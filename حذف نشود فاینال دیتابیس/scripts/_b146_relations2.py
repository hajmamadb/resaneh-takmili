# -*- coding: utf-8 -*-
"""Batch 146 relations: link duplicate/related model cards non-destructively."""
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-rel-batch146-20261116"

ROWS = [
    (1221, 1072, "MC-503 -> MC-157", 0.980, 70,
     "کارت مدل بیماری هزینه، نسخهٔ مدلی همان نظریهٔ ثبت‌شده در مدخل نظریه است."),
    (1221, 1106, "MC-503 -> MC-040", 0.850, 50,
     "بیماری هزینه سازوکار فشار هزینه بر مدل کسب‌وکار خبر را توضیح می‌دهد."),
    (1222, 836, "MC-504 -> MC-037", 0.980, 70,
     "کارت مدل دُم بلند، نسخهٔ مدلی همان نظریهٔ ثبت‌شده در مدخل نظریه است."),
    (1222, 1246, "MC-504 -> MC-526", 0.850, 50,
     "توزیع در دُم بلند به رتبه‌بندی و برجستگی الگوریتمی پلتفرم وابسته است."),
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
print("RELATIONS BATCH146b DONE")
