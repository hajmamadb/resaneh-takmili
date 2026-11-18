# -*- coding: utf-8 -*-
"""Batch 252: full SPEC documentation for CPT-001..005 (foundational communication concepts).

Standard per SPEC section 4.3: definition + summary + mechanism + features/dimensions
+ boundaries + origin + applications + assumptions, inline (Author, Year) citations,
2 web-verified sources per concept into kb_sources/kb_citations/kb_evidence,
live rubric §6.1 score, kb_entity_versions + kb_audit_log (DOC_ENRICH), backup + transaction.
"""
import json
import importlib.util
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch252-20261117"
NOW = "2026-11-17 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch252.json"

S = {
    "CPT-001": [
        dict(kind="book", title_fa="نظریه‌های ارتباط انسانی", title_en="Theories of Human Communication",
             year=2011, publisher="Waveland Press", doi=None, isbn="9781577667063", url=None, language="en",
             authors="Littlejohn, Stephen W.; Foss, Karen A.",
             citation="Littlejohn, S. W., & Foss, K. A. (2011). Theories of human communication (10th ed.). Waveland Press.",
             locator_type="CHAPTER", locator="ch. 1", verified=True,
             supports="چارچوب نظری ارتباط و مرور تعاریف و سنت‌های تولید معنا در ارتباط انسانی."),
        dict(kind="book", title_fa="نظریه ارتباطات انبوه مک‌کویل", title_en="McQuail's Mass Communication Theory",
             year=2010, publisher="Sage", doi=None, isbn="9781849202923", url=None, language="en",
             authors="McQuail, Denis",
             citation="McQuail, D. (2010). McQuail's mass communication theory (6th ed.). Sage.",
             locator_type="CHAPTER", locator="ch. 2", verified=True,
             supports="تمایز سنت‌های انتقال‌گرا و رفتاری از دیدگاه‌های فهم‌محور و میانجی‌شدن رسانه در زندگی اجتماعی."),
    ],
    "CPT-002": [
        dict(kind="book", title_fa="نظریه ریاضی ارتباطات", title_en="The Mathematical Theory of Communication",
             year=1949, publisher="University of Illinois Press", doi=None, isbn=None, url=None, language="en",
             authors="Shannon, Claude E.; Weaver, Warren",
             citation="Shannon, C. E., & Weaver, W. (1949). The mathematical theory of communication. University of Illinois Press.",
             locator_type="page_range", locator="pp. 3–31", verified=True,
             supports="الگوی فرایندی منبع–فرستنده–کانال–گیرنده–مقصد و نقش نویز در انتقال پیام."),
        dict(kind="chapter", title_fa="چگونه ارتباط برقرار می‌شود", title_en="How communication works",
             year=1954, publisher="University of Illinois Press", doi=None, isbn=None, url=None, language="en",
             authors="Schramm, Wilbur",
             citation="Schramm, W. (1954). How communication works. In W. Schramm (Ed.), The process and effects of mass communication (pp. 3–26). University of Illinois Press.",
             locator_type="page_range", locator="pp. 3–26", verified=True,
             supports="مدل فرایندی ارتباط با تاکید بر رمزگذاری، رمزگشایی، تجربه و زمینه‌ی مشترک و حلقه‌ی بازخورد."),
    ],
    "CPT-003": [
        dict(kind="book", title_fa="نظریه ریاضی ارتباطات", title_en="The Mathematical Theory of Communication",
             year=1949, publisher="University of Illinois Press", doi=None, isbn=None, url=None, language="en",
             authors="Shannon, Claude E.; Weaver, Warren",
             citation="Shannon, C. E., & Weaver, W. (1949). The mathematical theory of communication. University of Illinois Press.",
             locator_type="page_range", locator="pp. 5–7", verified=True,
             supports="مفهوم منبع اطلاعات که پیام مطلوب را از میان مجموعه‌ی پیام‌های ممکن انتخاب می‌کند."),
        dict(kind="book", title_fa="کتاب ارتباط میان‌فردی", title_en="The Interpersonal Communication Book",
             year=2016, publisher="Pearson", doi=None, isbn="9780133753813", url=None, language="en",
             authors="DeVito, Joseph A.",
             citation="DeVito, J. A. (2016). The interpersonal communication book (14th ed.). Pearson.",
             locator_type="CHAPTER", locator="ch. 1", verified=True,
             supports="نقش فرستنده به‌مثابه برقرارکننده‌ی ارتباط در مدل‌های میان‌فردی و مهارت‌های رمزگذاری."),
    ],
    "CPT-004": [
        dict(kind="book", title_fa="نظریه ریاضی ارتباطات", title_en="The Mathematical Theory of Communication",
             year=1949, publisher="University of Illinois Press", doi=None, isbn=None, url=None, language="en",
             authors="Shannon, Claude E.; Weaver, Warren",
             citation="Shannon, C. E., & Weaver, W. (1949). The mathematical theory of communication. University of Illinois Press.",
             locator_type="page_range", locator="pp. 5–7", verified=True,
             supports="مقصد ارتباط که پیام بازتولیدشده را دریافت می‌کند؛ گیرنده در قلب الگوی فرایندی."),
        dict(kind="book", title_fa="مقدمه‌ای بر مطالعات ارتباط", title_en="Introduction to Communication Studies",
             year=2011, publisher="Routledge", doi="10.4324/9780203837382", isbn="9780415596497", url=None, language="en",
             authors="Fiske, John",
             citation="Fiske, J. (2011). Introduction to communication studies (3rd ed.). Routledge.",
             locator_type="CHAPTER", locator="ch. 2", verified=True,
             supports="تأکید بر رمزگشایی پیام در بافت اجتماعی و فرهنگی و نقش گیرنده در تولید معنا."),
    ],
    "CPT-005": [
        dict(kind="book", title_fa="نظریه ارتباطات انبوه مک‌کویل", title_en="McQuail's Mass Communication Theory",
             year=2010, publisher="Sage", doi=None, isbn="9781849202923", url=None, language="en",
             authors="McQuail, Denis",
             citation="McQuail, D. (2010). McQuail's mass communication theory (6th ed.). Sage.",
             locator_type="CHAPTER", locator="ch. 13", verified=True,
             supports="پیام به‌مثابه محتوای رسانه: ساختار، کد و معنای پیام‌های رسانه‌ای و روش‌های مطالعه‌ی محتوا."),
        dict(kind="book", title_fa="مقدمه‌ای بر مطالعات ارتباط", title_en="Introduction to Communication Studies",
             year=2011, publisher="Routledge", doi="10.4324/9780203837382", isbn="9780415596497", url=None, language="en",
             authors="Fiske, John",
             citation="Fiske, J. (2011). Introduction to communication studies (3rd ed.). Routledge.",
             locator_type="CHAPTER", locator="ch. 2", verified=True,
             supports="پیام به‌مثابه متن کدبندی‌شده‌ای که گیرنده در بافت اجتماعی-فرهنگی آن را رمزگشایی می‌کند."),
    ],
}

ENRICH = {
    "CPT-001": dict(
        definition="فرایند انتقال و تولید مشترک معنا میان دو یا چند کنشگر از طریق تبادل پیام‌های نمادین، در یک زمینه‌ی اجتماعی و بر پایه‌ی کدهای مشترک؛ فرایندی که می‌تواند آگاهانه یا ناخودآگاه، مستقیم یا میانجی‌شده صورت گیرد (McQuail, 2010; Littlejohn & Foss, 2011).",
        summary="ارتباط از بنیادی‌ترین و در عین حال چندپاره‌ترین مفاهیم علم ارتباطات است. واژه‌ی لاتین آن (communicare) به معنای «سهیم شدن» است و نگاه فرایندی آن را تولید و تبادل معنا میان کنشگران از طریق پیام‌های نمادین می‌داند (Littlejohn & Foss, 2011). در سنت انتقال‌گرا، ارتباط «عبور پیام از کانال میان فرستنده و گیرنده» تعریف می‌شود و در آن نقش نویز، رمزگذاری و رمزگشایی برجسته است؛ سنت‌های بعدی اما ارتباط را نه «انتقال» بلکه «تولید مشترک معنا» تلقی می‌کنند و بر فهم، تفسیر و ساختار اجتماعی تأکید دارند (McQuail, 2010). ارتباط در سطح‌های گوناگون درون‌فردی، میان‌فردی، گروهی، سازمانی و جمعی انجام می‌گیرد و امروزه با فرایند میانجی‌شدن (mediatization) بسیاری از حوزه‌های زندگی اجتماعی از مسیر رسانه تعریف می‌شوند. تنوع تعاریف — از تعریف رفتاریِ خطی تا تعریف فهم‌محورِ گفتمانی — نشان می‌دهد مرز این مفهوم با «انتقال اطلاعات»، «تبادل» و «تولید معنا» هم‌پوشان است و هنوز تعریف واحدی که همه‌ی سنت‌ها را راضی کند وجود ندارد (Littlejohn & Foss, 2011).",
        mechanism="در الگوی فرایندی، ارتباط با انتخاب و ساخت پیام آغاز می‌شود: منبع، معنا را در قالب نمادها و بر اساس کدهای مشترک رمزگذاری می‌کند؛ پیام از کانالی عبور می‌کند که نویز می‌تواند تمامیت آن را تهدید کند؛ گیرنده پیام را رمزگشایی و به معنا تبدیل می‌کند و از طریق بازخورد، همگرایی معنایی میان طرفین حاصل می‌شود (McQuail, 2010). در دیدگاه تولید معنا، این زنجیره خطی نیست: هر دو طرف به‌طور هم‌زمان معنا می‌سازند، تفسیر می‌کنند و زمینه‌ی اجتماعی-فرهنگی بر همه‌ی حلقه‌ها اثر می‌گذارد (Littlejohn & Foss, 2011).",
        key_concepts=["معنا", "پیام", "کد و نماد", "کانال", "بازخورد", "زمینه‌ی ارتباطی"],
        critiques="اصلی‌ترین ابهام مفهومی این است که مرز ارتباط با مفاهیم نزدیک آن — به‌ویژه «انتقال اطلاعات» و «تأثیر» — روشن نیست: آیا هر رفتاری ارتباط است یا فقط رفتار نمادین؟ (Littlejohn & Foss, 2011). نقد دیگر بر «سوگیری انتقال‌گرایی» است که ارتباط را حمل چیزی از نقطه‌ای به نقطه‌دیگر می‌بیند و بعدِ تشریفاتی، فرهنگی و مشارکتی آن را کم‌می‌بیند (McQuail, 2010). همچنین بسیاری از تعاریف بر تعمد آگاهانه تمرکز دارند در حالی که بخش بزرگی از ارتباط انسانی ناخودآگاه است.",
        applications="طراحی نظام‌های رسانه‌ای و سیاست‌گذاری ارتباطی، آموزش مهارت‌های ارتباطی، ارتباط سلامت و اقناع عمومی، مدیریت سازمانی و روابط عمومی، و تحلیل میانجی‌شدن رسانه در حوزه‌هایی مانند سیاست، دین و آموزش (McQuail, 2010).",
        evolution="معنای واژه از communicare (سهیم شدن) در لاتین می‌آید؛ در قرن بیستم، نظریه‌ی ریاضی ارتباطات (۱۹۴۹) آن را به الگوی فرایندی منبع–کانال–مقصد تبدیل کرد و پژوهش‌های نیمه‌ی دوم قرن، با گسترش رسانه‌های جمعی و فرهنگی، دیدگاه‌های فهم‌محور، انتقادی و گفتمانی را بر آن افزودند (McQuail, 2010؛ Littlejohn & Foss, 2011).",
        assumptions="پیش‌فرض‌های نهفته: وجود کدها و نمادهای تا حدی مشترک میان طرفین، امکان دسترسی به کانال و زمینه‌ی مشترک، و این‌که معنا نه «در» پیام، بلکه در تعامل میان پیام، گیرنده و بافت ساخته می‌شود (Littlejohn & Foss, 2011).",
    ),
    "CPT-002": dict(
        definition="توالی پیوسته‌ی وقایع میان‌وابسته که از تولید قصد و انتخاب پیام توسط منبع آغاز، و با رمزگذاری، عبور از کانال، رمزگشایی و بازخورد توسط مقصد، به تبادل معنا می‌انجامد؛ توالی‌ای که در آن هر حلقه به حلقه‌ی پیشین وابسته است (Shannon & Weaver, 1949; Schramm, 1954).",
        summary="فرایند ارتباط نگرشی است که ارتباط را نه یک «رویداد» بلکه یک «جریانِ پیوسته و چرخه‌ای» می‌فهمد. الگوی شانون-ویور (۱۹۴۹) این فرایند را زنجیره‌ای از اجزا — منبع اطلاعات، فرستنده، کانال، گیرنده و مقصد — با نویز به‌عنوان تهدیدکننده‌ی هر حلقه تصویر می‌کند و مسئله‌ی بنیادین ارتباط را «بازتولید پیام در نقطه‌ای دیگر» تعریف می‌کند. شرام (۱۹۵۴) با افزودن «زمینه‌ی تجربه» و «بازخورد» به این زنجیره، آن را از الگوی یک‌طرفه به مدلی چرخه‌ای نزدیک کرد: فرستنده و گیرنده نقش‌هایی تبادل‌پذیر دارند و هر پیام، با زمینه‌ی تجربه‌ی مشترک طرفین، قابل فهم است. در این نگاه، ارتباط موفق یعنی هم‌پوشانیِ نسبیِ زمینه‌ها و گردشِ بازخورد که انحراف معنایی را اصلاح می‌کند. نقد بنیادین بر الگوهای فرایندی، خطی‌بودن و فقدان بعد اجتماعی-فرهنگی آن‌هاست: مدل‌ها به ما می‌گویند ارتباط «چگونه» جریان می‌یابد، اما نمی‌گویند معنا در بافت قدرت و فرهنگ چگونه ساخته می‌شود (Schramm, 1954).",
        mechanism="حلقه‌های اصلی فرایند: (۱) تولید قصد و انتخاب پیام از میان پیام‌های ممکن؛ (۲) رمزگذاری: تبدیل قصد به نمادها و سیگنال‌ها؛ (۳) انتقال از کانال با ظرفیت محدود و در معرض نویز؛ (۴) رمزگشایی: بازسازی معنا از سیگنال‌ها؛ (۵) بازخورد: پاسخی که فرستنده را از نتیجه‌ی انتقال آگاه می‌کند و چرخه را می‌بندد (Shannon & Weaver, 1949; Schramm, 1954).",
        key_concepts=["منبع و مقصد", "رمزگذاری و رمزگشایی", "کانال و ظرفیت", "نویز", "بازخورد", "زمینه‌ی تجربه‌ی مشترک"],
        critiques="الگوی فرایندی خطی، نقش فعال گیرنده و تفسیر او را کم‌می‌بیند و فرض می‌کند معنا عیناً منتقل می‌شود (Schramm, 1954 این را با زمینه‌ی تجربه اصلاح کرد). نقد دیگر، غفلت از ساختار اجتماعی و قدرت است: کانال‌ها متعلق به نهادها هستند و دسترسی به آن‌ها نامتقارن است. همچنین مفهوم نویز بیشتر فنی است و انواع اجتماعی «نویز» (کلیشه، سوگیری فرهنگی) را پوشش نمی‌دهد (Shannon & Weaver, 1949).",
        applications="طراحی شبکه‌ها و نظام‌های مخابراتی، بهینه‌سازی پیام‌های آموزشی و تبلیغاتی، ارزیابی کارایی کانال‌های سازمانی، و تحلیل شکست‌های ارتباطی در بحران‌ها — جایی که نویز و فقدان بازخورد تعیین‌کننده‌اند (Shannon & Weaver, 1949; Schramm, 1954).",
        evolution="الگوی فرایندی از مهندسی مخابرات (شانون، ۱۹۴۸/۱۹۴۹) وارد علوم ارتباط شد و با شرام (۱۹۵۴) و افزودن بازخورد و تجربه، به «مدل چرخه‌ای» نزدیک گردید؛ از دهه‌ی ۱۹۶۰ به بعد، دیدگاه‌های فهم‌محور و انتقادی مدل خطی را به‌نفع تولید مشترک معنا کنار گذاشتند (Schramm, 1954).",
        assumptions="فرض‌های نهفته: پیام قابل تفکیک از معناست، کانال دارای ظرفیت قابل اندازه‌گیری است، طرفین به کدهای مشترک دسترسی دارند و بازخورد صادقانه و به‌موقع فراهم می‌شود (Shannon & Weaver, 1949; Schramm, 1954).",
    ),
    "CPT-003": dict(
        definition="کنشگر یا عنصری در مدل فرایندی ارتباط که قصد را تولید، پیام را از میان پیام‌های ممکن انتخاب و آن را بر اساس کدهای مشترک رمزگذاری می‌کند تا از طریق کانال به گیرنده منتقل شود (Shannon & Weaver, 1949). در ارتباط میان‌فردی، فرستنده نقشی تبادل‌پذیر با گیرنده دارد و مسئولیت آغاز و جهت‌دهی به تعامل را بر عهده می‌گیرد (DeVito, 2016).",
        summary="فرستنده (منبع) نخستین حلقه‌ی الگوی فرایندی است: طبق شانون و ویور (۱۹۴۹)، «منبع اطلاعات پیامی مطلوب را از میان مجموعه‌ای از پیام‌های ممکن انتخاب می‌کند» و سپس آن را به سیگنال‌های قابل انتقال تبدیل می‌کند. در این دید، فرستنده کنشگری هدفمند است که با انتخاب پیام، میزان عدم قطعیت گیرنده را کاهش می‌دهد. در سنت میان‌فردی، نقش فرستنده فراتر از «تولید پیام» است: او با مهارت‌های کلامی و غیرکلامی، زمینه‌ی ارتباط را می‌سازد، پیام را به توانایی و سواد گیرنده تطبیق می‌دهد و از بازخورد برای اصلاح ارسال خود استفاده می‌کند (DeVito, 2016). نقد بنیادین بر مفهوم فرستنده، خطی‌بودن آن در الگوهای اولیه است — فرستنده‌ای که «صاحب معنا» فرض می‌شود و گیرنده را منفعل می‌بیند؛ در حالی که در تبادل واقعی، هر دو طرف هم‌زمان فرستنده و گیرنده‌اند و معنا به‌صورت مشترک ساخته می‌شود. همچنین در رسانه‌های امروزی، الگوریتم‌ها و پلتفرم‌ها خود به‌مثابه «فرستنده‌های ناپیدا» عمل می‌کنند (DeVito, 2016).",
        mechanism="فرایند نقش فرستنده: (۱) شکل‌گیری قصد و هدف ارتباطی؛ (۲) انتخاب پیام از میان گزینه‌ها — انتخابی که «آنتروپی» گیرنده را کم می‌کند؛ (۳) رمزگذاری: تبدیل قصد به کلمات، تصاویر و سیگنال‌ها بر اساس کدهای مشترک؛ (۴) انتقال از کانال و مدیریت نویز؛ و (۵) تفسیر بازخورد گیرنده و بازتنظیم پیام در چرخه‌های بعدی (Shannon & Weaver, 1949; DeVito, 2016).",
        key_concepts=["منبع اطلاعات", "انتخاب پیام", "رمزگذاری", "قصد ارتباطی", "مهارت‌های فرستادگی", "بازخورد"],
        critiques="انتقاد اصلی، فرض «فرستنده‌ی فعال/گیرنده‌ی منفعل» است که در تعامل واقعی مصداق ندارد؛ نقش‌ها در تعامل میان‌فردی دائم جابه‌جا می‌شوند (DeVito, 2016). نقد دیگر، بی‌توجهی به شرایط ساختاری است: توانایی «فرستادن» به توان رسانه‌ای، سرمایه نمادین و دسترسی به کانال‌ها گره خورده است. در مدل‌های فنی نیز فرستنده‌ی انسانی به «انتخاب‌کننده‌ی پیام» فروکاسته می‌شود و ابعاد اخلاقی و اجتماعی مسئولیت ارسال را پوشش نمی‌دهد (Shannon & Weaver, 1949).",
        applications="طراحی کمپین‌های اطلاع‌رسانی و آموزش عمومی، نگارش پیام‌های بحران با رمزگذاری واضح، آموزش مهارت‌های ارائه و مذاکره، و تحلیل مسئولیت اخلاقی نویسندگان، خبرنگاران و تولیدکنندگان محتوا به‌مثابه فرستنده‌های پیام (DeVito, 2016).",
        evolution="در الگوی شانون-ویور (۱۹۴۹) فرستنده «منبع»ی فنی بود که پیام را انتخاب می‌کرد؛ با ورود شرام و مکتب میان‌فردی، فرستنده به کنشگری اجتماعی با قصد، مهارت و مسئولیت اخلاقی بدل شد و در الگوهای تعاملی، نقش آن با گیرنده در هم آمیخت (DeVito, 2016).",
        assumptions="فرض‌های نهفته: فرستنده قصدی آگاهانه دارد، به کدهای مشترک با گیرنده دسترسی است، قادر به انتخاب میان پیام‌های جایگزین است و بازخورد معتبری دریافت می‌کند تا ارسال خود را اصلاح کند (Shannon & Weaver, 1949; DeVito, 2016).",
    ),
    "CPT-004": dict(
        definition="عنصری در مدل فرایندی ارتباط که پیام منتقل‌شده را دریافت، از سیگنال‌ها معنا را رمزگشایی و پیام بازتولیدشده را به مقصد تحویل می‌دهد (Shannon & Weaver, 1949). در سنت مطالعات فرهنگی، گیرنده کنشگری فعال است که پیام را در بافت اجتماعی-فرهنگی خود تفسیر می‌کند و معنای نهایی را می‌سازد (Fiske, 2011).",
        summary="گیرنده در الگوی شانون-ویور (۱۹۴۹) «مقصد» فرایند است: پیام پس از عبور از کانال توسط گیرنده دریافت و رمزگشایی می‌شود تا اثر ارتباط — کاهش عدم قطعیت در گیرنده — تحقق یابد. اما این تصویر، گیرنده را ظرفی منفعل می‌بیند. سنت‌های بعدی، به‌ویژه در مطالعات رسانه و فرهنگ، این نقش را بازتعریف کردند: گیرنده با سواد رسانه‌ای، سوگیری‌ها و کدهای فرهنگی خود، پیام را تفسیر می‌کند و ممکن است معنایی متفاوت از قصد فرستنده بسازد (Fiske, 2011). در این دید، «گیرندگی» یک فعالیت است نه یک وضعیت: انتخاب، توجه، تفسیر و به‌کارگیری پیام در زندگی روزمره. در رسانه‌های دیجیتال، الگوریتم‌های توصیه و پلتفرم‌ها نیز گیرندگی را شکل می‌دهند و مرز «انتخاب آگاهانه» مخاطب را تغییر داده‌اند. نقد بنیادین بر هر دو تصویر، خطی‌بودن زنجیره است: در تعامل واقعی افراد هم‌زمان فرستنده و گیرنده‌اند و معنا در چرخه‌ی پیوسته ساخته می‌شود (Fiske, 2011).",
        mechanism="فرایند نقش گیرنده: (۱) دریافت سیگنال‌ها و بازیابی پیام از میان نویز؛ (۲) رمزگشایی: تبدیل نمادها به معنا بر اساس کدهای شخصی و فرهنگی؛ (۳) تفسیر: قرار دادن پیام در زمینه‌ی تجربه و باورهای خود؛ (۴) پاسخ: تولید بازخورد — لحظه‌ای یا به‌صورت رفتار بعدی — که چرخه را می‌بندد (Shannon & Weaver, 1949; Fiske, 2011).",
        key_concepts=["مقصد ارتباط", "رمزگشایی", "تفسیر", "سواد رسانه‌ای", "بازخورد", "کنشگری مخاطب"],
        critiques="الگوی فنی گیرنده را منفعل و یکسان می‌پندارد و تفاوت‌های فردی، فرهنگی و طبقاتی در تفسیر را نمی‌بیند (Shannon & Weaver, 1949). نقد مقابل، خطر «برآورد بیش از حد فعالیت مخاطب» است: در شرایط انحصار رسانه‌ای و الگوریتمیک، گزینه‌های تفسیر محدود و هدایت می‌شوند و «کنشگری» نباید به انکار ساختار منجر شود (Fiske, 2011). همچنین مفهوم گیرنده در ارتباط انبوه دشوارتر است: مخاطب جمعی ناهمگن است و سخن گفتن از «گیرنده‌ی واحد» ساده‌سازی است.",
        applications="طراحی پیام‌های سلامت و آموزشی با لحاظ سواد مخاطب، سنجش اثربخشی رسانه‌ها با مطالعات مخاطب، تدوین سیاست‌های سواد رسانه‌ای، و تحلیل رفتار مصرف‌کنندگان در پلتفرم‌های دیجیتال (Fiske, 2011).",
        evolution="از «مقصد» فنی در الگوی ۱۹۴۹، به «مخاطب» فعال در پژوهش‌های اثرات (دهه‌های ۱۹۴۰ تا ۱۹۶۰) و سپس به «کنشگر تولیدکننده‌ی معنا» در مکتب فرهنگی و مطالعات پذیرش رسید (Fiske, 2011). در عصر پلتفرم، گیرندگی با داده‌سازی رفتار مخاطب و سیستم‌های توصیه‌گر بازتعریف شده است.",
        assumptions="فرض‌های نهفته: گیرنده به کدهای مشترک دسترسی دارد، توان و انگیزه رمزگشایی را دارد و بازخوردش به فرستنده می‌رسد؛ در سنت فعال، فرض بر این است که تفسیر مخاطب مشروع و گاه بر قصد فرستنده غلبه می‌کند (Shannon & Weaver, 1949; Fiske, 2011).",
    ),
    "CPT-005": dict(
        definition="متن کدبندی‌شده‌ای از نمادها — کلامی، تصویری، صوتی یا رفتاری — که برای انتقال قصد و معنا از فرستنده به گیرنده ساخته می‌شود و در بافت اجتماعی-فرهنگی خود معنای نهایی را می‌پذیرد (Fiske, 2011). در سنت رسانه‌های جمعی، پیام محتوای رسانه است: ساختاری از کدها و قالب‌ها که انتخاب و چینش عناصر آن، معنا را می‌سازد (McQuail, 2010).",
        summary="پیام قلب ارتباط است: هر آنچه از فرستنده به گیرنده می‌رسد — گفتار، متن، تصویر، ویدئو، موسیقی یا ترکیبی از آن‌ها. در سنت فرایندی، پیام «محموله‌ی معنا» است که رمزگذاری و رمزگشایی می‌شود (Fiske, 2011). در مطالعات رسانه، پیام به‌مثابه «محتوا» با سه لایه‌ی معنایی بررسی می‌شود: معنای مطلوب (قصد فرستنده)، معنای پذیرفته‌شده (تفسیر گیرنده) و معنای جمعی (نشانه‌های برجسته در فرهنگ) (McQuail, 2010). پیام‌ها در قالب‌های مشخص جریان می‌یابند — خبر، تبلیغ، داستان، گفت‌وگو — و هر قالب قواعد خود را برای ساخت معنا دارد. نقد بنیادین، تلقی پیام به‌مثابه «ظرف» خنثی است: در حقیقت انتخاب و چینش عناصر پیام، بازنمایی‌های جهت‌دار است و «بودن یا نبودن» یک عنصر، خود نوعی بیان است. همچنین با دیجیتالی‌شدن، پیام از «اثر ثابت» به «جریان داده‌ی شخصی‌سازی‌شده» تبدیل شده و یک پیام واحد برای همه وجود ندارد (McQuail, 2010).",
        mechanism="ساخت پیام: انتخاب نشانه‌ها (کلمات، تصاویر، صداها)، چینش آن‌ها بر اساس قواعد کد و قالب، و تولید یک کل معنادار. دریافت پیام نیز فرایندی است: گیرنده نشانه‌ها را رمزگشایی و در بافت اجتماعی خود تفسیر می‌کند؛ معنای نهایی در تقاطع ساختار پیام و بافت گیرنده ساخته می‌شود (Fiske, 2011).",
        key_concepts=["نشانه و کد", "قالب", "معنای مطلوب/پذیرفته‌شده", "بازنمایی", "قاب‌بندی", "جریان پیام"],
        critiques="مفهوم پیام با «انتقال» گره خورده و خطر کالایی‌بودن معنا را دارد؛ نقد انتقادی می‌گوید پیام‌ها نه «حامل» بلکه «سازنده‌ی واقعیت» اجتماعی‌اند (McQuail, 2010). نقد دیگر، تمایز شکننده‌ی «فرم/محتوا» است: قالب پیام (طول، سرعت، تصویری/متنی) بر معنای آن اثر می‌گذارد و نمی‌توان آن را از محتوا جدا دانست (Fiske, 2011). همچنین در محیط الگوریتمی، پیام‌های شخصی‌سازی‌شده، مفهوم «پیام واحد برای مخاطب جمعی» را به چالش کشیده‌اند.",
        applications="تحلیل محتوای رسانه‌ها، نگارش و ویرایش پیام‌های تبلیغاتی و خبری، طراحی پیام‌های سلامت عمومی، ارزیابی پیام‌های سیاسی در کمپین‌ها، و بهینه‌سازی پیام برای کانال‌های دیجیتال (McQuail, 2010; Fiske, 2011).",
        evolution="از پیام به‌مثابه «الگوی فیزیکی» در نظریه‌ی ریاضی (مفهومی برای اندازه‌گیری) به «متن کدبندی‌شده» در نظریه‌ی نشانه‌شناختی و سپس به «محتوای رسانه» در جامعه‌شناسی رسانه تکامل یافت؛ در عصر دیجیتال، پیام به جریانی از واحدهای کوچک داده‌محور تبدیل شده که توسط الگوریتم‌ها برای هر کاربر بازترکیب می‌شوند (McQuail, 2010؛ Fiske, 2011).",
        assumptions="فرض‌های نهفته: پیام از قصد فرستنده جداشدنی و توسط کدهای مشترک قابل رمزگشایی است؛ پیام دارای مرز مشخصی است (آغاز و پایان)؛ و تحلیل پیام بدون توجه به بافت گیرنده ناقص است (Fiske, 2011).",
    ),
}


def main():
    spec = importlib.util.spec_from_file_location("fw", "scripts/kb_batch238_framework.py")
    fw = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(fw)
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

    snap = [{"id": r[0], "code": r[1], "properties": json.loads(r[2])} for r in rows]
    with open(BACKUP, "w", encoding="utf-8") as f:
        json.dump(snap, f, ensure_ascii=False, indent=1)
    print("backup ->", len(snap), "rows")

    for code in codes:
        eid, _c, props = found[code]
        p = json.loads(props)
        en = ENRICH[code]

        for k, v in en.items():
            p[k] = v

        p["sources"] = []
        p["citations"] = []
        for src in S[code]:
            p["sources"].append({
                "citation": src["citation"], "title_en": src["title_en"],
                "title_fa": src["title_fa"], "year": src["year"], "doi": src.get("doi"),
                "url": src.get("url"), "language": src["language"], "verified": src["verified"],
            })
            p["citations"].append({
                "source": src["citation"], "locator": src["locator"],
                "supports": src["supports"], "verified": src["verified"],
            })

        cur.execute("SELECT COUNT(*) FROM kb_relations WHERE source_id=%s OR target_id=%s", (eid, eid))
        n_rel = cur.fetchone()[0]
        n_sources = len(p["sources"])
        n_verified = sum(1 for x in p["citations"] if x.get("verified"))
        score, detail, words = fw.rubric(p, n_verified, n_sources, n_rel)

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
            sid = fw.ensure_source(cur, src)
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
                     "full concept documentation (SPEC §4.3) + verified sources", STAMP, NOW))

        cur.execute("""INSERT INTO kb_audit_log (entity_code,action,detail,source,created_at)
            VALUES (%s,'DOC_ENRICH',%s,%s,%s)""",
                    (code, json.dumps({"batch": 252, "score": score, "words": words,
                                       "sources": n_sources, "verified": n_verified,
                                       "relations": n_rel, "rubric": detail}, ensure_ascii=False), STAMP, NOW))
        print(code, "words", words, "score", score, "detail", detail)

    conn.commit()
    conn.close()
    print("BATCH252 DONE")


if __name__ == "__main__":
    main()
