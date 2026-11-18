# -*- coding: utf-8 -*-
"""Batch 110: full documentation for MC-696, MC-707, MC-721, MC-724."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch110-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch110_theory.json"

S = {
    "MC-696": [
        dict(kind="BOOK",
             title_en="Making News: A Study in the Construction of Reality",
             title_fa="ساختن خبر: پژوهشی در برساخت واقعیت",
             authors="Tuchman, G.", year=1978, publisher="Free Press",
             doi=None, url="https://archive.org/details/makingnewsstudyi0000tuch",
             language="en", isbn="978-0-02-932930-6",
             citation="Tuchman, G. (1978). Making news: A study in the construction of reality. Free Press.",
             locator="work", locator_type="work",
             supports="news as constructed reality through routines, typification and facticity", verified=True),
        dict(kind="BOOK",
             title_en="The Social Construction of Reality: A Treatise in the Sociology of Knowledge",
             title_fa="برساخت اجتماعی واقعیت: رساله‌ای در جامعه‌شناسی معرفت",
             authors="Berger, P. L.; Luckmann, T.", year=1966, publisher="Doubleday",
             doi=None, url=None, language="en", isbn=None,
             citation="Berger, P. L., & Luckmann, T. (1966). The social construction of reality: A treatise in the sociology of knowledge. Doubleday.",
             locator="work", locator_type="work",
             supports="sociology-of-knowledge foundation of constructed reality", verified=False),
    ],
    "MC-707": [
        dict(kind="BOOK",
             title_en="Rediscovering the Social Group: A Self-Categorization Theory",
             title_fa="بازکشف گروه اجتماعی: نظریه طبقه‌بندی خود",
             authors="Turner, J. C.; Hogg, M. A.; Oakes, P. J.; Reicher, S. D.; Wetherell, M. S.",
             year=1987, publisher="Basil Blackwell",
             doi=None, url="https://psycnet.apa.org/record/1987-98657-000",
             language="en", isbn="978-0-631-16586-6",
             citation="Turner, J. C., Hogg, M. A., Oakes, P. J., Reicher, S. D., & Wetherell, M. S. (1987). Rediscovering the social group: A self-categorization theory. Basil Blackwell.",
             locator="work", locator_type="work",
             supports="self-categorization levels, depersonalization and group prototypes", verified=True),
        dict(kind="BOOK_CHAPTER",
             title_en="An Integrative Theory of Intergroup Conflict",
             title_fa="نظریه‌ای تلفیقی درباره تعارض میان‌گروهی",
             authors="Tajfel, H.; Turner, J. C.", year=1979,
             publisher="Brooks/Cole",
             doi=None, url=None, language="en", isbn=None,
             citation="Tajfel, H., & Turner, J. C. (1979). An integrative theory of intergroup conflict. In W. G. Austin & S. Worchel (Eds.), The social psychology of intergroup relations (pp. 33-47). Brooks/Cole.",
             locator="pp. 33-47", locator_type="page_range",
             supports="social identity foundation of self-categorization", verified=False),
    ],
    "MC-721": [
        dict(kind="BOOK",
             title_en="The Functions of Social Conflict",
             title_fa="کارکردهای تعارض اجتماعی",
             authors="Coser, L. A.", year=1956, publisher="Free Press",
             doi=None, url="https://psycnet.apa.org/record/1956-07012-000",
             language="en", isbn=None,
             citation="Coser, L. A. (1956). The functions of social conflict. Free Press.",
             locator="work", locator_type="work",
             supports="functional role of conflict and realistic versus nonrealistic conflict", verified=True),
        dict(kind="BOOK",
             title_en="Class and Class Conflict in Industrial Society",
             title_fa="طبقه و تعارض طبقاتی در جامعه صنعتی",
             authors="Dahrendorf, R.", year=1959, publisher="Stanford University Press",
             doi=None, url=None, language="en", isbn=None,
             citation="Dahrendorf, R. (1959). Class and class conflict in industrial society. Stanford University Press.",
             locator="work", locator_type="work",
             supports="authority relations and institutionalized conflict", verified=False),
    ],
    "MC-724": [
        dict(kind="BOOK",
             title_en="Gender Trouble: Feminism and the Subversion of Identity",
             title_fa="آشفتگی جنسیت: فمینیسم و براندازی هویت",
             authors="Butler, J.", year=1990, publisher="Routledge",
             doi="10.4324/9780203824979",
             url="https://www.taylorfrancis.com/books/mono/10.4324/9780203824979/gender-trouble-judith-butler",
             language="en", isbn=None,
             citation="Butler, J. (1990). Gender trouble: Feminism and the subversion of identity. Routledge.",
             locator="work", locator_type="work",
             supports="gender performativity and subversion of the sex-gender binary", verified=True),
        dict(kind="BOOK",
             title_en="Epistemology of the Closet",
             title_fa="معرفت‌شناسی گنجه",
             authors="Sedgwick, E. K.", year=1990, publisher="University of California Press",
             doi=None, url=None, language="en", isbn=None,
             citation="Sedgwick, E. K. (1990). Epistemology of the closet. University of California Press.",
             locator="work", locator_type="work",
             supports="binary oppositions structuring modern homo/heterosexual definition", verified=False),
    ],
}

ENRICH = {
    "MC-696": {
        "summary": "(تاچمن، ۱۹۷۸) نظریه برساخت اجتماعی خبر می‌گوید خبر، بازتاب بی‌واسطه واقعیت نیست، بلکه برساخته‌ای است که درون سازمان رسانه ساخته می‌شود. تاچمن با مشاهده میدانی نشان داد خبرنگاران از شبکه خبری، نمونه‌گیری و تیپ‌سازی استفاده می‌کنند تا رویدادهای بی‌پایان را به خبر قابل انتشار بدل کنند. عینیت‌گرایی نیز آیینی حرفه‌ای است که اعتماد می‌سازد، نه تضمین بی‌طرفی. زمان‌مندی، مکان‌مندی و روال‌های سازمانی، مرزهای خبر را تعیین می‌کنند. خبر به واقعیت «واقع‌نمایی» می‌بخشد و هم‌زمان بخشی از واقعیت را پنهان می‌کند. این نظریه، پایه پژوهش ساخت‌گرایانه خبر و نقد عینیت خبری است. همچنین تاچمن نشان داد ارزش خبری، توافق جمعی طبیعی نیست، بلکه نتیجه مذاکره پیوسته میان روزنامه‌نگاران، منابع و سازمان است. از این چشم، بی‌طرفی نه نقطه پایانی بلکه ادعایی حرفه‌ای است که باید در برابر منافع سازمانی و سیاسی سنجیده شود؛ و همین نکته، پژوهش رسانه را از پرسش «آیا خبر درست است» به پرسش «چگونه خبر ساخته می‌شود» می‌برد و امکان مقایسه روایت‌های رقیب را فراهم می‌کند، به شرط آنکه پژوهشگر تنها به متن بسنده نکند و روال تحریریه را نیز ببیند.",
        "definition": "برساخت اجتماعی خبر، رویکردی است که تولید خبر را فرایند سازمان‌یافته تیپ‌سازی، انتخاب و واقع‌نمایی می‌داند و خبر را نه آینه واقعیت، بلکه برساخته‌ای روال‌مند و نهادی می‌شمارد.",
        "main_problem": "مسئله این است که چرا خبر با وجود ادعای عینیت، همواره گزینشی و سازمان‌یافته است. پاسخ، روال‌های تولید و برساخت واقعیت است. پرسش دوم، مسئولیت است: اگر خبر برساخته است، معیار اعتبار آن چیست.",
        "mechanism": "۱. شبکه خبری: تعریف دایره منابع و رویدادهای قابل پوشش.\n۲. تیپ‌سازی: رده‌بندی رویداد در قالب‌های آشنا مانند خبر سخت.\n۳. واقع‌نمایی: ساخت نشانه‌های عینی بودن مانند نقل قول و تاریخ.\n۴. آیین عینیت: رویه‌هایی که اعتماد حرفه‌ای می‌سازد.\n۵. زمان و مکان: چارچوب‌بندی رویداد در نظم تحریریه.\n۶. نهاد: پیوند خبر با منبع رسمی، مشروعیت می‌سازد.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا خبر فوری بر رویدادهای قابل برنامه‌ریزی تکیه می‌کند، چرا صداهای غیررسمی کم‌تر شنیده می‌شوند و چرا یک رویداد یکسان در دو رسانه، دو خبر متفاوت می‌سازد. نکته مهم این است که برساخت، به معنای جعل نیست؛ خبر واقعیت را از زاویه‌ای سازمان‌یافته روایت می‌کند.",
        "assumptions": [
            "واقعیت اجتماعی برساخته است.",
            "خبر درون سازمان تولید می‌شود.",
            "روال‌ها، مرز خبر را تعیین می‌کنند.",
        ],
        "principles": [
            "عینیت خبری آیین حرفه‌ای است.",
            "منبع رسمی، مشروعیت خبر می‌سازد.",
            "برساخت، جعل نیست.",
        ],
        "critiques": [
            "۱. نسبی‌گرایی: مرز برساخت و تحریف روشن نیست.\n۲. مخاطب: نقش تفسیر مخاطب کم دیده می‌شود.\n۳. قدرت: ساختار کلان مالکیت کم‌تر تحلیل می‌شود.\n۴. سنجش: مشاهده میدانی، تعمیم را محدود می‌کند.\n۵. تغییر: تحول رسانه دیجیتال کم پوشش می‌ماند.",
        ],
        "applications": [
            "نقد خبر: تحلیل شبکه منبع و تیپ‌سازی.",
            "آموزش روزنامه‌نگاری: آگاهی از روال برسازنده.",
            "سواد رسانه‌ای: شناخت زاویه برساخت خبر.",
            "تحلیل تطبیقی: مقایسه روایت دو رسانه از یک رویداد.",
        ],
        "evolution": "تاچمن در ۱۹۷۸ با مشاهده میدانی این رویکرد را بنیان گذاشت. بعدها پژوهش قاب‌بندی، مطالعات تولید خبر و نقد رسانه دیجیتال، چارچوب را بسط دادند.",
        "key_concepts": [
            "برساخت خبر (News Construction)",
            "شبکه خبری (News Net)",
            "تیپ‌سازی (Typification)",
            "واقع‌نمایی (Facticity)",
            "آیین عینیت (Objectivity Ritual)",
            "روال تولید (Production Routine)",
        ],
        "studies": [
            "Tuchman, G. (1978). Making news: A study in the construction of reality. Free Press.",
            "Berger, P. L., & Luckmann, T. (1966). The social construction of reality. Doubleday.",
        ],
        "theorists": "گی تاچمن",
        "theorists_text": "تاچمن (۱۹۷۸)",
        "year": 1978,
        "model": "رویداد → شبکه خبری و تیپ‌سازی → واقع‌نمایی و آیین عینیت → خبر برساخته → بازتولید نهاد.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nتاچمن با تکیه بر جامعه‌شناسی معرفت، خبر را نهاد برسازنده واقعیت دید. نوآوری چارچوب، پیوند مشاهده میدانی با نقد عینیت است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با مشاهده تحریریه، مصاحبه خبرنگار و تحلیل محتوا انجام می‌شود. پژوهشی که تنها متن خبر را می‌خواند، روال تولید را از دست می‌دهد؛ و پژوهشی که هر انتخاب را تحریف می‌خواند، برساخت را به توطئه فرو می‌کاهد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در نقد رویه خبری است، اما باید با تحلیل مالکیت تکمیل شود. برساخت بی مسئولیت، به بی‌اعتمادی بدل می‌شود.",
        "critique_text": "\n".join([
            "۱. نسبی‌گرایی: مرز برساخت و تحریف روشن نیست.",
            "۲. مخاطب: نقش تفسیر کم دیده می‌شود.",
            "۳. قدرت: مالکیت کلان کم‌تر تحلیل می‌شود.",
            "۴. سنجش: مشاهده میدانی محدود است.",
            "۵. تغییر: رسانه دیجیتال کم پوشش می‌ماند.",
        ]),
        "example_text": "یک اعتراض خیابانی در رسانه‌ای با منبع رسمی، «اخلال در نظم» و در رسانه‌ای با منبع مردمی، «اعتراض مدنی» تیتر می‌شود؛ دو برساخت از یک رویداد.",
    },
    "MC-707": {
        "summary": "(ترنر و همکاران، ۱۹۸۷) نظریه طبقه‌بندی خود توضیح می‌دهد فرد چگونه خود را در قالب مقوله‌های اجتماعی می‌شناسد. خود در سه سطح مقوله‌بندی می‌شود: انسانی، اجتماعی و فردی. با برجسته شدن یک مقوله، فرد ویژگی‌های نمونه آن گروه را بر خود اعمال می‌کند و از ویژگی‌های شخصی فاصله می‌گیرد؛ این فرایند «شخصیت‌زدایی» نام دارد. اصل نسبت فرانمودی تعیین می‌کند کدام مقوله در موقعیت برجسته شود. نتیجه، هم‌شکلی با گروه و رفتار جمعی است. این نظریه، مکمل نظریه هویت اجتماعی تاجفل است و روابط میان‌گروهی، تعصب و رفتار جمعی رسانه‌ای را توضیح می‌دهد. پژوهش بعدی نشان داد رسانه می‌تواند با فعال‌سازی مقوله‌های گروهی، همبستگی یا دوقطبی‌سازی بسازد؛ مثلاً پوشش «نسل ما» در برابر «آن‌ها» سطح طبقه‌بندی خود را تغییر می‌دهد و نگرش مخاطب را به سمت گروه سوق می‌دهد. با این حال، برجستگی مقوله همیشه آگاهانه نیست و بخشی از آن از عادت مصرف رسانه و زمینه تعامل روزمره برمی‌خیزد.",
        "definition": "طبقه‌بندی خود، فرایندی شناختی است که فرد در آن خود را عضو یک مقوله اجتماعی می‌بیند، ویژگی‌های نمونه گروه را بر خود اعمال می‌کند و بر پایه برجستگی موقعیتی، رفتار جمعی می‌سازد.",
        "main_problem": "مسئله این است که چگونه افراد معمولی به کنشگران جمعی بدل می‌شوند. پاسخ، تغییر سطح طبقه‌بندی خود است. پرسش دوم، تعصب است: چگونه برجسته شدن مقوله گروهی، سوگیری میان‌گروهی می‌سازد.",
        "mechanism": "۱. سه سطح: خود انسانی، خود اجتماعی و خود فردی.\n۲. برجستگی: موقعیت، مقوله فعال را تعیین می‌کند.\n۳. نمونه گروهی: ویژگی‌های تیپیک گروه، معیار خودپنداره می‌شود.\n۴. شخصیت‌زدایی: فرد به نماینده گروه بدل می‌شود.\n۵. نسبت فرانمودی: تفاوت میان‌گروهی نسبت به درون‌گروهی، برجستگی را تنظیم می‌کند.\n۶. هم‌شکلی: نگرش و رفتار با گروه هم‌سو می‌شود.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا مخاطب با دیدن نمادهای گروهی، خود را بخشی از «ما» می‌بیند، چرا کمپین هویتی بر نمونه‌های گروهی تکیه می‌کند و چرا قطب‌بندی شبکه‌ای تعصب را تشدید می‌کند. نکته مهم این است که طبقه‌بندی، ثابت نیست؛ تغییر قاب رسانه‌ای می‌تواند سطح برجستگی را تغییر دهد.",
        "assumptions": [
            "خود در مقوله‌های اجتماعی سازمان می‌یابد.",
            "برجستگی مقوله، رفتار را تعیین می‌کند.",
            "نمونه گروهی، معیار خودپنداره می‌شود.",
        ],
        "principles": [
            "سطح طبقه‌بندی، نگرش را تغییر می‌دهد.",
            "برجستگی موقعیتی است، نه ثابت.",
            "شخصیت‌زدایی، رفتار جمعی می‌سازد.",
        ],
        "critiques": [
            "۱. سنجش: برجستگی سخت عملیاتی می‌شود.\n۲. فرهنگ: نمونه‌های گروهی فرهنگی‌اند.\n۳. قدرت: ساختار اجتماعی کم‌تر دیده می‌شود.\n۴. آزمایش: یافته‌ها بیشتر آزمایشگاهی‌اند.\n۵. رسانه: انتقال به مصرف پیچیده رسانه نیازمند احتیاط است.",
        ],
        "applications": [
            "کمپین هویتی: فعال‌سازی خود اجتماعی مخاطب.",
            "تحلیل تعصب: شناخت سوگیری میان‌گروهی.",
            "رسانه و قطب‌بندی: نقش قاب در برجستگی گروه.",
            "بازاریابی برند: پیوند برند با نمونه گروهی.",
        ],
        "evolution": "ترنر و همکاران در ۱۹۸۷ نظریه را در بازکشف گروه اجتماعی عرضه کردند. بعدها پژوهش هویت اجتماعی، رسانه و تعصب، چارچوب را گسترد.",
        "key_concepts": [
            "طبقه‌بندی خود (Self-Categorization)",
            "سطح اجتماعی خود (Social Self)",
            "شخصیت‌زدایی (Depersonalization)",
            "نمونه گروهی (Group Prototype)",
            "نسبت فرانمودی (Meta-Contrast Ratio)",
            "هم‌شکلی (Conformity)",
        ],
        "studies": [
            "Turner, J. C., Hogg, M. A., Oakes, P. J., Reicher, S. D., & Wetherell, M. S. (1987). Rediscovering the social group. Basil Blackwell.",
            "Tajfel, H., & Turner, J. C. (1979). An integrative theory of intergroup conflict. In The social psychology of intergroup relations (pp. 33-47). Brooks/Cole.",
        ],
        "theorists": "جان ترنر؛ مایکل هوگ؛ پنه‌لوپه اوکس",
        "theorists_text": "ترنر و همکاران (۱۹۸۷)",
        "year": 1987,
        "model": "مقوله‌های خود → برجستگی موقعیتی → نمونه گروهی → شخصیت‌زدایی → هم‌شکلی و رفتار جمعی.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nترنر خود را شناخت مقوله‌ای دید و نظریه هویت اجتماعی را از سطح میان‌گروهی به سطح شناختی فرد گسترد. نوآوری چارچوب، توضیح تغییر سطح خود است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با آزمایش برجستگی، مقیاس همانندی و تحلیل نمونه انجام می‌شود. پژوهشی که تنها نگرش را می‌سنجد، سطح طبقه‌بندی را از دست می‌دهد؛ و پژوهشی که نمونه گروهی را کلیشه ثابت می‌گیرد، پویایی آن را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در تحلیل قاب هویتی است، اما باید با مطالعه قدرت تکمیل شود. هویت بی دیگری، به تعصب بدل می‌شود.",
        "critique_text": "\n".join([
            "۱. سنجش: برجستگی سخت عملیاتی می‌شود.",
            "۲. فرهنگ: نمونه‌ها فرهنگی‌اند.",
            "۳. قدرت: ساختار کم‌تر دیده می‌شود.",
            "۴. آزمایش: یافته‌ها آزمایشگاهی‌اند.",
            "۵. رسانه: انتقال نیازمند احتیاط است.",
        ]),
        "example_text": "کمپین تلویزیونی که نوجوانان را «نسل ما» خطاب می‌کند، خود اجتماعی مخاطب را برجسته می‌سازد و رفتار جمعی مانند مشارکت در یک چالش را آسان‌تر می‌کند.",
    },
    "MC-721": {
        "summary": "(کوزر، ۱۹۵۶) نظریه تعارض می‌گوید تعارض همیشه ویرانگر نیست و می‌تواند کارکرد انسجام‌بخش داشته باشد. کوزر میان تعارض واقعی، که برای هدفی مشخص رخ می‌دهد، و تعارض غیرواقعی، که برای تخلیه تنش است، تفکیک کرد. تعارض درون‌گروهی می‌تواند انسجام را افزایش دهد و تعارض میان‌گروهی، مرزهای گروه را روشن‌تر کند. وجود نهادهای تخلیه تنش، مانند رسانه و دادگاه، از انفجار پیشگیری می‌کند. داهرندورف بعدها تعارض را به روابط اقتدار گره زد. در مطالعات رسانه، این چارچوب چارچوب‌بندی خبری تعارض، نقش رسانه در تشدید یا مدیریت آن و کارکرد گفت‌وگوی عمومی را توضیح می‌دهد. در پوشش خبری، چارچوب تعارض تعیین می‌کند که رسانه آن را «منازعه قابل حل» یا «تهدید وجودی» روایت کند؛ روایت دوم معمولاً مذاکره را دشوار و خشونت را محتمل‌تر می‌سازد. از این رو، روزنامه‌نگار مسئول نه با حذف تعارض، بلکه با شفاف‌سازی مواضع، دادن صدای برابر و پرهیز از دامن زدن به تعارض غیرواقعی، به نهادینه شدن آن کمک می‌کند و همین کارکرد، رسانه را از ابزار تبلیغ به عرصه عمومی بدل می‌سازد، هرچند فشار مالکیت این کارکرد را تضعیف می‌کند.",
        "definition": "تعارض اجتماعی، کشمکش میان گروه‌ها بر سر ارزش‌ها، منزلت و منابع است که می‌تواند هم‌زمان ویرانگر و سازنده باشد و رسانه، عرصه و کنشگر مدیریت یا تشدید آن است.",
        "main_problem": "مسئله این است که چرا تعارض در برخی جامعه‌ها به فروپاشی و در برخی به اصلاح می‌انجامد. پاسخ، نهادینه شدن و کارکرد تخلیه تنش است. پرسش دوم، نقش رسانه است: تشدید یا مدیریت تعارض.",
        "mechanism": "۱. تعارض واقعی: رقابت بر سر هدف مشخص.\n۲. تعارض غیرواقعی: تخلیه تنش بدون هدف ابزاری.\n۳. انسجام درون‌گروهی: تعارض بیرونی، همبستگی می‌سازد.\n۴. مرز گروهی: تعارض، مرز ما و آن‌ها را روشن می‌کند.\n۵. نهاد تخلیه: رسانه و دادگاه، فشار را آزاد می‌کنند.\n۶. نهادینه‌سازی: قواعد حل تعارض، فروپاشی را مهار می‌کند.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا پوشش منازعه سیاسی گاه همبستگی ملی می‌سازد و گاه شکاف را عمیق می‌کند، چرا رسانه مسئول با قواعد گفت‌وگو، تعارض را نهادینه می‌کند و چرا سانسور کامل تنش، خطر انفجار را بالا می‌برد. نکته مهم این است که رسانه می‌تواند عرصه تعارض باشد و هم‌زمان بازیگر آن.",
        "assumptions": [
            "تعارض جنبه سازنده دارد.",
            "نهادها تنش را مدیریت می‌کنند.",
            "رسانه عرصه و کنشگر تعارض است.",
        ],
        "principles": [
            "تعارض درون‌گروهی انسجام می‌سازد.",
            "نهادینه شدن، فروپاشی را مهار می‌کند.",
            "سانسور کامل تنش را تشدید می‌کند.",
        ],
        "critiques": [
            "۱. کارکردگرایی: تعارض ساختاری کم‌تر تحلیل می‌شود.\n۲. قدرت: نابرابری بنیادین نادیده می‌ماند.\n۳. سنجش: کارکرد تعارض سخت اندازه‌گیری می‌شود.\n۴. زمینه: نمونه‌ها بیشتر جوامع غربی‌اند.\n۵. رسانه: نقش رسانه در مدل اولیه کم‌رنگ است.",
        ],
        "applications": [
            "پوشش منازعه: تحلیل چارچوب‌بندی تعارض.",
            "گفت‌وگوی عمومی: ساخت نهاد تخلیه تنش.",
            "رسانه بحران: مدیریت تشدید یا آرام‌سازی.",
            "سیاست‌گذاری رسانه: توازن آزادی و قاعده‌مندی.",
        ],
        "evolution": "کوزر در ۱۹۵۶ کارکردهای تعارض را عرضه کرد و داهرندورف در ۱۹۵۹ آن را به روابط اقتدار گسترد. بعدها پژوهش رسانه و منازعه، نقش چارچوب‌بندی خبری را افزود.",
        "key_concepts": [
            "تعارض واقعی (Realistic Conflict)",
            "تعارض غیرواقعی (Nonrealistic Conflict)",
            "انسجام درون‌گروهی (In-Group Cohesion)",
            "نهاد تخلیه تنش (Safety-Valve Institution)",
            "نهادینه‌سازی تعارض (Institutionalization)",
            "مرز گروهی (Group Boundary)",
        ],
        "studies": [
            "Coser, L. A. (1956). The functions of social conflict. Free Press.",
            "Dahrendorf, R. (1959). Class and class conflict in industrial society. Stanford University Press.",
        ],
        "theorists": "لوئیس کوزر؛ رالف داهرندورف",
        "theorists_text": "کوزر (۱۹۵۶)؛ داهرندورف (۱۹۵۹)",
        "year": 1956,
        "model": "تعارض → نهادینه‌سازی یا تخلیه تنش → انسجام یا فروپاشی → بازتعریف مرز گروه.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nکوزر با تکیه بر زیمل، تعارض را کارکردی دید و آن را از نگاه صرفاً آسیب‌شناختی جدا کرد. نوآوری چارچوب، تفکیک تعارض واقعی و غیرواقعی است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با تحلیل تاریخی، مطالعه نهاد و مشاهده تعارض انجام می‌شود. پژوهشی که تنها شدت تعارض را می‌سنجد، کارکرد آن را از دست می‌دهد؛ و پژوهشی که هر تعارض را سازنده می‌خواند، خشونت ساختاری را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در تحلیل پوشش منازعه است، اما باید با اقتصاد سیاسی رسانه تکمیل شود. تعارض بی قاعده، به خشونت بدل می‌شود.",
        "critique_text": "\n".join([
            "۱. کارکردگرایی: ساختار کم‌تر تحلیل می‌شود.",
            "۲. قدرت: نابرابری بنیادین نادیده می‌ماند.",
            "۳. سنجش: کارکرد سخت اندازه‌پذیر است.",
            "۴. زمینه: نمونه‌ها غربی‌اند.",
            "۵. رسانه: نقش رسانه کم‌رنگ است.",
        ]),
        "example_text": "پوشش تلویزیونی یک اعتصاب می‌تواند با دعوت از هر دو طرف، تعارض را نهادینه کند یا با قاب «بحران امنیتی»، آن را به تقابل غیرقابل حل بدل سازد.",
    },
    "MC-724": {
        "summary": "(باتلر، ۱۹۹۰) نظریه کوئیر و رسانه از اندیشه باتلر درباره اجراگری جنسیت آغاز می‌شود. باتلر استدلال کرد جنسیت امری طبیعی و پیشین نیست، بلکه با تکرار اجراهای اجتماعی ساخته می‌شود. اگر جنسیت اجراست، دگرجنس‌گرایی هنجارمند نیز برساخته است، نه قانون طبیعت. کوئیر به تحلیل رسانه راه یافت تا بازنمایی اقلیت‌های جنسی، کلیشه‌سازی، پنهان‌سازی و بازارپسندی هویت را بررسی کند. مفاهیمی مانند دگرجنس‌گراهنجاری، هم‌جنساگرایی و طرد دوگانه مرد/زن، ابزار نقد بازنمایی شدند. نقد پسااستعماری و کوئیر رنگین‌پوستان، محدودیت روایت غربی را گوشزد کرد. این نظریه، سیاست بازنمایی و سکوت رسانه‌ای را برجسته می‌سازد. نظریه کوئیر همچنین به رابطه سکوت و قدرت توجه می‌کند: آنچه رسانه نشان نمی‌دهد، در شکل دادن به تصور عمومی از «بهنجار» به همان اندازه مهم است که آنچه نشان می‌دهد. از این چشم، تنوع بازنمایی تنها موضوع حساسیت فرهنگی نیست، بلکه پرسشی درباره عدالت رسانه‌ای است؛ و نقد کوئیر، بازنمایی را از دایره سلیقه بیرون می‌آورد و به میدان قدرت پیوند می‌دهد. با این حال، نظریه باید از فروکاستن هویت به تنها یک محور بپرهیزد و هم‌زمانی جنسیت، طبقه و نژاد را در نظر بگیرد، زیرا تجربه رسانه‌ای افراد در تلاقی این محورها شکل می‌گیرد.",
        "definition": "نظریه کوئیر در رسانه، چارچوبی است که جنسیت و میل را برساخته و اجراگری می‌داند و بازنمایی رسانه‌ای هویت‌های جنسی را از منظر هنجارشکنی، کلیشه و قدرت نقد می‌کند.",
        "main_problem": "مسئله این است که چرا رسانه برخی هویت‌های جنسی را طبیعی و برخی را حاشیه‌ای نشان می‌دهد. پاسخ، هنجار دگرجنس‌گراهنجار است. پرسش دوم، مقاومت است: چگونه بازنمایی می‌تواند هنجار را به چالش بکشد.",
        "mechanism": "۱. اجراگری: جنسیت با تکرار اجرا ساخته می‌شود.\n۲. دگرجنس‌گراهنجاری: هنجار دگرجنس‌گرا، مرز بهنجار و نابهنجار می‌سازد.\n۳. کلیشه بازنمایی: رسانه هویت را به تیپ تقلیل می‌دهد.\n۴. پنهان‌سازی: سکوت و حذف، نامرئی‌سازی می‌سازد.\n۵. بازارپسندی: هویت حاشیه‌ای به کالا بدل می‌شود.\n۶. هنجارشکنی: تکرار نافرمان، معنای هنجار را می‌شکند.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا شخصیت‌های غیردگرجنس‌گرا اغلب در نقش کلیشه‌ای ظاهر می‌شوند، چرا سکوت رسانه‌ای خود پیام است و چرا بازنمایی متنوع، سیاست هویت را تغییر می‌دهد. نکته مهم این است که نظریه، بازنمایی را آینه واقعیت نمی‌داند؛ آن را سازنده معنا می‌شمارد.",
        "assumptions": [
            "جنسیت برساخته و اجراگری است.",
            "رسانه هنجار جنسی را بازتولید می‌کند.",
            "بازنمایی، معنا می‌سازد نه آینه واقعیت.",
        ],
        "principles": [
            "هنجار دگرجنس‌گرا مرز می‌سازد.",
            "سکوت رسانه‌ای نیز پیام است.",
            "تکرار نافرمان، هنجار را می‌شکند.",
        ],
        "critiques": [
            "۱. انتزاع: مفاهیم برای تحلیل تجربی سخت عملیاتی می‌شوند.\n۲. زمینه: مدل بیشتر غربی و انگلیسی‌زبان است.\n۳. طبقه: پیوند جنسیت و اقتصاد کم‌تر دیده می‌شود.\n۴. مخاطب: دریافت مخاطب ناهمگون کم‌تر تحلیل می‌شود.\n۵. سیاست: مرز نقد و نمایش کالایی روشن نیست.",
        ],
        "applications": [
            "نقد بازنمایی: تحلیل کلیشه جنسی در رسانه.",
            "سیاست تنوع: طراحی بازنمایی غیرکلیشه‌ای.",
            "سواد رسانه‌ای: شناخت هنجار جنسی رسانه‌ای.",
            "مطالعات مخاطب: تفسیر ناهمگون هویت.",
        ],
        "evolution": "باتلر در ۱۹۹۰ آشفتگی جنسیت را منتشر کرد و سجویک در همان سال معرفت‌شناسی گنجه را عرضه کرد. بعدها نظریه کوئیر رنگین‌پوستان و مطالعات رسانه، چارچوب را بومی‌تر کردند.",
        "key_concepts": [
            "اجراگری جنسیت (Gender Performativity)",
            "دگرجنس‌گراهنجاری (Heteronormativity)",
            "دوگانه جنسی (Sex-Gender Binary)",
            "هنجارشکنی (Subversion)",
            "بازنمایی (Representation)",
            "پنهان‌سازی رسانه‌ای (Media Erasure)",
        ],
        "studies": [
            "Butler, J. (1990). Gender trouble. Routledge.",
            "Sedgwick, E. K. (1990). Epistemology of the closet. University of California Press.",
        ],
        "theorists": "جودیت باتلر؛ ایو کوسوفسکی سجویک",
        "theorists_text": "باتلر (۱۹۹۰)؛ سجویک (۱۹۹۰)",
        "year": 1990,
        "model": "هنجار جنسی → اجرای مکرر رسانه‌ای → کلیشه و پنهان‌سازی → تکرار نافرمان → بازتعریف معنا.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nباتلر با نقد فمینیسم ذات‌گرا، جنسیت را اجرا دید و سجویک دوگانه هنجاری را نقد کرد. نوآوری چارچوب، پیوند هویت با سیاست بازنمایی است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با تحلیل متن، مطالعه مخاطب و بررسی سیاست رسانه انجام می‌شود. پژوهشی که تنها شمارش شخصیت‌ها را می‌سنجد، معنا را از دست می‌دهد؛ و پژوهشی که هر بازنمایی را کالایی می‌خواند، مقاومت را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در نقد کلیشه است، اما باید با تحلیل اقتصاد رسانه تکمیل شود. نمایش بی سیاست، به کالا بدل می‌شود.",
        "critique_text": "\n".join([
            "۱. انتزاع: عملیاتی‌سازی دشوار است.",
            "۲. زمینه: مدل غربی است.",
            "۳. طبقه: پیوند با اقتصاد کم دیده می‌شود.",
            "۴. مخاطب: دریافت ناهمگون کم‌تر تحلیل می‌شود.",
            "۵. سیاست: مرز نقد و کالا روشن نیست.",
        ]),
        "example_text": "سریالی که شخصیت غیردگرجنس‌گرا را تنها در نقش تراژیک یا طنز نشان می‌دهد، با همان نمایش، کلیشه را بازتولید می‌کند؛ بازنمایی بی کلیشه، سیاست متن را تغییر می‌دهد.",
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
    "MC-707": ("نظریه طبقه‌بندی خود", "Self-Categorization Theory",
               "label repaired: corrupted 'خودگربه' -> 'طبقه‌بندی خود'"),
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
                                       "verified": n_verified, "batch": 110}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH110 THEORY DONE")


if __name__ == "__main__":
    main()
