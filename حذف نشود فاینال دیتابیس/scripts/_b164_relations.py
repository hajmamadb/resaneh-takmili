# -*- coding: utf-8 -*-
"""Relations for batch 164."""
import pymysql

STAMP = "qoder-rel-batch164-20261116"
DB = "resaname_kb_final_inspect"
ROWS = [
    ((1284, 772), 60, "پوشش دستور کار، پیشتازی نامزد را برجسته و واکنش ارابه را تقویت می‌کند."),
    ((1284, 1017), 55, "اقتصاد توجه، نظرسنجی را به محتوای رقابتی و پرتکرار بدل می‌کند."),
    ((1284, 1285), 70, "اثر ارابه و اثر زیردست، دو واکنش متقابل به انتشار نظرسنجی‌اند."),
    ((1285, 772), 55, "برجسته‌سازی عقب‌ماندگی نامزد، همدلی و حمایت را برمی‌انگیزد."),
    ((1285, 1105), 55, "چارچوب روایت بازنده، حمایت از نامزد ضعیف را شکل می‌دهد."),
    ((1286, 828), 80, "تقویت نگرش، هستهٔ تجربی پارادایم اثرات محدود است."),
    ((1286, 1179), 75, "همسویی، صورت پنلی و انتخاباتی فرضیهٔ تأثیر محدود است."),
    ((1286, 1105), 60, "چارچوب همسو، گزینش و تفسیر اطلاعات را هدایت می‌کند."),
    ((1286, 1438), 55, "تقویت نگرش همسو، زمینهٔ سکوت دیدگاه اقلیت را می‌سازد."),
    ((1287, 1256), 60, "کاتارسیس و انتقال تحریک، دو خوانش متقابل از هیجان خشونت‌اند."),
    ((1287, 1327), 55, "کاشت و کاتارسیس در تحلیل اثر خشونت رسانه‌ای مقابل هم قرار می‌گیرند."),
    ((1287, 1280), 50, "جهان خشن رسانه‌ای، فرض تخلیهٔ خشونت را به چالش می‌کشد."),
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
print("RELATIONS BATCH164 DONE")
