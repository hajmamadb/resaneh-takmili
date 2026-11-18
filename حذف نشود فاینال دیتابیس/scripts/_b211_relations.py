# -*- coding: utf-8 -*-
"""Batch 211 relations."""
import pymysql

DB = "resaname_kb_final_inspect"
ASSERTED = "qoder-rel-batch211-20261117"
VERIFIED = "qoder-verify-batch211"
NOW = "2026-11-17 00:00:00"

REL = [
    ("MC-304", "MC-026", "RELATED_TO", 0.85,
     "مدل خطی ارسطویی بنیان تاریخی جاذبه‌های بلاغی اخلاق، احساس و استدلال است."),
    ("MC-304", "TX-016", "RELATED_TO", 0.80,
     "فن خطابهٔ ارسطو یکی از ریشه‌های نظری پژوهش اقناع است."),
    ("MC-304", "MC-081", "RELATED_TO", 0.75,
     "مدل پنج‌پرسشی لاسول، چارچوب اقناعی ارسطویی را به تحلیل کارکردی ارتباط گسترش می‌دهد."),
    ("MC-304", "MC-135", "RELATED_TO", 0.70,
     "سلسله‌مراتب اثرات تبلیغ، سه‌گانهٔ شناخت، احساس و کنش ارسطویی را در قالب مراحل اثر بازسازی می‌کند."),

    ("MC-307", "MC-013", "RELATED_TO", 0.85,
     "دروازه‌بانی خبر، نقش کانال در مدل وستلی–مکلین را به پژوهش تجربی رسانه پیوند می‌دهد."),
    ("MC-307", "MC-463", "RELATED_TO", 0.85,
     "مدل وستلی–مکلین بر مثلث منبع-موضوع-گیرندهٔ نیوکامب بنا شده است."),
    ("MC-307", "MC-001", "RELATED_TO", 0.75,
     "گزینش کانال در مدل وستلی–مکلین سازوکاری نزدیک به برجسته‌سازی دستور کار است."),
    ("MC-307", "MC-704", "RELATED_TO", 0.75,
     "دروازه‌بانی الگوریتمی، بازتولید نقش کانال در مدل ۱۹۵۷ در محیط پلتفرمی است."),

    ("MC-310", "MC-462", "RELATED_TO", 0.80,
     "مدل تراکنشی بارنلوند و مدل حلقه‌ای شرام هر دو بازخورد و دوسویگی را در برابر مدل خطی برجسته می‌کنند."),
    ("MC-310", "MC-241", "RELATED_TO", 0.75,
     "تراکنش هم‌زمان با حضور اجتماعی و ادراک متقابل طرف‌ها پیوند دارد."),
    ("MC-310", "MDL-004", "RELATED_TO", 0.80,
     "مدل انتقال و تعامل، جایگاه مدل تراکنشی را در خانوادهٔ مدل‌های ارتباطی نشان می‌دهد."),
    ("MC-310", "MC-244", "RELATED_TO", 0.70,
     "در ارتباط با واسطهٔ رایانه، تراکنش هم‌زمان و آرمانی‌سازی متقابل سازوکار ابرشخصی را تقویت می‌کند."),

    ("MC-462", "MC-082", "RELATED_TO", 0.85,
     "مدل حلقه‌ای شرام بازنگری مدل خطی شانون و ویور با افزودن بازخورد است."),
    ("MC-462", "MC-310", "RELATED_TO", 0.80,
     "مدل تراکنشی بارنلوند دوسویگی حلقهٔ شرام را به هم‌زمانی کامل می‌رساند."),
    ("MC-462", "MDL-004", "RELATED_TO", 0.75,
     "مدل حلقه‌ای شرام نمونهٔ کلاسیک مدل تعاملی در خانوادهٔ مدل‌های ارتباطی است."),

    ("MC-463", "MC-307", "RELATED_TO", 0.85,
     "مدل وستلی–مکلین مثلث نیوکامب را با افزودن کانال و دروازه‌بانی گسترش داد."),
    ("MC-463", "MC-462", "RELATED_TO", 0.75,
     "هر دو مدل، تعادل و بازخورد را در تحلیل کنش ارتباطی وارد می‌کنند."),
    ("MC-463", "MC-576", "RELATED_TO", 0.70,
     "جست‌وجوی تعادل در مدل نیوکامب با سوگیری تأیید و شکل‌گیری اتاق پژواک پیوند دارد."),
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
