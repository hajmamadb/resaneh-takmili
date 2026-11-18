# -*- coding: utf-8 -*-
"""Batch 207 relations: MC-135, MC-143 (+links from MC-121/MC-131/MC-133)."""
import pymysql

DB = "resaname_kb_final_inspect"
ASSERTED = "qoder-rel-batch207-20261117"
VERIFIED = "qoder-verify-batch207"
NOW = "2026-11-17 00:00:00"

R = [
    # MC-135 سلسله‌مراتب اثرات
    ("MC-135", "TX-016", "RELATED_TO", 72, "سلسله‌مراتب اثرات، چارچوبی مرحله‌ای برای تحلیل اثر اقناعی تبلیغ است"),
    ("MC-135", "MC-107", "RELATED_TO", 64, "ظرفیت شناختی محدود، سرعت و دقت عبور مخاطب از مراحل اثر را تعیین می‌کند"),
    ("MC-135", "MC-082", "RELATED_TO", 56, "مدل انتقالی، پیش‌فرض سنجش اثر پیام را فراهم می‌کند که سلسله‌مراتب آن را مرحله‌بندی می‌کند"),
    ("MC-135", "MC-028", "RELATED_TO", 58, "هر دو مدل، تغییر را زنجیره‌ای از مراحل با پیش‌نیازهای شناختی و رفتاری می‌بینند"),
    # MC-143 مدیریت برداشت
    ("MC-143", "MC-598", "RELATED_TO", 76, "مدیریت معنا در روابط عمومی، مدیریت برداشت سازمانی در مقیاس ارتباطات عمومی است"),
    ("MC-143", "MC-121", "RELATED_TO", 64, "الگوهای روابط عمومی، صحنه‌های سازمانی مدیریت برداشت و تعریف موقعیت برای جمهورند"),
    ("MC-143", "MC-731", "RELATED_TO", 58, "خودارائه‌گری پلتفرمی، مادهٔ خام شکل‌گیری عمومیت‌های عاطفی است"),
    ("MC-143", "SFL-015", "RELATED_TO", 55, "در فرهنگ مشارکتی، هویت و برداشت فردی به‌طور مداوم در معرض اجرا و بازبینی جمعی است"),
    # پیوندهای تکمیلی کارت‌های دیگر این دسته
    ("MC-121", "MC-598", "RELATED_TO", 68, "مدل دوطرفهٔ متقارن، پیشینهٔ هنجاری چارچوب مدیریت معنا در روابط عمومی است"),
    ("MC-131", "CPT-072", "RELATED_TO", 74, "دانش اقناع، هستهٔ شناختی سواد رسانه‌ای و تبلیغاتی است"),
    ("MC-131", "TX-016", "RELATED_TO", 66, "مدل دانش اقناع، شرط اثرگذاری اقناع را تشخیص و مقاومت مخاطب می‌داند"),
    ("MC-133", "MC-028", "RELATED_TO", 62, "مدل باور سلامت و مدل فرانظری، دو چارچوب مکمل برای توضیح اقدام به رفتار سلامت‌اند"),
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
