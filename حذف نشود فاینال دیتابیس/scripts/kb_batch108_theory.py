# -*- coding: utf-8 -*-
"""Batch 108: full documentation for MC-686, MC-687, MC-688, MC-689."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch108-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch108_theory.json"

S = {
    "MC-686": [
        dict(kind="BOOK",
             title_en="Relating: Dialogues and Dialectics",
             title_fa="رابطه‌سازی: گفت‌وگومندی و دیالکتیک‌ها",
             authors="Baxter, L. A.; Montgomery, B. M.", year=1996,
             publisher="Guilford Press",
             doi=None, url="https://www.guilford.com/books/Relating/Baxter-Montgomery/9781572301016",
             language="en", isbn="978-1-57230-101-6",
             citation="Baxter, L. A., & Montgomery, B. M. (1996). Relating: Dialogues and dialectics. Guilford Press.",
             locator="work", locator_type="work",
             supports="relational dialectics of integration, stability and expression", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Relationships as Dialogues",
             title_fa="روابط به‌عنوان گفت‌وگو",
             authors="Baxter, L. A.", year=2004, publisher="Personal Relationships",
             doi=None, url=None, language="en", isbn=None,
             citation="Baxter, L. A. (2004). Relationships as dialogues. Personal Relationships, 11(1), 1-22.",
             locator="11(1):1-22", locator_type="page_range",
             supports="dialogic elaboration of relational dialectics", verified=False),
    ],
    "MC-687": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Social Behavior as Exchange",
             title_fa="رفتار اجتماعی به‌عنوان مبادله",
             authors="Homans, G. C.", year=1958,
             publisher="American Journal of Sociology",
             doi=None, url="https://www.journals.uchicago.edu/doi/abs/10.1086/222355",
             language="en", isbn=None,
             citation="Homans, G. C. (1958). Social behavior as exchange. American Journal of Sociology, 63(6), 597-606.",
             locator="63(6):597-606", locator_type="page_range",
             supports="social behavior as exchange of material and non-material goods", verified=True),
        dict(kind="BOOK",
             title_en="Exchange and Power in Social Life",
             title_fa="مبادله و قدرت در زندگی اجتماعی",
             authors="Blau, P. M.", year=1964, publisher="Wiley",
             doi=None, url=None, language="en", isbn=None,
             citation="Blau, P. M. (1964). Exchange and power in social life. Wiley.",
             locator="work", locator_type="work",
             supports="exchange theory of power, reciprocity and institutionalization", verified=False),
    ],
    "MC-688": [
        dict(kind="BOOK",
             title_en="The Social Psychology of Groups",
             title_fa="روان‌شناسی اجتماعی گروه‌ها",
             authors="Thibaut, J. W.; Kelley, H. H.", year=1959, publisher="Wiley",
             doi=None, url="https://psycnet.apa.org/record/1960-04214-000",
             language="en", isbn=None,
             citation="Thibaut, J. W., & Kelley, H. H. (1959). The social psychology of groups. Wiley.",
             locator="work", locator_type="work",
             supports="outcome matrix, comparison level and interdependence", verified=True),
        dict(kind="BOOK",
             title_en="Interpersonal Relations: A Theory of Interdependence",
             title_fa="روابط میان‌فردی: نظریه وابستگی متقابل",
             authors="Kelley, H. H.; Thibaut, J. W.", year=1978, publisher="Wiley",
             doi=None, url=None, language="en", isbn=None,
             citation="Kelley, H. H., & Thibaut, J. W. (1978). Interpersonal relations: A theory of interdependence. Wiley.",
             locator="work", locator_type="work",
             supports="given and effective matrices, transformation of motivation", verified=False),
    ],
    "MC-689": [
        dict(kind="BOOK",
             title_en="Attachment and Loss, Vol. 1: Attachment",
             title_fa="دلبستگی و فقدان، جلد یک: دلبستگی",
             authors="Bowlby, J.", year=1969, publisher="Basic Books",
             doi=None, url=None,
             language="en", isbn=None,
             citation="Bowlby, J. (1969). Attachment and loss: Vol. 1. Attachment. Basic Books.",
             locator="work", locator_type="work",
             supports="attachment behavioral system, secure base and internal working models", verified=True),
        dict(kind="BOOK",
             title_en="Patterns of Attachment: A Psychological Study of the Strange Situation",
             title_fa="الگوهای دلبستگی: پژوهشی روان‌شناختی در موقعیت ناآشنا",
             authors="Ainsworth, M. D. S.; Blehar, M. C.; Waters, E.; Wall, S.", year=1978,
             publisher="Lawrence Erlbaum",
             doi=None, url=None, language="en", isbn=None,
             citation="Ainsworth, M. D. S., Blehar, M. C., Waters, E., & Wall, S. (1978). Patterns of attachment: A psychological study of the strange situation. Lawrence Erlbaum.",
             locator="work", locator_type="work",
             supports="secure, avoidant and ambivalent attachment patterns", verified=False),
    ],
}

ENRICH = {
    "MC-686": {
        "summary": "(باکستر و مونتگومری، ۱۹۹۶) نظریه دیالکتیک‌های رابطه‌ای می‌گوید رابطه، حاصل گفت‌وگومندی و کشمکش میان گرایش‌های متضاد است، نه مسیری خطی به سوی صمیمیت. باکستر و مونتگومری با تکیه بر گفت‌وگومندی باختین، سه دیالکتیک اصلی را تفکیک کردند: پیوند و جدایی، ثبات و تغییر، و بیان و پنهان‌کاری. این تنش‌ها پایان‌ناپذیرند و هر راه‌حل، تنش را به شکلی تازه بازمی‌گرداند. زوج‌ها با انتخاب، جداسازی، خنثی‌سازی و بازقاب‌بندی، تنش را مدیریت می‌کنند. نظریه، ارتباط را سازنده رابطه می‌داند، نه فقط ابزار انتقال معنا. در تحلیل رسانه‌ای، همین چارچوب نشان می‌دهد مخاطب و رسانه نیز میان نزدیکی و فاصله، و میان خودافشایی و حفظ حریم در نوسان‌اند؛ روزنامه‌نگار میان نزدیکی به منبع و فاصله حرفه‌ای حرکت می‌کند و رسانه عمومی میان پاسخ‌گویی به مخاطب و استقلال تحریریه گرفتار تنش است. از این رو دیالکتیک‌ها نه نقص رابطه، بلکه ماده سازنده آن‌اند و مدیریت آگاهانه آن‌ها، به جای حذف، انعطاف رابطه را افزایش می‌دهد.",
        "definition": "دیالکتیک‌های رابطه‌ای، چارچوبی است که رابطه را میدان کشمکش پیوسته میان گرایش‌های متضاد مانند پیوند و جدایی یا ثبات و تغییر می‌داند و ارتباط را راه مدیریت و بازتولید این تنش‌ها می‌شمارد.",
        "main_problem": "مسئله این است که چرا زوج‌ها هم‌زمان به نزدیکی و استقلال نیاز دارند و چرا حل قطعی این تنش ممکن نیست. پاسخ، سرشت دیالکتیکی رابطه است. پرسش دوم، مدیریت است: کدام الگوی ارتباطی تنش را سازنده و کدام آن را مخرب می‌کند.",
        "mechanism": "۱. پیوند و جدایی: نیاز هم‌زمان به صمیمیت و استقلال.\n۲. ثبات و تغییر: نیاز به امنیت و نیاز به تازگی.\n۳. بیان و پنهان‌کاری: نیاز به صداقت و نیاز به حریم.\n۴. پایان‌ناپذیری: هر راه‌حل، تنش را به شکلی تازه بازمی‌گرداند.\n۵. راهبردهای مدیریت: انتخاب یک قطب، جداسازی حوزه‌ها، خنثی‌سازی و بازقاب‌بندی.\n۶. گفت‌وگومندی: صداهای متضاد، معنای رابطه را می‌سازند.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا زوج‌ها درباره میزان اشتراک‌گذاری زندگی در شبکه اجتماعی کشمکش می‌کنند، چرا خبرنگار میان نزدیکی به منبع و فاصله حرفه‌ای نوسان می‌کند و چرا رسانه عمومی میان پاسخ‌گویی و استقلال تحریریه تنش دارد. نکته مهم این است که تنش دیالکتیکی نقص رابطه نیست؛ ماده سازنده آن است و مدیریت آگاهانه، رابطه را انعطاف‌پذیر می‌کند.",
        "assumptions": [
            "رابطه از گرایش‌های متضاد ساخته می‌شود.",
            "تنش‌ها پایان‌ناپذیرند.",
            "ارتباط، تنش را مدیریت و بازتولید می‌کند.",
        ],
        "principles": [
            "پیوند و جدایی هم‌زمان مطلوب‌اند.",
            "هر راه‌حل، تنش تازه می‌سازد.",
            "مدیریت آگاهانه، رابطه را انعطاف‌پذیر می‌کند.",
        ],
        "critiques": [
            "۱. انتزاع: مفاهیم دیالکتیکی سخت عملیاتی می‌شوند.\n۲. زمینه: نمونه‌ها بیشتر غربی و زوج‌محورند.\n۳. قدرت: نابرابری و اجبار کم‌تر دیده می‌شود.\n۴. سنجش: تنش از تفسیر گفت‌وگو استخراج می‌شود.\n۵. تعمیم: کاربرد به رابطه رسانه‌ای نیازمند ترجمه است.",
        ],
        "applications": [
            "مشاوره زوج: شناخت تنش پیوند و استقلال.",
            "حریم خصوصی دیجیتال: مدیریت بیان و پنهان‌کاری.",
            "اخلاق خبر: توازن نزدیکی به منبع و فاصله حرفه‌ای.",
            "رسانه عمومی: مدیریت تنش پاسخ‌گویی و استقلال.",
        ],
        "evolution": "باکستر و مونتگومری در ۱۹۹۶ چارچوب را در کتاب رابطه‌سازی عرضه کردند. بعدها پژوهش ارتباط زوج، حریم خصوصی و رسانه، دیالکتیک‌ها را به زمینه‌های تازه گسترد و بر نقش قدرت تأکید کرد.",
        "key_concepts": [
            "دیالکتیک رابطه‌ای (Relational Dialectic)",
            "پیوند و جدایی (Integration-Separation)",
            "ثبات و تغییر (Stability-Change)",
            "بیان و پنهان‌کاری (Expression-Nonexpression)",
            "گفت‌وگومندی (Dialogism)",
            "بازقاب‌بندی (Reframing)",
        ],
        "studies": [
            "Baxter, L. A., & Montgomery, B. M. (1996). Relating: Dialogues and dialectics. Guilford Press.",
            "Baxter, L. A. (2004). Relationships as dialogues. Personal Relationships, 11(1), 1-22.",
        ],
        "theorists": "لزلی باکستر؛ باربارا مونتگومری",
        "theorists_text": "باکستر و مونتگومری (۱۹۹۶)",
        "year": 1996,
        "model": "گرایش‌های متضاد (پیوند/جدایی، ثبات/تغییر، بیان/پنهان‌کاری) → تنش پایان‌ناپذیر → راهبردهای مدیریت → بازتولید تنش در شکل تازه.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nباکستر و مونتگومری با تکیه بر گفت‌وگومندی باختین، رابطه را میدان صداهای متضاد دیدند. نوآوری چارچوب، رد حل خطی تنش است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با تحلیل گفت‌وگو، مصاحبه زوج و مشاهده تعامل انجام می‌شود. پژوهشی که تنها تعارض را می‌سنجد، تنش سازنده را از دست می‌دهد؛ و پژوهشی که دیالکتیک را به تعارض فرو می‌کاهد، سرشت پایان‌ناپذیر آن را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در تحلیل تنش حریم و بیان است، اما باید با تحلیل قدرت تکمیل شود. تنش بی قدرت، به نوسان بی پایان بدل می‌شود.",
        "critique_text": "\n".join([
            "۱. انتزاع: عملیاتی‌سازی دشوار است.",
            "۲. زمینه: نمونه‌ها غربی و زوج‌محورند.",
            "۳. قدرت: نابرابری کم دیده می‌شود.",
            "۴. سنجش: استخراج تنش تفسیری است.",
            "۵. تعمیم: کاربرد رسانه‌ای نیازمند ترجمه است.",
        ]),
        "example_text": "زوجی بر سر انتشار عکس مشترک در شبکه اجتماعی اختلاف دارند؛ یکی آن را بیان صمیمیت و دیگری آن را نقض حریم می‌داند. توافق بر حوزه‌های جداگانه، تنش را مدیریت می‌کند نه حذف.",
    },
    "MC-687": {
        "summary": "(هومنز، ۱۹۵۸) نظریه تبادل اجتماعی، رفتار اجتماعی را مبادله کالاهای مادی و غیرمادی می‌بیند: پاداش، هزینه، تأیید، منزلت و اطلاعات. هومنز با پیوند روان‌شناسی رفتارگرا و اقتصاد، نشان داد کنش متقابل تا زمانی ادامه می‌یابد که پاداش‌ها از هزینه‌ها بیشتر باشد. بلاو در ۱۹۶۴ این چارچوب را به قدرت، عدالت و نهادسازی گسترد: کسی که وابستگی یک‌سویه ایجاد می‌کند، قدرت می‌یابد. تبادل مستقیم و غیرمستقیم، هنجار تقابل و مقایسه سطح پاداش، مفاهیم کلیدی‌اند. نظریه، تعامل را نه صرفاً نمادین، بلکه حساب‌گرانه و وابسته به سود و زیان می‌داند. با این حال، اگر مبادله به تنها منطق رابطه بدل شود، فداکاری، همدلی و تعهد اخلاقی از چشم می‌افتند؛ از این رو نظریه بیشتر برای تحلیل رابطه‌های ابزاری و سازمانی کارآمد است و در روابط صمیمی باید با مفاهیم تعهد و هویت تکمیل شود.",
        "definition": "تبادل اجتماعی، چارچوبی است که کنش متقابل را مبادله پاداش و هزینه می‌داند و ادامه رابطه، قدرت و هنجارهای آن را بر پایه سنجش سود، وابستگی و تقابل توضیح می‌دهد.",
        "main_problem": "مسئله این است که چرا برخی روابط پایدار می‌مانند و برخی به سرعت پایان می‌یابند. پاسخ، تراز پاداش و هزینه است. پرسش دوم، مرز است: آیا همه رفتار اجتماعی را می‌توان مبادله خواند یا فداکاری، همدلی و هویت را نمی‌پوشاند.",
        "mechanism": "۱. پاداش: هر پیامد ارزشمند کنش، از تأیید تا پول.\n۲. هزینه: زمان، انرژی و فرصت از دست رفته.\n۳. تقابل: انتظار پاسخ متناسب به لطف و کمک.\n۴. سطح مقایسه: معیار فرد برای سود قابل قبول.\n۵. وابستگی و قدرت: وابستگی یک‌سویه، قدرت نامتقارن می‌سازد.\n۶. نهادسازی: تبادل تکرارشونده، هنجار و ساختار می‌سازد.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا رابطه خبرنگار و منبع بر مبادله اطلاعات و دسترسی استوار است، چرا مخاطب در برابر محتوای رایگان، داده و توجه می‌دهد و چرا رسانه برای حفظ مخاطب به پاداش پیوسته نیاز دارد. در روابط عمومی، دسترسی خبری در برابر پوشش مطلوب، نمونه‌ای از تبادل است. نکته مهم این است که فروکاستن همه رابطه به مبادله، فداکاری و تعهد اخلاقی را از دست می‌دهد.",
        "assumptions": [
            "رفتار اجتماعی پاداش و هزینه دارد.",
            "افراد سود و زیان کنش را می‌سنجند.",
            "تبادل تکرارشونده، هنجار و ساختار می‌سازد.",
        ],
        "principles": [
            "تقابل، تبادل را پایدار می‌کند.",
            "وابستگی یک‌سویه، قدرت می‌سازد.",
            "سطح مقایسه، رضایت را تنظیم می‌کند.",
        ],
        "critiques": [
            "۱. انسان عقلانی: فرض محاسبه‌گری، احساس و فداکاری را کم می‌بیند.\n۲. فرهنگ: معنای پاداش در فرهنگ‌ها یکسان نیست.\n۳. سنجش: پاداش غیرمادی سخت اندازه‌گیری می‌شود.\n۴. قدرت: ساختار اجتماعی کلان کم‌تر دیده می‌شود.\n۵. تعمیم: همه روابط تبادلی نیستند.",
        ],
        "applications": [
            "روابط خبرنگار و منبع: شناخت مبادله دسترسی و اطلاعات.",
            "روابط عمومی: تحلیل تبادل پوشش و دسترسی.",
            "اقتصاد توجه: سنجش پاداش و هزینه مخاطب.",
            "مدیریت رابطه: شناخت وابستگی نامتقارن.",
        ],
        "evolution": "هومنز در ۱۹۵۸ چارچوب را در مجله جامعه‌شناسی آمریکا عرضه کرد و بلاو در ۱۹۶۴ آن را به قدرت و نهاد گسترد. بعدها نظریه عدالت، سرمایه اجتماعی و اقتصاد توجه، عناصر تبادلی را بازبینی کردند.",
        "key_concepts": [
            "تبادل اجتماعی (Social Exchange)",
            "پاداش و هزینه (Reward and Cost)",
            "هنجار تقابل (Reciprocity Norm)",
            "سطح مقایسه (Comparison Level)",
            "وابستگی (Dependence)",
            "قدرت نامتقارن (Asymmetric Power)",
        ],
        "studies": [
            "Homans, G. C. (1958). Social behavior as exchange. American Journal of Sociology, 63(6), 597-606.",
            "Blau, P. M. (1964). Exchange and power in social life. Wiley.",
        ],
        "theorists": "جرج هومنز؛ پیتر بلاو",
        "theorists_text": "هومنز (۱۹۵۸)؛ بلاو (۱۹۶۴)",
        "year": 1958,
        "model": "پاداش − هزینه → تراز سود → ادامه یا قطع تبادل → تقابل و وابستگی → قدرت یا نهادسازی.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nهومنز رفتار اجتماعی را به مبادله فروکاست و بلاو آن را به ساختار قدرت گره زد. نوآوری چارچوب، پیوند روان‌شناسی رفتارگرا با جامعه‌شناسی است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با مشاهده تبادل، مقیاس رضایت و تحلیل وابستگی انجام می‌شود. پژوهشی که تنها پاداش مادی را می‌سنجد، منزلت و تأیید را از دست می‌دهد؛ و پژوهشی که هر کنش را مبادله می‌خواند، فداکاری را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در تحلیل رابطه منبع و رسانه است، اما باید با اخلاق تکمیل شود. تبادل بی هنجار، به فساد دسترسی بدل می‌شود.",
        "critique_text": "\n".join([
            "۱. انسان عقلانی: احساس و فداکاری کم دیده می‌شود.",
            "۲. فرهنگ: معنای پاداش یکسان نیست.",
            "۳. سنجش: پاداش غیرمادی اندازه‌پذیر نیست.",
            "۴. قدرت: ساختار کلان کم دیده می‌شود.",
            "۵. تعمیم: همه روابط تبادلی نیستند.",
        ]),
        "example_text": "خبرنگاری که در برابر دسترسی به یک پرونده، به منبع وعده انتشار بی قید می‌دهد، تبادلی نامتوازن می‌سازد؛ استقلال تحریریه هزینه پنهان این مبادله است.",
    },
    "MC-688": {
        "summary": "(تیبو و کلی، ۱۹۵۹) نظریه وابستگی متقابل، رابطه دونفره را با ماتریس پیامدها تحلیل می‌کند: هر ترکیب از کنش دو طرف، پیامدهایی برای هر دو دارد. سطح مقایسه، حداقل پیامد قابل قبول و سطح مقایسه جایگزین، بهترین گزینه بیرونی را نشان می‌دهد. وابستگی از همین مقایسه‌ها برمی‌خیزد و قدرت را نامتقارن می‌کند. کلی و تیبو در ۱۹۷۸ میان ماتریس داده‌شده و ماتریس اثربخش، یعنی پیامد پس از بازتعریف موقعیت، تفکیک کردند. هم‌راستایی منافع، هماهنگی و تعارض، گونه‌های وابستگی را می‌سازند. نظریه، رابطه را ساختار پیامدهای متقابل می‌داند.",
        "definition": "وابستگی متقابل، چارچوبی است که رابطه را ماتریس پیامدهای متقابل کنش‌ها می‌داند و وابستگی، قدرت و رضایت را بر پایه سطح مقایسه، گزینه جایگزین و هم‌راستایی منافع توضیح می‌دهد.",
        "main_problem": "مسئله این است که چرا در برخی روابط قدرت نامتقارن است و چرا افراد در رابطه نامطلوب می‌مانند. پاسخ، ساختار وابستگی و گزینه‌های جایگزین است. پرسش دوم، تغییر است: چگونه بازتعریف موقعیت، پیامدهای رابطه را دگرگون می‌کند.",
        "mechanism": "۱. ماتریس پیامد: هر ترکیب کنش، پیامد دو طرف را می‌سازد.\n۲. سطح مقایسه: حداقل پیامد قابل قبول برای ماندن.\n۳. گزینه جایگزین: بهترین گزینه بیرونی، وابستگی را تنظیم می‌کند.\n۴. قدرت: وابستگی کمتر، قدرت بیشتر می‌سازد.\n۵. هم‌راستایی منافع: هماهنگی، تبادل، وابستگی متقابل یا تعارض.\n۶. بازتعریف: طرفین پیامدها را بازتفسیر و ماتریس اثربخش را می‌سازند.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا منبعی که گزینه‌های رسانه‌ای بیشتری دارد، کنترل بیشتری بر مصاحبه دارد، چرا همکاری رسانه و نهاد در بحران به وابستگی متقابل بدل می‌شود و چرا مخاطب وفادار، قدرت چانه‌زنی رسانه را تغییر می‌دهد. نکته مهم این است که وابستگی متقابل همیشه نامتقارن نیست؛ هم‌راستایی منافع، رابطه پایدارتر می‌سازد. همچنین این چارچوب نشان می‌دهد چرا رسانه در بحران به همکاری با نهادهای رسمی وابسته می‌شود: هر دو طرف به منابع یکدیگر نیاز دارند و همین وابستگی متقابل، هم فرصت هماهنگی و هم خطر ادغام منافع را می‌سازد و مرز میان اطلاع‌رسانی و همداستانی را به آزمون می‌گذارد.",
        "assumptions": [
            "کنش دو طرف، پیامدهای متقابل دارد.",
            "افراد پیامدها را با معیار مقایسه می‌سنجند.",
            "وابستگی، قدرت و رضایت را تنظیم می‌کند.",
        ],
        "principles": [
            "گزینه جایگزین، وابستگی را کم می‌کند.",
            "وابستگی کمتر، قدرت بیشتر می‌سازد.",
            "بازتعریف موقعیت، پیامد را تغییر می‌دهد.",
        ],
        "critiques": [
            "۱. آزمایشگاهی: ماتریس‌ها اغلب در آزمایش ساخته شده‌اند.\n۲. ایستایی: رابطه پویا به ماتریس ثابت فروکاسته می‌شود.\n۳. عقلانیت: احساس و تعهد کم‌تر دیده می‌شود.\n۴. فرهنگ: معنای گزینه و پیامد فرهنگی است.\n۵. سنجش: پیامدهای ذهنی سخت اندازه‌گیری می‌شوند.",
        ],
        "applications": [
            "مذاکره رسانه‌ای: شناخت گزینه‌های جایگزین طرفین.",
            "رابطه منبع و خبرنگار: تحلیل وابستگی نامتقارن.",
            "همکاری بحران: ساخت هم‌راستایی منافع.",
            "مدیریت مخاطب: سنجش وفاداری و قدرت چانه‌زنی.",
        ],
        "evolution": "تیبو و کلی در ۱۹۵۹ ماتریس پیامد را عرضه کردند و کلی و تیبو در ۱۹۷۸ نظریه را با بازتعریف موقعیت گستردند. بعدها پژوهش رابطه نزدیک، وابستگی را با دلبستگی و تعهد ترکیب کرد.",
        "key_concepts": [
            "وابستگی متقابل (Interdependence)",
            "ماتریس پیامد (Outcome Matrix)",
            "سطح مقایسه (Comparison Level)",
            "گزینه جایگزین (Comparison Level for Alternatives)",
            "هم‌راستایی منافع (Correspondence of Outcomes)",
            "بازتعریف موقعیت (Transformation of Motivation)",
        ],
        "studies": [
            "Thibaut, J. W., & Kelley, H. H. (1959). The social psychology of groups. Wiley.",
            "Kelley, H. H., & Thibaut, J. W. (1978). Interpersonal relations. Wiley.",
        ],
        "theorists": "جان تیبو؛ هارولد کلی",
        "theorists_text": "تیبو و کلی (۱۹۵۹؛ ۱۹۷۸)",
        "year": 1959,
        "model": "ماتریس پیامد × سطح مقایسه × گزینه جایگزین → وابستگی و قدرت → هماهنگی یا تعارض → بازتعریف موقعیت.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nتیبو و کلی رابطه را ساختار پیامدهای متقابل دیدند و وابستگی را از مقایسه بیرون کشیدند. نوآوری چارچوب، تفکیک ماتریس داده‌شده از اثربخش است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با ماتریس آزمایشی، مقیاس وابستگی و تحلیل گزینه انجام می‌شود. پژوهشی که تنها رضایت را می‌سنجد، گزینه جایگزین را از دست می‌دهد؛ و پژوهشی که ماتریس را ثابت می‌گیرد، بازتعریف را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در تحلیل مذاکره است، اما باید با مطالعه احساس تکمیل شود. وابستگی بی تعهد، به رابطه ابزاری بدل می‌شود.",
        "critique_text": "\n".join([
            "۱. آزمایشگاهی: ماتریس‌ها مصنوعی‌اند.",
            "۲. ایستایی: رابطه پویا ثابت فرض می‌شود.",
            "۳. عقلانیت: احساس کم دیده می‌شود.",
            "۴. فرهنگ: معنای گزینه فرهنگی است.",
            "۵. سنجش: پیامد ذهنی اندازه‌پذیر نیست.",
        ]),
        "example_text": "منبعی که سه رسانه دیگر با او در تماس‌اند، در مصاحبه قدرت بیشتری دارد؛ خبرنگار وابسته‌تر، امتیاز بیشتری می‌دهد و توازن رابطه به سمت منبع می‌رود.",
    },
    "MC-689": {
        "summary": "(بالبی، ۱۹۶۹) نظریه دلبستگی می‌گوید کودک با نظام رفتاری دلبستگی، به مراقب نزدیک می‌ماند تا امنیت بیابد. بالبی دلبستگی را نیازی زیستی و تکاملی دید، نه صرفاً پاسخ به گرسنگی. چهره دلبستگی، پایگاه امنی است که کودک از آن برای کاوش جهان بیرون می‌رود. کودک مدل‌های کاری درونی از خود و دیگری می‌سازد که روابط بعدی را شکل می‌دهد. اینس‌ورث با موقعیت ناآشنا، الگوهای ایمن، اجتنابی و دوسوگرا را شناسایی کرد. بعدها دلبستگی بزرگسال و پیوند آن با رسانه و شخصیت‌های رسانه‌ای بررسی شد.",
        "definition": "دلبستگی، نظام رفتاری تکاملی‌ای است که کودک را در برابر تهدید به جست‌وجوی نزدیکی به چهره دلبستگی وامی‌دارد و از تجربه این رابطه، مدل‌های کاری درونی برای روابط بعدی می‌سازد.",
        "main_problem": "مسئله این است که چرا پیوند عاطفی کودک با مراقب، بر سلامت و روابط آینده اثر می‌گذارد. پاسخ، پایگاه امن و مدل‌های درونی است. پرسش دوم، تعمیم است: آیا الگوهای دلبستگی به روابط بزرگسال، رسانه و پیوند فرااجتماعی گسترش می‌یابند.",
        "mechanism": "۱. نظام دلبستگی: نزدیکی جویی در موقعیت تهدید.\n۲. پایگاه امن: چهره دلبستگی، تکیه‌گاه کاوش می‌شود.\n۳. هم‌آهنگسازی: پاسخ‌دهی حساس مراقب، امنیت می‌سازد.\n۴. مدل کاری درونی: بازنمایی خود و دیگری در رابطه.\n۵. اضطراب جدایی: دوری از چهره دلبستگی، اعتراض و اضطراب می‌سازد.\n۶. تداوم: الگوی رابطه اولیه، انتظارهای رابطه بعدی را شکل می‌دهد.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا مخاطب به شخصیت‌ها و مجریان محبوب دلبسته می‌شود، چرا کودکان به تکرار برنامه آشنا نیاز دارند و چرا اعتماد به رسانه می‌تواند کارکردی شبیه پایگاه امن داشته باشد. دلبستگی فرااجتماعی به چهره رسانه‌ای، نمونه‌ای از تعمیم این نظام است. در رسانه، همین منطق توضیح می‌دهد چرا مخاطب به مجری یا شخصیت آشنا دلبسته می‌شود و چرا قطع ناگهانی این پیوند، واکنشی شبیه اضطراب جدایی برمی‌انگیزد؛ رسانه‌ای که پاسخ‌دهی پیوسته و قابل پیش‌بینی دارد، کارکردی مانند پایگاه امن عاطفی می‌یابد. نکته مهم این است که نظریه، سرنوشت را قطعی نمی‌داند؛ مدل‌های کاری با تجربه‌های بعدی بازبینی می‌شوند.",
        "assumptions": [
            "دلبستگی نیاز تکاملی و زیستی است.",
            "پاسخ حساس مراقب، امنیت می‌سازد.",
            "تجربه دلبستگی، مدل درونی رابطه می‌سازد.",
        ],
        "principles": [
            "پایگاه امن، کاوش را ممکن می‌کند.",
            "مدل کاری، انتظار رابطه را می‌سازد.",
            "الگوی دلبستگی قطعی و تغییرناپذیر نیست.",
        ],
        "critiques": [
            "۱. جبر مادرانه: نقش مراقب اصلی بیش از اندازه تعیین‌کننده دیده می‌شود.\n۲. فرهنگ: الگوی مراقبت در فرهنگ‌ها متفاوت است.\n۳. پایداری: ثبات الگو در طول زندگی قطعی نیست.\n۴. سنجش: طبقه‌بندی دلبستگی به تفسیر وابسته است.\n۵. تعمیم: انتقال به رسانه نیازمند احتیاط است.",
        ],
        "applications": [
            "مخاطب‌شناسی: تحلیل دلبستگی به شخصیت و برند رسانه‌ای.",
            "روان‌شناسی رسانه: دلبستگی فرااجتماعی و امنیت عاطفی.",
            "تربیت رسانه‌ای کودک: نقش تکرار و آشنایی.",
            "اعتماد رسانه: کارکرد پایگاه امن اطلاعاتی.",
        ],
        "evolution": "بالبی در ۱۹۶۹ جلد نخست دلبستگی و فقدان را منتشر کرد و اینس‌ورث در ۱۹۷۸ الگوهای دلبستگی را با موقعیت ناآشنا نشان داد. بعدها دلبستگی بزرگسال، عصب‌شناسی و پژوهش رسانه، چارچوب را گستردند.",
        "key_concepts": [
            "نظام دلبستگی (Attachment System)",
            "پایگاه امن (Secure Base)",
            "مدل کاری درونی (Internal Working Model)",
            "اضطراب جدایی (Separation Anxiety)",
            "هم‌آهنگسازی (Attunement)",
            "دلبستگی فرااجتماعی (Parasocial Attachment)",
        ],
        "studies": [
            "Bowlby, J. (1969). Attachment and loss: Vol. 1. Attachment. Basic Books.",
            "Ainsworth, M. D. S., Blehar, M. C., Waters, E., & Wall, S. (1978). Patterns of attachment. Lawrence Erlbaum.",
        ],
        "theorists": "جان بالبی؛ مری اینس‌ورث",
        "theorists_text": "بالبی (۱۹۶۹)؛ اینس‌ورث (۱۹۷۸)",
        "year": 1969,
        "model": "تهدید → نزدیکی جویی به چهره دلبستگی → پایگاه امن → کاوش → مدل کاری درونی → انتظار رابطه بعدی.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nبالبی دلبستگی را نظام تکاملی دید و آن را از نظریه نیاز دهانی جدا کرد. نوآوری چارچوب، پیوند امنیت عاطفی با کاوش و مدل درونی است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با موقعیت ناآشنا، مصاحبه دلبستگی و مشاهده تعامل انجام می‌شود. پژوهشی که تنها رفتار نزدیکی را می‌سنجد، مدل درونی را از دست می‌دهد؛ و پژوهشی که الگو را سرنوشت قطعی می‌داند، بازبینی را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در تحلیل پیوند عاطفی مخاطب است، اما باید با مطالعه زمینه فرهنگی تکمیل شود. دلبستگی بی مرز، به وابستگی ناسالم بدل می‌شود.",
        "critique_text": "\n".join([
            "۱. جبر مادرانه: نقش مراقب بیش از اندازه تعیین‌کننده است.",
            "۲. فرهنگ: الگوی مراقبت متفاوت است.",
            "۳. پایداری: ثبات الگو قطعی نیست.",
            "۴. سنجش: طبقه‌بندی تفسیری است.",
            "۵. تعمیم: انتقال به رسانه نیازمند احتیاط است.",
        ]),
        "example_text": "کودکی که برنامه کودک آشنایی را هر شب می‌بیند، در آن ثبات و امنیت می‌یابد؛ تغییر ناگهانی مجری، واکنش عاطفی شبیه اضطراب جدایی می‌سازد.",
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
                                       "verified": n_verified, "batch": 108}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH108 THEORY DONE")


if __name__ == "__main__":
    main()
