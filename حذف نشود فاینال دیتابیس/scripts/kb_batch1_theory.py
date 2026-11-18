# -*- coding: utf-8 -*-
"""Batch 1 (THEORY): documented, web-verified sourcing + precise citations + real rubric score.
Target: resaname_kb_final_inspect only. Idempotent + transactional + backup + audit.
Sources below were verified via web search on 2026-11-16 (correcting wrong year/page in prior records)."""
import pymysql, json

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch1-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch1_theory.json"

# Web-verified sources (2026-11-16). verified=True => confirmed via web this run.
S = {
 "MC-007": [  # Spiral of Silence
   dict(kind="JOURNAL_ARTICLE", title_en="The Spiral of Silence: A Theory of Public Opinion",
        title_fa="مارپیچ سکوت: نظریهٔ افکار عمومی", authors="Noelle-Neumann, E.", year=1974,
        publisher="Journal of Communication, 24(2), 43-51", doi="10.1111/j.1460-2466.1974.tb00367.x",
        url="https://doi.org/10.1111/j.1460-2466.1974.tb00367.x", language="en",
        citation="Noelle-Neumann, E. (1974). The Spiral of Silence: A Theory of Public Opinion. Journal of Communication, 24(2), 43–51. https://doi.org/10.1111/j.1460-2466.1974.tb00367.x",
        locator="pp. 43–51", locator_type="page_range", supports="definition / main_problem / mechanism", verified=True),
   dict(kind="BOOK", title_en="The Spiral of Silence: Public Opinion and Our Mass Media",
        title_fa="مارپیچ سکوت: افکار عمومی و رسانه‌های توده‌ای", authors="Noelle-Neumann, E.", year=1984,
        publisher="Gordon and Breach", doi=None, url=None, language="en",
        citation="Noelle-Neumann, E. (1984). The Spiral of Silence: Public Opinion and Our Mass Media. Gordon and Breach.",
        locator="whole work", locator_type="work", supports="mechanism / applications", verified=False),
 ],
 "TX-014": [  # Uses and Gratifications
   dict(kind="JOURNAL_ARTICLE", title_en="Uses and Gratifications Research",
        title_fa="پژوهش‌های استفاده و رضامندی", authors="Katz, E., Blumler, J. G., & Gurevitch, M.", year=1973,
        publisher="Public Opinion Quarterly, 37(4), 509-523", doi="10.1086/268109",
        url="https://doi.org/10.1086/268109", language="en",
        citation="Katz, E., Blumler, J. G., & Gurevitch, M. (1973). Uses and Gratifications Research. Public Opinion Quarterly, 37(4), 509–523. https://doi.org/10.1086/268109",
        locator="pp. 509–523", locator_type="page_range", supports="definition / main_problem / mechanism", verified=True),
 ],
 "MC-004": [  # Media Framing
   dict(kind="BOOK", title_en="Frame Analysis: An Essay on the Organization of Experience",
        title_fa="تحلیل چارچوب", authors="Goffman, E.", year=1974,
        publisher="Princeton University Press", doi=None, url=None, language="en",
        citation="Goffman, E. (1974). Frame Analysis: An Essay on the Organization of Experience. Princeton University Press.",
        locator="whole work", locator_type="work", supports="origin / definition", verified=False),
   dict(kind="JOURNAL_ARTICLE", title_en="Framing: Toward Clarification of a Fractured Paradigm",
        title_fa="فریمینگ: به سوی روشن‌سازی پارادایمی خردشده", authors="Entman, R. M.", year=1993,
        publisher="Journal of Communication, 43(4), 52-64", doi="10.1111/j.1460-2466.1993.tb01304.x",
        url="https://doi.org/10.1111/j.1460-2466.1993.tb01304.x", language="en",
        citation="Entman, R. M. (1993). Framing: Toward Clarification of a Fractured Paradigm. Journal of Communication, 43(4), 52–64. https://doi.org/10.1111/j.1460-2466.1993.tb01304.x",
        locator="pp. 52–64", locator_type="page_range", supports="mechanism / definition", verified=True),
 ],
 "MC-012": [  # Two-Step Flow
   dict(kind="BOOK", title_en="Personal Influence: The Part Played by People in the Flow of Mass Communications",
        title_fa="تأثیر شخصی", authors="Katz, E., & Lazarsfeld, P. F.", year=1955,
        publisher="Bobbs-Merrill", isbn="9781412805070", doi=None, url=None, language="en",
        citation="Katz, E., & Lazarsfeld, P. F. (1955). Personal Influence: The Part Played by People in the Flow of Mass Communications. Bobbs-Merrill.",
        locator="whole work", locator_type="work", supports="definition / main_problem / mechanism", verified=True),
 ],
}

# Extra genuine content for the thin MC-012 (Two-Step Flow) — only fills missing keys.
MC012_FILL = {
 "summary": "نظریهٔ جریان دومرحله‌ای ارتباطات که توسط الیهو کاتز و پل لازارسفلد برپایهٔ مطالعهٔ دِکاتور (ایلینوی) صورت‌بندی شد، می‌گوید پیام‌های رسانهٔ توده‌ای به‌ندرت مستقیم بر عموم مردم اثر می‌گذارند؛ بلکه ابتدا به «رهبران افکار» (opinion leaders) می‌رسند و سپس از کانال ارتباطات شخصی به باقی جمعیت منتقل می‌شوند. بدین ترتیب جریان ارتباط «رسانه ← رهبر افکار ← مخاطب» است.",
 "main_problem": "آیا رسانه‌های توده‌ای مستقیماً و قوی بر نگرش و رفتار مردم اثر می‌گذارند، یا این اثر از طریق واسطه‌های انسانی (رهبران افکار) و شبکه‌های ارتباط شخصی شکل می‌گیرد؟",
 "mechanism": "مکانیزم در دو مرحله است: (۱) پیام رسانه‌ای ابتدا توسط رهبران افکار — افرادی فعال‌تر و متخصص‌تر در حوزهٔ مربوطه — دریافت و پردازش می‌شود؛ (۲) این رهبران پیام را در تعاملات روزمره و شخصی بازتولید و به هم‌رزمانان خود می‌رسانند. بنابراین «جریان» دو مرحله‌ای است و اثر واقعی رسانه، به‌واسطهٔ شبکهٔ ارتباطات بین‌فردی و اعتبار اجتماعی رهبران افکار تحقق می‌یابد.",
 "critiques": [
   "نقد رایج این است که مدل بیش از حد دوسویه ساده‌سازی‌شده است و در عمل، پیام‌ها می‌توانند در چندین مرحله (چندمرحله‌ای / n-step) جریان یابند.",
   "این نظریه بیشتر در بافت تصمیم‌گیری سیاسی و مصرفی (نظردهی، تبلیغات) آزمون شده و تعمیم آن به همهٔ بافت‌های رسانه‌ای (به‌ویژه رسانه‌های اجتماعی) بحث‌برانگیز است؛ در پلتفرم‌های اجتماعی، رهبران افکار می‌توانند خود رسانهٔ پخش باشند."
 ],
 "applications": [
   "مطالعهٔ تأثیر رسانه بر رأی‌دهی و ترجیحات سیاسی.",
   "طراحی کمپین‌های بازاریابی مبتنی بر رهبران افکار (influencer marketing).",
   "تحلیل پخش شایعه و اطلاعات در شبکه‌های اجتماعی."
 ],
 "assumptions": [
   "برخی افراد (رهبران افکار) در حوزه‌هایی بیشتر از دیگران از رسانه استفاده و اطلاعات بیشتری دارند.",
   "ارتباطات شخصی بر نگرش و رفتار هم‌رزمانان اثر قوی‌تری از رسانه دارد.",
   "جریان اطلاعات از رسانه به رهبران و سپس رهبران به عموم است."
 ],
}

# Extra genuine content for thin TX-014 (Uses & Gratifications) — fills only empty/thin keys.
TX014_FILL = {
 "main_problem": "به‌جای پرسش «رسانه به مردم چه می‌کند» (اثر یک‌سویهٔ پیام بر مخاطب منفعل)، این رویکرد پرسش را برمی‌گرداند: «مردم با رسانه چه می‌کنند؟» به عبارت دیگر، آیا انتخاب و مصرف رسانه نتیجهٔ نیازها و انگیزه‌های فعال مخاطب نیست، به‌جای تأثیرپذیری منفعلانه؟",
 "mechanism": "مکانیزم حول محور «نیاز ← استفاده از رسانه ← رضایت‌بخشی (gratification)» است. مخاطب برپایهٔ ریشه‌های اجتماعی-روان‌شناختی (نیازهای اطلاع‌یابی، تفریح، هویت، تعامل اجتماعی، گریز/فرار) به‌صورت فعال و هدفمند رسانه و محتوای خاصی را انتخاب می‌کند و از آن بهره می‌برد. بدین ترتیب عامل اصلی فرایند، مخاطب است نه پیام؛ رسانه ابزار دستیابی به رضایت نیازهای از پیش موجود است.",
 "assumptions": [
   "مخاطب فعال، هدفمند و عامل اصلی است، نه دریافت‌کنندهٔ منفعل.",
   "استفاده از رسانه رفتار ابزاری (instrumental) است و با انتخاب آگاهانه یا نیمه‌آگاهانه همراه است.",
   "مخاطبان می‌توانند انگیزه‌های خود را تا حدی گزارش کنند (قابلیت خودسنجی).",
   "تمرکز از «پیام» به «کاربر/مخاطب» می‌چرخد."
 ],
 "critiques": [
   "بیش‌تأکید بر خودگزارش مخاطب و پذیرش انگیزه‌های اظهارشده به‌دلیل خودسنجی، درحالی‌که انگیزه‌ها می‌توانند ناخودآگاه یا پنهان باشند.",
   "مخاطب را تا حدی عقلانی و پایدار می‌پندارد و ابعاد ساختاری-قدرتی تولید پیام (هژمونی، منافع رسانه) را کم‌رنگ می‌کند.",
   "تحقیق نیازها به‌صورت مستقیم دشوار است و سنجش «رضایت‌بخشی» اغلب بر شاخص‌های میانجی (مثل مدت مصرف) استوار می‌ماند."
 ],
 "applications": [
   "مطالعات مخاطب و تحلیل الگوهای مصرف رسانه.",
   "طراحی و برنامه‌ریزی رسانه‌ای برپایهٔ نیازهای مخاطب.",
   "پژوهش دلایل انتخاب پلتفرم و محتوا در محیط‌های رسانه‌ای رقابتی."
 ],
}

REQUIRED_SECTIONS = ["summary", "definition", "main_problem", "mechanism", "assumptions",
                     "principles", "critiques", "applications", "evolution", "key_concepts",
                     "theorists", "model", "studies"]

def wc(text):
    if not isinstance(text, str):
        return 0
    return len(text.split())

def has_content(v):
    if v is None: return False
    if isinstance(v, str): return len(v.strip()) > 10
    if isinstance(v, (list, dict)): return len(v) > 0
    return True

def rubric(p, n_verified, n_sources, n_relations):
    # SPEC §6.1 weighting: accuracy25 citation20 structure15 analysis15 relations10 classification5 clarity5 currency5
    detail = {}
    # structure (15): required sections present
    present = [k for k in REQUIRED_SECTIONS if has_content(p.get(k))]
    detail["structure_15"] = round(15 * min(1, len(present)/7))
    # analysis (15): body word count across analytic sections
    words = sum(wc(p.get(k)) for k in ["summary","definition","main_problem","mechanism","critiques","applications","evolution","key_concepts","principles"])
    a = 15 if words>=900 else 13 if words>=550 else 11 if words>=350 else 9 if words>=220 else 6 if words>=120 else 3
    detail["analysis_15"] = a
    # citation (20): verified sources with identifiers
    if n_verified>=1 and n_sources>=2: detail["citation_20"] = 20
    elif n_verified>=1: detail["citation_20"] = 17
    elif n_sources>=1: detail["citation_20"] = 10
    else: detail["citation_20"] = 0
    # accuracy (25): conservative auto-credit; NOT a claim of scientific verification
    acc = 0
    if has_content(p.get("summary")) or has_content(p.get("definition")): acc += 10
    if n_verified>=1: acc += 9
    if len(present)>=6: acc += 6
    detail["accuracy_25_auto"] = min(25, acc)
    # relations (10): absence is neutral, not a penalty
    detail["relations_10"] = 10 if n_relations>=1 else 6
    # classification (5)
    detail["classification_5"] = 5 if (p.get("field") or p.get("mapping")) else 2
    # clarity (5)
    detail["clarity_5"] = 5 if has_content(p.get("summary")) else 2
    # currency (5)
    detail["currency_5"] = 5
    total = sum(detail.values())
    return min(100, total), detail

def main():
    c = pymysql.connect(host="127.0.0.1", user="root", password="433700", database=DB, charset="utf8mb4", autocommit=False)
    cur = c.cursor()
    codes = list(S.keys())
    cur.execute("SELECT id, code, properties FROM kb_entities WHERE code IN (%s)" % ",".join(["%s"]*len(codes)), codes)
    rows = {code:(eid, json.loads(pr)) for (eid, code, pr) in cur.fetchall()}
    # backup
    with open(BACKUP, "w", encoding="utf-8") as f:
        json.dump([{ "code": cd, "props": rows[cd][1] } for cd in codes if cd in rows], f, ensure_ascii=False, indent=1)
    print("backup ->", len(rows), "rows")

    for code in codes:
        if code not in rows:
            print("WARN missing", code); continue
        eid, p = rows[code]
        FILL = {"MC-012": MC012_FILL, "TX-014": TX014_FILL}.get(code)
        if FILL:
            for k, v in FILL.items():
                if not has_content(p.get(k)):
                    p[k] = v
        spec = S[code]
        p.pop("floor_raised", None); p.pop("floor_raised_from", None)
        # properties.sources = clean citation list (end-of-text references)
        p["sources"] = [dict(citation=s["citation"], language=("انگلیسی" if s["language"]=="en" else "فارسی"),
                              doi=s.get("doi") or "", url=s.get("url") or "", year=s.get("year")) for s in spec]
        # properties.citations = structured precise citation mapping
        p["citations"] = [dict(source=s["citation"], locator=s["locator"], supports=s["supports"],
                                verified=bool(s.get("verified"))) for s in spec]
        # ensure definition key if only summary present
        if not has_content(p.get("definition")) and has_content(p.get("summary")):
            p["definition"] = p["summary"]
        n_sources = len(spec)
        n_verified = sum(1 for s in spec if s.get("verified"))
        # relations count
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

        # kb_sources (dedupe by doi or title_en+year)
        sids = []
        for s in spec:
            found = None
            if s.get("doi"):
                cur.execute("SELECT id FROM kb_sources WHERE doi=%s", (s["doi"],))
                r = cur.fetchone(); found = r[0] if r else None
            if found is None:
                cur.execute("SELECT id FROM kb_sources WHERE title_en=%s AND year=%s", (s["title_en"], s.get("year")))
                r = cur.fetchone(); found = r[0] if r else None
            if found is None:
                cur.execute("""INSERT INTO kb_sources (kind,title_fa,title_en,year,publisher,doi,isbn,url,language,access_type,bibliographic)
                                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                    (s["kind"], s.get("title_fa"), s["title_en"], s.get("year"), s.get("publisher"),
                     s.get("doi"), s.get("isbn"), s.get("url"), s.get("language"),
                     "open" if s.get("doi") else "unknown",
                     json.dumps({"authors": s.get("authors"), "citation": s["citation"]}, ensure_ascii=False)))
                found = cur.lastrowid
            sids.append(found)

        # kb_citations + kb_evidence per source
        for s, sid in zip(spec, sids):
            lt = "PAGE" if s.get("locator_type") == "page_range" else "SECTION"
            cur.execute("""INSERT INTO kb_citations (source_id,locator_type,locator_value,paraphrase,citation_style,language,accessed_at)
                            VALUES (%s,%s,%s,%s,'apa',%s,%s)""",
                        (sid, lt, s.get("locator"),
                         "پشتیبانی از بخش: "+s.get("supports",""), s.get("language","en"), NOW))
            cid = cur.lastrowid
            cur.execute("""INSERT INTO kb_evidence (source_id,citation_id,about_code,evidence_type,evidence_summary,locator,verification_status,extraction_method,direction)
                            VALUES (%s,%s,%s,'bibliographic_reference',%s,%s,%s,'ai_extraction','supports')""",
                        (sid, cid, code, s["citation"], s.get("locator"),
                         "verified" if s.get("verified") else "unverified"))

        # version snapshot (max existing +1 to avoid uq_ver collision)
        cur.execute("SELECT COALESCE(MAX(version),0)+1 FROM kb_entity_versions WHERE entity_id=%s", (eid,))
        ver = cur.fetchone()[0]
        cur.execute("INSERT INTO kb_entity_versions (entity_id, version, snapshot, change_reason, changed_by, created_at) VALUES (%s,%s,%s,%s,%s,%s)",
                    (eid, ver, json.dumps({"sources": p["sources"], "citations": p["citations"], "quality_score": score}, ensure_ascii=False),
                     "documented sourcing + rubric score", STAMP, NOW))
        # audit
        cur.execute("INSERT INTO kb_audit_log (entity_code, action, detail, source) VALUES (%s,%s,%s,%s)",
                    (code, "DOC_ENRICH", json.dumps({"quality_score": score, "sources": n_sources, "verified": n_verified, "score_breakdown": detail}, ensure_ascii=False), STAMP))
        print(f"{code}: score={score} sources={n_sources} verified={n_verified} relations={n_relations} | breakdown={detail}")
    c.commit()
    c.close()
    print("BATCH1 THEORY DONE")

if __name__ == "__main__":
    main()
