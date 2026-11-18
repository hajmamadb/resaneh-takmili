# -*- coding: utf-8 -*-
"""Batch 153 (MODEL): MC-597 Grunig strategic PR, MC-599 two-sided market, MC-606 five forces, MC-609 Hotelling."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch153-model-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch153_model.json"

S = {
    "MC-597": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Furnishing the Edifice: Ongoing Research on Public Relations As a Strategic Management Function",
             title_fa="ساختن بنای نظریه: پژوهش پیوسته دربارهٔ روابط عمومی به‌عنوان کارکرد مدیریت راهبردی",
             authors="Grunig, J. E.", year=2006,
             publisher="Journal of Public Relations Research",
             doi="10.1207/s1532754xjprr1802_5",
             url="https://www.tandfonline.com/doi/abs/10.1207/s1532754xjprr1802_5",
             language="en", isbn=None,
             citation="Grunig, J. E. (2006). Furnishing the edifice: Ongoing research on public relations as a strategic management function. Journal of Public Relations Research, 18(2).",
             locator="18(2)", locator_type="ISSUE",
             supports="public relations as a strategic management function linked to organizational effectiveness", verified=True),
        dict(kind="BOOK_CHAPTER",
             title_en="Furnishing the Edifice: Ongoing Research on Public Relations As a Strategic Management Function",
             title_fa="ساختن بنای نظریه: روابط عمومی به‌عنوان کارکرد مدیریت راهبردی",
             authors="Grunig, J. E.", year=2013,
             publisher="Routledge",
             doi="10.4324/9780203079256-1",
             url="https://www.taylorfrancis.com/chapters/edit/10.4324/9780203079256-1/furnishing-edifice-james-grunig",
             language="en", isbn=None,
             citation="Grunig, J. E. (2013). Furnishing the edifice: Ongoing research on public relations as a strategic management function. In Public Relations and Communication Management. London: Routledge.",
             locator="chapter 1", locator_type="chapter",
             supports="later book-chapter restatement of the strategic management argument", verified=True),
    ],
    "MC-599": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Platform Competition in Two-Sided Markets",
             title_fa="رقابت پلتفرم در بازارهای دوسویه",
             authors="Rochet, J.-C.; Tirole, J.", year=2003,
             publisher="Journal of the European Economic Association",
             doi=None,
             url="https://academic.oup.com/jeea/article-abstract/1/4/990/2280902",
             language="en", isbn=None,
             citation="Rochet, J.-C., & Tirole, J. (2003). Platform competition in two-sided markets. Journal of the European Economic Association, 1(4), 990-1029.",
             locator="1(4):990-1029", locator_type="page_range",
             supports="price allocation and platform competition when two sides interact through an intermediary", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Two-Sided Network Effects: A Theory of Information Product Design",
             title_fa="اثرهای شبکه‌ای دوسویه: نظریه‌ای برای طراحی محصول اطلاعاتی",
             authors="Parker, G. G.; Van Alstyne, M. W.", year=2005,
             publisher="Management Science",
             doi="10.1287/mnsc.1050.0400",
             url="https://pubsonline.informs.org/doi/10.1287/mnsc.1050.0400",
             language="en", isbn=None,
             citation="Parker, G. G., & Van Alstyne, M. W. (2005). Two-sided network effects: A theory of information product design. Management Science, 51(10), 1494-1504.",
             locator="51(10):1494-1504", locator_type="page_range",
             supports="cross-subsidy and free pricing justified by cross-side network effects", verified=True),
    ],
    "MC-606": [
        dict(kind="BOOK",
             title_en="Competitive Strategy: Techniques for Analyzing Industries and Competitors",
             title_fa="راهبرد رقابتی: فنون تحلیل صنایع و رقبا",
             authors="Porter, M. E.", year=1980,
             publisher="Free Press",
             doi=None,
             url="https://www.hbs.edu/faculty/Pages/item.aspx?num=195",
             language="en", isbn=None,
             citation="Porter, M. E. (1980). Competitive Strategy: Techniques for Analyzing Industries and Competitors. New York: Free Press.",
             locator="1980 edition", locator_type="edition",
             supports="five competitive forces as the structure of an industry", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Five Competitive Forces That Shape Strategy",
             title_fa="پنج نیروی رقابتی که راهبرد را می‌سازند",
             authors="Porter, M. E.", year=2008,
             publisher="Harvard Business Review",
             doi=None,
             url="https://public.dhe.ibm.com/software/data/sw-library/cognos/pdfs/articles/art_the_five_competitive_forces_that_shape_strategy.pdf",
             language="en", isbn=None,
             citation="Porter, M. E. (2008). The five competitive forces that shape strategy. Harvard Business Review, January 2008.",
             locator="January 2008 issue", locator_type="ISSUE",
             supports="restatement of the five forces and their strategic implications", verified=True),
    ],
    "MC-609": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Stability in Competition",
             title_fa="ثبات در رقابت",
             authors="Hotelling, H.", year=1929,
             publisher="The Economic Journal",
             doi=None,
             url="https://www.math.toronto.edu/mccann/assignments/477/Hotelling29.pdf",
             language="en", isbn=None,
             citation="Hotelling, H. (1929). Stability in competition. The Economic Journal, 39(153), 41-57.",
             locator="39(153):41-57", locator_type="page_range",
             supports="minimum differentiation in spatial duopoly competition", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="On Hotelling's Stability in Competition",
             title_fa="دربارهٔ ثبات در رقابت هاتلینگ",
             authors="d'Aspremont, C.; Gabszewicz, J. J.; Thisse, J. F.", year=1979,
             publisher="Econometrica",
             doi=None,
             url="https://www.di.ens.fr/~aspremon/Claude/PDFs/dAsp79a.pdf",
             language="en", isbn=None,
             citation="d'Aspremont, C., Gabszewicz, J. J., & Thisse, J. F. (1979). On Hotelling's stability in competition. Econometrica, 47(5).",
             locator="47(5)", locator_type="ISSUE",
             supports="critique showing minimum differentiation may not be equilibrium", verified=True),
    ],
}

ENRICH = {
    "MC-597": dict(
        year=2006,
        summary="مدل عمومی روابط عمومی، که جیمز گرونیگ در مقالهٔ سال ۲۰۰۶ با عنوان ساختن بنای نظریه جمع‌بندی کرد، روابط عمومی را کارکردی راهبردی می‌داند که به بقا و اثربخشی سازمان کمک می‌کند، نه فعالیتی حاشیه‌ای برای ساختن تصویر. در این مدل، روابط عمومی با پایش محیط، شناسایی عمومی‌های راهبردی و برقراری ارتباط متقارن، سازمان را در تصمیم‌گیری یاری می‌دهد. گرونیگ نشان داد که ارزش روابط عمومی زمانی آشکار می‌شود که در سطح مدیریت ارشد و پیش از تصمیم‌ها حضور داشته باشد؛ اگر تنها پس از تصمیم برای توجیه آن فراخوانده شود، کارکردی تزئینی است. مدل بر سه ستون استوار است: دانش راهبردی از محیط و ذی‌نفعان، ارتباط متقارن برای ساختن رابطه، و سنجش اثر بر اهداف سازمان؛ ستون سوم است که حرفه را از ادعا به سنجش می‌رساند. پژوهش تعالی، این مدل را با شواهد سازمانی گسترده آزمود و نشان داد که روابط عمومی متقارن با عملکرد بهتر سازمان پیوند دارد. نقدهای اصلی به آن، تمرکز بر سازمان‌های بزرگ، آرمانی‌بودن تقارن، سنجش دشوار ارزش راهبردی و کم‌توجهی به رسانه‌های دیجیتال را برجسته می‌کنند.",
        definition="مدل عمومی روابط عمومی، این حرفه را کارکردی راهبردی می‌داند که با پایش محیط، شناسایی عمومی‌های راهبردی و ارتباط متقارن، به تصمیم‌گیری و اثربخشی سازمان کمک می‌کند.",
        main_problem="روابط عمومی چگونه از فعالیت حاشیه‌ای و تصویرساز به کارکردی راهبردی تبدیل می‌شود که در تصمیم‌های کلان سازمان حضور دارد و ارزش خود را نشان می‌دهد.",
        mechanism="روابط عمومی محیط را پایش می‌کند، عمومی‌های راهبردی را شناسایی می‌کند، با آنان ارتباط متقارن می‌سازد و بازخورد را به تصمیم‌گیری سازمان می‌رساند؛ در نتیجه، تصمیم‌ها با فهم محیط و رابطه بهتر گرفته می‌شوند.",
        assumptions=[
            "روابط عمومی کارکردی راهبردی است.",
            "پایش محیط پیش از تصمیم لازم است.",
            "عمومی‌های راهبردی باید شناسایی شوند.",
            "تقارن، کیفیت رابطه را می‌سازد.",
            "ارزش آن با اثر بر اهداف سنجیده می‌شود.",
        ],
        principles=[
            "روابط عمومی را در سطح مدیریت ارشد بنشان.",
            "پایش محیط را پیوسته کن.",
            "عمومی‌های راهبردی را اولویت‌بندی کن.",
            "ارتباط را متقارن و پژوهش‌بنیان کن.",
            "بازخورد را به تصمیم‌گیری برسان.",
            "اثر راهبردی را با شاخص بسنج.",
        ],
        critiques=[
            "بر سازمان‌های بزرگ متمرکز است.",
            "تقارن را آرمانی فرض می‌کند.",
            "سنجش ارزش راهبردی دشوار است.",
            "رسانه‌های دیجیتال را کم‌بررسی می‌گذارد.",
            "قدرت مدیران را در تصمیم نادیده می‌گیرد.",
            "تعمیم به سازمان‌های کوچک محدود است.",
            "فرهنگ سازمانی را متغیر کمی می‌گیرد.",
            "داده‌های طولی اندک است.",
            "سازوکار قدرت در سازمان را کم‌تحلیل می‌گذارد.",
        ],
        critique_text="منتقدان می‌گویند مدل عمومی روابط عمومی جایگاه راهبردی حرفه را به‌درستی تثبیت کرد اما بر سازمان‌های بزرگ و شرایط آرمانی تکیه داشت و رسانه‌های دیجیتال را کم‌بررسی گذاشت؛ با این حال، چارچوب مرجع دفاع از ارزش راهبردی روابط عمومی است.",
        applications=[
            "طراحی ساختار روابط عمومی.",
            "پایش محیط سازمانی.",
            "ارزیابی اثربخشی ارتباط.",
            "آموزش مدیران ارتباط.",
            "برنامه‌ریزی راهبردی سازمان.",
            "پژوهش سازمانی.",
            "سنجش بازگشت سرمایهٔ ارتباط.",
            "بازنگری جایگاه واحد ارتباط در ساختار.",
        ],
        example_text="سازمانی که پیش از تغییر سیاست، نظر عمومی‌های کلیدی را می‌پرسد و آن را در تصمیم وارد می‌کند، روابط عمومی را راهبردی به کار گرفته است؛ سازمانی که پس از تصمیم از واحد ارتباط می‌خواهد آن را توجیه کند، همان کارکرد را تزئینی کرده است.",
        evolution="مقالهٔ سال ۲۰۰۶ گرونیگ پژوهش تعالی را جمع‌بندی و روابط عمومی را به‌عنوان کارکرد مدیریت راهبردی تثبیت کرد و راه را برای سنجش اثر باز کرد. فصل کتاب سال ۲۰۱۳ همان استدلال را در چارچوبی تازه بازگفت.",
        key_concepts=["مدیریت راهبردی", "عمومی راهبردی", "پایش محیط", "ارتباط متقارن", "اثربخشی سازمان", "نظریهٔ تعالی"],
        theorists="جیمز گرونیگ.",
        theorists_text="مدل در سنت پژوهش تعالی روابط عمومی شکل گرفت.",
        model="روابط عمومی به‌عنوان کارکرد راهبردی که با پایش محیط، شناسایی عمومی‌ها و ارتباط متقارن، به اثربخشی سازمان کمک می‌کند.",
        studies=[
            "مقالهٔ سال ۲۰۰۶ پژوهش تعالی را جمع‌بندی کرد.",
            "فصل سال ۲۰۱۳ استدلال را بازگفت.",
            "مطالعات سازمانی، پیوند تقارن و عملکرد را سنجیدند.",
            "پژوهش دیجیتال، مدل را در محیط شبکه‌ای آزمود.",
            "پیمایش‌های مدیریتی، جایگاه واحد ارتباط را سنجیدند.",
            "مطالعات موردی، نقش پایش محیط را نشان دادند.",
            "پژوهش‌های بحران، ارزش پیش‌بینی را سنجیدند.",
        ],
    ),
    "MC-599": dict(
        year=2003,
        summary="مدل بازار دوسویه، که ژان-شارل روشه و ژان تیرول در سال ۲۰۰۳ و جفری پارکر و مارشال ون آلستاین در سال ۲۰۰۵ صورت‌بندی کردند، بازارهایی را توصیف می‌کند که در آن‌ها یک پلتفرم دو گروه مختلف را به هم پیوند می‌دهد و حضور هر گروه، ارزش پلتفرم را برای گروه دیگر افزایش می‌دهد. نمونهٔ کلاسیک آن رسانه است: مخاطب و تبلیغ‌دهنده. ویژگی اصلی این بازارها، اثر شبکه‌ای متقاطع است: رشد یک طرف، سود طرف دیگر را بالا می‌برد. از این رو، پلتفرم اغلب یک طرف را با قیمت پایین یا رایگان جذب می‌کند و هزینه را از طرف دیگر یا از طریق تبلیغات و خدمات مکمل برمی‌دارد. ساختار قیمت، نه سطح قیمت، تعیین‌کنندهٔ موفقیت است. این مدل توضیح می‌دهد چرا روزنامه‌ها، شبکه‌های اجتماعی، موتورهای جست‌وجو و پلتفرم‌های خرید، مخاطب را رایگان نگه می‌دارند و از سوی دیگر درآمد می‌گیرند؛ قیمت صفر یک تصمیم راهبردی است، نه سخاوت. نقدهای اصلی به آن، فرض عقلانیت کامل بازیگران، کم‌توجهی به قدرت انحصاری پلتفرم‌ها، پیچیدگی سنجش اثر متقاطع و دشواری تعمیم به بازارهای چندطرفه را برجسته می‌کنند.",
        definition="مدل بازار دوسویه، پلتفرمی را توصیف می‌کند که دو گروه را به هم پیوند می‌دهد و با اثر شبکه‌ای متقاطع، یک طرف را با قیمت پایین یا رایگان جذب و هزینه را از طرف دیگر تأمین می‌کند.",
        main_problem="پلتفرم‌ها چگونه هم‌زمان دو گروه متفاوت را جذب می‌کنند، ساختار قیمت را چگونه تعیین می‌کنند و اثر شبکه‌ای متقاطع چگونه سود و رقابت را شکل می‌دهد.",
        mechanism="حضور بیشتر در یک طرف، ارزش پلتفرم را برای طرف دیگر بالا می‌برد؛ پلتفرم با قیمت‌گذاری نامتقارن یک طرف را یارانه می‌دهد و از طرف دیگر درآمد می‌گیرد تا چرخهٔ رشد هر دو طرف را فعال کند.",
        assumptions=[
            "دو گروه به هم وابسته‌اند.",
            "اثر شبکه‌ای متقاطع وجود دارد.",
            "ساختار قیمت مهم‌تر از سطح آن است.",
            "یک طرف می‌تواند یارانه بگیرد.",
            "پلتفرم واسطهٔ مبادله است.",
        ],
        principles=[
            "هر دو طرف را هم‌زمان جذب کن.",
            "طرف یارانه‌گیر را شناسایی کن.",
            "ساختار قیمت را نامتقارن طراحی کن.",
            "اثر متقاطع را بسنج.",
            "هزینهٔ تغییر طرفین را در نظر بگیر.",
            "انحصار پلتفرم را پایش کن.",
        ],
        critiques=[
            "عقلانیت کامل بازیگران را فرض می‌کند.",
            "قدرت انحصاری پلتفرم را کم‌می‌شمارد.",
            "سنجش اثر متقاطع دشوار است.",
            "تعمیم به بازارهای چندطرفه محدود است.",
            "کیفیت محتوا را به سود پلتفرم فرو می‌کاهد.",
            "اثر مقررات را کم‌بررسی می‌گذارد.",
            "پویایی بلندمدت را کم‌مدل می‌کند.",
            "هزینهٔ اجتماعی محتوای یارانه‌ای را نمی‌سنجد.",
            "رفتار کاربر را ساده فرض می‌کند.",
        ],
        critique_text="منتقدان می‌گویند مدل بازار دوسویه سازوکار رشد پلتفرم‌ها را روشن کرد اما قدرت انحصاری و اثر آن بر کیفیت محتوا را کم‌بررسی گذاشت؛ با این حال، چارچوب اصلی اقتصاد رسانه‌های پلتفرمی است.",
        applications=[
            "تحلیل اقتصاد رسانه.",
            "طراحی پلتفرم دیجیتال.",
            "قیمت‌گذاری اشتراک و تبلیغ.",
            "سیاست رقابت.",
            "پژوهش بازار رسانه.",
            "تحلیل شبکهٔ اجتماعی.",
            "طراحی بازارگاه دیجیتال.",
            "تحلیل درآمد آگهی پلتفرم.",
        ],
        example_text="شبکهٔ اجتماعی دسترسی کاربر را رایگان می‌گذارد و از تبلیغ‌دهنده درآمد می‌گیرد؛ رشد کاربران، ارزش تبلیغ را بالا می‌برد و رشد تبلیغ، کیفیت خدمت به کاربر را تقویت می‌کند، تا زمانی که تعادل دو طرف حفظ شود.",
        evolution="مقالهٔ سال ۲۰۰۳ روشه و تیرول و مقالهٔ سال ۲۰۰۵ پارکر و ون آلستاین پایهٔ اقتصاد بازارهای دوسویه را گذاشتند. پژوهش‌های بعدی، آن را به رسانه، پلتفرم‌های دیجیتال و سیاست رقابت گستردند.",
        key_concepts=["بازار دوسویه", "پلتفرم", "اثر شبکه‌ای متقاطع", "قیمت‌گذاری نامتقارن", "یارانهٔ یک طرف", "انحصار پلتفرم"],
        theorists="ژان-شارل روشه و ژان تیرول؛ جفری پارکر و مارشال ون آلستاین.",
        theorists_text="مدل در سنت اقتصاد صنعتی و اقتصاد اطلاعات شکل گرفت.",
        model="پلتفرم واسطه که با اثر شبکه‌ای متقاطع و قیمت‌گذاری نامتقارن، دو گروه وابسته را به هم پیوند می‌دهد و از یک طرف یارانه می‌دهد و از طرف دیگر درآمد می‌گیرد.",
        studies=[
            "مقالهٔ سال ۲۰۰۳ رقابت پلتفرم را الگوسازی کرد.",
            "مقالهٔ سال ۲۰۰۵ اثر متقاطع و طراحی محصول را تحلیل کرد.",
            "مطالعات رسانه، اقتصاد تبلیغ را سنجیدند.",
            "پژوهش رقابت، انحصار پلتفرم را بررسی کرد.",
            "مطالعات روزنامه، تبلیغ و مخاطب را تحلیل کردند.",
            "پژوهش پلتفرم، یارانهٔ دوطرفه را الگوسازی کرد.",
        ],
    ),
    "MC-606": dict(
        year=1980,
        summary="مدل پنج نیروی پورتر، که مایکل پورتر در کتاب راهبرد رقابتی سال ۱۹۸۰ ارائه کرد، سودآوری یک صنعت را نه محصول تصمیم‌های فردی، بلکه نتیجهٔ ساختار رقابتی آن می‌داند. پنج نیرو این ساختار را می‌سازند: رقابت میان رقبای موجود، تهدید ورودکنندگان تازه، تهدید کالاها و خدمات جایگزین، قدرت چانه‌زنی تأمین‌کنندگان و قدرت چانه‌زنی خریداران. شدت این نیروها تعیین می‌کند که ارزش ایجادشده در صنعت تا چه اندازه به بازیگران آن می‌رسد. پورتر تأکید کرد که راهبرد باید بر پایهٔ تحلیل ساختار صنعت بنا شود، نه فقط بر رقبای آشکار. او سه راهبرد عمومی را پیشنهاد کرد: رهبری هزینه، تمایز و تمرکز؛ هر سه تنها در نسبت با ساختار صنعت معنا دارند و بی تحلیل نیروها، نسخه‌ای بی‌پشتوانه‌اند. مدل در تحلیل صنایع رسانه‌ای نیز به کار رفت: ورود پلتفرم‌های دیجیتال، قدرت خریداران تبلیغاتی و تهدید محتوای جایگزین، ساختار روزنامه‌نگاری را دگرگون کرد. نقدهای اصلی به آن، ایستایی نسبی تحلیل، کم‌توجهی به همکاری و شبکه‌سازی، تمرکز بر ساختار به‌جای نوآوری و دشواری کاربرد در محیط‌های به‌سرعت متغیر را برجسته می‌کنند.",
        definition="مدل پنج نیروی پورتر، سودآوری صنعت را نتیجهٔ پنج نیروی رقابتی می‌داند: رقابت درونی، ورود تازه‌واردان، کالاهای جایگزین، قدرت تأمین‌کننده و قدرت خریدار.",
        main_problem="چرا سودآوری صنایع متفاوت است و چگونه می‌توان با تحلیل ساختار رقابتی، جایگاه راهبردی سازمان را در صنعت تعیین کرد.",
        mechanism="پنج نیروی رقابتی شدت سودآوری صنعت را تعیین می‌کنند؛ سازمان با تحلیل این نیروها و انتخاب راهبرد هزینه، تمایز یا تمرکز، در برابر فشار رقابتی موقعیت خود را تثبیت می‌کند.",
        assumptions=[
            "ساختار صنعت سودآوری را تعیین می‌کند.",
            "پنج نیروی اصلی قابل شناسایی‌اند.",
            "راهبرد باید ساختارمحور باشد.",
            "سه راهبرد عمومی وجود دارد.",
            "تحلیل صنعت پایهٔ تصمیم است.",
        ],
        principles=[
            "ساختار صنعت را پیش از رقیب تحلیل کن.",
            "هر پنج نیرو را جدا بسنج.",
            "راهبرد عمومی را آگاهانه برگزین.",
            "قدرت خریدار و تأمین‌کننده را پایش کن.",
            "تهدید جایگزین را زود ببین.",
            "تحلیل را با تغییر فناوری بازنگری کن.",
        ],
        critiques=[
            "تحلیل را نسبتاً ایستا می‌سازد.",
            "همکاری و شبکه‌سازی را کم‌می‌بیند.",
            "بر ساختار به‌جای نوآوری تمرکز می‌کند.",
            "در محیط‌های به‌سرعت متغیر دشوار است.",
            "قدرت پلتفرم را با پنج نیرو کامل توضیح نمی‌دهد.",
            "عوامل نهادی و فرهنگی را کم‌بررسی می‌گذارد.",
            "تحلیل پویا را جایگزین نمی‌کند.",
            "سنجش کمّی نیروها را دشوار می‌سازد.",
            "بازخورد راهبرد بر ساختار را کم‌می‌بیند.",
            "کالاهای دیجیتال رایگان را کامل پوشش نمی‌دهد.",
        ],
        critique_text="منتقدان می‌گویند مدل پنج نیرو چارچوبی قدرتمند برای تحلیل ساختار صنعت داد اما تحلیل را ایستا کرد و همکاری، نوآوری و پلتفرم‌ها را کم‌بررسی گذاشت؛ با این حال، همچنان نقطهٔ شروع تحلیل رقابت است.",
        applications=[
            "تحلیل صنعت رسانه.",
            "طراحی راهبرد رقابتی.",
            "ارزیابی ورود بازار.",
            "تحلیل قدرت تبلیغ‌دهنده.",
            "آموزش مدیریت راهبردی.",
            "پژوهش اقتصاد رسانه.",
            "ارزیابی سرمایه‌گذاری در صنعت.",
            "تحلیل سودآوری کسب‌وکار خبری.",
        ],
        example_text="روزنامه‌ای که هم‌زمان با کاهش خریداران تبلیغات، ورود پلتفرم‌های خبری و قدرت پلتفرم‌های توزیع را می‌بیند، پنج نیرو را در عمل تجربه می‌کند؛ تحلیل پورتر نشان می‌دهد که سودآوری نه از ضعف مدیریت، بلکه از تغییر ساختار صنعت کاهش یافته است.",
        evolution="کتاب سال ۱۹۸۰ مدل پنج نیرو را به چارچوب مسلط تحلیل صنعت تبدیل کرد. مقالهٔ سال ۲۰۰۸ همان چارچوب را برای مدیران بازگفت و پژوهش‌های رسانه‌ای آن را به اقتصاد خبر و پلتفرم گستردند، تا جایی که امروز نیروی ششم پلتفرم نیز پیشنهاد می‌شود.",
        key_concepts=["پنج نیرو", "ساختار صنعت", "موانع ورود", "قدرت چانه‌زنی", "کالای جایگزین", "راهبرد رقابتی"],
        theorists="مایکل پورتر.",
        theorists_text="مدل در سنت مدیریت راهبردی و اقتصاد صنعتی شکل گرفت.",
        model="سودآوری صنعت به‌عنوان نتیجهٔ پنج نیروی رقابتی که راهبرد هزینه، تمایز یا تمرکز را در برابر فشار رقابتی تعیین می‌کنند.",
        studies=[
            "کتاب سال ۱۹۸۰ مدل را معرفی کرد.",
            "مقالهٔ سال ۲۰۰۸ آن را برای مدیران بازگفت.",
            "مطالعات رسانه، ساختار خبر را تحلیل کردند.",
            "پژوهش پلتفرم، نیروی تازه‌ای افزود.",
            "مطالعات موردی، سودآوری صنایع خبری را مقایسه کردند.",
            "تحلیل‌های سیاستی، قدرت پلتفرم را سنجیدند.",
            "پژوهش راهبرد، تمایز رسانه‌ای را بازخوانی کرد.",
            "مطالعات تبلیغات، قدرت خریدار را سنجیدند.",
        ],
    ),
    "MC-609": dict(
        year=1929,
        summary="مدل مکانی هاتلینگ، که هارولد هاتلینگ در مقالهٔ سال ۱۹۲۹ با عنوان ثبات در رقابت ارائه کرد، رقابت دو فروشنده را در یک خیابان خطی تحلیل می‌کند و نشان می‌دهد که هر دو تمایل دارند به مرکز بازار نزدیک شوند. این نتیجه که «اصل تمایز حداقلی» نامیده شد، توضیح می‌دهد چرا محصولات رقیب اغلب شبیه هم می‌شوند و چرا رسانه‌ها به محتوای میانه‌رو و مشابه گرایش دارند. در مدل، مصرف‌کنندگان بر پایهٔ فاصله تصمیم می‌گیرند و فروشندگان با جابه‌جایی مکان، سهم بازار را تغییر می‌دهند. هاتلینگ خود دریافت که این تعادل همیشه پایدار نیست و بعدها داسپرمون و همکاران نشان دادند که با هزینهٔ خطی حمل، تعادل مرکزی از میان می‌رود. مدل در اقتصاد رسانه، تحلیل تنوع محتوا، جانمایی فروشگاه و طراحی پلتفرم به کار می‌رود و توضیحی اقتصادی برای همگرایی مواضع سیاسی نیز فراهم می‌کند. نقدهای اصلی به آن، سادگی فرض‌های مکانی، کم‌توجهی به تمایز کیفی، دشواری تعمیم به بازار چندبعدی و نادیده‌گرفتن قدرت برند را برجسته می‌کنند.",
        definition="مدل مکانی هاتلینگ، رقابت در فضای خطی را تحلیل می‌کند و نشان می‌دهد فروشندگان برای گرفتن سهم بیشتر به مرکز بازار گرایش دارند، پدیده‌ای که به تمایز حداقلی و شباهت محصولات می‌انجامد.",
        main_problem="چرا رقبای مکانی و رسانه‌ای به جای تمایز، به یکدیگر نزدیک و شبیه می‌شوند و این همگرایی چه پیامدی برای تنوع و رفاه مصرف‌کننده دارد.",
        mechanism="مصرف‌کننده نزدیک‌ترین فروشنده را برمی‌گزیند؛ فروشنده با حرکت به مرکز، بخش بیشتری از بازار را جذب می‌کند و رقیب نیز همین کار را می‌کند، تا هر دو در میانه به هم نزدیک شوند.",
        assumptions=[
            "بازار یک‌بعدی و خطی است.",
            "مصرف‌کننده بر پایهٔ فاصله انتخاب می‌کند.",
            "دو فروشنده رقیب وجود دارند.",
            "هزینهٔ حمل و جابه‌جایی مطرح است.",
            "قیمت ثابت فرض می‌شود.",
        ],
        principles=[
            "فضای رقابت را ترسیم کن.",
            "گرایش مرکزی رقبا را بسنج.",
            "تمایز کیفی را از مکان جدا کن.",
            "پایداری تعادل را بررسی کن.",
            "هزینهٔ جابه‌جایی مخاطب را در نظر بگیر.",
            "تنوع محتوا را پایش کن.",
        ],
        critiques=[
            "فرض‌های مکانی را ساده می‌گیرد.",
            "تمایز کیفی را کم‌می‌بیند.",
            "تعمیم به بازار چندبعدی دشوار است.",
            "قدرت برند را نادیده می‌گیرد.",
            "پایداری تعادل را ساده فرض می‌کند.",
            "رفتار راهبردی بلندمدت را کم‌بررسی می‌گذارد.",
            "فضای چندبعدی را یک‌بعدی می‌کند.",
            "تنوع کیفی مخاطب را نادیده می‌گیرد.",
            "اثر مقررات بر جانمایی را کم‌می‌بیند.",
            "هزینهٔ تبلیغات را در انتخاب مخاطب نادیده می‌گیرد.",
            "پویایی ورود رقیب تازه را کم‌تحلیل می‌گذارد.",
        ],
        critique_text="منتقدان می‌گویند مدل هاتلینگ بینش مهمی دربارهٔ همگرایی رقبا داد اما فرض‌های مکانی آن ساده است و تمایز کیفی را کم‌می‌بیند؛ با این حال، پایهٔ تحلیل تنوع محتوا و رقابت مکانی در اقتصاد رسانه است.",
        applications=[
            "تحلیل تنوع محتوای رسانه.",
            "جانمایی فروشگاه.",
            "طراحی پلتفرم.",
            "اقتصاد رسانه.",
            "تحلیل رقابت سیاسی.",
            "پژوهش بازاریابی.",
            "طراحی خط مشی تنوع رسانه.",
            "تحلیل همگرایی رسانه‌های محلی.",
        ],
        example_text="دو شبکهٔ تلویزیونی که هر دو برنامهٔ میانه‌رو پخش می‌کنند، به دو فروشندهٔ وسط خیابان می‌مانند؛ هر دو از ترس از دست دادن میانه، مخاطب حاشیه‌ای را رها می‌کنند و تنوع محتوا کاهش می‌یابد.",
        evolution="مقالهٔ سال ۱۹۲۹ هاتلینگ مدل رقابت مکانی را معرفی کرد. نقد سال ۱۹۷۹ نشان داد که تعادل مرکزی همیشه پایدار نیست و پژوهش‌های بعدی، مدل را به رسانه، خرده‌فروشی و پلتفرم گستردند.",
        key_concepts=["تمایز حداقلی", "رقابت مکانی", "بازار خطی", "هزینهٔ جابه‌جایی", "تنوع محتوا", "تعادل"],
        theorists="هارولد هاتلینگ.",
        theorists_text="مدل در سنت اقتصاد خرد و نظریهٔ مکان شکل گرفت.",
        model="رقابت دو فروشنده در فضای خطی که با گرایش به مرکز، به تمایز حداقلی و شباهت محصول می‌انجامد.",
        studies=[
            "مقالهٔ سال ۱۹۲۹ مدل را معرفی کرد.",
            "نقد سال ۱۹۷۹ پایداری تعادل را بررسی کرد.",
            "مطالعات رسانه، تنوع محتوا را سنجیدند.",
            "پژوهش پلتفرم، رقابت مکانی دیجیتال را تحلیل کرد.",
            "مطالعات سیاسی، همگرایی مواضع را با مدل سنجیدند.",
            "تحلیل خرده‌فروشی، جانمایی شعبه را بهینه کرد.",
            "پژوهش محتوای خبری، شباهت دستور کار را نشان داد.",
            "مطالعات رادیو، همگرایی برنامه‌سازی را بررسی کردند.",
        ],
    ),
}

NAME_FIX = {}
YEAR_FIX = {
    "MC-599": "سال و نظریه‌پرداز کارت خالی بود؛ سال ۲۰۰۳ و ۲۰۰۵ به‌عنوان شاهدهای بنیادی اقتصاد بازار دوسویه ثبت شد.",
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
                                       "verified": n_verified, "batch": 153}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH153 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
