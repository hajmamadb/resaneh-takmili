# -*- coding: utf-8 -*-
"""Batch 149 (MODEL): MC-549 Carey culture model, MC-550 Gerbner schematic, MC-554 dependency, MC-566 aggression growth."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch149-model-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch149_model.json"

S = {
    "MC-549": [
        dict(kind="BOOK_CHAPTER",
             title_en="A Cultural Approach to Communication",
             title_fa="رهیافتی فرهنگی به ارتباط",
             authors="Carey, J. W.", year=1989,
             publisher="Unwin Hyman (Communication as Culture)",
             doi=None,
             url="https://web.mit.edu/21l.432/www/readings/Carey_CulturalApproachCommunication.pdf",
             language="en", isbn=None,
             citation="Carey, J. W. (1989). A cultural approach to communication. In Communication as Culture: Essays on Media and Society. Boston: Unwin Hyman.",
             locator="chapter", locator_type="SECTION",
             supports="communication as a symbolic process that constructs shared reality", verified=True),
        dict(kind="WEBSITE",
             title_en="Ritual View of Communication",
             title_fa="دیدگاه آیینی ارتباط",
             authors="EBSCO Research Starters", year=None,
             publisher="EBSCO",
             doi=None,
             url="https://www.ebsco.com/research-starters/communication-and-mass-media/ritual-view-communication",
             language="en", isbn=None,
             citation="EBSCO Research Starters. (n.d.). Ritual view of communication. EBSCO.",
             locator="web page", locator_type="work",
             supports="cultural model's ritual orientation and its contrast with transmission", verified=True),
    ],
    "MC-550": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Toward a General Model of Communication",
             title_fa="به‌سوی مدلی عمومی از ارتباط",
             authors="Gerbner, G.", year=1956,
             publisher="Audio-Visual Communication Review",
             doi="10.1007/BF02717110",
             url="https://link.springer.com/article/10.1007/BF02717110",
             language="en", isbn=None,
             citation="Gerbner, G. (1956). Toward a general model of communication. Audio-Visual Communication Review, 4(3), 171-199.",
             locator="4(3):171-199", locator_type="page_range",
             supports="schematic model linking event, perception, message, media and action", verified=True),
        dict(kind="WEBSITE",
             title_en="Audio Visual Communication Review, Vol. 4, No. 3 (1956)",
             title_fa="مجلهٔ ارتباط دیداری و شنیداری، جلد ۴، شمارهٔ ۳",
             authors="JSTOR", year=1956,
             publisher="JSTOR",
             doi=None,
             url="https://www.jstor.org/stable/i30218419",
             language="en", isbn=None,
             citation="JSTOR. (1956). Audio Visual Communication Review, 4(3), including Gerbner's general model article.",
             locator="issue", locator_type="ISSUE",
             supports="bibliographic confirmation of the article's issue and pagination", verified=True),
    ],
    "MC-554": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="A Dependency Model of Mass-Media Effects",
             title_fa="مدلی وابستگی‌محور از اثرهای رسانه‌های جمعی",
             authors="Ball-Rokeach, S. J.; DeFleur, M. L.", year=1976,
             publisher="Communication Research",
             doi="10.1177/009365027600300101",
             url="https://journals.sagepub.com/doi/10.1177/009365027600300101",
             language="en", isbn=None,
             citation="Ball-Rokeach, S. J., & DeFleur, M. L. (1976). A dependency model of mass-media effects. Communication Research, 3(1), 3-21.",
             locator="3(1):3-21", locator_type="page_range",
             supports="tripartite audience-media-society dependency model", verified=True),
        dict(kind="WEBSITE",
             title_en="A Dependency Model of Mass-Media Effects (record)",
             title_fa="رکورد مدل وابستگی اثرهای رسانه",
             authors="APA PsycNet", year=1976,
             publisher="American Psychological Association",
             doi=None,
             url="https://psycnet.apa.org/record/1976-20455-001",
             language="en", isbn=None,
             citation="APA PsycNet. (1976). Record for A Dependency Model of Mass-Media Effects. American Psychological Association.",
             locator="record", locator_type="work",
             supports="independent bibliographic verification of the 1976 article", verified=True),
    ],
    "MC-566": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Longitudinal Relations Between Children's Exposure to TV Violence and Their Aggressive and Violent Behavior in Young Adulthood",
             title_fa="روابط طولی میان مواجههٔ کودکان با خشونت تلویزیونی و رفتار پرخاشگرانه و خشونت‌آمیز آنان در بزرگسالی",
             authors="Huesmann, L. R.; Moise-Titus, J.; Podolski, C.-L.; Eron, L. D.", year=2003,
             publisher="Developmental Psychology",
             doi=None,
             url="https://www.apa.org/pubs/journals/releases/dev-392201.pdf",
             language="en", isbn=None,
             citation="Huesmann, L. R., Moise-Titus, J., Podolski, C.-L., & Eron, L. D. (2003). Longitudinal relations between children's exposure to TV violence and their aggressive and violent behavior in young adulthood: 1977-1992. Developmental Psychology, 39(2), 201-221.",
             locator="39(2):201-221", locator_type="page_range",
             supports="long-term association between childhood media violence exposure and adult aggression", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Role of Media Violence in Violent Behavior",
             title_fa="نقش خشونت رسانه‌ای در رفتار خشونت‌آمیز",
             authors="Huesmann, L. R.; Taylor, L. D.", year=2006,
             publisher="Annual Review of Public Health",
             doi="10.1146/annurev.publhealth.26.021304.144640",
             url="https://www.annualreviews.org/content/journals/10.1146/annurev.publhealth.26.021304.144640",
             language="en", isbn=None,
             citation="Huesmann, L. R., & Taylor, L. D. (2006). The role of media violence in violent behavior. Annual Review of Public Health, 27, 393-415.",
             locator="27:393-415", locator_type="page_range",
             supports="review of short- and long-term effects of media violence on aggression", verified=True),
    ],
}

ENRICH = {
    "MC-549": dict(
        year=1989,
        summary="مدل ارتباط به‌مثابه فرهنگ، که جیمز کری در کتاب سال ۱۹۸۹ با عنوان ارتباط به‌عنوان فرهنگ صورت‌بندی کرد، رسانه را نه لولهٔ انتقال پیام، بلکه نهادی می‌داند که جهان نمادین را بازمی‌سازد. در این نگرش، ارتباط فرایندی نمادین است که در آن انسان‌ها تجربهٔ مشترک را بازنمایی می‌کنند و واقعیت اجتماعی را می‌سازند. کری میان دو فهم رقیب تمایز گذاشت: فهم انتقالی که ارتباط را جابه‌جایی پیام در فضا برای کنترل می‌داند، و فهم آیینی که ارتباط را مشارکت در فرهنگ مشترک و حفظ جامعه در زمان می‌بیند. مدل او بر این پایه استوار است که رسانه با بازنمایی رویدادها، نه آینهٔ جهان، بلکه سازندهٔ نسخه‌ای نمادین از آن است. خبر، سرگرمی و تبلیغ در این چارچوب آیین‌هایی هستند که نظم اجتماعی و مرزهای فرهنگی را بازتولید می‌کنند. کری همچنین فناوری ارتباطی را خود شکل فرهنگی می‌دانست، نه ابزاری بی‌طرف. نقدهای اصلی به مدل، آرمانی‌کردن فرهنگ مشترک، کم‌توجهی به نابرابری قدرت، ابهام روش تجربی و دشواری سنجش بازسازی جهان نمادین را برجسته می‌کنند. برای پژوهش امروز، مدل کری یادآوری می‌کند که پیش از سنجش اثر پیام، باید پرسید رسانه چه نسخه‌ای از جهان را طبیعی و بدیهی جلوه می‌دهد.",
        definition="مدل ارتباط به‌مثابه فرهنگ، رسانه را سازندهٔ جهان نمادین و ارتباط را مشارکت در فرهنگ مشترک می‌داند؛ پیام منتقل نمی‌شود، بلکه واقعیت اجتماعی بازسازی و بازنمایی می‌شود.",
        main_problem="اگر رسانه آینهٔ جهان نیست، چگونه با بازنمایی نمادین، واقعیت اجتماعی و نظم فرهنگی را می‌سازد و پژوهش ارتباط چگونه باید این فرایند را تحلیل کند.",
        mechanism="رسانه رویداد را گزینش و در قالب نمادین بازنمایی می‌کند؛ مخاطب در آیین‌های مشترک رسانه‌ای مشارکت می‌کند و از این راه معنای مشترک، مرزهای فرهنگی و نظم اجتماعی بازتولید می‌شود.",
        assumptions=[
            "ارتباط فرایندی نمادین است.",
            "رسانه واقعیت را بازسازی می‌کند.",
            "فرهنگ مشترک از ارتباط می‌زاید.",
            "فناوری ارتباطی شکل فرهنگی است.",
            "آیین رسانه‌ای نظم را بازتولید می‌کند.",
            "معنا در مشارکت مخاطب ساخته می‌شود.",
        ],
        principles=[
            "رسانه را سازندهٔ جهان نمادین ببین.",
            "بازنمایی را از آینه‌بودن جدا کن.",
            "آیین رسانه‌ای را در تحلیل بگنجان.",
            "معنای مشترک را با شواهد مستند کن.",
            "فناوری را شکل فرهنگی بخوان.",
            "نابرابری قدرت را در بازنمایی بسنج.",
            "آیین را از سرگرمی ساده جدا کن.",
            "زبان و روایت را در تحلیل بگنجان.",
        ],
        critiques=[
            "فرهنگ مشترک را آرمانی می‌کند.",
            "نابرابری قدرت را کم‌می‌شمارد.",
            "روش تجربی آن مبهم است.",
            "سنجش بازسازی نمادین دشوار است.",
            "مرز مدل و نظریهٔ فرهنگی روشن نیست.",
            "نقش اقتصاد رسانه را کم‌رنگ می‌کند.",
            "تعمیم میان‌فرهنگی آن محدود است.",
        ],
        critique_text="منتقدان می‌گویند مدل کری پژوهش رسانه را از تنگنای انتقال بیرون آورد اما فرهنگ مشترک را آرمانی کرد و معیار تجربی روشنی نداد؛ با این حال، چارچوب پایهٔ مطالعات فرهنگی رسانه است. دفاع کری آن است که رسانه پیش از هر اثر، جهان معنادار را برای ما قابل سکونت می‌کند و همین کارکرد نمادین باید موضوع اصلی پژوهش باشد.",
        applications=[
            "تحلیل بازنمایی خبر.",
            "مطالعهٔ آیین رسانه‌ای.",
            "پژوهش هویت فرهنگی.",
            "نقد رویکرد انتقالی.",
            "تحلیل تبلیغ به‌عنوان آیین مصرف.",
            "پژوهش حافظهٔ جمعی.",
            "تحلیل گردشگری و روایت ملی.",
            "پژوهش موزه و نمایشگاه فرهنگی.",
        ],
        example_text="پخش سالانهٔ یک مراسم ملی، اطلاعات تازه‌ای منتقل نمی‌کند، اما مخاطبان را در تجربه‌ای نمادین و مشترک جای می‌دهد؛ بازنمایی رسانه‌ای همان مراسم، حافظهٔ جمعی و مرزهای فرهنگی را بازمی‌سازد.",
        evolution="کتاب سال ۱۹۸۹ کری مدل فرهنگی ارتباط را تثبیت کرد و به مرجع مطالعات فرهنگی رسانه تبدیل شد. پژوهش‌های بعدی، آن را در رسانه‌های دیجیتال، حافظهٔ جمعی و آیین‌های آنلاین به کار گرفتند.",
        key_concepts=["ارتباط به‌مثابه فرهنگ", "جهان نمادین", "آیین", "بازنمایی", "فرهنگ مشترک", "حافظهٔ جمعی"],
        theorists="جیمز کری.",
        theorists_text="مدل در سنت مطالعات فرهنگی و جامعه‌شناسی رسانه شکل گرفت.",
        model="رسانه به‌عنوان سازندهٔ جهان نمادین؛ ارتباط آیینی که فرهنگ مشترک و نظم اجتماعی را بازسازی می‌کند.",
        studies=[
            "کتاب سال ۱۹۸۹ مدل فرهنگی را تثبیت کرد.",
            "مطالعات خبر، بازنمایی را تحلیل کرد.",
            "پژوهش حافظه، آیین رسانه‌ای را سنجید.",
            "مطالعات دیجیتال، فرهنگ مشترک آنلاین را بررسی کرد.",
            "پژوهش روایت ملی، بازسازی نمادین را نشان داد.",
        ],
    ),
    "MC-550": dict(
        year=1956,
        summary="مدل شماتیک گربر، که جورج گربر در مقالهٔ سال ۱۹۵۶ با عنوان به‌سوی مدلی عمومی از ارتباط ارائه کرد، ارتباط را زنجیره‌ای از ادراک و تولید می‌داند که در آن رویداد، ادراک، پیام، رسانه، ادراک و عمل به هم پیوند می‌خورند. گربر کوشید مدلی بسازد که هم ارتباط میان‌فردی و هم ارتباط جمعی را دربرگیرد. در این مدل، رویدادی در جهان رخ می‌دهد؛ ادراک‌کننده آن را گزینش و تفسیر می‌کند؛ سپس پیام ساخته می‌شود و از رسانه می‌گذرد؛ گیرنده پیام را ادراک می‌کند و بر پایهٔ آن عمل می‌کند. گربر دو بُعد را در مدل برجسته کرد: بُعد افقی که زنجیرهٔ ادراک تا عمل را نشان می‌دهد، و بُعد عمودی که دسترسی، کنترل و بافت اجتماعی را در هر مرحله وارد می‌کند. او تأکید کرد که ادراک و تولید، فرایندی فعال و گزینشی‌اند و پیام، بازنمایی رویداد است، نه خود رویداد. این مدل زمینهٔ پژوهش‌های بعدی گربر در تحلیل کاشت و سیاست رسانه شد. نقدهای اصلی به آن، پیچیدگی و دشواری آزمون، تمرکز بر فرایند ادراک فردی، کم‌توجهی به ساخت قدرت و اقتصاد رسانه و ابهام نسبت میان سطوح مدل را برجسته می‌کنند. با این حال، چارچوب او نشان داد که خبر، بازتاب سادهٔ رویداد نیست و در هر گام از زنجیره، دسترسی و کنترل سازمانی آن را دگرگون می‌کند.",
        definition="مدل شماتیک گربر، ارتباط را زنجیرهٔ رویداد، ادراک، تولید پیام، رسانه، ادراک گیرنده و عمل می‌داند که در هر مرحله با دسترسی، کنترل و بافت اجتماعی قید می‌خورد.",
        main_problem="رویداد جهان چگونه به پیام رسانه‌ای و سپس به ادراک و عمل گیرنده تبدیل می‌شود و دسترسی و کنترل در هر مرحله چه نقشی دارند.",
        mechanism="ادراک‌کننده رویداد را گزینش و تفسیر می‌کند، پیام را می‌سازد و از رسانه می‌گذراند؛ گیرنده پیام را ادراک می‌کند و عمل او بازخوردی به زنجیره می‌دهد؛ بُعد عمودی دسترسی و کنترل را در هر مرحله وارد می‌کند.",
        assumptions=[
            "ارتباط زنجیرهٔ ادراک و تولید است.",
            "پیام بازنمایی رویداد است، نه خود آن.",
            "ادراک فرایندی گزینشی است.",
            "دسترسی و کنترل در هر مرحله اثر دارند.",
            "مدل میان‌فردی و جمعی را دربرمی‌گیرد.",
        ],
        principles=[
            "رویداد را از بازنمایی آن جدا کن.",
            "گزینش ادراکی را در هر مرحله نشان بده.",
            "دسترسی و کنترل را در مدل بگنجان.",
            "بافت اجتماعی را در هر گره وارد کن.",
            "بازخورد عمل را به زنجیره پیوند بده.",
            "پیام را محصول تولید فعال بدان.",
            "هر گره را با شواهد جداگانه بسنج.",
        ],
        critiques=[
            "مدل را برای آزمون تجربی پیچیده می‌کند.",
            "بر ادراک فردی متمرکز است.",
            "ساخت قدرت و اقتصاد رسانه را کم‌می‌شمارد.",
            "نسبت سطوح مدل مبهم است.",
            "نقش مخاطب فعال را کامل توضیح نمی‌دهد.",
            "مرز میان سطوح تحلیل روشن نیست.",
        ],
        critique_text="منتقدان می‌گویند مدل شماتیک گربر پیوند ادراک، تولید و بافت را به‌خوبی نشان داد اما پیچیدگی آن آزمون را دشوار کرد و ساخت قدرت را کم‌بررسی گذاشت؛ با این حال، پایهٔ پژوهش کاشت و تحلیل سیاست رسانه شد. ارزش پایدار مدل در آن است که نشان می‌دهد هیچ پیامی بی‌واسطه به مخاطب نمی‌رسد و در هر گام، گزینش و کنترل شکل آن را دگرگون می‌کند.",
        applications=[
            "تحلیل زنجیرهٔ تولید خبر.",
            "آموزش مدل‌های ارتباط.",
            "پژوهش ادراک مخاطب.",
            "تحلیل دسترسی به رسانه.",
            "مطالعهٔ بازنمایی رویداد.",
            "تحلیل کنترل سیاسی رسانه.",
        ],
        example_text="زمین‌لرزه‌ای رخ می‌دهد؛ خبرنگار آن را گزینش و تفسیر می‌کند، گزارش را می‌سازد، شبکه پخش می‌کند و مخاطب بر پایهٔ ادراک خود واکنش نشان می‌دهد. در هر گره، دسترسی به اطلاعات و کنترل سازمانی، شکل پیام را تغییر می‌دهد.",
        evolution="مقالهٔ سال ۱۹۵۶ گربر مدل شماتیک را معرفی کرد و زمینهٔ نظریهٔ کاشت شد. پژوهش‌های بعدی، مدل را در تحلیل خبر، سیاست رسانه و ادراک مخاطب به کار گرفتند.",
        key_concepts=["رویداد", "ادراک", "تولید پیام", "دسترسی", "کنترل", "بازنمایی"],
        theorists="جورج گربر.",
        theorists_text="مدل در سنت پژوهش ارتباط جمعی و ادراک رسانه شکل گرفت.",
        model="زنجیرهٔ رویداد، ادراک، تولید، رسانه، ادراک و عمل که با بُعد دسترسی و کنترل در هر مرحله قید می‌خورد.",
        studies=[
            "مقالهٔ سال ۱۹۵۶ مدل شماتیک را معرفی کرد.",
            "پژوهش کاشت، مدل را گسترد.",
            "مطالعات خبر، گزینش ادراکی را سنجیدند.",
            "پژوهش سیاست، کنترل رسانه را تحلیل کرد.",
            "تحلیل تطبیقی، مدل را در کشورهای مختلف آزمود.",
        ],
    ),
    "MC-554": dict(
        year=1976,
        summary="مدل وابستگی رسانه–مخاطب، که ساندرا بال-روکیچ و ملوین دی‌فلور در مقالهٔ سال ۱۹۷۶ با عنوان مدلی وابستگی‌محور از اثرهای رسانه‌های جمعی ارائه کردند، اثر رسانه را نه محصول قدرت پیام، بلکه محصول رابطهٔ وابستگی میان مخاطب، رسانه و جامعه می‌داند. در این مدل، مخاطب برای برآوردن نیازهای خود به منابع رسانه‌ای وابسته می‌شود؛ این نیازها شامل فهم و شناخت جهان، جهت‌گیری برای عمل و تعامل، و سرگرمی است. شدت وابستگی به دو شرط بستگی دارد: میزان بی‌ثباتی ساختاری جامعه و شمار منابع جایگزین اطلاعات. هرچه جامعه ناپایدارتر و منابع جایگزین کمتر باشد، وابستگی به رسانه بیشتر و اثر رسانه قوی‌تر می‌شود. بال-روکیچ و دی‌فلور اثرها را در سه سطح شناختی، عاطفی و رفتاری دسته‌بندی کردند و نشان دادند که رسانه در بستر رابطهٔ سه‌گانهٔ مخاطب، رسانه و جامعه اثر می‌گذارد. نقدهای اصلی به مدل، ابهام سنجش وابستگی، دشواری تفکیک آن از استفاده و رضایت، کم‌توجهی به قدرت رسانه در تعریف نیازها و آزمون‌پذیری محدود در محیط چندرسانه‌ای را برجسته می‌کنند. با این حال، مدل نشان می‌دهد که اثر رسانه را نمی‌توان جدا از بستر اجتماعی و گزینه‌های اطلاعاتی موجود ارزیابی کرد.",
        definition="مدل وابستگی رسانه–مخاطب، اثر رسانه را محصول رابطهٔ سه‌گانهٔ مخاطب، رسانه و جامعه می‌داند که در آن نیازهای مخاطب و میزان بی‌ثباتی ساختاری، شدت وابستگی و اثر را تعیین می‌کند.",
        main_problem="چرا اثر رسانه در برخی شرایط اجتماعی قوی‌تر و در برخی ضعیف‌تر است و رابطهٔ وابستگی میان مخاطب، رسانه و جامعه چگونه این تفاوت را توضیح می‌دهد.",
        mechanism="مخاطب برای فهم، جهت‌گیری و سرگرمی به رسانه وابسته می‌شود؛ هرچه بی‌ثباتی ساختاری بیشتر و منابع جایگزین کمتر باشد، وابستگی شدیدتر و اثر رسانه در سطوح شناختی، عاطفی و رفتاری قوی‌تر می‌شود.",
        assumptions=[
            "اثر رسانه رابطه‌محور است، نه پیام‌محور.",
            "مخاطب برای نیازها به رسانه وابسته است.",
            "بی‌ثباتی ساختاری وابستگی را افزایش می‌دهد.",
            "منابع جایگزین، وابستگی را کاهش می‌دهند.",
            "اثر در سه سطح شناختی، عاطفی و رفتاری رخ می‌دهد.",
        ],
        principles=[
            "رابطهٔ سه‌گانه را واحد تحلیل بگیر.",
            "نیازهای مخاطب را مشخص کن.",
            "بی‌ثباتی ساختاری را بسنج.",
            "منابع جایگزین را در مدل بگنجان.",
            "سه سطح اثر را جدا تحلیل کن.",
            "وابستگی را از استفادهٔ ساده تفکیک کن.",
            "بحران را موقعیت طبیعی آزمون بگیر.",
            "سطح شناختی را از عاطفی جدا بسنج.",
        ],
        critiques=[
            "سنجش وابستگی مبهم است.",
            "تفکیک آن از استفاده و رضایت دشوار است.",
            "قدرت رسانه در تعریف نیازها را کم‌می‌شمارد.",
            "آزمون آن در محیط چندرسانه‌ای محدود است.",
            "نقش محتوای پیام را کم‌رنگ می‌کند.",
            "وابستگی را به‌سادگی به اثر فرو می‌کاهد.",
            "اثر بلندمدت را از اثر کوتاه‌مدت جدا نمی‌کند.",
        ],
        critique_text="منتقدان می‌گویند مدل وابستگی چارچوبی رابطه‌محور برای تبیین تفاوت اثر رسانه فراهم کرد اما سنجش وابستگی و تفکیک آن از استفاده دشوار ماند؛ با این حال، پایهٔ نظریهٔ وابستگی نظام رسانه‌ای است. امروز این مدل دوباره اهمیت یافته است، زیرا الگوریتم‌های توصیه‌گر وابستگی مخاطب به یک منبع اطلاعاتی را تشدید می‌کنند و دسترسی به منابع جایگزین را کاهش می‌دهند.",
        applications=[
            "تحلیل اثر رسانه در بحران.",
            "پژوهش وابستگی در انتخابات.",
            "مطالعهٔ رسانه و بی‌ثباتی اجتماعی.",
            "برنامه‌ریزی رسانهٔ عمومی.",
            "تحلیل وابستگی در رسانه‌های دیجیتال.",
            "سنجش وابستگی در جامعهٔ چندرسانه‌ای.",
            "تحلیل اثر رسانه در همه‌گیری اطلاعاتی.",
        ],
        example_text="در بحران طبیعی، مردم به‌سرعت به رسانهٔ رسمی و شبکه‌های اجتماعی وابسته می‌شوند، زیرا منابع جایگزین کم و جامعه بی‌ثبات است؛ همان رسانه در شرایط عادی اثر کمتری دارد، چون منابع متعدد و ساختار پایدار است.",
        evolution="مقالهٔ سال ۱۹۷۶ بال-روکیچ و دی‌فلور مدل وابستگی را معرفی کرد و به نظریهٔ وابستگی نظام رسانه‌ای گسترش یافت. پژوهش‌های بعدی، آن را در بحران‌ها و رسانه‌های دیجیتال آزمودند.",
        key_concepts=["وابستگی", "رابطهٔ سه‌گانه", "بی‌ثباتی ساختاری", "منابع جایگزین", "نیاز شناختی", "اثر رسانه"],
        theorists="ساندرا بال-روکیچ و ملوین دی‌فلور.",
        theorists_text="مدل در سنت پژوهش اثر رسانه و جامعه‌شناسی ارتباط شکل گرفت.",
        model="رابطهٔ وابستگی سه‌گانهٔ مخاطب، رسانه و جامعه که شدت اثر رسانه را با بی‌ثباتی ساختاری و منابع جایگزین تعیین می‌کند.",
        studies=[
            "مقالهٔ سال ۱۹۷۶ مدل را معرفی کرد.",
            "پژوهش بحران، وابستگی را سنجید.",
            "مطالعات انتخاباتی، اثر وابستگی را آزمودند.",
            "پژوهش دیجیتال، منابع جایگزین را تحلیل کرد.",
            "مطالعهٔ بحران، وابستگی نهادی را سنجید.",
        ],
    ),
    "MC-566": dict(
        year=2003,
        summary="فرضیهٔ رشد پرخاشگری رسانه‌ای، که در کارت با عنوان کوتاه پرخاشگری–رشد ثبت شده است، ادعا می‌کند مواجههٔ درازمدت با خشونت رسانه‌ای، رفتار پرخاشگرانه را در طول زمان افزایش می‌دهد. برخلاف فرضیه‌های کوتاه‌مدت که بر تحریک آنی تمرکز دارند، این فرضیه بر انباشت اثر در سال‌ها تأکید می‌کند. پژوهش طولی سال ۲۰۰۳ هوسمن و همکاران، مواجههٔ کودکان با خشونت تلویزیونی را با رفتار پرخاشگرانهٔ آنان در بزرگسالی، حدود پانزده سال بعد، پیوند داد و نشان داد که این رابطه پس از کنترل متغیرهای زمینه‌ای پایدار می‌ماند. مرور سال ۲۰۰۶ هوسمن و تیلور نیز شواهد کوتاه‌مدت و درازمدت را جمع‌بندی کرد. سازوکارهای پیشنهادی شامل یادگیری مشاهده‌ای، شکل‌گیری طرحواره‌های شناختی پرخاشگری، حساسیت‌زدایی و کاهش همدلی است. این فرضیه در سیاست‌گذاری رسانه و سلامت عمومی به کار رفت. نقدهای اصلی به آن، دشواری اثبات علیت، اندازهٔ کوچک اثر، نقش عوامل مداخله‌گر خانوادگی و اجتماعی، سوگیری انتشار و تفاوت‌های فرهنگی در تفسیر یافته‌ها را برجسته می‌کنند. با این حال، این فرضیه بحث دربارهٔ مسئولیت رسانه و خانواده را از سطح نگرانی اخلاقی به سطح شواهد طولی و سیاست سلامت عمومی ارتقا داد.",
        definition="فرضیهٔ رشد پرخاشگری رسانه‌ای می‌گوید مواجههٔ مکرر و درازمدت با خشونت رسانه‌ای، با سازوکارهای یادگیری و طرحواره‌سازی، رفتار پرخاشگرانه را در گذر سال‌ها افزایش می‌دهد.",
        main_problem="آیا مواجههٔ درازمدت با خشونت رسانه‌ای به رشد رفتار پرخاشگرانه در سال‌های بعد می‌انجامد و این رابطه تا چه اندازه علی و تعمیم‌پذیر است.",
        mechanism="مواجههٔ مکرر با خشونت، طرحواره‌های شناختی پرخاشگری را تقویت می‌کند، حساسیت به قربانی را کاهش می‌دهد و رفتار پرخاشگرانه را در موقعیت‌های بعدی محتمل‌تر می‌سازد.",
        assumptions=[
            "اثر رسانه می‌تواند انباشتی باشد.",
            "یادگیری مشاهده‌ای رفتار را شکل می‌دهد.",
            "طرحواره‌های شناختی در زمان تثبیت می‌شوند.",
            "حساسیت‌زدایی، مهار اخلاقی را کاهش می‌دهد.",
            "رابطه پس از کنترل زمینه پایدار می‌ماند.",
        ],
        principles=[
            "مواجهه را در بازهٔ طولی بسنج.",
            "متغیرهای زمینه‌ای را کنترل کن.",
            "سازوکار یادگیری را مستند کن.",
            "اندازهٔ اثر را واقع‌بینانه گزارش کن.",
            "تفاوت فرهنگی را در تفسیر بگنجان.",
            "علیت را با شواهد چندگانه بسنج.",
            "سازوکار جایگزین را نیز بررسی کن.",
        ],
        critiques=[
            "اثبات علیت دشوار است.",
            "اندازهٔ اثر کوچک و مورد مناقشه است.",
            "عوامل خانوادگی و اجتماعی مداخله می‌کنند.",
            "سوگیری انتشار یافته‌ها را تهدید می‌کند.",
            "تعمیم میان‌فرهنگی محدود است.",
            "رفتار پرخاشگرانه را با گزارش خودسنجی می‌سنجد.",
            "نقش محتوای خشونت را یکدست فرض می‌کند.",
            "شدت و نوع خشونت را از هم تفکیک نمی‌کند.",
            "سنجش مواجهه را به گزارش کودک محدود می‌کند.",
            "اثر همسالان را در مدل کم‌رنگ می‌بیند.",
            "سازوکار عصب‌شناختی آن کم‌آزموده مانده است.",
        ],
        critique_text="منتقدان می‌گویند فرضیهٔ رشد پرخاشگری رابطهٔ طولی مهمی را نشان داد اما به‌سختی علیت را اثبات می‌کند و عوامل خانوادگی و فرهنگی را کم‌بررسی می‌گذارد؛ با این حال، پژوهش درازمدت خشونت رسانه‌ای را به بحث سلامت عمومی کشاند. داوری منصفانه آن است که این فرضیه بخشی از مجموعهٔ شواهد است، نه اثبات یک علت یگانه، و باید در کنار مطالعات خانواده، مدرسه و همسالان خوانده شود.",
        applications=[
            "سیاست‌گذاری خشونت رسانه‌ای.",
            "آموزش سواد رسانه‌ای به خانواده.",
            "پژوهش طولی مخاطب کودک.",
            "طراحی رتبه‌بندی محتوا.",
            "مطالعهٔ سلامت عمومی.",
            "طراحی مداخلهٔ مدرسه‌ای.",
            "ارزیابی سیاست رتبه‌بندی سنی.",
            "آموزش والدین در سواد رسانه‌ای.",
            "مطالعهٔ بازی‌های رایانه‌ای و پرخاشگری.",
        ],
        example_text="کودکی که سال‌ها برنامه‌های پرخشونت تماشا می‌کند، ممکن است در نوجوانی در موقعیت تعارض، پاسخ پرخاشگرانه را آسان‌تر انتخاب کند؛ اما خانواده، مدرسه و گروه همسالان نیز در همین مسیر اثر دارند.",
        evolution="پژوهش طولی سال ۲۰۰۳ و مرور سال ۲۰۰۶ شواهد اصلی این فرضیه را تثبیت کردند و بحث سلامت عمومی را گستردند. پژوهش‌های بعدی، نقش عوامل زمینه‌ای و تفاوت‌های فرهنگی را برجسته‌تر کردند.",
        key_concepts=["رشد پرخاشگری", "مواجههٔ درازمدت", "یادگیری مشاهده‌ای", "طرحوارهٔ شناختی", "حساسیت‌زدایی", "خشونت رسانه‌ای"],
        theorists="لئونارد هوسمن و همکاران.",
        theorists_text="فرضیه در سنت پژوهش اثر خشونت رسانه‌ای و روان‌شناسی رشد شکل گرفت.",
        model="مواجههٔ انباشتی با خشونت رسانه‌ای که با یادگیری و طرحواره‌سازی، احتمال رفتار پرخاشگرانه را در سال‌های بعد افزایش می‌دهد.",
        studies=[
            "پژوهش طولی سال ۲۰۰۳ رابطهٔ پانزده‌ساله را نشان داد.",
            "مرور سال ۲۰۰۶ شواهد کوتاه و درازمدت را جمع‌بندی کرد.",
            "مطالعات خانواده، عوامل مداخله‌گر را سنجیدند.",
            "پژوهش میان‌فرهنگی، تعمیم‌پذیری را بررسی کرد.",
            "مطالعهٔ رسانهٔ تعاملی، مواجهه را دوباره سنجید.",
        ],
    ),
}

NAME_FIX = {
    "MC-566": ("فرضیهٔ رشد پرخاشگری رسانه‌ای", "Media Violence and Aggression Growth Hypothesis", "عنوان پیشین «پرخاشگری–رشد» کوتاه و مبهم بود و سال و نظریه‌پرداز کارت خالی مانده بود؛ نام گویا و انتساب مستند ثبت شد."),
}
YEAR_FIX = {
    "MC-549": "کارت مدل ارتباط به‌مثابه فرهنگ، نسخهٔ مدلی همان چارچوب فرهنگی کری است و سال ۱۹۸۹ با انتشار کتاب هم‌خوان است.",
    "MC-566": "سال کارت خالی بود؛ سال ۲۰۰۳ به‌عنوان نقطهٔ شاهد اصلی پژوهش طولی ثبت شد، در حالی که خود فرضیه در سنت پژوهش خشونت رسانه‌ای پیش‌تر شکل گرفته بود.",
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
                                       "verified": n_verified, "batch": 149}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH149 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
