# -*- coding: utf-8 -*-
"""Batch 94: full documentation for MC-517, MC-518, MC-519, MC-521."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch94-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch94_theory.json"

UTAUT_T = "User Acceptance of Information Technology: Toward a Unified View"

S = {
    "MC-517": [
        dict(kind="JOURNAL_ARTICLE",
             title_en=UTAUT_T,
             title_fa="پذیرش فناوری اطلاعات توسط کاربر: به سوی دیدگاهی یکپارچه",
             authors="Venkatesh, V.; Morris, M. G.; Davis, G. B.; Davis, F. D.", year=2003,
             publisher="MIS Quarterly",
             doi="10.2307/30036540",
             url="https://misq.umn.edu/misq/article/27/3/425/1340/User-Acceptance-of-Information-Technology-Toward-A",
             language="en", isbn=None,
             citation="Venkatesh, V., Morris, M. G., Davis, G. B., & Davis, F. D. (2003). User acceptance of information technology: Toward a unified view. MIS Quarterly, 27(3), 425-478. https://doi.org/10.2307/30036540",
             locator="27(3):425-478", locator_type="page_range",
             supports="four core determinants / moderators / unified acceptance model", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Consumer Acceptance and Use of Information Technology: Extending the Unified Theory of Acceptance and Use of Technology",
             title_fa="پذیرش و استفاده مصرف‌کننده از فناوری اطلاعات: گسترش نظریه یکپارچه",
             authors="Venkatesh, V.; Thong, J. Y. L.; Xu, X.", year=2012,
             publisher="MIS Quarterly",
             doi=None, url=None, language="en", isbn=None,
             citation="Venkatesh, V., Thong, J. Y. L., & Xu, X. (2012). Consumer acceptance and use of information technology: Extending the unified theory of acceptance and use of technology. MIS Quarterly, 36(1), 157-178.",
             locator="36(1):157-178", locator_type="page_range",
             supports="hedonic motivation / price value / habit extension", verified=False),
    ],
    "MC-518": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Technologies, Texts and Affordances",
             title_fa="فناوری‌ها، متن‌ها و امکانات عمل",
             authors="Hutchby, I.", year=2001, publisher="Sociology",
             doi="10.1017/S0038038501000219",
             url="https://journals.sagepub.com/doi/10.1177/S0038038501000219",
             language="en", isbn=None,
             citation="Hutchby, I. (2001). Technologies, texts and affordances. Sociology, 35(2), 441-456. https://doi.org/10.1017/S0038038501000219",
             locator="35(2):441-456", locator_type="page_range",
             supports="affordances as framing not determining / relational position", verified=True),
        dict(kind="BOOK",
             title_en="The Ecological Approach to Visual Perception",
             title_fa="رویکرد بوم‌شناختی به ادراک دیداری",
             authors="Gibson, J. J.", year=1979, publisher="Houghton Mifflin",
             doi=None, url=None, language="en", isbn=None,
             citation="Gibson, J. J. (1979). The ecological approach to visual perception. Houghton Mifflin.",
             locator="work", locator_type="work",
             supports="affordances as directly perceived action possibilities", verified=False),
        dict(kind="BOOK",
             title_en="The Psychology of Everyday Things",
             title_fa="روان‌شناسی اشیای روزمره",
             authors="Norman, D. A.", year=1988, publisher="Basic Books",
             doi=None, url=None, language="en", isbn=None,
             citation="Norman, D. A. (1988). The psychology of everyday things. Basic Books.",
             locator="work", locator_type="work",
             supports="perceived affordances in design", verified=False),
    ],
    "MC-519": [
        dict(kind="REPORT",
             title_en="Information Management: A Proposal",
             title_fa="مدیریت اطلاعات: یک پیشنهاد",
             authors="Berners-Lee, T.", year=1989, publisher="CERN",
             doi=None, url="https://cds.cern.ch/record/369245/files/dd-89-001.pdf",
             language="en", isbn=None,
             citation="Berners-Lee, T. (1989). Information management: A proposal. CERN.",
             locator="work", locator_type="work",
             supports="distributed hypertext information space / web as environment", verified=True),
        dict(kind="BOOK",
             title_en="Weaving the Web: The Original Design and Ultimate Destiny of the World Wide Web",
             title_fa="بافتن وب: طراحی آغازین و سرنوشت نهایی وب جهانی",
             authors="Berners-Lee, T.; Fischetti, M.", year=1999, publisher="HarperSanFrancisco",
             doi=None, url=None, language="en", isbn=None,
             citation="Berners-Lee, T., & Fischetti, M. (1999). Weaving the web: The original design and ultimate destiny of the World Wide Web. HarperSanFrancisco.",
             locator="work", locator_type="work",
             supports="web as open information space / design principles", verified=False),
    ],
    "MC-521": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Emergence of Scaling in Random Networks",
             title_fa="ظهور مقیاس‌ناپذیری در شبکه‌های تصادفی",
             authors="Barabasi, A.-L.; Albert, R.", year=1999, publisher="Science",
             doi="10.1126/science.286.5439.509",
             url="https://www.science.org/doi/10.1126/science.286.5439.509",
             language="en", isbn=None,
             citation="Barabasi, A.-L., & Albert, R. (1999). Emergence of scaling in random networks. Science, 286(5439), 509-512. https://doi.org/10.1126/science.286.5439.509",
             locator="286(5439):509-512", locator_type="page_range",
             supports="power-law degree distribution / growth and preferential attachment / hubs", verified=True),
        dict(kind="BOOK",
             title_en="Linked: The New Science of Networks",
             title_fa="پیوندها: علم نوین شبکه‌ها",
             authors="Barabasi, A.-L.", year=2002, publisher="Perseus",
             doi=None, url=None, language="en", isbn=None,
             citation="Barabasi, A.-L. (2002). Linked: The new science of networks. Perseus.",
             locator="work", locator_type="work",
             supports="robustness and vulnerability of scale-free networks", verified=False),
    ],
}

ENRICH = {
    "MC-517": {
        "summary": "(ونکاتش، موریس، دیویس و دیویس، ۲۰۰۳) نظریه یکپارچه پذیرش فناوری با ترکیب هشت مدل پیشین، چهار تعیین‌کننده اصلی پذیرش را معرفی کرد: انتظار عملکرد، انتظار تلاش، نفوذ اجتماعی و شرایط تسهیل‌کننده. این چهار عامل، قصد و استفاده از فناوری را پیش‌بینی می‌کنند و اثرشان با جنسیت، سن، تجربه و اختیاری‌بودن استفاده تعدیل می‌شود. مدل توانست بخش بزرگی از واریانس قصد رفتاری را توضیح دهد و به چارچوب مرجع پژوهش پذیرش فناوری بدل شد.",
        "definition": "نظریه یکپارچه پذیرش و استفاده از فناوری، مدلی است که با ترکیب مدل‌های پیشین، قصد و رفتار استفاده از فناوری را از چهار سازه انتظار عملکرد، انتظار تلاش، نفوذ اجتماعی و شرایط تسهیل‌کننده تبیین می‌کند.",
        "main_problem": "مسئله این است که چرا افراد فناوری‌های تازه را می‌پذیرند یا رد می‌کنند. مدل‌های پیشین، هر یک بخشی از پاسخ را داشتند؛ نظریه یکپارچه کوشید آن‌ها را در یک چارچوب جمع کند. پرسش دوم، تفاوت کاربران است: آیا همان عوامل برای زنان و مردان، جوانان و سالخوردگان و کاربران باتجربه و تازه‌کار یکسان عمل می‌کنند.",
        "mechanism": "۱. انتظار عملکرد: باور به اینکه فناوری، بهره‌وری یا کارایی فرد را بهبود می‌دهد؛ قوی‌ترین پیش‌بین قصد استفاده.\n۲. انتظار تلاش: درجه آسانی استفاده؛ هرچه فناوری کم‌دردسرتر باشد، پذیرش بیشتر است.\n۳. نفوذ اجتماعی: ادراک فرد از انتظار افراد مهم برای استفاده از فناوری.\n۴. شرایط تسهیل‌کننده: دسترسی به زیرساخت، آموزش و پشتیبانی که استفاده را ممکن می‌کند.\n۵. تعدیل‌گرها: جنسیت، سن، تجربه و اختیاری‌بودن، شدت اثر هر عامل را تغییر می‌دهند.\n۶. قصد و رفتار: قصد رفتاری، پیش‌بین استفاده است و شرایط تسهیل‌کننده، استفاده واقعی را تسهیل می‌کند.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا کاربران یک اپلیکیشن تازه را می‌پذیرند یا رها می‌کنند، چرا آموزش و پشتیبانی در پذیرش رسانه‌های دیجیتال تعیین‌کننده است و چرا فشار همکاران و مدیران در سازمان، استفاده را تسریع یا کند می‌کند. نکته مهم این است که مدل بر قصد و رفتار فردی متمرکز است و ساختار قدرت، محتوا و پیامدهای اجتماعی فناوری را کمتر می‌بیند.",
        "assumptions": [
            "پذیرش فناوری را می‌توان با چند سازه مشترک تبیین کرد.",
            "قصد رفتاری، پیش‌بین معتبر استفاده است.",
            "ویژگی‌های فردی، شدت اثر سازه‌ها را تعدیل می‌کنند.",
        ],
        "principles": [
            "بهره‌مندی ادراک‌شده، مهم‌ترین پیش‌بین پذیرش است.",
            "سهولت استفاده، شرط ورود و ماندن کاربر است.",
            "پشتیبانی و زیرساخت، فاصله قصد و رفتار را پر می‌کند.",
        ],
        "critiques": [
            "۱. تمرکز سازمانی: مدل بر کارکنان و فناوری اداری بنا شده است.\n۲. فرض عقلانیت: احساس، عادت و هویت در نسخه اولیه کم‌رنگ‌اند.\n۳. سنجش خودگزارشی: قصد و استفاده با پرسشنامه سنجیده می‌شود و سوگیری دارد.\n۴. زمینه غربی: نمونه‌ها به سازمان‌های آمریکایی محدود است.\n۵. تحول مصرف: پذیرش فناوری مصرفی و پلتفرمی به سازه‌های تازه نیاز داشت.",
        ],
        "applications": [
            "طراحی محصول: سنجش انتظار عملکرد و تلاش پیش از عرضه.",
            "آموزش دیجیتال: طراحی آموزش و پشتیبانی برای پذیرش فناوری.",
            "سیاست فناوری سازمانی: شناسایی موانع نفوذ اجتماعی و شرایط تسهیل‌کننده.",
            "پژوهش کاربر: پیش‌بینی قصد استفاده در گروه‌های مختلف.",
        ],
        "evolution": "مدل در ۲۰۰۳ با ترکیب هشت نظریه پذیرش معرفی شد و در ۲۰۱۲ با افزودن انگیزه لذت‌جویانه، ارزش قیمت و عادت به مصرف‌کننده گسترش یافت.",
        "key_concepts": [
            "انتظار عملکرد (Performance Expectancy)",
            "انتظار تلاش (Effort Expectancy)",
            "نفوذ اجتماعی (Social Influence)",
            "شرایط تسهیل‌کننده (Facilitating Conditions)",
            "قصد رفتاری (Behavioral Intention)",
            "تعدیل‌گرها (Moderators)",
        ],
        "studies": [
            "Venkatesh, V., Morris, M. G., Davis, G. B., & Davis, F. D. (2003). User acceptance of information technology. MIS Quarterly, 27(3), 425-478.",
            "Venkatesh, V., Thong, J. Y. L., & Xu, X. (2012). Consumer acceptance and use of information technology. MIS Quarterly, 36(1), 157-178.",
        ],
        "theorists": "ونکاتش، موریس، دیویس و دیویس (۲۰۰۳)",
        "theorists_text": "ونکاتش و همکاران (۲۰۰۳)",
        "year": 2003,
        "model": "مدل چهارسازه‌ای: انتظار عملکرد + انتظار تلاش + نفوذ اجتماعی → قصد رفتاری؛ شرایط تسهیل‌کننده → استفاده؛ با تعدیل جنسیت، سن، تجربه و اختیار.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nنظریه یکپارچه، حاصل مقایسه و ترکیب هشت مدل پذیرش بود. نوآوری آن، کاهش پراکندگی نظری به چهار سازه مشترک و نشان دادن نقش تعدیل‌گرها بود؛ ایده‌ای که پژوهش پذیرش فناوری را استاندارد کرد.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با پرسشنامه و مدل‌سازی معادلات ساختاری انجام می‌شود. پژوهش‌هایی که تنها قصد را می‌سنجند، شکاف قصد و رفتار را از دست می‌دهند؛ و پژوهش‌هایی که تنها استفاده را می‌سنجند، تفاوت انگیزه‌ها را نمی‌بینند.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در پیش‌بینی پذیرش است، اما محتوا، معنا و پیامد اجتماعی فناوری را توضیح نمی‌دهد. در محیط پلتفرمی، پذیرش به‌اندازه طراحی رابط و پشتیبانی، به شبکه همسالان و هنجارهای اجتماعی وابسته است.",
        "critique_text": "\n".join([
            "۱. تمرکز سازمانی: مدل بر کارکنان و فناوری اداری بنا شده است.",
            "۲. فرض عقلانیت: احساس، عادت و هویت در نسخه اولیه کم‌رنگ‌اند.",
            "۳. سنجش خودگزارشی: پرسشنامه، سوگیری پاسخ دارد.",
            "۴. زمینه غربی: نمونه‌ها به سازمان‌های آمریکایی محدود است.",
            "۵. تحول مصرف: پذیرش فناوری مصرفی به سازه‌های تازه نیاز داشت.",
        ]),
        "example_text": "سازمانی یک سامانه جلسه آنلاین را معرفی می‌کند. کارکنان مزیت آن را می‌پذیرند (انتظار عملکرد)، اما رابط پیچیده و نبود آموزش، استفاده را کم می‌کند. افزودن راهنما و پشتیبانی (شرایط تسهیل‌کننده) و حمایت مدیر (نفوذ اجتماعی)، فاصله میان قصد و استفاده را پر می‌کند.",
    },
    "MC-518": {
        "summary": "(گیبسون، ۱۹۷۹؛ نورمن، ۱۹۸۸؛ هاچبی، ۲۰۰۱) نظریه امکانات عمل می‌گوید محیط، فرصت‌های عمل را پیش روی موجود عرضه می‌کند و ادراک، این فرصت‌ها را مستقیم می‌بیند. نورمن مفهوم را به طراحی منتقل کرد: دستگیره در، امکان کشیدن را نشان می‌دهد و کاربر را راهنمایی می‌کند. هاچبی آن را به فناوری گسترد: هر فناوری، امکاناتی دارد که کنش را ممکن و هم محدود می‌کند؛ نه جبر فناورانه و نه ساخت کامل اجتماعی، بلکه چارچوب‌بندی رابطه‌ای. امکانات، کنش را ممکن می‌کنند، اما آن را تعیین نمی‌کنند.",
        "definition": "امکان عمل، ویژگی رابطه‌ای میان موجود و محیط یا فناوری است که فرصت‌های کنش را در دسترس ادراک قرار می‌دهد؛ مفهومی که از زیست‌شناسی ادراک به طراحی و سپس به جامعه‌شناسی فناوری منتقل شد.",
        "main_problem": "مسئله این است که رابطه انسان و فناوری چگونه فهم می‌شود: آیا فناوری کنش را تعیین می‌کند یا جامعه آن را می‌سازد. نظریه امکانات عمل راه میانه می‌جوید: فناوری، امکاناتی دارد که برخی کنش‌ها را آسان و برخی را دشوار می‌کند، اما معنای کنش در تعامل اجتماعی ساخته می‌شود. پرسش دوم، طراحی است: چگونه می‌توان امکانات را به‌گونه‌ای ساخت که کاربر بدون آموزش، کارکرد را بفهمد.",
        "mechanism": "۱. امکان عمل به‌عنوان رابطه: امکان، نه ویژگی صرف شیء است و نه ساخت صرف ذهن؛ رابطه‌ای میان ویژگی‌های شیء و توانایی‌های کاربر است.\n۲. ادراک مستقیم: موجود، فرصت‌های عمل را بدون استدلال پیچیده می‌بیند؛ صندلی، امکان نشستن را عرضه می‌کند.\n۳. امکانات ادراک‌شده در طراحی: طراحی خوب، امکان را در ظاهر شیء قابل فهم می‌کند و طراحی بد، سیگنال گمراه‌کننده می‌دهد.\n۴. قابلیت و محدودیت فناوری: هر فناوری، دامنه‌ای از کنش را ممکن و دامنه‌ای را دشوار یا ناممکن می‌کند.\n۵. عاملیت در چارچوب: کاربر آزاد است، اما در چارچوب امکاناتی که فناوری فراهم می‌کند؛ آزادی، مشروط است.\n۶. لایه اجتماعی امکانات: امکانات در بستر هنجار، مهارت و نهاد تفسیر می‌شوند و اثرشان تغییر می‌کند.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا رابط کاربری، رفتار کاربر را شکل می‌دهد، چرا پلتفرم‌ها با طراحی امکان، برخی کنش‌ها را تشویق می‌کنند و چرا تحلیل فناوری بدون تحلیل امکانات و زمینه اجتماعی ناقص است. نکته مهم این است که امکانات، فضای کنش را می‌سازند، نه نتیجه قطعی را.",
        "assumptions": [
            "امکانات عمل، رابطه‌ای و موقعیتی‌اند.",
            "ادراک، فرصت‌های عمل را در دسترس قرار می‌دهد.",
            "فناوری، کنش را چارچوب‌بندی می‌کند، نه تعیین.",
        ],
        "principles": [
            "طراحی خوب، امکان را قابل ادراک می‌کند.",
            "امکانات فناوری، هم توانمندساز و هم محدودکننده‌اند.",
            "معنای امکان، در زمینه اجتماعی ساخته می‌شود.",
        ],
        "critiques": [
            "۱. ابهام مفهومی: کاربرد مفهوم در زیست‌شناسی، طراحی و جامعه‌شناسی یکسان نیست.\n۲. انتقال بدون دقت: انتقال از ادراک حیوان به فناوری اجتماعی نیازمند تعدیل است.\n۳. خطر بازگشت جبرگرایی: تأکید بر امکانات می‌تواند به جبر فناورانه نرم بدل شود.\n۴. سنجش دشوار: تعیین امکانات یک فناوری، به زمینه و کاربر وابسته است.\n۵. پلتفرم پویا: امکانات الگوریتمی، پیوسته تغییر می‌کنند و چارچوب ثابتی ندارند.",
        ],
        "applications": [
            "طراحی رابط: ساخت امکانات قابل ادراک و کاهش خطای کاربر.",
            "تحلیل فناوری: بررسی توانمندسازی و محدودیت پلتفرم‌ها.",
            "آموزش دیجیتال: شناسایی امکانات و موانع استفاده.",
            "سیاست فناوری: تحلیل چگونگی شکل‌دهی طراحی به رفتار.",
        ],
        "evolution": "گیبسون مفهوم را در ۱۹۷۹ برای ادراک دیداری معرفی کرد؛ نورمن در ۱۹۸۸ آن را به طراحی منتقل کرد؛ و هاچبی در ۲۰۰۱ آن را به جامعه‌شناسی فناوری آورد تا راهی میانه میان جبر فناورانه و ساخت‌گرایی اجتماعی بسازد.",
        "key_concepts": [
            "امکان عمل (Affordance)",
            "امکان ادراک‌شده (Perceived Affordance)",
            "رابطه‌ای بودن (Relationality)",
            "چارچوب‌بندی کنش (Framing Action)",
            "طراحی کاربرمحور (User-Centered Design)",
            "عاملیت مشروط (Conditioned Agency)",
        ],
        "studies": [
            "Hutchby, I. (2001). Technologies, texts and affordances. Sociology, 35(2), 441-456.",
            "Gibson, J. J. (1979). The ecological approach to visual perception. Houghton Mifflin.",
            "Norman, D. A. (1988). The psychology of everyday things. Basic Books.",
        ],
        "theorists": "گیبسون؛ نورمن؛ هاچبی",
        "theorists_text": "جیمز گیبسون (۱۹۷۹)؛ دانلد نورمن (۱۹۸۸)؛ ایان هاچبی (۲۰۰۱)",
        "year": 1979,
        "model": "مدل رابطه‌ای: ویژگی‌های فناوری + توانایی و مهارت کاربر + زمینه اجتماعی → امکانات ادراک‌شده → دامنه کنش ممکن و دشوار.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nمفهوم امکان عمل، در برابر دوگانه جبر فناورانه و ساخت‌گرایی اجتماعی قرار می‌گیرد. نوآوری هاچبی این بود که نشان داد فناوری، هم قید دارد و هم انعطاف؛ کنش نه تعیین‌شده و نه بی‌قید است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش نیازمند تحلیل ویژگی‌های فناوری، مهارت کاربر و هنجار زمینه است. پژوهش‌هایی که تنها ویژگی فنی را می‌سنجند، تفسیر کاربر را از دست می‌دهند؛ و پژوهش‌هایی که تنها تجربه کاربر را می‌شنوند، قیدهای مادی را نمی‌بینند.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در پیوند طراحی و کنش است، اما باید با تحلیل قدرت و اقتصاد پلتفرم تکمیل شود. امکاناتی که پلتفرم فراهم می‌کند، با منافع تجاری و سنجه‌های الگوریتمی شکل می‌گیرند.",
        "critique_text": "\n".join([
            "۱. ابهام مفهومی: کاربرد مفهوم در سه حوزه یکسان نیست.",
            "۲. انتقال بدون دقت: نیازمند تعدیل برای فناوری اجتماعی است.",
            "۳. خطر بازگشت جبرگرایی: تأکید بر امکانات می‌تواند جبر نرم بسازد.",
            "۴. سنجش دشوار: امکانات به زمینه و کاربر وابسته‌اند.",
            "۵. پلتفرم پویا: امکانات الگوریتمی پیوسته تغییر می‌کنند.",
        ]),
        "example_text": "دکمه‌ای که برجسته و روشن است، امکان فشردن را نشان می‌دهد؛ دکمه‌ای که با متن مبهم و بی‌بازخورد طراحی شده، همان کارکرد را دارد اما امکان ادراک نمی‌شود. تفاوت، نه در فناوری، بلکه در طراحی رابطه میان شیء و کاربر است.",
    },
    "MC-519": {
        "summary": "(برنرز-لی، ۱۹۸۹) پیشنهاد «مدیریت اطلاعات» برنز-لی، نقطه آغاز وب به‌عنوان یک محیط اطلاعاتی است: فضایی پیوندی و توزیع‌شده که در آن هر سند می‌تواند به سند دیگر ارجاع دهد و مرز میان خواندن و نوشتن کم‌رنگ می‌شود. از این منظر، وب فقط مجموعه‌ای از صفحه‌ها نیست؛ محیطی است که دسترسی، جست‌وجو، تعامل و هویت را ساختار می‌دهد. نظریه وب به‌عنوان محیط، این ایده را بسط می‌دهد که وب شرایط امکان کنش اطلاعاتی را می‌سازد و نه فقط کانال انتقال پیام.",
        "definition": "نظریه وب به‌عنوان محیط، وب را فضایی اطلاعاتی و پیوندی می‌داند که با ساختار ابرمتنی و توزیع‌شده خود، شرایط دسترسی، تعامل و حضور را شکل می‌دهد و فراتر از کانال انتقال پیام عمل می‌کند.",
        "main_problem": "مسئله این است که وب چه چیزی را نسبت به رسانه‌های پیشین تغییر می‌دهد. پاسخ در ساختار محیط است: پیوند، توزیع و امکان نوشتن، رابطه کاربر با اطلاعات را از دریافت منفعل به حرکت و ساخت فعال تغییر می‌دهد. پرسش دوم، پیامد است: این محیط چه فرصت‌ها و چه محدودیت‌هایی برای دانش، هویت و قدرت می‌سازد.",
        "mechanism": "۱. فضای اطلاعاتی توزیع‌شده: اطلاعات در یک مکان متمرکز نیست و هر گره می‌تواند به گره دیگر ارجاع دهد.\n۲. پیوند و ابرمتن: ساختار پیوندی، مسیر خواندن را از خطی به شبکه‌ای تغییر می‌دهد.\n۳. خواندن و نوشتن: در وب، کاربر می‌تواند هم مصرف‌کننده و هم تولیدکننده محتوا باشد.\n۴. جست‌وجو و دسترسی: موتور جست‌وجو و پیوند، سازوکارهای اصلی یافتن اطلاعات‌اند و دستور کار آگاهی را شکل می‌دهند.\n۵. هویت و حضور: صفحه شخصی، نمایه و شبکه اجتماعی، شکل تازه‌ای از حضور و هویت می‌سازد.\n۶. محیط و زیرساخت: پروتکل، مرورگر و استاندارد، شرایط امکان کنش را تعیین می‌کنند.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا وب دسترسی به اطلاعات را دگرگون کرد، چرا پیوند و جست‌وجو به منابع قدرت بدل شدند و چرا انتقال از وب باز به پلتفرم بسته، پرسش تازه‌ای درباره محیط اطلاعاتی مطرح می‌کند. نکته مهم این است که طراحی اولیه وب، آرمان بازبودن داشت؛ اما محیط واقعی با مالکیت، الگوریتم و انحصار شکل گرفت.",
        "assumptions": [
            "وب، محیطی اطلاعاتی و نه فقط کانالی برای انتقال پیام است.",
            "ساختار پیوندی، الگوی دسترسی و خواندن را تغییر می‌دهد.",
            "امکان نوشتن، رابطه کاربر و محتوا را دگرگون می‌کند.",
        ],
        "principles": [
            "پیوند، واحد بنیادی ساختار وب است.",
            "بازبودن پروتکل، شرط رشد محیط است.",
            "دسترسی، تابع زیرساخت و سازوکار جست‌وجو است.",
        ],
        "critiques": [
            "۱. آرمان‌گرایی اولیه: فرض بازبودن و برابری دسترسی، با واقعیت پلتفرم فاصله داشت.\n۲. کم‌توجهی به قدرت: مالکیت زیرساخت و انحصار جست‌وجو کمتر تحلیل می‌شود.\n۳. تمرکز فنی: محیط وب بیشتر از منظر معماری دیده می‌شود.\n۴. سنجش محیط: اندازه‌گیری اثر محیطی وب دشوار است.\n۵. شکاف دسترسی: زبان، مهارت و زیرساخت، دسترسی را نابرابر می‌کند.",
        ],
        "applications": [
            "طراحی وب: توجه به ساختار پیوند و راهبری کاربر.",
            "سواد دیجیتال: آموزش حرکت و ارزیابی در محیط اطلاعاتی.",
            "سیاست اینترنت: تحلیل بازبودن و انحصار زیرساخت.",
            "مطالعات پلتفرم: بررسی انتقال از وب باز به محیط بسته.",
        ],
        "evolution": "برنز-لی در ۱۹۸۹ پیشنهاد وب را نوشت و در ۱۹۹۹ اصول طراحی آن را شرح داد. پژوهش بعدی، وب را به‌عنوان محیط اطلاعاتی، فضای اجتماعی و زیرساخت قدرت تحلیل کرد.",
        "key_concepts": [
            "محیط اطلاعاتی (Information Environment)",
            "ابرمتن (Hypertext)",
            "پیوند (Hyperlink)",
            "توزیع‌شدگی (Distributedness)",
            "بازبودن (Openness)",
            "حضور دیجیتال (Digital Presence)",
        ],
        "studies": [
            "Berners-Lee, T. (1989). Information management: A proposal. CERN.",
            "Berners-Lee, T., & Fischetti, M. (1999). Weaving the web. HarperSanFrancisco.",
        ],
        "theorists": "تیم برنرز-لی (۱۹۸۹)",
        "theorists_text": "تیم برنز-لی (۱۹۸۹)",
        "year": 1989,
        "model": "مدل محیطی: پروتکل و ابرمتن → فضای پیوندی توزیع‌شده → دسترسی، نوشتن و حضور → شرایط تازه کنش اطلاعاتی.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nپیشنهاد ۱۹۸۹ در اصل مسئله مدیریت اطلاعات سازمانی را حل می‌کرد، اما ساختار پیشنهادی — ابرمتن توزیع‌شده و باز — به محیطی جهانی بدل شد. نوآوری نظری، دیدن وب به‌عنوان محیط و نه فقط ابزار است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش نیازمند تحلیل ساختار پیوند، الگوی دسترسی و زیرساخت است. پژوهش‌هایی که تنها محتوای صفحه‌ها را می‌سنجند، ساختار محیط را از دست می‌دهند؛ و پژوهش‌هایی که تنها فناوری را می‌بینند، تجربه کاربر را نادیده می‌گیرند.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در نشان دادن ساختار محیط است، اما آرمان بازبودن را نباید با واقعیت اشتباه گرفت. در محیط پلتفرمی، ساختار پیوند و دسترسی به الگوریتم و مالکیت وابسته شده است.",
        "critique_text": "\n".join([
            "۱. آرمان‌گرایی اولیه: فرض بازبودن با واقعیت پلتفرم فاصله داشت.",
            "۲. کم‌توجهی به قدرت: انحصار زیرساخت و جست‌وجو کمتر تحلیل می‌شود.",
            "۳. تمرکز فنی: محیط بیشتر از منظر معماری دیده می‌شود.",
            "۴. سنجش محیط: اندازه‌گیری اثر محیطی وب دشوار است.",
            "۵. شکاف دسترسی: زبان و مهارت، دسترسی را نابرابر می‌کند.",
        ]),
        "example_text": "دانشجویی که پیش‌تر برای یافتن یک مقاله باید کتابخانه را می‌گشت، اکنون با پیوندها از یک سند به سند دیگر می‌رود و خودش فهرست و یادداشت می‌سازد. تغییر، نه فقط سرعت دسترسی، بلکه ساختار حرکت او در اطلاعات است.",
    },
    "MC-521": {
        "summary": "(باراباشی و آلبرت، ۱۹۹۹) باراباشی و آلبرت نشان دادند که بسیاری از شبکه‌های واقعی — وب، شبکه استناد و شبکه اجتماعی — توزیع درجه یکنواخت ندارند، بلکه از قانون توانی پیروی می‌کنند: شمار بسیار کمی گره، اتصال‌های بسیار زیاد دارند و بیشتر گره‌ها اتصال کم. دو سازوکار این ساختار را می‌سازد: رشد شبکه و اتصال ترجیحی؛ گره‌های پرتوصیل، سهم بیشتری از اتصال‌های تازه می‌گیرند. نتیجه، شبکه‌ای بدون مقیاس با گره‌های مرکزی است که در برابر حذف تصادفی مقاوم و در برابر حمله هدفمند آسیب‌پذیر است.",
        "definition": "شبکه بدون مقیاس، شبکه‌ای است که توزیع درجه آن از قانون توانی پیروی می‌کند و در آن شمار اندکی گره مرکزی، بخش بزرگی از اتصال‌ها را در اختیار دارند؛ ساختاری که از رشد و اتصال ترجیحی پدید می‌آید.",
        "main_problem": "مسئله این است که چرا شبکه‌های واقعی، ساختار نامتقارن دارند. مدل‌های تصادفی پیشین، توزیع یکنواخت پیش‌بینی می‌کردند؛ داده‌های واقعی، گره‌های مرکزی نیرومند نشان می‌دادند. پرسش دوم، پیامد است: این ساختار چه اثری بر پایداری، انتشار اطلاعات و قدرت گره‌ها دارد.",
        "mechanism": "۱. رشد: شبکه‌ها با افزودن گره‌های تازه شکل می‌گیرند و ثابت نمی‌مانند.\n۲. اتصال ترجیحی: گره تازه، با احتمال بیشتر به گره‌های پرتوصیل متصل می‌شود؛ ثروتمند ثروتمندتر می‌شود.\n۳. توزیع قانون توانی: احتمال وجود گره با درجه بسیار بالا کم است، اما صفر نیست؛ دنباله سنگین توزیع.\n۴. گره‌های مرکزی: شمار اندکی گره، بخش بزرگی از اتصال‌ها و جریان اطلاعات را کنترل می‌کنند.\n۵. مقاومت در برابر خطای تصادفی: حذف تصادفی گره‌ها، ساختار کلی را به‌سختی می‌شکند.\n۶. آسیب‌پذیری در برابر حمله هدفمند: حذف گره‌های مرکزی، شبکه را سریع از هم می‌پاشد.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا شمار اندکی از حساب‌ها و رسانه‌ها بیشترین توجه را جذب می‌کنند، چرا انتشار محتوا در شبکه‌های اجتماعی به گره‌های مرکزی وابسته است و چرا از کار افتادن یک پلتفرم بزرگ، اثر گسترده دارد. نکته مهم این است که مدل، ساختار اتصال را می‌سنجد و محتوا، معنا و قدرت نهادی را توضیح نمی‌دهد.",
        "assumptions": [
            "شبکه‌های واقعی با رشد و اتصال ترجیحی شکل می‌گیرند.",
            "توزیع درجه از قانون توانی پیروی می‌کند.",
            "ساختار اتصال، جریان اطلاعات و پایداری را تعیین می‌کند.",
        ],
        "principles": [
            "گره‌های مرکزی، جریان اطلاعات را کنترل می‌کنند.",
            "شبکه بدون مقیاس در برابر خطای تصادفی مقاوم است.",
            "حمله هدفمند به گره‌های مرکزی، شبکه را شکننده می‌کند.",
        ],
        "critiques": [
            "۱. نمونه‌گزینی: برخی شبکه‌ها قانون توانی ندارند یا دنباله بریده دارند.\n۲. فرض یکسان‌بودن سازوکار: رشد و اتصال ترجیحی برای همه شبکه‌ها کافی نیست.\n۳. برون‌یابی افراطی: نتیجه‌های ساختاری به فرایندهای اجتماعی تعمیم داده می‌شود.\n۴. کم‌توجهی به محتوا و معنا: ساختار اتصال به‌تنهایی رفتار شبکه را توضیح نمی‌دهد.\n۵. پویایی پلتفرم: الگوریتم و سیاست پلتفرم، ساختار را پیوسته تغییر می‌دهند.",
        ],
        "applications": [
            "تحلیل شبکه اجتماعی: شناسایی گره‌های مرکزی و مسیر انتشار.",
            "مدیریت بحران اطلاعاتی: تحلیل آسیب‌پذیری در برابر حمله هدفمند.",
            "استراتژی محتوا: شناخت نقش گره‌های مرکزی در گسترش پیام.",
            "مطالعات زیرساخت: تحلیل تمرکز و پایداری شبکه‌های ارتباطی.",
        ],
        "evolution": "مدل در ۱۹۹۹ با داده‌های وب و شبکه استناد معرفی شد و در دهه بعد به تحلیل شبکه‌های اجتماعی، زیستی و زیرساختی گسترد. پژوهش بعدی، محدودیت قانون توانی و نقش محتوا را نشان داد.",
        "key_concepts": [
            "شبکه بدون مقیاس (Scale-Free Network)",
            "قانون توانی (Power Law)",
            "اتصال ترجیحی (Preferential Attachment)",
            "گره مرکزی (Hub)",
            "دنباله سنگین (Heavy Tail)",
            "حمله هدفمند (Targeted Attack)",
        ],
        "studies": [
            "Barabasi, A.-L., & Albert, R. (1999). Emergence of scaling in random networks. Science, 286(5439), 509-512.",
            "Barabasi, A.-L. (2002). Linked: The new science of networks. Perseus.",
        ],
        "theorists": "باراباشی و آلبرت (۱۹۹۹)",
        "theorists_text": "باراباشی و آلبرت (۱۹۹۹)",
        "year": 1999,
        "model": "مدل رشد و اتصال ترجیحی: افزودن گره تازه + اتصال به گره‌های پرتوصیل → توزیع قانون توانی → گره‌های مرکزی → مقاومت به خطا و آسیب‌پذیری به حمله.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nمدل، نظریه شبکه‌های تصادفی را به چالش کشید و نشان داد که ساختار شبکه‌های واقعی، محصول تاریخ رشد و ترجیح اتصال است. نوآوری آن، پیوند سادگی سازوکار با پیچیدگی ساختار بود.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با تحلیل توزیع درجه و شبیه‌سازی حذف گره انجام می‌شود. پژوهش‌هایی که تنها توزیع درجه را می‌سنجند، پویایی انتشار را از دست می‌دهند؛ و پژوهش‌هایی که تنها یک شبکه را تحلیل می‌کنند، تعمیم را دشوار می‌سازند.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در توضیح تمرکز و پایداری شبکه است، اما محتوا و قدرت نهادی را توضیح نمی‌دهد. در محیط پلتفرمی، الگوریتم توصیه، اتصال ترجیحی را تشدید می‌کند و ساختار مرکزی تازه‌ای می‌سازد.",
        "critique_text": "\n".join([
            "۱. نمونه‌گزینی: برخی شبکه‌ها قانون توانی ندارند.",
            "۲. فرض یکسان‌بودن سازوکار: رشد و ترجیح برای همه کافی نیست.",
            "۳. برون‌یابی افراطی: نتیجه ساختاری به فرایند اجتماعی تعمیم می‌یابد.",
            "۴. کم‌توجهی به محتوا: ساختار اتصال رفتار را توضیح نمی‌دهد.",
            "۵. پویایی پلتفرم: الگوریتم ساختار را پیوسته تغییر می‌دهد.",
        ]),
        "example_text": "در یک شبکه اجتماعی، چند حساب پرمخاطب بیشتر پیوندها و بازنشرها را جذب می‌کنند. حذف تصادفی چند حساب کوچک، شبکه را نمی‌شکند؛ اما بسته‌شدن دو حساب مرکزی، جریان اطلاعات را به‌شدت مختل می‌کند.",
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
                                       "verified": n_verified, "batch": 94}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH94 THEORY DONE")


if __name__ == "__main__":
    main()
