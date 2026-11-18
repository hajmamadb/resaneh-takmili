# -*- coding: utf-8 -*-
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-rel-batch149-20261116"
NOW = "2026-11-16 00:00:00"
ROWS = [
    (1271, 1270, "RELATED_TO", 0.95, 70, "مدل ارتباط به‌مثابه فرهنگ، نسخهٔ مدلی همان چارچوب فرهنگی انتقالی در برابر آیینی است."),
    (1271, 1502, "RELATED_TO", 0.90, 65, "مدل کری بر دیدگاه آیینی ارتباطات تکیه دارد."),
    (1273, 1178, "RELATED_TO", 0.95, 70, "مدل شماتیک گربر، نسخهٔ دیگری از مدل گربر در این پایگاه است."),
    (1273, 1005, "RELATED_TO", 0.80, 60, "مدل شماتیک و مدل ادراکی گربر، دو بیان از زنجیرهٔ ادراک و تولیدند."),
    (1277, 1492, "RELATED_TO", 0.95, 70, "مدل وابستگی رسانه–مخاطب، صورت مدلی نظریهٔ وابستگی به نظام رسانه‌ای است."),
    (1277, 1015, "RELATED_TO", 0.90, 65, "این مدل با نسخهٔ دیگر نظریهٔ وابستگی در پایگاه هم‌پوشانی دارد."),
    (1290, 780, "RELATED_TO", 0.90, 65, "فرضیهٔ رشد پرخاشگری با مدل عمومی پرخاشگری در سازوکار یادگیری و طرحواره هم‌سو است."),
    (1290, 1327, "RELATED_TO", 0.80, 60, "فرضیهٔ رشد پرخاشگری به اثر درازمدت رسانه می‌پردازد، همچنان که نظریهٔ کاشت."),
    (1290, 1289, "RELATED_TO", 0.70, 55, "فرضیهٔ رشد پرخاشگری با فرضیهٔ ناکامی–پرخاشگری در تبیین پرخاشگری پیوند دارد."),
]

def main():
    c = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="433700",
                        database=DB, charset="utf8mb4")
    cur = c.cursor()
    ins = 0
    for src, tgt, label, conf, wt, note in ROWS:
        cur.execute("SELECT id FROM kb_relations WHERE source_id=%s AND target_id=%s AND relation_type=%s AND asserted_by=%s",
                    (src, tgt, label, STAMP))
        if cur.fetchone():
            continue
        cur.execute("""INSERT INTO kb_relations
            (source_id,target_id,relation_type,valid_from,valid_until,assertion_status,asserted_by,verified_by,
             extraction_confidence,note,weight,status,created_at,updated_at)
            VALUES (%s,%s,%s,NULL,NULL,'unverified',%s,NULL,%s,%s,%s,'active',%s,%s)""",
                    (src, tgt, label, STAMP, conf, note, wt, NOW, NOW))
        ins += 1
    c.commit()
    print("inserted", ins)
    print("RELATIONS BATCH149 DONE")

if __name__ == "__main__":
    main()
