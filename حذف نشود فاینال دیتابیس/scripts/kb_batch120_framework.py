# -*- coding: utf-8 -*-
"""Batch 120 (FRAMEWORK): full documentation for MC-236, MC-357, MC-363, MC-419."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch120-framework-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch120_framework.json"

S = {
    "MC-236": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Critical Questions for Big Data: Provocations for a Cultural, Technological, and Scholarly Phenomenon",
             title_fa="پرسش‌های انتقادی دربارهٔ داده‌های بزرگ: تحریک‌هایی برای پدیده‌ای فرهنگی، فناورانه و پژوهشی",
             authors="boyd, d.; Crawford, K.", year=2012,
             publisher="Information, Communication & Society",
             doi="10.1080/1369118X.2012.678878",
             url="https://www.tandfonline.com/doi/full/10.1080/1369118X.2012.678878",
             language="en", isbn=None,
             citation="boyd, d., & Crawford, K. (2012). Critical questions for big data: Provocations for a cultural, technological, and scholarly phenomenon. Information, Communication & Society, 15(5), 662-679.",
             locator="15(5):662-679", locator_type="page_range",
             supports="six provocations on objectivity, sampling, context and ethics of big data", verified=True),
        dict(kind="BOOK",
             title_en="The Data Revolution: Big Data, Open Data, Data Infrastructures and Their Consequences",
             title_fa="انقلاب داده: داده‌های بزرگ، داده‌های باز، زیرساخت‌های داده و پیامدهای آن‌ها",
             authors="Kitchin, R.", year=2014,
             publisher="Sage",
             doi=None, url=None, language="en", isbn=None,
             citation="Kitchin, R. (2014). The data revolution: Big data, open data, data infrastructures and their consequences. Sage.",
             locator="chs. 1-3", locator_type="work",
             supports="data infrastructures and the epistemological limits of big data", verified=False),
    ],
    "MC-357": [
        dict(kind="BOOK",
             title_en="Audiences: A Sociological Theory of Performance and Imagination",
             title_fa="مخاطبان: نظریه‌ای جامعه‌شناختی دربارهٔ اجرا و تخیل",
             authors="Abercrombie, N.; Longhurst, B.", year=1998,
             publisher="Sage",
             doi=None,
             url="https://sk.sagepub.com/book/mono/audiences/toc",
             language="en", isbn=None,
             citation="Abercrombie, N., & Longhurst, B. (1998). Audiences: A sociological theory of performance and imagination. Sage.",
             locator="chs. 1-3", locator_type="work",
             supports="simple, mass and diffused audience phases organized around performance and imagination", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Theorising Media as Practice",
             title_fa="نظریه‌پردازی رسانه به‌مثابه عمل",
             authors="Couldry, N.", year=2004,
             publisher="Social Semiotics",
             doi=None, url=None, language="en", isbn=None,
             citation="Couldry, N. (2004). Theorising media as practice. Social Semiotics, 14(2), 115-132.",
             locator="14(2):115-132", locator_type="page_range",
             supports="practice-based reframing of audience activity beyond text consumption", verified=False),
    ],
    "MC-363": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Cascading Activation: Contesting the White House's Frame After 9/11",
             title_fa="فعال‌سازی آبشاری: رقابت با چارچوب کاخ سفید پس از ۱۱ سپتامبر",
             authors="Entman, R. M.", year=2003,
             publisher="Political Communication",
             doi="10.1080/10584600390244176",
             url="https://www.tandfonline.com/doi/abs/10.1080/10584600390244176",
             language="en", isbn=None,
             citation="Entman, R. M. (2003). Cascading activation: Contesting the White House's frame after 9/11. Political Communication, 20(4), 415-432.",
             locator="20(4):415-432", locator_type="page_range",
             supports="frames activate and spread downward through a stratified political-media system with limited feedback", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Framing: Toward Clarification of a Fractured Paradigm",
             title_fa="چارچوب‌بندی: به‌سوی روشن‌سازی یک پارادایم چندپاره",
             authors="Entman, R. M.", year=1993,
             publisher="Journal of Communication",
             doi=None, url=None, language="en", isbn=None,
             citation="Entman, R. M. (1993). Framing: Toward clarification of a fractured paradigm. Journal of Communication, 43(4), 51-58.",
             locator="43(4):51-58", locator_type="page_range",
             supports="selection and salience as the core operations of framing", verified=False),
    ],
    "MC-419": [
        dict(kind="BOOK",
             title_en="How We Became Posthuman: Virtual Bodies in Cybernetics, Literature, and Informatics",
             title_fa="چگونه پسانسان شدیم: بدن‌های مجازی در سایبرنتیک، ادبیات و انفورماتیک",
             authors="Hayles, N. K.", year=1999,
             publisher="University of Chicago Press",
             doi=None,
             url="https://press.uchicago.edu/ucp/books/book/chicago/H/bo3769963.html",
             language="en", isbn=None,
             citation="Hayles, N. K. (1999). How we became posthuman: Virtual bodies in cybernetics, literature, and informatics. University of Chicago Press.",
             locator="chs. 1-3", locator_type="work",
             supports="posthuman as distributed cognition and embodiment, against the liberal humanist subject", verified=True),
        dict(kind="BOOK_CHAPTER",
             title_en="A Cyborg Manifesto: Science, Technology, and Socialist-Feminism in the Late Twentieth Century",
             title_fa="مانیفست سایبورگ: علم، فناوری و فمینیسم سوسیالیستی در پایان سدهٔ بیستم",
             authors="Haraway, D.", year=1991,
             publisher="Routledge",
             doi=None, url=None, language="en", isbn=None,
             citation="Haraway, D. (1991). A cyborg manifesto: Science, technology, and socialist-feminism in the late twentieth century. In Simians, cyborgs, and women: The reinvention of nature (pp. 149-181). Routledge.",
             locator="pp. 149-181", locator_type="page_range",
             supports="hybrid boundary-blurring between organism and machine as a political figure", verified=False),
    ],
}

ENRICH = {
    "MC-236": dict(
        summary="پرسش‌های انتقادی دربارهٔ داده‌های بزرگ، چارچوبی است که دنا بوید و کیت کراورفورد در مقالهٔ سال ۲۰۱۲ برای آزمون ادعاهای مربوط به داده‌های بزرگ عرضه کردند. آن‌ها شش تحریک را مطرح ساختند: نخست آنکه داده‌های بزرگ تعریف دانش را تغییر می‌دهند و سنجه‌های تازه‌ای از اعتبار می‌سازند؛ دوم آنکه ادعاهای عینیت و دقت آن‌ها گمراه‌کننده است، زیرا داده خام وجود ندارد و هر مجموعه از پیش انتخاب، پاک‌سازی و چارچوب‌بندی شده است؛ سوم آنکه داده بیشتر همیشه داده بهتر نیست و نمونه‌های بزرگ می‌توانند سوگیری نظام‌مند را پنهان کنند؛ چهارم آنکه داده بیرون از بافت معنای خود را از دست می‌دهد و تفسیر آن بدون دانش زمینه‌ای نادرست می‌شود؛ پنجم آنکه دسترس‌پذیری داده به معنای اخلاقی‌بودن استفاده از آن نیست و رضایت، حریم خصوصی و آسیب‌های گروهی باید سنجیده شود؛ ششم آنکه دسترسی نابرابر به داده، شکاف‌های تازه‌ای میان پژوهشگران، نهادها و کشورها می‌سازد. این چارچوب تحلیل داده را از شمارش به پرسش دربارهٔ قدرت، بافت و پیامد پیوند می‌زند و به پژوهشگر یادآوری می‌کند که هر الگوی آماری ممکن است محصول همبستگی کاذب یا بازنمایی ناقص باشد. کاربرد آن در روش‌شناسی علوم اجتماعی محاسباتی، اخلاق داده، روزنامه‌نگاری داده و حکمرانی الگوریتمی گسترده است. نقد اصلی به این چارچوب آن است که بیشتر پرسش‌محور است تا راه‌حل‌محور و دستورالعمل عملی مشخصی برای سنجش کیفیت داده ارائه نمی‌دهد.",
        definition="پرسش‌های انتقادی دربارهٔ داده‌های بزرگ، مجموعه‌ای از آزمون‌های معرفت‌شناختی و اخلاقی است که ادعاهای عینیت، جامعیت و بی‌طرفی تحلیل داده‌های بزرگ را به چالش می‌کشد.",
        main_problem="چگونه می‌توان از دام اعتماد بی‌نقد به حجم داده گذشت و پرسید این داده چگونه ساخته شد، چه کسانی در آن بازنمایی شده‌اند، در چه بافتی معنا می‌یابد و استفاده از آن چه پیامد اخلاقی دارد.",
        mechanism="پژوهشگر ابتدا زنجیرهٔ ساخت داده را از ثبت تا پاک‌سازی ردیابی می‌کند، سپس سوگیری نمونه و شکاف بازنمایی را می‌سنجد، بافت گردآوری را بازمی‌یابد و سرانجام پیامدهای اخلاقی و سیاسی استفاده را ارزیابی می‌کند. هر مرحله می‌تواند ادعای اولیه را محدود کند.",
        assumptions=[
            "هیچ داده‌ای خام و بی‌واسطه نیست؛ هر داده ساخته و انتخاب شده است.",
            "بافت گردآوری، معنای داده را تعیین می‌کند.",
            "دسترس‌پذیری فنی، مجوز اخلاقی استفاده نیست.",
            "دسترسی به داده میان بازیگران نابرابر توزیع شده است.",
        ],
        principles=[
            "عینیت داده ادعایی است که باید اثبات شود، نه پیش‌فرض.",
            "حجم بیشتر، جایگزین کیفیت و بازنمایی نیست.",
            "همبستگی در داده‌های بزرگ می‌تواند کاذب و بی‌معنا باشد.",
            "اخلاق داده باید از مرحلهٔ طراحی پژوهش حاضر باشد، نه پس از انتشار.",
        ],
        critiques=[
            "چارچوب پرسش‌محور است و معیار عملی سنجش کیفیت ارائه نمی‌دهد.",
            "بر داده‌های اجتماعی متمرکز است و داده‌های حسی و زیستی را کم‌تر پوشش می‌دهد.",
            "به ساختار مالکیت داده و اقتصاد پلتفرم کم‌تر می‌پردازد.",
            "ممکن است به بدبینی روش‌شناختی و بی‌اعتمادی به همهٔ داده‌ها بینجامد.",
        ],
        applications=[
            "ارزیابی انتقادی پژوهش‌های علوم اجتماعی محاسباتی.",
            "طراحی پروتکل اخلاقی برای پژوهش داده‌های کاربران.",
            "روزنامه‌نگاری داده و راستی‌آزمایی ادعاهای آماری.",
            "سیاست‌گذاری شفافیت و دسترسی منصفانه به داده.",
        ],
        evolution="این چارچوب در بستر نقدهای سال ۲۰۱۰ بر وعده‌های داده‌های بزرگ شکل گرفت؛ پس از آن به ادبیات اخلاق داده، عدالت داده و حکمرانی الگوریتمی راه یافت و پرسش‌های آن در دوران هوش مصنوعی مولد بازخوانی شد.",
        key_concepts=[
            "داده خام به‌مثابه افسانه (Raw Data as Myth)",
            "سوگیری نمونه (Sampling Bias)",
            "همبستگی کاذب (Apophenia)",
            "اخلاق داده (Data Ethics)",
            "شکاف دسترسی به داده (Data Divide)",
        ],
        theorists="دنا بوید؛ کیت کراورفورد",
        theorists_text="بوید و کراورفورد (۲۰۱۲)؛ کیچین (۲۰۱۴)",
        model="ساخت داده → بازنمایی و سوگیری → بافت تفسیر → پیامد اخلاقی و سیاسی.",
        studies=[
            "بوید و کراورفورد (۲۰۱۲) شش تحریک انتقادی دربارهٔ معرفت‌شناسی و اخلاق داده‌های بزرگ عرضه کردند.",
            "کیچین (۲۰۱۴) زیرساخت‌های داده و محدودیت‌های معرفتی آن‌ها را در چارچوبی گسترده‌تر تحلیل کرد.",
        ],
        detailed_analysis="تحلیل عمیق نشان می‌دهد پرسش‌های این چارچوب بیش از آنکه دربارهٔ فناوری باشند، دربارهٔ قدرت‌اند: چه کسی داده را تولید می‌کند، چه کسی به آن دسترسی دارد و چه کسی حق تفسیر آن را دارد. در پژوهش رسانه، همین پرسش‌ها به تحلیل داده‌های پلتفرم و سنجه‌های توجه منتقل می‌شود. پذیرش انتقادی این چارچوب به معنای رد داده‌های بزرگ نیست، بلکه به معنای همراه‌کردن هر تحلیل با مستندسازی فرایند ساخت، حدود بازنمایی و ارزیابی پیامد است.",
        critique_text="نقد اصلی آن است که چارچوب بیشتر پرسش‌محور است تا راه‌حل‌محور و معیار عملی مشخصی برای سنجش کیفیت داده و اصلاح سوگیری پیشنهاد نمی‌کند.",
        example_text="تحلیل داده‌های یک پلتفرم اجتماعی که فقط کاربران فعال را ثبت می‌کند، می‌تواند سکوت گروه‌های کم‌فعالیت را به غیبت کامل آن‌ها در نتایج تبدیل کند؛ پرسش دربارهٔ زنجیرهٔ ساخت داده، این خطا را آشکار می‌سازد.",
        year=2012,
    ),
    "MC-357": dict(
        summary="چارچوب سه دورهٔ مخاطب‌شناسی، تحول تاریخی رابطهٔ مخاطب با رسانه را در سه مرحله توضیح می‌دهد. نیکلاس آبرکرومبی و برایان لانگ‌هرست در کتاب سال ۱۹۹۸ خود میان مخاطب ساده، مخاطب توده‌ای و مخاطب پراکنده تمایز گذاشتند. مخاطب ساده در موقعیت حضوری و متمرکز شکل می‌گیرد؛ مانند تماشاگران یک نمایش یا شنوندگان یک سخنرانی که در زمان و مکان مشترک حضور دارند و اجرای جمعی را تجربه می‌کنند. مخاطب توده‌ای محصول رسانه‌های پخش گسترده است: جمعیتی بزرگ، پراکنده و ناشناس که هم‌زمان یک پیام را دریافت می‌کنند بی‌آنکه با یکدیگر تعامل داشته باشند. مخاطب پراکنده مرحلهٔ معاصر است: در آن، مرز میان تولید و مصرف فرو می‌ریزد، هر فرد هم تماشاگر است و هم اجراکننده، و رسانه در همهٔ ابعاد زندگی روزمره حضور دارد. دو مفهوم کلیدی این چارچوب، اجرا و تخیل است: مخاطب بودن کنشی اجرایی است که هویت را در برابر دیگران نمایش می‌دهد و تخیل، حضور دیگران و رسانه‌ها را در ذهن مخاطب ممکن می‌سازد. در محیط پلتفرمی، این چارچوب به‌خوبی توضیح می‌دهد چرا کاربران هم‌زمان مصرف‌کننده، تولیدکننده و نمایش‌دهندهٔ خود هستند و چرا مرز میان زندگی خصوصی و اجرای عمومی مخدوش شده است. کاربرد آن در تحلیل مخاطب شبکه‌های اجتماعی، مطالعهٔ خودنمایی و شهرت، و بازتعریف سیاست مخاطب در سازمان‌های رسانه‌ای است. نقد اصلی به آن، غلبهٔ زبان نمایش و اجرا بر تحلیل ساختار قدرت و اقتصاد رسانه است.",
        definition="سه دورهٔ مخاطب‌شناسی، چارچوبی تحلیلی است که تحول مخاطب را از اجتماع حضوری و متمرکز به تودهٔ پراکنده و سپس به مخاطب پراکندهٔ اجراکننده در محیط رسانه‌ای‌شده توضیح می‌دهد.",
        main_problem="چگونه می‌توان تفاوت کیفی مخاطب امروز را با مخاطب توده‌ای دوران پخش گسترده توضیح داد، وقتی مرز میان تولید و مصرف، و میان زندگی روزمره و اجرا فرو ریخته است.",
        mechanism="با گسترش رسانه‌ها، تجربهٔ مشترک حضوری جای خود را به دریافت هم‌زمان و پراکنده می‌دهد؛ سپس نفوذ رسانه در زندگی روزمره، هر فرد را به مخاطبی تبدیل می‌کند که خود اجرا می‌کند و تخیل مخاطب بودن دیگران، هویت او را شکل می‌دهد.",
        assumptions=[
            "مخاطب پدیده‌ای تاریخی است و در هر دوره شکل متفاوتی دارد.",
            "اجرا و تخیل دو سازوکار اصلی شکل‌گیری تجربهٔ مخاطب‌بودن‌اند.",
            "رسانه‌ای‌شدن زندگی روزمره، مرز تولید و مصرف را مخدوش می‌کند.",
            "مخاطب بودن کنشی فعال و هویت‌ساز است، نه دریافت منفعل.",
        ],
        principles=[
            "هر دورهٔ مخاطب، شکل نهادی و فناورانهٔ خاص خود را دارد.",
            "مخاطب ساده حضوری، توده‌ای پراکنده و مخاطب پراکنده اجراکننده است.",
            "اجرا همیشه در برابر مخاطب خیالی یا واقعی رخ می‌دهد.",
            "رسانه‌ای‌شدن زندگی، مخاطب را به بخشی از محیط تبدیل می‌کند.",
        ],
        critiques=[
            "زبان نمایش و اجرا، تحلیل ساختار قدرت و مالکیت رسانه را کم‌رنگ می‌کند.",
            "مرز سه دوره در تجربهٔ واقعی مخاطبان اغلب درهم‌آمیخته است.",
            "چارچوب به تنوع فرهنگی و نابرابری دسترسی کم‌تر می‌پردازد.",
            "مفهوم مخاطب پراکنده چنان گسترده است که مرز تحلیلی خود را از دست می‌دهد.",
        ],
        applications=[
            "تحلیل رفتار کاربران در شبکه‌های اجتماعی و فرهنگ شهرت.",
            "بازتعریف راهبرد مخاطب در سازمان‌های خبری و سرگرمی.",
            "مطالعهٔ خودنمایی، هواداری و هویت اجرایی در محیط دیجیتال.",
            "آموزش تحلیل مخاطب با تمرکز بر اجرا و تخیل.",
        ],
        evolution="مطالعات مخاطب از مخاطب توده‌ای دوران پخش به رویکرد دریافت و سپس به مخاطب فعال حرکت کرد؛ آبرکرومبی و لانگ‌هرست (۱۹۹۸) با افزودن مفهوم مخاطب پراکنده و دو سازوکار اجرا و تخیل، این تحول را در چارچوبی جامعه‌شناختی سازمان دادند.",
        key_concepts=[
            "مخاطب ساده (Simple Audience)",
            "مخاطب توده‌ای (Mass Audience)",
            "مخاطب پراکنده (Diffused Audience)",
            "اجرا (Performance)",
            "تخیل رسانه‌ای (Media Imagination)",
        ],
        theorists="نیکلاس آبرکرومبی؛ برایان لانگ‌هرست",
        theorists_text="آبرکرومبی و لانگ‌هرست (۱۹۹۸)",
        model="مخاطب سادهٔ حضوری → مخاطب توده‌ای پراکنده → مخاطب پراکندهٔ اجراکننده در زندگی رسانه‌ای‌شده.",
        studies=[
            "آبرکرومبی و لانگ‌هرست (۱۹۹۸) سه دورهٔ مخاطب را با مفاهیم اجرا و تخیل صورت‌بندی کردند.",
            "کودری (۲۰۰۴) تحلیل مخاطب را به‌سوی رسانه به‌مثابه عمل و رویهٔ روزمره بازفرموله کرد.",
        ],
        detailed_analysis="تحلیل عمیق نشان می‌دهد گذار میان سه دوره، جایگزینی کامل نیست: مخاطب ساده و توده‌ای هم‌زمان با مخاطب پراکنده وجود دارند. در یک کنسرت، تماشاگر حاضر هم مخاطب ساده است، هم در شبکه‌های اجتماعی اجرا می‌کند و هم مخاطب پیام‌های پخش‌شده است. ارزش تحلیلی چارچوب در آن است که مخاطب را نه یک جمعیت آماری، بلکه موقعیتی اجتماعی و اجرایی می‌بیند. این نگاه، سیاست مخاطب را از شمارش بیننده به فهم رابطهٔ هویتی و روزمره تغییر می‌دهد.",
        critique_text="نقد اصلی آن است که زبان نمایش و اجرا، تحلیل ساختار قدرت، مالکیت و اقتصاد رسانه را کم‌رنگ می‌کند و مرز سه دوره در تجربهٔ واقعی مخاطبان اغلب درهم‌آمیخته است.",
        example_text="یک هوادار فوتبال در ورزشگاه مخاطب ساده است، در خانه مخاطب توده‌ای پخش تلویزیونی و در شبکهٔ اجتماعی با انتشار ویدئو و نظر، مخاطب پراکندهٔ اجراکننده؛ هر سه موقعیت در یک روز تجربه می‌شوند.",
        year=1998,
    ),
    "MC-363": dict(
        summary="فعال‌سازی آبشاری چارچوب‌ها، مدلی است که رابرت انتمن در مقالهٔ سال ۲۰۰۳ برای توضیح جریان چارچوب‌های تفسیری در نظام سیاسی و رسانه‌ای آمریکا عرضه کرد. در این مدل، چارچوب‌ها از سطح بالا به پایین جاری می‌شوند: نخست دولت و کاخ سفید، سپس نخبگان غیردولتی مانند کنگره و مقام‌های پیشین، آنگاه شبکه‌های خبری، سپس متن خبری و سرانجام ادراک عمومی. هر سطح، چارچوب بالادست را به شکلی بازتولید یا بازتفسیر می‌کند و امکان بازخورد از پایین به بالا وجود دارد، اما این بازخورد ضعیف و مشروط است. انتمن با تحلیل پوشش خبری پس از ۱۱ سپتامبر نشان داد چگونه چارچوب دولت بوش در رسانه‌ها گسترش یافت و رقابت چارچوب‌های بدیل تا حد زیادی ناموفق ماند. سه عامل تعیین می‌کند چارچوبی در آبشار موفق شود: انسجام و تکرار در سطح بالا، هم‌خوانی با فرهنگ سیاسی مسلط و قدرت نهادی حامل آن. مدل همچنین نشان می‌دهد که رسانه نه آینهٔ بی‌طرف رویداد، بلکه ایستگاهی فعال در بازتولید یا تعدیل چارچوب نخبگان است. کاربرد آن در تحلیل پوشش سیاست خارجی، مدیریت بحران، ارتباطات دولتی و مطالعهٔ رقابت روایت‌ها در انتخابات است. نقد اصلی به این مدل، ساده‌سازی نظام چندلایه، فرضِ ضعف بیش‌ازحد بازخورد عمومی و کم‌توجهی به محیط پلتفرمی است که در آن جریان چارچوب دیگر تنها عمودی نیست.",
        definition="فعال‌سازی آبشاری، فرایند انتشار چارچوب‌های تفسیری از دولت و نخبگان به رسانه‌ها و سپس به عموم است که در آن هر سطح، چارچوب را بازتولید یا تعدیل می‌کند.",
        main_problem="چگونه یک چارچوب تفسیری از بالاترین سطح قدرت سیاسی به متن خبری و ادراک عمومی می‌رسد، چرا برخی چارچوب‌های بدیل در این مسیر شکست می‌خورند و بازخورد عمومی چه اندازه بر آن اثر دارد.",
        mechanism="نخبگان دولتی با تکرار و انسجام، چارچوب خود را به شبکه‌های خبری منتقل می‌کنند؛ روزنامه‌نگاران آن را با ارزش‌های خبری و منابع خود بازسازی می‌کنند؛ متن خبری چارچوب را به مخاطب می‌رساند. هم‌خوانی فرهنگی و قدرت نهادی، احتمال پذیرش چارچوب را افزایش می‌دهد.",
        assumptions=[
            "نظام سیاسی و رسانه‌ای لایه‌بندی شده و نابرابر است.",
            "چارچوب‌ها از سطوح بالا به پایین با سهولت بیشتری جریان می‌یابند.",
            "بازخورد از پایین به بالا ممکن اما ضعیف و مشروط است.",
            "هم‌خوانی با فرهنگ مسلط، شانس چارچوب را افزایش می‌دهد.",
        ],
        principles=[
            "قدرت چارچوب‌سازی با موقعیت نهادی گره خورده است.",
            "تکرار و انسجام پیام، شرط نفوذ چارچوب در آبشار است.",
            "رسانه ایستگاه فعال تفسیر است، نه مجرای خنثی.",
            "چارچوب بدیل برای رقابت موفق به منابع نهادی و هم‌خوانی فرهنگی نیاز دارد.",
        ],
        critiques=[
            "مدل نظام رسانه‌ای را بیش از حد ساده و لایه‌بندی را ثابت فرض می‌کند.",
            "نقش بازخورد عمومی و رسانه‌های اجتماعی را کم‌برآورد می‌کند.",
            "به تنوع نظام‌های رسانه‌ای خارج از آمریکا کم‌تر می‌پردازد.",
            "مرز میان سطوح در محیط همگرا و پلتفرمی مبهم شده است.",
        ],
        applications=[
            "تحلیل پوشش خبری سیاست خارجی و امنیتی.",
            "مدیریت ارتباطات بحران و رقابت روایت‌های دولتی.",
            "مطالعهٔ چارچوب‌بندی انتخابات و رقابت نخبگان.",
            "آموزش روزنامه‌نگاری برای شناخت فشار چارچوب‌های بالادست.",
        ],
        evolution="انتمن (۱۹۹۳) سازوکار گزینش و برجسته‌سازی را در نظریهٔ چارچوب‌بندی تدوین کرد؛ مدل آبشاری (۲۰۰۳) با مطالعهٔ پوشش پس از ۱۱ سپتامبر، جریان لایه‌ای چارچوب‌ها و محدودیت بازخورد را افزود و پژوهش‌های بعدی آن را در محیط دیجیتال آزمودند.",
        key_concepts=[
            "چارچوب تفسیری (Interpretive Frame)",
            "آبشار چارچوب (Frame Cascade)",
            "نخبگان غیردولتی (Non-Administration Elites)",
            "هم‌خوانی فرهنگی (Cultural Congruence)",
            "بازخورد پایین به بالا (Bottom-Up Feedback)",
        ],
        theorists="رابرت انتمن",
        theorists_text="انتمن (۲۰۰۳)؛ انتمن (۱۹۹۳)",
        model="دولت → نخبگان غیردولتی → شبکه‌های خبری → متن خبری → ادراک عمومی، با بازخورد ضعیف از پایین.",
        studies=[
            "انتمن (۲۰۰۳) جریان چارچوب کاخ سفید پس از ۱۱ سپتامبر را در رسانه‌ها ردیابی کرد.",
            "انتمن (۱۹۹۳) گزینش و برجسته‌سازی را به‌عنوان سازوکار مرکزی چارچوب‌بندی تعریف کرد.",
        ],
        detailed_analysis="تحلیل عمیق نشان می‌دهد قدرت آبشار نه از حقیقت چارچوب، بلکه از موقعیت نهادی حامل آن می‌آید. چارچوبی که در سطح دولت با انسجام تکرار می‌شود، برای رسانه ارزان‌تر و معتبرتر از چارچوبی است که باید از منابع پراکنده ساخته شود. در محیط پلتفرمی، این عدم تقارن تضعیف شده اما حذف نشده است: نخبگان همچنان دسترسی ساختاری دارند، ولی روایت‌های بدیل می‌توانند سریع‌تر و بی‌واسطه‌تر منتشر شوند. از این رو مدل آبشاری امروز باید با تحلیل شبکه و رقابت روایت ترکیب شود.",
        critique_text="نقد اصلی آن است که مدل، نظام رسانه‌ای را بیش از حد ساده و لایه‌بندی را ثابت فرض می‌کند و نقش بازخورد عمومی و رسانه‌های اجتماعی را کم‌برآورد می‌سازد.",
        example_text="در بحران یک حادثهٔ امنیتی، نخست دولت روایت رسمی را با تکرار روزانه تثبیت می‌کند، شبکه‌های خبری همان چارچوب را با منابع نهادی بازتولید می‌کنند و روایت‌های بدیل تنها وقتی نفوذ می‌کنند که شاهد مستقل یا شکاف در انسجام رسمی پدید آید.",
        year=2003,
    ),
    "MC-419": dict(
        summary="پسانسان‌گرایی در عصر رسانه، چارچوبی است که سوژهٔ انسانی لیبرال را در برابر درهم‌آمیختگی بدن با سیستم‌های اطلاعاتی و سایبرنتیک به چالش می‌کشد. کاترین هیلز در کتاب سال ۱۹۹۹ خود نشان داد چگونه در سایبرنتیک، اطلاعات از بدن جدا تصور شد و این جدایی، تصویری از انسان ساخت که می‌تواند در ماشین بارگذاری شود. او در برابر این تصویر، پسانسان را نه حذف بدن، بلکه توزیع شناخت میان بدن، محیط و فناوری تعریف کرد: آگاهی در شبکه‌ای از بازخوردها، رابط‌ها و ابزارها شکل می‌گیرد و مرز میان انسان و ماشین قابل تعیین یک‌باره نیست. در این نگاه، رسانه‌ها فقط حامل پیام نیستند، بلکه بخشی از زیرساخت ادراک و کنش‌اند: تلفن همراه، رابط لمسی، واقعیت مجازی و سامانه‌های هوشمند، بدن را به گره‌ای در شبکه تبدیل می‌کنند. هیلز با مرور سه موج سایبرنتیک نشان داد چگونه مفهوم اطلاعات از بافت مادی جدا شد و سپس نقد بدن‌مندی این جدایی را به مرکز آورد. چارچوب پسانسان‌گرا پرسش‌های تازه‌ای دربارهٔ مسئولیت، عاملیت، حریم بدن و مالکیت داده مطرح می‌کند: اگر شناخت توزیع‌شده است، مسئولیت کنش را به چه کسی نسبت دهیم. کاربرد آن در مطالعات واقعیت مجازی، هوش مصنوعی، رابط‌های مغز و ماشین و نقد انسان‌محوری در طراحی فناوری است. نقد اصلی به این چارچوب، ابهام تجربی، خطر کم‌رنگ‌کردن نابرابری‌های مادی و دشواری ترجمهٔ آن به سیاست عملی است.",
        definition="پسانسان‌گرایی چارچوبی است که انسان را نه سوژه‌ای مستقل و خودبسنده، بلکه موجودی توزیع‌شده در شبکهٔ بدن، فناوری، اطلاعات و محیط می‌داند و مرز انسان و ماشین را قابل بازتعریف می‌شمارد.",
        main_problem="اگر شناخت و کنش انسان میان بدن، فناوری و شبکه‌های اطلاعاتی توزیع شده باشد، چه معنایی برای عاملیت، مسئولیت اخلاقی و هویت انسانی در عصر رسانه‌های هوشمند باقی می‌ماند.",
        mechanism="رابط‌های فناورانه با ایجاد حلقه‌های بازخورد میان بدن و سامانه، ادراک و کنش را بازآرایی می‌کنند؛ اطلاعات از بافت مادی جدا و سپس در قالب‌های تازه بازجای‌گذاری می‌شود و سوژه در همین چرخه شکل می‌گیرد.",
        assumptions=[
            "مرز میان انسان و ماشین ثابت و طبیعی نیست.",
            "شناخت در شبکهٔ بدن و محیط و فناوری توزیع شده است.",
            "اطلاعات بدون بافت مادی، معنای کامل خود را از دست می‌دهد.",
            "فناوری رسانه‌ای بخشی از زیرساخت ادراک است، نه ابزار بیرونی.",
        ],
        principles=[
            "پسانسان بودن به معنای حذف بدن نیست، بلکه بازتعریف جایگاه آن است.",
            "بدن و ماده، شرط تحقق اطلاعات و شناخت‌اند.",
            "عاملیت انسانی در شبکه‌های بازخوردی توزیع می‌شود.",
            "طراحی فناوری، طراحی شکل‌های تازهٔ سوژه‌بودن است.",
        ],
        critiques=[
            "مفاهیم چارچوب انتزاعی‌اند و سنجش تجربی آن‌ها دشوار است.",
            "خطر کم‌رنگ‌کردن نابرابری‌های مادی و دسترسی نابرابر به فناوری.",
            "پرسش مسئولیت اخلاقی در کنش توزیع‌شده پاسخ روشنی نمی‌گیرد.",
            "مرز میان نقد فلسفی و تحلیل رسانه‌ای گاهی مبهم می‌شود.",
        ],
        applications=[
            "تحلیل تجربهٔ بدن در واقعیت مجازی و واقعیت افزوده.",
            "نقد انسان‌محوری در طراحی هوش مصنوعی و رابط‌های هوشمند.",
            "مطالعهٔ حریم بدن و مالکیت داده‌های زیستی.",
            "آموزش سواد فناورانه با تمرکز بر رابطهٔ انسان و ماشین.",
        ],
        evolution="هیلز (۱۹۹۹) با مرور سه موج سایبرنتیک، پسانسان را به‌عنوان شناخت توزیع‌شده و بدن‌مند صورت‌بندی کرد؛ پیش از او هاراوی (۱۹۹۱) با تصویر سایبورگ مرز ارگانیسم و ماشین را سیاسی کرد و پژوهش‌های بعدی این چارچوب را به رسانه‌های هوشمند و زیست‌فناوری گستردند.",
        key_concepts=[
            "شناخت توزیع‌شده (Distributed Cognition)",
            "بدن‌مندی (Embodiment)",
            "حلقهٔ بازخورد (Feedback Loop)",
            "سایبورگ (Cyborg)",
            "سوژهٔ لیبرال (Liberal Subject)",
        ],
        theorists="کاترین هیلز؛ دانا هاراوی",
        theorists_text="هیلز (۱۹۹۹)؛ هاراوی (۱۹۹۱)",
        model="بدن → رابط فناورانه → حلقهٔ بازخورد → شناخت توزیع‌شده → بازتعریف سوژه و مسئولیت.",
        studies=[
            "هیلز (۱۹۹۹) سه موج سایبرنتیک و جدایی اطلاعات از بدن را تحلیل کرد.",
            "هاراوی (۱۹۹۱) سایبورگ را به‌عنوان چهرهٔ سیاسی مرزشکنی انسان و ماشین عرضه کرد.",
        ],
        detailed_analysis="تحلیل عمیق نشان می‌دهد پرسش پسانسان‌گرا در رسانه امروز عملی شده است: کاربری که با عینک هوشمند، ساعت پایش سلامت و دستیار صوتی زندگی می‌کند، مرزهای بدن و اطلاعات را هر روز جابه‌جا می‌کند. مسئلهٔ کلیدی، نه پایان انسان بلکه بازتوزیع عاملیت است: بخشی از حافظه، تصمیم و ادراک به سامانه‌ها سپرده می‌شود و پرسش مسئولیت پیچیده می‌گردد. از این رو چارچوب پسانسان مکمل اخلاق داده و مطالعات زیرساخت است و بدون آن، تحلیل اثر رسانه‌های هوشمند ناقص می‌ماند.",
        critique_text="نقد اصلی آن است که مفاهیم چارچوب انتزاعی و دشوارسنجش‌اند، خطر کم‌رنگ‌کردن نابرابری‌های مادی را دارند و پرسش مسئولیت اخلاقی در کنش توزیع‌شده را بی‌پاسخ می‌گذارند.",
        example_text="بازیکنی که با هدست واقعیت مجازی بازی می‌کند، حرکت بدن، تصویر مصنوعی و بازخورد لمسی را در یک حلقه تجربه می‌کند؛ مرز میان بدن او و سامانه در این تجربه به‌طور عملی مبهم می‌شود.",
        year=1999,
    ),
}

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


REQUIRED_SECTIONS = ["summary", "definition", "main_problem", "mechanism", "assumptions",
                     "principles", "critiques", "applications", "evolution", "key_concepts",
                     "theorists", "model", "studies"]
WORD_KEYS = ["summary", "definition", "main_problem", "mechanism", "critiques",
             "applications", "evolution", "key_concepts", "principles", "studies", "assumptions"]


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
    "MC-363": "year corrected 2004 -> 2003 (Entman, Cascading Activation, Political Communication 20(4), 2003)",
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
                                       "verified": n_verified, "batch": 120}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH120 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
