# -*- coding: utf-8 -*-
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-rel-batch179-20261116"
NOW = "2026-11-16 00:00:00"

ROWS = [
    ("MC-237", "MC-716", "RELATED_TO", "نت‌نوگرافی نسخهٔ آنلاین قوم‌نگاری مخاطب است", 85, 85),
    ("MC-237", "MC-717", "RELATED_TO", "قوم‌نگاری رسانه‌های دیجیتال چارچوب نزدیک به نت‌نوگرافی است", 85, 80),
    ("MC-237", "MC-718", "RELATED_TO", "تحلیل شبکهٔ اجتماعی دادهٔ تعاملی مکمل نت‌نوگرافی فراهم می‌کند", 65, 60),
    ("MC-237", "MC-072", "RELATED_TO", "نت‌نوگرافی با تحلیل محتوای کیفی متون آنلاین تکمیل می‌شود", 65, 60),
    ("MC-239", "MC-073", "RELATED_TO", "روش‌های ترکیبی چارچوب عملیاتی سه‌سوسازی است", 85, 85),
    ("MC-239", "MC-072", "RELATED_TO", "تحلیل محتوا یکی از رشته‌های رایج در طرح‌های ترکیبی است", 65, 60),
    ("MC-239", "MC-714", "RELATED_TO", "تحلیل چارچوب در طرح‌های ترکیبی با پیمایش پیوند می‌خورد", 65, 60),
    ("MC-239", "MC-237", "RELATED_TO", "نت‌نوگرافی می‌تواند رشتهٔ کیفی یک طرح ترکیبی باشد", 65, 60),
    ("MC-267", "MDL-026", "RELATED_TO", "مدل مشارکت مخاطب برای تفسیر منحنی نگهداشت به کار می‌رود", 70, 65),
    ("MC-267", "CPT-063", "RELATED_TO", "نگهداشت کاربر شکل پایدار مشارکت مخاطب است", 70, 65),
    ("MC-267", "MC-073", "RELATED_TO", "تحلیل کوهورت در طرح‌های چندروشی با دادهٔ مصاحبه تقویت می‌شود", 60, 55),
    ("MC-267", "MC-239", "RELATED_TO", "تحلیل کوهورت و روش‌های ترکیبی در پژوهش مخاطب هم‌پوشانی دارند", 55, 50),
    ("MC-484", "MC-072", "RELATED_TO", "تحلیل روایت و تحلیل محتوا در بررسی متن رسانه‌ای مکمل‌اند", 80, 80),
    ("MC-484", "MC-073", "RELATED_TO", "تحلیل روایت یکی از روش‌های قابل ترکیب در سه‌سوسازی است", 65, 60),
    ("MC-484", "MC-714", "RELATED_TO", "تحلیل روایت در تحلیل چارچوب برای شناسایی داستان‌های خبری به کار می‌رود", 75, 70),
    ("MC-484", "CPT-244", "RELATED_TO", "چارچوب خبری اغلب در قالب روایت‌های تکرارشده ساخته می‌شود", 65, 60),
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
            (sid, tid, rt, STAMP, "qoder-verify-batch179", conf / 100.0, note, w, NOW, NOW))
        ins += 1
    c.commit()
    print("inserted=%d skipped=%d" % (ins, skip))
    c.close()


if __name__ == "__main__":
    main()
