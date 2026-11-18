# -*- coding: utf-8 -*-
"""Batch 92: full documentation for MC-509, MC-510, MC-511, MC-512."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch92-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch92_theory.json"

S = {
    "MC-509": [
        dict(kind="BOOK",
             title_en="The Managed Heart: Commercialization of Human Feeling",
             title_fa="قلب مدیریت‌شده: کالایی‌شدن احساس انسانی",
             authors="Hochschild, A. R.", year=1983,
             publisher="University of California Press",
             doi=None, url="https://www.jstor.org/stable/10.1525/j.ctt1pn9bk",
             language="en", isbn="9780520272941",
             citation="Hochschild, A. R. (1983). The managed heart: Commercialization of human feeling. University of California Press.",
             locator="work", locator_type="work",
             supports="emotional labor / feeling rules / surface and deep acting / emotional dissonance", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Emotion Work, Feeling Rules, and Social Structure",
             title_fa="کار احساسی، قواعد احساس و ساختار اجتماعی",
             authors="Hochschild, A. R.", year=1979,
             publisher="American Journal of Sociology",
             doi=None, url=None, language="en", isbn=None,
             citation="Hochschild, A. R. (1979). Emotion work, feeling rules, and social structure. American Journal of Sociology, 85(3), 551-575.",
             locator="85(3):551-575", locator_type="page_range",
             supports="emotion work / feeling rules as social structure", verified=False),
    ],
    "MC-510": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="In the Social Factory? Immaterial Labour, Precariousness and Cultural Work",
             title_fa="در کارخانه اجتماعی؟ کار غیرمادی، نامطمئنی و کار فرهنگی",
             authors="Gill, R.; Pratt, A. C.", year=2008,
             publisher="Theory, Culture & Society",
             doi="10.1177/0263276408097794",
             url="https://journals.sagepub.com/doi/10.1177/0263276408097794",
             language="en", isbn=None,
             citation="Gill, R., & Pratt, A. C. (2008). In the social factory? Immaterial labour, precariousness and cultural work. Theory, Culture & Society, 25(7-8), 1-30. https://doi.org/10.1177/0263276408097794",
             locator="25(7-8):1-30", locator_type="page_range",
             supports="precarity as norm / social factory / self-exploitation in cultural work", verified=True),
        dict(kind="BOOK",
             title_en="Creative Labour: Media Work in Three Cultural Industries",
             title_fa="کار خلاق: کار رسانه‌ای در سه صنعت فرهنگی",
             authors="Hesmondhalgh, D.; Baker, S.", year=2011, publisher="Routledge",
             doi=None, url=None, language="en", isbn=None,
             citation="Hesmondhalgh, D., & Baker, S. (2011). Creative labour: Media work in three cultural industries. Routledge.",
             locator="work", locator_type="work",
             supports="good and bad jobs in creative industries / autonomy and precariousness", verified=False),
    ],
    "MC-511": [
        dict(kind="BOOK",
             title_en="Blogs, Wikipedia, Second Life, and Beyond: From Production to Produsage",
             title_fa="وبلاگ‌ها، ویکی‌پدیا، سکند لایف و فراتر: از تولید به پرودیوژن",
             authors="Bruns, A.", year=2008, publisher="Peter Lang",
             doi=None, url="https://www.peterlang.com/document/1105725",
             language="en", isbn=None,
             citation="Bruns, A. (2008). Blogs, Wikipedia, Second Life, and beyond: From production to produsage. Peter Lang.",
             locator="work", locator_type="work",
             supports="produsage characteristics / open participation / fluid heterarchy", verified=True),
        dict(kind="BOOK",
             title_en="Convergence Culture: Where Old and New Media Collide",
             title_fa="فرهنگ همگرایی: جایی که رسانه قدیم و جدید به هم می‌رسند",
             authors="Jenkins, H.", year=2006, publisher="NYU Press",
             doi=None, url=None, language="en", isbn=None,
             citation="Jenkins, H. (2006). Convergence culture: Where old and new media collide. New York University Press.",
             locator="work", locator_type="work",
             supports="participatory culture / user-generated content", verified=False),
    ],
    "MC-512": [
        dict(kind="BOOK",
             title_en="The Third Wave",
             title_fa="موج سوم",
             authors="Toffler, A.", year=1980, publisher="William Morrow",
             doi=None, url=None, language="en", isbn="9780688035976",
             citation="Toffler, A. (1980). The third wave. William Morrow.",
             locator="work", locator_type="work",
             supports="prosumer / reunification of production and consumption / electronic cottage", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Production, Consumption, Prosumption: The Nature of Capitalism in the Age of the Digital 'Prosumer'",
             title_fa="تولید، مصرف، مصرف‌تولید: ماهیت سرمایه‌داری در عصر مصرف‌تولیدکننده دیجیتال",
             authors="Ritzer, G.; Jurgenson, N.", year=2010,
             publisher="Journal of Consumer Culture",
             doi="10.1177/1469540509354673", url=None, language="en", isbn=None,
             citation="Ritzer, G., & Jurgenson, N. (2010). Production, consumption, prosumption: The nature of capitalism in the age of the digital 'prosumer'. Journal of Consumer Culture, 10(1), 13-36. https://doi.org/10.1177/1469540509354673",
             locator="10(1):13-36", locator_type="page_range",
             supports="prosumption as exploitation and empowerment", verified=False),
    ],
}

ENRICH = {
    "MC-509": {
        "summary": "(هوخشیلد، ۱۹۸۳) هوخشیلد در «قلب مدیریت‌شده» نشان داد که در بسیاری از مشاغل خدماتی، احساس بخشی از کار است: مهماندار، پیشخدمت و وصول‌کننده بدهی باید احساس خود را مدیریت کنند تا نمایش عمومی مطلوبی بسازند. او این را «کار هیجانی» نامید و آن را از «کار احساسی» در زندگی خصوصی جدا کرد. کار هیجانی وقتی به دستمزد فروخته شود، قلب را به منبعی مدیریت‌شده بدل می‌کند؛ تنش میان احساس درونی و نمایش بیرونی، «ناهماهنگی هیجانی» می‌سازد.",
        "definition": "کار هیجانی، مدیریت احساس و نمایش هیجانی برای ایجاد حالت ذهنی مطلوب در مخاطب است؛ کاری که در مشاغل خدماتی به‌عنوان بخشی از شغل آموزش داده، نظارت و پاداش داده می‌شود و از کار احساسی در زندگی خصوصی متمایز است.",
        "main_problem": "مسئله این است که وقتی احساس به بخشی از دستمزد بدل می‌شود، چه اتفاقی برای فرد می‌افتد. هوخشیلد نشان داد که کارکنان باید میان احساس واقعی و احساس مطلوب سازمان فاصله بگذارند و این فاصله را مدیریت کنند. پرسش دوم، پیامد است: چه هزینه‌ای برای سلامت روانی، هویت و روابط فرد دارد که «قلب» او در محل کار مدیریت شود.",
        "mechanism": "۱. قواعد احساس: هر موقعیت شغلی، نمایش هیجانی مطلوبی دارد که سازمان آن را تعریف، آموزش و نظارت می‌کند.\n۲. نمایش سطحی: کارمند حالت بیرونی مطلوب را نشان می‌دهد، بی‌آنکه احساس درونی را تغییر دهد؛ لبخند بدون شادی.\n۳. نمایش عمیق: کارمند می‌کوشد احساس درونی را با نقش هماهنگ کند؛ خود را به تجربه مطلوب فرا می‌خواند.\n۴. ناهماهنگی هیجانی: شکاف میان احساس واقعی و نمایش مطلوب، تنش و فرسودگی می‌سازد.\n۵. کالایی‌شدن احساس: وقتی نمایش هیجانی فروخته می‌شود، احساس از دارایی شخصی به منبع سازمانی بدل می‌شود.\n۶. جنسیت و تقسیم کار هیجانی: انتظار نمایش هیجانی میان زنان و مردان و میان مشاغل مختلف یکسان توزیع نمی‌شود.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا مجریان، خبرنگاران و کارکنان پلتفرم‌های خدماتی، احساس خود را برای دوربین و کاربر مدیریت می‌کنند، چرا فرسودگی در مشاغل تعاملی بالا است و چرا آموزش مهارت‌های هیجانی، هم فرصت است و هم فشار. نکته مهم این است که کار هیجانی هم مهارت است و هم هزینه؛ تحلیل بدون دیدن هر دو وجه ناقص است.",
        "assumptions": [
            "احساس در تعامل اجتماعی مدیریت‌پذیر است.",
            "سازمان‌ها قواعد نمایش هیجانی را تعریف و نظارت می‌کنند.",
            "شکاف میان احساس درونی و نمایش بیرونی، پیامد روانی دارد.",
        ],
        "principles": [
            "احساس، بخشی از کار و نه حاشیه آن است.",
            "نمایش سطحی و عمیق، دو راهبرد مدیریت احساس‌اند.",
            "کالایی‌شدن احساس، مرز کار و هویت را مخدوش می‌کند.",
        ],
        "critiques": [
            "۱. نمونه محدود: مطالعه بر مشاغل خدماتی آمریکایی و چند حرفه متمرکز است.\n۲. سنجش دشوار: تفکیک نمایش سطحی از عمیق در مشاهده و مصاحبه آسان نیست.\n۳. فرض مرز کار و خانه: در کار دیجیتال و دورکاری، این مرز مخدوش شده است.\n۴. کم‌توجهی به عاملیت: کارکنان با طنز، فاصله‌گیری و همبستگی در برابر فشار مقاومت می‌کنند.\n۵. تحول پلتفرم: کار هیجانی در تعامل با کاربر و الگوریتم شکل تازه‌ای یافته است.",
        ],
        "applications": [
            "مدیریت خدمات: طراحی آموزش هیجانی بدون نادیده‌گرفتن هزینه روانی.",
            "سلامت شغلی: شناسایی فرسودگی ناشی از ناهماهنگی هیجانی.",
            "مطالعات رسانه: تحلیل کار هیجانی مجریان و چهره‌های رسانه‌ای.",
            "مطالعات جنسیت: بررسی توزیع نابرابر کار هیجانی.",
        ],
        "evolution": "هوخشیلد مفهوم کار احساسی را در ۱۹۷۹ صورت‌بندی کرد و در ۱۹۸۳ با «قلب مدیریت‌شده» آن را به کار هیجانی در سازمان گسترد. پژوهش بعدی، مفهوم را به کار دیجیتال، خدمات پلتفرمی و هیجانات الگوریتمی بسط داد.",
        "key_concepts": [
            "کار هیجانی (Emotional Labor)",
            "قواعد احساس (Feeling Rules)",
            "نمایش سطحی (Surface Acting)",
            "نمایش عمیق (Deep Acting)",
            "ناهماهنگی هیجانی (Emotional Dissonance)",
            "کالایی‌شدن احساس (Commodification of Feeling)",
        ],
        "studies": [
            "Hochschild, A. R. (1983). The managed heart: Commercialization of human feeling. University of California Press.",
            "Hochschild, A. R. (1979). Emotion work, feeling rules, and social structure. American Journal of Sociology, 85(3), 551-575.",
        ],
        "theorists": "آرلی راسل هوخشیلد (۱۹۸۳)",
        "theorists_text": "آرلی راسل هوخشیلد (۱۹۷۹؛ ۱۹۸۳)",
        "year": 1983,
        "model": "مدل کار هیجانی: قواعد احساس سازمانی → نمایش سطحی یا عمیق → ناهماهنگی هیجانی → فرسودگی و کالایی‌شدن احساس.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nهوخشیلد سنت جامعه‌شناسی احساس را با نقد اقتصاد خدماتی پیوند داد. نوآوری او این بود که احساس را نه حالت درونی صرف، بلکه عمل اجتماعی مدیریت‌شده دید؛ ایده‌ای که کار عاطفی را به موضوعی سازمانی و سیاسی بدل کرد.\n\n۲. منطق سنجش و دام‌های آن\nسنجش نیازمند مشاهده تعامل، مصاحبه درباره تجربه درونی و تحلیل قواعد سازمانی است. پژوهش‌هایی که تنها ظاهر رفتار را کدگذاری می‌کنند، تفاوت نمایش سطحی و عمیق را از دست می‌دهند؛ و پژوهش‌هایی که تنها فرسودگی را می‌سنجند، منبع سازمانی آن را نشان نمی‌دهند.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در پیوند احساس و کار است، اما باید با تحلیل قدرت و جنسیت تکمیل شود. در محیط پلتفرمی، کار هیجانی از تعامل رو در رو به تعامل با مخاطب ناشناس و سنجه‌های الگوریتمی گسترش یافته است.",
        "critique_text": "\n".join([
            "۱. نمونه محدود: مطالعه بر مشاغل خدماتی آمریکایی متمرکز است.",
            "۲. سنجش دشوار: تفکیک نمایش سطحی از عمیق آسان نیست.",
            "۳. فرض مرز کار و خانه: در کار دیجیتال، این مرز مخدوش شده است.",
            "۴. کم‌توجهی به عاملیت: کارکنان با طنز و فاصله‌گیری مقاومت می‌کنند.",
            "۵. تحول پلتفرم: کار هیجانی در تعامل با کاربر و الگوریتم شکل تازه‌ای یافته است.",
        ]),
        "example_text": "مهمانداری که در یک پرواز پرتنش لبخند می‌زند و آرامش نشان می‌دهد، هم‌زمان خستگی و نگرانی خود را سرکوب می‌کند. اگر این فاصله هر روز تکرار شود و سازمان تنها لبخند را بسنجد، نمایش سطحی به فرسودگی می‌انجامد؛ همان ناهماهنگی هیجانی که هوخشیلد توصیف کرد.",
    },
    "MC-510": {
        "summary": "(گیل و پرات، ۲۰۰۸) گیل و پرات نشان دادند که کار فرهنگی و خلاق، نمونه پیشرو «کار نامطمئن» است: قراردادهای کوتاه، پروژه‌محوری، کار بدون دستمزد، خودبهره‌کشی از سر عشق به کار و آمیختگی زندگی و کار. آنها با مفهوم «کارخانه اجتماعی» استدلال کردند که مرز کار و زندگی در این حوزه فروریخته و کل شبکه اجتماعی فرد به نیروی کار بدل می‌شود. نتیجه، نابرابری پنهان است: کسانی که پشتوانه مالی دارند، می‌توانند ریسک کنند و کسانی که ندارند، از میدان بیرون می‌مانند.",
        "definition": "کار خلاق و نامطمئن، الگویی از اشتغال در صنایع فرهنگی است که در آن پروژه‌محوری، قرارداد کوتاه، کار بی‌دستمزد و آمیختگی هویت حرفه‌ای با زندگی شخصی، ناامنی را به هنجار بدل می‌کند.",
        "main_problem": "مسئله این است که چرا کار خلاق، با وجود جذابیت و آزادی ظاهری، به ناامنی و نابرابری می‌انجامد. پاسخ در ساختار اشتغال است: پروژه‌محوری و شبکه‌محوری، امنیت بلندمدت را حذف می‌کند و هزینه ریسک را به فرد منتقل می‌سازد. پرسش دوم، پیامد است: چگونه ناامنی، روابط، سلامت و فرصت‌های گروه‌های محروم را شکل می‌دهد.",
        "mechanism": "۱. پروژه‌محوری و قرارداد کوتاه: کار به زنجیره‌ای از پروژه‌های موقت بدل می‌شود و امنیت شغلی از میان می‌رود.\n۲. کار بی‌دستمزد: کارآموزی، نمونه‌کار و آماده‌سازی، بخش پنهان و بی‌مزد چرخه کار خلاق است.\n۳. خودبهره‌کشی: عشق به کار، ساعات طولانی و مرزنامشخص را توجیه می‌کند و بهره‌کشی را درونی می‌سازد.\n۴. شبکه‌سازی به‌عنوان کار: حفظ رابطه، حضور اجتماعی و خودنمایی حرفه‌ای، بخشی از کار بدون دستمزد است.\n۵. کارخانه اجتماعی: مرز کار و زندگی فرومی‌ریزد و هویت، اوقات فراغت و روابط به منابع کار بدل می‌شوند.\n۶. نابرابری دسترسی: پشتوانه مالی، مسکن و شبکه خانوادگی، توان تحمل ریسک را نابرابر توزیع می‌کند.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا روزنامه‌نگاران آزاد، طراحان و تولیدکنندگان محتوا با بی‌ثباتی درآمد و فرسودگی روبه‌رویند، چرا «کار با عشق» می‌تواند پوششی برای بهره‌کشی باشد و چرا سیاست‌های صنایع خلاق، نابرابری را بازتولید می‌کنند. نکته مهم این است که ناامنی، انتخاب آزاد نیست؛ ساختار بازار و سیاست آن را تحمیل می‌کند.",
        "assumptions": [
            "کار خلاق، الگوی پیشرو تغییر ساختار اشتغال است.",
            "مرز کار و زندگی در این حوزه فروریخته است.",
            "ناامنی، هزینه‌ای است که به فرد منتقل می‌شود.",
        ],
        "principles": [
            "عشق به کار، جایگزین امنیت شغلی نمی‌شود.",
            "شبکه‌سازی، کار بی‌دستمزد است.",
            "دسترسی به کار خلاق، به منابع خانوادگی وابسته است.",
        ],
        "critiques": [
            "۱. تمرکز بر بریتانیا: یافته‌ها بر یک زمینه ملی و بخش خاص استوارند.\n۲. تعمیم به همه کار خلاق: تفاوت میان زیربخش‌ها و سطوح مهارت کم‌رنگ می‌شود.\n۳. کم‌توجهی به عاملیت: برخی کارکنان با مذاکره و همبستگی، ناامنی را مدیریت می‌کنند.\n۴. ابهام سنجش: اندازه‌گیری خودبهره‌کشی و مرز کار و زندگی دشوار است.\n۵. تحول پلتفرم: کار الگوریتمی و اقتصادی گیگ، شکل تازه‌ای از ناامنی ساخته است.",
        ],
        "applications": [
            "سیاست صنایع خلاق: طراحی حمایت از اشتغال پایدار و بیمه.",
            "مدیریت رسانه: شناسایی هزینه پنهان کار پروژه‌ای.",
            "حقوق کار: تنظیم کار بی‌دستمزد و کارآموزی.",
            "سلامت شغلی: پیشگیری از فرسودگی در کار خلاق.",
        ],
        "evolution": "گیل و پرات در ۲۰۰۸ ناامنی کار خلاق را در چارچوب کارخانه اجتماعی صورت‌بندی کردند. پژوهش بعدی، مفهوم را به کار پلتفرمی، اقتصاد گیگ و نابرابری‌های جنسیتی و نژادی گسترد.",
        "key_concepts": [
            "کار نامطمئن (Precarious Work)",
            "کارخانه اجتماعی (Social Factory)",
            "خودبهره‌کشی (Self-Exploitation)",
            "کار بی‌دستمزد (Unpaid Work)",
            "صنایع خلاق (Creative Industries)",
            "مسیر بلعنده (Bulimic Career)",
        ],
        "studies": [
            "Gill, R., & Pratt, A. C. (2008). In the social factory? Theory, Culture & Society, 25(7-8), 1-30.",
            "Hesmondhalgh, D., & Baker, S. (2011). Creative labour. Routledge.",
        ],
        "theorists": "گیل و پرات (۲۰۰۸)",
        "theorists_text": "گیل و پرات (۲۰۰۸)",
        "year": 2008,
        "model": "مدل ناامنی: پروژه‌محوری → کار بی‌دستمزد و خودبهره‌کشی → فروریختن مرز کار و زندگی → نابرابری دسترسی و فرسودگی.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nگیل و پرات، ادبیات کار غیرمادی و اقتصاد سیاسی رسانه را با مطالعات تجربی کار فرهنگی ترکیب کردند. نوآوری آنها این بود که جذابیت کار خلاق را نقد نکردند تا آن را رد کنند؛ نشان دادند که همان جذابیت، سازوکار بهره‌کشی را پنهان می‌کند.\n\n۲. منطق سنجش و دام‌های آن\nسنجش نیازمند ترکیب داده‌های اشتغال، درآمد، ساعت کار و تجربه زیسته است. پژوهش‌هایی که تنها درآمد را می‌سنجند، هزینه هویت و سلامت را از دست می‌دهند؛ و پژوهش‌هایی که تنها روایت‌های فردی را می‌شنوند، ساختار بازار را نمی‌بینند.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در پیوند ناامنی فردی و ساختار اقتصادی است، اما باید با تحلیل سیاست عمومی تکمیل شود. در محیط پلتفرمی، ناامنی از پروژه به الگوریتم منتقل شده است؛ سنجه‌های دیده‌شدن، شکل تازه‌ای از فشار بی‌پایان ساخته‌اند.",
        "critique_text": "\n".join([
            "۱. تمرکز بر بریتانیا: یافته‌ها بر یک زمینه ملی استوارند.",
            "۲. تعمیم به همه کار خلاق: تفاوت زیربخش‌ها کم‌رنگ می‌شود.",
            "۳. کم‌توجهی به عاملیت: برخی کارکنان با همبستگی ناامنی را مدیریت می‌کنند.",
            "۴. ابهام سنجش: اندازه‌گیری خودبهره‌کشی دشوار است.",
            "۵. تحول پلتفرم: کار الگوریتمی شکل تازه‌ای از ناامنی ساخته است.",
        ]),
        "example_text": "یک طراح آزاد برای دیده‌شدن، هر روز در شبکه‌های اجتماعی نمونه‌کار منتشر می‌کند، در رویدادها شرکت می‌کند و گاه پروژه آزمایشی بی‌دستمزد می‌پذیرد. بخش بزرگی از کار او دستمزد ندارد، اما شرط دسترسی به پروژه بعدی است؛ همین چرخه، نمونه روشن کارخانه اجتماعی است.",
    },
    "MC-511": {
        "summary": "(برونز، ۲۰۰۸) برونز مفهوم «پرودیوژن» را برای توصیف تولید مشارکتی کاربران ساخت: در محیط‌های شبکه‌ای، مرز تولیدکننده و مصرف‌کننده فرومی‌ریزد و کاربر هم‌زمان مصرف می‌کند و می‌سازد. او چهار ویژگی برای آن برشمرد: مشارکت باز و ارزیابی جمعی، سلسله‌مراتب سیال و شایسته‌سالاری موقت، محصول ناتمام و فرایند پیوسته، و مالکیت مشترک با پاداش فردی. ویکی‌پدیا، نرم‌افزار آزاد و وبلاگ، نمونه‌های این الگو هستند.",
        "definition": "پرودیوژن، الگوی تولید مشارکتی در محیط‌های شبکه‌ای است که در آن کاربران هم‌زمان مصرف‌کننده و تولیدکننده‌اند و محصول، پیوسته و جمعی و با مالکیت مشترک ساخته و بازسازی می‌شود.",
        "main_problem": "مسئله این است که آیا مفاهیم صنعتی تولید و مصرف برای محیط شبکه‌ای بسنده‌اند. برونز پاسخ می‌دهد که نه: در ویکی‌پدیا و نرم‌افزار آزاد، کاربر نه مشتری منفعل است و نه تولیدکننده حرفه‌ای، بلکه مشارکت‌کننده‌ای است که محصول را می‌سازد و هم‌زمان از آن استفاده می‌کند. پرسش دوم، کیفیت و اعتبار است: تولید جمعی و ناتمام چگونه می‌تواند قابل اعتماد بماند.",
        "mechanism": "۱. مشارکت باز و ارزیابی جمعی: هر کس می‌تواند وارد شود و کیفیت از دل بررسی هم‌نظران و اصلاح پیوسته بیرون می‌آید.\n۲. سلسله‌مراتب سیال و شایسته‌سالاری موقت: جایگاه از مشارکت و اعتبار به‌دست می‌آید و ثابت نیست.\n۳. محصول ناتمام و فرایند پیوسته: اثر هرگز «تمام» نیست؛ نسخه‌ها و اصلاح‌ها بخشی از ماهیت آن‌اند.\n۴. مالکیت مشترک و پاداش فردی: محصول به جامعه تعلق دارد، اما افراد برای اعتبار و مهارت پاداش می‌گیرند.\n۵. دروازه‌بانی به دروازه‌نگری: به‌جای گزینش پیش از انتشار، مشارکت‌کنندگان جریان محتوا را می‌پایند و پس از انتشار ارزیابی می‌کنند.\n۶. اعتبار احتمالی: به‌جای تضمین قطعی، سازوکارهایی مانند تاریخ ویرایش و بحث، احتمال درستی را می‌سازند.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا ویکی‌پدیا و نرم‌افزار آزاد می‌توانند بدون سازمان تولید صنعتی کار کنند، چرا رسانه‌های شهروندی به سازوکار اعتبار نیاز دارند و چرا پلتفرم‌ها با جذب مشارکت کاربر، آن را به ارزش اقتصادی بدل می‌کنند. نکته مهم این است که پرودیوژن، هم توانمندسازی است و هم میدان تازه‌ای برای بهره‌کشی از کار رایگان.",
        "assumptions": [
            "مرز تولیدکننده و مصرف‌کننده در محیط شبکه‌ای فرومی‌ریزد.",
            "تولید جمعی می‌تواند کیفیت قابل قبول بسازد.",
            "اعتبار از مشارکت و ارزیابی جمعی حاصل می‌شود.",
        ],
        "principles": [
            "محصول باز و ناتمام، فرصت اصلاح پیوسته می‌دهد.",
            "شایسته‌سالاری موقت، جای سلسله‌مراتب ثابت را می‌گیرد.",
            "ارزیابی پس از انتشار، جای گزینش پیش از انتشار را می‌گیرد.",
        ],
        "critiques": [
            "۱. نمونه‌گزینی موفق: ویکی‌پدیا و نرم‌افزار آزاد، موارد استثنایی‌اند و همه مشارکت‌ها چنین نیستند.\n۲. کم‌توجهی به نابرابری: مشارکت باز، نابرابری مهارت، زمان و زبان را حذف نمی‌کند.\n۳. کار رایگان: ارزش تولید کاربر، اغلب به پلتفرم منتقل می‌شود.\n۴. کیفیت و سوگیری: تولید جمعی می‌تواند سوگیری گروه مشارکت‌کننده را بازتولید کند.\n۵. ابهام مرز: تفکیک پرودیوژن از بازاریابی مشارکتی و کار طرفداران روشن نیست.",
        ],
        "applications": [
            "طراحی پلتفرم: ساخت سازوکار ارزیابی جمعی و تاریخ ویرایش.",
            "رسانه شهروندی: طراحی اعتبارسنجی برای محتوای کاربرساخته.",
            "آموزش: استفاده از تولید مشارکتی در یادگیری.",
            "سیاست دانش: حمایت از منابع دانش باز و مالکیت مشترک.",
        ],
        "evolution": "برونز مفهوم را در ۲۰۰۸ صورت‌بندی کرد. پژوهش بعدی آن را به رسانه اجتماعی، هوش مصنوعی مشارکتی و اقتصاد سازندگان گسترد و نقد کار رایگان را افزود.",
        "key_concepts": [
            "پرودیوژن (Produsage)",
            "کاربر تولیدکننده (Producer-User)",
            "شایسته‌سالاری موقت (Ad Hoc Meritocracy)",
            "محصول ناتمام (Unfinished Artefact)",
            "دروازه‌نگری (Gatewatching)",
            "مالکیت مشترک (Common Property)",
        ],
        "studies": [
            "Bruns, A. (2008). Blogs, Wikipedia, Second Life, and beyond: From production to produsage. Peter Lang.",
            "Jenkins, H. (2006). Convergence culture. New York University Press.",
        ],
        "theorists": "اکسل برونز (۲۰۰۸)",
        "theorists_text": "اکسل برونز (۲۰۰۸)",
        "year": 2008,
        "model": "مدل چهارویژگی: مشارکت باز و ارزیابی جمعی + سلسله‌مراتب سیال + محصول ناتمام + مالکیت مشترک/پاداش فردی → تولید مشارکتی پیوسته.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nبرونز در برابر مدل خطی تولید صنعتی ایستاد و تولید مشارکتی را نه حاشیه، بلکه الگوی نوظهور محیط شبکه‌ای دید. نوآوری او صورت‌بندی چهار ویژگی بود که پرودیوژن را از مشارکت ساده کاربران جدا می‌کند.\n\n۲. منطق سنجش و دام‌های آن\nسنجش نیازمند تحلیل ساختار مشارکت، سازوکار کیفیت و توزیع پاداش است. پژوهش‌هایی که تنها شمار مشارکت‌کنندگان را می‌شمارند، کیفیت را از دست می‌دهند؛ و پژوهش‌هایی که تنها محصول نهایی را می‌بینند، فرایند پیوسته اصلاح را نمی‌بینند.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در توضیح تولید بدون سازمان صنعتی است، اما باید با اقتصاد سیاسی پلتفرم تکمیل شود. مشارکت باز در محیطی رخ می‌دهد که شرایط استفاده، داده و ارزش افزوده را پلتفرم تعیین می‌کند.",
        "critique_text": "\n".join([
            "۱. نمونه‌گزینی موفق: ویکی‌پدیا و نرم‌افزار آزاد موارد استثنایی‌اند.",
            "۲. کم‌توجهی به نابرابری: مشارکت باز، نابرابری مهارت و زمان را حذف نمی‌کند.",
            "۳. کار رایگان: ارزش تولید کاربر اغلب به پلتفرم منتقل می‌شود.",
            "۴. کیفیت و سوگیری: تولید جمعی می‌تواند سوگیری گروه را بازتولید کند.",
            "۵. ابهام مرز: تفکیک پرودیوژن از بازاریابی مشارکتی روشن نیست.",
        ]),
        "example_text": "کاربری مقاله‌ای در ویکی‌پدیا می‌خواند، خطایی را اصلاح می‌کند و در صفحه بحث درباره منبع آن استدلال می‌آورد. او هم مصرف‌کننده است و هم تولیدکننده؛ محصول بدون او و هزاران کاربر دیگر، هرگز کامل نمی‌شود.",
    },
    "MC-512": {
        "summary": "(تافلر، ۱۹۸۰) تافلر در «موج سوم» واژه «تولیدگر» را ساخت: کسی که تولید و مصرف را در هم می‌آمیزد. در موج اول کشاورزی، تولید و مصرف در خانواده یکی بود؛ موج دوم صنعتی آن دو را جدا کرد و بازار واسطه شد؛ موج سوم، با فناوری‌های اطلاعاتی و کار خانگی الکترونیکی، این دو را دوباره به هم می‌پیوندد. پیش‌بینی تافلر از اقتصاد خودت انجام بده، بعدها با فرهنگ سازندگان، چاپ سه‌بعدی و محتوای کاربرساخته بازخوانی شد.",
        "definition": "تولیدگر یا مصرف‌تولیدکننده، فردی است که هم‌زمان تولیدکننده و مصرف‌کننده کالا و خدمت است؛ مفهومی که تافلر آن را برای توصیف بازپیوند تولید و مصرف در موج سوم به کار برد.",
        "main_problem": "مسئله این است که جدایی تولید و مصرف، ویژگی طبیعی اقتصاد نیست. تافلر نشان داد که این جدایی محصول موج دوم صنعتی است و با فناوری اطلاعات می‌تواند به هم بخورد. پرسش دوم، پیامد است: بازپیوند تولید و مصرف چه اثری بر کار، خانواده، بازار و روابط اجتماعی دارد.",
        "mechanism": "۱. سه‌موج: تاریخ به سه موج کشاورزی، صنعتی و اطلاعاتی تقسیم می‌شود و هر موج، الگوی تولید و مصرف خود را دارد.\n۲. جدایی تولید و مصرف: موج صنعتی، تولید را به کارخانه و مصرف را به بازار منتقل کرد و خانواده را از تولید جدا ساخت.\n۳. بازپیوند: موج سوم این دو را در خانه، اجتماع و محیط شبکه‌ای دوباره به هم می‌پیوندد.\n۴. فناوری اطلاعات و خانه الکترونیکی: رایانه و شبکه، امکان تولید در خانه و کار از راه دور را فراهم می‌کنند.\n۵. اقتصاد خودت انجام بده: بخشی از تولید به فعالیت خودیار و غیربازاری منتقل می‌شود.\n۶. پیامدهای فرهنگی و روانی: تغییر الگوی کار، هویت، مصرف و روابط خانوادگی را دگرگون می‌کند.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا محتوای کاربرساخته، فرهنگ سازندگان و تولید خانگی رشد کرده و چرا مرز مصرف‌کننده و تولیدکننده در پلتفرم‌ها مخدوش شده است. نکته مهم این است که پیش‌بینی تافلر کلی و جبرگرایانه بود؛ بازپیوند تولید و مصرف در عمل با مالکیت پلتفرمی و نابرابری دیجیتال همراه شد.",
        "assumptions": [
            "تاریخ اجتماعی در قالب سه موج قابل فهم است.",
            "فناوری اطلاعات، مرز تولید و مصرف را جابه‌جا می‌کند.",
            "بازپیوند تولید و مصرف، پیامد فرهنگی و روانی دارد.",
        ],
        "principles": [
            "جدایی تولید و مصرف، محصول تاریخی است، نه ویژگی طبیعی.",
            "فناوری می‌تواند محل تولید را به خانه و اجتماع بازگرداند.",
            "مصرف‌کننده می‌تواند هم‌زمان تولیدکننده باشد.",
        ],
        "critiques": [
            "۱. جبرگرایی فناورانه: فناوری عامل اصلی تغییر فرض می‌شود و روابط قدرت کمتر دیده می‌شود.\n۲. پیش‌بینی‌های نادرست: برخی پیش‌بینی‌های موج سوم محقق نشدند.\n۳. کم‌توجهی به مالکیت: بازپیوند تولید و مصرف، مالکیت و کنترل را تغییر نداد.\n۴. رمانتیک‌سازی خودیاری: کار خانگی و خودت انجام بده می‌تواند بار اضافی و نابرابری جنسیتی بسازد.\n۵. تفاوت با پرودیوژن شبکه‌ای: مدل تافلر، مشارکت جمعی و مالکیت مشترک را در نظر ندارد.",
        ],
        "applications": [
            "مطالعات مصرف: تحلیل مصرف‌کننده به‌عنوان تولیدکننده معنا و محتوا.",
            "اقتصاد دیجیتال: بررسی کار خانگی، خودیاری و اقتصاد سازندگان.",
            "مطالعات خانواده: تحلیل بازپیوند کار و خانه.",
            "آموزش رسانه: نقد پیش‌بینی‌های فناورانه درباره آینده کار و مصرف.",
        ],
        "evolution": "تافلر مفهوم را در ۱۹۸۰ معرفی کرد. پژوهش بعدی آن را با فرهنگ سازندگان، تولید همتا و پرودیوژن شبکه‌ای پیوند داد و در برابر آن، نقد اقتصاد سیاسی پلتفرم را مطرح کرد.",
        "key_concepts": [
            "تولیدگر (Prosumer)",
            "موج سوم (Third Wave)",
            "خانه الکترونیکی (Electronic Cottage)",
            "خودت انجام بده (Do-It-Yourself)",
            "بازپیوند تولید و مصرف (Reintegration of Production and Consumption)",
            "فرهنگ سازندگان (Maker Culture)",
        ],
        "studies": [
            "Toffler, A. (1980). The third wave. William Morrow.",
            "Ritzer, G., & Jurgenson, N. (2010). Production, consumption, prosumption. Journal of Consumer Culture, 10(1), 13-36.",
        ],
        "theorists": "آلوین تافلر (۱۹۸۰)",
        "theorists_text": "آلوین تافلر (۱۹۸۰)",
        "year": 1980,
        "model": "مدل سه‌موج: یکپارچگی تولید-مصرف (موج اول) → جدایی و بازار (موج دوم) → بازپیوند فناورانه و خانه الکترونیکی (موج سوم).",
        "detailed_analysis": "۱. بنیان و منطق نظری\nتافلر تاریخ اقتصاد و فرهنگ را در قالب امواج تغییر صورت‌بندی کرد. نوآوری او مفهوم تولیدگر بود: نشان داد که مصرف‌کننده می‌تواند تولیدکننده باشد و این تغییر، پیامدهای گسترده‌ای برای کار و خانواده دارد.\n\n۲. منطق سنجش و دام‌های آن\nسنجش نیازمند ردیابی سهم تولید غیربازاری، کار خانگی و فعالیت خودیار است. پژوهش‌هایی که تنها بازار رسمی را می‌سنجند، این بخش را از دست می‌دهند؛ و پژوهش‌هایی که تنها فناوری را می‌سنجند، روابط قدرت و مالکیت را نادیده می‌گیرند.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در پیش‌بینی بازپیوند تولید و مصرف است، اما تحلیل آن جبرگرایانه و کلی است. در محیط پلتفرمی، مصرف‌تولید با داده و تبلیغات پیوند خورده و شکل تازه‌ای از بهره‌کشی و مشارکت ساخته است.",
        "critique_text": "\n".join([
            "۱. جبرگرایی فناورانه: فناوری عامل اصلی تغییر فرض می‌شود.",
            "۲. پیش‌بینی‌های نادرست: برخی پیش‌بینی‌های موج سوم محقق نشدند.",
            "۳. کم‌توجهی به مالکیت: بازپیوند تولید و مصرف، کنترل را تغییر نداد.",
            "۴. رمانتیک‌سازی خودیاری: بار اضافی و نابرابری جنسیتی نادیده می‌ماند.",
            "۵. تفاوت با پرودیوژن: مشارکت جمعی و مالکیت مشترک در مدل نیست.",
        ]),
        "example_text": "خانواده‌ای با چاپگر سه‌بعدی قطعه‌ای برای لوازم خانگی می‌سازد، دستور ساخت را با دیگران به اشتراک می‌گذارد و هم‌زمان از راهنمای دیگران استفاده می‌کند. او هم مصرف‌کننده است و هم تولیدکننده؛ نمونه‌ای از همان بازپیوندی که تافلر پیش‌بینی کرد.",
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

        if code == "MC-511":
            cur.execute("UPDATE kb_entities SET canonical_name_fa=%s WHERE id=%s",
                        ("پرودیوژن / کاربر تولیدکننده", eid))
            cur.execute("""INSERT INTO kb_audit_log (entity_code,action,detail,source,created_at)
                VALUES (%s,'DOC_FIX',%s,%s,%s)""",
                        (code, json.dumps({"fix": "canonical_name_fa repaired (corrupt 'usage' token)"},
                                          ensure_ascii=False), STAMP, NOW))

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
                                       "verified": n_verified, "batch": 92}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH92 THEORY DONE")


if __name__ == "__main__":
    main()
