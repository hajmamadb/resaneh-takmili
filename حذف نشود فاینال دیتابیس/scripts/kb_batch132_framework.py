# -*- coding: utf-8 -*-
"""Batch 132 (MODEL): full documentation for MC-107, MC-108, MC-119, MC-121."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch132-model-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch132_model.json"

S = {
    "MC-107": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Limited Capacity Model of Mediated Message Processing",
             title_fa="مدل ظرفیت محدود پردازش پیام‌های رسانه‌ای",
             authors="Lang, A.", year=2000,
             publisher="Journal of Communication",
             doi="10.1111/j.1460-2466.2000.tb02833.x",
             url="https://academic.oup.com/joc/article-abstract/50/1/46/4110103",
             language="en", isbn=None,
             citation="Lang, A. (2000). The limited capacity model of mediated message processing. Journal of Communication, 50(1), 46-70.",
             locator="50(1):46-70", locator_type="page_range",
             supports="encoding, storage and retrieval competing for limited cognitive resources", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Using the Limited Capacity Model of Motivated Mediated Message Processing to Design Effective Cancer Communication Messages",
             title_fa="کاربرد مدل ظرفیت محدود در طراحی پیام‌های مؤثر ارتباطات سرطان",
             authors="Lang, A.", year=2006,
             publisher="Journal of Communication",
             doi=None, url=None, language="en", isbn=None,
             citation="Lang, A. (2006). Using the limited capacity model of motivated mediated message processing to design effective cancer communication messages. Journal of Communication, 56(s1), S57-S80.",
             locator="56(s1):S57-S80", locator_type="page_range",
             supports="extended motivated version of the limited capacity model", verified=False),
    ],
    "MC-108": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Differential Susceptibility to Media Effects Model",
             title_fa="مدل حساسیت دیفرانسیلی به اثرهای رسانه",
             authors="Valkenburg, P. M.; Peter, J.", year=2013,
             publisher="Journal of Communication",
             doi="10.1111/jcom.12024",
             url="https://academic.oup.com/joc/article-abstract/63/2/221/4085964",
             language="en", isbn=None,
             citation="Valkenburg, P. M., & Peter, J. (2013). The differential susceptibility to media effects model. Journal of Communication, 63(2), 221-243.",
             locator="63(2):221-243", locator_type="page_range",
             supports="dispositional, developmental and social susceptibility to media effects", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Differential Susceptibility to Media Effects Model: A Review of Its Explanatory Power",
             title_fa="مروری بر توان تبیینی مدل حساسیت دیفرانسیلی به اثرهای رسانه",
             authors="Valkenburg, P. M.; Peter, J.", year=2013,
             publisher="Journal of Communication",
             doi=None, url=None, language="en", isbn=None,
             citation="Valkenburg, P. M., & Peter, J. (2013). The differential susceptibility to media effects model. Journal of Communication, 63(2), 221-243. [transactional extension discussed in later reviews]",
             locator="63(2)", locator_type="page_range",
             supports="transactional relation between media use and susceptibility", verified=False),
    ],
    "MC-119": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Algorithmic Imaginary: Exploring the Ordinary Affects of Facebook Algorithms",
             title_fa="تخیل الگوریتمی: کاوش عواطف روزمرهٔ الگوریتم‌های فیس‌بوک",
             authors="Bucher, T.", year=2017,
             publisher="Information, Communication & Society",
             doi="10.1080/1369118X.2016.1154086",
             url="https://www.tandfonline.com/doi/full/10.1080/1369118X.2016.1154086",
             language="en", isbn=None,
             citation="Bucher, T. (2017). The algorithmic imaginary: Exploring the ordinary affects of Facebook algorithms. Information, Communication & Society, 20(1), 30-44.",
             locator="20(1):30-44", locator_type="page_range",
             supports="users' imaginaries of algorithms shape ordinary affects and practices", verified=True),
        dict(kind="BOOK_CHAPTER",
             title_en="The Relevance of Algorithms",
             title_fa="اهمیت الگوریتم‌ها",
             authors="Gillespie, T.", year=2014,
             publisher="MIT Press (Media Technologies)",
             doi="10.7551/mitpress/9780262525374.003.0009",
             url="https://direct.mit.edu/books/edited-volume/3021/chapter/82555/The-Relevance-of-Algorithms",
             language="en", isbn=None,
             citation="Gillespie, T. (2014). The relevance of algorithms. In T. Gillespie, P. J. Boczkowski, & K. A. Foot (Eds.), Media Technologies: Essays on Communication, Materiality, and Society (pp. 167-193). Cambridge, MA: MIT Press.",
             locator="pp. 167-193", locator_type="page_range",
             supports="public relevance algorithms and the promise of objectivity", verified=True),
    ],
    "MC-121": [
        dict(kind="BOOK",
             title_en="Managing Public Relations",
             title_fa="مدیریت روابط عمومی",
             authors="Grunig, J. E.; Hunt, T.", year=1984,
             publisher="Holt, Rinehart and Winston",
             doi=None,
             url="https://archive.org/details/managingpublicre0000unse",
             language="en", isbn=None,
             citation="Grunig, J. E., & Hunt, T. (1984). Managing Public Relations. New York: Holt, Rinehart and Winston.",
             locator="book", locator_type="SECTION",
             supports="four models of public relations", verified=True),
        dict(kind="BOOK",
             title_en="Excellence in Public Relations and Communication Management",
             title_fa="تعالی در روابط عمومی و مدیریت ارتباطات",
             authors="Grunig, J. E. (ed.)", year=1992,
             publisher="Lawrence Erlbaum Associates",
             doi=None, url=None, language="en", isbn=None,
             citation="Grunig, J. E. (Ed.). (1992). Excellence in Public Relations and Communication Management. Hillsdale, NJ: Lawrence Erlbaum Associates.",
             locator="book", locator_type="SECTION",
             supports="normative development of the two-way symmetrical model", verified=False),
    ],
}

ENRICH = {
    "MC-107": dict(
        year=2000,
        summary="مدل ظرفیت محدود پردازش پیام‌های رسانه‌ای، مدلی در روان‌شناسی شناختی رسانه است که آنی لانگ در سال ۲۰۰۰ در مجلهٔ ارتباطات معرفی کرد. ادعای مرکزی این است که ظرفیت شناختی انسان محدود است و پردازش پیام رسانه‌ای سه زیرفرایند دارد: رمزگذاری، یعنی تبدیل محرک به بازنمایی ذهنی؛ ذخیره‌سازی، یعنی نگه‌داشتن آن بازنمایی در حافظهٔ کاری؛ و بازیابی، یعنی فراخوانی اطلاعات مرتبط از حافظه. این سه فرایند از یک مخزن مشترک منابع بهره می‌گیرند؛ اگر پیام بیش از حد منابع را مصرف کند، یادآوری و درک افت می‌کند. سیستم‌های انگیزشی رویکرد و اجتناب، تخصیص منابع را هدایت می‌کنند و محرک‌های نوظهور مانند تغییر ناگهانی تصویر یا صدا، پاسخ جهت‌گیری و تخصیص خودکار منابع را برمی‌انگیزند. نسخهٔ انگیزشی بعدی مدل، این چارچوب را برای طراحی پیام‌های سلامت و تبلیغات بسط داد. این مدل در پژوهش تلویزیون، تبلیغات، خبر و رسانهٔ دیجیتال کاربرد گسترده دارد. نقدهای اصلی به آن، دشواری سنجش مستقیم تخصیص منابع، تفاوت‌های فردی در ظرفیت و کم‌توجهی به فرایندهای تفسیری سطح بالا مربوط می‌شود.",
        definition="مدل ظرفیت محدود، مدلی است که پردازش پیام رسانه‌ای را به سه فرایند رمزگذاری، ذخیره‌سازی و بازیابی تقسیم می‌کند که از منابع شناختی مشترک و محدود تغذیه می‌کنند و تخصیص این منابع را سیستم‌های انگیزشی هدایت می‌کنند.",
        main_problem="چرا در مواجهه با برخی پیام‌های رسانه‌ای، درک و یادآوری افت می‌کند، و چه عواملی تخصیص منابع شناختی محدود را تعیین می‌کند.",
        mechanism="پیام، تقاضای شناختی برای رمزگذاری، ذخیره و بازیابی ایجاد می‌کند؛ این تقاضاها از یک مخزن مشترک منابع تغذیه می‌شوند. محرک‌های نوظهور و انگیزشی، منابع را به خود جلب می‌کنند؛ اگر تقاضا از ظرفیت بیشتر شود، یکی از فرایندها با کمبود منابع روبه‌رو می‌شود و عملکرد یادآوری یا درک افت می‌کند.",
        assumptions=[
            "ظرفیت شناختی انسان محدود است.",
            "رمزگذاری، ذخیره و بازیابی از منابع مشترک استفاده می‌کنند.",
            "سیستم‌های انگیزشی رویکرد و اجتناب، تخصیص منابع را هدایت می‌کنند.",
            "محرک‌های نوظهور پاسخ جهت‌گیری و تخصیص خودکار ایجاد می‌کنند.",
            "بار شناختی بیش از ظرفیت، عملکرد پردازش را کاهش می‌دهد.",
        ],
        principles=[
            "پردازش پیام را باید در سه زیرفرایند تحلیل کرد.",
            "منابع شناختی مشترک و محدودند.",
            "طراحی پیام باید با ظرفیت پردازش مخاطب هم‌خوان باشد.",
            "محرک‌های برجسته، توجه و منابع را جلب می‌کنند.",
            "افزایش بار شناختی می‌تواند یادآوری را کاهش دهد.",
            "انگیزهٔ رویکرد و اجتناب، عمق پردازش را تغییر می‌دهد.",
        ],
        critiques=[
            "سنجش مستقیم تخصیص منابع دشوار است.",
            "تفاوت‌های فردی در ظرفیت کم‌بررسی می‌ماند.",
            "فرایندهای تفسیری سطح بالا کم‌رنگ می‌شوند.",
            "تعمیم نتایج آزمایشگاهی به محیط رسانه‌ای واقعی محدود است.",
            "مدل برای رسانهٔ تعاملی و چندوظیفه‌ای بازنگری می‌خواهد.",
        ],
        critique_text="منتقدان می‌گویند مدل ظرفیت محدود توضیحی روشن برای افت یادآوری در پیام‌های پرمحتوای رسانه‌ای فراهم کرد اما سنجش تجربی تخصیص منابع دشوار است و نقش تفسیر و انگیزه‌های بالاتر کم‌بررسی می‌ماند. با این حال، چارچوب مرجع پژوهش بار شناختی رسانه است.",
        applications=[
            "طراحی خبر تلویزیونی و پیام‌های بصری.",
            "تحلیل بار شناختی تبلیغات و ویدئوهای کوتاه.",
            "طراحی پیام سلامت با کنترل بار شناختی.",
            "پژوهش چندوظیفگی رسانه‌ای و توجه.",
            "آموزش سواد رسانه‌ای و طراحی رابط کاربری رسانه.",
        ],
        example_text="یک خبر تلویزیونی که هم‌زمان نوار خبری متحرک، تصویر پرتحرک و گفتار پرسرعت دارد، ممکن است توجه مخاطب را جلب کند اما منابع شناختی را چنان مصرف کند که یادآوری محتوای اصلی افت کند. مدل ظرفیت محدود این بده‌بستان شناختی را توضیح می‌دهد.",
        evolution="ریشهٔ مدل در پژوهش توجه و پردازش اطلاعات دههٔ ۱۹۸۰ و ۱۹۹۰ است. مقالهٔ سال ۲۰۰۰ نسخهٔ پایه را تثبیت کرد و نسخهٔ انگیزشی بعدی، سیستم‌های رویکرد و اجتناب را افزود و مدل را برای طراحی پیام سلامت به کار برد.",
        key_concepts=["رمزگذاری", "ذخیره‌سازی", "بازیابی", "منابع شناختی محدود", "بار شناختی", "پاسخ جهت‌گیری", "سیستم انگیزشی"],
        theorists="آنی لانگ، صورت‌بند مدل ظرفیت محدود.",
        theorists_text="این مدل در سنت روان‌شناسی شناختی رسانه شکل گرفت و با پژوهش توجه و بار شناختی پیوند خورد.",
        model="مدل سه‌فرایندی: رمزگذاری، ذخیره‌سازی و بازیابی از منابع مشترک؛ انگیزه و محرک نوظهور تخصیص منابع را هدایت می‌کنند و کمبود منابع، عملکرد پردازش را کاهش می‌دهد.",
        studies=[
            "مقالهٔ سال ۲۰۰۰ مدل را با پژوهش تلویزیون معرفی کرد.",
            "نسخهٔ انگیزشی، سیستم‌های رویکرد و اجتناب را افزود.",
            "پژوهش‌های تبلیغات، بار شناختی پیام را آزمودند.",
            "مطالعات رسانهٔ دیجیتال، مدل را برای محتوای تعاملی به کار بردند.",
        ],
    ),
    "MC-108": dict(
        year=2013,
        summary="مدل حساسیت دیفرانسیلی به اثرهای رسانه، مدلی یکپارچه در پژوهش اثر رسانه است که پتی والکنبورگ و یوخن پیتر در سال ۲۰۱۳ در مجلهٔ ارتباطات معرفی کردند. ادعای مرکزی این است که اثر رسانه بر همه یکسان نیست، زیرا افراد در سه نوع حساسیت با هم تفاوت دارند: حساسیت سرشتی، یعنی ویژگی‌های نسبتاً پایدار فردی مانند شخصیت و انگیزه؛ حساسیت رشدی، یعنی مرحلهٔ رشد شناختی و اجتماعی فرد، به‌ویژه در کودکی و نوجوانی؛ و حساسیت اجتماعی، یعنی بافت اجتماعی مانند خانواده، همسالان و فرهنگ. این حساسیت‌ها از سه مسیر بر اثر رسانه عمل می‌کنند: انتخاب محتوا، توجه به محتوای انتخاب‌شده، و پاسخ‌های شناختی، عاطفی و برانگیختگی به آن. مدل رابطهٔ دوسویه هم دارد: مصرف رسانه خود می‌تواند حساسیت فرد را تغییر دهد و چرخه‌ای تراکنشی بسازد. این مدل، چارچوبی برای پژوهش تفاوت‌های فردی در اثر رسانه، طراحی مداخله برای گروه‌های آسیب‌پذیر و تحلیل اثر رسانه بر نوجوانان فراهم کرد. نقدهای اصلی به آن، دشواری سنجش حساسیت، پیچیدگی عملیاتی و شمار محدود آزمون‌های تجربی مستقیم مربوط می‌شود.",
        definition="مدل حساسیت دیفرانسیلی، مدلی است که اثر رسانه را تابعی از سه نوع حساسیت سرشتی، رشدی و اجتماعی می‌داند که از مسیرهای انتخاب، توجه و پاسخ‌های شناختی و عاطفی بر اثر رسانه عمل می‌کنند و خود از مصرف رسانه تأثیر می‌پذیرند.",
        main_problem="چرا یک محتوای رسانه‌ای بر برخی افراد اثر قوی و بر برخی دیگر اثر ضعیف یا متفاوت دارد، و چه عواملی این تفاوت در حساسیت را توضیح می‌دهد.",
        mechanism="حساسیت سرشتی، رشدی و اجتماعی، انتخاب رسانه و توجه به آن را قالب می‌زنند؛ پاسخ‌های شناختی، عاطفی و برانگیختگی، مسیر نزدیک اثر رسانه‌اند. مصرف رسانه نیز به‌نوبهٔ خود حساسیت فرد را تغییر می‌دهد و رابطه را دوسویه می‌کند.",
        assumptions=[
            "اثر رسانه میان افراد متفاوت است.",
            "حساسیت سه نوع سرشتی، رشدی و اجتماعی دارد.",
            "انتخاب، توجه و پاسخ‌های درونی، مسیرهای واسط اثرند.",
            "مصرف رسانه می‌تواند حساسیت را تغییر دهد.",
            "رابطهٔ رسانه و مخاطب تراکنشی و دوسویه است.",
        ],
        principles=[
            "اثر رسانه را باید با تفاوت‌های فردی تحلیل کرد.",
            "حساسیت را باید در سه سطح سرشتی، رشدی و اجتماعی سنجید.",
            "انتخاب محتوا، حلقهٔ اول واسطه‌گری است.",
            "پاسخ شناختی، عاطفی و برانگیختگی، مسیر نزدیک اثرند.",
            "اثر رسانه می‌تواند حساسیت را بازتولید یا تغییر دهد.",
            "مداخله باید گروه‌های حساس‌تر را هدف بگیرد.",
        ],
        critiques=[
            "سنجش تجربی حساسیت دشوار و چندبعدی است.",
            "مدل پیچیده و عملیاتی‌سازی آن پرهزینه است.",
            "آزمون‌های تجربی مستقیم مدل محدودند.",
            "نقش محتوای رسانه در برابر ویژگی فرد کم‌رنگ می‌شود.",
            "تعمیم بین‌فرهنگی به بررسی بیشتر نیاز دارد.",
        ],
        critique_text="منتقدان می‌گویند مدل حساسیت دیفرانسیلی چارچوبی ارزشمند برای پایان‌دادن به فرض «اثر یکسان» فراهم کرد اما سنجش سه نوع حساسیت و مسیرهای واسط آن دشوار است و شواهد تجربی مستقیم کافی ندارد. با این حال، به چارچوب مرجع پژوهش تفاوت‌های فردی در اثر رسانه تبدیل شده است.",
        applications=[
            "پژوهش اثر رسانه بر کودکان و نوجوانان.",
            "طراحی مداخله برای گروه‌های آسیب‌پذیر.",
            "تحلیل اثر خشونت رسانه‌ای با توجه به تفاوت‌های فردی.",
            "پژوهش کمپین سلامت و تفاوت پاسخ مخاطبان.",
            "سیاست‌گذاری محتوای رسانه برای گروه‌های حساس.",
        ],
        example_text="یک برنامهٔ آموزشی سلامت ممکن است بر نوجوانی با بافت خانوادگی حمایتگر اثر قوی بگذارد و بر نوجوانی در محیط پرتنش اثر کمتری؛ مدل حساسیت دیفرانسیلی این تفاوت را به تفاوت در حساسیت رشدی و اجتماعی و مسیرهای انتخاب و پاسخ نسبت می‌دهد.",
        evolution="مدل در سنت پژوهش اثر رسانه و تفاوت‌های فردی شکل گرفت و در سال ۲۰۱۳ صورت‌بندی یکپارچه یافت. پژوهش‌های بعدی، آن را در سلامت، خشونت رسانه‌ای و رسانهٔ اجتماعی آزمودند و بر سنجش تجربی حساسیت تأکید کردند.",
        key_concepts=["حساسیت سرشتی", "حساسیت رشدی", "حساسیت اجتماعی", "انتخاب رسانه", "پاسخ شناختی", "رابطهٔ تراکنشی"],
        theorists="پتی والکنبورگ و یوخن پیتر، صورت‌بندانان مدل حساسیت دیفرانسیلی.",
        theorists_text="این مدل در سنت پژوهش اثر رسانه و روان‌شناسی رشد شکل گرفت و با تحلیل تفاوت‌های فردی پیوند خورد.",
        model="مدل سه‌حساسیتی: سرشتی، رشدی و اجتماعی؛ سه مسیر انتخاب، توجه و پاسخ درونی، اثر رسانه را واسطه‌گری می‌کنند و مصرف رسانه حساسیت را بازتولید یا تغییر می‌دهد.",
        studies=[
            "مقالهٔ سال ۲۰۱۳ مدل را با مرور شواهد صورت‌بندی کرد.",
            "پژوهش‌های نوجوانان، حساسیت رشدی را آزمودند.",
            "مطالعات خانواده و همسالان، حساسیت اجتماعی را بررسی کردند.",
            "پژوهش‌های مداخله، هدف‌گیری گروه‌های حساس را آزمودند.",
        ],
    ),
    "MC-119": dict(
        year=2017,
        summary="تخیل الگوریتمی، مفهومی در مطالعات رسانهٔ دیجیتال است که تاینا بوشر در مقالهٔ سال ۲۰۱۷ در مجلهٔ اطلاعات، ارتباطات و جامعه معرفی کرد. ادعای مرکزی این است که کاربران دربارهٔ نحوهٔ کار الگوریتم‌ها تصوراتی می‌سازند، حتی اگر این تصورات از نظر فنی دقیق نباشند، و بر پایهٔ همین تصورات رفتار می‌کنند. این «تخیل» تنها شناخت نیست؛ عواطف روزمره‌ای مانند کنجکاوی، اضطراب، خشم یا احساس ناتوانی را نیز در بر می‌گیرد و به عادت‌های استفاده، برداشت از فرهنگ عمومی پلتفرم و احساس قدرت یا بی‌قدرتی کاربر شکل می‌دهد. بوشر با مصاحبه با کاربران فیس‌بوک نشان داد که آنها الگوریتم را موجودی فعال تصور می‌کنند که «می‌بیند»، «قضاوت می‌کند» و «پاداش یا تنبیه می‌دهد» و در نتیجه رفتار خود را برای خوشایند آن تنظیم می‌کنند. این مفهوم، پژوهش «نظریه‌های عامیانه» دربارهٔ الگوریتم‌ها، شفافیت الگوریتمی و سواد الگوریتمی را پیش برد. نقدهای اصلی به آن، تکیه بر نمونهٔ کیفی محدود، تمرکز بر یک پلتفرم و خطر نسبت‌دادن آگاهی بیش از اندازه به کاربران مربوط می‌شود.",
        definition="تخیل الگوریتمی، مجموع تصورات، عواطف و انتظارات روزمره‌ای است که کاربران دربارهٔ نحوهٔ کار الگوریتم‌ها می‌سازند و بر پایهٔ آن رفتار و احساس خود را تنظیم می‌کنند.",
        main_problem="کاربران چگونه الگوریتم‌هایی را که نمی‌بینند و نمی‌فهمند تصور می‌کنند، و این تصورات چه اثری بر رفتار، عادت و احساس آنها دارد.",
        mechanism="کاربر از تجربهٔ روزمره، شایعات و نشانه‌های پراکنده، مدلی ذهنی از الگوریتم می‌سازد؛ این مدل با عواطف پیوند می‌خورد و به انتظاراتی دربارهٔ پاداش و تنبیه تبدیل می‌شود. کاربر رفتار خود را برای هم‌خوانی با تصور الگوریتم تنظیم می‌کند و این چرخه، عادت‌های استفاده را تثبیت می‌کند.",
        assumptions=[
            "کاربران دربارهٔ الگوریتم‌ها نظریهٔ عامیانه می‌سازند.",
            "این تصورات لازم نیست از نظر فنی درست باشند تا اثر بگذارند.",
            "تخیل الگوریتمی با عواطف روزمره پیوند دارد.",
            "تصورات کاربر، رفتار و عادت استفاده را تغییر می‌دهند.",
            "احساس قدرت یا ناتوانی کاربر از این تخیل شکل می‌گیرد.",
        ],
        principles=[
            "تجربهٔ کاربر از الگوریتم، به تصور و عاطفه وابسته است.",
            "نظریه‌های عامیانه کاربران، دادهٔ معتبر پژوهش‌اند.",
            "رفتار کاربر را باید با تخیل الگوریتمی او فهمید.",
            "شفافیت الگوریتمی بدون توجه به تخیل کاربر ناقص است.",
            "احساس عاملیت کاربر، بخشی از رابطهٔ او با الگوریتم است.",
            "پژوهش الگوریتم باید روش کیفی و تجربهٔ روزمره را جدی بگیرد.",
        ],
        critiques=[
            "بر نمونهٔ کیفی کوچک و یک پلتفرم تکیه دارد.",
            "خطر نسبت‌دادن آگاهی بیش از اندازه به کاربران را دارد.",
            "تعمیم به سایر پلتفرم‌ها و فرهنگ‌ها محدود است.",
            "مرز تخیل کاربر و تبلیغات پلتفرم روشن نیست.",
            "سنجش تجربی عواطف الگوریتمی دشوار است.",
        ],
        critique_text="منتقدان می‌گویند تخیل الگوریتمی مفهومی غنی برای فهم تجربهٔ روزمرهٔ کاربران فراهم کرد اما بر شواهد کیفی محدود تکیه دارد و ممکن است آگاهی کاربران از الگوریتم را بیش از واقع برآورد کند. با این حال، به یکی از مفاهیم کلیدی مطالعات الگوریتم و شفافیت تبدیل شده است.",
        applications=[
            "پژوهش تجربهٔ کاربر و نظریه‌های عامیانه دربارهٔ الگوریتم.",
            "طراحی سیاست شفافیت و توضیح‌پذیری الگوریتم.",
            "آموزش سواد الگوریتمی و رسانه‌ای.",
            "تحلیل رابطهٔ کاربر با پلتفرم‌های اجتماعی.",
            "مطالعهٔ احساس قدرت و ناتوانی در محیط دیجیتال.",
        ],
        example_text="کاربری که تصور می‌کند فیس‌بوک او را «فراموش کرده است»، شروع می‌کند به لایک‌کردن و کامنت‌گذاشتن بیشتر تا الگوریتم دوباره او را ببیند؛ این رفتار بر پایهٔ تصوری است که ممکن است از نظر فنی دقیق نباشد. مفهوم تخیل الگوریتمی همین چرخهٔ تصور و رفتار را توضیح می‌دهد.",
        evolution="مفهوم در بستر پژوهش انتقادی الگوریتم‌ها و نظریهٔ عامیانه در دههٔ ۲۰۱۰ شکل گرفت و مقالهٔ سال ۲۰۱۷ آن را تثبیت کرد. پژوهش‌های بعدی، آن را به شفافیت الگوریتمی، سواد الگوریتمی و پلتفرم‌های مختلف گستردند.",
        key_concepts=["تخیل الگوریتمی", "نظریهٔ عامیانه", "عواطف روزمره", "شفافیت الگوریتمی", "سواد الگوریتمی", "عاملیت کاربر"],
        theorists="تاینا بوشر، صورت‌بند مفهوم تخیل الگوریتمی.",
        theorists_text="این مفهوم در سنت مطالعات انتقادی الگوریتم و جامعه‌شناسی رسانهٔ دیجیتال شکل گرفت.",
        model="مدل چرخه‌ای: تجربه و نشانه‌های پراکنده، تخیل و عاطفه دربارهٔ الگوریتم می‌سازند؛ این تخیل، رفتار کاربر را قالب می‌زند و رفتار، تجربهٔ بعدی و تخیل را بازتولید می‌کند.",
        studies=[
            "مقالهٔ سال ۲۰۱۷ مصاحبه‌های کاربران فیس‌بوک را تحلیل کرد.",
            "پژوهش‌های نظریهٔ عامیانه، تخیل کاربران از الگوریتم را بررسی کردند.",
            "مطالعات شفافیت، نقش تصورات کاربر را در سیاست توضیح‌پذیری نشان دادند.",
            "پژوهش سواد الگوریتمی، مفهوم را به آموزش گسترد.",
        ],
    ),
    "MC-121": dict(
        year=1984,
        summary="مدل‌های چهارگانهٔ روابط عمومی، طبقه‌بندی کلاسیک الگوهای ارتباط سازمان با جمهور است که جیمز گرونیگ و تاد هانت در کتاب مدیریت روابط عمومی در سال ۱۹۸۴ معرفی کردند. ادعای مرکزی این است که روابط عمومی در چهار الگو عمل می‌کند: انتشاراتی، یعنی تبلیغ یک‌سویه با هدف جلب توجه و بدون الزام به دقت؛ اطلاع‌رسانی عمومی، یعنی انتشار یک‌سویهٔ اطلاعات صحیح اما بدون پژوهش دربارهٔ مخاطب؛ دوطرفهٔ نامتقارن، یعنی پژوهش دربارهٔ مخاطب برای طراحی پیام اقناعی و بدون تغییر سازمان؛ و دوطرفهٔ متقارن، یعنی ارتباط دوسویه با هدف فهم متقابل و تغییر هر دو طرف. گرونیگ این الگوها را روی پیوستاری از یک‌سویه تا دوسویه و از نامتقارن تا متقارن مرتب کرد و دوطرفهٔ متقارن را الگوی هنجاری مطلوب و پایهٔ نظریهٔ تعالی دانست. این مدل، چارچوب آموزش روابط عمومی، تحلیل عملکرد سازمان‌ها و پژوهش ارتباط سازمانی شد. نقدهای اصلی به آن، هنجاری‌بودن و آرمانی‌بودن الگوی متقارن، شواهد تجربی محدود برای برتری آن و کم‌توجهی به روابط قدرت و منافع نابرابر مربوط می‌شود.",
        definition="مدل‌های چهارگانهٔ روابط عمومی، طبقه‌بندی چهار الگوی ارتباط سازمان با جمهور، یعنی انتشاراتی، اطلاع‌رسانی عمومی، دوطرفهٔ نامتقارن و دوطرفهٔ متقارن، بر پایهٔ جهت ارتباط و توازن منافع است.",
        main_problem="سازمان‌ها چگونه با جمهور خود ارتباط برقرار می‌کنند، و کدام الگوی ارتباط می‌تواند فهم متقابل و اعتماد پایدار بسازد.",
        mechanism="در الگوهای یک‌سویه، سازمان پیام را به جمهور منتقل می‌کند و بازخورد ساختاری ندارد؛ در الگوی دوطرفهٔ نامتقارن، پژوهش مخاطب برای اقناع مؤثرتر به کار می‌رود اما هدف تغییر مخاطب است؛ در الگوی متقارن، بازخورد و مذاکره دوطرفه است و سازمان نیز ممکن است تغییر کند.",
        assumptions=[
            "روابط عمومی را می‌توان بر پایهٔ جهت و توازن ارتباط طبقه‌بندی کرد.",
            "جهت یک‌سویه و دوسویه، تفاوت کیفی ایجاد می‌کند.",
            "بازخورد ساختاری، شرط ارتباط متقارن است.",
            "فهم متقابل، هدف مطلوب ارتباط سازمانی است.",
            "الگوی متقارن با منافع بلندمدت سازمان هم‌خوان است.",
        ],
        principles=[
            "چهار الگو را باید بر پایهٔ جهت و توازن از هم تفکیک کرد.",
            "اطلاع‌رسانی عمومی از تبلیغ یک‌سویه متمایز است.",
            "پژوهش مخاطب، شرط الگوهای دوطرفه است.",
            "تقارن به معنای مذاکره و تغییر دوطرفه است.",
            "الگوی متقارن، آرمان هنجاری روابط عمومی است.",
            "انتخاب الگو، پیامد اخلاقی و اعتباری دارد.",
        ],
        critiques=[
            "الگوی متقارن آرمانی و هنجاری است.",
            "شواهد تجربی برتری آن یکدست نیست.",
            "روابط قدرت و منافع نابرابر کم‌بررسی می‌ماند.",
            "کاربرد الگو در بحران و محیط سیاسی دشوار است.",
            "طبقه‌بندی چهارگانه، تنوع عمل امروز را پوشش نمی‌دهد.",
            "نقش ارتباطات غیررسمی و شبکه‌های اجتماعی دیجیتال در مدل کم‌بررسی است.",
        ],
        critique_text="منتقدان می‌گویند مدل‌های چهارگانه چارچوبی روشن و آموزنده برای فهم تکامل روابط عمومی فراهم کردند اما الگوی متقارن بیش از اندازه آرمانی است و به روابط قدرت و محدودیت‌های عملی کم‌توجه می‌کند. با این حال، همچنان چارچوب پایهٔ آموزش و پژوهش روابط عمومی است.",
        applications=[
            "آموزش روابط عمومی و ارتباط سازمانی.",
            "تحلیل عملکرد ارتباطی سازمان‌ها.",
            "طراحی راهبرد ارتباط دوسویه با ذی‌نفعان.",
            "مدیریت بحران و اعتماد عمومی.",
            "پژوهش ارتباط سازمان و رسانه.",
            "تحلیل روابط عمومی دیجیتال و مدیریت شهرت برند.",
        ],
        example_text="سازمانی که در بحران تنها بیانیهٔ یک‌سویه منتشر می‌کند، در الگوی انتشاراتی یا اطلاع‌رسانی عمل می‌کند؛ سازمانی که نشست پرسش‌وپاسخ برگزار می‌کند و بر پایهٔ بازخورد، سیاست خود را اصلاح می‌کند، به الگوی دوطرفهٔ متقارن نزدیک‌تر است. مدل‌های چهارگانه این تفاوت را نشان می‌دهند.",
        evolution="کتاب سال ۱۹۸۴ چهار الگو را تثبیت کرد؛ پژوهش‌های بعدی گرونیگ و همکاران، نظریهٔ تعالی و الگوی متقارن را بسط دادند و در دههٔ ۱۹۹۰ نقدهای تجربی و مفهومی بر آن شکل گرفت. در دههٔ ۲۰۱۰، پژوهش روابط عمومی دیجیتال، مدل را برای تعامل در شبکه‌های اجتماعی بازخوانی کرد.",
        key_concepts=["انتشاراتی", "اطلاع‌رسانی عمومی", "دوطرفهٔ نامتقارن", "دوطرفهٔ متقارن", "تقارن", "نظریهٔ تعالی"],
        theorists="جیمز گرونیگ و تاد هانت، صورت‌بندانان مدل‌های چهارگانه.",
        theorists_text="این مدل در سنت پژوهش روابط عمومی و ارتباط سازمانی شکل گرفت و با نظریهٔ تعالی گرونیگ پیوند خورد.",
        model="مدل دوبُعدی: جهت ارتباط (یک‌سویه/دوسویه) در برابر توازن منافع (نامتقارن/متقارن)؛ چهار ترکیب، چهار الگوی روابط عمومی را می‌سازند.",
        studies=[
            "کتاب سال ۱۹۸۴ چهار الگو را معرفی کرد.",
            "پژوهش‌های نظریهٔ تعالی، الگوی متقارن را بسط دادند.",
            "مطالعات تجربی، کاربرد الگوها در سازمان‌ها را سنجیدند.",
            "نقدهای دههٔ ۱۹۹۰، محدودیت‌های هنجاری مدل را بررسی کردند.",
        ],
    ),
}

NAME_FIX = {}

YEAR_FIX = {}


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
                                       "verified": n_verified, "batch": 132}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH132 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
