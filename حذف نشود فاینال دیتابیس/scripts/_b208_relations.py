# -*- coding: utf-8 -*-
"""Batch 208 relations."""
import pymysql

DB = "resaname_kb_final_inspect"
ASSERTED = "qoder-rel-batch208-20261117"
VERIFIED = "qoder-verify-batch208"
NOW = "2026-11-17 00:00:00"

R = [
    ("card-212", "SFL-015", "RELATED_TO", 56, "کنشگری فراملی و فرهنگ مشارکتی، دو شکل سازمان‌یابی کنشگران بیرون از نهادهای رسمی‌اند"),
    ("card-212", "CPT-072", "RELATED_TO", 54, "سواد رسانه‌ای، توان کنشگران محلی برای جهانی‌کردن روایت و مقابله با انسداد اطلاعاتی را می‌سازد"),
    ("card-212", "MC-667", "RELATED_TO", 60, "برجستگی الگوریتمی، مسیر تازه‌ای برای جهانی‌شدن یا سرکوب روایت‌های کنشگری است"),
    ("card-212", "MC-731", "RELATED_TO", 58, "روایت مشترک کنشگران و همدلی فراملی، مادهٔ خام عمومیت عاطفی است"),
    ("card-540", "MC-082", "RELATED_TO", 68, "مدل مارپیچ در برابر مدل انتقالی، بُعد زمان و بازگشت معنا را وارد تحلیل ارتباط می‌کند"),
    ("card-540", "MC-081", "RELATED_TO", 60, "مدل پنج‌پرسشی لاسول، نقطهٔ مقابل تصویر خطی است که مدل مارپیچ نقد می‌کند"),
    ("card-540", "MC-107", "RELATED_TO", 55, "پردازش پیام در طول زمان و بازسازی معنا، به ظرفیت شناختی و توجه مخاطب گره خورده است"),
    ("card-540", "MC-028", "RELATED_TO", 52, "هر دو مدل، پیشرفت را مرحله‌ای و بازگشتی می‌بینند و بازگشت را بخشی از فرایند می‌دانند"),
    ("MC-156", "MC-069", "RELATED_TO", 58, "کار مدیریتی و کارت امتیازی متوازن، دو سوی سنجش و هدایت عملکرد سازمان‌اند"),
    ("MC-156", "MC-155", "RELATED_TO", 60, "نقش‌های مدیریتی، بستر انسانی یادگیری سازمانی و تصمیم‌گیری دوحلقه‌ای‌اند"),
    ("MC-156", "MC-121", "RELATED_TO", 55, "مدیر سازمان، بازیگر اصلی انتخاب الگوی روابط عمومی و مدیریت ارتباط با جمهور است"),
    ("MC-156", "MC-653", "RELATED_TO", 50, "پذیرش فناوری در سازمان به نقش‌های اطلاعاتی و تصمیم‌گیری مدیر وابسته است"),
    ("MC-173", "MC-428", "RELATED_TO", 64, "چرخهٔ عمر محصول و انتشار نوآوری، دو خوانش از مسیر پذیرش و اشباع در بازارند"),
    ("MC-173", "MC-169", "RELATED_TO", 56, "پلتفرمی‌شدن، چرخهٔ عمر محصول رسانه‌ای را کوتاه و شبکه‌ای کرده است"),
    ("MC-173", "MC-653", "RELATED_TO", 50, "مرحلهٔ چرخهٔ عمر محصول، زمینهٔ سازمانی و فناورانهٔ پذیرش را تغییر می‌دهد"),
    ("MC-173", "MC-069", "RELATED_TO", 52, "سنجه‌های عملکرد باید با مرحلهٔ چرخهٔ عمر محصول هم‌خوان شوند"),
    ("card-59", "MC-230", "RELATED_TO", 80, "پاسخگویی الگوریتمی، سازوکار نظارتی حکمرانی الگوریتمی است"),
    ("card-59", "MC-667", "RELATED_TO", 70, "برجستگی الگوریتمی، یکی از موضوع‌های اصلی ممیزی و پاسخ‌گویی است"),
    ("card-59", "MC-169", "RELATED_TO", 60, "نظم پلتفرم، میدان اصلی اجرای پاسخگویی الگوریتمی است"),
]

conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="433700",
                       database=DB, charset="utf8mb4", autocommit=False)
cur = conn.cursor()
codes = {c for pair in R for c in pair[:2]}
cur.execute("SELECT id, code FROM kb_entities WHERE code IN (%s)" %
            ",".join(["%s"] * len(codes)), list(codes))
ids = dict((c, i) for i, c in cur.fetchall())
missing = codes - set(ids)
if missing:
    raise SystemExit("missing codes: %s" % missing)

cur.execute("DELETE FROM kb_relations WHERE asserted_by=%s", (ASSERTED,))
n = 0
for s, t, rt, conf, note in R:
    cur.execute("""INSERT INTO kb_relations
        (source_id, target_id, relation_type, assertion_status, asserted_by, verified_by,
         extraction_confidence, note, weight, status, created_at, updated_at)
        VALUES (%s,%s,%s,'verified',%s,%s,%s,%s,1,'active',%s,%s)""",
        (ids[s], ids[t], rt, ASSERTED, VERIFIED, conf / 100.0, note, NOW, NOW))
    n += 1
conn.commit()
conn.close()
print("relations inserted:", n)
