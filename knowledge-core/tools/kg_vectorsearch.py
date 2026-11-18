# -*- coding: utf-8 -*-
"""جستجوی برداری یکپارچه: هسته‌ی دانش (kg_vectors) + ۸۵۲ محتوا (vectors)
در یک فایل SQLite واحد — resaname_vectors.sqlite — با مدل یکسان
Qwen3-Embedding-4B (DIM 2560، L2-normalized → cosine = dot).

Usage:
  python kg_vectorsearch.py "سوال فارسی" [k] [scope]
  scope: kg (فقط هسته‌ی دانش) | content (فقط ۸۵۲ محتوا) | all (پیش‌فرض)
"""
import sqlite3
import sys
import time

import numpy as np
import requests

DB = "D:/رسانامه تکمیلی/sql/resaname_vectors.sqlite"
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


def load(scope):
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    out = []
    if scope in ("all", "content"):
        rows = con.execute(
            "SELECT id, point_id, document_id, section_id, vector FROM vectors "
            "WHERE source='content'").fetchall()
        for r in rows:
            out.append((r["point_id"], r["document_id"], r["section_id"],
                        np.frombuffer(r["vector"], dtype=np.float32)))
    if scope in ("all", "kg"):
        krows = con.execute(
            "SELECT point_id, entity_id, chunk_key, vector FROM kg_vectors"
        ).fetchall()
        for r in krows:
            out.append((r["point_id"], r["entity_id"], r["chunk_key"],
                        np.frombuffer(r["vector"], dtype=np.float32)))
    con.close()
    return out


def search(query, k=10, scope="all"):
    t0 = time.time()
    qv = np.array(embed([query])[0], dtype=np.float32)
    n = np.linalg.norm(qv)
    if n > 0:
        qv = qv / n
    rows = load(scope)
    mat = np.stack([r[3] for r in rows])
    scores = mat @ qv
    top = np.argsort(-scores)[:max(k, 1)]
    t1 = time.time()
    results = []
    for i in top:
        p = rows[i]
        results.append({
            "score": round(float(scores[i]), 4),
            "point_id": p[0],
            "source": "kg" if str(p[0]).startswith("kc-") else "content",
            "ref": p[1],
            "sub": p[2],
        })
    return results, round(t1 - t0, 2)


if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else "روش تحلیل محتوای کدگذاری باز"
    k = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    scope = sys.argv[3] if len(sys.argv) > 3 else "all"
    for r in search(q, k, scope)[0]:
        tag = {"kg": "KG ", "content": "CNT"}[r["source"]]
        print(f"{tag} {r['score']:.4f}  {r['point_id']:<36} {r['ref']:<16} {r['sub'] or ''}")
