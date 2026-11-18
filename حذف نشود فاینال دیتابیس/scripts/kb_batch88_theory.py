# -*- coding: utf-8 -*-
"""Batch 88: full documentation for MC-474, MC-475, MC-477, MC-480."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch88-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch88_theory.json"

S = {
    "MC-474": [
        dict(kind="BOOK",
             title_en="Simulacra and Simulation",
             title_fa="وانمایی و شبیه‌سازی",
             authors="Baudrillard, J.; Glaser, S. F. (Trans.)", year=1994,
             publisher="University of Michigan Press",
             doi=None, url="https://press.umich.edu/Books/S/Simulacra-and-Simulation",
             language="en", isbn=None,
             citation="Baudrillard, J. (1994). Simulacra and simulation (S. F. Glaser, Trans.). University of Michigan Press. (Original work published 1981)",
             locator="work", locator_type="work",
             supports="simulacra / hyperreality / four stages of the image / precession of simulacra", verified=True),
        dict(kind="BOOK",
             title_en="Simulations",
             title_fa="شبیه‌سازی‌ها",
             authors="Baudrillard, J.", year=1983, publisher="Semiotext(e)",
             doi=None, url=None, language="en", isbn=None,
             citation="Baudrillard, J. (1983). Simulations (P. Foss, P. Patton, & P. Beitchman, Trans.). Semiotext(e).",
             locator="work", locator_type="work",
             supports="early English statement of simulation and the end of the real", verified=False),
    ],
    "MC-475": [
        dict(kind="BOOK",
             title_en="Amusing Ourselves to Death: Public Discourse in the Age of Show Business",
             title_fa="خود را تا حد مرگ سرگرم می‌کنیم: گفتمان عمومی در عصر نمایش",
             authors="Postman, N.", year=1985, publisher="Viking",
             doi=None, url="https://www.amazon.com/Amusing-Ourselves-Death-Discourse-Business/dp/014303653X",
             language="en", isbn="9780143036531",
             citation="Postman, N. (1985). Amusing ourselves to death: Public discourse in the age of show business. Viking.",
             locator="work", locator_type="work",
             supports="television as epistemology / public discourse as entertainment / Huxleyan warning", verified=True),
        dict(kind="BOOK",
             title_en="Technopoly: The Surrender of Culture to Technology",
             title_fa="تکنوپولی: تسلیم فرهنگ به فناوری",
             authors="Postman, N.", year=1992, publisher="Alfred A. Knopf",
             doi=None, url=None, language="en", isbn=None,
             citation="Postman, N. (1992). Technopoly: The surrender of culture to technology. Alfred A. Knopf.",
             locator="work", locator_type="work",
             supports="extension of media-as-epistemology argument to technological culture", verified=False),
    ],
    "MC-477": [
        dict(kind="BOOK",
             title_en="Communication and Cultural Domination",
             title_fa="ارتباطات و سلطه فرهنگی",
             authors="Schiller, H. I.", year=1976, publisher="International Arts and Sciences Press",
             doi="10.4324/9781315179162",
             url="https://www.taylorfrancis.com/books/mono/10.4324/9781315179162/revival-communication-cultural-domination-1976-herbert-schiller",
             language="en", isbn="0-87332-079-4",
             citation="Schiller, H. I. (1976). Communication and cultural domination. International Arts and Sciences Press. https://doi.org/10.4324/9781315179162",
             locator="work", locator_type="work",
             supports="cultural domination / free flow of information as ideology / media imperialism", verified=True),
        dict(kind="BOOK",
             title_en="Multinational Corporations and the Control of Culture: The Ideological Apparatuses of Imperialism",
             title_fa="شرکت‌های چندملیتی و کنترل فرهنگ: دستگاه‌های ایدئولوژیک امپریالیسم",
             authors="Mattelart, A.", year=1979, publisher="Harvester Press",
             doi=None, url=None, language="en", isbn=None,
             citation="Mattelart, A. (1979). Multinational corporations and the control of culture: The ideological apparatuses of imperialism. Harvester Press.",
             locator="work", locator_type="work",
             supports="cultural industries / international image markets / critique of free-flow doctrine", verified=False),
    ],
    "MC-480": [
        dict(kind="BOOK",
             title_en="Cours de linguistique générale",
             title_fa="درس‌های زبان‌شناسی عمومی",
             authors="de Saussure, F.; Bally, C.; Sechehaye, A.", year=1916, publisher="Payot",
             doi=None, url="https://archive.org/details/courseingenerall00saus",
             language="fr", isbn=None,
             citation="de Saussure, F. (1916). Cours de linguistique générale (C. Bally & A. Sechehaye, Eds.). Payot.",
             locator="work", locator_type="work",
             supports="signifier and signified / arbitrariness / langue vs parole / value through difference", verified=True),
        dict(kind="BOOK",
             title_en="Elements of Semiology",
             title_fa="مبانی نشانه‌شناسی",
             authors="Barthes, R.", year=1967, publisher="Hill and Wang",
             doi=None, url=None, language="en", isbn=None,
             citation="Barthes, R. (1967). Elements of semiology (A. Lavers & C. Smith, Trans.). Hill and Wang.",
             locator="work", locator_type="work",
             supports="application of Saussurean semiotics to mass culture and media", verified=False),
    ],
}

ENRICH = {
    "MC-474": {
        "summary": "(بودریار، ۱۹۸۱) وانمایی وضعیتی است که در آن نشانه‌ها دیگر به واقعیت بیرونی ارجاع نمی‌دهند، بلکه خود واقعیتی خودارجاع می‌سازند. بودریار چهار مرحله تصویر را از هم جدا می‌کند: بازتاب واقعیت، پوشاندن و تحریف واقعیت، پوشاندن غیاب واقعیت، و وانمایی محض که هیچ نسبتی با واقعیت ندارد. در این وضعیت، «فراواقعیت» پدید می‌آید: فضایی که در آن مدل و تصویر، معیار واقعی‌بودن‌اند و تجربه رسانه‌ای از تجربه مستقیم شدیدتر و معتبرتر می‌نماید. تعبیر «تقدّم وانمایی» یعنی نقشه پیش از قلمرو ساخته می‌شود.",
        "definition": "وانمایی، وضعیت جدایی بازنمایی از مرجع آن است؛ وضعیتی که در آن نشانه به‌جای اشاره به واقعیت، نسخه‌ای جایگزین از آن تولید می‌کند و مخاطب در فضایی زندگی می‌کند که در آن معیار حقیقت، انسجام تصاویر است و نه تطابق با جهان بیرون.",
        "main_problem": "مسئله این است که رسانه چگونه واقعیت را نه بازنمایی، بلکه تولید می‌کند و چگونه می‌توان وانمایی را تشخیص داد، در حالی که معیار تشخیص — یعنی واقعیت — خود در همان نظام نشانه‌ها ساخته می‌شود. بودریار پاسخ می‌دهد که تشخیص از درون نظام ممکن نیست و تنها با تحلیل تبار نشانه‌ها و شکاف‌های آن می‌توان رد وانمایی را گرفت. پرسش دوم، پیامد سیاسی است: وقتی رویداد به نمایش بدل شود، تصمیم و مسئولیت چه سرنوشتی می‌یابد.",
        "mechanism": "۱. تقدّم وانمایی: مدل و نقشه پیش از واقعیت ساخته می‌شوند و واقعیت بعد از آن، بر پایه مدل بازسازی می‌گردد؛ نمونه آن پیش‌بینی نظرسنجی، شبیه‌سازی و پیش‌نمایش رویدادهاست.\n۲. چهار مرحله تصویر: تصویر نخست واقعیت را بازتاب می‌دهد، سپس آن را پنهان و تحریف می‌کند، سپس غیاب آن را می‌پوشاند و در پایان، هیچ نسبتی با واقعیت ندارد و خود وانمایی است.\n۳. فراواقعیت: واقعی و خیالی در هم می‌آمیزند؛ تجربه بازسازی‌شده رسانه‌ای چنان کامل می‌شود که جای تجربه مستقیم را می‌گیرد.\n۴. بازتولید بی‌پایان نشانه: تصاویر از تصاویر دیگر زاده می‌شوند و ارجاع به مرجع اولیه به‌تدریج از دست می‌رود؛ نتیجه، انبوهی از نشانه‌های بی‌مرجع است.\n۵. جذب نقد: نظام وانمایی اعتراض را نیز جذب می‌کند و آن را به نشانه‌ای تازه و کالایی بدل می‌سازد؛ نقد، بخشی از نمایش می‌شود.\n۶. پیامد سیاسی رویداد: وقتی رویداد پیش از وقوع در رسانه ساخته می‌شود، مرز میان جنگ و نمایش، سیاست و اجرا فرو می‌ریزد؛ نمونه بحث‌برانگیز آن تحلیل بودریار از جنگ خلیج فارس است.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا برنامه‌های واقع‌نما واقعیتی بازطراحی‌شده عرضه می‌کنند، چرا تصاویر دیپ‌فیک بخشی از جنگ اطلاعاتی‌اند و چرا مخاطب شبکه‌های اجتماعی هویتی «بهینه‌شده» از خود می‌سازد. نکته مهم این است که وانمایی انکار واقعیت نیست؛ ادعایی است درباره اینکه واقعیت در چارچوب نشانه‌ها بازتولید و جایگزین می‌شود.",
        "assumptions": [
            "در وضعیت پسامدرن، نشانه‌ها از مرجع خود جدا شده‌اند.",
            "رسانه، واقعیت را بازنمایی نمی‌کند بلکه نسخه‌ای از آن می‌سازد.",
            "معیار حقیقت درون نظام تصاویر ساخته می‌شود، نه بیرون از آن.",
        ],
        "principles": [
            "تصویر در مرحله چهارم، هیچ نسبتی با واقعیت ندارد.",
            "فراواقعیت از واقعیت شدیدتر و جذاب‌تر تجربه می‌شود.",
            "نقد و اعتراض نیز در نظام وانمایی به نشانه بدل می‌شوند.",
        ],
        "critiques": [
            "۱. نسبی‌گرایی افراطی: انکار امکان دسترسی به واقعیت، راه هر داوری درباره رنج و بی‌عدالتی را دشوار می‌کند.\n۲. آزمون‌ناپذیری: بسیاری از گزاره‌های وانمایی، فلسفی و سبک‌محورند و آزمون تجربی نمی‌پذیرند.\n۳. نمونه‌گزینی: شواهد عمدتاً از فرهنگ فرانسه و آمریکا و رسانه‌های پخش سنتی می‌آید.\n۴. نادیده‌گرفتن تجربه زیسته: تمرکز بر نشانه، تجربه مادی و بدنی رنج و محرومیت را کم‌رنگ می‌کند.\n۵. ابهام مفهومی: وانمایی، فراواقعیت و وانمودگی گاه مترادف به‌کار می‌روند و مرزهایشان روشن نیست.",
        ],
        "applications": [
            "نقد واقع‌نمایی: تحلیل چگونگی ساختن واقعیت در برنامه‌های واقع‌نما و شبکه‌های اجتماعی.",
            "اطلاعات نادرست: بررسی دیپ‌فیک و تصاویر ساختگی به‌عنوان نشانه‌های بی‌مرجع.",
            "برندسازی: تحلیل هویت بهینه‌شده و نمایش زندگی روزمره در پلتفرم‌ها.",
            "پوشش خبری جنگ: بررسی تبدیل رویداد به نمایش و پیامدهای آن برای مسئولیت عمومی.",
        ],
        "evolution": "بودریار ایده را از نقد اقتصاد سیاسی نشانه در دهه ۱۹۷۰ به نظریه وانمایی در ۱۹۸۱ گسترد. سپس آن را در تحلیل جنگ خلیج فارس و رسانه‌های جهانی به‌کار گرفت. پژوهش بعدی، مفهوم را با واقعیت مجازی، شبکه‌های اجتماعی و هوش مصنوعی مولد پیوند داد.",
        "key_concepts": [
            "وانمایی (Simulation)",
            "وانموده (Simulacrum)",
            "فراواقعیت (Hyperreality)",
            "تقدّم وانمایی (Precession of Simulacra)",
            "بی‌مرجعی نشانه (Loss of Referent)",
            "جذب اعتراض (Recuperation of Critique)",
        ],
        "studies": [
            "Baudrillard, J. (1994). Simulacra and simulation (S. F. Glaser, Trans.). University of Michigan Press.",
            "Baudrillard, J. (1983). Simulations. Semiotext(e).",
        ],
        "theorists": "ژان بودریار (۱۹۸۱)",
        "theorists_text": "ژان بودریار (۱۹۸۱)",
        "year": 1981,
        "model": "مدل چهارمرحله‌ای تصویر: بازتاب واقعیت → تحریف و پوشاندن → پوشاندن غیاب واقعیت → وانمایی محض؛ خروجی: فراواقعیت و نشانه بی‌مرجع.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nبودریار نظریه را از نقد مصرف و اقتصاد سیاسی نشانه آغاز کرد و به این نتیجه رسید که در جامعه معاصر، نشانه از کالا نیز فراتر می‌رود و خود واقعیت را جانشین می‌کند. استعاره نقشه و قلمرو، وارونه‌سازی رابطه بازنمایی و جهان است: اینک مدل، اصل است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش تجربی این چارچوب دشوار است، زیرا معیار بیرونی برای مقایسه تصویر و واقعیت را زیر سؤال می‌برد. راه میانه، تحلیل تبار نشانه، مقایسه روایت‌های رقیب یک رویداد و شناسایی حلقه‌های بازتولید تصویر است؛ روش‌هایی که امکان نقد را بدون فرض دسترسی بی‌واسطه به واقعیت حفظ می‌کنند.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در تحلیل رسانه‌های تصویری و سیاست نمایش است؛ اما باید از دو دام پرهیز کرد: انکار کامل واقعیت و فروکاست همه رسانه به وانمایی. واقعیت همیشه با واسطه است، اما واسطه‌بودن به معنای نبود ارجاع نیست؛ رنج، محرومیت و سرکوب، مرجع‌هایی دارند که وانمایی نمی‌تواند حذفشان کند.",
        "critique_text": "\n".join([
            "۱. نسبی‌گرایی افراطی: انکار امکان دسترسی به واقعیت، داوری درباره رنج و بی‌عدالتی را دشوار می‌کند.",
            "۲. آزمون‌ناپذیری: بسیاری از گزاره‌های وانمایی، فلسفی و سبک‌محورند و آزمون تجربی نمی‌پذیرند.",
            "۳. نمونه‌گزینی: شواهد عمدتاً از فرهنگ فرانسه و آمریکا و رسانه‌های پخش سنتی می‌آید.",
            "۴. نادیده‌گرفتن تجربه زیسته: تمرکز بر نشانه، تجربه مادی رنج و محرومیت را کم‌رنگ می‌کند.",
            "۵. ابهام مفهومی: وانمایی، فراواقعیت و وانمودگی گاه مترادف به‌کار می‌روند.",
        ]),
        "example_text": "در شبکه‌های اجتماعی، کاربر پیش از سفر، مقصد را از راه تصاویر دیگران می‌شناسد و سپس تجربه خود را برای گرفتن عکس مشابه تنظیم می‌کند. تجربه، بر پایه تصویر از پیش ساخته‌شده بازسازی می‌شود؛ همین حلقه، نمونه روزمره‌ای از تقدّم وانمایی است.",
    },
    "MC-475": {
        "summary": "(پستمن، ۱۹۸۵) پستمن با وام‌گیری از ایده «رسانه استعاره است» استدلال می‌کند که تلویزیون فقط ابزار انتقال نیست، بلکه شکل شناخت است: تعیین می‌کند چه چیزی گفتنی، معتبر و مهم است. او تاریخ گفتمان عمومی آمریکا را به دو دوره تقسیم می‌کند: عصر تبیین و چاپ که استدلال، توالی و انتزاع را می‌پروراند، و عصر نمایش که همه حوزه‌ها — سیاست، دین، خبر و آموزش — را به سرگرمی بدل می‌کند. هشدار او هکسلی است، نه اورولی: خطر از لذت و بی‌دردی می‌آید، نه از سرکوب.",
        "definition": "«سرگرمی تا حد مرگ» تزی است درباره تبدیل گفتمان عمومی به نمایش: وقتی رسانه غالب، سرگرمی را معیار اعتبار قرار می‌دهد، سیاست به تصویر، خبر به قطعه‌های پراکنده و آموزش به نمایش بدل می‌شود و ظرفیت استدلال، تداوم و حافظه جمعی تضعیف می‌گردد.",
        "main_problem": "مسئله این است که چرا وفور اطلاعات و سرگرمی، به‌جای روشن‌گری، به افول گفتمان عقلانی می‌انجامد. پستمن پاسخ می‌دهد که مسئله محتوا نیست، فرم است: رسانه تلویزیونی امکان تداوم، زمینه و استدلال را از میان برمی‌دارد و همه چیز را در قالب سرگرمی بازچینش می‌کند. پرسش دوم، راه برون‌رفت است: آیا می‌توان با آگاهی از فرم رسانه، گفتمان عمومی را بازسازی کرد.",
        "mechanism": "۱. رسانه به‌عنوان معرفت‌شناسی: هر رسانه ساختار شناختی خاصی می‌سازد و تعیین می‌کند چه نوع گزاره‌ای قابل بیان و ارزیابی است.\n۲. گذار از چاپ به تلویزیون: چاپ، خواندن پیوسته، استدلال و انتزاع را تقویت می‌کند؛ تلویزیون، تصویر، فوریت و پراکندگی را.\n۳. گسست روایی خبر: ساختار «اکنون... این» خبر تلویزیونی، رویدادها را از زمینه جدا می‌کند و مخاطب را به پرش بی‌پایان میان موضوعات بی‌ربط عادت می‌دهد.\n۴. تبدیل حوزه‌های عمومی: سیاست به تصویر و تبلیغ، دین به نمایش احساسی و آموزش به مسابقه و سرگرمی بدل می‌شود.\n۵. معیار سرگرمی: جذابیت، جانشین درستی و اهمیت می‌شود؛ پیام نامفرح از دایره گفتمان بیرون می‌افتد.\n۶. هشدار هکسلی: خطر نه سرکوب اطلاعات، بلکه غرق‌شدن در سرگرمی است؛ مخاطب خودخواسته از گفتمان عمومی فاصله می‌گیرد.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا خبر به «اینفوتیتمنت» بدل می‌شود، چرا کمپین‌های سیاسی به نمایش شخصیت فروکاسته می‌شوند و چرا محتوای آموزشی برای جذب مخاطب باید سرگرم‌کننده باشد. با فراگیری پلتفرم‌های تعاملی، تز پستمن باید بازخوانی شود: سرگرمی امروز تعاملی و شخصی‌سازی‌شده است، اما منطق تبدیل گفتمان به نمایش پایدار مانده است.",
        "assumptions": [
            "شکل رسانه، نوع شناخت و گفتمان ممکن را تعیین می‌کند.",
            "تلویزیون، رسانه‌ای با منطق تصویری و سرگرمی‌محور است.",
            "افول گفتمان عمومی از راه لذت رخ می‌دهد، نه از راه سرکوب.",
        ],
        "principles": [
            "رسانه استعاره است؛ نه ظرف بی‌اثر پیام.",
            "سرگرمی، معیار پنهان اعتبار در رسانه تصویری است.",
            "خبر بدون زمینه، حافظه جمعی را فرسوده می‌کند.",
        ],
        "critiques": [
            "۱. جبرگرایی رسانه‌ای: تز پستمن عاملیت مخاطب و تنوع ژانرها را کم‌رنگ می‌کند.\n۲. آرمانی‌سازی چاپ: عصر چاپ نیز گفتمان عمومی آرمانی نداشت و سواد و دسترسی نابرابر بود.\n۳. تقلیل به تلویزیون: تحلیل بر تلویزیون پخش متمرکز است و پلتفرم‌های تعاملی را در نظر ندارد.\n۴. پیش‌بینی اغراق‌شده: افول کامل گفتمان رخ نداده و اشکال تازه استدلال جمعی پدید آمده است.\n۵. نادیده‌گرفتن اقتصاد سیاسی: مالکیت و منافع تجاری رسانه، در تحلیل کم‌رنگ می‌شود.",
        ],
        "applications": [
            "نقد خبر تلویزیونی: ارزیابی گسست روایی و فقدان زمینه در پوشش رویدادها.",
            "آموزش سواد رسانه‌ای: آموزش تشخیص منطق سرگرمی در حوزه‌های عمومی.",
            "تحلیل سیاست رسانه‌ای: بررسی تبدیل رقابت سیاسی به نمایش شخصیت.",
            "طراحی آموزش: توازن میان جذابیت و عمق در محتوای آموزشی رسانه‌ای.",
        ],
        "evolution": "پستمن تز را در ۱۹۸۵ صورت‌بندی کرد و در «تکنوپولی» (۱۹۹۲) به فرهنگ فناوری گسترد. پژوهش بعدی، آن را با واقعیت تلویزیونی، اینفوتیتمنت و رسانه‌های اجتماعی بازخوانی کرده است.",
        "key_concepts": [
            "رسانه به‌عنوان معرفت‌شناسی (Media as Epistemology)",
            "عصر نمایش (Age of Show Business)",
            "اینفوتیتمنت (Infotainment)",
            "گسست روایی خبر (News Discontinuity)",
            "هشدار هکسلی (Huxleyan Warning)",
            "گفتمان عمومی (Public Discourse)",
        ],
        "studies": [
            "Postman, N. (1985). Amusing ourselves to death: Public discourse in the age of show business. Viking.",
            "Postman, N. (1992). Technopoly: The surrender of culture to technology. Alfred A. Knopf.",
        ],
        "theorists": "نیل پستمن (۱۹۸۵)",
        "theorists_text": "نیل پستمن (۱۹۸۵)",
        "year": 1985,
        "model": "مدل دو‌عصری: عصر چاپ (توالی، استدلال، انتزاع) → عصر نمایش (تصویر، فوریت، سرگرمی) → تبدیل همه حوزه‌های گفتمان عمومی به نمایش.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nپستمن در سنت نقد رسانه مک لوهان و الور می‌نویسد، اما تمرکز خود را از محتوای پیام به فرم شناخت منتقل می‌کند. تز او درباره تلویزیون در واقع تزی درباره هر رسانه‌ای است که سرگرمی را به منطق غالب خود بدل می‌کند؛ از این رو برای تحلیل پلتفرم‌های امروز نیز ارزش دارد.\n\n۲. منطق سنجش و دام‌های آن\nسنجش این تز نیازمند تحلیل هم‌زمان فرم برنامه، ساختار گفتار و کیفیت استدلال عمومی است. پژوهش‌هایی که تنها زمان تماشا را می‌سنجند، به رابطه علّی نمی‌رسند؛ و پژوهش‌هایی که تنها محتوای یک برنامه را نقد می‌کنند، ادعای ساختاری پستمن را نمی‌آزمایند.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت تز در نشان دادن پیوند فرم رسانه و کیفیت گفتمان عمومی است؛ اما باید از آرمانی‌سازی گذشته و جبرگرایی رسانه‌ای پرهیز کرد. مخاطب فعال می‌تواند ژانرهای ترکیبی بسازد، و پلتفرم‌های تعاملی هم می‌توانند گفتمان عمومی را تضعیف و هم بازسازی کنند.",
        "critique_text": "\n".join([
            "۱. جبرگرایی رسانه‌ای: تز پستمن عاملیت مخاطب و تنوع ژانرها را کم‌رنگ می‌کند.",
            "۲. آرمانی‌سازی چاپ: عصر چاپ نیز گفتمان عمومی آرمانی نداشت و سواد و دسترسی نابرابر بود.",
            "۳. تقلیل به تلویزیون: تحلیل بر پخش متمرکز است و پلتفرم‌های تعاملی را در نظر ندارد.",
            "۴. پیش‌بینی اغراق‌شده: افول کامل گفتمان رخ نداده و اشکال تازه استدلال جمعی پدید آمده است.",
            "۵. نادیده‌گرفتن اقتصاد سیاسی: مالکیت و منافع تجاری رسانه در تحلیل کم‌رنگ می‌شود.",
        ]),
        "example_text": "یک برنامه خبری ساعته، در هر دقیقه چند رویداد بی‌ربط را با موسیقی و گرافیک پرسرعت کنار هم می‌چیند؛ مخاطب احساس آگاهی می‌کند اما زمینه و پیوند رویدادها را درک نمی‌کند. اگر همان رویدادها در قالب یک گزارش تحلیلی بلند پخش شوند، مخاطب کمتر جذب می‌کند؛ همین شکاف، نمونه روشنی از سلطه معیار سرگرمی است.",
    },
    "MC-477": {
        "summary": "(شیلر، ۱۹۷۶؛ متلارت، ۱۹۷۹) امپریالیسم فرهنگی و رسانه‌ای به مجموعه فرایندهایی اشاره دارد که جامعه‌ای را در نظام جهانی مدرن ادغام می‌کند و نهادهای اجتماعی و ارزش‌های آن را با ساختارهای مرکز مسلط همساز می‌سازد. شیلر نشان داد که دکترین «جریان آزاد اطلاعات» بیش از آزادی ارتباط، آزادی بازار و منافع تجاری شرکت‌های آمریکایی را تأمین می‌کند. متلارت نیز با تحلیل صنایع فرهنگی و بازارهای جهانی تصویر، سلطه را در سطح تولید و توزیع نشان داد.",
        "definition": "امپریالیسم رسانه‌ای، الگویی از روابط نابرابر در تولید، توزیع و مصرف رسانه است که در آن کشورهای مرکز، جریان محتوا، فناوری و مدل‌های نهادی را تعیین می‌کنند و کشورهای حاشیه به بازار مصرف و واردکننده تبدیل می‌شوند؛ فرایندی که هم‌زمان اقتصادی، سیاسی و فرهنگی است.",
        "main_problem": "مسئله این است که چرا استقلال سیاسی کشورهای تازه‌استقلال‌یافته به استقلال فرهنگی نینجامید و چگونه «جریان آزاد اطلاعات» به ابزار سلطه بدل شد. پاسخ در نابرابری ساختاری سرمایه، زیرساخت و بازار نهفته است: آزادی جریان، در شرایط نابرابری، آزادی بازیگر قوی‌تر است. پرسش دوم، امکان مقاومت است: آیا سیاست‌های ملی و همکاری جنوب می‌تواند جریان را متعادل کند.",
        "mechanism": "۱. عدم تقارن ساختاری: سرمایه تولید، شبکه توزیع و بازار تبلیغات در مرکز متمرکز است و حاشیه را به واردکننده بدل می‌کند.\n۲. ایدئولوژی جریان آزاد: آزادی ارتباط به آزادی تجارت تقلیل می‌یابد و مقررات حمایتی به «سانسور» متهم می‌شود.\n۳. صنایع فرهنگی فراملی: سینما، تلویزیون، تبلیغات و خبرگزاری‌ها، الگوهای مصرف و بازنمایی را صادر می‌کنند.\n۴. همسازی نهادی: آموزش، رسانه ملی و نظام تبلیغات در حاشیه بر پایه مدل مرکز بازساخته می‌شوند.\n۵. بازتولید ارزش‌ها: محتوای سرگرم‌کننده، ارزش‌های فردگرایی، مصرف و نظم سیاسی مرکز را طبیعی جلوه می‌دهد.\n۶. آگاهی و مقاومت: بحث نظم نوین اطلاعات و ارتباطات در یونسکو و گزارش مک‌برایدر (۱۹۸۰)، تلاش برای بازتعریف جریان و تقویت تولید ملی بود.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا بازار خبر جهانی نامتوازن است، چرا صادرات سرگرمی به ابزار قدرت نرم بدل می‌شود و چرا کشورها سیاست حمایت از تولید محلی را پیش می‌گیرند. نکته مهم این است که تحلیل انتقادی بعدی — جریان معکوس، جهانی‌محلی‌شدن و مخاطب فعال — بخشی از تصویر را اصلاح کرد، اما نابرابری زیرساخت و مالکیت را حذف نکرد.",
        "assumptions": [
            "جریان رسانه‌ای جهانی ساختاری نابرابر دارد.",
            "رسانه، هم‌زمان ابزار اقتصادی، سیاسی و فرهنگی است.",
            "دکترین جریان آزاد، ایدئولوژی خنثی نیست.",
        ],
        "principles": [
            "آزادی جریان در شرایط نابرابری، آزادی بازیگر قوی‌تر است.",
            "سلطه فرهنگی از راه نهادها و صنایع، نه فقط محتوا، بازتولید می‌شود.",
            "سیاست ملی و همکاری منطقه‌ای می‌تواند عدم تقارن را تعدیل کند.",
        ],
        "critiques": [
            "۱. تقلیل اقتصادی: فرهنگ به بازتاب منافع سرمایه فروکاسته می‌شود و خلاقیت و تفسیر محلی نادیده می‌ماند.\n۲. انکار عاملیت مخاطب: پژوهش مخاطب فعال نشان داد مصرف محلی، معنای تازه می‌سازد.\n۳. استعاره نظامی: واژه امپریالیسم، فرایندهای متنوع و متعارض را یکسان می‌کند.\n۴. سنجش دشوار: تفکیک اثر محتوای وارداتی از عوامل داخلی به‌سختی ممکن است.\n۵. تحول بستر: تحلیل بر پخش و سینما متمرکز است و اقتصاد پلتفرم و داده را در نظر ندارد.",
        ],
        "applications": [
            "سیاست رسانه‌ای: طراحی حمایت از تولید ملی بدون فروکاستن به سانسور.",
            "تحلیل جریان خبری: بررسی سهم منابع جهانی در اخبار داخلی.",
            "مذاکرات بین‌المللی: تحلیل منافع پشت دکترین جریان آزاد اطلاعات.",
            "مطالعات قدرت نرم: ارزیابی صادرات سرگرمی و اثر آن بر تصویر کشورها.",
        ],
        "evolution": "شیلر در ۱۹۶۹ و ۱۹۷۶ چارچوب را صورت‌بندی کرد و متلارت آن را با تحلیل صنایع فرهنگی گسترد. بحث نظم نوین اطلاعات در یونسکو اوج سیاسی آن بود. سپس نقد مخاطب فعال، جهانی‌محلی‌شدن و جریان معکوس، تصویر را پیچیده‌تر کرد.",
        "key_concepts": [
            "امپریالیسم فرهنگی (Cultural Imperialism)",
            "امپریالیسم رسانه‌ای (Media Imperialism)",
            "جریان آزاد اطلاعات (Free Flow of Information)",
            "صنایع فرهنگی فراملی (Transnational Cultural Industries)",
            "نظم نوین اطلاعات و ارتباطات (NWICO)",
            "عدم تقارن جریان (Flow Asymmetry)",
        ],
        "studies": [
            "Schiller, H. I. (1976). Communication and cultural domination. International Arts and Sciences Press.",
            "Mattelart, A. (1979). Multinational corporations and the control of culture. Harvester Press.",
        ],
        "theorists": "هربرت شیلر (۱۹۷۶)؛ آرمند متلارت (۱۹۷۹)",
        "theorists_text": "هربرت شیلر (۱۹۷۶)؛ آرمند متلارت (۱۹۷۹)",
        "year": 1976,
        "model": "مدل سه‌سطحی: نابرابری سرمایه و زیرساخت → ایدئولوژی جریان آزاد و صنایع فرهنگی فراملی → همسازی نهادی و بازتولید ارزش‌ها → مقاومت ملی و منطقه‌ای.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nشیلر و متلارت در سنت اقتصاد سیاسی انتقادی و در بستر استعمارزدایی نوشتند. پرسش آنان این بود که چرا پرچم سیاسی عوض شد اما ساختار وابستگی رسانه‌ای نه. پاسخ، پیوند سرمایه، فناوری و ایدئولوژی در یک نظام جهانی بود.\n\n۲. منطق سنجش و دام‌های آن\nسنجش این چارچوب نیازمند داده‌های چندسطحی است: سهم بازار، ترکیب برنامه، مالکیت و جریان سرمایه، و معنای دریافت‌شده. پژوهش‌هایی که تنها محتوای وارداتی را می‌شمارند، مقاومت و تفسیر محلی را از دست می‌دهند؛ و پژوهش‌هایی که تنها مصرف محلی را برجسته می‌کنند، نابرابری ساختاری را نادیده می‌گیرند.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در پیوند دادن اقتصاد، سیاست و فرهنگ است؛ اما نباید به تقلیل‌گرایی اقتصادی بینجامد. فرهنگ، میدان مذاکره و آفرینش است، نه فقط بازتاب سلطه؛ با این حال، نابرابری مالکیت و زیرساخت، میدان مذاکره را نامتقارن می‌کند.",
        "critique_text": "\n".join([
            "۱. تقلیل اقتصادی: فرهنگ به بازتاب منافع سرمایه فروکاسته می‌شود و خلاقیت و تفسیر محلی نادیده می‌ماند.",
            "۲. انکار عاملیت مخاطب: پژوهش مخاطب فعال نشان داد مصرف محلی، معنای تازه می‌سازد.",
            "۳. استعاره نظامی: واژه امپریالیسم، فرایندهای متنوع و متعارض را یکسان می‌کند.",
            "۴. سنجش دشوار: تفکیک اثر محتوای وارداتی از عوامل داخلی به‌سختی ممکن است.",
            "۵. تحول بستر: تحلیل بر پخش و سینما متمرکز است و اقتصاد پلتفرم و داده را در نظر ندارد.",
        ]),
        "example_text": "در کشوری که بیشتر فیلم‌های پرمخاطب آن وارداتی است، مخاطب محلی همان فیلم‌ها را با دوبله و شوخی محلی مصرف می‌کند و معنایی تازه می‌سازد؛ همین مصرف فعال نشان می‌دهد که سلطه کامل نیست. اما وقتی توزیع، تبلیغات و زیرساخت در دست شرکت‌های فراملی است، میدان این تفسیر همچنان نامتقارن می‌ماند.",
    },
    "MC-480": {
        "summary": "(سوسور، ۱۹۱۶) نشانه‌شناسی ساختاری بر این ایده بنا شده که نشانه از دو جزء ساخته می‌شود: دال، یعنی صورت مادی نشانه، و مدلول، یعنی مفهوم ذهنی آن. پیوند میان این دو دلبخواهی است: هیچ ضرورت طبیعی میان واژه و معنا وجود ندارد. سوسور زبان را به‌عنوان نظام (زبان) از کاربرد فردی (گفتار) جدا کرد و نشان داد که معنا نه از محتوای مثبت نشانه‌ها، بلکه از تفاوت آن‌ها با یکدیگر حاصل می‌شود. او علم عمومی نشانه‌ها را پیشنهاد کرد که بعدها پایه تحلیل رسانه شد.",
        "definition": "نشانه‌شناسی ساختاری، مطالعه نظام‌مند نشانه‌ها و قواعد ترکیب آن‌هاست؛ رویکردی که معنا را محصول روابط درونی نظام نشانه‌ای می‌داند، نه بازتاب مستقیم واقعیت. در این چارچوب، هر نشانه از راه تفاوت با نشانه‌های دیگر ارزش پیدا می‌کند.",
        "main_problem": "مسئله این است که اگر پیوند دال و مدلول دلبخواهی است، معنا چگونه پایدار می‌ماند و چگونه می‌تواند تغییر کند. پاسخ در نظام و تفاوت نهفته است: هر نشانه از راه جایگاه خود در شبکه تفاوت‌ها معنا می‌یابد و تغییر یک رابطه، کل شبکه را جابه‌جا می‌کند. پرسش دوم، کاربرد رسانه‌ای است: چگونه تحلیل نشانه‌ها می‌تواند ایدئولوژی و رمزگان پنهان پیام‌های رسانه‌ای را آشکار کند.",
        "mechanism": "۱. دال و مدلول: هر نشانه دو وجه دارد، صورت مادی قابل ادراک و مفهوم ذهنی؛ تحلیل نشانه‌شناختی این دو را از هم تفکیک می‌کند.\n۲. دلبخواهی بودن نشانه: رابطه دال و مدلول قراردادی است؛ همین دلبخواهی، امکان تغییر معنا و سوءاستفاده از آن را فراهم می‌کند.\n۳. تفاوت و ارزش: نشانه‌ها معنای خود را از تمایز با نشانه‌های دیگر می‌گیرند؛ «شب» فقط در نسبت با «روز» معنا دارد.\n۴. زبان و گفتار: نظام جمعی زبان، امکان کاربرد فردی گفتار را فراهم می‌کند؛ تحلیل باید هر دو سطح را ببیند.\n۵. همنشینی و جانشینی: نشانه‌ها هم در زنجیره کنار هم می‌آیند و هم از میان گزینه‌های ممکن انتخاب می‌شوند؛ این دو محور، ساختار پیام را می‌سازند.\n۶. همزمانی و نظام: تحلیل همزمان، زبان را به‌عنوان نظام در یک لحظه می‌بیند و تغییر تاریخی را به سطح ثانوی می‌راند؛ همین تمرکز، قدرت و محدودیت رویکرد است.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا انتخاب واژه، تصویر و رنگ در تبلیغ، معنای ایدئولوژیک می‌سازد و چرا تحلیل رمزگان، لایه پنهان پیام را آشکار می‌کند. بارت و ساختارگرایان بعدی، این ابزار را به تحلیل فرهنگ عامه، مد، عکاسی و خبر گستردند.",
        "assumptions": [
            "نشانه واحد بنیادی معناسازی است.",
            "معنا از روابط و تفاوت‌های درون نظام حاصل می‌شود.",
            "نظام زبان، مقدم بر کاربرد فردی آن است.",
        ],
        "principles": [
            "پیوند دال و مدلول قراردادی و دلبخواهی است.",
            "در نظام نشانه‌ها، تنها تفاوت وجود دارد.",
            "تحلیل ساختاری، پیام را به‌عنوان ترکیب انتخاب‌ها می‌بیند.",
        ],
        "critiques": [
            "۱. متن‌محوری: تحلیل ساختاری بافت اجتماعی، تاریخ و کاربرد را کم‌رنگ می‌کند.\n۲. نادیده‌گرفتن انگیزه: همه نشانه‌ها دلبخواهی نیستند و برخی شباهت یا انگیزه نمادین دارند.\n۳. جبرگرایی نظام: فرض می‌شود نظام، معنا را تعیین می‌کند و خلاقیت کنشگر کم‌رنگ می‌شود.\n۴. حاشیه‌ای‌کردن تغییر: تمرکز بر همزمانی، تحلیل تحول تاریخی معنا را دشوار می‌کند.\n۵. نسبت دادن افراط‌ها: بسیاری از تقلیل‌گرایی‌های ساختارگرای بعدی، بیش از خود سوسور به او نسبت داده شده است.",
        ],
        "applications": [
            "تحلیل تبلیغات: آشکارسازی رمزگان و انتخاب‌های معناساز در پیام تجاری.",
            "تحلیل خبر: بررسی واژه‌گزینی و چیدمان به‌عنوان سازوکار ایدئولوژیک.",
            "سواد بصری: آموزش خوانش نشانه‌های تصویری و طراحی.",
            "برندسازی: ساخت نظام معنایی متمایز برای محصول و هویت.",
        ],
        "evolution": "سوسور درس‌های خود را در آغاز قرن بیستم ارائه کرد و شاگردانش در ۱۹۱۶ آن را منتشر کردند. بارت و ساختارگرایان، ابزار او را به فرهنگ عامه گستردند؛ سپس پساساختارگرایی، تمرکز بر تفاوت و نظام را به نقد کشید و بافت و قدرت را وارد تحلیل کرد.",
        "key_concepts": [
            "دال و مدلول (Signifier and Signified)",
            "دلبخواهی بودن نشانه (Arbitrariness)",
            "زبان و گفتار (Langue and Parole)",
            "تفاوت (Difference)",
            "همنشینی و جانشینی (Syntagm and Paradigm)",
            "همزمانی و درزمانی (Synchronic and Diachronic)",
        ],
        "studies": [
            "de Saussure, F. (1916). Cours de linguistique générale. Payot.",
            "Barthes, R. (1967). Elements of semiology. Hill and Wang.",
        ],
        "theorists": "فردینان دو سوسور (۱۹۱۶)",
        "theorists_text": "فردینان دو سوسور (۱۹۱۶)",
        "year": 1916,
        "model": "مدل دوجزئی نشانه: دال + مدلول، با پیوند دلبخواهی؛ معنا از تفاوت در نظام (زبان) و از ترکیب انتخاب‌ها در دو محور همنشینی و جانشینی ساخته می‌شود.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nسوسور زبان‌شناسی را از تاریخی‌گری قرن نوزدهم به تحلیل نظام همزمان منتقل کرد. نوآوری او این بود که معنا را نه در ارجاع به جهان، بلکه در روابط درونی نشانه‌ها جست‌وجو کرد؛ ایده‌ای که پایه ساختارگرایی و نشانه‌شناسی رسانه شد.\n\n۲. منطق سنجش و دام‌های آن\nتحلیل نشانه‌شناختی نیازمند تفکیک سطح دال، سطح مدلول و سطح رمزگان فرهنگی است. خطای رایج، فروکاستن تحلیل به فهرست کردن نشانه‌ها بدون تحلیل روابط و بدون توجه به بافت است؛ روش مناسب، نشان دادن اینکه چرا این انتخاب و نه گزینه‌های دیگر، این معنا را می‌سازد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در آشکارسازی لایه‌های پنهان پیام است، اما نباید به متن‌محوری و نادیده‌گرفتن مخاطب بینجامد. معنا در تعامل متن، رمزگان و مخاطب ساخته می‌شود؛ از این رو تحلیل ساختاری باید با تحلیل دریافت و بافت تکمیل شود.",
        "critique_text": "\n".join([
            "۱. متن‌محوری: تحلیل ساختاری بافت اجتماعی، تاریخ و کاربرد را کم‌رنگ می‌کند.",
            "۲. نادیده‌گرفتن انگیزه: همه نشانه‌ها دلبخواهی نیستند و برخی شباهت یا انگیزه نمادین دارند.",
            "۳. جبرگرایی نظام: فرض می‌شود نظام، معنا را تعیین می‌کند و خلاقیت کنشگر کم‌رنگ می‌شود.",
            "۴. حاشیه‌ای‌کردن تغییر: تمرکز بر همزمانی، تحلیل تحول تاریخی معنا را دشوار می‌کند.",
            "۵. نسبت دادن افراط‌ها: تقلیل‌گرایی‌های ساختارگرای بعدی بیش از خود سوسور به او نسبت داده شده است.",
        ]),
        "example_text": "در تبلیغ یک خودرو، انتخاب رنگ سیاه، زاویه پایین دوربین و واژه «قدرت» در کنار هم، معنایی از سلطه و امنیت می‌سازد. هیچ‌یک از این نشانه‌ها به‌تنهایی این معنا را ندارد؛ معنا از روابط و انتخاب‌ها در نظام رمزگان تبلیغاتی زاده می‌شود.",
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
                                       "verified": n_verified, "batch": 88}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH88 THEORY DONE")


if __name__ == "__main__":
    main()
