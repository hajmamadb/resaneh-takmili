# -*- coding: utf-8 -*-
"""Relations for batch 153."""
import pymysql

STAMP = "qoder-rel-batch153-20261116"
DB = "resaname_kb_final_inspect"
ROWS = [
    ((1324, 1074), 70, "مدل عمومی روابط عمومی، صورت‌بندی راهبردی نظریهٔ تعالی است."),
    ((1324, 1309), 80, "نسخهٔ راهبردی مدل دوسویهٔ متقارن."),
    ((1324, 797), 65, "وارث خانوادهٔ مدل‌های چهارگانهٔ روابط عمومی."),
    ((1326, 1106), 75, "اقتصاد خبر را باید در چارچوب بازار دوسویهٔ مخاطب و تبلیغ فهمید."),
    ((1326, 836), 60, "بیماری هزینه فشار را در طرف محتوای پلتفرم دوطرفه توضیح می‌دهد."),
    ((1326, 1338), 55, "رقابت مکانی، بعد فضایی رقابت پلتفرم‌های دوسویه را روشن می‌کند."),
    ((1335, 1106), 70, "ساختار صنعت خبر با پنج نیرو تحلیل می‌شود."),
    ((1335, 836), 60, "بیماری هزینه یکی از فشارهای ساختاری صنعت رسانه است."),
    ((1335, 1326), 60, "پلتفرم‌ها نیروی رقابتی تازه‌ای در ساختار صنعت رسانه‌اند."),
    ((1338, 1106), 65, "همگرایی محتوا در اقتصاد خبر با مدل مکانی توضیح داده می‌شود."),
    ((1338, 1326), 60, "پلتفرم دوسویه رقابت مکانی دیجیتال را بازتولید می‌کند."),
    ((1338, 1327), 55, "کاشت و همگرایی محتوا هر دو به شباهت پیام در بازار رسانه می‌انجامند."),
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
print("RELATIONS BATCH153 DONE")
