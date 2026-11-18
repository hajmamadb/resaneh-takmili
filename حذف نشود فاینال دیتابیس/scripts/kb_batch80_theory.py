# -*- coding: utf-8 -*-
"""Batch 80: full documentation for MC-420, MC-422, MC-424, MC-425."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch80-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch80_theory.json"

S = {
    "MC-420": [
        dict(kind="BOOK",
             title_en="Media Archaeology: Approaches, Applications, and Implications",
             title_fa="باستان‌شناسی رسانه: رویکردها، کاربردها و دلالت‌ها",
             authors="Huhtamo, E.; Parikka, J. (eds.)", year=2011,
             publisher="University of California Press",
             doi=None, url="https://www.ucpress.edu/books/media-archaeology/paper",
             language="en", isbn=None,
             citation="Huhtamo, E., & Parikka, J. (Eds.). (2011). Media archaeology: Approaches, applications, and implications. University of California Press.",
             locator="work", locator_type="work",
             supports="media archaeology approaches / topoi / counter-history", verified=True),
        dict(kind="BOOK",
             title_en="What is Media Archaeology?",
             title_fa="باستان‌شناسی رسانه چیست؟",
             authors="Parikka, J.", year=2012, publisher="Polity Press",
             doi=None, url=None, language="en", isbn=None,
             citation="Parikka, J. (2012). What is media archaeology? Polity Press.",
             locator="work", locator_type="work",
             supports="systematic overview / methods", verified=False),
    ],
    "MC-422": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Strength of Weak Ties",
             title_fa="قدرت پیوندهای ضعیف",
             authors="Granovetter, M. S.", year=1973, publisher="University of Chicago Press",
             doi="10.1086/225469",
             url="https://www.journals.uchicago.edu/doi/10.1086/225469",
             language="en", isbn=None,
             citation="Granovetter, M. S. (1973). The strength of weak ties. American Journal of Sociology, 78(6), 1360-1380.",
             locator="pp. 1360-1380", locator_type="page_range",
             supports="tie strength / bridges / forbidden triad", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Strength of Weak Ties: A Network Theory Revisited",
             title_fa="قدرت پیوندهای ضعیف: بازبینی نظریه شبکه",
             authors="Granovetter, M. S.", year=1982, publisher="Wiley",
             doi=None, url=None, language="en", isbn=None,
             citation="Granovetter, M. S. (1982). The strength of weak ties: A network theory revisited. Sociological Theory, 1, 201-233.",
             locator="pp. 201-233", locator_type="page_range",
             supports="elaboration / diffusion implications", verified=False),
    ],
    "MC-424": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Collective Dynamics of 'Small-World' Networks",
             title_fa="دینامیک جمعی شبکه‌های «جهان کوچک»",
             authors="Watts, D. J.; Strogatz, S. H.", year=1998, publisher="Nature",
             doi="10.1038/30918", url="https://www.nature.com/articles/30918",
             language="en", isbn=None,
             citation="Watts, D. J., & Strogatz, S. H. (1998). Collective dynamics of 'small-world' networks. Nature, 393(6684), 440-442.",
             locator="pp. 440-442", locator_type="page_range",
             supports="small-world model / clustering and path length", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Small World Problem",
             title_fa="مسئله جهان کوچک",
             authors="Milgram, S.", year=1967, publisher="Psychology Today",
             doi=None, url=None, language="en", isbn=None,
             citation="Milgram, S. (1967). The small world problem. Psychology Today, 2(1), 60-67.",
             locator="pp. 60-67", locator_type="page_range",
             supports="six degrees / empirical precursor", verified=False),
    ],
    "MC-425": [
        dict(kind="BOOK",
             title_en="Structural Holes: The Social Structure of Competition",
             title_fa="سوراخ‌های ساختاری: ساختار اجتماعی رقابت",
             authors="Burt, R. S.", year=1992, publisher="Harvard University Press",
             doi="10.4159/9780674029095",
             url="https://www.hup.harvard.edu/books/9780674843714",
             language="en", isbn="9780674843714",
             citation="Burt, R. S. (1992). Structural holes: The social structure of competition. Harvard University Press.",
             locator="work", locator_type="work",
             supports="brokerage / information and control benefits", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Structural Holes and Good Ideas",
             title_fa="سوراخ‌های ساختاری و ایده‌های خوب",
             authors="Burt, R. S.", year=2004, publisher="University of Chicago Press",
             doi=None, url=None, language="en", isbn=None,
             citation="Burt, R. S. (2004). Structural holes and good ideas. American Journal of Sociology, 110(2), 349-399.",
             locator="pp. 349-399", locator_type="page_range",
             supports="brokerage and idea value", verified=False),
    ],
}

ENRICH = {
    "MC-420": {
        "summary": "(هوتامو و پاریکا، ۲۰۱۱) باستان‌شناسی رسانه رویکردی است که با حفاری در آرشیوها، رسانه‌های فراموش‌شده، پروژه‌های شکست‌خورده و ایده‌های تکرارشونده، روایت خطی پیشرفت فناورانه را به چالش می‌کشد. این رویکرد به‌جای تاریخ «پیروزمندان»، به حاشیه‌ها و زمان‌های چندلایه رسانه توجه می‌کند. هوتامو و پاریکا آن را نه یک مکتب واحد، بلکه مجموعه‌ای از رویکردهای ناهمگن با الهام از فوکو، کیتلر و تاریخ عمیق رسانه می‌دانند.",
        "definition": "باستان‌شناسی رسانه، روشی برای مطالعه رسانه است که بر مادیت، آرشیو و تداوم‌های پنهان تأکید می‌کند. برخلاف تاریخ رسانه که معمولاً از گذشته به حال و به‌سوی «نوآوری» حرکت می‌کند، این رویکرد از حال به گذشته بازمی‌گردد تا ببیند چه ایده‌ها، دستگاه‌ها و مسیرهایی کنار گذاشته شده‌اند و چگونه بازمی‌گردند.",
        "main_problem": "مسئله این است که تاریخ رسانه اغلب به روایت پیشرفت خطی تقلیل می‌یابد و جایگزین‌ها، شکست‌ها و تداوم‌ها را پنهان می‌کند. باستان‌شناسی رسانه می‌پرسد چه چیزی از میدان دید حذف شده و آن حذف چه اثری بر درک ما از رسانه امروز دارد.",
        "mechanism": "\n".join([
            "۱. حفاری آرشیو: جست‌وجو در اسناد، کاتالوگ‌ها، مجلات و دستگاه‌های فراموش‌شده به‌جای تکیه بر تاریخ رسمی نوآوری.",
            "۲. توپوی رسانه‌ای: ایده‌ها و آرزوهای تکرارشونده (مثل «حضور از راه دور») که در دوره‌های مختلف بازمی‌گردند و لباس فنی تازه می‌پوشند.",
            "۳. نقد روایت خطی: پیشرفت فناورانه نه زنجیره‌ای یک‌طرفه، بلکه مجموعه‌ای از گسست‌ها، بازگشت‌ها و مسیرهای مسدود است.",
            "۴. ماده‌گرایی رسانه‌ای: تأکید بر سخت‌افزار، کد، استاندارد و شرایط مادی، نه فقط محتوا و بازنمایی.",
            "۵. زمان عمیق رسانه: پیوند رسانه معاصر با لایه‌های تاریخی دورتر (از خط و چاپ تا ماشین حساب و اتوماتا).",
            "۶. تاریخ جایگزین به‌عنوان منبع نقد: بازخوانی شکست‌ها، امکان‌های رهاشده و طراحی‌های متفاوت را در برابر وضع موجود باز می‌کند.",
            "در بستر رسانه، باستان‌شناسی رسانه ابزار نقد روایت‌های «انقلاب دیجیتال» است: پلتفرم‌هایی که خود را بی‌سابقه معرفی می‌کنند، اغلب ایده‌های قدیمی تلویزیون، تلفن و پست را بازسازی می‌کنند. پژوهشگر با حفاری در پروژه‌های شکست‌خورده (شهرهای کابلی، رسانه‌های تعاملی اولیه، آرشیوهای توزیع‌شده) نشان می‌دهد که مسیر فعلی یکی از چند مسیر ممکن بوده است. همین بینش، طراحی امروز را از جبر فناورانه آزاد می‌کند و پرسش از جایگزین‌ها را ممکن می‌سازد.",
        ]),
        "assumptions": [
            "تاریخ رسانه چندلایه و ناپیوسته است، نه خطی.",
            "آرشیو و مادیت رسانه، منبع اصلی تحلیل‌اند.",
            "شکست‌ها و حاشیه‌ها به‌اندازه پیروزی‌ها معنادارند.",
        ],
        "principles": [
            "از حال به گذشته بازگردید، نه صرفاً از گذشته به حال.",
            "به تداوم ایده‌ها و بازگشت آن‌ها توجه کنید.",
            "مادیت رسانه را جدی بگیرید.",
        ],
        "critiques": [
            "کنجکاوی بی‌جهت: تمرکز بر اشیای عجیب و فراموش‌شده می‌تواند به مجموعه‌داری و توصیف بی‌سنتز فروبکاهد.",
            "ناهمگونی نظری: ترکیب فوکو، کیتلر و تاریخ هنر، چارچوب واحدی نمی‌سازد و مرز روشن تحلیل را دشوار می‌کند.",
            "ضعف اقتصاد سیاسی: قدرت شرکت‌ها، سرمایه و سیاست در بسیاری از روایت‌ها غایب است.",
            "حال‌گرایی: انتخاب اینکه چه چیزی از گذشته مهم است، اغلب از دغدغه‌های امروز تغذیه می‌شود و می‌تواند تاریخ را تحریف کند.",
            "کم‌توجهی به کاربر: تجربه و مصرف مخاطب در برابر مادیت دستگاه کم‌برجسته می‌شود.",
        ],
        "applications": [
            "نقد روایت‌های نوآوری و «رسانه جدید».",
            "پژوهش آرشیوی درباره رسانه‌های فراموش‌شده.",
            "الهام طراحی از مسیرهای رهاشده فناوری.",
            "آموزش تاریخ رسانه با رویکرد انتقادی.",
        ],
        "evolution": "ریشه‌ها در تاریخ فناوری و نظریه رسانه (کیتلر، زیلینسکی) است. هوتامو و پاریکا (۲۰۱۱) آن را به‌عنوان حوزه‌ای مستقل معرفی کردند و پاریکا (۲۰۱۲) صورت روش‌شناختی داد. در دهه اخیر به مطالعات پلتفرم، حافظه دیجیتال و باستان‌شناسی نرم‌افزار گسترش یافته است.",
        "key_concepts": [
            "باستان‌شناسی رسانه (media archaeology)",
            "توپوی رسانه‌ای (media topos)",
            "زمان عمیق رسانه (deep time of media)",
            "ماده‌گرایی رسانه‌ای (media materialism)",
            "تاریخ جایگزین (counter-history)",
            "بازگشت ایده (recurrence)",
        ],
        "studies": [
            "Huhtamo, E., & Parikka, J. (Eds.). (2011). Media archaeology: Approaches, applications, and implications. University of California Press.",
            "Parikka, J. (2012). What is media archaeology? Polity Press.",
        ],
        "theorists": "ارکی هوتامو و یوسی پاریکا (Erkki Huhtamo & Jussi Parikka)",
        "model": "چرخه باستان‌شناختی: آرشیو ← حفاری و توصیف مادیت ← شناسایی توپو و تداوم ← نقد روایت خطی ← بازگشایی امکان‌های جایگزین.",
        "detailed_analysis": "\n\n".join([
            "۱. بنیان و منطق نظری\nباستان‌شناسی رسانه از نارضایتی نسبت به روایت‌های تکامل‌گرا برخاست. هوتامو بر «توپوی» رسانه‌ای تأکید کرد: ایده‌هایی که در تاریخ تکرار می‌شوند و صرفاً با فناوری تازه لباس عوض می‌کنند. پاریکا بر مادیت و زمان عمیق تأکید کرد. نتیجه، حوزه‌ای چندصدایی است که وحدت نظری ندارد، اما روش‌های مشترکی دارد.",
            "۲. سازوکار عملی و تشخیصی\nبرای یک مطالعه باستان‌شناختی، سه پرسش مطرح می‌شود: چه چیزی از تاریخ حذف شده است؟ چه تداوم‌هایی در ایده‌ها دیده می‌شود؟ و مادیت دستگاه چه نقشی در معنای آن دارد؟ این پرسش‌ها پژوهش را از تاریخ پیروزمندان جدا می‌کند.",
            "۳. دلالت‌ها برای پژوهش رسانه\nپژوهش معاصر این رویکرد را برای نقد «پلتفرم‌های بی‌سابقه»، تحلیل باستان‌شناسی نرم‌افزار و مطالعه حافظه دیجیتال به کار می‌برد. پرسش باز: آیا می‌توان باستان‌شناسی رسانه را با اقتصاد سیاسی ترکیب کرد تا هم مادیت و هم قدرت را در تحلیل آورد؟",
        ]),
        "critique_text": "\n".join([
            "۱. کنجکاوی بی‌جهت: تمرکز بر اشیای عجیب و فراموش‌شده می‌تواند به مجموعه‌داری و توصیف بی‌سنتز فروبکاهد.",
            "۲. ناهمگونی نظری: ترکیب فوکو، کیتلر و تاریخ هنر، چارچوب واحدی نمی‌سازد و مرز روشن تحلیل را دشوار می‌کند.",
            "۳. ضعف اقتصاد سیاسی: قدرت شرکت‌ها، سرمایه و سیاست در بسیاری از روایت‌ها غایب است.",
            "۴. حال‌گرایی: انتخاب اینکه چه چیزی از گذشته مهم است، اغلب از دغدغه‌های امروز تغذیه می‌شود و می‌تواند تاریخ را تحریف کند.",
            "۵. کم‌توجهی به کاربر: تجربه و مصرف مخاطب در برابر مادیت دستگاه کم‌برجسته می‌شود.",
        ]),
        "example_text": "«واقعیت مجازی» پیش از هدست‌های امروزی در دستگاه‌های استریوسکوپی قرن نوزدهم و شبیه‌سازهای نظامی وجود داشت. باستان‌شناسی رسانه نشان می‌دهد که وعده «حضور در جای دیگر» تازه نیست؛ آنچه تغییر کرده، مادیت و مقیاس است. همین بازخوانی، ادعای «انقلاب بی‌سابقه» را نسبی می‌کند و پرسش از تداوم قدرت و تجربه را پیش می‌کشد.",
    },
    "MC-422": {
        "summary": "(گرانووتر، ۱۹۷۳) نظریه قدرت پیوندهای ضعیف نشان می‌دهد که پیوندهای قوی (خانواده و دوستان نزدیک) در خوشه‌های بسته متمرکزند و اطلاعات تکراری منتقل می‌کنند، در حالی که پیوندهای ضعیف (آشنایان دور) پل‌هایی به بخش‌های دیگر جامعه می‌سازند. بنابراین اطلاعات تازه، فرصت شغلی و نوآوری بیشتر از پیوندهای ضعیف می‌آید. گرانووتر این را با مفهوم «سه‌گانه ممنوعه» صورت‌بندی کرد.",
        "definition": "قدرت پیوند، تابعی از زمان، شدت عاطفی، صمیمیت و خدمات متقابل است. پیوند قوی، دو نفر را در یک خوشه نزدیک نگه می‌دارد؛ پیوند ضعیف، آن‌ها را به خوشه‌های دیگر وصل می‌کند. ارزش اطلاعاتی پیوند ضعیف در «پل‌بودن» آن است، نه در نزدیکی احساسی.",
        "main_problem": "مسئله این است که چگونه اطلاعات تازه در جامعه منتشر می‌شود، در حالی که گروه‌های نزدیک اطلاعات یکسانی دارند. پاسخ گرانووتر: پل‌های ضعیف، مسیرهای انتشار و نوآوری‌اند.",
        "mechanism": "\n".join([
            "۱. سنجش قدرت پیوند: زمان، شدت عاطفی، صمیمیت و خدمات متقابل، پیوند را قوی یا ضعیف می‌کند.",
            "۲. خوشه‌بندی پیوندهای قوی: دوستان نزدیک، اغلب با یکدیگر نیز آشنا هستند؛ بنابراین اطلاعات در خوشه می‌چرخد و تکراری می‌شود.",
            "۳. پل‌بودن پیوند ضعیف: آشنای دور، تنها مسیر اتصال دو خوشه است و اطلاعات تازه را وارد می‌کند.",
            "۴. سه‌گانه ممنوعه: اگر A با B و A با C پیوند قوی داشته باشد، B و C دست‌کم پیوند ضعیف خواهند داشت؛ نبود این پیوند نشانه ساختار غیرمعمول است.",
            "۵. پیامد فردی: یافتن شغل، ایده و فرصت بیشتر از آشنایان دور حاصل می‌شود تا از دوستان نزدیک.",
            "۶. پیامد کلان: انسجام جامعه به پیوندهای ضعیف میان خوشه‌ها وابسته است؛ حذف آن‌ها، جامعه را به جزایر منزوی تقسیم می‌کند.",
            "در بستر رسانه، شبکه‌های اجتماعی پیوندهای ضعیف را در مقیاس بی‌سابقه‌ای ممکن کرده‌اند: دنبال‌کردن افراد ناشناس، گروه‌های تخصصی و شبکه‌های حرفه‌ای. این پیوندها دسترسی به اطلاعات و فرصت را گسترش می‌دهند، اما معمولاً کم‌عمق و شکننده‌اند. پرسش معاصر این است که آیا پیوند ضعیف دیجیتال همان کارکرد پل را دارد یا به اتصالی نمایشی بدل شده که اعتماد و تعهد کمی دارد؛ شواهد نشان می‌دهد که ترکیب پیوندهای ضعیف گسترده با چند پیوند قوی، بیشترین اثر را دارد.",
        ]),
        "assumptions": [
            "قدرت پیوند از ترکیب زمان، عاطفه، صمیمیت و مبادله تعیین می‌شود.",
            "پیوندهای قوی در خوشه‌های متراکم و با اطلاعات تکراری قرار دارند.",
            "پیوندهای ضعیف، مسیرهای اصلی انتقال اطلاعات تازه‌اند.",
        ],
        "principles": [
            "برای تنوع اطلاعات، به پل‌های ضعیف توجه کنید.",
            "تراکم خوشه، لزوماً به اطلاعات تازه نمی‌انجامد.",
            "ساختار شبکه را جدا از محتوای رابطه تحلیل نکنید.",
        ],
        "critiques": [
            "جبر ساختاری: نظریه پیوند را تعیین‌کننده می‌بیند و محتوا، اعتماد و تاریخ رابطه را کم‌برجسته می‌کند.",
            "سنجش قدرت پیوند: شاخص‌های چهارگانه در عمل به‌سختی اندازه‌گیری می‌شوند و اغلب به فراوانی تماس تقلیل می‌یابند.",
            "ناکافی‌بودن اعتماد: پیوند ضعیف بدون حداقلی از اعتماد، اطلاعات را منتقل نمی‌کند.",
            "بافت‌وابستگی: مطالعات اولیه بر بازار کار آمریکا متمرکز بود و تعمیم آن به جوامع دیگر نیازمند احتیاط است.",
            "پیوند ضعیف دیجیتال: دنبال‌کردن در شبکه اجتماعی با آشنای دور واقعی یکی نیست و کارکرد پل را تضعیف می‌کند.",
        ],
        "applications": [
            "تحلیل شبکه‌های شغلی و فرصت‌های شغلی.",
            "پژوهش درباره انتشار نوآوری و اطلاعات.",
            "طراحی شبکه‌های حرفه‌ای و اجتماعات تخصصی.",
            "مطالعه انسجام اجتماعی و شکاف گروه‌ها.",
        ],
        "evolution": "گرانووتر در ۱۹۷۳ نظریه را با داده‌های بازار کار بوستون ارائه کرد و در ۱۹۸۲ بازبینی کرد. در دهه ۲۰۰۰ با داده‌های شبکه‌های آنلاین آزمون شد و در بحث‌های قطبی‌شدن و انتشار اطلاعات نادرست بازخوانی شد.",
        "key_concepts": [
            "قدرت پیوند (tie strength)",
            "پیوند ضعیف (weak tie)",
            "پل (bridge)",
            "سه‌گانه ممنوعه (forbidden triad)",
            "خوشه (cluster)",
            "انتشار (diffusion)",
        ],
        "studies": [
            "Granovetter, M. S. (1973). The strength of weak ties. American Journal of Sociology, 78(6), 1360-1380.",
            "Granovetter, M. S. (1982). The strength of weak ties: A network theory revisited. Sociological Theory, 1, 201-233.",
        ],
        "theorists": "مارک اس. گرانووتر (Mark S. Granovetter)",
        "model": "منطق پیوند: قدرت پیوند بالا ← تراکم خوشه و اطلاعات تکراری؛ پیوند ضعیف پل‌ساز ← دسترسی به اطلاعات و فرصت تازه؛ سه‌گانه ممنوعه به‌عنوان آزمون ساختار.",
        "detailed_analysis": "\n\n".join([
            "۱. بنیان و منطق نظری\nگرانووتر با نقد تصویر جامعه به‌عنوان شبکه‌ای از روابط نزدیک، نشان داد که پیوندهای ضعیف نقش ساختاری کلیدی دارند. او قدرت پیوند را با چهار شاخص تعریف کرد و سپس استدلال کرد که تراکم پیوندهای قوی، اطلاعات را تکراری می‌کند. ارزش نظریه در پیوند دادن سطح خرد رابطه با سطح کلان انتشار است.",
            "۲. سازوکار عملی و تشخیصی\nبرای تحلیل یک شبکه، سه پرسش مطرح می‌شود: پیوندهای پل‌ساز کدام‌اند؟ چه کسانی به خوشه‌های دیگر دسترسی دارند؟ و آیا تنوع اطلاعات با ساختار رابطه هم‌خوان است؟ این پرسش‌ها نظریه را از استعاره به ابزار تحلیل شبکه تبدیل می‌کند.",
            "۳. دلالت‌ها برای پژوهش رسانه\nپژوهش معاصر پیوندهای ضعیف را در شبکه‌های حرفه‌ای، انتشار اطلاعات نادرست و انسجام اجتماعی می‌سنجد. پرسش باز: آیا پلتفرم‌ها با پیشنهاد محتوا و افراد، پیوندهای ضعیف واقعی می‌سازند یا صرفاً اتصال‌های نمایشی که پل‌بودن ندارند؟",
        ]),
        "critique_text": "\n".join([
            "۱. جبر ساختاری: نظریه پیوند را تعیین‌کننده می‌بیند و محتوا، اعتماد و تاریخ رابطه را کم‌برجسته می‌کند.",
            "۲. سنجش قدرت پیوند: شاخص‌های چهارگانه در عمل به‌سختی اندازه‌گیری می‌شوند و اغلب به فراوانی تماس تقلیل می‌یابند.",
            "۳. ناکافی‌بودن اعتماد: پیوند ضعیف بدون حداقلی از اعتماد، اطلاعات را منتقل نمی‌کند.",
            "۴. بافت‌وابستگی: مطالعات اولیه بر بازار کار آمریکا متمرکز بود و تعمیم آن به جوامع دیگر نیازمند احتیاط است.",
            "۵. پیوند ضعیف دیجیتال: دنبال‌کردن در شبکه اجتماعی با آشنای دور واقعی یکی نیست و کارکرد پل را تضعیف می‌کند.",
        ]),
        "example_text": "کسی که تنها از طریق یک همکار قدیمی با یک صنعت دیگر آشناست، بیشتر احتمال دارد فرصت شغلی تازه بشنود تا از دوستان نزدیکش که همه در همان صنعت کار می‌کنند. همین همکار قدیمی، یک پیوند ضعیف پل‌ساز است. اگر او ارتباطش را قطع کند، کل خوشه دسترسی خود به آن صنعت را از دست می‌دهد؛ اهمیت ساختاری پیوند ضعیف در همین است.",
    },
    "MC-424": {
        "summary": "(واتس و استروگاتز، ۱۹۹۸) نظریه جهان کوچک نشان داد که بسیاری از شبکه‌های واقعی نه کاملاً منظم و نه کاملاً تصادفی‌اند، بلکه ترکیبی از خوشه‌بندی بالا و طول مسیر کوتاه دارند. آن‌ها با مدل بازسیم‌کشی نشان دادند که با افزودن تعداد کمی پیوند تصادفی، فاصله میان گره‌ها به‌شدت کاهش می‌یابد. این مدل توضیحی ریاضی برای پدیده «شش درجه جدایی» فراهم کرد.",
        "definition": "شبکه جهان کوچک، شبکه‌ای است که در آن گره‌ها به‌طور محلی خوشه‌بندی شده‌اند، اما مسیر میان هر دو گره به‌طور میانگین کوتاه است. این ترکیب، هم جدایی محلی (خوشه) و هم اتصال جهانی (فاصله کوتاه) را ممکن می‌کند.",
        "main_problem": "مسئله این است که شبکه‌های واقعی از یک سو محلی و خوشه‌ای‌اند و از سوی دیگر به‌طور شگفت‌آوری «کوچک»؛ چگونه این دو ویژگی هم‌زمان ممکن است؟ مدل واتس-استروگاتز پاسخ ریاضی این پرسش است.",
        "mechanism": "\n".join([
            "۱. مدل پایه: شبکه‌ای حلقه‌ای که هر گره به همسایگان نزدیک وصل است؛ خوشه‌بندی بالا اما فاصله طولانی.",
            "۲. بازسیم‌کشی: با احتمال p، برخی پیوندها به گره تصادفی وصل می‌شوند؛ p کوچک، تغییر بزرگ می‌سازد.",
            "۳. خوشه‌بندی بالا: حتی با p کوچک، ساختار محلی تا حد زیادی حفظ می‌شود.",
            "۴. طول مسیر کوتاه: همان چند پیوند تصادفی، فاصله میان گره‌های دور را به‌شدت کاهش می‌دهند.",
            "۵. شش درجه جدایی: مدل، شهود میلگرام را به سازوکار ساختاری بدل می‌کند: مسیرهای کوتاه از ترکیب خوشه و پل حاصل می‌شوند.",
            "۶. پیامد دینامیکی: جهان کوچک، انتشار اطلاعات، شایعه و بیماری را شتاب می‌دهد و همگام‌سازی را ممکن می‌کند.",
            "در بستر رسانه، مدل جهان کوچک توضیح می‌دهد چرا یک ویدیو یا شایعه می‌تواند در چند گام به بخش‌های دور شبکه برسد: خوشه‌های محلی آن را در گروه‌های نزدیک پخش می‌کنند و پیوندهای پل‌ساز آن را به خوشه‌های دیگر می‌برند. الگوریتم‌های پیشنهاد محتوا با تقویت همین پل‌ها، سرعت انتشار را افزایش می‌دهند. اما «کوچک‌بودن» شبکه، هم فرصت است (دسترسی به اطلاعات) و هم خطر (انتشار سریع اطلاعات نادرست)؛ بنابراین طراحی پلتفرم باید پیامدهای دینامیکی ساختار را در نظر بگیرد.",
        ]),
        "assumptions": [
            "شبکه‌های واقعی میان نظم و تصادف قرار دارند.",
            "تعداد کمی پیوند تصادفی برای کوتاه‌کردن فاصله کافی است.",
            "خوشه‌بندی محلی با دسترسی جهانی سازگار است.",
        ],
        "principles": [
            "ساختار شبکه را با خوشه‌بندی و طول مسیر هم‌زمان بسنجید.",
            "اثر پیوندهای پل را کوچک فرض نکنید.",
            "مدل را با داده واقعی و نه با شهود ساده بسنجید.",
        ],
        "critiques": [
            "سادگی مدل: شبکه‌های واقعی وزن‌دار، جهت‌دار و پویا هستند و مدل پایه این ویژگی‌ها را ندارد.",
            "بی‌تفاوتی به محتوا: مدل فقط توپولوژی را می‌بیند و معنای رابطه را نادیده می‌گیرد.",
            "ابهام «شش درجه»: عدد شش، نتیجه شرایط تجربی خاص است و تعمیم آن به همه شبکه‌ها نادرست است.",
            "نادیده‌گرفتن قدرت: ساختار شبکه به خودی خود توضیح نمی‌دهد چه کسی کنترل جریان را دارد.",
            "پیش‌بینی محدود: مدل توضیح می‌دهد چگونه انتشار ممکن است، نه اینکه چه چیزی منتشر می‌شود.",
        ],
        "applications": [
            "تحلیل انتشار اطلاعات و شایعه.",
            "مطالعه شبکه‌های همکاری علمی.",
            "مدل‌سازی انتشار بیماری و رفتار.",
            "طراحی شبکه‌های ارتباطی و زیرساخت.",
        ],
        "evolution": "میلگرام (۱۹۶۷) مسئله را تجربی طرح کرد؛ واتس و استروگاتز (۱۹۹۸) مدل ریاضی ارائه کردند. پس از آن، پژوهش شبکه‌های بدون مقیاس و مدل‌های پویا آن را گسترش داد و در مطالعات رسانه، همه‌گیری و انتشار اطلاعات به کار رفت.",
        "key_concepts": [
            "شبکه جهان کوچک (small-world network)",
            "ضریب خوشه‌بندی (clustering coefficient)",
            "طول مسیر میانگین (average path length)",
            "بازسیم‌کشی (rewiring)",
            "شش درجه جدایی (six degrees of separation)",
            "انتشار (diffusion)",
        ],
        "studies": [
            "Watts, D. J., & Strogatz, S. H. (1998). Collective dynamics of 'small-world' networks. Nature, 393(6684), 440-442.",
            "Milgram, S. (1967). The small world problem. Psychology Today, 2(1), 60-67.",
        ],
        "theorists": "دانکن واتس و استیون استروگاتز (Duncan J. Watts & Steven H. Strogatz)",
        "model": "مدل واتس-استروگاتز: شبکه منظم ← بازسیم‌کشی با احتمال p ← خوشه‌بندی بالا + طول مسیر کوتاه ← انتشار سریع و همگام‌سازی.",
        "detailed_analysis": "\n\n".join([
            "۱. بنیان و منطق نظری\nواتس و استروگاتز با پرسش از ساختار شبکه‌های زیستی و اجتماعی، مدلی ساختند که میان نظم کامل و تصادف کامل قرار می‌گیرد. نوآوری آن‌ها نشان‌دادن این نکته بود که تعداد کمی پیوند تصادفی، بدون فروپاشی خوشه‌بندی محلی، فاصله جهانی را کوتاه می‌کند. همین ترکیب، «جهان کوچک» را از استعاره به ویژگی ساختاری بدل کرد.",
            "۲. سازوکار عملی و تشخیصی\nبرای آزمون جهان‌کوچکی یک شبکه، دو شاخص سنجیده می‌شود: ضریب خوشه‌بندی و طول مسیر میانگین. اگر خوشه‌بندی بالا و مسیر کوتاه باشد، شبکه جهان کوچک است. این آزمون ساده، مدل را از توصیف کیفی جدا می‌کند.",
            "۳. دلالت‌ها برای پژوهش رسانه\nپژوهش معاصر جهان کوچک را در انتشار محتوا، هماهنگی کمپین‌ها و ساختار شبکه‌های اجتماعی می‌سنجد. پرسش باز: آیا الگوریتم‌های پیشنهاد، شبکه را «کوچک‌تر» می‌کنند یا با تقویت خوشه‌های همسان، آن را به جزایر قطبی تقسیم می‌کنند؟",
        ]),
        "critique_text": "\n".join([
            "۱. سادگی مدل: شبکه‌های واقعی وزن‌دار، جهت‌دار و پویا هستند و مدل پایه این ویژگی‌ها را ندارد.",
            "۲. بی‌تفاوتی به محتوا: مدل فقط توپولوژی را می‌بیند و معنای رابطه را نادیده می‌گیرد.",
            "۳. ابهام «شش درجه»: عدد شش، نتیجه شرایط تجربی خاص است و تعمیم آن به همه شبکه‌ها نادرست است.",
            "۴. نادیده‌گرفتن قدرت: ساختار شبکه به خودی خود توضیح نمی‌دهد چه کسی کنترل جریان را دارد.",
            "۵. پیش‌بینی محدود: مدل توضیح می‌دهد چگونه انتشار ممکن است، نه اینکه چه چیزی منتشر می‌شود.",
        ]),
        "example_text": "خبری که در یک گروه خانوادگی منتشر می‌شود، ابتدا در خوشه نزدیک می‌چرخد؛ اما اگر یکی از اعضا آن را به همکارانش در شهری دیگر بفرستد، همان یک پیوند پل، خبر را به خوشه‌ای دور منتقل می‌کند. با تکرار چند پل، خبر در چند گام به شبکه‌ای بسیار بزرگ می‌رسد. این مثال، تفاوت «شبکه کوچک» با «شبکه‌ای که همه اعضایش با هم آشنا هستند» را نشان می‌دهد.",
    },
    "MC-425": {
        "summary": "(برت، ۱۹۹۲) نظریه سوراخ‌های ساختاری می‌گوید مزیت رقابتی نه فقط از منابع، بلکه از موقعیت در شبکه اجتماعی می‌آید. کنشگری که شکاف میان خوشه‌های جدا را پر می‌کند، به اطلاعات متنوع و زودهنگام دسترسی می‌یابد و می‌تواند میان گروه‌ها واسطه شود. برت این مزیت را در دو شکل اطلاعاتی و کنترلی صورت‌بندی کرد و با مفهوم «محدودیت» سنجید.",
        "definition": "سوراخ ساختاری، نبود پیوند میان دو خوشه در شبکه است. کنشگری که این شکاف را با پیوندهای خود پر می‌کند، «واسطه» می‌شود و به سرمایه اجتماعی دسترسی پیدا می‌کند: اطلاعات غیرتکراری و توان کنترل جریان میان گروه‌ها.",
        "main_problem": "مسئله این است که چرا برخی کنشگرها در ساختارهای مشابه، عملکرد بهتری دارند. برت پاسخ می‌دهد که موقعیت واسطگی، دسترسی اطلاعاتی و قدرت چانه‌زنی می‌سازد و همین، رقابت را نامتقارن می‌کند.",
        "mechanism": "\n".join([
            "۱. سوراخ ساختاری: دو خوشه که پیوندی میانشان نیست؛ شکاف، فرصت واسطگی است.",
            "۲. واسطه‌گری: کنشگر با پیوند به هر دو خوشه، مسیر عبور اطلاعات و منابع می‌شود.",
            "۳. مزیت اطلاعاتی: دسترسی زودهنگام به اطلاعات متنوع و غیرتکراری که درون هر خوشه نمی‌چرخد.",
            "۴. مزیت کنترلی: واسطه می‌تواند جریان اطلاعات را تنظیم کند و در مذاکره موقعیت برتر داشته باشد (tertius gaudens).",
            "۵. محدودیت شبکه: هرچه پیوندهای یک کنشگر به یک خوشه محدودتر باشد، تنوع اطلاعات کمتر و محدودیت بیشتر است.",
            "۶. سرمایه اجتماعی و عملکرد: واسطگی با نوآوری، ارتقای شغلی و کیفیت ایده مرتبط است؛ بستار شبکه نیز می‌تواند اعتماد بسازد.",
            "در بستر رسانه، منطق سوراخ‌های ساختاری در صنایع خلاق و رسانه‌ای دیده می‌شود: تهیه‌کننده‌ای که هم با دنیای فناوری و هم با دنیای محتوا ارتباط دارد، ایده‌های تازه را زودتر می‌بیند و می‌تواند میان آن‌ها واسطه شود. پلتفرم‌ها نیز خود واسطه‌های ساختاری‌اند: میان تولیدکننده و مخاطب، میان تبلیغ‌دهنده و کاربر. اما واسطگی همیشه سودمند نیست؛ اگر واسطه اطلاعات را پنهان کند یا اعتماد را به انحصار بدل کند، شبکه به بی‌اعتمادی می‌رسد. برت خود بعدها نشان داد که ایده‌های «خوب» بیشتر از واسطه‌ها می‌آیند، اما ایده‌های «مقبول‌شده» به بستار و اعتماد نیاز دارند.",
        ]),
        "assumptions": [
            "مزیت رقابتی به موقعیت ساختاری در شبکه وابسته است.",
            "شکاف میان خوشه‌ها، فرصت اطلاعاتی و کنترلی می‌سازد.",
            "تنوع پیوندها با تنوع اطلاعات رابطه دارد.",
        ],
        "principles": [
            "برای تنوع اطلاعات، به شکاف‌های شبکه نگاه کنید.",
            "واسطگی را با محدودیت شبکه و اعتماد متوازن کنید.",
            "سرمایه اجتماعی را موقعیتی و رابطه‌ای هم‌زمان ببینید.",
        ],
        "critiques": [
            "جبر ساختاری: نظریه موقعیت را تعیین‌کننده می‌بیند و محتوا، مهارت و اعتماد را کم‌برجسته می‌کند.",
            "همبستگی به‌جای علیت: رابطه واسطگی و ارتقا می‌تواند ناشی از عوامل پنهان مانند مهارت یا منابع باشد.",
            "هزینه واسطگی: واسطه‌گری می‌تواند به بی‌اعتمادی، دستکاری و احساس بهره‌کشی بینجامد.",
            "سنجش محدودیت: شاخص‌های برت به داده کامل شبکه وابسته‌اند و در عمل با خطای اندازه‌گیری روبه‌رو می‌شوند.",
            "بافت سازمانی: شواهد عمدتاً از شرکت‌های غربی است و تعمیم آن به بسترهای دیگر نیازمند احتیاط است.",
        ],
        "applications": [
            "تحلیل شبکه‌های سازمانی و نوآوری.",
            "پژوهش درباره واسطگی در صنایع رسانه‌ای.",
            "طراحی تیم‌های میان‌رشته‌ای.",
            "مطالعه سرمایه اجتماعی و بازار کار.",
        ],
        "evolution": "برت نظریه را در ۱۹۹۲ با داده‌های سازمانی ارائه کرد و در ۲۰۰۴ با «سوراخ‌های ساختاری و ایده‌های خوب» بسط داد. پژوهش‌های بعدی آن را با بستار شبکه، اعتماد و شبکه‌های دیجیتال ترکیب کردند.",
        "key_concepts": [
            "سوراخ ساختاری (structural hole)",
            "واسطه‌گری (brokerage)",
            "مزیت اطلاعاتی (information benefit)",
            "مزیت کنترلی (control benefit)",
            "محدودیت (constraint)",
            "سرمایه اجتماعی (social capital)",
        ],
        "studies": [
            "Burt, R. S. (1992). Structural holes: The social structure of competition. Harvard University Press.",
            "Burt, R. S. (2004). Structural holes and good ideas. American Journal of Sociology, 110(2), 349-399.",
        ],
        "theorists": "رونالد اس. برت (Ronald S. Burt)",
        "model": "منطق واسطگی: شکاف میان خوشه‌ها ← پیوند واسطه ← اطلاعات متنوع و کنترل جریان ← مزیت رقابتی؛ با توازن میان واسطگی و بستار/اعتماد.",
        "detailed_analysis": "\n\n".join([
            "۱. بنیان و منطق نظری\nبرت رقابت را نه فقط مبارزه بر سر منابع، بلکه مبارزه بر سر موقعیت در ساختار اجتماعی دید. او نشان داد که شبکه‌های متراکم، اطلاعات را تکراری می‌کنند و شکاف‌ها، فرصت واسطگی می‌سازند. نظریه، پیوندی میان جامعه‌شناسی شبکه و اقتصاد سازمانی است.",
            "۲. سازوکار عملی و تشخیصی\nبرای ارزیابی یک موقعیت، سه پرسش مطرح می‌شود: کنشگر به چند خوشه جدا وصل است؟ پیوندهایش چقدر تکراری‌اند؟ و آیا می‌تواند جریان اطلاعات را کنترل کند؟ شاخص محدودیت برت، پاسخ کمی به این پرسش‌ها می‌دهد.",
            "۳. دلالت‌ها برای پژوهش رسانه\nپژوهش معاصر واسطگی را در صنایع خلاق، روزنامه‌نگاری و پلتفرم‌ها می‌سنجد. پرسش باز: آیا پلتفرم‌ها با تبدیل‌شدن به واسطه انحصاری، مزیت واسطگی را از کنشگران اجتماعی می‌گیرند و خود جای آن‌ها را می‌گیرند؟",
        ]),
        "critique_text": "\n".join([
            "۱. جبر ساختاری: نظریه موقعیت را تعیین‌کننده می‌بیند و محتوا، مهارت و اعتماد را کم‌برجسته می‌کند.",
            "۲. همبستگی به‌جای علیت: رابطه واسطگی و ارتقا می‌تواند ناشی از عوامل پنهان مانند مهارت یا منابع باشد.",
            "۳. هزینه واسطگی: واسطه‌گری می‌تواند به بی‌اعتمادی، دستکاری و احساس بهره‌کشی بینجامد.",
            "۴. سنجش محدودیت: شاخص‌های برت به داده کامل شبکه وابسته‌اند و در عمل با خطای اندازه‌گیری روبه‌رو می‌شوند.",
            "۵. بافت سازمانی: شواهد عمدتاً از شرکت‌های غربی است و تعمیم آن به بسترهای دیگر نیازمند احتیاط است.",
        ]),
        "example_text": "مشاور رسانه‌ای که هم با استارتاپ‌های فناوری و هم با تحریریه‌های سنتی ارتباط دارد، ایده‌های تازه را زودتر می‌شنود و می‌تواند میان دو دنیا پروژه بسازد. اگر تنها با یک طرف کار کند، اطلاعاتش تکراری می‌شود. اما اگر واسطگی را به پنهان‌کاری بدل کند، اعتماد هر دو طرف را از دست می‌دهد؛ مزیت ساختاری بدون اعتماد پایدار نمی‌ماند.",
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
                                       "verified": n_verified, "batch": 80}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH80 THEORY DONE")


if __name__ == "__main__":
    main()
