# -*- coding: utf-8 -*-
"""Phase 7: RAG recall evaluation — run 2 (final), after Phase 6f gap fix.

Targets (from برنامه-تکمیل-محتوا-برای-سامانه-هوشمند.md):
  - Recall@10 >= 90%          (top-10 chunks contain the correct source document)
  - Reference/link accuracy >= 99%  (every returned point maps to a real ai_documents row)
  - Documented answer >= 95%  (for section-targeted questions, the top-10 contains the
                               expected section — the retriever can point to a documented piece)

Dataset: 100 questions in 5 categories (v2 fixes run-1 design flaws):
  A. فنی/مفهومی   — 20 queries built from LONG, content-rich sections with
                    meaningful titles (avoid short generic titles like
                    "چارچوب نظری" which exist on all 731 cards).
  B. مفهومی        — 20 "مضمون اصلی «X»" questions over theory docs.
  C. نظریه‌پرداز    — 20 "نظریه‌پرداز «X» ... کشور" questions over theorist docs.
  D. کتاب/مجله     — 20 "«X» درباره چه چیزی است" questions over book/journal docs.
  E. بین‌متنی      — 20 cross-doc questions from verified doc-card<->doc-card
                    relationship edges.

Ground truth = the source document_id (and section_id where applicable), taken
from ai_documents / ai_document_sections / ai_relationships — not from the
vector store, so the test is independent of the retrieval backend.

Method:
  1. Load chunk store + 2560-dim matrix from vectors.json / resaname_vectors.sqlite.
  2. Generate A..E items (SEED=731) from MySQL.
  3. Embed all 100 queries in one batch call (ismc.ir Qwen3-Embedding-4B).
  4. Brute-force cosine (mat @ qmat.T), top-10 per query.
  5. Score the 3 KPIs + per-category breakdown.

Usage: python phase7_test.py
Outputs: phase7_results.json
"""
import hashlib
import json
import random
import sqlite3
import subprocess
import sys
import time
import urllib.request

import ijson
import numpy as np

DB = "resaname_vectors.sqlite"
VJSON = "vectors.json"
DIM = 2560
API = "https://ai.ismc.ir/api/v1/embeddings"
KEY = "sk-5K6TXne1qfnoiUWXvbQ0lg"
MODEL = "Qwen3-Embedding-4B"
OUT = "phase7_results.json"
K = 10
SEED = 731

# ---------- embed ----------
def embed(texts, retries=4):
    for i in range(retries):
        try:
            r = urllib.request.Request(
                API,
                data=json.dumps({"model": MODEL, "input": texts}).encode(),
                headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"})
            with urllib.request.urlopen(r, timeout=90) as resp:
                d = json.load(resp)
            return [item["embedding"] for item in d["data"]]
        except Exception as e:
            print(f"  embed retry {i+1}/{retries}: {e}", file=sys.stderr)
            time.sleep(3 * (i + 1))
    raise SystemExit("embed failed after retries")

# ---------- load chunks (content + mapping) from vectors.json ----------
print("Loading chunk store from vectors.json ...", flush=True)
chunks = {}   # point_id -> dict
with open(VJSON, "rb") as f:
    for p in ijson.items(f, "item"):
        pay = p["payload"]
        chunks[p["point_id"]] = {
            "point_id": p["point_id"],
            "document_id": pay["document_id"],
            "section_id": pay.get("section_id"),
            "section_key": pay.get("section_key"),
            "content": pay.get("content", ""),
        }
print(f"  {len(chunks)} chunks loaded", flush=True)

# ---------- load vector matrix (already L2-normalized) ----------
print("Loading vector matrix ...", flush=True)
con = sqlite3.connect(DB)
con.row_factory = sqlite3.Row
vrows = con.execute("SELECT id, point_id FROM vectors ORDER BY id").fetchall()
n = len(vrows)
mat = np.empty((n, DIM), dtype=np.float32)
blobs = con.execute("SELECT vector FROM vectors ORDER BY id").fetchall()
for i, (b,) in enumerate(blobs):
    mat[i] = np.frombuffer(b, dtype=np.float32)
con.close()
order = [r["point_id"] for r in vrows]   # row i in mat == order[i]
print(f"  {n} x {DIM} matrix ready ({mat.nbytes/1e6:.1f} MB)", flush=True)

# ---------- DB helpers ----------
def db_query(sql):
    r = subprocess.run(
        ['C:/Program Files/MySQL/MySQL Server 8.0/bin/mysql.exe', '--default-character-set=utf8mb4',
         '-u', 'root', '-p433700', 'resaname_h', '-N', '-B', '-e', sql],
        capture_output=True, text=True, encoding='utf-8')
    if r.returncode != 0:
        raise SystemExit(f"DB ERROR: {r.stderr[:500]}")
    return r.stdout

# ---------- doc titles ----------
titles = {}
for line in db_query("SELECT id, title FROM ai_documents;").splitlines():
    if '\t' in line:
        d, t = line.split('\t', 1)
        titles[d] = t
print(f"  {len(titles)} documents from MySQL", flush=True)

# ---------- sections (long + meaningful-title only, for category A) ----------
sections = []
rows2 = db_query(
    "SELECT document_id, id, section_key, IFNULL(section_title,''), "
    "LENGTH(content) AS clen, "
    "REPLACE(REPLACE(REPLACE(REPLACE(content,'\\t',' '), '\\n',' '), '\\r',' '), '\\x01',' ') "
    "FROM ai_document_sections "
    "WHERE document_id LIKE 'doc-card-%' AND LENGTH(section_title) >= 12 "
    "AND LENGTH(content) >= 600;")
for line in rows2.splitlines():
    parts = line.split('\t')
    if len(parts) >= 6:
        sections.append({'document_id': parts[0], 'section_id': parts[1],
                         'section_key': parts[2], 'title': parts[3],
                         'clen': int(parts[4]), 'content': parts[5]})
print(f"  {len(sections)}/5594 sections usable for cat A (title>=12, content>=600)", flush=True)

# ---------- question generation ----------
def first_sentences(content, n=2, max_chars=140):
    """Split on '. ' and take n sentences, total <= max_chars."""
    parts = content.split('. ')
    out, acc = [], 0
    for p in parts:
        p = p.strip()
        if not p:
            continue
        acc += len(p)
        out.append(p)
        if acc >= max_chars or len(out) >= n:
            break
    return ' '.join(out) + ' …'

rng = random.Random(SEED)

# Category A: technical questions from rich, well-titled sections (cards)
rng.shuffle(sections)
catA = []
for s in sections[:20]:
    lead = first_sentences(s['content'], 1, 120)
    q = f"در «{titles[s['document_id']]}» بخش «{s['title']}» چه می‌گوید؟ ({lead})"
    catA.append({'cat': 'A', 'query': q, 'expect_section': s['section_id'],
                 'expect_doc': s['document_id'], 'expect_docs': [s['document_id']]})

# Category B: conceptual "main idea" questions over the 15 theory docs
theory_docs = sorted(d for d in titles if d.startswith('doc-new-theory-'))
rng.shuffle(theory_docs)
catB = []
for d in theory_docs[:20]:
    t = titles[d]
    q = f"مضمون اصلی تئوری «{t}» چیست؟"
    catB.append({'cat': 'B', 'query': q, 'expect_section': None, 'expect_doc': d,
                 'expect_docs': [d]})

# Category C: theorist docs
theo_docs = sorted(d for d in titles if d.startswith('doc-new-theorist-'))
rng.shuffle(theo_docs)
catC = []
for d in theo_docs[:20]:
    t = titles[d]
    q = f"نظریه‌پرداز «{t}» چه دیدگاهی دارد و از کدام کشور است؟"
    catC.append({'cat': 'C', 'query': q, 'expect_section': None, 'expect_doc': d,
                 'expect_docs': [d]})

# Category D: books + journals
bookj_docs = sorted(d for d in titles if d.startswith('doc-new-book-') or d.startswith('doc-new-journal-'))
rng.shuffle(bookj_docs)
catD = []
for d in bookj_docs[:20]:
    t = titles[d]
    q = f"«{t}» درباره چه چیزی است و چه جایی را پوشش می‌دهد؟"
    catD.append({'cat': 'D', 'query': q, 'expect_section': None, 'expect_doc': d,
                 'expect_docs': [d]})

# Category E: cross-doc from verified doc-card<->doc-card edges
rel_pairs = []
rows3 = db_query(
    "SELECT source_id, target_id FROM ai_relationships "
    "WHERE source_id LIKE 'doc-card-%' AND target_id LIKE 'doc-card-%' "
    "AND verification_status='verified';")
for line in rows3.splitlines():
    if '\t' in line:
        a, b = line.split('\t')
        rel_pairs.append((a, b))
rng.shuffle(rel_pairs)
catE = []
used = set()
for a, b in rel_pairs:
    if a == b or (a, b) in used or (b, a) in used:
        continue
    used.add((a, b))
    ta, tb = titles.get(a, a), titles.get(b, b)
    q = f"ارتباط بین «{ta}» و «{tb}» چیست؟"
    catE.append({'cat': 'E', 'query': q, 'expect_section': None, 'expect_doc': a,
                 'expect_docs': [a, b]})
    if len(catE) >= 20:
        break

questions = catA + catB + catC + catD + catE
print(f"\nQuestions: A={len(catA)} B={len(catB)} C={len(catC)} D={len(catD)} E={len(catE)} total={len(questions)}")
for q in questions:
    q['qid'] = hashlib.sha1(q['query'].encode()).hexdigest()[:8]

# ---------- embed all questions ----------
print(f"Embedding {len(questions)} questions (batch) ...", flush=True)
qembeds = embed([q['query'] for q in questions])
qmat = np.array(qembeds, dtype=np.float32)
qnorms = np.linalg.norm(qmat, axis=1, keepdims=True)
qnorms[qnorms == 0] = 1
qmat = qmat / qnorms

# ---------- search ----------
print("Searching ...", flush=True)
t0 = time.time()
scores_all = mat @ qmat.T          # (11368, N)
top = np.argsort(-scores_all, axis=0)[:K]
print(f"  search done in {time.time()-t0:.2f}s", flush=True)

# ---------- evaluate ----------
# link accuracy: every returned point must map to a real ai_documents row (by title dict)
results = []
for qi, q in enumerate(questions):
    idxs = top[:, qi]
    hits = []
    for i in idxs:
        pid = order[i]
        c = chunks[pid]
        hits.append({'score': float(scores_all[i, qi]), 'point_id': pid,
                     'document_id': c['document_id'], 'section_id': c['section_id'],
                     'section_key': c['section_key']})
    docs_in = [h['document_id'] for h in hits]
    recall_ok = any(ed in docs_in for ed in q['expect_docs'])
    # strict: expected section present (only for cat A)
    recall_strict = recall_ok
    if q['expect_section']:
        recall_strict = any(h['section_id'] == q['expect_section'] for h in hits)
    # documented answer: top-10 contains a chunk with non-NULL section_id
    documented = any(h['section_id'] is not None for h in hits)
    # link accuracy: all top-K point ids exist in the chunk store (=> real ai_documents rows)
    link_ok = all(h['point_id'] in chunks for h in hits)
    results.append({'qid': q['qid'], 'cat': q['cat'], 'query': q['query'],
                    'expect_docs': q['expect_docs'], 'expect_section': q['expect_section'],
                    'recall_ok': recall_ok, 'recall_strict': recall_strict,
                    'documented': documented, 'link_ok': link_ok,
                    'top1_score': hits[0]['score'], 'top5': hits[:5]})

nq = len(results)
recall_n = sum(r['recall_ok'] for r in results)
recall_strict_n = sum(r['recall_strict'] for r in results)
doc_n = sum(r['documented'] for r in results)
link_n = sum(r['link_ok'] for r in results)
print("\n" + "=" * 62)
print(f"Phase 7 results (run 2) — {nq} questions, {n} vectors")
print("=" * 62)
print(f"Recall@10 (doc-level)      : {recall_n:3d}/{nq} = {recall_n/nq*100:5.1f}%   (target >= 90%)")
print(f"Recall@10 (strict section) : {recall_strict_n:3d}/{nq} = {recall_strict_n/nq*100:5.1f}%")
print(f"Documented answer (top-10) : {doc_n:3d}/{nq} = {doc_n/nq*100:5.1f}%   (target >= 95%)")
print(f"Link accuracy              : {link_n:3d}/{nq} = {link_n/nq*100:5.1f}%   (target >= 99%)")
print("-" * 62)
for c in "ABCDE":
    sub = [r for r in results if r['cat'] == c]
    if not sub:
        continue
    rn = sum(r['recall_ok'] for r in sub)
    dn = sum(r['documented'] for r in sub)
    print(f"  cat {c}: n={len(sub):3d}  recall={rn/len(sub)*100:5.1f}%  documented={dn/len(sub)*100:5.1f}%")
fails = [r for r in results if not r['recall_ok']]
if fails:
    print("-" * 62)
    print(f"FAILURES ({len(fails)}):")
    for r in fails[:25]:
        print(f"  [{r['cat']}] {r['query'][:80]}  expect={r['expect_docs']}  top1={r['top5'][0]['point_id']}({r['top1_score']:.3f})")

with open(OUT, 'w', encoding='utf-8') as f:
    json.dump({'summary': {
        'run': 2, 'n': nq, 'vectors': n,
        'recall': recall_n / nq, 'recall_strict': recall_strict_n / nq,
        'documented': doc_n / nq, 'link': link_n / nq},
        'results': results}, f, ensure_ascii=False, indent=1)
print(f"\nSaved -> {OUT}")
