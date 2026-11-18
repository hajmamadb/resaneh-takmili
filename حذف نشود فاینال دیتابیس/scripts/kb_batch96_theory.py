# -*- coding: utf-8 -*-
"""Batch 96: full documentation for MC-528, MC-529, MC-530, MC-532."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch96-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch96_theory.json"

S = {
    "MC-528": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Sousveillance: Inventing and Using Wearable Computing Devices for Data Collection in Surveillance Environments",
             title_fa="پادپایش: ابداع و کاربرد دستگاه‌های رایانش پوشیدنی برای گردآوری داده در محیط‌های نظارتی",
             authors="Mann, S.; Nolan, J.; Wellman, B.", year=2003,
             publisher="Surveillance & Society",
             doi=None,
             url="https://ojs.library.queensu.ca/index.php/surveillance-and-society/article/view/3344",
             language="en", isbn=None,
             citation="Mann, S., Nolan, J., & Wellman, B. (2003). Sousveillance: Inventing and using wearable computing devices for data collection in surveillance environments. Surveillance & Society, 1(3), 331-355.",
             locator="1(3):331-355", locator_type="page_range",
             supports="sousveillance / reflectionism / inverse panopticon / wearable recording", verified=True),
        dict(kind="BOOK",
             title_en="Discipline and Punish: The Birth of the Prison",
             title_fa="نظم و انضباط و تنبیه: زایش زندان",
             authors="Foucault, M.", year=1977, publisher="Pantheon",
             doi=None, url=None, language="en", isbn=None,
             citation="Foucault, M. (1977). Discipline and punish: The birth of the prison (A. Sheridan, Trans.). Pantheon.",
             locator="pt. 3", locator_type="CHAPTER",
             supports="panopticon baseline that sousveillance inverts", verified=False),
    ],
    "MC-529": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Information Technology and Dataveillance",
             title_fa="فناوری اطلاعات و پایش داده",
             authors="Clarke, R.", year=1988, publisher="Communications of the ACM",
             doi="10.1145/42411.42413",
             url="https://dl.acm.org/doi/10.1145/42411.42413",
             language="en", isbn=None,
             citation="Clarke, R. (1988). Information technology and dataveillance. Communications of the ACM, 31(5), 498-512. https://doi.org/10.1145/42411.42413",
             locator="31(5):498-512", locator_type="page_range",
             supports="dataveillance / personal vs mass dataveillance / categorical suspicion", verified=True),
        dict(kind="BOOK",
             title_en="Surveillance Society: Monitoring Everyday Life",
             title_fa="جامعه نظارتی: پایش زندگی روزمره",
             authors="Lyon, D.", year=2001, publisher="Open University Press",
             doi=None, url=None, language="en", isbn=None,
             citation="Lyon, D. (2001). Surveillance society: Monitoring everyday life. Open University Press.",
             locator="work", locator_type="work",
             supports="surveillance as ordinary routine infrastructure", verified=False),
    ],
    "MC-530": [
        dict(kind="BOOK",
             title_en="The Post-Truth Era: Dishonesty and Deception in Contemporary Life",
             title_fa="عصر پساحقیقت: ناراستی و فریب در زندگی معاصر",
             authors="Keyes, R.", year=2004, publisher="St. Martin's Press",
             doi=None, url="https://archive.org/details/posttrutheradish0000keye",
             language="en", isbn=None,
             citation="Keyes, R. (2004). The post-truth era: Dishonesty and deception in contemporary life. St. Martin's Press.",
             locator="work", locator_type="work",
             supports="post-truth as third category between truth and lie / euphemism and spin", verified=True),
        dict(kind="BOOK",
             title_en="Post-Truth",
             title_fa="پساحقیقت",
             authors="McIntyre, L.", year=2018, publisher="MIT Press",
             doi=None, url=None, language="en", isbn=None,
             citation="McIntyre, L. (2018). Post-truth. MIT Press.",
             locator="work", locator_type="work",
             supports="political definition of post-truth / erosion of objective truth", verified=True),
    ],
    "MC-532": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Accent Mobility: A Model and Some Data",
             title_fa="تحرک لهجه: یک مدل و برخی داده‌ها",
             authors="Giles, H.", year=1973, publisher="Anthropological Linguistics",
             doi=None, url=None, language="en", isbn=None,
             citation="Giles, H. (1973). Accent mobility: A model and some data. Anthropological Linguistics, 15(2), 87-105.",
             locator="15(2):87-105", locator_type="page_range",
             supports="accent convergence in interview / speaker accommodation model", verified=True),
        dict(kind="BOOK_CHAPTER",
             title_en="Accommodation Theory: Communication, Context, and Consequence",
             title_fa="نظریه تطابق: ارتباط، زمینه و پیامد",
             authors="Giles, H.; Coupland, N.; Coupland, J.", year=1991, publisher="Cambridge University Press",
             doi=None, url="https://resolve.cambridge.org/core/services/aop-cambridge-core/content/view/C71280FDB224240A8FB6C1F7B56C7E72/9780511663673c1_p1-68_CBO.pdf/accommodation-theory-communication-context-and-consequence.pdf",
             language="en", isbn=None,
             citation="Giles, H., Coupland, N., & Coupland, J. (1991). Accommodation theory: Communication, context, and consequence. In H. Giles, J. Coupland, & N. Coupland (Eds.), Contexts of accommodation: Developments in applied sociolinguistics (pp. 1-68). Cambridge University Press.",
             locator="pp. 1-68", locator_type="page_range",
             supports="convergence / divergence / maintenance typology and evaluation", verified=False),
    ],
}

ENRICH = {
    "MC-528": {
        "summary": "(مان، ۲۰۰۲؛ مان، نولان و ولمن، ۲۰۰۳) پادپایش یا سورویانس، ثبت و انتشار مشاهده از پایین است: افراد با دوربین پوشیدنی و رسانه‌های شخصی، رفتار صاحبان قدرت را مستند می‌کنند. مان این مفهوم را در برابر پایش از بالا نهاد و نشان داد ابزار یکسان می‌تواند هم نظارت کند و هم نظارت را وارونه سازد. مفهوم کلیدی او بازتابی‌گری است: به‌کارگیری فناوری تازه برای پرسش از پیش‌فرض‌های فناوری پیشین. پادپایش، عدم تقارن اطلاعاتی را هدف می‌گیرد و می‌کوشد نظارت را از انحصار سازمان بیرون آورد و به شهروند بازگرداند.",
        "definition": "پادپایش، عمل ثبت و انتشار مشاهده از موقعیت فرودست به‌سوی موقعیت فرادست است؛ کاربرد فناوری‌های ضبط و شبکه‌های انتشار توسط شهروندان برای مستندسازی رفتار قدرت، با هدف بازگرداندن نظارت و ساختن پاسخگویی.",
        "main_problem": "مسئله این است که نظارت در جوامع معاصر نامتقارن است: سازمان‌ها بیشتر می‌بینند و افراد کمتر. پرسش مان این است که آیا فناوری می‌تواند این عدم تقارن را برگرداند یا تنها آن را جابه‌جا می‌کند. پرسش دوم، پیامد است: وقتی همه دوربین دارند، نظارت به چه چیزی تبدیل می‌شود، چه کسی از آن سود می‌برد و چه کسی هزینه می‌پردازد.",
        "mechanism": "۱. تعریف جهت: پایش از بالا نهاد بر فرد است و پادپایش از فرد بر نهاد؛ تفاوت در جهت نگاه است، نه در ابزار.\n۲. فناوری پوشیدنی: دوربین کوچک و ضبط پیوسته، مشاهده را از رویداد استثنایی به جریان دائمی تبدیل می‌کند.\n۳. بازتابی‌گری: فناوری تازه به پرسش از پیش‌فرض‌های فناوری پیشین به کار می‌رود و مشروعیت پایش را آشکار می‌کند.\n۴. پانوپتیکن معکوس: به‌جای اندک بر بسیاری، بسیاری بر اندک نگاه می‌کنند و هزینه پایش را به بالا منتقل می‌سازند.\n۵. عدم تقارن دسترسی: ضبط از پایین اغلب بی‌سازمان و پراکنده است، اما انتشار شبکه‌ای آن می‌تواند اثر تجمعی بسازد.\n۶. هم‌پایشی و چرخه انتشار: افراد یکدیگر را نیز می‌پایند؛ نتیجه، چرخه‌ای از ثبت، برش و بازنشر است که معنا را تغییر می‌دهد.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا ویدئوی شهروندی از رفتار پلیس به مسئله عمومی تبدیل می‌شود، چرا دوربین بدن و پخش زنده هم ابزار پاسخگویی و هم ابزار فشار است و چرا پلتفرم‌ها به میدان نبرد پادپایش و پایش تبدیل می‌شوند. نکته مهم این است که پادپایش، نظارت را حذف نمی‌کند؛ توزیع می‌کند.",
        "assumptions": [
            "نظارت در جامعه معاصر نامتقارن و به سود نهادهاست.",
            "فناوری ضبط و انتشار، قدرت را از انحصار نهاد بیرون می‌آورد.",
            "مشروعیت پایش با آشکارشدن سازوکار آن به پرسش کشیده می‌شود.",
        ],
        "principles": [
            "جهت نگاه، پایش را از پادپایش جدا می‌کند.",
            "بازتابی‌گری، فناوری را به ابزار نقد بدل می‌کند.",
            "انتشار شبکه‌ای، اثر ضبط فردی را تجمعی می‌سازد.",
        ],
        "critiques": [
            "۱. تقارن صوری: ضبط از پایین، دسترسی به داده و قدرت تفسیر را برابر نمی‌کند.\n۲. خطر تشدید نظارت: دوربین شهروندی می‌تواند بهانه گسترش نظارت رسمی شود.\n۳. هم‌پایشی: پادپایش به سمت افراد عادی نیز می‌چرخد و حریم خصوصی را فرسوده می‌کند.\n۴. گزینش و برش: انتشار، همیشه گزینشی است و واقعیت را به قطعه‌ای قابل استناد تقلیل می‌دهد.\n۵. اقتصاد توجه: ارزش پادپایش به دیده‌شدن وابسته است و همین وابستگی، آن را به منطق پلتفرم گره می‌زند.",
        ],
        "applications": [
            "روزنامه‌نگاری شهروندی: مستندسازی رویداد و رفتار مأموران.",
            "پاسخگویی نهادی: دوربین بدن و ثبت تعامل با ارباب‌رجوع.",
            "پژوهش رسانه: تحلیل چرخه ضبط، برش و بازنشر ویدئوی شهروندی.",
            "سیاست حریم خصوصی: سنجش پیامد هم‌پایشی بر حقوق افراد.",
        ],
        "evolution": "مان در دهه ۱۹۹۰ با رایانش پوشیدنی، پادپایش را به‌عنوان عمل آزمایش کرد و در ۱۹۹۸ مفهوم بازتابی‌گری را صورت‌بندی کرد؛ مقاله ۲۰۰۳ آن را به چارچوبی برای تحلیل جهت نظارت گسترد. پژوهش بعدی، هم‌پایشی، دوربین بدن و پادپایش الگوریتمی را افزود و پرسش از پیامدهای تجاری و حریم خصوصی را پیش کشید.",
        "key_concepts": [
            "پادپایش (Sousveillance)",
            "پایش از بالا (Surveillance)",
            "بازتابی‌گری (Reflectionism)",
            "پانوپتیکن معکوس (Inverse Panopticon)",
            "هم‌پایشی (Coveillance)",
            "رایانش پوشیدنی (Wearable Computing)",
        ],
        "studies": [
            "Mann, S., Nolan, J., & Wellman, B. (2003). Sousveillance. Surveillance & Society, 1(3), 331-355.",
            "Foucault, M. (1977). Discipline and punish: The birth of the prison. Pantheon.",
        ],
        "theorists": "استیو مان؛ جیسون نولان؛ بری ولمن",
        "theorists_text": "استیو مان (۲۰۰۲)؛ مان، نولان و ولمن (۲۰۰۳)",
        "year": 2002,
        "model": "مدل سه‌گانه جهت پایش: پایش از بالا (نهاد بر فرد)، پادپایش (فرد بر نهاد)، هم‌پایشی (فرد بر فرد) → بازتابی‌گری → پرسش از مشروعیت پایش و بازتوزیع قدرت مشاهده.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nمان پادپایش را نه یک دستگاه، بلکه یک موقعیت مشاهده تعریف کرد: مشاهده‌ای که از سطح پایین سلسله‌مراتب آغاز می‌شود. نوآوری چارچوب، پیوند دادن فناوری پوشیدنی با پرسش سیاسی از مشروعیت نظارت است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش پادپایش با تحلیل جهت، دسترسی و اثر انجام می‌شود: چه کسی ضبط می‌کند، چه کسی می‌بیند و چه کسی پاسخ می‌دهد. پژوهش‌هایی که تنها حجم ویدئو را می‌سنجند، اثر سیاسی آن را نادیده می‌گیرند؛ و پژوهش‌هایی که تنها نیت را می‌سنجند، سازوکار انتشار را از دست می‌دهند.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در توضیح پاسخگویی شهروندی است، اما باید با تحلیل پلتفرم تکمیل شود. در محیط داده‌ای، پادپایش بدون دسترسی به داده و ابزار تفسیر، به نمایش بی‌اثر یا ابزار توجه تبدیل می‌شود.",
        "critique_text": "\n".join([
            "۱. تقارن صوری: ضبط از پایین، قدرت تفسیر را برابر نمی‌کند.",
            "۲. خطر تشدید نظارت: پادپایش می‌تواند بهانه گسترش پایش رسمی شود.",
            "۳. هم‌پایشی: نگاه انتقادی به سمت افراد عادی می‌چرخد.",
            "۴. گزینش و برش: انتشار، واقعیت را به قطعه تقلیل می‌دهد.",
            "۵. اقتصاد توجه: ارزش پادپایش به دیده‌شدن گره خورده است.",
        ]),
        "example_text": "شهروندی با گوشی، بازداشت خشن یک عابر را ضبط و منتشر می‌کند. ضبط، رویدادی محلی را به مسئله عمومی تبدیل می‌کند، اما پلتفرم با برش و پیشنهاد الگوریتمی، معنای آن را تغییر می‌دهد و همان ویدئو به دادگاهی از تفسیرهای رقیب بدل می‌شود.",
    },
    "MC-529": {
        "summary": "(کلارک، ۱۹۸۸) پایش داده یعنی نظارت بر افراد از راه داده‌های شخصی، نه از راه تماشای مستقیم رفتار. کلارک نشان داد فناوری اطلاعات، مشاهده را از بدن به پرونده منتقل می‌کند و همین جابه‌جایی، نظارت را ارزان، پیوسته و فراگیر می‌سازد. او دو سطح را تفکیک کرد: پایش داده فردی که پرونده یک شخص را دنبال می‌کند و پایش داده انبوه که با تطبیق و الگوگیری، جمعیت را غربال می‌کند. مفهوم «ظن مقوله‌ای» بیان می‌کند که عضویت در یک مقوله، جای شواهد فردی را می‌گیرد و افراد پیش از ارتکاب خطا مشکوک می‌شوند.",
        "definition": "پایش داده، گردآوری و پیوند نظام‌مند داده‌های شخصی برای پایش کنش‌ها و ارتباطات افراد است؛ نظارتی که موضوع آن پرونده و الگوی داده است، نه مشاهده مستقیم بدن.",
        "main_problem": "مسئله این است که نظارت دیجیتال بی‌سر‌و‌صدا و ارزان شده است: ثبت، ذخیره، پیوند و تحلیل داده، مشاهده را به فعالیتی پس‌زمینه‌ای تبدیل می‌کند. پرسش کلارک این است که چه زمانی داده، جانشین شخص می‌شود و تصمیم درباره انسان بر پایه تصویر داده‌ای او گرفته می‌شود. پرسش دوم، عدالت است: تطبیق و غربال، بار خطا را بر دوش چه کسانی می‌گذارد.",
        "mechanism": "۱. انتقال موضوع نظارت: مشاهده از بدن به پرونده منتقل می‌شود و همین انتقال، نظارت را مقیاس‌پذیر می‌کند.\n۲. ثبت رایگان اثر جانبی: هر تعامل دیجیتال داده می‌سازد، بی‌آنکه کسی قصد نظارت داشته باشد.\n۳. پیوند و تطبیق: داده‌های پراکنده با کلیدهای مشترک به هم وصل می‌شوند و تصویری کامل‌تر می‌سازند.\n۴. الگوگیری و غربال: پروفایل‌ها با الگوهای از پیش تعیین‌شده مقایسه و افراد دسته‌بندی می‌شوند.\n۵. ظن مقوله‌ای: عضویت در مقوله مشکوک، جانشین شواهد فردی می‌شود و بار اثبات جابه‌جا می‌گردد.\n۶. تصویر داده‌ای: شخص با بازنمایی داده‌ای خود جایگزین می‌شود و تصمیم بر پایه همان بازنمایی گرفته می‌شود.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا تبلیغات هدفمند، امتیازدهی اعتباری، تشخیص تقلب و مدیریت محتوا بر پایه پرونده عمل می‌کنند و چرا کاربران از سازوکار تصمیم بی‌خبرند. نکته مهم این است که پایش داده با محتوای ارتباط کار ندارد؛ با الگوی آن کار دارد.",
        "assumptions": [
            "داده‌های شخصی را می‌توان به‌طور معنادار به فرد نسبت داد.",
            "پیوند و تطبیق داده، تصویری معتبر از رفتار می‌سازد.",
            "الگوهای رفتاری، آینده فرد را قابل پیش‌بینی می‌کنند.",
        ],
        "principles": [
            "نظارت ارزان، گسترش می‌یابد.",
            "داده بی‌طرف نیست؛ گردآوری و تفسیر آن جهت‌دار است.",
            "بار خطای غربال بر دوش گروه‌های کم‌توان‌تر می‌افتد.",
        ],
        "critiques": [
            "۱. خطای بازنمایی: داده، آنچه ثبت شده را می‌بیند و آنچه ثبت نشده را نادیده می‌گیرد.\n۲. شفافیت ناکافی: سازوکار تطبیق و الگوگیری برای افراد نامعلوم است.\n۳. ظن پیشینی: غربال، بی‌گناهی را به اثبات‌پذیری وابسته می‌کند.\n۴. پیوند بی‌مرز: قابلیت اتصال داده‌ها، محدودیت هدف را از میان برمی‌دارد.\n۵. تعمیم بیش‌ازحد: کلارک چارچوب را در بستر نهادی دهه ۱۹۸۰ ساخت؛ پلتفرم‌های داده‌محور، سازوکار را پیچیده‌تر و نامرئی‌تر کرده‌اند.",
        ],
        "applications": [
            "حریم خصوصی داده: ارزیابی پیوند و هدف‌مندی داده‌های شخصی.",
            "امتیازدهی و اعتبارسنجی: تحلیل عدالت الگوریتمی در دسته‌بندی افراد.",
            "رسانه و تبلیغات: بررسی هدف‌گیری بر پایه پروفایل رفتاری.",
            "سیاست‌گذاری: طراحی حداقل‌سازی داده و حق توضیح تصمیم.",
        ],
        "evolution": "کلارک در ۱۹۸۸ پایش داده را نام‌گذاری و دو سطح فردی و انبوه آن را تفکیک کرد؛ در ۱۹۹۴ با مفهوم «شخصیت داده‌ای» بحث را به هویت بازنمایی‌شده در داده گسترد. پژوهش بعدی، نظارت پلتفرمی، یادگیری ماشین و عدالت الگوریتمی را به این خط افزود.",
        "key_concepts": [
            "پایش داده (Dataveillance)",
            "پایش داده فردی (Personal Dataveillance)",
            "پایش داده انبوه (Mass Dataveillance)",
            "ظن مقوله‌ای (Categorical Suspicion)",
            "شخصیت داده‌ای (Digital Persona)",
            "سایه داده (Data Shadow)",
        ],
        "studies": [
            "Clarke, R. (1988). Information technology and dataveillance. Communications of the ACM, 31(5), 498-512.",
            "Lyon, D. (2001). Surveillance society: Monitoring everyday life. Open University Press.",
        ],
        "theorists": "راجر کلارک",
        "theorists_text": "راجر کلارک (۱۹۸۸؛ ۱۹۹۴)",
        "year": 1988,
        "model": "زنجیره پایش داده: ثبت اثر جانبی تعامل → ذخیره و پیوند پرونده‌ها → تطبیق و الگوگیری → ظن مقوله‌ای → تصمیم بر پایه تصویر داده‌ای، با دو سطح فردی و انبوه.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nکلارک اصطلاح پایش داده را برای جداکردن نظارت داده‌محور از نظارت بصری ساخت. نوآوری او نشان دادن این نکته بود که ارزان‌شدن ثبت و پیوند، نظارت را از فعالیتی استثنایی به زیرساختی روزمره بدل می‌کند.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با شمار پرونده‌های پیوندخورده، دامنه تطبیق و نرخ خطای دسته‌بندی انجام می‌شود. پژوهشی که تنها حجم داده را می‌سنجد، اثر قدرت را از دست می‌دهد؛ و پژوهشی که تنها نیت سازمان را می‌سنجد، سازوکار فنی را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در پیوند دادن داده با تصمیم است، اما باید با تحلیل پلتفرم و یادگیری ماشین تکمیل شود. در محیط امروز، پایش داده نه فقط پرونده دولتی، بلکه زیرساخت تجاری و الگوریتمی است.",
        "critique_text": "\n".join([
            "۱. خطای بازنمایی: داده، ثبت‌نشده‌ها را نمی‌بیند.",
            "۲. شفافیت ناکافی: سازوکار الگوگیری پنهان است.",
            "۳. ظن پیشینی: بی‌گناهی به اثبات وابسته می‌شود.",
            "۴. پیوند بی‌مرز: محدودیت هدف از میان می‌رود.",
            "۵. تعمیم بیش‌ازحد: بستر نهادی دهه ۱۹۸۰ ساده‌تر از پلتفرم امروز است.",
        ]),
        "example_text": "سیستم ضدتقلب بانک، تراکنش‌های یک مشتری را با الگوی پرریسک مقایسه و حساب او را موقتاً می‌بندد. هیچ مشاهده مستقیمی رخ نداده است؛ تصمیم بر پایه پیوند داده و ظن مقوله‌ای گرفته شده و مشتری تنها با اثبات نادرستی الگو آزاد می‌شود.",
    },
    "MC-530": {
        "summary": "(کیز، ۲۰۰۴؛ مک‌اینتایر، ۲۰۱۸) پساحقیقت وضعیتی است که در آن تمایز میان راست و دروغ سست می‌شود و دسته‌ای سوم از گفتار پدید می‌آید: گزاره‌های مبهمی که دقیقاً راست نیستند، اما به دروغ هم نمی‌رسند. کیز این وضعیت را با فراوانی تعبیرهای تلطیف‌شده، چرخش تبلیغاتی و راست‌نمایی پیوند داد و نشان داد هزینه اجتماعی ناراستی کاهش یافته است. مک‌اینتایر مفهوم را سیاسی کرد: پساحقیقت، فرسایش جایگاه حقیقت عینی در بحث عمومی است. در این چارچوب، اطلاعات نادرست نه خطای فردی، بلکه سازوکار تولید بی‌اعتمادی است.",
        "definition": "پساحقیقت، وضعیتی ارتباطی است که در آن صدق و کذب معیار اصلی ارزیابی گفتار نیست و گزاره‌های مبهم، تلطیف‌شده یا عاطفه‌محور جای گزارش صادق را می‌گیرند؛ وضعیتی که در آن ادعای حقیقت از استدلال آن جدا می‌شود.",
        "main_problem": "مسئله این است که چرا در زندگی عمومی، دروغ آشکار هزینه کمی دارد و ابهام سودآور است. پاسخ کیز در فرهنگ است: تعبیر تلطیف‌شده، چرخش، و توجیه اخلاقی، ناراستی را قابل تحمل می‌کنند. پرسش مک‌اینتایر سیاسی است: وقتی معیار مشترک حقیقت از میان برود، داوری عمومی بر چه پایه‌ای ممکن است.",
        "mechanism": "۱. دسته سوم گفتار: گزاره‌های نه‌کاملاً‌راست و نه‌کاملاً‌دروغ، فضایی برای فرار از مسئولیت می‌سازند.\n۲. تعبیر تلطیف‌شده: واژه نرم، زشتی عمل را می‌پوشاند و حساسیت اخلاقی را کاهش می‌دهد.\n۳. چرخش و روایت: بازچینش زمینه، گزاره نادرست را قابل دفاع می‌کند.\n۴. راست‌نمایی: تأکید بر صداقت بیان، جانشین بررسی صدق محتوا می‌شود.\n۵. کاهش هزینه: اگر ناراستی در رقابت سودآور باشد و پیامدی نداشته باشد، گسترش می‌یابد.\n۶. فرسایش اعتماد: تکرار ناراستی، اعتماد به نهادهای تولید خبر و دانش را می‌فرساید و زمینه اطلاعات نادرست را می‌سازد.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا تکذیب و راستی‌آزمایی اغلب از ادعای نخست عقب می‌ماند، چرا مخاطب بر پایه هویت گروهی داوری می‌کند و چرا بازنشر عاطفی بر دقت پیشی می‌گیرد. نکته مهم این است که پساحقیقت، نبود حقیقت نیست؛ بی‌اثرشدن معیار حقیقت در داوری عمومی است.",
        "assumptions": [
            "گفتار عمومی می‌تواند میان راست، دروغ و ابهام تفکیک شود.",
            "هزینه اجتماعی ناراستی بر فراوانی آن اثر می‌گذارد.",
            "اعتماد به نهادهای دانش، شرط داوری عمومی معتبر است.",
        ],
        "principles": [
            "ابهام، از دروغ سودآورتر است.",
            "تکرار، جای صدق را نمی‌گیرد اما جای آن را می‌گیرد.",
            "راستی‌آزمایی بدون اعتماد نهادی اثر محدودی دارد.",
        ],
        "critiques": [
            "۱. ابهام مفهومی: مرز پساحقیقت با تبلیغ سنتی و دروغ سیاسی روشن نیست.\n۲. تمرکز بر اخلاق فردی: کیز ساختار اقتصادی و سیاسی تولید ناراستی را کم‌رنگ می‌کند.\n۳. سنجش دشوار: اندازه‌گیری کاهش صداقت در سطح جامعه با داده موجود ممکن نیست.\n۴. خطر نسبی‌انگاری: تأکید بر ساخت اجتماعی حقیقت می‌تواند به انکار معیار مشترک بیانجامد.\n۵. ساده‌سازی مخاطب: فرض واکنش یکسان مخاطبان، تفاوت مهارت و زمینه را نادیده می‌گیرد.",
        ],
        "applications": [
            "راستی‌آزمایی خبری: ارزیابی ادعا بر پایه شواهد و زمینه، نه لحن.",
            "سواد رسانه‌ای: آموزش تفکیک ابهام، چرخش و دروغ.",
            "سیاست ارتباطی: سنجش اثر کمپین‌های بی‌اعتمادساز.",
            "پژوهش افکار عمومی: تحلیل داوری هویت‌محور به‌جای داوری شواهدمحور.",
        ],
        "evolution": "کیز اصطلاح پساحقیقت را در دهه ۱۹۹۰ به کار برد و در ۲۰۰۴ به کتابی درباره فرهنگ ناراستی گسترد. در ۲۰۱۶ واژه سال فرهنگستان زبان انگلیسی آکسفورد شد و مک‌اینتایر در ۲۰۱۸ آن را به نظریه‌ای سیاسی درباره فرسایش حقیقت عینی بدل کرد؛ پژوهش بعدی، رسانه اجتماعی و اطلاعات نادرست را به این خط افزود.",
        "key_concepts": [
            "پساحقیقت (Post-Truth)",
            "ابهام‌گویی (Ambiguity)",
            "چرخش تبلیغاتی (Spin)",
            "راست‌نمایی (Truthiness)",
            "اطلاعات نادرست (Misinformation)",
            "اطلاعات جعلی (Disinformation)",
        ],
        "studies": [
            "Keyes, R. (2004). The post-truth era: Dishonesty and deception in contemporary life. St. Martin's Press.",
            "McIntyre, L. (2018). Post-truth. MIT Press.",
        ],
        "theorists": "رالف کیز؛ لی مک‌اینتایر",
        "theorists_text": "رالف کیز (۲۰۰۴)؛ لی مک‌اینتایر (۲۰۱۸)",
        "year": 2004,
        "model": "زنجیره پساحقیقت: تعبیر تلطیف‌شده و چرخش → گزاره مبهم → کاهش هزینه ناراستی → تکرار و عادت‌زدایی → فرسایش اعتماد نهادی → داوری هویت‌محور و گسترش اطلاعات نادرست.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nکیز پساحقیقت را در قلمرو اخلاق روزمره ساخت و مک‌اینتایر آن را به قلمرو سیاست برد. پیوند این دو، چارچوب را از توصیف یک عادت گفتاری به تحلیل فرسایش زیرساخت معرفتی جامعه ارتقا می‌دهد.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با تحلیل ادعا، نرخ تصحیح، دامنه انتشار و اعتماد نهادی انجام می‌شود. پژوهشی که تنها دروغ آشکار را می‌شمارد، ابهام سودآور را از دست می‌دهد؛ و پژوهشی که تنها اعتماد را می‌سنجد، محتوای گفتار را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در توضیح بی‌اثری تکذیب است، اما باید با تحلیل پلتفرم تکمیل شود. در محیط الگوریتمی، پاداش توجه به گزاره جنجالی، سازوکار پساحقیقت را تقویت می‌کند.",
        "critique_text": "\n".join([
            "۱. ابهام مفهومی: مرز با تبلیغ سنتی روشن نیست.",
            "۲. تمرکز بر اخلاق فردی: ساختار تولید ناراستی کم‌رنگ می‌شود.",
            "۳. سنجش دشوار: کاهش صداقت در سطح جامعه اندازه‌پذیر نیست.",
            "۴. خطر نسبی‌انگاری: ساخت اجتماعی حقیقت به انکار معیار می‌انجامد.",
            "۵. ساده‌سازی مخاطب: تفاوت مهارت و زمینه نادیده می‌ماند.",
        ]),
        "example_text": "سخنگوی یک نهاد می‌گوید «هیچ خطایی رخ نداده، اما رویه بازبینی می‌شود». گزاره دروغ نیست، اما مسئولیت را جابه‌جا می‌کند؛ تکذیب مفصل بعدی، کمتر از همان جمله دیده می‌شود و مخاطب در نهایت بر پایه اعتماد به گوینده داوری می‌کند، نه بر پایه شواهد.",
    },
    "MC-532": {
        "summary": "(گایلز، ۱۹۷۱؛ ۱۹۷۳؛ گایلز، کوپلند و کوپلند، ۱۹۹۱) نظریه تطابق ارتباطی توضیح می‌دهد که گویندگان در تعامل، سبک گفتار خود را به سبک طرف مقابل نزدیک یا از آن دور می‌کنند. همگرایی، فاصله ارتباطی را کم می‌کند و واگرایی آن را می‌گشاید؛ حفظ نیز حالتی است که گوینده سبک خود را تغییر نمی‌دهد. گایلز نشان داد این حرکت‌ها تصادفی نیستند: هم هویت گروهی و هم رابطه میان‌فردی آن را جهت می‌دهد. تطابق، هم ابزار جلب تأیید و هم ابزار مرزبندی است.",
        "definition": "نظریه تطابق ارتباطی، چارچوبی است که تغییرهای راهبردی گوینده در سبک گفتار را در تعامل توضیح می‌دهد؛ همگرایی، واگرایی و حفظ، پاسخ‌هایی به فاصله اجتماعی و هویت گروهی‌اند.",
        "main_problem": "مسئله این است که چرا مردم سبک گفتار خود را تغییر می‌دهند و این تغییر چه پیامدی دارد. پاسخ در ترکیب دو انگیزه است: میل به تأیید و کاهش فاصله، و میل به حفظ هویت و مرزبندی گروهی. پرسش دوم، ارزیابی است: تطابق چه زمانی صادق و چه زمانی تحمیلی یا تحقیرآمیز تلقی می‌شود.",
        "mechanism": "۱. همگرایی: گوینده آهنگ، سرعت، واژگان و فاصله را به طرف مقابل نزدیک می‌کند تا فهم و تأیید را افزایش دهد.\n۲. واگرایی: گوینده سبک خود را برجسته می‌کند تا تفاوت گروهی را نشان دهد و مرز حفظ شود.\n۳. حفظ: بدون تغییر آشکار، گوینده سبک خود را نگه می‌دارد؛ گاه نشانه بی‌اعتنایی و گاه نشانه ثبات هویت.\n۴. دو انگیزه هم‌زمان: نیاز به تأیید و نیاز به تمایز، جهت تطابق را تعیین می‌کنند.\n۵. ارزیابی مخاطب: تطابق می‌تواند صادق، اغراق‌شده یا تحقیرآمیز تفسیر شود و همین تفسیر، پیامد رابطه را می‌سازد.\n۶. بافت نهادی: در مصاحبه، کلاس درس و رسانه، عدم تقارن قدرت جهت تطابق را تعیین می‌کند.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا مجری لهجه خود را به مهمان نزدیک می‌کند، چرا گویندگان اقلیت در رسانه ملی سبک خود را تغییر می‌دهند یا بر آن پافشاری می‌کنند و چرا مخاطب، لحن نزدیک‌شده را گاه صمیمیت و گاه تظاهر می‌خواند. نکته مهم این است که تطابق، هم پل ارتباطی است و هم نشانه قدرت.",
        "assumptions": [
            "سبک گفتار، نشانه هویت گروهی و رابطه است.",
            "گویندگان در تعامل، سبک خود را راهبردی تنظیم می‌کنند.",
            "مخاطب، نیت تطابق را تفسیر و ارزیابی می‌کند.",
        ],
        "principles": [
            "همگرایی، فاصله اجتماعی را کاهش می‌دهد.",
            "واگرایی، مرز گروهی را برجسته می‌کند.",
            "ارزیابی مخاطب، اثر تطابق را تعیین می‌کند.",
        ],
        "critiques": [
            "۱. تمرکز بر گفتار: تطابق غیرکلامی و متنی کمتر صورت‌بندی شده است.\n۲. سنجش نیت: تفکیک همگرایی آگاهانه از همرنگی ناخودآگاه دشوار است.\n۳. نمونه آزمایشگاهی: بسیاری از شواهد اولیه از موقعیت‌های کنترل‌شده می‌آید.\n۴. کم‌توجهی به قدرت: جهت تطابق در رابطه نامتقارن، اغلب به سود طرف قدرتمند است.\n۵. فراتطابق: اغراق در نزدیک‌شدن می‌تواند تحقیرآمیز تلقی شود و به واگرایی بینجامد.",
        ],
        "applications": [
            "ارتباط بین‌فرهنگی: آموزش حساسیت به سبک و کاهش سوگیری لهجه‌ای.",
            "رسانه و گفتار عمومی: تحلیل سبک مجری و مهمان در برنامه‌های گفتاری.",
            "مراقبت سلامت: تطابق پزشک با سبک بیمار و اثر آن بر فهم دستور درمان.",
            "آموزش زبان: استفاده از تطابق برای کاهش اضطراب یادگیرنده.",
        ],
        "evolution": "گایلز در ۱۹۷۱ و ۱۹۷۳ با مطالعه تحرک لهجه، مدل تطابق را صورت‌بندی کرد؛ در ۱۹۹۱ با کوپلند و کوپلند آن را به چارچوبی برای ارتباط میان‌فردی و بین‌گروهی گسترد. پژوهش بعدی، فراتطابق، تطابق در رسانه و ارتباط سلامت را به این خط افزود.",
        "key_concepts": [
            "همگرایی (Convergence)",
            "واگرایی (Divergence)",
            "حفظ (Maintenance)",
            "فراتطابق (Over-accommodation)",
            "هویت گروهی (Group Identity)",
            "شایستگی تفسیری (Interpretive Competence)",
        ],
        "studies": [
            "Giles, H. (1973). Accent mobility: A model and some data. Anthropological Linguistics, 15(2), 87-105.",
            "Giles, H., Coupland, N., & Coupland, J. (1991). Accommodation theory. In Contexts of accommodation (pp. 1-68). Cambridge University Press.",
        ],
        "theorists": "هاوارد گایلز؛ نیکولاس کوپلند؛ جاستین کوپلند",
        "theorists_text": "هاوارد گایلز (۱۹۷۱؛ ۱۹۷۳)؛ گایلز، کوپلند و کوپلند (۱۹۹۱)",
        "year": 1971,
        "model": "مدل تطابق: فاصله اجتماعی و هویت گروهی + انگیزه تأیید → همگرایی / واگرایی / حفظ → تفسیر مخاطب → تقویت یا تضعیف رابطه و مرز گروهی.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nگایلز تطابق را از تغییر لهجه در مصاحبه آغاز کرد و آن را به نظریه‌ای درباره مدیریت فاصله اجتماعی گسترد. نوآوری چارچوب، پیوند دادن تغییر خردِ سبک گفتار با هویت گروهی و ساختار قدرت است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با مقایسه آوایی، واژگانی و آهنگی پیش و پس از تعامل انجام می‌شود. پژوهشی که تنها همگرایی را می‌سنجد، واگرایی و حفظ را از دست می‌دهد؛ و پژوهشی که تنها نیت گوینده را می‌سنجد، تفسیر مخاطب را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در توضیح سبک رسانه‌ای است، اما باید با تحلیل مخاطب تکمیل شود. در رسانه، تطابق نه فقط میان دو گوینده، بلکه میان گوینده و مخاطب نامرئی رخ می‌دهد.",
        "critique_text": "\n".join([
            "۱. تمرکز بر گفتار: تطابق غیرکلامی کمتر صورت‌بندی شده است.",
            "۲. سنجش نیت: تفکیک آگاهانه از ناخودآگاه دشوار است.",
            "۳. نمونه آزمایشگاهی: شواهد اولیه محدود به موقعیت کنترل‌شده است.",
            "۴. کم‌توجهی به قدرت: جهت تطابق به سود طرف قدرتمند است.",
            "۵. فراتطابق: اغراق در نزدیک‌شدن، تحقیرآمیز تلقی می‌شود.",
        ]),
        "example_text": "مجری تلویزیونی که با مهمانی از شهری دیگر گفت‌وگو می‌کند، آهنگ و واژگان خود را کمی به او نزدیک می‌کند. مخاطبان صمیمیت را می‌بینند، اما گروهی آن را تظاهر می‌خوانند؛ نتیجه به تفسیر مخاطب وابسته است، نه به نیت مجری.",
    },
}

REQUIRED_SECTIONS = ["summary", "definition", "main_problem", "mechanism", "assumptions",
                     "principles", "critiques", "applications", "evolution", "key_concepts",
                     "theorists", "model", "studies"]
WORD_KEYS = ["summary", "definition", "main_problem", "mechanism", "critiques", "applications",
             "evolution", "key_concepts", "principles", "studies", "assumptions"]


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


NAME_FIX = {
    "MC-528": ("سورویانس (پادپایش)", "Sousveillance",
               "canonical_name_fa/en repaired: transliteration 'سورویانس' + 'Surveillance' aligned to Mann's sousveillance (theorist=Mann, 2002)"),
    "MC-529": ("نظریه پایش داده (داده‌برداری)", "Dataveillance Theory",
               "canonical_name_fa/en repaired: 'داده‌کاوی' (data mining) / 'Data Extraction' aligned to Clarke's dataveillance"),
    "MC-532": ("نظریه تطابق ارتباطی", "Communication Accommodation Theory",
               "canonical_name_fa/en repaired: 'همانندی' (similarity) / 'Communication Similarity' aligned to Giles's accommodation theory"),
}


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

        cur.execute("UPDATE kb_entities SET properties=%s, version=version+1, updated_at=%s WHERE id=%s",
                    (json.dumps(p, ensure_ascii=False), NOW, eid))
        cur.execute("SELECT version FROM kb_entities WHERE id=%s", (eid,))
        new_version = cur.fetchone()[0]

        for src in S[code]:
            sid = ensure_source(cur, src)
            cur.execute("SELECT id FROM kb_evidence WHERE about_code=%s AND source_id=%s LIMIT 1", (code, sid))
            if cur.fetchone():
                continue
            lt = {"work": "SECTION", "page_range": "PAGE", "CHAPTER": "CHAPTER"}.get(src["locator_type"], "SECTION")
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
                                       "verified": n_verified, "batch": 96}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH96 THEORY DONE")


if __name__ == "__main__":
    main()
