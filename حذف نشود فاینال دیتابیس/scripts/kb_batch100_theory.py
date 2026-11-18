# -*- coding: utf-8 -*-
"""Batch 100: full documentation for MC-615, MC-616, MC-617, MC-618."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch100-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch100_theory.json"

S = {
    "MC-615": [
        dict(kind="BOOK",
             title_en="Theory Z: How American Business Can Meet the Japanese Challenge",
             title_fa="نظریه زد: چگونه کسب‌وکار آمریکایی می‌تواند به چالش ژاپن پاسخ دهد",
             authors="Ouchi, W. G.", year=1981, publisher="Addison-Wesley",
             doi=None, url="https://archive.org/details/theoryzhowameri100ouch",
             language="en", isbn=None,
             citation="Ouchi, W. G. (1981). Theory Z: How American business can meet the Japanese challenge. Addison-Wesley.",
             locator="work", locator_type="work",
             supports="type Z organizational model / seven features / trust, subtlety and intimacy", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Type Z Organization: Stability in the Midst of Mobility",
             title_fa="سازمان نوع زد: پایداری در میانه تحرک",
             authors="Ouchi, W. G.; Jaeger, A. M.", year=1978,
             publisher="Academy of Management Review",
             doi=None, url=None, language="en", isbn=None,
             citation="Ouchi, W. G., & Jaeger, A. M. (1978). Type Z organization: Stability in the midst of mobility. Academy of Management Review, 3(2), 305-314.",
             locator="3(2):305-314", locator_type="page_range",
             supports="type Z model antecedent / modified Japanese practices", verified=False),
    ],
    "MC-616": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Toward a Theory of Task Motivation and Incentives",
             title_fa="درآمدی بر نظریه انگیزش تکلیف و مشوق‌ها",
             authors="Locke, E. A.", year=1968,
             publisher="Organizational Behavior and Human Performance",
             doi=None, url=None, language="en", isbn=None,
             citation="Locke, E. A. (1968). Toward a theory of task motivation and incentives. Organizational Behavior and Human Performance, 3(2), 157-189.",
             locator="3(2):157-189", locator_type="page_range",
             supports="specific and difficult goals as performance determinants", verified=True),
        dict(kind="BOOK",
             title_en="A Theory of Goal Setting and Task Performance",
             title_fa="نظریه هدف‌گذاری و عملکرد تکلیف",
             authors="Locke, E. A.; Latham, G. P.", year=1990, publisher="Prentice Hall",
             doi=None, url=None, language="en", isbn=None,
             citation="Locke, E. A., & Latham, G. P. (1990). A theory of goal setting and task performance. Prentice Hall.",
             locator="work", locator_type="work",
             supports="moderators: ability, commitment, feedback, task complexity", verified=False),
    ],
    "MC-617": [
        dict(kind="BOOK",
             title_en="The Behavior of Organisms: An Experimental Analysis",
             title_fa="رفتار موجودات زنده: تحلیلی آزمایشی",
             authors="Skinner, B. F.", year=1938, publisher="Appleton-Century",
             doi=None, url="https://www.bfskinner.org/wp-content/uploads/2016/02/BoO.pdf",
             language="en", isbn=None,
             citation="Skinner, B. F. (1938). The behavior of organisms: An experimental analysis. Appleton-Century.",
             locator="work", locator_type="work",
             supports="operant conditioning / reinforcement as behavioral selection", verified=True),
        dict(kind="BOOK",
             title_en="Science and Human Behavior",
             title_fa="علم و رفتار انسانی",
             authors="Skinner, B. F.", year=1953, publisher="Macmillan",
             doi=None, url=None, language="en", isbn=None,
             citation="Skinner, B. F. (1953). Science and human behavior. Macmillan.",
             locator="work", locator_type="work",
             supports="reinforcement schedules / shaping / social applications", verified=False),
    ],
    "MC-618": [
        dict(kind="BOOK",
             title_en="The Achieving Society",
             title_fa="جامعه دستیابنده",
             authors="McClelland, D. C.", year=1961, publisher="D. Van Nostrand",
             doi=None, url="https://psycnet.apa.org/doiLanding?doi=10.1037%2F14359-000",
             language="en", isbn=None,
             citation="McClelland, D. C. (1961). The achieving society. D. Van Nostrand.",
             locator="work", locator_type="work",
             supports="learned needs for achievement, power and affiliation / economic growth link", verified=True),
        dict(kind="BOOK",
             title_en="Human Motivation",
             title_fa="انگیزش انسانی",
             authors="McClelland, D. C.", year=1987, publisher="Cambridge University Press",
             doi=None, url=None, language="en", isbn=None,
             citation="McClelland, D. C. (1987). Human motivation. Cambridge University Press.",
             locator="work", locator_type="work",
             supports="revised account of the three learned motives", verified=False),
    ],
}

ENRICH = {
    "MC-615": {
        "summary": "(اوچی، ۱۹۸۱) نظریه زد، الگویی از سازمان است که اوچی از مطالعه شرکت‌های ژاپنی و آمریکایی استخراج کرد تا راهی برای ترکیب بهره‌وری ژاپنی با ارزش‌های فردی آمریکایی بیابد. سازمان نوع زد هفت ویژگی دارد: استخدام بلندمدت، ارزیابی و ارتقای کند، مسیر شغلی غیرتخصصی، کنترل غیررسمی و ضمنی، تصمیم‌گیری جمعی، مسئولیت فردی و توجه کل‌نگر به کارمند و خانواده او. اوچی زد را در برابر نوع آمریکایی و نوع ژاپنی نشاند و گفت اعتماد، ظرافت و صمیمیت، سازوکار اصلی هماهنگی است.",
        "definition": "نظریه زد، مدلی از سازمان است که عناصر مدیریت ژاپنی و آمریکایی را در قالبی با استخدام بلندمدت، تصمیم‌گیری جمعی، مسئولیت فردی و کنترل ضمنی ترکیب می‌کند و هماهنگی را بر اعتماد و صمیمیت بنیاد می‌گذارد.",
        "main_problem": "مسئله این است که چرا شرکت‌های ژاپنی در دهه ۱۹۷۰ بهره‌وری بالاتری از شرکت‌های آمریکایی داشتند. پاسخ اوچی فناوری نیست؛ سازمان اجتماعی کارخانه است. پرسش دوم، انتقال است: کدام عناصر فرهنگ ژاپنی قابل انتقال است و کدام به بستر فرهنگی وابسته است.",
        "mechanism": "۱. استخدام بلندمدت: امنیت شغلی، انگیزه سرمایه‌گذاری در مهارت و وفاداری را می‌سازد و هزینه ترک سازمان را بالا می‌برد.\n۲. ارزیابی و ارتقای کند: ارزیابی بلندمدت، رقابت کوتاه‌مدت را کم و همکاری را تقویت می‌کند.\n۳. مسیر شغلی غیرتخصصی: چرخش شغلی، دید کل‌نگر و انعطاف تیمی می‌سازد.\n۴. کنترل ضمنی و غیررسمی: هنجارها و فرهنگ مشترک جای دستور و نظارت رسمی را می‌گیرد و کنترل را ارزان می‌کند.\n۵. تصمیم‌گیری جمعی با مسئولیت فردی: تصمیم با مشورت گرفته می‌شود اما مسئولیت نهایی فردی می‌ماند.\n۶. توجه کل‌نگر: سازمان به زندگی کارمند و خانواده او توجه می‌کند و پیوند عاطفی و تعهد می‌سازد.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا تحریریه‌ای با استخدام بلندمدت و ارتقای کند، همکاری و حافظه سازمانی بیشتری دارد و چرا تحریریه‌ای با جابه‌جایی سریع، دانش زمینه‌ای را از دست می‌دهد. تصمیم‌گیری جمعی در انتخاب موضوع و مسئولیت فردی در انتشار خبر، نمونه سازمانی این مدل است. نکته مهم این است که نظریه زد کنترل را از سلسله‌مراتب به فرهنگ منتقل می‌کند و همین، خطر همگرایی فکری و فشار همنوایی دارد.",
        "assumptions": [
            "بهره‌وری، تابع سازمان اجتماعی است نه فقط فناوری.",
            "اعتماد و صمیمیت، هزینه هماهنگی را کم می‌کنند.",
            "عناصر مدیریتی میان فرهنگ‌ها قابل ترکیب‌اند.",
        ],
        "principles": [
            "امنیت شغلی، پیش‌شرط سرمایه‌گذاری در مهارت است.",
            "ارزیابی بلندمدت، همکاری می‌سازد.",
            "فرهنگ مشترک، کنترل ارزان است.",
        ],
        "critiques": [
            "۱. انتقال‌پذیری فرهنگی: شرکت‌های نمونه، ژاپنی و منتخب بودند.\n۲. شواهد: موفقیت ژاپن به شرایط تاریخی و نهادی نیز وابسته بود.\n۳. هزینه امنیت شغلی: استخدام بلندمدت در بازار متغیر، انعطاف را کم می‌کند.\n۴. خطر همنوایی: کنترل فرهنگی می‌تواند اختلاف نظر را سرکوب کند.\n۵. تغییر زمینه: اقتصاد پلتفرمی، مفروضات استخدام بلندمدت را به چالش کشیده است.",
        ],
        "applications": [
            "طراحی سازمان رسانه‌ای: تعادل امنیت شغلی و نوآوری.",
            "مدیریت تحریریه: تصمیم‌گیری جمعی با مسئولیت روشن.",
            "فرهنگ سازمانی: جایگزینی نظارت با هنجار مشترک.",
            "پژوهش مدیریت: مقایسه الگوهای سازمانی میان فرهنگ‌ها.",
        ],
        "evolution": "اوچی در ۱۹۷۸ سازمان نوع زد را با یاگر توصیف کرد و در ۱۹۸۱ در کتاب نظریه زد آن را به الگویی برای مدیریت آمریکایی تبدیل کرد. این خط پژوهشی با مفهوم کنترل قبیله‌ای و سرمایه اجتماعی سازمانی پیوند خورد و بعدها با نقد انتقال‌پذیری فرهنگی و اقتصاد کار منعطف روبه‌رو شد.",
        "key_concepts": [
            "سازمان نوع زد (Type Z Organization)",
            "استخدام بلندمدت (Long-Term Employment)",
            "تصمیم‌گیری جمعی (Collective Decision Making)",
            "مسئولیت فردی (Individual Responsibility)",
            "کنترل ضمنی (Implicit Control)",
            "اعتماد سازمانی (Organizational Trust)",
        ],
        "studies": [
            "Ouchi, W. G. (1981). Theory Z: How American business can meet the Japanese challenge. Addison-Wesley.",
            "Ouchi, W. G., & Jaeger, A. M. (1978). Type Z organization. Academy of Management Review, 3(2), 305-314.",
        ],
        "theorists": "ویلیام اوچی",
        "theorists_text": "ویلیام اوچی (۱۹۸۱)",
        "year": 1981,
        "model": "مدل زد: استخدام بلندمدت + ارزیابی کند + مسیر غیرتخصصی + کنترل ضمنی + تصمیم جمعی + مسئولیت فردی + توجه کل‌نگر → اعتماد و هماهنگی → بهره‌وری.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nاوچی بهره‌وری را از فناوری به سازمان اجتماعی منتقل کرد و مدل ژاپنی را نه کپی، بلکه ترکیبی با ارزش‌های فردی آمریکایی خواند. نوآوری چارچوب، جایگزینی نظارت رسمی با اعتماد و فرهنگ است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با مطالعه موردی شرکت‌ها و مقایسه الگوهای استخدام، ارزیابی و تصمیم‌گیری انجام می‌شود. پژوهشی که تنها شاخص بهره‌وری را می‌سنجد، سازوکار اجتماعی را از دست می‌دهد؛ و پژوهشی که یک شرکت موفق را الگو می‌گیرد، انتخاب نمونه را وارد نتیجه می‌کند.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در توضیح حافظه سازمانی و همکاری تحریریه است، اما باید با تحلیل بازار کار تکمیل شود. امنیت شغلی بی سازوکار نقد، به رکود فکری می‌انجامد.",
        "critique_text": "\n".join([
            "۱. انتقال‌پذیری فرهنگی: نمونه‌ها ژاپنی و منتخب بودند.",
            "۲. شواهد: شرایط نهادی نیز تعیین‌کننده بود.",
            "۳. هزینه امنیت شغلی: انعطاف کم می‌شود.",
            "۴. خطر همنوایی: کنترل فرهنگی اختلاف را سرکوب می‌کند.",
            "۵. تغییر زمینه: اقتصاد پلتفرمی مفروضات را به چالش کشیده است.",
        ]),
        "example_text": "تحریریه‌ای که خبرنگاران را بلندمدت نگه می‌دارد و ارتقا را کند می‌کند، کمتر شاهد رقابت مخرب است؛ اما اگر جلسه‌های تصمیم به همنوایی بدل شود، تنوع دیدگاه از دست می‌رود.",
    },
    "MC-616": {
        "summary": "(لاک، ۱۹۶۸؛ لاک و لتم، ۱۹۹۰) نظریه هدف‌گذاری می‌گوید هدف آگاهانه رفتار را هدایت می‌کند و هدف مشخص و دشوار، عملکرد بالاتری از هدف مبهم «بهترین تلاش خود را بکن» می‌سازد، به شرط توانایی، تعهد به هدف، بازخورد و سادگی نسبی تکلیف. هدف از چهار مسیر عمل می‌کند: جهت‌دهی توجه، بسیج تلاش، افزایش پایداری و فعال‌سازی راهبرد. در تکالیف پیچیده، هدف یادگیری بهتر از هدف عملکردی جواب می‌دهد. مدل، پایه مدیریت بر مبنای هدف و سامانه‌های سنجه شد.",
        "definition": "نظریه هدف‌گذاری، چارچوبی است که رفتار کاری را تابع هدف‌های آگاهانه می‌داند و اثر هدف مشخص و دشوار بر عملکرد را با متغیرهای توانایی، تعهد، بازخورد و پیچیدگی تکلیف توضیح می‌دهد.",
        "main_problem": "مسئله این است که چرا برخی کارکنان با استعداد یکسان عملکرد متفاوت دارند. پاسخ، وضوح و دشواری هدف است. پرسش دوم، عوارض است: تمرکز بر هدف عددی چه زمانی به رفتار ناسالم، کوته‌بینی یا بازی با سنجه می‌انجامد.",
        "mechanism": "۱. جهت‌دهی توجه: هدف، توجه را از فعالیت‌های نامرتبط به رفتار مرتبط با نتیجه می‌برد.\n۲. بسیج تلاش: هرچه هدف دشوارتر اما دست‌یافتنی باشد، تلاش بیشتری برمی‌انگیزد.\n۳. پایداری: هدف، تحمل مدت طولانی‌تر کار و مقاومت در برابر وقفه را افزایش می‌دهد.\n۴. راهبرد: هدف، جست‌وجوی روش‌های تازه و انتخاب راهبرد مؤثرتر را فعال می‌کند.\n۵. تعدیل‌گرها: توانایی، تعهد به هدف، بازخورد و پیچیدگی تکلیف، شدت اثر هدف را تعیین می‌کنند.\n۶. هدف یادگیری: در تکالیف پیچیده و تازه، هدف یادگیری به جای هدف نتیجه، عملکرد را بهتر می‌سازد.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا تحریریه‌ای که تنها هدف دسترس یا کلیک می‌گیرد به طعمه‌کلیک می‌رسد و چرا هدف کیفیت باید در سنجه وارد شود. سنجه، رفتار را می‌سازد؛ هر معیاری که پاداش بگیرد به هدف بدل می‌شود، حتی اگر با مأموریت رسانه ناسازگار باشد. نکته مهم این است که هدف دشوار بی بازخورد و تعهد، به فشار و سرخوردگی می‌انجامد.",
        "assumptions": [
            "هدف آگاهانه، علت نزدیک رفتار است.",
            "هدف مشخص و دشوار، عملکرد را بالا می‌برد.",
            "تعهد و بازخورد، شرط اثر هدف‌اند.",
        ],
        "principles": [
            "هدف مبهم، عملکرد مبهم می‌سازد.",
            "دشواری هدف، تلاش را بالا می‌برد.",
            "سنجه پاداش‌گرفته، رفتار را هدایت می‌کند.",
        ],
        "critiques": [
            "۱. کوته‌بینی: هدف عددی، توجه به ابعاد ناسنجیده را کم می‌کند.\n۲. رفتار ناسالم: هدف سخت می‌تواند تقلب و میان‌بر را برانگیزد.\n۳. پیچیدگی تکلیف: در کار خلاق، هدف عملکردی می‌تواند عملکرد را کم کند.\n۴. تعمیم: بیشتر شواهد از تکالیف ساده و آزمایشگاهی می‌آید.\n۵. سنجه رسانه: هدف کلیک، کیفیت خبر را قربانی می‌کند.",
        ],
        "applications": [
            "مدیریت عملکرد: طراحی هدف مشخص، دشوار و بازخوردپذیر.",
            "مدیریت تحریریه: ترکیب هدف کیفیت و هدف دسترس.",
            "آموزش: هدف یادگیری برای مهارت‌های پیچیده.",
            "کمپین: هدف رفتاری مشخص به‌جای پیام کلی.",
        ],
        "evolution": "لاک در ۱۹۶۸ رابطه هدف و عملکرد را صورت‌بندی کرد و با لتم در دهه‌های بعد نظریه را با تعدیل‌گرها گسترد و در ۱۹۹۰ در کتابی نظام‌مند کرد. بعدها نقد کوته‌بینی و رفتار ناسالم، پژوهش هدف‌گذاری را به سمت هدف یادگیری و سنجه‌های چندبعدی برد.",
        "key_concepts": [
            "هدف مشخص (Specific Goal)",
            "دشواری هدف (Goal Difficulty)",
            "تعهد به هدف (Goal Commitment)",
            "بازخورد (Feedback)",
            "هدف یادگیری (Learning Goal)",
            "کوته‌بینی سنجه (Metric Myopia)",
        ],
        "studies": [
            "Locke, E. A. (1968). Toward a theory of task motivation and incentives. Organizational Behavior and Human Performance, 3(2), 157-189.",
            "Locke, E. A., & Latham, G. P. (1990). A theory of goal setting and task performance. Prentice Hall.",
        ],
        "theorists": "ادوین لاک؛ گری لتم",
        "theorists_text": "لاک (۱۹۶۸)؛ لاک و لتم (۱۹۹۰)",
        "year": 1968,
        "model": "هدف مشخص و دشوار + توانایی + تعهد + بازخورد → جهت‌دهی، تلاش، پایداری، راهبرد → عملکرد؛ در تکالیف پیچیده، هدف یادگیری.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nلاک رفتار کاری را از انگیزه درونی به هدف آگاهانه گره زد و نشان داد وضوح و دشواری هدف، عملکرد را پیش‌بینی می‌کند. نوآوری چارچوب، تبدیل انگیزش به سازوکاری قابل طراحی است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با تعیین هدف، اندازه‌گیری عملکرد و تحلیل تعدیل‌گرها انجام می‌شود. پژوهشی که تنها سطح هدف را می‌سنجد، تعهد و بازخورد را از دست می‌دهد؛ و پژوهشی که هدف سخت بی توانایی می‌دهد، سرخوردگی را با انگیزش اشتباه می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در طراحی سنجه تحریریه است، اما باید با اخلاق حرفه‌ای تکمیل شود. هدف کلیک بی سنجه کیفیت، مأموریت رسانه را به بهینه‌سازی تعامل تقلیل می‌دهد.",
        "critique_text": "\n".join([
            "۱. کوته‌بینی: ابعاد ناسنجیده نادیده می‌ماند.",
            "۲. رفتار ناسالم: هدف سخت، تقلب را برمی‌انگیزد.",
            "۳. پیچیدگی تکلیف: هدف عملکردی به خلاقیت آسیب می‌زند.",
            "۴. تعمیم: شواهد از تکالیف ساده است.",
            "۵. سنجه رسانه: هدف کلیک، کیفیت را قربانی می‌کند.",
        ]),
        "example_text": "سایت خبری برای خبرنگاران هدف تعداد بازدید می‌گذارد؛ تیترها به طعمه‌کلیک بدل می‌شوند و اعتماد مخاطب افت می‌کند. افزودن هدف کیفیت و بازخورد تحریریه، مسیر رفتار را عوض می‌کند.",
    },
    "MC-617": {
        "summary": "(اسکینر، ۱۹۳۸؛ ۱۹۵۳) نظریه تقویت می‌گوید رفتار را پیامدهای آن شکل می‌دهد: رفتاری که پاداش بگیرد تکرار می‌شود و رفتاری که تقویت نشود یا تنبیه شود کاهش می‌یابد. اسکینر این را شرطی‌سازی کنشگر نامید و تقویت را به مثبت، منفی، تنبیه و خاموشی تقسیم کرد. برنامه‌های تقویت، الگوی پایداری رفتار را تعیین می‌کنند. در ارتباطات، این چارچوب توضیح می‌دهد چرا عادت‌های رسانه‌ای شکل می‌گیرند و چرا رسانه می‌تواند نگرش موجود را تقویت کند.",
        "definition": "نظریه تقویت، چارچوبی رفتاری است که تغییر رفتار را تابع پیامدهای آن می‌داند و با تقویت مثبت و منفی، تنبیه و خاموشی و برنامه‌های تقویت، احتمال تکرار رفتار را توضیح می‌دهد.",
        "main_problem": "مسئله این است که چرا رفتار بدون تصمیم آگاهانه تکرار می‌شود. پاسخ اسکینر، پیامد است نه انگیزه درونی. پرسش دوم، مرز است: تقویت رسانه‌ای چه زمانی یادگیری است و چه زمانی شکل‌دهی پنهان رفتار.",
        "mechanism": "۱. تقویت مثبت: افزودن پیامد خوشایند پس از رفتار، احتمال تکرار آن را بالا می‌برد.\n۲. تقویت منفی: حذف محرک ناخوشایند پس از رفتار، همین اثر را دارد و با تنبیه یکی نیست.\n۳. تنبیه: افزودن محرک ناخوشایند رفتار را سرکوب می‌کند اما رفتار جانشین نمی‌سازد.\n۴. خاموشی: حذف تقویت، رفتار آموخته‌شده را به‌تدریج کم می‌کند.\n۵. برنامه تقویت: تقویت پیوسته یادگیری سریع و تقویت متناوب پایداری بیشتر می‌سازد؛ نسبت متغیر، مقاوم‌ترین الگوی عادت است.\n۶. شکل‌دهی: تقریب‌های متوالی رفتار مطلوب، رفتار پیچیده را گام‌به‌گام می‌سازد.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا کشیدن صفحه و اعلان، عادت می‌شود و چرا الگوریتم با پاداش متغیر، بازگشت مکرر را تقویت می‌کند. مدل تقویت کلپر نیز نشان داد رسانه بیشتر نگرش موجود را تحکیم می‌کند تا تغییر دهد. تبلیغات تجاری هم با پیوند کالا به پاداش عاطفی، ترجیح برند را به‌تدریج تقویت می‌کند. نکته مهم این است که الگوریتم برنامه تقویت را شخصی‌سازی می‌کند و همین، عادت را از انتخاب به اجبار نرم بدل می‌کند.",
        "assumptions": [
            "رفتار را پیامد قابل مشاهده شکل می‌دهد.",
            "تقویت، احتمال تکرار را تغییر می‌دهد.",
            "برنامه تقویت، پایداری رفتار را تعیین می‌کند.",
        ],
        "principles": [
            "پیامد نزدیک، مؤثرتر از توضیح دور است.",
            "تقویت متناوب، عادت پایدارتر می‌سازد.",
            "تنبیه، رفتار جانشین نمی‌سازد.",
        ],
        "critiques": [
            "۱. کم‌توجهی به معنا: تفسیر و نگرش مخاطب نادیده می‌ماند.\n۲. تعمیم آزمایشگاهی: شواهد از حیوان و تکلیف ساده می‌آید.\n۳. اخلاق اقناع: تقویت پنهان، مرز دستکاری را مبهم می‌کند.\n۴. نادیده‌گرفتن شناخت: باور و تفسیر در مدل جای محدودی دارد.\n۵. سنجش عادت رسانه‌ای: نسبت دادن عادت به برنامه تقویت دشوار است.",
        ],
        "applications": [
            "طراحی محصول: تحلیل حلقه پاداش و اعلان.",
            "سواد رسانه‌ای: آگاه‌سازی از سازوکار عادت.",
            "تبلیغات: پیوند پیام با پاداش ادراک‌شده.",
            "پژوهش اثر رسانه: تحلیل تقویت نگرش موجود.",
        ],
        "evolution": "اسکینر در ۱۹۳۸ شرطی‌سازی کنشگر را با آزمایش‌های حیوانی بنیاد گذاشت و در ۱۹۵۳ آن را در کتابی درباره علم رفتار انسانی گسترد. این چارچوب به آموزش برنامه‌ریزی‌شده و طراحی رفتار راه یافت و در ارتباطات با مدل تقویت کلپر و بعدها با نقد پلتفرم‌های پاداش متغیر پیوند خورد.",
        "key_concepts": [
            "شرطی‌سازی کنشگر (Operant Conditioning)",
            "تقویت مثبت (Positive Reinforcement)",
            "تقویت منفی (Negative Reinforcement)",
            "تنبیه (Punishment)",
            "خاموشی (Extinction)",
            "برنامه تقویت متغیر (Variable Reinforcement Schedule)",
        ],
        "studies": [
            "Skinner, B. F. (1938). The behavior of organisms. Appleton-Century.",
            "Skinner, B. F. (1953). Science and human behavior. Macmillan.",
        ],
        "theorists": "بی. اف. اسکینر",
        "theorists_text": "بی. اف. اسکینر (۱۹۳۸؛ ۱۹۵۳)",
        "year": 1938,
        "model": "محیط → رفتار → پیامد (تقویت، تنبیه، خاموشی) → احتمال تکرار رفتار؛ برنامه تقویت، پایداری رفتار را تعیین می‌کند.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nاسکینر رفتار را از انگیزه درونی جدا کرد و انتخاب رفتار را به پیامدهای آن سپرد. نوآوری چارچوب، تبدیل یادگیری به فرایندی قابل مشاهده و قابل طراحی است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با مشاهده نرخ پاسخ و تغییر برنامه تقویت انجام می‌شود. پژوهشی که تنها نگرش را می‌سنجد، رفتار را از دست می‌دهد؛ و پژوهشی که عادت را بی تحلیل برنامه تقویت می‌خواند، سازوکار را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در توضیح عادت و تکرار است، اما باید با تحلیل معنا تکمیل شود. مخاطب، پیام را تفسیر می‌کند و تقویت بی معنا، رفتار پایدار نمی‌سازد.",
        "critique_text": "\n".join([
            "۱. کم‌توجهی به معنا: تفسیر مخاطب نادیده می‌ماند.",
            "۲. تعمیم آزمایشگاهی: شواهد از تکلیف ساده است.",
            "۳. اخلاق اقناع: تقویت پنهان، دستکاری است.",
            "۴. نادیده‌گرفتن شناخت: باور جای محدودی دارد.",
            "۵. سنجش عادت: نسبت دادن عادت به تقویت دشوار است.",
        ]),
        "example_text": "کاربری که هر بار پس از باز کردن برنامه، اعلان تازه می‌بیند، بازگشت مکرر را یاد می‌گیرد. پاداش نامنظم و غیرقابل پیش‌بینی، عادت را پایدارتر از پاداش ثابت می‌کند.",
    },
    "MC-618": {
        "summary": "(مک‌کللند، ۱۹۶۱) نظریه نیازهای اکتسابی می‌گوید سه انگیزه در تعامل با فرهنگ و تجربه آموخته می‌شوند: نیاز به پیشرفت، نیاز به قدرت و نیاز به پیوند. مک‌کللند با تحلیل داستان‌های تصویری، شدت این نیازها را در افراد و جوامع سنجید و نشان داد نیاز پیشرفت با کارآفرینی و رشد اقتصادی پیوند دارد. نیاز قدرت با رهبری و نفوذ و نیاز پیوند با هماهنگی اجتماعی رابطه دارد. برخلاف هرم مازلو، نیازها ذاتی و مرتب نیستند؛ آموخته می‌شوند و هم‌زمان فعال می‌مانند.",
        "definition": "نظریه نیازهای اکتسابی، مدلی است که سه انگیزه آموخته‌شده پیشرفت، قدرت و پیوند را از هم تفکیک می‌کند و رفتار فرد و جامعه را بر پایه شدت این نیازها توضیح می‌دهد.",
        "main_problem": "مسئله این است که چرا افراد در موقعیت یکسان به پاداش‌های متفاوت پاسخ می‌دهند و چرا برخی جوامع کارآفرین‌ترند. پاسخ، شدت نیازهای آموخته‌شده است. پرسش دوم، سنجش است: آیا می‌توان نیاز ناخودآگاه را از روایت فرد خواند.",
        "mechanism": "۱. نیاز پیشرفت: میل به انجام کار بهتر، حل مسئله با دشواری متوسط و دریافت بازخورد روشن.\n۲. نیاز قدرت: میل به نفوذ، کنترل منابع و اثرگذاری بر دیگران.\n۳. نیاز پیوند: میل به پذیرش، همدلی و رابطه گرم با دیگران.\n۴. سنجش روایتی: داستان‌های مبهم، محتوای ناخودآگاه انگیزه را بیرون می‌کشند و شدت نیاز را کد می‌کنند.\n۵. یادگیری فرهنگی: خانواده، مدرسه و ارزش‌های جامعه، شدت این نیازها را شکل می‌دهند.\n۶. ترکیب نیازها: افراد ترکیبی از سه نیاز دارند و رفتار از تعامل شدت آن‌ها می‌آید.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا محتوای خودسازی و موفقیت جذب می‌شود، چرا ارتباطات سیاسی بر جذابیت قدرت و منزلت تکیه می‌کند و چرا پلتفرم‌های اجتماعی نیاز پیوند را برجسته می‌سازند. نکته مهم این است که رسانه می‌تواند نیاز را برجسته کند اما نمی‌تواند آن را از هیچ بسازد؛ پیام هم‌خوان با نیاز موجود، اثر بیشتری دارد.",
        "assumptions": [
            "نیازهای پیشرفت، قدرت و پیوند آموخته می‌شوند.",
            "شدت نیازها میان افراد متفاوت است.",
            "روایت فرد، دسترسی به انگیزه ناخودآگاه می‌دهد.",
        ],
        "principles": [
            "نیاز آموخته‌شده، قابل تغییر است.",
            "پیام هم‌خوان با نیاز، اثر بیشتری دارد.",
            "سه نیاز هم‌زمان فعال می‌شوند.",
        ],
        "critiques": [
            "۱. پایایی سنجش: کدگذاری روایت، وابسته به داور و آموزش است.\n۲. تعمیم اقتصادی: پیوند نیاز پیشرفت و رشد اقتصادی یکدست نبود.\n۳. سوگیری نمونه: نمونه‌های نخست عمدتاً مردان مدیر بودند.\n۴. فروکاست: سه نیاز، تنوع انگیزه انسانی را کم برآورد می‌کند.\n۵. تغییر زمینه: نیاز پیوند در پلتفرم‌های اجتماعی صورتی تازه یافته است.",
        ],
        "applications": [
            "تبلیغات: تطبیق پیام با نیاز غالب مخاطب.",
            "ارتباطات سیاسی: تحلیل جذابیت قدرت و منزلت.",
            "توسعه کارآفرینی: آموزش و تقویت انگیزه پیشرفت.",
            "پژوهش مخاطب: بخش‌بندی بر پایه انگیزه غالب.",
        ],
        "evolution": "مک‌کللند در ۱۹۶۱ نظریه را در کتاب جامعه دستیابنده ارائه کرد و در دهه‌های بعد ابزار سنجش و برنامه‌های آموزش انگیزه را گسترد. مدل او به پژوهش کارآفرینی، رهبری و ارتباطات راه یافت و با نقد پایایی سنجش روایتی روبه‌رو شد.",
        "key_concepts": [
            "نیاز پیشرفت (Need for Achievement)",
            "نیاز قدرت (Need for Power)",
            "نیاز پیوند (Need for Affiliation)",
            "سنجش روایتی (Thematic Apperception Test)",
            "انگیزه آموخته‌شده (Learned Motive)",
            "کارآفرینی (Entrepreneurship)",
        ],
        "studies": [
            "McClelland, D. C. (1961). The achieving society. D. Van Nostrand.",
            "McClelland, D. C. (1987). Human motivation. Cambridge University Press.",
        ],
        "theorists": "دیوید مک‌کللند",
        "theorists_text": "دیوید مک‌کللند (۱۹۶۱؛ ۱۹۸۷)",
        "year": 1961,
        "model": "سه نیاز آموخته: پیشرفت + قدرت + پیوند → شدت متفاوت → رفتار کارآفرینانه، رهبری و پیوندی.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nمک‌کللند انگیزه را از غریزه به یادگیری فرهنگی منتقل کرد و سه نیاز را به رفتار اقتصادی و رهبری گره زد. نوآوری چارچوب، سنجش انگیزه ناخودآگاه از روایت است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با تحلیل داستان‌های مبهم و کدگذاری محتوای پیشرفت، قدرت و پیوند انجام می‌شود. پژوهشی که تنها پرسش‌نامه خودگزارشی را می‌سنجد، انگیزه ناخودآگاه را از دست می‌دهد؛ و پژوهشی که کدگذار را آموزش نمی‌دهد، پایایی را قربانی می‌کند.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در بخش‌بندی پیام است، اما باید با تحلیل زمینه تکمیل شود. نیاز آموخته‌شده در فرهنگ شکل می‌گیرد و پیام رسانه‌ای بی هم‌خوانی فرهنگی اثر محدودی دارد.",
        "critique_text": "\n".join([
            "۱. پایایی سنجش: کدگذاری روایت به داور وابسته است.",
            "۲. تعمیم اقتصادی: پیوند با رشد اقتصادی یکدست نیست.",
            "۳. سوگیری نمونه: نمونه‌ها عمدتاً مردان مدیر بودند.",
            "۴. فروکاست: سه نیاز تنوع انگیزه را کم برآورد می‌کند.",
            "۵. تغییر زمینه: نیاز پیوند صورتی تازه یافته است.",
        ]),
        "example_text": "کارآفرینی که بازخورد روشن از فروش می‌گیرد، انگیزه پیشرفت را تقویت می‌کند؛ در حالی که همکاری که پذیرش گروه را برنده‌ترین پاداش می‌داند، به شبکه رابطه روی می‌آورد. تفاوت رفتار از شدت نیاز آموخته می‌آید.",
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
                                       "verified": n_verified, "batch": 100}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH100 THEORY DONE")


if __name__ == "__main__":
    main()
