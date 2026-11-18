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
                                       "verified": n_verified, "batch": 209}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH209 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
