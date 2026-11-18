# -*- coding: utf-8 -*-
"""Batch 1b (THEORY) phase 2: enrich the two thin entities (TX-014 Uses&Grat, MC-012 Two-Step)
with genuine, web-verified content + a second verified source each, and re-score all four
flagship theories consistently. Transactional + backup + audit. Target: resaname_kb_final_inspect."""
import pymysql, json

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch1b-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch1b_theory.json"

# --- new second source for each thin entity (web-verified 2026-11-16) ---
SECOND = {
 "TX-014": dict(kind="JOURNAL_ARTICLE",
   title_en="On the Uses of Mass Media for Important Things",
   title_fa="به‌کارگیری رسانه‌های توده‌ای برای امور مهم", authors="Katz, E., Gurevitch, M., & Haas, H.", year=1973,
   publisher="American Sociological Review, 38(2), 164-174", doi=None, url=None, language="en",
   citation="Katz, E., Gurevitch, M., & Haas, H. (1973). On the uses of mass media for important things. American Sociological Review, 38(2), 164–174.",
   locator="pp. 164–174", locator_type="page_range", supports="mechanism / assumptions / applications", verified=True),
 "MC-012": dict(kind="BOOK",
   title_en="Voting: A Study of Opinion Formation in a Presidential Campaign",
   title_fa="رأی‌گیری: مطالعه‌ای در شکل‌گیری نگرش در یک کمپین ریاست‌جمهوری", authors="Berelson, B. R., Lazarsfeld, P. F., & McPhee, W. N.", year=1954,
   publisher="University of Chicago Press", isbn=None, doi=None, url=None, language="en",
   citation="Berelson, B. R., Lazarsfeld, P. F., & McPhee, W. N. (1954). Voting: A Study of Opinion Formation in a Presidential Campaign. University of Chicago Press.",
   locator="whole work", locator_type="work", supports="origin / mechanism / studies", verified=True),
}

# --- genuine, richer analytic content (superset of prior thin text) ---
ENRICH = {
 "TX-014": {
   "main_problem": "رویکرد استفاده‌ها و رضامندی‌ها (Uses and Gratifications) پرسش بنیادین «رسانه به مخاطب چه می‌کند؟» (برپایهٔ فرض منفعت‌محوری و اثر یک‌سویهٔ پیام) را برمی‌گرداند و می‌پرسد: «مخاطب با رسانه چه می‌کند و چرا؟» به بیان دیگر، انتخاب و مصرف رسانه تا چه حد نتیجهٔ فعال، هدفمند و ابزاریِ مخاطب است و از چه نیازهای شناختی، عاطفی و اجتماعی ریشه می‌گیرد.",
   "mechanism": "مکانیزم در سه مرحلهٔ زنجیره‌ای «نیاز ← استفاده از رسانه ← رضامندی (gratification)» استوار است. نخست، مخاطب برپایهٔ ریشه‌های اجتماعی-روان‌شناختی خود نیازهای مشخصی دارد — نیازهای شناختی (اطلاعات، درک، اطمینان)، نیازهای عاطفی (سرگرمی، فرار از روزمرگی)، نیازهای اجتماعی-جانبی (تعامل، هویت، ارتباط با دیگران) و نیازهای شخصی (گشت‌وگذار، گریز). سپس بر اساس این نیازها، رسانه و محتوای خاصی را به‌صورت فعال و هدفمند انتخاب می‌کند. و در نهایت، تا جایی که رسانه آن نیاز را ارضا کند، رضامندی حاصل می‌شود. نکتهٔ کلیدی این است که «عامل» فرایند مخاطب است، نه پیام؛ رسانه ابزار دستیابی به رضامندیِ نیازِ از پیش موجود است و نه سازندهٔ آن.",
   "critiques": "مهم‌ترین نقدها: (۱) اتکای بیش‌ازحد به خودگزارش و پذیرش انگیزه‌های اظهارشدهٔ مخاطب به‌عنوان واقعی، درحالی‌که انگیزه‌ها می‌توانند ناخودآگاه، پنهان یا اجتماعی-مدلل‌سازی‌شده باشند؛ (۲) فرض عقلانیت و پایداری مخاطب و کم‌رنگ‌سازی ابعاد ساختاری-قدرتیِ تولید پیام (هژمونی، منافع رسانه‌ای، چارچوب‌های تولیدکننده) که به‌عنوان میراث‌دار رویکردهای انتقادی/مارکسیستی مطرح است؛ (۳) دشواری سنجش مستقیم «نیاز» و «رضامندی» و وابستگی عملی پژوهش‌ها به شاخص‌های میانجی مانند مدت و فرکانس مصرف.",
   "applications": "کاربردها: تحلیل الگوهای مصرف رسانه و تصمیم‌گیری رسانه‌ای مخاطب؛ طراحی و برنامه‌ریزی رسانه‌ای و محتوایی برپایهٔ نیازهای مخاطب (needs-based media planning)؛ پژوهش انتخاب پلتفرم و محتوا در محیط‌های رقابتی چندرسانه‌ای و شبکه‌های اجتماعی؛ و به‌طور کلی هر پژوهش مخاطب‌محوری که «چرایی» انتخاب رسانه را هدف می‌گیرد.",
   "evolution": "این رویکرد در اواخر دههٔ ۱۹۷۰ به‌عنوان پاسخی صریح به مدل‌های «اثرات» رسانه شکل گرفت و با مقالات کاتز، بلوملر و گورویچ (۱۹۷۳) و کاتز، گورویچ و هاس (۱۹۷۳) به‌طور رسمی صورت‌بندی شد. در دهه‌های بعد به‌ویژه در مطالعات تلویزیون و مصرف رسانه‌ای گسترش یافت و در سدهٔ ۲۱ به تحلیل انتخاب پلتفرم، مصرف چندرسانه‌ای و انگیزه‌های تعامل در شبکه‌های اجتماعی رسید.",
   "key_concepts": ["نیاز (need)", "رضامندی (gratification)", "استفادهٔ هدفمند (goal-directed use)", "انتخاب رسانه (media selection)", "نیازهای شناختی/عاطفی/اجتماعی/شخصی"],
   "principles": ["مخاطب فعال و عامل اصلی فرایند است، نه دریافت‌کنندهٔ منفعل", "استفاده از رسانه رفتار ابزاری و هدف‌مند است", "رسانه‌ها برای ارضای نیازهای مشترک با یکدیگر در رقابت‌اند", "هدف‌گیری رسانه تا حدی با اهداف و نیازهای مخاطب گره خورده است"],
   "studies": ["مطالعهٔ کاتز، گورویچ و هاس (۱۹۷۳) در وین: به‌کارگیری رسانه برای «امور مهم»", "پژوهش‌های مصرف تلویزیون برپایهٔ نیازهای شناختی و عاطفی در دهه‌های ۱۹۷۰–۱۹۸۰"],
 },
 "MC-012": {
   "main_problem": "نظریهٔ جریان دومرحله‌ای ارتباطات پرسش می‌کند: آیا رسانه‌های توده‌ای مستقیماً و قوی بر نگرش و رفتار عموم مردم اثر می‌گذارند، یا این اثر عمدتاً از طریق واسطه‌های انسانی — «رهبران افکار» (opinion leaders) — و شبکه‌های ارتباط شخصی شکل می‌گیرد؟ پاسخ این نظریه آن است که جریان ارتباط دو مرحله‌ای است: «رسانه ← رهبر افکار ← مخاطب».",
   "mechanism": "مکانیزم در دو مرحله است. مرحلهٔ نخست: پیام‌های رسانهٔ توده‌ای ابتدا توسط رهبران افکار — افرادی که در حوزهٔ مربوطه فعال‌تر، متخصص‌تر و مصرف‌کنندهٔ بیشتری از رسانه‌اند — دریافت، پردازش و تفسیر می‌شوند. مرحلهٔ دوم: این رهبران پیام را در تعاملات روزمرهٔ شخصی، بازتولید و به هم‌رزمان و همکاران خود می‌رسانند؛ و چون ارتباط شخصی اعتبار و نفوذ اجتماعی بیشتری دارد، اثر واقعی رسانه بر نگرش و رفتار عموم، عمدتاً از این شبکهٔ بین‌فردی تحقق می‌یابد. بنابراین «جریان» دومرحله‌ای است و واسطهٔ انسانی (رهبر افکار) نقش شکیب‌کنندهٔ پیام را ایفا می‌کند.",
   "critiques": ["ساده‌سازی دوسویه: در عمل پیام‌ها می‌توانند در چندین مرحله (چندمرحله‌ای / n-step flow) جریان یابند و نقش رهبر افکار در بسیاری از بافت‌ها ضعیف‌تر است.", "تعمیم‌پذیری: بیشتر در بافت رأی‌دهی سیاسی و تصمیم‌گیری مصرفی آزمون شده؛ تعمیم آن به همهٔ بافت‌های رسانه‌ای — به‌ویژه رسانه‌های اجتماعی که رهبران افکار خود می‌توانند رسانهٔ پخش باشند — بحث‌برانگیز است.", "تعریف ناپایدار «رهبر افکار»: رهبری به حوزه، بافت و موضوع بستگی دارد و فردی که در یک حوزه رهبر افکار است، در حوزهٔ دیگر نیست."],
   "applications": ["مطالعهٔ تأثیر رسانه بر رأی‌دهی و ترجیحات سیاسی", "طراحی کمپین‌های بازاریابی مبتنی بر رهبران افکار (influencer / opinion-leader marketing)", "تحلیل پخش شایعه و اطلاعات در شبکه‌های اجتماعی و نقش حساب‌های پرجنب‌وجوش"],
   "assumptions": ["برخی افراد (رهبران افکار) در حوزه‌هایی مصرف و اطلاعات بیشتری از رسانه دارند", "ارتباط شخصی بر نگرش و رفتار هم‌رزمان اثر قوی‌تری از رسانه دارد", "جریان اطلاعات از رسانه به رهبران و سپس از رهبران به عموم است"],
   "evolution": "ریشهٔ این نظریه در مطالعهٔ دِکاتور (ایلینوی) است که در کتاب «تأثیر شخصی» (کاتز و لازارسفلد، ۱۹۵۵) صورت‌بندی شد و با یافته‌های مطالعهٔ رأی‌گیری ۱۹۴۸ (برنسون، لازارسفلد و مک‌فی، ۱۹۵۴) تقویت شد. در دههٔ ۱۹۶۰ مفهوم به «جریان چندمرحله‌ای» (multi-step flow) گسترش یافت و در پیدایش شبکه‌های اجتماعی به تحلیل رهبران دیجیتال و ویروسی‌شدن محتوا پیوند خورد.",
   "key_concepts": ["رهبر افکار (opinion leader)", "جریان دومرحله‌ای (two-step flow)", "تأثیر شخصی (personal influence)", "شبکهٔ ارتباطات بین‌فردی"],
   "studies": ["مطالعهٔ دِکاتور (کاتز و لازارسفلد، ۱۹۵۵)", "مطالعهٔ رأی‌گیری ۱۹۴۸ (برنسون، لازارسفلد و مک‌فی، ۱۹۵۴)"],
 },
}

REQUIRED_SECTIONS = ["summary", "definition", "main_problem", "mechanism", "assumptions",
                     "principles", "critiques", "applications", "evolution", "key_concepts",
                     "theorists", "model", "studies"]

def wc(v):
    if isinstance(v, str):
        return len(v.split())
    if isinstance(v, list):
        n = 0
        for it in v:
            if isinstance(it, str):
                n += len(it.split())
            elif isinstance(it, dict):
                n += len(' '.join(str(x) for x in it.values()).split())
        return n
    if isinstance(v, dict):
        return len(' '.join(str(x) for x in v.values()).split())
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
    codes = ["MC-007", "TX-014", "MC-004", "MC-012"]
    cur.execute("SELECT id, code, properties FROM kb_entities WHERE code IN (%s)" % ",".join(["%s"]*len(codes)), codes)
    rows = {code:(eid, json.loads(pr)) for (eid, code, pr) in cur.fetchall()}
    with open(BACKUP, "w", encoding="utf-8") as f:
        json.dump([{"code": cd, "props": rows[cd][1]} for cd in codes if cd in rows], f, ensure_ascii=False, indent=1)
    print("backup ->", len(rows), "rows")

    for code in codes:
        eid, p = rows[code]
        # apply enrichment for the two thin entities (overwrite analytic fields; keep summary/theorists)
        if code in ENRICH:
            for k, v in ENRICH[code].items():
                if k not in ("summary", "theorists"):
                    p[k] = v
        spec = p.get("citations") or []   # existing precise citations from batch 1
        # if this is a thin entity, append the second source spec to its properties.sources/citations too
        if code in SECOND:
            s = SECOND[code]
            p.setdefault("sources", []).append(dict(citation=s["citation"],
                language=("انگلیسی" if s["language"]=="en" else "فارسی"),
                doi=s.get("doi") or "", url=s.get("url") or "", year=s.get("year")))
            p.setdefault("citations", []).append(dict(source=s["citation"], locator=s["locator"],
                supports=s["supports"], verified=bool(s.get("verified"))))
        if not has_content(p.get("definition")) and has_content(p.get("summary")):
            p["definition"] = p["summary"]

        n_sources = len(p.get("sources", []))
        n_verified = sum(1 for x in p.get("citations", []) if x.get("verified"))
        cur.execute("SELECT COUNT(*) FROM kb_relations r JOIN kb_entities a ON r.source_id=a.id JOIN kb_entities b ON r.target_id=b.id WHERE a.code=%s OR b.code=%s", (code, code))
        n_relations = cur.fetchone()[0]
        score, detail = rubric(p, n_verified, n_sources, n_relations)

        p["quality_score"] = score
        p["quality_assessment"] = dict(breakdown=detail, total=score,
            method="SPEC §6.1 auto-structural (accuracy is auto-credit, NOT human verification)",
            scored_at=NOW, scored_by=STAMP)
        p["status_scientific_note"] = "score is structural/citation-based; requires human expert review for scientific verification (SPEC §6.4)"
        p["updated_at"] = NOW; p["updated_by"] = STAMP
        cur.execute("UPDATE kb_entities SET properties=%s, version=version+1, updated_at=%s, updated_by=%s WHERE id=%s",
                    (json.dumps(p, ensure_ascii=False), NOW, STAMP, eid))

        # insert the second source + citation + evidence (only for the two thin entities)
        if code in SECOND:
            s = SECOND[code]
            sid = None
            cur.execute("SELECT id FROM kb_sources WHERE title_en=%s AND year=%s", (s["title_en"], s.get("year")))
            r = cur.fetchone(); sid = r[0] if r else None
            if sid is None:
                cur.execute("""INSERT INTO kb_sources (kind,title_fa,title_en,year,publisher,doi,isbn,url,language,access_type,bibliographic)
                                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                    (s["kind"], s.get("title_fa"), s["title_en"], s.get("year"), s.get("publisher"),
                     s.get("doi"), s.get("isbn"), s.get("url"), s.get("language"), "unknown",
                     json.dumps({"authors": s.get("authors"), "citation": s["citation"]}, ensure_ascii=False)))
                sid = cur.lastrowid
            cur.execute("SELECT 1 FROM kb_evidence e WHERE e.about_code=%s AND e.source_id=%s LIMIT 1", (code, sid))
            if cur.fetchone():
                print(f"{code}: 2nd source {sid} already linked, skipping citation/evidence")
            else:
                lt = "PAGE" if s.get("locator_type") == "page_range" else "SECTION"
                cur.execute("""INSERT INTO kb_citations (source_id,locator_type,locator_value,paraphrase,citation_style,language,accessed_at)
                                VALUES (%s,%s,%s,%s,'apa',%s,%s)""",
                            (sid, lt, s.get("locator"), "پشتیبانی از بخش: "+s.get("supports",""), s.get("language","en"), NOW))
                cid = cur.lastrowid
                cur.execute("""INSERT INTO kb_evidence (source_id,citation_id,about_code,evidence_type,evidence_summary,locator,verification_status,extraction_method,direction)
                                VALUES (%s,%s,%s,'bibliographic_reference',%s,%s,%s,'ai_extraction','supports')""",
                            (sid, cid, code, s["citation"], s.get("locator"), "verified"))

        cur.execute("SELECT COALESCE(MAX(version),0)+1 FROM kb_entity_versions WHERE entity_id=%s", (eid,))
        ver = cur.fetchone()[0]
        cur.execute("INSERT INTO kb_entity_versions (entity_id, version, snapshot, change_reason, changed_by, created_at) VALUES (%s,%s,%s,%s,%s,%s)",
                    (eid, ver, json.dumps({"quality_score": score, "analysis_words": rubric(p, n_verified, n_sources, n_relations)[1]["analysis_15"]}, ensure_ascii=False),
                     "phase-2 enrichment + re-score", STAMP, NOW))
        cur.execute("INSERT INTO kb_audit_log (entity_code, action, detail, source) VALUES (%s,%s,%s,%s)",
                    (code, "DOC_ENRICH_P2", json.dumps({"quality_score": score, "sources": n_sources, "verified": n_verified, "breakdown": detail}, ensure_ascii=False), STAMP))
        print(f"{code}: score={score} sources={n_sources} verified={n_verified} relations={n_relations} | {detail}")
    c.commit()
    c.close()
    print("BATCH1b THEORY DONE")

if __name__ == "__main__":
    main()
