# -*- coding: utf-8 -*-
"""Batch 140 (MODEL): full documentation for MC-309, MC-310, MC-319, MC-320."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch140-model-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch140_model.json"

S = {
    "MC-309": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Toward a General Model of Communication",
             title_fa="به سوی مدلی عمومی از ارتباط",
             authors="Gerbner, G.", year=1956,
             publisher="Audio-Visual Communication Review",
             doi="10.1007/BF02717110",
             url="https://link.springer.com/article/10.1007/BF02717110",
             language="en", isbn=None,
             citation="Gerbner, G. (1956). Toward a general model of communication. Audio-Visual Communication Review, 4(3), 171-199.",
             locator="4(3):171-199", locator_type="page_range",
             supports="perceptual model linking event, perception, message and reception", verified=True),
        dict(kind="BOOK_CHAPTER",
             title_en="Mass Media and Human Communication Theory",
             title_fa="رسانه‌های جمعی و نظریهٔ ارتباط انسانی",
             authors="Gerbner, G.", year=1967,
             publisher="Holt, Rinehart and Winston (Human Communication Theory)",
             doi=None, url=None, language="en", isbn=None,
             citation="Gerbner, G. (1967). Mass media and human communication theory. In F. E. X. Dance (Ed.), Human Communication Theory. New York: Holt, Rinehart and Winston.",
             locator="chapter", locator_type="SECTION",
             supports="later elaboration of the perceptual model for mass communication", verified=False),
    ],
    "MC-310": [
        dict(kind="BOOK_CHAPTER",
             title_en="A Transactional Model of Communication",
             title_fa="مدلی تراکنشی از ارتباط",
             authors="Barnlund, D. C.", year=1970,
             publisher="Harper & Row (Foundations of Communication Theory)",
             doi="10.1515/9783110878752.43",
             url="https://www.degruyterbrill.com/document/doi/10.1515/9783110878752.43/html",
             language="en", isbn=None,
             citation="Barnlund, D. C. (1970). A transactional model of communication. In K. K. Sereno & C. C. Mortensen (Eds.), Foundations of Communication Theory. New York: Harper & Row.",
             locator="chapter", locator_type="SECTION",
             supports="simultaneous transactional model with co-created meaning and public/private cues", verified=True),
        dict(kind="BOOK_CHAPTER",
             title_en="A Transactional Model of Communication (reprint)",
             title_fa="مدلی تراکنشی از ارتباط (بازچاپ)",
             authors="Barnlund, D. C.", year=2017,
             publisher="Routledge",
             doi="10.4324/9781315080918-5",
             url="https://www.taylorfrancis.com/chapters/edit/10.4324/9781315080918-5/transactional-model-communication-dean-barnlund",
             language="en", isbn=None,
             citation="Barnlund, D. C. (2017). A transactional model of communication. In Communication Theory (reprint). London: Routledge.",
             locator="chapter 5", locator_type="SECTION",
             supports="modern reprint documenting the transactional model", verified=True),
    ],
    "MC-319": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Elaboration Likelihood Model of Persuasion",
             title_fa="مدل احتمال تفصیل اقناع",
             authors="Petty, R. E.; Cacioppo, J. T.", year=1986,
             publisher="Advances in Experimental Social Psychology",
             doi="10.1016/S0065-2601(08)60214-2",
             url="https://doi.org/10.1016/S0065-2601(08)60214-2",
             language="en", isbn=None,
             citation="Petty, R. E., & Cacioppo, J. T. (1986). The elaboration likelihood model of persuasion. Advances in Experimental Social Psychology, 19, 123-205.",
             locator="19:123-205", locator_type="page_range",
             supports="dual-route model with central and peripheral processing along an elaboration continuum", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Personal Involvement as a Determinant of Argument-Based Persuasion",
             title_fa="درگیری شخصی به‌عنوان تعیین‌کنندهٔ اقناع مبتنی بر استدلال",
             authors="Petty, R. E.; Cacioppo, J. T.; Goldman, R.", year=1981,
             publisher="Journal of Personality and Social Psychology",
             doi=None,
             url="https://psycnet.apa.org/record/1982-09821-001",
             language="en", isbn=None,
             citation="Petty, R. E., Cacioppo, J. T., & Goldman, R. (1981). Personal involvement as a determinant of argument-based persuasion. Journal of Personality and Social Psychology, 41(5), 847-855.",
             locator="41(5):847-855", locator_type="page_range",
             supports="experimental evidence that involvement moderates argument-based versus cue-based persuasion", verified=True),
    ],
    "MC-320": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Heuristic versus Systematic Information Processing and the Use of Source versus Message Cues in Persuasion",
             title_fa="پردازش اطلاعات اکتشافی در برابر نظام‌مند و کاربرد نشانه‌های منبع در برابر پیام در اقناع",
             authors="Chaiken, S.", year=1980,
             publisher="Journal of Personality and Social Psychology",
             doi="10.1037/0022-3514.39.5.752",
             url="https://psycnet.apa.org/record/1981-05345-001",
             language="en", isbn=None,
             citation="Chaiken, S. (1980). Heuristic versus systematic information processing and the use of source versus message cues in persuasion. Journal of Personality and Social Psychology, 39(5), 752-766.",
             locator="39(5):752-766", locator_type="page_range",
             supports="two processing modes and reliance on source versus message cues", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Heuristic Processing Can Bias Systematic Processing",
             title_fa="پردازش اکتشافی می‌تواند پردازش نظام‌مند را سوگیرانه کند",
             authors="Chaiken, S.; Maheswaran, D.", year=1994,
             publisher="Journal of Personality and Social Psychology",
             doi="10.1037/0022-3514.66.3.460",
             url="https://pubmed.ncbi.nlm.nih.gov/8169760/",
             language="en", isbn=None,
             citation="Chaiken, S., & Maheswaran, D. (1994). Heuristic processing can bias systematic processing: Effects of source credibility, argument ambiguity, and task importance on attitude judgment. Journal of Personality and Social Psychology, 66(3), 460-473.",
             locator="66(3):460-473", locator_type="page_range",
             supports="additivity and bias effects between heuristic and systematic modes", verified=True),
    ],
}

ENRICH = {
    "MC-309": dict(
        year=1956,
        summary="مدل ادراکی گربر، مدلی در مبانی ارتباطات است که جورج گربنر نخست در سال ۱۹۵۶ در نشریهٔ ارتباط دیداری-شنیداری منتشر کرد و سپس در فصل سال ۱۹۶۷ آن را برای رسانه‌های جمعی گسترش داد. ادعای مرکزی این است که ارتباط زنجیره‌ای از ادراک و تبدیل است: رویدادی در محیط رخ می‌دهد، ادراک‌کننده آن را برمی‌گزیند و تفسیر می‌کند، سپس آن ادراک را به پیام تبدیل می‌کند؛ گیرنده نیز پیام را ادراک و بازتفسیر می‌کند. مدل دو بُعد را از هم جدا می‌کند: بُعد افقی که از رویداد به ادراک و پیام و دریافت می‌رود، و بُعد عمودی که فرایندهای دسترس‌پذیری، گزینش، بافت و کنترل را در هر مرحله نشان می‌دهد. گربنر تأکید کرد که ادراک، کنشی فعال و گزینشی است و پیام، بازنمایی واقعیت است نه خود واقعیت. او بعدها همین پیش‌فرض را در نظریهٔ کاشت به کار گرفت و نشان داد رسانه می‌تواند ادراک مخاطب از واقعیت اجتماعی را شکل دهد. نقدهای اصلی به مدل، پیچیدگی نمودار و دشواری آزمون تجربی، فرض ادراک‌کنندهٔ فعال بدون عملیاتی‌سازی کافی، کم‌توجهی به قدرت و اقتصاد رسانه، و تمرکز بر فرایند فردی به بهای ساختار اجتماعی را برجسته می‌کنند.",
        definition="مدل ادراکی گربر، ارتباط را زنجیره‌ای از ادراک گزینشی رویداد، تبدیل آن به پیام و بازادراک پیام توسط گیرنده می‌داند و بافت و کنترل را در هر مرحله وارد تحلیل می‌کند.",
        main_problem="چگونه رویداد بیرونی به ادراک، سپس به پیام و در نهایت به ادراک گیرنده تبدیل می‌شود و چه عواملی در هر مرحله بر این تبدیل اثر می‌گذارند.",
        mechanism="ادراک‌کننده رویداد را بر پایهٔ دسترس‌پذیری، گزینش و بافت درک می‌کند؛ ادراک به رمزهای پیام تبدیل می‌شود؛ گیرنده پیام را با همان فرایندهای گزینشی بازادراک می‌کند. کنترل و بافت در هر مرحله، شکل نهایی ادراک را تعیین می‌کنند.",
        assumptions=[
            "ادراک، کنشی فعال و گزینشی است.",
            "پیام بازنمایی رویداد است نه خود رویداد.",
            "بافت و کنترل در هر مرحله اثر می‌گذارند.",
            "گیرنده پیام را بازتفسیر می‌کند.",
            "زنجیرهٔ ادراک را می‌توان به مراحل قابل تفکیک شکست.",
        ],
        principles=[
            "ارتباط را زنجیرهٔ ادراک و تبدیل ببین.",
            "گزینش ادراکی را در مبدأ و مقصد بسنج.",
            "بافت و کنترل را در هر مرحله وارد کن.",
            "پیام را بازنمایی بدان نه واقعیت.",
            "مرز میان رویداد و ادراک آن را حفظ کن.",
            "مدل را مبنای تحلیل ادراک رسانه‌ای قرار بده.",
        ],
        critiques=[
            "نمودار مدل پیچیده و آزمون آن دشوار است.",
            "فرض ادراک فعال را عملیاتی نکرده است.",
            "قدرت و اقتصاد رسانه را کم‌رنگ می‌کند.",
            "بر فرایند فردی بیش از ساختار اجتماعی تأکید دارد.",
            "پیوند تجربی با نظریهٔ کاشت به‌طور کامل سنجیده نشده است.",
        ],
        critique_text="منتقدان می‌گویند مدل گربر با واردکردن ادراک و بافت، گامی مهم از مدل‌های انتقالی برداشت اما پیچیدگی آن آزمون تجربی را دشوار می‌کند و نقش نهادهای رسانه‌ای و قدرت را کم‌رنگ می‌گذارد؛ با این حال، پیوند ادراک و پیام را به هستهٔ تحلیل ارتباط تبدیل کرد.",
        applications=[
            "تحلیل ادراک مخاطب از خبر.",
            "مطالعهٔ بازنمایی واقعیت در رسانه.",
            "آموزش مبانی ادراک و گزینش.",
            "پژوهش پیش‌درآمد نظریهٔ کاشت.",
            "طراحی پیام با توجه به بافت ادراکی مخاطب.",
        ],
        example_text="خبرنگاری که رویدادی را مشاهده می‌کند، بر پایهٔ تجربه و بافت خود بخشی از آن را برمی‌گزیند و به خبر تبدیل می‌کند؛ مخاطب نیز همان خبر را با تجربهٔ خود بازتفسیر می‌کند. مدل گربر این دو مرحلهٔ گزینش و تبدیل را به هم پیوند می‌دهد.",
        evolution="مدل در مقالهٔ سال ۱۹۵۶ شکل گرفت و در فصل سال ۱۹۶۷ برای رسانه‌های جمعی گسترش یافت. پس از آن، پیش‌زمینهٔ نظریهٔ کاشت گربنر و پژوهش ادراک رسانه‌ای شد و در آموزش مدل‌های ارتباطی جای گرفت.",
        key_concepts=["رویداد", "ادراک", "گزینش", "بافت", "دسترس‌پذیری", "کنترل", "بازنمایی", "بازتفسیر"],
        theorists="جورج گربنر.",
        theorists_text="مدل در سنت پژوهش ارتباط دیداری-شنیداری و ادراک رسانه شکل گرفت.",
        model="زنجیرهٔ رویداد، ادراک گزینشی، پیام و بازادراک که در هر مرحله با دسترس‌پذیری، گزینش، بافت و کنترل تنظیم می‌شود.",
        studies=[
            "مقالهٔ سال ۱۹۵۶ مدل عمومی ادراکی را معرفی کرد.",
            "فصل سال ۱۹۶۷ کاربرد آن را در رسانه‌های جمعی گسترش داد.",
            "پژوهش‌های بعدی، پیوند آن با نظریهٔ کاشت را بررسی کردند.",
            "ادبیات آموزش ارتباطات، مدل را نمونهٔ گذار به رویکرد شناختی خواند.",
        ],
    ),
    "MC-310": dict(
        year=1970,
        summary="مدل تراکنشی ارتباطات، مدلی در مبانی ارتباطات است که دین بارنلوند در سال ۱۹۷۰ در کتاب مبانی نظریهٔ ارتباطات منتشر کرد. ادعای مرکزی این است که ارتباط فرایندی هم‌زمان، پویا و وابسته به بافت است که در آن معنا نه فرستاده می‌شود و نه دریافت، بلکه میان طرفین خلق و مبادله می‌شود. برخلاف مدل‌های خطی و حتی چرخه‌ای، در مدل تراکنشی هر طرف هم‌زمان فرستنده و گیرنده است و مرز روشنی میان این دو نقش وجود ندارد. بارنلوند سه سطح نشانه را از هم جدا کرد: نشانه‌های خصوصی که در ذهن فرد ساخته می‌شوند، نشانه‌های رفتاری که به بیرون بیان می‌شوند، و نشانه‌های عمومی که در فرهنگ مشترک معنا دارند. ارتباط، هم‌ترازی این سه سطح میان دو نفر است و در بافتی رخ می‌دهد که معنای نشانه‌ها را شکل می‌دهد. این مدل بر پراگماتیسم، نظریهٔ سیستم‌ها و کنش متقابل نمادین استوار است و ارتباط را نه انتقال اطلاعات بلکه هم‌آفرینی معنا می‌بیند. نقدهای اصلی به آن، انتزاعی‌بودن و دشواری عملیاتی‌سازی، فرض تقارن و عاملیت برابر طرفین، کم‌توجهی به ارتباط جمعی و نامتقارنی قدرت، و ابهام مفهومی در تعریف «تراکنش» را برجسته می‌کنند.",
        definition="مدل تراکنشی ارتباطات، ارتباط را فرایندی هم‌زمان و دوسویه می‌داند که در آن هر طرف هم‌زمان فرستنده و گیرنده است و معنا در بافت و تعامل، میان آنان آفریده می‌شود.",
        main_problem="چگونه می‌توان ارتباط انسانی را نه تبادل نوبتی پیام، بلکه فرایندی هم‌زمان و بافتی مدل‌سازی کرد که در آن معنا حاصل هم‌آفرینی طرفین است.",
        mechanism="هر طرف به‌طور هم‌زمان نشانه‌های خصوصی خود را به نشانه‌های رفتاری تبدیل می‌کند، نشانه‌های طرف مقابل را تفسیر می‌کند و بر پایهٔ نشانه‌های عمومی مشترک، معنایی مشترک می‌سازد. بافت، معنا و مسیر تعامل را پیوسته بازتنظیم می‌کند.",
        assumptions=[
            "ارتباط فرایندی هم‌زمان است نه نوبتی.",
            "هر طرف هم‌زمان فرستنده و گیرنده است.",
            "معنا در تعامل آفریده می‌شود نه منتقل.",
            "نشانه‌های خصوصی، رفتاری و عمومی از هم جدا هستند.",
            "بافت، معنای نشانه‌ها را شکل می‌دهد.",
        ],
        principles=[
            "ارتباط را تراکنش هم‌زمان ببین نه تبادل نوبتی.",
            "نقش فرستنده و گیرنده را در هم ادغام کن.",
            "معنا را حاصل هم‌آفرینی بدان.",
            "سه سطح نشانه را در تحلیل جدا کن.",
            "بافت را بخشی از فرایند بدان نه پس‌زمینه.",
            "مدل را برای تعامل رودررو به کار ببر و گسترهٔ آن را نقد کن.",
        ],
        critiques=[
            "مدل انتزاعی است و عملیاتی‌سازی آن دشوار است.",
            "تقارن و عاملیت برابر طرفین را مسلم می‌گیرد.",
            "ارتباط جمعی و نامتقارنی قدرت را پوشش نمی‌دهد.",
            "مفهوم تراکنش در آن ابهام دارد.",
            "شواهد تجربی مستقیم برای مدل محدود است.",
        ],
        critique_text="منتقدان می‌گویند مدل تراکنشی با ادغام نقش‌ها و تأکید بر هم‌آفرینی معنا، تصویری غنی از تعامل انسانی می‌دهد اما انتزاعی می‌ماند و برای ارتباط جمعی و روابط نامتقارن قدرت کارآمد نیست؛ با این حال، چارچوب مرجع ارتباط بین‌فرهنگی و میان‌فردی شد.",
        applications=[
            "تحلیل ارتباط بین‌فرهنگی و سوءبرداشت.",
            "آموزش مهارت گفت‌وگوی هم‌زمان.",
            "مطالعهٔ ارتباط درمانی و مشاوره.",
            "طراحی تعامل هم‌زمان در سامانه‌های گفت‌وگو.",
            "پژوهش هم‌آفرینی معنا در تیم‌های کاری.",
        ],
        example_text="در یک گفت‌وگوی حضوری، هر دو طرف هم‌زمان سخن می‌گویند، حالت چهره می‌خوانند و معنای مشترک می‌سازند؛ معنای نهایی جمله را نمی‌توان تنها به گوینده نسبت داد. مدل تراکنشی همین هم‌آفرینی هم‌زمان را تحلیل می‌کند.",
        evolution="مدل در فصل سال ۱۹۷۰ بارنلوند شکل گرفت و در دهه‌های بعد به چارچوب ارتباط بین‌فرهنگی و میان‌فردی تبدیل شد. در قرن بیست‌ویکم با رشد ارتباط هم‌زمان دیجیتال، بار دیگر برای تحلیل گفت‌وگوی چندکاناله بازخوانی شد.",
        key_concepts=["تراکنش", "هم‌زمانی", "هم‌آفرینی معنا", "نشانهٔ خصوصی", "نشانهٔ رفتاری", "نشانهٔ عمومی", "بافت"],
        theorists="دین بارنلوند.",
        theorists_text="مدل در سنت پراگماتیسم، نظریهٔ سیستم‌ها و کنش متقابل نمادین شکل گرفت.",
        model="تراکنش هم‌زمان دو طرف که هر یک هم‌زمان فرستنده و گیرنده است و با سه سطح نشانه و بافت، معنای مشترک می‌سازند.",
        studies=[
            "فصل سال ۱۹۷۰ مدل تراکنشی را معرفی کرد.",
            "پژوهش‌های بین‌فرهنگی، هم‌آفرینی معنا را با آن تحلیل کردند.",
            "مطالعات مشاوره، تراکنش هم‌زمان را در گفت‌وگوی درمانی به کار گرفتند.",
            "ادبیات ارتباط دیجیتال، مدل را برای تعامل چندکاناله بازخوانی کرد.",
        ],
    ),
    "MC-319": dict(
        year=1986,
        summary="مدل احتمال تفصیل، مدل دومسیرهٔ اقناع است که ریچارد پتی و جان کاسیوپو در سال ۱۹۸۶ در مجموعهٔ روان‌شناسی اجتماعی آزمایشی صورت‌بندی کردند. ادعای مرکزی این است که اقناع در امتداد یک پیوستار تفصیل رخ می‌دهد و بسته به میزان اندیشیدن مخاطب به پیام، یکی از دو مسیر غالب می‌شود. در مسیر مرکزی، مخاطب با انگیزه و توان کافی، استدلال‌ها را بررسی و ارزیابی می‌کند و تغییر نگرش پایدارتر و مقاوم‌تر در برابر ضدپیام تولید می‌شود. در مسیر پیرامونی، مخاطب با انگیزه یا توان کم، به نشانه‌های سطحی مانند جذابیت گوینده، اعتبار منبع، شمار استدلال‌ها یا احساس گذرا تکیه می‌کند و تغییر نگرش موقت و شکننده است. انگیزش با عواملی مانند درگیری شخصی و نیاز به شناخت و توان با عواملی مانند حواس‌پرتی و دانش پیشین سنجیده می‌شود. مدل میان تفصیل عینی و سوگیرانه نیز تمایز می‌گذارد: مخاطب می‌تواند استدلال‌ها را بی‌طرفانه ارزیابی کند یا با سوگیری به نفع موضع پیشین خود بپردازد. این مدل، چارچوب پژوهش تبلیغات، ارتباط سلامت و کمپین‌های سیاسی شد. نقدهای اصلی به آن، دشواری سنجش مسیر و تفصیل، ناهمگونی یافته‌های آزمایشگاهی و میدانی، تکثیر تعدیل‌گرها و ابهام مرز دو مسیر را برجسته می‌کنند.",
        definition="مدل احتمال تفصیل، اقناع را در دو مسیر مرکزی و پیرامونی مدل‌سازی می‌کند و تعیین‌کنندهٔ مسیر را میزان انگیزه و توان مخاطب برای اندیشیدن به استدلال‌های پیام می‌داند.",
        main_problem="چرا برخی پیام‌ها نگرش را پایدار و مقاوم تغییر می‌دهند و برخی دیگر تنها اثرهای گذرا می‌گذارند، و چه عواملی تعیین می‌کنند مخاطب استدلال را جدی بگیرد یا به نشانه‌های سطحی تکیه کند.",
        mechanism="اگر انگیزه و توان مخاطب بالا باشد، تفصیل استدلال‌ها رخ می‌دهد و کیفیت استدلال تعیین‌کنندهٔ نگرش می‌شود؛ اگر پایین باشد، نشانه‌های پیرامونی جای استدلال را می‌گیرند. نتیجهٔ مسیر مرکزی پایدارتر و مقاوم‌تر است.",
        assumptions=[
            "اقناع در پیوستاری از تفصیل کم تا زیاد رخ می‌دهد.",
            "انگیزه و توان، مسیر غالب را تعیین می‌کنند.",
            "نگرش ساخته‌شده در مسیر مرکزی پایدارتر است.",
            "نشانه‌های پیرامونی در تفصیل کم اثر می‌گذارند.",
            "تفصیل می‌تواند عینی یا سوگیرانه باشد.",
        ],
        principles=[
            "مسیر اقناع را با انگیزه و توان مخاطب تعیین کن.",
            "کیفیت استدلال را در مسیر مرکزی برجسته کن.",
            "نشانه‌های پیرامونی را برای مخاطب کم‌درگیر به کار ببر.",
            "پایداری نگرش را پیامد مسیر مرکزی بدان.",
            "تفصیل عینی و سوگیرانه را از هم جدا کن.",
            "سنجش مسیر را با شواهد فرایندی انجام بده.",
        ],
        critiques=[
            "سنجش مسیر و میزان تفصیل دشوار است.",
            "یافته‌های آزمایشگاهی و میدانی ناهمگون‌اند.",
            "تعدیل‌گرهای مدل به‌طور بی‌پایان تکثیر شده‌اند.",
            "مرز دو مسیر در عمل مبهم است.",
            "اثرهای اندازه‌گیری‌شده اغلب کوچک‌اند.",
        ],
        critique_text="منتقدان می‌گویند مدل احتمال تفصیل چارچوبی نیرومند برای سازمان‌دهی پژوهش اقناع فراهم کرد اما سنجش مستقل مسیرها و تفصیل دشوار است و تعدیل‌گرهای فراوان، آزمون‌پذیری آن را کاهش می‌دهند؛ با این حال، همچنان پرنفوذترین مدل دومسیره است.",
        applications=[
            "طراحی پیام تبلیغات و بازاریابی.",
            "کمپین‌های سلامت و تغییر رفتار.",
            "تحلیل اقناع سیاسی و مناظره.",
            "آموزش سواد رسانه‌ای و تشخیص نشانه‌های سطحی.",
            "طراحی پیام متناسب با درگیری مخاطب.",
        ],
        example_text="برای مخاطبی که دربارهٔ خرید لپ‌تاپ درگیر است، مقایسهٔ فنی پردازنده و گارانتی در مسیر مرکزی اثر می‌گذارد؛ برای مخاطبی بی‌تفاوت، چهرهٔ مشهور تبلیغ در مسیر پیرامونی تصمیم را جهت می‌دهد. مدل احتمال تفصیل همین تفاوت را توضیح می‌دهد.",
        evolution="مدل در مقالهٔ سال ۱۹۸۶ پتی و کاسیوپو تثبیت شد و بر پایهٔ آزمایش‌های درگیری شخصی سال ۱۹۸۱ استوار بود. در دهه‌های بعد به چارچوب مرجع اقناع در روان‌شناسی اجتماعی، ارتباط سلامت و بازاریابی تبدیل شد و نسخه‌های گسترده‌ای مانند مدل یکپارچهٔ اقناع از آن زاده شد.",
        key_concepts=["مسیر مرکزی", "مسیر پیرامونی", "تفصیل", "انگیزه", "توان", "درگیری شخصی", "نیاز به شناخت", "نشانهٔ پیرامونی"],
        theorists="ریچارد پتی و جان کاسیوپو.",
        theorists_text="مدل در سنت روان‌شناسی اجتماعی اقناع و پژوهش تغییر نگرش شکل گرفت.",
        model="پیوستار تفصیل با دو سرِ مسیر مرکزی و پیرامونی که انگیزه و توان مخاطب، مسیر و پایداری نگرش را تعیین می‌کند.",
        studies=[
            "آزمایش سال ۱۹۸۱ نقش درگیری شخصی را نشان داد.",
            "مقالهٔ سال ۱۹۸۶ مدل دومسیره را صورت‌بندی کرد.",
            "پژوهش‌های سلامت، پیام‌های مرکزی و پیرامونی را مقایسه کردند.",
            "مرورهای بعدی، تعدیل‌گرها و محدودیت‌های مدل را ارزیابی کردند.",
        ],
    ),
    "MC-320": dict(
        year=1980,
        summary="مدل پردازش نظام‌مند-اکتشافی، مدلی در روان‌شناسی اقناع است که شلی چایکن آن را در سال ۱۹۸۰ در مجلهٔ روان‌شناسی شخصیت و اجتماعی معرفی کرد. ادعای مرکزی این است که دو شیوهٔ پردازش پیام اقناعی می‌توانند هم‌زمان جریان داشته باشند: پردازش نظام‌مند که بر بررسی تحلیلی و جامع استدلال‌ها استوار است و پردازش اکتشافی که بر میانبرهای ذهنی ساده مانند «متخصصان راست می‌گویند» یا «اکثریت درست می‌گویند» تکیه می‌کند. برخلاف مدل‌هایی که این دو را دو سر یک پیوستار می‌دانند، چایکن بر هم‌زمانی و تعامل آن‌ها تأکید کرد. مدل بر اصل صرفه‌جویی شناختی و اصل کفایت استوار است: فرد تا حدی پردازش می‌کند که برای قضاوت مطمئن کافی باشد. وقتی اعتبار منبع بالا و ابهام استدلال کم باشد، نشانهٔ اکتشافی می‌تواند کافی تلقی شود؛ اما وقتی موضوع مهم یا استدلال مبهم باشد، پردازش نظام‌مند غالب می‌شود. پژوهش سال ۱۹۹۴ نشان داد پردازش اکتشافی می‌تواند پردازش نظام‌مند را سوگیرانه کند و اثر اعتبار منبع بر قضاوت را در شرایط ابهام تقویت نماید. نقدهای اصلی به مدل، دشواری تفکیک تجربی دو شیوه، ابهام معیار کفایت، کم‌توجهی به احساس و انگیزهٔ ضمنی، و تعمیم محدود یافته‌های آزمایشگاهی را برجسته می‌کنند.",
        definition="مدل پردازش نظام‌مند-اکتشافی، دو شیوهٔ هم‌زمان پردازش پیام را از هم جدا می‌کند: بررسی تحلیلی استدلال‌ها و تکیه بر میانبرهای ذهنی، و تعامل آن‌ها را بر پایهٔ اصل کفایت توضیح می‌دهد.",
        main_problem="چگونه افراد در اقناع، میان بررسی دقیق استدلال‌ها و تکیه بر میانبرهای ذهنی جابه‌جا می‌شوند و چه زمانی این دو شیوه هم‌زمان یا در تعارض با یکدیگر عمل می‌کنند.",
        mechanism="فرد تا حدی پردازش می‌کند که برای قضاوت مطمئن کافی باشد؛ نشانه‌های اکتشافی در شرایط کم‌ابهام و اعتبار بالا کافی تلقی می‌شوند، اما ابهام یا اهمیت موضوع، پردازش نظام‌مند را فعال می‌کند. دو شیوه می‌توانند جمع شوند یا یکی دیگری را سوگیرانه کند.",
        assumptions=[
            "دو شیوهٔ پردازش می‌توانند هم‌زمان فعال باشند.",
            "افراد بر پایهٔ اصل صرفه‌جویی شناختی عمل می‌کنند.",
            "معیار کفایت، میزان پردازش لازم را تعیین می‌کند.",
            "نشانه‌های اکتشافی از تجربه و فرهنگ می‌آیند.",
            "پردازش اکتشافی می‌تواند نظام‌مند را سوگیرانه کند.",
        ],
        principles=[
            "دو شیوهٔ پردازش را هم‌زمان در نظر بگیر.",
            "کفایت ادراک‌شده را معیار توقف پردازش بدان.",
            "نشانه‌های اکتشافی را در بافت فرهنگی تحلیل کن.",
            "ابهام و اهمیت موضوع را تعدیل‌گر بدان.",
            "اثر سوگیرانهٔ اکتشافی بر نظام‌مند را بسنج.",
            "مدل را برای پیام‌های چندنشانه‌ای به کار ببر.",
        ],
        critiques=[
            "تفکیک تجربی دو شیوه دشوار است.",
            "معیار کفایت مبهم و سنجش‌ناپذیر می‌ماند.",
            "احساس و انگیزهٔ ضمنی کم‌بررسی می‌شود.",
            "یافته‌ها بیشتر آزمایشگاهی و محدودند.",
            "مرز هم‌زمانی و توالی دو شیوه روشن نیست.",
        ],
        critique_text="منتقدان می‌گویند مدل چایکن با پذیرش هم‌زمانی دو شیوه، تصویری واقع‌گرایانه‌تر از اقناع داد اما تفکیک تجربی آن‌ها و سنجش کفایت دشوار است و نقش احساس را کم‌رنگ می‌کند؛ با این حال، چارچوبی نیرومند برای تحلیل تعامل نشانه و استدلال فراهم کرد.",
        applications=[
            "تحلیل اثر اعتبار منبع در تبلیغات.",
            "طراحی پیام سلامت با نشانه‌های روشن.",
            "پژوهش سوگیری در قضاوت مصرف‌کننده.",
            "آموزش تفکر انتقادی و تشخیص میانبر ذهنی.",
            "طراحی رابط کاربری با نشانه‌های اعتماد.",
        ],
        example_text="کاربری که در یک وبگاه خرید با نشان اعتبار و نظرات فراوان روبه‌رو می‌شود، ممکن است با میانبر «دیگران درست می‌گویند» تصمیم بگیرد؛ اما اگر مبلغ خرید بالا و مشخصات مبهم باشد، به بررسی نظام‌مند جزئیات می‌پردازد. مدل چایکن همین جابه‌جایی را توضیح می‌دهد.",
        evolution="مدل در مقالهٔ سال ۱۹۸۰ چایکن شکل گرفت و با پژوهش سال ۱۹۹۴ دربارهٔ اثر سوگیرانهٔ پردازش اکتشافی گسترش یافت. پس از آن، به چارچوب مرجع پژوهش اقناع، تصمیم مصرف‌کننده و ارتباط سلامت تبدیل شد و در برابر مدل‌های دومسیرهٔ رقیب جایگاه خود را حفظ کرد.",
        key_concepts=["پردازش نظام‌مند", "پردازش اکتشافی", "اصل کفایت", "صرفه‌جویی شناختی", "نشانهٔ اکتشافی", "اعتبار منبع", "سوگیری"],
        theorists="شلی چایکن.",
        theorists_text="مدل در سنت روان‌شناسی اجتماعی اقناع و شناخت اجتماعی شکل گرفت.",
        model="دو شیوهٔ هم‌زمان پردازش نظام‌مند و اکتشافی که بر پایهٔ اصل کفایت، بسته به ابهام و اهمیت موضوع، جمع یا یکدیگر را سوگیرانه می‌کنند.",
        studies=[
            "مقالهٔ سال ۱۹۸۰ دو شیوهٔ پردازش و نقش نشانه‌های منبع را نشان داد.",
            "پژوهش سال ۱۹۹۴ اثر سوگیرانهٔ اکتشافی بر نظام‌مند را آزمود.",
            "مطالعات سلامت، نشانه‌های اعتماد را در پیام تحلیل کردند.",
            "مرورهای بعدی، هم‌زمانی و محدودیت‌های مدل را ارزیابی کردند.",
        ],
    ),
}

NAME_FIX = {}
YEAR_FIX = {"MC-309": "سال مدل اصلی ۱۹۵۶ است؛ تاریخ ۱۹۶۷ در کارت به فصل گسترش‌یافتهٔ گربنر برای رسانه‌های جمعی اشاره دارد."}


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
                                       "verified": n_verified, "batch": 140}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH140 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
