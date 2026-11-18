# -*- coding: utf-8 -*-
"""Batch 102: full documentation for MC-628, MC-629, MC-632, MC-633.

MC-625 (Precarious Creative Work Theory) is skipped: duplicate of MC-510.
"""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch102-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch102_theory.json"

S = {
    "MC-628": [
        dict(kind="BOOK",
             title_en="The Knowledge-Creating Company: How Japanese Companies Create the Dynamics of Innovation",
             title_fa="شرکت دانش‌آفرین: چگونه شرکت‌های ژاپنی پویایی نوآوری را می‌سازند",
             authors="Nonaka, I.; Takeuchi, H.", year=1995, publisher="Oxford University Press",
             doi=None, url="https://global.oup.com/academic/product/the-knowledge-creating-company-9780195092691",
             language="en", isbn="9780195092691",
             citation="Nonaka, I., & Takeuchi, H. (1995). The knowledge-creating company: How Japanese companies create the dynamics of innovation. Oxford University Press.",
             locator="work", locator_type="work",
             supports="tacit-explicit knowledge conversion / four modes / knowledge spiral", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="A Dynamic Theory of Organizational Knowledge Creation",
             title_fa="نظریه‌ای پویا درباره آفرینش دانش سازمانی",
             authors="Nonaka, I.", year=1994, publisher="Organization Science",
             doi=None, url=None, language="en", isbn=None,
             citation="Nonaka, I. (1994). A dynamic theory of organizational knowledge creation. Organization Science, 5(1), 14-37.",
             locator="5(1):14-37", locator_type="page_range",
             supports="organizational knowledge creation theory antecedent", verified=False),
    ],
    "MC-629": [
        dict(kind="BOOK",
             title_en="The Fifth Discipline: The Art and Practice of the Learning Organization",
             title_fa="انضباط پنجم: هنر و عمل سازمان یادگیرنده",
             authors="Senge, P. M.", year=1990, publisher="Doubleday/Currency",
             doi=None, url=None, language="en", isbn=None,
             citation="Senge, P. M. (1990). The fifth discipline: The art and practice of the learning organization. Doubleday/Currency.",
             locator="work", locator_type="work",
             supports="five disciplines / systems thinking as fifth discipline", verified=True),
        dict(kind="BOOK",
             title_en="Organizational Learning: A Theory of Action Perspective",
             title_fa="یادگیری سازمانی: چشم‌اندازی نظریه کنش",
             authors="Argyris, C.; Schön, D. A.", year=1978, publisher="Addison-Wesley",
             doi=None, url=None, language="en", isbn=None,
             citation="Argyris, C., & Schön, D. A. (1978). Organizational learning: A theory of action perspective. Addison-Wesley.",
             locator="work", locator_type="work",
             supports="single-loop and double-loop learning antecedent", verified=False),
    ],
    "MC-632": [
        dict(kind="BOOK",
             title_en="Leadership and Performance Beyond Expectations",
             title_fa="رهبری و عملکرد فراتر از انتظار",
             authors="Bass, B. M.", year=1985, publisher="Free Press",
             doi=None, url="https://archive.org/details/leadershipperfor0000bass",
             language="en", isbn=None,
             citation="Bass, B. M. (1985). Leadership and performance beyond expectations. Free Press.",
             locator="work", locator_type="work",
             supports="transformational and transactional leadership / four transformational components", verified=True),
        dict(kind="BOOK",
             title_en="Leadership",
             title_fa="رهبری",
             authors="Burns, J. M.", year=1978, publisher="Harper & Row",
             doi=None, url=None, language="en", isbn=None,
             citation="Burns, J. M. (1978). Leadership. Harper & Row.",
             locator="work", locator_type="work",
             supports="transformational vs transactional leadership distinction", verified=False),
    ],
    "MC-633": [
        dict(kind="BOOK",
             title_en="Management of Organizational Behavior: Utilizing Human Resources",
             title_fa="مدیریت رفتار سازمانی: بهره‌گیری از منابع انسانی",
             authors="Hersey, P.; Blanchard, K. H.", year=1969, publisher="Prentice-Hall",
             doi=None, url=None, language="en", isbn=None,
             citation="Hersey, P., & Blanchard, K. H. (1969). Management of organizational behavior: Utilizing human resources. Prentice-Hall.",
             locator="work", locator_type="work",
             supports="situational leadership / task and relationship behavior / follower readiness", verified=True),
        dict(kind="BOOK",
             title_en="Management of Organizational Behavior: Leading Human Resources",
             title_fa="مدیریت رفتار سازمانی: رهبری منابع انسانی",
             authors="Hersey, P.; Blanchard, K. H.; Johnson, D. E.", year=2008, publisher="Prentice Hall",
             doi=None, url=None, language="en", isbn=None,
             citation="Hersey, P., Blanchard, K. H., & Johnson, D. E. (2008). Management of organizational behavior: Leading human resources (9th ed.). Prentice Hall.",
             locator="work", locator_type="work",
             supports="later refinement of situational leadership model", verified=False),
    ],
}

ENRICH = {
    "MC-628": {
        "summary": "(نوناکا و تاکوچی، ۱۹۹۵) مدیریت دانش، رویکردی است که دانش را منبع اصلی مزیت رقابتی می‌داند و چرخه تبدیل دانش پنهان و آشکار را سازمان می‌دهد. نوناکا چهار حالت تبدیل را تفکیک کرد: اجتماعی‌سازی، بیرونی‌سازی، ترکیب و درونی‌سازی. دانش پنهان در تجربه و مهارت افراد است و دانش آشکار در سند و قاعده. سازمان دانش‌آفرین با فراهم کردن زمینه مشترک، این تبدیل را ممکن می‌کند. مدیریت دانش، فناوری اطلاعات نیست؛ طراحی اجتماع و فرایند است.",
        "definition": "مدیریت دانش، مجموعه رویه‌هایی است که خلق، تبدیل، ذخیره، انتقال و کاربرد دانش سازمانی را برای بهبود تصمیم و نوآوری هماهنگ می‌کند و بر تبدیل دانش پنهان و آشکار استوار است.",
        "main_problem": "مسئله این است که سازمان‌ها دانش زیادی دارند اما آن را از دست می‌دهند. پاسخ، دانش پنهان بی تبدیل است که با ترک کارمند می‌رود. پرسش دوم، مرز فناوری و اجتماع است: سامانه بی فرهنگ مشارکت، انبار سند می‌شود نه دانش.",
        "mechanism": "۱. دانش پنهان: تجربه، شهود و مهارت که در ذهن و عمل افراد جای دارد و به‌سختی نوشته می‌شود.\n۲. دانش آشکار: دانش کدگذاری‌شده در سند، قاعده و پایگاه داده که انتقال آن آسان است.\n۳. اجتماعی‌سازی: انتقال دانش پنهان با مشاهده، همراهی و همکاری در زمینه مشترک.\n۴. بیرونی‌سازی: تبدیل دانش پنهان به مفهوم آشکار با استعاره، مدل و روایت.\n۵. ترکیب: بازآرایی دانش آشکار موجود به شکل تازه و نظام‌مند.\n۶. درونی‌سازی: یادگیری دانش آشکار و تبدیل آن به مهارت پنهان در عمل.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا قضاوت تحریریه‌ای با بازنشستگی سردبیر قدیمی از دست می‌رود، چرا آموزش خبرنگار تازه‌کار با همراهی دبیر مؤثرتر از خواندن آیین‌نامه است و چرا آرشیو بی روایت، قابل استفاده نیست. چرخه دانش در تحریریه از گزارش پس از انتشار و بازبینی جمعی عبور می‌کند. نکته مهم این است که سامانه جست‌وجو، دانش پنهان را جایگزین نمی‌کند؛ زمینه مشترک و زمان برای گفت‌وگو لازم است.",
        "assumptions": [
            "دانش، منبع اصلی مزیت رقابتی است.",
            "دانش پنهان و آشکار دو گونه متمایزند.",
            "تبدیل دانش، فرایندی اجتماعی است نه فقط فنی.",
        ],
        "principles": [
            "دانش بی تبدیل، با ترک فرد می‌رود.",
            "زمینه مشترک، شرط تبدیل است.",
            "سامانه بی فرهنگ مشارکت، انبار سند است.",
        ],
        "critiques": [
            "۱. ابهام مفهوم: مرز داده، اطلاعات و دانش روشن نیست.\n۲. سوگیری فناوری: مدیریت دانش به خرید سامانه تقلیل می‌یابد.\n۳. قدرت: کارکنان دانش را منبع قدرت می‌بینند و آن را پنهان می‌کنند.\n۴. سنجش: ارزش دانش و بازده آن سخت اندازه‌گیری می‌شود.\n۵. زمینه ژاپنی: مدل از شرکت‌های ژاپنی برخاسته و انتقال آن جهان‌شمول نیست.",
        ],
        "applications": [
            "مدیریت تحریریه: مستندسازی قضاوت حرفه‌ای و همراهی دبیران.",
            "آرشیو رسانه: روایت‌گذاری محتوای آرشیوی برای بازیابی.",
            "مدیریت ترک خدمت: انتقال دانش پیش از خروج کارمند کلیدی.",
            "آموزش سازمانی: طراحی چرخه اجتماعی‌سازی و درونی‌سازی.",
        ],
        "evolution": "نوناکا در ۱۹۹۴ نظریه آفرینش دانش سازمانی را در مجله علم سازمان منتشر کرد و در ۱۹۹۵ با تاکوچی در کتاب شرکت دانش‌آفرین آن را نظام‌مند ساخت. بعدها مدیریت دانش با سرمایه فکری، سازمان یادگیرنده و سامانه‌های اطلاعاتی پیوند خورد و با نقد سوگیری فناوری روبه‌رو شد.",
        "key_concepts": [
            "دانش پنهان (Tacit Knowledge)",
            "دانش آشکار (Explicit Knowledge)",
            "اجتماعی‌سازی (Socialization)",
            "بیرونی‌سازی (Externalization)",
            "ترکیب (Combination)",
            "مارپیچ دانش (Knowledge Spiral)",
        ],
        "studies": [
            "Nonaka, I., & Takeuchi, H. (1995). The knowledge-creating company. Oxford University Press.",
            "Nonaka, I. (1994). A dynamic theory of organizational knowledge creation. Organization Science, 5(1), 14-37.",
        ],
        "theorists": "ایکوجیرو نوناکا؛ هیروتاکا تاکوچی",
        "theorists_text": "نوناکا و تاکوچی (۱۹۹۵)",
        "year": 1995,
        "model": "چرخه تبدیل دانش: پنهان ↔ آشکار از راه اجتماعی‌سازی، بیرونی‌سازی، ترکیب و درونی‌سازی؛ مارپیچ دانش از فرد به گروه و سازمان.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nنوناکا دانش را از اطلاعات جدا کرد و آفرینش آن را به تعامل اجتماعی گره زد. نوآوری چارچوب، تبدیل دانش پنهان به دارایی سازمانی از راه چرخه چهارگانه است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با تحلیل جریان دانش، مصاحبه و مشاهده اجتماع عمل انجام می‌شود. پژوهشی که تنها شمار سند را می‌سنجد، دانش پنهان را از دست می‌دهد؛ و پژوهشی که سامانه را با مدیریت دانش یکی می‌گیرد، فرهنگ مشارکت را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در تحلیل حافظه سازمانی تحریریه است، اما باید با تحلیل قدرت تکمیل شود. دانشی که پنهان نگه داشته می‌شود، با ترک فرد از سازمان می‌رود.",
        "critique_text": "\n".join([
            "۱. ابهام مفهوم: مرز داده و دانش روشن نیست.",
            "۲. سوگیری فناوری: مدیریت دانش به خرید سامانه تقلیل می‌یابد.",
            "۳. قدرت: دانش پنهان می‌شود.",
            "۴. سنجش: ارزش دانش سخت اندازه‌گیری می‌شود.",
            "۵. زمینه ژاپنی: انتقال جهان‌شمول نیست.",
        ]),
        "example_text": "دبیر باسابقه‌ای پیش از بازنشستگی، سه ماه با جانشین خود گزارش‌ها را مشترک ویرایش می‌کند و منطق تصمیم‌ها را روایت می‌کند؛ این همراهی، دانش پنهان را پیش از خروج او به سازمان منتقل می‌کند.",
    },
    "MC-629": {
        "summary": "(سنگه، ۱۹۹۰) سازمان یادگیرنده، سازمانی است که اعضای آن پیوسته توان خود را برای ساختن آینده مطلوب گسترش می‌دهند. سنگه پنج اصل را معرفی کرد: تسلط شخصی، مدل‌های ذهنی، چشم‌انداز مشترک، یادگیری تیمی و تفکر سیستمی؛ اصل پنجم، پیونددهنده است. سازمان یادگیرنده از دو حلقه یادگیری عبور می‌کند: تک‌حلقه‌ای که خطا را اصلاح می‌کند و دوحلقه‌ای که اهداف و مفروضات را بازنگری می‌کند. این چارچوب، یادگیری را از آموزش فردی به ظرفیت سازمانی منتقل کرد.",
        "definition": "سازمان یادگیرنده، سازمانی است که با پنج اصل تسلط شخصی، مدل‌های ذهنی، چشم‌انداز مشترک، یادگیری تیمی و تفکر سیستمی، ظرفیت پیوسته یادگیری و تغییر خود را می‌سازد.",
        "main_problem": "مسئله این است که چرا سازمان‌ها از تجربه خود نمی‌آموزند و خطاها تکرار می‌شوند. پاسخ، یادگیری فردی بی بازنگری مفروضات سازمانی است. پرسش دوم، سنجش است: چگونه یادگیری را از شعار جدا کنیم.",
        "mechanism": "۱. تسلط شخصی: هر عضو، توانش را برای رسیدن به نتایجی که واقعاً می‌خواهد گسترش می‌دهد.\n۲. مدل‌های ذهنی: مفروضات و تصورات نانوشته آشکار و بازبینی می‌شوند.\n۳. چشم‌انداز مشترک: تصویر آینده مطلوب، تعهد جمعی می‌سازد.\n۴. یادگیری تیمی: گفت‌وگوی صریح و تفکر جمعی، دانش تیمی می‌سازد.\n۵. تفکر سیستمی: روابط و بازخوردهای کل نظام دیده می‌شود، نه رویدادهای جدا.\n۶. دوحلقه یادگیری: اصلاح خطا در حلقه نخست و بازنگری اهداف و مفروضات در حلقه دوم.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا تحریریه‌ای که تنها خطای تیتر را اصلاح می‌کند، ریشه افت اعتماد را نمی‌بیند و چرا جلسه پس از انتشار باید به بازبینی فرایند بدل شود. تحول دیجیتال رسانه بی تفکر سیستمی، به تغییر ابزار بی تغییر رویه می‌رسد. همچنین آیین بازبینی باید از سرزنش فردی به تحلیل فرایند تغییر کند تا کارکنان خطا را پنهان نکنند. نکته مهم این است که سازمان یادگیرنده، سازمان بی‌خطا نیست؛ سازمانی است که خطا را به دانش بدل می‌کند.",
        "assumptions": [
            "یادگیری سازمانی بیش از جمع یادگیری افراد است.",
            "مفروضات پنهان، رفتار سازمان را هدایت می‌کنند.",
            "تفکر سیستمی، شرط یادگیری پایدار است.",
        ],
        "principles": [
            "خطا، داده یادگیری است.",
            "گفت‌وگوی صریح، یادگیری تیمی می‌سازد.",
            "بازنگری مفروضات، از تکرار خطا جلوگیری می‌کند.",
        ],
        "critiques": [
            "۱. ابهام: پنج اصل، توصیفی و سخت قابل سنجش‌اند.\n۲. آرمان‌گرایی: سازمان یادگیرنده به آرزو بدل می‌شود.\n۳. قدرت: گفت‌وگوی باز در سلسله‌مراتب نابرابر دشوار است.\n۴. زمان: یادگیری دوحلقه‌ای به منابع و فراغت نیاز دارد.\n۵. عملکرد: پیوند یادگیری و عملکرد مالی یکدست نیست.",
        ],
        "applications": [
            "تحریریه: جلسه بازبینی پس از انتشار با نگاه سیستمی.",
            "تحول دیجیتال: بازنگری رویه، نه فقط خرید ابزار.",
            "آموزش سازمانی: طراحی گفت‌وگوی تیمی و مدل ذهنی.",
            "پژوهش سازمانی: سنجش ظرفیت یادگیری دوحلقه‌ای.",
        ],
        "evolution": "سنگه در ۱۹۹۰ پنج انضباط را در کتاب انضباط پنجم عرضه کرد و در ۲۰۰۶ نسخه بازنگری‌شده آن را منتشر کرد. این چارچوب بر پایه کار آرگریس و شون در یادگیری دوحلقه‌ای بنا شد و به مدیریت تغییر، توسعه سازمانی و پژوهش رسانه راه یافت.",
        "key_concepts": [
            "سازمان یادگیرنده (Learning Organization)",
            "تفکر سیستمی (Systems Thinking)",
            "مدل‌های ذهنی (Mental Models)",
            "چشم‌انداز مشترک (Shared Vision)",
            "یادگیری تیمی (Team Learning)",
            "یادگیری دوحلقه‌ای (Double-Loop Learning)",
        ],
        "studies": [
            "Senge, P. M. (1990). The fifth discipline: The art and practice of the learning organization. Doubleday/Currency.",
            "Argyris, C., & Schön, D. A. (1978). Organizational learning: A theory of action perspective. Addison-Wesley.",
        ],
        "theorists": "پیتر سنگه",
        "theorists_text": "پیتر سنگه (۱۹۹۰)",
        "year": 1990,
        "model": "پنج اصل: تسلط شخصی + مدل‌های ذهنی + چشم‌انداز مشترک + یادگیری تیمی + تفکر سیستمی → ظرفیت یادگیری دوحلقه‌ای.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nسنگه یادگیری را از آموزش فردی به ظرفیت جمعی سازمان منتقل کرد و تفکر سیستمی را پیونددهنده اصول دانست. نوآوری چارچوب، تبدیل یادگیری از رویداد به رویه است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با تحلیل جلسه‌های بازبینی، بررسی مدل‌های ذهنی و شاخص یادگیری انجام می‌شود. پژوهشی که تنها ساعت آموزش را می‌سنجد، یادگیری سازمانی را از دست می‌دهد؛ و پژوهشی که بی مشارکت کارکنان سنجش می‌کند، گفت‌وگوی باز را از بین می‌برد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در تحلیل تحول تحریریه است، اما باید با تحلیل قدرت تکمیل شود. یادگیری بی امنیت روانی، به سکوت و پنهان‌کاری خطا می‌انجامد.",
        "critique_text": "\n".join([
            "۱. ابهام: اصول سخت قابل سنجش نیستند.",
            "۲. آرمان‌گرایی: سازمان یادگیرنده به شعار بدل می‌شود.",
            "۳. قدرت: گفت‌وگوی باز در سلسله‌مراتب دشوار است.",
            "۴. زمان: یادگیری دوحلقه‌ای منابع می‌خواهد.",
            "۵. عملکرد: پیوند با عملکرد مالی یکدست نیست.",
        ]),
        "example_text": "تحریریه‌ای پس از یک خطای خبری، فقط تیتر را اصلاح می‌کند و ماه بعد خطای مشابه رخ می‌دهد؛ جلسه بازبینی که ریشه تصمیم و مفروضات را بررسی می‌کند، از حلقه نخست به حلقه دوم یادگیری می‌رود.",
    },
    "MC-632": {
        "summary": "(باس، ۱۹۸۵) نظریه رهبری تحول‌آفرین و تعاملی دو الگوی رهبری را تفکیک می‌کند: رهبر تعاملی با مبادله پاداش و نظارت، عملکرد مورد انتظار را حفظ می‌کند؛ رهبر تحول‌آفرین با نفوذ آرمانی، انگیزش الهام‌بخش، تحریک فکری و توجه فردی، عملکرد را از انتظار فراتر می‌برد. باس این مدل را بر پایه کار برنز بنا کرد، اما آن را به سازه‌های قابل سنجش تبدیل کرد. مدل چهار مؤلفه تحول‌آفرین دارد و به پژوهش رهبری، اعتماد و عملکرد گسترانده شد.",
        "definition": "رهبری تحول‌آفرین، سبکی است که با نفوذ آرمانی، انگیزش الهام‌بخش، تحریک فکری و توجه فردی، پیروان را به عملکرد فراتر از انتظار می‌برد؛ در برابر رهبری تعاملی که بر مبادله و نظارت استوار است.",
        "main_problem": "مسئله این است که چرا برخی رهبران تنها وظیفه را مدیریت می‌کنند و برخی سازمان را دگرگون می‌سازند. پاسخ، کیفیت رابطه و سطح انگیزش پیرو است. پرسش دوم، مرز اخلاقی است: تحول‌آفرینی می‌تواند کیش شخصیت و اطاعت کورکورانه هم بسازد.",
        "mechanism": "۱. پاداش مشروط: رهبر تعاملی در برابر عملکرد مورد انتظار، پاداش روشن می‌دهد.\n۲. مدیریت بر مبنای استثنا: رهبر تنها در انحراف از استاندارد دخالت می‌کند.\n۳. نفوذ آرمانی: رهبر الگوی رفتاری و ارزشی می‌شود و اعتماد و احترام می‌سازد.\n۴. انگیزش الهام‌بخش: رهبر چشم‌انداز جذاب می‌سازد و معنای کار را برجسته می‌کند.\n۵. تحریک فکری: رهبر پیروان را به بازنگری مفروضات و حل تازه مسائل برمی‌انگیزد.\n۶. توجه فردی: رهبر نیاز رشد هر فرد را می‌بیند و مسیر توسعه می‌سازد.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا سردبیری که تنها ضرب‌الاجل و پاداش می‌دهد، تحریریه‌ای محافظه‌کار می‌سازد و چرا رهبری که معنا و استقلال حرفه‌ای می‌دهد، نوآوری تحریریه را برمی‌انگیزد. در بحران رسانه، نفوذ آرمانی و انگیزش الهام‌بخش، تاب‌آوری تیم را می‌سازد و فضای آزمون و خطا را باز می‌کند. نکته مهم این است که تحول‌آفرینی بی سازوکار نقد، به وابستگی به شخصیت رهبر می‌انجامد.",
        "assumptions": [
            "رهبری تحول‌آفرین از رهبری تعاملی متمایز است.",
            "چهار مؤلفه تحول‌آفرین قابل سنجش‌اند.",
            "انگیزش درونی، عملکرد فراتر از انتظار می‌سازد.",
        ],
        "principles": [
            "مبادله، عملکرد مورد انتظار می‌سازد نه تحول.",
            "معنا، محرک عملکرد فراتر است.",
            "تحول بی نقد، وابستگی می‌سازد.",
        ],
        "critiques": [
            "۱. سوگیری سنجش: ابزار پرسش‌نامه‌ای، نگرش پیرو را می‌سنجد نه اثر عینی.\n۲. جذابیت تاریک: رهبری کاریزماتیک می‌تواند به استبداد بیانجامد.\n۳. نسبت‌دهی: موفقیت سازمان به رهبر نسبت داده می‌شود.\n۴. زمینه: اثربخشی سبک به فرهنگ و بحران وابسته است.\n۵. سوگیری جنسیتی: انتظارات از رهبر تحول‌آفرین، مردانه رمزگذاری شده است.",
        ],
        "applications": [
            "مدیریت تحریریه: ترکیب پاداش روشن با معنا و استقلال.",
            "مدیریت بحران رسانه: انگیزش الهام‌بخش برای تاب‌آوری تیم.",
            "توسعه رهبر: آموزش توجه فردی و تحریک فکری.",
            "پژوهش سازمانی: تحلیل سبک رهبری و نوآوری تحریریه.",
        ],
        "evolution": "برنز در ۱۹۷۸ رهبری تحول‌آفرین را از تعاملی تفکیک کرد و باس در ۱۹۸۵ آن را به مدلی چهارمؤلفه‌ای و سنجش‌پذیر تبدیل کرد. مدل بعدها با نظریه مبادله رهبر–عضو، اعتماد و عدالت سازمانی پیوند خورد و نقد جذابیت تاریک را جذب کرد.",
        "key_concepts": [
            "رهبری تحول‌آفرین (Transformational Leadership)",
            "رهبری تعاملی (Transactional Leadership)",
            "نفوذ آرمانی (Idealized Influence)",
            "انگیزش الهام‌بخش (Inspirational Motivation)",
            "تحریک فکری (Intellectual Stimulation)",
            "توجه فردی (Individualized Consideration)",
        ],
        "studies": [
            "Bass, B. M. (1985). Leadership and performance beyond expectations. Free Press.",
            "Burns, J. M. (1978). Leadership. Harper & Row.",
        ],
        "theorists": "برنارد باس؛ جیمز مک‌گرگور برنز",
        "theorists_text": "برنز (۱۹۷۸)؛ باس (۱۹۸۵)",
        "year": 1985,
        "model": "رهبری تعاملی: پاداش مشروط + مدیریت بر مبنای استثنا → عملکرد مورد انتظار؛ رهبری تحول‌آفرین: نفوذ آرمانی + انگیزش الهام‌بخش + تحریک فکری + توجه فردی → عملکرد فراتر از انتظار.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nباس رهبری را از مبادله به تحول انگیزشی گسترد و آن را در چهار سازه عملیاتی کرد. نوآوری چارچوب، سنجش‌پذیر کردن تفکیک برنز است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با پرسش‌نامه چندعاملی رهبری و رتبه‌بندی پیروان انجام می‌شود. پژوهشی که تنها رضایت پیرو را می‌سنجد، اثر عملکردی را از دست می‌دهد؛ و پژوهشی که رهبر را تنها منبع داده می‌گیرد، سوگیری خودستایی را وارد می‌کند.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در تحلیل تحول تحریریه است، اما باید با تحلیل ساختار تکمیل شود. رهبر تحول‌آفرین بی نقد بیرونی، تحریریه را به پیروی از شخصیت بدل می‌کند.",
        "critique_text": "\n".join([
            "۱. سوگیری سنجش: نگرش پیرو جای اثر عینی را می‌گیرد.",
            "۲. جذابیت تاریک: کاریزما به استبداد می‌انجامد.",
            "۳. نسبت‌دهی: موفقیت به رهبر نسبت داده می‌شود.",
            "۴. زمینه: اثربخشی به فرهنگ و بحران وابسته است.",
            "۵. سوگیری جنسیتی: انتظارات رهبری مردانه رمزگذاری شده است.",
        ]),
        "example_text": "سردبیری که تنها ضرب‌الاجل و پاداش می‌دهد، تیمی محافظه‌کار می‌سازد؛ سردبیری که معنا و استقلال می‌دهد و پرسش‌های تازه را پاداش می‌دهد، تیم را به نوآوری می‌برد. تفاوت، سبک تحول‌آفرین است نه حجم پاداش.",
    },
    "MC-633": {
        "summary": "(هرسی و بلانچارد، ۱۹۶۹) رهبری موقعیتی می‌گوید سبک مؤثر رهبری ثابت نیست و باید با آمادگی پیروان هم‌خوان شود. مدل دو بُعد رفتار را ترکیب می‌کند: رفتار وظیفه‌محور و رفتار رابطه‌محور، و چهار سبک می‌سازد: دستوردهی، فروش، مشارکت و تفویض. سبک مؤثر با سطح آمادگی پیرو، یعنی توانایی و انگیزه او در تکلیف، تعیین می‌شود. مدل، آموزش رهبری را از ویژگی‌های شخصی به تشخیص موقعیت منتقل کرد.",
        "definition": "رهبری موقعیتی، مدلی است که اثر رهبری را تابع هم‌خوانی سبک رهبر با سطح آمادگی پیرو در تکلیف می‌داند و چهار سبک دستوردهی، فروش، مشارکت و تفویض را از ترکیب رفتار وظیفه‌محور و رابطه‌محور می‌سازد.",
        "main_problem": "مسئله این است که چرا یک سبک رهبری در یک تیم کار می‌کند و در تیم دیگر نه. پاسخ، آمادگی پیرو است. پرسش دوم، سنجش است: آمادگی چگونه اندازه‌گیری می‌شود و خطر برچسب‌زنی پیرو کجاست.",
        "mechanism": "۱. رفتار وظیفه‌محور: میزان تعیین نقش، دستور کار و استاندارد عملکرد.\n۲. رفتار رابطه‌محور: میزان حمایت، شنیدن و تشویق ارتباط دوطرفه.\n۳. آمادگی پیرو: ترکیب توانایی و تمایل او برای انجام تکلیف.\n۴. سبک دستوردهی: وظیفه بالا و رابطه پایین؛ مناسب پیرو کم‌توان و کم‌انگیزه.\n۵. سبک فروش و مشارکت: با رشد آمادگی، رابطه و سپس مشارکت افزایش می‌یابد.\n۶. سبک تفویض: وظیفه و رابطه پایین؛ مناسب پیرو توانمند و متعهد.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا سردبیر با کارآموز باید دستور کار روشن بدهد و با خبرنگار باسابقه تفویض کند، چرا در بحران سبک دستوردهی موقت لازم می‌شود و چرا تفویض زودهنگام به آزمون و خطا می‌انجامد. همچنین تیم دورکار با آمادگی ناهمگون، سبک یکسان را برنمی‌تابد و رهبر باید سبک را در سطح هر عضو تنظیم کند، نه در سطح کل تیم. ارزیابی آمادگی نیز باید مخصوص تکلیف باشد؛ خبرنگار توانمند در گزارش تحقیقی ممکن است در تولید ویدئو تازه‌کار باشد. نکته مهم این است که آمادگی، وضعیتی و مخصوص تکلیف است؛ برچسب ثابت به فرد نمی‌چسبد.",
        "assumptions": [
            "سبک اثربخش رهبری، وابسته به موقعیت است.",
            "آمادگی پیرو، تعیین‌کننده سبک است.",
            "رفتار وظیفه‌محور و رابطه‌محور، دو بُعد مستقل‌اند.",
        ],
        "principles": [
            "سبک ثابت، در همه موقعیت‌ها مؤثر نیست.",
            "آمادگی، وضعیتی است نه ویژگی ثابت.",
            "تفویض بی آمادگی، رهاکردن است.",
        ],
        "critiques": [
            "۱. شواهد تجربی: پشتیبانی پژوهش‌ها یکدست نیست.\n۲. ابهام آمادگی: توانایی و انگیزه، ساده‌سازی شده‌اند.\n۳. توصیه‌گرایی: مدل بیشتر تجویزی است تا تبیینی.\n۴. زمینه فرهنگی: وزن دستوردهی در فرهنگ‌ها یکسان نیست.\n۵. کم‌توجهی به ساختار: محدودیت سازمانی و منابع کمتر دیده می‌شود.",
        ],
        "applications": [
            "مدیریت تحریریه: تطبیق سبک با تجربه خبرنگار.",
            "آموزش رهبری: تشخیص آمادگی و انتخاب سبک.",
            "مدیریت بحران: استفاده موقت از سبک دستوردهی.",
            "رهبری تیم دورکار: تنظیم نظارت بر پایه آمادگی.",
        ],
        "evolution": "هرسی و بلانچارد در ۱۹۶۹ مدل را در کتاب مدیریت رفتار سازمانی عرضه کردند و در ویرایش‌های بعدی آن را با مفهوم آمادگی پیرو بازنگری کردند. مدل به آموزش مدیریت راه یافت و با نقد شواهد و ابهام مفهومی روبه‌رو شد.",
        "key_concepts": [
            "رهبری موقعیتی (Situational Leadership)",
            "رفتار وظیفه‌محور (Task Behavior)",
            "رفتار رابطه‌محور (Relationship Behavior)",
            "آمادگی پیرو (Follower Readiness)",
            "سبک دستوردهی (Telling Style)",
            "سبک تفویض (Delegating Style)",
        ],
        "studies": [
            "Hersey, P., & Blanchard, K. H. (1969). Management of organizational behavior. Prentice-Hall.",
            "Hersey, P., Blanchard, K. H., & Johnson, D. E. (2008). Management of organizational behavior (9th ed.). Prentice Hall.",
        ],
        "theorists": "پاول هرسی؛ کن بلانچارد",
        "theorists_text": "هرسی و بلانچارد (۱۹۶۹)",
        "year": 1969,
        "model": "دو بُعد رفتار (وظیفه و رابطه) × آمادگی پیرو → چهار سبک: دستوردهی، فروش، مشارکت، تفویض؛ سبک با رشد آمادگی جابه‌جا می‌شود.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nهرسی و بلانچارد رهبری را از ویژگی شخصی به تعامل سبک و موقعیت منتقل کردند. نوآوری چارچوب، ترکیب دو بُعد رفتار در یک فضای چهارسبکی است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با پرسش‌نامه سبک رهبری و ارزیابی آمادگی پیرو انجام می‌شود. پژوهشی که تنها سبک را می‌سنجد، موقعیت را از دست می‌دهد؛ و پژوهشی که آمادگی را برچسب ثابت می‌گیرد، تحول پیرو را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در طراحی نظارت تحریریه است، اما باید با تحلیل ساختار تکمیل شود. تفویض در سازمان بی منابع، به رهاکردن بدل می‌شود.",
        "critique_text": "\n".join([
            "۱. شواهد تجربی: پشتیبانی یکدست نیست.",
            "۲. ابهام آمادگی: توانایی و انگیزه ساده شده‌اند.",
            "۳. توصیه‌گرایی: مدل تجویزی است.",
            "۴. زمینه فرهنگی: وزن دستوردهی یکسان نیست.",
            "۵. ساختار: محدودیت سازمانی کم دیده می‌شود.",
        ]),
        "example_text": "سردبیری که به کارآموز موضوع و ساختار گزارش را دقیق می‌گوید، سبک دستوردهی را برمی‌گزیند؛ همان سردبیر با گزارشگر باسابقه فقط موضوع را توافق می‌کند و نگارش را تفویض می‌کند. سبک با آمادگی پیرو تغییر کرده است.",
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
                                       "verified": n_verified, "batch": 102}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH102 THEORY DONE")


if __name__ == "__main__":
    main()
