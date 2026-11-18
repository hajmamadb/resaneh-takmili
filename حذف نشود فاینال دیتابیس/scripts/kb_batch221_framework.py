# -*- coding: utf-8 -*-
"""Batch 221: repair template analyses of MC-641 (post-democracy) and MC-643 (competitive authoritarianism)."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch221-20261117"
NOW = "2026-11-17 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch221.json"

S = {
    "MC-641": [
        dict(kind="BOOK", title_en="Post-Democracy",
             title_fa="پس‌دموکراسی",
             authors="Colin Crouch", year=2004, publisher="Polity Press",
             doi=None, url="https://www.wiley.com/Post-Democracy-p-9780745633145",
             language="en", isbn="9780745633145",
             citation="Crouch, C. (2004). Post-Democracy. Cambridge: Polity Press.",
             locator="book", locator_type="BOOK",
             supports="post-democracy as persistence of formal institutions alongside elite control of substantive decisions", verified=True),
        dict(kind="BOOK", title_en="Post-Democracy After the Crises",
             title_fa="پس‌دموکراسی پس از بحران‌ها",
             authors="Colin Crouch", year=2020, publisher="Polity Press",
             doi=None, url="https://www.politybooks.com/bookdetail?book_slug=post-democracy-after-the-crises--9781509541560",
             language="en", isbn="9781509541560",
             citation="Crouch, C. (2020). Post-Democracy After the Crises. Cambridge: Polity Press.",
             locator="book", locator_type="BOOK",
             supports="update of the post-democracy thesis under financial crisis, inequality and populism", verified=True),
        dict(kind="JOURNAL_ARTICLE", title_en="The Third Age of Political Communication: Influences and Features",
             title_fa="عصر سوم ارتباطات سیاسی: تأثیرها و ویژگی‌ها",
             authors="Jay G. Blumler; Dennis Kavanagh", year=1999, publisher="Political Communication",
             doi="10.1080/105846099198596",
             url="https://www.tandfonline.com/doi/abs/10.1080/105846099198596",
             language="en", isbn=None,
             citation="Blumler, J. G., & Kavanagh, D. (1999). The third age of political communication: Influences and features. Political Communication, 16(3), 209-230.",
             locator="16(3), 209-230", locator_type="PAGE",
             supports="media abundance, professionalisation and audience fragmentation in political communication", verified=True),
        dict(kind="BOOK", title_en="Media Democracy: How the Media Colonize Politics",
             title_fa="دموکراسی رسانه‌ای: چگونه رسانه سیاست را مستعمره می‌کند",
             authors="Thomas Meyer; Lew Hinchman", year=2002, publisher="Polity Press",
             doi=None, url="https://www.politybooks.com/bookdetail?book_slug=media-democracy-how-the-media-colonize-politics--9780745628448",
             language="en", isbn="9780745628448",
             citation="Meyer, T., & Hinchman, L. (2002). Media Democracy: How the Media Colonize Politics. Cambridge: Polity Press.",
             locator="book", locator_type="BOOK",
             supports="media logic displacing party logic and colonising political communication", verified=True),
    ],
    "MC-643": [
        dict(kind="JOURNAL_ARTICLE", title_en="Elections Without Democracy: The Rise of Competitive Authoritarianism",
             title_fa="انتخابات بدون دموکراسی: ظهور اقتدارگرایی رقابتی",
             authors="Steven Levitsky; Lucan A. Way", year=2002, publisher="Journal of Democracy",
             doi="10.1353/jod.2002.0026",
             url="https://muse.jhu.edu/article/17196",
             language="en", isbn=None,
             citation="Levitsky, S., & Way, L. A. (2002). Elections without democracy: The rise of competitive authoritarianism. Journal of Democracy, 13(2), 51-65.",
             locator="13(2), 51-65", locator_type="PAGE",
             supports="hybrid regimes where elections are real but the playing field is systematically uneven", verified=True),
        dict(kind="BOOK", title_en="Competitive Authoritarianism: Hybrid Regimes after the Cold War",
             title_fa="اقتدارگرایی رقابتی: رژیم‌های ترکیبی پس از جنگ سرد",
             authors="Steven Levitsky; Lucan A. Way", year=2010, publisher="Cambridge University Press",
             doi="10.1017/CBO9780511781353",
             url="https://www.cambridge.org/core/books/competitive-authoritarianism/20A51BE2EBAB59B8AAEFD91B8FA3C9D6",
             language="en", isbn="9780521709156",
             citation="Levitsky, S., & Way, L. A. (2010). Competitive Authoritarianism: Hybrid Regimes after the Cold War. Cambridge: Cambridge University Press.",
             locator="ch. 1-2", locator_type="CHAPTER",
             supports="four arenas of contestation (electoral, legislative, judicial, media) in 35 post-Cold War cases", verified=True),
        dict(kind="BOOK", title_en="Pluralism by Default: Weak Autocrats and the Rise of Competitive Politics",
             title_fa="کثرت‌گرایی پیش‌فرض: خودکامگان ضعیف و ظهور سیاست رقابتی",
             authors="Lucan A. Way", year=2015, publisher="Johns Hopkins University Press",
             doi=None, url="https://www.press.jhu.edu/books/title/11302/pluralism-default",
             language="en", isbn="9781421418124",
             citation="Way, L. A. (2015). Pluralism by Default: Weak Autocrats and the Rise of Competitive Politics. Baltimore: Johns Hopkins University Press.",
             locator="book", locator_type="BOOK",
             supports="pluralism resulting from weak state capacity rather than deliberate institutional design", verified=True),
        dict(kind="JOURNAL_ARTICLE", title_en="Review of Pluralism by Default",
             title_fa="مروری بر «کثرت‌گرایی پیش‌فرض»",
             authors="Henry E. Hale", year=2017, publisher="Perspectives on Politics",
             doi=None,
             url="https://www.cambridge.org/core/journals/perspectives-on-politics/article/pluralism-by-default-weak-autocrats-and-the-rise-of-competitive-politics-by-lucan-way-baltimore-johns-hopkins-university-press-2015-274p-4495/708A632DA50D72DACF0705F7A6E9BBBC",
             language="en", isbn=None,
             citation="Hale, H. E. (2017). Review of Pluralism by Default, by Lucan Way. Perspectives on Politics, 15(2).",
             locator="15(2)", locator_type="PAGE",
             supports="critical assessment of the weakness-based explanation of competitive politics", verified=True),
    ],
}

ENRICH = {
    "MC-641": dict(
        needs_enrichment=False,
        level="میان",
        related_approaches="جامعه‌شناسی سیاسی؛ اقتصاد سیاسی رسانه؛ ارتباطات سیاسی؛ نظریهٔ دموکراسی؛ مطالعات حکمرانی.",
        recommended_sources="«پس‌دموکراسی» (کراچ، ۲۰۰۴)؛ «پس‌دموکراسی پس از بحران‌ها» (کراچ، ۲۰۲۰)؛ «عصر سوم ارتباطات سیاسی» (بلوملر و کاوانا، ۱۹۹۹)؛ «دموکراسی رسانه‌ای» (مایر، ۲۰۰۲).",
        studies=[
            "کراچ (۲۰۰۴) تز پس‌دموکراسی را با استعارهٔ سهمی و مفهوم پاراپولیتیک معرفی کرد.",
            "بلوملر و کاوانا (۱۹۹۹) چارچوب عصر سوم ارتباطات سیاسی را برای تحلیل رسانه‌ای‌شدن سیاست ساختند.",
            "مایر (۲۰۰۲) استدلال کرد که منطق رسانه جای منطق حزب را می‌گیرد و سیاست را مستعمره می‌کند.",
            "کراچ (۲۰۲۰) تز را با بحران مالی، نابرابری و پوپولیسم به‌روز کرد.",
            "پژوهش‌های پوشش انتخاباتی، شخصیت‌محوری و مسابقهٔ اسبی را در رسانه مستند کردند.",
            "مطالعات مالکیت رسانه، پیوند سرمایهٔ شرکتی و پوشش سیاسی را ردیابی کردند.",
            "پژوهش‌های مشارکت مدنی، افول عضویت حزبی و اتحادیه‌ای را سنجیدند.",
            "مطالعات رسانه‌های اجتماعی، گذر از میانجی‌های حزبی به ارتباط مستقیم رهبر–مخاطب را بررسی کردند.",
            "پژوهش‌های تطبیقی، دشواری سنجش تهی‌شدن دموکراسی را نشان دادند.",
        ],
        detailed_analysis=(
            "۱. بنیان و منطق نظری\n"
            "پس‌دموکراسی، به تعبیر کالین کراچ (۲۰۰۴)، وضعیتی است که در آن نهادهای رسمی دموکراسی — انتخابات، پارلمان، احزاب و رسانهٔ نسبتاً آزاد — سر جای خود می‌مانند و حتی پرجنب‌وجوش‌تر می‌شوند، اما منطق ادارهٔ جامعه به الگویی نزدیک به پیش‌دموکراسی بازمی‌گردد. کراچ این سیر را با استعارهٔ «سهمی» صورتبندی می‌کند: جوامع از پیش‌دموکراسی به دموکراسی بالا می‌روند و سپس، بی‌آنکه نهادها فروبپاشند، به پس‌دموکراسی فرود می‌آیند. نکتهٔ کلیدی آن است که پس‌دموکراسی نفی دموکراسی نیست؛ صورت‌ها حفظ می‌شوند و روح در آن‌ها تحلیل می‌رود.\n\n"
            "۲. سازه‌های مفهومی\n"
            "در کنار استعارهٔ سهمی، «پاراپولیتیک» مفهوم محوری است: سیاستی نمایشی که در کنار و به‌جای سیاست واقعی اجرا می‌شود. طبقهٔ سیاسی حرفه‌ای، شهروند–تماشاگر، تجاری‌سازی خدمات عمومی، افول سازمان‌های واسط مانند احزاب عضویت‌محور و اتحادیه‌ها، و نابرابری فزاینده سازه‌های دیگرند. کراچ استدلال می‌کند که سیاست به رقابت تیم‌های حرفه‌ای بر سر رأی بدل شده و تصمیم‌های بنیادین دربارهٔ توزیع ثروت و قدرت بیرون از دسترس شهروندان گرفته می‌شود.\n\n"
            "۳. سازوکار رسانه‌ای\n"
            "کراچ خود بیشتر اقتصاد سیاسی را تحلیل می‌کند تا سازوکار رسانه را؛ تحلیل رسانه‌ای کامل‌تر از پیوند تز او با پژوهش‌های ارتباطات سیاسی به دست می‌آید. بلوملر و کاوانا (۱۹۹۹) «عصر سوم» ارتباطات سیاسی را با فراوانی رسانه، حرفه‌ای‌شدن ارتباطات سیاسی و تکه‌تکه‌شدن مخاطبان توصیف کردند. مایر (۲۰۰۲) استدلال کرد که منطق رسانه — جذابیت، شخصیت‌محوری، درام و سرعت — جای منطق حزب را می‌گیرد و سیاست را مستعمره می‌کند. در این چارچوب، پوشش انتخاباتی به مسابقهٔ شخصیت‌ها و رسوایی‌ها فروکاسته می‌شود، بسته‌بندی حرفه‌ای پیام جای گفت‌وگوی درون‌حزبی را می‌گیرد، دسترسی به رسانه پرهزینه یا وابسته به روابط می‌شود، و رهبران با رسانه‌های اجتماعی میانجی‌های حزبی و پارلمانی را دور می‌زنند.\n\n"
            "۴. نمونه‌های تحلیلی\n"
            "پوشش انتخاباتی که برنامه‌ها را به حاشیه می‌راند و رقابت شخصیت‌ها را برجسته می‌کند نمونهٔ آشکار پاراپولیتیک است. تصویب سیاست‌های ریاضتی برخلاف نظر اکثریت، در حالی که سازوکارهای رسمی رأی‌گیری کار می‌کنند، نمونهٔ فاصلهٔ نهاد و تصمیم است. چرخش مدیران دولتی به شرکت‌های لابی‌گر و بازگشت دوبارهٔ آن‌ها (درِ گردان) نفوذ شرکتی را نشان می‌دهد. تجاری‌سازی خدمات عمومی مانند سلامت و آموزش، منطق شهروندی را به منطق مشتری فرو می‌کاهد. افول روزنامه‌نگاری محلی و گسترش «بیابان‌های خبری» توان نظارت عمومی را می‌کاهد و هم‌زمان ارتباط مستقیم رهبر با هواداران در شبکه‌های اجتماعی، سیاست را به همه‌پرسی‌های مکرر و بی‌واسطه بدل می‌کند.\n\n"
            "۵. سیر تاریخی\n"
            "کتاب ۲۰۰۴ تز را در بستر جهانی‌شدن و افول سازمان‌های جمعی صورت‌بندی کرد. کتاب ۲۰۲۰ آن را با بحران مالی ۲۰۰۸، سیاست ریاضت، نابرابری و ظهور پوپولیسم به‌روز کرد. در همین دوره، پژوهش‌های ارتباطات سیاسی دربارهٔ تبلیغات داده‌محور، پلتفرم‌ها و افول روزنامه‌نگاری نظارتی، لایهٔ رسانه‌ای تز را غنی‌تر کردند.\n\n"
            "۶. نقدها و چالش‌ها\n"
            "نخستین نقد، نوستالژی است: آیا دموکراسی پیشین واقعاً «کامل» بود یا خود شکل ویژه‌ای از توازن طبقاتی؟ دوم، سنجش تهی‌شدن دشوار است و شاخص روشنی ندارد. سوم، مدل نقش مقاومت مدنی، دادگاه‌های مستقل و روزنامه‌نگاری تحقیقی را کم‌برآورد می‌کند. چهارم، خطر هم‌ارز گرفتن پس‌دموکراسی با اقتدارگرایی وجود دارد؛ در حالی که در تحلیل لویتسکی و وِی (۲۰۱۰) رقابت انتخاباتی واقعی اما نابرابر نشانهٔ رژیم ترکیبی است و سرکوب نظام‌مند در آن جای دیگری دارد. سرانجام، تبیین نخبه‌محور، عاملیت رأی‌دهندگان و پویایی‌های پایین‌به‌بالا را نادیده می‌گیرد.\n\n"
            "۷. جایگاه در بحث روز\n"
            "در بحث امروز دربارهٔ پس‌رفت دموکراسی، پس‌دموکراسی قطب «آرام» را نشان می‌دهد: نهادها می‌مانند و قدرت جابه‌جا می‌شود؛ در برابر قطب «پرسروصدای» اقتدارگرایی که در آن نهادها آشکارا هدف گرفته می‌شوند. این تفکیک برای سیاست‌گذاری رسانه‌ای — سقف مالکیت، رسانهٔ عمومی، شفافیت پلتفرم‌ها و حمایت از روزنامه‌نگاری محلی — پیامدهای عملی دارد و پیوند این مدل با «دموکراسی مخاطب» و «رژیم ترکیبی رقابتی» را روشن می‌کند."),
    ),
    "MC-643": dict(
        needs_enrichment=False,
        level="میان",
        related_approaches="مطالعات اقتدارگرایی؛ جامعه‌شناسی سیاسی تطبیقی؛ اقتصاد سیاسی رسانه؛ نظریهٔ رژیم‌های ترکیبی؛ ارتباطات سیاسی.",
        recommended_sources="«انتخابات بدون دموکراسی» (لویتسکی و وِی، ۲۰۰۲)؛ «اقتدارگرایی رقابتی» (لویتسکی و وِی، ۲۰۱۰)؛ «کثرت‌گرایی پیش‌فرض» (وِی، ۲۰۱۵)؛ «مروری بر کثرت‌گرایی پیش‌فرض» (هیل، ۲۰۱۷).",
        studies=[
            "مقالهٔ ۲۰۰۲ اقتدارگرایی رقابتی را به‌عنوان نوعی رژیم ترکیبی معرفی کرد.",
            "کتاب ۲۰۱۰ مفهوم را با ۳۵ مورد پس از جنگ سرد و چهار عرصهٔ رقابت آزمود.",
            "وِی (۲۰۱۵) نشان داد کثرت‌گرایی می‌تواند محصول ضعف دولت باشد، نه طراحی نهادی.",
            "هیل (۲۰۱۷) محدودیت‌های تبیین مبتنی بر ضعف را بررسی کرد.",
            "پژوهش‌های رسانه، مالکیت، آزار حقوقی و یارانهٔ دولتی را در این رژیم‌ها مستند کردند.",
            "مطالعات مجارستان، ترکیه و روسیه، ادغام رسانه و فشار مالی را ردیابی کردند.",
            "پژوهش‌های حقوقی، شکایت‌های تهمت و آزار روزنامه‌نگاران را ثبت کردند.",
            "مطالعات دیجیتال، سانسور نرم و کنترل پلتفرم را در رژیم‌های ترکیبی بررسی کردند.",
            "پژوهش‌های تطبیقی، دشواری مرزبندی دموکراسی ناقص و اقتدارگرایی رقابتی را نشان دادند.",
        ],
        detailed_analysis=(
            "۱. بنیان و منطق نظری\n"
            "استیون لویتسکی و لوکان وِی در مقالهٔ ۲۰۰۲ و سپس کتاب ۲۰۱۰، «اقتدارگرایی رقابتی» را برای توصیف رژیم‌هایی ساختند که نهادهای رسمی دموکراسی را دارند و انتخابات در آن‌ها ابزار اصلی دستیابی به قدرت است، اما حاکمان چنان مکرر و چنان گسترده قواعد را نقض می‌کنند که رژیم به معیارهای متعارف حداقلی دموکراسی نمی‌رسد. تفاوت کلیدی با اقتدارگرایی بسته آن است که در این رژیم‌ها رقابت واقعی و فضای نسبی مخالفت وجود دارد؛ تفاوت با دموکراسی آن است که میدان رقابت به‌طور نظام‌مند به سود حاکم چیده شده است.\n\n"
            "۲. سازه‌های مفهومی\n"
            "مفهوم محوری «بهره‌برداری حاکم از موقعیت» است: سوءاستفاده از منابع دولتی، دستگاه قضایی، رسانه‌های عمومی و قانون‌گذاری برای ماندن در قدرت. کتاب ۲۰۱۰ رقابت را در چهار عرصه می‌سنجد: انتخاباتی، قانون‌گذاری، قضایی و رسانه‌ای. در عرصهٔ رسانه، پرسش‌های سنجش شامل وجود رسانهٔ مستقل، دسترسی نامتقارن نامزدها، آزار روزنامه‌نگاران، شکایت‌های حقوقی، مقررات مجوز و تخصیص فرکانس، یارانهٔ تبلیغات دولتی، تمرکز مالکیت و رشوه است. این چارچوب در برابر مفاهیم مجاور مانند «اقتدارگرایی انتخاباتی» و «رژیم ترکیبی» جای می‌گیرد و بر تداوم نهادهای صوری تأکید می‌کند.\n\n"
            "۳. جایگاه رسانه در مدل\n"
            "نکتهٔ مهم و اغلب نادیده‌گرفته‌شده آن است که در کتاب ۲۰۱۰ رسانه یکی از عرصه‌های سنجش است و نه متغیر توضیحی اصلی؛ توضیح مسیر رژیم‌ها بیشتر بر پیوند با غرب، قدرت دولت، ساختار اقتصادی و سازمان‌پذیری رژیم تکیه دارد. با این حال، عرصهٔ رسانه از دو جهت اهمیت دارد: نخست، رسانهٔ مستقل شرط هماهنگی مخالفان و نظارت بر قدرت است؛ دوم، تسخیر رسانه ابزار اصلی مشروعیت‌سازی و بی‌اثر کردن رقابت است. سازوکارها دولایه‌اند: لایهٔ رسمی مانند مجوز، جریمه، مالیات و قواعد مالکیت؛ و لایهٔ غیررسمی مانند فشار مالی بر آگهی‌دهندگان، رشوه، تهدید و آزار. نتیجه، رسانه‌ای است که هم‌زمان کثرت‌گرا و ناکامل می‌ماند: صدای مخالف شنیده می‌شود اما به‌ندرت به قدرت می‌رسد.\n\n"
            "۴. نمونه‌های تحلیلی\n"
            "در روسیهٔ دههٔ ۲۰۰۰، انتقال مالکیت شبکهٔ تلویزیونی مستقل به شرکت‌های نزدیک به دولت و فشار بر روزنامه‌نگاران، نمونهٔ کلاسیک تسخیر رسانه است. در مجارستان دههٔ ۲۰۱۰، رسانه‌های عمومی زیر یک مدیریت واحد ادغام شدند و صدها رسانهٔ محلی به بنیادهای نزدیک به دولت منتقل شدند. در ترکیه، جریمه‌های مالیاتی سنگین علیه گروه رسانه‌ای مخالف در سال ۲۰۰۹ و بازآرایی مالکیت پس از آن نمونهٔ فشار اقتصادی است. در ونزوئلا، تمدید نشدن مجوز یک شبکهٔ تلویزیونی مخالف در ۲۰۰۷ نمونهٔ ابزار مقرراتی است. در مالزی، کنترل رسانه‌های اصلی تا تغییر انتخاباتی ۲۰۱۸ ادامه یافت.\n\n"
            "۵. سیر تاریخی\n"
            "بحث رژیم‌های ترکیبی در دههٔ ۱۹۹۰ و ۲۰۰۰ با مفاهیمی مانند اقتدارگرایی انتخاباتی و دموکراسی ناقص شکل گرفت. مقالهٔ ۲۰۰۲ و کتاب ۲۰۱۰ چارچوب را تثبیت کردند. سپس وِی (۲۰۱۵) با «کثرت‌گرایی پیش‌فرض» تأکید را جابه‌جا کرد: در بسیاری از کشورها کثرت‌گرایی از ضعف دولت و ناتوانی در تسخیر کامل جامعه می‌آید، نه از تعهد نهادی. از دههٔ ۲۰۱۰، پژوهش‌های اقتدارگرایی دیجیتال و تسخیر رسانه، لایهٔ پلتفرمی را به مدل افزودند.\n\n"
            "۶. نقدها و چالش‌ها\n"
            "نخستین نقد، کشش مفهومی است: تعریف چنان باز است که طیف وسیعی از رژیم‌ها را در بر می‌گیرد. دوم، سنجش عرصهٔ رسانه به قضاوت کدگذار وابسته است و آستانهٔ آن روشن نیست. سوم، تمرکز بر سطح ملی، پویایی‌های فراملی و پلتفرم‌های جهانی را کم‌بررسی می‌گذارد. چهارم، تصویر ایستا در برابر پویایی گذار و پس‌رفت دموکراسی محدودیت دارد. پنجم، مرز با «دموکراسی ناقص» در موارد میانی مبهم می‌ماند و خطر برچسب‌گذاری سیاسی وجود دارد. سرانجام، تبیین ساختاری، عاملیت روزنامه‌نگاران، دادگاه‌ها و جنبش‌های مدنی را کم‌وزن می‌کند.\n\n"
            "۷. جایگاه در بحث روز\n"
            "در بحث امروز دربارهٔ پس‌رفت دموکراسی، مدل رژیم ترکیبی رقابتی ابزار تحلیلی برای تفکیک «سرکوب آشکار» از «رقابت نابرابر» فراهم می‌کند و به همین دلیل با مدل پس‌دموکراسی کراچ قابل مقایسه است: در پس‌دموکراسی رقابت انتخاباتی واقعی است و قدرت از راه نفوذ شرکتی جابه‌جا می‌شود؛ در اقتدارگرایی رقابتی رقابت وجود دارد اما میدان به سود حاکم چیده شده است. کاربردهای امروزین آن شامل تحلیل تسخیر رسانه، شکایت‌های آزاردهنده، جاسوس‌افزار و مقررات پلتفرم است."),
    ),
}

NAME_FIX = {}
YEAR_FIX = {}


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



YEAR_FIX.update({
    "MC-582": "year corrected 2000 -> 2001 (verified anchor: Baker & Martinson, TARES Test, 2001); note: editorial card theorist attribution was unverifiable and documentation rebuilt from verified literature",
    "MC-598": "no year change; note: editorial card core_logic was a mismatched media-economics template, documentation rebuilt from Heath (1993) and Ihlen (2011)",
})


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
                                       "verified": n_verified, "batch": 221}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH221 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
