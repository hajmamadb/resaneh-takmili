# -*- coding: utf-8 -*-
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-rel-batch186-20261116"
NOW = "2026-11-16 00:00:00"

ROWS = [
    ("MC-333", "MC-091", "RELATED_TO", "مطالعات فرهنگی بریتانیا مفهوم هژمونی گرامشی را در تحلیل رسانه به کار گرفت", 80, 75),
    ("MC-333", "MC-355", "RELATED_TO", "مخاطب فعال و مقاومت عامه از دستاوردهای نظری این مکتب است", 85, 80),
    ("MC-333", "MC-723", "RELATED_TO", "فمینیسم رسانه‌ای از شاخه‌های گسترش‌یافتهٔ مطالعات فرهنگی است", 70, 65),
    ("MC-333", "MC-716", "RELATED_TO", "قوم‌نگاری مخاطب از روش‌های نزدیک به سنت مطالعات فرهنگی است", 70, 65),
    ("MC-339", "MC-727", "RELATED_TO", "تز سرگرمی‌شدن گفتمان عمومی در سنت بوم‌شناسی رسانه جای دارد", 80, 75),
    ("MC-339", "MC-473", "RELATED_TO", "تحلیل رسانهٔ سرد و گرم زمینهٔ نظری نقد تلویزیون پستمن را ساخت", 65, 60),
    ("MC-339", "MC-166", "RELATED_TO", "نقد سرگرمی‌شدن فرهنگ با نظریهٔ صنایع فرهنگی هم‌سو است", 60, 55),
    ("MC-339", "MC-369", "RELATED_TO", "مهندسی رضایت به پیوند سرگرمی و مدیریت افکار عمومی مربوط است", 55, 50),
    ("MC-344", "MC-727", "RELATED_TO", "فلسفهٔ فناوری هایدگر بنیانی برای فلسفهٔ رسانه فراهم کرد", 75, 70),
    ("MC-344", "MC-476", "RELATED_TO", "نقد گشتل با بحث فناوری و تمدن هم‌پوشانی دارد", 70, 65),
    ("MC-344", "MC-472", "RELATED_TO", "نقد عقلانیت ابزاری مارکوزه با نقد گشتل هایدگر هم‌سو است", 65, 60),
    ("MC-344", "MC-166", "RELATED_TO", "نقد فناوری و صنایع فرهنگی در مکتب فرانکفورت و هایدگر به هم می‌رسند", 55, 50),
    ("MC-472", "MC-344", "RELATED_TO", "عقلانیت ابزاری مارکوزه در گفت‌وگو با نقد فناوری هایدگر فهم می‌شود", 65, 60),
    ("MC-472", "MC-166", "RELATED_TO", "نظریهٔ صنایع فرهنگی بستر مفهومی انسان تک‌ساحتی است", 75, 70),
    ("MC-472", "MC-091", "RELATED_TO", "هژمونی فرهنگی سازوکار طبیعی‌شدن سلطهٔ عقلانیت ابزاری را توضیح می‌دهد", 60, 55),
    ("MC-472", "MC-277", "RELATED_TO", "گیمیفیکیشن نمونهٔ امروزی عقلانیت ابزاری در مدیریت و رسانه است", 60, 55),
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
            (sid, tid, rt, STAMP, "qoder-verify-batch186", conf / 100.0, note, w, NOW, NOW))
        ins += 1
    c.commit()
    print("inserted=%d skipped=%d" % (ins, skip))
    c.close()


if __name__ == "__main__":
    main()
