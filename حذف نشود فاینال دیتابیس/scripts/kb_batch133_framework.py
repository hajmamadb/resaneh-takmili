# -*- coding: utf-8 -*-
"""Batch 133 (MODEL): full documentation for MC-131, MC-132, MC-133, MC-135."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch133-model-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch133_model.json"

S = {
    "MC-131": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Persuasion Knowledge Model: How People Cope with Persuasion Attempts",
             title_fa="مدل دانش اقناع: مردم چگونه با کوشش‌های اقناعی روبه‌رو می‌شوند",
             authors="Friestad, M.; Wright, P.", year=1994,
             publisher="Journal of Consumer Research",
             doi=None,
             url="https://academic.oup.com/jcr/article-abstract/21/1/1/1853712",
             language="en", isbn=None,
             citation="Friestad, M., & Wright, P. (1994). The persuasion knowledge model: How people cope with persuasion attempts. Journal of Consumer Research, 21(1), 1-31.",
             locator="21(1):1-31", locator_type="page_range",
             supports="persuasion knowledge and coping tactics in response to persuasion attempts", verified=True),
        dict(kind="BOOK_CHAPTER",
             title_en="Persuasion Knowledge in Consumer Research",
             title_fa="دانش اقناع در پژوهش مصرف",
             authors="Eisend, M.", year=2024,
             publisher="Edward Elgar (Handbook chapter)",
             doi=None, url=None, language="en", isbn=None,
             citation="Eisend, M. (2024). Persuasion knowledge in consumer research. In Handbook of Persuasion (ch. 75). Edward Elgar Publishing.",
             locator="ch. 75", locator_type="SECTION",
             supports="review of persuasion knowledge research and extensions", verified=False),
    ],
    "MC-132": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Putting the Fear Back into Fear Appeals: The Extended Parallel Process Model",
             title_fa="بازگرداندن ترس به پیام‌های ترس: مدل فرایند موازی گسترده",
             authors="Witte, K.", year=1992,
             publisher="Communication Monographs",
             doi="10.1080/03637759209376276",
             url="https://www.tandfonline.com/doi/abs/10.1080/03637759209376276",
             language="en", isbn=None,
             citation="Witte, K. (1992). Putting the fear back into fear appeals: The extended parallel process model. Communication Monographs, 59(4), 329-349.",
             locator="59(4):329-349", locator_type="page_range",
             supports="danger control versus fear control in response to threat and efficacy", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="A Meta-Analysis of Fear Appeals: Implications for Effective Public Health Campaigns",
             title_fa="فراتحلیل پیام‌های ترس: پیامدها برای کمپین‌های مؤثر سلامت عمومی",
             authors="Witte, K.; Allen, M.", year=2000,
             publisher="Health Education & Behavior",
             doi=None, url=None, language="en", isbn=None,
             citation="Witte, K., & Allen, M. (2000). A meta-analysis of fear appeals: Implications for effective public health campaigns. Health Education & Behavior, 27(5), 591-615.",
             locator="27(5):591-615", locator_type="page_range",
             supports="meta-analytic evidence on fear appeal effectiveness and efficacy", verified=False),
    ],
    "MC-133": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Health Belief Model and Preventive Health Behavior",
             title_fa="مدل باور سلامت و رفتار سلامت پیشگیرانه",
             authors="Rosenstock, I. M.", year=1974,
             publisher="Health Education Monographs",
             doi="10.1177/109019817400200405",
             url="https://journals.sagepub.com/doi/10.1177/109019817400200405",
             language="en", isbn=None,
             citation="Rosenstock, I. M. (1974). The health belief model and preventive health behavior. Health Education Monographs, 2(4), 354-386.",
             locator="2(4):354-386", locator_type="page_range",
             supports="perceived susceptibility, severity, benefits and barriers in preventive behavior", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Health Belief Model and Sick Role Behavior",
             title_fa="مدل باور سلامت و رفتار نقش بیمار",
             authors="Becker, M. H.", year=1974,
             publisher="Health Education Monographs",
             doi=None, url=None, language="en", isbn=None,
             citation="Becker, M. H. (1974). The health belief model and sick role behavior. Health Education Monographs, 2(4), 409-419.",
             locator="2(4):409-419", locator_type="page_range",
             supports="extension of the model to sick-role behavior", verified=False),
    ],
    "MC-135": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="A Model for Predictive Measurements of Advertising Effectiveness",
             title_fa="مدلی برای سنجش پیش‌بینانهٔ اثربخشی تبلیغات",
             authors="Lavidge, R. J.; Steiner, G. A.", year=1961,
             publisher="Journal of Marketing",
             doi="10.1177/002224296102500611",
             url="https://journals.sagepub.com/doi/full/10.1177/002224296102500611",
             language="en", isbn=None,
             citation="Lavidge, R. J., & Steiner, G. A. (1961). A model for predictive measurements of advertising effectiveness. Journal of Marketing, 25(6), 59-62.",
             locator="25(6):59-62", locator_type="page_range",
             supports="six-stage hierarchy from awareness to purchase", verified=True),
        dict(kind="BOOK",
             title_en="Defining Advertising Goals for Measured Advertising Results",
             title_fa="تعریف اهداف تبلیغاتی برای نتایج اندازه‌گیری‌شدهٔ تبلیغات",
             authors="Colley, R. H.", year=1961,
             publisher="Association of National Advertisers",
             doi=None, url=None, language="en", isbn=None,
             citation="Colley, R. H. (1961). Defining Advertising Goals for Measured Advertising Results. New York: Association of National Advertisers.",
             locator="book", locator_type="SECTION",
             supports="DAGMAR approach to measurable advertising objectives", verified=False),
    ],
}

ENRICH = {
    "MC-131": dict(
        year=1994,
        summary="مدل دانش اقناع، مدلی در روان‌شناسی مصرف و ارتباطات اقناعی است که ماریان فریستد و پیتر رایت در سال ۱۹۹۴ در مجلهٔ پژوهش مصرف معرفی کردند. ادعای مرکزی این است که مخاطبان با گذشت زمان سه نوع دانش را دربارهٔ کوشش‌های اقناعی می‌سازند: دانش موضوعی، یعنی اطلاعات دربارهٔ محصول یا موضوع پیام؛ دانش اقناع، یعنی شناخت از شیوه‌ها و انگیزه‌های اقناع، مانند تبلیغ، تعریف از محصول و چارچوب‌بندی؛ و دانش عامل، یعنی باورها دربارهٔ فرستنده و ویژگی‌های او. وقتی مخاطب تشخیص می‌دهد پیام با هدف اقناع ساخته شده، دانش اقناعی او فعال می‌شود و راهبردهای مقابله مانند تردید، بررسی انتقادی، کنارگذاری پیام یا واکنش دفاعی را به کار می‌گیرد؛ در نتیجه اعتماد به فرستنده و پذیرش پیام کاهش می‌یابد. دانش اقناعی در طول زندگی و با تجربهٔ رسانه‌ای تقویت می‌شود و کودکان کمترین و بزرگسالان بیشترین سطح آن را دارند. این مدل، چارچوب پژوهش سواد تبلیغاتی، تبلیغات بومی و بازاریابی تأثیرگذار شد. نقدهای اصلی به آن، دشواری سنجش دانش اقناعی، تفاوت‌های فردی و فرهنگی و پیچیدگی محیط دیجیتال و تبلیغات پنهان مربوط می‌شود.",
        definition="مدل دانش اقناع، مدلی است که توضیح می‌دهد مخاطبان با دانش موضوعی، دانش اقناع و دانش عامل، کوشش‌های اقناعی را تشخیص می‌دهند و با راهبردهای مقابله به آنها پاسخ می‌دهند.",
        main_problem="مخاطبان چگونه تشخیص می‌دهند که پیامی با هدف اقناع ساخته شده، و از چه راهبردهایی برای مقابله با آن استفاده می‌کنند.",
        mechanism="مخاطب با نشانه‌هایی مانند قالب تبلیغاتی یا انگیزهٔ فرستنده، کوشش اقناعی را بازمی‌شناسد؛ دانش اقناعی فعال می‌شود و معنای پیام را از «اطلاعات» به «تلاش برای ترغیب» تغییر می‌دهد. این بازتفسیر، ارزیابی انتقادی یا دفاعی را برمی‌انگیزد و پذیرش پیام را کاهش می‌دهد.",
        assumptions=[
            "مخاطب دربارهٔ شیوه‌های اقناع دانش می‌سازد.",
            "دانش اقناعی با تجربهٔ رسانه‌ای افزایش می‌یابد.",
            "تشخیص هدف اقناعی، پاسخ مقابله‌ای برمی‌انگیزد.",
            "سه نوع دانش موضوعی، اقناعی و عامل از هم تفکیک‌پذیرند.",
            "بازتفسیر معنای پیام، پذیرش را تغییر می‌دهد.",
        ],
        principles=[
            "مخاطب منفعل نیست و دانش اقناعی دارد.",
            "دانش اقناعی، معنای پیام را بازتفسیر می‌کند.",
            "راهبردهای مقابله را باید بخشی از فرایند اقناع دانست.",
            "افزایش دانش اقناعی، اعتماد به تبلیغ را کاهش می‌دهد.",
            "کودکان در برابر اقناع آسیب‌پذیرترند.",
            "طراحی پیام باید واکنش دانش اقناعی مخاطب را پیش‌بینی کند.",
        ],
        critiques=[
            "سنجش دانش اقناعی دشوار و اغلب غیرمستقیم است.",
            "تفاوت‌های فردی و فرهنگی کم‌بررسی می‌ماند.",
            "تبلیغات بومی و پنهان، تشخیص را دشوار می‌کند.",
            "رابطهٔ دانش اقناعی و رفتار همیشه خطی نیست.",
            "در محیط دیجیتال، نشانه‌های اقناع مبهم‌تر شده‌اند.",
        ],
        critique_text="منتقدان می‌گویند مدل دانش اقناع چارچوبی ارزشمند برای فهم مقاومت مخاطب فراهم کرد اما سنجش دانش اقناعی دشوار است و در محیط تبلیغات بومی و الگوریتمی، تشخیص هدف اقناعی پیچیده‌تر شده است. با این حال، به چارچوب مرجع سواد تبلیغاتی تبدیل شده است.",
        applications=[
            "پژوهش سواد تبلیغاتی کودکان و نوجوانان.",
            "تحلیل تبلیغات بومی و بازاریابی تأثیرگذار.",
            "طراحی پیام با پیش‌بینی مقاومت مخاطب.",
            "آموزش سواد رسانه‌ای و مصرف انتقادی.",
            "تحلیل الگوهای تاریک و اقناع پنهان در رابط کاربری.",
        ],
        example_text="کاربری که متوجه می‌شود ویدئوی یک اینفلوئنسر با هزینهٔ برند ساخته شده است، پیام را نه توصیهٔ صادقانه بلکه تبلیغ می‌بیند و با تردید بیشتری به آن واکنش می‌دهد. مدل دانش اقناع همین فرایند بازشناسی و مقابله را توضیح می‌دهد.",
        evolution="ریشهٔ مدل در پژوهش اقناع و رفتار مصرف‌کنندهٔ دههٔ ۱۹۸۰ است. مقالهٔ سال ۱۹۹۴ آن را تثبیت کرد و پژوهش‌های بعدی، آن را به سواد تبلیغاتی، رسانهٔ دیجیتال و بازاریابی تأثیرگذار گستردند.",
        key_concepts=["دانش اقناع", "دانش موضوعی", "دانش عامل", "راهبرد مقابله", "بازتفسیر معنا", "سواد تبلیغاتی"],
        theorists="ماریان فریستد و پیتر رایت، صورت‌بندانان مدل دانش اقناع.",
        theorists_text="این مدل در سنت روان‌شناسی مصرف و پژوهش اقناع شکل گرفت و با سواد رسانه‌ای پیوند خورد.",
        model="مدل سه‌دانشی: دانش موضوعی، اقناعی و عامل؛ تشخیص کوشش اقناعی، فعال‌سازی دانش اقناعی، بازتفسیر معنا و انتخاب راهبرد مقابله را در بر می‌گیرد.",
        studies=[
            "مقالهٔ سال ۱۹۹۴ مدل را با مرور پژوهش اقناع معرفی کرد.",
            "مطالعات سواد تبلیغاتی، رشد دانش اقناعی در کودکان را بررسی کردند.",
            "پژوهش تبلیغات بومی، تشخیص و مقاومت مخاطب را آزمود.",
            "مطالعات دیجیتال، مدل را برای اینفلوئنسر مارکتینگ به کار بردند.",
        ],
    ),
    "MC-132": dict(
        year=1992,
        summary="مدل فرایند موازی گسترده، مدلی در پژوهش پیام‌های ترس و ارتباطات سلامت است که کاتلین ویت در سال ۱۹۹۲ در مونوگراف‌های ارتباطات معرفی کرد. ادعای مرکزی این است که مواجهه با پیام ترس دو ارزیابی پیاپی را برمی‌انگیزد: ارزیابی تهدید، یعنی درک شدت و احتمال خطر، و ارزیابی کارآمدی، یعنی باور به اثربخشی رفتار توصیه‌شده و توانایی فرد برای انجام آن. اگر تهدید درک شود و کارآمدی بالا باشد، فرد به «کنترل خطر» می‌رسد و رفتار محافظ را انجام می‌دهد؛ اما اگر تهدید بالا و کارآمدی پایین باشد، فرد به «کنترل ترس» روی می‌آورد و با انکار، اجتناب یا تحقیر پیام، ترس خود را مدیریت می‌کند؛ در این حالت پیام بی‌اثر یا حتی معکوس می‌شود. بنابراین افزایش ترس بدون افزایش کارآمدی توصیه نمی‌شود و پیام مؤثر باید هر دو مؤلفهٔ تهدید و کارآمدی را در بر داشته باشد. این مدل، چارچوب طراحی کمپین‌های سلامت، هشدارهای عمومی و پیام‌های ضدسیگار و ایدز شد. نقدهای اصلی به آن، دشواری سنجش کنترل ترس، ملاحظات اخلاقی پیام ترس و ناهمگونی شواهد میدانی مربوط می‌شود.",
        definition="مدل فرایند موازی گسترده، مدلی است که پاسخ به پیام ترس را حاصل دو ارزیابی تهدید و کارآمدی می‌داند و دو مسیر کنترل خطر و کنترل ترس را از هم تفکیک می‌کند.",
        main_problem="چه زمانی پیام‌های ترس‌محور رفتار محافظ ایجاد می‌کنند و چه زمانی به انکار و اجتناب می‌انجامند.",
        mechanism="پیام ترس، تهدید درک‌شده را بالا می‌برد؛ اگر فرد باور داشته باشد که توصیه مؤثر است و خودش توان انجام آن را دارد، مسیر کنترل خطر فعال می‌شود. اگر کارآمدی پایین باشد، ترس بی‌پاسخ می‌ماند و فرد برای کاهش احساس ترس به انکار یا اجتناب روی می‌آورد.",
        assumptions=[
            "ترس، پاسخ انگیزشی قدرتمندی است.",
            "درک تهدید از شدت و احتمال خطر ساخته می‌شود.",
            "کارآمدی پاسخ و خودکارآمدی، مسیر پاسخ را تعیین می‌کنند.",
            "ترس بدون کارآمدی به کنترل ترس می‌انجامد.",
            "دو مسیر کنترل خطر و کنترل ترس موازی‌اند.",
        ],
        principles=[
            "پیام ترس باید هم تهدید و هم کارآمدی را افزایش دهد.",
            "افزایش ترس بدون کارآمدی توصیه نمی‌شود.",
            "کارآمدی پاسخ و خودکارآمدی باید جدا سنجیده شوند.",
            "انکار و اجتناب نشانهٔ کنترل ترس است.",
            "طراحی پیام باید پاسخ‌های دفاعی را پیش‌بینی کند.",
            "سنجش تهدید و کارآمدی، پیش‌شرط ارزیابی کمپین است.",
        ],
        critiques=[
            "سنجش کنترل ترس در پژوهش دشوار است.",
            "پیام ترس ملاحظات اخلاقی جدی دارد.",
            "شواهد میدانی در مقایسه با آزمایشگاه ناهمگون است.",
            "نقش تفاوت‌های فردی و فرهنگی کم‌بررسی می‌ماند.",
            "اثر بلندمدت پیام ترس روشن نیست.",
            "کارآمدی توصیه‌شده باید برای مخاطب واقعاً در دسترس باشد و گرنه مدل به کنترل ترس می‌انجامد.",
        ],
        critique_text="منتقدان می‌گویند مدل فرایند موازی گسترده توضیحی روشن برای شکست پیام‌های ترس‌محور فراهم کرد اما سنجش کنترل ترس و پیامدهای اخلاقی استفاده از ترس همچنان محل بحث است. با این حال، چارچوب مرجع طراحی و ارزیابی پیام‌های سلامت ترس‌محور است.",
        applications=[
            "طراحی کمپین‌های سلامت و هشدار عمومی.",
            "پیام‌های ضدسیگار، ایدز و بیماری‌های واگیر.",
            "ارزیابی کمپین‌های ترس‌محور.",
            "آموزش ارتباطات سلامت.",
            "طراحی پیام بحران و هشدار بلایا.",
            "آموزش مهارت مقابله در کنار پیام تهدید برای مخاطبان پرخطر.",
        ],
        example_text="کمپینی که فقط تصاویر هولناک بیماری را نشان می‌دهد اما راه پیشگیری روشن و در دسترس ارائه نمی‌کند، ممکن است مخاطب را به انکار وادارد؛ همان کمپین با افزودن راهنمای گام‌به‌گام و تأکید بر توانایی فرد، رفتار محافظ را برمی‌انگیزد. مدل فرایند موازی گسترده این تفاوت را توضیح می‌دهد.",
        evolution="ریشهٔ مدل در پژوهش پیام ترس دههٔ ۱۹۵۰ تا ۱۹۸۰ است. مقالهٔ سال ۱۹۹۲ چارچوب را تثبیت کرد و فراتحلیل سال ۲۰۰۰ شواهد کارآمدی آن را جمع‌بندی کرد.",
        key_concepts=["تهدید درک‌شده", "کارآمدی پاسخ", "خودکارآمدی", "کنترل خطر", "کنترل ترس", "انکار"],
        theorists="کاتلین ویت، صورت‌بند مدل فرایند موازی گسترده.",
        theorists_text="این مدل در سنت پژوهش ارتباطات سلامت و روان‌شناسی ترس شکل گرفت و با طراحی کمپین پیوند خورد.",
        model="مدل دو‌ارزیابی: ارزیابی تهدید و کارآمدی؛ ترکیب تهدید بالا و کارآمدی بالا به کنترل خطر، و تهدید بالا با کارآمدی پایین به کنترل ترس می‌انجامد.",
        studies=[
            "مقالهٔ سال ۱۹۹۲ مدل را با مرور انتقادی پژوهش ترس معرفی کرد.",
            "فراتحلیل سال ۲۰۰۰ اثر تهدید و کارآمدی را جمع‌بندی کرد.",
            "پژوهش‌های سلامت، مدل را در کمپین‌های واقعی آزمودند.",
            "مطالعات بعدی، ملاحظات اخلاقی پیام ترس را بررسی کردند.",
        ],
    ),
    "MC-133": dict(
        year=1974,
        summary="مدل باور سلامت، یکی از پرکاربردترین مدل‌های رفتار سلامت است که ایروین روزنستاک در سال ۱۹۷۴ در مونوگراف‌های آموزش سلامت صورت‌بندی کرد، هرچند ریشه‌های آن به پژوهش‌های خدمات بهداشت عمومی آمریکا در دههٔ ۱۹۵۰ بازمی‌گردد. ادعای مرکزی این است که رفتار سلامت پیشگیرانه به باورهای فرد دربارهٔ چند عامل وابسته است: حساسیت درک‌شده، یعنی احتمال ابتلا؛ شدت درک‌شده، یعنی جدی‌بودن پیامدهای بیماری؛ منافع درک‌شده، یعنی فایدهٔ رفتار؛ موانع درک‌شده، یعنی هزینه و دشواری رفتار؛ و نشانه‌های عمل، یعنی محرک‌های درونی یا بیرونی که فرد را به اقدام وامی‌دارد. در نسخه‌های بعدی، خودکارآمدی به‌عنوان عامل ششم افزوده شد. پیام‌های ارتباطی باید این باورها را هدف بگیرند و پیام مؤثر، موانع را کم و منافع را برجسته می‌کند. این مدل در طراحی برنامه‌های واکسیناسیون، غربالگری، تغذیه و پیشگیری کاربرد گسترده دارد. نقدهای اصلی به آن، فردگرایی و غفلت از عوامل ساختاری، توان پیش‌بینی محدود، ناسازگاری در عملیاتی‌سازی سازه‌ها و کم‌توجهی به عادت و عاطفه مربوط می‌شود.",
        definition="مدل باور سلامت، مدلی است که رفتار سلامت پیشگیرانه را تابعی از حساسیت، شدت، منافع و موانع درک‌شده، نشانه‌های عمل و خودکارآمدی می‌داند و پیام سلامت را ابزار تغییر این باورها می‌بیند.",
        main_problem="چرا برخی افراد رفتار سلامت پیشگیرانه انجام می‌دهند و برخی دیگر با وجود آگاهی، اقدام نمی‌کنند.",
        mechanism="فرد ابتدا احتمال و شدت خطر را می‌سنجد؛ سپس منافع رفتار را با موانع آن مقایسه می‌کند. اگر منافع بیشتر باشد و نشانه‌ای برای عمل وجود داشته باشد، احتمال اقدام بالا می‌رود. خودکارآمدی، توان انجام رفتار را تعیین می‌کند و پیام ارتباطی این محاسبه را تغییر می‌دهد.",
        assumptions=[
            "رفتار سلامت محصول باورهای شناختی فرد است.",
            "حساسیت و شدت درک‌شده، انگیزهٔ اقدام می‌سازند.",
            "منافع و موانع درک‌شده، تصمیم را قالب می‌زنند.",
            "نشانه‌های عمل، رفتار را فعال می‌کنند.",
            "پیام ارتباطی می‌تواند باورها را تغییر دهد.",
        ],
        principles=[
            "پیام سلامت باید حساسیت و شدت را هدف بگیرد.",
            "کاهش موانع درک‌شده به اندازهٔ برجسته‌سازی منافع مهم است.",
            "نشانه‌های عمل باید در طراحی پیام گنجانده شوند.",
            "خودکارآمدی را باید در پیام تقویت کرد.",
            "سازه‌ها را باید جداگانه سنجید.",
            "باورهای سلامت را باید در بافت اجتماعی فرد فهمید.",
        ],
        critiques=[
            "مدل فردگرا است و عوامل ساختاری را نادیده می‌گیرد.",
            "توان پیش‌بینی رفتار در پژوهش‌ها محدود بوده است.",
            "عملیاتی‌سازی سازه‌ها ناسازگار است.",
            "نقش عادت، عاطفه و هنجار اجتماعی کم‌بررسی می‌ماند.",
            "مدل، نقش محیط و دسترسی به خدمات را کم‌رنگ می‌کند.",
            "سازه‌ها اغلب با ابزارهای ناهمگون سنجیده شده‌اند.",
            "برای رفتارهای پیچیده و بلندمدت کافی نیست.",
        ],
        critique_text="منتقدان می‌گویند مدل باور سلامت چارچوبی ساده و کاربردی برای طراحی پیام سلامت فراهم کرد اما بیش از اندازه بر باورهای فردی تمرکز دارد و توان توضیح رفتار واقعی را در بسیاری از مطالعات نداشته است. با این حال، همچنان یکی از پرکاربردترین مدل‌های آموزش سلامت است.",
        applications=[
            "طراحی برنامهٔ واکسیناسیون و غربالگری.",
            "کمپین‌های پیشگیری از بیماری‌های واگیر.",
            "آموزش تغذیه و فعالیت بدنی.",
            "پژوهش رفتار سلامت و ارزیابی مداخله.",
            "طراحی پیام سلامت برای گروه‌های کم‌درآمد.",
            "ارزیابی برنامه‌های آموزش سلامت در مدارس و مراکز بهداشت.",
        ],
        example_text="در یک کمپین غربالگری سرطان، پیام مؤثر هم احتمال بیماری را جدی نشان می‌دهد، هم منافع تشخیص زودهنگام را برجسته می‌کند و هم موانعی مانند هزینه و ترس از آزمون را کاهش می‌دهد؛ مدل باور سلامت همین چهار محور را برای طراحی پیام تعیین می‌کند.",
        evolution="ریشهٔ مدل در پژوهش‌های خدمات بهداشت عمومی دههٔ ۱۹۵۰ است. مقالهٔ سال ۱۹۷۴ چارچوب را تثبیت کرد، خودکارآمدی در دههٔ ۱۹۸۰ افزوده شد و در دههٔ ۲۰۰۰ نقدهای ساختاری و بسط‌های یکپارچه شکل گرفت.",
        key_concepts=["حساسیت درک‌شده", "شدت درک‌شده", "منافع درک‌شده", "موانع درک‌شده", "نشانه‌های عمل", "خودکارآمدی"],
        theorists="ایروین روزنستاک و مارشال بکر، صورت‌بندانان و بسط‌دهندگان مدل باور سلامت.",
        theorists_text="این مدل در سنت آموزش سلامت و روان‌شناسی اجتماعی شکل گرفت و با پژوهش پیشگیری پیوند خورد.",
        model="مدل محاسبهٔ باور: حساسیت و شدت، انگیزه را می‌سازند؛ منافع منهای موانع، تصمیم را تعیین می‌کنند؛ نشانهٔ عمل و خودکارآمدی، اقدام را فعال می‌کنند.",
        studies=[
            "مقالهٔ سال ۱۹۷۴ چارچوب را برای رفتار پیشگیرانه صورت‌بندی کرد.",
            "پژوهش‌های بکر، مدل را به رفتار نقش بیمار گستردند.",
            "مرورهای نظام‌مند، توان پیش‌بینی مدل را ارزیابی کردند.",
            "مداخلات سلامت، سازه‌های مدل را در کمپین‌ها آزمودند.",
        ],
    ),
    "MC-135": dict(
        year=1961,
        summary="سلسله‌مراتب اثرات تبلیغ، مدلی در پژوهش تبلیغات است که رابرت لاویج و گری اشتاینر در سال ۱۹۶۱ در مجلهٔ بازاریابی معرفی کردند. ادعای مرکزی این است که تبلیغ اثر خود را در زنجیره‌ای از مراحل به‌ترتیب اعمال می‌کند: آگاهی، شناخت، دوست‌داشتن، ترجیح، اعتقاد و خرید؛ سه مرحلهٔ نخست شناختی، دو مرحلهٔ بعد عاطفی و مرحلهٔ آخر رفتاری‌اند. هر مرحله پیش‌نیاز مرحلهٔ بعد است و اندازه‌گیری در هر مرحله، تصویری دقیق‌تر از اثربخشی تبلیغ می‌دهد. مدل آیدا با مراحل توجه، علاقه، تمایل و عمل و رویکرد داگمار با تأکید بر تعریف اهداف تبلیغاتی قابل اندازه‌گیری، از خانوادهٔ همین منطق‌اند. این مدل، چارچوب برنامه‌ریزی کمپین، تعیین شاخص‌های اثربخشی و طراحی پژوهش تبلیغات شد. نقدهای اصلی به آن، فرض حرکت خطی و یکسان برای همهٔ مخاطبان، نامناسب‌بودن برای خریدهای کم‌درگیری، نادیده‌گرفتن مسیرهای غیرخطی دیجیتال و شواهد تجربی ناهمگون دربارهٔ ترتیب مراحل مربوط می‌شود.",
        definition="سلسله‌مراتب اثرات تبلیغ، مدلی است که اثر تبلیغ را در زنجیره‌ای از مراحل شناختی، عاطفی و رفتاری از آگاهی تا خرید توصیف می‌کند و هر مرحله را پیش‌نیاز مرحلهٔ بعد می‌داند.",
        main_problem="تبلیغ چگونه از ایجاد آگاهی به تغییر نگرش و سپس به خرید می‌رسد، و اثربخشی آن را در کدام مرحله می‌توان سنجید.",
        mechanism="تبلیغ ابتدا توجه و آگاهی ایجاد می‌کند؛ اطلاعات و شناخت را افزایش می‌دهد؛ با ایجاد نگرش مثبت، دوست‌داشتن و ترجیح را می‌سازد؛ با تقویت اعتقاد، قصد خرید را شکل می‌دهد و در نهایت رفتار خرید را برمی‌انگیزد. سنجش در هر مرحله، نقطهٔ ضعف زنجیره را آشکار می‌کند.",
        assumptions=[
            "اثر تبلیغ را می‌توان به مراحل قابل تفکیک تجزیه کرد.",
            "مراحل به‌ترتیب و به‌صورت انباشتی طی می‌شوند.",
            "نگرش مثبت، پیش‌شرط قصد و رفتار است.",
            "اندازه‌گیری مرحله‌ای، اثربخشی را دقیق‌تر نشان می‌دهد.",
            "هدف تبلیغاتی را می‌توان به شاخص قابل‌سنجش ترجمه کرد.",
            "اثر تبلیغ در هر مرحله می‌تواند مستقل از مراحل دیگر ضعیف یا قوی باشد.",
        ],
        principles=[
            "اثربخشی تبلیغ را باید مرحله‌به‌مرحله سنجید.",
            "آگاهی پیش‌نیاز شناخت و نگرش است.",
            "نگرش مثبت، قصد خرید را تقویت می‌کند.",
            "اهداف تبلیغ باید قابل اندازه‌گیری تعریف شوند.",
            "شکست در هر مرحله، اثر مراحل بعد را محدود می‌کند.",
            "طراحی کمپین باید با مرحلهٔ هدف هم‌خوان باشد.",
            "باید مشخص شود کدام مرحله شاخص اصلی موفقیت کمپین است.",
            "سنجش مرحله‌ای باید با داده‌های رفتار واقعی ترکیب شود.",
        ],
        critiques=[
            "حرکت خطی و یکسان مخاطبان را مفروض می‌گیرد.",
            "برای خریدهای کم‌درگیری و تکانشی مناسب نیست.",
            "مسیرهای غیرخطی و بازگشتی دیجیتال را نادیده می‌گیرد.",
            "شواهد ترتیب دقیق مراحل یکدست نیست.",
            "سنجش نگرش و قصد، همیشه پیش‌بین رفتار نیست.",
        ],
        critique_text="منتقدان می‌گویند سلسله‌مراتب اثرات تبلیغ چارچوبی ساده و کاربردی برای برنامه‌ریزی و سنجش فراهم کرد اما فرض خطی‌بودن مسیر را نمی‌توان برای همهٔ محصولات و مخاطبان تعمیم داد؛ در محصولات کم‌درگیری، آگاهی ممکن است مستقیماً به خرید بینجامد و مرحلهٔ ترجیح کمرنگ شود. با این حال، همچنان چارچوب پایهٔ آموزش و ارزیابی تبلیغات است.",
        applications=[
            "برنامه‌ریزی کمپین و تعیین اهداف مرحله‌ای.",
            "طراحی شاخص‌های اثربخشی تبلیغ.",
            "پژوهش بازار و سنجش نگرش برند.",
            "آموزش تبلیغات و بازاریابی.",
            "تحلیل قیف بازاریابی دیجیتال.",
        ],
        example_text="در یک کمپین اینترنتی، اگر شاخص آگاهی بالا رود اما ترجیح برند تغییر نکند، تیم بازاریابی می‌فهمد که مشکل در مرحلهٔ نگرش و پیام‌سازی است و نه در دیده‌شدن. سلسله‌مراتب اثرات همین تقسیم کار تشخیصی را ممکن می‌کند.",
        evolution="مدل در سنت پژوهش اثربخشی تبلیغات دههٔ ۱۹۶۰ شکل گرفت و همراه با آیدا و داگمار به چارچوب استاندارد صنعت تبدیل شد. در دههٔ ۲۰۰۰ با قیف دیجیتال و مسیرهای غیرخطی مخاطب بازخوانی شد.",
        key_concepts=["آگاهی", "شناخت", "دوست‌داشتن", "ترجیح", "اعتقاد", "خرید", "اثربخشی تبلیغ"],
        theorists="رابرت لاویج و گری اشتاینر، صورت‌بندانان مدل؛ و راسل کالی با رویکرد داگمار.",
        theorists_text="این مدل در سنت پژوهش اثربخشی تبلیغات و بازاریابی شکل گرفت و با اندازه‌گیری کمپین پیوند خورد.",
        model="مدل شش‌مرحله‌ای: دو مرحلهٔ شناختی (آگاهی، شناخت)، دو مرحلهٔ عاطفی (دوست‌داشتن، ترجیح) و دو مرحلهٔ رفتاری (اعتقاد، خرید)؛ هر مرحله پیش‌نیاز بعدی است.",
        studies=[
            "مقالهٔ سال ۱۹۶۱ مدل شش‌مرحله‌ای را معرفی کرد.",
            "رویکرد داگمار، اهداف قابل اندازه‌گیری را افزود.",
            "پژوهش‌های اثربخشی، ترتیب مراحل را آزمودند.",
            "مطالعات دیجیتال، مدل را برای قیف آنلاین بازخوانی کردند.",
            "پژوهش‌های کمپین، اثرگذاری مرحله‌ای تبلیغ را با داده‌های فروش سنجیدند.",
            "مرورهای اثربخشی، ترتیب مراحل را در دسته‌های محصول مقایسه کردند.",
        ],
    ),
}

NAME_FIX = {
    "MC-131": ("مدل دانش اقناع", "Persuasion Knowledge Model", "card name «دانش شیوه‌ی ترغیب» was a broken translation of Persuasion Knowledge Model"),
    "MC-132": ("مدل فرایند موازی گستردهٔ ترس", "Extended Parallel Process Model", "card name «مدل توازی گسترده ترس» mistranslated 'parallel process'"),
}

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
                                       "verified": n_verified, "batch": 133}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH133 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
