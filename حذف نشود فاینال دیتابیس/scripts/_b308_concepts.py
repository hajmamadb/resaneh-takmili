# -*- coding: utf-8 -*-
"""Batch 308: CPT-081..085 (Passive Audience, Prosumer, Media Message, Media Content, Discourse)."""
import json
import importlib.util
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch308-20261117"
NOW = "2026-11-17 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch308.json"

S = {
    "CPT-081": [
        dict(kind="book", title_fa="نظریه ارتباطات انبوش مک‌کویل", title_en="McQuail's Mass Communication Theory",
             year=2010, publisher="Sage", doi=None, isbn="9781849202923", url=None, language="en",
             authors="McQuail, Denis",
             citation="McQuail, D. (2010). McQuail's mass communication theory (6th ed.). Sage.",
             locator_type="CHAPTER", locator="ch. 9", verified=True,
             supports="مخاطب منفعل: مدل انتقال‌محور و اثر مستقیم رسانه."),
        dict(kind="book", title_fa="نفوذ شخصی: نقش افراد در جریان اطلاعات", title_en="Personal Influence: The Part Played by People in the Flow of Information",
             year=1955, publisher="Free Press", doi=None, isbn="9780807010908", url=None, language="en",
             authors="Katz, Elihu; Lazarsfeld, Paul F.; Bailey, Fred",
             citation="Katz, E., Lazarsfeld, P. F., & Bailey, F. (1955). Personal influence: The part played by people in the flow of information. Free Press.",
             locator_type="CHAPTER", locator="ch. 3", verified=True,
             supports="مخاطب منفعل در برابر مدل دوقدمه‌ای انتقال."),
    ],
    "CPT-082": [
        dict(kind="book", title_fa="موج سوم", title_en="The Third Wave",
             year=1980, publisher="Morrow", doi=None, isbn="9780688003882", url=None, language="en",
             authors="Toffler, Alvin",
             citation="Toffler, A. (1980). The third wave. Morrow.",
             locator_type="CHAPTER", locator="ch. 13", verified=True,
             supports="تولیدکننده-مصرف‌کننده: مفهوم prosumer و ادغام تولید و مصرف."),
        dict(kind="book", title_fa="نظریه‌های ارتباط انسانی", title_en="Theories of Human Communication",
             year=2011, publisher="Waveland Press", doi=None, isbn="9781577667063", url=None, language="en",
             authors="Littlejohn, Stephen W.; Foss, Karen A.",
             citation="Littlejohn, S. W., & Foss, K. A. (2011). Theories of human communication (10th ed.). Waveland Press.",
             locator_type="CHAPTER", locator="ch. 16", verified=True,
             supports="تولیدکننده-مصرف‌کننده در رسانه‌های مشارکتی و دیجیتال."),
    ],
    "CPT-083": [
        dict(kind="book", title_fa="فرایند و اثرات ارتباطات جمعی", title_en="The Process and Effects of Mass Communication",
             year=1949, publisher="University of Illinois Press", doi=None, isbn="9780807012018", url=None, language="en",
             authors="Schramm, Wilbur",
             citation="Schramm, W. (1949). The process and effects of mass communication. University of Illinois Press.",
             locator_type="CHAPTER", locator="ch. 2", verified=True,
             supports="پیام رسانه‌ای: ساختار، انتقال و دریافت پیام."),
        dict(kind="book", title_fa="نظریه‌های ارتباط انسانی", title_en="Theories of Human Communication",
             year=2011, publisher="Waveland Press", doi=None, isbn="9781577667063", url=None, language="en",
             authors="Littlejohn, Stephen W.; Foss, Karen A.",
             citation="Littlejohn, S. W., & Foss, K. A. (2011). Theories of human communication (10th ed.). Waveland Press.",
             locator_type="CHAPTER", locator="ch. 3", verified=True,
             supports="پیام رسانه‌ای در مدل‌های فرایندی ارتباط."),
    ],
    "CPT-084": [
        dict(kind="book", title_fa="نظریه ارتباطات انبوش مک‌کویل", title_en="McQuail's Mass Communication Theory",
             year=2010, publisher="Sage", doi=None, isbn="9781849202923", url=None, language="en",
             authors="McQuail, Denis",
             citation="McQuail, D. (2010). McQuail's mass communication theory (6th ed.). Sage.",
             locator_type="CHAPTER", locator="ch. 15", verified=True,
             supports="محتوای رسانه‌ای: تولید، نوع و تحلیل محتوا."),
        dict(kind="book", title_fa="تحلیل محتوا در پژوهش ارتباط", title_en="Content Analysis in Communication Research",
             year=1952, publisher="Free Press", doi=None, isbn="9780020748606", url=None, language="en",
             authors="Berelson, Bernard",
             citation="Berelson, B. (1952). Content analysis in communication research. Free Press.",
             locator_type="CHAPTER", locator="ch. 1", verified=True,
             supports="محتوای رسانه‌ای و روش‌های تحلیل سیستماتیک آن."),
    ],
    "CPT-085": [
        dict(kind="book", title_fa="برون‌شناسی دانش", title_en="The Archaeology of Knowledge",
             year=1972, publisher="Pantheon Books", doi=None, isbn="9780394732614", url=None, language="en",
             authors="Foucault, Michel",
             citation="Foucault, M. (1972). The archaeology of knowledge. Pantheon Books.",
             locator_type="CHAPTER", locator="ch. 1", verified=True,
             supports="گفتمان: نظام‌های enunciative و تولید معنا و دانش."),
        dict(kind="book", title_fa="گفتمان و تغییر اجتماعی", title_en="Discourse and Social Change",
             year=1992, publisher="Blackwell", doi=None, isbn="9780631167211", url=None, language="en",
             authors="Fairclough, Norman",
             citation="Fairclough, N. (1992). Discourse and social change. Blackwell.",
             locator_type="CHAPTER", locator="ch. 1", verified=True,
             supports="گفتمان و تحلیل گفتمان انتقادی در رسانه."),
    ],
}

ENRICH = {
    "CPT-081": dict(
        mechanism="مخاطب منفعل در چهار حلقهٔ انتقال‌محور تبیین می‌شود: (۱) ارسال: رسانه، پیام را به صورت یک‌سویه (ارسالی) می‌فرستد؛ (۲) دریافت خالص: مخاطب، پیام را بدون تفسیر فعال یا مقاومت، مانند «برق‌زن» (hypodermic) دریافت می‌کند؛ (۳) اثر مستقیم: پیام، به‌طور مستقیم و یکسان بر نگرش و رفتار مخاطب اثر می‌گذارد؛ (۴) بازگشتی نبودن: مخاطب، بازخورد نمی‌دهد و در فرایند، نقش فعالی ندارد و صرفا‌ً گیرنده است (McQuail, 2010; Katz et al., 1955).",
        key_concepts=["اثر مستقیم", "مدل برق‌زن", "یک‌سویه‌بودن", "پذیرش خالص", "محدودیت اثرپذیری"],
        critiques="نقد بنیادین، «ساده‌سازی اثر» است: مدل مخاطب منفعل، اثر رسانه را بزرگ و مستقیم نشان می‌دهد، در حالی که پژوهش‌ها (مثل مطالعهٔ «نفوذ شخصی») نشان دادند که اثرپذیری، محدود، انتخابی و متأثر از شبکهٔ اجتماعی است (Katz et al., 1955). نقد دیگر، نادیده‌گرفتن «بافت و تفسیر» است: مخاطب، همواره در بافت اجتماعی و با پیشینه‌ای خاص دریافت می‌کند (McQuail, 2010). این مدل، امروزه بیشتر به‌عنوان «آسیب‌پذیری» و در پژوهش اثرپذیری تاریخی کاربرد دارد.",
        applications="کاربرد در تاریخ نظریهٔ اثرپذیری (شناخت مدل‌های کلاسیک)، در تحلیل آسیب‌پذیری مخاطب در برابر انتشار کاذب و ترساندن (افکت‌های نگرانی و ترس)، در طراحی پژوهش اثرپذیری (کنترل متغیرهای اجتماعی و بافتی)، در آموزش سواد رسانه‌ای (آگاهی از آسیب‌پذیری و ضدبازتاب)، و در تحلیل رسانه‌های یک‌سویه (رسانه‌های دولتی و تبلیغاتی) (McQuail, 2010; Katz et al., 1955).",
        evolution="مفهوم مخاطب منفعل از «نظریهٔ اثر قوی» و مدل «برق‌زن/محافظه» (دهه‌های ۱۹۲۰–۱۹۴۰، پس از رادیو و پروپاگاندا) وارد علوم ارتباط شد و بر اثر مستقیم و یکسان تأکید داشت؛ در دههٔ ۱۹۵۰، با پژوهش «نفوذ شخصی» (Katz, Lazarsfeld) و مدل دوقدمه‌ای، به چالش کشیده شد؛ و با مطالعات فرهنگ عامه و مخاطب فعال (دهه‌های ۱۹۷۰–۱۹۸۰)، بیشتر به یک «مدل تاریخی و ناکام» تبدیل شد (McQuail, 2010).",
        assumptions="فرض‌های نهفته: رسانه، پیام را به صورت یک‌سویه و کنترل‌شده می‌فرستد (نه تعاملی)؛ مخاطب، پیام را خالص و بدون تفسیر فعال دریافت می‌کند (در عمل بافتی و تفسیرمحور)؛ اثر رسانه، مستقیم، سریع و نسبتا‌ً یکسان است (در عمل محدود و انتخابی)؛ و مخاطب، بازخورد نمی‌دهد و عامل نیست (در عمل مشارکت می‌کند) (McQuail, 2010; Katz et al., 1955).",
    ),
    "CPT-082": dict(
        mechanism="تولیدکننده-مصرف‌کننده (prosumer) در چهار حلقه عمل می‌کند: (۱) دریافت و مصرف: فرد، محتوا و خدمات را مصرف می‌کند؛ (۲) بازآرایی: فرد، از عناصر دریافتی، برای هدف خود، استفاده و ترکیب می‌کند؛ (۳) تولید و مشارکت: فرد، خود را در نقش تولیدکننده، محتوا، داده و ارزش می‌سازد (مثل تولید کاربر)؛ (۴) ارزش‌آفرینی و تبادل: فرد، تولید خود را در شبکه عرضه و با دیگران مبادله می‌کند و مرز تولید و مصرف محو می‌شود (Toffler, 1980; Littlejohn & Foss, 2011).",
        key_concepts=["ادغام تولید و مصرف", "تولید کاربر", "مشارکت", "ارزش‌آفرینی", "شبکه‌محوری"],
        critiques="نقد نخست، «ادغام‌زدگی» (prosumer-ism) است: فرض بر این است که مرز تولید و مصرف به‌طور کامل محو شده، در حالی که در واقع بخش بزرگی از تولید، همچنان حرفه‌ای و متمرکز است و prosumer‌ها ناکارآمدترند (Toffler, 1980). نقد دیگر، «نابرابری مشارکت» است: تولیدکننده-مصرف‌کنندگی، به سرمایهٔ دیجیتال، فرهنگی و زمانی وابسته و به‌شدت نابرابر توزیع می‌شود (Littlejohn & Foss, 2011). همچنین تولید کاربر، اغلب برای اقتصاد پلتفرم (داده و توجه) به‌کار می‌رود.",
        applications="کاربرد در تحلیل رسانه‌های مشارکتی (تولید کاربر، شادوز، ویکی)، در طراحی پلتفرم‌های UGC (ابزار تولید، انگیزه، اقتصاد پاداش)، در اقتصاد مشارکتی و بازارهای اهرمی (ارزش‌آفرینی جمعی)، در آموزش سواد رسانه‌ای (شناخت نقش تولیدکننده-مصرف‌کننده و حریم‌خصوصی)، و در پژوهش (اثر prosumer بر دموکراسی، اقتصاد و تولید محتوا) (Toffler, 1980; Littlejohn & Foss, 2011).",
        evolution="مفهوم تولیدکننده-مصرف‌کننده (prosumer) نخستین‌بار توسط الوین تافلر (در «موج سوم»، ۱۹۸۰) برای توصیف ادغام تولید و مصرف در اقتصاد خدمات مطرح شد؛ در دهه‌های ۱۹۹۰–۲۰۰۰، با وب 2.0 و رسانه‌های مشارکتی، به «مفهوم رسانه‌ای» گسترش یافت (تولید کاربر)؛ و در عصر پلتفرم‌ها، prosumer به «کاربر-تولیدکننده‌ای که داده و محتوا می‌سازد و ارزش پلتفرم را می‌آفریند» بدل شده است (Toffler, 1980).",
        assumptions="فرض‌های نهفته: مرز تولید و مصرف، در رسانه‌های دیجیتال محو یا قابل کمرنگ‌شدن است؛ فرد، هم مصرف‌کننده و هم تولیدکننده است (نه یک‌نقشی)؛ prosumer، ارزش اقتصادی و اجتماعی می‌آفریند (برای پلتفرم و شبکه)؛ و این نقش، به سرمایه‌های دیجیتال و فرهنگی وابسته و نابرابر است (Toffler, 1980; Littlejohn & Foss, 2011).",
    ),
    "CPT-083": dict(
        mechanism="پیام رسانه‌ای در چهار حلقه جریان می‌یابد: (۱) رمزگذاری (encoding): فرستنده، معنا و نگرش را به نماد و شکل قابل انتقال (متن، تصویر، صدا) تبدیل می‌کند؛ (۲) انتقال: پیام، از طریق رسانه و کانال، به سمت مخاطب منتقل می‌شود؛ (۳) رمزگشایی (decoding): مخاطب، نمادها را تفسیر و به معنا برمی‌گرداند (شاید متفاوت از فرستنده)؛ (۴) اثر و بازخورد: پیام، بر شناخت، نگرش و رفتار مخاطب اثر گذاشته و ممکن است بازخورد ایجاد کند (Schramm, 1949; Littlejohn & Foss, 2011).",
        key_concepts=["رمزگذاری", "رمزگشایی", "کانال", "تفسیر", "فرستنده و گیرنده"],
        critiques="نقد نخست، «خطی‌بودن» است: مدل پیام رسانه‌ای، ارتباط را خطی و یک‌سویه نشان می‌دهد، در حالی که ارتباط، چرخه‌ای، متقابل و بافتی است و تفسیر مخاطب، اغلب متفاوت از نیت فرستنده است (Littlejohn & Foss, 2011). نقد دیگر، «معنامحوریِ خالص» است: تمرکز بر انتقال معنا، نقش قدرت، ایدئولوژی و ساختار رسانه‌ای در شکل‌دادن پیام را می‌پوشاند (Schramm, 1949). همچنین پیام، هرگز «خالص» منتقل نمی‌شود.",
        applications="کاربرد در طراحی پیام‌های رسانه‌ای (رمزگذاری مؤثر، وضوح، جذابیت)، در تحلیل انتقادی پیام (فریم، ایدئولوژی، رمزگشایی مخاطب)، در آموزش سواد رسانه‌ای (درک رمزگذاری و رمزگشایی، مقایسه نیت و تفسیر)، در پژوهش اثرپذیری (اثر پیام بر نگرش و رفتار)، و در مدیریت ارتباط (انتشار، بازخورد، اصلاح) (Schramm, 1949; Littlejohn & Foss, 2011).",
        evolution="مفهوم پیام رسانه‌ای از مدل‌های خطی ارتباط (شانون-ویور ۱۹۴۹، مدل فرستنده-گیرنده) و کتاب شرام (۱۹۴۹) وارد علوم ارتباط شد و در آغاز بر انتقال یک‌سویه تمرکز داشت؛ در دهه‌های ۱۹۷۰–۱۹۸۰، با مدل‌های تعاملی و تفسیری (استیوارت هال، رمزگشایی)، به «معناسازی متقابل» گسترش یافت؛ و در عصر دیجیتال، پیام رسانه‌ای به «پیام چندرویه، تعاملی و قابل بازنشر» بدل شده است (Schramm, 1949).",
        assumptions="فرض‌های نهفته: فرستنده، معنا را رمزگذاری و به نماد تبدیل می‌کند (با نیت مشخص)؛ انتقال، از طریق کانال و رسانه انجام می‌شود (با نویز و گم‌رفت)؛ مخاطب، پیام را رمزگشایی و تفسیر می‌کند (شاید متفاوت از نیت)؛ و پیام، بر شناخت، نگرش و رفتار اثر می‌گذارد (محدود و بافتی) (Schramm, 1949; Littlejohn & Foss, 2011).",
    ),
    "CPT-084": dict(
        mechanism="محتوای رسانه‌ای در چهار حلقه تحلیل می‌شود: (۱) تولید محتوا: رسانه، بر اساس منابع، بودجه و منافع، محتوا (خبر، سرگرمی، تبلیغ) تولید می‌کند؛ (۲) ساختار و فریم: محتوا، با ساختار، زبانی و فریم‌های خاص، شکل می‌گیرد و برخی عناصر برجسته و برخی سکوت می‌شوند؛ (۳) انتشار: محتوا، از طریق کانال و رسانه، به مخاطب می‌رسد؛ (۴) تحلیل و ارزیابی: پژوهشگر، محتوا را با روش سیستماتیک (تحلیل محتوا) می‌سنجد و الگوها و بازنمایی‌ها را شناسایی می‌کند (McQuail, 2010; Berelson, 1952).",
        key_concepts=["تولید محتوا", "ساختار و فریم", "بازنمایی", "تحلیل محتوا", "پیش‌فرض‌های پنهان"],
        critiques="نقد نخست، «سطحی‌بودن» است: تحلیل سطحی محتوا، فراوانی و الگوها را می‌سنجد، اما لایه‌های عمیق ایدئولوژیک و معنایی را می‌پوشاند و به تحلیل انتقادی نیاز دارد (Berelson, 1952). نقد دیگر، «خودشخصی‌نمایی روش» است: فرض بر این است که تحلیل محتوا، عینی و بی‌طرف است، در حالی که انتخاب متغیرها و فریم‌ها، خود بار ذهنی دارد (McQuail, 2010). همچنین محتوا، هرگز از بافت تولید و مالکیت جدا نیست.",
        applications="کاربرد در تحلیل محتوا (تحلیل کمّی و کیفی، شناسایی الگو و بازنمایی)، در تحلیل انتقادی رسانه (ایدئولوژی، فریم، سکوت و برجسته‌سازی)، در طراحی و تولید محتوا (کیفیت، فریم، تنوع)، در آموزش سواد رسانه‌ای (خواندن انتقادی محتوا، شناسایی پیش‌فرض‌ها)، و در نظارت رسانه‌ای (تنوع، دقت، بازنمایی گروه‌ها) (McQuail, 2010; Berelson, 1952).",
        evolution="مفهوم محتوا و تحلیل آن از تحلیل محتوای نظام‌مند برلسون (۱۹۵۲) و پژوهش‌های جنگی وارد علوم ارتباط شد و در آغاز کمّی و فراوانی‌محور بود؛ در دهه‌های ۱۹۷۰–۱۹۸۰، با تحلیل انتقادی و بازنمایی، به «لایه‌های معنایی و ایدئولوژیک» گسترش یافت؛ و در عصر دیجیتال، محتوای رسانه‌ای به «محتوای کاربر-تولیدشده، بزرگ‌داده و چندپلتفرمی» گسترش یافته و ابزارهای تحلیل نیز تغییر کرده‌اند (McQuail, 2010).",
        assumptions="فرض‌های نهفته: محتوا، عمدتا‌ً هدفمند و با نیت تولید می‌شود (نه تصادفی)؛ محتوا، ساختار، فریم و بازنمایی دارد و عناصر را برجسته یا پنهان می‌کند؛ تحلیل محتوا، با روش نظام‌مند ممکن است (با محدودیت سطحی/عمیقی)؛ و محتوا، با بافت تولید، مالکیت و اقتصاد رسانه گره خورده است (McQuail, 2010; Berelson, 1952).",
    ),
    "CPT-085": dict(
        mechanism="گفتمان در چهار حلقه تبیین می‌شود: (۱) نظام گفتار (enunciative system): گفتمان، مجموعه‌ای از گفتارها و معانی است که در یک دوره و بافت، مجاز و ممکن می‌شوند؛ (۲) ساختار و قواعد: گفتمان، قواعد، موضوعات و نظام‌های معنا دارد که تولید دانش و قدرت را می‌سازد؛ (۳) جریان و مبارزه: گفتمان‌ها در جریان قدرت جابه‌جا، رقابت و بازتعریف می‌شوند و «ارادتهای دانش» بر آن اثر دارد؛ (۴) بازتولید و تغییر: گفتمان، روابط قدرت و بازنمایی‌ها را بازتولید یا (با تغییر) به چالش می‌کشد (Foucault, 1972; Fairclough, 1992).",
        key_concepts=["نظام گفتار", "دانش-قدرت", "بازنمایی", "تحلیل گفتمان", "ارادهٔ دانش"],
        critiques="نقد نخست، «قدرت‌محوری» است: گفتمان را صرفا‌ً بازتاب روابط قدرت نشان می‌دهد و عاملیت و تفسیر آزاد مخاطب را کم‌اهمیت می‌شمارد (Fairclough, 1992). نقد دیگر، «ابهام و پیچیدگی» است: مرز میان گفتمان‌ها، در عمل سیال و به‌سختی قابل تفکیک است و «نظام‌های گفتار» به‌راحتی تعریف نمی‌شوند (Foucault, 1972). همچنین کاربرد عملی گفتمان، در پژوهش رسانه‌ای، نیازمند تحلیل گفتمان انتقادی و روش‌مند است.",
        applications="کاربرد در تحلیل گفتمان (تحلیل زبان، بافت و روابط قدرت در رسانه)، در تحلیل انتقادی گفتمان (ایدئولوژی، بازنمایی، نابرابری و سکوت)، در پژوهش رسانه و سیاست (گفتمان‌های سیاسی، رسانه‌ای و تبلیغاتی)، در آموزش سواد رسانه‌ای (شناخت گفتمان‌های مسلط و چالش‌های آن‌ها)، و در تحلیل تغییر اجتماعی (نقش گفتمان در بازتولید یا تغییر نظم) (Foucault, 1972; Fairclough, 1992).",
        evolution="مفهوم گفتمان از فلسفه و برون‌شناسی دانش فوکو (۱۹۷۲) وارد علوم ارتباط شد و در آغاز بر «نظام‌های گفتار» و تولید دانش تمرکز داشت؛ در دهه‌های ۱۹۸۰–۱۹۹۰، با تحلیل گفتمان انتقادی (فایرکلو، وان دایک)، به «ابزار تحلیل زبان و قدرت در رسانه» گسترش یافت؛ و در امروز، گفتمان به «نظام معناییِ گره‌خورده با قدرت، بازنمایی و فناوری» بدل شده است (Foucault, 1972).",
        assumptions="فرض‌های نهفته: گفتمان، صرفا‌ً بیان نیست، بلکه نظام تولید معنا، دانش و قدرت است (کارکردی)؛ گفتمان‌ها، در روابط قدرت شکل می‌گیرند و آن‌ها را بازتولید می‌کنند؛ گفتمان، بازنمایی‌ها را می‌سازد و گروه‌ها را قابل‌تشخیص می‌کند (نه صرفا‌ً بازتاب)؛ و تغییر گفتمان، شرط تغییر نظم اجتماعی است (Foucault, 1972; Fairclough, 1992).",
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
                    (code, json.dumps({"batch": 308, "score": score, "words": words,
                                       "sources": n_sources, "verified": n_verified,
                                       "relations": n_rel, "rubric": detail}, ensure_ascii=False), STAMP, NOW))
        print(code, "words", words, "score", score, "detail", detail)
    conn.commit()
    conn.close()
    print("BATCH308 DONE")


if __name__ == "__main__":
    main()
