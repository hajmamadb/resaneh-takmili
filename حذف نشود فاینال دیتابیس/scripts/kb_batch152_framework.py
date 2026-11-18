# -*- coding: utf-8 -*-
"""Batch 152 (MODEL): MC-591 social-mediated crisis, MC-593 reputation, MC-594 internet dialogic PR, MC-595 social media PR."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch152-model-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch152_model.json"

S = {
    "MC-591": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="How Publics Respond to Crisis Communication Strategies: The Interplay of Information Form and Source",
             title_fa="واکنش عمومی‌ها به راهبردهای ارتباط بحران: درهم‌تنیدگی شکل و منبع اطلاعات",
             authors="Liu, B. F.; Austin, L.; Jin, Y.", year=2011,
             publisher="Public Relations Review",
             doi=None,
             url="https://www.sciencedirect.com/science/article/abs/pii/S0363811111000956",
             language="en", isbn=None,
             citation="Liu, B. F., Austin, L., & Jin, Y. (2011). How publics respond to crisis communication strategies: The interplay of information form and source. Public Relations Review, 37(4), 345-353.",
             locator="37(4):345-353", locator_type="page_range",
             supports="information form and source shape publics' crisis responses in social media", verified=True),
        dict(kind="BOOK_CHAPTER",
             title_en="Social-Mediated Crisis Communication Research",
             title_fa="پژوهش ارتباط بحران با میانجیگری رسانه‌های اجتماعی",
             authors="Jin, Y.", year=2022,
             publisher="Wiley (The Handbook of Crisis Communication)",
             doi="10.1002/9781119678953.ch11",
             url="https://onlinelibrary.wiley.com/doi/abs/10.1002/9781119678953.ch11",
             language="en", isbn=None,
             citation="Jin, Y. (2022). Social-mediated crisis communication research. In The Handbook of Crisis Communication (2nd ed.). Hoboken: Wiley.",
             locator="chapter 11", locator_type="chapter",
             supports="review of the social-mediated crisis communication model", verified=True),
    ],
    "MC-593": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Reputational Landscape",
             title_fa="چشم‌انداز شهرت",
             authors="Fombrun, C. J.; van Riel, C. B. M.", year=1997,
             publisher="Corporate Reputation Review",
             doi="10.1057/palgrave.crr.1540024",
             url="https://link.springer.com/article/10.1057/palgrave.crr.1540024",
             language="en", isbn=None,
             citation="Fombrun, C. J., & van Riel, C. B. M. (1997). The reputational landscape. Corporate Reputation Review, 1(1), 5-13.",
             locator="1(1):5-13", locator_type="page_range",
             supports="reputation as a collective representation held by multiple stakeholders", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Corporate Reputation: The Definitional Landscape",
             title_fa="شهرت شرکتی: چشم‌انداز تعریف‌ها",
             authors="Barnett, M. L.; Jermier, J. M.; Lafferty, B. A.", year=2006,
             publisher="Corporate Reputation Review",
             doi=None,
             url="https://www.mv.helsinki.fi/home/aula/Top20/corp-reputation-definitional-landscape.pdf",
             language="en", isbn=None,
             citation="Barnett, M. L., Jermier, J. M., & Lafferty, B. A. (2006). Corporate reputation: The definitional landscape. Corporate Reputation Review.",
             locator="article", locator_type="work",
             supports="systematic comparison of definitions of corporate reputation", verified=True),
    ],
    "MC-594": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Building Dialogic Relationships Through the World Wide Web",
             title_fa="ساختن روابط گفت‌وگویی از راه وب جهانی",
             authors="Kent, M. L.; Taylor, M.", year=1998,
             publisher="Public Relations Review",
             doi=None,
             url="https://www.sciencedirect.com/science/article/pii/S036381119980143X",
             language="en", isbn=None,
             citation="Kent, M. L., & Taylor, M. (1998). Building dialogic relationships through the World Wide Web. Public Relations Review, 24(3), 321-334.",
             locator="24(3):321-334", locator_type="page_range",
             supports="five dialogic principles for organizational websites", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Toward a Dialogic Theory of Public Relations",
             title_fa="به‌سوی نظریهٔ گفت‌وگویی روابط عمومی",
             authors="Kent, M. L.; Taylor, M.", year=2002,
             publisher="Public Relations Review",
             doi=None,
             url="https://www.sciencedirect.com/science/article/abs/pii/S036381110200108X",
             language="en", isbn=None,
             citation="Kent, M. L., & Taylor, M. (2002). Toward a dialogic theory of public relations. Public Relations Review, 28(1), 21-37.",
             locator="28(1):21-37", locator_type="page_range",
             supports="mutuality, propinquity, empathy, risk and commitment as dialogic tenets", verified=True),
    ],
    "MC-595": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="A Delphi Study of the Future of New Technology Research in Public Relations",
             title_fa="پژوهشی دلفی دربارهٔ آیندهٔ پژوهش فناوری‌های نو در روابط عمومی",
             authors="Kent, M. L.; Saffer, A. J.", year=2014,
             publisher="Public Relations Review",
             doi=None,
             url="http://mlkent.com/PDFs/Kent_Saffer_Delphi_2014B.pdf",
             language="en", isbn=None,
             citation="Kent, M. L., & Saffer, A. J. (2014). A Delphi study of the future of new technology research in public relations. Public Relations Review, 40(3), 568-576.",
             locator="40(3):568-576", locator_type="page_range",
             supports="expert consensus on technology's role in public relations research", verified=True),
        dict(kind="WEBSITE",
             title_en="A Delphi Study of the Future of New Technology Research in Public Relations (record)",
             title_fa="رکورد پژوهش دلفی دربارهٔ آیندهٔ پژوهش فناوری‌های نو",
             authors="University of Minnesota Experts", year=2014,
             publisher="University of Minnesota",
             doi=None,
             url="https://experts.umn.edu/en/publications/a-delphi-study-of-the-future-of-new-technology-research-in-public",
             language="en", isbn=None,
             citation="University of Minnesota Experts. (2014). Record for A Delphi study of the future of new technology research in public relations.",
             locator="record", locator_type="work",
             supports="independent bibliographic verification of the 2014 article", verified=True),
    ],
}

ENRICH = {
    "MC-591": dict(
        year=2011,
        summary="مدل ارتباطات بحران با میانجی‌گری رسانه‌های اجتماعی، که لیو، آستین و جین در سال ۲۰۱۱ صورت‌بندی کردند، توضیح می‌دهد که در بحران، مخاطبان دیگر تنها از رسانه‌های رسمی اطلاعات نمی‌گیرند، بلکه از شبکه‌های اجتماعی، وبگاه‌ها، دوستان و منابع غیررسمی نیز بهره می‌برند. بر پایهٔ این مدل، واکنش عمومی‌ها به بحران به سه عامل بستگی دارد: منشأ بحران، شکل اطلاعات و منبع اطلاعات. اطلاعاتی که از رسانهٔ اجتماعی می‌آید، به‌ویژه وقتی با تجربهٔ نزدیکان همراه شود، اعتبار و اثر بیشتری دارد. مدل سه گروه عمومی را از هم جدا می‌کند: عمومی‌هایی که مستقیماً از رسانهٔ اجتماعی استفاده می‌کنند، کسانی که با واسطهٔ دیگران اطلاعات را می‌گیرند، و کسانی که به رسانه‌های سنتی تکیه دارند. سازمان در بحران باید هم‌زمان در کانال‌های رسمی و اجتماعی حضور داشته باشد، اطلاعات را سریع و منسجم منتشر کند و به شایعه پاسخ دهد. این مدل توسعهٔ نظریهٔ ارتباط بحران وضعیتی برای محیط رسانه‌ای شبکه‌ای است. نقدهای اصلی به آن، دشواری سنجش منبع در محیط چندکانالی، سرعت تغییر بستر فناوری، کم‌توجهی به الگوریتم‌های انتشار و تفاوت مهارت دیجیتال مخاطبان را برجسته می‌کنند.",
        definition="مدل ارتباطات بحران با میانجی‌گری رسانه‌های اجتماعی می‌گوید واکنش عمومی‌ها به بحران از درهم‌تنیدگی منشأ بحران، شکل اطلاعات و منبع اطلاعات ساخته می‌شود و سازمان باید در کانال‌های رسمی و اجتماعی هم‌زمان حضور داشته باشد.",
        main_problem="در محیط رسانه‌ای شبکه‌ای، مخاطب بحران از کدام منابع اطلاعات می‌گیرد و ترکیب شکل و منبع اطلاعات چگونه واکنش او را به بحران و پاسخ سازمان شکل می‌دهد.",
        mechanism="مخاطب در بحران از منابع رسمی و اجتماعی اطلاعات می‌گیرد؛ اعتبار و اثر پیام به منشأ بحران، شکل اطلاعات و نزدیکی منبع به تجربهٔ او بستگی دارد و سازمان با حضور هم‌زمان در کانال‌ها روایت را مدیریت می‌کند.",
        assumptions=[
            "مخاطب بحران چندکانالی است.",
            "منبع اطلاعات بر اعتبار پیام اثر دارد.",
            "شکل اطلاعات بر پردازش اثر می‌گذارد.",
            "شبکه‌های اجتماعی سرعت انتشار را افزایش می‌دهند.",
            "سازمان باید در کانال‌های متعدد حاضر باشد.",
        ],
        principles=[
            "منشأ بحران را پیش از پیام روشن کن.",
            "اطلاعات رسمی و اجتماعی را هم‌سو کن.",
            "شایعه را سریع و مستند پاسخ بده.",
            "منبع پیام را شفاف اعلام کن.",
            "گروه‌های عمومی را جدا تحلیل کن.",
            "هماهنگی سخنگو را تضمین کن.",
        ],
        critiques=[
            "سنجش منبع در محیط چندکانالی دشوار است.",
            "بستر فناوری سریع تغییر می‌کند.",
            "الگوریتم‌های انتشار را کم‌بررسی می‌گذارد.",
            "مهارت دیجیتال مخاطبان را یکدست فرض می‌کند.",
            "اثر بلندمدت آن کم‌سنجیده مانده است.",
            "نقش رسانه‌های سنتی را کم‌رنگ می‌کند.",
            "سرعت واکنش سازمان را بر دقت اطلاعات مقدم می‌دارد.",
            "تفاوت گروه‌های سنی در استفاده از شبکه را نادیده می‌گیرد.",
        ],
        critique_text="منتقدان می‌گویند مدل ارتباط بحران با میانجی‌گری رسانه‌های اجتماعی چارچوب لازم برای محیط شبکه‌ای فراهم کرد اما سنجش منبع و نقش الگوریتم‌ها را کم‌بررسی گذاشت؛ با این حال، به چارچوب مرجع مدیریت بحران در رسانه‌های اجتماعی تبدیل شد.",
        applications=[
            "مدیریت بحران شبکه‌ای.",
            "پایش شایعه.",
            "آموزش سخنگوی دیجیتال.",
            "طراحی اتاق خبر بحران.",
            "ارزیابی پاسخ عمومی.",
            "پژوهش اعتماد رسانه‌ای.",
            "طراحی پاسخ چندکانالی.",
        ],
        example_text="در بحران یک محصول، ویدئوی مصرف‌کننده در شبکهٔ اجتماعی سریع‌تر از بیانیهٔ رسمی منتشر می‌شود؛ سازمانی که هم‌زمان در همان شبکه پاسخ می‌دهد و منبع اطلاعات را روشن می‌کند، روایت را بهتر در دست می‌گیرد.",
        evolution="پژوهش سال ۲۰۱۱ لیو، آستین و جین شواهد اولیهٔ مدل را فراهم کرد. مدل ارتباط بحران با میانجی‌گری رسانه‌های اجتماعی در پژوهش‌های بعدی به چارچوب مرجع محیط شبکه‌ای تبدیل شد.",
        key_concepts=["ارتباط بحران", "رسانهٔ اجتماعی", "شکل اطلاعات", "منبع اطلاعات", "عمومی‌های بحران", "شایعه"],
        theorists="بروک فیشر لیو، لوسینا آستین و یان جین.",
        theorists_text="مدل در سنت پژوهش ارتباط بحران و روابط عمومی دیجیتال شکل گرفت.",
        model="واکنش عمومی‌ها به بحران بر پایهٔ منشأ بحران، شکل اطلاعات و منبع اطلاعات، در محیطی که رسانه‌های رسمی و اجتماعی هم‌زمان حضور دارند.",
        studies=[
            "پژوهش سال ۲۰۱۱ واکنش عمومی‌ها را سنجید.",
            "مطالعات بعدی مدل را در بحران‌های سلامت آزمودند.",
            "پژوهش رسانهٔ اجتماعی، سرعت شایعه را بررسی کرد.",
            "مرور سال ۲۰۲۲ چارچوب را جمع‌بندی کرد.",
            "مطالعهٔ تطبیقی، تفاوت کشورها را بررسی کرد.",
        ],
    ),
    "MC-593": dict(
        year=1997,
        summary="مدل شهرت و اعتبار سازمانی، که چارلز فومبران و کِس فان ریل در سال ۱۹۹۷ صورت‌بندی کردند، شهرت را نه تصویر تبلیغاتی، بلکه بازنمایی جمعی و پایدار از سازمان در ذهن ذی‌نفعان می‌داند. در این مدل، شهرت از مجموع ادراک گروه‌های گوناگون نسبت به عملکرد گذشته و انتظار عملکرد آیندهٔ سازمان ساخته می‌شود. فومبران و فان ریل نشان دادند که شهرت مفهومی چندرشته‌ای است و اقتصاد، راهبرد، بازاریابی، جامعه‌شناسی و روان‌شناسی هر یک بخشی از آن را روشن می‌کنند. اعتبار، بُعد ارتباطی و پیامی شهرت است: باور مخاطب به درستی، شایستگی و حسن‌نیت سازمان در گفتار و کردار. شهرت خوب، هزینهٔ ارتباط را کاهش می‌دهد، در بحران سپر دفاعی می‌سازد و در بازار کار و سرمایه مزیت ایجاد می‌کند. مدل با شاخص‌هایی مانند کیفیت محصول، عملکرد مالی، مسئولیت اجتماعی و جذابیت محیط کار سنجیده شد و نشان داد که شهرت، سرمایه‌ای نامرئی است که در تصمیم‌های بازار و بحران بازدهی دارد. نقدهای اصلی به آن، تمرکز بر تصویر ذهنی به‌جای عملکرد واقعی، دشواری تفکیک شهرت از اعتبار، سوگیری پیمایش‌های ذی‌نفعان و کم‌توجهی به قدرت رسانه در ساخت شهرت را برجسته می‌کنند.",
        definition="مدل شهرت و اعتبار سازمانی، شهرت را بازنمایی جمعی و پایدار از عملکرد و انتظار سازمان در ذهن ذی‌نفعان می‌داند و اعتبار را بُعد ارتباطی آن، یعنی باور به درستی و شایستگی سازمان، تعریف می‌کند.",
        main_problem="شهرت سازمان چگونه از ادراک گروه‌های متعدد ذی‌نفع ساخته می‌شود، چه ابعادی دارد و اعتبار ارتباطی چگونه در برابر بحران از آن محافظت می‌کند.",
        mechanism="ذی‌نفعان بر پایهٔ تجربهٔ مستقیم، گزارش رسانه و گفت‌وگوی اجتماعی، ارزیابی‌هایی از عملکرد و انتظارات سازمان می‌سازند؛ این ارزیابی‌ها در زمان انباشته و به بازنمایی جمعی پایدار، یعنی شهرت، تبدیل می‌شوند.",
        assumptions=[
            "شهرت بازنمایی جمعی است.",
            "ذی‌نفعان متعدد و متفاوت‌اند.",
            "عملکرد گذشته شهرت می‌سازد.",
            "اعتبار بُعد ارتباطی شهرت است.",
            "شهرت در بحران سپر دفاعی می‌شود.",
        ],
        principles=[
            "شهرت را چندذی‌نفعی بسنج.",
            "عملکرد را از تصویر جدا کن.",
            "اعتبار را در پیام و کردار هم‌سو کن.",
            "بحران را با سابقهٔ شهرت مدیریت کن.",
            "شاخص‌های شهرت را مستند کن.",
            "گفت‌وگوی ذی‌نفعان را پیوسته نگه دار.",
        ],
        critiques=[
            "بر تصویر ذهنی به‌جای عملکرد تمرکز می‌کند.",
            "تفکیک شهرت از اعتبار دشوار است.",
            "پیمایش ذی‌نفعان سوگیری دارد.",
            "نقش قدرت رسانه را کم‌می‌شمارد.",
            "شهرت را بیش از حد پایدار فرض می‌کند.",
            "تفاوت فرهنگی در ارزیابی را کم‌بررسی می‌گذارد.",
            "شهرت را به‌سادگی به ارزش مالی فرو می‌کاهد.",
            "اعتبار رسانه‌ای را با اعتبار سازمانی یکی می‌گیرد.",
            "شهرت را بیشتر از عملکرد پایدار فرض می‌کند.",
            "نقش کارکنان در ساخت شهرت را کم‌بررسی می‌گذارد.",
            "سابقهٔ اخلاقی سازمان را کم‌وزن می‌کند.",
        ],
        critique_text="منتقدان می‌گویند مدل شهرت و اعتبار سازمانی چارچوبی چندرشته‌ای برای فهم شهرت فراهم کرد اما مرز شهرت و تصویر و اعتبار را مبهم گذاشت و نقش رسانه را کم‌بررسی کرد؛ با این حال، به چارچوب مرجع سنجش شهرت سازمانی تبدیل شد.",
        applications=[
            "سنجش شهرت سازمانی.",
            "مدیریت بحران اعتبار.",
            "ارتباطات سرمایه‌گذار.",
            "مسئولیت اجتماعی شرکت.",
            "آموزش روابط عمومی.",
            "پژوهش رفتار مصرف‌کننده.",
            "سنجش اعتماد سرمایه‌گذار.",
            "طراحی گزارش پایداری.",
        ],
        example_text="شرکتی که سال‌ها کیفیت پایدار و پاسخ‌گویی نشان داده است، در یک خطای تولیدی سریع‌تر باور عمومی را حفظ می‌کند؛ همان خطا برای سازمانی با سابقهٔ پنهان‌کاری به بحران شهرت تبدیل می‌شود.",
        evolution="مقالهٔ سال ۱۹۹۷ فومبران و فان ریل شهرت را به مفهومی چندرشته‌ای و سنجش‌پذیر تبدیل کرد. پژوهش‌های بعدی، شاخص‌های شهرت و پیوند آن با اعتبار و بحران را گستردند.",
        key_concepts=["شهرت سازمانی", "اعتبار", "بازنمایی جمعی", "ذی‌نفعان", "تصویر سازمانی", "سرمایهٔ شهرت"],
        theorists="چارلز فومبران و کِس فان ریل.",
        theorists_text="مدل در سنت پژوهش راهبردی و ارتباطات سازمانی شکل گرفت.",
        model="شهرت به‌عنوان بازنمایی جمعی پایدار از عملکرد سازمان و اعتبار به‌عنوان بُعد ارتباطی آن که در بحران سپر دفاعی می‌سازد.",
        studies=[
            "مقالهٔ سال ۱۹۹۷ شهرت را تعریف و دسته‌بندی کرد.",
            "پژوهش شاخص‌ها، ابعاد شهرت را سنجید.",
            "مطالعات بحران، پیوند شهرت و اعتبار را آزمودند.",
            "پژوهش سال ۲۰۰۶ تعریف‌ها را مقایسه کرد.",
            "مطالعهٔ بازار، ارزش مالی شهرت را سنجید.",
        ],
    ),
    "MC-594": dict(
        year=1998,
        summary="مدل اینترنت و روابط عمومی، که مایکل کنت و مورین تیلور در سال ۱۹۹۸ ارائه کردند، وب را نه تابلوی تبلیغات، بلکه فضایی برای گفت‌وگوی واقعی سازمان با مخاطبان می‌داند. آنان پنج اصل گفت‌وگویی برای وبگاه سازمانی صورت‌بندی کردند: حلقهٔ گفت‌وگو، یعنی امکان تعامل دوسویه و پاسخ؛ سودمندی اطلاعات برای همهٔ مخاطبان؛ ایجاد انگیزهٔ بازگشت؛ آسانی استفاده و رابط کاربری شهودی؛ و حفظ بازدیدکننده در وبگاه. این اصول، وبگاه را از آرشیو یک‌سویه به محیطی برای رابطه‌سازی تبدیل می‌کنند. مدل بر این باور است که فناوری به‌تنهایی گفت‌وگو نمی‌سازد و بدون اراده و ساختار سازمانی، وب تنها ابزار انتشار می‌ماند. پژوهش سال ۲۰۰۲ همان نویسندگان نظریهٔ گفت‌وگویی روابط عمومی را با اصول هم‌سویی، نزدیکی، همدلی، پذیرش خطر و تعهد تکمیل کرد. مدل در طراحی وبگاه، رسانه‌های اجتماعی، دولت الکترونیک و ارتباطات سلامت به کار می‌رود و نشان می‌دهد که فناوری، شرط لازم گفت‌وگوست، نه شرط کافی. نقدهای اصلی به آن، آرمانی‌بودن گفت‌وگوی سازمانی، سنجش دشوار حلقهٔ گفت‌وگو، کم‌توجهی به محدودیت منابع سازمان‌ها و تغییر سریع فناوری را برجسته می‌کنند.",
        definition="مدل اینترنت و روابط عمومی، وبگاه سازمانی را محیطی برای گفت‌وگوی دوسویه می‌داند و آن را با پنج اصل حلقهٔ گفت‌وگو، سودمندی اطلاعات، بازگشت، آسانی استفاده و حفظ بازدیدکننده می‌سنجد.",
        main_problem="فناوری وب چگونه می‌تواند ارتباط سازمان و مخاطب را از انتشار یک‌سویه به گفت‌وگوی دوسویه تبدیل کند و کدام اصول طراحی این گفت‌وگو را ممکن می‌سازد.",
        mechanism="وبگاه با فراهم‌کردن پاسخ دوسویه، اطلاعات سودمند، انگیزهٔ بازگشت، رابط آسان و حفظ بازدیدکننده، مخاطب را به مشارکت می‌کشاند و رابطهٔ سازمان و عمومی را از انتشار به گفت‌وگو می‌برد.",
        assumptions=[
            "وب فضای گفت‌وگوست، نه فقط انتشار.",
            "گفت‌وگو به ارادهٔ سازمانی نیاز دارد.",
            "پاسخ دوسویه رابطه می‌سازد.",
            "طراحی رابط بر مشارکت اثر دارد.",
            "اطلاعات سودمند مخاطب را نگه می‌دارد.",
        ],
        principles=[
            "حلقهٔ پاسخ دوسویه را بساز.",
            "اطلاعات را برای همهٔ مخاطبان سودمند کن.",
            "انگیزهٔ بازگشت را فراهم کن.",
            "رابط را ساده و شهودی نگه دار.",
            "بازدیدکننده را در وبگاه نگه دار.",
            "گفت‌وگو را با ساختار سازمانی پشتیبانی کن.",
        ],
        critiques=[
            "گفت‌وگوی سازمانی را آرمانی فرض می‌کند.",
            "سنجش حلقهٔ گفت‌وگو دشوار است.",
            "محدودیت منابع سازمان را کم‌می‌شمارد.",
            "فناوری سریع تغییر می‌کند.",
            "نقش قدرت در گفت‌وگو را کم‌بررسی می‌گذارد.",
            "کاربرد آن در سازمان‌های کوچک محدود است.",
            "گفت‌وگو را به فناوری وب فرو می‌کاهد.",
            "سنجش اثر طراحی را ساده فرض می‌کند.",
            "تغییر نسلی کاربران وب را در تحلیل نادیده می‌گیرد.",
            "نقش سازمان‌های واسط را کم‌می‌شمارد.",
            "رابط‌های چندزبانه و دسترس‌پذیر را کم‌بررسی می‌گذارد.",
            "اثر اعتماد پیشین مخاطب را نادیده می‌گیرد.",
        ],
        critique_text="منتقدان می‌گویند مدل اینترنت و روابط عمومی چارچوبی روشن برای گفت‌وگومحورکردن وب داد اما گفت‌وگوی واقعی را آسان‌تر از عمل فرض کرد و محدودیت منابع را کم‌بررسی گذاشت؛ با این حال، پایهٔ نظریهٔ گفت‌وگویی روابط عمومی دیجیتال است.",
        applications=[
            "طراحی وبگاه سازمانی.",
            "ارزیابی گفت‌وگوی دیجیتال.",
            "دولت الکترونیک.",
            "ارتباطات سلامت.",
            "آموزش روابط عمومی.",
            "طراحی رسانهٔ اجتماعی.",
            "آموزش سواد دیجیتال سازمانی.",
            "ارزیابی وبگاه بخش عمومی.",
        ],
        example_text="وبگاهی که فقط بیانیه و گزارش منتشر می‌کند، وبگاه اطلاع‌رسانی است؛ وبگاهی که پرسش مخاطب را در همان صفحه پاسخ می‌دهد، امکان بازخورد و پیگیری می‌دهد و اطلاعات را برای گروه‌های مختلف بازنویسی می‌کند، به گفت‌وگو نزدیک‌تر است.",
        evolution="مقالهٔ سال ۱۹۹۸ کنت و تیلور پنج اصل گفت‌وگویی وب را معرفی کرد و پژوهش روابط عمومی دیجیتال را پایه گذاشت. نظریهٔ گفت‌وگویی سال ۲۰۰۲ و پژوهش‌های بعدی، آن را به رسانه‌های اجتماعی گستردند.",
        key_concepts=["گفت‌وگو", "حلقهٔ گفت‌وگو", "وبگاه سازمانی", "رابط کاربری", "حفظ بازدیدکننده", "روابط عمومی دیجیتال"],
        theorists="مایکل کنت و مورین تیلور.",
        theorists_text="مدل در سنت پژوهش روابط عمومی گفت‌وگومحور و ارتباطات دیجیتال شکل گرفت.",
        model="وبگاه سازمانی به‌عنوان فضای گفت‌وگوی دوسویه که با پنج اصل طراحی، رابطهٔ سازمان و مخاطب را می‌سازد.",
        studies=[
            "مقالهٔ سال ۱۹۹۸ پنج اصل را معرفی کرد.",
            "نظریهٔ سال ۲۰۰۲ اصول گفت‌وگو را تکمیل کرد.",
            "مطالعات وبگاه، اصول را در عمل سنجیدند.",
            "پژوهش دیجیتال، مدل را به شبکه‌های اجتماعی برد.",
            "مطالعهٔ دولت، وبگاه‌های عمومی را ارزیابی کرد.",
        ],
    ),
    "MC-595": dict(
        year=2014,
        summary="مدل رسانه‌های اجتماعی و روابط عمومی، که مایکل کنت و آدام سفر در سال ۲۰۱۴ با پژوهش دلفی صورت‌بندی کردند، رسانه‌های اجتماعی را نه کانال تبلیغ اضافه، بلکه محیطی برای بازآرایی رابطهٔ سازمان و مخاطب می‌داند. در این مدل، فناوری‌های نو سه تغییر بنیادی می‌سازند: مخاطب از دریافت‌کننده به مشارکت‌کننده تبدیل می‌شود؛ سازمان ناچار است پاسخ‌گو و شفاف باشد؛ و مرز میان ارتباط رسمی و گفت‌وگوی عمومی کم‌رنگ می‌شود. پژوهش دلفی با نظر خبرگان نشان داد که آیندهٔ پژوهش فناوری در روابط عمومی باید بر تعامل، اعتماد، اخلاق و سنجش اثر متمرکز شود، نه فقط بر ابزارها. مدل همچنین تأکید کرد که رسانهٔ اجتماعی بدون راهبرد گفت‌وگویی، تنها سرعت انتشار می‌افزاید و می‌تواند بحران را تشدید کند. کاربردهای آن در مدیریت ارتباط با مشتری، بحران، کمپین سلامت و ارتباطات عمومی دیده می‌شود و نشان می‌دهد که اعتماد در این محیط، محصول پاسخ‌گویی روزمره است، نه بیانیهٔ بحران. نقدهای اصلی به آن، تمرکز بر اجماع خبرگان به‌جای شواهد میدانی، تعمیم از نمونهٔ محدود، کم‌توجهی به شکاف دیجیتال، اثر الگوریتم‌ها و سرعت زوال بسترهای فناوری را برجسته می‌کنند.",
        definition="مدل رسانه‌های اجتماعی و روابط عمومی، رسانهٔ اجتماعی را محیطی برای گفت‌وگوی مشارکتی می‌داند که مخاطب را به مشارکت‌کننده تبدیل می‌کند و سازمان را ناچار به شفافیت، پاسخ‌گویی و سنجش اثر می‌سازد.",
        main_problem="رسانه‌های اجتماعی چه تغییری در رابطهٔ سازمان و مخاطب می‌سازند و پژوهش و راهبرد روابط عمومی باید چه اولویت‌هایی را در این محیط دنبال کند.",
        mechanism="رسانهٔ اجتماعی مانع انتشار را برمی‌دارد، مخاطب را به مشارکت‌کننده تبدیل می‌کند و پاسخ‌گویی را اجباری می‌سازد؛ سازمانی که گفت‌وگو و شفافیت را در راهبرد بگنجاند، اعتماد می‌سازد و سازمانی که فقط انتشار می‌افزاید، بحران را سریع‌تر می‌کند.",
        assumptions=[
            "مخاطب رسانهٔ اجتماعی مشارکت‌کننده است.",
            "شفافیت در این محیط اجباری است.",
            "ابزار بدون راهبرد اثر پایدار ندارد.",
            "اعتماد و اخلاق محور پژوهش‌اند.",
            "مرز رسمی و عمومی کم‌رنگ می‌شود.",
        ],
        principles=[
            "راهبرد گفت‌وگو را پیش از ابزار بساز.",
            "پاسخ‌گویی را در ساختار سازمان بگنجان.",
            "اعتماد را با شفافیت حفظ کن.",
            "اثر را با شاخص بسنج.",
            "اخلاق انتشار را رعایت کن.",
            "شکاف دیجیتال را در برنامه ببین.",
        ],
        critiques=[
            "بر اجماع خبرگان به‌جای شواهد میدانی تکیه دارد.",
            "از نمونهٔ محدود تعمیم می‌دهد.",
            "شکاف دیجیتال را کم‌بررسی می‌گذارد.",
            "اثر الگوریتم‌ها را نادیده می‌گیرد.",
            "بسترهای فناوری سریع زوال می‌یابند.",
            "سنجش اثر بلندمدت را ساده فرض می‌کند.",
            "پاسخ‌گویی را بیش از حد به حضور آنلاین فرو می‌کاهد.",
            "ساختار مالکیت پلتفرم‌ها را کم‌بررسی می‌گذارد.",
            "اخلاق داده و حریم خصوصی را کم‌می‌سنجد.",
            "تأثیر الگوریتم بر دیده‌شدن پیام را ساده فرض می‌کند.",
            "نابرابری دسترسی سازمان‌ها به تیم دیجیتال را نادیده می‌گیرد.",
        ],
        critique_text="منتقدان می‌گویند مدل رسانه‌های اجتماعی و روابط عمومی جهت‌گیری پژوهشی روشنی داد اما بر اجماع خبرگان تکیه کرد و اثر الگوریتم و شکاف دیجیتال را کم‌بررسی گذاشت؛ با این حال، بحث روابط عمومی دیجیتال را از ابزارمحوری به رابطه‌محوری برد.",
        applications=[
            "طراحی راهبرد رسانهٔ اجتماعی.",
            "مدیریت بحران دیجیتال.",
            "ارتباط با مشتری.",
            "کمپین سلامت.",
            "آموزش روابط عمومی.",
            "پژوهش فناوری ارتباطات.",
            "طراحی شاخص تعامل.",
            "ارزیابی اعتماد آنلاین.",
        ],
        example_text="سازمانی که در شبکهٔ اجتماعی فقط اطلاعیه منتشر می‌کند و به پرسش‌ها پاسخ نمی‌دهد، حضور دارد اما گفت‌وگو ندارد؛ همان سازمان با پاسخ‌گویی، شفافیت در خطا و سنجش بازخورد، اعتماد می‌سازد.",
        evolution="پژوهش دلفی سال ۲۰۱۴ کنت و سفر اولویت‌های پژوهش فناوری در روابط عمومی را جمع‌بندی کرد. پژوهش‌های بعدی، تعامل، اخلاق و سنجش اثر را در رسانه‌های اجتماعی گستردند.",
        key_concepts=["رسانهٔ اجتماعی", "گفت‌وگوی دیجیتال", "شفافیت", "پاسخ‌گویی", "اعتماد", "سنجش اثر"],
        theorists="مایکل کنت و آدام سفر.",
        theorists_text="مدل در سنت پژوهش روابط عمومی دیجیتال و فناوری ارتباطات شکل گرفت.",
        model="رسانهٔ اجتماعی به‌عنوان محیط مشارکت که سازمان را به شفافیت، پاسخ‌گویی و سنجش اثر وامی‌دارد و ابزار بدون راهبرد گفت‌وگو را بی‌اثر می‌داند.",
        studies=[
            "پژوهش دلفی سال ۲۰۱۴ اولویت‌ها را جمع‌بندی کرد.",
            "مطالعات بعدی تعامل و اعتماد را سنجیدند.",
            "پژوهش بحران، نقش شبکه را بررسی کرد.",
            "مطالعات اخلاق، مرز تبلیغ و گفت‌وگو را کاویدند.",
            "پژوهش پلتفرم، ساختار مالکیت را تحلیل کرد.",
        ],
    ),
}

NAME_FIX = {}
YEAR_FIX = {
    "MC-593": "سال ۱۹۹۴ در کارت با مقالهٔ سال ۱۹۹۷ فومبران و فان ریل هم‌خوان نبود؛ سال انتشار مستند ثبت شد.",
    "MC-591": "ترتیب نام نویسندگان در کارت جابه‌جا و نام خانوادگی ناقص بود؛ انتساب مستند به لیو، آستین و جین ثبت شد.",
    "MC-595": "نام «سِگریت» در کارت با نام خانوادگی مستند سفر هم‌خوان نبود؛ انتساب درست ثبت شد.",
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
                                       "verified": n_verified, "batch": 152}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH152 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
