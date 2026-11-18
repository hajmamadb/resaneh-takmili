# -*- coding: utf-8 -*-
"""Batch 215 relations."""
import pymysql

DB = "resaname_kb_final_inspect"
AB = "qoder-rel-batch215-20261117"
VB = "qoder-verify-batch215"

REL = [
    ("MC-062", "MDL-064", "RELATED_TO", 86, "زنجیرهٔ ارزش پورتر تحلیل درون‌صنعتی نیروهای پنج‌گانه را تکمیل می‌کند"),
    ("MC-062", "MC-034", "RELATED_TO", 84, "تحلیل ساختار صنعت رسانه پیش‌نیاز طراحی مدل درآمدی است"),
    ("MC-062", "MC-501", "RELATED_TO", 80, "در بازار دوسویه، شدت نیروها با اثر شبکه‌ای بین‌گروهی تغییر می‌کند"),
    ("MC-174", "MC-034", "RELATED_TO", 82, "تنوع‌بخشی درآمدی رسانه یکی از گزینه‌های ماتریس رشد است"),
    ("MC-174", "MC-504", "RELATED_TO", 78, "توسعهٔ محصول دیجیتال و بازار دُم بلند دو مسیر رشد رسانه‌اند"),
    ("MC-174", "MDL-067", "RELATED_TO", 76, "تحلیل سوات محیط درونی و بیرونی را پیش از انتخاب گزینهٔ رشد روشن می‌کند"),
    ("MC-503", "MC-040", "RELATED_TO", 88, "بیماری هزینه توضیح‌دهندهٔ فشار هزینهٔ تولید خبر است"),
    ("MC-503", "MC-611", "RELATED_TO", 80, "فشار هزینهٔ تولید اصیل از دلایل اصلی توجیه رسانهٔ عمومی است"),
    ("MC-504", "MC-501", "RELATED_TO", 84, "اقتصاد دُم بلند در بستر پلتفرم دوسویه عمل می‌کند"),
    ("MC-504", "MC-610", "RELATED_TO", 78, "کاهش هزینهٔ تولید و توزیع، اقتصاد سازندگان را ممکن می‌سازد"),
]

conn = pymysql.connect(host="127.0.0.1", port=3306, user="root",
                       password="433700", db=DB, charset="utf8mb4")
cur = conn.cursor()
codes = sorted({x for row in REL for x in row[:2]})
cur.execute("SELECT code,id FROM kb_entities WHERE code IN (%s)" % ",".join(["%s"] * len(codes)), codes)
m = dict(cur.fetchall())
missing = [c for c in codes if c not in m]
if missing:
    print("MISSING CODES:", missing)

cur.execute("SELECT source_id,target_id,relation_type FROM kb_relations")
have = {(a, b, t) for a, b, t in cur.fetchall()}

ins = 0
for src, tgt, rt, conf, note in REL:
    if src not in m or tgt not in m:
        continue
    a, b = m[src], m[tgt]
    if (a, b, rt) in have:
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
