# -*- coding: utf-8 -*-
"""Batch 211 relations."""
import pymysql

DB = "resaname_kb_final_inspect"
ASSERTED = "qoder-rel-batch212-20261117"
VERIFIED = "qoder-verify-batch212"
NOW = "2026-11-17 00:00:00"

REL = [
    ("MC-464", "MC-082", "RELATED_TO", 0.80,
     "مدل برلو عناصر انتقالی شانون و ویور را با عوامل انسانی و فرهنگی دو سر مدل گسترش می‌دهد."),
    ("MC-464", "MC-307", "RELATED_TO", 0.75,
     "مدل وستلی–مکلین و مدل برلو هر دو بر نقش کانال و عوامل فرستنده و گیرنده تأکید دارند."),
    ("MC-464", "MC-462", "RELATED_TO", 0.75,
     "مدل حلقه‌ای شرام با افزودن بازخورد، محدودیت خطی مدل برلو را جبران می‌کند."),

    ("MC-309", "MC-082", "RELATED_TO", 0.75,
     "مدل ادراکی گربر با نقد انتقال سادهٔ سیگنال، گزینش و ادراک را وارد تحلیل ارتباط کرد."),
    ("MC-309", "MC-013", "RELATED_TO", 0.70,
     "گزینش ادراکی در مدل گربر با سازوکار دروازه‌بانی خبر پیوند دارد."),
    ("MC-309", "MC-304", "RELATED_TO", 0.65,
     "تأکید گربر بر ادراک گیرنده، نقدی بر تمرکز یک‌سویهٔ مدل خطی ارسطویی است."),

    ("MC-021", "TX-016", "RELATED_TO", 0.85,
     "مدل احتمال بسط یکی از چارچوب‌های بنیادین نظریهٔ اقناع است."),
    ("MC-021", "MC-135", "RELATED_TO", 0.70,
     "مسیرهای پردازش مدل احتمال بسط، تبیین شناختی مراحل سلسله‌مراتب اثرات را غنی می‌کند."),
    ("MC-021", "MC-107", "RELATED_TO", 0.80,
     "ظرفیت محدود پردازش، شرط توانایی در مدل احتمال بسط را توضیح می‌دهد."),
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
