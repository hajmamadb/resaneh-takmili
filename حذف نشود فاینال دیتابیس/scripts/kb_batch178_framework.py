# -*- coding: utf-8 -*-
"""Batch 178 (WORK + METHOD): MC-639 rally effect, MC-072 content analysis, MC-073 triangulation, MC-234 participatory action research."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch178-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch178.json"

WORK_MAPPING = {"entity_type": "WORK", "content_type": "اثر رسانه‌ای (پدیده)", "needs_review": False}
METHOD_MAPPING = {"entity_type": "METHOD", "content_type": "روش پژوهش (Research Method)", "needs_review": False}

S = {
    "MC-639": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Presidential Popularity from Truman to Johnson",
             title_fa="محبوبیت ریاست‌جمهوری از ترومن تا جانسون",
             authors="Mueller, J. E.", year=1970,
             publisher="American Political Science Review, 64(1), 18-34",
             doi="10.2307/1955610",
             url="https://doi.org/10.2307/1955610",
             language="en", isbn=None,
             citation="Mueller, J. E. (1970). Presidential popularity from Truman to Johnson. American Political Science Review, 64(1), 18-34.",
             locator="64(1), pp. 18-34", locator_type="page_range",
             supports="original time-series evidence for post-crisis popularity rallies", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Patriotism or Opinion Leadership? The Nature and Origins of the Rally 'Round the Flag Effect",
             title_fa="میهن‌گرایی یا رهبری افکار؟ ماهیت و خاستگاه اثر گردهمایی دور پرچم",
             authors="Baker, W. D., & Oneal, J. R.", year=2001,
             publisher="Journal of Conflict Resolution, 45(5), 661-687",
             doi="10.1177/0022002701045005006",
             url="https://doi.org/10.1177/0022002701045005006",
             language="en", isbn=None,
             citation="Baker, W. D., & Oneal, J. R. (2001). Patriotism or opinion leadership? The nature and origins of the rally 'round the flag effect. Journal of Conflict Resolution, 45(5), 661-687.",
             locator="45(5), pp. 661-687", locator_type="page_range",
             supports="media coverage, bipartisan support and White House spin as rally mechanisms", verified=True),
    ],
    "MC-072": [
        dict(kind="BOOK",
             title_en="Content Analysis in Communication Research",
             title_fa="تحلیل محتوا در پژوهش ارتباطات",
             authors="Berelson, B.", year=1952,
             publisher="Free Press",
             doi=None,
             url="https://archive.org/details/contentanalysisi0000bern",
             language="en", isbn=None,
             citation="Berelson, B. (1952). Content Analysis in Communication Research. Glencoe, IL: Free Press.",
             locator="whole book", locator_type="book",
             supports="foundational formulation of content analysis for communication research", verified=True),
        dict(kind="BOOK",
             title_en="Content Analysis: An Introduction to Its Methodology",
             title_fa="تحلیل محتوا: درآمدی بر روش‌شناسی آن",
             authors="Krippendorff, K.", year=1980,
             publisher="SAGE Publications",
             doi=None,
             url=None,
             language="en", isbn=None,
             citation="Krippendorff, K. (1980). Content Analysis: An Introduction to Its Methodology. Beverly Hills, CA: SAGE Publications.",
             locator="whole book", locator_type="book",
             supports="methodological framework: unitizing, categories, reliability, inference", verified=True),
    ],
    "MC-073": [
        dict(kind="BOOK",
             title_en="The Research Act: A Theoretical Introduction to Sociological Methods",
             title_fa="کنش پژوهش: درآمدی نظری بر روش‌های جامعه‌شناختی",
             authors="Denzin, N. K.", year=1978,
             publisher="McGraw-Hill",
             doi=None,
             url="https://books.google.com/books/about/The_Research_Act.html?id=gfS1AAAAIAAJ",
             language="en", isbn="0070163618",
             citation="Denzin, N. K. (1978). The Research Act: A Theoretical Introduction to Sociological Methods (2nd ed.). New York: McGraw-Hill.",
             locator="2nd edition", locator_type="book",
             supports="fourfold typology of triangulation: data, investigator, theory, method", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Mixing Qualitative and Quantitative Methods: Triangulation in Action",
             title_fa="ترکیب روش‌های کیفی و کمّی: سه‌سوسازی در عمل",
             authors="Jick, T. D.", year=1979,
             publisher="Administrative Science Quarterly, 24(4), 602-611",
             doi="10.2307/2392366",
             url="https://doi.org/10.2307/2392366",
             language="en", isbn=None,
             citation="Jick, T. D. (1979). Mixing qualitative and quantitative methods: Triangulation in action. Administrative Science Quarterly, 24(4), 602-611.",
             locator="24(4), pp. 602-611", locator_type="page_range",
             supports="practical demonstration of convergent and divergent triangulation", verified=True),
    ],
    "MC-234": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Action Research and Minority Problems",
             title_fa="پژوهش کنش و مسائل اقلیت‌ها",
             authors="Lewin, K.", year=1946,
             publisher="Journal of Social Issues, 2(4), 34-46",
             doi="10.1111/j.1540-4560.1946.tb02295.x",
             url="https://doi.org/10.1111/j.1540-4560.1946.tb02295.x",
             language="en", isbn=None,
             citation="Lewin, K. (1946). Action research and minority problems. Journal of Social Issues, 2(4), 34-46.",
             locator="2(4), pp. 34-46", locator_type="page_range",
             supports="origin of the action-research cycle and participatory inquiry", verified=True),
        dict(kind="BOOK",
             title_en="The SAGE Handbook of Action Research: Participative Inquiry and Practice",
             title_fa="راهنمای پژوهش کنش: کاوش و عمل مشارکتی",
             authors="Reason, P., & Bradbury, H. (Eds.)", year=2008,
             publisher="SAGE Publications",
             doi=None,
             url="https://methods.sagepub.com/book/edvol/the-sage-handbook-of-action-research/toc",
             language="en", isbn=None,
             citation="Reason, P., & Bradbury, H. (Eds.). (2008). The SAGE Handbook of Action Research: Participative Inquiry and Practice (2nd ed.). London: SAGE Publications.",
             locator="2nd edition", locator_type="book",
             supports="consolidation of participatory and critical action-research traditions", verified=True),
    ],
}

ENRICH = {
    "MC-639": dict(
        year=1970,
        mapping=WORK_MAPPING,
        summary="اثر گردهمایی دور پرچم افزایش موقت و نسبتاً یکنواخت محبوبیت رئیس‌جمهور یا رهبر سیاسی در پی رویدادهای بین‌المللی تنش‌زاست. مولر در سال ۱۹۷۰ با تحلیل نظرسنجی‌های گالوپ از ترومن تا جانسون نشان داد محبوبیت ریاست‌جمهوری پس از بحران‌های خارجی کوتاه‌مدت بالا می‌رود و سپس به روند نزولی بازمی‌گردد. او این جهش را به همبستگی ملی در برابر تهدید بیرونی نسبت داد و کوشید آن را از روند عمومی فرسایش محبوبیت جدا کند. بیکر و اونیل در سال ۲۰۰۱ پرسیدند آیا این افزایش محصول میهن‌گرایی توده است یا رهبری افکار؛ آنان نشان دادند پوشش رسانه‌ای همسو، حمایت دوحزبی و مدیریت خبری کاخ سفید در تولید این جهش نقش دارند و اندازهٔ اثر با درجهٔ توجه رسانه‌ها و اجماع نخبگان رابطه دارد. سازوکار آن ترکیبی از کاهش نقد درونی، برجسته‌شدن هویت ملی و تمرکز رسانه‌ای بر تهدید است. اثر معمولاً چند هفته تا چند ماه می‌پاید و با تداوم بحران یا دوقطبی شدن نخبگان فرومی‌ریزد. نقدها بر تعریف عملیاتی رویداد، انتخاب گزینشی موارد و نادیده گرفتن تفاوت رسانه‌ای میان کشورها تأکید دارند.",
        definition="اثر گردهمایی دور پرچم عبارت است از افزایش موقت و قابل اندازه‌گیری حمایت عمومی از رهبر سیاسی در پی تهدید بیرونی، بحران بین‌المللی یا رویداد امنیتی که همبستگی ملی را برجسته می‌کند.",
        main_problem="چرا بحران‌های بیرونی نقد داخلی را موقتاً فرو می‌نشانند و محبوبیت رهبر را بالا می‌برند، و چه شرایطی این همبستگی کوتاه‌عمر را تقویت یا تضعیف می‌کند.",
        mechanism="تهدید بیرونی نقد درونی را هزینه‌دار می‌کند؛ رسانه‌ها توجه را بر رویداد و رهبر متمرکز می‌کنند، هویت ملی برجسته می‌شود و مخالفان سیاسی موقتاً سکوت می‌کنند، بنابراین حمایت عمومی جهش می‌کند و با فروکش تهدید و بازگشت رقابت نخبگان به روند پیشین برمی‌گردد.",
        assumptions=[
            "رخداد بیرونی به‌طور مستقل از رهبر قابل شناسایی است.",
            "محبوبیت پیش و پس از رویداد با نظرسنجی سنجیده می‌شود.",
            "رسانه‌ها رویداد را برجسته و همسو پوشش می‌دهند.",
            "نخبگان سیاسی موقتاً از نقد دست می‌کشند.",
            "هویت ملی در بحران برجسته می‌شود.",
            "جهش موقت است و روند بلندمدت را تغییر نمی‌دهد.",
            "شدت تهدید با اندازهٔ جهش رابطه دارد.",
            "روند پایه محبوبیت با فرسایش تدریجی توضیح‌پذیر است.",
        ],
        principles=[
            "رویداد محرک را پیش از تحلیل دقیق تعریف کن.",
            "روند پایه را از جهش کوتاه‌مدت جدا کن.",
            "پوشش رسانه‌ای را هم‌زمان با نظرسنجی بسنج.",
            "اجماع نخبگان را متغیر میانجی بگیر.",
            "پنجرهٔ زمانی اثر را مشخص کن.",
            "موارد ناهمسو را نیز در تحلیل بگنجان.",
        ],
        critiques=[
            "تعریف عملیاتی رویداد محرک مبهم است.",
            "انتخاب موارد در نمونه‌های تاریخی گزینشی است.",
            "سنجش محبوبیت به کیفیت نظرسنجی وابسته است.",
            "سهم رسانه از میهن‌گرایی تفکیک نمی‌شود.",
            "تعمیم نتایج یک کشور به دیگر نظام‌ها محدود است.",
            "جهش‌های کوچک از نوسان نمونه قابل تفکیک نیست.",
        ],
        critique_text="منتقدان می‌گویند اثر گردهمایی بیشتر یک برچسب توصیفی است تا سازوکار علّی؛ رویداد محرک را پس از وقوع انتخاب می‌کنیم و همین انتخاب گزینشی جهش را بزرگ‌تر نشان می‌دهد. با این حال مولر و بیکر و اونیل نشان دادند جهش پس از بحران‌های مشخص و در داده‌های سری زمانی تکرارشدنی است.",
        applications=[
            "تحلیل محبوبیت رئیس‌جمهور در بحران‌های خارجی.",
            "پژوهش ارتباطات سیاسی و مدیریت بحران.",
            "سنجش اثر پوشش خبری جنگ و تروریسم.",
            "تحلیل افکار عمومی پیش از انتخابات.",
            "مطالعهٔ همبستگی ملی پس از حملات.",
            "ارزیابی راهبرد مدیریت خبری دولت.",
            "پژوهش روابط بین‌الملل و افکار عمومی.",
            "تحلیل نوسان اعتماد به نهادهای امنیتی.",
            "مطالعهٔ سکوت موقت مخالفان سیاسی.",
            "پژوهش اثر چارچوب‌بندی تهدید.",
            "تحلیل محبوبیت رهبر در بحران بهداشتی.",
            "مطالعهٔ مقایسه‌ای بحران در کشورهای گوناگون.",
        ],
        example_text="پس از یک حملهٔ تروریستی، محبوبیت رئیس‌جمهور در نظرسنجی هفتگی چند واحد بالا می‌رود، رسانه‌ها بر وحدت ملی تأکید می‌کنند و رقیبان سیاسی انتقاد را عقب می‌اندازند؛ چند هفته بعد با بازگشت بحث‌های داخلی، محبوبیت به روند پیشین برمی‌گردد.",
        evolution="مولر در ۱۹۷۰ الگوی جهش را کمّی کرد؛ پژوهش‌های بعدی آن را به جنگ، بحران گروگان‌گیری، بلایای طبیعی و بحران بهداشتی گستراندند و بیکر و اونیل در ۲۰۰۱ نقش رسانه و اجماع نخبگان را برجسته کردند.",
        key_concepts=["تهدید بیرونی", "همبستگی ملی", "محبوبیت ریاست‌جمهوری", "پوشش همسو", "اجماع نخبگان", "جهش موقت"],
        theorists="جان مولر، ویلیام بیکر و جان اونیل.",
        theorists_text="مولر اثر را با داده‌های نظرسنجی صورت‌بندی کرد و بیکر و اونیل سازوکار رسانه‌ای و نخبگانی آن را بسط دادند.",
        model="مدل تهدید و همبستگی: رویداد بیرونی توجه رسانه را متمرکز می‌کند، نقد درونی را پرهزینه می‌سازد و حمایت عمومی را موقتاً بالا می‌برد.",
        studies=[
            "تحلیل مولر از نظرسنجی‌های ترومن تا جانسون در ۱۹۷۰.",
            "پژوهش بیکر و اونیل در ۲۰۰۱.",
            "مطالعات بحران جنگ کره و بحران موشکی کوبا.",
            "تحلیل افکار عمومی پس از حملات یازده سپتامبر.",
            "پژوهش بحران گروگان‌گیری.",
            "مطالعهٔ بحران کرونا و اعتماد به دولت.",
            "تحلیل پوشش خبری جنگ عراق.",
            "پژوهش مقایسه‌ای بحران در دموکراسی‌های نوپا.",
            "مطالعهٔ سکوت مخالفان در بحران امنیتی.",
            "تحلیل چارچوب‌بندی تهدید در تلویزیون.",
            "پژوهش اثر بلایای طبیعی بر محبوبیت.",
            "مطالعهٔ تفاوت حزبی در اندازهٔ جهش.",
            "تحلیل بازگشت روند پس از فروکش بحران.",
        ],
    ),
    "MC-072": dict(
        year=1980,
        mapping=METHOD_MAPPING,
        summary="تحلیل محتوا روشی نظام‌مند برای تبدیل متن، تصویر، صدا یا هر محتوای نمادین به داده‌های قابل شمارش و تفسیرپذیر است. برلسون در سال ۱۹۵۲ آن را در پژوهش ارتباطات صورت‌بندی کرد و تحلیل محتوای آشکار را با شمارش مقوله‌های تعریف‌شده پیش برد. کریپندورف در سال ۱۹۸۰ چارچوب روش‌شناختی منسجم‌تری ساخت: واحد تحلیل، مقوله‌بندی، اعتبار، پایایی میان کدگذاران و استنباط از متن به زمینه را در یک فرایند چرخه‌ای به هم پیوند داد. امروز تحلیل محتوا هم نسخهٔ کمّی و هم نسخهٔ کیفی و هم نسخهٔ رایانشی دارد. مراحل آن تعیین پرسش، انتخاب نمونه، تعریف واحد تحلیل، ساخت مقوله‌ها، آموزش کدگذاران، آزمون پایایی، کدگذاری و گزارش است. پایایی با توافق میان کدگذاران سنجیده می‌شود و اعتبار به تناسب مقوله‌ها با مفهوم و زمینه بستگی دارد. تحلیل محتوا با نشانه‌شناسی، تحلیل گفتمان و تحلیل چارچوب مرز مشترک دارد اما در سنجه‌پذیری و تکرارپذیری متمایز می‌شود. نقدها بر تقلیل معنا به شمارش، حساسیت به زمینهٔ رمزگذاری و شفافیت مقوله‌سازی تأکید دارند.",
        definition="تحلیل محتوا مجموعهٔ روش‌های نظام‌مند برای توصیف عینی، کمّی یا کیفی محتوای آشکار و پنهان پیام‌ها بر پایهٔ مقوله‌های تعریف‌شده و قابل تکرار است.",
        main_problem="چگونه می‌توان حجم انبوه پیام‌های رسانه‌ای را به داده‌های معتبر، قابل تکرار و قابل مقایسه تبدیل کرد بی‌آنکه معنا و زمینهٔ پیام از دست برود.",
        mechanism="پژوهشگر پرسش و نمونه را تعیین می‌کند، واحد تحلیل و مقوله‌ها را می‌سازد، کدگذاران را آموزش می‌دهد، پایایی را با نمونهٔ آزمون می‌سنجد، سپس کل نمونه را کدگذاری و داده را با آمار توصیفی یا تحلیلی تفسیر می‌کند؛ بازخورد مرحلهٔ پایایی به بازتعریف مقوله‌ها برمی‌گردد.",
        assumptions=[
            "پیام‌ها ویژگی‌های قابل تعریف و قابل مشاهده دارند.",
            "مقوله‌ها را می‌توان پیش از کدگذاری روشن کرد.",
            "کدگذاران آموزش‌دیده به نتیجهٔ مشابه می‌رسند.",
            "نمونهٔ منتخب نمایندهٔ جامعهٔ پیام‌ها است.",
            "شمارش فراوانی معنای ارتباطی دارد.",
            "زمینهٔ تولید و دریافت در تفسیر دخیل است.",
            "پایایی پیش‌شرط اعتبار است.",
            "مقوله‌ها می‌توانند هم توصیفی و هم تحلیلی باشند.",
        ],
        principles=[
            "پرسش پژوهش را پیش از ساخت مقوله روشن کن.",
            "واحد تحلیل و واحد نمونه‌گیری را جدا تعریف کن.",
            "مقوله‌ها را جامع و مانع بساز.",
            "پایایی کدگذاران را پیش از کدگذاری نهایی بسنج.",
            "نمونهٔ تصادفی یا هدفمند را مستند کن.",
            "استنباط را از توصیف جدا نگه دار.",
            "کدگذاری را با پرسش کانونی سازگار کن.",
        ],
        critiques=[
            "شمارش فراوانی با اهمیت معنا یکی گرفته می‌شود.",
            "مقوله‌سازی پژوهشگر را به متن تحمیل می‌کند.",
            "پایایی به آموزش و تجربهٔ کدگذار حساس است.",
            "تحلیل محتوای کیفی با نسخهٔ کمّی اشتباه می‌شود.",
            "متن‌های چندرسانه‌ای و طنز سخت مقوله‌بندی می‌شوند.",
            "شفافیت گزارش نمونه و کدگذاری ناکافی است.",
        ],
        critique_text="منتقدان می‌گویند تحلیل محتوا معنا را به شمارش فرو می‌کاهد و مقوله‌های از پیش ساخته، آنچه در متن نیست را به آن تحمیل می‌کنند؛ همچنین پایایی بالا به معنای اعتبار نیست. با این حال برلسون و کریپندورف پایایی، اعتبار و استنباط را در یک چارچوب روشن به هم گره زدند و روش را از شمارش سادهٔ کلمات جدا کردند.",
        applications=[
            "تحلیل بازنمایی گروه‌ها در اخبار.",
            "سنجش چارچوب‌بندی رسانه‌ای.",
            "پژوهش تبلیغات و محتوای برند.",
            "تحلیل گفت‌وگو در شبکه‌های اجتماعی.",
            "بررسی تبلیغات انتخاباتی.",
            "مطالعهٔ تصویرسازی در فیلم و سریال.",
            "تحلیل محتوای کتاب درسی.",
            "پایش نفرت‌پراکنی در پلتفرم‌ها.",
            "پژوهش سلامت و پوشش خبری بیماری.",
            "تحلیل محتوای وب‌سایت سازمان‌ها.",
            "بررسی کیفیت خبر و منابع.",
            "مطالعهٔ بازنمایی جنسیت.",
            "تحلیل خودکار متون با روش‌های رایانشی.",
        ],
        example_text="پژوهشگری هزار تیتر خبری دربارهٔ مهاجرت را از سه خبرگزاری نمونه‌گیری می‌کند، پنج مقولهٔ بازنمایی می‌سازد، دو کدگذار مستقل ده‌درصد نمونه را کد می‌کنند و آلفای توافق را می‌سنجند؛ پس از رسیدن به توافق، کل نمونه کدگذاری می‌شود.",
        evolution="برلسون در ۱۹۵۲ تحلیل محتوای ارتباطات را نظام‌مند کرد؛ کریپندورف در ۱۹۸۰ چارچوب روش‌شناختی و سنجهٔ پایایی را گسترد و از دههٔ ۲۰۰۰ روش‌های رایانشی و یادگیری ماشین تحلیل متن بزرگ را ممکن کردند.",
        key_concepts=["واحد تحلیل", "مقوله‌بندی", "پایایی کدگذاران", "اعتبار", "نمونه‌گیری پیام", "استنباط از متن"],
        theorists="برنارد برلسون و کلاوس کریپندورف.",
        theorists_text="برلسون سنت تحلیل محتوای ارتباطات را بنیان گذاشت و کریپندورف چارچوب روش‌شناختی و سنجه‌های پایایی آن را تدوین کرد.",
        model="چرخهٔ تحلیل محتوا: پرسش، نمونه، مقوله، آموزش کدگذار، آزمون پایایی، کدگذاری، تحلیل و بازگشت اصلاحی به مقوله‌ها.",
        studies=[
            "تحلیل برلسون از محتوای تبلیغات سیاسی.",
            "چارچوب کریپندورف در ۱۹۸۰.",
            "پژوهش آلفای کریپندورف.",
            "تحلیل بازنمایی مهاجران در خبر.",
            "مطالعهٔ چارچوب‌بندی انتخابات.",
            "تحلیل محتوای تبلیغات تلویزیونی.",
            "پژوهش کیفیت خبر آنلاین.",
            "تحلیل محتوای رسانه‌های اجتماعی.",
            "مطالعهٔ خشونت در فیلم.",
            "تحلیل کتاب‌های درسی.",
            "پژوهش بازنمایی جنسیت.",
            "تحلیل تطبیقی چند کشور.",
            "پژوهش تحلیل محتوای خودکار.",
        ],
    ),
    "MC-073": dict(
        year=1978,
        mapping=METHOD_MAPPING,
        summary="سه‌سوسازی استفادهٔ هم‌زمان از دو یا چند روش، منبع داده، پژوهشگر یا نظریه برای بررسی یک پدیده است تا اعتبار یافته‌ها با همگرایی شواهد مستقل افزایش یابد. دنزین در سال ۱۹۷۸ در کتاب کنش پژوهش چهار گونهٔ آن را از هم جدا کرد: سه‌سوسازی داده، پژوهشگر، نظریه و روش‌شناختی. جیک در سال ۱۹۷۹ نشان داد ترکیب روش کمّی و کیفی نه‌تنها خطای یک روش را جبران می‌کند، بلکه زوایای ناهمسازی را هم آشکار می‌سازد و تفسیر غنی‌تری می‌سازد. منطق آن این است که نقاط قوت یک روش ضعف روش دیگر را می‌پوشاند. سه‌سوسازی می‌تواند همگرا، مکمل یا ناهمساز باشد و ناهمسازی خود دادهٔ تحلیلی است. امروز سه‌سوسازی در پژوهش ترکیبی، ارزیابی برنامه، تحلیل دادهٔ چندمنبعی و پژوهش رسانه به کار می‌رود. نقدها بر هزینه، پیچیدگی و این باور که ترکیب همیشه اعتبار می‌آورد تأکید دارند.",
        definition="سه‌سوسازی بهره‌گیری هم‌زمان از چند روش، منبع، پژوهشگر یا چارچوب نظری برای مطالعهٔ یک پدیده و سنجش همگرایی یا ناهمسازی شواهد است.",
        main_problem="چگونه می‌توان اطمینان یافت که یافتهٔ یک روش، ویژگی پدیده است و نه محصول ابزار، نمونه یا سوگیری پژوهشگر.",
        mechanism="هر روش خطا و سوگیری خاص خود را دارد؛ وقتی چند روش مستقل به نتیجهٔ مشابه برسند احتمال خطای مشترک کاهش می‌یابد و اگر نتایج ناهمسو باشند پژوهشگر به بازبینی مفهوم، ابزار یا زمینه هدایت می‌شود.",
        assumptions=[
            "خطاهای روش‌های گوناگون مستقل از هم است.",
            "همگرایی شواهد نشانهٔ اعتبار است.",
            "ناهمسازی اطلاعات تحلیلی دارد.",
            "هر روش بخشی از پدیده را می‌بیند.",
            "پژوهشگر می‌تواند نتایج را معنادار ترکیب کند.",
            "منابع داده مستقل از هم گردآوری می‌شوند.",
            "هزینهٔ افزوده با دقت افزوده توجیه می‌شود.",
            "رویکرد هم برای کمّی و هم کیفی کاربرد دارد.",
        ],
        principles=[
            "هدف ترکیب را پیش از اجرا روشن کن.",
            "نقاط قوت و ضعف هر روش را بنویس.",
            "استقلال منابع را حفظ کن.",
            "ناهمسازی را پنهان نکن.",
            "وزن شواهد را شفاف کن.",
            "هزینه و زمان را در طرح بگنجان.",
        ],
        critiques=[
            "ترکیب روش‌ها همیشه اعتبار نمی‌آورد.",
            "هزینه و زمان پژوهش را چند برابر می‌کند.",
            "استقلال واقعی روش‌ها بیشتر مفروض است.",
            "ناهمسازی اغلب به‌جای تحلیل سرکوب می‌شود.",
            "معیار روشنی برای همگرایی وجود ندارد.",
            "سه‌سوسازی گاه به تزیین روش‌شناختی تبدیل می‌شود.",
            "ترکیب روش‌ها نیازمند تخصص چندگانه است.",
        ],
        critique_text="منتقدان می‌گویند سه‌سوسازی به‌تنهایی اعتبار نمی‌سازد؛ ترکیب دو روش ضعیف یافتهٔ قوی تولید نمی‌کند و استقلال روش‌ها اغلب ادعایی است. با این حال دنزین و جیک نشان دادند ارزش اصلی در آشکار کردن ناهمسازی و واداشتن پژوهشگر به تفسیر چندلایه است، نه در جمع سادهٔ نتایج.",
        applications=[
            "پژوهش ترکیبی در ارتباطات.",
            "ارزیابی برنامه‌های رسانه‌ای.",
            "سنجش اعتماد به اخبار با چند منبع.",
            "مطالعهٔ مخاطب با پیمایش و مصاحبه.",
            "پژوهش سازمانی.",
            "ارزیابی سلامت عمومی.",
            "تحلیل دادهٔ دیجیتال و پیمایش.",
            "مطالعهٔ اثر رسانه در چند بستر.",
            "پژوهش آموزشی.",
            "تحلیل سیاست عمومی.",
            "مطالعهٔ بازار و مصرف.",
            "پژوهش کیفی چندروشی.",
            "پژوهش چندروشی دربارهٔ اثر خشونت رسانه‌ای.",
            "تحلیل دادهٔ پیمایش و محتوای شبکه‌های اجتماعی.",
        ],
        example_text="پژوهشی دربارهٔ اعتماد به اخبار، پیمایش کمّی، مصاحبهٔ عمیق و دادهٔ رفتار کاربر را هم‌زمان به کار می‌برد؛ وقتی پیمایش اعتماد بالا نشان می‌دهد اما رفتار کلیک خلاف آن است، ناهمسازی به پرسش تازه دربارهٔ فاصلهٔ گفتار و کردار می‌رسد.",
        evolution="دنزین در ۱۹۷۸ چهار گونهٔ سه‌سوسازی را صورت‌بندی کرد، جیک در ۱۹۷۹ آن را به ترکیب کمّی و کیفی گستراند و امروز در پژوهش ترکیبی، ارزیابی برنامه و تحلیل چندمنبعی دادهٔ دیجیتال به کار می‌رود.",
        key_concepts=["همگرایی شواهد", "چندروشی", "استقلال منبع", "ناهمسازی", "اعتبار", "پژوهش ترکیبی"],
        theorists="نورمن دنزین و تاد جیک.",
        theorists_text="دنزین گونه‌های سه‌سوسازی را نظری کرد و جیک کاربرد عملی آن را در ترکیب روش‌های کیفی و کمّی نشان داد.",
        model="مثلث شواهد: روش، منبع و پژوهشگر سه ضلع بررسی‌اند و همگرایی یا واگرایی آن‌ها مبنای استنباط است.",
        studies=[
            "صورت‌بندی دنزین در ۱۹۷۸.",
            "پژوهش جیک در ۱۹۷۹.",
            "مطالعهٔ ادغام سازمانی جیک.",
            "پژوهش اعتماد به اخبار با روش ترکیبی.",
            "مطالعهٔ مخاطب تلویزیون.",
            "ارزیابی کمپین سلامت.",
            "تحلیل سیاست آموزشی.",
            "پژوهش رسانه و جوانان.",
            "مطالعهٔ چندمنبعی دادهٔ دیجیتال.",
            "ارزیابی برنامهٔ توسعهٔ محلی.",
            "پژوهش بازار با مصاحبه و پیمایش.",
            "تحلیل مقایسه‌ای روش‌ها.",
        ],
    ),
    "MC-234": dict(
        year=1946,
        mapping=METHOD_MAPPING,
        summary="پژوهش کنش‌مشارکتی رویکردی است که در آن پژوهشگر و کسانی که مسئله به آن‌ها مربوط است، در همهٔ مراحل پژوهش از تعریف مسئله تا تفسیر و اقدام، شریک می‌شوند. لوین در سال ۱۹۴۶ مفهوم پژوهش کنش را برای حل مسائل اقلیت‌ها و روابط گروهی پیشنهاد کرد و چرخهٔ برنامه‌ریزی، اقدام، مشاهده و بازتاب را ساخت. در نسخهٔ مشارکتی، اعضای جامعه دیگر موضوع مطالعه نیستند بلکه هم‌پژوهشگرند. هدف تنها توصیف نیست؛ تولید دانشی است که به تغییر عملی و توانمندسازی بینجامد. قدرت، مالکیت داده و بازگشت نتایج به جامعه در مرکز این رویکرد قرار دارد. چرخه‌های تکراری پژوهش و کنش، یافته‌ها را در عمل می‌آزمایند و دانش محلی را با دانش پژوهشی ترکیب می‌کنند. این رویکرد در آموزش، سلامت، توسعهٔ محلی و سواد رسانه‌ای کاربرد دارد. نقدها بر تعمیم‌پذیری محدود، دشواری مدیریت مشارکت و خطر رتوریک توانمندسازی بدون تغییر واقعی تأکید دارند.",
        definition="پژوهش کنش‌مشارکتی فرایندی چرخه‌ای و مشارکتی است که پژوهشگران و اعضای جامعه را در تولید دانش، بازتاب و اقدام برای تغییر وضعیت مسئله‌دار شریک می‌کند.",
        main_problem="چگونه می‌توان دانشی تولید کرد که هم معتبر باشد و هم اعضای جامعهٔ درگیر را به کنش و تغییر توانا کند، بی‌آنکه صدای آن‌ها در تفسیر پژوهش حذف شود.",
        mechanism="گروهی متشکل از پژوهشگر و اعضای جامعه مسئله را تعریف می‌کنند، اقدام صورت می‌گیرد، داده در حین اقدام گردآوری و مشاهده می‌شود، گروه بازتاب می‌کند و چرخهٔ بعدی برنامه‌ریزی از دل همین بازتاب شکل می‌گیرد؛ مالکیت داده و تفسیر میان اعضا تقسیم می‌شود.",
        assumptions=[
            "اعضای جامعه ظرفیت تولید دانش دارند.",
            "دانش از عمل جدا نیست.",
            "مشارکت واقعی نیازمند بازتوزیع قدرت است.",
            "چرخه‌های تکراری بهترین شکل یادگیری‌اند.",
            "تغییر عملی معیار موفقیت است.",
            "بازتاب جمعی خطا را اصلاح می‌کند.",
            "زمینهٔ محلی بر یافته‌ها اثر دارد.",
            "پژوهشگر خود بخشی از میدان است.",
        ],
        principles=[
            "مسئله را با جامعه تعریف کن.",
            "مالکیت و دسترسی به داده را توافق کن.",
            "اقدام و پژوهش را هم‌زمان ببر.",
            "بازتاب را در هر چرخه بگنجان.",
            "نتایج را به جامعه برگردان.",
            "آسیب و رضایت را پیوسته پایش کن.",
        ],
        critiques=[
            "تعمیم‌پذیری یافته‌ها محدود است.",
            "مدیریت مشارکت و تعارض دشوار است.",
            "خطر رتوریک توانمندسازی وجود دارد.",
            "مرز پژوهش و کنشگری مبهم می‌شود.",
            "زمان و هزینهٔ بالا دارد.",
            "سنجش پیامد دشوار است.",
        ],
        critique_text="منتقدان می‌گویند پژوهش کنش‌مشارکتی گاه به کنشگری با پوشش پژوهش تبدیل می‌شود و توانمندسازی را ادعا می‌کند بدون آنکه ساختار قدرت را تغییر دهد؛ تعمیم نتایج نیز دشوار است. با این حال لوین و پژوهشگران بعدی نشان دادند چرخهٔ بازتاب جمعی می‌تواند دانشی بسازد که هم در عمل آزموده شده و هم به جامعه برگردد.",
        applications=[
            "سواد رسانه‌ای در جامعهٔ محلی.",
            "پژوهش سلامت مشارکتی.",
            "توسعهٔ رسانهٔ محلی.",
            "ارزیابی برنامهٔ آموزشی.",
            "مطالعهٔ عدالت محیطی.",
            "پژوهش با گروه‌های حاشیه‌ای.",
            "طراحی سیاست شهری.",
            "پژوهش سازمانی مشارکتی.",
            "مطالعهٔ مصرف رسانه در مدرسه.",
            "کار با جوانان در پلتفرم‌ها.",
            "بهبود خدمات عمومی.",
            "پژوهش کنش انتقادی.",
            "مطالعهٔ مشارکتی دربارهٔ اعتماد به خبر محلی.",
            "طراحی برنامهٔ سواد رسانه‌ای با معلمان.",
        ],
        example_text="در یک محله، گروهی از ساکنان و دو پژوهشگر برای کاهش اخبار نادرست محلی همکاری می‌کنند؛ هر چرخه با کارگاه سواد رسانه‌ای آغاز می‌شود، دادهٔ گروه‌های محلی ثبت و بازتاب می‌شود و چرخهٔ بعدی محتوا و روش را اصلاح می‌کند.",
        evolution="لوین در ۱۹۴۶ چرخهٔ پژوهش کنش را ساخت؛ از دههٔ ۱۹۷۰ رویکرد انتقادی و مشارکتی آن شکل گرفت و در دههٔ ۲۰۰۰ با راهنمای پژوهش کنش به سلامت، آموزش، توسعه و سواد رسانه‌ای گسترانده شد.",
        key_concepts=["چرخهٔ کنش", "هم‌پژوهشی", "بازتاب جمعی", "توانمندسازی", "مالکیت داده", "تغییر اجتماعی"],
        theorists="کرت لوین، پیتر ریزن و هیلاری بردبری.",
        theorists_text="لوین چرخهٔ پژوهش کنش را بنیان گذاشت و ریزن و بردبری سنت مشارکتی و انتقادی آن را در راهنمای پژوهش کنش تدوین کردند.",
        model="چرخهٔ لوین: برنامه‌ریزی، اقدام، مشاهده و بازتاب که در هر دور با مشارکت جامعه بازسازی می‌شود.",
        studies=[
            "مقالهٔ لوین در ۱۹۴۶.",
            "پژوهش کنش دربارهٔ روابط گروهی.",
            "مطالعهٔ تغییر سازمانی با چرخهٔ کنش.",
            "پژوهش سلامت مشارکتی.",
            "برنامهٔ سواد رسانه‌ای محلی.",
            "مطالعهٔ رسانهٔ جامعه‌محور.",
            "پژوهش کنش انتقادی در آموزش.",
            "ارزیابی توسعهٔ محله.",
            "مطالعهٔ مشارکت جوانان.",
            "پژوهش عدالت محیطی.",
            "تحلیل برنامهٔ خدمات عمومی.",
            "مطالعهٔ پژوهش کنش در مدرسه.",
            "پژوهش مشارکتی با گروه‌های حاشیه‌ای.",
        ],
    ),
}

NAME_FIX = {}
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
                                       "verified": n_verified, "batch": 178}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH178 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
