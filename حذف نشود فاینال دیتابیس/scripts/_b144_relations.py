# -*- coding: utf-8 -*-
"""Batch 144 pre-step: link duplicate cards (ELM, HSM, press/advertising) to canonical entries."""
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-rel-batch144-20261116"
NOW = "2026-11-16 00:00:00"

PAIRS = [
    ("MC-467", "MC-319", "کارت موازی همان مدل احتمال تفصیل است؛ برای بازبینی ادغام و پرهیز از تکرار در دانشنامه ثبت شد."),
    ("MC-468", "MC-320", "کارت موازی همان مدل اکتشافی-سیستماتیک است؛ برای بازبینی ادغام و پرهیز از تکرار در دانشنامه ثبت شد."),
    ("MC-493", "MC-367", "کارت موازی سنت تبلیغ‌گری نمایشی بارنوم است؛ برای بازبینی ادغام و پرهیز از تکرار در دانشنامه ثبت شد."),
    ("MC-493", "MDL-047", "کارت مطبوعاتی-تبلیغاتی به مدل تبلیغات‌محور در تاکسونومی نزدیک است؛ برای بازبینی ادغام ثبت شد."),
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
               VALUES (%s, %s, 'RELATED_TO', 'under_review', %s, 0.990, %s, 60, 'needs_review', %s, %s)""",
            (s, t, STAMP, note, NOW, NOW))
        print(src, "->", tgt, "inserted id", cur.lastrowid)
    conn.commit()
    print("RELATIONS BATCH144 DONE")
finally:
    conn.close()
