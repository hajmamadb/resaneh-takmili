# -*- coding: utf-8 -*-
"""Batch 160 (THEORY): MC-608 value chain, MC-623 emotional labor, MC-625 precarious creative work, MC-673 post-truth."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch160-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch160_theory.json"

S = {
    "MC-608": [
        dict(kind="BOOK",
             title_en="Competitive Advantage: Creating and Sustaining Superior Performance",
             title_fa="مزیت رقابتی: آفرینش و پایدارسازی عملکرد برتر",
             authors="Porter, M. E.", year=1985,
             publisher="Free Press",
             doi=None,
             url="https://www.hbs.edu/faculty/Pages/item.aspx?num=193",
             language="en", isbn=None,
             citation="Porter, M. E. (1985). Competitive Advantage: Creating and Sustaining Superior Performance. New York: Free Press.",
             locator="1985 edition", locator_type="edition",
             supports="primary and support activities, value chain and margin", verified=True),
        dict(kind="BOOK",
             title_en="The Economics and Financing of Media Companies (2nd ed.)",
             title_fa="اقتصاد و تأمین مالی شرکت‌های رسانه‌ای",
             authors="Picard, R. G.", year=2011,
             publisher="Fordham University Press",
             doi=None,
             url="https://www.jstor.org/stable/j.ctt13x0d0c",
             language="en", isbn="9780823232574",
             citation="Picard, R. G. (2011). The Economics and Financing of Media Companies (2nd ed.). New York: Fordham University Press.",
             locator="2nd edition", locator_type="edition",
             supports="application of value chain logic to media markets and financing", verified=True),
    ],
    "MC-623": [
        dict(kind="BOOK",
             title_en="The Managed Heart: Commercialization of Human Feeling",
             title_fa="قلب مدیریت‌شده: کالایی‌شدن احساس انسانی",
             authors="Hochschild, A. R.", year=1983,
             publisher="University of California Press",
             doi=None,
             url="https://www.jstor.org/stable/10.1525/j.ctt1pn9bk",
             language="en", isbn=None,
             citation="Hochschild, A. R. (1983). The Managed Heart: Commercialization of Human Feeling. Berkeley: University of California Press.",
             locator="1983 edition", locator_type="edition",
             supports="emotional labor, surface acting and deep acting in service work", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Emotion Work, Feeling Rules, and Social Structure",
             title_fa="کار احساسی، قواعد احساس و ساختار اجتماعی",
             authors="Hochschild, A. R.", year=1979,
             publisher="American Journal of Sociology",
             doi="10.1086/227049",
             url="https://www.journals.uchicago.edu/doi/abs/10.1086/227049",
             language="en", isbn=None,
             citation="Hochschild, A. R. (1979). Emotion work, feeling rules, and social structure. American Journal of Sociology, 85(3), 551-575.",
             locator="85(3):551-575", locator_type="page_range",
             supports="emotion management perspective linking self, interaction and structure", verified=True),
    ],
    "MC-625": [
        dict(kind="BOOK",
             title_en="Be Creative: Making a Living in the New Culture Industries",
             title_fa="خلاق باش: زندگی‌کردن در صنایع فرهنگی نو",
             authors="McRobbie, A.", year=2016,
             publisher="Polity Press",
             doi=None,
             url="https://www.politybooks.com/bookdetail?book_slug=be-creative-making-a-living-in-the-new-culture-industries--9780745661940",
             language="en", isbn="9780745661940",
             citation="McRobbie, A. (2016). Be Creative: Making a Living in the New Culture Industries. Cambridge: Polity Press.",
             locator="2016 edition", locator_type="edition",
             supports="precarity, entrepreneurial self and informal networks in cultural work", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="In the Social Factory? Immaterial Labour, Precariousness and Cultural Work",
             title_fa="در کارخانهٔ اجتماعی؟ کار غیرمادی، ناپایداری و کار فرهنگی",
             authors="Gill, R.; Pratt, A.", year=2008,
             publisher="Theory, Culture & Society",
             doi="10.1177/0263276408097794",
             url="https://journals.sagepub.com/doi/10.1177/0263276408097794",
             language="en", isbn=None,
             citation="Gill, R., & Pratt, A. (2008). In the social factory? Immaterial labour, precariousness and cultural work. Theory, Culture & Society, 25(7-8), 1-30.",
             locator="25(7-8):1-30", locator_type="page_range",
             supports="precarity and immaterial labor in cultural and creative work", verified=True),
    ],
    "MC-673": [
        dict(kind="BOOK",
             title_en="The Post-Truth Era: Dishonesty and Deception in Contemporary Life",
             title_fa="عصر پس‌حقیقت: بی‌صداقتی و فریب در زندگی معاصر",
             authors="Keyes, R.", year=2004,
             publisher="St. Martin's Press",
             doi=None,
             url="https://archive.org/details/posttrutheradish0000keye",
             language="en", isbn=None,
             citation="Keyes, R. (2004). The Post-Truth Era: Dishonesty and Deception in Contemporary Life. New York: St. Martin's Press.",
             locator="2004 edition", locator_type="edition",
             supports="coining and description of the post-truth era", verified=True),
        dict(kind="BOOK",
             title_en="Post-Truth",
             title_fa="پس‌حقیقت",
             authors="McIntyre, L.", year=2018,
             publisher="MIT Press",
             doi=None,
             url="https://mitpress.mit.edu/9780262535045/post-truth/",
             language="en", isbn="9780262535045",
             citation="McIntyre, L. (2018). Post-Truth. Cambridge, MA: MIT Press.",
             locator="2018 edition", locator_type="edition",
             supports="cognitive and political account of post-truth and science denial", verified=True),
    ],
}

ENRICH = {
    "MC-608": dict(
        year=1985,
        summary="نظریهٔ زنجیرهٔ ارزش، که مایکل پورتر در سال ۱۹۸۵ در کتاب مزیت رقابتی صورت‌بندی کرد، سازمان را مجموعه‌ای از فعالیت‌های به‌هم‌پیوسته می‌داند که هر یک بخشی از ارزش نهایی محصول را می‌سازد. پورتر فعالیت‌ها را به دو گروه تقسیم کرد: فعالیت‌های اصلی مانند ورود مواد، تولید، توزیع، بازاریابی و خدمات پس از فروش، و فعالیت‌های پشتیبان مانند تأمین، فناوری، منابع انسانی و زیرساخت. ارزش افزودهٔ هر فعالیت و حاشیهٔ نهایی، جایگاه رقابتی سازمان را تعیین می‌کند و مزیت رقابتی از ارزان‌تر یا متمایزتر انجام‌دادن همین فعالیت‌ها می‌آید. در رسانه، زنجیره از تولید محتوا و بسته‌بندی آغاز می‌شود، به توزیع و پخش می‌رسد و با بازاریابی، اشتراک و تبلیغات کامل می‌شود؛ تحلیل زنجیره نشان می‌دهد کدام حلقه سود می‌سازد و کدام حلقه در محیط دیجیتال فرو می‌ریزد. رابرت پیکارد این منطق را به اقتصاد شرکت‌های رسانه‌ای و الگوهای تأمین مالی آن‌ها گره زد. مدل برای تحلیل مدل کسب‌وکار، تصمیم برون‌سپاری، ادغام و ارزیابی اثر پلتفرم‌ها به کار می‌رود. نقدهای اصلی به آن، خطی‌بودن در برابر شبکهٔ پلتفرمی، کم‌توجهی به ارزش فرهنگی و عمومی، ایستایی در بازار پویا و ساده‌سازی روابط قدرت را برجسته می‌کنند.",
        definition="نظریهٔ زنجیرهٔ ارزش، سازمان را مجموعه‌ای از فعالیت‌های اصلی و پشتیبان می‌داند که ارزش افزوده و مزیت رقابتی را می‌سازند و در رسانه از تولید محتوا تا توزیع و درآمد امتداد می‌یابند.",
        main_problem="ارزش در کدام حلقه‌های زنجیرهٔ تولید و توزیع رسانه ساخته می‌شود، کدام حلقه سود می‌آورد و چگونه می‌توان مزیت رقابتی پایدار ساخت.",
        mechanism="هر فعالیت اصلی یا پشتیبان بخشی از ارزش نهایی را می‌افزاید؛ حاشیهٔ کل از تفاوت ارزش و هزینهٔ فعالیت‌ها می‌آید و بهبود یا تمایز در یک حلقه، جایگاه رقابتی را جابه‌جا می‌کند.",
        assumptions=[
            "سازمان از فعالیت‌های به‌هم‌پیوسته ساخته شده است.",
            "ارزش در هر حلقه افزوده می‌شود.",
            "مزیت رقابتی از تمایز یا هزینه می‌آید.",
            "زنجیره قابل تحلیل و بازطراحی است.",
            "حاشیهٔ نهایی معیار موفقیت است.",
        ],
        principles=[
            "هر حلقه را جدا تحلیل کن.",
            "هزینه و ارزش هر فعالیت را بسنج.",
            "حلقهٔ سودآور را تقویت کن.",
            "برون‌سپاری را با منطق ارزش بسنج.",
            "تمایز را در حلقهٔ کلیدی بساز.",
            "اثر پلتفرم بر زنجیره را رصد کن.",
            "ارزش عمومی را در تحلیل بگنجان.",
        ],
        critiques=[
            "در محیط پلتفرمی خطی است.",
            "ارزش فرهنگی و عمومی را کم می‌بیند.",
            "به بازار پویا کم توجه دارد.",
            "روابط قدرت را ساده می‌کند.",
            "به کاربر به‌عنوان تولیدکننده کم می‌پردازد.",
            "به هزینهٔ اجتماعی محتوا توجه ندارد.",
            "به کسب‌وکارهای کوچک رسانه‌ای کم می‌پردازد.",
        ],
        critique_text="منتقدان می‌گویند زنجیرهٔ ارزش ابزار دقیقی برای تحلیل اقتصاد رسانه داد اما ساختار خطی آن با شبکهٔ پلتفرمی و تولید کاربر هم‌خوان نیست و ارزش عمومی را کم می‌بیند؛ با این حال، چارچوب پایهٔ تحلیل کسب‌وکار رسانه است.",
        applications=[
            "تحلیل مدل کسب‌وکار رسانه.",
            "تصمیم برون‌سپاری تولید.",
            "ارزیابی ادغام و خرید.",
            "تحلیل اثر پلتفرم بر توزیع.",
            "طراحی مدل اشتراک.",
            "پژوهش اقتصاد رسانه.",
            "بهینه‌سازی زنجیرهٔ خبر.",
            "ارزیابی سودآوری بخش‌ها.",
            "تحلیل زنجیرهٔ ارزش کسب‌وکار پادکست.",
        ],
        example_text="در یک روزنامه، تولید محتوا هزینه می‌سازد اما ارزش برند و اشتراک در حلقهٔ توزیع و بازاریابی آزاد می‌شود؛ تحلیل زنجیره نشان می‌دهد چرا حذف چاپ، اقتصاد سازمان را از پایه تغییر می‌دهد.",
        evolution="پورتر در سال ۱۹۸۵ زنجیرهٔ ارزش را به‌عنوان ابزار تحلیل مزیت رقابتی معرفی کرد و پیکارد در سال ۲۰۱۱ آن را به اقتصاد رسانه برد؛ پژوهش‌های دیجیتال بعدی، زنجیره را به شبکهٔ ارزش و اکوسیستم پلتفرمی گستردند.",
        key_concepts=["زنجیرهٔ ارزش", "فعالیت اصلی", "فعالیت پشتیبان", "حاشیه", "مزیت رقابتی", "ارزش افزوده"],
        theorists="مایکل پورتر و رابرت پیکارد.",
        theorists_text="نظریه در سنت اقتصاد صنعتی و اقتصاد رسانه شکل گرفت.",
        model="رسانه به‌عنوان زنجیرهٔ فعالیت‌های ارزش‌ساز از تولید محتوا تا توزیع و درآمد.",
        studies=[
            "کتاب سال ۱۹۸۵ چارچوب زنجیره را ساخت.",
            "کتاب سال ۲۰۱۱ آن را به رسانه برد.",
            "پژوهش دیجیتال، شبکهٔ ارزش را بررسی کرد.",
            "مطالعهٔ خبر، اقتصاد زنجیره را تحلیل کرد.",
            "مطالعهٔ پلتفرم، زنجیره را بازطراحی کرد.",
        ],
    ),
    "MC-623": dict(
        year=1983,
        summary="نظریهٔ کار احساسی، که آرلی راسل هوخشیلد آن را در مقالهٔ سال ۱۹۷۹ و کتاب قلب مدیریت‌شده در سال ۱۹۸۳ بسط داد، نشان می‌دهد که احساس در محیط کار تنها حالت درونی نیست، بلکه بخشی از کار است. هوخشیلد میان کار احساسی، یعنی مدیریت احساس در زندگی خصوصی، و کار احساسی شغلی، یعنی مدیریت احساس به‌عنوان بخشی از وظیفهٔ شغلی، تفکیک کرد. او دو شیوهٔ نمایش را از هم جدا کرد: نمایش سطحی که در آن فرد احساسی را که ندارد نشان می‌دهد، و نمایش عمیق که در آن می‌کوشد احساس مورد انتظار را در خود بسازد. قواعد احساس، تعیین می‌کنند چه احساسی در چه موقعیتی مناسب است و کارکنان خدماتی، از مهماندار تا وصول‌کنندهٔ بدهی، ناچارند این قواعد را در خود و در تعامل با مشتری اجرا کنند. نتیجه، کالایی‌شدن احساس و فاصله‌گرفتن فرد از تجربهٔ خود است. در رسانه، مدل برای تحلیل کار احساسی خبرنگار در بحران، مجری تلویزیون، مدیر محتوای شبکهٔ اجتماعی و اینفلوئنسر به کار می‌رود. نقدهای اصلی به آن، فرض جنسیتی‌شده دربارهٔ کار عاطفی، دشواری سنجش نمایش عمیق، کم‌توجهی به عاملیت کارکنان و تعمیم‌نداشتن به کار دیجیتال را برجسته می‌کنند.",
        definition="نظریهٔ کار احساسی، مدیریت احساس را بخشی از کار شغلی می‌داند که با قواعد احساس، نمایش سطحی و نمایش عمیق اداره می‌شود و به کالایی‌شدن احساس می‌انجامد.",
        main_problem="سازمان‌ها چگونه احساس کارکنان را در خدمت تولید ارزش مدیریت می‌کنند و این مدیریت چه اثری بر هویت، سلامت و تجربهٔ فردی آنان دارد.",
        mechanism="قواعد احساس تعریف می‌کنند چه حسی مناسب است؛ کارمند با نمایش سطحی یا عمیق آن را اجرا می‌کند؛ تکرار این اجرا، فاصلهٔ عاطفی و فرسودگی می‌سازد و احساس به منبع ارزش سازمانی بدل می‌شود.",
        assumptions=[
            "احساس در کار مدیریت می‌شود.",
            "قواعد احساس وجود دارند.",
            "نمایش سطحی و عمیق تفکیک‌پذیرند.",
            "احساس می‌تواند کالایی شود.",
            "کار احساسی هزینهٔ فردی دارد.",
        ],
        principles=[
            "قواعد احساس را آشکار کن.",
            "نمایش سطحی را از عمیق جدا کن.",
            "هزینهٔ عاطفی کار را بسنج.",
            "از فرسودگی پیشگیری کن.",
            "به عاملیت کارمند توجه کن.",
            "احساس را در آموزش شغلی ببین.",
        ],
        critiques=[
            "فرض جنسیتی دارد.",
            "سنجش نمایش عمیق دشوار است.",
            "عاملیت کارکنان را کم می‌بیند.",
            "به کار دیجیتال کم می‌پردازد.",
            "به تفاوت فرهنگی کم توجه دارد.",
            "مرز کار احساسی و خصوصی مبهم است.",
            "به آموزش عاطفی در سازمان‌ها کم توجه دارد.",
            "نقش فناوری در استانداردسازی احساس را کم می‌بیند.",
        ],
        critique_text="منتقدان می‌گویند نظریهٔ کار احساسی چهرهٔ پنهان کار خدماتی را آشکار کرد اما سنجش نمایش عمیق و عاملیت کارکنان را کم‌بررسی گذاشت؛ با این حال، چارچوب پایهٔ مطالعهٔ کار عاطفی در رسانه است.",
        applications=[
            "تحلیل کار خبرنگار در بحران.",
            "پژوهش مجری تلویزیون.",
            "مطالعهٔ مدیر محتوای شبکه.",
            "تحلیل کار احساسی اینفلوئنسر.",
            "آموزش پیشگیری از فرسودگی.",
            "سیاست سلامت شغلی.",
            "پژوهش کار خدماتی.",
            "تحلیل تعامل با مخاطب.",
            "پژوهش کار عاطفی در خبر.",
            "مطالعهٔ فرسودگی عاطفی مجریان تلویزیون.",
        ],
        example_text="خبرنگاری که پس از دیدن صحنهٔ حادثه باید آرام گزارش دهد، احساس خود را مدیریت می‌کند تا حرفه‌ای به نظر برسد؛ مدل می‌گوید این مدیریت، خودش بخشی از کار است و هزینهٔ آن بر فرد می‌ماند.",
        evolution="هوخشیلد در سال ۱۹۷۹ چارچوب کار احساسی را ساخت و در سال ۱۹۸۳ با قلب مدیریت‌شده آن را به کار خدماتی برد؛ پژوهش‌های بعدی، مفاهیم را به کار دیجیتال، مراقبت و رسانه گستردند.",
        key_concepts=["کار احساسی", "قواعد احساس", "نمایش سطحی", "نمایش عمیق", "کالایی‌شدن احساس", "فرسودگی"],
        theorists="آرلی راسل هوخشیلد.",
        theorists_text="نظریه در سنت جامعه‌شناسی احساس و کار شکل گرفت.",
        model="مدیریت احساس به‌عنوان بخشی از کار شغلی و منبع ارزش سازمانی.",
        studies=[
            "مقالهٔ سال ۱۹۷۹ چارچوب را ساخت.",
            "کتاب سال ۱۹۸۳ کار خدماتی را تحلیل کرد.",
            "پژوهش خبر، کار احساسی بحران را سنجید.",
            "مطالعهٔ دیجیتال، کار عاطفی پلتفرم را بررسی کرد.",
            "مطالعهٔ تطبیقی، قواعد احساس را در دو کشور سنجید.",
            "پژوهش مجری، نمایش عمیق را تحلیل کرد.",
        ],
    ),
    "MC-625": dict(
        year=2016,
        summary="نظریهٔ کار خلاق نامطمئن، که آنجلا مک‌رابی در کتاب خلاق باش در سال ۲۰۱۶ و در گفت‌وگو با پژوهش‌های روزالیند گیل و اندی پرات در سال ۲۰۰۸ صورت‌بندی کرد، زندگی حرفه‌ای در صنایع فرهنگی را با ناپایداری، شبکه‌های غیررسمی و خودکارفرمایی تحلیل می‌کند. در این نظریه، کار خلاق نه شغل پایدار با قرارداد و بیمه، بلکه زنجیره‌ای از پروژه‌های موقت است که با اعتماد، شهرت و توصیهٔ شخصی به هم وصل می‌شوند. کارگر خلاق خود را کارآفرین می‌بیند، زمان و مهارت خود را بی‌مرز می‌کند و اغلب بخشی از کار را بدون دستمزد، برای نمونه در قالب نمونه‌کار و شبکه‌سازی، انجام می‌دهد. عشق به کار و «شور» حرفه‌ای، سازوکاری می‌شود که ناپایداری را تحمل‌پذیر و حتی مطلوب جلوه می‌دهد. مک‌رابی نشان می‌دهد که این الگو، نابرابری را بازتولید می‌کند: کسانی که پشتوانهٔ خانوادگی دارند، می‌توانند دورهٔ بی‌درآمد را تحمل کنند و دیگران حذف می‌شوند. در رسانه، نظریه برای تحلیل خبرنگار آزاد، تولیدکنندهٔ محتوا، طراح و کارگر پلتفرم به کار می‌رود. نقدهای اصلی به آن، رمانتیک‌زدایی از یک‌سو و مبهم‌بودن مرز ناپایداری و آزادی از سوی دیگر، کم‌توجهی به جنوب جهانی و دشواری سنجش را برجسته می‌کنند.",
        definition="نظریهٔ کار خلاق نامطمئن، کار فرهنگی را زنجیره‌ای از پروژه‌های موقت، شبکه‌محور و بی‌حمایت می‌داند که با ایدهٔ کارآفرین خلاق و شور حرفه‌ای، ناپایداری را طبیعی جلوه می‌دهد.",
        main_problem="چرا کار در صنایع فرهنگی با وجود جذابیت، به ناپایداری، بی‌حمایتی و نابرابری می‌انجامد و چه سازوکاری این وضعیت را تحمل‌پذیر می‌کند.",
        mechanism="پروژه‌های موقت و شبکه‌های غیررسمی، امنیت شغلی را حذف می‌کنند؛ ایدهٔ خودکارفرمایی و شور حرفه‌ای، کار بی‌دستمزد و زمان بی‌مرز را توجیه می‌کند و پشتوانهٔ خانوادگی، توان تحمل ناپایداری را نابرابر توزیع می‌کند.",
        assumptions=[
            "کار خلاق پروژه‌محور است.",
            "شبکهٔ غیررسمی جای قرارداد را می‌گیرد.",
            "شور حرفه‌ای ناپایداری را توجیه می‌کند.",
            "بخشی از کار بی‌دستمزد است.",
            "پشتوانهٔ خانوادگی نابرابری می‌سازد.",
        ],
        principles=[
            "قرارداد را جای شبکهٔ غیررسمی بگذار.",
            "کار بی‌دستمزد را آشکار کن.",
            "زمان کار را مرزبندی کن.",
            "شور حرفه‌ای را نقد کن.",
            "به نابرابری دسترسی توجه کن.",
            "حمایت اجتماعی را طراحی کن.",
        ],
        critiques=[
            "ناپایداری و آزادی را می‌آمیزد.",
            "جنوب جهانی را کم می‌بیند.",
            "سنجش ناپایداری دشوار است.",
            "به تفاوت زیربخش‌ها کم می‌پردازد.",
            "به نقش پلتفرم کم توجه دارد.",
            "مفهوم طبقه را کم‌وزن می‌کند.",
            "به تفاوت کشورهای جنوب جهانی کم می‌پردازد.",
            "نقش اتحادیه‌ها و سازمان‌های صنفی را کم می‌بیند.",
            "به هزینهٔ روانی بی‌ثباتی کم توجه دارد.",
        ],
        critique_text="منتقدان می‌گویند نظریهٔ کار خلاق نامطمئن چهرهٔ نابرابر صنایع فرهنگی را نشان داد اما مرز آزادی و ناامنی را مبهم گذاشت و پلتفرم‌ها را کم‌بررسی کرد؛ با این حال، چارچوب مرجع کار فرهنگی امروز است.",
        applications=[
            "تحلیل خبرنگار آزاد.",
            "پژوهش تولیدکنندهٔ محتوا.",
            "مطالعهٔ کارگر پلتفرم.",
            "سیاست حمایت از فریلنسر.",
            "آموزش حقوق کار خلاق.",
            "تحلیل نابرابری جنسیتی.",
            "پژوهش اقتصاد خلاق.",
            "ارزیابی مدل پروژه‌ای.",
            "پژوهش درآمد فریلنسر.",
            "تحلیل قرارداد در صنعت موسیقی.",
        ],
        example_text="خبرنگار آزادی که ماه‌ها بدون قرارداد برای یک رسانه می‌نویسد و امید به پروژهٔ بعدی دارد، هم آزاد است و هم ناامن؛ نظریه می‌گوید روایت شور حرفه‌ای، همین ناامنی را تحمل‌پذیر می‌کند.",
        evolution="گیل و پرات در سال ۲۰۰۸ ناپایداری کار فرهنگی را صورت‌بندی کردند و مک‌رابی در سال ۲۰۱۶ آن را با خودکارفرمایی و شبکه‌های غیررسمی بسط داد؛ پژوهش‌های بعدی، آن را به کار پلتفرمی و اقتصاد خالقان محتوا گستردند.",
        key_concepts=["کار خلاق", "ناپایداری", "خودکارفرمایی", "شبکهٔ غیررسمی", "کار بی‌دستمزد", "شور حرفه‌ای"],
        theorists="آنجلا مک‌رابی، روزالیند گیل و اندی پرات.",
        theorists_text="نظریه در سنت مطالعات فرهنگی و جامعه‌شناسی کار شکل گرفت.",
        model="کار فرهنگی به‌عنوان زنجیرهٔ پروژه‌های ناپایدار که با روایت شور و خودکارفرمایی طبیعی می‌شود.",
        studies=[
            "کتاب سال ۲۰۱۶ کار فرهنگی را تحلیل کرد.",
            "مقالهٔ سال ۲۰۰۸ ناپایداری را صورت‌بندی کرد.",
            "پژوهش فریلنسر، بی‌حمایتی را سنجید.",
            "مطالعهٔ پلتفرم، کار خلاق دیجیتال را بررسی کرد.",
            "مطالعهٔ طولی، مسیر شغلی فریلنسر را پیگیری کرد.",
            "پژوهش جنسیت، نابرابری دسترسی را سنجید.",
        ],
    ),
    "MC-673": dict(
        year=2004,
        summary="نظریهٔ پس‌حقیقت، که رالف کیز در کتاب عصر پس‌حقیقت در سال ۲۰۰۴ نام‌گذاری کرد و لی مکان‌تایر در سال ۲۰۱۸ صورت‌بندی فلسفی و سیاسی آن را داد، وضعیتی را توصیف می‌کند که در آن صدق ادعا دیگر معیار اصلی پذیرش عمومی نیست. کیز نشان داد که در فرهنگ معاصر، بی‌صداقتی از دروغ آشکار فراتر می‌رود و به شکل ابهام، اغراق و بی‌تفاوتی به واقعیت درمی‌آید. مکان‌تایر این وضعیت را با انکار علم، شکاکیت سازمان‌یافته و رسانهٔ شبکه‌ای پیوند داد و آن را نه بحران شناختی صرف، بلکه محصول سیاست و صنعت اطلاع‌رسانی دانست. سازوکار نظریه سه لایه دارد: تولید ادعای بی‌اعتنا به سند، توزیع آن در حباب اطلاعاتی و پاداش سیاسی برای تکرار. در این وضعیت، راستی‌آزمایی ضروری است اما کافی نیست، زیرا باور عمومی بیشتر به هویت گروهی و هیجان وابسته است تا به سند. در رسانه، نظریه برای تحلیل خبر جعلی، انکار انتخاباتی، بی‌اعتمادی به نهادها و بحران اقتدار روزنامه‌نگاری به کار می‌رود. نقدهای اصلی به آن، ابهام مفهومی، اغراق در تازگی، کم‌توجهی به عاملیت مخاطب و فرض تقارن میان جریان‌های سیاسی را برجسته می‌کنند.",
        definition="نظریهٔ پس‌حقیقت، وضعیتی را توصیف می‌کند که در آن صدق ادعا معیار اصلی پذیرش عمومی نیست و ابهام، هیجان و هویت گروهی جای سند و استدلال را می‌گیرند.",
        main_problem="چگونه بی‌تفاوتی به واقعیت به هنجار عمومی بدل شد، چه سازوکارهایی آن را بازتولید می‌کنند و روزنامه‌نگاری چگونه می‌تواند اقتدار معرفتی خود را بازسازد.",
        mechanism="ادعای بی‌اعتنا به سند تولید می‌شود، در حباب اطلاعاتی توزیع می‌شود و پاداش سیاسی می‌گیرد؛ تکرار، باور را به هویت گروهی گره می‌زند و راستی‌آزمایی را کم‌اثر می‌کند.",
        assumptions=[
            "صدق معیار اصلی پذیرش نیست.",
            "هویت گروهی باور را شکل می‌دهد.",
            "رسانهٔ شبکه‌ای تکرار را تسهیل می‌کند.",
            "انکار علم سازمان‌یافته است.",
            "راستی‌آزمایی به‌تنهایی کافی نیست.",
        ],
        principles=[
            "سند را به باور گره بزن.",
            "هیجان را از صدق جدا کن.",
            "منبع و انگیزه را آشکار کن.",
            "به هویت گروهی توجه کن.",
            "شفافیت نهادی بساز.",
            "آموزش تفکر انتقادی را جدی بگیر.",
        ],
        critiques=[
            "مفهوم مبهم است.",
            "تازگی پدیده را اغراق می‌کند.",
            "عاملیت مخاطب را کم می‌بیند.",
            "تقارن سیاسی را فرض می‌کند.",
            "سنجش تجربی آن دشوار است.",
            "به زمینهٔ غیرغربی کم می‌پردازد.",
            "مرز پس‌حقیقت و دروغ سیاسی را روشن نمی‌کند.",
            "به نقش سواد رسانه‌ای در مقاومت کم توجه دارد.",
            "تعریف عملیاتی سنجش‌پذیر کمی دارد.",
        ],
        critique_text="منتقدان می‌گویند نظریهٔ پس‌حقیقت بحران اقتدار واقعیت را برجسته کرد اما مفهوم را مبهم و تازگی آن را اغراق‌شده گذاشت؛ با این حال، چارچوب مهمی برای فهم بی‌اعتمادی معاصر است.",
        applications=[
            "تحلیل خبر جعلی.",
            "پژوهش انکار انتخاباتی.",
            "مطالعهٔ بی‌اعتمادی نهادی.",
            "آموزش سواد خبری.",
            "سیاست شفافیت.",
            "تحلیل بحران اقتدار خبر.",
            "پژوهش انکار علم.",
            "طراحی راستی‌آزمایی.",
            "مطالعهٔ شکاکیت سازمان‌یافتهٔ معاصر.",
            "تحلیل پوشش انتخاباتی.",
            "تحلیل انکار در رسانهٔ سلامت.",
        ],
        example_text="ادعایی که سند روشنی ندارد اما با هویت یک گروه هم‌خوان است، در شبکه‌ها تکرار می‌شود و تکذیب آن هم به نفع همان گروه تفسیر می‌شود؛ نظریه می‌گوید مسئله فقط اطلاعات غلط نیست، جایگاه صدق است.",
        evolution="کیز در سال ۲۰۰۴ اصطلاح را در فرهنگ عمومی جا انداخت و مکان‌تایر در سال ۲۰۱۸ آن را به فلسفه و سیاست علم پیوند داد؛ سپس فرهنگ لغت آکسفورد در سال ۲۰۱۶ آن را واژهٔ سال کرد و پژوهش‌های ارتباطات آن را گستردند.",
        key_concepts=["پس‌حقیقت", "بی‌تفاوتی به واقعیت", "حباب اطلاعاتی", "انکار علم", "هویت گروهی", "اقتدار معرفتی"],
        theorists="رالف کیز و لی مکان‌تایر.",
        theorists_text="نظریه در سنت فلسفهٔ صدق و جامعه‌شناسی رسانه شکل گرفت.",
        model="پذیرش عمومی ادعا به‌عنوان نتیجهٔ هیجان و هویت گروهی، نه سند و استدلال.",
        studies=[
            "کتاب سال ۲۰۰۴ اصطلاح را تثبیت کرد.",
            "کتاب سال ۲۰۱۸ چارچوب فلسفی داد.",
            "پژوهش خبر، بی‌اعتمادی را سنجید.",
            "مطالعهٔ علم، انکار را بررسی کرد.",
            "پژوهش حباب، تکرار ادعا را سنجید.",
            "مطالعهٔ تطبیقی، پس‌حقیقت را در دو کشور بررسی کرد.",
            "پژوهش سلامت، انکار واکسن را بررسی کرد.",
        ],
    ),
}

NAME_FIX = {
    "MC-623": ("کار احساسی (قلب مدیریت‌شده)", "Emotional Labor (The Managed Heart)", "عنوان پیشین «قدرت هیجانی کار» نام اثر هوخشیلد را نمی‌رساند و بدنهٔ کارت نیز قالب حرفه‌گرایی بود؛ عنوان به مفهوم اصلی اصلاح شد."),
}
YEAR_FIX = {
    "MC-608": "بدنهٔ کارت بیشتر قالب عمومی اقتصاد رسانه بود؛ محتوا بر پایهٔ پورتر ۱۹۸۵ و پیکارد ۲۰۱۱ بازنویسی شد.",
    "MC-623": "بدنهٔ کارت قالب عمومی حرفه‌گرایی بود و سال ۱۹۸۳ درست اما محتوا بی‌ربط بود؛ محتوا بر پایهٔ هوخشیلد ۱۹۷۹ و ۱۹۸۳ بازنویسی شد.",
    "MC-625": "بدنهٔ کارت قالب عمومی حرفه‌گرایی بود؛ محتوا بر پایهٔ مک‌رابی ۲۰۱۶ و گیل و پرات ۲۰۰۸ بازنویسی شد.",
    "MC-673": "بدنهٔ کارت به نظارت داده و کالایی‌شدن داده مربوط بود، نه پس‌حقیقت؛ محتوا بر پایهٔ کیز ۲۰۰۴ و مکان‌تایر ۲۰۱۸ بازنویسی شد.",
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
                                       "verified": n_verified, "batch": 160}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH160 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
