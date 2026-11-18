# -*- coding: utf-8 -*-
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-rel-batch178-20261116"
NOW = "2026-11-16 00:00:00"

ROWS = [
    ("MC-639", "MC-085", "RELATED_TO", "جهش محبوبیت در بحران، نمونه‌ای از شکل‌گیری ادراک عمومی در محیط رسانه‌ای است", 75, 75),
    ("MC-639", "TX-063", "RELATED_TO", "اثر گردهمایی سازوکار افکار عمومی در مدیریت بحران است", 80, 80),
    ("MC-639", "MC-004", "RELATED_TO", "پوشش چارچوب‌بندی‌شدهٔ تهدید در اندازهٔ جهش نقش دارد", 75, 70),
    ("MC-639", "MC-370", "RELATED_TO", "هم‌سویی رسانه و نخبگان در بحران با دستکاری افکار عمومی هم‌پوشانی دارد", 65, 60),
    ("MC-072", "MC-073", "RELATED_TO", "تحلیل محتوا اغلب با سه‌سوسازی در پژوهش ترکیبی به کار می‌رود", 80, 80),
    ("MC-072", "MC-714", "RELATED_TO", "تحلیل محتوا و تحلیل چارچوب در سنجش متن رسانه‌ای هم‌پوشانی دارند", 85, 85),
    ("MC-072", "MC-484", "RELATED_TO", "تحلیل محتوای کیفی با تحلیل روایت در بررسی متن پیوند دارد", 70, 65),
    ("MC-072", "MC-695", "RELATED_TO", "تحلیل محتوا برای آزمون بازتاب یا برساخت خبر به کار می‌رود", 65, 60),
    ("MC-073", "MC-072", "RELATED_TO", "سه‌سوسازی روش‌شناختی با تحلیل محتوا به‌عنوان یکی از اضلاع کاربرد دارد", 80, 80),
    ("MC-073", "MC-237", "RELATED_TO", "نت‌نوگرافی با سه‌سوسازی دادهٔ آنلاین و آفلاین اعتبار می‌یابد", 70, 65),
    ("MC-073", "MC-718", "RELATED_TO", "تحلیل شبکهٔ اجتماعی یکی از منابع دادهٔ مکمل در طرح سه‌سوسازی است", 65, 60),
    ("MC-073", "MC-714", "RELATED_TO", "تحلیل چارچوب در پژوهش‌های چندروشی با سه‌سوسازی تقویت می‌شود", 65, 60),
    ("MC-234", "CPT-063", "RELATED_TO", "مشارکت جامعهٔ درگیر هستهٔ پژوهش کنش‌مشارکتی است", 90, 90),
    ("MC-234", "MC-114", "RELATED_TO", "فرهنگ مشارکتی بستر رشد پژوهش کنش‌مشارکتی است", 75, 70),
    ("MC-234", "MDL-026", "RELATED_TO", "مدل مشارکت مخاطب در طراحی مرحلهٔ اقدام پژوهش کنش به کار می‌رود", 70, 65),
    ("MC-234", "MC-073", "RELATED_TO", "پژوهش کنش‌مشارکتی با سه‌سوسازی دادهٔ مشاهده، مصاحبه و اقدام اعتبار می‌یابد", 70, 65),
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
            (sid, tid, rt, STAMP, "qoder-verify-batch178", conf / 100.0, note, w, NOW, NOW))
        ins += 1
    c.commit()
    print("inserted=%d skipped=%d" % (ins, skip))
    c.close()


if __name__ == "__main__":
    main()
