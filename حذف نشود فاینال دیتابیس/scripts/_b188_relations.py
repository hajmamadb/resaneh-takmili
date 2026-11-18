# -*- coding: utf-8 -*-
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-rel-batch188-20261116"
NOW = "2026-11-16 00:00:00"

ROWS = [
    ("MC-603", "MC-604", "RELATED_TO", "قانون مور و قانون گیندر دو روند مکمل رشد محاسبه و پهنای باند را توصیف می‌کنند", 75, 70),
    ("MC-603", "MC-602", "RELATED_TO", "قانون نیلسن رشد پهنای باند را با چارچوب رشد محاسباتی مور مقایسه می‌کند", 70, 65),
    ("MC-603", "MC-161", "RELATED_TO", "اقتصاد ابرستاره‌ها به صرفه‌جویی مقیاس ناشی از رشد توان محاسباتی وابسته است", 55, 50),
    ("MC-603", "MC-225", "RELATED_TO", "فرهنگ الگوریتمی بر ظرفیت محاسباتی رشد یافته تکیه دارد", 50, 45),
    ("MC-604", "MC-602", "RELATED_TO", "قانون نیلسن سنجش تجربی‌تری از همان روند رشد پهنای باند فراهم می‌کند", 70, 65),
    ("MC-604", "MC-603", "RELATED_TO", "فراوانی انتقال شبکه در کنار رشد توان پردازش اقتصاد رسانه را می‌سازد", 70, 65),
    ("MC-604", "MC-418", "RELATED_TO", "پهنای باند فراوان زیرساخت مشارکت و هوش جمعی آنلاین است", 50, 45),
    ("MC-604", "CPT-056", "RELATED_TO", "فراوانی پهنای باند الگوی مصرف رسانه‌ای را دگرگون می‌کند", 60, 55),
    ("MC-605", "MC-602", "RELATED_TO", "هر دو قاعده تلاش‌اند برای پیش‌بینی روند رشد فناوری رسانه", 55, 50),
    ("MC-605", "MC-225", "RELATED_TO", "هیجان کوتاه‌مدت و نفوذ آرام الگوریتم‌ها نمونهٔ امروزی قانون آمارا است", 55, 50),
    ("MC-605", "MC-277", "RELATED_TO", "گیمیفیکیشن نمونهٔ فناوری با بیش‌برآورد کوتاه‌مدت و نفوذ بلندمدت است", 55, 50),
    ("MC-605", "MC-418", "RELATED_TO", "وعدهٔ هوش جمعی نمونه‌ای از انتظار اغراق‌شدهٔ فناوری است", 50, 45),
    ("MC-151", "MC-153", "RELATED_TO", "استراتژی اقیانوس آبی در واکنش به چارچوب رقابتی پورتر شکل گرفت", 75, 70),
    ("MC-151", "CPT-180", "RELATED_TO", "مزیت رقابتی هدف اصلی سه استراتژی عمومی است", 80, 75),
    ("MC-151", "MC-171", "RELATED_TO", "هم‌رقابتی مرز رقابت و همکاری را که پورتر کمتر دیده پیچیده می‌کند", 60, 55),
    ("MC-151", "MC-161", "RELATED_TO", "اقتصاد برنده‌همه‌چیز موضع رقابتی رسانهٔ دیجیتال را بازتعریف می‌کند", 60, 55),
]


def main():
    c = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="433700",
                        database=DB, charset="utf8mb4")
    cur = c.cursor()
    codes = sorted({r[0] for r in ROWS} | {r[1] for r in ROWS})
    q = "SELECT code, id FROM kb_entities WHERE code IN (%s)" % ",".join(["%s"] * len(codes))
    cur.execute(q, codes)
    ids = dict(cur.fetchall())
    missing = [x for x in codes if x not in ids]
    if missing:
        raise SystemExit("missing codes: %s" % missing)
    ins = skip = 0
    for s, t, rt, note, conf, w in ROWS:
        sid, tid = ids[s], ids[t]
        cur.execute("""SELECT id FROM kb_relations WHERE source_id=%s AND target_id=%s
                       AND relation_type=%s""", (sid, tid, rt))
        if cur.fetchone():
            skip += 1
            continue
        cur.execute("""INSERT INTO kb_relations
            (source_id, target_id, relation_type, valid_from, valid_until, assertion_status,
             asserted_by, verified_by, extraction_confidence, note, weight, status, created_at, updated_at)
            VALUES (%s,%s,%s,NULL,NULL,'unverified',%s,%s,%s,%s,%s,'active',%s,%s)""",
            (sid, tid, rt, STAMP, "qoder-verify-batch188", conf / 100.0, note, w, NOW, NOW))
        ins += 1
    c.commit()
    print("inserted=%d skipped=%d" % (ins, skip))
    c.close()


if __name__ == "__main__":
    main()
