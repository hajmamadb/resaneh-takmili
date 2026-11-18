# -*- coding: utf-8 -*-
"""Batch 187: MC-473, MC-476, MC-478 (SCHOOL) + MC-602 (LAW)."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch187-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch187.json"

SCHOOL_MAPPING = {"entity_type": "SCHOOL", "content_type": "مکتب فکری (School)", "needs_review": False}
LAW_MAPPING = {"entity_type": "LAW", "content_type": "قانون/قاعدهٔ تجربی (Law)", "needs_review": False}

S = {
    "MC-473": [
        dict(kind="BOOK",
             title_en="Understanding Media: The Extensions of Man",
             title_fa="شناخت رسانه: امتدادهای انسان",
             authors="Marshall McLuhan", year=1964,
             publisher="McGraw-Hill",
             doi=None,
             url="https://archive.org/details/understandingmed0000mclu",
             language="en", isbn=None,
             citation="McLuhan, M. (1964). Understanding Media: The Extensions of Man. New York: McGraw-Hill.",
             locator="chapter 2: Media Hot and Cold", locator_type="CHAPTER",
             supports="definition of hot and cool media by degree of definition and audience participation", verified=True),
        dict(kind="WEBSITE",
             title_en="Media, Hot and Cold: Introduction (International Journal of Communication, vol. 8)",
             title_fa="رسانه، گرم و سرد: درآمد (مجلهٔ بین‌المللی ارتباطات، جلد ۸)",
             authors="Dylan Mulvin, Jonathan Sterne (eds.)", year=2014,
             publisher="International Journal of Communication",
             doi=None,
             url="https://monoskop.org/images/a/a1/Mulvin_Dylan_Sterne_Jonathan_eds_IJoC_8_Media_Hot_and_Cold.pdf",
             language="en", isbn=None,
             citation="Mulvin, D., & Sterne, J. (Eds.). (2014). Media, Hot and Cold. International Journal of Communication, 8.",
             locator="special section introduction", locator_type="SECTION",
             supports="scholarly reassessment of McLuhan's hot/cold distinction and its reception", verified=True),
    ],
    "MC-476": [
        dict(kind="BOOK",
             title_en="Speed and Politics: An Essay on Dromology",
             title_fa="سرعت و سیاست: جستاری در درمولوژی",
             authors="Paul Virilio; trans. Mark Polizzotti", year=1977,
             publisher="Semiotext(e)",
             doi=None,
             url="https://archive.org/details/speedpolitics0000viri",
             language="en", isbn=None,
             citation="Virilio, P. (1977/2006). Speed and Politics: An Essay on Dromology (M. Polizzotti, Trans.). Los Angeles: Semiotext(e).",
             locator="essay on dromology", locator_type="SECTION",
             supports="speed as the organizing principle of political and technological power", verified=True),
        dict(kind="WEBSITE",
             title_en="The Politics of Speed: Paul Virilio's Dromology",
             title_fa="سیاست سرعت: درمولوژی پل ویریلیو",
             authors="A. Aykutalp", year=2017,
             publisher="PhilArchive",
             doi=None,
             url="https://philarchive.org/rec/AYKHSP-2",
             language="en", isbn=None,
             citation="Aykutalp, A. (2017). The Politics of Speed: Paul Virilio's Dromology. PhilArchive.",
             locator="discussion of dromology and dromocratic power", locator_type="SECTION",
             supports="scholarly exposition of Virilio's concepts of speed, dromology and power", verified=True),
    ],
    "MC-478": [
        dict(kind="BOOK",
             title_en="Soziologie: Untersuchungen über die Formen der Vergesellschaftung",
             title_fa="جامعه‌شناسی: پژوهش‌هایی در صورت‌های اجتماعی‌شدن",
             authors="Georg Simmel", year=1908,
             publisher="Duncker & Humblot",
             doi=None,
             url="https://www.ssoar.info/ssoar/handle/document/54620",
             language="de", isbn=None,
             citation="Simmel, G. (1908). Soziologie: Untersuchungen über die Formen der Vergesellschaftung. Leipzig: Duncker & Humblot.",
             locator="monograph record, 782 pp.", locator_type="SECTION",
             supports="formal sociology and the study of social forms including the stranger and social circles", verified=True),
        dict(kind="BOOK",
             title_en="Soziologie. Untersuchungen über die Formen der Vergesellschaftung (archive scan)",
             title_fa="جامعه‌شناسی: پژوهش‌هایی در صورت‌های اجتماعی‌شدن (نسخهٔ اسکن‌شده)",
             authors="Georg Simmel", year=1908,
             publisher="Duncker & Humblot",
             doi=None,
             url="https://archive.org/details/soziologieunters00simmrich",
             language="de", isbn=None,
             citation="Simmel, G. (1908). Soziologie. Leipzig: Duncker & Humblot. Internet Archive scan.",
             locator="full text scan", locator_type="SECTION",
             supports="primary text of Simmel's formal sociology", verified=True),
    ],
    "MC-602": [
        dict(kind="WEBSITE",
             title_en="Nielsen's Law of Internet Bandwidth",
             title_fa="قانون نیلسن دربارهٔ پهنای باند اینترنت",
             authors="Jakob Nielsen", year=1998,
             publisher="Nielsen Norman Group",
             doi=None,
             url="https://www.nngroup.com/articles/law-of-bandwidth/",
             language="en", isbn=None,
             citation="Nielsen, J. (1998). Nielsen's Law of Internet Bandwidth. Nielsen Norman Group.",
             locator="article, 4 April 1998 (updated figure set)", locator_type="SECTION",
             supports="high-end users' connection speed grows by 50 percent per year", verified=True),
        dict(kind="WEBSITE",
             title_en="Nielsen's Law of Internet Bandwidth (CircleID commentary)",
             title_fa="قانون نیلسن دربارهٔ پهنای باند اینترنت (تحلیل سرکل‌آی‌دی)",
             authors="K. Kilkki", year=2019,
             publisher="CircleID",
             doi=None,
             url="https://circleid.com/posts/20191119_nielsens_law_of_internet_bandwidth",
             language="en", isbn=None,
             citation="Kilkki, K. (2019). Nielsen's Law of Internet Bandwidth. CircleID.",
             locator="commentary on 1998 measurement (53 percent rounded to 50 percent)", locator_type="SECTION",
             supports="historical measurement basis and persistence of the law since 1998", verified=True),
    ],
}

ENRICH = {
    "MC-473": dict(
        year=1964,
        mapping=SCHOOL_MAPPING,
        summary="رسانهٔ سرد و گرم تقسیم‌بندی مشهور مارشال مکلوهان در کتاب شناخت رسانه در ۱۹۶۴ است که رسانه‌ها را بر پایهٔ میزان تعریف و مشارکت مخاطب دسته‌بندی می‌کند. رسانهٔ گرم دادهٔ حسی را با تعریف بالا و جزئیات فراوان به مخاطب می‌دهد و مجال کمی برای تکمیل و مشارکت باقی می‌گذارد؛ رادیو، سینما، عکس و چاپ نمونه‌های آن‌اند. رسانهٔ سرد برعکس، تعریف پایین و جزئیات کمتر دارد و مخاطب ناچار است برای کامل‌کردن معنا فعالانه مشارکت کند؛ تلویزیون، تلفن، گفتار و کمیک نمونه‌های آن‌اند. مکلوهان تلویزیون را رسانه‌ای سرد می‌داند که با تصویر کم‌جزئیات بیننده را به درون صحنه می‌کشد و همین ویژگی سیاست و آموزش را دگرگون می‌کند. این تقسیم‌بندی در دههٔ ۱۹۶۰ بحث‌های فراوانی برانگیخت و به نظریهٔ رسانه و بوم‌شناسی رسانه راه یافت. امروزه پژوهشگران آن را به رسانه‌های تعاملی و پلتفرم‌ها تعمیم داده‌اند و از آن برای تحلیل میزان درگیری کاربر استفاده می‌کنند. نقدها بر ساده‌سازی دوگانه، ابهام تعریف و جبرگرایی فناورانه تأکید دارند.",
        definition="رسانهٔ سرد و گرم تمایزی مکلوهانی است که رسانه‌ها را بر پایهٔ تعریف بالا و مشارکت پایین (گرم) در برابر تعریف پایین و مشارکت بالا (سرد) دسته‌بندی می‌کند.",
        main_problem="چگونه می‌توان توضیح داد که رسانه‌های مختلف، با میزان جزئیات و تعریفی که ارائه می‌دهند، درجهٔ مشارکت حسی و ذهنی مخاطب را متفاوت می‌سازند و تجربهٔ اجتماعی را دگرگون می‌کنند.",
        mechanism="رسانهٔ گرم حس غالب را اشباع می‌کند و مخاطب را تکمیل‌نشده رها نمی‌کند؛ رسانهٔ سرد با دادهٔ کم، حس‌های متعدد را درگیر می‌کند و مخاطب برای بستن شکاف معنا، خود فعالانه وارد می‌شود.",
        assumptions=[
            "رسانه امتداد حواس انسان است.",
            "میزان تعریف رسانه بر مشارکت اثر می‌گذارد.",
            "مخاطب در رسانهٔ سرد فعال‌تر است.",
            "شکل رسانه بر تجربهٔ اجتماعی اثر دارد.",
            "تلویزیون رسانه‌ای سرد است.",
            "چاپ و سینما رسانه‌هایی گرم‌اند.",
            "تغییر رسانه، تغییر حواس را در پی دارد.",
            "محتوای رسانه کمتر از شکل آن اهمیت دارد.",
        ],
        principles=[
            "میزان جزئیات رسانه را بسنج.",
            "مشارکت مخاطب را با شکل رسانه تحلیل کن.",
            "از دوگانهٔ ساده پرهیز کن.",
            "زمینهٔ تاریخی رسانه را ببین.",
            "اثر حواس را در تجربهٔ رسانه بررسی کن.",
            "رسانه را امتداد بدن و حس بدان.",
            "از جبرگرایی فناورانه دوری کن.",
        ],
        critiques=[
            "تمایز گرم و سرد بیش از اندازه ساده است.",
            "تعریف دو مفهوم مبهم و لغزان است.",
            "جبرگرایی فناورانه در تحلیل دیده می‌شود.",
            "شواهد تجربی کافی ارائه نمی‌شود.",
            "نمونه‌ها به رسانهٔ آنالوگ محدودند.",
            "نقش محتوا کم‌رنگ می‌شود.",
            "تعمیم به رسانهٔ دیجیتال روشن نیست.",
        ],
        critique_text="منتقدان می‌گویند دوگانهٔ گرم و سرد ساده‌سازی‌شده، تعریف‌های آن لغزان و تحلیل آن جبرگرایانه است؛ با این حال این تمایز پرسش مهمی دربارهٔ رابطهٔ شکل رسانه با درجهٔ مشارکت مخاطب پیش گذاشت که در پژوهش رسانهٔ تعاملی همچنان زنده است.",
        applications=[
            "تحلیل مشارکت مخاطب تلویزیون.",
            "مقایسهٔ رادیو و تلویزیون.",
            "پژوهش رسانهٔ تعاملی.",
            "تحلیل بازی ویدیویی.",
            "مطالعهٔ شبکه‌های اجتماعی.",
            "پژوهش آموزش با رسانه.",
            "تحلیل تبلیغات تصویری.",
            "مطالعهٔ سیاست تلویزیونی.",
            "پژوهش کمیک و فرهنگ بصری.",
            "تحلیل تلفن و گفت‌وگو.",
            "مطالعهٔ پلتفرم و تعامل.",
            "پژوهش حواس و رسانه.",
            "تحلیل واقعیت مجازی.",
            "مطالعهٔ خبر و تصویر.",
        ],
        example_text="مقایسهٔ یک برنامهٔ رادیویی و یک برنامهٔ تلویزیونی هم‌موضوع نشان می‌دهد شنوندهٔ رادیو باید صحنه را در ذهن بسازد و بینندهٔ تلویزیون صحنهٔ آماده را می‌گیرد؛ همین تفاوت، میزان مشارکت و شکل حافظهٔ مخاطب را تغییر می‌دهد.",
        evolution="مکلوهان این تمایز را در ۱۹۶۴ مطرح کرد، در دههٔ ۱۹۷۰ با نقد رسانه‌ای پیوند یافت، در دههٔ ۱۹۹۰ با رسانهٔ دیجیتال بازخوانی شد و امروز در تحلیل تعامل کاربر و طراحی تجربه به کار می‌رود.",
        key_concepts=["رسانهٔ گرم", "رسانهٔ سرد", "تعریف بالا و پایین", "مشارکت مخاطب", "امتداد انسان", "بوم‌شناسی رسانه"],
        theorists="مارشال مکلوهان.",
        theorists_text="مکلوهان در شناخت رسانه، رسانه را امتداد حواس انسان دانست و با تمایز گرم و سرد، رابطهٔ شکل رسانه با مشارکت مخاطب را صورت‌بندی کرد.",
        model="مدل دما: رسانهٔ گرم با جزئیات فراوان حس را اشباع می‌کند و مشارکت را کم می‌کند؛ رسانهٔ سرد با جزئیات کم، مخاطب را به تکمیل معنا فرا می‌خواند و درگیری او را افزایش می‌دهد.",
        studies=[
            "مقایسهٔ رادیو و تلویزیون.",
            "پژوهش مشارکت مخاطب.",
            "تحلیل بازی ویدیویی.",
            "مطالعهٔ شبکهٔ اجتماعی.",
            "پژوهش آموزش رسانه‌ای.",
            "تحلیل تبلیغات تصویری.",
            "مطالعهٔ سیاست تلویزیونی.",
            "پژوهش فرهنگ بصری.",
            "تحلیل تلفن و گفت‌وگو.",
            "مطالعهٔ تعامل پلتفرم.",
            "پژوهش حواس و رسانه.",
            "تحلیل واقعیت مجازی.",
            "مطالعهٔ خبر تصویری.",
            "پژوهش رسانهٔ تعاملی.",
        ],
    ),
    "MC-476": dict(
        year=1977,
        mapping=SCHOOL_MAPPING,
        summary="فناوری و تمدن در این کارت به اندیشهٔ پل ویریلیو دربارهٔ سرعت و دگرگونی تمدن اشاره دارد. ویریلیو با مفهوم درمولوژی یا علم سرعت نشان می‌دهد که تاریخ تمدن را نمی‌توان تنها با تولید و مالکیت فهمید، بلکه سرعت جابه‌جایی اطلاعات، انسان و سلاح، شکل اصلی قدرت است. او از انقلاب درمولوژیک سخن می‌گوید که در آن برتری با کسانی است که سریع‌تر می‌بینند، سریع‌تر تصمیم می‌گیرند و پیش از دیگران در صحنه حاضر می‌شوند. لجستیک ادراک، جنگ و سینما، شهر و پادشهر و تلویزیون زنده از موضوعات اوست. به باور ویریلیو هر فناوری در ذات خود حادثه‌ای را نیز حمل می‌کند و سرعت بی‌پایان، سیاست و دموکراسی را به بحران می‌برد. این اندیشه بر نظریهٔ رسانه، مطالعات جنگ و امنیت، معماری و شهر و نقد فناوری اثر گذاشته است. نوشته‌های او بیشتر جستار فلسفی‌اند و کمتر به دادهٔ تجربی تکیه می‌کنند. نقدها بر سبک قصیده‌وار، جبرگرایی سرعت و کمبود شواهد تأکید دارند.",
        definition="فناوری و تمدن در خوانش ویریلیو مطالعهٔ سرعت به‌عنوان بنیاد قدرت و تمدن است؛ درمولوژی نشان می‌دهد چگونه فناوری‌های سرعت، ادراک، سیاست و جنگ را بازسازمان‌دهی می‌کنند.",
        main_problem="چگونه می‌توان توضیح داد که سرعت جابه‌جایی اطلاعات و نیرو، بیش از مالکیت ابزار تولید، سلسله‌مراتب قدرت و شکل تمدن را در دوران مدرن تعیین می‌کند.",
        mechanism="فناوری‌های سرعت، فاصله و زمان را فشرده می‌کنند؛ برتری به کسی می‌رسد که زودتر در صحنه حاضر شود و ادراک را سازمان دهد؛ در نتیجه سیاست به مدیریت جریان‌ها و جنگ به مسابقهٔ سرعت بدل می‌شود.",
        assumptions=[
            "سرعت بنیاد قدرت است.",
            "فاصله و زمان با فناوری فشرده می‌شوند.",
            "ادراک با لجستیک سازمان می‌یابد.",
            "هر فناوری حادثهٔ درونی خود را دارد.",
            "جنگ و رسانه به هم پیوسته‌اند.",
            "شهر با سرعت ارتباط بازسازمان می‌شود.",
            "دموکراسی با بی‌درنگی آسیب می‌بیند.",
            "تاریخ را باید با سرعت خواند.",
        ],
        principles=[
            "سرعت را در تحلیل قدرت بگنجان.",
            "لجستیک ادراک را بررسی کن.",
            "حادثهٔ درونی فناوری را ببین.",
            "پیوند جنگ و رسانه را جدی بگیر.",
            "زمان واقعی را از زمان تقویمی جدا کن.",
            "از پیشرفت خطی پرهیز کن.",
            "شهر را با جریان‌ها بخوان.",
        ],
        critiques=[
            "سبک نوشتار قصیده‌وار و پراکنده است.",
            "جبرگرایی سرعت جای تحلیل نهادی را می‌گیرد.",
            "شواهد تجربی و داده ارائه نمی‌شود.",
            "تمرکز بر تجربهٔ اروپا و جنگ غالب است.",
            "مفهوم درمولوژی بیش از اندازه گسترده است.",
            "راه‌حل سیاسی روشنی پیشنهاد نمی‌شود.",
            "نقش کنشگران اجتماعی کم‌رنگ می‌ماند.",
        ],
        critique_text="منتقدان می‌گویند سبک قصیده‌وار، جبرگرایی سرعت و کمبود شواهد تجربی، تحلیل ویریلیو را در برابر نقد آسیب‌پذیر می‌کند؛ با این حال او پیش از فراگیری رسانهٔ بلادرنگ، پیوند سرعت، ادراک و قدرت را به پرسش اصلی تمدن بدل کرد.",
        applications=[
            "تحلیل رسانهٔ بلادرنگ.",
            "مطالعهٔ جنگ و ارتباطات.",
            "پژوهش امنیت و سرعت.",
            "تحلیل شهر و تحرک.",
            "مطالعهٔ لجستیک.",
            "پژوهش نظارت و کنترل.",
            "تحلیل ترافیک داده.",
            "مطالعهٔ معماری و فاصله.",
            "پژوهش فناوری نظامی.",
            "تحلیل خبر فوری.",
            "مطالعهٔ بازار مالی.",
            "پژوهش حمل‌ونقل.",
            "تحلیل هوش مصنوعی بلادرنگ.",
            "مطالعهٔ گردشگری و سرعت.",
        ],
        example_text="تحلیل پوشش زندهٔ یک بحران نشان می‌دهد که چگونه تصویر بلادرنگ پیش از تصمیم سیاسی به مخاطب می‌رسد و مدیران را زیر فشار زمان قرار می‌دهد؛ این نمونه، پیوند سرعت، ادراک و قدرت را در عمل آشکار می‌کند.",
        evolution="ویریلیو درمولوژی را در ۱۹۷۷ صورت‌بندی کرد، در دههٔ ۱۹۸۰ به جنگ و سینما پرداخت، در دههٔ ۱۹۹۰ با اینترنت و زمان واقعی روبه‌رو شد و امروز در تحلیل پلتفرم‌های بلادرنگ و فناوری نظامی بازخوانی می‌شود.",
        key_concepts=["درمولوژی", "سرعت", "لجستیک ادراک", "حادثهٔ فناوری", "زمان واقعی", "قدرت"],
        theorists="پل ویریلیو.",
        theorists_text="پل ویریلیو با مفهوم درمولوژی، سرعت را بنیاد قدرت و تمدن دانست و پیوند جنگ، رسانه و ادراک را در آثار خود گسترد.",
        model="مدل درمولوژیک: قدرت با توان جابه‌جایی و سازمان‌دهی سرعت سنجیده می‌شود؛ فناوری‌های سرعت فاصله را حذف می‌کنند و سیاست را به مدیریت زمان واقعی بدل می‌سازند.",
        studies=[
            "تحلیل رسانهٔ بلادرنگ.",
            "پژوهش جنگ و سینما.",
            "مطالعهٔ امنیت و سرعت.",
            "تحلیل تحرک شهری.",
            "پژوهش لجستیک نظامی.",
            "مطالعهٔ نظارت و کنترل.",
            "تحلیل ترافیک داده.",
            "پژوهش معماری و فاصله.",
            "مطالعهٔ فناوری نظامی.",
            "تحلیل خبر فوری.",
            "پژوهش بازار مالی.",
            "مطالعهٔ حمل‌ونقل.",
            "تحلیل هوش مصنوعی بلادرنگ.",
            "پژوهش گردشگری و سرعت.",
        ],
    ),
    "MC-478": dict(
        year=1908,
        mapping=SCHOOL_MAPPING,
        summary="زیمل و جامعه‌شناسی صورت‌ها به سنت صورت‌گرایی گئورگ زیمل بازمی‌گردد که در کتاب جامعه‌شناسی در ۱۹۰۸ صورت‌بندی شد. زیمل پیشنهاد می‌کند جامعه‌شناسی به جای محتوای کنش، صورت‌های پایدار رابطهٔ اجتماعی را مطالعه کند: دوگانه، سه‌گانه، غریبه، راز، مد، محافل اجتماعی و شهر. به باور او فاصله و نزدیکی اجتماعی مقولاتی هستند که تجربهٔ مدرن را سازمان می‌دهند و رسانه‌ها یکی از صورت‌های نهادینهٔ همین فاصله‌اند. مقالهٔ کلان‌شهر و حیات ذهنی نشان می‌دهد چگونه تراکم و پول، نگرش بی‌تفاوت و محتاط شهرنشین را می‌سازد. زیمل با تحلیل مد و تغییر سریع آن، منطق تقلید و تمایز را در فرهنگ مصرفی توضیح می‌دهد. صورت‌گرایی او بر مکتب شیکاگو، کنش متقابل نمادین، تحلیل شبکهٔ اجتماعی و جامعه‌شناسی رسانه اثر گذاشته است. غریبه و راز او چارچوبی برای فهم حریم خصوصی و ناشناختگی در رسانهٔ امروز فراهم می‌کند. نقدها بر انتزاع صورت‌ها، روش ژورنالیستی و کمبود شواهد نظام‌مند تأکید دارند.",
        definition="زیمل و جامعه‌شناسی صورت‌ها مکتبی است که به جای محتوای کنش، صورت‌های پایدار رابطهٔ اجتماعی مانند غریبه، راز، مد و گروه را موضوع جامعه‌شناسی قرار می‌دهد.",
        main_problem="چگونه می‌توان جامعه‌شناسی را از توصیف محتوای تاریخی کنش آزاد کرد و صورت‌های تکرارشوندهٔ رابطهٔ اجتماعی را که در همهٔ جوامع دیده می‌شوند شناسایی و تحلیل کرد.",
        mechanism="صورت‌های اجتماعی از محتوای انگیزه‌ها و اهداف جدا می‌شوند و به‌عنوان قالب‌های پایدار تحلیل می‌شوند؛ فاصله، اندازهٔ گروه، راز و مد، الگوهای تعامل را سازمان می‌دهند و تجربهٔ مدرن را شکل می‌دهند.",
        assumptions=[
            "جامعه‌شناسی صورت‌ها را مطالعه می‌کند.",
            "صورت‌های اجتماعی از محتوا جدا شدنی‌اند.",
            "فاصله و نزدیکی، مقولات بنیادین‌اند.",
            "اندازهٔ گروه بر تعامل اثر می‌گذارد.",
            "راز و حریم، سازوکار حفظ فاصله‌اند.",
            "مد منطق تقلید و تمایز دارد.",
            "تجربهٔ شهری نگرش مدرن می‌سازد.",
            "صورت‌ها در فرهنگ‌های مختلف تکرار می‌شوند.",
        ],
        principles=[
            "صورت را از محتوا جدا کن.",
            "اندازهٔ گروه را در تحلیل بگنجان.",
            "فاصلهٔ اجتماعی را بسنج.",
            "راز و حریم را جدی بگیر.",
            "مد را به‌عنوان صورت تحلیل کن.",
            "تجربهٔ شهری را زمینه بگذار.",
            "از توصیف صرف فراتر برو.",
        ],
        critiques=[
            "صورت‌گرایی بیش از اندازه انتزاعی است.",
            "روش بیشتر جستاری و ژورنالیستی است.",
            "شواهد نظام‌مند تجربی کم است.",
            "بافت تاریخی و اقتصادی کم‌رنگ می‌شود.",
            "مفاهیم برای سنجش کمی دشوارند.",
            "تمرکز بر زندگی شهری اروپایی غالب است.",
            "پیوند نظریه با سیاست‌گذاری روشن نیست.",
        ],
        critique_text="منتقدان می‌گویند انتزاع صورت‌ها، روش جستاری و کمبود شواهد نظام‌مند، دقت تجربی این سنت را محدود می‌کند؛ با این حال مفاهیم غریبه، فاصله و راز، چارچوبی ماندگار برای فهم تعامل در رسانه و شهر فراهم کرده‌اند.",
        applications=[
            "تحلیل غریبه در شبکهٔ اجتماعی.",
            "مطالعهٔ حریم خصوصی آنلاین.",
            "پژوهش مد و مصرف.",
            "تحلیل اندازهٔ گروه در پیام‌رسان.",
            "مطالعهٔ حیات شهری.",
            "پژوهش ناشناختگی آنلاین.",
            "تحلیل محافل اجتماعی.",
            "مطالعهٔ راز و افشا.",
            "پژوهش فاصلهٔ اجتماعی.",
            "تحلیل مد و تمایز.",
            "مطالعهٔ کنش متقابل نمادین.",
            "پژوهش شبکهٔ دوستی.",
            "تحلیل مهاجرت و غربت.",
            "مطالعهٔ فرهنگ مصرفی.",
        ],
        example_text="کاربری که در شبکهٔ اجتماعی با نام مستعار فعالیت می‌کند، صورت امروزی غریبهٔ زیمل است: نزدیک به دیگران اما در فاصله‌ای کنترل‌شده؛ تحلیل این وضع با مفاهیم فاصله و راز، پویایی اعتماد و افشا را روشن می‌کند.",
        evolution="زیمل مفاهیم خود را در دههٔ ۱۹۰۰ صورت‌بندی کرد، کتاب جامعه‌شناسی در ۱۹۰۸ منتشر شد، صورت‌گرایی او در مکتب شیکاگو و کنش متقابل نمادین ادامه یافت، در تحلیل شبکهٔ اجتماعی بازخوانی شد و امروز در مطالعهٔ تعامل دیجیتال به کار می‌رود.",
        key_concepts=["صورت اجتماعی", "غریبه", "فاصلهٔ اجتماعی", "راز", "مد", "سه‌گانه"],
        theorists="گئورگ زیمل.",
        theorists_text="زیمل با صورت‌گرایی، غریبه، راز و مد، صورت‌های پایدار تعامل را از محتوای تاریخی کنش جدا کرد و راهی تازه برای جامعه‌شناسی گشود.",
        model="مدل صورت‌گرایی: انگیزه‌ها محتوای کنش‌اند و صورت‌ها قالب‌های پایدار رابطه؛ تحلیل جامعه‌شناختی با انتزاع صورت از محتوا، الگوهای تکرارشوندهٔ فاصله و تمایز را آشکار می‌کند.",
        studies=[
            "تحلیل غریبهٔ زیمل.",
            "پژوهش حریم خصوصی.",
            "مطالعهٔ مد و مصرف.",
            "تحلیل اندازهٔ گروه.",
            "پژوهش حیات شهری.",
            "مطالعهٔ ناشناختگی آنلاین.",
            "تحلیل محافل اجتماعی.",
            "پژوهش راز و افشا.",
            "مطالعهٔ فاصلهٔ اجتماعی.",
            "تحلیل کنش متقابل نمادین.",
            "پژوهش شبکهٔ دوستی.",
            "مطالعهٔ مهاجرت و غربت.",
            "تحلیل فرهنگ مصرفی.",
            "پژوهش سه‌گانه و اتحاد.",
        ],
    ),
    "MC-602": dict(
        year=1998,
        mapping=LAW_MAPPING,
        summary="قانون نیلسن یک قاعدهٔ تجربی دربارهٔ رشد پهنای باند اینترنت است که یاکوب نیلسن در ۱۹۹۸ صورت‌بندی کرد. بر پایهٔ این قانون، سرعت اتصال کاربران پیشرو سالانه حدود پنجاه درصد رشد می‌کند و این رشد از دههٔ ۱۹۸۰ تا امروز با نوسان ادامه داشته است. نیلسن این قاعده را از داده‌های تاریخی سرعت دسترسی استخراج کرد و آن را با قانون مور مقایسه کرد؛ در حالی که قدرت پردازش تقریباً هر هجده ماه دو برابر می‌شود، پهنای باند کاربران پیشرو شتابی مشابه یا بیشتر دارد. پیامد طراحی این است که خدمات وب باید برای پهنای باند آینده طراحی شوند نه وضع موجود، چون کاربران به‌سرعت به تجربهٔ غنی‌تر عادت می‌کنند. این قانون در برنامه‌ریزی شبکه، توسعهٔ ویدئو و خدمات ابری به کار می‌رود. نقدها بر تمرکز بر کاربران پیشرو، تفاوت رشد بی‌سیم و ثابت و نابرابری دسترسی تأکید دارند.",
        definition="قانون نیلسن قاعده‌ای تجربی است که می‌گوید سرعت اتصال کاربران پیشرو اینترنت سالانه حدود پنجاه درصد افزایش می‌یابد.",
        main_problem="چگونه می‌توان نیاز آیندهٔ کاربران به پهنای باند را پیش‌بینی کرد و طراحی خدمات شبکه را با سرعت رشد واقعی دسترسی هم‌گام ساخت.",
        mechanism="داده‌های تاریخی سرعت اتصال کاربران پیشرو نشان می‌دهد رشد سالانه حدود پنجاه درصد است؛ طراح اگر بر پایهٔ این روند آینده‌نگر باشد، ظرفیت و تجربهٔ خدمت را پیش از رسیدن تقاضا آماده می‌کند.",
        assumptions=[
            "سرعت دسترسی کاربران پیشرو روندی پایدار دارد.",
            "رشد پهنای باند با رشد قدرت پردازش قابل مقایسه است.",
            "کاربران به تجربهٔ غنی‌تر عادت می‌کنند.",
            "آینده‌نگری طراحی از وضع موجود مهم‌تر است.",
            "دادهٔ تاریخی مبنای پیش‌بینی است.",
            "ظرفیت شبکه باید پیش از تقاضا آماده شود.",
            "کاربران پیشرو جهت آیندهٔ عموم را نشان می‌دهند.",
            "رشد فناوری ناهم‌گون است.",
        ],
        principles=[
            "برای پهنای باند آینده طراحی کن.",
            "روند تاریخی را پایش کن.",
            "کاربران پیشرو را از عموم جدا کن.",
            "ظرفیت را پیش از تقاضا بساز.",
            "تفاوت شبکهٔ ثابت و بی‌سیم را ببین.",
            "نابرابری دسترسی را در سیاست لحاظ کن.",
            "پیش‌بینی را با داده به‌روز کن.",
        ],
        critiques=[
            "فقط کاربران پیشرو را می‌سنجد.",
            "رشد بی‌سیم با روند ثابت تفاوت دارد.",
            "میانگین پنهان، نابرابری دسترسی را می‌پوشاند.",
            "کاهش شتاب رشد در دههٔ ۲۰۲۰ بحث‌برانگیز است.",
            "قانون توصیفی است نه تبیینی.",
            "به کیفیت تجربه و تأخیر توجه ندارد.",
            "برای کشورهای در حال توسعه تعمیم‌پذیر نیست.",
        ],
        critique_text="منتقدان می‌گویند تمرکز بر کاربران پیشرو، نادیده‌گرفتن شکاف دسترسی و تفاوت شبکهٔ بی‌سیم، کاربرد سیاستی این قانون را محدود می‌کند؛ با این حال قانون نیلسن همچنان چارچوبی ساده و کارآمد برای پیش‌بینی تقاضای پهنای باند و برنامه‌ریزی زیرساخت است.",
        applications=[
            "برنامه‌ریزی ظرفیت شبکه.",
            "طراحی سرویس ویدئو.",
            "توسعهٔ خدمات ابری.",
            "سیاست‌گذاری دسترسی پرسرعت.",
            "تحلیل آموزش آنلاین.",
            "پژوهش بازی آنلاین.",
            "طراحی تجربهٔ وب.",
            "مطالعهٔ اینترنت اشیا.",
            "تحلیل پخش زنده.",
            "پژوهش زیرساخت مخابرات.",
            "برنامه‌ریزی شهر هوشمند.",
            "تحلیل کار از راه دور.",
            "پژوهش شکاف دیجیتال.",
            "طراحی مرکز داده.",
        ],
        example_text="شرکتی که سرویس ویدئویی طراحی می‌کند، کیفیت پخش را برای پهنای باند دو سال آینده تنظیم می‌کند نه سرعت میانگین امروز؛ نتیجه آن است که کاربران هنگام ارتقای اتصال، بدون بازطراحی، تجربهٔ بهتری می‌گیرند.",
        evolution="نیلسن قانون را در ۱۹۹۸ بر پایهٔ داده‌های دههٔ ۱۹۸۰ و ۱۹۹۰ منتشر کرد، در دههٔ ۲۰۰۰ با رشد پهنای باند ثابت تأیید شد، در دههٔ ۲۰۱۰ با موبایل و ویدئوی جریانی بازآزمایی شد و امروز با بحث دربارهٔ کندی رشد و شکاف دسترسی ادامه دارد.",
        key_concepts=["پهنای باند", "کاربر پیشرو", "رشد نمایی", "قانون مور", "ظرفیت شبکه", "شکاف دیجیتال"],
        theorists="یاکوب نیلسن.",
        theorists_text="یاکوب نیلسن با تحلیل داده‌های تاریخی سرعت اتصال، قانون رشد پنجاه درصدی پهنای باند را صورت‌بندی کرد و آن را به تصمیم‌های طراحی وب پیوند داد.",
        model="مدل رشد پهنای باند: سرعت کاربران پیشرو سالانه حدود پنجاه درصد رشد می‌کند؛ طراحی آینده‌نگر ظرفیت را پیش از تقاضا آماده می‌کند و تجربهٔ کاربر را با روند رشد هم‌گام می‌سازد.",
        studies=[
            "پایش روند پهنای باند.",
            "تحلیل سرویس ویدئو.",
            "پژوهش خدمات ابری.",
            "مطالعهٔ آموزش آنلاین.",
            "تحلیل بازی آنلاین.",
            "پژوهش تجربهٔ وب.",
            "مطالعهٔ اینترنت اشیا.",
            "تحلیل پخش زنده.",
            "پژوهش زیرساخت مخابرات.",
            "مطالعهٔ شهر هوشمند.",
            "تحلیل کار از راه دور.",
            "پژوهش شکاف دیجیتال.",
            "تحلیل مرکز داده.",
            "مطالعهٔ رشد موبایل.",
        ],
    ),
}

NAME_FIX = {}
YEAR_FIX = {
    "MC-473": "no year change; verified anchor: McLuhan, Understanding Media, 1964, chapter 2 Media Hot and Cold",
    "MC-476": "year added 1977 (verified anchor: Virilio, Vitesse et politique, 1977; English Speed and Politics, 1986/2006); card had no year value; card theorist Paul Virilio confirms the dromology framing",
    "MC-478": "no year change; verified anchor: Simmel, Soziologie, Duncker & Humblot, 1908 (SSOAR record)",
    "MC-602": "no year change; verified anchor: Nielsen, Nielsen's Law of Internet Bandwidth, published 4 April 1998 (Nielsen Norman Group)",
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
                                       "verified": n_verified, "batch": 187}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH187 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
