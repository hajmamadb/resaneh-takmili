# -*- coding: utf-8 -*-
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-rel-batch169-20261116"
NOW = "2026-11-16 00:00:00"

ROWS = [
    ("th-3", "MC-335", "RELATED_TO", "مک‌لوهان مفهوم دهکدهٔ جهانی را رواج داد", 80, 90),
    ("th-3", "MC-408", "RELATED_TO", "مک‌لوهان متهم اصلی جبرگرایی فناورانه در رسانه است", 65, 70),
    ("th-3", "MC-221", "RELATED_TO", "بوم‌شناسی رسانه از سنت مک‌لوهان زاده شد", 70, 80),
    ("th-31", "MC-221", "RELATED_TO", "پستمن نام‌گذار و بنیان‌گذار بوم‌شناسی رسانه است", 80, 90),
    ("th-31", "MC-084", "RELATED_TO", "نقد سرگرمی پستمن با نقد صنعت فرهنگ هم‌راستا است", 55, 60),
    ("th-31", "MC-408", "RELATED_TO", "نقد پستمن بر فن‌سالاری به جبرگرایی فناورانه نزدیک می‌شود", 50, 55),
    ("th-11", "MC-016", "RELATED_TO", "کاستلز نظریه‌پرداز جامعهٔ شبکه‌ای و قدرت ارتباطات است", 85, 90),
    ("th-11", "TX-033", "RELATED_TO", "نظریهٔ جامعهٔ شبکه‌ای بر سه‌گانهٔ عصر اطلاعات کاستلز استوار است", 75, 85),
    ("th-11", "MC-115", "RELATED_TO", "جامعهٔ شبکه‌ای با فردگرایی شبکه‌ای همبسته است", 55, 60),
    ("th-18", "MC-341", "RELATED_TO", "بودریار از نظریه‌پردازان شاخص پست‌مدرنیسم است", 70, 80),
    ("th-18", "MC-084", "RELATED_TO", "نقد وانموده و مصرف با نقد صنعت فرهنگ پیوند دارد", 55, 60),
    ("th-18", "MC-335", "RELATED_TO", "فراواقعیت در ادامهٔ ایدهٔ دهکدهٔ جهانی رسانه‌ای خوانده می‌شود", 50, 55),
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
            (sid, tid, rt, STAMP, "qoder-verify-batch169", conf / 100.0, note, w, NOW, NOW))
        ins += 1
    c.commit()
    print("inserted=%d skipped=%d" % (ins, skip))
    c.close()


if __name__ == "__main__":
    main()
