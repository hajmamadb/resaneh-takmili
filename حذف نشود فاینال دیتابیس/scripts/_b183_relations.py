# -*- coding: utf-8 -*-
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-rel-batch183-20261116"
NOW = "2026-11-16 00:00:00"

ROWS = [
    ("MC-725", "MC-715", "RELATED_TO", "پساساختارگرایی نقد رادیکال نشانه‌شناسی ساختارگرا است", 80, 75),
    ("MC-725", "MC-714", "RELATED_TO", "تحلیل چارچوب و تحلیل گفتمان پساساختارگرا در مطالعهٔ معنا هم‌پوشانی دارند", 70, 65),
    ("MC-725", "MC-484", "RELATED_TO", "واسازی و تحلیل روایت در بررسی روایت‌های رسانه‌ای مکمل‌اند", 65, 60),
    ("MC-725", "MC-072", "RELATED_TO", "تحلیل محتوای کیفی می‌تواند با واسازی متن تکمیل شود", 60, 55),
    ("MC-726", "MC-239", "RELATED_TO", "عملگرایی بنیاد معرفتی رایج روش‌های ترکیبی است", 85, 85),
    ("MC-726", "MC-073", "RELATED_TO", "سه‌سوسازی با منطق عملگرایانه توجیه می‌شود", 75, 70),
    ("MC-726", "MC-716", "RELATED_TO", "قوم‌نگاری مخاطب با معیار سودمندی عملی ارزیابی می‌شود", 55, 50),
    ("MC-726", "MC-072", "RELATED_TO", "تحلیل محتوا در پژوهش کاربردی رسانه جایگاه عملگرایانه دارد", 55, 50),
    ("MC-727", "th-3", "RELATED_TO", "مارشال مک‌لوهان بنیان‌گذار اصلی فلسفه رسانه است", 90, 90),
    ("MC-727", "MC-473", "RELATED_TO", "رسانه سرد و گرم صورت‌بندی مک‌لوهانی از ماهیت رسانه است", 85, 85),
    ("MC-727", "MC-344", "RELATED_TO", "فلسفه فناوری و گشتل به پرسش ماهیت فناوری رسانه پاسخ می‌دهد", 70, 65),
    ("MC-727", "MC-476", "RELATED_TO", "فناوری و تمدن تحلیل فلسفی پیامدهای فناوری رسانه است", 65, 60),
    ("MC-265", "MC-264", "RELATED_TO", "خالص نمرهٔ مروّج برای پیش‌بینی چرخهٔ وفاداری و ریزش به کار می‌رود", 75, 70),
    ("MC-265", "MDL-030", "RELATED_TO", "مدل وفاداری مخاطب با شاخص توصیه سنجیده می‌شود", 70, 65),
    ("MC-265", "CPT-230", "RELATED_TO", "خالص نمرهٔ مروّج سنجهٔ رایج وفاداری به برند است", 80, 80),
    ("MC-265", "CPT-066", "RELATED_TO", "شاخص توصیه یکی از سنجه‌های وفاداری مخاطب است", 70, 65),
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
            (sid, tid, rt, STAMP, "qoder-verify-batch183", conf / 100.0, note, w, NOW, NOW))
        ins += 1
    c.commit()
    print("inserted=%d skipped=%d" % (ins, skip))
    c.close()


if __name__ == "__main__":
    main()
