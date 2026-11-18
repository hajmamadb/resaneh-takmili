# -*- coding: utf-8 -*-
"""Phase 6b+6c: chunk ai_document_sections (+ doc summary as chunk 0) into ai_chunks,
   then embed each chunk via ismc.ir and write vectors + SQL.

   DNS is flaky on this machine (ai.ismc.ir sometimes fails getaddrinfo) —
   patched socket.getaddrinfo to fall back to DoH (dns.google) for our host.

Design:
- chunk target: ~600-680 chars (≈400-700 tokens for Persian), overlap ~80 chars
- split on sentence boundaries (. ! ? ‼ … ) else word boundary
- chunk 0 of each doc = its summary (if present) so the title/summary is directly reachable
- chunk_id  = ch-<document_id>-<n>
- point_id  = same as chunk_id (1:1 mapping) — Qdrant payload carries document_id/section_id/title
- content_hash = SHA-256 of chunk content
- vector saved as JSON array to vectors.json; SQL upsert to ai_chunks with vector_point_id
"""
import hashlib
import json
import re
import subprocess
import sys
import urllib.request
import urllib.error
import time

BASE = "https://ai.ismc.ir/api"
API_KEY = "sk-5K6TXne1qfnoiUWXvbQ0lg"
MODEL = "Qwen3-Embedding-4B"
EMBED_BATCH = 8           # texts per API call (conservative for Qwen3-4B latency)
MAX_CHARS = 680           # target chunk length (chars)
OVERLAP = 80              # overlap chars between chunks
TOKEN_EST = 0.55          # chars per token estimate for Persian

# ---------- DoH DNS fallback for ai.ismc.ir ----------
import socket as _socket
_DOH_HOSTS = {"ai.ismc.ir"}
def _doh_resolve(host):
    u = f"https://dns.google/resolve?name={host}&type=A"
    d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent":"m"}), timeout=10))
    ips = [a["data"] for a in d.get("Answer", []) if a.get("type") == 1]
    if not ips:
        raise _socket.gaierror(f"DoH no A for {host}")
    return [(_socket.AF_INET, _socket.SOCK_STREAM, 6, "", (ip, 443)) for ip in ips]
_orig_gai = _socket.getaddrinfo
def _patched(host, port, *a, **kw):
    try:
        return _orig_gai(host, port, *a, **kw)
    except _socket.gaierror:
        if host in _DOH_HOSTS:
            return _doh_resolve(host)
        raise
_socket.getaddrinfo = _patched

# ---------- load sections + summaries from DB ----------
def db_query(sql):
    r = subprocess.run(
        ['C:/Program Files/MySQL/MySQL Server 8.0/bin/mysql.exe', '--default-character-set=utf8mb4',
         '-u', 'root', '-p433700', 'resaname_h', '-N', '-B', '-e', sql],
        capture_output=True, text=True, encoding='utf-8'
    )
    if r.returncode != 0:
        print("DB ERROR:", r.stderr[:500])
        sys.exit(1)
    return r.stdout

print("Loading sections...")
# Use tab-separated; section content may contain newlines? content is mediumtext single-line in seed.
# NOTE: column is `id` (section PK), not `section_id`
sections = []
rows2 = db_query(
    "SELECT document_id, id, section_key, IFNULL(section_title,''), "
    "REPLACE(REPLACE(REPLACE(content, '\\t', ' '), '\\n', ' '), '\\r', ' '), "
    "sort_order FROM ai_document_sections ORDER BY document_id, sort_order;"
)
for line in rows2.splitlines():
    parts = line.split('\t')
    if len(parts) >= 6:
        sections.append({
            'document_id': parts[0],
            'section_id': parts[1],
            'section_key': parts[2],
            'section_title': parts[3],
            'content': parts[4],
            'sort_order': int(parts[5]),
        })
print(f"  sections loaded: {len(sections)}")

summaries = {}
for line in db_query(
    "SELECT id, IFNULL(summary,'') FROM ai_documents WHERE summary IS NOT NULL AND summary != '';"
).splitlines():
    parts = line.split('\t')
    if len(parts) >= 2:
        summaries[parts[0]] = parts[1]
print(f"  docs with summary: {len(summaries)}")

# ---------- chunker ----------
SENT_END = re.compile(r'(?<=[.!?؟۔…])\s+')

def split_text(text, max_chars=MAX_CHARS, overlap=OVERLAP):
    text = text.strip()
    if len(text) <= max_chars:
        return [text] if text else []
    chunks = []
    start = 0
    n = len(text)
    while start < n:
        end = min(start + max_chars, n)
        if end < n:
            # try to end at a sentence boundary within the window
            seg = text[start:end]
            m = None
            for m in SENT_END.finditer(seg):
                pass
            if m and m.start() >= max_chars * 0.5:
                end = start + m.end()
            else:
                # else break at last space
                sp = seg.rfind(' ')
                if sp >= max_chars * 0.4:
                    end = start + sp
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        if end >= n:
            break
        start = max(end - overlap, start + 1)
    return chunks

# build chunks list
chunks = []  # dicts: id, document_id, section_id, section_key, chunk_index, content, token_count
sections_by_doc = {}
for s in sections:
    sections_by_doc.setdefault(s['document_id'], []).append(s)

for doc_id in sorted(sections_by_doc):
    # chunk 0: summary
    if doc_id in summaries and summaries[doc_id].strip():
        c = summaries[doc_id].strip()
        chunks.append({
            'id': f'ch-{doc_id}-0',
            'document_id': doc_id, 'section_id': None,
            'section_key': 'summary', 'chunk_index': 0,
            'content': c[:2000],
            'token_count': int(len(c) / TOKEN_EST),
        })
    idx = 1
    group = sections_by_doc[doc_id]
    for s in sorted(group, key=lambda x: x['sort_order']):
        for piece in split_text(s['content']):
            chunks.append({
                'id': f'ch-{doc_id}-{idx}',
                'document_id': doc_id, 'section_id': s['section_id'],
                'section_key': s['section_key'], 'chunk_index': idx,
                'content': piece,
                'token_count': int(len(piece) / TOKEN_EST),
            })
            idx += 1

print(f"total chunks: {len(chunks)}")

# ---------- embedding ----------
def embed_batch(texts, retries=5):
    last = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(
                BASE + "/v1/embeddings",
                headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
                data=json.dumps({"model": MODEL, "input": texts}).encode('utf-8'),
                method="POST",
            )
            with urllib.request.urlopen(req, timeout=90) as r:
                d = json.load(r)
            return [x['embedding'] for x in sorted(d['data'], key=lambda x: x['index'])]
        except Exception as e:
            last = e
            wait = 3 * (attempt + 1)
            print(f"  embed attempt {attempt+1} failed ({e}); sleeping {wait}s")
            time.sleep(wait)
    raise last

def embed_all(texts, resume_from=0):
    vectors = [None] * len(texts)
    t0 = time.time()
    for i in range(resume_from, len(texts), EMBED_BATCH):
        batch = texts[i:i+EMBED_BATCH]
        vecs = embed_batch(batch)
        for j, v in enumerate(vecs):
            vectors[i+j] = v
        done = i + len(batch)
        if done % (EMBED_BATCH*10) == 0 or done == len(texts):
            el = time.time()-t0
            print(f"  embedded {done}/{len(texts)}  ({el:.0f}s)")
    return vectors

# resume support
state_file = 'chunks_state.json'
try:
    st = json.load(open(state_file, encoding='utf-8'))
    if st.get('chunk_ids') == [c['id'] for c in chunks]:
        vectors = st['vectors']
        print(f"resumed vectors: {sum(1 for v in vectors if v)}/{len(chunks)}")
    else:
        raise ValueError("chunk ids changed")
except Exception:
    vectors = [None] * len(chunks)
    print("fresh embed run")

if any(v is None for v in vectors):
    # Only send chunks whose vector is still missing; keep already-done ones.
    todo_idx = [i for i, v in enumerate(vectors) if v is None]
    print(f"embedding {len(todo_idx)} missing chunks...")
    for k, i in enumerate(todo_idx, 1):
        try:
            vectors[i] = embed_batch([chunks[i]['content']])[0]
        except Exception as e:
            print(f"  chunk {i} ({chunks[i]['id']}) failed permanently: {e}")
        if k % 100 == 0:
            print(f"  progress {k}/{len(todo_idx)}")
            json.dump({'chunk_ids': [c['id'] for c in chunks], 'vectors': vectors},
                      open(state_file, 'w'))
    json.dump({'chunk_ids': [c['id'] for c in chunks], 'vectors': vectors},
              open(state_file, 'w'))
    print("saved vectors to chunks_state.json")

# ---------- write vectors.json + SQL ----------
# vectors.json: list of {point_id, vector, payload}
points = []
for c, v in zip(chunks, vectors):
    points.append({
        'point_id': c['id'],
        'vector': v,
        'payload': {
            'document_id': c['document_id'],
            'section_id': c['section_id'],
            'section_key': c['section_key'],
            'chunk_index': c['chunk_index'],
            'content': c['content'],
            'token_count': c['token_count'],
            'embedding_model': MODEL,
        },
    })
json.dump(points, open('vectors.json', 'w', encoding='utf-8'))
print(f"wrote vectors.json: {len(points)} points, dim={len(vectors[0]) if vectors[0] else 0}")

# SQL for ai_chunks
sql = ['-- Phase 6: ai_chunks upsert (document_id, chunk_index) ',
       'USE resaname_h;', 'SET FOREIGN_KEY_CHECKS = 0;', '']
def q(s):
    return s.replace('\\', '\\\\').replace("'", "''")
for c in chunks:
    h = hashlib.sha256(c['content'].encode('utf-8')).hexdigest()
    sec = "NULL" if c['section_id'] is None else f"'{q(c['section_id'])}'"
    sql.append(
        f"INSERT INTO ai_chunks (id, document_id, section_id, chunk_index, content, content_hash, "
        f"token_count, vector_point_id, embedding_model, embedding_version) "
        f"VALUES ('{c['id']}', '{q(c['document_id'])}', {sec}, {c['chunk_index']}, "
        f"'{q(c['content'])}', '{h}', {c['token_count']}, '{c['id']}', '{MODEL}', '1') "
        f"ON DUPLICATE KEY UPDATE content_hash='{h}', token_count={c['token_count']}, "
        f"vector_point_id='{c['id']}', embedding_model='{MODEL}', embedding_version='1';"
    )
sql += ['', 'SET FOREIGN_KEY_CHECKS = 1;', '', '-- verify:',
        "-- SELECT COUNT(*) FROM ai_chunks;"]
open('load_chunks.sql', 'w', encoding='utf-8', newline='').write('\n'.join(sql))
print(f"wrote load_chunks.sql: {len(chunks)} rows")
