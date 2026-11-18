# -*- coding: utf-8 -*-
"""Relations for batch 162."""
import pymysql

STAMP = "qoder-rel-batch162-20261116"
DB = "resaname_kb_final_inspect"
ROWS = [
    ((784, 796), 75, "شکاف دانش، بعد دانشی و مهارتی شکاف دیجیتال است."),
    ((784, 1481), 65, "استفادهٔ هدفمند و انگیزهٔ مخاطب، شکاف دانش را تعدیل می‌کند."),
    ((784, 772), 55, "دستور کار مشترک رسانه، پیش‌شرط شکل‌گیری شکاف دانش است."),
    ((784, 1832), 65, "سواد رسانه‌ای، توان جذب و ارزیابی دانش را تعیین می‌کند."),
    ((1179, 828), 80, "فرضیهٔ تأثیر محدود، صورت تجربی پارادایم اثرات محدود است."),
    ((1179, 1438), 60, "مارپیچ سکوت، اثر مشروط رسانه را در سطح اجتماعی توضیح می‌دهد."),
    ((1179, 808), 55, "دانش اقناع، مقاومت مخاطب در برابر پیام را توضیح می‌دهد."),
    ((1179, 1013), 65, "رهبران افکار، اثر رسانه را واسطه‌گری و تعدیل می‌کنند."),
    ((1274, 1013), 75, "جریان چندمرحله‌ای بر نقش رهبران افکار استوار است."),
    ((1274, 1137), 65, "انتشار نوآوری، بسط جریان چندمرحله‌ای در شبکه‌های اجتماعی است."),
    ((1275, 1012), 85, "جریان یک‌مرحله‌ای همان مدل گلولهٔ جادویی و سوزن تزریقی است."),
    ((1275, 828), 75, "جریان یک‌مرحله‌ای، نقطهٔ مقابل پارادایم اثرات محدود است."),
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
print("RELATIONS BATCH162 DONE")
