# -*- coding: utf-8 -*-
"""Batch 105: full documentation for MC-657, MC-658, MC-659, MC-661."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch105-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch105_theory.json"

S = {
    "MC-657": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Channel Expansion Theory and the Experiential Nature of Media Richness Perceptions",
             title_fa="نظریه گسترش کانال و سرشت تجربی ادراک غنای رسانه",
             authors="Carlson, J. R.; Zmud, R. W.", year=1999,
             publisher="Academy of Management Journal",
             doi=None, url="https://psycnet.apa.org/record/2014-20281-003",
             language="en", isbn=None,
             citation="Carlson, J. R., & Zmud, R. W. (1999). Channel expansion theory and the experiential nature of media richness perceptions. Academy of Management Journal, 42(2), 153-170.",
             locator="42(2):153-170", locator_type="page_range",
             supports="experience with channel, topic, partner and context expands perceived richness", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Examining the Scope of Channel Expansion",
             title_fa="بررسی دامنه گسترش کانال",
             authors="D'Urso, S. C.; Rains, S. A.", year=2008,
             publisher="Management Communication Quarterly",
             doi=None, url=None, language="en", isbn=None,
             citation="D'Urso, S. C., & Rains, S. A. (2008). Examining the scope of channel expansion. Management Communication Quarterly, 21(4), 486-507.",
             locator="21(4):486-507", locator_type="page_range",
             supports="extension of channel expansion to new and traditional media", verified=False),
    ],
    "MC-658": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Emergence of Scaling in Random Networks",
             title_fa="پیدایش مقیاس‌پذیری در شبکه‌های تصادفی",
             authors="Barabasi, A.-L.; Albert, R.", year=1999,
             publisher="Science",
             doi="10.1126/science.286.5439.509",
             url="https://www.science.org/doi/10.1126/science.286.5439.509",
             language="en", isbn=None,
             citation="Barabasi, A.-L., & Albert, R. (1999). Emergence of scaling in random networks. Science, 286(5439), 509-512. https://doi.org/10.1126/science.286.5439.509",
             locator="286(5439):509-512", locator_type="page_range",
             supports="growth plus preferential attachment yields scale-free networks", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Statistical Mechanics of Complex Networks",
             title_fa="مکانیک آماری شبکه‌های پیچیده",
             authors="Albert, R.; Barabasi, A.-L.", year=2002,
             publisher="Reviews of Modern Physics",
             doi=None, url=None, language="en", isbn=None,
             citation="Albert, R., & Barabasi, A.-L. (2002). Statistical mechanics of complex networks. Reviews of Modern Physics, 74(1), 47-97.",
             locator="74(1):47-97", locator_type="page_range",
             supports="review of scale-free network models and degree distributions", verified=False),
    ],
    "MC-659": [
        dict(kind="BOOK_CHAPTER",
             title_en="Friendship as a Social Process: A Substantive and Methodological Analysis",
             title_fa="دوستی به‌عنوان یک فرایند اجتماعی: تحلیلی ماهوی و روش‌شناختی",
             authors="Lazarsfeld, P. F.; Merton, R. K.", year=1954,
             publisher="Van Nostrand",
             doi=None, url="https://www.scirp.org/reference/ReferencesPapers?ReferenceID=2418200",
             language="en", isbn=None,
             citation="Lazarsfeld, P. F., & Merton, R. K. (1954). Friendship as a social process: A substantive and methodological analysis. In M. Berger, T. Abel, & C. H. Page (Eds.), Freedom and control in modern society (pp. 18-66). Van Nostrand.",
             locator="pp. 18-66", locator_type="PAGE",
             supports="coining of homophily: similarity breeds connection", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Birds of a Feather: Homophily in Social Networks",
             title_fa="کبوتران هم‌پر: همگونی در شبکه‌های اجتماعی",
             authors="McPherson, M.; Smith-Lovin, L.; Cook, J. M.", year=2001,
             publisher="Annual Review of Sociology",
             doi=None, url=None, language="en", isbn=None,
             citation="McPherson, M., Smith-Lovin, L., & Cook, J. M. (2001). Birds of a feather: Homophily in social networks. Annual Review of Sociology, 27, 415-444.",
             locator="27:415-444", locator_type="page_range",
             supports="review of status and value homophily across social dimensions", verified=False),
    ],
    "MC-661": [
        dict(kind="BOOK",
             title_en="Bowling Alone: The Collapse and Revival of American Community",
             title_fa="تنها بولینگ: فروپاشی و احیای اجتماع آمریکایی",
             authors="Putnam, R. D.", year=2000, publisher="Simon & Schuster",
             doi=None, url="http://www.csun.edu/~rdavids/350fall08/350readings/Putnam_Bowling_Alone.pdf",
             language="en", isbn=None,
             citation="Putnam, R. D. (2000). Bowling alone: The collapse and revival of American community. Simon & Schuster.",
             locator="work", locator_type="work",
             supports="distinction between bonding and bridging social capital", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Strength of Weak Ties",
             title_fa="قوت پیوندهای ضعیف",
             authors="Granovetter, M. S.", year=1973,
             publisher="American Journal of Sociology",
             doi=None, url=None, language="en", isbn=None,
             citation="Granovetter, M. S. (1973). The strength of weak ties. American Journal of Sociology, 78(6), 1360-1380.",
             locator="78(6):1360-1380", locator_type="page_range",
             supports="bridging value of weak ties across groups", verified=False),
    ],
}

ENRICH = {
    "MC-657": {
        "summary": "(کارلسون و زومود، ۱۹۹۹) نظریه گسترش کانال می‌گوید ادراک غنای یک رسانه ویژگی ثابت آن نیست و با تجربه کاربر گسترش می‌یابد. چهار نوع تجربه در این گسترش نقش دارند: تجربه با کانال، تجربه با موضوع پیام، تجربه با طرف ارتباط و تجربه با زمینه سازمانی. هرچه این تجربه‌ها بیشتر شود، کاربر همان رسانه را غنی‌تر می‌بیند و آن را برای پیام‌های مبهم‌تر به کار می‌برد. کارلسون و زومود این را با ایمیل آزمودند: رسانه‌ای که در آغاز کم‌غنا دیده می‌شد، با تجربه برای موضوع‌های پیچیده‌تر مناسب شمرده شد. نظریه، سلسله‌مراتب ثابت غنا را به فرایندی یادگیرانه بدل می‌کند.",
        "definition": "نظریه گسترش کانال، چارچوبی است که ادراک غنای رسانه را نتیجه تجربه کاربر با کانال، موضوع، طرف ارتباط و زمینه سازمانی می‌داند و رشد این تجربه را عامل استفاده از رسانه برای پیام‌های مبهم‌تر می‌شمارد.",
        "main_problem": "مسئله این است که چرا رسانه‌ای که برای یک کارمند کم‌غنا است، برای همکار باتجربه همان سازمان غنی به نظر می‌رسد. پاسخ، تفاوت تجربه است. پرسش دوم، پیامد سازمانی است: چگونه می‌توان پذیرش ابزار ارتباطی نو را با یادگیری تسریع کرد.",
        "mechanism": "۱. تجربه با کانال: کاربر قواعد بیان، محدودیت‌ها و امکانات رسانه را می‌آموزد.\n۲. تجربه با موضوع: شناخت واژگان و پیش‌فرض‌های موضوع، پیام کوتاه را کافی می‌کند.\n۳. تجربه با طرف ارتباط: شناخت طرف مقابل، نیاز به توضیح را کم می‌کند.\n۴. تجربه با زمینه: شناخت هنجارها و تاریخچه سازمان، ابهام را کاهش می‌دهد.\n۵. ادراک غنا: ترکیب این تجربه‌ها، رسانه را در ذهن کاربر غنی‌تر می‌سازد.\n۶. گسترش کاربرد: کاربر رسانه را برای پیام‌های مبهم‌تر به کار می‌برد و تجربه بیشتر می‌شود.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا خبرنگاری که سال‌ها با یک پیام‌رسان با منابع خود کار کرده، همان ابزار را برای گفت‌وگوی حساس کافی می‌داند و چرا همکار تازه‌وارد همان ابزار را نامناسب می‌بیند. در استقرار ابزار تحریریه، آموزش موضوع و زمینه، بخشی از پذیرش فناوری است. نکته مهم این است که ادراک غنا با عملکرد واقعی یکی نیست؛ کاربر ممکن است رسانه را غنی‌تر از توان واقعی آن ببیند.",
        "assumptions": [
            "غنای ادراک‌شده، ثابت نیست.",
            "تجربه، ادراک غنا را می‌سازد.",
            "گسترش تجربه، کاربرد برای پیام مبهم را ممکن می‌کند.",
        ],
        "principles": [
            "تجربه کانال، موضوع و طرف ارتباط مهم است.",
            "ادراک غنا با عملکرد یکی نیست.",
            "یادگیری سازمانی، پذیرش ابزار را تسریع می‌کند.",
        ],
        "critiques": [
            "۱. ادراک در برابر عملکرد: غنای ادراک‌شده لزوماً نتیجه بهتر نمی‌دهد.\n۲. خودگزارشی: سنجش ادراک به پرسش‌نامه وابسته است.\n۳. شواهد طولی: آزمون بلندمدت گسترش کم است.\n۴. زمینه: نقش فرهنگ سازمانی کم‌تر بررسی شده است.\n۵. هم‌پوشانی: مرز با غنای رسانه و نفوذ اجتماعی روشن نیست.",
        ],
        "applications": [
            "استقرار ابزار تحریریه: آموزش موضوع و زمینه برای پذیرش.",
            "تیم‌های پراکنده: ساخت تجربه مشترک پیش از سپردن کارهای پیچیده.",
            "روابط با منبع خبری: سرمایه‌گذاری بر تجربه طرف ارتباط.",
            "آموزش خبرنگار: شناخت محدودیت‌های کانال.",
        ],
        "evolution": "کارلسون و زومود در ۱۹۹۹ نظریه را در مجله آکادمی مدیریت عرضه کردند و ادراک غنا را تجربی دیدند. بعدها پژوهش‌های آزمون دامنه، نظریه را به رسانه‌های نو و سنتی گسترد و بر تفاوت ادراک و عملکرد تأکید کرد.",
        "key_concepts": [
            "گسترش کانال (Channel Expansion)",
            "غنای ادراک‌شده (Perceived Richness)",
            "تجربه کانال (Channel Experience)",
            "تجربه موضوع (Topic Experience)",
            "تجربه طرف ارتباط (Partner Experience)",
            "زمینه سازمانی (Organizational Context)",
        ],
        "studies": [
            "Carlson, J. R., & Zmud, R. W. (1999). Channel expansion theory. Academy of Management Journal, 42(2), 153-170.",
            "D'Urso, S. C., & Rains, S. A. (2008). Examining the scope of channel expansion. Management Communication Quarterly, 21(4), 486-507.",
        ],
        "theorists": "جان کارلسون؛ رابرت زومود",
        "theorists_text": "کارلسون و زومود (۱۹۹۹)",
        "year": 1999,
        "model": "تجربه کانال + موضوع + طرف ارتباط + زمینه → ادراک غنای بیشتر → کاربرد برای پیام مبهم‌تر → تجربه بیشتر.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nکارلسون و زومود غنای رسانه را از ویژگی ابزار جدا و به تجربه کاربر گره زدند. نوآوری چارچوب، تبدیل سلسله‌مراتب ثابت غنا به فرایند یادگیری است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با پرسش‌نامه ادراک غنا، سابقه استفاده و آزمون انتخاب رسانه انجام می‌شود. پژوهشی که تنها ادراک را می‌سنجد، عملکرد را از دست می‌دهد؛ و پژوهشی که تجربه را با مدت عضویت یکی می‌گیرد، کیفیت یادگیری را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در استقرار ابزار ارتباطی است، اما باید با ارزیابی عملکرد تکمیل شود. ادراک غنای بی مهارت، به اعتماد بیش از اندازه به رسانه کم‌غنا می‌انجامد.",
        "critique_text": "\n".join([
            "۱. ادراک در برابر عملکرد: نتیجه بهتر تضمین نمی‌شود.",
            "۲. خودگزارشی: سنجش ادراک سوگیرانه است.",
            "۳. شواهد طولی: آزمون بلندمدت کم است.",
            "۴. زمینه: فرهنگ سازمانی کم بررسی شده است.",
            "۵. هم‌پوشانی: مرز با نظریه‌های مجاور روشن نیست.",
        ]),
        "example_text": "خبرنگاری که دو سال با یک پیام‌رسان با منابع خود کار کرده، پیام کوتاه را برای هماهنگی مصاحبه حساس کافی می‌داند؛ همکار تازه‌وارد همان پیام را مبهم می‌یابد و تماس صوتی ترجیح می‌دهد.",
    },
    "MC-658": {
        "summary": "(باراباشی و آلبرت، ۱۹۹۹) نظریه اتصال ترجیحی توضیح می‌دهد چرا شبکه‌های واقعی، توزیع درجه نامتقارن و مقیاس‌پذیر دارند. شبکه با افزودن گره‌های نو رشد می‌کند و هر گره نو با احتمالی متناسب با درجه گره‌های موجود به آن‌ها وصل می‌شود؛ گره‌های پرپیوند، شانس بیشتری برای پیوند تازه دارند. این سازوکار «ثروتمند ثروتمندتر می‌شود» نامیده می‌شود و به شکل‌گیری قطب‌های شبکه می‌انجامد. باراباشی و آلبرت نشان دادند رشد به‌همراه اتصال ترجیحی، توزیع توانی درجه می‌سازد. مدل آن‌ها، شبکه‌های بی‌مقیاس را به‌جای شبکه تصادفی به الگوی رایج شبکه‌های پیچیده بدل کرد. این مدل، پژوهش شبکه پیچیده را از شبکه تصادفی جدا کرد.",
        "definition": "اتصال ترجیحی، سازوکاری است که در آن گره تازه با احتمال متناسب با درجه گره‌های موجود به آن‌ها متصل می‌شود و در نتیجه گره‌های پرپیوند سهم نامتناسبی از پیوندهای نو را جذب می‌کنند.",
        "main_problem": "مسئله این است که چرا در شبکه‌های واقعی شمار اندکی گره، بیشتر پیوندها را در دست دارند. پاسخ، رشد به‌همراه اتصال ترجیحی است. پرسش دوم، تعمیم است: آیا هر شبکه واقعی بی‌مقیاس است یا سازوکارهای دیگری نیز در کارند.",
        "mechanism": "۱. رشد: شبکه با افزودن گره تازه گسترده می‌شود.\n۲. اتصال ترجیحی: گره نو به گره‌های پرپیوند با احتمال بیشتر وصل می‌شود.\n۳. ثروتمند ثروتمندتر: هر پیوند تازه، شانس پیوند بعدی را زیاد می‌کند.\n۴. قطب‌سازی: شمار اندکی گره به قطب بدل می‌شوند.\n۵. توزیع توانی: توزیع درجه دنباله سنگین می‌یابد و مقیاس مشخصی ندارد.\n۶. حساسیت به ترتیب: گره‌های زودتر، شانس بیشتری برای قطب شدن دارند.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا شمار اندکی از حساب‌ها بیشتر توجه را جذب می‌کنند، چرا شبکه پیوند خبری حول چند سایت پرپیوند متمرکز می‌شود و چرا الگوریتم پیشنهاد که پیوندهای موجود را تقویت می‌کند، قطب‌سازی را شدت می‌بخشد. نکته مهم این است که قطب‌سازی پیامد رشد است، نه لزوماً کیفیت؛ گره پرپیوند همیشه معتبرترین گره نیست.",
        "assumptions": [
            "شبکه‌ها رشد می‌کنند.",
            "پیوند نو با درجه گره موجود همبسته است.",
            "رشد و اتصال ترجیحی با هم توزیع توانی می‌سازند.",
        ],
        "principles": [
            "پرپیوندها پیوند بیشتری جذب می‌کنند.",
            "ترتیب ورود، سرنوشت گره را شکل می‌دهد.",
            "قطب‌سازی پیامد رشد است، نه معیار کیفیت.",
        ],
        "critiques": [
            "۱. تعمیم: همه شبکه‌های واقعی بی‌مقیاس نیستند.\n۲. تناسب: تناسب، آمادگی و پیری گره نادیده می‌ماند.\n۳. سنجش: برازش توزیع توانی به داده محدود، شکننده است.\n۴. جایگزین‌ها: توزیع لگ‌نرمال یا نمایی نیز گزارش شده است.\n۵. جبر ساختاری: عاملیت و محتوای پیوند کم‌تر دیده می‌شود.",
        ],
        "applications": [
            "تحلیل شبکه خبری: شناسایی قطب‌های پیوند و تمرکز توجه.",
            "طراحی پلتفرم: پیش‌بینی اثر الگوریتم پیشنهاد بر تمرکز.",
            "بازاریابی تأثیرگذار: شناخت مزیت انباشته حساب‌های پرپیوند.",
            "مطالعه استناد: تحلیل تمرکز استناد در چند نشریه.",
        ],
        "evolution": "باراباشی و آلبرت در ۱۹۹۹ مدل را در مجله علم عرضه کردند. بعدها پژوهش شبکه‌های پیچیده، تناسب، آمادگی، پیری گره و توزیع‌های جایگزین را به مدل افزود و کاربرد آن را به شبکه اجتماعی، استناد و وب گسترد.",
        "key_concepts": [
            "اتصال ترجیحی (Preferential Attachment)",
            "شبکه بی‌مقیاس (Scale-Free Network)",
            "توزیع توانی درجه (Power-Law Degree Distribution)",
            "قطب شبکه (Network Hub)",
            "رشد شبکه (Network Growth)",
            "ثروتمند ثروتمندتر (Rich-Get-Richer)",
        ],
        "studies": [
            "Barabasi, A.-L., & Albert, R. (1999). Emergence of scaling in random networks. Science, 286(5439), 509-512.",
            "Albert, R., & Barabasi, A.-L. (2002). Statistical mechanics of complex networks. Reviews of Modern Physics, 74(1), 47-97.",
        ],
        "theorists": "آلبرت‌لاسلو باراباشی؛ رکا آلبرت",
        "theorists_text": "باراباشی و آلبرت (۱۹۹۹)",
        "year": 1999,
        "model": "رشد شبکه + اتصال متناسب با درجه → قطب‌سازی → توزیع توانی درجه → شبکه بی‌مقیاس.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nباراباشی و آلبرت شبکه تصادفی را با رشد و اتصال ترجیحی جایگزین کردند. نوآوری چارچوب، توضیح قطب‌سازی از سازوکار ساده رشد است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با برازش توزیع درجه، تحلیل رشد و شبیه‌سازی انجام می‌شود. پژوهشی که تنها توزیع توانی را برازش می‌دهد، سازوکار را اثبات نمی‌کند؛ و پژوهشی که هر قطب را نتیجه اتصال ترجیحی می‌داند، تناسب و کیفیت را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در تحلیل تمرکز توجه است، اما باید با محتوای پیوند تکمیل شود. قطب بی اعتبار، بیشترین توجه را جذب می‌کند.",
        "critique_text": "\n".join([
            "۱. تعمیم: همه شبکه‌ها بی‌مقیاس نیستند.",
            "۲. تناسب: آمادگی و پیری گره نادیده می‌ماند.",
            "۳. سنجش: برازش توانی شکننده است.",
            "۴. جایگزین‌ها: توزیع لگ‌نرمال نیز گزارش شده است.",
            "۵. جبر ساختاری: عاملیت کم‌تر دیده می‌شود.",
        ]),
        "example_text": "شبکه‌ای خبری که تازه راه افتاده، پیوندهایش را به چند سایت پرمخاطب می‌دهد؛ همان چند سایت با هر پیوند نو مشهورتر می‌شوند و سهم توجه عمومی متمرکز می‌ماند.",
    },
    "MC-659": {
        "summary": "(لازارسفلد و مرتون، ۱۹۵۴) همگونی به گرایش پیوندهای اجتماعی به شکل‌گیری میان افراد مشابه گفته می‌شود. لازارسفلد و مرتون این مفهوم را در مطالعه دوستی‌ها صورت‌بندی کردند و نشان دادند شباهت در وضعیت اجتماعی، پیوند را آسان می‌کند. همگونی وضعیتی به شباهت در ویژگی‌هایی مانند نژاد، جنسیت، سن و تحصیلات و همگونی ارزشی به شباهت در نگرش و باور اشاره دارد. همگونی از ترجیح فردی و فرصت ساختاری هر دو برمی‌خیزد. در رسانه، همگونی با انتخاب گزینشی، حباب فیلتر و هم‌صدایی شبکه‌های اجتماعی گره می‌خورد. همگونی، هم فرصت و هم محدودیت را در شبکه بازتولید می‌کند و نابرابری اطلاعاتی را پایدار می‌سازد.",
        "definition": "همگونی، گرایش پیوندهای اجتماعی به شکل‌گیری میان افرادی است که در ویژگی‌های وضعیتی یا ارزشی به هم شبیه‌اند و در نتیجه شبکه‌های شخصی را همگن‌تر از جمعیت عمومی می‌سازد.",
        "main_problem": "مسئله این است که چرا شبکه‌های اجتماعی افراد با وجود جمعیت متنوع، همگن‌اند. پاسخ، هم‌آمیزی ترجیح و فرصت است. پرسش دوم، علیت است: آیا افراد مشابه را انتخاب می‌کنند یا محیط، فرصت آشنایی با مشابه‌ها را می‌سازد.",
        "mechanism": "۱. ترجیح فردی: افراد با مشابه‌ها راحت‌تر و بیشتر ارتباط می‌گیرند.\n۲. فرصت ساختاری: محله، مدرسه و محل کار، دامنه آشنایی را محدود می‌کنند.\n۳. هم‌آمیزی شناختی: تعادل و هماهنگی نگرش، پیوند را پایدار می‌کند.\n۴. شکل‌گیری و گسست پیوند: پیوند مشابه پایدارتر است و پیوند نامشابه بیشتر می‌شکند.\n۵. بازخورد شبکه‌ای: شبکه همگن، فرصت آشنایی با ناهمسان را کم می‌کند.\n۶. تقویت الگوریتمی: پیشنهاد محتوای مشابه، همگونی را تشدید می‌کند.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا مخاطبان خبر در جریان‌های هم‌سو قرار می‌گیرند، چرا شبکه‌های اجتماعی به هم‌صدایی گرایش دارند و چرا کمپین‌های تنوع در تحریریه، همگونی استخدام را هدف می‌گیرند. نکته مهم این است که همگونی همیشه پیامد بد نیست؛ پیوند همگن، اعتماد و پشتیبانی می‌سازد، اما تنوع اطلاعات را کم می‌کند.",
        "assumptions": [
            "شباهت، شکل‌گیری پیوند را آسان می‌کند.",
            "هم ترجیح و هم فرصت ساختاری نقش دارند.",
            "شبکه شخصی معمولاً همگن‌تر از جمعیت است.",
        ],
        "principles": [
            "شباهت، پیوند می‌سازد.",
            "فرصت ساختاری، دامنه انتخاب را محدود می‌کند.",
            "همگونی، تنوع اطلاعات را کم می‌کند.",
        ],
        "critiques": [
            "۱. سنجش: همگونی از داده خودگزارشی و نمونه محدود برمی‌آید.\n۲. علیت: تفکیک ترجیح از فرصت دشوار است.\n۳. مبالغه: شدت حباب فیلتر بیش از شواهد گزارش می‌شود.\n۴. زمینه: الگوی همگونی در فرهنگ‌ها متفاوت است.\n۵. پیامد: همگونی می‌تواند پشتیبان هم باشد، نه فقط تهدید.",
        ],
        "applications": [
            "مخاطب‌شناسی خبر: تحلیل هم‌صدایی جریان‌های خبری.",
            "طراحی پلتفرم: سنجش اثر پیشنهاد بر تنوع مواجهه.",
            "سیاست تنوع: هدف‌گذاری استخدام و منابع تحریریه.",
            "سواد رسانه‌ای: شناخت محدودیت شبکه شخصی.",
        ],
        "evolution": "لازارسفلد و مرتون در ۱۹۵۴ مفهوم را در مطالعه دوستی صورت‌بندی کردند. بعدها مرور مک‌فرسون و همکاران در ۲۰۰۱ همگونی وضعیتی و ارزشی را در شبکه‌های اجتماعی نظام‌مند کرد و پژوهش حباب فیلتر، مفهوم را به رسانه شبکه‌ای گسترد.",
        "key_concepts": [
            "همگونی (Homophily)",
            "همگونی وضعیتی (Status Homophily)",
            "همگونی ارزشی (Value Homophily)",
            "هم‌صدایی (Echo Chamber)",
            "حباب فیلتر (Filter Bubble)",
            "مواجهه گزینشی (Selective Exposure)",
        ],
        "studies": [
            "Lazarsfeld, P. F., & Merton, R. K. (1954). Friendship as a social process. In Freedom and control in modern society (pp. 18-66). Van Nostrand.",
            "McPherson, M., Smith-Lovin, L., & Cook, J. M. (2001). Birds of a feather. Annual Review of Sociology, 27, 415-444.",
        ],
        "theorists": "پل لازارسفلد؛ رابرت مرتون",
        "theorists_text": "لازارسفلد و مرتون (۱۹۵۴)",
        "year": 1954,
        "model": "ترجیح مشابهت + فرصت ساختاری → شکل‌گیری پیوند همگن → پایداری بیشتر → شبکه همگن‌تر از جمعیت.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nلازارسفلد و مرتون دوستی را فرایندی اجتماعی دیدند و شباهت را شرط شکل‌گیری آن خواندند. نوآوری چارچوب، پیوند تحلیل شبکه با وضعیت اجتماعی است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با شاخص همگونی، تحلیل شبکه و مقایسه با خط پایه انجام می‌شود. پژوهشی که همگونی را بی خط پایه می‌سنجد، فرصت ساختاری را از دست می‌دهد؛ و پژوهشی که هر هم‌صدایی را حباب می‌خواند، پیوند همگن پشتیبان را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در تحلیل تنوع مواجهه است، اما باید با داده رفتار واقعی تکمیل شود. همگونی بی سنجش خط پایه، به تشخیصی اغراق‌شده بدل می‌شود.",
        "critique_text": "\n".join([
            "۱. سنجش: داده خودگزارشی و نمونه محدود.",
            "۲. علیت: ترجیح از فرصت تفکیک نمی‌شود.",
            "۳. مبالغه: شدت حباب بیش از شواهد گزارش می‌شود.",
            "۴. زمینه: الگوی همگونی فرهنگی است.",
            "۵. پیامد: همگونی می‌تواند پشتیبان باشد.",
        ]),
        "example_text": "روزنامه‌نگاری که بیشتر منابع خود را از یک طیف فکری برگزیده، در جریان یک مناقشه تنها صداهای هم‌سو را می‌شنود؛ افزودن دو منبع ناهمسان به فهرست ثابت، تنوع اطلاعاتی او را بالا می‌برد.",
    },
    "MC-661": {
        "summary": "(پاتنام، ۲۰۰۰) پاتنام سرمایه اجتماعی را به دو گونه تفکیک می‌کند: پیوندی و پلی. سرمایه پیوندی درون گروه‌های همگن، پیوندهای نزدیک، اعتماد ضخیم و پشتیبانی متقابل می‌سازد و به «از پس هم برآمدن» کمک می‌کند. سرمایه پلی میان گروه‌های ناهمگن پل می‌زند، اطلاعات و فرصت تازه می‌آورد و به «پیش رفتن» یاری می‌رساند. پاتنام این دو را به چسب اجتماعی و روغن اجتماعی تشبیه کرد. هر دو برای جامعه لازم‌اند، اما یکی بدون دیگری به بسته‌شدن یا پراکندگی می‌انجامد. رسانه‌ها می‌توانند هر دو گونه را تقویت یا تضعیف کنند. پژوهش رسانه می‌تواند هر دو گونه را جداگانه بسنجد و اثر سکوها را بر تعادل آن‌ها بررسی کند. تفکیک دوگانه اما، به طیف کامل پیوندها وفادار نیست.",
        "definition": "تفکیک پیوند درون‌گروهی و میان‌گروهی، دو گونه سرمایه اجتماعی را از هم جدا می‌کند: پیوندهای نزدیک و همگن که پشتیبانی می‌سازند و پیوندهای دور و ناهمگن که اطلاعات و فرصت تازه می‌آورند.",
        "main_problem": "مسئله این است که چرا برخی اجتماع‌ها منسجم اما بسته و برخی باز اما بی‌پشتیبان‌اند. پاسخ، ترکیب نامتوازن دو گونه سرمایه است. پرسش دوم، نقش رسانه است: کدام رسانه پیوند درون‌گروهی و کدام پیوند میان‌گروهی می‌سازد.",
        "mechanism": "۱. پیوند درون‌گروهی: رابطه نزدیک، مکرر و مبتنی بر اعتماد ضخیم.\n۲. پیوند میان‌گروهی: رابطه دور، گاه یک‌باره و مبتنی بر اعتماد نازک.\n۳. جریان اطلاعات: پیوند میان‌گروهی اطلاعات تازه و ناهمگون می‌آورد.\n۴. پشتیبانی: پیوند درون‌گروهی در بحران پشتیبانی می‌دهد.\n۵. هنجار و نظارت: پیوند نزدیک، نظارت اجتماعی و تعهد می‌سازد.\n۶. ترکیب: اجتماع سالم هر دو گونه را در توازن دارد.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا رسانه محلی پیوند درون‌گروهی می‌سازد، چرا رسانه فرامرزی پل میان گروه‌ها می‌زند و چرا شبکه اجتماعی می‌تواند هر دو را هم‌زمان تقویت یا تضعیف کند. نکته مهم این است که تفکیک دوگانه، طیف را ساده می‌کند؛ بسیاری از پیوندها هر دو ویژگی را دارند و سنجش، نیازمند شاخص چندبعدی است.",
        "assumptions": [
            "سرمایه اجتماعی دو گونه متمایز دارد.",
            "پیوند نزدیک و دور کارکردهای متفاوت دارند.",
            "توازن دو گونه، اجتماع سالم می‌سازد.",
        ],
        "principles": [
            "پیوند نزدیک، پشتیبانی می‌سازد.",
            "پیوند دور، اطلاعات تازه می‌آورد.",
            "توازن دو گونه لازم است.",
        ],
        "critiques": [
            "۱. دوگانه‌سازی: طیف پیوندها به دو دسته فروکاسته می‌شود.\n۲. سنجش: شاخص یکدست برای دو گونه وجود ندارد.\n۳. سوگیری هنجاری: پیوند پلی به‌طور هنجاری برتر دیده می‌شود.\n۴. زمینه: کارکرد پیوند به فرهنگ و شبکه وابسته است.\n۵. رسانه دیجیتال: پیوند ضعیف و قوی در هم می‌آمیزد.",
        ],
        "applications": [
            "روزنامه‌نگاری محلی: تقویت پیوند درون‌گروهی اجتماع.",
            "رسانه فرامرزی: ساخت پل میان گروه‌ها و منابع.",
            "طراحی پلتفرم: سنجش اثر بر هر دو گونه سرمایه.",
            "سیاست اجتماعی: توازن پشتیبانی و گشودگی.",
        ],
        "evolution": "پاتنام در ۲۰۰۰ تفکیک پیوندی و پلی را در کتاب تنها بولینگ عرضه کرد. بعدها پژوهش سرمایه اجتماعی، مفهوم را به رسانه اجتماعی، اجتماع محلی و سیاست تنوع گسترد و نقد دوگانه‌سازی را پیش کشید.",
        "key_concepts": [
            "سرمایه پیوندی (Bonding Social Capital)",
            "سرمایه پلی (Bridging Social Capital)",
            "اعتماد ضخیم (Thick Trust)",
            "اعتماد نازک (Thin Trust)",
            "پیوند ضعیف (Weak Tie)",
            "همگونی شبکه (Network Homophily)",
        ],
        "studies": [
            "Putnam, R. D. (2000). Bowling alone. Simon & Schuster.",
            "Granovetter, M. S. (1973). The strength of weak ties. American Journal of Sociology, 78(6), 1360-1380.",
        ],
        "theorists": "رابرت پاتنام",
        "theorists_text": "پاتنام (۲۰۰۰)",
        "year": 2000,
        "model": "پیوند نزدیک و همگن → سرمایه پیوندی (پشتیبانی)؛ پیوند دور و ناهمگن → سرمایه پلی (اطلاعات)؛ توازن دو گونه → اجتماع سالم.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nپاتنام سرمایه اجتماعی را از انجمن‌های مدنی به ساختار پیوندها برد و دو کارکرد متفاوت را تفکیک کرد. نوآوری چارچوب، پیوند سرمایه اجتماعی با تنوع و پشتیبانی است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با شاخص شبکه، اعتماد و مشارکت انجام می‌شود. پژوهشی که تنها شمار پیوند را می‌سنجد، کیفیت آن را از دست می‌دهد؛ و پژوهشی که پل را برتر می‌داند، کارکرد پشتیبانی پیوند نزدیک را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در تحلیل نقش رسانه در اجتماع است، اما باید با داده شبکه تکمیل شود. پل بی اعتماد، به تماس بی تعهد بدل می‌شود.",
        "critique_text": "\n".join([
            "۱. دوگانه‌سازی: طیف پیوندها به دو دسته فروکاسته می‌شود.",
            "۲. سنجش: شاخص یکدست وجود ندارد.",
            "۳. سوگیری هنجاری: پل برتر دیده می‌شود.",
            "۴. زمینه: کارکرد پیوند فرهنگی است.",
            "۵. رسانه دیجیتال: پیوند ضعیف و قوی در هم می‌آمیزد.",
        ]),
        "example_text": "رسانه محلی با پوشش رویدادهای محله، پیوند درون‌گروهی می‌سازد؛ همان رسانه با دعوت از صداهای مهاجر و اقلیت، پل میان گروه‌ها می‌زند و دو گونه سرمایه را هم‌زمان تقویت می‌کند.",
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
    "MC-658": ("اتصال ترجیحی", "Preferential Attachment",
               "canonical_name repaired: 'Preferential Stickiness' is a mistranslation of preferential attachment (Barabasi-Albert model)"),
    "MC-659": ("همگونی (هوموفیلی)", "Homophily",
               "canonical_name repaired: label conflated homophily with conformity; aligned to Lazarsfeld & Merton homophily"),
    "MC-661": ("تفکیک پیوند درون‌گروهی و میان‌گروهی", "Bonding-Bridging Tie Distinction",
               "canonical_name repaired: 'Sticky-Bridge Tie Distinction' was a garbled rendering of Putnam's bonding/bridging distinction"),
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
                                       "verified": n_verified, "batch": 105}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH105 THEORY DONE")


if __name__ == "__main__":
    main()
