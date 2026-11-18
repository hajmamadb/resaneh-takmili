# -*- coding: utf-8 -*-
"""Batch 98: full documentation for MC-571, MC-586, MC-589, MC-592."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch98-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch98_theory.json"

S = {
    "MC-571": [
        dict(kind="BOOK",
             title_en="Belief, Attitude, Intention and Behavior: An Introduction to Theory and Research",
             title_fa="باور، نگرش، قصد و رفتار: درآمدی بر نظریه و پژوهش",
             authors="Fishbein, M.; Ajzen, I.", year=1975, publisher="Addison-Wesley",
             doi=None, url=None, language="en", isbn=None,
             citation="Fishbein, M., & Ajzen, I. (1975). Belief, attitude, intention and behavior: An introduction to theory and research. Addison-Wesley.",
             locator="work", locator_type="work",
             supports="intention as proximal predictor / attitude and subjective norm determinants", verified=True),
        dict(kind="BOOK",
             title_en="Understanding Attitudes and Predicting Social Behavior",
             title_fa="فهم نگرش‌ها و پیش‌بینی رفتار اجتماعی",
             authors="Ajzen, I.; Fishbein, M.", year=1980, publisher="Prentice-Hall",
             doi=None, url=None, language="en", isbn=None,
             citation="Ajzen, I., & Fishbein, M. (1980). Understanding attitudes and predicting social behavior. Prentice-Hall.",
             locator="work", locator_type="work",
             supports="behavioral and normative belief structure / measurement correspondence", verified=False),
    ],
    "MC-586": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Problem Solving and Communicative Action: A Situational Theory of Problem Solving",
             title_fa="حل مسئله و کنش ارتباطی: نظریه موقعیتی حل مسئله",
             authors="Kim, J.-N.; Grunig, J. E.", year=2011, publisher="Journal of Communication",
             doi="10.1111/j.1460-2466.2010.01529.x",
             url="https://academic.oup.com/joc/article-abstract/61/1/120/4098453",
             language="en", isbn=None,
             citation="Kim, J.-N., & Grunig, J. E. (2011). Problem solving and communicative action: A situational theory of problem solving. Journal of Communication, 61(1), 120-149. https://doi.org/10.1111/j.1460-2466.2010.01529.x",
             locator="61(1):120-149", locator_type="page_range",
             supports="situational motivation / six communicative behaviors / referent criterion", verified=True),
        dict(kind="BOOK",
             title_en="Managing Public Relations",
             title_fa="مدیریت روابط عمومی",
             authors="Grunig, J. E.; Hunt, T.", year=1984, publisher="Holt, Rinehart and Winston",
             doi=None, url=None, language="en", isbn=None,
             citation="Grunig, J. E., & Hunt, T. (1984). Managing public relations. Holt, Rinehart and Winston.",
             locator="work", locator_type="work",
             supports="situational theory of publics baseline", verified=False),
    ],
    "MC-589": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Public Issue Management: The New Science",
             title_fa="مدیریت مسائل عمومی: علم تازه",
             authors="Chase, W. H.", year=1977, publisher="Public Relations Journal",
             doi=None, url=None, language="en", isbn=None,
             citation="Chase, W. H. (1977). Public issue management: The new science. Public Relations Journal, 33(10).",
             locator="33(10)", locator_type="page_range",
             supports="five-stage issue management model / anticipatory response", verified=True),
        dict(kind="BOOK",
             title_en="Issue Management: Origins of the Future",
             title_fa="مدیریت مسئله: خاستگاه‌های آینده",
             authors="Chase, W. H.", year=1984, publisher="Issue Action Publications",
             doi=None, url="https://books.google.com/books/about/Issue_Management.html?id=neYOAQAAMAAJ",
             language="en", isbn=None,
             citation="Chase, W. H. (1984). Issue management: Origins of the future. Issue Action Publications.",
             locator="work", locator_type="work",
             supports="institutionalization of issue management practice", verified=False),
    ],
    "MC-592": [
        dict(kind="BOOK",
             title_en="Cannibals with Forks: The Triple Bottom Line of 21st Century Business",
             title_fa="آدم‌خواران با چنگال: سه‌گانه سود در کسب‌وکار سده بیست‌ویکم",
             authors="Elkington, J.", year=1997, publisher="Capstone",
             doi=None, url="https://www.johnelkington.com/archive/TBL-elkington-chapter.pdf",
             language="en", isbn=None,
             citation="Elkington, J. (1997). Cannibals with forks: The triple bottom line of 21st century business. Capstone.",
             locator="work", locator_type="work",
             supports="triple bottom line / economic, social and environmental performance", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Partnerships from Cannibals to Forks: Globalization and the Triple Bottom Line",
             title_fa="مشارکت‌ها از آدم‌خواران تا چنگال: جهانی‌شدن و سه‌گانه سود",
             authors="Elkington, J.", year=1998, publisher="UNEP Industry and Environment",
             doi=None, url=None, language="en", isbn=None,
             citation="Elkington, J. (1998). Partnerships from cannibals to forks: Globalization and the triple bottom line. UNEP Industry and Environment, 21(1), 18-21.",
             locator="21(1):18-21", locator_type="page_range",
             supports="sustainability accounting and partnership framing", verified=False),
    ],
}

ENRICH = {
    "MC-571": {
        "summary": "(فیشبین و آیزن، ۱۹۷۵؛ آیزن و فیشبین، ۱۹۸۰) نظریه عمل منطقی می‌گوید رفتار ارادی را نمی‌توان مستقیم از نگرش پیش‌بینی کرد؛ حلقه واسط، قصد رفتاری است. قصد از دو مسیر ساخته می‌شود: نگرش نسبت به رفتار، و هنجار ذهنی یعنی تصور فرد از انتظار اطرافیان. نگرش خود از باورهای رفتاری و ارزیابی پیامدها می‌آید و هنجار از باورهای هنجاری و انگیزه همنوایی. نظریه بر رفتار ارادی و سنجش متناظر باور، قصد و رفتار استوار است؛ همین تدقیق، پیش‌بینی رفتار را از حدس نگرشی جدا کرد.",
        "definition": "نظریه عمل منطقی، مدلی است که رفتار ارادی را تابع قصد رفتاری می‌داند و قصد را از ترکیب نگرش نسبت به رفتار و هنجار ذهنی درباره آن رفتار توضیح می‌دهد.",
        "main_problem": "مسئله این است که دانستن نگرش فرد، رفتار او را با دقت پیش‌بینی نمی‌کند. پاسخ فیشبین و آیزن، افزودن دو حلقه میانی است: قصد و هنجار اجتماعی. پرسش دوم، محدودیت است: چه رفتاری در دایره اراده فرد قرار می‌گیرد و چه رفتاری به مهارت و فرصت وابسته است.",
        "mechanism": "۱. باورهای رفتاری: فرد پیامدهای رفتار و ارزش آن پیامدها را می‌سنجد و نگرش نسبت به رفتار شکل می‌گیرد.\n۲. باورهای هنجاری: فرد انتظار افراد مهم را درباره آن رفتار تصور می‌کند.\n۳. انگیزه همنوایی: وزن هر مرجع، از تمایل فرد به همراستایی با او می‌آید.\n۴. هنجار ذهنی: ترکیب باورهای هنجاری و انگیزه همنوایی، فشار اجتماعی ادراک‌شده می‌سازد.\n۵. قصد رفتاری: نگرش و هنجار ذهنی، قصد را می‌سازند و قصد، رفتار ارادی را هدایت می‌کند.\n۶. تناظر سنجش: باور، نگرش، قصد و رفتار باید به یک کنش، هدف، زمینه و زمان اشاره کنند؛ بی این تناظر، پیش‌بینی معتبر نیست.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا پیام آموزشی، نگرش را تغییر می‌دهد اما رفتار را نه، چرا همسالان و خانواده بر قصد مصرف یا اشتراک‌گذاری اثر می‌گذارند و چرا کمپین‌ها باید نگرش و هنجار را هم‌زمان هدف بگیرند. نکته مهم این است که فاصله قصد تا رفتار، خود موضوع پژوهشی مستقل است.",
        "assumptions": [
            "رفتار مورد مطالعه، ارادی و در کنترل فرد است.",
            "قصد، نزدیک‌ترین پیش‌بینی‌کننده رفتار است.",
            "نگرش و هنجار ذهنی، دو مسیر مستقل ساخت قصدند.",
        ],
        "principles": [
            "تناظر سنجش، شرط اعتبار پیش‌بینی است.",
            "نگرش بی هنجار، رفتار را توضیح نمی‌دهد.",
            "قصد، حلقه واسط لازم است.",
        ],
        "critiques": [
            "۱. فاصله قصد تا رفتار: عوامل موقعیتی می‌توانند قصد را بی‌اثر کنند.\n۲. فرض ارادی‌بودن: بسیاری از رفتارهای رسانه‌ای به عادت و دسترسی وابسته‌اند.\n۳. عقلانیت محدود: مدل، تصمیم را بیش از اندازه محاسبه‌گر می‌بیند.\n۴. تناظر دشوار: ساخت پرسش‌نامه با تناظر کامل، عملاً پیچیده است.\n۵. تنوع فرهنگی: وزن هنجار ذهنی در جوامع جمع‌گرا و فردگرا یکسان نیست.",
        ],
        "applications": [
            "کمپین سلامت: هدف‌گیری هم‌زمان نگرش و هنجار اجتماعی.",
            "پیش‌آزمون تبلیغ: سنجش قصد خرید پیش از انتشار.",
            "پژوهش مخاطب: تحلیل قصد اشتراک‌گذاری محتوا.",
            "ارزیابی کمپین: تفکیک تغییر نگرش از تغییر رفتار.",
        ],
        "evolution": "فیشبین در دهه ۱۹۶۰ پیوند نگرش و رفتار را بازتعریف کرد و با آیزن در ۱۹۷۵ نظریه عمل منطقی را نظام‌مند ساخت. آیزن در ۱۹۸۵ و ۱۹۹۱ با افزودن کنترل رفتاری ادراک‌شده، نظریه رفتار برنامه‌ریزی‌شده را برای رفتارهای غیرارادی گسترد.",
        "key_concepts": [
            "قصد رفتاری (Behavioral Intention)",
            "نگرش نسبت به رفتار (Attitude toward Behavior)",
            "هنجار ذهنی (Subjective Norm)",
            "باور رفتاری (Behavioral Belief)",
            "انگیزه همنوایی (Motivation to Comply)",
            "اصل تناظر (Correspondence Principle)",
        ],
        "studies": [
            "Fishbein, M., & Ajzen, I. (1975). Belief, attitude, intention and behavior. Addison-Wesley.",
            "Ajzen, I., & Fishbein, M. (1980). Understanding attitudes and predicting social behavior. Prentice-Hall.",
        ],
        "theorists": "مارتین فیشبین؛ آیسک آیزن",
        "theorists_text": "مارتین فیشبین و آیسک آیزن (۱۹۷۵؛ ۱۹۸۰)",
        "year": 1975,
        "model": "مدل عمل منطقی: باورهای رفتاری + ارزیابی پیامد → نگرش؛ باورهای هنجاری + انگیزه همنوایی → هنجار ذهنی؛ نگرش + هنجار → قصد → رفتار ارادی.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nفیشبین و آیزن نگرش را از رفتار جدا کردند و قصد را به‌عنوان حلقه واسط معرفی کردند. نوآوری چارچوب، جایگزینی پیش‌بینی خام نگرشی با مدلی دو‌مسیره و سنجش‌پذیر است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با پرسش‌نامه باور، نگرش، هنجار و قصد و با تناظر کنش و زمینه انجام می‌شود. پژوهشی که تنها نگرش را می‌سنجد، هنجار را از دست می‌دهد؛ و پژوهشی که تناظر را رعایت نمی‌کند، ضریب پیش‌بینی ضعیف می‌گیرد و آن را به ضعف نظریه نسبت می‌دهد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در طراحی کمپین است، اما باید با تحلیل بافت تکمیل شود. برای رفتارهای عادت‌محور یا وابسته به دسترسی، افزودن کنترل ادراک‌شده یا تحلیل زیرساخت لازم است.",
        "critique_text": "\n".join([
            "۱. فاصله قصد تا رفتار: عوامل موقعیتی قصد را بی‌اثر می‌کنند.",
            "۲. فرض ارادی‌بودن: بسیاری از رفتارها عادت‌محورند.",
            "۳. عقلانیت محدود: مدل، تصمیم را محاسبه‌گر می‌بیند.",
            "۴. تناظر دشوار: ساخت ابزار با تناظر کامل پیچیده است.",
            "۵. تنوع فرهنگی: وزن هنجار در جوامع یکسان نیست.",
        ]),
        "example_text": "کمپینی نگرش مخاطب به واکسن را مثبت می‌کند، اما قصد واکسیناسیون تغییر نمی‌کند. بررسی نشان می‌دهد هنجار ذهنی در گروه همسالان منفی مانده است؛ نگرش مثبت بی هنجار حمایتگر، به رفتار نمی‌رسد.",
    },
    "MC-586": {
        "summary": "(کیم و گرونیگ، ۲۰۱۱) نظریه موقعیتی حل مسئله، گسترش نظریه جمهورهاست و می‌پرسد چرا افراد در برابر یک مسئله به کنش ارتباطی دست می‌زنند. سه متغیر مستقل، وضعیت را می‌سازند: تشخیص مسئله، تشخیص محدودیت و تشخیص درگیری. ترکیب این سه، انگیزه موقعیتی حل مسئله را می‌سازد و انگیزه، کنش ارتباطی را در شش شکل ممکن می‌سازد: جست‌وجو، توجه، پیشگیری، اجازه، بازفرست و اشتراک. معیار مرجع نیز جهت تفسیر مسئله را تعیین می‌کند.",
        "definition": "نظریه موقعیتی حل مسئله، چارچوبی است که کنش ارتباطی افراد را تابع انگیزه موقعیتی حل مسئله می‌داند؛ انگیزه‌ای که از تشخیص مسئله، تشخیص محدودیت و تشخیص درگیری ساخته می‌شود.",
        "main_problem": "مسئله این است که چرا در برابر یک مسئله عمومی، برخی فعالانه اطلاعات می‌جویند و بازنشر می‌کنند و برخی بی‌اعتنا می‌مانند. پاسخ در وضعیت ادراک‌شده فرد است، نه در ویژگی پایدار او. پرسش دوم، طراحی مداخله است: چه تغییری در تشخیص محدودیت، فرد را از انفعال به کنش می‌برد.",
        "mechanism": "۱. تشخیص مسئله: فرد مسئله را می‌بیند و آن را مسئله‌ای واقعی می‌داند؛ این، نخستین شرط کنش است.\n۲. تشخیص محدودیت: هر مانع ادراک‌شده، انگیزه کنش را کاهش می‌دهد، حتی اگر مسئله مهم باشد.\n۳. تشخیص درگیری: هرچه فرد خود را درگیر مسئله بداند، انگیزه بیشتری برای پردازش و کنش دارد.\n۴. انگیزه موقعیتی: ترکیب سه تشخیص، آمادگی روانی برای حل مسئله می‌سازد.\n۵. شش کنش ارتباطی: جست‌وجوی فعال و توجه منفعل برای کسب اطلاعات؛ پیشگیری و اجازه برای گزینش اطلاعات؛ بازفرست و اشتراک برای انتقال اطلاعات.\n۶. معیار مرجع: باورها و تجربه پیشین، چارچوب تفسیر مسئله و انتخاب کنش را شکل می‌دهند.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا یک بحران برای گروهی مسئله است و برای گروهی نه، چرا کاهش موانع ادراکی مؤثرتر از افزایش حجم پیام است و چرا مخاطب فعال، هم مصرف‌کننده و هم توزیع‌کننده اطلاعات می‌شود. نکته مهم این است که کنش ارتباطی، تابع وضعیت است، نه تابع شخصیت.",
        "assumptions": [
            "کنش ارتباطی، واکنشی به وضعیت ادراک‌شده مسئله است.",
            "سه تشخیص، انگیزه موقعیتی را می‌سازند.",
            "موانع ادراک‌شده، کنش را بیش از اهمیت مسئله مهار می‌کنند.",
        ],
        "principles": [
            "مسئله دیده‌شده، شرط نخست کنش است.",
            "کاهش محدودیت ادراکی، مؤثرتر از تکرار پیام است.",
            "درگیری ادراک‌شده، عمق پردازش را تعیین می‌کند.",
        ],
        "critiques": [
            "۱. تمرکز بر ادراک: تفاوت ادراک و واقعیت محدودیت کم‌رنگ می‌شود.\n۲. سنجش شش کنش: تفکیک تجربی شکل‌های کنش دشوار است.\n۳. زمینه غربی: بیشتر شواهد از دموکراسی‌های لیبرال می‌آید.\n۴. کم‌توجهی به الگوریتم: دسترسی به اطلاعات در پلتفرم، محدودیت را بازتعریف می‌کند.\n۵. پیوند با کنش غیرارتباطی: مدل، کنش سیاسی و مدنی بیرون از ارتباط را کمتر توضیح می‌دهد.",
        ],
        "applications": [
            "روابط عمومی: بخش‌بندی مخاطب بر پایه وضعیت مسئله.",
            "ارتباطات بحران: کاهش موانع ادراکی برای کنش محافظتی.",
            "سلامت عمومی: طراحی پیام متناسب با سطح درگیری گروه‌ها.",
            "فعالیت مدنی: تحلیل مسیر از درگیری تا بازنشر و کنش جمعی.",
        ],
        "evolution": "گرونیگ در ۱۹۶۸ نظریه موقعیتی جمهورها را با سه متغیر پایه ساخت و در ۱۹۸۴ آن را نظام‌مند کرد. کیم و گرونیگ در ۲۰۱۱ با افزودن انگیزه موقعیتی، شش کنش ارتباطی و معیار مرجع، مدل را به نظریه‌ای عمومی درباره حل مسئله گستردند.",
        "key_concepts": [
            "تشخیص مسئله (Problem Recognition)",
            "تشخیص محدودیت (Constraint Recognition)",
            "تشخیص درگیری (Involvement Recognition)",
            "انگیزه موقعیتی حل مسئله (Situational Motivation)",
            "کنش ارتباطی (Communicative Action)",
            "معیار مرجع (Referent Criterion)",
        ],
        "studies": [
            "Kim, J.-N., & Grunig, J. E. (2011). Problem solving and communicative action. Journal of Communication, 61(1), 120-149.",
            "Grunig, J. E., & Hunt, T. (1984). Managing public relations. Holt, Rinehart and Winston.",
        ],
        "theorists": "جونگ-نام کیم؛ جیمز گرونیگ",
        "theorists_text": "کیم و گرونیگ (۲۰۱۱)",
        "year": 2011,
        "model": "مدل موقعیتی: تشخیص مسئله + تشخیص محدودیت + تشخیص درگیری + معیار مرجع → انگیزه موقعیتی → شش کنش ارتباطی (جست‌وجو، توجه، پیشگیری، اجازه، بازفرست، اشتراک).",
        "detailed_analysis": "۱. بنیان و منطق نظری\nنظریه، نظریه جمهورها را از توصیف چهار جمهور به مدلی فرایندی درباره انگیزه و کنش ارتقا می‌دهد. نوآوری چارچوب، تفکیک شکل‌های کنش ارتباطی و افزودن معیار مرجع است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با مقیاس سه تشخیص، انگیزه و شش کنش انجام می‌شود. پژوهشی که تنها انگیزه را می‌سنجد، شکل کنش را از دست می‌دهد؛ و پژوهشی که تنها یک کنش را می‌سنجد، دامنه رفتار ارتباطی را کم‌نمایی می‌کند.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در توضیح تفاوت واکنش گروه‌هاست، اما باید با تحلیل پلتفرم تکمیل شود. در محیط الگوریتمی، دسترسی و نمایش، خود یک محدودیت ادراکی تازه می‌سازد.",
        "critique_text": "\n".join([
            "۱. تمرکز بر ادراک: تفاوت ادراک و واقعیت کم‌رنگ می‌شود.",
            "۲. سنجش شش کنش: تفکیک تجربی دشوار است.",
            "۳. زمینه غربی: شواهد از دموکراسی‌های لیبرال می‌آید.",
            "۴. کم‌توجهی به الگوریتم: دسترسی، محدودیت را بازتعریف می‌کند.",
            "۵. کنش غیرارتباطی: کنش سیاسی کمتر توضیح داده می‌شود.",
        ]),
        "example_text": "شهروندی که آلودگی هوای محله را زندگی خود می‌داند، درباره آن فعالانه جست‌وجو می‌کند و گزارش‌ها را بازمی‌فرستد. همسایه‌ای با درگیری کمتر، تنها به‌طور تصادفی خبر را می‌بیند؛ تفاوت در تشخیص، شکل کنش را تعیین کرده است.",
    },
    "MC-589": {
        "summary": "(چیس، ۱۹۷۷؛ چیس و جونز) مدیریت مسائل، رویکردی پیشنگر است که سازمان را از واکنش به رویداد به پیش‌بینی و شکل‌دهی مسائل عمومی می‌برد. چیس مدل پنج‌مرحله‌ای را پیشنهاد کرد: شناسایی مسئله، تحلیل، تدوین گزینه‌های راهبرد، برنامه کنش و ارزیابی نتیجه. در این چارچوب، مسئله عمومی چرخه عمر دارد و سازمان می‌تواند در مرحله شکل‌گیری بر تعریف آن اثر بگذارد. مدیریت مسئله، پلی میان راهبرد سازمان و فرایند سیاست‌گذاری است.",
        "definition": "مدیریت مسائل، فرایند نظام‌مند شناسایی، تحلیل و پاسخ به مسائل عمومی است که بر سازمان اثر می‌گذارند یا سازمان بر آن‌ها اثر می‌گذارد؛ فرایندی پیشنگر که هدف آن شکل‌دهی دستور کار عمومی است.",
        "main_problem": "مسئله این است که سازمان‌ها اغلب پس از بحران واکنش نشان می‌دهند، زمانی که تعریف مسئله و انتظارات عمومی تثبیت شده است. پرسش چیس این است که چگونه می‌توان پیش از تثبیت، مسئله را دید و بر تعریف آن اثر گذاشت. پرسش دوم، مشروعیت است: مرز میان مدیریت مسئله و دستکاری دستور کار کجاست.",
        "mechanism": "۱. شناسایی زودهنگام: پایش نشانه‌های ضعیف در رسانه، قانون‌گذاری و گروه‌های ذی‌نفع، مسئله را پیش از بلوغ آشکار می‌کند.\n۲. تحلیل: سازمان ذی‌نفعان، شدت، دامنه و مسیر احتمالی مسئله را ارزیابی می‌کند.\n۳. گزینه‌های راهبرد: پاسخ می‌تواند انطباق، گفت‌وگو، تغییر رویه یا مشارکت در تدوین قاعده باشد.\n۴. برنامه کنش: انتخاب پیام، کانال و مخاطب برای اثرگذاری بر تعریف و اولویت مسئله.\n۵. ارزیابی: نتیجه با شاخص‌های دستور کار، نگرش ذی‌نفعان و تصمیم عمومی سنجیده می‌شود.\n۶. چرخه عمر: مسئله از ظهور به بلوغ و سپس نهادینه‌شدن یا فروکش می‌رود و راهبرد باید با مرحله هم‌خوان باشد.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا سازمان‌ها پیش از تصویب قانون، گزارش و گفت‌وگو منتشر می‌کنند، چرا تعریف مسئله در رسانه بر سرنوشت آن اثر می‌گذارد و چرا واکنش دیرهنگام گران تمام می‌شود. نکته مهم این است که مدیریت مسئله، در بهترین شکل خود گفت‌وگوی زودهنگام است، نه سرکوب انتقاد.",
        "assumptions": [
            "مسائل عمومی چرخه عمر قابل پیش‌بینی دارند.",
            "اثرگذاری بر تعریف مسئله، پیش از تثبیت ممکن است.",
            "سازمان و محیط عمومی در رابطه دوطرفه‌اند.",
        ],
        "principles": [
            "پیشگیری ارزان‌تر از واکنش است.",
            "تعریف مسئله، سرنوشت آن را تعیین می‌کند.",
            "پایش نشانه‌های ضعیف، شرط شناسایی زودهنگام است.",
        ],
        "critiques": [
            "۱. خطر دستکاری: مدیریت مسئله می‌تواند به مدیریت ادراک و انحراف توجه بدل شود.\n۲. تمرکز شرکتی: چارچوب از تجربه سازمان‌های بزرگ و منافع خصوصی برخاسته است.\n۳. کم‌توجهی به قدرت: توان اثرگذاری میان بازیگران نابرابر توزیع شده است.\n۴. سنجش اثر: نسبت‌دادن تغییر دستور کار به یک برنامه دشوار است.\n۵. ابهام مرز اخلاقی: تفکیک گفت‌وگوی مشروع از کارزار بی‌اعتمادساز روشن نیست.",
        ],
        "applications": [
            "روابط عمومی راهبردی: پایش زودهنگام و طراحی پاسخ پیش از بحران.",
            "سیاست عمومی: تحلیل نقش سازمان‌ها در شکل‌گیری دستور کار.",
            "مسئولیت اجتماعی: گفت‌وگوی زودهنگام با ذی‌نفعان.",
            "پژوهش رسانه: تحلیل چرخه عمر مسئله در پوشش خبری.",
        ],
        "evolution": "چیس در ۱۹۷۷ مدیریت مسئله را علم تازه خواند و مدل پنج‌مرحله‌ای را پیش نهاد؛ در ۱۹۸۴ آن را در کتابی درباره خاستگاه‌های آینده نهادینه کرد. پژوهش بعدی، مدیریت مسئله را با تحلیل ذی‌نفعان، سیاست عمومی و رسانه پیوند داد.",
        "key_concepts": [
            "مسئله عمومی (Public Issue)",
            "چرخه عمر مسئله (Issue Life Cycle)",
            "مدیریت پیشنگر (Anticipatory Management)",
            "برنامه کنش مسئله (Issue Action Program)",
            "دستور کار عمومی (Public Agenda)",
            "ذی‌نفع (Stakeholder)",
        ],
        "studies": [
            "Chase, W. H. (1977). Public issue management: The new science. Public Relations Journal, 33(10).",
            "Chase, W. H. (1984). Issue management: Origins of the future. Issue Action Publications.",
        ],
        "theorists": "دبلیو. هاوارد چیس؛ بری جونز",
        "theorists_text": "هاوارد چیس (۱۹۷۷؛ ۱۹۸۴)",
        "year": 1979,
        "model": "مدل پنج‌مرحله‌ای: شناسایی مسئله → تحلیل → گزینه‌های راهبرد → برنامه کنش → ارزیابی، در چارچوب چرخه عمر مسئله و رابطه دوطرفه با محیط عمومی.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nچیس مدیریت مسئله را از واکنش به پیش‌بینی منتقل کرد و آن را در کنار راهبرد سازمان نشاند. نوآوری چارچوب، تبدیل پایش محیط به فرایندی با مرحله و شاخص است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با رصد نشانه‌های زودهنگام، تحلیل ذی‌نفعان و ارزیابی تغییر دستور کار انجام می‌شود. پژوهشی که تنها خروجی رسانه‌ای را می‌سنجد، مسیر تعریف مسئله را از دست می‌دهد؛ و پژوهشی که تنها نیت سازمان را می‌خواند، اثر عمومی را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در توضیح زمان‌بندی پاسخ است، اما باید با تحلیل قدرت تکمیل شود. بدون شفافیت، مدیریت مسئله به مدیریت ادراک بدل می‌شود.",
        "critique_text": "\n".join([
            "۱. خطر دستکاری: مدیریت مسئله به مدیریت ادراک بدل می‌شود.",
            "۲. تمرکز شرکتی: چارچوب از تجربه سازمان‌های بزرگ برخاسته است.",
            "۳. کم‌توجهی به قدرت: توان بازیگران نابرابر است.",
            "۴. سنجش اثر: نسبت‌دادن تغییر دستور کار به یک برنامه دشوار است.",
            "۵. ابهام اخلاقی: مرز گفت‌وگو و کارزار بی‌اعتمادساز روشن نیست.",
        ]),
        "example_text": "شرکتی پیش از آنکه ضوابط بسته‌بندی به قانون بدل شود، داده‌های بازیافت را منتشر و با تنظیم‌گر گفت‌وگو می‌کند. همین کنش زودهنگام، تعریف مسئله را از «تخلف شرکت» به «زیرساخت بازیافت» جابه‌جا می‌کند.",
    },
    "MC-592": {
        "summary": "(الکینگتون، ۱۹۹۷) سه‌گانه سود، کارکرد سازمان را نه تنها با سود اقتصادی، بلکه با عملکرد اجتماعی و زیست‌محیطی می‌سنجد. الکینگتون این چارچوب را برای حسابداری پایداری ساخت تا ارزش‌آفرینی سازمان در سه سطح هم‌زمان دیده شود. او هشدار داد گزارش‌دهی تک‌بعدی، هزینه‌های پنهان را از دید خارج می‌کند. سه‌گانه سود، ابزار سنجش است، نه فقط شعار؛ و همین خصلت، آن را از مسئولیت اجتماعی تزئینی جدا می‌کند.",
        "definition": "سه‌گانه سود، چارچوبی برای سنجش عملکرد سازمان در سه بُعد اقتصادی، اجتماعی و زیست‌محیطی است؛ چارچوبی که ارزش را نه در سود سهامدار، بلکه در مجموع اثر سازمان بر ذی‌نفعان و محیط می‌بیند.",
        "main_problem": "مسئله این است که سنجش تک‌بعدی سود، هزینه‌های اجتماعی و زیست‌محیطی را نامرئی می‌کند. پرسش الکینگتون این است که چگونه می‌توان عملکرد را بی آنکه به یک عدد تقلیل یابد، مقایسه‌پذیر کرد. پرسش دوم، انگیزه است: پایداری چه زمانی به رویه سازمانی بدل می‌شود و چه زمانی در گزارش می‌ماند.",
        "mechanism": "۱. سه بُعد هم‌زمان: سود اقتصادی، سرمایه اجتماعی و اثر زیست‌محیطی، هم‌زمان و در یک چارچوب سنجیده می‌شوند.\n۲. حسابداری پایداری: شاخص‌ها به‌گونه‌ای ساخته می‌شوند که هزینه‌های بیرونی در حساب سازمان دیده شود.\n۳. ذی‌نفعان چندگانه: سازمان در برابر سهامدار، کارمند، جامعه محلی و محیط پاسخ‌گو است.\n۴. ارزش بلندمدت: پایداری به‌عنوان شرط دوام کسب‌وکار، نه هزینه اضافی، بازتعریف می‌شود.\n۵. پیوند با راهبرد: شاخص‌های سه‌گانه در تصمیم سرمایه‌گذاری و زنجیره تأمین وارد می‌شوند.\n۶. خطر فاصله گزارش و عمل: بدون سازوکار راستی‌آزمایی، سه‌گانه سود به ابزار تبلیغاتی بدل می‌شود.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا گزارش پایداری به قالبی ارتباطی رایج بدل شده، چرا سبزشویی رشد می‌کند و چرا مخاطب به ادعای پایداری بدگمان است. نکته مهم این است که سه‌گانه سود، معیار سنجش است و بدون داده قابل راستی‌آزمایی، تنها روایت می‌سازد.",
        "assumptions": [
            "عملکرد سازمان در سه بُعد قابل سنجش است.",
            "هزینه‌های اجتماعی و زیست‌محیطی را می‌توان در حساب سازمان آورد.",
            "پایداری بلندمدت، به دوام کسب‌وکار کمک می‌کند.",
        ],
        "principles": [
            "سنجش تک‌بعدی، هزینه پنهان می‌سازد.",
            "پاسخگویی به ذی‌نفعان چندگانه، شرط مشروعیت است.",
            "گزارش بی راستی‌آزمایی، تبلیغ است.",
        ],
        "critiques": [
            "۱. دشواری تجمیع: سه بُعد ناهمگون را نمی‌توان به یک عدد تقلیل داد.\n۲. خطر سبزشویی: چارچوب به ابزار روایت شرکتی بدل می‌شود.\n۳. تمرکز داوطلبانه: گزارش‌دهی بدون الزام قانونی، گزینشی می‌ماند.\n۴. کم‌توجهی به ساختار: پایداری بدون تغییر زنجیره ارزش و مدل کسب‌وکار سطحی می‌ماند.\n۵. بازنگری خود بنیان‌گذار: الکینگتون خود بعدها هشدار داد چارچوب به ابزاری برای حسابداری سود بدل شده است.",
        ],
        "applications": [
            "گزارشگری پایداری: تدوین شاخص‌های سه‌بعدی و راستی‌آزمایی‌پذیر.",
            "ارتباطات شرکتی: اجتناب از ادعای پایداری بی داده.",
            "سرمایه‌گذاری: ارزیابی ریسک اجتماعی و زیست‌محیطی.",
            "سیاست عمومی: الزام گزارش‌دهی و مقایسه‌پذیری.",
        ],
        "evolution": "الکینگتون اصطلاح سه‌گانه سود را در ۱۹۹۴ به کار برد و در ۱۹۹۷ در کتابی درباره کسب‌وکار سده بیست‌ویکم گسترد. این چارچوب به گزارش‌دهی پایداری راه یافت و در دهه ۲۰۱۰ با نقد سبزشویی و بازنگری خود بنیان‌گذار روبه‌رو شد.",
        "key_concepts": [
            "سه‌گانه سود (Triple Bottom Line)",
            "حسابداری پایداری (Sustainability Accounting)",
            "سبزشویی (Greenwashing)",
            "ذی‌نفعان (Stakeholders)",
            "گزارش‌دهی پایداری (Sustainability Reporting)",
            "هزینه بیرونی (Externality)",
        ],
        "studies": [
            "Elkington, J. (1997). Cannibals with forks: The triple bottom line of 21st century business. Capstone.",
            "Elkington, J. (1998). Partnerships from cannibals to forks. UNEP Industry and Environment, 21(1), 18-21.",
        ],
        "theorists": "جان الکینگتون",
        "theorists_text": "جان الکینگتون (۱۹۹۷)",
        "year": 1997,
        "model": "مدل سه‌گانه: عملکرد اقتصادی + عملکرد اجتماعی + عملکرد زیست‌محیطی → حسابداری پایداری → ارزش بلندمدت، با شرط راستی‌آزمایی برای جلوگیری از سبزشویی.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nالکینگتون سنجش عملکرد را از سود سهامدار به اثر سه‌بعدی گسترد و آن را به راهبرد کسب‌وکار گره زد. نوآوری چارچوب، تبدیل پایداری از ارزش اخلاقی به معیار سنجش است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با شاخص‌های اقتصادی، اجتماعی و زیست‌محیطی و با راستی‌آزمایی بیرونی انجام می‌شود. پژوهشی که تنها گزارش شرکت را می‌خواند، فاصله گفتار و عمل را از دست می‌دهد؛ و پژوهشی که تنها یک بُعد را می‌سنجد، ادعای سه‌گانه را نقض می‌کند.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در پیوند دادن ارتباطات شرکتی با سنجه است، اما باید با تحلیل قدرت تکمیل شود. بدون الزام و راستی‌آزمایی، سه‌گانه سود به قالبی تبلیغاتی بدل می‌شود.",
        "critique_text": "\n".join([
            "۱. دشواری تجمیع: سه بُعد ناهمگون به یک عدد تقلیل نمی‌یابد.",
            "۲. خطر سبزشویی: چارچوب به روایت شرکتی بدل می‌شود.",
            "۳. تمرکز داوطلبانه: گزارش‌دهی گزینشی می‌ماند.",
            "۴. کم‌توجهی به ساختار: پایداری سطحی می‌ماند.",
            "۵. بازنگری بنیان‌گذار: ابزار به حسابداری سود بدل شده است.",
        ]),
        "example_text": "شرکتی در گزارش پایداری، کاهش انتشار کربن را برجسته می‌کند اما شرایط کار تأمین‌کنندگان را نمی‌گوید. سه‌گانه سود می‌پرسد بُعد اجتماعی کجاست؛ گزارش بی آن بُعد، ادعای پایداری نیست.",
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
    "MC-571": ("نظریه عمل منطقی", "Theory of Reasoned Action",
               "canonical_name_en repaired: 'Rational Action Theory' aligned to Fishbein & Ajzen's theory of reasoned action"),
    "MC-586": ("نظریه موقعیتی حل مسئله", "Situational Theory of Problem Solving",
               "canonical_name_en repaired: 'Situational Problem-Solving Theory' aligned to Kim & Grunig's STOPS"),
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
                                       "verified": n_verified, "batch": 98}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH98 THEORY DONE")


if __name__ == "__main__":
    main()
