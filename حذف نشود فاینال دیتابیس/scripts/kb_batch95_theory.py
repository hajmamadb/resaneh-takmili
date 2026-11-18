# -*- coding: utf-8 -*-
"""Batch 95: full documentation for MC-522, MC-523, MC-525, MC-527."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch95-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch95_theory.json"

S = {
    "MC-522": [
        dict(kind="BOOK_CHAPTER",
             title_en="Friendship as a Social Process: A Substantive and Methodological Analysis",
             title_fa="دوستی به‌عنوان فرایند اجتماعی: تحلیلی ماهوی و روش‌شناختی",
             authors="Lazarsfeld, P. F.; Merton, R. K.", year=1954, publisher="Van Nostrand",
             doi=None, url=None, language="en", isbn=None,
             citation="Lazarsfeld, P. F., & Merton, R. K. (1954). Friendship as a social process: A substantive and methodological analysis. In M. Berger, T. Abel, & C. H. Page (Eds.), Freedom and control in modern society (pp. 18-66). Van Nostrand.",
             locator="pp. 18-66", locator_type="page_range",
             supports="homophily in friendship / value homophily / information flow", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Birds of a Feather: Homophily in Social Networks",
             title_fa="کبوتران هم‌پر: همسانی در شبکه‌های اجتماعی",
             authors="McPherson, J. M.; Smith-Lovin, L.; Cook, J. M.", year=2001,
             publisher="Annual Review of Sociology",
             doi="10.1146/annurev.soc.27.1.415", url=None, language="en", isbn=None,
             citation="McPherson, J. M., Smith-Lovin, L., & Cook, J. M. (2001). Birds of a feather: Homophily in social networks. Annual Review of Sociology, 27, 415-444. https://doi.org/10.1146/annurev.soc.27.1.415",
             locator="27:415-444", locator_type="page_range",
             supports="baseline and inbreeding homophily / selection and influence", verified=True),
    ],
    "MC-523": [
        dict(kind="BOOK",
             title_en="Diffusion of Innovations (5th ed.)",
             title_fa="تسهیم نوآوری (ویرایش پنجم)",
             authors="Rogers, E. M.", year=2003, publisher="Free Press",
             doi=None, url="https://www.simonandschuster.com/books/Diffusion-of-Innovations-5th-Edition/Everett-M-Rogers/9780743222099",
             language="en", isbn="9780743222099",
             citation="Rogers, E. M. (2003). Diffusion of innovations (5th ed.). Free Press.",
             locator="work", locator_type="work",
             supports="innovation attributes / adopter categories / diffusion elements", verified=True),
        dict(kind="BOOK",
             title_en="Diffusion of Innovations",
             title_fa="تسهیم نوآوری",
             authors="Rogers, E. M.", year=1962, publisher="Free Press",
             doi=None, url=None, language="en", isbn=None,
             citation="Rogers, E. M. (1962). Diffusion of innovations. Free Press.",
             locator="work", locator_type="work",
             supports="original formulation of diffusion model", verified=False),
    ],
    "MC-525": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Critical Questions for Big Data: Provocations for a Cultural, Technological, and Scholarly Phenomenon",
             title_fa="پرسش‌های انتقادی درباره کلان‌داده: تأملاتی در یک پدیده فرهنگی، فناورانه و علمی",
             authors="boyd, d.; Crawford, K.", year=2012,
             publisher="Information, Communication & Society",
             doi="10.1080/1369118X.2012.678878",
             url="https://www.tandfonline.com/doi/full/10.1080/1369118X.2012.678878",
             language="en", isbn=None,
             citation="boyd, d., & Crawford, K. (2012). Critical questions for big data: Provocations for a cultural, technological, and scholarly phenomenon. Information, Communication & Society, 15(5), 662-679. https://doi.org/10.1080/1369118X.2012.678878",
             locator="15(5):662-679", locator_type="page_range",
             supports="big data as cultural phenomenon / six critical questions / data are constructed", verified=True),
        dict(kind="BOOK",
             title_en="Big Data: A Revolution That Will Transform How We Live, Work, and Think",
             title_fa="کلان‌داده: انقلابی که زندگی، کار و اندیشیدن ما را دگرگون می‌کند",
             authors="Mayer-Schonberger, V.; Cukier, K.", year=2013,
             publisher="Houghton Mifflin Harcourt",
             doi=None, url=None, language="en", isbn=None,
             citation="Mayer-Schonberger, V., & Cukier, K. (2013). Big data: A revolution that will transform how we live, work, and think. Houghton Mifflin Harcourt.",
             locator="work", locator_type="work",
             supports="volume, velocity, variety / data-driven prediction", verified=False),
    ],
    "MC-527": [
        dict(kind="BOOK",
             title_en="Surveiller et punir: Naissance de la prison",
             title_fa="نظارت و تنبیه: زایش زندان",
             authors="Foucault, M.", year=1975, publisher="Gallimard",
             doi=None, url=None, language="fr", isbn=None,
             citation="Foucault, M. (1975). Surveiller et punir: Naissance de la prison. Gallimard.",
             locator="pt. 3", locator_type="CHAPTER",
             supports="panopticism / disciplinary power / internalized surveillance", verified=True),
        dict(kind="BOOK",
             title_en="Discipline and Punish: The Birth of the Prison",
             title_fa="نظم و انضباط و تنبیه: زایش زندان",
             authors="Foucault, M.", year=1977, publisher="Pantheon",
             doi=None, url=None, language="en", isbn=None,
             citation="Foucault, M. (1977). Discipline and punish: The birth of the prison (A. Sheridan, Trans.). Pantheon.",
             locator="work", locator_type="work",
             supports="English translation of panopticism", verified=False),
        dict(kind="BOOK",
             title_en="Panopticon; or, the Inspection-House",
             title_fa="پانوپتیکن؛ یا خانه بازرسی",
             authors="Bentham, J.", year=1791, publisher="T. Payne",
             doi=None, url=None, language="en", isbn=None,
             citation="Bentham, J. (1791). Panopticon; or, the inspection-house. T. Payne.",
             locator="work", locator_type="work",
             supports="architectural origin of the panopticon", verified=False),
    ],
}

ENRICH = {
    "MC-522": {
        "summary": "(لازارسفلد و مرتون، ۱۹۵۴؛ مکفرسون و همکاران، ۲۰۰۱) همسانی یعنی گرایش افراد به پیوند با کسانی که در ویژگی‌های اجتماعی به آن‌ها شبیه‌اند: سن، تحصیلات، شغل، نگرش و رفتار. لازارسفلد و مرتون در مطالعه دوستی نشان دادند که دوستی بیش از تصادف، میان افراد هم‌ویژگی شکل می‌گیرد و این همسانی بر جریان اطلاعات اثر می‌گذارد. مکفرسون و همکاران در مرور گسترده پژوهش‌ها نشان دادند همسانی در ازدواج، دوستی، شبکه‌های آنلاین و سازمان‌ها الگویی پایدار است و دو سازوکار دارد: انتخاب (شباهت‌گزینی) و تأثیر (شبیه‌شدن پس از ارتباط).",
        "definition": "همسانی، گرایش به شکل‌دهی رابطه با افراد مشابه در ویژگی‌های جمعیت‌شناختی، نگرشی یا رفتاری است؛ گرایشی که ساختار شبکه، جریان اطلاعات و مرزهای گروه را شکل می‌دهد.",
        "main_problem": "مسئله این است که چرا شبکه‌های اجتماعی نامتقارن و خوشه‌ای‌اند. پاسخ در گرایش به شباهت است: افراد با کسانی ارتباط می‌گیرند که به آن‌ها شبیه‌اند و در طول رابطه نیز به هم شبیه‌تر می‌شوند. پرسش دوم، پیامد است: همسانی چه اثری بر دسترسی به اطلاعات تازه، تنوع دیدگاه و نابرابری فرصت دارد.",
        "mechanism": "۱. همسانی پایه: حتی در غیاب گرایش، تفاوت اندازه گروه‌ها باعث می‌شود پیوندهای درون‌گروهی بیشتر از پیوندهای بین‌گروهی باشد.\n۲. انتخاب و شباهت‌گزینی: افراد آگاهانه یا ناآگاهانه شبیه‌های خود را برای رابطه برمی‌گزینند.\n۳. تأثیر و شبیه‌شدن: ارتباط طولانی، نگرش و رفتار طرفین را به هم نزدیک می‌کند.\n۴. ابعاد همسانی: جمعیت‌شناختی، نگرشی و رفتاری؛ هر بُعد شبکه متفاوتی می‌سازد.\n۵. پیامد جریان اطلاعات: همسانی، دسترسی به اطلاعات تازه را محدود و خوشه‌های اطلاعاتی مشابه می‌سازد.\n۶. نهادها و زمینه: ازدواج، سازمان، محله و پلتفرم، فرصت‌های تماس و در نتیجه همسانی را شکل می‌دهند.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا شبکه‌های اجتماعی به خوشه‌های هم‌نظر تقسیم می‌شوند، چرا اخبار از مسیرهای مشابه می‌رسند و چرا تنوع دیدگاه در محیط الگوریتمی کاهش می‌یابد. نکته مهم این است که همسانی هم سازوکار انتخاب است و هم پیامد تأثیر؛ تفکیک این دو، مسئله اصلی سنجش است.",
        "assumptions": [
            "افراد به شباهت در رابطه گرایش دارند.",
            "همسانی، ساختار شبکه و جریان اطلاعات را شکل می‌دهد.",
            "همسانی از انتخاب و تأثیر هر دو پدید می‌آید.",
        ],
        "principles": [
            "همسانی، دسترسی به اطلاعات متنوع را محدود می‌کند.",
            "پیوندهای ضعیف، پل میان خوشه‌های ناهمگون‌اند.",
            "ساختار فرصت، دامنه همسانی را تعیین می‌کند.",
        ],
        "critiques": [
            "۱. علیت معکوس: تفکیک انتخاب از تأثیر در داده‌های مقطعی دشوار است.\n۲. سنجش ویژگی: تعریف و وزن ویژگی‌های شبیه‌ساز، به پژوهش وابسته است.\n۳. نمونه‌های محدود: بسیاری از مطالعات بر شبکه‌های کوچک و زمینه خاص استوارند.\n۴. کم‌توجهی به پیوندهای ضعیف: تمرکز بر پیوندهای قوی، تنوع شبکه را کم‌نمایی می‌کند.\n۵. همسانی الگوریتمی: توصیه‌گرها می‌توانند همسانی را تشدید و از انتخاب طبیعی جدا کنند.",
        ],
        "applications": [
            "تحلیل شبکه اجتماعی: سنجش خوشه‌بندی و تنوع تماس.",
            "طراحی پلتفرم: کاهش همسانی الگوریتمی و افزایش مواجهه با دیدگاه‌های متفاوت.",
            "بازاریابی: شناسایی مسیرهای انتشار در خوشه‌های هم‌ویژگی.",
            "سیاست عمومی: تحلیل نابرابری فرصت ناشی از شبکه‌های همسان.",
        ],
        "evolution": "لازارسفلد و مرتون در ۱۹۵۴ همسانی را در مطالعه دوستی صورت‌بندی کردند و مکفرسون و همکاران در ۲۰۰۱ آن را به نظریه‌ای عمومی شبکه گستردند؛ پژوهش بعدی، همسانی الگوریتمی و اتاق‌های پژواک را افزود.",
        "key_concepts": [
            "همسانی (Homophily)",
            "همسانی پایه (Baseline Homophily)",
            "شباهت‌گزینی (Selection)",
            "تأثیر اجتماعی (Influence)",
            "خوشه اطلاعاتی (Information Cluster)",
            "پیوند ضعیف (Weak Tie)",
        ],
        "studies": [
            "Lazarsfeld, P. F., & Merton, R. K. (1954). Friendship as a social process. In Freedom and control in modern society (pp. 18-66). Van Nostrand.",
            "McPherson, J. M., Smith-Lovin, L., & Cook, J. M. (2001). Birds of a feather. Annual Review of Sociology, 27, 415-444.",
        ],
        "theorists": "لازارسفلد و مرتون؛ مکفرسون و همکاران",
        "theorists_text": "لازارسفلد و مرتون (۱۹۵۴)؛ مکفرسون و همکاران (۲۰۰۱)",
        "year": 1954,
        "model": "مدل دو سازوکار: ساختار فرصت + انتخاب شباهت‌محور → پیوند همسان → تأثیر و شبیه‌شدن متقابل → خوشه‌بندی شبکه و محدودیت جریان اطلاعات.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nهمسانی، پیوند نظریه شبکه و جامعه‌شناسی ارتباطات است. نوآوری لازارسفلد و مرتون، نشان دادن اثر همسانی بر جریان اطلاعات بود؛ و مکفرسون و همکاران آن را به الگویی فراگیر در شبکه‌های اجتماعی گستردند.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با شاخص همسانی و تحلیل شبکه انجام می‌شود. پژوهش‌هایی که تنها نسبت پیوندهای همسان را می‌سنجند، همسانی پایه را نادیده می‌گیرند؛ و پژوهش‌هایی که تنها نگرش را می‌سنجند، ساختار فرصت را از دست می‌دهند.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در توضیح خوشه‌بندی و محدودیت اطلاعات است، اما باید با تحلیل محتوا و الگوریتم تکمیل شود. در پلتفرم‌ها، همسانی نه فقط انتخاب کاربر، بلکه پیامد طراحی و توصیه است.",
        "critique_text": "\n".join([
            "۱. علیت معکوس: تفکیک انتخاب از تأثیر دشوار است.",
            "۲. سنجش ویژگی: وزن ویژگی‌های شبیه‌ساز به پژوهش وابسته است.",
            "۳. نمونه‌های محدود: مطالعات بر شبکه‌های کوچک استوارند.",
            "۴. کم‌توجهی به پیوندهای ضعیف: تنوع شبکه کم‌نمایی می‌شود.",
            "۵. همسانی الگوریتمی: توصیه‌گرها همسانی را تشدید می‌کنند.",
        ]),
        "example_text": "در یک سازمان، کارکنان بخش فنی بیشتر با همکاران فنی خود ناهار می‌خورند و اطلاعات پروژه‌های دیگر را دیرتر می‌شنوند. این همسانی، هم انتخاب است (شباهت علاقه) و هم تأثیر (زبان مشترک)؛ نتیجه، خوشه اطلاعاتی و کندی هماهنگی میان‌بخشی است.",
    },
    "MC-523": {
        "summary": "(راجرز، ۱۹۶۲) راجرز نشان داد نوآوری در یک نظام اجتماعی از مسیر ارتباطات میان افراد منتشر می‌شود و پذیرش آن از الگویی مشخص پیروی می‌کند: مبتکران، پذیرندگان اولیه، اکثریت اولیه، اکثریت دیرهنگام و واپس‌ماندگان. پنج ویژگی نوآوری بر سرعت پذیرش اثر می‌گذارد: مزیت نسبی، سازگاری، پیچیدگی، آزمون‌پذیری و قابلیت مشاهده. کانال‌های ارتباطی، عاملان تغییر و هنجارهای نظام اجتماعی، سرعت و الگوی انتشار را تعیین می‌کنند.",
        "definition": "تسهیم نوآوری، فرایندی است که در آن یک نوآوری از طریق کانال‌های ارتباطی در طول زمان میان اعضای یک نظام اجتماعی منتشر می‌شود و به پذیرش یا رد می‌انجامد.",
        "main_problem": "مسئله این است که چرا برخی نوآوری‌ها سریع منتشر می‌شوند و برخی کند یا هرگز. پاسخ در ترکیب ویژگی نوآوری، کانال ارتباطی و ساختار نظام اجتماعی است. پرسش دوم، الگوی پذیرش است: چه کسانی زودتر می‌پذیرند و این الگو چه پیامدی برای نابرابری دارد.",
        "mechanism": "۱. چهار عنصر: نوآوری، کانال ارتباطی، زمان و نظام اجتماعی؛ بدون هر چهار، انتشار فهم نمی‌شود.\n۲. منحنی پذیرش: شمار پذیرندگان در طول زمان، الگویی زنگوله‌ای می‌سازد و پذیرندگان را به پنج دسته تقسیم می‌کند.\n۳. پنج ویژگی نوآوری: مزیت نسبی، سازگاری، پیچیدگی، آزمون‌پذیری و قابلیت مشاهده، سرعت پذیرش را تعیین می‌کنند.\n۴. کانال‌های ارتباطی: رسانه جمعی آگاهی می‌سازد و ارتباط میان‌فردی، متقاعد می‌کند.\n۵. عامل تغییر و رهبران نظر: واسطه‌ها و افراد معتبر، پل میان نوآوری و پذیرندگان دیرهنگام‌اند.\n۶. بازآفرینی و پیامد: نوآوری در عمل تغییر می‌کند و پیامدهای مطلوب و نامطلوب می‌سازد.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا رسانه‌های تازه از مسیر پذیرندگان اولیه و رهبران نظر منتشر می‌شوند، چرا آموزش و نمایش کاربرد، پذیرش را تسریع می‌کند و چرا شکاف پذیرش میان گروه‌ها پدید می‌آید. نکته مهم این است که مدل به نوآوری و پذیرش آن گرایش مثبت دارد؛ باید با پرسش از پیامد و نابرابری تعدیل شود.",
        "assumptions": [
            "انتشار نوآوری از طریق ارتباطات اجتماعی رخ می‌دهد.",
            "پذیرش، فرایندی مرحله‌ای و زمان‌مند است.",
            "ویژگی‌های نوآوری، سرعت پذیرش را تعیین می‌کنند.",
        ],
        "principles": [
            "ارتباط میان‌فردی، متقاعدسازی را ممکن می‌کند.",
            "نمایش و آزمون‌پذیری، ابهام را کاهش می‌دهد.",
            "رهبران نظر، مسیر انتشار را شکل می‌دهند.",
        ],
        "critiques": [
            "۱. سوگیری به نفع نوآوری: مدل، پذیرش را مطلوب و مقاومت را مشکل می‌بیند.\n۲. مقصر دانستن مقاومت: مخالفت می‌تواند انتقاد مشروع باشد.\n۳. نمونه کشاورزی و غربی: شواهد اولیه به زمینه خاص محدود است.\n۴. کم‌توجهی به قدرت: نابرابری دسترسی و منافع سازندگان نوآوری کمتر تحلیل می‌شود.\n۵. انتشار پلتفرمی: در محیط شبکه‌ای، انتشار سریع، ناهموار و آمیخته با سوگیری است.",
        ],
        "applications": [
            "بازاریابی فناوری: طراحی پیام بر پایه پنج ویژگی نوآوری.",
            "بهداشت عمومی: استفاده از رهبران نظر برای پذیرش رفتار سالم.",
            "سیاست فناوری: شناسایی شکاف پذیرش میان گروه‌ها.",
            "آموزش: نمایش کاربرد و کاهش پیچیدگی برای تسریع پذیرش.",
        ],
        "evolution": "راجرز مدل را در ۱۹۶۲ صورت‌بندی کرد و در ویرایش‌های بعدی، به‌ویژه ویرایش پنجم ۲۰۰۳، آن را با اینترنت و شبکه‌های اجتماعی گسترد. پژوهش بعدی، نقد سوگیری نوآوری و تحلیل نابرابری پذیرش را افزود.",
        "key_concepts": [
            "نوآوری (Innovation)",
            "کانال ارتباطی (Communication Channel)",
            "نظام اجتماعی (Social System)",
            "دسته‌های پذیرنده (Adopter Categories)",
            "مزیت نسبی (Relative Advantage)",
            "قابلیت مشاهده (Observability)",
        ],
        "studies": [
            "Rogers, E. M. (2003). Diffusion of innovations (5th ed.). Free Press.",
            "Rogers, E. M. (1962). Diffusion of innovations. Free Press.",
        ],
        "theorists": "اورت راجرز (۱۹۶۲)",
        "theorists_text": "اورت راجرز (۱۹۶۲؛ ۲۰۰۳)",
        "year": 1962,
        "model": "مدل انتشار: نوآوری + کانال + زمان + نظام اجتماعی → آگاهی → متقاعدسازی → تصمیم → اجرا → تأیید؛ با منحنی پذیرش و پنج دسته پذیرنده.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nراجرز، پژوهش‌های پراکنده انتشار را در یک مدل مرحله‌ای جمع کرد. نوآوری او این بود که انتشار را فرایندی اجتماعی و ارتباطی دید، نه رویدادی فنی؛ از این رو کانال، رهبر نظر و نظام اجتماعی به تحلیل افزوده شد.\n\n۲. منطق سنجش و دام‌های آن\nسنجش نیازمند داده طولی درباره زمان پذیرش و ویژگی پذیرندگان است. پژوهش‌هایی که تنها تصمیم نهایی را می‌سنجند، مراحل میانی را از دست می‌دهند؛ و پژوهش‌هایی که تنها ویژگی نوآوری را می‌سنجند، ساختار اجتماعی را نادیده می‌گیرند.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در توضیح سرعت و الگوی پذیرش است، اما باید با نقد پیامد و قدرت تعدیل شود. در محیط پلتفرمی، انتشار می‌تواند سریع و جهانی باشد، اما الگوی پذیرش همچنان نابرابر می‌ماند.",
        "critique_text": "\n".join([
            "۱. سوگیری به نفع نوآوری: مقاومت به‌عنوان مشکل دیده می‌شود.",
            "۲. مقصر دانستن مقاومت: مخالفت می‌تواند انتقاد مشروع باشد.",
            "۳. نمونه کشاورزی و غربی: شواهد اولیه محدود است.",
            "۴. کم‌توجهی به قدرت: نابرابری دسترسی کمتر تحلیل می‌شود.",
            "۵. انتشار پلتفرمی: انتشار سریع و آمیخته با سوگیری است.",
        ]),
        "example_text": "یک اپلیکیشن سلامت ابتدا میان مبتکران و پذیرندگان اولیه رواج می‌یابد؛ نمایش نتیجه در شبکه دوستان، اعتماد می‌سازد و اکثریت را جذب می‌کند. گروه‌هایی که دسترسی یا مهارت کمتری دارند، دیرتر می‌پذیرند و شکاف سلامت دیجیتال پایدار می‌ماند.",
    },
    "MC-525": {
        "summary": "(بوید و کرافورد، ۲۰۱۲) کلان‌داده فقط حجم زیاد داده نیست؛ پدیده‌ای فرهنگی، فناوری و علمی است که بر باور به توانایی داده برای شناخت رفتار تکیه دارد. بوید و کرافورد شش پرسش انتقادی مطرح کردند: کلان‌داده چه معنایی دارد، آیا بزرگ‌تر یعنی بهتر، چه چیزی از داده حذف می‌شود، آیا داده خام وجود دارد، اخلاق و حریم چه می‌شود و تقسیم‌بندی پژوهش چگونه تغییر می‌کند. آنها نشان دادند داده برساخته است و بی‌طرف نیست.",
        "definition": "کلان‌داده، پدیده‌ای فرهنگی و فناورانه است که بر تولید، ذخیره و تحلیل حجم بزرگی از داده برای کشف الگو تکیه دارد؛ پدیده‌ای که با باور به عینیت داده، پرسش‌های اخلاقی و روش‌شناختی تازه‌ای می‌سازد.",
        "main_problem": "مسئله این است که آیا حجم بزرگ داده، شناخت بهتری می‌دهد. بوید و کرافورد پاسخ می‌دهند که حجم، کیفیت و اعتبار را تضمین نمی‌کند؛ داده، محصول انتخاب، ابزار و زمینه است. پرسش دوم، قدرت است: چه کسی داده را جمع می‌کند، چه کسی تفسیر می‌کند و پیامد آن برای حریم و عدالت چیست.",
        "mechanism": "۱. حجم، سرعت و تنوع: کلان‌داده با مقیاس و تنوع منابع تعریف می‌شود، اما این تعریف فنی، ماهیت اجتماعی آن را پنهان می‌کند.\n۲. توهم خام‌بودن داده: هیچ داده‌ای خام نیست؛ انتخاب، دسته‌بندی و ابزار، داده را می‌سازند.\n۳. نمونه‌گیری و سوگیری: داده بزرگ نیز از جهان نمونه می‌گیرد و گروه‌های بی‌صدا را حذف می‌کند.\n۴. حریم و اخلاق: جمع‌آوری داده بدون رضایت آگاهانه، پرسش عدالت و نظارت را مطرح می‌کند.\n۵. قدرت و دسترسی: شرکت‌ها و دولت‌ها مالک داده‌اند و پژوهشگر مستقل دسترسی محدود دارد.\n۶. تفسیر و زمینه: الگو بدون نظریه و زمینه، می‌تواند گمراه‌کننده باشد.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا سنجه‌های پلتفرم، سیاست محتوا را شکل می‌دهند، چرا داده رفتاری به منبع قدرت تجاری بدل شده و چرا حریم و تبعیض الگوریتمی موضوع سیاست عمومی است. نکته مهم این است که کلان‌داده، ابزار نیست؛ نظامی از دانش و قدرت است.",
        "assumptions": [
            "داده، برساخته و وابسته به زمینه است.",
            "حجم داده، اعتبار شناخت را تضمین نمی‌کند.",
            "جمع‌آوری و تحلیل داده، پرسش اخلاقی و سیاسی می‌سازد.",
        ],
        "principles": [
            "داده خام وجود ندارد.",
            "نمونه‌گیری، حتی در مقیاس بزرگ، سوگیری می‌سازد.",
            "شفافیت و رضایت، شرط اخلاقی پژوهش داده است.",
        ],
        "critiques": [
            "۱. تعریف مبهم: مرز کلان‌داده با داده معمولی روشن نیست.\n۲. رمانتیک‌سازی داده: نقد خوب است، اما جایگزین روش‌شناختی روشنی پیشنهاد نمی‌شود.\n۳. کم‌توجهی به زیرساخت: مالکیت سرور و انرژی، کمتر تحلیل می‌شود.\n۴. سنجش کیفیت: معیار ارزیابی داده و الگو همچنان محل بحث است.\n۵. تحول هوش مصنوعی: مدل‌های مولد، پرسش داده آموزشی و سوگیری را تشدید کرده‌اند.",
        ],
        "applications": [
            "اخلاق داده: طراحی رضایت آگاهانه و حریم.",
            "سیاست پلتفرم: تحلیل قدرت داده و شفافیت الگوریتم.",
            "روش پژوهش: ترکیب تحلیل کلان‌داده با زمینه و نظریه.",
            "سواد داده: آموزش خوانش انتقادی نمودار و سنجه.",
        ],
        "evolution": "بوید و کرافورد در ۲۰۱۲ نقد فرهنگی و روش‌شناختی کلان‌داده را صورت‌بندی کردند. پژوهش بعدی، مفهوم را با هوش مصنوعی، داده‌محوری و عدالت الگوریتمی گسترد.",
        "key_concepts": [
            "کلان‌داده (Big Data)",
            "توهم خام‌بودن (Raw Data Fallacy)",
            "سوگیری نمونه (Sampling Bias)",
            "حریم داده (Data Privacy)",
            "عدالت الگوریتمی (Algorithmic Fairness)",
            "داده‌محوری (Datafication)",
        ],
        "studies": [
            "boyd, d., & Crawford, K. (2012). Critical questions for big data. Information, Communication & Society, 15(5), 662-679.",
            "Mayer-Schonberger, V., & Cukier, K. (2013). Big data. Houghton Mifflin Harcourt.",
        ],
        "theorists": "بوید و کرافورد (۲۰۱۲)",
        "theorists_text": "بوید و کرافورد (۲۰۱۲)",
        "year": 2012,
        "model": "مدل انتقادی شش‌پرسشی: معنای داده، کیفیت، گزینش، خامی، اخلاق و تقسیم پژوهش → داده به‌عنوان برساخته فرهنگی و ابزار قدرت.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nنقد بوید و کرافورد، کلان‌داده را از حوزه فنی به حوزه فرهنگ و قدرت برد. نوآوری آنها این بود که نشان دادند داده، پیش از تحلیل نیز انتخاب و تفسیر شده است؛ از این رو ادعای عینیت داده، نادرست است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش نیازمند مستندسازی منبع، روش نمونه‌گیری و تفسیر است. پژوهش‌هایی که تنها نتیجه الگو را گزارش می‌کنند، مسیر ساخت داده را پنهان می‌کنند؛ و پژوهش‌هایی که تنها حجم داده را می‌سنجند، کیفیت را نادیده می‌گیرند.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در پیوند داده و قدرت است، اما جایگزین روش‌شناختی کاملی ارائه نمی‌دهد. در محیط هوش مصنوعی، پرسش داده آموزشی، سوگیری و پاسخ‌گویی، شکل تازه‌ای از همان نقد است.",
        "critique_text": "\n".join([
            "۱. تعریف مبهم: مرز کلان‌داده با داده معمولی روشن نیست.",
            "۲. رمانتیک‌سازی داده: جایگزین روش‌شناختی روشنی پیشنهاد نمی‌شود.",
            "۳. کم‌توجهی به زیرساخت: مالکیت سرور و انرژی کمتر تحلیل می‌شود.",
            "۴. سنجش کیفیت: معیار ارزیابی داده محل بحث است.",
            "۵. تحول هوش مصنوعی: داده آموزشی و سوگیری، پرسش تازه‌ای ساخته است.",
        ]),
        "example_text": "پلتفرمی اعلام می‌کند داده‌هایش نشان می‌دهد کاربران محتوای کوتاه را ترجیح می‌دهند و تولید محتوای بلند را کاهش می‌دهد. پرسش انتقادی این است: چه محتوایی در داده ثبت شده، چه گروهی حذف شده و چه کسی این الگو را تفسیر کرده است؟",
    },
    "MC-527": {
        "summary": "(فوکو، ۱۹۷۵) فوکو در «نظارت و تنبیه» پانوپتیکن بنتام را نه طرحی معماری، بلکه الگوی قدرت مدرن خواند: برجی مرکزی که زندانی نمی‌داند دیده می‌شود یا نه، و همین نامعلومی، خودتنظیمی می‌سازد. قدرت از نمایش شکنجه به نظارت پیوسته و درونی‌شده منتقل می‌شود؛ نظم و انضباط در زندان، بیمارستان، مدرسه و کارخانه تعمیم می‌یابد. نتیجه، جامعه‌ای است که اعضایش خود را ناظر خود می‌کنند.",
        "definition": "پانوپتیکن، الگوی معماری و سازوکار قدرت انضباطی است که با نظارت نامعلوم و پیوسته، فرد را به خودتنظیمی وامی‌دارد و مرز میان نهادهای تنبیهی و جامعه را کم‌رنگ می‌کند.",
        "main_problem": "مسئله این است که قدرت مدرن چگونه بدون خشونت آشکار، نظم را حفظ می‌کند. پاسخ فوکو در سازوکار نظارت است: وقتی فرد نداند دیده می‌شود یا نه، خود را چنان رفتار می‌کند که گویی همیشه دیده می‌شود. پرسش دوم، گستره است: تا چه حد این سازوکار از زندان به مدرسه، بیمارستان، کارخانه و رسانه گسترش یافته است.",
        "mechanism": "۱. معماری برج مرکزی: ساختار فضا، دیدن را ممکن و دیده‌شدن را نامعلوم می‌کند.\n۲. نامعلومی نظارت: عدم قطعیت، هزینه نظارت را از ناظر به سوژه منتقل می‌کند.\n۳. خودتنظیمی: سوژه، رفتار خود را بر پایه احتمال نظارت تنظیم می‌کند.\n۴. قدرت انضباطی: تمرین، زمان‌بندی و فضا، بدن را شکل‌پذیر و قابل مدیریت می‌کند.\n۵. تعمیم نهادی: همان سازوکار در مدرسه، بیمارستان، پادگان و کارخانه تکرار می‌شود.\n۶. دانش و قدرت: مشاهده پیوسته، سوژه را قابل شناخت و دسته‌بندی می‌کند و دانش تازه می‌سازد.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا نظارت دیجیتال، داده رفتاری و سنجه‌های عملکرد، رفتار را بدون دستور مستقیم شکل می‌دهند، چرا کاربران خود را برای دوربین و الگوریتم تنظیم می‌کنند و چرا حریم خصوصی مسئله‌ای سیاسی است. نکته مهم این است که فوکو، پانوپتیکن را استعاره‌ای برای سازوکار قدرت می‌داند، نه توصیف یک زندان.",
        "assumptions": [
            "قدرت مدرن از طریق نظارت و انضباط عمل می‌کند.",
            "نامعلومی نظارت، خودتنظیمی می‌سازد.",
            "سازوکارهای نهادی، الگوی واحدی دارند.",
        ],
        "principles": [
            "دیده‌شدن نامعلوم، مؤثرتر از نظارت آشکار است.",
            "فضا و زمان، ابزار قدرت انضباطی‌اند.",
            "دانش درباره سوژه، ابزار کنترل اوست.",
        ],
        "critiques": [
            "۱. تعمیم افراطی: همه نهادها را با یک الگو تحلیل می‌کند.\n۲. کم‌توجهی به مقاومت: سوژه‌ها همیشه منقاد نیستند.\n۳. نمونه تاریخی: تحلیل بر اروپای مدرن متمرکز است.\n۴. سنجش دشوار: قدرت انضباطی به‌سختی قابل اندازه‌گیری است.\n۵. نظارت دیجیتال: پانوپتیکن معکوس و نظارت افقی، الگوی فوکو را به چالش می‌کشد.",
        ],
        "applications": [
            "مطالعات نظارت: تحلیل دوربین، داده و سنجه عملکرد.",
            "حریم خصوصی: نقد نظارت پیوسته در پلتفرم‌ها.",
            "جامعه‌شناسی سازمان: تحلیل انضباط در محل کار.",
            "مطالعات رسانه: بررسی خودتنظیمی کاربران در محیط دیجیتال.",
        ],
        "evolution": "بنتام طرح پانوپتیکن را در ۱۷۹۱ منتشر کرد؛ فوکو در ۱۹۷۵ آن را به الگوی قدرت انضباطی بدل کرد. پژوهش بعدی، مفهوم را به نظارت دیجیتال، داده و نظارت افقی شبکه‌ای گسترد.",
        "key_concepts": [
            "پانوپتیکن (Panopticon)",
            "قدرت انضباطی (Disciplinary Power)",
            "نظارت درونی‌شده (Internalized Surveillance)",
            "سوژه مشاهده‌پذیر (Observable Subject)",
            "دانش-قدرت (Power-Knowledge)",
            "نهاد انضباطی (Disciplinary Institution)",
        ],
        "studies": [
            "Foucault, M. (1975). Surveiller et punir. Gallimard.",
            "Foucault, M. (1977). Discipline and punish. Pantheon.",
            "Bentham, J. (1791). Panopticon; or, the inspection-house. T. Payne.",
        ],
        "theorists": "میشل فوکو (۱۹۷۵)",
        "theorists_text": "میشل فوکو (۱۹۷۵)؛ با ریشه معماری در جرمی بنتام (۱۷۹۱)",
        "year": 1975,
        "model": "مدل انضباطی: فضای قابل مشاهده + نظارت نامعلوم → خودتنظیمی سوژه → تعمیم نهادی → جامعه انضباطی.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nفوکو، طرح بنتام را از سطح اصلاح زندان به سطح تحلیل قدرت برد. نوآوری او این بود که نشان داد قدرت مدرن، نه با نمایش، بلکه با نظارت و دانش عمل می‌کند؛ ایده‌ای که پایه مطالعات نظارت شد.\n\n۲. منطق سنجش و دام‌های آن\nسنجش نیازمند تحلیل فضا، رویه و خودتنظیمی سوژه است. پژوهش‌هایی که تنها فناوری نظارت را می‌سنجند، اثر آن بر رفتار را از دست می‌دهند؛ و پژوهش‌هایی که تنها تجربه سوژه را می‌شنوند، ساختار قدرت را نمی‌بینند.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در پیوند نظارت و خودتنظیمی است، اما باید برای محیط شبکه‌ای تعدیل شود. در پلتفرم‌ها، نظارت هم از بالا و هم از سوی همسالان اعمال می‌شود و مرز ناظر و سوژه مخدوش شده است.",
        "critique_text": "\n".join([
            "۱. تعمیم افراطی: همه نهادها با یک الگو تحلیل می‌شوند.",
            "۲. کم‌توجهی به مقاومت: سوژه‌ها همیشه منقاد نیستند.",
            "۳. نمونه تاریخی: تحلیل بر اروپای مدرن متمرکز است.",
            "۴. سنجش دشوار: قدرت انضباطی به‌سختی اندازه‌گیری می‌شود.",
            "۵. نظارت دیجیتال: نظارت افقی، الگوی فوکو را به چالش می‌کشد.",
        ]),
        "example_text": "کارمندی که می‌داند فعالیت صفحه‌اش ممکن است ثبت شود، خود را حتی در نبود نظارت مستقیم مهار می‌کند. همین خودتنظیمی، سازوکار پانوپتیکن است: ناظر لازم نیست همیشه حاضر باشد؛ احتمال حضور کافی است.",
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
    total = structure + analysis + citation + accuracy + relations + classification + clarity + currency
    detail = {"structure_15": structure, "analysis_15": analysis, "citation_20": citation,
              "accuracy_25_auto": accuracy, "relations_10": relations,
              "classification_5": classification, "clarity_5": clarity, "currency_5": currency}
    return total, detail, words


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

        if code == "MC-525":
            cur.execute("UPDATE kb_entities SET canonical_name_en=%s WHERE id=%s",
                        ("Big Data Studies", eid))
            cur.execute("""INSERT INTO kb_audit_log (entity_code,action,detail,source,created_at)
                VALUES (%s,'DOC_FIX',%s,%s,%s)""",
                        (code, json.dumps({"fix": "canonical_name_en repaired: Glocalization -> Big Data Studies (mismatch with canonical_name_fa)"},
                                          ensure_ascii=False), STAMP, NOW))

        cur.execute("UPDATE kb_entities SET properties=%s, version=version+1, updated_at=%s WHERE id=%s",
                    (json.dumps(p, ensure_ascii=False), NOW, eid))
        cur.execute("SELECT version FROM kb_entities WHERE id=%s", (eid,))
        new_version = cur.fetchone()[0]

        for src in S[code]:
            sid = ensure_source(cur, src)
            cur.execute("SELECT id FROM kb_evidence WHERE about_code=%s AND source_id=%s LIMIT 1", (code, sid))
            if cur.fetchone():
                continue
            lt = {"work": "SECTION", "page_range": "PAGE", "CHAPTER": "CHAPTER"}.get(src["locator_type"], "SECTION")
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
                                       "verified": n_verified, "batch": 95}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH95 THEORY DONE")


if __name__ == "__main__":
    main()
