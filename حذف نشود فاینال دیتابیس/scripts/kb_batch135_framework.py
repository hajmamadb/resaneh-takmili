# -*- coding: utf-8 -*-
"""Batch 135 (MODEL): full documentation for MC-175, MC-185, MC-225, MC-230."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch135-model-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch135_model.json"

S = {
    "MC-175": [
        dict(kind="REPORT",
             title_en="The Experience Curve",
             title_fa="منحنی تجربه",
             authors="Henderson, B. D.; Boston Consulting Group", year=1968,
             publisher="Boston Consulting Group (Perspectives on Experience)",
             doi=None,
             url="https://www.bcg.com/publications/1968/business-unit-strategy-growth-experience-curve",
             language="en", isbn=None,
             citation="Henderson, B. D. (1968). The Experience Curve. In Perspectives on Experience. Boston: Boston Consulting Group.",
             locator="Perspectives on Experience", locator_type="SECTION",
             supports="unit cost declines by a constant percentage with each doubling of cumulative output", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Diagnosing the Experience Curve",
             title_fa="تشخیص منحنی تجربه",
             authors="Day, G. S.; Montgomery, D. B.", year=1983,
             publisher="Journal of Marketing",
             doi=None, url=None, language="en", isbn=None,
             citation="Day, G. S., & Montgomery, D. B. (1983). Diagnosing the experience curve. Journal of Marketing, 47(2), 44-58.",
             locator="47(2):44-58", locator_type="page_range",
             supports="critical assessment of experience-curve strategy", verified=False),
    ],
    "MC-185": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Stability in Competition",
             title_fa="پایداری در رقابت",
             authors="Hotelling, H.", year=1929,
             publisher="The Economic Journal",
             doi="10.2307/2224214",
             url="https://www.math.toronto.edu/mccann/assignments/477/Hotelling29.pdf",
             language="en", isbn=None,
             citation="Hotelling, H. (1929). Stability in competition. The Economic Journal, 39(153), 41-57.",
             locator="39(153):41-57", locator_type="page_range",
             supports="principle of minimum differentiation in spatial duopoly", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="On Hotelling's 'Stability in Competition'",
             title_fa="دربارهٔ «پایداری در رقابت» هتلینگ",
             authors="d'Aspremont, C.; Gabszewicz, J. J.; Thisse, J.-F.", year=1979,
             publisher="Econometrica",
             doi=None, url=None, language="en", isbn=None,
             citation="d'Aspremont, C., Gabszewicz, J. J., & Thisse, J.-F. (1979). On Hotelling's 'Stability in competition'. Econometrica, 47(5), 1145-1150.",
             locator="47(5):1145-1150", locator_type="page_range",
             supports="technical critique showing non-existence of equilibrium", verified=False),
    ],
    "MC-225": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Algorithmic Culture",
             title_fa="فرهنگ الگوریتمی",
             authors="Striphas, T.", year=2015,
             publisher="European Journal of Cultural Studies",
             doi="10.1177/1367549415577392",
             url="https://journals.sagepub.com/doi/10.1177/1367549415577392",
             language="en", isbn=None,
             citation="Striphas, T. (2015). Algorithmic culture. European Journal of Cultural Studies, 18(4-5), 395-412.",
             locator="18(4-5):395-412", locator_type="page_range",
             supports="algorithms as active agents in selecting and reproducing culture", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Recommended for You: The Netflix Prize and the Production of Algorithmic Culture",
             title_fa="پیشنهادشده برای شما: جایزهٔ نتفلیکس و تولید فرهنگ الگوریتمی",
             authors="Hallinan, B.; Striphas, T.", year=2016,
             publisher="New Media & Society",
             doi=None, url=None, language="en", isbn=None,
             citation="Hallinan, B., & Striphas, T. (2016). Recommended for you: The Netflix Prize and the production of algorithmic culture. New Media & Society, 18(1), 117-137.",
             locator="18(1):117-137", locator_type="page_range",
             supports="case evidence on recommendation algorithms shaping cultural choice", verified=False),
    ],
    "MC-230": [
        dict(kind="BOOK_CHAPTER",
             title_en="The Relevance of Algorithms",
             title_fa="اهمیت الگوریتم‌ها",
             authors="Gillespie, T.", year=2014,
             publisher="MIT Press (Media Technologies)",
             doi="10.7551/mitpress/9780262525374.003.0009",
             url="https://direct.mit.edu/books/edited-volume/3021/chapter/82555/The-Relevance-of-Algorithms",
             language="en", isbn=None,
             citation="Gillespie, T. (2014). The relevance of algorithms. In T. Gillespie, P. J. Boczkowski, & K. A. Foot (Eds.), Media Technologies: Essays on Communication, Materiality, and Society (pp. 167-193). Cambridge, MA: MIT Press.",
             locator="pp. 167-193", locator_type="page_range",
             supports="algorithms as public relevance systems with contested accountability", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Accountable Algorithms",
             title_fa="الگوریتم‌های پاسخگو",
             authors="Kroll, J. A.; Huey, J.; Barocas, S.; Felten, E. W.; Reidenberg, J. R.; Robinson, D. G.; Yu, H.", year=2017,
             publisher="University of Pennsylvania Law Review",
             doi=None,
             url="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2765268",
             language="en", isbn=None,
             citation="Kroll, J. A., Huey, J., Barocas, S., Felten, E. W., Reidenberg, J. R., Robinson, D. G., & Yu, H. (2017). Accountable algorithms. University of Pennsylvania Law Review, 165(3), 633-705.",
             locator="165(3):633-705", locator_type="page_range",
             supports="technical and procedural mechanisms for algorithmic accountability", verified=True),
    ],
}

ENRICH = {
    "MC-175": dict(
        year=1968,
        summary="منحنی تجربه، چارچوبی در راهبرد هزینه است که گروه مشاوران بوستون و بروس هندرسون در سال ۱۹۶۸ در مجموعهٔ دیدگاه‌هایی دربارهٔ تجربه صورت‌بندی کردند. ادعای مرکزی این است که با هر دو برابر شدن حجم تولید تجمعی، هزینهٔ واحد محصول معمولاً به درصد ثابتی کاهش می‌یابد؛ این کاهش از یادگیری کارکنان، بهبود فرایند، صرفه‌جویی مقیاس و بهینه‌سازی طراحی برمی‌خیزد. برخلاف منحنی یادگیری که تنها بر ساعت کار و تجربهٔ تولید تمرکز داشت، منحنی تجربه همهٔ هزینه‌ها از جمله بازاریابی و سرمایه را در نظر می‌گیرد. نتیجهٔ راهبردی این است که بنگاهی که زودتر سهم بازار بیشتری به دست آورد، به هزینهٔ پایین‌تر و مزیت پایدارتری می‌رسد و می‌تواند رقبا را با قیمت پایین‌تر بیرون براند. این منطق، پایهٔ راهبردهای قیمت‌گذاری تهاجمی و رشد سهم بازار در دههٔ ۱۹۷۰ شد. در صنایع رسانه‌ای، منحنی تجربه برای تحلیل هزینهٔ تولید محتوا و اقتصاد مقیاس پلتفرم‌ها به کار رفته است. نقدهای اصلی به آن، درجهٔ بالای تنوع شیب منحنی میان صنایع، خطر تمرکز افراطی بر سهم بازار، نادیده‌گرفتن مرزهای یادگیری فناورانه و شواهد تجربی ناهمگون مربوط می‌شود.",
        definition="منحنی تجربه، رابطه‌ای است که کاهش درصدی ثابت هزینهٔ واحد را با هر دو برابر شدن تولید تجمعی پیش‌بینی می‌کند و مزیت هزینه‌ای را به سهم بازار و انباشت تجربه پیوند می‌دهد.",
        main_problem="چرا هزینهٔ واحد تولید با افزایش تجربه و حجم کاهش می‌یابد، و چگونه می‌توان این کاهش را به راهبرد قیمت و سهم بازار تبدیل کرد.",
        mechanism="افزایش تولید تجمعی، یادگیری، بهبود فرایند، صرفه‌جویی مقیاس و بازطراحی را برمی‌انگیزد؛ این عوامل هزینهٔ واحد را به درصدی ثابت کاهش می‌دهند. بنگاهی که سریع‌تر حجم می‌گیرد، در موقعیت هزینه‌ای بهتری قرار می‌گیرد و می‌تواند با قیمت پایین‌تر سهم بازار را تثبیت کند.",
        assumptions=[
            "هزینهٔ واحد با تولید تجمعی کاهش می‌یابد.",
            "شیب کاهش هزینه در محدودهٔ صنعت نسبتاً ثابت است.",
            "یادگیری و مقیاس، منابع اصلی کاهش هزینه‌اند.",
            "سهم بازار بیشتر، مزیت هزینه‌ای پایدارتر می‌آورد.",
            "راهبرد قیمت می‌تواند از مزیت هزینه‌ای بهره ببرد.",
        ],
        principles=[
            "هزینه را باید در برابر تولید تجمعی و نه فقط زمان تحلیل کرد.",
            "کاهش هزینه از یادگیری، فرایند و مقیاس می‌آید.",
            "سهم بازار زودهنگام، مزیت هزینه‌ای می‌سازد.",
            "قیمت‌گذاری تهاجمی می‌تواند رقبا را بیرون براند.",
            "شیب منحنی را باید برای هر صنعت جداگانه سنجید.",
            "مزیت هزینه‌ای بدون کیفیت و نوآوری پایدار نیست.",
        ],
        critiques=[
            "شیب منحنی میان صنایع و بنگاه‌ها بسیار متفاوت است.",
            "تمرکز افراطی بر سهم بازار می‌تواند به قیمت سود کوتاه‌مدت تمام شود.",
            "مرزهای یادگیری فناورانه نادیده گرفته می‌شود.",
            "خطر رقابت مخرب قیمتی را افزایش می‌دهد.",
            "شواهد تجربی برای ثبات رابطه یکدست نیست.",
        ],
        critique_text="منتقدان می‌گویند منحنی تجربه منطق قدرتمندی برای مزیت هزینه ارائه کرد اما شیب آن در صنایع مختلف بسیار ناهمگون است و راهبردهای مبتنی بر آن می‌تواند به رقابت قیمتی مخرب و کم‌توجهی به کیفیت بینجامد. با این حال، همچنان ابزار مهمی در تحلیل هزینه و راهبرد تولید است.",
        applications=[
            "تحلیل هزینهٔ تولید محتوا و اقتصاد مقیاس رسانه.",
            "قیمت‌گذاری تهاجمی و راهبرد سهم بازار.",
            "برنامه‌ریزی ظرفیت و پیش‌بینی هزینه.",
            "ارزیابی مزیت رقابتی در صنایع تولیدی و پلتفرمی.",
            "آموزش راهبرد هزینه و مدیریت تولید.",
        ],
        example_text="یک پلتفرم پخش ویدئو با افزایش شمار مشترکان، هزینهٔ سرانهٔ زیرساخت و پشتیبانی را کاهش می‌دهد و می‌تواند با قیمت پایین‌تر رقبا را تحت فشار بگذارد؛ اما اگر افزایش مقیاس به کیفیت توصیه‌گر یا محتوا آسیب بزند، مزیت هزینه به مزیت رقابتی پایدار تبدیل نمی‌شود. منحنی تجربه این بده‌بستان را روشن می‌کند.",
        evolution="ریشهٔ منحنی در پژوهش یادگیری تولید دههٔ ۱۹۳۰ است. صورت‌بندی سال ۱۹۶۸ آن را به ابزار راهبردی تبدیل کرد و در دههٔ ۱۹۷۰ راهنمای سهم بازار شد. از دههٔ ۱۹۸۰ نقدهای تجربی و مرزهای یادگیری فناورانه، کاربرد جبری آن را محدود کرد.",
        key_concepts=["تولید تجمعی", "هزینهٔ واحد", "شیب منحنی", "یادگیری", "صرفه‌جویی مقیاس", "سهم بازار"],
        theorists="بروس هندرسون و گروه مشاوران بوستون، صورت‌بندانان منحنی تجربه.",
        theorists_text="این چارچوب در سنت مشاورهٔ راهبردی و اقتصاد تولید شکل گرفت و با تحلیل هزینه پیوند خورد.",
        model="مدل کاهش هزینه: هر دو برابر شدن تولید تجمعی، هزینهٔ واحد را به درصدی ثابت کاهش می‌دهد؛ تجربه، مقیاس و فرایند، موتور این کاهش‌اند.",
        studies=[
            "گزارش سال ۱۹۶۸ منحنی تجربه را به ابزار راهبردی تبدیل کرد.",
            "پژوهش‌های دههٔ ۱۹۷۰ آن را در صنایع مختلف آزمودند.",
            "مقالهٔ سال ۱۹۸۳ شیب و محدودیت‌های منحنی را ارزیابی کرد.",
            "مطالعات پلتفرم، اقتصاد مقیاس دیجیتال را با این منطق تحلیل کردند.",
        ],
    ),
    "MC-185": dict(
        year=1929,
        summary="مدل تمایز مکانی هتلینگ، مدلی در اقتصاد رقابت انحصاری است که هارولد هتلینگ در سال ۱۹۲۹ در مقالهٔ پایداری در رقابت در مجلهٔ اقتصادی منتشر کرد. ادعای مرکزی این است که در یک بازار خطی با مشتریان یکنواخت پراکنده و دو فروشنده، هر فروشنده با نزدیک‌شدن به مرکز می‌تواند مشتری بیشتری جذب کند؛ بنابراین هر دو به سمت مرکز حرکت می‌کنند و تمایز از میان می‌رود. این نتیجه که «اصل تمایز حداقلی» نامیده می‌شود نشان می‌دهد رقابت ممکن است محصولات را شبیه‌تر کند، نه متمایزتر. هتلینگ سپس همین منطق را به رقابت سیاسی و تنوع محصول تعمیم داد. در صنایع رسانه‌ای، مدل برای توضیح همگرایی قالب‌های برنامه‌ای، شبیه‌شدن روزنامه‌ها و هم‌گرایی مواضع رسانه‌های رقیب و نامزدهای انتخاباتی به کار رفته است. بعدها نشان داده شد که با هزینه‌های خطی حمل‌و‌نقل، تعادل خالص وجود ندارد و مدل نیازمند بازنگری فنی است. نقدهای اصلی به آن، ساده‌سازی فضای خطی، فرض یکنواختی مشتریان و نادیده‌گرفتن تمایز عمودی و ناملموس برند مربوط می‌شود.",
        definition="مدل تمایز مکانی هتلینگ، مدلی است که رقابت دو فروشنده در فضای خطی را تحلیل می‌کند و نشان می‌دهد جست‌وجوی سهم بازار، آنها را به مرکز می‌کشاند و تمایز را از میان می‌برد.",
        main_problem="چرا رقبای نزدیک به هم تمایل دارند شبیه یکدیگر شوند و در مرکز بازار تمرکز یابند، و این هم‌گرایی چه پیامدی برای مصرف‌کننده دارد.",
        mechanism="هر فروشنده با جابه‌جایی به سمت مرکز، مشتریان حاشیه‌ای بیشتری جذب می‌کند؛ رقیب نیز همین کار را می‌کند و تعادل به نزدیکی دو فروشنده در مرکز می‌انجامد. نتیجه، شباهت بیشتر محصولات و کاهش تنوع است.",
        assumptions=[
            "بازار را می‌توان روی یک خط با مشتریان یکنواخت نمایش داد.",
            "مشتری به نزدیک‌ترین فروشنده مراجعه می‌کند.",
            "دو فروشنده می‌توانند موقعیت خود را آزادانه تغییر دهند.",
            "هزینهٔ حمل‌و‌نقل خطی است.",
            "تمایز مکانی، تنها بُعد رقابت است.",
        ],
        principles=[
            "رقابت می‌تواند به هم‌گرایی و نه تمایز بینجامد.",
            "موقعیت مرکزی، سهم بازار بیشتری جذب می‌کند.",
            "هم‌گرایی محصول، تنوع را برای مصرف‌کننده کم می‌کند.",
            "مدل را می‌توان به رقابت سیاسی و رسانه‌ای تعمیم داد.",
            "تمایز عمودی و ناملموس باید جدا تحلیل شود.",
            "تعادل مدل به فرض‌های هزینه وابسته است.",
            "هم‌گرایی را باید با شواهد تجربی بازار آزمود.",
        ],
        critiques=[
            "فضای خطی، ساده‌سازی واقعیت بازار است.",
            "با هزینهٔ خطی، تعادل فنی برقرار نمی‌شود.",
            "تمایز عمودی و برند نادیده گرفته می‌شود.",
            "یکنواختی مشتریان واقع‌گرایانه نیست.",
            "برای بازارهای چندبُعدی و پلتفرمی کافی نیست.",
            "نقش هزینهٔ ورود و مقررات در موقعیت‌یابی کم‌بررسی است.",
        ],
        critique_text="منتقدان می‌گویند مدل هتلینگ شهود ارزشمندی دربارهٔ هم‌گرایی رقابتی فراهم کرد اما فرض‌های فنی آن، به‌ویژه با هزینهٔ خطی، تعادل پایدار نمی‌سازد و تمایز عمودی را کنار می‌گذارد. با این حال، همچنان چارچوب مرجع تحلیل تمایز مکانی و هم‌گرایی محصول و سیاست است.",
        applications=[
            "تحلیل هم‌گرایی قالب‌های برنامه‌سازی رسانه.",
            "توضیح شبیه‌شدن روزنامه‌ها و مواضع تحریریه.",
            "تحلیل هم‌گرایی مواضع نامزدهای انتخاباتی.",
            "طراحی تمایز محصول و جایگاه‌یابی برند.",
            "آموزش اقتصاد رقابت انحصاری و سازمان صنعت.",
        ],
        example_text="دو شبکهٔ تلویزیونی رقیب که هر یک برنامهٔ خبری ساعت هشت پخش می‌کنند، با تغییر ساعت به سمت زمان پربینندهٔ مرکزی، مخاطب بیشتری جذب می‌کنند؛ رقیب نیز همان کار را می‌کند و هر دو در یک بازهٔ زمانی مشابه متمرکز می‌شوند. مدل هتلینگ همین هم‌گرایی را توضیح می‌دهد.",
        evolution="مقالهٔ سال ۱۹۲۹ اصل تمایز حداقلی را معرفی کرد و به متن کلاسیک اقتصاد صنعتی تبدیل شد. نقد فنی سال ۱۹۷۹ تعادل مدل را به چالش کشید و نسخه‌های بعدی با هزینهٔ درجه‌دوم و تمایز عمودی بازنگری شدند.",
        key_concepts=["تمایز مکانی", "اصل تمایز حداقلی", "هم‌گرایی رقابتی", "شهر خطی", "سهم بازار", "تمایز عمودی"],
        theorists="هارولد هتلینگ، سازندهٔ مدل تمایز مکانی.",
        theorists_text="این مدل در سنت اقتصاد رقابت انحصاری و سازمان صنعت شکل گرفت.",
        model="مدل خطی: دو فروشنده و مشتریان پراکنده؛ حرکت به مرکز سهم بازار را زیاد می‌کند و تعادل به هم‌گرایی و کاهش تنوع می‌انجامد.",
        studies=[
            "مقالهٔ سال ۱۹۲۹ مدل و تعمیم سیاسی آن را معرفی کرد.",
            "نقد سال ۱۹۷۹ نبود تعادل با هزینهٔ خطی را نشان داد.",
            "مطالعات رسانه، هم‌گرایی قالب و موضع را تحلیل کردند.",
            "پژوهش‌های بازاریابی، تمایز عمودی را به مدل افزودند.",
        ],
    ),
    "MC-225": dict(
        year=2015,
        summary="فرهنگ الگوریتمی، مفهومی در مطالعات فرهنگی و رسانهٔ دیجیتال است که تد استریپاس در مقالهٔ سال ۲۰۱۵ در مجلهٔ مطالعات فرهنگی اروپا معرفی کرد. ادعای مرکزی این است که الگوریتم‌ها در تعیین اینکه چه چیزی دیده، خوانده، شنیده یا خریده شود نقش فعال دارند و بنابراین تنها ابزار فنی نیستند، بلکه بخشی از فرایند فرهنگی‌شدن به شمار می‌آیند. استریپاس با ردیابی تاریخ مفهوم فرهنگ نشان می‌دهد که فرهنگ همواره با سازوکارهای گزینش، رتبه‌بندی و انتقال پیوند داشته و اکنون الگوریتم‌ها جانشین یا مکمل نهادهای انسانی در این سازوکارها شده‌اند. بنابراین فرهنگ امروز تا حد زیادی توسط الگوریتم‌ها گزینش، دسته‌بندی و بازتولید می‌شود و سلیقه، شهرت و ارزش فرهنگی از دل این پردازش‌ها شکل می‌گیرد. این مفهوم، پژوهش توصیه‌گرها، رتبه‌بندی موسیقی و ویدئو، فرهنگ‌سازی پلتفرمی و سیاست فرهنگی را پیش برد. نقدهای اصلی به آن، گستردگی و ابهام مفهومی، خطر نسبت‌دادن عاملیت بیش از اندازه به الگوریتم و نیاز به شواهد تجربی بیشتر دربارهٔ سازوکارهای فرهنگی مربوط می‌شود.",
        definition="فرهنگ الگوریتمی، وضعیتی است که در آن الگوریتم‌ها با گزینش، رتبه‌بندی و توزیع محتوا در تولید و بازتولید فرهنگ نقش فعال دارند و نه فقط ابزار فنی بی‌طرف.",
        main_problem="الگوریتم‌ها چگونه در شکل‌گیری سلیقه، شهرت و ارزش فرهنگی مشارکت می‌کنند، و چه تفاوتی میان فرهنگ‌سازی نهادی و فرهنگ‌سازی الگوریتمی وجود دارد.",
        mechanism="الگوریتم با داده‌های رفتاری، گزینه‌ها را رتبه‌بندی و فیلتر می‌کند؛ این رتبه‌بندی، دیده‌شدن و دسترسی را تعیین می‌کند و به‌تدریج سلیقه و معیارهای ارزش را بازتولید یا تغییر می‌دهد. حلقهٔ بازخورد داده و رفتار، فرهنگ را به‌طور پیوسته بازسازی می‌کند.",
        assumptions=[
            "الگوریتم‌ها در گزینش و توزیع فرهنگ نقش فعال دارند.",
            "دیده‌شدن، تابع رتبه‌بندی الگوریتمی است.",
            "داده‌های رفتاری، سلیقه و ارزش فرهنگی را بازتاب و بازسازی می‌کنند.",
            "فرهنگ همواره با سازوکارهای گزینش پیوند داشته است.",
            "فرهنگ الگوریتمی را باید در بستر تاریخی فرهنگ فهمید.",
        ],
        principles=[
            "الگوریتم را باید عاملی فرهنگی و نه فقط فنی دید.",
            "رتبه‌بندی، ابزار قدرت فرهنگی است.",
            "حلقهٔ بازخورد داده و رفتار، فرهنگ را بازتولید می‌کند.",
            "تحلیل فرهنگ الگوریتمی به شواهد تجربی نیاز دارد.",
            "نهادهای انسانی و الگوریتم‌ها در فرهنگ‌سازی درهم‌تنیده‌اند.",
            "سیاست فرهنگی باید گزینش الگوریتمی را در نظر بگیرد.",
            "سلیقه را باید محصول مشترک کاربر، نهاد و الگوریتم دانست.",
        ],
        critiques=[
            "مفهوم گسترده و از نظر تحلیلی مبهم است.",
            "خطر نسبت‌دادن عاملیت بیش از اندازه به الگوریتم‌ها را دارد.",
            "شواهد تجربی سازوکارهای فرهنگی محدود است.",
            "تفاوت پلتفرم‌ها و بافت‌های فرهنگی کم‌بررسی می‌ماند.",
            "مرز فرهنگ الگوریتمی و بازاریابی هدفمند روشن نیست.",
        ],
        critique_text="منتقدان می‌گویند فرهنگ الگوریتمی مفهومی برانگیزنده برای پیوند مطالعات فرهنگی و فناوری فراهم کرد اما گستردگی آن، مرز تحلیل را مبهم می‌کند و خطر آن دارد که الگوریتم‌ها را بیش از واقع توانمند ببیند. با این حال، به چارچوب مرجع پژوهش فرهنگ پلتفرمی تبدیل شده است.",
        applications=[
            "پژوهش توصیه‌گر و رتبه‌بندی محتوا.",
            "تحلیل فرهنگ موسیقی و ویدئو در پلتفرم‌ها.",
            "سیاست فرهنگی و مقررات شفافیت الگوریتمی.",
            "آموزش سواد رسانه‌ای و فرهنگی دیجیتال.",
            "مطالعهٔ شهرت و ارزش فرهنگی در محیط آنلاین.",
        ],
        example_text="وقتی یک سرویس پخش موسیقی، آهنگ‌های مشابه را در فهرست «پیشنهاد برای شما» بالا می‌آورد، شنیده‌شدن هنرمندان کوچک به رتبه‌بندی الگوریتمی وابسته می‌شود؛ در نتیجه سلیقهٔ جمعی و معیار شهرت فرهنگی به‌تدریج از دل این پردازش شکل می‌گیرد. مفهوم فرهنگ الگوریتمی همین چرخه را تحلیل می‌کند.",
        evolution="مفهوم در بستر مطالعات فرهنگی و پژوهش پلتفرم در دههٔ ۲۰۱۰ شکل گرفت. مقالهٔ سال ۲۰۱۵ آن را تثبیت کرد و پژوهش‌های بعدی، آن را به توصیه‌گرها، موسیقی، خبر و سیاست فرهنگی گستردند.",
        key_concepts=["فرهنگ الگوریتمی", "گزینش الگوریتمی", "رتبه‌بندی", "توصیه‌گر", "حلقهٔ بازخورد", "عاملیت الگوریتم"],
        theorists="تد استریپاس، صورت‌بند مفهوم فرهنگ الگوریتمی.",
        theorists_text="این مفهوم در سنت مطالعات فرهنگی و پژوهش انتقادی پلتفرم شکل گرفت.",
        model="مدل چرخهٔ فرهنگی: داده‌های رفتاری، رتبه‌بندی و گزینش الگوریتمی می‌سازند؛ دیده‌شدن و دسترسی تعیین می‌شود و رفتار بعدی، داده و فرهنگ را بازتولید می‌کند.",
        studies=[
            "مقالهٔ سال ۲۰۱۵ تاریخ مفهومی فرهنگ الگوریتمی را ترسیم کرد.",
            "پژوهش جایزهٔ نتفلیکس، توصیه‌گر و فرهنگ را تحلیل کرد.",
            "مطالعات موسیقی، اثر رتبه‌بندی بر شنیده‌شدن را بررسی کردند.",
            "پژوهش سیاست فرهنگی، شفافیت الگوریتمی را ارزیابی کرد.",
            "مطالعات خبر، اثر رتبه‌بندی الگوریتمی بر دیده‌شدن را سنجیدند.",
        ],
    ),
    "MC-230": dict(
        year=2014,
        summary="حاکمیت الگوریتمی، حوزه‌ای در مطالعات رسانه و سیاست فناوری است که با مقالهٔ اهمیت الگوریتم‌های ترلتون گیلسپی در سال ۲۰۱۴ و پژوهش‌های حقوقی و فنی بعدی دربارهٔ پاسخگویی شکل گرفت. ادعای مرکزی این است که تصمیم‌های مهمی دربارهٔ گزینش خبر، تعدیل محتوا، اعتبارسنجی کاربران و تخصیص فرصت‌ها از طریق الگوریتم‌هایی گرفته می‌شود که معمولاً شفاف و پاسخگو نیستند. حاکمیت الگوریتمی به سازوکارهایی اشاره دارد که این تصمیم‌ها را قابل ممیزی، توضیح و مسئولیت‌پذیر می‌کند: ثبت تصمیم، آزمون سیستم، مستندسازی داده و مدل، فرایند شکایت و بازبینی انسانی. گیلسپی نشان داد الگوریتم‌های ارتباط عمومی، نظام‌های «مرتبط‌سازی» هستند که معیار اهمیت را می‌سازند و بنابراین باید همچون نهادهای رسانه‌ای پاسخگو باشند. پژوهش حقوقی، سازوکارهای فنی پاسخگویی مانند آزمون منصفانه و ممیزی را بسط داد. این حوزه، چارچوب تحلیل مقررات پلتفرم، شفافیت محتوا و حکمرانی خبر الگوریتمی را فراهم کرد. نقدهای اصلی به آن، تمرکز فنی بر پاسخگویی بدون توجه کافی به قدرت سیاسی، خطر «شست‌وشوی حاکمیتی» و محدودیت ممیزی بیرونی الگوریتم‌های بسته مربوط می‌شود.",
        definition="حاکمیت الگوریتمی، مجموعهٔ سازوکارهایی است که تصمیم‌های الگوریتمی در گزینش، تعدیل و رتبه‌بندی را قابل ممیزی، توضیح و مسئولیت‌پذیر می‌کند و آنها را در برابر هنجارهای عمومی پاسخگو می‌سازد.",
        main_problem="چه کسی و بر پایهٔ چه معیاری تصمیم‌های الگوریتمی دربارهٔ دیده‌شدن، دسترسی و اعتبار را می‌گیرد، و چگونه می‌توان این تصمیم‌ها را پاسخگو کرد.",
        mechanism="الگوریتم با معیارهای پنهان، محتوا و کاربران را رتبه‌بندی و فیلتر می‌کند؛ نهاد حاکم با ابزارهای ثبت، ممیزی، توضیح‌پذیری و بازبینی، این معیارها و پیامدها را در معرض بررسی قرار می‌دهد و سازوکار شکایت و اصلاح ایجاد می‌کند.",
        assumptions=[
            "تصمیم‌های الگوریتمی، پیامد عمومی و توزیعی دارند.",
            "شفافیت و ممیزی، پیش‌شرط پاسخگویی است.",
            "الگوریتم‌های مرتبط‌سازی، معیار اهمیت را می‌سازند.",
            "پاسخگویی به سازوکار نهادی و فنی هم‌زمان نیاز دارد.",
            "بازبینی انسانی، بخشی از حاکمیت الگوریتمی است.",
            "پاسخگویی باید پیش از وقوع آسیب و نه فقط پس از آن طراحی شود.",
        ],
        principles=[
            "تصمیم الگوریتمی را باید همچون تصمیم نهادی پاسخگو دید.",
            "ثبت و مستندسازی، پایهٔ ممیزی است.",
            "توضیح‌پذیری باید برای مخاطب و ناظر معنادار باشد.",
            "سازوکار شکایت و بازبینی انسانی ضروری است.",
            "معیار مرتبط‌سازی را باید موضوع بحث عمومی کرد.",
            "حاکمیت الگوریتمی به همکاری فنی، حقوقی و رسانه‌ای نیاز دارد.",
        ],
        critiques=[
            "پاسخگویی فنی بدون توجه به قدرت سیاسی ناکافی است.",
            "خطر شست‌وشوی حاکمیتی و نمایشی وجود دارد.",
            "ممیزی الگوریتم‌های بسته از بیرون دشوار است.",
            "معیارهای پاسخگویی میان حوزه‌ها یکدست نیست.",
            "هزینهٔ انطباق می‌تواند نوآوری کوچک را محدود کند.",
        ],
        critique_text="منتقدان می‌گویند حاکمیت الگوریتمی چارچوب مهمی برای پاسخگویی فنی فراهم کرد اما اگر به توزیع قدرت و منافع سیاسی پیوند نخورد، به رویه‌ای تشریفاتی تبدیل می‌شود. با این حال، به چارچوب مرجع مقررات پلتفرم و شفافیت محتوا تبدیل شده است.",
        applications=[
            "مقررات شفافیت و پاسخگویی پلتفرم.",
            "طراحی سازوکار شکایت و بازبینی محتوا.",
            "ممیزی الگوریتم گزینش خبر.",
            "سیاست‌گذاری تعدیل محتوا و اعتبار کاربر.",
            "آموزش حکمرانی فناوری و حقوق رسانه.",
            "طراحی سیاست تعدیل محتوای رسانه‌های اجتماعی.",
        ],
        example_text="وقتی پلتفرمی یک حساب را به دلیل رفتار مشکوک محدود می‌کند، کاربر باید بتواند دلیل تصمیم را بفهمد، درخواست بازبینی بدهد و پاسخ دریافت کند؛ ثبت تصمیم و بازبینی انسانی، همان سازوکار حاکمیت الگوریتمی است که تصمیم پنهان را پاسخگو می‌کند.",
        evolution="ریشهٔ حوزه در پژوهش انتقادی الگوریتم و حقوق فناوری دههٔ ۲۰۱۰ است. مقالهٔ سال ۲۰۱۴ اهمیت عمومی الگوریتم‌ها را تثبیت کرد و پژوهش حقوقی سال ۲۰۱۷ سازوکارهای پاسخگویی را بسط داد. از ۲۰۲۰ مقررات پلتفرم، این حوزه را به سیاست عمومی کشاند.",
        key_concepts=["پاسخگویی الگوریتمی", "شفافیت", "ممیزی", "توضیح‌پذیری", "مرتبط‌سازی", "بازبینی انسانی"],
        theorists="ترلتون گیلسپی و پژوهشگران حقوق و فناوری پاسخگویی الگوریتمی.",
        theorists_text="این حوزه در تقاطع مطالعات رسانه، حقوق و علوم رایانه شکل گرفت و با مقررات پلتفرم پیوند خورد.",
        model="مدل پاسخگویی: تصمیم الگوریتمی، ثبت و مستندسازی، ممیزی فنی و نهادی، توضیح به کاربر و بازبینی؛ حلقهٔ اصلاح، حاکمیت را تکمیل می‌کند.",
        studies=[
            "مقالهٔ سال ۲۰۱۴ اهمیت عمومی الگوریتم‌ها را تحلیل کرد.",
            "مقالهٔ حقوقی سال ۲۰۱۷ سازوکارهای پاسخگویی را صورت‌بندی کرد.",
            "پژوهش‌های شفافیت، آزمون بیرونی الگوریتم را بررسی کردند.",
            "مطالعات مقررات، حاکمیت پلتفرم را در بافت سیاسی تحلیل کردند.",
        ],
    ),
}

NAME_FIX = {}

YEAR_FIX = {}


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
                                       "verified": n_verified, "batch": 135}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH135 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
