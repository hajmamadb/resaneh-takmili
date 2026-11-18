# -*- coding: utf-8 -*-
"""Batch 230 relations: MDL-041..045 (RELATED_TO, numeric ids, code-keyed)."""
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch230-20261117"
NOW = "2026-11-17 00:00:00"
conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="433700",
                       database=DB, charset="utf8mb4", cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()

PAIRS = [
    ("MDL-041", "MDL-040"),
    ("MDL-042", "MDL-041"),
    ("MDL-043", "MDL-040"),
    ("MDL-044", "MDL-043"),
    ("MDL-045", "MDL-044"),
    ("MDL-045", "MDL-026"),
    ("MDL-042", "MDL-027"),
]

codes = sorted({c for p in PAIRS for c in p})
cur.execute("SELECT id, code FROM kb_entities WHERE code IN (%s)" % ",".join(["%s"] * len(codes)), codes)
idof = {r["code"]: r["id"] for r in cur.fetchall()}
missing = [c for c in codes if c not in idof]
if missing:
    print("MISSING", missing); raise SystemExit(1)

cur.execute("SELECT source_id, target_id FROM kb_relations")
have = set()
for r in cur.fetchall():
    have.add((r["source_id"], r["target_id"])); have.add((r["target_id"], r["source_id"]))

added = 0
for a, b in PAIRS:
    ia, ib = idof[a], idof[b]
    if (ia, ib) in have:
        print("SKIP", a, b); continue
    cur.execute(
        "INSERT INTO kb_relations (source_id,target_id,relation_type,assertion_status,asserted_by,weight,status,created_at,updated_at) "
        "VALUES (%s,%s,'RELATED_TO','verified',%s,1,'active',%s,%s)",
        (ia, ib, STAMP, NOW, NOW))
    have.add((ia, ib)); have.add((ib, ia)); added += 1
    print("ADD", a, b)
conn.commit()
print("added", added)
conn.close()
