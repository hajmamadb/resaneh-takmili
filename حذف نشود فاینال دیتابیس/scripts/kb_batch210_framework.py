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
                                       "verified": n_verified, "batch": 210}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH210 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
