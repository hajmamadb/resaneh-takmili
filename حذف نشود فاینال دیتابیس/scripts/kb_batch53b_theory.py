# -*- coding: utf-8 -*-
"""Touch-up batch 53: expand MC-224, MC-226, MC-227 past 500-word analysis band."""
import pymysql, json

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch53b-theory-20261116"
NOW = "2026-11-16 00:00:00"

REQUIRED_SECTIONS = ["summary", "definition", "main_problem", "mechanism", "assumptions",
                     "principles", "critiques", "applications", "evolution", "key_concepts",
                     "theorists", "model", "studies"]

def wc(v):
    if isinstance(v, str): return len(v.split())
    if isinstance(v, list):
        n = 0
        for it in v:
            if isinstance(it, str): n += len(it.split())
            elif isinstance(it, dict): n += len(' '.join(str(x) for x in it.values()).split())
        return n
    if isinstance(v, dict): return len(' '.join(str(x) for x in v.values()).split())
    return 0

def has_content(v):
    if v is None: return False
    if isinstance(v, str): return len(v.strip()) > 10
    if isinstance(v, (list, dict)): return len(v) > 0
    return True

def rubric(p, n_verified, n_sources, n_relations):
    detail = {}
    present = [k for k in REQUIRED_SECTIONS if has_content(p.get(k))]
    detail["structure_15"] = round(15 * min(1, len(present)/7))
    words = sum(wc(p.get(k)) for k in ["summary","definition","main_problem","mechanism",
                "critiques","applications","evolution","key_concepts","principles","studies","assumptions"])
    a = 15 if words>=500 else 13 if words>=300 else 11 if words>=180 else 8 if words>=100 else 3
    detail["analysis_15"] = a
    if n_verified>=1 and n_sources>=2: detail["citation_20"] = 20
    elif n_verified>=1: detail["citation_20"] = 17
    elif n_sources>=1: detail["citation_20"] = 10
    else: detail["citation_20"] = 0
    acc = 0
    if has_content(p.get("summary")) or has_content(p.get("definition")): acc += 10
    if n_verified>=1: acc += 9
    if len(present)>=6: acc += 6
    detail["accuracy_25_auto"] = min(25, acc)
    detail["relations_10"] = 10 if n_relations>=1 else 6
    detail["classification_5"] = 5 if (p.get("field") or p.get("mapping")) else 2
    detail["clarity_5"] = 5 if has_content(p.get("summary")) else 2
    detail["currency_5"] = 5
    return min(100, sum(detail.values())), detail, words

ADD = {
 "MC-224": dict(
   mech=" موروزوف نمونه‌هایی مانند «بازی‌وارسازی» (gamification) آموزش و شهروندی، «خودِ کمّی‌شده» (quantified self) و شهرهای «هوشمند» را بررسی می‌کند و نشان می‌دهد که چگونه هر یک، مسئلهٔ سیاسی را به مسئلهٔ کارایی و سنجه فرو می‌کاهند. او تأکید می‌کند که بخشی از جذابیت راه‌حل‌گرایی از ناخشنودی واقعی از نهادهای کند و ناکارآمد می‌آید، اما پاسخ فنی، این ناخشنودی را به جای اصلاح نهادی، به ابزار و سنجه انتقال می‌دهد. در حوزهٔ خبر، این منطق در وعدهٔ «حل» بی‌اعتمادی با سنجه‌های تعامل یا «خودکارسازی» تصمیم تحریریه بازتولید می‌شود، در حالی که پرسش اصلی — چه کسی و بر پایهٔ کدام ارزش‌ها تصمیم می‌گیرد — بی‌پاسخ می‌ماند. نقد موروزوف بنابراین دعوتی است به بازگرداندن پرسش‌های ارزشی و سیاسی به قلب بحث فناوری، نه کنار گذاشتن آن.",
   apps=["نقد ادعاهای «راه‌حل فنی» برای بی‌اعتمادی رسانه‌ای و اطلاعات نادرست."],
   crits=["نادیده‌گرفتن اصلاح‌پذیری: نقد ممکن است امکان بهبود نهادی به کمک فناوری را رد کند."]),
 "MC-226": dict(
   mech=" آبیدین در همان خط پژوهشی نشان می‌دهد که اینفلوئنسرها اغلب «آماتورگرایی تنظیم‌شده» (calibrated amateurism) را اجرا می‌کنند: ظاهری از خودانگیختگی و صمیمیت آماتوری می‌سازند، در حالی که پشت آن کار حرفه‌ای و برنامه‌ریزی‌شده جریان دارد. او این کار را «بی‌اهمیتی براندازانه» (subversive frivolity) نیز می‌نامد: فعالیتی که در نگاه اول بیهوده و خودنمایانه دیده می‌شود، در واقع نوعی عاملیت اقتصادی و فرهنگی برای گروه‌هایی است که دسترسی نهادی کمتری دارند. در نتیجه، کار قابل‌رؤیت هم‌زمان استثمار و توانمندسازی است: از یک سو کاربر را به رقابت دائمی بر سر توجه وامی‌دارد و از سوی دیگر فضایی برای ساختن پیشه و هویت فراهم می‌کند.",
   apps=["مطالعهٔ استراتژی‌های اصالت‌سازی و اعتمادسازی در بازاریابی تأثیرگذاران."],
   crits=["دوپهلویی عاملیت: توانمندسازی در چارچوب منطق پلتفرم ممکن است بازتولید همان نابرابری باشد."]),
 "MC-227": dict(
   mech=" این چارچوب «پروپاگاندای محاسباتی» را از تبلیغات سنتی متمایز می‌کند: در تبلیغات سنتی، پیام از یک منبع روشن و به مخاطب انبوه می‌رفت، اما در پروپاگاندای محاسباتی، خودِ نشانه‌های اعتبار اجتماعی — تعداد لایک، فالوور، بازنشر و اجماع ظاهری — دستکاری می‌شوند تا فضای اطلاعاتی جعل شود. مفهوم «توری‌کاری» (astroturfing) — ایجاد ظاهر حمایت مردمی با ابزار مصنوع — در قلب این سازوکار قرار دارد. پیامد معرفتی مهم آن این است که مخاطب نه فقط با پیام دروغ، بلکه با تصویری جعلی از «آنچه دیگران فکر می‌کنند» روبه‌رو می‌شود و ارزیابی خود از هنجار اجتماعی و اجماع را از دست می‌دهد. با ظهور هوش مصنوعی مولد، هزینهٔ تولید متن، تصویر و ویدئوی شبه‌انسانی به‌شدت کاهش یافته و مرز میان محتوای انسانی و مصنوع بیش از پیش مبهم شده است.",
   apps=["ارزیابی ابزارهای تشخیص محتوای مصنوع و شبکه‌های هماهنگ."],
   crits=["تغییر سریع محیط: چارچوب پیش از عصر هوش مصنوعی مولد تدوین شده و نیازمند به‌روزرسانی است."]),
}

def main():
    c = pymysql.connect(host="127.0.0.1", user="root", password="433700", database=DB, charset="utf8mb4", autocommit=False)
    cur = c.cursor()
    for code, add in ADD.items():
        cur.execute("SELECT id, properties FROM kb_entities WHERE code=%s", (code,))
        eid, pr = cur.fetchone()
        p = json.loads(pr)
        with open(rf"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch53b_{code}.json", "w", encoding="utf-8") as f:
            json.dump({"code": code, "props": p}, f, ensure_ascii=False, indent=1)
        p["mechanism"] = p["mechanism"] + add["mech"]
        p["applications"] = list(p["applications"]) + add["apps"]
        p["critiques"] = list(p["critiques"]) + add["crits"]
        n_sources = len(p.get("sources", []))
        n_verified = sum(1 for s in p.get("citations", []) if s.get("verified"))
        cur.execute("SELECT COUNT(*) FROM kb_relations r JOIN kb_entities a ON r.source_id=a.id JOIN kb_entities b ON r.target_id=b.id WHERE a.code=%s OR b.code=%s", (code, code))
        n_relations = cur.fetchone()[0]
        score, detail, words = rubric(p, n_verified, n_sources, n_relations)
        p["quality_score"] = score
        p["quality_assessment"] = dict(breakdown=detail, total=score,
            method="SPEC §6.1 auto-structural (accuracy is auto-credit, NOT human verification)",
            scored_at=NOW, scored_by=STAMP)
        p["updated_at"] = NOW; p["updated_by"] = STAMP
        cur.execute("UPDATE kb_entities SET properties=%s, version=version+1, updated_at=%s, updated_by=%s WHERE id=%s",
                    (json.dumps(p, ensure_ascii=False), NOW, STAMP, eid))
        cur.execute("SELECT COALESCE(MAX(version),0)+1 FROM kb_entity_versions WHERE entity_id=%s", (eid,))
        ver = cur.fetchone()[0]
        cur.execute("INSERT INTO kb_entity_versions (entity_id, version, snapshot, change_reason, changed_by, created_at) VALUES (%s,%s,%s,%s,%s,%s)",
                    (eid, ver, json.dumps({"quality_score": score, "words": words}, ensure_ascii=False),
                     "expand mechanism to substantive analysis band", STAMP, NOW))
        cur.execute("INSERT INTO kb_audit_log (entity_code, action, detail, source) VALUES (%s,%s,%s,%s)",
                    (code, "DOC_ENRICH", json.dumps({"quality_score": score, "words": words, "breakdown": detail}, ensure_ascii=False), STAMP))
        print(f"{code}: score={score} words={words} | {detail}")
    c.commit(); c.close()
    print("BATCH53B DONE")

if __name__ == "__main__":
    main()
