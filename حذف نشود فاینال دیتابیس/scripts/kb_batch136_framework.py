# -*- coding: utf-8 -*-
"""Batch 136 (MODEL): full documentation for MC-235, MC-244, MC-245, MC-264."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch136-model-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch136_model.json"

S = {
    "MC-235": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Latent Dirichlet Allocation",
             title_fa="تخصیص نهفتهٔ دیریکله",
             authors="Blei, D. M.; Ng, A. Y.; Jordan, M. I.", year=2003,
             publisher="Journal of Machine Learning Research",
             doi=None,
             url="https://www.jmlr.org/papers/volume3/blei03a/blei03a.pdf",
             language="en", isbn=None,
             citation="Blei, D. M., Ng, A. Y., & Jordan, M. I. (2003). Latent Dirichlet allocation. Journal of Machine Learning Research, 3, 993-1022.",
             locator="3:993-1022", locator_type="page_range",
             supports="generative topic model with document-topic and topic-word distributions", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Probabilistic Topic Models",
             title_fa="مدل‌های موضوعی احتمالاتی",
             authors="Blei, D. M.", year=2012,
             publisher="Communications of the ACM",
             doi=None, url=None, language="en", isbn=None,
             citation="Blei, D. M. (2012). Probabilistic topic models. Communications of the ACM, 55(4), 77-84.",
             locator="55(4):77-84", locator_type="page_range",
             supports="accessible overview of topic modeling for text analysis", verified=False),
    ],
    "MC-244": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Computer-Mediated Communication: Impersonal, Interpersonal, and Hyperpersonal Interaction",
             title_fa="ارتباط با واسطهٔ رایانه: تعامل غیرشخصی، میان‌شخصی و ابرشخصی",
             authors="Walther, J. B.", year=1996,
             publisher="Communication Research",
             doi="10.1177/009365096023001001",
             url="https://journals.sagepub.com/doi/10.1177/009365096023001001",
             language="en", isbn=None,
             citation="Walther, J. B. (1996). Computer-mediated communication: Impersonal, interpersonal, and hyperpersonal interaction. Communication Research, 23(1), 3-43.",
             locator="23(1):3-43", locator_type="page_range",
             supports="four-component hyperpersonal model of online interaction", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Selective Self-Presentation in Computer-Mediated Communication: Hyperpersonal Dimensions of Technology, Language, and Cognition",
             title_fa="خودارائه‌گری گزینشی در ارتباط با واسطهٔ رایانه",
             authors="Walther, J. B.", year=2007,
             publisher="Computers in Human Behavior",
             doi=None, url=None, language="en", isbn=None,
             citation="Walther, J. B. (2007). Selective self-presentation in computer-mediated communication: Hyperpersonal dimensions of technology, language, and cognition. Computers in Human Behavior, 23(5), 2538-2557.",
             locator="23(5):2538-2557", locator_type="page_range",
             supports="extension of the hyperpersonal model to self-presentation", verified=False),
    ],
    "MC-245": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Computer-Mediated Communication, De-Individuation and Group Decision-Making",
             title_fa="ارتباط با واسطهٔ رایانه، فردیت‌زدایی و تصمیم‌گیری گروهی",
             authors="Lea, M.; Spears, R.", year=1991,
             publisher="International Journal of Man-Machine Studies",
             doi=None,
             url="https://www.sciencedirect.com/science/article/pii/0020737391900459",
             language="en", isbn=None,
             citation="Lea, M., & Spears, R. (1991). Computer-mediated communication, de-individuation and group decision-making. International Journal of Man-Machine Studies, 34(2), 283-301.",
             locator="34(2):283-301", locator_type="page_range",
             supports="social identity reinterpretation of deindividuation in CMC", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="A Social Identity Model of Deindividuation Phenomena",
             title_fa="مدل هویت اجتماعی پدیده‌های فردیت‌زدایی",
             authors="Reicher, S. D.; Spears, R.; Postmes, T.", year=1995,
             publisher="European Review of Social Psychology",
             doi=None, url=None, language="en", isbn=None,
             citation="Reicher, S. D., Spears, R., & Postmes, T. (1995). A social identity model of deindividuation phenomena. European Review of Social Psychology, 6(1), 161-198.",
             locator="6(1):161-198", locator_type="page_range",
             supports="cognitive and strategic dimensions of the SIDE model", verified=False),
    ],
    "MC-264": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Whence Consumer Loyalty?",
             title_fa="وفاداری مصرف‌کننده از کجا می‌آید؟",
             authors="Oliver, R. L.", year=1999,
             publisher="Journal of Marketing",
             doi="10.1177/00222429990634s105",
             url="https://journals.sagepub.com/doi/10.1177/00222429990634s105",
             language="en", isbn=None,
             citation="Oliver, R. L. (1999). Whence consumer loyalty? Journal of Marketing, 63(Special Issue), 33-44.",
             locator="63:33-44", locator_type="page_range",
             supports="cognitive, affective, conative and action loyalty phases", verified=True),
        dict(kind="BOOK",
             title_en="The Loyalty Effect: The Hidden Force Behind Growth, Profits, and Lasting Value",
             title_fa="اثر وفاداری: نیروی پنهان پشت رشد، سود و ارزش پایدار",
             authors="Reichheld, F. F.", year=1996,
             publisher="Harvard Business School Press",
             doi=None, url=None, language="en", isbn=None,
             citation="Reichheld, F. F. (1996). The Loyalty Effect: The Hidden Force Behind Growth, Profits, and Lasting Value. Boston: Harvard Business School Press.",
             locator="book", locator_type="SECTION",
             supports="economic argument linking retention to profitability", verified=False),
    ],
}

ENRICH = {
    "MC-235": dict(
        year=2003,
        summary="مدل‌سازی موضوعی، خانواده‌ای از مدل‌های آماری برای تحلیل متن است که پایهٔ اصلی آن، مدل تخصیص نهفتهٔ دیریکله، در سال ۲۰۰۳ توسط دیوید بلی، اندرو نگ و مایکل جوردن در مجلهٔ پژوهش یادگیری ماشین معرفی شد. ادعای مرکزی این است که هر سند ترکیبی از چند موضوع پنهان است و هر موضوع توزیعی از واژه‌ها دارد؛ با تحلیل هم‌رخدادی واژگان در مجموعهٔ بزرگ اسناد، می‌توان این موضوع‌های پنهان را بدون برچسب‌گذاری دستی استخراج کرد. برخلاف روش‌های سادهٔ شمارش واژه، مدل موضوعی امکان می‌دهد یک سند هم‌زمان به چند موضوع نسبت داده شود و وزن هر موضوع تعیین گردد. استنتاج مدل با روش‌های تقریبی مانند نمونه‌گیری گیبس یا استنتاج تغییراتی انجام می‌شود. این روش، تحلیل کمی بزرگ‌مقیاس متن را در پژوهش ارتباطات، تحلیل چارچوب‌بندی خبر، دستور کار رسانه و تحلیل شبکه‌های اجتماعی ممکن کرد. نقدهای اصلی به آن، فرض کیسهٔ واژه‌ها و بی‌توجهی به ترتیب و بافت جمله، وابستگی نتیجه به شمار موضوع‌ها و آستانه‌های تنظیم، دشواری تفسیر موضوع‌ها و نیاز به اعتبارسنجی انسانی مربوط می‌شود.",
        definition="مدل‌سازی موضوعی، روشی آماری است که با فرض ترکیب‌شدن هر سند از چند موضوع پنهان و هر موضوع از توزیعی از واژه‌ها، موضوع‌های اصلی یک مجموعهٔ متنی را به‌طور خودکار استخراج می‌کند.",
        main_problem="چگونه می‌توان از میان هزاران سند متنی، موضوع‌های اصلی و الگوهای پنهان را بدون خواندن و برچسب‌گذاری دستی همهٔ آنها شناسایی کرد.",
        mechanism="مدل فرض می‌کند هر سند از توزیعی روی موضوع‌ها و هر موضوع از توزیعی روی واژه‌ها ساخته می‌شود؛ الگوریتم با تحلیل هم‌رخدادی واژه‌ها، توزیع‌هایی را می‌یابد که احتمال مشاهدهٔ متن را بیشینه می‌کنند. نتیجه، فهرستی از موضوع‌ها با واژه‌های شاخص و وزن هر موضوع در هر سند است.",
        assumptions=[
            "هر سند ترکیبی از چند موضوع پنهان است.",
            "هر موضوع، توزیعی از واژه‌ها دارد.",
            "ترتیب واژه‌ها در سند قابل صرف‌نظر است.",
            "الگوهای هم‌رخدادی، موضوع‌ها را آشکار می‌کنند.",
            "شمار موضوع‌ها را پژوهشگر تعیین می‌کند.",
        ],
        principles=[
            "متن را باید به‌صورت مجموعه‌ای از توزیع‌های آماری مدل کرد.",
            "هر سند می‌تواند هم‌زمان در چند موضوع سهم داشته باشد.",
            "واژه‌های شاخص، موضوع را بازنمایی می‌کنند.",
            "نتیجهٔ مدل نیازمند تفسیر و اعتبارسنجی انسانی است.",
            "شمار موضوع‌ها باید با معیارهای نظری و تجربی انتخاب شود.",
            "تحلیل بزرگ‌مقیاس مکمل و نه جانشین خوانش کیفی است.",
        ],
        critiques=[
            "فرض کیسهٔ واژه‌ها، ترتیب و بافت را نادیده می‌گیرد.",
            "نتیجه به شمار موضوع‌ها و تنظیم‌ها حساس است.",
            "تفسیر موضوع‌ها ذهنی و دشوار است.",
            "اعتبارسنجی مدل، معیار استاندارد یکدستی ندارد.",
            "برای متن‌های کوتاه و گفتاری ضعیف عمل می‌کند.",
        ],
        critique_text="منتقدان می‌گویند مدل‌سازی موضوعی ابزار قدرتمندی برای تحلیل بزرگ‌مقیاس متن فراهم کرد اما فرض کیسهٔ واژه‌ها و حساسیت به تنظیم‌ها، اعتبار نتایج را محدود می‌کند و تفسیر موضوع‌ها همیشه قابل تکرار نیست. با این حال، به یکی از پرکاربردترین روش‌های تحلیل محتوای محاسباتی تبدیل شده است.",
        applications=[
            "تحلیل چارچوب‌بندی خبر در حجم بزرگ.",
            "شناسایی موضوع‌های گفت‌وگوی شبکه‌های اجتماعی.",
            "تحلیل دستور کار رسانه و تغییر موضوع در زمان.",
            "کاوش مجموعه‌های اسناد تاریخی و آرشیوی.",
            "پیش‌پردازش و اکتشاف دادهٔ متنی در پژوهش ارتباطات.",
        ],
        example_text="پژوهشگری که ده هزار گزارش خبری دربارهٔ بحران آب جمع‌آوری کرده است، با مدل موضوعی می‌تواند موضوع‌هایی مانند «کمبود منابع»، «مدیریت سیاسی» و «اعتراض محلی» را استخراج کند و سهم هر موضوع را در هر سال بسنجد؛ سپس با خوانش نمونه‌ای، تفسیر خود را اعتبارسنجی می‌کند. مدل‌سازی موضوعی همین تحلیل اکتشافی را ممکن می‌کند.",
        evolution="مدل در سنت یادگیری ماشین آماری و پردازش زبان طبیعی شکل گرفت. مقالهٔ سال ۲۰۰۳ مدل تخصیص نهفتهٔ دیریکله را تثبیت کرد و در دههٔ ۲۰۱۰ با رشد دادهٔ متنی، به روش استاندارد تحلیل محتوای محاسباتی تبدیل شد.",
        key_concepts=["موضوع پنهان", "توزیع سند-موضوع", "توزیع موضوع-واژه", "کیسهٔ واژه‌ها", "استنتاج تغییراتی", "نمونه‌گیری گیبس"],
        theorists="دیوید بلی، اندرو نگ و مایکل جوردن، صورت‌بندانان مدل تخصیص نهفتهٔ دیریکله.",
        theorists_text="این روش در سنت یادگیری ماشین احتمالاتی و تحلیل محتوای محاسباتی شکل گرفت.",
        model="مدل مولد: هر سند توزیعی روی موضوع‌ها و هر موضوع توزیعی روی واژه‌ها دارد؛ استنتاج، توزیع‌های پنهان را از دادهٔ مشاهده‌شده بازیابی می‌کند.",
        studies=[
            "مقالهٔ سال ۲۰۰۳ مدل تخصیص نهفتهٔ دیریکله را معرفی کرد.",
            "پژوهش‌های ارتباطات، موضوع‌های خبری را با مدل استخراج کردند.",
            "مطالعات شبکهٔ اجتماعی، گفت‌وگو را در حجم بزرگ تحلیل کردند.",
            "مرورهای روش‌شناختی، اعتبار و محدودیت مدل را ارزیابی کردند.",
        ],
    ),
    "MC-244": dict(
        year=1996,
        summary="مدل ابرشخصی، مدلی در پژوهش ارتباط با واسطهٔ رایانه است که جوزف والتر در سال ۱۹۹۶ در مجلهٔ پژوهش ارتباطات معرفی کرد. ادعای مرکزی این است که ارتباط با واسطه گاهی می‌تواند از ارتباط رودررو صمیمی‌تر و مطلوب‌تر باشد. چهار مؤلفه این فرایند را می‌سازند: فرستنده خود را به‌صورت گزینشی و بهینه عرضه می‌کند و جنبه‌های مطلوب هویت را برجسته می‌سازد؛ گیرنده با نشانه‌های اجتماعی کم، تصویری آرمانی از فرستنده می‌سازد و ویژگی‌های مثبت را بیش از واقع به او نسبت می‌دهد؛ کانال ناهمزمان امکان ویرایش، تأمل و بازنویسی پیام را می‌دهد؛ و بازخورد متقابل، این تصویرهای آرمانی را از راه تأیید رفتاری تقویت می‌کند و چرخه‌ای صمیمیت‌افزا می‌سازد. این مدل، چارچوب پژوهش دوستی آنلاین، قرار اینترنتی، خودارائه‌گری در شبکه‌های اجتماعی و کار دور را فراهم کرد. نقدهای اصلی به آن، تمرکز بر ارتباط متنی ناهمزمان، کم‌توجهی به انتقال صمیمیت به محیط رودررو و امکان فریب و آرمانی‌سازی نادرست مربوط می‌شود.",
        definition="مدل ابرشخصی، مدلی است که توضیح می‌دهد عرضهٔ گزینشی خود، آرمانی‌سازی گیرنده، ویرایش‌پذیری کانال ناهمزمان و بازخورد تقویتی چگونه ارتباط با واسطه را از تعامل رودررو صمیمی‌تر می‌سازند.",
        main_problem="چرا ارتباط متنی و ناهمزمان گاهی صمیمیت بیشتری از گفت‌وگوی رودررو ایجاد می‌کند، و چه سازوکارهایی این اثر را می‌سازند.",
        mechanism="فرستنده با ویرایش پیام، نسخهٔ بهینهٔ خود را ارائه می‌کند؛ گیرنده با اطلاعات کم، تصویر آرمانی می‌سازد؛ بازخورد مطلوب، این تصویر را تأیید و تقویت می‌کند. این چرخهٔ تأیید متقابل، صمیمیت و جذب را بیش از تعامل رودررو بالا می‌برد.",
        assumptions=[
            "فرستنده می‌تواند خود را گزینشی و بهینه عرضه کند.",
            "کمبود نشانه‌های اجتماعی، آرمانی‌سازی را افزایش می‌دهد.",
            "کانال ناهمزمان امکان ویرایش و تأمل می‌دهد.",
            "بازخورد متقابل، تصویر آرمانی را تقویت می‌کند.",
            "ارتباط با واسطه می‌تواند از رودررو صمیمی‌تر شود.",
        ],
        principles=[
            "چهار مؤلفهٔ فرستنده، گیرنده، کانال و بازخورد باید جدا تحلیل شوند.",
            "عرضهٔ گزینشی خود، پایهٔ ابرشخصی‌شدن است.",
            "آرمانی‌سازی گیرنده، نقش محوری دارد.",
            "ناهمزمانی کانال، امکان تأمل و ویرایش می‌دهد.",
            "بازخورد تقویتی، چرخهٔ صمیمیت را می‌سازد.",
            "اثر ابرشخصی، پیامد اخلاقی فریب نیز دارد.",
            "چرخهٔ ابرشخصی را باید در بستر رابطهٔ بلندمدت و نه تک‌تعامل دید.",
        ],
        critiques=[
            "بیشتر بر ارتباط متنی و ناهمزمان تمرکز دارد.",
            "انتقال صمیمیت به محیط رودررو کم‌بررسی می‌ماند.",
            "خطر فریب و آرمانی‌سازی نادرست را کم‌رنگ می‌کند.",
            "برای ویدئو و ارتباط همزمان بازنگری می‌خواهد.",
            "شواهد تجربی در بافت‌های فرهنگی مختلف ناهمگون است.",
            "تفاوت جنسیت و شخصیت در آرمانی‌سازی کم‌بررسی مانده است.",
        ],
        critique_text="منتقدان می‌گویند مدل ابرشخصی توضیحی بدیع برای صمیمیت آنلاین فراهم کرد اما بیشتر بر ارتباط متنی استوار است و پیامدهای منفی آرمانی‌سازی مانند فریب و ناکامی در انتقال به زندگی واقعی را کم‌بررسی می‌گذارد. با این حال، چارچوب مرجع پژوهش ارتباط آنلاین است.",
        applications=[
            "پژوهش قرار اینترنتی و دوستی آنلاین.",
            "تحلیل خودارائه‌گری در شبکه‌های اجتماعی.",
            "مطالعهٔ ارتباط تیمی در کار دور.",
            "طراحی پلتفرم‌های آشنایی و گفت‌وگوی متنی.",
            "آموزش سواد ارتباط دیجیتال و شناخت آرمانی‌سازی.",
            "طراحی سامانه‌های پیام‌رسانی برای کاهش سوءبرداشت در تعامل متنی.",
        ],
        example_text="دو همکار که تنها با پیام متنی در ارتباط‌اند ممکن است تصویری آرمانی از یکدیگر بسازند، پیام‌هایشان را با دقت ویرایش کنند و با بازخورد مثبت، صمیمیتی بیش از همکاران حضوری تجربه کنند؛ اما در نخستین دیدار رودررو ممکن است شکاف تصویر و واقعیت آشکار شود. مدل ابرشخصی این چرخه را توضیح می‌دهد.",
        evolution="مدل در سنت پژوهش ارتباط با واسطهٔ رایانه دههٔ ۱۹۹۰ شکل گرفت و مقالهٔ سال ۱۹۹۶ آن را تثبیت کرد. پژوهش‌های بعدی، آن را به شبکهٔ اجتماعی، ویدئوکنفرانس و قرار اینترنتی گستردند و بعد اخلاقی آن را برجسته کردند.",
        key_concepts=["ابرشخصی", "عرضهٔ گزینشی خود", "آرمانی‌سازی گیرنده", "ناهمزمانی", "بازخورد تقویتی", "تأیید رفتاری"],
        theorists="جوزف والتر، صورت‌بند مدل ابرشخصی.",
        theorists_text="این مدل در سنت پژوهش ارتباط با واسطهٔ رایانه و روان‌شناسی اجتماعی شکل گرفت.",
        model="مدل چهارمؤلفه‌ای: عرضهٔ گزینشی فرستنده، آرمانی‌سازی گیرنده، ویرایش‌پذیری کانال و بازخورد تقویتی؛ چرخهٔ تأیید متقابل، صمیمیت ابرشخصی می‌سازد.",
        studies=[
            "مقالهٔ سال ۱۹۹۶ مدل چهارمؤلفه‌ای را معرفی کرد.",
            "پژوهش قرار اینترنتی، آرمانی‌سازی و رضایت را سنجید.",
            "مطالعات خودارائه‌گری، عرضهٔ گزینشی را در شبکه‌های اجتماعی بررسی کردند.",
            "پژوهش کار دور، صمیمیت تیمی آنلاین را تحلیل کرد.",
        ],
    ),
    "MC-245": dict(
        year=1991,
        summary="مدل هویت اجتماعی پدیده‌های فردیت‌زدایی، مدلی در روان‌شناسی اجتماعی ارتباط با واسطه است که مارتین لیا و راسل اسپیرز در سال ۱۹۹۱ در پژوهش ارتباط با واسطهٔ رایانه معرفی کردند و بعدتر توسط استیون رایکر، اسپیرز و تام پوستمس بسط یافت. ادعای مرکزی این است که برخلاف نظریهٔ کلاسیک فردیت‌زدایی، گمنامی به از دست رفتن خود نمی‌انجامد، بلکه برجستگی را از هویت فردی به هویت اجتماعی منتقل می‌کند. وقتی هویت گروهی برجسته باشد، کاربران گمنام بیشتر از هنجارهای گروه پیروی می‌کنند؛ این را بعد شناختی مدل می‌نامند. شناسایی‌پذیری در برابر گروه بیرونی نیز بر میزان ابراز آزادانهٔ هنجارهای گروه اثر می‌گذارد؛ این بعد راهبردی است، زیرا گروه می‌تواند بسته به حضور ناظر بیرونی، هنجارهای خود را آشکارتر یا پنهان‌تر بیان کند. این مدل، چارچوب پژوهش رفتار آنلاین گروهی، قطب‌بندی و افراط‌گرایی، آزار آنلاین و اثر گمنامی بر مشارکت سیاسی را فراهم کرد. نقدهای اصلی به آن، دشواری سنجش برجستگی هویت، تفاوت پلتفرم‌ها در نوع گمنامی و کم‌توجهی به قدرت ساختاری مربوط می‌شود.",
        definition="مدل هویت اجتماعی فردیت‌زدایی، مدلی است که گمنامی را عامل جابه‌جایی برجستگی از هویت فردی به هویت اجتماعی می‌داند و اثر آن را در دو بعد شناختی و راهبردی توضیح می‌دهد.",
        main_problem="چرا افراد گمنام در محیط آنلاین گاهی بیش از حالت شناسایی‌شده از هنجارهای گروه پیروی می‌کنند یا برعکس، بی‌قیدتر عمل می‌کنند.",
        mechanism="گمنامی، نشانه‌های فردی را کم می‌کند و هویت گروهی را برجسته می‌سازد؛ فرد بر پایهٔ هنجارهای گروه عمل می‌کند. حضور یا غیبت ناظر بیرونی، تعیین می‌کند گروه هنجار خود را آشکارا ابراز کند یا پنهان نگه دارد.",
        assumptions=[
            "گمنامی، هویت فردی را از برجستگی می‌اندازد.",
            "هویت اجتماعی می‌تواند جایگزین هویت فردی شود.",
            "هنجارهای گروه، رفتار گمنام را هدایت می‌کنند.",
            "حضور ناظر بیرونی، ابراز هنجار را تغییر می‌دهد.",
            "فردیت‌زدایی به معنای از دست رفتن خود نیست.",
        ],
        principles=[
            "گمنامی را نباید معادل بی‌هویتی دانست.",
            "بعد شناختی، برجستگی هویت گروهی را توضیح می‌دهد.",
            "بعد راهبردی، اثر ناظر بیرونی بر ابراز هنجار را توضیح می‌دهد.",
            "هنجار گروه، جهت رفتار آنلاین را تعیین می‌کند.",
            "طراحی پلتفرم باید اثر گمنامی بر هنجار گروهی را در نظر بگیرد.",
            "قطب‌بندی آنلاین را باید با هنجار گروهی تحلیل کرد.",
            "هویت گروهی برجسته، هنجارهای درون‌گروهی را تقویت می‌کند.",
        ],
        critiques=[
            "سنجش برجستگی هویت در محیط آنلاین دشوار است.",
            "نوع گمنامی میان پلتفرم‌ها بسیار متفاوت است.",
            "نقش قدرت و نابرابری ساختاری کم‌بررسی می‌ماند.",
            "شواهد تجربی دربارهٔ آزادسازی هنجار ناهمگون است.",
            "مدل بیشتر بر گروه‌های کوچک متمرکز است.",
        ],
        critique_text="منتقدان می‌گویند مدل هویت اجتماعی فردیت‌زدایی تصویر کلاسیک از گمنامی را به‌درستی اصلاح کرد اما سنجش تجربی برجستگی هویت و تعمیم آن به پلتفرم‌های متنوع دیجیتال دشوار است. با این حال، چارچوب مرجع تحلیل رفتار گروهی آنلاین و آزار و قطب‌بندی است.",
        applications=[
            "تحلیل آزار آنلاین و گفت‌وگوی گمنام.",
            "پژوهش قطب‌بندی و افراط‌گرایی گروهی.",
            "طراحی سیاست هویت و گمنامی در پلتفرم.",
            "مطالعهٔ مشارکت سیاسی آنلاین.",
            "آموزش مدیریت اجتماع آنلاین و هنجار گروهی.",
        ],
        example_text="در یک انجمن گمنام، کاربری که هویت فردی‌اش پنهان است، خود را بیشتر عضو گروه «طرفداران تیم» می‌بیند و هنجارهای آن گروه را شدیدتر اجرا می‌کند؛ اگر رسانه‌های بیرونی انجمن را زیر نظر بگیرند، همان گروه ممکن است هنجار خود را محتاطانه‌تر بیان کند. مدل هویت اجتماعی فردیت‌زدایی این دو بعد را توضیح می‌دهد.",
        evolution="ریشهٔ مدل در نقد نظریهٔ کلاسیک فردیت‌زدایی در دههٔ ۱۹۸۰ است. مقالهٔ سال ۱۹۹۱ آن را به ارتباط با واسطه پیوند داد و نسخهٔ سال ۱۹۹۵ دو بعد شناختی و راهبردی را صورت‌بندی کرد. پژوهش‌های بعدی، مدل را به رسانهٔ اجتماعی و قطب‌بندی گستردند.",
        key_concepts=["فردیت‌زدایی", "هویت اجتماعی", "برجستگی هویت", "بعد شناختی", "بعد راهبردی", "هنجار گروهی"],
        theorists="مارتین لیا، راسل اسپیرز، استیون رایکر و تام پوستمس، بسط‌دهندگان مدل هویت اجتماعی فردیت‌زدایی.",
        theorists_text="این مدل در سنت روان‌شناسی اجتماعی هویت گروهی و پژوهش ارتباط با واسطه شکل گرفت.",
        model="مدل دوبُعدی: بعد شناختی (برجستگی هویت گروهی در گمنامی) و بعد راهبردی (اثر ناظر بیرونی بر ابراز هنجار)؛ هنجار گروه، رفتار کاربر گمنام را هدایت می‌کند.",
        studies=[
            "مقالهٔ سال ۱۹۹۱ مدل را به ارتباط با واسطه پیوند داد.",
            "نسخهٔ سال ۱۹۹۵ دو بعد شناختی و راهبردی را صورت‌بندی کرد.",
            "پژوهش‌های آزار آنلاین، اثر گمنامی را آزمودند.",
            "مطالعات قطب‌بندی، هنجار گروهی آنلاین را تحلیل کردند.",
        ],
    ),
    "MC-264": dict(
        year=1999,
        summary="چرخهٔ وفاداری و ریزش، چارچوبی در بازاریابی رابطه‌مند است که ریشهٔ نظری آن به مقالهٔ ریچارد الیور در سال ۱۹۹۹ دربارهٔ سرچشمهٔ وفاداری مصرف‌کننده و اقتصاد وفاداری فردریک رایکهلد در سال ۱۹۹۶ بازمی‌گردد. ادعای مرکزی این است که وفاداری یک حالت واحد نیست، بلکه چهار مرحله دارد: وفاداری شناختی، یعنی باور به برتری برند بر پایهٔ اطلاعات؛ وفاداری عاطفی، یعنی دلبستگی و لذت از برند؛ وفاداری کنشی، یعنی قصد رفتاری قوی برای خرید دوباره؛ و وفاداری عملی، یعنی عادت رفتاری و غلبه بر موانع خرید مجدد. هر مرحله در برابر ریزش آسیب‌پذیری متفاوتی دارد و وفاداری عملی پایدارترین است. ریزش زمانی رخ می‌دهد که ارزش ادراک‌شدهٔ ادامه از هزینهٔ ماندن کمتر شود، و نشانه‌های کوچک مانند کاهش دفعات استفاده معمولاً پیش‌درآمد ریزش کامل‌اند. در رسانه‌های اشتراکی، این چارچوب برای تحلیل چرخهٔ عمر مشترک، پیش‌بینی ریزش و طراحی راهبرد نگهداشت به کار می‌رود. نقدهای اصلی به آن، دشواری سنجش عاطفه، تفاوت رفتار وفاداری در بازارهای کم‌رقیب و اثر برنامه‌های وفاداری بر افزایش سود مربوط می‌شود.",
        definition="چرخهٔ وفاداری، مدلی است که وفاداری را در چهار مرحلهٔ شناختی، عاطفی، کنشی و عملی توصیف می‌کند و ریزش را حاصل کاهش ارزش ادراک‌شدهٔ ادامه در برابر هزینهٔ ماندن می‌داند.",
        main_problem="مشتری چگونه از شناخت برند به عادت رفتاری می‌رسد، و چه نشانه‌هایی پیش از ریزش کامل او را می‌توان شناسایی کرد.",
        mechanism="مشتری ابتدا بر پایهٔ اطلاعات برند را برتر می‌بیند؛ سپس دلبستگی عاطفی می‌سازد؛ قصد خرید دوباره پیدا می‌کند و در نهایت به عادت می‌رسد. کاهش ارزش ادراک‌شده یا افزایش هزینهٔ ماندن، وفاداری را در هر مرحله تضعیف می‌کند و نشانه‌های رفتاری کوچک، ریزش قریب‌الوقوع را هشدار می‌دهند.",
        assumptions=[
            "وفاداری چهار مرحلهٔ متمایز دارد.",
            "هر مرحله آسیب‌پذیری متفاوتی در برابر ریزش دارد.",
            "وفاداری عاطفی و عملی پایدارتر از شناختی است.",
            "ریزش از محاسبهٔ ارزش در برابر هزینه برمی‌خیزد.",
            "نشانه‌های رفتاری کوچک، ریزش را پیش‌بینی می‌کنند.",
        ],
        principles=[
            "وفاداری را باید مرحله‌ای و نه دوقطبی سنجید.",
            "دلبستگی عاطفی، گذر از وفاداری شناختی را ممکن می‌کند.",
            "عادت رفتاری، پایدارترین شکل وفاداری است.",
            "کاهش استفاده، هشدار زودهنگام ریزش است.",
            "نگهداشت باید پیش از مرحلهٔ ریزش آغاز شود.",
            "ارزش ادراک‌شده را باید در برابر هزینهٔ ماندن سنجید.",
        ],
        critiques=[
            "سنجش عاطفه و مرحلهٔ کنشی دشوار است.",
            "رفتار وفاداری در بازارهای کم‌رقیب متفاوت است.",
            "اثر برنامه‌های وفاداری بر سود یکدست نیست.",
            "مدل بیشتر بر مصرف‌کنندهٔ فردی متمرکز است.",
            "نقش عوامل ساختاری و رقابتی کم‌بررسی می‌ماند.",
            "دادهٔ رفتاری، نشانه‌های ریزش را پیش از لغو آشکار می‌کند.",
        ],
        critique_text="منتقدان می‌گویند چارچوب چرخهٔ وفاداری تصویری دقیق‌تر از وفاداری دوقطبی ارائه کرد اما سنجش مراحل عاطفی و کنشی دشوار است و اثربخشی برنامه‌های وفاداری بر سود همواره تأیید نشده است. با این حال، چارچوب مرجع تحلیل نگهداشت و ریزش مشترک در رسانه است.",
        applications=[
            "تحلیل چرخهٔ عمر مشترک رسانهٔ اشتراکی.",
            "پیش‌بینی ریزش و طراحی کمپین نگهداشت.",
            "طراحی برنامهٔ وفاداری و باشگاه مشتریان.",
            "پژوهش رفتار مصرف‌کننده و ارزش عمر مشتری.",
            "تحلیل ریزش کاربر در اپلیکیشن و پلتفرم.",
            "طراحی شاخص‌های هشدار زودهنگام ریزش در داشبورد مشتری.",
        ],
        example_text="یک سرویس اشتراک خبری متوجه می‌شود گروهی از مشترکان که پیش‌تر روزانه اپلیکیشن را باز می‌کردند، اکنون هفته‌ای یک بار باز می‌کنند؛ این کاهش دفعات استفاده، هشدار ریزش است و تیم نگهداشت با پیشنهاد محتوای شخصی‌سازی‌شده پیش از لغو اشتراک مداخله می‌کند. چرخهٔ وفاداری و ریزش همین منطق را توضیح می‌دهد.",
        evolution="ریشهٔ چارچوب در پژوهش وفاداری برند و اقتصاد نگهداشت دههٔ ۱۹۹۰ است. مقالهٔ سال ۱۹۹۹ چهار مرحلهٔ وفاداری را صورت‌بندی کرد و پژوهش‌های بعدی، آن را به رسانهٔ اشتراکی و تحلیل دادهٔ ریزش گستردند.",
        key_concepts=["وفاداری شناختی", "وفاداری عاطفی", "وفاداری کنشی", "وفاداری عملی", "ریزش", "ارزش عمر مشتری"],
        theorists="ریچارد الیور و فردریک رایکهلد، صورت‌بندانان چرخهٔ وفاداری و اقتصاد نگهداشت.",
        theorists_text="این چارچوب در سنت بازاریابی رابطه‌مند و اقتصاد مشتری شکل گرفت و با مدیریت رسانهٔ اشتراکی پیوند خورد.",
        model="مدل چهارمرحله‌ای: شناختی، عاطفی، کنشی و عملی؛ ریزش از کاهش ارزش ادراک‌شده در برابر هزینهٔ ماندن برمی‌خیزد و افت استفاده، نشانهٔ هشدار است.",
        studies=[
            "مقالهٔ سال ۱۹۹۹ مراحل وفاداری را صورت‌بندی کرد.",
            "پژوهش وفاداری، اثر دلبستگی عاطفی را آزمود.",
            "مطالعات اشتراک رسانه، ریزش مشترک را تحلیل کردند.",
            "پژوهش‌های نگهداشت، نشانه‌های زودهنگام ریزش را بررسی کردند.",
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
                                       "verified": n_verified, "batch": 136}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH136 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
