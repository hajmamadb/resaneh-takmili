# -*- coding: utf-8 -*-
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-rel-batch187-20261116"
NOW = "2026-11-16 00:00:00"

ROWS = [
    ("MC-473", "MC-727", "RELATED_TO", "تمایز رسانهٔ گرم و سرد در سنت فلسفه و بوم‌شناسی رسانه جای دارد", 75, 70),
    ("MC-473", "MC-339", "RELATED_TO", "نقد تلویزیون پستمن بر تحلیل مکلوهان از رسانهٔ سرد تکیه دارد", 65, 60),
    ("MC-473", "MC-355", "RELATED_TO", "مشارکت مخاطب در رسانهٔ سرد با مفهوم مخاطب فعال پیوند دارد", 70, 65),
    ("MC-473", "MC-166", "RELATED_TO", "نقد صنایع فرهنگی و تحلیل شکل رسانه در مکتب فرانکفورت و مکلوهان به هم می‌رسند", 55, 50),
    ("MC-476", "MC-344", "RELATED_TO", "درمولوژی ویریلیو و نقد گشتل هایدگر هر دو فناوری را فراتر از ابزار می‌بینند", 65, 60),
    ("MC-476", "MC-727", "RELATED_TO", "سرعت و ادراک از موضوعات فلسفهٔ رسانه است", 70, 65),
    ("MC-476", "MC-472", "RELATED_TO", "سرعت فناورانه و عقلانیت ابزاری در نقد جامعهٔ صناعی هم‌پوشانی دارند", 60, 55),
    ("MC-476", "MC-225", "RELATED_TO", "فرهنگ الگوریتمی نمونهٔ امروزی سازمان‌دهی زمان واقعی است", 55, 50),
    ("MC-478", "MC-718", "RELATED_TO", "صورت‌گرایی زیمل بر تحلیل رابطه و شبکهٔ اجتماعی اثر گذاشته است", 65, 60),
    ("MC-478", "MC-186", "RELATED_TO", "تحلیل مد و تمایز زیمل با مصرف نمایشی هم‌سو است", 65, 60),
    ("MC-478", "MC-716", "RELATED_TO", "مطالعهٔ صورت‌های تعامل به قوم‌نگاری زندگی روزمره نزدیک است", 55, 50),
    ("MC-478", "CPT-056", "RELATED_TO", "مصرف رسانه‌ای صورت امروزی تمایز و فاصلهٔ اجتماعی است", 55, 50),
    ("MC-602", "MDL-060", "RELATED_TO", "مدل تلویزیون اینترنتی به ظرفیت پهنای باند و روند رشد آن وابسته است", 60, 55),
    ("MC-602", "CPT-056", "RELATED_TO", "رشد پهنای باند الگوی مصرف رسانه‌ای را دگرگون می‌کند", 60, 55),
    ("MC-602", "MC-225", "RELATED_TO", "خدمات الگوریتمی به ظرفیت شبکه و پهنای باند نیاز دارند", 50, 45),
    ("MC-602", "MC-418", "RELATED_TO", "پهنای باند زیرساخت مشارکت و هوش جمعی آنلاین است", 50, 45),
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
            (sid, tid, rt, STAMP, "qoder-verify-batch187", conf / 100.0, note, w, NOW, NOW))
        ins += 1
    c.commit()
    print("inserted=%d skipped=%d" % (ins, skip))
    c.close()


if __name__ == "__main__":
    main()
