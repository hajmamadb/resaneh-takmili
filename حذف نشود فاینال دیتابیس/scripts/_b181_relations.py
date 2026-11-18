# -*- coding: utf-8 -*-
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-rel-batch181-20261116"
NOW = "2026-11-16 00:00:00"

ROWS = [
    ("MC-715", "MC-714", "RELATED_TO", "نشانه‌شناسی و تحلیل چارچوب هر دو روش‌شناسی تفسیر معنای متن‌اند", 75, 70),
    ("MC-715", "MC-072", "RELATED_TO", "تحلیل محتوای کیفی اغلب با تحلیل نشانه‌شناختی تکمیل می‌شود", 65, 60),
    ("MC-715", "MC-484", "RELATED_TO", "تحلیل روایت و نشانه‌شناسی در مطالعهٔ متن رسانه‌ای هم‌پوشانی دارند", 70, 65),
    ("MC-715", "MC-328", "RELATED_TO", "نشانه‌شناسی ابزار تحلیل چارچوب‌های معنایی رسانه است", 70, 65),
    ("MC-719", "MC-073", "RELATED_TO", "آزمایش یکی از رشته‌های رایج در طرح‌های چندروشی است", 75, 70),
    ("MC-719", "MC-239", "RELATED_TO", "روش‌های ترکیبی آزمایش را با پیمایش و مصاحبه پیوند می‌دهند", 80, 80),
    ("MC-719", "MC-072", "RELATED_TO", "آزمایش اغلب با تحلیل محتوای محرک رسانه‌ای ترکیب می‌شود", 65, 60),
    ("MC-719", "MC-714", "RELATED_TO", "اثر چارچوب اغلب در طرح آزمایشی سنجیده می‌شود", 80, 80),
    ("MC-233", "MC-072", "RELATED_TO", "تحلیل محتوای پیام‌های توسعه در برنامه‌های ارتباطی به کار می‌رود", 65, 60),
    ("MC-233", "MC-073", "RELATED_TO", "ارزیابی برنامهٔ توسعه اغلب با طرح چندروشی انجام می‌شود", 65, 60),
    ("MC-233", "MC-237", "RELATED_TO", "نت‌نوگرافی اجتماعات آنلاین توسعه‌ای مکمل ارزیابی برنامه است", 60, 55),
    ("MC-233", "MC-716", "RELATED_TO", "قوم‌نگاری مخاطب مصرف پیام توسعه را در بافت محلی می‌کاود", 60, 55),
    ("MC-015", "MC-072", "RELATED_TO", "تحلیل محتوا برای سنجش محتوای رسانه در پژوهش اثرات محدود به کار می‌رود", 70, 65),
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
            (sid, tid, rt, STAMP, "qoder-verify-batch181", conf / 100.0, note, w, NOW, NOW))
        ins += 1
    c.commit()
    print("inserted=%d skipped=%d" % (ins, skip))
    c.close()


if __name__ == "__main__":
    main()
