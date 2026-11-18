# -*- coding: utf-8 -*-
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-rel-batch171-20261116"
NOW = "2026-11-16 00:00:00"

ROWS = [
    ("th-8", "MC-342", "RELATED_TO", "گافمن صورت‌بند نظریهٔ نمایشی و مدیریت تأثیر است", 85, 90),
    ("th-8", "MC-328", "RELATED_TO", "مفهوم چارچوب در ارتباطات از گافمن وام گرفته شد", 80, 85),
    ("th-8", "MC-004", "RELATED_TO", "ریشهٔ چارچوب‌بندی رسانه‌ای در تحلیل چارچوب گافمن است", 75, 80),
    ("th-8", "CPT-244", "RELATED_TO", "چارچوب خبری به سنت تحلیل چارچوب گافمن تکیه دارد", 60, 65),
    ("th-22", "MC-114", "RELATED_TO", "جنکینز نظریه‌پرداز فرهنگ مشارکتی است", 85, 90),
    ("th-22", "MC-453", "RELATED_TO", "فرهنگ همگرایی عنوان و کانون نظریهٔ جنکینز است", 85, 90),
    ("th-22", "MC-487", "RELATED_TO", "پژوهش فرهنگ هواداران با شکارچیان متنی جنکینز آغاز شد", 80, 85),
    ("th-23", "MC-019", "RELATED_TO", "هیارد از نظریه‌پردازان اصلی رسانه‌ای‌شدن است", 85, 90),
    ("th-23", "MC-018", "RELATED_TO", "منطق رسانه مفهوم محوری رسانه‌ای‌شدن هیارد است", 80, 85),
    ("th-23", "CPT-048", "RELATED_TO", "منطق رسانه‌ای در چارچوب هیارد نفوذ رسانه در حوزه‌های دیگر را توضیح می‌دهد", 60, 65),
    ("th-23", "DSC-018", "RELATED_TO", "رسانه‌ای‌شدن دین یکی از حوزه‌های اصلی پژوهش هیارد است", 55, 60),
    ("th-24", "MC-099", "RELATED_TO", "کولدری نظریه‌پرداز دیدگاه آیینی ارتباطات است", 80, 85),
    ("th-24", "MDL-006", "RELATED_TO", "مدل ارتباطات آیینی با آیین‌های رسانه‌ای کولدری پیوند دارد", 65, 70),
    ("th-24", "CPT-298", "RELATED_TO", "ارتباطات آیینی از مفاهیم کلیدی رویکرد کولدری است", 65, 70),
    ("th-24", "MC-292", "RELATED_TO", "مرکزیت رسانه در نظریهٔ کولدری شکلی از قدرت نمادین است", 55, 60),
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
            (sid, tid, rt, STAMP, "qoder-verify-batch171", conf / 100.0, note, w, NOW, NOW))
        ins += 1
    c.commit()
    print("inserted=%d skipped=%d" % (ins, skip))
    c.close()


if __name__ == "__main__":
    main()
