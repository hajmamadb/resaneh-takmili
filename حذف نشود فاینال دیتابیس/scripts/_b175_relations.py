# -*- coding: utf-8 -*-
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-rel-batch175-20261116"
NOW = "2026-11-16 00:00:00"

ROWS = [
    ("MC-109", "MC-138", "RELATED_TO", "اثر خواب‌آلود در آزمایش‌های اعتبار منبع کشف و صورت‌بندی شد", 90, 90),
    ("MC-109", "TX-016", "RELATED_TO", "اثر خواب‌آلود از پدیده‌های کلاسیک نظریهٔ اقناع است", 80, 80),
    ("MC-109", "MC-131", "RELATED_TO", "مدل دانش اقناع یادآوری پیام و منبع را در تبیین اثر دخیل می‌کند", 60, 60),
    ("MC-109", "MC-579", "RELATED_TO", "تکرار و تأخیر دو مسیر متمایز افزایش اثر پیام‌اند", 55, 50),
    ("MC-110", "MC-530", "RELATED_TO", "اثر حقیقت‌نمایی سازوکار بقای باور نادرست را توضیح می‌دهد", 85, 85),
    ("MC-110", "CPT-255", "RELATED_TO", "تکرار خبر جعلی باورپذیری آن را افزایش می‌دهد", 80, 80),
    ("MC-110", "MC-183", "RELATED_TO", "آبشار اطلاعاتی با تکرار و مشاهدهٔ باور دیگران تشدید می‌شود", 60, 55),
    ("MC-110", "MC-579", "RELATED_TO", "اثر حقیقت‌نمایی همتای شناختی اثر تکرار در اقناع است", 70, 60),
    ("MC-211", "MC-085", "RELATED_TO", "پوشش خبری بحران تصویر محیط و فشار عمومی می‌سازد", 60, 55),
    ("MC-211", "MC-004", "RELATED_TO", "چارچوب‌بندی بحران بر جهت فشار رسانه‌ای اثر می‌گذارد", 65, 60),
    ("MC-211", "MC-370", "RELATED_TO", "پوشش بحران می‌تواند به ابزار دستکاری افکار عمومی نزدیک شود", 55, 50),
    ("MC-211", "MC-337", "RELATED_TO", "سوگیری در انتخاب بحران بر سیاست خارجی اثر می‌گذارد", 55, 50),
    ("MC-246", "TX-052", "RELATED_TO", "ناشناسی و هویت گروهی رفتار آنلاین را شکل می‌دهند", 55, 55),
    ("MC-246", "MC-117", "RELATED_TO", "طراحی پلتفرم زمینهٔ بی‌بازداری آنلاین است", 60, 60),
    ("MC-246", "MC-415", "RELATED_TO", "قواعد پلتفرم مرزهای ابرازگری را تعیین می‌کنند", 55, 55),
    ("MC-246", "MC-292", "RELATED_TO", "ابرازگری آنلاین در میدان قدرت نمادین رخ می‌دهد", 50, 50),
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
            (sid, tid, rt, STAMP, "qoder-verify-batch175", conf / 100.0, note, w, NOW, NOW))
        ins += 1
    c.commit()
    print("inserted=%d skipped=%d" % (ins, skip))
    c.close()


if __name__ == "__main__":
    main()
