# -*- coding: utf-8 -*-
"""Batch 157 (MODEL): MC-654 TTF, MC-674 fake news diffusion, MC-679 myth, MC-697 negotiation/marginalization."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch157-model-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch157_model.json"

S = {
    "MC-654": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Task-Technology Fit and Individual Performance",
             title_fa="تناسب وظیفه–فناوری و عملکرد فردی",
             authors="Goodhue, D. L.; Thompson, R. L.", year=1995,
             publisher="MIS Quarterly",
             doi="10.2307/249689",
             url="https://misq.umn.edu/misq/article/19/2/213/1157/Task-Technology-Fit-and-Individual-Performance",
             language="en", isbn=None,
             citation="Goodhue, D. L., & Thompson, R. L. (1995). Task-technology fit and individual performance. MIS Quarterly, 19(2), 213-236.",
             locator="19(2):213-236", locator_type="page_range",
             supports="fit between task and technology as the driver of performance impact", verified=True),
        dict(kind="REPORT",
             title_en="Task-Technology Fit - TheoryHub",
             title_fa="تناسب وظیفه–فناوری - بانک نظریه‌های نیوکاسل",
             authors="Marikyan, D.; Papagiannidis, S.", year=2022,
             publisher="Newcastle University TheoryHub",
             doi=None,
             url="https://open.ncl.ac.uk/theory-library/task-technology-fit.pdf",
             language="en", isbn=None,
             citation="Marikyan, D., & Papagiannidis, S. (2022). Task-Technology Fit. Newcastle University TheoryHub.",
             locator="theory library entry", locator_type="entry",
             supports="review of TTF constructs, extensions and empirical record", verified=True),
    ],
    "MC-674": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Spread of True and False News Online",
             title_fa="اشاعهٔ خبر درست و نادرست در فضای آنلاین",
             authors="Vosoughi, S.; Roy, D.; Aral, S.", year=2018,
             publisher="Science",
             doi="10.1126/science.aap9559",
             url="https://www.science.org/doi/10.1126/science.aap9559",
             language="en", isbn=None,
             citation="Vosoughi, S., Roy, D., & Aral, S. (2018). The spread of true and false news online. Science, 359(6380), 1146-1151.",
             locator="359(6380):1146-1151", locator_type="page_range",
             supports="false news spreading farther, faster and deeper than true news", verified=True),
        dict(kind="REPORT",
             title_en="The Spread of True and False News Online - IDE Research Brief",
             title_fa="خلاصهٔ پژوهشی اشاعهٔ خبر درست و نادرست",
             authors="MIT Initiative on the Digital Economy", year=2018,
             publisher="MIT IDE",
             doi=None,
             url="https://ide.mit.edu/wp-content/uploads/2018/12/2017-IDE-Research-Brief-False-News.pdf",
             language="en", isbn=None,
             citation="MIT Initiative on the Digital Economy (2018). The Spread of True and False News Online. Research Brief.",
             locator="2018 brief", locator_type="report",
             supports="role of humans rather than bots in false-news diffusion", verified=True),
    ],
    "MC-679": [
        dict(kind="BOOK",
             title_en="Mythologies",
             title_fa="اسطوره‌ها",
             authors="Barthes, R.", year=1957,
             publisher="Éditions du Seuil (English: Hill and Wang, 1972)",
             doi=None,
             url="https://monoskop.org/File:Barthes_Roland_Mythologies_EN_1972.pdf",
             language="en", isbn=None,
             citation="Barthes, R. (1957/1972). Mythologies (A. Lavers, Trans.). New York: Hill and Wang.",
             locator="English 1972 edition", locator_type="edition",
             supports="myth as second-order signification that naturalizes ideology", verified=True),
        dict(kind="BOOK",
             title_en="The Message of Television: Myth and Narrative in Contemporary Culture",
             title_fa="پیام تلویزیون: اسطوره و روایت در فرهنگ معاصر",
             authors="Silverstone, R.", year=1981,
             publisher="Heinemann Educational",
             doi=None,
             url="https://www.nypl.org/research/research-catalog/bib/b10786710",
             language="en", isbn="0435828258",
             citation="Silverstone, R. (1981). The Message of Television: Myth and Narrative in Contemporary Culture. London: Heinemann Educational.",
             locator="1981 edition", locator_type="edition",
             supports="myth and narrative structures in television output", verified=True),
    ],
    "MC-697": [
        dict(kind="BOOK",
             title_en="Policing the Crisis: Mugging, the State, and Law and Order",
             title_fa="پلیس‌کردن بحران: سرقت خیابانی، دولت و نظم قانونی",
             authors="Hall, S.; Critcher, C.; Jefferson, T.; Clarke, J.; Roberts, B.", year=1978,
             publisher="Macmillan",
             doi=None,
             url="https://archive.org/details/policingcrisismu0000hall",
             language="en", isbn=None,
             citation="Hall, S., Critcher, C., Jefferson, T., Clarke, J., & Roberts, B. (1978). Policing the Crisis: Mugging, the State, and Law and Order. London: Macmillan.",
             locator="1978 edition", locator_type="edition",
             supports="media amplification, primary definition and moral panic around mugging", verified=True),
        dict(kind="BOOK",
             title_en="Policing the Crisis: Mugging, the State and Law and Order (35th Anniversary Edition)",
             title_fa="پلیس‌کردن بحران: ویراست سی‌وپنجمین سال",
             authors="Hall, S.; Critcher, C.; Jefferson, T.; Clarke, J.; Roberts, B.", year=2013,
             publisher="Palgrave Macmillan",
             doi=None,
             url="https://oro.open.ac.uk/37679/",
             language="en", isbn=None,
             citation="Hall, S., Critcher, C., Jefferson, T., Clarke, J., & Roberts, B. (2013). Policing the Crisis (35th anniversary ed.). Basingstoke: Palgrave Macmillan.",
             locator="35th anniversary edition", locator_type="edition",
             supports="retrospective framing of the negotiation/marginalization argument", verified=True),
    ],
}

ENRICH = {
    "MC-654": dict(
        year=1995,
        summary="مدل تناسب وظیفه–فناوری، که دیل گودهیو و رونالد تامپسون در سال ۱۹۹۵ ارائه کردند، اثر فناوری اطلاعات بر عملکرد را نه به خود فناوری، بلکه به تناسب میان فناوری و وظیفه گره می‌زند. مدل سه عامل را جدا می‌کند: ویژگی‌های وظیفه، ویژگی‌های فناوری و توانایی‌های فرد. تناسب میان این سه، تعیین می‌کند که فناوری تا چه اندازه کار را آسان‌تر می‌کند و عملکرد فردی را بالا می‌برد. مدل دو مسیر را می‌بیند: مسیر تناسب که به بهبود کار و کیفیت می‌رسد، و مسیر استفاده که به پذیرش و بهره‌گیری وابسته است؛ استفاده بدون تناسب، عملکرد را بالا نمی‌برد. در رسانه، مدل برای ارزیابی ابزار خبرنگاری میدانی، اپلیکیشن جمع‌آوری خبر و سیستم مدیریت محتوا به کار می‌رود: ابزاری که با شرایط کار میدانی و سرعت خبر هم‌خوان نباشد، حتی اگر مدرن باشد، عملکرد را بهبود نمی‌دهد. نقدهای اصلی به آن، سنجش ذهنی تناسب، کم‌توجهی به عوامل سازمانی، سادگی مفهوم وظیفه و دشواری مقایسهٔ فناوری‌های چندکاره را برجسته می‌کنند.",
        definition="مدل تناسب وظیفه–فناوری، اثر فناوری بر عملکرد را نتیجهٔ تناسب میان ویژگی‌های وظیفه، ویژگی‌های فناوری و توانایی فرد می‌داند و استفاده بدون تناسب را بی‌اثر می‌شمارد.",
        main_problem="چرا فناوری‌های اطلاعاتی با کیفیت یکسان، در سازمان‌های مختلف عملکرد متفاوت می‌سازند و چگونه می‌توان تناسب ابزار و وظیفه را پیش از سرمایه‌گذاری سنجید.",
        mechanism="تناسب وظیفه و فناوری، هزینهٔ انجام کار را کاهش و کیفیت را افزایش می‌دهد؛ استفاده از فناوری تنها وقتی به عملکرد می‌رسد که این تناسب برقرار باشد و توانایی فرد نیز کافی باشد.",
        assumptions=[
            "وظیفه و فناوری قابل تفکیک‌اند.",
            "تناسب، متغیر اصلی اثر است.",
            "استفاده به تناسب وابسته است.",
            "توانایی فرد تعدیل می‌کند.",
            "عملکرد فردی هدف است.",
        ],
        principles=[
            "وظیفه را پیش از ابزار تحلیل کن.",
            "ویژگی فناوری را با وظیفه بسنج.",
            "توانایی کاربر را در نظر بگیر.",
            "تناسب را پیش از خرید آزمون کن.",
            "استفاده را با تناسب پیوند بده.",
            "اثر را در عملکرد بسنج، نه در استفاده.",
        ],
        critiques=[
            "تناسب را ذهنی می‌سنجد.",
            "عوامل سازمانی را کم می‌بیند.",
            "مفهوم وظیفه را ساده می‌گیرد.",
            "مقایسهٔ فناوری‌های چندکاره دشوار است.",
            "به یادگیری بلندمدت کم می‌پردازد.",
            "فرهنگ کاربر را کم‌وزن می‌کند.",
            "بازتعریف وظیفه در اثر یادگیری سازمانی را ایستا فرض می‌کند.",
            "اثر هم‌افزایی کار تیمی را در سنجش عملکرد نادیده می‌گیرد.",
            "شکاف میان تناسب ادراک‌شده و تناسب عینی را کم می‌سنجد.",
            "به هزینهٔ آموزش کاربر در محاسبهٔ تناسب کم توجه دارد.",
        ],
        critique_text="منتقدان می‌گویند تناسب وظیفه–فناوری چارچوبی دقیق برای ارزیابی ابزار داد اما سنجش تناسب را ذهنی گذاشت و عوامل سازمانی را کم‌بررسی کرد؛ با این حال، جایگزین مهمی برای مدل‌های صرفاً مبتنی بر پذیرش است.",
        applications=[
            "ارزیابی ابزار خبرنگاری میدانی.",
            "سنجش اپلیکیشن جمع‌آوری خبر.",
            "ارزیابی سیستم مدیریت محتوا.",
            "طراحی ابزار تحریریه.",
            "پژوهش فناوری اطلاعات.",
            "آموزش خبرنگار.",
            "برنامه‌ریزی آموزش ابزار بر پایهٔ شکاف تناسب.",
            "ارزیابی سامانهٔ آرشیو دیجیتال سازمان خبری.",
            "تحلیل شکاف مهارت و ابزار در دفاتر خبری منطقه‌ای.",
            "سنجش تناسب ابزار پخش زنده در پوشش رویداد ورزشی.",
        ],
        example_text="خبرنگاری که با تلفن همراه در محل حادثه گزارش می‌فرستد، ابزاری متناسب با وظیفهٔ سرعت دارد؛ همان تحریریه اگر سیستم سنگین آرشیو را برای کار میدانی تحمیل کند، تناسب را از دست می‌دهد و عملکرد پایین می‌آید؛ اما در تحریریهٔ کوچک که یک نفر هم گزارش می‌دهد و هم منتشر می‌کند، همان ابزار ممکن است متناسب شود و عملکرد را بالا ببرد.",
        evolution="مقالهٔ سال ۱۹۹۵ مدل را با داده‌های سازمانی آزمود و پژوهش‌های بعدی، تناسب را با پذیرش فناوری ترکیب کردند؛ گزارش‌های مروری، مدل را به حوزه‌های سلامت و رسانه گستردند.",
        key_concepts=["تناسب وظیفه–فناوری", "ویژگی وظیفه", "ویژگی فناوری", "استفاده", "عملکرد فردی", "توانایی کاربر"],
        theorists="دیل ال. گودهیو و رونالد ال. تامپسون.",
        theorists_text="مدل در سنت پژوهش سیستم‌های اطلاعاتی و عملکرد فردی شکل گرفت.",
        model="اثر فناوری بر عملکرد به‌عنوان نتیجهٔ تناسب وظیفه، فناوری و توانایی فرد، نه صرفاً کیفیت ابزار.",
        studies=[
            "مقالهٔ سال ۱۹۹۵ مدل را آزمود.",
            "مرور سال ۲۰۲۲ سازه‌ها را جمع‌بندی کرد.",
            "مطالعات خبر، ابزار میدانی را ارزیابی کردند.",
            "پژوهش سلامت، تناسب را در بالین سنجید.",
            "مطالعهٔ سازمانی، اثر آموزش بر بازتعریف تناسب را بررسی کرد.",
            "پژوهش شهری، تناسب سامانهٔ اطلاع‌رسانی بحران را سنجید.",
        ],
    ),
    "MC-674": dict(
        year=2018,
        summary="مدل اشاعهٔ خبر جعلی، که سوروش ووسوغی، دِب روی و سینان آرال در سال ۲۰۱۸ با تحلیل میلیون‌ها توییت منتشرشده میان سال‌های ۲۰۰۶ و ۲۰۱۷ صورت‌بندی کردند، نشان می‌دهد که خبر نادرست در شبکه‌های اجتماعی سریع‌تر، دورتر، عمیق‌تر و گسترده‌تر از خبر درست منتشر می‌شود. یافتهٔ کلیدی این بود که ربات‌ها عامل اصلی این تفاوت نیستند، بلکه انسان‌ها با رفتار اشتراک‌گذاری خود، خبر نادرست را تقویت می‌کنند. تحلیل محتوای پیام‌ها نشان داد که خبر نادرست بیش از خبر درست، تازگی و بار هیجانی دارد و همین ویژگی‌ها احتمال بازنشر را بالا می‌برد. مدل، اشاعه را حاصل تعامل ویژگی پیام، انگیزهٔ کاربر و ساختار شبکه می‌داند. در رسانه، مدل برای طراحی راهبرد راستی‌آزمایی، شناسایی نقاط اشاعه و آموزش سواد خبری به کار می‌رود. نقدهای اصلی به آن، محدودبودن به یک پلتفرم، دشواری تعریف تجربی نادرستی، تمرکز بر هیجان به‌جای انگیزهٔ سیاسی و کم‌توجهی به زمینهٔ کشورهای غیرغربی را برجسته می‌کنند.",
        definition="مدل اشاعهٔ خبر جعلی، اشاعهٔ سریع‌تر و گسترده‌تر خبر نادرست را حاصل تازگی و بار هیجانی پیام، رفتار اشتراک‌گذاری انسان و ساختار شبکه می‌داند، نه فقط فعالیت ربات‌ها.",
        main_problem="چرا خبر نادرست سریع‌تر از خبر درست منتشر می‌شود، چه عواملی این تفاوت را می‌سازند و مداخلهٔ مؤثر برای مهار آن کدام است.",
        mechanism="پیام نادرست با تازگی و هیجان بالا، توجه و بازنشر انسانی را برمی‌انگیزد؛ ساختار شبکه، این بازنشر را تشدید می‌کند و در غیاب راستی‌آزمایی، خبر جعلی به لایه‌های وسیع‌تری می‌رسد.",
        assumptions=[
            "نادرستی خبر سنجیدنی است.",
            "رفتار انسان موتور اشاعه است.",
            "تازگی و هیجان بازنشر را بالا می‌برد.",
            "ساختار شبکه اثر تشدید دارد.",
            "ربات‌ها عامل اصلی نیستند.",
        ],
        principles=[
            "پیام را پیش از بازنشر راستی‌آزمایی کن.",
            "هیجان را نشانهٔ هشدار بگیر.",
            "منبع را ردیابی کن.",
            "نقاط پرش اشاعه را پایش کن.",
            "سواد خبری را آموزش بده.",
            "ربات و انسان را از هم جدا کن.",
        ],
        critiques=[
            "به یک پلتفرم محدود است.",
            "تعریف نادرستی دشوار است.",
            "انگیزهٔ سیاسی را کم می‌بیند.",
            "زمینهٔ غیرغربی را کم دارد.",
            "به اشاعهٔ خارج از شبکه کم می‌پردازد.",
            "مداخلهٔ عملی را کم استنتاج می‌کند.",
            "نقش رسانه‌های سنتی در بازنشر روایت نادرست را جدا نمی‌سنجد.",
            "سنجش تازگی بر پایهٔ داده‌های یک پلتفرم، سوگیری نمونه دارد.",
            "تفاوت اشاعهٔ درون‌زبانی و ترجمه‌ای را جدا نمی‌کند.",
            "به تفاوت مخاطب عام و نخبه در بازنشر کم می‌پردازد.",
        ],
        critique_text="منتقدان می‌گویند مدل اشاعهٔ خبر جعلی یافته‌ای مهم و بزرگ‌مقیاس ساخت اما به یک پلتفرم محدود بود و انگیزهٔ سیاسی و زمینهٔ منطقه‌ای را کم‌بررسی گذاشت؛ با این حال، مرجع اصلی پژوهش اشاعهٔ نادرستی است.",
        applications=[
            "طراحی راهبرد راستی‌آزمایی.",
            "پایش اشاعهٔ شایعه.",
            "آموزش سواد خبری.",
            "سیاست پلتفرم.",
            "پژوهش رسانهٔ اجتماعی.",
            "تحلیل بحران اطلاعاتی.",
            "طراحی هشدار پیش از بازنشر برای تحریریه‌ها.",
            "ارزیابی کمپین واکسیناسیون در برابر شایعه.",
            "پایش روایت‌های انتخاباتی در پیام‌رسان‌ها.",
            "آموزش روزنامه‌نگار برای شناخت الگوی هیجانی شایعه.",
            "طراحی سازوکار گزارش شهروندی شایعهٔ محلی.",
        ],
        example_text="شایعه‌ای هیجانی دربارهٔ یک رویداد، در چند ساعت به میلیون‌ها کاربر می‌رسد در حالی که تکذیب آرام همان رویداد دیده نمی‌شود؛ مدل نشان می‌دهد که این تفاوت از الگوریتم نیست، از رفتار بازنشر ماست.",
        evolution="مقالهٔ سال ۲۰۱۸ با تحلیل سراسری توییتر منتشر شد و پژوهش‌های بعدی، مدل را به سایر پلتفرم‌ها، زمینه‌های انتخاباتی و مداخله‌های راستی‌آزمایی گستردند؛ در سال‌های بعد، پژوهش‌ها بر نقش پیام‌رسان‌ها و زمینهٔ زبانی غیرانگلیسی تمرکز کردند.",
        key_concepts=["خبر جعلی", "اشاعه", "بار هیجانی", "تازگی", "بازنشر انسانی", "راستی‌آزمایی"],
        theorists="سوروش ووسوغی، دِب روی و سینان آرال.",
        theorists_text="مدل در سنت پژوهش شبکه و ارتباطات سیاسی شکل گرفت.",
        model="اشاعهٔ سریع‌تر خبر نادرست به‌عنوان تعامل تازگی و هیجان پیام با بازنشر انسانی در ساختار شبکه.",
        studies=[
            "مقالهٔ سال ۲۰۱۸ توییتر را تحلیل کرد.",
            "خلاصهٔ پژوهشی سال ۲۰۱۸ نقش انسان را برجسته کرد.",
            "مطالعات راستی‌آزمایی، مداخله را سنجیدند.",
            "پژوهش سلامت، شایعهٔ واکسن را بررسی کرد.",
            "مطالعهٔ تطبیقی، تفاوت پلتفرم‌ها را در اشاعهٔ نادرستی سنجید.",
            "پژوهش ارتباطات سیاسی، خشم را عامل بازنشر یافت.",
            "مطالعهٔ پیام‌رسان، سرعت اشاعهٔ نادرستی را سنجید.",
        ],
    ),
    "MC-679": dict(
        year=1957,
        summary="مدل اسطوره و رسانه، که رولان بارت در کتاب اسطوره‌ها در سال ۱۹۵۷ پایه گذاشت و راجر سیلوراستون در سال ۱۹۸۱ به تلویزیون گسترد، نشان می‌دهد که رسانه چگونه معنای فرهنگی را طبیعی جلوه می‌دهد. بارت در تحلیل نشانه‌شناختی خود دو سطح معنا را از هم جدا کرد: سطح نخست، دلالت مستقیم نشانه است و سطح دوم، معنای فرهنگی افزوده که اسطوره نام دارد. اسطوره با پاک‌کردن تاریخ و زمینه، آنچه ساختهٔ فرهنگ است را بدیهی و طبیعی جلوه می‌دهد. سیلوراستون نشان داد که تلویزیون با روایت و ساختار اسطوره‌ای، تجربهٔ روزمره را به داستان‌های فرهنگی بدل می‌کند. مدل برای تحلیل اخبار، تبلیغات، ستاره‌ها و روایت‌های ملی به کار می‌رود و پرسش اصلی آن این است که چه چیزی بدیهی فرض شده و چه کسی از این بدیهی‌سازی سود می‌برد. نقدهای اصلی به آن، ساختارگرایی سخت، کم‌توجهی به مخاطب فعال، دشواری تعمیم تحلیل متنی و نادیده‌گرفتن تنوع فرهنگی را برجسته می‌کنند. مدل پرسش تحلیل فرهنگی را از «چه گفته شد» به «چه چیزی بدیهی فرض شد» تغییر می‌دهد. تحلیل بارت نشان می‌دهد که بی‌گناهی ظاهری یک تصویر، خودش پیامی ایدئولوژیک است.",
        definition="مدل اسطوره و رسانه، رسانه را سازوکار ساختن معنای سطح دومی می‌داند که با طبیعی جلوه‌دادن ارزش‌های فرهنگی، آن‌ها را از تاریخ و قدرت جدا می‌کند.",
        main_problem="رسانه چگونه ارزش‌ها و روابط قدرت را طبیعی و بدیهی جلوه می‌دهد، و تحلیل نشانه‌شناختی چگونه می‌تواند این طبیعی‌سازی را آشکار کند.",
        mechanism="نشانه در سطح نخست معنای مستقیم دارد؛ در سطح دوم، معنای فرهنگی افزوده می‌شود که تاریخ و زمینه را می‌زداید و ارزش‌ها را بدیهی می‌سازد.",
        assumptions=[
            "رسانه نظام نشانه‌ای است.",
            "معنا دو سطح دارد.",
            "اسطوره، تاریخ را می‌زداید.",
            "طبیعی‌سازی، قدرت را پنهان می‌کند.",
            "تحلیل متنی معنا را آشکار می‌کند.",
        ],
        principles=[
            "دلالت مستقیم را از اسطوره جدا کن.",
            "بپرس چه چیزی بدیهی فرض شده.",
            "تاریخ و زمینه را بازگردان.",
            "سود پنهان را آشکار کن.",
            "روایت را تحلیل کن.",
            "مخاطب را در تفسیر ببین.",
        ],
        critiques=[
            "ساختارگرایی سخت دارد.",
            "مخاطب فعال را کم می‌بیند.",
            "تعمیم تحلیل متنی دشوار است.",
            "تنوع فرهنگی را نادیده می‌گیرد.",
            "مرز اسطوره و ایدئولوژی مبهم است.",
            "اثر تجربی را کم می‌سنجد.",
            "نمونه‌های بارت کوتاه و بدون نمونه‌گیری نظام‌مند انتخاب شده‌اند.",
            "مرز اسطورهٔ خبری و اسطورهٔ سرگرمی روشن نیست.",
            "به شرایط تولید نشانه در صنعت رسانه کم توجه دارد.",
            "روش تحلیل را برای مقایسهٔ میان‌فرهنگی استاندارد نکرده است.",
        ],
        critique_text="منتقدان می‌گویند مدل اسطوره و رسانه ابزار نیرومندی برای آشکارکردن طبیعی‌سازی داد اما ساختارگرا بود و مخاطب و تنوع فرهنگی را کم‌بررسی گذاشت؛ با این حال، پایهٔ تحلیل فرهنگی رسانه است.",
        applications=[
            "تحلیل اسطورهٔ خبری.",
            "نقد تبلیغات.",
            "تحلیل ستاره‌سازی.",
            "پژوهش روایت ملی.",
            "آموزش سواد رسانه‌ای.",
            "تحلیل نشانه‌شناختی.",
            "تحلیل بازنمایی مهاجر در خبر تلویزیونی.",
            "نقد روایت ملی در مستند.",
            "بررسی تبلیغات سیاسی از منظر طبیعی‌سازی.",
            "تحلیل عکس خبری از منظر اسطوره.",
        ],
        example_text="خبری که یک گروه را «تهدید طبیعی» می‌نامد، پیش از آنکه استدلال کند، معنای فرهنگی را در سطح دوم جا می‌اندازد؛ تحلیل بارت می‌پرسد این بدیهی‌بودن از کجا آمده و چه کسی از آن سود می‌برد.",
        evolution="کتاب سال ۱۹۵۷ بارت پایهٔ نشانه‌شناسی فرهنگی را گذاشت و سیلوراستون در سال ۱۹۸۱ آن را به روایت تلویزیونی برد؛ مطالعات فرهنگی بعدی، مخاطب و قدرت را به مدل افزودند و نشانه‌شناسی اجتماعی، لایهٔ مخاطب را به تحلیل افزود.",
        key_concepts=["اسطوره", "دلالت سطح دوم", "طبیعی‌سازی", "نشانه‌شناسی", "روایت", "ایدئولوژی"],
        theorists="رولان بارت و راجر سیلوراستون.",
        theorists_text="مدل در سنت نشانه‌شناسی و مطالعات فرهنگی شکل گرفت.",
        model="رسانه به‌عنوان سازوکار معنای سطح دوم که ارزش‌های فرهنگی را طبیعی و بدیهی جلوه می‌دهد.",
        studies=[
            "کتاب سال ۱۹۵۷ پایهٔ تحلیل اسطوره را گذاشت.",
            "کتاب سال ۱۹۸۱ آن را به تلویزیون برد.",
            "مطالعات خبر، اسطورهٔ تهدید را تحلیل کردند.",
            "پژوهش تبلیغات، طبیعی‌سازی را نشان داد.",
            "مطالعهٔ تلویزیون، ساختار روایت اسطوره‌ای را تحلیل کرد.",
            "تحلیل تبلیغات، طبیعی‌سازی مصرف را نشان داد.",
            "پژوهش نشانه‌شناسی، عکس خبری را همچون اسطوره خواند.",
        ],
    ),
    "MC-697": dict(
        year=1978,
        summary="مدل مذاکره و حاشیه‌نشینی خبر، که استوارت هال و همکارانش در کتاب پلیس‌کردن بحران سال ۱۹۷۸ صورت‌بندی کردند، نشان می‌دهد که معنا در خبر نه ساختهٔ رسانه به‌تنهایی، بلکه حاصل مذاکره میان منابع قدرت و روزنامه‌نگاران است. در این مدل، مقام‌های رسمی به‌عنوان تعریف‌کنندگان اولیه، چارچوب اصلی رویداد را تعیین می‌کنند و رسانه آن را بازتولید می‌کند. صداهای مخالف به حاشیه رانده می‌شوند یا تنها در قالب چارچوب رسمی اجازهٔ ظهور می‌یابند. هال و همکارانش با مطالعهٔ پوشش «سرقت خیابانی» در بریتانیا نشان دادند که رسانه چگونه بحران اخلاقی می‌سازد، افکار عمومی را آماده می‌کند و سیاست سخت‌گیرانه را مشروع می‌سازد. مدل سه سازوکار را برجسته می‌کند: تعریف اولیه، تقویت و حاشیه‌رانی. در رسانه، مدل برای تحلیل پوشش جرم، مهاجرت، اعتراض و بحران به کار می‌رود. در این چارچوب، بی‌طرفی ظاهری خبر نیز خود یک موضع است، زیرا چارچوب رسمی را بدون نام‌گذاری بازتولید می‌کند. نقدهای اصلی به آن، کارکردگرایی ضمنی، تمرکز بر بافت بریتانیایی، کم‌توجهی به مقاومت مخاطب و دشواری تعمیم به محیط چندرسانه‌ای را برجسته می‌کنند.",
        definition="مدل مذاکره و حاشیه‌نشینی خبر، تولید معنا را حاصل مذاکرهٔ منابع قدرت و رسانه می‌داند که با تعریف اولیه، چارچوب رسمی را مسلط و صداهای مخالف را حاشیه‌ای می‌کند.",
        main_problem="رسانه چگونه چارچوب رسمی رویداد را مسلط می‌کند، صداهای مخالف را به حاشیه می‌راند و از این راه بحران اخلاقی و سیاست سخت‌گیرانه را مشروع می‌سازد.",
        mechanism="منابع رسمی، تعریف اولیهٔ رویداد را می‌دهند؛ رسانه با تکیه بر آن، چارچوب را تقویت می‌کند و صداهای مخالف را در قالب همان چارچوب یا در حاشیه بازنمایی می‌کند.",
        assumptions=[
            "معنا مذاکره‌ای است.",
            "منابع رسمی تعریف اولیه دارند.",
            "رسانه چارچوب را تقویت می‌کند.",
            "صداهای مخالف حاشیه‌ای می‌شوند.",
            "خبر، بحران اخلاقی می‌سازد.",
        ],
        principles=[
            "منبع تعریف اولیه را شناسایی کن.",
            "چارچوب رسمی را آشکار کن.",
            "صدای حاشیه‌ای را بشنو.",
            "بحران اخلاقی را از رویداد جدا کن.",
            "زمینهٔ سیاسی را ببین.",
            "مقاومت مخاطب را جدی بگیر.",
        ],
        critiques=[
            "کارکردگرایی ضمنی دارد.",
            "بر بریتانیا متمرکز است.",
            "مقاومت مخاطب را کم می‌بیند.",
            "تعمیم به محیط چندرسانه‌ای دشوار است.",
            "نقش اقتصاد رسانه را کم‌وزن می‌کند.",
            "به رسانهٔ دیجیتال کم می‌پردازد.",
            "رسانه‌های تجاری و عمومی را در سنجش تعریف اولیه یکسان می‌گیرد.",
            "نقش منابع دیجیتال غیررسمی در شکستن انحصار تعریف را کم می‌بیند.",
            "به تفاوت تعریف اولیه در رسانهٔ عمومی و خصوصی کم می‌پردازد.",
            "به فرایند درونی تحریریه در انتخاب منبع کم توجه دارد.",
        ],
        critique_text="منتقدان می‌گویند مدل مذاکره و حاشیه‌نشینی بینش مهمی دربارهٔ تعریف اولیه و بحران اخلاقی داد اما کارکردگرا بود و مقاومت مخاطب را کم‌بررسی گذاشت؛ با این حال، پایهٔ تحلیل انتقادی خبر است.",
        applications=[
            "تحلیل پوشش جرم.",
            "پژوهش بحران مهاجرت.",
            "نقد پوشش اعتراض.",
            "مطالعات هراس اخلاقی.",
            "آموزش روزنامه‌نگاری انتقادی.",
            "تحلیل رسانه و سیاست.",
            "تحلیل پوشش رسانه‌ای اعتراض‌های خیابانی.",
            "پژوهش هراس اخلاقی دربارهٔ بازی‌های رایانه‌ای.",
            "تحلیل پوشش بحران بهداشت عمومی.",
        ],
        example_text="پوششی که یک حادثهٔ محلی را به «موج جدید جرم» بدل می‌کند، با تعریف اولیهٔ پلیس و تقویت رسانه‌ای، بحرانی اخلاقی می‌سازد؛ صدای جامعهٔ متهم تنها در حاشیهٔ همان چارچوب شنیده می‌شود.",
        evolution="کتاب سال ۱۹۷۸ مدل را با مطالعهٔ تاریخی بحران سرقت خیابانی ساخت و ویراست سی‌وپنجمین سال در سال ۲۰۱۳ آن را با مطالعات فرهنگی بعدی بازخوانی کرد؛ پژوهش‌های دیجیتال بعدی، مفهوم تعریف اولیه را به منابع شبکه‌ای و پلتفرمی گستردند و پلتفرم‌ها را تعریف‌کنندهٔ تازه دانستند.",
        key_concepts=["تعریف اولیه", "بحران اخلاقی", "حاشیه‌رانی", "مذاکرهٔ معنا", "منابع رسمی", "مشروعیت‌سازی"],
        theorists="استوارت هال، چارلی کریچر، تونی جفرسون، جان کلارک و برایان رابرتز.",
        theorists_text="مدل در سنت مطالعات فرهنگی بیرمنگام شکل گرفت.",
        model="تولید خبر به‌عنوان مذاکرهٔ تعریف اولیه با منابع قدرت و حاشیه‌رانی صداهای مخالف.",
        studies=[
            "کتاب سال ۱۹۷۸ بحران سرقت خیابانی را تحلیل کرد.",
            "ویراست سال ۲۰۱۳ آن را بازخوانی کرد.",
            "مطالعات هراس، پوشش جرم را سنجید.",
            "پژوهش مهاجرت، تعریف اولیه را ردیابی کرد.",
            "مطالعهٔ تطبیقی، حاشیه‌رانی صدای معترضان را سنجید.",
            "پژوهش دیجیتال، تعریف اولیهٔ پلتفرم را بررسی کرد.",
        ],
    ),
}

NAME_FIX = {}
YEAR_FIX = {
    "MC-654": "بدنهٔ کارت قالب عمومی محیط رسانه‌ای بود و به تناسب وظیفه–فناوری ربطی نداشت؛ محتوا بر پایهٔ گودهیو و تامپسون ۱۹۹۵ بازنویسی شد.",
    "MC-674": "بدنهٔ کارت، مدل نظارت داده را به ووسوغی نسبت می‌داد؛ هستهٔ مقالهٔ ۲۰۱۸ اشاعهٔ خبر نادرست است و محتوا بر همان پایه بازنویسی شد.",
    "MC-679": "کارت سال و متن منسجم نداشت و بارت را با مدل مخاطب فعال آمیخته بود؛ سال ۱۹۵۷ و ۱۹۸۱ و مدل اسطوره مبنا قرار گرفت.",
    "MC-697": "بدنهٔ کارت تقریباً خالی بود و فقط به پلیس‌کردن بحران اشاره داشت؛ محتوا بر پایهٔ هال و همکاران ۱۹۷۸ و ویراست ۲۰۱۳ بازنویسی شد.",
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
                                       "verified": n_verified, "batch": 157}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH157 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
