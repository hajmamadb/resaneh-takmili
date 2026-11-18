# -*- coding: utf-8 -*-
"""Batch 201: MC-731, MC-432, MC-236, MC-637, MC-538 (FRAMEWORK)."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch201-20261117"
NOW = "2026-11-17 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch201.json"

S = {
    "MC-731": [
        dict(kind="BOOK",
             title_en="Affective Publics: Sentiment, Technology, and Politics",
             title_fa="عمومیت‌های عاطفی: احساس، فناوری و سیاست",
             authors="Zizi Papacharissi", year=2015,
             publisher="Oxford University Press",
             doi=None,
             url="https://academic.oup.com/book/26400",
             language="en", isbn=None,
             citation="Papacharissi, Z. (2015). Affective Publics: Sentiment, Technology, and Politics. New York: Oxford University Press.",
             locator="book",
             locator_type="BOOK",
             supports="affective publics formed through storytelling and shared sentiment on platforms",
             verified=True),
        dict(kind="BOOK",
             title_en="Marxism and Literature",
             title_fa="مارکسیسم و ادبیات",
             authors="Raymond Williams", year=1977,
             publisher="Oxford University Press",
             doi=None,
             url=None,
             language="en", isbn=None,
             citation="Williams, R. (1977). Marxism and Literature. Oxford: Oxford University Press.",
             locator="structures of feeling",
             locator_type="CHAPTER",
             supports="structures of feeling as emergent, shared affective experience before it is formalized",
             verified=True),
    ],
    "MC-432": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Affect, Not Ideology: A Social Identity Perspective on Polarization",
             title_fa="عاطفه، نه ایدئولوژی: چشم‌اندازی هویتی-اجتماعی بر قطب‌بندی",
             authors="Shanto Iyengar; Gaurav Sood; Yphtach Lelkes", year=2012,
             publisher="Public Opinion Quarterly",
             doi=None,
             url="https://academic.oup.com/poq/article/76/3/405/1894274",
             language="en", isbn=None,
             citation="Iyengar, S., Sood, G., & Lelkes, Y. (2012). Affect, not ideology: A social identity perspective on polarization. Public Opinion Quarterly, 76(3), 405-431.",
             locator="76(3), 405-431",
             locator_type="PAGE",
             supports="partisan affect and social distance, rather than issue positions, drive contemporary polarization",
             verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Origins and Consequences of Affective Polarization in the United States",
             title_fa="خاستگاه‌ها و پیامدهای قطب‌بندی عاطفی در ایالات متحده",
             authors="Shanto Iyengar; Yphtach Lelkes; Matthew Levendusky; Neil Malhotra; Sean J. Westwood", year=2019,
             publisher="Annual Review of Political Science",
             doi=None,
             url=None,
             language="en", isbn=None,
             citation="Iyengar, S., Lelkes, Y., Levendusky, M., Malhotra, N., & Westwood, S. J. (2019). The origins and consequences of affective polarization in the United States. Annual Review of Political Science, 22, 129-146.",
             locator="22, 129-146",
             locator_type="PAGE",
             supports="a review of measurement, causes and consequences of affective polarization",
             verified=True),
    ],
    "MC-236": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Critical Questions for Big Data: Provocations for a Cultural, Technological, and Scholarly Phenomenon",
             title_fa="پرسش‌های انتقادی دربارهٔ داده‌های بزرگ: برانگیزه‌هایی برای یک پدیدهٔ فرهنگی، فناورانه و علمی",
             authors="danah boyd; Kate Crawford", year=2012,
             publisher="Information, Communication & Society",
             doi="10.1080/1369118X.2012.678878",
             url="https://www.tandfonline.com/doi/full/10.1080/1369118X.2012.678878",
             language="en", isbn=None,
             citation="boyd, d., & Crawford, K. (2012). Critical questions for big data: Provocations for a cultural, technological, and scholarly phenomenon. Information, Communication & Society, 15(5), 662-679. https://doi.org/10.1080/1369118X.2012.678878",
             locator="15(5), 662-679",
             locator_type="PAGE",
             supports="six provocations on objectivity, sampling, context and ethics of big data",
             verified=True),
        dict(kind="BOOK",
             title_en="The Data Revolution: Big Data, Open Data, Data Infrastructures and Their Consequences",
             title_fa="انقلاب داده: کلان‌داده، دادهٔ باز، زیرساخت‌های داده و پیامدهای آن‌ها",
             authors="Rob Kitchin", year=2014,
             publisher="Sage",
             doi=None,
             url=None,
             language="en", isbn=None,
             citation="Kitchin, R. (2014). The Data Revolution: Big Data, Open Data, Data Infrastructures and Their Consequences. London: Sage.",
             locator="chapters on data infrastructures and ethics",
             locator_type="CHAPTER",
             supports="the infrastructural and ethical analysis of data-driven knowledge production",
             verified=True),
    ],
    "MC-637": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Issue Ownership in Presidential Elections, with a 1980 Case Study",
             title_fa="مالکیت موضوع در انتخابات ریاست‌جمهوری، با مطالعهٔ موردی ۱۹۸۰",
             authors="John R. Petrocik", year=1996,
             publisher="American Journal of Political Science",
             doi=None,
             url="https://www.jstor.org/stable/2111797",
             language="en", isbn=None,
             citation="Petrocik, J. R. (1996). Issue ownership in presidential elections, with a 1980 case study. American Journal of Political Science, 40(3), 825-850.",
             locator="40(3), 825-850",
             locator_type="PAGE",
             supports="issue ownership theory and issue-based voting",
             verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Issue Ownership and Presidential Campaigning, 1952-2000",
             title_fa="مالکیت موضوع و کارزار انتخاباتی ریاست‌جمهوری، ۱۹۵۲ تا ۲۰۰۰",
             authors="John R. Petrocik; William L. Benoit; Glenn J. Hansen", year=2003,
             publisher="Political Science Quarterly",
             doi=None,
             url=None,
             language="en", isbn=None,
             citation="Petrocik, J. R., Benoit, W. L., & Hansen, G. J. (2003). Issue ownership and presidential campaigning, 1952-2000. Political Science Quarterly, 118(4), 599-626.",
             locator="118(4), 599-626",
             locator_type="PAGE",
             supports="campaign strategy evidence that parties emphasize owned issues",
             verified=True),
    ],
    "MC-538": [
        dict(kind="CONFERENCE_PAPER",
             title_en="From Game Design Elements to Gamefulness: Defining Gamification",
             title_fa="از عناصر طراحی بازی به بازی‌گونگی: تعریف گیمیفیکیشن",
             authors="Sebastian Deterding; Dan Dixon; Rilla Khaled; Lennart Nacke", year=2011,
             publisher="ACM (MindTrek 2011)",
             doi="10.1145/2181037.2181040",
             url="https://dl.acm.org/doi/10.1145/2181037.2181040",
             language="en", isbn=None,
             citation="Deterding, S., Dixon, D., Khaled, R., & Nacke, L. (2011). From game design elements to gamefulness: Defining gamification. In Proceedings of the 15th International Academic MindTrek Conference (pp. 9-15). ACM. https://doi.org/10.1145/2181037.2181040",
             locator="pp. 9-15",
             locator_type="PAGE",
             supports="gamification as the use of game design elements in non-game contexts",
             verified=True),
        dict(kind="CONFERENCE_PAPER",
             title_en="Does Gamification Work? A Literature Review of Empirical Studies on Gamification",
             title_fa="آیا گیمیفیکیشن کار می‌کند؟ مروری بر پژوهش‌های تجربی",
             authors="Juho Hamari; Jonna Koivisto; Harri Sarsa", year=2014,
             publisher="HICSS (IEEE)",
             doi=None,
             url=None,
             language="en", isbn=None,
             citation="Hamari, J., Koivisto, J., & Sarsa, H. (2014). Does gamification work? A literature review of empirical studies on gamification. In Proceedings of the 47th Hawaii International Conference on System Sciences (pp. 3025-3034). IEEE.",
             locator="pp. 3025-3034",
             locator_type="PAGE",
             supports="mixed but generally positive effects of gamification, contingent on context and design",
             verified=True),
    ],
}

ENRICH = {
    "MC-731": dict(
        needs_enrichment=False,
        principles=["توجه به عاطفه به‌عنوان سازندهٔ عمومیت، نه فقط واکنش به آن", "تحلیل روایت و داستان‌سرایی کاربران", "پیوند ساختارهای احساس با بستر پلتفرم", "پرهیز از یکسان‌انگاری هیجان با عقلانیت سیاسی", "توجه به نابرابری صدا و دیده‌شدن", "بررسی گذر از عمومیت عاطفی به کنش سیاسی", "تفکیک عمومیت گذرا از عمومیت سازمان‌یافته در تحلیل پیامدها", "پرهیز از تقلیل احساس جمعی به هیجان منفی یا غیرعقلانی", "بررسی رابطهٔ عاطفه با اعتماد به نهادها و رسانه"],
        detailed_analysis="عمومیت عاطفی نه جمعیتی از افراد با نظر مشترک، بلکه پیوند موقت و احساسی کسانی است که با داستان‌سرایی دربارهٔ یک رویداد به هم می‌رسند. پاپاچاریسی (۲۰۱۵) نشان می‌دهد هشتگ‌ها و جریان‌های خبری، قالب‌هایی برای بیان عمومی احساس فراهم می‌کنند: کاربر تجربهٔ شخصی را روایت می‌کند، دیگران آن را بازنشر می‌دهند و در این جریان، حس «ما» ساخته می‌شود. مفهوم ساختارهای احساس ویلیامز (۱۹۷۷) توضیح می‌دهد که این حس مشترک پیش از صورت‌بندی ایدئولوژیک شکل می‌گیرد و می‌تواند به بسیج یا به فرسایش گفت‌وگو بینجامد. برای پژوهش رسانه، پرسش کلیدی این است که چه عواطفی دیده می‌شوند، چه کسانی صدای بلندتری دارند، و عمومیت عاطفی چه هنگام به کنش پایدار یا به دوقطبی‌شدن تبدیل می‌شود. از این منظر، تحلیل عاطفه باید هم‌زمان سه لایه را ببیند: متن و روایت کاربر، معماری تعامل پلتفرم، و زمینهٔ سیاسی که چرخهٔ احساس را تقویت یا مهار می‌کند؛ نادیده گرفتن هر لایه تصویر را ناقص می‌کند. همچنین باید میان عمومیت عاطفی گذرا و عمومیت سازمان‌یافته تفکیک کرد: تنها دومی است که به ساختارهای پایدار کنش جمعی، رسانهٔ جایگزین یا نهاد سیاسی می‌رسد و می‌تواند در برابر فشار سانسور یا بی‌اعتمادی دوام بیاورد.",
        recommended_sources="«عمومیت‌های عاطفی: احساس، فناوری و سیاست» (پاپاچاریسی، ۲۰۱۵)؛ «مارکسیسم و ادبیات» (ویلیامز، ۱۹۷۷) برای مفهوم ساختارهای احساس؛ پژوهش‌های هشتگ و کنشگری عاطفی.",
    ),
    "MC-432": dict(
        needs_enrichment=False,
        key_concepts=["هویت حزبی", "دماسنج احساسی", "فاصلهٔ اجتماعی", "بیرون‌گروه", "هم‌رنگی هویتی"],
        recommended_sources="«عاطفه، نه ایدئولوژی» (اینگار، سود و للکز، ۲۰۱۲)؛ «خاستگاه‌ها و پیامدهای قطب‌بندی عاطفی» (اینگار و همکاران، ۲۰۱۹)؛ پژوهش‌های رسانه‌های اجتماعی و تقویت قطب‌بندی.",
    ),
    "MC-236": dict(
        needs_enrichment=False,
        key_concepts=["دادهٔ خام به‌مثابه افسانه", "سوگیری نمونه", "همبستگی کاذب", "اخلاق داده", "شکاف دسترسی به داده"],
        recommended_sources="«پرسش‌های انتقادی دربارهٔ داده‌های بزرگ» (بوید و کراورفورد، ۲۰۱۲)؛ «انقلاب داده» (کیچین، ۲۰۱۴)؛ پژوهش‌های اخلاق داده و عدالت داده.",
    ),
    "MC-637": dict(
        needs_enrichment=False,
        detailed_analysis="مالکیت موضوع می‌گوید رأی‌دهنده به موضوعی رأی می‌دهد که به باور او یک حزب بهتر از دیگری از عهدهٔ آن برمی‌آید. پتروچیک (۱۹۹۶) نشان داد شهرت تاریخی حزب در کارایی، ابزار تحلیلی مهمی است: جمهوری‌خواهان در موضوعاتی مانند امنیت و مالیات و دموکرات‌ها در موضوعاتی مانند رفاه و محیط زیست «مالک» شناخته می‌شوند. کارزار انتخاباتی دو راه دارد: برجسته‌سازی موضوع‌های مالکیت‌شده یا تلاش برای تغییر مالکیت با عملکرد و پیام. پتروچیک، بنوا و هانسن (۲۰۰۳) با داده‌های کارزارهای ۱۹۵۲ تا ۲۰۰۰ نشان دادند احزاب به‌طور نظام‌مند موضوع‌های مالکیت‌شده را برجسته می‌کنند. در محیط رسانه‌ای چندکاناله، پرسش تازه این است که الگوریتم‌ها و رسانه‌های حزبی چگونه بر برجستگی و ادراک مالکیت اثر می‌گذارند و آیا مرز مالکیت موضوعی را جابه‌جا می‌کنند.",
        recommended_sources="«مالکیت موضوع در انتخابات ریاست‌جمهوری» (پتروچیک، ۱۹۹۶)؛ «مالکیت موضوع و کارزار انتخاباتی ریاست‌جمهوری» (پتروچیک، بنوا و هانسن، ۲۰۰۳)؛ پژوهش‌های دستور کار رسانه و ارتباطات سیاسی.",
    ),
    "MC-538": dict(
        needs_enrichment=False,
        key_concepts=["بازی جدی", "گیمیفیکیشن", "بازی‌گونگی", "انگیزهٔ درونی", "بازخورد فوری"],
        principles=["کاربرد عناصر بازی برای هدف غیربازی", "طراحی بر پایهٔ انگیزهٔ درونی نه فقط پاداش بیرونی", "سنجش اثر با معیارهای زمینه‌ای", "پرهیز از یکسان‌انگاری بازی جدی با سرگرمی", "توجه به خطر دستکاری رفتار", "ارزیابی پایداری اثر پس از پایان مداخله", "ملاحظهٔ عدالت در دسترسی به تجربهٔ بازی‌گونه"],
        recommended_sources="«از عناصر طراحی بازی به بازی‌گونگی» (دتردینگ و همکاران، ۲۰۱۱)؛ «آیا گیمیفیکیشن کار می‌کند؟» (هاماری، کویویستو و سارسا، ۲۰۱۴)؛ پژوهش‌های بازی جدی در آموزش و سلامت.",
    ),
}

NAME_FIX = {}

YEAR_FIX = {
    "MC-731": "year=2015 (Papacharissi 2015); Williams 1977 verified; rebuilt wrong-topic detailed analysis",
    "MC-432": "year=2012 (Iyengar, Sood & Lelkes 2012); 2019 review verified; removed Latin glosses and replaced irrelevant recommendations",
    "MC-236": "year=2012 (boyd & Crawford 2012); Kitchin 2014 verified; removed Latin glosses and replaced generic-methods recommendations",
    "MC-637": "year=1996 (Petrocik 1996); Petrocik, Benoit & Hansen 2003 verified; rebuilt wrong-topic detailed analysis",
    "MC-538": "year=2011 (Deterding et al. 2011); Hamari et al. 2014 verified; removed Latin glosses and replaced irrelevant recommendations",
}


def wc(v):
    if v is None:
        return 0
    if isinstance(v, str):
        return len(v.split())
    if isinstance(v, (list, tuple)):
        return sum(len(str(x).split()) for x in v)
    return 0


def has_content(v):
    if v is None:
        return False
    if isinstance(v, str):
        return bool(v.strip())
    if isinstance(v, (list, dict)):
        return len(v) > 0
    return True


REQUIRED_SECTIONS = ["summary", "definition", "main_problem", "mechanism", "assumptions",
                     "principles", "critiques", "applications", "evolution", "key_concepts",
                     "theorists", "model", "studies"]
WORD_KEYS = ["summary", "definition", "main_problem", "mechanism", "critiques",
             "applications", "evolution", "key_concepts", "principles", "studies", "assumptions"]


def rubric(p, n_verified, n_sources, n_relations):
    present = sum(1 for k in REQUIRED_SECTIONS if has_content(p.get(k)))
    structure = round(15 * min(1, present / 7))
    words = sum(wc(p.get(k)) for k in WORD_KEYS)
    if words >= 500:
        analysis = 15
    elif words >= 300:
        analysis = 13
    elif words >= 180:
        analysis = 11
    elif words >= 100:
        analysis = 8
    else:
        analysis = 3
    if n_verified >= 1 and n_sources >= 2:
        citation = 20
    elif n_verified >= 1:
        citation = 17
    elif n_sources >= 1:
        citation = 10
    else:
        citation = 0
    accuracy = 0
    if has_content(p.get("summary")) and has_content(p.get("definition")):
        accuracy += 10
    if n_verified >= 1:
        accuracy += 9
    if present >= 6:
        accuracy += 6
    accuracy = min(25, accuracy)
    relations = 10 if n_relations >= 1 else 6
    classification = 5 if (p.get("mapping") or p.get("category_id")) else 0
    clarity = 5 if has_content(p.get("summary")) else 0
    currency = 5
    score = structure + analysis + citation + accuracy + relations + classification + clarity + currency
    detail = "structure=%d analysis=%d citation=%d accuracy=%d relations=%d classification=%d clarity=%d currency=%d" % (
        structure, analysis, citation, accuracy, relations, classification, clarity, currency)
    return score, detail, words


def ensure_source(cur, src):
    if src.get("doi"):
        cur.execute("SELECT id FROM kb_sources WHERE doi=%s LIMIT 1", (src["doi"],))
        r = cur.fetchone()
        if r:
            return r[0]
    cur.execute("SELECT id FROM kb_sources WHERE title_en=%s AND year=%s LIMIT 1",
                (src["title_en"], src["year"]))
    r = cur.fetchone()
    if r:
        return r[0]
    cur.execute("""INSERT INTO kb_sources
        (kind,title_fa,title_en,year,publisher,doi,isbn,issn,url,language,access_type,bibliographic,work_id)
        VALUES (%s,%s,%s,%s,%s,%s,%s,NULL,%s,%s,'unknown',%s,NULL)""",
                (src["kind"], src["title_fa"], src["title_en"], src["year"], src["publisher"],
                 src.get("doi"), src.get("isbn"), src.get("url"), src["language"],
                 json.dumps({"authors": src["authors"], "citation": src["citation"]}, ensure_ascii=False)))
    return cur.lastrowid



YEAR_FIX.update({
    "MC-582": "year corrected 2000 -> 2001 (verified anchor: Baker & Martinson, TARES Test, 2001); note: editorial card theorist attribution was unverifiable and documentation rebuilt from verified literature",
    "MC-598": "no year change; note: editorial card core_logic was a mismatched media-economics template, documentation rebuilt from Heath (1993) and Ihlen (2011)",
})


def main():
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="433700",
                           database=DB, charset="utf8mb4", autocommit=False)
    cur = conn.cursor()
    codes = list(ENRICH.keys())
    ph = ",".join(["%s"] * len(codes))
    cur.execute("SELECT id,code,properties FROM kb_entities WHERE code IN (%s)" % ph, codes)
    rows = cur.fetchall()
    found = {r[1]: r for r in rows}
    missing = [c for c in codes if c not in found]
    assert not missing, "not found: %s" % missing

    snap = []
    for code, (eid, _c, props) in found.items():
        snap.append({"id": eid, "code": code, "properties": json.loads(props)})
    with open(BACKUP, "w", encoding="utf-8") as f:
        json.dump(snap, f, ensure_ascii=False, indent=1)
    print("backup ->", len(snap), "rows")

    for code in codes:
        eid, _c, props = found[code]
        p = json.loads(props)
        en = ENRICH[code]

        if "critique_text" in en:
            p["critique"] = en["critique_text"]
        if "example_text" in en:
            p["example"] = en["example_text"]
        for k, v in en.items():
            if k in ("critique_text", "example_text"):
                continue
            p[k] = v

        p["sources"] = []
        p["citations"] = []
        for src in S[code]:
            p["sources"].append({
                "citation": src["citation"],
                "title_en": src["title_en"],
                "title_fa": src["title_fa"],
                "year": src["year"],
                "doi": src.get("doi"),
                "url": src.get("url"),
                "language": src["language"],
                "verified": src["verified"],
            })
            p["citations"].append({
                "source": src["citation"],
                "locator": src["locator"],
                "supports": src["supports"],
                "verified": src["verified"],
            })

        cur.execute("SELECT COUNT(*) FROM kb_relations WHERE source_id=%s OR target_id=%s", (eid, eid))
        n_rel = cur.fetchone()[0]
        n_sources = len(p["sources"])
        n_verified = sum(1 for x in p["citations"] if x.get("verified"))
        score, detail, words = rubric(p, n_verified, n_sources, n_rel)

        p["quality_score"] = score
        p["quality_assessment"] = "ارزیابی خودکار SPEC §6.1: %d/100 (نمره پایه؛ نیازمند بازبینی علمی انسانی)" % score
        p["status_scientific_note"] = "مستندسازی با منابع تأییدشده شبکه‌ای؛ نمره بر پایه سنجه خودکار است و جانشین داوری علمی (SPEC §6.4) نیست."
        p["updated_at"] = NOW
        p["updated_by"] = STAMP

        if code in NAME_FIX:
            fa_name, en_name, why = NAME_FIX[code]
            cur.execute("UPDATE kb_entities SET canonical_name_fa=%s, canonical_name_en=%s WHERE id=%s",
                        (fa_name, en_name, eid))
            cur.execute("""INSERT INTO kb_audit_log (entity_code,action,detail,source,created_at)
                VALUES (%s,'DOC_FIX',%s,%s,%s)""",
                        (code, json.dumps({"fix": why}, ensure_ascii=False), STAMP, NOW))

        if code in YEAR_FIX:
            cur.execute("""INSERT INTO kb_audit_log (entity_code,action,detail,source,created_at)
                VALUES (%s,'DOC_FIX',%s,%s,%s)""",
                        (code, json.dumps({"fix": YEAR_FIX[code]}, ensure_ascii=False), STAMP, NOW))

        cur.execute("UPDATE kb_entities SET properties=%s, version=version+1, updated_at=%s WHERE id=%s",
                    (json.dumps(p, ensure_ascii=False), NOW, eid))
        cur.execute("SELECT version FROM kb_entities WHERE id=%s", (eid,))
        new_version = cur.fetchone()[0]

        for src in S[code]:
            sid = ensure_source(cur, src)
            cur.execute("SELECT id FROM kb_evidence WHERE about_code=%s AND source_id=%s LIMIT 1", (code, sid))
            if cur.fetchone():
                continue
            lt = {"work": "SECTION", "page_range": "PAGE", "CHAPTER": "CHAPTER", "PAGE": "PAGE"}.get(src["locator_type"], "SECTION")
            cur.execute("""INSERT INTO kb_citations
                (source_id,locator_type,locator_value,quoted_text,paraphrase,citation_style,language,accessed_at)
                VALUES (%s,%s,%s,NULL,%s,'apa',%s,%s)""",
                        (sid, lt, src["locator"], src["supports"], src["language"], NOW))
            cid = cur.lastrowid
            cur.execute("""INSERT INTO kb_evidence
                (source_id,citation_id,about_code,evidence_type,evidence_summary,quoted_content,locator,
                 page_start,page_end,direction,extraction_method,verification_status,extraction_confidence)
                VALUES (%s,%s,%s,'bibliographic_reference',%s,NULL,%s,NULL,NULL,'supports','ai_extraction',%s,NULL)""",
                        (sid, cid, code, src["supports"], src["locator"],
                         "verified" if src["verified"] else "unverified"))

        cur.execute("""INSERT INTO kb_entity_versions
            (entity_id,version,snapshot,change_reason,changed_by,created_at)
            VALUES (%s,%s,%s,%s,%s,%s)""",
                    (eid, new_version, json.dumps(p, ensure_ascii=False),
                     "full documentation enrichment + verified sources", STAMP, NOW))

        cur.execute("""INSERT INTO kb_audit_log (entity_code,action,detail,source,created_at)
            VALUES (%s,'DOC_ENRICH',%s,%s,%s)""",
                    (code, json.dumps({"score": score, "words": words, "sources": n_sources,
                                       "verified": n_verified, "batch": 201}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH201 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
