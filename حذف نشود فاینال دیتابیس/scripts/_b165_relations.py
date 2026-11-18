# -*- coding: utf-8 -*-
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-rel-batch165-20261116"
NOW = "2026-11-16 00:00:00"

ROWS = [
    ("MC-490", "MC-192", "RELATED_TO", "رکورد تکراری فرضیهٔ نمایه‌سازی؛ ارجاع به رکورد اصلی", 60, 85),
    ("MC-490", "MC-001", "RELATED_TO", "نمایه‌سازی، دامنهٔ دستور کار رسمی را به خبر پیوند می‌دهد", 60, 70),
    ("MC-490", "MC-007", "RELATED_TO", "خاموشی صداهای بیرون دامنه، با مارپیچ سکوت همسو است", 55, 60),
    ("MC-564", "MC-565", "RELATED_TO", "محرک آزارندهٔ ناکامی، محرک موقعیتی پرخاشگری است", 65, 80),
    ("MC-564", "MC-563", "RELATED_TO", "تخلیهٔ هیجانی، فرضیهٔ رقیب دربارهٔ سرنوشت خشم است", 55, 65),
    ("MC-564", "MC-535", "RELATED_TO", "برانگیختگی انتقال‌یافته، شدت پاسخ به محرک را تعدیل می‌کند", 55, 70),
    ("MC-565", "MC-564", "RELATED_TO", "سرکوب و محرک، صورت‌بندی دقیق‌تر پیوند ناکامی و پرخاشگری است", 65, 80),
    ("MC-565", "MC-563", "RELATED_TO", "کاتارسیس، پاسخ رقیب به پرسش از سرنوشت خشم ناکامی است", 55, 70),
    ("MC-565", "MC-201", "RELATED_TO", "ناکامی مزمن، با بی‌اعتمادی و مالیخولیای سیاسی همبسته است", 50, 55),
    ("MC-080", "MC-120", "RELATED_TO", "دسترسی نابرابر به داده، شکاف دیجیتال را بازتولید می‌کند", 55, 55),
    ("MC-080", "MC-001", "RELATED_TO", "دادهٔ جست‌وجو و خبر، مطالعهٔ دستور کار را در مقیاس بزرگ ممکن کرد", 50, 50),
    ("MC-080", "MC-002", "RELATED_TO", "دادهٔ شبکه‌ای، برجسته‌سازی شبکه‌ای را آزمون‌پذیر می‌کند", 55, 60),
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
                       AND relation_type=%s AND asserted_by=%s""", (sid, tid, rt, STAMP))
        if cur.fetchone():
            skip += 1
            continue
        cur.execute("""INSERT INTO kb_relations
            (source_id, target_id, relation_type, valid_from, valid_until, assertion_status,
             asserted_by, verified_by, extraction_confidence, note, weight, status, created_at, updated_at)
            VALUES (%s,%s,%s,NULL,NULL,'unverified',%s,%s,%s,%s,%s,'active',%s,%s)""",
            (sid, tid, rt, STAMP, "qoder-verify-batch165", conf / 100.0, note, w, NOW, NOW))
        ins += 1
    c.commit()
    print("inserted=%d skipped=%d" % (ins, skip))
    c.close()


if __name__ == "__main__":
    main()
