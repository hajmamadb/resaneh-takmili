# -*- coding: utf-8 -*-
"""Batch 78: full documentation for MC-409..MC-411 and MC-413."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch78-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch78_theory.json"

S = {
    "MC-409": [
        dict(kind="BOOK",
             title_en="Reassembling the Social: An Introduction to Actor-Network-Theory",
             title_fa="بازآرایش امر اجتماعی: درآمدی بر نظریه کنشگر-شبکه",
             authors="Latour, B.", year=2005, publisher="Oxford University Press",
             doi=None, url="https://academic.oup.com/book/52349",
             language="en", isbn="9780199256044",
             citation="Latour, B. (2005). Reassembling the social: An introduction to actor-network-theory. Oxford University Press.",
             locator="work", locator_type="work",
             supports="ANT principles / symmetry / associations", verified=True),
        dict(kind="BOOK_CHAPTER",
             title_en="Some Elements of a Sociology of Translation: Domestication of the Scallops and the Fishermen of St Brieuc Bay",
             title_fa="عناصری از جامعه‌شناسی ترجمه",
             authors="Callon, M.", year=1986, publisher="Routledge",
             doi=None, url=None, language="en", isbn=None,
             citation="Callon, M. (1986). Some elements of a sociology of translation: Domestication of the scallops and the fishermen of St Brieuc Bay. In J. Law (Ed.), Power, action and belief (pp. 196-233). Routledge.",
             locator="pp. 196-233", locator_type="page_range",
             supports="translation / enrolment", verified=False),
    ],
    "MC-410": [
        dict(kind="BOOK",
             title_en="No Sense of Place: The Impact of Electronic Media on Social Behavior",
             title_fa="بی‌حسی مکان: تأثیر رسانه‌های الکترونیک بر رفتار اجتماعی",
             authors="Meyrowitz, J.", year=1985, publisher="Oxford University Press",
             doi=None, url="https://global.oup.com/academic/product/no-sense-of-place-9780195042313",
             language="en", isbn="9780195042313",
             citation="Meyrowitz, J. (1985). No sense of place: The impact of electronic media on social behavior. Oxford University Press.",
             locator="work", locator_type="work",
             supports="media as environment / situational geography", verified=True),
        dict(kind="BOOK_CHAPTER",
             title_en="Medium Theory",
             title_fa="نظریه رسانه",
             authors="Meyrowitz, J.", year=1994, publisher="Polity Press",
             doi=None, url=None, language="en", isbn=None,
             citation="Meyrowitz, J. (1994). Medium theory. In D. Crowley & D. Mitchell (Eds.), Communication theory today (pp. 50-77). Polity Press.",
             locator="pp. 50-77", locator_type="page_range",
             supports="medium theory elaboration", verified=False),
    ],
    "MC-411": [
        dict(kind="BOOK",
             title_en="Consuming Technologies: Media and Information in Domestic Spaces",
             title_fa="مصرف فناوری‌ها: رسانه و اطلاعات در فضاهای خانگی",
             authors="Silverstone, R.; Hirsch, E. (eds.)", year=1992, publisher="Routledge",
             doi=None, url="https://www.jstor.org/stable/690186",
             language="en", isbn=None,
             citation="Silverstone, R., & Hirsch, E. (Eds.). (1992). Consuming technologies: Media and information in domestic spaces. Routledge.",
             locator="work", locator_type="work",
             supports="domestication / moral economy of household", verified=True),
        dict(kind="BOOK_CHAPTER",
             title_en="Information and Communication Technologies and the Moral Economy of the Household",
             title_fa="فناوری‌های اطلاعات و ارتباطات و اقتصاد اخلاقی خانواده",
             authors="Silverstone, R.; Hirsch, E.; Morley, D.", year=1992, publisher="Routledge",
             doi=None, url=None, language="en", isbn=None,
             citation="Silverstone, R., Hirsch, E., & Morley, D. (1992). Information and communication technologies and the moral economy of the household. In R. Silverstone & E. Hirsch (Eds.), Consuming technologies (pp. 15-31). Routledge.",
             locator="pp. 15-31", locator_type="page_range",
             supports="four phases / moral economy", verified=False),
    ],
    "MC-413": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="User Acceptance of Information Technology: Toward a Unified View",
             title_fa="پذیرش فناوری اطلاعات توسط کاربر: به سوی دیدگاهی یکپارچه",
             authors="Venkatesh, V.; Morris, M. G.; Davis, G. B.; Davis, F. D.", year=2003,
             publisher="MIS Quarterly", doi=None,
             url="https://misq.umn.edu/misq/article/27/3/425/1340/User-Acceptance-of-Information-Technology-Toward-A",
             language="en", isbn=None,
             citation="Venkatesh, V., Morris, M. G., Davis, G. B., & Davis, F. D. (2003). User acceptance of information technology: Toward a unified view. MIS Quarterly, 27(3), 425-478.",
             locator="pp. 425-478", locator_type="page_range",
             supports="four constructs / moderators / unified model", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Consumer Acceptance and Use of Information Technology: Extending the Unified Theory of Acceptance and Use of Technology",
             title_fa="پذیرش و کاربست مصرف‌کننده: گسترش UTAUT",
             authors="Venkatesh, V.; Thong, J. Y. L.; Xu, X.", year=2012,
             publisher="MIS Quarterly", doi=None, url=None,
             language="en", isbn=None,
             citation="Venkatesh, V., Thong, J. Y. L., & Xu, X. (2012). Consumer acceptance and use of information technology: Extending the unified theory of acceptance and use of technology. MIS Quarterly, 36(1), 157-178.",
             locator="pp. 157-178", locator_type="page_range",
             supports="UTAUT2 extension / consumer context", verified=False),
    ],
}

ENRICH = {
    "MC-409": {
        "summary": "(لاتور، ۲۰۰۵؛ کالون، ۱۹۸۶) نظریه کنشگر-شبکه، جامعه را نه از پیش موجود، بلکه محصول پیوند میان کنشگران انسانی و غیرانسانی می‌داند. اشیا، نرم‌افزار، استانداردها و متن‌ها نیز «کنشگر» محسوب می‌شوند و در ساخت واقعیت اجتماعی سهم دارند. نظریه با رد تفکیک سوژه/ابژه و با «اصل تقارن تعمیم‌یافته»، خواستار ردیابی شبکه‌هایی است که از راه «ترجمه» ساخته و پایدار می‌شوند.",
        "definition": "کنشگر-شبکه واحد تحلیل نیست؛ برعکس، هر کنشگر خود نتیجه اتصال شبکه‌ای از انسان‌ها و ناانسان‌هاست. نظریه کنشگر-شبکه روشی برای توصیف این اتصال‌هاست: دنبال‌کردن مسیرهایی که یک ادعا، یک فناوری یا یک سازمان را پایدار می‌کند، بی‌آنکه به تبیین‌های پیشینی درباره «جامعه» یا «فناوری» متوسل شویم.",
        "main_problem": "مسئله این است که چگونه می‌توان نظم اجتماعی را توضیح داد بدون آنکه یا به جامعه‌شناسی «امر اجتماعی» (نیروهای پنهان) یا به جبر فناورانه فروبکاهیم. پاسخ لاتور: نظم، اثر شبکه‌سازی است، نه داده‌ای پیشین؛ باید دید چه پیوندهایی آن را برپا می‌دارند.",
        "mechanism": "\n".join([
            "۱. تقارن تعمیم‌یافته: انسان و ناانسان با یک واژگان تحلیل می‌شوند؛ هیچ‌کدام پیشاپیش عاملیت یا انفعال ندارند.",
            "۲. کنشگر-شبکه: هر کنشگر، گره‌ای است که خودش از شبکه‌ای از واسطه‌ها ساخته شده است؛ «کنشگر» و «شبکه» دو روی یک سکه‌اند.",
            "۳. ترجمه: فرایندی که در آن کنشگران، منافع و هویت‌های یکدیگر را بازتعریف می‌کنند تا پیوند برقرار شود (مسئله‌سازی، جلب توجه، ثبت‌نام، بسیج).",
            "۴. واسطه در برابر میانجی: واسطه چیزی را تغییر می‌دهد و میانجی صرفاً انتقال می‌دهد؛ قدرت شبکه به تعداد واسطه‌های فعال بسته است.",
            "۵. کتیبه‌گذاری: ارزش‌ها و برنامه‌ها در طراحی اشیا و کدها نوشته می‌شوند و سپس رفتار را شکل می‌دهند.",
            "۶. بازآرایی امر اجتماعی: جامعه‌شناسی باید «انجمن‌ها» را دنبال کند، نه ساختارهای از پیش فرض‌شده؛ توصیف دقیق، جای تبیین جبری را می‌گیرد.",
            "در بستر رسانه، نظریه کنشگر-شبکه اجازه می‌دهد پلتفرم را نه صرفاً ابزار یا نهاد، بلکه شبکه‌ای از سرورها، پروتکل‌ها، قراردادها، الگوریتم‌ها، کاربران و تبلیغ‌دهندگان ببینیم. وقتی یک قابلیت جدید معرفی می‌شود، موفقیت آن به ترجمه منافع این کنشگران وابسته است: آیا تبلیغ‌دهنده آن را می‌پذیرد؟ آیا الگوریتم آن را تقویت می‌کند؟ آیا کاربر آن را در روال روزانه جای می‌دهد؟ این چارچوب، نوآوری رسانه‌ای را از روایت «پذیرش ایده» به تحلیل شبکه‌ای از پیوندها و منافع منتقل می‌کند.",
        ]),
        "assumptions": [
            "مرز میان انسان و ناانسان از نظر تحلیلی قابل تعلیق است.",
            "نظم اجتماعی محصول شبکه‌سازی و ترجمه است، نه داده‌ای پیشین.",
            "توصیف دقیق پیوندها بر تبیین جبری مقدم است.",
        ],
        "principles": [
            "تحلیل باید کنشگران غیرانسانی را نیز در شمار آورد.",
            "به‌جای فرض ساختار، مسیر اتصال‌ها را دنبال کنید.",
            "پایداری یک واقعیت، به شمار و کیفیت واسطه‌های آن بسته است.",
        ],
        "critiques": [
            "انسان‌واره‌سازی اشیا: اعطای عاملیت به ناانسان‌ها می‌تواند به ابهام مفهومی بینجامد و مسئولیت انسانی را تار کند.",
            "کم‌توجهی به قدرت ساختاری: توصیف شبکه‌ها اغلب نابرابری، طبقه و سلطه را که در پس پیوندهاست کم‌برجسته می‌کند.",
            "توصیف به‌جای تبیین: نظریه قوی در ردیابی است اما در توضیح چرایی و پیش‌بینی ضعیف عمل می‌کند.",
            "دشواری تجربی: ردیابی کامل شبکه‌ها در عمل بی‌پایان و پرهزینه است و مرز تحلیل مبهم می‌شود.",
            "بی‌طرفی سیاسی: تمرکز بر تقارن می‌تواند به بی‌تفاوتی نسبت به پیامدهای اخلاقی و توزیعی بینجامد.",
        ],
        "applications": [
            "تحلیل توسعه فناوری و نوآوری رسانه‌ای.",
            "مطالعه زیرساخت پلتفرم و زنجیره کنشگران.",
            "پژوهش درباره پذیرش یا شکست نوآوری در سازمان.",
            "طراحی مداخله با شناسایی گره‌های کلیدی شبکه.",
        ],
        "evolution": "نظریه در دهه ۱۹۸۰ در مطالعات علم و فناوری شکل گرفت (لاتور، کالون، لاو) و در «بازآرایی امر اجتماعی» (۲۰۰۵) صورت روش‌شناختی یافت. در دهه ۲۰۱۰ به تحلیل پلتفرم، الگوریتم و زیرساخت راه یافت و بحث «امور مورد توجه» لاتور، آن را به حوزه عمومی و بحران اقلیمی گستراند.",
        "key_concepts": [
            "کنشگر-شبکه (actor-network)",
            "اصل تقارن تعمیم‌یافته (generalized symmetry)",
            "ترجمه (translation)",
            "ثبت‌نام (enrolment)",
            "کتیبه‌گذاری (inscription)",
            "واسطه/میانجی (mediator/intermediary)",
        ],
        "studies": [
            "Latour, B. (2005). Reassembling the social: An introduction to actor-network-theory. Oxford University Press.",
            "Callon, M. (1986). Some elements of a sociology of translation. In J. Law (Ed.), Power, action and belief (pp. 196-233). Routledge.",
        ],
        "theorists": "برونو لاتور، میشل کالون و جان لاو (Bruno Latour, Michel Callon & John Law)",
        "model": "زنجیره ترجمه: مسئله‌سازی ← جلب توجه ← ثبت‌نام کنشگران ← بسیج شبکه ← تثبیت در اشیا و استانداردها؛ با ردیابی واسطه‌ها به‌جای فرض ساختار.",
        "detailed_analysis": "\n\n".join([
            "۱. بنیان و منطق نظری\nنظریه کنشگر-شبکه از مطالعات آزمایشگاه لاتور و وولگار برخاست و در آثار کالون و لاو بسط یافت. ایده مرکزی آن است که «اجتماعی» صفت اشیا نیست، بلکه پیوندی است که باید ساخته و نگه‌داشته شود. از این منظر، فناوری و جامعه دو قلمرو جدا نیستند؛ هر دو اثر شبکه‌ای از واسطه‌ها هستند.",
            "۲. سازوکار عملی و تشخیصی\nبرای تحلیل یک نوآوری، سه پرسش مطرح می‌شود: چه کنشگرانی (انسانی و غیرانسانی) درگیرند؟ منافع آن‌ها چگونه ترجمه شده است؟ و کدام گره‌ها در صورت حذف، شبکه را فرومی‌پاشند؟ این پرسش‌ها چارچوب را از استعاره به روش ردیابی تجربی بدل می‌کند.",
            "۳. دلالت‌ها برای پژوهش رسانه\nپژوهش معاصر از این چارچوب برای تحلیل زیرساخت پلتفرم، زنجیره تأمین داده و پذیرش الگوریتم استفاده می‌کند. پرسش باز: آیا می‌توان کنشگران غیرانسانی را در تحلیل قدرت جای داد، بی‌آنکه مسئولیت انسانی و نابرابری ساختاری محو شود؟",
        ]),
        "critique_text": "\n".join([
            "۱. انسان‌واره‌سازی اشیا: اعطای عاملیت به ناانسان‌ها می‌تواند به ابهام مفهومی بینجامد و مسئولیت انسانی را تار کند.",
            "۲. کم‌توجهی به قدرت ساختاری: توصیف شبکه‌ها اغلب نابرابری، طبقه و سلطه را که در پس پیوندهاست کم‌برجسته می‌کند.",
            "۳. توصیف به‌جای تبیین: نظریه قوی در ردیابی است اما در توضیح چرایی و پیش‌بینی ضعیف عمل می‌کند.",
            "۴. دشواری تجربی: ردیابی کامل شبکه‌ها در عمل بی‌پایان و پرهزینه است و مرز تحلیل مبهم می‌شود.",
            "۵. بی‌طرفی سیاسی: تمرکز بر تقارن می‌تواند به بی‌تفاوتی نسبت به پیامدهای اخلاقی و توزیعی بینجامد.",
        ]),
        "example_text": "راه‌اندازی یک سیستم توصیه خبری در یک خبرگزاری، فقط تصمیم مدیران نیست: الگوریتم، داده آموزشی، تیم فنی، روزنامه‌نگاران، قواعد حقوقی و عادت مخاطبان همه کنشگرند. اگر روزنامه‌نگاران سامانه را «جعبه سیاه» ببینند و داده کافی در اختیارش نگذارند، شبکه ناپایدار می‌شود. تحلیل کنشگر-شبکه نشان می‌دهد شکست یا موفقیت، حاصل ترجمه منافع این گره‌هاست، نه کیفیت فنی صرف.",
    },
    "MC-410": {
        "summary": "(میروویتز، ۱۹۸۵) نظریه رسانه به‌عنوان بستر، رسانه‌های الکترونیک را محیط‌هایی می‌داند که «جغرافیای موقعیت‌ها» را بازآرایی می‌کنند. تلویزیون با درهم‌آمیختن موقعیت‌های اجتماعی که پیش‌تر با مکان فیزیکی جدا می‌شدند، مرزهای عمومی/خصوصی، بزرگسال/کودک و مرد/زن را می‌شکند. نتیجه آن، «بی‌حسی مکان» است: جایگاه اجتماعی دیگر با جای فیزیکی تعریف نمی‌شود.",
        "definition": "رسانه به‌عنوان بستر، دیدگاهی است که رسانه را نه کانال انتقال پیام، بلکه محیطی می‌بیند که موقعیت‌های اجتماعی را می‌سازد یا در هم می‌آمیزد. بر پایه سنت گافمن، رفتار اجتماعی وابسته به تعریف موقعیت است؛ رسانه‌های الکترونیک با تغییر مرز موقعیت‌ها، هویت و سلسله‌مراتب را نیز تغییر می‌دهند.",
        "main_problem": "مسئله این است که چرا در عصر تلویزیون، نقش‌های اجتماعی و مرزهای حریم خصوصی به‌سرعت دگرگون شدند، بدون آنکه محتوای برنامه‌ها لزوماً تغییر کرده باشد. میروویتز پاسخ می‌دهد که خودِ شکل رسانه، موقعیت‌ها را بازآرایی می‌کند.",
        "mechanism": "\n".join([
            "۱. موقعیت به‌جای مکان: موقعیت اجتماعی مجموعه‌ای از انتظارات نقش است؛ رسانه می‌تواند آن را از مکان فیزیکی جدا کند.",
            "۲. رسانه به‌عنوان محیط: هر رسانه، فضایی از دسترسی و آگاهی می‌سازد که رفتار ممکن را تعریف می‌کند.",
            "۳. ادغام موقعیت‌ها: تلویزیون صحنه‌هایی را که پیش‌تر جدا بودند (خانه، محل کار، مدرسه) به یک فضای مشترک می‌آورد.",
            "۴. فروپاشی جدایی بزرگسال/کودک: کودکان به اطلاعات بزرگسالان دسترسی می‌یابند و مرز اقتدار آموزشی سست می‌شود.",
            "۵. افشای پشت‌صحنه: رسانه، پشت صحنه نهادها را به روی همه می‌گشاید و اقتدار را از رمز و فاصله تهی می‌کند.",
            "۶. بازآرایی سلسله‌مراتب: گروه‌هایی که پیش‌تر از فضای عمومی حذف بودند، امکان دیده‌شدن می‌یابند؛ هم‌زمان، حریم خصوصی فرومی‌پاشد.",
            "در بستر رسانه، منطق میروویتز در عصر رسانه‌های اجتماعی به اوج می‌رسد: «ادغام بافت» (context collapse) باعث می‌شود مخاطب ناشناخته، همکار و خانواده در یک فید واحد حاضر باشند و کاربر نتواند مرزهای اجرای نقش را حفظ کند. اسکرول بی‌پایان، دسترسی به پشت صحنه دیگران را به سرگرمی بدل می‌کند و حریم خصوصی را به مذاکره‌ای دائمی تبدیل می‌کند. همان طور که میروویتز پیش‌بینی می‌کرد، تغییر اصلی نه در محتوای پیام‌ها، بلکه در ساختار موقعیت‌هایی است که رسانه می‌سازد.",
        ]),
        "assumptions": [
            "رفتار اجتماعی وابسته به تعریف موقعیت است.",
            "رسانه‌های الکترونیک، موقعیت‌ها را از مکان فیزیکی جدا می‌کنند.",
            "شکل رسانه مستقل از محتوا، ساختار اجتماعی را تغییر می‌دهد.",
        ],
        "principles": [
            "اثر رسانه را در بازآرایی موقعیت‌ها جست‌وجو کنید، نه فقط در پیام‌ها.",
            "مرزهای عمومی/خصوصی، محصول دسترسی رسانه‌ای‌اند.",
            "تغییر رسانه، تغییر سلسله‌مراتب و اقتدار است.",
        ],
        "critiques": [
            "جبر رسانه‌ای نرم: شکل رسانه تقریباً علت اصلی فرض می‌شود و تفسیر مخاطب، محتوا و بستر نهادی کم‌برجسته می‌شوند.",
            "تمرکز بر تلویزیون: مدل برای دوران پخش طراحی شده و تعمیم آن به رسانه‌های تعاملی و شخصی‌سازی‌شده نیازمند بازنگری است.",
            "شواهد تاریخی گزینشی: ادعاهای مربوط به فروپاشی نقش‌ها با شواهد تجربی نظام‌مند کمی پشتیبانی شده‌اند.",
            "کم‌توجهی به محتوا: تأکید بر «شکل» می‌تواند تفاوت برنامه‌ها و ایدئولوژی‌های رسانه‌ای را نادیده بگیرد.",
            "پیوند ناقص با گافمن: مفهوم موقعیت گافمن برای تعامل رودررو ساخته شد و انتقال آن به رسانه‌های جمعی نیازمند استدلال بیشتر است.",
        ],
        "applications": [
            "تحلیل مرزهای عمومی/خصوصی در شبکه‌های اجتماعی.",
            "پژوهش درباره هویت و اجرای نقش آنلاین.",
            "آموزش سواد رسانه‌ای و مدیریت حریم خصوصی.",
            "مطالعه اثر رسانه بر اقتدار نهادی.",
        ],
        "evolution": "میروویتز در ۱۹۸۵ نظریه را با تکیه بر تلویزیون صورت‌بندی کرد و در ۱۹۹۴ آن را در چارچوب «نظریه رسانه» جای داد. پژوهش‌های بعدی، منطق ادغام موقعیت‌ها را به اینترنت، شبکه‌های اجتماعی و «ادغام بافت» تعمیم دادند و آن را با مطالعات حریم خصوصی و اجرای هویت پیوند زدند.",
        "key_concepts": [
            "بی‌حسی مکان (no sense of place)",
            "جغرافیای موقعیت (situational geography)",
            "ادغام موقعیت (situation merging)",
            "پشت‌صحنه (backstage)",
            "ادغام بافت (context collapse)",
            "نظریه رسانه (medium theory)",
        ],
        "studies": [
            "Meyrowitz, J. (1985). No sense of place: The impact of electronic media on social behavior. Oxford University Press.",
            "Meyrowitz, J. (1994). Medium theory. In D. Crowley & D. Mitchell (Eds.), Communication theory today (pp. 50-77). Polity Press.",
        ],
        "theorists": "جاشوا میروویتز (Joshua Meyrowitz)",
        "model": "زنجیره اثر: رسانه الکترونیک ← ادغام موقعیت‌ها ← از میان‌رفتن مرز مکان/نقش ← افشای پشت‌صحنه ← بازآرایی هویت و سلسله‌مراتب.",
        "detailed_analysis": "\n\n".join([
            "۱. بنیان و منطق نظری\nمیروویتز با ترکیب سنت گافمن (اجرای نقش و پشت‌صحنه) و نظریه رسانه مک‌لوهان، پرسشی تازه ساخت: اگر رفتار به موقعیت وابسته است، رسانه‌ای که موقعیت‌ها را در هم می‌آمیزد چه اثری بر نقش‌ها دارد؟ پاسخ او این بود که تلویزیون «جغرافیای موقعیت» را تغییر می‌دهد و از این راه، مرزهای اجتماعی را جابه‌جا می‌کند.",
            "۲. سازوکار عملی و تشخیصی\nبرای تحلیل یک رسانه، سه پرسش مطرح می‌شود: چه کسانی را در یک فضای مشترک گرد هم می‌آورد؟ چه مرزهایی (عمومی/خصوصی، کودک/بزرگسال) را می‌شکند؟ و چه پشت‌صحنه‌هایی را افشا می‌کند؟ پاسخ این پرسش‌ها، اثر رسانه را از محتوای صرف جدا می‌کند.",
            "۳. دلالت‌ها برای پژوهش رسانه\nپژوهش معاصر منطق میروویتز را در شبکه‌های اجتماعی، ویدیوی زنده و واقعیت مجازی به کار می‌برد. پرسش باز: در محیطی که هر کاربر خود رسانه است، آیا «موقعیت» هنوز واحد تحلیلی مفیدی است یا باید از «بافت‌های هم‌پوشان» سخن گفت؟",
        ]),
        "critique_text": "\n".join([
            "۱. جبر رسانه‌ای نرم: شکل رسانه تقریباً علت اصلی فرض می‌شود و تفسیر مخاطب، محتوا و بستر نهادی کم‌برجسته می‌شوند.",
            "۲. تمرکز بر تلویزیون: مدل برای دوران پخش طراحی شده و تعمیم آن به رسانه‌های تعاملی و شخصی‌سازی‌شده نیازمند بازنگری است.",
            "۳. شواهد تاریخی گزینشی: ادعاهای مربوط به فروپاشی نقش‌ها با شواهد تجربی نظام‌مند کمی پشتیبانی شده‌اند.",
            "۴. کم‌توجهی به محتوا: تأکید بر «شکل» می‌تواند تفاوت برنامه‌ها و ایدئولوژی‌های رسانه‌ای را نادیده بگیرد.",
            "۵. پیوند ناقص با گافمن: مفهوم موقعیت گافمن برای تعامل رودررو ساخته شد و انتقال آن به رسانه‌های جمعی نیازمند استدلال بیشتر است.",
        ]),
        "example_text": "نوجوانی که در شبکه اجتماعی هم با همکلاسی، هم با معلم و هم با اقوام بزرگ‌تر در یک حساب ارتباط دارد، مجبور است برای همه یک اجرای واحد داشته باشد. نتیجه، یا محافظه‌کاری شدید است یا افشای ناخواسته پشت‌صحنه. این وضعیت، همان «بی‌حسی مکان» است: مخاطب می‌داند کیست، اما نمی‌داند در کدام موقعیت نشسته است.",
    },
    "MC-411": {
        "summary": "(سیلورستون و هرش، ۱۹۹۲) اهلی‌سازی فناوری، فرایند چهارمرحله‌ای ادغام یک فناوری در زندگی روزمره است: تصاحب، عینیت‌بخشی، ادغام و تبدیل. فناوری در این فرایند از شیئی بیرونی به بخشی از روال خانه و هویت خانواده بدل می‌شود. نظریه بر «اقتصاد اخلاقی خانواده» تأکید دارد: ارزش‌ها، روابط جنسیتی و قدرت در انتخاب و استفاده از فناوری نقش تعیین‌کننده دارند.",
        "definition": "اهلی‌سازی، فرایند اجتماعی-فرهنگی تثبیت فناوری در زندگی روزمره است که در آن کاربران، فناوری را خریداری، جای‌گذاری، در روال‌ها ادغام و در نهایت به نشانه هویت خود تبدیل می‌کنند. این فرایند یک‌طرفه نیست؛ فناوری نیز خانواده را تغییر می‌دهد.",
        "main_problem": "مسئله این است که چرا فناوری‌های مشابه در خانه‌های مختلف سرنوشت متفاوتی می‌یابند: در جایی به ابزار روزمره بدل می‌شوند و در جایی رها می‌شوند. پاسخ نظریه، فراتر از ویژگی‌های فنی، به فرایند فرهنگی-خانوادگی پذیرش است.",
        "mechanism": "\n".join([
            "۱. تصاحب: تصمیم خرید و مالکیت؛ چه کسی فناوری را وارد خانه می‌کند و با چه توجیهی.",
            "۲. عینیت‌بخشی: جای‌گذاری مادی فناوری در خانه؛ مکان شیء، معنای اجتماعی و دسترسی را تعیین می‌کند.",
            "۳. ادغام: واردشدن فناوری به روال‌های زمانی و تعاملی خانواده؛ چه کاری با آن انجام می‌شود و چه کسی.",
            "۴. تبدیل: نمایش فناوری به بیرون؛ فناوری به نشانه هویت، پایگاه یا سلیقه خانواده بدل می‌شود.",
            "۵. اقتصاد اخلاقی خانواده: ارزش‌ها، تقسیم کار جنسیتی و اقتدار والدین، مسیر اهلی‌سازی را شکل می‌دهند.",
            "۶. دوگانه‌پیوندی: رسانه هم شیء مادی است و هم محتوا؛ اهلی‌سازی باید هر دو لایه را هم‌زمان تحلیل کند.",
            "در بستر رسانه، اهلی‌سازی در عصر گوشی هوشمند و استریم، منطق خود را حفظ کرده اما واحد تحلیل تغییر کرده است: خانه دیگر تنها مرز نیست و فرد نیز «خانوار» خود را دارد. اشتراک حساب، قواعد استفاده خانوادگی، مکان شارژ گوشی و انتخاب پلتفرم، همه نمونه‌های معاصر تصاحب و عینیت‌بخشی‌اند. پرسش تازه این است که وقتی زیرساخت محاسباتی به ابر منتقل می‌شود، آیا «خانه» هنوز محل اهلی‌سازی است یا پلتفرم، خود نقش خانه دوم را بازی می‌کند.",
        ]),
        "assumptions": [
            "پذیرش فناوری فرایندی فعال و فرهنگی است، نه صرفاً خرید.",
            "خانواده واحد معناداری برای تحلیل مصرف رسانه است.",
            "ارزش‌ها و روابط قدرت در خانه، مسیر اهلی‌سازی را تعیین می‌کنند.",
        ],
        "principles": [
            "اهلی‌سازی را در چهار مرحله و به‌صورت فرایندی تحلیل کنید.",
            "لایه مادی و لایه محتوایی رسانه را هم‌زمان ببینید.",
            "قواعد استفاده، بازتاب اقتصاد اخلاقی خانواده است.",
        ],
        "critiques": [
            "تمرکز بر خانوار: مدل برای رسانه خانگی طراحی شده و با فردی‌شدن رسانه‌ها، واحد تحلیل باید بازنگری شود.",
            "الگوی خانوادگی هنجاری: فرض خانواده هسته‌ای غربی، تعمیم را محدود می‌کند.",
            "کم‌توجهی به اقتصاد سیاسی: قدرت پلتفرم و مدل کسب‌وکار در فرایند اهلی‌سازی کم‌برجسته می‌شود.",
            "توصیفی‌بودن: نظریه فرایند را خوب توصیف می‌کند اما پیش‌بینی یا تبیین علّی قوی ارائه نمی‌دهد.",
            "نادیده‌گرفتن مقاومت: مصرف‌کنندگان می‌توانند فناوری را رد یا بازتعریف کنند و مدل این امکان را کم‌رنگ می‌بیند.",
        ],
        "applications": [
            "پژوهش درباره پذیرش رسانه‌های نو در خانه.",
            "طراحی محصول با توجه به روال‌های خانوادگی.",
            "تحلیل جنسیتی دسترسی و استفاده از فناوری.",
            "مطالعه اینترنت اشیا و خانه هوشمند.",
        ],
        "evolution": "مفهوم در پروژه «اطلاعات و ارتباطات در خانه» دهه ۱۹۸۰ شکل گرفت و در «مصرف فناوری‌ها» (۱۹۹۲) نظام‌مند شد. هادون و دیگران آن را به رسانه‌های سیار و فردی گستردند و در سال‌های اخیر به خانه هوشمند، پلتفرم‌ها و اینترنت اشیا تعمیم یافته است.",
        "key_concepts": [
            "اهلی‌سازی (domestication)",
            "تصاحب (appropriation)",
            "عینیت‌بخشی (objectification)",
            "ادغام (incorporation)",
            "تبدیل (conversion)",
            "اقتصاد اخلاقی خانواده (moral economy of the household)",
        ],
        "studies": [
            "Silverstone, R., & Hirsch, E. (Eds.). (1992). Consuming technologies: Media and information in domestic spaces. Routledge.",
            "Silverstone, R., Hirsch, E., & Morley, D. (1992). Information and communication technologies and the moral economy of the household. In R. Silverstone & E. Hirsch (Eds.), Consuming technologies (pp. 15-31). Routledge.",
        ],
        "theorists": "راجر سیلورستون و اریک هرش (Roger Silverstone & Eric Hirsch)",
        "model": "چهار مرحله اهلی‌سازی: تصاحب ← عینیت‌بخشی ← ادغام ← تبدیل؛ با میانجی‌گری اقتصاد اخلاقی خانواده و دوگانه‌پیوندی شیء/محتوا.",
        "detailed_analysis": "\n\n".join([
            "۱. بنیان و منطق نظری\nسیلورستون و همکارانش مصرف رسانه را فعالیتی تولیدی و معناساز دیدند، نه واکنشی. اهلی‌سازی، نقطه تلاقی مادیت فناوری و فرهنگ خانه است: فناوری وارد خانه می‌شود و خانه نیز فناوری را بازتعریف می‌کند. مفهوم «اقتصاد اخلاقی» نشان می‌دهد که این فرایند در بستری از ارزش‌ها و روابط قدرت رخ می‌دهد.",
            "۲. سازوکار عملی و تشخیصی\nبرای تحلیل اهلی‌سازی یک فناوری، چهار پرسش مطرح می‌شود: چگونه وارد خانه شد؟ کجا قرار گرفت؟ در کدام روال‌ها ادغام شد؟ و چگونه به بیرون نمایش داده می‌شود؟ پاسخ این پرسش‌ها، پذیرش را از «خرید» به «فرایند فرهنگی» ارتقا می‌دهد.",
            "۳. دلالت‌ها برای پژوهش رسانه\nپژوهش معاصر اهلی‌سازی را در رسانه‌های سیار، خانه هوشمند و پلتفرم‌های استریم به کار می‌برد. پرسش باز: وقتی زیرساخت به ابر منتقل می‌شود و حساب کاربری جای خانه را می‌گیرد، آیا مرزهای سنتی اهلی‌سازی هنوز معنا دارند؟",
        ]),
        "critique_text": "\n".join([
            "۱. تمرکز بر خانوار: مدل برای رسانه خانگی طراحی شده و با فردی‌شدن رسانه‌ها، واحد تحلیل باید بازنگری شود.",
            "۲. الگوی خانوادگی هنجاری: فرض خانواده هسته‌ای غربی، تعمیم را محدود می‌کند.",
            "۳. کم‌توجهی به اقتصاد سیاسی: قدرت پلتفرم و مدل کسب‌وکار در فرایند اهلی‌سازی کم‌برجسته می‌شود.",
            "۴. توصیفی‌بودن: نظریه فرایند را خوب توصیف می‌کند اما پیش‌بینی یا تبیین علّی قوی ارائه نمی‌دهد.",
            "۵. نادیده‌گرفتن مقاومت: مصرف‌کنندگان می‌توانند فناوری را رد یا بازتعریف کنند و مدل این امکان را کم‌رنگ می‌بیند.",
        ]),
        "example_text": "خانواده‌ای تلویزیون هوشمند می‌خرد (تصاحب)، آن را در پذیرایی می‌گذارد (عینیت‌بخشی)، تماشای مشترک شبانه را جایگزین گفت‌وگو می‌کند (ادغام) و در مهمانی از آن به‌عنوان نشانه مدرن‌بودن یاد می‌کند (تبدیل). در خانواده دیگری همان تلویزیون در اتاق کودک قرار می‌گیرد و به ابزار انفرادی بدل می‌شود. یک فناوری، دو مسیر اهلی‌سازی؛ تفاوت در اقتصاد اخلاقی و روابط قدرت خانه است.",
    },
    "MC-413": {
        "summary": "(ونکاتش و همکاران، ۲۰۰۳) نظریه یکپارچه پذیرش و کاربست فناوری، هشت مدل رقیب پذیرش فناوری را در یک چارچوب واحد ادغام می‌کند. بر پایه آن، قصد استفاده از چهار سازه اثر می‌گیرد: امید به عملکرد، امید به تلاش، نفوذ اجتماعی و شرایط تسهیل‌کننده. سن، جنسیت، تجربه و داوطلبانه‌بودن استفاده، این روابط را تعدیل می‌کنند. UTAUT در سال ۲۰۱۲ با افزودن انگیزه لذت‌جویانه، ارزش قیمتی و عادت (UTAUT2) گسترش یافت.",
        "definition": "UTAUT مدلی است که قصد رفتاری و رفتار استفاده از فناوری را از چهار سازه اصلی توضیح می‌دهد و با تعدیلگرهای جمعیت‌شناختی و تجربی، دقت پیش‌بینی را افزایش می‌دهد. این مدل بر پایه ترکیب نظریه کنش منطقی، رفتار برنامه‌ریزی‌شده، TAM، نوآوری‌پذیری و نظریه شناختی-اجتماعی ساخته شده است.",
        "main_problem": "مسئله این است که ادبیات پذیرش فناوری با مدل‌های متعدد و یافته‌های ناسازگار پراکنده شده و انتخاب مدل برای پژوهشگر و مدیر دشوار است. UTAUT کوشید با ترکیب سازه‌های مشترک، چارچوبی یکپارچه و آزمون‌پذیر بسازد.",
        "mechanism": "\n".join([
            "۱. امید به عملکرد: باور به اینکه فناوری به بهبود کار یا دستیابی به هدف کمک می‌کند؛ قوی‌ترین پیش‌بین قصد استفاده.",
            "۲. امید به تلاش: سهولت ادراک‌شده استفاده؛ اثر آن با تجربه و سن تعدیل می‌شود.",
            "۳. نفوذ اجتماعی: ادراک اینکه افراد مهم باور دارند فرد باید از فناوری استفاده کند؛ اثر آن با جنسیت، سن و داوطلبانه‌بودن تعدیل می‌شود.",
            "۴. شرایط تسهیل‌کننده: باور به وجود زیرساخت، پشتیبانی و منابع لازم؛ عمدتاً بر رفتار استفاده اثر می‌گذارد، نه فقط قصد.",
            "۵. قصد رفتاری: متغیر میانی میان باورها و رفتار؛ در مدل، رفتار استفاده از قصد و شرایط تسهیل‌کننده پیش‌بینی می‌شود.",
            "۶. تعدیلگرها: سن، جنسیت، تجربه و داوطلبانه‌بودن، شدت و جهت روابط را تغییر می‌دهند و همین، مدل را از یک الگوی ساده متمایز می‌کند.",
            "در بستر رسانه، UTAUT برای تحلیل پذیرش اپلیکیشن خبری، ابزارهای هوش مصنوعی و سرویس‌های اشتراکی به کار می‌رود: کاربری که معتقد است ابزار خلاصه‌سازی خبر در زمانش صرفه‌جویی می‌کند (امید به عملکرد)، رابط ساده‌ای می‌بیند (امید به تلاش) و همکارانش آن را پذیرفته‌اند (نفوذ اجتماعی)، احتمال بیشتری دارد آن را بپذیرد. اما مدل، انگیزه‌های لذت‌جویانه، هویت و اعتماد را کمتر می‌بیند؛ به همین دلیل، پژوهش رسانه معمولاً آن را با نظریه‌های استفاده و خشنودی یا مدل‌های اعتماد ترکیب می‌کند.",
        ]),
        "assumptions": [
            "پذیرش فناوری از باورهای ادراکی درباره عملکرد و تلاش نشئت می‌گیرد.",
            "قصد رفتاری، پیش‌بین نزدیک رفتار استفاده است.",
            "اثر سازه‌ها با ویژگی‌های فردی و بستر سازمانی تعدیل می‌شود.",
        ],
        "principles": [
            "برای پیش‌بینی پذیرش، هم باورهای فردی و هم شرایط سازمانی را بسنجید.",
            "اثر یکسان سازه‌ها را برای همه گروه‌ها فرض نکنید.",
            "قصد استفاده با استفاده واقعی یکی نیست و باید جدا سنجیده شود.",
        ],
        "critiques": [
            "تبیین ناقص واریانس: مدل بخشی از واریانس رفتار را توضیح می‌دهد و عوامل عاطفی، عادت و اعتماد را کم‌برجسته می‌کند.",
            "طراحی مقطعی: بیشتر آزمون‌ها مقطعی و مبتنی بر خودگزارشی‌اند و رابطه علّی را به‌طور کامل تأیید نمی‌کنند.",
            "بستر سازمانی: مدل در محیط‌های سازمانی و داوطلبانه توسعه یافته و تعمیم آن به مصرف‌کنندگان نیازمند UTAUT2 است.",
            "کم‌توجهی به معنا: تجربه لذت، هویت و معنای اجتماعی استفاده در سازه‌های اصلی حاضر نیست.",
            "خطای پذیرش/استفاده: پذیرش فناوری با استفاده معنادار و پایدار برابر نیست و مدل این تفاوت را کم‌رنگ می‌کند.",
        ],
        "applications": [
            "پیش‌بینی پذیرش ابزارهای دیجیتال در سازمان.",
            "طراحی مداخله برای افزایش استفاده از سرویس رسانه‌ای.",
            "پژوهش درباره شکاف دیجیتال و تفاوت گروه‌های سنی.",
            "ارزیابی سرویس‌های اشتراکی و اپلیکیشن‌های خبری.",
        ],
        "evolution": "UTAUT در ۲۰۰۳ با ترکیب هشت مدل معرفی شد و به یکی از پراستنادترین مدل‌های سیستم‌های اطلاعاتی بدل شد. در ۲۰۱۲، UTAUT2 با افزودن انگیزه لذت‌جویانه، ارزش قیمتی و عادت برای بستر مصرف‌کننده گسترش یافت. پژوهش‌های بعدی آن را با مدل‌های اعتماد، حریم خصوصی و هوش مصنوعی ترکیب کرده‌اند.",
        "key_concepts": [
            "امید به عملکرد (performance expectancy)",
            "امید به تلاش (effort expectancy)",
            "نفوذ اجتماعی (social influence)",
            "شرایط تسهیل‌کننده (facilitating conditions)",
            "قصد رفتاری (behavioral intention)",
            "تعدیلگر (moderator)",
        ],
        "studies": [
            "Venkatesh, V., Morris, M. G., Davis, G. B., & Davis, F. D. (2003). User acceptance of information technology: Toward a unified view. MIS Quarterly, 27(3), 425-478.",
            "Venkatesh, V., Thong, J. Y. L., & Xu, X. (2012). Consumer acceptance and use of information technology: Extending the unified theory of acceptance and use of technology. MIS Quarterly, 36(1), 157-178.",
        ],
        "theorists": "ویشواناتش ونکاتش، مایکل موریس، گوردون دیویس و فرد دیویس (Viswanath Venkatesh, Michael G. Morris, Gordon B. Davis & Fred D. Davis)",
        "model": "UTAUT: امید به عملکرد، امید به تلاش و نفوذ اجتماعی ← قصد رفتاری ← رفتار استفاده؛ با اثر مستقیم شرایط تسهیل‌کننده و تعدیل سن، جنسیت، تجربه و داوطلبانه‌بودن.",
        "detailed_analysis": "\n\n".join([
            "۱. بنیان و منطق نظری\nUTAUT حاصل مرور و آزمون تجربی هشت مدل پذیرش فناوری بود. ونکاتش و همکاران دریافتند که سازه‌های مشترک را می‌توان در چهار عامل ادغام کرد و اثر آن‌ها را با تعدیلگرهای جمعیت‌شناختی دقیق‌تر ساخت. نوآوری مدل، نه کشف سازه تازه، بلکه یکپارچه‌سازی و آزمون مقایسه‌ای بود.",
            "۲. سازوکار عملی و تشخیصی\nبرای ارزیابی پذیرش یک فناوری، چهار پرسش مطرح می‌شود: آیا کاربر سود عملکردی می‌بیند؟ آیا استفاده را آسان می‌داند؟ آیا افراد مهم او را به استفاده تشویق می‌کنند؟ و آیا زیرساخت و پشتیبانی لازم وجود دارد؟ این پرسش‌ها به پرسشنامه استاندارد و مداخله طراحی قابل تبدیل است.",
            "۳. دلالت‌ها برای پژوهش رسانه\nپژوهش معاصر UTAUT را با اعتماد، حریم خصوصی و هویت ترکیب می‌کند، زیرا پذیرش رسانه‌ای بیش از بهره‌وری، به لذت و معنا وابسته است. پرسش باز: در عصر هوش مصنوعی مولد، آیا سازه‌های UTAUT برای توضیح پذیرش ابزارهایی که خود محتوا تولید می‌کنند کافی‌اند؟",
        ]),
        "critique_text": "\n".join([
            "۱. تبیین ناقص واریانس: مدل بخشی از واریانس رفتار را توضیح می‌دهد و عوامل عاطفی، عادت و اعتماد را کم‌برجسته می‌کند.",
            "۲. طراحی مقطعی: بیشتر آزمون‌ها مقطعی و مبتنی بر خودگزارشی‌اند و رابطه علّی را به‌طور کامل تأیید نمی‌کنند.",
            "۳. بستر سازمانی: مدل در محیط‌های سازمانی و داوطلبانه توسعه یافته و تعمیم آن به مصرف‌کنندگان نیازمند UTAUT2 است.",
            "۴. کم‌توجهی به معنا: تجربه لذت، هویت و معنای اجتماعی استفاده در سازه‌های اصلی حاضر نیست.",
            "۵. خطای پذیرش/استفاده: پذیرش فناوری با استفاده معنادار و پایدار برابر نیست و مدل این تفاوت را کم‌رنگ می‌کند.",
        ]),
        "example_text": "دو خبرنگار در یک تحریریه، ابزار هوش مصنوعی برای خلاصه‌سازی را دریافت می‌کنند. یکی آن را می‌پذیرد چون معتقد است زمان صرفه‌جویی می‌کند و رابط ساده‌ای دارد؛ دیگری آن را رها می‌کند چون همکارانش به آن اعتماد ندارند و آموزش کافی ندیده است. UTAUT این تفاوت را با امید به عملکرد، نفوذ اجتماعی و شرایط تسهیل‌کننده توضیح می‌دهد؛ اما اگر ابزار برای کاربر «سرگرم‌کننده» یا «هویت‌ساز» باشد، مدل به تنهایی کافی نیست.",
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
                                       "verified": n_verified, "batch": 78}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH78 THEORY DONE")


if __name__ == "__main__":
    main()
