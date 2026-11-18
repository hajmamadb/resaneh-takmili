# -*- coding: utf-8 -*-
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-rel-batch180-20261116"
NOW = "2026-11-16 00:00:00"

ROWS = [
    ("MC-716", "MC-237", "RELATED_TO", "قوم‌نگاری مخاطب سنت خویشاوند نت‌نوگرافی است", 85, 85),
    ("MC-716", "MC-114", "RELATED_TO", "قوم‌نگاری مخاطب فرهنگ مشارکتی طرفداران را می‌کاود", 75, 70),
    ("MC-716", "MC-073", "RELATED_TO", "قوم‌نگاری مخاطب در طرح‌های چندروشی با مصاحبه ترکیب می‌شود", 60, 55),
    ("MC-717", "MC-237", "RELATED_TO", "قوم‌نگاری رسانه‌های دیجیتال بسط نت‌نوگرافی در محیط شبکه‌ای است", 90, 90),
    ("MC-717", "MC-718", "RELATED_TO", "تحلیل شبکهٔ اجتماعی دادهٔ ساختاری مکمل قوم‌نگاری دیجیتال است", 65, 60),
    ("MC-717", "MC-716", "RELATED_TO", "قوم‌نگاری دیجیتال شکل آنلاین قوم‌نگاری مخاطب است", 85, 80),
    ("MC-718", "MC-073", "RELATED_TO", "تحلیل شبکهٔ اجتماعی در طرح‌های ترکیبی با روش کیفی پیوند می‌خورد", 60, 55),
    ("MC-718", "MC-237", "RELATED_TO", "سنجه‌های شبکه تفسیر نت‌نوگرافی از اجتماعات آنلاین را نظام‌مند می‌کند", 65, 60),
    ("MC-718", "MC-717", "RELATED_TO", "تحلیل شبکه و قوم‌نگاری دیجیتال در مطالعهٔ پلتفرم مکمل‌اند", 70, 65),
    ("MC-718", "MDL-026", "RELATED_TO", "مدل مشارکت مخاطب برای تفسیر الگوی شبکهٔ تعامل به کار می‌رود", 65, 60),
    ("MC-714", "MC-004", "RELATED_TO", "تحلیل چارچوب اقدام روش‌شناختی نظریهٔ چارچوب‌بندی رسانه‌ای است", 90, 90),
    ("MC-714", "MC-328", "RELATED_TO", "تحلیل چارچوب روش عملیاتی نظریهٔ چارچوب‌بندی است", 90, 90),
    ("MC-714", "CPT-244", "RELATED_TO", "چارچوب خبری واحد تحلیل رایج در تحلیل چارچوب است", 85, 80),
    ("MC-714", "MC-072", "RELATED_TO", "تحلیل چارچوب اغلب با تحلیل محتوا اجرا می‌شود", 80, 80),
    ("MC-714", "MC-073", "RELATED_TO", "تحلیل چارچوب در طرح‌های چندروشی با مصاحبه و پیمایش ترکیب می‌شود", 65, 60),
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
            (sid, tid, rt, STAMP, "qoder-verify-batch180", conf / 100.0, note, w, NOW, NOW))
        ins += 1
    c.commit()
    print("inserted=%d skipped=%d" % (ins, skip))
    c.close()


if __name__ == "__main__":
    main()
