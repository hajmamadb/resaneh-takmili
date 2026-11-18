# -*- coding: utf-8 -*-
"""فاز A — هسته‌ی دانش: chunking + embedding از knowledge_entities (resaname_v2)
به resaname_vectors.sqlite (جدول kg_vectors) + جدول kg_chunks (MySQL).

رابطه با پایپلاین موجود (sql/embed_v3.py):
- مدل یکسان: Qwen3-Embedding-4B (ai.ismc.ir) — DIM 2560، L2-normalized
- chunk 0 هر موجودیت = title_fa + title_en + entity_type + abstract
  (مثل chunk 0 = summary در embed_v3.py)
- chunk‌های بعدی: میدان‌های روایی (~680 کاراکتر، overlap 80)
- state resumable: kg_chunks_state.json
- جدول جدا (kg_vectors) تا 11513 موجودیت vectors دست‌نخورده بماند؛
  ستون source='kg' در هر دو جدول برای جستجوی یکپارچه.

اجرا:  python kg_chunk_embed.py
"""
import hashlib
import json
import re
import sqlite3
import subprocess
import sys
import time

import numpy as np

BASE = "https://ai.ismc.ir/api"
API_KEY = "sk-5K6TXne1qfnoiUWXvbQ0lg"
MODEL = "Qwen3-Embedding-4B"
DIM = 2560
EMBED_BATCH = 32   # measured: ~4s/batch on ai.ismc.ir (Qwen3-4B) — 8 was too conservative
MAX_CHARS = 680
OVERLAP = 80
TOKEN_EST = 0.55
MYSQL = "C:/Program Files/MySQL/MySQL Server 8.0/bin/mysql.exe"
DB = "resaname_v2"
SQLITE = "D:/رسانامه تکمیلی/sql/resaname_vectors.sqlite"
STATE = "D:/رسانامه تکمیلی/knowledge-core/tools/kg_chunks_state.json"

# --- DoH DNS fallback (ai.ismc.ir sometimes fails getaddrinfo) ---
import socket as _socket
_DOH_HOSTS = {"ai.ismc.ir"}
def _doh_resolve(host):
    import urllib.request
    u = f"https://dns.google/resolve?name={host}&type=A"
    d = json.load(urllib.request.urlopen(
        urllib.request.Request(u, headers={"User-Agent": "m"}), timeout=10))
    ips = [a["data"] for a in d.get("Answer", []) if a.get("type") == 1]
    if not ips:
        raise _socket.gaierror(f"DoH no A for {host}")
    return [(_socket.AF_INET, _socket.SOCK_STREAM, 6, "", (ip, 443)) for ip in ips]
_orig_gai = _socket.getaddrinfo
def _patched(host, port, *a, **kw):
    if host in _DOH_HOSTS:
        try:
            return _doh_resolve(host)
        except Exception:
            pass
    return _orig_gai(host, port, *a, **kw)
_socket.getaddrinfo = _patched

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
session = requests.Session()
adapter = HTTPAdapter(max_retries=Retry(total=3, backoff_factor=2,
                                        status_forcelist=[500, 502, 503, 504]))
session.mount("https://", adapter)
session.headers.update({"Authorization": f"Bearer {API_KEY}",
                        "Content-Type": "application/json"})


def db_query(sql):
    r = subprocess.run(
        [MYSQL, "--default-character-set=utf8mb4", "-u", "root", "-p433700",
         DB, "-N", "-B", "-e", sql],
        capture_output=True, text=True, encoding="utf-8")
    if r.returncode != 0:
        print("DB ERROR:", r.stderr[:500], file=sys.stderr); sys.exit(1)
    return r.stdout


# --- load entities (tab-separated; strip tabs/newlines inside fields) --------
ENT_FIELDS = ["id", "title_fa", "title_en", "slug", "entity_type",
              "abstract", "description", "historical_background",
              "philosophical_foundations", "key_propositions", "key_figures",
              "origin_period", "geographical_origin", "related_disciplines",
              "applications", "strengths", "limitations", "criticisms",
              "references", "status"]
N = len(ENT_FIELDS)
print("Loading knowledge_entities...", flush=True)
raw = db_query(
    "SELECT " + ", ".join(
        f"IFNULL(REPLACE(REPLACE(REPLACE(`{f}`, '\\t', ' '), '\\n', ' '), '\\r', ' '), '')"
        for f in ENT_FIELDS) + " FROM knowledge_entities ORDER BY id;")
entities = []
for line in raw.splitlines():
    p = line.split("\t")
    if len(p) >= N:
        entities.append(dict(zip(ENT_FIELDS, p[:N])))
print(f"  entities: {len(entities)}", flush=True)

# --- chunker (same sentence/word-boundary logic as embed_v3.py) --------------
SENT_END = re.compile(r"(?<=[.!?؟۔…])\s+")
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
                sp = seg.rfind(" ")
                if sp >= max_chars * 0.4:
                    end = start + sp
        c = text[start:end].strip()
        if c:
            out.append(c)
        if end >= n:
            break
        start = max(end - overlap, start + 1)
    return out


def entity_chunks(e):
    """chunk 0 = identity/summary؛ بعدی = میدان‌های روایی (ترتیب ثابت)."""
    out = []
    head = " ".join(x for x in [
        e["title_fa"],
        ("(" + e["title_en"] + ")") if e["title_en"] else "",
        "نوع: " + e["entity_type"],
        e["abstract"],
    ] if x).strip()
    if head:
        out.append(("summary", head[:2000]))
    narrative = ["description", "historical_background",
                 "philosophical_foundations", "key_propositions",
                 "key_figures", "origin_period", "geographical_origin",
                 "related_disciplines", "applications", "strengths",
                 "limitations", "criticisms", "references"]
    for f in narrative:
        for piece in split_text(e.get(f) or ""):
            out.append((f, piece))
    return out


chunks = []
for e in entities:
    idx = 0
    for key, text in entity_chunks(e):
        idx += 1
        chunks.append({
            "id": f"kc-{e['id']}-{idx}" if idx > 1 else f"kc-{e['id']}-0",
            "entity_id": e["id"],
            "chunk_key": key,
            "chunk_index": idx,
            "content": text,
            "token_count": int(len(text) / TOKEN_EST),
        })
print(f"total chunks: {len(chunks)}", flush=True)

# --- embed (resumable) --------------------------------------------------------
def embed_batch(texts):
    r = session.post(BASE + "/v1/embeddings",
                     json={"model": MODEL, "input": texts}, timeout=120)
    r.raise_for_status()
    d = r.json()
    return [x["embedding"] for x in sorted(d["data"], key=lambda x: x["index"])]

state_file = STATE
try:
    st = json.load(open(state_file, encoding="utf-8"))
    if st.get("chunk_ids") == [c["id"] for c in chunks]:
        vectors = st["vectors"]
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
        batch = chunks[i0:i0 + EMBED_BATCH]
        if all(vectors[i0 + j] is not None for j in range(len(batch))):
            continue
        try:
            vecs = embed_batch([c["content"] for c in batch])
            for j, v in enumerate(vecs):
                vectors[i0 + j] = v
        except Exception as e:
            print(f"  batch {bi + 1} error: {e}", flush=True)
            time.sleep(5)
            continue
        if bi % 25 == 0 or bi == n_batches - 1:
            el = time.time() - t0
            done = sum(1 for v in vectors if v)
            rate = done / max(el, 1)
            eta = (len(chunks) - done) / max(rate, 0.01)
            print(f"  [{bi + 1}/{n_batches}] {done}/{len(chunks)} "
                  f"({100 * done / len(chunks):.1f}%)  {el:.0f}s  "
                  f"ETA {eta / 60:.0f}min", flush=True)
            json.dump({"chunk_ids": [c["id"] for c in chunks], "vectors": vectors},
                      open(state_file, "w"))
    json.dump({"chunk_ids": [c["id"] for c in chunks], "vectors": vectors},
              open(state_file, "w"))
print(f"embed complete: {sum(1 for v in vectors if v)}/{len(chunks)}", flush=True)

# --- write SQLite: kg_vectors table + source discriminator -------------------
con = sqlite3.connect(SQLITE)
con.execute("CREATE TABLE IF NOT EXISTS kg_vectors ("
            "id TEXT PRIMARY KEY, point_id TEXT NOT NULL, "
            "entity_id TEXT NOT NULL, chunk_key TEXT, "
            "vector BLOB NOT NULL, source TEXT NOT NULL DEFAULT 'kg')")
con.execute("ALTER TABLE vectors ADD COLUMN source TEXT")  # may already exist
con.execute("UPDATE vectors SET source='content' WHERE source IS NULL")
if "source" not in {r[1] for r in con.execute("PRAGMA table_info(kg_vectors)")}:
    con.execute("ALTER TABLE kg_vectors ADD COLUMN source TEXT NOT NULL DEFAULT 'kg'")
con.execute("DELETE FROM kg_vectors WHERE entity_id IS NOT NULL")  # rebuild
for c, v in zip(chunks, vectors):
    if v is None:
        continue
    arr = np.asarray(v, dtype=np.float32)
    nrm = np.linalg.norm(arr)
    if nrm > 0:
        arr = arr / nrm
    con.execute("INSERT INTO kg_vectors (id, point_id, entity_id, chunk_key, vector, source) "
                "VALUES (?,?,?,?,?,?)",
                (c["id"], c["id"], c["entity_id"], c["chunk_key"],
                 arr.tobytes(), "kg"))
con.commit()
kg_n = con.execute("SELECT COUNT(*) FROM kg_vectors").fetchone()[0]
all_n = con.execute("SELECT COUNT(*) FROM vectors").fetchone()[0]
con.close()
print(f"sqlite: kg_vectors={kg_n}  vectors(content)={all_n}", flush=True)

# --- write kg_chunks upsert SQL (MySQL) --------------------------------------
def q(s):
    return s.replace("\\", "\\\\").replace("'", "''")

sql = ["-- فاز A: kg_chunks upsert (هسته‌ی دانش)", "USE resaname_v2;",
       "SET FOREIGN_KEY_CHECKS=0;", ""]
for c, v in zip(chunks, vectors):
    if v is None:
        continue
    h = hashlib.sha256(c["content"].encode()).hexdigest()
    sql.append(
        f"INSERT INTO kg_chunks (id, entity_id, chunk_index, content, content_hash, "
        f"token_count, vector_point_id, embedding_model, embedding_version) "
        f"VALUES ('{q(c['id'])}', '{q(c['entity_id'])}', {c['chunk_index']}, "
        f"'{q(c['content'])}', '{h}', {c['token_count']}, '{q(c['id'])}', "
        f"'{MODEL}', '1') ON DUPLICATE KEY UPDATE content_hash='{h}', "
        f"token_count={c['token_count']}, vector_point_id='{q(c['id'])}', "
        f"embedding_model='{MODEL}', embedding_version='1';")
sql += ["", "SET FOREIGN_KEY_CHECKS=1;",
        "-- verify: SELECT COUNT(*) FROM kg_chunks;"]
out_sql = "D:/رسانامه تکمیلی/knowledge-core/tools/load_kg_chunks.sql"
open(out_sql, "w", encoding="utf-8", newline="").write("\n".join(sql))
print(f"wrote {out_sql}: {len(chunks)} rows", flush=True)
print("DONE", flush=True)
