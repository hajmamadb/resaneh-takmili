# -*- coding: utf-8 -*-
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-rel-batch172-20261116"
NOW = "2026-11-16 00:00:00"

ROWS = [
    ("th-25", "MC-575", "RELATED_TO", "نظریهٔ چشم‌انداز کانمن بنیاد اثر چارچوب تصمیم است", 70, 75),
    ("th-25", "MC-129", "RELATED_TO", "زیان‌گریزی و ادراک احتمال، ارتباطات ریسک را توضیح می‌دهد", 60, 65),
    ("th-25", "MC-123", "RELATED_TO", "داوری شهودی مخاطب در تقویت اجتماعی ادراک ریسک نقش دارد", 50, 55),
    ("th-26", "MC-018", "RELATED_TO", "آلتهاید از صورت‌بندی‌کنندگان نظریهٔ منطق رسانه است", 85, 90),
    ("th-26", "CPT-048", "RELATED_TO", "منطق رسانه‌ای مفهوم محوری آلتهاید و اسنو است", 80, 85),
    ("th-26", "TX-036", "RELATED_TO", "منطق رسانه در پلتفرم‌های اجتماعی امتداد یافته است", 50, 55),
    ("th-29", "MC-011", "RELATED_TO", "تیچنور صورت‌بند فرضیهٔ شکاف دانش است", 85, 90),
    ("th-29", "MC-120", "RELATED_TO", "فرضیهٔ شکاف دانش پیشینهٔ پژوهشی شکاف دیجیتال است", 55, 60),
    ("th-29", "MC-087", "RELATED_TO", "مواجهه و پردازش گزینشی از شرایط اقتضایی شکاف دانش است", 50, 55),
    ("th-30", "MC-013", "RELATED_TO", "مطالعهٔ دروازه‌بان وایت نقطهٔ آغاز نظریهٔ دروازه‌بانی خبر است", 85, 90),
    ("th-30", "CPT-240", "RELATED_TO", "دروازه‌بانی مفهوم کلیدی وایت است", 80, 85),
    ("th-30", "MC-704", "RELATED_TO", "دروازه‌بانی الگوریتمی امتداد دیجیتال انتخاب خبر است", 45, 50),
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
            (sid, tid, rt, STAMP, "qoder-verify-batch172", conf / 100.0, note, w, NOW, NOW))
        ins += 1
    c.commit()
    print("inserted=%d skipped=%d" % (ins, skip))
    c.close()


if __name__ == "__main__":
    main()
