# -*- coding: utf-8 -*-
"""Batch 186 (SCHOOL): MC-333, MC-339, MC-344, MC-472."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch186-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch186.json"

SCHOOL_MAPPING = {"entity_type": "SCHOOL", "content_type": "مکتب فکری (School)", "needs_review": False}

S = {
    "MC-333": [
        dict(kind="BOOK",
             title_en="The Uses of Literacy: Aspects of Working-Class Life",
             title_fa="کاربردهای سوادآموزی: وجوه زندگی طبقهٔ کارگر",
             authors="Richard Hoggart", year=1957,
             publisher="Chatto & Windus",
             doi=None,
             url="https://archive.org/details/usesofliteracyby0000unse",
             language="en", isbn=None,
             citation="Hoggart, R. (1957). The Uses of Literacy: Aspects of Working-Class Life. London: Chatto & Windus.",
             locator="sections on working-class publications and entertainments", locator_type="SECTION",
             supports="foundational text of British cultural studies and its attention to popular culture", verified=True),
        dict(kind="BOOK",
             title_en="Culture, Media, Language: Working Papers in Cultural Studies, 1972-79",
             title_fa="فرهنگ، رسانه، زبان: مقاله‌های مرکز مطالعات فرهنگی ۱۹۷۲ تا ۱۹۷۹",
             authors="Stuart Hall, Dorothy Hobson, Andrew Lowe, Paul Willis (eds.)", year=1980,
             publisher="Hutchinson",
             doi=None,
             url="https://archive.org/details/culturemedialang0000unse",
             language="en", isbn=None,
             citation="Hall, S., Hobson, D., Lowe, A., & Willis, P. (Eds.). (1980). Culture, Media, Language. London: Hutchinson.",
             locator="Hall, Encoding/decoding, pp. 128-138", locator_type="PAGE",
             supports="encoding/decoding model at the centre of British cultural studies", verified=True),
        dict(kind="REPORT",
             title_en="Encoding and Decoding in the Television Discourse",
             title_fa="رمزگذاری و رمزگشایی در گفتمان تلویزیونی",
             authors="Stuart Hall; Centre for Contemporary Cultural Studies", year=1973,
             publisher="University of Birmingham",
             doi=None,
             url="https://epapers.bham.ac.uk/2962/1/Hall,_1973,_Encoding_and_Decoding_in_the_Television_Discourse.pdf",
             language="en", isbn=None,
             citation="Hall, S. (1973). Encoding and Decoding in the Television Discourse. CCCS Occasional Paper. Birmingham: University of Birmingham.",
             locator="CCCS occasional paper, September 1973", locator_type="SECTION",
             supports="original stencilled paper version of the encoding/decoding argument", verified=True),
    ],
    "MC-339": [
        dict(kind="BOOK",
             title_en="Amusing Ourselves to Death: Public Discourse in the Age of Show Business",
             title_fa="سرگرم تا سرحد مرگ: گفتمان عمومی در عصر نمایش تجاری",
             authors="Neil Postman", year=1985,
             publisher="Viking",
             doi=None,
             url="https://archive.org/details/amusingourselves0000post",
             language="en", isbn=None,
             citation="Postman, N. (1985). Amusing Ourselves to Death: Public Discourse in the Age of Show Business. New York: Viking.",
             locator="chapters on television and public discourse", locator_type="SECTION",
             supports="thesis that entertainment has become the dominant form of public discourse", verified=True),
        dict(kind="BOOK",
             title_en="Technopoly: The Surrender of Culture to Technology",
             title_fa="تکنوپولی: تسلیم فرهنگ به فناوری",
             authors="Neil Postman", year=1992,
             publisher="Alfred A. Knopf",
             doi=None,
             url="https://archive.org/details/235p-technopoly-neil-postman",
             language="en", isbn=None,
             citation="Postman, N. (1992). Technopoly: The Surrender of Culture to Technology. New York: Knopf.",
             locator="chapters on technocracy and technopoly", locator_type="SECTION",
             supports="media ecology continuity from television critique to the critique of technological culture", verified=True),
    ],
    "MC-344": [
        dict(kind="BOOK",
             title_en="The Question Concerning Technology and Other Essays",
             title_fa="پرسش از فناوری و مقاله‌های دیگر",
             authors="Martin Heidegger; trans. William Lovitt", year=1977,
             publisher="Harper & Row",
             doi=None,
             url="https://archive.org/details/questionconcerni00heid",
             language="en", isbn=None,
             citation="Heidegger, M. (1977). The Question Concerning Technology and Other Essays (W. Lovitt, Trans.). New York: Harper & Row.",
             locator="The Question Concerning Technology, pp. 3-35", locator_type="PAGE",
             supports="Gestell (enframing) as the essence of modern technology", verified=True),
        dict(kind="WEBSITE",
             title_en="Philosophy of Technology (Stanford Encyclopedia of Philosophy)",
             title_fa="فلسفهٔ فناوری (دانشنامهٔ فلسفهٔ استنفورد)",
             authors="Maarten Franssen, Gert-Jan Lokhorst, Ibo van de Poel", year=2009,
             publisher="Stanford University",
             doi=None,
             url="https://plato.stanford.edu/entries/technology/",
             language="en", isbn=None,
             citation="Franssen, M., Lokhorst, G.-J., & van de Poel, I. (2009). Philosophy of Technology. Stanford Encyclopedia of Philosophy.",
             locator="sections on Heidegger and the essence of technology", locator_type="SECTION",
             supports="scholarly exposition of Heidegger's account of technology as enframing", verified=True),
    ],
    "MC-472": [
        dict(kind="BOOK",
             title_en="One-Dimensional Man: Studies in the Ideology of Advanced Industrial Society",
             title_fa="انسان تک‌ساحتی: پژوهش‌هایی در ایدئولوژی جامعهٔ صناعی پیشرفته",
             authors="Herbert Marcuse", year=1964,
             publisher="Beacon Press",
             doi=None,
             url="https://archive.org/details/onedimensionalm00marc",
             language="en", isbn=None,
             citation="Marcuse, H. (1964). One-Dimensional Man. Boston: Beacon Press.",
             locator="chapters on technological rationality and one-dimensional thought", locator_type="SECTION",
             supports="instrumental rationality as a mode of domination in advanced industrial society", verified=True),
        dict(kind="WEBSITE",
             title_en="Herbert Marcuse (Stanford Encyclopedia of Philosophy)",
             title_fa="هربرت مارکوزه (دانشنامهٔ فلسفهٔ استنفورد)",
             authors="Arnold Farr", year=2013,
             publisher="Stanford University",
             doi=None,
             url="https://plato.stanford.edu/entries/marcuse/",
             language="en", isbn=None,
             citation="Farr, A. (2013). Herbert Marcuse. Stanford Encyclopedia of Philosophy.",
             locator="sections on technological rationality and one-dimensionality", locator_type="SECTION",
             supports="overview of Marcuse's critique of instrumental and technological rationality", verified=True),
    ],
}

ENRICH = {
    "MC-333": dict(
        year=1964,
        mapping=SCHOOL_MAPPING,
        summary="مطالعات فرهنگی بریتانیا مکتبی فکری است که در ۱۹۶۴ با تأسیس مرکز مطالعات فرهنگی معاصر در دانشگاه بیرمنگام شکل گرفت و رسانه و فرهنگ عامه را میدان تولید معنا و منازعهٔ اجتماعی دانست. ریچارد هگارت با کتاب کاربردهای سوادآموزی راه را گشود و استوارت هال با مقالهٔ رمزگذاری و رمزگشایی الگوی تازه‌ای برای مطالعهٔ مخاطب ساخت. این مکتب مفهوم هژمونی را از گرامشی گرفت و نشان داد چگونه معناهای مسلط در رسانه ساخته و گاه به چالش کشیده می‌شوند. پژوهش‌های آن از تحلیل متن و مصاحبه تا قوم‌نگاری و تاریخ فرهنگی را در بر می‌گرفت و مطالعهٔ خرده‌فرهنگ، جوانان، نژاد و هراس اخلاقی را در دستور کار گذاشت. تأکید بر فعال‌بودن مخاطب و بر ساخت اجتماعی معنا، مرز میان متن و زمینه را بازتعریف کرد. این مکتب در دههٔ ۱۹۸۰ به آمریکا و استرالیا و آسیا گسترش یافت و به یکی از منابع اصلی مطالعات رسانه و مطالعات پسااستعماری بدل شد. مرکز بیرمنگام در ۲۰۰۲ بسته شد، اما میراث نظری آن در برنامه‌های درسی ارتباطات زنده ماند. نقدها بر متن‌محوری، کم‌توجهی به اقتصاد سیاسی و تمرکز بر تجربهٔ بریتانیا تأکید دارند.",
        definition="مطالعات فرهنگی بریتانیا مکتبی میان‌رشته‌ای است که از ۱۹۶۴ در بیرمنگام شکل گرفت و فرهنگ عامه و رسانه را عرصهٔ تولید معنا، هژمونی و مقاومت می‌داند.",
        main_problem="چگونه می‌توان نشان داد که معناهای فرهنگی و رسانه‌ای نه واقعیت‌های طبیعی، بلکه برساخته‌های اجتماعی و میدان کشمکش قدرت‌اند و مخاطب در برابر آن‌ها کنشگر است.",
        mechanism="تحلیل متن و رمزگذاری پیام را با مطالعهٔ مخاطب و زمینهٔ تاریخی پیوند می‌دهد؛ مفهوم هژمونی توضیح می‌دهد چگونه معناهای مسلط طبیعی می‌شوند و مفهوم مفصل‌بندی نشان می‌دهد معنا در ترکیب عناصر فرهنگی شکل می‌گیرد.",
        assumptions=[
            "فرهنگ عرصهٔ منازعهٔ معناست.",
            "معنا برساختهٔ اجتماعی است.",
            "مخاطب تفسیرکنندهٔ فعال است.",
            "رسانه بازتولیدکنندهٔ روابط قدرت است.",
            "تجربهٔ روزمرهٔ مردم شایستهٔ مطالعه است.",
            "تحلیل باید زمینهٔ تاریخی داشته باشد.",
            "طبقه، نژاد و جنسیت در هم تنیده‌اند.",
            "زبان و بازنمایی قدرت را پنهان می‌کنند.",
        ],
        principles=[
            "معنا را در زمینه بخوان.",
            "صدای فرهنگ عامه را جدی بگیر.",
            "هژمونی را در متن و مخاطب ردیابی کن.",
            "مقاومت مخاطب را جست‌وجو کن.",
            "تحلیل را با شواهد تاریخی پیوند بده.",
            "از تقلیل فرهنگ به اقتصاد بپرهیز.",
            "بازنمایی گروه‌های حاشیه‌ای را بررسی کن.",
        ],
        critiques=[
            "تحلیل متن‌محور است.",
            "اقتصاد سیاسی رسانه کم‌رنگ می‌شود.",
            "تمرکز بر تجربهٔ بریتانیا غالب است.",
            "روش‌ها گاه مبهم و تکرارناپذیرند.",
            "مرکز بیرمنگام در ۲۰۰۲ بسته شد.",
            "مفهوم مقاومت مخاطب اغراق شده است.",
            "پیوند مکتب با سیاست‌گذاری روشن نیست.",
        ],
        critique_text="منتقدان می‌گویند متن‌محوری، کم‌توجهی به اقتصاد سیاسی و تمرکز بر تجربهٔ بریتانیا، تعمیم‌پذیری و دقت روش‌شناختی این مکتب را محدود کرده است؛ با این حال مفهوم مخاطب فعال و تحلیل هژمونیک معنا، پژوهش رسانه را برای همیشه دگرگون کرد.",
        applications=[
            "تحلیل مخاطب تلویزیون.",
            "مطالعهٔ خرده‌فرهنگ جوانان.",
            "بررسی هراس اخلاقی رسانه‌ای.",
            "تحلیل بازنمایی نژاد.",
            "پژوهش سیاست هویت.",
            "مطالعهٔ موسیقی و سبک زندگی.",
            "تحلیل فرهنگ عامه.",
            "پژوهش رسانهٔ اقلیت‌ها.",
            "مطالعهٔ پسااستعماری رسانه.",
            "تحلیل تبلیغات و مصرف.",
            "پژوهش مخاطب اینترنت.",
            "مطالعهٔ بازنمایی جنسیت.",
            "تحلیل گفتمان خبر.",
            "پژوهش مقاومت کاربران.",
        ],
        example_text="پژوهشی دربارهٔ تفسیر یک سریال پرطرفدار نشان می‌دهد گروه‌های مختلف مخاطب پیام یکسان را به سه شکل مسلط، مذاکره‌ای و مقاومتی می‌خوانند؛ این یافتهٔ کلاسیک رمزگذاری و رمزگشایی، الگوی پژوهش مخاطب فعال را در مطالعات بعدی تثبیت می‌کند.",
        evolution="هگارت در ۱۹۵۷ راه را گشود، مرکز بیرمنگام در ۱۹۶۴ تأسیس شد، هال در ۱۹۶۸ رهبری نظری را گرفت، مقالهٔ رمزگذاری و رمزگشایی در ۱۹۷۳ و کتاب بحران پلیسی در ۱۹۷۸ منتشر شد، مکتب در دههٔ ۱۹۸۰ جهانی شد و پس از بسته‌شدن مرکز در ۲۰۰۲ به سنتی زنده در دانشگاه‌های جهان بدل شد.",
        key_concepts=["رمزگذاری و رمزگشایی", "هژمونی", "مفصل‌بندی", "خرده‌فرهنگ", "هراس اخلاقی", "مخاطب فعال", "بازنمایی"],
        theorists="ریچارد هگارت و استوارت هال.",
        theorists_text="هگارت مرکز را بنیان نهاد و هال با نظریهٔ رمزگذاری و رمزگشایی و مفهوم هژمونی، چارچوب نظری مکتب را صورت‌بندی کرد.",
        model="مدل گردش معنا: تولید، متن و مصرف سه لحظهٔ جداگانه‌اند و معنا در هر لحظه بازتولید یا دگرگون می‌شود؛ بنابراین تحلیل رسانه باید هر سه را جداگانه بررسی کند.",
        studies=[
            "تحلیل رمزگذاری و رمزگشایی.",
            "پژوهش خرده‌فرهنگ جوانان.",
            "مطالعهٔ هراس اخلاقی.",
            "تحلیل بحران پلیسی.",
            "پژوهش بازنمایی نژاد.",
            "مطالعهٔ مخاطب تلویزیون.",
            "تحلیل فرهنگ عامه.",
            "پژوهش موسیقی جوانان.",
            "مطالعهٔ سیاست هویت.",
            "تحلیل رسانهٔ اقلیت‌ها.",
            "پژوهش پسااستعماری.",
            "مطالعهٔ بازنمایی جنسیت.",
            "تحلیل گفتمان خبر.",
            "پژوهش مقاومت کاربر.",
        ],
    ),
    "MC-339": dict(
        year=1985,
        mapping=SCHOOL_MAPPING,
        summary="سرگرم تا سرحد مرگ عنوان کتابی از نیل پستمن در ۱۹۸۵ است که به‌عنوان یک موضع فکری در سنت بوم‌شناسی رسانه شناخته می‌شود و ادعا می‌کند سرگرمی به شکل غالب گفتمان عمومی در آمریکا بدل شده است. پستمن با الهام از هشدار آلدوس هاکسلی در دنیای قشنگ نو می‌گوید خطر اصلی نه سانسور یک حکومت تمامیت‌خواه، بلکه غرق‌شدن جامعه در سرگرمی است. او تلویزیون را نه فقط ابزار انتقال محتوا، بلکه خود شکل معرفت می‌داند که معیارهای جدیت، دقت و پیوستگی استدلال را تغییر می‌دهد. به باور او خبر، سیاست، دین و آموزش وقتی در قالب تلویزیون بیان می‌شوند به نمایش بدل می‌شوند و بینندگان در برابر جهان به تماشاگر بی‌واکنش فروکاسته می‌شوند. ساختار برنامه‌های خبری با گذار ناگهانی از یک موضوع به موضوع دیگر، پیوند رویدادها را می‌گسلد. این موضع بر نقد رسانه‌ای، سواد رسانه‌ای و اخلاق روزنامه‌نگاری اثر گذاشت. نقدها بر جبرگرایی فناورانه، نوستالژی جهان چاپی و نبود شواهد تجربی از مخاطب تأکید دارند.",
        definition="سرگرم تا سرحد مرگ موضعی فکری از نیل پستمن است که سرگرمی را شکل غالب گفتمان عمومی و تلویزیون را دگرگون‌کنندهٔ معیارهای معرفت می‌داند.",
        main_problem="چگونه می‌توان فهمید که تسلط سرگرمی بر رسانه، خود شیوهٔ اندیشیدن عمومی و معیارهای صدق و جدیت را دگرگون می‌کند و جامعه را به تماشاگر بی‌واکنش بدل می‌سازد.",
        mechanism="رسانه صرفاً محتوا را منتقل نمی‌کند بلکه شکل بیان را تحمیل می‌کند؛ تلویزیون با تصویر متحرک و گذار سریع، استدلال پیوسته را به قطعه‌های جذاب تبدیل می‌کند و همان معیارهای نمایشی به حوزه‌های سیاست و آموزش سرریز می‌شود.",
        assumptions=[
            "شکل رسانه بر معرفت اثر می‌گذارد.",
            "سرگرمی در آمریکا به گفتمان مسلط بدل شده است.",
            "مخاطب تلویزیون بیشتر تماشاگر است تا مشارکت‌کننده.",
            "پیوستگی استدلال در چاپ با تصویر تلویزیون متفاوت است.",
            "رسانه می‌تواند فرهنگ را بدون سانسور تضعیف کند.",
            "سواد رسانه‌ای پاسخ ممکن به این وضع است.",
            "هشدار هاکسلی از هشدار اورول واقعی‌تر است.",
            "معیارهای نمایشی به سیاست و دین سرریز می‌کنند.",
        ],
        principles=[
            "شکل رسانه را جدا از محتوا بررسی کن.",
            "سرگرمی را به‌عنوان معیار عمومی نقد کن.",
            "پیوستگی استدلال را در رسانه بسنج.",
            "مخاطب را از تماشاگر به پرسشگر بدل کن.",
            "سواد رسانه‌ای را آموزش بده.",
            "از نوستالژی ساده‌انگارانه بپرهیز.",
            "پیامدهای معرفتی سرگرمی را نشان بده.",
        ],
        critiques=[
            "جبرگرایی فناورانه در تحلیل دیده می‌شود.",
            "نوستالژی جهان چاپی بر استدلال سایه می‌اندازد.",
            "شواهد تجربی از مخاطب ارائه نمی‌شود.",
            "تجربهٔ آمریکا به همهٔ جوامع تعمیم می‌یابد.",
            "نقش مخاطب فعال نادیده می‌ماند.",
            "تفاوت ژانرهای سرگرمی کم‌رنگ می‌شود.",
            "راه‌حل‌های سیاستی روشن نیست.",
        ],
        critique_text="منتقدان می‌گویند جبرگرایی فناورانه، نوستالژی جهان چاپی و نبود شواهد تجربی، استدلال پستمن را آسیب‌پذیر می‌کند؛ با این حال پرسش او دربارهٔ پیامدهای معرفتی سرگرمی، همچنان یکی از مهم‌ترین پرسش‌های نقد رسانه است.",
        applications=[
            "آموزش سواد رسانه‌ای.",
            "نقد برنامه‌های خبری تلویزیون.",
            "تحلیل تبلیغات سیاسی.",
            "پژوهش رسانه و آموزش.",
            "بررسی سرگرمی‌شدن سیاست.",
            "نقد فرهنگ سلبریتی.",
            "مطالعهٔ خبر و نمایش.",
            "تحلیل دین در رسانه.",
            "پژوهش مخاطب کودک.",
            "نقد رسانهٔ تجاری.",
            "مطالعهٔ طنز سیاسی.",
            "تحلیل واقع‌نمایی تلویزیون.",
            "پژوهش رسانه و دموکراسی.",
            "نقد مصرف خبر.",
        ],
        example_text="تحلیل یک مناظرهٔ انتخاباتی تلویزیونی نشان می‌دهد چگونه بُرش‌های سریع، موسیقی و گرافیک، استدلال سیاسی را به نمایش جذاب تبدیل می‌کنند و بیننده بیشتر واکنش احساسی می‌گیرد تا پیام استدلالی؛ این نمونهٔ عینی، تز سرگرمی‌شدن گفتمان عمومی را روشن می‌کند.",
        evolution="پستمن این تز را در ۱۹۸۵ منتشر کرد، در دههٔ ۱۹۹۰ آن را در تکنوپولی گسترش داد، پس از فراگیری اینترنت و شبکه‌های اجتماعی این پرسش به سرگرمی الگوریتمی و اقتصاد توجه تعمیم یافت و امروز همچنان در نقد رسانهٔ دیجیتال به کار می‌رود.",
        key_concepts=["بوم‌شناسی رسانه", "سرگرمی", "گفتمان عمومی", "تماشاگر", "معرفت رسانه‌ای", "سواد رسانه‌ای"],
        theorists="نیل پستمن.",
        theorists_text="نیل پستمن در سنت بوم‌شناسی رسانه، تز سرگرمی‌شدن گفتمان عمومی را صورت‌بندی کرد و آن را به نقد فرهنگ فناورانه گسترش داد.",
        model="مدل شکل‌دهی رسانه: رسانه نه فقط ظرف محتوا بلکه قالب معرفت است؛ تغییر قالب از چاپ به تصویر، معیارهای جدیت و استدلال را تغییر می‌دهد و سرگرمی را به هنجار عمومی بدل می‌کند.",
        studies=[
            "تحلیل ساختار خبر تلویزیونی.",
            "پژوهش سرگرمی سیاسی.",
            "مطالعهٔ آموزش تلویزیونی.",
            "نقد تبلیغات انتخاباتی.",
            "تحلیل دین در رسانه.",
            "پژوهش مخاطب کودک.",
            "مطالعهٔ طنز سیاسی.",
            "تحلیل واقع‌نمایی تلویزیون.",
            "پژوهش رسانه و دموکراسی.",
            "نقد مصرف خبر.",
            "مطالعهٔ سلبریتی.",
            "تحلیل نمایش درام.",
            "پژوهش سواد رسانه‌ای.",
            "نقد اقتصاد توجه.",
        ],
    ),
    "MC-344": dict(
        year=1954,
        mapping=SCHOOL_MAPPING,
        summary="فلسفهٔ فناوری و گشتل به موضع هایدگر در مقالهٔ پرسش از فناوری بازمی‌گردد که نخست در ۱۹۵۴ منتشر شد و در ۱۹۷۷ به انگلیسی ترجمه شد. هایدگر تعریف ابزاری و انسان‌محور فناوری را ناکافی می‌داند و می‌کوشد ذات فناوری را از دل پرسش از حقیقت آشکار کند. به باور او فناوری مدرن نه ابزار بی‌طرف، بلکه شیوه‌ای از آشکارسازی است که طبیعت و انسان را به‌عنوان ذخیرهٔ قابل بهره‌برداری فرا می‌خواند. مفهوم گشتل یا چارچوب‌بندی، این فرا خواندن را به‌عنوان ساختار مسلط عصر نشان می‌دهد که در آن همه‌چیز به منبع و موجودی برای مصرف بدل می‌شود. هایدگر خطر را در همین چارچوب‌بندی می‌بیند، اما از نجات نیز سخن می‌گوید و هنر و تفکر تأملی را راهی برای نسبت آزادتر با فناوری می‌داند. این اندیشه بر فلسفهٔ فناوری، نظریهٔ رسانهٔ آلمانی، اخلاق فناوری و نقد هوش مصنوعی اثر گذاشته است. نقدها بر زبان دشوار، کلی‌گویی و بی‌اعتنایی به تحلیل تجربی و سیاسی تأکید دارند.",
        definition="فلسفهٔ فناوری و گشتل موضع هایدگر است که فناوری مدرن را نه ابزار بی‌طرف، بلکه شیوهٔ آشکارسازی و چارچوب‌بندی هستی به‌عنوان ذخیره می‌داند.",
        main_problem="چگونه می‌توان ذات فناوری مدرن را فهمید اگر تعریف ابزاری آن ناکافی باشد و چگونه می‌توان در عین پذیرش فناوری، از سلطهٔ چارچوب‌بندی رها شد.",
        mechanism="مقاله از پرسش از علت و ابزار آغاز می‌کند و با تحلیل آشکارسازی به مفهوم گشتل می‌رسد؛ در این چارچوب، طبیعت و انسان به موجودی برای بهره‌برداری بدل می‌شوند و تفکر تأملی و هنر می‌توانند نسبت دیگری با فناوری بگشایند.",
        assumptions=[
            "فناوری صرفاً ابزار نیست.",
            "ذات فناوری به آشکارسازی حقیقت پیوند دارد.",
            "فناوری مدرن جهان را به ذخیره بدل می‌کند.",
            "انسان نیز در چارچوب‌بندی گرفتار می‌شود.",
            "خطر در ذات فناوری نهفته است.",
            "هنر می‌تواند راه نجات بگشاید.",
            "تفکر تأملی با محاسبه‌گری متفاوت است.",
            "پرسش از فناوری خود نوعی مقاومت است.",
        ],
        principles=[
            "از تعریف ابزاری فراتر برو.",
            "ذات پدیده را از راه پرسش بگشا.",
            "زبان فناوری را نقد کن.",
            "خطر و نجات را با هم ببین.",
            "تفکر محاسبه‌گر را محدود کن.",
            "نسبت آزاد با فناوری را بجوی.",
            "هنر و شعر را جدی بگیر.",
        ],
        critiques=[
            "زبان مقاله دشوار و مبهم است.",
            "تحلیل تجربی و تاریخی ارائه نمی‌شود.",
            "نقد سیاسی روشنی در آن نیست.",
            "راه‌حل عملی برای سیاست فناوری ندارد.",
            "مفهوم گشتل بیش از اندازه کلی است.",
            "موضع ضد فناوری به آن نسبت داده می‌شود.",
            "نقش نهادها و اقتصاد نادیده می‌ماند.",
        ],
        critique_text="منتقدان می‌گویند زبان دشوار، کلی‌گویی و بی‌اعتنایی به تحلیل تجربی و سیاسی، کاربرد عملی این فلسفه را محدود می‌کند؛ با این حال پرسش هایدگر دربارهٔ ذات فناوری، چارچوبی ماندگار برای نقد جبرگرایی فناورانه و اخلاق طراحی فراهم کرده است.",
        applications=[
            "اخلاق هوش مصنوعی.",
            "نقد جبرگرایی فناورانه.",
            "فلسفهٔ طراحی.",
            "تحلیل فناوری و محیط زیست.",
            "نظریهٔ رسانهٔ آلمانی.",
            "پژوهش فناوری و بدن.",
            "نقد اقتصاد داده.",
            "اخلاق مهندسی.",
            "مطالعهٔ اتوماسیون کار.",
            "تحلیل فناوری و هنر.",
            "پژوهش زیرساخت رسانه.",
            "نقد مصرف‌گرایی فناورانه.",
            "مطالعهٔ فناوری و زمان.",
            "تحلیل رابطهٔ انسان و ماشین.",
        ],
        example_text="طراح یک سیستم هوش مصنوعی با پرسش هایدگری می‌آزماید که آیا سامانه، کاربر و داده را تنها به‌عنوان منبع بهره‌برداری می‌بیند یا امکان نسبت انسانی و پاسخ‌گویی را باز می‌گذارد؛ این پرسش، اخلاق طراحی را از کارایی صرف فراتر می‌برد.",
        evolution="مقاله در ۱۹۵۴ در مجموعهٔ سخنرانی‌ها و مقاله‌ها منتشر شد، در ۱۹۷۷ به انگلیسی ترجمه شد، در دههٔ ۱۹۸۰ با فلسفهٔ فناوری معاصر پیوند یافت، در دههٔ ۲۰۰۰ به اخلاق اطلاعات و طراحی راه یافت و امروز در نقد هوش مصنوعی و اقتصاد داده به کار می‌رود.",
        key_concepts=["گشتل", "چارچوب‌بندی", "آشکارسازی", "ذخیرهٔ موجود", "تفکر تأملی", "خطر و نجات"],
        theorists="مارتین هایدگر.",
        theorists_text="هایدگر در پرسش از فناوری، ذات فناوری مدرن را به‌عنوان گشتل صورت‌بندی کرد و نسبت تفکر تأملی و هنر با فناوری را گشود.",
        model="مدل چارچوب‌بندی: فناوری مدرن جهان را به ذخیرهٔ قابل محاسبه بدل می‌کند؛ آگاهی از این چارچوب و پرورش تفکر تأملی، امکان نسبت آزادتر با فناوری را فراهم می‌کند.",
        studies=[
            "تحلیل مقالهٔ پرسش از فناوری.",
            "پژوهش گشتل و اخلاق طراحی.",
            "مطالعهٔ فناوری و محیط زیست.",
            "تحلیل هوش مصنوعی و انسان.",
            "پژوهش نظریهٔ رسانهٔ آلمانی.",
            "مطالعهٔ فناوری و هنر.",
            "تحلیل اقتصاد داده.",
            "پژوهش اتوماسیون کار.",
            "مطالعهٔ زیرساخت رسانه.",
            "تحلیل فناوری و زمان.",
            "پژوهش بدن و فناوری.",
            "مطالعهٔ جبرگرایی فناورانه.",
            "تحلیل رابطهٔ انسان و ماشین.",
            "پژوهش تفکر محاسبه‌گر.",
        ],
    ),
    "MC-472": dict(
        year=1964,
        mapping=SCHOOL_MAPPING,
        summary="عقلانیت ابزاری و انسان تک‌ساحتی موضع هربرت مارکوزه در کتاب انسان تک‌ساحتی در ۱۹۶۴ است که در سنت مکتب فرانکفورت جای دارد. مارکوزه نشان می‌دهد در جامعهٔ صناعی پیشرفته، عقلانیت فناورانه از ابزار کارآمدی به شکل سلطه بدل می‌شود و انسان را به موجودی مصرف‌کننده و سازگار فرو می‌کاهد. او از نیازهای کاذبی سخن می‌گوید که نظام تولید و تبلیغات می‌سازد و رضایت مصرفی را جانشین آزادی می‌کند. مفهوم تک‌ساحتی بودن به از میان رفتن بُعد انتقادی و ناتوانی در تصور بدیل اشاره دارد؛ زبانی که پیچیدگی را حذف می‌کند و تفکر را به تأیید وضع موجود محدود می‌سازد. مارکوزه همچنین از تسکین واپس‌راننده سخن می‌گوید؛ آزادسازی ظاهری سکسوالیته و سرگرمی که در خدمت تثبیت نظم موجود قرار می‌گیرد. او راه رهایی را در هنر، تخیل و نیروهای حاشیه‌ای جامعه می‌جوید. این اندیشه بر نقد مصرف‌گرایی، مطالعات فرهنگی، نقد فناوری و نظریهٔ انتقادی رسانه اثر گذاشته است. نقدها بر بدبینی، نخبه‌گرایی و نبود شواهد تجربی تأکید دارند.",
        definition="عقلانیت ابزاری و انسان تک‌ساحتی موضع مارکوزه است که عقلانیت فناورانه را شکل نوینی از سلطه می‌داند که بُعد انتقادی انسان را در جامعهٔ صناعی پیشرفته از میان می‌برد.",
        main_problem="چگونه می‌توان توضیح داد که در جامعه‌ای با رفاه مادی و آزادی رسمی، انسان‌ها به وضع موجود تن می‌دهند و توان نقد و تصور بدیل را از دست می‌دهند.",
        mechanism="نظام تولید و تبلیغات نیازهای کاذب می‌سازد، عقلانیت کارآمدی را به هنجار عمومی بدل می‌کند و زبان و فرهنگ را به تأیید وضع موجود محدود می‌سازد؛ در نتیجه بُعد انتقادی در برابر جذابیت مصرف و سرگرمی تحلیل می‌رود.",
        assumptions=[
            "عقلانیت فناورانه شکل سلطه است.",
            "نیازهای مصرفی می‌توانند ساختگی باشند.",
            "جامعهٔ رفاهی مخالفان را جذب می‌کند.",
            "زبان رسمی پیچیدگی انتقادی را حذف می‌کند.",
            "هنر بُعد رهایی‌بخش دارد.",
            "گروه‌های حاشیه‌ای نیروی تغییرند.",
            "آزادی رسمی با سلطهٔ واقعی همراه می‌شود.",
            "تفکر تک‌ساحتی بدیل‌ها را ناممکن می‌بیند.",
        ],
        principles=[
            "کارآمدی را با آزادی بسنج.",
            "نیازهای مصرفی را نقد کن.",
            "بُعد انتقادی را زنده نگه دار.",
            "زبان ساده‌شده را وارسی کن.",
            "هنر را عرصهٔ بدیل ببین.",
            "صدای حاشیه‌ها را جدی بگیر.",
            "از تسکین واپس‌راننده بپرهیز.",
        ],
        critiques=[
            "تحلیل بدبینانه و یک‌سویه است.",
            "نخبه‌گرایی در داوری فرهنگ دیده می‌شود.",
            "شواهد تجربی گسترده ارائه نمی‌شود.",
            "نقش کنشگری مخاطب کم‌رنگ است.",
            "مفهوم نیاز کاذب مبهم است.",
            "تحلیل اقتصادی ساختاری کافی نیست.",
            "راه رهایی عملی روشن نیست.",
        ],
        critique_text="منتقدان می‌گویند بدبینی، نخبه‌گرایی و نبود شواهد تجربی، تحلیل مارکوزه را در برابر نقد آسیب‌پذیر می‌کند؛ با این حال پیوند او میان عقلانیت فناورانه، مصرف و افول نقد، همچنان چارچوبی نیرومند برای نقد جامعهٔ مصرفی و رسانهٔ تجاری است.",
        applications=[
            "نقد مصرف‌گرایی.",
            "تحلیل تبلیغات تجاری.",
            "پژوهش فناوری و کنترل.",
            "نقد مدیریت الگوریتمی.",
            "مطالعهٔ فرهنگ سرگرمی.",
            "تحلیل صنعت فرهنگ.",
            "پژوهش آموزش و کارآمدی.",
            "نقد زبان بوروکراتیک.",
            "مطالعهٔ بدن و مصرف.",
            "تحلیل گیمیفیکیشن.",
            "پژوهش رسانه و اعتراض.",
            "نقد اقتصاد توجه.",
            "مطالعهٔ شهر و مصرف.",
            "تحلیل هنر انتقادی.",
        ],
        example_text="پژوهشی دربارهٔ سامانه‌های امتیازدهی کارکنان نشان می‌دهد چگونه سنجه‌های کارآمدی، رفتار و حتی خلاقیت را به شاخص قابل مدیریت تبدیل می‌کنند و اعتراض را بی‌معنا می‌سازند؛ این نمونه، عقلانیت ابزاری مارکوزه‌ای را در سازمان امروز بازمی‌یابد.",
        evolution="مارکوزه این تحلیل را در ۱۹۶۴ منتشر کرد، در جنبش‌های دانشجویی دههٔ ۱۹۶۰ اثر گذاشت، در دههٔ ۱۹۷۰ با نقد فناوری و زیست‌محیطی پیوند یافت، در دههٔ ۲۰۰۰ در نقد مدیریت و مصرف بازخوانی شد و امروز در تحلیل پلتفرم و هوش مصنوعی به کار می‌رود.",
        key_concepts=["عقلانیت ابزاری", "انسان تک‌ساحتی", "نیاز کاذب", "تسکین واپس‌راننده", "صنعت فرهنگ", "بُعد انتقادی"],
        theorists="هربرت مارکوزه.",
        theorists_text="مارکوزه در سنت مکتب فرانکفورت، عقلانیت فناورانه را به‌عنوان شکل نوین سلطه تحلیل کرد و بُعد انتقادی و هنری انسان را نقطهٔ مقاومت دانست.",
        model="مدل تک‌ساحتی‌شدن: عقلانیت کارآمدی نیاز می‌سازد، مصرف رضایت جای آزادی را می‌گیرد و زبان و فرهنگ بُعد انتقادی را حذف می‌کنند؛ رهایی از راه هنر و نیروهای حاشیه‌ای ممکن می‌شود.",
        studies=[
            "تحلیل انسان تک‌ساحتی.",
            "پژوهش نیاز کاذب.",
            "مطالعهٔ صنعت فرهنگ.",
            "تحلیل تسکین واپس‌راننده.",
            "پژوهش مدیریت الگوریتمی.",
            "مطالعهٔ تبلیغات تجاری.",
            "تحلیل گیمیفیکیشن.",
            "پژوهش زبان بوروکراتیک.",
            "مطالعهٔ بدن و مصرف.",
            "تحلیل رسانه و اعتراض.",
            "پژوهش اقتصاد توجه.",
            "مطالعهٔ آموزش کارآمدی.",
            "تحلیل هنر انتقادی.",
            "پژوهش شهر و مصرف.",
        ],
    ),
}

NAME_FIX = {}
YEAR_FIX = {
    "MC-333": "year corrected 1960 -> 1964 (verified anchor: Centre for Contemporary Cultural Studies founded at Birmingham in 1964); card had no documentation",
    "MC-339": "no year change; note: entity_type is SCHOOL but the subject is Neil Postman's 1985 book thesis, so it is documented as a school-of-thought position (media ecology); flagged for editorial reclassification, no entity_type change made",
    "MC-344": "no year change; verified anchor: Heidegger's Die Frage nach der Technik first published 1954 (English translation 1977)",
    "MC-472": "no year change; verified anchor: Marcuse, One-Dimensional Man, 1964",
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
                                       "verified": n_verified, "batch": 186}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH186 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
