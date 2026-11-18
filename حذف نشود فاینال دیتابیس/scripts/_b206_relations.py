# -*- coding: utf-8 -*-
"""Batch 206 relations: MC-069, MC-082, MC-107 (+refs from MC-028/MC-081)."""
import pymysql

DB = "resaname_kb_final_inspect"
ASSERTED = "qoder-rel-batch206-20261117"
VERIFIED = "qoder-verify-batch206"
NOW = "2026-11-17 00:00:00"

R = [
    # MC-069 کارت امتیازی متوازن
    ("MC-069", "MC-155", "RELATED_TO", 82, "کارت امتیازی متوازن و یادگیری سازمانی هر دو ظرفیت یادگیری را موتور بهبود عملکرد می‌دانند"),
    ("MC-069", "MC-653", "RELATED_TO", 70, "هر دو چارچوب، پذیرش و اجرای نوآوری سازمانی را از چند بُعد می‌سنجند"),
    ("MC-069", "MC-598", "RELATED_TO", 62, "کارت امتیازی متوازن، سنجش اثربخشی مدیریت معنا و اعتبار سازمانی را کمی می‌کند"),
    ("MC-069", "MC-028", "RELATED_TO", 55, "سنجه‌های تغییر رفتار و سنجه‌های عملکرد سازمانی، هر دو حرکت مرحله‌ای را مفروض می‌گیرند"),
    # MC-082 شانون-ویور
    ("MC-082", "MC-081", "RELATED_TO", 90, "مدل انتقالی شانون-ویور و مدل پنج‌پرسشی لاسول، دو صورت‌بندی بنیادین ارتباط خطی‌اند"),
    ("MC-082", "MC-107", "RELATED_TO", 72, "ظرفیت کانال و ظرفیت شناختی، دو خوانش از محدودیت پردازش و انتقال پیام‌اند"),
    ("MC-082", "TX-016", "RELATED_TO", 60, "مدل انتقالی، چارچوب پایهٔ تحلیل پیام و اثر اقناعی را فراهم می‌کند"),
    ("MC-082", "MC-004", "RELATED_TO", 58, "چهارچوب‌بندی، نقدی بر انتقال معنای بی‌طرف در مدل ریاضی ارتباط است"),
    # MC-107 مدل ظرفیت محدود
    ("MC-107", "MC-082", "RELATED_TO", 72, "محدودیت ظرفیت کانال و محدودیت منابع شناختی، دو صورت از سقف پردازش‌اند"),
    ("MC-107", "CPT-072", "RELATED_TO", 66, "سواد رسانه‌ای، مهارت مدیریت بار شناختی و تخصیص توجه در محیط پیام‌محور است"),
    ("MC-107", "MC-709", "RELATED_TO", 60, "سرگرمی رسانه‌ای، انگیزه و محرک نوظهوری است که تخصیص منابع شناختی را هدایت می‌کند"),
    ("MC-107", "TX-016", "RELATED_TO", 58, "بار شناختی، شرط اثرگذاری اقناع است: پیام سنگین، پردازش و پذیرش را کاهش می‌دهد"),
]

conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="433700",
                       database=DB, charset="utf8mb4", autocommit=False)
cur = conn.cursor()
cur.execute("SELECT id, code FROM kb_entities WHERE code IN (%s)" %
            ",".join(["%s"] * len({c for pair in R for c in pair[:2]})),
            list({c for pair in R for c in pair[:2]}))
ids = dict((c, i) for i, c in cur.fetchall())

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
