# -*- coding: utf-8 -*-
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-rel-batch173-20261116"
NOW = "2026-11-16 00:00:00"

ROWS = [
    ("th-21", "TX-027", "RELATED_TO", "بال-روکیچ هم‌صورت‌بند نظریهٔ وابستگی رسانه‌ای است", 85, 90),
    ("th-21", "MC-554", "RELATED_TO", "مدل وابستگی رسانه–مخاطب بر کار بال-روکیچ استوار است", 70, 75),
    ("th-21", "MC-318", "RELATED_TO", "نظریهٔ وابستگی به سیستم رسانه‌ای با بال-روکیچ پیوند دارد", 75, 80),
    ("th-33", "MC-195", "RELATED_TO", "گالتونگ بنیان‌گذار روزنامه‌نگاری صلح است", 85, 90),
    ("th-33", "CPT-238", "RELATED_TO", "ارزش‌های خبری گالتونگ و روگه سنگ بنای پژوهش انتخاب خبر است", 80, 85),
    ("th-33", "MC-013", "RELATED_TO", "ارزش‌های خبری گالتونگ در تبیین دروازه‌بانی خبر به کار می‌آید", 55, 60),
    ("th-34", "TX-060", "RELATED_TO", "نظریهٔ مسیرهای اقناع از مدل احتمال پردازش پتی سرچشمه می‌گیرد", 80, 85),
    ("th-34", "MDL-012", "RELATED_TO", "مدل احتمال اقناع صورت‌بندی پتی و کاچیوپو است", 85, 90),
    ("th-34", "MC-579", "RELATED_TO", "اثر تکرار در اقناع در پژوهش‌های پتی بررسی شد", 50, 55),
    ("th-34", "TX-016", "RELATED_TO", "مدل احتمال پردازش از نظریه‌های اصلی اقناع است", 65, 70),
    ("th-35", "MC-070", "RELATED_TO", "وایک صورت‌بند نظریهٔ معناسازی است", 85, 90),
    ("th-35", "MC-728", "RELATED_TO", "حس‌سازی سازمانی با معناسازی وایک پیوند نزدیک دارد", 70, 75),
    ("th-35", "MC-534", "RELATED_TO", "ارتباطات سازمانی به‌عنوان تولید معنا بر معناسازی وایک تکیه دارد", 65, 70),
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
            (sid, tid, rt, STAMP, "qoder-verify-batch173", conf / 100.0, note, w, NOW, NOW))
        ins += 1
    c.commit()
    print("inserted=%d skipped=%d" % (ins, skip))
    c.close()


if __name__ == "__main__":
    main()
