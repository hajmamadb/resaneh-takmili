# -*- coding: utf-8 -*-
"""Batch 131 (MODEL): full documentation for MC-069, MC-081, MC-082, MC-106."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch131-model-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch131_model.json"

S = {
    "MC-069": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Balanced Scorecard—Measures That Drive Performance",
             title_fa="کارت امتیازی متوازن: سنجه‌هایی که عملکرد را پیش می‌برند",
             authors="Kaplan, R. S.; Norton, D. P.", year=1992,
             publisher="Harvard Business Review",
             doi=None,
             url="https://hbr.org/1992/01/the-balanced-scorecard-measures-that-drive-performance-2",
             language="en", isbn=None,
             citation="Kaplan, R. S., & Norton, D. P. (1992). The balanced scorecard—Measures that drive performance. Harvard Business Review, 70(1), 71-79.",
             locator="70(1):71-79", locator_type="page_range",
             supports="four-perspective performance measurement framework", verified=True),
        dict(kind="BOOK",
             title_en="The Balanced Scorecard: Translating Strategy into Action",
             title_fa="کارت امتیازی متوازن: ترجمهٔ راهبرد به عمل",
             authors="Kaplan, R. S.; Norton, D. P.", year=1996,
             publisher="Harvard Business School Press",
             doi=None, url=None, language="en", isbn=None,
             citation="Kaplan, R. S., & Norton, D. P. (1996). The Balanced Scorecard: Translating Strategy into Action. Boston: Harvard Business School Press.",
             locator="book", locator_type="SECTION",
             supports="strategy-map and implementation version of the scorecard", verified=False),
    ],
    "MC-081": [
        dict(kind="BOOK_CHAPTER",
             title_en="The Structure and Function of Communication in Society",
             title_fa="ساختار و کارکرد ارتباطات در جامعه",
             authors="Lasswell, H. D.", year=1948,
             publisher="Harper & Brothers (The Communication of Ideas)",
             doi=None,
             url="http://www.irfanerdogan.com/dergiweb2008/24/12.pdf",
             language="en", isbn=None,
             citation="Lasswell, H. D. (1948). The structure and function of communication in society. In L. Bryson (Ed.), The Communication of Ideas (pp. 37-51). New York: Harper & Brothers.",
             locator="pp. 37-51", locator_type="page_range",
             supports="5W model and three social functions of communication", verified=True),
        dict(kind="BOOK",
             title_en="Propaganda Technique in the World War",
             title_fa="فن تبلیغات در جنگ جهانی",
             authors="Lasswell, H. D.", year=1927,
             publisher="Alfred A. Knopf",
             doi=None, url=None, language="en", isbn=None,
             citation="Lasswell, H. D. (1927). Propaganda Technique in the World War. New York: Alfred A. Knopf.",
             locator="book", locator_type="SECTION",
             supports="early propaganda-analysis background of the 5W framework", verified=False),
    ],
    "MC-082": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="A Mathematical Theory of Communication",
             title_fa="نظریهٔ ریاضی ارتباطات",
             authors="Shannon, C. E.", year=1948,
             publisher="Bell System Technical Journal",
             doi="10.1002/j.1538-7305.1948.tb01338.x",
             url="https://onlinelibrary.wiley.com/doi/abs/10.1002/j.1538-7305.1948.tb01338.x",
             language="en", isbn=None,
             citation="Shannon, C. E. (1948). A mathematical theory of communication. Bell System Technical Journal, 27(3), 379-423; 27(4), 623-656.",
             locator="27:379-423, 623-656", locator_type="page_range",
             supports="source-transmitter-channel-receiver model and information entropy", verified=True),
        dict(kind="BOOK",
             title_en="The Mathematical Theory of Communication",
             title_fa="نظریهٔ ریاضی ارتباطات",
             authors="Shannon, C. E.; Weaver, W.", year=1949,
             publisher="University of Illinois Press",
             doi=None, url=None, language="en", isbn=None,
             citation="Shannon, C. E., & Weaver, W. (1949). The Mathematical Theory of Communication. Urbana: University of Illinois Press.",
             locator="book", locator_type="SECTION",
             supports="Weaver's three levels: technical, semantic, effectiveness", verified=False),
    ],
    "MC-106": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Human Aggression",
             title_fa="پرخاشگری انسانی",
             authors="Anderson, C. A.; Bushman, B. J.", year=2002,
             publisher="Annual Review of Psychology",
             doi="10.1146/annurev.psych.53.100901.135231",
             url="https://psycnet.apa.org/record/2001-09759-002",
             language="en", isbn=None,
             citation="Anderson, C. A., & Bushman, B. J. (2002). Human aggression. Annual Review of Psychology, 53, 27-51.",
             locator="53:27-51", locator_type="page_range",
             supports="general aggression model integrating person and situation inputs", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Video Games and Aggressive Thoughts, Feelings, and Behavior in the Laboratory and in Life",
             title_fa="بازی‌های ویدئویی و افکار، احساسات و رفتار پرخاشگرانه در آزمایشگاه و زندگی",
             authors="Anderson, C. A.; Dill, K. E.", year=2000,
             publisher="Journal of Personality and Social Psychology",
             doi="10.1037/0022-3514.78.4.772",
             url=None, language="en", isbn=None,
             citation="Anderson, C. A., & Dill, K. E. (2000). Video games and aggressive thoughts, feelings, and behavior in the laboratory and in life. Journal of Personality and Social Psychology, 78(4), 772-790.",
             locator="78(4):772-790", locator_type="page_range",
             supports="empirical background on violent-game exposure and aggression", verified=False),
    ],
}

ENRICH = {
    "MC-069": dict(
        year=1992,
        summary="کارت امتیازی متوازن، چارچوبی برای سنجش عملکرد و اجرای راهبرد است که رابرت کاپلان و دیوید نورتون در مقالهٔ سال ۱۹۹۲ در هاروارد بیزینس ریویو معرفی کردند و در کتاب سال ۱۹۹۶ آن را به ابزار اجرای راهبرد بدل ساختند. ادعای مرکزی این است که ارزیابی سازمان تنها با شاخص‌های مالی کافی نیست، زیرا این شاخص‌ها گذشته را گزارش می‌کنند و نشانه‌های آینده را نمی‌بینند. چارچوب، چهار دیدگاه را به هم پیوند می‌دهد: مالی، مشتری، فرایندهای داخلی، و یادگیری و رشد؛ و میان سنجه‌های پیشرو و پسرو تمایز می‌گذارد تا مدیران زنجیرهٔ علّی راهبرد را در قالب نقشهٔ راهبرد ببینند. در نسخهٔ بعدی، کارت امتیازی به ابزار ارتباط راهبرد در سراسر سازمان تبدیل شد. در مدیریت رسانه، این چارچوب برای متوازن‌کردن فشار مالی با کیفیت محتوا، رضایت مخاطب و نوآوری به کار رفته است. نقدهای اصلی به آن، استفادهٔ مکانیکی و تشریفاتی، ضعف شواهد تجربی دربارهٔ رابطهٔ علّی سنجه‌ها و دشواری سنجش سرمایهٔ انسانی و نوآوری مربوط می‌شود.",
        definition="کارت امتیازی متوازن، چارچوبی است که عملکرد سازمان را در چهار دیدگاه مالی، مشتری، فرایندهای داخلی و یادگیری و رشد می‌سنجد و سنجه‌های پیشرو را به نتایج مالی پیوند می‌دهد.",
        main_problem="چگونه می‌توان عملکرد سازمان را فراتر از شاخص‌های مالی سنجید و راهبرد را به سنجه‌های قابل پیگیری و علت‌ومعلولی ترجمه کرد.",
        mechanism="هر دیدگاه مجموعه‌ای از اهداف و سنجه‌ها دارد؛ بهبود در یادگیری و رشد، فرایندهای داخلی را بهتر می‌کند، این بهبود به رضایت مشتری می‌انجامد و در نهایت در نتیجهٔ مالی بازتاب می‌یابد. نقشهٔ راهبرد این زنجیرهٔ علّی را صریح می‌کند و سنجه‌های پیشرو هشدار زودهنگام می‌دهند.",
        assumptions=[
            "شاخص‌های مالی به‌تنهایی تصویر کامل عملکرد را نمی‌دهند.",
            "بین چهار دیدگاه رابطهٔ علّی قابل شناسایی وجود دارد.",
            "سنجه‌های پیشرو را می‌توان پیش از نتایج مالی رصد کرد.",
            "راهبرد را می‌توان به سنجه‌های قابل اندازه‌گیری ترجمه کرد.",
            "توازن میان دیدگاه‌ها از تمرکز افراطی بر کوتاه‌مدت جلوگیری می‌کند.",
        ],
        principles=[
            "عملکرد را باید در چهار دیدگاه متوازن سنجید.",
            "سنجه‌های پیشرو و پسرو باید از هم تفکیک شوند.",
            "راهبرد باید در قالب نقشهٔ علّی بیان شود.",
            "سنجه‌ها باید به راهبرد و نه به آسانی اندازه‌گیری وابسته باشند.",
            "یادگیری و رشد، پایهٔ بهبود بلندمدت است.",
            "ارتباط راهبرد در سراسر سازمان، بخشی از کارکرد چارچوب است.",
        ],
        critiques=[
            "در عمل اغلب به فهرستی تشریفاتی از شاخص‌ها تبدیل می‌شود.",
            "شواهد تجربی دربارهٔ رابطهٔ علّی دیدگاه‌ها ضعیف است.",
            "سنجش سرمایهٔ انسانی و نوآوری دشوار و اغلب کیفی است.",
            "می‌تواند بار گزارش‌دهی و بوروکراسی را افزایش دهد.",
            "در محیط‌های پلتفرمی سریع، ممکن است کهنه شود.",
        ],
        critique_text="منتقدان می‌گویند کارت امتیازی متوازن چارچوبی مفید برای متوازن‌کردن سنجه‌ها و ارتباط راهبرد فراهم کرد اما در بسیاری از سازمان‌ها به آیین تشریفاتی تبدیل شد و شواهد روشنی برای زنجیرهٔ علّی مفروض آن وجود ندارد. با این حال، همچنان یکی از پرکاربردترین چارچوب‌های مدیریت عملکرد است.",
        applications=[
            "سنجش عملکرد سازمان‌های رسانه‌ای با توازن مالی و کیفیت محتوا.",
            "ترجمهٔ راهبرد سازمان به سنجه‌های قابل پیگیری.",
            "طراحی داشبورد مدیریتی و گزارش به هیئت‌مدیره.",
            "ارزیابی سرمایه‌گذاری در آموزش و نوآوری.",
            "آموزش مدیریت راهبردی و عملکرد.",
        ],
        example_text="یک سازمان رسانه‌ای ممکن است در دیدگاه مالی کاهش هزینه را هدف بگیرد، اما کارت امتیازی نشان می‌دهد که کاهش سرمایه‌گذاری در آموزش خبرنگاران، کیفیت محتوا و در نتیجه رضایت مخاطب را کم می‌کند و در میان‌مدت به درآمد آسیب می‌زند. نقشهٔ راهبرد این زنجیره را پیش از افت مالی آشکار می‌کند.",
        evolution="مقالهٔ سال ۱۹۹۲ چارچوب چهار دیدگاه را معرفی کرد؛ کتاب سال ۱۹۹۶ آن را به ابزار اجرای راهبرد و نقشهٔ راهبرد گسترد. در دههٔ ۲۰۰۰ چارچوب به بخش عمومی و سازمان‌های غیرانتفاعی راه یافت و نقدهای تجربی دربارهٔ کارایی آن شکل گرفت.",
        key_concepts=["چهار دیدگاه", "سنجهٔ پیشرو", "سنجهٔ پسرو", "نقشهٔ راهبرد", "یادگیری و رشد", "توازن سنجه‌ها"],
        theorists="رابرت کاپلان و دیوید نورتون، سازندگان کارت امتیازی متوازن.",
        theorists_text="این چارچوب در سنت حسابداری مدیریت و مدیریت راهبردی شکل گرفت و با اجرای راهبرد پیوند خورد.",
        model="مدل چهار دیدگاه: مالی، مشتری، فرایندهای داخلی و یادگیری و رشد؛ زنجیرهٔ علّی از یادگیری تا نتیجهٔ مالی، با سنجه‌های پیشرو و پسرو در هر دیدگاه.",
        studies=[
            "مقالهٔ سال ۱۹۹۲ چارچوب را با نمونه‌های سازمانی معرفی کرد.",
            "کتاب سال ۱۹۹۶ نقشهٔ راهبرد و اجرای راهبردی را افزود.",
            "مطالعات بعدی، کاربرد و محدودیت‌های چارچوب را ارزیابی کردند.",
            "پژوهش مدیریت رسانه، چارچوب را برای سازمان‌های رسانه‌ای به کار برد.",
        ],
    ),
    "MC-081": dict(
        year=1948,
        summary="مدل لاسول، یکی از بنیادی‌ترین مدل‌های ارتباطات است که هارولد لاسول آن را در مقالهٔ ساختار و کارکرد ارتباطات در جامعه در سال ۱۹۴۸ در کتاب ارتباط اندیشه‌ها به ویراستاری لایمن برایسون منتشر کرد. ادعای مرکزی این است که هر کنش ارتباطی را می‌توان با پنج پرسش تحلیل کرد: چه کسی، چه چیزی را، از چه کانالی، به چه کسی، با چه اثری می‌گوید. هر پرسش یک حوزهٔ پژوهشی را مشخص می‌کند: تحلیل کنترل (چه کسی)، تحلیل محتوا (چه چیزی)، تحلیل رسانه (چه کانالی)، تحلیل مخاطب (به چه کسی) و تحلیل اثر (با چه اثری). لاسول همچنین سه کارکرد اجتماعی ارتباطات را برشمرد: نظارت بر محیط، همبستگی اجزای جامعه در پاسخ به محیط، و انتقال میراث اجتماعی از نسلی به نسل دیگر. این مدل، چارچوب پایهٔ پژوهش ارتباطات، تحلیل تبلیغات و سیاست‌گذاری ارتباطی شد. نقدهای اصلی به آن، خطی و یک‌سویه‌بودن، غفلت از بازخورد و تعامل، تمرکز بر قصد فرستنده و بی‌توجهی به ساختار معنایی و قدرت در ارتباط مربوط می‌شود.",
        definition="مدل لاسول، مدل پنج‌پرسشی ارتباط است که هر کنش ارتباطی را با پرسش‌های چه کسی، چه چیزی، از چه کانالی، به چه کسی و با چه اثری تحلیل می‌کند و سه کارکرد نظارت، همبستگی و انتقال میراث را برای ارتباطات اجتماعی تعریف می‌کند.",
        main_problem="چگونه می‌توان کنش‌های ارتباطی را به‌طور نظام‌مند تحلیل کرد و حوزه‌های پژوهشی ارتباطات را از یکدیگر تفکیک نمود.",
        mechanism="هر کنش ارتباطی از پنج مؤلفهٔ قابل تفکیک ساخته می‌شود؛ تحلیل هر مؤلفه، پرسشی مستقل و روش پژوهشی متناظر دارد. کارکردهای سه‌گانه نیز نشان می‌دهند ارتباط اجتماعی چه نقشی در بقا و تداوم جامعه ایفا می‌کند.",
        assumptions=[
            "ارتباط را می‌توان به مؤلفه‌های قابل تفکیک تجزیه کرد.",
            "هر مؤلفهٔ ارتباطی، حوزهٔ پژوهشی مستقلی دارد.",
            "ارتباط، کارکردی اجتماعی برای بقا و تداوم جامعه دارد.",
            "قصد فرستنده، محور تحلیل ارتباط است.",
            "اثر ارتباط را می‌توان جدا از فرایند معناسازی سنجید.",
        ],
        principles=[
            "تحلیل ارتباط با پنج پرسش بنیادی آغاز می‌شود.",
            "هر پرسش به حوزهٔ پژوهشی متناظر اشاره دارد.",
            "ارتباطات سه کارکرد نظارت، همبستگی و انتقال میراث دارد.",
            "تحلیل کنترل، محتوا، رسانه، مخاطب و اثر باید جدا بررسی شوند.",
            "مدل، چارچوبی برای مطالعهٔ تبلیغات و سیاست است.",
            "کارکردهای ارتباطی، پیوند ارتباط و ساختار اجتماعی را نشان می‌دهند.",
        ],
        critiques=[
            "مدل خطی و یک‌سویه است و بازخورد را نادیده می‌گیرد.",
            "تعامل و مذاکرهٔ معنا در آن جای ندارد.",
            "بر قصد فرستنده و اثر تمرکز دارد.",
            "نقش قدرت و نابرابری در ارتباط را کم‌رنگ می‌کند.",
            "برای ارتباطات دیجیتال و شبکه‌ای کافی نیست.",
        ],
        critique_text="منتقدان می‌گویند مدل لاسول چارچوبی روشن و کاربردی برای تقسیم حوزه‌های پژوهش ارتباطات فراهم کرد اما ارتباط را خطی و بدون بازخورد می‌بیند و فرایند تعاملی معناسازی را نادیده می‌گیرد. با این حال، همچنان نقطهٔ شروع آموزش ارتباطات و تحلیل محتوا است.",
        applications=[
            "تحلیل محتوای پیام‌های رسانه‌ای.",
            "تحلیل تبلیغات و کمپین‌های ارتباطی.",
            "آموزش مقدماتی نظریه‌های ارتباطات.",
            "طراحی پژوهش مخاطب و اثر.",
            "تحلیل سیاست ارتباطی و کنترل رسانه.",
        ],
        example_text="در تحلیل یک کمپین انتخاباتی، پژوهشگر با مدل لاسول می‌پرسد چه کسی پیام را فرستاده، محتوای پیام چیست، از چه کانالی منتشر شده، مخاطب آن کیست و چه اثری داشته است؛ هر پرسش به یک بخش مستقل از پژوهش تبدیل می‌شود. مدل لاسول همین تقسیم کار را ممکن می‌کند.",
        evolution="ریشهٔ مدل در پژوهش تبلیغات و تحلیل پروپاگاندا در دههٔ ۱۹۲۰ و ۱۹۳۰ است. مقالهٔ سال ۱۹۴۸ آن را به چارچوب پایهٔ ارتباطات تبدیل کرد و در دههٔ ۱۹۵۰ با افزودن بازخورد و تفسیر، نقد و بسط یافت.",
        key_concepts=["پنج پرسش", "تحلیل کنترل", "تحلیل محتوا", "تحلیل رسانه", "تحلیل مخاطب", "تحلیل اثر", "کارکردهای ارتباطات"],
        theorists="هارولد لاسول، سازندهٔ مدل؛ و چارلز رایت که کارکردهای ارتباطات را بسط داد.",
        theorists_text="این مدل در سنت پژوهش پروپاگاندا و جامعه‌شناسی ارتباطات شکل گرفت و به چارچوب پایهٔ آموزش ارتباطات تبدیل شد.",
        model="مدل پنج‌مؤلفه‌ای: فرستنده، پیام، کانال، گیرنده و اثر؛ با سه کارکرد اجتماعی نظارت، همبستگی و انتقال میراث.",
        studies=[
            "مقالهٔ سال ۱۹۴۸ مدل پنج پرسش و کارکردهای سه‌گانه را معرفی کرد.",
            "پژوهش‌های تحلیل محتوا، مدل را به‌عنوان چارچوب پایه به کار بردند.",
            "نقدهای دههٔ ۱۹۵۰ بازخورد و تفسیر را به مدل افزودند.",
            "آموزش ارتباطات، مدل را به چارچوب مقدماتی استاندارد تبدیل کرد.",
        ],
    ),
    "MC-082": dict(
        year=1948,
        summary="مدل ریاضی ارتباط، مدلی مهندسی برای انتقال اطلاعات است که کلود شانون در مقالهٔ نظریهٔ ریاضی ارتباطات در سال ۱۹۴۸ در مجلهٔ فنی سیستم بل منتشر کرد و در کتاب سال ۱۹۴۹ با وارن ویور بازنشر شد. ادعای مرکزی این است که ارتباط را می‌توان زنجیره‌ای از منبع اطلاعات، فرستنده، کانال، گیرنده و مقصد دید که در آن نویز می‌تواند سیگنال را مخدوش کند؛ هدف، انتقال دقیق و کارآمد پیام با کمترین خطاست. شانون مفهوم آنتروپی اطلاعات و ظرفیت کانال را صورت‌بندی کرد و پایهٔ نظریهٔ اطلاعات را گذاشت. ویور در مقدمهٔ کتاب، سه سطح مسئله را از هم جدا کرد: سطح فنی (دقت انتقال نمادها)، سطح معنایی (دقت انتقال معنا) و سطح اثربخشی (تأثیر بر رفتار). این مدل پایهٔ فناوری ارتباطات دیجیتال، فشرده‌سازی داده و طراحی شبکه شد و در ارتباطات اجتماعی نیز به‌عنوان مدل انتقالی پایه به کار رفت. نقدهای اصلی به آن، بی‌توجهی به معنا و تعامل، خطی و یک‌سویه‌بودن، و نامناسب‌بودن برای تحلیل ارتباط انسانی و اجتماعی مربوط می‌شود.",
        definition="مدل ریاضی ارتباط، مدلی است که ارتباط را به‌عنوان انتقال سیگنال از منبع به مقصد از طریق فرستنده و کانال و با امکان اختلال نویز توصیف می‌کند و سه سطح فنی، معنایی و اثربخشی را از هم جدا می‌کند.",
        main_problem="چگونه می‌توان اطلاعات را با کمترین خطا و بیشترین کارآمدی از یک نقطه به نقطهٔ دیگر منتقل کرد، و اختلال کانال چه محدودیتی بر ظرفیت انتقال می‌گذارد.",
        mechanism="منبع، پیام را تولید می‌کند؛ فرستنده آن را به سیگنال تبدیل می‌کند؛ کانال سیگنال را منتقل می‌کند و نویز آن را مخدوش می‌سازد؛ گیرنده سیگنال را به پیام بازمی‌گرداند و مقصد آن را دریافت می‌کند. ظرفیت کانال، سقف نرخ انتقال بی‌خطا را تعیین می‌کند.",
        assumptions=[
            "اطلاعات را می‌توان به‌صورت کمّی و ریاضی اندازه گرفت.",
            "کانال، ظرفیت محدود و قابل محاسبه دارد.",
            "نویز، اختلالی تصادفی و قابل مدل‌سازی است.",
            "مسئلهٔ فنی انتقال را می‌توان از مسئلهٔ معنایی جدا کرد.",
            "هدف، بازتولید دقیق پیام در مقصد است.",
        ],
        principles=[
            "ارتباط را می‌توان زنجیرهٔ منبع تا مقصد تحلیل کرد.",
            "آنتروپی، معیار کمّی اطلاعات است.",
            "ظرفیت کانال، سقف انتقال بی‌خطا را تعیین می‌کند.",
            "نویز را می‌توان مدل و در صورت امکان جبران کرد.",
            "سه سطح فنی، معنایی و اثربخشی باید از هم تفکیک شوند.",
            "کارآمدی انتقال، هدف اصلی مدل است.",
        ],
        critiques=[
            "مدل معنا و تفسیر انسانی را نادیده می‌گیرد.",
            "ارتباط را خطی و بدون بازخورد می‌بیند.",
            "برای ارتباط اجتماعی و تعاملی مناسب نیست.",
            "گیرنده را منفعل و تنها بازگردانندهٔ پیام می‌بیند.",
            "نقش بافت و قدرت در ارتباط را پوشش نمی‌دهد.",
        ],
        critique_text="منتقدان می‌گویند مدل ریاضی ارتباط برای مسئلهٔ مهندسی انتقال بسیار موفق بود اما به‌عنوان مدل ارتباط انسانی ناقص است، زیرا معنا، تعامل و بافت را نادیده می‌گیرد. با این حال، مفاهیم آنتروپی و ظرفیت کانال، پایهٔ فناوری اطلاعات مدرن شد.",
        applications=[
            "طراحی شبکه‌های ارتباطی و مخابراتی.",
            "فشرده‌سازی و رمزگذاری داده.",
            "تحلیل خطا و نویز در انتقال پیام.",
            "آموزش مقدماتی مدل‌های انتقالی ارتباط.",
            "مبانی نظری ارتباطات دیجیتال.",
        ],
        example_text="در انتقال یک فایل تصویری از یک سرور به تلفن همراه، داده‌ها از کانال شبکه می‌گذرند و ممکن است با نویز مخدوش شوند؛ الگوریتم‌های تصحیح خطا با استفاده از ظرفیت کانال، انتقال بی‌خطا را ممکن می‌کنند. مدل شانون همین فرایند را صورت‌بندی می‌کند.",
        evolution="مقالهٔ سال ۱۹۴۸ نظریهٔ اطلاعات را بنیان گذاشت؛ کتاب سال ۱۹۴۹ با مقدمهٔ ویور سه سطح مسئله را افزود. در دههٔ ۱۹۵۰ مدل به ارتباطات اجتماعی راه یافت و از دههٔ ۱۹۷۰ با فناوری دیجیتال به زیربنای مهندسی ارتباطات تبدیل شد.",
        key_concepts=["منبع اطلاعات", "فرستنده", "کانال", "نویز", "آنتروپی", "ظرفیت کانال", "سه سطح مسئله"],
        theorists="کلود شانون، بنیان‌گذار نظریهٔ اطلاعات؛ و وارن ویور، صورت‌بند سه سطح مسئله.",
        theorists_text="این مدل در سنت مهندسی مخابرات شکل گرفت و بعدها به چارچوب پایهٔ مدل‌های انتقالی ارتباطات تبدیل شد.",
        model="مدل خطی انتقال: منبع، فرستنده، کانال، نویز، گیرنده و مقصد؛ با سه سطح فنی، معنایی و اثربخشی و مفهوم ظرفیت کانال.",
        studies=[
            "مقالهٔ سال ۱۹۴۸ آنتروپی و ظرفیت کانال را صورت‌بندی کرد.",
            "کتاب سال ۱۹۴۹ سه سطح مسئله را افزود.",
            "پژوهش‌های مخابرات، مدل را به فناوری دیجیتال گستردند.",
            "نقدهای ارتباطات اجتماعی، محدودیت مدل انتقالی را نشان دادند.",
        ],
    ),
    "MC-106": dict(
        year=2002,
        summary="مدل عمومی پرخاشگری، چارچوبی یکپارچه برای تبیین پرخاشگری انسانی است که کریگ اندرسون و برد بوشمن در مقالهٔ پرخاشگری انسانی در سال ۲۰۰۲ در سالنامهٔ روان‌شناسی معرفی کردند. ادعای مرکزی این است که پرخاشگری از تعامل عوامل فردی و موقعیتی برمی‌خیزد: عوامل فردی مانند شخصیت، نگرش و تجربهٔ پیشین، و عوامل موقعیتی مانند تحریک، محرومیت و مواجهه با خشونت رسانه‌ای، بر وضعیت درونی فرد یعنی شناخت، عاطفه و برانگیختگی اثر می‌گذارند؛ این وضعیت درونی، ارزیابی و تصمیم فرد را در یک موقعیت اجتماعی شکل می‌دهد و احتمال پاسخ پرخاشگرانه را تغییر می‌دهد. در بلندمدت، مواجههٔ مکرر با خشونت از طریق یادگیری، ساختارهای دانش پرخاشگرانه مانند طرحواره‌ها و فیلم‌نامه‌های پرخاشگری را تقویت می‌کند و حساسیت‌زدایی نسبت به خشونت را افزایش می‌دهد. این مدل، چارچوبی برای پژوهش اثر خشونت رسانه‌ای، بازی‌های ویدئویی و مداخلهٔ کاهش پرخاشگری فراهم کرد. نقدهای اصلی به آن، اندازهٔ اثرهای مورد مناقشه، سوگیری انتشار در پژوهش خشونت رسانه‌ای، تفاوت نتایج آزمایشگاهی و طولی و کم‌توجهی به عوامل ساختاری و فرهنگی مربوط می‌شود.",
        definition="مدل عمومی پرخاشگری، چارچوبی است که پرخاشگری را حاصل تعامل عوامل فردی و موقعیتی، از طریق وضعیت درونی شناخت، عاطفه و برانگیختگی، و در بلندمدت از طریق تقویت ساختارهای دانش پرخاشگرانه توضیح می‌دهد.",
        main_problem="چرا افراد در موقعیت‌های مختلف پاسخ پرخاشگرانه می‌دهند، و مواجههٔ مکرر با خشونت رسانه‌ای چگونه احتمال پرخاشگری را در کوتاه‌مدت و بلندمدت تغییر می‌دهد.",
        mechanism="عوامل فردی و موقعیتی، وضعیت درونی فرد را در سه بعد شناخت، عاطفه و برانگیختگی تغییر می‌دهند؛ فرد موقعیت را ارزیابی می‌کند و بر پایهٔ آن تصمیم می‌گیرد. در بلندمدت، تجربهٔ مکرر، طرحواره‌ها و فیلم‌نامه‌های پرخاشگری را تقویت و حساسیت به خشونت را کم می‌کند.",
        assumptions=[
            "پرخاشگری از تعامل فرد و موقعیت برمی‌خیزد.",
            "شناخت، عاطفه و برانگیختگی، مسیرهای واسط اصلی‌اند.",
            "مواجههٔ مکرر با خشونت، ساختارهای دانش را تغییر می‌دهد.",
            "ارزیابی موقعیت، تصمیم پرخاشگرانه را قالب می‌زند.",
            "مدل باید نظریه‌های دامنه‌محدود پرخاشگری را یکپارچه کند.",
        ],
        principles=[
            "هیچ عامل واحدی پرخاشگری را تعیین نمی‌کند.",
            "وضعیت درونی، واسطهٔ اثر عوامل فردی و موقعیتی است.",
            "یادگیری بلندمدت، ساختارهای دانش پرخاشگرانه می‌سازد.",
            "حساسیت‌زدایی، آستانهٔ پاسخ پرخاشگرانه را پایین می‌آورد.",
            "ارزیابی و تصمیم، حلقهٔ نهایی زنجیرهٔ پرخاشگری است.",
            "مداخله می‌تواند در هر حلقهٔ زنجیره اثر بگذارد.",
        ],
        critiques=[
            "اندازهٔ اثر خشونت رسانه‌ای محل مناقشه است.",
            "سوگیری انتشار در پژوهش‌های این حوزه مطرح شده است.",
            "نتایج آزمایشگاهی و طولی همیشه هم‌خوان نیستند.",
            "عوامل ساختاری و فرهنگی کم‌بررسی می‌مانند.",
            "سنجش ساختارهای دانش پرخاشگرانه دشوار است.",
        ],
        critique_text="منتقدان می‌گویند مدل عمومی پرخاشگری چارچوبی جامع برای یکپارچه‌سازی نظریه‌های پرخاشگری فراهم کرد اما برآورد اندازهٔ اثر خشونت رسانه‌ای و رابطهٔ نتایج آزمایشگاهی با رفتار واقعی محل بحث است. با این حال، مدل مرجع اصلی پژوهش اثر خشونت رسانه‌ای باقی مانده است.",
        applications=[
            "پژوهش اثر خشونت رسانه‌ای و بازی‌های ویدئویی.",
            "طراحی مداخلهٔ کاهش پرخاشگری در مدرسه و رسانه.",
            "تحلیل سیاست‌گذاری محتوای خشونت‌آمیز.",
            "آموزش سواد رسانه‌ای دربارهٔ خشونت.",
            "پژوهش حساسیت‌زدایی در مواجههٔ مکرر با خشونت.",
        ],
        example_text="نوجوانی که ساعت‌ها بازی خشونت‌آمیز انجام می‌دهد، در کوتاه‌مدت با افزایش برانگیختگی و افکار پرخاشگرانه و در بلندمدت با تقویت طرحواره‌های پرخاشگری روبه‌رو می‌شود؛ اما همین فرد در محیطی با نظارت و آموزش سواد رسانه‌ای ممکن است پاسخ‌های متفاوتی نشان دهد. مدل عمومی پرخاشگری این تعامل را توضیح می‌دهد.",
        evolution="ریشهٔ مدل در نظریهٔ یادگیری اجتماعی و پژوهش‌های خشونت رسانه‌ای دههٔ ۱۹۸۰ و ۱۹۹۰ است. مقالهٔ سال ۲۰۰۲ چارچوب یکپارچه را تثبیت کرد و پژوهش‌های بعدی، آن را به بازی‌های ویدئویی، رسانهٔ اجتماعی و مداخله گستردند.",
        key_concepts=["عوامل فردی", "عوامل موقعیتی", "وضعیت درونی", "ساختارهای دانش پرخاشگرانه", "حساسیت‌زدایی", "فیلم‌نامهٔ پرخاشگری"],
        theorists="کریگ اندرسون و برد بوشمن، صورت‌بندانان مدل عمومی پرخاشگری.",
        theorists_text="این مدل در سنت روان‌شناسی اجتماعی پرخاشگری و پژوهش اثر رسانه شکل گرفت و نظریه‌های دامنه‌محدود را یکپارچه کرد.",
        model="مدل سه‌حلقه‌ای: ورودی‌های فردی و موقعیتی، وضعیت درونی شناخت/عاطفه/برانگیختگی، و ارزیابی و تصمیم؛ با حلقهٔ بلندمدت یادگیری ساختارهای دانش پرخاشگرانه.",
        studies=[
            "مقالهٔ سال ۲۰۰۲ چارچوب یکپارچه را با مرور شواهد ارائه کرد.",
            "پژوهش‌های بازی ویدئویی، مسیرهای کوتاه‌مدت مدل را آزمودند.",
            "مطالعات طولی، اثر تجمعی مواجهه با خشونت را بررسی کردند.",
            "مرورهای بعدی، اندازهٔ اثر و سوگیری انتشار را ارزیابی کردند.",
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
                                       "verified": n_verified, "batch": 131}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH131 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
