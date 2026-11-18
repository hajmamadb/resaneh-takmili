# -*- coding: utf-8 -*-
"""resaname_v2 gap fix: 12 Phase-4 contents (book 21/22, journal 16-20,
theorist 21-25) have sections but ZERO chunks/vectors.

For each of the 12 contents:
  1. build chunks (summary chunk ch-<cid>-0 + per-section chunks ch-<cid>-N)
     using the exact chunker from embed_v2.py (MAX_CHARS=680, OVERLAP=80)
  2. embed via ai.ismc.ir (Qwen3-Embedding-4B, 2560-dim) with DoH fallback
  3. insert into resaname_v2.chunks (content_id / section_id)
  4. append to resaname_vectors.sqlite (L2-normalized float32)
  5. append to vectors.json (source of truth)
Resumable via state file gap_v2_12_state.json (vectors cached if ids match).
"""
import hashlib, json, os, sqlite3, sys, time, urllib.request
import socket as _socket

import numpy as np

BASE = "https://ai.ismc.ir/api"
API_KEY = "sk-5K6TXne1qfnoiUWXvbQ0lg"
MODEL = "Qwen3-Embedding-4B"
DIM = 2560
EMBED_BATCH = 8
MAX_CHARS = 680
OVERLAP = 80
TOKEN_EST = 0.55
VJSON = os.path.join(os.path.dirname(os.path.abspath(__file__)), "vectors.json")
VDB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "resaname_vectors.sqlite")
STATE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "gap_v2_12_state.json")

TWELVE = [
    'doc-new-book-21', 'doc-new-book-22',
    'doc-new-journal-16', 'doc-new-journal-17', 'doc-new-journal-18',
    'doc-new-journal-19', 'doc-new-journal-20',
    'doc-new-theorist-21', 'doc-new-theorist-22', 'doc-new-theorist-23',
    'doc-new-theorist-24', 'doc-new-theorist-25',
]

# ---- DoH fallback for ai.ismc.ir (local DNS is flaky) ----
_DOH_HOSTS = {"ai.ismc.ir"}
def _doh_resolve(host):
    u = f"https://dns.google/resolve?name={host}&type=A"
    d = json.load(urllib.request.urlopen(
        urllib.request.Request(u, headers={"User-Agent": "m"}), timeout=10))
    ips = [a["data"] for a in d.get("Answer", []) if a.get("type") == 1]
    if not ips:
        raise _socket.gaierror(f"DoH no A for {host}")
    return [(_socket.AF_INET, _socket.SOCK_STREAM, 6, "", (ip, 443)) for ip in ips]
_orig_gai = _socket.getaddrinfo
def _patched_gai(host, port, *a, **kw):
    try:
        return _orig_gai(host, port, *a, **kw)
    except _socket.gaierror:
        if host in _DOH_HOSTS:
            return _doh_resolve(host)
        raise
_socket.getaddrinfo = _patched_gai

import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', password='433700',
                       database='resaname_v2', charset='utf8mb4')
cur = conn.cursor()

# --- 1. load sections for the 12 contents (ordered) ---
ph = ','.join(['%s'] * len(TWELVE))
cur.execute(
    "SELECT id, content_id, section_key, IFNULL(section_title,''), content, sort_order "
    "FROM sections WHERE content_id IN (" + ph + ") ORDER BY content_id, sort_order",
    TWELVE)
sections = [{'id': r[0], 'content_id': r[1], 'section_key': r[2],
             'section_title': r[3], 'content': r[4], 'sort_order': r[5]}
            for r in cur.fetchall()]
print(f"sections loaded for 12 contents: {len(sections)}", flush=True)

# --- 2. summaries for chunk-0 ---
cur.execute(
    "SELECT id, IFNULL(summary,'') FROM contents WHERE id IN (" + ph + ")", TWELVE)
summaries = {r[0]: (r[1] or '').strip() for r in cur.fetchall()}

# --- chunker (identical to embed_v2.py) ---
import re
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
            for m in SENT_END.finditer(seg):
                pass
            if m and m.start() >= max_chars * 0.5:
                end = start + m.end()
            else:
                sp = seg.rfind(' ')
                if sp >= max_chars * 0.4:
                    end = start + sp
        c = text[start:end].strip()
        if c:
            out.append(c)
        if end >= n:
            break
        start = max(end - overlap, start + 1)
    return out

by_doc = {}
for s in sections:
    by_doc.setdefault(s['content_id'], []).append(s)
chunks = []
for cid in TWELVE:  # fixed order -> deterministic chunk ids
    if cid in summaries and summaries[cid]:
        c = summaries[cid][:2000]
        chunks.append({'id': f'ch-{cid}-0', 'content_id': cid,
                       'section_id': None, 'section_key': 'summary',
                       'chunk_index': 0, 'content': c,
                       'token_count': int(len(c) / TOKEN_EST)})
    idx = 1
    for s in sorted(by_doc.get(cid, []), key=lambda x: x['sort_order']):
        for piece in split_text(s['content']):
            chunks.append({'id': f'ch-{cid}-{idx}', 'content_id': cid,
                           'section_id': s['id'], 'section_key': s['section_key'],
                           'chunk_index': idx, 'content': piece,
                           'token_count': int(len(piece) / TOKEN_EST)})
            idx += 1
print(f"total chunks to create: {len(chunks)}", flush=True)
for cid in TWELVE:
    print(f"  {cid}: {sum(1 for c in chunks if c['content_id']==cid)} chunks", flush=True)

# --- 3. embed (with resume) ---
def embed_batch(texts, retries=6):
    last = None
    for attempt in range(retries):
        t0 = time.time()
        try:
            req = urllib.request.Request(
                BASE + "/v1/embeddings",
                headers={"Authorization": f"Bearer {API_KEY}",
                         "Content-Type": "application/json"},
                data=json.dumps({"model": MODEL, "input": texts}).encode(),
                method="POST")
            with urllib.request.urlopen(req, timeout=120) as r:
                d = json.load(r)
            return [x['embedding'] for x in sorted(d['data'], key=lambda x: x['index'])]
        except Exception as e:
            last = e
            wait = 5 * (attempt + 1)
            print(f"  embed attempt {attempt+1} failed ({e}) after {time.time()-t0:.0f}s; sleep {wait}s", flush=True)
            time.sleep(wait)
    raise last

try:
    st = json.load(open(STATE, encoding='utf-8'))
    if st.get('ids') == [c['id'] for c in chunks]:
        vectors = st['vectors']
        print(f"resumed: {sum(1 for v in vectors if v)}/{len(vectors)} cached", flush=True)
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
        batch = chunks[i0:i0 + EMBED_BATCH]
        if all(vectors[i0 + j] is not None for j in range(len(batch))):
            continue
        vecs = embed_batch([c['content'] for c in batch])
        for j, v in enumerate(vecs):
            vectors[i0 + j] = v
        if bi % 5 == 0 or bi == n_batches - 1:
            done = sum(1 for v in vectors if v)
            el = time.time() - t0
            print(f"  batch {bi+1}/{n_batches} done {done}/{len(chunks)} {el:.0f}s", flush=True)
        json.dump({'ids': [c['id'] for c in chunks], 'vectors': vectors},
                  open(STATE, 'w', encoding='utf-8'), ensure_ascii=False)
assert all(vectors), f"missing vectors: {sum(1 for v in vectors if v is None)}"

# --- 4. MySQL resaname_v2.chunks (INSERT IGNORE, idempotent) ---
def esc(s):
    return s.replace('\\', '\\\\').replace("'", "''")
sql_lines = []
for c in chunks:
    h = hashlib.sha256(c['content'].encode()).hexdigest()
    sec = "NULL" if c['section_id'] is None else f"'{esc(c['section_id'])}'"
    sql_lines.append(
        "INSERT IGNORE INTO chunks (id, content_id, section_id, chunk_index, content, "
        f"content_hash, token_count, vector_point_id, embedding_model, embedding_version) "
        f"VALUES ('{c['id']}', '{esc(c['content_id'])}', {sec}, {c['chunk_index']}, "
        f"'{esc(c['content'])}', '{h}', {c['token_count']}, '{c['id']}', '{MODEL}', 'v1');")
tmp_sql = os.path.join(os.path.dirname(os.path.abspath(__file__)), "gap_v2_12_chunks.sql")
with open(tmp_sql, "w", encoding="utf-8") as f:
    f.write("\n".join(sql_lines))
r = __import__('subprocess').run(
    ['C:/Program Files/MySQL/MySQL Server 8.0/bin/mysql.exe',
     '--default-character-set=utf8mb4', '-u', 'root', '-p433700', 'resaname_v2'],
    stdin=open(tmp_sql, "rb"), capture_output=True, text=True, encoding='utf-8')
if r.returncode != 0:
    raise SystemExit(f"mysql insert failed: {r.stderr[:500]}")
print(f"chunks: {len(chunks)} rows INSERTed (ignore existing)", flush=True)

# --- 5. SQLite vector store (append, L2-normalized float32) ---
con = sqlite3.connect(VDB)
n = con.execute("SELECT MAX(id) FROM vectors").fetchone()[0] or 0
rows = []
for c, v in zip(chunks, vectors):
    vec = np.array(v, dtype=np.float32)
    norm = np.linalg.norm(vec)
    if norm > 0:
        vec = vec / norm
    rows.append((n + len(rows) + 1, c['id'], c['content_id'], c['section_id'], vec.tobytes()))
con.executemany(
    "INSERT OR REPLACE INTO vectors (id, point_id, document_id, section_id, vector) VALUES (?,?,?,?,?)",
    rows)
con.execute("INSERT OR REPLACE INTO meta VALUES ('count', ?)", (str(n + len(rows)),))
con.commit()
con.close()
print(f"sqlite updated: {len(rows)} vectors appended (new count {n + len(rows)})", flush=True)

# --- 6. append to vectors.json (source of truth) ---
data = open(VJSON, "rb").read()
assert data.rstrip().endswith(b']'), "vectors.json does not end with ']'"
objs = []
for c, v in zip(chunks, vectors):
    objs.append({
        "point_id": c['id'],
        "vector": [float(x) for x in v],
        "payload": {
            "document_id": c['content_id'],
            "section_id": c['section_id'],
            "section_key": c['section_key'],
            "chunk_index": c['chunk_index'],
            "content": c['content'],
            "token_count": c['token_count'],
            "embedding_model": MODEL,
        },
    })
joined = ",".join(json.dumps(o, ensure_ascii=False) for o in objs)
out = open(VJSON + ".tmp", "wb")
out.write(data[:-1])
out.write(b"," + joined.encode("utf-8") + b"]")
out.close()
os.replace(VJSON + ".tmp", VJSON)
print(f"appended {len(chunks)} points to {os.path.basename(VJSON)}", flush=True)

conn.close()
print(f"DONE: 12 contents / {len(chunks)} chunks embedded + stored (mysql + sqlite + vectors.json)", flush=True)
