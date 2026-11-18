# -*- coding: utf-8 -*-
"""Phase 6c v3: embed all chunks using requests.Session (persistent connection).
   Pre-resolves ai.ismc.ir via DoH and pins the IP to avoid per-call DNS.
   Resumable via chunks_state.json.
"""
import hashlib, json, re, subprocess, sys, time, os

# --- Pre-resolve ai.ismc.ir via DoH (local DNS is flaky) ---
import socket, urllib.request as _ur
def _doh_resolve(host):
    u = f"https://dns.google/resolve?name={host}&type=A"
    d = json.load(_ur.urlopen(_ur.Request(u, headers={"User-Agent": "m"}), timeout=10))
    ips = [a["data"] for a in d.get("Answer", []) if a.get("type") == 1]
    if not ips:
        raise RuntimeError(f"DoH no A for {host}")
    return ips
print("Resolving ai.ismc.ir via DoH...", flush=True)
_ISMC_IP = _doh_resolve("ai.ismc.ir")[0]
print(f"  -> {_ISMC_IP}", flush=True)

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Session with persistent connection to the resolved IP
# We connect to https://<IP> with SNI=ai.ismc.ir via Host header
# Simpler: patch socket.getaddrinfo to always return our IP for ai.ismc.ir
_orig_gai = socket.getaddrinfo
def _pinned_gai(host, port, *a, **kw):
    if host == "ai.ismc.ir":
        return [(socket.AF_INET, socket.SOCK_STREAM, 6, "", (_ISMC_IP, port))]
    return _orig_gai(host, port, *a, **kw)
socket.getaddrinfo = _pinned_gai

BASE = "https://ai.ismc.ir/api"
API_KEY = "sk-5K6TXne1qfnoiUWXvbQ0lg"
MODEL = "Qwen3-Embedding-4B"
EMBED_BATCH = 8
MAX_CHARS = 680
OVERLAP = 80
TOKEN_EST = 0.55

session = requests.Session()
adapter = HTTPAdapter(pool_connections=1, pool_maxsize=1,
                      max_retries=Retry(total=3, backoff_factor=2,
                                        status_forcelist=[500, 502, 503, 504]))
session.mount("https://", adapter)
session.headers.update({"Authorization": f"Bearer {API_KEY}",
                        "Content-Type": "application/json"})

def db_query(sql):
    r = subprocess.run(
        ['C:/Program Files/MySQL/MySQL Server 8.0/bin/mysql.exe',
         '--default-character-set=utf8mb4', '-u', 'root', '-p433700',
         'resaname_h', '-N', '-B', '-e', sql],
        capture_output=True, text=True, encoding='utf-8')
    if r.returncode != 0:
        print("DB ERROR:", r.stderr[:500]); sys.exit(1)
    return r.stdout

# --- load ---
print("Loading sections...", flush=True)
sections = []
for line in db_query(
    "SELECT document_id, id, section_key, IFNULL(section_title,''), "
    "REPLACE(REPLACE(REPLACE(content, '\\t', ' '), '\\n', ' '), '\\r', ' '), "
    "sort_order FROM ai_document_sections ORDER BY document_id, sort_order;"
).splitlines():
    p = line.split('\t')
    if len(p) >= 6:
        sections.append({'document_id': p[0], 'section_id': p[1],
                         'section_key': p[2], 'section_title': p[3],
                         'content': p[4], 'sort_order': int(p[5])})
print(f"  sections: {len(sections)}", flush=True)

summaries = {}
for line in db_query("SELECT id, IFNULL(summary,'') FROM ai_documents "
                     "WHERE summary IS NOT NULL AND summary != '';").splitlines():
    p = line.split('\t')
    if len(p) >= 2:
        summaries[p[0]] = p[1]
print(f"  docs with summary: {len(summaries)}", flush=True)

# --- chunker ---
SENT_END = re.compile(r'(?<=[.!?؟۔…])\s+')
def split_text(text, max_chars=MAX_CHARS, overlap=OVERLAP):
    text = text.strip()
    if len(text) <= max_chars:
        return [text] if text else []
    out, start, n = [], 0, len(text)
    while start < n:
        end = min(start + max_chars, n)
        if end < n:
            seg = text[start:end]
            m = None
            for m in SENT_END.finditer(seg): pass
            if m and m.start() >= max_chars * 0.5:
                end = start + m.end()
            else:
                sp = seg.rfind(' ')
                if sp >= max_chars * 0.4:
                    end = start + sp
        c = text[start:end].strip()
        if c: out.append(c)
        if end >= n: break
        start = max(end - overlap, start + 1)
    return out

by_doc = {}
for s in sections: by_doc.setdefault(s['document_id'], []).append(s)
chunks = []
for doc_id in sorted(by_doc):
    if doc_id in summaries and summaries[doc_id].strip():
        c = summaries[doc_id].strip()[:2000]
        chunks.append({'id': f'ch-{doc_id}-0', 'document_id': doc_id,
                       'section_id': None, 'section_key': 'summary',
                       'chunk_index': 0, 'content': c,
                       'token_count': int(len(c)/TOKEN_EST)})
    idx = 1
    for s in sorted(by_doc[doc_id], key=lambda x: x['sort_order']):
        for piece in split_text(s['content']):
            chunks.append({'id': f'ch-{doc_id}-{idx}', 'document_id': doc_id,
                           'section_id': s['section_id'],
                           'section_key': s['section_key'], 'chunk_index': idx,
                           'content': piece, 'token_count': int(len(piece)/TOKEN_EST)})
            idx += 1
print(f"total chunks: {len(chunks)}", flush=True)

# --- embed ---
def embed_batch(texts):
    r = session.post(BASE + "/v1/embeddings",
                     json={"model": MODEL, "input": texts}, timeout=120)
    r.raise_for_status()
    d = r.json()
    return [x['embedding'] for x in sorted(d['data'], key=lambda x: x['index'])]

# resume
state_file = 'chunks_state.json'
try:
    st = json.load(open(state_file, encoding='utf-8'))
    if st.get('chunk_ids') == [c['id'] for c in chunks]:
        vectors = st['vectors']
        print(f"resumed: {sum(1 for v in vectors if v)}/{len(chunks)} done", flush=True)
    else:
        raise ValueError("ids changed")
except Exception:
    vectors = [None] * len(chunks)
    print("fresh run", flush=True)

if any(v is None for v in vectors):
    t0 = time.time()
    n_batches = (len(chunks) + EMBED_BATCH - 1) // EMBED_BATCH
    for bi in range(n_batches):
        i0 = bi * EMBED_BATCH
        batch = chunks[i0:i0+EMBED_BATCH]
        if all(vectors[i0+j] is not None for j in range(len(batch))):
            continue
        try:
            vecs = embed_batch([c['content'] for c in batch])
            for j, v in enumerate(vecs):
                vectors[i0+j] = v
        except Exception as e:
            print(f"  batch {bi+1} error: {e}", flush=True)
            time.sleep(5)
            continue  # skip this batch, retry next pass
        if bi % 25 == 0 or bi == n_batches - 1:
            el = time.time() - t0
            done = sum(1 for v in vectors if v)
            rate = done / max(el, 1)
            eta = (len(chunks) - done) / max(rate, 0.01)
            print(f"  [{bi+1}/{n_batches}] {done}/{len(chunks)} "
                  f"({100*done/len(chunks):.1f}%)  {el:.0f}s  "
                  f"ETA {eta/60:.0f}min", flush=True)
            json.dump({'chunk_ids': [c['id'] for c in chunks], 'vectors': vectors},
                      open(state_file, 'w'))
    json.dump({'chunk_ids': [c['id'] for c in chunks], 'vectors': vectors},
              open(state_file, 'w'))
    print(f"embed complete: {sum(1 for v in vectors if v)}/{len(chunks)}", flush=True)

# --- write vectors.json + SQL ---
points = []
for c, v in zip(chunks, vectors):
    if v is None: continue
    points.append({'point_id': c['id'], 'vector': v, 'payload': {
        'document_id': c['document_id'], 'section_id': c['section_id'],
        'section_key': c['section_key'], 'chunk_index': c['chunk_index'],
        'content': c['content'], 'token_count': c['token_count'],
        'embedding_model': MODEL}})
json.dump(points, open('vectors.json', 'w', encoding='utf-8'))
print(f"wrote vectors.json: {len(points)} points", flush=True)

sql = ['-- Phase 6: ai_chunks upsert', 'USE resaname_h;', 'SET FOREIGN_KEY_CHECKS=0;', '']
def q(s): return s.replace('\\','\\\\').replace("'", "''")
for c in chunks:
    h = hashlib.sha256(c['content'].encode()).hexdigest()
    sec = "NULL" if c['section_id'] is None else f"'{q(c['section_id'])}'"
    sql.append(
        f"INSERT INTO ai_chunks (id, document_id, section_id, chunk_index, content, "
        f"content_hash, token_count, vector_point_id, embedding_model, embedding_version) "
        f"VALUES ('{c['id']}', '{q(c['document_id'])}', {sec}, {c['chunk_index']}, "
        f"'{q(c['content'])}', '{h}', {c['token_count']}, '{c['id']}', '{MODEL}', '1') "
        f"ON DUPLICATE KEY UPDATE content_hash='{h}', token_count={c['token_count']}, "
        f"vector_point_id='{c['id']}', embedding_model='{MODEL}', embedding_version='1';")
sql += ['', 'SET FOREIGN_KEY_CHECKS=1;', '-- verify: SELECT COUNT(*) FROM ai_chunks;']
open('load_chunks.sql', 'w', encoding='utf-8', newline='').write('\n'.join(sql))
print(f"wrote load_chunks.sql: {len(chunks)} rows", flush=True)
print("DONE", flush=True)
