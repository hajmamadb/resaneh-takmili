# -*- coding: utf-8 -*-
"""فاز B — مرحله ۱: تولید کاندیداهای اتصال موجودیت‌های هسته‌ی دانش به ۸۵۲ contents
خروجی: kg_link_candidates.json
   [
     {"content_id": "doc-card-51", "content_title": "حریم خصوصی",
      "content_type": "concept", "candidates": [
          {"entity_id": "kg-...", "title_fa": "...", "entity_type": "CONCEPT", "score": 0.62}, ...
      ]},
     ...
   ]
فقط جفت‌هایی با score >= THRESHOLD و تا KMAX کاندیدای برتر در هر محتوا ثبت می‌شوند.

اجرا:  python kg_link_candidates.py
"""
import json
import sqlite3
import subprocess
import sys

import numpy as np

DB_SQLITE = "D:/رسانامه تکمیلی/sql/resaname_vectors.sqlite"
MYSQL = "C:/Program Files/MySQL/MySQL Server 8.0/bin/mysql.exe"
MDB = "resaname_v2"
THRESHOLD = 0.60
KMAX = 6

API = "https://ai.ismc.ir/api/v1/embeddings"
KEY = "sk-5K6TXne1qfnoiUWXvbQ0lg"
MODEL = "Qwen3-Embedding-4B"


def db_query(sql):
    r = subprocess.run(
        [MYSQL, "--default-character-set=utf8mb4", "-u", "root", "-p433700",
         MDB, "-N", "-B", "-e", sql],
        capture_output=True, text=True, encoding="utf-8")
    if r.returncode != 0:
        print("DB ERROR:", r.stderr[:500], file=sys.stderr); sys.exit(1)
    return r.stdout


print("loading contents + entities...", flush=True)
rows = db_query(
    "SELECT id, title, IFNULL(english_title,''), IFNULL(summary,'') "
    "FROM contents ORDER BY id;").splitlines()
contents = []
for line in rows:
    p = line.split("\t", 3)
    if len(p) >= 2:
        contents.append({"id": p[0], "title": p[1],
                         "en": p[2] if len(p) > 2 else "",
                         "summary": p[3] if len(p) > 3 else ""})
print(f"  contents: {len(contents)}", flush=True)

ent_rows = db_query(
    "SELECT id, title_fa, IFNULL(title_en,''), entity_type FROM knowledge_entities "
    "ORDER BY id;").splitlines()
entities = []
for line in ent_rows:
    p = line.split("\t", 3)
    if len(p) >= 3:
        entities.append({"id": p[0], "title_fa": p[1],
                         "title_en": p[2], "entity_type": p[3]})
print(f"  entities: {len(entities)}", flush=True)

# --- load vectors -------------------------------------------------------------
con = sqlite3.connect(DB_SQLITE)
con.row_factory = sqlite3.Row
cv = {}
for r in con.execute("SELECT point_id, vector FROM vectors WHERE source='content'"):
    cv[r["point_id"]] = np.frombuffer(r["vector"], dtype=np.float32)
kgv = {}
kg_ent_of = {}  # chunk point_id -> entity_id
for r in con.execute("SELECT point_id, entity_id, vector FROM kg_vectors"):
    kgv[r["point_id"]] = np.frombuffer(r["vector"], dtype=np.float32)
    kg_ent_of[r["point_id"]] = r["entity_id"]
con.close()
print(f"  vectors: content={len(cv)} kg={len(kgv)}", flush=True)

# --- embed content titles (resumable state) -----------------------------------
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
session = requests.Session()
session.mount("https://", HTTPAdapter(
    max_retries=Retry(total=3, backoff_factor=2,
                      status_forcelist=[500, 502, 503, 504])))
session.headers.update({"Authorization": f"Bearer {KEY}"})


def embed_batch(texts):
    r = session.post(API, json={"model": MODEL, "input": texts}, timeout=120)
    r.raise_for_status()
    d = r.json()
    return [x["embedding"] for x in sorted(d["data"], key=lambda x: x["index"])]


texts = []
for c in contents:
    head = c["title"]
    if c["en"]:
        head += " (" + c["en"] + ")"
    texts.append(head)

STATE = "D:/رسانامه تکمیلی/knowledge-core/tools/kg_link_state.json"
vecs = [None] * len(texts)
try:
    st = json.load(open(STATE, encoding="utf-8"))
    if st.get("ids") == [c["id"] for c in contents]:
        vecs = st["vectors"]
        print(f"resumed: {sum(1 for v in vecs if v)}/{len(texts)}", flush=True)
except Exception:
    pass

if any(v is None for v in vecs):
    B = 32
    nb = (len(texts) + B - 1) // B
    for bi in range(nb):
        i0 = bi * B
        if all(vecs[i0 + j] is not None for j in range(len(texts[i0:i0 + B]))):
            continue
        try:
            vs = embed_batch(texts[i0:i0 + B])
            for j, v in enumerate(vs):
                vecs[i0 + j] = v  # keep as list for JSON; converted on use
        except Exception as e:
            print(f"  batch {bi + 1} error: {e}", flush=True)
        if bi % 4 == 0 or bi == nb - 1:
            json.dump({"ids": [c["id"] for c in contents], "vectors": vecs},
                      open(STATE, "w"))
            print(f"  [{bi + 1}/{nb}] "
                  f"{sum(1 for v in vecs if v is not None)}/{len(texts)}",
                  flush=True)
    json.dump({"ids": [c["id"] for c in contents], "vectors": vecs},
              open(STATE, "w"))

# --- score ---------------------------------------------------------------------
kg_ids = list(kgv.keys())
kg_mat = np.stack([kgv[k] / max(np.linalg.norm(kgv[k]), 1e-9) for k in kg_ids])
kg_idx = {e["id"]: i for i, e in enumerate(entities)}

def norm(x):
    n = np.linalg.norm(x)
    return x / n if n > 0 else x


# aggregate per entity (max over its chunks) — one entity per position
ent_idx = np.array([kg_idx[kg_ent_of[k]] for k in kg_ids])
qmat = np.stack([norm(np.asarray(v, dtype=np.float32)) for v in vecs])
SIM = qmat @ kg_mat.T  # (852, 4464)
print("  sim computed, aggregating per entity...", flush=True)
ent_max = np.full((len(contents), len(entities)), -2.0)
np.maximum.at(ent_max, (np.repeat(np.arange(len(contents)), len(kg_ids)),
                        np.tile(ent_idx, len(contents))), SIM.ravel())
SIM = ent_max  # (852, 545)
print(f"  entity-level sim ready: {SIM.shape}", flush=True)

out = []
n_with = 0
for ci, c in enumerate(contents):
    srow = np.asarray(SIM[ci])
    order = np.argsort(-srow)
    cand = []
    for pos in order:
        s = float(srow[pos])
        if s < THRESHOLD:
            break
        if len(cand) >= KMAX:
            break
        e = entities[pos]
        cand.append({"entity_id": e["id"], "title_fa": e["title_fa"],
                     "entity_type": e["entity_type"], "score": round(s, 4)})
    if cand:
        out.append({"content_id": c["id"], "content_title": c["title"],
                    "content_type": c["en"] or "", "candidates": cand})
        n_with += 1
    if ci % 100 == 0:
        print(f"  scored {ci}/{len(contents)} (matched so far: {n_with})",
              flush=True)

json.dump(out, open("D:/رسانامه تکمیلی/knowledge-core/tools/kg_link_candidates.json",
                    "w", encoding="utf-8"), ensure_ascii=False, indent=1)
total_c = sum(len(o["candidates"]) for o in out)
print(f"DONE: contents_with_candidates={n_with}/{len(contents)}  "
      f"candidate_pairs={total_c}", flush=True)
