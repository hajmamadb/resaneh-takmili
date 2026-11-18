# -*- coding: utf-8 -*-
"""Relations for batch 158."""
import pymysql

STAMP = "qoder-rel-batch158-20261116"
DB = "resaname_kb_final_inspect"
ROWS = [
    ((1440, 806), 80, "دروازه‌بانی، سازوکار درونی رابطهٔ منبع و رسانه در تولید خبر است."),
    ((1440, 1105), 70, "چارچوب خبری، محصول مذاکرهٔ رسانه و منبع بر سر تعریف رویداد است."),
    ((1440, 1500), 60, "همزیستی با منابع رسمی، زمینهٔ تقویت روایت تهدید و هراس اخلاقی است."),
    ((1443, 1105), 65, "زمینه‌سازی بلندفرم، لایهٔ عمیق چارچوب‌بندی خبر است."),
    ((1443, 1481), 60, "روزنامه‌نگاری کند به انتظار مخاطب برای عمق و خشنودی پاسخ می‌دهد."),
    ((1443, 1444), 55, "منطق سرعت در توزیع الگوریتمی، نقطهٔ مقابل منطق کند است."),
    ((1444, 806), 85, "دروازه‌بانی الگوریتمی، بازنویسی نظریهٔ کلاسیک دروازه‌بانی است."),
    ((1444, 1410), 65, "رتبه‌بندی و توصیه‌گری، اشاعهٔ خبر نادرست را تشدید یا مهار می‌کند."),
    ((1444, 1115), 55, "اثر ساختار فناورانه بر دیده‌شدن خبر، صورتی از جبرگرایی فناورانه است."),
    ((1445, 1410), 80, "راستی‌آزمایی، پاسخ حرفه‌ای به اشاعهٔ خبر نادرست است."),
    ((1445, 1444), 70, "دسترسی راستی‌آزمایی به مخاطب به گزینش پلتفرم وابسته است."),
    ((1445, 1105), 60, "ادعای نادرست با چارچوب خبری معتبر پوشش داده می‌شود و راستی‌آزمایی آن را می‌گشاید."),
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
print("RELATIONS BATCH158 DONE")
