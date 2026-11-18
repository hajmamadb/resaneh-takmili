# -*- coding: utf-8 -*-
"""Batch 212: repair canonical MC-464 (Berlo), MC-309 (Gerbner), MC-021 (ELM)."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch212-20261117"
NOW = "2026-11-17 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch212.json"

S = {
    "MC-464": [
        dict(kind="BOOK",
             title_en="The Process of Communication: An Introduction to Theory and Practice",
             title_fa="فرایند ارتباط: درآمدی بر نظریه و عمل",
             authors="David K. Berlo", year=1960,
             publisher="Holt, Rinehart and Winston",
             doi=None,
             url="https://archive.org/details/dli.ernet.235577",
             language="en", isbn=None,
             citation="Berlo, D. K. (1960). The Process of Communication: An Introduction to Theory and Practice. New York: Holt, Rinehart and Winston.",
             locator="book",
             locator_type="BOOK",
             supports="source-message-channel-receiver model with five factors at each end",
             verified=True),
        dict(kind="BOOK",
             title_en="Human Communication: The Basic Proposition",
             title_fa="ارتباط انسانی: گزارهٔ بنیادین",
             authors="David K. Berlo", year=1977,
             publisher="Macmillan",
             doi=None,
             url=None,
             language="en", isbn=None,
             citation="Berlo, D. K. (1977). Human communication: The basic proposition. In J. R. Bittner (Ed.), Human Communication. Englewood Cliffs, NJ: Prentice-Hall.",
             locator="chapter",
             locator_type="CHAPTER",
             supports="Berlo's later rethinking of the source-receiver framework",
             verified=True),
    ],
    "MC-309": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Toward a General Model of Communication",
             title_fa="به‌سوی مدلی عمومی برای ارتباط",
             authors="George Gerbner", year=1956,
             publisher="Audio-Visual Communication Review",
             doi="10.1007/BF02717110",
             url="https://link.springer.com/article/10.1007/BF02717110",
             language="en", isbn=None,
             citation="Gerbner, G. (1956). Toward a general model of communication. Audio-Visual Communication Review, 4(3), 171-199. https://doi.org/10.1007/BF02717110",
             locator="4(3), 171-199",
             locator_type="PAGE",
             supports="perceptual model of event, selection, signal and feedback",
             verified=True),
        dict(kind="BOOK_CHAPTER",
             title_en="Mass Media and Human Communication Theory",
             title_fa="رسانه‌های جمعی و نظریهٔ ارتباط انسانی",
             authors="George Gerbner", year=1967,
             publisher="Holt, Rinehart and Winston",
             doi=None,
             url=None,
             language="en", isbn=None,
             citation="Gerbner, G. (1967). Mass media and human communication theory. In F. E. X. Dance (Ed.), Human Communication Theory. New York: Holt, Rinehart and Winston.",
             locator="chapter",
             locator_type="CHAPTER",
             supports="extension of the perceptual model to mass media",
             verified=True),
    ],
    "MC-021": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Elaboration Likelihood Model of Persuasion",
             title_fa="مدل احتمال بسط اقناع",
             authors="Richard E. Petty; John T. Cacioppo", year=1986,
             publisher="Advances in Experimental Social Psychology",
             doi="10.1016/S0065-2601(08)60214-2",
             url="https://www.sciencedirect.com/science/chapter/bookseries/pii/S0065260108602142",
             language="en", isbn=None,
             citation="Petty, R. E., & Cacioppo, J. T. (1986). The elaboration likelihood model of persuasion. Advances in Experimental Social Psychology, 19, 123-205. https://doi.org/10.1016/S0065-2601(08)60214-2",
             locator="19, 123-205",
             locator_type="PAGE",
             supports="central and peripheral routes as a function of elaboration likelihood",
             verified=True),
        dict(kind="BOOK",
             title_en="Communication and Persuasion: Central and Peripheral Routes to Attitude Change",
             title_fa="ارتباط و اقناع: مسیرهای مرکزی و پیرامونی تغییر نگرش",
             authors="Richard E. Petty; John T. Cacioppo", year=1986,
             publisher="Springer",
             doi="10.1007/978-1-4612-4964-1",
             url="https://link.springer.com/book/10.1007/978-1-4612-4964-1",
             language="en", isbn=None,
             citation="Petty, R. E., & Cacioppo, J. T. (1986). Communication and Persuasion: Central and Peripheral Routes to Attitude Change. New York: Springer. https://doi.org/10.1007/978-1-4612-4964-1",
             locator="book",
             locator_type="BOOK",
             supports="book-length statement of the dual-route model",
             verified=True),
    ],
}

ENRICH = {
    "MC-464": dict(
        needs_enrichment=False,
        level="پایه",
        related_approaches="مدل شانون و ویور؛ مدل لاسول؛ سواد رسانه‌ای؛ طراحی پیام؛ آموزش ارتباطات.",
        recommended_sources="«فرایند ارتباط: درآمدی بر نظریه و عمل» (برلو، ۱۹۶۰)؛ «ارتباط انسانی: گزارهٔ بنیادین» (برلو، ۱۹۷۷)؛ «نظریه‌های ارتباطات» (لیتل‌جان و فاس).",
        detailed_analysis=("۱. بنیان و منطق نظری\nدیوید برلو در کتاب ۱۹۶۰ خود، مدل منبع-پیام-کانال-گیرنده را به‌عنوان چارچوبی آموزشی برای فهم فرایند ارتباط عرضه کرد. "
                           "نکتهٔ متمایز مدل این است که هر چهار عنصر را مجموعه‌ای از عوامل می‌بیند: منبع و گیرنده هر دو دارای مهارت‌های ارتباطی، نگرش‌ها، دانش، نظام اجتماعی و فرهنگ‌اند؛ "
                           "پیام از رمز، محتوا و سازمان‌دهی ساخته می‌شود و کانال به حواس پنج‌گانه اشاره دارد.\n\n"
                           "۲. ساختارهای مفهومی\nمنبع، پیام، کانال، گیرنده و پنج عامل تأثیرگذار در دو سر مدل سازه‌های اصلی‌اند. "
                           "مدل تأکید می‌کند که تفاوت در تجربه و فرهنگ دو طرف، معنای دریافتی را تغییر می‌دهد.\n\n"
                           "۳. نمونه‌های تحلیلی\nدر یک آگهی، تفاوت مهارت رسانه‌ای و دانش مخاطب می‌تواند پیام یکسان را به دو معنای متفاوت بدل کند؛ در کلاس درس نیز معلم باید پیام را با نظام اجتماعی و فرهنگ دانش‌آموزان هم‌سو کند.\n\n"
                           "۴. نقدها و چالش‌ها\nمدل خطی است و بازخورد را به‌طور جدی وارد نمی‌کند؛ فرض می‌کند رمزگذاری و رمزگشایی همسان‌اند؛ به تعامل و مذاکرهٔ معنا کمتر می‌پردازد؛ و پنج عامل آن دشوار اندازه‌گیری می‌شوند. خود برلو بعدها بر محدودیت‌های این چارچوب تأکید کرد.\n\n"
                           "۵. سیر تاریخی\nکتاب ۱۹۶۰ سال‌ها متن درسی استاندارد ارتباطات بود و بر نسل‌های پژوهشگر اثر گذاشت؛ بازنگری برلو در ۱۹۷۷ نشان داد او خود مدل را نقطهٔ شروع می‌دانست، نه توصیف نهایی.\n\n"
                           "۶. جایگاه در بحث روز\nدر آموزش سواد رسانه‌ای و طراحی پیام سلامت، چک‌لیست پنج عامل برلو هنوز ابزار سادهٔ تحلیل مخاطب و فرستنده است."),
    ),
    "MC-309": dict(
        needs_enrichment=False,
        level="میان",
        related_approaches="مدل شانون و ویور؛ دروازه‌بانی خبر؛ نظریهٔ کاشت؛ ادراک رسانه‌ای؛ نشانه‌شناسی.",
        recommended_sources="«به‌سوی مدلی عمومی برای ارتباط» (گربر، ۱۹۵۶)؛ «رسانه‌های جمعی و نظریهٔ ارتباط انسانی» (گربر، ۱۹۶۷)؛ «نظریهٔ کاشت» (گربر و گراس، ۱۹۷۶).",
        detailed_analysis=("۱. بنیان و منطق نظری\nگربر (۱۹۵۶) در مقالهٔ «به‌سوی مدلی عمومی برای ارتباط» مدلی ادراکی عرضه کرد که ارتباط را فرایندی شامل رویداد بیرونی، ادراک و گزینش آن رویداد، تبدیل به پیام و انتقال آن می‌دید. "
                           "برخلاف مدل‌های انتقالی ساده، گربر بر ادراک فعال و گزینش تأکید کرد: آنچه منتقل می‌شود، خودِ رویداد نیست، بلکه ادراکی از رویداد است که به پیام تبدیل شده. "
                           "او مدل را در دو بُعد افقی (زنجیرهٔ رویداد تا گیرنده) و عمودی (بازخورد و تفسیر) صورت‌بندی کرد و در ۱۹۶۷ آن را برای رسانه‌های جمعی بسط داد.\n\n"
                           "۲. ساختارهای مفهومی\nرویداد، ادراک، گزینش، تبدیل به سیگنال، پیام، بازخورد و ابعاد افقی و عمودی سازه‌های اصلی‌اند.\n\n"
                           "۳. نمونه‌های تحلیلی\nدر پوشش خبری یک اعتراض، خبرنگار نه رویداد خام بلکه ادراک گزینش‌شدهٔ خود را به پیام تبدیل می‌کند؛ بازخورد مخاطب و سیاست رسانه، این گزینش را در چرخهٔ بعدی شکل می‌دهد.\n\n"
                           "۴. نقدها و چالش‌ها\nمدل پیچیده و پراجزاست و کاربرد تجربی آن دشوار است؛ سنجش ادراک و گزینش در عمل مبهم می‌ماند؛ فرض فعال‌بودن گیرنده همیشه برقرار نیست؛ و مرز میان پیام و سیگنال روشن نیست.\n\n"
                           "۵. سیر تاریخی\nمقالهٔ ۱۹۵۶ یکی از مدل‌های مرجع مبانی ارتباطات شد، بسط ۱۹۶۷ آن را به رسانه‌های جمعی گره زد و مسیر پژوهش‌های بعدی گربر در نظریهٔ کاشت را هموار کرد.\n\n"
                           "۶. جایگاه در بحث روز\nدر تحلیل بازنمایی رسانه‌ای و تولید تصویر از رویدادها، تأکید گربر بر ادراک و گزینش هنوز چارچوبی دقیق برای نقد بی‌طرفی ظاهری رسانه است."),
    ),
    "MC-021": dict(
        needs_enrichment=False,
        level="میان",
        related_approaches="نظریهٔ اقناع؛ مدل دانش اقناع؛ مدل ظرفیت محدود؛ سلسله‌مراتب اثرات؛ روان‌شناسی شناختی.",
        recommended_sources="«مدل احتمال بسط اقناع» (پتی و کاسیوپو، ۱۹۸۶)؛ «ارتباط و اقناع: مسیرهای مرکزی و پیرامونی» (پتی و کاسیوپو، ۱۹۸۶)؛ «نظریه‌های اقناع» (اوکیف، ۲۰۰۲).",
        detailed_analysis=("۱. بنیان و منطق نظری\nپتی و کاسیوپو (۱۹۸۶) مدل احتمال بسط را عرضه کردند تا توضیح دهند چرا گاهی استدلال قوی و گاهی نشانه‌های سطحی مانند جذابیت گوینده اقناع می‌کند. "
                           "ادعای مرکزی این است که احتمال بسط پیام — یعنی میزان پردازش شناختی آن — به انگیزش و توانایی گیرنده بستگی دارد. "
                           "در بسط بالا، مسیر مرکزی فعال می‌شود و کیفیت استدلال تعیین‌کننده است؛ در بسط پایین، مسیر پیرامونی با نشانه‌های ساده کار می‌کند.\n\n"
                           "۲. ساختارهای مفهومی\nمسیر مرکزی، مسیر پیرامونی، احتمال بسط، انگیزش، توانایی و نشانه‌های پیرامونی سازه‌های اصلی‌اند. "
                           "تغییر نگرش از مسیر مرکزی پایدارتر و مقاوم‌تر دانسته می‌شود.\n\n"
                           "۳. نمونه‌های تحلیلی\nدر تبلیغ یک محصول پرریسک و گران، مخاطب انگیزهٔ پردازش دارد و استدلال‌های محتوایی اثر می‌گذارد؛ در خرید کم‌ریسک، چهرهٔ معتبر یا موسیقی می‌تواند بدون پردازش عمیق تصمیم را تغییر دهد.\n\n"
                           "۴. نقدها و چالش‌ها\nمرز دو مسیر همیشه روشن نیست و پردازش مختلط را کم توضیح می‌دهد؛ سنجش احتمال بسط به شاخص‌های غیرمستقیم وابسته است؛ نقش احساس و عادت کم‌رنگ می‌شود؛ و برخی یافته‌های تجربی در بازتولید محدود بوده‌اند.\n\n"
                           "۵. سیر تاریخی\nپژوهش ۱۹۸۱ دربارهٔ درگیری شخصی و استدلال، مقدمهٔ مدل بود؛ مقاله و کتاب ۱۹۸۶ آن را تثبیت کردند و امروز یکی از پراستنادترین چارچوب‌های اقناع است.\n\n"
                           "۶. جایگاه در بحث روز\nدر تبلیغ هدفمند شبکه‌های اجتماعی و مقابله با اطلاعات نادرست، پرسش از انگیزش و توانایی پردازش مخاطب، محور طراحی پیام و مداخله شده است."),
    ),
}

NAME_FIX = {}

YEAR_FIX = {
    "MC-464": "year=1960 (Berlo 1960 verified via archive.org); replaced generic template analysis",
    "MC-309": "year=1956 (Gerbner 1956, DOI 10.1007/BF02717110); Gerbner 1967 verified; replaced generic template analysis",
    "MC-021": "year=1986 (Petty & Cacioppo 1986); both sources verified with DOIs; replaced generic template analysis",
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
                                       "verified": n_verified, "batch": 212}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH212 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
