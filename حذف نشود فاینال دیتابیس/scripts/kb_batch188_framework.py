# -*- coding: utf-8 -*-
"""Batch 188: MC-603, MC-604, MC-605 (LAW) + MC-151 (STRATEGY)."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch188-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch188.json"

LAW_MAPPING = {"entity_type": "LAW", "content_type": "قانون/قاعدهٔ تجربی (Law)", "needs_review": False}
STRATEGY_MAPPING = {"entity_type": "STRATEGY", "content_type": "استراتژی (Strategy)", "needs_review": False}

S = {
    "MC-603": [
        dict(kind="OTHER",
             title_en="Cramming More Components Onto Integrated Circuits (Electronics, 1965)",
             title_fa="چپاندن اجزای بیشتر در مدارهای مجتمع (الکترونیکس، ۱۹۶۵)",
             authors="Gordon E. Moore", year=1965,
             publisher="Electronics",
             doi=None,
             url="https://www.cs.utexas.edu/~fussell/courses/cs352h/papers/moore.pdf",
             language="en", isbn=None,
             citation="Moore, G. E. (1965, April 19). Cramming more components onto integrated circuits. Electronics, 38(8), 114-117.",
             locator="full article, pp. 114-117", locator_type="PAGE",
             supports="original prediction that component counts on integrated circuits double at a regular pace", verified=True),
        dict(kind="WEBSITE",
             title_en="1965: Moore's Law Predicts the Future of Integrated Circuits",
             title_fa="۱۹۶۵: قانون مور آیندهٔ مدارهای مجتمع را پیش‌بینی می‌کند",
             authors="Computer History Museum", year=2026,
             publisher="Computer History Museum",
             doi=None,
             url="https://www.computerhistory.org/siliconengine/moores-law-predicts-the-future-of-integrated-circuits/",
             language="en", isbn=None,
             citation="Computer History Museum. 1965: Moore's Law Predicts the Future of Integrated Circuits. Silicon Engine.",
             locator="Silicon Engine exhibit entry", locator_type="SECTION",
             supports="publication of the 1965 Electronics article on April 19, 1965", verified=True),
    ],
    "MC-604": [
        dict(kind="WEBSITE",
             title_en="Gilder's Law (NetLingo definition)",
             title_fa="قانون گیندر (تعریف نت‌لینگو)",
             authors="NetLingo", year=2026,
             publisher="NetLingo",
             doi=None,
             url="https://www.netlingo.com/word/gilders-law.php",
             language="en", isbn=None,
             citation="NetLingo. Gilder's Law. NetLingo dictionary of Internet terms.",
             locator="dictionary entry", locator_type="SECTION",
             supports="bandwidth grows at least three times faster than computer power", verified=True),
        dict(kind="WEBSITE",
             title_en="The Twenty Laws of the Telecosm",
             title_fa="بیست قانون تله‌کازم",
             authors="Ray Kurzweil (ed.)", year=2001,
             publisher="Kurzweil Library",
             doi=None,
             url="https://www.writingsbyraykurzweil.com/the-twenty-laws-of-the-telecosm",
             language="en", isbn=None,
             citation="Kurzweil, R. (Ed.). (2001). The Twenty Laws of the Telecosm. Kurzweil Library.",
             locator="law 2: Gilder's Law", locator_type="SECTION",
             supports="restatement of Gilder's Law alongside Moore's Law in the telecosm framework", verified=True),
    ],
    "MC-605": [
        dict(kind="WEBSITE",
             title_en="IFTF Ten-Year Forecast: Amara's Law",
             title_fa="پیش‌بینی ده‌سالهٔ مؤسسهٔ آینده: قانون آمارا",
             authors="Institute for the Future", year=2026,
             publisher="Institute for the Future",
             doi=None,
             url="https://www.iftf.org/projects/iftf-ten-year-forecast-urgent-futures-perspectives/",
             language="en", isbn=None,
             citation="Institute for the Future. Amara's Law. IFTF Ten-Year Forecast.",
             locator="statement attributed to Roy Amara, 1973", locator_type="SECTION",
             supports="Amara coined the observation in 1973 as IFTF president", verified=True),
        dict(kind="WEBSITE",
             title_en="Roy Amara (Wikipedia entry)",
             title_fa="روی آمارا (مدخل ویکی‌پدیا)",
             authors="Wikipedia contributors", year=2026,
             publisher="Wikipedia",
             doi=None,
             url="https://en.wikipedia.org/wiki/Roy_Amara",
             language="en", isbn=None,
             citation="Wikipedia contributors. Roy Amara. Wikipedia.",
             locator="biography and Amara's Law section", locator_type="SECTION",
             supports="biographical identification of Roy Amara as futurist and IFTF president associated with the law", verified=True),
    ],
    "MC-151": [
        dict(kind="BOOK",
             title_en="Competitive Strategy: Techniques for Analyzing Industries and Competitors",
             title_fa="استراتژی رقابتی: فنون تحلیل صنایع و رقبا",
             authors="Michael E. Porter", year=1980,
             publisher="Free Press",
             doi=None,
             url="https://archive.org/details/competitivestrat0000port",
             language="en", isbn=None,
             citation="Porter, M. E. (1980). Competitive Strategy: Techniques for Analyzing Industries and Competitors. New York: Free Press.",
             locator="chapters on generic competitive strategies", locator_type="CHAPTER",
             supports="cost leadership, differentiation and focus as the three generic strategies", verified=True),
        dict(kind="WEBSITE",
             title_en="What Is Strategy? (Harvard Business Review, 1996)",
             title_fa="استراتژی چیست؟ (هاروارد بیزینس ریویو، ۱۹۹۶)",
             authors="Michael E. Porter", year=1996,
             publisher="Harvard Business Review",
             doi=None,
             url="https://hbr.org/1996/11/what-is-strategy",
             language="en", isbn=None,
             citation="Porter, M. E. (1996). What Is Strategy? Harvard Business Review, 74(6), 61-78.",
             locator="article, November-December 1996", locator_type="SECTION",
             supports="refinement of positioning through fit among activities rather than standalone generic labels", verified=True),
    ],
}

ENRICH = {
    "MC-603": dict(
        year=1965,
        mapping=LAW_MAPPING,
        summary="قانون مور قاعده‌ای تجربی دربارهٔ رشد توان محاسباتی است که گوردون مور در مقالهٔ ۱۹۶۵ خود در مجلهٔ الکترونیکس مطرح کرد. او پیش‌بینی کرد شمار اجزای مدارهای مجتمع در بازه‌های منظم افزایش می‌یابد و هزینهٔ هر جزء کاهش می‌یابد؛ پیش‌بینی نخست سالانه بود و در ۱۹۷۵ به حدود هر دو سال بازنگری شد. این قاعده به بنیاد نقشهٔ راه صنعت نیمه‌رسانا بدل شد و توضیح داد چگونه رایانه، تلفن همراه و رسانهٔ دیجیتال به‌سرعت ارزان و فراگیر می‌شوند. قانون مور بیشتر یک برنامهٔ صنعتی و انتظار جمعی است تا قانونی طبیعی؛ شرکت‌ها اهداف تولید را بر پایهٔ آن تنظیم کرده‌اند و همین، بخشی از تحقق آن را ساخته است. با نزدیک‌شدن به محدودیت‌های فیزیکی و اقتصادی، شتاب رشد کند شده و بحث دربارهٔ پایان آن بالا گرفته است. در پژوهش رسانه، این قانون چارچوبی برای فهم اقتصاد فراوانی پردازش، پلتفرم و هوش مصنوعی فراهم می‌کند. نقدها بر خودتحقق‌سازبودن، نادیده‌گرفتن هزینهٔ انرژی و اثر زیست‌محیطی تأکید دارند.",
        definition="قانون مور قاعده‌ای است که می‌گوید شمار ترانزیستورهای مدار مجتمع هر حدود دو سال دو برابر می‌شود و هزینهٔ محاسبه به‌شدت کاهش می‌یابد.",
        main_problem="چگونه می‌توان رشد نمایی توان محاسباتی و کاهش هزینهٔ آن را پیش‌بینی کرد و برنامهٔ راه صنعت و طراحی فناوری رسانه را بر آن استوار ساخت.",
        mechanism="کوچک‌سازی اجزا، شمار ترانزیستور در هر تراشه را در بازه‌های منظم افزایش می‌دهد و هزینهٔ هر عملیات محاسباتی را کاهش می‌دهد؛ این روند ظرفیت پردازش رسانه، رمزگذاری و هوش مصنوعی را پیوسته گسترش می‌دهد.",
        assumptions=[
            "کوچک‌سازی اجزا تا بازه‌ای ادامه‌پذیر است.",
            "روند رشد در بازه‌های منظم رخ می‌دهد.",
            "هزینهٔ محاسبه با مقیاس کاهش می‌یابد.",
            "صنعت اهداف تولید را بر روند تنظیم می‌کند.",
            "افزایش توان به کاربردهای تازه می‌انجامد.",
            "محدودیت فیزیکی در نهایت اثر می‌گذارد.",
            "قدرت پردازش به رسانهٔ غنی‌تر راه می‌دهد.",
            "اقتصاد مقیاس مزیت رقابتی می‌سازد.",
        ],
        principles=[
            "روند بلندمدت را پایش کن.",
            "هزینهٔ کل مالکیت را در نظر بگیر.",
            "محدودیت حرارتی و انرژی را بسنج.",
            "برنامهٔ راه صنعت را با داده به‌روز کن.",
            "از تعمیم خطی بپرهیز.",
            "کاربردهای توان اضافی را طراحی کن.",
            "اثر زیست‌محیطی را در تحلیل بگنجان.",
        ],
        critiques=[
            "قانونی طبیعی نیست و خودتحقق‌ساز است.",
            "هزینهٔ انرژی و خنک‌سازی نادیده می‌ماند.",
            "شتاب رشد در سال‌های اخیر کند شده است.",
            "اثر زیست‌محیطی تولید تراشه کم‌رنگ می‌شود.",
            "نابرابری دسترسی به توان محاسباتی را توضیح نمی‌دهد.",
            "پیش‌بینی دقیق نقطهٔ پایان ممکن نیست.",
            "به معماری و نرم‌افزار کمتر توجه دارد.",
        ],
        critique_text="منتقدان می‌گویند قانون مور بیش از آنکه قانون طبیعت باشد، هدفی صنعتی و خودتحقق‌ساز است و هزینهٔ انرژی، اثر زیست‌محیطی و کندی رشد اخیر را توضیح نمی‌دهد؛ با این حال همچنان مؤثرترین چارچوب پیش‌بینی رشد فناوری رسانه است.",
        applications=[
            "برنامه‌ریزی زیرساخت محاسباتی.",
            "تحلیل اقتصاد رسانهٔ دیجیتال.",
            "پژوهش هوش مصنوعی.",
            "مطالعهٔ تلفن همراه.",
            "تحلیل مرکز داده.",
            "پژوهش رمزگذاری و امنیت.",
            "مطالعهٔ رایانش ابری.",
            "تحلیل صنعت نیمه‌رسانا.",
            "پژوهش بازی رایانه‌ای.",
            "مطالعهٔ اینترنت اشیا.",
            "تحلیل ویدئوی دیجیتال.",
            "پژوهش اتوماسیون.",
            "مطالعهٔ رباتیک.",
            "تحلیل فناوری پوشیدنی.",
        ],
        example_text="گسترش ویدئوی باکیفیت در تلفن همراه نمونهٔ روشنی است: کاهش پیوستهٔ هزینهٔ پردازش و حافظه، رمزگذاری پیشرفته را در دستگاهی جیبی ممکن کرد و عادت مصرف رسانه را دگرگون ساخت.",
        evolution="مور پیش‌بینی نخست را در ۱۹۶۵ منتشر کرد، در ۱۹۷۵ بازنگری کرد، صنعت نیمه‌رسانا در دههٔ ۱۹۸۰ آن را به نقشهٔ راه بدل کرد، در دههٔ ۲۰۰۰ محدودیت توان و حرارت آشکار شد و امروز بحث پایان قانون مور با معماری‌های تخصصی و تراشه‌های چندبخشی ادامه دارد.",
        key_concepts=["ترانزیستور", "رشد نمایی", "هزینهٔ محاسبه", "نقشهٔ راه صنعت", "مقیاس", "محدودیت فیزیکی"],
        theorists="گوردون مور.",
        theorists_text="گوردون مور با مشاهدهٔ روند شمار اجزا در مدارهای مجتمع، پیش‌بینی رشد منظم توان محاسباتی را صورت‌بندی کرد و آن را به برنامهٔ صنعت نیمه‌رسانا بدل ساخت.",
        model="مدل رشد نمایی محاسبه: شمار اجزا در هر تراشه در بازه‌های منظم دو برابر می‌شود، هزینهٔ محاسبه کاهش می‌یابد و ظرفیت کاربردهای رسانه‌ای پیوسته گسترش می‌یابد تا محدودیت فیزیکی و اقتصادی اثر خود را بگذارد.",
        studies=[
            "پایش رشد ترانزیستور.",
            "تحلیل اقتصاد رسانهٔ دیجیتال.",
            "پژوهش زیرساخت هوش مصنوعی.",
            "مطالعهٔ تلفن همراه.",
            "تحلیل مرکز داده.",
            "پژوهش رمزگذاری.",
            "مطالعهٔ رایانش ابری.",
            "تحلیل صنعت نیمه‌رسانا.",
            "پژوهش بازی رایانه‌ای.",
            "مطالعهٔ اینترنت اشیا.",
            "تحلیل ویدئوی دیجیتال.",
            "پژوهش اتوماسیون.",
            "مطالعهٔ رباتیک.",
            "تحلیل فناوری پوشیدنی.",
        ],
    ),
    "MC-604": dict(
        year=1993,
        mapping=LAW_MAPPING,
        summary="قانون گیندر قاعده‌ای تجربی دربارهٔ رشد پهنای باند است که به جورج گیندر، نویسنده و تحلیلگر فناوری، نسبت داده می‌شود. بر پایهٔ این قانون، ظرفیت انتقال شبکه دست‌کم سه برابر سریع‌تر از توان پردازش رایانه رشد می‌کند و همین عدم‌توازن، اقتصاد رسانه و ارتباطات را دگرگون می‌سازد. گیندر در نوشته‌های خود از موج‌های پهنای باند و فراوانی ارتباطات سخن گفت و پیش‌بینی کرد که محدودیت شبکه جای خود را به فراوانی فیبر و ظرفیت انتقال بدهد. پیامد این قانون آن است که خدمات مبتنی بر انتقال داده، مانند ویدئوی جریانی، رایانش ابری و رسانهٔ اجتماعی، سریع‌تر از توان محلی دستگاه‌ها گسترش می‌یابند. این ایده در کنار قانون مور و قانون متکالف، مثلث فهم اقتصاد دیجیتال را می‌سازد. نقدها بر دقت تجربی کم، نادیده‌گرفتن محدودیت طیف و نابرابری دسترسی، و ساده‌سازی رابطهٔ عرضه و تقاضای پهنای باند تأکید دارند.",
        definition="قانون گیندر می‌گوید پهنای باند شبکه دست‌کم سه برابر سریع‌تر از توان پردازش رایانه رشد می‌کند و فراوانی انتقال، اقتصاد رسانه را بازسازمان می‌دهد.",
        main_problem="چگونه می‌توان توضیح داد که ظرفیت انتقال شبکه سریع‌تر از توان محاسبه رشد می‌کند و این عدم‌توازن چه پیامدهایی برای معماری خدمات و اقتصاد رسانه دارد.",
        mechanism="پیشرفت فیبر نوری و فناوری انتقال، ظرفیت شبکه را با شتابی بیش از رشد پردازش افزایش می‌دهد؛ در نتیجه بخش بیشتری از توان محاسبه به سمت خدماتی می‌رود که داده را جابه‌جا و پردازش را به ابر می‌سپارند.",
        assumptions=[
            "ظرفیت انتقال سریع‌تر از پردازش رشد می‌کند.",
            "فراوانی پهنای باند هزینهٔ ارتباط را کاهش می‌دهد.",
            "خدمات ابری بر انتقال داده تکیه دارند.",
            "رشد شبکه بر معماری نرم‌افزار اثر می‌گذارد.",
            "تقاضای ویدئو محرک اصلی پهنای باند است.",
            "فیبر نوری ظرفیت بالایی فراهم می‌کند.",
            "محدودیت طیف بی‌سیم جدی است.",
            "اقتصاد رسانه با فراوانی انتقال دگرگون می‌شود.",
        ],
        principles=[
            "ظرفیت شبکه را پیش از تقاضا بسنج.",
            "معماری را به ابر و انتقال بسپار.",
            "تفاوت شبکهٔ ثابت و بی‌سیم را ببین.",
            "هزینهٔ طیف و زیرساخت را لحاظ کن.",
            "رشد پهنای باند را با داده پایش کن.",
            "نابرابری دسترسی را در سیاست بگنجان.",
            "از پیش‌بینی خطی بپرهیز.",
        ],
        critiques=[
            "پشتوانهٔ تجربی قانون محدود است.",
            "محدودیت طیف و زیرساخت نادیده می‌ماند.",
            "نابرابری دسترسی را توضیح نمی‌دهد.",
            "رابطهٔ عرضه و تقاضا ساده‌سازی می‌شود.",
            "تعریف دقیق «سه برابر» روشن نیست.",
            "کیفیت تجربه و تأخیر را در نظر نمی‌گیرد.",
            "تجربهٔ کشورهای در حال توسعه را پوشش نمی‌دهد.",
        ],
        critique_text="منتقدان می‌گویند پشتوانهٔ تجربی محدود، تعریف مبهم و نادیده‌گرفتن محدودیت طیف و شکاف دسترسی، دقت این قانون را کاهش می‌دهد؛ با این حال بینش اصلی آن دربارهٔ سبقت ظرفیت انتقال از توان پردازش، در طراحی خدمات ابری و رسانهٔ جریانی راهنما بوده است.",
        applications=[
            "برنامه‌ریزی شبکهٔ فیبر.",
            "طراحی خدمات ابری.",
            "تحلیل ویدئوی جریانی.",
            "پژوهش رسانهٔ اجتماعی.",
            "مطالعهٔ مرکز داده.",
            "تحلیل اقتصاد ارتباطات.",
            "پژوهش اینترنت اشیا.",
            "مطالعهٔ شهر هوشمند.",
            "تحلیل کار از راه دور.",
            "پژوهش بازی ابری.",
            "مطالعهٔ آموزش آنلاین.",
            "تحلیل سلامت دیجیتال.",
            "پژوهش واقعیت مجازی.",
            "تحلیل زیرساخت مخابرات.",
        ],
        example_text="گسترش پخش ویدئوی چهارکی نمونهٔ روشنی است: ظرفیت انتقال سریع‌تر از توان پردازش دستگاه‌های خانگی رشد کرد و امکان داد محاسبهٔ رمزگذاری به ابر منتقل شود و دستگاه ارزان‌تر بماند.",
        evolution="گیندر ایده را در نوشته‌های اوایل دههٔ ۱۹۹۰ و سپس در کتاب تله‌کازم گسترد، در دههٔ ۲۰۰۰ با رشد فیبر و پهنای باند خانگی تأیید شد، در دههٔ ۲۰۱۰ با ویدئوی جریانی و ابر تثبیت شد و امروز در بحث شبکهٔ نسل پنجم و شکاف دسترسی ادامه دارد.",
        key_concepts=["پهنای باند", "فیبر نوری", "فراوانی انتقال", "رایانش ابری", "قانون مور", "شکاف دسترسی"],
        theorists="جورج گیندر.",
        theorists_text="جورج گیندر با تحلیل رشد ظرفیت انتقال، فراوانی پهنای باند را محور اقتصاد ارتباطات دانست و آن را در کنار رشد پردازش و ارزش شبکه صورت‌بندی کرد.",
        model="مدل فراوانی انتقال: ظرفیت شبکه با شتابی بیش از توان پردازش رشد می‌کند؛ خدماتی که داده را جابه‌جا می‌کنند سریع‌تر گسترش می‌یابند و معماری نرم‌افزار به سمت ابر و انتقال می‌رود.",
        studies=[
            "پایش رشد پهنای باند.",
            "تحلیل شبکهٔ فیبر.",
            "پژوهش خدمات ابری.",
            "مطالعهٔ ویدئوی جریانی.",
            "تحلیل رسانهٔ اجتماعی.",
            "پژوهش مرکز داده.",
            "مطالعهٔ اقتصاد ارتباطات.",
            "تحلیل اینترنت اشیا.",
            "پژوهش شهر هوشمند.",
            "مطالعهٔ کار از راه دور.",
            "تحلیل بازی ابری.",
            "پژوهش آموزش آنلاین.",
            "مطالعهٔ سلامت دیجیتال.",
            "تحلیل واقعیت مجازی.",
        ],
    ),
    "MC-605": dict(
        year=1973,
        mapping=LAW_MAPPING,
        summary="قانون آمارا مشاهده‌ای دربارهٔ ادراک اجتماعی فناوری است که روی آمارا، رئیس مؤسسهٔ آینده، در ۱۹۷۳ آن را مطرح کرد. بر پایهٔ این قانون، ما اثر یک فناوری را در کوتاه‌مدت بیش‌برآورد و در بلندمدت کم‌برآورد می‌کنیم. توضیح آن ساده است: در آغاز، شور و وعده‌های فناوری از شواهد واقعی جلو می‌زند و انتظار دگرگونی فوری می‌سازد؛ اما دگرگونی واقعی به تکمیل زیرساخت، مهارت، نهاد و مدل کسب‌وکار نیاز دارد و آهسته و پیوسته رخ می‌دهد. این قانون چارچوبی برای فهم چرخهٔ هیجان فناوری، شکست استارتاپ‌های پرسر‌و‌صدا و موفقیت آرام فناوری‌هایی فراهم می‌کند که در آغاز کم‌اهمیت به نظر می‌رسند. در رسانه، سرنوشت رادیو، تلویزیون، اینترنت و هوش مصنوعی نمونه‌های گویای این الگو هستند. قانون آمارا بیشتر ابزار شهودی است تا مدل کمّی و برای پژوهشگر رسانه یادآور می‌شود که داوری دربارهٔ فناوری تازه را به افق بلندمدت بسپارد. نقدها بر دشواری اندازه‌گیری، سوگیری پس‌نگر، نادیده‌گرفتن تفاوت توزیع منافع و کم‌توجهی به نقش سیاست‌گذاری تأکید دارند.",
        definition="قانون آمارا می‌گوید اثر یک فناوری در کوتاه‌مدت بیش‌برآورد و در بلندمدت کم‌برآورد می‌شود.",
        main_problem="چگونه می‌توان توضیح داد که جامعه در برابر فناوری تازه هم دچار هیجان افراطی می‌شود و هم دگرگونی آرام و گستردهٔ آن را نادیده می‌گیرد.",
        mechanism="در کوتاه‌مدت، روایت و وعده از شواهد جلو می‌زند و انتظار غیرواقعی می‌سازد؛ در بلندمدت، فناوری با تکمیل زیرساخت، مهارت و نهاد در زندگی روزمره نفوذ می‌کند اما این نفوذ تدریجی و کم‌فروغ است و کمتر دیده می‌شود.",
        assumptions=[
            "ادراک فناوری با اثر واقعی آن هم‌گام نیست.",
            "وعده‌های فناوری در آغاز اغراق می‌شوند.",
            "دگرگونی واقعی به تکمیل زیرساخت نیاز دارد.",
            "نفوذ بلندمدت تدریجی و کم‌فروغ است.",
            "چرخهٔ هیجان الگویی تکرارشونده دارد.",
            "رسانه‌ها در ساختن انتظار نقش دارند.",
            "ارزیابی فناوری به زمان نیاز دارد.",
            "منافع و هزینه‌ها ناهمگون توزیع می‌شوند.",
        ],
        principles=[
            "از پیش‌بینی کوتاه‌مدت بپرهیز.",
            "افق بلندمدت را جدی بگیر.",
            "زیرساخت و مهارت را در تحلیل بگنجان.",
            "چرخهٔ هیجان را از شواهد جدا کن.",
            "توزیع منافع را بسنج.",
            "روایت رسانه‌ای را نقد کن.",
            "ارزیابی را با داده به‌روز کن.",
        ],
        critiques=[
            "اندازه‌گیری کمّی آن دشوار است.",
            "مرز کوتاه‌مدت و بلندمدت روشن نیست.",
            "سوگیری پس‌نگر در کاربرد آن دیده می‌شود.",
            "توزیع نابرابر منافع را نادیده می‌گیرد.",
            "به تفاوت جوامع کمتر توجه دارد.",
            "برای تصمیم فوری راهنمای عملی کمی می‌دهد.",
            "به نقش سیاست‌گذاری کم می‌پردازد.",
        ],
        critique_text="منتقدان می‌گویند ابهام زمانی، دشواری اندازه‌گیری و نادیده‌گرفتن توزیع منافع، کاربرد عملی قانون آمارا را محدود می‌کند؛ با این حال این مشاهده چارچوبی شهودی و ماندگار برای نقد هیجان فناوری و جدی‌گرفتن دگرگونی آرام فراهم کرده است.",
        applications=[
            "تحلیل چرخهٔ هیجان فناوری.",
            "پژوهش پذیرش رسانهٔ نو.",
            "مطالعهٔ هوش مصنوعی.",
            "تحلیل سرمایه‌گذاری فناوری.",
            "پژوهش سیاست نوآوری.",
            "مطالعهٔ آموزش دیجیتال.",
            "تحلیل سلامت دیجیتال.",
            "پژوهش خودروی خودران.",
            "مطالعهٔ واقعیت مجازی.",
            "تحلیل بلاک‌چین.",
            "پژوهش رسانهٔ اجتماعی.",
            "مطالعهٔ اتوماسیون کار.",
            "تحلیل شهر هوشمند.",
            "پژوهش فناوری پوشیدنی.",
            "مطالعهٔ اینترنت ماهواره‌ای.",
            "پژوهش رایانش کوانتومی.",
        ],
        example_text="در آغاز عرضهٔ عینک واقعیت مجازی، رسانه‌ها از دگرگونی فوری آموزش و سرگرمی سخن گفتند؛ سال‌ها بعد این فناوری در آموزش حرفه‌ای و طراحی صنعتی آرام نفوذ کرد، بی‌آنکه وعدهٔ نخست محقق شود.",
        evolution="آمارا مشاهده را در ۱۹۷۳ مطرح کرد، در دههٔ ۱۹۹۰ با چرخهٔ هیجان فناوری پیوند یافت، در دههٔ ۲۰۰۰ به ابزار تحلیل سرمایه‌گذاری بدل شد و امروز در بحث هوش مصنوعی و فناوری‌های نوپدید بارها نقل می‌شود.",
        key_concepts=["بیش‌برآورد کوتاه‌مدت", "کم‌برآورد بلندمدت", "چرخهٔ هیجان", "پذیرش فناوری", "زیرساخت", "نفوذ تدریجی"],
        theorists="روی آمارا.",
        theorists_text="روی آمارا به‌عنوان رئیس مؤسسهٔ آینده، الگوی ادراک عمومی فناوری را صورت‌بندی کرد و بر فاصلهٔ وعدهٔ کوتاه‌مدت و اثر بلندمدت تأکید کرد.",
        model="مدل منحنی انتظار: در آغاز، انتظار از اثر فناوری بالاتر از واقعیت است؛ سپس ناامیدی می‌رسد و در بلندمدت نفوذ آرام و گسترده، اثر واقعی را آشکار می‌کند.",
        studies=[
            "تحلیل چرخهٔ هیجان.",
            "پژوهش پذیرش رسانه.",
            "مطالعهٔ هوش مصنوعی.",
            "تحلیل سرمایه‌گذاری فناوری.",
            "پژوهش سیاست نوآوری.",
            "مطالعهٔ آموزش دیجیتال.",
            "تحلیل سلامت دیجیتال.",
            "پژوهش خودروی خودران.",
            "مطالعهٔ واقعیت مجازی.",
            "تحلیل بلاک‌چین.",
            "پژوهش رسانهٔ اجتماعی.",
            "مطالعهٔ اتوماسیون کار.",
            "تحلیل شهر هوشمند.",
            "پژوهش فناوری پوشیدنی.",
        ],
    ),
    "MC-151": dict(
        year=1980,
        mapping=STRATEGY_MAPPING,
        summary="استراتژی‌های عمومی رقابتی چارچوب مایکل پورتر در کتاب استراتژی رقابتی در ۱۹۸۰ است که سه راه بنیادین کسب مزیت را از هم جدا می‌کند. رهبری هزینه یعنی تولید با کمترین هزینه در صنعت و عرضهٔ محصول به بهایی پایین‌تر از رقبا. تمایز یعنی ساختن ویژگی‌هایی که مشتری برای آن‌ها بهای بیشتری می‌پردازد، مانند کیفیت، برند یا خدمات. تمرکز یعنی هدف‌گیری یک بخش ویژهٔ بازار و خدمت بهتر به آن بخش، خواه با هزینهٔ پایین و خواه با تمایز. پورتر هشدار می‌دهد سازمانی که هیچ‌یک را کامل انتخاب نکند میان دو راه گرفتار می‌شود و مزیت پایدار نمی‌سازد. این چارچوب در تحلیل رسانه نیز به کار رفته است: سازمان‌های خبری کم‌هزینه، رسانه‌های متمایز برندمحور و نشریات تخصصی با تمرکز بر مخاطب خاص. پورتر در مقالهٔ استراتژی چیست در ۱۹۹۶ تأکید کرد که مزیت پایدار از تناسب میان فعالیت‌ها می‌آید نه از برچسب استراتژی. نقدها بر امکان ترکیب هزینه و تمایز و کارایی کمتر مدل در بازار پلتفرمی تأکید دارند.",
        definition="استراتژی‌های عمومی رقابتی چارچوبی است که سه راه رهبری هزینه، تمایز و تمرکز را برای کسب مزیت رقابتی پایدار از هم جدا می‌کند.",
        main_problem="چگونه می‌توان در یک صنعت رقابتی، موضعی روشن و پایدار انتخاب کرد که سازمان را از رقبا متمایز کند و از گرفتارشدن در میانهٔ راه جلوگیری کند.",
        mechanism="سازمان یا با مقیاس و کارایی هزینه را پایین می‌آورد، یا با ویژگی‌های بی‌همتا بهایی بالاتر می‌گیرد، یا نیاز یک بخش ویژه را بهتر برمی‌آورد؛ تناسب میان فعالیت‌ها این موضع را تقلیدناپذیر می‌کند.",
        assumptions=[
            "رقابت بر پایهٔ موضع روشن شکل می‌گیرد.",
            "هزینه و تمایز دو محور اصلی مزیت‌اند.",
            "بخش‌بندی بازار امکان تمرکز می‌دهد.",
            "گرفتارشدن در میانه مزیت را از بین می‌برد.",
            "تناسب فعالیت‌ها تقلید را دشوار می‌کند.",
            "مزیت پایدار به انتخاب پایدار نیاز دارد.",
            "ساختار صنعت بر سود اثر می‌گذارد.",
            "مشتری به تفاوت‌ها پاسخ می‌دهد.",
        ],
        principles=[
            "یک موضع روشن انتخاب کن.",
            "هزینهٔ کل را مدیریت کن.",
            "تمایز را برای مشتری معنادار بساز.",
            "بخش بازار را دقیق هدف بگیر.",
            "از میانهٔ راه بپرهیز.",
            "تناسب فعالیت‌ها را بساز.",
            "مزیت را پایدار نگه دار.",
        ],
        critiques=[
            "ترکیب هزینه و تمایز ممکن است.",
            "مدل در بازار پلتفرمی کمتر کارایی دارد.",
            "مرز سه استراتژی همیشه روشن نیست.",
            "پویایی تغییر فناوری کم‌رنگ می‌شود.",
            "نقش فرهنگ و نوآوری سازمانی کم است.",
            "تمرکز بر موضع، انعطاف را کاهش می‌دهد.",
            "سنجش «میانهٔ راه» دشوار است.",
        ],
        critique_text="منتقدان می‌گویند امکان ترکیب هزینه و تمایز، ابهام مرزها و کارایی کمتر مدل در بازار پلتفرمی، چارچوب پورتر را محدود می‌کند؛ با این حال زبان روشن آن برای انتخاب موضع رقابتی، همچنان یکی از پرکاربردترین چارچوب‌های استراتژی رسانه است.",
        applications=[
            "استراتژی رسانهٔ کم‌هزینه.",
            "تمایز برند خبری.",
            "نشریهٔ تخصصی و تمرکز.",
            "تحلیل رقابت پلتفرمی.",
            "استراتژی پخش عمومی.",
            "مطالعهٔ مدل اشتراک.",
            "تحلیل بازار تبلیغات.",
            "پژوهش رسانهٔ محلی.",
            "استراتژی پادکست.",
            "تحلیل روزنامهٔ رایگان.",
            "مطالعهٔ خدمات جریانی.",
            "پژوهش رسانهٔ قومی.",
            "تحلیل کسب‌وکار خبر.",
            "استراتژی محتوای ویژه.",
        ],
        example_text="یک روزنامهٔ محلی با تمرکز بر خبرهای شهر و خدمات اشتراک، در برابر پلتفرم‌های عمومی موضعی متمایز می‌سازد؛ تناسب میان تحریریهٔ محلی، شبکهٔ توزیع و رابطه با خوانندگان، تقلید این موضع را برای رقبای بزرگ دشوار می‌کند.",
        evolution="پورتر چارچوب را در ۱۹۸۰ منتشر کرد، در دههٔ ۱۹۸۰ به زبان مشترک مدیریت بدل شد، در ۱۹۹۶ با تأکید بر تناسب فعالیت‌ها بازنگری شد، در دههٔ ۲۰۰۰ در تحلیل رسانهٔ دیجیتال به کار رفت و امروز در کنار رویکردهای پلتفرمی و پویا خوانده می‌شود.",
        key_concepts=["رهبری هزینه", "تمایز", "تمرکز", "میانهٔ راه", "مزیت رقابتی", "تناسب فعالیت‌ها"],
        theorists="مایکل پورتر.",
        theorists_text="مایکل پورتر با تحلیل ساختار صنعت و سه استراتژی عمومی، زبان مشترکی برای انتخاب موضع رقابتی ساخت و سپس با مفهوم تناسب فعالیت‌ها آن را عمیق‌تر ساخت.",
        model="مدل سه‌راهی: سازمان یا هزینه را پایین می‌آورد، یا تمایز می‌سازد، یا بخشی ویژه را هدف می‌گیرد؛ تناسب فعالیت‌ها موضع را پایدار و تقلیدناپذیر می‌کند.",
        studies=[
            "تحلیل استراتژی رسانهٔ کم‌هزینه.",
            "پژوهش تمایز برند خبری.",
            "مطالعهٔ نشریهٔ تخصصی.",
            "تحلیل رقابت پلتفرمی.",
            "پژوهش پخش عمومی.",
            "مطالعهٔ مدل اشتراک.",
            "تحلیل بازار تبلیغات.",
            "پژوهش رسانهٔ محلی.",
            "مطالعهٔ پادکست.",
            "تحلیل روزنامهٔ رایگان.",
            "پژوهش خدمات جریانی.",
            "مطالعهٔ رسانهٔ قومی.",
            "تحلیل کسب‌وکار خبر.",
            "پژوهش محتوای ویژه.",
        ],
    ),
}

NAME_FIX = {
    "MC-605": ("قانون آمارا", "Amara's Law", "canonical_name_en corrected from Amaro's Law to Amara's Law (verified spelling of Roy Amara, IFTF president); Persian name unchanged; year corrected 1960 -> 1973 in same pass"),
}
YEAR_FIX = {
    "MC-603": "no year change; note: the original 1965 article predicted yearly doubling, revised in 1975 to roughly every two years; card core_logic reflects the later two-year formulation",
    "MC-604": "no year change; note: Gilder's Law is attributed to Gilder's early-1990s Forbes ASAP and Telecosm writings; the canonical statement is that bandwidth grows at least three times faster than computing power, while card core_logic's 'tripling every 12 months' is one loose variant",
    "MC-605": "year corrected 1960 -> 1973 (verified anchor: IFTF states Roy Amara coined the observation in 1973 as IFTF president); card had no documentation",
    "MC-151": "no year change; verified anchor: Porter, Competitive Strategy, Free Press, 1980",
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
                                       "verified": n_verified, "batch": 188}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH188 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
