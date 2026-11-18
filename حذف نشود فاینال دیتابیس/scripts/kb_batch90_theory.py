# -*- coding: utf-8 -*-
"""Batch 90: full documentation for MC-487, MC-488, MC-491, MC-492."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch90-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch90_theory.json"

S = {
    "MC-487": [
        dict(kind="BOOK",
             title_en="Textual Poachers: Television Fans and Participatory Culture",
             title_fa="شکارچیان متن: هواداران تلویزیون و فرهنگ مشارکتی",
             authors="Jenkins, H.", year=1992, publisher="Routledge",
             doi="10.4324/9780203114339",
             url="https://www.taylorfrancis.com/books/mono/10.4324/9780203114339/textual-poachers-henry-jenkins",
             language="en", isbn=None,
             citation="Jenkins, H. (1992). Textual poachers: Television fans and participatory culture. Routledge. https://doi.org/10.4324/9780203114339",
             locator="work", locator_type="work",
             supports="textual poaching / fandom as participatory culture / fan production", verified=True),
        dict(kind="BOOK_CHAPTER",
             title_en="The Cultural Economy of Fandom",
             title_fa="اقتصاد فرهنگی هواداری",
             authors="Fiske, J.", year=1992, publisher="Routledge",
             doi=None, url=None, language="en", isbn=None,
             citation="Fiske, J. (1992). The cultural economy of fandom. In L. A. Lewis (Ed.), The adoring audience: Fan culture and popular media (pp. 30-49). Routledge.",
             locator="pp. 30-49", locator_type="page_range",
             supports="fandom as productivity / popular cultural economy", verified=False),
    ],
    "MC-488": [
        dict(kind="BOOK",
             title_en="Discovering the News: A Social History of American Newspapers",
             title_fa="کشف خبر: تاریخ اجتماعی روزنامه‌های آمریکایی",
             authors="Schudson, M.", year=1978, publisher="Basic Books",
             doi=None, url="https://www.basicbooks.com/titles/michael-schudson/discovering-the-news/9780465016662/",
             language="en", isbn="9780465016662",
             citation="Schudson, M. (1978). Discovering the news: A social history of American newspapers. Basic Books.",
             locator="work", locator_type="work",
             supports="objectivity as historical norm / information vs story / news as cultural form", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Objectivity as Strategic Ritual: An Examination of Newsmen's Notions of Objectivity",
             title_fa="عینیت به‌عنوان آیین راهبردی: بررسی تلقی خبرنگاران از عینیت",
             authors="Tuchman, G.", year=1972, publisher="American Journal of Sociology",
             doi=None, url=None, language="en", isbn=None,
             citation="Tuchman, G. (1972). Objectivity as strategic ritual: An examination of newsmen's notions of objectivity. American Journal of Sociology, 77(4), 660-679.",
             locator="77(4):660-679", locator_type="page_range",
             supports="objectivity procedures as ritual protection against criticism", verified=False),
    ],
    "MC-491": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Cascading Activation: Contesting the White House's Frame After 9/11",
             title_fa="فعال‌سازی آبشاری: نبرد بر سر چارچوب کاخ سفید پس از ۱۱ سپتامبر",
             authors="Entman, R. M.", year=2003, publisher="Political Communication",
             doi="10.1080/10584600390244176", url=None, language="en", isbn=None,
             citation="Entman, R. M. (2003). Cascading activation: Contesting the White House's frame after 9/11. Political Communication, 20(4), 415-432. https://doi.org/10.1080/10584600390244176",
             locator="20(4):415-432", locator_type="page_range",
             supports="cascading activation / cultural congruence / network activation", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Framing: Toward Clarification of a Fractured Paradigm",
             title_fa="چارچوب‌بندی: به سوی روشن‌سازی یک پارادایم چندپاره",
             authors="Entman, R. M.", year=1993, publisher="Journal of Communication",
             doi=None, url=None, language="en", isbn=None,
             citation="Entman, R. M. (1993). Framing: Toward clarification of a fractured paradigm. Journal of Communication, 43(4), 51-58.",
             locator="43(4):51-58", locator_type="page_range",
             supports="selection and salience / definition of framing", verified=False),
    ],
    "MC-492": [
        dict(kind="BOOK",
             title_en="Excellence in Public Relations and Communication Management",
             title_fa="تعالی در روابط عمومی و مدیریت ارتباطات",
             authors="Grunig, J. E. (Ed.)", year=1992, publisher="Lawrence Erlbaum",
             doi="10.4324/9780203812303",
             url="https://www.taylorfrancis.com/books/edit/10.4324/9780203812303/excellence-public-relations-communication-management-james-grunig",
             language="en", isbn="9780805802276",
             citation="Grunig, J. E. (Ed.). (1992). Excellence in public relations and communication management. Lawrence Erlbaum. https://doi.org/10.4324/9780203812303",
             locator="work", locator_type="work",
             supports="excellence project / symmetrical two-way model / PR as management function", verified=True),
        dict(kind="BOOK",
             title_en="Managing Public Relations",
             title_fa="مدیریت روابط عمومی",
             authors="Grunig, J. E.; Hunt, T.", year=1984, publisher="Holt, Rinehart and Winston",
             doi=None, url=None, language="en", isbn=None,
             citation="Grunig, J. E., & Hunt, T. (1984). Managing public relations. Holt, Rinehart and Winston.",
             locator="work", locator_type="work",
             supports="four models of public relations / definition of PR as communication management", verified=False),
    ],
}

ENRICH = {
    "MC-487": {
        "summary": "(جنکینز، ۱۹۹۲) جنکینز در «شکارچیان متن» کلیشه هوادار وسواسی و منفعل را رد کرد و فندوم را فرهنگ مشارکتی خواند: هوادار متن محبوب را «می‌رباید»، بازخوانی می‌کند و با نوشتن داستان، ساختن ویدئو، طراحی و انتشار فن‌زین آن را گسترش می‌دهد. او با وام‌گیری مفهوم شکار متن از دو سرتو، نشان داد که خواندن هوادارانه، شکل خاصی از تولید معنایا است. فندوم هم‌زمان جامعه تفسیری، شبکه توزیع غیررسمی و فضای اجتماعی است؛ از این رو هوادار نه مصرف‌کننده منفعل، بلکه تولیدکننده فرهنگی است.",
        "definition": "فرهنگ هواداران، مجموعه رویه‌های مشترک خواندن، بازنویسی، تولید و توزیع است که در آن طرفداران متن محبوب را از مرزهای اثر اصلی فراتر می‌برند و جامعه‌ای تفسیری و تولیدی می‌سازند؛ جامعه‌ای که هم درون صنعت فرهنگ جای دارد و هم در برابر منطق آن مقاومت می‌کند.",
        "main_problem": "مسئله این است که هوادار مصرف‌کننده منفعل صنعت فرهنگ است یا تولیدکننده معنا؛ و رابطه هواداری با مصرف کالایی چگونه است. جنکینز پاسخ می‌دهد که هوادار هم‌زمان مصرف‌کننده و تولیدکننده است: او مواد فرهنگی صنعت را می‌گیرد و با بازنویسی، آن را به معنایی تازه بدل می‌کند. پرسش دوم، مسئله قدرت است: تا چه حد این تولید مردمی می‌تواند در برابر جذب تجاری و کنترل حقوقی مقاومت کند.",
        "mechanism": "۱. شکار متن: هوادار متن را آن‌گونه که هست نمی‌پذیرد؛ آن را برمی‌دارد و از زاویه دلخواه خود بازخوانی می‌کند؛ خواندن، شکلی از تصاحب است.\n۲. بازنویسی و گسترش روایت: داستان هواداری، شخصیت‌های حاشیه‌ای را محور می‌کند، پایان‌های ممکن را می‌آزماید و شکاف‌های روایت اصلی را پر می‌کند.\n۳. تولید چندرسانه‌ای: ویدئوی هواداری، فن‌آرت، موسیقی و ویرایش، متن را به زبان رسانه‌های دیگر ترجمه می‌کند و مهارت‌های تازه‌ای می‌سازد.\n۴. جامعه تفسیری و توزیع غیررسمی: فن‌زین و شبکه‌های مبادله، معیارهای اعتبار و سلیقه را درون جامعه شکل می‌دهند و از بازار رسمی عبور می‌کنند.\n۵. فضای جنسیت‌شده و امن: بخش مهمی از فندوم‌های اولیه، فضایی برای زنان و گروه‌های حاشیه‌ای بود تا روایت‌هایی بسازند که رسانه اصلی نمی‌ساخت.\n۶. تنش مقاومت و ادغام: صنعت از خلاقیت هواداران بهره می‌برد و آن را جذب می‌کند، اما هواداران نیز مرزهای مالکیت و وفاداری را به چالش می‌کشند؛ نتیجه، مذاکره‌ای پیوسته است.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا فندوم‌ها موتور گسترش روایت‌های تلویزیونی و بازی‌های ویدئویی‌اند، چرا پلتفرم‌ها محتوای کاربرساخته را تشویق می‌کنند و چرا تنش بر سر حقوق و بازنشر ادامه دارد. نکته مهم این است که فندوم، هم خلاقیت جمعی است و هم بخشی از زنجیره ارزش صنعت؛ تحلیل بدون توجه به هر دو وجه ناقص است.",
        "assumptions": [
            "هوادار خواننده‌ای فعال است و متن را بازتفسیر و بازنویسی می‌کند.",
            "فندوم، جامعه‌ای تفسیری با معیارهای مشترک است.",
            "مصرف فرهنگی می‌تواند هم‌زمان شکل مقاومت و مشارکت در بازار باشد.",
        ],
        "principles": [
            "خواندن هوادارانه، شکلی از تولید معنا است.",
            "تولید مردمی هم‌زمان درون و بیرون منطق صنعت فرهنگ قرار دارد.",
            "فضای هواداری می‌تواند روایت‌های حاشیه‌ای را ممکن کند.",
        ],
        "critiques": [
            "۱. نمونه‌گزینی: فندوم‌های پرصدای غربی و تلویزیونی نماینده همه هواداران نیستند.\n۲. رمانتیک‌سازی مقاومت: خلاقیت هوادار می‌تواند ارزش اقتصادی صنعت را افزایش دهد و مقاومت را به کالا بدل کند.\n۳. نابرابری دسترسی: مهارت، زمان و فناوری لازم برای تولید، میان هواداران یکسان نیست.\n۴. تحول بستر: تحلیل بر فن‌زین و ویدئوی آنالوگ متمرکز است و منطق پلتفرم و الگوریتم را در نظر ندارد.\n۵. ابهام مرز: تفکیک هوادار از مصرف‌کننده عادی و تولیدکننده حرفه‌ای در عمل روشن نیست.",
        ],
        "applications": [
            "تحلیل فندوم: بررسی تولید هواداری و مناسبات آن با صنعت رسانه.",
            "استراتژی محتوای پلتفرم: طراحی زمینه مشارکت هواداران و مدیریت حقوق.",
            "سواد رسانه‌ای: آموزش خوانش خلاقانه و آگاهانه متن و تولید مسئولانه.",
            "مطالعات جنسیت: تحلیل فضای هواداری به‌عنوان عرصه بازنویسی هنجارها.",
        ],
        "evolution": "جنکینز مفهوم را در ۱۹۹۲ بر پایه مردم‌نگاری فندوم‌های تلویزیونی صورت‌بندی کرد و در «فرهنگ همگرایی» (۲۰۰۶) و «رسانه‌های پخش‌پذیر» (۲۰۱۳) آن را به فرهنگ مشارکتی دیجیتال گسترد.",
        "key_concepts": [
            "شکار متن (Textual Poaching)",
            "فرهنگ مشارکتی (Participatory Culture)",
            "داستان هواداری (Fan Fiction)",
            "وید هواداری (Fan Vid)",
            "فن‌زین (Fanzine)",
            "جامعه تفسیری (Interpretive Community)",
        ],
        "studies": [
            "Jenkins, H. (1992). Textual poachers: Television fans and participatory culture. Routledge.",
            "Fiske, J. (1992). The cultural economy of fandom. In The adoring audience (pp. 30-49). Routledge.",
        ],
        "theorists": "هنری جنکینز (۱۹۹۲)",
        "theorists_text": "هنری جنکینز (۱۹۹۲)",
        "year": 1992,
        "model": "مدل سه‌لایه: شکار و بازخوانی متن → تولید و بازنویسی (داستان، ویدئو، فن‌زین) → جامعه تفسیری و توزیع غیررسمی؛ با تنش پیوسته مقاومت و ادغام تجاری.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nجنکینز در برابر دو روایت ایستاد: روایت صنعتی که هوادار را مصرف‌کننده وسواسی می‌دید و روایت انتقادی که او را قربانی فریب صنعت فرهنگ می‌دانست. تحلیل مردم‌نگارانه او نشان داد که فندوم، فضایی برای تولید معنا، مهارت و اجتماع است؛ ایده‌ای که پایه نظریه فرهنگ مشارکتی شد.\n\n۲. منطق سنجش و دام‌های آن\nسنجش فندوم نیازمند مشاهده رویه‌های تولید، تحلیل آثار و مصاحبه با اعضاست. پژوهش‌هایی که تنها حجم محتوای هواداری را می‌شمارند، کیفیت تفسیر و روابط اجتماعی را از دست می‌دهند؛ و پژوهش‌هایی که تنها نمونه‌های حرفه‌ای‌شده را می‌بینند، تنوع فندوم را کم‌نمایی می‌کنند.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در نشان دادن عاملیت فرهنگی هوادار است؛ اما باید با تحلیل اقتصاد پلتفرم و کار رایگان تکمیل شود. خلاقیت هوادار در محیطی رخ می‌دهد که مالکیت، دیده‌شدن و داده را پلتفرم‌ها تعیین می‌کنند.",
        "critique_text": "\n".join([
            "۱. نمونه‌گزینی: فندوم‌های پرصدای غربی و تلویزیونی نماینده همه هواداران نیستند.",
            "۲. رمانتیک‌سازی مقاومت: خلاقیت هوادار می‌تواند ارزش اقتصادی صنعت را افزایش دهد و مقاومت را به کالا بدل کند.",
            "۳. نابرابری دسترسی: مهارت، زمان و فناوری لازم برای تولید میان هواداران یکسان نیست.",
            "۴. تحول بستر: تحلیل بر فن‌زین و ویدئوی آنالوگ متمرکز است و منطق پلتفرم را در نظر ندارد.",
            "۵. ابهام مرز: تفکیک هوادار از مصرف‌کننده عادی و تولیدکننده حرفه‌ای روشن نیست.",
        ]),
        "example_text": "جامعه‌ای از طرفداران یک سریال، داستان شخصیت فرعی را می‌نویسند، ویدئوی تدوینی می‌سازند و در یک آرشیو جمعی منتشر می‌کنند. سازندگان سریال از این محتوا برای تبلیغ استفاده می‌کنند، اما وقتی ویدئوها از مرز مجاز عبور کنند، درخواست حذف می‌فرستند؛ همین رفت‌وبرگشت، نمونه روشن تنش مقاومت و ادغام است.",
    },
    "MC-488": {
        "summary": "(شادسون، ۱۹۷۸) شادسون نشان داد که عینیت، ویژگی طبیعی خبر نیست، بلکه هنجاری تاریخی و برساخته است. او در تاریخ مطبوعات آمریکا چرخش از الگوی «داستان» به الگوی «اطلاعات» را در مطبوعات پنی قرن نوزدهم نشان داد و سپس توضیح داد که چگونه بحران اعتماد دهه ۱۹۲۰ — تبلیغات جنگ، رشد روابط عمومی و شک به «واقعیت‌های ساده» — آرمان عینیت را به‌عنوان راه دفاعی روزنامه‌نگاران در برابر شک پدید آورد. خبر در این تحلیل، آینه واقعیت نیست؛ شکلی از فرهنگ است.",
        "definition": "عینیت‌گرایی خبر، مجموعه هنجارها و رویه‌هایی است که روزنامه‌نگاران برای جدا کردن گزارش از نظر، ارجاع به منابع و ارائه دیدگاه‌های رقیب به کار می‌برند؛ هنجاری تاریخی که در پاسخ به بحران اعتماد شکل گرفت و امروز بخشی از هویت حرفه‌ای خبر است.",
        "main_problem": "مسئله این است که چرا عینیت به هنجار مسلط خبر بدل شد و آیا خبر می‌تواند آینه بی‌واسطه واقعیت باشد. شادسون پاسخ می‌دهد که عینیت از دل شک زاده شد: وقتی معلوم شد واقعیت‌ها نیز از صافی منافع و تبلیغات می‌گذرند، روزنامه‌نگاران به رویه‌هایی روی آوردند که گزارش را از نظر جدا کند. پرسش دوم، محدودیت است: آیا این رویه‌ها می‌توانند سوگیری ساختاری انتخاب و چارچوب‌بندی را جبران کنند.",
        "mechanism": "۱. گذار از داستان به اطلاعات: مطبوعات پنی، خبر را از روایت ادبی و حزبی به گزاره اطلاعاتی و بازارپسند چرخاندند؛ این چرخش، پیش‌شرط ظهور هنجار عینیت بود.\n۲. بحران اعتماد دهه ۱۹۲۰: تبلیغات جنگ و رشد روابط عمومی نشان داد که «واقعیت» نیز قابل ساخت است؛ اعتماد به گزارش ساده فرو ریخت.\n۳. عینیت به‌عنوان راه دفاعی: روزنامه‌نگاران با جدا کردن خبر از نظر، نقل قول مستقیم و ارجاع به منبع، در برابر اتهام سوگیری سپر ساختند.\n۴. رویه‌های عینیت: توازن دیدگاه‌ها، تفکیک گزارش از تفسیر و استناد به منبع رسمی، معیارهای عملی حرفه شدند.\n۵. خبر به‌عنوان شکل فرهنگی: انتخاب رویداد، تعیین اهمیت و ترتیب ارائه، خبر را به محصولی فرهنگی بدل می‌کند، نه بازتاب خنثی جهان.\n۶. عینیت به‌عنوان آیین راهبردی: رویه‌های عینیت بیش از آنکه بی‌طرفی را تضمین کنند، اعتبار حرفه‌ای و دفاع در برابر نقد را تأمین می‌کنند.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا «بی‌طرفی» در خبر به معیار اعتبار بدل شد، چرا رسانه‌ها به منبع رسمی تکیه می‌کنند و چرا در محیط دیجیتال، بحث از عینیت به شفافیت و «عینیت سردبیری» تغییر کرده است. نکته مهم این است که عینیت، نبود موضع نیست؛ مجموعه‌ای از رویه‌ها برای مدیریت موضع است.",
        "assumptions": [
            "هنجارهای خبری محصول تاریخ‌اند، نه ویژگی طبیعی.",
            "رویه‌های عینیت می‌توانند سوگیری فردی را کاهش دهند.",
            "خبر، شکلی از فرهنگ است و نه بازتاب خنثی واقعیت.",
        ],
        "principles": [
            "عینیت از بحران اعتماد زاده شد، نه از خنثی‌بودن واقعیت.",
            "تفکیک گزارش از نظر، راهبرد دفاعی حرفه‌ای است.",
            "انتخاب و چارچوب‌بندی، حتی در گزارش بی‌طرف، حضور دارند.",
        ],
        "critiques": [
            "۱. تمرکز آمریکایی: تاریخ روایت‌شده به مطبوعات آمریکا محدود است.\n۲. فرض امکان بی‌طرفی: عینیت می‌تواند سوگیری ساختاری را پنهان کند و به «هر دو طرف» یکسان وزن دهد.\n۳. کم‌توجهی به مالکیت: نقش منافع تجاری و سیاسی در شکل‌گیری هنجارها کمتر تحلیل می‌شود.\n۴. عینیت به‌عنوان پوشش: رویه‌های عینیت می‌توانند دیدگاه مسلط را طبیعی جلوه دهند.\n۵. تحول دیجیتال: مدل عینیت حرفه‌ای با منطق پلتفرم و رسانه شهروندی به چالش افتاده است.",
        ],
        "applications": [
            "آموزش روزنامه‌نگاری: آموزش عینیت به‌عنوان رویه و نه ادعای خنثی‌بودن.",
            "نقد رسانه: بررسی سوگیری ساختاری در انتخاب و چارچوب‌بندی خبر.",
            "سیاست رسانه‌ای: تحلیل پیامدهای تکیه بر منبع رسمی.",
            "اخلاق خبر: طراحی معیارهای شفافیت در کنار عینیت.",
        ],
        "evolution": "شادسون تاریخ هنجار عینیت را در ۱۹۷۸ ترسیم کرد. پژوهش بعدی، عینیت را به‌عنوان آیین راهبردی، ایدئولوژی حرفه‌ای و ابزار پوشش سوگیری نقد کرد و در محیط دیجیتال، بحث شفافیت و بی‌طرفی را جایگزین یا مکمل آن ساخت.",
        "key_concepts": [
            "عینیت خبری (News Objectivity)",
            "الگوی اطلاعات و داستان (Information vs Story)",
            "آیین راهبردی (Strategic Ritual)",
            "خبر به‌عنوان شکل فرهنگی (News as Cultural Form)",
            "توازن دیدگاه‌ها (Balance)",
            "شفافیت (Transparency)",
        ],
        "studies": [
            "Schudson, M. (1978). Discovering the news: A social history of American newspapers. Basic Books.",
            "Tuchman, G. (1972). Objectivity as strategic ritual. American Journal of Sociology, 77(4), 660-679.",
        ],
        "theorists": "مایکل شادسون (۱۹۷۸)",
        "theorists_text": "مایکل شادسون (۱۹۷۸)",
        "year": 1978,
        "model": "مدل تاریخی: مطبوعات پنی و گذار به «اطلاعات» → بحران اعتماد دهه ۱۹۲۰ → عینیت به‌عنوان راه دفاعی و رویه حرفه‌ای → خبر به‌عنوان شکل فرهنگی.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nشادسون با رویکرد تاریخ اجتماعی نشان داد که هنجارهای خبری محصول شرایط تاریخی‌اند. نوآوری او این بود که عینیت را نه دستاورد طبیعی پیشرفت حرفه‌ای، بلکه پاسخ به بحران اعتماد و رشد روابط عمومی دید؛ تحلیلی که پایه نقد رسانه و جامعه‌شناسی خبر شد.\n\n۲. منطق سنجش و دام‌های آن\nسنجش عینیت نیازمند تحلیل هم‌زمان رویه‌های تولید، محتوای خبر و بافت نهادی است. پژوهش‌هایی که تنها توازن دیدگاه‌ها را می‌سنجند، سوگیری انتخاب رویداد را از دست می‌دهند؛ و پژوهش‌هایی که تنها محتوای یک رسانه را تحلیل می‌کنند، تفاوت منابع و مالکیت را نادیده می‌گیرند.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در نشان دادن تاریخی‌بودن هنجار عینیت است؛ اما نباید به نسبی‌گرایی کامل بینجامد. عینیت به‌عنوان رویه، دستاورد حرفه‌ای مهمی است؛ مسئله در ادعای خنثی‌بودن کامل است، نه در تلاش برای دقت و انصاف.",
        "critique_text": "\n".join([
            "۱. تمرکز آمریکایی: تاریخ روایت‌شده به مطبوعات آمریکا محدود است.",
            "۲. فرض امکان بی‌طرفی: عینیت می‌تواند سوگیری ساختاری را پنهان کند.",
            "۳. کم‌توجهی به مالکیت: نقش منافع تجاری و سیاسی در شکل‌گیری هنجارها کمتر تحلیل می‌شود.",
            "۴. عینیت به‌عنوان پوشش: رویه‌های عینیت می‌توانند دیدگاه مسلط را طبیعی جلوه دهند.",
            "۵. تحول دیجیتال: مدل عینیت حرفه‌ای با منطق پلتفرم و رسانه شهروندی به چالش افتاده است.",
        ]),
        "example_text": "روزنامه‌ای گزارشی درباره یک اعتراض منتشر می‌کند: نقل قول معترضان، نقل قول پلیس و آمار رسمی را کنار هم می‌گذارد. گزارش از نظر رویه‌ای متوازن است، اما انتخاب همین رویداد، همین منابع و همین ترتیب، چارچوبی خاص می‌سازد؛ همین شکاف میان رویه و چارچوب، موضوع نقد عینیت است.",
    },
    "MC-491": {
        "summary": "(انتمن، ۲۰۰۳) مدل فعال‌سازی آبشاری توضیح می‌دهد که چارچوب‌های تفسیری چگونه در یک نظام ارتباطی سلسله‌مراتبی منتشر می‌شوند: چارچوب‌ها ابتدا در سطح دولت فعال می‌شوند، سپس در میان نخبگان دیگر رقابت می‌کنند، بعد به رسانه‌ها می‌رسند و در نهایت افکار عمومی را شکل می‌دهند. توانایی یک چارچوب در عبور از این سطوح به همخوانی فرهنگی، انگیزه و راهبرد بازیگران، قدرت نهادی و شبکه فعال‌سازی بستگی دارد. انتمن این مدل را با مطالعه نبرد بر سر چارچوب رویدادهای ۱۱ سپتامبر نشان داد.",
        "definition": "فعال‌سازی آبشاری، مدلی برای انتشار سلسله‌مراتبی چارچوب‌ها در نظام سیاسی-رسانه‌ای است: چارچوب‌ها از سطح قدرت دولتی به نخبگان، رسانه و عموم سرازیر می‌شوند و در هر سطح می‌توانند تقویت، تعدیل یا مقاومت شوند.",
        "main_problem": "مسئله این است که چرا برخی چارچوب‌های دولتی در رسانه و افکار عمومی مسلط می‌شوند و برخی دیگر در سطح نخبگان یا رسانه متوقف می‌مانند. پاسخ در ترکیب چهار عامل نهفته است: همخوانی چارچوب با فرهنگ مسلط، انگیزه و راهبرد بازیگران، قدرت نهادی و ساختار شبکه رسانه‌ای. پرسش دوم، امکان مقاومت است: چه شرایطی اجازه می‌دهد چارچوب رقیب از پایین به بالا نفوذ کند.",
        "mechanism": "۱. سطوح سلسله‌مراتبی: چارچوب‌ها از دولت به نخبگان دیگر، سپس به رسانه‌ها و در نهایت به افکار عمومی منتقل می‌شوند؛ هر سطح، فیلتر و تقویت‌کننده است.\n۲. همخوانی فرهنگی: چارچوبی که با روایت‌های فرهنگی مسلط همخوان‌تر باشد، آسان‌تر در سطوح پایین پذیرفته می‌شود.\n۳. انگیزه و راهبرد بازیگران: نخبگان و روزنامه‌نگاران بر پایه منافع، باور و راهبرد خود، چارچوب را تقویت، تعدیل یا رد می‌کنند.\n۴. قدرت نهادی: کنترل منابع، دسترسی به رسانه و اقتدار رسمی، توان انتشار چارچوب را افزایش می‌دهد.\n۵. شبکه فعال‌سازی: رسانه‌ها چارچوب‌ها را در شبکه‌ای از متون، منابع و تفسیرها به هم پیوند می‌دهند و از این راه چارچوب را تثبیت می‌کنند.\n۶. مقاومت و شکستن آبشار: چارچوب رقیب وقتی می‌تواند بالا برود که نخبگان رقیب، روزنامه‌نگاران مستقل و شبکه‌های جایگزین آن را تقویت کنند.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا روایت رسمی یک بحران در رسانه‌های اصلی تکرار می‌شود، چرا پلتفرم‌های جایگزین می‌توانند چارچوب رقیب را تقویت کنند و چرا گاه شکاف میان چارچوب نخبگان و افکار عمومی پدید می‌آید. نکته مهم این است که آبشار، جریان یک‌طرفه نیست؛ در هر سطح، مقاومت و تعدیل ممکن است.",
        "assumptions": [
            "چارچوب‌ها در نظامی سلسله‌مراتبی از سطوح قدرت عبور می‌کنند.",
            "همخوانی فرهنگی، شرط پذیرش چارچوب است.",
            "بازیگران در هر سطح، بر پایه انگیزه و راهبرد عمل می‌کنند.",
        ],
        "principles": [
            "چارچوب مسلط، محصول رقابت در چند سطح است، نه فرمان یک‌طرفه.",
            "همخوانی فرهنگی، هزینه انتشار چارچوب را کاهش می‌دهد.",
            "شبکه رسانه‌ای، چارچوب‌ها را تثبیت یا متزلزل می‌کند.",
        ],
        "critiques": [
            "۱. تعمیم از یک مورد: مدل بر مطالعه ۱۱ سپتامبر در آمریکا بنا شده است.\n۲. فرض ساختار آمریکایی: سلسله‌مراتب دولت-رسانه در نظام‌های دیگر متفاوت است.\n۳. سنجش دشوار: تفکیک سطوح و اندازه‌گیری انتقال چارچوب میان آن‌ها پیچیده است.\n۴. کم‌توجهی به پلتفرم: منطق الگوریتمی و رسانه اجتماعی در مدل اصلی جای ندارد.\n۵. رابطه با شاخص‌گذاری: مرز میان آبشاری بودن و تبعیت رسانه از نخبگان (شاخص‌گذاری) روشن نیست.",
        ],
        "applications": [
            "تحلیل بحران: بررسی چگونگی انتشار چارچوب رسمی و رقیب در رسانه.",
            "ارتباطات سیاسی: ارزیابی توان نخبگان در تعریف مسئله و راه‌حل.",
            "پژوهش خبر: تحلیل همخوانی چارچوب خبری با روایت فرهنگی مسلط.",
            "سواد رسانه‌ای: آموزش ردیابی منشأ چارچوب‌ها و مسیر انتشار آن‌ها.",
        ],
        "evolution": "انتمن مدل را در ۲۰۰۳ در ادامه نظریه چارچوب‌بندی خود صورت‌بندی کرد. پژوهش بعدی آن را در بحران‌های دیگر، سیاست خارجی و محیط رسانه‌ای دیجیتال آزمود و با نظریه شاخص‌گذاری و مدل‌های شبکه‌ای ترکیب کرد.",
        "key_concepts": [
            "فعال‌سازی آبشاری (Cascading Activation)",
            "چارچوب‌بندی (Framing)",
            "همخوانی فرهنگی (Cultural Congruence)",
            "شبکه فعال‌سازی (Network Activation)",
            "نخبگان نمادین (Symbolic Elites)",
            "شاخص‌گذاری (Indexing)",
        ],
        "studies": [
            "Entman, R. M. (2003). Cascading activation: Contesting the White House's frame after 9/11. Political Communication, 20(4), 415-432.",
            "Entman, R. M. (1993). Framing: Toward clarification of a fractured paradigm. Journal of Communication, 43(4), 51-58.",
        ],
        "theorists": "رابرت انتمن (۲۰۰۳)",
        "theorists_text": "رابرت انتمن (۲۰۰۳)",
        "year": 2003,
        "model": "مدل چهارسطحی: دولت → نخبگان دیگر → رسانه‌ها → افکار عمومی؛ با چهار تعدیل‌کننده همخوانی فرهنگی، انگیزه بازیگران، قدرت نهادی و شبکه فعال‌سازی.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nانتمن نظریه چارچوب‌بندی را از سطح متن به سطح نظام ارتباطی گسترد. پرسش او این بود که چرا برخی تعریف‌ها از رویداد در کل نظام مسلط می‌شوند؛ پاسخ، ترکیبی از قدرت، فرهنگ و شبکه بود. این مدل، حلقه واسط میان مطالعات چارچوب‌بندی و نظریه نخبگان است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش مدل نیازمند تحلیل هم‌زمان گفتار دولت، نخبگان، رسانه و افکار عمومی است. پژوهش‌هایی که تنها محتوای رسانه را تحلیل می‌کنند، منشأ چارچوب را از دست می‌دهند؛ و پژوهش‌هایی که تنها نظرسنجی عمومی را می‌سنجند، مسیر انتقال را نمی‌بینند.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در نشان دادن پیوند قدرت و معنا است؛ اما باید برای نظام‌های سیاسی متفاوت و محیط پلتفرمی تعدیل شود. در محیط دیجیتال، آبشار می‌تواند چندجهته و آشفته‌تر شود، اما نابرابری دسترسی به منابع چارچوب‌سازی حذف نمی‌شود.",
        "critique_text": "\n".join([
            "۱. تعمیم از یک مورد: مدل بر مطالعه ۱۱ سپتامبر در آمریکا بنا شده است.",
            "۲. فرض ساختار آمریکایی: سلسله‌مراتب دولت-رسانه در نظام‌های دیگر متفاوت است.",
            "۳. سنجش دشوار: تفکیک سطوح و اندازه‌گیری انتقال چارچوب میان آن‌ها پیچیده است.",
            "۴. کم‌توجهی به پلتفرم: منطق الگوریتمی و رسانه اجتماعی در مدل اصلی جای ندارد.",
            "۵. ابهام نسبت با شاخص‌گذاری: مرز آبشاری بودن و تبعیت از نخبگان روشن نیست.",
        ]),
        "example_text": "پس از یک حمله، دولت نخست رویداد را «جنگ علیه تروریسم» چارچوب‌بندی می‌کند؛ نخبگان هم‌سو آن را تکرار می‌کنند، رسانه‌های اصلی منابع رسمی را بازنشر می‌کنند و افکار عمومی همان چارچوب را می‌پذیرد. اگر روزنامه‌نگاران مستقل چارچوب رقیبی مطرح کنند که با روایت فرهنگی مسلط هم‌خوان نباشد، در سطح رسانه متوقف می‌ماند.",
    },
    "MC-492": {
        "summary": "(گرونیگ، ۱۹۹۲) نظریه تعالی، حاصل پروژه پژوهشی گسترده انجمن بین‌المللی ارتباطات تجاری در دهه ۱۹۸۰ است. گرونیگ و همکارانش کوشیدند نشان دهند چه نوع روابط عمومی به اثربخشی سازمان کمک می‌کند. یافته هنجاری اصلی این بود که ارتباط دوسویه متقارن — گفت‌وگویی که به دنبال فهم متقابل و تعدیل دوطرفه است — از مدل‌های یک‌سویه مؤثرتر است. تعالی همچنین به مشارکت روابط عمومی در مدیریت راهبردی، ارتباط درونی متقارن و توانمندسازی کارکرد ارتباط وابسته است.",
        "definition": "نظریه تعالی، چارچوبی هنجاری-تجربی برای ارزیابی روابط عمومی است: ارتباط سازمانی زمانی «متعالی» است که در مدیریت راهبردی مشارکت کند، با عمومی‌ها گفت‌وگوی دوسویه متقارن داشته باشد و کارکرد ارتباط را در سازمان توانمند سازد.",
        "main_problem": "مسئله این است که چه نوع روابط عمومی به اثربخشی سازمان کمک می‌کند و آیا روابط عمومی می‌تواند فراتر از تبلیغ و مدیریت تصویر، کارکردی راهبردی باشد. پاسخ گرونیگ در پیوند ارتباط متقارن با تصمیم‌گیری سازمانی است: سازمانی که به عمومی‌ها گوش می‌دهد، بهتر می‌فهمد و بهتر تصمیم می‌گیرد. پرسش دوم، فاصله هنجار و واقعیت است: چرا بسیاری از سازمان‌ها همچنان مدل‌های یک‌سویه را ترجیح می‌دهند.",
        "mechanism": "۱. روابط عمومی به‌عنوان کارکرد مدیریتی: ارتباط نباید حاشیه‌ای و تشریفاتی باشد؛ باید در تصمیم‌گیری راهبردی سازمان حاضر و مؤثر باشد.\n۲. چهار مدل روابط عمومی: عامل مطبوعاتی، اطلاع‌رسانی عمومی، دوسویه نامتقارن و دوسویه متقارن؛ مدل چهارم، آرمان هنجاری نظریه است.\n۳. ارتباط دوسویه متقارن: سازمان و عمومی، هر دو می‌توانند موضع خود را تعدیل کنند؛ هدف، فهم متقابل است، نه فقط اقناع.\n۴. مشارکت در مدیریت راهبردی: روابط عمومی باید روندهای محیطی و انتظارات عمومی را به تصمیم‌گیران منتقل کند.\n۵. ارتباط درونی متقارن و توانمندسازی: کارکنان نیز عمومی سازمان‌اند؛ ارتباط درونی متقارن، اعتماد و مشارکت می‌سازد.\n۶. تنوع و چندگانگی عمومی: سازمان موفق، عمومی‌های متنوع و متعارض را می‌شناسد و گفت‌وگوی چندصدایی را ممکن می‌کند.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا سازمان‌ها در بحران، به‌جای پاسخ یک‌سویه، به گفت‌وگو و اصلاح تصمیم روی می‌آورند و چرا رسانه‌های اجتماعی، امکان ارتباط دوسویه را گسترده‌تر کرده‌اند. نکته انتقادی این است که تقارن کامل در شرایط نابرابری قدرت دشوار است؛ از این رو نظریه باید با تحلیل منافع و قدرت تکمیل شود.",
        "assumptions": [
            "ارتباط مؤثر، به اثربخشی سازمان کمک می‌کند.",
            "گفت‌وگوی دوسویه متقارن، از مدل‌های یک‌سویه پایدارتر است.",
            "روابط عمومی باید در تصمیم‌گیری راهبردی مشارکت کند.",
        ],
        "principles": [
            "تقارن، آرمان هنجاری روابط عمومی متعالی است.",
            "گوش‌دادن به عمومی‌ها، تصمیم‌گیری سازمان را بهبود می‌دهد.",
            "توانمندسازی کارکرد ارتباط، شرط نقش راهبردی آن است.",
        ],
        "critiques": [
            "۱. فاصله هنجار و واقعیت: بسیاری از سازمان‌ها در عمل به مدل‌های یک‌سویه بسنده می‌کنند.\n۲. تمرکز غربی: پروژه بر سازمان‌های آمریکایی و اروپایی متمرکز بود.\n۳. سنجش اثربخشی: اندازه‌گیری رابطه تعالی و عملکرد سازمانی دشوار و گاه دوری است.\n۴. فرض منافع مشترک: در شرایط نابرابری قدرت، تقارن کامل ممکن نیست.\n۵. روابط عمومی تاریک: نظریه کمتر به کاربردهای دستکاری‌گرانه و پنهان ارتباط می‌پردازد.",
        ],
        "applications": [
            "مدیریت بحران: جایگزینی پاسخ یک‌سویه با گفت‌وگوی متقارن و اصلاح تصمیم.",
            "ارزیابی روابط عمومی: سنجش مشارکت راهبردی و کیفیت ارتباط با عمومی‌ها.",
            "ارتباط درونی: طراحی کانال‌های گفت‌وگوی متقارن با کارکنان.",
            "مسئولیت اجتماعی: پیوند انتظارات عمومی با تصمیم‌گیری سازمان.",
        ],
        "evolution": "گرونیگ چهار مدل را در ۱۹۸۴ صورت‌بندی کرد و در ۱۹۹۲ با پروژه تعالی، مدل دوسویه متقارن را به آرمان هنجاری روابط عمومی بدل کرد. پژوهش بعدی، نظریه را با رویکرد انتقادی، فرهنگی و دیجیتال بازخوانی کرد.",
        "key_concepts": [
            "نظریه تعالی (Excellence Theory)",
            "ارتباط دوسویه متقارن (Symmetrical Two-Way Communication)",
            "مدل‌های چهارگانه روابط عمومی (Four Models of PR)",
            "مدیریت راهبردی (Strategic Management)",
            "توانمندسازی کارکرد ارتباط (Empowered PR Function)",
            "عمومی‌های چندگانه (Multiple Publics)",
        ],
        "studies": [
            "Grunig, J. E. (Ed.). (1992). Excellence in public relations and communication management. Lawrence Erlbaum.",
            "Grunig, J. E., & Hunt, T. (1984). Managing public relations. Holt, Rinehart and Winston.",
        ],
        "theorists": "جیمز گرونیگ (۱۹۸۴؛ ۱۹۹۲)",
        "theorists_text": "جیمز گرونیگ (۱۹۸۴؛ ۱۹۹۲)",
        "year": 1992,
        "model": "مدل تعالی: مشارکت راهبردی + ارتباط دوسویه متقارن (درونی و بیرونی) + توانمندسازی کارکرد ارتباط → اعتماد و اثربخشی سازمانی.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nپروژه تعالی کوشید روابط عمومی را از حاشیه به مرکز تصمیم‌گیری سازمان بیاورد. استدلال اصلی این بود که ارتباط متقارن، اطلاعات بهتری برای تصمیم‌گیری فراهم می‌کند و اعتماد عمومی‌ها را می‌سازد؛ از این رو تعالی، هم هنجاری است و هم کارکردی.\n\n۲. منطق سنجش و دام‌های آن\nسنجش نیازمند تفکیک سه سطح است: رویه ارتباطی، جایگاه کارکرد در سازمان و پیامد سازمانی. پژوهش‌هایی که تنها رضایت مدیران را می‌سنجند، کیفیت گفت‌وگو با عمومی‌ها را از دست می‌دهند؛ و پژوهش‌هایی که تنها اعتماد عمومی را می‌سنجند، نقش تصمیم سازمانی را نمی‌بینند.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در پیوند ارتباط و اثربخشی سازمانی است، اما باید با تحلیل قدرت تعدیل شود. در شرایط نابرابری، تقارن کامل به تغییر توزیع قدرت نیاز دارد؛ بدون آن، گفت‌وگو می‌تواند به ابزار مشروعیت‌بخشی بدل شود.",
        "critique_text": "\n".join([
            "۱. فاصله هنجار و واقعیت: بسیاری از سازمان‌ها در عمل به مدل‌های یک‌سویه بسنده می‌کنند.",
            "۲. تمرکز غربی: پروژه بر سازمان‌های آمریکایی و اروپایی متمرکز بود.",
            "۳. سنجش اثربخشی: اندازه‌گیری رابطه تعالی و عملکرد سازمانی دشوار و گاه دوری است.",
            "۴. فرض منافع مشترک: در شرایط نابرابری قدرت، تقارن کامل ممکن نیست.",
            "۵. روابط عمومی تاریک: نظریه کمتر به کاربردهای دستکاری‌گرانه و پنهان می‌پردازد.",
        ]),
        "example_text": "در یک بحران آلودگی، سازمانی که نخست بیانیه دفاعی می‌فرستد، اعتماد را بیشتر از دست می‌دهد؛ سازمانی که جلسه گفت‌وگو با ساکنان محلی برگزار می‌کند، نگرانی‌ها را ثبت می‌کند و برنامه را اصلاح می‌کند، اعتماد را بازمی‌سازد. تفاوت، در تقارن ارتباط است، نه در حجم پیام.",
    },
}

REQUIRED_SECTIONS = ["summary", "definition", "main_problem", "mechanism", "assumptions",
                     "principles", "critiques", "applications", "evolution", "key_concepts",
                     "theorists", "model", "studies"]
WORD_KEYS = ["summary", "definition", "main_problem", "mechanism", "critiques", "applications",
             "evolution", "key_concepts", "principles", "studies", "assumptions"]


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
    total = structure + analysis + citation + accuracy + relations + classification + clarity + currency
    detail = {"structure_15": structure, "analysis_15": analysis, "citation_20": citation,
              "accuracy_25_auto": accuracy, "relations_10": relations,
              "classification_5": classification, "clarity_5": clarity, "currency_5": currency}
    return total, detail, words


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

        cur.execute("UPDATE kb_entities SET properties=%s, version=version+1, updated_at=%s WHERE id=%s",
                    (json.dumps(p, ensure_ascii=False), NOW, eid))
        cur.execute("SELECT version FROM kb_entities WHERE id=%s", (eid,))
        new_version = cur.fetchone()[0]

        for src in S[code]:
            sid = ensure_source(cur, src)
            cur.execute("SELECT id FROM kb_evidence WHERE about_code=%s AND source_id=%s LIMIT 1", (code, sid))
            if cur.fetchone():
                continue
            lt = {"work": "SECTION", "page_range": "PAGE", "CHAPTER": "CHAPTER"}.get(src["locator_type"], "SECTION")
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
                                       "verified": n_verified, "batch": 90}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH90 THEORY DONE")


if __name__ == "__main__":
    main()
