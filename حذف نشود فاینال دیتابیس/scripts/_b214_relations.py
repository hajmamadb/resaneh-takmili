# -*- coding: utf-8 -*-
"""Batch 214 relations."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
AB = "qoder-rel-batch214-20261117"
VB = "qoder-verify-batch214"

REL = [
    ("MC-368", "MC-121", "RELATED_TO", 88, "مدل انتشار صادقانه ناظر بر شیوه‌های ارتباط سازمانی با رسانه است"),
    ("MC-368", "MC-367", "RELATED_TO", 90, "تبلیغ‌گری مطبوعاتی پیش‌درآمد تاریخی مدل انتشار صادقانه است"),
    ("MC-368", "MC-032", "RELATED_TO", 84, "هر دو در قلمرو ارتباطات ترغیبی سازمانی قرار می‌گیرند"),
    ("MC-368", "MC-493", "RELATED_TO", 82, "تاریخ حرفه‌ای‌شدن روابط عمومی با اعلامیهٔ اصول ۱۹۰۶ پیوند دارد"),
    ("MC-421", "MC-230", "RELATED_TO", 80, "حاکمیت الگوریتمی چارچوب قدرت و شفافیت سامانه‌های تولید خبر خودکار است"),
    ("MC-421", "MC-489", "RELATED_TO", 78, "خودکارسازی خبر بر حرفه‌ای‌گرایی و استقلال خبری اثر می‌گذارد"),
    ("MC-421", "MC-667", "RELATED_TO", 76, "سوگیری داده و الگوریتم به خروجی خبر خودکار منتقل می‌شود"),
    ("MC-541", "MC-082", "RELATED_TO", 92, "مدل رایلی و رایلی جایگاه اجتماعی فرستنده و گیرنده را به مدل خطی می‌افزاید"),
    ("MC-541", "MC-307", "RELATED_TO", 86, "هر دو پیام را در بافت اجتماعی و تجربهٔ گروهی مخاطب تحلیل می‌کنند"),
    ("MC-541", "MC-542", "RELATED_TO", 80, "تحلیل کارکردی پیام در نظام اجتماعی با چارچوب کارکردهای یاکوبسون تکمیل می‌شود"),
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
REL = [r for r in REL if r[0] in m and r[1] in m]

cur.execute("SELECT source_id,target_id,relation_type FROM kb_relations WHERE asserted_by=%s", (AB,))
have = {(a, b, t) for a, b, t in cur.fetchall()}

ins = 0
for src, tgt, rt, conf, note in REL:
    a, b = m[src], m[tgt]
    if (a, b, rt) in have:
        print("skip existing", src, tgt)
        continue
    cur.execute(
        "INSERT INTO kb_relations (source_id,target_id,relation_type,assertion_status,"
        "extraction_confidence,weight,asserted_by,verified_by,status,note,created_at,updated_at) "
        "VALUES (%s,%s,%s,'verified',%s,%s,%s,%s,'active',%s,NOW(),NOW())",
        (a, b, rt, conf / 100.0, 1, AB, VB, note))
    ins += 1

conn.commit()
print("inserted", ins, "relations")
cur.execute("SELECT count(*) FROM kb_relations WHERE asserted_by=%s", (AB,))
print("total in batch:", cur.fetchone()[0])
conn.close()
