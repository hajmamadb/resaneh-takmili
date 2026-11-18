# -*- coding: utf-8 -*-
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-rel-batch168-20261116"
NOW = "2026-11-16 00:00:00"

ROWS = [
    ("th-6", "MC-006", "RELATED_TO", "گربنر بنیان‌گذار نظریهٔ کاشت است", 85, 90),
    ("th-6", "TX-011", "RELATED_TO", "مدل نظری کاشت بر پایهٔ شاخص‌های فرهنگی گربنر ساخته شد", 70, 80),
    ("th-6", "MC-201", "RELATED_TO", "جهان بی‌رحم کاشت‌شده با بی‌اعتمادی و مالیخولیای سیاسی همبسته است", 55, 60),
    ("th-7", "MC-007", "RELATED_TO", "نوئل-نویمان صورت‌بند نظریهٔ مارپیچ سکوت است", 85, 90),
    ("th-7", "MC-041", "RELATED_TO", "جو عمومی و حوزهٔ عمومی در تحلیل افکار عمومی به هم می‌رسند", 55, 60),
    ("th-7", "MC-001", "RELATED_TO", "ادراک جو عمومی با دستور کار رسانه پیوند دارد", 50, 55),
    ("th-28", "MC-551", "RELATED_TO", "کتز جریان دومرحله‌ای را تثبیت کرد", 80, 85),
    ("th-28", "MC-008", "RELATED_TO", "کتز صورت‌بند رویکرد کاربردها و خشنودی‌ها است", 80, 85),
    ("th-28", "MC-316", "RELATED_TO", "رهبران نظر واسط پیام رسانه‌اند", 70, 80),
    ("th-9", "MC-015", "RELATED_TO", "لازارسفلد بنیان‌گذار فرضیهٔ تأثیرات محدود است", 80, 90),
    ("th-9", "MC-551", "RELATED_TO", "پژوهش ایری کانتی به جریان دومرحله‌ای راه برد", 75, 85),
    ("th-9", "MC-316", "RELATED_TO", "رهبران نظر در ادامهٔ پژوهش لازارسفلد برجسته شدند", 65, 75),
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
            (sid, tid, rt, STAMP, "qoder-verify-batch168", conf / 100.0, note, w, NOW, NOW))
        ins += 1
    c.commit()
    print("inserted=%d skipped=%d" % (ins, skip))
    c.close()


if __name__ == "__main__":
    main()
