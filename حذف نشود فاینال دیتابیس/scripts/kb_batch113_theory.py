# -*- coding: utf-8 -*-
"""Batch 113: full documentation for MC-698, MC-665, MC-667, MC-675."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch113-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch113_theory.json"

S = {
    "MC-698": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Repairing the News: A Case Study of the News Paradigm",
             title_fa="ترمیم خبر: مطالعه موردی پارادایم خبری",
             authors="Bennett, W. L.; Gressett, L. A.; Haltom, W.", year=1985,
             publisher="Journal of Communication",
             doi=None, url="https://web.stanford.edu/class/comm1a/readings/bennett-press-state.pdf",
             language="en", isbn=None,
             citation="Bennett, W. L., Gressett, L. A., & Haltom, W. (1985). Repairing the news: A case study of the news paradigm. Journal of Communication, 35(2), 50-68.",
             locator="35(2):50-68", locator_type="page_range",
             supports="news paradigm and paradigm repair after breach", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="The News Paradigm and the Ideology of Objectivity: A Socialist at the Wall Street Journal",
             title_fa="پارادایم خبری و ایدئولوژی عینیت: سوسیالیستی در وال‌استریت ژورنال",
             authors="Reese, S. D.", year=1990, publisher="Critical Studies in Mass Communication",
             doi=None, url="https://journalism.utexas.edu/sites/default/files/sites/journalism.utexas.edu/files/attachments/reese/news-paradigm-add.pdf",
             language="en", isbn=None,
             citation="Reese, S. D. (1990). The news paradigm and the ideology of objectivity: A socialist at the Wall Street Journal. Critical Studies in Mass Communication, 7(4), 390-409.",
             locator="7(4):390-409", locator_type="page_range",
             supports="objectivity as the core paradigm of professional journalism", verified=False),
    ],
    "MC-665": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Connection Strategies: Social Capital Implications of Facebook-Enabled Communication Practices",
             title_fa="راهبردهای پیوند: پیامدهای سرمایه اجتماعی رویه‌های ارتباطی فعال‌شده در فیسبوک",
             authors="Ellison, N. B.; Steinfield, C.; Lampe, C.", year=2011,
             publisher="New Media & Society",
             doi="10.1177/1461444810385389",
             url="https://journals.sagepub.com/doi/10.1177/1461444810385389",
             language="en", isbn=None,
             citation="Ellison, N. B., Steinfield, C., & Lampe, C. (2011). Connection strategies: Social capital implications of Facebook-enabled communication practices. New Media & Society, 13(6), 873-892.",
             locator="13(6):873-892", locator_type="page_range",
             supports="online maintenance of weak ties and bridging social capital", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Strength of Weak Ties",
             title_fa="قدرت پیوندهای ضعیف",
             authors="Granovetter, M. S.", year=1973, publisher="American Journal of Sociology",
             doi=None, url=None, language="en", isbn=None,
             citation="Granovetter, M. S. (1973). The strength of weak ties. American Journal of Sociology, 78(6), 1360-1380.",
             locator="78(6):1360-1380", locator_type="page_range",
             supports="weak ties as bridges to novel information across clusters", verified=False),
    ],
    "MC-667": [
        dict(kind="BOOK_CHAPTER",
             title_en="The Relevance of Algorithms",
             title_fa="مرتبط‌بودن الگوریتم‌ها",
             authors="Gillespie, T.", year=2014, publisher="MIT Press",
             doi="10.7551/mitpress/9780262525374.003.0009",
             url="https://direct.mit.edu/books/edited-volume/3021/chapter/82555/The-Relevance-of-Algorithms",
             language="en", isbn=None,
             citation="Gillespie, T. (2014). The relevance of algorithms. In T. Gillespie, P. J. Boczkowski, & K. A. Foot (Eds.), Media technologies: Essays on communication, materiality, and society (pp. 167-194). MIT Press.",
             locator="pp. 167-194", locator_type="page_range",
             supports="algorithms as public relevance technologies shaping visibility", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Want to Be on the Top? Algorithmic Power and the Threat of Invisibility on Facebook",
             title_fa="می‌خواهید بالا باشیم؟ قدرت الگوریتمی و تهدید نامرئی‌شدن در فیسبوک",
             authors="Bucher, T.", year=2012, publisher="New Media & Society",
             doi=None, url=None, language="en", isbn=None,
             citation="Bucher, T. (2012). Want to be on the top? Algorithmic power and the threat of invisibility on Facebook. New Media & Society, 14(7), 1164-1180.",
             locator="14(7):1164-1180", locator_type="page_range",
             supports="users' tactics in response to algorithmic visibility", verified=False),
    ],
    "MC-675": [
        dict(kind="BOOK",
             title_en="Audiences: A Sociological Theory of Performance and Imagination",
             title_fa="مخاطبان: نظریه‌ای جامعه‌شناختی درباره اجرا و تخیل",
             authors="Abercrombie, N.; Longhurst, B.", year=1998, publisher="Sage",
             doi=None, url="https://books.google.com/books/about/Audiences.html?id=WtMPSmNkaYUC",
             language="en", isbn=None,
             citation="Abercrombie, N., & Longhurst, B. (1998). Audiences: A sociological theory of performance and imagination. Sage.",
             locator="work", locator_type="work",
             supports="diffused audience in the spectacle/performance paradigm", verified=True),
        dict(kind="BOOK",
             title_en="The Audience in Everyday Life: Living in a Media World",
             title_fa="مخاطب در زندگی روزمره: زیستن در جهان رسانه‌ای",
             authors="Bird, S. E.", year=2003, publisher="Routledge",
             doi=None, url=None, language="en", isbn=None,
             citation="Bird, S. E. (2003). The audience in everyday life: Living in a media world. Routledge.",
             locator="work", locator_type="work",
             supports="everyday, diffuse character of audience experience", verified=False),
    ],
}

ENRICH = {
    "MC-698": {
        "summary": "(بننت، گِرست و هالتوم، ۱۹۸۵) نظریه پارادایم خبری می‌گوید روزنامه‌نگاران در چارچوبی از مفروضات مشترک کار می‌کنند که تعیین می‌کند چه چیزی خبر است و چگونه باید روایت شود. این پارادایم شامل عینیت، توازن، ارزش خبری و رویه‌های تحریریه است. وقتی خبری این چارچوب را نقض می‌کند، رسانه به «ترمیم پارادایم» می‌پردازد: خطا را فردی می‌کند، رویه را اصلاح می‌نماید و اعتبار حرفه را بازمی‌سازد. ریس در ۱۹۹۰ نشان داد عینیت، هسته ایدئولوژیک این پارادایم است. پارادایم، هم راهنمای عمل است و هم مرز نقد را تعیین می‌کند. در محیط دیجیتال، این چارچوب توضیح می‌دهد چرا رسانه در برابر بحران اعتماد به اصلاح رویه می‌پردازد، نه بازنگری بنیادین. همچنین پژوهش پارادایم نشان داد رسانه در مواجهه با رقیب بیرونی مانند رسانه شهروندی، نخست مرز حرفه را با معیارهایی مانند راستی‌آزمایی و پاسخ‌گویی بازتعریف می‌کند و تنها در صورت فشار پیوسته، معیارهای خود را تغییر می‌دهد؛ بنابراین تغییر پارادایم، فرایندی تدریجی و منازعه‌آمیز است.",
        "definition": "پارادایم خبری، مجموعه مفروضات، قواعد و نمونه‌های مشترک حرفه روزنامه‌نگاری است که تعریف خبر، معیار ارزش و شیوه روایت را تعیین می‌کند و در برابر نقض، با ترمیم از خود دفاع می‌کند.",
        "main_problem": "مسئله این است که چرا رسانه‌های رقیب در تعریف خبر و خطا به الگوهای مشابه می‌رسند. پاسخ، پارادایم مشترک حرفه است. پرسش دوم، تغییر است: پارادایم در چه شرایطی به جای ترمیم، دگرگون می‌شود.",
        "mechanism": "۱. مفروضات مشترک: تعریف خبر و ارزش خبری.\n۲. رویه استاندارد: عینیت، توازن و راستی‌آزمایی.\n۳. نمونه‌های مرجع: گزارش‌های الگو برای حرفه.\n۴. نقض: خطای آشکار یا چالش بیرونی.\n۵. ترمیم: فردی‌سازی خطا و اصلاح رویه.\n۶. مرز نقد: پارادایم تعیین می‌کند چه نقدی مشروع است.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا خبرنگار متخلف به‌عنوان استثنا معرفی می‌شود، چرا رسانه در بحران اعتماد بیانیه رویه‌ای منتشر می‌کند و چرا روزنامه‌نگاری داده گاه به‌عنوان تهدید پارادایم دیده می‌شود. نکته مهم این است که ترمیم، هم دفاع مشروع است و هم می‌تواند بازنگری بنیادین را به تعویق بیندازد؛ همین دوگانگی، پژوهش رسانه را به سنجش نسبت میان پاسخ‌گویی و اصلاح‌گری فرامی‌خواند.",
        "assumptions": [
            "حرفه روزنامه‌نگاری پارادایم مشترک دارد.",
            "پارادایم تعریف خبر را تعیین می‌کند.",
            "نقض پارادایم، واکنش ترمیمی می‌سازد.",
        ],
        "principles": [
            "عینیت، هسته ایدئولوژیک پارادایم است.",
            "ترمیم، اعتبار حرفه را حفظ می‌کند.",
            "پارادایم، مرز نقد مشروع را می‌سازد.",
        ],
        "critiques": [
            "۱. ایستایی: تغییر پارادایم کم‌تر توضیح داده می‌شود.\n۲. قدرت: منافع مالکیت کم‌تر تحلیل می‌شود.\n۳. سنجش: مرز پارادایم تفسیری است.\n۴. زمینه: نمونه‌ها بیشتر آمریکایی‌اند.\n۵. دیجیتال: پارادایم شبکه‌ای نیازمند بازبینی است.",
        ],
        "applications": [
            "نقد رسانه: تحلیل ترمیم پس از خطا.",
            "آموزش روزنامه‌نگاری: آگاهی از مفروضات حرفه.",
            "اعتماد عمومی: ارزیابی اصلاح رویه.",
            "نوآوری خبری: شناخت مقاومت پارادایمی.",
        ],
        "evolution": "بننت و همکاران در ۱۹۸۵ ترمیم پارادایم را صورتبندی کردند و ریس در ۱۹۹۰ عینیت را هسته آن دید. پژوهش رسانه دیجیتال، پارادایم شبکه‌ای و بحران اعتماد را افزود.",
        "key_concepts": [
            "پارادایم خبری (News Paradigm)",
            "ترمیم پارادایم (Paradigm Repair)",
            "ایدئولوژی عینیت (Ideology of Objectivity)",
            "ارزش خبری (News Value)",
            "رویه تحریریه (Editorial Routine)",
            "مرز نقد (Boundary of Critique)",
        ],
        "studies": [
            "Bennett, W. L., Gressett, L. A., & Haltom, W. (1985). Repairing the news. Journal of Communication, 35(2), 50-68.",
            "Reese, S. D. (1990). The news paradigm and the ideology of objectivity. Critical Studies in Mass Communication, 7(4), 390-409.",
        ],
        "theorists": "دبلیو. لنس بننت؛ استیون ریس",
        "theorists_text": "بننت و همکاران (۱۹۸۵)؛ ریس (۱۹۹۰)",
        "year": 1985,
        "model": "پارادایم مشترک → تعریف خبر و رویه → نقض → ترمیم → بازسازی اعتبار حرفه.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nبننت و همکاران پارادایم را از فلسفه علم وام گرفتند و به حرفه خبر بردند. نوآوری چارچوب، توضیح واکنش حرفه به خطاست.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با مطالعه موردی، تحلیل متن و مصاحبه خبرنگار انجام می‌شود. پژوهشی که تنها بیانیه رسانه را می‌خواند، رویه پنهان را از دست می‌دهد؛ و پژوهشی که هر اصلاح را ترمیم می‌خواند، تغییر واقعی را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در تحلیل بحران اعتماد است، اما باید با اقتصاد سیاسی تکمیل شود. ترمیم بی بازنگری، به حفظ وضع بدل می‌شود.",
        "critique_text": "\n".join([
            "۱. ایستایی: تغییر پارادایم کم‌تر توضیح داده می‌شود.",
            "۲. قدرت: مالکیت کم‌تر تحلیل می‌شود.",
            "۳. سنجش: مرز پارادایم تفسیری است.",
            "۴. زمینه: نمونه‌ها آمریکایی‌اند.",
            "۵. دیجیتال: پارادایم شبکه‌ای بازبینی می‌خواهد.",
        ]),
        "example_text": "پس از افشای جعل خبر، رسانه نه تعریف خبر، بلکه رویه راستی‌آزمایی را اصلاح می‌کند؛ ترمیم، اعتبار را بازمی‌سازد اما پرسش بنیادین درباره منطق خبر را بی‌پاسخ می‌گذارد.",
    },
    "MC-665": {
        "summary": "(الیسون، استاینفیلد و لمپ، ۲۰۱۱) نظریه پیوند ضعیف در شبکه‌های آنلاین، یافته گرانوویتر را به محیط دیجیتال گسترش می‌دهد. گرانوویتر نشان داده بود پیوندهای ضعیف، پل میان خوشه‌های اجتماعی‌اند و اطلاعات تازه و فرصت شغلی می‌آورند. در شبکه آنلاین، هزینه نگهداشت این پیوندها به‌شدت کاهش می‌یابد و کاربر می‌تواند صدها پیوند ضعیف را زنده نگه دارد. الیسون و همکاران نشان دادند راهبردهای پیوند بر سرمایه اجتماعی پل‌زننده اثر می‌گذارد. «دوستان» شبکه‌ای، مرز میان پیوند قوی و ضعیف را مخدوش می‌کند. نظریه، نقش پلتفرم در گسترش شبکه فرصت و اطلاعات را توضیح می‌دهد.",
        "definition": "پیوند ضعیف در شبکه آنلاین، رابطه‌ای روابط‌محور با هزینه نگهداشت پایین است که پل میان خوشه‌ها می‌سازد و دسترسی به اطلاعات متنوع و سرمایه اجتماعی پل‌زننده را ممکن می‌کند.",
        "main_problem": "مسئله این است که چرا مهارت و اطلاعات نو، بیش از آنکه از دوستان نزدیک برسد، از آشنایان دور می‌رسد. پاسخ، کارکرد پل‌زننده پیوند ضعیف است. پرسش دوم، دیجیتال است: پلتفرم چگونه کیفیت و کمیت این پیوندها را تغییر می‌دهد.",
        "mechanism": "۱. قدرت پیوند ضعیف: پل میان خوشه‌های متراکم.\n۲. تنوع اطلاعات: پیوند ضعیف، خبر تازه می‌آورد.\n۳. هزینه پایین نگهداشت: لایک و پیام کوتاه، رابطه را زنده نگه می‌دارد.\n۴. سرمایه پل‌زننده: دسترسی به منابع فراتر از حلقه نزدیک.\n۵. مخدوش‌شدن مرز: «دوست» شبکه‌ای، قوی و ضعیف را درهم می‌آمیزد.\n۶. راهبرد پیوند: الگوی کاربر، ترکیب شبکه را تعیین می‌کند.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا شبکه اجتماعی فرصت شغلی می‌سازد، چرا انتشار خبر از طریق آشنایان دور سریع‌تر است و چرا کاربران با شبکه متنوع، اطلاعات بیشتری می‌گیرند. نکته مهم این است که پیوند ضعیف، جای حمایت عاطفی نزدیک را نمی‌گیرد؛ کارکرد آن دسترسی است، نه پشتیبانی. با این حال، گسترش پیوندها می‌تواند توهم نزدیکی بسازد: کاربر صدها آشنا دارد اما در بحران، تکیه‌گاه اندکی می‌یابد؛ از این رو، پلتفرم باید هم پل بسازد و هم حمایت نزدیک را تقویت کند.",
        "assumptions": [
            "پیوند ضعیف پل میان خوشه‌هاست.",
            "پلتفرم هزینه نگهداشت را کاهش می‌دهد.",
            "شبکه متنوع، اطلاعات تازه می‌آورد.",
        ],
        "principles": [
            "پیوند ضعیف، اطلاعات غیرتکراری می‌آورد.",
            "سرمایه پل‌زننده از تنوع شبکه می‌آید.",
            "پیوند ضعیف جای حمایت نزدیک را نمی‌گیرد.",
        ],
        "critiques": [
            "۱. سنجش: قوت پیوند در فضای آنلاین سخت اندازه‌گیری می‌شود.\n۲. کیفیت: شمار زیاد «دوست» به معنای پیوند مؤثر نیست.\n۳. زمینه: یافته‌ها بیشتر به کاربران غربی محدودند.\n۴. قدرت: اثر الگوریتم بر نمایش پیوند کم دیده می‌شود.\n۵. زمان: پویایی بلندمدت شبکه کم بررسی شده است.",
        ],
        "applications": [
            "شبکه اجتماعی: طراحی برای پیوند میان‌خوشه‌ای.",
            "بازار کار: بهره‌گیری از پیوند ضعیف در فرصت شغلی.",
            "رسانه و خبر: انتشار از طریق شبکه آشنایان.",
            "سرمایه اجتماعی: سنجش پل‌زنندگی شبکه.",
        ],
        "evolution": "گرانوویتر در ۱۹۷۳ قدرت پیوند ضعیف را صورتبندی کرد و الیسون و همکاران در ۲۰۱۱ آن را به فیسبوک و سرمایه اجتماعی گستردند. پژوهش پلتفرم بعدی، نقش الگوریتم را افزود.",
        "key_concepts": [
            "پیوند ضعیف (Weak Tie)",
            "پل میان‌خوشه‌ای (Inter-Cluster Bridge)",
            "سرمایه اجتماعی پل‌زننده (Bridging Social Capital)",
            "هزینه نگهداشت (Maintenance Cost)",
            "راهبرد پیوند (Connection Strategy)",
            "شبکه فرصت (Opportunity Network)",
        ],
        "studies": [
            "Ellison, N. B., Steinfield, C., & Lampe, C. (2011). Connection strategies. New Media & Society, 13(6), 873-892.",
            "Granovetter, M. S. (1973). The strength of weak ties. American Journal of Sociology, 78(6), 1360-1380.",
        ],
        "theorists": "نیکول الیسون؛ چارلز استاینفیلد؛ کلیف لمپ؛ مارک گرانوویتر",
        "theorists_text": "الیسون و همکاران (۲۰۱۱)؛ گرانوویتر (۱۹۷۳)",
        "year": 2011,
        "model": "پیوند ضعیف با هزینه پایین → پل میان خوشه‌ها → اطلاعات متنوع → سرمایه پل‌زننده.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nالیسون و همکاران نظریه شبکه گرانوویتر را در بستر پلتفرم آزمودند. نوآوری چارچوب، پیوند راهبرد ارتباطی با سرمایه اجتماعی است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با پیمایش شبکه، داده تعامل و مقیاس سرمایه انجام می‌شود. پژوهشی که تنها شمار دوستان را می‌سنجد، کیفیت پیوند را از دست می‌دهد؛ و پژوهشی که هر تعامل آنلاین را پیوند ضعیف می‌خواند، تفاوت را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در تحلیل شبکه فرصت است، اما باید با مطالعه الگوریتم تکمیل شود. پیوند بی کیفیت، به شلوغی بی اثر بدل می‌شود.",
        "critique_text": "\n".join([
            "۱. سنجش: قوت پیوند سخت اندازه‌پذیر است.",
            "۲. کیفیت: شمار دوست، پیوند مؤثر نیست.",
            "۳. زمینه: یافته‌ها غربی‌اند.",
            "۴. قدرت: اثر الگوریتم کم دیده می‌شود.",
            "۵. زمان: پویایی بلندمدت کم بررسی شده است.",
        ]),
        "example_text": "کاربری که در شبکه اجتماعی با هم‌دانشگاهیان قدیمی در تماس است، آگهی شغلی را زودتر از دوستان نزدیک دریافت می‌کند؛ پیوند ضعیف، پل فرصت است.",
    },
    "MC-667": {
        "summary": "(گیلاسپی، ۲۰۱۴) نظریه برجستگی الگوریتمی می‌گوید الگوریتم‌های رسانه، فناوری مرتبط‌بودن عمومی‌اند: آن‌ها تعیین می‌کنند چه چیزی دیده شود، چه چیزی مهم تلقی شود و چه چیزی ناپیدا بماند. گیلاسپی بر سه ویژگی تأکید کرد: الگوریتم بر داده الگو می‌یابد، انتخاب را خودکار می‌کند و معیارش اغلب کدر است. بوخر نشان داد کاربران از نامرئی‌شدن می‌ترسند و برای دیده شدن تاکتیک می‌سازند. برجستگی الگوریتمی، جانشین دروازه‌بانی انسانی نیست، بلکه آن را بازآرایی می‌کند. در رسانه اجتماعی، این چارچوب توضیح می‌دهد چرا محتوای یکسان برای دو کاربر وزن متفاوت دارد و چرا معیار مرتبط‌بودن، خود موضوع قدرت است.",
        "definition": "برجستگی الگوریتمی، فرایندی است که در آن سامانه خودکار بر پایه داده و معیار کدر، اهمیت و دیدپذیری محتوا را تعیین می‌کند و ترتیب دیده‌شدن را به سازوکاری قدرت‌محور بدل می‌سازد.",
        "main_problem": "مسئله این است که چه کسی و بر چه معیاری تعیین می‌کند محتوایی مهم است. پاسخ، الگوریتم مرتبط‌بودن است. پرسش دوم، شفافیت است: چگونه می‌توان معیار برجستگی را پاسخگو کرد.",
        "mechanism": "۱. داده و الگو: رفتار گذشته، معیار پیش‌بینی می‌سازد.\n۲. خودکارسازی: انتخاب بدون دخالت انسانی.\n۳. کدری: معیار مرتبط‌بودن برای مخاطب روشن نیست.\n۴. شخصی‌سازی: برجستگی برای هر کاربر متفاوت است.\n۵. نامرئی‌شدن: محتوای کم‌تعامل، حذف می‌شود.\n۶. تاکتیک کاربر: تلاش برای تطبیق با معیار.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا خبر مهم در فید یک کاربر دیده نمی‌شود، چرا برند رسانه‌ای به معیار تعامل وابسته می‌شود و چرا پژوهش سوگیری الگوریتمی اهمیت دارد. نکته مهم این است که الگوریتم بی‌طرف نیست، اما قادر مطلق هم نیست؛ کاربر و زمینه اجتماعی، اثر آن را تعدیل می‌کنند. همچنین برجستگی الگوریتمی، مفهوم دستور کار عمومی را پیچیده می‌کند: وقتی هر کاربر فهرست متفاوتی می‌بیند، آنچه جامعه درباره آن گفت‌وگو می‌کند دیگر از یک فهرست مشترک برنمی‌خیزد. از این رو، پژوهش رسانه باید هم معیار رتبه‌بندی و هم تجربه کاربر را هم‌زمان ببیند، از فروکاستن مسئله به یک الگوریتم فاسد بپرهیزد و همین هم‌زمانی، مرز میان قدرت سامانه و انتخاب فرد را روشن‌تر می‌سازد و راه را برای پاسخ‌گویی عملی هموار می‌کند و به جای نقد نظری صرف، مبنایی برای سنجش عملکرد عملی رسانه فراهم می‌آورد.",
        "assumptions": [
            "الگوریتم، مرتبط‌بودن را تعیین می‌کند.",
            "معیار برجستگی اغلب کدر است.",
            "برجستگی، قدرت و دیدپذیری می‌سازد.",
        ],
        "principles": [
            "الگوریتم بی‌طرف نیست.",
            "شخصی‌سازی، برجستگی را فردی می‌کند.",
            "کاربر برای دیده‌شدن تاکتیک می‌سازد.",
        ],
        "critiques": [
            "۱. قدرت: عاملیت کاربر کم‌تر دیده می‌شود.\n۲. سنجش: اثر الگوریتم در آزمایش سخت جدا می‌شود.\n۳. شفافیت: معیارها تجاری و پنهان‌اند.\n۴. تعمیم: یافته‌ها بیشتر به پلتفرم‌های بزرگ محدودند.\n۵. علیت: تمایز اثر الگوریتم و انتخاب کاربر دشوار است.",
        ],
        "applications": [
            "پژوهش الگوریتم: تحلیل معیار مرتبط‌بودن.",
            "سیاست پلتفرم: الزام شفافیت رتبه‌بندی.",
            "رسانه خبری: مدیریت وابستگی به فید.",
            "سواد الگوریتمی: شناخت برجستگی شخصی.",
        ],
        "evolution": "گیلاسپی در ۲۰۱۴ الگوریتم را فناوری مرتبط‌بودن عمومی خواند و بوخر در ۲۰۱۲ ترس از نامرئی‌شدن را نشان داد. پژوهش حسابرسی الگوریتم، چارچوب را در دهه بعد بسط داد.",
        "key_concepts": [
            "برجستگی الگوریتمی (Algorithmic Salience)",
            "مرتبط‌بودن عمومی (Public Relevance)",
            "دروازه‌بانی الگوریتمی (Algorithmic Gatekeeping)",
            "نامرئی‌شدن (Invisibility)",
            "شخصی‌سازی (Personalization)",
            "کدری معیار (Criterion Opacity)",
        ],
        "studies": [
            "Gillespie, T. (2014). The relevance of algorithms. In Media technologies (pp. 167-194). MIT Press.",
            "Bucher, T. (2012). Want to be on the top? New Media & Society, 14(7), 1164-1180.",
        ],
        "theorists": "تارلتون گیلاسپی؛ تاینا بوخر",
        "theorists_text": "گیلاسپی (۲۰۱۴)؛ بوخر (۲۰۱۲)",
        "year": 2014,
        "model": "داده و معیار کدر → رتبه‌بندی خودکار → برجستگی فردی → دیدپذیری یا نامرئی‌شدن.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nگیلاسپی الگوریتم را نهاد معنا‌ساز دید و آن را از ابزار فنی صرف جدا کرد. نوآوری چارچوب، پیوند رتبه‌بندی با قدرت عمومی است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با تحلیل خروجی رتبه‌بندی، آزمایش و مصاحبه انجام می‌شود. پژوهشی که تنها کلیک را می‌سنجد، معیار را از دست می‌دهد؛ و پژوهشی که برجستگی را تماماً به الگوریتم نسبت می‌دهد، انتخاب کاربر را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در نقد پلتفرم است، اما باید با مطالعه مصرف تکمیل شود. الگوریتم بی شفافیت، به قدرت پنهان بدل می‌شود.",
        "critique_text": "\n".join([
            "۱. قدرت: عاملیت کاربر کم دیده می‌شود.",
            "۲. سنجش: اثر الگوریتم سخت جدا می‌شود.",
            "۳. شفافیت: معیار تجاری پنهان است.",
            "۴. تعمیم: یافته‌ها محدود به پلتفرم بزرگ‌اند.",
            "۵. علیت: تمایز از انتخاب کاربر دشوار است.",
        ]),
        "example_text": "دو کاربر در یک روز، دو ترتیب متفاوت از اخبار یک رویداد می‌بینند؛ در هر فید، معیار تعامل گذشته تعیین کرده است که کدام روایت برجسته شود.",
    },
    "MC-675": {
        "summary": "(ابرکرامبی و لانگهرست، ۱۹۹۸) نظریه مخاطب پراکنده می‌گوید دیگر نمی‌توان مخاطب را گروهی متمرکز و منفعل دید. آنان سه گونه تاریخی را تفکیک کردند: مخاطب ساده، مخاطب توده‌ای و مخاطب پراکنده. در وضعیت پراکنده، مرز اجرا و تماشا فرو می‌ریزد و همه تقریباً همیشه مخاطب‌اند: در خانه، خیابان و شبکه اجتماعی. این وضعیت در چارچوب نمایش و تخیل فهم می‌شود: زندگی روزمره به اجرا و خود به تصویر بدل می‌شود. رسانه در بافت زندگی حل می‌شود و مصرف، پیوسته و غیرمتمرکز است. نظریه، مخاطب را پدیده‌ای فراگیر و رابطه‌ای می‌داند، نه موقعیتی محدود در برابر صفحه.",
        "definition": "مخاطب پراکنده، وضعیتی است که در آن تجربه مخاطب‌بودن از موقعیت‌های مشخص رسانه‌ای فراتر می‌رود، با زندگی روزمره درهم می‌آمیزد و مرز اجراکننده و تماشاگر را مخدوش می‌کند.",
        "main_problem": "مسئله این است که چرا مفهوم مخاطب به‌عنوان گروهی که در برابر رسانه می‌نشیند دیگر کافی نیست. پاسخ، پراکندگی رسانه در زندگی است. پرسش دوم، پیامد است: این پراکندگی چه اثری بر هویت و روابط اجتماعی دارد.",
        "mechanism": "۱. سه گونه: مخاطب ساده، توده‌ای و پراکنده.\n۲. فروریزی مرز: تماشاگر خود نیز اجرا می‌کند.\n۳. چارچوب نمایش: زندگی روزمره صحنه اجراست.\n۴. حلول رسانه: مصرف در همه فضاها جریان دارد.\n۵. خود بازتابی: فرد خود را از چشم مخاطب می‌بیند.\n۶. پیوستگی: مخاطب‌بودن وضعیت دائمی است.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا کاربر شبکه اجتماعی هم مصرف‌کننده و هم تولیدکننده است، چرا رفتار روزمره اجراگونه می‌شود و چرا سنجش مخاطب با شمار بیننده دشوار است. نکته مهم این است که واژه پراکنده به معنای همگن‌شدن مخاطبان نیست؛ تجربه مشترک، دریافت‌های متفاوت را در خود دارد. همچنین این چارچوب به پژوهش مخاطب یادآوری می‌کند که مصرف رسانه تنها در برابر صفحه رخ نمی‌دهد؛ در گفت‌وگوی روزمره، حافظه و بدن نیز ادامه می‌یابد. از این رو، سنجش مخاطب باید تجربه زیسته را ببیند، نه فقط زمان مواجهه را، و این نگاه، پژوهش مخاطب را از شمارش به فهم فرهنگی پیوند می‌دهد و سیاست‌گذاری رسانه را از هدف‌گیری جمعیت به درک تجربه روزمره سوق می‌دهد و محدودیت شمارش صرف را آشکار می‌کند و مرز میان تماشاگر و بازیگر را در رسانه معاصر بازتعریف می‌نماید.",
        "assumptions": [
            "مخاطب در زندگی روزمره حلول کرده است.",
            "مرز اجرا و تماشا فرو می‌ریزد.",
            "مخاطب‌بودن وضعیتی پیوسته است.",
        ],
        "principles": [
            "مخاطب ساده دیگر الگوی غالب نیست.",
            "رسانه، بافت زندگی است نه رویداد.",
            "مخاطب هم مصرف‌کننده و هم اجراکننده است.",
        ],
        "critiques": [
            "۱. تعمیم: همه مخاطبان پراکنده نیستند.\n۲. سنجش: مخاطب پراکنده سخت اندازه‌گیری می‌شود.\n۳. نابرابری: دسترسی و مهارت یکسان نیست.\n۴. قدرت: اقتصاد رسانه کم‌تر تحلیل می‌شود.\n۵. مخاطب فعال: مرز فعالیت و مصرف مبهم می‌ماند.",
        ],
        "applications": [
            "مطالعات مخاطب: بازتعریف واحد تحلیل.",
            "رسانه اجتماعی: تحلیل مصرف و تولید هم‌زمان.",
            "سنجش رسانه: فراتر رفتن از شمار بیننده.",
            "آموزش رسانه: شناخت مخاطب‌بودن پیوسته.",
        ],
        "evolution": "ابرکرامبی و لانگهرست در ۱۹۹۸ سه‌گانه مخاطب را عرضه کردند. پژوهش رسانه اجتماعی، خوداجرایی و مخاطب شبکه‌ای، چارچوب را آزمود و گسترد.",
        "key_concepts": [
            "مخاطب پراکنده (Diffused Audience)",
            "مخاطب ساده (Simple Audience)",
            "مخاطب توده‌ای (Mass Audience)",
            "چارچوب نمایش (Spectacle Paradigm)",
            "خوداجرایی (Self-Performance)",
            "حلول رسانه (Media Saturation)",
        ],
        "studies": [
            "Abercrombie, N., & Longhurst, B. (1998). Audiences: A sociological theory of performance and imagination. Sage.",
            "Bird, S. E. (2003). The audience in everyday life. Routledge.",
        ],
        "theorists": "نیکلاس ابرکرامبی؛ برایان لانگهرست",
        "theorists_text": "ابرکرامبی و لانگهرست (۱۹۹۸)",
        "year": 1998,
        "model": "حلول رسانه در زندگی → فروریزی مرز اجرا و تماشا → مخاطب پراکنده → خود بازتابی و اجرای روزمره.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nابرکرامبی و لانگهرست مخاطب را در چارچوب نمایش و تخیل بازتعریف کردند. نوآوری چارچوب، رد مخاطب منفعل و متمرکز است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با مردم‌نگاری، مصاحبه و تحلیل مصرف انجام می‌شود. پژوهشی که تنها شمار بیننده را می‌سنجد، تجربه پراکنده را از دست می‌دهد؛ و پژوهشی که همه را مخاطب پراکنده می‌خواند، نابرابری دسترسی را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در تحلیل رسانه اجتماعی است، اما باید با اقتصاد سیاسی تکمیل شود. پراکندگی بی مهارت، به مصرف بی‌مقاومت بدل می‌شود.",
        "critique_text": "\n".join([
            "۱. تعمیم: همه مخاطبان پراکنده نیستند.",
            "۲. سنجش: مخاطب پراکنده سخت اندازه‌پذیر است.",
            "۳. نابرابری: دسترسی یکسان نیست.",
            "۴. قدرت: اقتصاد رسانه کم‌تر تحلیل می‌شود.",
            "۵. فعالیت: مرز مصرف و تولید مبهم است.",
        ]),
        "example_text": "کاربری که در شبکه اجتماعی فیلم کوتاه می‌بیند و همان لحظه پاسخ خود را ضبط می‌کند، هم مخاطب است و هم اجراکننده؛ مرز تماشا و نمایش فرو ریخته است.",
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
YEAR_FIX = {
    "MC-675": "year corrected 1990 -> 1998 (Abercrombie & Longhurst, Audiences, 1998)",
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

        if code in YEAR_FIX:
            cur.execute("""INSERT INTO kb_audit_log (entity_code,action,detail,source,created_at)
                VALUES (%s,'DOC_FIX',%s,%s,%s)""",
                        (code, json.dumps({"fix": YEAR_FIX[code]}, ensure_ascii=False), STAMP, NOW))

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
                                       "verified": n_verified, "batch": 113}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH113 THEORY DONE")


if __name__ == "__main__":
    main()
