# -*- coding: utf-8 -*-
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-rel-batch152-20261116"
NOW = "2026-11-16 00:00:00"
ROWS = [
    (1318, 1213, "RELATED_TO", 0.90, 65, "مدل ارتباط بحران با میانجی‌گری رسانه‌های اجتماعی، گسترش مدل ارتباطات بحران در محیط شبکه‌ای است."),
    (1318, 1314, "RELATED_TO", 0.80, 55, "دزدیدن رعد و ارتباط بحران شبکه‌ای در مدیریت روایت بحران هم‌پوشانی دارند."),
    (1318, 798, "RELATED_TO", 0.85, 60, "این مدل بر نظریهٔ ارتباطات بحران وضعیتی و پاسخ عمومی‌ها تکیه دارد."),
    (1320, 1215, "RELATED_TO", 0.90, 65, "مدل شهرت و اعتبار سازمانی با چارچوب مدیریت اعتبار و شهرت هم‌سو است."),
    (1320, 815, "RELATED_TO", 0.85, 60, "اعتبار سازمانی و اعتبار منبع در باور مخاطب به شایستگی و درستی پیوند دارند."),
    (1320, 1317, "RELATED_TO", 0.75, 55, "اعتماد منبع در ارتباط خطر با شهرت و اعتبار سازمانی رابطه دارد."),
    (1321, 1309, "RELATED_TO", 0.85, 60, "گفت‌وگوی وب، صورت دیجیتال مدل دوسویهٔ متقارن است."),
    (1321, 1211, "RELATED_TO", 0.90, 65, "مدل اینترنت و روابط عمومی با مدل گفت‌وگویی روابط عمومی هم‌سو است."),
    (1322, 1321, "RELATED_TO", 0.90, 65, "مدل رسانه‌های اجتماعی و روابط عمومی، ادامهٔ مدل اینترنت و گفت‌وگوی وب است."),
    (1322, 1211, "RELATED_TO", 0.80, 55, "مدل رسانه‌های اجتماعی بر گفت‌وگوی دوسویه در روابط عمومی تأکید دارد."),
    (1322, 1309, "RELATED_TO", 0.75, 55, "رسانهٔ اجتماعی محیط آزمون تقارن و تغییر متقابل سازمان و مخاطب است."),
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
    print("RELATIONS BATCH152 DONE")

if __name__ == "__main__":
    main()
