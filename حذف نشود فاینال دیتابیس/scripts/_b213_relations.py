# -*- coding: utf-8 -*-
"""Batch 211 relations."""
import pymysql

DB = "resaname_kb_final_inspect"
ASSERTED = "qoder-rel-batch213-20261117"
VERIFIED = "qoder-verify-batch213"
NOW = "2026-11-17 00:00:00"

REL = [
    ("MC-495", "MC-121", "RELATED_TO", 0.85,
     "مدل گفت‌وگویی، نقد و تکمیل مدل‌های چهارگانهٔ روابط عمومی با تأکید بر تعامل دوسویه است."),
    ("MC-495", "MC-597", "RELATED_TO", 0.75,
     "مدل عمومی روابط عمومی، جایگاه گفت‌وگو را در فرایند ارتباط سازمانی نشان می‌دهد."),
    ("MC-495", "MC-594", "RELATED_TO", 0.80,
     "مدل گفت‌وگویی در محیط وب و رسانه‌های اجتماعی به‌کار می‌رود."),
    ("MC-495", "MC-593", "RELATED_TO", 0.65,
     "گفت‌وگوی واقعی یکی از عوامل ساخت شهرت و اعتبار سازمانی است."),

    ("MC-497", "MC-590", "RELATED_TO", 0.80,
     "نظریهٔ موقعیتی بحران و مدل ارتباطات خطر هر دو بر ارزیابی تهدید و پاسخ مناسب تأکید دارند."),
    ("MC-497", "MC-591", "RELATED_TO", 0.80,
     "بحران در محیط شبکه‌های اجتماعی چارچوب موقعیتی را با سرعت انتشار و پاسخ آنی گسترش می‌دهد."),
    ("MC-497", "MC-593", "RELATED_TO", 0.85,
     "انتخاب راهبرد پاسخ در نظریهٔ موقعیتی، مستقیماً بر حفظ شهرت سازمانی اثر می‌گذارد."),
    ("MC-497", "MC-149", "RELATED_TO", 0.75,
     "نظریهٔ انتساب، بنیان شناختی انتخاب راهبرد پاسخ در نظریهٔ موقعیتی است."),

    ("MC-345", "MC-544", "RELATED_TO", 0.75,
     "مدل ارگانون بولر و سه‌گانهٔ پیرس هر دو رابطهٔ سه‌جزئی نشانه را تحلیل می‌کنند."),
    ("MC-345", "MC-542", "RELATED_TO", 0.70,
     "مدل یاکوبسون کارکردهای نشانه را در چارچوبی نزدیک به گونه‌شناسی پیرس صورت‌بندی می‌کند."),
    ("MC-345", "MC-348", "RELATED_TO", 0.75,
     "خوانندهٔ الگوی اکو، تفسیر را مرحلهٔ سوم سه‌گانهٔ نشانهٔ پیرس می‌داند."),

    ("MC-348", "MC-345", "RELATED_TO", 0.75,
     "نشانه‌شناسی سه‌گانه، بنیان نظری مفهوم همکاری تفسیری در خوانندهٔ الگوست."),
    ("MC-348", "MC-542", "RELATED_TO", 0.70,
     "مدل یاکوبسون و خوانندهٔ الگو هر دو بر نقش گیرنده در تکمیل معنا تأکید دارند."),
    ("MC-348", "MC-544", "RELATED_TO", 0.65,
     "تحلیل نشانه‌شناختی متن در مدل بولر به فهم تفاوت متن باز و بسته کمک می‌کند."),
    ("MC-348", "MC-546", "RELATED_TO", 0.65,
     "مدل تخصیص معنا، سازوکار همکاری خواننده در تولید معنا را توضیح می‌دهد."),

    ("MC-367", "MC-121", "RELATED_TO", 0.85,
     "تبلیغ‌گری مطبوعاتی نخستین مدل در گونه‌شناسی چهارگانهٔ روابط عمومی است."),
    ("MC-367", "MC-368", "RELATED_TO", 0.80,
     "مدل انتشار صادقانه اطلاعات، واکنشی به شیوهٔ فریب‌آمیز تبلیغ‌گری مطبوعاتی است."),
    ("MC-367", "MC-493", "RELATED_TO", 0.75,
     "مدل تبلیغات‌محور مطبوعات، ادامهٔ منطق جلب توجه رسانه‌ای در ساختار مطبوعاتی است."),
    ("MC-367", "MC-032", "RELATED_TO", 0.65,
     "منطق جلب توجه در تبلیغ‌گری با سازوکارهای اقتصاد توجه پیوند دارد."),
]

def main():
    c = pymysql.connect(host="127.0.0.1", port=3306, user="root",
                        password="433700", database=DB, charset="utf8mb4")
    cur = c.cursor()
    codes = sorted({x for row in REL for x in row[:2]})
    cur.execute("SELECT code,id FROM kb_entities WHERE code IN (%s)" % ",".join(["%s"] * len(codes)),
                codes)
    ids = dict(cur.fetchall())
    n = 0
    for src, tgt, rtype, conf, note in REL:
        if src not in ids or tgt not in ids:
            print("MISSING", src, tgt)
            continue
        cur.execute("SELECT id FROM kb_relations WHERE source_id=%s AND target_id=%s AND relation_type=%s AND asserted_by=%s",
                    (ids[src], ids[tgt], rtype, ASSERTED))
        if cur.fetchone():
            continue
        cur.execute("""INSERT INTO kb_relations
            (source_id,target_id,relation_type,assertion_status,asserted_by,verified_by,
             extraction_confidence,note,weight,status,created_at,updated_at)
            VALUES (%s,%s,%s,'verified',%s,%s,%s,%s,1,'active',%s,%s)""",
                    (ids[src], ids[tgt], rtype, ASSERTED, VERIFIED, conf, note, NOW, NOW))
        n += 1
    c.commit()
    print("inserted", n)
    c.close()

if __name__ == "__main__":
    main()
