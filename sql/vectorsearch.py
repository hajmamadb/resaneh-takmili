# -*- coding: utf-8 -*-
"""Local vector search over resaname_vectors.sqlite (11313 x 2560-dim, Qwen3-Embedding-4B).
Cosine similarity via L2-normalized vectors (dot product).
Usage: python vectorsearch.py "سوال فارسی" [k]
"""
import json, sqlite3, sys, time
import numpy as np
import requests

DB = "resaname_vectors.sqlite"
DIM = 2560
API = "https://ai.ismc.ir/api/v1/embeddings"
KEY = "sk-5K6TXne1qfnoiUWXvbQ0lg"
MODEL = "Qwen3-Embedding-4B"

def embed(texts):
    r = requests.post(API, headers={"Authorization": f"Bearer {KEY}"},
                      json={"model": MODEL, "input": texts}, timeout=60)
    r.raise_for_status()
    d = r.json()
    return [item["embedding"] for item in d["data"]]

def load_all():
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    rows = con.execute("SELECT id, point_id, document_id, section_id, vector FROM vectors").fetchall()
    con.close()
    mat = np.empty((len(rows), DIM), dtype=np.float32)
    for i, r in enumerate(rows):
        mat[i] = np.frombuffer(r["vector"], dtype=np.float32)
    return rows, mat

def search(query, k=10):
    t0 = time.time()
    qv = np.array(embed([query])[0], dtype=np.float32)
    n = np.linalg.norm(qv)
    if n > 0:
        qv = qv / n
    rows, mat = load_all()
    scores = mat @ qv
    idx = np.argsort(-scores)[:k]
    t1 = time.time()
    out = []
    for i in idx:
        r = rows[i]
        out.append({
            "score": float(scores[i]),
            "point_id": r["point_id"],
            "document_id": r["document_id"],
            "section_id": r["section_id"],
            "embed_s": round(t1 - t0, 2),
        })
    return out

if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else "رسانه‌ها چگونه افکار عمومی را شکل می‌دهند؟"
    k = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    for r in search(q, k):
        print(f"{r['score']:.4f}  {r['point_id']:<28} doc={r['document_id']:<12} sec={r['section_id']}")
