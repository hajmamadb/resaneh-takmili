# -*- coding: utf-8 -*-
"""Relations for batch 154."""
import pymysql

STAMP = "qoder-rel-batch154-20261116"
DB = "resaname_kb_final_inspect"
ROWS = [
    ((1340, 1698), 75, "اقتصاد سازندگان، صورت تولیدی اقتصاد خالقان محتواست."),
    ((1340, 1919), 80, "سازندگان، لایهٔ تولید اقتصاد خالقان را می‌سازند."),
    ((1340, 847), 65, "آزادی تولید با ناپایداری کار خلاق پیوند دارد."),
    ((1341, 1799), 85, "مدل رسانهٔ عمومی، صورت نهادی مفهوم رسانهٔ عمومی است."),
    ((1341, 1204), 70, "استقلال خبری شرط تحقق خدمت عمومی است."),
    ((1341, 1106), 60, "رسانهٔ عمومی بدیل نهادی اقتصاد بازار خبر است."),
    ((1349, 870), 70, "مدل ویژگی‌های شغل، غنی‌سازی شغل را بر انگیزش درونی بنا می‌کند."),
    ((1349, 1351), 75, "طراحی شغل و تقاضا–منبع، دو چارچوب مکمل سلامت شغلی‌اند."),
    ((1349, 1204), 65, "خودمختاری تحریریه، هستهٔ مشترک طراحی شغل و حرفه‌گرایی است."),
    ((1351, 1349), 75, "تقاضا–منبع، طراحی شغل را با فرایند فرسودگی به هم می‌پیوندد."),
    ((1351, 870), 65, "منابع شغلی، معادل سازمانی عوامل انگیزش‌بخش‌اند."),
    ((1351, 1204), 60, "فشار حرفه‌ای خبرنگاری، تقاضای شغلی محسوب می‌شود."),
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
print("RELATIONS BATCH154 DONE")
