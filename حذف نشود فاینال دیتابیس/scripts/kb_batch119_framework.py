# -*- coding: utf-8 -*-
"""Batch 119 (FRAMEWORK): full documentation for MC-128, MC-168, MC-199, MC-221."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch119-framework-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch119_framework.json"

S = {
    "MC-128": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Pyramid of Corporate Social Responsibility: Toward the Moral Management of Organizational Stakeholders",
             title_fa="هرم مسئولیت اجتماعی شرکتی: به‌سوی مدیریت اخلاقی ذی‌نفعان سازمان",
             authors="Carroll, A. B.", year=1991,
             publisher="Business Horizons",
             doi="10.1016/0007-6813(91)90005-G",
             url="https://www.sciencedirect.com/science/article/pii/000768139190005G",
             language="en", isbn=None,
             citation="Carroll, A. B. (1991). The pyramid of corporate social responsibility: Toward the moral management of organizational stakeholders. Business Horizons, 34(4), 39-48.",
             locator="34(4):39-48", locator_type="page_range",
             supports="four-layered CSR pyramid: economic, legal, ethical and philanthropic responsibilities", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Corporate Social Responsibility: Evolution of a Definitional Construct",
             title_fa="مسئولیت اجتماعی شرکتی: تحول یک سازهٔ تعریفی",
             authors="Carroll, A. B.", year=1999,
             publisher="Business & Society",
             doi=None, url=None, language="en", isbn=None,
             citation="Carroll, A. B. (1999). Corporate social responsibility: Evolution of a definitional construct. Business & Society, 38(3), 268-295.",
             locator="38(3):268-295", locator_type="page_range",
             supports="historical consolidation of CSR definitions and the pyramid's place in them", verified=False),
    ],
    "MC-168": [
        dict(kind="BOOK",
             title_en="Business Model Generation: A Handbook for Visionaries, Game Changers, and Challengers",
             title_fa="تولید مدل کسب‌وکار: راهنمای صاحبان چشم‌انداز، بازیگران تغییر و چالش‌گران",
             authors="Osterwalder, A.; Pigneur, Y.", year=2010,
             publisher="Wiley",
             doi=None,
             url="https://www.wiley.com/en-us/shop/general-introductory-business-management/business-model-generation-a-handbook-for-visionaries-game-changers-and-challengers-p-9780470876411",
             language="en", isbn="9780470876411",
             citation="Osterwalder, A., & Pigneur, Y. (2010). Business model generation: A handbook for visionaries, game changers, and challengers. Wiley.",
             locator="pp. 14-49", locator_type="page_range",
             supports="nine building blocks arranged on a single-page business model canvas", verified=True),
        dict(kind="THESIS",
             title_en="The Business Model Ontology: A Proposition in a Design Science Approach",
             title_fa="هستی‌شناسی مدل کسب‌وکار: پیشنهادی در رویکرد علم طراحی",
             authors="Osterwalder, A.", year=2004,
             publisher="Universite de Lausanne",
             doi=None, url=None, language="en", isbn=None,
             citation="Osterwalder, A. (2004). The business model ontology: A proposition in a design science approach (Doctoral dissertation). Universite de Lausanne.",
             locator="ch. 3", locator_type="work",
             supports="ontological derivation of the nine business model elements", verified=False),
    ],
    "MC-199": [
        dict(kind="REPORT",
             title_en="Information Disorder: Toward an Interdisciplinary Framework for Research and Policy Making",
             title_fa="اختلال اطلاعاتی: به‌سوی چارچوبی میان‌رشته‌ای برای پژوهش و سیاست‌گذاری",
             authors="Wardle, C.; Derakhshan, H.", year=2017,
             publisher="Council of Europe",
             doi=None,
             url="https://shorensteincenter.org/wp-content/uploads/2017/10/Information-Disorder-Toward-an-interdisciplinary-framework.pdf",
             language="en", isbn=None,
             citation="Wardle, C., & Derakhshan, H. (2017). Information disorder: Toward an interdisciplinary framework for research and policy making (Council of Europe report DGI(2017)09). Council of Europe.",
             locator="pp. 1-109", locator_type="page_range",
             supports="tripartite typology of mis-, dis- and mal-information with creation, production and distribution phases", verified=True),
        dict(kind="REPORT",
             title_en="Information Disorder: The Essential Glossary",
             title_fa="اختلال اطلاعاتی: واژه‌نامهٔ ضروری",
             authors="Wardle, C.; Derakhshan, H.", year=2018,
             publisher="First Draft",
             doi=None, url=None, language="en", isbn=None,
             citation="Wardle, C., & Derakhshan, H. (2018). Information disorder: The essential glossary. First Draft.",
             locator="glossary entries", locator_type="work",
             supports="operational definitions of key terms in the information disorder framework", verified=False),
    ],
    "MC-221": [
        dict(kind="BOOK_CHAPTER",
             title_en="The Reformed English Curriculum",
             title_fa="برنامهٔ درسی بازنگری‌شدهٔ زبان انگلیسی",
             authors="Postman, N.", year=1970,
             publisher="Pitman",
             doi=None,
             url="https://media-ecology.org/What-Is-Media-Ecology",
             language="en", isbn=None,
             citation="Postman, N. (1970). The reformed English curriculum. In A. C. Eurich (Ed.), High school 1980: The shape of the future in American secondary education (pp. 160-168). Pitman.",
             locator="pp. 160-168", locator_type="page_range",
             supports="media ecology defined as the study of media as environments", verified=True),
        dict(kind="BOOK",
             title_en="Understanding Media: The Extensions of Man",
             title_fa="شناخت رسانه: امتدادهای انسان",
             authors="McLuhan, M.", year=1964,
             publisher="McGraw-Hill",
             doi=None, url=None, language="en", isbn=None,
             citation="McLuhan, M. (1964). Understanding media: The extensions of man. McGraw-Hill.",
             locator="ch. 1", locator_type="work",
             supports="media as extensions of human faculties shaping sensory ratios and social form", verified=False),
    ],
}

ENRICH = {
    "MC-128": dict(
        summary="ارتباطات مسئولیت اجتماعی شرکتی، چارچوبی برای انتقال تعهدهای اخلاقی و اجتماعی سازمان به ذی‌نفعان است. آرچی کرول در مقالهٔ سال ۱۹۹۱ مسئولیت اجتماعی شرکت را در چهار لایه سازمان داد: مسئولیت اقتصادی به‌عنوان پایه، مسئولیت قانونی، مسئولیت اخلاقی و در رأس هرم مسئولیت بشردوستانه. در این چارچوب، شرکت پیش از هر چیز باید سودآور و کارآمد باشد، سپس در چارچوب قانون فعالیت کند، از انتظارهای اخلاقی پاسخگو باشد و در نهایت با منابع خود به بهبود جامعه کمک کند. ارتباطات مسئولیت اجتماعی وظیفه دارد این چهار لایه را به زبان ذی‌نفعان ترجمه کند و نشان دهد ادعاهای سازمان با رفتار واقعی آن هم‌خوان است. اعتبار این ارتباطات به سه شرط بستگی دارد: هم‌خوانی ادعا و عمل، شفافیت گزارش‌دهی و قابلیت راستی‌آزمایی مستقل. اگر این شروط برآورده نشوند، ارتباطات مسئولیت اجتماعی به سبزشویی تبدیل می‌شود؛ یعنی ارائهٔ تصویری اخلاقی از سازمانی که عملکردش با آن تصویر نمی‌خواند. از این رو پژوهش‌های معاصر بر شکاف میان گفتار و کردار سازمانی، نقش رسانه‌ها در آشکارسازی این شکاف و اهمیت گفت‌وگوی دوسویه با ذی‌نفعان تأکید می‌کنند. این چارچوب در تحلیل ارتباطات سازمانی، اعتبار برند، گزارش‌های پایداری و بحران‌های اعتماد عمومی کاربرد گسترده دارد و رسانه‌ها هم به‌عنوان ناقل و هم به‌عنوان ناظر بر ادعاهای شرکتی نقش دوگانه دارند. نقد اصلی به آن، خطر تبدیل مسئولیت اجتماعی به ابزار بازاریابی و کم‌رنگ‌شدن الزام‌های ساختاری است.",
        definition="ارتباطات مسئولیت اجتماعی شرکتی، مجموعهٔ راهبردها و پیام‌هایی است که سازمان برای اطلاع‌رسانی دربارهٔ تعهدها، عملکرد و پیامدهای اجتماعی و زیست‌محیطی خود به ذی‌نفعان به کار می‌گیرد.",
        main_problem="چگونه سازمان می‌تواند ادعاهای مسئولیت اجتماعی خود را چنان معتبر و شفاف بیان کند که ذی‌نفعان آن را باور کنند و به سبزشویی یا بدبینی عمومی دامن نزند.",
        mechanism="سازمان ابتدا اولویت‌های مسئولیت را بر پایهٔ اهمیت ذی‌نفعان تعیین می‌کند، سپس اقدام‌ها را در گزارش‌های قابل راستی‌آزمایی مستند می‌سازد و از مجرای رسانه‌های رسمی و اجتماعی، وبگاه و گفت‌وگوی مستقیم با ذی‌نفعان منتشر می‌کند. بازخورد ذی‌نفعان، اولویت‌ها و پیام‌ها را بازتنظیم می‌کند.",
        assumptions=[
            "شرکت در برابر جامعه فراتر از الزام قانونی مسئول است.",
            "ذی‌نفعان می‌توانند ادعاهای سازمان را ارزیابی و راستی‌آزمایی کنند.",
            "شفافیت و هم‌خوانی گفتار و کردار، شرط اصلی اعتبار است.",
            "گفت‌وگوی دوسویه بر تبلیغ یک‌سویه برتری دارد.",
        ],
        principles=[
            "هر لایهٔ مسئولیت بر لایهٔ زیرین خود استوار است؛ سودآوری پایهٔ بشردوستی است.",
            "پیام مسئولیت باید با شواهد عملکرد پشتیبانی شود.",
            "گزارش‌دهی باید کامل، قابل مقایسه و مستقل قابل بررسی باشد.",
            "سبزشویی، اعتبار بلندمدت سازمان را بیش از سود کوتاه‌مدت تخریب می‌کند.",
        ],
        critiques=[
            "مسئولیت اجتماعی می‌تواند به ابزار روابط عمومی و مدیریت تصویر فروکاسته شود.",
            "چارچوب هرمی، انتظارهای متعارض ذی‌نفعان را ساده می‌کند.",
            "تأکید بر اقدام داوطلبانه، فشار برای الزام قانونی را کاهش می‌دهد.",
            "سنجش اثر واقعی برنامه‌های بشردوستانه دشوار و کم‌سند است.",
        ],
        applications=[
            "طراحی راهبرد ارتباطی و گزارش پایداری سازمان‌های رسانه‌ای.",
            "ارزیابی اعتبار ادعاهای زیست‌محیطی و شناسایی سبزشویی.",
            "مدیریت بحران اعتماد پس از رسوایی سازمانی.",
            "آموزش روزنامه‌نگاری داده برای بررسی ادعاهای شرکتی.",
        ],
        evolution="کرول (۱۹۹۱) هرم چهارلایه را عرضه کرد و در ۱۹۹۹ تاریخ تحول تعریف‌ها را تدوین کرد؛ پژوهش‌های بعدی به مسئولیت اجتماعی مبتنی بر ذی‌نفعان، گزارش‌دهی پایداری، ارتباطات گفت‌وگومحور و در نهایت مفاهیم سبزشویی و شست‌وشوی اجتماعی گسترش یافت.",
        key_concepts=[
            "هرم مسئولیت اجتماعی (CSR Pyramid)",
            "ذی‌نفعان (Stakeholders)",
            "سبزشویی (Greenwashing)",
            "گزارش پایداری (Sustainability Reporting)",
            "شکاف گفتار و کردار (Walk-Talk Gap)",
        ],
        theorists="آرچی کرول",
        theorists_text="کرول (۱۹۹۱)؛ کرول (۱۹۹۹)",
        model="لایهٔ اقتصادی → لایهٔ قانونی → لایهٔ اخلاقی → لایهٔ بشردوستانه → انتقال شفاف به ذی‌نفعان → اعتبار یا سبزشویی.",
        studies=[
            "کرول (۱۹۹۱) هرم چهارلایه را با تأکید بر مدیریت اخلاقی ذی‌نفعان صورت‌بندی کرد.",
            "کرول (۱۹۹۹) تحول تعریف مسئولیت اجتماعی را از دههٔ ۱۹۵۰ به بعد مستند ساخت.",
        ],
        detailed_analysis="تحلیل عمیق نشان می‌دهد اعتبار ارتباطات مسئولیت اجتماعی بیش از حجم پیام به قابلیت اثبات آن وابسته است. سازمانی که گزارش‌هایش توسط نهاد مستقل بررسی می‌شود و ناکامی‌هایش را نیز اعلام می‌کند، سرمایهٔ اعتماد بیشتری می‌سازد. در محیط پلتفرمی، ذی‌نفعان خود تولیدکنندهٔ روایت‌اند و شکاف میان تبلیغ و عملکرد به‌سرعت آشکار می‌شود. از این رو ارتباطات مسئولیت اجتماعی به سمت گفت‌وگوی مستمر، پاسخ‌گویی و پذیرش نقد حرکت کرده است.",
        critique_text="نقد اصلی آن است که مسئولیت اجتماعی می‌تواند به ابزار روابط عمومی و مدیریت تصویر فروکاسته شود و بدون الزام قانونی و نظارت مستقل، به سبزشویی بیانجامد.",
        example_text="شرکتی که کمپین «بسته‌بندی سبز» راه می‌اندازد اما زبالهٔ صنعتی خود را پنهان می‌کند، با افشای گزارش نهاد مستقل، اعتماد عمومی را از دست می‌دهد؛ در حالی که همان شرکت با انتشار داده کامل و پذیرش نقد، می‌تواند اعتبار بازسازد.",
        year=1991,
    ),
    "MC-168": dict(
        summary="بوم مدل کسب‌وکار ابزاری بصری است که الکساندر استروالدر و ایو پینیور در کتاب سال ۲۰۱۰ خود معرفی کردند تا کل منطق اقتصادی یک سازمان در یک صفحه نمایش داده شود. این بوم مدل را به نه بلوک تقسیم می‌کند: بخش‌های مشتری، ارزش پیشنهادی، کانال‌ها، رابطه با مشتری، جریان‌های درآمد، منابع کلیدی، فعالیت‌های کلیدی، شرکای کلیدی و ساختار هزینه. چهار بلوک نخست در سمت راست بر بازار و مشتری تمرکز دارند و چهار بلوک بعدی در سمت چپ بر زیرساخت و کارایی؛ ارزش پیشنهادی در مرکز، پیوند دهندهٔ این دو نیمه است. کارکرد اصلی بوم آن است که مدیر را از فهرست کردن اجزا به دیدن وابستگی‌ها ببرد: تغییر در یک بلوک، بلوک‌های دیگر را تحت تأثیر قرار می‌دهد و انسجام کل مدل را می‌آزماید. در سازمان‌های رسانه‌ای، بوم به‌ویژه برای تفکیک مشتری از مخاطب و روشن‌کردن رابطهٔ محتوای رایگان با درآمد آگهی یا اشتراک سودمند است. این ابزار در کارگاه‌های طراحی مدل، مقایسهٔ گزینه‌های راهبردی و مستندسازی مدل موجود به کار می‌رود. نقد اصلی به بوم آن است که تصویری ایستا از کسب‌وکار می‌دهد و رقابت، پویایی بازار، اثرهای بیرونی اجتماعی و زیست‌محیطی را در خود جای نمی‌دهد؛ از این رو نسخه‌های تکمیلی مانند بوم ارزش پیشنهادی و بوم مدل پایدار برای رفع این کمبود ارائه شده‌اند.",
        definition="بوم مدل کسب‌وکار یک نمایش‌گر یک‌صفحه‌ای از نه عنصر سازندهٔ مدل کسب‌وکار است که منطق خلق، ارائه و تصرف ارزش در سازمان را به‌صورت بصری و قابل بحث نشان می‌دهد.",
        main_problem="چگونه می‌توان مدل کسب‌وکار پیچیده را چنان ساده و یکپارچه نمایش داد که تیم مدیریت بتواند وابستگی اجزا و پیامد تغییر هر بخش را هم‌زمان ببیند.",
        mechanism="تیم ابتدا بخش‌های مشتری و ارزش پیشنهادی را تعریف می‌کند، سپس کانال‌ها و رابطه با مشتری را برای رساندن ارزش مشخص می‌سازد؛ در سمت زیرساخت، منابع و فعالیت‌های کلیدی و شرکا را تعیین می‌کند و سرانجام جریان‌های درآمد و ساختار هزینه را برای سنجش تعادل مالی ترسیم می‌کند. تکرار این چرخه، فرض‌ها را می‌آزماید.",
        assumptions=[
            "مدل کسب‌وکار را می‌توان به اجزای نسبتاً مستقل و در عین حال وابسته تقسیم کرد.",
            "ارزش پیشنهادی، پیوند دهندهٔ نیاز مشتری و توانمندی سازمان است.",
            "نمایش بصری، فهم مشترک تیم را بهتر از متن طولانی می‌سازد.",
            "مدل را می‌توان پیش از اجرای کامل، روی کاغذ طراحی و مقایسه کرد.",
        ],
        principles=[
            "مدل کسب‌وکار یک سند یکپارچه است، نه فهرستی از بخش‌های جدا.",
            "هر بلوک باید با ارزش پیشنهادی و بخش مشتری سازگار باشد.",
            "درآمد و هزینه باید در کنار هم و نه جدا از هم تحلیل شوند.",
            "بوم نقطهٔ شروع گفت‌وگو است، نه نتیجهٔ نهایی تحلیل.",
        ],
        critiques=[
            "بوم تصویری ایستا می‌دهد و پویایی رقابت و تغییر بازار را نشان نمی‌دهد.",
            "اثرهای اجتماعی و زیست‌محیطی در نسخهٔ اصلی جایی ندارند.",
            "بوم به راهبرد رقابتی، موانع ورود و قدرت بازار نمی‌پردازد.",
            "بدون دادهٔ تجربی، بوم می‌تواند به تمرین ذهنی بی‌اعتبار تبدیل شود.",
        ],
        applications=[
            "طراحی مدل درآمدی استارتاپ رسانه‌ای و خدمات اشتراکی.",
            "مقایسهٔ گزینه‌های راهبردی سازمان خبری در گذار دیجیتال.",
            "مستندسازی و بازطراحی مدل کسب‌وکار موجود در کارگاه مدیریتی.",
            "آموزش کارآفرینی رسانه و تحلیل نمونه‌های موفق پلتفرمی.",
        ],
        evolution="استروالدر (۲۰۰۴) هستی‌شناسی نه‌عنصری مدل کسب‌وکار را در رسالهٔ دکتری خود تدوین کرد؛ کتاب ۲۰۱۰ آن را به ابزار بصری عمومی تبدیل کرد و نسخه‌های تکمیلی مانند بوم ارزش پیشنهادی و بوم مدل پایدار در دههٔ بعد افزوده شدند.",
        key_concepts=[
            "ارزش پیشنهادی (Value Proposition)",
            "بخش‌های مشتری (Customer Segments)",
            "جریان درآمد (Revenue Streams)",
            "ساختار هزینه (Cost Structure)",
            "شرکای کلیدی (Key Partnerships)",
        ],
        theorists="الکساندر استروالدر؛ ایو پینیور",
        theorists_text="استروالدر و پینیور (۲۰۱۰)؛ استروالدر (۲۰۰۴)",
        model="بخش مشتری و ارزش پیشنهادی → کانال و رابطه → منابع، فعالیت و شرکا → درآمد و هزینه → ارزیابی انسجام مدل.",
        studies=[
            "استروالدر و پینیور (۲۰۱۰) نه بلوک را در قالب یک بوم یک‌صفحه‌ای استاندارد کردند.",
            "استروالدر (۲۰۰۴) ریشهٔ نظری این نه عنصر را در هستی‌شناسی مدل کسب‌وکار تشریح کرد.",
        ],
        detailed_analysis="تحلیل عمیق نشان می‌دهد ارزش بوم در گفت‌وگوی تیمی و آشکارسازی فرض‌های ناسازگار است. تیمی که بلوک‌ها را پر می‌کند، اغلب متوجه می‌شود بخش مشتری و جریان درآمدش با ارزش پیشنهادی هم‌خوان نیست. در رسانه، این ناسازگاری معمولاً در تفکیک مخاطب از مشتری آشکار می‌شود: مخاطب محتوا می‌خواهد و آگهی‌دهنده دسترسی؛ بوم این دو رابطه را در یک قاب کنار هم می‌گذارد. برای تحلیل پویا، بوم باید با داده‌های بازار، سناریو و شاخص‌های عملکرد ترکیب شود.",
        critique_text="نقد اصلی آن است که بوم تصویری ایستا از کسب‌وکار می‌دهد و رقابت، پویایی بازار و اثرهای اجتماعی و زیست‌محیطی را در خود جای نمی‌دهد.",
        example_text="یک پادکست مستقل در بوم خود نشان می‌دهد مخاطب رایگان، ارزش پیشنهادی محتوای تخصصی، کانال توزیع پلتفرم‌های صوتی و درآمد از حمایت شنوندگان و آگهی است؛ همین قاب آشکار می‌کند وابستگی درآمد به یک پلتفرم، نقطهٔ آسیب مدل است.",
        year=2010,
    ),
    "MC-199": dict(
        summary="چارچوب اختلال اطلاعاتی، طبقه‌بندی سه‌گانه‌ای برای تحلیل اطلاعات زیان‌بار در محیط رسانه‌ای معاصر است. کلر واردل و حسین درخشان در گزارش سال ۲۰۱۷ برای شورای اروپا واژهٔ «اخبار جعلی» را نارسا دانستند و به جای آن سه مقوله را پیشنهاد کردند: اطلاعات نادرست، یعنی محتوای غلط که بدون قصد آسیب ساخته شده است؛ اطلاعات بدخواهانه، یعنی محتوای غلط که با قصد فریب و آسیب تولید و منتشر می‌شود؛ و اطلاعات گمراه‌کننده، یعنی محتوای درست که با بافت نادرست، هدف یا شیوهٔ ارائه، زیان می‌رساند. این تفکیک به سیاست‌گذار کمک می‌کند پاسخ متناسب با نوع و قصد را انتخاب کند و از یکسان‌سازی خطا و دسیسه بپرهیزد. چارچوب همچنین سه عنصر را از هم جدا می‌سازد: عامل یا فرستنده، پیام و مفسر. به همین ترتیب، سه مرحلهٔ ساخت، تولید و توزیع بررسی می‌شود، زیرا یک محتوا می‌تواند در مرحلهٔ ساخت بی‌قصد و در مرحلهٔ توزیع آگاهانه تقویت شود. هفت شکل رایج نیز در آن فهرست شده است: طنز و پارودی، محتوای گمراه‌کننده، محتوای جعلی با هویت دروغین، محتوای ساختگی، پیوند نادرست، زمینهٔ نادرست و محتوای دستکاری‌شده. کاربرد آن در راهبردهای راستی‌آزمایی، آموزش سواد رسانه‌ای، سیاست‌گذاری پلتفرم و تحلیل کمپین‌های اطلاعاتی گسترده است. نقد اصلی به چارچوب، دشواری اثبات قصد، ساده‌سازی طیف خاکستری میان خطا و فریب و کم‌توجهی به انگیزه‌های اقتصادی توجه است.",
        definition="اختلال اطلاعاتی وضعیتی است که در آن اطلاعات نادرست، بدخواهانه یا گمراه‌کننده در نظام رسانه‌ای منتشر می‌شود و توانایی مخاطب در تشخیص، اعتماد و تصمیم‌گیری را مختل می‌سازد.",
        main_problem="چگونه می‌توان انواع مختلف اطلاعات زیان‌بار را بر پایهٔ درستی محتوا و قصد عامل از یکدیگر تفکیک کرد تا پاسخ سیاستی و رسانه‌ای متناسب و متناسب با خطر باشد.",
        mechanism="یک محتوا در مرحلهٔ ساخت شکل می‌گیرد، در مرحلهٔ تولید با قالب رسانه‌ای بازسازی می‌شود و در مرحلهٔ توزیع از طریق شبکه‌های اجتماعی، رسانه‌های خبری و واسطه‌ها گسترش می‌یابد. مفسران با پیش‌داوری و بافت خود، معنا و اثر محتوا را تغییر می‌دهند.",
        assumptions=[
            "درستی محتوا و قصد عامل دو بعد مستقل برای طبقه‌بندی‌اند.",
            "واژهٔ فراگیر «اخبار جعلی» برای تحلیل دقیق ناکافی است.",
            "نوع اختلال، راهبرد پاسخ مناسب را تعیین می‌کند.",
            "مراحل ساخت، تولید و توزیع را می‌توان جداگانه تحلیل کرد.",
        ],
        principles=[
            "خطای بی‌قصد و فریب آگاهانه یکسان نیستند و پاسخ یکسان نمی‌طلبند.",
            "محتوای درست نیز با بافت یا قالب نادرست می‌تواند زیان برساند.",
            "عامل، پیام و مفسر سه واحد تحلیلی جداگانه‌اند.",
            "درستی‌آزمایی باید متناسب با شکل اختلال و مرحلهٔ آن طراحی شود.",
        ],
        critiques=[
            "اثبات قصد عامل در عمل دشوار و اغلب استنتاجی است.",
            "تفکیک سه‌گانه، طیف خاکستری انگیزه‌های ترکیبی را ساده می‌کند.",
            "انگیزه‌های اقتصادی مدل توجه و تبلیغات کمتر تحلیل شده است.",
            "مفهوم اختلال می‌تواند در دسترس تفسیرهای سیاسی قرار گیرد.",
        ],
        applications=[
            "طراحی پروتکل راستی‌آزمایی برای تحریریه‌ها و سازمان‌های خبری.",
            "آموزش سواد رسانه‌ای برای تشخیص زمینهٔ نادرست و دستکاری.",
            "سیاست‌گذاری پلتفرم برای برچسب‌گذاری و کاهش انتشار محتوای زیان‌بار.",
            "تحلیل کمپین‌های اطلاعاتی و روایت‌های هماهنگ در بحران‌ها.",
        ],
        evolution="پس از بحث‌های سال ۲۰۱۶ دربارهٔ اخبار جعلی، واردل و درخشان (۲۰۱۷) چارچوب سه‌گانه را برای شورای اروپا تدوین کردند؛ واژه‌نامهٔ ۲۰۱۸ آن را عملیاتی کرد و پژوهش‌های بعدی، آن را به تحلیل رسانه‌های اجتماعی، هوش مصنوعی مولد و روایت‌های بحران گستردند.",
        key_concepts=[
            "اطلاعات نادرست (Misinformation)",
            "اطلاعات بدخواهانه (Disinformation)",
            "اطلاعات گمراه‌کننده (Malinformation)",
            "زمینهٔ نادرست (False Context)",
            "محتوای دستکاری‌شده (Manipulated Content)",
        ],
        theorists="کلر واردل؛ حسین درخشان",
        theorists_text="واردل و درخشان (۲۰۱۷)",
        model="عامل → پیام → مفسر؛ در سه مرحلهٔ ساخت، تولید و توزیع؛ با سه نوع نادرست، بدخواهانه و گمراه‌کننده.",
        studies=[
            "واردل و درخشان (۲۰۱۷) سه‌گانهٔ اختلال و هفت شکل رایج آن را در گزارش شورای اروپا مستند کردند.",
            "واژه‌نامهٔ ۲۰۱۸ مفاهیم را برای استفادهٔ مشترک پژوهشگران و سیاست‌گذاران عملیاتی ساخت.",
        ],
        detailed_analysis="تحلیل عمیق نشان می‌دهد ارزش اصلی چارچوب در جداکردن دو پرسش است: آیا محتوا نادرست است و آیا قصد آسیب وجود دارد. پاسخ به این دو پرسش، چهار وضعیت ممکن می‌سازد که تنها سه‌تای آن در چارچوب نام‌گذاری شده است. در عمل، بسیاری از موارد ترکیبی‌اند: محتوای درست با قصد فریب منتشر می‌شود یا محتوای نادرست بی‌قصد در شبکه‌ای هماهنگ تقویت می‌گردد. از این رو تحلیل دقیق نیازمند بررسی زنجیرهٔ توزیع و منافع بازیگران است، نه فقط داوری دربارهٔ یک پیام منفرد.",
        critique_text="نقد اصلی آن است که اثبات قصد عامل در عمل دشوار است و تفکیک سه‌گانه، طیف خاکستری انگیزه‌های ترکیبی و انگیزه‌های اقتصادی مدل توجه را ساده می‌کند.",
        example_text="ویدئویی واقعی از یک اعتراض در شهر دیگر با عنوانی منتشر می‌شود که آن را به شهر مخاطب نسبت می‌دهد؛ محتوا درست است اما زمینه نادرست دارد و نمونهٔ روشنی از اطلاعات گمراه‌کننده به شمار می‌رود.",
        year=2017,
    ),
    "MC-221": dict(
        summary="بوم‌شناسی رسانه چارچوبی است که رسانه‌ها را نه ابزار انتقال پیام، بلکه محیط‌هایی می‌داند که ادراک حسی، ساختار اجتماعی و فرهنگ انسانی را شکل می‌دهند. مارشال مک‌لوهان در کتاب شناخت رسانه (۱۹۶۴) رسانه را امتداد حواس و توانایی‌های انسان خواند و اعلام کرد که پیام واقعی هر رسانه، تغییر مقیاس، سرعت و الگوی تعاملات انسانی است. نیل پستمن اصطلاح بوم‌شناسی رسانه را در سخنرانی سال ۱۹۶۸ به کار برد و در مقاله‌ای در سال ۱۹۷۰ آن را چنین تعریف کرد: مطالعهٔ رسانه به‌عنوان محیط. در این نگاه، هر رسانه بستری است که در آن، الگوهای فکر، زبان، نهاد و ارزش شکل می‌گیرد و رسانه‌های نو، محیط‌های تازه‌ای می‌سازند که رسانه‌های پیشین را بازآرایی می‌کنند. مکتب تورنتو با اینس، مک‌لوهان و اونگ و سپس برنامهٔ بوم‌شناسی رسانه در دانشگاه نیویورک به رهبری پستمن، این سنت را بسط دادند. چارچوب سه پرسش کانونی دارد: رسانه چه کاری با ما می‌کند، چه چیزی را ممکن و چه چیزی را ناممکن می‌سازد، و چگونه تعادل حواس و نهادها را جابه‌جا می‌کند. کاربرد آن در تحلیل محیط‌های پلتفرمی، آموزش سواد رسانه‌ای، مطالعهٔ تغییر شکل توجه و نقد فناوری‌محوری آموزش است. نقد اصلی به این چارچوب، گرایش به جبر فناورانه، ابهام استعارهٔ محیط و کم‌توجهی به عاملیت مخاطب و اقتصاد سیاسی رسانه است.",
        definition="بوم‌شناسی رسانه مطالعهٔ رسانه‌ها به‌عنوان محیط‌هایی است که ساختار ادراک، تعامل اجتماعی و فرهنگ را شکل می‌دهند و نه صرفاً مجراهای انتقال محتوا.",
        main_problem="چگونه می‌توان اثر رسانه را نه در محتوای پیام، بلکه در تغییر ساختار محیط ارتباطی، مقیاس تعامل و الگوی حواس انسان تشخیص داد و تحلیل کرد.",
        mechanism="هر رسانه با سرعت، مقیاس و قالب خاص خود، نسبت حواس را جابه‌جا می‌کند؛ این جابه‌جایی، الگوهای توجه، حافظه و سازمان اجتماعی را تغییر می‌دهد و رسانه‌های نو، محیط تازه‌ای می‌سازند که رسانه‌های قدیم در آن بازتعریف می‌شوند.",
        assumptions=[
            "رسانه محیط است، نه فقط وسیلهٔ انتقال پیام.",
            "قالب و سرعت رسانه، مستقل از محتوا اثر می‌گذارد.",
            "تغییر رسانه، نسبت حواس و ساختار اجتماعی را دگرگون می‌کند.",
            "رسانه‌های نو، رسانه‌های پیشین را حذف نمی‌کنند بلکه بازآرایی می‌کنند.",
        ],
        principles=[
            "پیام هر رسانه، خود آن رسانه و تغییر مقیاس و سرعتی است که می‌آفریند.",
            "محتوا همیشه رسانهٔ دیگری است؛ تحلیل باید در سطح محیط انجام شود.",
            "هر محیط رسانه‌ای، امکان‌ها و محدودیت‌های خاص خود را دارد.",
            "سواد رسانه‌ای یعنی شناخت محیط، نه فقط نقد پیام.",
        ],
        critiques=[
            "چارچوب به جبر فناورانه نزدیک می‌شود و عاملیت انسانی را کم‌رنگ می‌کند.",
            "استعارهٔ محیط مبهم است و سنجش تجربی اثر آن دشوار است.",
            "اقتصاد سیاسی، مالکیت و قدرت رسانه در تحلیل کم‌تر دیده می‌شود.",
            "تمایز میان اثر قالب و اثر محتوا در عمل به‌سختی قابل تفکیک است.",
        ],
        applications=[
            "تحلیل اثر محیط پلتفرمی بر توجه، حافظه و گفت‌وگوی عمومی.",
            "طراحی برنامهٔ سواد رسانه‌ای با تمرکز بر قالب و محیط.",
            "نقد فناوری‌محوری در سیاست‌گذاری آموزش دیجیتال.",
            "مطالعهٔ تاریخی گذار رسانه‌ها و بازآرایی نهادهای اجتماعی.",
        ],
        evolution="مکتب تورنتو با اینس و مک‌لوهان بنیان گذاشته شد؛ پستمن اصطلاح را در ۱۹۶۸ به کار برد و در ۱۹۷۰ منتشر کرد؛ برنامهٔ دانشگاه نیویورک آن را به رشتهٔ دانشگاهی تبدیل کرد و انجمن بوم‌شناسی رسانه در ۱۹۹۸ شکل گرفت.",
        key_concepts=[
            "رسانه به‌عنوان محیط (Media as Environment)",
            "امتداد حواس (Extensions of Man)",
            "نسبت حواس (Sensory Ratio)",
            "رسانهٔ نو، محیط نو (New Medium, New Environment)",
            "سواد رسانه‌ای محیطی (Environmental Media Literacy)",
        ],
        theorists="مارشال مک‌لوهان؛ نیل پستمن؛ هارولد اینس؛ والتر اونگ",
        theorists_text="مک‌لوهان (۱۹۶۴)؛ پستمن (۱۹۶۸ و ۱۹۷۰)",
        model="رسانه → تغییر مقیاس و سرعت تعامل → جابه‌جایی نسبت حواس → دگرگونی نهاد و فرهنگ.",
        studies=[
            "مک‌لوهان (۱۹۶۴) رسانه را امتداد حواس و پیام آن را تغییر مقیاس تعامل تعریف کرد.",
            "پستمن (۱۹۷۰) بوم‌شناسی رسانه را مطالعهٔ رسانه به‌عنوان محیط صورت‌بندی کرد.",
        ],
        detailed_analysis="تحلیل عمیق نشان می‌دهد پرسش بوم‌شناختی با پرسش محتوایی تفاوت بنیادی دارد: پژوهش محتوایی می‌پرسد چه پیامی منتقل شد، اما پژوهش بوم‌شناختی می‌پرسد چه نوع انسان و چه نوع جامعه‌ای در این محیط پرورش می‌یابد. در محیط پلتفرمی، الگوریتم‌ها و رابط‌ها همان نقش محیط را بازی می‌کنند: سرعت بازخورد، سنجه‌های عمومی توجه و قالب کوتاه، الگوهای بیان را شکل می‌دهند. از این رو تحلیل بوم‌شناختی مکمل اقتصاد سیاسی و مطالعات مخاطب است، نه جانشین آن‌ها.",
        critique_text="نقد اصلی آن است که چارچوب به جبر فناورانه نزدیک می‌شود، استعارهٔ محیط را مبهم نگه می‌دارد و نقش اقتصاد سیاسی و عاملیت مخاطب را کم‌رنگ می‌کند.",
        example_text="گسترش پیام‌رسان‌های کوتاه در یک سازمان، پیش از هر تغییری در محتوای پیام‌ها، سرعت تصمیم‌گیری و الگوی توجه کارکنان را دگرگون می‌کند؛ همین تغییر محیطی، نمونهٔ موردنظر بوم‌شناسی رسانه است.",
        year=1964,
    ),
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


NAME_FIX = {}
YEAR_FIX = {}


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
                                       "verified": n_verified, "batch": 119}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH119 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
