# -*- coding: utf-8 -*-
"""Batch 190: card-479 (SCHOOL) + card-33, card-581, res-e081 (WORK)."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch190-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch190.json"

SCHOOL_MAPPING = {"entity_type": "SCHOOL", "content_type": "مکتب (School)", "needs_review": False}
WORK_MAPPING = {"entity_type": "WORK", "content_type": "اثر (Effect)", "needs_review": False}

S = {
    "card-479": [
        dict(kind="WEBSITE",
             title_en="Philosophy of Technology (Stanford Encyclopedia of Philosophy)",
             title_fa="فلسفهٔ تکنولوژی (دانشنامهٔ فلسفهٔ استنفورد)",
             authors="Stanford Encyclopedia of Philosophy", year=2026,
             publisher="Stanford Encyclopedia of Philosophy",
             doi=None,
             url="https://plato.stanford.edu/entries/technology/",
             language="en", isbn=None,
             citation="Stanford Encyclopedia of Philosophy. Philosophy of Technology. https://plato.stanford.edu/entries/technology/",
             locator="survey entry on the field and its approaches", locator_type="SECTION",
             supports="overview of the field, engineering versus humanities traditions, and central debates", verified=True),
        dict(kind="BOOK",
             title_en="Thinking Through Technology: The Path between Engineering and Philosophy",
             title_fa="اندیشیدن در فناوری: مسیر میان مهندسی و فلسفه",
             authors="Carl Mitcham", year=1994,
             publisher="University of Chicago Press",
             doi=None,
             url="https://archive.org/details/thinkingthrought0000mitc",
             language="en", isbn=None,
             citation="Mitcham, C. (1994). Thinking Through Technology: The Path between Engineering and Philosophy. Chicago: University of Chicago Press.",
             locator="chapters distinguishing engineering and humanities philosophy of technology", locator_type="CHAPTER",
             supports="the canonical distinction between engineering and humanities traditions in the philosophy of technology", verified=True),
    ],
    "card-33": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Network Externalities, Competition, and Compatibility",
             title_fa="اثرهای خارجی شبکه، رقابت و سازگاری",
             authors="Michael L. Katz; Carl Shapiro", year=1985,
             publisher="American Economic Review",
             doi=None,
             url="https://econpapers.repec.org/RePEc:aea:aecrev:v:75:y:1985:i:3:p:424-40",
             language="en", isbn=None,
             citation="Katz, M. L., & Shapiro, C. (1985). Network externalities, competition, and compatibility. American Economic Review, 75(3), 424-440.",
             locator="pp. 424-440", locator_type="PAGE",
             supports="formal economic account of network externalities, compatibility and competition", verified=True),
        dict(kind="WEBSITE",
             title_en="Network effect (Wikipedia entry)",
             title_fa="اثر شبکه‌ای (مدخل ویکی‌پدیا)",
             authors="Wikipedia contributors", year=2026,
             publisher="Wikipedia",
             doi=None,
             url="https://en.wikipedia.org/wiki/Network_effect",
             language="en", isbn=None,
             citation="Wikipedia contributors. Network effect. Wikipedia.",
             locator="definition, origins, critical mass and market tipping sections", locator_type="SECTION",
             supports="direct and indirect network effects, critical mass, market tipping and Metcalfe's law", verified=True),
    ],
    "card-581": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Boomerang Effect: A Synthesis of Findings and a Preliminary Theoretical Framework",
             title_fa="اثر بومرنگ: ترکیب یافته‌ها و چارچوب نظری مقدماتی",
             authors="Sara Byrne; P. Sol Hart", year=2009,
             publisher="Communication Yearbook (Taylor & Francis)",
             doi="10.1080/23808985.2009.11679083",
             url="https://www.tandfonline.com/doi/abs/10.1080/23808985.2009.11679083",
             language="en", isbn=None,
             citation="Byrne, S., & Hart, P. S. (2009). The boomerang effect: A synthesis of findings and a preliminary theoretical framework. Communication Yearbook, 33.",
             locator="review of boomerang findings and proposed framework", locator_type="SECTION",
             supports="systematic synthesis of boomerang effects and their theoretical mechanisms", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Boomerang Effects in Science Communication",
             title_fa="اثرهای بومرنگ در ارتباطات علم",
             authors="P. Sol Hart; Matthew C. Nisbet", year=2012,
             publisher="Communication Research (SAGE)",
             doi="10.1177/0093650211416646",
             url="https://journals.sagepub.com/doi/abs/10.1177/0093650211416646",
             language="en", isbn=None,
             citation="Hart, P. S., & Nisbet, M. C. (2012). Boomerang effects in science communication. Communication Research, 39(6).",
             locator="study on motivated reasoning and identity cues", locator_type="SECTION",
             supports="empirical evidence that identity cues can amplify polarization instead of persuading", verified=True),
    ],
    "res-e081bac707848a7377a4": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Communication Theory as a Field",
             title_fa="نظریهٔ ارتباطات به‌مثابه یک حوزه",
             authors="Robert T. Craig", year=1999,
             publisher="Communication Theory (Wiley)",
             doi="10.1111/j.1468-2885.1999.tb00355.x",
             url="https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1468-2885.1999.tb00355.x",
             language="en", isbn=None,
             citation="Craig, R. T. (1999). Communication theory as a field. Communication Theory, 9(2), 119-161.",
             locator="pp. 119-161", locator_type="PAGE",
             supports="the seven traditions of communication theory and the constitutive metamodel", verified=True),
        dict(kind="BOOK",
             title_en="Communication Theories: Origins, Methods, and Uses in the Mass Media",
             title_fa="نظریه‌های ارتباطات: خاستگاه‌ها، روش‌ها و کاربردها در رسانه‌های جمعی",
             authors="Werner J. Severin; James W. Tankard", year=1997,
             publisher="Longman",
             doi=None,
             url="https://archive.org/details/communicationthe0000seve_i0r9",
             language="en", isbn="0801317037",
             citation="Severin, W. J., & Tankard, J. W. (1997). Communication Theories: Origins, Methods, and Uses in the Mass Media. New York: Longman.",
             locator="survey chapters on media effects theories", locator_type="CHAPTER",
             supports="textbook survey linking theory origins, research methods and media applications", verified=True),
    ],
}

ENRICH = {
    "card-479": dict(
        year=1954,
        mapping=SCHOOL_MAPPING,
        summary="فلسفهٔ تکنولوژی حوزه‌ای پژوهشی است که پرسش‌های فلسفی دربارهٔ ماهیت، ساختار، معنا و پیامدهای فناوری را طرح می‌کند. کارل میچم این حوزه را به دو سنت تقسیم کرد: فلسفهٔ مهندسیِ فناوری که از درون مهندسی به تحلیل طراحی، کارکرد و مصنوع فنی می‌پردازد، و فلسفهٔ انسانیِ فناوری که از بیرون به نقد اخلاقی، سیاسی و فرهنگی فناوری می‌نشیند. پرسش‌های محوری آن عبارت‌اند از نسبت فناوری با علم، تفاوت مصنوع فنی و شیء طبیعی، نقش فناوری در شکل‌دهی به ادراک و کنش انسان، و مسئولیت در برابر پیامدهای آن. سنت‌های مختلف پاسخ‌های متفاوتی داده‌اند: ابزارگرایی فناوری را وسیلهٔ خنثی می‌داند، جوهری‌گرایی آن را نظامی خودمختار می‌بیند، نظریهٔ انتقادی آن را به مناسبات قدرت پیوند می‌زند، و پساپدیدارشناسی آن را میانجی رابطهٔ انسان و جهان می‌فهمد. مقالهٔ پرسش دربارهٔ فناوری هایدگر در ۱۹۵۴ از متون بنیان‌گذار این حوزه است. در مطالعات رسانه، این حوزه چارچوبی برای فهم رسانه به‌مثابه فناوری میانجی، نقد جبرگرایی فناورانه و ارزیابی اخلاقی فناوری‌های نوپدید فراهم می‌کند. نقدها بر تمرکز بر سنت غربی، انتزاعی‌بودن و کم‌توجهی به تجربهٔ جوامع غیرغربی تأکید دارند.",
        definition="فلسفهٔ تکنولوژی مطالعهٔ فلسفی ماهیت، ساختار، کارکرد و پیامدهای فناوری است و نسبت آن را با علم، اخلاق، سیاست و تجربهٔ انسانی می‌سنجد.",
        main_problem="فناوری چیست و چگونه رابطهٔ انسان با جهان، دانش، قدرت و مسئولیت اخلاقی را دگرگون می‌کند.",
        mechanism="مصنوع فنی با بازسازمان‌دهی کنش و ادراک، امکان‌های تازه می‌سازد و محدودیت‌های تازه تحمیل می‌کند؛ تحلیل فلسفی این میانجی‌گری را در طراحی، استفاده و پیامد اجتماعی می‌کاود.",
        assumptions=[
            "فناوری صرفاً ابزار خنثی نیست.",
            "مصنوع فنی ساختار کنش را شکل می‌دهد.",
            "طراحی فناوری ارزش‌های اخلاقی و سیاسی دارد.",
            "فناوری و جامعه یکدیگر را برمی‌سازند.",
            "تجربهٔ فناوری به بدن و ادراک گره خورده است.",
            "مسئولیت پیامدها را نمی‌توان به کاربر واگذاشت.",
            "سنت‌های مهندسی و انسانی مکمل‌اند.",
            "ارزیابی فناوری به داوری هنجاری نیاز دارد.",
        ],
        principles=[
            "فناوری را در بستر اجتماعی تحلیل کن.",
            "از جبرگرایی فناورانه بپرهیز.",
            "طراحی را تصمیم اخلاقی بدان.",
            "تجربهٔ کاربر و بدن را جدی بگیر.",
            "پیامدهای غیرقصدی را بسنج.",
            "تاریخ فناوری را در تحلیل بگنجان.",
            "گفت‌وگوی مهندسی و علوم انسانی را تقویت کن.",
        ],
        critiques=[
            "تمرکز بر سنت فلسفی غربی غالب است.",
            "تحلیل‌ها اغلب انتزاعی و کم‌پیوند با عمل‌اند.",
            "تجربهٔ جوامع غیرغربی کم‌رنگ می‌شود.",
            "مرز مهندسی و انسانی همیشه روشن نیست.",
            "سنجش تجربی مفاهیم آن دشوار است.",
            "به نابرابری دسترسی و قدرت کم می‌پردازد.",
            "سرعت تحول فناوری از تحلیل فلسفی جلو می‌زند.",
        ],
        critique_text="منتقدان می‌گویند فلسفهٔ تکنولوژی اغلب در سنت غربی و در سطح انتزاعی می‌ماند، تجربهٔ جوامع دیگر و نابرابری قدرت را کم‌رنگ می‌کند و سنجش تجربی مفاهیم آن دشوار است؛ با این حال چارچوبی ضروری برای نقد جبرگرایی و ارزیابی اخلاقی فناوری رسانه فراهم می‌کند.",
        applications=[
            "اخلاق هوش مصنوعی.",
            "نقد جبرگرایی فناورانه.",
            "تحلیل میانجی‌گری رسانه.",
            "اخلاق طراحی فناوری.",
            "مطالعهٔ حریم خصوصی دیجیتال.",
            "ارزیابی فناوری سلامت.",
            "پژوهش فناوری نظامی.",
            "تحلیل فناوری زیستی.",
            "مطالعهٔ شهر هوشمند.",
            "پژوهش فناوری پوشیدنی.",
            "تحلیل اتوماسیون کار.",
            "مطالعهٔ واقعیت مجازی.",
            "پژوهش انرژی و محیط‌زیست.",
            "سیاست‌گذاری فناوری.",
        ],
        example_text="عینک نمونهٔ سادهٔ میانجی‌گری فناوری است: ابزاری که نه صرفاً دید را تقویت می‌کند، بلکه شیوهٔ دیدن و نسبت بدن با جهان را بازتنظیم می‌کند؛ همین منطق در گوشی هوشمند به شکل‌دهی به توجه، حافظه و تعامل اجتماعی گسترش می‌یابد.",
        evolution="این حوزه از فلسفهٔ فناوری قرن نوزدهم و آثار ارنست کاپ آغاز شد، با هایدگر و الیول در میانهٔ قرن بیستم صورت جوهری یافت، در دههٔ ۱۹۸۰ با پساپدیدارشناسی و برساخت اجتماعی فناوری دگرگون شد، در دههٔ ۲۰۰۰ به اخلاق فناوری‌های نوپدید گرایید و امروز با هوش مصنوعی و داده گسترش یافته است.",
        key_concepts=["مصنوع فنی", "میانجی‌گری فناوری", "جبرگرایی فناورانه", "برساخت اجتماعی فناوری", "پساپدیدارشناسی", "اخلاق فناوری"],
        theorists="کارل میچم، دان آیدی، اندرو فینبرگ و پیتر-پل وربیک.",
        theorists_text="کارل میچم با تفکیک سنت مهندسی و انسانی، دان آیدی با پساپدیدارشناسی و تحلیل رابطهٔ انسان و فناوری، و اندرو فینبرگ و پیتر-پل وربیک با چرخش تجربی و اخلاقی، این حوزه را صورت‌بندی کردند.",
        model="مدل میانجی‌گری: فناوری در رابطهٔ انسان و جهان جای می‌گیرد، ادراک و کنش را شکل می‌دهد و در همان حال ارزش‌ها و مناسبات قدرت را در طراحی خود حمل می‌کند.",
        studies=[
            "پژوهش ماهیت مصنوع فنی.",
            "تحلیل میانجی‌گری رسانه.",
            "مطالعهٔ اخلاق هوش مصنوعی.",
            "پژوهش جبرگرایی فناورانه.",
            "تحلیل طراحی اخلاقی.",
            "مطالعهٔ حریم خصوصی دیجیتال.",
            "پژوهش فناوری سلامت.",
            "تحلیل فناوری نظامی.",
            "مطالعهٔ فناوری زیستی.",
            "پژوهش شهر هوشمند.",
            "تحلیل اتوماسیون کار.",
            "مطالعهٔ واقعیت مجازی.",
            "پژوهش انرژی و محیط‌زیست.",
            "تحلیل سیاست فناوری.",
        ],
    ),
    "card-33": dict(
        year=1985,
        mapping=WORK_MAPPING,
        summary="اثر شبکه‌ای پدیده‌ای اقتصادی است که در آن ارزش یک کالا یا خدمت برای هر کاربر با افزایش شمار کاربران سازگار افزایش می‌یابد. در اثر مستقیم، ارزش یک خدمت برای کاربران همان گروه با پیوستن کاربران بیشتر بالا می‌رود، مانند شبکهٔ تلفن یا پیام‌رسان. در اثر غیرمستقیم، ارزش یک گروه به رشد گروه دیگر وابسته است، مانند ارزش کنسول بازی به فراوانی بازی‌های سازگار یا ارزش پلتفرم رسانه‌ای به شمار تولیدکنندگان محتوا. مایکل کتز و کارل شپیرو در ۱۹۸۵ صورت‌بندی اقتصادی این پدیده را با تحلیل رقابت و سازگاری ارائه کردند و پژوهش‌های بعدی مفاهیم جرم بحرانی، نقطهٔ چرخش بازار و قفل‌شدگی را افزودند. قانون متکالف، ارزش شبکه را متناسب با مربع شمار کاربران می‌داند، هرچند این قاعده بیشتر شهودی است تا اندازه‌گیری دقیق. در رسانه و پلتفرم، اثر شبکه‌ای توضیح می‌دهد چگونه خدمات اندک‌شماری به سلطه می‌رسند، چرا سازگاری و استاندارد اهمیت دارد و چگونه بازارهای دوسویه یک سمت را ارزان یا رایگان نگه می‌دارند. نقدها بر بیش‌برآورد ارزش، نادیده‌گرفتن ازدحام و اثرهای منفی شبکه، اشباع بازار و کاهش قفل‌شدگی با چندپهلویی تأکید دارند.",
        definition="اثر شبکه‌ای افزایش ارزش یک کالا یا خدمت برای کاربران با افزایش شمار کاربران سازگار است و در دو شکل مستقیم و غیرمستقیم ظاهر می‌شود.",
        main_problem="چرا برخی بازارها به سلطهٔ یک بازیگر می‌رسند و چگونه می‌توان ارزش شبکه، جرم بحرانی و قفل‌شدگی را در طراحی خدمت و سیاست‌گذاری مدیریت کرد.",
        mechanism="با پیوستن هر کاربر تازه، شمار پیوندها و تعامل‌های ممکن افزایش می‌یابد و ارزش ادراک‌شده برای کاربران پیشین بالا می‌رود؛ این بازخورد مثبت پس از جرم بحرانی، پذیرش را به راهبرد غالب بدل می‌کند.",
        assumptions=[
            "ارزش خدمت به شمار کاربران وابسته است.",
            "کاربران به انتظار رشد شبکه پاسخ می‌دهند.",
            "سازگاری محصولات دامنهٔ شبکه را گسترش می‌دهد.",
            "پس از جرم بحرانی بازخورد مثبت غالب می‌شود.",
            "هزینهٔ جابه‌جایی کاربران در قفل‌شدگی اثر دارد.",
            "بازارهای دوسویه به تعادل قیمتی نیاز دارند.",
            "اثر شبکه‌ای در همهٔ بازارها یکسان نیست.",
            "ظرفیت شبکه می‌تواند به ازدحام بیانجامد.",
        ],
        principles=[
            "جرم بحرانی را پیش از رقابت هدف بگیر.",
            "سازگاری و استاندارد باز را جدی بگیر.",
            "ارزش پایه را پیش از رشد شبکه بساز.",
            "هزینهٔ جابه‌جایی را اخلاقی بسنج.",
            "اثرهای منفی ازدحام را مدیریت کن.",
            "بازار دوسویه را متعادل طراحی کن.",
            "قفل‌شدگی را با شواهد پایش کن.",
        ],
        critiques=[
            "قانون متکالف ارزش را بیش‌برآورد می‌کند.",
            "شمار کاربران معیار کافی برای ارزش نیست.",
            "ازدحام و اثرهای منفی شبکه کم‌رنگ می‌شود.",
            "قفل‌شدگی با چندپهلویی کاهش می‌یابد.",
            "رشد شبکه در اشباع بازار متوقف می‌شود.",
            "سوگیری به سمت پلتفرم‌های بزرگ را تقویت می‌کند.",
            "کيفيت تعامل و اعتماد را توضیح نمی‌دهد.",
        ],
        critique_text="منتقدان می‌گویند شمار کاربران به‌تنهایی ارزش شبکه را توضیح نمی‌دهد، قانون متکالف بیش‌برآورد می‌کند و ازدحام، اشباع و چندپهلویی، تصویر سادهٔ قفل‌شدگی را پیچیده می‌کند؛ با این حال اثر شبکه‌ای همچنان کلید فهم اقتصاد پلتفرم و سیاست سازگاری است.",
        applications=[
            "تحلیل اقتصاد پلتفرم.",
            "طراحی خدمات پیام‌رسان.",
            "مطالعهٔ شبکه‌های اجتماعی.",
            "سیاست‌گذاری سازگاری.",
            "تحلیل بازار کنسول بازی.",
            "پژوهش رسانهٔ جریانی.",
            "مطالعهٔ پرداخت دیجیتال.",
            "تحلیل بازار دوسویه.",
            "پژوهش اینترنت اشیا.",
            "مطالعهٔ نرم‌افزار اداری.",
            "تحلیل استاندارد باز.",
            "پژوهش حمل‌ونقل اشتراکی.",
            "مطالعهٔ تجارت الکترونیک.",
            "تحلیل رسانهٔ محلی.",
        ],
        example_text="پیام‌رسان نمونهٔ روشنی است: هر کاربر تازه شمار مخاطبان در دسترس دیگران را افزایش می‌دهد و جابه‌جایی به خدمتی با کاربران کمتر را پرهزینه می‌کند؛ همین منطق در پلتفرم‌های رسانه‌ای با پیوند میان مخاطب، تولیدکننده و تبلیغ‌دهنده پیچیده‌تر می‌شود.",
        evolution="اندیشهٔ اثر شبکه از تجربهٔ تلفن و نوشته‌های اوایل قرن بیستم ریشه گرفت، کتز و شپیرو در ۱۹۸۵ آن را صورت‌بندی اقتصادی کردند، در دههٔ ۱۹۹۰ با استانداردها و بازارهای فناوری گسترش یافت، در دههٔ ۲۰۰۰ با پلتفرم‌های آنلاین به محور اقتصاد دیجیتال بدل شد و امروز بحث سازگاری و تنظیم‌گری پلتفرم ادامه دارد.",
        key_concepts=["اثر مستقیم", "اثر غیرمستقیم", "جرم بحرانی", "قفل‌شدگی", "بازار دوسویه", "سازگاری"],
        theorists="مایکل کتز، کارل شپیرو و رابرت متکالف.",
        theorists_text="مایکل کتز و کارل شپیرو تحلیل اقتصادی اثرهای خارجی شبکه و رقابت سازگاری را بنیان گذاشتند و رابرت متکالف با صورت‌بندی شهودی ارزش متناسب با مربع کاربران، این ایده را به زبان صنعت فناوری آورد.",
        model="مدل بازخورد شبکه: ارزش برای هر کاربر با پیوستن کاربران سازگار بالا می‌رود؛ پس از جرم بحرانی پذیرش شتاب می‌گیرد و با هزینهٔ جابه‌جایی بالا، بازار به سمت یک بازیگر می‌چرخد.",
        studies=[
            "پژوهش اثرهای خارجی شبکه.",
            "تحلیل رقابت سازگاری.",
            "مطالعهٔ جرم بحرانی.",
            "پژوهش چرخش بازار.",
            "تحلیل قفل‌شدگی.",
            "مطالعهٔ بازار دوسویه.",
            "پژوهش اقتصاد پلتفرم.",
            "تحلیل شبکهٔ اجتماعی.",
            "مطالعهٔ بازار کنسول.",
            "پژوهش رسانهٔ جریانی.",
            "تحلیل پرداخت دیجیتال.",
            "مطالعهٔ استاندارد باز.",
            "پژوهش حمل‌ونقل اشتراکی.",
            "تحلیل تجارت الکترونیک.",
        ],
    ),
    "card-581": dict(
        year=1953,
        mapping=WORK_MAPPING,
        summary="اثر بومرنگ به پیامد معکوس پیام اقناعی اشاره دارد: پیامی که برای تغییر نگرش یا رفتار طراحی شده است، در برخی مخاطبان نگرش مخالف را تقویت می‌کند یا رفتار ناخواسته را برمی‌انگیزد. سازوکارهای توضیح‌دهندهٔ آن چندگانه‌اند: نظریهٔ واکنش روانی می‌گوید وقتی مخاطب آزادی خود را تهدیدشده می‌بیند، برای بازیابی آزادی در جهت مخالف پیام موضع می‌گیرد؛ سوگیری تأیید و استدلال انگیزشی باعث می‌شود پیام ناسازگار با هویت، رد یا وارونه تفسیر شود؛ قرار گرفتن گزینشی و اجتناب از پیام نیز اثر را تشدید می‌کند. سارا برن و پی. سال هارت در ۲۰۰۹ یافته‌های پژوهش بومرنگ را ترکیب کردند و چارچوبی مقدماتی برای شرایط بروز آن پیشنهادند. پژوهش هارت و نیسبت در ۲۰۱۲ نشان داد نشانه‌های هویتی در ارتباطات علم می‌تواند قطبی‌شدن را به‌جای کاهش، تقویت کند. این اثر در کمپین‌های سلامت، تبلیغات سیاسی منفی، برچسب‌های هشدار و تلاش برای اصلاح اطلاعات نادرست دیده شده است. نقدها بر ناهمگونی یافته‌ها، دشواری تکرار برخی نتایج، وابستگی اثر به زمینه و گروه مخاطب و خطر تعمیم افراطی تأکید دارند.",
        definition="اثر بومرنگ پیامد معکوس یک پیام اقناعی است؛ یعنی پیام به‌جای تغییر نگرش در جهت مقصود، نگرش مخالف را تقویت می‌کند یا رفتار ناخواسته را برمی‌انگیزد.",
        main_problem="چرا و در چه شرایطی پیام‌های اقناعی، به‌جای همراه‌کردن مخاطب، مقاومت او را برمی‌انگیزند و نگرش مخالف را تقویت می‌کنند.",
        mechanism="تهدید آزادی، پیام ناسازگار با هویت و تفسیر انگیزشی، مخاطب را به رد پیام یا موضع‌گیری مخالف سوق می‌دهد؛ هرچه پیام فشار بیشتری وارد کند، احتمال واکنش معکوس بیشتر می‌شود.",
        assumptions=[
            "مخاطب موجودی فعال و مقاوم است.",
            "تهدید آزادی به واکنش روانی می‌انجامد.",
            "هویت گروهی بر تفسیر پیام اثر می‌گذارد.",
            "پیام ناسازگار گزینشی پردازش می‌شود.",
            "شدت فشار پیام اثر معکوس را افزایش می‌دهد.",
            "اعتبار منبع بر پذیرش اثر می‌گذارد.",
            "بروز بومرنگ به زمینه وابسته است.",
            "اثر در همهٔ مخاطبان یکسان نیست.",
        ],
        principles=[
            "فشار اقناعی را متناسب نگه دار.",
            "به هویت و آزادی مخاطب احترام بگذار.",
            "منبع را معتبر و بی‌طرف نشان بده.",
            "پیام را با زبان مخاطب هم‌سو کن.",
            "پیش از کمپین، مقاومت را بسنج.",
            "اثر را با آزمون میدانی پایش کن.",
            "از تحقیر و برچسب‌زنی بپرهیز.",
        ],
        critiques=[
            "یافته‌ها ناهمگون و وابسته به زمینه‌اند.",
            "برخی نتایج بومرنگ در تکرار تأیید نشد.",
            "سنجش نگرش و رفتار اغلب ناهم‌خوان است.",
            "خطر تعمیم افراطی به همهٔ کمپین‌ها وجود دارد.",
            "سوگیری انتشار به سمت یافته‌های چشمگیر.",
            "مرز بومرنگ و بی‌اثری روشن نیست.",
            "عوامل ساختاری و رسانه‌ای کم‌رنگ می‌شوند.",
        ],
        critique_text="منتقدان می‌گویند اثر بومرنگ به زمینه و گروه مخاطب وابسته است، برخی یافته‌های آن در تکرار تأیید نشده و مرز آن با بی‌اثری روشن نیست؛ با این حال توجه به آن طراحی کمپین را از فرض سادهٔ «پیام بیشتر، اثر بیشتر» دور می‌کند.",
        applications=[
            "طراحی کمپین سلامت.",
            "ارتباطات تغییر اقلیم.",
            "تبلیغات سیاسی.",
            "اصلاح اطلاعات نادرست.",
            "برچسب هشدار محصول.",
            "ارتباطات بحران.",
            "کمپین واکسیناسیون.",
            "آموزش رسانه‌ای.",
            "روابط عمومی سازمانی.",
            "پیام‌های انتخاباتی.",
            "کمپین محیط‌زیست.",
            "ارتباطات سلامت عمومی.",
            "پیشگیری از مصرف دخانیات.",
            "پژوهش افکار عمومی.",
        ],
        example_text="کمپین هشدار دربارهٔ یک رفتار پرخطر که مخاطب را تحقیر یا تهدید کند، ممکن است در گروهی که آن رفتار را بخشی از هویت خود می‌داند، مقاومت برانگیزد و رفتار را تقویت کند؛ همین منطق در اصلاح باورهای نادرست سیاسی نیز دیده شده است.",
        evolution="پژوهش اقناع در دههٔ ۱۹۵۰ و ۱۹۶۰ به پیامدهای ناخواستهٔ پیام توجه کرد، نظریهٔ واکنش روانی در ۱۹۶۶ چارچوبی برای آن فراهم کرد، در دههٔ ۱۹۸۰ و ۱۹۹۰ پژوهش کمپین‌های سلامت آن را گسترد، برن و هارت در ۲۰۰۹ یافته‌ها را ترکیب کردند و در دههٔ ۲۰۱۰ بحث تکرارپذیری و شرایط مرزی آن شدت گرفت.",
        key_concepts=["واکنش روانی", "استدلال انگیزشی", "سوگیری تأیید", "هویت گروهی", "مقاومت پیام", "شرایط مرزی"],
        theorists="سارا برن، پی. سال هارت، جک برهم و متیو نیسبت.",
        theorists_text="جک برهم با نظریهٔ واکنش روانی سازوکار مرکزی بومرنگ را توضیح داد، سارا برن و پی. سال هارت یافته‌ها را ترکیب کردند و متیو نیسبت با پژوهش ارتباطات علم، نقش هویت را در تقویت قطب‌بندی نشان داد.",
        model="مدل واکنش معکوس: فشار اقناعی بالا، تهدید آزادی و ناسازگاری پیام با هویت، مقاومت را فعال می‌کند؛ نتیجه بسته به اعتبار منبع و زمینه، از بی‌اثری تا تقویت موضع مخالف متغیر است.",
        studies=[
            "پژوهش ترکیبی اثر بومرنگ.",
            "مطالعهٔ واکنش روانی.",
            "تحلیل کمپین سلامت.",
            "پژوهش ارتباطات اقلیم.",
            "مطالعهٔ تبلیغات سیاسی.",
            "تحلیل اصلاح اطلاعات نادرست.",
            "پژوهش برچسب هشدار.",
            "مطالعهٔ ارتباطات بحران.",
            "تحلیل کمپین واکسیناسیون.",
            "پژوهش آموزش رسانه‌ای.",
            "مطالعهٔ روابط عمومی.",
            "تحلیل پیام انتخاباتی.",
            "پژوهش کمپین محیط‌زیست.",
            "تحلیل افکار عمومی.",
        ],
    ),
    "res-e081bac707848a7377a4": dict(
        year=1999,
        mapping=WORK_MAPPING,
        summary="نظریه‌های ارتباطات مجموعه‌ای از چارچوب‌های نظام‌مندند که تولید، انتقال، دریافت و اثرهای ارتباط را توضیح می‌دهند. این حوزه از دو چشم‌انداز بنیادین آغاز می‌شود: چشم‌انداز انتقالی که ارتباط را انتقال پیام از فرستنده به گیرنده با هدف اثر می‌بیند، و چشم‌انداز آیینی که ارتباط را مشارکت در ساختن معنا و جامعه می‌فهمد. نظریه‌ها در سطوح میان‌فردی، گروهی، سازمانی و جمعی سازمان می‌یابند و تاریخ پژوهش اثرها از الگوی تزریقی به اثرهای محدود، استفاده و رضامندی، برجسته‌سازی، چارچوب‌بندی و کاشت حرکت کرده است. رابرت کریگ در ۱۹۹۹ با پیشنهاد الگوی فرانظری برسازنده، هفت سنت نظری را از هم تفکیک کرد: بلاغی، نشانه‌شناختی، پدیدارشناختی، سایبرنتیک، اجتماعی‌روانی، اجتماعی‌فرهنگی و انتقادی. کتاب‌های درسی مانند سورین و تنکارد نظریه‌ها را به خاستگاه، روش و کاربرد رسانه‌ای پیوند می‌دهند. در مطالعات رسانه، این نظریه‌ها ابزار تحلیل تولید محتوا، انتخاب مخاطب، شکل‌گیری معنا و اثرهای اجتماعی‌اند و در دههٔ اخیر نظریه‌های بوم‌شناسی رسانه، شبکه و داده نیز به این مجموعه افزوده شده‌اند. نقدها بر پراکندگی حوزه، غلبهٔ سنت غربی، شکاف نظریه و عمل و دشواری سنجش تجربی مفاهیم تأکید دارند.",
        definition="نظریه‌های ارتباطات مجموعه‌ای از چارچوب‌های نظام‌مند برای تبیین تولید، انتقال، تفسیر و اثرهای ارتباط در سطوح میان‌فردی تا جمعی است.",
        main_problem="چگونه می‌توان فرایند پیچیدهٔ ارتباط و اثرهای آن را در سطوح مختلف با چارچوب‌های نظام‌مند و آزمون‌پذیر تبیین کرد.",
        mechanism="نظریه‌ها با مفاهیم فرستنده، پیام، کانال، رمزگذاری، معنا، مخاطب و زمینه، سازوکار تولید و دریافت معنا را مدل می‌کنند و فرض‌های آزمون‌پذیر دربارهٔ اثر می‌سازند.",
        assumptions=[
            "ارتباط فرایندی نظام‌مند و مطالعه‌پذیر است.",
            "معنا در تعامل ساخته می‌شود.",
            "مخاطب فعال و تفسیرگر است.",
            "زمینه بر تولید و دریافت اثر می‌گذارد.",
            "سطوح ارتباط به هم پیوسته‌اند.",
            "نظریه باید با شواهد آزموده شود.",
            "سنت‌های نظری متکثرند.",
            "رسانه در شکل‌دهی معنا نقش دارد.",
        ],
        principles=[
            "سطح تحلیل را روشن کن.",
            "میان نظریه و روش پیوند بساز.",
            "تکثر سنت‌های نظری را جدی بگیر.",
            "مخاطب را فعال فرض کن.",
            "زمینهٔ فرهنگی را در تحلیل بگنجان.",
            "مفاهیم را آزمون‌پذیر کن.",
            "از تقلیل ارتباط به انتقال بپرهیز.",
        ],
        critiques=[
            "حوزه پراکنده و فاقد هستهٔ واحد است.",
            "غلبهٔ سنت غربی در نظریه‌ها دیده می‌شود.",
            "شکاف میان نظریه و عمل رسانه‌ای جدی است.",
            "سنجش تجربی برخی مفاهیم دشوار است.",
            "نظریه‌های اثر اغلب یک‌سویه‌اند.",
            "تغییر سریع رسانه از نظریه‌پردازی جلو می‌زند.",
            "مرز سنت‌های نظری همیشه روشن نیست.",
        ],
        critique_text="منتقدان می‌گویند حوزهٔ نظریه‌های ارتباطات پراکنده است، سنت غربی بر آن غلبه دارد و پیوند آن با عمل رسانه‌ای و سنجش تجربی مفاهیم ضعیف می‌ماند؛ با این حال این مجموعه زبان مشترکی برای تحلیل تولید، معنا و اثر رسانه فراهم می‌کند.",
        applications=[
            "تحلیل اثر رسانه.",
            "پژوهش مخاطب.",
            "مطالعهٔ تولید خبر.",
            "تحلیل چارچوب‌بندی.",
            "پژوهش برجسته‌سازی.",
            "مطالعهٔ کاشت.",
            "تحلیل ارتباطات سیاسی.",
            "پژوهش ارتباطات سلامت.",
            "مطالعهٔ ارتباطات سازمانی.",
            "تحلیل ارتباطات میان‌فرهنگی.",
            "پژوهش رسانهٔ اجتماعی.",
            "مطالعهٔ افکار عمومی.",
            "تحلیل تبلیغات.",
            "آموزش روزنامه‌نگاری.",
        ],
        example_text="تحلیل پوشش خبری یک اعتراض نمونهٔ پیوند نظریه و روش است: نظریهٔ چارچوب‌بندی نشان می‌دهد چگونه انتخاب زاویه و واژه‌ها تفسیر مخاطب را جهت می‌دهد و پژوهش تجربی این فرض را با مقایسهٔ متن و نگرش مخاطب می‌آزماید.",
        evolution="پژوهش ارتباطات در نیمهٔ اول قرن بیستم با مطالعهٔ تبلیغات و اقناع شکل گرفت، در دههٔ ۱۹۴۰ و ۱۹۵۰ اثرهای محدود و استفاده و رضامندی مطرح شد، در دههٔ ۱۹۷۰ برجسته‌سازی و کاشت گسترش یافت، در دههٔ ۱۹۸۰ چرخش انتقادی و فرهنگی قدرت گرفت و از دههٔ ۱۹۹۰ به بعد نظریه‌های رسانهٔ دیجیتال و شبکه افزوده شد.",
        key_concepts=["چشم‌انداز انتقالی", "چشم‌انداز آیینی", "سنت‌های هفت‌گانه", "اثرهای محدود", "چارچوب‌بندی", "مخاطب فعال"],
        theorists="رابرت کریگ، ورنر سورین، جیمز تنکارد و استیون لیتل‌جان.",
        theorists_text="رابرت کریگ با الگوی فرانظری و تفکیک هفت سنت، نقشهٔ حوزه را ترسیم کرد و سورین و تنکارد با پیوند خاستگاه، روش و کاربرد رسانه‌ای، نظریه‌ها را به پژوهش تجربی نزدیک کردند.",
        model="مدل چندسطحی: ارتباط در سطوح میان‌فردی تا جمعی بررسی می‌شود؛ در هر سطح، مفاهیم فرستنده، پیام، کانال، تفسیر و زمینه به کار می‌آیند و نظریه‌های اثر، فرض‌های آزمون‌پذیر می‌سازند.",
        studies=[
            "پژوهش اثر رسانه.",
            "تحلیل مخاطب.",
            "مطالعهٔ تولید خبر.",
            "پژوهش چارچوب‌بندی.",
            "تحلیل برجسته‌سازی.",
            "مطالعهٔ کاشت.",
            "پژوهش ارتباطات سیاسی.",
            "تحلیل ارتباطات سلامت.",
            "مطالعهٔ ارتباطات سازمانی.",
            "پژوهش ارتباطات میان‌فرهنگی.",
            "تحلیل رسانهٔ اجتماعی.",
            "مطالعهٔ افکار عمومی.",
            "پژوهش تبلیغات.",
            "تحلیل آموزش روزنامه‌نگاری.",
        ],
    ),
}

NAME_FIX = {}
YEAR_FIX = {
    "card-479": "no year change; verified anchor: Heidegger's Die Frage nach der Technik was published in 1954 (Vorträge und Aufsätze), a founding text of the field; Mitcham 1994 and the SEP survey document the field's later consolidation",
    "card-33": "no year change; verified anchor: Katz & Shapiro, American Economic Review 75(3), 1985, pp. 424-440",
    "card-581": "no year change; year 1953 marks the classic persuasion-research era; verified anchors for the effect's synthesis are Byrne & Hart 2009 and Hart & Nisbet 2012",
    "res-e081bac707848a7377a4": "year 1999 added (card previously had no year); verified anchor: Craig, Communication Theory 9(2), 1999, pp. 119-161, the field-mapping article used as the card's theoretical anchor",
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
                                       "verified": n_verified, "batch": 190}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH190 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
