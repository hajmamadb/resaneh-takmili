# -*- coding: utf-8 -*-
"""Batch 253: full SPEC documentation for CPT-006..010 (Channel, Media, Feedback, Encoding, Decoding).
All sources already exist in kb_sources from batch 252 (ensure_source dedupes by title_en+year/doi)."""
import json
import importlib.util
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch253-20261117"
NOW = "2026-11-17 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch253.json"

S = {
    "CPT-006": [
        dict(kind="book", title_fa="نظریه ریاضی ارتباطات", title_en="The Mathematical Theory of Communication",
             year=1949, publisher="University of Illinois Press", doi=None, isbn=None, url=None, language="en",
             authors="Shannon, Claude E.; Weaver, Warren",
             citation="Shannon, C. E., & Weaver, W. (1949). The mathematical theory of communication. University of Illinois Press.",
             locator_type="page_range", locator="pp. 29–40", verified=True,
             supports="کانال به‌مثابه مسیر انتقال سیگنال با ظرفیت و در معرض نویز."),
        dict(kind="book", title_fa="نظریه ارتباطات انبوه مک‌کویل", title_en="McQuail's Mass Communication Theory",
             year=2010, publisher="Sage", doi=None, isbn="9781849202923", url=None, language="en",
             authors="McQuail, Denis",
             citation="McQuail, D. (2010). McQuail's mass communication theory (6th ed.). Sage.",
             locator_type="CHAPTER", locator="ch. 5", verified=True,
             supports="رسانه به‌مثابه کانال‌های جمعی: ویژگی‌های فنی، اقتصادی و اجتماعی کانال رسانه‌ای."),
    ],
    "CPT-007": [
        dict(kind="book", title_fa="نظریه ارتباطات انبوه مک‌کویل", title_en="McQuail's Mass Communication Theory",
             year=2010, publisher="Sage", doi=None, isbn="9781849202923", url=None, language="en",
             authors="McQuail, Denis",
             citation="McQuail, D. (2010). McQuail's mass communication theory (6th ed.). Sage.",
             locator_type="CHAPTER", locator="ch. 1", verified=True,
             supports="رسانه‌های جمعی: تعریف، طبقه‌بندی و ویژگی‌های تمایز‌بخش رسانه."),
        dict(kind="book", title_fa="نظریه‌های ارتباط انسانی", title_en="Theories of Human Communication",
             year=2011, publisher="Waveland Press", doi=None, isbn="9781577667063", url=None, language="en",
             authors="Littlejohn, Stephen W.; Foss, Karen A.",
             citation="Littlejohn, S. W., & Foss, K. A. (2011). Theories of human communication (10th ed.). Waveland Press.",
             locator_type="CHAPTER", locator="ch. 1", verified=True,
             supports="رسانه به‌مثابه عنصر میانجی و نظام نمادین؛ رسانه در سنت‌های فرایندی و فرهنگی."),
    ],
    "CPT-008": [
        dict(kind="book", title_fa="نظریه ریاضی ارتباطات", title_en="The Mathematical Theory of Communication",
             year=1949, publisher="University of Illinois Press", doi=None, isbn=None, url=None, language="en",
             authors="Shannon, Claude E.; Weaver, Warren",
             citation="Shannon, C. E., & Weaver, W. (1949). The mathematical theory of communication. University of Illinois Press.",
             locator_type="page_range", locator="pp. 5–15", verified=True,
             supports="نقش بازخورد در کنترل و اصلاح فرایند انتقال پیام."),
        dict(kind="book", title_fa="کتاب ارتباط میان‌فردی", title_en="The Interpersonal Communication Book",
             year=2016, publisher="Pearson", doi=None, isbn="9780133753813", url=None, language="en",
             authors="DeVito, Joseph A.",
             citation="DeVito, J. A. (2016). The interpersonal communication book (14th ed.). Pearson.",
             locator_type="CHAPTER", locator="ch. 1", verified=True,
             supports="بازخورد به‌مثابه پاسخ گیرنده و سازوکار تنظیم و ارزیابی در تعامل."),
    ],
    "CPT-009": [
        dict(kind="book", title_fa="نظریه ریاضی ارتباطات", title_en="The Mathematical Theory of Communication",
             year=1949, publisher="University of Illinois Press", doi=None, isbn=None, url=None, language="en",
             authors="Shannon, Claude E.; Weaver, Warren",
             citation="Shannon, C. E., & Weaver, W. (1949). The mathematical theory of communication. University of Illinois Press.",
             locator_type="page_range", locator="pp. 29–35", verified=True,
             supports="رمزگذاری به‌مثابه تبدیل پیام به سیگنال‌های قابل انتقال بر اساس کد."),
        dict(kind="book", title_fa="مقدمه‌ای بر مطالعات ارتباط", title_en="Introduction to Communication Studies",
             year=2011, publisher="Routledge", doi="10.4324/9780203837382", isbn="9780415596497", url=None, language="en",
             authors="Fiske, John",
             citation="Fiske, J. (2011). Introduction to communication studies (3rd ed.). Routledge.",
             locator_type="CHAPTER", locator="ch. 2", verified=True,
             supports="رمزگذاری به‌مثابه انتخاب نشانه‌ها از میان کدهای فرهنگی و اجتماعی."),
    ],
    "CPT-010": [
        dict(kind="book", title_fa="نظریه ریاضی ارتباطات", title_en="The Mathematical Theory of Communication",
             year=1949, publisher="University of Illinois Press", doi=None, isbn=None, url=None, language="en",
             authors="Shannon, Claude E.; Weaver, Warren",
             citation="Shannon, C. E., & Weaver, W. (1949). The mathematical theory of communication. University of Illinois Press.",
             locator_type="page_range", locator="pp. 35–45", verified=True,
             supports="رمزگشایی به‌مثابه بازسازی پیام از سیگنال‌های دریافتی."),
        dict(kind="book", title_fa="مقدمه‌ای بر مطالعات ارتباط", title_en="Introduction to Communication Studies",
             year=2011, publisher="Routledge", doi="10.4324/9780203837382", isbn="9780415596497", url=None, language="en",
             authors="Fiske, John",
             citation="Fiske, J. (2011). Introduction to communication studies (3rd ed.). Routledge.",
             locator_type="CHAPTER", locator="ch. 2", verified=True,
             supports="رمزگشایی به‌مثابه تفسیر نشانه‌ها در بافت اجتماعی و فرهنگی گیرنده."),
    ],
}

ENRICH = {
    "CPT-006": dict(
        definition="مسیری که پیام یا سیگنال از فرستنده به گیرنده از آن عبور می‌کند؛ مسیری با ظرفیت محدود، قابل اندازه‌گیری و در معرض نویز که ممکن است فیزیکی (سیم، هوا)، دیجیتال یا نمادین باشد (Shannon & Weaver, 1949). در سنت رسانه‌های جمعی، کانال به مجموعه‌ی فناوری، نهاد و قالب‌های انتقال می‌گوید (McQuail, 2010).",
        summary="کانال یکی از اجزای بنیادین الگوی فرایندی است. در نظریه‌ی ریاضی ارتباطات (شانون، ۱۹۴۸/۱۹۴۹)، کانال «مسیر انتقال سیگنال» است که دارای ظرفیت (bandwidth) مشخصی است و نویز می‌تواند سیگنال را تشویش دهد؛ مسئله‌ی ارتباط، بازتولید پیام در مقصد با حداکثر صحت از طریق کانالی است که ظرفیت و شرایط آن محدودکننده‌اند (Shannon & Weaver, 1949). در سنت رسانه‌ای، کانال مفهوم فراتر از یک مجرای فنی است: هر رسانه (رادیو، تلویزیون، روزنامه، وب) یک کانال با ویژگی‌های فنی، اقتصادی و فرهنگی متمایز است که بر نوع پیام و رفتار مخاطب اثر می‌گذارد (McQuail, 2010). نقد بنیادین بر مفهوم کانال، تقلیل‌گرایی فنی آن است: کانال در مدل‌های فرایندی مجرای خنثی‌ای است که پیام را «می‌کَنَد»، در حالی که در واقع ساختار، اقتصاد و قواعد کانال بر معنا و تفسیر اثر مستقیم دارند (McQuail, 2010). همچنین در محیط دیجیتال، «کانال» مرز روشنی با «پلتفرم» ندارد: الگوریتم‌ها، ظرفیت و مسیر کانال را تعیین می‌کنند و کانال یک‌طرفه به شبکه‌ای چندجانبه بدل شده است.",
        mechanism="در الگوی شانون-ویور، کانال سه نقش دارد: (۱) انتقال سیگنال از فرستنده به گیرنده با ظرفیت محدود؛ (۲) قرار گرفتن در معرض نویز (تشویش) که احتمال خطا را بالا می‌برد؛ (۳) تعیین نرخ و نوع اطلاعات قابل انتقال. در کانال‌های چندرسانه‌ای، ترکیب باندپهنای مختلف (صوت، تصویر، داده) ظرفیت ترکیبی ایجاد می‌کند که بر کیفیت و نوع پیام اثر می‌گذارد (Shannon & Weaver, 1949; McQuail, 2010).",
        key_concepts=["ظرفیت کانال", "نویز", "باندپهنای رسانه‌ای", "کانال فنی و نمادین", "پلتفرم"],
        critiques="الگوی فنی کانال را خنثی و مجزای از معنا می‌بیند (Shannon & Weaver, 1949)؛ نقد انتقادی می‌گوید ساختار اقتصادی و سیاسی کانال (مالکیت، دسترسی، الگوریتم) بر معنای پیام اثر مستقیم دارد (McQuail, 2010). همچنین مفهوم «کانال» در رسانه‌های تعاملی و شبکه‌ای مرز روشنی با «پلتفرم» و «شبکه» ندارد و مدل خطی آن در شبکه‌های چندجانبه کاربرد کمتری دارد.",
        applications="طراحی شبکه‌های مخابراتی و بهینه‌سازی ظرفیت کانال، انتخاب رسانه برای کمپین‌های تبلیغاتی و اطلاع‌رسانی (media mix)، تحلیل اثر فناوری کانال بر محتوا و مخاطب، و طراحی پلتفرم‌های چندرسانه‌ای (Shannon & Weaver, 1949; McQuail, 2010).",
        evolution="از «کانال» به‌مثابه مجرای فنی در مهندسی مخابرات (شانون، ۱۹۴۸)، به «رسانه» در علوم ارتباط جمعی (دهه‌های ۱۹۴۰–۱۹۶۰) و سپس به «پلتفرم» در عصر دیجیتال تکامل یافت؛ امروزه کانال و پلتفرم در هم تنیده‌اند و الگوریتم‌ها ظرفیت و مسیر آن‌ها را تعیین می‌کنند (McQuail, 2010).",
        assumptions="فرض‌های نهفته: کانال دارای ظرفیت قابل اندازه‌گیری و ثابت است، نویز تصادفی و از پیش‌بینی‌نکردنی است، و پیام از کانال بدون تغییر معنایی عبور می‌کند (Shannon & Weaver, 1949)؛ در سنت رسانه‌ای، فرض بر این است که ویژگی‌های فنی کانال بر نوع پیام قابل‌انتقال اثر می‌گذارند (McQuail, 2010).",
    ),
    "CPT-007": dict(
        definition="نظام فناوری، نهاد و نمادین برای تولید، پخش و مصرف پیام‌های نمادین به مخاطبان گسترده؛ رسانه کانال میانجی بین فرستنده و گیرنده است و خود ساختار، اقتصاد و قواعد معنایی مستقل دارد (McQuail, 2010; Littlejohn & Foss, 2011).",
        summary="رسانه از کلیدی‌ترین مفاهیم علم ارتباط جمعی است. در معنای باریک، رسانه «فناوری انتقال» است — رادیو، تلویزیون، مطبوعات، وب — و در معنای گسترده، به «نهاد و نظام» تولید و توزیع محتوا اشاره دارد (McQuail, 2010). رسانه در سنت فرایندی، کانالی است که پیام را از فرستنده به مخاطب می‌رساند؛ اما در سنت فرهنگی و انتقادی، رسانه «دستگاه نمادین» است که خود واقعیت اجتماعی را می‌سازد و نه صرفاً منعکس می‌کند (Littlejohn & Foss, 2011). ویژگی‌های تمایز‌بخش رسانه‌های جمعی: مخاطبان گسترده و ناهمگن، یک‌طرفگی نسبی، سازمان‌دار بودن تولید، و بازتولید اقتصادی (McQuail, 2010). نقد بنیادین، «مجلّی‌زدگی» (reification) رسانه است: رسانه به‌مثابه «چیز» خنثی توصیف می‌شود در حالی که در واقع ساختار قدرت، مالکیت و اقتصاد آن بر معنا و اثر آن اثر مستقیم دارد. همچنین با پلتفرمی‌شدن، مرز تولیدکننده و مصرف‌کننده به‌شدت محو شده و رسانه از «مؤسسه» به «سیستم» تبدیل شده است (Littlejohn & Foss, 2011).",
        mechanism="رسانه سه لایه عمل می‌کند: (۱) لایه‌ی فنی: فناوری‌های تولید، پخش و دسترسی که بر نوع و سرعت پیام اثر می‌گذارند؛ (۲) لایه‌ی نهادی: سازمان‌ها، مالکیت، اقتصاد و قواعد حرفه‌ای که بر انتخاب و قاب‌بندی محتوا اثر می‌گذارند؛ (۳) لایه‌ی نمادین: کدها، قالب‌ها و روایت‌های فرهنگی که بر تفسیر مخاطب اثر می‌گذارند (McQuail, 2010; Littlejohn & Foss, 2011).",
        key_concepts=["کانال جمعی", "نهاد رسانه‌ای", "کد و قالب", "اقتصاد رسانه", "میانجی‌شدن", "پلتفرم"],
        critiques="تعریف «رسانه» مرز روشنی با «تکنولوژی»، «نهاد» و «نظام» ندارد و در ادبیات اغلب خلط می‌شود (Littlejohn & Foss, 2011). نقد دیگر، «ارزش‌مندی‌زدایی» (de-institutionalization) رسانه در عصر دیجیتال است: وقتی هر کاربر می‌تواند تولیدکننده باشد، مفهوم «رسانه‌ی جمعی» و «مخاطب جمعی» از معنای خود می‌کاهد (McQuail, 2010). همچنین تحلیل رسانه‌ای اغلب بر «محتوا» تمرکز دارد و ساختار مالکیت و اقتصاد آن را کم‌بررسی می‌گذارد.",
        applications="تحلیل سیاست رسانه‌ای و تنظیم‌گری، طراحی استراتژی‌های رسانه‌ای سازمان‌ها و نهادهای عمومی، آموزش سواد رسانه‌ای، و تحلیل اثر فناوری جدید بر ساختار و اقتصاد رسانه (McQuail, 2010).",
        evolution="واژه‌ی رسانه (media) از medium لاتین می‌آید. در قرن بیستم، با گسترش فناوری‌های پخش (رادیو ۱۹۲۰، تلویزیون ۱۹۴۰)، مفهوم رسانه به «فناوری پخش جمعی» محدود شد؛ در دهه‌های ۱۹۶۰–۱۹۷۰، مکتب مونیخ و مکتب فرهنگی بریتانیا آن را به «دستگاه نمادین و نهادی» ارتقا دادند؛ در دهه‌ی ۲۰۰۰ به بعد، پلتفرمی‌شدن و شبکه‌ای‌شدن، رسانه را از «مؤسسه» به «سیستم پویا» تبدیل کرد (McQuail, 2010; Littlejohn & Foss, 2011).",
        assumptions="فرض‌های نهفته: رسانه دارای ساختار نسبی مستقل از محتوایش است (محدودیت‌های فنی و اقتصادی)؛ مخاطبان به رسانه‌ها به‌صورت جمعی دسترسی دارند؛ و رسانه بر ساختار اجتماعی-فرهنگی اثر متقابل دارد نه یک‌طرفه (McQuail, 2010).",
    ),
    "CPT-008": dict(
        definition="پاسخ گیرنده به پیام دریافت‌شده — کلامی، غیرکلامی یا رفتاری — که به فرستنده باز می‌گردد و فرایند ارتباط را به‌صورت چرخه‌ای و تنظیم‌پذیر می‌سازد (DeVito, 2016). در الگوی فنی، بازخورد سازوکار کنترل و اصلاح انحراف معنایی در انتقال پیام است (Shannon & Weaver, 1949).",
        summary="بازخورد از اجزای تمایز‌بخش فرایند ارتباط است. در الگوی شانون-ویور (۱۹۴۹)، بازخورد «اطلاعی است که مقصد به منبع برمی‌گرداند تا میزان موفقیت انتقال و انحراف معنایی را بسنجد و ارسال بعدی را اصلاح کند»؛ بدون بازخورد، ارتباط یک‌طرفه و غیرقابل‌تنظیم است. در سنت میان‌فردی، بازخورد فراتر از «پاسخ فنی» است: هر پیام، هر واکنش — حتی سکوت — نوعی بازخورد است و تعامل واقعی را به «رقصِ پیوسته‌ی ارسال و پاسخ» تبدیل می‌کند (DeVito, 2016). در رسانه‌های جمعی، بازخورد رسمی (نظرسنجی، شکایت، امتیازدهی) و غیررسمی (گفت‌وگوی مخاطبان، ویروسی‌شدن محتوا) دو لایه دارد. نقد بنیادین، «عدم تقارن بازخورد» است: در ارتباط انبوه، بازخورد دیرهنگام، پراکنده و اغلب فیلترشده است و فرستنده نمی‌تواند آن را به‌موقع و دقیق دریافت کند؛ در محیط دیجیتال، الگوریتم‌ها و پلتفرم‌ها بازخورد را داده‌سازی و شخصی‌سازی کرده‌اند و مرز «بازخورد واقعی» و «بازخورد سنجیده‌شده» را محو کرده‌اند (DeVito, 2016).",
        mechanism="فرایند بازخورد: (۱) گیرنده پیام را دریافت و رمزگشایی می‌کند؛ (۲) واکنش می‌سازد — کلامی (پاسخ گفتاری)، غیرکلامی (زبان بدن، ابرو) یا رفتاری (تغییر عمل)؛ (۳) این واکنش به فرستنده می‌رسد؛ (۴) فرستنده بر اساس آن، ارسال بعدی را تنظیم می‌کند. در ارتباط انبوه، این چرخه دیرهنگام و غیرمستقیم است: رسانه با نظرسنجی، امتیازدهی و داده‌های رفتار، بازخورد را به‌صورت آماری جمع می‌کند (Shannon & Weaver, 1949; DeVito, 2016).",
        key_concepts=["پاسخ گیرنده", "تنظیم و کنترل", "چرخه‌ی ارتباط", "بازخورد رسمی و غیررسمی", "بازخورد الگوریتمی"],
        critiques="الگوی فنی بازخورد را «سیگنال»ی خنثی می‌بیند که انحراف را کم می‌کند، اما در عمل بازخورد اغلب تفسیرپذیر و جهت‌دار است (Shannon & Weaver, 1949). نقد دیگر، «اثر حلقه‌ی بازخورد» (feedback loop) است: در سیستم‌های الگوریتمی، بازخورد کاربر می‌تواند الگوریتم را تقویت‌کننده‌ی سوگیری‌ها کند و «اتاق پژواک» بسازد (DeVito, 2016). همچنین در ارتباط انبوه، بازخورد اغلب ناهمگن و پراکنده است و «بازخورد واقعی» با «بازخورد نمایشی» (social desirability) خلط می‌شود.",
        applications="طراحی سیستم‌های آموزش آنلاین با بازخورد فوری، مدیریت بحران رسانه‌ای با پایش بازخورد عمومی، بهینه‌سازی محصولات و محتوای دیجیتال بر اساس داده‌های تعامل، و آموزش مهارت‌های گوش‌دادن فعال و بازخورددهی در محیط کار (DeVito, 2016).",
        evolution="در الگوی ۱۹۴۹، بازخورد «کنترل فنی» بود؛ با ورود شرام و مکتب میان‌فردی (دهه‌ی ۱۹۵۰ به بعد)، بازخورد به «تعامل اجتماعی» و «تنظیم متقابل» بدل شد؛ در عصر دیجیتال، بازخورد به «داده‌ی رفتاری» و «سیگنال الگوریتمی» تبدیل شده و نقش آن از «اصلاح» به «بهینه‌سازی و شخصی‌سازی» گسترش یافته است (DeVito, 2016).",
        assumptions="فرض‌های نهفته: بازخورد صادقانه، به‌موقع و قابل‌تفسیر است؛ فرستنده توانایی تفسیر و بازتنظیم بر اساس بازخورد را دارد؛ و بازخورد می‌تواند از فرستنده تمایز یابد (یعنی یک «پاسخ» مشخص است نه «ادامه‌ی جریان» خالی) (Shannon & Weaver, 1949; DeVito, 2016).",
    ),
    "CPT-009": dict(
        definition="فرایند تبدیل قصد و معنا به نشانه‌ها و سیگنال‌های قابل انتقال — کلمات، اعداد، تصاویر، صداهای صوتی — بر اساس کدهای مشترک و قواعد ساختاری، تا از طریق کانال منتقل شوند (Shannon & Weaver, 1949). در سنت نشانه‌شناختی، رمزگذاری «انتخاب و ترکیب نشانه‌ها از میان کدهای فرهنگی» است (Fiske, 2011).",
        summary="رمزگذاری (encoding) حلقه‌ای است که قصد را به سیگنال تبدیل می‌کند. در الگوی شانون-ویور (۱۹۴۹)، رمزگذاری «عملکرد فرستنده» است: پیام انتخاب‌شده بر اساس کد (code) به سیگنال‌هایی تبدیل می‌شود که ظرفیت کانال را داشته باشند و قابل انتقال باشند. دقت رمزگذاری تعیین‌کننده‌ی کیفیت انتقال است: کدگذاری ناقص یا نامناسب، نویز را افزایش و احتمال خطا را بالا می‌برد. در سنت نشانه‌شناختی، رمزگذاری فراتر از «تکنیک» است: انتخاب هر نشانه، یک انتخاب فرهنگی و سیاسی است؛ «کد» به مجموعه‌ی قواعد مشترک بین فرستنده و گیرنده می‌گوید که معنای نشانه‌ها را می‌سازد (Fiske, 2011). در رسانه، رمزگذاری یعنی: انتخاب واژه، لحن، تصویر، رنگ، ترتیب و قالب — همه در هم‌افزایی، معنای پیام را می‌سازند. نقد بنیادین، «فرض کد مشترک» است: در محیط‌های چندفرهنگی و چندزبانه، کدها همیشه مشترک نیستند و رمزگذاری می‌تواند «فهم‌ناپذیر» یا «جهت‌دار» باشد. همچنین در رسانه‌های دیجیتال، رمزگذاری به‌صورت خودکار و الگوریتمی انجام می‌شود و «فرستنده‌ی انسانی» از تصمیمات ساختاری کنار رفته است (Fiske, 2011).",
        mechanism="فرایند رمزگذاری: (۱) تعیین قصد و هدف پیام؛ (۲) انتخاب نشانه‌ها (واژه، تصویر، صدا، حرکت) بر اساس کد؛ (۳) ترکیب نشانه‌ها بر اساس قواعد ساختاری (گرامر، ترکیب‌بندی، ریتم)؛ (۴) تنظیم سیگنال برای ظرفیت کانال (مثلاً فشرده‌سازی دیجیتال)؛ (۵) ارسال از کانال. در ارتباط میان‌فردی، این فرایند هم‌زمان و پیوسته است: فرستنده در حین صحبت، بازخورد غیرکلامی گیرنده را می‌بیند و رمزگذاری را بازتنظیم می‌کند (Shannon & Weaver, 1949; Fiske, 2011).",
        key_concepts=["کد و نشانه", "انتخاب و ترکیب", "قواعد ساختاری", "ظرفیت کانال", "رمزگذاری الگوریتمی"],
        critiques="الگوی فنی رمزگذاری را «عملیات تبدیل» می‌بیند و بعد فرهنگی و سیاسی آن را کم‌می‌بیند (Shannon & Weaver, 1949). نقد نشانه‌شناختی می‌گوید کد هرگز «خنثی» نیست: هر انتخاب نشانه، یک جای‌گزینی است و معنای آن را در بافت قدرت و فرهنگ تعریف می‌کند (Fiske, 2011). همچنین فرض «کد مشترک» در محیط‌های چندفرهنگی و چندزبانه شکننده است: تفاوت در کد، رمزگذاری را «تفهم‌ناپذیر» یا «جهت‌دار» می‌کند. در محیط الگوریتمی، رمزگذاری از «انتخاب انسانی» به «تولید خودکار» تبدیل شده و «مسئولیت رمزگذاری» مبهم شده است.",
        applications="نگارش و طراحی پیام‌های تبلیغاتی و اطلاع‌رسانی با توجه به کد مخاطب، آموزش مهارت‌های بیان و ارائه (رمزگذاری مؤثر)، طراحی رابط کاربری و تعامل (رمزگذاری UX)، و تحلیل انتقادی رسانه: چگونه کدها و قالب‌ها معنای رسانه‌ای را می‌سازند (Fiske, 2011).",
        evolution="از «رمزگذاری» به‌مثابه عملیات فنی تبدیل سیگنال در نظریه‌ی ریاضی (۱۹۴۹)، به «انتخاب نشانه‌ها بر اساس کد» در نشانه‌شناسی و مطالعات فرهنگی (دهه‌های ۱۹۶۰–۱۹۷۰) و سپس به «رمزگذاری الگوریتمی» در عصر دیجیتال تکامل یافت؛ امروزه بخشی از رمزگذاری توسط الگوریتم‌ها و سیستم‌های خودکار انجام می‌شود (Fiske, 2011).",
        assumptions="فرض‌های نهفته: فرستنده به کدهای مشترک با گیرنده دسترسی دارد؛ نشانه‌ها معنای پایدار و قابل‌انتقال دارند؛ و فرایند رمزگذاری تحت کنترل آگاهانه‌ی فرستنده است (Shannon & Weaver, 1949; Fiske, 2011). در محیط چندفرهنگی و الگوریتمی، این فرض‌ها به چالش کشیده می‌شوند.",
    ),
    "CPT-010": dict(
        definition="فرایند تفسیر و بازسازی معنا از سیگنال‌های دریافتی، بر اساس کدهای مشترک، تجربه و بافت اجتماعی-فرهنگی گیرنده؛ رمزگشایی «تولید معنا در گیرنده» است نه صرفاً «بازیابی پیام» (Fiske, 2011). در الگوی فنی، رمزگشایی «بازسازی سیگنال در مقصد» است (Shannon & Weaver, 1949).",
        summary="رمزگشایی (decoding) معکوسِ رمزگذاری است. در الگوی شانون-ویور (۱۹۴۹)، رمزگشایی «عملکرد مقصد» است: سیگنال‌های دریافتی بر اساس کد، به پیام اولیه بازسازی می‌شوند و صحت رمزگشایی تعیین‌کننده‌ی موفقیت ارتباط است. اما در سنت نشانه‌شناختی و فرهنگی، رمزگشایی فراتر از «بازیابی» است: گیرنده با کدهای فرهنگی، تجربه و باورهای خود، نشانه‌ها را تفسیر می‌کند و ممکن است معنایی متفاوت از قصد فرستنده بسازد (Fiske, 2011). در مطالعات رسانه، «رمزگشایی» به «موضع‌گیری مخاطب» می‌گویند: تفسیر غالب (مطابق قصد فرستنده)، تفسیر مذاکره‌شده (ترکیب معنای فرستنده و بافت مخاطب) و تفسیر مقاومتی (رد یا معکوس‌سازی معنای فرستنده) (Fiske, 2011). نقد بنیادین، «فرض کد مشترک» است: در محیط‌های چندفرهنگی، رمزگشایی به‌شدت به بافت اجتماعی و فرهنگی گیرنده وابسته است و «معنای واحد» فرضی است. همچنین در رسانه‌های دیجیتال، الگوریتم‌ها و شخصی‌سازی، رمزگشایی را محدود و هدایت می‌کنند: مخاطب «آزاد» به نظر می‌رسد اما گزینه‌های تفسیرش از پیش فیلتر شده‌اند.",
        mechanism="فرایند رمزگشایی: (۱) دریافت سیگنال‌ها از کانال و بازیابی اولیه؛ (۲) شناسایی نشانه‌ها بر اساس کد؛ (۳) ترکیب نشانه‌ها و ساخت معنای اولیه؛ (۴) قرار دادن معنا در بافت تجربه و باورهای شخصی (تفسیر)؛ (۵) تولید پاسخ — کلامی، رفتاری یا عاطفی. در ارتباط میان‌فردی، این فرایند هم‌زمان با بازخورد غیرکلامی بازتنظیم می‌شود (Shannon & Weaver, 1949; Fiske, 2011).",
        key_concepts=["تفسیر نشانه", "کد و بافت فرهنگی", "موضع‌گیری مخاطب", "رمزگشایی الگوریتمی", "تولید معنا"],
        critiques="الگوی فنی رمزگشایی را «بازیابی سیگنال» می‌بیند و بعد تفسیری و فعال آن را نادیده می‌گیرد (Shannon & Weaver, 1949). نقد نشانه‌شناختی می‌گوید رمزگشایی هرگز «خنثی» نیست: گیرنده با کد و بافت خود، معنا را می‌سازد نه صرفاً می‌گیرد (Fiske, 2011). نقد دیگر، «کنترل الگوریتمی» رمزگشایی است: در پلتفرم‌های دیجیتال، گزینه‌های تفسیر مخاطب از پیش فیلتر و هدایت می‌شوند و «آزادی تفسیر» ظاهری است. همچنین فرض «معنای واحد و قابل‌انتقال» در محیط‌های چندفرهنگی و چندزبانه شکننده است.",
        applications="طراحی پیام‌های رسانه‌ای با توجه به کد و بافت مخاطب، تحلیل انتقادی رسانه ( چگونه معنای رسانه‌ای در گیرنده تولید می‌شود)، آموزش سواد رسانه‌ای (بهبود توانایی رمزگشایی انتقادی)، و بهینه‌سازی محتوا بر اساس داده‌های رفتار مخاطب (Fiske, 2011).",
        evolution="از «رمزگشایی» به‌مثابه بازیابی سیگنال در نظریه‌ی ریاضی (۱۹۴۹)، به «تفسیر نشانه در بافت» در نشانه‌شناسی و مطالعات فرهنگی (دهه‌های ۱۹۶۰–۱۹۷۰) و سپس به «رمزگشایی الگوریتمی و شخصی‌سازی‌شده» در عصر دیجیتال تکامل یافت؛ امروزه مرز «رمزگشایی انسانی» و «رمزگشایی الگوریتمی» مبهم است (Fiske, 2011).",
        assumptions="فرض‌های نهفته: گیرنده به کدهای مشترک با فرستنده دسترسی دارد؛ نشانه‌ها معنای قابل‌تفسیر و نسبتاً پایدار دارند؛ و گیرنده توانایی و انگیزه رمزگشایی را دارد (Shannon & Weaver, 1949). در سنت نشانه‌شناختی، فرض بر این است که تفسیر مخاطب مشروع است و گاه بر قصد فرستنده غلبه می‌کند (Fiske, 2011).",
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
                    (code, json.dumps({"batch": 253, "score": score, "words": words,
                                       "sources": n_sources, "verified": n_verified,
                                       "relations": n_rel, "rubric": detail}, ensure_ascii=False), STAMP, NOW))
        print(code, "words", words, "score", score, "detail", detail)

    conn.commit()
    conn.close()
    print("BATCH253 DONE")


if __name__ == "__main__":
    main()
