# -*- coding: utf-8 -*-
"""Batch 146 (MODEL): full documentation for MC-503, MC-504, MC-526, MC-531."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch146-model-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch146_model.json"

S = {
    "MC-503": [
        dict(kind="BOOK",
             title_en="Performing Arts: The Economic Dilemma",
             title_fa="هنرهای نمایشی: دشواری اقتصادی",
             authors="Baumol, W. J.; Bowen, W. G.", year=1966,
             publisher="The Twentieth Century Fund",
             doi=None,
             url="https://books.google.com/books/about/Performing_Arts.html?id=11JOA0gEACAAJ",
             language="en", isbn=None,
             citation="Baumol, W. J., & Bowen, W. G. (1966). Performing Arts: The Economic Dilemma. New York: The Twentieth Century Fund.",
             locator="book", locator_type="SECTION",
             supports="productivity lag and rising unit costs in labour-intensive performing arts", verified=True),
        dict(kind="BOOK_CHAPTER",
             title_en="Baumol's Cost Disease",
             title_fa="بیماری هزینهٔ بامول",
             authors="Heilbrun, J.", year=2003,
             publisher="Edward Elgar (A Handbook of Cultural Economics)",
             doi=None,
             url="https://repub.eur.nl/pub/782/TOWSE%20EBOOK_pages0103-0113.pdf",
             language="en", isbn=None,
             citation="Heilbrun, J. (2003). Baumol's cost disease. In R. Towse (Ed.), A Handbook of Cultural Economics (pp. 91-101). Cheltenham: Edward Elgar.",
             locator="pp. 91-101", locator_type="page_range",
             supports="scholarly restatement of the cost disease argument and its limits", verified=True),
    ],
    "MC-504": [
        dict(kind="WEBSITE",
             title_en="The Long Tail",
             title_fa="دُم بلند",
             authors="Anderson, C.", year=2004,
             publisher="Wired",
             doi=None,
             url="https://www.wired.com/2004/10/tail/",
             language="en", isbn=None,
             citation="Anderson, C. (2004, October). The long tail. Wired, 12(10).",
             locator="12(10)", locator_type="ISSUE",
             supports="niche aggregation and the economics of abundant distribution", verified=True),
        dict(kind="BOOK",
             title_en="The Long Tail: Why the Future of Business Is Selling Less of More",
             title_fa="دُم بلند: چرا آیندهٔ کسب‌وکار فروش کمتر از بیشتر است",
             authors="Anderson, C.", year=2006,
             publisher="Hyperion",
             doi=None,
             url="https://www.abebooks.com/9781401302375/Long-Tail-Why-Future-Business-1401302378/plp",
             language="en", isbn="9781401302375",
             citation="Anderson, C. (2006). The Long Tail: Why the Future of Business Is Selling Less of More. New York: Hyperion.",
             locator="book", locator_type="SECTION",
             supports="book-length statement of long-tail distribution economics", verified=True),
    ],
    "MC-526": [
        dict(kind="BOOK_CHAPTER",
             title_en="The Relevance of Algorithms",
             title_fa="ربط‌پذیری الگوریتم‌ها",
             authors="Gillespie, T.", year=2014,
             publisher="MIT Press (Media Technologies)",
             doi="10.7551/mitpress/9780262525374.003.0009",
             url="https://direct.mit.edu/books/edited-volume/3021/chapter/82555/The-Relevance-of-Algorithms",
             language="en", isbn=None,
             citation="Gillespie, T. (2014). The relevance of algorithms. In T. Gillespie, P. J. Boczkowski, & K. A. Foot (Eds.), Media Technologies: Essays on Communication, Materiality, and Society (pp. 167-194). Cambridge, MA: MIT Press.",
             locator="pp. 167-194", locator_type="page_range",
             supports="algorithms as culture and the production of calculated publics", verified=True),
        dict(kind="BOOK",
             title_en="If...Then: Algorithmic Power and Politics",
             title_fa="اگر... آنگاه: قدرت و سیاست الگوریتمی",
             authors="Bucher, T.", year=2018,
             publisher="Oxford University Press",
             doi=None,
             url="https://global.oup.com/academic/product/ifthen-9780190493035",
             language="en", isbn="9780190493035",
             citation="Bucher, T. (2018). If...Then: Algorithmic Power and Politics. New York: Oxford University Press.",
             locator="book", locator_type="SECTION",
             supports="algorithmic power, visibility and the shaping of everyday experience", verified=True),
    ],
    "MC-531": [
        dict(kind="OTHER",
             title_en="Language Models are Few-Shot Learners",
             title_fa="مدل‌های زبانی، یادگیرندگان چندنمونه‌ای",
             authors="Brown, T. B.; Mann, B.; Ryder, N.; Subbiah, M.; Kaplan, J.; Dhariwal, P.; et al.", year=2020,
             publisher="Advances in Neural Information Processing Systems 33 (NeurIPS 2020)",
             doi=None,
             url="https://arxiv.org/abs/2005.14165",
             language="en", isbn=None,
             citation="Brown, T. B., Mann, B., Ryder, N., Subbiah, M., Kaplan, J., Dhariwal, P., et al. (2020). Language models are few-shot learners. Advances in Neural Information Processing Systems, 33, 1877-1901.",
             locator="arXiv:2005.14165", locator_type="work",
             supports="large-scale generative language modelling that underpins media applications", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Collaborating With ChatGPT: Considering the Implications of Generative Artificial Intelligence for Journalism and Media Education",
             title_fa="همکاری با چت‌جی‌پی‌تی: ملاحظهٔ پیامدهای هوش مصنوعی مولد برای روزنامه‌نگاری و آموزش رسانه",
             authors="Pavlik, J. V.", year=2023,
             publisher="Journalism & Mass Communication Educator",
             doi="10.1177/10776958221149577",
             url="https://journals.sagepub.com/doi/abs/10.1177/10776958221149577",
             language="en", isbn=None,
             citation="Pavlik, J. V. (2023). Collaborating with ChatGPT: Considering the implications of generative artificial intelligence for journalism and media education. Journalism & Mass Communication Educator, 78(1), 84-93.",
             locator="78(1):84-93", locator_type="page_range",
             supports="capabilities and limits of generative AI for journalism practice and education", verified=True),
    ],
}

ENRICH = {
    "MC-503": dict(
        year=1966,
        summary="بیماری هزینهٔ بامول، که ویلیام بامول و ویلیام بوون در کتاب هنرهای نمایشی: دشواری اقتصادی در سال ۱۹۶۶ صورت‌بندی کردند، توضیح می‌دهد چرا هزینهٔ برخی خدمات فرهنگی و انسانی پیوسته از تورم عمومی جلو می‌زند. استدلال مرکزی این است که در بخش‌های کارمحور مانند اجرای زنده، آموزش و برخی خدمات رسانه‌ای، بهره‌وری نیروی کار به‌سختی افزایش می‌یابد؛ زیرا اجرای یک نمایش یا تدریس یک کلاس را نمی‌توان مانند تولید صنعتی چند برابر کرد. در همان حال، دستمزدها باید با سطح دستمزد بخش‌های بهره‌ور اقتصاد هم‌تراز بمانند، وگرنه نیروی کار جذب صنایع دیگر می‌شود. نتیجه آن است که شکاف میان هزینه و درآمد در این بخش‌ها پایدار می‌شود و سازمان‌های فرهنگی برای بقا به یارانه، کمک مالی یا افزایش قیمت بلیت نیاز پیدا می‌کنند. فناوری دیجیتال در توزیع و تکثیر محتوا این فشار را تا حدی جبران می‌کند، اما در تولید اصیل و اجرای زنده اثر محدودی دارد. نقدهای اصلی به مدل، ساده‌سازی سنجش بهره‌وری، نادیده‌گرفتن نوآوری سازمانی و فناورانه، تمرکز بر بخش‌های کارمحور و کم‌توجهی به بازار ستارگان و تغییر ساختار مصرف را برجسته می‌کنند.",
        definition="بیماری هزینهٔ بامول، شکاف پایدار میان رشد دستمزد و رشد بهره‌وری در خدمات کارمحور را توضیح می‌دهد و نشان می‌دهد چرا هزینهٔ تولید فرهنگی و رسانه‌ای بی‌وقفه بالا می‌رود.",
        main_problem="چرا هزینهٔ تولید در بخش‌های فرهنگی و کارمحور از تورم عمومی جلو می‌زند و این شکاف چه پیامدهایی برای بقا و سیاست‌گذاری این بخش‌ها دارد.",
        mechanism="دستمزدها با بهره‌وری کل اقتصاد بالا می‌روند، اما در اجرای زنده و خدمات انسانی بهره‌وری تقریباً ثابت می‌ماند؛ شکاف هزینه و درآمد پایدار می‌شود و یارانه یا افزایش قیمت، راه جبران می‌شود.",
        assumptions=[
            "اجرای زنده و خدمات انسانی کارمحورند.",
            "دستمزدها با بهره‌وری کل اقتصاد هم‌تراز می‌شوند.",
            "افزایش بهره‌وری در این بخش‌ها محدود است.",
            "شکاف هزینه و درآمد پایدار است.",
            "یارانه یا افزایش قیمت، راه جبران است.",
        ],
        principles=[
            "بهره‌وری بخش را با کل اقتصاد مقایسه کن.",
            "شکاف هزینه و درآمد را بلندمدت بسنج.",
            "نقش یارانه و کمک مالی را تحلیل کن.",
            "اثر فناوری دیجیتال بر توزیع را جدا کن.",
            "هزینهٔ تولید اصیل را از تکثیر تفکیک کن.",
            "قیمت‌گذاری را با کشش تقاضا هماهنگ کن.",
            "نقش فناوری دیجیتال در تولید اصیل را جداگانه بسنج.",
        ],
        critiques=[
            "سنجش بهره‌وری را ساده می‌کند.",
            "نوآوری سازمانی و فناورانه را کم‌می‌شمارد.",
            "بر بخش‌های کارمحور متمرکز است.",
            "بازار ستارگان و تغییر مصرف را نادیده می‌گیرد.",
            "یارانه را تنها راه‌حل تصویر می‌کند.",
        ],
        critique_text="منتقدان می‌گویند بیماری هزینهٔ بامول منطق فشار هزینه در فرهنگ و رسانه را روشن کرد اما سنجش بهره‌وری را ساده می‌کند و نقش نوآوری، بازار ستارگان و تحول دیجیتال را کم‌می‌شمارد؛ با این حال، چارچوب پایهٔ اقتصاد فرهنگ و سیاست یارانه است.",
        applications=[
            "تحلیل اقتصاد تئاتر و موسیقی زنده.",
            "سیاست‌گذاری یارانهٔ فرهنگی.",
            "تحلیل هزینهٔ تولید رسانهٔ خبری.",
            "برنامه‌ریزی مالی نهادهای فرهنگی.",
            "مطالعهٔ اثر دیجیتال بر هزینهٔ توزیع.",
        ],
        example_text="ارکستری که همان تعداد نوازنده و تمرین را برای هر کنسرت لازم دارد، نمی‌تواند هزینهٔ هر اجرا را با افزایش تولید کم کند؛ اما دستمزد نوازندگان باید با بازار کار هم‌تراز بماند. نتیجه، شکاف پایدار هزینه و درآمد و نیاز به یارانه یا افزایش قیمت بلیت است.",
        evolution="مدل در کتاب سال ۱۹۶۶ بامول و بوون شکل گرفت و بعدها به بخش‌های دیگر خدمات انسانی مانند آموزش و سلامت تعمیم یافت. در اقتصاد رسانه برای توضیح فشار هزینهٔ تولید خبر و محتوای اصیل به کار رفت و با تحول دیجیتال بازبینی شد.",
        key_concepts=["بیماری هزینه", "بهره‌وری", "اجرای زنده", "شکاف درآمد و هزینه", "یارانه", "کارمحوری"],
        theorists="ویلیام بامول و ویلیام بوون.",
        theorists_text="مدل در سنت اقتصاد فرهنگ و اقتصاد خدمات شکل گرفت.",
        model="شکاف پایدار رشد دستمزد و رشد بهره‌وری در خدمات کارمحور که هزینهٔ تولید فرهنگی را بی‌وقفه بالا می‌برد.",
        studies=[
            "کتاب سال ۱۹۶۶ شکاف هزینهٔ هنرهای نمایشی را مستند کرد.",
            "پژوهش سال ۲۰۰۳ بازخوانی انتقادی مدل را ارائه داد.",
            "مطالعات رسانه، فشار هزینهٔ تولید خبر را تحلیل کردند.",
            "پژوهش دیجیتال، اثر توزیع بر هزینه را سنجید.",
            "پژوهش اقتصاد سلامت، منطق بیماری هزینه را به خدمات درمانی تعمیم داد.",
        ],
    ),
    "MC-504": dict(
        year=2004,
        summary="مدل دُم بلند، که کریس اندرسون نخست در مقالهٔ سال ۲۰۰۴ در مجلهٔ وایرد و سپس در کتاب سال ۲۰۰۶ گسترد، تحول ساختار تقاضا در بازارهای محتوای دیجیتال را توضیح می‌دهد. استدلال مرکزی این است که کاهش هزینهٔ ذخیره‌سازی، توزیع و جست‌وجو، محدودیت قفسهٔ فروشگاه‌های فیزیکی را برمی‌دارد و عرضهٔ اقلام کم‌فروش را ممکن می‌سازد. در نتیجه، به‌جای تمرکز بر چند عنوان پرفروش، مجموعهٔ بزرگی از اقلام کم‌نمونه در دُم توزیع می‌تواند در مجموع درآمدی قابل توجه بسازد. الگوریتم‌های پیشنهاددهنده و جست‌وجو، تقاضا را به سمت این اقلام هدایت می‌کنند و هزینهٔ مبادله را کاهش می‌دهند. اندرسون این وضعیت را فرصتی برای تنوع فرهنگی و دسترسی به محتوای حاشیه‌ای می‌دید. با این حال، پژوهش‌های بعدی نشان دادند که توجه مخاطب همچنان به سرِ توزیع گرایش دارد و پلتفرم‌ها با الگوریتم و فهرست‌های برجسته، شکل تازه‌ای از دروازه‌بانی می‌سازند. نقدهای اصلی به مدل، اغراق در قدرت دُم، نادیده‌گرفتن توزیع نامتقارن توجه، وابستگی به زیرساخت پلتفرم، دشواری سنجش فروش اقلام کم‌نمونه و کم‌توجهی به هزینهٔ کشف محتوا را برجسته می‌کنند.",
        definition="مدل دُم بلند، کاهش هزینهٔ توزیع و ذخیره‌سازی دیجیتال را عامل رشد فروش اقلام کم‌نمونه می‌داند و استدلال می‌کند مجموع درآمد دُم می‌تواند با سرِ توزیع رقابت کند.",
        main_problem="چگونه کاهش هزینهٔ توزیع و جست‌وجو در بازار دیجیتال، اقتصاد اقلام کم‌فروش را ممکن می‌سازد و این تحول چه پیامدهایی برای تنوع فرهنگی و قدرت پلتفرم دارد.",
        mechanism="هزینهٔ ذخیره‌سازی و توزیع دیجیتال نزدیک به صفر می‌شود، عرضهٔ اقلام کم‌نمونه ممکن می‌شود و ابزارهای پیشنهاد و جست‌وجو تقاضا را به دُم هدایت می‌کنند؛ مجموع فروش دُم، درآمد معناداری می‌سازد.",
        assumptions=[
            "هزینهٔ توزیع دیجیتال پایین است.",
            "فضای عرضه در پلتفرم نامحدود است.",
            "پیشنهاددهی، تقاضای دُم را افزایش می‌دهد.",
            "مجموع اقلام کم‌فروش درآمدزا است.",
            "دسترسی به محتوای حاشیه‌ای گسترده می‌شود.",
        ],
        principles=[
            "هزینهٔ توزیع و ذخیره‌سازی را بسنج.",
            "عمق فهرست محتوا را گسترش بده.",
            "کیفیت پیشنهاددهی را بهبود بده.",
            "کشف محتوا را برای مخاطب آسان کن.",
            "درآمد دُم را جدا از سر تحلیل کن.",
            "قدرت دروازه‌بانی پلتفرم را رصد کن.",
            "هزینهٔ کشف محتوا را در محاسبهٔ کل درآمد لحاظ کن.",
            "اثر فهرست برجسته بر تقاضا را رصد کن.",
        ],
        critiques=[
            "قدرت دُم را بیش از واقع برمی‌آورد.",
            "توزیع نامتقارن توجه را نادیده می‌گیرد.",
            "به زیرساخت و سیاست پلتفرم وابسته است.",
            "سنجش فروش اقلام کم‌نمونه دشوار است.",
            "هزینهٔ کشف محتوا را کم‌می‌شمارد.",
            "نقش زیرساخت پلتفرم را در شکل‌دهی تقاضا کم‌بررسی می‌گذارد.",
        ],
        critique_text="منتقدان می‌گویند مدل دُم بلند اقتصاد توزیع دیجیتال را روشن کرد اما توجه مخاطب همچنان به سر بازار گرایش دارد و پلتفرم‌ها با الگوریتم، شکل تازه‌ای از دروازه‌بانی می‌سازند؛ با این حال، چارچوب پایهٔ تحلیل تنوع محتوای دیجیتال است.",
        applications=[
            "تحلیل اقتصاد پلتفرم‌های محتوا.",
            "سیاست‌گذاری تنوع فرهنگی و دسترسی.",
            "طراحی سامانهٔ پیشنهاد محتوا.",
            "مطالعهٔ بازار موسیقی و ویدیو.",
            "تحلیل فروش کتاب و محتوای نیچ.",
        ],
        example_text="پلتفرم پخش موسیقی که میلیون‌ها قطعهٔ کم‌شنیده را در کنار آهنگ‌های پرفروش عرضه می‌کند، از مجموع شنیدن‌های اقلام کم‌نمونه درآمد قابل توجهی می‌سازد؛ اما اگر الگوریتم صفحهٔ اصلی فقط پرفروش‌ها را نشان دهد، دُم در عمل به حاشیه می‌رود.",
        evolution="مقالهٔ سال ۲۰۰۴ اندرسون مفهوم را معرفی کرد و کتاب سال ۲۰۰۶ آن را گسترد. پژوهش‌های بعدی، محدودیت‌های تجربی مدل و نقش الگوریتم‌های پلتفرم در توزیع توجه را برجسته کردند و مفهوم به بحث تنوع فرهنگی و اقتصاد اشتراکی راه یافت.",
        key_concepts=["دُم بلند", "سر توزیع", "هزینهٔ توزیع", "پیشنهاددهی", "کشف محتوا", "تنوع فرهنگی"],
        theorists="کریس اندرسون.",
        theorists_text="مدل در سنت اقتصاد اینترنت و رسانهٔ دیجیتال شکل گرفت.",
        model="کاهش هزینهٔ توزیع و گسترش فهرست محتوا که فروش تجمعی اقلام کم‌نمونه را به منبع درآمد تبدیل می‌کند.",
        studies=[
            "مقالهٔ سال ۲۰۰۴ مفهوم دُم بلند را معرفی کرد.",
            "کتاب سال ۲۰۰۶ مدل را گسترد.",
            "پژوهش موسیقی، توزیع توجه را سنجید.",
            "مطالعات پلتفرم، دروازه‌بانی الگوریتمی را نقد کردند.",
            "پژوهش کتاب، اقتصاد فروش اقلام کم‌نمونه را مستند کرد.",
            "مطالعات تنوع فرهنگی، دسترسی به محتوای حاشیه‌ای را سنجیدند.",
        ],
    ),
    "MC-526": dict(
        year=2014,
        summary="نظریهٔ برچسب‌گذاری و امتیازدهی الگوریتمی، که تارلتون گیلسپی در فصل سال ۲۰۱۴ با عنوان ربط‌پذیری الگوریتم‌ها صورت‌بندی کرد و تاینا بوچر در کتاب سال ۲۰۱۸ گسترد، الگوریتم‌های پلتفرم را نه ابزار خنثی، بلکه سازندهٔ نظم اجتماعی و فرهنگی می‌داند. ادعای مرکزی این است که پلتفرم‌ها با محاسبهٔ ربط، برجستگی و رتبه، به محتوا و کاربران برچسب و امتیاز می‌دهند و از این راه تعیین می‌کنند چه چیزی دیده شود. گیلسپی شش بُعد برای این سازوکار برمی‌شمارد: الگوهای شمول، چرخه‌های پیش‌بینی، ارزیابی ربط، وعدهٔ عینیت الگوریتمی، درهم‌تنیدگی با عمل و تولید عموم محاسبه‌شده. نتیجه آن است که الگوریتم نه‌تنها محتوا را مرتب می‌کند، بلکه هویت و عموم‌ها را نیز شکل می‌دهد. بوچر با مفهوم قدرت الگوریتمی نشان می‌دهد که این نظم در تجربهٔ روزمره و ادراک کاربران نفوذ می‌کند. نقدهای اصلی به نظریه، خطر جبرگرایی زیرساختی، ابهام دوطرفهٔ الگوریتم و کاربر، جابه‌جایی سریع موضوع پژوهش، دشواری آزمون تجربی و کم‌توجهی به مقاومت و نظارت معکوس را برجسته می‌کنند.",
        definition="نظریهٔ برچسب‌گذاری و امتیازدهی الگوریتمی، محاسبهٔ ربط و رتبه‌بندی پلتفرم را سازندهٔ برجستگی، هویت و عموم می‌داند و الگوریتم را عاملی فرهنگی و سیاسی، نه ابزاری خنثی، تحلیل می‌کند.",
        main_problem="الگوریتم‌های پلتفرم چگونه با برچسب، امتیاز و رتبه‌بندی، تعیین می‌کنند چه چیزی دیده شود و این نظم محاسباتی چه پیامدهایی برای فرهنگ و سیاست دارد.",
        mechanism="پلتفرم داده و رفتار کاربران را در الگوهای شمول می‌گنجاند، ربط و برجستگی را محاسبه می‌کند و با رتبه و برچسب، محتوا و کاربران را دسته‌بندی می‌سازد؛ این دسته‌بندی، تجربه و ادراک کاربران را شکل می‌دهد و عموم محاسبه‌شده می‌سازد.",
        assumptions=[
            "الگوریتم سازندهٔ نظم اجتماعی است.",
            "ربط و برجستگی محاسبه‌پذیرند.",
            "برچسب و امتیاز، دسترسی را تعیین می‌کند.",
            "کاربران از منطق الگوریتم آگاه نیستند.",
            "عموم محاسبه‌شده محصول رتبه‌بندی است.",
        ],
        principles=[
            "الگوهای شمول داده را بررسی کن.",
            "معیار ربط و رتبه را آشکار کن.",
            "برچسب‌ها و امتیازها را مستند کن.",
            "وعدهٔ عینیت الگوریتمی را نقد کن.",
            "اثر رتبه‌بندی بر ادراک کاربر را بسنج.",
            "امکان مقاومت و نظارت معکوس را جدی بگیر.",
            "توزیع دادهٔ آموزشی را از نظر نمایندگی بسنج.",
            "اثر برچسب بر دسترسی گروه‌های حاشیه‌ای را بررسی کن.",
        ],
        critiques=[
            "خطر جبرگرایی زیرساختی دارد.",
            "ابهام الگوریتم و کاربر دوطرفه است.",
            "موضوع پژوهش سریع جابه‌جا می‌شود.",
            "آزمون تجربی ادعاها دشوار است.",
            "مقاومت مدنی را کم‌بررسی می‌گذارد.",
            "عاملیت کاربر در برابر رتبه‌بندی را کم‌بررسی می‌گذارد.",
        ],
        critique_text="منتقدان می‌گویند نظریهٔ برچسب‌گذاری الگوریتمی قدرت رتبه‌بندی پلتفرم را درست برجسته می‌کند اما گاه به تصویری جبرگرا از زیرساخت می‌رسد و عاملیت کاربر و مقاومت مدنی را کم‌می‌شمارد؛ با این حال، چارچوب اصلی نقد قدرت الگوریتمی است.",
        applications=[
            "تحلیل رتبه‌بندی و برجستگی در پلتفرم.",
            "پژوهش عموم محاسبه‌شده و ادراک کاربر.",
            "نقد شفافیت و پاسخ‌گویی الگوریتمی.",
            "آموزش سواد الگوریتمی.",
            "سیاست‌گذاری عدالت در سامانه‌های رتبه‌بندی.",
            "آموزش روزنامه‌نگاران برای فهم رتبه‌بندی پلتفرم.",
        ],
        example_text="موتور جست‌وجویی که نتیجه‌ای را در صفحهٔ اول نشان می‌دهد، به آن نتیجه برچسب اهمیت می‌زند؛ کاربر معمولاً صفحهٔ اول را واقعیت می‌پندارد، در حالی که رتبه محصول معیارهای محاسباتی پنهان است. این همان تولید برجستگی و عموم محاسبه‌شده است.",
        evolution="فصل گیلسپی در سال ۲۰۱۴ چارچوب ربط‌پذیری الگوریتمی را معرفی کرد و کتاب بوچر در سال ۲۰۱۸ قدرت الگوریتمی را در تجربهٔ روزمره گسترد. پس از آن، به چارچوب اصلی پژوهش انتقادی الگوریتم و سیاست شفافیت تبدیل شد.",
        key_concepts=["ربط‌پذیری الگوریتمی", "برچسب", "امتیاز", "عموم محاسبه‌شده", "قدرت الگوریتمی", "شفافیت"],
        theorists="تارلتون گیلسپی.",
        theorists_text="نظریه در سنت مطالعات علم و فناوری و نقد رسانهٔ دیجیتال شکل گرفت.",
        model="محاسبهٔ ربط و رتبه که با برچسب و امتیاز، برجستگی محتوا و هویت کاربران را می‌سازد و عموم محاسبه‌شده پدید می‌آورد.",
        studies=[
            "فصل سال ۲۰۱۴ شش بُعد ربط‌پذیری را معرفی کرد.",
            "کتاب سال ۲۰۱۸ قدرت الگوریتمی را گسترد.",
            "پژوهش پلتفرم، رتبه‌بندی را تحلیل کرد.",
            "مطالعات شفافیت، پاسخ‌گویی الگوریتمی را بررسی کردند.",
            "پژوهش جست‌وجو، اثر رتبه بر اعتماد کاربر را سنجید.",
            "مطالعات رسانهٔ اجتماعی، برجستگی الگوریتمی را تحلیل کردند.",
            "پژوهش سیاست، الزام شفافیت الگوریتمی را بررسی کرد.",
        ],
    ),
    "MC-531": dict(
        year=2020,
        summary="مدل هوش مصنوعی مولد در رسانه، تولید محتوای متنی، تصویری و صوتی با مدل‌های یادگیری عمیق را تحلیل می‌کند. نقطهٔ عطف این حوزه، پژوهش سال ۲۰۲۰ براون و همکاران دربارهٔ مدل‌های زبانی بزرگ بود که نشان داد مدل با آموزش بر پیکرهٔ عظیم متن، می‌تواند بدون آموزش ویژه برای هر وظیفه، متن تازه تولید کند. این مدل‌ها بر پایهٔ احتمال توزیع واژه‌ها کار می‌کنند و خروجی آن‌ها بازتولید آماری الگوهای آموخته‌شده است، نه فهم تضمین‌شدهٔ واقعیت. در رسانه، این فناوری برای پیش‌نویس خبر، خلاصه‌سازی، ترجمه، تیترسازی، روایت داده و تولید تصویر به کار رفت و پژوهش سال ۲۰۲۳ پاولیک ظرفیت‌ها و محدودیت‌های آن را برای روزنامه‌نگاری و آموزش رسانه بررسی کرد. مزیت‌های اعلام‌شده شامل سرعت، کاهش هزینه و آزادکردن زمان برای تحلیل است. با این حال، خطر تولید اطلاعات نادرست، توهم مدل، سوگیری دادهٔ آموزشی، نقض حق مؤلف، شفافیت نداشتن و تضعیف اعتماد خبری جدی است. نقدهای اصلی به این حوزه، جبرگرایی فناورانه، ناهمگنی ابزارها، تمرکز بر نمونه‌های تجاری غربی و کم‌توجهی به کار و مسئولیت انسانی را برجسته می‌کنند.",
        definition="مدل هوش مصنوعی مولد در رسانه، تولید خودکار متن، تصویر و صدا با مدل‌های یادگیری عمیق را توصیف می‌کند که بر پایهٔ الگوهای آماری پیکرهٔ آموزشی، محتوای تازه می‌سازند و پرسش‌های تازه‌ای دربارهٔ صحت، نویسندگی و مسئولیت پدید می‌آورند.",
        main_problem="مدل‌های مولد چگونه تولید محتوای رسانه‌ای را دگرگون می‌کنند و چه پیامدهایی برای صحت، نویسندگی، کار خبری و اعتماد عمومی دارند.",
        mechanism="مدل بر پیکرهٔ عظیم داده آموزش می‌بیند و با پیش‌بینی احتمال واژه یا پیکسل، خروجی تازه تولید می‌کند؛ کاربر با دستور متنی خروجی را هدایت می‌کند و بازبینی انسانی برای صحت و زمینه لازم می‌ماند.",
        assumptions=[
            "تولید محتوا را می‌توان آماری مدل کرد.",
            "پیکرهٔ آموزشی، الگوهای زبانی را بازنمایی می‌کند.",
            "دستور متنی، خروجی را هدایت‌پذیر می‌کند.",
            "سرعت و مقیاس، ارزش رسانه‌ای می‌سازد.",
            "بازبینی انسانی، صحت را تضمین می‌کند.",
        ],
        principles=[
            "خروجی مولد را پیش از انتشار بازبینی کن.",
            "منبع و روش تولید را شفاف کن.",
            "توهم و خطای مدل را پیش‌بینی کن.",
            "سوگیری دادهٔ آموزشی را بسنج.",
            "حق مؤلف و مالکیت خروجی را روشن کن.",
            "مسئولیت انسانی انتشار را حفظ کن.",
            "پیامدهای کار و اشتغال خبرنگاران را در ارزیابی لحاظ کن.",
        ],
        critiques=[
            "جبرگرایی فناورانه در تحلیل رایج است.",
            "ابزارها و کاربردها بسیار ناهمگن‌اند.",
            "نمونه‌ها عمدتاً تجاری و غربی‌اند.",
            "پیامدهای کار و اشتغال کم‌بررسی است.",
            "شفافیت مدل‌های تجاری محدود است.",
            "پاسخ‌گویی خطای مدل را کم‌بررسی می‌گذارد.",
        ],
        critique_text="منتقدان می‌گویند پژوهش هوش مصنوعی مولد در رسانه گاه فناوری را عامل تعیین‌کننده می‌داند و انتخاب‌های انسانی نهفته در داده، طراحی و کار را نادیده می‌گیرد؛ با این حال، پرسش‌های مهمی دربارهٔ صحت، نویسندگی و مسئولیت خبری گشود.",
        applications=[
            "پیش‌نویس و خلاصه‌سازی خبر.",
            "ترجمه و تیترسازی چندزبانه.",
            "تولید تصویر و ویدیوی خبری.",
            "روایت داده و گزارش‌های خودکار.",
            "آموزش سواد هوش مصنوعی به خبرنگاران.",
        ],
        example_text="خبرگزاری‌ای با مدل زبانی، پیش‌نویس گزارش دادهٔ اقتصادی را در چند دقیقه می‌سازد؛ خبرنگار آمار را راستی‌آزمایی می‌کند، زمینه را می‌افزاید و مسئولیت انتشار را می‌پذیرد. اگر همان پیش‌نویس بدون بازبینی منتشر شود، توهم مدل به خبر نادرست تبدیل می‌شود.",
        evolution="پژوهش سال ۲۰۲۰ مدل‌های زبانی بزرگ را معرفی کرد و با انتشار عمومی ابزارهای مولد در سال‌های بعد، کاربرد رسانه‌ای گسترش یافت. پژوهش سال ۲۰۲۳ پاولیک ظرفیت و محدودیت آن را برای روزنامه‌نگاری تحلیل کرد و از آن پس، سیاست‌های شفافیت و بازبینی در خبرگزاری‌ها شکل گرفت.",
        key_concepts=["هوش مصنوعی مولد", "مدل زبانی بزرگ", "دستور متنی", "توهم مدل", "محتوای ترکیبی", "بازبینی انسانی", "شفافیت"],
        theorists="تام براون و همکاران.",
        theorists_text="حوزه در سنت یادگیری عمیق و مطالعات روزنامه‌نگاری دیجیتال شکل گرفت.",
        model="زنجیرهٔ دادهٔ آموزشی، مدل مولد، دستور متنی و بازبینی انسانی که تولید محتوای رسانه‌ای را دگرگون می‌کند.",
        studies=[
            "پژوهش سال ۲۰۲۰ مدل‌های زبانی بزرگ را معرفی کرد.",
            "پژوهش سال ۲۰۲۳ ظرفیت و محدودیت خبری را تحلیل کرد.",
            "مطالعات خبرگزاری، کاربرد مولد را نگاشت کردند.",
            "پژوهش کیفیت، خوانش مخاطب از محتوای مولد را سنجید.",
        ],
    ),
}

NAME_FIX = {
    "MC-503": ("بیماری هزینهٔ بامول", "Baumol's Cost Disease", "عنوان پیشین «هزینه و بیماری هزینه» تکرار واژه و مبهم بود؛ نام متعارف مفهوم در ادبیات اقتصاد فرهنگ ثبت شد."),
    "MC-526": ("نظریهٔ برچسب‌گذاری و امتیازدهی الگوریتمی", "Algorithmic Labeling and Scoring Theory", "عنوان پیشین با خط تیرهٔ مبهم نوشته شده بود؛ «و» جایگزین شد تا دو سازوکار برچسب و امتیاز روشن شود."),
}
YEAR_FIX = {
    "MC-531": "سال ۲۰۲۰ به انتشار پژوهش بنیادی مدل‌های زبانی بزرگ اشاره دارد؛ متن core_logic کارت از الگوی نظریهٔ پلتفرم آمده و با عنوان کارت هم‌خوان نیست، بنابراین مستندسازی بر پایهٔ عنوان و منابع معتبر بازسازی شد.",
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
                                       "verified": n_verified, "batch": 146}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH146 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
