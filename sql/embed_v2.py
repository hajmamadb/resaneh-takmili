# -*- coding: utf-8 -*-
"""Phase 6c v2: embed all 11313 chunks, batched, with per-batch progress.
   No DoH patch (local DNS works now). Resumable via chunks_state.json.
"""
import hashlib, json, re, subprocess, sys, time, urllib.request
import socket as _socket

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

BASE = "https://ai.ismc.ir/api"
API_KEY = "sk-5K6TXne1qfnoiUWXvbQ0lg"
MODEL = "Qwen3-Embedding-4B"
EMBED_BATCH = 8
MAX_CHARS = 680
OVERLAP = 80
TOKEN_EST = 0.55

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
        texts = [c['content'] for c in batch]
        # skip batches already done
        if all(vectors[i0+j] is not None for j in range(len(batch))):
            continue
        try:
            vecs = embed_batch(texts)
            for j, v in enumerate(vecs):
                vectors[i0+j] = v
        except Exception as e:
            print(f"  batch {bi} FAILED: {e}", flush=True)
        if bi % 50 == 0 or bi == n_batches - 1:
            el = time.time() - t0
            done = sum(1 for v in vectors if v)
            eta = (el / max(done,1)) * (len(chunks) - done) if done else 0
            print(f"  batch {bi+1}/{n_batches}  done {done}/{len(chunks)}  "
                  f"{el:.0f}s elapsed  ETA {eta/60:.0f}min", flush=True)
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
