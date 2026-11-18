# -*- coding: utf-8 -*-
"""Batch 216 relations."""
import pymysql

DB = "resaname_kb_final_inspect"
AB = "qoder-rel-batch216-20261117"
VB = "qoder-verify-batch216"

REL = [
    ("MC-494", "MC-368", "RELATED_TO", 92, "مدل اطلاع‌رسانی عمومی و مدل انتشار صادقانه یک الگوی واحدند با دو نام"),
    ("MC-494", "MC-367", "RELATED_TO", 86, "اطلاع‌رسانی عمومی واکنش به تبلیغ‌گری مطبوعاتی است"),
    ("MC-494", "MDL-072", "RELATED_TO", 84, "مدل اطلاع‌رسانی عمومی یکی از چهار مدل روابط عمومی گرونیگ و هانت است"),
    ("MC-543", "MC-307", "RELATED_TO", 80, "هر دو نقش تصویر فرستنده و بافت ادراکی گیرنده را در ساخت معنا برجسته می‌کنند"),
    ("MC-543", "MC-421", "RELATED_TO", 74, "فشار سازمانی بر تولید پیام در تحلیل خودکارسازی خبر نیز مطرح است"),
    ("MC-543", "MC-546", "RELATED_TO", 84, "بازسازی روان‌شناختی پیام در مدل مالتزکه با تخصیص معنا در گیرنده هم‌سو است"),
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
