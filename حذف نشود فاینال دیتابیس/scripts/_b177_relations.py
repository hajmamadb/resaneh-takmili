# -*- coding: utf-8 -*-
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-rel-batch177-20261116"
NOW = "2026-11-16 00:00:00"

ROWS = [
    ("MC-576", "MC-530", "RELATED_TO", "سوگیری تأیید یکی از سازوکارهای پذیرش و بقای اطلاعات نادرست است", 85, 85),
    ("MC-576", "CPT-255", "RELATED_TO", "تأیید خبر جعلی با جست‌وجوی شواهد هم‌سو آسان‌تر می‌شود", 80, 75),
    ("MC-576", "MC-085", "RELATED_TO", "مواجههٔ گزینشی سوگیری تأیید را در محیط رسانه‌ای تقویت می‌کند", 70, 65),
    ("MC-576", "MC-210", "RELATED_TO", "سوگیری تأیید در چارچوب میانبرهای اطلاعاتی قابل تحلیل است", 60, 55),
    ("MC-578", "MC-007", "RELATED_TO", "ادراک اجماع کاذب با ارزیابی جو عمومی در مارپیچ سکوت پیوند دارد", 80, 80),
    ("MC-578", "MC-560", "RELATED_TO", "اثر اجماع کاذب و اثر ارابه هر دو بر ادراک اکثریت استوارند", 75, 70),
    ("MC-578", "MC-183", "RELATED_TO", "آبشار اطلاعاتی برآورد اجماع را تشدید می‌کند", 65, 60),
    ("MC-578", "MC-085", "RELATED_TO", "محیط کاذب برآورد فراوانی دیدگاه‌ها را جهت می‌دهد", 65, 60),
    ("MC-580", "CPT-217", "RELATED_TO", "جذابیت منبع یکی از محرک‌های اصلی اثر هاله است", 85, 85),
    ("MC-580", "MC-138", "RELATED_TO", "اعتبار منبع از برداشت کلی و اثر هاله اثر می‌پذیرد", 80, 80),
    ("MC-580", "CPT-231", "RELATED_TO", "تصویر برند با تعمیم برداشت کلی به ویژگی‌های محصول پیوند دارد", 70, 65),
    ("MC-580", "CPT-103", "RELATED_TO", "اثر هاله با کلیشه در ادراک اجتماعی هم‌پوشانی دارد", 65, 60),
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
            (sid, tid, rt, STAMP, "qoder-verify-batch177", conf / 100.0, note, w, NOW, NOW))
        ins += 1
    c.commit()
    print("inserted=%d skipped=%d" % (ins, skip))
    c.close()


if __name__ == "__main__":
    main()
