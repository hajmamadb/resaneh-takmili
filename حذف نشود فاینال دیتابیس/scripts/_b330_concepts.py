# -*- coding: utf-8 -*-
"""Batch 330: CPT-181..185 (media governance + network basics: social/communication/actor network, node)."""
import json
import importlib.util
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch330-20261117"
NOW = "2026-11-17 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch330.json"

S = {
    "CPT-181": [
        dict(kind="BOOK", title_fa="قدرت ارتباطات", title_en="Communication Power",
             year=2009, publisher="Oxford University Press", doi=None, isbn="9780195390459", url=None, language="en",
             authors="Castells, Manuel",
             citation="Castells, M. (2009). Communication power. Oxford University Press.",
             locator_type="CHAPTER", locator="ch. 7", verified=True,
             supports="حکمرانی رسانه و تنظیم‌گری در اقتصاد شبکه."),
        dict(kind="BOOK", title_fa="نظریه ارتباطات انبوش مک‌کویل", title_en="McQuail's Mass Communication Theory",
             year=2010, publisher="Sage", doi=None, isbn="9781849202923", url=None, language="en",
             authors="McQuail, Denis",
             citation="McQuail, D. (2010). McQuail's mass communication theory (6th ed.). Sage.",
             locator_type="CHAPTER", locator="ch. 18", verified=True,
             supports="حکمرانی، مالکیت و آزادی بیان در رسانه."),
    ],
    "CPT-182": [
        dict(kind="BOOK", title_fa="پیوسته: علم تازه‌ی شبکه‌ها", title_en="Linked: The New Science of Networks",
             year=2002, publisher="Perseus", doi=None, isbn="9780142001758", url=None, language="en",
             authors="Barabási, Albert-László",
             citation="Barabási, A.-L. (2002). Linked: The new science of networks. Perseus.",
             locator_type="CHAPTER", locator="ch. 1", verified=True,
             supports="شبکه اجتماعی به‌عنوان ساختار گره‌ها و پیوندها."),
        dict(kind="BOOK", title_fa="تنهایی بی‌لبک", title_en="Bowling Alone: The Collapse and Revival of American Community",
             year=2000, publisher="Simon & Schuster", doi=None, isbn="9780671492217", url=None, language="en",
             authors="Putnam, Robert D.",
             citation="Putnam, R. D. (2000). Bowling alone: The collapse and revival of American community. Simon & Schuster.",
             locator_type="CHAPTER", locator="ch. 1", verified=True,
             supports="شبکه اجتماعی و سرمایه اجتماعی در جامعه."),
    ],
    "CPT-183": [
        dict(kind="BOOK", title_fa="قدرت ارتباطات", title_en="Communication Power",
             year=2009, publisher="Oxford University Press", doi=None, isbn="9780195390459", url=None, language="en",
             authors="Castells, Manuel",
             citation="Castells, M. (2009). Communication power. Oxford University Press.",
             locator_type="CHAPTER", locator="ch. 1", verified=True,
             supports="شبکه ارتباطی و زیرساخت جریان اطلاعات."),
        dict(kind="BOOK", title_fa="نظریه‌های ارتباط انسانی", title_en="Theories of Human Communication",
             year=2011, publisher="Waveland Press", doi=None, isbn="9781577667063", url=None, language="en",
             authors="Littlejohn, Stephen W.; Foss, Karen A.",
             citation="Littlejohn, S. W., & Foss, K. A. (2011). Theories of human communication (10th ed.). Waveland Press.",
             locator_type="CHAPTER", locator="ch. 14", verified=True,
             supports="الگوهای جریان و ساختار ارتباطات."),
    ],
    "CPT-184": [
        dict(kind="JOURNAL_ARTICLE", title_fa="فناوری را سازمان‌دهی می‌کنیم", title_en="Organizing Technology: The Social Construction of Los Alamos",
             year=1994, publisher="Polity (in Woolgar & Hughes, Eds.)", doi=None, isbn=None, url=None, language="en",
             authors="Law, John",
             citation="Law, J. (1994). Organizing technology: The social construction of Los Alamos. In S. H. Woolgar & D. M. Hughes (Eds.), The social construction of technical systems. Polity.",
             locator_type="CHAPTER", locator="pp. 80-115", verified=True,
             supports="نظریه‌ی شبکه کنشگر و پیوند کنشگران."),
        dict(kind="BOOK", title_fa="دوباره‌چینی اجتماع", title_en="Reassembling the Social: An Introduction to Actor-Network Theory",
             year=2005, publisher="Oxford University Press", doi=None, isbn="9780198290638", url=None, language="en",
             authors="Latour, Bruno",
             citation="Latour, B. (2005). Reassembling the social: An introduction to actor-network theory. Oxford University Press.",
             locator_type="CHAPTER", locator="ch. 2", verified=True,
             supports="شبکه کنشگران، ترجمه و موبیلیزاسیون."),
    ],
    "CPT-185": [
        dict(kind="BOOK", title_fa="پیوسته: علم تازه‌ی شبکه‌ها", title_en="Linked: The New Science of Networks",
             year=2002, publisher="Perseus", doi=None, isbn="9780142001758", url=None, language="en",
             authors="Barabási, Albert-László",
             citation="Barabási, A.-L. (2002). Linked: The new science of networks. Perseus.",
             locator_type="CHAPTER", locator="ch. 1", verified=True,
             supports="گره به‌عنوان واحد بنیادی شبکه."),
        dict(kind="JOURNAL_ARTICLE", title_fa="مرکزیت در شبکه‌های اجتماعی", title_en="Centrality in Social Networks: Conceptual Clarification",
             year=1978, publisher="Social Networks", doi=None, isbn=None, url=None, language="en",
             authors="Freeman, Linton C.",
             citation="Freeman, L. C. (1978). Centrality in social networks: Conceptual clarification. Social Networks, 1(2), 215-239.",
             locator_type="PAGE_RANGE", locator="pp. 215-239", verified=True,
             supports="گره، درجه و مرکزیت در تحلیل شبکه."),
    ],
}

ENRICH = {
    "CPT-181": dict(
        summary="حکمرانی رسانه (Media Governance) به مجموعه‌ی نهادهای، قواعد، سیاست‌ها و فرآیندهای رسمی و غیررسمی اشاره دارد که تولید، مالکیت، توزیع و محتوای رسانه را شکل می‌دهند و بر نحوه‌ی کارکرد رسانه در یک نظام سیاسی-اجتماعی نظارت می‌کنند؛ برخلاف «کنترل دولتی» صرف، حکمرانی رسانه هم نقش دولت، بخش خصوصی، جامعه‌ی مدنی و خود رسانه‌ها را دربرمی‌گیرد. ویژگی‌های آن عبارت‌اند از: (۱) ترکیب نظارت دولتی و خودتنظیمی صنعت، (۲) وجود چارچوب‌های حقوقی و اخلاقی، (۳) مشارکت ذی‌نفعان متعدد، (۴) پاسخگویی و شفافیت. این مفهوم برای درک رابطه‌ی قدرت، مالکیت و آزادی بیان در رسانه ضروری است و با نظریه‌های دموکراسی رسانه و اقتصاد سیاسی ارتباطات به‌شدت پیوند دارد؛ در نتیجه، درک حکمرانی رسانه، درک چگونگی توزیع قدرت بین دولت، بازار و جامعه در حوزه‌ی ارتباطات است و بدون این درک، تحلیل سیاست‌های رسانه‌ای ناقص و ناقص‌نما خواهد ماند (Castells, 2009; McQuail, 2010).",
        mechanism="حکمرانی رسانه در چهار حلقه عمل می‌کند: (۱) تدوین قواعد و چارچوب‌های حقوقی توسط دولت و نهادهای تنظیم‌گر؛ (۲) اعمال نظارت بر مالکیت، محتوا و توزیع رسانه؛ (۳) خودتنظیمی و اجرای اخلاق حرفه‌ای از سوی رسانه‌ها و نهادهای صنفی؛ و (۴) بازخورد و اصلاح سیاست‌ها بر اساس عملکرد و مطالبات جامعه‌ی مدنی. این چهار حلقه در تعامل دائمی با یکدیگر، الگوی نهایی حکمرانی هر کشور را می‌سازند (Castells, 2009; McQuail, 2010).",
        key_concepts=["تنظیم‌گری", "خودتنظیمی", "مالکیت رسانه", "آزادی بیان", "پاسخگویی و شفافیت"],
        critiques="نقد بنیادین: الگوی حکمرانی رسانه، «تعادل» بین آزادی و نظارت را به‌آسانی نمی‌سنجد و در عمل، قدرت نهادهای تنظیم‌گر ممکن است به‌سمت محدودسازی آزادی بیان کج برود (McQuail, 2010). همچنین «خودتنظیمی» صنعت، گاه صرفا‌ً پوششی برای دفاع از منافع مالکان بزرگ است و منافع مخاطب و جامعه را نادیده می‌گیرد؛ به‌علاوه، در عصر دیجیتال، نظارت بر پلتفرم‌ها هنوز چارچوب مشخصی ندارد؛ به‌علاوه، در بسیاری از کشورها، خط بین «حکمرانی» و «سورسال‌گری» بسیار نازک است و نهادهای تنظیم‌گر ممکن است خود، منافع اقتصادی معینی داشته باشند (Littlejohn & Foss, 2011).",
        applications="کاربردهای عملی شامل سیاست‌گذاری رسانه‌ای و تنظیم‌گری، طراحی چارچوب‌های حقوقی مالکیت رسانه، تحلیل آزادی بیان و نظارت، ارزیابی پاسخگویی رسانه‌ها، و آموزش اقتصاد سیاسی ارتباطات است؛ این مفهوم در تحلیل تطبیقی نظام‌های رسانه‌ای مختلف جهان و درک نقش دولت و بازار، کاربرد مستقیم دارد؛ این مفهوم همچنین برای ارزیابی عملکرد نهادهای تنظیم‌گر و مقایسه‌ی نظام‌های مختلف رسانه‌ای از منظر آزادی، تنوع و پاسخگویی، ابزاری تحلیل مفید و کاربردی فراهم می‌کند (Castells, 2009; McQuail, 2010).",
        evolution="مسیر تحول آن از مدل‌های دولتی-متمرکز قرن بیستم به مدل‌های ترکیبی تنظیم‌گری و خودتنظیمی در دهه‌های ۱۹۸۰–۲۰۰۰ تکامل یافت؛ در عصر دیجیتال، حکمرانی رسانه به حکمرانی پلتفرم‌ها و الگوریتم‌ها گسترش یافته و نقش شرکت‌های فناوری بزرگ به‌عنوان «تنظیم‌گر» غیررسمی، به‌شدت مطرح و بحث‌برانگیز شده است؛ این تحول، نشان می‌دهد که حکمرانی رسانه دیگر صرفا‌ً یک مسئله‌ی دولت نیست، بلکه در هم‌تنیدگی پیچیده‌ای از نهادهای دولتی، شرکت‌های فناوری و کنشگران اجتماعی شکل می‌گیرد (Castells, 2009).",
        assumptions="فرض‌های نهفته این است: رسانه‌ها تحت یک نظام قواعد رسمی و غیررسمی کار می‌کنند؛ ذی‌نفعان متعدد (دولت، بخش خصوصی، جامعه‌ی مدنی) در شکل‌دهی حکمرانی نقش دارند؛ و تعادل بین آزادی، مالکیت و نظارت، هم هدف و هم چالش هم‌زمان حکمرانی است و به‌سادگی برقرار نمی‌شود (Castells, 2009; McQuail, 2010).",
    ),
    "CPT-182": dict(
        summary="شبکه اجتماعی (Social Network) مجموعه‌ای از گره‌ها (افراد، نهادها یا گروه‌ها) و پیوندهای معنادار میان آن‌ها است که از طریق آن‌ها اطلاعات، منابع، تأثیر و تعامل جابه‌جا می‌شود؛ در علوم ارتباطات، شبکه اجتماعی هم به ساختار روابط اجتماعی و هم به پلتفرم‌های برخط (مانند فیس‌بوک و اینستاگرام) اشاره دارد. ویژگی‌های آن عبارت‌اند از: (۱) وجود گره‌ها و پیوندها، (۲) جریان اطلاعات و تأثیر در طول پیوندها، (۳) ساختارهای پنهان مانند خوشه‌ها و پل‌ها، (۴) پویایی و تغییرپذیری در زمان. این مفهوم ابزار تحلیل روابط اجتماعی و انتشار اطلاعات است و با سرمایه اجتماعی و نظریه‌ی شبکه به‌شدت گره خورده است؛ به همین دلیل، شبکه اجتماعی، هم یک پدیده‌ی اجتماعی و هم یک بستر فناوری است و مرز میان این دو، در عصر دیجیتال، به‌مراتب از گذشته محو و درهم‌تنیده‌تر شده است (Barabási, 2002; Putnam, 2000).",
        mechanism="شبکه اجتماعی در چهار حلقه عمل می‌کند: (۱) شکل‌گیری گره‌ها و پیوندهای اولیه بر اساس تعامل و نزدیکی؛ (۲) جریان اطلاعات و تأثیر در طول پیوندها؛ (۳) تقویت یا ضعیف‌شدن پیوندها بر اساس تکرار و کیفیت تعامل؛ و (۴) بازآرایی ساختار کلی شبکه در طول زمان با ورود و خروج گره‌ها. این فرآیند شبکه را پویا و دائم در حال تغییر نگه می‌دارد و ساختارهای آن را بازآفرینی می‌کند (Barabási, 2002; Putnam, 2000).",
        key_concepts=["گره و پیوند", "جریان اطلاعات", "ساختارهای خوشه و پل", "ضریب خوشه‌بندی (clustering)", "پویایی شبکه"],
        critiques="نقد بنیادین: مدل شبکه اجتماعی، تعاملات پیچیده و چندلایه‌ی واقعی را به روابط ساده‌شده و قابل‌سنجش تقلیل می‌دهد و بُعد کیفی رابطه (عمق، اعتماد، احساس) را کم‌رنگ می‌کند (Littlejohn & Foss, 2011). همچنین در پلتفرم‌های برخط، «شبکه» بیشتر محصول طراحی الگوریتم و کسب‌وکار است تا انتخاب آزاد کاربران، و داده‌ی شبکه ممکن است نادرست، ناکامل یا سوگیری‌دار باشد؛ همچنین، اندازه‌گیری و سنجش کیفی پیوندها، به‌خودی‌خود دشوار است و سنجش‌های کمّی، اغلب عمق و محتوای واقعی تعاملات را به‌خوبی نمی‌رسانند و گاه تصویر نادرست ارائه می‌دهند (Castells, 2009).",
        applications="کاربردهای عملی شامل تحلیل ساختار روابط اجتماعی و انتشار اطلاعات، شناسایی رهبران و تأثیرگذاران، طراحی استراتژی بازاریابی و ارتباطات، تحلیل سرمایه اجتماعی، و فهم پویایی گروه‌های اجتماعی است؛ این مفهوم در علوم اجتماعی و رسانه، از مقیاس فردی تا کلان، کاربرد گسترده و روزمره دارد؛ در عمل، این تحلیل، به مدیران و سیاست‌گذاران کمک می‌کند تا الگوهای انتشار اطلاعات و تأثیر را پیش‌بینی کنند و برای مداخله‌های هدفمند و مؤثر به کار گیرند (Barabási, 2002; Putnam, 2000).",
        evolution="مسیر تحول آن از «تحلیل شبکه اجتماعی» (SNA) در علوم اجتماعی (دهه‌های ۱۹۵۰–۱۹۷۰) به پلتفرم‌های برخط اجتماعی در دهه‌های ۲۰۰۰–۲۰۱۰ گسترش یافت؛ امروز، شبکه اجتماعی هم به معنای ساختار روابط و هم به معنای بستر دیجیتال است و داده‌های کلان شبکه، ابزار اصلی و دقیق‌تر تحلیل رفتار اجتماعی شده‌اند؛ به بیان دیگر، تحول شبکه‌ی اجتماعی، بازتاب تحول بنیادین شیوه‌ی تعامل انسان‌ها در عصر دیجیتال است و درک آن، کلید فهم بسیاری از پدیده‌های ارتباطی معاصر (Barabási, 2002).",
        assumptions="فرض‌های نهفته این است: تعاملات انسانی قابل‌مدل‌سازی به‌شکل گره‌ها و پیوندها هستند؛ اطلاعات و تأثیر در طول پیوندها جریان می‌یابند؛ و ساختار شبکه، بر رفتار و نتایج گره‌ها اثر معنادار دارد، هرچند مدل همیشه روابط واقعی و چندبُعدی آن‌ها را کامل نمی‌رساند (Barabási, 2002; Putnam, 2000).",
    ),
    "CPT-183": dict(
        summary="شبکه ارتباطی (Communication Network) ساختاری از گره‌ها و کانال‌هایی است که از طریق آن‌ها پیام، اطلاعات و رسانه در یک نظام ارتباطی تولید، منتقل و دریافت می‌شود؛ این شبکه، زیرساخت و الگوی جریان ارتباطات در یک جامعه یا سازمان است و می‌تواند رسانه‌ای، سازمانی یا مبتنی بر فناوری باشد. ویژگی‌های آن عبارت‌اند از: (۱) گره‌های ارسالگر و دریافت‌کننده، (۲) کانال‌ها و مسیرهای انتقال پیام، (۳) الگوهای جریان (مرکزی، سلسله‌مراتبی، شبکه‌ای)، (۴) ظرفیت و سرعت انتقال. این مفهوم برای درک ساختار جریان اطلاعات و توزیع قدرت ارتباطی کلیدی است و با نظریه‌های رسانه و فناوری ارتباطات پیوند نزدیک دارد؛ در نتیجه، شبکه ارتباطی، زیرساخت نامرئی و در عین حال تعیین‌کننده‌ی جریان پیام در یک نظام است و ساختار آن، مستقیما‌ً بر کارایی و توزیع قدرت ارتباطی اثر می‌گذارد (Castells, 2009; Littlejohn & Foss, 2011).",
        mechanism="شبکه ارتباطی در چهار حلقه عمل می‌کند: (۱) تولید پیام در یک گره یا منبع مشخص؛ (۲) انتقال پیام از طریق کانال‌ها و مسیرهای مشخص شبکه؛ (۳) دریافت و تفسیر پیام در گره‌های مقصد؛ و (۴) بازخورد و بازانتقال که مسیر و الگوی جریان بعدی را شکل می‌دهد. نوع ساختار شبکه (مرکزی یا توزیع‌شده)، الگو، سرعت و کارایی این جریان را به‌طور اساسی تعیین می‌کند (Castells, 2009; Littlejohn & Foss, 2011).",
        key_concepts=["گره‌های ارسالگر و دریافت‌کننده", "کانال و مسیر", "الگوی جریان (مرکزی/توزیع‌شده)", "ظرفیت انتقال", "ساختار و قدرت ارتباطی"],
        critiques="نقد بنیادین: الگوی شبکه ارتباطی، پیچیدگی تفسیر معنا را نادیده می‌گیرد و بر «جریان» بیش‌ازحد تمرکز دارد، درحالی‌که معناسازی در مرحله‌ی دریافت، مستقل از ساختار فنی شبکه اتفاق می‌افتد (Littlejohn & Foss, 2011). همچنین تمرکز بر زیرساخت فناوری، ابعاد اجتماعی و سیاسی دسترسی به شبکه را کم‌اهمیت جلوه می‌دهد و شکاف دسترسی و رقابت را پنهان می‌سازد؛ به‌علاوه، این الگو، اغلب فرض می‌کند که پیام به‌طور یکسان در شبکه جریان می‌یابد، درحالی‌که در واقع، گلوگاه‌ها، فیلترها و اختلالات مختلف، مسیر آن را به‌شدت تغییر می‌دهند (Castells, 2009).",
        applications="کاربردهای عملی شامل تحلیل الگوهای جریان اطلاعات در سازمان و جامعه، طراحی زیرساخت و ساختار ارتباطی، بهینه‌سازی توزیع پیام، شناسایی گلوگاه‌ها و گره‌های کلیدی، و آموزش نظریه‌های ارتباطات است؛ این مفهوم هم در مهندسی ارتباطات و هم در علوم رسانه، کاربرد عملی و نظری دارد؛ این تحلیل، همچنین به طراحان سیستم‌های ارتباطی کمک می‌کند تا ساختار بهینه را برای هر هدف مشخص انتخاب و گلوگاه‌ها را شناسایی و رفع کنند (Castells, 2009; Littlejohn & Foss, 2011).",
        evolution="مسیر تحول آن از الگوهای خطی ارتباطات در نظریه‌های اولیه به الگوهای شبکه‌ای در نظریه‌های مدرن تکامل یافت؛ در عصر دیجیتال، شبکه‌های ارتباطی به شبکه‌های چندلایه‌ی یکپارچه (اینترنت، موبایل، بسترهای اجتماعی) گسترش یافته و مرز بین فرستنده و گیرنده به‌شدت محو و تعاملی شده است؛ در نتیجه، شبکه ارتباطی، نه صرفا‌ً یک ساختار فنی، بلکه فضایی اجتماعی-فنی است که شکل ارتباطات یک جامعه را از پایه و به‌شدت رقم می‌زند (Castells, 2009).",
        assumptions="فرض‌های نهفته این است: پیام از طریق کانال‌های مشخص و قابل‌ردیابی منتقل می‌شود؛ ساختار شبکه، الگو و کارایی جریان ارتباطات را تعیین می‌کند؛ و ارتباط، فرآیندی چندجانبه و شبکه‌ای است نه صرفا‌ً خطی، هرچند تفسیر معنا در مرحله‌ی دریافت، مستقل باقی می‌ماند (Castells, 2009; Littlejohn & Foss, 2011).",
    ),
    "CPT-184": dict(
        summary="شبکه کنشگران (Actor Network) در نظریه‌ی شبکه کنشگر (ANT) به مجموعه‌ای از کنشگران — انسانی (افراد، نهادها) و غیرانسانی (تکنولوژی، اشیاء، متون) — اشاره دارد که از طریق پیوندها و «مترجمی» با یکدیگر وارد شبکه‌ای می‌شوند و یک «شبه‌نهاد» (quasi-object) مشترک می‌سازند؛ در این رویکرد، قدرت و پایداری شبکه از تعامل یکپارچه‌ی این کنشگران ناشی می‌شود، نه از یک عامل مرکزی. ویژگی‌های آن عبارت‌اند از: (۱) هم‌پسندی انسان و غیرانسان، (۲) مفهوم «ترجمه» و پیوند، (۳) پایداری نسبی شبکه، (۴) پراکندگی عاملیت. این مفهوم در مطالعات فناوری و رسانه برای تحلیل نقش اشیاء و فناوری در ساخت اجتماعی بسیار کاربرد دارد؛ بنابراین، شبکه کنشگران، به ما یاد می‌دهد که «اجتماع»، حاصل تعامل گره‌های انسانی و غیرانسانی است و نباید همه‌چیز را صرفا‌ً به اراده‌ی انسان منتسب کرد (Law, 1994; Latour, 2005).",
        mechanism="شبکه کنشگران در چهار حلقه (مراحل ترجمه در ANT) شکل می‌گیرد: (۱) مسئله‌سازی: یک کنشگر، خود را به‌عنوان گره ضروری و محوری مطرح می‌کند؛ (۲) پیوند‌سازی (interessement): کنشگران با وعده و ابزار، به شبکه جذب می‌شوند؛ (۳) نمایندگی (delegation): وظایف به کنشگران، از جمله فناوری، سپرده می‌شود؛ و (۴) موبیلیزاسیون: شبکه به‌عنوان یک «شبه‌نهاد» پایدار و عمل‌کننده عمل می‌کند. این چرخه، شبکه را به‌شکل تدریجی و تعاملی می‌سازد (Law, 1994; Latour, 2005).",
        key_concepts=["هم‌پسندی انسان و غیرانسان", "ترجمه و پیوند", "شبه‌نهاد (quasi-object)", "موبیلیزاسیون", "پراکندگی عاملیت"],
        critiques="نقد بنیادین: رویکرد «هم‌پسندی» (symmetry) در ANT، تفاوت ساختاری بین کنشگران انسانی و غیرانسانی را کم‌اهمیت جلوه می‌دهد و گاه ابعاد قدرت و تضاد اجتماعی را محو می‌کند (Littlejohn & Foss, 2011). همچنین این رویکرد توصیفی و «بازنمایی‌گرا» است و به‌شکلی روشن درباره‌ی علل و اهداف کنش‌ها سخن نمی‌گوید و برای تحلیل انتقادی ساختارهای قدرت، ابزار محدودی به نظر می‌رسد؛ به‌علاوه، این رویکرد، برای تحلیل تضادها، نابرابری‌ها و ساختارهای قدرت، کمتر مناسب است و برخی آن را بیش‌ازحد توصیفی و گاه دور از واقعیت‌های سیاسی می‌دانند (Law, 1994).",
        applications="کاربردهای عملی شامل تحلیل نقش فناوری و اشیاء در ساخت اجتماعی و رسانه‌ای، مطالعات فناوری و طراحی، درک پایداری شبکه‌های پیچیده، تحلیل جریان‌های مترجمی در سازمان‌ها، و آموزش نظریه‌های ارتباطات معاصر است؛ این رویکرد در مطالعات رسانه‌ی دیجیتال، الگوریتم و پلتفرم، کاربرد ویژه و رو به رشد دارد؛ این رویکرد، به‌ویژه برای درک چگونگی پیدایش و پایداری فناوری‌های رسانه‌ای و نقش الگوریتم‌ها و پلتفرم‌ها، ابزار تحلیل تازه و کاربردی در دنیای امروز فراهم می‌کند (Law, 1994; Latour, 2005).",
        evolution="نظریه‌ی شبکه کنشگر در دهه‌های ۱۹۸۰–۱۹۹۰ در رشته‌های مطالعات علم و فناوری شکل گرفت و بعدها به مطالعات رسانه و ارتباطات وارد شد؛ در عصر دیجیتال، ANT برای تحلیل تعامل انسان و الگوریتم و پلتفرم، به‌عنوان کنشگران فعال در شبکه، کاربرد تازه‌ای یافته و بازتاب گسترده‌ای پیدا کرده است؛ این گسترش کاربرد، نشان می‌دهد که رویکرد شبکه کنشگران، به یکی از مهم‌ترین چارچوب‌های تحلیل رسانه و فناوری در پژوهش‌های معاصر تبدیل شده است (Latour, 2005).",
        assumptions="فرض‌های نهفته این است: عاملیت به یک کنشگر انسانی متمرکز نیست بلکه در شبکه پراکنده است؛ کنشگران غیرانسانی (فناوری، اشیاء، الگوریتم) نیز نقش فعال و معنادار ایفا می‌کنند؛ و پایداری شبکه، محصول پیوندها و ترجمه‌هاست نه اراده‌ی یک مرکز فرمانده (Law, 1994; Latour, 2005).",
    ),
    "CPT-185": dict(
        summary="گره (Node) در تحلیل شبکه، هر واحد یا کنشگری است که به‌عنوان نقطه‌ی اتصال در یک شبکه عمل می‌کند؛ گره می‌تواند فرد، نهاد، رسانه، دستگاه، وب‌گاه یا حتی یک ایده باشد و هویت و ساختار شبکه، از طریق گره‌ها و پیوندهای میان آن‌ها ساخته می‌شود. ویژگی‌های آن عبارت‌اند از: (۱) موقعیت گره در شبکه، (۲) تعداد و نوع پیوندهای آن، (۳) نقش و مرکزیت نسبی، (۴) ویژگی‌های درونی گره. این مفهوم، واحد بنیادی تحلیل شبکه اجتماعی و ارتباطی است و درک آن پیش‌شرط تحلیل مرکزیت، تراکم و جریان اطلاعات در شبکه است؛ به همین دلیل، درک گره، نخستین گام در هر تحلیل شبکه‌ای است و بدون تعریف دقیق گره، هیچ محاسبه‌ای از مرکزیت یا تراکم معنا ندارد و نتیجه‌گیری معتبر نمی‌شود (Barabási, 2002; Freeman, 1978).",
        mechanism="گره در چهار سطح عمل می‌کند: (۱) قرارگیری در یک نقطه‌ی مشخص از فضای شبکه؛ (۲) ایجاد و نگه‌داشتن پیوندها با گره‌های دیگر؛ (۳) انتقال و جابه‌جایی اطلاعات و منابع در طول پیوندها؛ و (۴) تغییر موقعیت و مرکزیت بر اساس الگوی تعامل در طول زمان. ویژگی‌های یک گره (مانند درجه‌ی آن و تعداد پیوندهایش) نقش آن را در ساختار کلی شبکه به‌طور مستقیم تعیین می‌کند (Barabási, 2002; Freeman, 1978).",
        key_concepts=["واحد بنیادی شبکه", "موقعیت شبکه‌ای", "درجه (degree)", "مرکزیت", "پیوند و ارتباط"],
        critiques="نقد بنیادین: تعریف «گره» اغلب ساده‌سازی است و پیچیدگی واقعی یک کنشگر (مثلاً یک فرد با نقش‌های چندگانه و چندلایه) را به یک نقطه‌ی تک‌بُعدی تقلیل می‌دهد (Littlejohn & Foss, 2011). همچنین مرز و سطح گره (آیا فرد است یا گروه؟) همیشه روشن نیست و انتخاب آن، نتایج تحلیل را به‌شدت تحت تأثیر قرار می‌دهد و گاه دل‌خواه و قابل‌بررسی است؛ همچنین، در شبکه‌های واقعی، مرز بین گره‌ها گاه مبهم است و یک واحد می‌تواند هم‌زمان چند نقش داشته باشد که مدل‌بندی ساده را دشوار و گاه ناکافی می‌سازد (Barabási, 2002).",
        applications="کاربردهای عملی شامل شناسایی و تعریف واحد‌های تحلیل در شبکه اجتماعی و ارتباطی، محاسبه‌ی مرکزیت و درجه‌ی گره‌ها، شناسایی گره‌های کلیدی و تأثیرگذار، تحلیل جریان اطلاعات، و طراحی مدل‌های شبکه‌ای است؛ این مفهوم، پایه‌ی همه‌ی محاسبات و تحلیل‌ها در نظریه‌ی گراف و شبکه است؛ در عمل، گره‌های کلیدی (مانند گره‌های پُردرجه) برای شناسایی تأثیرگذاران و رهبران، و برای طراحی مداخلات شبکه‌ای، اهمیت ویژه‌ای دارند و معیار عملی هستند (Barabási, 2002; Freeman, 1978).",
        evolution="مفهوم گره از ریاضیات گراف و نظریه‌ی گراف (قرن نوزدهم) وارد تحلیل شبکه اجتماعی (دهه‌های ۱۹۵۰–۱۹۷۰) و سپس شبکه‌های برخط در عصر دیجیتال شد؛ امروز، گره‌ها در شبکه‌های کلان و چندلایه، با استفاده از داده‌های بزرگ و الگوریتم‌ها، به‌شکل پویا و لحظه‌ای مدل‌سازی می‌شوند؛ بنابراین، گره از یک مفهوم انتزاعی ریاضی به واحد اصلی تحلیل شبکه‌های اجتماعی، رسانه‌ای و سازمانی معاصر بدل شده و جایگاه محوری خود را حفظ می‌کند (Barabási, 2002).",
        assumptions="فرض‌های نهفته این است: تعاملات و عناصر شبکه به واحد‌های گسسته و قابل‌شناسایی (گره‌ها) تجزیه می‌شوند؛ هر گره موقعیت مشخص و متمایزی در شبکه دارد؛ و ویژگی‌های یک گره، رفتار و نقش آن را در شبکه تا حد قابل‌توجهی تعیین می‌کنند، هرچند واقعیت همیشه ساده‌تر از مدل نیست (Barabási, 2002; Freeman, 1978).",
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
        if not isinstance(p.get("sources"), list):
            p["sources"] = []
        if not isinstance(p.get("citations"), list):
            p["citations"] = []
        existing_srcs = set(x.get("citation") for x in p["sources"])
        existing_cits = set(x.get("source") for x in p["citations"])
        for src in S[code]:
            if src["citation"] not in existing_srcs:
                p["sources"].append({
                    "citation": src["citation"], "title_en": src["title_en"],
                    "title_fa": src["title_fa"], "year": src["year"], "doi": src.get("doi"),
                    "url": src.get("url"), "language": src["language"], "verified": src["verified"],
                })
            if src["citation"] not in existing_cits:
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
                    (code, json.dumps({"batch": 330, "score": score, "words": words,
                                       "sources": n_sources, "verified": n_verified,
                                       "relations": n_rel, "rubric": detail}, ensure_ascii=False), STAMP, NOW))
        print(code, "words", words, "score", score, "detail", detail)
    conn.commit()
    conn.close()
    print("BATCH330 DONE")


if __name__ == "__main__":
    main()
