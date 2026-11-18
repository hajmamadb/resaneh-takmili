# -*- coding: utf-8 -*-
"""Touch-up batch 65c: MC-302 (Mathematical Theory of Information) carries generic
communication-model boilerplate in `critique` and `example` (Lasswell sender/channel text)
that contradicts its Shannon-specific `critiques`/`applications`. Replace both with
Shannon-specific Persian text. Rubric rescored for consistency."""
import pymysql, json

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch65c-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch65c_theory.json"

CODE = "MC-302"

CRITIQUE = "\n".join([
 "۱. معنا بیرون از نظریه: شانون خود تأکید کرد که جنبه‌های معنایی پیام به‌عمد کنار گذاشته شده‌اند؛ ازاین‌رو نظریهٔ او نظریهٔ انتقال نشانه است، نه نظریهٔ معنا، تفسیر یا ارتباط انسانی، و تعمیم آن به ارتباطات اجتماعی نیازمند ترجمه‌ای است که خود شانون انجام نداد.",
 "۲. تقلیل‌گرایی کمی: سنجش «اطلاعات» با آنتروپی و بیت، پدیده‌های کیفی مانند ابهام تفسیری، کنایه و بافت فرهنگی را به کمیت فرو می‌کاهد و آنچه را نمی‌توان کدگذاری کرد، نادیده می‌گیرد.",
 "۳. زمینه‌زدایی اجتماعی: مدل انتقالی قدرت، منافع، نهادها و روابط اجتماعی تولید پیام را کنار می‌گذارد؛ همین خصلت باعث شد این مدل برای تحلیل محتوای رسانه‌ای — آن‌گونه که در نقد سنت انتقالی آمده — ناکافی باشد.",
 "۴. کاربرد عامه‌پسند: در ادبیات متأخر رسانه، «اطلاعات» شانونی با «دانش» یکی گرفته شد و مدل او به الگویی جهان‌شمول برای هر ارتباطی ارتقا یافت، در حالی که شانون خود این تفاوت را برجسته کرده بود.",
 "۵. بی‌اعتنایی به بازخورد: طرح اصلی، انتقال یک‌سویه از منبع تا مقصد را مفروض می‌گیرد؛ بازخورد و تعامل، افزوده‌های بعدی (وینر و مکتب سیبرنتیک) هستند، نه بخشی از صورت‌بندی ۱۹۴۸.",
])

EXAMPLE = "\n".join([
 "در خط تلفن، نویز گرمایی کانال ظرفیت انتقال را محدود می‌کند؛ قضیهٔ شانون دقیقاً نشان می‌دهد تا چه نرخی از اطلاعات می‌توان با احتمال خطای دلخواه کوچک منتقل کرد و چرا فشرده‌سازی و کدگذاری تصحیح خطا دو روی یک سکه‌اند.",
 "در پخش ویدئو، همان منطق به کار می‌رود: آنتروپی صحنه‌های تصویری تعیین می‌کند چقدر می‌توان بیت‌ریت را کاهش داد، و کدهای تصحیح خطا تضمین می‌کنند بسته‌های گم‌شده در شبکه، کیفیت تصویر را فرو نریزند.",
 "در یک پادکست، تفکیک شانونی میان منبع، رمزگذار، کانال و مقصد به تولیدکننده کمک می‌کند کیفیت صدا (نویز کانال)، پهنای باند و نرخ نمونه‌برداری را جداگانه بررسی کند — نه اینکه همه را به «محتوا» فروبکاهد.",
 "در سنجش کیفیت شبکه، ظرفیت کانال به زبان بیت بر ثانیه بیان می‌شود و برنامه‌ریزی پهنای باند بر پایهٔ همان سقف نظری انجام می‌گیرد؛ این کاربرد، نمونهٔ بی‌واسطهٔ مهندسی نظریهٔ شانون است.",
 "در تحلیل رسانه‌ای، دقت اصطلاحی مهم است: اگر «اطلاعات» شانونی را با «معنا» یکی بگیریم، پیام‌های تکراری ولی معنادار را بی‌ارزش می‌شماریم؛ در حالی که از دید نظریه، تکرار ارزش اطلاعاتی را کاهش می‌دهد، نه اهمیت اجتماعی پیام را.",
])

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

def main():
    c = pymysql.connect(host="127.0.0.1", user="root", password="433700", database=DB, charset="utf8mb4", autocommit=False)
    cur = c.cursor()
    cur.execute("SELECT id, properties FROM kb_entities WHERE code=%s", (CODE,))
    eid, pr = cur.fetchone()
    p = json.loads(pr)
    with open(BACKUP, "w", encoding="utf-8") as f:
        json.dump([{"code": CODE, "props": p}], f, ensure_ascii=False, indent=1)
    print("backup -> 1 row")

    p["critique"] = CRITIQUE
    p["example"] = EXAMPLE
    n_sources = len(p.get("sources", []))
    n_verified = sum(1 for civ in p.get("citations", []) if civ.get("verified"))
    cur.execute("SELECT COUNT(*) FROM kb_relations r JOIN kb_entities a ON r.source_id=a.id JOIN kb_entities b ON r.target_id=b.id WHERE a.code=%s OR b.code=%s", (CODE, CODE))
    n_relations = cur.fetchone()[0]
    score, detail, words = rubric(p, n_verified, n_sources, n_relations)
    p["quality_score"] = score
    p["quality_assessment"] = dict(breakdown=detail, total=score,
        method="SPEC §6.1 auto-structural (accuracy is auto-credit, NOT human verification)",
        scored_at=NOW, scored_by=STAMP)
    p["status_scientific_note"] = "score is structural/citation-based; requires human expert review for scientific verification (SPEC §6.4)"
    p["updated_at"] = NOW; p["updated_by"] = STAMP
    cur.execute("UPDATE kb_entities SET properties=%s, version=version+1, updated_at=%s, updated_by=%s WHERE id=%s",
                (json.dumps(p, ensure_ascii=False), NOW, STAMP, eid))
    cur.execute("SELECT COALESCE(MAX(version),0)+1 FROM kb_entity_versions WHERE entity_id=%s", (eid,))
    ver = cur.fetchone()[0]
    cur.execute("INSERT INTO kb_entity_versions (entity_id, version, snapshot, change_reason, changed_by, created_at) VALUES (%s,%s,%s,%s,%s,%s)",
                (eid, ver, json.dumps({"quality_score": score, "words": words, "sources": n_sources, "verified": n_verified}, ensure_ascii=False),
                 "replaced mismatched generic critique/example with Shannon-specific text", STAMP, NOW))
    cur.execute("INSERT INTO kb_audit_log (entity_code, action, detail, source) VALUES (%s,%s,%s,%s)",
                (CODE, "DOC_ENRICH", json.dumps({"quality_score": score, "words": words, "sources": n_sources, "verified": n_verified, "breakdown": detail, "fix": "critique+example overwritten (was Lasswell boilerplate)"}, ensure_ascii=False), STAMP))
    print(f"{CODE}: score={score} words={words} sources={n_sources} verified={n_verified} relations={n_relations}")
    c.commit()
    c.close()
    print("BATCH65c THEORY DONE")

if __name__ == "__main__":
    main()
