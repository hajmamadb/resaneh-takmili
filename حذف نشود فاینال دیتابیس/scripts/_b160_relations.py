# -*- coding: utf-8 -*-
"""Relations for batch 160."""
import pymysql

STAMP = "qoder-rel-batch160-20261116"
DB = "resaname_kb_final_inspect"
ROWS = [
    ((1337, 807), 80, "زنجیرهٔ ارزش، ابزار پایهٔ تحلیل اقتصاد رسانه است."),
    ((1337, 846), 70, "صنایع فرهنگی، میدان کاربرد زنجیرهٔ ارزش در تولید نمادین است."),
    ((1337, 1083), 65, "اقتصاد سیاسی رسانه، توزیع قدرت در حلقه‌های زنجیره را می‌پرسد."),
    ((1354, 1099), 85, "کار احساسی، هم‌ارز مفهومی کار هیجانی در این مدخل است."),
    ((1354, 913), 65, "کار دیده‌شدن، صورتی دیجیتال از کار احساسی است."),
    ((1354, 847), 60, "کار خلاق ناپایدار، کار احساسی را با بی‌ثباتی شغلی می‌آمیزد."),
    ((1356, 847), 85, "نظریهٔ کار خلاق نامطمئن، بسط همان سنت پژوهش ناپایداری کار خلاق است."),
    ((1356, 909), 70, "سرمایه‌داری پلتفرمی، ناپایداری کار خلاق را تشدید می‌کند."),
    ((1356, 916), 65, "کار آزاد و بی‌دستمزد، سازوکار پنهان ناپایداری خلاق است."),
    ((1409, 1410), 75, "اشاعهٔ خبر نادرست، سازوکار تجربی پس‌حقیقت است."),
    ((1409, 1445), 70, "راستی‌آزمایی، پاسخ حرفه‌ای به بحران صدق است."),
    ((1409, 1017), 60, "اقتصاد توجه، رقابت بر سر دیده‌شدن را به فشار بر صدق بدل می‌کند."),
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
print("RELATIONS BATCH160 DONE")
