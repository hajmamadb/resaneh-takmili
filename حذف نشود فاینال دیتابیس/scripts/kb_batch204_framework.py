# -*- coding: utf-8 -*-
"""Batch 204: MC-078, MC-199, MC-481, MC-582, MC-598 (FRAMEWORK)."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch204-20261117"
NOW = "2026-11-17 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch204.json"

S = {
    "MC-078": [
        dict(kind="BOOK",
             title_en="Experimental and Quasi-Experimental Designs for Research",
             title_fa="طرح‌های آزمایشی و شبه‌آزمایشی برای پژوهش",
             authors="Donald T. Campbell; Julian C. Stanley", year=1963,
             publisher="Rand McNally",
             doi=None,
             url=None,
             language="en", isbn=None,
             citation="Campbell, D. T., & Stanley, J. C. (1963). Experimental and Quasi-Experimental Designs for Research. Chicago: Rand McNally.",
             locator="chs. 1-5",
             locator_type="CHAPTER",
             supports="internal and external validity and threats in experimental and quasi-experimental designs",
             verified=True),
        dict(kind="BOOK",
             title_en="Quasi-Experimentation: Design and Analysis Issues for Field Settings",
             title_fa="شبه‌آزمایش: مسائل طرح و تحلیل در موقعیت‌های میدانی",
             authors="Thomas D. Cook; Donald T. Campbell", year=1979,
             publisher="Houghton Mifflin",
             doi=None,
             url="https://archive.org/details/quasiexperimenta00cook",
             language="en", isbn=None,
             citation="Cook, T. D., & Campbell, D. T. (1979). Quasi-Experimentation: Design and Analysis Issues for Field Settings. Boston: Houghton Mifflin.",
             locator="chs. 1-2",
             locator_type="CHAPTER",
             supports="expanded validity typology including statistical conclusion and construct validity",
             verified=True),
    ],
    "MC-199": [
        dict(kind="REPORT",
             title_en="Information Disorder: Toward an Interdisciplinary Framework for Research and Policy Making",
             title_fa="اختلال اطلاعاتی: به‌سوی چارچوبی میان‌رشته‌ای برای پژوهش و سیاست‌گذاری",
             authors="Claire Wardle; Hossein Derakhshan", year=2017,
             publisher="Council of Europe",
             doi=None,
             url="https://shorensteincenter.org/wp-content/uploads/2017/10/Information-Disorder-Toward-an-interdisciplinary-framework.pdf",
             language="en", isbn=None,
             citation="Wardle, C., & Derakhshan, H. (2017). Information Disorder: Toward an Interdisciplinary Framework for Research and Policy Making. Strasbourg: Council of Europe.",
             locator="pp. 1-107",
             locator_type="PAGE",
             supports="three-part typology of misinformation, disinformation and malinformation across phases and agents",
             verified=True),
        dict(kind="REPORT",
             title_en="Information Disorder: The Essential Glossary",
             title_fa="اختلال اطلاعاتی: واژه‌نامهٔ ضروری",
             authors="Claire Wardle", year=2018,
             publisher="Shorenstein Center, Harvard Kennedy School",
             doi=None,
             url=None,
             language="en", isbn=None,
             citation="Wardle, C. (2018). Information Disorder: The Essential Glossary. Cambridge, MA: Shorenstein Center on Media, Politics and Public Policy, Harvard Kennedy School.",
             locator="glossary",
             locator_type="SECTION",
             supports="operational definitions distinguishing misinformation, disinformation and malinformation",
             verified=True),
    ],
    "MC-481": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="On a New List of Categories",
             title_fa="دربارهٔ فهرست تازه‌ای از مقولات",
             authors="Charles S. Peirce", year=1867,
             publisher="Proceedings of the American Academy of Arts and Sciences",
             doi=None,
             url=None,
             language="en", isbn=None,
             citation="Peirce, C. S. (1867). On a new list of categories. Proceedings of the American Academy of Arts and Sciences, 7, 287-298.",
             locator="7, 287-298",
             locator_type="PAGE",
             supports="early formulation of the categories underlying the triadic sign",
             verified=True),
        dict(kind="BOOK",
             title_en="Collected Papers of Charles Sanders Peirce",
             title_fa="مقالات گردآوری‌شدهٔ چارلز سندرس پیرس",
             authors="Charles S. Peirce", year=1931,
             publisher="Harvard University Press",
             doi=None,
             url="https://www.hup.harvard.edu/books/9780674138001",
             language="en", isbn=None,
             citation="Peirce, C. S. (1931-1958). Collected Papers of Charles Sanders Peirce (Vols. 1-8). Cambridge, MA: Harvard University Press.",
             locator="vols. 1-8",
             locator_type="BOOK",
             supports="systematic account of sign, object, interpretant and semiosis",
             verified=True),
    ],
    "MC-582": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="The TARES Test: Five Principles for Ethical Persuasion",
             title_fa="آزمون تارِس: پنج اصل برای اقناع اخلاقی",
             authors="Sherry Baker; David L. Martinson", year=2001,
             publisher="Journal of Mass Media Ethics",
             doi=None,
             url="http://www.communicationcache.com/uploads/1/0/8/8/10887248/the_tares_test-_five_principles_for_ethical_persuasion.pdf",
             language="en", isbn=None,
             citation="Baker, S., & Martinson, D. L. (2001). The TARES test: Five principles for ethical persuasion. Journal of Mass Media Ethics, 16(2-3), 148-175.",
             locator="16(2-3), 148-175",
             locator_type="PAGE",
             supports="five-part ethical test of persuasive communication",
             verified=True),
        dict(kind="BOOK",
             title_en="Ethics in Human Communication",
             title_fa="اخلاق در ارتباطات انسانی",
             authors="Richard L. Johannesen", year=2002,
             publisher="Waveland Press",
             doi=None,
             url="https://archive.org/details/ethicsinhumancom0000joha_i0u6",
             language="en", isbn=None,
             citation="Johannesen, R. L. (2002). Ethics in Human Communication (5th ed.). Prospect Heights, IL: Waveland Press.",
             locator="chs. 1-4",
             locator_type="CHAPTER",
             supports="ethical perspectives and standards for communication practice",
             verified=True),
    ],
    "MC-598": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="A Rhetorical Approach to Zones of Meaning and Organizational Prerogatives",
             title_fa="رویکردی بلاغی به پهنه‌های معنا و اختیارات سازمانی",
             authors="Robert L. Heath", year=1993,
             publisher="Public Relations Review",
             doi=None,
             url="https://www.sciencedirect.com/science/article/pii/036381119390004V",
             language="en", isbn=None,
             citation="Heath, R. L. (1993). A rhetorical approach to zones of meaning and organizational prerogatives. Public Relations Review, 19(2), 141-155.",
             locator="19(2), 141-155",
             locator_type="PAGE",
             supports="public relations as rhetorical negotiation of zones of meaning",
             verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="On Barnyard Scrambles: Toward a Rhetoric of Public Relations",
             title_fa="دربارهٔ کشمکش‌های حیاط مزرعه: به‌سوی بلاغتی برای روابط عمومی",
             authors="Øyvind Ihlen", year=2011,
             publisher="Management Communication Quarterly",
             doi="10.1177/0893318911409533",
             url="https://journals.sagepub.com/doi/10.1177/0893318911409533",
             language="en", isbn=None,
             citation="Ihlen, Ø. (2011). On barnyard scrambles: Toward a rhetoric of public relations. Management Communication Quarterly, 25(3), 455-473. https://doi.org/10.1177/0893318911409533",
             locator="25(3), 455-473",
             locator_type="PAGE",
             supports="rhetorical framework for public relations as strategic meaning making",
             verified=True),
    ],
}

ENRICH = {
    "MC-078": dict(
        needs_enrichment=False,
        level="روش‌شناختی",
        key_concepts=["اعتبار درونی", "اعتبار بیرونی", "تهدید اعتبار", "گمارش تصادفی",
                      "طرح شبه‌آزمایشی", "اعتبار سازه", "اعتبار آماری"],
        principles=["اعتبار درونی، امکان استنتاج علّی را می‌سنجد.", "اعتبار بیرونی، تعمیم‌پذیری یافته به موقعیت‌های دیگر است.",
                    "گمارش تصادفی، تهدیدهای درونی را کاهش می‌دهد اما تعمیم‌پذیری را تضمین نمی‌کند.",
                    "طرح شبه‌آزمایشی، در نبود تصادفی‌سازی نیازمند گروه کنترل و پیش‌آزمون است.",
                    "تهدیدهای اعتبار باید پیش از اجرا فهرست و مهار شوند.",
                    "اعتبار سازه و آماری نیز بخشی از ارزیابی طرح‌اند.", "تعمیم نتیجه به مخاطب، رسانه و زمان دیگر نیازمند شواهد است."],
        constructs=("• اعتبار درونی: اطمینان از اینکه تغییر مشاهده‌شده ناشی از مداخله است، نه عوامل دیگر.\n"
                    "• اعتبار بیرونی: تعمیم‌پذیری نتیجه به جمعیت‌ها، موقعیت‌ها و زمان‌های دیگر.\n"
                    "• تهدیدهای اعتبار: رویداد هم‌زمان، بلوغ، آزمون، ابزار، انتخاب و ریزش نمونه.\n"
                    "• طرح شبه‌آزمایشی: طرح بدون گمارش تصادفی که با گروه کنترل و پیش‌آزمون، استنتاج علّی را ممکن می‌کند."),
        related_approaches="روش کمّی؛ روش کیفی؛ روش ترکیبی؛ تحلیل محتوا؛ فراتحلیل؛ طرح آزمایشی میدانی.",
        recommended_sources="«طرح‌های آزمایشی و شبه‌آزمایشی برای پژوهش» (کمپبل و استنلی، ۱۹۶۳)؛ «شبه‌آزمایش» (کوک و کمپبل، ۱۹۷۹)؛ «طرح‌های آزمایشی و شبه‌آزمایشی» (شادیش، کوک و کمپبل، ۲۰۰۲).",
    ),
    "MC-199": dict(
        needs_enrichment=False,
        key_concepts=["اطلاعات نادرست", "اطلاعات بدخواهانه", "اطلاعات گمراه‌کننده", "زمینهٔ نادرست",
                      "محتوای دستکاری‌شده", "عاملان و مراحل انتشار"],
        principles=["اختلال اطلاعاتی سه‌گانه است: نادرست، بدخواهانه و گمراه‌کننده.",
                    "قصد عامل انتشار، مرز میان اطلاعات نادرست و بدخواهانه را می‌سازد.",
                    "محتوای اصیل می‌تواند با زمینهٔ نادرست گمراه‌کننده شود.",
                    "اختلال در سه مرحلهٔ ساخت، تولید و توزیع تحلیل می‌شود.",
                    "بازیگران دولتی، رسانه‌ای و کاربری نقش متفاوتی دارند.",
                    "راه‌حل تنها فناورانه نیست و سواد رسانه‌ای و پاسخ‌گویی نهادی را می‌طلبد."],
        constructs=("• اطلاعات نادرست: محتوای غلط بدون قصد آسیب.\n"
                    "• اطلاعات بدخواهانه: محتوای غلط با قصد فریب و آسیب.\n"
                    "• اطلاعات گمراه‌کننده: محتوای درست با قصد آسیب یا زمینهٔ فریب‌دهنده.\n"
                    "• سه مرحله: ساخت، تولید و توزیع محتوای مسئله‌دار."),
        related_approaches="روزنامه‌نگاری و راستی‌آزمایی؛ سواد رسانه‌ای؛ مطالعات تبلیغات؛ ارتباطات سیاسی؛ حاکمیت پلتفرم.",
        recommended_sources="«اختلال اطلاعاتی: چارچوبی میان‌رشته‌ای» (واردل و درخشان، ۲۰۱۷)؛ «واژه‌نامهٔ اختلال اطلاعاتی» (واردل، ۲۰۱۸)؛ پژوهش‌های راستی‌آزمایی و سواد رسانه‌ای.",
    ),
    "MC-481": dict(
        needs_enrichment=False,
        level="نظری",
        key_concepts=["نشانه", "موضوع", "تفسیرگر", "سه‌گانهٔ نشانه‌ای", "شمایل، نمایه و نماد", "فرایند نشانه‌ای"],
        principles=["نشانه هرگز به‌تنهایی معنا ندارد؛ سه‌گانهٔ نشانه، موضوع و تفسیرگر لازم است.",
                    "معنا در فرایند نشانه‌ای و تفسیر پیوسته ساخته می‌شود، نه در شیء.",
                    "شمایل با شباهت، نمایه با پیوند علّی و نماد با قرارداد عمل می‌کند.",
                    "تفسیرگر خود نشانهٔ تازه‌ای است و فرایند را ادامه می‌دهد.",
                    "نشانه‌شناسی پیرس با نشانه‌شناسی دوسویهٔ سوسور متفاوت است.",
                    "تحلیل رسانه می‌تواند نشانه را در سه سطح شمایلی، نمایه‌ای و نمادین بخواند."],
        constructs=("• نشانه: چیزی که چیزی دیگر را برای کسی بازنمایی می‌کند.\n"
                    "• موضوع: آنچه نشانه به آن ارجاع می‌دهد.\n"
                    "• تفسیرگر: معنایی که در ذهن مفسر ساخته می‌شود.\n"
                    "• سه‌گانهٔ نشانه‌ای: نسبت ضروری میان سه رکن بالا.\n"
                    "• فرایند نشانه‌ای: زنجیرهٔ تفسیرهای پیوسته."),
        related_approaches="نشانه‌شناسی؛ تحلیل گفتمان؛ تحلیل روایت؛ مطالعات بصری؛ نشانه‌شناسی اجتماعی.",
        recommended_sources="«دربارهٔ فهرست تازه‌ای از مقولات» (پیرس، ۱۸۶۷)؛ «مقالات گردآوری‌شدهٔ پیرس» (۱۹۳۱ تا ۱۹۵۸)؛ «نشانه‌شناسی: مبانی» (چندلر، ۲۰۰۷).",
    ),
    "MC-582": dict(
        needs_enrichment=False,
        key_concepts=["راست‌گویی", "اصالت", "احترام", "انصاف", "مسئولیت اجتماعی"],
        principles=["اقناع اخلاقی باید راستگو و مستند باشد.", "پیام باید با هویت و ارزش‌های فرستنده اصالت داشته باشد.",
                    "مخاطب باید به‌عنوان هدف اخلاقی محترم شمرده شود، نه ابزار.", "اقناع نباید اطلاعات لازم برای تصمیم را پنهان کند.",
                    "فرستنده در قبال پیامدهای اجتماعی پیام مسئول است.", "آزمون اخلاقی باید پیش از انتشار، نه پس از آن، اجرا شود.",
                    "معیارهای اخلاقی، تبلیغ تجاری و اقناع سیاسی را یکسان در بر می‌گیرد."],
        constructs=("• راست‌گویی: صدق محتوای پیام.\n"
                    "• اصالت: هم‌خوانی پیام با ارزش‌های واقعی فرستنده.\n"
                    "• احترام: به‌رسمیت شناختن مخاطب و حق انتخاب او.\n"
                    "• انصاف: توزیع برابر منافع و دسترسی به اطلاعات.\n"
                    "• مسئولیت اجتماعی: پاسخ‌گویی در قبال پیامدهای عمومی پیام."),
        related_approaches="اخلاق ارتباطات؛ اقناع و تغییر نگرش؛ ارتباطات بازاریابی؛ روابط عمومی؛ سواد رسانه‌ای.",
        recommended_sources="«آزمون تارِس: پنج اصل برای اقناع اخلاقی» (بیکر و مارتینسون، ۲۰۰۱)؛ «اخلاق در ارتباطات انسانی» (یوهانسن، ۲۰۰۲)؛ «پویایی اقناع» (پرلاف، ۲۰۰۳).",
    ),
    "MC-598": dict(
        needs_enrichment=False,
        title_fa="چارچوب «روابط عمومی به‌عنوان مدیریت معنا»",
        constructs=("• پهنهٔ معنا: فضای مشترک تفسیر که سازمان و عمومی‌ها در آن معنا می‌سازند.\n"
                    "• بازار معنا: رقابت روایت‌ها و تعریف‌ها در فضای عمومی.\n"
                    "• پاسخ‌گویی بلاغی: تعهد سازمان به توضیح و دفاع از تصمیم‌ها.\n"
                    "• چارچوب‌بندی سازمانی: تلاش سازمان برای تعریف موضوع و مرز مسئولیت.\n"
                    "• گفت‌وگوی عمومی: فرایند دوسویهٔ مذاکرهٔ معنا با ذی‌نفعان."),
        core_logic="روابط عمومی نه انتقال پیام، بلکه مدیریت معناست: سازمان در پهنهٔ معنا و بازار رقابتی روایت‌ها، با بلاغت، چارچوب‌بندی و گفت‌وگو می‌کوشد تعریف خود و مسئولیت‌هایش را در ذهن عمومی‌ها تثبیت کند.",
        detailed_analysis=("۱. بنیان و منطق نظری\nهیث (۱۹۹۳) روابط عمومی را کنشی بلاغی می‌داند که در پهنه‌های معنا رخ می‌دهد. "
                           "سازمان و عمومی‌ها در فضایی از تعریف‌های رقیب، دربارهٔ معنا، مسئولیت و مشروعیت مذاکره می‌کنند و روابط عمومی ابزار مدیریت این مذاکره است. "
                           "در این چارچوب، پیام فقط انتقال اطلاعات نیست؛ کنشی است که مرز مسئولیت سازمان را تعیین می‌کند و پاسخ‌گویی بلاغی می‌سازد. "
                           "ایهلن (۲۰۱۱) این دیدگاه را با تأکید بر بلاغت به‌عنوان هستهٔ روابط عمومی گسترش داد و نشان داد که سازمان‌ها در بازار معنا با روایت‌های دیگر رقابت می‌کنند.\n\n"
                           "۲. کاربرد و نقد\nاین چارچوب در تحلیل بحران، مسئولیت اجتماعی سازمان و روابط با ذی‌نفعان کاربرد دارد و پژوهشگر را از پرسش «چه پیامی فرستاده شد؟» به پرسش «چه معنایی ساخته و به رسمیت شناخته شد؟» می‌برد. "
                           "نقد اصلی، خطر تقلیل روابط عمومی به مدیریت تصویر و کم‌توجهی به نابرابری قدرت در گفت‌وگوست؛ پاسخ به این نقد، تأکید بر پاسخ‌گویی و گفت‌وگوی واقعی با ذی‌نفعان است."),
        related_approaches="بلاغت سازمانی؛ روابط عمومی راهبردی؛ مدیریت بحران؛ مسئولیت اجتماعی سازمان؛ نظریهٔ ذی‌نفعان.",
        recommended_sources="«رویکردی بلاغی به پهنه‌های معنا» (هیث، ۱۹۹۳)؛ «به‌سوی بلاغتی برای روابط عمومی» (ایهلن، ۲۰۱۱)؛ «راهنمای روابط عمومی» (هیث، ۲۰۰۱).",
    ),
}

NAME_FIX = {}

YEAR_FIX = {
    "MC-078": "year=1963 (Campbell & Stanley 1963); Cook & Campbell 1979 verified; removed Latin glosses and generic-methods recommendations",
    "MC-199": "year=2017 (Wardle & Derakhshan 2017); Wardle 2018 glossary verified (single author); removed Latin glosses and newsroom-template recommendations",
    "MC-481": "year=1867 (Peirce 1867); Collected Papers 1931-1958 verified; replaced Barthes-template constructs and Latin glosses",
    "MC-582": "year=2001 (Baker & Martinson 2001); pages corrected to 16(2-3), 148-175; Johannesen 2002 verified; removed persuasion-template fields",
    "MC-598": "year=1993 (Heath 1993); Ihlen 2011 verified (25(3), 455-473); removed media-economics-template fields and garbled recommendations",
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
                                       "verified": n_verified, "batch": 204}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH204 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
