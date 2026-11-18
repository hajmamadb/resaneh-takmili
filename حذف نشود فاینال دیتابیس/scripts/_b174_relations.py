# -*- coding: utf-8 -*-
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-rel-batch174-20261116"
NOW = "2026-11-16 00:00:00"

ROWS = [
    ("th-36", "MC-507", "RELATED_TO", "کونگ از پژوهشگران شاخص مدیریت رسانه است", 85, 90),
    ("th-36", "MC-039", "RELATED_TO", "پژوهش کونگ بر نوآوری در سازمان خبری متمرکز است", 60, 65),
    ("th-36", "DSC-015", "RELATED_TO", "مدیریت راهبردی رسانه در حوزهٔ مطالعات مدیریت رسانه جای دارد", 65, 70),
    ("th-37", "MC-731", "RELATED_TO", "پاپاچاریسی صورت‌بند مفهوم عمومیت‌های عاطفی است", 85, 90),
    ("th-37", "MC-041", "RELATED_TO", "نظریهٔ حوزهٔ خصوصی پاپاچاریسی نقدی بر الگوی حوزهٔ عمومی است", 75, 80),
    ("th-37", "MC-117", "RELATED_TO", "عموم‌های عاطفی در بستر جامعهٔ پلتفرمی شکل می‌گیرند", 50, 55),
    ("th-39", "MC-415", "RELATED_TO", "نیبورگ از نظریه‌پردازان پلتفرمیزاسیون تولید فرهنگی است", 85, 90),
    ("th-39", "MC-117", "RELATED_TO", "پلتفرمی‌شدن تولید فرهنگی به جامعهٔ پلتفرمی پیوند دارد", 55, 60),
    ("th-39", "CPT-158", "RELATED_TO", "اقتصاد پلتفرمی زمینهٔ تحلیل کالای فرهنگی اقتضایی است", 60, 65),
    ("MC-101", "MC-010", "RELATED_TO", "اثر رسانهٔ خصمانه با اثر شخص سوم هم‌خانواده است", 65, 70),
    ("MC-101", "MC-558", "RELATED_TO", "فرضیهٔ اثر شخص سوم در تبیین ادراک خصمانه به کار می‌آید", 60, 65),
    ("MC-101", "MC-337", "RELATED_TO", "ادراک رسانهٔ خصمانه شکلی از سوگیری ادراکی رسانه است", 70, 75),
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
            (sid, tid, rt, STAMP, "qoder-verify-batch174", conf / 100.0, note, w, NOW, NOW))
        ins += 1
    c.commit()
    print("inserted=%d skipped=%d" % (ins, skip))
    c.close()


if __name__ == "__main__":
    main()
