# -*- coding: utf-8 -*-
"""Batch 129 (MODEL): full documentation for MC-014, MC-021, MC-022, MC-028."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch129-model-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch129_model.json"

S = {
    "MC-014": [
        dict(kind="BOOK_CHAPTER",
             title_en="Encoding/Decoding",
             title_fa="رمزگذاری/رمزگشایی",
             authors="Hall, S.", year=1980,
             publisher="Hutchinson (Culture, Media, Language)",
             doi=None,
             url="https://spkb.blot.im/_readings/EncodingDecoding_HALL_1980.pdf",
             language="en", isbn=None,
             citation="Hall, S. (1980). Encoding/decoding. In S. Hall, D. Hobson, A. Lowe, & P. Willis (Eds.), Culture, Media, Language (pp. 128-138). London: Hutchinson.",
             locator="pp. 128-138", locator_type="page_range",
             supports="three decoding positions: dominant-hegemonic, negotiated, oppositional", verified=True),
        dict(kind="BOOK_CHAPTER",
             title_en="Encoding and Decoding in the Television Discourse",
             title_fa="رمزگذاری و رمزگشایی در گفتمان تلویزیونی",
             authors="Hall, S.", year=1973,
             publisher="Centre for Contemporary Cultural Studies, University of Birmingham",
             doi=None,
             url="https://epapers.bham.ac.uk/2962/",
             language="en", isbn=None,
             citation="Hall, S. (1973). Encoding and decoding in the television discourse (CCCS Stencilled Paper No. 7). Birmingham: Centre for Contemporary Cultural Studies.",
             locator="Stencilled Paper No. 7", locator_type="SECTION",
             supports="original formulation of the encoding/decoding circuit", verified=True),
    ],
    "MC-021": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Elaboration Likelihood Model of Persuasion",
             title_fa="مدل احتمال بسط در اقناع",
             authors="Petty, R. E.; Cacioppo, J. T.", year=1986,
             publisher="Advances in Experimental Social Psychology",
             doi="10.1016/S0065-2601(08)60214-2",
             url="https://www.sciencedirect.com/science/chapter/bookseries/pii/S0065260108602142",
             language="en", isbn=None,
             citation="Petty, R. E., & Cacioppo, J. T. (1986). The elaboration likelihood model of persuasion. Advances in Experimental Social Psychology, 19, 123-205.",
             locator="19:123-205", locator_type="page_range",
             supports="central and peripheral routes of persuasion moderated by motivation and ability", verified=True),
        dict(kind="BOOK",
             title_en="Communication and Persuasion: Central and Peripheral Routes to Attitude Change",
             title_fa="ارتباطات و اقناع: مسیرهای مرکزی و پیرامونی برای تغییر نگرش",
             authors="Petty, R. E.; Cacioppo, J. T.", year=1986,
             publisher="Springer-Verlag",
             doi=None, url=None, language="en", isbn=None,
             citation="Petty, R. E., & Cacioppo, J. T. (1986). Communication and Persuasion: Central and Peripheral Routes to Attitude Change. New York: Springer-Verlag.",
             locator="book", locator_type="SECTION",
             supports="book-length statement of the dual-route model", verified=False),
    ],
    "MC-022": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Heuristic Versus Systematic Information Processing and the Use of Source Versus Message Cues in Persuasion",
             title_fa="پردازش اطلاعات اکتشافی در برابر نظام‌مند و کاربرد نشانه‌های منبع در برابر پیام در اقناع",
             authors="Chaiken, S.", year=1980,
             publisher="Journal of Personality and Social Psychology",
             doi="10.1037/0022-3514.39.5.752",
             url="https://fbaum.unc.edu/teaching/articles/jpsp-1980-Chaiken.pdf",
             language="en", isbn=None,
             citation="Chaiken, S. (1980). Heuristic versus systematic information processing and the use of source versus message cues in persuasion. Journal of Personality and Social Psychology, 39(5), 752-766.",
             locator="39(5):752-766", locator_type="page_range",
             supports="two modes of processing and sufficiency principle in persuasion", verified=True),
        dict(kind="BOOK_CHAPTER",
             title_en="Heuristic and Systematic Information Processing Within and Beyond the Persuasion Context",
             title_fa="پردازش اطلاعات اکتشافی و نظام‌مند درون و فراتر از بافت اقناع",
             authors="Chaiken, S.; Liberman, A.; Eagly, A. H.", year=1989,
             publisher="Guilford Press (Unintended Thought)",
             doi=None, url=None, language="en", isbn=None,
             citation="Chaiken, S., Liberman, A., & Eagly, A. H. (1989). Heuristic and systematic information processing within and beyond the persuasion context. In J. S. Uleman & J. A. Bargh (Eds.), Unintended Thought (pp. 212-252). New York: Guilford Press.",
             locator="pp. 212-252", locator_type="page_range",
             supports="co-occurrence of heuristic and systematic processing", verified=False),
    ],
    "MC-028": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Stages and Processes of Self-Change of Smoking: Toward an Integrative Model of Change",
             title_fa="مراحل و فرایندهای خودتغییری در سیگار: به‌سوی مدلی یکپارچه برای تغییر",
             authors="Prochaska, J. O.; DiClemente, C. C.", year=1983,
             publisher="Journal of Consulting and Clinical Psychology",
             doi="10.1037/0022-006X.51.3.390",
             url="https://pubmed.ncbi.nlm.nih.gov/6863699/",
             language="en", isbn=None,
             citation="Prochaska, J. O., & DiClemente, C. C. (1983). Stages and processes of self-change of smoking: Toward an integrative model of change. Journal of Consulting and Clinical Psychology, 51(3), 390-395.",
             locator="51(3):390-395", locator_type="page_range",
             supports="five stages and ten processes of change in the transtheoretical model", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="In Search of How People Change: Applications to Addictive Behaviors",
             title_fa="در جست‌وجوی چگونگی تغییر مردم: کاربردها در رفتارهای اعتیادی",
             authors="Prochaska, J. O.; DiClemente, C. C.; Norcross, J. C.", year=1992,
             publisher="American Psychologist",
             doi=None, url=None, language="en", isbn=None,
             citation="Prochaska, J. O., DiClemente, C. C., & Norcross, J. C. (1992). In search of how people change: Applications to addictive behaviors. American Psychologist, 47(9), 1102-1114.",
             locator="47(9):1102-1114", locator_type="page_range",
             supports="consolidated statement of the transtheoretical model", verified=False),
    ],
}

ENRICH = {
    "MC-014": dict(
        year=1973,
        summary="مدل رمزگذاری و رمزگشایی، مدلی در مطالعات فرهنگی و ارتباطات است که استوارت هال آن را در مقاله‌ای در سال ۱۹۷۳ در مرکز مطالعات فرهنگی معاصر بیرمنگام ارائه کرد و در سال ۱۹۸۰ در کتاب فرهنگ، رسانه، زبان منتشر شد. ادعای مرکزی این است که معنا در متن رسانه‌ای امری ثابت و بسته نیست: تولیدکنندگان پیام را بر پایهٔ چارچوب‌های فکری، منافع نهادی و روابط قدرت «رمزگذاری» می‌کنند، اما مخاطبان منفعل نیستند و بر پایهٔ موقعیت اجتماعی و تجربهٔ فرهنگی خود آن را «رمزگشایی» می‌کنند. هال سه موقعیت رمزگشایی را از هم جدا کرد: موقعیت مسلط-هژمونیک، یعنی پذیرش کامل معنای رمزگذاری‌شده؛ موقعیت مذاکره‌ای، یعنی پذیرش بخشی از معنا همراه با مقاومت در بخشی دیگر؛ و موقعیت تقابلی، یعنی خوانش معنایی مخالف با قصد تولیدکننده. اهمیت این مدل در تحلیل خبر، تبلیغ، برنامهٔ سرگرمی و پذیرش یا مقاومت مخاطب است و پژوهش‌های دریافت پس از آن را شکل داد. نقدهای اصلی به آن، تمرکز بیش از اندازه بر متن، کم‌توجهی به شواهد تجربی دریافت، مبهم‌بودن مفهوم چارچوب مسلط و دشواری سنجش موقعیت‌های رمزگشایی مربوط می‌شود.",
        definition="مدل رمزگذاری و رمزگشایی، مدلی است که تولید معنا در رسانه را در دو مرحلهٔ رمزگذاری به‌دست تولیدکننده و رمزگشایی به‌دست مخاطب می‌بیند و سه موقعیت خوانش مسلط، مذاکره‌ای و تقابلی را از هم جدا می‌کند.",
        main_problem="اگر تولیدکننده معنا را در متن رمزگذاری می‌کند، چرا مخاطبان مختلف به یک متن یکسان معناهای متفاوت می‌دهند و چه چیزی این تفاوت را توضیح می‌دهد.",
        mechanism="تولیدکننده پیام را در چارچوب رمز فرهنگی مسلط رمزگذاری می‌کند؛ مخاطب در موقعیت اجتماعی خود و با منابع فرهنگی خویش آن را رمزگشایی می‌کند و ممکن است معنا را کامل بپذیرد، بخشی را مذاکره کند یا آن را وارونه بخواند. معنا محصول تقاطع این دو مرحله است و نه محتوای متن به‌تنهایی.",
        assumptions=[
            "معنا در متن به‌طور کامل و ثابت تعیین نمی‌شود.",
            "تولیدکننده و مخاطب، رمزهای فرهنگی متفاوتی در اختیار دارند.",
            "موقعیت اجتماعی مخاطب، شکل رمزگشایی را قالب می‌زند.",
            "چند خوانش از یک متن ممکن است و همه به یک اندازه مشروع نیستند.",
            "رسانه، میدان رقابت معنا و قدرت است.",
        ],
        principles=[
            "تولید و دریافت معنا دو مرحلهٔ متمایزند.",
            "متن، ساختار رمزگذاری‌شده دارد اما معنای بسته ندارد.",
            "سه موقعیت خوانش مسلط، مذاکره‌ای و تقابلی باید از هم تفکیک شوند.",
            "رمزهای فرهنگی، محصول روابط قدرت و تاریخ‌اند.",
            "مخاطب فعال است اما در محدودهٔ منابع فرهنگی خود.",
            "تحلیل رسانه باید هم تولید و هم دریافت را ببیند.",
        ],
        critiques=[
            "مدل بیش از اندازه بر متن و رمز تمرکز دارد.",
            "شواهد تجربی دریافت در نسخهٔ اولیه محدود است.",
            "مفهوم چارچوب معنایی مسلط مبهم می‌ماند.",
            "سنجش موقعیت‌های سه‌گانه در پژوهش دشوار است.",
            "نقش عاطفه و بدن در دریافت کم‌بررسی می‌ماند.",
        ],
        critique_text="منتقدان می‌گویند مدل رمزگذاری و رمزگشایی مخاطب را فعال کرد اما فعال‌بودن او را بیشتر در چارچوب رمزهای موجود تعریف کرد؛ پژوهش‌های بعدی دریافت نشان دادند که خوانش مخاطبان بیش از سه موقعیت و آمیخته با تجربهٔ روزمره است. با این حال، این مدل یکی از بنیادی‌ترین چارچوب‌های مطالعات فرهنگی رسانه باقی مانده است.",
        applications=[
            "تحلیل دریافت خبر و مقاومت مخاطب در برابر روایت رسمی.",
            "پژوهش خوانش مخاطبان از تبلیغات و سرگرمی.",
            "تحلیل میم‌ها و بازتفسیر محتوا در شبکه‌های اجتماعی.",
            "آموزش سواد رسانه‌ای و تحلیل رمزهای فرهنگی.",
            "پژوهش مخاطب در رسانه‌های هویتی و قومی.",
        ],
        example_text="یک گزارش خبری دربارهٔ یک سیاست اقتصادی ممکن است با رمز «ضرورت اصلاح» تولید شود؛ گروهی از مخاطبان آن را کامل بپذیرند، گروهی بخشی از آن را بپذیرند و در بخشی تردید کنند، و گروهی آن را خوانشی وارونه و در خدمت منافع خاص ببینند. مدل رمزگذاری و رمزگشایی این تفاوت را به تفاوت موقعیت‌های اجتماعی و رمزهای فرهنگی نسبت می‌دهد.",
        evolution="مقالهٔ سال ۱۹۷۳ نسخهٔ نخست مدل را در مرکز بیرمنگام ارائه کرد و انتشار سال ۱۹۸۰ آن را به متن مرجع مطالعات فرهنگی تبدیل کرد. پژوهش‌های دریافت در دههٔ ۱۹۸۰ مدل را تجربی‌تر کردند و در دههٔ ۲۰۰۰ با مطالعات مخاطب دیجیتال و محتوای کاربرساخته بازخوانی شد.",
        key_concepts=["رمزگذاری", "رمزگشایی", "چارچوب معنایی مسلط", "خوانش مذاکره‌ای", "خوانش تقابلی", "رمز فرهنگی", "مخاطب فعال"],
        theorists="استوارت هال، صورت‌بند مدل رمزگذاری و رمزگشایی در سنت مطالعات فرهنگی بیرمنگام.",
        theorists_text="این مدل در سنت مطالعات فرهنگی بریتانیا شکل گرفت و با نظریهٔ هژمونی و تحلیل گفتمان پیوند خورد.",
        model="مدل مرحله‌ای: رمزگذاری در نهاد تولید، متن به‌عنوان ساختار رمزگذاری‌شده، رمزگشایی در موقعیت اجتماعی مخاطب، و سه خوانش ممکن؛ معنا در تقاطع این مراحل ساخته می‌شود.",
        studies=[
            "مقالهٔ سال ۱۹۷۳ نسخهٔ نخست مدل سه‌موقعیتی را معرفی کرد.",
            "انتشار سال ۱۹۸۰ مدل را به متن مرجع مطالعات فرهنگی تبدیل کرد.",
            "پژوهش‌های دریافت، خوانش مخاطبان مختلف از یک برنامه را آزمودند.",
            "مطالعات دیجیتال، مدل را برای بازتفسیر محتوا در پلتفرم‌ها به کار بردند.",
        ],
    ),
    "MC-021": dict(
        year=1986,
        summary="مدل احتمال بسط، مدلی در روان‌شناسی اقناع است که ریچارد پتی و جان کاسیوپو در سال ۱۹۸۶ صورت‌بندی کردند. ادعای مرکزی این است که پیام‌های اقناعی از دو مسیر ذهنی متمایز پردازش می‌شوند: مسیر مرکزی، که در آن مخاطب با انگیزه و توان کافی، استدلال‌های پیام را دقیق می‌سنجد؛ و مسیر پیرامونی، که در آن مخاطب با نشانه‌های ساده مانند جذابیت منبع، اعتبار ظاهری یا شمار استدلال‌ها قضاوت می‌کند. انتخاب مسیر به «احتمال بسط» بستگی دارد، یعنی به میزان انگیزه و توانایی شناختی مخاطب برای درگیرشدن با پیام. تغییر نگرش از مسیر مرکزی پایدارتر، مقاوم‌تر در برابر اقناع متقابل و پیش‌بین قوی‌تر رفتار است؛ تغییر از مسیر پیرامونی موقتی و شکننده است. این مدل در تحلیل تبلیغات، کمپین‌های سلامت، ارتباطات سیاسی و پذیرش اطلاعات نادرست به کار می‌رود. نقدهای اصلی به آن، دشواری سنجش مستقل بسط، همپوشانی دو مسیر در عمل، ابهام مرز نشانه‌های پیرامونی و پیوند ضعیف با یافته‌های علوم اعصاب مربوط می‌شود.",
        definition="مدل احتمال بسط، مدلی است که اقناع را در دو مسیر مرکزی و پیرامونی توضیح می‌دهد و انتخاب مسیر را به انگیزه و توانایی شناختی مخاطب برای بسط پیام وابسته می‌داند.",
        main_problem="چرا یک پیام یکسان برای برخی مخاطبان تغییر نگرش پایدار می‌سازد و برای برخی دیگر تنها واکنشی گذرا، و چه عواملی این تفاوت را تعیین می‌کند.",
        mechanism="اگر مخاطب انگیزه و توان کافی برای پردازش داشته باشد، استدلال‌ها را می‌سنجد و نگرشش از راه مسیر مرکزی تغییر می‌کند؛ اگر انگیزه یا توان کم باشد، به نشانه‌های پیرامونی تکیه می‌کند و تغییر نگرش سطحی و موقت است. افزایش انگیزه و توان، احتمال بسط را بالا می‌برد.",
        assumptions=[
            "مخاطب موجودی شناختی فعال است که بسته به شرایط، پیام را عمیق یا سطحی پردازش می‌کند.",
            "تغییر نگرش از مسیر مرکزی پایدارتر و مقاوم‌تر است.",
            "انگیزه و توانایی، دو شرط اصلی پردازش عمیق‌اند.",
            "نشانه‌های منبع و بافت، در پردازش سطحی اثر می‌گذارند.",
            "اثر متغیرهای اقناعی به مسیر پردازش وابسته است.",
        ],
        principles=[
            "اقناع را باید در یک پیوستار بسط فهمید و نه دو حالت مطلق.",
            "انگیزه و توانایی شناختی، احتمال بسط را تعیین می‌کنند.",
            "کیفیت استدلال در مسیر مرکزی و نشانه‌های پیرامونی در مسیر سطحی وزن دارند.",
            "تغییر نگرش مرکزی پایدارتر و پیش‌بین رفتار است.",
            "یک متغیر می‌تواند بسته به شرایط، نقش مرکزی یا پیرامونی بگیرد.",
            "طراحی پیام باید با سطح پردازش مخاطب هم‌خوان باشد.",
        ],
        critiques=[
            "سنجش مستقل احتمال بسط در پژوهش دشوار است.",
            "مرز مسیر مرکزی و پیرامونی در عمل مبهم می‌شود.",
            "برخی یافته‌های آزمایشگاهی بازتولیدپذیری ضعیفی داشته‌اند.",
            "نقش عاطفه و خودکاربودن تصمیم کم‌بررسی می‌ماند.",
            "تعمیم نتایج آزمایشگاهی به محیط رسانه‌ای پیچیده محدود است.",
        ],
        critique_text="منتقدان می‌گویند مدل احتمال بسط چارچوبی روشن برای تفکیک پردازش عمیق و سطحی فراهم کرد، اما سنجش تجربی «بسط» و مرزبندی دو مسیر آسان نیست و پژوهش‌های بعدی نشان دادند که عوامل عاطفی و خودکار نیز در اقناع نقش دارند. با این حال، مدل همچنان یکی از پرکاربردترین چارچوب‌های اقناع است.",
        applications=[
            "طراحی پیام تبلیغاتی و کمپین سلامت.",
            "تحلیل اقناع سیاسی و تبلیغات انتخاباتی.",
            "پژوهش مقاومت مخاطب در برابر اطلاعات نادرست.",
            "طراحی آموزش و پیام‌های عمومی برای مخاطبان کم‌انگیزه.",
            "تحلیل اثر اعتبار منبع و جذابیت پیام‌آور.",
        ],
        example_text="در یک تبلیغ دارویی، مخاطبی که خودش دربارهٔ بیماری تحقیق کرده است استدلال‌های علمی آگهی را می‌سنجد؛ مخاطبی که بی‌حوصله از کنار آگهی می‌گذرد، تنها به شهرت برند یا چهرهٔ معرفی‌کننده تکیه می‌کند. مدل احتمال بسط توضیح می‌دهد چرا اثر اولی پایدارتر است.",
        evolution="ریشهٔ مدل در پژوهش‌های دههٔ ۱۹۷۰ دربارهٔ اقناع و پردازش استدلال است. مقالهٔ سال ۱۹۸۶ در مجموعهٔ روان‌شناسی اجتماعی تجربی و کتاب همان سال، مدل را تثبیت کردند. پژوهش‌های بعدی، مدل را به سلامت، سیاست، مصرف و رسانهٔ دیجیتال گستردند و در دههٔ ۲۰۱۰ با نقد بازتولیدپذیری روبه‌رو شدند.",
        key_concepts=["مسیر مرکزی", "مسیر پیرامونی", "احتمال بسط", "انگیزه", "توانایی شناختی", "کیفیت استدلال", "نشانه‌های پیرامونی"],
        theorists="ریچارد پتی و جان کاسیوپو، سازندگان مدل احتمال بسط.",
        theorists_text="این مدل در سنت روان‌شناسی اجتماعی اقناع و پژوهش نگرش شکل گرفت و با مدل‌های دوگانهٔ پردازش اطلاعات پیوند خورد.",
        model="مدل دو‌مسیره: انگیزه و توانایی، احتمال بسط را تعیین می‌کنند؛ بسط بالا مسیر مرکزی و تغییر نگرش پایدار، بسط پایین مسیر پیرامونی و تغییر موقت را به دنبال دارد.",
        studies=[
            "مقالهٔ سال ۱۹۸۶ مدل را با شواهد آزمایشی صورت‌بندی کرد.",
            "کتاب همان سال، چارچوب کامل دو مسیر را ارائه کرد.",
            "پژوهش‌های سلامت و سیاست، مدل را در پیام‌های واقعی آزمودند.",
            "مرورهای بعدی، شواهد و محدودیت‌های مدل را ارزیابی کردند.",
        ],
    ),
    "MC-022": dict(
        year=1980,
        summary="مدل اکتشافی-نظام‌مند، مدلی در روان‌شناسی اجتماعی پردازش اطلاعات است که شلی چایکن در سال ۱۹۸۰ معرفی کرد. ادعای مرکزی این است که افراد میان دو شیوهٔ پردازش انتخاب می‌کنند: پردازش نظام‌مند، یعنی بررسی دقیق و پرتلاش محتوای پیام؛ و پردازش اکتشافی، یعنی کاربرد قواعد سادهٔ شناختی مانند «کارشناسان راست می‌گویند» یا «اکثریت درست می‌گوید». انتخاب شیوه بر پایهٔ «اصل کفایت» است: فرد تا جایی پردازش می‌کند که اطمینان کافی برای قضاوت به دست آورد، و اگر اطمینان لازم بالا باشد یا انگیزه کم باشد، به قاعدهٔ اکتشافی بسنده می‌کند. نسخهٔ بعدی مدل نشان داد دو شیوه می‌توانند هم‌زمان رخ دهند و اثرشان جمع شود، و سه انگیزهٔ دقت، دفاع از خود و تأثیرگذاری بر دیگران، سطح کفایت را تعیین می‌کند. این مدل در تحلیل اعتبار منبع، پذیرش اطلاعات نادرست و اقناع آنلاین به کار می‌رود. نقدهای اصلی به آن، ابهام محتوای قواعد اکتشافی، دشواری سنجش آستانهٔ کفایت، همپوشانی با مدل احتمال بسط و کم‌توجهی به عاطفه مربوط می‌شود.",
        definition="مدل اکتشافی-نظام‌مند، مدلی است که دو شیوهٔ پردازش اطلاعات، یعنی بررسی دقیق و پرتلاش در برابر کاربرد قواعد سادهٔ شناختی، را از هم جدا می‌کند و انتخاب شیوه را به اصل کفایت وابسته می‌داند.",
        main_problem="افراد چگونه تصمیم می‌گیرند چه اندازه برای پردازش یک پیام تلاش کنند، و چه زمانی به قاعده‌های سادهٔ شناختی بسنده می‌کنند.",
        mechanism="فرد آستانه‌ای از اطمینان لازم برای قضاوت دارد؛ اگر پردازش اکتشافی به این آستانه برسد، تلاش بیشتر نمی‌کند و اگر نرسد یا انگیزه‌اش بالا باشد، پردازش نظام‌مند را آغاز می‌کند. دو شیوه می‌توانند هم‌زمان عمل کنند و اثرشان با هم جمع شود.",
        assumptions=[
            "افراد در پردازش اطلاعات، کم‌تلاش‌ترین مسیر کافی را برمی‌گزینند.",
            "قواعد اکتشافی در حافظه ذخیره شده‌اند و به‌سرعت فعال می‌شوند.",
            "آستانهٔ اطمینان به انگیزه و شرایط وابسته است.",
            "پردازش نظام‌مند و اکتشافی می‌توانند هم‌زمان رخ دهند.",
            "انگیزهٔ دقت، دفاع و تأثیرگذاری، سطح کفایت را تعیین می‌کند.",
        ],
        principles=[
            "دو شیوهٔ پردازش باید از هم تفکیک شوند.",
            "اصل کفایت، توقف یا ادامهٔ پردازش را توضیح می‌دهد.",
            "قاعده‌های اکتشافی مانند اعتبار منبع و اجماع، میان‌بر شناختی‌اند.",
            "پردازش نظام‌مند به توان و انگیزهٔ بیشتر نیاز دارد.",
            "اثر دو شیوه می‌تواند جمع شود و نه فقط جانشین یکدیگر.",
            "بافت و انگیزه، آستانهٔ کفایت را جابه‌جا می‌کنند.",
        ],
        critiques=[
            "محتوای قواعد اکتشافی روشن و شمارش‌پذیر نیست.",
            "آستانهٔ کفایت به‌سختی سنجیده می‌شود.",
            "همپوشانی زیادی با مدل احتمال بسط دارد.",
            "نقش عاطفه و تجربهٔ بدن در پردازش کم‌بررسی می‌ماند.",
            "شواهد تجربی دربارهٔ جمع‌شدن دو شیوه ناهمگون است.",
        ],
        critique_text="منتقدان می‌گویند مدل اکتشافی-نظام‌مند چارچوبی ظریف‌تر از مدل‌های دوگانهٔ ساده ارائه می‌دهد اما مفاهیم آن دشوار سنجیده می‌شوند و مرز آن با مدل احتمال بسط روشن نیست. با این حال، مفهوم قاعدهٔ اکتشافی و اصل کفایت، در پژوهش اقناع و اعتبار رسانه بسیار اثرگذار بوده است.",
        applications=[
            "تحلیل اعتبار منبع در خبر و رسانهٔ اجتماعی.",
            "پژوهش پذیرش اطلاعات نادرست و شایعه.",
            "طراحی پیام‌های سلامت با میان‌برهای شناختی.",
            "تحلیل تصمیم خرید و تبلیغات مصرفی.",
            "آموزش سواد رسانه‌ای برای شناخت قاعده‌های اکتشافی.",
        ],
        example_text="در شبکه‌های اجتماعی، کاربری که با انبوه پست روبه‌روست ممکن است بر پایهٔ قاعدهٔ «بازنشر زیاد یعنی درست است» قضاوت کند؛ اما اگر موضوع برایش مهم باشد یا با نشانه‌های ناسازگار روبه‌رو شود، پردازش نظام‌مند را آغاز می‌کند. مدل اکتشافی-نظام‌مند این جابه‌جایی را توضیح می‌دهد.",
        evolution="مقالهٔ سال ۱۹۸۰ نسخهٔ نخست مدل را معرفی کرد و پژوهش‌های دههٔ ۱۹۸۰ و ۱۹۹۰ نسخهٔ پردازش هم‌زمان و اصل کفایت را بسط دادند. در دههٔ ۲۰۰۰ مدل برای تحلیل اعتبار در محیط آنلاین و پذیرش اطلاعات نادرست به کار رفت.",
        key_concepts=["پردازش نظام‌مند", "پردازش اکتشافی", "اصل کفایت", "قاعدهٔ اکتشافی", "انگیزهٔ دقت", "آستانهٔ اطمینان"],
        theorists="شلی چایکن، سازندهٔ مدل؛ و همکارانی که نسخهٔ هم‌زمانی دو شیوه را بسط دادند.",
        theorists_text="این مدل در سنت روان‌شناسی اجتماعی اقناع شکل گرفت و با پژوهش تغییر نگرش و تصمیم‌گیری پیوند خورد.",
        model="مدل کفایت‌محور: اهداف و انگیزه، آستانهٔ اطمینان را تعیین می‌کنند؛ پردازش اکتشافی و نظام‌مند می‌توانند هم‌زمان عمل کنند و قضاوت نهایی از ترکیب آنها ساخته می‌شود.",
        studies=[
            "مقالهٔ سال ۱۹۸۰ مدل دو شیوه را با شواهد آزمایشی معرفی کرد.",
            "پژوهش‌های دههٔ ۱۹۸۰ نسخهٔ هم‌زمانی و اصل کفایت را بسط دادند.",
            "مطالعات اعتبار منبع، وزن قاعده‌های اکتشافی را آزمودند.",
            "پژوهش اطلاعات نادرست، مدل را برای محیط آنلاین به کار برد.",
        ],
    ),
    "MC-028": dict(
        year=1983,
        summary="مدل فرانظری، مدلی برای تغییر رفتار است که جیمز پروچاسکا و کارلو دی‌کلمنته در مقالهٔ سال ۱۹۸۳ دربارهٔ خودتغییری سیگار صورت‌بندی کردند. ادعای مرکزی این است که تغییر رفتار رویدادی لحظه‌ای نیست، بلکه فرایندی مرحله‌ای است: پیش‌تفکر، یعنی فرد در آیندهٔ نزدیک قصد تغییر ندارد؛ تفکر، یعنی فرد مشکل را می‌شناسد و سود و زیان تغییر را می‌سنجد؛ آماده‌سازی، یعنی فرد قصد جدی تغییر در آیندهٔ نزدیک دارد؛ عمل، یعنی فرد رفتار را در بازهٔ کوتاه تغییر می‌دهد؛ و حفظ، یعنی تغییر تثبیت می‌شود. مدل با ده فرایند تغییر، تعادل تصمیم و خودکارآمدی تکمیل می‌شود و مداخلهٔ هم‌خوان با مرحلهٔ فرد را پیشنهاد می‌کند. پژوهش اصلی با نزدیک به هزار شرکت‌کننده در مراحل مختلف ترک سیگار انجام شد و تفاوت فرایندهای مؤثر در هر مرحله را نشان داد. این مدل در سیاست سلامت، کمپین‌های رسانه‌ای و طراحی پیام تغییر رفتار کاربرد گسترده یافته است. نقدهای اصلی به آن، مرزهای دلبخواهی مراحل، فرض حرکت خطی، شواهد ناهمگون دربارهٔ کارایی و کم‌توجهی به بافت اجتماعی مربوط می‌شود.",
        definition="مدل فرانظری، مدلی است که تغییر رفتار را در پنج مرحلهٔ پیش‌تفکر، تفکر، آماده‌سازی، عمل و حفظ توضیح می‌دهد و مداخلهٔ متناسب با هر مرحله را پیشنهاد می‌کند.",
        main_problem="چگونه می‌توان مداخله و پیام تغییر رفتار را با سطح آمادگی واقعی فرد هم‌خوان کرد، بی‌آنکه فرض شود همه در یک نقطه از مسیر تغییر قرار دارند.",
        mechanism="فرد از ناآگاهی یا بی‌قصدی به سنجش سود و زیان و سپس قصد و عمل می‌رسد؛ فرایندهای شناختی و رفتاری در هر مرحله تغییر می‌کنند و تعادل تصمیم و خودکارآمدی، سرعت عبور را تعیین می‌کنند. بازگشت به مرحلهٔ پیشین نیز بخشی از مسیر است.",
        assumptions=[
            "تغییر رفتار فرایندی مرحله‌ای است و نه رویدادی یک‌باره.",
            "مراحل را می‌توان از راه قصد و رفتار سنجید.",
            "فرایندهای مؤثر در هر مرحله متفاوت‌اند.",
            "تعادل تصمیم و خودکارآمدی، پیشرفت را تعیین می‌کنند.",
            "بازگشت، بخشی طبیعی از مسیر تغییر است.",
        ],
        principles=[
            "مداخله باید با مرحلهٔ آمادگی فرد هم‌خوان باشد.",
            "پیام آگاهی‌بخش برای مرحلهٔ پیش‌تفکر و مهارت‌آموزی برای مرحلهٔ عمل مناسب است.",
            "ده فرایند تغییر باید متناسب با مرحله به کار روند.",
            "تعادل تصمیم باید در طراحی پیام لحاظ شود.",
            "خودکارآمدی، شاخص مهم پیشرفت در مراحل پایانی است.",
            "بازگشت را باید بخشی از فرایند و نه شکست کامل دانست.",
        ],
        critiques=[
            "مرزهای مراحل دلبخواهی و دشوار برای سنجش‌اند.",
            "فرض حرکت خطی، پیچیدگی بازگشت و چرخه را کم‌رنگ می‌کند.",
            "شواهد کارایی مداخلات مبتنی بر مدل ناهمگون است.",
            "بافت اجتماعی و اقتصادی در تحلیل جای کافی ندارد.",
            "برخی پژوهش‌ها ساختار پنج‌مرحله‌ای را تأیید نکرده‌اند.",
        ],
        critique_text="منتقدان می‌گویند مدل فرانظری چارچوبی مفید برای تقسیم مخاطب و زمان‌بندی پیام فراهم کرد، اما شواهد تجربی دربارهٔ مرزهای مراحل و برتری آن بر مداخلات ساده یکدست نیست. با این حال، در سیاست سلامت و ارتباطات تغییر رفتار همچنان پرکاربرد است.",
        applications=[
            "طراحی کمپین‌های سلامت و ترک اعتیاد.",
            "تقسیم مخاطب بر پایهٔ آمادگی تغییر در پیام‌رسانی.",
            "آموزش مشاوران و طراحی مداخلهٔ مرحله‌محور.",
            "تحلیل پیام‌های رسانه‌ای سلامت و هم‌خوانی آنها با مرحلهٔ مخاطب.",
            "پژوهش تغییر رفتار در مصرف رسانه و عادت‌های دیجیتال.",
        ],
        example_text="در یک کمپین ترک سیگار، پیام «خطرات سیگار را بشناسید» برای فرد در مرحلهٔ پیش‌تفکر مناسب است، در حالی که برای فرد در مرحلهٔ عمل، آموزش مهارت مقابله با وسوسه اثر بیشتری دارد. مدل فرانظری همین هم‌خوانی پیام و مرحله را اصل طراحی قرار می‌دهد.",
        evolution="مقالهٔ سال ۱۹۸۳ با مطالعهٔ خودتغییری سیگار، مراحل و فرایندها را معرفی کرد و پژوهش‌های بعدی مدل را با تعادل تصمیم، خودکارآمدی و کاربرد در رفتارهای سلامت گوناگون بسط دادند. در دههٔ ۲۰۰۰ نقدهای روش‌شناختی و مرورهای نظام‌مند، محدودیت‌های شواهد را روشن کردند.",
        key_concepts=["مراحل تغییر", "فرایندهای تغییر", "تعادل تصمیم", "خودکارآمدی", "بازگشت", "آمادگی تغییر"],
        theorists="جیمز پروچاسکا و کارلو دی‌کلمنته، سازندگان مدل فرانظری.",
        theorists_text="این مدل در سنت پژوهش روان‌درمانی یکپارچه و سلامت رفتار شکل گرفت و با ارتباطات سلامت پیوند خورد.",
        model="مدل پنج‌مرحله‌ای با فرایندهای متناظر: پیش‌تفکر، تفکر، آماده‌سازی، عمل و حفظ؛ تعادل تصمیم، خودکارآمدی و بازگشت، پویایی حرکت میان مراحل را توضیح می‌دهند.",
        studies=[
            "مقالهٔ سال ۱۹۸۳ مراحل و ده فرایند تغییر را با نمونهٔ بزرگ سیگاری‌ها معرفی کرد.",
            "پژوهش‌های بعدی، مدل را به رفتارهای سلامت دیگر گستردند.",
            "مرورهای نظام‌مند، شواهد کارایی مداخلات مرحله‌محور را ارزیابی کردند.",
            "مطالعات ارتباطات سلامت، هم‌خوانی پیام و مرحله را آزمودند.",
        ],
    ),
}

NAME_FIX = {}

YEAR_FIX = {
    "MC-028": "no year change; note: this MODEL entry overlaps the FRAMEWORK entry MC-572 (Stages of Change); documented here from the 1983 smoking study that formally introduced the stage model, kept as a distinct model-level record",
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
                                       "verified": n_verified, "batch": 129}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH129 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
