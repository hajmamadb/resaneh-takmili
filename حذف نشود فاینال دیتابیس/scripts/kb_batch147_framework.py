# -*- coding: utf-8 -*-
"""Batch 147 (MODEL): MC-541 Riley & Riley, MC-542 Jakobson, MC-543 Maletzke, MC-544 Bühler."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch147-model-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch147_model.json"

S = {
    "MC-541": [
        dict(kind="BOOK_CHAPTER",
             title_en="Mass Communication and the Social System",
             title_fa="ارتباط جمعی و نظام اجتماعی",
             authors="Riley, J. W.; Riley, M. W.", year=1959,
             publisher="Basic Books (Sociology Today)",
             doi=None,
             url="https://www.bibsonomy.org/bibtex/511caba312593920ee0c3540ca8fcf61",
             language="en", isbn=None,
             citation="Riley, J. W., & Riley, M. W. (1959). Mass communication and the social system. In R. K. Merton, L. Broom, & L. S. Cottrell (Eds.), Sociology Today. New York: Basic Books.",
             locator="chapter", locator_type="SECTION",
             supports="sociological model of mass communication embedded in social structure", verified=True),
        dict(kind="WEBSITE",
             title_en="Riley & Riley Model of Communication",
             title_fa="مدل ارتباطی رایلی و رایلی",
             authors="Communication Theory", year=None,
             publisher="communicationtheory.org",
             doi=None,
             url="https://communicationtheory.org/riley-riley-model-of-communication/",
             language="en", isbn=None,
             citation="Communication Theory. (n.d.). Riley & Riley model of communication. Retrieved from communicationtheory.org.",
             locator="web page", locator_type="work",
             supports="pedagogical exposition of the sociological model and its feedback loop", verified=True),
    ],
    "MC-542": [
        dict(kind="BOOK_CHAPTER",
             title_en="Closing Statement: Linguistics and Poetics",
             title_fa="سخن پایانی: زبان‌شناسی و شعرشناسی",
             authors="Jakobson, R.", year=1960,
             publisher="MIT Press (Style in Language)",
             doi=None,
             url="https://monoskop.org/images/archive/8/84/20141028191454%21Jakobson_Roman_1960_Closing_statement_Linguistics_and_Poetics.pdf",
             language="en", isbn=None,
             citation="Jakobson, R. (1960). Closing statement: Linguistics and poetics. In T. A. Sebeok (Ed.), Style in Language (pp. 350-377). Cambridge, MA: MIT Press.",
             locator="pp. 350-377", locator_type="page_range",
             supports="six factors and six functions of verbal communication", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="What Is the Proper Function of Language?",
             title_fa="کارکرد مناسب زبان چیست؟",
             authors="Michaelson, E.", year=2024,
             publisher="Inquiry",
             doi="10.1080/0020174X.2024.2325616",
             url="https://www.tandfonline.com/doi/full/10.1080/0020174X.2024.2325616",
             language="en", isbn=None,
             citation="Michaelson, E. (2024). What is the proper function of language? Inquiry. https://doi.org/10.1080/0020174X.2024.2325616",
             locator="online first", locator_type="work",
             supports="contemporary philosophical discussion of Jakobson's six functions", verified=True),
    ],
    "MC-543": [
        dict(kind="BOOK",
             title_en="Psychologie der Massenkommunikation: Theorie und Systematik",
             title_fa="روان‌شناسی ارتباط جمعی: نظریه و نظام‌مندی",
             authors="Maletzke, G.", year=1963,
             publisher="Verlag Hans-Bredow-Institut",
             doi=None,
             url="https://www.fachportal-paedagogik.de/literatur/vollanzeige.html?FId=bbf_1307972",
             language="de", isbn=None,
             citation="Maletzke, G. (1963). Psychologie der Massenkommunikation: Theorie und Systematik. Hamburg: Verlag Hans-Bredow-Institut.",
             locator="book", locator_type="SECTION",
             supports="psychological model of mass communication with communicator and receiver fields", verified=True),
        dict(kind="WEBSITE",
             title_en="Maletzke's Model",
             title_fa="مدل مالتزکه",
             authors="Comunicologos", year=None,
             publisher="comunicologos.com",
             doi=None,
             url="https://www.comunicologos.com/english/theories/maletzke-s-model/",
             language="en", isbn=None,
             citation="Comunicologos. (n.d.). Maletzke's model. Retrieved from comunicologos.com.",
             locator="web page", locator_type="work",
             supports="exposition of the model's progressive construction and field constraints", verified=True),
    ],
    "MC-544": [
        dict(kind="BOOK",
             title_en="Sprachtheorie: Die Darstellungsfunktion der Sprache",
             title_fa="نظریهٔ زبان: کارکرد بازنمایی زبان",
             authors="Bühler, K.", year=1934,
             publisher="Gustav Fischer",
             doi=None,
             url="https://pure.mpg.de/view/item_2305592_5",
             language="de", isbn=None,
             citation="Bühler, K. (1934). Sprachtheorie: Die Darstellungsfunktion der Sprache. Jena: Gustav Fischer.",
             locator="book", locator_type="SECTION",
             supports="organon model with expression, appeal and representation functions", verified=True),
        dict(kind="BOOK",
             title_en="Theory of Language: The Representational Function of Language",
             title_fa="نظریهٔ زبان: کارکرد بازنمایی زبان",
             authors="Bühler, K.", year=2011,
             publisher="John Benjamins",
             doi="10.1075/z.164",
             url="https://benjamins.com/catalog/z.164",
             language="en", isbn="9789027286864",
             citation="Bühler, K. (2011). Theory of Language: The Representational Function of Language (D. F. Goodwin, Trans.). Amsterdam: John Benjamins. (Original work published 1934)",
             locator="book", locator_type="SECTION",
             supports="English translation of the organon model for international scholarship", verified=True),
    ],
}

ENRICH = {
    "MC-541": dict(
        year=1959,
        summary="مدل رایلی و رایلی، که جان و ماتیلدا رایلی در فصل سال ۱۹۵۹ با عنوان ارتباط جمعی و نظام اجتماعی معرفی کردند، ارتباط را زنجیره‌ای خطی از فرستنده به گیرنده نمی‌بیند، بلکه فرایندی می‌داند که درون یک نظام اجتماعی جای گرفته است. در این نگرش، فرستنده خود عضوی از گروه‌های اولیه و سازمان‌های ثانویه است و پیام او پیش از رسیدن به مخاطب از کانال‌های نهادی می‌گذرد. گیرنده نیز در شبکه‌ای از گروه‌های اولیه، خانواده، همکاران و اجتماع محلی جای دارد و معنای پیام را در همان بستر تفسیر می‌کند. رایلی و رایلی تأکید کردند که پژوهش ارتباط جمعی باید هم‌زمان به موقعیت فرستنده و موقعیت گیرنده در ساخت اجتماعی توجه کند، زیرا هر دو طرف با انتظارات گروهی، هنجارها و فشارهای نهادی روبه‌رو هستند. مدل آن‌ها بازخورد را نیز در چرخهٔ ارتباط جای داد و نشان داد که واکنش مخاطب به نوبهٔ خود بر تولید پیام بعدی اثر می‌گذارد. این مدل مقدمهٔ نظریه‌های دریافت و مطالعات مخاطب شد. نقدهای اصلی به آن، باقی‌ماندن در سطح توصیفی، کم‌توجهی به سنجش تجربی روابط میان سطوح اجتماعی، فرض هماهنگی نسبی نظام اجتماعی و روشن نکردن سازوکار قدرت را برجسته می‌کنند.",
        definition="مدل رایلی و رایلی، ارتباط جمعی را فرایندی درون نظام اجتماعی می‌داند که فرستنده، پیام و گیرنده هر سه در شبکهٔ گروه‌ها و نهادها جای دارند و معنا در همین بستر ساخته و بازتفسیر می‌شود.",
        main_problem="چگونه جایگاه فرستنده و گیرنده در ساخت اجتماعی، تولید و تفسیر پیام ارتباط جمعی را شکل می‌دهد و پژوهش ارتباط چگونه باید این بستر را در تحلیل بگنجاند.",
        mechanism="فرستنده در گروه‌ها و نهادها عمل می‌کند و پیام را با انتظارات گروهی می‌سازد؛ گیرنده نیز در شبکهٔ گروه‌های اولیه پیام را تفسیر می‌کند و واکنش او از راه بازخورد به تولید بعدی بازمی‌گردد.",
        assumptions=[
            "ارتباط جمعی درون نظام اجتماعی رخ می‌دهد.",
            "فرستنده عضوی از گروه‌ها و نهادهاست.",
            "گیرنده در شبکهٔ گروه‌های اولیه جای دارد.",
            "معنا در بستر اجتماعی تفسیر می‌شود.",
            "بازخورد چرخهٔ تولید را می‌بندد.",
        ],
        principles=[
            "موقعیت فرستنده را در ساخت اجتماعی مشخص کن.",
            "شبکهٔ گروهی گیرنده را در تحلیل بگنجان.",
            "مسیر نهادی پیام را تا مخاطب دنبال کن.",
            "بازخورد مخاطب را به تولید پیوند بده.",
            "معنا را در بستر اجتماعی تفسیر کن.",
            "سطوح خرد و کلان را هم‌زمان بسنج.",
        ],
        critiques=[
            "در سطح توصیفی می‌ماند.",
            "سنجش تجربی روابط میان سطوح را کم‌می‌شمارد.",
            "هماهنگی نسبی نظام اجتماعی را فرض می‌گیرد.",
            "سازوکار قدرت را روشن نمی‌کند.",
            "نقش رسانه در بازتولید نابرابری را کم‌بررسی می‌گذارد.",
            "روابط میان سطوح نظام را آزمون‌پذیر نمی‌سازد.",
        ],
        critique_text="منتقدان می‌گویند مدل رایلی و رایلی افق جامعه‌شناختی پژوهش ارتباط را گشود اما بیشتر توصیفی ماند و نابرابری قدرت و نقش رسانه در بازتولید آن را کم‌بررسی گذاشت؛ با این حال، چارچوب پایهٔ مطالعات مخاطب و دریافت است.",
        applications=[
            "تحلیل مخاطب در بستر گروه‌های اجتماعی.",
            "پژوهش دریافت پیام خبری.",
            "برنامه‌ریزی ارتباطات توسعه.",
            "مطالعهٔ بازخورد در رسانه.",
            "آموزش روش پژوهش ارتباط.",
        ],
        example_text="خبری که یک سازمان رسانه‌ای دربارهٔ برنامهٔ محلی منتشر می‌کند، پیش از انتشار از فیلتر سیاست‌های نهادی می‌گذرد و پس از انتشار در خانواده و محلهٔ مخاطب بازتفسیر می‌شود؛ اگر مخاطبان به آن واکنش منفی بدهند، همان واکنش به بازخورد تبدیل می‌شود و تولید بعدی را تغییر می‌دهد.",
        evolution="مدل در فصل سال ۱۹۵۹ رایلی و رایلی صورت‌بندی شد و با گسترش مطالعات مخاطب و نظریه‌های دریافت، به یکی از مراجع کلاسیک جامعه‌شناسی ارتباط تبدیل شد. پژوهش‌های بعدی، نقش قدرت و نابرابری را به چارچوب افزودند.",
        key_concepts=["نظام اجتماعی", "گروه اولیه", "بازخورد", "بستر تفسیر", "ساخت اجتماعی", "مخاطب"],
        theorists="جان رایلی و ماتیلدا رایلی.",
        theorists_text="مدل در سنت جامعه‌شناسی ارتباط جمعی و پژوهش مخاطب شکل گرفت.",
        model="ارتباط جمعی درون نظام اجتماعی؛ فرستنده و گیرنده هر دو در گروه‌های اولیه و نهادها جای دارند و پیام میان این دو قطب جریان می‌یابد.",
        studies=[
            "فصل سال ۱۹۵۹ چارچوب جامعه‌شناختی ارتباط را معرفی کرد.",
            "پژوهش مخاطب، نقش گروه اولیه را مستند کرد.",
            "مطالعات دریافت، تفسیر بستر‌محور را گسترد.",
            "پژوهش بازخورد، چرخهٔ تولید را تحلیل کرد.",
            "پژوهش خانواده، نقش گروه اولیه در تفسیر خبر را سنجید.",
        ],
    ),
    "MC-542": dict(
        year=1960,
        summary="مدل جاکوبسون، که رومن جاکوبسون در سخن پایانی سال ۱۹۶۰ با عنوان زبان‌شناسی و شعرشناسی در کتاب سبک در زبان ارائه کرد، ارتباط کلامی را بر پایهٔ شش عامل می‌سازد: زمینه، فرستنده، گیرنده، تماس، رمزگان و پیام. هر عامل با یک کارکرد زبان پیوند دارد. کارکرد ارجاعی بر زمینه و اطلاعات تمرکز دارد؛ کارکرد عاطفی بر فرستنده و بیان حال او؛ کارکرد ترغیبی بر گیرنده و برانگیختن او؛ کارکرد تماسی بر تماس و نگه‌داشتن کانال؛ کارکرد فرازبانی بر رمزگان و توضیح معنا؛ و کارکرد شعری بر خود پیام و شکل آن. جاکوبسون تأکید کرد که هر پیام معمولاً چند کارکرد را هم‌زمان دارد و آنچه وجه غالب پیام را می‌سازد، حضور پررنگ‌تر یک کارکرد است. او شعرشناسی را بخشی از زبان‌شناسی دانست و نشان داد که بررسی شکل پیام، نه حاشیه‌ای بر معنا، بلکه بخشی از تحلیل زبان است. این مدل به چارچوبی بنیادین در نشانه‌شناسی، تحلیل گفتمان، مطالعات ترجمه و نقد ادبی تبدیل شد. نقدهای اصلی به آن، تمرکز بر زبان کلامی، فرض هم‌ارزی کارکردها، کم‌توجهی به بستر نهادی و تاریخی و دشواری کاربرد تجربی در پیام‌های چندرسانه‌ای را برجسته می‌کنند.",
        definition="مدل جاکوبسون، شش عامل ارتباط کلامی را به شش کارکرد زبان پیوند می‌دهد و نشان می‌دهد که وجه غالب هر پیام را می‌توان از روی کارکرد برجستهٔ آن تشخیص داد.",
        main_problem="زبان چگونه هم‌زمان اطلاعات، احساس، ترغیب، تماس، فرازبان و شکل زیبایی‌شناختی را حمل می‌کند و کدام کارکرد وجه غالب یک پیام را می‌سازد.",
        mechanism="هر عامل ارتباطی یک کارکرد زبان را برجسته می‌کند؛ هم‌نشینی شش عامل در پیام، شش کارکرد را فعال می‌کند و کارکردی که برجسته‌تر باشد، جهت‌گیری اصلی پیام را تعیین می‌کند.",
        assumptions=[
            "ارتباط کلامی شش عامل دارد.",
            "هر عامل با یک کارکرد زبان پیوند دارد.",
            "پیام هم‌زمان چند کارکرد را حمل می‌کند.",
            "کارکرد غالب، وجه پیام را تعیین می‌کند.",
            "شعرشناسی بخشی از زبان‌شناسی است.",
        ],
        principles=[
            "عامل برجستهٔ پیام را مشخص کن.",
            "کارکرد غالب را از شکل پیام بخوان.",
            "شش کارکرد را جداگانه بررسی کن.",
            "فرم پیام را بخشی از معنا بدان.",
            "زمینه و رمزگان را در تحلیل بگنجان.",
            "کارکرد شعری را از تزئین جدا کن.",
            "کارکرد غالب را با شواهد متنی مستند کن.",
            "رمزگان مشترک دو طرف را بررسی کن.",
            "تماس را شرط برقراری ارتباط بدان.",
        ],
        critiques=[
            "بر زبان کلامی متمرکز است.",
            "هم‌ارزی کارکردها را فرض می‌گیرد.",
            "بستر نهادی و تاریخی را کم‌می‌شمارد.",
            "کاربرد تجربی آن در چندرسانه‌ای دشوار است.",
            "مرز کارکردها در عمل مبهم می‌شود.",
            "کارکردهای پیام تصویری را کم‌پوشش می‌گذارد.",
        ],
        critique_text="منتقدان می‌گویند مدل جاکوبسون ابزار دقیقی برای تحلیل شکل پیام فراهم کرد اما بر زبان کلامی متمرکز ماند و بستر قدرت و تاریخ را کم‌بررسی گذاشت؛ با این حال، همچنان چارچوب پایهٔ نشانه‌شناسی ارتباط است.",
        applications=[
            "تحلیل متن تبلیغی و خبری.",
            "نقد ادبی و شعرشناسی.",
            "مطالعات ترجمه و سبک.",
            "آموزش نشانه‌شناسی.",
            "تحلیل پیام در ارتباطات سیاسی.",
            "آموزش تحلیل کارکرد پیام به دانشجویان رسانه.",
        ],
        example_text="شعار تبلیغاتی که بر آهنگ و تکرار واژه‌ها تکیه می‌کند، کارکرد شعری را برجسته می‌سازد؛ همان شعار اگر با جمله‌ای خبری همراه شود، کارکرد ارجاعی را فعال می‌کند و اگر مخاطب را به عمل فرا خواند، کارکرد ترغیبی غالب می‌شود.",
        evolution="سخن پایانی سال ۱۹۶۰ جاکوبسون مدل شش‌کارکردی را تثبیت کرد و از آن پس به چارچوب مرجع نشانه‌شناسی، سبک‌شناسی و تحلیل گفتمان تبدیل شد. پژوهش‌های بعدی، آن را به رسانه‌های تصویری و چندرسانه‌ای گستردند.",
        key_concepts=["کارکرد ارجاعی", "کارکرد عاطفی", "کارکرد ترغیبی", "کارکرد تماسی", "کارکرد فرازبانی", "کارکرد شعری"],
        theorists="رومن جاکوبسون.",
        theorists_text="مدل در سنت زبان‌شناسی ساختگرا و نشانه‌شناسی شکل گرفت.",
        model="شش عامل (زمینه، فرستنده، گیرنده، تماس، رمزگان، پیام) و شش کارکرد زبان که کارکرد غالب، وجه پیام را تعیین می‌کند.",
        studies=[
            "سخن پایانی سال ۱۹۶۰ مدل را تثبیت کرد.",
            "پژوهش نشانه‌شناسی، مدل را گسترد.",
            "مطالعات ترجمه، کارکردها را به کار گرفت.",
            "تحلیل تبلیغ، کارکرد غالب را سنجید.",
            "پژوهش گفتمان، کارکردهای شش‌گانه را در متن خبری یافت.",
        ],
    ),
    "MC-543": dict(
        year=1963,
        summary="مدل مالتزکه، که گرهارد مالتزکه در کتاب سال ۱۹۶۳ با عنوان روان‌شناسی ارتباط جمعی: نظریه و نظام‌مندی ارائه کرد، ارتباط جمعی را فرایندی روان‌شناختی و اجتماعی می‌داند که در آن فرستنده و گیرنده هر دو با میدان تجربه و ادراک خود پیام را می‌سازند و بازمی‌سازند. مالتزکه مدل را به‌تدریج از یک طرح ساده به طرحی چندلایه گسترد. در سمت فرستنده، خودانگاره، شخصیت، محیط اجتماعی، فشارهای سازمان برنامه و تصویری که از مخاطب دارد، بر ساخت پیام اثر می‌گذارد. پیام خود ساختاری چندلایه دارد و موضوع ارتباط را در قالبی نمادین سازمان می‌دهد. در سمت گیرنده نیز خودانگاره، شخصیت، محیط اجتماعی، تصویر او از فرستنده و میزان رضایت از محتوا بر گزینش و تفسیر اثر می‌گذارد. مالتزکه سه ویژگی ارتباط جمعی را نیز برجسته کرد: علنی بودن، پراکندگی و ناهمگونی مخاطب، و هم‌زمانی تولید و دریافت. او فرایند دریافت را بازسازی روان‌شناختی پیام می‌دانست؛ یعنی گیرنده معنای پیام را از نو می‌سازد، نه اینکه آن را بی‌تغییر دریافت کند. نقدهای اصلی به مدل، پیچیدگی و دشواری آزمون، تمرکز بر روان‌شناسی فردی، کم‌توجهی به ساخت قدرت و اقتصاد رسانه و ابهام برخی سازه‌ها را برجسته می‌کنند.",
        definition="مدل مالتزکه، ارتباط جمعی را برهم‌کنش میدان‌های ادراکی فرستنده و گیرنده می‌داند که در آن پیام نه منتقل، بلکه به‌طور روان‌شناختی بازسازی می‌شود و فشارهای سازمانی و اجتماعی هر دو سمت را شکل می‌دهند.",
        main_problem="چگونه ویژگی‌های روان‌شناختی و اجتماعی فرستنده و گیرنده، همراه با فشارهای سازمان رسانه، ساخت و دریافت پیام ارتباط جمعی را تعیین می‌کند.",
        mechanism="فرستنده زیر تأثیر خودانگاره، شخصیت، محیط و فشار سازمان پیام را می‌سازد؛ گیرنده با خودانگاره، شخصیت، محیط و تصویر فرستنده پیام را گزینش و بازسازی می‌کند و سه ویژگی علنی بودن، پراکندگی و هم‌زمانی این فرایند را قید می‌زند.",
        assumptions=[
            "فرستنده و گیرنده هر دو ادراک فعال دارند.",
            "پیام در دریافت بازسازی می‌شود.",
            "فشار سازمانی بر تولید اثر دارد.",
            "محیط اجتماعی دو طرف را شکل می‌دهد.",
            "ارتباط جمعی علنی، پراکنده و هم‌زمان است.",
        ],
        principles=[
            "خودانگارهٔ فرستنده را در تحلیل بگنجان.",
            "تصویر فرستنده از مخاطب را بررسی کن.",
            "فشار سازمانی بر تولید را بسنج.",
            "بازسازی روان‌شناختی پیام را جدی بگیر.",
            "محیط اجتماعی گیرنده را مشخص کن.",
            "سه ویژگی ارتباط جمعی را در مدل نگه دار.",
        ],
        critiques=[
            "پیچیدگی مدل آزمون را دشوار می‌کند.",
            "بر روان‌شناسی فردی متمرکز است.",
            "ساخت قدرت و اقتصاد رسانه را کم‌بررسی می‌گذارد.",
            "برخی سازه‌ها مبهم‌اند.",
            "بستر تاریخی دریافت را نادیده می‌گیرد.",
            "مرز میدان ادراک فرستنده و گیرنده را روشن نمی‌کند.",
        ],
        critique_text="منتقدان می‌گویند مدل مالتزکه غنای روان‌شناختی تحلیل ارتباط جمعی را بالا برد اما با انبوه سازه‌ها آزمون‌پذیری را کاهش داد و ساخت قدرت و اقتصاد رسانه را کم‌بررسی گذاشت؛ با این حال، یکی از جامع‌ترین مدل‌های اروپایی این حوزه است.",
        applications=[
            "تحلیل تولید خبر در سازمان رسانه.",
            "پژوهش ادراک و تفسیر مخاطب.",
            "آموزش ارتباطات سازمانی.",
            "طراحی پیام بهداشتی و عمومی.",
            "مطالعهٔ تصویر فرستنده در مخاطب.",
        ],
        example_text="خبرنگاری که تصور می‌کند مخاطبش جوان و بی‌حوصله است، لحن خبر را تندتر و کوتاه‌تر می‌کند؛ همان خبر در خانواده‌ای سنتی با پیش‌فرض‌های دیگر خوانده و بازسازی می‌شود و ممکن است معنایی متفاوت بگیرد.",
        evolution="کتاب سال ۱۹۶۳ مالتزکه مدل را در سنت روان‌شناسی ارتباط جمعی آلمان صورت‌بندی کرد و نسل‌های بعدی پژوهش ارتباط در اروپا آن را گستردند. با ظهور رسانه‌های دیجیتال، برخی قیدهای آن مانند هم‌زمانی و پراکندگی مخاطب بازبینی شد.",
        key_concepts=["بازسازی روان‌شناختی", "خودانگاره", "میدان ادراک", "فشار سازمانی", "علنی بودن", "هم‌زمانی"],
        theorists="گرهارد مالتزکه.",
        theorists_text="مدل در سنت روان‌شناسی ارتباط جمعی آلمان شکل گرفت.",
        model="برهم‌کنش میدان ادراکی فرستنده و گیرنده زیر فشارهای سازمانی و اجتماعی که پیام را در دریافت به بازسازی روان‌شناختی می‌کشاند.",
        studies=[
            "کتاب سال ۱۹۶۳ مدل چندلایه را معرفی کرد.",
            "پژوهش آلمانی، فشار سازمانی را مستند کرد.",
            "مطالعات مخاطب، بازسازی پیام را سنجیدند.",
            "پژوهش دیجیتال، قید هم‌زمانی را بازبینی کرد.",
            "پژوهش سازمانی، نقش تصویر مخاطب را مستند کرد.",
            "پژوهش روان‌شناسی، بازسازی پیام را آزمود.",
        ],
    ),
    "MC-544": dict(
        year=1934,
        summary="مدل ارگانون بولر، که کارل بولر در کتاب نظریهٔ زبان در سال ۱۹۳۴ صورت‌بندی کرد، نشانهٔ زبانی را ابزاری سه‌کارکردی می‌داند. بولر با الهام از مفهوم ارگانون در اندیشهٔ یونانی، زبان را ابزار ارتباط میان سه قطب می‌بیند: گوینده، شنونده و جهان. هر نشانهٔ زبانی هم‌زمان سه کارکرد دارد. کارکرد بیان، حال و نگرش گوینده را نشان می‌دهد. کارکرد برانگیختن، شنونده را به واکنش وامی‌دارد. کارکرد بازنمایی، جهان و اشیا را به‌صورت نمادین ارائه می‌کند. بولر این سه کارکرد را در یک مثلث نشانه‌شناختی ترسیم کرد که در آن نشانه با هر سه ضلع نسبت دارد، اما نسبت آن با جهان بازنمایی‌گرانه است. این مدل پایهٔ نظریهٔ کارکردهای زبان شد و بعدها جاکوبسون آن را گسترد و به شش کارکرد رساند. بولر تأکید کرد که کارکرد بازنمایی در زبان انسان ویژگی بنیادین است و زبان را از آوای حیوانی جدا می‌کند. نقدهای اصلی به مدل، ساده‌سازی روابط نشانه، کم‌توجهی به بستر اجتماعی و نهادی، فرض جدایی نسبتاً روشن سه قطب، تمرکز بر زبان کلامی و دشواری تعمیم به پیام‌های تصویری و دیجیتال را برجسته می‌کنند.",
        definition="مدل ارگانون بولر، نشانهٔ زبانی را ابزاری سه‌کارکردی می‌داند که هم‌زمان حال گوینده را بیان می‌کند، شنونده را برمی‌انگیزد و جهان را بازنمایی می‌کند.",
        main_problem="نشانهٔ زبانی چگونه هم‌زمان به گوینده، شنونده و جهان نسبت دارد و کدام کارکرد، ویژگی بنیادین زبان انسان را می‌سازد.",
        mechanism="هر نشانه در مثلث گوینده، شنونده و جهان جای می‌گیرد؛ نسبت با گوینده کارکرد بیان، نسبت با شنونده کارکرد برانگیختن و نسبت با جهان کارکرد بازنمایی را فعال می‌کند.",
        assumptions=[
            "نشانهٔ زبانی سه نسبت دارد.",
            "سه کارکرد هم‌زمان فعال‌اند.",
            "بازنمایی ویژگی بنیادین زبان است.",
            "گوینده و شنونده دو قطب متمایزند.",
            "زبان انسان با آوای حیوانی تفاوت بنیادین دارد.",
        ],
        principles=[
            "سه قطب نشانه را جداگانه مشخص کن.",
            "کارکرد بیان را از بازنمایی تفکیک کن.",
            "کارکرد برانگیختن را در پیام بیاب.",
            "نسبت نشانه با جهان را تحلیل کن.",
            "بازنمایی را هستهٔ زبان انسان بدان.",
            "کارکردهای هم‌زمان را در یک مثلث ببین.",
            "نسبت نشانه با گوینده را جداگانه بسنج.",
            "کارکردها را در یک پیام هم‌زمان ببین.",
            "سه قطب را در تحلیل پیام جدا نگه دار.",
        ],
        critiques=[
            "روابط نشانه را ساده می‌کند.",
            "بستر اجتماعی و نهادی را کم‌می‌شمارد.",
            "جدایی سه قطب را روشن‌تر از واقع فرض می‌کند.",
            "بر زبان کلامی متمرکز است.",
            "تعمیم آن به پیام تصویری دشوار است.",
            "نقش قرارداد اجتماعی در معنا را کم‌می‌شمارد.",
            "کارکرد برانگیختن را از ترغیب جدا نمی‌کند.",
        ],
        critique_text="منتقدان می‌گویند مدل ارگانون بولر پایهٔ نظریهٔ کارکردهای زبان را نهاد اما روابط نشانه را ساده کرد و بستر اجتماعی و پیام‌های غیرکلامی را کم‌بررسی گذاشت؛ با این حال، همچنان نقطهٔ شروع تحلیل کارکردی ارتباط است.",
        applications=[
            "تحلیل کارکرد پیام تبلیغی.",
            "آموزش نشانه‌شناسی زبان.",
            "مطالعهٔ کارکرد بازنمایی خبر.",
            "تحلیل گفتمان سیاسی.",
            "پژوهش ارتباط غیرکلامی.",
            "تحلیل پیام در ارتباطات سلامت.",
        ],
        example_text="جمله‌ای مانند هوا سرد است هم‌زمان جهان را بازنمایی می‌کند، حال گوینده را بیان می‌کند و ممکن است شنونده را به بستن پنجره برانگیزد؛ سه کارکرد در یک جملهٔ کوتاه فعال‌اند.",
        evolution="کتاب سال ۱۹۳۴ بولر مدل ارگانون را در نظریهٔ زبان صورت‌بندی کرد و پایهٔ کارکردگرایی در زبان‌شناسی شد. جاکوبسون در سال ۱۹۶۰ آن را به شش کارکرد گسترد و نشانه‌شناسی معاصر آن را به تحلیل رسانه تعمیم داد.",
        key_concepts=["ارگانون", "کارکرد بیان", "کارکرد برانگیختن", "کارکرد بازنمایی", "مثلث نشانه", "بازنمایی"],
        theorists="کارل بولر.",
        theorists_text="مدل در سنت روان‌شناسی زبان و نظریهٔ نشانه شکل گرفت.",
        model="مثلث گوینده، شنونده و جهان که نشانهٔ زبانی را هم‌زمان به بیان، برانگیختن و بازنمایی پیوند می‌دهد.",
        studies=[
            "کتاب سال ۱۹۳۴ مدل ارگانون را معرفی کرد.",
            "جاکوبسون مدل را به شش کارکرد گسترد.",
            "پژوهش نشانه‌شناسی، مثلث را بازخوانی کرد.",
            "مطالعات رسانه، کارکردها را به تصویر تعمیم دادند.",
            "پژوهش زبان‌شناسی، مثلث بولر را بازخوانی کرد.",
            "مطالعات ارتباط، کارکرد بیان را در تبلیغ سنجیدند.",
            "پژوهش ترجمه، کارکرد بازنمایی را بررسی کرد.",
        ],
    ),
}

NAME_FIX = {
    "MC-541": ("مدل رایلی و رایلی", "Riley and Riley Model", "پرانتز «جامعه‌شناختی» از عنوان حذف شد تا نام متعارف مدل ثبت شود و توضیح جامعه‌شناختی به متن مدخل منتقل شود."),
    "MC-543": ("مدل مالتزکه", "Maletzke's Model", "نگارش پیشین «مالِتزکه» و «Maltzke» نادرست بود؛ نام خانوادگی درست گرهارد مالتزکه ثبت شد."),
    "MC-544": ("مدل ارگانون بولر", "Bühler's Organon Model", "عنوان پیشین «مدل بوم/ارابه» و «Ecosystem/Bandwagon» با محتوای کارت (سه کارکرد زبان بولر) هم‌خوان نبود و به نام واقعی مدل اصلاح شد."),
}
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
                                       "verified": n_verified, "batch": 147}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH147 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
