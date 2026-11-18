# -*- coding: utf-8 -*-
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-rel-batch185-20261116"
NOW = "2026-11-16 00:00:00"

ROWS = [
    ("pub-mass-comm-society", "MC-004", "RELATED_TO", "پژوهش چارچوب‌بندی رسانه‌ای از موضوع‌های رایج در این نشریه است", 70, 65),
    ("pub-mass-comm-society", "MC-328", "RELATED_TO", "چارچوب‌بندی به‌عنوان نظریهٔ خبر در دامنهٔ نشریه جای دارد", 65, 60),
    ("pub-mass-comm-society", "MC-072", "RELATED_TO", "تحلیل محتوا از روش‌های پرکاربرد در مقاله‌های نشریه است", 70, 65),
    ("pub-mass-comm-society", "MC-369", "RELATED_TO", "مهندسی رضایت نمونهٔ پژوهش تاریخی رسانه و افکار عمومی است", 60, 55),
    ("pub-media-culture", "MC-333", "RELATED_TO", "نشریه در سنت مطالعات فرهنگی بریتانیا منتشر می‌شود", 85, 80),
    ("pub-media-culture", "MC-723", "RELATED_TO", "فمینیسم رسانه‌ای از حوزه‌های پرتواتر در نشریه است", 75, 70),
    ("pub-media-culture", "MC-725", "RELATED_TO", "تحلیل پساساختارگرایانهٔ متن در نشریه جایگاه دارد", 65, 60),
    ("pub-media-culture", "MC-484", "RELATED_TO", "تحلیل روایت از روش‌های تفسیری رایج در مطالعات فرهنگی رسانه است", 65, 60),
    ("pub-new-media-society", "MC-717", "RELATED_TO", "قوم‌نگاری رسانه‌های دیجیتال از روش‌های محوری پژوهش اینترنت است", 75, 70),
    ("pub-new-media-society", "MC-718", "RELATED_TO", "تحلیل شبکهٔ اجتماعی برای مطالعهٔ تعامل پلتفرمی به کار می‌رود", 70, 65),
    ("pub-new-media-society", "MC-237", "RELATED_TO", "نت‌نوگرافی روش مطالعهٔ جوامع آنلاین است", 75, 70),
    ("pub-new-media-society", "MC-716", "RELATED_TO", "قوم‌نگاری مخاطب در پژوهش مصرف رسانهٔ دیجیتال کاربرد دارد", 60, 55),
    ("pub-public-relation-qr", "MC-121", "RELATED_TO", "مدل‌های چهارگانه روابط عمومی در ادبیات حرفه‌ای نشریه بازتاب یافته است", 65, 60),
    ("pub-public-relation-qr", "MC-141", "RELATED_TO", "نظریهٔ برتری روابط عمومی از چارچوب‌های مرجع بحث حرفه‌ای است", 65, 60),
    ("pub-public-relation-qr", "MC-377", "RELATED_TO", "نقش‌های روابط عمومی موضوع مقاله‌های کاربردی نشریه است", 70, 65),
    ("pub-public-relation-qr", "MC-699", "RELATED_TO", "نظریهٔ همزیستی خبر و روابط عمومی به بحث روابط رسانه‌ای پیوند دارد", 60, 55),
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
            (sid, tid, rt, STAMP, "qoder-verify-batch185", conf / 100.0, note, w, NOW, NOW))
        ins += 1
    c.commit()
    print("inserted=%d skipped=%d" % (ins, skip))
    c.close()


if __name__ == "__main__":
    main()
