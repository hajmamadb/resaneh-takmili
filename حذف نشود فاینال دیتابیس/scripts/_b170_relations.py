# -*- coding: utf-8 -*-
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-rel-batch170-20261116"
NOW = "2026-11-16 00:00:00"

ROWS = [
    ("th-12", "MC-328", "RELATED_TO", "انتمن صورت‌بند تعریف اثرگذار چارچوب در ارتباطات است", 85, 90),
    ("th-12", "MC-363", "RELATED_TO", "مدل فعال‌سازی آبشاری چارچوب‌ها از انتمن است", 85, 90),
    ("th-12", "MC-004", "RELATED_TO", "انتمن از نظریه‌پردازان اصلی چارچوب‌بندی رسانه‌ای است", 80, 85),
    ("th-12", "MC-001", "RELATED_TO", "چارچوب‌بندی انتمن در سنت برجسته‌سازی ریشه دارد", 60, 65),
    ("th-13", "MC-004", "RELATED_TO", "اینگار چارچوب رویدادمحور و موضوع‌محور خبر را صورت‌بندی کرد", 80, 85),
    ("th-13", "MC-001", "RELATED_TO", "آزمایش‌های اینگار و کیندر برجسته‌سازی خبری را آزمود", 75, 80),
    ("th-13", "MC-714", "RELATED_TO", "روش تحلیل چارچوب با تمایز اینگار عملیاتی شد", 55, 60),
    ("th-14", "MC-049", "RELATED_TO", "مک‌کوایل نظریه‌های هنجاری رسانه را نظام‌مند کرد", 80, 85),
    ("th-14", "MC-045", "RELATED_TO", "مسئولیت اجتماعی رسانه در چارچوب هنجاری مک‌کوایل جای دارد", 65, 70),
    ("th-14", "MC-008", "RELATED_TO", "مک‌کوایل پژوهش مخاطب را به سنت استفاده و خشنودی پیوند داد", 60, 65),
    ("th-14", "CPT-080", "RELATED_TO", "مخاطب فعال از مفاهیم کلیدی نظریهٔ مخاطب مک‌کوایل است", 55, 60),
    ("th-20", "TX-027", "RELATED_TO", "دفلور از صورت‌بندی‌کنندگان نظریهٔ وابستگی رسانه‌ای است", 85, 90),
    ("th-20", "MC-554", "RELATED_TO", "مدل وابستگی رسانه–مخاطب بر الگوی دفلور و بال-روکیچ استوار است", 70, 75),
    ("th-20", "TX-013", "RELATED_TO", "دفلور نظریهٔ وابستگی به رسانه را با بال-روکیچ ساخت", 85, 90),
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
            (sid, tid, rt, STAMP, "qoder-verify-batch170", conf / 100.0, note, w, NOW, NOW))
        ins += 1
    c.commit()
    print("inserted=%d skipped=%d" % (ins, skip))
    c.close()


if __name__ == "__main__":
    main()
