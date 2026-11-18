# -*- coding: utf-8 -*-
"""Batch 210 relations: MC-274, MC-275, MC-276, MC-281."""
import pymysql

DB = "resaname_kb_final_inspect"
ASSERTED = "qoder-rel-batch210-20261117"
VERIFIED = "qoder-verify-batch210"
NOW = "2026-11-17 00:00:00"

REL = [
    ("MC-274", "MC-275", "RELATED_TO", 0.85,
     "مدل قلاب چهارچوب فاگ را با افزودن سرمایه‌گذاری و پاداش متغیر به چرخهٔ عادت توسعه می‌دهد."),
    ("MC-274", "TX-016", "RELATED_TO", 0.80,
     "مدل قلاب کاربرد طراحی محصول از نظریهٔ اقناع در محیط دیجیتال است."),
    ("MC-274", "CPT-070", "RELATED_TO", 0.85,
     "هدف نهایی چرخهٔ قلاب، شکل‌گیری عادت رسانه‌ای در کاربر است."),
    ("MC-274", "MC-032", "RELATED_TO", 0.75,
     "محصولات عادت‌ساز از سازوکارهای اقتصاد توجه برای حفظ زمان و بازگشت کاربر بهره می‌برند."),

    ("MC-275", "MC-274", "RELATED_TO", 0.85,
     "مدل قلاب، مدل رفتاری فاگ را به‌عنوان بنیان نظری به‌کار می‌گیرد."),
    ("MC-275", "MC-137", "RELATED_TO", 0.80,
     "هر دو چارچوب بر نقش محرک و طراحی انتخاب در وقوع رفتار تأکید دارند."),
    ("MC-275", "MC-027", "RELATED_TO", 0.75,
     "مدل فاگ و نظریهٔ رفتار برنامه‌ریزی‌شده هر دو انگیزش و توان کنترل را در توضیح رفتار دخیل می‌دانند."),
    ("MC-275", "TX-016", "RELATED_TO", 0.80,
     "مدل رفتاری فاگ در خانوادهٔ چارچوب‌های طراحی اقناعی جای می‌گیرد."),

    ("MC-276", "MC-288", "RELATED_TO", 0.80,
     "طراحی حساس به ارزش، چارچوب هنجاری نقد الگوهای فریبنده است."),
    ("MC-276", "MC-137", "RELATED_TO", 0.85,
     "الگوهای فریبنده شکل دستکاری‌شدهٔ معماری انتخاب‌اند که به ضرر کاربر عمل می‌کند."),
    ("MC-276", "TX-016", "RELATED_TO", 0.80,
     "الگوهای فریبنده ابزار اقناع پنهان و نامتقارن‌اند و در نقد اقناع دستکاری‌آمیز بررسی می‌شوند."),
    ("MC-276", "MC-274", "RELATED_TO", 0.70,
     "مرز میان طراحی عادت‌ساز و طراحی فریبنده، محل تلاقی مدل قلاب و پژوهش الگوهای فریبنده است."),

    ("MC-281", "MC-284", "RELATED_TO", 0.85,
     "کتاب نوبل یکی از بنیان‌های تجربی بحث عدالت داده و بازنمایی الگوریتمی است."),
    ("MC-281", "MC-668", "RELATED_TO", 0.80,
     "سوگیری رتبه‌بندی جستجو نمونهٔ عملی تبعیض الگوریتمی است."),
    ("MC-281", "MC-667", "RELATED_TO", 0.80,
     "فرانمایی و نامرئی‌سازی در جستجو سازوکاری از برجستگی الگوریتمی است."),
    ("MC-281", "MC-230", "RELATED_TO", 0.80,
     "نقد نوبل بر الگوریتم جستجو، ضرورت حاکمیت و پاسخ‌گویی الگوریتمی را تقویت می‌کند."),
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
