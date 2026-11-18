# -*- coding: utf-8 -*-
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-rel-batch176-20261116"
NOW = "2026-11-16 00:00:00"

ROWS = [
    ("MC-505", "MC-161", "RELATED_TO", "اثر شبکه‌ای به بازار برنده‌همه‌چیز و تمرکز صنعت می‌انجامد", 80, 80),
    ("MC-505", "MC-381", "RELATED_TO", "شبکهٔ پلتفرم با بازار دوسویه و وابستگی دو گروه کاربر پیوند دارد", 75, 75),
    ("MC-505", "MC-254", "RELATED_TO", "رشد شبکه با پیوست ترجیحی و توزیع بی‌مقیاس قابل تحلیل است", 65, 60),
    ("MC-505", "MC-117", "RELATED_TO", "اثر شبکه‌ای یکی از سازوکارهای شکل‌گیری جامعهٔ پلتفرمی است", 60, 60),
    ("MC-573", "CPT-059", "RELATED_TO", "توجه آغازین و پایانی سهم بیشتری از پردازش پیام می‌گیرد", 80, 75),
    ("MC-573", "MDL-020", "RELATED_TO", "مدل مواجهه و توجه جایگاه پیام را در پردازش توضیح می‌دهد", 65, 60),
    ("MC-573", "MC-677", "RELATED_TO", "حافظهٔ جمعی رسانه‌ای از برجستگی اقلام آغازین و پایانی خبر بهره می‌برد", 55, 50),
    ("MC-573", "MC-001", "RELATED_TO", "جایگاه خبر در دستور کار بر برجستگی آن اثر می‌گذارد", 55, 50),
    ("MC-574", "MC-575", "RELATED_TO", "لنگر و چارچوب دو میانبر هم‌خانواده در قضاوت و تصمیم‌اند", 85, 85),
    ("MC-574", "MC-126", "RELATED_TO", "لنگر عددی بر ارزیابی سود و زیان پیام اثر می‌گذارد", 60, 55),
    ("MC-574", "MC-247", "RELATED_TO", "لنگر در قضاوت تحت عدم قطعیت و کاهش آن عمل می‌کند", 50, 50),
    ("MC-574", "MC-129", "RELATED_TO", "برآورد ریسک عمومی تحت اثر لنگرهای عددی است", 50, 45),
    ("MC-575", "MC-126", "RELATED_TO", "اثر چارچوب با قاب‌بندی سود و زیان در پیام‌رسانی پیوند مستقیم دارد", 85, 85),
    ("MC-575", "MC-574", "RELATED_TO", "چارچوب و لنگر دو میانبر هم‌خانواده در تصمیم‌گیری‌اند", 80, 80),
    ("MC-575", "TX-056", "RELATED_TO", "چارچوب‌بندی بر تصمیم گروهی و اشتراک اطلاعات اثر می‌گذارد", 55, 50),
    ("MC-575", "MC-129", "RELATED_TO", "چارچوب پیام ریسک بر ادراک و تصمیم مخاطب اثر دارد", 60, 55),
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
            (sid, tid, rt, STAMP, "qoder-verify-batch176", conf / 100.0, note, w, NOW, NOW))
        ins += 1
    c.commit()
    print("inserted=%d skipped=%d" % (ins, skip))
    c.close()


if __name__ == "__main__":
    main()
