# -*- coding: utf-8 -*-
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-rel-batch150-20261116"
NOW = "2026-11-16 00:00:00"
ROWS = [
    (1291, 895, "RELATED_TO", 0.80, 60, "شرطی‌سازی ارزشیابی، مسیر کم‌بسط پردازش اقناع را در مدل احتمال بسط توضیح می‌دهد."),
    (1291, 1860, "RELATED_TO", 0.90, 65, "مدل شرطی‌سازی رسانه، سازوکاری برای شکل‌گیری نگرش در فرایند اقناع است."),
    (1293, 895, "RELATED_TO", 0.80, 60, "مدل غلبه بر مقاومت سرگرمی با کاهش بسط انتقادی در برابر مدل احتمال بسط قرار می‌گیرد."),
    (1293, 1621, "RELATED_TO", 0.85, 65, "مدل سرگرمی و غلبه بر مقاومت بر سازوکار روایت و درگیری روایی تکیه دارد."),
    (1302, 809, "RELATED_TO", 0.95, 70, "این مدل نسخهٔ دیگری از مدل فرایند موازی گستردهٔ ترس در پایگاه است."),
    (1302, 928, "RELATED_TO", 0.90, 65, "مدل فرایند موازی گسترده بر نظریهٔ انگیزش محافظت و سازهٔ کارآمدی تکیه دارد."),
    (1302, 1448, "RELATED_TO", 0.85, 60, "مدل با نظریهٔ هشدار ترس در تبیین اثر پیام‌های ترس‌محور هم‌پوشانی دارد."),
    (1309, 797, "RELATED_TO", 0.95, 70, "مدل دوسویهٔ متقارن یکی از چهار مدل روابط عمومی گرونیگ و هانت است."),
    (1309, 1074, "RELATED_TO", 0.90, 65, "مدل متقارن به نظریهٔ تعالی روابط عمومی راه برد."),
    (1309, 1211, "RELATED_TO", 0.85, 60, "مدل متقارن و مدل گفت‌وگویی روابط عمومی در تأکید بر ارتباط دوسویه هم‌سو هستند."),
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
    print("RELATIONS BATCH150 DONE")

if __name__ == "__main__":
    main()
