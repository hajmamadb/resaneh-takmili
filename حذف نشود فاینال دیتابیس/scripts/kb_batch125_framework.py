# -*- coding: utf-8 -*-
"""Batch 125 (FRAMEWORK): full documentation for MC-638, MC-642, MC-645, MC-647."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch125-framework-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch125_framework.json"

S = {
    "MC-638": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="The CNN Effect: Can the News Media Drive Foreign Policy?",
             title_fa="اثر سیانان: آیا رسانه‌های خبری می‌توانند سیاست خارجی را هدایت کنند؟",
             authors="Robinson, P.", year=1999,
             publisher="Review of International Studies",
             doi=None,
             url="https://www.cambridge.org/core/journals/review-of-international-studies/article/cnn-effect-can-the-news-media-drive-foreign-policy/82861CF3D16F66F2BB51A8591E6470EF",
             language="en", isbn=None,
             citation="Robinson, P. (1999). The CNN effect: Can the news media drive foreign policy? Review of International Studies, 25(2), 301-309.",
             locator="25(2):301-309", locator_type="page_range",
             supports="conditional CNN effect: agenda-setting, short-term and impediment effects", verified=True),
        dict(kind="BOOK",
             title_en="The CNN Effect: The Myth of News, Foreign Policy and Intervention",
             title_fa="اثر سیانان: افسانهٔ خبر، سیاست خارجی و مداخله",
             authors="Robinson, P.", year=2002,
             publisher="Routledge",
             doi=None, url=None, language="en", isbn=None,
             citation="Robinson, P. (2002). The CNN Effect: The Myth of News, Foreign Policy and Intervention. London: Routledge.",
             locator="book", locator_type="SECTION",
             supports="book-length development of the conditional media-policy model", verified=False),
    ],
    "MC-642": [
        dict(kind="REPORT",
             title_en="Report of the Working Group on Internet Governance",
             title_fa="گزارش گروه کاری حاکمیت اینترنت",
             authors="Working Group on Internet Governance", year=2005,
             publisher="United Nations / WSIS",
             doi=None,
             url="https://www.wgig.org/docs/WGIGREPORT.pdf",
             language="en", isbn=None,
             citation="Working Group on Internet Governance. (2005). Report of the Working Group on Internet Governance. Geneva: United Nations.",
             locator="working definition of Internet governance", locator_type="SECTION",
             supports="working definition of Internet governance and multi-stakeholder model", verified=True),
        dict(kind="BOOK",
             title_en="The Global War for Internet Governance",
             title_fa="جنگ جهانی حاکمیت اینترنت",
             authors="DeNardis, L.", year=2014,
             publisher="Yale University Press",
             doi=None, url=None, language="en", isbn=None,
             citation="DeNardis, L. (2014). The Global War for Internet Governance. New Haven: Yale University Press.",
             locator="book", locator_type="SECTION",
             supports="infrastructure-based account of Internet governance conflicts", verified=False),
    ],
    "MC-645": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Consumer Acceptance and Use of Information Technology: Extending the Unified Theory of Acceptance and Use of Technology",
             title_fa="پذیرش و کاربرد فناوری اطلاعات به‌دست مصرف‌کننده: بسط نظریهٔ یکپارچهٔ پذیرش و کاربرد فناوری",
             authors="Venkatesh, V.; Thong, J. Y. L.; Xu, X.", year=2012,
             publisher="MIS Quarterly",
             doi="10.2307/41410412",
             url="https://aisel.aisnet.org/misq/vol36/iss1/13/",
             language="en", isbn=None,
             citation="Venkatesh, V., Thong, J. Y. L., & Xu, X. (2012). Consumer acceptance and use of information technology: Extending the unified theory of acceptance and use of technology. MIS Quarterly, 36(1), 157-178.",
             locator="36(1):157-178", locator_type="page_range",
             supports="UTAUT2 model with hedonic motivation, price value and habit", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="User Acceptance of Information Technology: Toward a Unified View",
             title_fa="پذیرش فناوری اطلاعات به‌دست کاربر: به‌سوی دیدگاهی یکپارچه",
             authors="Venkatesh, V.; Morris, M. G.; Davis, G. B.; Davis, F. D.", year=2003,
             publisher="MIS Quarterly",
             doi=None, url=None, language="en", isbn=None,
             citation="Venkatesh, V., Morris, M. G., Davis, G. B., & Davis, F. D. (2003). User acceptance of information technology: Toward a unified view. MIS Quarterly, 27(3), 425-478.",
             locator="27(3):425-478", locator_type="page_range",
             supports="original UTAUT model that UTAUT2 extends", verified=False),
    ],
    "MC-647": [
        dict(kind="BOOK",
             title_en="Remediation: Understanding New Media",
             title_fa="بازواسازی: فهم رسانه‌های نو",
             authors="Bolter, J. D.; Grusin, R.", year=1999,
             publisher="MIT Press",
             doi=None,
             url="https://mitpress.mit.edu/9780262024525/remediation/",
             language="en", isbn="9780262024525",
             citation="Bolter, J. D., & Grusin, R. (1999). Remediation: Understanding New Media. Cambridge, MA: MIT Press.",
             locator="book", locator_type="SECTION",
             supports="double logic of immediacy and hypermediacy in remediation", verified=True),
        dict(kind="BOOK",
             title_en="Understanding Media: The Extensions of Man",
             title_fa="فهم رسانه: امتدادهای انسان",
             authors="McLuhan, M.", year=1964,
             publisher="McGraw-Hill",
             doi=None, url=None, language="en", isbn=None,
             citation="McLuhan, M. (1964). Understanding Media: The Extensions of Man. New York: McGraw-Hill.",
             locator="book", locator_type="SECTION",
             supports="media as extensions and prior genealogies of media forms", verified=False),
    ],
}

ENRICH = {
    "MC-638": dict(
        year=1999,
        summary="اثر سیانان، اصطلاحی است که در دههٔ ۱۹۹۰ برای توصیف تأثیر پوشش خبری زنده و پیوسته بر سیاست خارجی ساخته شد. عبارت به پوشش شبکهٔ خبری سیانان از جنگ خلیج فارس و بحران‌های سومالی، بوسنی و کوزوو اشاره داشت و این گمان را بیان می‌کرد که دوربین خبری می‌تواند دولت‌ها را به واکنش وادار کند. پییرز رابینسون در مقالهٔ سال ۱۹۹۹ در نشریهٔ مطالعات بین‌المللی این گمان را به نظریه‌ای آزمون‌پذیر تبدیل کرد. او سه گونهٔ اثر را از هم جدا کرد: اثر تعیین دستور کار، یعنی اولویت‌دادن رسانه به موضوعی که پیش‌تر در سیاست وجود داشته است؛ اثر کوتاه‌مدت، یعنی واکنش سریع دولت به فشار خبری؛ و اثر بازدارنده، یعنی محدودشدن گزینه‌های نظامی به‌سبب نگرانی از افکار عمومی. نتیجهٔ مرکزی او این بود که اثر سیانان مشروط است: در حوزه‌ای از سیاست خارجی که تصمیم‌گیرندگان دربارهٔ آن مطمئن نیستند و اجماع نخبگان ضعیف است، فشار خبری بیشترین نقش را دارد. این نظریه بعدها به تحلیل مداخلهٔ بشردوستانه و دیپلماسی بحران راه یافت. نقدهای اصلی به آن، دشواری جداسازی اثر رسانه از عوامل دیگر، امکان ساختگی بودن اثر به‌دست خود دولت‌ها و شواهد ناهمگون مطالعات موردی است.",
        definition="اثر سیانان، گزاره‌ای در مطالعات رسانه و سیاست خارجی است که می‌گوید پوشش خبری زنده و پیوسته می‌تواند واکنش دولت‌ها را برانگیزد یا گزینه‌های آنها را محدود کند، به‌ویژه زمانی که سیاست رسمی نامطمئن و اجماع نخبگان ضعیف است.",
        main_problem="آیا خبررسانی آنی می‌تواند سیاست خارجی را از مسیر عقلانی تصمیم‌گیری بیرون ببرد و دولت را به واکنش در برابر فشار افکار عمومی وادارد، و اگر چنین است، این اثر در چه شرایطی رخ می‌دهد.",
        mechanism="پوشش زنده، رنج و بحران را به بینندگان نزدیک می‌کند و فشار عاطفی و عمومی می‌سازد؛ این فشار از راه رسانه‌های داخلی و پرسش‌های خبرنگاران به تصمیم‌گیرندگان منتقل می‌شود. اثر در سه سطح عمل می‌کند: تعیین اولویت موضوعی، واکنش کوتاه‌مدت و بازدارندگی از گزینهٔ نظامی. شرط اثرگذاری، ابهام سیاست رسمی و شکاف در اجماع نخبگان است؛ جایی که سیاست روشن و اجماع قوی باشد، رسانه بیشتر مجرای اجرای همان سیاست می‌شود.",
        assumptions=[
            "تصمیم‌گیرندگان به افکار عمومی و پوشش خبری حساس‌اند.",
            "پوشش زنده و پیوسته می‌تواند احساسات عمومی را به‌سرعت برانگیزد.",
            "سیاست خارجی در شرایط ابهام، فضای بیشتری برای اثرپذیری از فشار خبری دارد.",
            "اجماع نخبگان شرط میانی مهمی برای اثرگذاری رسانه است.",
            "مطالعات موردی می‌توانند سازوکار اثر را در بحران‌های واقعی آشکار کنند.",
        ],
        principles=[
            "اثر رسانه بر سیاست خارجی را نباید یکسان و همه‌جایی فرض کرد.",
            "سه گونهٔ اثر، یعنی تعیین دستور کار، واکنش کوتاه‌مدت و بازدارندگی، باید از هم تفکیک شوند.",
            "اجماع نخبگان و اطمینان سیاست، متغیرهای شرطی اصلی‌اند.",
            "اثر بازدارنده می‌تواند به محدودشدن خشونت یا به فلج‌شدن تصمیم بیانجامد.",
            "پوشش خبری ممکن است به ابزار مشروعیت‌بخشی به سیاست دولتی نیز تبدیل شود.",
            "تحلیل باید پوشش خبری و تصمیم رسمی را در بستر یک بحران مشخص بررسی کند.",
        ],
        critiques=[
            "جداسازی اثر رسانه از عوامل سیاسی و دیپلماتیک در عمل دشوار است.",
            "دولت‌ها می‌توانند با خبرسازی، اثر رسانه را به سود خود بسازند.",
            "شواهد مطالعات موردی ناهمگون و گاه متناقض است.",
            "عبارت اثر سیانان بیش از آنکه مفهوم نظری دقیقی باشد، برچسب رسانه‌ای است.",
            "تحول پلتفرم‌های دیجیتال، شرایط اثرگذاری خبری را از دوران پخش تلویزیونی دگرگون کرده است.",
        ],
        critique_text="منتقدان می‌گویند نظریهٔ سادهٔ «رسانه سیاست را می‌رانَد» با شواهد سازگار نیست و رابینسون خود این نتیجه را تأیید کرد. آنچه باقی می‌ماند، مدلی شرطی است: رسانه در فضای ابهام و شکاف نخبگان اثر می‌گذارد و در فضای اجماع، بیشتر بازتاب یا ابزار سیاست است. با این حال، همین مدل شرطی چارچوبی مفید برای تحلیل مداخلهٔ بشردوستانه فراهم می‌کند.",
        applications=[
            "تحلیل نقش رسانه در مداخلهٔ بشردوستانه و دیپلماسی بحران.",
            "بررسی تأثیر پوشش خبری بر تصمیم‌گیری دولت در بحران‌های بین‌المللی.",
            "طراحی سیاست رسانه‌ای در وزارت خارجه و نهادهای دیپلماتیک.",
            "آموزش خبرنگاران برای پوشش مسئولانهٔ بحران‌های انسانی.",
            "پژوهش تطبیقی دربارهٔ رابطهٔ خبر، افکار عمومی و سیاست خارجی.",
        ],
        example_text="در بحران کوزوو در سال ۱۹۹۹، پوشش گستردهٔ آوارگی و خشونت، فشار عمومی برای مداخلهٔ بشردوستانه را افزایش داد؛ اما رابینسون نشان داد این فشار تنها در شرایطی به سیاست تبدیل شد که دولت‌های غربی در اجماعی نسبی و سیاستی نامطمئن قرار داشتند. در بحران‌هایی که سیاست رسمی روشن بود، پوشش خبری بیشتر سیاست موجود را تقویت کرد و آن را تغییر نداد.",
        evolution="این اصطلاح در میانهٔ دههٔ ۱۹۹۰ در گفت‌وگوهای دیپلماتیک دربارهٔ جنگ خلیج فارس و سومالی رواج یافت و سپس در پژوهش‌های دانشگاهی به مفهومی تحلیلی تبدیل شد. رابینسون در سال ۱۹۹۹ مدل شرطی خود را معرفی کرد و در سال ۲۰۰۲ آن را در کتابی مستقل بسط داد. از دههٔ ۲۰۱۰ به بعد، پژوهش‌ها این پرسش را به محیط پلتفرم‌های دیجیتال و خبر شهروندی منتقل کرده‌اند.",
        key_concepts=["اثر سیانان", "اثر تعیین دستور کار", "اثر کوتاه‌مدت", "اثر بازدارنده", "اجماع نخبگان", "ابهام سیاست", "مداخلهٔ بشردوستانه"],
        theorists="پییرز رابینسون، استاد سیاست و رسانه، سازندهٔ مدل شرطی اثر سیانان است.",
        theorists_text="بحث اثر سیانان در سنت پژوهش دربارهٔ رابطهٔ رسانه، افکار عمومی و سیاست خارجی شکل گرفت و با مطالعات مداخلهٔ بشردوستانه و دیپلماسی رسانه‌ای پیوند خورد.",
        model="مدل شرطی: پوشش خبری زنده، فشار عمومی و پرسش خبرنگاران را می‌سازد؛ اگر سیاست رسمی نامطمئن و اجماع نخبگان ضعیف باشد، اثر در سطح تعیین دستور کار، واکنش کوتاه‌مدت یا بازدارندگی ظاهر می‌شود؛ اگر سیاست روشن و اجماع قوی باشد، رسانه ابزار اجرای سیاست می‌ماند.",
        studies=[
            "مقالهٔ سال ۱۹۹۹ سه‌گانهٔ اثرها را با شواهد بحران‌های دههٔ ۱۹۹۰ صورت‌بندی کرد.",
            "کتاب سال ۲۰۰۲ مدل شرطی را با مطالعهٔ تطبیقی مداخله‌ها بسط داد.",
            "پژوهش‌های بعدی دربارهٔ افکار عمومی و سیاست خارجی، وزن متغیرهای شرطی را آزمودند.",
            "مطالعات رسانهٔ دیجیتال، شرایط اثرگذاری خبری در محیط پلتفرم را بازخوانی کرده‌اند.",
        ],
    ),
    "MC-642": dict(
        year=2005,
        summary="چارچوب حاکمیت اینترنت، مجموعهٔ اصول، هنجارها، قواعد و رویه‌هایی است که تکامل و کاربرد اینترنت را شکل می‌دهد. صورت‌بندی رسمی آن در گزارش گروه کاری حاکمیت اینترنت در سال ۲۰۰۵ و سپس در دستور کار تونس اجلاس جهانی جامعهٔ اطلاعات دیده شد. تعریف رسمی، حاکمیت اینترنت را «تدوین و کاربرد اصول، هنجارها، قواعد و رویه‌های مشترک تصمیم‌گیری به‌دست دولت‌ها، بخش خصوصی و جامعهٔ مدنی در نقش‌های مربوط» می‌داند. این تعریف، مدل چندذی‌نفعی را بنیاد می‌گذارد: حکمرانی از بالا به پایین میان دولت‌ها، نهادهای فنی مانند سازمان‌های مدیریت نام و نشانی، بخش خصوصی و جامعهٔ مدنی تقسیم می‌شود. موضوع‌ها از زیرساخت فنی و منابع حیاتی مانند نام دامنه تا امنیت سایبری، حریم خصوصی، محتوا، شکاف دیجیتال و صلاحیت قضایی گسترده‌اند. نهادهای گوناگون، از سازمان‌های فنی جهانی تا مجمع حاکمیت اینترنت و اتحادیهٔ بین‌المللی مخابرات، در این فضا نقش دارند. پژوهش‌های بعدی نشان دادند که بسیاری از مناقشات حاکمیت، در واقع مناقشه بر سر زیرساخت‌اند: پروتکل‌ها، نام دامنه و مسیریابی داده، لایه‌هایی‌اند که قدرت و حقوق در آنها تعیین می‌شود. نقدهای اصلی به چارچوب، ابهام تعریف، نامتوازنی قدرت میان ذی‌نفعان، تنش میان حاکمیت دولتی و مدل چندذی‌نفعی و ضعف سازوکار اجرا مربوط می‌شود.",
        definition="حاکمیت اینترنت، چارچوب تدوین و کاربرد اصول، هنجارها، قواعد و رویه‌های مشترک تصمیم‌گیری به‌دست دولت‌ها، بخش خصوصی و جامعهٔ مدنی است که تکامل و کاربرد اینترنت را شکل می‌دهد.",
        main_problem="اینترنت به‌عنوان زیرساختی جهانی بدون حاکمیت مرکزی، چگونه اداره می‌شود و مرجعیت تصمیم‌گیری دربارهٔ منابع حیاتی، امنیت و حقوق کاربران میان دولت‌ها، نهادهای فنی و بازیگران خصوصی چگونه تقسیم می‌شود.",
        mechanism="حاکمیت در لایه‌های چندگانه عمل می‌کند: لایهٔ زیرساخت فنی و پروتکل‌ها، لایهٔ منابع حیاتی مانند نام دامنه و نشانی‌های شبکه، و لایهٔ محتوا و حقوق. در هر لایه، مجموعه‌ای از نهادها با سازوکارهای متفاوت تصمیم می‌گیرند و مشروعیت تصمیم از ترکیبی از توافق دولت‌ها، تخصص فنی و مشارکت ذی‌نفعان می‌آید. مدل چندذی‌نفعی، مذاکره و اجماع را جایگزین فرمان یک‌سویه می‌کند.",
        assumptions=[
            "اینترنت زیرساختی جهانی و چندلایه است که با یک مرکز فرماندهی اداره نمی‌شود.",
            "ذی‌نفعان متعدد، از دولت تا کاربر، در حکمرانی نقش مشروع دارند.",
            "تصمیم‌های فنی دربارهٔ پروتکل و زیرساخت، پیامدهای اجتماعی و حقوقی دارند.",
            "هماهنگی میان نهادها می‌تواند از چندپارگی شبکه جلوگیری کند.",
            "مشروعیت تصمیم به شفافیت و مشارکت ذی‌نفعان وابسته است.",
        ],
        principles=[
            "حاکمیت اینترنت باید چندذی‌نفعی و شفاف باشد.",
            "باز بودن، قابلیت هم‌کنش و امنیت شبکه باید حفظ شود.",
            "منابع حیاتی اینترنت باید با رویه‌های قابل پیش‌بینی اداره شوند.",
            "حقوق کاربران و حریم خصوصی بخشی از دستور کار حاکمیت است.",
            "همکاری بین‌المللی برای جلوگیری از چندپارگی ضروری است.",
            "تصمیم فنی و تصمیم سیاسی باید در گفت‌وگوی مستمر باشند.",
        ],
        critiques=[
            "تعریف رسمی گسترده و در عمل مبهم است.",
            "قدرت واقعی میان ذی‌نفعان نامتوازن است و بازیگران مسلط، دستور کار را تعیین می‌کنند.",
            "تنش میان حاکمیت دولتی و مدل چندذی‌نفعی حل‌نشده مانده است.",
            "سازوکارهای اجرا و پاسخ‌گویی ضعیف‌اند.",
            "خطر چندپارگی اینترنت و بازگشت به مرزهای ملی جدی است.",
        ],
        critique_text="منتقدان می‌گویند مدل چندذی‌نفعی در سطح گفتار فراگیر است اما در سطح تصمیم، توازن قدرت را بازتولید می‌کند؛ دولت‌های قدرتمند و شرکت‌های بزرگ فناوری بیشترین نفوذ را دارند و جامعهٔ مدنی اغلب در حاشیه می‌ماند. با این حال، همین چارچوب زبان مشترکی برای گفت‌وگوی جهانی دربارهٔ زیرساخت، حقوق و امنیت فراهم کرده است.",
        applications=[
            "تحلیل سیاست رسانه و پلتفرم در سطح ملی و جهانی.",
            "پژوهش دربارهٔ آزادی بیان، حریم خصوصی و حاکمیت داده.",
            "طراحی مجامع ملی و منطقه‌ای حاکمیت اینترنت.",
            "تحلیل مناقشات مربوط به فیلترینگ، نام دامنه و مسیریابی داده.",
            "آموزش حقوق رسانه و سیاست فناوری.",
        ],
        example_text="مناقشه بر سر مدیریت نام دامنه و نشانی‌های شبکه نشان می‌دهد چگونه یک تصمیم فنی به موضوعی سیاسی بدل می‌شود: نهادی فنی مدیریت را بر عهده دارد، دولت‌ها بر مرزهای ملی و حاکمیت داده تأکید می‌کنند و جامعهٔ مدنی بر شفافیت و حقوق کاربران پافشاری می‌کند. چارچوب حاکمیت اینترنت، زبان و رویهٔ گفت‌وگو میان این سه دستهٔ بازیگر را فراهم می‌کند.",
        evolution="در دههٔ ۱۹۹۰ حاکمیت اینترنت بیشتر خودگردان و فنی بود. در سال ۲۰۰۵ گروه کاری سازمان ملل تعریف رسمی را ارائه کرد و اجلاس جهانی جامعهٔ اطلاعات آن را پذیرفت. از سال ۲۰۰۶ مجمع سالانهٔ حاکمیت اینترنت به کار افتاد و از دههٔ ۲۰۱۰ بحث قدرت پلتفرم‌ها، امنیت سایبری و چندپارگی، دستور کار را گسترش داد.",
        key_concepts=["حاکمیت چندذی‌نفعی", "منابع حیاتی", "لایهٔ زیرساخت", "چندپارگی اینترنت", "سیاست پلتفرم", "حریم خصوصی", "شکاف دیجیتال"],
        theorists="گروه کاری حاکمیت اینترنت، سازندهٔ تعریف رسمی؛ لورا دیناردیس، پژوهشگر حاکمیت مبتنی بر زیرساخت؛ و نهادهای فنی جهانی مانند سازمان‌های مدیریت نام و نشانی.",
        theorists_text="این چارچوب در گفت‌وگوی میان حقوق بین‌الملل، سیاست فناوری و جامعهٔ مدنی شکل گرفت و بعدها با پژوهش‌های اقتصاد سیاسی پلتفرم گسترش یافت.",
        model="مدل لایه‌ای چندذی‌نفعی: لایهٔ فنی و پروتکل، لایهٔ منابع حیاتی، و لایهٔ محتوا و حقوق؛ در هر لایه، دولت‌ها، نهادهای فنی، بخش خصوصی و جامعهٔ مدنی با رویه‌های مذاکره و اجماع تصمیم می‌گیرند.",
        studies=[
            "گزارش سال ۲۰۰۵ گروه کاری، تعریف رسمی و مدل چندذی‌نفعی را صورت‌بندی کرد.",
            "دستور کار تونس در سال ۲۰۰۵ تعریف را در سند بین‌دولتی تثبیت کرد.",
            "پژوهش‌های دههٔ ۲۰۱۰ نشان دادند مناقشات حاکمیت در لایهٔ زیرساخت رخ می‌دهند.",
            "مطالعات بعدی دربارهٔ چندپارگی، مرزهای ملی و قدرت پلتفرم را بررسی کرده‌اند.",
        ],
    ),
    "MC-645": dict(
        year=2012,
        summary="نظریهٔ یکپارچهٔ پذیرش و کاربرد فناوری در نسخهٔ دوم، مدلی برای توضیح پذیرش فناوری به‌دست مصرف‌کننده است که ویشوانات ونکاتش، جیمز تونگ و شین شو آن را در سال ۲۰۱۲ در فصل‌نامهٔ سیستم‌های اطلاعاتی مدیریت منتشر کردند. نسخهٔ نخست این نظریه در سال ۲۰۰۳ چند مدل پذیرش فناوری را در هم ادغام کرده بود و برای کارکنان سازمانی ساخته شده بود. نسخهٔ دوم زمینهٔ مصرف شخصی و سرگرمی را هدف گرفت و سه سازهٔ تازه افزود: انگیزهٔ لذت‌جویانه، یعنی لذت و شادی استفاده؛ ارزش قیمتی، یعنی سنجش فایده در برابر هزینهٔ پولی؛ و عادت، یعنی رفتار خودکار پس از تکرار استفاده. چهار سازهٔ پایه نیز حفظ شد: انتظار عملکرد، انتظار تلاش، تأثیر اجتماعی و شرایط تسهیل‌کننده. سن، جنسیت و تجربهٔ پیشین، اثر سازه‌ها را تعدیل می‌کنند. در مطالعهٔ اصلی، مدل حدود هفتاد درصد از واریانس قصد رفتاری و بیش از نیمی از واریانس استفادهٔ واقعی را توضیح داد. کاربرد رسانه‌ای آن در تحلیل پذیرش اپلیکیشن خبری، پیام‌رسان و سرویس پخش ویدئو است: پذیرش مصرف‌کننده تنها به سودمندی و سهولت وابسته نیست، بلکه به لذت، قیمت و عادت نیز بستگی دارد. نقدهای اصلی به مقطعی بودن داده‌ها، اتکا به خودگزارشی، نمونهٔ غربی، سنجش مبهم عادت و توان محدود پیش‌بینی در بافت‌های فرهنگی متفاوت مربوط می‌شود.",
        definition="نظریهٔ یکپارچهٔ پذیرش و کاربرد فناوری در نسخهٔ دوم، مدلی است که قصد و رفتار استفادهٔ مصرف‌کنندگان از فناوری را با چهار سازهٔ پایه و سه سازهٔ افزوده، یعنی انگیزهٔ لذت‌جویانه، ارزش قیمتی و عادت، توضیح می‌دهد.",
        main_problem="چرا مصرف‌کنندگان عادی، برخلاف کارکنان سازمانی، فناوری‌هایی مانند پیام‌رسان، اپلیکیشن خبری و سرویس سرگرمی را می‌پذیرند یا کنار می‌گذارند، و چه عواملی فراتر از سودمندی و سهولت در این تصمیم نقش دارند.",
        mechanism="چهار سازهٔ پایه، قصد رفتاری را می‌سازند و سه سازهٔ تازه آن را در بافت مصرف گسترش می‌دهند: لذت استفاده قصد را بالا می‌برد، ارزش قیمتی فایدهٔ درک‌شده را با هزینه می‌سنجد و عادت، رفتار را از تصمیم آگاهانه به واکنش خودکار تبدیل می‌کند. سن، جنسیت و تجربهٔ استفاده، قدرت این اثرها را تعدیل می‌کنند.",
        assumptions=[
            "قصد رفتاری پیش‌بین معتبر استفادهٔ واقعی است.",
            "سازه‌های ادراکی، یعنی باورها و انتظارات کاربر، رفتار آینده را شکل می‌دهند.",
            "بافت مصرف شخصی با بافت سازمانی تفاوت دارد و سازه‌های تازه لازم است.",
            "اثر سازه‌ها میان گروه‌های سنی، جنسیتی و تجربی متفاوت است.",
            "عادت پس از تکرار استفاده شکل می‌گیرد و پایدار می‌ماند.",
        ],
        principles=[
            "پذیرش مصرف‌کننده را باید با مدلی مخصوص بافت مصرف سنجید.",
            "لذت و ارزش قیمتی در فناوری‌های سرگرمی و رسانه‌ای وزن بالایی دارند.",
            "عادت، پس از تکرار، نقش تصمیم آگاهانه را کم‌رنگ می‌کند.",
            "تأثیر اجتماعی در مراحل نخست پذیرش قوی‌تر است.",
            "شرایط تسهیل‌کننده، به‌ویژه دسترسی و پشتیبانی، استفاده را ممکن می‌کند.",
            "تفاوت‌های جمعیتی باید در تفسیر نتایج لحاظ شوند.",
        ],
        critiques=[
            "داده‌های مقطعی، رابطهٔ علت و معلول را به‌سختی اثبات می‌کنند.",
            "اتکا به خودگزارشی، خطر سوگیری پاسخ را دارد.",
            "نمونهٔ اصلی آمریکایی است و تعمیم فرهنگی آن محدود است.",
            "سنجش عادت با پرسش‌های خودگزارشی مبهم و ناپایدار است.",
            "توان پیش‌بینی مدل در بافت‌های کم‌درآمد و کاربران تازه دیجیتال کمتر است.",
        ],
        critique_text="منتقدان می‌گویند نسخهٔ دوم با افزودن سازه‌ها، قدرت توضیحی را بالا برد اما مدل را پیچیده‌تر و آزمون‌پذیری را دشوارتر کرد؛ برخی پژوهش‌ها نیز نشان داده‌اند وزن سازه‌ها در کشورها و فرهنگ‌های مختلف تفاوت چشمگیری دارد. با این حال، مدل همچنان پرکاربردترین چارچوب پذیرش فناوری در پژوهش رسانه و فناوری است.",
        applications=[
            "تحلیل پذیرش اپلیکیشن‌های خبری و پیام‌رسان‌ها.",
            "طراحی تجربهٔ کاربری سرویس‌های رسانه‌ای با تأکید بر لذت و ارزش قیمتی.",
            "پژوهش شکاف دیجیتال و موانع استفادهٔ گروه‌های کم‌دسترس.",
            "ارزیابی پذیرش رسانه‌های عمومی و خدمات دیجیتال دولتی.",
            "برنامه‌ریزی کمپین‌های تشویق به استفاده از خدمات آنلاین.",
        ],
        example_text="یک اپلیکیشن خبری تازه ممکن است از نظر سودمندی و سهولت امتیاز خوبی بگیرد، اما اگر تجربهٔ استفاده لذت‌بخش نباشد، هزینهٔ اشتراک با ارزش ادراک‌شده هم‌خوان نباشد یا عادت روزانهٔ مطالعهٔ خبر شکل نگیرد، استفادهٔ پایدار رخ نمی‌دهد. مدل نسخهٔ دوم توضیح می‌دهد چرا برخی سرویس‌ها با وجود فایدهٔ روشن، کنار گذاشته می‌شوند.",
        evolution="مدل پذیرش فناوری در سال ۱۹۸۹ با تأکید بر سودمندی و سهولت ادراک‌شده آغاز شد، در سال ۲۰۰۳ در قالب نظریهٔ یکپارچه با چهار سازه و متغیرهای تعدیل‌گر بازآرایی شد و در سال ۲۰۱۲ نسخهٔ دوم با سه سازهٔ مصرفی بسط یافت. پژوهش‌های بعدی، مدل را به بافت‌های فرهنگی گوناگون و فناوری‌های تازه‌تر مانند دستیارهای هوشمند و واقعیت مجازی گستردند.",
        key_concepts=["انتظار عملکرد", "انتظار تلاش", "تأثیر اجتماعی", "شرایط تسهیل‌کننده", "انگیزهٔ لذت‌جویانه", "ارزش قیمتی", "عادت", "قصد رفتاری"],
        theorists="ویشوانات ونکاتش، جیمز تونگ و شین شو، سازندگان نسخهٔ دوم؛ فرد دیویس، بنیان‌گذار مدل پذیرش فناوری که سنت این پژوهش را آغاز کرد.",
        theorists_text="این سنت پژوهشی در سیستم‌های اطلاعاتی و روان‌شناسی فناوری شکل گرفت و بعدها به پژوهش رسانه و ارتباطات راه یافت.",
        model="مدل مسیرمحور: چهار سازهٔ پایه و سه سازهٔ مصرفی بر قصد رفتاری اثر می‌گذارند و قصد، استفادهٔ واقعی را پیش‌بینی می‌کند؛ سن، جنسیت و تجربه، شدت این مسیرها را تعدیل می‌کنند.",
        studies=[
            "مقالهٔ سال ۲۰۱۲ نسخهٔ دوم را با سه سازهٔ تازه و آزمون میدانی معرفی کرد.",
            "مقالهٔ سال ۲۰۰۳ نسخهٔ یکپارچهٔ نخست را با ترکیب چند مدل پذیرش ساخت.",
            "پژوهش‌های تطبیقی، وزن متفاوت سازه‌ها در فرهنگ‌های گوناگون را نشان دادند.",
            "مطالعات رسانه، مدل را برای پذیرش اپلیکیشن و سرویس‌های محتوایی به کار بردند.",
        ],
    ),
    "MC-647": dict(
        year=1999,
        summary="بازواسازی رسانه، نظریه‌ای است که جی دیوید بولتر و ریچارد گروزین در کتاب سال ۱۹۹۹ با عنوان بازواسازی: فهم رسانه‌های نو ارائه کردند. ایدهٔ مرکزی این است که رسانه‌های تازه هرگز از هیچ آغاز نمی‌شوند؛ آنها رسانه‌های پیشین را بازنمایی، بازسازی و اصلاح می‌کنند و هویت خود را با ارجاع به آنها می‌سازند. عکاسی نقاشی را بازواسازی کرد، سینما تئاتر و عکاسی را، و رسانه‌های دیجیتال همهٔ رسانه‌های پیشین را. بازواسازی دو منطق هم‌زمان دارد: بی‌واسطگی، یعنی کوشش برای پنهان‌کردن خود واسطه تا تجربهٔ مستقیم واقعیت ساخته شود؛ و فراواسطگی، یعنی انبوه‌کردن پنجره‌ها و واسطه‌های دیداری و پذیرش آشکار واسطه‌گری. رسانه‌های نو میان این دو منطق نوسان می‌کنند و هر بازواسازی، خود موضوع بازواسازی بعدی می‌شود. اهمیت این نظریه در تحلیل رسانه است: صفحهٔ یک وبگاه خبری که ویدئوی زنده، متن، عکس و جریان شبکهٔ اجتماعی را در هم می‌آمیزد، نمونه‌ای از فراواسطگی است، در حالی که لنز دوربین و صفحهٔ تمام‌صفحه می‌کوشند واسطه را نامرئی کنند. نقدهای اصلی به این نظریه، ادعای جهان‌شمول و تاریخی‌نگرانه، ابهام مفهومی، کم‌توجهی به اقتصاد سیاسی رسانه و خطر فناوری‌محوری مربوط می‌شود.",
        definition="بازواسازی رسانه، فرایندی است که در آن رسانه‌های تازه رسانه‌های پیشین را بازنمایی، بازسازی و اصلاح می‌کنند و هویت خود را با ارجاع به آنها می‌سازند.",
        main_problem="رسانه‌های تازه چگونه با رسانه‌های پیشین نسبت برقرار می‌کنند و چه منطقی بر این نسبت حاکم است، در حالی که هر نسل رسانه ادعای تازگی و بی‌واسطگی دارد.",
        mechanism="دو منطق در بازواسازی هم‌زمان عمل می‌کنند. منطق بی‌واسطگی، واسطه را پنهان می‌کند تا کاربر تجربهٔ مستقیم داشته باشد: دوربین نامرئی، صفحهٔ تمام‌صفحه و رابط کاربری ساده. منطق فراواسطگی، واسطه‌ها را آشکار و انبوه می‌کند: چند پنجره، لایه‌های متن و تصویر و پیوند. رسانهٔ نو میان این دو نوسان می‌کند و در همان حال رسانهٔ پیشین را جذب و بازآرایی می‌کند؛ این چرخه در نسل‌های بعدی تکرار می‌شود.",
        assumptions=[
            "هیچ رسانه‌ای بدون ارجاع به رسانه‌های پیشین شکل نمی‌گیرد.",
            "کوشش برای بی‌واسطگی، خود نوعی واسطه‌گری است.",
            "فراواسطگی و بی‌واسطگی دو قطب یک پیوستارند و نه دو دورهٔ تاریخی.",
            "مفهوم رسانه شامل ابزار، فن و رویهٔ فرهنگی است.",
            "تحلیل تاریخی رسانه‌ها می‌تواند منطق رسانه‌های نو را روشن کند.",
        ],
        principles=[
            "رسانهٔ نو را باید در نسب‌نامهٔ رسانه‌ای آن فهمید.",
            "بی‌واسطگی و فراواسطگی هم‌زمان حضور دارند.",
            "بازواسازی فرایندی دوسویه است: رسانهٔ نو رسانهٔ کهن را جذب می‌کند و رسانهٔ کهن نیز بازآرایی می‌شود.",
            "تجربهٔ بی‌واسطگی، محصول طراحی است و نه غیاب واقعی واسطه.",
            "هر بازواسازی، زمینهٔ بازواسازی بعدی را می‌سازد.",
            "تحلیل رسانه باید فرم، تجربهٔ کاربر و نسب‌نامهٔ تاریخی را با هم ببیند.",
        ],
        critiques=[
            "ادعای جهان‌شمولی و تاریخی‌نگرانهٔ بی‌واسطگی، شواهد کافی ندارد.",
            "مرز میان بازواسازی و سایر اشکال وام‌گیری رسانه‌ای مبهم است.",
            "اقتصاد سیاسی و روابط قدرت در تحلیل کم‌رنگ می‌شود.",
            "خطر فناوری‌محوری و کم‌توجهی به مخاطب فعال وجود دارد.",
            "کاربرد مفهوم برای همهٔ رسانه‌ها آن را به اصطلاحی کشسان تبدیل می‌کند.",
        ],
        critique_text="منتقدان می‌گویند بولتر و گروزین میل به بی‌واسطگی را به همهٔ دوره‌های رسانه‌ای تعمیم می‌دهند، بی‌آنکه شواهد تاریخی کافی برای این ادعا بیاورند و بی‌آنکه نقش قدرت، مالکیت و بازار را در شکل‌گیری رسانه‌ها توضیح دهند. با این حال، مفهوم بازواسازی ابزار تحلیلی نیرومندی برای فهم پیوند رسانه‌های نو با رسانه‌های پیشین فراهم کرده است.",
        applications=[
            "تحلیل طراحی وبگاه‌های خبری و اپلیکیشن‌های رسانه‌ای.",
            "پژوهش دربارهٔ واقعیت مجازی، واقعیت افزوده و بازی‌های دیجیتال.",
            "تحلیل ترارسانانه و بازآرایی محتوا در چند رسانه.",
            "مطالعات باستان‌شناسی رسانه و تاریخ فناوری‌های ارتباطی.",
            "آموزش طراحی تجربهٔ کاربری با توجه به منطق بی‌واسطگی و فراواسطگی.",
        ],
        example_text="یک وبگاه خبری مدرن هم‌زمان دو منطق را نمایش می‌دهد: پخش زنده با لنز دوربین می‌کوشد واسطه را نامرئی کند و حس حضور مستقیم بسازد؛ و در همان صفحه، جریان شبکهٔ اجتماعی، نمودار، پیوند و ویدئوی کوتاه لایه‌های واسطه را انبوه می‌کنند. طراحی خوب، میان این دو منطق تعادل می‌سازد.",
        evolution="ریشهٔ بحث به اندیشهٔ مارشال مک‌لوهان دربارهٔ رسانه به‌عنوان امتداد انسان بازمی‌گردد. بولتر و گروزین در سال ۱۹۹۹ مفهوم بازواسازی و دوگانهٔ بی‌واسطگی و فراواسطگی را صورت‌بندی کردند. بعدها این مفهوم در مطالعات بازی، خبر دیجیتال، واقعیت مجازی و باستان‌شناسی رسانه به کار رفت و در دههٔ ۲۰۱۰ با بحث بازآرایی محتوا در پلتفرم‌ها گسترش یافت.",
        key_concepts=["بازواسازی", "بی‌واسطگی", "فراواسطگی", "منطق دوگانه", "نسب‌نامهٔ رسانه", "بازواسازی متقابل"],
        theorists="جی دیوید بولتر و ریچارد گروزین، سازندگان نظریهٔ بازواسازی؛ و مارشال مک‌لوهان، پیشگام تحلیل رسانه به‌عنوان امتداد انسان.",
        theorists_text="این نظریه در سنت مطالعات رسانه و نقد فناوری شکل گرفت و با تاریخ رسانه و مطالعات بصری پیوند خورد.",
        model="مدل دو‌قطبی: رسانهٔ نو رسانهٔ کهن را بازواسازی می‌کند و میان قطب بی‌واسطگی، یعنی پنهان‌سازی واسطه، و قطب فراواسطگی، یعنی انبوه‌سازی و آشکارسازی واسطه‌ها، نوسان می‌کند؛ هر دورهٔ بازواسازی، مواد دورهٔ بعد را فراهم می‌کند.",
        studies=[
            "کتاب سال ۱۹۹۹ دوگانهٔ بی‌واسطگی و فراواسطگی را با نمونه‌های تاریخی رسانه صورت‌بندی کرد.",
            "مطالعات بعدی، مفهوم را به بازی‌های دیجیتال و واقعیت مجازی گستردند.",
            "پژوهش خبر دیجیتال، بازواسازی تلویزیون در وب را تحلیل کرد.",
            "باستان‌شناسی رسانه، نسب‌نامهٔ رسانه‌ای بازواسازی را در دورهٔ پیش از دیجیتال بررسی کرد.",
        ],
    ),
}

NAME_FIX = {
    "MC-645": ("نظریهٔ یکپارچهٔ پذیرش و کاربرد فناوری (نسخهٔ دوم)",
               "UTAUT2 (Unified Theory of Acceptance and Use of Technology 2)",
               "name normalized from bare acronym to Persian descriptive title"),
    "MC-647": ("بازواسازی رسانه (ترمیم‌گری)", "Media Remediation",
               "name normalized: slash form replaced with descriptive Persian title"),
}

YEAR_FIX = {
    "MC-638": "year corrected 1997 -> 1999 (verified anchor: Robinson, The CNN Effect, Review of International Studies 25(2), 1999); note: editorial card core_logic was a mismatched media-governance template, documentation rebuilt from Robinson (1999)",
    "MC-642": "year corrected 2000 -> 2005 (verified anchor: WGIG report and Tunis Agenda, 2005); note: editorial card had no theorist and a generic governance template, documentation rebuilt from the WGIG report (2005)",
    "MC-645": "no year change; note: editorial card core_logic was a mismatched network-society template, documentation rebuilt from Venkatesh, Thong & Xu (2012)",
    "MC-647": "no year change; note: editorial card core_logic was a mismatched network-society template, documentation rebuilt from Bolter & Grusin (1999)",
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
                                       "verified": n_verified, "batch": 125}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH125 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
