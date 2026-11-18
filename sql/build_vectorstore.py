# -*- coding: utf-8 -*-
"""Build a local SQLite vector store (resaname_vectors.sqlite) from vectors.json.
Replaces the broken Qdrant binary. 11313 x 2560-dim float32 vectors + JSON payload.
Cosine search via numpy: vectors are L2-normalized on insert, so cosine = dot.
"""
import ijson, json, sqlite3, struct, sys, time
import numpy as np

SRC = "vectors.json"
DB = "resaname_vectors.sqlite"
DIM = 2560
BATCH = 256

t0 = time.time()
con = sqlite3.connect(DB)
con.execute("PRAGMA journal_mode=WAL")
con.execute("PRAGMA synchronous=NORMAL")
con.execute("""
CREATE TABLE IF NOT EXISTS vectors (
    id          INTEGER PRIMARY KEY,
    point_id    TEXT NOT NULL UNIQUE,
    document_id TEXT NOT NULL,
    section_id  TEXT,
    vector      BLOB NOT NULL
)""")
con.execute("CREATE INDEX IF NOT EXISTS idx_vec_doc ON vectors(document_id)")
con.execute("CREATE INDEX IF NOT EXISTS idx_vec_point ON vectors(point_id)")
con.execute("""
CREATE TABLE IF NOT EXISTS meta (
    k TEXT PRIMARY KEY, v TEXT
)""")
con.commit()
con.execute("DELETE FROM vectors")
con.execute("INSERT OR REPLACE INTO meta VALUES ('dim', '2560')")
con.execute("INSERT OR REPLACE INTO meta VALUES ('model', 'Qwen3-Embedding-4B')")

rows = []
n = 0
with open(SRC, "rb") as f:
    for p in ijson.items(f, "item"):
        vec = np.array(p["vector"], dtype=np.float32)
        # L2-normalize so dot == cosine
        norm = np.linalg.norm(vec)
        if norm > 0:
            vec = vec / norm
        pay = p["payload"]
        rows.append((
            n + 1,
            p["point_id"],
            pay["document_id"],
            pay.get("section_id"),
            vec.tobytes(),
        ))
        n += 1
        if len(rows) >= BATCH:
            con.executemany("INSERT INTO vectors (id, point_id, document_id, section_id, vector) VALUES (?,?,?,?,?)", rows)
            rows = []
            if n % 1000 == 0:
                print(f"{n} rows  {time.time()-t0:.0f}s", flush=True)
if rows:
    con.executemany("INSERT INTO vectors (id, point_id, document_id, section_id, vector) VALUES (?,?,?,?,?)", rows)
con.execute("INSERT OR REPLACE INTO meta VALUES ('count', ?)", (str(n),))
con.commit()
con.close()
print(f"DONE: {n} vectors in {time.time()-t0:.0f}s -> {DB}")
