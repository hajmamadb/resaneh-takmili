# -*- coding: utf-8 -*-
"""Batch 220 relations."""
import pymysql

DB = "resaname_kb_final_inspect"
AB = "qoder-rel-batch220-20261117"
VB = "qoder-verify-batch220"

REL = [
    ("MC-599", "MC-501", "RELATED_TO", 96, "رکورد دوم مدل بازار دوسویه؛ رکورد اصلی با کد MC-501"),
    ("MC-609", "MC-185", "RELATED_TO", 96, "رکورد دوم مدل تمایز مکانی هاتلینگ؛ رکورد اصلی با کد MC-185"),
    ("MC-597", "MC-583", "RELATED_TO", 90, "مدل عمومی روابط عمومی، مدل دوسویهٔ متقارن را در چارچوب کارکرد راهبردی جای می‌دهد"),
    ("MC-597", "MC-593", "RELATED_TO", 78, "شهرت و اعتبار از پیامدهای کارکرد راهبردی روابط عمومی است"),
    ("MC-610", "MC-504", "RELATED_TO", 82, "اقتصاد سازندگان ادامهٔ منطق دُم بلند در تولید توزیع‌شده است"),
    ("MC-611", "MC-503", "RELATED_TO", 76, "توجیه عمومی رسانه با فشار هزینهٔ تولید و شکست بازار پیوند دارد"),
    ("MC-611", "MC-493", "RELATED_TO", 74, "رسانهٔ عمومی بدیل مدل تبلیغات‌محور مطبوعات است"),
]

conn = pymysql.connect(host="127.0.0.1", port=3306, user="root",
                       password="433700", db=DB, charset="utf8mb4")
cur = conn.cursor()
codes = sorted({x for row in REL for x in row[:2]})
cur.execute("SELECT code,id FROM kb_entities WHERE code IN (%s)" % ",".join(["%s"] * len(codes)), codes)
m = dict(cur.fetchall())
missing = [c for c in codes if c not in m]
if missing:
    print("MISSING:", missing)

cur.execute("SELECT source_id,target_id,relation_type FROM kb_relations")
have = {(a, b, t) for a, b, t in cur.fetchall()}

ins = 0
for src, tgt, rt, conf, note in REL:
    if src not in m or tgt not in m:
        continue
    a, b = m[src], m[tgt]
    if (a, b, rt) in have or (b, a, rt) in have:
        continue
    cur.execute(
        "INSERT INTO kb_relations (source_id,target_id,relation_type,assertion_status,"
        "extraction_confidence,weight,asserted_by,verified_by,status,note,created_at,updated_at) "
        "VALUES (%s,%s,%s,'verified',%s,%s,%s,%s,'active',%s,NOW(),NOW())",
        (a, b, rt, conf / 100.0, 1, AB, VB, note))
    ins += 1

conn.commit()
print("inserted", ins)
conn.close()
