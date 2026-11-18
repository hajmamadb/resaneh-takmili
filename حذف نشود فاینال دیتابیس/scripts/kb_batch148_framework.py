# -*- coding: utf-8 -*-
"""Batch 148 (MODEL): MC-545 Ruesch & Bateson, MC-546 Thayer, MC-547 Wright, MC-548 Carey."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch148-model-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch148_model.json"

S = {
    "MC-545": [
        dict(kind="BOOK",
             title_en="Communication: The Social Matrix of Psychiatry",
             title_fa="ارتباط: بافت اجتماعی روان‌پزشکی",
             authors="Ruesch, J.; Bateson, G.", year=1951,
             publisher="W. W. Norton",
             doi=None,
             url="https://archive.org/details/communicationsoc00inrues",
             language="en", isbn=None,
             citation="Ruesch, J., & Bateson, G. (1951). Communication: The Social Matrix of Psychiatry. New York: W. W. Norton.",
             locator="book", locator_type="SECTION",
             supports="communication as a circular social process with levels of message", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Review of Communication: The Social Matrix of Psychiatry",
             title_fa="مروری بر ارتباط: بافت اجتماعی روان‌پزشکی",
             authors="Hinkle, G. J.", year=1951,
             publisher="The Annals of the American Academy of Political and Social Science",
             doi="10.1177/000271625127800158",
             url="https://journals.sagepub.com/doi/10.1177/000271625127800158",
             language="en", isbn=None,
             citation="Hinkle, G. J. (1951). Review of Communication: The Social Matrix of Psychiatry. The Annals of the American Academy of Political and Social Science, 278(1).",
             locator="278(1)", locator_type="ISSUE",
             supports="contemporary scholarly reception of the communication framework", verified=True),
    ],
    "MC-546": [
        dict(kind="BOOK",
             title_en="Communication and Communication Systems",
             title_fa="ارتباط و نظام‌های ارتباطی",
             authors="Thayer, L.", year=1968,
             publisher="Richard D. Irwin",
             doi=None,
             url="https://search.gesis.org/publication/gesis-bib-90579?lang=en",
             language="en", isbn=None,
             citation="Thayer, L. (1968). Communication and Communication Systems. Homewood, IL: Richard D. Irwin.",
             locator="book", locator_type="SECTION",
             supports="meaning allocation and communication as a systemic process", verified=True),
        dict(kind="WEBSITE",
             title_en="GESIS record for Communication and Communication Systems",
             title_fa="رکورد کتاب‌شناختی ارتباط و نظام‌های ارتباطی",
             authors="GESIS Leibniz Institute", year=1968,
             publisher="GESIS",
             doi=None,
             url="https://search.gesis.org/publication/gesis-bib-90579?lang=en",
             language="en", isbn=None,
             citation="GESIS Leibniz Institute for the Social Sciences. (n.d.). Bibliographic record for Communication and Communication Systems (L. Thayer, 1968).",
             locator="record", locator_type="work",
             supports="bibliographic verification of the 1968 edition", verified=True),
    ],
    "MC-547": [
        dict(kind="BOOK",
             title_en="Mass Communication: A Sociological Perspective",
             title_fa="ارتباط جمعی: چشم‌اندازی جامعه‌شناختی",
             authors="Wright, C. R.", year=1959,
             publisher="Random House",
             doi=None,
             url="https://books.google.com/books/about/Mass_Communication.html?id=-cNoAAAAIAAJ",
             language="en", isbn=None,
             citation="Wright, C. R. (1959). Mass Communication: A Sociological Perspective. New York: Random House.",
             locator="book", locator_type="SECTION",
             supports="structural-functional analysis and four functions of mass communication", verified=True),
        dict(kind="WEBSITE",
             title_en="Charles R. Wright, Communications",
             title_fa="چارلز رایت، ارتباطات",
             authors="Almanac, University of Pennsylvania", year=2017,
             publisher="University of Pennsylvania",
             doi=None,
             url="https://almanac.upenn.edu/articles/charles-r.-wright-communications",
             language="en", isbn=None,
             citation="University of Pennsylvania Almanac. (2017). Charles R. Wright, Communications. Almanac, University of Pennsylvania.",
             locator="web page", locator_type="work",
             supports="biographical confirmation of the 1959 functionalist book", verified=True),
    ],
    "MC-548": [
        dict(kind="BOOK_CHAPTER",
             title_en="A Cultural Approach to Communication",
             title_fa="رهیافتی فرهنگی به ارتباط",
             authors="Carey, J. W.", year=1989,
             publisher="Unwin Hyman (Communication as Culture)",
             doi=None,
             url="https://web.mit.edu/21l.432/www/readings/Carey_CulturalApproachCommunication.pdf",
             language="en", isbn=None,
             citation="Carey, J. W. (1989). A cultural approach to communication. In Communication as Culture: Essays on Media and Society. Boston: Unwin Hyman.",
             locator="chapter", locator_type="SECTION",
             supports="contrast between transmission and ritual views of communication", verified=True),
        dict(kind="WEBSITE",
             title_en="Ritual View of Communication",
             title_fa="دیدگاه آیینی ارتباط",
             authors="EBSCO Research Starters", year=None,
             publisher="EBSCO",
             doi=None,
             url="https://www.ebsco.com/research-starters/communication-and-mass-media/ritual-view-communication",
             language="en", isbn=None,
             citation="EBSCO Research Starters. (n.d.). Ritual view of communication. EBSCO.",
             locator="web page", locator_type="work",
             supports="definition and attribution of the ritual view to Carey", verified=True),
    ],
}

ENRICH = {
    "MC-545": dict(
        year=1951,
        summary="مدل روش و بیتسون، که یورگن روش و گرگوری بیتسون در کتاب سال ۱۹۵۱ با عنوان ارتباط: بافت اجتماعی روان‌پزشکی ارائه کردند، ارتباط را نه انتقال یک‌طرفهٔ اطلاعات، بلکه فرایندی دایره‌ای می‌داند که در یک بافت اجتماعی رخ می‌دهد. آن‌ها ارتباط را به سطوح گوناگون تقسیم کردند: ارتباط درون‌فردی، میان‌فردی، گروهی و فرهنگی. در هر سطح، پیام‌ها افزون بر محتوا، سطح دیگری نیز دارند؛ یعنی همان گزاره‌ای که گفته می‌شود، در قالبی ارتباطی درمی‌آید و می‌تواند دربارهٔ خودِ ارتباط نیز حرف بزند. روش و بیتسون این لایهٔ دوم را فراتر از محتوا در نظر گرفتند و نشان دادند که اختلال در همین سطح فراتر می‌تواند به سوءتفاهم و آسیب روانی بیانجامد. آن‌ها ارتباط را در بافت روابط انسانی و نهادهای اجتماعی جای دادند و کوشیدند روان‌پزشکی را با نظریهٔ ارتباط پیوند دهند. این اثر بر مکتب ارتباطی پالو آلتوی کالیفرنیا و مفهوم پیام دوگانه اثر گذاشت. نقدهای اصلی به مدل، ابهام سطوح ارتباطی، دشواری سنجش تجربی، تمرکز بر آسیب‌شناسی و کم‌توجهی به بستر اقتصادی و سیاسی را برجسته می‌کنند.",
        definition="مدل روش و بیتسون، ارتباط را فرایندی دایره‌ای در بافت اجتماعی می‌داند که در سطوح گوناگون جریان دارد و هر پیام افزون بر محتوا، لایه‌ای دربارهٔ خود ارتباط نیز حمل می‌کند.",
        main_problem="ارتباط انسانی چگونه در بافت اجتماعی و در سطوح چندگانه رخ می‌دهد و اختلال در لایه‌های فراتر از محتوا چه پیامدهایی برای فهم و سلامت روان دارد.",
        mechanism="پیام‌ها در بافتی از روابط اجتماعی مبادله می‌شوند؛ هر پیام هم محتوا دارد و هم قالبی که دربارهٔ ارتباط حرف می‌زند؛ بازخورد دایره‌ای، این سطوح را به هم پیوند می‌دهد و اختلال در یک سطح بر سطوح دیگر اثر می‌گذارد.",
        assumptions=[
            "ارتباط فرایندی دایره‌ای است.",
            "پیام در بافت اجتماعی معنا می‌یابد.",
            "پیام‌ها سطوح چندگانه دارند.",
            "قالب پیام نیز پیام است.",
            "اختلال ارتباطی به آسیب روانی می‌انجامد.",
        ],
        principles=[
            "بافت اجتماعی ارتباط را در تحلیل بگنجان.",
            "سطح محتوا را از سطح ارتباط تفکیک کن.",
            "بازخورد دایره‌ای را دنبال کن.",
            "پیام را در رابطهٔ دو طرف بخوان.",
            "اختلال ارتباط را در چند سطح بسنج.",
            "نهادهای اجتماعی را در مدل لحاظ کن.",
            "فراارتباط را در تحلیل مکالمه ثبت کن.",
            "روابط نهادی را در بافت ارتباط بگنجان.",
        ],
        critiques=[
            "سطوح ارتباطی را مبهم تعریف می‌کند.",
            "سنجش تجربی مفاهیم دشوار است.",
            "بر آسیب‌شناسی متمرکز می‌شود.",
            "بستر اقتصادی و سیاسی را کم‌می‌شمارد.",
            "تعمیم آن به ارتباط جمعی روشن نیست.",
            "نقش فرهنگ را در سطوح ارتباط روشن نمی‌کند.",
            "مفاهیم را برای پژوهش میدانی عملیاتی نمی‌کند.",
        ],
        critique_text="منتقدان می‌گویند مدل روش و بیتسون پیوند ارتباط و روابط انسانی را پیش برد اما سطوح آن مبهم ماند و سنجش تجربی سخت شد؛ با این حال، پایهٔ مکتب تعاملی ارتباط و پژوهش پیام دوگانه است.",
        applications=[
            "تحلیل ارتباط درمانی.",
            "آموزش مهارت‌های ارتباط بین‌فردی.",
            "مطالعهٔ سوءتفاهم در خانواده.",
            "پژوهش ارتباط سازمانی.",
            "تحلیل پیام در مشاوره.",
            "آموزش ارتباط به درمانگران.",
        ],
        example_text="پدری که به فرزندش می‌گوید هر وقت خواستی حرف بزنی، در همان حال ساعت را نگاه می‌کند؛ محتوای جمله دعوت به گفت‌وگوست، اما قالب رفتاری می‌گوید وقت ندارم. فرزند به لایهٔ دوم واکنش می‌دهد، نه به محتوا.",
        evolution="کتاب سال ۱۹۵۱ روش و بیتسون چارچوب تعاملی ارتباط را معرفی کرد و بر مکتب پالو آلتوی کالیفرنیا اثر گذاشت. پژوهش‌های بعدی، سطوح ارتباط را به تحلیل خانواده، سازمان و رسانه گستردند.",
        key_concepts=["بافت اجتماعی", "سطوح ارتباط", "فراارتباط", "بازخورد", "پیام دوگانه", "روابط انسانی"],
        theorists="یورگن روش و گرگوری بیتسون.",
        theorists_text="مدل در سنت روان‌پزشکی اجتماعی و نظریهٔ تعاملی ارتباط شکل گرفت.",
        model="شبکه‌های ارتباطی دایره‌ای در بافت اجتماعی که پیام را در سطوح محتوا و فراتر از محتوا جریان می‌دهند.",
        studies=[
            "کتاب سال ۱۹۵۱ چارچوب تعاملی را معرفی کرد.",
            "مکتب پالو آلتوی کالیفرنیا، مدل را گسترد.",
            "پژوهش خانواده، پیام دوگانه را تحلیل کرد.",
            "مطالعات سازمانی، سطوح ارتباط را به کار گرفتند.",
            "پژوهش مکالمه، فراارتباط را مستند کرد.",
            "مطالعات نهاد، بافت اجتماعی را سنجیدند.",
            "پژوهش سلامت، سطوح ارتباط را در درمان سنجید.",
        ],
    ),
    "MC-546": dict(
        year=1968,
        summary="مدل تخصیص معنا، که لی تایر در کتاب سال ۱۹۶۸ با عنوان ارتباط و نظام‌های ارتباطی صورت‌بندی کرد، ارتباط را نه انتقال معنا از فرستنده به گیرنده، بلکه خلق و بازخلق معنا در میان انسان‌ها می‌داند. تایر استدلال کرد که معنا در پیام جای ندارد؛ پیام تنها نشانه‌هایی است که هر طرف بر پایهٔ تجربه، نظام مفهومی و موقعیت خود به آن معنا می‌دهد. از این رو، ارتباط فرایندی فعال است که در آن گیرنده معنا را تخصیص می‌دهد و فرستنده نیز معنای خود را از واکنش طرف مقابل بازمی‌سازد. تایر ارتباط را در چارچوب نظام‌ها تحلیل کرد و نشان داد که سازمان‌ها و روابط انسانی، نظام‌هایی از انتظارات و معانی مشترک می‌سازند. او ارتباط را شیوه‌ای از بودن و زیستن در کنار دیگران می‌دانست، نه ابزاری خنثی برای جابه‌جایی اطلاعات. این نگرش به نظریه‌های تفسیری سازمان، رویکردهای ساختگرا و پژوهش ارتباط سازمانی راه یافت. نقدهای اصلی به مدل، نسبی‌گرایی بیش‌ازحد در معنا، دشواری سنجش تخصیص معنا، کم‌توجهی به عدم تقارن قدرت و ابهام مرز میان ارتباط و فرهنگ را برجسته می‌کنند.",
        definition="مدل تخصیص معنا، معنا را نه درون پیام، بلکه محصول تخصیص فعال گیرنده و بازخلق مشترک دو طرف در بستر نظام‌های ارتباطی و سازمانی می‌داند.",
        main_problem="اگر معنا در پیام نیست، ارتباط چگونه ممکن می‌شود و انسان‌ها در نظام‌های سازمانی چگونه معنای مشترک می‌سازند و بازمی‌سازند.",
        mechanism="فرستنده نشانه‌هایی می‌فرستد؛ گیرنده بر پایهٔ تجربه و نظام مفهومی خود به نشانه‌ها معنا تخصیص می‌دهد؛ واکنش او به فرستنده بازمی‌گردد و چرخهٔ خلق و بازخلق معنا ادامه می‌یابد.",
        assumptions=[
            "معنا در پیام جای ندارد.",
            "گیرنده معنا را تخصیص می‌دهد.",
            "تجربه و نظام مفهومی، معنا را می‌سازد.",
            "ارتباط در نظام‌های اجتماعی رخ می‌دهد.",
            "ارتباط شیوه‌ای از بودن است.",
        ],
        principles=[
            "معنا را از پیام جدا تحلیل کن.",
            "تجربهٔ گیرنده را در تفسیر بگنجان.",
            "نظام انتظارات سازمانی را بررسی کن.",
            "بازخورد را بخشی از خلق معنا بدان.",
            "ارتباط را فرایند مستمر ببین.",
            "عدم تقارن قدرت را در معنا بسنج.",
            "نظام مفهومی گیرنده را بازسازی کن.",
            "معنای مشترک را در عمل بسنج.",
            "زمینهٔ سازمانی پیام را مستند کن.",
            "بازخورد را در چرخهٔ معنا ثبت کن.",
        ],
        critiques=[
            "به نسبی‌گرایی در معنا می‌انجامد.",
            "سنجش تخصیص معنا دشوار است.",
            "عدم تقارن قدرت را کم‌می‌شمارد.",
            "مرز ارتباط و فرهنگ را روشن نمی‌کند.",
            "کاربرد عملی آن در سیاست‌گذاری محدود است.",
            "معیار فهم مشترک را ارائه نمی‌دهد.",
            "به فردگرایی تفسیری می‌گراید.",
            "نقش رسانه را در تخصیص معنا کم می‌بیند.",
            "معنای مشترک را به تعامل فردی فرو می‌کاهد.",
        ],
        critique_text="منتقدان می‌گویند مدل تخصیص معنا نقش فعال گیرنده را به‌درستی برجسته کرد اما با نسبی‌گرایی، امکان فهم مشترک و سنجش تجربی را دشوار ساخت؛ با این حال، پایهٔ رویکردهای تفسیری ارتباط سازمانی است.",
        applications=[
            "تحلیل ارتباط سازمانی.",
            "آموزش مهارت شنیدن فعال.",
            "پژوهش سوءتفاهم میان‌فرهنگی.",
            "طراحی پیام سازمانی.",
            "مطالعهٔ فرهنگ سازمانی.",
            "طراحی پیام تغییر رفتار.",
            "آموزش رهبری ارتباطی.",
            "مطالعهٔ رضایت شغلی.",
        ],
        example_text="در جلسه‌ای، مدیر می‌گوید این طرح باید بازنگری شود. یکی از کارکنان آن را فرصت بهبود می‌فهمد و دیگری آن را نشانهٔ نارضایتی؛ پیام یکسان است، اما معنا در تجربه و جایگاه هر یک تخصیص می‌یابد.",
        evolution="کتاب سال ۱۹۶۸ تایر مدل تخصیص معنا را در چارچوب نظام‌های ارتباطی معرفی کرد و بر نظریه‌های تفسیری سازمان اثر گذاشت. پژوهش‌های بعدی، آن را با رویکردهای فرهنگی و انتقادی ترکیب کردند.",
        key_concepts=["تخصیص معنا", "بازخلق معنا", "نظام ارتباطی", "تجربهٔ گیرنده", "فرهنگ سازمانی", "بازخورد"],
        theorists="لی تایر.",
        theorists_text="مدل در سنت نظام‌گرایی و رویکرد تفسیری به ارتباط سازمانی شکل گرفت.",
        model="چرخهٔ خلق و بازخلق معنا در نظام‌های ارتباطی؛ پیام فقط نشانه است و معنا در تجربهٔ دو طرف تخصیص می‌یابد.",
        studies=[
            "کتاب سال ۱۹۶۸ مدل را صورت‌بندی کرد.",
            "پژوهش سازمانی، نظام معانی را تحلیل کرد.",
            "مطالعات میان‌فرهنگی، سوءتفاهم را سنجید.",
            "پژوهش تفسیری، بازخلق معنا را گسترد.",
            "پژوهش جلسه، تخصیص معنا را تحلیل کرد.",
            "مطالعات رهبری، بازخلق معنا را سنجیدند.",
            "پژوهش مشتری، تخصیص معنا را در خدمت سنجید.",
        ],
    ),
    "MC-547": dict(
        year=1959,
        summary="مدل ساختاری–کارکردی ارتباط جمعی، که چارلز رایت در کتاب سال ۱۹۵۹ با عنوان ارتباط جمعی: چشم‌اندازی جامعه‌شناختی ارائه کرد، تحلیل کارکردی را به مطالعهٔ رسانه‌های جمعی گسترد. رایت بر پایهٔ سنت ساختاری–کارکردی، رسانه را نهادی در نظام اجتماعی می‌داند که برای بقا و تعادل نظام، کارکردهایی انجام می‌دهد. او چهار کارکرد اصلی را برمی‌شمارد: اطلاع و هشدار دربارهٔ رویدادهای محیط، همبستگی و تفسیر اطلاعات برای هدایت واکنش جمعی، انتقال فرهنگ و میراث اجتماعی به نسل‌های بعد، و سرگرمی برای آسایش و پرکردن اوقات فراغت. رایت تأکید کرد که این کارکردها را باید همراه با پرسش‌های دیگر سنجید: برای چه کسی، با چه پیامدی و در چه شرایطی. به همین دلیل، از کارکردهای آشکار و پنهان و از کژکارکردها نیز سخن گفت؛ مثلاً اطلاع‌رسانی می‌تواند به اضطراب جمعی بینجامد یا سرگرمی می‌تواند مشارکت اجتماعی را تضعیف کند. این مدل چارچوبی برای تحلیل سیاست رسانه و ارزیابی پیامدهای اجتماعی فراهم کرد. نقدهای اصلی به آن، محافظه‌کاری کارکردگرایی، فرض تعادل نظام، کم‌توجهی به قدرت و تغییر اجتماعی و دشواری تفکیک کارکرد از کژکارکرد را برجسته می‌کنند.",
        definition="مدل ساختاری–کارکردی ارتباط جمعی، رسانه را نهادی در نظام اجتماعی می‌داند که چهار کارکرد اطلاع و هشدار، همبستگی، انتقال فرهنگ و سرگرمی را برای بقا و تعادل نظام انجام می‌دهد.",
        main_problem="رسانه‌های جمعی چه کارکردهایی برای نظام اجتماعی انجام می‌دهند، این کارکردها برای چه کسانی و با چه پیامدهایی همراه‌اند و چگونه می‌توان آشکار و پنهان آن‌ها را از هم شناخت.",
        mechanism="رسانه به‌عنوان نهاد، اطلاعات محیط را گردآوری و تفسیر می‌کند، فرهنگ را منتقل می‌سازد و سرگرمی فراهم می‌کند؛ این کارکردها تعادل نظام را حفظ می‌کنند اما می‌توانند کژکارکرد نیز داشته باشند.",
        assumptions=[
            "رسانه نهادی در نظام اجتماعی است.",
            "نظام اجتماعی به تعادل گرایش دارد.",
            "رسانه چهار کارکرد اصلی دارد.",
            "کارکردها آشکار و پنهان‌اند.",
            "هر کارکرد می‌تواند کژکارکرد داشته باشد.",
        ],
        principles=[
            "کارکرد را با پرسش برای چه کسی بسنج.",
            "کارکرد آشکار را از پنهان جدا کن.",
            "کژکارکردها را در تحلیل بگنجان.",
            "چهار کارکرد را جداگانه بررسی کن.",
            "نقش رسانه در تعادل نظام را بسنج.",
            "پیامدهای اجتماعی را مستند کن.",
            "کارکرد رسانه را با مخاطب بسنج.",
            "کژکارکرد خبر را مستند کن.",
        ],
        critiques=[
            "محافظه‌کاری کارکردگرایی را بازتولید می‌کند.",
            "تعادل نظام را مفروض می‌گیرد.",
            "قدرت و تغییر اجتماعی را کم‌می‌شمارد.",
            "تفکیک کارکرد از کژکارکرد دشوار است.",
            "نقش مخاطب فعال را نادیده می‌گیرد.",
            "مخاطب را منفعل فرض می‌گیرد.",
            "تحول رسانهٔ دیجیتال را در مدل نمی‌گنجاند.",
        ],
        critique_text="منتقدان می‌گویند مدل رایت تحلیل کارکردی رسانه را نظام‌مند کرد اما با فرض تعادل، نقش قدرت و تغییر اجتماعی را کم‌رنگ ساخت؛ با این حال، چارچوبی پایه برای سیاست رسانه و ارزیابی پیامدها فراهم آورد.",
        applications=[
            "تحلیل سیاست رسانه.",
            "ارزیابی پیامدهای اجتماعی خبر.",
            "برنامه‌ریزی رسانهٔ عمومی.",
            "آموزش جامعه‌شناسی رسانه.",
            "مطالعهٔ سرگرمی و مشارکت.",
            "ارزیابی عملکرد رسانهٔ محلی.",
            "تحلیل کارکرد تبلیغ عمومی.",
        ],
        example_text="پخش خبری دربارهٔ بحران آب، کارکرد اطلاع و هشدار را انجام می‌دهد؛ اگر گزارش با تفسیر مسئولان همراه شود، کارکرد همبستگی فعال می‌شود و اگر فقط اضطراب بیازاید، کژکارکرد آشکار می‌شود.",
        evolution="کتاب سال ۱۹۵۹ رایت چارچوب ساختاری–کارکردی رسانه را تثبیت کرد و به مرجع تحلیل کارکردهای ارتباط جمعی تبدیل شد. پژوهش‌های بعدی، نقد قدرت و مخاطب فعال را به آن افزودند.",
        key_concepts=["کارکرد", "کژکارکرد", "کارکرد آشکار", "کارکرد پنهان", "انتقال فرهنگ", "همبستگی"],
        theorists="چارلز رایت.",
        theorists_text="مدل در سنت ساختاری–کارکردی جامعه‌شناسی رسانه شکل گرفت.",
        model="چهار کارکرد اطلاع و هشدار، همبستگی، انتقال فرهنگ و سرگرمی که رسانه به‌عنوان نهاد برای تعادل نظام انجام می‌دهد.",
        studies=[
            "کتاب سال ۱۹۵۹ چهار کارکرد را تثبیت کرد.",
            "پژوهش رسانه، کژکارکرد خبر را سنجید.",
            "مطالعات فرهنگی، انتقال فرهنگ را نقد کرد.",
            "پژوهش سیاست، کارکرد رسانهٔ عمومی را تحلیل کرد.",
            "پژوهش مخاطب، کارکرد سرگرمی را سنجید.",
            "مطالعات سیاست، انتقال فرهنگ را نقد کرد.",
            "پژوهش بحران، کژکارکرد هشدار را تحلیل کرد.",
            "مطالعهٔ سرگرمی، کژکارکرد مشارکت را بررسی کرد.",
        ],
    ),
    "MC-548": dict(
        year=1989,
        summary="مدل انتقالی در برابر آیینی، که جیمز کری در کتاب سال ۱۹۸۹ با عنوان ارتباط به‌عنوان فرهنگ صورت‌بندی کرد، دو فهم رقیب از ارتباط را از هم جدا می‌کند. در دیدگاه انتقالی، ارتباط فرایندی است که در آن پیام‌ها برای کنترل و نفوذ بر دیگران در فضا منتقل می‌شوند؛ این دیدگاه بر انتقال اطلاعات، سرعت و دقت تأکید دارد و ریشه در تلگراف و ارتباط از راه دور دارد. در دیدگاه آیینی، ارتباط نه انتقال اطلاعات، بلکه مشارکت در یک فرهنگ مشترک و بازنمایی تجربهٔ مشترک است؛ هدف آن حفظ جامعه در زمان و ساختن معنای مشترک است، نه صرفاً انتقال پیام در مکان. کری استدلال کرد که دیدگاه انتقالی در پژوهش رسانهٔ آمریکایی غالب شده و بخشی از تجربهٔ ارتباطی را پنهان می‌کند. او خوانش خبر را نمونه‌ای از دیدگاه آیینی دانست: خبر نه فقط اطلاع‌رسانی، بلکه آیینی است که جهان را بازنمایی و نظم اجتماعی را بازتولید می‌کند. این تمایز به چارچوبی بنیادین در مطالعات فرهنگی رسانه تبدیل شد. نقدهای اصلی به آن، دوگانه‌سازی افراطی دو دیدگاه، کم‌توجهی به پیوندشان، ابهام روش تجربی و آرمانی‌کردن فرهنگ مشترک را برجسته می‌کنند.",
        definition="مدل انتقالی در برابر آیینی، دو فهم رقیب از ارتباط را نشان می‌دهد: انتقال پیام برای کنترل در فضا، در برابر مشارکت در فرهنگ مشترک و بازتولید معنا در زمان.",
        main_problem="پژوهش رسانه چگونه تحت سلطهٔ دیدگاه انتقالی قرار گرفت و چه بخشی از تجربهٔ ارتباطی با جایگزین‌کردن دیدگاه آیینی روشن می‌شود.",
        mechanism="در دیدگاه انتقالی، پیام از فرستنده به گیرنده در فضا جریان می‌یابد و هدف کنترل و نفوذ است؛ در دیدگاه آیینی، ارتباط بازنمایی تجربهٔ مشترک و مشارکت در فرهنگ است و نظم اجتماعی را در زمان حفظ می‌کند.",
        assumptions=[
            "دو فهم رقیب از ارتباط وجود دارد.",
            "دیدگاه انتقالی بر پژوهش غالب شده است.",
            "ارتباط آیینی فرهنگ را بازتولید می‌کند.",
            "خبر نمونه‌ای از ارتباط آیینی است.",
            "معنای مشترک، هستهٔ جامعه است.",
        ],
        principles=[
            "دیدگاه نظری پژوهش را آشکار کن.",
            "انتقال را از مشارکت فرهنگی جدا کن.",
            "خبر را به‌عنوان آیین بخوان.",
            "بازتولید نظم اجتماعی را بسنج.",
            "زمان و مکان را در تحلیل بگنجان.",
            "دو دیدگاه را مکمل ببین، نه مطلق.",
            "آیین رسانه‌ای را در زمینهٔ تاریخی بخوان.",
            "معنای مشترک را با شواهد مستند کن.",
        ],
        critiques=[
            "دو دیدگاه را بیش از اندازه دوگانه می‌کند.",
            "پیوند انتقال و آیین را کم‌بررسی می‌گذارد.",
            "روش تجربی آن مبهم است.",
            "فرهنگ مشترک را آرمانی می‌کند.",
            "نابرابری قدرت در آیین را کم‌می‌شمارد.",
            "به فرهنگ‌گرایی افراطی می‌گراید.",
            "نقش قدرت در آیین را روشن نمی‌کند.",
        ],
        critique_text="منتقدان می‌گویند مدل کری افق فرهنگی پژوهش رسانه را گشود اما با دوگانه‌سازی انتقال و آیین، پیوندشان را نادیده گرفت و روش تجربی روشنی پیشنهاد نکرد؛ با این حال، چارچوب پایهٔ مطالعات فرهنگی رسانه است.",
        applications=[
            "تحلیل فرهنگی خبر.",
            "پژوهش آیین رسانه‌ای.",
            "نقد رویکرد انتقالی در ارتباطات.",
            "مطالعهٔ هویت و رسانه.",
            "آموزش مطالعات فرهنگی.",
            "تحلیل آیین خبری تلویزیون.",
        ],
        example_text="تماشای مشترک یک برنامهٔ خبری در خانهٔ خانواده، تنها دریافت اطلاعات نیست؛ آیینی است که خانواده را در تجربه‌ای مشترک و در نظمی نمادین جای می‌دهد، حتی اگر اطلاعات برنامه تازه نباشد.",
        evolution="کتاب سال ۱۹۸۹ کری تمایز انتقال و آیین را تثبیت کرد و به یکی از چارچوب‌های مرجع مطالعات فرهنگی رسانه تبدیل شد. پژوهش‌های بعدی، آن را در رسانه‌های دیجیتال و آیین‌های آنلاین به کار گرفتند.",
        key_concepts=["دیدگاه انتقالی", "دیدگاه آیینی", "فرهنگ مشترک", "بازنمایی", "آیین رسانه‌ای", "بازتولید نظم"],
        theorists="جیمز کری.",
        theorists_text="مدل در سنت مطالعات فرهنگی و جامعه‌شناسی رسانه شکل گرفت.",
        model="تمایز دو فهم ارتباط: انتقال پیام برای کنترل در فضا، در برابر مشارکت آیینی در فرهنگ مشترک و بازتولید نظم اجتماعی.",
        studies=[
            "کتاب سال ۱۹۸۹ تمایز را تثبیت کرد.",
            "مطالعات فرهنگی، خبر را آیین خواند.",
            "پژوهش هویت، فرهنگ مشترک را تحلیل کرد.",
            "مطالعات دیجیتال، آیین آنلاین را بررسی کرد.",
            "پژوهش مخاطب، آیین تماشا را سنجید.",
            "مطالعات خبر، بازنمایی نظم را تحلیل کرد.",
        ],
    ),
}

NAME_FIX = {
    "MC-545": ("مدل روش و بیتسون", "Ruesch and Bateson Model", "عنوان پیشین «راس و بیتسون» و «Ross» نادرست بود؛ نام خانوادگی یورگن روش (Jürgen Ruesch) اصلاح شد."),
}
YEAR_FIX = {
    "MC-546": "متن theorists کارت «لی ثیر» نوشته شده بود که نگارش نادرست نام لی تایر است؛ سال ۱۹۶۸ با نخستین چاپ کتاب هم‌خوان است.",
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
                                       "verified": n_verified, "batch": 148}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH148 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
