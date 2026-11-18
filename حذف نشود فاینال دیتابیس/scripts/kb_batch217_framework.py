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
                                       "verified": n_verified, "batch": 217}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH217 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
