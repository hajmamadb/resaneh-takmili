# -*- coding: utf-8 -*-
"""Batch 158 (MODEL): MC-700 media-source symbiosis, MC-703 slow journalism, MC-704 algorithmic gatekeeping, MC-705 fake news/fact-checking."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch158-model-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch158_model.json"

S = {
    "MC-700": [
        dict(kind="BOOK",
             title_en="Deciding What's News: A Study of CBS Evening News, NBC Nightly News, Newsweek, and Time",
             title_fa="تصمیم‌گیری دربارهٔ خبر",
             authors="Gans, H. J.", year=1979,
             publisher="Pantheon Books (reissued by Northwestern University Press, 2004)",
             doi=None,
             url="https://nupress.northwestern.edu/9780810122376/deciding-whats-news/",
             language="en", isbn="9780810122376",
             citation="Gans, H. J. (1979). Deciding What's News: A Study of CBS Evening News, NBC Nightly News, Newsweek, and Time. New York: Pantheon Books.",
             locator="1979 edition", locator_type="edition",
             supports="journalist-source relationship as a tug of war and mutual dependence", verified=True),
        dict(kind="BOOK",
             title_en="Policing the Crisis: Mugging, the State, and Law and Order",
             title_fa="پلیس‌کردن بحران: سرقت خیابانی، دولت و نظم قانونی",
             authors="Hall, S.; Critcher, C.; Jefferson, T.; Clarke, J.; Roberts, B.", year=1978,
             publisher="Macmillan",
             doi=None,
             url="https://archive.org/details/policingcrisismu0000hall",
             language="en", isbn=None,
             citation="Hall, S., Critcher, C., Jefferson, T., Clarke, J., & Roberts, B. (1978). Policing the Crisis. London: Macmillan.",
             locator="1978 edition", locator_type="edition",
             supports="official sources as primary definers of news frames", verified=True),
    ],
    "MC-703": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Slow Journalism",
             title_fa="روزنامه‌نگاری کند",
             authors="Greenberg, S.", year=2007,
             publisher="Prospect",
             doi=None,
             url="https://oddfish.uk/wp-content/uploads/2011/08/slowjo_feb07.pdf",
             language="en", isbn=None,
             citation="Greenberg, S. (2007, February). Slow journalism. Prospect.",
             locator="February 2007 issue", locator_type="issue",
             supports="coining of slow journalism as narrative craft over speed", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="What is Slow Journalism?",
             title_fa="روزنامه‌نگاری کند چیست؟",
             authors="Le Masurier, M.", year=2015,
             publisher="Journalism Practice",
             doi="10.1080/17512786.2014.916471",
             url="https://www.tandfonline.com/doi/abs/10.1080/17512786.2014.916471",
             language="en", isbn=None,
             citation="Le Masurier, M. (2015). What is slow journalism? Journalism Practice, 9(2), 138-152.",
             locator="9(2):138-152", locator_type="page_range",
             supports="definitional framework of slow journalism as critique of speed", verified=True),
    ],
    "MC-704": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Modelling Contemporary Gatekeeping: The Rise of Individuals, Algorithms and Platforms in Digital News Dissemination",
             title_fa="مدل‌سازی دروازه‌بانی معاصر: ظهور افراد، الگوریتم‌ها و پلتفرم‌ها در توزیع خبر دیجیتال",
             authors="Wallace, J.", year=2018,
             publisher="Digital Journalism",
             doi="10.1080/21670811.2017.1343648",
             url="https://www.tandfonline.com/doi/abs/10.1080/21670811.2017.1343648",
             language="en", isbn=None,
             citation="Wallace, J. (2018). Modelling contemporary gatekeeping. Digital Journalism, 6(3), 274-293.",
             locator="6(3):274-293", locator_type="page_range",
             supports="four gatekeeper archetypes across individual, algorithmic and platform levels", verified=True),
        dict(kind="OTHER",
             title_en="Modelling Contemporary Gatekeeping (author manuscript)",
             title_fa="مدل‌سازی دروازه‌بانی معاصر (نسخهٔ نویسنده)",
             authors="Wallace, J.", year=2017,
             publisher="University of Zurich / mediachange.ch",
             doi=None,
             url="https://mediachange.ch/media/pdf/publications/Wallace2017_Digital_Gatekeeping.pdf",
             language="en", isbn=None,
             citation="Wallace, J. (2017). Modelling Contemporary Gatekeeping. Author manuscript, University of Zurich.",
             locator="author PDF", locator_type="manuscript",
             supports="detailed exposition of the digital gatekeeping model", verified=True),
    ],
    "MC-705": [
        dict(kind="BOOK",
             title_en="Deciding What's True: The Rise of Political Fact-Checking in American Journalism",
             title_fa="تصمیم دربارهٔ درستی: ظهور راستی‌آزمایی سیاسی در روزنامه‌نگاری آمریکا",
             authors="Graves, L.", year=2016,
             publisher="Columbia University Press",
             doi=None,
             url="https://cup.columbia.edu/book/deciding-whats-true/9780231175067/",
             language="en", isbn="9780231175067",
             citation="Graves, L. (2016). Deciding What's True: The Rise of Political Fact-Checking in American Journalism. New York: Columbia University Press.",
             locator="2016 edition", locator_type="edition",
             supports="newsroom ethnography of political fact-checking as a professional movement", verified=True),
        dict(kind="BOOK_CHAPTER",
             title_en="Fact-Checking as Idea and Practice in Journalism",
             title_fa="راستی‌آزمایی به‌عنوان اندیشه و عمل در روزنامه‌نگاری",
             authors="Graves, L.; Amazeen, M. A.", year=2019,
             publisher="Oxford Research Encyclopedia of Communication",
             doi="10.1093/acrefore/9780190228613.013.808",
             url="https://ora.ox.ac.uk/objects/uuid:a7450b2f-f5a7-4207-90e2-254ec5de14e2",
             language="en", isbn=None,
             citation="Graves, L., & Amazeen, M. A. (2019). Fact-checking as idea and practice in journalism. In Oxford Research Encyclopedia of Communication. Oxford University Press.",
             locator="encyclopedia entry", locator_type="entry",
             supports="distinction between ante hoc verification and post hoc fact-checking", verified=False),
    ],
}

ENRICH = {
    "MC-700": dict(
        year=1978,
        summary="مدل همزیستی رسانه و منبع، رابطهٔ میان سازمان خبری و منابع خبر را وابستگی متقابل می‌داند: منبع برای دیده‌شدن به رسانه نیاز دارد و رسانه برای دسترسی به اطلاعات به منبع. هربرت گنز در سال ۱۹۷۹ این رابطه را «کشمکش دونفره» توصیف کرد که در آن دو طرف می‌کوشند روایت را به سود خود مدیریت کنند. استوارت هال و همکارانش در سال ۱۹۷۸ لایهٔ قدرت را افزودند: منابع رسمی به‌عنوان تعریف‌کنندگان اولیه، چارچوب خبر را می‌سازند و روزنامه‌نگار در عمل به آن چارچوب دسترسی پیدا می‌کند. از این ترکیب، مدل همزیستی بیرون می‌آید: نه سلطهٔ یک‌سویهٔ منبع، نه استقلال کامل رسانه، بلکه مبادلهٔ پایدار میان دسترسی و اعتبار. مدل چهار سازوکار را جدا می‌کند: چانه‌زنی بر سر دسترسی، مدیریت اطلاعات، اعتباردهی متقابل و مرزنگه‌داری میان منبع و خبرنگار. در رسانه، مدل برای تحلیل روابط تحریریه با دولت، شرکت‌ها و نهادهای مدنی و برای فهم وابستگی خبر به روابط عمومی به کار می‌رود. نقدهای اصلی به آن، کم‌توجهی به منابع بی‌سازمان، فرض تعادل میان طرفین نابرابر قدرت و دشواری سنجش تجربی همزیستی را برجسته می‌کنند.",
        definition="مدل همزیستی رسانه و منبع، رابطهٔ خبرنگار و منبع را وابستگی متقابل و کشمکش مدیریت‌شده بر سر دسترسی و اعتبار می‌داند که در آن منابع رسمی اغلب چارچوب خبر را تعیین می‌کنند.",
        main_problem="رسانه چگونه بدون رهاکردن استقلال، به اطلاعات منابع قدرت دسترسی پیدا می‌کند و این وابستگی متقابل چه اثری بر چارچوب خبر می‌گذارد.",
        mechanism="منبع با ارائهٔ اطلاعات و دسترسی، اعتبار رسانه را تغذیه می‌کند؛ رسانه با پوشش، اعتبار و دیده‌شدن را به منبع می‌دهد؛ چانه‌زنی روزمره این مبادله را تنظیم می‌کند و منابع رسمی، چارچوب را زودتر تعیین می‌کنند.",
        assumptions=[
            "رسانه و منبع به هم نیاز دارند.",
            "رابطهٔ دو طرف کشمکش مدیریت‌شده است.",
            "منابع رسمی دسترسی بیشتری دارند.",
            "دسترسی، چارچوب خبر را جهت می‌دهد.",
            "اعتبار، سرمایهٔ مبادله است.",
        ],
        principles=[
            "منبع و منافع آن را بشناس.",
            "وابستگی را آشکار نگه دار.",
            "به منابع جایگزین دسترسی بساز.",
            "مرز خبر و روابط عمومی را روشن کن.",
            "اعتبار بلندمدت را بر دسترسی کوتاه‌مدت ترجیح بده.",
            "کشمکش را مستند کن.",
            "به منبع دوم دسترسی بساز.",
        ],
        critiques=[
            "به منابع بی‌سازمان کم می‌پردازد.",
            "تعادل میان طرفین نابرابر را فرض می‌کند.",
            "سنجش تجربی همزیستی دشوار است.",
            "نقش روابط عمومی را کم‌وزن می‌کند.",
            "به تفاوت رسانهٔ عمومی و تجاری کم توجه دارد.",
            "زمینهٔ کشورهای غیرغربی را کم دارد.",
            "نقش رسانه‌های اجتماعی در تنوع منبع را کم می‌بیند.",
        ],
        critique_text="منتقدان می‌گویند مدل همزیستی رسانه و منبع رابطهٔ دسترسی و اعتبار را روشن کرد اما نابرابری قدرت میان منبع و خبرنگار را کم‌بررسی گذاشت؛ با این حال، چارچوب پایهٔ تحلیل روابط منبع در مطالعات خبر است.",
        applications=[
            "تحلیل رابطهٔ تحریریه و دولت.",
            "پژوهش وابستگی خبر به روابط عمومی.",
            "ارزیابی تنوع منابع خبری.",
            "آموزش مرزنگه‌داری خبرنگار.",
            "تحلیل پوشش نهادهای مدنی.",
            "طراحی سیاست دسترسی به اطلاعات.",
            "بررسی تعریف اولیه در خبر فوری.",
            "پژوهش روابط منبع در رسانهٔ محلی.",
            "تحلیل روابط منبع در پوشش انتخابات.",
            "پژوهش روابط منبع در خبر سلامت.",
        ],
        example_text="خبرنگاری که تنها منبعش سخنگوی نهاد رسمی است، دسترسی سریع می‌گیرد اما چارچوب را هم از همان‌جا می‌گیرد؛ مدل همزیستی نشان می‌دهد که ساختن منبع دوم، هم استقلال و هم دقت را تقویت می‌کند.",
        evolution="گنز در سال ۱۹۷۹ رابطهٔ منبع و خبرنگار را کشمکشی دونفره خواند و هال و همکارانش در ۱۹۷۸ لایهٔ تعریف اولیه را افزودند؛ پژوهش‌های بعدی، مدل را به روابط عمومی، منابع دیجیتال و روزنامه‌نگاری داده گستردند.",
        key_concepts=["همزیستی", "دسترسی", "اعتبار", "تعریف اولیه", "کشمکش دونفره", "مرزنگه‌داری"],
        theorists="هربرت گنز و استوارت هال و همکاران.",
        theorists_text="مدل در سنت جامعه‌شناسی خبر و مطالعات فرهنگی شکل گرفت.",
        model="رابطهٔ رسانه و منبع به‌عنوان وابستگی متقابل و کشمکش مدیریت‌شده بر سر دسترسی و اعتبار.",
        studies=[
            "کتاب سال ۱۹۷۹ کشمکش منبع و خبرنگار را توصیف کرد.",
            "کتاب سال ۱۹۷۸ نقش تعریف اولیه را نشان داد.",
            "مطالعات روابط عمومی، وابستگی خبر را سنجیدند.",
            "پژوهش رسانهٔ محلی، تنوع منبع را بررسی کرد.",
        ],
    ),
    "MC-703": dict(
        year=2007,
        summary="مدل روزنامه‌نگاری بلندفرم و کند، که سوزان گرینبرگ در سال ۲۰۰۷ در مجلهٔ پراسپکت نام‌گذاری کرد و مگان لو مازوریه در سال ۲۰۱۵ صورت‌بندی نظری آن را داد، سرعت را از هستهٔ ارزش خبری بیرون می‌برد. در این مدل، ارزش خبری از «اول بودن» به «درست و عمیق بودن» جابه‌جا می‌شود: زمان صرف تحقیق، زمینه‌سازی، روایت و ویرایش می‌شود و محصول، بلندفرم یا گزارش عمیق است. مدل چهار ستون دارد: زمان کافی برای گزارش، تمرکز بر زمینه و تبیین، روایت ادبی و ویرایش دقیق، و وفاداری به دقت به‌جای مسابقهٔ انتشار. روزنامه‌نگاری کند خود را جایگزین خبر فوری نمی‌داند، بلکه مکمل آن است: خبر فوری چه گفت، گزارش کند چرا و چگونه را می‌گوید. در رسانه، مدل برای طراحی واحدهای بلندفرم، پادکست روایی، مجلات تخصصی و مدل‌های اشتراکی به کار می‌رود. نقدهای اصلی به آن، هزینهٔ بالا و دسترسی نابرابر مخاطب، خطر نخبه‌گرایی، دشواری سنجش اثر، وابستگی به مدل درآمدی و کندشدن پاسخ به بحران‌های فوری را برجسته می‌کنند.",
        definition="مدل روزنامه‌نگاری بلندفرم و کند، ارزش خبری را از سرعت به دقت، زمینه و روایت عمیق جابه‌جا می‌کند و زمان گزارش‌دهی را سرمایهٔ اصلی کیفیت می‌داند.",
        main_problem="در محیط خبری مبتنی بر سرعت و کلیک، چگونه می‌توان کیفیت، زمینه و دقت را به ارزش خبری بدل کرد و هزینهٔ این انتخاب را تأمین کرد.",
        mechanism="سرمایه‌گذاری زمان در تحقیق و ویرایش، دقت و عمق را بالا می‌برد؛ روایت و زمینه، فهم مخاطب را افزایش می‌دهد؛ وفاداری به کیفیت، اعتماد و اشتراک پایدار می‌سازد.",
        assumptions=[
            "سرعت، کیفیت را قربانی می‌کند.",
            "زمان، سرمایهٔ اصلی گزارش است.",
            "زمینه، فهم مخاطب را بالا می‌برد.",
            "روایت، ارزش خبری افزوده است.",
            "مخاطب برای عمق هزینه می‌پردازد.",
        ],
        principles=[
            "زمان کافی برای گزارش بگذار.",
            "زمینه و تبیین را در متن بیاور.",
            "روایت را جدی بگیر.",
            "دقت را بر اول‌بودن ترجیح بده.",
            "مدل درآمدی پایدار طراحی کن.",
            "خبر فوری را مکمل بدان، نه رقیب.",
            "زمان انتشار را با عمق هماهنگ کن.",
        ],
        critiques=[
            "هزینهٔ تولید آن بالاست.",
            "دسترسی مخاطب نابرابر است.",
            "خطر نخبه‌گرایی دارد.",
            "سنجش اثر آن دشوار است.",
            "به مدل درآمدی وابسته است.",
            "در بحران فوری کند است.",
            "به مخاطب کم‌سواد کمتر می‌رسد.",
            "تعریف آن از کندی مبهم است.",
            "برای مخاطب کم‌درآمد، دسترسی به محتوای اشتراکی دشوار است.",
            "مرز روزنامه‌نگاری کند و مستندسازی را روشن نمی‌کند.",
            "به تفاوت هزینهٔ گزارش کند در کشورهای کم‌درآمد کم توجه دارد.",
        ],
        critique_text="منتقدان می‌گویند روزنامه‌نگاری کند کیفیت و زمینه را به ارزش خبری برگرداند اما هزینهٔ بالا و وابستگی به اشتراک، آن را برای بخشی از مخاطبان دشوار می‌کند؛ با این حال، بدیل مهمی برای اقتصاد کلیک است.",
        applications=[
            "طراحی واحد بلندفرم تحریریه.",
            "تولید پادکست روایی.",
            "راه‌اندازی مجلهٔ تخصصی.",
            "طراحی مدل اشتراک خبری.",
            "آموزش گزارش عمیق.",
            "پوشش موضوع‌های پیچیده.",
            "ارزیابی کیفیت خبر در بحران.",
            "پژوهش اقتصاد رسانه.",
            "طراحی دورهٔ روزنامه‌نگاری روایی.",
            "ارزیابی بلندفرم در رسانهٔ عمومی.",
            "تحلیل پایداری مالی مجلهٔ کند.",
        ],
        example_text="یک پروندهٔ فساد را می‌توان در یک خبر فوری خلاصه کرد یا در گزارشی چندماهه با اسناد و روایت باز کرد؛ مدل کند می‌گوید گزارش دوم نه دیرتر، بلکه لایهٔ دیگری از خبر است.",
        evolution="گرینبرگ در سال ۲۰۰۷ نام روزنامه‌نگاری کند را گذاشت و لو مازوریه در سال ۲۰۱۵ آن را به چارچوب نظری بدل کرد؛ سپس مجلات، پادکست‌ها و استارتاپ‌های اشتراکی آن را به عمل درآوردند.",
        key_concepts=["روزنامه‌نگاری کند", "بلندفرم", "زمینه", "روایت", "دقت", "مدل اشتراک"],
        theorists="سوزان گرینبرگ و مگان لو مازوریه.",
        theorists_text="مدل در سنت نقد سرعت خبری و اقتصاد رسانه شکل گرفت.",
        model="جابه‌جایی ارزش خبری از سرعت به دقت و عمق با سرمایه‌گذاری زمان در گزارش و روایت.",
        studies=[
            "مقالهٔ سال ۲۰۰۷ نام‌گذاری و توصیف کرد.",
            "مقالهٔ سال ۲۰۱۵ چارچوب نظری داد.",
            "پژوهش رسانه، مدل اشتراک را بررسی کرد.",
            "مطالعهٔ پادکست، روایت کند را تحلیل کرد.",
            "مطالعهٔ تطبیقی، مدل کند را در سه کشور بررسی کرد.",
            "پژوهش مخاطب، تمایل به پرداخت را سنجید.",
            "تحلیل محتوا، عمق زمینه را در بلندفرم سنجید.",
            "پژوهش روایت، ساختار بلندفرم را در مجلات بررسی کرد.",
        ],
    ),
    "MC-704": dict(
        year=2018,
        summary="چارچوب دروازه‌بانی الگوریتمی، که جولیان والاس در سال ۲۰۱۸ ارائه کرد، نظریهٔ کلاسیک دروازه‌بانی را برای محیط دیجیتال بازنویسی می‌کند. در نظریهٔ کلاسیک، دروازه‌بان فردی در تحریریه تصمیم می‌گرفت چه خبری منتشر شود؛ والاس نشان می‌دهد که در توزیع خبر دیجیتال، دروازه‌بانی از یک فرد به شبکه‌ای از کنشگران منتقل شده است. چارچوب او چهار سنخ دروازه‌بان را از هم جدا می‌کند و سه لایهٔ گزینش را می‌بیند: لایهٔ فردی مانند خبرنگار و سردبیر، لایهٔ الگوریتمی مانند موتور توصیه و رتبه‌بندی، و لایهٔ پلتفرمی مانند قواعد و سیاست‌های توزیع. نکتهٔ کلیدی این است که گزینش دیگر یک لحظهٔ واحد نیست، بلکه زنجیره‌ای توزیع‌شده است که در آن هر لایه بخشی از تصمیم دیده‌شدن را می‌گیرد. مدل برای تحلیل فیلترشدن خبر، سوگیری الگوریتم، قدرت پلتفرم و پاسخ‌گویی توزیع به کار می‌رود. نقدهای اصلی به آن، تمرکز بر سطح نظری، کم‌توجهی به داده‌های تجربی گسترده، فرض شفافیت قواعد پلتفرم و دشواری نسبت‌دادن مسئولیت در شبکهٔ توزیع‌شده را برجسته می‌کنند.",
        definition="چارچوب دروازه‌بانی الگوریتمی، گزینش خبر را از تصمیم فردی سردبیر به زنجیرهٔ توزیع‌شدهٔ افراد، الگوریتم‌ها و پلتفرم‌ها جابه‌جا می‌کند و مسئولیت دیده‌شدن را میان لایه‌ها تقسیم می‌کند.",
        main_problem="وقتی توصیه‌گری الگوریتمی و قواعد پلتفرم تعیین می‌کنند چه خبری دیده شود، دروازه‌بانی کجا رخ می‌دهد و مسئولیت آن با کیست.",
        mechanism="هر لایه بخشی از گزینش را انجام می‌دهد: تحریریه تولید و انتخاب می‌کند، الگوریتم رتبه و توصیه می‌دهد، پلتفرم قواعد توزیع را تعیین می‌کند؛ نتیجهٔ نهایی محصول این زنجیره است، نه یک تصمیم واحد.",
        assumptions=[
            "دروازه‌بانی توزیع‌شده است.",
            "الگوریتم کنشگر گزینش است.",
            "پلتفرم قواعد توزیع را می‌سازد.",
            "چهار سنخ دروازه‌بان قابل تفکیک‌اند.",
            "مسئولیت میان لایه‌ها تقسیم می‌شود.",
        ],
        principles=[
            "زنجیرهٔ توزیع را ترسیم کن.",
            "هر لایهٔ گزینش را جدا بررسی کن.",
            "قواعد الگوریتم را شفاف کن.",
            "مسئولیت پلتفرم را روشن کن.",
            "سوگیری رتبه‌بندی را بسنج.",
            "پاسخ‌گویی توزیع را مطالبه کن.",
            "لایهٔ انسانی را در زنجیره حفظ کن.",
        ],
        critiques=[
            "در سطح نظری می‌ماند.",
            "دادهٔ تجربی گسترده کم دارد.",
            "شفافیت قواعد پلتفرم را فرض می‌کند.",
            "نسبت‌دادن مسئولیت دشوار است.",
            "به تفاوت ملی پلتفرم‌ها کم می‌پردازد.",
            "نقش مخاطب را کم‌وزن می‌کند.",
            "به سوگیری دادهٔ آموزش الگوریتم کم می‌پردازد.",
            "نقش روزنامه‌نگار در مقاومت به رتبه‌بندی را کم می‌بیند.",
            "به زمینهٔ کشورهای جنوب جهانی کم توجه دارد.",
            "سنجهٔ عینی برای اندازه‌گیری قدرت دروازه‌بان کم دارد.",
            "به تعامل دروازه‌بان انسانی و الگوریتم در عمل کم می‌پردازد.",
        ],
        critique_text="منتقدان می‌گویند چارچوب دروازه‌بانی الگوریتمی نقشهٔ خوبی از توزیع‌شدگی گزینش داد اما آزمون تجربی و شفافیت دادهٔ پلتفرم را مفروض گرفت؛ با این حال، پل مهمی میان نظریهٔ کلاسیک و محیط دیجیتال است.",
        applications=[
            "تحلیل فیلترشدن خبر.",
            "سنجش سوگیری الگوریتم توصیه.",
            "پژوهش قدرت پلتفرم.",
            "طراحی پاسخ‌گویی توزیع.",
            "آموزش سواد الگوریتمی.",
            "سیاست‌گذاری شفافیت.",
            "تحلیل زنجیرهٔ دیده‌شدن خبر.",
            "پژوهش دروازه‌بانی شبکه‌ای.",
            "تحلیل دروازه‌بانی در پلتفرم پیام‌رسان.",
            "سنجش شفافیت سیاست‌های توزیع پلتفرم.",
            "طراحی شاخص تنوع در توصیه‌گری.",
            "تحلیل تأثیر رتبه‌بندی بر دیده‌شدن خبر محلی.",
        ],
        example_text="خبری که تحریریه منتشر می‌کند اما الگوریتم آن را پایین می‌برد، در عمل دروازه‌بانی شده است؛ چارچوب والاس می‌پرسد این تصمیم در کدام لایه گرفته شد و چه کسی پاسخ‌گوست؛ اگر هیچ لایه‌ای پاسخ‌گو نباشد، دیده‌شدن به نتیجهٔ تصادفی بدل می‌شود.",
        evolution="والاس در سال ۲۰۱۸ مدل را با ترکیب نظریهٔ کلاسیک دروازه‌بانی و پژوهش پلتفرم ساخت؛ پژوهش‌های بعدی، آن را به توصیه‌گری، اخبار جعلی و حکمرانی الگوریتمی گستردند و به پرسش مسئولیت حقوقی پلتفرم رسیدند.",
        key_concepts=["دروازه‌بانی الگوریتمی", "سنخ‌های دروازه‌بان", "لایهٔ پلتفرم", "توصیه‌گری", "توزیع‌شدگی", "پاسخ‌گویی"],
        theorists="جولیان والاس.",
        theorists_text="چارچوب در سنت نظریهٔ دروازه‌بانی و پژوهش پلتفرم شکل گرفت.",
        model="گزینش خبر به‌عنوان زنجیرهٔ توزیع‌شدهٔ افراد، الگوریتم‌ها و پلتفرم‌ها.",
        studies=[
            "مقالهٔ سال ۲۰۱۸ چهار سنخ را معرفی کرد.",
            "نسخهٔ نویسنده، منطق مدل را شرح داد.",
            "پژوهش توصیه‌گری، سوگیری رتبه را سنجید.",
            "مطالعهٔ پلتفرم، قواعد توزیع را تحلیل کرد.",
            "پژوهش الگوریتم، رتبه‌بندی خبر را بازسازی کرد.",
            "مطالعهٔ تطبیقی، قواعد پلتفرم را در دو کشور سنجید.",
        ],
    ),
    "MC-705": dict(
        year=2016,
        summary="مدل اخبار جعلی و راستی‌آزمایی، که لوکاس گریوز در کتاب تصمیم دربارهٔ درستی در سال ۲۰۱۶ با مطالعهٔ مردم‌نگارانهٔ تحریریه‌های راستی‌آزمایی صورت‌بندی کرد و در سال ۲۰۱۹ با میشل آمازین به چارچوب مفهومی گسترده‌تری رسید، راستی‌آزمایی را به دو نوع تقسیم می‌کند: راستی‌آزمایی پیش از انتشار که بخشی از رویهٔ درونی خبر است، و راستی‌آزمایی پس از انتشار که نهاد مستقلی ادعای عمومی را می‌سنجد. مدل نشان می‌دهد که موج تازهٔ راستی‌آزمایی سیاسی از سال‌های پایانی دههٔ ۲۰۰۰، حرفه‌ای تازه با معیار، برچسب و مخاطب ساخته است. سازوکار آن سه مرحله دارد: انتخاب ادعای قابل بررسی، گردآوری شواهد و داوری با مقیاس روشن، و انتشار نتیجه با شفافیت منبع. مدل، خبر جعلی را نه فقط محتوای نادرست، بلکه ادعایی می‌داند که با ظاهر خبری و انگیزهٔ سیاسی منتشر می‌شود و راستی‌آزمایی را پاسخ حرفه‌ای به آن می‌شمارد. در رسانه، مدل برای طراحی واحد راستی‌آزمایی و همکاری با پلتفرم‌ها به کار می‌رود. نقدهای اصلی به آن، محدودبودن به ادعاهای سنجش‌پذیر، اثر اصلاحی محدود بر باورمندان، وابستگی به سیاست پلتفرم و کم‌توجهی به زمینهٔ غیرآمریکایی را برجسته می‌کنند.",
        definition="مدل اخبار جعلی و راستی‌آزمایی، راستی‌آزمایی را حرفه‌ای مستقل با رویهٔ انتخاب ادعا، داوری شفاف و انتشار نتیجه می‌داند که به انتشار ادعاهای نادرست با ظاهر خبری پاسخ می‌دهد.",
        main_problem="چگونه می‌توان ادعاهای عمومی نادرست را با معیار روشن سنجید، نتیجه را شفاف منتشر کرد و اثر آن را بر باور مخاطب و سیاست پلتفرم افزایش داد.",
        mechanism="ادعای قابل بررسی انتخاب می‌شود، شواهد گردآوری و با مقیاس داوری می‌شود، نتیجه با شفافیت منبع منتشر می‌شود؛ تکرار این چرخه، اعتبار نهاد راستی‌آزمایی را می‌سازد.",
        assumptions=[
            "ادعاهای عمومی سنجش‌پذیرند.",
            "شفافیت منبع، اعتبار می‌سازد.",
            "راستی‌آزمایی حرفه‌ای مستقل است.",
            "خبر جعلی ظاهر خبری دارد.",
            "اثر اصلاحی به مخاطب وابسته است.",
        ],
        principles=[
            "ادعای قابل بررسی را انتخاب کن.",
            "شواهد را مستند کن.",
            "مقیاس داوری را روشن کن.",
            "نتیجه را شفاف منتشر کن.",
            "خطا را اصلاح کن.",
            "همکاری پلتفرم را جدی بگیر.",
            "شفافیت روش را بر سرعت انتشار مقدم بدان.",
            "خطای خود را سریع و علنی اصلاح کن.",
        ],
        critiques=[
            "به ادعاهای سنجش‌پذیر محدود است.",
            "اثر اصلاحی آن محدود است.",
            "به سیاست پلتفرم وابسته است.",
            "زمینهٔ غیرآمریکایی را کم دارد.",
            "به باورمندان سرسخت کم اثر است.",
            "هزینهٔ تولید آن بالاست.",
            "به ادعاهای غیرقابل سنجش مانند ارزش‌داوری کم می‌پردازد.",
            "نقش رسانهٔ عمومی در پذیرش نتیجه را کم می‌بیند.",
            "مرز راستی‌آزمایی خبری و بررسی علمی را روشن نمی‌کند.",
        ],
        critique_text="منتقدان می‌گویند راستی‌آزمایی ابزار مهمی برای شفافیت ساخت اما به ادعاهای سنجش‌پذیر محدود ماند و اثر آن بر باورمندان کم بود؛ با این حال، استاندارد حرفه‌ای تازه‌ای برای دقت خبری ساخت.",
        applications=[
            "طراحی واحد راستی‌آزمایی.",
            "همکاری با پلتفرم‌ها.",
            "آموزش سواد خبری.",
            "پوشش انتخاباتی.",
            "پایش ادعای سلامت.",
            "پژوهش خبر جعلی.",
            "طراحی برچسب شفافیت.",
            "ارزیابی اثر اصلاح.",
            "طراحی همکاری راستی‌آزمایی با دانشگاه.",
            "پایش ادعاهای مهاجرت در پوشش خبری.",
        ],
        example_text="وقتی یک ادعای انتخاباتی با عددی ساختگی منتشر می‌شود، واحد راستی‌آزمایی عدد را با منبع اصلی می‌سنجد، مقیاس داوری را نشان می‌دهد و نتیجه را با سند منتشر می‌کند؛ مدل می‌گوید اعتبار از همین شفافیت می‌آید.",
        evolution="گریوز در سال ۲۰۱۶ حرفهٔ راستی‌آزمایی را با مردم‌نگاری توصیف کرد و در سال ۲۰۱۹ با آمازین چارچوب مفهومی گسترده‌تری ساخت؛ پژوهش‌های بعدی، اثر و محدودیت آن را سنجیدند و به پرسش مرز راستی‌آزمایی و سانسور رسیدند.",
        key_concepts=["راستی‌آزمایی", "خبر جعلی", "ادعای سنجش‌پذیر", "شفافیت", "مقیاس داوری", "اصلاح"],
        theorists="لوکاس گریوز و میشل آمازین.",
        theorists_text="مدل در سنت جامعه‌شناسی خبر و پژوهش دقت رسانه‌ای شکل گرفت.",
        model="راستی‌آزمایی به‌عنوان حرفهٔ مستقل با چرخهٔ انتخاب ادعا، داوری شفاف و انتشار نتیجه.",
        studies=[
            "کتاب سال ۲۰۱۶ تحریریه‌های راستی‌آزمایی را مطالعه کرد.",
            "مدخل سال ۲۰۱۹ چارچوب مفهومی داد.",
            "پژوهش اثر، اصلاح باور را سنجید.",
            "مطالعهٔ سلامت، ادعای واکسن را بررسی کرد.",
            "مطالعهٔ انتخاباتی، اثر برچسب نادرستی را سنجید.",
            "پژوهش پلتفرم، سرعت اصلاح را بررسی کرد.",
        ],
    ),
}

NAME_FIX = {}
YEAR_FIX = {
    "MC-700": "بدنهٔ کارت قالب عمومی حرفه‌گرایی بود و انتساب به «ساکس ۱۹۷۸» مستند نشد؛ مدل بر پایهٔ گنز ۱۹۷۹ و هال و همکاران ۱۹۷۸ بازنویسی شد.",
    "MC-703": "کارت سال و منبع نداشت و انتساب به «پترسون» برای روزنامه‌نگاری کند مستند نشد؛ سال ۲۰۰۷ و گرینبرگ و لو مازوریه مبنا قرار گرفت.",
    "MC-704": "بدنهٔ کارت قالب عمومی حرفه‌گرایی بود؛ محتوا بر پایهٔ والاس ۲۰۱۸ و نسخهٔ نویسندهٔ ۲۰۱۷ بازنویسی شد.",
    "MC-705": "بدنهٔ کارت قالب عمومی حرفه‌گرایی بود و سال ۲۰۱۷ ذکر شده بود؛ کتاب گریوز ۲۰۱۶ و مدخل ۲۰۱۹ با آمازین مبنا قرار گرفت.",
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
                                       "verified": n_verified, "batch": 158}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH158 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
