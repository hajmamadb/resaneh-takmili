# -*- coding: utf-8 -*-
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-rel-batch166-20261116"
NOW = "2026-11-16 00:00:00"

ROWS = [
    ("th-1", "MC-001", "RELATED_TO", "مک‌کامبز بنیان‌گذار نظریهٔ برجسته‌سازی است", 80, 90),
    ("th-1", "MC-002", "RELATED_TO", "سطح سوم شبکه در ادامهٔ برنامهٔ پژوهشی مک‌کامبز شکل گرفت", 65, 75),
    ("th-1", "MC-004", "RELATED_TO", "برجسته‌سازی سطح دوم با چارچوب‌بندی صفات هم‌پوشانی دارد", 55, 65),
    ("th-2", "MC-001", "RELATED_TO", "شاو هم‌بنیان‌گذار برجسته‌سازی و پژوهش چپل هیل است", 80, 90),
    ("th-2", "MC-002", "RELATED_TO", "سطح شبکه‌ای برجسته‌سازی در سنت پژوهشی شاو ریشه دارد", 60, 70),
    ("th-2", "MC-013", "RELATED_TO", "شاو به ساخت دستور کار مطبوعات و دروازه‌بانی خبر پرداخت", 50, 55),
    ("th-15", "MC-001", "RELATED_TO", "لیپمن با تصاویر در سر ما پیش‌درآمد برجسته‌سازی است", 70, 80),
    ("th-15", "MC-004", "RELATED_TO", "کلیشه و محیط شبه‌واقعی، پیش‌درآمد چارچوب‌بندی رسانه‌ای است", 60, 70),
    ("th-15", "CPT-103", "RELATED_TO", "لیپمن مفهوم کلیشه را در افکار عمومی ۱۹۲۲ برجسته کرد", 75, 85),
    ("th-10", "TX-087", "RELATED_TO", "لاسول پایهٔ تحلیل نظام‌مند تبلیغات را گذاشت", 70, 85),
    ("th-10", "MC-072", "RELATED_TO", "تحلیل محتوا به‌عنوان روش، وامدار لاسول است", 70, 80),
    ("th-10", "MC-315", "RELATED_TO", "مدل پنج‌پرسشی، صورت‌بندی دقیق‌تر مدل انتقالی است", 55, 65),
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
            (sid, tid, rt, STAMP, "qoder-verify-batch166", conf / 100.0, note, w, NOW, NOW))
        ins += 1
    c.commit()
    print("inserted=%d skipped=%d" % (ins, skip))
    c.close()


if __name__ == "__main__":
    main()
