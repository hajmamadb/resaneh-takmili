# -*- coding: utf-8 -*-
"""Batch 89: full documentation for MC-482, MC-483, MC-485, MC-486."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch89-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch89_theory.json"

S = {
    "MC-482": [
        dict(kind="BOOK",
             title_en="Mythologies",
             title_fa="اسطوره‌شناسی‌ها",
             authors="Barthes, R.; Lavers, A. (Trans.)", year=1972,
             publisher="Hill and Wang",
             doi=None, url=None, language="en", isbn=None,
             citation="Barthes, R. (1972). Mythologies (A. Lavers, Trans.). Hill and Wang. (Original work published 1957)",
             locator="Myth Today", locator_type="CHAPTER",
             supports="myth as second-order signification / naturalization / depoliticized speech", verified=True),
        dict(kind="BOOK",
             title_en="Image, Music, Text",
             title_fa="تصویر، موسیقی، متن",
             authors="Barthes, R.; Heath, S. (Trans.)", year=1977, publisher="Fontana",
             doi=None, url=None, language="en", isbn=None,
             citation="Barthes, R. (1977). Image, music, text (S. Heath, Trans.). Fontana.",
             locator="work", locator_type="work",
             supports="denotation and connotation / rhetoric of the image", verified=False),
    ],
    "MC-483": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Principles of Critical Discourse Analysis",
             title_fa="اصول تحلیل انتقادی گفتمان",
             authors="van Dijk, T. A.", year=1993,
             publisher="Discourse & Society",
             doi="10.1177/0957926593004002006", url=None, language="en", isbn=None,
             citation="van Dijk, T. A. (1993). Principles of critical discourse analysis. Discourse & Society, 4(2), 249-283. https://doi.org/10.1177/0957926593004002006",
             locator="4(2):249-283", locator_type="page_range",
             supports="social cognition / ideological square / access to discourse as power", verified=True),
        dict(kind="BOOK",
             title_en="Critical Discourse Analysis: The Critical Study of Language",
             title_fa="تحلیل انتقادی گفتمان: مطالعه انتقادی زبان",
             authors="Fairclough, N.", year=1995, publisher="Longman",
             doi=None, url=None, language="en", isbn=None,
             citation="Fairclough, N. (1995). Critical discourse analysis: The critical study of language. Longman.",
             locator="work", locator_type="work",
             supports="three-dimensional model / intertextuality / orders of discourse", verified=False),
    ],
    "MC-485": [
        dict(kind="BOOK",
             title_en="Is There a Text in This Class? The Authority of Interpretive Communities",
             title_fa="آیا در این کلاس متنی وجود دارد؟ اقتدار جماعت‌های تفسیری",
             authors="Fish, S.", year=1980, publisher="Harvard University Press",
             doi=None, url=None, language="en", isbn=None,
             citation="Fish, S. (1980). Is there a text in this class? The authority of interpretive communities. Harvard University Press.",
             locator="work", locator_type="work",
             supports="interpretive strategies / meaning as product of interpretive communities", verified=True),
        dict(kind="BOOK",
             title_en="Doing What Comes Naturally: Change, Rhetoric, and the Practice of Theory in Literary and Legal Studies",
             title_fa="انجام آنچه طبیعی می‌نماید: تغییر، بلاغت و عمل نظریه در مطالعات ادبی و حقوقی",
             authors="Fish, S.", year=1989, publisher="Duke University Press",
             doi=None, url=None, language="en", isbn=None,
             citation="Fish, S. (1989). Doing what comes naturally: Change, rhetoric, and the practice of theory in literary and legal studies. Duke University Press.",
             locator="work", locator_type="work",
             supports="extension of interpretive community to law and professional practice", verified=False),
    ],
    "MC-486": [
        dict(kind="BOOK",
             title_en="Audiences: A Sociological Theory of Performance and Imagination",
             title_fa="مخاطبان: نظریه جامعه‌شناختی نمایش و تخیل",
             authors="Abercrombie, N.; Longhurst, B.", year=1998, publisher="Sage",
             doi=None, url="https://sk.sagepub.com/book/mono/audiences/toc",
             language="en", isbn=None,
             citation="Abercrombie, N., & Longhurst, B. (1998). Audiences: A sociological theory of performance and imagination. Sage.",
             locator="work", locator_type="work",
             supports="simple / mass / diffused audience / spectacle-performance paradigm", verified=True),
        dict(kind="BOOK",
             title_en="The 'Nationwide' Audience: Structure and Decoding",
             title_fa="مخاطب برنامه «سراسری»: ساختار و رمزگشایی",
             authors="Morley, D.", year=1980, publisher="British Film Institute",
             doi=None, url=None, language="en", isbn=None,
             citation="Morley, D. (1980). The 'Nationwide' audience: Structure and decoding. British Film Institute.",
             locator="work", locator_type="work",
             supports="socially structured decoding / audience research tradition", verified=False),
    ],
}

ENRICH = {
    "MC-482": {
        "summary": "(بارت، ۱۹۵۷) بارت در «اسطوره‌شناسی‌ها» نشان داد که فرهنگ عامه بورژوایی، نشانه‌های تاریخی و ایدئولوژیک را طبیعی و بدیهی جلوه می‌دهد. او در مقاله «اسطوره امروز» نظام دوسطحی دلالت را معرفی می‌کند: در سطح نخست، نشانه به امری ارجاع می‌دهد؛ در سطح دوم، همان نشانه به دالِ مفهومی ایدئولوژیک بدل می‌شود. اسطوره، گفتارِ مسلحانه‌ای است که تاریخ را از چیزها می‌زداید و آنچه ساخته شده را چون طبیعت عرضه می‌کند. تحلیل نشانه‌شناختی، وظیفه بازگرداندن این تاریخ پنهان را بر عهده دارد.",
        "definition": "اسطوره، نظام دلالت ثانویه است: یک نشانه کامل از سطح نخست، در سطح دوم به دال مفهومی ایدئولوژیک بدل می‌شود. نتیجه این فرایند «طبیعی‌سازی» است؛ یعنی تبدیل امر تاریخی، سیاسی و برساخته به امری بدیهی و بی‌نیاز از توضیح.",
        "main_problem": "مسئله این است که چرا معنای ایدئولوژیک پیام‌های روزمره — از تبلیغات تا خبر و سرگرمی — بدیهی به نظر می‌رسد و کمتر پرسش می‌شود. بارت پاسخ می‌دهد که اسطوره با دو سطح دلالت کار می‌کند و در سطح دوم، تاریخ و منافع را از نشانه می‌زداید. پرسش دوم، امکان نقد است: چگونه تحلیل می‌تواند اسطوره را بخواند، در حالی که خود تحلیلگر نیز درون همان رمزگان فرهنگی می‌اندیشد.",
        "mechanism": "۱. نظام دوسطحی دلالت: در سطح نخست (دلالت صریح)، نشانه به مرجعی ارجاع می‌دهد؛ در سطح دوم (دلالت ضمنی و اسطوره)، همین نشانه به دالِ مفهومی تازه بدل می‌شود.\n۲. اسطوره به‌عنوان شکل، نه محتوا: هر چیزی می‌تواند اسطوره شود؛ اسطوره مقوله‌ای از محتوا نیست، بلکه شیوه‌ای از عرضه و شکل‌دهی است.\n۳. طبیعی‌سازی: اسطوره تاریخ را به طبیعت بدل می‌کند؛ آنچه در زمان ساخته شده، به‌صورت امری جاودان و بدیهی عرضه می‌شود.\n۴. تخلیه سیاست: بارت اسطوره را «گفتارِ غیرسیاسی‌شده» می‌داند؛ اسطوره بار سیاسی و تاریخی مفهوم را می‌زداید و آن را بی‌طرف جلوه می‌دهد.\n۵. رمزگان فرهنگی: خوانش متن به رمزگان مشترک فرهنگی وابسته است؛ معنا نه در متن تنها، بلکه در برخورد متن با رمزگان خواننده ساخته می‌شود.\n۶. شکستن اسطوره: تحلیل نشانه‌شناختی، اسطوره را «بازمسیسی» می‌کند و تاریخ ازدست‌رفته را به آن بازمی‌گرداند؛ همین بازگرداندن، کار انتقادی تحلیل است.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا بازنمایی‌های تبلیغاتی از خانواده، موفقیت یا زیبایی، طبیعی و جهان‌شمول جلوه می‌کنند و چرا خبر، برخی رویدادها را بدیهی و برخی را استثنا نشان می‌دهد. نکته مهم این است که اسطوره دروغ نیست؛ تحریف نسبت تاریخی و سیاسی مفهوم در قالب بدیهی است.",
        "assumptions": [
            "نشانه‌ها نظامی دوسطحی از دلالت می‌سازند.",
            "فرهنگ عامه، میدان تولید اسطوره‌های ایدئولوژیک است.",
            "تحلیل نشانه‌شناختی می‌تواند لایه طبیعی‌شده معنا را آشکار کند.",
        ],
        "principles": [
            "اسطوره، تاریخ را به طبیعت بدل می‌کند.",
            "معنای ایدئولوژیک از راه شکل و عرضه، نه فقط محتوا، ساخته می‌شود.",
            "تحلیل انتقادی، بار سیاسی نشانه را بازمی‌گرداند.",
        ],
        "critiques": [
            "۱. خوانش نخبه‌گرا: تحلیل بارت اغلب مخاطب عام را فریب‌خورده فرض می‌کند و قرائت‌های مقاومتی را نمی‌بیند.\n۲. نمونه‌گزینی: شواهد از فرهنگ فرانسه دهه ۱۹۵۰ و طبقه متوسط شهری می‌آید.\n۳. ناپایداری مرز: تفکیک دلالت صریح از ضمنی در عمل روشن و باثبات نیست.\n۴. مسئله معیار: اگر همه فرهنگ اسطوره‌ای است، معیار تحلیلگر برای ایستادن بیرون از اسطوره چیست.\n۵. تحول نظری: بارت خود بعدها از ساختارگرایی فاصله گرفت و بر متن خواندنی/نوشتنی و نقش فعال خواننده تأکید کرد.",
        ],
        "applications": [
            "تحلیل تبلیغات: آشکارسازی طبیعی‌سازی ارزش‌ها و سبک زندگی در پیام تجاری.",
            "نقد خبر: بررسی چگونگی عرضه رویدادها به‌عنوان بدیهی یا استثنا.",
            "مطالعات بازنمایی: تحلیل اسطوره‌های جنسیت، خانواده و موفقیت در رسانه.",
            "سواد رسانه‌ای: آموزش خوانش دوسطحی پیام و پرسش از تاریخ پنهان آن.",
        ],
        "evolution": "بارت مقاله‌های کوتاه را در دهه ۱۹۵۰ نوشت و در ۱۹۵۷ با مقاله نظری «اسطوره امروز» منتشر کرد. او بعدها در «تصویر، موسیقی، متن» و «S/Z» از ساختارگرایی به پساساختارگرایی گرایید و بر نقش فعال خواننده تأکید کرد.",
        "key_concepts": [
            "اسطوره (Myth)",
            "دلالت صریح و ضمنی (Denotation and Connotation)",
            "طبیعی‌سازی (Naturalization)",
            "گفتار غیرسیاسی‌شده (Depoliticized Speech)",
            "رمزگان (Code)",
            "نظام دلالت ثانویه (Second-Order Signification)",
        ],
        "studies": [
            "Barthes, R. (1972). Mythologies (A. Lavers, Trans.). Hill and Wang.",
            "Barthes, R. (1977). Image, music, text (S. Heath, Trans.). Fontana.",
        ],
        "theorists": "رولان بارت (۱۹۵۷)",
        "theorists_text": "رولان بارت (۱۹۵۷)",
        "year": 1957,
        "model": "مدل دوسطحی: نشانه سطح اول (دال + مدلول) → تبدیل کل نشانه به دال سطح دوم → مفهوم اسطوره‌ای → طبیعی‌سازی و تخلیه سیاست.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nبارت ابزار نشانه‌شناسی سوسور را به نقد فرهنگ عامه گره زد. نوآوری او این بود که ایدئولوژی را نه در محتوای پیام، بلکه در سازوکار شکل‌دهی و طبیعی‌سازی نشانه جست‌وجو کرد؛ ایده‌ای که پایه نقد فرهنگی و مطالعات بازنمایی شد.\n\n۲. منطق سنجش و دام‌های آن\nتحلیل اسطوره‌شناختی نیازمند نشان دادن زنجیره دلالت است: از نشانه سطح اول تا مفهوم سطح دوم و سپس پیامد طبیعی‌سازی. خطای رایج، اعلام ایدئولوژیک بودن پیام بدون نشان دادن سازوکار آن است؛ روش مناسب، بازسازی مسیر دلالت و مقایسه با صورت‌بندی‌های جایگزین است.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در آشکارسازی لایه پنهان پیام است، اما باید از نخبه‌گرایی و فرض مخاطب منفعل پرهیز کرد. مخاطب امروز خود تولیدکننده اسطوره است؛ از این رو تحلیل باید هم تولید و هم دریافت اسطوره را در نظر بگیرد.",
        "critique_text": "\n".join([
            "۱. خوانش نخبه‌گرا: مخاطب عام فریب‌خورده فرض می‌شود و قرائت‌های مقاومتی دیده نمی‌شود.",
            "۲. نمونه‌گزینی: شواهد از فرهنگ فرانسه دهه ۱۹۵۰ و طبقه متوسط شهری می‌آید.",
            "۳. ناپایداری مرز: تفکیک دلالت صریح از ضمنی در عمل روشن و باثبات نیست.",
            "۴. مسئله معیار: اگر همه فرهنگ اسطوره‌ای است، معیار ایستادن تحلیلگر بیرون از اسطوره چیست.",
            "۵. تحول نظری: بارت بعدها از ساختارگرایی فاصله گرفت و بر نقش فعال خواننده تأکید کرد.",
        ]),
        "example_text": "در تبلیغ یک برند لوازم خانگی، صحنه‌ای آرام از خانواده‌ای خوشحال در آشپزخانه نشان داده می‌شود. در سطح اول، این تصویر فقط یک خانواده و یک وسیله است؛ در سطح دوم، به دالِ «نظم طبیعی خانواده و نقش زن» بدل می‌شود. اسطوره، تاریخی‌بودن این نقش را می‌زداید و آن را بدیهی جلوه می‌دهد.",
    },
    "MC-483": {
        "summary": "(فرکلاف، ۱۹۹۵؛ ون دایک، ۱۹۹۳) تحلیل انتقادی گفتمان، زبان را نه آیینه واقعیت، بلکه کنش اجتماعی و ابزار قدرت می‌داند. فرکلاف مدل سه‌بعدی متن، عمل گفتمانی و عمل اجتماعی را پیشنهاد کرد و بر بینامتنیت و نظم گفتمان تأکید کرد. ون دایک با مفهوم شناخت اجتماعی نشان داد که بازنمایی‌های ذهنی مشترک، حلقه واسط میان گفتمان و ساختار اجتماعی‌اند و نخبگان نمادین از راه کنترل دسترسی به گفتمان، قدرت را بازتولید می‌کنند. وداک با رویکرد تاریخی-گفتمانی، بافت را در چند سطح و راهبردهای نام‌دهی و استدلال را در تحلیل وارد کرد.",
        "definition": "تحلیل انتقادی گفتمان، چارچوبی میان‌رشته‌ای برای مطالعه نظام‌مند متن، گفتار و ارتباط است که هدفش آشکارسازی روابط قدرت، ایدئولوژی و نابرابری در ساختارهای زبانی و اجتماعی است؛ «انتقادی» بودن به معنای موضع صریح در برابر سلطه و بی‌عدالتی است.",
        "main_problem": "مسئله این است که چگونه قدرت و ایدئولوژی در متن پنهان می‌شوند و تحلیل چه ابزاری برای آشکارسازی آن‌ها دارد. پاسخ در پیوند سه سطح است: ساختار زبانی متن، رویه‌های تولید و مصرف گفتمان، و ساختار اجتماعی که گفتمان در آن عمل می‌کند. پرسش دوم، مسئله عینیت است: آیا تحلیلگر می‌تواند هم‌زمان موضع انتقادی داشته باشد و از تحلیل سوگیرانه بپرهیزد.",
        "mechanism": "۱. زبان به‌عنوان کنش اجتماعی: گفتمان نه توصیف بی‌طرف جهان، بلکه عملی است که روابط اجتماعی و هویت‌ها را می‌سازد و بازتولید می‌کند.\n۲. مدل سه‌بعدی فرکلاف: هر رخداد گفتمانی سه وجه دارد — متن، عمل گفتمانی (تولید، توزیع و مصرف) و عمل اجتماعی؛ تحلیل معتبر باید هر سه را در نظر بگیرد.\n۳. بینامتنیت و نظم گفتمان: متن‌ها به متن‌های دیگر ارجاع می‌دهند و مجموعه‌ای از ژانرها و گفتارها، فضای ممکن بیان را محدود می‌کند.\n۴. شناخت اجتماعی ون دایک: میان ساختار اجتماعی و متن، بازنمایی‌های ذهنی مشترک قرار دارند؛ ایدئولوژی در این بازنمایی‌ها سازمان می‌یابد.\n۵. مربع ایدئولوژیک: گفتمان غالب اغلب خوبی‌های «ما» و بدی‌های «آن‌ها» را برجسته و عکس آن را کم‌رنگ می‌کند؛ سازوکاری که در خبر و تبلیغ سیاسی دیده می‌شود.\n۶. دسترسی به گفتمان: قدرت یعنی کنترل دسترسی به متن، تولید آن و توزیع آن؛ نخبگان نمادین همین کنترل را بازتولید می‌کنند.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا واژه‌گزینی خبری، منبع‌دهی و ترتیب روایت، معنای سیاسی می‌سازد و چرا برخی صداها در فضای عمومی شنیده نمی‌شوند. نکته مهم این است که تحلیل انتقادی نباید به جست‌وجوی ایدئولوژی در هر جمله فروکاسته شود؛ هدف، نشان دادن الگوهای نظام‌مند و پیامدهای اجتماعی آن‌هاست.",
        "assumptions": [
            "گفتمان، عمل اجتماعی و نه صرفاً انتقال اطلاعات است.",
            "روابط قدرت در ساختارهای زبانی قابل ردیابی‌اند.",
            "تحلیل انتقادی باید موضعی صریح در برابر سلطه داشته باشد.",
        ],
        "principles": [
            "تحلیل معتبر، متن و بافت اجتماعی را هم‌زمان می‌بیند.",
            "کنترل دسترسی به گفتمان، شکلی از قدرت است.",
            "ایدئولوژی از راه الگوهای نظام‌مند زبانی بازتولید می‌شود.",
        ],
        "critiques": [
            "۱. مسئله عینیت: موضع انتقادی صریح می‌تواند به گزینش شواهد هم‌سو با فرضیه بینجامد.\n۲. نمونه‌گزینی: پژوهش‌ها اغلب متون سیاسی یا خبری خاص را برمی‌گزینند و تعمیم آن‌ها دشوار است.\n۳. کم‌توجهی به دریافت: تحلیل بر تولید متن متمرکز است و تفسیر مخاطب کمتر سنجیده می‌شود.\n۴. ناهمگونی روش: سه سنت فرکلاف، ون دایک و وداک ابزارها و سطوح تحلیل متفاوتی دارند.\n۵. خطر تقلیل: فروکاستن همه گفتمان به ایدئولوژی، پیچیدگی ژانرها و کارکردهای زبان را نادیده می‌گیرد.",
        ],
        "applications": [
            "تحلیل خبر: بررسی واژه‌گزینی، منبع‌دهی و چارچوب‌بندی رویدادها.",
            "نقد گفتمان سیاسی: تحلیل راهبردهای نام‌دهی و استدلال در سخنرانی‌ها.",
            "مطالعات نژاد و جنسیت: ردیابی بازنمایی‌های نابرابر در رسانه.",
            "سواد رسانه‌ای: آموزش خوانش انتقادی متن با پرسش از قدرت و منافع.",
        ],
        "evolution": "CDA در دهه ۱۹۸۰ و ۱۹۹۰ در اروپا شکل گرفت و سه سنت اصلی آن — مدل سه‌بعدی فرکلاف، شناخت اجتماعی ون دایک و رویکرد تاریخی-گفتمانی وداک — در کنار هم رشد کردند. پژوهش بعدی آن را با پیکره‌های بزرگ، تحلیل چندوجهی و رسانه‌های دیجیتال ترکیب کرد.",
        "key_concepts": [
            "تحلیل انتقادی گفتمان (Critical Discourse Analysis)",
            "عمل گفتمانی (Discursive Practice)",
            "بینامتنیت (Intertextuality)",
            "نظم گفتمان (Order of Discourse)",
            "شناخت اجتماعی (Social Cognition)",
            "مربع ایدئولوژیک (Ideological Square)",
        ],
        "studies": [
            "van Dijk, T. A. (1993). Principles of critical discourse analysis. Discourse & Society, 4(2), 249-283.",
            "Fairclough, N. (1995). Critical discourse analysis: The critical study of language. Longman.",
        ],
        "theorists": "نورمن فرکلاف (۱۹۹۵)؛ تون ون دایک (۱۹۹۳)؛ روت وداک (۲۰۰۱)",
        "theorists_text": "نورمن فرکلاف (۱۹۹۵)؛ تون ون دایک (۱۹۹۳)؛ روت وداک (۲۰۰۱)",
        "year": 1995,
        "model": "مدل سه‌سطحی: متن (ساختار زبانی) → عمل گفتمانی (تولید، توزیع، مصرف) → عمل اجتماعی (روابط قدرت و نهادها)؛ با واسطه شناخت اجتماعی و ایدئولوژی.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nCDA از پیوند زبان‌شناسی انتقادی، نظریه اجتماعی و مطالعات فرهنگی شکل گرفت. ادعای مرکزی آن این است که انتخاب‌های زبانی بی‌طرف نیستند و الگوهای نظام‌مند آن‌ها، روابط قدرت را بازتولید می‌کند؛ از این رو تحلیل زبان، بخشی از نقد اجتماعی است.\n\n۲. منطق سنجش و دام‌های آن\nتحلیل معتبر نیازمند دو چیز است: نمایش الگوی نظام‌مند (نه نمونه‌های پراکنده) و پیوند آن با بافت نهادی و اجتماعی. خطای رایج، انتخاب جمله‌ای تکان‌دهنده و نتیجه‌گیری درباره ایدئولوژی کل رسانه است؛ روش مناسب، تحلیل پیکره، مقایسه منابع رقیب و شفاف‌سازی معیارهای انتخاب است.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در پیوند زبان و قدرت است، اما باید از سوگیری تأییدی و تقلیل‌گرایی پرهیز کند. تحلیل انتقادی مؤثر، هم الگوی سلطه را نشان می‌دهد و هم امکان‌های مقاومت و تغییر گفتمان را می‌بیند.",
        "critique_text": "\n".join([
            "۱. مسئله عینیت: موضع انتقادی صریح می‌تواند به گزینش شواهد هم‌سو با فرضیه بینجامد.",
            "۲. نمونه‌گزینی: پژوهش‌ها اغلب متون سیاسی یا خبری خاص را برمی‌گزینند و تعمیم دشوار است.",
            "۳. کم‌توجهی به دریافت: تحلیل بر تولید متن متمرکز است و تفسیر مخاطب کمتر سنجیده می‌شود.",
            "۴. ناهمگونی روش: سه سنت اصلی ابزارها و سطوح تحلیل متفاوتی دارند.",
            "۵. خطر تقلیل: فروکاستن همه گفتمان به ایدئولوژی، پیچیدگی ژانرها را نادیده می‌گیرد.",
        ]),
        "example_text": "دو خبرگزاری یک اعتراض خیابانی را پوشش می‌دهند؛ یکی از واژه «آشوبگر» و دیگری از «معترض» استفاده می‌کند، یکی صدای پلیس را اول می‌آورد و دیگری صدای معترضان را. هیچ جمله‌ای به‌تنهایی دروغ نیست، اما الگوی واژه‌گزینی و منبع‌دهی، دو چارچوب متفاوت از رویداد می‌سازد.",
    },
    "MC-485": {
        "summary": "(فیش، ۱۹۸۰) فیش در برابر صورت‌گرایی که معنا را در متن می‌جست و در برابر ذهن‌گرایی که آن را به خواننده واگذار می‌کرد، مفهوم جماعت تفسیری را مطرح کرد: معنا محصول راهبردهای تفسیری مشترکی است که اعضای یک جماعت آموخته‌اند. از این رو متن مستقل از تفسیر، شیئی قابل شناسایی نیست؛ متن، پیامد راهبردهایی است که ما با آن به سراغش می‌رویم. تفسیرها درون یک جماعت پایدار و میان جماعت‌ها متفاوت‌اند.",
        "definition": "جماعت تفسیری، گروهی از خوانندگان است که راهبردهای مشترک تفسیر را به کار می‌برند و از این رو به معنایی مشابه می‌رسند. در این چارچوب، اعتبار تفسیر نه از متن به‌تنهایی و نه از ذوق فردی، بلکه از رویه‌های مشترک جماعت برمی‌خیزد.",
        "main_problem": "مسئله این است که اگر متن معنای ذاتی و مستقل ندارد، چرا تفسیرها کاملاً تصادفی و بی‌قاعده نیستند و چگونه می‌توان درباره درستی تفسیرها داوری کرد. پاسخ فیش در اشتراک راهبردهاست: خوانندگان یک جماعت، همان قراردادها را به کار می‌برند و بنابراین به نتایج مشابه می‌رسند. پرسش دوم، مسئله تغییر است: چگونه یک جماعت تفسیری با جماعتی دیگر جایگزین می‌شود و معیارهای خوانش تغییر می‌کند.",
        "mechanism": "۱. متن به‌عنوان پیامد، نه شیء مستقل: آنچه «متن» می‌نامیم، حاصل اعمال راهبردهای تفسیری است؛ بدون این راهبردها، نشانه‌ها بی‌معنا می‌مانند.\n۲. راهبردهای تفسیری آموخته‌شده: خواننده با قراردادهای فرهنگی و آموزشی می‌آموزد چه چیزی را نشانه، چه چیزی را زمینه و چه چیزی را معنای متن بداند.\n۳. جماعت به‌عنوان مرجع اعتبار: معیار درست‌بودن تفسیر، پذیرش آن در جماعت است؛ نه تطابق با متن مستقل.\n۴. پایداری درون‌جماعتی و اختلاف بین‌جماعتی: درون جماعت، تفسیرها نسبتاً پایدارند؛ میان جماعت‌ها، تفاوت‌ها می‌توانند بنیادین باشند.\n۵. برساخته بودن امر ادبی: «ادبی» بودن متن، ویژگی ذاتی آن نیست؛ برساخته جماعتی است که آن را ادبی می‌خواند.\n۶. مسئله معیار و نقد: اگر جماعت معیار باشد، نقد جماعت از درون دشوار می‌شود؛ فیش این را نه نسبی‌گرایی، بلکه جمع‌گرایی رویه‌ای می‌داند.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا طرفداران یک سریال، خوانش مشترکی از شخصیت‌ها می‌سازند، چرا مخاطبان خبری با گرایش‌های متفاوت از یک گزارش معناهای متفاوت می‌گیرند و چرا «ژانر» و «قرارداد» چارچوب تفسیر را تعیین می‌کنند. نکته مهم این است که جماعت تفسیری، مخاطب را نه منفعل و نه آزاد مطلق، بلکه وابسته به رویه‌های مشترک می‌بیند.",
        "assumptions": [
            "متن مستقل از تفسیر، معنای قابل شناسایی ندارد.",
            "راهبردهای تفسیری، آموخته‌شده و مشترک‌اند.",
            "معیار اعتبار تفسیر، رویه‌های جماعت است.",
        ],
        "principles": [
            "معنا محصول راهبرد تفسیری است، نه شیء درون متن.",
            "جماعت تفسیری، پایداری معنا را تأمین می‌کند.",
            "مرز میان خوانش ادبی و غیرادبی، برساخته جماعت است.",
        ],
        "critiques": [
            "۱. خطر نسبی‌گرایی: اگر جماعت معیار باشد، داوری میان جماعت‌ها دشوار می‌شود.\n۲. ابهام مفهوم: تعریف مرزهای جماعت و عضویت در آن روشن نیست.\n۳. کم‌توجهی به قدرت: نقش نهادها و منافع در شکل‌گیری جماعت‌ها کمتر تحلیل می‌شود.\n۴. محافظه‌کاری: تأکید بر رویه‌های مشترک می‌تواند معیارهای مسلط را طبیعی جلوه دهد.\n۵. تعمیم: نظریه در مطالعات ادبی شکل گرفت و انتقال آن به رسانه نیازمند تعدیل است.",
        ],
        "applications": [
            "مطالعه فندام: تحلیل جماعت‌های طرفدار و راهبردهای مشترک تفسیر.",
            "پژوهش مخاطب: بررسی تفاوت خوانش گروه‌های اجتماعی از یک پیام.",
            "تحلیل ژانر: نشان دادن نقش قراردادهای ژانری در تفسیر.",
            "آموزش ادبیات و رسانه: آگاه‌سازی از راهبردهای تفسیری و منشأ آن‌ها.",
        ],
        "evolution": "فیش نظریه را در دهه ۱۹۷۰ در نقد صورت‌گرایی و نظریه خواننده‌محور شکل داد و در ۱۹۸۰ منتشر کرد. بعدها آن را به حقوق و رویه‌های حرفه‌ای گسترد. پژوهش رسانه، مفهوم را با مطالعات مخاطب فعال و جماعت‌های طرفدار پیوند داد.",
        "key_concepts": [
            "جماعت تفسیری (Interpretive Community)",
            "راهبرد تفسیری (Interpretive Strategy)",
            "متن به‌عنوان پیامد (Text as Consequence)",
            "بلاغت خواننده‌محور (Affective Stylistics)",
            "قرارداد تفسیری (Interpretive Convention)",
            "جمع‌گرایی رویه‌ای (Procedural Collectivism)",
        ],
        "studies": [
            "Fish, S. (1980). Is there a text in this class? The authority of interpretive communities. Harvard University Press.",
            "Fish, S. (1989). Doing what comes naturally. Duke University Press.",
        ],
        "theorists": "استنلی فیش (۱۹۸۰)",
        "theorists_text": "استنلی فیش (۱۹۸۰)",
        "year": 1980,
        "model": "مدل سه‌جزئی: راهبردهای تفسیری مشترک → جماعت تفسیری → پایداری معنا درون جماعت و تفاوت میان جماعت‌ها؛ متن به‌عنوان پیامد تفسیر.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nفیش در جدال با صورت‌گرایی و نظریه‌های خواننده‌محور افراطی، راه سومی پیشنهاد کرد: معنا نه در متن نهفته است و نه از ذهن آزاد خواننده می‌آید، بلکه از راهبردهای مشترکی می‌آید که خواننده از جماعت خود آموخته است. این ایده، پایه اجتماعی نظریه دریافت شد.\n\n۲. منطق سنجش و دام‌های آن\nسنجش تجربی این چارچوب نیازمند شناسایی راهبردهای تفسیری و مرزهای جماعت است. پژوهش‌هایی که تنها تفاوت تفسیرها را گزارش می‌کنند، وجود جماعت را ثابت نمی‌کنند؛ و پژوهش‌هایی که تنها اشتراک تفسیر را نشان می‌دهند، نقش تفاوت‌های درون‌جماعتی را نادیده می‌گیرند.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در نشان دادن اجتماعی‌بودن معناست، اما باید با تحلیل قدرت و نهاد تکمیل شود. جماعت‌ها در خلأ شکل نمی‌گیرند؛ آموزش، رسانه و بازار، دسترسی به راهبردهای تفسیری را نامتقارن می‌کنند.",
        "critique_text": "\n".join([
            "۱. خطر نسبی‌گرایی: اگر جماعت معیار باشد، داوری میان جماعت‌ها دشوار می‌شود.",
            "۲. ابهام مفهوم: تعریف مرزهای جماعت و عضویت در آن روشن نیست.",
            "۳. کم‌توجهی به قدرت: نقش نهادها و منافع در شکل‌گیری جماعت‌ها کمتر تحلیل می‌شود.",
            "۴. محافظه‌کاری: تأکید بر رویه‌های مشترک می‌تواند معیارهای مسلط را طبیعی جلوه دهد.",
            "۵. تعمیم: نظریه در مطالعات ادبی شکل گرفت و انتقال آن به رسانه نیازمند تعدیل است.",
        ]),
        "example_text": "دو گروه از بینندگان یک سریال سیاسی، یکی آن را «نقد قدرت» و دیگری «تبلیغ» می‌خوانند؛ هر دو گروه از قراردادهای تفسیری متفاوتی استفاده می‌کنند که در جماعت خود آموخته‌اند. اختلاف آن‌ها بر سر متن نیست، بر سر راهبرد خواندن متن است.",
    },
    "MC-486": {
        "summary": "(آبرکرومبی و لانگ‌هرست، ۱۹۹۸) این نظریه، سه نوع مخاطب را از هم جدا می‌کند: مخاطب ساده که در رویدادی حضوری و مشترک شرکت می‌کند، مخاطب توده‌ای که رسانه پخش او را در خانه‌ها پراکنده می‌کند، و مخاطب پراکنده که در محیط اشباع از رسانه، همیشه و همه‌جا مخاطب است. نویسندگان با الگوی «نمایش/تماشا» استدلال می‌کنند که زندگی روزمره زیبایی‌شناسی شده و مخاطب هم اجراگر است؛ مرز میان اجرا و تماشا فرو ریخته است.",
        "definition": "سه‌گانه مخاطب، گونه‌شناسی تاریخی-اجتماعی مخاطب است: مخاطب ساده (حضور مشترک در رویداد)، مخاطب توده‌ای (دریافت پراکنده و خصوصی رسانه پخش) و مخاطب پراکنده (مواجهه دائمی با رسانه در زندگی روزمره). در نوع سوم، مخاطب بودن وضعیتی فراگیر و اجراگرانه است.",
        "main_problem": "مسئله این است که چارچوب‌های رایج مخاطب — توده منفعل در برابر مخاطب فعال — برای محیط رسانه‌ای فراگیر کافی نیستند. نویسندگان پاسخ می‌دهند که باید مخاطب را در نسبت با شکل رویداد و میزان نفوذ رسانه در زندگی روزمره بازتعریف کرد. پرسش دوم، پیامد فرهنگی است: وقتی همه هم اجراگر و هم تماشاگرند، تجربه رسانه‌ای چه ویژگی تازه‌ای می‌یابد.",
        "mechanism": "۱. مخاطب ساده: مخاطب در رویدادی حضوری و مشترک شرکت می‌کند؛ مرز اجرا و تماشا روشن و مکان رویداد مشخص است.\n۲. مخاطب توده‌ای: رسانه پخش، رویداد را از مکان جدا می‌کند و مخاطبان پراکنده و خصوصی می‌سازد؛ تجربه مشترک کاهش می‌یابد.\n۳. مخاطب پراکنده: در محیط اشباع از رسانه، مواجهه دائمی و بی‌مرز می‌شود؛ فرد در خانه، خیابان و محل کار مخاطب است.\n۴. الگوی نمایش/تماشا: زندگی روزمره زیبایی‌شناسی می‌شود و به عرصه نمایش بدل می‌گردد؛ مصرف، سبک و هویت اجرا می‌شوند.\n۵. مخاطب به‌عنوان اجراگر: فرد هم تماشاگر است و هم اجراگر؛ خودنمایی در شبکه‌های اجتماعی، صورت روشن این هم‌زمانی است.\n۶. نقش تخیل: مخاطب خود را از دید دیگری تصور می‌کند و اجرای خود را بر پایه این تصور تنظیم می‌کند؛ تخیل، حلقه واسط تجربه رسانه‌ای و هویت است.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا مرز میان تولید و مصرف، و میان زندگی خصوصی و اجرای عمومی، فرو ریخته است و چرا مخاطب امروز نه فقط مصرف‌کننده، بلکه اجراگر هویت است. نکته مهم این است که سه‌گانه، مراحل جایگزین نیستند؛ اشکال مخاطب بودن در کنار هم حضور دارند و شدتشان متفاوت است.",
        "assumptions": [
            "شکل رویداد و میزان نفوذ رسانه، نوع مخاطب بودن را تعیین می‌کند.",
            "زندگی روزمره معاصر، عرصه نمایش و زیبایی‌شناسی است.",
            "مخاطب هم‌زمان تماشاگر و اجراگر است.",
        ],
        "principles": [
            "سه نوع مخاطب در کنار هم حضور دارند و جایگزین یکدیگر نیستند.",
            "در محیط رسانه‌ای فراگیر، مخاطب بودن وضعیتی دائمی است.",
            "تخیل، تجربه رسانه‌ای و اجرای هویت را به هم پیوند می‌دهد.",
        ],
        "critiques": [
            "۱. خطی‌بودن ظاهری: سه‌گانه ممکن است مرحله‌ای خوانده شود، در حالی که اشکال مخاطب هم‌زمان‌اند.\n۲. زمینه غربی: نمونه‌ها عمدتاً از جوامع غربی و رسانه‌های فراگیر می‌آید.\n۳. نادیده‌گرفتن نابرابری: دسترسی به ابزار اجرا و دیده‌شدن، نامتوازن است.\n۴. ابهام مخاطب پراکنده: مرز این نوع با مخاطب توده‌ای در عمل روشن نیست.\n۵. تحول پلتفرم: نظریه پیش از شبکه‌های اجتماعی فراگیر نوشته شد و باید با منطق الگوریتم بازخوانی شود.",
        ],
        "applications": [
            "تحلیل شبکه‌های اجتماعی: بررسی هم‌زمانی تماشا و اجرای هویت.",
            "مطالعات رویداد: مقایسه مخاطب ساده رویداد حضوری با پوشش رسانه‌ای آن.",
            "پژوهش مصرف: تحلیل زیبایی‌شناسی‌شدن زندگی روزمره و سبک.",
            "سیاست رسانه‌ای: توجه به مخاطب به‌عنوان تولیدکننده محتوا، نه فقط دریافت‌کننده.",
        ],
        "evolution": "آبرکرومبی و لانگ‌هرست نظریه را در ادامه سنت مطالعات مخاطب و در نقد چارچوب توده‌ای/فعال شکل دادند. پژوهش بعدی آن را با واقعیت تلویزیونی، شبکه‌های اجتماعی و اقتصاد توجه پیوند داد.",
        "key_concepts": [
            "مخاطب ساده (Simple Audience)",
            "مخاطب توده‌ای (Mass Audience)",
            "مخاطب پراکنده (Diffused Audience)",
            "الگوی نمایش/تماشا (Spectacle/Performance Paradigm)",
            "زیبایی‌شناسی‌شدن زندگی روزمره (Aestheticization of Everyday Life)",
            "تخیل (Imagination)",
        ],
        "studies": [
            "Abercrombie, N., & Longhurst, B. (1998). Audiences: A sociological theory of performance and imagination. Sage.",
            "Morley, D. (1980). The 'Nationwide' audience: Structure and decoding. British Film Institute.",
        ],
        "theorists": "نیکلاس آبرکرومبی و برایان لانگ‌هرست (۱۹۹۸)",
        "theorists_text": "نیکلاس آبرکرومبی و برایان لانگ‌هرست (۱۹۹۸)",
        "year": 1998,
        "model": "مدل سه‌گانه: مخاطب ساده → مخاطب توده‌ای → مخاطب پراکنده؛ با گذار به الگوی نمایش/تماشا که در آن زندگی روزمره اجرا و مخاطب، اجراگر می‌شود.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nنویسندگان در نقد دوگانه «توده منفعل/مخاطب فعال» نشان دادند که نوع مخاطب بودن به شکل رویداد و نفوذ رسانه وابسته است. نوآوری آن‌ها افزودن مخاطب پراکنده و پیوند آن با زیبایی‌شناسی‌شدن زندگی روزمره بود؛ ایده‌ای که تجربه رسانه‌ای امروز را بهتر توضیح می‌دهد.\n\n۲. منطق سنجش و دام‌های آن\nسنجش این چارچوب نیازمند تحلیل هم‌زمان نوع مواجهه، مکان تجربه و نقش اجراگری مخاطب است. پژوهش‌هایی که تنها زمان مصرف را می‌سنجند، تفاوت مخاطب توده‌ای و پراکنده را از دست می‌دهند؛ و پژوهش‌هایی که تنها محتوای تولیدشده کاربر را می‌شمارند، تماشای خاموش را نادیده می‌گیرند.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در به‌هم‌پیوستن مصرف، اجرا و هویت است؛ اما باید با تحلیل نابرابری دسترسی و قدرت الگوریتم تکمیل شود. نه همه به یک اندازه دیده می‌شوند و نه همه به یک اندازه توان اجرای عمومی دارند.",
        "critique_text": "\n".join([
            "۱. خطی‌بودن ظاهری: سه‌گانه ممکن است مرحله‌ای خوانده شود، در حالی که اشکال مخاطب هم‌زمان‌اند.",
            "۲. زمینه غربی: نمونه‌ها عمدتاً از جوامع غربی و رسانه‌های فراگیر می‌آید.",
            "۳. نادیده‌گرفتن نابرابری: دسترسی به ابزار اجرا و دیده‌شدن، نامتوازن است.",
            "۴. ابهام مخاطب پراکنده: مرز این نوع با مخاطب توده‌ای در عمل روشن نیست.",
            "۵. تحول پلتفرم: نظریه پیش از شبکه‌های اجتماعی فراگیر نوشته شد و باید بازخوانی شود.",
        ]),
        "example_text": "یک کنسرت موسیقی هم مخاطب ساده دارد (حاضران در سالن)، هم مخاطب توده‌ای (بینندگان پخش تلویزیونی) و هم مخاطب پراکنده (کاربرانی که کلیپ‌های آن را در شبکه‌های اجتماعی می‌بینند و خود کلیپ مشابه می‌سازند). در حالت سوم، تماشاگر و اجراگر یکی می‌شوند.",
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
                                       "verified": n_verified, "batch": 89}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH89 THEORY DONE")


if __name__ == "__main__":
    main()
