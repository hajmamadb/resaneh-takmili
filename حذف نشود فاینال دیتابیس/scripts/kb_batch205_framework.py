# -*- coding: utf-8 -*-
"""Batch 205: MC-678, MC-694, card-403 (FRAMEWORK)."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch205-20261117"
NOW = "2026-11-17 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch205.json"

S = {
    "MC-678": [
        dict(kind="BOOK",
             title_en="Remembering to Forget: Holocaust Memory through the Camera's Eye",
             title_fa="یادآوری برای فراموشی: حافظهٔ هولوکاست از دریچهٔ دوربین",
             authors="Barbie Zelizer", year=1998,
             publisher="University of Chicago Press",
             doi=None,
             url=None,
             language="en", isbn=None,
             citation="Zelizer, B. (1998). Remembering to Forget: Holocaust Memory through the Camera's Eye. Chicago: University of Chicago Press.",
             locator="book",
             locator_type="BOOK",
             supports="press photographs of liberation as agents of collective memory and forgetting",
             verified=True),
        dict(kind="BOOK",
             title_en="On Collective Memory",
             title_fa="دربارهٔ حافظهٔ جمعی",
             authors="Maurice Halbwachs", year=1992,
             publisher="University of Chicago Press",
             doi=None,
             url="https://press.uchicago.edu/ucp/books/book/chicago/O/bo3619875.html",
             language="en", isbn=None,
             citation="Halbwachs, M. (1992). On Collective Memory (L. A. Coser, Ed. & Trans.). Chicago: University of Chicago Press.",
             locator="book",
             locator_type="BOOK",
             supports="social frameworks of memory and the selectivity of collective recollection",
             verified=True),
    ],
    "MC-694": [
        dict(kind="REPORT",
             title_en="Many Voices, One World: Towards a New, More Just, and More Efficient World Information and Communication Order",
             title_fa="صداهای بسیار، یک جهان: به‌سوی نظم نوین، عادلانه‌تر و کارآمدتر اطلاعات و ارتباطات جهانی",
             authors="International Commission for the Study of Communication Problems; Seán MacBride", year=1980,
             publisher="UNESCO",
             doi=None,
             url="https://unesdoc.unesco.org/ark:/48223/pf0000372754",
             language="en", isbn=None,
             citation="International Commission for the Study of Communication Problems. (1980). Many Voices, One World: Towards a New, More Just, and More Efficient World Information and Communication Order. Paris: UNESCO.",
             locator="report",
             locator_type="BOOK",
             supports="analysis of global information imbalance and the NWICO proposals",
             verified=True),
        dict(kind="BOOK",
             title_en="The Global Media: The New Missionaries of Corporate Capitalism",
             title_fa="رسانه‌های جهانی: مبلغان تازهٔ سرمایه‌داری شرکتی",
             authors="Edward S. Herman; Robert W. McChesney", year=1997,
             publisher="Cassell",
             doi=None,
             url="https://archive.org/details/globalmedianewmi0000herm",
             language="en", isbn=None,
             citation="Herman, E. S., & McChesney, R. W. (1997). The Global Media: The New Missionaries of Corporate Capitalism. London: Cassell.",
             locator="book",
             locator_type="BOOK",
             supports="political-economy account of global media concentration after NWICO",
             verified=True),
    ],
    "card-403": [
        dict(kind="REPORT",
             title_en="Many Voices, One World: Towards a New, More Just, and More Efficient World Information and Communication Order",
             title_fa="صداهای بسیار، یک جهان: به‌سوی نظم نوین، عادلانه‌تر و کارآمدتر اطلاعات و ارتباطات جهانی",
             authors="International Commission for the Study of Communication Problems; Seán MacBride", year=1980,
             publisher="UNESCO",
             doi=None,
             url="https://unesdoc.unesco.org/ark:/48223/pf0000372754",
             language="en", isbn=None,
             citation="International Commission for the Study of Communication Problems. (1980). Many Voices, One World. Paris: UNESCO.",
             locator="report",
             locator_type="BOOK",
             supports="origin statement of the New World Information and Communication Order",
             verified=True),
        dict(kind="BOOK",
             title_en="The Global Media: The New Missionaries of Corporate Capitalism",
             title_fa="رسانه‌های جهانی: مبلغان تازهٔ سرمایه‌داری شرکتی",
             authors="Edward S. Herman; Robert W. McChesney", year=1997,
             publisher="Cassell",
             doi=None,
             url="https://archive.org/details/globalmedianewmi0000herm",
             language="en", isbn=None,
             citation="Herman, E. S., & McChesney, R. W. (1997). The Global Media: The New Missionaries of Corporate Capitalism. London: Cassell.",
             locator="book",
             locator_type="BOOK",
             supports="corporate concentration as the counter-force to a balanced information order",
             verified=True),
    ],
}

ENRICH = {
    "MC-678": dict(
        needs_enrichment=False,
        constructs=("• حافظهٔ جمعی: بازسازی گذشته در قالب‌های اجتماعی مشترک.\n"
                    "• فراموشی جمعی: حذف یا حاشیه‌رانی روایت‌ها از حافظهٔ عمومی.\n"
                    "• چارچوب حافظه: ساختار تفسیری که تعیین می‌کند چه چیزی به‌یاد بماند.\n"
                    "• آرشیو و آیین یادبود: نهادها و آیین‌هایی که حافظه را تثبیت می‌کنند.\n"
                    "• تصویر شاهد: عکس و فیلم به‌عنوان مدرک و چارچوب روایت گذشته."),
        core_logic="رسانه‌ها نه مجرای خنثای گذشته، بلکه عامل ساختن حافظه‌اند: انتخاب تصویر، چارچوب‌بندی روایت، تکرار آیینی در سالگردها و منطق آرشیو، برخی روایت‌ها را تثبیت و برخی را به حاشیه می‌راند؛ آنچه به‌یاد می‌ماند و آنچه فراموش می‌شود، پیامد قدرت است.",
        detailed_analysis=("۱. بنیان و منطق نظری\nچارچوب یادآوری و فراموشی جمعی ریشه در بحث هالبواکس (۱۹۹۲) دربارهٔ چارچوب‌های اجتماعی حافظه دارد: حافظه در خلأ فردی عمل نمی‌کند، بلکه در گروه‌ها، زبان و آیین‌ها شکل می‌گیرد و همواره گزینشی است. "
                           "زلایزر (۱۹۹۸) با تحلیل عکس‌های آزادسازی اردوگاه‌های هولوکاست نشان داد که مطبوعات با انتخاب و چیدمان تصویر، حافظهٔ عمومی را می‌سازند و در همان حال ابعادی از رنج را از دید خارج می‌کنند. "
                           "رسانه از این منظر نه کانال انتقال گذشته، بلکه صحنهٔ رقابت روایت‌ها و منافع است؛ آرشیو، سالگرد و آیین یادبود، سازوکارهای تثبیت یا حذف حافظه‌اند.\n\n"
                           "۲. کاربرد و نقد\nاین چارچوب در تحلیل پوشش جنگ، فاجعه و بحران، سیاست سالگرد و آرشیو دیجیتال به‌کار می‌رود و به پژوهشگر یادآوری می‌کند که پرسش «چه چیزی پوشش داده شد؟» را با پرسش «چه چیزی از حافظه حذف شد؟» کامل کند. "
                           "نقد اصلی، رسانه‌محوری بیش از اندازه، سوگیری انتخاب نمونه در مطالعات موردی و ابهام مفهومی حافظهٔ جمعی است؛ با این حال، پیوند آن با قدرت و روایت، همچنان یکی از پرثمرترین چارچوب‌های مطالعات رسانه است."),
        related_approaches="مطالعات حافظهٔ جمعی؛ تاریخ بصری؛ جامعه‌شناسی حافظه؛ تحلیل روایت؛ مطالعات آرشیو.",
        recommended_sources="«یادآوری برای فراموشی» (زلایزر، ۱۹۹۸)؛ «دربارهٔ حافظهٔ جمعی» (هالبواکس، ۱۹۹۲)؛ پژوهش‌های حافظهٔ اجتماعی و رسانه.",
    ),
    "MC-694": dict(
        needs_enrichment=False,
        level="کلان",
        summary="گزارش مک‌براید، سند سال ۱۹۸۰ سازمان آموزشی، علمی و فرهنگی ملل متحد است که با عنوان «صداهای بسیار، یک جهان: به‌سوی نظم اطلاعاتی و ارتباطی جهانی عادلانه‌تر و کارآمدتر» منتشر شد. این گزارش حاصل کار کمیسیون بین‌المللی مطالعهٔ مسائل ارتباطات بود که شان مک‌براید، سیاستمدار و حقوق‌دان ایرلندی، ریاست آن را بر عهده داشت. گزارش، نابرابری جریان اطلاعات میان شمال و جنوب را نقد کرد و خواستار نظم نوین اطلاعات و ارتباطات جهانی شد: تعادل جریان خبر، دسترسی برابر به فناوری، حق ارتباط، مشارکت جوامع محلی در تولید محتوا و کاهش تمرکز مالکیت رسانه. این سند به‌سرعت به نماد جدال سیاسی تبدیل شد؛ کشورهای در حال توسعه آن را برنامهٔ عدالت ارتباطی خواندند و دولت‌های غربی و شرکت‌های رسانه‌ای آن را تهدید آزادی مطبوعات دانستند. پیامد سیاسی آن، خروج دو کشور بزرگ از سازمان آموزشی و فرهنگی ملل متحد در میانهٔ دههٔ ۱۹۸۰ بود. با این حال، ایده‌های گزارش در بحث‌های بعدی دربارهٔ شکاف دیجیتال، تنوع رسانه‌ای، حق ارتباط و قدرت پلتفرم‌ها بازتاب یافت. اهمیت آن برای پژوهش رسانه، پیوند دادن ارتباطات با عدالت اجتماعی و سیاست جهانی است. نقدهای اصلی به آرمان‌گرایی، ابهام سازوکارهای اجرا و خطر تبدیل حق ارتباط به ابزار کنترل دولتی مربوط می‌شود.",
        constructs=("• نظم نوین اطلاعات و ارتباطات: مجموعهٔ اصول و سیاست‌هایی برای متعادل‌سازی جریان جهانی اطلاعات.\n"
                    "• حق ارتباط: حق همهٔ انسان‌ها برای بیان، دسترسی و مشارکت در ارتباطات.\n"
                    "• تعادل جریان خبر: کاهش سلطهٔ خبرگزاری‌های شمال بر روایت جنوب.\n"
                    "• تمرکز مالکیت رسانه: تجمع رسانه در دست شرکت‌های معدود و پیامد آن برای تنوع.\n"
                    "• عدالت ارتباطی: توزیع برابر فرصت‌های ارتباطی میان جوامع."),
        related_approaches="اقتصاد سیاسی رسانه؛ سیاست جهانی ارتباطات؛ عدالت ارتباطی؛ شکاف دیجیتال؛ مطالعات پسااستعماری.",
        recommended_sources="«صداهای بسیار، یک جهان» (گزارش مک‌براید، ۱۹۸۰)؛ «رسانه‌های جهانی» (هرمن و مک‌چزنی، ۱۹۹۷)؛ پژوهش‌های عدالت ارتباطی و شکاف دیجیتال.",
    ),
    "card-403": dict(
        needs_enrichment=False,
        level="کلان",
        definition="نظم نوین جهانی اطلاعات و ارتباطات، چارچوبی است که در دههٔ ۱۹۷۰ و ۱۹۸۰ برای تحلیل و اصلاح نابرابری جریان اطلاعات میان شمال و جنوب شکل گرفت و تعادل خبری، حق ارتباط و تنوع مالکیت رسانه را در کانون سیاست جهانی قرار داد.",
        summary="نظم نوین جهانی اطلاعات و ارتباطات، چارچوبی نظری در سطح کلان برای تحلیل قدرت، سیاست و حاکمیت رسانه است که از بحث‌های دههٔ ۱۹۷۰ دربارهٔ نابرابری جریان اطلاعات برخاست و در گزارش مک‌براید (۱۹۸۰) صورت‌بندی شد.",
        recommended_sources="«صداهای بسیار، یک جهان» (گزارش مک‌براید، ۱۹۸۰)؛ «رسانه‌های جهانی» (هرمن و مک‌چزنی، ۱۹۹۷)؛ اسناد یونسکو دربارهٔ نظم نوین اطلاعات و ارتباطات.",
        theorists_text="کمیسیون بین‌المللی مطالعهٔ مسائل ارتباطات به ریاست شان مک‌براید، با همکاری کارشناسان چند کشور، گزارش ۱۹۸۰ را تدوین کرد؛ این سند در سنت نقد اقتصاد سیاسی رسانه و بحث عدالت جهانی ارتباطات جای می‌گیرد.",
        studies=["گزارش سال ۱۹۸۰ کمیسیون بین‌المللی مطالعهٔ مسائل ارتباطات، نابرابری جریان خبر و پیشنهادهای نظم نوین را منتشر کرد.", "پژوهش‌های اقتصاد سیاسی رسانه، تمرکز مالکیت جهانی را به‌عنوان مانع اصلی تحقق این نظم تحلیل کردند."],
    ),
}

NAME_FIX = {}

YEAR_FIX = {
    "MC-678": "year=1998 (Zelizer 1998); Halbwachs 1992 verified; removed uses-and-gratifications template fields and irrelevant recommendations",
    "MC-694": "year=1980 (MacBride Report); Herman & McChesney 1997 verified; fixed title typo, removed interpersonal-communication template fields",
    "card-403": "year=1980 (MacBride Report); added definition, citations, recommendations and theorist text; removed interpersonal misfire",
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
                                       "verified": n_verified, "batch": 205}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH205 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
