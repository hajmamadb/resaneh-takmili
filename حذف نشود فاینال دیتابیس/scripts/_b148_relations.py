# -*- coding: utf-8 -*-
"""Batch 148 relations: interactional, meaning, functionalist and ritual models."""
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-rel-batch148-20261116"

ROWS = [
    (1267, 1001, "MC-545 -> MC-305", 0.850, 50,
     "هر دو مدل ارتباط را فرایندی دایره‌ای با بازخورد و بافت رابطه می‌دانند."),
    (1268, 1255, "MC-546 -> MC-534", 0.900, 60,
     "تخصیص معنا و ارتباط سازمانی به‌عنوان تولید معنا یک بینش interpretive مشترک دارند."),
    (1268, 1439, "MC-546 -> MC-070", 0.850, 50,
     "مدل تخصیص معنا در سنت معناسازی تفسیری جای می‌گیرد."),
    (1269, 1483, "MC-547 -> MC-081", 0.900, 60,
     "چهار کارکرد رایت بسط کارکردهای سه‌گانهٔ لاسول است."),
    (1269, 1462, "MC-547 -> MC-720", 0.950, 70,
     "مدل رایت کاربرد پارادایم کارکردگرایی ساختاری در ارتباط جمعی است."),
    (1270, 1502, "MC-548 -> MC-099", 0.950, 70,
     "کارت مدل، نسخهٔ مدلی همان دیدگاه آیینی ارتباطات است."),
    (1270, 997, "MC-548 -> MC-301", 0.950, 70,
     "مدل انتقالی در برابر آیینی، مدل انتقالی ارتباط را به‌عنوان قطب مقابل صورتبندی می‌کند."),
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
print("RELATIONS BATCH148 DONE")
