# -*- coding: utf-8 -*-
"""Batch 165: MC-564 aggression cue/inhibition, MC-565 frustration-aggression, MC-490 indexing (duplicate), MC-080 computational social science."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch165-mixed-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch165_mixed.json"

S = {
    "MC-564": [
        dict(kind="BOOK",
             title_en="Aggression: A Social Psychological Analysis",
             title_fa="پرخاشگری: تحلیلی روان‌شناختی و اجتماعی",
             authors="Berkowitz, L.", year=1962,
             publisher="McGraw-Hill",
             doi=None,
             url="https://archive.org/details/aggressionsocial0000leon",
             language="en", isbn=None,
             citation="Berkowitz, L. (1962). Aggression: A Social Psychological Analysis. New York: McGraw-Hill.",
             locator="1962 edition", locator_type="edition",
             supports="cue theory of aggression and inhibitory role of punishment cues", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Weapons as Aggression-Eliciting Stimuli",
             title_fa="سلاح‌ها به‌عنوان محرک‌های برانگیزانندهٔ پرخاشگری",
             authors="Berkowitz, L.; LePage, A.", year=1967,
             publisher="Journal of Personality and Social Psychology",
             doi="10.1037/h0025008",
             url="https://psycnet.apa.org/record/1967-16673-001",
             language="en", isbn=None,
             citation="Berkowitz, L., & LePage, A. (1967). Weapons as aggression-eliciting stimuli. Journal of Personality and Social Psychology, 5(4), 411-417.",
             locator="5(4):411-417", locator_type="page_range",
             supports="weapons effect: aggression-related cues facilitate aggressive responses", verified=True),
    ],
    "MC-565": [
        dict(kind="BOOK",
             title_en="Frustration and Aggression",
             title_fa="ناکامی و پرخاشگری",
             authors="Dollard, J.; Miller, N. E.; Doob, L. W.; Mowrer, O. H.; Sears, R. R.", year=1939,
             publisher="Yale University Press",
             doi="10.1037/10022-000",
             url="https://archive.org/details/frustrationaggre00doll",
             language="en", isbn=None,
             citation="Dollard, J., Miller, N. E., Doob, L. W., Mowrer, O. H., & Sears, R. R. (1939). Frustration and Aggression. New Haven: Yale University Press.",
             locator="1939 edition", locator_type="edition",
             supports="original frustration-aggression hypothesis", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Frustration-Aggression Hypothesis: Examination and Reformulation",
             title_fa="فرضیهٔ ناکامی-پرخاشگری: بررسی و صورت‌بندی دوباره",
             authors="Berkowitz, L.", year=1989,
             publisher="Psychological Bulletin",
             doi="10.1037/0033-2909.106.1.59",
             url="https://psycnet.apa.org/record/1989-36458-001",
             language="en", isbn=None,
             citation="Berkowitz, L. (1989). Frustration-aggression hypothesis: Examination and reformulation. Psychological Bulletin, 106(1), 59-73.",
             locator="106(1):59-73", locator_type="page_range",
             supports="reformulation of frustration as an aversive stimulus producing aggressive inclination", verified=True),
    ],
    "MC-490": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Toward a Theory of Press-State Relations in the United States",
             title_fa="به سوی نظریه‌ای دربارهٔ روابط مطبوعات و دولت در ایالات متحده",
             authors="Bennett, W. L.", year=1990,
             publisher="Journal of Communication",
             doi="10.1111/j.1460-2466.1990.tb02265.x",
             url="https://academic.oup.com/joc/article-abstract/40/2/103/4210575",
             language="en", isbn=None,
             citation="Bennett, W. L. (1990). Toward a theory of press-state relations in the United States. Journal of Communication, 40(2), 103-127.",
             locator="40(2):103-127", locator_type="page_range",
             supports="indexing norm: news indexed to the range of official debate", verified=True),
        dict(kind="BOOK",
             title_en="Projections of Power: Framing News, Public Opinion, and U.S. Foreign Policy",
             title_fa="فرافکنی قدرت: چارچوب‌بندی خبر، افکار عمومی و سیاست خارجی ایالات متحده",
             authors="Entman, R. M.", year=2004,
             publisher="University of Chicago Press",
             doi="10.7208/chicago/9780226210735.001.0001",
             url="https://press.uchicago.edu/ucp/books/book/chicago/P/bo3637444.html",
             language="en", isbn=None,
             citation="Entman, R. M. (2004). Projections of Power: Framing News, Public Opinion, and U.S. Foreign Policy. Chicago: University of Chicago Press.",
             locator="2004 edition", locator_type="edition",
             supports="indexing and cascading activation in foreign-policy news", verified=True),
    ],
    "MC-080": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Computational Social Science",
             title_fa="علوم اجتماعی محاسباتی",
             authors="Lazer, D.; Pentland, A.; Adamic, L.; Aral, S.; Barabasi, A.-L.; Brewer, D.; et al.", year=2009,
             publisher="Science",
             doi="10.1126/science.1167742",
             url="https://www.science.org/doi/10.1126/science.1167742",
             language="en", isbn=None,
             citation="Lazer, D., Pentland, A., Adamic, L., Aral, S., Barabasi, A.-L., Brewer, D., et al. (2009). Computational social science. Science, 323(5915), 721-723.",
             locator="323(5915):721-723", locator_type="page_range",
             supports="programmatic definition of computational social science", verified=True),
        dict(kind="BOOK",
             title_en="Bit by Bit: Social Research in the Digital Age",
             title_fa="قطره‌قطره: پژوهش اجتماعی در عصر دیجیتال",
             authors="Salganik, M. J.", year=2018,
             publisher="Princeton University Press",
             doi=None,
             url="https://press.princeton.edu/books/paperback/9780691196107/bit-by-bit",
             language="en", isbn="9780691196107",
             citation="Salganik, M. J. (2018). Bit by Bit: Social Research in the Digital Age. Princeton, NJ: Princeton University Press.",
             locator="2018 edition", locator_type="edition",
             supports="methods, ethics and design of digital social research", verified=True),
    ],
}

ENRICH = {
    "MC-564": dict(
        year=1962,
        summary="فرضیهٔ سرکوب و محرک تهاجم، که لئونارد برکوویتز در کتاب پرخاشگری: تحلیلی روان‌شناختی و اجتماعی در سال ۱۹۶۲ صورت‌بندی کرد، دو سازوکار متقابل را در کنار هم می‌گذارد: محرک‌های مرتبط با پرخاشگری می‌توانند پاسخ پرخاشگرانه را فعال کنند و همان محرک‌ها، اگر با نشانه‌های تنبیه و هنجار همراه شوند، آن را مهار کنند. برکوویتز استدلال کرد که محرک‌های محیطی مانند سلاح، تصویر خشونت یا واژهٔ تهدید، شبکهٔ معنایی پرخاشگری را فعال می‌کنند و فرد خشمگین را به پاسخ شدیدتر وامی‌دارند. او با آنتونی لپاژ در سال ۱۹۶۷ در آزمایش سلاح نشان داد که حضور سلاح در موقعیت خشم، شدت پاسخ پرخاشگرانه را افزایش می‌دهد؛ یافته‌ای که به اثر سلاح شهرت یافت. در سوی دیگر، نشانه‌های تنبیه و پیامد منفی می‌توانند پرخاشگری را مهار کنند و همین دوگانگی، نام سرکوب و محرک را برای فرضیه ساخته است. کارلسون، مارکوس-نیوهال و میلر در فراتحلیل سال ۱۹۹۰ نشان دادند اثر محرک‌های موقعیتی کوچک اما پایدار است و به برانگیختگی و تفسیر فرد بستگی دارد. در رسانه، فرضیه برای تحلیل نمایش سلاح، بازی خشونت‌آمیز، تبلیغات تهدیدآمیز و هنجارهای مهار خشونت به کار می‌رود. نقدهای اصلی به آن، وابستگی اثر به خشم پیشین، تفاوت فردی، نگرانی اخلاقی آزمایش سلاح و تعمیم‌پذیری محدود را برجسته می‌کنند.",
        definition="فرضیهٔ سرکوب و محرک تهاجم می‌گوید محرک‌های مرتبط با پرخاشگری پاسخ پرخاشگرانه را فعال می‌کنند، اما نشانه‌های تنبیه و هنجار می‌توانند همان پاسخ را مهار کنند.",
        main_problem="چرا حضور محرک‌های مرتبط با پرخاشگری در محیط، رفتار پرخاشگرانه را افزایش یا کاهش می‌دهد و چه شرایطی جهت اثر را تعیین می‌کند.",
        mechanism="محرک محیطی مانند سلاح، شبکهٔ معنایی و هیجانی پرخاشگری را فعال می‌کند و پاسخ فرد خشمگین را شدت می‌بخشد؛ اما اگر همان محرک با نشانهٔ تنبیه و هنجار همراه شود، ترس از پیامد پاسخ را مهار می‌کند.",
        assumptions=[
            "محرک‌های محیطی معنای پرخاشگری دارند.",
            "خشم پیشین آمادگی پاسخ می‌سازد.",
            "شبکهٔ معنایی با محرک فعال می‌شود.",
            "نشانهٔ تنبیه پاسخ را مهار می‌کند.",
            "جهت اثر به تفسیر فرد بستگی دارد.",
        ],
        principles=[
            "محرک را در بافت موقعیت بسنج.",
            "خشم پیشین را کنترل کن.",
            "نشانه‌های هنجاری را جدا تحلیل کن.",
            "به تفسیر فرد توجه کن.",
            "از تعمیم آزمایشگاهی پرهیز کن.",
            "ملاحظهٔ اخلاقی را جدی بگیر.",
        ],
        critiques=[
            "اثر به خشم پیشین وابسته است.",
            "تفاوت فردی را کم می‌بیند.",
            "آزمایش سلاح نگرانی اخلاقی دارد.",
            "تعمیم آن محدود است.",
            "سنجش تفسیر دشوار است.",
            "به زمینهٔ فرهنگی کم توجه دارد.",
            "مرز فعال‌سازی و مهار روشن نیست.",
            "به اثر بلندمدت کم می‌پردازد.",
        ],
        critique_text="منتقدان می‌گویند فرضیهٔ محرک تهاجم سازوکار محیطی مهمی را نشان داد اما وابستگی آن به خشم پیشین و شرایط آزمایشگاهی، تعمیم آن را محدود می‌کند؛ با این حال، پایهٔ پژوهش اثر سلاح و خشونت رسانه‌ای است.",
        applications=[
            "تحلیل نمایش سلاح در رسانه.",
            "پژوهش بازی خشونت‌آمیز.",
            "مطالعهٔ تبلیغات تهدیدآمیز.",
            "تحلیل هنجارهای مهار خشونت.",
            "پژوهش خبر خشونت.",
            "آموزش مدیریت خشم.",
            "تحلیل طراحی محیط.",
            "مطالعهٔ اثر تصویر خشونت.",
            "تحلیل پیام‌های تهدیدآمیز سیاسی.",
            "پژوهش کنترل سلاح و رسانه.",
        ],
        example_text="فردی که پیش‌تر خشمگین شده و سپس تصویری از سلاح می‌بیند، پاسخ شدیدتری نشان می‌دهد؛ اما اگر همان تصویر با پیامد تنبیه همراه شود، ترس از مجازات پاسخ او را مهار می‌کند.",
        evolution="برکوویتز در سال ۱۹۶۲ چارچوب محرک و مهار را ساخت و در سال ۱۹۶۷ اثر سلاح را آزمود؛ فراتحلیل‌های دههٔ ۱۹۹۰ اندازهٔ اثر را کوچک اما پایدار یافتند و پژوهش دیجیتال، محرک‌های نمادین شبکه‌ای را بررسی کرد.",
        key_concepts=["محرک تهاجم", "اثر سلاح", "سرکوب", "شبکهٔ معنایی", "برانگیختگی", "هنجار تنبیه"],
        theorists="لئونارد برکوویتز، آنتونی لپاژ و مایکل کارلسون.",
        theorists_text="فرضیه در سنت روان‌شناسی اجتماعی پرخاشگری شکل گرفت.",
        model="محرک محیطی به‌عنوان فعال‌کننده یا مهارکنندهٔ پاسخ پرخاشگرانه.",
        studies=[
            "کتاب سال ۱۹۶۲ چارچوب را ساخت.",
            "آزمایش سال ۱۹۶۷ اثر سلاح را نشان داد.",
            "فراتحلیل سال ۱۹۹۰ اندازهٔ اثر را سنجید.",
            "مطالعهٔ بازی، محرک را بررسی کرد.",
            "پژوهش خبر، خشونت را تحلیل کرد.",
            "مطالعهٔ محیط، هنجار را سنجید.",
        ],
    ),
    "MC-565": dict(
        year=1939,
        summary="فرضیهٔ ناکامی و پرخاشگری، که جان دولارد، نیل میلر، لئونارد دوب، اُ هابارت ماورر و رابرت سیرز در سال ۱۹۳۹ در دانشگاه ییل صورت‌بندی کردند، می‌گوید ناکامی همواره نوعی آمادگی برای پرخاشگری می‌سازد و پرخاشگری در نهایت به ناکامی برمی‌گردد. در صورت‌بندی اولیه، ناکامی به معنای بازداشتن فرد از رسیدن به هدفی بود که انتظار داشت به آن برسد و پرخاشگری پاسخ طبیعی به این بازداشت شمرده می‌شد. نظریه‌پردازان ییل به جابه‌جایی پرخاشگری توجه کردند: اگر منبع ناکامی قوی یا نامرئی باشد، خشم به هدفی ضعیف‌تر یا بی‌گناه منتقل می‌شود. لئونارد برکوویتز در سال ۱۹۸۹ این فرضیه را بازبینی کرد و گفت ناکامی نه علت یکتای پرخاشگری، بلکه یک محرک آزارنده است که آمادگی پرخاشگری را برمی‌انگیزد و تفسیر فرد و نشانه‌های موقعیت، وقوع رفتار را تعیین می‌کنند. در رسانه، فرضیه برای تحلیل پیام ناکامی اقتصادی، بی‌عدالتی خبری، سازوکار بزغاله و خصومت آنلاین به کار می‌رود. نقدهای اصلی به آن، جبرگرایی اولیه، فرض پیوند یک‌به‌یک ناکامی و پرخاشگری، کم‌توجهی به تفاوت فردی و دشواری سنجش ناکامی را برجسته می‌کنند.",
        definition="فرضیهٔ ناکامی و پرخاشگری می‌گوید ناکامی آمادگی و انگیزهٔ پرخاشگری می‌سازد و پرخاشگری به‌طور معمول پاسخی به بازداشتن فرد از هدف مورد انتظار است.",
        main_problem="چرا ناکامی به پرخاشگری می‌انجامد، چه شرایطی این پیوند را تقویت می‌کند و چرا خشم گاه به هدفی بی‌گناه منتقل می‌شود.",
        mechanism="بازداشتن فرد از هدف، حالت آزارنده و برانگیختگی می‌سازد؛ این حالت آمادگی پرخاشگری را فعال می‌کند و اگر منبع ناکامی دست‌نیافتنی باشد، خشم به هدف ضعیف‌تر جابه‌جا می‌شود.",
        assumptions=[
            "ناکامی بازداشتن از هدف است.",
            "ناکامی حالت آزارنده می‌سازد.",
            "آمادگی پرخاشگری فعال می‌شود.",
            "پرخاشگری می‌تواند جابه‌جا شود.",
            "تفسیر موقعیت رفتار را تعیین می‌کند.",
        ],
        principles=[
            "منبع ناکامی را مشخص کن.",
            "هدف جابه‌جایی را رصد کن.",
            "تفسیر فرد را در تحلیل بگنجان.",
            "به تفاوت فردی توجه کن.",
            "از جبرگرایی پرهیز کن.",
            "زمینهٔ ساختاری ناکامی را ببین.",
        ],
        critiques=[
            "جبرگرایی اولیه دارد.",
            "پیوند یک‌به‌یک را فرض می‌کند.",
            "تفاوت فردی را کم می‌بیند.",
            "سنجش ناکامی دشوار است.",
            "به زمینهٔ فرهنگی کم توجه دارد.",
            "به پرخاشگری ابزاری کم می‌پردازد.",
            "به نقش رسانه در ناکامی کم توجه است.",
            "به ناکامی ناشی از مقایسهٔ اجتماعی کم توجه است.",
            "تعمیم آزمایشگاهی محدود است.",
        ],
        critique_text="منتقدان می‌گویند صورت‌بندی اولیه فرضیه جبرگرایانه بود اما بازبینی برکوویتز آن را به رابطه‌ای مشروط و تفسیری بدل کرد؛ امروز فرضیه نه علت یکتا، بلکه چارچوب پایهٔ مطالعهٔ خشم و ناکامی است.",
        applications=[
            "تحلیل ناکامی اقتصادی.",
            "پژوهش بی‌عدالتی خبری.",
            "مطالعهٔ سازوکار بزغاله.",
            "تحلیل خصومت آنلاین.",
            "پژوهش اعتراض اجتماعی.",
            "تحلیل خبر بحران.",
            "مطالعهٔ تبعیض و خشم.",
            "آموزش مدیریت خشم.",
            "تحلیل خشونت ورزشی.",
            "پژوهش رابطهٔ محرومیت و پرخاشگری.",
            "تحلیل ناکامی در مناطق محروم.",
            "پژوهش خشم در بازار کار.",
            "مطالعهٔ ناکامی در ورزش حرفه‌ای.",
            "تحلیل ناکامی و خشونت خانگی.",
        ],
        example_text="گروهی که احساس می‌کند فرصت‌های اقتصادی خود را از دست داده است، خشم خود را به گروهی ضعیف‌تر و بی‌گناه منتقل می‌کند؛ فرضیه می‌گوید این جابه‌جایی، پاسخ ناکامی است، نه علت مستقل.",
        evolution="دولارد و همکاران در سال ۱۹۳۹ فرضیه را ساختند و پژوهش‌های دههٔ ۱۹۴۰ جابه‌جایی را بررسی کردند؛ برکوویتز در سال ۱۹۸۹ آن را به محرک آزارنده و تفسیر شناختی بازبینی کرد و پژوهش رسانه، فرضیه را به خبر و شبکه‌های اجتماعی برد.",
        key_concepts=["ناکامی", "پرخاشگری", "جابه‌جایی", "محرک آزارنده", "بزغاله", "تفسیر موقعیت"],
        theorists="جان دولارد، نیل میلر، لئونارد برکوویتز و رابرت سیرز.",
        theorists_text="فرضیه در سنت روان‌کاوی و روان‌شناسی اجتماعی ییل شکل گرفت.",
        model="ناکامی به‌عنوان محرک آزارنده‌ای که آمادگی پرخاشگری می‌سازد و می‌تواند جابه‌جا شود.",
        studies=[
            "کتاب سال ۱۹۳۹ فرضیه را ساخت.",
            "پژوهش دههٔ ۱۹۴۰ جابه‌جایی را بررسی کرد.",
            "بازبینی سال ۱۹۸۹ پیوند را مشروط کرد.",
            "مطالعهٔ بزغاله، جابه‌جایی را تحلیل کرد.",
            "پژوهش خبر، ناکامی را سنجید.",
            "مطالعهٔ دیجیتال، خصومت را بررسی کرد.",
            "مطالعهٔ ناکامی در گروه‌های کم‌درآمد.",
            "پژوهش ناکامی رسانه‌ای در بلایا.",
            "تحلیل ناکامی و اعتماد سیاسی.",
            "مطالعهٔ مقایسه‌ای ناکامی در دو کشور.",
        ],
    ),
    "MC-490": dict(
        year=1990,
        summary="فرضیهٔ نمایه‌سازی، که دبلیو لنس بنت در سال ۱۹۹۰ صورت‌بندی کرد، می‌گوید خبر سیاسی به گسترهٔ دیدگاه‌های مطرح‌شده در نهادهای رسمی نمایه می‌شود و صداهای بیرون این دامنه کمتر به خبر راه می‌یابند. این کارت رکورد دوم همین فرضیه است و با رکورد اصلی هم‌پوشانی کامل دارد؛ ثبت دوبارهٔ آن نشان می‌دهد که عنوان فارسی «ایندکس‌کردن» در فهرست نخستین، معادل دقیق مفهوم را نمی‌رساند. بنت نشان داد خبرنگاران واشینگتن صداهایی را پوشش می‌دهند که در چارچوب بحث نخبگان رسمی جای دارند و تنها وقتی نخبگان درونی اختلاف پیدا می‌کنند، دامنهٔ پوشش باز می‌شود. مطبوعات در این مدل نه کاملاً مستقل از دولت و نه کاملاً فرمان‌بردار آن، بلکه نیمه‌مستقل‌اند. سازوکار نظریه سه لایه دارد: تعریف دامنهٔ بحث رسمی، هم‌ترازی گزارش با آن دامنه و بازشدن پوشش در هنگام شکاف نخبگان. پژوهش بعدی، این منطق را به بحران رسوایی و جنگ عراق برد. در رسانه، فرضیه برای تحلیل پوشش سیاست خارجی، سکوت خبری و رابطهٔ خبرنگار با منابع رسمی به کار می‌رود. نقدهای اصلی به آن، نخبه‌محوری، کم‌توجهی به افکار عمومی، دشواری سنجش دامنهٔ نمایه و تعمیم‌پذیری محدود است.",
        definition="فرضیهٔ نمایه‌سازی می‌گوید پوشش خبری سیاست به گسترهٔ دیدگاه‌های مطرح در نهادهای رسمی نمایه می‌شود و صداهای بیرون آن دامنه کمتر شنیده می‌شوند.",
        main_problem="چرا خبر برخی دیدگاه‌ها را پررنگ و برخی را خاموش می‌کند و رابطهٔ مطبوعات با دولت چگونه دامنهٔ پوشش را تعیین می‌کند.",
        mechanism="دامنهٔ بحث رسمی تعریف می‌شود؛ گزارش خبری با آن هم‌تراز می‌شود؛ تنها با اختلاف نخبگان درونی، پوشش به دیدگاه‌های بیرونی باز می‌شود و در غیر این صورت سکوت خبری پایدار می‌ماند.",
        assumptions=[
            "خبر آینهٔ واقعیت نیست.",
            "نخبگان رسمی دامنهٔ بحث را می‌سازند.",
            "خبرنگار به منابع رسمی وابسته است.",
            "اختلاف نخبگان پوشش را باز می‌کند.",
            "مطبوعات نیمه‌مستقل‌اند.",
        ],
        principles=[
            "دامنهٔ بحث رسمی را مشخص کن.",
            "صداهای بیرون دامنه را رصد کن.",
            "اختلاف نخبگان را نشانهٔ بازشدن بدان.",
            "سکوت خبری را نیز داده بدان.",
            "وابستگی منبع و خبر را بسنج.",
            "به رسانهٔ جایگزین توجه کن.",
        ],
        critiques=[
            "نخبه‌محور است.",
            "افکار عمومی را کم می‌بیند.",
            "رسانهٔ جایگزین را نادیده می‌گیرد.",
            "سنجش دامنهٔ نمایه دشوار است.",
            "تعمیم آن به غیرآمریکا محدود است.",
            "به قدرت ساختاری رسانه کم می‌پردازد.",
            "نقش روزنامه‌نگاری تحقیقی را کم می‌بیند.",
            "به پویایی رسانهٔ دیجیتال کم توجه دارد.",
        ],
        critique_text="منتقدان می‌گویند نمایه‌سازی رابطهٔ خبر و دولت را دقیق نشان داد اما نخبه‌محور است و رسانهٔ جایگزین را کم می‌بیند؛ با این حال، چارچوب پایهٔ تحلیل پوشش سیاسی است.",
        applications=[
            "تحلیل پوشش سیاست خارجی.",
            "پژوهش خبر انتخابات.",
            "مطالعهٔ منابع رسمی خبر.",
            "تحلیل سکوت خبری.",
            "پژوهش روابط مطبوعات و دولت.",
            "آموزش روزنامه‌نگاری سیاسی.",
            "تحلیل پوشش رسوایی.",
            "مطالعهٔ تنوع صدا در خبر.",
            "تحلیل پوشش بحران در تلویزیون دولتی.",
            "پژوهش خبر در دورهٔ اعتراض.",
            "تحلیل پوشش سیاست داخلی در خبرگزاری‌های دولتی.",
        ],
        example_text="تا وقتی مقام‌ها دربارهٔ یک سیاست اختلاف علنی ندارند، خبرگزاری‌ها همان چارچوب رسمی را بازتولید می‌کنند؛ با آشکار شدن شکاف، صداهای منتقد ناگهان به خبر راه می‌یابند.",
        evolution="بنت در سال ۱۹۹۰ فرضیه را ساخت و در پژوهش‌های بعدی با لارنس و لیوینگستون آن را به بحران عراق برد؛ انتمن در سال ۲۰۰۴ آن را با فعال‌سازی آبشاری ترکیب کرد و پژوهش دیجیتال، نمایه‌سازی را به رسانهٔ شبکه‌ای گسترد.",
        key_concepts=["نمایه‌سازی", "دامنهٔ بحث رسمی", "نخبگان", "نیمه‌مستقل", "سکوت خبری", "منبع رسمی"],
        theorists="دبلیو لنس بنت، رجینا لارنس و استیون لیوینگستون.",
        theorists_text="فرضیه در سنت پژوهش روابط مطبوعات و دولت شکل گرفت.",
        model="خبر سیاسی به‌عنوان نمایهٔ دامنهٔ بحث نخبگان رسمی، نه آینهٔ افکار عمومی.",
        studies=[
            "مقالهٔ سال ۱۹۹۰ فرضیه را ساخت.",
            "پژوهش رسوایی، سکوت خبری را سنجید.",
            "کتاب سال ۲۰۰۷ بحران عراق را تحلیل کرد.",
            "کتاب سال ۲۰۰۴ مدل آبشاری را افزود.",
            "مطالعهٔ انتخابات، دامنهٔ پوشش را سنجید.",
            "پژوهش دیجیتال، نمایه‌سازی شبکه‌ای را بررسی کرد.",
            "مطالعهٔ پوشش انتخابات، دامنهٔ نمایه را سنجید.",
        ],
    ),
    "MC-080": dict(
        year=2009,
        summary="علوم اجتماعی محاسباتی، که دیوید لیزر و همکاران در سال ۲۰۰۹ در مقالهٔ مجلهٔ ساینس صورت‌بندی کردند، حوزه‌ای میان‌رشته‌ای است که داده‌های دیجیتال و روش‌های محاسباتی را برای مطالعهٔ رفتار اجتماعی به کار می‌گیرد. ردپای دیجیتال کاربران، از جست‌وجو و شبکهٔ اجتماعی تا تلفن همراه و خرید، امکان مشاهدهٔ رفتار در مقیاس بزرگ و زمان واقعی را فراهم کرده است. این حوزه سه جریان اصلی دارد: تحلیل کلان‌داده‌های رفتاری، آزمایش‌های میدانی گسترده و مدل‌سازی عامل‌محور. متیو سالگانیک در کتاب قطره‌قطره نشان داد که پژوهش دیجیتال چهار گام دارد: مشاهدهٔ رفتار، پرسیدن، آزمایش و همکاری با پلتفرم‌ها، و هر گام فرصت و محدودیت اخلاقی خود را دارد. در ارتباطات، این حوزه به مطالعهٔ انتشار خبر، شبکهٔ اجتماعی، خصومت آنلاین و اثر الگوریتم انجامید. نقدهای اصلی به آن، دسترسی انحصاری شرکت‌ها به داده، نقض حریم خصوصی، اعتبار اندازه‌گیری، سوگیری الگوریتمی، بحران تکرارپذیری و تعمیم‌پذیری محدود نمونه‌های پلتفرمی را برجسته می‌کنند.",
        definition="علوم اجتماعی محاسباتی حوزه‌ای میان‌رشته‌ای است که با داده‌های دیجیتال و روش‌های محاسباتی، رفتار اجتماعی را در مقیاس بزرگ و زمان واقعی مطالعه می‌کند.",
        main_problem="داده‌های دیجیتال چگونه می‌توانند فهم ما از رفتار اجتماعی را تغییر دهند و چه محدودیت‌های روش‌شناختی و اخلاقی برای این پژوهش وجود دارد.",
        mechanism="ردپای دیجیتال رفتار را در مقیاس بزرگ ثبت می‌کند؛ تحلیل محاسباتی الگوها را می‌یابد و آزمایش میدانی رابطهٔ علّی را می‌آزماید؛ همکاری با پلتفرم، دسترسی و اعتبار داده را تعیین می‌کند.",
        assumptions=[
            "ردپای دیجیتال رفتار را بازنمایی می‌کند.",
            "مقیاس بزرگ الگوهای نو نشان می‌دهد.",
            "آزمایش میدانی رابطهٔ علّی را می‌آزماید.",
            "دسترسی داده مشروط به پلتفرم است.",
            "اخلاق پژوهش مسئلهٔ محوری است.",
            "داده‌های پلتفرم نمایندهٔ جامعه نیست.",
        ],
        principles=[
            "اعتبار اندازه‌گیری را بسنج.",
            "حریم خصوصی را تضمین کن.",
            "سوگیری نمونه را آشکار کن.",
            "آزمایش را با مشاهده ترکیب کن.",
            "شفافیت روش را حفظ کن.",
            "همکاری با پلتفرم را اخلاقی کن.",
        ],
        critiques=[
            "دسترسی داده انحصاری است.",
            "حریم خصوصی در خطر است.",
            "اعتبار اندازه‌گیری محدود است.",
            "سوگیری الگوریتمی وجود دارد.",
            "بحران تکرارپذیری جدی است.",
            "تعمیم نمونه‌های پلتفرمی محدود است.",
            "به زمینهٔ غیرغربی کم توجه دارد.",
            "وابستگی به شرکت‌ها را کم می‌بیند.",
            "به استانداردهای شفافیت داده کم توجه است.",
            "به عدالت داده در جنوب جهانی کم توجه دارد.",
        ],
        critique_text="منتقدان می‌گویند علوم اجتماعی محاسباتی افق تازه‌ای گشود اما دسترسی انحصاری، حریم خصوصی و اعتبار اندازه‌گیری، اعتماد به یافته‌های آن را مشروط کرده است؛ با این حال، روش‌های آن به سرعت در ارتباطات نهادینه شد.",
        applications=[
            "تحلیل انتشار خبر.",
            "پژوهش شبکهٔ اجتماعی.",
            "مطالعهٔ خصومت آنلاین.",
            "تحلیل اثر الگوریتم.",
            "پژوهش افکار عمومی.",
            "آزمایش میدانی سیاست.",
            "تحلیل دادهٔ تلفن همراه.",
            "مطالعهٔ تحرک شهری.",
            "تحلیل رفتار خرید.",
            "پژوهش ارتباطات سیاسی دیجیتال.",
            "تحلیل دادهٔ کلان شبکه‌های اجتماعی.",
            "پژوهش ردیابی تماس برای سلامت عمومی.",
            "مطالعهٔ سوگیری در داده‌های پلتفرم.",
            "تحلیل اخلاق داده‌های بزرگ.",
            "تحلیل تفاوت سکوهای دیجیتال.",
        ],
        example_text="پژوهشگری با دادهٔ جست‌وجوی عمومی نشان می‌دهد که توجه به یک موضوع سلامت، پیش از اوج خبری بالا می‌رود؛ همین ردپای دیجیتال، پرسش تازه‌ای دربارهٔ رابطهٔ توجه و خبر می‌سازد.",
        evolution="لیزر و همکاران در سال ۲۰۰۹ برنامهٔ علوم اجتماعی محاسباتی را اعلام کردند و سالگانیک در سال ۲۰۱۸ چارچوب روش‌شناختی و اخلاقی آن را نظام‌مند کرد؛ پس از آن، مراکز و رشته‌های دانشگاهی و پژوهش ارتباطات محاسباتی گسترش یافت.",
        key_concepts=["علوم اجتماعی محاسباتی", "ردپای دیجیتال", "کلان‌داده", "آزمایش میدانی", "حریم خصوصی", "اعتبار اندازه‌گیری"],
        theorists="دیوید لیزر، متیو سالگانیک و الکس پنتلند.",
        theorists_text="حوزه در سنت علوم اجتماعی محاسباتی و پژوهش دادهٔ دیجیتال شکل گرفت.",
        model="رفتار اجتماعی به‌عنوان الگوی قابل مشاهده در ردپای دیجیتال و آزمون‌پذیر در آزمایش میدانی.",
        studies=[
            "مقالهٔ سال ۲۰۰۹ حوزه را اعلام کرد.",
            "کتاب سال ۲۰۱۸ روش را نظام‌مند کرد.",
            "پژوهش خبر، انتشار را تحلیل کرد.",
            "مطالعهٔ شبکه، الگو را بررسی کرد.",
            "آزمایش میدانی، اثر را سنجید.",
            "پژوهش اخلاق، حریم خصوصی را تحلیل کرد.",
            "مطالعهٔ دادهٔ تلفن همراه در بحران.",
            "پژوهش بازتولید در علوم اجتماعی محاسباتی.",
        ],
    ),
}

NAME_FIX = {
    "MC-490": ("فرضیهٔ نمایه‌سازی (رکورد دوم)", "Indexing Hypothesis (second record)", "این رکورد با فرضیهٔ نمایه‌سازی هم‌پوشانی کامل دارد و عنوان «ایندکس‌کردن» معادل دقیق مفهوم نیست؛ عنوان برای شناسایی رابطهٔ تکراری اصلاح شد."),
}
YEAR_FIX = {
    "MC-564": "کارت بدون نظریه‌پرداز و با عنوان مبهم بود؛ محتوا بر پایهٔ برکوویتز ۱۹۶۲ و برکوویتز و لپاژ ۱۹۶۷ بازنویسی شد.",
    "MC-565": "کارت بدون نظریه‌پرداز بود؛ فرضیه از دولارد و همکاران ۱۹۳۹ است و با بازبینی برکوویتز ۱۹۸۹ تکمیل شد.",
    "MC-490": "این رکورد تکراری فرضیهٔ نمایه‌سازی است؛ محتوا با رکورد اصلی هم‌راستا و بر پایهٔ بنت ۱۹۹۰ و انتمن ۲۰۰۴ مستند شد.",
    "MC-080": "کارت بدون منبع و نظریه‌پرداز بود؛ محتوا بر پایهٔ لیزر و همکاران ۲۰۰۹ و سالگانیک ۲۰۱۸ بازنویسی شد.",
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
                                       "verified": n_verified, "batch": 165}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH165 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
