# -*- coding: utf-8 -*-
"""Batch 209: MC-175, MC-185, MC-230, MC-235, MC-244 (MODEL)."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch209-20261117"
NOW = "2026-11-17 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch209.json"

S = {
    "MC-175": [
        dict(kind="BOOK",
             title_en="Perspectives on Experience",
             title_fa="چشم‌اندازهایی دربارهٔ تجربه",
             authors="Boston Consulting Group; Bruce D. Henderson", year=1968,
             publisher="Boston Consulting Group",
             doi=None,
             url=None,
             language="en", isbn=None,
             citation="Boston Consulting Group. (1968). Perspectives on Experience. Boston: Boston Consulting Group.",
             locator="experience curve chapters",
             locator_type="CHAPTER",
             supports="constant percentage unit-cost decline with each doubling of cumulative output",
             verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Application and Misapplication of the Experience Curve",
             title_fa="کاربرد و کاربرد نادرست منحنی تجربه",
             authors="Bruce D. Henderson", year=1984,
             publisher="Journal of Business Strategy",
             doi="10.1108/eb039027",
             url="https://www.emerald.com/jbs/article/4/3/3/207072/THE-APPLICATION-AND-MISAPPLICATION-OF-THE",
             language="en", isbn=None,
             citation="Henderson, B. D. (1984). The application and misapplication of the experience curve. Journal of Business Strategy, 4(3), 3-9. https://doi.org/10.1108/eb039027",
             locator="4(3), 3-9",
             locator_type="PAGE",
             supports="limits and misuses of experience-curve strategy",
             verified=True),
    ],
    "MC-185": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Stability in Competition",
             title_fa="پایداری در رقابت",
             authors="Harold Hotelling", year=1929,
             publisher="The Economic Journal",
             doi=None,
             url="https://www.math.toronto.edu/mccann/assignments/477/Hotelling29.pdf",
             language="en", isbn=None,
             citation="Hotelling, H. (1929). Stability in competition. The Economic Journal, 39(153), 41-57.",
             locator="39(153), 41-57",
             locator_type="PAGE",
             supports="spatial competition and the principle of minimum differentiation",
             verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="On Hotelling's 'Stability in Competition'",
             title_fa="دربارهٔ «پایداری در رقابت» هتلینگ",
             authors="Claude d'Aspremont; Jean Jaskold Gabszewicz; Jacques-François Thisse", year=1979,
             publisher="Econometrica",
             doi=None,
             url="https://www.econometricsociety.org/publications/econometrica/1979/09/01/hotellings-stability-competition",
             language="en", isbn=None,
             citation="d'Aspremont, C., Gabszewicz, J. J., & Thisse, J.-F. (1979). On Hotelling's 'Stability in competition'. Econometrica, 47(5), 1145-1150.",
             locator="47(5), 1145-1150",
             locator_type="PAGE",
             supports="non-existence of pure-strategy equilibrium under linear transport costs",
             verified=True),
    ],
    "MC-230": [
        dict(kind="BOOK_CHAPTER",
             title_en="The Relevance of Algorithms",
             title_fa="اهمیت الگوریتم‌ها",
             authors="Tarleton Gillespie", year=2014,
             publisher="MIT Press",
             doi="10.7551/mitpress/9780262525374.003.0009",
             url="https://direct.mit.edu/books/edited-volume/3021/chapter/82555/The-Relevance-of-Algorithms",
             language="en", isbn=None,
             citation="Gillespie, T. (2014). The relevance of algorithms. In T. Gillespie, P. J. Boczkowski, & K. A. Foot (Eds.), Media Technologies: Essays on Communication, Materiality, and Society (pp. 167-194). Cambridge, MA: MIT Press. https://doi.org/10.7551/mitpress/9780262525374.003.0009",
             locator="pp. 167-194",
             locator_type="PAGE",
             supports="algorithms as public relevance machines shaping information ecosystems",
             verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Accountable Algorithms",
             title_fa="الگوریتم‌های پاسخ‌گو",
             authors="Joshua A. Kroll; Joanna Huey; Solon Barocas; Edward W. Felten; Joel R. Reidenberg; David G. Robinson; Harlan Yu", year=2017,
             publisher="University of Pennsylvania Law Review",
             doi=None,
             url="https://pennlawreview.com/2017/02/23/accountable-algorithms/",
             language="en", isbn=None,
             citation="Kroll, J. A., Huey, J., Barocas, S., Felten, E. W., Reidenberg, J. R., Robinson, D. G., & Yu, H. (2017). Accountable algorithms. University of Pennsylvania Law Review, 165(3), 633-705.",
             locator="165(3), 633-705",
             locator_type="PAGE",
             supports="procedural and technical mechanisms for algorithmic accountability",
             verified=True),
    ],
    "MC-235": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Latent Dirichlet Allocation",
             title_fa="تخصیص نهفتهٔ دیریکله",
             authors="David M. Blei; Andrew Y. Ng; Michael I. Jordan", year=2003,
             publisher="Journal of Machine Learning Research",
             doi=None,
             url="https://www.jmlr.org/papers/volume3/blei03a/blei03a.pdf",
             language="en", isbn=None,
             citation="Blei, D. M., Ng, A. Y., & Jordan, M. I. (2003). Latent Dirichlet allocation. Journal of Machine Learning Research, 3, 993-1022.",
             locator="3, 993-1022",
             locator_type="PAGE",
             supports="three-level hierarchical generative model of documents and topics",
             verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Probabilistic Topic Models",
             title_fa="مدل‌های موضوعی احتمالاتی",
             authors="David M. Blei", year=2012,
             publisher="Communications of the ACM",
             doi="10.1145/2133806.2133826",
             url="https://dl.acm.org/doi/10.1145/2133806.2133826",
             language="en", isbn=None,
             citation="Blei, D. M. (2012). Probabilistic topic models. Communications of the ACM, 55(4), 77-84. https://doi.org/10.1145/2133806.2133826",
             locator="55(4), 77-84",
             locator_type="PAGE",
             supports="survey of inference and evaluation for topic models",
             verified=True),
    ],
    "MC-244": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Computer-Mediated Communication: Impersonal, Interpersonal, and Hyperpersonal Interaction",
             title_fa="ارتباط با واسطهٔ رایانه: تعامل غیرشخصی، میان‌فردی و ابرشخصی",
             authors="Joseph B. Walther", year=1996,
             publisher="Communication Research",
             doi="10.1177/009365096023001001",
             url="https://journals.sagepub.com/doi/10.1177/009365096023001001",
             language="en", isbn=None,
             citation="Walther, J. B. (1996). Computer-mediated communication: Impersonal, interpersonal, and hyperpersonal interaction. Communication Research, 23(1), 3-43. https://doi.org/10.1177/009365096023001001",
             locator="23(1), 3-43",
             locator_type="PAGE",
             supports="hyperpersonal model of selective self-presentation and idealized perception",
             verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Selective Self-Presentation in Computer-Mediated Communication: Hyperpersonal Dimensions of Technology, Language, and Cognition",
             title_fa="خودارائه‌گری گزینشی در ارتباط با واسطهٔ رایانه: ابعاد ابرشخصی فناوری، زبان و شناخت",
             authors="Joseph B. Walther", year=2007,
             publisher="Computers in Human Behavior",
             doi=None,
             url="https://smg.media.mit.edu/library/Walther_2007_Computers-in-Human-Behavior.pdf",
             language="en", isbn=None,
             citation="Walther, J. B. (2007). Selective self-presentation in computer-mediated communication: Hyperpersonal dimensions of technology, language, and cognition. Computers in Human Behavior, 23(5), 2538-2557.",
             locator="23(5), 2538-2557",
             locator_type="PAGE",
             supports="technology, language and cognition as hyperpersonal mechanisms",
             verified=True),
    ],
}

ENRICH = {
    "MC-175": dict(
        needs_enrichment=False,
        level="میان",
        related_approaches="راهبرد هزینه؛ منحنی یادگیری؛ مدیریت راهبردی؛ اقتصاد مقیاس؛ چرخهٔ عمر محصول.",
        core_logic=("با هر دو برابر شدن تولید تجمعی، هزینهٔ واحد به درصدی ثابت کاهش می‌یابد، زیرا یادگیری، بهبود فرایند و صرفه‌جویی مقیاس هم‌زمان فعال می‌شوند. "
                    "بنگاهی که سریع‌تر حجم می‌گیرد، زودتر از این کاهش هزینه بهره می‌برد و می‌تواند قیمت را پایین آورد و سهم بازار را تثبیت کند. "
                    "این چرخه، مزیت هزینه‌ای را به سهم بازار پیوند می‌زند، اما شیب آن میان صنایع متفاوت است و بیش از حد تعمیم‌پذیر نیست."),
        recommended_sources="«چشم‌اندازهایی دربارهٔ تجربه» (گروه مشاوران بوستون، ۱۹۶۸)؛ «کاربرد و کاربرد نادرست منحنی تجربه» (هندرسون، ۱۹۸۴)؛ «بازنگری در آموزهٔ منحنی تجربه» (آلبرتس، ۱۹۸۹).",
        detailed_analysis=("۱. بنیان و منطق نظری\nمنحنی تجربه در سال ۱۹۶۸ از سوی گروه مشاوران بوستون و بروس هندرسون صورت‌بندی شد. "
                           "مشاهدهٔ تجربی این بود که در بسیاری از صنایع، هزینهٔ واحد با افزایش تولید تجمعی به درصدی ثابت کاهش می‌یابد — معمولاً ده تا سی درصد با هر دو برابر شدن تولید. "
                           "منبع این کاهش، ترکیبی از یادگیری کارکنان، بهبود فرایند، بازطراحی محصول و صرفه‌جویی مقیاس است.\n\n"
                           "۲. ساختارهای مفهومی\nتولید تجمعی، هزینهٔ واحد، شیب منحنی و سهم بازار چهار سازهٔ اصلی‌اند. "
                           "شیب منحنی، سرعت یادگیری صنعت را نشان می‌دهد و سهم بازار، سنجهٔ نزدیک به انباشت تجربه است.\n\n"
                           "۳. نمونه‌های تحلیلی\nدر صنایع تولیدی با حجم بالا، پیشروی بازار می‌تواند با قیمت‌گذاری تهاجمی حجم را سریع‌تر بالا ببرد و از رقیب عقب‌مانده فاصلهٔ هزینه‌ای بگیرد؛ اما همین راهبرد در صنایعی که تمایز برند یا نوآوری سریع تعیین‌کننده است، به رقابت مخرب قیمتی می‌انجامد.\n\n"
                           "۴. نقدها و چالش‌ها\nشیب منحنی میان صنایع و بنگاه‌ها بسیار متفاوت است؛ تمرکز افراطی بر سهم بازار می‌تواند سود کوتاه‌مدت را قربانی کند؛ مرزهای یادگیری فناورانه و اثر جهش‌های فناورانه نادیده گرفته می‌شود؛ و خطر رقابت مخرب قیمتی جدی است. "
                           "در اقتصاد دیجیتال نیز شبکه‌اثر و هزینهٔ نزدیک به صفر توزیع، منطق منحنی را دگرگون کرده است.\n\n"
                           "۵. سیر تاریخی\nگزارش ۱۹۶۸ منحنی را به ابزار راهبردی تبدیل کرد، پژوهش‌های دههٔ ۱۹۷۰ آن را در صنایع مختلف آزمودند و هندرسون (۱۹۸۴) حدود کاربرد و کژکاربرد آن را روشن کرد.\n\n"
                           "۶. جایگاه در بحث روز\nدر اقتصاد پلتفرمی، منحنی تجربه به منحنی داده و یادگیری الگوریتمی پیوند خورده است؛ مزیت هزینه‌ای اکنون از انباشت داده و بهبود مدل می‌آید، هرچند خطر تمرکز بازار شدیدتر شده است."),
    ),
    "MC-185": dict(
        needs_enrichment=False,
        level="میان",
        related_approaches="اقتصاد صنعتی؛ رقابت انحصاری؛ نظریهٔ مکان‌یابی؛ تمایز محصول؛ اقتصاد پلتفرم.",
        core_logic=("در بازار خطی، هر فروشنده با جابه‌جایی به سمت مرکز، مشتریان حاشیه‌ای بیشتری جذب می‌کند و رقیب نیز همین کار را می‌کند. "
                    "نتیجه، هم‌گرایی به مرکز و کاهش تنوع است؛ اما با هزینهٔ حمل‌ونقل خطی، تعادل خالص وجود ندارد و مدل نیازمند بازنگری است."),
        recommended_sources="«پایداری در رقابت» (هتلینگ، ۱۹۲۹)؛ «دربارهٔ پایداری در رقابت هتلینگ» (دآسپرمون، گابشویچ و تیس، ۱۹۷۹)؛ پژوهش‌های تمایز محصول و اقتصاد پلتفرم.",
        detailed_analysis=("۱. بنیان و منطق نظری\nهتلینگ (۱۹۲۹) رقابت دو فروشنده را در یک شهر خطی تحلیل کرد که مشتریان به‌طور یکنواخت توزیع شده‌اند و به نزدیک‌ترین فروشنده مراجعه می‌کنند. "
                           "او استدلال کرد جست‌وجوی سهم بازار، فروشندگان را به مرکز می‌کشاند و اصل تمایز حداقلی را صورت‌بندی کرد.\n\n"
                           "۲. ساختارهای مفهومی\nفضای خطی، هزینهٔ حمل‌ونقل، موقعیت فروشنده، سهم بازار و تمایز مکانی سازه‌های اصلی‌اند. "
                           "بعدها تمایز عمودی (کیفیت و برند) و بازارهای چندبُعدی به مدل افزوده شد.\n\n"
                           "۳. نمونه‌های تحلیلی\nهم‌گرایی قالب‌های رسانه‌ای و شباهت فزایندهٔ برنامه‌های شبکه‌های رقیب، نمونهٔ روشنی از منطق هتلینگ است: هر شبکه با حرکت به سمت محتوای پرطرفدار میانی، مخاطب بیشتری جذب می‌کند و در نتیجه تنوع کم می‌شود.\n\n"
                           "۴. نقدها و چالش‌ها\nدآسپرمون، گابشویچ و تیس (۱۹۷۹) نشان دادند با هزینهٔ حمل‌ونقل خطی، تعادل خالص وجود ندارد؛ فضای خطی ساده‌سازی واقعیت است؛ تمایز عمودی و برند نادیده می‌ماند؛ یکنواختی مشتریان واقع‌گرایانه نیست؛ و برای بازارهای چندبُعدی و پلتفرمی کافی نیست.\n\n"
                           "۵. سیر تاریخی\nمدل در ۱۹۲۹ معرفی شد، در ۱۹۷۹ با نقد تعادل بازنگری شد و در دهه‌های بعد در اقتصاد رسانه، تمایز محصول و اقتصاد پلتفرم به‌کار رفت.\n\n"
                           "۶. جایگاه در بحث روز\nدر پلتفرم‌های دوسویه، تمایز مکانی به تمایز در طراحی و الگوریتم تبدیل شده است؛ منطق هم‌گرایی هتلینگ هنوز هم‌گرایی قالب و محتوا را توضیح می‌دهد."),
    ),
    "MC-230": dict(
        needs_enrichment=False,
        level="کلان",
        related_approaches="پاسخگویی الگوریتمی؛ نظم پلتفرم؛ اخلاق هوش مصنوعی؛ سیاست شفافیت؛ جامعه‌شناسی الگوریتم.",
        core_logic=("الگوریتم‌ها با معیارهای پنهان، محتوا و کاربران را رتبه‌بندی، فیلتر و تعدیل می‌کنند و از این راه قدرت عمومی اعمال می‌کنند. "
                    "حاکمیت الگوریتمی با ابزارهای ثبت، ممیزی، توضیح‌پذیری و بازبینی انسانی، این معیارها و پیامدها را در معرض بررسی قرار می‌دهد و سازوکار شکایت و اصلاح می‌سازد."),
        recommended_sources="«اهمیت الگوریتم‌ها» (گیلسپی، ۲۰۱۴)؛ «الگوریتم‌های پاسخ‌گو» (کرول و همکاران، ۲۰۱۷)؛ «پاسخگویی الگوریتمی» (دیاکوپولوس، ۲۰۱۵).",
        detailed_analysis=("۱. بنیان و منطق نظری\nگیلسپی (۲۰۱۴) نشان داد الگوریتم‌ها ماشین‌های اهمیت عمومی‌اند: تعیین می‌کنند چه چیزی دیده شود، چه چیزی معتبر تلقی شود و چه چیزی در حاشیه بماند. "
                           "از این منظر، الگوریتم صرفاً ابزار فنی نیست، بلکه نهادی است که هنجار و قدرت را بازتولید می‌کند. "
                           "کرول و همکاران (۲۰۱۷) در چارچوب حقوقی، سازوکارهای رویه‌ای و فنی پاسخ‌گویی را صورت‌بندی کردند.\n\n"
                           "۲. ساختارهای مفهومی\nپاسخ‌گویی، شفافیت، ممیزی، توضیح‌پذیری، مرتبط‌سازی و بازبینی انسانی شش سازهٔ اصلی‌اند. "
                           "مرتبط‌سازی، معیار اهمیت را می‌سازد و ممیزی، صحت و انصاف آن را می‌سنجد.\n\n"
                           "۳. نمونه‌های تحلیلی\nدر توزیع خبر، الگوریتم مرتبط‌سازی می‌تواند یک جریان سیاسی را به‌طور نظام‌مند کم‌نمایش دهد؛ حاکمیت الگوریتمی با ثبت تصمیم‌ها، ممیزی بیرونی و مسیر شکایت، این کم‌نمایش را قابل اثبات و اصلاح می‌کند.\n\n"
                           "۴. نقدها و چالش‌ها\nپاسخ‌گویی فنی بدون توجه به قدرت سیاسی ناکافی است؛ خطر شست‌وشوی حاکمیتی و پاسخ‌گویی نمایشی وجود دارد؛ ممیزی الگوریتم‌های بسته از بیرون دشوار است؛ معیارهای پاسخ‌گویی میان حوزه‌ها یکدست نیست؛ و هزینهٔ انطباق می‌تواند به مانع ورود تبدیل شود.\n\n"
                           "۵. سیر تاریخی\nگیلسپی (۲۰۱۴) اهمیت عمومی الگوریتم‌ها را تحلیل کرد، کرول و همکاران (۲۰۱۷) سازوکارهای پاسخ‌گویی را صورت‌بندی کردند و پژوهش‌های مقرراتی، حاکمیت الگوریتمی را به قانون خدمات دیجیتال و مقررات هوش مصنوعی پیوند زدند.\n\n"
                           "۶. جایگاه در بحث روز\nبا فراگیرشدن مدل‌های زبانی، پرسش حاکمیت از رتبه‌بندی به تولید و بازنمایی محتوا گسترش یافته است و حاکمیت الگوریتمی به یکی از محورهای اصلی سیاست رسانه تبدیل شده است."),
    ),
    "MC-235": dict(
        needs_enrichment=False,
        theorists_text="دیوید بلی، اندرو نگ و مایکل جردن",
        level="روش",
        related_approaches="تحلیل محتوای خودکار؛ پردازش زبان طبیعی؛ تحلیل شبکهٔ معنایی؛ یادگیری ماشین؛ روش‌های محاسباتی ارتباطات.",
        core_logic=("هر سند ترکیبی از چند موضوع پنهان و هر موضوع توزیعی از واژه‌هاست. "
                    "با تحلیل هم‌رخدادی واژه‌ها، توزیع‌هایی یافت می‌شود که احتمال مشاهدهٔ مجموعهٔ متن را بیشینه می‌کند؛ نتیجه، موضوع‌های اصلی و وزن آن‌ها در هر سند است."),
        recommended_sources="«تخصیص نهفتهٔ دیریکله» (بلی، نگ و جردن، ۲۰۰۳)؛ «مدل‌های موضوعی احتمالاتی» (بلی، ۲۰۱۲)؛ مرورهای روش‌شناختی مدل‌سازی موضوعی در پژوهش ارتباطات.",
        detailed_analysis=("۱. بنیان و منطق نظری\nبلی، نگ و جردن (۲۰۰۳) مدل تخصیص نهفتهٔ دیریکله را به‌عنوان مدلی مولد سه‌سطحی معرفی کردند: مجموعهٔ اسناد، توزیع موضوع در سند و توزیع واژه در موضوع. "
                           "برخلاف تحلیل محتوای دستی، مدل بدون مقوله‌بندی پیشین، ساختار موضوعی را از داده استخراج می‌کند.\n\n"
                           "۲. ساختارهای مفهومی\nموضوع پنهان، توزیع سند-موضوع، توزیع موضوع-واژه و فرض کیسهٔ واژه‌ها سازه‌های بنیادین‌اند. "
                           "استنتاج تغییراتی و نمونه‌گیری گیبس دو روش رایج برآورد پارامترهاست.\n\n"
                           "۳. نمونه‌های تحلیلی\nدر پژوهش خبر، مدل می‌تواند در مجموعهٔ بزرگی از گزارش‌ها، موضوع‌هایی مانند سیاست خارجی، سلامت و ورزش را استخراج کند و سهم هر موضوع را در هر سند نشان دهد. "
                           "در تحلیل شبکه‌های اجتماعی نیز گفت‌وگوهای بزرگ را به محورهای موضوعی تقسیم می‌کند.\n\n"
                           "۴. نقدها و چالش‌ها\nفرض کیسهٔ واژه‌ها ترتیب و بافت را نادیده می‌گیرد؛ نتیجه به شمار موضوع‌ها و تنظیم‌ها حساس است؛ تفسیر موضوع‌ها ذهنی و دشوار است؛ اعتبارسنجی معیار استاندارد یکدستی ندارد؛ و برای متن‌های کوتاه و گفتار روزمره محدود است.\n\n"
                           "۵. سیر تاریخی\nمقالهٔ ۲۰۰۳ مدل را تثبیت کرد، بلی (۲۰۱۲) مروری بر استنتاج و ارزیابی ارائه داد و مدل‌های موضوعی بعدی با اطلاعات زمانی، شبکه‌ای و عصبی گسترش یافتند.\n\n"
                           "۶. جایگاه در بحث روز\nبا رشد مدل‌های زبانی بزرگ، مدل‌سازی موضوعی به‌عنوان روش تفسیرپذیر و کم‌هزینه در کنار روش‌های عصبی جای خود را حفظ کرده است، به‌ویژه در پژوهش‌هایی که شفافیت روش اهمیت دارد."),
    ),
    "MC-244": dict(
        needs_enrichment=False,
        level="میان",
        constructs=("• عرضهٔ گزینشی خود: ارائهٔ نسخهٔ ویرایش‌شده و بهینه‌شدهٔ خود در کانال.\n"
                    "• آرمانی‌سازی گیرنده: ساختن تصویری مطلوب از طرف مقابل با اطلاعات کم.\n"
                    "• ناهمزمانی کانال: فرصت تأمل، ویرایش و بازنگری پیام.\n"
                    "• بازخورد تقویتی: چرخهٔ تأیید متقابل که تصویر آرمانی را تقویت می‌کند.\n"
                    "• تأیید رفتاری: هم‌سو شدن رفتار با تصویری که دیگری ساخته است."),
        related_approaches="ارتباط با واسطهٔ رایانه؛ خودارائه‌گری؛ نظریهٔ حضور اجتماعی؛ مدل پردازش اطلاعات اجتماعی؛ روان‌شناسی رسانهٔ اجتماعی.",
        core_logic=("فرستنده با ویرایش پیام، نسخهٔ بهینهٔ خود را عرضه می‌کند؛ گیرنده با اطلاعات کم، تصویر آرمانی می‌سازد؛ بازخورد مطلوب این تصویر را تأیید و تقویت می‌کند. "
                    "این چرخهٔ تأیید متقابل می‌تواند صمیمیت و جذب را بیش از تعامل رودررو بالا ببرد."),
        recommended_sources="«ارتباط با واسطهٔ رایانه: تعامل غیرشخصی، میان‌فردی و ابرشخصی» (والتر، ۱۹۹۶)؛ «خودارائه‌گری گزینشی در ارتباط با واسطهٔ رایانه» (والتر، ۲۰۰۷)؛ پژوهش‌های قرار اینترنتی و خودارائه‌گری دیجیتال.",
        detailed_analysis=("۱. بنیان و منطق نظری\nوالتر (۱۹۹۶) مدل ابرشخصی را در واکنش به دیدگاه کاهش نشانه‌ها معرفی کرد که ارتباط با واسطه را سرد و غیرشخصی می‌دانست. "
                           "او نشان داد همان ویژگی‌های کانال — ناهمزمانی، ویرایش‌پذیری و کمبود نشانه‌های اجتماعی — می‌تواند ارتباط را از تعامل رودررو صمیمی‌تر کند.\n\n"
                           "۲. ساختارهای مفهومی\nچهار سازهٔ عرضهٔ گزینشی خود، آرمانی‌سازی گیرنده، ناهمزمانی و بازخورد تقویتی، سازوکار ابرشخصی را می‌سازند. "
                           "تأیید رفتاری، حلقهٔ نهایی است که تصویر ساخته‌شده را به رفتار تبدیل می‌کند.\n\n"
                           "۳. نمونه‌های تحلیلی\nدر قرارهای اینترنتی، پروفایل ویرایش‌شده و گفت‌وگوی ناهمزمان می‌تواند صمیمیت سریع و انتظارهای آرمانی بسازد؛ اما همین سازوکار، خطر ناامیدی در دیدار رودررو و فریب را افزایش می‌دهد.\n\n"
                           "۴. نقدها و چالش‌ها\nمدل بیشتر بر ارتباط متنی و ناهمزمان تمرکز دارد؛ انتقال صمیمیت به محیط رودررو کم‌بررسی می‌ماند؛ خطر فریب و آرمانی‌سازی نادرست کم‌رنگ می‌شود؛ برای ویدئو و ارتباط همزمان بازنگری می‌خواهد؛ و شواهد تجربی در بافت‌های فرهنگی متفاوت ناهمگون است.\n\n"
                           "۵. سیر تاریخی\nمقالهٔ ۱۹۹۶ مدل چهارمؤلفه‌ای را معرفی کرد، پژوهش‌های قرار اینترنتی آن را آزمودند و والتر (۲۰۰۷) ابعاد فناوری، زبان و شناخت را بسط داد.\n\n"
                           "۶. جایگاه در بحث روز\nدر شبکه‌های اجتماعی و آواتارها، عرضهٔ گزینشی خود به هنجار تبدیل شده است؛ مدل ابرشخصی توضیح می‌دهد چرا ارتباط دیجیتال می‌تواند هم صمیمیت شدید و هم فریب و آرمانی‌سازی نادرست تولید کند."),
    ),
}

NAME_FIX = {}

YEAR_FIX = {
    "MC-175": "year=1968 (BCG 1968); Henderson 1984 verified; removed media-economics template analysis and «پarker» recommendations",
    "MC-185": "year=1929 (Hotelling 1929); d'Aspremont et al. 1979 verified; removed media-economics template analysis and garbled recommendations",
    "MC-230": "year=2014 (Gillespie 2014); Kroll et al. 2017 verified; removed data-capitalism template analysis and unrelated recommendations",
    "MC-235": "year=2003 (Blei, Ng & Jordan 2003); Blei 2012 verified; replaced garbled template analysis and irrelevant method recommendations",
    "MC-244": "year=1996 (Walther 1996); Walther 2007 verified; replaced garbled template analysis, Latin constructs and irrelevant recommendations",
}
