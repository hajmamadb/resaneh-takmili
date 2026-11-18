# -*- coding: utf-8 -*-
"""Batch 206: MC-028, MC-069, MC-081, MC-082, MC-107 (MODEL)."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch206-20261117"
NOW = "2026-11-17 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch206.json"

S = {
    "MC-028": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Stages and Processes of Self-Change of Smoking: Toward an Integrative Model of Change",
             title_fa="مراحل و فرایندهای خودتغییری سیگار: به‌سوی مدلی یکپارچه از تغییر",
             authors="James O. Prochaska; Carlo C. DiClemente", year=1983,
             publisher="Journal of Consulting and Clinical Psychology",
             doi=None,
             url=None,
             language="en", isbn=None,
             citation="Prochaska, J. O., & DiClemente, C. C. (1983). Stages and processes of self-change of smoking: Toward an integrative model of change. Journal of Consulting and Clinical Psychology, 51(3), 390-395.",
             locator="51(3), 390-395",
             locator_type="PAGE",
             supports="stages and processes of change in self-quitting smoking",
             verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="In Search of How People Change: Applications to Addictive Behaviors",
             title_fa="در جست‌وجوی چگونگی تغییر افراد: کاربردها در رفتارهای اعتیادی",
             authors="James O. Prochaska; Carlo C. DiClemente; John C. Norcross", year=1992,
             publisher="American Psychologist",
             doi=None,
             url="https://pubmed.ncbi.nlm.nih.gov/1329589/",
             language="en", isbn=None,
             citation="Prochaska, J. O., DiClemente, C. C., & Norcross, J. C. (1992). In search of how people change: Applications to addictive behaviors. American Psychologist, 47(9), 1102-1114.",
             locator="47(9), 1102-1114",
             locator_type="PAGE",
             supports="stage-matched interventions and relapse in the change cycle",
             verified=True),
    ],
    "MC-069": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Balanced Scorecard: Measures That Drive Performance",
             title_fa="کارت امتیازی متوازن: سنجه‌هایی که عملکرد را هدایت می‌کنند",
             authors="Robert S. Kaplan; David P. Norton", year=1992,
             publisher="Harvard Business Review",
             doi=None,
             url="https://hbr.org/1992/01/the-balanced-scorecard-measures-that-drive-performance-2",
             language="en", isbn=None,
             citation="Kaplan, R. S., & Norton, D. P. (1992). The balanced scorecard: Measures that drive performance. Harvard Business Review, 70(1), 71-79.",
             locator="70(1), 71-79",
             locator_type="PAGE",
             supports="four-perspective performance measurement system",
             verified=True),
        dict(kind="BOOK",
             title_en="The Balanced Scorecard: Translating Strategy into Action",
             title_fa="کارت امتیازی متوازن: ترجمهٔ راهبرد به کنش",
             authors="Robert S. Kaplan; David P. Norton", year=1996,
             publisher="Harvard Business School Press",
             doi=None,
             url="https://www.hbs.edu/faculty/Pages/item.aspx?num=8831",
             language="en", isbn=None,
             citation="Kaplan, R. S., & Norton, D. P. (1996). The Balanced Scorecard: Translating Strategy into Action. Boston: Harvard Business School Press.",
             locator="book",
             locator_type="BOOK",
             supports="causal chain from learning and growth to financial outcomes",
             verified=True),
    ],
    "MC-081": [
        dict(kind="BOOK",
             title_en="The Structure and Function of Communication in Society",
             title_fa="ساختار و کارکرد ارتباطات در جامعه",
             authors="Harold D. Lasswell", year=1948,
             publisher="Institute for Religious and Social Studies",
             doi=None,
             url=None,
             language="en", isbn=None,
             citation="Lasswell, H. D. (1948). The structure and function of communication in society. In L. Bryson (Ed.), The Communication of Ideas (pp. 37-51). New York: Institute for Religious and Social Studies.",
             locator="pp. 37-51",
             locator_type="PAGE",
             supports="five-component model and three social functions of communication",
             verified=True),
        dict(kind="BOOK",
             title_en="Propaganda Technique in the World War",
             title_fa="فن پروپاگاندا در جنگ جهانی",
             authors="Harold D. Lasswell", year=1927,
             publisher="Alfred A. Knopf",
             doi=None,
             url="https://archive.org/details/dli.ernet.233727",
             language="en", isbn=None,
             citation="Lasswell, H. D. (1927). Propaganda Technique in the World War. New York: Alfred A. Knopf.",
             locator="book",
             locator_type="BOOK",
             supports="propaganda research background of the model",
             verified=True),
    ],
    "MC-082": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="A Mathematical Theory of Communication",
             title_fa="نظریهٔ ریاضی ارتباطات",
             authors="Claude E. Shannon", year=1948,
             publisher="Bell System Technical Journal",
             doi=None,
             url="https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf",
             language="en", isbn=None,
             citation="Shannon, C. E. (1948). A mathematical theory of communication. Bell System Technical Journal, 27(3), 379-423; 27(4), 623-656.",
             locator="27(3), 379-423",
             locator_type="PAGE",
             supports="entropy, channel capacity and the technical model of transmission",
             verified=True),
        dict(kind="BOOK",
             title_en="The Mathematical Theory of Communication",
             title_fa="نظریهٔ ریاضی ارتباطات",
             authors="Claude E. Shannon; Warren Weaver", year=1949,
             publisher="University of Illinois Press",
             doi=None,
             url=None,
             language="en", isbn=None,
             citation="Shannon, C. E., & Weaver, W. (1949). The Mathematical Theory of Communication. Urbana: University of Illinois Press.",
             locator="book",
             locator_type="BOOK",
             supports="three levels of communication problems: technical, semantic, effectiveness",
             verified=True),
    ],
    "MC-107": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Limited Capacity Model of Mediated Message Processing",
             title_fa="مدل ظرفیت محدود پردازش پیام رسانه‌ای",
             authors="Annie Lang", year=2000,
             publisher="Journal of Communication",
             doi=None,
             url=None,
             language="en", isbn=None,
             citation="Lang, A. (2000). The limited capacity model of mediated message processing. Journal of Communication, 50(1), 46-70.",
             locator="50(1), 46-70",
             locator_type="PAGE",
             supports="encoding, storage and retrieval drawing on shared cognitive resources",
             verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Using the Limited Capacity Model of Motivated Mediated Message Processing to Design Effective Cancer Communication Messages",
             title_fa="کاربرد مدل ظرفیت محدود پردازش پیام رسانه‌ای انگیزشی در طراحی پیام‌های ارتباطی سرطان",
             authors="Annie Lang", year=2006,
             publisher="Journal of Communication",
             doi="10.1111/j.1460-2466.2006.00283.x",
             url="https://academic.oup.com/joc/article-abstract/56/suppl_1/S57/4102578",
             language="en", isbn=None,
             citation="Lang, A. (2006). Using the limited capacity model of motivated mediated message processing to design effective cancer communication messages. Journal of Communication, 56(S1), S57-S80. https://doi.org/10.1111/j.1460-2466.2006.00283.x",
             locator="56(S1), S57-S80",
             locator_type="PAGE",
             supports="applied design implications of LC4MP for health messages",
             verified=True),
    ],
}

ENRICH = {
    "MC-028": dict(
        needs_enrichment=False,
        constructs=("• مراحل تغییر: پیش‌تفکر، تفکر، آماده‌سازی، عمل، حفظ و پایان.\n"
                    "• فرایندهای تغییر: راهبردهای شناختی و رفتاری متناظر با هر مرحله.\n"
                    "• تعادل تصمیم: سنجش سود و زیان تغییر.\n"
                    "• خودکارآمدی: اطمینان به توان حفظ رفتار تازه.\n"
                    "• بازگشت: چرخهٔ طبیعی بازگشت و شروع دوباره."),
        related_approaches="ارتباطات سلامت؛ اقناع و تغییر نگرش؛ بازاریابی اجتماعی؛ مدل باور سلامت؛ طراحی مداخلهٔ رفتاری.",
        recommended_sources="«مراحل و فرایندهای خودتغییری سیگار» (پروچاسکا و دی‌کلمنته، ۱۹۸۳)؛ «در جست‌وجوی چگونگی تغییر افراد» (پروچاسکا، دی‌کلمنته و نورکراس، ۱۹۹۲)؛ «مدل فرانظری تغییر رفتار سلامت» (پروچاسکا و ولیسر، ۱۹۹۷).",
        detailed_analysis=("۱. بنیان و منطق نظری\nمدل فرانظری، تغییر رفتار را مسیری مرحله‌ای می‌داند: پیش‌تفکر، تفکر، آماده‌سازی، عمل، حفظ و پایان. "
                           "پروچاسکا و دی‌کلمنته (۱۹۸۳) با مطالعهٔ خودتغییری سیگار نشان دادند افراد در هر مرحله فرایندهای شناختی و رفتاری متفاوتی به‌کار می‌گیرند و مداخلهٔ یکسان برای همه، بی‌اثر یا مقاومت‌آفرین است. "
                           "تعادل تصمیم، خودکارآمدی و وسوسه، حرکت میان مراحل را توضیح می‌دهند و بازگشت بخشی از چرخه است، نه شکست نهایی. "
                           "مقالهٔ ۱۹۹۲ این منطق را برای رفتارهای اعتیادی و برنامه‌های مرحله‌محور بسط داد.\n\n"
                           "۲. کاربرد و نقد\nاین مدل در کمپین‌های سلامت و ارتباطات اقناعی به‌کار می‌رود و به طراح پیام می‌آموزد پیش از تولید محتوا، مرحلهٔ آمادگی مخاطب را بسنجد. "
                           "نقد اصلی، دلبخواهی بودن مرز مراحل، ساده‌سازی حرکت خطی و شواهد ناهمگون دربارهٔ کارایی مداخلات مرحله‌محور است."),
    ),
    "MC-069": dict(
        needs_enrichment=False,
        related_approaches="مدیریت راهبردی؛ سنجش عملکرد؛ مدیریت رسانه؛ کنترل مدیریت؛ راهبرد سازمانی.",
        recommended_sources="«کارت امتیازی متوازن: سنجه‌هایی که عملکرد را هدایت می‌کنند» (کپلن و نورتون، ۱۹۹۲)؛ «کارت امتیازی متوازن: ترجمهٔ راهبرد به کنش» (کپلن و نورتون، ۱۹۹۶)؛ «سازمان راهبرد‌محور» (کپلن و نورتون، ۲۰۰۱).",
        detailed_analysis=("۱. بنیان و منطق نظری\nکارت امتیازی متوازن در سال ۱۹۹۲ برای رفع کاستی سنجه‌های مالی صرف ارائه شد. "
                           "کپلن و نورتون چهار دیدگاه مالی، مشتری، فرایندهای داخلی و یادگیری و رشد را پیشنهاد کردند و نشان دادند که این دیدگاه‌ها با زنجیرهٔ علّی به هم وصل‌اند: سرمایه‌گذاری در یادگیری، فرایند را بهبود می‌دهد، رضایت مشتری را می‌سازد و در نهایت به نتیجهٔ مالی می‌رسد. "
                           "سنجه‌های پیشرو و پسرو در هر دیدگاه، تصویری متوازن از عملکرد و اجرای راهبرد فراهم می‌کنند.\n\n"
                           "۲. کاربرد و نقد\nدر سازمان‌های رسانه‌ای، این مدل برای پیوند راهبرد محتوایی با شاخص‌های مخاطب، فرایند تحریریه و ظرفیت یادگیری به‌کار می‌رود. "
                           "نقد اصلی، خطر تبدیل کارت به فهرست سنجه و بوروکراسی، فرض علّیت خطی میان دیدگاه‌ها و دشواری سنجش دارایی‌های نامشهود است."),
    ),
    "MC-081": dict(
        needs_enrichment=False,
        level="کلان",
        constructs="منبع؛ پیام؛ کانال؛ مخاطب؛ اثر؛ نظارت؛ همبستگی؛ انتقال میراث؛ سرگرمی.",
        related_approaches="مدل ارتباطی لاسول؛ نظریهٔ اطلاعات شانون-ویور؛ مدل تعاملی ارتباط؛ تحلیل کارکردگرای رسانه؛ پژوهش پروپاگاندا.",
        recommended_sources="«ساختار و کارکرد ارتباطات در جامعه» (لاسول، ۱۹۴۸)؛ «فن پروپاگاندا در جنگ جهانی» (لاسول، ۱۹۲۷)؛ «نظریه‌های ارتباطات جمعی» (مک‌کوایل، ۱۹۸۳).",
        detailed_analysis=("۱. بنیان و منطق نظری\nمدل لاسول ارتباط را با پنج پرسش صورت‌بندی می‌کند: چه کسی، چه می‌گوید، از چه کانالی، به چه کسی و با چه اثری. "
                           "این پنج مؤلفه بعدها به فرستنده، پیام، کانال، گیرنده و اثر ترجمه شد و به چارچوب پایهٔ آموزش ارتباطات تبدیل شد. "
                           "لاسول سه کارکرد اجتماعی برای ارتباطات برمی‌شمارد: نظارت بر محیط، همبستگی اجزای جامعه در پاسخ به محیط و انتقال میراث اجتماعی؛ سرگرمی نیز بعدها به این فهرست افزوده شد. "
                           "ریشهٔ مدل در پژوهش پروپاگاندا و تجربهٔ جنگ جهانی اول است.\n\n"
                           "۲. کاربرد و نقد\nمدل لاسول برای آموزش، تحلیل خبر و بررسی کارکرد رسانه‌ها ابزار ساده و مؤثری است، اما خطی بودن آن، غفلت از بازخورد، معنا و زمینهٔ اجتماعی، و فرض اثری یک‌سویه از مهم‌ترین نقدهای وارد بر آن است."),
    ),
    "MC-082": dict(
        needs_enrichment=False,
        constructs="منبع اطلاعات؛ فرستنده؛ کانال؛ نویز؛ گیرنده؛ مقصد؛ آنتروپی؛ ظرفیت کانال؛ افزونگی.",
        related_approaches="مدل ارتباطی لاسول؛ نظریهٔ اطلاعات؛ مدل تعاملی ارتباط؛ مدل‌های انتقالی ارتباط؛ نظریهٔ رمزگذاری.",
        recommended_sources="«نظریهٔ ریاضی ارتباطات» (شانون، ۱۹۴۸)؛ «نظریهٔ ریاضی ارتباطات» (شانون و ویور، ۱۹۴۹)؛ «نظریه‌های ارتباطات جمعی» (مک‌کوایل، ۱۹۸۳).",
        detailed_analysis=("۱. بنیان و منطق نظری\nشانون (۱۹۴۸) در مقالهٔ مهندسی خود، ارتباط را مسئلهٔ انتقال سیگنال در کانال تعریف کرد و مفاهیم آنتروپی، افزونگی و ظرفیت کانال را معرفی کرد. "
                           "شانون و ویور (۱۹۴۹) با افزودن سه سطح فنی، معنایی و اثربخشی، مدل را به علوم ارتباطات آوردند: منبع، فرستنده، کانال، نویز، گیرنده و مقصد. "
                           "هدف مدل، بیشینه‌سازی وفاداری انتقال در برابر نویز است و نه توضیح معنا یا تعامل اجتماعی.\n\n"
                           "۲. کاربرد و نقد\nاین مدل در طراحی شبکه، فشرده‌سازی داده و آموزش مبانی ارتباطات اثرگذار بوده است. "
                           "نقد اصلی، خطی بودن، غفلت از بازخورد، معنا، زمینه و قدرت، و تقلیل ارتباط انسانی به انتقال اطلاعات است؛ با این حال، مفاهیم ظرفیت و افزونگی همچنان در تحلیل رسانه به‌کار می‌روند."),
    ),
    "MC-107": dict(
        needs_enrichment=False,
        constructs=("• ظرفیت محدود: منابع شناختی پردازش پیام محدودند.\n"
                    "• رمزگذاری، ذخیره‌سازی و بازیابی: سه فرایند رقیب بر منابع مشترک.\n"
                    "• انگیزه و محرک نوظهور: عوامل هدایت‌کنندهٔ تخصیص منابع.\n"
                    "• بار شناختی: تقاضای پردازش که با کمبود منابع، عملکرد را کاهش می‌دهد."),
        related_approaches="پردازش اطلاعات؛ نظریهٔ بار شناختی؛ پردازش انگیزشی؛ روان‌شناسی رسانه؛ ارتباطات سلامت.",
        recommended_sources="«مدل ظرفیت محدود پردازش پیام رسانه‌ای» (لانگ، ۲۰۰۰)؛ «کاربرد مدل ظرفیت محدود در طراحی پیام‌های سرطان» (لانگ، ۲۰۰۶)؛ پژوهش‌های بار شناختی و توجه رسانه‌ای.",
        detailed_analysis=("۱. بنیان و منطق نظری\nمدل ظرفیت محدود پردازش پیام رسانه‌ای (لانگ، ۲۰۰۰) بر این فرض استوار است که منابع شناختی انسان محدود است و سه فرایند رمزگذاری، ذخیره‌سازی و بازیابی بر همان منابع مشترک رقابت می‌کنند. "
                           "انگیزه و محرک‌های نوظهور پیام، تخصیص منابع را هدایت می‌کنند و اگر تقاضای پردازش از ظرفیت بیشتر شود، عملکرد پردازش کاهش می‌یابد. "
                           "مدل در سال ۲۰۰۶ برای طراحی پیام‌های ارتباطی سلامت به‌کار رفت و نشان داد ساختار پیام می‌تواند بار شناختی و در نتیجه یادگیری را تغییر دهد.\n\n"
                           "۲. کاربرد و نقد\nاین مدل در تحلیل تبلیغات، خبر تلویزیونی و پیام‌های سلامت کاربرد دارد و طراحان را به سنجش بار شناختی مخاطب وادار می‌کند. "
                           "نقد اصلی، دشواری سنجش مستقیم منابع و ساده‌سازی تفاوت‌های فردی است؛ با این حال، پیوند آن میان طراحی پیام و ظرفیت شناختی، همچنان پرثمر است."),
    ),
}

NAME_FIX = {}

YEAR_FIX = {
    "MC-028": "year=1983 (Prochaska & DiClemente 1983); 1992 verified; removed selective-exposure template fields",
    "MC-069": "year=1992 (Kaplan & Norton 1992); 1996 book verified; removed media-business template analysis and garbled recommendations",
    "MC-081": "year=1948 (Lasswell 1948); Lasswell 1927 verified; removed Latin glosses and thin recommendation",
    "MC-082": "year=1948 (Shannon 1948); Shannon & Weaver 1949 verified; removed Latin glosses and repaired recommendations",
    "MC-107": "year=2000 (Lang 2000); Lang 2006 verified (DOI 10.1111/j.1460-2466.2006.00283.x); replaced English-only recommendations and Latin glosses",
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
                                       "verified": n_verified, "batch": 206}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH206 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
