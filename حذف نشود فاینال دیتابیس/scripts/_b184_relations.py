# -*- coding: utf-8 -*-
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-rel-batch184-20261116"
NOW = "2026-11-16 00:00:00"

ROWS = [
    ("pub-icjr", "MC-239", "RELATED_TO", "نشریهٔ دسترسی‌آزاد چندرشته‌ای محل انتشار پژوهش‌های ترکیبی ارتباطات است", 55, 50),
    ("pub-icjr", "MC-714", "RELATED_TO", "تحلیل چارچوب از موضوع‌های پرتکرار این نشریه است", 50, 45),
    ("pub-icjr", "MC-718", "RELATED_TO", "تحلیل شبکه و روش‌های رایانشی در آن جایگاه رو به رشد دارد", 45, 40),
    ("pub-joc", "MC-015", "RELATED_TO", "پارادایم اثرات محدود در این نشریه نقد و بازخوانی شده است", 65, 60),
    ("pub-joc", "MC-328", "RELATED_TO", "نظریهٔ چارچوب‌بندی در آن گسترش یافته است", 60, 55),
    ("pub-joc", "MC-570", "RELATED_TO", "پارادایم روایی از مباحث نظری رایج آن است", 55, 50),
    ("pub-joc", "MC-484", "RELATED_TO", "تحلیل روایت در پژوهش‌های خبری آن به کار می‌رود", 55, 50),
    ("pub-journal-adv-studies", "MC-369", "RELATED_TO", "مهندسی رضایت پیوند نزدیکی با پژوهش تبلیغات دارد", 60, 55),
    ("pub-journal-adv-studies", "MC-265", "RELATED_TO", "خالص نمرهٔ مروّج در پژوهش وفاداری تبلیغاتی به کار می‌رود", 55, 50),
    ("pub-journal-adv-studies", "MC-004", "RELATED_TO", "چارچوب‌بندی پیام از مباحث محوری تبلیغات است", 60, 55),
    ("pub-journal-adv-studies", "MC-277", "RELATED_TO", "گیمیفیکیشن در پژوهش تبلیغات دیجیتال بررسی می‌شود", 50, 45),
    ("pub-journalism-studies", "MC-484", "RELATED_TO", "تحلیل روایت خبری از روش‌های رایج این نشریه است", 60, 55),
    ("pub-journalism-studies", "MC-004", "RELATED_TO", "چارچوب‌بندی خبر از موضوع‌های اصلی مطالعات روزنامه‌نگاری است", 65, 60),
    ("pub-journalism-studies", "MC-072", "RELATED_TO", "تحلیل محتوای خبر پرکاربردترین روش در آن است", 65, 60),
    ("pub-journalism-studies", "MC-073", "RELATED_TO", "طرح‌های چندروشی در پژوهش تحریریه به کار می‌روند", 50, 45),
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
            (sid, tid, rt, STAMP, "qoder-verify-batch184", conf / 100.0, note, w, NOW, NOW))
        ins += 1
    c.commit()
    print("inserted=%d skipped=%d" % (ins, skip))
    c.close()


if __name__ == "__main__":
    main()
