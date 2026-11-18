# -*- coding: utf-8 -*-
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-rel-batch167-20261116"
NOW = "2026-11-16 00:00:00"

ROWS = [
    ("th-19", "MC-084", "RELATED_TO", "آدورنو صورت‌بند مفهوم صنعت فرهنگ است", 80, 90),
    ("th-19", "MC-333", "RELATED_TO", "نقد آدورنو بر مطالعات فرهنگی بریتانیا اثر گذاشت", 55, 60),
    ("th-19", "TX-029", "RELATED_TO", "نظریهٔ مطالعات فرهنگی با نقد صنعت فرهنگ آغاز شد", 60, 65),
    ("th-4", "MC-041", "RELATED_TO", "هابرماس نظریه‌پرداز حوزهٔ عمومی است", 80, 90),
    ("th-4", "MC-007", "RELATED_TO", "حوزهٔ عمومی و افکار عمومی در تحلیل هابرماس به هم گره می‌خورند", 55, 60),
    ("th-4", "MC-315", "RELATED_TO", "کنش ارتباطی، بدیل نظری مدل انتقالی یک‌سویه است", 50, 55),
    ("th-5", "MC-014", "RELATED_TO", "هال صورت‌بند مدل رمزگذاری و رمزگشایی است", 80, 90),
    ("th-5", "TX-066", "RELATED_TO", "نظریهٔ بازنمایی فرهنگی هال در کتاب ۱۹۹۷ نظام‌مند شد", 70, 80),
    ("th-5", "MC-461", "RELATED_TO", "بازنمایی دیگری و کلیشه، در سنت مطالعات فرهنگی هال تحلیل شد", 55, 60),
    ("th-17", "MC-047", "RELATED_TO", "بوردیو میدان روزنامه‌نگاری را تحلیل کرد", 75, 85),
    ("th-17", "TX-006", "RELATED_TO", "بوردیو بنیان‌گذار نظریهٔ میدان است", 80, 85),
    ("th-17", "CPT-070", "RELATED_TO", "عادت‌وارهٔ رسانه‌ای از مفهوم عادت‌وارهٔ بوردیو گرفته شده است", 60, 65),
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
            (sid, tid, rt, STAMP, "qoder-verify-batch167", conf / 100.0, note, w, NOW, NOW))
        ins += 1
    c.commit()
    print("inserted=%d skipped=%d" % (ins, skip))
    c.close()


if __name__ == "__main__":
    main()
