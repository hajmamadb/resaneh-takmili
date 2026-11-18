# -*- coding: utf-8 -*-
"""Batch 93: full documentation for MC-513, MC-514, MC-515, MC-516."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch93-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch93_theory.json"

S = {
    "MC-513": [
        dict(kind="REPORT",
             title_en="Many Voices, One World: Towards a New, More Just, and More Efficient World Information and Communication Order",
             title_fa="بسیار صداها، یک جهان: به سوی نظمی نوین، عادلانه‌تر و کارآمدتر در اطلاعات و ارتباطات جهانی",
             authors="MacBride, S. (et al.); UNESCO", year=1980, publisher="UNESCO",
             doi=None, url="https://unesdoc.unesco.org/ark:/48223/pf0000372754",
             language="en", isbn=None,
             citation="MacBride, S., et al. (1980). Many voices, one world: Towards a new, more just, and more efficient world information and communication order. UNESCO.",
             locator="work", locator_type="work",
             supports="imbalanced news flow / new world information and communication order / right to communicate", verified=True),
        dict(kind="BOOK",
             title_en="Global Glasnost: Toward a New World Information and Communication Order?",
             title_fa="گلاسنوست جهانی: به سوی نظم نوین اطلاعات و ارتباطات جهانی؟",
             authors="Galtung, J.; Vincent, R. C.", year=1992, publisher="Hampton Press",
             doi=None, url=None, language="en", isbn=None,
             citation="Galtung, J., & Vincent, R. C. (1992). Global glasnost: Toward a new world information and communication order? Hampton Press.",
             locator="work", locator_type="work",
             supports="NWICO debate / structural imbalance and communication rights", verified=False),
    ],
    "MC-514": [
        dict(kind="BOOK_CHAPTER",
             title_en="Mass Media and Democracy: A Reappraisal",
             title_fa="رسانه‌های جمعی و دموکراسی: بازنگری",
             authors="Curran, J.", year=1991, publisher="Edward Arnold",
             doi=None, url=None, language="en", isbn=None,
             citation="Curran, J. (1991). Mass media and democracy: A reappraisal. In J. Curran & M. Gurevitch (Eds.), Mass media and society. Edward Arnold.",
             locator="ch.", locator_type="CHAPTER",
             supports="market failure of media diversity / civic and public media sector", verified=True),
        dict(kind="BOOK",
             title_en="The Structural Transformation of the Public Sphere",
             title_fa="دگرگونی ساختاری حوزه عمومی",
             authors="Habermas, J.", year=1989, publisher="MIT Press",
             doi=None, url=None, language="en", isbn=None,
             citation="Habermas, J. (1989). The structural transformation of the public sphere: An inquiry into a category of bourgeois society. MIT Press.",
             locator="work", locator_type="work",
             supports="public sphere / rational-critical debate / commercialization critique", verified=False),
    ],
    "MC-515": [
        dict(kind="BOOK",
             title_en="Understanding Media: The Extensions of Man",
             title_fa="فهم رسانه: امتدادهای انسان",
             authors="McLuhan, M.", year=1964, publisher="McGraw-Hill",
             doi=None, url="https://mitpress.mit.edu/9780262631594/understanding-media/",
             language="en", isbn="9780262631594",
             citation="McLuhan, M. (1964). Understanding media: The extensions of man. McGraw-Hill.",
             locator="work", locator_type="work",
             supports="the medium is the message / media as extensions of the senses", verified=True),
        dict(kind="BOOK",
             title_en="The Bias of Communication",
             title_fa="سوگیری ارتباطات",
             authors="Innis, H. A.", year=1951, publisher="University of Toronto Press",
             doi=None, url=None, language="en", isbn=None,
             citation="Innis, H. A. (1951). The bias of communication. University of Toronto Press.",
             locator="work", locator_type="work",
             supports="time-binding and space-binding media / media bias and empire", verified=False),
    ],
    "MC-516": [
        dict(kind="BOOK",
             title_en="No Sense of Place: The Impact of Electronic Media on Social Behavior",
             title_fa="بی‌حسی مکان: تأثیر رسانه‌های الکترونیک بر رفتار اجتماعی",
             authors="Meyrowitz, J.", year=1985, publisher="Oxford University Press",
             doi=None, url="https://global.oup.com/academic/product/no-sense-of-place-9780195042313",
             language="en", isbn="9780195042313",
             citation="Meyrowitz, J. (1985). No sense of place: The impact of electronic media on social behavior. Oxford University Press.",
             locator="work", locator_type="work",
             supports="media as environments / blurring of situations / front-back region change", verified=True),
        dict(kind="BOOK_CHAPTER",
             title_en="Medium Theory",
             title_fa="نظریه رسانه میانی",
             authors="Meyrowitz, J.", year=1994, publisher="Polity",
             doi=None, url=None, language="en", isbn=None,
             citation="Meyrowitz, J. (1994). Medium theory. In D. Crowley & D. Mitchell (Eds.), Communication theory today (pp. 50-77). Polity.",
             locator="pp. 50-77", locator_type="page_range",
             supports="medium theory / media as environments rather than channels", verified=False),
    ],
}

ENRICH = {
    "MC-513": {
        "summary": "(مک‌براید و همکاران، ۱۹۸۰) گزارش «بسیار صداها، یک جهان» که کمیسیون بین‌المللی مطالعه مسائل ارتباطات یونسکو منتشر کرد، نشان داد جریان خبر و اطلاعات از شمال به جنوب یک‌سویه است. کشورهای در حال توسعه خواستار نظم نوین اطلاعات و ارتباطات جهانی شدند: تعادل جریان، دسترسی به فناوری، حق حاکمیت بر اطلاعات و تقویت رسانه‌های ملی. این خواسته به مناظره‌ای تلخ انجامید: جنوب آن را عدالت ارتباطی خواند و غرب آن را تهدید آزادی مطبوعات. نتیجه، خروج آمریکا و بریتانیا از یونسکو و افول این خواسته بود.",
        "definition": "نظریه نظم جهانی اطلاعات، چارچوبی انتقادی است که ساختار نابرابر جریان خبر، مالکیت فناوری و قدرت ارتباطی را تحلیل می‌کند و نظمی عادلانه‌تر در اطلاعات و ارتباطات جهانی را تجویز می‌کند.",
        "main_problem": "مسئله این است که چرا جریان اطلاعات جهان یک‌سویه است و چه کسی از این عدم تعادل سود می‌برد. گزارش نشان داد که چند آژانس خبری غربی، تعریف رویدادهای جهان را در دست دارند و کشورهای جنوب، هم در تولید و هم در توزیع خبر حاشیه‌ای‌اند. پرسش دوم، راه‌حل است: آیا می‌توان با اصلاح ساختار، به تعادل و تنوع رسید یا این خواسته به کنترل دولتی می‌انجامد.",
        "mechanism": "۱. عدم تعادل جریان: خبر از شمال به جنوب سرازیر می‌شود و رویدادهای جنوب از صافی رسانه‌های شمال تعریف می‌شوند.\n۲. تمرکز زیرساخت و فناوری: مالکیت فناوری، ماهواره و شبکه توزیع، قدرت تعیین دستور کار را در دست چند کشور متمرکز می‌کند.\n۳. حق حاکمیت بر اطلاعات: کشورها حق دارند بر جریان اطلاعات درون مرزهای خود نظارت و سیاست‌گذاری کنند.\n۴. حق ارتباط: دسترسی به ارتباط و مشارکت در جریان اطلاعات، حقی جمعی و توسعه‌ای تلقی می‌شود.\n۵. تقویت رسانه‌های ملی و همکاری جنوب-جنوب: تبادل خبر، آموزش روزنامه‌نگار و زیرساخت مشترک، راه تعادل است.\n۶. مناظره آزادی و عدالت: هر اصلاح ساختاری با پرسش از آزادی مطبوعات و استقلال حرفه‌ای روبه‌رو می‌شود.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا بحث درباره سلطه خبری، کمک به رسانه‌های محلی و حاکمیت داده ادامه دارد، چرا پلتفرم‌های جهانی همان عدم تعادل را به شکل تازه بازتولید می‌کنند و چرا سیاست‌های ارتباطی کشورها میان دسترسی و کنترل نوسان می‌کنند. نکته مهم این است که خواسته اصلی، تعادل و تنوع بود؛ اما در عمل، این خواسته با منافع دولت‌ها و منطق جنگ سرد درهم آمیخت.",
        "assumptions": [
            "جریان جهانی اطلاعات ساختاری نابرابر دارد.",
            "تعادل جریان، شرط توسعه و عدالت ارتباطی است.",
            "سیاست‌گذاری ملی و همکاری بین‌المللی می‌تواند ساختار را اصلاح کند.",
        ],
        "principles": [
            "حق ارتباط، حقی جمعی و توسعه‌ای است.",
            "تنوع منابع خبری، شرط بازنمایی چندصدایی جهان است.",
            "حاکمیت اطلاعات، مرز میان عدالت و کنترل است.",
        ],
        "critiques": [
            "۱. آرمان‌گرایی: تجویزهای گزارش، سازوکار اجرایی روشنی نداشتند.\n۲. خطر کنترل دولتی: اصلاح ساختار می‌تواند به سانسور و انحصار دولتی بدل شود.\n۳. دوقطبی جنگ سرد: مناظره به رقابت شرق و غرب فروکاسته شد.\n۴. فرض دولت به‌عنوان نماینده ملت: صدای دولت با صدای جامعه یکسان گرفته شد.\n۵. تحول دیجیتال: شکاف دسترسی به اینترنت و قدرت پلتفرم‌ها، صورت تازه‌ای از همان عدم تعادل است.",
        ],
        "applications": [
            "سیاست ارتباطی: طراحی حمایت از رسانه‌های محلی و تنوع خبری.",
            "همکاری بین‌المللی: تبادل خبر و آموزش روزنامه‌نگاران جنوب.",
            "تحلیل جریان خبر: سنجش یک‌سویگی پوشش رویدادهای جهانی.",
            "حقوق ارتباطات: تحلیل حق دسترسی و مشارکت در جریان اطلاعات.",
        ],
        "evolution": "خواسته نظم نوین در دهه ۱۹۷۰ در جنبش کشورهای غیرمتعهد شکل گرفت و در گزارش ۱۹۸۰ صورت‌بندی شد. پس از خروج آمریکا و بریتانیا از یونسکو، این خواسته افول کرد و بعدها در بحث شکاف دیجیتال و حاکمیت اینترنت بازخوانی شد.",
        "key_concepts": [
            "نظم نوین اطلاعات و ارتباطات جهانی (New World Information and Communication Order)",
            "عدم تعادل جریان خبر (News Flow Imbalance)",
            "حق ارتباط (Right to Communicate)",
            "حاکمیت اطلاعات (Information Sovereignty)",
            "همکاری جنوب-جنوب (South-South Cooperation)",
            "سلطه ارتباطی (Communication Dominance)",
        ],
        "studies": [
            "MacBride, S., et al. (1980). Many voices, one world. UNESCO.",
            "Galtung, J., & Vincent, R. C. (1992). Global glasnost. Hampton Press.",
        ],
        "theorists": "کمیسیون مک‌براید / یونسکو (۱۹۸۰)",
        "theorists_text": "کمیسیون بین‌المللی مک‌براید (۱۹۸۰)",
        "year": 1980,
        "model": "مدل ساختاری: تمرکز تولید و توزیع خبر → جریان یک‌سویه شمال به جنوب → حاشیه‌ای‌شدن جنوب → تجویز تعادل، حق ارتباط و همکاری جنوب-جنوب.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nنظریه نظم جهانی اطلاعات، تحلیل اقتصاد سیاسی رسانه را با مطالبه عدالت بین‌المللی پیوند داد. نوآوری آن این بود که عدم تعادل خبری را نه مسئله فنی، بلکه مسئله قدرت و ساختار جهانی دید؛ ایده‌ای که بنیان سیاست‌های ارتباطی توسعه شد.\n\n۲. منطق سنجش و دام‌های آن\nسنجش نیازمند تحلیل جهت جریان خبر، منابع نقل قول و مالکیت زیرساخت است. پژوهش‌هایی که تنها شمار خبر را می‌شمارند، کیفیت بازنمایی را از دست می‌دهند؛ و پژوهش‌هایی که تنها محتوا را تحلیل می‌کنند، مالکیت و زیرساخت را نمی‌بینند.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در نشان دادن ساختار نابرابر است، اما در تجویز، مرز عدالت و کنترل را روشن نکرد. در محیط پلتفرمی، عدم تعادل از آژانس خبری به الگوریتم و زیرساخت داده منتقل شده است؛ همان پرسش‌ها با ابزار تازه تکرار می‌شوند.",
        "critique_text": "\n".join([
            "۱. آرمان‌گرایی: تجویزهای گزارش سازوکار اجرایی روشنی نداشتند.",
            "۲. خطر کنترل دولتی: اصلاح ساختار می‌تواند به سانسور بدل شود.",
            "۳. دوقطبی جنگ سرد: مناظره به رقابت شرق و غرب فروکاسته شد.",
            "۴. فرض دولت به‌عنوان نماینده ملت: صدای دولت با صدای جامعه یکسان گرفته شد.",
            "۵. تحول دیجیتال: قدرت پلتفرم‌ها صورت تازه‌ای از عدم تعادل است.",
        ]),
        "example_text": "رویدادی در یک کشور آفریقایی رخ می‌دهد؛ خبر آن ابتدا از یک آژانس غربی منتشر می‌شود و رسانه‌های محلی ناچارند همان روایت را بازنشر کنند. نبود خبرگزاری منطقه‌ای، نبود آموزش و نبود زیرساخت، همان زنجیره‌ای است که گزارش مک‌براید توصیف کرد.",
    },
    "MC-514": {
        "summary": "رسانه و دموکراسی، رابطه‌ای دووجهی است: رسانه هم ابزار دموکراسی است — اطلاع‌رسانی، نظارت بر قدرت، ساختن عرصه عمومی و دادن صدا به گروه‌های مختلف — و هم می‌تواند ابزار سلطه باشد: تمرکز مالکیت، وابستگی به تبلیغات و سرگرمی‌زدگی، تنوع و نظارت را تضعیف می‌کند. کران (۱۹۹۱) با بازنگری نظریه لیبرال نشان داد بازار آزاد به‌خودی‌خود تنوع نمی‌سازد و به سیاست رسانه‌ای، بخش عمومی و رسانه شهروندی نیاز است. هابرماس (۱۹۸۹) با مفهوم حوزه عمومی، معیار گفت‌وگوی عقلانی و نقد تجاری‌شدن آن را مطرح کرد.",
        "definition": "نظریه رسانه و دموکراسی، مجموعه‌ای از چارچوب‌هاست که نقش رسانه را در اطلاع‌رسانی، نظارت، گفت‌وگوی عمومی و بازنمایی گروه‌ها تحلیل می‌کند و شرایط ساختاری و سیاستی لازم برای کارکرد دموکراتیک رسانه را می‌سنجد.",
        "main_problem": "مسئله این است که رسانه چه زمانی به دموکراسی کمک می‌کند و چه زمانی آن را تضعیف. پاسخ، نه در فناوری و نه در نیت روزنامه‌نگار، بلکه در ساختار مالکیت، مدل درآمد و سیاست رسانه‌ای است. پرسش دوم، معیار است: چگونه می‌توان کارکرد دموکراتیک رسانه را سنجید و از کدام الگوی سیاستی دفاع کرد.",
        "mechanism": "۱. کارکرد اطلاع‌رسانی و نظارت: رسانه با گزارش رویدادها و رسواکردن سوءاستفاده، شهروند را برای تصمیم آگاهانه مجهز می‌کند.\n۲. عرصه عمومی و گفت‌وگو: رسانه فضایی برای طرح دیدگاه‌ها و شکل‌گیری اراده عمومی می‌سازد؛ کیفیت این فضا به تنوع و استقلال وابسته است.\n۳. مالکیت و تمرکز: تمرکز مالکیت، دامنه دیدگاه‌های بازنمایی‌شده را محدود می‌کند.\n۴. وابستگی به تبلیغات: مدل درآمدی تبلیغاتی، محتوا را به سمت مخاطب پسند و آگهی‌پسند می‌برد و نظارت انتقادی را تضعیف می‌کند.\n۵. دسترسی و بازنمایی: گروه‌های محروم اگر صدای رسانه‌ای نداشته باشند، در گفت‌وگوی عمومی غایب می‌مانند.\n۶. سیاست رسانه‌ای: بخش عمومی، رسانه شهروندی، تنظیم مالکیت و حمایت از روزنامه‌نگاری، سازوکارهای اصلاح‌اند.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا رسانه‌های تجاری در بحران‌های سیاسی محافظه‌کار می‌شوند، چرا رسانه خدمات عمومی برای تنوع اهمیت دارد و چرا پلتفرم‌ها با وجود دسترسی گسترده، می‌توانند تمرکز قدرت ارتباطی را بازتولید کنند. نکته مهم این است که دموکراسی رسانه‌ای، محصول بازار یا فناوری به‌تنهایی نیست؛ محصول سیاست و نهاد است.",
        "assumptions": [
            "رسانه مستقل و متنوع، شرط دموکراسی است.",
            "بازار به‌تنهایی تنوع و نظارت کافی تولید نمی‌کند.",
            "سیاست رسانه‌ای می‌تواند کارکرد دموکراتیک را تقویت یا تضعیف کند.",
        ],
        "principles": [
            "تنوع مالکیت، شرط تنوع دیدگاه است.",
            "استقلال از آگهی‌دهنده، شرط نظارت انتقادی است.",
            "دسترسی گروه‌های محروم، معیار دموکراتیک‌بودن رسانه است.",
        ],
        "critiques": [
            "۱. آرمان‌گرایی حوزه عمومی: گفت‌وگوی عقلانی، همه تعاملات رسانه‌ای را توصیف نمی‌کند.\n۲. نمونه غربی: الگوی لیبرال دموکراسی، تجربه کشورهای دیگر را پوشش نمی‌دهد.\n۳. کم‌توجهی به پلتفرم: تمرکز بر رسانه جمعی، منطق الگوریتمی را در نظر نمی‌گیرد.\n۴. فرض مخاطب عقلانی: احساس، سرگرمی و هویت در مصرف رسانه سهم دارند.\n۵. رابطه پیچیده با دولت: تنظیم می‌تواند هم حمایت و هم کنترل باشد.",
        ],
        "applications": [
            "سیاست رسانه‌ای: طراحی حمایت از تنوع مالکیت و رسانه عمومی.",
            "سواد رسانه‌ای: آموزش تشخیص کیفیت گفت‌وگوی عمومی.",
            "تحلیل خبر: سنجش تنوع منابع و بازنمایی گروه‌ها.",
            "مطالعات پلتفرم: بررسی تمرکز قدرت ارتباطی در محیط دیجیتال.",
        ],
        "evolution": "نظریه لیبرال مطبوعات، رسانه را نگهبان دموکراسی می‌دید. پژوهش انتقادی دهه ۱۹۸۰ و ۱۹۹۰ نشان داد که بازار و مالکیت، این کارکرد را محدود می‌کنند؛ از این رو بحث بخش عمومی، رسانه شهروندی و تنظیم مالکیت شکل گرفت و در محیط پلتفرمی بازخوانی شد.",
        "key_concepts": [
            "حوزه عمومی (Public Sphere)",
            "نظارت رسانه‌ای (Media Watchdog)",
            "تنوع مالکیت (Media Ownership Diversity)",
            "رسانه شهروندی (Citizen Media)",
            "رسانه خدمات عمومی (Public Service Media)",
            "شکاف دسترسی (Access Divide)",
        ],
        "studies": [
            "Curran, J. (1991). Mass media and democracy: A reappraisal. In Mass media and society. Edward Arnold.",
            "Habermas, J. (1989). The structural transformation of the public sphere. MIT Press.",
        ],
        "theorists": "کران؛ هابرماس",
        "theorists_text": "کران (۱۹۹۱)؛ هابرماس (۱۹۸۹)",
        "year": 1991,
        "model": "مدل شرایط دموکراتیک: تنوع مالکیت + استقلال از آگهی + دسترسی گروه‌ها + سیاست حمایتی → اطلاع‌رسانی، نظارت و گفت‌وگوی عمومی.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nاین حوزه، سنت لیبرال مطبوعات را با اقتصاد سیاسی و نظریه حوزه عمومی پیوند می‌دهد. نوآوری کران این بود که نشان داد بازار آزاد، تنوع مطلوب نظریه لیبرال را تولید نمی‌کند؛ از این رو به جای انتخاب میان بازار و دولت، ترکیبی از بخش‌های عمومی، تجاری و شهروندی را پیشنهاد کرد.\n\n۲. منطق سنجش و دام‌های آن\nسنجش نیازمند تحلیل هم‌زمان ساختار مالکیت، محتوا و دسترسی است. پژوهش‌هایی که تنها محتوا را تحلیل می‌کنند، ساختار را نمی‌بینند؛ و پژوهش‌هایی که تنها مالکیت را می‌سنجند، کیفیت گفت‌وگو را از دست می‌دهند.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در پیوند ساختار و کیفیت دموکراسی است، اما باید با تحلیل پلتفرم و زمینه ملی تکمیل شود. در محیط شبکه‌ای، دسترسی گسترده‌تر شده، اما تمرکز داده و الگوریتم، شکل تازه‌ای از قدرت ارتباطی ساخته است.",
        "critique_text": "\n".join([
            "۱. آرمان‌گرایی حوزه عمومی: گفت‌وگوی عقلانی همه تعاملات را توصیف نمی‌کند.",
            "۲. نمونه غربی: الگوی لیبرال دموکراسی تجربه کشورهای دیگر را پوشش نمی‌دهد.",
            "۳. کم‌توجهی به پلتفرم: منطق الگوریتمی در نظر گرفته نمی‌شود.",
            "۴. فرض مخاطب عقلانی: احساس و سرگرمی سهم دارند.",
            "۵. رابطه پیچیده با دولت: تنظیم می‌تواند هم حمایت و هم کنترل باشد.",
        ]),
        "example_text": "شهری دو روزنامه دارد؛ هر دو به یک گروه تجاری تعلق دارند و بیشتر درآمدشان از آگهی است. پوشش انتقادی یک شرکت بزرگ کاهش می‌یابد، نه به فرمان کسی، بلکه به دلیل ساختار. افزودن یک رسانه محلی غیرانتفاعی، تنوع و نظارت را بازمی‌گرداند.",
    },
    "MC-515": {
        "summary": "(مکلوهان، ۱۹۶۴؛ اینیس) قطعیت تکنولوژیک می‌گوید شکل فناوری رسانه، بیش از محتوای آن، جامعه و ادراک را دگرگون می‌کند. مکلوهان با جمله «رسانه پیام است» استدلال کرد که هر رسانه، امتدادی از حواس انسان است و نسبت حواس و شیوه اندیشیدن را تغییر می‌دهد. اینیس پیش‌تر نشان داده بود که سوگیری رسانه به زمان یا مکان، ساختار قدرت و گستره امپراتوری را شکل می‌دهد. نقد اصلی این است که این چارچوب، فناوری را عامل تعیین‌کننده می‌بیند و عاملیت انسانی، زمینه اجتماعی و مناسبات قدرت را کم‌رنگ می‌کند.",
        "definition": "قطعیت تکنولوژیک، رویکردی است که تغییر اجتماعی و فرهنگی را تابع ویژگی‌های شکلی فناوری، به‌ویژه فناوری رسانه، می‌داند و اثر محتوا را در برابر اثر شکل رسانه ثانویه می‌شمارد.",
        "main_problem": "مسئله این است که چه چیزی جامعه را بیشتر تغییر می‌دهد: پیام رسانه یا خود رسانه. مکلوهان پاسخ می‌دهد که شکل رسانه، ساختار ادراک و تعامل را بازآرایی می‌کند و محتوا فقط درون این ساختار عمل می‌کند. پرسش دوم، حد این تعیین‌کنندگی است: آیا فناوری علت مستقل است یا در بستر نهادها و منافع عمل می‌کند.",
        "mechanism": "۱. رسانه به‌عنوان امتداد حواس: هر فناوری، توانایی حسی یا بدنی انسان را گسترش می‌دهد و نسبت حواس را تغییر می‌دهد.\n۲. تغییر نسبت حواس و ادراک: چیرگی یک حس، شیوه اندیشیدن، حافظه و تجربه زمان را دگرگون می‌کند.\n۳. سوگیری زمان و مکان: رسانه‌های زمان‌محور، تداوم و سنت را و رسانه‌های مکان‌محور، گسترش و کنترل را تقویت می‌کنند.\n۴. فشردگی زمان و مکان: رسانه الکترونیک، فاصله را کاهش می‌دهد و آگاهی جهانی می‌سازد.\n۵. رسانه گرم و سرد: میزان مشارکت حسی مخاطب در هر رسانه متفاوت است و پیامد اجتماعی متفاوتی دارد.\n۶. شکل اجتماعی و ساختار قدرت: ویژگی شکلی رسانه، الگوی سازمان‌دهی سیاسی و اقتصادی را ممکن یا دشوار می‌کند.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا ظهور چاپ، تلویزیون و اینترنت با دگرگونی‌های گسترده اجتماعی همراه بود، چرا تغییر رسانه را نمی‌توان تنها با تغییر محتوا فهمید و چرا تحلیل رسانه باید شکل و زیرساخت را ببیند. نکته مهم این است که نسخه سخت این نظریه نقد شده است؛ نسخه نرم می‌گوید فناوری شرایط امکان می‌سازد، نه نتیجه قطعی.",
        "assumptions": [
            "شکل رسانه، اثر مستقل و نیرومندی بر ادراک و جامعه دارد.",
            "فناوری، امتداد حواس و توانایی‌های انسان است.",
            "تغییر رسانه، الگوی تعامل و سازمان اجتماعی را دگرگون می‌کند.",
        ],
        "principles": [
            "رسانه، محیط است و نه فقط کانال انتقال پیام.",
            "سوگیری رسانه، ساختار قدرت را شکل می‌دهد.",
            "اثر شکل رسانه را نمی‌توان به محتوا فروکاست.",
        ],
        "critiques": [
            "۱. جبرگرایی: فناوری علت اصلی تغییر فرض می‌شود و عاملیت انسانی نادیده می‌ماند.\n۲. ابهام مفهومی: مفاهیمی مانند رسانه گرم و سرد، دقیق و آزمون‌پذیر نیستند.\n۳. کم‌توجهی به محتوا و زمینه: معنا، نهاد و منافع در تحلیل کم‌رنگ می‌شوند.\n۴. نمونه‌گزینی تاریخی: روایت تاریخ رسانه، گزینشی و کلی است.\n۵. نسخه نرم: ویلیامز نشان داد فناوری در بستر تصمیم‌های اجتماعی و اقتصادی شکل می‌گیرد.",
        ],
        "applications": [
            "تحلیل رسانه: بررسی اثر شکل رسانه در کنار محتوا.",
            "مطالعات فناوری: تحلیل رابطه فناوری، نهاد و تغییر اجتماعی.",
            "آموزش سواد رسانه‌ای: توجه به محیط رسانه‌ای و نه فقط پیام.",
            "تاریخ رسانه: تحلیل پیوند رسانه و ساختار قدرت.",
        ],
        "evolution": "اینیس در دهه ۱۹۵۰ سوگیری رسانه را صورت‌بندی کرد و مکلوهان در ۱۹۶۴ آن را به نظریه‌ای عمومی گسترد. نقدهای ویلیامز و پژوهش‌های بعدی، نسخه سخت را تعدیل کرد و بر تعامل فناوری، نهاد و عاملیت تأکید کرد.",
        "key_concepts": [
            "رسانه پیام است (The Medium is the Message)",
            "امتداد حواس (Extensions of Man)",
            "سوگیری رسانه (Bias of Communication)",
            "دهکده جهانی (Global Village)",
            "رسانه گرم و سرد (Hot and Cool Media)",
            "جبرگرایی فناورانه (Technological Determinism)",
        ],
        "studies": [
            "McLuhan, M. (1964). Understanding media: The extensions of man. McGraw-Hill.",
            "Innis, H. A. (1951). The bias of communication. University of Toronto Press.",
        ],
        "theorists": "مکلوهان؛ اینیس",
        "theorists_text": "مارشال مکلوهان (۱۹۶۴)؛ هارولد اینیس (۱۹۵۱)",
        "year": 1964,
        "model": "مدل شکلی: ویژگی فناوری رسانه → تغییر نسبت حواس و ساختار تعامل → دگرگونی سازمان اجتماعی و فرهنگی.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nمکتب تورنتو، رسانه را نه وسیله انتقال پیام، بلکه محیط شکل‌دهنده تجربه دید. نوآوری مکلوهان، جابه‌جایی توجه از محتوا به شکل بود؛ ایده‌ای که مطالعات رسانه را از تحلیل پیام به تحلیل زیرساخت و محیط گسترد.\n\n۲. منطق سنجش و دام‌های آن\nسنجش نیازمند مقایسه دوره‌های رسانه‌ای و تحلیل تغییر ساختار ادراک و تعامل است. پژوهش‌هایی که تنها محتوا را می‌سنجند، شکل را از دست می‌دهند؛ و پژوهش‌هایی که تنها فناوری را می‌بینند، نهاد و عاملیت را نادیده می‌گیرند.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در دیدن زیرساخت رسانه است، اما باید از جبرگرایی پرهیز کند. در محیط پلتفرمی، شکل تازه رسانه — داده، الگوریتم و رابط — اثر مستقل دارد؛ تحلیل بدون دیدن این شکل، ناقص است.",
        "critique_text": "\n".join([
            "۱. جبرگرایی: فناوری علت اصلی تغییر فرض می‌شود.",
            "۲. ابهام مفهومی: رسانه گرم و سرد دقیق و آزمون‌پذیر نیست.",
            "۳. کم‌توجهی به محتوا و زمینه: معنا و نهاد کم‌رنگ می‌شوند.",
            "۴. نمونه‌گزینی تاریخی: روایت تاریخ رسانه گزینشی است.",
            "۵. نسخه نرم: فناوری در بستر تصمیم‌های اجتماعی شکل می‌گیرد.",
        ]),
        "example_text": "ورود تلویزیون به خانه، تنها برنامه‌ها را عوض نکرد؛ زمان خواب، الگوی گفت‌وگوی خانوادگی و مرز اطلاعاتی کودکان و بزرگسالان را نیز تغییر داد. حتی اگر محتوای برنامه بی‌ضرر باشد، شکل رسانه اثر خود را می‌گذارد.",
    },
    "MC-516": {
        "summary": "(مایروویتز، ۱۹۸۵) مایروویتز رسانه را نه کانال پیام، بلکه محیطی می‌دید که «موقعیت‌های اجتماعی» را بازآرایی می‌کند. رسانه الکترونیک پیوند دیرینه مکان و تعامل را می‌شکند: مخاطب از هر جا در معرض رویدادها و اطلاعاتی قرار می‌گیرد که پیش‌تر مخصوص جای دیگری بود. نتیجه، جابه‌جایی مرز صحنه و پشت صحنه است؛ کودک و بزرگسال، زن و مرد و رهبر و پیرو بیش از پیش در معرض اطلاعات یکسان قرار می‌گیرند. به همین دلیل، اثر رسانه در تغییر ساختار موقعیت و هویت است، نه فقط در اقناع مستقیم.",
        "definition": "نظریه رسانه به‌عنوان واسطه، رسانه را محیطی می‌داند که با جدا کردن تعامل از مکان، مرز موقعیت‌های اجتماعی را جابه‌جا می‌کند و الگوی نقش، هویت و اقتدار را دگرگون می‌سازد.",
        "main_problem": "مسئله این است که چرا رسانه‌های الکترونیک، الگوهای رفتاری و هویتی را دگرگون می‌کنند، حتی وقتی پیام مشخصی برای تغییر رفتار نمی‌فرستند. پاسخ در ساختار موقعیت است: رسانه، دسترسی به اطلاعات پشت صحنه را همگانی می‌کند و مرزهای نقش را می‌شکند. پرسش دوم، پیامد است: چه اتفاقی برای اقتدار، حریم و هویت رخ می‌دهد وقتی همه در یک محیط اطلاعاتی مشترک قرار می‌گیرند.",
        "mechanism": "۱. رسانه به‌عنوان محیط: رسانه، بستری است که تجربه و تعامل در آن شکل می‌گیرد؛ اثر آن به محتوا محدود نیست.\n۲. شکستن پیوند مکان و تعامل: در رسانه الکترونیک، حضور فیزیکی شرط تعامل نیست و تجربه از مکان جدا می‌شود.\n۳. جابه‌جایی مرز صحنه و پشت صحنه: اطلاعاتی که پیش‌تر پنهان بود، آشکار می‌شود و مرز رفتار رسمی و غیررسمی مخدوش می‌گردد.\n۴. بازتعریف موقعیت اجتماعی: موقعیت، ترکیبی از دسترسی به اطلاعات و حضور در صحنه است؛ رسانه این ترکیب را تغییر می‌دهد.\n۵. ادغام حوزه‌ها: مرزهای کودکی و بزرگسالی، زنانگی و مردانگی، و اقتدار و پیروی کم‌رنگ می‌شود.\n۶. هویت و بی‌حسی مکان: بدون لنگر مکان، هویت از نقش‌های محلی جدا و در معرض مخاطبان گسترده ساخته می‌شود.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا تلویزیون مرز اطلاعاتی کودکان و بزرگسالان را کاهش داد، چرا پلتفرم‌ها حریم و اقتدار را بازتعریف می‌کنند و چرا اثر رسانه را باید در تغییر موقعیت جست، نه فقط در تغییر نگرش. نکته مهم این است که نظریه بیشتر بر تلویزیون متمرکز است؛ در محیط شبکه‌ای، موقعیت‌ها بیش از پیش سیال و چندلایه شده‌اند.",
        "assumptions": [
            "رسانه، محیط شکل‌دهنده تجربه و تعامل است.",
            "مرز موقعیت اجتماعی، تابع دسترسی به اطلاعات است.",
            "رسانه الکترونیک، پیوند مکان و تعامل را می‌شکند.",
        ],
        "principles": [
            "اثر رسانه را باید در ساختار موقعیت جست، نه فقط در محتوا.",
            "آشکارشدن پشت صحنه، اقتدار و نقش را دگرگون می‌کند.",
            "هویت، در محیط اطلاعاتی مشترک بازساخته می‌شود.",
        ],
        "critiques": [
            "۱. تمرکز بر تلویزیون: نظریه با رسانه‌های تعاملی و پلتفرمی به‌سختی تطبیق می‌یابد.\n۲. کم‌توجهی به محتوا و تفسیر: معنا و زمینه فرهنگی کم‌رنگ می‌شود.\n۳. نمونه آمریکایی: شواهد تجربی به یک زمینه ملی محدود است.\n۴. سنجش موقعیت: تعریف و اندازه‌گیری مرز صحنه و پشت صحنه دشوار است.\n۵. تعامل شبکه‌ای: در محیط دیجیتال، مخاطب هم تماشاگر و هم اجراکننده است.",
        ],
        "applications": [
            "مطالعات رسانه: تحلیل تغییر موقعیت و مرز نقش.",
            "حریم خصوصی: بررسی آشکارشدن پشت صحنه در پلتفرم‌ها.",
            "مطالعات کودکی: تحلیل کاهش مرز اطلاعاتی کودکان و بزرگسالان.",
            "جامعه‌شناسی رسانه: پیوند رسانه، مکان و هویت.",
        ],
        "evolution": "مایروویتز در ۱۹۸۵ نظریه را با پیوند گافمن و مکلوهان صورت‌بندی کرد و در ۱۹۹۴ آن را به‌عنوان نظریه رسانه میانی معرفی کرد. پژوهش بعدی، مفهوم را به اینترنت، شبکه‌های اجتماعی و حریم دیجیتال گسترد.",
        "key_concepts": [
            "رسانه به‌عنوان محیط (Media as Environment)",
            "موقعیت اجتماعی (Social Situation)",
            "صحنه و پشت صحنه (Front and Back Region)",
            "بی‌حسی مکان (No Sense of Place)",
            "مرز نقش (Role Boundary)",
            "رسانه میانی (Medium Theory)",
        ],
        "studies": [
            "Meyrowitz, J. (1985). No sense of place. Oxford University Press.",
            "Meyrowitz, J. (1994). Medium theory. In Communication theory today (pp. 50-77). Polity.",
        ],
        "theorists": "جاشوا مایروویتز (۱۹۸۵)",
        "theorists_text": "جاشوا مایروویتز (۱۹۸۵)",
        "year": 1985,
        "model": "مدل موقعیتی: رسانه → جدایی تعامل از مکان → آشکارشدن پشت صحنه → بازتعریف موقعیت و نقش → تغییر هویت و اقتدار.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nمایروویتز، جامعه‌شناسی صحنه گافمن را با نظریه رسانه مکلوهان ترکیب کرد. نوآوری او این بود که اثر رسانه را از سطح نگرش به سطح ساختار موقعیت برد؛ رسانه، چیدمان صحنه اجتماعی را عوض می‌کند.\n\n۲. منطق سنجش و دام‌های آن\nسنجش نیازمند تحلیل دسترسی به اطلاعات، تغییر مرز نقش و بازتعریف موقعیت است. پژوهش‌هایی که تنها نگرش مخاطب را می‌سنجند، ساختار موقعیت را از دست می‌دهند؛ و پژوهش‌هایی که تنها محتوا را تحلیل می‌کنند، تغییر محیط را نمی‌بینند.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در توضیح تغییر اقتدار و حریم است، اما باید برای محیط شبکه‌ای تعدیل شود. در پلتفرم‌ها، مرز صحنه و پشت صحنه نه حذف، بلکه پیوسته مذاکره می‌شود؛ کاربر هم اجرا می‌کند و هم تماشا.",
        "critique_text": "\n".join([
            "۱. تمرکز بر تلویزیون: نظریه با رسانه‌های تعاملی به‌سختی تطبیق می‌یابد.",
            "۲. کم‌توجهی به محتوا و تفسیر: زمینه فرهنگی کم‌رنگ می‌شود.",
            "۳. نمونه آمریکایی: شواهد تجربی به یک زمینه ملی محدود است.",
            "۴. سنجش موقعیت: اندازه‌گیری مرز صحنه و پشت صحنه دشوار است.",
            "۵. تعامل شبکه‌ای: مخاطب هم تماشاگر و هم اجراکننده است.",
        ]),
        "example_text": "کودکی که پیش‌تر از گفت‌وگوهای بزرگسالان دور نگه داشته می‌شد، با تلویزیون به همان اطلاعات دسترسی پیدا می‌کند. مرز اطلاعاتی فرو می‌ریزد و اقتدار بزرگسال بر دانستن، تضعیف می‌شود؛ این همان جابه‌جایی موقعیت است که مایروویتز توصیف کرد.",
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
                                       "verified": n_verified, "batch": 93}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH93 THEORY DONE")


if __name__ == "__main__":
    main()
