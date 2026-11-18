# -*- coding: utf-8 -*-
"""Batch 215: repair template-era analyses on five MODEL cards."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch215-20261117"
NOW = "2026-11-17 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch215.json"

S = {
    "MC-062": [
        dict(kind="BOOK",
             title_en="Competitive Strategy: Techniques for Analyzing Industries and Competitors",
             title_fa="راهبرد رقابتی: فنون تحلیل صنایع و رقبا",
             authors="Michael E. Porter", year=1980,
             publisher="Free Press",
             doi=None,
             url="https://www.hbs.edu/faculty/Pages/item.aspx?num=195",
             language="en", isbn=None,
             citation="Porter, M. E. (1980). Competitive Strategy: Techniques for Analyzing Industries and Competitors. New York: Free Press.",
             locator="book", locator_type="BOOK",
             supports="five competitive forces framework",
             verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Five Competitive Forces That Shape Strategy",
             title_fa="پنج نیروی رقابتی که راهبرد را شکل می‌دهند",
             authors="Michael E. Porter", year=2008,
             publisher="Harvard Business Review",
             doi=None,
             url="https://hbr.org/2008/01/the-five-competitive-forces-that-shape-strategy",
             language="en", isbn=None,
             citation="Porter, M. E. (2008). The five competitive forces that shape strategy. Harvard Business Review, 86(1), 78-93.",
             locator="86(1):78-93", locator_type="PAGE",
             supports="restatement and updating of the five-forces framework",
             verified=True),
    ],
    "MC-174": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Strategies for Diversification",
             title_fa="راهبردهای تنوع‌بخشی",
             authors="H. Igor Ansoff", year=1957,
             publisher="Harvard Business Review",
             doi=None,
             url="https://www.casrilanka.com/casl/images/stories/2017/2017_pdfs/sab_portal/course_material/strategies_for_diversification.pdf",
             language="en", isbn=None,
             citation="Ansoff, H. I. (1957). Strategies for diversification. Harvard Business Review, 35(5), 113-124.",
             locator="35(5):113-124", locator_type="PAGE",
             supports="market/product growth matrix with four strategies",
             verified=True),
        dict(kind="BOOK",
             title_en="Corporate Strategy: An Analytic Approach to Business Policy for Growth and Expansion",
             title_fa="راهبرد شرکتی: رویکردی تحلیلی به سیاست کسب‌وکار برای رشد و گسترش",
             authors="H. Igor Ansoff", year=1965,
             publisher="McGraw-Hill",
             doi=None,
             url=None,
             language="en", isbn=None,
             citation="Ansoff, H. I. (1965). Corporate Strategy: An Analytic Approach to Business Policy for Growth and Expansion. New York: McGraw-Hill.",
             locator="book", locator_type="BOOK",
             supports="systematic development of the growth-vector framework",
             verified=False),
    ],
    "MC-501": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Platform Competition in Two-Sided Markets",
             title_fa="رقابت پلتفرم در بازارهای دوسویه",
             authors="Jean-Charles Rochet; Jean Tirole", year=2003,
             publisher="Journal of the European Economic Association",
             doi=None,
             url="https://academic.oup.com/jeea/article-abstract/1/4/990/2280902",
             language="en", isbn=None,
             citation="Rochet, J.-C., & Tirole, J. (2003). Platform competition in two-sided markets. Journal of the European Economic Association, 1(4), 990-1029.",
             locator="1(4):990-1029", locator_type="PAGE",
             supports="price structure and cross-side network effects in two-sided markets",
             verified=True),
        dict(kind="BOOK_CHAPTER",
             title_en="The Media and Advertising: A Tale of Two-Sided Markets",
             title_fa="رسانه و تبلیغات: حکایت بازارهای دوسویه",
             authors="Simon P. Anderson; Jean J. Gabszewicz", year=2006,
             publisher="Elsevier",
             doi=None,
             url="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=831807",
             language="en", isbn=None,
             citation="Anderson, S. P., & Gabszewicz, J. J. (2006). The media and advertising: A tale of two-sided markets. In V. Ginsburgh & D. Throsby (Eds.), Handbook of the Economics of Art and Culture (vol. 1, pp. 567-614). Amsterdam: Elsevier.",
             locator="pp. 567-614", locator_type="PAGE",
             supports="extension of two-sided market logic to media and advertising",
             verified=True),
    ],
    "MC-503": [
        dict(kind="BOOK",
             title_en="Performing Arts: The Economic Dilemma",
             title_fa="هنرهای نمایشی: دشواری اقتصادی",
             authors="William J. Baumol; William G. Bowen", year=1966,
             publisher="The Twentieth Century Fund",
             doi=None,
             url="https://books.google.com/books/about/Performing_Arts.html?id=11JOA0gEACAAJ",
             language="en", isbn=None,
             citation="Baumol, W. J., & Bowen, W. G. (1966). Performing Arts: The Economic Dilemma. New York: The Twentieth Century Fund.",
             locator="book", locator_type="BOOK",
             supports="productivity lag and rising unit costs in labour-intensive performing arts",
             verified=True),
        dict(kind="BOOK_CHAPTER",
             title_en="Baumol's Cost Disease",
             title_fa="بیماری هزینهٔ بامول",
             authors="James Heilbrun", year=2003,
             publisher="Edward Elgar",
             doi=None,
             url="https://repub.eur.nl/pub/782/TOWSE%20EBOOK_pages0103-0113.pdf",
             language="en", isbn=None,
             citation="Heilbrun, J. (2003). Baumol's cost disease. In R. Towse (Ed.), A Handbook of Cultural Economics (pp. 91-101). Cheltenham: Edward Elgar.",
             locator="pp. 91-101", locator_type="PAGE",
             supports="scholarly restatement of the cost disease argument and its limits",
             verified=True),
    ],
    "MC-504": [
        dict(kind="MAGAZINE_ARTICLE",
             title_en="The Long Tail",
             title_fa="دُم بلند",
             authors="Chris Anderson", year=2004,
             publisher="Wired",
             doi=None,
             url="https://www.wired.com/2004/10/tail/",
             language="en", isbn=None,
             citation="Anderson, C. (2004, October). The long tail. Wired, 12(10).",
             locator="12(10)", locator_type="PAGE",
             supports="niche aggregation and the economics of abundant distribution",
             verified=True),
        dict(kind="BOOK",
             title_en="The Long Tail: Why the Future of Business Is Selling Less of More",
             title_fa="دُم بلند: چرا آیندهٔ کسب‌وکار فروش کمتر از بیشتر است",
             authors="Chris Anderson", year=2006,
             publisher="Hyperion",
             doi=None,
             url="https://www.abebooks.com/9781401302375/Long-Tail-Why-Future-Business-1401302378/plp",
             language="en", isbn=None,
             citation="Anderson, C. (2006). The Long Tail: Why the Future of Business Is Selling Less of More. New York: Hyperion.",
             locator="book", locator_type="BOOK",
             supports="book-length statement of long-tail distribution economics",
             verified=True),
    ],
}

ENRICH = {
    "MC-062": dict(
        needs_enrichment=False,
        level="میان",
        related_approaches="تحلیل صنعت؛ اقتصاد رسانه؛ راهبرد رقابتی؛ نظریهٔ سازمان صنعتی؛ تحلیل پلتفرم.",
        recommended_sources="«راهبرد رقابتی» (پورتر، ۱۹۸۰)؛ «پنج نیروی رقابتی که راهبرد را شکل می‌دهند» (پورتر، ۲۰۰۸)؛ «اقتصاد رسانه» (هاردوود)؛ «رقابت پلتفرم در بازارهای دوسویه» (روشه و تیرول، ۲۰۰۳).",
        detailed_analysis=("۱. بنیان و منطق نظری\nپورتر (۱۹۸۰) جذابیت و سودآوری صنعت را پیامد ساختار آن دانست، نه نتیجهٔ هوشمندی مدیریتی صرف، و پنج نیروی ساختاری را نام برد: رقابت درونی، تهدید ورود تازه‌واردان، تهدید کالای جایگزین، قدرت چانه‌زنی خریدار و قدرت چانه‌زنی تأمین‌کننده. "
                           "مقالهٔ بازنگری ۲۰۰۸ همان چارچوب را در برابر سوءبرداشت‌ها بازخوانی کرد و بر تحلیل شواهد صنعتی به‌جای فهرست‌سازی تأکید کرد.\n\n"
                           "۲. ساختارهای مفهومی\nهر نیرو از یک جهت حاشیهٔ سود صنعت را می‌فشارد؛ ترکیب شدت پنج نیرو ساختار صنعت را می‌سازد و راهبرد بنگاه باید موقعیتی بسازد که در برابر شدیدترین نیروها محافظت شود.\n\n"
                           "۳. نمونه‌های تحلیلی\nدر صنعت خبر، رقابت درونی با سرگرمی دیجیتال و قدرت خریدار تبلیغ‌دهنده، شدت می‌گیرد و تهدید تازه‌واردان از سمت پلتفرم‌ها افزون می‌شود؛ در پخش، قدرت تأمین‌کنندهٔ محتوای ورزشی نمونهٔ روشنی از فشار بر حاشیهٔ سود است.\n\n"
                           "۴. نقدها و چالش‌ها\nمدل ایستا و توصیف‌گر است؛ نقش مکمل‌ها و اکوسیستم پلتفرمی را کم‌رنگ می‌کند؛ سنجش شدت نیروها به قضاوت کیفی وابسته است؛ و نوآوری و مرزبندی متغیر صنعت را دشوار می‌کند. نقد مکمل‌ها به‌ویژه در اقتصاد دیجیتال پررنگ شده است.\n\n"
                           "۵. سیر تاریخی\nکتاب ۱۹۸۰ چارچوب را تثبیت کرد و به متن کلاسیک راهبرد تبدیل شد؛ بازنگری ۲۰۰۸ آن را بازخوانی کرد و از دههٔ ۲۰۱۰ پژوهش پلتفرم‌ها، پژوهش‌های مکمل‌ها و ششمین نیرو را بر آن افزود.\n\n"
                           "۶. جایگاه در بحث روز\nدر تحلیل رقابت رسانه و پلتفرم، چارچوب پورتر همچنان زبان مشترک تحلیل صنعت است، به شرط آنکه با تحلیل اکوسیستم و زیرساخت داده تکمیل شود."),
    ),
    "MC-174": dict(
        needs_enrichment=False,
        level="پایه",
        related_approaches="راهبرد رشد؛ تحلیل سبد؛ اقتصاد رسانه؛ مدیریت محصول؛ راهبرد پلتفرم.",
        recommended_sources="«راهبردهای تنوع‌بخشی» (آنسوف، ۱۹۵۷)؛ «راهبرد شرکتی» (آنسوف، ۱۹۶۵)؛ «راهبرد رقابتی» (پورتر، ۱۹۸۰)؛ «اقتصاد رسانه» (هاردوود).",
        detailed_analysis=("۱. بنیان و منطق نظری\nآنسوف (۱۹۵۷) در مقالهٔ «راهبردهای تنوع‌بخشی» چهار گزینهٔ رشد را بر دو محور تازگی بازار و تازگی محصول مرتب ساخت: نفوذ در بازار، توسعهٔ بازار، توسعهٔ محصول و تنوع‌بخشی. "
                           "کتاب راهبرد شرکتی (۱۹۶۵) این ماتریس را به بردار رشد و چارچوب نظام‌مند انتخاب راهبرد گسترد و آن را به متون استاندارد مدیریت راهبردی وارد کرد.\n\n"
                           "۲. ساختارهای مفهومی\nچهار گزینه، ریسک فزاینده با تازگی هر دو بعد، سبک رشد و ارتباط با قابلیت‌های موجود سازه‌های اصلی‌اند. ماتریس پیش از هر چیز ابزار گفت‌وگو دربارهٔ گزینه‌ها است، نه پیش‌بینی موفقیت.\n\n"
                           "۳. نمونه‌های تحلیلی\nنفوذ در بازار برای رسانه یعنی افزایش مصرف همان مخاطب با همان محصول؛ توسعهٔ بازار یعنی ورود به بازار مخاطب تازه یا جغرافیای جدید؛ توسعهٔ محصول یعنی قالب تازه مانند پادکست برای همان مخاطب؛ و تنوع‌بخشی یعنی ورود به کسب‌وکاری با محصول و بازار هر دو تازه.\n\n"
                           "۴. نقدها و چالش‌ها\nمدل دو بعدی و ایستاست؛ منابع و قابلیت‌های سازمانی را کم‌رنگ می‌کند؛ اتحاد راهبردی و اکوسیستم همکاری را نادیده می‌گیرد؛ مرز بازار موجود و جدید مبهم است؛ و برای محیط پلتفرمی با محصول مشترک و بازارهای چندگانه، تفکیک دو بعد دشوار می‌شود.\n\n"
                           "۵. سیر تاریخی\nمقالهٔ ۱۹۵۷ چهار گزینه را معرفی کرد، کتاب ۱۹۶۵ آن را نظام‌مند کرد و از دههٔ ۱۹۸۰ به متن استاندارد راهبرد شرکتی و آموزش بازاریابی تبدیل شد؛ در دههٔ ۲۰۱۰ با اقتصاد پلتفرم بازخوانی شد.\n\n"
                           "۶. جایگاه در بحث روز\nماتریس آنسوف در تصمیم‌های رشد رسانه‌های دیجیتال همچنان ابزار سادهٔ گفت‌وگوی مدیریتی است؛ ارزش آن در شفاف‌کردن ریسک گزینه‌ها است و نه در پیش‌بینی نتیجهٔ بازار."),
    ),
    "MC-501": dict(
        needs_enrichment=False,
        level="میان",
        related_approaches="اقتصاد پلتفرم؛ اقتصاد رسانه؛ نظریهٔ بازار دوسویه؛ اثر شبکه‌ای؛ سیاست رقابت دیجیتال.",
        recommended_sources="«رقابت پلتفرم در بازارهای دوسویه» (روشه و تیرول، ۲۰۰۳)؛ «رسانه و تبلیغات: حکایت بازارهای دوسویه» (اندرسون و گابژوویچ، ۲۰۰۶)؛ «اقتصاد رسانه» (هاردوود)؛ «انقلاب پلتفرمی» (پارکر، ون آلس‌تاین و چوداری، ۲۰۱۶).",
        detailed_analysis=("۱. بنیان و منطق نظری\nروشه و تیرول (۲۰۰۳) نشان دادند در بازارهایی که پلتفرم دو گروه کاربری متمایز را به هم پیوند می‌دهد، تصمیم کلیدی ساختار قیمت است و نه فقط سطح قیمت؛ پلتفرم می‌تواند یک طرف را یارانه بدهد و هزینه را از طرف دیگر بگیرد. "
                           "اندرسون و گابژوویچ (۲۰۰۶) همین منطق را به رسانه و تبلیغات بردند و نشان دادند رسانهٔ تبلیغات‌محور در واقع هم‌زمان دو بازار مخاطب و تبلیغ‌دهنده را تأمین می‌کند.\n\n"
                           "۲. ساختارهای مفهومی\nبازار دوسویه، اثر شبکه‌ای بین‌گروهی، ساختار قیمت، یارانهٔ متقابل و کیفیت توجه سازه‌های اصلی‌اند. ارزش یک طرف با حضور و کیفیت طرف دیگر بالا می‌رود.\n\n"
                           "۳. نمونه‌های تحلیلی\nروزنامهٔ تبلیغات‌محور از خواننده یارانه می‌گیرد و از تبلیغ‌دهنده درآمد می‌سازد؛ پلتفرم ویدیو با محتوای رایگان کاربر را جذب می‌کند و دسترسی هدفمند را به آگهی‌دهنده می‌فروشد. در هر دو، تصمیم دربارهٔ سمت پولی و سمت رایگان تعیین‌کننده است.\n\n"
                           "۴. نقدها و چالش‌ها\nمدل بُعد فرهنگی و سیاسی رسانه را به بازار تقلیل می‌دهد؛ با پلتفرم‌های چندطرفه و داده‌محور کامل هم‌خوان نیست؛ سنجش ارزش توجه دشوار است؛ و قدرت انحصاری پلتفرم‌ها را کم‌بررسی می‌گذارد. نقد اخیر به «بازار سه‌گانه» و نقش داده پرداخته است.\n\n"
                           "۵. سیر تاریخی\nمقالهٔ ۲۰۰۳ چارچوب رقابت دوسویه را ساخت، فصل ۲۰۰۶ آن را به رسانه آورد و از دههٔ ۲۰۱۰ به هستهٔ اقتصاد پلتفرم و پرونده‌های رقابت دیجیتال تبدیل شد.\n\n"
                           "۶. جایگاه در بحث روز\nدر سیاست‌گذاری پلتفرم و بحث دسترسی و شفافیت تبلیغات، مدل دوسویه همچنان چارچوب پایه است، اما برای توضیح قدرت داده و انحصار باید با پژوهش‌های رقابت دیجیتال تکمیل شود."),
    ),
    "MC-503": dict(
        needs_enrichment=False,
        level="میان",
        related_approaches="اقتصاد فرهنگ؛ اقتصاد رسانه؛ اقتصاد خدمات؛ سیاست یارانه؛ تحلیل هزینهٔ خبر.",
        recommended_sources="«هنرهای نمایشی: دشواری اقتصادی» (بامول و بوون، ۱۹۶۶)؛ «بیماری هزینهٔ بامول» (هایلبرون، ۲۰۰۳)؛ «اقتصاد و فرهنگ» (توز، ۲۰۰۳)؛ «اقتصاد رسانه» (هاردوود).",
        detailed_analysis=("۱. بنیان و منطق نظری\nبامول و بوون (۱۹۶۶) در مطالعهٔ اقتصاد هنرهای نمایشی نشان دادند دستمزدها در کل اقتصاد با رشد بهره‌وری بالا می‌رود، اما در اجرای زنده افزایش بهره‌وری تقریباً ناممکن است؛ پس شکاف پایدار میان هزینه و درآمد پدید می‌آید. "
                           "هایلبرون (۲۰۰۳) این استدلال را نظام‌مند بازگو کرد و حدود و تعمیم آن را بررسی کرد.\n\n"
                           "۲. ساختارهای مفهومی\nبهره‌وری، کارمحوری، شکاف هزینه و درآمد، یارانه و قیمت‌گذاری سازه‌های اصلی‌اند. نکتهٔ کلیدی این است که افزایش قیمت بلیت نمی‌تواند شکاف را کاملاً جبران کند.\n\n"
                           "۳. نمونه‌های تحلیلی\nیک ارکستر برای اجرای سمفونی به همان شمار نوازندهٔ صد سال پیش نیاز دارد، در حالی که دستمزدها با اقتصاد رشد کرده است؛ در خبر، گزارش‌گری میدانی و تولید محتوای اصیل همین منطق را نشان می‌دهد، هرچند دیجیتال‌شدن هزینهٔ توزیع را جداگانه کاهش داده است.\n\n"
                           "۴. نقدها و چالش‌ها\nسنجش بهره‌وری را ساده می‌کند؛ نوآوری سازمانی و فناورانه را کم‌می‌شمارد؛ بر بخش‌های کارمحور متمرکز است؛ بازار ستارگان و تغییر الگوی مصرف را نادیده می‌گیرد؛ و یارانه را تنها راه‌حل جلوه می‌دهد.\n\n"
                           "۵. سیر تاریخی\nکتاب ۱۹۶۶ به آموزش، سلامت و خدمات عمومی تعمیم یافت؛ در اقتصاد رسانه برای توضیح فشار هزینهٔ تولید خبر به کار رفت و با تحول دیجیتال و مدل‌های اشتراکی بازبینی شد.\n\n"
                           "۶. جایگاه در بحث روز\nدر بحران کسب‌وکار خبر و بحث حمایت عمومی از روزنامه‌نگاری، بیماری هزینه توضیح می‌دهد چرا کاهش هزینهٔ توزیع، مسئلهٔ هزینهٔ تولید اصیل را حل نمی‌کند."),
    ),
    "MC-504": dict(
        needs_enrichment=False,
        level="میان",
        related_approaches="اقتصاد پلتفرم؛ اقتصاد محتوا؛ تنوع فرهنگی؛ الگوریتم پیشنهاد؛ دروازه‌بانی پلتفرم.",
        recommended_sources="«دُم بلند» (اندرسون، ۲۰۰۴)؛ «دُم بلند: چرا آیندهٔ کسب‌وکار فروش کمتر از بیشتر است» (اندرسون، ۲۰۰۶)؛ «اقتصاد رسانه» (هاردوود)؛ «فیلتر حباب» (پاریزر، ۲۰۱۱).",
        detailed_analysis=("۱. بنیان و منطق نظری\nاندرسون (۲۰۰۴) در مقالهٔ وایرد استدلال کرد کاهش هزینهٔ ذخیره‌سازی، توزیع و جست‌وجو، عرضهٔ اقلام کم‌نمونه را ممکن می‌کند و مجموع فروش این دُم می‌تواند با سرِ توزیع رقابت کند. "
                           "کتاب ۲۰۰۶ این استدلال را با داده‌های بازار کتاب، موسیقی و ویدیو گسترد و به یکی از پرنقل‌ترین روایت‌های اقتصاد دیجیتال تبدیل کرد.\n\n"
                           "۲. ساختارهای مفهومی\nدُم بلند، سر توزیع، هزینهٔ توزیع، پیشنهاددهی، کشف محتوا و تنوع فرهنگی سازه‌های اصلی‌اند. مکانیزم، جمع‌شدن تقاضای پراکندهٔ اقلام کم‌فروش است.\n\n"
                           "۳. نمونه‌های تحلیلی\nفروشگاه موسیقی آنلاین می‌تواند میلیون‌ها قطعه را عرضه کند و از مجموع فروش کم اقلام حاشیه‌ای درآمد بسازد؛ سامانهٔ پیشنهاد کتاب و ویدیو نیز تقاضا را به دُم هدایت می‌کند.\n\n"
                           "۴. نقدها و چالش‌ها\nقدرت دُم را بیش از واقع برمی‌آورد؛ توزیع نامتقارن توجه را نادیده می‌گیرد؛ به زیرساخت و سیاست پلتفرم وابسته است؛ سنجش فروش اقلام کم‌نمونه دشوار است؛ و هزینهٔ کشف محتوا را کم‌می‌شمارد. پژوهش‌های بعدی نشان دادند الگوریتم‌ها می‌توانند دُم را دوباره به سر فشار دهند.\n\n"
                           "۵. سیر تاریخی\nمقالهٔ ۲۰۰۴ مفهوم را معرفی کرد، کتاب ۲۰۰۶ آن را گسترد، و از دههٔ ۲۰۱۰ پژوهش‌های پلتفرم نقش پیشنهاددهی و دروازه‌بانی الگوریتمی را برجسته کردند.\n\n"
                           "۶. جایگاه در بحث روز\nدر بحث تنوع فرهنگی و دسترسی، مدل دُم بلند هم وعدهٔ دموکراتیک‌شدن عرضه را نشان می‌دهد و هم خطر تمرکز توجه در دست الگوریتم‌های پلتفرم را یادآوری می‌کند."),
    ),
}

NAME_FIX = {}

YEAR_FIX = {
    "MC-062": "replaced media-economics template analysis with Porter-specific analysis; rebuilt recommendations without Latin leakage",
    "MC-174": "replaced media-economics template analysis with Ansoff-specific analysis; rebuilt recommendations",
    "MC-501": "replaced media-economics template analysis with Rochet-Tirole analysis; rebuilt recommendations without Latin leakage",
    "MC-503": "replaced media-economics template analysis with Baumol-Bowen analysis; rebuilt recommendations",
    "MC-504": "replaced media-economics template analysis with long-tail analysis; rebuilt recommendations",
}
