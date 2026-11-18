# -*- coding: utf-8 -*-
"""Batch 127 (FRAMEWORK): full documentation for MC-695, MC-702, MC-706, MC-712."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch127-framework-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch127_framework.json"

S = {
    "MC-695": [
        dict(kind="BOOK",
             title_en="Discovering the News: A Social History of American Newspapers",
             title_fa="کشف خبر: تاریخ اجتماعی روزنامه‌های آمریکایی",
             authors="Schudson, M.", year=1978,
             publisher="Basic Books",
             doi=None,
             url="https://searchworks.stanford.edu/view/1394312",
             language="en", isbn=None,
             citation="Schudson, M. (1978). Discovering the News: A Social History of American Newspapers. New York: Basic Books.",
             locator="book", locator_type="SECTION",
             supports="objectivity as a historical social product, not a natural given", verified=True),
        dict(kind="BOOK",
             title_en="Making News: A Study in the Construction of Reality",
             title_fa="ساختن خبر: پژوهشی در برساخت واقعیت",
             authors="Tuchman, G.", year=1978,
             publisher="Free Press",
             doi=None, url=None, language="en", isbn=None,
             citation="Tuchman, G. (1978). Making News: A Study in the Construction of Reality. New York: Free Press.",
             locator="news net and objectivity ritual", locator_type="SECTION",
             supports="news as a socially constructed reality; objectivity as strategic ritual", verified=False),
    ],
    "MC-702": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Solutions Journalism: The Effects of Including Solution Information in News Stories about Social Problems",
             title_fa="روزنامه‌نگاری راه‌حل‌محور: اثرهای افزودن اطلاعات راه‌حل در گزارش‌های اجتماعی",
             authors="McIntyre, K.", year=2019,
             publisher="Journalism Practice",
             doi=None, url=None, language="en", isbn=None,
             citation="McIntyre, K. (2019). Solutions journalism: The effects of including solution information in news stories about social problems. Journalism Practice, 13(1), 16-34.",
             locator="13(1):16-34", locator_type="page_range",
             supports="experimental evidence on effects of solution information in news", verified=True),
        dict(kind="BOOK",
             title_en="From Mirrors to Movers: Five Elements of Positive Psychology in Constructive Journalism",
             title_fa="از آینه تا محرک: پنج عنصر روان‌شناسی مثبت در روزنامه‌نگاری سازنده",
             authors="Gyldensted, C.", year=2015,
             publisher="Group Publishing",
             doi=None, url=None, language="en", isbn=None,
             citation="Gyldensted, C. (2015). From Mirrors to Movers: Five Elements of Positive Psychology in Constructive Journalism. Charleston: Group Publishing.",
             locator="book", locator_type="SECTION",
             supports="constructive journalism framing of solutions-oriented reporting", verified=False),
    ],
    "MC-706": [
        dict(kind="BOOK",
             title_en="Social Learning and Personality Development",
             title_fa="یادگیری اجتماعی و رشد شخصیت",
             authors="Bandura, A.; Walters, R. H.", year=1963,
             publisher="Holt, Rinehart and Winston",
             doi=None,
             url="https://psycnet.apa.org/record/1963-35030-000",
             language="en", isbn=None,
             citation="Bandura, A., & Walters, R. H. (1963). Social Learning and Personality Development. New York: Holt, Rinehart and Winston.",
             locator="book", locator_type="SECTION",
             supports="observational learning, modeling and vicarious reinforcement", verified=True),
        dict(kind="BOOK",
             title_en="Social Learning Theory",
             title_fa="نظریهٔ یادگیری اجتماعی",
             authors="Bandura, A.", year=1977,
             publisher="Prentice Hall",
             doi=None, url=None, language="en", isbn=None,
             citation="Bandura, A. (1977). Social Learning Theory. Englewood Cliffs: Prentice Hall.",
             locator="book", locator_type="SECTION",
             supports="consolidated statement of social learning theory", verified=False),
    ],
    "MC-712": [
        dict(kind="STANDARD",
             title_en="International Classification of Diseases, 11th Revision (ICD-11): Gaming Disorder",
             title_fa="طبقه‌بندی بین‌المللی بیماری‌ها، بازنگری یازدهم: اختلال بازی",
             authors="World Health Organization", year=2019,
             publisher="World Health Organization",
             doi=None,
             url="https://www.who.int/news-room/questions-and-answers/item/addictive-behaviours-gaming-disorder",
             language="en", isbn=None,
             citation="World Health Organization. (2019). International Classification of Diseases, 11th Revision (ICD-11): Gaming disorder. Geneva: WHO.",
             locator="6C51 Gaming disorder", locator_type="SECTION",
             supports="three core criteria and 12-month course for gaming disorder", verified=True),
        dict(kind="STANDARD",
             title_en="Diagnostic and Statistical Manual of Mental Disorders, Fifth Edition: Internet Gaming Disorder",
             title_fa="راهنمای تشخیصی و آماری اختلال‌های روانی، ویرایش پنجم: اختلال بازی اینترنتی",
             authors="American Psychiatric Association", year=2013,
             publisher="American Psychiatric Association",
             doi=None, url=None, language="en", isbn=None,
             citation="American Psychiatric Association. (2013). Diagnostic and Statistical Manual of Mental Disorders (5th ed.). Washington, DC: APA.",
             locator="Section III, Internet Gaming Disorder", locator_type="SECTION",
             supports="Internet gaming disorder as a condition for further study with nine criteria", verified=False),
    ],
}

ENRICH = {
    "MC-695": dict(
        year=1978,
        summary="چارچوب آینه در برابر برساخت، تقابلی نظری در مطالعات روزنامه‌نگاری است دربارهٔ نسبت خبر با واقعیت. در دیدگاه آینه، خبر بازتاب بی‌طرف رویدادهاست و وظیفهٔ روزنامه‌نگار کنار زدن پردهٔ پیش‌داوری و نمایش واقعیت آن‌گونه که هست تعریف می‌شود؛ این دیدگاه با هنجار عینیت و رویه‌های حرفه‌ای مانند استناد به منبع و تفکیک خبر از نظر گره خورده است. در دیدگاه برساخت، خبر نه بازتاب خام واقعیت، بلکه محصول رویه‌های حرفه‌ای، ساختار سازمانی و چارچوب‌های فرهنگی است: انتخاب رویداد، شبکهٔ خبری، نوعی‌سازی منابع و روایت‌های از پیش‌آماده، واقعیت خبری را می‌سازند. مایکل شادسون در کتاب سال ۱۹۷۸ نشان داد که آرمان عینیت خود محصول تاریخی و اجتماعی است و نه امری طبیعی؛ و گی تاچمن در همان سال با مفهوم آیین راهبردی عینیت توضیح داد که روزنامه‌نگاران چگونه با رویه‌هایی مانند نقل قول متوازن، ادعای بی‌طرفی را عملی می‌کنند. اهمیت این چارچوب در تحلیل سوگیری، منبع‌گزینی، چارچوب‌بندی و اعتبار خبر است. نقدهای اصلی به آن، دوگانه‌سازی افراطی دو دیدگاه، خطر لغزش برساخت‌گرایی به نسبیت و کم‌توجهی به تفاوت‌های فرهنگی در فهم عینیت مربوط می‌شود.",
        definition="چارچوب آینه در برابر برساخت، تقابلی نظری است که خبر را یا بازتاب بی‌طرف واقعیت یا برساختی برآمده از رویه‌های حرفه‌ای و فرهنگی می‌داند.",
        main_problem="آیا خبر می‌تواند واقعیت را بی‌واسطه بازتاب دهد، یا هر گزارش خبری ناگزیر از راه انتخاب، منبع‌گزینی و روایت، واقعیتی خبری می‌سازد؛ و اگر چنین است، ادعای عینیت چه معنایی دارد.",
        mechanism="روزنامه‌نگار از میان انبوه رویدادها با شبکهٔ خبری خود انتخاب می‌کند، منابع را بر پایهٔ اعتبار نهادی نوعی‌سازی می‌کند و رویداد را در قالب‌های از پیش‌آمادهٔ خبر می‌ریزد. در دیدگاه آینه، این رویه‌ها برای حذف سوگیری به کار می‌روند؛ در دیدگاه برساخت، همین رویه‌ها هستند که واقعیت خبری را شکل می‌دهند.",
        assumptions=[
            "خبر محصول کار نهادی و حرفه‌ای است و نه بازتاب خودکار واقعیت.",
            "انتخاب رویداد و منبع، بخشی اجتناب‌ناپذیر از تولید خبر است.",
            "هنجار عینیت، برساختهٔ تاریخی و اجتماعی است.",
            "رویه‌های حرفه‌ای می‌توانند ادعای بی‌طرفی را عملی کنند، بی‌آنکه آن را تضمین کنند.",
            "تحلیل خبر باید تولید، متن و دریافت را با هم ببیند.",
        ],
        principles=[
            "خبر را باید هم محصول و هم بازنمایی واقعیت دانست.",
            "هنجار عینیت تاریخ دارد و در بستر اجتماعی شکل گرفته است.",
            "شبکهٔ خبری و نوعی‌سازی منابع، واقعیت خبری را قالب می‌زنند.",
            "آیین‌های عینیت مانند نقل قول متوازن، ادعای بی‌طرفی را عملی می‌کنند.",
            "سوگیری را باید در سطح رویه و ساختار جست، نه فقط در نیت فردی.",
            "تحلیل خبر باید تفاوت میان بازتاب و برساخت را روشن نگه دارد.",
        ],
        critiques=[
            "دوگانهٔ آینه و برساخت بیش از اندازه تند و ساده‌ساز است.",
            "برساخت‌گرایی افراطی می‌تواند به نسبیت و انکار امکان صدق بیانجامد.",
            "تفاوت‌های فرهنگی در فهم عینیت کم‌بررسی می‌ماند.",
            "نقش مخاطب در پذیرش یا مقاومت برابر روایت خبری کم‌رنگ می‌شود.",
            "تحلیل ساختاری می‌تواند مسئولیت فردی روزنامه‌نگار را پنهان کند.",
        ],
        critique_text="منتقدان می‌گویند بیشتر پژوهش‌های خبری در عمل میان دو قطب می‌ایستند: خبر نه بازتاب محض است و نه برساخت دلبخواه؛ بلکه بازنمایی مقید به رویه، منبع و هنجار است. بنابراین چارچوب آینه و برساخت بیشتر دو آرمان‌نوع تحلیلی‌اند تا دو اردوگاه متضاد، و ارزش آنها در روشن‌کردن هزینه‌های هر ادعای بی‌طرفی است.",
        applications=[
            "تحلیل سوگیری و منبع‌گزینی در پوشش خبری.",
            "پژوهش چارچوب‌بندی و روایت در رسانه.",
            "آموزش اخلاق و رویه‌های حرفه‌ای روزنامه‌نگاری.",
            "ارزیابی ادعاهای عینیت در رسانه‌های عمومی و خصوصی.",
            "تحلیل پوشش خبری بحران‌ها و انتخابات.",
        ],
        example_text="وقتی دو رسانه یک اعتراض خیابانی را پوشش می‌دهند، یکی آن را «اعتراض شهروندان» و دیگری «ناآرامی» می‌نامد؛ هر دو مدعی گزارش واقعیت‌اند، اما انتخاب واژه، منبع و قالب روایت نشان می‌دهد که خبر در همان حال که رویداد را بازتاب می‌دهد، آن را می‌سازد. چارچوب آینه و برساخت این تنش را به پرسش تحلیلی تبدیل می‌کند.",
        evolution="هنجار عینیت از اوایل سدهٔ بیستم در روزنامه‌نگاری آمریکایی شکل گرفت و پس از دههٔ ۱۹۷۰ با پژوهش‌های تاریخی و برساخت‌گرایانه بازخوانی شد. شادسون و تاچمن در سال ۱۹۷۸ دو ستون این بازخوانی را گذاشتند و بعدها پژوهش چارچوب‌بندی و مطالعات تولید خبر آن را بسط دادند. در محیط دیجیتال، پرسش عینیت با خبر جعلی و رسانهٔ شهروندی ابعاد تازه‌ای یافته است.",
        key_concepts=["عینیت", "بازتاب واقعیت", "برساخت واقعیت", "شبکهٔ خبری", "نوعی‌سازی", "آیین راهبردی عینیت", "چارچوب‌بندی"],
        theorists="مایکل شادسون، مورخ اجتماعی خبر و عینیت؛ و گی تاچمن، پژوهشگر برساخت واقعیت خبری و آیین عینیت.",
        theorists_text="این چارچوب در سنت جامعه‌شناسی خبر و مطالعات حرفه‌ای روزنامه‌نگاری شکل گرفت و با پژوهش چارچوب‌بندی پیوند خورد.",
        model="مدل دو‌قطبی: قطب آینه، خبر را بازتاب واقعیت می‌بیند و رویه‌های حرفه‌ای را ابزار حذف سوگیری می‌داند؛ قطب برساخت، خبر را محصول انتخاب، منبع‌گزینی و روایت می‌داند؛ پژوهش واقعی میان این دو قطب و بر پایهٔ شواهد تولید خبر جای می‌گیرد.",
        studies=[
            "تاریخ اجتماعی شادسون نشان داد عینیت محصول تحول تاریخی روزنامه‌نگاری است.",
            "پژوهش تاچمن برساخت خبر و آیین عینیت را با مشاهدهٔ میدانی تحلیل کرد.",
            "مطالعات چارچوب‌بندی، سازوکارهای انتخاب و برجسته‌سازی خبر را بسط دادند.",
            "پژوهش خبر دیجیتال، پرسش عینیت را در محیط پلتفرم بازخوانی کرده است.",
        ],
    ),
    "MC-702": dict(
        year=2019,
        summary="روزنامه‌نگاری راه‌حل‌محور، رویکردی در گزارش‌دهی است که به همان اندازه که مشکل اجتماعی را روایت می‌کند، به پاسخ‌ها و راه‌حل‌های آزموده‌شده نیز می‌پردازد. گزارش راه‌حل‌محور باید چهار عنصر را روشن کند: چه کسی چه کاری انجام داده است، شواهد اثربخشی چیست، سازوکار و جزئیات اجرا چگونه است و محدودیت‌ها و ناکامی‌ها کدام‌اند. این رویکرد از گزارش مثبت و تبلیغی جدا است: ادعای موفقیت را با شواهد می‌سنجد و از کنشگری پرهیز می‌کند. ریشهٔ آن به نقد «اخبار بد» و خستگی مخاطب از روایت بحران در دههٔ ۲۰۰۰ بازمی‌گردد و با جنبش روزنامه‌نگاری سازنده پیوند دارد. کارن مک‌اینتایر در پژوهش سال ۲۰۱۹ نشان داد افزودن اطلاعات راه‌حل‌محور به گزارش‌های اجتماعی می‌تواند ادراک مخاطب از مسئله و نگرش او را تغییر دهد، هرچند این اثرها مشروط و نه یکسان است. در عمل، رسانه‌ها این چارچوب را برای پوشش فقر، سلامت، محیط زیست و سیاست عمومی به کار می‌برند. نقدهای اصلی به آن، خطر تبلیغ‌گرایی، تضعیف نقش ناظر، اتکا به داستان‌های موفقیت‌آمیز گزینشی، شواهد ناهمگون دربارهٔ اثر و خطر ابزاری‌شدن برای مدل‌های تجاری رسانه مربوط می‌شود.",
        definition="روزنامه‌نگاری راه‌حل‌محور، رویکردی در گزارش‌دهی است که پاسخ‌ها به مشکلات اجتماعی را با همان دقت و استانداردهای خبرنگاری سختگزارش می‌کند، بی‌آنکه به تبلیغ یا کنشگری بینجامد.",
        main_problem="پوشش خبری مداوم بحران و مشکل، مخاطب را به بی‌حسی و بی‌اعتمادی می‌کشاند؛ پرسش این است که چگونه می‌توان پاسخ‌ها و راه‌حل‌های آزموده‌شده را نیز پوشش داد بی‌آنکه استانداردهای خبری و استقلال حرفه‌ای آسیب ببیند.",
        mechanism="گزارش راه‌حل‌محور با پرسش دربارهٔ پاسخ‌های موجود آغاز می‌شود، شواهد اثربخشی را بررسی می‌کند، جزئیات اجرا و موانع را روایت می‌کند و محدودیت‌ها را پنهان نمی‌کند. این ساختار، امید را به شواهد گره می‌زند و از الگوی تبلیغاتی جدا می‌شود.",
        assumptions=[
            "مخاطبان به گزارش‌های بحران‌محور صرف، بی‌حس یا بی‌اعتماد می‌شوند.",
            "پاسخ‌ها و راه‌حل‌ها می‌توانند به‌اندازهٔ مشکلات ارزش خبری داشته باشند.",
            "اثربخشی راه‌حل را می‌توان با شواهد ارزیابی کرد.",
            "روزنامه‌نگار می‌تواند راه‌حل را گزارش کند بی‌آنکه به کنشگر تبدیل شود.",
            "محدودیت‌ها و ناکامی‌ها باید بخشی از گزارش باشند.",
        ],
        principles=[
            "گزارش راه‌حل باید بر پاسخ‌های واقعی و آزموده‌شده تمرکز کند.",
            "شواهد اثربخشی باید ارائه و ارزیابی شود.",
            "جزئیات اجرا و سازوکار پاسخ باید روشن باشد.",
            "محدودیت‌ها و ناکامی‌ها باید صریح گزارش شوند.",
            "از تبلیغ، کنشگری و داستان موفقیت گزینشی باید پرهیز کرد.",
            "استانداردهای خبرنگاری سخت بر گزارش راه‌حل نیز حاکم است.",
        ],
        critiques=[
            "خطر تبلیغ‌گرایی و تبدیل خبر به روابط عمومی وجود دارد.",
            "تمرکز بر راه‌حل می‌تواند نقش ناظر رسانه را تضعیف کند.",
            "گزینش داستان‌های موفق، تصویری نادرست از واقعیت می‌سازد.",
            "شواهد دربارهٔ اثرهای مخاطبی ناهمگون و محدود است.",
            "مدل می‌تواند به ابزار تجاری برای جلب توجه تبدیل شود.",
        ],
        critique_text="منتقدان می‌گویند «راه‌حل» در عمل می‌تواند به «تبلیغ» بلغزد، به‌ویژه وقتی رسانه به منبع مالی راه‌حل‌ها وابسته باشد. طرفداران پاسخ می‌دهند که استانداردهای شواهد، محدودیت‌ها و استقلال حرفه‌ای، مرز میان گزارش راه‌حل و تبلیغ را روشن می‌کند؛ با این حال، سنجش تجربی اثرها هنوز ناهمگون است.",
        applications=[
            "پوشش فقر، سلامت، محیط زیست و سیاست عمومی.",
            "طراحی تحریریه‌های تخصصی گزارش راه‌حل.",
            "آموزش روزنامه‌نگاران برای گزارش شواهد و محدودیت‌ها.",
            "ارزیابی اثر گزارش راه‌حل بر ادراک و اعتماد مخاطب.",
            "تحلیل پوشش رسانه در دوره‌های بحران و بازسازی.",
        ],
        example_text="در پوشش یک بحران آب، گزارش راه‌حل‌محور نه فقط کاهش ذخایر را روایت می‌کند، بلکه تجربهٔ شهرهایی را که مصرف را کاهش داده‌اند بررسی می‌کند، شواهد اثربخشی و هزینه را می‌سنجد و محدودیت‌های راه‌حل را بیان می‌کند؛ چنین گزارشی امید را به شواهد گره می‌زند و از تبلیغ یک سیاست خاص فاصله می‌گیرد.",
        evolution="این رویکرد در دههٔ ۲۰۰۰ در واکنش به خبر بد و بی‌حسی مخاطب شکل گرفت و در دههٔ ۲۰۱۰ با جنبش روزنامه‌نگاری سازنده و شبکه‌های آموزش روزنامه‌نگاران گسترش یافت. پژوهش تجربی دربارهٔ اثرهای آن از دههٔ ۲۰۱۰ آغاز شد و هنوز در حال بسط است.",
        key_concepts=["روزنامه‌نگاری راه‌حل‌محور", "روزنامه‌نگاری سازنده", "شواهد اثربخشی", "محدودیت راه‌حل", "خبر بد", "اعتماد مخاطب"],
        theorists="کارن مک‌اینتایر، پژوهشگر اثرهای روزنامه‌نگاری راه‌حل‌محور؛ و کاترین گیلدنستد، صورت‌بند روزنامه‌نگاری سازنده.",
        theorists_text="این رویکرد در تقاطع روزنامه‌نگاری، روان‌شناسی مثبت و نقد پوشش بحران شکل گرفت و با شبکه‌های آموزشی حرفه‌ای گسترش یافت.",
        model="مدل چهارعنصری: پاسخ چیست، شواهد اثربخشی چیست، چگونه اجرا شده است، و محدودیت‌ها کدام‌اند؛ گزارش معتبر باید هر چهار عنصر را با استانداردهای خبری پوشش دهد.",
        studies=[
            "پژوهش سال ۲۰۱۹ اثر افزودن اطلاعات راه‌حل را در گزارش‌های اجتماعی آزمود.",
            "مرورهای روزنامه‌نگاری سازنده، چارچوب نظری و اصول این رویکرد را تدوین کردند.",
            "پژوهش‌های تحریریه‌ای، پذیرش و مقاومت روزنامه‌نگاران را بررسی کردند.",
            "مطالعات اعتماد مخاطب، پیوند پوشش راه‌حل و اعتبار رسانه را سنجیدند.",
        ],
    ),
    "MC-706": dict(
        year=1963,
        summary="نظریهٔ یادگیری اجتماعی، رویکردی در روان‌شناسی است که می‌گوید انسان‌ها بخش بزرگی از رفتار را از راه مشاهدهٔ دیگران می‌آموزند، نه فقط از راه تقویت مستقیم. آلبرت بندورا و ریچارد والترز در کتاب سال ۱۹۶۳ با عنوان یادگیری اجتماعی و رشد شخصیت، نقش الگوگیری، تقویت جانشینی و فرایندهای شناختی را در یادگیری رفتار صورت‌بندی کردند. ایدهٔ کلیدی این است که فرد با مشاهدهٔ پیامد رفتار دیگران، رفتار را بدون تجربهٔ مستقیم می‌آموزد: توجه به الگو، نگهداری در حافظه، بازتولید حرکتی و انگیزه، چهار مرحلهٔ اصلی‌اند. پژوهش‌های بندورا دربارهٔ الگوگیری پرخاشگری از تلویزیون، این نظریه را به مطالعات رسانه پیوند داد و نشان داد نمایش رفتار در رسانه می‌تواند سرمشق یادگیری باشد. بعدها بندورا نظریهٔ شناختی-اجتماعی را با مفهوم خودکارآمدی بسط داد. امروزه نظریهٔ یادگیری اجتماعی برای تحلیل تأثیر اینفلوئنسرها، آموزش رسانه‌ای، کمپین‌های سلامت و یادگیری از ویدئوهای آموزشی به کار می‌رود. نقدهای اصلی به آن، مصنوعی‌بودن آزمایش‌های اولیه، نادیده‌گرفتن معناکاوی مخاطب، اثرهای ضعیف در محیط طبیعی و کم‌توجهی به عوامل ساختاری مربوط می‌شود.",
        definition="نظریهٔ یادگیری اجتماعی، نظریه‌ای است که یادگیری رفتار را نتیجهٔ مشاهدهٔ الگوها، تقویت جانشینی و فرایندهای شناختی می‌داند و نه صرفاً نتیجهٔ تقویت مستقیم.",
        main_problem="چگونه انسان‌ها رفتارهای تازه را بدون تجربهٔ مستقیم پاداش و تنبیه می‌آموزند، و رسانه چه نقشی در فراهم‌کردن الگوهای رفتاری دارد.",
        mechanism="فرد الگویی را می‌بیند، به آن توجه می‌کند، رفتار را در حافظه نگه می‌دارد، آن را بازتولید می‌کند و بر پایهٔ پیامدهای مشاهده‌شده یا انتظار پاداش، به تکرار آن انگیزه می‌یابد. تقویت جانشینی، یعنی دیدن پاداش یا تنبیه الگو، به‌جای تجربهٔ مستقیم عمل می‌کند.",
        assumptions=[
            "بخش بزرگی از یادگیری از راه مشاهده رخ می‌دهد.",
            "پیامدهای رفتار الگو بر یادگیری فرد اثر می‌گذارد.",
            "فرایندهای شناختی مانند توجه و حافظه در یادگیری نقش دارند.",
            "رسانه می‌تواند الگوهای رفتاری در دسترس قرار دهد.",
            "رفتار آموخته‌شده می‌تواند به موقعیت‌های تازه تعمیم یابد.",
        ],
        principles=[
            "یادگیری می‌تواند بدون تقویت مستقیم و از راه مشاهده رخ دهد.",
            "توجه، حافظه، بازتولید و انگیزه چهار مرحلهٔ یادگیری مشاهده‌ای‌اند.",
            "تقویت جانشینی، اثر پیامد رفتار الگو بر یادگیرنده است.",
            "الگوهای رسانه‌ای می‌توانند سرمشق رفتار باشند.",
            "خودکارآمدی، انگیزهٔ اجرای رفتار آموخته‌شده را تعیین می‌کند.",
            "یادگیری و عملکرد دو مرحلهٔ متمایزند.",
        ],
        critiques=[
            "آزمایش‌های اولیه در محیط مصنوعی انجام شدند.",
            "معناکاوی و تفسیر مخاطب از الگو کم‌بررسی می‌ماند.",
            "اثرهای مشاهده‌شده در محیط طبیعی ضعیف‌تر و مشروط‌ترند.",
            "عوامل ساختاری و فرهنگی در توضیح رفتار کم‌رنگ می‌شوند.",
            "تعمیم نتایج دربارهٔ پرخاشگری به همهٔ محتواهای رسانه‌ای دشوار است.",
        ],
        critique_text="منتقدان می‌گویند نظریهٔ یادگیری اجتماعی توضیح روشنی برای کسب رفتار ارائه می‌دهد اما در توضیح اینکه چه کسی چه الگویی را برمی‌گزیند و چگونه آن را تفسیر می‌کند، به پژوهش بیشتری نیاز دارد. با این حال، تأکید آن بر یادگیری مشاهده‌ای، بنیاد پژوهش رسانه دربارهٔ الگوگیری و آموزش رسانه‌ای شده است.",
        applications=[
            "تحلیل تأثیر اینفلوئنسرها و الگوهای رفتاری در شبکه‌های اجتماعی.",
            "طراحی کمپین‌های سلامت با الگوهای رفتاری مثبت.",
            "آموزش رسانه‌ای و سواد بصری برای کودکان و نوجوانان.",
            "پژوهش اثر نمایش پرخاشگری و رفتار اجتماعی در رسانه.",
            "طراحی آموزش مهارت‌های حرفه‌ای از راه ویدئو و نمایش عملی.",
        ],
        example_text="در یک کمپین سلامت، نمایش فردی هم‌سن و هم‌فرهنگ مخاطب که رفتار سالم را انجام می‌دهد و پیامد مثبت آن را تجربه می‌کند، بیش از پیام انتزاعی می‌تواند الگوی رفتار بسازد؛ این همان سازوکار یادگیری مشاهده‌ای و تقویت جانشینی است که نظریهٔ یادگیری اجتماعی توضیح می‌دهد.",
        evolution="نظریه در کتاب سال ۱۹۶۳ صورت‌بندی شد و در سال ۱۹۷۷ با کتاب مستقل یادگیری اجتماعی تثبیت شد. بندورا در سال ۱۹۸۶ با نظریهٔ شناختی-اجتماعی و مفهوم خودکارآمدی، نقش باورهای فردی را برجسته کرد. در مطالعات رسانه، این نظریه با پژوهش اثرهای تلویزیون و بعدها با تحلیل شبکه‌های اجتماعی پیوند یافت.",
        key_concepts=["یادگیری مشاهده‌ای", "الگوگیری", "تقویت جانشینی", "خودکارآمدی", "بازتولید حرکتی", "نظریهٔ شناختی-اجتماعی"],
        theorists="آلبرت بندورا، بنیان‌گذار نظریهٔ یادگیری اجتماعی و شناختی-اجتماعی؛ و ریچارد والترز، همکار او در صورت‌بندی اولیه.",
        theorists_text="این نظریه در سنت رفتارگرایی و روان‌شناسی یادگیری شکل گرفت و با افزودن فرایندهای شناختی از رفتارگرایی ساده فاصله گرفت.",
        model="مدل چهارمرحله‌ای: توجه به الگو، نگهداری در حافظه، بازتولید حرکتی و انگیزهٔ اجرا؛ پیامدهای مشاهده‌شدهٔ رفتار الگو و باور به خودکارآمدی، شدت یادگیری و اجرا را تعیین می‌کنند.",
        studies=[
            "کتاب سال ۱۹۶۳ یادگیری مشاهده‌ای و تقویت جانشینی را صورت‌بندی کرد.",
            "پژوهش‌های الگوگیری پرخاشگری، پیوند نظریه با محتوای تلویزیونی را نشان دادند.",
            "کتاب سال ۱۹۷۷، نظریه را در قالب مستقل و منسجم ارائه کرد.",
            "نظریهٔ شناختی-اجتماعی بعدی، خودکارآمدی را به هستهٔ توضیح افزود.",
        ],
    ),
    "MC-712": dict(
        year=2019,
        summary="اختلال بازی، تشخیصی است که سازمان جهانی بهداشت در یازدهمین بازنگری طبقه‌بندی بین‌المللی بیماری‌ها گنجانده و مجمع جهانی بهداشت در سال ۲۰۱۹ آن را پذیرفت. این اختلال الگویی از رفتار بازی پایدار یا تکرارشونده است که سه نشانهٔ اصلی دارد: ضعف در کنترل بر بازی، اولویت‌گرفتن بازی بر سایر علایق و فعالیت‌های روزانه تا حدی که بر زندگی چیره شود، و ادامه یا تشدید بازی با وجود پیامدهای منفی. برای تشخیص، الگو باید دست‌کم دوازده ماه ادامه یافته باشد و به آسیب چشمگیر در زندگی شخصی، خانوادگی، تحصیلی یا شغلی بیانجامد؛ در موارد شدید می‌توان دورهٔ کوتاه‌تری را پذیرفت. طبقه‌بندی، اختلال بازی را در گروه اختلال‌های ناشی از رفتارهای اعتیادی و در کنار قمار قرار می‌دهد. نسخهٔ پنجم راهنمای تشخیصی روان‌پزشکی در سال ۲۰۱۳ مفهوم اختلال بازی اینترنتی را به‌عنوان وضعیتی نیازمند پژوهش بیشتر معرفی کرده بود. این تشخیص جدال علمی و عمومی گسترده‌ای برانگیخت: برخی آن را گامی برای درمان و پوشش بیمه‌ای می‌دانند و برخی هشدار می‌دهند رفتار روزمرهٔ بخش بزرگی از بازیکنان به آسیب‌شناسی تبدیل شود. کاربرد آن در سیاست رسانه، طراحی پلتفرم، غربالگری سلامت روان و راهنمایی خانواده است. نقدهای اصلی به شیوع ناهمگون، مبنای شواهد محدود، خطر هراس اخلاقی، هم‌بودی با اختلال‌های دیگر و خطر توسل به تشخیص به‌جای توجه به شرایط زمینه‌ای مربوط می‌شود.",
        definition="اختلال بازی، الگویی از رفتار بازی پایدار یا تکرارشونده با ضعف کنترل، اولویت‌گرفتن بازی بر سایر فعالیت‌ها و ادامهٔ آن با وجود پیامدهای منفی است که به آسیب چشمگیر می‌انجامد.",
        main_problem="چه زمانی بازی، رفتار روزمره و سالم است و چه زمانی به اختلالی با آسیب چشمگیر تبدیل می‌شود، و معیارهای تشخیصی چگونه می‌توانند بی‌آنکه بخش بزرگی از بازیکنان را بیمار بخوانند، موارد نیازمند درمان را شناسایی کنند.",
        mechanism="طبقه‌بندی، سه نشانهٔ رفتاری و یک شرط زمانی و پیامد را کنار هم می‌گذارد: ضعف کنترل، اولویت‌یافتن بازی، ادامه با وجود پیامدهای منفی، تداوم معمولاً دوازده‌ماهه و آسیب چشمگیر. تشخیص بر الگوی رفتار متمرکز است و نه بر مقدار ساعات بازی، و به همین دلیل ادعای سادگی سنجش را رد می‌کند.",
        assumptions=[
            "رفتار بازی، مانند سایر رفتارهای اعتیادی، می‌تواند الگوی کنترل‌نشده پیدا کند.",
            "الگوی رفتار را می‌توان از ساعات بازی جدا کرد و سنجید.",
            "آسیب چشمگیر در کارکرد روزمره، شرط لازم تشخیص است.",
            "تداوم دوازده‌ماهه، معیار احتیاطی برای جلوگیری از تشخیص شتاب‌زده است.",
            "طبقه‌بندی تشخیصی می‌تواند به دسترسی به درمان کمک کند.",
        ],
        principles=[
            "تشخیص بر الگوی رفتار استوار است و نه بر مقدار زمان بازی.",
            "سه نشانهٔ اصلی باید هم‌زمان و پایدار باشند.",
            "آسیب چشمگیر در کارکرد، شرط لازم است.",
            "تداوم دوازده‌ماهه، معیار احتیاطی پیش‌فرض است.",
            "اختلال بازی در گروه رفتارهای اعتیادی و در کنار قمار قرار می‌گیرد.",
            "تشخیص باید به درمان و حمایت بیانجامد و نه برچسب‌زنی.",
        ],
        critiques=[
            "برآورد شیوع بسیار ناهمگون است.",
            "مبنای شواهد برای اعتبار تشخیص هنوز محدود است.",
            "خطر هراس اخلاقی و آسیب‌شناسی‌کردن رفتار عادی وجود دارد.",
            "هم‌بودی با اضطراب و افسردگی، مرز تشخیص را مبهم می‌کند.",
            "تمرکز بر تشخیص می‌تواند شرایط زمینه‌ای و طراحی بازی را کم‌رنگ کند.",
        ],
        critique_text="منتقدان می‌گویند گنجاندن اختلال بازی در طبقه‌بندی رسمی، در حالی که شواهد شیوع و مرزهای آن هنوز ناپایدار است، می‌تواند به برچسب‌زنی و تجاری‌شدن درمان بیانجامد. طرفداران پاسخ می‌دهند که معیارهای سخت‌گیرانه مانند آسیب چشمگیر و تداوم دوازده‌ماهه، از تشخیص شتاب‌زده جلوگیری می‌کند و وجود تشخیص، دسترسی به درمان را ممکن می‌سازد.",
        applications=[
            "غربالگری سلامت روان و ارجاع به درمان.",
            "سیاست‌گذاری رسانه و بازی‌های دیجیتال.",
            "طراحی مسئولانهٔ بازی و سازوکارهای اعتیادآور.",
            "راهنمایی خانواده و آموزش سواد بازی.",
            "پژوهش همه‌گیرشناسی دربارهٔ رفتار بازی و آسیب.",
        ],
        example_text="نوجوانی که ساعت‌های طولانی بازی می‌کند اما تحصیل، خواب و روابطش را حفظ کرده است، بر پایهٔ معیارها به اختلال بازی تشخیص داده نمی‌شود؛ در مقابل، فردی که کنترل بازی را از دست داده، آن را بر خواب و مدرسه مقدم کرده و با وجود افت تحصیلی ادامه می‌دهد، ممکن است معیارها را برآورده کند. همین تفکیک، کاربرد اصلی چارچوب است.",
        evolution="نسخهٔ پنجم راهنمای تشخیصی روان‌پزشکی در سال ۲۰۱۳ اختلال بازی اینترنتی را به‌عنوان وضعیت نیازمند پژوهش معرفی کرد و سازمان جهانی بهداشت در سال ۲۰۱۹ اختلال بازی را در طبقه‌بندی یازدهم رسمیت داد. پژوهش‌های بعدی بر سنجش شیوع، ابزارهای غربالگری و مرز تشخیص با رفتار عادی متمرکز شده‌اند.",
        key_concepts=["اختلال بازی", "کنترل بازی", "آسیب چشمگیر", "تداوم دوازده‌ماهه", "رفتار اعتیادی", "هم‌بودی"],
        theorists="سازمان جهانی بهداشت، تدوین‌کنندهٔ طبقه‌بندی یازدهم؛ و انجمن روان‌پزشکی آمریکا، معرفی‌کنندهٔ اختلال بازی اینترنتی در راهنمای تشخیصی.",
        theorists_text="این تشخیص در سنت طبقه‌بندی اختلال‌های اعتیادی و پژوهش سلامت روان دیجیتال شکل گرفت و با نقدهای رسانه‌ای و عمومی گسترده روبه‌رو شد.",
        model="مدل سه‌نشانه‌ای با شرط پیامد: ضعف کنترل، اولویت‌یافتن بازی و ادامه با وجود پیامدهای منفی، به‌همراه تداوم دوازده‌ماهه و آسیب چشمگیر؛ تشخیص بر الگوی رفتار استوار است و نه بر مدت زمان بازی.",
        studies=[
            "طبقه‌بندی یازدهم سازمان جهانی بهداشت، معیارهای اختلال بازی را رسمیت داد.",
            "راهنمای تشخیصی پنجم، اختلال بازی اینترنتی را برای پژوهش بیشتر معرفی کرد.",
            "پژوهش‌های همه‌گیرشناسی، برآوردهای بسیار متفاوتی از شیوع ارائه کردند.",
            "مطالعات بالینی، هم‌بودی با اضطراب و افسردگی را بررسی کردند.",
        ],
    ),
}

NAME_FIX = {
    "MC-695": ("چارچوب آینه در برابر برساخت (خبر: بازتاب یا ساخت)",
               "Mirror/Reflection vs. Construction Framework",
               "name normalized for readability; slash removed"),
    "MC-712": ("اختلال بازی (طبقه‌بندی یازدهم)", "Gaming Disorder (ICD-11)",
               "name aligned with ICD-11 terminology; 'internet gaming disorder' is the DSM-5 label"),
}

YEAR_FIX = {
    "MC-695": "year filled: none -> 1978 (Schudson, Discovering the News; Tuchman, Making News); note: editorial card core_logic was a mismatched professionalization template and its theorist attribution was unclear, documentation rebuilt from Schudson (1978) and Tuchman (1978)",
    "MC-702": "year filled: none -> 2019 (verified anchor: McIntyre, Solutions Journalism, Journalism Practice 13(1)); note: editorial card theorist entry 'بنش' was unverifiable and documentation rebuilt from verified literature",
    "MC-706": "no year change; note: editorial card core_logic was a mismatched game-culture template, documentation rebuilt from Bandura & Walters (1963)",
    "MC-712": "no year change; note: editorial card core_logic was a mismatched game-culture template, documentation rebuilt from WHO ICD-11 (2019) and DSM-5 (2013)",
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
                                       "verified": n_verified, "batch": 127}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH127 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
