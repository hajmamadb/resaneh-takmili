# -*- coding: utf-8 -*-
"""Batch 91: full documentation for MC-496, MC-498, MC-507, MC-508."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch91-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch91_theory.json"

S = {
    "MC-496": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="It Depends: A Contingency Theory of Accommodation in Public Relations",
             title_fa="بستگی دارد: نظریه اقتضایی سازش در روابط عمومی",
             authors="Cancel, A. E.; Cameron, G. T.; Sallot, L. M.; Mitrook, M. A.", year=1997,
             publisher="Journal of Public Relations Research",
             doi="10.1207/s1532754xjprr0901_02",
             url="https://www.tandfonline.com/doi/abs/10.1207/s1532754xjprr0901_02",
             language="en", isbn=None,
             citation="Cancel, A. E., Cameron, G. T., Sallot, L. M., & Mitrook, M. A. (1997). It depends: A contingency theory of accommodation in public relations. Journal of Public Relations Research, 9(1), 31-63. https://doi.org/10.1207/s1532754xjprr0901_02",
             locator="9(1):31-63", locator_type="page_range",
             supports="advocacy-accommodation continuum / contingent variables / it depends", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Testing the Contingency Theory of Accommodation in Public Relations",
             title_fa="آزمون نظریه اقتضایی سازش در روابط عمومی",
             authors="Cancel, A. E.; Mitrook, M. A.; Cameron, G. T.", year=1999,
             publisher="Public Relations Review",
             doi=None,
             url="https://www.sciencedirect.com/science/article/pii/S0363811199801611",
             language="en", isbn=None,
             citation="Cancel, A. E., Mitrook, M. A., & Cameron, G. T. (1999). Testing the contingency theory of accommodation in public relations. Public Relations Review, 25(2), 171-197.",
             locator="25(2):171-197", locator_type="page_range",
             supports="empirical test of contingent variables in conflict situations", verified=False),
    ],
    "MC-498": [
        dict(kind="BOOK",
             title_en="Effective Public Relations (6th ed.)",
             title_fa="روابط عمومی اثربخش (ویرایش ششم)",
             authors="Cutlip, S. M.; Center, A. H.; Broom, G. M.", year=1985,
             publisher="Prentice-Hall",
             doi=None, url=None, language="en", isbn=None,
             citation="Cutlip, S. M., Center, A. H., & Broom, G. M. (1985). Effective public relations (6th ed.). Prentice-Hall.",
             locator="ch. 8", locator_type="CHAPTER",
             supports="open systems model of public relations / boundary-spanning function", verified=True),
        dict(kind="BOOK",
             title_en="Using Research in Public Relations: Applications to Program Management",
             title_fa="کاربرد پژوهش در روابط عمومی: کاربردها در مدیریت برنامه",
             authors="Broom, G. M.; Dozier, D. M.", year=1990, publisher="Prentice Hall",
             doi=None, url=None, language="en", isbn=None,
             citation="Broom, G. M., & Dozier, D. M. (1990). Using research in public relations: Applications to program management. Prentice Hall.",
             locator="work", locator_type="work",
             supports="systems-based program planning and feedback", verified=False),
    ],
    "MC-507": [
        dict(kind="BOOK",
             title_en="Media Economics: Concepts and Issues",
             title_fa="اقتصاد رسانه: مفاهیم و مسائل",
             authors="Picard, R. G.", year=1989, publisher="Sage",
             doi=None,
             url="https://www.econbiz.de/Record/media-economics-concepts-and-issues-picard-robert/10004087537",
             language="en", isbn=None,
             citation="Picard, R. G. (1989). Media economics: Concepts and issues. Sage.",
             locator="work", locator_type="work",
             supports="dual product market / market structure / media economics framework", verified=True),
        dict(kind="BOOK",
             title_en="Strategic Management in the Media: Theory to Practice",
             title_fa="مدیریت راهبردی در رسانه: از نظریه تا عمل",
             authors="Kung, L.", year=2008, publisher="Sage",
             doi=None, url=None, language="en", isbn=None,
             citation="Kung, L. (2008). Strategic management in the media: Theory to practice. Sage.",
             locator="work", locator_type="work",
             supports="strategic management / balancing creative and commercial logics", verified=False),
    ],
    "MC-508": [
        dict(kind="BOOK_CHAPTER",
             title_en="Inequity in Social Exchange",
             title_fa="نابرابری در مبادله اجتماعی",
             authors="Adams, J. S.", year=1965, publisher="Academic Press",
             doi="10.1016/S0065-2601(08)60108-2",
             url="https://www.sciencedirect.com/science/chapter/bookseries/pii/S0065260108601082",
             language="en", isbn=None,
             citation="Adams, J. S. (1965). Inequity in social exchange. In L. Berkowitz (Ed.), Advances in experimental social psychology (Vol. 2, pp. 267-299). Academic Press. https://doi.org/10.1016/S0065-2601(08)60108-2",
             locator="pp. 267-299", locator_type="page_range",
             supports="outcome-input ratio / referent comparison / restoring equity", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Toward an Understanding of Inequity",
             title_fa="به سوی فهم نابرابری",
             authors="Adams, J. S.", year=1963,
             publisher="Journal of Abnormal and Social Psychology",
             doi=None, url=None, language="en", isbn=None,
             citation="Adams, J. S. (1963). Toward an understanding of inequity. Journal of Abnormal and Social Psychology, 67(5), 422-436.",
             locator="67(5):422-436", locator_type="page_range",
             supports="normative expectations / normative expectations and inequity tension", verified=False),
    ],
}

ENRICH = {
    "MC-496": {
        "summary": "(کانسل، کامرون، سالوت و میتروک، ۱۹۹۷) نظریه اقتضایی، روابط عمومی را نه یک‌سره ستیزه‌جویانه و نه یک‌سره سازش‌پذیر می‌بیند. سازمان در هر موقعیت، روی پیوستاری از «حمایت‌گری محض» تا «سازش محض» جای می‌گیرد و موضع خود را بر پایه مجموعه‌ای از متغیرهای درونی و بیرونی تنظیم می‌کند. پاسخ نظریه به پرسش موضع درست، جمله‌ای کوتاه است: بستگی دارد. سازمان می‌تواند در برابر یک عمومی ستیزه‌جو بایستد و در برابر عمومی دیگر سازش کند؛ موضع، ثابت نیست، راهبردی و موقعیتی است.",
        "definition": "نظریه اقتضایی روابط عمومی، چارچوبی است که موضع سازمان در برابر عمومی‌ها را روی پیوستاری از حمایت‌گری محض تا سازش محض تبیین می‌کند و جایگاه هر سازمان را تابعی از متغیرهای محیطی و سازمانی می‌داند؛ موضعی که می‌تواند به تفکیک عمومی، موضوع و زمان تغییر کند.",
        "main_problem": "مسئله این است که سازمان در تعارض با عمومی‌ها چه موضعی باید بگیرد: مقاومت، مذاکره یا سازش. مدل‌های پیشین، یکی از این دو قطب را تجویز می‌کردند؛ نظریه اقتضایی می‌پرسد چه شرایطی موضع را تعیین می‌کند. پرسش دوم، سنجش است: کدام متغیرها و با چه وزنی، موضع سازمان را به این سو یا آن سو می‌بَرند.",
        "mechanism": "۱. پیوستار دوگانه: موضع سازمان در هر لحظه، نقطه‌ای میان حمایت‌گری محض و سازش محض است؛ نه دو گزینه، بلکه طیفی از راهبردها.\n۲. متغیرهای بیرونی: شدت تهدید، محیط صنعت، فشار سیاسی و حقوقی، فعالیت عمومی‌های سازمان‌یافته و پوشش رسانه‌ای، سازمان را به سوی یکی از دو قطب می‌رانند.\n۳. متغیرهای درونی: اندازه و فرهنگ سازمان، ساختار تصمیم‌گیری، منابع و تجربه پیشین، دامنه حرکت را تعیین می‌کنند.\n۴. ائتلاف مسلط و جایگاه ارتباط: اگر کارکرد ارتباط در تصمیم‌گیری حاضر باشد، احتمال راهبرد سازش‌پذیرتر بیشتر است.\n۵. ویژگی‌های رابطه: تاریخ تعامل، اعتماد و سطح تنش میان سازمان و عمومی، هزینه هر موضع را تغییر می‌دهد.\n۶. مدیریت راهبردی تعارض: موضع در طول بحران بازتنظیم می‌شود؛ سازمان ممکن است ابتدا مقاومت و سپس سازش کند.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا سازمان در بحران‌های پرسروصدا موضع سخت می‌گیرد و در بحران‌های کم‌دیده سازش می‌کند، و چرا موضع سازمان در برابر رسانه‌های مختلف یکسان نیست. نکته مهم این است که «بستگی دارد» به معنای بی‌اصولی نیست؛ به معنای وابستگی موضع به مجموعه‌ای قابل شناسایی از شرایط است.",
        "assumptions": [
            "موضع سازمان پیوسته است، نه دوگانه.",
            "متغیرهای محیطی و سازمانی، موضع را به طور نظام‌مند تعیین می‌کنند.",
            "موضع می‌تواند به تفکیک عمومی و در طول زمان تغییر کند.",
        ],
        "principles": [
            "هیچ موضعی به‌طور پیشینی درست نیست؛ اقتضا تعیین‌کننده است.",
            "شناسایی عمومی و شدت تهدید، پیش‌شرط انتخاب موضع است.",
            "جایگاه کارکرد ارتباط در ائتلاف مسلط، دامنه سازش را گسترش می‌دهد.",
        ],
        "critiques": [
            "۱. فهرست بلند متغیرها: شمار متغیرها سنجش و آزمون تجربی را دشوار می‌کند.\n۲. تمرکز بر سازمان: تجربه و صدای عمومی‌ها در تعیین موضع کمتر دیده می‌شود.\n۳. نسبی‌گرایی: «بستگی دارد» می‌تواند به توجیه هر موضعی بدل شود.\n۴. آزمون محدود: شواهد تجربی بیشتر بر موارد معدود و زمینه آمریکایی استوار است.\n۵. نبود وزن‌دهی: نظریه نمی‌گوید کدام متغیرها مهم‌ترند.",
        ],
        "applications": [
            "مدیریت بحران: انتخاب موضع متناسب با شدت تهدید و عمومی هدف.",
            "تحلیل ذی‌نفعان: تفکیک موضع سازمان در برابر هر عمومی.",
            "آموزش روابط عمومی: آموزش تصمیم‌گیری اقتضایی به‌جای نسخه واحد.",
            "پژوهش تعارض: بررسی رابطه متغیرهای درونی و بیرونی با راهبرد سازمان.",
        ],
        "evolution": "کانسل و همکاران در ۱۹۹۷ نظریه را با پیوستار حمایت‌گری-سازش صورت‌بندی کردند و در ۱۹۹۹ آن را آزمودند. پژوهش بعدی، نظریه را به مدیریت راهبردی تعارض گسترد و متغیرهای دیجیتال و عمومی‌های شبکه‌ای را افزود.",
        "key_concepts": [
            "پیوستار حمایت‌گری-سازش (Advocacy-Accommodation Continuum)",
            "متغیرهای اقتضایی (Contingent Variables)",
            "مدیریت راهبردی تعارض (Strategic Conflict Management)",
            "ائتلاف مسلط (Dominant Coalition)",
            "عمومی فعال (Active Public)",
            "موضع راهبردی (Strategic Stance)",
        ],
        "studies": [
            "Cancel, A. E., Cameron, G. T., Sallot, L. M., & Mitrook, M. A. (1997). It depends: A contingency theory of accommodation in public relations. Journal of Public Relations Research, 9(1), 31-63.",
            "Cancel, A. E., Mitrook, M. A., & Cameron, G. T. (1999). Testing the contingency theory of accommodation in public relations. Public Relations Review, 25(2), 171-197.",
        ],
        "theorists": "کانسل، کامرون، سالوت و میتروک (۱۹۹۷)",
        "theorists_text": "کانسل، کامرون، سالوت و میتروک (۱۹۹۷)",
        "year": 1997,
        "model": "مدل پیوستاری: حمایت‌گری محض ← موضع اقتضایی ← سازش محض؛ موضع تابع متغیرهای بیرونی (تهدید، محیط، فشار) و درونی (ساختار، ائتلاف، رابطه).",
        "detailed_analysis": "۱. بنیان و منطق نظری\nنظریه اقتضایی در برابر دو سنت ایستاد: سنت تجویزی که سازش دوسویه را تنها راه درست می‌دانست و سنت واقع‌گرا که مقاومت را اصل می‌گرفت. نوآوری آن، تبدیل این دوگانه به پیوستار و جست‌وجوی شرایط تعیین‌کننده موضع بود؛ ایده‌ای که روابط عمومی را از اخلاق تجویزی به تحلیل موقعیتی برد.\n\n۲. منطق سنجش و دام‌های آن\nسنجش نیازمند تحلیل هم‌زمان محیط، سازمان و رابطه است. پژوهش‌هایی که تنها بیانیه‌های سازمان را کدگذاری می‌کنند، فشار عمومی‌ها را از دست می‌دهند؛ و پژوهش‌هایی که تنها نظر مدیران را می‌سنجند، تفاوت میان موضع رسمی و رفتار واقعی را نمی‌بینند.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در توضیح تنوع رفتار سازمانی است، اما باید با تحلیل قدرت و مسئولیت تکمیل شود. «بستگی دارد» بدون معیار اخلاقی می‌تواند به فرار از پاسخ‌گویی بدل شود؛ از این رو نظریه باید با پرسش از منافع عمومی همراه شود.",
        "critique_text": "\n".join([
            "۱. فهرست بلند متغیرها: شمار متغیرها سنجش و آزمون تجربی را دشوار می‌کند.",
            "۲. تمرکز بر سازمان: تجربه و صدای عمومی‌ها در تعیین موضع کمتر دیده می‌شود.",
            "۳. نسبی‌گرایی: «بستگی دارد» می‌تواند به توجیه هر موضعی بدل شود.",
            "۴. آزمون محدود: شواهد تجربی بیشتر بر موارد معدود و زمینه آمریکایی استوار است.",
            "۵. نبود وزن‌دهی: نظریه نمی‌گوید کدام متغیرها مهم‌ترند.",
        ]),
        "example_text": "یک شرکت غذایی با گزارش آلودگی روبه‌رو می‌شود. در برابر رسانه‌های ملی، موضع دفاعی می‌گیرد و از کیفیت محصول می‌گوید؛ در برابر انجمن‌های محلی، جلسه گفت‌وگو می‌پذیرد و فرایند تولید را بازبینی می‌کند. یک سازمان، دو موضع؛ تفاوت از اقتضای هر رابطه می‌آید.",
    },
    "MC-498": {
        "summary": "نظریه سیستمی، سازمان را نظامی باز می‌بیند که برای بقا باید با محیط خود مبادله کند. روابط عمومی در این چارچوب، کارکرد مرزی است: اطلاعات محیط را به سازمان می‌آورد و پیام سازمان را به محیط می‌برد و از طریق بازخورد، امکان سازگاری دوطرفه را فراهم می‌کند. کاتلیپ، سنتر و بروم این مدل را در «روابط عمومی اثربخش» صورت‌بندی کردند: روابط عمومی حلقه پیوند سازمان و عمومی‌هاست و سلامت این حلقه، به سلامت کل نظام وابسته است.",
        "definition": "نظریه سیستمی روابط عمومی، روابط عمومی را کارکرد مرزی سازمان در نظامی باز می‌داند که با دریافت درون‌داد از محیط، تولید و ارسال پیام و دریافت بازخورد، سازگاری متقابل سازمان و عمومی‌ها را ممکن می‌سازد.",
        "main_problem": "مسئله این است که روابط عمومی چگونه به بقا و سازگاری سازمان کمک می‌کند. پاسخ سیستمی این است که سازمانِ بسته محکوم به بحران است؛ سازمانی که اطلاعات محیط را دریافت، پردازش و به رفتار تبدیل نکند، از محیط عقب می‌ماند. پرسش دوم، مرز است: چه کسی و با چه اختیاری، اطلاعات بیرون را به تصمیم درون منتقل می‌کند.",
        "mechanism": "۱. سازمان به‌عنوان نظام باز: سازمان با محیط خود منابع، اطلاعات و مشروعیت مبادله می‌کند و بدون این مبادله نمی‌ماند.\n۲. زیرنظام‌ها و مرزها: تولید، بازاریابی و ارتباط، زیرنظام‌هایی‌اند که هر یک با بخشی از محیط در تعامل‌اند.\n۳. کارکرد مرزی: روابط عمومی روی مرز سازمان می‌ایستد و هم نماینده سازمان در بیرون و هم نماینده محیط در درون است.\n۴. درون‌داد، تبدیل و برون‌داد: اطلاعات محیط به تصمیم سازمان بدل می‌شود و پیام سازمان به محیط بازمی‌گردد.\n۵. بازخورد و تعادل: بازخورد، انحراف سازمان از انتظارات محیط را نشان می‌دهد و اصلاح را ممکن می‌کند.\n۶. سازگاری و تغییر: سازمان یا خود را با محیط تطبیق می‌دهد یا می‌کوشد محیط را تغییر دهد؛ روابط عمومی هر دو مسیر را پشتیبانی می‌کند.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا سازمان‌ها واحد رصد رسانه و افکار عمومی می‌سازند، چرا بازخورد به تصمیم‌گیری راهبردی راه می‌یابد و چرا سازمانی که فقط پیام می‌فرستد و گوش نمی‌دهد، در بحران غافلگیر می‌شود. نکته مهم این است که کارکرد مرزی، هم فرصت است و هم تنش: فرد مرزی هم‌زمان به دو نظام وفادار است.",
        "assumptions": [
            "سازمان، نظامی باز و وابسته به محیط است.",
            "روابط عمومی کارکرد مرزی میان سازمان و محیط است.",
            "بازخورد، شرط سازگاری و بقای سازمان است.",
        ],
        "principles": [
            "سازمان بدون دریافت اطلاعات محیط، تصمیم راهبردی نمی‌تواند بگیرد.",
            "کارکرد مرزی، هم به سازمان و هم به محیط پاسخ‌گوست.",
            "بازخورد، حلقه اصلاح تصمیم و رفتار است.",
        ],
        "critiques": [
            "۱. استعاره مکانیکی: زبان نظام و تعادل، سازمان را بیش از حد هماهنگ و بی‌کشمکش نشان می‌دهد.\n۲. کم‌توجهی به قدرت: نظریه کمتر می‌گوید چه کسی اطلاعات را کنترل می‌کند.\n۳. فرض تعادل: سازمان‌ها گاه در بی‌تعادلی پایدار و حتی تعارض ساختاری می‌مانند.\n۴. سنجش مرز: تعیین دقیق مرز سازمان و محیط در عمل دشوار است.\n۵. توصیفی بودن: مدل بیشتر توصیف می‌کند تا تبیین کند چرا برخی سازمان‌ها سازگارترند.",
        ],
        "applications": [
            "رصد رسانه و افکار عمومی: طراحی نظام دریافت و تحلیل بازخورد محیطی.",
            "برنامه‌ریزی ارتباطی: پیوند اهداف سازمان با انتظارات عمومی در چرخه برنامه.",
            "مدیریت بحران: شناسایی زودهنگام نشانه‌های محیطی پیش از بحران.",
            "ساختار سازمانی: تعریف جایگاه کارکرد مرزی و اختیار انتقال اطلاعات.",
        ],
        "evolution": "مدل نظام باز در کتاب‌های درسی روابط عمومی دهه ۱۹۸۰ صورت‌بندی شد و بعدها با نظریه‌های تعالی، مدیریت تعارض و رویکردهای شبکه‌ای ترکیب شد.",
        "key_concepts": [
            "نظام باز (Open System)",
            "کارکرد مرزی (Boundary-Spanning)",
            "درون‌داد و برون‌داد (Input and Output)",
            "بازخورد (Feedback)",
            "سازگاری با محیط (Environmental Adaptation)",
            "زیرنظام (Subsystem)",
        ],
        "studies": [
            "Cutlip, S. M., Center, A. H., & Broom, G. M. (1985). Effective public relations (6th ed.). Prentice-Hall.",
            "Broom, G. M., & Dozier, D. M. (1990). Using research in public relations. Prentice Hall.",
        ],
        "theorists": "کاتلیپ، سنتر و بروم",
        "theorists_text": "کاتلیپ، سنتر و بروم",
        "year": 1985,
        "model": "مدل نظام باز: محیط → درون‌داد → سازمان (زیرنظام‌ها) → برون‌داد → محیط؛ با بازخورد پیوسته و کارکرد مرزی روابط عمومی در هر دو جهت.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nنظریه سیستمی، روابط عمومی را از مجموعه‌ای از فنون به کارکردی ساختاری بدل کرد. ایده اصلی این بود که ارتباط، سازوکار سازگاری سازمان با محیط است؛ از این رو جایگاه روابط عمومی در ساختار سازمان، موضوعی راهبردی است و نه تشریفاتی.\n\n۲. منطق سنجش و دام‌های آن\nسنجش نیازمند ردیابی جریان اطلاعات از محیط به تصمیم و از تصمیم به محیط است. پژوهش‌هایی که تنها حجم پوشش رسانه‌ای را می‌شمارند، تبدیل اطلاعات به تصمیم را نمی‌بینند؛ و پژوهش‌هایی که تنها ساختار رسمی را ترسیم می‌کنند، جریان‌های غیررسمی را از دست می‌دهند.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در نشان دادن وابستگی سازمان به محیط است، اما باید با تحلیل قدرت و منافع تکمیل شود. در محیط پلتفرمی، مرز سازمان و محیط نفوذپذیرتر شده است؛ بازخورد سریع‌تر و پرسروصداتر است و کارکرد مرزی، هم فرصت بیشتری دارد و هم فشار بیشتری.",
        "critique_text": "\n".join([
            "۱. استعاره مکانیکی: زبان نظام و تعادل، سازمان را بیش از حد هماهنگ نشان می‌دهد.",
            "۲. کم‌توجهی به قدرت: نظریه کمتر می‌گوید چه کسی اطلاعات را کنترل می‌کند.",
            "۳. فرض تعادل: سازمان‌ها گاه در بی‌تعادلی پایدار می‌مانند.",
            "۴. سنجش مرز: تعیین دقیق مرز سازمان و محیط در عمل دشوار است.",
            "۵. توصیفی بودن: مدل بیشتر توصیف می‌کند تا تبیین.",
        ]),
        "example_text": "واحد ارتباطات یک بیمارستان، گزارش‌های شبکه‌های اجتماعی درباره انتظار زمان ویزیت را جمع می‌کند، به مدیریت منتقل می‌کند و پس از تغییر فرایند نوبت‌دهی، نتیجه را به همان شبکه‌ها بازمی‌گرداند. حلقه درون‌داد-تصمیم-برون‌داد-بازخورد، همان مدل نظام باز است.",
    },
    "MC-507": {
        "summary": "(پیکارد، ۱۹۸۹؛ کونگ) مدیریت رسانه، کاربرد اصول اقتصاد و مدیریت راهبردی در سازمان‌های رسانه‌ای است. پیکارد نشان داد که رسانه‌ها در بازار دوگانه فعالیت می‌کنند: محتوا را به مخاطب و مخاطب را به آگهی‌دهنده می‌فروشند. از این‌رو تصمیم‌های محتوایی و تجاری در هم تنیده‌اند. کونگ بر مدیریت راهبردی تأکید کرد: سازمان رسانه‌ای باید میان منطق خلاقیت و منطق تجارت تعادل برقرار کند. در رسانه خدمات عمومی، این تعادل با مأموریت عمومی و منافع جمعی سنجیده می‌شود، نه تنها با سود.",
        "definition": "مدیریت رسانه، مجموعه تصمیم‌ها و رویه‌هایی است که منابع، تولید، توزیع و بازار سازمان رسانه‌ای را در تعامل با محیط رقابتی و مأموریت عمومی هماهنگ می‌کند؛ حوزه‌ای میان اقتصاد رسانه، راهبرد سازمانی و مدیریت نیروی کار خلاق.",
        "main_problem": "مسئله این است که سازمان رسانه‌ای چگونه هم‌زمان به بازار و به مأموریت پاسخ می‌دهد. رسانه، بنگاه اقتصادی است و به درآمد نیاز دارد؛ اما محصولش فرهنگ و اطلاعات است و پیامد عمومی دارد. پرسش دوم، مدیریت تعادل است: چگونه می‌توان خلاقیت را که پیش‌شرط کیفیت است، با انضباط هزینه و راهبرد بازار هم‌نشین کرد.",
        "mechanism": "۱. بازار دوگانه: رسانه محتوا را به مخاطب می‌فروشد و دسترسی مخاطب را به آگهی‌دهنده؛ هر دو بازار بر تصمیم محتوایی اثر می‌گذارند.\n۲. ساختار بازار و رقابت: شمار رقبا، موانع ورود و درجه تمرکز، فضای راهبردی سازمان را تعیین می‌کند.\n۳. صرفه‌های مقیاس و دامنه: تولید مشترک، بازنشر و بسته‌بندی محتوا، هزینه واحد را کاهش می‌دهد و به ادغام و تمرکز می‌انجامد.\n۴. مدیریت راهبردی و مدل کسب‌وکار: انتخاب بازار، منبع درآمد و زنجیره ارزش، هویت اقتصادی سازمان را می‌سازد.\n۵. تعادل منطق خلاق و تجاری: مدیر رسانه باید هم به کیفیت و اعتبار حرفه‌ای و هم به پایداری مالی پاسخ دهد.\n۶. مأموریت عمومی و ارزش اجتماعی: در رسانه خدمات عمومی، معیار موفقیت فراتر از سهم بازار است و دسترسی، تنوع و منفعت جمعی را در بر می‌گیرد.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا مدل‌های اشتراکی و تبلیغاتی، محتوای متفاوتی تولید می‌کنند، چرا تمرکز رسانه‌ای تنوع را کاهش می‌دهد و چرا رسانه خدمات عمومی در محیط پلتفرمی با بحران مشروعیت و تأمین مالی روبه‌روست. نکته مهم این است که تصمیم اقتصادی رسانه، تصمیم فرهنگی هم هست.",
        "assumptions": [
            "رسانه بنگاهی است که در بازار دوگانه فعالیت می‌کند.",
            "تصمیم‌های تجاری و محتوایی به هم وابسته‌اند.",
            "پایداری سازمان رسانه‌ای به تعادل خلاقیت و انضباط مالی وابسته است.",
        ],
        "principles": [
            "ساختار بازار، دامنه تنوع محتوایی را محدود یا باز می‌کند.",
            "مأموریت عمومی، معیار موفقیت را از سود فراتر می‌برد.",
            "مدیریت رسانه، مدیریت هم‌زمان خلاقیت و منابع است.",
        ],
        "critiques": [
            "۱. غلبه منطق بازار: تمرکز بر اقتصاد می‌تواند منفعت عمومی و کیفیت را کم‌رنگ کند.\n۲. سنجش ارزش اجتماعی: اندازه‌گیری ارزش عمومی رسانه دشوار و اغلب کیفی است.\n۳. تمرکز بر سازمان‌های بزرگ: کسب‌وکارهای کوچک و رسانه‌های اجتماعی کمتر پوشش می‌یابند.\n۴. تحول پلتفرم: مدل‌های کلاسیک با اقتصاد توجه و الگوریتم به‌سختی تطبیق می‌یابند.\n۵. کم‌توجهی به نیروی کار: شرایط کار خبرنگاران و تولیدکنندگان خلاق کمتر تحلیل می‌شود.",
        ],
        "applications": [
            "راهبرد رسانه: انتخاب مدل درآمدی و بازار متناسب با مأموریت.",
            "سیاست رسانه‌ای: تحلیل پیامد تمرکز و ادغام بر تنوع.",
            "مدیریت تحریریه: تعادل کیفیت حرفه‌ای و فشار اقتصادی.",
            "رسانه خدمات عمومی: طراحی معیارهای ارزیابی فراتر از سهم بازار.",
        ],
        "evolution": "پیکارد در ۱۹۸۹ اقتصاد رسانه را به‌عنوان حوزه نظام‌مند معرفی کرد و کونگ در دهه ۲۰۰۰ مدیریت راهبردی رسانه را بسط داد. پژوهش بعدی، اقتصاد پلتفرم، مدل‌های اشتراکی و بحران تأمین مالی رسانه خدمات عمومی را افزود.",
        "key_concepts": [
            "بازار دوگانه (Dual Product Market)",
            "اقتصاد رسانه (Media Economics)",
            "مدیریت راهبردی رسانه (Strategic Media Management)",
            "تمرکز رسانه‌ای (Media Concentration)",
            "منطق خلاق و تجاری (Creative-Commercial Logics)",
            "رسانه خدمات عمومی (Public Service Media)",
        ],
        "studies": [
            "Picard, R. G. (1989). Media economics: Concepts and issues. Sage.",
            "Kung, L. (2008). Strategic management in the media: Theory to practice. Sage.",
        ],
        "theorists": "پیکارد؛ کونگ",
        "theorists_text": "پیکارد (۱۹۸۹)؛ کونگ (۲۰۰۸)",
        "year": 1989,
        "model": "مدل بازار دوگانه + راهبرد: ساختار بازار → مدل کسب‌وکار → تصمیم محتوایی → مخاطب و درآمد؛ با قید مأموریت عمومی در رسانه خدمات عمومی.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nمدیریت رسانه، پیوند economics و مدیریت راهبردی با ویژگی‌های خاص محصول فرهنگی است. نوآوری پیکارد، صورت‌بندی بازار دوگانه بود؛ نوآوری کونگ، نشان دادن تنش میان منطق خلاق و تجاری در تصمیم راهبردی. این چارچوب، رسانه را نه فقط نهاد فرهنگی و نه فقط بنگاه، بلکه هر دو می‌بیند.\n\n۲. منطق سنجش و دام‌های آن\nسنجش نیازمند ترکیب شاخص‌های بازار (درآمد، سهم، هزینه) با شاخص‌های کیفیت و تنوع است. پژوهش‌هایی که تنها سود را می‌سنجند، ارزش عمومی را از دست می‌دهند؛ و پژوهش‌هایی که تنها محتوای آرمانی را می‌سنجند، پایداری سازمان را نادیده می‌گیرند.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در توضیح رفتار اقتصادی رسانه است، اما باید با تحلیل قدرت و منفعت عمومی تکمیل شود. در محیط پلتفرمی، مرز میان رسانه و پلتفرم مخدوش شده است؛ مدل‌های درآمدی داده‌محور، هم فرصت و هم تهدید برای استقلال حرفه‌ای‌اند.",
        "critique_text": "\n".join([
            "۱. غلبه منطق بازار: تمرکز بر اقتصاد می‌تواند منفعت عمومی را کم‌رنگ کند.",
            "۲. سنجش ارزش اجتماعی: اندازه‌گیری ارزش عمومی رسانه دشوار است.",
            "۳. تمرکز بر سازمان‌های بزرگ: کسب‌وکارهای کوچک کمتر پوشش می‌یابند.",
            "۴. تحول پلتفرم: مدل‌های کلاسیک با اقتصاد توجه به‌سختی تطبیق می‌یابند.",
            "۵. کم‌توجهی به نیروی کار: شرایط کار تولیدکنندگان خلاق کمتر تحلیل می‌شود.",
        ]),
        "example_text": "یک رسانه خبری که تنها بر تبلیغات تکیه دارد، برای افزایش بازدید به محتوای پرسروصدا گرایش می‌یابد؛ همان رسانه با افزودن اشتراک و عضویت، انگیزه‌ای برای کیفیت و اعتماد می‌سازد. تغییر مدل درآمدی، تغییر محتوا را به همراه دارد؛ این همان پیوند بازار دوگانه و تصمیم محتوایی است.",
    },
    "MC-508": {
        "summary": "(آدامز، ۱۹۶۵) نظریه برابری می‌گوید افراد در سازمان، نسبت ستاده‌ها به داده‌های خود را با فردی مرجع مقایسه می‌کنند. اگر نسبت‌ها نابرابر باشد، تنشی روانی پدید می‌آید و فرد می‌کوشد آن را جبران کند: با تغییر داده یا ستاده، بازتفسیر شناختی، تغییر مرجع مقایسه یا ترک رابطه. نابرابری به زیان فرد به خشم و در جهت سود او به احساس گناه می‌انجامد. این نظریه، پایه نظریه‌های عدالت سازمانی شد.",
        "definition": "نظریه برابری، نظریه‌ای انگیزشی است که رضایت و رفتار افراد را تابع ادراک آن‌ها از تناسب میان ستاده‌ها و داده‌ها در مقایسه با مرجع می‌داند و نابرابری را محرک تلاش برای بازگرداندن تعادل می‌شمارد.",
        "main_problem": "مسئله این است که چرا افراد با وجود شرایط عینی مشابه، رضایت و انگیزه متفاوت دارند. پاسخ آدامز این است که افراد به ارزش مطلق پاداش نگاه نمی‌کنند؛ نسبت پاداش به تلاش را با دیگری مقایسه می‌کنند. پرسش دوم، واکنش است: فرد در برابر نابرابری چه می‌کند و چه زمانی به جای اصلاح، رابطه را ترک می‌کند.",
        "mechanism": "۱. داده‌ها: تلاش، مهارت، آموزش، زمان و تعهدی که فرد به رابطه می‌آورد.\n۲. ستاده‌ها: دستمزد، ارتقا، احترام، امنیت و پاداش‌های نمادین که از رابطه می‌گیرد.\n۳. مرجع مقایسه: همکار، گروه مشابه یا معیار درونی که فرد خود را با آن می‌سنجد؛ انتخاب مرجع، نتیجه ادراک را تغییر می‌دهد.\n۴. ادراک نابرابری و تنش: ناهم‌ترازی نسبت‌ها، تنشی انگیزشی می‌سازد که فرد می‌کوشد کاهش دهد.\n۵. راهبردهای بازگرداندن برابری: کاهش تلاش، افزایش ستاده، بازتفسیر شناختی، تغییر مرجع یا ترک رابطه.\n۶. جهت نابرابری: کم‌پرداختی به خشم و رفتار اعتراضی، بیش‌پرداختی به گناه و افزایش تلاش می‌انجامد.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا مقایسه دستمزد و اعتبار میان خبرنگاران و تولیدکنندگان محتوا به نارضایتی می‌انجامد، چرا شفافیت در پاداش، ادراک عدالت را تغییر می‌دهد و چرا ادراک بی‌عدالتی، انگیزه همکاری را کاهش می‌دهد. نکته مهم این است که عدالت، ادراکی است؛ پاداش یکسان می‌تواند برای دو نفر ناعادلانه به نظر برسد.",
        "assumptions": [
            "افراد نسبت ستاده به داده خود را با مرجع مقایسه می‌کنند.",
            "ادراک نابرابری، تنش انگیزشی می‌سازد.",
            "افراد می‌کوشند تعادل ادراک‌شده را بازگردانند.",
        ],
        "principles": [
            "عدالت ادراکی است، نه فقط عینی.",
            "انتخاب مرجع مقایسه، رضایت را شکل می‌دهد.",
            "نابرابری پایدار، به کاهش تلاش یا ترک رابطه می‌انجامد.",
        ],
        "critiques": [
            "۱. فرض عقلانیت محاسبه‌گر: افراد همیشه داده و ستاده را دقیق محاسبه نمی‌کنند.\n۲. ابهام مرجع: نظریه نمی‌گوید فرد چه زمانی و چرا مرجع خاصی را برمی‌گزیند.\n۳. سنجش ذهنی: وزن داده‌ها و ستاده‌ها برای افراد متفاوت و دشوارسنجش است.\n۴. کم‌توجهی به رویه: نسخه اولیه بر توزیع نتیجه متمرکز است و عدالت رویه‌ای را در بر نمی‌گیرد.\n۵. تفاوت فرهنگی: معنای برابری و مرجع مقایسه در فرهنگ‌های مختلف یکسان نیست.",
        ],
        "applications": [
            "مدیریت منابع انسانی: شفاف‌سازی معیار پاداش و ارتقا.",
            "تحلیل رضایت شغلی: بررسی ادراک برابری در گروه‌های کاری.",
            "طراحی نظام پاداش: کاهش نابرابری ادراک‌شده میان نقش‌های مشابه.",
            "عدالت سازمانی: پیوند برابری توزیعی با رویه‌های منصفانه و ارتباط محترمانه.",
        ],
        "evolution": "آدامز نظریه را در ۱۹۶۳ و ۱۹۶۵ صورت‌بندی کرد. پژوهش بعدی آن را به نظریه عدالت سازمانی گسترد و سه بُعد توزیعی، رویه‌ای و تعاملی را افزود.",
        "key_concepts": [
            "نسبت ستاده به داده (Outcome-Input Ratio)",
            "مرجع مقایسه (Referent)",
            "نابرابری ادراک‌شده (Perceived Inequity)",
            "بازگرداندن برابری (Restoring Equity)",
            "عدالت توزیعی (Distributive Justice)",
            "عدالت رویه‌ای (Procedural Justice)",
        ],
        "studies": [
            "Adams, J. S. (1965). Inequity in social exchange. In Advances in experimental social psychology (Vol. 2, pp. 267-299). Academic Press.",
            "Adams, J. S. (1963). Toward an understanding of inequity. Journal of Abnormal and Social Psychology, 67(5), 422-436.",
        ],
        "theorists": "جان استیسی آدامز (۱۹۶۵)",
        "theorists_text": "جان استیسی آدامز (۱۹۶۳؛ ۱۹۶۵)",
        "year": 1965,
        "model": "مدل برابری: داده‌ها و ستاده‌ها → مقایسه با مرجع → ادراک برابری یا نابرابری → تنش → راهبرد بازگرداندن تعادل (تغییر داده، تغییر ستاده، بازتفسیر، تغییر مرجع، ترک رابطه).",
        "detailed_analysis": "۱. بنیان و منطق نظری\nنظریه برابری، انگیزه را از سطح فرد به سطح رابطه اجتماعی برد. نوآوری آن این بود که پاداش مطلق را کنار گذاشت و نسبت پاداش به تلاش را در مقایسه با دیگری محور کرد؛ ایده‌ای که پایه نظریه‌های عدالت سازمانی و اقتصاد رفتاری شد.\n\n۲. منطق سنجش و دام‌های آن\nسنجش نیازمند شناسایی مرجع مقایسه و وزن ذهنی داده‌ها و ستاده‌هاست. پژوهش‌هایی که تنها دستمزد عینی را می‌سنجند، ادراک عدالت را از دست می‌دهند؛ و پژوهش‌هایی که تنها رضایت را می‌سنجند، منبع نابرابری را نشان نمی‌دهند.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در توضیح واکنش به نابرابری است، اما باید با عدالت رویه‌ای و تعاملی تکمیل شود. در سازمان‌های رسانه‌ای، مقایسه اعتبار و دیده‌شدن، به‌اندازه دستمزد اهمیت دارد؛ از این رو تحلیل عدالت باید پاداش‌های نمادین را نیز در بر گیرد.",
        "critique_text": "\n".join([
            "۱. فرض عقلانیت محاسبه‌گر: افراد همیشه داده و ستاده را دقیق محاسبه نمی‌کنند.",
            "۲. ابهام مرجع: نظریه نمی‌گوید فرد چرا مرجع خاصی را برمی‌گزیند.",
            "۳. سنجش ذهنی: وزن داده‌ها و ستاده‌ها برای افراد متفاوت است.",
            "۴. کم‌توجهی به رویه: نسخه اولیه عدالت رویه‌ای را در بر نمی‌گیرد.",
            "۵. تفاوت فرهنگی: معنای برابری در فرهنگ‌های مختلف یکسان نیست.",
        ]),
        "example_text": "دو خبرنگار با حجم کار مشابه، دستمزد متفاوت می‌گیرند. خبرنگار کم‌پرداخت‌تر ابتدا تلاش خود را کاهش می‌دهد؛ وقتی تفاوت ادامه یابد، مرجع مقایسه را تغییر می‌دهد یا سازمان را ترک می‌کند. سازمان اگر معیار پاداش را شفاف کند، ادراک نابرابری و هزینه ترک را کاهش می‌دهد.",
    },
}

REQUIRED_SECTIONS = REQUIRED_SECTIONS = ["summary", "definition", "main_problem", "mechanism", "assumptions",
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
                                       "verified": n_verified, "batch": 91}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH91 THEORY DONE")


if __name__ == "__main__":
    main()
