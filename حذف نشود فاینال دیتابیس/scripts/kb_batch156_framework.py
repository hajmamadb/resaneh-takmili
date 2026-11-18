# -*- coding: utf-8 -*-
"""Batch 156 (MODEL): MC-643 hybrid regime, MC-649 media environment, MC-650 news automation, MC-652 IS success."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch156-model-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch156_model.json"

S = {
    "MC-643": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Elections Without Democracy: The Rise of Competitive Authoritarianism",
             title_fa="انتخابات بدون دموکراسی: ظهور اقتدارگرایی رقابتی",
             authors="Levitsky, S.; Way, L. A.", year=2002,
             publisher="Journal of Democracy",
             doi="10.1353/jod.2002.0026",
             url="https://muse.jhu.edu/article/17196",
             language="en", isbn=None,
             citation="Levitsky, S., & Way, L. A. (2002). Elections without democracy: The rise of competitive authoritarianism. Journal of Democracy, 13(2), 51-65.",
             locator="13(2):51-65", locator_type="page_range",
             supports="hybrid regimes where elections are real but the playing field is uneven", verified=True),
        dict(kind="BOOK",
             title_en="Competitive Authoritarianism: Hybrid Regimes After the Cold War",
             title_fa="اقتدارگرایی رقابتی: رژیم‌های ترکیبی پس از جنگ سرد",
             authors="Levitsky, S.; Way, L. A.", year=2010,
             publisher="Cambridge University Press",
             doi=None,
             url="https://www.cambridge.org/core/books/competitive-authoritarianism/20A51BE2EBAB59B8AAEFD91B8FA3C9D6",
             language="en", isbn=None,
             citation="Levitsky, S., & Way, L. A. (2010). Competitive Authoritarianism: Hybrid Regimes After the Cold War. Cambridge: Cambridge University Press.",
             locator="2010 edition", locator_type="edition",
             supports="media harassment and uneven access as core features of hybrid regimes", verified=True),
    ],
    "MC-649": [
        dict(kind="BOOK",
             title_en="Understanding Media: The Extensions of Man",
             title_fa="فهم رسانه‌ها: گسترش‌های انسان",
             authors="McLuhan, M.", year=1964,
             publisher="McGraw-Hill (Routledge Classics edition, 2001)",
             doi=None,
             url="https://www.routledge.com/Understanding-Media/McLuhan/p/book/9780415253970",
             language="en", isbn=None,
             citation="McLuhan, M. (1964). Understanding Media: The Extensions of Man. New York: McGraw-Hill.",
             locator="Routledge Classics edition", locator_type="edition",
             supports="media as environments that reshape perception and social life", verified=True),
        dict(kind="BOOK",
             title_en="No Sense of Place: The Impact of Electronic Media on Social Behavior",
             title_fa="بی‌حسی مکان: اثر رسانه‌های الکترونیک بر رفتار اجتماعی",
             authors="Meyrowitz, J.", year=1985,
             publisher="Oxford University Press",
             doi=None,
             url="https://global.oup.com/academic/product/no-sense-of-place-9780195042313",
             language="en", isbn=None,
             citation="Meyrowitz, J. (1985). No Sense of Place: The Impact of Electronic Media on Social Behavior. New York: Oxford University Press.",
             locator="1985 edition", locator_type="edition",
             supports="media as information systems that reorganize social situations", verified=True),
    ],
    "MC-650": [
        dict(kind="REPORT",
             title_en="Guide to Automated Journalism",
             title_fa="راهنمای روزنامه‌نگاری خودکار",
             authors="Graefe, A.", year=2016,
             publisher="Tow Center for Digital Journalism, Columbia University",
             doi=None,
             url="https://towcenter.org/research/guide-to-automated-journalism/",
             language="en", isbn=None,
             citation="Graefe, A. (2016). Guide to Automated Journalism. New York: Tow Center for Digital Journalism.",
             locator="2016 report", locator_type="report",
             supports="natural language generation in newsrooms and its implications", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Automated News: Better than Expected?",
             title_fa="خبر خودکار: بهتر از انتظار؟",
             authors="Haim, M.; Graefe, A.", year=2017,
             publisher="Digital Journalism",
             doi="10.1080/21670811.2017.1345643",
             url="https://www.tandfonline.com/doi/abs/10.1080/21670811.2017.1345643",
             language="en", isbn=None,
             citation="Haim, M., & Graefe, A. (2017). Automated news: Better than expected? Digital Journalism, 5(8), 1044-1059.",
             locator="5(8):1044-1059", locator_type="page_range",
             supports="audience expectations and perceptions of automated versus human news", verified=True),
    ],
    "MC-652": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Information Systems Success: The Quest for the Dependent Variable",
             title_fa="موفقیت سیستم‌های اطلاعاتی: جست‌وجوی متغیر وابسته",
             authors="DeLone, W. H.; McLean, E. R.", year=1992,
             publisher="Information Systems Research",
             doi="10.1287/isre.3.1.60",
             url="https://pubsonline.informs.org/doi/10.1287/isre.3.1.60",
             language="en", isbn=None,
             citation="DeLone, W. H., & McLean, E. R. (1992). Information systems success: The quest for the dependent variable. Information Systems Research, 3(1), 60-95.",
             locator="3(1):60-95", locator_type="page_range",
             supports="six interdependent dimensions of information system success", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="The DeLone and McLean Model of Information Systems Success: A Ten-Year Update",
             title_fa="مدل موفقیت سیستم‌های اطلاعاتی دِلون و مکلین: روزآمدی ده‌ساله",
             authors="DeLone, W. H.; McLean, E. R.", year=2003,
             publisher="Journal of Management Information Systems",
             doi="10.1080/07421222.2003.11045748",
             url="https://www.tandfonline.com/doi/abs/10.1080/07421222.2003.11045748",
             language="en", isbn=None,
             citation="DeLone, W. H., & McLean, E. R. (2003). The DeLone and McLean model of information systems success: A ten-year update. Journal of Management Information Systems, 19(4), 9-30.",
             locator="19(4):9-30", locator_type="page_range",
             supports="addition of service quality and net benefits to the 1992 model", verified=True),
    ],
}

ENRICH = {
    "MC-643": dict(
        year=2002,
        summary="مدل رژیم ترکیبی رقابتی، که استیون لویتسکی و لوکان وِی در سال ۲۰۰۲ صورت‌بندی کردند، دسته‌ای از رژیم‌ها را توصیف می‌کند که در آن‌ها نهادهای رسمی دموکراسی وجود دارند اما میدان رقابت به‌طور نظام‌مند به سود حاکمان چیده شده است. انتخابات برگزار می‌شود و مخالفان می‌توانند رقابت کنند، اما دولت از منابع عمومی، رسانه‌ها و دستگاه قضایی برای ماندن در قدرت استفاده می‌کند. رسانه در این مدل جایگاه دوگانه دارد: از یک سو، فضای نسبی برای نقد و رقابت باقی می‌ماند؛ از سوی دیگر، تلویزیون و مطبوعات اصلی اغلب در اختیار حاکمان یا متحدان اقتصادی آن‌ها هستند و روزنامه‌نگاران مستقل با آزار، شکایت و فشار اقتصادی روبه‌رو می‌شوند. نتیجه، رسانه‌ای است که هم‌زمان پراتفاق و ناکامل است: صدای مخالف شنیده می‌شود، اما به‌ندرت به قدرت می‌رسد. مدل در تحلیل رسانه در ترکیه، روسیه، مجارستان و کشورهای پسااستعماری به کار رفته است. نقدهای اصلی به آن، ابهام مرز با دموکراسی ناقص، تمرکز بر سطح ملی، کم‌توجهی به پلتفرم‌های دیجیتال و دشواری سنجش نابرابری میدان را برجسته می‌کنند.",
        definition="مدل رژیم ترکیبی رقابتی، نظامی را توصیف می‌کند که انتخابات و نهادهای رسمی دموکراسی را دارد اما دولت با دستکاری میدان رقابت، رسانه و قوهٔ قضایی، مزیت پایدار برای خود می‌سازد.",
        main_problem="چگونه رژیمی می‌تواند هم‌زمان انتخابات و رسانهٔ نسبتاً آزاد داشته باشد و در قدرت بماند، و رسانه در این وضعیت دوگانه چه نقشی در بقا یا تضعیف آن ایفا می‌کند.",
        mechanism="دولت با کنترل مالکیت و یارانهٔ رسانه، آزار حقوقی روزنامه‌نگاران و دسترسی نامتقارن به منابع، میدان رقابت را نابرابر می‌کند؛ فضای نقد باقی می‌ماند اما به ابزار تغییر قدرت بدل نمی‌شود.",
        assumptions=[
            "نهادهای رسمی دموکراسی وجود دارند.",
            "میدان رقابت نابرابر است.",
            "دولت به منابع و رسانه دسترسی ممتاز دارد.",
            "مخالفان رقابت می‌کنند اما شکست می‌خورند.",
            "رسانه هم‌زمان کثرت‌گرا و مهارشده است.",
        ],
        principles=[
            "مالکیت رسانه را نقشه‌برداری کن.",
            "دسترسی نامتقارن را بسنج.",
            "آزار حقوقی را مستند کن.",
            "مرز دموکراسی و اقتدارگرایی را روشن کن.",
            "پلتفرم را به تحلیل بیفزا.",
            "میدان رقابت را نه فقط انتخابات بسنج.",
        ],
        critiques=[
            "مرز آن با دموکراسی ناقص مبهم است.",
            "بر سطح ملی متمرکز است.",
            "پلتفرم‌های دیجیتال را کم می‌بیند.",
            "سنجش نابرابری میدان دشوار است.",
            "نقش عوامل خارجی را کم‌وزن می‌کند.",
            "تجربهٔ منطقه‌ای را کم‌پوشش می‌دهد.",
            "به نقش رسانهٔ تبعیدی کم می‌پردازد.",
            "نقش سرمایهٔ خارجی را کم‌می‌بیند.",
        ],
        critique_text="منتقدان می‌گویند مدل رژیم ترکیبی رقابتی چارچوبی دقیق برای فهم اقتدارگرایی انتخاباتی ساخت اما مرز آن با دموکراسی ناقص مبهم ماند و پلتفرم‌های دیجیتال را کم‌بررسی گذاشت؛ با این حال، استاندارد تحلیل رسانه در رژیم‌های ترکیبی است.",
        applications=[
            "تحلیل رسانه در رژیم‌های ترکیبی.",
            "پژوهش گذار دموکراتیک.",
            "سنجش آزادی رسانه.",
            "سیاست حمایت از روزنامه‌نگاران.",
            "تحلیل مالکیت رسانه.",
            "مطالعات منطقه‌ای.",
            "سنجش نابرابری دسترسی به رسانه.",
        ],
        example_text="کشوری که انتخابات منظم دارد اما بزرگ‌ترین شبکهٔ تلویزیونی در اختیار خانوادهٔ حاکم است و روزنامه‌نگار منتقد با شکایت مالی تحت فشار قرار می‌گیرد، نمونهٔ رژیم ترکیبی رقابتی است؛ رسانه در ظاهر آزاد است و در عمل مهارشده.",
        evolution="مقالهٔ سال ۲۰۰۲ مفهوم اقتدارگرایی رقابتی را معرفی کرد و کتاب سال ۲۰۱۰ آن را با ۳۵ مطالعهٔ موردی و تحلیل بقا گسترد؛ پژوهش‌های بعدی، رسانه و پلتفرم را به هستهٔ تحلیل افزودند.",
        key_concepts=["اقتدارگرایی رقابتی", "رژیم ترکیبی", "میدان نابرابر", "مالکیت رسانه", "آزار حقوقی", "کثرت‌گرایی مهارشده"],
        theorists="استیون لویتسکی و لوکان ای. وِی.",
        theorists_text="مدل در سنت سیاست مقایسه‌ای و مطالعات دموکراتیزاسیون شکل گرفت.",
        model="رژیم ترکیبی که با انتخابات واقعی اما میدان رقابتی نابرابر و رسانهٔ مهارشده، قدرت حاکمان را بازتولید می‌کند.",
        studies=[
            "مقالهٔ سال ۲۰۰۲ اقتدارگرایی رقابتی را معرفی کرد.",
            "کتاب سال ۲۰۱۰ آن را با ۳۵ مورد آزمود.",
            "مطالعات رسانه، مالکیت و آزار را مستند کردند.",
            "پژوهش دیجیتال، کنترل پلتفرم را بررسی کرد.",
            "مطالعات تطبیقی، رسانهٔ ترکیبی را مقایسه کردند.",
            "پژوهش حقوقی، آزار روزنامه‌نگار را مستند کرد.",
            "مطالعات اقتصادی، یارانهٔ رسانه را تحلیل کردند.",
            "پژوهش انتخابات، پوشش نامتقارن را سنجید.",
            "مطالعات دیجیتال، سانسور نرم را بررسی کردند.",
        ],
    ),
    "MC-649": dict(
        year=1964,
        summary="مدل محیط رسانه‌ای، که در سنت بوم‌شناسی رسانه و با کار مارشال مکلوهان و جاشوا میرُویتز شکل گرفت، رسانه را نه کانالی برای انتقال پیام، بلکه محیطی می‌داند که شرایط ارتباط، ادراک و رفتار اجتماعی را می‌سازد. مکلوهان با جملهٔ «رسانه پیام است» استدلال کرد که ویژگی‌های خودِ رسانه، بیش از محتوای آن، حواس و سازمان اجتماعی را دگرگون می‌کند. میرُویتز در امتداد این سنت نشان داد که رسانه‌های الکترونیک، مرز میان صحنهٔ جلو و پشت، کودک و بزرگسال، و مرد و زن را فرو می‌ریزند و موقعیت‌های اجتماعی تازه می‌سازند. در نسخهٔ دیجیتال این مدل، پلتفرم به محیط بدل می‌شود: معماری، الگوریتم و قواعد دسترسی، رفتار کاربر و اقتصاد محتوا را شکل می‌دهند. مدل برای تحلیل گذار به پلتفرم، شکل‌گیری حباب اطلاعاتی و بازتعریف حریم خصوصی به کار می‌رود. نقدهای اصلی به آن، جبرگرایی فناورانه، ابهام مفهوم محیط، کم‌توجهی به قدرت و سیاست، و دشواری آزمون تجربی را برجسته می‌کنند؛ نقدهایی که نسخهٔ دیجیتال مدل را به سمت تحلیل معماری و قدرت سوق داده است.",
        definition="مدل محیط رسانه‌ای، رسانه را محیطی می‌داند که با ویژگی‌های فنی و معماری خود، شرایط ادراک، تعامل و سازمان اجتماعی را شکل می‌دهد، نه فقط کانالی برای انتقال محتوا.",
        main_problem="رسانه‌ها چگونه فراتر از محتوایشان، محیط زندگی اجتماعی را دگرگون می‌کنند و پلتفرم‌های دیجیتال چه نوع محیط تازه‌ای می‌سازند.",
        mechanism="هر رسانه، نسبت حواس، سرعت و دامنهٔ دسترسی را تغییر می‌دهد؛ این تغییر، مرز موقعیت‌های اجتماعی را جابه‌جا می‌کند و رفتار، هویت و روابط قدرت را بازآرایی می‌کند.",
        assumptions=[
            "رسانه محیط است، نه فقط کانال.",
            "ویژگی رسانه بر محتوا مقدم است.",
            "رسانه مرز موقعیت‌ها را جابه‌جا می‌کند.",
            "فناوری، شکل ادراک را می‌سازد.",
            "معماری پلتفرم رفتار را شکل می‌دهد.",
        ],
        principles=[
            "خودِ رسانه را تحلیل کن.",
            "معماری و قواعد را ببین.",
            "مرز صحنه و پشت صحنه را بسنج.",
            "اثر محیطی را از اثر محتوایی جدا کن.",
            "قدرت طراحی را جدی بگیر.",
            "جبرگرایی را نقد کن.",
        ],
        critiques=[
            "جبرگرایی فناورانه دارد.",
            "مفهوم محیط مبهم است.",
            "قدرت و سیاست را کم می‌بیند.",
            "آزمون تجربی آن دشوار است.",
            "نقش کاربر را منفعل فرض می‌کند.",
            "تفاوت فرهنگی را کم‌وزن می‌کند.",
            "به اقتصاد رسانه کم می‌پردازد.",
            "انواع پلتفرم را یکسان می‌گیرد.",
            "به سیاست‌گذاری رسانه کم می‌پردازد.",
        ],
        critique_text="منتقدان می‌گویند مدل محیط رسانه‌ای بینش نیرومندی دربارهٔ اثر شکل رسانه داد اما به جبرگرایی فناورانه نزدیک شد و قدرت اجتماعی را کم‌بررسی گذاشت؛ با این حال، چارچوب اصلی تحلیل پلتفرم به‌عنوان محیط است.",
        applications=[
            "تحلیل گذار به پلتفرم.",
            "پژوهش حباب اطلاعاتی.",
            "بازتعریف حریم خصوصی.",
            "آموزش سواد رسانه‌ای.",
            "طراحی سیاست فناوری.",
            "مطالعات کودکی و رسانه.",
            "تحلیل معماری تعامل.",
        ],
        example_text="تلفن هوشمند فقط پیام رسانه‌ای را عوض نکرد؛ مرز خانه و محل کار، خصوصی و عمومی، و کودک و بزرگسال را جابه‌جا کرد؛ همین جابه‌جایی است که مدل محیط رسانه‌ای بر آن انگشت می‌گذارد.",
        evolution="مکلوهان در سال ۱۹۶۴ رسانه را محیط خواند و میرُویتز در سال ۱۹۸۵ آن را به موقعیت اجتماعی گره زد؛ پژوهش پلتفرم در دههٔ ۲۰۱۰، همان منطق را به معماری الگوریتمی تعمیم داد.",
        key_concepts=["بوم‌شناسی رسانه", "رسانه پیام است", "محیط اطلاعاتی", "موقعیت اجتماعی", "معماری پلتفرم", "مرز صحنه"],
        theorists="مارشال مکلوهان و جاشوا میرُویتز.",
        theorists_text="مدل در سنت بوم‌شناسی رسانه شکل گرفت.",
        model="رسانه به‌عنوان محیطی که با تغییر نسبت حواس و مرز موقعیت‌ها، رفتار و سازمان اجتماعی را دگرگون می‌کند.",
        studies=[
            "کتاب سال ۱۹۶۴ رسانه را محیط خواند.",
            "کتاب سال ۱۹۸۵ موقعیت اجتماعی را افزود.",
            "مطالعات پلتفرم، معماری الگوریتم را تحلیل کردند.",
            "پژوهش حباب، محیط اطلاعاتی را آزمود.",
            "مطالعات کودک، مرز سنی را بررسی کردند.",
            "پژوهش حریم خصوصی، معماری داده را تحلیل کرد.",
            "مطالعات تاریخ رسانه، گذار محیطی را روایت کردند.",
            "پژوهش سیاست، مقررات پلتفرم را بررسی کرد.",
            "مطالعات سواد، درک محیط را سنجیدند.",
            "پژوهش موبایل، محیط همیشه‌روشن را تحلیل کرد.",
            "مطالعات معماری، رابط کاربر را محیط رفتار خواند.",
            "پژوهش دیجیتال، محیط الگوریتمی را نقد کرد.",
        ],
    ),
    "MC-650": dict(
        year=2016,
        summary="مدل خودکارسازی خبر، که با گزارش آندریاس گرافِه در سال ۲۰۱۶ و پژوهش‌های پس از آن صورت‌بندی شد، تولید خبر را در بخش‌هایی از زنجیرهٔ تحریریه به الگوریتم و تولید زبان طبیعی می‌سپارد. در این مدل، داده‌های ساختاریافته مانند نتایج ورزشی، گزارش مالی یا آمار آب‌وهوا به قالب‌های زبانی از پیش تعریف‌شده فرستاده می‌شوند و خبر بدون دخالت مستقیم انسان تولید می‌شود. مدل سه لایه را از هم جدا می‌کند: داده، الگوی زبانی و نظارت انسانی. خودکارسازی سرعت، دقت و مقیاس را بالا می‌برد و خبرنگار را برای تحلیل و تحقیق آزاد می‌کند، اما پرسش مسئولیت، شفافیت و کیفیت را پیش می‌آورد. پژوهش‌های مخاطب نشان دادند که خوانندگان، خبر خودکار را پیش از آزمون کم‌ارزش‌تر می‌دانند اما در ارزیابی واقعی تفاوت کمتری می‌بینند. در رسانه، مدل برای پوشش انتخاباتی، ورزشی و داده‌محور به کار می‌رود. نقدهای اصلی به آن، خطای پنهان داده، یکسان‌سازی زبان، کاهش مهارت خبرنگار، ابهام مسئولیت و خطر خودکارسازی سوگیری را برجسته می‌کنند؛ نقدهایی که حکمرانی الگوریتمی را به دستور کار تحریریه بدل کرده‌اند.",
        definition="مدل خودکارسازی خبر، تولید بخشی از خبر را به زنجیرهٔ داده، الگوی زبانی و الگوریتم می‌سپارد و نقش انسان را به طراحی قالب، نظارت و تفسیر محدود می‌کند.",
        main_problem="کدام بخش‌های تولید خبر را می‌توان به الگوریتم سپرد، این سپردن چه پیامدی برای کیفیت، اشتغال و مسئولیت خبر دارد و مخاطب چگونه خبر خودکار را ارزیابی می‌کند.",
        mechanism="داده‌های ساختاریافته به قالب‌های زبانی وارد می‌شوند و متن خبر به‌طور خودکار تولید می‌شود؛ انسان قالب و نظارت را طراحی می‌کند و در موارد پیچیده، بازبینی انسانی وارد می‌شود.",
        assumptions=[
            "داده ساختاریافته در دسترس است.",
            "الگوی زبانی قابل تعریف است.",
            "نظارت انسانی ممکن است.",
            "بخشی از خبر قابل قالب‌بندی است.",
            "مخاطب خبر خودکار را می‌پذیرد.",
        ],
        principles=[
            "داده را پیش از الگو پاک کن.",
            "قالب را شفاف و قابل ردیابی بساز.",
            "مرز نظارت انسانی را روشن کن.",
            "خطا را پایش و اصلاح کن.",
            "مسئولیت حقوقی را تعیین کن.",
            "مهارت خبرنگار را به تحلیل ببر.",
        ],
        critiques=[
            "خطای داده پنهان می‌ماند.",
            "زبان را یکسان می‌کند.",
            "مهارت خبرنگار را کاهش می‌دهد.",
            "مسئولیت را مبهم می‌سازد.",
            "سوگیری الگو را بازتولید می‌کند.",
            "تحقیق عمیق را جایگزین نمی‌شود.",
            "شفافیت الگوریتم را کم می‌سازد.",
            "به اتحادیه‌های حرفه‌ای کم می‌پردازد.",
            "خطای زبانی را کم‌می‌بیند.",
        ],
        critique_text="منتقدان می‌گویند خودکارسازی خبر سرعت و مقیاس آورد اما خطای داده، یکسان‌سازی زبان و ابهام مسئولیت را به تحریریه افزود؛ با این حال، چارچوب اصلی تحلیل تولید الگوریتمی خبر است.",
        applications=[
            "پوشش خودکار ورزش.",
            "گزارش مالی الگوریتمی.",
            "پوشش انتخاباتی داده‌محور.",
            "طراحی گردش کار تحریریه.",
            "آموزش روزنامه‌نگاری داده.",
            "سنجش اعتماد مخاطب.",
            "ارزیابی کیفیت متن خودکار.",
        ],
        example_text="خبرگزاری‌ای که نتایج بازی‌های محلی را با الگو منتشر می‌کند، خبرنگار را برای تحقیق دربارهٔ باشگاه آزاد می‌کند؛ همان سیستم اگر داده را بی‌بازبینی منتشر کند، خطای آماری را با سرعت بالا تکثیر می‌کند.",
        evolution="گزارش سال ۲۰۱۶ چارچوب عملی خودکارسازی را داد و پژوهش سال ۲۰۱۷ ادراک مخاطب را آزمود؛ پژوهش‌های بعدی، آن را به تولید محتوای مولد و نظارت الگوریتمی گستردند.",
        key_concepts=["تولید زبان طبیعی", "داده ساختاریافته", "الگوی زبانی", "نظارت انسانی", "اعتماد مخاطب", "مسئولیت الگوریتمی"],
        theorists="آندریاس گرافِه؛ ماریو هایم.",
        theorists_text="مدل در سنت روزنامه‌نگاری داده و مطالعات الگوریتم شکل گرفت.",
        model="تولید خودکار بخشی از خبر از راه داده، الگو و نظارت انسانی با پیامدهایی برای کیفیت، کار و مسئولیت.",
        studies=[
            "گزارش سال ۲۰۱۶ چارچوب تولید را داد.",
            "پژوهش سال ۲۰۱۷ ادراک مخاطب را سنجید.",
            "مطالعات تحریریه، اثر بر کار خبرنگار را تحلیل کردند.",
            "پژوهش مسئولیت، شفافیت الگوریتم را بررسی کرد.",
            "مطالعات اشتغال، جابه‌جایی مهارت را ردیابی کردند.",
            "پژوهش کیفیت، خطای داده را سنجید.",
            "مطالعات مخاطب، اعتماد را بین دو نوع خبر مقایسه کردند.",
            "پژوهش اخلاق، مسئولیت را در زنجیرهٔ خودکار بررسی کرد.",
            "مطالعات دیجیتال، خبر مولد را تحلیل کردند.",
            "پژوهش تولید، گردش کار خودکار را ترسیم کرد.",
            "مطالعات خبرگزاری، پذیرش الگو را سنجیدند.",
        ],
    ),
    "MC-652": dict(
        year=1992,
        summary="مدل موفقیت سیستم‌های اطلاعاتی، که ویلیام دِلون و افرایم مکلین در سال ۱۹۹۲ معرفی کردند، موفقیت یک سیستم اطلاعاتی را نه یک متغیر، بلکه شش بُعد به‌هم‌پیوسته می‌داند: کیفیت سیستم، کیفیت اطلاعات، استفاده، رضایت کاربر، تأثیر فردی و تأثیر سازمانی. مدل در سال ۲۰۰۳ با افزودن کیفیت خدمات و مفهوم منافع خالص بازنگری شد: کیفیت سیستم، اطلاعات و خدمات بر استفاده و رضایت اثر می‌گذارند و این دو به منافع خالص می‌رسند. حلقهٔ بازخورد نیز میان منافع و استفاده و رضایت برقرار است. این مدل به چارچوب مرجع سنجش اثربخشی فناوری اطلاعات بدل شد. در رسانه، مدل برای ارزیابی سیستم مدیریت محتوا، اپلیکیشن خبری، سامانهٔ آرشیو و پلتفرم تحریریه به کار می‌رود: کیفیت فنی، اعتبار محتوا و پشتیبانی، پذیرش و رضایت خبرنگار و سرانجام ارزش سازمانی را به هم می‌پیوندد. نقدهای اصلی به آن، سادگی روابط، ابهام تعریف منافع خالص، کم‌توجهی به زمینهٔ سازمانی و دشواری سنجش طولی را برجسته می‌کنند؛ با این حال، واژگان آن استاندارد ارزیابی فناوری در رسانه شده است.",
        definition="مدل موفقیت سیستم‌های اطلاعاتی، موفقیت را در شش بُعد کیفیت سیستم، کیفیت اطلاعات، استفاده، رضایت کاربر، تأثیر فردی و تأثیر سازمانی می‌بیند و در بازنگری ۲۰۰۳ کیفیت خدمات و منافع خالص را می‌افزاید.",
        main_problem="موفقیت یک سیستم اطلاعاتی را چگونه می‌توان سنجید، کدام ابعاد بر یکدیگر اثر می‌گذارند و سازمان رسانه‌ای چگونه می‌تواند ارزش فناوری اطلاعات خود را ارزیابی کند.",
        mechanism="کیفیت فنی، محتوایی و خدماتی، استفاده و رضایت را می‌سازد؛ استفاده و رضایت به تأثیر فردی و سازمانی می‌رسند و بازخورد منافع، چرخهٔ بهبود سیستم را می‌بندد.",
        assumptions=[
            "موفقیت چندبعدی است.",
            "کیفیت پیش‌شرط استفاده است.",
            "استفاده و رضایت به هم می‌پیوندند.",
            "منافع در دو سطح سنجیده می‌شود.",
            "بازخورد، سیستم را بهبود می‌دهد.",
        ],
        principles=[
            "کیفیت سیستم را بسنج.",
            "کیفیت اطلاعات را جدا بسنج.",
            "کیفیت خدمات را فراموش نکن.",
            "استفاده و رضایت را هم‌زمان بگیر.",
            "منافع خالص را تعریف کن.",
            "بازخورد را در طراحی برگردان.",
        ],
        critiques=[
            "روابط را ساده می‌گیرد.",
            "منافع خالص مبهم است.",
            "زمینهٔ سازمانی را کم می‌بیند.",
            "سنجش طولی دشوار است.",
            "تفاوت کاربران را کم‌وزن می‌کند.",
            "به فرهنگ سازمانی کم می‌پردازد.",
            "کیفیت خدمات را متغیر مستقل ساده می‌گیرد.",
            "به تفاوت نسل کاربران کم می‌پردازد.",
            "بازخورد منافع را یک‌سویه می‌گیرد.",
        ],
        critique_text="منتقدان می‌گویند مدل موفقیت سیستم‌های اطلاعاتی چارچوبی روشن برای سنجش ساخت اما روابط را ساده کرد و زمینهٔ سازمانی و تفاوت کاربران را کم‌بررسی گذاشت؛ با این حال، مرجع اصلی ارزیابی فناوری اطلاعات است.",
        applications=[
            "ارزیابی سیستم مدیریت محتوا.",
            "سنجش اپلیکیشن خبری.",
            "ارزیابی سامانهٔ آرشیو.",
            "طراحی پلتفرم تحریریه.",
            "پژوهش فناوری اطلاعات.",
            "آموزش مدیریت رسانه.",
            "سنجش بازگشت سرمایهٔ فناوری.",
        ],
        example_text="تحریریه‌ای که سامانهٔ تازه می‌آورد اما کیفیت اطلاعات آرشیو و پشتیبانی را نمی‌سنجد، با سیستم سریع اما بی‌اعتماد روبه‌رو می‌شود؛ مدل نشان می‌دهد که رضایت خبرنگار از کیفیت اطلاعات، نه از سرعت صرف، می‌آید.",
        evolution="مقالهٔ سال ۱۹۹۲ شش بُعد را معرفی کرد و بازنگری سال ۲۰۰۳ کیفیت خدمات و منافع خالص را افزود؛ پژوهش‌های بعدی، مدل را به سیستم‌های موبایل و پلتفرم رسانه تعمیم دادند.",
        key_concepts=["کیفیت سیستم", "کیفیت اطلاعات", "کیفیت خدمات", "رضایت کاربر", "منافع خالص", "استفاده"],
        theorists="ویلیام اچ. دِلون و افرایم آر. مکلین.",
        theorists_text="مدل در سنت سنجش اثربخشی سیستم‌های اطلاعاتی شکل گرفت.",
        model="موفقیت سیستم اطلاعاتی به‌عنوان زنجیرهٔ کیفیت، استفاده، رضایت و منافع خالص در دو سطح فردی و سازمانی.",
        studies=[
            "مقالهٔ سال ۱۹۹۲ شش بُعد را معرفی کرد.",
            "بازنگری سال ۲۰۰۳ کیفیت خدمات را افزود.",
            "مطالعات رسانه، سیستم مدیریت محتوا را ارزیابی کردند.",
            "پژوهش موبایل، رضایت کاربر را سنجید.",
            "مطالعات طولی، منافع خالص را ردیابی کردند.",
            "پژوهش سازمانی، کیفیت خدمات را آزمود.",
            "مطالعات کاربر، سواد دیجیتال را عامل تعدیل یافتند.",
            "پژوهش ارزیابی، منافع خالص را در رسانه سنجید.",
            "مطالعات پلتفرم، کیفیت سیستم را بازتعریف کردند.",
            "پژوهش کاربر، رضایت خبرنگار را تحلیل کرد.",
            "مطالعات موبایل، پذیرش اپلیکیشن خبری را سنجیدند.",
            "پژوهش سازمان، کیفیت خدمات پشتیبانی را تحلیل کرد.",
        ],
    ),
}

NAME_FIX = {
    "MC-643": ("مدل رژیم ترکیبی رقابتی و رسانه", "Competitive Authoritarian Regime and Media Model",
               "عنوان کارت عام بود؛ مفهوم مشخص لویتسکی و وِی، اقتدارگرایی رقابتی است."),
}
YEAR_FIX = {
    "MC-643": "بدنهٔ کارت، مدل قدرت رسانه را با انتساب به لویتسکی می‌آمیخت؛ هستهٔ مفهومی لویتسکی و وِی ۲۰۰۲ و ۲۰۱۰ ثبت شد.",
    "MC-649": "سال کارت خالی و بدنهٔ آن ترکیبی از مکلوهان و ادبیات پلتفرم بود؛ سال ۱۹۶۴ و سنت بوم‌شناسی رسانه مبنا قرار گرفت.",
    "MC-650": "بدنهٔ کارت قالب عمومی محیط رسانه‌ای بود و انتساب «کاستر» نادرست؛ محتوا بر پایهٔ گرافه ۲۰۱۶ و هایم و گرافه ۲۰۱۷ بازنویسی شد.",
    "MC-652": "بدنهٔ کارت قالب عمومی محیط رسانه‌ای بود؛ محتوا بر پایهٔ دِلون و مکلین ۱۹۹۲ و ۲۰۰۳ بازنویسی شد.",
}

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



YEAR_FIX.update({
    "MC-582": "year corrected 2000 -> 2001 (verified anchor: Baker & Martinson, TARES Test, 2001); note: editorial card theorist attribution was unverifiable and documentation rebuilt from verified literature",
    "MC-598": "no year change; note: editorial card core_logic was a mismatched media-economics template, documentation rebuilt from Heath (1993) and Ihlen (2011)",
})


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
                                       "verified": n_verified, "batch": 156}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH156 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
