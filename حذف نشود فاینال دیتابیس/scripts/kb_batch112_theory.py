# -*- coding: utf-8 -*-
"""Batch 112: full documentation for MC-693, MC-685, MC-677, MC-668."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch112-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch112_theory.json"

S = {
    "MC-693": [
        dict(kind="BOOK",
             title_en="The Modern World-System I: Capitalist Agriculture and the Origins of the European World-Economy in the Sixteenth Century",
             title_fa="نظام جهانی مدرن، جلد یک: کشاورزی سرمایه‌داری و خاستگاه‌های اقتصاد جهانی اروپا در سده شانزدهم",
             authors="Wallerstein, I.", year=1974, publisher="Academic Press",
             doi=None, url="https://www.jstor.org/stable/10.1525/j.ctt1pnrj9",
             language="en", isbn=None,
             citation="Wallerstein, I. (1974). The modern world-system I: Capitalist agriculture and the origins of the European world-economy in the sixteenth century. Academic Press.",
             locator="work", locator_type="work",
             supports="capitalist world-economy, core-periphery division of labor", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Rise and Future Demise of the World Capitalist System: Concepts for Comparative Analysis",
             title_fa="برآمدن و فرجام نظام سرمایه‌داری جهانی: مفاهیمی برای تحلیل تطبیقی",
             authors="Wallerstein, I.", year=1974, publisher="Comparative Studies in Society and History",
             doi=None, url=None, language="en", isbn=None,
             citation="Wallerstein, I. (1974). The rise and future demise of the world capitalist system: Concepts for comparative analysis. Comparative Studies in Society and History, 16(4), 387-415.",
             locator="16(4):387-415", locator_type="page_range",
             supports="world-system as unit of analysis", verified=False),
    ],
    "MC-685": [
        dict(kind="BOOK",
             title_en="Communication, Action, and Meaning: The Creation of Social Realities",
             title_fa="ارتباط، کنش و معنا: آفرینش واقعیت‌های اجتماعی",
             authors="Pearce, W. B.; Cronen, V. E.", year=1980, publisher="Praeger",
             doi=None, url="https://digitalcommons.usu.edu/unf_research/56/",
             language="en", isbn="978-0-03-057611-9",
             citation="Pearce, W. B., & Cronen, V. E. (1980). Communication, action, and meaning: The creation of social realities. Praeger.",
             locator="work", locator_type="work",
             supports="hierarchy of meaning and coordinated management of meaning", verified=True),
        dict(kind="BOOK",
             title_en="Making Social Worlds: A Communication Perspective",
             title_fa="ساختن جهان‌های اجتماعی: چشم‌اندازی ارتباطی",
             authors="Pearce, W. B.", year=2007, publisher="Blackwell",
             doi=None, url=None, language="en", isbn=None,
             citation="Pearce, W. B. (2007). Making social worlds: A communication perspective. Blackwell.",
             locator="work", locator_type="work",
             supports="dialogic and reflexive elaboration of CMM", verified=False),
    ],
    "MC-677": [
        dict(kind="BOOK",
             title_en="On Collective Memory",
             title_fa="درباره حافظه جمعی",
             authors="Halbwachs, M.", year=1992, publisher="University of Chicago Press",
             doi=None, url="https://press.uchicago.edu/ucp/books/book/chicago/O/bo3619875.html",
             language="en", isbn=None,
             citation="Halbwachs, M. (1992). On collective memory (L. A. Coser, Ed. & Trans.). University of Chicago Press.",
             locator="work", locator_type="work",
             supports="social frameworks of memory and selective reconstruction of the past", verified=True),
        dict(kind="BOOK",
             title_en="Media Events: The Live Broadcasting of History",
             title_fa="رویدادهای رسانه‌ای: پخش زنده تاریخ",
             authors="Dayan, D.; Katz, E.", year=1992, publisher="Harvard University Press",
             doi=None, url=None, language="en", isbn=None,
             citation="Dayan, D., & Katz, E. (1992). Media events: The live broadcasting of history. Harvard University Press.",
             locator="work", locator_type="work",
             supports="media events as sites of collective memory", verified=False),
    ],
    "MC-668": [
        dict(kind="BOOK",
             title_en="Algorithms of Oppression: How Search Engines Reinforce Racism",
             title_fa="الگوریتم‌های ستم: چگونه موتورهای جست‌وجو نژادپرستی را بازتولید می‌کنند",
             authors="Noble, S. U.", year=2018, publisher="New York University Press",
             doi="10.2307/j.ctt1pwt9w5",
             url="https://nyupress.org/9781479837243/algorithms-of-oppression/",
             language="en", isbn="978-1-4798-3724-3",
             citation="Noble, S. U. (2018). Algorithms of oppression: How search engines reinforce racism. New York University Press.",
             locator="work", locator_type="work",
             supports="algorithmic bias in search and classification systems", verified=True),
        dict(kind="BOOK",
             title_en="Weapons of Math Destruction: How Big Data Increases Inequality and Threatens Democracy",
             title_fa="سلاح‌های ویرانی ریاضی: چگونه داده‌های کلان نابرابری را افزایش و دموکراسی را تهدید می‌کند",
             authors="O'Neil, C.", year=2016, publisher="Crown",
             doi=None, url=None, language="en", isbn=None,
             citation="O'Neil, C. (2016). Weapons of math destruction: How big data increases inequality and threatens democracy. Crown.",
             locator="work", locator_type="work",
             supports="opaque automated models producing harmful outcomes", verified=False),
    ],
}

ENRICH = {
    "MC-693": {
        "summary": "(والرشتاین، ۱۹۷۴) نظریه نظام‌های جهانی، تحلیل تاریخی را از واحد ملی به سامانه جهانی تغییر می‌دهد. والرشتاین نشان داد اقتصاد سرمایه‌داری جهانی از سده شانزدهم با تقسیم کار بین‌المللی شکل گرفت و کشورها را در سه جایگاه هسته، نیمه‌پیرامون و پیرامون سازمان داد. هسته، تولید صنعتی و مالی پیشرفته را در دست دارد و پیرامون، مواد خام و کار ارزان را تأمین می‌کند. نظام بین‌دولتی و چرخه‌های سلطه، این سلسله‌مراتب را بازتولید می‌کنند. والرشتاین این ساختار را نه مرحله‌ای موقت، بلکه منطق بنیادین نظام جهانی دید. در مطالعات رسانه، این چارچوب جریان نامتوازن اطلاعات و امپریالیسم رسانه‌ای را توضیح می‌دهد. همچنین این چارچوب توضیح می‌دهد چرا سیاست‌های ارتباطی و کمک‌رسانی رسانه‌ای اغلب بازتولیدکننده وابستگی‌اند: کمک، جریان یک‌سویه اطلاعات و فناوری را تقویت می‌کند و صدای پیرامون را در سطح جهانی کم‌شنیده می‌گذارد. از این رو، رسانه بومی و مالکیت عمومی می‌تواند راهبرد مقاومت باشد، هرچند بدون تغییر ساختار اقتصادی، اثری محدود دارد و می‌تواند به نمایش تنوع بسنده کند، در حالی که تغییر واقعی به بازتوزیع منابع و توان تولید نیاز دارد.",
        "definition": "نظام جهانی، سامانه‌ای تاریخی و اقتصادی است که با تقسیم کار میان هسته، نیمه‌پیرامون و پیرامون، روابط نابرابر کشورها را در قالب یک اقتصاد جهانی سرمایه‌داری سازمان می‌دهد.",
        "main_problem": "مسئله این است که چرا نابرابری جهانی پایدار می‌ماند و توسعه یک کشور را نمی‌توان جدا از جایگاه آن در سامانه فهمید. پاسخ، منطق نظام جهانی است. پرسش دوم، فرهنگ است: چگونه جریان اطلاعات و معنا نیز همین سلسله‌مراتب را بازتولید می‌کند.",
        "mechanism": "۱. اقتصاد جهانی: بازار و تقسیم کار فراملی.\n۲. هسته: سرمایه، فناوری و تولید پیشرفته.\n۳. پیرامون: مواد خام و کار کم‌مزد.\n۴. نیمه‌پیرامون: جایگاه میانی و رقابت‌پذیر.\n۵. نظام بین‌دولتی: چارچوب سیاسی حفظ سامانه.\n۶. چرخه سلطه: جابه‌جایی قدرت میان هسته‌ها.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا خبر جهانی از پایتخت‌های هسته تولید می‌شود، چرا کشورهای پیرامونی مصرف‌کننده محتوای هسته‌اند و چرا مالکیت پلتفرم، شکل تازه‌ای از مرکزیت می‌سازد. نکته مهم این است که چارچوب اقتصادی را تعیین‌کننده مطلق نمی‌بیند؛ فرهنگ و مقاومت نیز در بازتولید یا تغییر جایگاه نقش دارند.",
        "assumptions": [
            "واحد تحلیل، نظام جهانی است.",
            "تقسیم کار، جایگاه کشورها را تعیین می‌کند.",
            "سلسله‌مراتب هسته و پیرامون پایدار است.",
        ],
        "principles": [
            "توسعه درون سامانه فهم می‌شود.",
            "جریان اطلاعات از سلسله‌مراتب تبعیت می‌کند.",
            "سلطه چرخه‌ای است، نه ابدی.",
        ],
        "critiques": [
            "۱. جبر اقتصادی: فرهنگ و عاملیت کم دیده می‌شود.\n۲. تعمیم: تفاوت کشورهای پیرامونی نادیده می‌ماند.\n۳. هدف: پیش‌بینی فرجام نظام قطعی نیست.\n۴. سنجش: جایگاه‌ها سخت عملیاتی می‌شوند.\n۵. رسانه: پیوند اقتصادی و فرهنگی نیازمند میانجی است.",
        ],
        "applications": [
            "رسانه جهانی: تحلیل جریان نامتوازن خبر.",
            "امپریالیسم رسانه‌ای: مطالعه وابستگی محتوایی.",
            "سیاست ارتباطی: حمایت از تولید بومی.",
            "اقتصاد سیاسی پلتفرم: تحلیل مرکزیت داده.",
        ],
        "evolution": "والرشتاین در ۱۹۷۴ جلد نخست را منتشر کرد و چارچوب را در جلدهای بعدی تا سده بیستم گسترد. پژوهش امپریالیسم رسانه‌ای و اقتصاد سیاسی ارتباطات، آن را در حوزه فرهنگ به کار گرفت.",
        "key_concepts": [
            "نظام جهانی (World-System)",
            "اقتصاد جهانی (World-Economy)",
            "هسته (Core)",
            "پیرامون (Periphery)",
            "نیمه‌پیرامون (Semi-Periphery)",
            "چرخه سلطه (Hegemonic Cycle)",
        ],
        "studies": [
            "Wallerstein, I. (1974). The modern world-system I. Academic Press.",
            "Wallerstein, I. (1974). The rise and future demise of the world capitalist system. Comparative Studies in Society and History, 16(4), 387-415.",
        ],
        "theorists": "ایمانوئل والرشتاین",
        "theorists_text": "والرشتاین (۱۹۷۴)",
        "year": 1974,
        "model": "تقسیم کار جهانی → جایگاه هسته/نیمه‌پیرامون/پیرامون → نظام بین‌دولتی → بازتولید نابرابری → جریان نامتوازن اطلاعات.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nوالرشتاین تاریخ را در مقیاس سامانه دید و نظریه نوسازی را نقد کرد. نوآوری چارچوب، جایگزینی واحد ملی با نظام جهانی است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با تحلیل تاریخی، داده تجارت و مطالعه نهادها انجام می‌شود. پژوهشی که تنها شاخص ملی را می‌سنجد، جایگاه سامانه‌ای را از دست می‌دهد؛ و پژوهشی که اقتصاد را تنها تعیین‌کننده می‌داند، فرهنگ و مقاومت را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در تحلیل جریان خبر و مالکیت پلتفرم است، اما باید با مطالعه مصرف بومی تکمیل شود. مرکزیت بی توجه به عاملیت، به جبر بدل می‌شود.",
        "critique_text": "\n".join([
            "۱. جبر اقتصادی: فرهنگ کم دیده می‌شود.",
            "۲. تعمیم: تفاوت پیرامون نادیده می‌ماند.",
            "۳. هدف: فرجام نظام قطعی نیست.",
            "۴. سنجش: جایگاه سخت عملیاتی می‌شود.",
            "۵. رسانه: پیوند اقتصادی و فرهنگی نیازمند میانجی است.",
        ]),
        "example_text": "خبر بحران در کشوری پیرامونی اغلب از خبرگزاری‌های هسته بازنشر می‌شود؛ چارچوب روایت، پیش از رسیدن به مخاطب بومی، در مرکز سامانه تعیین شده است.",
    },
    "MC-685": {
        "summary": "(پیرس و کرونن، ۱۹۸۰) نظریه مدیریت هماهنگ‌شده معنا می‌گوید انسان‌ها در گفت‌وگو، معنای کنش یکدیگر را هماهنگ می‌کنند. معنا در سلسله‌مراتبی سازمان می‌یابد: محتوا، کنش گفتاری، قرارداد، قطعه، رابطه، نقش زندگی و الگوی فرهنگی. هر سطح، معنای سطح پایین‌تر را قاب می‌بندد و خود از سطح بالاتر اثر می‌گیرد. پیرس و کرونن بر بازتابندگی تأکید کردند: ما در گفتن، واقعیت اجتماعی می‌سازیم و همان واقعیت، گفتن بعدی را محدود می‌کند. هماهنگی و انسجام دو معیار ارزیابی‌اند و همیشه هم‌راستا نیستند. نظریه در خانواده‌درمانی، تحلیل سازمان و نقد گفت‌وگوی رسانه‌ای به کار رفته است. پژوهش بعدی نشان داد رسانه با گزینش سطح قاب، هماهنگی یا شکست معنا را ممکن می‌کند: تیتر و تصویر می‌توانند یک کنش گفتاری را از سطح شوخی به سطح تهدید منتقل کنند. از این چشم، تحلیل رسانه تنها رمزگشایی متن نیست، بلکه مطالعه چگونگی هماهنگ‌سازی معنا میان تولیدکننده، متن و مخاطب است و همین هماهنگی، زمینه اعتماد یا بی‌اعتمادی عمومی را می‌سازد و به کنش جمعی جهت می‌دهد؛ از این رو، سوءتفاهم رسانه‌ای را باید در سطح رابطه و فرهنگ جست، نه تنها در واژه‌ها.",
        "definition": "مدیریت هماهنگ‌شده معنا، نظریه‌ای ارتباطی است که معنای کنش را برساخته تعامل می‌داند و آن را در سلسله‌مراتبی از سطح محتوا تا الگوی فرهنگی، هماهنگ و بازتولید می‌کند.",
        "main_problem": "مسئله این است که چگونه افراد با معناهای متفاوت به کنش مشترک می‌رسند. پاسخ، هماهنگی در سلسله‌مراتب معناست. پرسش دوم، شکست است: چرا گفت‌وگو به سوءتفاهم یا تعارض می‌انجامد.",
        "mechanism": "۱. سلسله‌مراتب: محتوا، کنش گفتاری، قرارداد، قطعه، رابطه، نقش زندگی و فرهنگ.\n۲. قاب‌بندی: سطح بالاتر، معنای سطح پایین‌تر را تعیین می‌کند.\n۳. بازتابندگی: کنش، واقعیت اجتماعی می‌سازد و از آن اثر می‌گیرد.\n۴. نیروی منطقی: احساس اجبار به ادامه الگوی گفتار.\n۵. هماهنگی: تطابق کنش‌ها، نه لزوماً توافق معنا.\n۶. انسجام: سازگاری روایت با باورها و ارزش‌ها.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا یک جمله در مصاحبه، بسته به سطح رابطه و فرهنگ، توهین یا شوخی خوانده می‌شود، چرا بحران سازمانی از شکست هماهنگی معنا آغاز می‌شود و چرا دیپلماسی رسانه‌ای به هماهنگی سطح فرهنگی نیاز دارد. نکته مهم این است که هماهنگی، لزوماً درستی یا اخلاقی بودن معنا را تضمین نمی‌کند.",
        "assumptions": [
            "معنا در تعامل ساخته می‌شود.",
            "معنا در سلسله‌مراتب سطح‌ها سازمان می‌یابد.",
            "گفتار، واقعیت اجتماعی می‌سازد.",
        ],
        "principles": [
            "سطح بالاتر، معنای پایین‌تر را قاب می‌بندد.",
            "هماهنگی با توافق یکسان نیست.",
            "بازتابندگی، الگو را تثبیت یا تغییر می‌دهد.",
        ],
        "critiques": [
            "۱. پیچیدگی: مدل برای کار تجربی سنگین است.\n۲. هنجار: معیار هماهنگی خوب روشن نیست.\n۳. قدرت: نابرابری ساختاری کم‌تر تحلیل می‌شود.\n۴. سنجش: سطوح معنا سخت عملیاتی می‌شوند.\n۵. فرهنگ: کاربرد بین‌فرهنگی نیازمند بومی‌سازی است.",
        ],
        "applications": [
            "خانواده‌درمانی: بازچینش سلسله‌مراتب معنا.",
            "ارتباطات سازمانی: تشخیص شکست هماهنگی.",
            "تحلیل گفت‌وگوی رسانه‌ای: قاب‌بندی کنش گفتاری.",
            "دیپلماسی رسانه‌ای: هماهنگی سطح فرهنگی.",
        ],
        "evolution": "پیرس و کرونن در ۱۹۸۰ چارچوب را عرضه کردند و پیرس در ۲۰۰۷ آن را با نگاه گفت‌وگومندانه گسترد. پژوهش خانواده‌درمانی و ارتباطات سازمانی، مدل را آزمود.",
        "key_concepts": [
            "هماهنگی معنا (Coordination of Meaning)",
            "سلسله‌مراتب معنا (Hierarchy of Meaning)",
            "بازتابندگی (Reflexivity)",
            "نیروی منطقی (Logical Force)",
            "قطعه (Episode)",
            "نقش زندگی (Life Script)",
        ],
        "studies": [
            "Pearce, W. B., & Cronen, V. E. (1980). Communication, action, and meaning. Praeger.",
            "Pearce, W. B. (2007). Making social worlds: A communication perspective. Blackwell.",
        ],
        "theorists": "دبلیو. بارنت پیرس؛ ورنون کرونن",
        "theorists_text": "پیرس و کرونن (۱۹۸۰)",
        "year": 1980,
        "model": "کنش گفتاری → قاب‌بندی در سطوح معنا → هماهنگی یا شکست → بازتولید یا تغییر واقعیت اجتماعی.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nپیرس و کرونن ارتباط را سازنده واقعیت اجتماعی دیدند و مدل را جایگزین انتقال خطی کردند. نوآوری چارچوب، سلسله‌مراتب سطح معنا است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با تحلیل گفت‌وگو، مصاحبه و مشاهده درمان انجام می‌شود. پژوهشی که تنها محتوا را می‌سنجد، سطوح بالاتر را از دست می‌دهد؛ و پژوهشی که هماهنگی را توافق می‌خواند، تفاوت را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در تحلیل سوءتفاهم رسانه‌ای است، اما باید با مطالعه قدرت تکمیل شود. هماهنگی بی اخلاق، به همدستی بدل می‌شود.",
        "critique_text": "\n".join([
            "۱. پیچیدگی: مدل برای آزمون سنگین است.",
            "۲. هنجار: معیار هماهنگی خوب روشن نیست.",
            "۳. قدرت: نابرابری کم‌تر تحلیل می‌شود.",
            "۴. سنجش: سطوح معنا سخت عملیاتی می‌شوند.",
            "۵. فرهنگ: بومی‌سازی لازم است.",
        ]),
        "example_text": "مدیری که در جلسه می‌گوید «این فقط یک پیشنهاد است»، در سطح رابطه آن را دستور می‌خواند؛ هماهنگی معنا تنها با شناخت سطح رابطه و فرهنگ سازمان ممکن است.",
    },
    "MC-677": {
        "summary": "(هالبواخس، ۱۹۹۲) نظریه حافظه جمعی و رسانه می‌گوید یادآوری، کنشی صرفاً فردی نیست و در چارچوب‌های اجتماعی شکل می‌گیرد. هالبواخس استدلال کرد حافظه همیشه گزینشی و بازسازی‌شده است و گروه‌ها گذشته را از منظر نیازهای حال روایت می‌کنند. رسانه، عامل کلیدی این چارچوب‌بندی است: آرشیو، سالگرد، مستند و خبر، گذشته مشترک را می‌سازند و بازسازی می‌کنند. رسانه هم‌زمان چیزی را به یاد می‌آورد و چیزی را فراموش می‌کند. حافظه جمعی، هویت ملی و مشروعیت سیاسی را تقویت یا تضعیف می‌کند. در محیط دیجیتال، حافظه به شکلی شبکه‌ای و پیوسته بازتولید می‌شود. نظریه، گذشته را میدان کشمکش معنا می‌داند. همچنین رسانه می‌تواند با ایجاد رویداد مشترک، حافظه‌ای تازه بسازد: پخش زنده یک مراسم ملی، میلیون‌ها بیننده را در یک لحظه تاریخی سهیم می‌کند و خاطره جمعی مشترکی می‌آفریند؛ این خاطره بعدها در روایت‌های رسانه‌ای بازخوانی و بازتعریف می‌شود و گروه‌های مختلف می‌کوشند معنای آن را به نفع روایت خود تغییر دهند.",
        "definition": "حافظه جمعی، بازنمایی مشترک و گزینشی گذشته در یک گروه است که در چارچوب‌های اجتماعی ساخته می‌شود و رسانه، از طریق آرشیو، روایت و آیین یادآوری، آن را بازتولید یا دگرگون می‌کند.",
        "main_problem": "مسئله این است که چرا گروه‌ها گذشته را یکسان به یاد نمی‌آورند و چرا یادآوری با فراموشی همراه است. پاسخ، چارچوب اجتماعی و گزینش است. پرسش دوم، قدرت است: چه کسی حق روایت گذشته را دارد.",
        "mechanism": "۱. چارچوب اجتماعی: گروه، شرایط یادآوری را می‌سازد.\n۲. گزینش: گذشته بازسازی می‌شود، نه بازتولید.\n۳. آیین یادآوری: سالگرد و مراسم، حافظه را زنده می‌کند.\n۴. آرشیو رسانه‌ای: ذخیره و دسترسی، مرز یادآوری را تعیین می‌کند.\n۵. فراموشی: حذف و سکوت، بخشی از حافظه است.\n۶. هویت: روایت گذشته، مرز ما و آن‌ها را می‌سازد.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا پوشش سالگرد یک رویداد، هویت جمعی را تقویت می‌کند، چرا مستند تاریخی می‌تواند روایت رسمی را به چالش بکشد و چرا آرشیو دیجیتال، حافظه را هم گسترده‌تر و هم آسیب‌پذیرتر می‌کند. نکته مهم این است که حافظه جمعی، حافظه دقیق نیست؛ روایتی معنادار برای حال است.",
        "assumptions": [
            "یادآوری در چارچوب اجتماعی رخ می‌دهد.",
            "حافظه گزینشی و بازسازی‌شده است.",
            "رسانه عامل ساخت حافظه است.",
        ],
        "principles": [
            "گذشته از منظر حال روایت می‌شود.",
            "فراموشی بخشی از حافظه است.",
            "روایت گذشته، هویت می‌سازد.",
        ],
        "critiques": [
            "۱. دقت: حافظه جمعی با تاریخ انتقادی همسان نیست.\n۲. قدرت: روایت رسمی می‌تواند حافظه‌های دیگر را حذف کند.\n۳. سنجش: حافظه جمعی سخت اندازه‌گیری می‌شود.\n۴. رسانه: نقش مخاطب در بازتفسیر کم دیده می‌شود.\n۵. دیجیتال: پیوند آرشیو و فراموشی نیازمند مطالعه است.",
        ],
        "applications": [
            "روزنامه‌نگاری تاریخی: تحلیل قاب سالگرد.",
            "مستند: بازخوانی انتقادی روایت رسمی.",
            "سیاست حافظه: تنوع روایت‌های گذشته.",
            "آرشیو رسانه‌ای: حفظ و دسترسی به حافظه.",
        ],
        "evolution": "هالبواخس در نیمه نخست سده بیستم چارچوب اجتماعی حافظه را صورتبندی کرد و ترجمه کوزر در ۱۹۹۲ آن را به انگلیسی گسترد. پژوهش رسانه، حافظه دیجیتال و سیاست یادآوری، چارچوب را بسط داد.",
        "key_concepts": [
            "حافظه جمعی (Collective Memory)",
            "چارچوب اجتماعی (Social Framework)",
            "بازسازی گذشته (Reconstruction of the Past)",
            "آیین یادآوری (Commemoration)",
            "حافظه و فراموشی (Memory and Forgetting)",
            "هویت جمعی (Collective Identity)",
        ],
        "studies": [
            "Halbwachs, M. (1992). On collective memory. University of Chicago Press.",
            "Dayan, D., & Katz, E. (1992). Media events: The live broadcasting of history. Harvard University Press.",
        ],
        "theorists": "موریس هالبواخس",
        "theorists_text": "هالبواخس (۱۹۲۵/۱۹۹۲)",
        "year": 1992,
        "model": "چارچوب اجتماعی → گزینش و بازسازی گذشته → آیین و آرشیو رسانه‌ای → هویت جمعی → بازتفسیر حال.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nهالبواخس حافظه را اجتماعی دید و آن را از روان‌شناسی فردی جدا کرد. نوآوری چارچوب، پیوند یادآوری با گروه و حال است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با تحلیل روایت، مصاحبه و مطالعه آیین انجام می‌شود. پژوهشی که تنها متن رسانه را می‌خواند، حافظه مخاطب را از دست می‌دهد؛ و پژوهشی که روایت رسمی را حافظه جمعی می‌خواند، کشمکش معنا را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در تحلیل سالگرد و آرشیو است، اما باید با مطالعه قدرت تکمیل شود. حافظه بی تنوع، به حذف بدل می‌شود.",
        "critique_text": "\n".join([
            "۱. دقت: حافظه با تاریخ انتقادی همسان نیست.",
            "۲. قدرت: روایت رسمی حافظه‌های دیگر را حذف می‌کند.",
            "۳. سنجش: حافظه سخت اندازه‌پذیر است.",
            "۴. رسانه: نقش مخاطب کم دیده می‌شود.",
            "۵. دیجیتال: آرشیو و فراموشی نیازمند مطالعه است.",
        ]),
        "example_text": "مستندی که یک رویداد تاریخی را تنها از دید قربانیان روایت می‌کند، می‌تواند حافظه جمعی را بازچینش کند و روایت رسمی را به پرسش بکشد.",
    },
    "MC-668": {
        "summary": "(نوبل، ۲۰۱۸) نظریه خودکارسازی تصمیم و تبعیض الگوریتمی نشان می‌دهد سپردن انتخاب به رایانه، سوگیری را حذف نمی‌کند بلکه آن را پنهان می‌سازد. سامانه‌های توصیه، میانجی‌گری محتوا و هدف‌گیری تبلیغ، بر داده آموزش می‌بینند و الگوهای تبعیض موجود را بازتولید می‌کنند. نوبل نشان داد جست‌وجوی تصویری می‌تواند کلیشه نژادی و جنسیتی را تقویت کند. اونیل خطر مدل‌های کدر را در نابرابری ساختاری برجسته کرد. کدری، مقیاس و حلقه بازخورد، سه سازوکار تشدیدند. تصمیم خودکار، مسئولیت را نیز پراکنده می‌کند. در رسانه، این چارچوب تبعیض توصیه، حذف محتوا و هدف‌گیری را تحلیل می‌کند. همچنین خودکارسازی تصمیم پرسش دموکراتیک تازه‌ای می‌سازد: وقتی سامانه تعیین می‌کند چه خبری دیده شود یا کدام حساب محدود شود، قدرت عمومی بدون پاسخ‌گویی عمومی اعمال می‌شود. از این رو، حسابرسی مستقل، حق اعتراض و امکان بازبینی انسانی نه افزوده‌ای فنی بلکه شرط مشروعیت سامانه‌های رسانه‌ای خودکارند؛ و بی آن‌ها، بی‌طرفی ادعایی الگوریتم به پوششی برای سوگیری بدل می‌شود و اعتماد مخاطب را در بلندمدت فرسوده می‌کند، حتی اگر هر تصمیم منفرد کوچک به نظر برسد. این همان خطای مقیاس است که اونیل هشدار داد: آسیبی که در یک تصمیم ناچیز به نظر می‌رسد، در تکرار میلیونی به نابرابری ساختاری بدل می‌شود.",
        "definition": "تبعیض الگوریتمی، بروز نابرابری سیستماتیک در خروجی سامانه خودکار است که از داده آموزش، معیار بهینه‌سازی و طراحی کدر برمی‌خیزد و در مقیاس گسترده بازتولید می‌شود.",
        "main_problem": "مسئله این است که چرا سامانه ظاهراً بی‌طرف، نتایج نابرابر تولید می‌کند. پاسخ، سوگیری داده و طراحی است. پرسش دوم، مسئولیت است: چه کسی پاسخگوی تصمیم خودکار است.",
        "mechanism": "۱. داده آموزش: الگوهای تاریخی تبعیض را در خود دارد.\n۲. معیار بهینه‌سازی: هدف سود یا تعامل، نابرابری را تقویت می‌کند.\n۳. کدری: کاربر منطق تصمیم را نمی‌بیند.\n۴. مقیاس: خطای کوچک در میلیون‌ها تصمیم تکرار می‌شود.\n۵. حلقه بازخورد: خروجی سوگیرانه، داده بعدی را سوگیرانه می‌کند.\n۶. پراکندگی مسئولیت: هیچ‌کس خود را پاسخگو نمی‌داند.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا توصیه محتوا گروه‌هایی را کمتر می‌بیند، چرا حذف خودکار محتوا به سانسور نابرابر می‌انجامد و چرا تبلیغ هدفمند می‌تواند تبعیض مسکن و اشتغال بسازد. نکته مهم این است که شفافیت به‌تنها کافی نیست؛ حسابرسی و اصلاح داده نیز لازم است.",
        "assumptions": [
            "الگوریتم از داده سوگیرانه می‌آموزد.",
            "خودکارسازی، سوگیری را حذف نمی‌کند.",
            "تصمیم خودکار در مقیاس اثر می‌گذارد.",
        ],
        "principles": [
            "کدری، پاسخ‌گویی را تضعیف می‌کند.",
            "حلقه بازخورد، سوگیری را تشدید می‌کند.",
            "حسابرسی، شرط عدالت الگوریتمی است.",
        ],
        "critiques": [
            "۱. سنجش: سوگیری سخت اثبات و اندازه‌گیری می‌شود.\n۲. زمینه: معنای تبعیض فرهنگی است.\n۳. نیت: تمرکز بر اثر، نیت طراح را کنار می‌گذارد.\n۴. داده: دسترسی به داده شرکت‌ها محدود است.\n۵. راه‌حل: شفافیت به‌تنهایی کافی نیست.",
        ],
        "applications": [
            "حسابرسی الگوریتم: سنجش اثر گروهی توصیه.",
            "سیاست محتوا: عدالت در حذف خودکار.",
            "رسانه و تبلیغ: پرهیز از هدف‌گیری تبعیض‌آمیز.",
            "سواد الگوریتمی: شناخت کدری تصمیم.",
        ],
        "evolution": "پژوهش تبعیض الگوریتمی در دهه ۲۰۱۰ با کار نوبل و اونیل گسترش یافت. بعدها چارچوب حسابرسی، مستندسازی مدل و مقررات داده، آن را نهادینه کرد.",
        "key_concepts": [
            "تبعیض الگوریتمی (Algorithmic Bias)",
            "اثر تفاوت‌گذار (Disparate Impact)",
            "کدری (Opacity)",
            "حلقه بازخورد (Feedback Loop)",
            "حسابرسی الگوریتم (Algorithm Audit)",
            "مسئولیت‌پذیری (Accountability)",
        ],
        "studies": [
            "Noble, S. U. (2018). Algorithms of oppression. New York University Press.",
            "O'Neil, C. (2016). Weapons of math destruction. Crown.",
        ],
        "theorists": "صفیه نوبل؛ کتی اونیل",
        "theorists_text": "نوبل (۲۰۱۸)؛ اونیل (۲۰۱۶)",
        "year": 2019,
        "model": "داده سوگیرانه → آموزش مدل → خروجی کدر در مقیاس → حلقه بازخورد → نابرابری ساختاری.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nنوبل جست‌وجو را نهاد قدرت دید و اونیل اثر مدل کدر را بر نابرابری نشان داد. نوآوری چارچوب، پیوند فنی و عدالت اجتماعی است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با حسابرسی خروجی، آزمون سناریو و تحلیل داده انجام می‌شود. پژوهشی که تنها دقت مدل را می‌سنجد، اثر گروهی را از دست می‌دهد؛ و پژوهشی که نیت طراح را مسلم بی‌طرف می‌داند، پیامد ساختاری را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در تحلیل توصیه و حذف است، اما باید با مطالعه زمینه تکمیل شود. شفافیت بی حسابرسی، به تشریفات بدل می‌شود.",
        "critique_text": "\n".join([
            "۱. سنجش: سوگیری سخت اندازه‌پذیر است.",
            "۲. زمینه: معنای تبعیض فرهنگی است.",
            "۳. نیت: تمرکز بر اثر، نیت را کنار می‌گذارد.",
            "۴. داده: دسترسی محدود است.",
            "۵. راه‌حل: شفافیت کافی نیست.",
        ]),
        "example_text": "سامانه توصیه‌ای که بر داده تعامل گذشته آموزش دیده، گروهی را که کمتر کلیک کرده کمتر نشان می‌دهد؛ این حلقه، حضور گروه را در توصیه‌های بعدی باز هم کم‌تر می‌کند.",
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
    "MC-693": ("نظریه نظام‌های جهانی", "World-Systems Theory",
               "label repaired: mistranslated 'سامانه-جهان/System-World' -> world-systems theory (Wallerstein 1974)"),
    "MC-685": ("مدیریت هماهنگ‌شده معنا", "Coordinated Management of Meaning (CMM)",
               "label repaired: 'Meaning Harmony Management' -> coordinated management of meaning (Pearce & Cronen 1980)"),
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
                                       "verified": n_verified, "batch": 112}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH112 THEORY DONE")


if __name__ == "__main__":
    main()
