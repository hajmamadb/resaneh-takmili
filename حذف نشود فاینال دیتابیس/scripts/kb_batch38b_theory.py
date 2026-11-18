# -*- coding: utf-8 -*-
"""Touch-up for MC-079 and MC-147: expand genuine analysis to full SPEC §6.1 analysis band.
Recomputes rubric only; evidence rows already created by batch 38 (idempotent)."""
import pymysql, json

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch38b-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch38b_theory.json"

ADD = {
 "MC-079": {
   "mechanism": "تاکمن مکانیسم را در سه سطح توضیح می‌دهد: (۱) «شبکهٔ خبری» (news net) — سازمان‌های خبری با تخصیص خبرنگار به منابع ثابت (پلیس، دولت، دادگاه) رویدادها را می‌پایند و ناگزیر بخشی از واقعیت را از شبکه عبور می‌دهند؛ (۲) «روتین‌سازی» (routinization) — مقولات خبری، برنامهٔ زمانی و معیارهای «ارزش خبری» به کار روزمره نظم می‌دهند و پیش‌بینی‌پذیر می‌سازند؛ (۳) «نوع‌سازی» (typification) — خبرنگاران رویدادها را در قالب‌های آشنا (جرم، بحران، سیاست) دسته‌بندی می‌کنند و معنای آن‌ها را بازسازی می‌کنند (Tuchman, 1978). تاکمن همچنین «عینیت» را «آیین راهبردی» توصیف کرد: مجموعه رویه‌هایی که روزنامه‌نگار را در برابر انتقاد محافظت می‌کند. \n\nدر لایهٔ عملی‌تر، تاکمن نشان می‌دهد که خبر با «واقعیت‌نمایی» (facticity) ساخته می‌شود: جدا کردن «اخبار سخت» از «اخبار نرم»، استناد به مقامات، نقل‌قول مستقیم و ترتیب دادن اطلاعات در قالب «هرم وارونه»، همه سازوکارهایی‌اند که گزارش را «واقعی‌نما» می‌کنند، بدون آنکه الزاماً واقعیت را بی‌واسطه بازتاب دهند. او این فرایند را «بازسازی واقعیت» (reconstitution of reality) می‌نامد: رویداد خام، پیش از رسیدن به مخاطب، از صافی مقولات سازمانی و حرفه‌ای می‌گذرد و به شکل «خبر» درمی‌آید. نتیجه این است که خبر، «واقعیتِ نهادینه‌شده» است، نه انعکاس بی‌واسطهٔ جهان.",
   "applications": [
     "مطالعهٔ تولید خبر و تحولات تحریریه در عصر دیجیتال و داده‌محور.",
     "تحلیل سوگیری رسانه و رابطهٔ سازمان خبر با منابع قدرت.",
     "پژوهش دربارهٔ کار روزنامه‌نگاران، فشارهای شغلی و اخلاق حرفه‌ای.",
     "ارزیابی نقش فناوری‌های تحریریه (نرم‌افزار، تحلیل داده و هوش مصنوعی) در تغییر روتین‌های خبری."
   ],
 },
 "MC-147": {
   "mechanism": "کلر مکانیسم را از طریق «دانش برند» (brand knowledge) توضیح می‌دهد که دو مؤلفه دارد: (۱) «آگاهی از برند» (brand awareness) شامل تشخیص و یادآوری برند؛ (۲) «تصویر برند» (brand image) یعنی مجموعهٔ تداعی‌های ذهنی دربارهٔ برند. برند‌ارزشی زمانی بالا می‌رود که مصرف‌کننده با برند آشنا باشد و تداعی‌هایی «قوی، مطلوب و منحصربه‌فرد» (strong, favorable, unique) در ذهن او شکل گرفته باشد؛ این تداعی‌ها در مقایسه با برندهای رقیب، مزیت ذهنی می‌سازند (Keller, 1993). در توسعهٔ بعدی، کلر «هرم برند‌ارزشی» را معرفی کرد: برجستگی (salience) → عملکرد و تصویرسازی (performance/imagery) → داوری‌ها و احساسات (judgments/feelings) → طنین برند (resonance).\n\nبرای سنجش، کلر دو مسیر را پیشنهاد می‌کند: رویکرد «غیرمستقیم» که با سنجش آگاهی و تداعی‌ها به ساختار دانش برند می‌پردازد، و رویکرد «مستقیم» که واکنش مصرف‌کننده به عناصر بازاریابی را در مقایسه با نسخهٔ بدون برند آزمایش می‌کند. بنابراین برند‌ارزشی، سازه‌ای چندلایه و سازگار با سنجش پیمایشی و آزمایشی است، نه فقط یک شاخص مالی.",
 },
}

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
    return min(100, sum(detail.values())), detail

def main():
    c = pymysql.connect(host="127.0.0.1", user="root", password="433700", database=DB, charset="utf8mb4", autocommit=False)
    cur = c.cursor()
    codes = list(ADD.keys())
    cur.execute("SELECT id, code, properties FROM kb_entities WHERE code IN (%s)" % ",".join(["%s"]*len(codes)), codes)
    rows = {code:(eid, json.loads(pr)) for (eid, code, pr) in cur.fetchall()}
    with open(BACKUP, "w", encoding="utf-8") as f:
        json.dump([{"code": cd, "props": rows[cd][1]} for cd in codes if cd in rows], f, ensure_ascii=False, indent=1)
    for code in codes:
        eid, p = rows[code]
        for k, v in ADD[code].items():
            p[k] = v
        n_sources = len(p.get("sources") or [])
        n_verified = sum(1 for s in (p.get("sources") or []) if s.get("citation") in
                         [ci.get("source") for ci in (p.get("citations") or []) if ci.get("verified")])
        cur.execute("SELECT COUNT(*) FROM kb_relations r JOIN kb_entities a ON r.source_id=a.id JOIN kb_entities b ON r.target_id=b.id WHERE a.code=%s OR b.code=%s", (code, code))
        n_relations = cur.fetchone()[0]
        score, detail = rubric(p, n_verified, n_sources, n_relations)
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
                    (eid, ver, json.dumps({"quality_score": score}, ensure_ascii=False),
                     "expanded analysis to full rubric band", STAMP, NOW))
        cur.execute("INSERT INTO kb_audit_log (entity_code, action, detail, source) VALUES (%s,%s,%s,%s)",
                    (code, "DOC_ENRICH", json.dumps({"quality_score": score, "breakdown": detail}, ensure_ascii=False), STAMP))
        print(f"{code}: score={score} | {detail}")
    c.commit(); c.close()
    print("TOUCHUP DONE")

if __name__ == "__main__":
    main()
