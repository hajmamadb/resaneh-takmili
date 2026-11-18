# -*- coding: utf-8 -*-
"""Batch 209 relations: MC-175, MC-185, MC-235, MC-244."""
import pymysql

DB = "resaname_kb_final_inspect"
ASSERTED = "qoder-rel-batch209-20261117"
VERIFIED = "qoder-verify-batch209"
NOW = "2026-11-17 00:00:00"

REL = [
    ("MC-175", "MC-173", "RELATED_TO", 0.80,
     "منحنی تجربه و چرخهٔ عمر محصول هر دو هزینه و قیمت را در طول چرخهٔ حیات بازار توضیح می‌دهند."),
    ("MC-175", "MC-036", "RELATED_TO", 0.85,
     "صرفه‌های مقیاس یکی از منابع بنیادین کاهش هزینهٔ واحد در منحنی تجربه است."),
    ("MC-175", "MC-069", "RELATED_TO", 0.75,
     "منحنی تجربه در صورت‌بندی راهبرد هزینه، یکی از ورودی‌های سنجش عملکرد در کارت امتیازی متوازن است."),
    ("MC-175", "MC-155", "RELATED_TO", 0.70,
     "یادگیری سازمانی سازوکار رفتاری پشت کاهش هزینه در منحنی تجربه را توضیح می‌دهد."),

    ("MC-185", "MC-151", "RELATED_TO", 0.80,
     "تمایز مکانی هتلینگ یکی از بنیان‌های نظری راهبردهای عمومی رقابتی و موقعیت‌یابی است."),
    ("MC-185", "CPT-165", "RELATED_TO", 0.85,
     "رقابت رسانه‌ای در انتخاب قالب و محتوا از منطق هم‌گرایی به مرکز در مدل هتلینگ پیروی می‌کند."),
    ("MC-185", "MC-169", "RELATED_TO", 0.75,
     "در پلتفرم‌ها، تمایز مکانی به تمایز در طراحی خدمت و الگوریتم مرتبط‌سازی ترجمه می‌شود."),
    ("MC-185", "MC-171", "RELATED_TO", 0.70,
     "رقابت مکانی می‌تواند هم‌زمان رقابتی و همکارانه باشد؛ مدل هتلینگ یک مورد خاص از این طیف است."),

    ("MC-235", "MC-072", "RELATED_TO", 0.85,
     "مدل‌سازی موضوعی گسترش محاسباتی تحلیل محتوای کمّی برای مجموعه‌های متنی بزرگ است."),
    ("MC-235", "MDL-071", "RELATED_TO", 0.80,
     "مدل‌سازی موضوعی و تحلیل محتوای کیفی هر دو مقوله‌بندی متن را هدف می‌گیرند، یکی استقرایی-محاسباتی و دیگری تفسیری."),
    ("MC-235", "CPT-199", "RELATED_TO", 0.85,
     "مدل‌سازی موضوعی یکی از کاربردهای شناخته‌شدهٔ داده‌کاوی متن در پژوهش ارتباطات است."),
    ("MC-235", "MC-718", "RELATED_TO", 0.75,
     "خروجی مدل‌سازی موضوعی ورودی رایج تحلیل شبکهٔ معنایی و اجتماعی گفت‌وگوهاست."),

    ("MC-244", "MC-241", "RELATED_TO", 0.85,
     "مدل ابرشخصی در گفت‌وگو با نظریهٔ حضور اجتماعی دربارهٔ اثر کانال بر صمیمیت شکل گرفت."),
    ("MC-244", "MC-243", "RELATED_TO", 0.80,
     "هر دو مدل نشان می‌دهند کاربران با گذشت زمان نشانه‌های اجتماعی را در کانال بازسازی می‌کنند."),
    ("MC-244", "MC-143", "RELATED_TO", 0.85,
     "عرضهٔ گزینشی خود در مدل ابرشخصی، کاربرد مدیریت برداشت در محیط دیجیتال است."),
    ("MC-244", "MC-429", "RELATED_TO", 0.80,
     "سایت‌های شبکه اجتماعی بستر اصلی عرضهٔ گزینشی خود و بازخورد تقویتی در مدل ابرشرصی هستند."),
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
