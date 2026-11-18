# -*- coding: utf-8 -*-
"""Batch 143 (MODEL): full documentation for MC-462, MC-463, MC-464, MC-465."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch143-model-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch143_model.json"

S = {
    "MC-462": [
        dict(kind="BOOK_CHAPTER",
             title_en="How Communication Works",
             title_fa="ارتباط چگونه کار می‌کند",
             authors="Schramm, W.", year=1954,
             publisher="University of Illinois Press (The Process and Effects of Mass Communication)",
             doi=None,
             url="https://search-library.ucsd.edu/discovery/fulldisplay/alma991015712739706535/01UCS_SDI:UCSD",
             language="en", isbn=None,
             citation="Schramm, W. (1954). How communication works. In W. Schramm (Ed.), The Process and Effects of Mass Communication (pp. 3-26). Urbana: University of Illinois Press.",
             locator="pp. 3-26", locator_type="page_range",
             supports="loop model in which participants encode, interpret and decode within overlapping fields of experience", verified=True),
        dict(kind="BOOK_CHAPTER",
             title_en="How Communication Works (revised edition)",
             title_fa="ارتباط چگونه کار می‌کند (ویراست بازنگری‌شده)",
             authors="Schramm, W.; Roberts, D. F. (eds.)", year=1971,
             publisher="University of Illinois Press",
             doi=None,
             url="https://www.worldradiohistory.com/BOOKSHELF-ARH/Education/The-Process-and-Effects-of-Mass-Communications-Schramm-1971.pdf",
             language="en", isbn=None,
             citation="Schramm, W. (1971). How communication works. In W. Schramm & D. F. Roberts (Eds.), The Process and Effects of Mass Communication (rev. ed., pp. 3-26). Urbana: University of Illinois Press.",
             locator="pp. 3-26", locator_type="page_range",
             supports="revised loop diagram and its mass communication extension", verified=True),
    ],
    "MC-463": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="An Approach to the Study of Communicative Acts",
             title_fa="رهیافتی به مطالعهٔ کنش‌های ارتباطی",
             authors="Newcomb, T. M.", year=1953,
             publisher="Psychological Review",
             doi="10.1037/h0063098",
             url="https://psycnet.apa.org/record/1954-05963-001",
             language="en", isbn=None,
             citation="Newcomb, T. M. (1953). An approach to the study of communicative acts. Psychological Review, 60(6), 393-404.",
             locator="60(6):393-404", locator_type="page_range",
             supports="ABX model of orientation among two persons and a shared object", verified=True),
        dict(kind="OTHER",
             title_en="Coorientation Theory (Encyclopedia of Communication Theory entry)",
             title_fa="نظریهٔ هم‌جهت‌گیری (مدخل دانشنامهٔ نظریهٔ ارتباطات)",
             authors="SAGE Publications", year=2009,
             publisher="SAGE Encyclopedia of Communication Theory",
             doi=None,
             url="https://sk.sagepub.com/ency/edvol/download/communicationtheory/chpt/coorientation-theory.pdf",
             language="en", isbn=None,
             citation="SAGE Publications. (2009). Coorientation theory. In Encyclopedia of Communication Theory. Thousand Oaks: SAGE.",
             locator="entry", locator_type="SECTION",
             supports="overview of coorientation research built on the ABX formulation", verified=True),
    ],
    "MC-464": [
        dict(kind="BOOK",
             title_en="The Process of Communication: An Introduction to Theory and Practice",
             title_fa="فرایند ارتباط: درآمدی بر نظریه و عمل",
             authors="Berlo, D. K.", year=1960,
             publisher="Holt, Rinehart and Winston",
             doi=None,
             url="https://archive.org/details/processofcommuni0000berl",
             language="en", isbn="9780030556869",
             citation="Berlo, D. K. (1960). The Process of Communication: An Introduction to Theory and Practice. New York: Holt, Rinehart and Winston.",
             locator="book", locator_type="SECTION",
             supports="source-message-channel-receiver model with skills, attitudes, knowledge, social system and culture", verified=True),
        dict(kind="BOOK",
             title_en="The Process of Communication (1967 printing record)",
             title_fa="فرایند ارتباط (نسخهٔ چاپ ۱۹۶۷)",
             authors="Berlo, D. K.", year=1960,
             publisher="Holt, Rinehart and Winston",
             doi=None,
             url="https://openlibrary.org/books/OL19944064M/The_process_of_communication",
             language="en", isbn=None,
             citation="Berlo, D. K. (1960). The Process of Communication: An Introduction to Theory and Practice. New York: Holt, Rinehart and Winston. (1967 printing, Open Library record OL19944064M)",
             locator="book", locator_type="SECTION",
             supports="bibliographic record of the model's source volume", verified=True),
    ],
    "MC-465": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Toward a General Model of Communication",
             title_fa="به سوی مدلی عمومی از ارتباط",
             authors="Gerbner, G.", year=1956,
             publisher="Audio-Visual Communication Review",
             doi="10.1007/BF02717110",
             url="https://link.springer.com/article/10.1007/BF02717110",
             language="en", isbn=None,
             citation="Gerbner, G. (1956). Toward a general model of communication. Audio-Visual Communication Review, 4(3), 171-199.",
             locator="4(3):171-199", locator_type="page_range",
             supports="perceptual model with selection, context and availability shaping the message", verified=True),
        dict(kind="BOOK_CHAPTER",
             title_en="Mass Media and Human Communication Theory",
             title_fa="رسانه‌های جمعی و نظریهٔ ارتباط انسانی",
             authors="Gerbner, G.", year=1967,
             publisher="Holt, Rinehart and Winston (Human Communication Theory)",
             doi=None, url=None, language="en", isbn=None,
             citation="Gerbner, G. (1967). Mass media and human communication theory. In F. E. X. Dance (Ed.), Human Communication Theory. New York: Holt, Rinehart and Winston.",
             locator="chapter", locator_type="SECTION",
             supports="mass communication elaboration of the perceptual model", verified=False),
    ],
}

ENRICH = {
    "MC-462": dict(
        year=1954,
        summary="مدل حلقه‌ای شرام، که ویلفرد شرام در فصل «ارتباط چگونه کار می‌کند» در کتاب فرایند و اثرهای ارتباط جمعی در سال ۱۹۵۴ ارائه کرد، نخستین بازنگری جدی در مدل خطی شانون و ویور است. در این مدل، ارتباط انتقال یک‌سویهٔ پیام نیست، بلکه فرایندی حلقه‌ای و متقابل است که در آن فرستنده و گیرنده هم‌زمان رمزگذاری و رمزگشایی می‌کنند. هر طرف پیش از تفسیر پیام، آن را با میدان تجربهٔ خود می‌سنجد؛ میدان تجربه مجموعهٔ دانش، فرهنگ، نگرش‌ها و تجربه‌های زیستهٔ فرد است. هرچه دو میدان تجربه هم‌پوشانی بیشتری داشته باشند، احتمال فهم مشترک بیشتر می‌شود. پیام در میانهٔ حلقه جای دارد و بازخورد، مسیر بازگشت تفسیر گیرنده به فرستنده را می‌سازد. شرام سپس همین حلقه را برای ارتباط جمعی گسترش داد: سازمان رسانه‌ای با چند رمزگذار پیام را به مخاطبان بسیار می‌فرستد و بازخورد کند و غیرمستقیم است. این مدل نقطهٔ گذار از تلقی مکانیکی به تلقی تفسیری ارتباط بود و زمینهٔ مدل‌های تعاملی بعدی را فراهم کرد. نقدهای اصلی به آن، فرض هم‌پوشانی کافی میدان‌های تجربه، آرمانی‌بودن بازخورد، کم‌توجهی به قدرت و نابرابری، تمرکز بر ارتباط دو نفره و ساده‌سازی بافت اجتماعی را برجسته می‌کنند.",
        definition="مدل حلقه‌ای شرام، ارتباط را فرایندی چرخه‌ای و متقابل می‌داند که در آن دو طرف با تکیه بر میدان تجربه، هم‌زمان پیام را رمزگذاری، تفسیر و رمزگشایی می‌کنند و بازخورد حلقه را می‌بندد.",
        main_problem="چگونه می‌توان ارتباط را به‌جای انتقال یک‌سویهٔ پیام، فرایندی متقابل و تفسیری فهمید که در آن معنا در تعامل دو طرف شکل می‌گیرد.",
        mechanism="فرستنده پیام را رمزگذاری می‌کند، گیرنده آن را رمزگشایی و با میدان تجربهٔ خود تفسیر می‌کند و پاسخ خود را به‌صورت بازخورد بازمی‌فرستد؛ هم‌زمانی رمزگذاری و رمزگشایی حلقه را پیوسته نگه می‌دارد و هم‌پوشانی میدان‌های تجربه فهم مشترک را ممکن می‌سازد.",
        assumptions=[
            "ارتباط فرایندی چرخه‌ای و متقابل است.",
            "معنا در تفسیر گیرنده شکل می‌گیرد.",
            "میدان تجربهٔ مشترک پیش‌شرط فهم است.",
            "فرستنده و گیرنده هم‌زمان فعال‌اند.",
            "بازخورد حلقهٔ ارتباط را می‌بندد.",
        ],
        principles=[
            "میدان تجربهٔ مخاطب را بشناس.",
            "پیام را با زبان مشترک رمزگذاری کن.",
            "بازخورد را جدی بگیر و حلقه را باز نگه دار.",
            "نقش تفسیر گیرنده را در طراحی پیام لحاظ کن.",
            "هم‌زمانی فرستادن و دریافت را در نظر بگیر.",
            "هم‌پوشانی تجربه را با مثال و زمینه بساز.",
        ],
        critiques=[
            "فرض هم‌پوشانی کافی میدان‌های تجربه ساده‌ساز است.",
            "بازخورد را آرمانی و بی‌اصطکاک تصویر می‌کند.",
            "نابرابری قدرت و دسترسی را نادیده می‌گیرد.",
            "بر ارتباط دو نفره متمرکز و بافت اجتماعی را کم‌بررسی می‌گذارد.",
            "مرز رمزگذاری و تفسیر را در عمل مبهم می‌کند.",
        ],
        critique_text="منتقدان می‌گویند مدل حلقه‌ای گامی مهم از انتقال به تعامل بود اما هم‌پوشانی میدان تجربه را بیش از واقع فرض می‌کند و بازخورد را بدون اصطکاک قدرت و سازمان نشان می‌دهد؛ با این حال، چارچوب پایهٔ آموزش ارتباط متقابل و روابط عمومی دوسویه شد.",
        applications=[
            "آموزش مهارت‌های ارتباط متقابل.",
            "طراحی پیام سلامت و آموزش.",
            "تحلیل روابط عمومی دوسویه.",
            "مطالعهٔ سواد رسانه‌ای و تفسیر مخاطب.",
            "آموزش مذاکره و گفت‌وگوی سازمانی.",
        ],
        example_text="پزشکی که پیش از توضیح درمان سطح دانش و نگرانی بیمار را می‌سنجد و پس از توضیح بازخورد او را می‌پرسد، حلقهٔ شرام را در عمل اجرا می‌کند؛ اگر همان توضیح بدون سنجش میدان تجربه و بدون بازخورد گفته شود، پیام می‌رسد اما فهم شکل نمی‌گیرد.",
        evolution="مدل در سال ۱۹۵۴ در فصل شرام صورت‌بندی شد و در ویراست سال ۱۹۷۱ برای ارتباط جمعی بازنویسی شد. پس از آن به پایهٔ مدل‌های تعاملی و دوسویه در ارتباطات و روابط عمومی تبدیل شد و در آموزش ارتباطات به‌عنوان نقطهٔ گذار از مدل خطی شناخته می‌شود.",
        key_concepts=["میدان تجربه", "رمزگذاری", "رمزگشایی", "تفسیر", "بازخورد", "حلقهٔ ارتباطی", "هم‌پوشانی تجربه"],
        theorists="ویلفرد شرام.",
        theorists_text="مدل در سنت پژوهش ارتباط جمعی دانشگاه ایلینوی شکل گرفت.",
        model="حلقهٔ رمزگذاری، تفسیر و رمزگشایی متقابل که با بازخورد بسته می‌شود و بر میدان تجربهٔ مشترک استوار است.",
        studies=[
            "فصل سال ۱۹۵۴ مدل حلقه‌ای را معرفی کرد.",
            "ویراست سال ۱۹۷۱ نسخهٔ ارتباط جمعی را گسترد.",
            "پژوهش‌های آموزش ارتباط، مدل را مبنای تمرین بازخورد کردند.",
            "مطالعات روابط عمومی، حلقه را به ارتباط دوسویه پیوند دادند.",
        ],
    ),
    "MC-463": dict(
        year=1953,
        summary="مدل نیوکامب، که تئودور نیوکامب در مقالهٔ سال ۱۹۵۳ در مجلهٔ روان‌شناسی ارائه کرد، ارتباط را در چارچوب هم‌جهت‌گیری دو شخص نسبت به یک موضوع مشترک توضیح می‌دهد. سه عنصر مدل عبارت‌اند از شخص نخست، شخص دوم و موضوعی که هر دو به آن گرایش دارند. هر شخص دو نگرش دارد: نگرش به دیگری و نگرش به موضوع. وقتی این نگرش‌ها ناهمخوان باشند، نیرویی به سوی تقارن پدید می‌آید و ارتباط ابزار اصلی بازگرداندن تعادل است. نیوکامب این منطق را از نظریهٔ تعادل هایدر وام گرفت و آن را به موقعیت ارتباطی دو نفره گسترد. مدل او بعدها پایهٔ پژوهش هم‌جهت‌گیری شد که در آن ادراک هر طرف از نگرش طرف دیگر نیز سنجیده می‌شود، نه فقط نگرش واقعی او. همین ایده در مطالعهٔ روابط رسانه، دولت و افکار عمومی نیز به کار رفت. نقدهای اصلی به مدل، تمرکز افراطی بر دو نفر، فرض تمایل طبیعی به تعادل، نادیده‌گرفتن قدرت و نابرابری، بی‌توجهی به محتوای پیام و دشواری آزمون پویایی تغییر را برجسته می‌کنند.",
        definition="مدل نیوکامب، ارتباط را کنشی برای بازگرداندن تعادل میان نگرش دو شخص و نگرش آن‌ها به یک موضوع مشترک می‌داند و هم‌جهت‌گیری را سازوکار اصلی این تعادل معرفی می‌کند.",
        main_problem="چگونه ارتباط میان دو شخص، ناهمخوانی نگرش‌ها را کاهش می‌دهد و تعادل شناختی و اجتماعی را بازمی‌گرداند.",
        mechanism="هر شخص نگرش خود به دیگری و به موضوع را می‌سنجد؛ اگر ترکیب نگرش‌ها ناهمخوان باشد، فشار روانی به سوی تقارن ایجاد می‌شود و طرفین با گفت‌وگو، تغییر نگرش یا بازتعریف رابطه، تعادل را بازمی‌سازند.",
        assumptions=[
            "افراد به تعادل شناختی گرایش دارند.",
            "ارتباط ابزار بازگرداندن تعادل است.",
            "نگرش به شخص و موضوع هم‌زمان اهمیت دارد.",
            "ادراک فرد از نگرش دیگری بر رفتار اثر می‌گذارد.",
            "موضوع مشترک، محور هم‌جهت‌گیری است.",
        ],
        principles=[
            "نگرش هر طرف به دیگری و به موضوع را جدا بسنج.",
            "ادراک طرفین از نگرش یکدیگر را بررسی کن.",
            "ناهمخوانی نگرش‌ها را به‌عنوان محرک ارتباط ببین.",
            "نقش گروه مرجع و هنجار جمعی را لحاظ کن.",
            "تعادل را فرایندی پویا و نه وضعیتی ثابت بدان.",
            "موضوع مشترک را به‌روشنی تعریف کن.",
            "هنجارهای گروه را در تحلیل تعادل وارد کن.",
        ],
        critiques=[
            "بر دو نفر متمرکز است و گروه را کم‌بررسی می‌گذارد.",
            "تمایل طبیعی به تعادل را بیش از واقع فرض می‌کند.",
            "قدرت و نابرابری رابطه را نادیده می‌گیرد.",
            "به محتوای پیام و معنا کم‌توجه است.",
            "آزمون تجربی پویایی تغییر دشوار است.",
            "هم‌زمانی چند موضوع مشترک را نادیده می‌گیرد.",
        ],
        critique_text="منتقدان می‌گویند مدل نیوکامب با فرض گرایش به تعادل، ارتباط را بیش از اندازه هماهنگ و بی‌کشمکش تصویر می‌کند و نقش قدرت و محتوای پیام را کم‌رنگ می‌سازد؛ با این حال، بنیان پژوهش هم‌جهت‌گیری و مطالعهٔ نگرش در ارتباطات شد.",
        applications=[
            "تحلیل ارتباط خانوادگی و زناشویی.",
            "مطالعهٔ جو کلاس و ارتباط معلم و دانش‌آموز.",
            "پژوهش هم‌جهت‌گیری رسانه و افکار عمومی.",
            "بررسی تعادل نگرش در گروه‌های کاری.",
            "آموزش میانجی‌گری و حل تعارض.",
            "تحلیل تبلیغات مقایسه‌ای و نگرش برند.",
        ],
        example_text="دو همکار که یکی طرح جدید را مفید و دیگری بی‌فایده می‌داند، دربارهٔ آن گفت‌وگو می‌کنند تا نگرش‌ها به هم نزدیک شود؛ اگر گفت‌وگو نتیجه ندهد، ممکن است نگرش یکی به دیگری نیز تغییر کند تا تعادل حفظ شود. این پویایی، هستهٔ مدل نیوکامب است.",
        evolution="مدل در مقالهٔ سال ۱۹۵۳ صورت‌بندی شد و سپس در سنت پژوهش هم‌جهت‌گیری گسترش یافت. این سنت، ادراک طرفین از نگرش یکدیگر را به مدل افزود و آن را برای مطالعهٔ رسانه، سازمان و افکار عمومی به کار گرفت.",
        key_concepts=["هم‌جهت‌گیری", "تعادل شناختی", "تقارن", "نگرش به موضوع", "نگرش به دیگری", "گروه مرجع"],
        theorists="تئودور نیوکامب.",
        theorists_text="مدل در سنت روان‌شناسی اجتماعی و پژوهش نگرش شکل گرفت.",
        model="سه‌گانهٔ دو شخص و یک موضوع مشترک که با فشار به سوی تقارن و از راه ارتباط به تعادل می‌رسد.",
        studies=[
            "مقالهٔ سال ۱۹۵۳ مدل سه‌گانه را معرفی کرد.",
            "پژوهش هم‌جهت‌گیری، ادراک متقابل را به مدل افزود.",
            "مطالعات رسانه، مدل را برای رابطهٔ مطبوعات و عموم به کار بردند.",
            "پژوهش ارتباط خانوادگی، تعادل نگرش را آزمود.",
            "پژوهش نگرش، تقارن را در موقعیت‌های آزمایشی سنجید.",
        ],
    ),
    "MC-464": dict(
        year=1960,
        summary="مدل اس‌ام‌سی‌آر برلو، که دیوید برلو در کتاب فرایند ارتباط در سال ۱۹۶۰ معرفی کرد، ارتباط را با چهار عنصر منبع، پیام، کانال و گیرنده توصیف می‌کند و برای هر عنصر عوامل مؤثر را فهرست می‌کند. منبع و گیرنده هر دو با پنج عامل مشخص می‌شوند: مهارت‌های ارتباطی، نگرش‌ها، دانش، نظام اجتماعی و فرهنگ. پیام نیز با محتوا، نحوهٔ ارائه، ساختار و رمز سنجیده می‌شود و کانال، حواس پنج‌گانه را در بر می‌گیرد. نوآوری برلو در آن بود که گیرنده را آینهٔ منبع دانست و تأکید کرد موفقیت ارتباط به هم‌خوانی این عوامل در دو سوی فرایند بستگی دارد. با این حال، مدل همچنان خطی و یک‌سویه است و بازخورد و تفسیر فعال گیرنده در آن جایی ندارد. برلو خود ارتباط را فرایندی تعاملی می‌دانست اما ترسیم او بیشتر به انتقال معنا شبیه است. این مدل در آموزش ارتباطات، طراحی پیام آموزشی و تبلیغات بسیار به کار رفت. نقدهای اصلی به آن، نادیده‌گرفتن بازخورد، تمرکز بر انتقال به‌جای ساخت معنا، غفلت از پارازیت و بافت، فردگرایی و ساده‌سازی عوامل فرهنگی را برجسته می‌کنند.",
        definition="مدل اس‌ام‌سی‌آر، ارتباط را با چهار عنصر منبع، پیام، کانال و گیرنده توصیف می‌کند و برای هر عنصر عواملی مانند مهارت، نگرش، دانش، نظام اجتماعی و فرهنگ را در نظر می‌گیرد.",
        main_problem="چه عواملی در منبع، پیام، کانال و گیرنده تعیین می‌کنند که پیام به‌درستی منتقل شود و فهم مشترک شکل بگیرد.",
        mechanism="منبع با مهارت، نگرش، دانش و زمینهٔ فرهنگی خود پیام را می‌سازد؛ پیام با محتوا، ساختار، نحوهٔ ارائه و رمز در کانالی حسی به گیرنده می‌رسد و گیرنده با عوامل مشابه خود آن را دریافت می‌کند؛ هم‌خوانی این عوامل، فهم را تسهیل می‌کند.",
        assumptions=[
            "ارتباط انتقال پیام از منبع به گیرنده است.",
            "منبع و گیرنده عوامل مشابهی دارند.",
            "مهارت و دانش، کیفیت ارتباط را تعیین می‌کنند.",
            "کانال‌های حسی مسیر انتقال‌اند.",
            "هم‌خوانی عوامل دو طرف، فهم را ممکن می‌سازد.",
        ],
        principles=[
            "مهارت‌های ارتباطی منبع و گیرنده را بسنج.",
            "نگرش و دانش مخاطب را در طراحی پیام لحاظ کن.",
            "محتوا و ساختار پیام را با رمز مشترک هماهنگ کن.",
            "کانال مناسب را بر پایهٔ حواس مخاطب برگزین.",
            "زمینهٔ اجتماعی و فرهنگی دو طرف را در نظر بگیر.",
            "هم‌خوانی عوامل منبع و گیرنده را هدف بگیر.",
            "پارازیت و اختلال کانال را پیش‌بینی کن.",
        ],
        critiques=[
            "بازخورد و تفسیر فعال گیرنده را نادیده می‌گیرد.",
            "بر انتقال به‌جای ساخت معنا تمرکز دارد.",
            "پارازیت و بافت موقعیتی را لحاظ نمی‌کند.",
            "فردگرا و کم‌توجه به ساختار اجتماعی است.",
            "عوامل فرهنگی را به فهرستی ساده فرو می‌کاهد.",
        ],
        critique_text="منتقدان می‌گویند مدل برلو با فهرست‌کردن عوامل، چارچوب آموزشی مفیدی ساخت اما ارتباط را همچنان انتقالی و یک‌سویه دید و بازخورد، بافت و ساخت معنا را کم‌رنگ کرد؛ با این حال، پایهٔ آموزش طراحی پیام و ارتباط آموزشی شد.",
        applications=[
            "طراحی پیام آموزشی و کمک‌آموزشی.",
            "آموزش مهارت‌های ارتباطی.",
            "تحلیل پیام تبلیغاتی و تبلیغ سلامت.",
            "تدوین راهنمای ارتباط سازمانی.",
            "ارزیابی هم‌خوانی پیام و مخاطب.",
        ],
        example_text="یک کارگاه بهداشت زمانی موفق است که مدرس مهارت بیان، نگرش و دانش مخاطبان را بسنجد، محتوا را ساده و ساختارمند ارائه کند و از کانال دیداری و شنیداری مناسب بهره بگیرد؛ اگر یکی از این عوامل هم‌خوان نباشد، پیام منتقل می‌شود اما رفتار تغییر نمی‌کند.",
        evolution="مدل در کتاب سال ۱۹۶۰ برلو معرفی شد و به سرعت در آموزش ارتباطات و طراحی پیام جای گرفت. با چرخش به مدل‌های تعاملی و تفسیری، محدودیت خطی‌بودن آن آشکار شد اما چارچوب چهارعنصری آن همچنان در آموزش به کار می‌رود.",
        key_concepts=["منبع", "پیام", "کانال", "گیرنده", "مهارت ارتباطی", "نظام اجتماعی", "فرهنگ"],
        theorists="دیوید برلو.",
        theorists_text="مدل در سنت آموزش ارتباطات و نظریهٔ انتقال پیام شکل گرفت.",
        model="چهار عنصر منبع، پیام، کانال و گیرنده که هر یک با مهارت، نگرش، دانش و زمینهٔ فرهنگی و اجتماعی مشخص می‌شود.",
        studies=[
            "کتاب سال ۱۹۶۰ مدل چهارعنصری را معرفی کرد.",
            "پژوهش آموزش، مدل را مبنای طراحی کمک‌آموزشی کرد.",
            "مطالعات تبلیغات، عوامل پیام را با آن تحلیل کردند.",
            "ادبیات ارتباط سلامت، هم‌خوانی منبع و گیرنده را آزمود.",
        ],
    ),
    "MC-465": dict(
        year=1967,
        summary="مدل ادراکی گربر، که جورج گربر آن را در مقالهٔ سال ۱۹۵۶ صورت‌بندی کرد و در فصل سال ۱۹۶۷ برای رسانه‌های جمعی گسترد، ارتباط را فرایندی ادراکی و زنجیره‌ای می‌داند. در این مدل، رویداد بیرونی وجود دارد اما آنچه پیام می‌شود، ادراک ما از رویداد است، نه خود رویداد. گربر دو بُعد را از هم جدا می‌کند: بُعد افقی که گزینش، بافت و دسترس‌پذیری را در بر می‌گیرد و بُعد عمودی که بر پیام تمرکز دارد و شامل ادراک، ابزار و کانال، شکل، محتوا و پیامد است. او ارتباط را کنشی متقابل میان این دو بُعد می‌بیند و تأکید می‌کند پیام، ادراکی از ادراک است. در نسخهٔ رسانه‌ای، سازمان رسانه‌ای چند مرحلهٔ گزینش و پردازش را میان رویداد و مخاطب قرار می‌دهد و هر مرحله ادراک را دگرگون می‌سازد. این مدل، پلی میان نظریهٔ ادراک و تحلیل محتوای رسانه است. نقدهای اصلی به آن، پیچیدگی و دشواری عملیاتی‌سازی مفاهیم، ابهام رابطهٔ بُعد افقی و عمودی، تمرکز بر ادراک فردی، آزمون‌پذیری محدود و فرض‌های هنجاری دربارهٔ وفاداری پیام را برجسته می‌کنند.",
        definition="مدل ادراکی گربر، ارتباط را زنجیره‌ای از ادراک‌ها می‌داند که در آن پیام، ادراک گزینش‌شدهٔ رویداد است و گزینش، بافت و دسترس‌پذیری، شکل و محتوای آن را می‌سازند.",
        main_problem="چگونه ادراک گزینشی و بافت‌مند، رویداد را به پیام تبدیل می‌کند و رسانه‌های جمعی این زنجیرهٔ ادراکی را چگونه دگرگون می‌سازند.",
        mechanism="رویداد در بُعد افقی با گزینش، بافت و دسترس‌پذیری به ادراک تبدیل می‌شود؛ در بُعد عمودی این ادراک با ابزار، شکل و محتوا به پیام می‌رسد و در گیرنده ادراک تازه‌ای می‌سازد؛ هر مرحله، بخشی از اطلاعات را حذف یا دگرگون می‌کند.",
        assumptions=[
            "پیام بازنمایی مستقیم رویداد نیست.",
            "ادراک، گزینشی و بافت‌مند است.",
            "دسترس‌پذیری بر انتخاب رویداد اثر می‌گذارد.",
            "هر مرحلهٔ انتقال، ادراک را دگرگون می‌کند.",
            "ادراک گیرنده از ادراک فرستنده متفاوت است.",
        ],
        principles=[
            "بُعد افقی و عمودی پیام را جدا تحلیل کن.",
            "گزینش، بافت و دسترس‌پذیری را در تولید پیام بسنج.",
            "تفاوت ادراک فرستنده و گیرنده را جدی بگیر.",
            "مراحل پردازش رسانه‌ای را در زنجیره ردیابی کن.",
            "شکل و محتوای پیام را با هم تحلیل کن.",
            "پیامد ادراکی پیام را در مخاطب بررسی کن.",
            "زنجیرهٔ ادراک را از رویداد تا مخاطب ترسیم کن.",
        ],
        critiques=[
            "مفاهیم مدل برای عملیاتی‌سازی دشوارند.",
            "رابطهٔ بُعد افقی و عمودی مبهم است.",
            "بر ادراک فردی متمرکز و ساختار اجتماعی را کم‌بررسی می‌گذارد.",
            "آزمون تجربی کامل مدل دشوار است.",
            "فرض‌های هنجاری دربارهٔ وفاداری پیام دارد.",
            "مفهوم دسترس‌پذیری مبهم و چندمعناست.",
        ],
        critique_text="منتقدان می‌گویند مدل گربر پیچیدگی ادراک را به‌خوبی نشان می‌دهد اما مفاهیم آن چنان گسترده‌اند که سنجش تجربی را دشوار می‌کنند و نقش ساختار اجتماعی کم‌رنگ می‌ماند؛ با این حال، پلی مهم میان نظریهٔ ادراک و تحلیل محتوای رسانه ساخت.",
        applications=[
            "تحلیل محتوای رسانه و گزینش خبر.",
            "آموزش سواد رسانه‌ای و ادراک مخاطب.",
            "مطالعهٔ ادراک خطر و پیام سلامت.",
            "تحلیل ارتباط دیداری و شکل پیام.",
            "پژوهش کاشت و پیامدهای ادراکی رسانه.",
        ],
        example_text="یک رویداد شهری در چند رسانه به شکل‌های متفاوت روایت می‌شود: هر رسانه بخشی از رویداد را گزینش می‌کند، آن را در بافت خود می‌گذارد و با قالب دیداری یا خبری خاصی ارائه می‌دهد؛ مخاطب نه رویداد، بلکه ادراک رسانه از رویداد را دریافت می‌کند. این زنجیره، دقیقاً همان چیزی است که گربر ترسیم کرد.",
        evolution="مدل در مقالهٔ سال ۱۹۵۶ گربر معرفی شد و در فصل سال ۱۹۶۷ برای رسانه‌های جمعی گسترش یافت. پس از آن، در تحلیل محتوا و پژوهش کاشت به کار رفت و زمینهٔ پیوند نظریهٔ ادراک با مطالعات رسانه را فراهم کرد.",
        key_concepts=["ادراک", "گزینش", "بافت", "دسترس‌پذیری", "بُعد افقی", "بُعد عمودی", "زنجیرهٔ ادراک"],
        theorists="جورج گربر.",
        theorists_text="مدل در سنت پژوهش ارتباط دیداری و نظریهٔ ادراک شکل گرفت.",
        model="زنجیرهٔ رویداد، ادراک گزینش‌شده و پیام که در دو بُعد افقی و عمودی، شکل و محتوای ارتباط را می‌سازد.",
        studies=[
            "مقالهٔ سال ۱۹۵۶ مدل ادراکی را معرفی کرد.",
            "فصل سال ۱۹۶۷ نسخهٔ رسانه‌های جمعی را گسترد.",
            "پژوهش کاشت، پیامد ادراکی رسانه را بررسی کرد.",
            "مطالعات تحلیل محتوا، گزینش خبری را با مدل تحلیل کردند.",
        ],
    ),
}

NAME_FIX = {"MC-462": ("مدل حلقه‌ای شرام", "Schramm's Loop Model", "عنوان پیشین «مدل حلقه/چرخه اسکم» خطای نویسه‌گردانی نام شرام بود؛ این کارت نسخهٔ موازی MC-305 است و برای بازبینی ادغام علامت‌گذاری شده است.")}
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
                                       "verified": n_verified, "batch": 143}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH143 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
