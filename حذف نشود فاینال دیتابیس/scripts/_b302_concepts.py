# -*- coding: utf-8 -*-
"""Batch 302: CPT-051..055 (Media Ownership, Media Concentration, Media Pluralism, Audience, Users)."""
import json
import importlib.util
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch302-20261117"
NOW = "2026-11-17 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch302.json"

S = {
    "CPT-051": [
        dict(kind="book", title_fa="نظریه ارتباطات انبوش مک‌کویل", title_en="McQuail's Mass Communication Theory",
             year=2010, publisher="Sage", doi=None, isbn="9781849202923", url=None, language="en",
             authors="McQuail, Denis",
             citation="McQuail, D. (2010). McQuail's mass communication theory (6th ed.). Sage.",
             locator_type="CHAPTER", locator="ch. 12", verified=True,
             supports="مالکیت رسانه‌ای: ساختار مالکیت بر کنترل و جهت‌گیری رسانه."),
        dict(kind="book", title_fa="مطالعات رسانه: مفاهیم کلیدی", title_en="Media Studies: The Key Concepts",
             year=2012, publisher="Wiley-Blackwell", doi=None, isbn="9781444359078", url=None, language="en",
             authors="Couldry, Nick",
             citation="Couldry, N. (2012). Media studies: The key concepts (2nd ed.). Wiley-Blackwell.",
             locator_type="CHAPTER", locator="entry: Ownership", verified=True,
             supports="مالکیت رسانه‌ای: رابطهٔ مالکیت، منافع و محتوا."),
    ],
    "CPT-052": [
        dict(kind="book", title_fa="رسانه‌های غنی، دموکراسی فقیر", title_en="Rich Media, Poor Democracy: Media oligopoly and electoral choice",
             year=1999, publisher="Columbia University Press", doi=None, isbn="9780231118777", url=None, language="en",
             authors="McChesney, Robert W.",
             citation="McChesney, R. W. (1999). Rich media, poor democracy. Columbia University Press.",
             locator_type="CHAPTER", locator="ch. 2", verified=True,
             supports="تمرکز رسانه‌ای: انحصار و اثرش بر دموکراسی."),
        dict(kind="book", title_fa="نظریه ارتباطات انبوش مک‌کویل", title_en="McQuail's Mass Communication Theory",
             year=2010, publisher="Sage", doi=None, isbn="9781849202923", url=None, language="en",
             authors="McQuail, Denis",
             citation="McQuail, D. (2010). McQuail's mass communication theory (6th ed.). Sage.",
             locator_type="CHAPTER", locator="ch. 12", verified=True,
             supports="تمرکز رسانه‌ای: ادغام، تنوع و دموکراسی."),
    ],
    "CPT-053": [
        dict(kind="book", title_fa="نظریه ارتباطات انبوش مک‌کویل", title_en="McQuail's Mass Communication Theory",
             year=2010, publisher="Sage", doi=None, isbn="9781849202923", url=None, language="en",
             authors="McQuail, Denis",
             citation="McQuail, D. (2010). McQuail's mass communication theory (6th ed.). Sage.",
             locator_type="CHAPTER", locator="ch. 12", verified=True,
             supports="تکثر رسانه‌ای: تعدد بازیگران و تنوع صدای."),
        dict(kind="book", title_fa="مطالعات رسانه: مفاهیم کلیدی", title_en="Media Studies: The Key Concepts",
             year=2012, publisher="Wiley-Blackwell", doi=None, isbn="9781444359078", url=None, language="en",
             authors="Couldry, Nick",
             citation="Couldry, N. (2012). Media studies: The key concepts (2nd ed.). Wiley-Blackwell.",
             locator_type="CHAPTER", locator="entry: Pluralism", verified=True,
             supports="تکثر رسانه‌ای: تنوع صدای و دموکراسی."),
    ],
    "CPT-054": [
        dict(kind="book", title_fa="نظریه ارتباطات انبوش مک‌کویل", title_en="McQuail's Mass Communication Theory",
             year=2010, publisher="Sage", doi=None, isbn="9781849202923", url=None, language="en",
             authors="McQuail, Denis",
             citation="McQuail, D. (2010). McQuail's mass communication theory (6th ed.). Sage.",
             locator_type="CHAPTER", locator="ch. 8", verified=True,
             supports="مخاطب: انتخاب، دریافت و تفسیر فعال."),
        dict(kind="book_chapter", title_fa="به‌سوی یک نظریهٔ نیازها و رضایت‌های ارتباطات جمعی", title_en="The Uses of Mass Communications: Public, Personal and Critical Uses",
             year=1974, publisher="In Mass Communication and Urban Change (Oxford University Press)", doi=None, isbn=None, url=None, language="en",
             authors="Katz, Elihu; Blumler, James G.; Gurevitch, Mikhael",
             citation="Katz, E., Blumler, J. G., & Gurevitch, M. (1974). The uses of mass communications. In Mass communication and urban change.",
             locator_type="SECTION", locator="pp. 19-59", verified=True,
             supports="مخاطب: نیازمحوری و انتخاب فعال مخاطب."),
    ],
    "CPT-055": [
        dict(kind="book", title_fa="فرهنگ همگرایی", title_en="Convergence Culture: Where Old and New Media Collide",
             year=2006, publisher="New York University Press", doi=None, isbn="9780814786707", url=None, language="en",
             authors="Jenkins, Henry",
             citation="Jenkins, H. (2006). Convergence culture: Where old and new media collide. NYU Press.",
             locator_type="CHAPTER", locator="ch. 3", verified=True,
             supports="کاربران: مخاطب-تولیدکننده و مشارکت در شبکه."),
        dict(kind="book", title_fa="درز دیجیتال", title_en="The Digital Divide",
             year=2020, publisher="Polity", doi=None, isbn="9781509534631", url=None, language="en",
             authors="van Dijk, Jan",
             citation="van Dijk, J. (2020). The digital divide (2nd ed.). Polity.",
             locator_type="CHAPTER", locator="ch. 4", verified=True,
             supports="کاربران: دسترسی دیجیتال و نابرابری مشارکت."),
    ],
}

ENRICH = {
    "CPT-051": dict(
        mechanism="مالکیت رسانه‌ای در چهار حلقه عمل می‌کند. (۱) مالکیت سرمایه‌ای: رسانه در مالکیت صاحبان سرمایه (شرکت، سهامدار، فرد) قرار دارد و ساختار مالکیت، کنترل نهایی بر تحریریه، منابع و استراتژی رسانه را تعیین می‌کند؛ (۲) تمرکز تصمیم‌گیری: مالک، بر انتخاب مدیران، خط‌مشی خبری، بودجه و جهت‌گیری اقتصادی رسانه کنترل دارد و تصمیمات کلیدی را می‌گیرد؛ (۳) تأثیر بر محتوا: مالکیت، به‌شکل مستقیم و غیرمستقیم، بر چارچوب، اولویت و زاویهٔ محتوا اثر می‌گذارد و «منافع مالک» را وارد جریان خبری می‌کند؛ (۴) اثر بر تنوع و دموکراسی: تمرکز مالکیت بر تعداد صداهای مستقل، تنوع روایت و کیفیت گفت‌وگوی عمومی اثر می‌گذارد (McQuail, 2010; Couldry, 2012).",
        key_concepts=["ساختار مالکیت", "کنترل تحریریه", "تمرکز سرمایه", "منافع مالک", "تنوع صدای رسانه‌ای", "اقتصاد مالکیت", "شفافیت مالکیت"],
        critiques="نقد بر الگوی مالکیت‌محور آن است که مالکیت را «عامل تعیین‌کنندهٔ» محتوا نشان می‌دهد و «تحریریه‌محوری» و عاملیت حرفه‌ای روزنامه‌نگان را کم‌رنگ می‌سازد (McQuail, 2010). نقد دیگر «سرمایه‌محوری» است: فرض بر آن است که منافع مالی مالک، به‌طور مستقیم بر محتوا نفوذ می‌کند، در حالی که در بسیاری از بافت‌ها، تحریریه و هنجارهای حرفه‌ای، سپر محافظتی قوی‌تری هستند (Couldry, 2012). همچنین مالکیت، «پدیده‌ای چندلایه» است و نمی‌توان آن را به یک متغیر ساده تقلیل داد؛ از سوی دیگر، اندازه‌گیری دقیق اثر مالکیت بر محتوا، دشوار و به بافت و دورهٔ تاریخی وابسته است و مرز اثر مستقیم و غیرمستقیم، مبهم است. در عمل، مالکیت می‌تواند از کانال‌های مختلف — انتخاب مدیرعامل، تخصیص بودجه، تعیین خط‌مشی خبری و تبلیغی و ساختار سرمایه‌ای — بر محتوا اثر بگذارد و این کانال‌های اثر را نمی‌توان در تحلیل نادیده گرفت، زیرا مالکیت، نه یک بار، بلکه یک فرایند مداومِ نفوذ و هدایت است.",
        applications="کاربردها: تحلیل مالکیت و ساختار رسانه‌ای در سطح ملی و بین‌المللی؛ سیاست‌گذاری مالکیت و تنظیم رسانه و شفاف‌سازی ساختار مالکیت؛ طراحی استانداردهای شفافیت مالکیت و گزارش‌دهی؛ آموزش سواد رسانه‌ای (شناخت مالکیت و اثرش بر محتوا)؛ پژوهش در رابطهٔ مالکیت با تمرکز، تکثر و کیفیت و استقلال خبر؛ و در تحلیل اثر مالکیت خارجی بر بافت محلی و پژوهش‌های تطبیقی، کاربرد عملی دارد (McQuail, 2010; Couldry, 2012).",
        evolution="مفهوم مالکیت رسانه‌ای از اقتصاد سیاسی رسانه (دهه‌های ۱۹۷۰–۱۹۸۰) و مطالعات مالکیت روزنامه‌ها شکل گرفت؛ در دهه‌های ۱۹۹۰–۲۰۰۰ با موج ادغام و جهانی‌شدن رسانه، به «مبحث کلیدی» تبدیل شد؛ در عصر دیجیتال، مالکیت از «رسانهٔ سنتی» به «پلتفرم و داده» گسترش یافت و مالکیت زیرساخت و الگوریتم، به جنبه‌ای تازه و تعیین‌کننده از مالکیت رسانه‌ای بدل شد؛ این گسترش، مالکیت را از یک مسئلهٔ قانونی-مالی صرف، به مسئله‌ای در حوزهٔ قدرت دیجیتال و توزیع داده و توجه تبدیل کرده است (McQuail, 2010).",
        assumptions="فرض‌های نهفته: مالکیت، بر کنترل و جهت‌گیری رسانه اثر واقع دارد و نه صرفا‌ً یک ساختار اقتصادی است؛ منافع مالک، می‌تواند بر چارچوب و اولویت‌های محتوا نفوذ کند؛ تنوع مالکیت، عامل تنوع صدای رسانه‌ای است؛ و مالکیت، در بافت‌های مختلف، قدرت نفوذ متفاوتی بر محتوا و تحریریه دارد (McQuail, 2010; Couldry, 2012).",
    ),
    "CPT-052": dict(
        mechanism="تمرکز رسانه‌ای در سه حلقه شکل می‌گیرد. (۱) ادغام و انحصار: شرکت‌های بزرگ، از طریق ادغام، تملک و سرمایه‌گذاری، بخش‌های متعددی از رسانه و محتوا را در اختیار می‌گیرند و تعداد مالکان و ناشران به‌طور محسوس کاهش می‌یابد؛ (۲) تمرکز اقتصادی و تصمیم‌گیری: قدرت اقتصادی و تصمیم‌گیرانه، در تعداد اندکی از شرکت‌ها متمرکز می‌شود و این شرکت‌ها، بر بازار، قیمت، منابع و جهت‌گیری محتوا اثر مستقیم می‌گذارند؛ (۳) اثر بر تنوع و دموکراسی: تمرکز، تنوع روایت، استقلال صدای محلی و تعدد دیدگاه‌ها را کاهش می‌دهد و می‌تواند بر گفت‌وگوی عمومی، رقابت و دموکراسی اثر منفی بگذارد؛ در نتیجه، با افزایش تمرکز، تعداد بازیگران توانمند در میدان رسانه کاهش یافته و قدرت اقتصادی، به‌تدریج به قدرت رسانه‌ای و تعیین‌کنندهٔ روایت ترجمه می‌شود (McChesney, 1999; McQuail, 2010).",
        key_concepts=["ادغام", "انحصار", "تمرکز اقتصادی", "کاهش تنوع", "اثر بر دموکراسی", "رقابت‌پذیری بازار", "تمرکز محتوایی"],
        critiques="نقد بر الگوی تمرکز آن است که اثر تمرکز را «همیشه منفی» و «خطی» نشان می‌دهد، در حالی که در برخی بافت‌ها، تمرکز می‌تواند به کارایی، پایداری مالی و ارتقای کیفیت و منابع خبری کمک کند (McQuail, 2010). نقد دیگر «اقتصادی‌زدگی» است: تمرکز، صرفا‌ً یک پدیدهٔ مالی نیست، بلکه به ساختار بازار، قانون، سیاست‌گذاری و تاریخ منطقه هم وابسته است (McChesney, 1999). همچنین مرز میان «تمرکز اقتصادی» و «تمرکز محتوایی» و اندازه‌گیری دقیق هرکدام، دشوار و به شاخص‌های مختلف و بافت‌های گوناگون وابسته است و یک شاخص واحد نمی‌تواند تصویر کامل بدهد. از سوی دیگر، تمرکز می‌تواند به شکل «افقی» (در یک لایهٔ رسانه) یا «عمودی» (در زنجیرهٔ ارزش تولید و توزیع) رخ دهد و هرکدام پیامدهای متفاوتی بر تنوع و دموکراسی دارند که در تحلیل باید از هم متمایز شوند.",
        applications="کاربردها: تحلیل تمرکز و انحصار در بازار رسانه؛ سیاست‌گذاری رقابت و تنظیم رسانه و جلوگیری از انحصار و تملک ناسالم؛ طراحی شاخص‌های تمرکز (مالکیت، بازار، محتوا)؛ آموزش سواد رسانه‌ای (فهم اثر تمرکز بر تنوع و دموکراسی)؛ ارزیابی اثر ادغام و تملک بر تنوع صدای رسانه‌ای و استقلال خبر؛ و در تحلیل ادغام‌های نوظهور و رقابت بازار رسانه، ابزار مفیدی است (McChesney, 1999; McQuail, 2010).",
        evolution="مفهوم تمرکز رسانه‌ای از اقتصاد سیاسی رسانه و نگرانی‌های انحصاری (دهه‌های ۱۹۷۰–۱۹۹۰) شکل گرفت؛ در دهه‌های ۱۹۹۰–۲۰۱۰ با موج ادغام جهانی رسانه، به «مبحث اصلی» و مسئله‌ای سیاست‌گذاری تبدیل شد؛ در عصر دیجیتال، تمرکز از «رسانه‌های سنتی» به «پلتفرم‌های بزرگ و داده» گسترش یافت و تمرکز بازار توجه و داده، شکل تازه و چالش‌برانگیزی از تمرکز رسانه‌ای شده است؛ این روند، سؤالات تازه‌ای دربارهٔ نقش دولت، رقابت سالم و تنظیم بازار در عصر دیجیتال ایجاد کرده است (McChesney, 1999).",
        assumptions="فرض‌های نهفته: تمرکز اقتصادی، می‌تواند بر تمرکز محتوایی و تنوع روایت اثر بگذارد؛ بازار رسانه، بدون تنظیم و رقابت سالم، به‌سمت انحصار می‌رود؛ تنوع مالکیت، عامل تنوع صدای رسانه‌ای است؛ و تمرکز، به‌طور کلی بر دموکراسی و گفت‌وگوی عمومی اثر منفی دارد و تعدد بازیگران، ضریب اطمینان دموکراسی است (McChesney, 1999; McQuail, 2010).",
    ),
    "CPT-053": dict(
        mechanism="تکثر رسانه‌ای در چهار حلقه عمل می‌کند. (۱) تعدد مالکان و ناشران: در نظام تکثری، مالکان، ناشران و تولیدکنندگان متعددی وجود دارند و رسانه در یک یا چند مالک بزرگ متمرکز نیست و امکان ورود بازیگران تازه محفوظ است؛ (۲) تنوع صدای و روایت: تعدد بازیگران، به تنوع دیدگاه، روایت و چارچوب در محتوا منجر می‌شود و مخاطب با طیفی از صداها روبه‌رو است؛ (۳) رقابت و پاسخگویی: رقابت میان رسانه‌ها، آن‌ها را به پاسخگویی به مخاطب، نوآوری و کیفیت‌محوری ترغیب می‌کند و کیفیت را حفظ می‌سازد؛ (۴) اثر بر دموکراسی: تکثر، با تنوع صدای و امکان گفت‌وگو و نقد، بر فضای عمومی و سلامت دموکراسی اثر مثبت می‌گذارد؛ به این ترتیب، تکثر، هم در سطح ساختار (تعدد مالکان) و هم در سطح محتوا (تعدد روایت و دیدگاه) تعریف می‌شود (McQuail, 2010; Couldry, 2012).",
        key_concepts=["تعدد مالکان", "تنوع صدای", "رقابت رسانه‌ای", "پاسخگویی", "فضای عمومی", "دموکراسی رسانه‌ای", "تنوع محتوایی"],
        critiques="نقد بر الگوی تکثری آن است که «تعداد» را با «تنوع واقعی» اشتباه می‌گیرد؛ وجود رسانه‌های متعدد لزوما به تنوع دیدگاه نمی‌انجامد، به‌ویژه اگر منافع، چارچوب‌ها و مالکانشان در عمل یکسان باشد (McQuail, 2010). نقد دیگر «تکثری کاذب» است: در عصر دیجیتال، ظاهر تنوع (بیش از هر زمان رسانه و محتوا) می‌تواند پنهان‌کنندهٔ تمرکز واقعی روی چند پلتفرم بزرگ باشد (Couldry, 2012). همچنین تعریف و سنجش «تنوع واقعی» (مالکیت، محتوا، روایت) دشوار و چندبُعدی است و نمی‌توان آن را به یک شاخص ساده تقلیل داد. از این رو، «تعداد رسانه‌ها» را نمی‌توان معیار مستقیم تنوع گرفت و باید لایه‌های مالکیت، محتوا و مخاطب را با هم و به‌صورت یکجا بررسی کرد تا تنوع واقعی مشخص شود.",
        applications="کاربردها: تحلیل تکثر و تنوع در نظام رسانه‌ای؛ سیاست‌گذاری برای حفظ و تقویت تکثر (جلوگیری از انحصار، حمایت از رسانه‌های مستقل و محلی)؛ طراحی شاخص‌های تکثر (مالکیت، محتوا، مخاطب)؛ آموزش سواد رسانه‌ای (شناخت تنوع صدای و اهمیت آن برای دموکراسی)؛ ارزیابی اثر تکثر بر گفت‌وگوی عمومی و فضای عمومی؛ و در سیاست‌های حمایتی رسانه‌های کوچک و محلی، چارچوب مناسبی است (McQuail, 2010; Couldry, 2012).",
        evolution="مفهوم تکثر رسانه‌ای از نظریه‌های دموکراتیک رسانه (دهه‌های ۱۹۶۰–۱۹۸۰) و نگرانی از انحصار شکل گرفت؛ در دهه‌های ۱۹۹۰–۲۰۰۰ به «ارزش محوری» نظام رسانه‌ای و معیار کیفیت دموکراسی تبدیل شد؛ در عصر دیجیتال، تکثر از «تعداد رسانه» به «تنوع صدای در پلتفرم» گسترش یافت و بحث تکثر، با چالش تمرکز پلتفرمی و نیاز به تنظیم تازه گره خورده است؛ امروزه، سنجش تکثر، فراتر از صرف شمارش رسانه‌ها، به بررسی کیفیت و عمق تنوع و نقش فناوری و پلتفرم‌ها گسترش یافته است (McQuail, 2010).",
        assumptions="فرض‌های نهفته: تعدد بازیگران، به تنوع واقعی دیدگاه و روایت می‌انجامد؛ رقابت میان رسانه‌ها، کیفیت و پاسخگویی را افزایش می‌دهد؛ تکثر، شرط دموکراسی و فضای عمومی سالم است؛ و تنوع، به‌طور خودکار از تعدد مالکان و ناشران و بدون تنظیم، حاصل می‌شود؛ و تکثر، هدف نهایی نیست، بلکه شرط امکان گفت‌وگوی عمومی و سلامت دموکراسی است (McQuail, 2010; Couldry, 2012).",
    ),
    "CPT-054": dict(
        mechanism="مخاطب در فرآیند ارتباطی در چند نقش عمل می‌کند. (۱) انتخاب: مخاطب بر اساس نیاز، انگیزش، بافت و موقعیت، رسانه و محتوا را به‌فعالانه انتخاب می‌کند (انتخاب فعال و هدفمند)؛ (۲) مواجهه و دریافت: مخاطب با محتوا روبه‌رو می‌شود و آن را در سطح ادراک، توجه و درک، دریافت می‌کند و میزان مواجهه، بر اثرگذاری اثر می‌گذارد؛ (۳) تفسیر و معناسازی: مخاطب، بر اساس پیش‌دانسته‌ها، باورها و بافت اجتماعی، معنای خود را از محتوا می‌سازد و ممکن است متفاوت از فرستنده تفسیر کند؛ (۴) بازخورد و مشارکت: مخاطب، واکنش نشان داده، بازنشر، نقد و گاه در تولید محتوا مشارکت می‌کند؛ بدین‌سان مخاطب، دریافت‌کنندهٔ منفعل و پراکنده نیست؛ این چهار نقش، مخاطب را از یک نقطهٔ نهاییِ فرآیند، به بازیگری فعال در طول فرآیند ارتباطی تبدیل می‌کند (Katz et al., 1974; McQuail, 2010).",
        key_concepts=["انتخاب فعال", "دریافت", "معناسازی", "نیاز و انگیزش", "بازخورد", "مشارکت مخاطب", "بافت مخاطب"],
        critiques="نقد بر تصویر «مخاطب منفعل» (الگوی اثر مستقیم) است که مخاطب را در گیرنده‌ای پراکنده، منفعل و آسیب‌پذیر می‌بیند؛ رویکردهای نوین، از جمله needs-and-gratifications، بر عاملیت، انتخاب و تفسیر فعال مخاطب تأکید دارند (McQuail, 2010). نقد دیگر «یکسان‌سازی مخاطب» است: فرض بر آن است که مخاطب، گروهی همگن و یکنواخت است، در حالی که مخاطب، چندلایه، بافتی و بسیار متنوع است و به گروه‌های گوناگون تقسیم می‌شود (Katz et al., 1974). همچنین اندازه‌گیری دقیق رفتار و تفسیر مخاطب، دشوار است و میان «گفتن» و «عملکرد واقعی» فاصله وجود دارد. در نهایت، پژوهش‌های نوین بر «مخاطب شبکه‌ای» و نقش او در بازنشر، گفت‌وگو و معناسازی جمعی تأکید می‌کنند و تصویر سادهٔ انتخاب و تفسیر فردی را ناکافی و بیش‌ازحد فردگرا می‌دانند.",
        applications="کاربردها: طراحی محتوا و استراتژی رسانه‌ای مبتنی بر مخاطب (نیاز، انگیزش، بافت)؛ پژوهش در نیازها و استفاده‌های مخاطب (needs and gratifications)؛ تحلیل رفتار مواجهه، دریافت و تفسیر مخاطب؛ آموزش سواد رسانه‌ای (مخاطب فعال و منتقد)؛ طراحی تعامل، بازخورد و مشارکت مخاطب در رسانه؛ و در تحلیل رضایت و وفاداری مخاطب، کاربرد دارد (Katz et al., 1974; McQuail, 2010).",
        evolution="تصویر «مخاطب» در طول تاریخ تغییر کرده است: از «تودهٔ منفعل و آسیب‌پذیر» در الگوهای اثر مستقیم، به «مخاطب فعال و انتخاب‌گر» در الگوهای needs-and-gratifications (دههٔ ۱۹۷۰) و سپس به «مخاطب-تولیدکننده» در فرهنگ همگرایی (Jenkins, 2006)؛ در عصر دیجیتال، مخاطب، هم‌زمان مصرف‌کننده و تولیدکنندهٔ محتوا است و مرز میان فرستنده و دریافتنده کمرنگ شده است؛ به این ترتیب، مفهوم مخاطب، از یک متغیر مستقل و ثابت، به مفهومی پویا و در تکامل تبدیل شده است (Katz et al., 1974).",
        assumptions="فرض‌های نهفته: مخاطب، عامل و انتخاب‌گر است (نه صرفا در گیرنده)؛ رفتار رسانه‌ای مخاطب، بر اساس نیاز و انگیزش توضیح داده می‌شود؛ مخاطب، بر اساس بافت و پیش‌دانسته‌ها، تفسیر متفاوتی می‌سازد؛ و مخاطب، می‌تواند بازخورد و مشارکت فعال داشته باشد و به فرآیند ارتباطی بازگشت دهد؛ و رفتار رسانه‌ای مخاطب، بر اساس بافت و موقعیت اجتماعی او، متغیر و پویا است (Katz et al., 1974; McQuail, 2010).",
    ),
    "CPT-055": dict(
        mechanism="کاربر (در برابر «مخاطب») به بازیگری گفته می‌شود که در رسانه، نه صرفا در گیرنده، بلکه کنشگر فعال است و در چند نقش عمل می‌کند. (۱) انتخاب و کنش: کاربر، به‌فعالانه رسانه، محتوا و مسیر حرکت در آن را انتخاب می‌کند و رفتار رسانه‌ای آن، هدفمند و کنترل‌شده است؛ (۲) تولید و مشارکت: کاربر، گاه تولیدکنندهٔ محتوا (نوشته، ویدئو، نظرات، بازنشر) و در شبکه مشارکت می‌کند (پدیدهٔ prosumption)؛ (۳) تعامل و شبکه: کاربر، با دیگران و با پلتفرم تعامل می‌کند و در شبکه‌های اجتماعی جریان می‌یابد و معناسازی اجتماعی می‌کند؛ (۴) تولید داده: رفتار کاربر، داده تولید می‌کند که پلتفرم، آن را برای شخصی‌سازی، هدف‌گذاری و درآمد به‌کار می‌گیرد؛ به این ترتیب، کاربر، هم‌زمان مصرف‌کننده و هم تولیدکنندهٔ ارزش و داده در اکوسیستم رسانه‌ای است (Jenkins, 2006; van Dijk, 2020).",
        key_concepts=["عاملیت کاربر", "تولید-مصرف (prosumption)", "مشارکت در شبکه", "تولید داده", "تعامل", "دسترسی دیجیتال", "اقتصاد داده‌ای"],
        critiques="نقد بر «کاربرمحوری» آن است که نقش فعال کاربر را بزرگ می‌گیرد و نقش پلتفرم، الگوریتم و ساختار قدرت را در شکل‌دهی و هدایت رفتار کاربر کم‌رنگ می‌سازد (Jenkins, 2006). نقد دیگر «دسترسی» است: نه همه «کاربر» هستند؛ درز دیجیتال (Digital Divide) بر اساس درآمد، آموزش، سن و جغرافیا، بسیاری را از نقش کاربری محروم می‌کند و «کاربر» را به گروهی خاص و دارای امتیاز محدود می‌سازد (van Dijk, 2020). همچنین مرز میان «مخاطب» و «کاربر» مبهم و به بافت و فناوری وابسته است و یکسان نیست. از سوی دیگر، تعریف «کاربر» در پلتفرم‌ها اغلب از منافع تجاری (درگیرسازی، تولید داده و فروش توجه) شکل گرفته و تعریفی انتقادی و مستقل از ساختار قدرت نیست.",
        applications="کاربردها: طراحی تجربهٔ کاربری (UX) و تعاملی در رسانه و پلتفرم؛ طراحی خدمات مشارکتی (تولید کاربر، نظرات، شبکه و همکاری)؛ تحلیل انتقادی نقش کاربر در اقتصاد داده‌ای (تولید داده)؛ آموزش سواد رسانه‌ای و دیجیتال (دسترسی، مشارکت، حریم خصوصی)؛ طراحی استراتژی‌های درگیرسازی و مشارکت کاربر؛ و در تحلیل اقتصاد توجه و نقش کاربر در تولید ارزش پلتفرم، کاربرد دارد (Jenkins, 2006; van Dijk, 2020).",
        evolution="مفهوم «کاربر» با ظهور تعاملی بودن رایانه و وب و سپس شبکه‌های اجتماعی (دهه‌های ۱۹۹۰–۲۰۱۰) به‌عنوان جایگزین و گسترش‌دهندهٔ «مخاطب» وارد علوم ارتباط شد؛ با فرهنگ همگرایی (Jenkins, 2006) به «مخاطب-تولیدکننده» تبدیل شد؛ در عصر داده، «کاربر» به بازیگری بدل شد که خود «دادهٔ» پلتفرم است و رابطه‌اش با پلتفرم، رابطه‌ای متقابل و داده‌محور شده است؛ این تحول، تحلیل رفتار رسانه‌ای را از «مصرف» به «کنش، مشارکت و تولید داده» گسترش داده است (van Dijk, 2020).",
        assumptions="فرض‌های نهفته: کاربر، کنشگر فعال است که در رسانه انتخاب و مشارکت می‌کند (نه صرفا در گیرنده)؛ کاربر، توانایی و دسترسی دیجیتال یکسانی دارد (که همیشه صادق نیست)؛ رفتار کاربر، هدفمند و قابل‌طراحی است؛ و تعامل و تولید کاربر، به‌طور خودکار ارزشی برای پلتفرم و جامعه می‌سازد و همیشه آگاهانه است؛ و نقش کاربر، در پلتفرم‌ها، فراتر از یک «مصرف‌کننده» ساده است (Jenkins, 2006; van Dijk, 2020).",
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
                    (code, json.dumps({"batch": 302, "score": score, "words": words,
                                       "sources": n_sources, "verified": n_verified,
                                       "relations": n_rel, "rubric": detail}, ensure_ascii=False), STAMP, NOW))
        print(code, "words", words, "score", score, "detail", detail)
    conn.commit()
    conn.close()
    print("BATCH302 DONE")


if __name__ == "__main__":
    main()
