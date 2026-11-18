# -*- coding: utf-8 -*-
"""Batch 111: full documentation for MC-670, MC-672, MC-708, MC-713."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch111-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch111_theory.json"

S = {
    "MC-670": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Information Privacy Concerns, Procedural Fairness, and Impersonal Trust: An Empirical Investigation",
             title_fa="نگرانی‌های حریم خصوصی اطلاعات، انصاف رویه‌ای و اعتماد غیرشخصی: پژوهشی تجربی",
             authors="Culnan, M. J.; Armstrong, P. K.", year=1999, publisher="Organization Science",
             doi="10.1287/orsc.10.1.104",
             url="https://dl.acm.org/doi/10.1287/orsc.10.1.104",
             language="en", isbn=None,
             citation="Culnan, M. J., & Armstrong, P. K. (1999). Information privacy concerns, procedural fairness, and impersonal trust: An empirical investigation. Organization Science, 10(1), 104-115.",
             locator="10(1):104-115", locator_type="page_range",
             supports="privacy calculus balancing disclosure benefits against privacy risk", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="An Extended Privacy Calculus Model for E-Commerce Transactions",
             title_fa="مدل گسترده محاسبه حریم خصوصی برای تراکنش‌های تجارت الکترونیک",
             authors="Dinev, T.; Hart, P.", year=2006, publisher="Information Systems Research",
             doi=None, url=None, language="en", isbn=None,
             citation="Dinev, T., & Hart, P. (2006). An extended privacy calculus model for e-commerce transactions. Information Systems Research, 17(1), 61-80.",
             locator="17(1):61-80", locator_type="page_range",
             supports="extended calculus with trust and risk beliefs", verified=False),
    ],
    "MC-672": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Engineering the Public: Big Data, Surveillance and Computational Politics",
             title_fa="مهندسی افکار عمومی: داده‌های کلان، پایش و سیاست محاسباتی",
             authors="Tufekci, Z.", year=2014, publisher="First Monday",
             doi=None, url="https://firstmonday.org/ojs/index.php/fm/article/view/4901",
             language="en", isbn=None,
             citation="Tufekci, Z. (2014). Engineering the public: Big data, surveillance and computational politics. First Monday, 19(7).",
             locator="19(7)", locator_type="work",
             supports="computational politics, individualized persuasion and feedback loops", verified=True),
        dict(kind="BOOK",
             title_en="New Media Campaigns and the Managed Citizen",
             title_fa="کمپین‌های رسانه جدید و شهروند مدیریت‌شده",
             authors="Howard, P. N.", year=2006, publisher="Cambridge University Press",
             doi=None, url=None, language="en", isbn=None,
             citation="Howard, P. N. (2006). New media campaigns and the managed citizen. Cambridge University Press.",
             locator="work", locator_type="work",
             supports="data-driven campaign management and voter profiling", verified=False),
    ],
    "MC-708": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Putting the Fear Back into Fear Appeals: The Extended Parallel Process Model",
             title_fa="بازگرداندن ترس به هشدارهای ترس: مدل فرایند موازی گسترده",
             authors="Witte, K.", year=1992, publisher="Communication Monographs",
             doi="10.1080/03637759209376276",
             url="https://www.tandfonline.com/doi/abs/10.1080/03637759209376276",
             language="en", isbn=None,
             citation="Witte, K. (1992). Putting the fear back into fear appeals: The extended parallel process model. Communication Monographs, 59(4), 329-349.",
             locator="59(4):329-349", locator_type="page_range",
             supports="threat and efficacy appraisal leading to danger or fear control", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="A Protection Motivation Theory of Fear Appeals and Attitude Change",
             title_fa="نظریه انگیزش حفاظتی درباره هشدارهای ترس و تغییر نگرش",
             authors="Rogers, R. W.", year=1975, publisher="Journal of Psychology",
             doi=None, url=None, language="en", isbn=None,
             citation="Rogers, R. W. (1975). A protection motivation theory of fear appeals and attitude change. Journal of Psychology, 91(1), 93-114.",
             locator="91(1):93-114", locator_type="page_range",
             supports="protection motivation and appraisal components", verified=False),
    ],
    "MC-713": [
        dict(kind="BOOK",
             title_en="Exacting Beauty: Theory, Assessment, and Treatment of Body Image Disturbance",
             title_fa="زیبایی سخت‌گیرانه: نظریه، سنجش و درمان اختلال تصویر بدن",
             authors="Thompson, J. K.; Heinberg, L. J.; Altabe, M.; Tantleff-Dunn, S.",
             year=1999, publisher="American Psychological Association",
             doi=None, url="https://psycnet.apa.org/doiLanding?doi=10.1037%2F10312-000",
             language="en", isbn=None,
             citation="Thompson, J. K., Heinberg, L. J., Altabe, M., & Tantleff-Dunn, S. (1999). Exacting beauty: Theory, assessment, and treatment of body image disturbance. American Psychological Association.",
             locator="work", locator_type="work",
             supports="tripartite sociocultural influences on body image", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="A Theory of Social Comparison Processes",
             title_fa="نظریه فرایندهای مقایسه اجتماعی",
             authors="Festinger, L.", year=1954, publisher="Human Relations",
             doi=None, url=None, language="en", isbn=None,
             citation="Festinger, L. (1954). A theory of social comparison processes. Human Relations, 7(2), 117-140.",
             locator="7(2):117-140", locator_type="page_range",
             supports="social comparison as mediator of media influence", verified=False),
    ],
}

ENRICH = {
    "MC-670": {
        "summary": "(کالن و آرمسترانگ، ۱۹۹۹) نظریه محاسبه حریم خصوصی می‌گوید کاربر هنگام افشای اطلاعات شخصی، سود و زیان را می‌سنجد. پاداش‌هایی مانند خدمات شخصی‌سازی‌شده، دسترسی رایگان و سهولت، در برابر خطرهایی مانند سوءاستفاده، پایش و از دست دادن کنترل قرار می‌گیرند. کالن و آرمسترانگ نشان دادند انصاف رویه‌ای و اعتماد به سازمان، خطر ادراک‌شده را کاهش می‌دهد. دینف و هارت مدل را با باورهای خطر و اعتماد گستردند. تناقض حریم خصوصی، یعنی شکاف میان نگرانی اعلام‌شده و رفتار افشاگرانه، نشان داد محاسبه همیشه آگاهانه نیست. در رسانه دیجیتال، این چارچوب توضیح می‌دهد چرا مخاطب در برابر محتوای رایگان، داده می‌دهد. از این رو، شفافیت و کنترل کاربر بر داده تنها الزام حقوقی نیست؛ شرط حفظ اعتماد و تداوم رابطه رسانه با مخاطب است، زیرا اعتماد یک بار شکسته، به سختی بازسازی می‌شود.",
        "definition": "محاسبه حریم خصوصی، فرایندی است که فرد در آن سودهای ادراک‌شده افشای اطلاعات را در برابر خطرهای حریم خصوصی می‌سنجد و بر پایه تراز این دو، تصمیم به افشا یا خودداری می‌گیرد.",
        "main_problem": "مسئله این است که چرا افراد با وجود نگرانی از حریم خصوصی، اطلاعات خود را افشا می‌کنند. پاسخ، تراز سود و زیان ادراکی است. پرسش دوم، شکاف است: چرا اعلام نگرانی با رفتار واقعی هم‌خوان نیست.",
        "mechanism": "۱. سود ادراک‌شده: خدمت، تخفیف و سهولت.\n۲. خطر ادراک‌شده: سوءاستفاده، پایش و از دست دادن کنترل.\n۳. اعتماد: اطمینان به نیت سازمان، خطر را کاهش می‌دهد.\n۴. انصاف رویه‌ای: شفافیت رویه، تراز را به سود افشا می‌برد.\n۵. عادت: استفاده مکرر، محاسبه را خودکار و کم‌هزینه می‌کند.\n۶. تناقض: نگرانی بالا با افشای بالا هم‌زیستی دارد.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا کاربر برای دسترسی به شبکه اجتماعی، شرایط حریم خصوصی را می‌پذیرد، چرا رضایت آگاهانه کاغذی کم‌اثر است و چرا رسوایی داده، اعتماد را می‌شکند. نکته مهم این است که محاسبه همیشه عقلانی و کامل نیست؛ سوگیری خوش‌بینی و عادت آن را تحریف می‌کنند.",
        "assumptions": [
            "کاربر سود و زیان افشا را می‌سنجد.",
            "اعتماد، خطر ادراک‌شده را کاهش می‌دهد.",
            "محاسبه همیشه آگاهانه نیست.",
        ],
        "principles": [
            "انصاف رویه‌ای، افشا را تسهیل می‌کند.",
            "تناقض حریم، عقلانیت کامل را رد می‌کند.",
            "رسوایی داده، اعتماد را می‌شکند.",
        ],
        "critiques": [
            "۱. عقلانیت: محاسبه را بیش از اندازه آگاهانه می‌بیند.\n۲. زمینه: سود و زیان فرهنگی و موقعیتی است.\n۳. قدرت: نابرابری چانه‌زنی کاربر کم دیده می‌شود.\n۴. سنجش: خطر ادراک‌شده سخت اندازه‌گیری می‌شود.\n۵. طراحی: اثر تیره الگوی رابط کم‌تر تحلیل می‌شود.",
        ],
        "applications": [
            "سیاست حریم خصوصی: طراحی رضایت شفاف.",
            "رسانه دیجیتال: تحلیل مبادله محتوا و داده.",
            "بازاریابی: اعتمادسازی پیش از درخواست داده.",
            "سواد دیجیتال: آگاهی از سوگیری محاسبه.",
        ],
        "evolution": "کالن و آرمسترانگ در ۱۹۹۹ محاسبه را با انصاف رویه‌ای و اعتماد پیوند دادند و دینف و هارت در ۲۰۰۶ مدل را گستردند. بعدها پژوهش تناقض حریم و اقتصاد داده، چارچوب را بسط داد.",
        "key_concepts": [
            "محاسبه حریم خصوصی (Privacy Calculus)",
            "خطر ادراک‌شده (Perceived Risk)",
            "سود ادراک‌شده (Perceived Benefit)",
            "انصاف رویه‌ای (Procedural Fairness)",
            "اعتماد غیرشخصی (Impersonal Trust)",
            "تناقض حریم خصوصی (Privacy Paradox)",
        ],
        "studies": [
            "Culnan, M. J., & Armstrong, P. K. (1999). Information privacy concerns, procedural fairness, and impersonal trust. Organization Science, 10(1), 104-115.",
            "Dinev, T., & Hart, P. (2006). An extended privacy calculus model for e-commerce transactions. Information Systems Research, 17(1), 61-80.",
        ],
        "theorists": "مری کالن؛ پاملا آرمسترانگ",
        "theorists_text": "کالن و آرمسترانگ (۱۹۹۹)",
        "year": 1999,
        "model": "سود ادراک‌شده − خطر ادراک‌شده × اعتماد و انصاف → تصمیم افشا → بازخورد به اعتماد.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nکالن و آرمسترانگ حریم خصوصی را مبادله‌ای ادراکی دیدند و اعتماد را میانجی ساختند. نوآوری چارچوب، پیوند اخلاق داده با رفتار مصرف‌کننده است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با پیمایش نگرش، آزمون سناریو و تحلیل رفتار انجام می‌شود. پژوهشی که تنها نگرانی را می‌سنجد، رفتار را از دست می‌دهد؛ و پژوهشی که محاسبه را کامل عقلانی می‌گیرد، تناقض حریم را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در تحلیل رضایت داده است، اما باید با مطالعه طراحی تیره تکمیل شود. افشای بی حمایت، به استثمار داده بدل می‌شود.",
        "critique_text": "\n".join([
            "۱. عقلانیت: محاسبه بیش از اندازه آگاهانه فرض می‌شود.",
            "۲. زمینه: سود و زیان فرهنگی است.",
            "۳. قدرت: نابرابری چانه‌زنی کم دیده می‌شود.",
            "۴. سنجش: خطر ادراک‌شده سخت اندازه‌پذیر است.",
            "۵. طراحی: اثر تیره الگو کم‌تر تحلیل می‌شود.",
        ]),
        "example_text": "کاربری که نگران حریم خصوصی است، برای دسترسی به یک اپلیکیشن رایگان اجازه دسترسی به مخاطبان را می‌دهد؛ سود فوری بر خطر دورتر چیره می‌شود.",
    },
    "MC-672": {
        "summary": "(توفکچی، ۲۰۱۴) نظریه داده‌کاوی سیاسی توضیح می‌دهد چگونه داده‌های کلان، کمپین سیاسی را از تبلیغ جمعی به اقناع فردی‌شده تغییر می‌دهد. توفکچی شش پویایی درهم‌تنیده را برشمرد: رشد داده کلان، گذار از جمعیت‌شناسی به پروفایل فردی، حلقه بازخورد، دروازه‌بانی الگوریتمی، آزمون پیوسته پیام و تلاش برای مهندسی افکار عمومی. این سازوکارها، شهروند را به داده‌ای قابل پیش‌بینی و هدف‌گیری بدل می‌کنند. پایش، مرز میان کمپین و نظارت را محو می‌سازد. نظریه، پیوند میان پروفایل‌سازی، آزمون پیام و اثر سیاسی را برجسته می‌کند و پرسش‌های اخلاقی و دموکراتیک تازه‌ای می‌سازد. همچنین باید میان دستکاری و اقناع تفکیک کرد: اقناع با استدلال و شفافیت همراه است، در حالی که دستکاری با پنهان کردن هدف و سوءاستفاده از سوگیری‌های شناختی کار می‌کند. از این چشم، مسئله اصلی تنها دقت داده نیست، بلکه پاسخ‌گویی نهادهایی است که داده را گرد می‌آورند و به کار می‌گیرند، به‌ویژه هنگامی که پایش داده به ابزار فشار بر شهروندان بدل شود و مرز میان خدمات عمومی و نظارت از میان برود؛ چنین وضعیتی، پرسش شهروند را از «چه پیامی به من رسیده» به «چرا سامانه این پیام را برای من برگزیده» تغییر می‌دهد.",
        "definition": "داده‌کاوی سیاسی، مجموعه رویه‌های گردآوری، ترکیب و تحلیل داده شخصی برای پروفایل‌سازی رأی‌دهنده و تنظیم فردی‌شده پیام سیاسی است که کمپین را به سامانه‌ای محاسباتی بدل می‌کند.",
        "main_problem": "مسئله این است که چگونه داده، اقناع سیاسی را کارآمدتر و نامرئی‌تر می‌کند. پاسخ، پروفایل‌سازی فردی و آزمون پیوسته است. پرسش دوم، اخلاق است: مرز میان ارتباط سیاسی و دستکاری شهروند کجاست.",
        "mechanism": "۱. داده کلان: ترکیب فهرست رأی‌دهنده، مصرف رسانه و داده تجاری.\n۲. فردی‌سازی: گذار از دسته جمعیتی به پروفایل یک‌به‌یک.\n۳. حلقه بازخورد: واکنش مخاطب، پیام بعدی را تنظیم می‌کند.\n۴. دروازه‌بانی الگوریتمی: سامانه تعیین می‌کند چه کسی چه پیامی ببیند.\n۵. آزمون پیوسته: آزمایش پیام برای بیشینه‌سازی اثر.\n۶. مهندسی افکار: شکل‌دهی ترجیح پیش از رأی‌گیری.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا دو رأی‌دهنده در یک انتخابات پیام‌های متضاد می‌بینند، چرا شفافیت تبلیغات سیاسی دشوار است و چرا پایش داده، اعتماد عمومی را فرسوده می‌کند. نکته مهم این است که اثربخشی داده‌کاوی اغلب بیش‌برآورد می‌شود؛ داده، جایگزین زمینه اجتماعی نیست.",
        "assumptions": [
            "داده شخصی، رفتار سیاسی را پیش‌بینی‌پذیر می‌سازد.",
            "پیام فردی‌شده اثر بیشتری دارد.",
            "پایش و کمپین مرز روشنی ندارند.",
        ],
        "principles": [
            "حلقه بازخورد، اقناع را تشدید می‌کند.",
            "دروازه‌بانی الگوریتمی، دیدگاه را محدود می‌کند.",
            "شفافیت، شرط مشروعیت است.",
        ],
        "critiques": [
            "۱. اثربخشی: قدرت اقناع فردی‌شده بیش‌برآورد شده است.\n۲. اخلاق: رضایت آگاهانه کاربر نادیده می‌ماند.\n۳. نظارت: مرز کمپین و پایش محو می‌شود.\n۴. شواهد: داده‌های کمپین شفاف نیستند.\n۵. زمینه: مدل بیشتر آمریکایی است.",
        ],
        "applications": [
            "سیاست‌گذاری تبلیغات سیاسی: الزام شفافیت داده.",
            "روزنامه‌نگاری داده: افشای پروفایل‌سازی.",
            "سواد سیاسی: شناخت پیام فردی‌شده.",
            "اخلاق کمپین: مرز اقناع و دستکاری.",
        ],
        "evolution": "توفکچی در ۲۰۱۴ شش پویایی سیاست محاسباتی را صورتبندی کرد. پس از رسوایی‌های داده، پژوهش شفافیت، پایش و مقررات، چارچوب را گسترد.",
        "key_concepts": [
            "سیاست محاسباتی (Computational Politics)",
            "پروفایل‌سازی رأی‌دهنده (Voter Profiling)",
            "حلقه بازخورد (Feedback Loop)",
            "دروازه‌بانی الگوریتمی (Algorithmic Gatekeeping)",
            "آزمون پیام (Message Testing)",
            "مهندسی افکار عمومی (Engineering the Public)",
        ],
        "studies": [
            "Tufekci, Z. (2014). Engineering the public. First Monday, 19(7).",
            "Howard, P. N. (2006). New media campaigns and the managed citizen. Cambridge University Press.",
        ],
        "theorists": "زنپ توفکچی؛ فیلیپ هاوارد",
        "theorists_text": "توفکچی (۲۰۱۴)",
        "year": 2014,
        "model": "داده شخصی → پروفایل فردی → پیام آزمون‌شده → حلقه بازخورد → مهندسی ترجیح سیاسی.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nتوفکچی سیاست محاسباتی را پیوند داده، الگوریتم و اقناع دید. نوآوری چارچوب، تحلیل حلقه بازخورد میان پایش و پیام است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با تحلیل داده کمپین، مصاحبه و مطالعه موردی انجام می‌شود. پژوهشی که تنها اثر تبلیغ را می‌سنجد، پایش پنهان را از دست می‌دهد؛ و پژوهشی که اثربخشی را مسلم می‌گیرد، شواهد ناکافی را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در نقد شفافیت است، اما باید با مطالعه زمینه سیاسی تکمیل شود. داده بی مقررات، به ابزار دستکاری بدل می‌شود.",
        "critique_text": "\n".join([
            "۱. اثربخشی: اقناع فردی بیش‌برآورد می‌شود.",
            "۲. اخلاق: رضایت آگاهانه نادیده می‌ماند.",
            "۳. نظارت: مرز کمپین و پایش محو می‌شود.",
            "۴. شواهد: داده کمپین شفاف نیست.",
            "۵. زمینه: مدل آمریکایی است.",
        ]),
        "example_text": "کمپینی که برای هر رأی‌دهنده پیامی متفاوت درباره یک موضوع واحد می‌فرستد، امکان گفت‌وگوی عمومی مشترک را تضعیف می‌کند؛ شهروندان دیگر یک واقعیت مشترک نمی‌بینند.",
    },
    "MC-708": {
        "summary": "(ویت، ۱۹۹۲) نظریه هشدار ترس در مدل فرایند موازی گسترده، سازوکار پیام ترس‌محور را توضیح می‌دهد. پیام ترس، تهدید را با شدت و آسیب‌پذیری ادراک‌شده می‌سازد. مخاطب سپس کارآمدی پاسخ و خودکارآمدی را می‌سنجد. اگر تهدید و کارآمدی هر دو بالا باشند، مخاطب به کنترل خطر می‌رسد و رفتار محافظتی می‌پذیرد. اگر تهدید بالا و کارآمدی پایین باشد، کنترل ترس رخ می‌دهد: انکار، اجتناب و مقاومت. ویت این مدل را بر پایه چارچوب کنترل خطر و کنترل ترس لونتال ساخت. راجرز پیش‌تر انگیزش حفاظتی را صورتبندی کرده بود. در کمپین سلامت و هشدار بحران، توازن تهدید و کارآمدی تعیین‌کننده است. همچنین پژوهش کمپین نشان داد پیام ترس باید مخاطب را در حل مسئله توانمند کند، نه فقط بترساند؛ افزودن توصیه مشخص، شاهد اجتماعی و پشتیبانی نهادی، کارآمدی پاسخ را بالا می‌برد و از مقاومت می‌کاهد. در مقابل، تکرار خالی هشدار بی راهکار به خستگی و بی‌حسی بدل می‌شود و اعتماد عمومی به نهاد سلامت را نیز فرسوده می‌کند.",
        "definition": "هشدار ترس، پیام اقناعی‌ای است که تهدید را برجسته می‌کند؛ اثر آن به سنجش تهدید و کارآمدی بستگی دارد و تنها با کارآمدی بالا به رفتار محافظتی می‌انجامد.",
        "main_problem": "مسئله این است که چرا برخی پیام‌های ترس‌محور رفتار را تغییر می‌دهند و برخی آن را بدتر می‌کنند. پاسخ، تعامل تهدید و کارآمدی است. پرسش دوم، اخلاق است: مرز آگاهی‌بخشی و ایجاد ترس کجاست.",
        "mechanism": "۱. سنجش تهدید: شدت و آسیب‌پذیری ادراک‌شده.\n۲. سنجش کارآمدی: کارآمدی پاسخ و خودکارآمدی.\n۳. کنترل خطر: پذیرش رفتار محافظتی.\n۴. کنترل ترس: انکار، اجتناب و مقاومت.\n۵. آستانه: تهدید بالا بی کارآمدی، اثر معکوس دارد.\n۶. پیام دومرحله‌ای: ترس باید با راهکار همراه شود.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا کمپین سیگار با تصویر هولناک بی راه ترک، مقاومت می‌سازد، چرا هشدار بحران باید همراه دستور عمل باشد و چرا پیام سلامت ترس‌محور در مخاطب کم‌اعتماد به نهاد، پس‌زننده می‌شود. نکته مهم این است که ترس به‌تنهایی انگیزه نمی‌سازد؛ راهکار باورپذیر می‌سازد.",
        "assumptions": [
            "ترس، سنجش تهدید را فعال می‌کند.",
            "کارآمدی، مسیر پاسخ را تعیین می‌کند.",
            "ترس بی راهکار، مقاومت می‌سازد.",
        ],
        "principles": [
            "تهدید و کارآمدی با هم اثر می‌کنند.",
            "پیام باید راهکار عملی داشته باشد.",
            "اعتماد به منبع، کارآمدی را تعدیل می‌کند.",
        ],
        "critiques": [
            "۱. اخلاق: ایجاد ترس بی رضایت، مسئله‌دار است.\n۲. اثر معکوس: ترس بالا می‌تواند اجتناب بسازد.\n۳. فرهنگ: آستانه ترس فرهنگی است.\n۴. سنجش: تهدید ادراک‌شده سخت اندازه‌گیری می‌شود.\n۵. زمان: اثر بلندمدت کم‌تر بررسی شده است.",
        ],
        "applications": [
            "کمپین سلامت: طراحی پیام ترس همراه راهکار.",
            "هشدار بحران: پیوند تهدید و دستور عمل.",
            "تبلیغات ایمنی: افزایش کارآمدی ادراک‌شده.",
            "سواد رسانه‌ای: شناخت دستکاری ترس.",
        ],
        "evolution": "راجرز در ۱۹۷۵ انگیزش حفاظتی را صورتبندی کرد و ویت در ۱۹۹۲ مدل فرایند موازی گسترده را با تفکیک کنترل خطر و کنترل ترس عرضه کرد. پژوهش سلامت بعدی، شرایط مرزی را افزود.",
        "key_concepts": [
            "هشدار ترس (Fear Appeal)",
            "سنجش تهدید (Threat Appraisal)",
            "سنجش کارآمدی (Efficacy Appraisal)",
            "کنترل خطر (Danger Control)",
            "کنترل ترس (Fear Control)",
            "انگیزش حفاظتی (Protection Motivation)",
        ],
        "studies": [
            "Witte, K. (1992). Putting the fear back into fear appeals. Communication Monographs, 59(4), 329-349.",
            "Rogers, R. W. (1975). A protection motivation theory of fear appeals and attitude change. Journal of Psychology, 91(1), 93-114.",
        ],
        "theorists": "کیم ویت؛ رونالد راجرز",
        "theorists_text": "ویت (۱۹۹۲)؛ راجرز (۱۹۷۵)",
        "year": 1992,
        "model": "پیام ترس → سنجش تهدید و کارآمدی → کنترل خطر (رفتار محافظتی) یا کنترل ترس (اجتناب).",
        "detailed_analysis": "۱. بنیان و منطق نظری\nویت مدل را بر چارچوب کنترل خطر و کنترل ترس لونتال ساخت و نقش کارآمدی را برجسته کرد. نوآوری چارچوب، توضیح شکست پیام ترس است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با آزمایش پیام، مقیاس تهدید و کارآمدی و مشاهده رفتار انجام می‌شود. پژوهشی که تنها نگرش را می‌سنجد، اجتناب را از دست می‌دهد؛ و پژوهشی که ترس را مستقل از کارآمدی می‌سنجد، اثر تعاملی را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در طراحی کمپین سلامت است، اما باید با اخلاق ارتباط تکمیل شود. ترس بی راهکار، به بی‌اعتمادی بدل می‌شود.",
        "critique_text": "\n".join([
            "۱. اخلاق: ترس بی رضایت مسئله‌دار است.",
            "۲. اثر معکوس: ترس بالا اجتناب می‌سازد.",
            "۳. فرهنگ: آستانه ترس فرهنگی است.",
            "۴. سنجش: تهدید ادراکی سخت اندازه‌پذیر است.",
            "۵. زمان: اثر بلندمدت کم بررسی شده است.",
        ]),
        "example_text": "پوستر هشدار بلای طبیعی که تنها ویرانی را نشان می‌دهد، ترس می‌سازد اما بی نقشه تخلیه، اجتناب می‌آفریند؛ افزودن مسیر و شماره تماس، آن را به کنترل خطر بدل می‌کند.",
    },
    "MC-713": {
        "summary": "(تامپسون و همکاران، ۱۹۹۹) نظریه تصویر بدن و رسانه، اثر فشارهای اجتماعی‌فرهنگی بر تصویر بدن را توضیح می‌دهد. مدل تأثیر سه‌گانه، سه منبع فشار را برمی‌شمارد: همسالان، خانواده و رسانه. این فشارها با درونی‌سازی آرمان لاغری و مقایسه اجتماعی ظاهر، به نارضایتی از بدن می‌انجامند. فستینگر مقایسه اجتماعی را پیش‌تر صورتبندی کرده بود. پژوهش بعدی نشان داد شبکه اجتماعی، مقایسه را پیوسته و فراگیر می‌کند. برای مردان نیز آرمان عضلانی مشابهی عمل می‌کند. سواد رسانه‌ای و تنوع بازنمایی، از مداخلات شناخته‌شده‌اند. نظریه، رسانه را تنها علت نمی‌داند، بلکه آن را در شبکه‌ای از فشارها می‌نشاند. همچنین پژوهش نشان می‌دهد تغییر معیار زیبایی به تنهایی کافی نیست؛ کاهش مواجهه با محتوای ویرایش‌شده، آموزش مهارت نقد تصویر و تقویت حمایت اجتماعی، اثر فشار سه‌گانه را کاهش می‌دهند. از این رو، مسئولیت تنها بر دوش فرد نیست و طراحی پلتفرم و سیاست محتوا نیز در این زنجیره سهم دارند و بدون آن، مداخله فردی محدود می‌ماند؛ به همین دلیل، تنوع بازنمایی بدن در رسانه را باید بخشی از بهداشت عمومی شمرد، نه سلیقه بازار.",
        "definition": "تصویر بدن، بازنمایی ذهنی فرد از ظاهر خویش و نگرش او به آن است و نظریه رسانه‌ای، نقش فشار همسالان، خانواده و تصاویر رسانه‌ای را در شکل‌گیری نارضایتی از بدن توضیح می‌دهد.",
        "main_problem": "مسئله این است که چرا مواجهه با تصاویر آرمانی، نارضایتی از بدن می‌سازد. پاسخ، درونی‌سازی آرمان و مقایسه اجتماعی است. پرسش دوم، مداخله است: کدام راهبرد می‌تواند اثر منفی را کاهش دهد.",
        "mechanism": "۱. فشار سه‌گانه: همسال، خانواده و رسانه.\n۲. درونی‌سازی آرمان: پذیرش لاغری یا عضلانی‌بودن به‌عنوان معیار.\n۳. مقایسه اجتماعی: سنجش خود با تصویر آرمانی.\n۴. شکاف ادراکی: فاصله خود و آرمان، نارضایتی می‌سازد.\n۵. تکرار مواجهه: رسانه شبکه‌ای، مقایسه را پیوسته می‌کند.\n۶. مداخله: سواد رسانه‌ای و تنوع بازنمایی.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا مجلات مد و شبکه‌های تصویری با فیلتر و ویرایش، آرمانی دست‌نیافتنی می‌سازند، چرا کمپین تنوع بدن اثر دارد و چرا نوجوان بیشتر آسیب‌پذیر است. نکته مهم این است که رسانه تنها عامل نیست؛ خانواده و همسال و ویژگی فردی نیز نقش دارند.",
        "assumptions": [
            "تصویر بدن از فشار اجتماعی‌فرهنگی اثر می‌گیرد.",
            "درونی‌سازی آرمان، نارضایتی می‌سازد.",
            "رسانه یکی از چند منبع فشار است.",
        ],
        "principles": [
            "مقایسه اجتماعی میانجی اثر رسانه است.",
            "تکرار مواجهه، اثر را تشدید می‌کند.",
            "سواد رسانه‌ای اثر منفی را کاهش می‌دهد.",
        ],
        "critiques": [
            "۱. علت‌یابی: جهت علیت آزمایشی سخت اثبات می‌شود.\n۲. فرهنگ: آرمان بدن فرهنگی است.\n۳. تفاوت فردی: آسیب‌پذیری یکسان نیست.\n۴. فراتر از لاغری: عضلانی‌بودن و سالم‌نمایی کم‌تر پوشش می‌یابد.\n۵. سنجش: تصویر بدن سخت اندازه‌گیری می‌شود.",
        ],
        "applications": [
            "سواد رسانه‌ای: نقد تصویر آرمانی ویرایش‌شده.",
            "سیاست محتوا: تنوع بازنمایی بدن.",
            "بهداشت روان: پیشگیری از نارضایتی بدن.",
            "تبلیغات مسئول: پرهیز از آرمان دست‌نیافتنی.",
        ],
        "evolution": "تامپسون و همکاران در ۱۹۹۹ مدل تأثیر سه‌گانه را عرضه کردند. پژوهش شبکه اجتماعی و تصویر بدن، مقایسه پیوسته و ایده‌آل عضلانی را به چارچوب افزود.",
        "key_concepts": [
            "تصویر بدن (Body Image)",
            "مدل تأثیر سه‌گانه (Tripartite Influence Model)",
            "درونی‌سازی آرمان (Ideal Internalization)",
            "مقایسه اجتماعی (Social Comparison)",
            "نارضایتی از بدن (Body Dissatisfaction)",
            "سواد رسانه‌ای (Media Literacy)",
        ],
        "studies": [
            "Thompson, J. K., Heinberg, L. J., Altabe, M., & Tantleff-Dunn, S. (1999). Exacting beauty. American Psychological Association.",
            "Festinger, L. (1954). A theory of social comparison processes. Human Relations, 7(2), 117-140.",
        ],
        "theorists": "جی. کوین تامپسون؛ لزلی هاینبرگ",
        "theorists_text": "تامپسون و همکاران (۱۹۹۹)",
        "year": 1999,
        "model": "فشار همسال، خانواده و رسانه → درونی‌سازی آرمان → مقایسه اجتماعی → نارضایتی از بدن.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nتامپسون و همکاران فشارهای فرهنگی را در مدلی سه‌گانه سازمان دادند. نوآوری چارچوب، جای دادن رسانه در شبکه فشار به جای علت یگانه است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با مقیاس تصویر بدن، تحلیل مواجهه و مدل معادلات ساختاری انجام می‌شود. پژوهشی که تنها مواجهه را می‌سنجد، درونی‌سازی را از دست می‌دهد؛ و پژوهشی که همبستگی را علیت می‌خواند، جهت اثر را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در تحلیل محتوای تصویری است، اما باید با مطالعه فرهنگ تکمیل شود. آرمان بی تنوع، به حذف بدن‌های واقعی بدل می‌شود.",
        "critique_text": "\n".join([
            "۱. علت‌یابی: علیت سخت اثبات می‌شود.",
            "۲. فرهنگ: آرمان بدن فرهنگی است.",
            "۳. تفاوت فردی: آسیب‌پذیری یکسان نیست.",
            "۴. فراتر از لاغری: ایده‌آل عضلانی کم پوشش است.",
            "۵. سنجش: تصویر بدن سخت اندازه‌پذیر است.",
        ]),
        "example_text": "نوجوانی که روزانه تصاویر ویرایش‌شده را در شبکه اجتماعی می‌بیند، خود را با آرمانی دست‌نیافتنی مقایسه می‌کند؛ آموزش نقد تصویر و نمایش بدن‌های متنوع، این مقایسه را تعدیل می‌کند.",
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
    "MC-708": ("نظریه هشدار ترس (مدل فرایند موازی گسترده)", "Fear Appeal Theory (EPPM)",
               "label repaired: mixed-language label -> standard Persian/English name"),
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
                                       "verified": n_verified, "batch": 111}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH111 THEORY DONE")


if __name__ == "__main__":
    main()
