# -*- coding: utf-8 -*-
"""Batch 124 (FRAMEWORK): full documentation for MC-601, MC-607, MC-627, MC-637."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch124-framework-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch124_framework.json"

S = {
    "MC-601": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Law of the Pack",
             title_fa="قانون گله: شبکه‌های دوسویه، گروه‌ساز و پخش",
             authors="Reed, D. P.", year=2001,
             publisher="Harvard Business Review",
             doi=None,
             url="https://hbr.org/2001/02/the-law-of-the-pack",
             language="en", isbn=None,
             citation="Reed, D. P. (2001). The law of the pack. Harvard Business Review, 79(2), 23-24.",
             locator="79(2):23-24", locator_type="page_range",
             supports="Reed's law: utility of group-forming networks scales exponentially", verified=True),
        dict(kind="OTHER",
             title_en="That Sneaky Exponential: Beyond Metcalfe's Law to the Power of Community Building",
             title_fa="آن توان پنهان: فراتر از قانون متکالف و قدرت اجتماع‌سازی",
             authors="Reed, D. P.", year=1999,
             publisher="Context Magazine",
             doi=None, url=None, language="en", isbn=None,
             citation="Reed, D. P. (1999). That sneaky exponential: Beyond Metcalfe's Law to the power of community building. Context Magazine, 2(1).",
             locator="essay", locator_type="SECTION",
             supports="original statement distinguishing broadcast, transaction and group-forming networks", verified=False),
        dict(kind="BOOK",
             title_en="Information Rules: A Strategic Guide to the Network Economy",
             title_fa="قواعد اطلاعات: راهنمای راهبردی اقتصاد شبکه",
             authors="Shapiro, C.; Varian, H. R.", year=1999,
             publisher="Harvard Business School Press",
             doi=None, url=None, language="en", isbn=None,
             citation="Shapiro, C., & Varian, H. R. (1999). Information Rules: A Strategic Guide to the Network Economy. Boston: Harvard Business School Press.",
             locator="network effects chapters", locator_type="SECTION",
             supports="economics of network effects and positive feedback", verified=False),
    ],
    "MC-607": [
        dict(kind="BOOK",
             title_en="Competitive Strategy: Techniques for Analyzing Industries and Competitors",
             title_fa="استراتژی رقابتی: روش‌هایی برای تحلیل صنایع و رقبا",
             authors="Porter, M. E.", year=1980,
             publisher="Free Press",
             doi=None,
             url="https://www.hbs.edu/faculty/Pages/item.aspx?num=195",
             language="en", isbn=None,
             citation="Porter, M. E. (1980). Competitive Strategy: Techniques for Analyzing Industries and Competitors. New York: Free Press.",
             locator="chapters 1-2", locator_type="SECTION",
             supports="three generic strategies: cost leadership, differentiation and focus", verified=True),
        dict(kind="BOOK",
             title_en="Competitive Advantage: Creating and Sustaining Superior Performance",
             title_fa="مزیت رقابتی: آفرینش و حفظ عملکرد برتر",
             authors="Porter, M. E.", year=1985,
             publisher="Free Press",
             doi=None, url=None, language="en", isbn=None,
             citation="Porter, M. E. (1985). Competitive Advantage: Creating and Sustaining Superior Performance. New York: Free Press.",
             locator="value chain chapters", locator_type="SECTION",
             supports="value chain as the locus where cost and differentiation advantages are built", verified=False),
    ],
    "MC-627": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Testing for Competence Rather Than for Intelligence",
             title_fa="سنجش شایستگی به‌جای هوش",
             authors="McClelland, D. C.", year=1973,
             publisher="American Psychologist",
             doi="10.1037/h0034092",
             url="https://psycnet.apa.org/record/1973-22126-001",
             language="en", isbn=None,
             citation="McClelland, D. C. (1973). Testing for competence rather than for intelligence. American Psychologist, 28(1), 1-14.",
             locator="28(1):1-14", locator_type="page_range",
             supports="criterion sampling and competence testing as an alternative to intelligence tests", verified=True),
        dict(kind="BOOK",
             title_en="The Competent Manager: A Model for Effective Performance",
             title_fa="مدیر شایسته: مدلی برای عملکرد اثربخش",
             authors="Boyatzis, R. E.", year=1982,
             publisher="Wiley",
             doi=None, url=None, language="en", isbn=None,
             citation="Boyatzis, R. E. (1982). The Competent Manager: A Model for Effective Performance. New York: Wiley.",
             locator="competency model chapters", locator_type="SECTION",
             supports="empirical competency model distinguishing superior from average managers", verified=False),
    ],
    "MC-637": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Issue Ownership in Presidential Elections, with a 1980 Case Study",
             title_fa="مالکیت موضوع در انتخابات ریاست‌جمهوری، با مطالعهٔ موردی سال ۱۹۸۰",
             authors="Petrocik, J. R.", year=1996,
             publisher="American Journal of Political Science",
             doi=None,
             url="https://www.semanticscholar.org/paper/Issue-Ownership-in-Presidential-Elections%2C-with-a-Petrocik/e38a9005b95731003353db9d0c1a18e6cfba47b2",
             language="en", isbn=None,
             citation="Petrocik, J. R. (1996). Issue ownership in presidential elections, with a 1980 case study. American Journal of Political Science, 40(3), 825-850.",
             locator="40(3):825-850", locator_type="page_range",
             supports="issue ownership theory and issue-based voting", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Issue Ownership and Presidential Campaigning, 1952-2000",
             title_fa="مالکیت موضوع و کارزار انتخاباتی ریاست‌جمهوری، ۱۹۵۲ تا ۲۰۰۰",
             authors="Petrocik, J. R.; Benoit, W. L.; Hansen, G. J.", year=2003,
             publisher="Political Science Quarterly",
             doi=None, url=None, language="en", isbn=None,
             citation="Petrocik, J. R., Benoit, W. L., & Hansen, G. J. (2003). Issue ownership and presidential campaigning, 1952-2000. Political Science Quarterly, 118(4), 599-626.",
             locator="118(4):599-626", locator_type="page_range",
             supports="campaigns emphasize issues owned by their party", verified=False),
    ],
}

ENRICH = {
    "MC-601": dict(
        year=2001,
        summary="قانون رید، اصلی در اقتصاد شبکه‌های دیجیتال است که می‌گوید ارزش شبکه‌ای که کاربرانش می‌توانند آزادانه گروه تشکیل دهند، به‌مراتب سریع‌تر از پیش‌بینی قانون متکالف رشد می‌کند. دیوید رید سه گونهٔ شبکه را از هم جدا کرد: شبکهٔ پخش که در آن یک فرستنده به بسیاری از گیرندگان پیام می‌رساند و ارزشش با شمار کاربران خطی بالا می‌رود؛ شبکهٔ تراکنشی که در آن هر کاربر می‌تواند با هر کاربر دیگر رابطهٔ دوسویه داشته باشد و ارزشش با مجذور شمار کاربران رشد می‌کند؛ و شبکهٔ گروه‌ساز که در آن هر زیرمجموعه از کاربران می‌تواند واحد مستقلی از تعامل باشد. در این حالت شمار گروه‌های ممکن از مرتبهٔ دو به توان تعداد اعضاست و ارزش بالقوهٔ شبکه به‌صورت نمایی بالا می‌رود. اهمیت رسانه‌ای این قانون در توضیح ارزش پیام‌رسان‌ها، انجمن‌های آنلاین و رسانه‌های شهروندی است: آنچه ارزش می‌سازد نه فقط خطوط ارتباطی، بلکه ظرفیت اجتماع‌سازی و همکاری گروهی است. همین منطق مبنای طراحی کانال، گروه و اجتماع در پلتفرم‌ها شده است. با این حال، منتقدان تأکید می‌کنند که رشد نمایی یک کران ریاضی برای ارزش بالقوه است، نه پیش‌بینی ارزش واقعی؛ کیفیت پیوندها، محدودیت توجه کاربران، هزینهٔ شلوغی و احتمال تشکیل گروه‌های بی‌ارزش یا مضر در محاسبه نمی‌آید. پس قانون رید ابزار استدلال دربارهٔ سقف ارزش شبکه است و نه معیار سنجش مستقیم آن.",
        definition="قانون رید گزاره‌ای در اقتصاد شبکه است که ارزش بالقوهٔ شبکهٔ گروه‌ساز را متناسب با شمار زیرمجموعه‌های قابل تشکیل، یعنی رشدی نمایی نسبت به شمار اعضا، می‌داند.",
        main_problem="قواعد سادهٔ ارزش شبکه، مانند قانون متکالف، ارزش پیوندهای انسانی را تنها بر پایهٔ شمار جفت‌های ارتباطی می‌سنجند و از ظرفیت شبکه برای تشکیل گروه‌های مشترک‌منفعت غافل می‌مانند؛ پرسش این است که چگونه می‌توان ارزش اجتماعی و اقتصادی گروه‌سازی را در مدل‌سازی شبکه لحاظ کرد.",
        mechanism="با تفکیک سه گونه شبکه، مکانیسم روشن می‌شود: در شبکهٔ پخش، افزودن یک کاربر تنها یک گیرندهٔ تازه می‌آورد؛ در شبکهٔ تراکنشی، افزودن یک کاربر همهٔ کاربران پیشین را به او وصل می‌کند و شمار پیوندهای ممکن با مجذور تعداد اعضا بالا می‌رود؛ اما در شبکهٔ گروه‌ساز، هر زیرمجموعهٔ دلخواه از اعضا می‌تواند گروهی مستقل باشد، از گروه‌های چندنفرهٔ کوچک تا اجتماع‌های بزرگ، و شمار این زیرگروه‌ها با دو به توان تعداد اعضا هم‌مرتبه است. ارزش شبکه از خط به مجذور و از مجذور به نمایی می‌رود و ابزارهای گروه‌سازی، این ارزش نهفته را آزاد می‌کنند.",
        assumptions=[
            "شبکه امکان تشکیل گروه‌های آزاد و چندنفره را برای کاربران فراهم می‌کند.",
            "کاربران می‌توانند هم‌زمان در چند گروه عضو باشند، بی‌آنکه هزینهٔ بازدارنده‌ای بپردازند.",
            "ارزش هر گروه مستقل از کیفیت اعضا و کیفیت تعامل درون آن فرض می‌شود.",
            "زیرساخت فنی، تشکیل گروه با اندازهٔ دلخواه را ممکن می‌کند.",
            "منافع گروه‌سازی افزودنی است و اثرهای منفی بیرونی در محاسبه نمی‌آید.",
        ],
        principles=[
            "شبکهٔ پخش، شبکهٔ تراکنشی و شبکهٔ گروه‌ساز باید از هم تفکیک شوند.",
            "ارزش بالقوهٔ شبکه متناسب با شمار زیرگروه‌های ممکن رشد می‌کند.",
            "واحد پایهٔ ارزش در شبکهٔ گروه‌ساز، گروه است و نه فرد.",
            "ارزش نهفته تا زمانی که ابزار گروه‌سازی فراهم نشود آزاد نمی‌شود.",
            "شکل معماری شبکه، سرعت رشد ارزش آن را تعیین می‌کند.",
            "اقتصاد شبکه را باید بر پایهٔ ظرفیت مشارکت جمعی سنجید، نه فقط شمار اشتراک‌ها.",
        ],
        critiques=[
            "رشد نمایی یک کران ریاضی است و پیش‌بینی تجربی ارزش واقعی نیست.",
            "فرض برابری ارزش همهٔ گروه‌ها با واقعیت فاصله دارد.",
            "محدودیت توجه کاربران و هزینهٔ شلوغی نادیده گرفته می‌شود.",
            "کیفیت پیوندها، اعتماد و تعامل در محاسبه نمی‌آید.",
            "احتمال تشکیل گروه‌های بی‌ارزش، هرزنامه‌ای یا آسیب‌زا کنار گذاشته شده است.",
        ],
        critique_text="منتقدان می‌گویند قانون رید سقف نظری ارزش را نشان می‌دهد و نه ارزش تحقق‌یافته را؛ در عمل بسیاری از گروه‌های ممکن هرگز شکل نمی‌گیرند، بیشتر گروه‌های شکل‌گرفته ارزش اندکی دارند و توجه کاربران کالایی کمیاب است. بنابراین رشد نمایی باید استدلالی دربارهٔ اهمیت معماری گروه‌ساز خوانده شود و نه پیش‌بینی عددی.",
        applications=[
            "تحلیل ارزش پلتفرم‌های اجتماعی و پیام‌رسان‌ها.",
            "طراحی انجمن‌های آنلاین، کانال‌های محتوایی و اجتماع‌های تخصصی.",
            "ارزیابی اقتصاد رسانهٔ شهروندی و محتوای کاربرساخته.",
            "تحلیل ارزش شبکه‌های همکاری سازمانی و ابزارهای کار گروهی.",
            "سیاست‌گذاری رقابت و تنظیم‌گری در بازار پلتفرم‌ها.",
        ],
        example_text="در یک پیام‌رسان مانند ایتا، ارزش پلتفرم تنها به شمار مخاطبان مستقیم هر کاربر وابسته نیست؛ کانال‌ها، گروه‌های خانوادگی، گروه‌های صنفی و اجتماع‌های محلی لایه‌ای از ارزش می‌سازند که با شمار اعضا به‌صورت نمایی گسترش می‌یابد. به همین دلیل پلتفرم‌هایی که ساخت گروه و کانال را ساده‌تر و ارزان‌تر می‌کنند، سریع‌تر رشد می‌کنند و وابستگی کاربران را بیشتر می‌کنند.",
        evolution="ریشهٔ بحث به قانون متکالف بازمی‌گردد که ارزش شبکه را با مجذور شمار کاربران می‌سنجید، اما این قاعده فقط پیوندهای دوسویهٔ فردی را در نظر می‌گرفت. دیوید رید در سال ۱۹۹۹ لایهٔ سوم را افزود و بر ارزش گروه‌سازی تأکید کرد و در سال ۲۰۰۱ آن را در نشریهٔ کسب‌وکار هاروارد برای مدیران اجرایی صورت‌بندی کرد. سپس پژوهشگرانی مانند اندرو اودلیزکو و ریچارد تیلی نشان دادند که هیچ قانون ساده‌ای جای سنجش تجربی ارزش شبکه را نمی‌گیرد و ارزش محتوا و پهنای باند نیز باید جداگانه سنجیده شود.",
        key_concepts=["شبکهٔ گروه‌ساز", "قانون متکالف", "ارزش شبکه", "زیرگروه", "اثر شبکه‌ای", "هزینهٔ توجه", "معماری شبکه"],
        theorists="دیوید رید، مهندس نرم‌افزار و نظریه‌پرداز شبکه‌های دیجیتال است که سه‌گانهٔ شبکه‌های پخش، تراکنشی و گروه‌ساز را صورت‌بندی کرد.",
        theorists_text="در سنت بحث قانون‌های شبکه، رابرت متکالف با قانون مجذور کاربران و اندرو اودلیزکو با نقد تجربی این قانون‌ها زمینهٔ بحث رید را ساختند.",
        model="مدل سه‌سطحی ارزش: سطح پخش با رشد خطی، سطح تراکنشی با رشد مجذوری و سطح گروه‌ساز با رشد نمایی؛ ارزش تحقق‌یافته در هر سطح به ظرفیت فنی و انگیزهٔ مشارکت کاربران وابسته است.",
        studies=[
            "مقالهٔ رید در سال ۲۰۰۱ صورت‌بندی مدیرانهٔ قانون را در دسترس گسترده قرار داد.",
            "مقالهٔ اولیهٔ سال ۱۹۹۹ سه‌گانهٔ شبکه‌ها را با تأکید بر اجتماع‌سازی معرفی کرد.",
            "پژوهش‌های اقتصاد شبکه دربارهٔ اثرهای شبکه‌ای و بازخورد مثبت، مبانی سنجش ارزش را گستردند.",
            "نقدهای تجربی نشان دادند ارزش واقعی شبکه باید با دادهٔ رفتاری سنجیده شود و نه با فرمول.",
        ],
    ),
    "MC-607": dict(
        year=1980,
        summary="راهبردهای عمومی پورتر، چارچوبی است که مایکل پورتر در کتاب استراتژی رقابتی سال ۱۹۸۰ برای پاسخ به یک پرسش بنیادی ارائه کرد: شرکت چگونه می‌تواند در یک صنعت جایگاهی دفاع‌پذیر به دست آورد؟ پاسخ او سه مسیر بود. رهبری هزینه یعنی رسیدن به کمترین هزینهٔ تولید و توزیع در صنعت و جلب مشتریان حساس به قیمت. تمایز یعنی عرضهٔ محصول یا خدمتی که در سراسر صنعت یگانه شمرده می‌شود و مشتری حاضر است برایش بهای بیشتری بپردازد. تمرکز یعنی خدمت‌رسانی به یک بخش محدود از بازار که یا با هزینهٔ پایین یا با تمایز ویژه اداره می‌شود. چارچوب در بستر تحلیل ساختاری صنعت با پنج نیروی رقابتی و تحلیل زنجیرهٔ ارزش جای می‌گیرد و ادعای مرکزی آن این است که شرکت باید یکی از سه مسیر را روشن انتخاب کند، زیرا گیر افتادن در میانهٔ راه، مزیت هیچ‌یک را به دست نمی‌دهد. در رسانه‌ها این چارچوب هم برای توضیح موقعیت برندهای خبری ممتاز، هم برای فهم پلتفرم‌های کم‌هزینه و هم برای طراحی رسانه‌های تخصصی مخاطب‌محور به کار می‌رود. با این حال، پژوهش‌های تجربی بعدی نشان دادند که راهبردهای ترکیبی نیز می‌توانند موفق باشند و ساختار صنعت تنها عامل تعیین‌کنندهٔ سود نیست.",
        definition="راهبردهای عمومی، سه مسیر بنیادی برای کسب مزیت رقابتی پایدار در یک صنعت است: رهبری هزینه، تمایز، و تمرکز بر یک بخش محدود بازار.",
        main_problem="شرکت در بازاری پر از رقیب چگونه می‌تواند موضعی دفاع‌پذیر بسازد و از نوسان سود و تقلید رقبا در امان بماند، در حالی که منابعش محدود است.",
        mechanism="چارچوب دو انتخاب بنیادی را از هم جدا می‌کند: دامنهٔ رقابت، یعنی کل صنعت یا یک بخش محدود؛ و نوع مزیت، یعنی هزینهٔ پایین یا تمایز. تلاقی این دو، ماتریسی دو در دو می‌سازد که سه خانهٔ آن مسیر معتبر است. پنج نیروی رقابتی شدت جذابیت صنعت را تعیین می‌کنند و زنجیرهٔ ارزش نشان می‌دهد مزیت هزینه یا تمایز در کدام فعالیت‌ها ساخته می‌شود.",
        assumptions=[
            "ساختار صنعت، یعنی شدت پنج نیروی رقابتی، سود بلندمدت را تعیین می‌کند.",
            "شرکت می‌تواند به‌روشنی میان دامنهٔ گسترده و بخش محدود انتخاب کند.",
            "مزیت هزینه یا تمایز پایدار است و تقلید رقیب آن را به‌سرعت از میان نمی‌برد.",
            "بخش‌های بازار شناسایی‌پذیرند و نیازهای متفاوتی دارند.",
            "گیر افتادن در میانهٔ راه به عملکرد ضعیف می‌انجامد.",
        ],
        principles=[
            "مزیت رقابتی باید در یکی از دو محور صریح هزینه یا تمایز تعریف شود.",
            "دامنهٔ رقابت باید آگاهانه انتخاب شود، نه به‌طور پیش‌فرض.",
            "تحلیل صنعت با پنج نیرو پیش از انتخاب راهبرد انجام می‌شود.",
            "مزیت در فعالیت‌های زنجیرهٔ ارزش ساخته می‌شود و نه در شعار.",
            "از راهبرد مبهم و میانهٔ راه باید پرهیز کرد.",
            "رهبری هزینه به مقیاس و سهم بازار وابسته است و تمایز به اعتبار و کیفیت ادراک‌شده.",
        ],
        critiques=[
            "شواهد تجربی نشان می‌دهد راهبردهای ترکیبی هزینه و تمایز می‌توانند موفق باشند.",
            "چارچوب ساختار صنعت را بیش از اندازه ثابت فرض می‌کند و پویایی نوآوری را کم‌رنگ می‌بیند.",
            "عوامل نهادی، فرهنگی و مسیر وابسته در تحلیل جای کافی ندارند.",
            "مرز میان بخش بازار و کل صنعت در عمل مبهم می‌شود.",
            "موفقیت برندهای رسانه‌ای اغلب به اعتماد و هویت جمعی وابسته است، نه فقط به هزینه و تمایز.",
        ],
        critique_text="منتقدان، به‌ویژه پس از پژوهش‌های دههٔ ۱۹۸۰، ادعای ناسازگاری هزینه و تمایز را به چالش کشیدند و نمونه‌هایی از شرکت‌هایی آوردند که هر دو را هم‌زمان به کار می‌گیرند. پاسخ پورتر این بود که چنین ترکیبی موقتی است و در بلندمدت نیازمند انتخاب روشن است، اما بحث نشان داد که چارچوب بیشتر ابزار تحلیل است تا قانون آهنین.",
        applications=[
            "تحلیل جایگاه برندهای خبری و روزنامه‌ها در بازار رسانه.",
            "طراحی پلتفرم‌های ویدئویی کم‌هزینه در برابر سرویس‌های ممتاز.",
            "راه‌اندازی رسانه‌های تخصصی برای بخش محدود مخاطبان.",
            "ارزیابی پنج نیروی رقابتی در بازار رسانه و تبلیغات.",
            "تحلیل زنجیرهٔ ارزش از تولید تا توزیع محتوا.",
        ],
        example_text="یک روزنامهٔ اقتصادی می‌تواند با تمرکز بر مخاطب حرفه‌ای و تمایز در دقت و عمق تحلیلی فعالیت کند، در حالی که یک پلتفرم خبری عمومی با رهبری هزینه و اتکا به محتوای کاربران به مقیاس می‌رسد؛ انتخاب نکردن روشن میان این دو مسیر، هر دو را تضعیف می‌کند.",
        evolution="چارچوب در کتاب استراتژی رقابتی سال ۱۹۸۰ صورت‌بندی شد، در مزیت رقابتی سال ۱۹۸۵ با مفهوم زنجیرهٔ ارزش بسط یافت و در مقالهٔ سال ۱۹۹۶ دربارهٔ چیستی راهبرد به تمایز میان کارایی عملیاتی و جایگاه راهبردی رسید. نقدهای دههٔ ۱۹۸۰ و ۱۹۹۰ و ظهور رویکردهای مبتنی بر منابع و بعدها راهبرد اقیانوس آبی، چارچوب را از قانون مطلق به یکی از ابزارهای پایه در جعبه‌ابزار تحلیل راهبردی تبدیل کرد.",
        key_concepts=["مزیت رقابتی", "رهبری هزینه", "تمایز", "تمرکز", "بخش بازار", "پنج نیروی رقابتی", "زنجیرهٔ ارزش", "میانهٔ راه"],
        theorists="مایکل پورتر، اقتصاددان و استاد مدرسهٔ کسب‌وکار هاروارد، سازندهٔ چارچوب پنج نیرو و راهبردهای عمومی است.",
        theorists_text="پورتر این چارچوب را در گفت‌وگو با سنت اقتصاد صنعتی و پژوهش‌های ساختار بازار صورت‌بندی کرد و بعدها منتقدانی مانند دنی میلر و پژوهشگران رویکرد مبتنی بر منابع آن را بازخوانی کردند.",
        model="ماتریسی دو‌بعدی: محور افقی نوع مزیت، یعنی هزینه در برابر تمایز؛ و محور عمودی دامنه، یعنی کل صنعت در برابر بخش محدود. سه خانهٔ معتبر عبارت‌اند از رهبری هزینه، تمایز و تمرکز که خود دو گونهٔ هزینه‌محور و تمایزمحور دارد.",
        studies=[
            "کتاب استراتژی رقابتی سال ۱۹۸۰ چارچوب سه‌گانه را با تحلیل ساختاری صنعت معرفی کرد.",
            "کتاب مزیت رقابتی سال ۱۹۸۵ زنجیرهٔ ارزش را به‌عنوان محل ساخت مزیت افزود.",
            "پژوهش‌های تجربی دربارهٔ راهبردهای عمومی و عملکرد، شواهدی به سود و زیان تفکیک سخت میان مسیرها فراهم کردند.",
            "نقدهای بعدی نشان دادند راهبردهای ترکیبی می‌توانند در برخی صنایع عملکرد بهتری داشته باشند.",
        ],
    ),
    "MC-627": dict(
        year=1973,
        summary="چارچوب شایستگی، رویکردی به سنجش و پرورش توانمندی حرفه‌ای است که ریشهٔ آن به مقالهٔ دیوید مک‌کللند در سال ۱۹۷۳ بازمی‌گردد. مک‌کللند استدلال کرد که آزمون‌های هوش و نمره‌های تحصیلی پیش‌بین ضعیفی برای موفقیت در کار هستند و به سوگیری طبقاتی و فرهنگی متهم‌اند. او به‌جای آن، سنجش ملاک‌محور را پیشنهاد کرد: شایستگی‌ها باید از مقایسهٔ رفتار شاغلان برتر با شاغلان متوسط در همان نقش استخراج شوند. ریچارد بویاتزیس در دههٔ ۱۹۸۰ این ایده را به مدلی رفتاری برای مدیران اثربخش تبدیل کرد و پس از او، چارچوب‌های شایستگی در گزینش، آموزش و ارزیابی منابع انسانی گسترش یافت. در رسانه، چارچوب شایستگی برای طراحی دورهٔ آموزش روزنامه‌نگاری چندرسانه‌ای، گزینش خبرنگاران و ارزیابی عملکرد حرفه‌ای به کار می‌رود: به‌جای فهرست کردن مدرک و سابقه، رفتارهای قابل مشاهده‌ای تعریف می‌شود که عملکرد برتر را از متوسط جدا می‌کند. نقد اصلی به این رویکرد، اتکا به خودگزارشی و تفسیر مصاحبه‌گر، تورم فهرست‌های شایستگی، کم‌توجهی به بافت سازمانی و پیوند ضعیف با عملکرد سازمانی است. با این حال، ایدهٔ پایهٔ آن، یعنی سنجش بر پایهٔ عملکرد واقعی و نه نمرهٔ انتزاعی، همچنان معتبر و پرکاربرد است.",
        definition="چارچوب شایستگی، مجموعهٔ سازمان‌یافته‌ای از دانش، مهارت و ویژگی‌های رفتاری است که عملکرد برتر را در یک نقش یا سازمان توصیف و پیش‌بینی می‌کند.",
        main_problem="آزمون‌های هوش و نمره‌های تحصیلی پیش‌بین ضعیفی برای موفقیت شغلی بودند و به سوگیری طبقاتی و فرهنگی متهم می‌شدند؛ پرسش این بود که چه سنجه‌ای می‌تواند عملکرد واقعی را پیش‌بینی کند.",
        mechanism="مکانیسم پایه، نمونه‌گیری ملاک‌محور است: پژوهشگر گروهی از شاغلان برتر و گروهی از شاغلان متوسط را برمی‌گزیند، با هر دو به‌شیوهٔ رویداد رفتاری مصاحبه می‌کند و می‌پرسد در موقعیت‌های دشوار چه کردند و چه اندیشیدند؛ سپس تفاوت‌های تکرارشونده در رفتار و اندیشه را به‌عنوان شایستگی‌های تمایزساز استخراج می‌کند. این شایستگی‌ها به زبان رفتاری توصیف می‌شوند تا در گزینش و آموزش به کار آیند.",
        assumptions=[
            "شاغلان برتر و متوسط در رفتار قابل مشاهده با هم تفاوت دارند.",
            "این تفاوت‌ها را می‌توان از راه مصاحبهٔ نظام‌مند و مشاهدهٔ نمونه‌های واقعی کشف کرد.",
            "شایستگی‌ها را می‌توان به زبان رفتاری توصیف و در آموزش بازتولید کرد.",
            "عملکرد برتر تا اندازهٔ زیادی به ویژگی‌های فردی وابسته است و نه فقط به دانش فنی.",
            "نمونهٔ مقایسه‌ای به‌اندازهٔ کافی نمایندهٔ نقش مورد مطالعه است.",
        ],
        principles=[
            "سنجش باید ملاک‌محور باشد، یعنی با عملکرد واقعی سنجیده شود و نه با نمرهٔ آزمون.",
            "مقایسهٔ شاغلان برتر و متوسط، روش پایهٔ استخراج شایستگی است.",
            "شایستگی باید به رفتار قابل مشاهده ترجمه شود.",
            "دانش، مهارت و انگیزش در کنار هم سنجیده می‌شوند.",
            "شایستگی‌های آستانه‌ای برای حداقل پذیرش و شایستگی‌های تمایزساز برای برتری جدا می‌شوند.",
            "چارچوب باید به فرایندهای گزینش، آموزش و ارزیابی گره بخورد.",
        ],
        critiques=[
            "روش مصاحبهٔ رویداد رفتاری به حافظهٔ خودگزارشی و تفسیر مصاحبه‌گر وابسته است.",
            "فهرست‌های شایستگی در عمل بسیار بزرگ، تکراری و مبهم می‌شوند.",
            "بافت سازمانی، فناوری و شرایط کار در مدل‌های فردمحور کم‌رنگ می‌شود.",
            "پیوند میان شایستگی‌های فردی و عملکرد سازمانی ضعیف و ناهمگون است.",
            "خطر تبدیل شایستگی به برچسب و ابزار کنترل مدیریتی وجود دارد.",
        ],
        critique_text="منتقدان می‌گویند چارچوب شایستگی از نقدی روشن آغاز شد اما در عمل به فهرست‌های بلند و مبهم انجامید و گاه به ابزاری برای مشروعیت‌بخشی به تصمیم‌های مدیریتی تبدیل شد. با این حال، ایدهٔ سنجش ملاک‌محور و توصیف رفتار برتر، همچنان در طراحی آموزش حرفه‌ای رسانه معتبر و کارآمد است.",
        applications=[
            "گزینش روزنامه‌نگاران و خبرنگاران چندرسانه‌ای.",
            "طراحی دوره‌های آموزش حرفه‌ای رسانه بر پایهٔ رفتار برتر.",
            "ارزیابی عملکرد کارکنان تحریریه و تولید محتوا.",
            "طراحی مسیر شغلی و توسعهٔ مهارت در سازمان رسانه‌ای.",
            "مدیریت استعداد و جانشین‌پروری در رسانه‌ها.",
        ],
        example_text="مدل شایستگی یک خبرنگار چندرسانه‌ای می‌تواند شامل مهارت فنی تولید محتوا در چند قالب، قضاوت خبری در شرایط ابهام، پایبندی به اخلاق حرفه‌ای، توان تعامل با مخاطب و کار تیمی باشد؛ هر شایستگی با نمونه‌های رفتاری سنجیده می‌شود، نه با مدرک یا سابقهٔ صرف.",
        evolution="مقالهٔ مک‌کللند در سال ۱۹۷۳ نقد روش‌شناختی را آغاز کرد، کتاب بویاتزیس در سال ۱۹۸۲ مدل رفتاری مدیران اثربخش را ارائه داد و در دههٔ ۱۹۹۰ چارچوب‌های شایستگی به‌طور گسترده در سازمان‌ها و کتاب‌های مدیریت منابع انسانی به کار رفت. از دههٔ ۲۰۰۰ به بعد، نقدهای روش‌شناختی بر تورم فهرست‌ها و کم‌توجهی به بافت، به بازطراحی چارچوب‌ها به‌سوی مدل‌های یکپارچه و موقعیت‌محور انجامید.",
        key_concepts=["شایستگی", "شایستگی تمایزساز", "شایستگی آستانه‌ای", "نمونه‌گیری ملاک‌محور", "مصاحبهٔ رویداد رفتاری", "عملکرد برتر"],
        theorists="دیوید مک‌کللند، روان‌شناس انگیزش و بنیان‌گذار رویکرد شایستگی؛ ریچارد بویاتزیس، سازندهٔ مدل شایستگی مدیران؛ و لایل اسپنسر و سیگن اسپنسر، تدوین‌کنندگان چارچوب کاربردی شایستگی.",
        theorists_text="سنت پژوهش شایستگی بر پایهٔ روان‌شناسی انگیزش و سنجش رفتار شکل گرفت و بعدها با مدیریت راهبردی منابع انسانی پیوند خورد.",
        model="مدل لایه‌ای شایستگی: دانش و مهارت در سطح آشکار و انگیزش، ویژگی‌های شخصی و خودپنداره در سطح نهفته قرار می‌گیرند؛ شایستگی‌های نهفته پیش‌بین قوی‌تر عملکرد برتر شمرده می‌شوند.",
        studies=[
            "مقالهٔ سال ۱۹۷۳ نقد آزمون‌های هوش و پیشنهاد سنجش ملاک‌محور را صورت‌بندی کرد.",
            "کتاب سال ۱۹۸۲ مدل شایستگی را برای مدیران اثربخش به‌صورت تجربی آزمود.",
            "چارچوب‌های دههٔ ۱۹۹۰ شایستگی را به زبان کاربردی منابع انسانی ترجمه کردند.",
            "پژوهش‌های نقدی دههٔ ۲۰۰۰ به ضعف پیوند شایستگی فردی با عملکرد سازمانی پرداختند.",
        ],
    ),
    "MC-637": dict(
        year=1996,
        summary="نظریهٔ مالکیت موضوع، نظریه‌ای در رفتار رأی‌دهی و ارتباطات سیاسی است که جان پتروچیک آن را در سال ۱۹۹۶ صورت‌بندی کرد. ایدهٔ مرکزی این است که هر حزب در نظر رأی‌دهندگان بر برخی موضوعات اعتبار ویژه دارد و آن موضوعات را «مالک» است: رأی‌دهندگان باور دارند آن حزب بهتر می‌تواند مشکل مربوط را حل کند. رأی‌دهنده مجموعه‌ای از اولویت‌های موضوعی دارد که از هویت گروهی، تجربهٔ گذشته و شرایط جاری شکل می‌گیرد و به همان اندازه که به حزب وابسته است، به دستور کار موضوعی روز نیز وابسته است. کمپین انتخاباتی مالک یک موضوع، می‌کوشد آن موضوع را در مرکز توجه عمومی نگه دارد و موضوعات متعلق به رقیب را کم‌رنگ کند؛ به این ترتیب، نوسان نتایج انتخابات تا اندازهٔ زیادی به این بستگی دارد که کدام مجموعه از موضوعات در آن دوره برجسته شده است. پتروچیک در مطالعهٔ موردی خود نشان داد در انتخابات ریاست‌جمهوری آمریکا، جمهوری‌خواهان مالک موضوعات امنیت ملی و مالیات و دموکرات‌ها مالک خدمات اجتماعی و حقوق مدنی شمرده می‌شدند و سالی که موضوعات یک حزب برجسته می‌شد، شانس آن حزب بالا می‌رفت. این نظریه بعدها به تحلیل کارزار، پوشش خبری و سنجش افکار عمومی راه یافت. نقدهای اصلی به سنجش ناپایدار مالکیت با نظرسنجی تک‌پرسشی، ابهام مرز مالکیت و هویت حزبی، کم‌توجهی به نقش رسانه در تغییر مالکیت و محدودیت تعمیم یافته‌های آمریکایی به نظام‌های چندحزبی مربوط می‌شود.",
        definition="نظریهٔ مالکیت موضوع، نظریه‌ای در رفتار رأی‌دهی و ارتباطات سیاسی است که می‌گوید هر حزب در نظر رأی‌دهندگان بر برخی موضوعات اعتبار ویژه و مالکیت دارد و کمپین‌ها با برجسته‌کردن موضوعات متعلق به خود، شانس رأی را افزایش می‌دهند.",
        main_problem="وفاداری حزبی نسبتاً پایدار است، اما نتایج انتخابات نوسان دارد؛ پرسش این است که چه سازوکاری این نوسان را توضیح می‌دهد و کمپین‌ها چگونه می‌توانند آن را مدیریت کنند.",
        mechanism="رأی‌دهنده مجموعه‌ای از اولویت‌های موضوعی دارد که از هویت گروهی، تجربهٔ گذشته و شرایط جاری شکل می‌گیرد. برای هر موضوع، حزبی که در نظر رأی‌دهنده تواناتر شمرده می‌شود مالک آن است. کمپین مالک، موضوعات متعلق به خود را برجسته و موضوعات رقیب را کم‌رنگ می‌کند و می‌کوشد دستور کار انتخاب را به نفع خود بچرخاند؛ در نتیجه، ترکیب موضوعات برجسته در هر دوره، نتیجه را جابه‌جا می‌کند.",
        assumptions=[
            "رأی‌دهندگان درک پایدار و متمایزی از توانایی احزاب در موضوعات دارند.",
            "مالکیت موضوع از تاریخ حزب، پایگاه اجتماعی و عملکرد گذشته شکل می‌گیرد.",
            "برجستگی موضوع در ذهن رأی‌دهنده بر انتخاب او اثر می‌گذارد.",
            "کمپین‌ها می‌توانند دستور کار موضوعی را تا اندازه‌ای جهت دهند.",
            "شرایط جاری و بحران‌ها می‌توانند اولویت موضوعی رأی‌دهنده را تغییر دهند.",
        ],
        principles=[
            "موضوع، واحد تحلیل رقابت انتخاباتی است.",
            "مالکیت موضوع اعتبار ادراک‌شده است و نه لزوماً عملکرد عینی.",
            "کمپین موفق بر موضوعات مالکیت‌شده تمرکز می‌کند.",
            "رأی‌دهی موضوعی در رأی‌دهندگان بی‌طرف و کم‌وفادار قوی‌تر است.",
            "مالکیت موضوع پایدار اما تغییرپذیر است.",
            "پوشش خبری می‌تواند مالکیت موضوع را تقویت یا تضعیف کند.",
        ],
        critiques=[
            "سنجش مالکیت بر نظرسنجی تک‌پرسشی و ناپایدار تکیه دارد.",
            "مرز میان مالکیت موضوع و هویت حزبی مبهم است.",
            "نقش رسانه و چارچوب‌بندی خبری در تغییر مالکیت کم‌بررسی مانده است.",
            "رأی‌دهندگان ممکن است موضوعات را بر پایهٔ منافع شخصی ارزیابی کنند و نه مالکیت حزبی.",
            "تعمیم یافته‌های آمریکایی به نظام‌های چندحزبی و ائتلافی محدود است.",
        ],
        critique_text="منتقدان می‌گویند مالکیت موضوع بیش از آنکه ویژگی ثابت احزاب باشد، برآیند ادراک عمومی در یک دورهٔ زمانی است و رسانه‌ها می‌توانند آن را جابه‌جا کنند. با این حال، شواهد تجربی متعدد نشان داده‌اند که برجسته‌سازی موضوعات مالکیت‌شده در کمپین، با تغییر سهم رأی همراه است و همین نکته، نظریه را به ابزاری کاربردی در تحلیل ارتباطات سیاسی تبدیل کرده است.",
        applications=[
            "تحلیل استراتژی پیام و دستور کار کمپین‌های انتخاباتی.",
            "سنجش افکار عمومی و رصد مالکیت موضوعی احزاب.",
            "مشاورهٔ سیاسی و طراحی تقویم موضوعی کمپین.",
            "تحلیل پوشش خبری و برجسته‌سازی موضوعات.",
            "ارتباطات دولتی و مدیریت دستور کار عمومی.",
        ],
        example_text="در انتخابات ریاست‌جمهوری آمریکا، جمهوری‌خواهان مالک موضوعات امنیت ملی و مالیات و دموکرات‌ها مالک خدمات اجتماعی شمرده می‌شدند؛ پتروچیک نشان داد سالی که موضوعات متعلق به یک حزب برجسته می‌شود، شانس آن حزب بالا می‌رود و کمپین‌ها نیز آگاهانه بر همان موضوعات تمرکز می‌کنند.",
        evolution="نظریه در سال ۱۹۹۶ با مطالعهٔ موردی انتخابات ۱۹۸۰ معرفی شد، در سال ۲۰۰۳ با تحلیل تبلیغات ریاست‌جمهوری نیم‌قرن به‌کار رفت، آزمون‌های تطبیقی در اروپا و نظام‌های چندحزبی آن را بازخوانی کردند و پژوهش‌های دههٔ ۲۰۱۰ مالکیت را به اولویت‌های حزبی و سیاست‌گذاری پیوند دادند.",
        key_concepts=["مالکیت موضوع", "برجستگی موضوع", "اولویت موضوعی", "رأی‌دهی موضوعی", "اعتبار ادراک‌شده", "دستور کار انتخاب"],
        theorists="جان پتروچیک، صورت‌بند نظریهٔ مالکیت موضوع؛ ویلیام ون در بروخ، آزمون‌کنندهٔ آن در رفتار رأی‌دهنده؛ و پاتریک ایگان، پژوهشگر مالکیت موضوع و اولویت‌های حزبی.",
        theorists_text="این نظریه در سنت پژوهش رفتار انتخاباتی و ارتباطات سیاسی شکل گرفت و با پژوهش‌های تطبیقی به نظام‌های حزبی دیگر راه یافت.",
        model="مدل سه‌لایه: پایگاه اجتماعی و تاریخ حزب، مالکیت موضوعی را می‌سازد؛ کمپین برجستگی موضوعات مالکیت‌شده را بالا می‌برد؛ و رأی‌دهنده بر پایهٔ ترکیب موضوعات برجسته و اعتبار ادراک‌شدهٔ احزاب انتخاب می‌کند.",
        studies=[
            "مقالهٔ سال ۱۹۹۶ نظریه را با مطالعهٔ موردی انتخابات ۱۹۸۰ معرفی کرد.",
            "پژوهش سال ۲۰۰۳ تبلیغات ریاست‌جمهوری نیم‌قرن را با منطق مالکیت موضوع تحلیل کرد.",
            "آزمون‌های تطبیقی در دموکراسی‌های اروپایی مرزهای تعمیم نظریه را روشن کردند.",
            "پژوهش‌های بعدی مالکیت موضوع را به اولویت‌های سیاستی و عملکرد دولت پیوند دادند.",
        ],
    ),
}

NAME_FIX = {
    "MC-607": ("راهبردهای عمومی پورتر", "Porter's Generic Strategies",
               "name normalized: استراتژی‌های -> راهبردهای for terminology consistency"),
}

YEAR_FIX = {
    "MC-607": "year filled: none -> 1980 (Porter, Competitive Strategy, Free Press)",
    "MC-627": "no year change; note: editorial card core_logic was a mismatched generic professionalization template; documentation rebuilt from McClelland (1973) and Boyatzis (1982)",
    "MC-637": "no year change; note: editorial card core_logic was a mismatched media-governance template; documentation rebuilt from Petrocik (1996)",
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
                                       "verified": n_verified, "batch": 124}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH124 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
