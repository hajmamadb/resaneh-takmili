# -*- coding: utf-8 -*-
"""Relations for batch 157."""
import pymysql

STAMP = "qoder-rel-batch157-20261116"
DB = "resaname_kb_final_inspect"
ROWS = [
    ((1388, 1492), 65, "تناسب ابزار و وظیفه، استفادهٔ مؤثر از رسانه را در وابستگی به نظام رسانه‌ای توضیح می‌دهد."),
    ((1388, 1115), 70, "مدل تناسب، پاسخ تجربی به ادعای جبرگرایانهٔ اثر یکسان فناوری است."),
    ((1388, 1481), 60, "تناسب وظیفه–فناوری، شرط بهره‌گیری مؤثر از رسانه در چارچوب استفاده و خشنودی است."),
    ((1410, 1105), 75, "اشاعهٔ خبر جعلی به چارچوب‌بندی رسانه‌ای و بازنمایی هیجانی رویداد وابسته است."),
    ((1410, 772), 65, "خبر جعلی با سازوکار برجسته‌سازی، اهمیت موضوع را در ذهن مخاطب دستکاری می‌کند."),
    ((1410, 1015), 60, "اشاعهٔ نادرستی در وضعیت وابستگی مخاطب به شبکهٔ اجتماعی تشدید می‌شود."),
    ((1415, 1476), 80, "مدل اسطوره، کاربست نشانه‌شناسی در تحلیل معنای فرهنگی رسانه است."),
    ((1415, 1500), 60, "اسطورهٔ تهدید، مادهٔ خام ساختن هراس اخلاقی در رسانه است."),
    ((1415, 1105), 55, "چارچوب‌بندی خبری با لایهٔ اسطوره‌ای، معنای رویداد را طبیعی جلوه می‌دهد."),
    ((1435, 1500), 80, "تعریف اولیه و تقویت رسانه‌ای، سازوکار شکل‌گیری هراس اخلاقی است."),
    ((1435, 806), 75, "دروازه‌بانی، جایگاه نهادی تعریف اولیه و حاشیه‌رانی صداها را نشان می‌دهد."),
    ((1435, 1105), 65, "چارچوب رسمی خبر، صورت عملی تعریف اولیه در پوشش رویداد است."),
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
print("RELATIONS BATCH157 DONE")
