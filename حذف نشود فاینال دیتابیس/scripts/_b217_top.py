# -*- coding: utf-8 -*-
"""Batch 217: repair MC-544, MC-545, MC-546, MC-547, MC-548."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch217-20261117"
NOW = "2026-11-17 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch217.json"

S = {
    "MC-544": [
        dict(kind="BOOK", title_en="Sprachtheorie: Die Darstellungsfunktion der Sprache",
             title_fa="نظریهٔ زبان: کارکرد بازنمایی زبان",
             authors="Karl Bühler", year=1934, publisher="Gustav Fischer",
             doi=None, url="https://pure.mpg.de/view/item_2305592_5",
             language="de", isbn=None,
             citation="Bühler, K. (1934). Sprachtheorie: Die Darstellungsfunktion der Sprache. Jena: Gustav Fischer.",
             locator="book", locator_type="BOOK",
             supports="organon model with expression, appeal and representation functions", verified=True),
        dict(kind="BOOK", title_en="Theory of Language: The Representational Function of Language",
             title_fa="نظریهٔ زبان: کارکرد بازنمایی زبان",
             authors="Karl Bühler", year=2011, publisher="John Benjamins",
             doi="10.1075/z.164", url="https://benjamins.com/catalog/z.164",
             language="en", isbn=None,
             citation="Bühler, K. (2011). Theory of Language: The Representational Function of Language (D. F. Goodwin, Trans.). Amsterdam: John Benjamins. (Original work published 1934)",
             locator="book", locator_type="BOOK",
             supports="English translation of the organon model for international scholarship", verified=True),
    ],
    "MC-545": [
        dict(kind="BOOK", title_en="Communication: The Social Matrix of Psychiatry",
             title_fa="ارتباط: بافت اجتماعی روان‌پزشکی",
             authors="Jürgen Ruesch; Gregory Bateson", year=1951, publisher="W. W. Norton",
             doi=None, url="https://archive.org/details/communicationsoc00inrues",
             language="en", isbn=None,
             citation="Ruesch, J., & Bateson, G. (1951). Communication: The Social Matrix of Psychiatry. New York: W. W. Norton.",
             locator="book", locator_type="BOOK",
             supports="communication as a circular social process with levels of message", verified=True),
        dict(kind="JOURNAL_ARTICLE", title_en="Review of Communication: The Social Matrix of Psychiatry",
             title_fa="مروری بر ارتباط: بافت اجتماعی روان‌پزشکی",
             authors="George J. Hinkle", year=1951,
             publisher="The Annals of the American Academy of Political and Social Science",
             doi="10.1177/000271625127800158",
             url="https://journals.sagepub.com/doi/10.1177/000271625127800158",
             language="en", isbn=None,
             citation="Hinkle, G. J. (1951). Review of Communication: The Social Matrix of Psychiatry. The Annals of the American Academy of Political and Social Science, 278(1).",
             locator="278(1)", locator_type="PAGE",
             supports="contemporary scholarly reception of the communication framework", verified=True),
    ],
    "MC-546": [
        dict(kind="BOOK", title_en="Communication and Communication Systems",
             title_fa="ارتباط و نظام‌های ارتباطی",
             authors="Lee Thayer", year=1968, publisher="Richard D. Irwin",
             doi=None, url="https://search.gesis.org/publication/gesis-bib-90579?lang=en",
             language="en", isbn=None,
             citation="Thayer, L. (1968). Communication and Communication Systems. Homewood, IL: Richard D. Irwin.",
             locator="book", locator_type="BOOK",
             supports="meaning allocation and communication as a systemic process", verified=True),
        dict(kind="WEBSITE", title_en="GESIS record for Communication and Communication Systems",
             title_fa="رکورد کتاب‌شناختی ارتباط و نظام‌های ارتباطی",
             authors="GESIS Leibniz Institute for the Social Sciences", year=1968,
             publisher="GESIS",
             doi=None, url="https://search.gesis.org/publication/gesis-bib-90579?lang=en",
             language="en", isbn=None,
             citation="GESIS Leibniz Institute for the Social Sciences. (n.d.). Bibliographic record for Communication and Communication Systems (L. Thayer, 1968).",
             locator="record", locator_type="PAGE",
             supports="bibliographic verification of the 1968 edition", verified=True),
    ],
    "MC-547": [
        dict(kind="BOOK", title_en="Mass Communication: A Sociological Perspective",
             title_fa="ارتباط جمعی: چشم‌اندازی جامعه‌شناختی",
             authors="Charles R. Wright", year=1959, publisher="Random House",
             doi=None, url="https://books.google.com/books/about/Mass_Communication.html?id=-cNoAAAAIAAJ",
             language="en", isbn=None,
             citation="Wright, C. R. (1959). Mass Communication: A Sociological Perspective. New York: Random House.",
             locator="book", locator_type="BOOK",
             supports="structural-functional analysis and four functions of mass communication", verified=True),
        dict(kind="WEBSITE", title_en="Charles R. Wright, Communications",
             title_fa="چارلز رایت، ارتباطات",
             authors="University of Pennsylvania Almanac", year=2017,
             publisher="University of Pennsylvania",
             doi=None, url="https://almanac.upenn.edu/articles/charles-r.-wright-communications",
             language="en", isbn=None,
             citation="University of Pennsylvania Almanac. (2017). Charles R. Wright, Communications. Almanac, University of Pennsylvania.",
             locator="web page", locator_type="PAGE",
             supports="biographical confirmation of the 1959 functionalist book", verified=True),
    ],
    "MC-548": [
        dict(kind="BOOK_CHAPTER", title_en="A Cultural Approach to Communication",
             title_fa="رهیافتی فرهنگی به ارتباط",
             authors="James W. Carey", year=1989, publisher="Unwin Hyman",
             doi=None, url="https://web.mit.edu/21l.432/www/readings/Carey_CulturalApproachCommunication.pdf",
             language="en", isbn=None,
             citation="Carey, J. W. (1989). A cultural approach to communication. In Communication as Culture: Essays on Media and Society. Boston: Unwin Hyman.",
             locator="chapter", locator_type="CHAPTER",
             supports="contrast between transmission and ritual views of communication", verified=True),
        dict(kind="WEBSITE", title_en="Ritual View of Communication",
             title_fa="دیدگاه آیینی ارتباط",
             authors="EBSCO Research Starters", year=None, publisher="EBSCO",
             doi=None, url="https://www.ebsco.com/research-starters/communication-and-mass-media/ritual-view-communication",
             language="en", isbn=None,
             citation="EBSCO Research Starters. (n.d.). Ritual view of communication. EBSCO.",
             locator="web page", locator_type="PAGE",
             supports="definition and attribution of the ritual view to Carey", verified=True),
    ],
}

ENRICH = {
    "MC-544": dict(
        needs_enrichment=False,
        level="پایه",
        related_approaches="نشانه‌شناسی؛ مدل کارکردهای زبان یاکوبسون؛ تحلیل گفتمان؛ زبان‌شناسی نقش‌گرا؛ نظریهٔ ارتباط کلامی.",
        recommended_sources="«نظریهٔ زبان: کارکرد بازنمایی زبان» (بولر، ۱۹۳۴)؛ «نظریهٔ زبان» (ترجمهٔ انگلیسی، ۲۰۱۱)؛ «سخن پایانی: زبان‌شناسی و شعرشناسی» (یاکوبسون، ۱۹۶۰).",
        detailed_analysis=("۱. بنیان و منطق نظری\nبولر (۱۹۳۴) در نظریهٔ زبان، نشانهٔ زبانی را ابزاری سه‌کارکردی دانست و آن را بر پایهٔ مفهوم ارگانون در اندیشهٔ یونانی در مثلثی رسم کرد که سه ضلع آن گوینده، شنونده و جهان است. "
                           "هر نشانه هم‌زمان بیان حال گوینده، برانگیختن شنونده و بازنمایی جهان را انجام می‌دهد؛ هیچ‌کدام از سه کارکرد به‌تنهایی کامل نیست.\n\n"
                           "۲. ساختارهای مفهومی\nکارکرد بیان، کارکرد برانگیختن و کارکرد بازنمایی، همراه با سه قطب گوینده، شنونده و جهان، سازه‌های اصلی‌اند. نشانه با هر سه ضلع نسبت دارد و همین نسبت سه‌گانه، هستهٔ مدل است.\n\n"
                           "۳. نمونه‌های تحلیلی\nجملهٔ «باران می‌آید» می‌تواند هم‌زمان واقعیت را بازنمایی کند، نگرانی گوینده را بیان کند و شنونده را به بردن چتر وادار کند؛ در تبلیغ، وزن کارکرد برانگیختن بیشتر می‌شود و در خبر، کارکرد بازنمایی.\n\n"
                           "۴. نقدها و چالش‌ها\nمدل بر زبان کلامی متمرکز است و ارتباط غیرکلامی و تصویری را کم پوشش می‌دهد؛ نقش بازخورد و مذاکرهٔ معنا را کم‌رنگ می‌کند؛ سه کارکرد را بدون سلسله‌مراتب و وزن تجربی رها می‌کند؛ و بافت فرهنگی رمزگان را چندان تحلیل نمی‌کند.\n\n"
                           "۵. سیر تاریخی\nمدل در سال ۱۹۳۴ منتشر شد و در ترجمهٔ انگلیسی ۲۰۱۱ به دسترس پژوهشگران بین‌المللی رسید. یاکوبسون (۱۹۶۰) آن را به شش کارکرد گسترد و به تحلیل شعر، تبلیغ و رسانه راه داد.\n\n"
                           "۶. جایگاه در بحث روز\nدر تحلیل چندرسانه‌ای و چندوجهی، مدل بولر یادآوری می‌کند که هر پیام هم‌زمان بازنمایی، بیان و برانگیختن است و تقلیل پیام به «انتقال اطلاعات» ناقص است."),
    ),
    "MC-545": dict(
        needs_enrichment=False,
        level="میان",
        related_approaches="مکتب پالو آلتو؛ نظریهٔ نظام‌ها؛ ارتباطات درمانی؛ فرانظریهٔ ارتباط؛ ارتباطات بین‌فرهنگی.",
        recommended_sources="«ارتباط: بافت اجتماعی روان‌پزشکی» (روش و بیتسون، ۱۹۵۱)؛ «مروری بر ارتباط: بافت اجتماعی روان‌پزشکی» (هینکل، ۱۹۵۱)؛ «عمل‌گرایی و نظریهٔ ارتباط» (واتزلاویک و همکاران).",
        detailed_analysis=("۱. بنیان و منطق نظری\nروش و بیتسون (۱۹۵۱) ارتباط را نه انتقال یک‌طرفهٔ اطلاعات، بلکه فرایندی دایره‌ای در بافت اجتماعی دانستند که در سطوح درون‌فردی، میان‌فردی، گروهی و فرهنگی جریان دارد. "
                           "هر پیام افزون بر محتوا، لایه‌ای دربارهٔ خودِ ارتباط نیز حمل می‌کند؛ همین ایده بعدها به مفهوم فرارتباط در مکتب پالو آلتو تبدیل شد.\n\n"
                           "۲. ساختارهای مفهومی\nفرایند دایره‌ای، سطوح ارتباط، بافت اجتماعی، محتوا و لایهٔ ارتباطی سازه‌های اصلی‌اند. مدل ارتباط را از مدل خطی جدا می‌کند و بازخورد را ذاتی می‌داند.\n\n"
                           "۳. نمونه‌های تحلیلی\nیک جملهٔ ساده در گفت‌وگوی درمانی می‌تواند هم محتوا داشته باشد و هم دربارهٔ رابطهٔ گوینده و شنونده حرف بزند؛ در تعارض سازمانی نیز پیام‌ها بیش از آنکه اطلاعات منتقل کنند، وضعیت رابطه را تعریف می‌کنند.\n\n"
                           "۴. نقدها و چالش‌ها\nخاستگاه روان‌پزشکی، مدل را به بافت درمانی وابسته می‌کند؛ سازه‌ها انتزاعی و سنجش تجربی دشوار است؛ ساخت قدرت و اقتصاد رسانه کمتر تحلیل می‌شود؛ و کاربرد آن در ارتباط جمعی به تفسیر کیفی وابسته می‌ماند.\n\n"
                           "۵. سیر تاریخی\nکتاب ۱۹۵۱ پیوند روان‌پزشکی و نظریهٔ ارتباط را برقرار کرد و نقد معاصر هینکل همان سال، پذیرش علمی آن را نشان می‌دهد؛ مکتب پالو آلتو و نظریهٔ نظام‌ها میراث آن را گستردند.\n\n"
                           "۶. جایگاه در بحث روز\nدر تحلیل ارتباط درمانی، تعارض سازمانی و پیام‌های رسانه‌ای چندلایه، مدل روش و بیتسون همچنان چارچوبی برای دیدن لایهٔ رابطه‌ای ارتباط است."),
    ),
    "MC-546": dict(
        needs_enrichment=False,
        level="میان",
        related_approaches="نظریهٔ نظام‌ها؛ ارتباطات سازمانی؛ نشانه‌شناسی دریافت؛ مدل انتقالی در برابر آیینی؛ ساخت‌گرایی اجتماعی.",
        recommended_sources="«ارتباط و نظام‌های ارتباطی» (تایر، ۱۹۶۸)؛ «رهیافتی فرهنگی به ارتباط» (کری، ۱۹۸۹)؛ «نظریه‌های ارتباط جمعی» (مک‌کوایل).",
        detailed_analysis=("۱. بنیان و منطق نظری\nتایر (۱۹۶۸) استدلال کرد معنا در پیام جای ندارد؛ پیام تنها مجموعه‌ای از نشانه‌ها است و هر طرف بر پایهٔ تجربه، نظام مفهومی و موقعیت خود به آن معنا تخصیص می‌دهد. "
                           "از این رو ارتباط، خلق و بازخلق معنا در بستر نظام‌های ارتباطی است و نه انتقال یک بستهٔ معنایی از فرستنده به گیرنده.\n\n"
                           "۲. ساختارهای مفهومی\nتخصیص معنا، بازخلق مشترک، نظام ارتباطی، تجربهٔ پیشین و بافت سازمانی سازه‌های اصلی‌اند. مدل بر فعال بودن گیرنده تأکید می‌کند.\n\n"
                           "۳. نمونه‌های تحلیلی\nیک بخشنامهٔ سازمانی یکسان می‌تواند در دو واحد متفاوت دو معنا بگیرد؛ خبر نیز در گروه‌های اجتماعی مختلف تفسیرهای متفاوت می‌یابد؛ همین سازوکار توضیح می‌دهد چرا پیام واحد به نتایج ناهمگون می‌رسد.\n\n"
                           "۴. نقدها و چالش‌ها\nمدل به ایده‌آلیسم نزدیک می‌شود و نقش ساختار قدرت و منابع را کم‌رنگ می‌کند؛ تخصیص معنا را دشوار می‌توان سنجید؛ مرز میان تفسیر فردی و رمزگان فرهنگی روشن نیست؛ و خطر نسبی‌گرایی تفسیری را دارد.\n\n"
                           "۵. سیر تاریخی\nکتاب ۱۹۶۸ در سنت ارتباطات سازمانی و نظام‌ها منتشر شد و بعدها با چرخش فرهنگی و پژوهش‌های دریافت مخاطب پیوند یافت.\n\n"
                           "۶. جایگاه در بحث روز\nدر تحلیل ارتباطات سازمانی و تفسیر مخاطب از محتوای دیجیتال، تأکید تایر بر تخصیص فعال معنا همچنان بنیادین است."),
    ),
    "MC-547": dict(
        needs_enrichment=False,
        level="میان",
        related_approaches="کارکردگرایی ساختاری؛ جامعه‌شناسی ارتباطات؛ مدل رایلی و رایلی؛ نظریهٔ استفاده و رضامندی؛ نقد کارکردگرایی.",
        recommended_sources="«ارتباط جمعی: چشم‌اندازی جامعه‌شناختی» (رایت، ۱۹۵۹)؛ «ارتباط جمعی و نظام اجتماعی» (رایلی و رایلی، ۱۹۵۹)؛ «نظریهٔ اجتماعی و ساختار اجتماعی» (مرتون).",
        detailed_analysis=("۱. بنیان و منطق نظری\nرایت (۱۹۵۹) تحلیل کارکردی مرتون را به ارتباط جمعی برد و رسانه را نهادی در نظام اجتماعی دانست که برای بقا و تعادل نظام کارکردهایی انجام می‌دهد. "
                           "او چهار کارکرد را برشمرد: اطلاع و هشدار دربارهٔ محیط، همبستگی و تفسیر اطلاعات برای واکنش جمعی، انتقال فرهنگ و میراث اجتماعی، و سرگرمی.\n\n"
                           "۲. ساختارهای مفهومی\nکارکرد آشکار و پنهان، کژکارکرد، نظام اجتماعی، نهاد رسانه و تعادل نظام سازه‌های اصلی‌اند. مدل کارکردها را در نسبت با نیازهای نظام تعریف می‌کند.\n\n"
                           "۳. نمونه‌های تحلیلی\nپوشش خبری هشدار دربارهٔ بلایای طبیعی کارکرد آشکار اطلاع دارد و تقویت همبستگی ملی کارکرد پنهان آن است؛ برنامهٔ سرگرمی می‌تواند هم آسایش بدهد و هم کژکارکرد انفعال سیاسی داشته باشد.\n\n"
                           "۴. نقدها و چالش‌ها\nکارکردگرایی به حفظ وضع موجود گرایش دارد؛ تعادل نظام را بیش از تعارض مفروض می‌گیرد؛ قدرت و نابرابری را کم‌بررسی می‌گذارد؛ کارکردها را دشوار می‌توان جدا از تفسیر تحلیلگر سنجید؛ و برای رسانهٔ دیجیتال و تعامل مخاطب بازنگری می‌خواهد.\n\n"
                           "۵. سیر تاریخی\nکتاب ۱۹۵۹ چارچوب کارکردی را در جامعه‌شناسی ارتباط جمعی تثبیت کرد و با نقد کارکردگرایی در دهه‌های بعد، پژوهش‌های استفاده و رضامندی و تحلیل تعارض جای آن را گرفتند.\n\n"
                           "۶. جایگاه در بحث روز\nدر تحلیل نقش رسانه در انسجام اجتماعی و بحران، چارچوب چهار کارکرد رایت همچنان زبان توصیفی مفیدی است، به شرط افزودن تحلیل قدرت و نابرابری."),
    ),
    "MC-548": dict(
        needs_enrichment=False,
        level="میان",
        related_approaches="چرخش فرهنگی در ارتباطات؛ مدل ارتباط به‌مثابه فرهنگ؛ نشانه‌شناسی؛ مطالعات فرهنگی؛ آیین رسانه‌ای.",
        recommended_sources="«رهیافتی فرهنگی به ارتباط» (کری، ۱۹۸۹)؛ «ارتباط به‌مثابه فرهنگ» (کری، ۱۹۸۹)؛ «دیدگاه آیینی ارتباط» (ای‌بی‌اس‌کو).",
        detailed_analysis=("۱. بنیان و منطق نظری\nکری (۱۹۸۹) دو فهم رقیب از ارتباط را از هم جدا کرد. دیدگاه انتقالی، ارتباط را فرایند انتقال پیام در فضا برای کنترل و نفوذ می‌داند و ریشهٔ آن به تلگراف و ارتباط از راه دور می‌رسد. "
                           "دیدگاه آیینی، ارتباط را مشارکت در فرهنگ مشترک و بازنمایی تجربهٔ مشترک می‌داند که جامعه را در زمان حفظ می‌کند.\n\n"
                           "۲. ساختارهای مفهومی\nانتقال در برابر آیین، فضا در برابر زمان، کنترل در برابر مشارکت، و اطلاعات در برابر معنا جفت‌های مفهومی اصلی‌اند. این دو دیدگاه دو استعارهٔ بنیادین از ارتباط‌اند.\n\n"
                           "۳. نمونه‌های تحلیلی\nخواندن خبر با دید انتقالی یعنی دریافت اطلاعات دربارهٔ رویدادها؛ با دید آیینی یعنی شرکت در آیین بازنمایی جامعه و بازسازی تصور مشترک از واقعیت؛ تماشای یک رویداد ملی نمونهٔ روشن وجه آیینی است.\n\n"
                           "۴. نقدها و چالش‌ها\nدوقطبی‌سازی انتقال و آیین واقعیت را ساده می‌کند؛ دید آیینی می‌تواند قدرت و ایدئولوژی را کم‌بررسی بگذارد؛ مدل بیشتر فرانظری است تا آزمون‌پذیر؛ و مرز دو دیدگاه در پژوهش تجربی مبهم می‌ماند.\n\n"
                           "۵. سیر تاریخی\nمقالهٔ کری در کتاب ارتباط به‌مثابه فرهنگ (۱۹۸۹) به یکی از متون بنیادین چرخش فرهنگی تبدیل شد و پژوهش‌های آیین رسانه‌ای و حافظهٔ جمعی بر آن تکیه کردند.\n\n"
                           "۶. جایگاه در بحث روز\nدر تحلیل رویدادهای رسانه‌ای و آیین‌های دیجیتال، تمایز انتقال و آیین ابزار مفیدی برای پرسیدن این است که رسانه چه چیزی را برای جامعه بازسازی می‌کند."),
    ),
}

NAME_FIX = {}

YEAR_FIX = {
    "MC-544": "replaced sender-template analysis with Bühler-specific analysis; rebuilt recommendations",
    "MC-545": "replaced sender-template analysis with Ruesch-Bateson analysis; rebuilt recommendations",
    "MC-546": "replaced sender-template analysis with Thayer meaning-allocation analysis; rebuilt recommendations",
    "MC-547": "replaced sender-template analysis with Wright functional analysis; rebuilt recommendations",
    "MC-548": "replaced sender-template analysis with Carey transmission-vs-ritual analysis; distinguished from MC-549",
}
