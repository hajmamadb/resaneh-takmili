# -*- coding: utf-8 -*-
"""Batch 109: full documentation for MC-690, MC-691, MC-682, MC-710."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch109-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch109_theory.json"

S = {
    "MC-690": [
        dict(kind="BOOK",
             title_en="Culture's Consequences: International Differences in Work-Related Values",
             title_fa="پیامدهای فرهنگ: تفاوت‌های بین‌المللی در ارزش‌های مرتبط با کار",
             authors="Hofstede, G.", year=1980, publisher="Sage",
             doi=None, url="https://geerthofstede.com/cultures-consequences-40-years-on/",
             language="en", isbn=None,
             citation="Hofstede, G. (1980). Culture's consequences: International differences in work-related values. Sage.",
             locator="work", locator_type="work",
             supports="four national cultural dimensions derived from IBM survey data", verified=True),
        dict(kind="BOOK",
             title_en="Culture's Consequences: Comparing Values, Behaviors, Institutions, and Organizations Across Nations",
             title_fa="پیامدهای فرهنگ: مقایسه ارزش‌ها، رفتارها، نهادها و سازمان‌ها در ملت‌ها",
             authors="Hofstede, G.", year=2001, publisher="Sage",
             doi=None, url="https://digitalcommons.usu.edu/unf_research/53/",
             language="en", isbn=None,
             citation="Hofstede, G. (2001). Culture's consequences: Comparing values, behaviors, institutions, and organizations across nations (2nd ed.). Sage.",
             locator="work", locator_type="work",
             supports="expanded five-dimension model and methodological reflection", verified=False),
    ],
    "MC-691": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Universals in the Content and Structure of Values: Theoretical Advances and Empirical Tests in 20 Countries",
             title_fa="جهان‌شمولی محتوا و ساختار ارزش‌ها: پیشرفت نظری و آزمون تجربی در بیست کشور",
             authors="Schwartz, S. H.", year=1992,
             publisher="Advances in Experimental Social Psychology",
             doi="10.1016/S0065-2601(08)60281-6",
             url="https://www.sciencedirect.com/science/chapter/bookseries/pii/S0065260108602816",
             language="en", isbn=None,
             citation="Schwartz, S. H. (1992). Universals in the content and structure of values: Theoretical advances and empirical tests in 20 countries. Advances in Experimental Social Psychology, 25, 1-65.",
             locator="25:1-65", locator_type="page_range",
             supports="ten basic values in a circular motivational continuum", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="An Overview of the Schwartz Theory of Basic Values",
             title_fa="مروری بر نظریه ارزش‌های بنیادی شوارتز",
             authors="Schwartz, S. H.", year=2012,
             publisher="Online Readings in Psychology and Culture",
             doi=None, url="https://scholarworks.gvsu.edu/cgi/viewcontent.cgi?article=1116&context=orpc",
             language="en", isbn=None,
             citation="Schwartz, S. H. (2012). An overview of the Schwartz theory of basic values. Online Readings in Psychology and Culture, 2(1).",
             locator="2(1)", locator_type="work",
             supports="refined 19-value model and culture-level orientations", verified=False),
    ],
    "MC-682": [
        dict(kind="BOOK",
             title_en="Politeness: Some Universals in Language Usage",
             title_fa="ادب: برخی جهان‌شمولی‌ها در کاربرد زبان",
             authors="Brown, P.; Levinson, S. C.", year=1987,
             publisher="Cambridge University Press",
             doi=None, url="https://www.cambridge.org/highereducation/books/politeness/89113EE2FB4A1D254D4A8D2011E542E4",
             language="en", isbn="978-0-521-31355-1",
             citation="Brown, P., & Levinson, S. C. (1987). Politeness: Some universals in language usage. Cambridge University Press.",
             locator="work", locator_type="work",
             supports="face, face-threatening acts and five politeness strategies", verified=True),
        dict(kind="BOOK",
             title_en="Interaction Ritual: Essays on Face-to-Face Behavior",
             title_fa="آیین تعامل: مقالاتی درباره رفتار رو در رو",
             authors="Goffman, E.", year=1967, publisher="Pantheon Books",
             doi=None, url=None, language="en", isbn=None,
             citation="Goffman, E. (1967). Interaction ritual: Essays on face-to-face behavior. Pantheon Books.",
             locator="work", locator_type="work",
             supports="face-work as the interactional basis of politeness", verified=False),
    ],
    "MC-710": [
        dict(kind="BOOK",
             title_en="A Theory of Cognitive Dissonance",
             title_fa="نظریه ناهماهنگی شناختی",
             authors="Festinger, L.", year=1957, publisher="Row, Peterson",
             doi=None, url=None, language="en", isbn=None,
             citation="Festinger, L. (1957). A theory of cognitive dissonance. Row, Peterson.",
             locator="work", locator_type="work",
             supports="preference for consonant information as dissonance reduction", verified=True),
        dict(kind="BOOK",
             title_en="The Effects of Mass Communication",
             title_fa="اثرات ارتباطات جمعی",
             authors="Klapper, J. T.", year=1960, publisher="Free Press",
             doi=None, url=None, language="en", isbn=None,
             citation="Klapper, J. T. (1960). The effects of mass communication. Free Press.",
             locator="work", locator_type="work",
             supports="selective exposure, perception and retention in mass communication", verified=False),
    ],
}

ENRICH = {
    "MC-690": {
        "summary": "(هوفستد، ۱۹۸۰) نظریه ابعاد فرهنگی هوفستد، فرهنگ‌های ملی را با چند بُعد قابل سنجش مقایسه می‌کند. هوفستد با تحلیل پرسش‌نامه‌های کارکنان شرکت آی‌بی‌ام در بیش از پنجاه کشور، چهار بُعد نخست را استخراج کرد: فاصله قدرت، فردگرایی در برابر جمع‌گرایی، مردانگی در برابر زنانگی و اجتناب از ابهام. بعدها بُعد جهت‌گیری بلندمدت به یاری پژوهش باوند و بُعد لذت‌گرایی در برابر خویشتن‌داری افزوده شد. هر بُعد، الگویی از ارزش‌های مشترک است که رفتار نهادی و ارتباطی را جهت می‌دهد. این ابعاد نمره فرد نیستند، بلکه میانگین گرایش یک جامعه‌اند. همچنین این چارچوب نشان می‌دهد چرا رسانه‌های خبری در فرهنگ‌های با ابهام‌گریزی بالا روایت قطعی و کارشناسی را ترجیح می‌دهند، در حالی که فرهنگ‌های با تحمل ابهام بیشتر، تحلیل چندپهلو و طنزآمیز را می‌پذیرند. با این حال، بنگاه رسانه‌ای باید از تعمیم نمره ملی به سلیقه فردی بپرهیزد، زیرا ابعاد ابزار مقایسه میانگین‌هاست و نه پیش‌بینی رفتار هر مخاطب. در ارتباطات، بازاریابی و مدیریت رسانه، ابعاد به توضیح تفاوت مخاطب، سبک مذاکره و انتظار از اقتدار کمک می‌کند.",
        "definition": "ابعاد فرهنگی، مجموعه‌ای از محورهای ارزشی قابل سنجش است که تفاوت جوامع ملی را در نگرش به قدرت، فرد و گروه، نقش‌های جنسیتی، ابهام، زمان و لذت توضیح می‌دهد.",
        "main_problem": "مسئله این است که چگونه می‌توان تفاوت‌های فرهنگی را بدون فروکاستن به کلیشه، به شکلی مقایسه‌پذیر سنجید. پاسخ، ابعاد پیوسته و نمره‌پذیر است. پرسش دوم، اعتبار است: آیا نمونه سازمانی و روش پرسش‌نامه‌ای، فرهنگ ملی را بازنمایی می‌کند.",
        "mechanism": "۱. فاصله قدرت: پذیرش توزیع نابرابر قدرت در نهادها.\n۲. فردگرایی و جمع‌گرایی: اولویت من یا گروه.\n۳. مردانگی و زنانگی: اولویت رقابت و دستاورد یا مراقبت و کیفیت زندگی.\n۴. اجتناب از ابهام: تحمل یا گریز از موقعیت نامعین.\n۵. جهت‌گیری بلندمدت: اولویت آینده و صرفه‌جویی یا حال و سنت.\n۶. خویشتن‌داری: مهار یا آزادگذاری لذت.\n\nدر بستر رسانه، این ابعاد توضیح می‌دهند چرا خبر در فرهنگ‌های کم‌فاصله‌قدرت، پرسش‌گرانه‌تر است، چرا تبلیغ در فرهنگ جمع‌گرا بر خانواده تأکید می‌کند و چرا طنز سیاسی در برخی جوامع پذیرفته‌تر است. نکته مهم این است که ابعاد ابزار مقایسه‌اند، نه برچسب قطعی برای افراد.",
        "assumptions": [
            "فرهنگ ملی الگوهای ارزشی نسبتاً پایدار دارد.",
            "ارزش‌ها را می‌توان با پرسش‌نامه سنجید.",
            "ابعاد، میانگین جامعه‌اند نه ویژگی فرد.",
        ],
        "principles": [
            "ابعاد پیوسته‌اند، نه دوگانه.",
            "نمره ملی، فرد را توصیف نمی‌کند.",
            "زمینه تاریخی، معنای بُعد را می‌سازد.",
        ],
        "critiques": [
            "۱. نمونه: داده‌ها از کارکنان یک شرکت غربی‌اند.\n۲. زمان: فرهنگ ایستا فرض می‌شود.\n۳. ملی‌گرایی روش: تنوع درون‌کشوری نادیده می‌ماند.\n۴. سنجش: پرسش‌نامه، معنای بومی ارزش را نمی‌گیرد.\n۵. کاربرد: خطر کلیشه‌سازی و تعمیم ناروا.",
        ],
        "applications": [
            "بازاریابی بین‌فرهنگی: تنظیم پیام بر پایه ابعاد.",
            "روزنامه‌نگاری تطبیقی: تحلیل سبک رابطه با قدرت.",
            "مدیریت رسانه: تفاوت انتظار از اقتدار و ابهام.",
            "آموزش بین‌فرهنگی: خودآگاهی از سوگیری فرهنگی.",
        ],
        "evolution": "هوفستد در ۱۹۸۰ چهار بُعد را عرضه کرد و در ۲۰۰۱ با همکاری پژوهشگران، بُعد پنجم و ششم را افزود. بعدها پروژه گلوب و نقدهای روش‌شناختی، مدل را بازبینی کردند.",
        "key_concepts": [
            "فاصله قدرت (Power Distance)",
            "فردگرایی و جمع‌گرایی (Individualism-Collectivism)",
            "مردانگی و زنانگی (Masculinity-Femininity)",
            "اجتناب از ابهام (Uncertainty Avoidance)",
            "جهت‌گیری بلندمدت (Long-Term Orientation)",
            "خویشتن‌داری (Indulgence-Restraint)",
        ],
        "studies": [
            "Hofstede, G. (1980). Culture's consequences. Sage.",
            "Hofstede, G. (2001). Culture's consequences (2nd ed.). Sage.",
        ],
        "theorists": "گیرت هوفستد",
        "theorists_text": "هوفستد (۱۹۸۰؛ ۲۰۰۱)",
        "year": 1980,
        "model": "ارزش‌های مشترک ملی → ابعاد پیوسته → نهادها و رفتار ارتباطی → تفاوت میان‌فرهنگی.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nهوفستد فرهنگ را برنامه‌ریزی ذهنی جمعی دید و ابعاد را از داده تجربی استخراج کرد. نوآوری چارچوب، تبدیل فرهنگ به محورهای سنجش‌پذیر است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با پرسش‌نامه ارزش و تحلیل میانگین ملی انجام می‌شود. پژوهشی که نمره ملی را به فرد نسبت می‌دهد، دچار مغالطه بوم‌شناختی می‌شود؛ و پژوهشی که ابعاد را کلیشه می‌گیرد، تنوع درون‌فرهنگی را از دست می‌دهد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در مقایسه تطبیقی است، اما باید با مطالعه بومی تکمیل شود. بُعد بی زمینه تاریخی، به برچسب بدل می‌شود.",
        "critique_text": "\n".join([
            "۱. نمونه: کارکنان یک شرکت غربی.",
            "۲. زمان: فرهنگ ایستا فرض می‌شود.",
            "۳. ملی‌گرایی روش: تنوع درون‌کشوری نادیده می‌ماند.",
            "۴. سنجش: معنای بومی ارزش گرفته نمی‌شود.",
            "۵. کاربرد: خطر کلیشه‌سازی.",
        ]),
        "example_text": "کمپین تبلیغاتی جهانی که در فرهنگ فردگرا بر موفقیت شخصی و در فرهنگ جمع‌گرا بر رفاه خانواده تأکید می‌کند، از همین ابعاد برای تنظیم پیام بهره می‌برد.",
    },
    "MC-691": {
        "summary": "(شوارتز، ۱۹۹۲) نظریه ارزش‌های بنیادی شوارتز، ده ارزش پایه را در یک پیوستار دایره‌ای سازمان می‌دهد. شوارتز با تحلیل داده بیست کشور نشان داد ارزش‌ها همچون هدف‌های انگیزشی، در دو محور متضاد جای می‌گیرند: خودفراروی در برابر خودافزایی، و پذیرش تغییر در برابر حفظ وضع موجود. ارزش‌های همسایه در دایره با هم سازگارند و ارزش‌های مقابل، کشمکش می‌سازند. این ساختار در فرهنگ‌ها تکرار می‌شود، هرچند اولویت‌ها متفاوت‌اند. شوارتز در ۲۰۱۲ مدل را به نوزده ارزش دقیق‌تر کرد. در سطح فرهنگ، هفت جهت‌گیری ارزشی مانند خودمختاری، سلسله‌مراتب و هماهنگی را تفکیک کرد. نظریه، ارزش را معیار انتخاب و توجیه رفتار می‌داند. همچنین پژوهش ارزش‌ها نشان داده اولویت ارزشی با نوع مصرف رسانه پیوند دارد: مخاطبان امنیت‌محور بیشتر خبر و محتوای هشداردهنده را دنبال می‌کنند، در حالی که مخاطبان با ارزش تحریک‌جویی، سرگرمی و محتوای تازه را ترجیح می‌دهند. این پیوند در تبلیغات سیاسی نیز برای بخش‌بندی مخاطب به کار می‌رود.",
        "definition": "نظریه ارزش‌های بنیادی، ده ارزش انگیزشی جهان‌شمول را در پیوستاری دایره‌ای بر پایه سازگاری و تضاد سازمان می‌دهد و اولویت ارزشی افراد و فرهنگ‌ها را توضیح می‌دهد.",
        "main_problem": "مسئله این است که چگونه ارزش‌های انسانی را بدون فهرست بی‌پایان، به ساختاری جهان‌شمول و آزمون‌پذیر رساند. پاسخ، دایره انگیزشی است. پرسش دوم، نسبت ارزش و رفتار است: اولویت ارزشی چگونه انتخاب رسانه و پیام را جهت می‌دهد.",
        "mechanism": "۱. ارزش: هدف فراتر از موقعیت که معیار انتخاب است.\n۲. ده ارزش پایه: خودرهبری، تحریک‌جویی، لذت‌گرایی، پیشرفت، قدرت، امنیت، همنوایی، سنت، خیرخواهی و جهان‌شمول‌گرایی.\n۳. دایره سازگاری: ارزش‌های همسایه هم‌راستا و مقابل‌ها متضادند.\n۴. دو محور: خودفراروی/خودافزایی و پذیرش تغییر/حفظ وضع.\n۵. سطح فرهنگ: هفت جهت‌گیری مانند خودمختاری و سلسله‌مراتب.\n۶. اولویت: ساختار مشترک است، سلسله‌مراتب آن فرهنگی است.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا مخاطب با ارزش امنیت، خبر تهدیدمحور را ترجیح می‌دهد و مخاطب با ارزش جهان‌شمول‌گرایی، محتوای همدلانه را برمی‌گزیند. تبلیغات نیز ارزش‌ها را بهانه اقناع می‌کند. نکته مهم این است که ارزش، انگیزه رفتار است نه پیش‌بینی قطعی آن.",
        "assumptions": [
            "ارزش‌ها هدف‌های انگیزشی جهان‌شمول‌اند.",
            "ساختار ارزش‌ها در فرهنگ‌ها تکرار می‌شود.",
            "اولویت ارزشی، انتخاب و رفتار را جهت می‌دهد.",
        ],
        "principles": [
            "ارزش‌های همسایه سازگارند.",
            "ارزش‌های مقابل کشمکش می‌سازند.",
            "اولویت ارزشی فرهنگی است.",
        ],
        "critiques": [
            "۱. سنجش: پرسش‌نامه به معنای بومی ارزش حساس نیست.\n۲. رفتار: فاصله ارزش و کنش همیشه کم نیست.\n۳. پوشش: ده ارزش، تنوع انگیزه را کامل نمی‌پوشاند.\n۴. زمینه: نمونه‌ها بیشتر دانشجویی‌اند.\n۵. فرهنگ: هفت جهت‌گیری با ابعاد دیگر هم‌پوشانی دارد.",
        ],
        "applications": [
            "مخاطب‌شناسی: پیوند اولویت ارزشی و انتخاب محتوا.",
            "تبلیغات: قاب‌بندی پیام با ارزش مخاطب.",
            "ارتباطات توسعه: هم‌راستایی پیام با ارزش‌های محلی.",
            "رسانه دینی و هویتی: تحلیل کشمکش ارزشی.",
        ],
        "evolution": "شوارتز در ۱۹۹۲ ده ارزش و ساختار دایره‌ای را عرضه کرد و در ۲۰۱۲ مدل نوزده ارزشی را پیشنهاد داد. پژوهش بین‌فرهنگی بعدی، سطح فرهنگ را با جهت‌گیری‌های هفت‌گانه گسترد.",
        "key_concepts": [
            "ارزش بنیادی (Basic Value)",
            "دایره ارزشی (Value Circle)",
            "خودفراروی (Self-Transcendence)",
            "خودافزایی (Self-Enhancement)",
            "پذیرش تغییر (Openness to Change)",
            "حفظ وضع موجود (Conservation)",
        ],
        "studies": [
            "Schwartz, S. H. (1992). Universals in the content and structure of values. Advances in Experimental Social Psychology, 25, 1-65.",
            "Schwartz, S. H. (2012). An overview of the Schwartz theory of basic values. Online Readings in Psychology and Culture, 2(1).",
        ],
        "theorists": "شالوم شوارتز",
        "theorists_text": "شوارتز (۱۹۹۲؛ ۲۰۱۲)",
        "year": 1992,
        "model": "نیازهای جهان‌شمول → ده ارزش در دایره → دو محور متضاد → اولویت فرهنگی → انتخاب و رفتار.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nشوارتز ارزش را پاسخ شناختی به سه نیاز جهان‌شمول دید و ساختار دایره‌ای را از داده تجربی ساخت. نوآوری چارچوب، پیوند سازگاری ارزش با ساختار انگیزشی است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با پرسش‌نامه ارزش شوارتز و تحلیل همسایگی انجام می‌شود. پژوهشی که تنها یک ارزش را می‌سنجد، کشمکش را از دست می‌دهد؛ و پژوهشی که اولویت را به رفتار فرو می‌کاهد، فاصله ارزش و کنش را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در تحلیل قاب‌بندی ارزشی پیام است، اما باید با مطالعه بومی تکمیل شود. ارزش بی زمینه، به برچسب تبلیغاتی بدل می‌شود.",
        "critique_text": "\n".join([
            "۱. سنجش: معنای بومی ارزش گرفته نمی‌شود.",
            "۲. رفتار: فاصله ارزش و کنش کم نیست.",
            "۳. پوشش: ده ارزش کافی نیست.",
            "۴. زمینه: نمونه‌ها دانشجویی‌اند.",
            "۵. فرهنگ: هم‌پوشانی با ابعاد دیگر.",
        ]),
        "example_text": "خبری که بحران زیستی را در قاب «مسئولیت مشترک انسانی» می‌آورد، با ارزش جهان‌شمول‌گرایی هم‌راستاست؛ همان خبر در قاب «تهدید امنیت ملی»، ارزش امنیت را برجسته می‌کند.",
    },
    "MC-682": {
        "summary": "(براون و لوینسون، ۱۹۸۷) نظریه ادب، ادب را مدیریت وجه می‌داند. وجه، تصویر عمومی مورد انتظار فرد است و به وجه مثبت و منفی تقسیم می‌شود. بسیاری از کنش‌های گفتاری، کنش تهدیدکننده وجه‌اند؛ درخواست، انتقاد و رد، وجه منفی یا مثبت را تهدید می‌کنند. براون و لوینسون پنج راهبرد ادب را از صریح تا پرهیز کامل از کنش تفکیک کردند و انتخاب راهبرد را تابع فاصله اجتماعی، قدرت نسبی و درجه تحمیل دانستند. آنان ادب را جهان‌شمول خواندند. پژوهشگران آسیایی و بین‌فرهنگی، این جهان‌شمولی را نقد و بر نقش فرهنگ در معنای وجه تأکید کردند. در ارتباطات، ادب توضیح می‌دهد چرا مصاحبه‌گر نقد را نرم می‌کند. همچنین ادب آنلاین نشان می‌دهد فقدان نشانه‌های چهره، تعبیر تهدید وجه را تشدید می‌کند و بی‌ادبی شبکه‌ای را محتمل‌تر می‌سازد؛ از این رو رسانه‌های تعاملی به هنجارهای صریح مشارکت نیاز دارند و بی‌آن، گفت‌وگوی عمومی به تخریب متقابل وجه فرو می‌کاهد.",
        "definition": "ادب، مجموعه راهبردهای زبانی و تعاملی برای حفظ وجه خود و دیگری در برابر کنش‌های تهدیدکننده است و شدت آن با فاصله، قدرت و تحمیل تنظیم می‌شود.",
        "main_problem": "مسئله این است که چرا گویشوران از بیان مستقیم پرهیز می‌کنند و چرا یک درخواست به شکل‌های متفاوت بیان می‌شود. پاسخ، تهدید وجه است. پرسش دوم، جهان‌شمولی است: آیا معیارهای ادب در همه فرهنگ‌ها یکسان‌اند.",
        "mechanism": "۱. وجه مثبت: نیاز به تأیید و تعلق.\n۲. وجه منفی: نیاز به آزادی و عدم مزاحمت.\n۳. کنش تهدیدکننده: گفتاری که وجه را به خطر می‌اندازد.\n۴. پنج راهبرد: صریح، ادب مثبت، ادب منفی، غیرمستقیم و پرهیز از کنش.\n۵. سه متغیر: فاصله اجتماعی، قدرت نسبی و درجه تحمیل.\n۶. انتخاب راهبرد: هرچه تهدید بیشتر، ادب بیشتر.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا مجری گفت‌وگو نقد تند را با تعارف می‌پوشاند، چرا مصاحبه سیاسی به شکل غیرمستقیم انجام می‌شود و چرا بی‌ادبی آنلاین واکنش جمعی برمی‌انگیزد. نکته مهم این است که ادب، نمایش تصنعی نیست؛ سازوکار حفظ نظم تعاملی است.",
        "assumptions": [
            "انسان وجه دارد و از آن محافظت می‌کند.",
            "بسیاری از کنش‌های گفتاری وجه را تهدید می‌کنند.",
            "حفظ وجه، نظم تعامل را می‌سازد.",
        ],
        "principles": [
            "فاصله، قدرت و تحمیل، ادب را تنظیم می‌کنند.",
            "هرچه تهدید بیشتر، راهبرد غیرمستقیم‌تر.",
            "ادب در فرهنگ‌ها معنای متفاوت دارد.",
        ],
        "critiques": [
            "۱. جهان‌شمولی: معیار ادب غربی به فرهنگ‌های دیگر تحمیل می‌شود.\n۲. فردگرایی: مدل بر فرد و وجه شخصی استوار است.\n۳. تعارف: نظام‌های آیینی مانند تعارف کم دیده می‌شوند.\n۴. قدرت: ساختار کلان کم‌تر تحلیل می‌شود.\n۵. سنجش: تشخیص کنش تهدیدکننده تفسیری است.",
        ],
        "applications": [
            "مصاحبه رسانه‌ای: مدیریت نقد و پرسش تهدیدکننده.",
            "ارتباطات بین‌فرهنگی: شناخت تفاوت معنای ادب.",
            "رسانه و بی‌ادبی: تحلیل شکست وجه آنلاین.",
            "روابط عمومی بحران: حفظ وجه سازمان و مخاطب.",
        ],
        "evolution": "براون و لوینسون در ۱۹۸۷ مدل را در کتاب ادب عرضه کردند. بعدها نقدهای آسیایی، پژوهش تعارف و ادب آنلاین، چارچوب را بومی‌تر و تعاملی‌تر کردند.",
        "key_concepts": [
            "وجه (Face)",
            "وجه مثبت و منفی (Positive and Negative Face)",
            "کنش تهدیدکننده وجه (Face-Threatening Act)",
            "ادب مثبت و منفی (Positive and Negative Politeness)",
            "غیرمستقیمی (Off-Record Strategy)",
            "تحمیل (Ranking of Imposition)",
        ],
        "studies": [
            "Brown, P., & Levinson, S. C. (1987). Politeness: Some universals in language usage. Cambridge University Press.",
            "Goffman, E. (1967). Interaction ritual. Pantheon Books.",
        ],
        "theorists": "پنه‌لوپه براون؛ استیون لوینسون",
        "theorists_text": "براون و لوینسون (۱۹۸۷)",
        "year": 1987,
        "model": "کنش تهدیدکننده وجه × فاصله × قدرت × تحمیل → انتخاب راهبرد ادب → حفظ وجه.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nبراون و لوینسون مدل گافمن را به الگویی زبانی گستردند و وجه را به دو نیاز تقسیم کردند. نوآوری چارچوب، پیوند صورت‌های زبانی با متغیرهای اجتماعی است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با تحلیل گفت‌وگو، آزمون درخواست و مقایسه بین‌فرهنگی انجام می‌شود. پژوهشی که تنها صورت مؤدبانه را می‌شمارد، تهدید وجه را از دست می‌دهد؛ و پژوهشی که مدل را جهان‌شمول مطلق می‌گیرد، تفاوت فرهنگی را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در تحلیل گفت‌وگوی رسانه‌ای است، اما باید با مطالعه قدرت تکمیل شود. ادب بی صداقت، به پنهان‌کاری بدل می‌شود.",
        "critique_text": "\n".join([
            "۱. جهان‌شمولی: معیار غربی تحمیل می‌شود.",
            "۲. فردگرایی: مدل فردمحور است.",
            "۳. تعارف: نظام‌های آیینی کم دیده می‌شوند.",
            "۴. قدرت: ساختار کلان کم‌تر تحلیل می‌شود.",
            "۵. سنجش: تهدید وجه تفسیری است.",
        ]),
        "example_text": "مجری در مصاحبه با مقام ارشد، به جای پرسش صریح درباره خطا، می‌پرسد «اگر باز هم چنین شرایطی پیش بیاید، چه تغییری لازم است؟»؛ پرسش غیرمستقیم، وجه طرف مقابل را حفظ می‌کند.",
    },
    "MC-710": {
        "summary": "(فستینگر، ۱۹۵۷) نظریه انتخاب مواجهه می‌گوید مخاطب اطلاعات هم‌سو با نگرش خود را ترجیح می‌دهد. ریشه چارچوب، نظریه ناهماهنگی شناختی است: فرد برای کاهش تنش روانی، از مواجهه با اطلاعات ناسازگار می‌گریزد. کلپر این سازوکار را به سه گزینش گسترد: گزینش مواجهه، گزینش ادراک و گزینش یادآوری. مخاطب نه منفعل است و نه همه‌چیز را یکسان می‌گیرد؛ او در معرض، در تفسیر و در حافظه گزینش می‌کند. پژوهش بعدی نشان داد گزینش مواجهه همیشه رخ نمی‌دهد و به اعتماد به منبع و اهمیت موضوع بستگی دارد. در محیط الگوریتمی، گزینش فردی و گزینش سامانه‌ای در هم می‌آمیزند و اتاق پژواک را ممکن می‌کنند.",
        "definition": "انتخاب مواجهه، گرایش مخاطب به گزینش اطلاعات هم‌سو با نگرش خویش و پرهیز از اطلاعات ناسازگار است و همراه با گزینش ادراک و یادآوری، اثر رسانه را صافی می‌کند.",
        "main_problem": "مسئله این است که چرا اثر رسانه بر مخاطب یکسان نیست. پاسخ، گزینش پیش و پس از دریافت پیام است. پرسش دوم، تعمیم است: آیا گزینش مواجهه در محیط رسانه‌های اجتماعی و الگوریتمی تشدید می‌شود یا تضعیف.",
        "mechanism": "۱. ناهماهنگی: تعارض شناخت‌ها تنش می‌سازد.\n۲. کاهش تنش: فرد از اطلاعات ناسازگار می‌گریزد.\n۳. گزینش مواجهه: انتخاب منبع هم‌سو.\n۴. گزینش ادراک: تفسیر پیام مطابق نگرش.\n۵. گزینش یادآوری: یادآوری بهتر پیام هم‌سو.\n۶. شرط‌مندی: اعتماد به منبع و اهمیت موضوع، گزینش را تعدیل می‌کند.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا هواداران یک جناح کمتر خبر رسانه رقیب را می‌خوانند، چرا الگوریتم با یادگیری ترجیح، دایره اطلاعات را تنگ می‌کند و چرا کمپین سلامت باید مقاومت گزینشی را پیش‌بینی کند. نکته مهم این است که اتاق پژواک صرفاً محصول الگوریتم نیست؛ گزینش انسانی نیز آن را می‌سازد. همچنین گزینش مواجهه توضیح می‌دهد چرا پیام‌های کمپین که تنها بر مخاطبان هم‌سو تکیه می‌کنند اثری محدود دارند؛ برای عبور از این صافی، پیام باید اعتماد منبع و پیوند با تجربه روزمره مخاطب را تقویت کند و مخاطب مردد را هدف بگیرد، نه صرفاً هوادار متقاعدشده را؛ به تعبیر دیگر، آگاهی از سازوکار گزینش، پیش‌شرط طراحی پیام مؤثر است.",
        "assumptions": [
            "مخاطب از تنش شناختی می‌گریزد.",
            "گزینش در مواجهه، ادراک و یادآوری رخ می‌دهد.",
            "اثر رسانه از صافی گزینش می‌گذرد.",
        ],
        "principles": [
            "اطلاعات هم‌سو ترجیح داده می‌شود.",
            "گزینش، اثر پیام را تعدیل می‌کند.",
            "الگوریتم می‌تواند گزینش را تشدید کند.",
        ],
        "critiques": [
            "۱. سادگی: مدل مخاطب را بیش از اندازه عقلانی می‌بیند.\n۲. شواهد: گزینش مواجهه همیشه تأیید نشده است.\n۳. زمینه: اعتماد و اهمیت موضوع کم‌تر سنجیده می‌شود.\n۴. ساختار: عرضه رسانه و الگوریتم کم‌تر تحلیل می‌شود.\n۵. تعمیم: اتاق پژواک از گزینش فردی نتیجه گرفته می‌شود.",
        ],
        "applications": [
            "کمپین سلامت: پیش‌بینی مقاومت گزینشی مخاطب.",
            "سواد رسانه‌ای: آگاهی از سوگیری مواجهه.",
            "تحلیل الگوریتم: گزینش فردی و سامانه‌ای.",
            "تبلیغات سیاسی: مدیریت مواجهه هوادار و مردد.",
        ],
        "evolution": "فستینگر در ۱۹۵۷ گزینش مواجهه را از ناهماهنگی شناختی استخراج کرد و کلپر در ۱۹۶۰ آن را به سه گزینش گسترد. پژوهش بعدی، شرایط مرزی و نقش الگوریتم را افزود.",
        "key_concepts": [
            "گزینش مواجهه (Selective Exposure)",
            "گزینش ادراک (Selective Perception)",
            "گزینش یادآوری (Selective Retention)",
            "ناهماهنگی شناختی (Cognitive Dissonance)",
            "اتاق پژواک (Echo Chamber)",
            "حباب صافی (Filter Bubble)",
        ],
        "studies": [
            "Festinger, L. (1957). A theory of cognitive dissonance. Row, Peterson.",
            "Klapper, J. T. (1960). The effects of mass communication. Free Press.",
        ],
        "theorists": "لئون فستینگر؛ جوزف کلپر",
        "theorists_text": "فستینگر (۱۹۵۷)؛ کلپر (۱۹۶۰)",
        "year": 1957,
        "model": "نگرش موجود → ترجیح اطلاعات هم‌سو → گزینش مواجهه، ادراک و یادآوری → تعدیل اثر رسانه.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nفستینگر گزینش را سازوکار کاهش ناهماهنگی دید و کلپر آن را در ارتباطات جمعی بسط داد. نوآوری چارچوب، جای دادن مخاطب فعال در مدل اثر است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با آزمایش مواجهه، ردیابی انتخاب محتوا و پرسش درباره نگرش انجام می‌شود. پژوهشی که تنها کلیک را می‌سنجد، انگیزه گزینش را از دست می‌دهد؛ و پژوهشی که از گزینش فردی، اتاق پژواک جمعی می‌سازد، دچار تعمیم ناروا می‌شود.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در تحلیل سوگیری مخاطب است، اما باید با مطالعه عرضه و الگوریتم تکمیل شود. گزینش بی تنوع، به انزوای اطلاعاتی بدل می‌شود.",
        "critique_text": "\n".join([
            "۱. سادگی: مخاطب بیش از اندازه عقلانی است.",
            "۲. شواهد: گزینش همیشه تأیید نشده است.",
            "۳. زمینه: اعتماد و اهمیت موضوع کم‌تر سنجیده می‌شود.",
            "۴. ساختار: عرضه رسانه کم‌تر تحلیل می‌شود.",
            "۵. تعمیم: اتاق پژواک از فرد به جمع تعمیم می‌یابد.",
        ]),
        "example_text": "خواننده‌ای که تنها صفحه هم‌سو با نگرش خود را دنبال می‌کند، خبر ناسازگار را نه تنها نمی‌پذیرد بلکه کمتر می‌بیند؛ الگوریتم نیز با تقویت این الگو، دایره اطلاعات او را تنگ‌تر می‌کند.",
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


NAME_FIX = {}


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
                                       "verified": n_verified, "batch": 109}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH109 THEORY DONE")


if __name__ == "__main__":
    main()
