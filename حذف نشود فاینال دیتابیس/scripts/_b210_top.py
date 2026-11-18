# -*- coding: utf-8 -*-
"""Batch 210: MC-264, MC-274, MC-275, MC-276, MC-281 (MODEL)."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch210-20261117"
NOW = "2026-11-17 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch210.json"

S = {
    "MC-264": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Whence Consumer Loyalty?",
             title_fa="وفاداری مصرف‌کننده از کجا می‌آید؟",
             authors="Richard L. Oliver", year=1999,
             publisher="Journal of Marketing",
             doi="10.1177/00222429990634s105",
             url="https://journals.sagepub.com/doi/10.1177/00222429990634s105",
             language="en", isbn=None,
             citation="Oliver, R. L. (1999). Whence consumer loyalty? Journal of Marketing, 63(Special Issue), 33-44. https://doi.org/10.1177/00222429990634s105",
             locator="63, 33-44",
             locator_type="PAGE",
             supports="cognitive, affective, conative and action loyalty phases",
             verified=True),
        dict(kind="BOOK",
             title_en="The Loyalty Effect: The Hidden Force Behind Growth, Profits, and Lasting Value",
             title_fa="اثر وفاداری: نیروی پنهان پشت رشد، سود و ارزش پایدار",
             authors="Frederick F. Reichheld; Thomas Teal", year=1996,
             publisher="Harvard Business School Press",
             doi=None,
             url="https://archive.org/details/loyaltyeffecthid00reic",
             language="en", isbn=None,
             citation="Reichheld, F. F. (1996). The Loyalty Effect: The Hidden Force Behind Growth, Profits, and Lasting Value. Boston: Harvard Business School Press.",
             locator="book",
             locator_type="BOOK",
             supports="economic argument linking retention to profitability",
             verified=True),
    ],
    "MC-274": [
        dict(kind="BOOK",
             title_en="Hooked: How to Build Habit-Forming Products",
             title_fa="قلاب: چگونه محصولات عادت‌ساز بسازیم",
             authors="Nir Eyal; Ryan Hoover", year=2014,
             publisher="Portfolio / Penguin",
             doi=None,
             url="https://www.penguinrandomhouse.com/books/317898/hooked-by-nir-eyal/",
             language="en", isbn=None,
             citation="Eyal, N., & Hoover, R. (2014). Hooked: How to Build Habit-Forming Products. New York: Portfolio / Penguin.",
             locator="book",
             locator_type="BOOK",
             supports="four-phase Hook Model of trigger, action, variable reward and investment",
             verified=True),
        dict(kind="BOOK",
             title_en="Hooked: How to Build Habit-Forming Products (revised edition)",
             title_fa="قلاب: چگونه محصولات عادت‌ساز بسازیم (ویراست بازنگری‌شده)",
             authors="Nir Eyal", year=2019,
             publisher="Penguin Books",
             doi=None,
             url="https://www.penguin.co.uk/books/278201/hooked-by-eyal-nir/9780241184837",
             language="en", isbn=None,
             citation="Eyal, N. (2019). Hooked: How to Build Habit-Forming Products (revised ed.). London: Penguin Books.",
             locator="book",
             locator_type="BOOK",
             supports="revised presentation of the Hook Model including ethical design discussion",
             verified=True),
    ],
    "MC-275": [
        dict(kind="CONFERENCE_PAPER",
             title_en="A Behavior Model for Persuasive Design",
             title_fa="مدلی رفتاری برای طراحی اقناعی",
             authors="B. J. Fogg", year=2009,
             publisher="ACM",
             doi="10.1145/1541948.1541999",
             url="https://dl.acm.org/doi/10.1145/1541948.1541999",
             language="en", isbn=None,
             citation="Fogg, B. J. (2009). A behavior model for persuasive design. In Proceedings of the 4th International Conference on Persuasive Technology (Article 40). New York: ACM. https://doi.org/10.1145/1541948.1541999",
             locator="Article 40",
             locator_type="ARTICLE",
             supports="behavior occurs when motivation, ability and prompt converge",
             verified=True),
        dict(kind="BOOK",
             title_en="Tiny Habits: The Small Changes That Change Everything",
             title_fa="عادت‌های کوچک: تغییرهای کوچکی که همه‌چیز را تغییر می‌دهند",
             authors="B. J. Fogg", year=2020,
             publisher="Houghton Mifflin Harcourt",
             doi=None,
             url="https://www.publishersweekly.com/9780358003328",
             language="en", isbn=None,
             citation="Fogg, B. J. (2020). Tiny Habits: The Small Changes That Change Everything. Boston: Houghton Mifflin Harcourt.",
             locator="book",
             locator_type="BOOK",
             supports="practical extension of the behavior model to habit formation",
             verified=True),
    ],
    "MC-276": [
        dict(kind="CONFERENCE_PAPER",
             title_en="The Dark (Patterns) Side of UX Design",
             title_fa="سویهٔ تاریک طراحی تجربهٔ کاربر: الگوهای فریبنده",
             authors="Colin M. Gray; Yubo Kou; Bryan Battles; Joseph Hoggatt; Austin L. Toombs", year=2018,
             publisher="ACM",
             doi="10.1145/3173574.3174108",
             url="https://dl.acm.org/doi/10.1145/3173574.3174108",
             language="en", isbn=None,
             citation="Gray, C. M., Kou, Y., Battles, B., Hoggatt, J., & Toombs, A. L. (2018). The dark (patterns) side of UX design. In Proceedings of the 2018 CHI Conference on Human Factors in Computing Systems (Paper 534). New York: ACM. https://doi.org/10.1145/3173574.3174108",
             locator="Paper 534",
             locator_type="ARTICLE",
             supports="taxonomy of dark patterns as strategies rather than mere tricks",
             verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Dark Patterns at Scale: Findings from a Crawl of 11K Shopping Websites",
             title_fa="الگوهای فریبنده در مقیاس بزرگ: یافته‌های خزش ۱۱ هزار وبگاه خرید",
             authors="Arunesh Mathur; Gunes Acar; Michael J. Friedman; Elena Lucherini; Jonathan Mayer; Marshini Chetty; Arvind Narayanan", year=2019,
             publisher="Proceedings of the ACM on Human-Computer Interaction",
             doi="10.1145/3359183",
             url="https://dl.acm.org/doi/10.1145/3359183",
             language="en", isbn=None,
             citation="Mathur, A., Acar, G., Friedman, M. J., Lucherini, E., Mayer, J., Chetty, M., & Narayanan, A. (2019). Dark patterns at scale: Findings from a crawl of 11K shopping websites. Proceedings of the ACM on Human-Computer Interaction, 3(CSCW), Article 81. https://doi.org/10.1145/3359183",
             locator="3(CSCW), Article 81",
             locator_type="ARTICLE",
             supports="1,818 dark pattern instances across 15 types and 7 categories",
             verified=True),
    ],
    "MC-281": [
        dict(kind="BOOK",
             title_en="Algorithms of Oppression: How Search Engines Reinforce Racism",
             title_fa="الگوریتم‌های سرکوب: چگونه موتورهای جستجو نژادپرستی را بازتولید می‌کنند",
             authors="Safiya Umoja Noble", year=2018,
             publisher="New York University Press",
             doi=None,
             url="https://nyupress.org/9781479849949/algorithms-of-oppression/",
             language="en", isbn=None,
             citation="Noble, S. U. (2018). Algorithms of Oppression: How Search Engines Reinforce Racism. New York: New York University Press.",
             locator="book",
             locator_type="BOOK",
             supports="commercial and historical bias of search ranking as a mechanism of oppression",
             verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Google Search: Hyper-visibility as a Means of Rendering Black Women and Girls Invisible",
             title_fa="جستجوی گوگل: فرانمایی به‌عنوان سازوکار نامرئی‌سازی زنان و دختران سیاه‌پوست",
             authors="Safiya Umoja Noble", year=2013,
             publisher="InVisible Culture",
             doi=None,
             url="https://www.invisibleculturejournal.com/pub/google-search-hypervisibility",
             language="en", isbn=None,
             citation="Noble, S. U. (2013). Google search: Hyper-visibility as a means of rendering Black women and girls invisible. InVisible Culture, 19.",
             locator="19",
             locator_type="ARTICLE",
             supports="early empirical study of racialized and sexualized search result bias",
             verified=True),
    ],
}

ENRICH = {
    "MC-264": dict(
        needs_enrichment=False,
        level="میان",
        related_approaches="بازاریابی رابطه‌مند؛ مدیریت ارتباط با مشتری؛ ارزش عمر مشتری؛ پژوهش وفاداری برند؛ تحلیل ریزش در رسانهٔ اشتراکی.",
        recommended_sources="«وفاداری مصرف‌کننده از کجا می‌آید؟» (الیور، ۱۹۹۹)؛ «اثر وفاداری» (رایکهلد، ۱۹۹۶)؛ پژوهش‌های ریزش و پیش‌بینی ارزش عمر مشتری در رسانه.",
        detailed_analysis=("۱. بنیان و منطق نظری\nالیور (۱۹۹۹) در مقالهٔ «وفاداری مصرف‌کننده از کجا می‌آید؟» وفاداری را فرایندی مرحله‌ای دانست: وفاداری شناختی (باور به برتری برند بر پایهٔ اطلاعات)، "
                           "وفاداری عاطفی (دلبستگی و لذت)، وفاداری کنشی (قصد رفتاری قوی برای خرید دوباره) و وفاداری عملی (رفتار پایدار در برابر موانع). "
                           "این صورت‌بندی، وفاداری را از تک‌شاخص «تکرار خرید» جدا کرد. رایکهلد (۱۹۹۶) در «اثر وفاداری» استدلال اقتصادی پیوند نرخ نگهداشت و سودآوری را پیش گذاشت.\n\n"
                           "۲. ساختارهای مفهومی\nچهار مرحلهٔ وفاداری، ریزش و ارزش عمر مشتری سازه‌های اصلی‌اند. وفاداری زمانی به ارزش تبدیل می‌شود که مشتری در مرحلهٔ عملی باقی بماند و ریزش مهار شود.\n\n"
                           "۳. نمونه‌های تحلیلی\nدر سرویس‌های اشتراکی، مشتری ممکن است باور شناختی و دلبستگی عاطفی داشته باشد اما با افزایش یک‌بارهٔ قیمت بلافاصله برود؛ این نشان می‌دهد مراحل وفاداری یکدیگر را تضمین نمی‌کنند و مدیر باید هر مرحله را جدا اندازه بگیرد.\n\n"
                           "۴. نقدها و چالش‌ها\nمرحله‌بندی خطی نیست و مشتری می‌تواند میان مراحل جابه‌جا شود؛ فاصلهٔ نیت و رفتار عملی در اندازه‌گیری مسئله‌ساز است؛ ارزش عمر مشتری به فرض‌های نرخ نگهداشت و حاشیهٔ سود حساس است؛ ریزش خاموش کمتر دیده می‌شود؛ و رقابت قیمتی می‌تواند وفاداری عاطفی را به‌سرعت بی‌اثر کند.\n\n"
                           "۵. سیر تاریخی\n«اثر وفاداری» (۱۹۹۶) گفتمان اقتصادی نگهداشت را گسترش داد، الیور (۱۹۹۹) چارچوب مرحله‌ای را تثبیت کرد و پژوهش‌های مدیریت ارتباط با مشتری، مدل‌های پیش‌بینی ریزش را ساختند.\n\n"
                           "۶. جایگاه در بحث روز\nدر اقتصاد اشتراک، چرخهٔ وفاداری و ریزش ابزار روزمرهٔ تحلیل رسانه است؛ سنجه‌ها اکنون ریزش اختیاری و غیراختیاری را جدا می‌کنند و به پیش‌بینی زودهنگام تمرکز دارند."),
    ),
    "MC-274": dict(
        needs_enrichment=False,
        level="میان",
        related_approaches="طراحی اقناعی؛ مدل رفتاری فاگ؛ اقتصاد توجه؛ طراحی اعتیادآور؛ وارونه‌سازی اخلاقی طراحی محصول.",
        recommended_sources="«قلاب» (ایال و هوور، ۲۰۱۴)؛ ویراست بازنگری‌شدهٔ «قلاب» (ایال، ۲۰۱۹)؛ «فناوری اقناعی» (فاگ، ۲۰۰۳).",
        detailed_analysis=("۱. بنیان و منطق نظری\nایال و هوور (۲۰۱۴) مدل قلاب را به‌عنوان چرخهٔ چهارمرحله‌ای محرک، کنش، پاداش متغیر و سرمایه‌گذاری معرفی کردند. "
                           "محرک می‌تواند بیرونی (اعلان، پیام، تبلیغ) یا درونی (احساس تنهایی، ملال، اضطراب) باشد؛ هدف محصول این است که محرک بیرونی را به درونی تبدیل کند. "
                           "سازوکار پاداش متغیر با پژوهش‌های تقویت نامنظم اسکینر پیوند دارد و سرمایه‌گذاری کاربر، ارزش و تعهد ذخیره‌شده می‌سازد.\n\n"
                           "۲. ساختارهای مفهومی\nچهار مرحلهٔ قلاب، ناحیهٔ عادت (رفتار پرتکرار و پرلیاقت) و سه نوع پاداش قبیله‌ای، شکار و خود از سازه‌های محوری‌اند.\n\n"
                           "۳. نمونه‌های تحلیلی\nدر شبکه‌های اجتماعی، اعلان (محرک) کاربر را به بازکردن برنامه (کنش) می‌کشاند؛ محتوای تازه و غیرقابل پیش‌بینی (پاداش متغیر) انتظار را زنده نگه می‌دارد و پسندیدن و فالو کردن (سرمایه‌گذاری) بازگشت بعدی را آسان‌تر می‌کند.\n\n"
                           "۴. نقدها و چالش‌ها\nمدل بر پایهٔ تجربهٔ صنعتی و مطالعهٔ موردی بنا شده و شواهد تجربی کنترل‌شدهٔ کمی دارد؛ عادت مضر و عادت مفید را از هم جدا نمی‌کند؛ تمرکز بر زمان صرف‌شده می‌تواند ارزش کاربر را نادیده بگیرد؛ خطر مهندسی اعتیاد و مسئولیت اخلاقی طراح را کم‌رنگ می‌کند؛ و در بافت‌های فرهنگی متفاوت اعتبار یکسانی ندارد.\n\n"
                           "۵. سیر تاریخی\nکتاب ۲۰۱۴ مدل را در ادبیات طراحی محصول تثبیت کرد، ویراست ۲۰۱۹ بحث اخلاق و ارتباط با معیارهای رفاه دیجیتال را افزود و پژوهش‌های طراحی اقناعی انتقادی، مرز عادت و اجبار را کاویدند.\n\n"
                           "۶. جایگاه در بحث روز\nبا رشد مقررات مربوط به الگوهای فریبنده و سلامت دیجیتال، پرسش از مرز میان طراحی عادت‌ساز و طراحی استثمارگر به یکی از محورهای اصلی سیاست محصول تبدیل شده است."),
    ),
    "MC-275": dict(
        needs_enrichment=False,
        level="میان",
        related_approaches="طراحی اقناعی؛ مدل قلاب؛ اقتصاد رفتار؛ طراحی مرحله‌ای تغییر رفتار؛ عادت‌سازی.",
        recommended_sources="«مدلی رفتاری برای طراحی اقناعی» (فاگ، ۲۰۰۹)؛ «عادت‌های کوچک» (فاگ، ۲۰۲۰)؛ «فناوری اقناعی» (فاگ، ۲۰۰۳).",
        detailed_analysis=("۱. بنیان و منطق نظری\nفاگ (۲۰۰۹) در مقالهٔ کنفرانس فناوری اقناعی، مدل رفتاری خود را چنین صورت‌بندی کرد: رفتار در یک لحظه رخ می‌دهد اگر انگیزش، توانایی و محرک هم‌زمان کافی باشند. "
                           "او انگیزش را از سه جفت متضاد (لذت و درد، امید و ترس، پذیرش و طرد اجتماعی) و توانایی را با شش عامل زمان، هزینه، تلاش جسمی، تلاش ذهنی، انطباق با روال اجتماعی و عادت سنجید.\n\n"
                           "۲. ساختارهای مفهومی\nانگیزش، توانایی، محرک و آستانهٔ رفتار سازه‌های اصلی‌اند. محرک سه گونه است: انگیزه‌افزا (وقتی انگیزش کم است)، تسهیل‌گر (وقتی توانایی کم است) و نشانه (وقتی هر دو کافی است).\n\n"
                           "۳. نمونه‌های تحلیلی\nدر یک اپ سلامت، اگر انگیزش و توانایی بالا باشد یک اعلان ساده کافی است؛ اما برای کاربر بی‌انگیزه، محرک باید احساس ارزش بسازد و برای کاربر ناتوان، محرک باید مانع را کم کند، نه اینکه فشار بیاورد.\n\n"
                           "۴. نقدها و چالش‌ها\nمدل توصیفی است و پیش‌بینی کمی نمی‌دهد؛ سنجش انگیزش و توانایی ذهنی و وابسته به بافت است؛ عادت و محرک‌های درونی را کامل پوشش نمی‌دهد؛ خطر کاربرد اقناعی برای دستکاری و نه برای رفاه کاربر جدی است؛ و شواهد تجربی مستقل در دامنه‌های گوناگون ناهمگون است.\n\n"
                           "۵. سیر تاریخی\nمقالهٔ ۲۰۰۹ چارچوب را تثبیت کرد، «عادت‌های کوچک» (۲۰۲۰) آن را به عمل عادت‌سازی و جشن کوچک گسترش داد و پژوهش‌های طراحی رفتاری، مدل را با نظریهٔ خودتعیینی و اقتصاد رفتار ترکیب کردند.\n\n"
                           "۶. جایگاه در بحث روز\nدر طراحی سلامت دیجیتال، این مدل هم برای افزایش تعامل سالم و هم برای نقد شیوه‌های اقناعی اجباری به‌کار می‌رود و اکنون در بحث مقرراتی دربارهٔ طراحی منصفانه حاضر است."),
    ),
    "MC-276": dict(
        needs_enrichment=False,
        level="میان",
        related_approaches="اخلاق طراحی؛ طراحی اقناعی؛ اقتصاد توجه؛ حقوق مصرف‌کننده؛ مقررات پلتفرم.",
        recommended_sources="«سویهٔ تاریک طراحی تجربهٔ کاربر» (گری و همکاران، ۲۰۱۸)؛ «الگوهای فریبنده در مقیاس بزرگ» (ماتور و همکاران، ۲۰۱۹)؛ وبگاه مستندسازی الگوهای فریبنده (برنول، ۲۰۱۰).",
        detailed_analysis=("۱. بنیان و منطق نظری\nاصطلاح «الگوهای فریبنده» را هری برنول در ۲۰۱۰ برای توصیف طرح‌های رابطی رواج داد که کاربر را به انتخابی ناخواسته می‌کشانند. "
                           "گری و همکاران (۲۰۱۸) نشان دادند این‌ها فهرستی از ترفندهای پراکنده نیستند، بلکه راهبردهایی برای تأمین ارزش کسب‌وکار به قیمت ارزش کاربرند. "
                           "ماتور و همکاران (۲۰۱۹) با خزش حدود ۱۱ هزار وبگاه خرید، بیش از ۱۸۰۰ نمونه در ۱۵ نوع و ۷ ردهٔ بزرگ یافتند.\n\n"
                           "۲. ساختارهای مفهومی\nنامتقارنی اطلاعات و قدرت، پنهان‌کاری، مانع‌تراشی، دستکاری رابط، اجبار به کنش و فوریت و کمبود ساختگی، خانواده‌های اصلی‌اند.\n\n"
                           "۳. نمونه‌های تحلیلی\nپیش‌انتخاب گزینهٔ گران‌تر، پیچیده‌کردن مسیر لغو اشتراک و نمایش شمارش معکوس جعلی، سه نمونهٔ پرتکرارند که هر سه بار شناختی کاربر را در لحظهٔ تصمیم دستکاری می‌کنند.\n\n"
                           "۴. نقدها و چالش‌ها\nمرز میان طراحی بد و طراحی فریبنده مبهم است؛ اثبات نیت طراح دشوار است؛ یافته‌های خزش وب به بافت یک کشور و یک دوره محدود است؛ خطر اتهام‌زنی به طراحی‌های صرفاً نامتعارف وجود دارد؛ و انگیزهٔ رقابتی، بنگاه‌ها را به تقلید این الگوها سوق می‌دهد.\n\n"
                           "۵. سیر تاریخی\nبرنول (۲۰۱۰) واژه را رواج داد، گری و همکاران (۲۰۱۸) آن را به مفهوم طراحی نظام‌مند ارتقا دادند، ماتور و همکاران (۲۰۱۹) اندازه‌گیری در مقیاس را ممکن کردند و مقررات اروپایی، الگوهای فریبنده را به موضوع الزام قانونی تبدیل کرد.\n\n"
                           "۶. جایگاه در بحث روز\nممیزی رابط کاربری و الزام به طراحی منصفانه اکنون بخشی از نظارت بر پلتفرم‌هاست و پژوهش الگوهای فریبنده به سنجه‌های استاندارد و ابزارهای تشخیص خودکار مجهز شده است."),
    ),
    "MC-281": dict(
        needs_enrichment=False,
        level="کلان",
        related_approaches="عدالت الگوریتمی؛ سوگیری در یادگیری ماشین؛ تقاطع‌گرایی؛ اقتصاد سیاسی جستجو؛ نژاد و فناوری.",
        recommended_sources="«الگوریتم‌های سرکوب» (نوبل، ۲۰۱۸)؛ «جستجوی گوگل: فرانمایی به‌عنوان سازوکار نامرئی‌سازی» (نوبل، ۲۰۱۳)؛ پژوهش‌های عدالت الگوریتمی و ممیزی موتور جستجو.",
        detailed_analysis=("۱. بنیان و منطق نظری\nنوبل (۲۰۱۸) در کتاب «الگوریتم‌های سرکوب» استدلال کرد موتورهای جستجو ابزار بی‌طرف دانش نیستند، بلکه محصول مناسبات تجاری، تاریخی و نژادی‌اند. "
                           "او پیش‌تر در مقالهٔ ۲۰۱۳ نشان داده بود جستجوی عبارت‌های مرتبط با زنان سیاه‌پوست، محتوای جنسی و تحقیرآمیز را در صدر می‌آورد و این «فرانمایی» به نامرئی‌سازی مدنی می‌انجامد.\n\n"
                           "۲. ساختارهای مفهومی\nسوگیری الگوریتمی، فرانمایی، نامرئی‌سازی، تقاطع‌گرایی، اقتصاد تبلیغاتی جستجو و عدالت داده سازه‌های محوری‌اند. "
                           "فرانمایی و نامرئی‌سازی دو روی یک سازوکارند: نمایش افراطی کلیشه و حذف هم‌زمان تجربهٔ واقعی.\n\n"
                           "۳. نمونه‌های تحلیلی\nوقتی الگوریتم برای تعامل و درآمد تبلیغاتی بهینه می‌شود، محتوایی را بالا می‌آورد که کاربران پیش‌تر بیشتر کلیک کرده‌اند؛ چون دادهٔ تاریخی متأثر از کلیشه است، نتیجه چرخهٔ بازخوردی تقویت کلیشه است.\n\n"
                           "۴. نقدها و چالش‌ها\nتحلیل بر نمونه‌های محدود و مشاهدهٔ شخصی استوار است و دادهٔ سیستماتیک کمی دارد؛ تعمیم از یک موتور جستجو به کل بوم داده مسئله‌ساز است؛ نقش عاملیت و مقاومت کاربران کم‌رنگ می‌شود؛ و تمرکز بر بازنمایی، سازوکارهای اقتصادی و مقرراتی را در حاشیه نگه می‌دارد.\n\n"
                           "۵. سیر تاریخی\nمقالهٔ ۲۰۱۳ مبنای تجربی کتاب شد، کتاب ۲۰۱۸ آن را به چارچوبی برای عدالت الگوریتمی و سیاست داده گسترش داد و پژوهش‌های بعدی مفهوم ممیزی الگوریتمی را نهادینه کردند.\n\n"
                           "۶. جایگاه در بحث روز\nبا فراگیرشدن هوش مصنوعی مولد، پرسش نوبل دربارهٔ بازنمایی و کلیشه به تولید تصویر و متن گسترش یافته و به یکی از محورهای اصلی بحث عدالت داده تبدیل شده است."),
    ),
}

NAME_FIX = {}

YEAR_FIX = {
    "MC-264": "Reichheld 1996 verified via archive.org; removed media-economics template analysis and garbled recommendations",
    "MC-274": "year=2014 (Eyal & Hoover 2014); replaced governance-mechanism template analysis and unrelated media-policy recommendations",
    "MC-275": "year=2009 (Fogg 2009); replaced governance-mechanism template analysis and unrelated media-policy recommendations",
    "MC-276": "year=2010 (Brignull coinage); Gray 2018 and Mathur 2019 verified; replaced governance template analysis and unrelated recommendations",
    "MC-281": "year=2018 (Noble 2018); replaced data-capitalism template analysis and surveillance-capitalism recommendations",
}
