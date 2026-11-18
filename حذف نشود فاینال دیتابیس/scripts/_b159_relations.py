# -*- coding: utf-8 -*-
"""Relations for batch 159."""
import pymysql

STAMP = "qoder-rel-batch159-20261116"
DB = "resaname_kb_final_inspect"
ROWS = [
    ((1452, 1481), 70, "استفادهٔ مسئله‌ساز از رسانه، صورت آسیب‌زای خشنودی جویی است."),
    ((1452, 1492), 65, "وابستگی فزاینده به رسانه، زمینهٔ الگوی اعتیادی را می‌سازد."),
    ((1452, 1449), 60, "سرگرمی تعاملی، بستر اصلی استفادهٔ مسئله‌ساز رسانه‌ای است."),
    ((1257, 1481), 70, "تعامل فرااجتماعی، خشنودی رابطه‌ای مخاطب را توضیح می‌دهد."),
    ((1257, 795), 60, "شخصیت رسانه‌ای می‌تواند همچون رهبر عقیده عمل کند."),
    ((1257, 1327), 55, "مواجههٔ مکرر با شخصیت، باور و برداشت مخاطب را شکل می‌دهد."),
    ((1258, 1449), 80, "نظریهٔ بازی، پایهٔ نظری پژوهش سرگرمی است."),
    ((1258, 1481), 65, "لذت بازی‌گونه، یکی از خشنودی‌های اصلی مصرف رسانه است."),
    ((1258, 1257), 55, "مصرف بازی‌گونه، زمینهٔ شکل‌گیری رابطهٔ فرااجتماعی است."),
    ((1280, 1327), 85, "سندرم جهان خشن، شاخهٔ کاربردی نظریهٔ کشت است."),
    ((1280, 772), 60, "برجسته‌سازی خبر جرم، ترس از جرم را تقویت می‌کند."),
    ((1280, 1500), 55, "تقویت ترس رسانه‌ای، به هراس اخلاقی و سیاست سخت‌گیرانه می‌رسد."),
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
print("RELATIONS BATCH159 DONE")
