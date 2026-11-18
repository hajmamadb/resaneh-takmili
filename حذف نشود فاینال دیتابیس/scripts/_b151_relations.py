# -*- coding: utf-8 -*-
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-rel-batch151-20261116"
NOW = "2026-11-16 00:00:00"
ROWS = [
    (1313, 1309, "RELATED_TO", 0.85, 60, "هم‌جهت‌یابی، ادراک متقابل لازم برای گفت‌وگوی دوسویهٔ متقارن را می‌سنجد."),
    (1313, 1311, "RELATED_TO", 0.80, 55, "هم‌جهت‌یابی و نظریهٔ وضعیتی عمومی‌ها هر دو بر ادراک طرفین از یکدیگر تکیه دارند."),
    (1314, 1213, "RELATED_TO", 0.90, 65, "دزدیدن رعد راهبردی در چارچوب مدل ارتباطات بحران است."),
    (1314, 798, "RELATED_TO", 0.85, 60, "افشای پیش‌دستانه، پاسخ سازمان را در نظریهٔ ارتباطات بحران وضعیتی شکل می‌دهد."),
    (1314, 1215, "RELATED_TO", 0.80, 55, "دزدیدن رعد برای مدیریت اعتبار و شهرت سازمانی در بحران به کار می‌رود."),
    (1317, 1302, "RELATED_TO", 0.85, 60, "ارتباط خطر و پیام ترس‌محور در برانگیختن رفتار محافظتی هم‌پوشانی دارند."),
    (1317, 815, "RELATED_TO", 0.90, 65, "مدل ارتباطات خطر بر اعتبار منبع به‌عنوان شرط پذیرش پیام تکیه دارد."),
    (1317, 1314, "RELATED_TO", 0.75, 55, "ارتباط خطر و ارتباط بحران در مدیریت موقعیت‌های پرنگرانی پیوند دارند."),
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
    print("RELATIONS BATCH151 DONE")

if __name__ == "__main__":
    main()
