# -*- coding: utf-8 -*-
"""Batch 134 (MODEL): full documentation for MC-143, MC-156, MC-173, MC-174."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch134-model-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch134_model.json"

S = {
    "MC-143": [
        dict(kind="BOOK",
             title_en="The Presentation of Self in Everyday Life",
             title_fa="ارائهٔ خود در زندگی روزمره",
             authors="Goffman, E.", year=1959,
             publisher="Doubleday (Anchor Books)",
             doi=None,
             url="https://monoskop.org/images/1/19/Goffman_Erving_The_Presentation_of_Self_in_Everyday_Life.pdf",
             language="en", isbn=None,
             citation="Goffman, E. (1959). The Presentation of Self in Everyday Life. Garden City, NY: Doubleday.",
             locator="book", locator_type="SECTION",
             supports="dramaturgical model with front stage and back stage", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="On Face-Work: An Analysis of Ritual Elements in Social Interaction",
             title_fa="دربارهٔ حفظ آبرو: تحلیلی از عناصر آیینی تعامل اجتماعی",
             authors="Goffman, E.", year=1955,
             publisher="Psychiatry",
             doi=None, url=None, language="en", isbn=None,
             citation="Goffman, E. (1955). On face-work: An analysis of ritual elements in social interaction. Psychiatry, 18(3), 213-231.",
             locator="18(3):213-231", locator_type="page_range",
             supports="face-work as ritual management of self in interaction", verified=False),
    ],
    "MC-156": [
        dict(kind="BOOK",
             title_en="The Nature of Managerial Work",
             title_fa="ماهیت کار مدیریتی",
             authors="Mintzberg, H.", year=1973,
             publisher="Harper & Row",
             doi=None,
             url="https://hib510week9.pbworks.com/f/The+Nature+of+Managerial+Work,+Mintzberg+1973.pdf",
             language="en", isbn=None,
             citation="Mintzberg, H. (1973). The Nature of Managerial Work. New York: Harper & Row.",
             locator="book", locator_type="SECTION",
             supports="ten managerial roles in three categories", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Manager's Job: Folklore and Fact",
             title_fa="کار مدیر: افسانه و واقعیت",
             authors="Mintzberg, H.", year=1975,
             publisher="Harvard Business Review",
             doi=None, url=None, language="en", isbn=None,
             citation="Mintzberg, H. (1975). The manager's job: Folklore and fact. Harvard Business Review, 53(4), 49-61.",
             locator="53(4):49-61", locator_type="page_range",
             supports="empirical description of fragmented managerial work", verified=False),
    ],
    "MC-173": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="International Investment and International Trade in the Product Cycle",
             title_fa="سرمایه‌گذاری بین‌المللی و تجارت بین‌المللی در چرخهٔ عمر محصول",
             authors="Vernon, R.", year=1966,
             publisher="The Quarterly Journal of Economics",
             doi=None,
             url="https://academic.oup.com/qje/article-abstract/80/2/190/1868595",
             language="en", isbn=None,
             citation="Vernon, R. (1966). International investment and international trade in the product cycle. The Quarterly Journal of Economics, 80(2), 190-207.",
             locator="80(2):190-207", locator_type="page_range",
             supports="product cycle theory of trade and investment", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Exploit the Product Life Cycle",
             title_fa="بهره‌گیری از چرخهٔ عمر محصول",
             authors="Levitt, T.", year=1965,
             publisher="Harvard Business Review",
             doi=None, url=None, language="en", isbn=None,
             citation="Levitt, T. (1965). Exploit the product life cycle. Harvard Business Review, 43(6), 81-94.",
             locator="43(6):81-94", locator_type="page_range",
             supports="managerial strategy across product life cycle stages", verified=False),
    ],
    "MC-174": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Strategies for Diversification",
             title_fa="راهبردهای تنوع‌بخشی",
             authors="Ansoff, H. I.", year=1957,
             publisher="Harvard Business Review",
             doi=None,
             url="https://www.casrilanka.com/casl/images/stories/2017/2017_pdfs/sab_portal/course_material/strategies_for_diversification.pdf",
             language="en", isbn=None,
             citation="Ansoff, H. I. (1957). Strategies for diversification. Harvard Business Review, 35(5), 113-124.",
             locator="35(5):113-124", locator_type="page_range",
             supports="market/product growth matrix with four strategies", verified=True),
        dict(kind="BOOK",
             title_en="Corporate Strategy: An Analytic Approach to Business Policy for Growth and Expansion",
             title_fa="راهبرد شرکتی: رویکردی تحلیلی به سیاست کسب‌وکار برای رشد و گسترش",
             authors="Ansoff, H. I.", year=1965,
             publisher="McGraw-Hill",
             doi=None, url=None, language="en", isbn=None,
             citation="Ansoff, H. I. (1965). Corporate Strategy: An Analytic Approach to Business Policy for Growth and Expansion. New York: McGraw-Hill.",
             locator="book", locator_type="SECTION",
             supports="systematic development of the growth-vector framework", verified=False),
    ],
}

ENRICH = {
    "MC-143": dict(
        year=1959,
        summary="مدیریت برداشت، چارچوبی در جامعه‌شناسی تعامل است که اروینگ گافمن در کتاب ارائهٔ خود در زندگی روزمره در سال ۱۹۵۹ صورت‌بندی کرد. ادعای مرکزی این است که تعامل اجتماعی را می‌توان مانند یک نمایش تحلیل کرد: افراد در «صحنهٔ جلو» تلاش می‌کنند تصویر مطلوبی از خود ارائه دهند، با ظاهر، رفتار و ابزار مناسب نقش، و در «پشت صحنه» آماده‌سازی می‌کنند و از نقش خارج می‌شوند. نمایش، تیمی برای هماهنگی میان اجراکنندگان و مدیریت برداشت تماشاگران است؛ ناهماهنگی صحنهٔ جلو و پشت صحنه، افشای پشت صحنه یا شکست در حفظ ظاهر می‌تواند اعتبار فرد را فرو بریزد. گافمن در مقالهٔ پیشین خود دربارهٔ حفظ آبرو هم نشان داده بود که افراد در تعامل، با آیین‌های پرهیز و ترمیم، تصویر اجتماعی خود و دیگری را حفظ می‌کنند. این چارچوب در تحلیل روابط عمومی، ارتباطات سیاسی، برندسازی شخصی و رسانهٔ اجتماعی کاربرد گسترده دارد و سازمان‌ها نیز صحنهٔ جلو و پشت صحنهٔ خود را مدیریت می‌کنند. نقدهای اصلی به آن، ابهام مرز صحنه‌ها، کم‌توجهی به قدرت ساختاری و دشواری جداکردن مدیریت برداشت راهبردی از بیان اصیل خود مربوط می‌شود.",
        definition="مدیریت برداشت، فرایندی است که در آن افراد و سازمان‌ها با اجرای نمایشی در صحنهٔ جلو و آماده‌سازی در پشت صحنه، تلاش می‌کنند تصویر مطلوبی از خود در ذهن دیگران بسازند.",
        main_problem="افراد چگونه در تعامل روزمره، تصویر خود را کنترل می‌کنند، و چه اتفاقی می‌افتد وقتی صحنهٔ جلو و پشت صحنه با هم ناسازگار شوند.",
        mechanism="فرد با انتخاب ظاهر، لحن، اطلاعات و ابزار، نقش خود را در صحنهٔ جلو اجرا می‌کند؛ تیم اجرا با هماهنگی، برداشت تماشاگر را هدایت می‌کند. پشت صحنه، محل آماده‌سازی و رهایی از نقش است؛ افشای آن یا ناهماهنگی با صحنهٔ جلو، اعتبار اجرا را تخریب می‌کند.",
        assumptions=[
            "تعامل اجتماعی را می‌توان به‌مثابهٔ نمایش تحلیل کرد.",
            "افراد در پی ارائهٔ تصویری مطلوب از خود هستند.",
            "صحنهٔ جلو و پشت صحنه از هم متمایزند.",
            "برداشت دیگران، محصول اجرا و هماهنگی تیمی است.",
            "ناهماهنگی صحنه‌ها، اعتبار را تهدید می‌کند.",
        ],
        principles=[
            "تعامل را باید در قالب اجرا، نقش و صحنه فهمید.",
            "ظاهر و رفتار، ابزار مدیریت برداشت‌اند.",
            "پشت صحنه، شرط آماده‌سازی اجرای صحنهٔ جلو است.",
            "افشای پشت صحنه، اعتبار اجرا را به خطر می‌اندازد.",
            "حفظ آبرو، آیینی تعاملی و دوسویه است.",
            "سازمان‌ها نیز صحنهٔ جلو و پشت صحنهٔ خود را مدیریت می‌کنند.",
        ],
        critiques=[
            "مرز صحنهٔ جلو و پشت صحنه همیشه روشن نیست.",
            "نقش قدرت و نابرابری ساختاری کم‌بررسی می‌ماند.",
            "مدیریت برداشت راهبردی با بیان اصیل خود خلط می‌شود.",
            "در محیط دیجیتال، مرز صحنه‌ها مبهم‌تر شده است.",
            "سنجش تجربی برداشت تماشاگر دشوار است.",
        ],
        critique_text="منتقدان می‌گویند چارچوب نمایشی گافمن توصیفی غنی از تعامل روزمره فراهم کرد اما مرز صحنه‌ها را مبهم می‌گذارد و نقش قدرت و ساختار را کم‌رنگ می‌کند؛ در رسانهٔ اجتماعی نیز مرز صحنهٔ جلو و پشت صحنه چنان درهم‌تنیده شده که کاربرد مدل را پیچیده کرده است. با این حال، همچنان چارچوب بنیادی تحلیل خود و برداشت است.",
        applications=[
            "تحلیل ارتباطات سیاسی و تصویر نامزدها.",
            "برندسازی شخصی و مدیریت شهرت.",
            "تحلیل رفتار سازمانی و روابط عمومی.",
            "پژوهش هویت و خودارائه‌گری در رسانهٔ اجتماعی.",
            "آموزش ارتباطات بین‌فردی و مدیریت بحران اعتبار.",
        ],
        example_text="یک سیاستمدار در سخنرانی عمومی با لباس و لحن مناسب، تصویر «رهبر توانمند» را در صحنهٔ جلو اجرا می‌کند؛ اما اگر ویدئوی پشت صحنه‌ای منتشر شود که لحن و رفتار متفاوتی را نشان دهد، برداشت مخاطبان فرو می‌ریزد. مدیریت برداشت همین رابطهٔ صحنه‌ها را توضیح می‌دهد.",
        evolution="ریشهٔ چارچوب در جامعه‌شناسی تعامل و مقالهٔ حفظ آبرو در سال ۱۹۵۵ است. کتاب سال ۱۹۵۹ نسخهٔ نمایشی را تثبیت کرد و پژوهش‌های بعدی، آن را به رسانهٔ اجتماعی، برندسازی و ارتباطات سازمانی گستردند.",
        key_concepts=["صحنهٔ جلو", "پشت صحنه", "اجرا", "مدیریت برداشت", "حفظ آبرو", "تیم نمایش"],
        theorists="اروینگ گافمن، صورت‌بند چارچوب نمایشی و مدیریت برداشت.",
        theorists_text="این چارچوب در سنت جامعه‌شناسی تعامل نمادین و تحلیل نمایشی شکل گرفت.",
        model="مدل نمایشی: اجرا در صحنهٔ جلو با ظاهر و رفتار مناسب، آماده‌سازی در پشت صحنه، هماهنگی تیم نمایش و مدیریت برداشت تماشاگر؛ ناهماهنگی صحنه‌ها به از دست رفتن اعتبار می‌انجامد.",
        studies=[
            "کتاب سال ۱۹۵۹ چارچوب نمایشی را تثبیت کرد.",
            "پژوهش‌های تعامل، حفظ آبرو و آیین‌های ترمیم را بررسی کردند.",
            "مطالعات رسانهٔ اجتماعی، خودارائه‌گری دیجیتال را با مدل تحلیل کردند.",
            "پژوهش ارتباطات سیاسی، مدیریت تصویر را در کمپین‌ها آزمود.",
        ],
    ),
    "MC-156": dict(
        year=1973,
        summary="نقش‌های مدیریتی، مدلی توصیفی از کار مدیر است که هنری مینتزبرگ در کتاب ماهیت کار مدیریتی در سال ۱۹۷۳ و مقالهٔ کار مدیر: افسانه و واقعیت در سال ۱۹۷۵ ارائه کرد. ادعای مرکزی این است که کار مدیریت، برخلاف تصور کلاسیک برنامه‌ریزی، سازمان‌دهی و کنترل، پیوسته، کوتاه‌مدت و پراکنده است و بیشتر با وقفه، ارتباط شفاهی و واکنش به رویدادها انجام می‌شود. مینتزبرگ با مشاهدهٔ مستقیم مدیران، ده نقش را در سه دستهٔ بین‌فردی (نمادین، رهبر، رابط)، اطلاعاتی (پایشگر، انتشاردهنده، سخنگو) و تصمیم‌گیری (کارآفرین، حل‌کنندهٔ اختلال، تخصیص‌دهندهٔ منابع، مذاکره‌کننده) گروه‌بندی کرد. این نقش‌ها به‌طور هم‌زمان و در هم‌تنیده اجرا می‌شوند و بسته به سطح سازمان و بافت، وزن متفاوتی دارند. برای مدیر رسانه، این چارچوب به‌ویژه در تعامل میان تحریریه، بازاریابی و مدیریت و در مدیریت بحران کاربرد دارد. نقدهای اصلی به آن، تکیه بر مشاهدهٔ محدود، تعمیم از نمونهٔ کوچک مدیران و دشواری تفکیک نقش‌ها در محیط دیجیتال مربوط می‌شود.",
        definition="نقش‌های مدیریتی، مدلی است که کار مدیر را در ده نقش بین‌فردی، اطلاعاتی و تصمیم‌گیری توصیف می‌کند و بر ماهیت پراکنده، شفاهی و واکنشی آن تأکید دارد.",
        main_problem="مدیران در عمل چه کاری انجام می‌دهند، و آیا تصور کلاسیک از کار مدیریت با واقعیت روزمرهٔ آن هم‌خوان است.",
        mechanism="مدیر در جریان کار روزمره میان نقش‌ها جابه‌جا می‌شود: روابط بین‌فردی را می‌سازد، اطلاعات را جمع و توزیع می‌کند و در موقعیت‌های تصمیم، منابع و اختلال‌ها را مدیریت می‌کند. وقفه‌های پیاپی و ارتباط شفاهی، ساختار زمانی کار مدیر را می‌سازند.",
        assumptions=[
            "کار مدیریت را باید با مشاهدهٔ مستقیم توصیف کرد.",
            "کار مدیر پراکنده، کوتاه‌مدت و همراه با وقفه است.",
            "مدیر در چند نقش هم‌زمان عمل می‌کند.",
            "ارتباط شفاهی، سهم بزرگی از زمان مدیر را می‌گیرد.",
            "نقش‌ها بسته به سطح و بافت سازمان وزن متفاوت دارند.",
        ],
        principles=[
            "توصیف واقعی کار مدیر مقدم بر تجویز هنجاری است.",
            "ده نقش در سه دستهٔ بین‌فردی، اطلاعاتی و تصمیم‌گیری قرار می‌گیرند.",
            "نقش‌ها هم‌زمان و در هم‌تنیده‌اند.",
            "مدیر رسانه باید میان تحریریه و کسب‌وکار میانجی‌گری کند.",
            "تحلیل نقش‌ها به ارزیابی نیازهای آموزشی مدیر کمک می‌کند.",
            "بافت دیجیتال، وزن نقش‌های اطلاعاتی را بالا برده است.",
            "مدل به تحلیل هم‌زمانی چند نقش در موقعیت بحرانی کمک می‌کند.",
        ],
        critiques=[
            "مشاهدهٔ محدود و نمونهٔ کوچک، تعمیم را محدود می‌کند.",
            "تفکیک نقش‌ها در عمل دشوار است.",
            "توصیف، تجویز راهبردی برای مدیریت ارائه نمی‌دهد.",
            "تفاوت‌های فرهنگی و صنعتی کم‌بررسی می‌ماند.",
            "کار مدیریت در محیط دیجیتال، شکل تازه‌ای یافته است.",
        ],
        critique_text="منتقدان می‌گویند مینتزبرگ با توصیف واقع‌گرایانهٔ کار مدیر، تصویر کلاسیک برنامه‌ریزی را به چالش کشید اما مدل او بیشتر توصیفی است و نسخهٔ تجویزی روشنی برای بهبود مدیریت ارائه نمی‌دهد. با این حال، چارچوب ده‌نقشی همچنان در آموزش مدیریت و تحلیل نقش مدیر رسانه به کار می‌رود.",
        applications=[
            "آموزش و ارزیابی مدیران رسانه.",
            "تحلیل نقش میانجی مدیر میان تحریریه و کسب‌وکار.",
            "طراحی شرح شغل و شایستگی‌های مدیریتی.",
            "پژوهش کار روزمرهٔ مدیران.",
            "مدیریت بحران و تخصیص منابع در سازمان رسانه‌ای.",
        ],
        example_text="مدیر یک خبرگزاری در یک روز کاری هم در نقش سخنگو با رسانه‌های دیگر مصاحبه می‌کند، هم در نقش حل‌کنندهٔ اختلال برای تأخیر انتشار خبر مداخله می‌کند و هم در نقش رهبر، تیم تحریریه را برای پوشش رویداد بسیج می‌کند. مدل نقش‌های مدیریتی همین جابه‌جایی سریع را توصیف می‌کند.",
        evolution="کتاب سال ۱۹۷۳ توصیف تجربی کار مدیر را ارائه کرد و مقالهٔ سال ۱۹۷۵ آن را به مخاطب مدیریتی گسترده رساند. پژوهش‌های بعدی، مدل را به مدیریت رسانه، بخش عمومی و محیط دیجیتال گستردند.",
        key_concepts=["نقش بین‌فردی", "نقش اطلاعاتی", "نقش تصمیم‌گیری", "کار پراکنده", "ارتباط شفاهی", "وقفه"],
        theorists="هنری مینتزبرگ، صورت‌بند مدل نقش‌های مدیریتی.",
        theorists_text="این مدل در سنت پژوهش تجربی مدیریت و مشاهدهٔ میدانی شکل گرفت.",
        model="مدل ده‌نقشی: سه نقش بین‌فردی، سه نقش اطلاعاتی و چهار نقش تصمیم‌گیری؛ نقش‌ها هم‌زمان و در بستر کار پراکنده و شفاهی اجرا می‌شوند.",
        studies=[
            "کتاب سال ۱۹۷۳ مشاهدات میدانی کار مدیر را گزارش کرد.",
            "مقالهٔ سال ۱۹۷۵ مدل را برای مخاطب گسترده‌تر بازگفت.",
            "پژوهش‌های مدیریت رسانه، نقش‌ها را در سازمان خبری آزمودند.",
            "مطالعات دیجیتال، تغییر وزن نقش‌های اطلاعاتی را بررسی کردند.",
            "پژوهش‌های تطبیقی، تفاوت نقش‌ها در سطوح مختلف مدیریت را سنجیدند.",
        ],
    ),
    "MC-173": dict(
        year=1966,
        summary="چرخهٔ عمر محصول، مدلی در بازاریابی و راهبرد است که ریشهٔ مدیریتی آن به مقالهٔ تئودور لویت در سال ۱۹۶۵ و صورت‌بندی بین‌المللی آن به مقالهٔ ریموند ورنون در سال ۱۹۶۶ بازمی‌گردد. ادعای مرکزی این است که محصولات معمولاً چهار مرحله را طی می‌کنند: معرفی، رشد، بلوغ و افول. در معرفی، فروش کم و هزینهٔ تبلیغ بالا است؛ در رشد، فروش سریع بالا می‌رود و رقبا وارد می‌شوند؛ در بلوغ، رشد کند و رقابت قیمتی شدید می‌شود؛ و در افول، فروش و سود کاهش می‌یابد و تصمیم دربارهٔ حذف یا احیا مطرح می‌شود. هر مرحله، فشار رقابتی، قیمت، شیوهٔ تبلیغ و منطق سرمایه‌گذاری متفاوتی دارد و مدیر باید راهبرد را با مرحله هم‌خوان کند. ورنون این چارچوب را برای توضیح جابه‌جایی تولید میان کشورها در طول چرخهٔ عمر محصول به کار برد. در صنایع رسانه‌ای، چرخهٔ عمر برای تحلیل قالب‌های محتوایی، فناوری‌های توزیع و محصولات خبری به کار رفته است. نقدهای اصلی به آن، پشتوانهٔ تجربی ضعیف، خطر خودتحقق‌بخش‌شدن، نبود مرحلهٔ بازتولید و تفاوت مسیر محصولات مختلف مربوط می‌شود.",
        definition="چرخهٔ عمر محصول، مدلی است که مسیر فروش و سود محصول را در چهار مرحلهٔ معرفی، رشد، بلوغ و افول توصیف می‌کند و برای هر مرحله راهبرد بازاریابی متفاوتی پیشنهاد می‌دهد.",
        main_problem="محصول در طول عمر خود با چه تغییراتی در فروش، رقابت و سود روبه‌رو می‌شود، و مدیر چگونه باید راهبرد بازاریابی و سرمایه‌گذاری را با هر مرحله هم‌خوان کند.",
        mechanism="در معرفی، آگاهی و پذیرش کم است و سرمایه‌گذاری تبلیغاتی بالا؛ در رشد، تقلید و ورود رقبا، فروش را سریع بالا می‌برد؛ در بلوغ، اشباع بازار و رقابت قیمتی، حاشیهٔ سود را کم می‌کند؛ در افول، تغییر سلیقه یا فناوری، فروش را کاهش می‌دهد و تصمیم دربارهٔ حذف یا بازآفرینی محصول الزامی می‌شود.",
        assumptions=[
            "محصولات چرخهٔ عمر قابل شناسایی دارند.",
            "هر مرحله، منطق رقابتی و بازاریابی متفاوتی دارد.",
            "راهبرد باید با مرحلهٔ چرخه هم‌خوان باشد.",
            "رشد فروش در بلوغ کند و در افول منفی می‌شود.",
            "تصمیم دربارهٔ سرمایه‌گذاری به مرحلهٔ محصول وابسته است.",
        ],
        principles=[
            "چهار مرحلهٔ معرفی، رشد، بلوغ و افول را باید تفکیک کرد.",
            "تبلیغ آگاهی‌بخش در معرفی و تبلیغ تمایزی در بلوغ مناسب است.",
            "قیمت‌گذاری باید با مرحله و کشش بازار هم‌خوان شود.",
            "در بلوغ، تمایز و وفاداری مهم‌تر از گسترش کمی است.",
            "در افول، حذف یا بازآفرینی محصول باید تصمیم راهبردی شود.",
            "مدل برای برنامه‌ریزی سبد محصول، نه پیش‌بینی قطعی، به کار می‌رود.",
        ],
        critiques=[
            "پشتوانهٔ تجربی مراحل چهارگانه ضعیف است.",
            "مدل می‌تواند خودتحقق‌بخش شود.",
            "همهٔ محصولات مسیر یکسان طی نمی‌کنند.",
            "مرحلهٔ بازتولید و احیای محصول کم‌بررسی می‌ماند.",
            "برای محصولات دیجیتال با چرخهٔ کوتاه، بازنگری می‌خواهد.",
        ],
        critique_text="منتقدان می‌گویند چرخهٔ عمر محصول چارچوبی ساده و آموزنده برای هم‌خوانی راهبرد با مرحلهٔ بازار است اما شواهد تجربی یکدستی برای مراحل چهارگانه وجود ندارد و استفادهٔ جبری از آن می‌تواند به پیش‌بینی خودتحقق‌بخش بینجامد. با این حال، در آموزش بازاریابی و مدیریت محصول رسانه همچنان پرکاربرد است.",
        applications=[
            "برنامه‌ریزی سبد محصول و محتوای رسانه‌ای.",
            "تحلیل مرحلهٔ قالب‌های محتوایی و فناوری توزیع.",
            "تعیین راهبرد تبلیغ و قیمت در هر مرحله.",
            "تصمیم دربارهٔ حذف یا احیای محصول.",
            "تحلیل جابه‌جایی تولید و بازار بین‌المللی.",
        ],
        example_text="یک قالب پادکست ممکن است در مرحلهٔ رشد با ورود سریع تولیدکنندگان روبه‌رو شود، در بلوغ با اشباع مخاطب و رقابت بر سر زمان شنیدن، و در افول با جابه‌جایی توجه به قالب تازه؛ مدیر رسانه در هر مرحله راهبرد محتوا و تبلیغ متفاوتی برمی‌گزیند. چرخهٔ عمر محصول همین منطق را فراهم می‌کند.",
        evolution="مقالهٔ لویت در سال ۱۹۶۵ چارچوب مدیریتی را معرفی کرد و مقالهٔ ورنون در سال ۱۹۶۶ آن را برای تجارت و سرمایه‌گذاری بین‌المللی بسط داد. در دههٔ ۱۹۷۰ مدل به متن استاندارد بازاریابی تبدیل شد و از دههٔ ۲۰۰۰ با نقد تجربی و بازخوانی دیجیتال روبه‌رو شد.",
        key_concepts=["معرفی", "رشد", "بلوغ", "افول", "راهبرد مرحله‌ای", "اشباع بازار"],
        theorists="تئودور لویت و ریموند ورنون، صورت‌بندانان چرخهٔ عمر محصول.",
        theorists_text="این مدل در سنت بازاریابی و اقتصاد بین‌الملل شکل گرفت و با مدیریت راهبردی محصول پیوند خورد.",
        model="مدل چهارمرحله‌ای: معرفی، رشد، بلوغ و افول؛ هر مرحله با الگوی فروش، شدت رقابت و راهبرد بازاریابی متمایز شناخته می‌شود.",
        studies=[
            "مقالهٔ سال ۱۹۶۵ چارچوب مدیریتی چرخهٔ عمر را معرفی کرد.",
            "مقالهٔ سال ۱۹۶۶ آن را به تجارت بین‌المللی پیوند داد.",
            "پژوهش‌های بازاریابی، شواهد تجربی مراحل را آزمودند.",
            "مطالعات رسانه، چرخهٔ عمر قالب‌های محتوایی را تحلیل کردند.",
        ],
    ),
    "MC-174": dict(
        year=1957,
        summary="ماتریس آنسوف، چارچوبی در راهبرد رشد است که ایگور آنسوف در سال ۱۹۵۷ در مقالهٔ راهبردهای تنوع‌بخشی در هاروارد بیزینس ریویو معرفی کرد و در کتاب راهبرد شرکتی در سال ۱۹۶۵ بسط داد. ادعای مرکزی این است که راهبردهای رشد را می‌توان بر پایهٔ دو بعد، بازار (موجود یا جدید) و محصول (موجود یا جدید)، در چهار گزینه دسته‌بندی کرد: نفوذ در بازار، یعنی فروش بیشتر محصول موجود در بازار موجود؛ توسعهٔ بازار، یعنی عرضهٔ محصول موجود در بازار جدید؛ توسعهٔ محصول، یعنی عرضهٔ محصول جدید در بازار موجود؛ و تنوع‌بخشی، یعنی ورود هم‌زمان به بازار و محصول جدید. هرچه هر دو بعد جدیدتر باشند، عدم‌قطعیت و ریسک بیشتر است؛ بنابراین تنوع‌بخشی پرمخاطره‌ترین و نفوذ در بازار کم‌ریسک‌ترین گزینه است. این ماتریس به مدیر کمک می‌کند ریسک هر گزینه را در کنار فرصت آن ببیند و سبد راهبرد رشد را متوازن کند. در صنایع رسانه‌ای، آنسوف برای تحلیل توسعهٔ پلتفرم، ورود به بازارهای جدید مخاطب و تنوع‌بخشی درآمد به کار رفته است. نقدهای اصلی به آن، سادگی و ایستایی دو‌بُعدی، کم‌توجهی به قابلیت‌های سازمانی و نادیده‌گرفتن اکوسیستم‌های همکاری مربوط می‌شود.",
        definition="ماتریس آنسوف، چارچوبی است که چهار راهبرد رشد، یعنی نفوذ در بازار، توسعهٔ بازار، توسعهٔ محصول و تنوع‌بخشی، را بر پایهٔ تازگی بازار و محصول از هم جدا می‌کند و ریسک هر گزینه را نشان می‌دهد.",
        main_problem="سازمان چه گزینه‌هایی برای رشد دارد، و چگونه می‌توان ریسک و فرصت هر گزینه را بر پایهٔ تازگی بازار و محصول مقایسه کرد.",
        mechanism="با ترکیب دو بعد بازار و محصول، چهار گزینهٔ رشد ساخته می‌شود؛ هرچه محصول یا بازار تازه‌تر باشد، نیاز به توانمندی، سرمایه و یادگیری بیشتر و ریسک بالاتر است. سازمان با انتخاب ترکیبی از این گزینه‌ها، سبد رشد خود را متوازن می‌کند.",
        assumptions=[
            "رشد از دو مسیر بازار و محصول ممکن است.",
            "تازگی بازار و محصول، معیار اصلی ریسک است.",
            "سازمان می‌تواند میان چهار گزینه انتخاب کند.",
            "تنوع‌بخشی پرمخاطره‌ترین و نفوذ در بازار کم‌ریسک‌ترین گزینه است.",
            "توازن سبد راهبرد رشد، ریسک کل را کاهش می‌دهد.",
        ],
        principles=[
            "چهار گزینهٔ رشد را باید بر پایهٔ دو بعد بازار و محصول تفکیک کرد.",
            "ریسک با تازگی هر دو بعد افزایش می‌یابد.",
            "نفوذ در بازار، کم‌ریسک‌ترین گزینه است.",
            "تنوع‌بخشی به توانمندی و منابع تازه نیاز دارد.",
            "انتخاب گزینه باید با قابلیت‌های سازمان هم‌خوان باشد.",
            "سبد رشد باید میان گزینه‌های کم‌ریسک و پرریسک متوازن شود.",
        ],
        critiques=[
            "مدل دو‌بُعدی و ایستاست.",
            "قابلیت‌ها و منابع سازمانی را کم‌رنگ می‌کند.",
            "اکوسیستم همکاری و اتحاد راهبردی را نادیده می‌گیرد.",
            "مرز بازار موجود و جدید همیشه روشن نیست.",
            "برای محیط پلتفرمی و چندبازاری، ساده‌سازی‌شده است.",
        ],
        critique_text="منتقدان می‌گویند ماتریس آنسوف ابزاری روشن و آموزنده برای مقایسهٔ گزینه‌های رشد است اما تصویری ساده و ایستا می‌دهد و نقش قابلیت سازمانی، اتحاد و اکوسیستم را کم‌رنگ می‌کند. با این حال، همچنان چارچوب پایهٔ تحلیل راهبرد رشد و تنوع‌بخشی است.",
        applications=[
            "تحلیل گزینه‌های رشد سازمان رسانه‌ای.",
            "تصمیم دربارهٔ ورود به بازار مخاطب جدید.",
            "ارزیابی تنوع‌بخشی درآمدی.",
            "آموزش راهبرد شرکتی و بازاریابی.",
            "برنامه‌ریزی توسعهٔ محصول و پلتفرم.",
        ],
        example_text="یک روزنامه برای رشد می‌تواند شمار خوانندگان فعلی را افزایش دهد (نفوذ در بازار)، نسخهٔ شهری تازه راه‌اندازی کند (توسعهٔ بازار)، پادکست خبری بسازد (توسعهٔ محصول) یا به کسب‌وکار رویداد و آموزش وارد شود (تنوع‌بخشی). ماتریس آنسوف این گزینه‌ها را با ریسک متفاوتشان کنار هم می‌گذارد.",
        evolution="مقالهٔ سال ۱۹۵۷ چهار گزینهٔ رشد را معرفی کرد؛ کتاب سال ۱۹۶۵ چارچوب را نظام‌مند کرد و در دههٔ ۱۹۸۰ به متن استاندارد راهبرد شرکتی تبدیل شد. در دههٔ ۲۰۱۰ با اکوسیستم پلتفرمی و راهبرد اتحاد بازخوانی شد.",
        key_concepts=["نفوذ در بازار", "توسعهٔ بازار", "توسعهٔ محصول", "تنوع‌بخشی", "ریسک رشد", "سبد راهبرد"],
        theorists="ایگور آنسوف، سازندهٔ ماتریس رشد.",
        theorists_text="این چارچوب در سنت راهبرد شرکتی و برنامه‌ریزی رشد شکل گرفت.",
        model="مدل چهارخانه: بازار موجود/جدید در برابر محصول موجود/جدید؛ چهار راهبرد رشد با ریسک فزاینده از نفوذ در بازار تا تنوع‌بخشی.",
        studies=[
            "مقالهٔ سال ۱۹۵۷ چهار گزینهٔ رشد را معرفی کرد.",
            "کتاب سال ۱۹۶۵ چارچوب را نظام‌مند کرد.",
            "پژوهش‌های راهبرد، کاربرد ماتریس در تنوع‌بخشی را آزمودند.",
            "مطالعات رسانه، ماتریس را برای رشد دیجیتال به کار بردند.",
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
                                       "verified": n_verified, "batch": 134}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH134 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
