# -*- coding: utf-8 -*-
"""Batch 146 pre-step: relate algorithmic scoring and generative AI to neighbouring models."""
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-rel-batch146-20261116"
NOW = "2026-11-16 00:00:00"

PAIRS = [
    ("MC-526", "MC-704", "نظریهٔ برچسب و امتیازدهی الگوریتمی با چارچوب دروازه‌بانی الگوریتمی هم‌پوشانی مفهومی دارد."),
    ("MC-531", "MC-421", "مدل هوش مصنوعی مولد در رسانه ادامهٔ منطق خودکارسازی تولید خبر است."),
]

conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="433700",
                       database=DB, charset="utf8mb4", autocommit=False)
try:
    cur = conn.cursor()
    ids = {}
    for a, b, _ in PAIRS:
        cur.execute("SELECT code, id FROM kb_entities WHERE code IN (%s, %s)", (a, b))
        for code, eid in cur.fetchall():
            ids[code] = eid
    for src, tgt, note in PAIRS:
        s, t = ids[src], ids[tgt]
        cur.execute("SELECT id FROM kb_relations WHERE source_id=%s AND target_id=%s AND relation_type='RELATED_TO'", (s, t))
        if cur.fetchone():
            print(src, "->", tgt, "exists, skipped")
            continue
        cur.execute(
            """INSERT INTO kb_relations
               (source_id, target_id, relation_type, assertion_status, asserted_by,
                extraction_confidence, note, weight, status, created_at, updated_at)
               VALUES (%s, %s, 'RELATED_TO', 'under_review', %s, 0.900, %s, 50, 'needs_review', %s, %s)""",
            (s, t, STAMP, note, NOW, NOW))
        print(src, "->", tgt, "inserted id", cur.lastrowid)
    conn.commit()
    print("RELATIONS BATCH146 DONE")
finally:
    conn.close()
