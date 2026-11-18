# -*- coding: utf-8 -*-
"""Relations for batch 156."""
import pymysql

STAMP = "qoder-rel-batch156-20261116"
DB = "resaname_kb_final_inspect"
ROWS = [
    ((1376, 1374), 75, "رژیم ترکیبی، وضعیت میانی میان دموکراسی مخاطب و پس‌دموکراسی است."),
    ((1376, 1107), 65, "رسانهٔ رکن چهارم، در رژیم ترکیبی به نهاد مهارشده بدل می‌شود."),
    ((1376, 1233), 70, "تحلیل رسانه و دموکراسی، زمینهٔ نظری رژیم ترکیبی است."),
    ((1382, 872), 75, "رسانه‌ای‌شدن، سازوکار محیطی‌شدن رسانه در زندگی اجتماعی است."),
    ((1382, 792), 75, "جامعهٔ پلتفرمی، صورت دیجیتال محیط رسانه‌ای است."),
    ((1382, 1112), 65, "تنظیم‌گری پلتفرمی، پاسخ سیاستی به محیط رسانه‌ای تازه است."),
    ((1384, 1444), 80, "دروازه‌بانی الگوریتمی، لایهٔ نهادی خودکارسازی خبر است."),
    ((1384, 1204), 70, "خودکارسازی، مرز حرفه‌گرایی و مهارت خبرنگار را جابه‌جا می‌کند."),
    ((1384, 1382), 60, "خودکارسازی در محیط رسانه‌ای الگوریتمی رشد می‌کند."),
    ((1386, 1384), 65, "موفقیت سامانهٔ تحریریه، پذیرش خودکارسازی را تعیین می‌کند."),
    ((1386, 1120), 70, "پذیرش فناوری، حلقهٔ کاربری مدل موفقیت را توضیح می‌دهد."),
    ((1386, 1382), 55, "سنجش موفقیت سامانه، بخشی از تحلیل محیط رسانه‌ای است."),
]

c = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="433700",
                   database=DB, charset="utf8mb4")
cur = c.cursor()
inserted = 0
for (src, tgt), w, note in ROWS:
    cur.execute("""SELECT id FROM kb_relations WHERE source_id=%s AND target_id=%s
                   AND relation_type='RELATED_TO' AND asserted_by=%s""", (src, tgt, STAMP))
    if cur.fetchone():
        continue
    cur.execute("""INSERT INTO kb_relations
        (source_id, target_id, relation_type, valid_from, valid_until, assertion_status,
         asserted_by, verified_by, extraction_confidence, note, weight, status, created_at, updated_at)
        VALUES (%s,%s,'RELATED_TO',NULL,NULL,'unverified',%s,NULL,0.80,%s,%s,'active',NOW(),NOW())""",
        (src, tgt, STAMP, note, w))
    inserted += 1
c.commit()
print("inserted", inserted)
c.close()
print("RELATIONS BATCH156 DONE")
