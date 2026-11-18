# -*- coding: utf-8 -*-
"""Batch 303: CPT-056..060 (Media Consumption, Media Selection, Media Exposure, Attention, Perception)."""
import json
import importlib.util
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch303-20261117"
NOW = "2026-11-17 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch303.json"

S = {
    "CPT-056": [
        dict(kind="book", title_fa="نظریه ارتباطات انبوش مک‌کویل", title_en="McQuail's Mass Communication Theory",
             year=2010, publisher="Sage", doi=None, isbn="9781849202923", url=None, language="en",
             authors="McQuail, Denis",
             citation="McQuail, D. (2010). McQuail's mass communication theory (6th ed.). Sage.",
             locator_type="CHAPTER", locator="ch. 8", verified=True,
             supports="مصرف رسانه‌ای: الگو و بهره‌مندی مخاطب."),
        dict(kind="book", title_fa="مطالعات رسانه: مفاهیم کلیدی", title_en="Media Studies: The Key Concepts",
             year=2012, publisher="Wiley-Blackwell", doi=None, isbn="9781444359078", url=None, language="en",
             authors="Couldry, Nick",
             citation="Couldry, N. (2012). Media studies: The key concepts (2nd ed.). Wiley-Blackwell.",
             locator_type="CHAPTER", locator="entry: Consumption", verified=True,
             supports="مصرف رسانه‌ای: بافت و کیفیت مصرف."),
    ],
    "CPT-057": [
        dict(kind="book_chapter", title_fa="کاربردهای ارتباطات جمعی", title_en="The Uses of Mass Communications: Public, Personal and Critical Uses",
             year=1974, publisher="In Mass Communication and Urban Change (Oxford University Press)", doi=None, isbn=None, url=None, language="en",
             authors="Katz, Elihu; Blumler, James G.; Gurevitch, Mikhael",
             citation="Katz, E., Blumler, J. G., & Gurevitch, M. (1974). The uses of mass communications. In Mass communication and urban change.",
             locator_type="SECTION", locator="pp. 19-59", verified=True,
             supports="انتخاب رسانه: انتخاب فعال و نیازمحور مخاطب."),
        dict(kind="book", title_fa="نظریه ارتباطات انبوش مک‌کویل", title_en="McQuail's Mass Communication Theory",
             year=2010, publisher="Sage", doi=None, isbn="9781849202923", url=None, language="en",
             authors="McQuail, Denis",
             citation="McQuail, D. (2010). McQuail's mass communication theory (6th ed.). Sage.",
             locator_type="CHAPTER", locator="ch. 8", verified=True,
             supports="انتخاب رسانه: ترجیح و ارزیابی رسانه."),
    ],
    "CPT-058": [
        dict(kind="book", title_fa="نظریه ارتباطات انبوش مک‌کویل", title_en="McQuail's Mass Communication Theory",
             year=2010, publisher="Sage", doi=None, isbn="9781849202923", url=None, language="en",
             authors="McQuail, Denis",
             citation="McQuail, D. (2010). McQuail's mass communication theory (6th ed.). Sage.",
             locator_type="CHAPTER", locator="ch. 9", verified=True,
             supports="مواجهه رسانه‌ای: تماس با محتوا و اثر."),
        dict(kind="book", title_fa="مطالعات رسانه: مفاهیم کلیدی", title_en="Media Studies: The Key Concepts",
             year=2012, publisher="Wiley-Blackwell", doi=None, isbn="9781444359078", url=None, language="en",
             authors="Couldry, Nick",
             citation="Couldry, N. (2012). Media studies: The key concepts (2nd ed.). Wiley-Blackwell.",
             locator_type="CHAPTER", locator="entry: Exposure", verified=True,
             supports="مواجهه رسانه‌ای: کیفیت و اندازه‌گیری مواجهه."),
    ],
    "CPT-059": [
        dict(kind="book", title_fa="مطالعات رسانه: مفاهیم کلیدی", title_en="Media Studies: The Key Concepts",
             year=2012, publisher="Wiley-Blackwell", doi=None, isbn="9781444359078", url=None, language="en",
             authors="Couldry, Nick",
             citation="Couldry, N. (2012). Media studies: The key concepts (2nd ed.). Wiley-Blackwell.",
             locator_type="CHAPTER", locator="entry: Attention", verified=True,
             supports="توجه: جلب و نگهداری توجه مخاطب."),
        dict(kind="book", title_fa="نظریه ارتباطات انبوش مک‌کویل", title_en="McQuail's Mass Communication Theory",
             year=2010, publisher="Sage", doi=None, isbn="9781849202923", url=None, language="en",
             authors="McQuail, Denis",
             citation="McQuail, D. (2010). McQuail's mass communication theory (6th ed.). Sage.",
             locator_type="CHAPTER", locator="ch. 13", verified=True,
             supports="توجه: اقتصاد توجه و رقابت رسانه‌ها."),
    ],
    "CPT-060": [
        dict(kind="book", title_fa="نظریه‌های ارتباط انسانی", title_en="Theories of Human Communication",
             year=2011, publisher="Waveland Press", doi=None, isbn="9781577667063", url=None, language="en",
             authors="Littlejohn, Stephen W.; Foss, Karen A.",
             citation="Littlejohn, S. W., & Foss, K. A. (2011). Theories of human communication (10th ed.). Waveland Press.",
             locator_type="CHAPTER", locator="ch. 4", verified=True,
             supports="ادراک: فرآیند سازمان‌دهی و تفسیر فعال."),
        dict(kind="book", title_fa="نظریه ارتباطات انبوش مک‌کویل", title_en="McQuail's Mass Communication Theory",
             year=2010, publisher="Sage", doi=None, isbn="9781849202923", url=None, language="en",
             authors="McQuail, Denis",
             citation="McQuail, D. (2010). McQuail's mass communication theory (6th ed.). Sage.",
             locator_type="CHAPTER", locator="ch. 9", verified=True,
             supports="ادراک: اثر پیام بر نگرش و رفتار."),
    ],
}

ENRICH = {
    "CPT-056": dict(
        mechanism="مصرف رسانه‌ای در چهار حلقه عمل می‌کند. (۱) انتخاب رسانه و محتوا: مخاطب بر اساس نیاز، انگیزش، بافت و موقعیت، رسانه و محتوای خاصی را انتخاب می‌کند و تصمیم می‌گیرد چه، کجا و چه زمانی مصرف کند؛ (۲) مواجهه و دریافت: مخاطب با محتوا روبه‌رو می‌شود، آن را در سطح ادراک و توجه دریافت و در حافظه ثبت می‌کند؛ (۳) تفسیر و استفاده: مخاطب، بر اساس پیش‌دانسته‌ها و بافت، از محتوا معناسازی و بهره‌مندی می‌کند (اطلاعات، سرگرمی، هویت، ارتباط)؛ (۴) رفتار پس از مصرف: مصرف، بر نگرش، رفتار، خرید و تعامل‌های بعدی مخاطب اثر می‌گذارد و الگوی و عادت مصرف را شکل می‌دهد و آن را بازآرایی می‌کند (McQuail, 2010; Couldry, 2012).",
        key_concepts=["انتخاب رسانه", "مواجهه و دریافت", "بهره‌مندی", "الگوی مصرف", "نیاز و انگیزش", "سرگرمی و اطلاعات", "رفتار پس از مصرف"],
        critiques="نقد بر الگوی مصرف‌محور آن است که مصرف را صرفا یک «رفتار فردی و انتخابی» نشان می‌دهد و نقش ساختار، بافت، فرهنگ و قدرت را در شکل‌دهی به الگوی مصرف کم‌رنگ می‌سازد (McQuail, 2010). نقد دیگر «یکسان‌سازی مصرف» است: فرض بر آن است که مصرف، در همه گروه‌ها یکسان و صرفا قابل‌اندازه‌گیری با ساعات تماشا و خواندن است، در حالی که مصرف، بافتی و چندبُعدی است و «میزان» و «کیفیت» آن تفاوت محسوسی دارند (Couldry, 2012). همچنین مصرف در عصر دیجیتال، از «تفریح» به «کار و داده‌سازی» گسترش یافته و مرز مصرف و تولید کمرنگ شده که الگوهای کلاسیک مصرف را ناکافی می‌سازد. در نهایت، الگوی مصرف، در برابر الگوهای «اثر»، تأکید دارد که مخاطب، فعالانه و برای برآورده‌کردن نیازهای خود از رسانه استفاده می‌کند و مصرف، هدفمند، متنوع و بافتی است و یک «اثر واحد و یکسان» برای همه مخاطبان ندارد.",
        applications="کاربردها: طراحی و برنامه‌ریزی رسانه‌ای مبتنی بر الگوی مصرف مخاطب (نیاز، موقعیت، بافت)؛ پژوهش در عادات و الگوهای مصرف رسانه‌ای (خبر، سرگرمی، شبکه اجتماعی)؛ طراحی خدمات و محتوای متناسب با مراحل مختلف مصرف؛ آموزش سواد رسانه‌ای (مصرف آگاهانه و منتقد)؛ تحلیل رفتار پس از مصرف (نگرش، خرید، تعامل)؛ همچنین در مقایسه بین‌المللی عادات رسانه‌ای، تحلیل تغییر الگوی مصرف در نسل‌های مختلف و طراحی خدمات چندموقیتی، کاربرد مستقیم دارد (McQuail, 2010; Couldry, 2012).",
        evolution="مفهوم مصرف رسانه‌ای از نظریه‌های «مخاطب» و «استفاده و رضایت» (دهه‌های ۱۹۶۰–۱۹۷۰) شکل گرفت؛ در دهه‌های ۱۹۸۰–۲۰۰۰ با مطالعات عادات رسانه‌ای تقویت شد؛ در عصر دیجیتال، مصرف از «تفریحی» به «روزمره و چندموقیتی» (موبایل، کار، خانه) گسترش یافت و به «مصرف هم‌زمان و چندرسانه‌ای» بدل شد که در آن مرز میان مصرف و تولید کمرنگ و چندمرحله‌ای است (McQuail, 2010).",
        assumptions="فرض‌های نهفته: مصرف، یک فرآیند فعال و انتخابی است (نه صرفا دریافت منفعل)؛ الگوی مصرف، بر اساس نیاز، انگیزش و بافت توضیح داده می‌شود؛ مصرف، بر نگرش و رفتار مخاطب اثر می‌گذارد؛ و مصرف، قابل اندازه‌گیری از طریق ساعات و رفتار است (که همیشه دقیق و کامل نیست)؛ و الگوی مصرف، بر اساس بافت، نسل و موقعیت، متغیر و پویا است (McQuail, 2010; Couldry, 2012).",
    ),
    "CPT-057": dict(
        mechanism="انتخاب رسانه در سه حلقه عمل می‌کند. (۱) فعال‌سازی نیاز: مخاطب، با یک نیاز، انگیزه یا موقعیت (اطلاعات، سرگرمی، هویت، ارتباط) روبه‌رو می‌شود و این نیاز، جست‌وجوی رسانه‌ای و انگیزهٔ انتخاب را فعال می‌کند؛ (۲) ارزیابی گزینه‌ها: مخاطب، بر اساس دسترسی، عادت، اعتبار، هزینه، بافت و موقعیت، میان رسانه‌ها و محتواها ارزیابی و ترجیح می‌گذارد و گزینه‌های ممکن را محدود می‌کند؛ (۳) انتخاب و مصرف: مخاطب، رسانه و محتوای موردنظر را انتخاب، مصرف و از آن بهره‌مندی می‌کند و در صورت عدم رضایت، به گزینه‌های دیگر می‌رود و انتخاب را بازآرایی می‌کند (Katz et al., 1974; McQuail, 2010).",
        key_concepts=["فعال‌سازی نیاز", "ارزیابی گزینه‌ها", "ترجیح رسانه", "بهره‌مندی", "عادت و دسترسی", "رضا و تغییر"],
        critiques="نقد بر الگوی انتخاب‌محور آن است که انتخاب را صرفا یک «فرآیند عقلانی و هدفمند» نشان می‌دهد، در حالی که بخش زیادی از انتخاب رسانه، «عادی، عادت‌محور و بدون تفکر» است و هدفمند و آگاهانه نیست (McQuail, 2010). نقد دیگر «فردگرایانه بودن» است: الگو، انتخاب را در سطح فرد توضیح می‌دهد و نقش بافت اجتماعی، فرهنگ، اقتصاد و الگوریتم‌ها را در هدایت و شکل‌دهی انتخاب کم‌رنگ می‌سازد (Katz et al., 1974). همچنین در عصر دیجیتال، الگوریتم‌ها و پیشنهادها، انتخاب «آزاد» مخاطب را محدود و شکل می‌دهند که الگوهای کلاسیک آن را نادیده می‌گیرند. در نهایت، «انتخاب» در بافت‌های فقیررسانه‌ای، به‌سختی «انتخاب آزاد» است و بیشتر «پذیرش» است تا انتخاب، که الگوها آن را نادیده می‌گیرند و انتخاب را بیش‌ازحد ممکن نشان می‌دهند.",
        applications="کاربردها: طراحی استراتژی رسانه‌ای و محتوایی بر اساس نیاز و ترجیح مخاطب؛ پژوهش در الگوهای انتخاب و ترجیح رسانه (نیازمحور)؛ طراحی دسترسی و توزیع محتوا برای تسهیل انتخاب؛ آموزش سواد رسانه‌ای (انتخاب آگاهانه و منتقد)؛ همچنین در بازاریابی، هدف‌گذاری رسانه‌ای، شخصی‌سازی محتوا و طراحی سرویس‌های پیشنهادی، کاربرد مستقیم و عملی دارد؛ و در تحلیل رفتار انتخاب بین چند رسانه و پژوهش‌های تطبیقی، کاربرد دارد (Katz et al., 1974; McQuail, 2010).",
        evolution="مفهوم انتخاب رسانه، از نظریهٔ «استفاده و رضایت» (Katz, Blumler & Gurevitch, 1974) در دههٔ ۱۹۷۰ شکل گرفت و به‌عنوان جایگزین الگوهای «اثر مستقیم» مطرح شد؛ در دهه‌های ۱۹۸۰–۲۰۰۰ با پژوهش‌های انتخاب و ترجیح رسانه تقویت شد؛ در عصر دیجیتال، انتخاب از «انتخاب آگاهانه فردی» به «انتخاب شکل‌داده‌شده توسط الگوریتم و پیشنهاد» گسترش یافت و مفهوم «انتخاب» پیچیده‌تر و چندلایه‌تر شده است؛ امروزه، مرز میان «انتخاب» و «هدایت الگوریتمی» به‌شدت کمرنگ شده و انتخاب، بیشتر فرآیندی شکل‌داده‌شده است تا یک تصمیم کاملاً آزاد و مستقل (Katz et al., 1974).",
        assumptions="فرض‌های نهفته: مخاطب، در انتخاب رسانه، فعال و هدفمند است (نه منفعل)؛ انتخاب، بر اساس نیاز و انگیزه توضیح داده می‌شود؛ مخاطب، به گزینه‌های متنوع دسترسی دارد و می‌تواند آزاد انتخاب کند؛ و انتخاب، به‌طور آزاد و بدون محدودیتِ بافت و فناوری انجام می‌شود و عادت، نقش کمتری دارد؛ در نتیجه، «انتخاب» هم‌واره ممکن است و در همه بافت‌ها، یک انتخاب واقعی و آزاد محقق می‌شود (Katz et al., 1974; McQuail, 2010).",
    ),
    "CPT-058": dict(
        mechanism="مواجهه رسانه‌ای در سه حلقه تعریف می‌شود. (۱) تماس با محتوا: مخاطب، در یک موقعیت و زمان مشخص، با پیام یا محتوای رسانه‌ای روبه‌رو می‌شود و تماس فیزیکی و ادراکی با آن برقرار می‌کند؛ (۲) کیفیت مواجهه: مواجهه، بر اساس مدت، شدت، تکرار، توجه و بافت، متفاوت است و «میزان» و «کیفیت» مواجهه، بر شدت و عمق اثر آن اثر می‌گذارد؛ (۳) اثر مواجهه: مواجهه، پیش‌دانسته، نگرش، باورها و رفتار مخاطب را شکل می‌دهد و گاه بر انتخاب‌های بعدی و رفتار اجتماعی او اثر ماندگار می‌گذارد و الگوهای ادراکی را بازآرایی می‌کند؛ به این ترتیب، مواجهه، نقطهٔ ورود رسانه به زندگی روزمره و بافت مخاطب است و کیفیت آن، بر عمق اثر تعیین‌کننده است (McQuail, 2010; Couldry, 2012).",
        key_concepts=["تماس با محتوا", "مدت و شدت", "تکرار", "توجه", "اثر بر نگرش و رفتار", "بافت مواجهه", "پوشش رسانه‌ای", "مواجهه انتخابی"],
        critiques="نقد بر الگوی مواجهه‌محور آن است که «مواجهه» را با «اثر» مساوی می‌گیرد (اگر مخاطب ببیند، تأثیر می‌پذیرد)، در حالی که بین تماس و اثر، مراحل ادراک، تفسیر و بافت، میان‌جی هستند و اثر، تضمین‌شده نیست (Couldry, 2012). نقد دیگر «اندازه‌گیری» است: مواجهه، اغلب از طریق خوداظهاری و تخمین (ساعات) سنجیده می‌شود که با «مواجهه واقعی و توجه‌دار» تفاوت محسوسی دارد (McQuail, 2010). همچنین در عصر دیجیتال، «مواجهه» به‌شکل چندموقیتی و گذرا رخ می‌دهد و مرز «مواجهه» و «غیرمواجهه» کمرنگ و مبهم شده است. در نهایت، «مواجههٔ انتخابی» (خودخواسته) و «مواجههٔ اجباری» (مانند تابلوهای شهری و محیط‌های کاری) تفاوت ماهوی دارند که باید در پژوهش از هم متمایز شوند.",
        applications="کاربردها: پژوهش در میزان و الگوهای مواجهه رسانه‌ای (خبر، سرگرمی، شبکه اجتماعی)؛ تحلیل اثر مواجهه بر نگرش، باورها و رفتار (مثلا در بحران، تبلیغ و اطلاع‌رسانی)؛ طراحی پیام و کمپین برای بهینه‌سازی مواجهه مؤثر؛ آموزش سواد رسانه‌ای (آگاهی از مواجهه و اثر آن)؛ همچنین در ارزیابی پوشش رسانه‌ای، دسترسی و تحلیل مواجهه در بحران‌ها، کاربرد مستقیم دارد؛ و در طراحی استراتژی توزیع و زمان‌بندی پیام‌ها برای حداکثرسازی مواجهه مؤثر، کاربرد عملی دارد (McQuail, 2010; Couldry, 2012).",
        evolution="مفهوم مواجهه رسانه‌ای از پژوهش‌های «اثر رسانه» (دهه‌های ۱۹۴۰–۱۹۶۰) و پژوهش کلاسیک لاس‌ولز شکل گرفت؛ در دهه‌های ۱۹۷۰–۱۹۹۰ با پژوهش‌های اثر رسانه و تکرار تقویت شد؛ در عصر دیجیتال، مواجهه از «مواجههٔ یک‌بار با رسانهٔ جمعی» به «مواجههٔ مستمر، چندموقیتی و الگوریتمی» گسترش یافت و مفهوم «مواجهه» در عصر داده پیچیده‌تر و چندلایه‌تر شده است؛ امروزه، سنجش مواجهه، از «ساعات تماشا» به «کیفیت توجه و بافت مواجهه» تغییر کرده و معیارهای کلاسیک ناکافی شده‌اند (McQuail, 2010).",
        assumptions="فرض‌های نهفته: مواجهه، پیش‌شرط اثر رسانه است (بدون تماس، اثری نیست)؛ میزان و کیفیت مواجهه، بر شدت و عمق اثر اثر می‌گذارد؛ مخاطب، هنگام مواجهه، توجه و درک دارد؛ و مواجهه، قابل اندازه‌گیری و با اثر قابل‌ارتباط است (که همیشه دقیق نیست)؛ مخاطب، هنگام مواجهه، هم‌زمان توجه و درک دارد و مواجهه، به‌خودی‌خود، پیام را مؤثر منتقل می‌کند (McQuail, 2010; Couldry, 2012).",
    ),
    "CPT-059": dict(
        mechanism="توجه در فرآیند ارتباطی در چهار حلقه عمل می‌کند. (۱) جلب توجه: محتوا یا محرک، از میان بی‌شمار محرک‌ها، توجه مخاطب را به خود جلب می‌کند (با جذابیت، نوآوری، احساسی بودن یا اهمیت)؛ (۲) پردازش: مخاطب، پیام را در سطح ادراک و حافظه پردازش و بر اساس اهمیت و بافت، تفسیر و معناسازی می‌کند؛ (۳) نگهداری توجه: توجه، در طول مواجهه، حفظ و گاه از دست می‌رود و شدت و مدت آن، بر عمق درک اثر می‌گذارد؛ (۴) اثر توجه: توجه، تعیین‌کنندهٔ آن است که چه پیامی «دریافت» و بر نگرش و رفتار اثر بگذارد؛ بدین‌سان توجه، گلوگاه کلیدی فرآیند ارتباطی است (Couldry, 2012; McQuail, 2010).",
        key_concepts=["جلب توجه", "پردازش پیام", "نگهداری توجه", "رقابت محرک‌ها", "اقتصاد توجه", "عمق درک", "درگیرسازی", "رقابت رسانه‌ای"],
        critiques="نقد بر الگوی توجه‌محور آن است که توجه را «کالایی محدود» نشان می‌دهد که باید «رقابت» بر سر آن بود (اقتصاد توجه)، در حالی که توجه، فرآیندی چندبُعدی و بافتی است و نه صرفا «محدود» و «فروشی» (Couldry, 2012). نقد دیگر «بازاریابی‌زدگی» است: تمرکز بیش‌ازحد بر جلب توجه، می‌تواند محتوا را به «جذب‌کننده و هیجانی» بدل کند و عمق، دقت و اعتبار خبر را فدای «توجه‌برندگی» بکند (McQuail, 2010). همچنین اندازه‌گیری توجه واقعی (در برابر نگاه‌کردن صرف) دشوار است و در عصر چک‌کردن موبایل، تعریف «توجه» مبهم و متغیر شده است. در نهایت، تمرکز بیش‌ازحد بر جلب توجه، می‌تواند مخاطب را به یک «منبع کالایی» تقلیل دهد که از نظر اخلاقی و حرفه‌ای چالش‌برانگیز است و کیفیت محتوا را کاهش می‌دهد.",
        applications="کاربردها: طراحی محتوا و خبر برای جلب و حفظ توجه (عنوان، تصویر، ساختار)؛ پژوهش در الگوها و عوامل توجه (محرک، بافت، اهمیت)؛ تحلیل اقتصاد توجه و رقابت رسانه‌ها برای توجه مخاطب؛ آموزش سواد رسانه‌ای (آگاهی از جلب توجه و هیجان‌افزایی)؛ همچنین در طراحی تجربهٔ کاربری، تبلیغ و رقابت پلتفرم‌ها برای نگهداشت کاربر، کاربرد مستقیم دارد؛ و در تحلیل رفتار کاربر در برابر پیشنهاد و پژوهش درگیرسازی، کاربرد عملی دارد (Couldry, 2012; McQuail, 2010).",
        evolution="مفهوم توجه از روان‌شناسی ادراک (قرن ۱۹) وارد مطالعات رسانه شد؛ در دهه‌های ۱۹۹۰–۲۰۰۰ با «اقتصاد توجه» (Goldhaber) به مفهوم محوری رسانه و بازاریابی تبدیل شد؛ در عصر دیجیتال، توجه به «محدودیت اصلی» بدل شد و «رقابت برای توجه» و «اقتصاد توجه و داده» شکل تازه‌ای از تحلیل توجه ایجاد کرد که در آن توجه، کالای اصلی رسانه‌ها است؛ امروزه، «توجه» با «داده و رفتار کاربر» گره خورده و اقتصاد توجه، به اقتصاد داده و پیش‌بینی رفتار گسترش یافته و پیچیده‌تر شده است (Couldry, 2012).",
        assumptions="فرض‌های نهفته: توجه، پیش‌شرط دریافت و اثر پیام است (بدون توجه، اثری نیست)؛ توجه، منبعی محدود است و رسانه‌ها بر سر آن رقابت می‌کنند؛ توجه، قابل جلب و طراحی است (با محرک و جذابیت)؛ و توجه، قابل اندازه‌گیری و دارای ارزش تجاری است؛ توجه، هم‌واره قابل جلب و طراحی است و هر مخاطب، به هر محرک، به یک شکل توجه می‌کند و توجه، با رفتار یکسان است (Couldry, 2012; McQuail, 2010).",
    ),
    "CPT-060": dict(
        mechanism="ادراک در فرآیند ارتباطی در چهار حلقه عمل می‌کند. (۱) دریافت حسگرانه: پیام از طریق حواس (بینایی، شنوایی) وارد سیستم ادراکی مخاطب می‌شود و محرک‌ها ثبت می‌شوند؛ (۲) سازمان‌دهی: مخاطب، بر اساس پیش‌دانسته‌ها، باورها و چارچوب‌ها، محرک‌ها را سازمان‌دهی و معنادار می‌کند (ادراک، فعال و معناساز است نه صرفا بازتاب)؛ (۳) تفسیر: مخاطب، به پیام، بر اساس بافت و انگیزه، معنایی می‌دهد که ممکن است با نیت فرستنده متفاوت باشد؛ (۴) اثر ادراک: ادراک، بر نگرش، قضاوت و رفتار مخاطب اثر می‌گذارد و ادراک‌های متفاوت، به قضاوت‌ها و واکنش‌های متفاوت می‌انجامد (Littlejohn & Foss, 2011; McQuail, 2010).",
        key_concepts=["دریافت حسگرانه", "سازمان‌دهی ادراکی", "پیش‌دانسته‌ها و چارچوب", "تفسیر فعال", "ادراک و معناسازی", "اثر بر نگرش", "ادراک اجتماعی", "زبان و ادراک", "ادراک چندرسانه‌ای"],
        critiques="نقد بر الگوی ادراکی آن است که ادراک را «مستقل و فردی» نشان می‌دهد، در حالی که ادراک، اجتماعی، فرهنگی و بافتی است و در گفت‌وگو و تعامل شکل می‌گیرد و نمی‌توان آن را به فرد تقلیل داد (Littlejohn & Foss, 2011). نقد دیگر «شناختی‌زدگی» است: الگوها بر «پردازش ذهنی» تأکید دارند و نقش احساس، بدن و بافت اجتماعی را در ادراک کم‌رنگ می‌سازند (McQuail, 2010). همچنین ادراک، فرآیندی «ناآگاه» و «غیرمستقیم» است و سنجش مستقیم آن دشوار است و بین ادراک درونی و رفتار بیرونی فاصله وجود دارد. در نهایت، ادراک رسانه‌ای، به‌شدت با «چارچوب‌بندی» و «زبان» گره خورده و نمی‌توان ادراک را از زبان، تصویر و رسانه جدا کرد و به یک فرآیند خالص تقلیل داد.",
        applications="کاربردها: طراحی پیام و رسانه برای هدایت و بهبود ادراک مخاطب (چارچوب، تصویر، واژگان)؛ پژوهش در ادراک رسانه‌ای و اثر چارچوب‌بندی بر ادراک؛ تحلیل ادراک عمومی از رویدادها و رسانه‌ها؛ آموزش سواد رسانه‌ای (آگاهی از فرآیند ادراک و چارچوب‌ها)؛ همچنین در طراحی تجربهٔ کاربری، بازاریابی و طراحی پیام‌های عمومی، کاربرد مستقیم و عملی دارد؛ و در تحلیل ادراک رسانه‌ای در بافت‌های مختلف، طراحی آموزش و اطلاع‌رسانی و پژوهش در ادراک عمومی، کاربرد مهم دارد (Littlejohn & Foss, 2011; McQuail, 2010).",
        evolution="مفهوم ادراک از روان‌شناسی شناختی (قرن ۱۹ و ۲۰) وارد علوم ارتباط شد؛ در دهه‌های ۱۹۷۰–۱۹۹۰ با «گستۀ شناختی» و پژوهش‌های چارچوب‌بندی تقویت شد؛ در مطالعات رسانه معاصر، ادراک، از «پردازش فردی» به «ادراک اجتماعی و چندلایه» گسترش یافت و نقش فرهنگ، گفت‌وگو و رسانه در شکل‌دهی ادراک، پررنگ‌تر و قابل‌سنجش‌تر شده است؛ امروزه، ادراک، با «ادراک چندرسانه‌ای» و «ادراک در بستر الگوریتم و پلتفرم» گسترش یافته و پیچیده‌تر شده است (Littlejohn & Foss, 2011).",
        assumptions="فرض‌های نهفته: ادراک، فرآیندی فعال و معناساز است (نه بازتاب منفعل محرک)؛ ادراک، بر اساس پیش‌دانسته‌ها و چارچوب‌های مخاطب شکل می‌گیرد؛ پیام، بر اساس ادراک مخاطب، تفسیر می‌شود (نه صرفا بر اساس نیت فرستنده)؛ و ادراک، بر نگرش و رفتار اثر واقع و ماندگار دارد؛ ادراک، یکپارچه و پایدار است و در همه بافت‌ها، پیام به یک شکل ادراک می‌شود و تفاوت ادراک‌ها، ناچیز است و ادراک، قابل پیش‌بینی و یکسان است (Littlejohn & Foss, 2011; McQuail, 2010).",
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
                    (code, json.dumps({"batch": 303, "score": score, "words": words,
                                       "sources": n_sources, "verified": n_verified,
                                       "relations": n_rel, "rubric": detail}, ensure_ascii=False), STAMP, NOW))
        print(code, "words", words, "score", score, "detail", detail)
    conn.commit()
    conn.close()
    print("BATCH303 DONE")


if __name__ == "__main__":
    main()
