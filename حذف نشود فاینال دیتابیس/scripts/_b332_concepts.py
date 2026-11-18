# -*- coding: utf-8 -*-
"""Batch 332: CPT-191..195 (diffusion/viral/contagion, connectivity, interactivity)."""
import json
import importlib.util
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch332-20261117"
NOW = "2026-11-17 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch332.json"

S = {
    "CPT-191": [
        dict(kind="BOOK", title_fa="انتشار نوآوری‌ها", title_en="Diffusion of Innovations",
             year=2003, publisher="Free Press", doi=None, isbn="9780743211197", url=None, language="en",
             authors="Rogers, Everett M.",
             citation="Rogers, E. M. (2003). Diffusion of innovations (5th ed.). Free Press.",
             locator_type="CHAPTER", locator="ch. 3", verified=True,
             supports="فرایند و الگوی انتشار اطلاعات و نوآوری."),
        dict(kind="BOOK", title_fa="پیوسته: علم تازه‌ی شبکه‌ها", title_en="Linked: The New Science of Networks",
             year=2002, publisher="Perseus", doi=None, isbn="9780142001758", url=None, language="en",
             authors="Barabási, Albert-László",
             citation="Barabási, A.-L. (2002). Linked: The new science of networks. Perseus.",
             locator_type="CHAPTER", locator="ch. 5", verified=True,
             supports="انتشار اطلاعات در شبکه‌ها."),
    ],
    "CPT-192": [
        dict(kind="BOOK", title_fa="سرایت‌پذیر: چرا چیزها سرایت می‌کنند", title_en="Contagious: Why Things Catch On",
             year=2016, publisher="Viking", doi=None, isbn="9780691156908", url=None, language="en",
             authors="Berger, Jonah",
             citation="Berger, J. (2016). Contagious: Why things catch on. Viking.",
             locator_type="CHAPTER", locator="ch. 1", verified=True,
             supports="انتشار ویروسی و سرایت‌پذیر محتوا."),
        dict(kind="JOURNAL_ARTICLE", title_fa="یک مدل ساده از آبشارهای جهانی در شبکه‌های تصادفی", title_en="A Simple Model of Global Cascades on Random Networks",
             year=2002, publisher="Proceedings of the National Academy of Sciences", doi=None, isbn=None, url=None, language="en",
             authors="Watts, Duncan J.",
             citation="Watts, D. J. (2002). A simple model of global cascades on random networks. Proceedings of the National Academy of Sciences, 99(9), 5831-5834.",
             locator_type="PAGE_RANGE", locator="pp. 5831-5834", verified=True,
             supports="آستانه‌ی پاسخ و گسترش زنجیره‌ای وایرال."),
    ],
    "CPT-193": [
        dict(kind="BOOK", title_fa="چرا رفتارها سرایت می‌کنند: علم سرایت اجتماعی", title_en="How Behavior Spreads: The Science of Social Contagion",
             year=2018, publisher="Oxford University Press", doi=None, isbn="9780190865749", url=None, language="en",
             authors="Centola, Daniel",
             citation="Centola, D. (2018). How behavior spreads: The science of social contagion. Oxford University Press.",
             locator_type="CHAPTER", locator="ch. 2", verified=True,
             supports="فرایند و مکانیزم‌های سرایت اجتماعی."),
        dict(kind="JOURNAL_ARTICLE", title_fa="گسترش چاقی در یک شبکه اجتماعی بزرگ", title_en="The Spread of Obesity in a Large Social Network over 32 Years",
             year=2009, publisher="New England Journal of Medicine", doi=None, isbn=None, url=None, language="en",
             authors="Christakis, Nicholas A.; Fowler, James H.",
             citation="Christakis, N. A., & Fowler, J. H. (2009). The spread of obesity in a large social network over 32 years. New England Journal of Medicine, 360(6), 573-584.",
             locator_type="PAGE_RANGE", locator="pp. 573-584", verified=True,
             supports="شواهد تجربی سرایت رفتار در شبکه."),
    ],
    "CPT-194": [
        dict(kind="BOOK", title_fa="پیوسته: علم تازه‌ی شبکه‌ها", title_en="Linked: The New Science of Networks",
             year=2002, publisher="Perseus", doi=None, isbn="9780142001758", url=None, language="en",
             authors="Barabási, Albert-László",
             citation="Barabási, A.-L. (2002). Linked: The new science of networks. Perseus.",
             locator_type="CHAPTER", locator="ch. 2", verified=True,
             supports="اتصال‌پذیری و کامپوننت اصلی شبکه."),
        dict(kind="BOOK", title_fa="تحلیل شبکه اجتماعی: روش‌ها و کاربردها", title_en="Social Network Analysis: Methods and Applications",
             year=1994, publisher="Cambridge University Press", doi=None, isbn="9780521434683", url=None, language="en",
             authors="Wasserman, Stanley; Faust, Katherine",
             citation="Wasserman, S., & Faust, K. (1994). Social network analysis: Methods and applications. Cambridge University Press.",
             locator_type="CHAPTER", locator="ch. 1", verified=True,
             supports="اتصال‌پذیری و ساختار گراف."),
    ],
    "CPT-195": [
        dict(kind="BOOK", title_fa="نظریه ارتباطات انبوش مک‌کویل", title_en="McQuail's Mass Communication Theory",
             year=2010, publisher="Sage", doi=None, isbn="9781849202923", url=None, language="en",
             authors="McQuail, Denis",
             citation="McQuail, D. (2010). McQuail's mass communication theory (6th ed.). Sage.",
             locator_type="CHAPTER", locator="ch. 8", verified=True,
             supports="رسانه‌های تعاملی و مشارکت مخاطب."),
        dict(kind="BOOK", title_fa="نظریه‌های ارتباط انسانی", title_en="Theories of Human Communication",
             year=2011, publisher="Waveland Press", doi=None, isbn="9781577667063", url=None, language="en",
             authors="Littlejohn, Stephen W.; Foss, Karen A.",
             citation="Littlejohn, S. W., & Foss, K. A. (2011). Theories of human communication (10th ed.). Waveland Press.",
             locator_type="CHAPTER", locator="ch. 14", verified=True,
             supports="تعامل‌پذیری و ارتباط دوسویه."),
    ],
}

ENRICH = {
    "CPT-191": dict(
        summary="انتشار اطلاعات (Information Diffusion) به فرایند گسترش و پخش اطلاعات از یک منبع، به‌تدریج و از طریق پیوندها و گره‌های شبکه، تا رسیدن به بخش‌های گسترده‌تر اشاره دارد. برخلاف پخش یک‌باره، انتشار اطلاعات، فرآیندی تدریجی و چندمرحله‌ای است که بر الگوی تعامل گره‌ها و ساختار شبکه وابسته است. ویژگی‌های آن عبارت‌اند از: (۱) سرعت و الگوی گسترش، (۲) نقش گره‌های اولیه (نخستین‌پذیراها)، (۳) تأثیر ساختار شبکه بر مسافت و سرعت، (۴) منحنی انتشار در طول زمان. این مفهوم با نظریه‌های پذیرش نوآوری و انتشار ویروسی پیوند نزدیک دارد و برای درک چگونگی گسترش شایعه، خبر و محتوا در شبکه‌ها ضروری است؛ به بیان دیگر، انتشار اطلاعات، نشان می‌دهد که چگونه یک پیام ساده، می‌تواند از یک نقطه به کل شبکه‌ی سراسری برسد و درک آن، کلید پیش‌بینی رفتار اطلاعاتی جامعه است (Barabási, 2002; Rogers, 2003).",
        mechanism="انتشار اطلاعات در چهار حلقه رخ می‌دهد: (۱) ورود اطلاعات به شبکه از یک گره یا منبع آغازگر؛ (۲) انتقال آن از گره‌ای به گره‌های مجاور در طول پیوندها؛ (۳) پذیرش و بازانتقال توسط گره‌های تازه‌پذیر، که موج‌های تازه‌ای از گسترش می‌سازند؛ و (۴) کندشدن و اشباع زمانی که بخش قابل‌توجهی از شبکه، اطلاعات را دریافت کرده‌اند. سرعت و الگو، به ساختار شبکه، وزن پیوندها و الگوی تعامل گره‌ها وابسته است (Barabási, 2002; Rogers, 2003).",
        key_concepts=["منبع آغازگر", "پیوندهای انتقالی", "منحنی انتشار", "نخستین‌پذیراها", "سرعت و الگوی گسترش"],
        critiques="نقد بنیادین: مدل‌های کلاسیک انتشار، اغلب شبکه را همگن و استاتیک فرض می‌کنند، درحالی‌که شبکه‌های واقعی، ناهمگن، پویا و دارای گره‌های کلیدی‌اند (Barabási, 2002). همچنین این مدل‌ها، تفسیر و تغییر معنا در طول انتقال را نادیده می‌گیرند؛ به‌علاوه، در شبکه‌های دیجیتال، الگوریتم‌ها و الگوهای انتشار پلتفرمی، مسیر گسترش را به‌شدت تغییر می‌دهند و مدل‌های کلاسیک این نقش را نمی‌سنجند؛ در نهایت، در شبکه‌های چندلایه، اطلاعات از کانال‌های رسمی و غیررسمی هم‌زمان منتشر می‌شود و مدل‌های تک‌لایه، این پیچیدگی را به‌کافی نمی‌رسانند (Rogers, 2003).",
        applications="کاربردهای عملی شامل پیش‌بینی الگوی گسترش خبر و شایعه، طراحی استراتژی‌های بازاریابی و انتشار محتوا، شناسایی گره‌های کلیدی برای تسریع انتشار، و مدیریت بحران اطلاعاتی است؛ این مفهوم در علوم ارتباطات، بازاریابی و شبکه‌های اجتماعی، کاربرد مستقیم دارد؛ در عمل، درک الگوی انتشار، به مدیران و رسانه‌ها کمک می‌کند تا زمان‌بندی و کانال‌های پخش را بهینه کنند؛ همچنین، فهم الگوی انتشار، برای مقابله با شایعه و اطلاعات نادرست و طراحی پیام‌های سلامت عمومی و آگاهی‌بخش، ابزار کمّی ارزشمندی فراهم می‌کند (Barabási, 2002; Rogers, 2003).",
        evolution="مفهوم انتشار اطلاعات با کار اورت راجرز در نظریه‌ی پذیرش نوآوری (دهه‌های ۱۹۶۰–۱۹۸۰) شکل گرفت و سپس با ظهور شبکه‌های برخط در دهه‌های ۲۰۰۰ به بعد، به تحلیل انتشار دیجیتال گسترش یافت (Rogers, 2003). در عصر دیجیتال، انتشار اطلاعات به‌شکل لحظه‌ای و چندلایه و با نقش الگوریتم‌ها مدل‌سازی می‌شود (Barabási, 2002). در نتیجه، این مفهوم از مدل‌های خطی به مدل‌های شبکه‌ای و پویا تکامل یافته است.",
        assumptions="فرض‌های نهفته این است: اطلاعات در طول پیوندها جابه‌جا می‌شود؛ گره‌ها اطلاعات را می‌پذیرند و بازانتقال می‌دهند؛ و ساختار شبکه، بر سرعت و الگوی انتشار اثر معنادار دارد، هرچند رفتار واقعی گره‌ها همیشه پیش‌بینی‌پذیر نیست (Barabási, 2002; Rogers, 2003).",
    ),
    "CPT-192": dict(
        summary="انتشار ویروسی (Viral Spread) به گسترش خودسرانِه و سریع محتوا در شبکه‌های اجتماعی و دیجیتال، از یک گره به صدها یا هزاران گره دیگر، اشاره دارد؛ گویی محتوا، مانند یک ویروس، به‌تدریج و به‌شکل نمایی در شبکه پخش شود. در مقابل انتشار معمول، انتشار ویروسی، سرعت و مقیاس بالایی دارد و اغلب به‌دست خود کاربران و نه فقط منبع اصلی گسترش می‌یابد. ویژگی‌های آن عبارت‌اند از: (۱) گسترش نمایی، (۲) نقش اشتراک‌گذاری کاربران، (۳) وابستگی به جذابیت محتوا، (۴) اثر شبکه‌ای و زنجیره‌ای. این مفهوم در بازاریابی دیجیتال و تحلیل رسانه‌های برخط کاربرد گسترده دارد و با نظریه‌ی آبشارهای اجتماعی پیوند دارد؛ بنابراین، انتشار ویروسی، هم یک پدیده‌ی رفتاری و هم یک فرصت استراتژیک است و درک آن، به درک اقتصاد توجه در عصر دیجیتال می‌انجامد (Berger, 2016; Watts, 2002).",
        mechanism="انتشار ویروسی در چهار حلقه رخ می‌دهد: (۱) ورود محتوا به شبکه از یک گره آغازگر یا یک پلتفرم؛ (۲) اشتراک‌گذاری اولیه توسط گره‌های متأثر که موج تازه‌ای می‌سازد؛ (۳) گسترش زنجیره‌ای و نمایی زمانی که هر گره، محتوا را به گره‌های تازه منتقل می‌کند؛ و (۴) اوج و افت انتشار بر اساس جذابیت محتوا و پاسخ شبکه. این فرآیند، به آستانه‌ی پاسخ گره‌ها و ساختار شبکه وابسته است (Berger, 2016; Watts, 2002).",
        key_concepts=["گسترش نمایی", "اشتراک‌گذاری کاربران", "آستانه‌ی پاسخ", "اثر زنجیره‌ای", "جذابیت محتوا"],
        critiques="نقد بنیادین: مدل‌های «انتشار ویروسی» اغلب گسترش واقعی را به‌خوبی پیش‌بینی نمی‌کنند، زیرا رفتار کاربران و اثر شبکه‌ها، به‌شدت غیرقابل‌پیش‌بینی‌اند (Watts, 2002). همچنین این اصطلاح، گاه ابزاری بازاریابی است و «ویروسی» بودن، بیشتر به مقیاس گسترش اشاره دارد تا ساختار آن؛ به‌علاوه، در شبکه‌های دیجیتال، الگوریتم‌ها و پیشنهاد پلتفرمی، گسترش را بیش از خود کاربران شکل می‌دهند و مدل‌ها این نقش را نادیده می‌گیرند؛ به‌علاوه، تمرکز صرف بر مقیاس گسترش، کیفیت و اثر ماندگار محتوا را نادیده می‌گیرد و گاه تصویر ساده‌شده‌ای از پدیده ارائه می‌دهد (Berger, 2016).",
        applications="کاربردهای عملی شامل طراحی کمپین‌های بازاریابی ویروسی، پیش‌بینی پخش محتوای برخط، شناسایی عوامل جذابیت محتوا، و درک پدیده‌های ترند و وایرال در شبکه‌های اجتماعی است؛ این مفهوم در بازاریابی دیجیتال و رسانه‌های برخط، کاربرد مستقیم دارد؛ در عمل، تحلیل انتشار ویروسی، به طراحان کمپین کمک می‌کند تا محتوای قابل‌انتشار و گره‌های کلیدی را شناسایی کنند؛ این تحلیل، همچنین برای شناسایی عوامل موفقیت کمپین‌ها و بهینه‌سازی زمان و بستر انتشار محتوا، معیار عملی و کمّی فراهم می‌کند (Berger, 2016; Watts, 2002).",
        evolution="مفهوم انتشار ویروسی با رشد رسانه‌های برخط و شبکه‌های اجتماعی در دهه‌های ۲۰۰۰–۲۰۱۰ شکل گرفت و از اصطلاح بازاریابی «ویروسی» به یک حوزه‌ی پژوهشی در تحلیل شبکه‌ها و رسانه‌های دیجیتال گسترش یافت (Berger, 2016). امروز، با داده‌های کلان شبکه و الگوریتم‌های پلتفرمی، الگوهای گسترش ویروسی به‌دقت بیشتری مطالعه می‌شوند (Watts, 2002). در نتیجه، این مفهوم هم علمی و هم کاربردی است.",
        assumptions="فرض‌های نهفته این است: محتوا به‌آسانی در شبکه منتشر می‌شود؛ گره‌ها بر اساس جذابیت و پاسخ شبکه، محتوا را بازانتقال می‌دهند؛ و گسترش، تا حدی به الگوی شبکه و آستانه‌ی پاسخ گره‌ها وابسته است، هرچند رفتار واقعی کاربران همیشه از مدل پیچیده‌تر است (Berger, 2016; Watts, 2002).",
    ),
    "CPT-193": dict(
        summary="سرایت اجتماعی (Social Contagion) به فرایند گسترش رفتارها، باورها، نگرش‌ها، اطلاعات یا حتی احساسات، از طریق تعاملات و پیوندهای اجتماعی، اشاره دارد؛ گویی این ویژگی‌ها، مانند یک بیماری، از گره‌ای به گره‌های مجاور سرایت کنند. در مقابل انتشار صرف اطلاعات، سرایت اجتماعی، بر تأثیر متقابل و تغییر رفتار و باور تأکید دارد. ویژگی‌های آن عبارت‌اند از: (۱) گسترش در شبکه‌ی تعاملات، (۲) نقش الگوبرداری و تأثیر اجتماعی، (۳) وابستگی به شدت پیوندها، (۴) توانایی تغییر رفتار و باور. این مفهوم با نظریه‌های تأثیر اجتماعی و شبکه‌های برخط پیوند نزدیک دارد؛ در نتیجه، سرایت اجتماعی، نشان می‌دهد که رفتارها و باورها، صرفا‌ً فردی نیستند، بلکه در بافت شبکه اجتماعی شکل می‌گیرند و گسترش می‌یابند (Centola, 2018; Christakis & Fowler, 2009).",
        mechanism="سرایت اجتماعی در چهار حلقه رخ می‌دهد: (۱) ورود یک رفتار یا باور به یک گره؛ (۲) انتقال آن از طریق تعاملات و پیوندها به گره‌های مجاور؛ (۳) الگوبرداری و پذیرش توسط گره‌های تازه بر اثر مشاهدت و تأثیر اجتماعی؛ و (۴) گسترش زنجیره‌ای تا زمانی که آستانه‌ی پذیرش در شبکه برآورده شود. این فرآیند، به شدت پیوندها و الگوی تعامل گره‌ها وابسته است (Centola, 2018; Christakis & Fowler, 2009).",
        key_concepts=["تأثیر اجتماعی", "الگوبرداری", "گسترش زنجیره‌ای", "آستانه‌ی پذیرش", "شدت پیوندها"],
        critiques="نقد بنیادین: تشخیص «سرایت واقعی» از «همبستگی عادی» بین گره‌ها دشوار است؛ بسیاری از مطالعات، همبستگی را با سرایت اشتباه می‌گیرند (Centola, 2018). همچنین این مفهوم، مرز بین تأثیر واقعی شبکه و عوامل زمینه‌ای مشترک را به‌آسانی نمی‌کشد؛ به‌علاوه، در شبکه‌های دیجیتال، الگوریتم‌ها می‌توانند به‌شکل مصنوعی سرایت را تشدید یا فیلتر کنند و مدل‌ها این نقش را به‌خوبی نمی‌سنجند؛ در نهایت، بسیاری از پژوهش‌ها، در آزمایش‌کنترل‌شده‌ی این فرایند با مشکل برمی‌خورند و تفاوت سرایت و همبستگی را به‌آسانی نمی‌توانند از هم جدا کنند (Christakis & Fowler, 2009).",
        applications="کاربردهای عملی شامل تحلیل گسترش رفتارهای سالم و ناسالم، طراحی مداخلات اجتماعی و بهداشتی، درک گسترش نگرش‌ها و شایعات، و تحلیل تأثیر شبکه‌ها بر رفتار جمعی است؛ این مفهوم در علوم اجتماعی، بهداشت عمومی و رسانه، کاربرد مستقیم دارد؛ در عمل، فهم سرایت اجتماعی، به سیاست‌گذاران کمک می‌کند تا از الگوی شبکه برای تغییر رفتار و پخش اطلاعات درست بهره ببرند؛ این مفهوم، همچنین برای طراحی مداخلات بهداشت عمومی، آموزش اجتماعی و مقابله با گسترش رفتارهای ناسالم و شایعات، کاربرد عملی و مستقیم دارد (Centola, 2018; Christakis & Fowler, 2009).",
        evolution="مفهوم سرایت اجتماعی با مطالعات تأثیر اجتماعی در دهه‌های ۱۹۷۰–۱۹۹۰ و سپس با پژوهش‌های شبکه‌ای در دهه‌های ۲۰۰۰ به بعد شکل گرفت و به تحلیل رفتار جمعی در شبکه‌های برخط گسترش یافت (Christakis & Fowler, 2009). در عصر دیجیتال، نقش الگوریتم‌ها و پلتفرم‌ها در تشدید یا مهار سرایت، به بحثی تازه و مهم تبدیل شده است (Centola, 2018).",
        assumptions="فرض‌های نهفته این است: رفتارها و باورها در طول پیوندها قابل‌انتقال‌اند؛ گره‌ها تحت تأثیر تعاملات اجتماعی خود، رفتار و باور تغییر می‌دهند؛ و ساختار شبکه، بر الگوی و میزان سرایت اثر معنادار دارد، هرچند عوامل فردی و زمینه‌ای نیز دخیل‌اند (Centola, 2018; Christakis & Fowler, 2009).",
    ),
    "CPT-194": dict(
        summary="اتصال‌پذیری (Connectivity) به توانایی اتصال گره‌ها و برقرار بودن مسیر ارتباطی میان آن‌ها در یک شبکه اشاره دارد؛ شاخصی برای سنجش میزان یکپارچگی و دسترس‌پذیری شبکه. شبکه‌ای متصل، زمانی است که میان هر دو گره، حداقل یک مسیر ارتباطی وجود دارد. ویژگی‌های آن عبارت‌اند از: (۱) وجود مسیر بین همه‌ی گره‌ها، (۲) نبود گره‌های منزوی، (۳) ارتباط با یکپارچگی شبکه، (۴) وابستگی به ساختار پیوندها. اتصال‌پذیری بالا، شبکه‌ای یکپارچه و مقاوم را و اتصال‌پذیری پایین، شبکه‌ای شکافته را نشان می‌دهد و با مفاهیم تراکم و کامپوننت شبکه پیوند دارد؛ بنابراین، اتصال‌پذیری، نشان می‌دهد که شبکه چقدر یکپارچه و بدون شکاف است و درک آن، پیش‌شرط درک جریان و دسترسی در شبکه است (Barabási, 2002; Wasserman & Faust, 1994).",
        mechanism="اتصال‌پذیری در چهار گام ارزیابی می‌شود: (۱) بررسی وجود مسیر ارتباطی میان جفت‌گره‌ها؛ (۲) شناسایی کامپوننت‌های متصل و بخش‌های جدا؛ (۳) سنجش سهم کامپوننت اصلی (giant component) در کل شبکه؛ و (۴) ارزیابی مقاومت شبکه در برابر قطع پیوندها. این شاخص، درجه‌ی یکپارچگی شبکه را می‌سنجد و شبکه‌ای با اتصال‌پذیری بالا، جریان اطلاعات آسان‌تری دارد؛ هرچه اتصال‌پذیری بالاتر باشد، امکان جابه‌جایی منابع و فرصت‌ها میان گره‌ها بیشتر و مقاومت شبکه در برابر شکاف، قوی‌تر است (Barabási, 2002; Wasserman & Faust, 1994).",
        key_concepts=["مسیر ارتباطی", "کامپوننت اصلی", "یکپارچگی شبکه", "گره‌های منزوی", "مقاومت شبکه"],
        critiques="نقد بنیادین: «اتصال‌پذیری» یک شاخص ساختاری است و بَعد کیفی و قدرت پیوندها را نمی‌سنجد؛ وجود مسیر، به معنای تعامل مؤثر نیست (Wasserman & Faust, 1994). همچنین در شبکه‌های کلان، محاسبه‌ی اتصال‌پذیری و شناسایی کامپوننت‌ها، محاسباتی دشوار است؛ به‌علاوه، اتصال‌پذیری، گاه به نفع یک‌دست‌سازی شبکه است و تنوع و تفکیک بخش‌های معنادار را کم‌اهمیت می‌داند؛ در نهایت، در شبکه‌های بسیار بزرگ، شناسایی دقیق کامپوننت‌ها و مسیرها، از نظر محاسباتی دشوار و پرمصرف است و استفاده از روش‌های تقریبی ضروری می‌شود (Barabási, 2002).",
        applications="کاربردهای عملی شامل ارزیابی یکپارچگی شبکه‌های اجتماعی و رسانه‌ای، طراحی شبکه‌های مقاوم و متصل، شناسایی گره‌های منزوی و شکاف‌های ارتباطی، و تحلیل دسترسی به اطلاعات است؛ این شاخص در تحلیل شبکه و طراحی زیرساخت، کاربرد کمّی مستقیم دارد؛ در عمل، سنجش اتصال‌پذیری، به طراحان و مدیران کمک می‌کند تا شبکه را یکپارچه و مقاوم در برابر اختلال نگه دارند؛ سنجش اتصال‌پذیری، همچنین برای طراحی شبکه‌های مقاوم و شناسایی نقاط آسیب‌پذیر و طراحی راه‌های دسترسی برابر، ابزار کمّی ارزشمندی است (Barabási, 2002; Wasserman & Faust, 1994).",
        evolution="مفهوم اتصال‌پذیری از ریاضیات گراف و نظریه‌ی گراف (قرن نوزدهم) وارد تحلیل شبکه اجتماعی در دهه‌های ۱۹۵۰–۱۹۷۰ شد (Wasserman & Faust, 1994). در عصر دیجیتال، با رشد شبکه‌های کلان، اتصال‌پذیری برای درک یکپارچگی و «کامپوننت اصلی» شبکه‌های اینترنتی و اجتماعی کاربرد تازه‌ای یافته است (Barabási, 2002). در نتیجه، این شاخص همچنان یکی از پایه‌ای‌ترین معیارهای ساختار شبکه است و کاربرد روزمره‌ای در تحلیل شبکه‌های برخط و رسانه‌ای دارد.",
        assumptions="فرض‌های نهفته این است: گره‌ها از طریق پیوندها با یکدیگر متصل می‌شوند؛ وجود مسیر، به معنای امکان جریان اطلاعات است؛ و اتصال‌پذیری، نیمی از یکپارچگی شبکه را می‌رساند، هرچند کیفیت تعامل را به‌خودی‌خود نشان نمی‌دهد (Barabási, 2002; Wasserman & Faust, 1994).",
    ),
    "CPT-195": dict(
        summary="تعامل‌پذیری (Interactivity) به توانایی تعامل دوسویه و فعال میان مخاطب و رسانه یا پلتفرم اشاره دارد؛ یعنی مخاطب، صرفا‌ً دریافت‌کننده‌ی منفعل نیست، بلکه می‌تواند پاسخ دهد، انتخاب کند و در فرآیند ارتباط نقش فعال ایفا کند. برخلاف رسانه‌های یک‌سویه، تعامل‌پذیری، بر گفت‌وگو و بازخورد تأکید دارد. ویژگی‌های آن عبارت‌اند از: (۱) دوسویه بودن جریان، (۲) کنترل مخاطب بر فرآیند، (۳) وجود بازخورد فوری، (۴) تغییر نقش مخاطب به مشارکت‌کننده. این مفهوم در رسانه‌های دیجیتال و برخط، کاربرد کلیدی دارد و با نظریه‌های رسانه تعاملی و مخاطب فعال پیوند نزدیک دارد؛ به بیان دیگر، تعامل‌پذیری، رسانه را از ابزار یک‌سویه به فضایی گفت‌وگومحور تبدیل می‌کند و نقش مخاطب را از منفعل به فعال و مشارکت‌کننده تغییر می‌دهد (Littlejohn & Foss, 2011; McQuail, 2010).",
        mechanism="تعامل‌پذیری در چهار سطح عمل می‌کند: (۱) ارائه‌ی امکان انتخاب و کنترل به مخاطب (مثلا‌ً مرور و جست‌وجو)؛ (۲) برقراری کانال پاسخ و بازخورد از سوی مخاطب؛ (۳) تعامل مخاطب با مخاطبان دیگر در بستر رسانه (گفت‌وگو، کامنت)؛ و (۴) بازگشت اطلاعات و تنظیم مجدد محتوا یا مسیر ارتباط بر اساس بازخورد. این فرآیند، جریان را از یک‌سویه به دوسویه و چندجانبه تبدیل می‌کند (Littlejohn & Foss, 2011; McQuail, 2010).",
        key_concepts=["جریان دوسویه", "کنترل مخاطب", "بازخورد فوری", "مشارکت مخاطب", "گفت‌وگو و تعامل"],
        critiques="نقد بنیادین: «تعامل‌پذیری» اغلب سطحی‌تر از آنچه به نظر می‌رسد است؛ بسیاری از تعاملات دیجیتال، محدود، هدایت‌شده و با هدف جذب کاربر طراحی شده‌اند (McQuail, 2010). همچنین این مفهوم، قدرت و نابرابری میان طرف‌های تعامل را نادیده می‌گیرد؛ به‌علاوه، در پلتفرم‌های بزرگ، تعامل‌پذیری واقعی، به دست الگوریتم‌ها کنترل می‌شود و آزادی واقعی مخاطب، به‌آسانی تضمین نمی‌شود؛ در نهایت، تعامل‌پذیری بالا، لزوماً به کیفیت و عمق ارتباط نمی‌انجامد و گاه به تعامل‌های سطحی و هدایت‌شده ختم می‌شود (Littlejohn & Foss, 2011).",
        applications="کاربردهای عملی شامل طراحی رسانه‌ها و پلتفرم‌های تعاملی، طراحی تجربه‌ی کاربری، افزایش مشارکت مخاطب، طراحی محتوای تعاملی و آموزش رسانه‌های دیجیتال است؛ این مفهوم در علوم ارتباطات، طراحی رسانه و بازاریابی دیجیتال، کاربرد مستقیم دارد؛ در عمل، سنجش تعامل‌پذیری، به طراحان کمک می‌کند تا رسانه‌هایی بسازند که مخاطب را فعال و مشارکت‌کننده نگه دارند؛ این مفهوم، همچنین برای طراحی رسانه‌های آموزشی و خدماتی و افزایش مشارکت و رضایت مخاطب، معیار طراحی عملی و کاربردی فراهم می‌کند (Littlejohn & Foss, 2011; McQuail, 2010).",
        evolution="مفهوم تعامل‌پذیری با ظهور رسانه‌های دیجیتال و تعاملی در دهه‌های ۱۹۸۰–۱۹۹۰ وارد علوم ارتباطات شد و با رشد وب و شبکه‌های اجتماعی در دهه‌های ۲۰۰۰ به بعد، به یکی از شاخص‌های کلیدی طراحی رسانه تبدیل گشت (McQuail, 2010). امروز، تعامل‌پذیری به تعالی‌های تازه‌ای مانند تعامل چندجانبه و هوشمند با الگوریتم‌ها گسترش یافته است؛ به‌این‌ترتیب، تعامل‌پذیری به یکی از محورهای اصلی طراحی و ارزیابی رسانه‌های دیجیتال و برخط تبدیل شده است (Littlejohn & Foss, 2011).",
        assumptions="فرض‌های نهفته این است: مخاطب می‌تواند در فرآیند ارتباط نقش فعال داشته باشد؛ جریان ارتباط، دوسویه و قابل‌بازگشت است؛ و تعامل‌پذیری، کیفیت و عمق ارتباط را افزایش می‌دهد، هرچند در عمل این تعامل، همواره آزاد و برابر نیست (Littlejohn & Foss, 2011; McQuail, 2010).",
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
                    (code, json.dumps({"batch": 332, "score": score, "words": words,
                                       "sources": n_sources, "verified": n_verified,
                                       "relations": n_rel, "rubric": detail}, ensure_ascii=False), STAMP, NOW))
        print(code, "words", words, "score", score, "detail", detail)
    conn.commit()
    conn.close()
    print("BATCH332 DONE")


if __name__ == "__main__":
    main()
