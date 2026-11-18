# -*- coding: utf-8 -*-
"""Batch 115: full documentation for MC-699, MC-701."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch115-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch115_theory.json"

S = {
    "MC-699": [
        dict(kind="BOOK",
             title_en="Beyond Agenda Setting: Information Subsidies and Public Policy",
             title_fa="فراتر از برجسته‌سازی: یارانه‌های اطلاعاتی و سیاست عمومی",
             authors="Gandy, O. H.", year=1982, publisher="Ablex",
             doi=None,
             url="https://archive.org/details/beyondagendasett00osca",
             language="en", isbn=None,
             citation="Gandy, O. H. (1982). Beyond agenda setting: Information subsidies and public policy. Ablex.",
             locator="work", locator_type="work",
             supports="information subsidies create structural dependence between news media and PR sources", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Investigating Relationships between Journalists and Public Relations Practitioners: Working Together to Set, Frame and Build the Public Agenda, 1991-2004",
             title_fa="بررسی رابطه روزنامه‌نگاران و کارگزاران روابط عمومی: همکاری برای تعیین، چارچوب‌بندی و ساختن دستور کار عمومی، ۱۹۹۱-۲۰۰۴",
             authors="Sallot, L. M.; Johnson, E. A.", year=2006,
             publisher="Public Relations Review",
             doi=None,
             url="https://www.sciencedirect.com/science/article/abs/pii/S0363811106000245",
             language="en", isbn=None,
             citation="Sallot, L. M., & Johnson, E. A. (2006). Investigating relationships between journalists and public relations practitioners: Working together to set, frame and build the public agenda, 1991-2004. Public Relations Review, 32(2), 151-159.",
             locator="32(2):151-159", locator_type="page_range",
             supports="synthesis of cooperation and competition in journalist-PR relations", verified=True),
    ],
    "MC-701": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Spin Doctors in the United States, Great Britain, and Germany: Metacommunication about Media Manipulation",
             title_fa="چرخش‌دهندگان در آمریکا، بریتانیا و آلمان: فراارتباطی درباره دستکاری رسانه",
             authors="Esser, F.; Reinemann, C.; Fan, D.", year=2001,
             publisher="The International Journal of Press/Politics",
             doi="10.1177/1081180X01006001003",
             url="https://journals.sagepub.com/doi/10.1177/1081180X01006001003",
             language="en", isbn=None,
             citation="Esser, F., Reinemann, C., & Fan, D. (2001). Spin doctors in the United States, Great Britain, and Germany: Metacommunication about media manipulation. The International Journal of Press/Politics, 6(1), 16-45.",
             locator="6(1):16-45", locator_type="page_range",
             supports="spin as metacommunication aiming at news criteria and media coverage", verified=True),
        dict(kind="BOOK",
             title_en="Spin Cycle: How the White House and the Media Manipulate the News",
             title_fa="چرخه چرخش: چگونه کاخ سفید و رسانه خبر را دستکاری می‌کنند",
             authors="Kurtz, H.", year=1997, publisher="Free Press",
             doi=None,
             url="https://www.simonandschuster.com/books/Spin-Cycle/Howard-Kurtz/9780684857152",
             language="en", isbn=None,
             citation="Kurtz, H. (1997). Spin cycle: How the White House and the media manipulate the news. Free Press.",
             locator="work", locator_type="work",
             supports="tactics of spin in the daily battle for control of the news", verified=False),
    ],
}

ENRICH = {
    "MC-699": {
        "summary": "نظریه همزیستی خبر و روابط عمومی می‌گوید روزنامه‌نگاری و روابط عمومی نه دو قلمرو جدا، بلکه دو نهاد وابسته به یکدیگرند: رسانه به منبع، داده و رویداد آماده نیاز دارد و روابط عمومی به دسترسی به مخاطب. گاندی در ۱۹۸۲ این وابستگی را با مفهوم یارانه اطلاعاتی صورت‌بندی کرد: واحد روابط عمومی هزینه گردآوری خبر را برای رسانه کاهش می‌دهد و در برابر، تعریف رویداد و چارچوب آن را نیز عرضه می‌کند. رسانه به سبب فشار زمان و کمبود منابع این یارانه را می‌پذیرد و مرز حرفه را با رویه‌هایی مانند بازنویسی، راستی‌آزمایی و افزودن زمینه حفظ می‌کند. سالوت و جانسون در ۲۰۰۶ با مرور بیش از یک دهه پژوهش نشان دادند رابطه دو حرفه ترکیبی از همکاری و رقابت است و اعتماد، کالای اصلی این رابطه است. نظریه توضیح می‌دهد چرا بخش بزرگی از اخبار از بیانیه‌های خبری می‌آید، چرا روابط عمومی گاه گفتار رسانه را شکل می‌دهد و چرا شفافیت منبع معیار اصلی اعتماد است. اهمیت عملی آن، طراحی رویه‌های تحریریه برای تشخیص یارانه از تبلیغ پنهان است.",
        "definition": "همزیستی خبر و روابط عمومی، رابطه وابستگی متقابل میان دو نهاد است که در آن یارانه اطلاعاتی، هزینه گردآوری خبر را برای رسانه کاهش می‌دهد و در برابر، دسترسی و چارچوب رویداد را برای منبع فراهم می‌کند.",
        "main_problem": "مسئله این است که چرا رسانه مستقل، پیوسته از منبع ذی‌نفع نقل می‌کند. پاسخ، وابستگی ساختاری و کاهش هزینه است. پرسش دوم، مرز است: تحریریه چگونه یارانه اطلاعاتی را بپذیرد بی‌آنکه چارچوب منبع را وام بگیرد.",
        "mechanism": "۱. یارانه اطلاعاتی: واحد روابط عمومی، داده آماده و رویداد سازمان‌یافته عرضه می‌کند.\n۲. کاهش هزینه: رسانه در زمان و نیروی محدود، خبر آماده را می‌پذیرد.\n۳. دسترسی متقابل: روابط عمومی به مخاطب و رسانه به منبع نیاز دارد.\n۴. چارچوب‌بندی منبع: تعریف رویداد و اولویت آن، همراه یارانه می‌آید.\n۵. مرز حرفه: بازنویسی، راستی‌آزمایی و افزودن زمینه، استقلال را حفظ می‌کند.\n۶. اعتماد: شفافیت رابطه منبع با خبر، سرمایه اصلی است.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا بیانیه خبری به متن رسانه راه می‌یابد، چرا بحران سازمانی با روایت آماده مدیریت می‌شود و چرا خبرنگار بی منبع، دسترسی را از دست می‌دهد. نکته مهم این است که همزیستی هم همکاری مشروع است و هم خطر: اگر تحریریه سنجه‌ای برای تشخیص منفعت منبع نداشته باشد، یارانه به تبلیغ پنهان بدل می‌شود؛ از این رو، رویه شفافیت شرط بقای اعتماد است.",
        "assumptions": [
            "رسانه و روابط عمومی به هم وابسته‌اند.",
            "یارانه اطلاعاتی، هزینه گردآوری را کاهش می‌دهد.",
            "چارچوب منبع با داده آماده منتقل می‌شود.",
        ],
        "principles": [
            "دسترسی، بده‌بستان دوطرفه است.",
            "شفافیت منبع، اعتماد را حفظ می‌کند.",
            "مرز حرفه با رویه تحریریه ساخته می‌شود.",
        ],
        "critiques": [
            "۱. تعمیم: الگوی وابستگی در کشورها و رسانه‌های کوچک متفاوت است.\n۲. قدرت: روابط عمومی ثروتمند، دسترسی نابرابر می‌سازد.\n۳. سنجش: سهم یارانه در خبر سخت اندازه‌گیری می‌شود.\n۴. دیجیتال: رسانه اجتماعی، رابطه را از خبرنگار به الگوریتم منتقل کرده است.\n۵. اعتماد: نظرسنجی از مخاطب، تصویر کامل رابطه را نمی‌دهد.",
        ],
        "applications": [
            "تحریریه: سنجه شفافیت منبع.",
            "آموزش روزنامه‌نگاری: تمایز یارانه و تبلیغ.",
            "روابط عمومی: اخلاق دسترسی.",
            "سیاست رسانه: شفافیت مالی منابع خبری.",
        ],
        "evolution": "گاندی در ۱۹۸۲ یارانه اطلاعاتی را صورت‌بندی کرد، پژوهش رابطه دو حرفه در دهه ۱۹۹۰ گسترش یافت و سالوت و جانسون در ۲۰۰۶ با مرور پژوهش، همکاری و رقابت را در یک چارچوب جمع کردند.",
        "key_concepts": [
            "یارانه اطلاعاتی (Information Subsidy)",
            "وابستگی متقابل (Mutual Dependence)",
            "دسترسی (Access)",
            "چارچوب‌بندی منبع (Source Framing)",
            "مرز حرفه (Professional Boundary)",
            "شفافیت منبع (Source Transparency)",
        ],
        "studies": [
            "Gandy, O. H. (1982). Beyond agenda setting. Ablex.",
            "Sallot, L. M., & Johnson, E. A. (2006). Investigating relationships between journalists and public relations practitioners. Public Relations Review, 32(2), 151-159.",
        ],
        "theorists": "اسکار گاندی جونیور؛ لین سالوت؛ الیزابت جانسون",
        "theorists_text": "گاندی (۱۹۸۲)؛ سالوت و جانسون (۲۰۰۶)",
        "year": 1982,
        "model": "یارانه اطلاعاتی + نیاز رسانه → پذیرش داده آماده → حفظ مرز با رویه تحریریه → اعتماد یا تبلیغ پنهان.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nگاندی خبر را محصول تبادل منابع دید: منبع، داده ارزان می‌دهد و رسانه، دسترسی می‌دهد. نوآوری چارچوب، تحلیل خبر به‌عنوان اقتصاد توجه و اطلاعات است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با تحلیل محتوای خبر، مصاحبه تحریریه و ردیابی منبع انجام می‌شود. پژوهشی که تنها بیانیه خبری را می‌خواند، بازنویسی تحریریه را از دست می‌دهد؛ و پژوهشی که هر نقل قول را نفوذ می‌خواند، تفاوت روزنامه‌نگاری و تبلیغ را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در تحلیل دستور کار است، اما باید با تحلیل مالکیت تکمیل شود. دسترسی بی شفافیت، به نابرابری گفتار بدل می‌شود.",
        "critique_text": "\n".join([
            "۱. تعمیم: الگوی وابستگی یکسان نیست.",
            "۲. قدرت: دسترسی نابرابر کم تحلیل می‌شود.",
            "۳. سنجش: سهم یارانه سخت اندازه‌پذیر است.",
            "۴. دیجیتال: رابطه به الگوریتم منتقل شده است.",
            "۵. اعتماد: تصویر کامل رابطه ناقص است.",
        ]),
        "example_text": "شرکتی که سانحه‌ای را با بیانیه آماده و ویدئوی اختصاصی اعلام می‌کند، هم خبر را ارزان می‌کند و هم روایت را می‌سازد؛ رسانه اگر منبع و انگیزه را افشا نکند، ناخواسته بازوی انتشار می‌شود.",
    },
    "MC-701": {
        "summary": "نظریه چرخش خبری، مدیریت راهبردی معنا در خبر را تحلیل می‌کند: کنشگر سیاسی یا سازمانی می‌کوشد رویداد را پیش از انتشار، به سود خود تعریف و تفسیر کند. کرتز در ۱۹۹۷ با مطالعه کاخ سفید نشان داد چرخش تنها دروغ یا پنهان‌کاری نیست؛ مجموعه‌ای از تاکتیک‌های زمان‌بندی، افشای گزینشی، تکرار پیام و مدیریت دستور کار است. اسر، راینمان و فان در ۲۰۰۱ چارچوب فراارتباطی را عرضه کردند: چرخش‌دهنده نه فقط درباره رویداد، بلکه درباره خود رسانه و نحوه پوشش آن نیز پیام می‌فرستد و می‌کوشد معیار خبرنگاری را جابه‌جا کند. رسانه در برابر، با راستی‌آزمایی، زمینه‌سازی و افشای انگیزه پاسخ می‌دهد. بنابراین خبر، محصول منازعه‌ای میان روایت منبع و رویه تحریریه است. نظریه توضیح می‌دهد چرا یک رویداد واحد روایت‌های متضاد می‌گیرد، چرا زمان انتشار خبر اهمیت دارد و چرا شفافیت مهم‌ترین سلاح خبرنگار در برابر چرخش است. اهمیت چارچوب، تحلیل خبر به‌عنوان فرایند مذاکره معناست، نه انتقال واقعیت؛ و همین نگاه، ارزیابی رسانه را از صداقت فردی به کیفیت رویه پیوند می‌دهد.",
        "definition": "چرخش خبری، مجموعه تاکتیک‌های راهبردی برای تعریف، زمان‌بندی و چارچوب‌بندی رویداد به سود کنشگر است که با مدیریت فراارتباطی، معیار پوشش رسانه‌ای را نیز هدف می‌گیرد.",
        "main_problem": "مسئله این است که چرا رویداد واحد روایت‌های متضاد می‌گیرد و چه کسی تعریف آن را پیش از انتشار می‌سازد. پاسخ، چرخش راهبردی است. پرسش دوم، مقاومت است: تحریریه چگونه چرخش را از انتخاب مشروع واقعیت جدا کند.",
        "mechanism": "۱. تعریف پیش‌دستانه: رویداد پیش از انتشار، در چارچوب مطلوب روایت می‌شود.\n۲. زمان‌بندی: انتشار در لحظه مناسب، رقابت روایت‌ها را محدود می‌کند.\n۳. افشای گزینشی: بخشی از داده برای هدایت توجه عرضه می‌شود.\n۴. تکرار پیام: عبارت کوتاه و تکرارشونده، حافظه خبری را می‌سازد.\n۵. فراارتباطی: چرخش‌دهنده درباره خود رسانه و معیار آن نیز پیام می‌فرستد.\n۶. پاسخ تحریریه: راستی‌آزمایی، زمینه‌سازی و افشای انگیزه، چرخش را محدود می‌کند.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا یک بحران با عبارت‌های آماده توصیف می‌شود، چرا خبر فوری گاه ناقص منتشر می‌شود و چرا رسانه‌ای که منبع را افشا نمی‌کند، در دام چرخش می‌افتد. نکته مهم این است که چرخش همیشه دروغ نیست؛ گاه انتخاب مشروع از میان واقعیت‌هاست و همین ابهام تشخیص را دشوار می‌کند؛ از این رو، معیار ارزیابی نباید نیت فردی، بلکه شفافیت رویه و تناسب زمینه باشد.",
        "assumptions": [
            "خبر، میدان منازعه تعریف است.",
            "زمان‌بندی، رقابت روایت را محدود می‌کند.",
            "چرخش می‌تواند بی دروغ رخ دهد.",
        ],
        "principles": [
            "پیش‌دستی در تعریف، مزیت می‌سازد.",
            "فراارتباطی، معیار رسانه را هدف می‌گیرد.",
            "شفافیت، مقاومت تحریریه است.",
        ],
        "critiques": [
            "۱. سنجش: تشخیص چرخش از انتخاب مشروع دشوار است.\n۲. نیت: چارچوب اغلب به انگیزه کنشگر تکیه می‌کند.\n۳. زمینه: الگوی چرخش در نظام‌های سیاسی متفاوت است.\n۴. دیجیتال: شبکه اجتماعی، چرخش را به عمل جمعی بدل کرده است.\n۵. اثربخشی: اندازه اثر چرخش بر مخاطب کم سنجیده شده است.",
        ],
        "applications": [
            "تحریریه: رویه راستی‌آزمایی و افشای انگیزه.",
            "ارتباط سیاسی: تحلیل راهبرد پیام.",
            "سواد خبری: شناخت تاکتیک چرخش.",
            "پژوهش رسانه: ردیابی منبع روایت.",
        ],
        "evolution": "کرتز در ۱۹۹۷ چرخش را در عمل سیاسی مستند کرد و اسر و همکاران در ۲۰۰۱ آن را به چارچوب فراارتباطی پیوند زدند. پژوهش رسانه اجتماعی، چرخش شبکه‌ای و حساب‌های ناشناس را افزود.",
        "key_concepts": [
            "چرخش خبری (News Spin)",
            "فراارتباطی (Metacommunication)",
            "مدیریت دستور کار (Agenda Management)",
            "افشای گزینشی (Selective Disclosure)",
            "چارچوب‌بندی راهبردی (Strategic Framing)",
            "راستی‌آزمایی (Verification)",
        ],
        "studies": [
            "Esser, F., Reinemann, C., & Fan, D. (2001). Spin doctors in the United States, Great Britain, and Germany. The International Journal of Press/Politics, 6(1), 16-45.",
            "Kurtz, H. (1997). Spin cycle. Free Press.",
        ],
        "theorists": "هوارد کرتز؛ فرانک اسر؛ کارستن راینمان؛ دیوید فان",
        "theorists_text": "کرتز (۱۹۹۷)؛ اسر و همکاران (۲۰۰۱)",
        "year": 2001,
        "model": "تعریف و زمان‌بندی منبع → فراارتباطی → انتشار روایت → پاسخ تحریریه یا تسلیم به چارچوب.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nکرتز چرخش را در عمل روزمره قدرت توصیف کرد و اسر و همکاران آن را به نظریه فراارتباطی رساندند. نوآوری چارچوب، پیوند تاکتیک رسانه‌ای با معیار خبرنگاری است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با تحلیل محتوا، مصاحبه خبرنگار و ردیابی زمان انتشار انجام می‌شود. پژوهشی که تنها نیت را می‌خواند، رویه را از دست می‌دهد؛ و پژوهشی که هر چارچوب‌بندی را چرخش می‌خواند، انتخاب مشروع را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در تحلیل خبر فوری است، اما باید با مطالعه مخاطب تکمیل شود. چرخش بی پاسخ تحریریه، به نفوذ کامل بدل می‌شود.",
        "critique_text": "\n".join([
            "۱. سنجش: تمایز چرخش و انتخاب دشوار است.",
            "۲. نیت: چارچوب به انگیزه تکیه می‌کند.",
            "۳. زمینه: نظام‌های سیاسی متفاوت‌اند.",
            "۴. دیجیتال: چرخش جمعی شده است.",
            "۵. اثر: تأثیر بر مخاطب کم سنجیده شده است.",
        ]),
        "example_text": "وزارتی خبر افزایش قیمت را در ساعت پایانی روز و همراه با بسته حمایتی اعلام می‌کند؛ زمان‌بندی و چارچوب، پیش از واکنش رسانه، معنای خبر را جهت می‌دهد.",
    },
}

REQUIRED_SECTIONS = ["summary", "definition", "main_problem", "mechanism", "assumptions",
                     "principles", "critiques", "applications", "evolution", "key_concepts",
                     "theorists", "model", "studies"]
WORD_KEYS = ["summary", "definition", "main_problem", "mechanism", "critiques", "applications",
             "evolution", "key_concepts", "principles", "studies", "assumptions"]


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


NAME_FIX = {}
YEAR_FIX = {
    "MC-699": "year corrected 1959 -> 1982: unverifiable 'Gieber/Bass 1959' attribution replaced by verified anchor Gandy 1982 (information subsidies)",
    "MC-701": "year corrected 1974 -> 2001: unverifiable 'Taro 1974' attribution replaced by verified anchor Esser, Reinemann & Fan 2001 (metacommunication)",
}


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
                                       "verified": n_verified, "batch": 115}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH115 THEORY DONE")


if __name__ == "__main__":
    main()
