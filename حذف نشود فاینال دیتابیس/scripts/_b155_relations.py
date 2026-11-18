# -*- coding: utf-8 -*-
"""Relations for batch 155."""
import pymysql

STAMP = "qoder-rel-batch155-20261116"
DB = "resaname_kb_final_inspect"
ROWS = [
    ((1362, 1718), 75, "مدل سه‌مرحله‌ای، هستهٔ مدل ارتباطات تغییر سازمانی است."),
    ((1362, 972), 65, "تغییر سازمانی و تغییر رفتار، دو سطح مکمل تحلیل تغییرند."),
    ((1362, 1488), 60, "انجماد تغییر با پذیرش نوآوری در سازمان پیوند دارد."),
    ((1363, 1718), 75, "هشت گام کاتر، برنامهٔ عملی ارتباط تغییر است."),
    ((1363, 972), 60, "کاتر بر آمادگی و مقاطع زمانی تغییر تأکید می‌کند."),
    ((1363, 1364), 70, "رهبری تحول‌آفرین، نیروی انسانی مدل کاتر را تأمین می‌کند."),
    ((1373, 1374), 80, "دموکراسی مخاطب، پیش‌درآمد تجربی پس‌دموکراسی است."),
    ((1373, 893), 75, "شخصی‌سازی سیاست، سازوکار اصلی دموکراسی مخاطب است."),
    ((1373, 872), 70, "رسانه‌ای‌شدن سیاست، زمینهٔ گذار به دموکراسی مخاطب است."),
    ((1374, 1373), 80, "تهی‌شدن پس‌دموکراتیک با تماشاگری مخاطب آغاز می‌شود."),
    ((1374, 1233), 70, "نقد رسانه و دموکراسی، زمینهٔ نظری پس‌دموکراسی است."),
    ((1374, 1642), 65, "پوپولیسم رسانه‌ای، بازخوانی تازهٔ تز پس‌دموکراسی است."),
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
print("RELATIONS BATCH155 DONE")
