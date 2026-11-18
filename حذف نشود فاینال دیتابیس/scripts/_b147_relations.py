# -*- coding: utf-8 -*-
"""Batch 147 relations: basic communication models (non-destructive RELATED_TO)."""
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-rel-batch147-20261116"

ROWS = [
    (1263, 1483, "MC-541 -> MC-081", 0.900, 60,
     "مدل رایلی و رایلی چارچوب خطی لاسول را در نظام اجتماعی جای می‌دهد."),
    (1264, 1266, "MC-542 -> MC-544", 0.950, 70,
     "کارکردهای شش‌گانهٔ جاکوبسون گسترش مدل ارگانون بولر است."),
    (1265, 1005, "MC-543 -> MC-309", 0.850, 50,
     "هر دو مدل بر بازسازی ادراکی پیام در گیرنده تأکید دارند."),
    (1266, 1264, "MC-544 -> MC-542", 0.950, 70,
     "مدل ارگانون بولر پیش‌درآمد کارکردهای شش‌گانهٔ جاکوبسون است."),
]

c = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="433700",
                    database=DB, charset="utf8mb4", autocommit=False)
cur = c.cursor()
for src, tgt, label, conf, weight, note in ROWS:
    cur.execute(
        "SELECT id FROM kb_relations WHERE source_id=%s AND target_id=%s AND relation_type='RELATED_TO' AND asserted_by=%s",
        (src, tgt, STAMP))
    if cur.fetchone():
        print(label, "exists")
        continue
    cur.execute(
        "INSERT INTO kb_relations (source_id, target_id, relation_type, assertion_status, asserted_by, "
        "extraction_confidence, note, weight, status, created_at, updated_at) "
        "VALUES (%s,%s,'RELATED_TO','unverified',%s,%s,%s,%s,'needs_review',NOW(),NOW())",
        (src, tgt, STAMP, conf, note, weight))
    print(label, "inserted id", cur.lastrowid)
c.commit()
c.close()
print("RELATIONS BATCH147 DONE")
