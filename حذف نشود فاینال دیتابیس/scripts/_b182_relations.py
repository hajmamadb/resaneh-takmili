# -*- coding: utf-8 -*-
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-rel-batch182-20261116"
NOW = "2026-11-16 00:00:00"

ROWS = [
    ("MC-570", "MC-484", "RELATED_TO", "پارادایم روایی بنیاد نظری تحلیل روایت است", 90, 90),
    ("MC-570", "MC-715", "RELATED_TO", "نشانه‌شناسی و روایت‌شناسی دو مسیر تحلیل معنای متن‌اند", 65, 60),
    ("MC-570", "MC-073", "RELATED_TO", "پژوهش روایی اغلب در طرح چندروشی با مصاحبه ترکیب می‌شود", 60, 55),
    ("MC-570", "MC-239", "RELATED_TO", "روش‌های ترکیبی برای سنجش پذیرش روایت به کار می‌روند", 60, 55),
    ("MC-722", "MC-716", "RELATED_TO", "قوم‌نگاری مخاطب از تجربهٔ زیستهٔ پدیدارشناختی الهام می‌گیرد", 65, 60),
    ("MC-722", "MC-237", "RELATED_TO", "نت‌نوگرافی تجربهٔ کاربران آنلاین را در بستر معنایی می‌کاود", 60, 55),
    ("MC-722", "MC-073", "RELATED_TO", "مصاحبهٔ پدیده‌شناختی در طرح‌های چندروشی به کار می‌رود", 60, 55),
    ("MC-722", "MC-714", "RELATED_TO", "تحلیل چارچوب و پدیدارشناسی هر دو به معناسازی مخاطب می‌پردازند", 60, 55),
    ("MC-723", "MC-072", "RELATED_TO", "تحلیل محتوای جنسیتی متداول‌ترین روش در فمینیسم رسانه‌ای است", 80, 80),
    ("MC-723", "MC-714", "RELATED_TO", "تحلیل چارچوب برای آشکارسازی بازنمایی جنسیتی به کار می‌رود", 70, 65),
    ("MC-723", "MC-716", "RELATED_TO", "قوم‌نگاری مخاطب تجربهٔ دریافت زنان را زمینه‌مند می‌کند", 70, 65),
    ("MC-723", "MC-114", "RELATED_TO", "فرهنگ مشارکتی و فمینیسم رسانه‌ای در مطالعهٔ طرفداران هم‌پوشانی دارند", 60, 55),
    ("MC-720", "MC-518", "RELATED_TO", "نظریهٔ کارکردها بنیاد کارکردگرایانهٔ تحلیل رسانه است", 85, 85),
    ("MC-720", "MC-072", "RELATED_TO", "تحلیل محتوای کارکردی از پارادایم کارکردگرایی الهام می‌گیرد", 65, 60),
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
            (sid, tid, rt, STAMP, "qoder-verify-batch182", conf / 100.0, note, w, NOW, NOW))
        ins += 1
    c.commit()
    print("inserted=%d skipped=%d" % (ins, skip))
    c.close()


if __name__ == "__main__":
    main()
