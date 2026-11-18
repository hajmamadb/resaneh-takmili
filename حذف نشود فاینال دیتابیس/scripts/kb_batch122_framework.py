# -*- coding: utf-8 -*-
"""Batch 122 (FRAMEWORK): full documentation for MC-499, MC-500, MC-520, MC-538."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch122-framework-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch122_framework.json"

S = {
    "MC-499": [
        dict(kind="BOOK",
             title_en="Fame and Fortune: How Successful Companies Build Winning Reputations",
             title_fa="نام و ثروت: چگونه شرکت‌های موفق شهرت برنده می‌سازند",
             authors="Fombrun, C. J.; van Riel, C. B. M.", year=2004,
             publisher="Financial Times Prentice Hall",
             doi=None,
             url="https://books.google.com/books/about/Fame_Fortune.html?id=7iZcLsu5HxgC",
             language="en", isbn=None,
             citation="Fombrun, C. J., & van Riel, C. B. M. (2004). Fame and fortune: How successful companies build winning reputations. Financial Times Prentice Hall.",
             locator="chs. 1-4", locator_type="work",
             supports="reputation as reputational capital built through identity, image and performance alignment", verified=True),
        dict(kind="BOOK",
             title_en="Reputation: Realizing Value from the Corporate Image",
             title_fa="شهرت: تحقق ارزش از تصویر شرکتی",
             authors="Fombrun, C. J.", year=1996,
             publisher="Harvard Business School Press",
             doi=None, url=None, language="en", isbn=None,
             citation="Fombrun, C. J. (1996). Reputation: Realizing value from the corporate image. Harvard Business School Press.",
             locator="chs. 1-2", locator_type="work",
             supports="reputation as an aggregate of stakeholder perceptions yielding economic value", verified=False),
    ],
    "MC-500": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Defining Strategic Communication",
             title_fa="تعریف ارتباطات راهبردی",
             authors="Hallahan, K.; Holtzhausen, D.; van Ruler, B.; Vercic, D.; Sriramesh, K.", year=2007,
             publisher="International Journal of Strategic Communication",
             doi="10.1080/15531180701285244",
             url="https://www.tandfonline.com/doi/abs/10.1080/15531180701285244",
             language="en", isbn=None,
             citation="Hallahan, K., Holtzhausen, D., van Ruler, B., Vercic, D., & Sriramesh, K. (2007). Defining strategic communication. International Journal of Strategic Communication, 1(1), 3-35.",
             locator="1(1):3-35", locator_type="page_range",
             supports="strategic communication as the purposeful use of communication to fulfill an organization's mission", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Communication Theory: An Underrated Pillar on Which Strategic Communication Rests",
             title_fa="نظریهٔ ارتباطات: ستونی کم‌ارزش‌شمرده که ارتباطات راهبردی بر آن استوار است",
             authors="van Ruler, B.", year=2018,
             publisher="International Journal of Strategic Communication",
             doi=None, url=None, language="en", isbn=None,
             citation="van Ruler, B. (2018). Communication theory: An underrated pillar on which strategic communication rests. International Journal of Strategic Communication, 12(4), 367-381.",
             locator="12(4):367-381", locator_type="page_range",
             supports="theoretical grounding of strategic communication in general communication theory", verified=False),
    ],
    "MC-520": [
        dict(kind="BOOK",
             title_en="Virtual Reality",
             title_fa="واقعیت مجازی",
             authors="Rheingold, H.", year=1991,
             publisher="Summit Books",
             doi=None,
             url="https://books.google.com/books/about/Virtual_Reality.html?id=hHZQAAAAMAAJ",
             language="en", isbn=None,
             citation="Rheingold, H. (1991). Virtual reality. Summit Books.",
             locator="chs. 1-3", locator_type="work",
             supports="popular account of immersive VR systems and their communicative promise", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Defining Virtual Reality: Dimensions Determining Telepresence",
             title_fa="تعریف واقعیت مجازی: ابعاد تعیین‌کنندهٔ حضور از دور",
             authors="Steuer, J.", year=1992,
             publisher="Journal of Communication",
             doi=None,
             url="https://www.semanticscholar.org/paper/Defining-virtual-reality%3A-dimensions-determining-Steuer/5ac60be482fe521fdbe601c432e58068287f7036",
             language="en", isbn=None,
             citation="Steuer, J. (1992). Defining virtual reality: Dimensions determining telepresence. Journal of Communication, 42(4), 73-93.",
             locator="42(4):73-93", locator_type="page_range",
             supports="VR defined by telepresence, determined by vividness and interactivity", verified=True),
    ],
    "MC-538": [
        dict(kind="OTHER",
             title_en="From Game Design Elements to Gamefulness: Defining Gamification",
             title_fa="از عناصر طراحی بازی تا بازی‌گونگی: تعریف گیمیفیکیشن",
             authors="Deterding, S.; Dixon, D.; Khaled, R.; Nacke, L.", year=2011,
             publisher="ACM (MindTrek 2011)",
             doi="10.1145/2181037.2181040",
             url="https://dl.acm.org/doi/10.1145/2181037.2181040",
             language="en", isbn=None,
             citation="Deterding, S., Dixon, D., Khaled, R., & Nacke, L. (2011). From game design elements to gamefulness: Defining gamification. In Proceedings of the 15th International Academic MindTrek Conference (pp. 9-15). ACM.",
             locator="pp. 9-15", locator_type="page_range",
             supports="gamification as the use of game design elements in non-game contexts", verified=True),
        dict(kind="OTHER",
             title_en="Does Gamification Work? A Literature Review of Empirical Studies on Gamification",
             title_fa="آیا گیمیفیکیشن کار می‌کند؟ مروری بر مطالعات تجربی گیمیفیکیشن",
             authors="Hamari, J.; Koivisto, J.; Sarsa, H.", year=2014,
             publisher="HICSS",
             doi=None, url=None, language="en", isbn=None,
             citation="Hamari, J., Koivisto, J., & Sarsa, H. (2014). Does gamification work? A literature review of empirical studies on gamification. In Proceedings of the 47th Hawaii International Conference on System Sciences (pp. 3025-3034). IEEE.",
             locator="pp. 3025-3034", locator_type="page_range",
             supports="mixed but generally positive effects of gamification, contingent on context and design", verified=False),
    ],
}

ENRICH = {
    "MC-499": dict(
        summary="مدیریت اعتبار و شهرت، چارچوبی برای فهم چگونگی ساخت، حفظ و دفاع از باورهای مخاطبان دربارهٔ قابلیت اعتماد و کیفیت یک سازمان یا رسانه است. در سنت پژوهش اقناع، اعتبار منبع به دو مؤلفهٔ تخصص و قابلیت اعتماد تقسیم می‌شود: مخاطب باید باور کند گوینده دانش لازم را دارد و انگیزهٔ او خیرخواهانه است. چارلز فومبران و کیس ون ریل در کتاب سال ۲۰۰۴ خود شهرت را سرمایه‌ای راهبردی دانستند که از تلاقی سه چیز ساخته می‌شود: هویت اعلام‌شدهٔ سازمان، تصویری که ذی‌نفعان می‌سازند و عملکرد واقعی سازمان. در این نگاه، شهرت مجموع ارزیابی‌های ذی‌نفعان در ابعاد مختلف است و به دارایی نامرئی تبدیل می‌شود که اعتماد، وفاداری و ارزش اقتصادی می‌آفریند. مدیریت شهرت با سنجش مستمر ادراک ذی‌نفعان، هم‌ترازی گفتار و کردار، شفافیت گزارش‌دهی و آمادگی برای بحران انجام می‌شود. در سازمان‌های رسانه‌ای، اعتبار حرفه‌ای سرمایهٔ اصلی است: اعتماد مخاطب به دقت، بی‌طرفی و پاسخ‌گویی، مستقیماً بر انتخاب رسانه اثر می‌گذارد. نقد اصلی به این چارچوب، خطر تبدیل اعتبار به مدیریت تصویر و پنهان‌کاری، دشواری سنجش معتبر شهرت و کم‌توجهی به ساختار قدرت رسانه‌ای است. یادآوری: متن کارت تحریریهٔ این مدخل با محتوای آن هم‌خوان نبود و مستندسازی حاضر بر پایهٔ منابع تأییدشده بازنویسی شده است.",
        definition="مدیریت اعتبار و شهرت، مجموعهٔ راهبردها و سنجه‌هایی است که سازمان برای ساخت و حفظ باور ذی‌نفعان به تخصص، صداقت و کیفیت خود به کار می‌گیرد.",
        main_problem="چگونه سازمان می‌تواند باور عمومی به قابلیت اعتماد خود را بسازد و در برابر بحران، اطلاعات نادرست و رقابت حفظ کند، بی‌آنکه به مدیریت تصویر فریب‌کارانه فروکاسته شود.",
        mechanism="سازمان هویت خود را اعلام می‌کند، عملکردش را در معرض تجربهٔ ذی‌نفعان می‌گذارد و از مجرای رسانه، گزارش و تعامل مستقیم، تفسیر مثبت می‌سازد؛ شواهد مستقل و رفتار بحرانی، این تفسیر را تأیید یا تخریب می‌کنند.",
        assumptions=[
            "اعتبار، ادراکی است که در ذهن مخاطب ساخته می‌شود.",
            "تخصص و قابلیت اعتماد دو مؤلفهٔ مستقل اعتبارند.",
            "شهرت به ارزش اقتصادی و وفاداری تبدیل می‌شود.",
            "هم‌ترازی گفتار و کردار شرط پایدار ماندن شهرت است.",
        ],
        principles=[
            "اعتبار با ادعا ساخته نمی‌شود، با شواهد عملکرد تأیید می‌شود.",
            "شفافیت در بحران، سرمایهٔ اعتماد را حفظ می‌کند.",
            "سنجش مستمر ادراک ذی‌نفعان، بخشی از مدیریت شهرت است.",
            "اعتبار رسانه به دقت، پاسخ‌گویی و استقلال حرفه‌ای گره خورده است.",
        ],
        critiques=[
            "مدیریت شهرت می‌تواند به مدیریت تصویر و پنهان‌کاری تبدیل شود.",
            "سنجه‌های شهرت اغلب ادراک نخبگان را به‌جای ادراک عمومی می‌سنجند.",
            "چارچوب به ساختار مالکیت و فشار سیاسی بر رسانه کم‌تر می‌پردازد.",
            "رابطهٔ علّی شهرت و عملکرد مالی به‌سختی اثبات‌پذیر است.",
        ],
        applications=[
            "مدیریت اعتبار سازمان‌های خبری و پاسخ به بحران بی‌اعتمادی.",
            "ارزیابی اعتبار منبع در پیام‌های سلامت و کمپین‌های عمومی.",
            "تحلیل شهرت برند و مقایسهٔ آن با رقبا.",
            "آموزش ارتباطات بحران به سازمان‌های رسانه‌ای.",
        ],
        evolution="پژوهش اقناع از دههٔ ۱۹۵۰ اعتبار منبع را به تخصص و قابلیت اعتماد تفکیک کرد؛ فومبران (۱۹۹۶) و فومبران و ون ریل (۲۰۰۴) شهرت را به سرمایهٔ راهبردی و سنجهٔ سازمانی تبدیل کردند و پژوهش‌های پلتفرمی، اعتبار را به امتیاز، نظر کاربران و شفافیت الگوریتمی گستردند.",
        key_concepts=[
            "اعتبار منبع (Source Credibility)",
            "تخصص و قابلیت اعتماد (Expertise and Trustworthiness)",
            "سرمایهٔ شهرت (Reputational Capital)",
            "هم‌ترازی هویت و تصویر (Identity-Image Alignment)",
            "ارتباطات بحران (Crisis Communication)",
        ],
        theorists="چارلز فومبران؛ کیس ون ریل",
        theorists_text="فومبران و ون ریل (۲۰۰۴)؛ فومبران (۱۹۹۶)",
        model="هویت اعلام‌شده → عملکرد واقعی → ادراک ذی‌نفعان → سرمایهٔ شهرت → اعتماد و ارزش اقتصادی.",
        studies=[
            "فومبران و ون ریل (۲۰۰۴) شهرت را حاصل هم‌ترازی هویت، تصویر و عملکرد دانستند.",
            "فومبران (۱۹۹۶) شهرت را مجموعهٔ ادراکات ذی‌نفعان با ارزش اقتصادی تعریف کرد.",
        ],
        detailed_analysis="تحلیل عمیق نشان می‌دهد اعتبار و شهرت دو سطح متفاوت‌اند: اعتبار به قضاوت دربارهٔ یک پیام یا منبع در لحظه مربوط است و شهرت به ارزیابی انباشته و تاریخی سازمان. رسانه‌ای که در یک خبر خطا کند ممکن است اعتبار آن خبر را از دست بدهد، اما شهرت بلندمدت آن با پاسخ‌گویی سریع حفظ شود. در محیط پلتفرمی، امتیاز کاربران و نظر عمومی، سنجهٔ شهرت را دموکراتیک‌تر اما آسیب‌پذیرتر کرده است.",
        critique_text="نقد اصلی آن است که مدیریت شهرت می‌تواند به مدیریت تصویر و پنهان‌کاری تبدیل شود و رابطهٔ علّی میان شهرت و عملکرد مالی به‌سختی اثبات‌پذیر است.",
        example_text="یک روزنامه پس از انتشار خبر نادرست، اصلاحیهٔ برجسته و توضیح فرایند خطا را منتشر می‌کند؛ این پاسخ‌گویی، اعتبار خبر را بازنمی‌گرداند اما شهرت حرفه‌ای سازمان را در بلندمدت حفظ می‌کند.",
        year=2004,
    ),
    "MC-500": dict(
        summary="ارتباطات راهبردی، چارچوبی است که ارتباط سازمانی را نه فعالیتی حاشیه‌ای، بلکه ابزاری هدفمند برای تحقق مأموریت سازمان تعریف می‌کند. کرک هالاهان و همکارانش در مقالهٔ سال ۲۰۰۷ اصطلاح را چنین تعریف کردند: استفادهٔ هدفمند از ارتباط توسط سازمان برای انجام مأموریت خود. در این چارچوب، راهبردی بودن به معنای پیوند هر پیام با اهداف سازمانی، مخاطبان مشخص و نتایج سنجش‌پذیر است. نویسندگان شش حوزهٔ کاربرد را از هم تفکیک کردند: مدیریت، بازاریابی، روابط عمومی، ارتباطات فنی، ارتباطات سیاسی و ارتباطات سلامت؛ و تأکید کردند که این حوزه‌ها در سطح فردی، گروهی، سازمانی و اجتماعی عمل می‌کنند. ارتباطات راهبردی بر پایهٔ پژوهش مخاطب، تحلیل محیط، تعیین پیام و انتخاب کانال بنا می‌شود و با سنجش اثر، چرخهٔ خود را کامل می‌کند. در سازمان‌های رسانه‌ای، این چارچوب هم برای ارتباط با مخاطب و هم برای مدیریت اعتبار، بحران و روابط با ذی‌نفعان به کار می‌رود. تفاوت آن با تبلیغات در گسترهٔ آن است: ارتباطات راهبردی همهٔ اشکال ارتباط هدفمند سازمان را در بر می‌گیرد و به هم‌ترازی پیام‌ها در سطح کل سازمان توجه دارد. کاربرد آن در طراحی کمپین‌های عمومی، مدیریت بحران، ارتباطات سیاسی و دیپلماسی عمومی گسترده است. نقد اصلی به این چارچوب، گرایش ابزاری و یک‌سویه به ارتباط، کم‌توجهی به اخلاق اقناع و دشواری سنجش اثر بلندمدت است.",
        definition="ارتباطات راهبردی، استفادهٔ هدفمند و برنامه‌ریزی‌شده از ارتباط توسط سازمان برای تحقق مأموریت، مدیریت روابط با ذی‌نفعان و ساختن معنای مشترک است.",
        main_problem="چگونه سازمان می‌تواند همهٔ پیام‌ها و کانال‌های ارتباطی خود را با اهداف راهبردی هم‌تراز کند و اثر آن‌ها را بسنجد، بدون آنکه ارتباط به مجموعه‌ای از تاکتیک‌های پراکنده فروکاسته شود.",
        mechanism="سازمان محیط و ذی‌نفعان را تحلیل می‌کند، اهداف ارتباطی را از مأموریت استخراج می‌کند، پیام و کانال را انتخاب می‌سازد، اجرا می‌کند و با شاخص‌های اثر، برنامه را بازتنظیم می‌کند؛ هم‌ترازی میان واحدهای سازمانی، شرط انسجام پیام است.",
        assumptions=[
            "ارتباط سازمانی می‌تواند هدفمند و برنامه‌ریزی‌شده باشد.",
            "هم‌ترازی پیام‌ها در سطح سازمان، اثر را افزایش می‌دهد.",
            "مخاطب و محیط قابل تحلیل و بخش‌بندی‌اند.",
            "اثر ارتباط را می‌توان با شاخص سنجید و بازخورد گرفت.",
        ],
        principles=[
            "هر فعالیت ارتباطی باید به هدف سازمانی گره بخورد.",
            "تحقیق مخاطب، پیش‌شرط طراحی پیام است.",
            "انسجام پیام میان واحدها، اعتبار سازمان را می‌سازد.",
            "سنجش اثر، بخشی از فرایند راهبردی است، نه افزودهٔ پایانی.",
        ],
        critiques=[
            "چارچوب گرایش ابزاری و یک‌سویه به ارتباط دارد.",
            "اخلاق اقناع و خطر دستکاری کمتر تحلیل می‌شود.",
            "سنجش اثر بلندمدت ارتباط دشوار و اغلب نادیده گرفته می‌شود.",
            "تعریف گسترده، مرز آن را با سایر حوزه‌های ارتباطی مبهم می‌کند.",
        ],
        applications=[
            "طراحی کمپین ارتباطی سازمان‌های رسانه‌ای و عمومی.",
            "مدیریت بحران و هم‌ترازی پیام در چند کانال.",
            "ارتباطات سیاسی و دیپلماسی عمومی.",
            "آموزش مدیریت ارتباطات در سازمان‌های چندواحدی.",
        ],
        evolution="اصطلاح از دههٔ ۱۹۹۰ در ادبیات روابط عمومی و مدیریت رسانه رواج یافت؛ هالاهان و همکاران (۲۰۰۷) تعریف، حوزه‌ها و سطوح آن را نظام‌مند کردند و پژوهش‌های بعدی آن را به رسانه‌های اجتماعی، شفافیت سازمانی و اخلاق ارتباطات گستردند.",
        key_concepts=[
            "ارتباط هدفمند (Purposeful Communication)",
            "هم‌ترازی پیام (Message Alignment)",
            "ذی‌نفعان سازمانی (Organizational Stakeholders)",
            "سنجش اثر (Outcome Measurement)",
            "ارتباطات بحران (Crisis Communication)",
        ],
        theorists="کرک هالاهان؛ دیرک هولتسهاوزن؛ بت ون رولر؛ دژان ورچیچ؛ کریشنامورتی سری‌رامش",
        theorists_text="هالاهان و همکاران (۲۰۰۷)؛ ون رولر (۲۰۱۸)",
        model="تحلیل محیط → تعیین هدف از مأموریت → طراحی پیام و کانال → اجرا → سنجش اثر → بازتنظیم.",
        studies=[
            "هالاهان و همکاران (۲۰۰۷) ارتباطات راهبردی را تعریف و شش حوزهٔ کاربرد آن را تفکیک کردند.",
            "ون رولر (۲۰۱۸) بر پیوند نظری ارتباطات راهبردی با نظریهٔ عمومی ارتباطات تأکید کرد.",
        ],
        detailed_analysis="تحلیل عمیق نشان می‌دهد ارزش چارچوب در جابه‌جایی کانون از تاکتیک به مأموریت است: پیام خوب بدون پیوند با هدف سازمانی، فقط سر و صداست. در سازمان رسانه‌ای، این هم‌ترازی میان تحریریه، بازاریابی و روابط عمومی اغلب محل تنش است، زیرا منطق خبر با منطق تبلیغ تفاوت دارد. چارچوب راهبردی زمانی موفق است که استقلال تحریریه را به‌عنوان شرط اعتبار در نظر بگیرد، نه مانعی برای پیام واحد.",
        critique_text="نقد اصلی آن است که چارچوب گرایش ابزاری و یک‌سویه دارد، اخلاق اقناع را کم‌رنگ می‌کند و سنجش اثر بلندمدت ارتباط را دشوار می‌سازد.",
        example_text="دانشگاهی که برای جذب دانشجو کمپین راه می‌اندازد، باید پیام تبلیغاتی خود را با تجربهٔ واقعی کلاس، خدمات و کیفیت آموزش هم‌تراز کند؛ ناهم‌ترازی این دو، به بی‌اعتمادی می‌انجامد.",
        year=2007,
    ),
    "MC-520": dict(
        summary="واقعیت مجازی، چارچوبی برای تحلیل محیط‌های شبیه‌سازی‌شده‌ای است که کاربر را در فضایی رایانه‌ساخته غوطه‌ور می‌کنند و تجربهٔ حضور در آن فضا را می‌سازند. هاوارد رینگولد در کتاب سال ۱۹۹۱ خود این فناوری را به مخاطب عمومی معرفی کرد و آن را امکانی برای تجربهٔ محیط‌هایی دانست که یا وجود ندارند یا دسترسی به آن‌ها خطرناک و پرهزینه است. جاناتان استویر در مقالهٔ سال ۱۹۹۲ تعریفی ارتباطی‌تر ارائه داد: واقعیت مجازی را نه با دستگاه، بلکه با تجربهٔ حضور از دور تعریف کرد که از دو بعد زنده‌بودن و تعامل‌پذیری ساخته می‌شود. زنده‌بودن به غنای حسی و گسترهٔ کانال‌های ادراکی مربوط است و تعامل‌پذیری به توانایی کاربر در تغییر محیط و دریافت بازخورد سریع. از ترکیب این دو، درجهٔ غوطه‌وری و احساس «بودن در آنجا» شکل می‌گیرد. کاربردهای رسانه‌ای آن از مستند غوطه‌ور و خبر شبیه‌سازی‌شده تا آموزش پزشکی، درمان مواجهه‌ای و بازی‌های واقعیت مجازی گسترده است. این چارچوب پرسش‌های تازه‌ای دربارهٔ ادراک، بدن، حضور و اخلاق تجربهٔ مصنوعی مطرح می‌کند و در مطالعات بازی، سلامت و آموزش رسانه‌ای کاربرد دارد. نقد اصلی به آن، تمرکز بر فناوری و کم‌توجهی به بافت اجتماعی، هزینهٔ دسترسی، عوارض جسمی و خطر جدایی تجربهٔ مجازی از مسئولیت واقعی است. از این رو پژوهش رسانه‌ای معاصر آن را در پیوند با بدن، هویت و مرز میان تجربهٔ واقعی و مصنوعی تحلیل می‌کند.",
        definition="واقعیت مجازی، محیطی رایانه‌ساخته است که کاربر با حواس خود در آن غوطه‌ور می‌شود و تجربهٔ حضور در فضایی دیگر را به‌دست می‌آورد؛ این تجربه با زنده‌بودن و تعامل‌پذیری سنجیده می‌شود.",
        main_problem="چه چیزی تجربهٔ حضور در محیط مجازی را می‌سازد و چگونه می‌توان اثر ارتباطی این تجربه را بر ادراک، احساس و رفتار کاربر توضیح داد.",
        mechanism="سامانه با ارائهٔ محرک‌های حسی غنی و پاسخ سریع به کنش کاربر، حس حضور را می‌سازد؛ هرچه زنده‌بودن و تعامل‌پذیری بیشتر باشد، غوطه‌وری و انتقال تجربه قوی‌تر می‌شود.",
        assumptions=[
            "تجربهٔ حضور را می‌توان از فناوری دستگاه جدا تحلیل کرد.",
            "زنده‌بودن و تعامل‌پذیری دو بعد اصلی حضورند.",
            "حس حضور بر ادراک و رفتار کاربر اثر می‌گذارد.",
            "محیط مجازی می‌تواند جای تجربهٔ واقعی را در برخی موقعیت‌ها بگیرد.",
        ],
        principles=[
            "واقعیت مجازی با تجربه تعریف می‌شود، نه فقط با سخت‌افزار.",
            "غنای حسی و پاسخ‌گویی، عمق غوطه‌وری را تعیین می‌کند.",
            "بدن کاربر بخشی از حلقهٔ بازخورد تجربه است.",
            "طراحی تجربه باید پیامدهای اخلاقی و جسمی را در نظر بگیرد.",
        ],
        critiques=[
            "چارچوب بر فناوری تمرکز می‌کند و بافت اجتماعی مصرف را کم‌رنگ می‌سازد.",
            "هزینه و دسترسی نابرابر، شکاف دیجیتال تازه‌ای می‌سازد.",
            "عوارض جسمی و روانی تجربهٔ طولانی کمتر تحلیل شده است.",
            "خطر جدایی تجربهٔ مجازی از مسئولیت در جهان واقعی مطرح است.",
        ],
        applications=[
            "مستند غوطه‌ور و بازسازی خبری رویدادها.",
            "آموزش مهارت‌های پزشکی، صنعتی و نظامی.",
            "درمان مواجهه‌ای برای اضطراب و ترس.",
            "بازی و تجربهٔ سرگرمی تعاملی.",
        ],
        evolution="اصطلاح در دههٔ ۱۹۸۰ با کارهای آزمایشگاهی رواج یافت؛ رینگولد (۱۹۹۱) آن را عمومی کرد، استویر (۱۹۹۲) تعریف ارتباطی حضور را داد و از دههٔ ۲۰۱۰ با هدست‌های مصرفی، پژوهش رسانه‌ای و آموزش به‌طور گسترده به آن پرداخت.",
        key_concepts=[
            "حضور (Presence)",
            "غوطه‌وری (Immersion)",
            "زنده‌بودن (Vividness)",
            "تعامل‌پذیری (Interactivity)",
            "حضور از دور (Telepresence)",
        ],
        theorists="هاوارد رینگولد؛ جاناتان استویر",
        theorists_text="رینگولد (۱۹۹۱)؛ استویر (۱۹۹۲)",
        model="محرک حسی و پاسخ‌گویی → زنده‌بودن و تعامل‌پذیری → غوطه‌وری → احساس حضور → اثر ارتباطی.",
        studies=[
            "رینگولد (۱۹۹۱) تاریخ و وعدهٔ ارتباطی واقعیت مجازی را مستند کرد.",
            "استویر (۱۹۹۲) واقعیت مجازی را با دو بعد زنده‌بودن و تعامل‌پذیری تعریف کرد.",
        ],
        detailed_analysis="تحلیل عمیق نشان می‌دهد حضور، پدیده‌ای ادراکی است و نه ویژگی صرف دستگاه: کاربر ممکن است با نمایشگری ساده نیز احساس حضور کند، اگر روایت و پاسخ‌گویی تجربه را بسازد. در خبر غوطه‌ور، همین ویژگی پرسش اخلاقی مهمی می‌سازد: بازسازی صحنهٔ فاجعه می‌تواند همدلی بیافریند یا آسیب روانی را بازتولید کند. از این رو پژوهش معاصر، طراحی تجربه را با اخلاق مراقبت و سنجش پیامد ترکیب می‌کند.",
        critique_text="نقد اصلی آن است که چارچوب بر فناوری تمرکز دارد، بافت اجتماعی و نابرابری دسترسی را کم‌رنگ می‌کند و عوارض جسمی و روانی تجربهٔ طولانی را کمتر می‌سنجد.",
        example_text="دانشجوی پزشکی با هدست واقعیت مجازی عمل جراحی را تمرین می‌کند؛ غنای تصویر و پاسخ‌گویی ابزار به حرکت دست، حس حضور در اتاق عمل و یادگیری مهارت را ممکن می‌سازد.",
        year=1991,
    ),
    "MC-538": dict(
        summary="بازی‌های جدی و گیمیفیکیشن، چارچوبی برای به‌کارگیری منطق و عناصر بازی در زمینه‌های غیربازی است. بازی جدی، بازی‌ای است که هدف اصلی آن سرگرمی نیست، بلکه آموزش، سلامت، تغییر رفتار یا مشارکت مدنی است؛ این مفهوم را کلارک ابت در سال ۱۹۷۰ در کتابی با همین نام صورت‌بندی کرد. گیمیفیکیشن، که سباستین دتردینگ و همکارانش در سال ۲۰۱۱ آن را چنین تعریف کردند، استفاده از عناصر طراحی بازی در بافت‌های غیربازی است: امتیاز، نشان، جدول رده‌بندی، مأموریت و بازخورد فوری. تفاوت این دو در گستره است: بازی جدی یک بازی کامل با قواعد و هدف است، در حالی که گیمیفیکیشن فقط عناصری از بازی را به فعالیت موجود می‌افزاید. چارچوب بر سه نیاز روان‌شناختی خودمختاری، شایستگی و پیوند استوار است و توضیح می‌دهد چرا بازخورد فوری و پیشرفت قابل مشاهده، انگیزهٔ درونی می‌سازد. کاربرد آن در آموزش رسانه‌ای، اپلیکیشن‌های سلامت، مشارکت خبری و برنامه‌های وفاداری گسترده است. نقد اصلی به آن، خطر جایگزینی انگیزهٔ درونی با پاداش بیرونی، طراحی سطحی و نمایشی، امکان دستکاری رفتار و کم‌توجهی به عدالت در دسترسی است. یادآوری: متن کارت تحریریهٔ این مدخل با محتوای آن هم‌خوان نبود و مستندسازی حاضر بر پایهٔ منابع تأییدشده بازنویسی شده است.",
        definition="بازی‌های جدی، بازی‌هایی با هدف آموزشی یا کاربردی فراتر از سرگرمی‌اند و گیمیفیکیشن، کاربرد عناصر طراحی بازی در بافت‌های غیربازی برای افزایش انگیزه و مشارکت است.",
        main_problem="چگونه می‌توان از منطق بازی برای افزایش مشارکت و یادگیری در زمینه‌های جدی بهره گرفت، بدون آنکه انگیزهٔ درونی به پاداش بیرونی فروکاسته شود یا رفتار کاربر دستکاری گردد.",
        mechanism="عناصر بازی مانند هدف روشن، بازخورد فوری، پیشرفت قابل مشاهده و نشان اجتماعی، چرخهٔ تلاش و پاداش می‌سازند؛ این چرخه با نیازهای خودمختاری، شایستگی و پیوند پیوند می‌خورد و مشارکت پایدارتر می‌شود.",
        assumptions=[
            "عناصر بازی را می‌توان از بافت بازی جدا و منتقل کرد.",
            "بازخورد فوری و پیشرفت قابل مشاهده، انگیزه را افزایش می‌دهد.",
            "نیازهای روان‌شناختی خودمختاری، شایستگی و پیوند، پایهٔ انگیزه‌اند.",
            "بافت و طراحی، تعیین‌کنندهٔ اثر گیمیفیکیشن‌اند.",
        ],
        principles=[
            "گیمیفیکیشن افزودن عناصر بازی است، نه ساختن بازی کامل.",
            "بازی جدی، بازی کامل با هدفی فراتر از سرگرمی است.",
            "بازخورد و پیشرفت باید معنادار و متناسب با فعالیت باشد.",
            "طراحی باید انگیزهٔ درونی را تقویت کند، نه جایگزین آن شود.",
        ],
        critiques=[
            "پاداش بیرونی می‌تواند انگیزهٔ درونی را تضعیف کند.",
            "گیمیفیکیشن سطحی به نمایش و اندازه‌گیری بی‌معنا می‌انجامد.",
            "خطر دستکاری رفتار و سوءاستفادهٔ تجاری وجود دارد.",
            "طراحی نامتناسب، شکاف دسترسی و عدالت را تشدید می‌کند.",
        ],
        applications=[
            "آموزش سواد رسانه‌ای و مهارت‌های دیجیتال.",
            "اپلیکیشن‌های سلامت و پیگیری رفتار.",
            "مشارکت مخاطب در رسانه و پلتفرم‌های خبری.",
            "برنامه‌های وفاداری و آموزش سازمانی.",
        ],
        evolution="ابت (۱۹۷۰) مفهوم بازی جدی را معرفی کرد؛ پژوهش‌های بازی و یادگیری در دههٔ ۲۰۰۰ آن را بسط دادند؛ دتردینگ و همکاران (۲۰۱۱) گیمیفیکیشن را تعریف و از بازی جدی تفکیک کردند و مطالعهٔ ۲۰۱۴ شواهد تجربی اثر آن را مرور کرد.",
        key_concepts=[
            "بازی جدی (Serious Game)",
            "گیمیفیکیشن (Gamification)",
            "بازی‌گونگی (Gamefulness)",
            "انگیزهٔ درونی (Intrinsic Motivation)",
            "بازخورد فوری (Immediate Feedback)",
        ],
        theorists="کلارک ابت؛ سباستین دتردینگ؛ جوهامری",
        theorists_text="ابت (۱۹۷۰)؛ دتردینگ و همکاران (۲۰۱۱)؛ هاماری و همکاران (۲۰۱۴)",
        model="هدف غیربازی → افزودن عناصر بازی → چرخهٔ بازخورد و پیشرفت → ارضای نیازهای روان‌شناختی → مشارکت پایدار.",
        studies=[
            "دتردینگ و همکاران (۲۰۱۱) گیمیفیکیشن را استفاده از عناصر طراحی بازی در بافت غیربازی تعریف کردند.",
            "هاماری و همکاران (۲۰۱۴) اثر گیمیفیکیشن را در مطالعات تجربی مرور کردند و به وابستگی آن به بافت و طراحی رسیدند.",
        ],
        detailed_analysis="تحلیل عمیق نشان می‌دهد موفقیت گیمیفیکیشن به تناسب عنصر بازی با فعالیت بستگی دارد: نشان دادن پیشرفت در یادگیری معنادار است، اما امتیاز دادن به کلیک، رفتار نمایشی می‌سازد. در رسانه، گیمیفیکیشن می‌تواند مشارکت خبری را افزایش دهد، ولی اگر به سنجهٔ توجه پاداش دهد، کیفیت گفت‌وگو را تضعیف می‌کند. از این رو طراحی باید با هدف یادگیری یا مشارکت واقعی سنجیده شود، نه با شمار تعامل.",
        critique_text="نقد اصلی آن است که پاداش بیرونی می‌تواند انگیزهٔ درونی را تضعیف کند، گیمیفیکیشن سطحی به نمایش و اندازه‌گیری بی‌معنا می‌انجامد و خطر دستکاری رفتار وجود دارد.",
        example_text="یک دورهٔ آموزش خبرنگاری با نشان دادن پیشرفت مهارت‌ها و بازخورد فوری تمرین، یادگیری را جذاب می‌کند؛ اما اگر فقط تعداد کلیک را پاداش دهد، دانشجو را به رفتار سطحی سوق می‌دهد.",
        year=2011,
    ),
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


NAME_FIX = {}
YEAR_FIX = {
    "MC-499": "year corrected 1994 -> 2004 (verified anchor: Fombrun & van Riel, Fame and Fortune, 2004); note: editorial card core_logic was a mismatched template and documentation was rebuilt from verified literature",
    "MC-520": "no year change; note: editorial card core_logic was a mismatched platform template, documentation rebuilt from Rheingold (1991) and Steuer (1992)",
    "MC-538": "year corrected 2010 -> 2011 (verified anchor: Deterding et al., Defining Gamification, 2011); note: editorial card core_logic was a mismatched template and documentation was rebuilt from verified literature",
}


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
                                       "verified": n_verified, "batch": 122}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH122 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
