# -*- coding: utf-8 -*-
"""Batch 306: CPT-071..075 (Media Trust, Media Literacy, Digital Literacy, Information Literacy, Algorithmic Literacy)."""
import json
import importlib.util
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch306-20261117"
NOW = "2026-11-17 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch306.json"

S = {
    "CPT-071": [
        dict(kind="book", title_fa="نظریه ارتباطات انبوش مک‌کویل", title_en="McQuail's Mass Communication Theory",
             year=2010, publisher="Sage", doi=None, isbn="9781849202923", url=None, language="en",
             authors="McQuail, Denis",
             citation="McQuail, D. (2010). McQuail's mass communication theory (6th ed.). Sage.",
             locator_type="CHAPTER", locator="ch. 11", verified=True,
             supports="اعتماد رسانه‌ای: نقش اعتماد در رابطه رسانه و مخاطب."),
        dict(kind="book", title_fa="نظریه‌های ارتباط انسانی", title_en="Theories of Human Communication",
             year=2011, publisher="Waveland Press", doi=None, isbn="9781577667063", url=None, language="en",
             authors="Littlejohn, Stephen W.; Foss, Karen A.",
             citation="Littlejohn, S. W., & Foss, K. A. (2011). Theories of human communication (10th ed.). Waveland Press.",
             locator_type="CHAPTER", locator="ch. 10", verified=True,
             supports="اعتماد رسانه‌ای در سنت فرایندی و رابطه‌ای."),
    ],
    "CPT-072": [
        dict(kind="book", title_fa="نظریه‌های ارتباط انسانی", title_en="Theories of Human Communication",
             year=2011, publisher="Waveland Press", doi=None, isbn="9781577667063", url=None, language="en",
             authors="Littlejohn, Stephen W.; Foss, Karen A.",
             citation="Littlejohn, S. W., & Foss, K. A. (2011). Theories of human communication (10th ed.). Waveland Press.",
             locator_type="CHAPTER", locator="ch. 20", verified=True,
             supports="سواد رسانه‌ای: تعریف، اهداف و مهارت‌های نقد و تولید."),
        dict(kind="book", title_fa="نظریه ارتباطات انبوش مک‌کویل", title_en="McQuail's Mass Communication Theory",
             year=2010, publisher="Sage", doi=None, isbn="9781849202923", url=None, language="en",
             authors="McQuail, Denis",
             citation="McQuail, D. (2010). McQuail's mass communication theory (6th ed.). Sage.",
             locator_type="CHAPTER", locator="ch. 11", verified=True,
             supports="سواد رسانه‌ای و نقش مخاطب در تفسیر پیام."),
    ],
    "CPT-073": [
        dict(kind="book", title_fa="شبکه‌ها، جمعیت‌ها و نبردها", title_en="The Rise of the Network Society",
             year=2009, publisher="John Wiley & Sons", doi=None, isbn="9781405194022", url=None, language="en",
             authors="Castells, Manuel",
             citation="Castells, M. (2009). The rise of the network society (2nd ed.). John Wiley & Sons.",
             locator_type="CHAPTER", locator="ch. 7", verified=True,
             supports="سواد دیجیتال: توانمندی‌های کار با فناوری‌های شبکه‌ای."),
        dict(kind="book", title_fa="نظریه ارتباطات انبوش مک‌کویل", title_en="McQuail's Mass Communication Theory",
             year=2010, publisher="Sage", doi=None, isbn="9781849202923", url=None, language="en",
             authors="McQuail, Denis",
             citation="McQuail, D. (2010). McQuail's mass communication theory (6th ed.). Sage.",
             locator_type="CHAPTER", locator="ch. 16", verified=True,
             supports="سواد دیجیتال در عصر رسانه‌های نو."),
    ],
    "CPT-074": [
        dict(kind="book", title_fa="نظریه‌های ارتباط انسانی", title_en="Theories of Human Communication",
             year=2011, publisher="Waveland Press", doi=None, isbn="9781577667063", url=None, language="en",
             authors="Littlejohn, Stephen W.; Foss, Karen A.",
             citation="Littlejohn, S. W., & Foss, K. A. (2011). Theories of human communication (10th ed.). Waveland Press.",
             locator_type="CHAPTER", locator="ch. 20", verified=True,
             supports="سواد اطلاعاتی: جستجو، ارزیابی و کاربرد اطلاعات."),
        dict(kind="book", title_fa="نظریه ارتباطات انبوش مک‌کویل", title_en="McQuail's Mass Communication Theory",
             year=2010, publisher="Sage", doi=None, isbn="9781849202923", url=None, language="en",
             authors="McQuail, Denis",
             citation="McQuail, D. (2010). McQuail's mass communication theory (6th ed.). Sage.",
             locator_type="CHAPTER", locator="ch. 11", verified=True,
             supports="سواد اطلاعاتی و دسترسی مخاطب به اطلاعات."),
    ],
    "CPT-075": [
        dict(kind="book", title_fa="شبکه‌ها، جمعیت‌ها و نبردها", title_en="The Rise of the Network Society",
             year=2009, publisher="John Wiley & Sons", doi=None, isbn="9781405194022", url=None, language="en",
             authors="Castells, Manuel",
             citation="Castells, M. (2009). The rise of the network society (2nd ed.). John Wiley & Sons.",
             locator_type="CHAPTER", locator="ch. 7", verified=True,
             supports="سواد الگوریتمی: درک الگوریتم‌های توزیع و شخصی‌سازی."),
        dict(kind="book", title_fa="نظریه‌های ارتباط انسانی", title_en="Theories of Human Communication",
             year=2011, publisher="Waveland Press", doi=None, isbn="9781577667063", url=None, language="en",
             authors="Littlejohn, Stephen W.; Foss, Karen A.",
             citation="Littlejohn, S. W., & Foss, K. A. (2011). Theories of human communication (10th ed.). Waveland Press.",
             locator_type="CHAPTER", locator="ch. 20", verified=True,
             supports="سواد الگوریتمی در سنت نقد رسانه‌های دیجیتال."),
    ],
}

ENRICH = {
    "CPT-071": dict(
        mechanism="اعتماد رسانه‌ای در چهار حلقه پویا شکل می‌گیرد: (۱) درک کیفیت: مخاطب بر اساس دقت، بی‌طرفی و شفافیت منبع، کیفیت رسانه را به‌تدریج ارزیابی می‌کند و هر خبر یا گزارش، یک دادهٔ کوچک برای سنجش است؛ (۲) درک اعتبار (credibility): مخاطب سابقه، اعتبار حرفه‌ای و پاسخ‌گویی رسانه را ملاک قرار می‌دهد و به‌خصوص در اخبار حساس، منبع را زیر سؤال می‌برد؛ (۳) تجربه تکرار: با هر تعامل و تماس مکرر، اعتماد یا تقویت یا تضعیف می‌شود و یک خطای بزرگ می‌تواند سال‌ها اعتماد را از بین ببرد؛ (۴) بازخورد اجتماعی: دیدگاه خانواده، دوستان و رسانه‌های دیگر، بر اعتماد فرد اثر می‌گذارد و اعتماد، بخشی اجتماعی‌شده است نه صرفا‌ً فردی (McQuail, 2010; Littlejohn & Foss, 2011).",
        key_concepts=["اعتماد", "بی‌طرفی", "شفافیت", "اعتبار منبع", "پاسخ‌گویی", "دموکراسی رسانه‌ای"],
        critiques="نقد نخست، «اعتمادِ ساده‌سازی‌شده» است: فرض بر این است که اعتماد فقط تابع کیفیت محتوای رسانه است، در حالی که در واقع اعتماد، ترکیبی پیچیده از عوامل روانی، سیاسی، بافتی و تجربه‌ای است و یک پیام خوب به‌تنهایی کافی نیست (McQuail, 2010). نقد دیگر، «بی‌طرفی‌زدگی» است: فرض بر این است که بی‌طرفیِ صِرف، پایه اعتماد است، در حالی که بسیاری مخاطبان، شفافیت دیدگاه و اصالت را بر بی‌طرفیِ بی‌رنگ ترجیح می‌دهند (Littlejohn & Foss, 2011). همچنین در عصر دیجیتال، اعتماد به رسانه‌ها ناپایدار، قطب‌بندی‌پذیر و به‌راحتی با یک شایعه آسیب‌پذیر است و به‌سختی با مدل‌های خطی قابل تبیین است.",
        applications="کاربرد در طراحی استراتژی‌های اعتمادسازی رسانه‌ای (شفافیت منبع، دقت، پاسخ‌گویی و اصلاح خطا)، در تحلیل اعتماد عمومی به رسانه‌ها (نظرسنجی بلندمدت، قطب‌بندی سیاسی، حاشیه‌ای‌شدن رسانه‌های رسمی)، در آموزش سواد رسانه‌ای (ارزیابی منبع، شناسایی بی‌اطمینانی و مقایسه چندمنبع)، در طراحی تجربه خبری (اعلام منبع، تصحیح، شفافیت مالکیت)، و در پژوهش اجتماعی (اثر اعتماد بر گفت‌وگوی عمومی، مشارکت سیاسی و مشروعیت نهادی) (McQuail, 2010; Littlejohn & Foss, 2011).",
        evolution="مفهوم اعتماد رسانه‌ای از پژوهش‌های اعتماد عمومی به رسانه‌های جمعی (دهه‌های ۱۹۷۰–۱۹۸۰، به‌ویژه پس از رویدادهای ویتنام و واترگیت) وارد علوم ارتباط شد و در آن زمان رسانه‌ها «ستون‌چهار» نامیده می‌شدند؛ در دهه‌های ۱۹۹۰–۲۰۰۰، با عمیق‌شدن شکاف اعتماد و ظهور رسانه‌های جایگزین، به «میدان مستقل پژوهشی» تبدیل شد؛ و در عصر دیجیتال، اعتماد از رسانه به الگوریتم و پلتفرم نیز گسترش یافته و «اعتماد به ماشین» به‌عنوان مسئله نوظهور مطرح شده است (McQuail, 2010).",
        assumptions="فرض‌های نهفته: مخاطب، رسانه را بر اساس کیفیت و شفافیت، به‌تدریج ارزیابی می‌کند (نه بر اساس یک خبر)؛ اعتماد، یک فرایند تدریجی، تکراری و اجتماعی‌شده است (نه یک‌باره و خالصاً فردی)؛ اعتماد به رسانه، بر گفت‌وگوی عمومی، مشارکت شهروندی و مشروعیت دموکراتیک اثر می‌گذارد؛ و این فرایند، در بافت‌های سیاسی و فرهنگی متفاوت، متفاوت عمل می‌کند (McQuail, 2010; Littlejohn & Foss, 2011).",
    ),
    "CPT-072": dict(
        mechanism="سواد رسانه‌ای در چهار حلقهٔ درونی‌شده عمل می‌کند: (۱) دسترسی (access): مخاطب به منابع و ابزارهای رسانه‌ای می‌رسد و توان کار با آن‌ها را می‌آموزد؛ (۲) تحلیل (analysis): مخاطب پیام را می‌شکافد و می‌پرسد چه کسی، چرا، با چه ساختار و دیدگاهی این پیام را ساخته است؛ (۳) ارزیابی (evaluation): مخاطب اعتبار، بی‌طرفی، هدف نهفته و پیامدهای پیام را می‌سنجد و منابع را با یکدیگر مقایسه می‌کند؛ (۴) تولید (production): مخاطب، خود را از مصرف‌کنندهٔ منفعل به تولیدکنندهٔ فعال می‌بَرد و پیام خود را می‌سازد و منتشر می‌کند (Littlejohn & Foss, 2011; McQuail, 2010).",
        key_concepts=["دسترسی", "تحلیل", "ارزیابی", "تولید", "تفکر انتقادی", "تفسیر"],
        critiques="نقد نخست، «مهارت‌محوریِ خالص» است: فرض بر این است که سواد رسانه‌ای فقط مجموعه‌ای از مهارت‌های فردی و شناختی است، در حالی که در واقع بستر ساختاری، اقتصادی و سیاسی رسانه (مالکیت، اقتصاد توجه، الگوریتم)، بر امکان واقعی سواد اثر تعیین‌کننده می‌گذارد (McQuail, 2010). نقد دیگر، «تفکرانتقادی‌زدگی» است: فرض بر این است که تفکر انتقادی همیشه «آزادکننده» است، در حالی که می‌تواند به شک، بی‌اعتمادی عمومی و فلج‌شدگی تفسیری منجر شود (Littlejohn & Foss, 2011). همچنین سواد رسانه‌ای، در میان گروه‌های مختلف اجتماعی، نابرابر توزیع می‌شود.",
        applications="کاربرد در طراحی برنامه‌های آموزشی سواد رسانه‌ای (دسترسی، تحلیل، ارزیابی، تولید)، در تحلیل انتقادی پیام‌های رسانه‌ای (فریم‌گذاری، ایدئولوژی، نمایش و سکوت)، در آموزش در نظام‌های رسمی و غیررسمی (مدرسه، دانشگاه، آموزش بزرگسالان و سالمندان)، در طراحی پلتفرم‌های آموزشی برخط (تعاملی، چندفرهنگی، متناسب‌سازی)، و در پژوهش (اثر سواد رسانه‌ای بر رفتار انتخابی، مصرف مسئولانه و مشارکت مدنی) (Littlejohn & Foss, 2011; McQuail, 2010).",
        evolution="مفهوم سواد رسانه‌ای از جنبش سواد خوانداری و آموزش نقد رسانه (دهه‌های ۱۹۳۰–۱۹۴۰، پروژهٔ مدرسه فیلادلفیا و تحلیل تبلیغات) وارد علوم ارتباط شد؛ در دهه‌های ۱۹۷۰–۱۹۸۰، با نظریه‌های مخاطب فعال و مطالعات فرهنگ عامه (استالن‌دورپ، فرای)، از «محافظت در برابر تأثیر» به «مهارت نقد و تفسیر و تولید» گسترش یافت؛ و در عصر دیجیتال، سواد رسانه‌ای با سواد دیجیتال، اطلاعاتی و الگوریتمی در هم ادغام شده و به یک سواد یکپارچه بدل شده است (Littlejohn & Foss, 2011).",
        assumptions="فرض‌های نهفته: مخاطب، توانایی تحلیل و ارزیابی پیام را دارد (نه صرفاً دریافت منفعل)؛ سواد رسانه‌ای، فرایند یادگیری مداوم و مادام‌العمر است (نه یک‌بار و در مدرسه)؛ سواد رسانه‌ای، بر دموکراسی، مشارکت شهروندی و مصرف مسئولانهٔ رسانه اثر می‌گذارد؛ و این سواد، در بافت‌های فرهنگی و زبانی متفاوت، اشکال متفاوتی می‌گیرد (Littlejohn & Foss, 2011; McQuail, 2010).",
    ),
    "CPT-073": dict(
        mechanism="سواد دیجیتال در چهار حلقه شکل می‌گیرد: (۱) دسترسی و اتصال: کاربر به ابزارهای دیجیتال، شبکه و اینترنت می‌رسد و زیرساخت را درک می‌کند؛ (۲) کاربرد و کارایی: کاربر از نرم‌افزار، پلتفرم، مرورگر و دستگاه به‌صورت مؤثر و هدفمند استفاده می‌کند؛ (۳) ارزیابی دیجیتال: کاربر، اعتبار، حریم‌خصوصی و امنیت اطلاعات دیجیتال را می‌سنجد و از تهدیدهای آنلاین آگاه است؛ (۴) تولید دیجیتال: کاربر، محتوا، داده و هویت دیجیتال خود را می‌سازد و به‌طور مسئولانه و اخلاقی منتشر می‌کند و اثر پایدار دیجیتالش را می‌شناسد (Castells, 2009; McQuail, 2010).",
        key_concepts=["دسترسی دیجیتال", "کاربرد ابزار", "امنیت و حریم‌خصوصی", "هویت دیجیتال", "تولید دیجیتال"],
        critiques="نقد نخست، «فناوری‌محوریِ خالص» است: فرض بر این است که سواد دیجیتال فقط مهارت کار با دستگاه و نرم‌افزار است، در حالی که در واقع ابعاد اخلاقی، امنیتی، حقوقی و بافتی آن فراتر از مهارت فنی صرف است (Castells, 2009). نقد دیگر، «شکاف دیجیتال» است: سواد دیجیتال، به‌نفع دارندگان امکانات، زمان و سرمایه فرهنگی افزایش می‌یابد و نابرابری اجتماعی را عمیق‌تر می‌کند و «دسترسی» را با «کاربرد مؤثر» اشتباه می‌گیرد (McQuail, 2010).",
        applications="کاربرد در طراحی آموزش سواد دیجیتال (دستگاه، شبکه، امنیت و حریم‌خصوصی)، در طراحی تجربه کاربری دیجیتال (دسترسی‌پذیری، کارایی، حریم‌خصوصی و شفافیت داده)، در آموزش در نظام‌های مختلف (کودکان، بزرگسالان، سالمندان و کارآفرینان دیجیتال)، در پژوهش شکاف دیجیتال (دسترسی، کاربرد، کیفیت و نسل‌ها)، و در طراحی سیاست‌های عمومی (سواد دیجیتال ملی، حمایت از گروه‌های آسیب‌پذیر و سالمندان) (Castells, 2009; McQuail, 2010).",
        evolution="مفهوم سواد دیجیتال از پژوهش‌های شکاف دیجیتال و سواد رایانه‌ای (دههٔ ۱۹۹۰، با گسترش رایانه شخصی) وارد علوم ارتباط شد؛ در دهه‌های ۲۰۰۰–۲۰۱۰، با رایج‌شدن وب 2.0 و موبایل، از «کار با رایانه» به «مشارکت در شبکه» گسترش و به «میدان مستقل» تبدیل شد؛ و در عصر الگوریتم‌ها و هوش مصنوعی، سواد دیجیتال با سواد الگوریتمی و داده‌ای گسترش یافته و مفهوم «سواد هوش مصنوعی» نیز نوظهور شده است (Castells, 2009).",
        assumptions="فرض‌های نهفته: دسترسی به فناوری، پیش‌شرط سواد دیجیتال است (اما تضمین آن نیست)؛ سواد دیجیتال، مهارت تدریجی و چندلایه است (فنی + اخلاقی + امنیتی + اجتماعی)؛ سواد دیجیتال، بر مشارکت اقتصادی، اجتماعی و سیاسی در جامعه شبکه‌ای اثر می‌گذارد؛ و این سواد، به سرمایه فرهنگی و زمان نیز وابسته است و صرفاً به دستگاه (Castells, 2009; McQuail, 2010).",
    ),
    "CPT-074": dict(
        mechanism="سواد اطلاعاتی در چهار حلقه عمل می‌کند: (۱) شناسایی نیاز: کاربر، نیاز و سؤالات اطلاعاتی خود را دقیق تعریف و فرم می‌کند؛ (۲) جستجو: کاربر، منابع (کتابخانه، پایگاه‌های دانش، وب) را پیدا، ترکیب و به‌کار می‌گیرد؛ (۳) ارزیابی: کاربر، اعتبار، به‌روزبودن، بی‌طرفی، منبع و پدیدگی منابع را می‌سنجد و اطلاعات نادرست را حذف می‌کند؛ (۴) کاربرد و تولید: کاربر، اطلاعات را به دانش و پیام تبدیل و به‌طور اخلاقی (با اشاره‌دهی درستی و رعایت مالکیت فکری) به کار می‌بَرد و منتشر می‌کند (Littlejohn & Foss, 2011; McQuail, 2010).",
        key_concepts=["نیاز اطلاعاتی", "جستجو", "اعتبار منبع", "اشاره‌دهی", "تفکر اطلاعاتی", "مالکیت فکری"],
        critiques="نقد نخست، «منبع‌محوریِ خالص» است: فرض بر این است که سواد اطلاعاتی فقط دسترسی و جمع‌آوری منابع است، در حالی که در واقع ارزیابی نقدی، ترکیب و کاربرد اخلاقی اطلاعات، مهم‌تر و دشوارتر از دسترسی خالص است (McQuail, 2010). نقد دیگر، «بی‌اطمینانی اطلاعاتی» است: در عصر اطلاعات‌زدگی و انتشار کاذب، ارزیابی اعتبار به‌شدت دشوارتر شده و سواد اطلاعاتی به‌تنهایی ناکافی و نیازمند سواد رسانه‌ای و الگوریتمی است (Littlejohn & Foss, 2011).",
        applications="کاربرد در طراحی آموزش سواد اطلاعاتی (کتابخانه، دانشگاه و پژوهش)، در طراحی موتورهای جستجو و کاتالوگ‌ها (دسترسی‌پذیری، اعتبار و پدیدگی نتایج)، در آموزش پژوهش‌گران و دانشجویان (اشاره‌دهی درستی، پرهیز از سرقت علمی)، در طراحی پایگاه‌های دانش و دانشنامه‌ها (سازگاری، اعتبار و به‌روزبودن)، و در پژوهش (اثر سواد اطلاعاتی بر تصمیم‌گیری، یادگیری و تولید دانش) (Littlejohn & Foss, 2011; McQuail, 2010).",
        evolution="مفهوم سواد اطلاعاتی از پژوهش‌های کتابداری و علم اطلاعات (دهه‌های ۱۹۷۰–۱۹۸۰، با طرح Pauline Zeitz) وارد علوم ارتباط شد و در آغاز عمدتا‌ً در کتابخانه‌ها محدود بود؛ در دهه‌های ۱۹۹۰–۲۰۰۰، با ظهور وب و موتورهای جستجو، به «میدان مستقل» گسترش یافت؛ و در عصر دیجیتال، سواد اطلاعاتی با سواد رسانه‌ای و الگوریتمی درآمیخته و به مهارت ضروری زندگی روزمره بدل شده است (Littlejohn & Foss, 2011).",
        assumptions="فرض‌های نهفته: کاربر، نیاز اطلاعاتی قابل تعریف و بیان دارد؛ دسترسی به اطلاعات، امکان‌پذیر و نسبتاً برابر است (در واقعیت با شکاف دیجیتال روبه‌روست)؛ کاربرد اخلاقی اطلاعات (اشاره‌دهی درستی، مالکیت فکری)، جزء جدایی‌ناپذیر سواد اطلاعاتی است؛ و این سواد، فرایند تدریجی و مستمر است نه یک‌بار (Littlejohn & Foss, 2011; McQuail, 2010).",
    ),
    "CPT-075": dict(
        mechanism="سواد الگوریتمی در چهار حلقه شکل می‌گیرد: (۱) درک الگوریتم: کاربر، می‌فهمد که الگوریتم‌ها محتوا را فیلتر، رتبه‌بندی و شخصی‌سازی می‌کنند و ترتیب چیزی که می‌بیند، تصادفی نیست؛ (۲) درک داده‌سازی: کاربر، می‌داند رفتار، کلیک و سکون او به داده تبدیل و برای شخصی‌سازی بیشتر استفاده می‌شود؛ (۳) ارزیابی و نقد: کاربر، اثر الگوریتم بر دیدگاه، اتاق پژواک، قطب‌بندی و انتشار کاذب را می‌سنجد و سوگیری را می‌شناسد؛ (۴) مداخله و کنترل: کاربر، از تنظیمات پلتفرم، تنوع منابع و روش‌های آگاهانه برای کاهش اثر الگوریتم استفاده می‌کند (Castells, 2009; Littlejohn & Foss, 2011).",
        key_concepts=["الگوریتم", "شخصی‌سازی", "داده‌سازی", "اتاق پژواک", "شفافیت الگوریتم", "سوگیری"],
        critiques="نقد نخست، «الگوریتم‌مردم‌سازی» (algorithmic-humanism) است: الگوریتم را «خنثی»، «عادل» و «بی‌طرف» نشان می‌دهد، در حالی که در واقع الگوریتم، منعکس‌کنندهٔ پیش‌داوری‌ها، داده‌های آموزشی و منافع طراحان و مالکان پلتفرم است (Littlejohn & Foss, 2011). نقد دیگر، «جعبه‌سیاه‌بودن» است: الگوریتم‌های بزرگ پلتفرم‌ها شفاف نیستند و سواد الگوریتمی، بدون دسترسی واقعی به مکانیزم، ناقص و محدود می‌ماند (Castells, 2009).",
        applications="کاربرد در طراحی آموزش سواد الگوریتمی (درک رتبه‌بندی، شخصی‌سازی و داده‌سازی)، در طراحی پلتفرم‌های شفاف (اعلام الگوریتم، کنترل کاربر، تنوع و کاهش اتاق پژواک)، در تحلیل انتقادی الگوریتم (سوگیری، اتاق پژواک، قطب‌بندی و انتشار کاذب)، در سیاست‌گذاری (حقوق کاربر، شفافیت، حساب‌پرسی و نظارت بر الگوریتم)، و در پژوهش (اثر الگوریتم بر اطلاعات، انتخاب و مشارکت شهروندی) (Castells, 2009; Littlejohn & Foss, 2011).",
        evolution="مفهوم سواد الگوریتمی از پژوهش‌های الگوریتم و رسانه‌های اجتماعی (دههٔ ۲۰۱۰، با رشد نوارهای خبری شخصی‌سازی‌شده) وارد علوم ارتباط شد و در آغاز یک زیرمفهوم بود؛ با رشد پلتفرم‌های شخصی‌سازی‌شده و هوش مصنوعی، به «میدان نوظهور» مستقل تبدیل شده است؛ و اکنون به‌عنوان زیرشاخه‌ای از سواد دیجیتال، رسانه‌ای و داده‌ای در حال شکل‌گیری و تعریف است (Castells, 2009).",
        assumptions="فرض‌های نهفته: الگوریتم، بر توزیع و دریافت محتوا اثر معنادار می‌گذارد (نه صرفاً ابزار خنثی)؛ کاربر، می‌تواند تا حدی اثر الگوریتم را درک و کنترل کند (با وجود محدودیت شفافیت و جعبه‌سیاه‌بودن)؛ سواد الگوریتمی، بر دموکراسی اطلاعاتی و آزادی انتخاب اثر می‌گذارد؛ و این سواد، نیازمند شفافیت بیشتر از سوی پلتفرم‌ها است (Castells, 2009; Littlejohn & Foss, 2011).",
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
                    (code, json.dumps({"batch": 306, "score": score, "words": words,
                                       "sources": n_sources, "verified": n_verified,
                                       "relations": n_rel, "rubric": detail}, ensure_ascii=False), STAMP, NOW))
        print(code, "words", words, "score", score, "detail", detail)
    conn.commit()
    conn.close()
    print("BATCH306 DONE")


if __name__ == "__main__":
    main()
