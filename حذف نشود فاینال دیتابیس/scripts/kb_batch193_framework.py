# -*- coding: utf-8 -*-
"""Batch 193: DSC-015..DSC-019 (DISCIPLINE)."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch193-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch193.json"

D015 = {"entity_type": "DISCIPLINE", "content_type": "حوزه مطالعاتی (Discipline)",
        "needs_review": False, "taxonomy_section": "3"}
D016 = dict(D015)
D017 = dict(D015)
D018 = dict(D015)
D019 = dict(D015)

S = {
    "DSC-015": [
        dict(kind="BOOK",
             title_en="Strategic Management in the Media: Theory to Practice",
             title_fa="مدیریت راهبردی در رسانه: از نظریه تا عمل",
             authors="Lucy Küng", year=2008,
             publisher="Sage Publications",
             doi=None,
             url="https://books.google.com/books/about/Strategic_Management_in_the_Media.html?id=PnsIAxZDGlEC",
             language="en", isbn=None,
             citation="Küng, L. (2008). Strategic Management in the Media: Theory to Practice. London: Sage Publications.",
             locator="chapters on strategy, structure and leadership in media firms",
             locator_type="CHAPTER",
             supports="the application of strategic management theory to media organizations, including digital transition",
             verified=True),
        dict(kind="BOOK",
             title_en="The Economics and Financing of Media Companies",
             title_fa="اقتصاد و تأمین مالی بنگاه‌های رسانه‌ای",
             authors="Robert G. Picard", year=2002,
             publisher="Fordham University Press",
             doi=None,
             url="https://www.robertpicard.net/PDFFiles/MCDProjectResults.pdf",
             language="en", isbn=None,
             citation="Picard, R. G. (2002). The Economics and Financing of Media Companies. New York: Fordham University Press.",
             locator="chapters on media markets, dual product markets and financing",
             locator_type="CHAPTER",
             supports="the dual-market economics of media firms and the resource constraints that shape media strategy",
             verified=True),
    ],
    "DSC-016": [
        dict(kind="BOOK",
             title_en="The Irony of Free Speech",
             title_fa="طنز آزادی بیان",
             authors="Owen M. Fiss", year=1996,
             publisher="Harvard University Press",
             doi=None,
             url="https://www.hup.harvard.edu/books/9780674466616",
             language="en", isbn="9780674466616",
             citation="Fiss, O. M. (1996). The Irony of Free Speech. Cambridge, MA: Harvard University Press.",
             locator="argument that state regulation may serve rather than only restrict free expression",
             locator_type="CHAPTER",
             supports="the case for regulation in service of expressive diversity, not merely against it",
             verified=True),
        dict(kind="BOOK",
             title_en="The Politics of Media Policy",
             title_fa="سیاست‌گذاری رسانه",
             authors="Des Freedman", year=2008,
             publisher="Polity Press",
             doi=None,
             url="https://diposit.ub.edu/bitstreams/2207497c-0698-467a-b33a-64785db7c254/download",
             language="en", isbn=None,
             citation="Freedman, D. (2008). The Politics of Media Policy. Cambridge: Polity Press.",
             locator="chapters on media policy, ownership and the politics of regulation",
             locator_type="CHAPTER",
             supports="media policy as a contested political process shaped by ownership and state-market relations",
             verified=True),
    ],
    "DSC-017": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Misunderstood Misunderstanding: Social Identities and Public Uptake of Science",
             title_fa="سوءتفاهمِ سوءتفاهم‌شده: هویت‌های اجتماعی و دریافت عمومی علم",
             authors="Brian Wynne", year=1992,
             publisher="Public Understanding of Science",
             doi="10.1088/0963-6625/1/3/004",
             url="https://journals.sagepub.com/doi/10.1088/0963-6625/1/3/004",
             language="en", isbn=None,
             citation="Wynne, B. (1992). Misunderstood misunderstanding: Social identities and public uptake of science. Public Understanding of Science, 1(3), 281-304.",
             locator="pp. 281-304", locator_type="PAGE",
             supports="the critique of the deficit model: lay responses are cultural interpretations, not mere ignorance",
             verified=True),
        dict(kind="BOOK",
             title_en="Routledge Handbook of Public Communication of Science and Technology",
             title_fa="راهنمای راتلج ارتباطات عمومی علم و فناوری",
             authors="Massimiano Bucchi; Brian Trench (Eds.)", year=2021,
             publisher="Routledge",
             doi="10.4324/9781003039242",
             url="https://www.taylorfrancis.com/books/edit/10.4324/9781003039242/routledge-handbook-public-communication-science-technology-massimiano-bucchi-brian-trench",
             language="en", isbn=None,
             citation="Bucchi, M., & Trench, B. (Eds.). (2021). Routledge Handbook of Public Communication of Science and Technology (3rd ed.). London: Routledge.",
             locator="chapters on models of science communication, public engagement and trust",
             locator_type="CHAPTER",
             supports="the shift from deficit models to dialogue, participation and trust-based models of science communication",
             verified=True),
    ],
    "DSC-018": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Understanding the Relationship between Religion Online and Offline in a Networked Society",
             title_fa="فهم رابطهٔ دین آنلاین و آفلاین در جامعهٔ شبکه‌ای",
             authors="Heidi A. Campbell", year=2012,
             publisher="Journal of the American Academy of Religion",
             doi="10.1093/jaarel/lfr074",
             url="https://academic.oup.com/jaar/article-abstract/80/1/64/1007151",
             language="en", isbn=None,
             citation="Campbell, H. A. (2012). Understanding the relationship between religion online and offline in a networked society. Journal of the American Academy of Religion, 80(1), 64-93.",
             locator="pp. 64-93", locator_type="PAGE",
             supports="digital religion as a networked practice in which community, authority, identity and ritual cross online and offline spaces",
             verified=True),
        dict(kind="BOOK",
             title_en="Religion in the Media Age",
             title_fa="دین در عصر رسانه",
             authors="Stewart M. Hoover", year=2006,
             publisher="Routledge",
             doi=None,
             url="https://journals.sagepub.com/doi/abs/10.1177/01634437070290060903",
             language="en", isbn=None,
             citation="Hoover, S. M. (2006). Religion in the Media Age. London: Routledge.",
             locator="chapters on media, religion and the mediation of belief in everyday life",
             locator_type="CHAPTER",
             supports="the everyday mediation of religion through media and the mutual shaping of religious and media practice",
             verified=True),
    ],
    "DSC-019": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Theory of Planned Behavior",
             title_fa="نظریهٔ رفتار برنامه‌ریزی‌شده",
             authors="Icek Ajzen", year=1991,
             publisher="Organizational Behavior and Human Decision Processes",
             doi="10.1016/0749-5978(91)90020-T",
             url="https://www.sciencedirect.com/science/article/pii/074959789190020T",
             language="en", isbn=None,
             citation="Ajzen, I. (1991). The theory of planned behavior. Organizational Behavior and Human Decision Processes, 50(2), 179-211.",
             locator="pp. 179-211", locator_type="PAGE",
             supports="behavior as a function of intention, which is shaped by attitudes, subjective norms and perceived behavioral control",
             verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Perception of Risk",
             title_fa="ادراک ریسک",
             authors="Paul Slovic", year=1987,
             publisher="Science",
             doi="10.1126/science.3563507",
             url="https://www.science.org/doi/10.1126/science.3563507",
             language="en", isbn=None,
             citation="Slovic, P. (1987). Perception of risk. Science, 236(4799), 280-285.",
             locator="pp. 280-285", locator_type="PAGE",
             supports="lay risk judgments are driven by dread and unknownness rather than by technical probability alone",
             verified=True),
    ],
}

ENRICH = {
    "DSC-015": dict(
        mapping=D015,
        definition="مطالعات مدیریت رسانه حوزه‌ای کاربردی و میان‌رشته‌ای است که نظریهٔ سازمان و راهبرد را به بنگاه رسانه‌ای تعمیم می‌دهد و بر سه محور تمرکز دارد: تدوین راهبرد در بازار دووجهی محتوا و تبلیغ، طراحی ساختار و رهبری سازمان رسانه‌ای، و مدیریت منابع کمیاب مانند محتوا، مخاطب، برند و داده.",
        mechanism="چرخهٔ مدیریت با تحلیل محیط آغاز می‌شود: شناسایی رقبا، روندهای فناورانه، مقررات و رفتار مخاطب. سپس راهبرد انتخاب می‌گردد: تمایز محتوایی، رهبری هزینه، تمرکز بر بازار خاص یا تنوع سبد. در گام سوم ساختار سازمانی، فرایند تولید و نظام پاداش با راهبرد هم‌تراز می‌شوند. سرانجام عملکرد با شاخص‌هایی مانند سهم بازار، نگهداشت مخاطب، حاشیهٔ سود و بلوغ دیجیتال سنجیده و راهبرد بازنگری می‌گردد.",
        critiques="۱. رسانه کالایی دووجهی است و ابزارهای مدیریت صنایع عادی بدون تعدیل به آن منتقل نمی‌شوند. ۲. تمرکز بر کارایی می‌تواند مأموریت عمومی و کیفیت محتوا را به حاشیه براند. ۳. بلوغ دیجیتال سنجه‌ای مبهم است و به خودارزیابی خوش‌بینانه دامن می‌زند. ۴. دادهٔ عملکرد در رسانه‌های کوچک کم و مقایسه‌پذیری آن محدود است.",
        evolution="این حوزه از دههٔ ۱۹۸۰ با اقتصاد رسانه و مطالعهٔ بنگاه‌های خبری آغاز شد، در دههٔ ۲۰۰۰ به راهبرد و مدل کسب‌وکار دیجیتال گرایش یافت و امروز بر تحول دیجیتال، اشتراک، مدیریت داده و حاکمیت پلتفرم متمرکز است.",
        principles=["تحلیل محیط پیش از انتخاب راهبرد", "هم‌ترازی ساختار با راهبرد", "توجه به بازار دووجهی محتوا و تبلیغ", "سنجش عملکرد با شاخص‌های روشن", "حفظ مأموریت عمومی در کنار پایداری اقتصادی"],
        assumptions=["سازمان رسانه‌ای می‌تواند با ابزارهای راهبردی اداره شود.", "محیط رسانه به‌اندازهٔ کافی قابل تحلیل و پیش‌بینی است.", "منابع کمیاب‌اند و انتخاب میان آن‌ها ضروری است.", "رهبری و فرهنگ سازمانی بر عملکرد اثر می‌گذارد."],
        theorists=[
            {"role": "مدیریت راهبردی و مزیت رقابتی", "name_fa": "مایکل پورتر"},
            {"role": "مدیریت راهبردی رسانه", "name_fa": "لوسی کونگ"},
            {"role": "اقتصاد رسانه", "name_fa": "رابرت پیکارد"},
        ],
        theorists_text="این حوزه از مدیریت راهبردی پورتر تغذیه می‌کند و کونگ آن را به بنگاه رسانه‌ای تعمیم داد؛ پیکارد نیز چارچوب اقتصاد و تأمین مالی رسانه را فراهم کرد که پایهٔ تحلیل منابع و بازار دووجهی است.",
        studies=[
            "مدیریت راهبردی در رسانه (کونگ، ۲۰۰۸): تعمیم نظریهٔ راهبرد به سازمان رسانه‌ای و گذار دیجیتال.",
            "اقتصاد و تأمین مالی بنگاه‌های رسانه‌ای (پیکارد، ۲۰۰۲): ساختار بازار و منابع مالی رسانه.",
            "مطالعات موردی تحول دیجیتال: بازطراحی مدل کسب‌وکار سازمان‌های خبری.",
            "پژوهش‌های بلوغ دیجیتال: سنجش آمادگی سازمانی برای گذار دیجیتال.",
            "تحلیل عملکرد رسانه: پیوند شاخص‌های مخاطب و بازار با تصمیم راهبردی.",
            "پژوهش مدل اشتراک در خبر: پایداری مالی و پیوند مستقیم با مخاطب.",
        ],
    ),
    "DSC-016": dict(
        mapping=D016,
        definition="مطالعات حقوق و سیاست‌گذاری رسانه حوزه‌ای است که چارچوب قانونی، تنظیم‌گری و حکمرانی رسانه و پلتفرم را بررسی می‌کند؛ موضوع آن تعیین مرزهای آزادی بیان، مسئولیت محتوا، مالکیت فکری و حریم خصوصی و طراحی نهادهایی است که این مرزها را اجرا می‌کنند.",
        mechanism="تحلیل با شناسایی هنجار آغاز می‌شود: کدام حق و کدام مسئولیت در قانون یا رویهٔ قضایی شناسایی شده است. سپس منافع متعارض — آزادی بیان، امنیت، کرامت، رقابت و حریم خصوصی — و وزن‌دهی آن‌ها بررسی می‌گردد. در گام بعد ابزار حکمرانی انتخاب می‌شود: قاعده‌گذاری دولتی، خودتنظیم‌گری صنفی، تنظیم‌گری مستقل یا حکمرانی چندجانبه. سرانجام پیامدهای اجرا و امکان پاسخ‌گویی و بازبینی قضایی سنجیده می‌شود.",
        critiques="۱. تعادل آزادی و نظم به بافت سیاسی وابسته است و قاعدهٔ جهان‌شمول ندارد. ۲. تنظیم‌گری می‌تواند به ابزار کنترل سیاسی بدل شود. ۳. خودتنظیم‌گری پلتفرم‌ها شفافیت و پاسخ‌گویی کافی ندارد. ۴. سرعت تحول فناوری از سرعت قانون‌گذاری پیشی می‌گیرد و شکاف تنظیم‌گری می‌سازد. ۵. تحلیل تطبیقی بدون توجه به زمینهٔ نهادی گمراه‌کننده است.",
        evolution="این حوزه در نیمهٔ دوم قرن بیستم حول آزادی مطبوعات، مالکیت رسانه و مقررات پخش شکل گرفت. از دههٔ ۲۰۰۰ با اینترنت به مسائل حق نسخه‌برداری، بی‌طرفی شبکه و حریم خصوصی گسترش یافت و امروز بر مسئولیت پلتفرم، شفافیت الگوریتمی و حکمرانی داده متمرکز است.",
        principles=["تعادل آزادی بیان و آسیب", "تناسب ابزار تنظیم با هدف", "شفافیت و پاسخ‌گویی نهادهای تنظیم‌گر", "استقلال تنظیم‌گر از قدرت سیاسی", "حمایت از تنوع و کثرت منابع اطلاعاتی"],
        assumptions=["حق آزادی بیان بنیادین اما مشروط به آسیب قابل اثبات است.", "بازار رسانه به‌تنهایی تنوع مطلوب را تضمین نمی‌کند.", "نهاد تنظیم‌گر می‌تواند مستقل و پاسخ‌گو باشد.", "قانون و رویهٔ قضایی قابل مقایسه و انتقال محدود است."],
        theorists=[
            {"role": "آزادی بیان و تنظیم‌گری", "name_fa": "اوون فیس"},
            {"role": "سیاست‌گذاری رسانه", "name_fa": "دس فریدمن"},
        ],
        theorists_text="اوون فیس نشان داد که تنظیم‌گری می‌تواند در خدمت تنوع بیان باشد نه فقط محدودکنندهٔ آن؛ دس فریدمن سیاست‌گذاری رسانه را فرایندی سیاسی و متأثر از مالکیت و مناسبات دولت و بازار تحلیل کرد.",
        studies=[
            "طنز آزادی بیان (فیس، ۱۹۹۶): دفاع از تنظیم‌گری در خدمت کثرت بیان.",
            "سیاست‌گذاری رسانه (فریدمن، ۲۰۰۸): سیاست رسانه به‌عنوان فرایند سیاسی.",
            "تحلیل تطبیقی مقررات پخش: مقایسهٔ نهادهای تنظیم‌گر و حدود استقلال آن‌ها.",
            "پژوهش مسئولیت پلتفرم: توزیع مسئولیت میان کاربر، پلتفرم و دولت.",
            "مطالعات حریم خصوصی و داده: تعادل نظارت و حقوق کاربر.",
            "پژوهش خودتنظیم‌گری رسانه: کارآمدی پیمان‌های صنفی در برابر قاعده‌گذاری دولتی.",
        ],
    ),
    "DSC-017": dict(
        mapping=D017,
        definition="مطالعات ارتباطات علم به جریان، بازنمایی و دریافت دانش علمی در میان عموم، سیاست‌گذاران و گروه‌های ذی‌نفع می‌پردازد و سه پرسش را دنبال می‌کند: علم چگونه بازنمایی می‌شود، عموم چگونه آن را تفسیر می‌کند، و چه مداخله‌ای اعتماد و سواد علمی را تقویت می‌کند.",
        mechanism="فرایند از بازنمایی آغاز می‌شود: رسانه و نهاد علمی چه روایتی از یافته می‌سازند و چه چیزی حذف می‌شود. سپس دریافت عمومی بررسی می‌گردد؛ نه به‌عنوان انبار خالی، بلکه به‌عنوان تفسیری مبتنی بر تجربه، هویت و اعتماد نهادی. در گام بعد مداخله طراحی می‌شود: آموزش، گفت‌وگوی عمومی، مشارکت شهروندی یا ارتباط بحران. سرانجام اثر مداخله بر دانش، نگرش و رفتار سنجیده و بازخورد آن به سیاست علم بازگردانده می‌شود.",
        critiques="۱. مدل کمبود دانش، شکاف علمی را به نقص عمومی فرو می‌کاهد و نقش نهاد علم را نادیده می‌گیرد. ۲. سنجش سواد علمی با آزمون واژگان، فهم فرایند علم را نمی‌سنجد. ۳. اعتماد به علم تابع تجربهٔ نهادی است و با اطلاع‌رسانی بیشتر لزوماً افزایش نمی‌یابد. ۴. ارتباط بحران می‌تواند عدم قطعیت را پنهان کند و اعتماد را در بلندمدت فرسوده سازد.",
        evolution="حوزه از سنجش سواد علمی در دههٔ ۱۹۷۰ آغاز شد، در دههٔ ۱۹۹۰ با نقد مدل کمبود و مطالعات درک عمومی علم دگرگون شد، در دههٔ ۲۰۰۰ به گفت‌وگو و مشارکت عمومی گرایش یافت و امروز بر اعتماد، ارتباط بحران سلامت و مقابله با اطلاعات نادرست علمی متمرکز است.",
        principles=["پرهیز از مدل یک‌سویهٔ انتقال", "شفافیت دربارهٔ عدم قطعیت", "گفت‌وگو به‌جای تحمیل", "توجه به هویت و اعتماد مخاطب", "هم‌طراحی با جامعهٔ هدف", "سنجش فرایند علم نه فقط واژگان"],
        assumptions=["عموم مخاطب منفعل و تهی از دانش نیست.", "تفسیر عمومی تحت تأثیر هویت و تجربه شکل می‌گیرد.", "اعتماد نهادی بر پذیرش پیام اثر می‌گذارد.", "ارتباط مؤثر نیازمند تعامل دوسویه است."],
        theorists=[
            {"role": "نقد مدل کمبود و درک عمومی علم", "name_fa": "برایان واین"},
            {"role": "مدل‌های ارتباطات عمومی علم", "name_fa": "ماسیمیانو بوکی و برایان ترنچ"},
        ],
        theorists_text="برایان واین با مطالعهٔ دریافت عمومی علم نشان داد که واکنش غیرمتخصصان تفسیری فرهنگی است نه صرفاً نادانی؛ بوکی و ترنچ نیز تحول مدل‌ها از انتقال یک‌سویه به گفت‌وگو و مشارکت را نظام‌مند کردند.",
        studies=[
            "سوءتفاهم سوءتفاهم‌شده (واین، ۱۹۹۲): نقد مدل کمبود و نقش هویت اجتماعی.",
            "راهنمای ارتباطات عمومی علم و فناوری (بوکی و ترنچ، ۲۰۲۱): مرور مدل‌ها و رویه‌های ارتباط علم.",
            "پژوهش‌های اعتماد به علم: رابطهٔ تجربهٔ نهادی و پذیرش یافته‌ها.",
            "مطالعات ارتباط بحران سلامت: مدیریت عدم قطعیت در اپیدمی‌ها.",
            "تحلیل بازنمایی علم در خبر: ساده‌سازی و اغراق در پوشش یافته‌ها.",
        ],
    ),
    "DSC-018": dict(
        mapping=D018,
        definition="مطالعات ارتباطات دینی به تعامل دین، رسانه و ارتباطات می‌پردازد: بازنمایی دین در رسانه، تبلیغ و ارتباطات دینی، دین دیجیتال و معنویت آنلاین، ارتباطات آیینی و مناسکی، و گفتمان و مرجعیت دینی در فضای رسانه‌ای.",
        mechanism="تحلیل از دو سو انجام می‌شود. از یک سو بازنمایی بررسی می‌شود: رسانه چه تصویری از دین، نمادها و کنشگران دینی می‌سازد و چه چیزی را حذف یا ساده می‌کند. از سوی دیگر عمل دینی در بستر دیجیتال رصد می‌گردد: جماعت آنلاین، مناسک مجازی، تولید محتوای تبلیغی و منازعه بر سر مرجعیت. سپس تعامل این دو لایه در بافت فرهنگی و سیاسی تفسیر می‌شود.",
        critiques="۱. حساسیت موضوع دین، بی‌طرفی روش‌شناختی را دشوار می‌کند. ۲. تمرکز بر رسانه‌های غالب می‌تواند تجربهٔ گروه‌های دینی کوچک را نادیده بگیرد. ۳. مفهوم دین دیجیتال مرز میان آنلاین و آفلاین را مبهم می‌کند. ۴. تعمیم یافته‌های یک سنت دینی به سنت‌های دیگر اعتبار ندارد.",
        evolution="این قلمرو از دههٔ ۱۹۹۰ با مطالعهٔ پوشش خبری دین و سپس با ظهور وب به دین آنلاین گسترش یافت. در دههٔ ۲۰۱۰ مفهوم دین دیجیتال به‌عنوان عمل شبکه‌ای تثبیت شد و امروز بر مرجعیت دینی در پلتفرم‌ها، معنویت آنلاین و ارتباطات آیینی تمرکز دارد.",
        principles=["بی‌طرفی روش‌شناختی نسبت به باورها", "توجه به تنوع سنت‌های دینی", "پیوند تحلیل متن با عمل دینی", "ملاحظهٔ اخلاق پژوهش در جوامع دینی", "پرهیز از تقلیل دین به بازنمایی رسانه‌ای"],
        assumptions=["دین و رسانه یکدیگر را متقابلاً شکل می‌دهند.", "عمل دینی در فضای دیجیتال امتداد عمل آفلاین است.", "مرجعیت دینی در بستر شبکه‌ای بازتوزیع می‌شود.", "معنا در بافت فرهنگی کنشگران ساخته می‌شود."],
        theorists=[
            {"role": "دین دیجیتال و دین شبکه‌ای", "name_fa": "هایدی کمپبل"},
            {"role": "دین و رسانه", "name_fa": "استیوارت هوور"},
        ],
        theorists_text="هایدی کمپبل دین دیجیتال را عمل شبکه‌ای دانست که جماعت، مرجعیت، هویت و مناسک در آن میان آنلاین و آفلاین جابه‌جا می‌شوند؛ استیوارت هوور نیز میانجی‌گری روزمرهٔ دین در رسانه را تحلیل کرد.",
        studies=[
            "رابطهٔ دین آنلاین و آفلاین (کمپبل، ۲۰۱۲): دین دیجیتال به‌عنوان عمل شبکه‌ای.",
            "دین در عصر رسانه (هوور، ۲۰۰۶): میانجی‌گری روزمرهٔ باور در رسانه.",
            "مطالعات جماعت‌های آنلاین: شکل‌گیری اجتماع دینی در پلتفرم‌ها.",
            "پژوهش مرجعیت دینی: بازتوزیع اقتدار در شبکه‌های اجتماعی.",
            "تحلیل مناسک مجازی: بازسازی آیین در بستر دیجیتال.",
            "مطالعهٔ تبلیغ دینی در شبکه‌های اجتماعی: تغییر زبان و مخاطب.",
            "پژوهش معنویت آنلاین: تجربهٔ فردی باور در فضای شبکه‌ای.",
        ],
        detailed_analysis="مطالعات ارتباطات دینی قلمروی نو و میان‌رشته‌ای است که در تقاطع مطالعات دین، ارتباطات و رسانه شکل گرفته است. پرسش بنیادین آن دوگانه است: از یک سو دین و باور چگونه در رسانه بازنمایی و گاه کج یا ساده‌سازی می‌شوند، و از سوی دیگر رسانه و فناوری دیجیتال چگونه با معنویت و جوامع دینی تعامل دارند.\nبه دلیل نو بودن این قلمرو، هنوز چارچوب نظری واحد و نظریه‌پرداز بنیان‌گذار مشخصی ندارد و بیشتر از پژوهش‌های نوظهور تغذیه می‌کند. چالش اصلی پژوهش، حساسیت موضوع دین و تنوع باورهاست که روش و تفسیر را به دقت و بی‌طرفی فرا می‌خواند.",
    ),
    "DSC-019": dict(
        mapping=D019,
        definition="مطالعات ارتباطات سلامت و محیط‌زیست حوزه‌ای کاربردی و میان‌رشته‌ای است که نقش ارتباطات را در ارتقای سلامت عمومی، مدیریت ریسک و بحران، و پایداری محیط‌زیست بررسی می‌کند و هدفش تغییر رفتار جمعیت هدف در جهت منافع سلامت و پایداری است.",
        mechanism="مداخلهٔ ارتباطی با تحلیل مخاطب و رفتار هدف آغاز می‌شود: چه باور، هنجار و مانعی رفتار را شکل می‌دهد. سپس پیام و کانال بر پایهٔ مدل رفتاری انتخاب می‌شود — نگرش، هنجار ذهنی، کنترل ادراک‌شده، یا ادراک ریسک. پیام با آزمون پیش‌آزمون و اصلاح، در معرض مخاطب قرار می‌گیرد. سرانجام اثر آن بر آگاهی، نیت و رفتار سنجیده و مداخله بازطراحی می‌گردد.",
        critiques="۱. مدل‌های رفتاری فردمحورند و نقش ساختار، فقر و دسترسی را کم‌برجسته می‌کنند. ۲. کمپین‌ها اغلب شکاف سلامت میان گروه‌ها را گسترده‌تر می‌کنند. ۳. ترس‌افکنی بی‌پشتوانه اثر معکوس دارد. ۴. سنجش تغییر رفتار به خودگزارشی وابسته و در معرض سوگیری است. ۵. در بحران محیط‌زیست، منافع صنعتی می‌تواند پیام علمی را تحریف کند.",
        evolution="حوزه از کمپین‌های سلامت دههٔ ۱۹۷۰ و مدل‌های تغییر رفتار شکل گرفت، در دههٔ ۱۹۸۰ با ارتباطات ریسک و ادراک ریسک گسترش یافت، در دههٔ ۲۰۰۰ به سواد سلامت و ارتباطات بحران گرایش یافت و امروز بر اطلاعات نادرست سلامت، عدالت سلامت و ارتباطات اقلیمی متمرکز است؛ همچنین سنجش مواجهه و دوز پیام به معیار ارزیابی استاندارد بدل شده است.",
        principles=["طراحی مداخله بر پایهٔ مدل رفتاری", "پیش‌آزمون پیام پیش از انتشار", "پرهیز از ترس‌افکنی بی‌پشتوانه", "توجه به عدالت و دسترسی گروه‌های کم‌برخوردار", "شفافیت دربارهٔ عدم قطعیت ریسک", "ارزیابی اثر با سنجه‌های معتبر"],
        assumptions=["رفتار تابع نیت و کنترل ادراک‌شده است.", "ادراک ریسک عمومی با احتمال فنی یکسان نیست.", "پیام متناسب با مخاطب اثر بیشتری دارد.", "تغییر پایدار نیازمند پشتوانهٔ محیطی و ساختاری است."],
        theorists=[
            {"role": "نظریهٔ رفتار برنامه‌ریزی‌شده", "name_fa": "ایسک آجین"},
            {"role": "ادراک ریسک", "name_fa": "پاول اسلوویک"},
        ],
        theorists_text="ایسک آجین رفتار را تابع نیت دانست که از نگرش، هنجار ذهنی و کنترل ادراک‌شده ساخته می‌شود؛ پاول اسلوویک نشان داد داوری عمومی دربارهٔ ریسک بیشتر تحت تأثیر هراس و ناشناختگی است تا احتمال فنی.",
        studies=[
            "نظریهٔ رفتار برنامه‌ریزی‌شده (آجین، ۱۹۹۱): نگرش، هنجار و کنترل ادراک‌شده به‌عنوان پیش‌بینی‌کنندهٔ نیت.",
            "ادراک ریسک (اسلوویک، ۱۹۸۷): نقش هراس و ناشناختگی در داوری عمومی.",
            "کمپین‌های واکسیناسیون: آزمون پیام و اثر بر نیت رفتاری.",
            "ارتباطات بحران اقلیمی: چارچوب‌بندی عدم قطعیت و اعتماد.",
            "مطالعات سواد سلامت: پیوند سواد و رفتار محافظتی.",
            "پژوهش ارتباطات محیط‌زیست: چارچوب‌بندی پایداری و رفتار مصرف.",
            "مطالعهٔ ارتباطات خطر در بلایا: سرعت هشدار و اعتماد به منبع.",
            "تحلیل کمپین کاهش مصرف: پیوند هنجار اجتماعی و کنترل ادراک‌شده.",
        ],
        detailed_analysis="مطالعات ارتباطات سلامت و محیط‌زیست قلمروی کاربردی-میان‌رشته‌ای است که هدفش تغییر رفتار است. ستون نظری آن مدل‌های رفتاری‌اند؛ مهم‌ترین آن‌ها نظریهٔ اقدام معقول و نظریهٔ رفتار برنامه‌ریزی‌شدهٔ آجین است که رفتار را تابع نگرش، هنجارهای اجتماعی و کنترل ادراک‌شده می‌دانند.\nدر لایهٔ ریسک و بحران، چالش اصلی ارتباط مؤثر ریسک است: چگونه اطلاعات ریسک را بدون ترس‌افکنی بیش‌ازحد یا دست‌کم‌گرفتن به عموم برسانیم تا رفتار محافظتی را بپذیرند. ورود بحران‌های جهانی مانند اپیدمی‌ها اهمیت این حوزه را به‌شدت بالا برده است.",
    ),
}

NAME_FIX = {}
YEAR_FIX = {
    "DSC-015": "no year set: discipline-level card has no single verified founding date; the unverifiable applied-theorist entry was replaced with Porter, Kung and Picard",
    "DSC-016": "no year set: discipline-level card has no single verified founding date; theorists limited to Fiss (1996) and Freedman (2008)",
    "DSC-017": "no year set: discipline-level card has no single verified founding date; theorists limited to Wynne (1992) and Bucchi & Trench (2021)",
    "DSC-018": "no year set: discipline-level card has no single verified founding date; corrupted snippet in detailed_analysis was replaced and theorists limited to Campbell (2012) and Hoover (2006)",
    "DSC-019": "no year set: discipline-level card has no single verified founding date; corrupted snippet in detailed_analysis was replaced and theorists limited to Ajzen (1991) and Slovic (1987)",
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
                                       "verified": n_verified, "batch": 193}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH193 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
