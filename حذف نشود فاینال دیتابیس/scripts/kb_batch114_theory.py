# -*- coding: utf-8 -*-
"""Batch 114: full documentation for MC-585, MC-664, MC-671, MC-676."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch114-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch114_theory.json"

S = {
    "MC-585": [
        dict(kind="BOOK",
             title_en="Managing Public Relations",
             title_fa="مدیریت روابط عمومی",
             authors="Grunig, J. E.; Hunt, T.", year=1984,
             publisher="Holt, Rinehart and Winston",
             doi=None,
             url="https://www.researchgate.net/profile/James-Grunig/publication/322802009_Managing_Public_Relations",
             language="en", isbn=None,
             citation="Grunig, J. E., & Hunt, T. (1984). Managing public relations. Holt, Rinehart and Winston.",
             locator="work", locator_type="work",
             supports="situational theory of publics applied to public relations management", verified=True),
        dict(kind="BOOK_CHAPTER",
             title_en="A Situational Theory of Publics: Conceptual History, Recent Challenges and New Research",
             title_fa="نظریه وضعیتی عمومی‌ها: تاریخ مفهومی، چالش‌های تازه و پژوهش نو",
             authors="Grunig, J. E.", year=1997,
             publisher="International Thomson Business Press",
             doi=None, url=None, language="en", isbn=None,
             citation="Grunig, J. E. (1997). A situational theory of publics: Conceptual history, recent challenges and new research. In D. Moss, T. MacManus, & D. Verčič (Eds.), Public relations research: An international perspective (pp. 3-48). International Thomson Business Press.",
             locator="pp. 3-48", locator_type="page_range",
             supports="conceptual history and referent criterion revision of the theory", verified=False),
    ],
    "MC-664": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Influentials, Networks, and Public Opinion Formation",
             title_fa="تأثیرگذاران، شبکه‌ها و شکل‌گیری افکار عمومی",
             authors="Watts, D. J.; Dodds, P. S.", year=2007,
             publisher="Journal of Consumer Research",
             doi=None,
             url="https://academic.oup.com/jcr/article/34/4/441/1820236",
             language="en", isbn=None,
             citation="Watts, D. J., & Dodds, P. S. (2007). Influentials, networks, and public opinion formation. Journal of Consumer Research, 34(4), 441-458.",
             locator="34(4):441-458", locator_type="page_range",
             supports="large cascades can arise without influentials; threshold and network structure explain diffusion", verified=True),
        dict(kind="BOOK",
             title_en="Personal Influence: The Part Played by People in the Flow of Mass Communications",
             title_fa="نفوذ شخصی: نقش افراد در جریان ارتباطات جمعی",
             authors="Katz, E.; Lazarsfeld, P. F.", year=1955,
             publisher="Free Press",
             doi=None, url=None, language="en", isbn=None,
             citation="Katz, E., & Lazarsfeld, P. F. (1955). Personal influence: The part played by people in the flow of mass communications. Free Press.",
             locator="work", locator_type="work",
             supports="two-step flow and the influentials hypothesis", verified=False),
    ],
    "MC-671": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Privacy as Contextual Integrity",
             title_fa="حریم خصوصی به‌عنوان یکپارچگی زمینه‌ای",
             authors="Nissenbaum, H.", year=2004,
             publisher="Washington Law Review",
             doi=None,
             url="https://digitalcommons.law.uw.edu/wlr/vol79/iss1/10/",
             language="en", isbn=None,
             citation="Nissenbaum, H. (2004). Privacy as contextual integrity. Washington Law Review, 79(1), 119-158.",
             locator="79(1):119-158", locator_type="page_range",
             supports="privacy as appropriate flow of information under contextual norms", verified=True),
        dict(kind="BOOK",
             title_en="Privacy in Context: Technology, Policy, and the Integrity of Social Life",
             title_fa="حریم خصوصی در بافت: فناوری، سیاست و یکپارچگی زندگی اجتماعی",
             authors="Nissenbaum, H.", year=2010,
             publisher="Stanford University Press",
             doi=None, url=None, language="en", isbn=None,
             citation="Nissenbaum, H. (2010). Privacy in context: Technology, policy, and the integrity of social life. Stanford University Press.",
             locator="work", locator_type="work",
             supports="book-length development of the contextual integrity framework", verified=False),
    ],
    "MC-676": [
        dict(kind="BOOK",
             title_en="Cold Intimacies: The Making of Emotional Capitalism",
             title_fa="صمیمیت سرد: ساخت سرمایه‌داری عاطفی",
             authors="Illouz, E.", year=2007, publisher="Polity",
             doi=None,
             url="https://www.politybooks.com/bookdetail?book_slug=cold-intimacies-the-making-of-emotional-capitalism--9780745639048",
             language="en", isbn=None,
             citation="Illouz, E. (2007). Cold intimacies: The making of emotional capitalism. Polity.",
             locator="work", locator_type="work",
             supports="emotional capitalism: fusion of emotional and economic language", verified=True),
        dict(kind="BOOK",
             title_en="The Managed Heart: Commercialization of Human Feeling",
             title_fa="قلب مدیریت‌شده: کالایی‌شدن احساس انسانی",
             authors="Hochschild, A. R.", year=1983,
             publisher="University of California Press",
             doi=None,
             url="https://www.jstor.org/stable/10.1525/j.ctt1pn9bk",
             language="en", isbn=None,
             citation="Hochschild, A. R. (1983). The managed heart: Commercialization of human feeling. University of California Press.",
             locator="work", locator_type="work",
             supports="emotional labor and feeling rules in service work", verified=False),
    ],
}

ENRICH = {
    "MC-585": {
        "summary": "نظریه وضعیتی عمومی‌ها، که گرونیگ آن را در دهه ۱۹۶۰ صورت‌بندی کرد، توضیح می‌دهد چرا بخش‌های مختلف یک جامعه درباره یک مسئله واحد به شکل‌های متفاوت ارتباط برقرار می‌کنند. گرونیگ سه متغیر مستقل را معرفی کرد: تشخیص مسئله، تشخیص محدودیت و سطح درگیری. ترکیب این سه، مخاطب را به چهار گونه تقسیم می‌کند: عمومی فعال، عمومی آگاه، عمومی نهفته و عمومی بی‌تفاوت. عمومی فعال مسئله را می‌بیند، مانع را کم می‌داند و برای کنش سازمان می‌یابد؛ عمومی نهفته، مسئله را می‌بیند اما مانع را چنان سنگین می‌داند که اقدام نمی‌کند. نظریه، ارتباط جمعی را نه واکنش یکدست توده، بلکه پیامد موقعیت ادراک‌شده گروه می‌داند. گرونیگ و هانت در ۱۹۸۴ چارچوب را در مدیریت روابط عمومی به کار بستند و در بازنگری‌های بعدی، معیار مرجع نیز به مدل افزوده شد. در محیط شبکه‌ای، نظریه توضیح می‌دهد چرا یک بحران برای گروهی مسئله است و برای گروهی دیگر نه، و چرا کمپین همگانی به جای مشارکت، بی‌تفاوتی می‌سازد. اهمیت عملی آن، بخش‌بندی عمومی بر پایه ادراک است، نه جمعیت‌شناسی صرف؛ و همین نگاه، ارزیابی کمپین را از شمار پیام به کیفیت کنش عمومی می‌برد.",
        "definition": "نظریه وضعیتی عمومی‌ها چارچوبی است که ظهور عمومی فعال را پیامد سه ادراک می‌داند: تشخیص مسئله، تشخیص محدودیت و سطح درگیری، و ارتباط را بر پایه موقعیت ادراک‌شده گروه، نه ویژگی‌های جمعیت‌شناختی، توضیح می‌دهد.",
        "main_problem": "مسئله این است که چرا پیام یکسان در یک گروه کنش و در گروهی دیگر بی‌تفاوتی می‌سازد. پاسخ، ادراک موقعیتی گروه است. پرسش دوم، کاربرد است: سازمان چگونه عمومی فعال را پیش از بحران شناسایی کند تا پیام به جای همگان، به همان گروه برسد.",
        "mechanism": "۱. تشخیص مسئله: گروه می‌فهمد موضوعی بر زندگی‌اش اثر دارد.\n۲. تشخیص محدودیت: مانع‌های قانونی، مالی یا روانی سنجیده می‌شود.\n۳. سطح درگیری: موضوع چقدر به منافع نزدیک گروه گره خورده است.\n۴. گونه‌بندی: ترکیب سه متغیر، عمومی فعال، آگاه، نهفته یا بی‌تفاوت می‌سازد.\n۵. جست‌وجوی اطلاعات: عمومی فعال به دنبال داده می‌رود و آن را پردازش می‌کند.\n۶. کنش: کاهش مانع تشخیص‌داده‌شده، احتمال سازمان‌یابی را بالا می‌برد.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا پیام سلامت برای گروهی مسئله است و برای گروهی دیگر تبلیغی بی‌ربط، چرا بحران سازمانی پیش از انفجار عمومی نشانه‌های ادراکی دارد و چرا روزنامه‌نگاری که تنها شمار مخاطب را می‌سنجد، عموم فعال را از دست می‌دهد. نکته مهم این است که تشخیص محدودیت، سازوکاری محافظه‌کار است: گروهی که مانع را بزرگ می‌بیند، حتی با آگاهی بالا کنش نمی‌کند؛ از این رو، کاهش مانع ادراک‌شده گاه مؤثرتر از تکرار پیام است.",
        "assumptions": [
            "عمومی، گروهی موقعیتی است نه توده یکدست.",
            "ادراک گروه، کنش ارتباطی را تعیین می‌کند.",
            "سه متغیر مستقل، قابل تفکیک و سنجش‌اند.",
        ],
        "principles": [
            "مسئله ادراک‌شده، نه شدت عینی، انگیزه کنش است.",
            "مانع ادراک‌شده، آگاهی را به بی‌عملی بدل می‌کند.",
            "بخش‌بندی بر پایه ادراک، مؤثرتر از جمعیت‌شناسی است.",
        ],
        "critiques": [
            "۱. سنجش: ادراک گروه با پیمایش سنجیده می‌شود و پاسخ‌دهندگان اغلب ادراک خود را دقیق گزارش نمی‌کنند.\n۲. ایستایی: مدل، تک‌رویداد است و پویایی طولانی بحران را کم توضیح می‌دهد.\n۳. فرهنگ: هنجارهای محلی و اعتماد نهادی در مدل کم‌رنگ‌اند.\n۴. دیجیتال: شبکه اجتماعی، مرز عمومی فعال و نهفته را پیوسته جابه‌جا می‌کند.\n۵. قدرت: نقش منابع رسانه‌ای در ساختن تشخیص مسئله کم دیده می‌شود.",
        ],
        "applications": [
            "روابط عمومی: شناسایی عمومی پیش از بحران.",
            "بهداشت عمومی: کاهش مانع ادراک‌شده به جای تکرار پیام.",
            "کمپین سیاسی: بخش‌بندی بر پایه درگیری.",
            "سنجش کمپین: کنش عمومی به جای شمار پیام.",
        ],
        "evolution": "گرونیگ در دهه ۱۹۶۰ نظریه را بر پایه کار دیویی درباره عمومی صورت‌بندی کرد، گرونیگ و هانت آن را در ۱۹۸۴ به مدیریت روابط عمومی آوردند و بازنگری ۱۹۹۷ معیار مرجع و چالش‌های تازه را افزود. پژوهش ارتباط بحران، مدل را به شبکه اجتماعی گسترد.",
        "key_concepts": [
            "تشخیص مسئله (Problem Recognition)",
            "تشخیص محدودیت (Constraint Recognition)",
            "سطح درگیری (Level of Involvement)",
            "عمومی فعال (Active Public)",
            "عمومی نهفته (Latent Public)",
            "معیار مرجع (Referent Criterion)",
        ],
        "studies": [
            "Grunig, J. E., & Hunt, T. (1984). Managing public relations. Holt, Rinehart and Winston.",
            "Grunig, J. E. (1997). A situational theory of publics. In Public relations research (pp. 3-48). International Thomson Business Press.",
        ],
        "theorists": "جیمز ای. گرونیگ؛ تاد هانت",
        "theorists_text": "گرونیگ (دهه ۱۹۶۰)؛ گرونیگ و هانت (۱۹۸۴)",
        "year": 1968,
        "model": "سه ادراک (مسئله، محدودیت، درگیری) → گونه عمومی → جست‌وجوی اطلاعات و کنش.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nگرونیگ مفهوم عمومی را از فلسفه عملگرا و کار دیویی وام گرفت و آن را به سه متغیر ادراکی فروکاست. نوآوری چارچوب، جایگزینی توده با گروه موقعیتی است؛ عمومی چیزی نیست که کسی عضوش باشد، بلکه وضعیتی است که گروه در آن قرار می‌گیرد.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با پیمایش سه متغیر و تحلیل کنش انجام می‌شود. پژوهشی که تنها نگرش را می‌سنجد، تشخیص محدودیت را از دست می‌دهد؛ و پژوهشی که هر گروه آگاه را فعال می‌خواند، فاصله آگاهی و کنش را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در پیش‌بینی مشارکت است، اما باید با تحلیل منابع و اعتماد نهادی تکمیل شود. کمپینی که مانع را نمی‌شناسد، پیام را تکرار می‌کند و بی‌عملی می‌سازد.",
        "critique_text": "\n".join([
            "۱. سنجش: گزارش ادراک اغلب دقیق نیست.",
            "۲. ایستایی: پویایی بحران کم توضیح داده می‌شود.",
            "۳. فرهنگ: هنجار محلی کم‌رنگ است.",
            "۴. دیجیتال: مرز گونه‌ها جابه‌جا می‌شود.",
            "۵. قدرت: نقش منابع رسانه کم دیده می‌شود.",
        ]),
        "example_text": "شهری که طرح جدید ترافیک را تهدید معیشت می‌داند، عمومی فعال می‌سازد؛ در محله‌ای دیگر همان طرح مسئله‌ای دور می‌ماند و پیام یکسان، دو واکنش متفاوت می‌گیرد.",
    },
    "MC-664": {
        "summary": "نظریه برجستگی و نفوذ به این پرسش پاسخ می‌دهد که آیا انتشار گسترده یک عقیده محصول چند فرد بسیار تأثیرگذار است یا پیامد ساختار شبکه و آستانه پذیرش افراد. فرضیه تأثیرگذاران می‌گفت اقلیتی آگاه، جریان اطلاعات را به راه می‌اندازند؛ همان منطقی که کاتز و لازارسفلد در ۱۹۵۵ با جریان دو مرحله‌ای ارتباط صورت‌بندی کردند. واتس و دادز در ۲۰۰۷ با شبیه‌سازی نشان دادند آبشارهای بزرگ تأثیر بدون تأثیرگذاران نیز ممکن است: اگر شمار زیادی از افراد به‌راحتی پذیرا باشند، پیام از راه انبوه افراد معمولی نیز گسترش می‌یابد. پس برجستگی یک موضوع تنها به فرستنده قدرتمند وابسته نیست؛ به آستانه‌های پذیرش، چگالی پیوندها و موقعیت گره در شبکه بستگی دارد. نظریه، صنعت تأثیرگذاری دیجیتال را نسبی می‌کند: هوادار زیاد تضمین نفوذ نیست و نفوذ واقعی به بافت شبکه‌ای وابسته است. همچنین نشان می‌دهد سیاست‌گذاری رسانه‌ای که تنها چند صدا را تقویت می‌کند، ممکن است شبکه را از مسیرهای پخش طبیعی محروم کند. اهمیت چارچوب، جابه‌جایی کانون از ویژگی فرد تأثیرگذار به ساختار رابطه‌هاست و همین جابه‌جایی، سنجش کمپین را از شمار هوادار به الگوی انتشار می‌برد.",
        "definition": "برجستگی و نفوذ، چارچوبی است که گسترش یک عقیده را پیامد ترکیب آستانه پذیرش افراد، ساختار پیوندهای شبکه و موقعیت گره‌ها می‌داند و نقش تعیین‌کننده اقلیت تأثیرگذار را نسبی می‌کند.",
        "main_problem": "مسئله این است که چرا برخی عقیده‌ها در شبکه می‌گسترد و برخی می‌مانند. پاسخ نخست، تأثیرگذاران بود؛ پاسخ واتس و دادز، آستانه و ساختار است. پرسش دوم، سنجش است: نفوذ یک گره را چگونه می‌توان جدا از بخت شبکه‌اش سنجید.",
        "mechanism": "۱. آستانه پذیرش: هر فرد با شمار معینی از مواجهه، عقیده را می‌پذیرد.\n۲. چگالی پیوند: شبکه متراکم، آستانه مؤثر را پایین می‌آورد.\n۳. موقعیت گره: گره میان‌بینی، مسیر انتشار را کوتاه می‌کند.\n۴. آبشار: زنجیره پذیرش، پیام را به گره‌های دور می‌رساند.\n۵. برجستگی: موضوعی که تکرار شبکه‌ای می‌گیرد، مهم تلقی می‌شود.\n۶. نسبی‌بودن نفوذ: گره پرپیوند، تنها در بافت مناسب مؤثر است.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا کمپین با چند چهره مشهور گاه شکست می‌خورد، چرا محتوای معمولی در شبکه متراکم می‌گیرد و چرا برجستگی موضوع با الگوی انتشار سنجیده می‌شود. نکته مهم این است که نفوذ، ویژگی ثابت فرد نیست؛ موقعیتی است که از تلاقی آستانه‌ها و ساختار برمی‌خیزد؛ از این رو، برچسب «تأثیرگذار» بدون سنجش بافت، ادعایی بیش نیست.",
        "assumptions": [
            "پذیرش عقیده، آستانه‌ای است.",
            "ساختار شبکه، مسیر انتشار را تعیین می‌کند.",
            "آبشار بزرگ بدون اقلیت تأثیرگذار ممکن است.",
        ],
        "principles": [
            "نفوذ، رابطه‌ای و موقعیتی است.",
            "آستانه پایین جمعی، جایگزین تأثیرگذار است.",
            "برجستگی را باید با الگوی انتشار سنجید.",
        ],
        "critiques": [
            "۱. سنجش: آستانه پذیرش در میدان سخت اندازه‌گیری می‌شود.\n۲. داده: شبیه‌سازی، پیچیدگی فرهنگی شبکه واقعی را ساده می‌کند.\n۳. زمان: پویایی بلندمدت آبشار کم بررسی شده است.\n۴. پلتفرم: الگوریتم، ساختار پیوند را دستکاری می‌کند.\n۵. تعمیم: یافته‌ها بیشتر بر شبکه‌های کوچک آزمایشی تکیه دارند.",
        ],
        "applications": [
            "بازاریابی: سنجش الگوی انتشار به جای شمار هوادار.",
            "کمپین عمومی: تقویت آستانه‌های پایین جمعی.",
            "پژوهش شبکه: تحلیل گره میان‌بینی.",
            "سواد رسانه: نسبی‌بودن برچسب تأثیرگذار.",
        ],
        "evolution": "کاتز و لازارسفلد در ۱۹۵۵ جریان دو مرحله‌ای را صورت‌بندی کردند و فرضیه تأثیرگذاران از آن برآمد. واتس و دادز در ۲۰۰۷ با شبیه‌سازی آن را نسبی کردند و پژوهش شبکه پلتفرمی، آستانه و الگوریتم را افزود.",
        "key_concepts": [
            "آستانه پذیرش (Adoption Threshold)",
            "آبشار اطلاعات (Information Cascade)",
            "چگالی شبکه (Network Density)",
            "گره میان‌بین (Betweenness)",
            "فرضیه تأثیرگذاران (Influentials Hypothesis)",
            "برجستگی موضوع (Issue Salience)",
        ],
        "studies": [
            "Watts, D. J., & Dodds, P. S. (2007). Influentials, networks, and public opinion formation. Journal of Consumer Research, 34(4), 441-458.",
            "Katz, E., & Lazarsfeld, P. F. (1955). Personal influence. Free Press.",
        ],
        "theorists": "دانکن واتس؛ پیتر دادز؛ الیهو کاتز؛ پل لازارسفلد",
        "theorists_text": "واتس و دادز (۲۰۰۷)؛ کاتز و لازارسفلد (۱۹۵۵)",
        "year": 2007,
        "model": "آستانه پذیرش + ساختار پیوند → آبشار انتشار → برجستگی موضوع در شبکه.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nواتس و دادز فرضیه تأثیرگذاران را به مدل آستانه‌ای شبکه پیوند زدند. نوآوری چارچوب، نشان‌دادن این نکته است که آبشار بزرگ، به تأثیرگذار بزرگ نیاز ندارد.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با شبیه‌سازی، تحلیل شبکه و داده انتشار انجام می‌شود. پژوهشی که تنها شمار هوادار را می‌سنجد، ساختار را از دست می‌دهد؛ و پژوهشی که هر آبشار را به یک گره نسبت می‌دهد، بخت شبکه را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در نقد صنعت تأثیرگذاری است، اما باید با داده پلتفرم واقعی تکمیل شود. تأثیرگذار بی بافت، به افسانه بازار بدل می‌شود.",
        "critique_text": "\n".join([
            "۱. سنجش: آستانه در میدان سخت اندازه‌پذیر است.",
            "۲. داده: شبیه‌سازی، فرهنگ را ساده می‌کند.",
            "۳. زمان: پویایی بلندمدت کم بررسی شده است.",
            "۴. پلتفرم: الگوریتم ساختار را دستکاری می‌کند.",
            "۵. تعمیم: شبکه‌های آزمایشی کوچک‌اند.",
        ]),
        "example_text": "یک ویدئوی ساده در گروهی از دانشجویان می‌چرخد و به شهر می‌رسد، بی آنکه هیچ چهره مشهوری آن را بازنشر کند؛ آستانه پایین جمعی، جای تأثیرگذار را گرفته است.",
    },
    "MC-671": {
        "summary": "نظریه یکپارچگی زمینه‌ای، که نیسنباوم آن را در ۲۰۰۴ صورت‌بندی کرد، حریم خصوصی را نه پنهان‌بودن اطلاعات، بلکه جریان مناسب اطلاعات در بافت تعریف می‌کند. هر بافت اجتماعی هنجار اطلاعاتی خود را دارد: چه کسی می‌فرستد، چه کسی می‌گیرد، چه داده‌ای مبادله می‌شود و با چه شرطی. نقض حریم خصوصی زمانی رخ می‌دهد که جریان داده از این هنجارها بیرون بزند، حتی اگر اطلاعات پیش‌تر عمومی بوده باشد. چارچوب توضیح می‌دهد چرا انتشار داده پزشکی در یک نشریه تخصصی نقض نیست، اما فروش همان داده به شرکت تبلیغاتی نقض است. در عصر پلتفرم، نظریه ابزار طراحی و سیاست‌گذاری است: تغییر هدف داده، تغییر بافت است و باید با تناسب و رضایت سنجیده شود. نیسنباوم بعدها چارچوب را در کتاب حریم خصوصی در بافت گسترد. نقد اصلی، ابهام هنجار بافت و کندی آن در برابر جریان‌های داده تازه است. اهمیت عملی نظریه، جابه‌جایی پرسش از «آیا داده عمومی است» به «آیا جریان داده با بافت می‌خواند» است و همین جابه‌جایی، ارزیابی پلتفرم را دقیق‌تر می‌کند.",
        "definition": "یکپارچگی زمینه‌ای، معیاری برای حریم خصوصی است که درست‌بودن جریان اطلاعات را با هنجارهای بافت اجتماعی می‌سنجد؛ نه با عمومی یا خصوصی بودن داده.",
        "main_problem": "مسئله این است که چرا داده عمومی نیز می‌تواند حریم خصوصی را نقض کند. پاسخ، جابه‌جایی بافت است. پرسش دوم، طراحی است: پلتفرم چگونه جریان داده را با هنجار بافت هم‌تراز کند.",
        "mechanism": "۱. بافت: حوزه اجتماعی با هدف، نقش و هنجار مشخص.\n۲. بازیگران: فرستنده، گیرنده و موضوع داده.\n۳. صفت: نوع داده‌ای که مبادله می‌شود.\n۴. اصل انتقال: شرط مجاز بودن جریان داده.\n۵. ارزیابی: مقایسه جریان واقعی با هنجار بافت.\n۶. نقض: خروج داده از شرط، حتی بدون آسیب آشکار.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا ردیابی رفتاری در فروشگاه با تبلیغات هدفمند تفاوت دارد، چرا انتشار داده سلامت در گروه بسته با فروش آن یکی نیست و چرا رضایت کلی، جانشین تناسب بافتی نمی‌شود. نکته مهم این است که هنجار بافت ثابت نیست؛ با فناوری تغییر می‌کند و همین پویایی، سنجش را به گفت‌وگوی عمومی نیازمند می‌کند؛ از این رو، طراحی حریم خصوصی باید فرایندی و مشارکتی باشد، نه فهرستی از موافقت‌نامه‌ها.",
        "assumptions": [
            "بافت اجتماعی هنجار اطلاعاتی دارد.",
            "جریان داده، مستقل از محتوا ارزیابی می‌شود.",
            "نقض حریم خصوصی، نقض هنجار بافت است.",
        ],
        "principles": [
            "عمومی بودن داده، مجوز هر جریان نیست.",
            "تناسب، معیار اصلی انتقال داده است.",
            "رضایت بدون تناسب کافی نیست.",
        ],
        "critiques": [
            "۱. ابهام: هنجار بافت اغلب صریح نیست.\n۲. پویایی: بافت دیجیتال سریع تغییر می‌کند.\n۳. فرهنگ: هنجارها میان جوامع متفاوت‌اند.\n۴. قدرت: هنجار غالب، منافع بازیگر قوی را بازتولید می‌کند.\n۵. اجرا: تبدیل هنجار به قاعده فنی دشوار است.",
        ],
        "applications": [
            "حکمرانی داده: ارزیابی تناسب جریان داده.",
            "طراحی پلتفرم: تفکیک بافت مصرف داده.",
            "سلامت دیجیتال: حفاظت داده حساس.",
            "سیاست رسانه: نقد استفاده ثانویه از داده.",
        ],
        "evolution": "نیسنباوم در ۲۰۰۴ حریم خصوصی را به‌عنوان یکپارچگی زمینه‌ای صورت‌بندی کرد و در ۲۰۱۰ چارچوب را در کتابی مستقل گسترد. پژوهش حکمرانی الگوریتمی، آن را به ارزیابی داده پلتفرمی پیوند زد.",
        "key_concepts": [
            "بافت (Context)",
            "هنجار اطلاعاتی (Informational Norm)",
            "اصل انتقال (Transmission Principle)",
            "تناسب (Appropriateness)",
            "بازیگر داده (Data Actor)",
            "جابه‌جایی بافت (Context Shift)",
        ],
        "studies": [
            "Nissenbaum, H. (2004). Privacy as contextual integrity. Washington Law Review, 79(1), 119-158.",
            "Nissenbaum, H. (2010). Privacy in context. Stanford University Press.",
        ],
        "theorists": "هلن نیسنباوم",
        "theorists_text": "نیسنباوم (۲۰۰۴، ۲۰۱۰)",
        "year": 2004,
        "model": "بافت و هنجار → بازیگران و صفت داده → اصل انتقال → ارزیابی تناسب یا نقض.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nنیسنباوم حریم خصوصی را از دوقطبی عمومی و خصوصی بیرون آورد و آن را به هنجار بافت گره زد. نوآوری چارچوب، سنجش جریان داده به جای سنجش مالکیت داده است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با تحلیل بافت، مصاحبه با کاربران و بازبینی طراحی انجام می‌شود. پژوهشی که تنها رضایت‌نامه را می‌خواند، هنجار بافت را از دست می‌دهد؛ و پژوهشی که هر مبادله داده را نقض می‌خواند، تفاوت بافت‌ها را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در نقد داده‌کشی پلتفرم است، اما باید با تحلیل قدرت تکمیل شود. هنجار بی مشارکت، به پوشش منافع غالب بدل می‌شود.",
        "critique_text": "\n".join([
            "۱. ابهام: هنجار بافت صریح نیست.",
            "۲. پویایی: بافت دیجیتال سریع تغییر می‌کند.",
            "۳. فرهنگ: هنجارها متفاوت‌اند.",
            "۴. قدرت: هنجار غالب بازتولید می‌شود.",
            "۵. اجرا: قاعده فنی‌سازی دشوار است.",
        ]),
        "example_text": "گزارش پزشکی یک بیمار در کنفرانس تخصصی پذیرفتنی است، اما همان گزارش در تبلیغ بیمه، بافت را می‌شکند و بی آنکه داده تازه‌ای افشا شود، حریم خصوصی را نقض می‌کند.",
    },
    "MC-676": {
        "summary": "نظریه اقتصاد عاطفی می‌گوید سرمایه‌داری معاصر، احساس را به زبان مشترک بازار و زندگی خصوصی بدل کرده است. ایلوز در ۲۰۰۷ نشان داد زبان درمانی، مدیریت احساس و سنجش رابطه از محل کار به صمیمیت و از آنجا به رسانه رسوخ می‌کند؛ در نتیجه، عاطفه هم کالا می‌شود و هم سرمایه. هوشیلد پیش‌تر در ۱۹۸۳ کار عاطفی را صورت‌بندی کرده بود: کارمند احساس خود را بر پایه قواعد نمایش مدیریت می‌کند و بخشی از خود را می‌فروشد. اقتصاد عاطفی مخاطب، همین منطق را به پلتفرم می‌برد: تعامل، اشک و خشم به معیار ارزش بدل می‌شوند و تولیدکننده محتوا برای دیده‌شدن، احساس را شدت می‌بخشد. چارچوب توضیح می‌دهد چرا محتوای خشم‌آلود بیشتر دیده می‌شود، چرا برند از صمیمیت سخن می‌گوید و چرا مخاطب، عاطفه خود را به داده‌ای سنجش‌پذیر بدل می‌کند. نقد اصلی، روان‌شناختی‌شدن مسئله ساختاری و کم‌رنگ‌شدن اقتصاد سیاسی است. اهمیت نظریه، پیوند احساس با ارزش اقتصادی و نشان‌دادن این نکته است که بازار تنها کالا نمی‌فروشد؛ قواعد احساس را نیز شکل می‌دهد.",
        "definition": "اقتصاد عاطفی، چارچوبی است که گردش احساس در بازار، کار و رسانه را به‌عنوان جریان ارزش تحلیل می‌کند و نشان می‌دهد عاطفه چگونه سنجیده، مدیریت و کالایی می‌شود.",
        "main_problem": "مسئله این است که چرا احساس در رسانه معاصر به معیار ارزش بدل شده است. پاسخ، پیوند عاطفه و بازار است. پرسش دوم، پیامد است: شدت‌گرفتن احساس چه اثری بر گفت‌وگوی عمومی دارد.",
        "mechanism": "۱. قاعده احساس: بافت، نمایش درست عاطفه را تعیین می‌کند.\n۲. کار عاطفی: مدیریت احساس در ازای دستمزد یا توجه.\n۳. کالایی‌شدن: عاطفه به معیار سنجش تعامل بدل می‌شود.\n۴. زبان درمانی: واژگان روان‌شناختی، رابطه را بازتعریف می‌کند.\n۵. شدت‌بخشی: رقابت برای دیده‌شدن، احساس را اغراق می‌کند.\n۶. بازخورد: سنجه تعامل، تولید عاطفی را هدایت می‌کند.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا فید شبکه اجتماعی به محتوای خشم و شادی شدید پاداش می‌دهد، چرا تبلیغات از صمیمیت خانوادگی سخن می‌گوید و چرا کارکنان رسانه از فرسودگی عاطفی می‌گویند. نکته مهم این است که عاطفه تنها سوخت تعامل نیست؛ سرمایه‌ای است که مدیریت می‌شود؛ از این رو، سواد عاطفی رسانه‌ای باید هم فرصت بیان و هم خطر استثمار احساس را ببیند و سنجه‌های صرفاً کمی را به پرسش بکشد.",
        "assumptions": [
            "احساس، قاعده اجتماعی دارد.",
            "بازار، عاطفه را سنجش‌پذیر می‌کند.",
            "رسانه، جریان عاطفی را هدایت می‌کند.",
        ],
        "principles": [
            "کار عاطفی، بخشی از شغل است.",
            "سنجه تعامل، عاطفه را شکل می‌دهد.",
            "صمیمیت، زبان بازار می‌شود.",
        ],
        "critiques": [
            "۱. روان‌شناسی: مسئله ساختاری به ویژگی فردی فروکاسته می‌شود.\n۲. سنجش: شدت عاطفه با داده تعامل یکی نیست.\n۳. زمینه: یافته‌ها بیشتر به جوامع غربی محدودند.\n۴. قدرت: مالکیت پلتفرم کم تحلیل می‌شود.\n۵. مقاومت: شکل‌های عاطفه غیربازاری کم دیده می‌شوند.",
        ],
        "applications": [
            "نقد رسانه: تحلیل اقتصاد توجه و تعامل.",
            "مدیریت رسانه: کاهش فشار کار عاطفی.",
            "بازاریابی: نقد صمیمیت ساختگی برند.",
            "سواد رسانه: شناخت مدیریت احساس در فید.",
        ],
        "evolution": "هوشیلد در ۱۹۸۳ کار عاطفی را صورت‌بندی کرد و ایلوز در ۲۰۰۷ سرمایه‌داری عاطفی را گسترد. پژوهش پلتفرم، سنجه تعامل و اقتصاد توجه را به چارچوب افزود.",
        "key_concepts": [
            "کار عاطفی (Emotional Labor)",
            "قاعده احساس (Feeling Rule)",
            "سرمایه‌داری عاطفی (Emotional Capitalism)",
            "اقتصاد توجه (Attention Economy)",
            "زبان درمانی (Therapeutic Discourse)",
            "کالایی‌شدن عاطفه (Commodification of Affect)",
        ],
        "studies": [
            "Illouz, E. (2007). Cold intimacies: The making of emotional capitalism. Polity.",
            "Hochschild, A. R. (1983). The managed heart. University of California Press.",
        ],
        "theorists": "اوا ایلوز؛ آرلی هوشیلد",
        "theorists_text": "ایلوز (۲۰۰۷)؛ هوشیلد (۱۹۸۳)",
        "year": 2007,
        "model": "قاعده احساس → کار عاطفی → کالایی‌شدن عاطفه در بازار → بازخورد سنجه تعامل.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nهوشیلد کار عاطفی را در خدمات و ایلوز سرمایه‌داری عاطفی را در فرهنگ صورت‌بندی کردند. نوآوری چارچوب، پیوند احساس با ارزش اقتصادی است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با مصاحبه، تحلیل محتوای تبلیغ و داده تعامل انجام می‌شود. پژوهشی که تنها سنجه تعامل را می‌خواند، تجربه عاطفی را از دست می‌دهد؛ و پژوهشی که هر احساس رسانه‌ای را کالایی می‌خواند، شکل‌های خودانگیخته را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در نقد اقتصاد توجه است، اما باید با اقتصاد سیاسی تکمیل شود. عاطفه بی حمایت، به فرسودگی بدل می‌شود.",
        "critique_text": "\n".join([
            "۱. روان‌شناسی: مسئله ساختاری فردی می‌شود.",
            "۲. سنجش: تعامل با شدت عاطفه یکی نیست.",
            "۳. زمینه: یافته‌ها غربی‌اند.",
            "۴. قدرت: مالکیت پلتفرم کم تحلیل است.",
            "۵. مقاومت: عاطفه غیربازاری کم دیده می‌شود.",
        ]),
        "example_text": "برندی که در تبلیغ خود از لحظه‌های خانوادگی سخن می‌گوید، همان عاطفه‌ای را می‌فروشد که کارکنانش موظف‌اند در برخورد با مشتری نمایش دهند؛ احساس، هزینه و درآمد می‌شود.",
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


NAME_FIX = {
    "MC-585": ("نظریه وضعیتی عمومی‌ها (گرونیگ)", "Situational Theory of Publics",
               "label repaired: 'نظریه وضعیتی افکار عمومی' -> situational theory of publics (Grunig); publics are issue-specific segments, not public opinion in general"),
    "MC-671": ("یکپارچگی زمینه‌ای (حریم خصوصی)", "Contextual Integrity",
               "label repaired: mistranslated 'یکپارچگی زمینهای / Field Integrity' -> contextual integrity (Nissenbaum 2004)"),
}
YEAR_FIX = {
    "MC-676": "year corrected 2009 -> 2007 (Illouz, Cold Intimacies, 2007)",
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
                                       "verified": n_verified, "batch": 114}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH114 THEORY DONE")


if __name__ == "__main__":
    main()
