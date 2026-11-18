# -*- coding: utf-8 -*-
"""Batch 99: full documentation for MC-596, MC-612, MC-613, MC-614.

MC-608 (زنجیره ارزش / Value Chain) is skipped: duplicate of MC-152.
"""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch99-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch99_theory.json"

S = {
    "MC-596": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Boundary Spanning Roles and Organization Structure",
             title_fa="نقش‌های مرزگذری و ساختار سازمان",
             authors="Aldrich, H. E.; Herker, D.", year=1977,
             publisher="Academy of Management Review",
             doi="10.5465/amr.1977.4409044",
             url="https://journals.aom.org/doi/10.5465/amr.1977.4409044",
             language="en", isbn=None,
             citation="Aldrich, H. E., & Herker, D. (1977). Boundary spanning roles and organization structure. Academy of Management Review, 2(2), 217-230. https://doi.org/10.5465/amr.1977.4409044",
             locator="2(2):217-230", locator_type="page_range",
             supports="boundary roles as information processing and external representation / role conflict and ambiguity", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Boundary Spanning Individuals: Their Role in Information Transfer and Their Antecedents",
             title_fa="افراد مرزگذر: نقش آن‌ها در انتقال اطلاعات و پیشایندهایشان",
             authors="Tushman, M. L.; Scanlan, T. J.", year=1981,
             publisher="Academy of Management Journal",
             doi=None, url=None, language="en", isbn=None,
             citation="Tushman, M. L., & Scanlan, T. J. (1981). Boundary spanning individuals: Their role in information transfer and their antecedents. Academy of Management Journal, 24(2), 289-305.",
             locator="24(2):289-305", locator_type="page_range",
             supports="individual boundary spanners as information transfer agents / antecedents", verified=False),
    ],
    "MC-612": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="A Theory of Human Motivation",
             title_fa="نظریه انگیزش انسانی",
             authors="Maslow, A. H.", year=1943, publisher="Psychological Review",
             doi="10.1037/h0054346",
             url="https://psychclassics.yorku.ca/Maslow/motivation.htm",
             language="en", isbn=None,
             citation="Maslow, A. H. (1943). A theory of human motivation. Psychological Review, 50(4), 370-396. https://doi.org/10.1037/h0054346",
             locator="50(4):370-396", locator_type="page_range",
             supports="five-level need hierarchy / prepotency principle", verified=True),
        dict(kind="BOOK",
             title_en="Motivation and Personality",
             title_fa="انگیزش و شخصیت",
             authors="Maslow, A. H.", year=1954, publisher="Harper & Brothers",
             doi=None, url=None, language="en", isbn=None,
             citation="Maslow, A. H. (1954). Motivation and personality. Harper & Brothers.",
             locator="work", locator_type="work",
             supports="book-length elaboration of the need hierarchy", verified=False),
    ],
    "MC-613": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="An Empirical Test of a New Theory of Human Needs",
             title_fa="آزمون تجربی نظریه‌ای تازه درباره نیازهای انسانی",
             authors="Alderfer, C. P.", year=1969,
             publisher="Organizational Behavior and Human Performance",
             doi="10.1016/0030-5073(69)90004-X",
             url="https://www.sciencedirect.com/science/article/pii/003050736990004X",
             language="en", isbn=None,
             citation="Alderfer, C. P. (1969). An empirical test of a new theory of human needs. Organizational Behavior and Human Performance, 4(2), 142-175. https://doi.org/10.1016/0030-5073(69)90004-X",
             locator="4(2):142-175", locator_type="page_range",
             supports="existence-relatedness-growth needs / satisfaction-progression and frustration-regression", verified=True),
        dict(kind="BOOK",
             title_en="Existence, Relatedness, and Growth: Human Needs in Organizational Settings",
             title_fa="هستی، پیوند و رشد: نیازهای انسانی در محیط سازمانی",
             authors="Alderfer, C. P.", year=1972, publisher="Free Press",
             doi=None, url=None, language="en", isbn=None,
             citation="Alderfer, C. P. (1972). Existence, relatedness, and growth: Human needs in organizational settings. Free Press.",
             locator="work", locator_type="work",
             supports="organizational elaboration of ERG theory", verified=False),
    ],
    "MC-614": [
        dict(kind="BOOK",
             title_en="The Motivation to Work",
             title_fa="انگیزش برای کار",
             authors="Herzberg, F.; Mausner, B.; Snyderman, B. B.", year=1959,
             publisher="Wiley",
             doi=None, url=None, language="en", isbn=None,
             citation="Herzberg, F., Mausner, B., & Snyderman, B. B. (1959). The motivation to work. Wiley.",
             locator="work", locator_type="work",
             supports="two-factor structure of job satisfaction and dissatisfaction / critical incident interviews", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="One More Time: How Do You Motivate Employees?",
             title_fa="یک بار دیگر: چگونه کارکنان را برانگیزیم؟",
             authors="Herzberg, F.", year=1968, publisher="Harvard Business Review",
             doi=None, url=None, language="en", isbn=None,
             citation="Herzberg, F. (1968). One more time: How do you motivate employees? Harvard Business Review, 46(1), 53-62.",
             locator="46(1):53-62", locator_type="page_range",
             supports="popularization of motivators vs hygiene factors / job enrichment", verified=False),
    ],
}

ENRICH = {
    "MC-596": {
        "summary": "(آلدریچ و هرکر، ۱۹۷۷) سازمان‌ها سیستم‌های بازی هستند که برای بقا به مبادله با محیط وابسته‌اند و مرز سازمان، نقطه همین تعامل است. نظریه مرزگذری می‌گوید کارکرد حیاتی مرزها را افرادی انجام می‌دهند که نقش مرزگذر دارند: پردازش اطلاعات محیط و نمایندگی سازمان در بیرون. آلدریچ و هرکر دو کارکرد اصلی را تفکیک کردند: جمع‌آوری و تفسیر اطلاعات، و تأثیرگذاری بر محیط از راه مذاکره، نمایش و تبادل. این نقش‌ها هم فرصت‌اند و هم منبع تعارض نقش، ابهام و فشار روانی.",
        "definition": "نظریه مرزگذری سازمانی، چارچوبی است که تعامل سازمان با محیط را از راه نقش‌هایی توضیح می‌دهد که در مرز سازمان قرار دارند و دو کارکرد پردازش اطلاعات و نمایندگی بیرونی را انجام می‌دهند.",
        "main_problem": "مسئله این است که سازمان چگونه محیط نامطمئن را می‌شناسد و بر آن اثر می‌گذارد. پاسخ در ساختار مرزی است، نه تنها در مدیریت ارشد. پرسش دوم، هزینه است: چرا صاحبان نقش‌های مرزی بیشتر دچار تعارض و فرسودگی می‌شوند و سازمان چگونه می‌تواند این هزینه را مهار کند.",
        "mechanism": "۱. مرز سازمانی: مرز، نقطه تماس سازمان با محیط و مکان مبادله منابع، اطلاعات و مشروعیت است، نه دیواری که سازمان را می‌بندد.\n۲. پردازش اطلاعات: مرزگذر محیط را پایش می‌کند، نشانه‌های ضعیف را می‌گیرد و اطلاعات بیرونی را به زبان سازمان ترجمه می‌کند.\n۳. تفسیر و فیلتر: اطلاعات پیش از رسیدن به تصمیم‌گیرنده گزینش و تفسیر می‌شود؛ همین مرحله، هم منبع قدرت مرزگذر است و هم منبع خطای سازمان.\n۴. نمایندگی بیرونی: مرزگذر سازمان را به بیرون نشان می‌دهد و از راه مذاکره، اقناع و تبادل بر انتظارات محیط اثر می‌گذارد.\n۵. تعارض و ابهام نقش: مرزگذر هم‌زمان به انتظارات سازمان و محیط پاسخ می‌دهد؛ این دوگانگی، تعارض نقش و ابهام می‌سازد.\n۶. سازوکارهای مدیریت: سازمان با گزینش افراد دارای تحمل ابهام، آموزش، پاداش مناسب و چرخش نقش، هزینه مرزگذری را کاهش می‌دهد.\n\nدر بستر رسانه، روابط عمومی، بازاریابی، فروش و روزنامه‌نگاری سازمانی نقش‌های مرزگذرند؛ آن‌ها هم اطلاعات محیط را به سازمان می‌آورند و هم تصویر سازمان را به بیرون می‌برند. این چارچوب توضیح می‌دهد چرا در بحران، واحد ارتباطات هم منبع هشدار زودهنگام است و هم آماج انتقاد؛ و چرا رسانه‌های اجتماعی مرز سازمان را نازک و نفوذپذیر کرده‌اند تا هر کارمند بتواند مرزگذر شود. نکته مهم این است که مرزگذری نباید به سانسور اطلاعات بدل شود؛ کارکرد آن تفسیر مسئولانه و انتقال بازخورد است.",
        "assumptions": [
            "سازمان، سیستم بازی است که به محیط وابسته است.",
            "تعامل با محیط را افرادی در نقش‌های مرزی انجام می‌دهند.",
            "نقش مرزی، تعارض و ابهام ساختاری می‌سازد.",
        ],
        "principles": [
            "مرز، مکان مبادله است نه دیوار.",
            "اطلاعات پیش از تصمیم، تفسیر و فیلتر می‌شود.",
            "نمایندگی بیرونی به اندازه پایش درون‌رو اثر دارد.",
        ],
        "critiques": [
            "۱. تمرکز بر ساختار: نظریه نقش را توصیف می‌کند اما سازوکار روانی مرزگذر را کم توضیح می‌دهد.\n۲. سنجش تعارض نقش: ابزارهای سنجش، تعارض را بیشتر از ابهام می‌گیرند.\n۳. زمینه سازمانی: شواهد اولیه از سازمان‌های صنعتی و دولتی می‌آید.\n۴. کم‌توجهی به قدرت: مرزگذر می‌تواند اطلاعات را راهبردی پنهان کند.\n۵. مرزهای شبکه‌ای: در سازمان‌های پلتفرمی مرز ثابت نیست و چارچوب نیازمند بازنگری است.",
        ],
        "applications": [
            "روابط عمومی: طراحی نقش پایش محیط و نمایندگی سازمان.",
            "مدیریت بحران: استفاده از مرزگذر به‌عنوان حسگر زودهنگام.",
            "مدیریت منابع انسانی: گزینش و آموزش افراد با تحمل ابهام بالا.",
            "پژوهش رسانه: تحلیل نقش خبرنگار و سخنگو به‌عنوان مرزگذر.",
        ],
        "evolution": "آلدریچ و هرکر در ۱۹۷۷ نقش‌های مرزی را در چارچوب نظریه وابستگی به منابع صورت‌بندی کردند. تاشمن و اسکنلن در ۱۹۸۱ فرد مرزگذر را به‌عنوان واسط انتقال اطلاعات در نوآوری مطالعه کردند و لیفر و دلبک در ۱۹۷۸ مدل تبادل سازمان با محیط را گستردند. بعدها این خط پژوهشی با مدیریت دانش، شبکه‌های سازمانی و ارتباطات راهبردی پیوند خورد.",
        "key_concepts": [
            "نقش مرزگذر (Boundary Spanning Role)",
            "پردازش اطلاعات مرزی (Boundary Information Processing)",
            "نمایندگی بیرونی (External Representation)",
            "تعارض نقش (Role Conflict)",
            "ابهام نقش (Role Ambiguity)",
            "نفوذپذیری مرز (Boundary Permeability)",
        ],
        "studies": [
            "Aldrich, H. E., & Herker, D. (1977). Boundary spanning roles and organization structure. Academy of Management Review, 2(2), 217-230.",
            "Tushman, M. L., & Scanlan, T. J. (1981). Boundary spanning individuals. Academy of Management Journal, 24(2), 289-305.",
        ],
        "theorists": "هاوارد آلدریچ؛ دیوید هرکر",
        "theorists_text": "آلدریچ و هرکر (۱۹۷۷)",
        "year": 1977,
        "model": "مدل مرزگذری: محیط نامطمئن → نقش مرزگذر (پایش و پردازش اطلاعات ↔ نمایندگی و نفوذ بیرونی) → سازگاری سازمان با محیط، با هزینه تعارض و ابهام نقش.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nنظریه از تصویر سازمان به‌عنوان سیستم باز آغاز می‌شود و مرز را مکان تبادل می‌داند. نوآوری چارچوب، انتقال کارکرد مرزی از سطح مدیریت ارشد به نقش‌های سازمانی روزمره است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با تحلیل نقش، مشاهده تعامل مرزی و پرسش‌نامه تعارض و ابهام انجام می‌شود. پژوهشی که تنها ساختار رسمی را می‌خواند، مرزگذری غیررسمی را از دست می‌دهد؛ و پژوهشی که تنها فشار روانی را می‌سنجد، کارکرد اطلاعاتی نقش را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در توضیح رابطه سازمان و رسانه است، اما باید با تحلیل قدرت تکمیل شود. مرزگذر بی پاسخ‌گویی می‌تواند به دروازه‌بان اطلاعات بدل شود؛ شفافیت، شرط مشروعیت نقش است.",
        "critique_text": "\n".join([
            "۱. تمرکز بر ساختار: سازوکار روانی مرزگذر کم توضیح می‌ماند.",
            "۲. سنجش تعارض نقش: ابزارها ابهام را کم می‌گیرند.",
            "۳. زمینه سازمانی: شواهد از سازمان‌های صنعتی و دولتی است.",
            "۴. کم‌توجهی به قدرت: اطلاعات می‌تواند راهبردی پنهان شود.",
            "۵. مرزهای شبکه‌ای: مرز ثابت نیست و چارچوب نیازمند بازنگری است.",
        ]),
        "example_text": "واحد روابط عمومی شرکتی پیش از انتشار خبر تغییر مدیرعامل، بازخورد رسانه‌ها و کارکنان را جمع می‌کند و روایت رسمی را تنظیم می‌کند؛ همان واحد هم هشدار نارضایتی را به مدیریت می‌برد. دو کارکرد مرزگذری در یک نقش دیده می‌شود.",
    },
    "MC-612": {
        "summary": "(مازلو، ۱۹۴۳) نظریه سلسله‌مراتب نیازها می‌گوید نیازهای انسان در پنج سطح سازمان می‌یابند: فیزیولوژیک، ایمنی، تعلق و عشق، احترام و خودشکوفایی. نیاز سطح پایین‌تر تا حدی ارضا شود، نیاز سطح بالاتر برجسته می‌شود؛ مازلو این را اصل برتری خواند. نظریه از مشاهده بالینی و نه آزمایش کنترل‌شده برخاست و مازلو خود آن را فرضیه‌ای قابل بازنگری دانست. سلسله‌مراتب، زبان مشترکی برای تحلیل انگیزش ساخت، هرچند سخت‌گیری تجربی آن محل نقد است.",
        "definition": "هرم نیازهای مازلو، مدلی از انگیزش است که نیازهای انسان را در پنج سطح سلسله‌مراتبی می‌چیند و بر این فرض استوار است که ارضای نیازهای پایین‌تر، نیازهای بالاتر را برجسته می‌کند.",
        "main_problem": "مسئله این است که چرا انسان‌ها در موقعیت‌های متفاوت به انگیزه‌های متفاوت پاسخ می‌دهند و چه چیزی اولویت نیاز را تعیین می‌کند. پاسخ مازلو، سطح ارضای نیازهای پایه است. پرسش دوم، اعتبار تجربی است: آیا ترتیب سلسله‌مراتب جهان‌شمول است یا به فرهنگ و موقعیت وابسته.",
        "mechanism": "۱. نیاز فیزیولوژیک: گرسنگی، تشنگی، خواب و تعادل بدن؛ در محرومیت شدید، سایر نیازها را به حاشیه می‌برند.\n۲. نیاز ایمنی: ثبات، نظم، امنیت جسمی و روانی، سلامت و آینده قابل پیش‌بینی.\n۳. تعلق و عشق: پیوند عاطفی، خانواده، دوستی و پذیرش گروهی.\n۴. احترام: عزت نفس، شایستگی، شناخته‌شدن و منزلت اجتماعی.\n۵. خودشکوفایی: شکوفا کردن توان بالقوه، خلاقیت و معنا.\n۶. اصل برتری: نیاز ارضاشده محرک را از دست می‌دهد و نیاز سطح بالاتر برجسته می‌شود؛ در محرومیت، فرد به سطح پایین‌تر بازمی‌گردد.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا پیام ترس و امنیت در بحران اثر می‌کند، چرا محتوای اجتماعی و پیوندی در پلتفرم‌ها جذب می‌شود و چرا تبلیغ منزلت و خلاقیت در بازارهای اشباع‌شده کار می‌کند. نظریه استفاده و رضامندی تا حدی از همین منطق بهره برده است. نکته مهم این است که هرم، ابزار بخش‌بندی مخاطب است و نباید به قالب خطی سفت و سخت تقلیل یابد.",
        "assumptions": [
            "نیازها سلسله‌مراتبی و قابل رتبه‌بندی‌اند.",
            "ارضای نیاز پایین‌تر، شرط برجسته‌شدن نیاز بالاتر است.",
            "نیاز ارضاشده، انگیزه‌دهنده نمی‌ماند.",
        ],
        "principles": [
            "محرومیت، اولویت نیاز را تعیین می‌کند.",
            "انگیزه، تابع مرحله است نه ویژگی ثابت.",
            "بالاترین سطح، معنا و شکوفایی است.",
        ],
        "critiques": [
            "۱. شواهد ضعیف: مازلو از مشاهده بالینی و نمونه گزینشی استفاده کرد.\n۲. آزمون‌های تجربی: مرور پژوهش‌ها در ۱۹۷۶ ترتیب سخت سلسله‌مراتب را نیافت.\n۳. سوگیری فرهنگی: وزن تعلق و احترام در جوامع فردگرا و جمع‌گرا یکسان نیست.\n۴. سنجش: مرز نیازها و ترتیب آن‌ها در عمل مبهم است.\n۵. کاربرد شرکتی: هرم به ابزار تبلیغاتی و آموزشی ساده‌شده بدل شده است.",
        ],
        "applications": [
            "تبلیغات: طراحی پیام بر پایه سطح نیاز مخاطب.",
            "ارتباطات بحران: اولویت پیام ایمنی در شرایط اضطراری.",
            "مدیریت منابع انسانی: طراحی انگیزش بر پایه مرحله کارکنان.",
            "پژوهش مخاطب: تحلیل رضامندی رسانه‌ای در سطح نیاز.",
        ],
        "evolution": "مازلو در ۱۹۴۳ نظریه انگیزش انسانی را در مجله روانشناسی منتشر کرد و در ۱۹۵۴ آن را در کتاب انگیزش و شخصیت گسترد. در دهه ۱۹۶۰ مفهوم خودشکوفایی را بسط داد و در ۱۹۶۹ نیاز خودفراروی را به‌عنوان سطحی فراتر از خودشکوفایی مطرح کرد. مدل او به نظریه استفاده و رضامندی و مطالعات انگیزش کارکنان راه یافت.",
        "key_concepts": [
            "نیاز فیزیولوژیک (Physiological Need)",
            "نیاز ایمنی (Safety Need)",
            "تعلق و عشق (Belongingness and Love)",
            "احترام (Esteem)",
            "خودشکوفایی (Self-Actualization)",
            "اصل برتری (Prepotency)",
        ],
        "studies": [
            "Maslow, A. H. (1943). A theory of human motivation. Psychological Review, 50(4), 370-396.",
            "Maslow, A. H. (1954). Motivation and personality. Harper & Brothers.",
        ],
        "theorists": "آبراهام مازلو",
        "theorists_text": "آبراهام مازلو (۱۹۴۳؛ ۱۹۵۴)",
        "year": 1943,
        "model": "هرم پنج‌سطحی: فیزیولوژیک ← ایمنی ← تعلق ← احترام ← خودشکوفایی؛ ارضای هر سطح، سطح بالاتر را برجسته می‌کند.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nمازلو انگیزش را از فهرست غرایز جدا کرد و آن را به سلسله‌مراتب نیازهای قابل رشد گره زد. نوآوری چارچوب، پیوند انگیزش با مرحله ارضا و سلامت روان است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با درجه‌بندی رضایت نیاز و تحلیل روایت فرد انجام می‌شود. پژوهشی که تنها یک سطح را می‌سنجد، ترتیب را از دست می‌دهد؛ و پژوهشی که هرم را آزمون قطعی می‌گیرد، آن را بیش از خود مازلو سخت‌گیرانه می‌خواند.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در بخش‌بندی پیام است، اما باید با تحلیل زمینه تکمیل شود. در بحران، پیام ایمنی مقدم است؛ در آرامش، پیام معنا و پیوند اثر بیشتری دارد.",
        "critique_text": "\n".join([
            "۱. شواهد ضعیف: مشاهده بالینی و نمونه گزینشی.",
            "۲. آزمون‌های تجربی: ترتیب سخت تأیید نشده است.",
            "۳. سوگیری فرهنگی: وزن نیازها یکسان نیست.",
            "۴. سنجش: مرز نیازها مبهم است.",
            "۵. کاربرد شرکتی: هرم به ابزار تبلیغاتی بدل شده است.",
        ]),
        "example_text": "در زلزله، پیام‌های امنیت و سرپناه بیشترین اثر را دارند؛ پس از تثبیت وضعیت، پیام‌های همبستگی و سپس مشارکت داوطلبانه جذب می‌شوند. ترتیب اثر پیام با سطح نیاز جابه‌جا شده است.",
    },
    "MC-613": {
        "summary": "(آلدرفر، ۱۹۶۹) نظریه ای‌آرجی، هرم مازلو را به سه نیاز کاهش می‌دهد: هستی (نیازهای مادی و فیزیولوژیک)، پیوند (روابط میان‌فردی) و رشد (شکوفایی توان). آلدرفر سلسله‌مراتب سخت را کنار گذاشت و گفت چند نیاز هم‌زمان فعال‌اند. نوآوری اصلی او فرضیه ناکامی–بازگشت است: وقتی نیاز سطح بالاتر ارضا نشود، فرد به نیاز سطح پایین‌تر بازمی‌گردد. نظریه از آزمون تجربی برخاست و برای تحلیل انگیزش در سازمان ساخته شد.",
        "definition": "نظریه ای‌آرجی، نظریه‌ای سه‌نیازی درباره انگیزش است که هستی، پیوند و رشد را از هم تفکیک می‌کند و در آن نیازها هم‌زمان فعال‌اند و ناکامی در سطح بالاتر به بازگشت به سطح پایین‌تر می‌انجامد.",
        "main_problem": "مسئله این است که هرم مازلو با شواهد سازمانی هم‌خوان نیست: کارکنان هم‌زمان به حقوق، رابطه و رشد اهمیت می‌دهند. پرسش آلدرفر این است که مدل نیاز را چگونه می‌توان ساده‌تر و آزمون‌پذیرتر کرد. پرسش دوم، رفتار در ناکامی است: وقتی مسیر رشد بسته می‌شود، انرژی انگیزشی به کجا می‌رود.",
        "mechanism": "۱. نیاز هستی: بقا و رفاه مادی؛ حقوق، امنیت شغلی، شرایط کار و سلامت.\n۲. نیاز پیوند: ارتباط، حمایت، پذیرش و همدلی در گروه کاری.\n۳. نیاز رشد: یادگیری، خلاقیت، پیشرفت و شکوفایی توان.\n۴. فعالیت هم‌زمان: سه نیاز در یک زمان می‌توانند فعال باشند و ترتیب سخت وجود ندارد.\n۵. ارضای نیاز: ارضای هر نیاز، شدت آن را کاهش می‌دهد و ارضای نیاز پیوند، نیاز رشد را برجسته می‌کند.\n۶. ناکامی–بازگشت: اگر نیاز رشد ارضا نشود، فرد به نیاز پیوند و سپس هستی بازمی‌گردد و آن را با شدت بیشتری طلب می‌کند.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا کارکنان رسانه در شرایط فشار، به‌جای خلاقیت، بر امنیت شغلی و روابط تیمی تمرکز می‌کنند؛ چرا برنامه‌های توسعه حرفه‌ای بی امنیت شغلی شکست می‌خورند؛ و چرا مخاطبان در ناامنی اقتصادی به محتوای سرگرم‌کننده و پیوندی روی می‌آورند. نکته مهم این است که ناکامی، نیاز را حذف نمی‌کند؛ مسیر آن را جابه‌جا می‌کند.",
        "assumptions": [
            "سه نیاز بنیادین، هستی، پیوند و رشدند.",
            "نیازها هم‌زمان فعال می‌شوند.",
            "ناکامی در سطح بالاتر، بازگشت به سطح پایین‌تر می‌سازد.",
        ],
        "principles": [
            "سلسله‌مراتب سخت وجود ندارد.",
            "ارضای نیاز، شدت آن را کم می‌کند.",
            "ناکامی، انگیزه را جابه‌جا می‌کند نه حذف.",
        ],
        "critiques": [
            "۱. سادگی بیش از حد: سه نیاز ممکن است تنوع انگیزه سازمانی را کم برآورد.\n۲. سنجش ناکامی–بازگشت: شواهد تجربی برای بازگشت یکدست نیست.\n۳. ابهام مرزها: تفکیک پیوند و رشد در عمل دشوار است.\n۴. زمینه: آزمون نخست در نمونه محدود کارکنان انجام شد.\n۵. کم‌توجهی به تفاوت فردی: شدت نیازها میان افراد و فرهنگ‌ها یکسان نیست.",
        ],
        "applications": [
            "طراحی شغل: توازن امنیت، روابط تیمی و مسیر رشد.",
            "مدیریت تغییر: پیش‌بینی افت انگیزه هنگام بسته‌شدن مسیر ارتقا.",
            "توسعه سازمانی: برنامه‌های آموزش همراه با امنیت شغلی.",
            "پژوهش مخاطب: تحلیل رضامندی رسانه‌ای در سه سطح نیاز.",
        ],
        "evolution": "آلدرفر در ۱۹۶۹ نظریه خود را در آزمون تجربی منتشر کرد و در ۱۹۷۲ در کتابی درباره نیازها در محیط سازمانی بسط داد. این نظریه واکنشی انتقادی به سلسله‌مراتب مازلو بود و بعدها با نظریه خودتعیین‌گری و طراحی شغل پیوند خورد.",
        "key_concepts": [
            "نیاز هستی (Existence Needs)",
            "نیاز پیوند (Relatedness Needs)",
            "نیاز رشد (Growth Needs)",
            "ارضای–پیشرفت (Satisfaction-Progression)",
            "ناکامی–بازگشت (Frustration-Regression)",
            "فعالیت هم‌زمان نیازها (Simultaneous Needs)",
        ],
        "studies": [
            "Alderfer, C. P. (1969). An empirical test of a new theory of human needs. Organizational Behavior and Human Performance, 4(2), 142-175.",
            "Alderfer, C. P. (1972). Existence, relatedness, and growth. Free Press.",
        ],
        "theorists": "کلیتون آلدرفر",
        "theorists_text": "کلیتون آلدرفر (۱۹۶۹؛ ۱۹۷۲)",
        "year": 1969,
        "model": "سه نیاز: هستی ← پیوند ← رشد؛ فعالیت هم‌زمان؛ ارضا باعث کاهش شدت و ناکامی باعث بازگشت به سطح پایین‌تر می‌شود.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nآلدرفر هرم را به سه دسته آزمون‌پذیر فروکاست و منطق ناکامی را به آن افزود. نوآوری چارچوب، جایگزینی صعود خطی با حرکت دوطرفه میان سطوح نیاز است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با پرسش‌نامه شدت و رضایت سه نیاز و تحلیل همبستگی آن‌ها انجام می‌شود. پژوهشی که تنها ارضا را می‌سنجد، بازگشت ناشی از ناکامی را از دست می‌دهد؛ و پژوهشی که سه نیاز را مستقل می‌گیرد، هم‌زمانی آن‌ها را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در توضیح افت انگیزه سازمانی است، اما باید با تحلیل اقتصادی تکمیل شود. ناکامی رشد در محیط ناامن، به محافظه‌کاری و تمرکز بر بقا می‌انجامد.",
        "critique_text": "\n".join([
            "۱. سادگی بیش از حد: تنوع انگیزه کم برآورد می‌شود.",
            "۲. سنجش ناکامی–بازگشت: شواهد یکدست نیست.",
            "۳. ابهام مرزها: تفکیک پیوند و رشد دشوار است.",
            "۴. زمینه: آزمون نخست در نمونه محدود انجام شد.",
            "۵. تفاوت فردی: شدت نیازها یکسان نیست.",
        ]),
        "example_text": "در تحریریه‌ای که مسیر ارتقا بسته شده، خبرنگاران به‌جای پیگیری پروژه‌های خلاق، بر تثبیت جایگاه تیمی و مذاکره بر حقوق تمرکز می‌کنند؛ ناکامی در رشد، انگیزه را به پیوند و هستی بازگردانده است.",
    },
    "MC-614": {
        "summary": "(هرزبرگ، ماوسنر و اسنایدرمن، ۱۹۵۹) نظریه دو عاملی می‌گوید رضایت شغلی و نارضایتی شغلی دو قطب یک پیوستار نیستند، بلکه دو پیوستار جدا با عوامل متفاوت‌اند. عوامل انگیزشی (پیشرفت، شناخت، خود کار، مسئولیت و رشد) رضایت می‌سازند؛ عوامل بهداشتی (سیاست سازمان، سرپرستی، حقوق، روابط و شرایط کار) فقط نارضایتی را کم می‌کنند. هرزبرگ این نتیجه را از مصاحبه رویداد بحرانی با ۲۰۳ حسابدار و مهندس گرفت. مدل، پایه جنبش غنی‌سازی شغل شد، اما روش آن محل نقد است.",
        "definition": "نظریه دو عاملی، مدلی از انگیزش شغلی است که رضایت و نارضایتی را دو سازه مستقل می‌داند و برای هر یک مجموعه عوامل جداگانه، انگیزشی و بهداشتی، تعریف می‌کند.",
        "main_problem": "مسئله این است که چرا افزایش حقوق و بهبود شرایط، نارضایتی را کم می‌کند اما کارکنان را برانگیخته نمی‌سازد. پاسخ هرزبرگ تفکیک دو سازه است. پرسش دوم، روش است: آیا نتایج از منطق مصاحبه و نمونه محدود برمی‌آید یا واقعیتی سازمانی را نشان می‌دهد.",
        "mechanism": "۱. رویداد بحرانی: کارکنان رویدادهایی را می‌گویند که در آن احساس بسیار خوب یا بسیار بد داشته‌اند و جهت نسبت‌دهی آن‌ها ثبت می‌شود.\n۲. عوامل انگیزشی: پیشرفت، شناخت، خود کار، مسئولیت، ارتقا و رشد؛ این عوامل در رویدادهای رضایت‌بخش غالب‌اند.\n۳. عوامل بهداشتی: سیاست و مدیریت، سرپرستی، حقوق، روابط میان‌فردی و شرایط کار؛ در رویدادهای ناخوشایند غالب‌اند.\n۴. دو پیوستار جدا: افزایش عوامل بهداشتی نارضایتی را کاهش می‌دهد اما رضایت و انگیزش نمی‌سازد.\n۵. طراحی شغل: غنی‌سازی شغل با افزودن تنوع، هویت و بازخورد وظیفه، عوامل انگیزشی را در خود کار می‌آورد.\n۶. مرز اثر: عوامل بیرونی پیش‌شرط‌اند و عوامل درونی محرک؛ بی بهداشت انگیزش نمی‌گیرد و بی انگیزش بهداشت به رضایت نمی‌رسد.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا تحریریه‌ای با حقوق بهتر اما بی خودمختاری همچنان بی‌انگیزه است؛ چرا خبرنگاران بر شناخت و اهمیت کار خود بیش از پاداش تکیه می‌کنند؛ و چرا سازمان‌های رسانه‌ای برای نگهداشت خلاقیت باید بر طراحی نقش و مسئولیت تمرکز کنند. نکته مهم این است که پول نارضایتی را کم می‌کند و انگیزش خلاق نمی‌سازد.",
        "assumptions": [
            "رضایت و نارضایتی دو سازه مستقل‌اند.",
            "عوامل درونی انگیزش می‌سازند و عوامل بیرونی نارضایتی را کم می‌کنند.",
            "نسبت‌دهی کارکنان در روایت رویداد قابل اعتماد است.",
        ],
        "principles": [
            "نبود نارضایتی، رضایت نیست.",
            "کار خود، منبع اصلی انگیزش است.",
            "بهبود بیرونی، تنها پیش‌شرط است.",
        ],
        "critiques": [
            "۱. سوگیری روش: نسبت‌دهی موفقیت به خود و شکست به محیط، نتایج را متورم می‌کند.\n۲. نمونه: نمونه نخست، حسابداران و مهندسان بود.\n۳. آستانه دو عاملی: مرز عوامل انگیزشی و بهداشتی در عمل مبهم است.\n۴. تکرارپذیری: پژوهش‌های بعدی نتایج را یکدست تأیید نکردند.\n۵. کم‌توجهی به اقتصاد کار: نقش دستمزد در گروه‌های کم‌درآمد کم‌برآورد می‌شود.",
        ],
        "applications": [
            "طراحی شغل: غنی‌سازی شغل و افزایش خودمختاری.",
            "نگهداشت استعداد: تمرکز بر شناخت و مسیر رشد.",
            "ارتباطات سازمانی: تفکیک پیام رفع نارضایتی از پیام انگیزش.",
            "تحلیل تحریریه: تشخیص انگیزه خبرنگاران و طراحی نقش.",
        ],
        "evolution": "هرزبرگ و همکارانش در ۱۹۵۹ نظریه را در کتاب انگیزش برای کار منتشر کردند و در ۱۹۶۸ در مقاله‌ای در نشریه کسب‌وکار هاروارد آن را عمومی کردند. مدل، پایه غنی‌سازی شغل و نظریه ویژگی‌های شغل شد و نقدهای روش‌شناختی آن را به بحثی کلاسیک در انگیزش تبدیل کرد.",
        "key_concepts": [
            "عوامل انگیزشی (Motivators)",
            "عوامل بهداشتی (Hygiene Factors)",
            "غنی‌سازی شغل (Job Enrichment)",
            "رضایت شغلی (Job Satisfaction)",
            "نارضایتی شغلی (Job Dissatisfaction)",
            "روش رویداد بحرانی (Critical Incident Technique)",
        ],
        "studies": [
            "Herzberg, F., Mausner, B., & Snyderman, B. B. (1959). The motivation to work. Wiley.",
            "Herzberg, F. (1968). One more time: How do you motivate employees? Harvard Business Review, 46(1), 53-62.",
        ],
        "theorists": "فردریک هرزبرگ؛ برنارد ماوسنر؛ باربارا اسنایدرمن",
        "theorists_text": "هرزبرگ، ماوسنر و اسنایدرمن (۱۹۵۹)",
        "year": 1959,
        "model": "دو پیوستار: عوامل انگیزشی ↔ رضایت؛ عوامل بهداشتی ↔ نبود نارضایتی؛ غنی‌سازی شغل، محرک اصلی انگیزش درونی.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nهرزبرگ رضایت را از نارضایتی جدا کرد و انگیزش را به محتوای کار گره زد. نوآوری چارچوب، رد فرض پیوستار واحد و تفکیک عوامل درونی از بیرونی است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با مصاحبه رویداد بحرانی و کدگذاری جهت روایت انجام می‌شود. پژوهشی که تنها نارضایتی را می‌سنجد، عوامل انگیزشی را از دست می‌دهد؛ و پژوهشی که نسبت‌دهی را بی راستی‌آزمایی می‌پذیرد، سوگیری روش را وارد نتیجه می‌کند.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در طراحی شغل خلاق است، اما باید با تحلیل بازار کار تکمیل شود. در مشاغل کم‌دستمزد، عوامل بهداشتی وزن بیشتری می‌گیرند و تفکیک دو عاملی کم‌رنگ می‌شود.",
        "critique_text": "\n".join([
            "۱. سوگیری روش: نسبت‌دهی جهت‌دار نتایج را متورم می‌کند.",
            "۲. نمونه: حسابداران و مهندسان.",
            "۳. آستانه دو عاملی: مرز عوامل مبهم است.",
            "۴. تکرارپذیری: نتایج یکدست تأیید نشده است.",
            "۵. اقتصاد کار: نقش دستمزد کم‌برآورد می‌شود.",
        ]),
        "example_text": "تحریریه‌ای حقوق‌ها را افزایش می‌دهد اما شکایت‌ها ادامه دارد؛ بررسی نشان می‌دهد خبرنگاران از نبود خودمختاری در انتخاب موضوع ناراضی‌اند. عوامل بهداشتی بهبود یافته، اما عوامل انگیزشی دست‌نخورده مانده است.",
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
    "MC-596": ("نظریه مرزگذری سازمانی", "Boundary Spanning Theory",
               "canonical_name_fa repaired: ungrammatical 'نظریه مرزگذاری سازمان'; canonical_name_en repaired: 'Organizational Boundary Theory' aligned to boundary spanning theory"),
    "MC-613": ("نظریه ای‌آرجی (هستی، پیوند، رشد)", "ERG Theory",
               "canonical_name_fa repaired: Latin acronym 'ERG' Persianized to 'ای‌آرجی' and needs named"),
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
                                       "verified": n_verified, "batch": 99}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH99 THEORY DONE")


if __name__ == "__main__":
    main()
