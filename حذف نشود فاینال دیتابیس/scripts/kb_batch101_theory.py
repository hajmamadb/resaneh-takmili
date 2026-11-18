# -*- coding: utf-8 -*-
"""Batch 101: full documentation for MC-621, MC-622, MC-624, MC-626.

MC-623 (قدرت هیجانی کار / The Emotional Power of Work) is skipped:
empty duplicate of the documented emotional-labor entries MC-394 / MC-509.
"""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch101-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch101_theory.json"

S = {
    "MC-621": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Psychological and Implied Contracts in Organizations",
             title_fa="قراردادهای روان‌شناختی و ضمنی در سازمان‌ها",
             authors="Rousseau, D. M.", year=1989,
             publisher="Employee Responsibilities and Rights Journal",
             doi="10.1007/BF01384942",
             url="https://link.springer.com/article/10.1007/BF01384942",
             language="en", isbn=None,
             citation="Rousseau, D. M. (1989). Psychological and implied contracts in organizations. Employee Responsibilities and Rights Journal, 2(2), 121-139. https://doi.org/10.1007/BF01384942",
             locator="2(2):121-139", locator_type="page_range",
             supports="psychological contract as individual beliefs in reciprocal obligation", verified=True),
        dict(kind="BOOK",
             title_en="Understanding Organizational Behavior",
             title_fa="فهم رفتار سازمانی",
             authors="Argyris, C.", year=1960, publisher="Dorsey Press",
             doi=None, url=None, language="en", isbn=None,
             citation="Argyris, C. (1960). Understanding organizational behavior. Dorsey Press.",
             locator="work", locator_type="work",
             supports="original notion of unwritten psychological work contract", verified=False),
    ],
    "MC-622": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="A Three-Component Conceptualization of Organizational Commitment",
             title_fa="مفهوم‌سازی سه‌مؤلفه‌ای تعهد سازمانی",
             authors="Meyer, J. P.; Allen, N. J.", year=1991,
             publisher="Human Resource Management Review",
             doi=None, url=None, language="en", isbn=None,
             citation="Meyer, J. P., & Allen, N. J. (1991). A three-component conceptualization of organizational commitment. Human Resource Management Review, 1(1), 61-89.",
             locator="1(1):61-89", locator_type="page_range",
             supports="affective, continuance and normative commitment components", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Measurement of Organizational Commitment",
             title_fa="سنجش تعهد سازمانی",
             authors="Mowday, R. T.; Steers, R. M.; Porter, L. W.", year=1979,
             publisher="Journal of Vocational Behavior",
             doi=None, url=None, language="en", isbn=None,
             citation="Mowday, R. T., Steers, R. M., & Porter, L. W. (1979). The measurement of organizational commitment. Journal of Vocational Behavior, 14(2), 224-247.",
             locator="14(2):224-247", locator_type="page_range",
             supports="attitudinal commitment scale antecedent", verified=False),
    ],
    "MC-624": [
        dict(kind="BOOK",
             title_en="Blogs, Wikipedia, Second Life, and Beyond: From Production to Produsage",
             title_fa="وبلاگ‌ها، ویکی‌پدیا، زندگی دوم و فراتر از آن: از تولید به تولیدمصرفی",
             authors="Bruns, A.", year=2008, publisher="Peter Lang",
             doi=None, url="https://produsage.org/book",
             language="en", isbn="978-0-8204-8866-0",
             citation="Bruns, A. (2008). Blogs, Wikipedia, Second Life, and beyond: From production to produsage. Peter Lang.",
             locator="work", locator_type="work",
             supports="four characteristics of produsage / user-led content production", verified=True),
        dict(kind="OTHER",
             title_en="Produsage: Towards a Broader Framework for User-Led Content Creation",
             title_fa="تولیدمصرفی: به سوی چارچوبی گسترده‌تر برای تولید محتوای کاربرمحور",
             authors="Bruns, A.", year=2007, publisher="Proceedings of Creativity and Cognition",
             doi=None, url=None, language="en", isbn=None,
             citation="Bruns, A. (2007). Produsage: Towards a broader framework for user-led content creation. Proceedings of Creativity and Cognition.",
             locator="work", locator_type="work",
             supports="earlier articulation of produsage framework", verified=False),
    ],
    "MC-626": [
        dict(kind="BOOK",
             title_en="The War for Talent",
             title_fa="جنگ بر سر استعداد",
             authors="Michaels, E.; Handfield-Jones, H.; Axelrod, B.", year=2001,
             publisher="Harvard Business School Press",
             doi=None, url="https://hbsp.harvard.edu/product/4592-HBK-ENG",
             language="en", isbn="978-1-57851-459-5",
             citation="Michaels, E., Handfield-Jones, H., & Axelrod, B. (2001). The war for talent. Harvard Business School Press.",
             locator="work", locator_type="work",
             supports="talent mindset / employee value proposition / differentiated talent management", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="The War for Talent",
             title_fa="جنگ بر سر استعداد",
             authors="Chambers, E. G.; Foulon, M.; Handfield-Jones, H.; Hankin, S. M.; Michaels, E. G.", year=1998,
             publisher="McKinsey Quarterly",
             doi=None, url=None, language="en", isbn=None,
             citation="Chambers, E. G., Foulon, M., Handfield-Jones, H., Hankin, S. M., & Michaels, E. G. (1998). The war for talent. McKinsey Quarterly, 3, 44-57.",
             locator="1998(3):44-57", locator_type="page_range",
             supports="survey-based origin of the war-for-talent argument", verified=False),
    ],
}

ENRICH = {
    "MC-621": {
        "summary": "(آرگریس، ۱۹۶۰؛ روسو، ۱۹۸۹) قرارداد روان‌شناختی، باورهای فرد درباره تعهدات دوجانبه میان او و سازمان است؛ تعهداتی که در قرارداد رسمی نوشته نشده‌اند اما رفتار را هدایت می‌کنند. آرگریس این مفهوم را برای توصیف انتظارات نانوشته کارمند و سازمان به کار برد و روسو آن را به باورهای فردی درباره مبادله تقلیل داد. قرارداد روان‌شناختی دو گونه اصلی دارد: تبادلی با مبادله کوتاه‌مدت و مشخص، و رابطه‌ای با تعهد بلندمدت و نامشخص. نقض این قرارداد، بی‌اعتمادی و کاهش تعهد می‌سازد.",
        "definition": "قرارداد روان‌شناختی، مجموعه باورهای فرد درباره تعهدات متقابل او و سازمان است؛ باورهایی که از وعده‌ها و تجربه شکل می‌گیرند و خارج از قرارداد رسمی، انتظارات و رفتار طرفین را تنظیم می‌کنند.",
        "main_problem": "مسئله این است که چرا کارکنان با وجود قرارداد رسمی مشابه، احساس بی‌عدالتی یا خیانت می‌کنند. پاسخ در انتظارات نانوشته است. پرسش دوم، مدیریت است: سازمان چگونه می‌تواند تعهدات ضمنی را روشن کند بی آنکه انعطاف مدیریتی را از دست بدهد.",
        "mechanism": "۱. وعده و انتظار: پیام‌های آشکار و ضمنی سازمان، انتظار آینده را در کارمند می‌سازد.\n۲. باور دوجانبه: کارمند تعهد خود و تعهد سازمان را در ذهن تراز می‌کند؛ این تراز، مبنای داوری عدالت است.\n۳. گونه تبادلی: مبادله محدود، مشخص و کوتاه‌مدت؛ وفاداری تابع پاداش فوری است.\n۴. گونه رابطه‌ای: تعهد بلندمدت، انعطاف و اعتماد متقابل؛ کارمند در برابر امنیت، وفاداری می‌دهد.\n۵. نقض قرارداد: وقتی سازمان به تعهد ادراک‌شده عمل نکند، احساس بی‌عدالتی و خشم شکل می‌گیرد.\n۶. بازسازی: گفت‌وگوی صریح، بازتعریف انتظارات و عمل به وعده‌ها، قرارداد را ترمیم می‌کند.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا خبرنگاران در ادغام رسانه‌ها احساس خیانت می‌کنند، چرا وعده «امنیت شغلی» در برابر «انعطاف» سنجیده می‌شود و چرا روابط پلتفرم با سازندگان محتوا شکننده است. قرارداد روان‌شناختی در کار رسانه‌ای بیشتر رابطه‌ای است تا تبادلی؛ اما وقتی سازمان تنها پاداش کوتاه‌مدت می‌دهد، انتظار بلندمدت به سرخوردگی می‌رسد. نکته مهم این است که قرارداد روان‌شناختی در ذهن کارمند ساخته می‌شود، نه در سند؛ بنابراین مدیریت آن نیازمند گوش دادن و شفافیت است.",
        "assumptions": [
            "انتظارات نانوشته، رفتار را هدایت می‌کنند.",
            "قرارداد در ذهن فرد ساخته می‌شود نه در سند.",
            "نقض تعهد ادراک‌شده، واکنش عاطفی می‌سازد.",
        ],
        "principles": [
            "وعده ضمنی هم تعهد است.",
            "شفافیت، هزینه نقض را کم می‌کند.",
            "قرارداد تبادلی و رابطه‌ای، مدیریت متفاوت می‌خواهند.",
        ],
        "critiques": [
            "۱. ابهام مفهومی: مرز قرارداد روان‌شناختی و انتظار شغلی روشن نیست.\n۲. سنجش: باور ذهنی، سخت اندازه‌گیری و مقایسه‌پذیر است.\n۳. تمرکز فردی: نقش ساختار و قدرت سازمانی کم دیده می‌شود.\n۴. تغییر زمینه: کار پلتفرمی، قرارداد بلندمدت را کم‌رنگ کرده است.\n۵. خطر تفسیر: هر نارضایتی می‌تواند نقض قرارداد خوانده شود.",
        ],
        "applications": [
            "مدیریت تغییر رسانه‌ای: مدیریت انتظارات در ادغام و بازسازی.",
            "نگهداشت خبرنگار: روشن‌کردن وعده‌های رشد و امنیت.",
            "روابط با سازندگان محتوا: شفاف‌سازی قواعد درآمد و مالکیت.",
            "پژوهش سازمانی: تحلیل اعتماد در محیط کار.",
        ],
        "evolution": "آرگریس در ۱۹۶۰ مفهوم قرارداد روان‌شناختی را برای انتظارات نانوشته به کار برد؛ لوینسون و همکاران در ۱۹۶۲ آن را بسط دادند و روسو در ۱۹۸۹ با تعریف باورهای فردی درباره تعهد متقابل، مفهوم را عملیاتی کرد. بعدها پژوهش نقض قرارداد و قراردادهای تبادلی و رابطه‌ای، این چارچوب را به مدیریت منابع انسانی و ارتباطات سازمانی گستراند.",
        "key_concepts": [
            "قرارداد روان‌شناختی (Psychological Contract)",
            "تعهد متقابل (Reciprocal Obligation)",
            "قرارداد تبادلی (Transactional Contract)",
            "قرارداد رابطه‌ای (Relational Contract)",
            "نقض قرارداد (Contract Breach)",
            "اعتماد سازمانی (Organizational Trust)",
        ],
        "studies": [
            "Argyris, C. (1960). Understanding organizational behavior. Dorsey Press.",
            "Rousseau, D. M. (1989). Psychological and implied contracts in organizations. Employee Responsibilities and Rights Journal, 2(2), 121-139.",
        ],
        "theorists": "کریس آرگریس؛ دنیس روسو",
        "theorists_text": "آرگریس (۱۹۶۰)؛ روسو (۱۹۸۹)",
        "year": 1960,
        "model": "وعده‌ها و تجربه → باور به تعهد دوجانبه (تبادلی یا رابطه‌ای) → داوری عدالت → تعهد یا نقض و بی‌اعتمادی.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nآرگریس انتظارات نانوشته را وارد تحلیل سازمان کرد و روسو آن را به باور فردی درباره مبادله محدود ساخت. نوآوری چارچوب، توضیح واکنش عاطفی کارکنان به وعده‌های نشده است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با تحلیل محتوای وعده‌ها، پرسش‌نامه تعهد ادراک‌شده و رویداد نقض انجام می‌شود. پژوهشی که تنها رضایت را می‌سنجد، منشأ بی‌اعتمادی را از دست می‌دهد؛ و پژوهشی که هر انتظار را تعهد می‌خواند، مفهوم را تورم می‌دهد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در تحلیل ادغام و بازسازی رسانه است، اما باید با تحلیل ساختار تکمیل شود. قرارداد روان‌شناختی بی قدرت چانه‌زنی، به انتظار بی‌پاسخ بدل می‌شود.",
        "critique_text": "\n".join([
            "۱. ابهام مفهومی: مرز با انتظار شغلی روشن نیست.",
            "۲. سنجش: باور ذهنی سخت اندازه‌گیری می‌شود.",
            "۳. تمرکز فردی: ساختار و قدرت کم دیده می‌شود.",
            "۴. تغییر زمینه: کار پلتفرمی قرارداد بلندمدت را کم‌رنگ کرد.",
            "۵. خطر تفسیر: هر نارضایتی نقض قرارداد خوانده می‌شود.",
        ]),
        "example_text": "سازمانی در مصاحبه وعده رشد می‌دهد اما پس از ادغام مسیر ارتقا را می‌بندد؛ کارکنان با وجود حفظ حقوق، وعده شکسته را نقض قرارداد می‌خوانند و تعهد عاطفی آن‌ها افت می‌کند.",
    },
    "MC-622": {
        "summary": "(مایر و آلن، ۱۹۹۱) تعهد سازمانی، پیوند روانی کارمند با سازمان است و سه مؤلفه دارد: عاطفی (دلبستگی و همانندی)، مستمر (هزینه ترک) و هنجاری (احساس وظیفه). مایر و آلن نشان دادند این سه مؤلفه پیشایندها و پیامدهای متفاوت دارند: تعهد عاطفی با رضایت و رفتار شهروندی، تعهد مستمر با ماندن اجباری و تعهد هنجاری با احساس دِین پیوند دارد. تعهد، تنها ماندن در سازمان نیست؛ کیفیت رابطه است. مدل، ابزار سنجش و تحلیل نگهداشت نیروی انسانی را دگرگون کرد.",
        "definition": "تعهد سازمانی، پیوند روانی کارمند با سازمان است که در سه مؤلفه عاطفی، مستمر و هنجاری نمود می‌یابد و احتمال ماندن، تلاش و پذیرش ارزش‌های سازمان را توضیح می‌دهد.",
        "main_problem": "مسئله این است که چرا برخی کارکنان می‌مانند و می‌کوشند و برخی تنها حضور فیزیکی دارند. پاسخ، نوع تعهد است نه مقدار آن. پرسش دوم، مدیریت است: کدام نوع تعهد به عملکرد و خلاقیت می‌انجامد و کدام به ماندن اجباری.",
        "mechanism": "۱. تعهد عاطفی: دلبستگی احساسی، همانندی با ارزش‌ها و لذت عضویت.\n۲. تعهد مستمر: آگاهی از هزینه ترک؛ حقوق، ارشدیت و نبود جایگزین، ماندن را اجباری می‌کند.\n۳. تعهد هنجاری: احساس وظیفه و دِین اخلاقی به سازمان.\n۴. پیشایندهای متفاوت: تجربه کاری و حمایت سازمانی تعهد عاطفی می‌سازد؛ سرمایه‌گذاری و جایگزین‌ها تعهد مستمر؛ جامعه‌پذیری تعهد هنجاری.\n۵. پیامدهای متفاوت: تعهد عاطفی با تلاش و رفتار شهروندی، تعهد مستمر با ماندن کم‌هزینه و کم‌اشتیاق.\n۶. سنجش سه‌گانه: پرسش‌نامه‌های جداگانه هر مؤلفه را می‌سنجند و نمره کل را جایگزین نمی‌کنند.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا تحریریه‌ای با تعهد عاطفی بالا، کار تحقیقی سنگین را می‌پذیرد و چرا سازمانی که تنها با حقوق و ارشدیت نگه می‌دارد، خبرنگار فرسوده را حفظ می‌کند بی آنکه خلاقیت را حفظ کند. تعهد هنجاری در رسانه‌های خانوادگی و نهادی وزن بیشتری دارد. نکته مهم این است که ماندن بی تعهد عاطفی، هزینه پنهان سازمان است؛ سازمان می‌ماند اما خلاقیت نمی‌ماند.",
        "assumptions": [
            "تعهد، سازه‌ای چندبعدی است.",
            "سه مؤلفه پیشایند و پیامد متفاوت دارند.",
            "تعهد قابل سنجش و مدیریت است.",
        ],
        "principles": [
            "ماندن، معادل تعهد نیست.",
            "تعهد عاطفی، عملکرد و خلاقیت می‌سازد.",
            "تعهد مستمر، ماندن اجباری است.",
        ],
        "critiques": [
            "۱. هم‌پوشانی: سه مؤلفه در عمل همبستگی بالایی دارند.\n۲. سوگیری نمونه: بیشتر شواهد از آمریکای شمالی است.\n۳. سنجش خودگزارشی: تعهد وابسته به تفسیر فرد است.\n۴. زمینه: کار پروژه‌ای و پلتفرمی، معنای ماندن را تغییر داده است.\n۵. کم‌توجهی به سطح: تعهد به تیم و حرفه از تعهد به سازمان جدا می‌شود.",
        ],
        "applications": [
            "نگهداشت نیروی انسانی: تقویت تعهد عاطفی با حمایت و رشد.",
            "مدیریت تحریریه: تفکیک ماندن اجباری از دلبستگی حرفه‌ای.",
            "مدیریت تغییر: کاهش تعهد مستمر وابسته به ترس.",
            "پژوهش سازمانی: سنجش سه‌گانه تعهد در رسانه.",
        ],
        "evolution": "مودی، استیرز و پورتر در ۱۹۷۹ تعهد را با دلبستگی و تمایل به تلاش سنجیدند؛ مایر و آلن در ۱۹۹۱ مدل سه‌گانه را عرضه کردند و در ۱۹۹۷ ابزار و شواهد آن را گستردند. این مدل به پژوهش نگهداشت، رفتار شهروندی و مدیریت تغییر راه یافت.",
        "key_concepts": [
            "تعهد عاطفی (Affective Commitment)",
            "تعهد مستمر (Continuance Commitment)",
            "تعهد هنجاری (Normative Commitment)",
            "رفتار شهروندی سازمانی (Organizational Citizenship Behavior)",
            "نگهداشت کارمند (Employee Retention)",
            "دلبستگی سازمانی (Organizational Attachment)",
        ],
        "studies": [
            "Meyer, J. P., & Allen, N. J. (1991). A three-component conceptualization of organizational commitment. Human Resource Management Review, 1(1), 61-89.",
            "Mowday, R. T., Steers, R. M., & Porter, L. W. (1979). The measurement of organizational commitment. Journal of Vocational Behavior, 14(2), 224-247.",
        ],
        "theorists": "جان مایر؛ ناتالی آلن",
        "theorists_text": "مایر و آلن (۱۹۹۱)",
        "year": 1991,
        "model": "سه مؤلفه تعهد: عاطفی (دلبستگی) + مستمر (هزینه ترک) + هنجاری (وظیفه) → ماندن، تلاش و پذیرش ارزش‌ها.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nمایر و آلن تعهد را از یک نگرش کلی به سه سازه با منطق روانی متفاوت تفکیک کردند. نوآوری چارچوب، توضیح ماندن بی دلبستگی و دلبستگی بی محاسبه است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با سه مقیاس جداگانه و تحلیل پیشایند و پیامد انجام می‌شود. پژوهشی که نمره کل را می‌سنجد، نوع تعهد را از دست می‌دهد؛ و پژوهشی که تنها ماندن را می‌سنجد، تعهد عاطفی را با اجباری اشتباه می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در تحلیل نگهداشت تحریریه است، اما باید با تحلیل بازار کار تکمیل شود. تعهد مستمر در بازار بی‌جایگزین، ماندن را حفظ می‌کند اما خلاقیت را نه.",
        "critique_text": "\n".join([
            "۱. هم‌پوشانی: سه مؤلفه همبستگی بالایی دارند.",
            "۲. سوگیری نمونه: شواهد از آمریکای شمالی است.",
            "۳. سنجش: خودگزارشی وابسته به تفسیر است.",
            "۴. زمینه: کار پلتفرمی معنای ماندن را تغییر داد.",
            "۵. سطح تحلیل: تعهد به تیم و حرفه جدا می‌شود.",
        ]),
        "example_text": "خبرنگاری با وجود پیشنهاد بهتر می‌ماند چون ارشدیت و مزایای او وابسته به سابقه است؛ تعهد مستمر او را نگه داشته اما انگیزه تحقیق را نکشته است. همکار جوانی با تعهد عاطفی بالا، پروژه سنگین را داوطلبانه می‌پذیرد.",
    },
    "MC-624": {
        "summary": "(برونز، ۲۰۰۸) تولیدمصرفی، وضعیتی است که در آن مصرف‌کننده هم‌زمان تولیدکننده است و مرز میان تولید و مصرف محتوا فرو می‌ریزد. برونز این مفهوم را برای توصیف ویکی‌پدیا، وبلاگ‌ها، نرم‌افزار آزاد و اجتماعات آنلاین ساخت. تولیدمصرفی چهار ویژگی دارد: مشارکت باز و ارزیابی همگانی، سلسله‌مراتب سیال، محصول ناتمام و مالکیت مشترک. در این چارچوب، محتوا محصولی نیست که یک بار ساخته و فروخته شود، بلکه فرایندی است که پیوسته بازنگری می‌شود. مدل، اقتصاد و اخلاق کار دیجیتال را به بحث کشید.",
        "definition": "تولیدمصرفی، چارچوبی است که در آن کاربران به‌طور هم‌زمان مصرف‌کننده و تولیدکننده محتوا هستند و تولید، فرایندی باز، مشارکتی، ناتمام و متعلق به جمع است.",
        "main_problem": "مسئله این است که مدل تولید صنعتی، کاربر مشارکت‌کننده را توضیح نمی‌دهد. پاسخ، تغییر منطق تولید است. پرسش دوم، ارزش است: وقتی کاربران آزادانه تولید می‌کنند، ارزش اقتصادی چگونه توزیع می‌شود و مرز بهره‌کشی کجاست.",
        "mechanism": "۱. مشارکت باز: هر کسی می‌تواند وارد تولید شود و سد ورود پایین است.\n۲. ارزیابی همگانی: کیفیت با داوری جمعی و ویرایش متقابل سنجیده می‌شود، نه تنها با بازار.\n۳. سلسله‌مراتب سیال: جایگاه فرد با مشارکت و شایستگی جابه‌جا می‌شود و ثابت نیست.\n۴. محصول ناتمام: محتوا همیشه در حال بازنگری است و نسخه نهایی وجود ندارد.\n۵. مالکیت مشترک: محصول به جمع تعلق دارد و حق استفاده و تغییر گسترده است.\n۶. مدل اقتصادی: ارزش از مشارکت جمعی می‌آید و پرسش توزیع آن، کانون نقد است.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا ویکی‌پدیا بی سازمان رسمی دوام می‌آورد، چرا مخاطب خبر به هم‌تولیدکننده بدل می‌شود و چرا پلتفرم‌ها بر کار کاربر تکیه می‌کنند. کیفیت مدخل‌ها نیز به هنجارهای اجتماع ویرایشگر وابسته است، نه به بازار. نکته مهم این است که تولیدمصرفی بهره‌کشی را حذف نمی‌کند؛ اگر مالکیت و پاداش روشن نباشد، مشارکت آزاد به کار مجانی بدل می‌شود.",
        "assumptions": [
            "مرز تولید و مصرف فرو ریخته است.",
            "کیفیت با داوری جمعی قابل مدیریت است.",
            "مالکیت مشترک، انگیزه مشارکت را می‌سازد.",
        ],
        "principles": [
            "مشارکت باز، نوآوری را زیاد می‌کند.",
            "محصول ناتمام، بازنگری را ممکن می‌کند.",
            "مالکیت جمعی، مشروعیت می‌سازد.",
        ],
        "critiques": [
            "۱. آرمان‌گرایی: مالکیت مشترک در پلتفرم‌های تجاری محقق نمی‌شود.\n۲. کیفیت: داوری جمعی می‌تواند به حاکمیت اکثریت یا خرابکاری بیانجامد.\n۳. کار مجانی: ارزش کاربر به سود پلتفرم منتقل می‌شود.\n۴. دسترسی: مشارکت برابر نیست و شکاف مهارت باقی می‌ماند.\n۵. تعریف: مرز تولیدمصرفی و هم‌آفرینی مبهم است.",
        ],
        "applications": [
            "تحلیل ویکی‌پدیا: کیفیت و حکمرانی اجتماع تولید.",
            "رسانه مشارکتی: طراحی مشارکت مخاطب و بازنگری.",
            "سیاست پلتفرم: شفاف‌سازی مالکیت و پاداش کار کاربر.",
            "آموزش رسانه: تحلیل هم‌تولیدی محتوا.",
        ],
        "evolution": "برونز مفهوم را در دهه ۲۰۰۰ در مقاله‌هایی درباره تولید کاربرمحور ساخت و در ۲۰۰۸ در کتابی درباره وبلاگ، ویکی‌پدیا و جهان‌های مجازی نظام‌مند کرد. این چارچوب به پژوهش کار دیجیتال، هم‌آفرینی و حکمرانی پلتفرم راه یافت و با نقد کار مجانی و بهره‌کشی الگوریتمی روبه‌رو شد.",
        "key_concepts": [
            "تولیدمصرفی (Produsage)",
            "هم‌آفرینی (Co-creation)",
            "مشارکت باز (Open Participation)",
            "مالکیت مشترک (Common Property)",
            "سلسله‌مراتب سیال (Fluid Heterarchy)",
            "کار دیجیتال (Digital Labor)",
        ],
        "studies": [
            "Bruns, A. (2008). Blogs, Wikipedia, Second Life, and beyond: From production to produsage. Peter Lang.",
            "Bruns, A. (2007). Produsage: Towards a broader framework for user-led content creation. Proceedings of Creativity and Cognition.",
        ],
        "theorists": "اکسل برونز",
        "theorists_text": "اکسل برونز (۲۰۰۸)",
        "year": 2008,
        "model": "مشارکت باز + ارزیابی همگانی + سلسله‌مراتب سیال + محصول ناتمام + مالکیت مشترک → تولید کاربرمحور؛ با پرسش توزیع ارزش.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nبرونز تولید محتوا را از خط مونتاژ صنعتی به فرایند مشارکتی و پیوسته منتقل کرد. نوآوری چارچوب، تفکیک تولیدمصرفی از مصرف منفعل و از تولید حرفه‌ای است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با تحلیل تاریخ ویرایش، ساختار اجتماع و کیفیت محصول انجام می‌شود. پژوهشی که تنها حجم مشارکت را می‌سنجد، کیفیت را از دست می‌دهد؛ و پژوهشی که مالکیت پلتفرم را نمی‌بیند، بهره‌کشی کار کاربر را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در توضیح رسانه مشارکتی است، اما باید با تحلیل اقتصاد سیاسی رسانه تکمیل شود. مشارکت آزاد بی پاداش، پایدار نمی‌ماند.",
        "critique_text": "\n".join([
            "۱. آرمان‌گرایی: مالکیت مشترک در پلتفرم تجاری محقق نمی‌شود.",
            "۲. کیفیت: داوری جمعی به حاکمیت اکثریت می‌انجامد.",
            "۳. کار مجانی: ارزش کاربر به سود پلتفرم می‌رود.",
            "۴. دسترسی: مشارکت برابر نیست.",
            "۵. تعریف: مرز با هم‌آفرینی مبهم است.",
        ]),
        "example_text": "کاربران ویکی‌پدیا مقاله را می‌نویسند، ویرایش می‌کنند و بی مزد منتشر می‌سازند؛ همان مقاله در موتور جست‌وجو به ارزش تجاری بدل می‌شود. تولیدمصرفی، مشارکت را توضیح می‌دهد و پرسش توزیع ارزش را باقی می‌گذارد.",
    },
    "MC-626": {
        "summary": "(مایکلز، هندفیلد-جونز و اکسلراد، ۲۰۰۱) مدیریت استعداد، رویکردی است که جذب، توسعه و نگهداشت افراد با عملکرد بالا را به راهبرد سازمان گره می‌زند. این رویکرد از مطالعه مشاوره‌ای اواخر دهه ۱۹۹۰ برخاست و استدلال کرد که مزیت رقابتی به ذهنیت استعداد مدیران، پیشنهاد ارزش کارمند، برنامه توسعه و تمایز عملکرد وابسته است. مدل، بازار کار استعداد را رقابتی و مجموع صفر می‌بیند. مدیریت استعداد به سیاست‌های جذب، ارزیابی، جانشین‌پروری و نگهداشت راه یافت.",
        "definition": "مدیریت استعداد، مجموعه سیاست‌ها و رویه‌هایی است که جذب، توسعه، ارزیابی و نگهداشت افراد با توان بالا را برای دستیابی به اهداف راهبردی سازمان هماهنگ می‌کند.",
        "main_problem": "مسئله این است که چرا سازمان‌ها با وجود بازار کار پر از نیروی جویای کار، برای نقش‌های کلیدی کمبود استعداد دارند. پاسخ، تفاوت عملکرد و رقابت بر سر گروه کوچکی از افراد است. پرسش دوم، عدالت است: تمایزگذاری میان کارکنان چه زمانی به انگیزش و چه زمانی به بی‌اعتمادی می‌انجامد.",
        "mechanism": "۱. ذهنیت استعداد: مدیران استعداد را اولویت راهبردی می‌دانند، نه وظیفه واحد منابع انسانی.\n۲. پیشنهاد ارزش کارمند: بسته حقوق، رشد، فرهنگ و معنا برای جذب و نگهداشت طراحی می‌شود.\n۳. جذب هدفمند: شناسایی و جذب افراد با عملکرد بالا در بازار رقابتی.\n۴. توسعه و جانشین‌پروری: آموزش، چرخش شغلی و مسیر جانشینی برای نقش‌های کلیدی.\n۵. تمایز عملکرد: تفکیک افراد بر پایه عملکرد و پاداش متناسب.\n۶. نگهداشت: شناخت محرک‌های ماندن و کاهش ریسک ترک افراد کلیدی.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا سازمان‌های رسانه‌ای بر جذب ستاره‌ها و روزنامه‌نگاران برجسته رقابت می‌کنند، چرا برنامه جانشین‌پروری برای سردبیری حیاتی است و چرا تمایز بی‌ضابطه، تیم را به رقابت مخرب می‌برد. نکته مهم این است که استعداد یک برسازه است؛ هر تعریفی از آن، چه کسی را شامل و چه کسی را حذف می‌کند.",
        "assumptions": [
            "عملکرد افراد به‌طور معنادار متفاوت است.",
            "استعداد کمیاب و رقابتی است.",
            "مدیریت فعال استعداد، عملکرد سازمان را بالا می‌برد.",
        ],
        "principles": [
            "استعداد، اولویت راهبردی است.",
            "پیشنهاد ارزش، شرط جذب است.",
            "نگهداشت، ارزان‌تر از جایگزینی است.",
        ],
        "critiques": [
            "۱. شواهد: پیوند مدیریت استعداد و عملکرد سازمانی یکدست نیست.\n۲. نخبه‌گرایی: برچسب استعداد، دیگران را بی‌انگیزه می‌کند.\n۳. مجموع صفر: فرض کمیابی، رقابت مخرب می‌سازد.\n۴. تعریف: استعداد اغلب با عملکرد گذشته یا شبکه غیررسمی سنجیده می‌شود.\n۵. تناقض: برنامه استعداد با اخراج‌های گسترده هم‌زمان شده است.",
        ],
        "applications": [
            "مدیریت رسانه: جانشین‌پروری برای نقش‌های سردبیری.",
            "جذب حرفه‌ای: طراحی پیشنهاد ارزش برای خبرنگاران.",
            "توسعه: برنامه رشد متناسب با عملکرد.",
            "پژوهش سازمانی: تحلیل عدالت در تمایز کارکنان.",
        ],
        "evolution": "ریشه اصطلاح به مطالعه مشاوره‌ای اواخر دهه ۱۹۹۰ و مقاله ۱۹۹۸ بازمی‌گردد و در ۲۰۰۱ در کتابی درباره رقابت بر سر استعداد نظام‌مند شد. بعدها نقد نخبه‌گرایی و شواهد ضعیف، پژوهش را به سمت مدیریت استعداد فراگیر و تحلیل داده نیروی انسانی برد.",
        "key_concepts": [
            "مدیریت استعداد (Talent Management)",
            "ذهنیت استعداد (Talent Mindset)",
            "پیشنهاد ارزش کارمند (Employee Value Proposition)",
            "جانشین‌پروری (Succession Planning)",
            "تمایز عملکرد (Performance Differentiation)",
            "نگهداشت استعداد (Talent Retention)",
        ],
        "studies": [
            "Michaels, E., Handfield-Jones, H., & Axelrod, B. (2001). The war for talent. Harvard Business School Press.",
            "Chambers, E. G., Foulon, M., Handfield-Jones, H., Hankin, S. M., & Michaels, E. G. (1998). The war for talent. McKinsey Quarterly, 3, 44-57.",
        ],
        "theorists": "اد مایکلز؛ هلن هندفیلد-جونز؛ بث اکسلراد",
        "theorists_text": "مایکلز، هندفیلد-جونز و اکسلراد (۲۰۰۱)",
        "year": 2001,
        "model": "ذهنیت استعداد + پیشنهاد ارزش + جذب + توسعه + تمایز + نگهداشت → عملکرد سازمانی؛ با خطر نخبه‌گرایی و رقابت مخرب.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nمدیریت استعداد، عملکرد سازمان را به کیفیت نیروی انسانی کلیدی گره زد و آن را از وظیفه اداری به راهبرد ارتقا داد. نوآوری چارچوب، تبدیل استعداد از ویژگی فردی به سازوکار مدیریتی است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با ارزیابی عملکرد، تحلیل مسیر جانشینی و شاخص نگهداشت انجام می‌شود. پژوهشی که تنها عملکرد گذشته را می‌سنجد، توان آینده را از دست می‌دهد؛ و پژوهشی که تمایز را بی معیار شفاف می‌سنجد، سوگیری شبکه را وارد تصمیم می‌کند.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در طراحی جانشینی تحریریه است، اما باید با تحلیل عدالت تکمیل شود. تمایز بی‌ضابطه، اعتماد تیم را از بین می‌برد و همکاری را به رقابت مخرب بدل می‌کند.",
        "critique_text": "\n".join([
            "۱. شواهد: پیوند با عملکرد سازمانی یکدست نیست.",
            "۲. نخبه‌گرایی: برچسب استعداد دیگران را بی‌انگیزه می‌کند.",
            "۳. مجموع صفر: فرض کمیابی رقابت مخرب می‌سازد.",
            "۴. تعریف: استعداد با شبکه غیررسمی سنجیده می‌شود.",
            "۵. تناقض: برنامه استعداد با اخراج هم‌زمان شده است.",
        ]),
        "example_text": "سازمان رسانه‌ای برای سردبیری آینده برنامه جانشین‌پروری می‌سازد و دو دبیر را در پروژه‌های راهبردی می‌گمارد؛ اما اگر انتخاب تنها بر پایه آشنایی مدیر باشد، برنامه به بازتولید شبکه غیررسمی بدل می‌شود.",
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
                                       "verified": n_verified, "batch": 101}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH101 THEORY DONE")


if __name__ == "__main__":
    main()
