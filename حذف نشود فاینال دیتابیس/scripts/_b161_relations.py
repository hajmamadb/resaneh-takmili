# -*- coding: utf-8 -*-
"""Relations for batch 161."""
import pymysql

STAMP = "qoder-rel-batch161-20261116"
DB = "resaname_kb_final_inspect"
ROWS = [
    ((1430, 846), 65, "گروه خاموش در صنایع فرهنگی، صداهای حاشیه‌ای را به بازنمایی نابرابر وامی‌دارد."),
    ((1430, 1105), 60, "چارچوب‌بندی غالب، تجربهٔ گروه خاموش را از میدان دید خبر بیرون می‌گذارد."),
    ((1430, 1327), 55, "جهان نمادین رسانه، مدل گروه مسلط را بازتولید و بیان حاشیه‌ای را خاموش می‌کند."),
    ((1449, 1481), 70, "سرگرمی، از اصلی‌ترین خشنودی‌های مخاطب در مدل استفاده و خشنودی است."),
    ((1449, 1327), 60, "تلویزیون سرگرم‌کننده، بخشی از جهان نمادین مشترک مخاطبان را می‌سازد."),
    ((1449, 1017), 55, "سرگرمی، کالای رقابتی اقتصاد توجه و پلتفرم‌های پخش است."),
    ((875, 806), 75, "نمایه‌سازی، سازوکار خبری دروازه‌بانی در حوزهٔ سیاست است."),
    ((875, 772), 70, "دستور کار رسمی، دامنهٔ بحثی را می‌سازد که خبر به آن نمایه می‌شود."),
    ((875, 1105), 70, "نمایه‌سازی و چارچوب‌بندی، دو لایهٔ قدرت رسانه در تعریف خبر سیاسی‌اند."),
    ((886, 772), 65, "دستور کار منفی خبر، زمینهٔ بدبینی و مالیخولیای سیاسی را می‌سازد."),
    ((886, 1327), 60, "جهان نمادین بدبینانهٔ رسانه، اعتماد سیاسی مخاطب را می‌فرساید."),
    ((886, 1105), 65, "چارچوب راهبردی خبر، سیاست را کشمکش نشان می‌دهد و بی‌اعتمادی می‌سازد."),
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
print("RELATIONS BATCH161 DONE")
