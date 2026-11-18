# -*- coding: utf-8 -*-
"""Relations for batch 163."""
import pymysql

STAMP = "qoder-rel-batch163-20261116"
DB = "resaname_kb_final_inspect"
ROWS = [
    ((1256, 1449), 70, "انتقال تحریک، سازوکار هیجانی لذت در سرگرمی رسانه‌ای است."),
    ((1256, 1327), 55, "انتقال تحریک، اثر کوتاه‌مدت مکمل کاشت بلندمدت رسانه است."),
    ((1256, 1017), 60, "محتوای پرهیجان، رقابت اقتصاد توجه را نشان می‌دهد."),
    ((1276, 1327), 75, "بازگشت اثرات قوی با کاشت بلندمدت هم‌راستاست."),
    ((1276, 1438), 80, "نوئل-نویمان، بازگشت اثرات قوی را در مارپیچ سکوت بسط داد."),
    ((1276, 772), 65, "قدرت بلندمدت رسانه در دستور کارسازی آشکار می‌شود."),
    ((1281, 1445), 65, "اثر شخص سوم، حمایت از تنظیم محتوای جعلی را توضیح می‌دهد."),
    ((1281, 1410), 60, "ادراک اثر بر دیگران، بازنشر هشدارگونهٔ خبر جعلی را توجیه می‌کند."),
    ((1281, 1500), 55, "ادراک آسیب‌پذیری دیگران، زمینهٔ هراس اخلاقی را می‌سازد."),
    ((1281, 806), 50, "دروازه‌بانی محتوا با ادراک اثر آن بر دیگران توجیه می‌شود."),
    ((1282, 1281), 75, "اثر شخص اول، الگوی معکوس اثر شخص سوم است."),
    ((1282, 1481), 55, "پذیرش پیام مطلوب، خشنودی کارکردی مخاطب را توضیح می‌دهد."),
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
print("RELATIONS BATCH163 DONE")
