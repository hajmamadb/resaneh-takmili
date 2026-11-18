# -*- coding: utf-8 -*-
"""Batch 126 (FRAMEWORK): full documentation for MC-653, MC-660, MC-678, MC-694."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch126-framework-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch126_framework.json"

S = {
    "MC-653": [
        dict(kind="BOOK",
             title_en="The Processes of Technological Innovation",
             title_fa="فرایندهای نوآوری فناورانه",
             authors="Tornatzky, L. G.; Fleischer, M.", year=1990,
             publisher="Lexington Books",
             doi=None,
             url="https://archive.org/details/processesoftechn0000torn",
             language="en", isbn=None,
             citation="Tornatzky, L. G., & Fleischer, M. (1990). The Processes of Technological Innovation. Lexington, MA: Lexington Books.",
             locator="technology-organization-environment context", locator_type="SECTION",
             supports="TOE framework: technological, organizational and environmental contexts of adoption", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Electronic Data Interchange and Small Organizations: Adoption and Impact of Technology",
             title_fa="تبادل الکترونیکی داده و سازمان‌های کوچک: پذیرش و اثر فناوری",
             authors="Iacovou, C. L.; Benbasat, I.; Dexter, A. S.", year=1995,
             publisher="MIS Quarterly",
             doi=None, url=None, language="en", isbn=None,
             citation="Iacovou, C. L., Benbasat, I., & Dexter, A. S. (1995). Electronic data interchange and small organizations: Adoption and impact of technology. MIS Quarterly, 19(4), 465-485.",
             locator="19(4):465-485", locator_type="page_range",
             supports="empirical application of TOE contexts to interorganizational technology adoption", verified=False),
    ],
    "MC-660": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Strength of Weak Ties",
             title_fa="قدرت پیوندهای ضعیف",
             authors="Granovetter, M. S.", year=1973,
             publisher="American Journal of Sociology",
             doi="10.1086/225469",
             url="https://snap.stanford.edu/class/cs224w-readings/granovetter73weakties.pdf",
             language="en", isbn=None,
             citation="Granovetter, M. S. (1973). The strength of weak ties. American Journal of Sociology, 78(6), 1360-1380.",
             locator="78(6):1360-1380", locator_type="page_range",
             supports="strong ties tend toward triadic closure; weak ties bridge clusters", verified=True),
        dict(kind="BOOK",
             title_en="Soziologie: Untersuchungen über die Formen der Vergesellschaftung",
             title_fa="جامعه‌شناسی: پژوهش در شکل‌های اجتماعی‌شدن",
             authors="Simmel, G.", year=1908,
             publisher="Duncker & Humblot",
             doi=None, url=None, language="de", isbn=None,
             citation="Simmel, G. (1908). Soziologie: Untersuchungen über die Formen der Vergesellschaftung. Berlin: Duncker & Humblot.",
             locator="excursus on the triad", locator_type="SECTION",
             supports="triad as minimal sociological structure and formal analysis of social forms", verified=False),
    ],
    "MC-678": [
        dict(kind="BOOK",
             title_en="Remembering to Forget: Holocaust Memory through the Camera's Eye",
             title_fa="به‌یادآوردن برای فراموش‌کردن: حافظهٔ هولوکاست از دریچهٔ دوربین",
             authors="Zelizer, B.", year=1998,
             publisher="University of Chicago Press",
             doi=None,
             url="https://press.uchicago.edu/ucp/books/book/chicago/R/bo3637820.html",
             language="en", isbn=None,
             citation="Zelizer, B. (1998). Remembering to Forget: Holocaust Memory through the Camera's Eye. Chicago: University of Chicago Press.",
             locator="book", locator_type="SECTION",
             supports="media images as agents of collective memory and forgetting", verified=True),
        dict(kind="BOOK",
             title_en="On Collective Memory",
             title_fa="دربارهٔ حافظهٔ جمعی",
             authors="Halbwachs, M.", year=1992,
             publisher="University of Chicago Press",
             doi=None, url=None, language="en", isbn=None,
             citation="Halbwachs, M. (1992). On Collective Memory (L. A. Coser, Ed. & Trans.). Chicago: University of Chicago Press.",
             locator="book", locator_type="SECTION",
             supports="social frameworks of memory", verified=False),
    ],
    "MC-694": [
        dict(kind="REPORT",
             title_en="Many Voices, One World: Towards a New, More Just and More Efficient World Information and Communication Order",
             title_fa="بسی صداها، یک جهان: به‌سوی نظم اطلاعاتی و ارتباطی جهانی عادلانه‌تر و کارآمدتر",
             authors="International Commission for the Study of Communication Problems (MacBride, S., chair)", year=1980,
             publisher="UNESCO",
             doi=None,
             url="https://unesdoc.unesco.org/ark:/48223/pf0000372754",
             language="en", isbn=None,
             citation="International Commission for the Study of Communication Problems. (1980). Many Voices, One World. Paris: UNESCO.",
             locator="report", locator_type="SECTION",
             supports="NWICO critique of global information inequality and right to communicate", verified=True),
        dict(kind="BOOK",
             title_en="The Global Media: The New Missionaries of Corporate Capitalism",
             title_fa="رسانهٔ جهانی: میسیونرهای نوین سرمایه‌داری شرکتی",
             authors="Herman, E. S.; McChesney, R. W.", year=1997,
             publisher="Cassell",
             doi=None, url=None, language="en", isbn=None,
             citation="Herman, E. S., & McChesney, R. W. (1997). The Global Media: The New Missionaries of Corporate Capitalism. London: Cassell.",
             locator="book", locator_type="SECTION",
             supports="later political-economy account of global media concentration", verified=False),
    ],
}

ENRICH = {
    "MC-653": dict(
        year=1990,
        summary="چارچوب فناوری، سازمان و محیط، مدلی برای توضیح پذیرش نوآوری فناورانه در بنگاه‌هاست که لوئیس تورناتزکی و میچل فلیشر در کتاب سال ۱۹۹۰ با عنوان فرایندهای نوآوری فناورانه معرفی کردند. ادعای مرکزی این است که پذیرش یک فناوری در سازمان تنها به ویژگی‌های خود فناوری وابسته نیست، بلکه از سه زمینهٔ هم‌زمان اثر می‌گیرد: زمینهٔ فناوری، یعنی فناوری‌های موجود و ویژگی‌های فناوری تازه مانند نسبی بودن مزیت و پیچیدگی؛ زمینهٔ سازمانی، یعنی اندازه، ساختار، منابع و سبک ارتباط درون‌سازمانی؛ و زمینهٔ محیطی، یعنی صنعت، رقبا، فشار شرکای تجاری و مقررات. چارچوب در پژوهش‌های نظام‌های اطلاعاتی بسیار به کار رفته و بعدها برای تحلیل پذیرش تجارت الکترونیک و فناوری‌های دیجیتال گسترش یافت. در رسانه، این چارچوب برای فهم پذیرش سامانه‌های مدیریت محتوا، ابزارهای تحلیلی و فناوری‌های خودکار در تحریریه‌ها مناسب است: پذیرش فناوری تازه در یک سازمان خبری هم به مزیت ادراک‌شده و پیچیدگی ابزار وابسته است، هم به آمادگی سازمانی و هم به فشار رقابتی و مقررات. نقدهای اصلی به آن، ایستایی مدل، سطح تحلیل بنگاه و کم‌توجهی به کنشگران فردی و میدان نهادی مربوط می‌شود.",
        definition="چارچوب فناوری، سازمان و محیط، مدلی است که پذیرش نوآوری فناورانه در بنگاه را با سه زمینهٔ فناوری، سازمانی و محیطی توضیح می‌دهد.",
        main_problem="چرا بنگاه‌ها فناوری تازه را با سرعت‌های متفاوت می‌پذیرند، در حالی که ویژگی خود فناوری تنها بخشی از توضیح است.",
        mechanism="ویژگی‌های فناوری مانند مزیت نسبی، سازگاری و پیچیدگی، آمادگی سازمانی مانند اندازه، منابع و ساختار، و فشار محیطی مانند رقابت، شرکای تجاری و مقررات، در کنار هم تصمیم پذیرش را می‌سازند؛ ضعف در هر زمینه می‌تواند پذیرش را متوقف کند، حتی اگر فناوری از نظر فنی برتر باشد.",
        assumptions=[
            "پذیرش نوآوری تصمیمی در سطح بنگاه است.",
            "سه زمینهٔ فناوری، سازمان و محیط را می‌توان به‌طور تحلیلی از هم جدا کرد.",
            "ویژگی‌های ادراک‌شدهٔ فناوری بر تصمیم پذیرش اثر می‌گذارند.",
            "منابع و ساختار سازمان، ظرفیت پذیرش را تعیین می‌کنند.",
            "فشار محیطی، از جمله رقابت و مقررات، پذیرش را تسریع یا کند می‌کند.",
        ],
        principles=[
            "پذیرش را باید در سه زمینهٔ هم‌زمان بررسی کرد.",
            "مزیت نسبی و پیچیدگی ادراک‌شدهٔ فناوری، متغیرهای کلیدی زمینهٔ فناوری‌اند.",
            "اندازه و منابع سازمان، ظرفیت جذب را می‌سازند.",
            "فشار رقبا و شرکای تجاری می‌تواند پذیرش را از درون سازمان جلو بیندازد.",
            "مقررات و سیاست‌های دولتی بخشی از زمینهٔ محیطی‌اند.",
            "تحلیل پذیرش باید به مرحلهٔ تصمیم و نه فقط نتیجهٔ نهایی توجه کند.",
        ],
        critiques=[
            "مدل ایستاست و پویایی یادگیری سازمانی را کم‌رنگ می‌بیند.",
            "سطح تحلیل بنگاه، کنشگران فردی و نقش مدیران را نادیده می‌گیرد.",
            "میدان نهادی و فشارهای فرهنگی و مشروعیتی جای کافی ندارند.",
            "سنجه‌های سه زمینه در پژوهش‌ها ناهمگون‌اند.",
            "مرز میان زمینهٔ سازمانی و محیطی در عمل مبهم می‌شود.",
        ],
        critique_text="منتقدان می‌گویند چارچوب فناوری، سازمان و محیط فهرستی مفید از عوامل است اما نظریه‌ای دربارهٔ سازوکار و ترتیب اثر آنها ارائه نمی‌دهد؛ پژوهش‌های بعدی با افزودن سازه‌های فردی و نهادی کوشیدند این شکاف را پر کنند. با این حال، چارچوب همچنان یکی از پرکاربردترین مدل‌های پذیرش فناوری در سطح سازمان است.",
        applications=[
            "تحلیل پذیرش سامانه‌های مدیریت محتوا در تحریریه‌ها.",
            "مطالعهٔ پذیرش ابزارهای تحلیلی و خودکارسازی در رسانه.",
            "ارزیابی پذیرش تجارت الکترونیک و خدمات دیجیتال در بنگاه‌ها.",
            "سیاست‌گذاری حمایت از نوسازی فناورانه در سازمان‌های رسانه‌ای.",
            "پژوهش تطبیقی دربارهٔ پذیرش فناوری در صنایع مختلف.",
        ],
        example_text="یک سازمان خبری ممکن است فناوری تحلیل مخاطب را از نظر فنی مناسب بداند، اما اگر منابع انسانی کافی برای آموزش نداشته باشد یا فشار رقابتی ضعیف باشد، پذیرش را به تعویق بیندازد؛ در مقابل، فشار رقبا و مقررات شفافیت می‌تواند پذیرش همان فناوری را در سازمانی مشابه تسریع کند. سه زمینه در کنار هم تصمیم را توضیح می‌دهند.",
        evolution="ریشهٔ چارچوب در پژوهش‌های دههٔ ۱۹۸۰ دربارهٔ نوآوری سازمانی است و صورت‌بندی آن در کتاب سال ۱۹۹۰ انجام شد. در دههٔ ۱۹۹۰ پژوهش‌های نظام‌های اطلاعاتی آن را برای پذیرش فناوری‌های میان‌سازمانی به کار بردند و در دههٔ ۲۰۰۰ مرورهای نظام‌مند، آن را در کنار مدل‌های فردی پذیرش قرار دادند. در سال‌های اخیر، چارچوب برای تحلیل پذیرش هوش مصنوعی و ابزارهای خودکار در سازمان‌ها بازخوانی شده است.",
        key_concepts=["زمینهٔ فناوری", "زمینهٔ سازمانی", "زمینهٔ محیطی", "مزیت نسبی", "پیچیدگی", "ظرفیت جذب", "فشار محیطی"],
        theorists="لوئیس تورناتزکی و میچل فلیشر، سازندگان چارچوب؛ و پژوهشگران نظام‌های اطلاعاتی که آن را برای پذیرش فناوری‌های سازمانی بسط دادند.",
        theorists_text="این چارچوب در سنت پژوهش نوآوری سازمانی و نظام‌های اطلاعاتی شکل گرفت و با مدل‌های فردی پذیرش فناوری پیوند یافت.",
        model="مدل سه‌زمینه‌ای: زمینهٔ فناوری، زمینهٔ سازمانی و زمینهٔ محیطی بر تصمیم پذیرش اثر می‌گذارند؛ شدت و ترکیب این اثرها به اندازه و منابع بنگاه و به فشار رقابتی و مقررات وابسته است.",
        studies=[
            "کتاب سال ۱۹۹۰ سه زمینه را به‌عنوان توضیح پذیرش نوآوری معرفی کرد.",
            "پژوهش‌های دههٔ ۱۹۹۰ چارچوب را برای فناوری‌های میان‌سازمانی آزمودند.",
            "مرورهای نظام‌مند دههٔ ۲۰۰۰ جایگاه چارچوب را در ادبیات پذیرش تثبیت کردند.",
            "پژوهش‌های اخیر آن را برای ابزارهای خودکار و هوشمند به کار برده‌اند.",
        ],
    ),
    "MC-660": dict(
        year=1908,
        summary="بستار سهگانه، مفهومی در تحلیل شبکه‌های اجتماعی است که می‌گوید اگر دو گره با یک گرهٔ سوم پیوند داشته باشند، به‌احتمال زیاد میان آن دو نیز پیوندی شکل می‌گیرد. این گرایش به تراگذری، یعنی جایی که دوستی دو دوست به دوستی مشترک می‌انجامد، یکی از بنیادی‌ترین سازوکارهای ساخت‌یابی شبکه است. ریشهٔ نظری آن به جامعه‌شناسی گئورگ زیمل در اوایل سدهٔ بیستم بازمی‌گردد که ساختار سه‌نفره را واحد کمینهٔ جامعه‌شناسی می‌دانست، و صورت‌بندی تجربی آن با پژوهش مارک گرانووتر در سال ۱۹۷۳ دربارهٔ قدرت پیوندهای ضعیف گره خورده است. گرانووتر نشان داد پیوندهای قوی گرایش دارند مثلث بسته بسازند و پیوندهای ضعیف، پل میان خوشه‌ها می‌شوند؛ هنجار «مثلث ممنوع» در شبکه‌های اجتماعی نیز از همین منطق می‌آید. در رسانه، بستار سهگانه برای فهم شکل‌گیری خوشه‌های مخاطب، انتشار خبر در شبکه‌های پیوندی، شکل‌گیری حباب‌های اطلاعاتی و ساختار به‌هم‌پیوستهٔ منابع خبری به کار می‌رود. سنجهٔ رایج آن، ضریب خوشه‌بندی است که نسبت مثلث‌های بسته به مثلث‌های ممکن را می‌سنجد. نقدهای اصلی به ایستا بودن سنجه‌ها، نادیده‌گرفتن محتوای پیوند، هم‌ریشگی با هم‌سنخی و دشواری استنباط علّی از داده‌های مقطعی مربوط می‌شود.",
        definition="بستار سهگانه، گرایش شبکه‌های اجتماعی به شکل‌گیری پیوند میان دو گره است که هر دو با یک گرهٔ سوم پیوند دارند.",
        main_problem="چرا شبکه‌های اجتماعی خوشه‌ای می‌شوند و چه سازوکاری سبب می‌شود پیوندهای تازه بیشتر درون خوشه‌ها شکل بگیرند تا میان آنها.",
        mechanism="پیوندهای قوی زمان، اعتماد و تجربهٔ مشترک می‌سازند و دو گره را به گره‌های مشترک وصل می‌کنند؛ هنجار مثلث ممنوع، نبود پیوند میان دو دوست مشترک را پرهزینه می‌کند؛ در نتیجه مثلث‌ها بسته می‌شوند. پیوندهای ضعیف اما پل میان خوشه‌ها می‌شوند و اطلاعات و فرصت تازه را جابه‌جا می‌کنند.",
        assumptions=[
            "پیوندهای اجتماعی را می‌توان به‌عنوان یال در شبکه بازنمایی کرد.",
            "شدت پیوند و میزان تراگذری را می‌توان سنجید.",
            "گرایش به توازن و هم‌خوانی در روابط انسانی وجود دارد.",
            "پیوند مشترک، فرصت و اعتماد لازم برای پیوند تازه را می‌سازد.",
            "شبکه را می‌توان در یک مقطع زمانی به‌طور معنادار تحلیل کرد.",
        ],
        principles=[
            "ساختار پیوندها و نه محتوای ارتباط، واحد تحلیل است.",
            "پیوندهای قوی گرایش به بستن مثلث دارند.",
            "پیوندهای ضعیف پل میان خوشه‌ها و مجرای اطلاعات تازه‌اند.",
            "ضریب خوشه‌بندی، سنجهٔ استاندارد بستار است.",
            "موقعیت گره در شبکه، فرصت و محدودیت کنش را می‌سازد.",
            "تحلیل شبکه باید هم خوشه و هم پل را ببیند.",
        ],
        critiques=[
            "سنجه‌های بستار ایستا و مقطعی‌اند و پویایی شبکه را نشان نمی‌دهند.",
            "محتوای پیوند، اعتماد و کیفیت رابطه در سنجه نادیده می‌ماند.",
            "هم‌سنخی می‌تواند الگوی بستار را بدون سازوکار علّی توضیح دهد.",
            "در شبکه‌های بزرگ دیجیتال، خوشه‌بندی کمتر از شبکه‌های کوچک است.",
            "استنباط علّی از همبستگی ساختاری دشوار است.",
        ],
        critique_text="منتقدان می‌گویند بستار سهگانه الگوی ساختاری مهمی را نشان می‌دهد اما به‌تنهایی توضیح نمی‌دهد که چرا پیوندها شکل می‌گیرند؛ هم‌سنخی، محدودیت جغرافیایی و الگوریتم‌های پیشنهاد دوست می‌توانند الگوی بستار را بدون آنکه افراد آگاهانه مثلث بسازند، بازتولید کنند. با این حال، این مفهوم همچنان ستون تحلیل ساختاری شبکه است.",
        applications=[
            "تحلیل خوشه‌های مخاطب در شبکه‌های اجتماعی.",
            "مطالعهٔ انتشار خبر و شایعه در شبکه‌های پیوندی.",
            "بررسی حباب‌های اطلاعاتی و قطبی‌شدن شبکه‌های گفت‌وگو.",
            "تحلیل شبکهٔ منابع خبری و پیوند میان رسانه‌ها.",
            "الگوریتم‌های تشخیص اجتماع و پیشنهاد پیوند.",
        ],
        example_text="در یک شبکهٔ پیام‌رسان، اگر دو همکار هر دو با یک همکار سوم در ارتباط باشند، احتمال شکل‌گیری گروه مشترک میان آن دو بالا می‌رود؛ همین منطق توضیح می‌دهد چرا خبرها بیشتر درون گروه‌های بسته می‌گردند و برای رسیدن به خوشه‌های دیگر به پل‌های ضعیف نیاز دارند.",
        evolution="زیمل در آغاز سدهٔ بیستم ساختار سه‌نفره را واحد کمینهٔ جامعه‌شناسی دانست و تحلیل صورت‌گرای روابط را بنیان گذاشت. گرانووتر در سال ۱۹۷۳ پیوند میان بستار و پیوندهای ضعیف را صورت‌بندی کرد و از دههٔ ۱۹۷۰ به بعد ریاضیات شبکه و سنجه‌های خوشه‌بندی توسعه یافت. در دههٔ ۲۰۰۰ با داده‌های بزرگ شبکه‌های آنلاین، بستار سهگانه به یکی از سنجه‌های استاندارد تحلیل شبکه تبدیل شد.",
        key_concepts=["بستار سهگانه", "تراگذری", "ضریب خوشه‌بندی", "مثلث ممنوع", "پیوند ضعیف", "پل ساختاری", "خوشه"],
        theorists="گئورگ زیمل، بنیان‌گذار تحلیل صورت‌گرای سه‌گانه؛ و مارک گرانووتر، صورت‌بند پیوند بستار با قدرت پیوندهای ضعیف.",
        theorists_text="این مفهوم در سنت جامعه‌شناسی صورت‌گرا و بعدها در تحلیل شبکهٔ اجتماعی و شبکه‌های پیچیده بسط یافت.",
        model="مدل ساختاری: پیوندهای قوی به بستن مثلث و تشکیل خوشه می‌انجامند؛ پیوندهای ضعیف پل میان خوشه‌ها می‌شوند و جریان اطلاعات تازه را ممکن می‌کنند؛ موقعیت گره در این ساختار، فرصت و محدودیت کنش را تعیین می‌کند.",
        studies=[
            "جامعه‌شناسی زیمل، تحلیل سه‌گانه را به‌عنوان شکل پایهٔ اجتماعی‌شدن معرفی کرد.",
            "مقالهٔ سال ۱۹۷۳ بستار را با پیوندهای ضعیف و پل‌های ساختاری پیوند داد.",
            "پژوهش‌های ریاضی شبکه، ضریب خوشه‌بندی را استاندارد سنجش بستار کردند.",
            "مطالعات شبکه‌های آنلاین، الگوهای بستار و شکاف خوشه‌ها را در مقیاس بزرگ بررسی کردند.",
        ],
    ),
    "MC-678": dict(
        year=1998,
        summary="چارچوب یادآوری و فراموشی جمعی، مجموعه‌ای از پژوهش‌هاست که رسانه‌ها را نه ابزار انتقال اطلاعات، بلکه عاملان ساختن حافظهٔ جمعی می‌داند. باربی زلایزر در کتاب سال ۱۹۹۸ با عنوان به‌یادآوردن برای فراموش‌کردن: حافظهٔ هولوکاست از دریچهٔ دوربین، نشان داد عکس‌های آزادسازی اردوگاه‌ها چگونه حافظهٔ عمومی را شکل دادند و به الگویی برای فهم فجایع بعدی تبدیل شدند. ایدهٔ کلیدی این است که رسانه هم‌زمان به‌یاد می‌آورد و فراموش می‌کند: انتخاب یک تصویر یا روایت، تصاویر و روایت‌های دیگر را به حاشیه می‌راند و حافظهٔ جمعی در قالبی تثبیت می‌شود که بعدها جای تجربهٔ مستقیم را می‌گیرد. مکانیسم‌ها شامل چارچوب‌بندی خبری، سالگردها، آرشیو، تکرار تصویر و روایت‌های آیینی است. در رسانه‌های دیجیتال، الگوریتم‌های نمایش و آرشیو و حذف محتوا، نسخهٔ تازه‌ای از همین سازوکارند. اهمیت این چارچوب در تحلیل بحران‌ها، جنگ، فاجعه و هویت ملی است. نقدهای اصلی به رسانه‌محوری، سوگیری انتخاب نمونه، ابهام مفهومی حافظهٔ جمعی و کم‌توجهی به مقاومت گروه‌های حاشیه‌ای مربوط می‌شود.",
        definition="چارچوب یادآوری و فراموشی جمعی، مجموعه‌ای از رویکردهاست که رسانه‌ها را عامل ساختن، تثبیت و حذف حافظهٔ جمعی می‌داند.",
        main_problem="جامعه‌ها چگونه از راه رسانه به‌یاد می‌آورند و فراموش می‌کنند، و چه کسی تعیین می‌کند کدام روایت از گذشته به حافظهٔ عمومی راه یابد.",
        mechanism="انتخاب تصویر و روایت، چارچوب‌بندی خبری، تکرار آیینی در سالگردها و آرشیو، روایت‌های رقیب را به حاشیه می‌راند و قالبی برای فهم رویدادهای بعدی می‌سازد؛ حذف، سکوت و کهنه‌شدن نیز فراموشی را نهادینه می‌کند. حافظهٔ جمعی نه در ذهن فرد، بلکه در ابزارها و رویه‌های رسانه‌ای نگهداری می‌شود.",
        assumptions=[
            "حافظه فراتر از ذهن فرد و در قالب‌های اجتماعی شکل می‌گیرد.",
            "رسانه‌ها در انتخاب و انتقال گذشته نقش فعال دارند.",
            "تصویر و روایت، قالب‌های اصلی حافظهٔ رسانه‌ای‌اند.",
            "فراموشی، پیامد نبود توجه است و نه فقط از دست رفتن اطلاعات.",
            "سالگردها و آرشیو، حافظه را در زمان تثبیت می‌کنند.",
        ],
        principles=[
            "رسانه را باید عامل حافظه دانست و نه مجرای خنثای گذشته.",
            "انتخاب تصویر، خود عملی حافظه‌ساز و فراموشی‌ساز است.",
            "تکرار و آیین، روایت‌های حافظه را تثبیت می‌کند.",
            "آرشیو، سیاست انتخاب و حذف دارد.",
            "حافظهٔ جمعی همیشه رقابتی و چندروایتی است.",
            "تحلیل رسانه باید هم حضور و هم غیاب روایت‌ها را ببیند.",
        ],
        critiques=[
            "چارچوب بیش از اندازه رسانه‌محور است.",
            "سوگیری انتخاب نمونه در مطالعات موردی جدی است.",
            "مفهوم حافظهٔ جمعی مبهم و گاه استعاری می‌ماند.",
            "مقاومت گروه‌های حاشیه‌ای و حافظهٔ رقیب کم‌بررسی می‌شود.",
            "پیوند میان حافظهٔ رسانه‌ای و کنش سیاسی روشن نیست.",
        ],
        critique_text="منتقدان می‌گویند رسانه‌ها تنها یکی از عاملان حافظه‌اند و خانواده، مدرسه، آیین و آرشیوهای غیررسمی نیز سهم دارند؛ تمرکز بر رسانه می‌تواند تصویری بیش از اندازه قدرتمند از آن بسازد. با این حال، چارچوب زلایزر نشان داد که حافظهٔ عمومی محصول انتخاب رسانه‌ای است و همین بصیرت، پژوهش رسانه و تاریخ را به هم پیوند داده است.",
        applications=[
            "تحلیل پوشش بحران، جنگ و فاجعه در رسانه.",
            "مطالعهٔ سیاست سالگرد و آیین‌های یادبود.",
            "پژوهش آرشیو دیجیتال و سیاست حذف محتوا.",
            "تحلیل هویت ملی و روایت‌های تاریخی در رسانه.",
            "آموزش روزنامه‌نگاری حافظه و پوشش مسئولانهٔ فجایع.",
        ],
        example_text="عکس‌های آزادسازی اردوگاه‌های نازی در سال ۱۹۴۵ نه فقط رویدادی را ثبت کردند، بلکه به الگویی برای پوشش فجایع بعدی تبدیل شدند؛ خبرنگاران بعدها با استناد به همان تصاویر، فجایع تازه را فهم‌پذیر کردند. همین تکرار، روایت‌های دیگر را به حاشیه برد و نشان داد که یادآوری و فراموشی دو روی یک سازوکارند.",
        evolution="ریشهٔ مفهومی به هالبواکس و بحث چارچوب‌های اجتماعی حافظه در دههٔ ۱۹۲۰ بازمی‌گردد. زلایزر در سال ۱۹۹۸ حافظهٔ رسانه‌ای را با مطالعهٔ تصویر صورت‌بندی کرد. از دههٔ ۲۰۰۰ پژوهش حافظهٔ دیجیتال، آرشیو آنلاین و سیاست حذف محتوا را به این سنت افزود.",
        key_concepts=["حافظهٔ جمعی", "فراموشی جمعی", "چارچوب حافظه", "آرشیو", "روایت آیینی", "تصویر شاهد"],
        theorists="باربی زلایزر، صورت‌بند حافظهٔ رسانه‌ای؛ و موریس هالبواکس، پیشگام بحث چارچوب‌های اجتماعی حافظه.",
        theorists_text="این چارچوب در سنت جامعه‌شناسی حافظه و مطالعات رسانه شکل گرفت و با تاریخ بصری و پژوهش فاجعه پیوند خورد.",
        model="مدل چرخهٔ حافظه: رویداد، چارچوب‌بندی رسانه‌ای، انتخاب تصویر و روایت، تکرار آیینی در سالگردها و آرشیو، تثبیت قالب فهم، و به حاشیه راندن روایت‌های رقیب؛ چرخه‌ای که هم‌زمان حافظه و فراموشی تولید می‌کند.",
        studies=[
            "کتاب سال ۱۹۹۸ نقش عکس‌های آزادسازی اردوگاه‌ها در حافظهٔ عمومی را تحلیل کرد.",
            "پژوهش‌های حافظهٔ جمعی، چارچوب‌های اجتماعی یادآوری را بسط دادند.",
            "مطالعات خبر، نقش سالگرد و روایت آیینی در تثبیت حافظه را نشان دادند.",
            "پژوهش حافظهٔ دیجیتال، آرشیو و حذف محتوا را در محیط پلتفرم بررسی کرد.",
        ],
    ),
    "MC-694": dict(
        year=1980,
        summary="گزارش مک‌براید، سند سال ۱۹۸۰ سازمان آموزشی، علمی و فرهنگی ملل متحد است که با عنوان «بسی صداها، یک جهان: به‌سوی نظم اطلاعاتی و ارتباطی جهانی عادلانه‌تر و کارآمدتر» منتشر شد. این گزارش حاصل کار کمیسیون بین‌المللی مطالعهٔ مسائل ارتباطات بود که شون مک‌براید، سیاستمدار و حقوق‌دان ایرلندی، ریاست آن را بر عهده داشت. گزارش، نابرابری جریان اطلاعات میان شمال و جنوب را نقد کرد و خواستار نظم نوین اطلاعات و ارتباطات جهانی شد: تعادل جریان خبر، دسترسی برابر به فناوری، حق ارتباط، مشارکت جوامع محلی در تولید محتوا و کاهش تمرکز مالکیت رسانه. این سند به‌سرعت به نماد جدال سیاسی تبدیل شد؛ کشورهای در حال توسعه آن را برنامهٔ عدالت ارتباطی خواندند و دولت‌های غربی و شرکت‌های رسانه‌ای آن را تهدید آزادی مطبوعات دانستند. پیامد سیاسی آن، خروج دو کشور بزرگ از سازمان آموزشی و فرهنگی ملل متحد در میانهٔ دههٔ ۱۹۸۰ بود. با این حال، ایده‌های گزارش در بحث‌های بعدی دربارهٔ شکاف دیجیتال، تنوع رسانه‌ای، حق ارتباط و قدرت پلتفرم‌ها بازتاب یافت. اهمیت آن برای پژوهش رسانه، پیوند دادن ارتباطات با عدالت اجتماعی و سیاست جهانی است. نقدهای اصلی به آرمان‌گرایی، ابهام سازوکارهای اجرا و خطر تبدیل حق ارتباط به ابزار کنترل دولتی مربوط می‌شود.",
        definition="گزارش مک‌براید، سند سال ۱۹۸۰ کمیسیون بین‌المللی مطالعهٔ مسائل ارتباطات است که نابرابری جریان جهانی اطلاعات را نقد و نظم نوین اطلاعات و ارتباطات را پیشنهاد کرد.",
        main_problem="چگونه می‌توان جریان اطلاعات جهانی را متعادل کرد و حق ارتباط و مشارکت را برای جوامع کم‌بهره تضمین کرد، بی‌آنکه آزادی رسانه‌ها از میان برود.",
        mechanism="کمیسیون با گردهم آوردن کارشناسان چند کشور، وضعیت جریان خبر، مالکیت رسانه و دسترسی به فناوری را بررسی کرد و مجموعه‌ای از توصیه‌ها را برای تعادل، دسترسی، مشارکت و تنوع ارائه داد؛ توصیه‌ها از راه نهادهای بین‌المللی و سیاست‌های ملی دنبال می‌شد و بحث‌های جهانی دربارهٔ عدالت ارتباطی را برانگیخت.",
        assumptions=[
            "جریان جهانی اطلاعات نامتوازن است و این نابرابری پیامدهای سیاسی و فرهنگی دارد.",
            "ارتباطات حق بشری است و نه فقط کالا.",
            "مشارکت جوامع محلی در تولید محتوا، تنوع را افزایش می‌دهد.",
            "نهادهای بین‌المللی می‌توانند در متعادل‌سازی جریان اطلاعات نقش داشته باشند.",
            "کاهش تمرکز مالکیت رسانه، شرط تنوع محتواست.",
        ],
        principles=[
            "تعادل جریان خبر میان شمال و جنوب باید برقرار شود.",
            "حق ارتباط باید به رسمیت شناخته شود.",
            "دسترسی برابر به فناوری، بخشی از عدالت ارتباطی است.",
            "مشارکت جوامع محلی در تولید محتوا باید تقویت شود.",
            "تنوع مالکیت و محتوا باید حفظ شود.",
            "همکاری بین‌المللی برای کاهش شکاف ارتباطی ضروری است.",
        ],
        critiques=[
            "گزارش آرمان‌گرایانه است و سازوکار اجرای توصیه‌ها را روشن نمی‌کند.",
            "خطر تبدیل حق ارتباط به ابزار کنترل دولتی بر رسانه وجود دارد.",
            "تقابل شمال و جنوب، تنوع درون هر دو بلوک را نادیده می‌گیرد.",
            "مناقشهٔ سیاسی، خوانش علمی گزارش را تحت‌الشعاع قرار داد.",
            "کاربرد آن برای محیط پلتفرم‌های خصوصی جهانی نیازمند بازخوانی است.",
        ],
        critique_text="منتقدان می‌گویند گزارش مک‌براید در تشخیص نابرابری درست بود اما در تجویز، به سازوکارهای اجرایی و تضمین آزادی رسانه کمتر پرداخت؛ همین ابهام، زمینهٔ سوءبرداشت سیاسی را فراهم کرد. با این حال، سند همچنان یکی از مهم‌ترین تلاش‌ها برای پیوند ارتباطات با عدالت جهانی است.",
        applications=[
            "تحلیل سیاست رسانه و عدالت ارتباطی در سطح جهانی.",
            "پژوهش شکاف دیجیتال و دسترسی به فناوری.",
            "مطالعهٔ تنوع مالکیت و تمرکز رسانه.",
            "آموزش سیاست‌گذاری ارتباطات و حقوق ارتباطی.",
            "تحلیل و بازخوانی آن برای قدرت پلتفرم‌های جهانی.",
        ],
        example_text="در مناقشهٔ دههٔ ۱۹۷۰ و ۱۹۸۰ دربارهٔ جریان خبر، کشورهای در حال توسعه به سلطهٔ خبرگزاری‌های بزرگ بر روایت رویدادهای جهانی اعتراض کردند و گزارش مک‌براید این اعتراض را به زبان سیاست بین‌المللی ترجمه کرد؛ امروز همان پرسش در قالب سلطهٔ الگوریتم‌ها و پلتفرم‌های جهانی بر جریان اطلاعات بازتولید شده است.",
        evolution="این گزارش حاصل سال‌ها بحث در یونسکو دربارهٔ نظم نوین اطلاعات و ارتباطات بود و در سال ۱۹۸۰ منتشر شد. در میانهٔ دههٔ ۱۹۸۰ با خروج دو کشور بزرگ از یونسکو، دورهٔ افول سیاسی آن آغاز شد، اما در دههٔ ۲۰۰۰ در بحث شکاف دیجیتال و در دههٔ ۲۰۱۰ در نقد قدرت پلتفرم‌ها بازخوانی شد.",
        key_concepts=["نظم نوین اطلاعات و ارتباطات", "حق ارتباط", "تعادل جریان خبر", "تمرکز مالکیت رسانه", "عدالت ارتباطی", "شکاف دیجیتال"],
        theorists="شون مک‌براید، رئیس کمیسیون و نام‌دهندهٔ گزارش؛ و کمیسیون بین‌المللی مطالعهٔ مسائل ارتباطات که سند را تدوین کرد.",
        theorists_text="این سند در سنت نقد اقتصاد سیاسی رسانه و بحث عدالت جهانی ارتباطات شکل گرفت و بعدها با پژوهش شکاف دیجیتال پیوند خورد.",
        model="مدل چهارمحوری: تعادل جریان، دسترسی، مشارکت و تنوع؛ هر محور با توصیه‌های سیاستی به نهادهای بین‌المللی و دولت‌ها گره می‌خورد و هدف نهایی، نظم اطلاعاتی عادلانه‌تر است.",
        studies=[
            "گزارش سال ۱۹۸۰ نابرابری جریان اطلاعات و توصیه‌های نظم نوین را منتشر کرد.",
            "پژوهش‌های بعدی، پیامدهای سیاسی گزارش و خروج کشورها از یونسکو را تحلیل کردند.",
            "مطالعات اقتصاد سیاسی رسانه، تمرکز مالکیت جهانی را بررسی کردند.",
            "پژوهش شکاف دیجیتال، ایده‌های گزارش را در محیط اینترنت بازخوانی کرد.",
        ],
    ),
}

NAME_FIX = {
    "MC-653": ("چارچوب فناوری، سازمان و محیط", "TOE Framework (Technology-Organization-Environment)",
               "name normalized: Latin acronym removed from Persian title"),
    "MC-660": ("بستار سهگانه (بستار مثلثی در شبکه)", "Triadic Closure",
               "English title 'Triple Substrate' was a mistranslation; entity documented as triadic closure (Simmel 1908; Granovetter 1973)"),
}

YEAR_FIX = {
    "MC-653": "no year change; note: editorial card core_logic was a mismatched network-society template, documentation rebuilt from Tornatzky & Fleischer (1990)",
    "MC-660": "year filled: none -> 1908 (Simmel, Soziologie, triadic structures); note: English title 'Triple Substrate' was a mistranslation, documentation rebuilt as triadic closure with Granovetter (1973)",
    "MC-678": "year filled: none -> 1998 (Zelizer, Remembering to Forget); note: editorial card core_logic was a mismatched active-audience template, documentation rebuilt from Zelizer (1998) and Halbwachs (1992)",
    "MC-694": "no year change; note: editorial card core_logic was a mismatched interpersonal-communication template, documentation rebuilt from the UNESCO MacBride report (1980)",
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
                                       "verified": n_verified, "batch": 126}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH126 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
