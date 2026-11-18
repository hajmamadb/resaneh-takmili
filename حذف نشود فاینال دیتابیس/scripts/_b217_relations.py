# -*- coding: utf-8 -*-
"""Batch 217 relations."""
import pymysql

DB = "resaname_kb_final_inspect"
AB = "qoder-rel-batch217-20261117"
VB = "qoder-verify-batch217"

REL = [
    ("MC-545", "MC-546", "RELATED_TO", 84, "هر دو معنا را محصول تعامل و تفسیر فعال طرفین می‌دانند"),
    ("MC-545", "MC-307", "RELATED_TO", 80, "مدل روش و بیتسون لایهٔ رابطه‌ای پیام را به تحلیل تجربهٔ مشترک می‌افزاید"),
    ("MC-545", "MC-542", "RELATED_TO", 76, "لایهٔ فرارتباطی پیام با کارکرد فرازبانی یاکوبسون هم‌سو است"),
    ("MC-547", "MC-541", "RELATED_TO", 88, "مدل کارکردی رایت و مدل نظام اجتماعی رایلی و رایلی دو خوانش مکمل از رسانه در نظام اجتماعی‌اند"),
    ("MC-547", "MC-548", "RELATED_TO", 78, "تحلیل کارکردی رسانه با دیدگاه آیینی کری در بازتولید فرهنگ هم‌پوشانی دارد"),
    ("MC-548", "MC-549", "RELATED_TO", 94, "تمایز انتقالی-آیینی هستهٔ مدل ارتباط به‌مثابه فرهنگ کری است"),
    ("MC-548", "MC-345", "RELATED_TO", 80, "دیدگاه آیینی ارتباط بر بازنمایی نمادین و تولید معنا تکیه دارد"),
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
