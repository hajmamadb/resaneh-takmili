# -*- coding: utf-8 -*-
"""Phase 6f gap fix: 55 Phase-4 docs (theorist 20 + book 20 + journal 15) have
NO ai_document_sections rows — only an ai_documents.summary. The original
build_chunks.py only chunked docs that had sections, so these 55 were skipped
entirely (not in ai_chunks, not in vectors.json).

Fix: for each of the 55 docs, create chunk ch-<doc>-0 from its summary,
embed via ismc.ir (Qwen3-Embedding-4B), append to vectors.json, insert into
ai_chunks (MySQL), and add to resaname_vectors.sqlite (L2-normalized float32).
"""
import hashlib, json, sqlite3, subprocess, sys, time, urllib.request

import ijson
import numpy as np

BASE = "https://ai.ismc.ir/api"
API_KEY = "sk-5K6TXne1qfnoiUWXvbQ0lg"
MODEL = "Qwen3-Embedding-4B"
DIM = 2560
EMBED_BATCH = 8
TOKEN_EST = 0.55
VJSON = "vectors.json"
VDB = "resaname_vectors.sqlite"
STATE = "gap55_state.json"

def db_query(sql):
    r = subprocess.run(
        ['C:/Program Files/MySQL/MySQL Server 8.0/bin/mysql.exe', '--default-character-set=utf8mb4',
         '-u', 'root', '-p433700', 'resaname_h', '-N', '-B', '-e', sql],
        capture_output=True, text=True, encoding='utf-8')
    if r.returncode != 0:
        raise SystemExit(f"DB ERROR: {r.stderr[:500]}")
    return r.stdout

# --- 1. find the 55 missing docs (have summary, no chunks in vectors.json) ---
docs = {}
for line in db_query("SELECT id, IFNULL(summary,''), LEFT(title,0) FROM ai_documents WHERE id LIKE 'doc-new-%';").splitlines():
    parts = line.split('\t')
    if len(parts) >= 2:
        docs[parts[0]] = parts[1].strip()

existing = set()
with open(VJSON, "rb") as f:
    for p in ijson.items(f, "item"):
        existing.add(p["payload"]["document_id"])

missing = sorted(d for d, s in docs.items() if s and d not in existing)
print(f"docs with summary, missing from vectors.json: {len(missing)}")
assert len(missing) == 55, f"expected 55, got {len(missing)}"

# --- 2. build chunks (one summary chunk each) ---
chunks = []
for d in missing:
    c = docs[d][:2000]
    chunks.append({
        'id': f'ch-{d}-0',
        'document_id': d, 'section_id': None,
        'section_key': 'summary', 'chunk_index': 0,
        'content': c,
        'token_count': int(len(c) / TOKEN_EST),
        'content_hash': hashlib.sha256(c.encode('utf-8')).hexdigest(),
    })
print(f"chunks to create: {len(chunks)}")

# --- 3. embed (with resume state) ---
def embed_batch(texts, retries=5):
    last = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(
                BASE + "/v1/embeddings",
                headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
                data=json.dumps({"model": MODEL, "input": texts}).encode('utf-8'), method="POST")
            with urllib.request.urlopen(req, timeout=90) as r:
                d = json.load(r)
            return [x['embedding'] for x in sorted(d['data'], key=lambda x: x['index'])]
        except Exception as e:
            last = e
            time.sleep(3 * (attempt + 1))
    raise last

try:
    st = json.load(open(STATE, encoding='utf-8'))
    if st.get('ids') == [c['id'] for c in chunks]:
        vectors = st['vectors']
        print(f"resumed: {sum(1 for v in vectors if v)}/{len(vectors)} vectors cached")
    else:
        raise ValueError("ids changed")
except Exception:
    vectors = [None] * len(chunks)
    t0 = time.time()
    for i in range(0, len(chunks), EMBED_BATCH):
        batch = [c['content'] for c in chunks[i:i+EMBED_BATCH]]
        vecs = embed_batch(batch)
        for j, v in enumerate(vecs):
            vectors[i+j] = v
        done = i + EMBED_BATCH
        print(f"  embedded {min(done,len(chunks))}/{len(chunks)}  ({time.time()-t0:.0f}s)", flush=True)
        json.dump({'ids': [c['id'] for c in chunks], 'vectors': vectors},
                  open(STATE, 'w', encoding='utf-8'), ensure_ascii=False)

assert all(vectors), "some vectors still missing"

# --- 4. append to vectors.json (replace trailing ']' with ',<items>]' atomically) ---
data = open(VJSON, "rb").read()
assert data.rstrip().endswith(b']'), "vectors.json does not end with ']'"
objs = []
for c, v in zip(chunks, vectors):
    objs.append({
        "point_id": c['id'],
        "vector": [float(x) for x in v],
        "payload": {
            "document_id": c['document_id'],
            "section_id": c['section_id'],
            "section_key": c['section_key'],
            "chunk_index": c['chunk_index'],
            "content": c['content'],
            "token_count": c['token_count'],
            "embedding_model": MODEL,
        },
    })
new_tail = ("",",")[bool(objs[0])]  # noqa — just for clarity
joined = ",".join(json.dumps(o, ensure_ascii=False) for o in objs)
out = open(VJSON + ".tmp", "wb")
out.write(data[:-1])          # drop the final ']'
out.write(b"," + joined.encode("utf-8") + b"]")
out.close()
import os
os.replace(VJSON + ".tmp", VJSON)
print(f"appended {len(chunks)} points to {VJSON}")

# --- 5. MySQL ai_chunks (via temp .sql file — avoids command-line length limit) ---
def esc(s):
    return s.replace('\\', '\\\\').replace("'", "''")
sql_lines = []
for c in chunks:
    sql_lines.append(
        "INSERT INTO ai_chunks (id, document_id, section_id, chunk_index, content, content_hash, "
        "token_count, vector_point_id, embedding_model, embedding_version) VALUES "
        f"('{c['id']}', '{c['document_id']}', NULL, 0, '{esc(c['content'])}', '{c['content_hash']}', "
        f"{c['token_count']}, '{c['id']}', '{MODEL}', 'v1');"
    )
tmp_sql = "gap55_ai_chunks.sql"
with open(tmp_sql, "w", encoding="utf-8") as f:
    f.write("\n".join(sql_lines))
r = subprocess.run(
    ['C:/Program Files/MySQL/MySQL Server 8.0/bin/mysql.exe', '--default-character-set=utf8mb4',
     '-u', 'root', '-p433700', 'resaname_h'],
    stdin=open(tmp_sql, "rb"), capture_output=True, text=True, encoding='utf-8')
if r.returncode != 0:
    raise SystemExit(f"mysql insert failed: {r.stderr[:500]}")
print(f"ai_chunks: {len(chunks)} rows inserted")

# --- 6. SQLite vector store (append, L2-normalized float32) ---
con = sqlite3.connect(VDB)
n = con.execute("SELECT MAX(id) FROM vectors").fetchone()[0]
rows = []
for c, v in zip(chunks, vectors):
    vec = np.array(v, dtype=np.float32)
    norm = np.linalg.norm(vec)
    if norm > 0:
        vec = vec / norm
    rows.append((n + len(rows) + 1, c['id'], c['document_id'], c['section_id'], vec.tobytes()))
con.executemany("INSERT OR REPLACE INTO vectors (id, point_id, document_id, section_id, vector) VALUES (?,?,?,?,?)", rows)
con.execute("INSERT OR REPLACE INTO meta VALUES ('count', ?)", (str(n + len(rows)),))
con.commit()
con.close()
print(f"sqlite updated: {len(rows)} vectors appended (new count {n + len(rows)})")
print("DONE gap fix: 55 docs / 55 summary chunks embedded + stored everywhere")
