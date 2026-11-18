# -*- coding: utf-8 -*-
"""Batch 154 (MODEL): MC-610 maker economy, MC-611 public media, MC-619 JCM, MC-620 JD-R."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch154-model-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch154_model.json"

S = {
    "MC-610": [
        dict(kind="BOOK",
             title_en="Makers: The New Industrial Revolution",
             title_fa="سازندگان: انقلاب صنعتی نوین",
             authors="Anderson, C.", year=2012,
             publisher="Crown Business",
             doi=None,
             url="https://en.wikipedia.org/wiki/Makers:_The_New_Industrial_Revolution",
             language="en", isbn=None,
             citation="Anderson, C. (2012). Makers: The New Industrial Revolution. New York: Crown Business.",
             locator="2012 edition", locator_type="edition",
             supports="maker economy built on open design, desktop fabrication and web-based distribution", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Makers: The New Industrial Revolution by Chris Anderson - review",
             title_fa="نقد کتاب سازندگان اثر کریس اندرسون",
             authors="The Guardian", year=2012,
             publisher="The Guardian",
             doi=None,
             url="https://www.theguardian.com/books/2012/dec/07/makers-chris-anderson-review",
             language="en", isbn=None,
             citation="The Guardian (2012, December 7). Makers: The New Industrial Revolution by Chris Anderson - review.",
             locator="7 December 2012", locator_type="date",
             supports="critical reception and limits of the maker-economy claim", verified=True),
    ],
    "MC-611": [
        dict(kind="REPORT",
             title_en="What is the Public Value of Public Service Broadcasting? PEC Discussion Paper",
             title_fa="ارزش عمومی پخش عمومی چیست؟",
             authors="Chivers, T.", year=2022,
             publisher="Public Service Broadcasting and Media Policy Discussion Paper",
             doi=None,
             url="https://pec.ac.uk/wp-content/uploads/2024/01/What-is-the-Public-Value-of-Public-Service-Broadcasting-PEC-Discussion-Paper-Jan-2022.pdf",
             language="en", isbn=None,
             citation="Chivers, T. (2022). What is the Public Value of Public Service Broadcasting? PEC Discussion Paper, January 2022.",
             locator="January 2022", locator_type="date",
             supports="public value framework for publicly funded broadcasting", verified=True),
        dict(kind="REPORT",
             title_en="BBC Royal Charter Review - House of Commons CMS Committee Report",
             title_fa="بازنگری منشور سلطنتی بی‌بی‌سی - گزارش کمیته رسانه مجلس بریتانیا",
             authors="House of Commons Culture, Media and Sport Committee", year=2026,
             publisher="UK Parliament",
             doi=None,
             url="https://publications.parliament.uk/pa/cm5902/cmselect/cmcumeds/140/report.html",
             language="en", isbn=None,
             citation="House of Commons Culture, Media and Sport Committee (2026). BBC Royal Charter Review. HC 140.",
             locator="HC 140", locator_type="report_number",
             supports="governance, funding and independence of public media", verified=True),
    ],
    "MC-619": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Motivation through the Design of Work: Test of a Theory",
             title_fa="انگیزش از راه طراحی کار: آزمون یک نظریه",
             authors="Hackman, J. R.; Oldham, G. R.", year=1976,
             publisher="Organizational Behavior and Human Performance",
             doi="10.1016/0030-5073(76)90016-7",
             url="https://www.sciencedirect.com/science/article/pii/0030507376900167",
             language="en", isbn=None,
             citation="Hackman, J. R., & Oldham, G. R. (1976). Motivation through the design of work: Test of a theory. Organizational Behavior and Human Performance, 16(2), 250-279.",
             locator="16(2):250-279", locator_type="page_range",
             supports="five core job dimensions shaping critical psychological states and work outcomes", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Development of the Job Diagnostic Survey",
             title_fa="توسعهٔ پیمایش تشخیص شغل",
             authors="Hackman, J. R.; Oldham, G. R.", year=1975,
             publisher="Journal of Applied Psychology",
             doi=None,
             url="https://psycnet.apa.org/record/1975-22031-001",
             language="en", isbn=None,
             citation="Hackman, J. R., & Oldham, G. R. (1975). Development of the Job Diagnostic Survey. Journal of Applied Psychology, 60(2), 159-170.",
             locator="60(2):159-170", locator_type="page_range",
             supports="operational measurement of job dimensions and motivating potential", verified=True),
    ],
    "MC-620": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Job Demands-Resources Model of Burnout",
             title_fa="مدل تقاضاها–منابع شغلیِ فرسودگی",
             authors="Demerouti, E.; Bakker, A. B.; Nachreiner, F.; Schaufeli, W. B.", year=2001,
             publisher="Journal of Applied Psychology",
             doi="10.1037/0021-9010.86.3.499",
             url="https://psycnet.apa.org/record/2001-06715-012",
             language="en", isbn=None,
             citation="Demerouti, E., Bakker, A. B., Nachreiner, F., & Schaufeli, W. B. (2001). The job demands-resources model of burnout. Journal of Applied Psychology, 86(3), 499-512.",
             locator="86(3):499-512", locator_type="page_range",
             supports="two categories of working conditions and the burnout pathway", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Job Demands-Resources Model: State of the Art",
             title_fa="مدل تقاضاها–منابع شغلی: وضعیت روزآمد",
             authors="Bakker, A. B.; Demerouti, E.", year=2007,
             publisher="Journal of Managerial Psychology",
             doi="10.1108/02683940710733115",
             url="https://www.emerald.com/jmp/article/22/3/309/236386/The-Job-Demands-Resources-model-state-of-the-art",
             language="en", isbn=None,
             citation="Bakker, A. B., & Demerouti, E. (2007). The job demands-resources model: State of the art. Journal of Managerial Psychology, 22(3), 309-328.",
             locator="22(3):309-328", locator_type="page_range",
             supports="health-impairment and motivational processes plus buffering hypothesis", verified=True),
    ],
}

ENRICH = {
    "MC-610": dict(
        year=2012,
        summary="اقتصاد سازندگان، که کریس اندرسون در کتاب سازندگان: انقلاب صنعتی نوین سال ۲۰۱۲ صورت‌بندی کرد، الگویی از تولید و توزیع را توصیف می‌کند که در آن افراد و گروه‌های کوچک با ابزارهای دیجیتال ارزان، طراحی باز و پلتفرم‌های توزیع، از مصرف‌کننده به تولیدکننده تبدیل می‌شوند. در این اقتصاد، مرز میان حرفه‌ای و آماتور، و میان کارخانه و کارگاه خانگی، فرو می‌ریزد: چاپ سه‌بعدی، برش لیزری، نرم‌افزار آزاد و بازارگاه‌های آنلاین، تولید در مقیاس کوچک را ممکن می‌کنند. اندرسون استدلال کرد که این جنبش می‌تواند تولید صنعتی متمرکز را به تولید توزیع‌شده و سفارشی تبدیل کند. در رسانه، اقتصاد سازندگان به خالقان محتوا، پادکست‌سازان و سازندگان ویدیو تعمیم یافت که با اشتراک، حمایت مالی و فروش مستقیم، از مخاطب درآمد می‌گیرند. مدل بر سه رکن استوار است: ابزار ارزان تولید، دسترسی باز به دانش و کانال توزیع مستقیم. نقدهای اصلی به آن، اغراق فناورانه، پنهان‌سازی نابرابری مهارت، بی‌ثباتی درآمد خالقان، وابستگی به پلتفرم و فراموش‌کردن کار یدی پشت تولید را برجسته می‌کنند؛ نقدی که پادزهر لازم برای هر سیاست حمایتی است.",
        definition="اقتصاد سازندگان، الگوی تولید و توزیع مبتنی بر ابزارهای دیجیتال ارزان، طراحی باز و کانال‌های مستقیم است که افراد و گروه‌های کوچک را از مصرف‌کننده به تولیدکننده تبدیل می‌کند و مرز حرفه و آماتور را می‌شکند.",
        main_problem="چگونه ابزارهای دیجیتال ارزان و کانال‌های توزیع مستقیم، تولید رسانه و کالا را از انحصار سازمان‌های بزرگ خارج می‌کنند و چه فرصت‌ها و خطرهایی برای خالقان پدید می‌آورند.",
        mechanism="ابزار تولید ارزان و دانش باز، هزینهٔ ورود را پایین می‌آورد؛ پلتفرم‌های توزیع، دسترسی مستقیم به مخاطب می‌دهند؛ درآمد از اشتراک، حمایت مالی و فروش مکمل تأمین می‌شود و چرخهٔ تولید مستقل را ممکن می‌کند.",
        assumptions=[
            "ابزار تولید ارزان در دسترس است.",
            "دانش طراحی باز مبادله می‌شود.",
            "پلتفرم توزیع مستقیم فراهم است.",
            "خالق می‌تواند مخاطب بسازد.",
            "درآمد خرد تجمع‌پذیر است.",
        ],
        principles=[
            "هزینهٔ تولید را پایین بیاور.",
            "دانش و طراحی را باز بگذار.",
            "مخاطب را مستقیم بساز.",
            "درآمد را متنوع کن.",
            "کیفیت را جای کمیت بنشان.",
            "وابستگی به پلتفرم را کم کن.",
        ],
        critiques=[
            "اغراق فناورانه دارد.",
            "نابرابری مهارت را پنهان می‌کند.",
            "درآمد خالقان بی‌ثبات است.",
            "به پلتفرم وابسته است.",
            "کار یدی پشت تولید را می‌پوشاند.",
            "مصرف‌گرایی را بازتولید می‌کند.",
            "حقوق کارگر خرد را نادیده می‌گیرد.",
            "سنجش اثر اقتصادی آن دشوار است.",
        ],
        critique_text="منتقدان می‌گویند اقتصاد سازندگان آزادی تولید را بزرگ‌نمایی کرد و نابرابری مهارت، بی‌ثباتی درآمد و وابستگی به پلتفرم را کم‌بررسی گذاشت؛ با این حال، چارچوب مفیدی برای فهم تولید مستقل در رسانه است.",
        applications=[
            "تحلیل اقتصاد خالقان.",
            "طراحی کسب‌وکار رسانه‌ای کوچک.",
            "سیاست حمایت از تولید مستقل.",
            "آموزش مهارت دیجیتال.",
            "پژوهش کار خانگی.",
            "تحلیل پلتفرم توزیع.",
            "برنامهٔ آموزش کارآفرینی خرد.",
        ],
        example_text="پادکست‌سازی که با میکروفن ارزان و نرم‌افزار آزاد تولید می‌کند و از طریق حمایت شنوندگان درآمد دارد، نمونهٔ روشن اقتصاد سازندگان است؛ همان سازوکاری که او را از وابستگی به شبکهٔ بزرگ آزاد می‌کند، او را به الگوریتم پلتفرم گره می‌زند.",
        evolution="کتاب سال ۲۰۱۲ اندرسون، جنبش سازندگان را از کارگاه‌های اشتراکی به الگوی اقتصادی گسترد. پژوهش‌های بعدی، آن را به اقتصاد خالقان و کار پلتفرمی پیوند دادند و پرسش از پایداری درآمد را پیش گذاشتند.",
        key_concepts=["سازنده", "طراحی باز", "تولید توزیع‌شده", "اقتصاد خالقان", "کار پلتفرمی", "توزیع مستقیم"],
        theorists="کریس اندرسون.",
        theorists_text="مدل در سنت اقتصاد دیجیتال و فرهنگ سازندگان شکل گرفت.",
        model="الگوی تولید مستقل مبتنی بر ابزار ارزان، دانش باز و توزیع مستقیم که افراد را به تولیدکننده تبدیل می‌کند.",
        studies=[
            "کتاب سال ۲۰۱۲ الگوی سازندگان را معرفی کرد.",
            "نقد سال ۲۰۱۲ محدودیت‌های ادعا را نشان داد.",
            "مطالعات کار، بی‌ثباتی خالقان را سنجیدند.",
            "پژوهش پلتفرم، وابستگی توزیع را تحلیل کرد.",
            "مطالعات صنعتی، تولید توزیع‌شده را ارزیابی کردند.",
            "پژوهش جنسیت، کار خالقان زن را بررسی کرد.",
            "مطالعات حقوقی، مالکیت طرح باز را بررسی کردند.",
            "تحلیل آموزشی، یادگیری مهارت سازندگی را سنجید.",
            "پژوهش شهری، کارگاه‌های اشتراکی را تحلیل کرد.",
            "مطالعات اقتصادی، بازار صنایع خرد را سنجیدند.",
        ],
    ),
    "MC-611": dict(
        year=1927,
        summary="مدل رسانهٔ عمومی، که با تجربهٔ بی‌بی‌سی و پخش عمومی در اروپا شکل گرفت، رسانه را نه کالای بازاری بلکه خدمتی عمومی می‌داند که با بودجهٔ عمومی، دسترسی همگانی، استقلال از دولت و بازار، و پاسخ‌گویی به منافع عمومی اداره می‌شود. در این مدل، پخش‌کنندهٔ عمومی از راه حق اشتراک یا مالیات تأمین می‌شود تا از فشار تبلیغ‌دهنده و وابستگی سیاسی رها بماند. اصول کلاسیک آن، جهان‌شمولی، تنوع، کیفیت، بی‌طرفی و خدمت به اقلیت‌هاست. مدل در برابر رسانهٔ تجاری، معیار سنجش موفقیت را سود نمی‌داند، بلکه ارزش عمومی و اعتماد مخاطب را ملاک می‌گیرد. در عصر دیجیتال، پخش عمومی با پلتفرم‌های جهانی، فرسایش حق اشتراک و مناقشهٔ بی‌طرفی روبه‌رو شده و به رسانهٔ عمومی چندسکویی تغییر شکل داده است؛ گذاری که پرسش از مرز خدمت عمومی و سرگرمی را دوباره زنده کرد. نقدهای اصلی به آن، هزینهٔ عمومی، خطر نزدیکی به دولت، محافظه‌کاری نهادی، دشواری سنجش ارزش عمومی و رقابت نابرابر با پلتفرم‌ها را برجسته می‌کنند.",
        definition="مدل رسانهٔ عمومی، رسانه را خدمتی همگانی می‌داند که با بودجهٔ عمومی اداره می‌شود، از دولت و بازار استقلال دارد و معیار موفقیت آن ارزش عمومی و اعتماد مخاطب است، نه سود؛ همین جابه‌جایی معیار، هستهٔ تمایز آن از رسانهٔ تجاری است.",
        main_problem="چگونه می‌توان رسانه‌ای ساخت که هم‌زمان از فشار دولت و بازار آزاد باشد، به همهٔ شهروندان خدمت کند و در محیط پلتفرمی همچنان مشروعیت و تأمین مالی خود را حفظ کند.",
        mechanism="بودجهٔ عمومی و حکمرانی مستقل، رسانه را از وابستگی به تبلیغ و دولت رها می‌کند؛ اصول جهان‌شمولی و تنوع، خدمت به همهٔ گروه‌ها را تضمین می‌کند و پاسخ‌گویی عمومی، مشروعیت آن را بازتولید می‌کند.",
        assumptions=[
            "رسانه خدمتی عمومی است.",
            "بودجهٔ عمومی لازم است.",
            "استقلال از دولت و بازار ممکن است.",
            "دسترسی همگانی هدف است.",
            "ارزش عمومی سنجیدنی است.",
        ],
        principles=[
            "جهان‌شمولی را حفظ کن.",
            "استقلال را نهادی کن.",
            "تنوع و کیفیت را بسنج.",
            "به اقلیت‌ها خدمت کن.",
            "پاسخ‌گویی عمومی بساز.",
            "حضور چندسکویی را جدی بگیر.",
        ],
        critiques=[
            "بار مالی عمومی دارد.",
            "خطر نزدیکی به دولت هست.",
            "محافظه‌کاری نهادی را تقویت می‌کند.",
            "سنجش ارزش عمومی دشوار است.",
            "در برابر پلتفرم‌ها نابرابر است.",
            "جوانان را کمتر جذب می‌کند.",
            "رقابت با پلتفرم‌های جهانی را سخت می‌یابد.",
            "تعریف مرز بی‌طرفی مناقشه‌آمیز است.",
        ],
        critique_text="منتقدان می‌گویند مدل رسانهٔ عمومی خدمت همگانی را تضمین کرد اما هزینهٔ عمومی، خطر وابستگی سیاسی و کندی نهادی را به همراه داشت؛ با این حال، معیار جایگزینی برای سودمحوری رسانه فراهم می‌کند.",
        applications=[
            "طراحی سیاست رسانهٔ عمومی.",
            "تحلیل تأمین مالی بی‌بی‌سی.",
            "ارزیابی ارزش عمومی.",
            "پژوهش رسانهٔ خدمت عمومی.",
            "آموزش روزنامه‌نگاری.",
            "سیاست رسانهٔ دیجیتال.",
            "تحلیل مشروعیت نهاد رسانه.",
            "مقایسهٔ مدل‌های تأمین مالی.",
        ],
        example_text="بی‌بی‌سی با حق اشتراک خانوار تأمین می‌شود و منشور آن، جهان‌شمولی و بی‌طرفی را الزام می‌کند؛ همین ساختار آن را از فشار تبلیغ‌دهنده دور می‌کند، اما در برابر پلتفرم‌های رایگان و مناقشهٔ سیاسی آسیب‌پذیر می‌سازد.",
        evolution="مدل از تجربهٔ بی‌بی‌سی در دههٔ ۱۹۲۰ برخاست و در نیمهٔ دوم قرن بیستم، با رادیو و تلویزیون عمومی، به الگوی اروپایی پخش عمومی بدل شد؛ در دههٔ ۲۰۲۰ با بازنگری منشور و گذار دیجیتال بازتعریف شد.",
        key_concepts=["پخش عمومی", "ارزش عمومی", "حق اشتراک", "جهان‌شمولی", "استقلال تحریریه", "پاسخ‌گویی"],
        theorists="جان ریت و سنت پخش عمومی اروپا.",
        theorists_text="مدل در سنت پخش عمومی و سیاست رسانهٔ اروپایی شکل گرفت.",
        model="رسانهٔ خدمت عمومی که با بودجهٔ عمومی اداره می‌شود و معیار آن ارزش عمومی، تنوع و استقلال است.",
        studies=[
            "تجربهٔ بی‌بی‌سی الگوی مرجع شد.",
            "گزارش سال ۲۰۲۲ ارزش عمومی را چارچوب داد.",
            "گزارش پارلمانی ۲۰۲۶ حکمرانی و تأمین مالی را بررسی کرد.",
            "پژوهش دیجیتال، گذار چندسکویی را تحلیل کرد.",
            "مطالعات تطبیقی، مدل اروپایی را مقایسه کردند.",
            "پژوهش مخاطب، اعتماد به رسانهٔ عمومی را سنجید.",
            "مطالعات اقتصادی، بار مالی حق اشتراک را سنجیدند.",
            "پژوهش حقوقی، استقلال تحریریه را تحلیل کرد.",
            "مطالعات تاریخی، تحول پخش عمومی را روایت کردند.",
            "پژوهش سیاست، مشروعیت حق اشتراک را بررسی کرد.",
        ],
    ),
    "MC-619": dict(
        year=1976,
        summary="مدل ویژگی‌های شغل، که جی. ریچارد هاکمن و گرگ آر. اولدهام در مقالهٔ سال ۱۹۷۶ ارائه کردند، توضیح می‌دهد که طراحی شغل چگونه انگیزش، رضایت و عملکرد را شکل می‌دهد. مدل پنج ویژگی اصلی شغل را مشخص می‌کند: تنوع مهارت، هویت وظیفه، اهمیت وظیفه، خودمختاری و بازخورد. سه ویژگی نخست، معناداری کار را می‌سازند؛ خودمختاری، مسئولیت نسبت به نتیجه را؛ و بازخورد، آگاهی از نتایج را. این سه حالت روانی، انگیزش درونی، رضایت، کیفیت عملکرد و حضور کاری را افزایش می‌دهند. مدل یک نمرهٔ پتانسیل انگیزشی از ترکیب این ویژگی‌ها می‌سازد و ابزار پیمایش تشخیص شغل را برای سنجش آن فراهم می‌کند. در رسانه، مدل برای تحلیل شغل خبرنگار به کار می‌رود: خودمختاری تحریریه، تنوع موضوعی، بازخورد سردبیر و اهمیت اجتماعی گزارش، انگیزش حرفه‌ای را تعیین می‌کنند و معیار بازطراحی اتاق خبر می‌شوند. نقدهای اصلی به آن، فردگرایی روان‌شناختی، کم‌توجهی به تفاوت‌های فرهنگی، فرض ثبات ویژگی‌ها و سنجش پیمایشی محدود را برجسته می‌کنند.",
        definition="مدل ویژگی‌های شغل، پنج ویژگی طراحی شغل را به سه حالت روانی و سپس به انگیزش، رضایت و عملکرد پیوند می‌دهد و با نمرهٔ پتانسیل انگیزشی، کیفیت طراحی شغل را می‌سنجد؛ ابزاری عملی برای بازطراحی مشاغل کم‌انگیزه.",
        main_problem="چگونه می‌توان شغل را طوری طراحی کرد که کارکنان، به‌ویژه در محیط‌های پرتقاضای رسانه، از درون برانگیخته شوند و کیفیت عملکرد و رضایت شغلی بالا رود.",
        mechanism="ویژگی‌های شغل، حالت‌های روانی معناداری، مسئولیت و آگاهی از نتیجه را می‌سازند؛ این حالت‌ها انگیزش درونی و عملکرد را تقویت می‌کنند و طراحی شغل، متغیر مداخله‌پذیر مدیر است.",
        assumptions=[
            "طراحی شغل قابل تغییر است.",
            "پنج ویژگی اصلی قابل سنجش‌اند.",
            "معناداری از سه ویژگی می‌آید.",
            "حالت‌های روانی انگیزش می‌سازند.",
            "تفاوت فردی تعدیل می‌کند.",
        ],
        principles=[
            "تنوع مهارت را افزایش ده.",
            "وظیفه را کامل و شناسایی‌پذیر کن.",
            "اهمیت اجتماعی کار را روشن کن.",
            "خودمختاری واقعی بده.",
            "بازخورد مستقیم و روشن بده.",
            "نمرهٔ پتانسیل را پایش کن.",
        ],
        critiques=[
            "فردگرایی روان‌شناختی دارد.",
            "تفاوت فرهنگی را کم‌می‌بیند.",
            "ثبات ویژگی‌ها را فرض می‌کند.",
            "سنجش پیمایشی محدود است.",
            "شرایط مادی کار را کم‌بررسی می‌گذارد.",
            "به کار دانشی کامل تعمیم نمی‌یابد.",
            "قدرت مذاکرهٔ کارکنان را نادیده می‌گیرد.",
            "به فناوری شغلی کم می‌پردازد.",
            "انگیزش بیرونی را کم‌وزن می‌کند.",
        ],
        critique_text="منتقدان می‌گویند مدل ویژگی‌های شغل طراحی کار را دقیق ساخت اما فردگرا بود و شرایط مادی و فرهنگی کار را کم‌بررسی گذاشت؛ با این حال، ابزار اصلی تحلیل انگیزش شغلی در سازمان‌های رسانه‌ای است.",
        applications=[
            "طراحی شغل خبرنگار.",
            "بازطراحی تحریریه.",
            "سنجش انگیزش کارکنان.",
            "آموزش مدیران رسانه.",
            "پژوهش منابع انسانی.",
            "ارزیابی مشاغل پلتفرمی.",
            "طراحی تیم‌های تحریریه.",
            "تحلیل شغل‌های تخصصی رسانه.",
        ],
        example_text="خبرنگاری که فقط تیتر بازنویسی می‌کند، تنوع و هویت وظیفه ندارد و انگیزشش می‌ریزد؛ همان فرد با پروندهٔ تحقیقی کامل، خودمختاری و بازخورد سردبیر، کار را معنادار تجربه می‌کند.",
        evolution="مقالهٔ سال ۱۹۷۶ مدل را آزمود و پیمایش سال ۱۹۷۵ ابزار سنجش آن را داد. پژوهش‌های بعدی، مدل را به کار دانشی، تیم‌های خبری و مشاغل دیجیتال گستردند و نقد فردگرایی آن را پیش کشیدند.",
        key_concepts=["تنوع مهارت", "هویت وظیفه", "خودمختاری", "بازخورد", "حالت‌های روانی", "پتانسیل انگیزشی"],
        theorists="جی. ریچارد هاکمن و گرگ آر. اولدهام.",
        theorists_text="مدل در سنت روان‌شناسی سازمانی و طراحی کار شکل گرفت.",
        model="پیوند پنج ویژگی شغل با سه حالت روانی و با انگیزش درونی، رضایت و کیفیت عملکرد.",
        studies=[
            "مقالهٔ سال ۱۹۷۶ مدل را آزمود.",
            "پیمایش سال ۱۹۷۵ ابزار سنجش ساخت.",
            "مطالعات رسانه، شغل خبرنگار را تحلیل کردند.",
            "پژوهش پلتفرم، طراحی کار الگوریتمی را سنجید.",
            "مطالعات منابع انسانی، پتانسیل انگیزشی را آزمودند.",
            "پژوهش حرفه، خودمختاری خبرنگار را بررسی کرد.",
            "مطالعات تطبیقی، پتانسیل انگیزشی را بین مشاغل سنجید.",
            "پژوهش دیجیتال، اثر الگوریتم بر خودمختاری را بررسی کرد.",
            "مطالعات سلامت، فرسودگی اتاق خبر را سنجیدند.",
            "پژوهش انگیزش، نقش بازخورد را آزمود.",
            "مطالعات حرفه، تنوع مهارت خبرنگار را بررسی کردند.",
            "پژوهش سازمان، هویت وظیفه را در تحریریه سنجید.",
            "مطالعات مدیریت، بازخورد سردبیر را تحلیل کردند.",
        ],
    ),
    "MC-620": dict(
        year=2001,
        summary="مدل تقاضاها–منابع شغلی، که اوانجلیا دمروتی و همکارانش در سال ۲۰۰۱ معرفی کردند، همهٔ شرایط کاری را در دو دستهٔ کلی جای می‌دهد: تقاضاها و منابع. تقاضاها جنبه‌هایی از کارند که انرژی و توان شناختی و هیجانی می‌طلبند؛ منابع جنبه‌هایی هستند که به دستیابی به هدف، کاهش تقاضا یا رشد فردی کمک می‌کنند. مدل دو فرایند موازی را پیشنهاد می‌کند: فرایند تضعیف سلامت، که تقاضای مزمن را به فرسودگی می‌رساند، و فرایند انگیزشی، که منابع را به تعهد و عملکرد پیوند می‌دهد. منابع همچنین می‌توانند اثر تقاضا را تعدیل کنند. برخلاف مدل‌های پیشین، این مدل به فهرست ثابتی از تقاضاها و منابع وابسته نیست و برای هر حرفه قابل انطباق است. در رسانه، فشار زمانی، بار هیجانی خبر بد و فشار سیاسی تقاضا محسوب می‌شوند؛ حمایت سردبیر، خودمختاری، بازخورد سازنده و همکاران خوب منابع‌اند و تفاوت میان تحریریهٔ سالم و فرسوده را می‌سازند. نقدهای اصلی به آن، ابهام مفهومی مرز تقاضا و منبع، سنجش خودگزارشی، کم‌توجهی به طراحی سازمانی و خطر فردی‌کردن مسئولیت فرسودگی را برجسته می‌کنند.",
        definition="مدل تقاضاها–منابع شغلی، شرایط کار را به تقاضاها و منابع تقسیم می‌کند و از دو فرایند تضعیف سلامت و انگیزشی برای توضیح فرسودگی و اشتیاق کاری استفاده می‌کند؛ چارچوبی که مداخله را از سطح فرد به طراحی شغل می‌برد.",
        main_problem="چرا برخی کارکنان در برابر فشار کاری فرسوده می‌شوند و برخی شکوفا می‌مانند، و چگونه منابع شغلی می‌توانند اثر تقاضاها را تعدیل کنند.",
        mechanism="تقاضاهای مزمن، توان را می‌فرسایند و به فرسودگی می‌رسند؛ منابع، انگیزش و تعهد می‌سازند و در حضور منابع بالا، اثر منفی تقاضا کاهش می‌یابد.",
        assumptions=[
            "شرایط کار دو دسته‌اند.",
            "تقاضا و منبع قابل تفکیک‌اند.",
            "دو فرایند موازی جریان دارد.",
            "منابع اثر تقاضا را تعدیل می‌کنند.",
            "فهرست برای هر حرفه انعطاف‌پذیر است.",
        ],
        principles=[
            "تقاضاها را شناسایی کن.",
            "منابع کلیدی را بساز.",
            "فرسودگی را زود پایش کن.",
            "منابع را در برابر تقاضا تقویت کن.",
            "مداخله را سازمانی کن.",
            "مسئولیت را فردی نکن.",
        ],
        critiques=[
            "مرز تقاضا و منبع مبهم است.",
            "سنجش خودگزارشی محدود است.",
            "طراحی سازمانی را کم‌می‌بیند.",
            "مسئولیت فرسودگی را فردی می‌کند.",
            "به فرهنگ سازمانی کم می‌پردازد.",
            "مدل طولی کم دارد.",
            "تقاضاهای مثبت را کم بررسی می‌کند.",
            "به عوامل ساختاری بازار کار کم می‌پردازد.",
            "تفاوت فردی را کم‌وزن می‌کند.",
        ],
        critique_text="منتقدان می‌گویند مدل تقاضاها–منابع شغلی چارچوبی انعطاف‌پذیر برای فرسودگی ساخت اما مرز مفاهیم را مبهم گذاشت و خطر فردی‌کردن مسئولیت سازمانی را در پی داشت؛ با این حال، چارچوب مسلط پژوهش سلامت شغلی است.",
        applications=[
            "سنجش فرسودگی خبرنگاران.",
            "طراحی مداخلهٔ سازمانی.",
            "پژوهش اشتیاق کاری.",
            "سیاست منابع انسانی رسانه.",
            "تحلیل کار پلتفرمی.",
            "آموزش مدیران.",
            "بازطراحی بار کاری تحریریه.",
            "ارزیابی سیاست سلامت شغلی.",
        ],
        example_text="تحریریه‌ای که بار خبری سنگین و ضرب‌الاجل دائمی دارد اما خودمختاری و حمایت سردبیر نمی‌دهد، تقاضا را بالا و منابع را پایین نگه می‌دارد؛ مدل نشان می‌دهد که افزودن منبع، پیش از فروپاشی کارکنان، مسیر ارزان‌تری است.",
        evolution="مقالهٔ سال ۲۰۰۱ مدل را با پژوهش فرسودگی معرفی کرد و مقالهٔ سال ۲۰۰۷ آن را به نظریهٔ پخته‌تری با دو فرایند، فرض تعدیل و برنامهٔ پژوهشی گسترده بدل ساخت.",
        key_concepts=["تقاضای شغلی", "منبع شغلی", "فرسودگی", "اشتیاق کاری", "فرایند تضعیف سلامت", "تعدیل"],
        theorists="اوانجلیا دمروتی، آرنولد ب. باکر، فریده ناخراینر و ویلمار ب. شوفلی.",
        theorists_text="مدل در سنت روان‌شناسی سلامت شغلی شکل گرفت.",
        model="دو دستهٔ تقاضا و منبع با دو فرایند تضعیف سلامت و انگیزشی که فرسودگی و اشتیاق کاری را توضیح می‌دهند.",
        studies=[
            "مقالهٔ سال ۲۰۰۱ مدل فرسودگی را معرفی کرد.",
            "مقالهٔ سال ۲۰۰۷ نظریه را بازآرایی کرد.",
            "مطالعات رسانه، فرسودگی خبرنگاران را سنجیدند.",
            "پژوهش پلتفرم، تقاضاهای الگوریتمی را تحلیل کرد.",
            "مطالعات طولی، مسیر فرسودگی را ردیابی کردند.",
            "پژوهش مداخله، اثر منابع را سنجید.",
            "مطالعات تطبیقی، مدل را بین حرفه‌ها آزمودند.",
            "پژوهش دیجیتال، تقاضای همیشه‌روشن را بررسی کرد.",
            "مطالعات مدیریت، حمایت سردبیر را منبع کلیدی یافتند.",
            "پژوهش سلامت، بار هیجانی خبر بد را تحلیل کرد.",
            "مطالعات تطبیقی، منابع شغلی خبرنگاران را مقایسه کردند.",
        ],
    ),
}

NAME_FIX = {}
YEAR_FIX = {
    "MC-610": "کارت سال ۲۰۲۰ و بی‌نظریه‌پرداز بود؛ منبع بنیادی، کتاب اندرسون ۲۰۱۲ است و سال همان ثبت شد.",
    "MC-611": "کارت سال و نظریه‌پرداز نداشت و متن آن قالب عمومی اقتصاد رسانه بود؛ سال ۱۹۲۷ (تجربهٔ بی‌بی‌سی) و مدل پخش عمومی مبنا قرار گرفت.",
    "MC-619": "متن کارت قالب عمومی حرفه‌ای‌سازی بود؛ محتوا بر پایهٔ مدل اصلی هاکمن و اولدهام ۱۹۷۶ بازنویسی شد.",
    "MC-620": "متن کارت قالب عمومی حرفه‌ای‌سازی و انتساب نادرست به باکر بود؛ محتوا بر پایهٔ دمروتی و همکاران ۲۰۰۱ بازنویسی شد.",
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
                                       "verified": n_verified, "batch": 154}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH154 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
