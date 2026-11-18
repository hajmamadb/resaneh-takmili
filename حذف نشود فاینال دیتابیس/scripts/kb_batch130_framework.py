# -*- coding: utf-8 -*-
"""Batch 130 (MODEL): full documentation for MC-029, MC-034, MC-040, MC-062."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch130-model-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch130_model.json"

S = {
    "MC-029": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Role of Transportation in the Persuasiveness of Public Narratives",
             title_fa="نقش انتقال در اقناع‌گری روایت‌های عمومی",
             authors="Green, M. C.; Brock, T. C.", year=2000,
             publisher="Journal of Personality and Social Psychology",
             doi="10.1037/0022-3514.79.5.701",
             url="https://pubmed.ncbi.nlm.nih.gov/11079236/",
             language="en", isbn=None,
             citation="Green, M. C., & Brock, T. C. (2000). The role of transportation in the persuasiveness of public narratives. Journal of Personality and Social Psychology, 79(5), 701-721.",
             locator="79(5):701-721", locator_type="page_range",
             supports="transportation into narrative reduces counterarguing and shifts beliefs", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Entertainment-Education and Elaboration Likelihood: Understanding the Processing of Narrative Persuasion",
             title_fa="سرگرمی-آموزش و احتمال بسط: فهم پردازش اقناع روایی",
             authors="Slater, M. D.; Rouner, D.", year=2002,
             publisher="Communication Theory",
             doi=None, url=None, language="en", isbn=None,
             citation="Slater, M. D., & Rouner, D. (2002). Entertainment-education and elaboration likelihood: Understanding the processing of narrative persuasion. Communication Theory, 12(2), 173-191.",
             locator="12(2):173-191", locator_type="page_range",
             supports="extended elaboration likelihood model for narrative persuasion", verified=False),
    ],
    "MC-034": [
        dict(kind="BOOK",
             title_en="Media Economics: Concepts and Issues",
             title_fa="اقتصاد رسانه: مفاهیم و مسائل",
             authors="Picard, R. G.", year=1989,
             publisher="Sage Publications",
             doi=None,
             url="https://books.google.com/books/about/Media_Economics.html?id=5JwcAQAAIAAJ",
             language="en", isbn="9780803935020",
             citation="Picard, R. G. (1989). Media Economics: Concepts and Issues. Newbury Park, CA: Sage Publications.",
             locator="book", locator_type="SECTION",
             supports="systematic treatment of media markets and revenue sources", verified=True),
        dict(kind="BOOK",
             title_en="Media Economics: Understanding Markets, Industries and Concepts",
             title_fa="اقتصاد رسانه: فهم بازارها، صنایع و مفاهیم",
             authors="Albarran, A. B.", year=1996,
             publisher="Iowa State University Press",
             doi=None, url=None, language="en", isbn=None,
             citation="Albarran, A. B. (1996). Media Economics: Understanding Markets, Industries and Concepts. Ames: Iowa State University Press.",
             locator="book", locator_type="SECTION",
             supports="industry-level analysis of media markets and revenue structures", verified=False),
    ],
    "MC-040": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Twilight or New Dawn of Journalism? Evidence from the Changing News Ecosystem",
             title_fa="گرگ‌ومیش یا سپیدهٔ تازهٔ روزنامه‌نگاری؟ شواهدی از زیست‌بوم خبری در حال تغییر",
             authors="Picard, R. G.", year=2014,
             publisher="Digital Journalism",
             doi="10.1080/1461670X.2014.895530",
             url="https://www.tandfonline.com/doi/full/10.1080/1461670X.2014.895530",
             language="en", isbn=None,
             citation="Picard, R. G. (2014). Twilight or new dawn of journalism? Evidence from the changing news ecosystem. Digital Journalism, 2(3), 273-283.",
             locator="2(3)", locator_type="page_range",
             supports="analysis of declining news revenue and the journalism business-model crisis", verified=True),
        dict(kind="BOOK",
             title_en="Local Journalism: The Decline of Newspapers and the Rise of Digital Media",
             title_fa="روزنامه‌نگاری محلی: افول روزنامه‌ها و ظهور رسانهٔ دیجیتال",
             authors="Nielsen, R. K. (ed.)", year=2015,
             publisher="I.B. Tauris",
             doi=None, url=None, language="en", isbn=None,
             citation="Nielsen, R. K. (Ed.). (2015). Local Journalism: The Decline of Newspapers and the Rise of Digital Media. London: I.B. Tauris.",
             locator="book", locator_type="SECTION",
             supports="empirical evidence on local news decline across countries", verified=False),
    ],
    "MC-062": [
        dict(kind="BOOK",
             title_en="Competitive Strategy: Techniques for Analyzing Industries and Competitors",
             title_fa="راهبرد رقابتی: فنون تحلیل صنایع و رقبا",
             authors="Porter, M. E.", year=1980,
             publisher="Free Press",
             doi=None,
             url="https://www.hbs.edu/faculty/Pages/item.aspx?num=195",
             language="en", isbn=None,
             citation="Porter, M. E. (1980). Competitive Strategy: Techniques for Analyzing Industries and Competitors. New York: Free Press.",
             locator="book", locator_type="SECTION",
             supports="five competitive forces framework", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Five Competitive Forces That Shape Strategy",
             title_fa="پنج نیروی رقابتی که راهبرد را شکل می‌دهند",
             authors="Porter, M. E.", year=2008,
             publisher="Harvard Business Review",
             doi=None,
             url="https://hbr.org/2008/01/the-five-competitive-forces-that-shape-strategy",
             language="en", isbn=None,
             citation="Porter, M. E. (2008). The five competitive forces that shape strategy. Harvard Business Review, 86(1), 78-93.",
             locator="86(1):78-93", locator_type="page_range",
             supports="restatement and updating of the five-forces framework", verified=True),
    ],
}

ENRICH = {
    "MC-029": dict(
        year=2000,
        summary="انتقال روایی، مدلی در پژوهش اقناع روایی است که ملانی گرین و تیموتی براک در سال ۲۰۰۰ با مطالعهٔ تجربی دربارهٔ اثر داستان‌ها بر باورها معرفی کردند و بعدتر در قالب مدل بسط‌یافتهٔ احتمال بسط برای روایت بسط یافت. ادعای مرکزی این است که وقتی مخاطب «در روایت منتقل می‌شود» — یعنی از نظر شناختی، عاطفی و تخیلی در جهان داستان غرق می‌شود — جریان پردازش انتقادی و ضداستدلال کاهش می‌یابد و باورهای او با جهان داستان همسو می‌شود. انتقال سه مؤلفهٔ اصلی دارد: تصویرسازی ذهنی، درگیری عاطفی و توجه متمرکز؛ و هرچه انتقال بیشتر باشد، اثر اقناعی داستان بر باورها بیشتر است، حتی وقتی مخاطب می‌داند داستان ساختگی است. نسخهٔ بسط‌یافتهٔ مدل، انتقال را مسیری مکمل مسیرهای مرکزی و پیرامونی مدل احتمال بسط می‌داند که در آن هم‌ذات‌پنداری با شخصیت‌ها و درگیری با خط داستان جای بررسی استدلال‌ها را می‌گیرد. این مدل در تحلیل سریال‌های سرگرمی-آموزشی، تبلیغات داستانی، پادکست و کمپین‌های سلامت به کار می‌رود. نقدهای اصلی به آن، دشواری سنجش انتقال، مرز مبهم با هم‌ذات‌پنداری و درگیری روایی، و محدودبودن شواهد دربارهٔ اثرهای بلندمدت مربوط می‌شود.",
        definition="انتقال روایی، وضعیتی است که در آن مخاطب از نظر شناختی و عاطفی در جهان داستان غرق می‌شود و در نتیجه مقاومت و ضداستدلال او کاهش می‌یابد و باورهایش با محتوای روایت همسو می‌شود.",
        main_problem="چگونه داستان‌ها می‌توانند بدون استدلال صریح و حتی با آگاهی مخاطب از ساختگی‌بودن، باورها و نگرش‌های او را تغییر دهند.",
        mechanism="مخاطب با تصویرسازی، عاطفه و توجه متمرکز در جهان داستان غرق می‌شود؛ این غرق‌شدگی ظرفیت پردازش انتقادی و تولید ضداستدلال را کم می‌کند و در نتیجه پیام‌های نهفته در داستان با مقاومت کمتری پذیرفته می‌شوند. هم‌ذات‌پنداری با شخصیت و درگیری با خط داستان، انتقال را تقویت می‌کند.",
        assumptions=[
            "مخاطب می‌تواند در جهان داستان از نظر شناختی و عاطفی غرق شود.",
            "انتقال، پردازش انتقادی و ضداستدلال را کاهش می‌دهد.",
            "اثر اقناعی داستان با میزان انتقال رابطهٔ مثبت دارد.",
            "باورهای همسو با داستان پس از انتقال تقویت می‌شوند.",
            "داستان می‌تواند حتی با آگاهی از ساختگی‌بودن اثر بگذارد.",
        ],
        principles=[
            "انتقال از تصویرسازی، عاطفه و توجه متمرکز ساخته می‌شود.",
            "انتقال بیشتر، مقاومت کمتر در برابر پیام داستان.",
            "هم‌ذات‌پنداری با شخصیت، مسیر مهمی برای اثرگذاری است.",
            "روایت مسیری مکمل و نه جانشین پردازش استدلالی است.",
            "طراحی داستان باید درگیری عاطفی و تصویری ایجاد کند.",
            "اثر انتقال را باید جدا از درگیری و لذت سنجید.",
        ],
        critiques=[
            "سنجش انتقال عمدتاً بر خودگزارشی تکیه دارد.",
            "مرز انتقال با هم‌ذات‌پنداری و درگیری روایی مبهم است.",
            "شواهد دربارهٔ پایداری بلندمدت اثرها محدود است.",
            "نقش تفاوت‌های فردی و فرهنگی کم‌بررسی مانده است.",
            "تعمیم نتایج آزمایشگاهی به رسانهٔ واقعی دشوار است.",
        ],
        critique_text="منتقدان می‌گویند انتقال روایی چارچوبی روشن برای توضیح اقناع غیراستدلالی فراهم کرد اما سنجش آن بیشتر به خودگزارشی وابسته است و مرز آن با مفاهیم همسایه روشن نیست. با این حال، پژوهش سرگرمی-آموزشی و تبلیغات داستانی به‌طور گسترده از آن استفاده می‌کند.",
        applications=[
            "طراحی سریال و برنامهٔ سرگرمی-آموزشی برای تغییر نگرش.",
            "کمپین‌های سلامت با روایت شخصی و شهادت داستانی.",
            "تحلیل تبلیغات داستانی و برند‌استوری‌تلینگ.",
            "پژوهش اثر پادکست و روایت صوتی بر باور مخاطب.",
            "طراحی پیام علیه اطلاعات نادرست با روایت جایگزین.",
        ],
        example_text="در یک سریال دربارهٔ بیماری روانی، مخاطب با شخصیت اصلی هم‌ذات‌پنداری می‌کند و در طول فصل در جهان او غرق می‌شود؛ پس از پایان، نگرش او نسبت به جست‌وجوی کمک درمانی مثبت‌تر می‌شود، هرچند هیچ استدلال صریحی در سریال ارائه نشده است. مدل انتقال روایی این تغییر را توضیح می‌دهد.",
        evolution="مقالهٔ سال ۲۰۰۰ مفهوم انتقال و مقیاس سنجش آن را تثبیت کرد. پژوهش‌های بعدی مدل را به سرگرمی-آموزشی، سلامت و سیاست گستردند و نسخهٔ بسط‌یافتهٔ آن، انتقال را به مدل احتمال بسط پیوند داد.",
        key_concepts=["انتقال روایی", "غرق‌شدگی", "هم‌ذات‌پنداری", "ضداستدلال", "تصویرسازی ذهنی", "درگیری عاطفی"],
        theorists="ملانی گرین و تیموتی براک، صورت‌بندان انتقال روایی؛ و پژوهشگرانی که مدل بسط‌یافتهٔ آن را برای روایت ارائه کردند.",
        theorists_text="این مدل در سنت روان‌شناسی اقناع و پژوهش سرگرمی-آموزشی شکل گرفت و با مدل احتمال بسط پیوند خورد.",
        model="مدل انتقال: مؤلفه‌های تصویرسازی، عاطفه و توجه، میزان انتقال را می‌سازند؛ انتقال بالا ضداستدلال را کم و همسویی باور با داستان را زیاد می‌کند. مدل بسط‌یافته، انتقال را مسیر سوم اقناع در کنار مسیرهای مرکزی و پیرامونی می‌بیند.",
        studies=[
            "مقالهٔ سال ۲۰۰۰ اثر انتقال بر باورهای همسو با داستان را آزمود.",
            "پژوهش‌های سرگرمی-آموزشی، انتقال را در برنامه‌های سلامت سنجیدند.",
            "مدل بسط‌یافته، انتقال را به چارچوب احتمال بسط پیوند داد.",
            "مطالعات رسانهٔ دیجیتال، انتقال را در پادکست و ویدئوی کوتاه آزمودند.",
        ],
    ),
    "MC-034": dict(
        year=1989,
        summary="مدل‌های درآمدی رسانه، چارچوبی در اقتصاد رسانه است که رابرت پیکارد در سال ۱۹۸۹ در کتاب اقتصاد رسانه: مفاهیم و مسائل آن را نظام‌مند کرد. ادعای مرکزی این است که رسانه‌ها از چند منبع درآمدی اصلی تأمین می‌شوند: تبلیغات، که در آن مخاطب کالای فروخته‌شده به آگهی‌دهنده است؛ اشتراک و پرداخت مستقیم، که در آن مخاطب بهای دسترسی یا محتوا را می‌پردازد؛ یارانه و بودجهٔ عمومی یا حمایت نهادی؛ و درآمدهای ترکیبی و جانبی مانند رویدادها، حق نشر و تجارت الکترونیک. انتخاب ترکیب درآمدی بر ساختار محتوا، رابطه با مخاطب، وابستگی به آگهی‌دهنده و استقلال تحریریه اثر می‌گذارد. رسانه‌های وابسته به تبلیغات به شمار و ترکیب مخاطب حساس‌اند، در حالی که رسانه‌های اشتراکی به رضایت و وفاداری مخاطب وابسته‌اند. این چارچوب پایهٔ تحلیل بازار رسانه، سیاست‌گذاری حمایت از رسانه و پژوهش مدل کسب‌وکار شد. نقدهای اصلی به آن، ساده‌سازی بیش از اندازهٔ پیچیدگی بازارهای دوطرفه، کم‌توجهی به اقتصاد پلتفرم و نیاز به بازنگری در عصر دیجیتال مربوط می‌شود.",
        definition="مدل‌های درآمدی رسانه، چارچوبی است که منابع اصلی تأمین مالی رسانه، یعنی تبلیغات، اشتراک و پرداخت مستقیم، یارانه و درآمدهای ترکیبی، را از هم تفکیک می‌کند و اثر هرکدام را بر محتوا و استقلال تحریریه می‌سنجد.",
        main_problem="رسانه‌ها چگونه هزینهٔ تولید محتوا را تأمین می‌کنند، و انتخاب هر منبع درآمدی چه پیامدهایی برای محتوا، مخاطب و استقلال تحریریه دارد.",
        mechanism="رسانه با ترکیب منابع درآمدی، ریسک مالی را تقسیم می‌کند؛ هر منبع، مشوق‌های متفاوتی ایجاد می‌کند. درآمد تبلیغاتی شمار و ویژگی مخاطب را پاداش می‌دهد، درآمد اشتراکی رضایت و وفاداری را، و یارانه عمومی خدمت عمومی را؛ بنابراین ترکیب درآمدی، ساختار محتوا و رابطه با مخاطب را قالب می‌زند.",
        assumptions=[
            "رسانه‌ها بنگاه‌های اقتصادی با هزینهٔ تولید بالا هستند.",
            "منابع درآمدی متفاوت، مشوق‌های متفاوتی ایجاد می‌کنند.",
            "استقلال تحریریه با ساختار درآمدی رابطه دارد.",
            "بازار رسانه اغلب دوطرفه است: مخاطب و آگهی‌دهنده.",
            "ترکیب درآمدی بر ریسک و پایداری سازمان اثر می‌گذارد.",
        ],
        principles=[
            "منابع درآمدی را باید از هم تفکیک و ترکیبشان را تحلیل کرد.",
            "درآمد تبلیغاتی، مخاطب را به کالا تبدیل می‌کند.",
            "درآمد اشتراکی، کیفیت و وفاداری را پاداش می‌دهد.",
            "یارانه و حمایت عمومی، خدمت عمومی را پشتیبانی می‌کند.",
            "تنوع درآمدی، وابستگی و ریسک را کاهش می‌دهد.",
            "مدل درآمدی، پیامد تحریریه‌ای و اخلاقی دارد.",
        ],
        critiques=[
            "بازارهای دوطرفه و پلتفرمی پیچیده‌تر از چهارگانهٔ کلاسیک‌اند.",
            "اقتصاد پلتفرم و داده، منطق درآمدی را دگرگون کرده است.",
            "اثر مدل درآمدی بر محتوا به‌طور تجربی یکدست نیست.",
            "نقش سرمایه‌گذاری خطرپذیر و مالکیت خصوصی کم‌بررسی می‌ماند.",
            "مقایسهٔ بین‌کشوری به دلیل تفاوت نظام‌های حمایتی دشوار است.",
        ],
        critique_text="منتقدان می‌گویند چارچوب کلاسیک درآمدی رسانه برای تحلیل روزنامه و پخش مناسب بود اما اقتصاد پلتفرمی، درآمد داده‌محور و مدل‌های ترکیبی دیجیتال را به‌درستی پوشش نمی‌دهد. با این حال، تفکیک منابع درآمدی همچنان ابزار پایهٔ تحلیل اقتصاد رسانه است.",
        applications=[
            "تحلیل پایداری مالی رسانه‌های خبری.",
            "طراحی مدل اشتراک و دیوار پرداخت.",
            "سیاست‌گذاری حمایت عمومی از رسانه.",
            "مقایسهٔ استقلال تحریریه در رسانه‌های تبلیغاتی و اشتراکی.",
            "آموزش مدیریت رسانه و تحلیل بازار.",
        ],
        example_text="دو روزنامه با شمار مخاطب یکسان می‌توانند سرنوشت تحریریه‌ای متفاوت داشته باشند: یکی که به آگهی‌دهندهٔ بزرگ وابسته است ممکن است در پوشش انتقادی محتاط باشد، در حالی که دیگری با درآمد اشتراکی به رضایت خواننده و کیفیت محتوا وابسته است. چارچوب مدل‌های درآمدی این تفاوت را توضیح می‌دهد.",
        evolution="کتاب سال ۱۹۸۹ مفاهیم پایهٔ اقتصاد رسانه را تثبیت کرد و پژوهش‌های دههٔ ۱۹۹۰ با تحلیل صنعتی بسط یافت. از دههٔ ۲۰۰۰، مدل‌های دیجیتال، اشتراک دیجیتال و درآمد پلتفرمی، بازنگری چارچوب را ضروری کردند.",
        key_concepts=["درآمد تبلیغاتی", "اشتراک", "پرداخت مستقیم", "یارانه", "بازار دوطرفه", "استقلال تحریریه", "تنوع درآمدی"],
        theorists="رابرت پیکارد و آلن آلباران، صورت‌بندانان اقتصاد رسانه و مدل‌های درآمدی.",
        theorists_text="این چارچوب در سنت اقتصاد صنعتی و مدیریت رسانه شکل گرفت و با سیاست‌گذاری رسانه پیوند خورد.",
        model="مدل چهارمنبعی: تبلیغات، اشتراک/پرداخت مستقیم، یارانه/عمومی و درآمدهای ترکیبی؛ ترکیب این منابع، ساختار محتوا، رابطه با مخاطب و استقلال تحریریه را تعیین می‌کند.",
        studies=[
            "کتاب سال ۱۹۸۹ مفاهیم و منابع درآمدی را نظام‌مند کرد.",
            "پژوهش‌های صنعتی، ساختار درآمدی رسانه‌های مختلف را مقایسه کردند.",
            "مطالعات دیجیتال، گذار به اشتراک و درآمد پلتفرمی را بررسی کردند.",
            "پژوهش‌های سیاست رسانه، اثر یارانه بر تنوع محتوا را سنجیدند.",
        ],
    ),
    "MC-040": dict(
        year=2014,
        summary="اقتصاد خبر و بحران مدل کسب‌وکار روزنامه‌نگاری، حوزه‌ای در اقتصاد رسانه است که رابرت پیکارد در مقالهٔ سال ۲۰۱۴ دربارهٔ زیست‌بوم خبری در حال تغییر آن را صورت‌بندی کرد. ادعای مرکزی این است که مدل کسب‌وکار سنتی خبر، یعنی ترکیب درآمد تبلیغاتی و فروش نسخه، با انتقال آگهی‌های طبقه‌بندی‌شده و تبلیغات هدفمند به پلتفرم‌های دیجیتال فروپاشید. پلتفرم‌ها با داده و هدف‌گیری دقیق، آگهی‌دهندگان را جذب کردند و درآمد تبلیغاتی را از ناشران خبری بیرون کشیدند؛ نتیجه، کاهش بودجهٔ تحریریه، کوچک‌شدن ساختار خبری و به‌ویژه افول خبر محلی و ظهور «بیابان خبری» در بسیاری از مناطق بود. پاسخ ناشران، ترکیبی از دیوار پرداخت، عضویت، رویداد، خدمات تجاری، حمایت بشردوستانه و کمک عمومی بوده است که هیچ‌کدام به‌تنهایی جایگزین کامل درآمد گذشته نشده‌اند. این حوزه، چارچوب تحلیل سیاست حمایت از خبر، نوآوری مدل کسب‌وکار و رابطهٔ خبر با پلتفرم را فراهم کرد. نقدهای اصلی به آن، ساده‌سازی بیش از اندازهٔ روایت افول، کم‌توجهی به نوآوری‌های موفق و تمرکز بیش از اندازه بر بازار آمریکا و اروپا مربوط می‌شود.",
        definition="اقتصاد خبر، مطالعهٔ ساختار هزینه و درآمد تولید خبر است؛ بحران مدل کسب‌وکار روزنامه‌نگاری به فروپاشی ترکیب سنتی درآمد تبلیغاتی و فروش نسخه و جابه‌جایی آن به پلتفرم‌های دیجیتال اشاره دارد.",
        main_problem="چرا مدل کسب‌وکار سنتی خبر دیگر هزینهٔ تولید روزنامه‌نگاری باکیفیت را پوشش نمی‌دهد، و چه ترکیبی از منابع درآمدی می‌تواند پایداری خبر را تأمین کند.",
        mechanism="آگهی‌دهندگان با هدف‌گیری دقیق‌تر و هزینهٔ کمتر به پلتفرم‌ها مهاجرت می‌کنند؛ درآمد ناشران کاهش می‌یابد و بودجهٔ تحریریه کوچک می‌شود. کاهش پوشش، به‌ویژه خبر محلی، تقاضای عمومی برای خبر را نیز تضعیف می‌کند و چرخهٔ افول را تشدید می‌کند.",
        assumptions=[
            "تولید خبر باکیفیت هزینهٔ ثابت و بالایی دارد.",
            "آگهی‌دهنده به هدف‌گیری دقیق و بازده سرمایه‌گذاری حساس است.",
            "پلتفرم‌های دیجیتال مزیت داده و مقیاس دارند.",
            "کاهش بودجهٔ تحریریه کیفیت و کمیت خبر را کم می‌کند.",
            "خبر عمومی کالایی با منفعت اجتماعی فراتر از مصرف فردی است.",
        ],
        principles=[
            "درآمد تبلیغاتی خبر به پلتفرم‌ها منتقل شده است.",
            "دیوار پرداخت و عضویت، جایگزین جزئی و نه کامل درآمدند.",
            "خبر محلی بیشترین آسیب را از بحران مدل کسب‌وکار دیده است.",
            "حمایت بشردوستانه و عمومی، بخشی از راه‌حل پایداری است.",
            "مدل کسب‌وکار باید با مأموریت عمومی خبر هم‌خوان باشد.",
            "بحران خبر، مسئلهٔ سیاست عمومی و نه فقط بازار است.",
        ],
        critiques=[
            "روایت افول، نوآوری‌های موفق خبری را کم‌رنگ می‌کند.",
            "تمرکز بر بازارهای غربی، تعمیم را محدود می‌کند.",
            "اثر دیوار پرداخت بر تنوع مخاطب یکدست نیست.",
            "رابطهٔ خبر با پلتفرم بیش از اندازه ساده‌سازی می‌شود.",
            "سنجش «بیابان خبری» به تعریف‌های متفاوت وابسته است.",
        ],
        critique_text="منتقدان می‌گویند روایت بحران مدل کسب‌وکار خبر به‌درستی فشار ساختاری را نشان می‌دهد اما بعضاً تنوع پاسخ‌های نوآورانه و تفاوت‌های منطقه‌ای را نادیده می‌گیرد. با این حال، این چارچوب به یکی از محورهای اصلی سیاست رسانه و پژوهش پایداری خبر تبدیل شده است.",
        applications=[
            "تحلیل پایداری رسانه‌های خبری و طراحی مدل درآمدی.",
            "سیاست‌گذاری حمایت از خبر محلی و عمومی.",
            "پژوهش رابطهٔ خبر و پلتفرم‌های دیجیتال.",
            "طراحی دیوار پرداخت و راهبرد عضویت.",
            "آموزش روزنامه‌نگاری و مدیریت رسانه.",
        ],
        example_text="یک روزنامهٔ محلی که درآمد خود را از آگهی‌های طبقه‌بندی‌شده و تبلیغات محلی می‌گرفت، با انتقال آگهی‌ها به پلتفرم‌ها بخش بزرگی از درآمدش را از دست می‌دهد و ناچار به کاهش تحریریه می‌شود؛ نتیجه، کاهش پوشش شورای شهر و افزایش فاصلهٔ شهروندان از خبر محلی است. چارچوب اقتصاد خبر این زنجیره را توضیح می‌دهد.",
        evolution="ریشهٔ این حوزه در اقتصاد رسانهٔ دههٔ ۱۹۸۰ است. مقالهٔ سال ۲۰۱۴ چارچوب بحران را تثبیت کرد و پژوهش‌های دههٔ ۲۰۱۰ و ۲۰۲۰ با داده‌های بحران خبر محلی، دیوار پرداخت و حمایت بشردوستانه آن را بسط دادند.",
        key_concepts=["مدل کسب‌وکار خبر", "درآمد تبلیغاتی", "دیوار پرداخت", "بیابان خبری", "خبر محلی", "حمایت بشردوستانه"],
        theorists="رابرت پیکارد، راسموس کلایس نیلسن و پنه‌لوپه ابرناتی، پژوهشگران اقتصاد و بحران خبر.",
        theorists_text="این حوزه در سنت اقتصاد رسانه و پژوهش روزنامه‌نگاری شکل گرفت و با سیاست‌گذاری رسانه پیوند خورد.",
        model="مدل زنجیره‌ای بحران: مهاجرت آگهی به پلتفرم، کاهش درآمد ناشر، کوچک‌شدن تحریریه، کاهش پوشش و تشدید افول؛ پاسخ‌ها شامل اشتراک، رویداد، حمایت بشردوستانه و کمک عمومی است.",
        studies=[
            "مقالهٔ سال ۲۰۱۴ شواهد تغییر زیست‌بوم خبری را تحلیل کرد.",
            "پژوهش‌های خبر محلی، افول و بیابان خبری را مستند کردند.",
            "مطالعات دیوار پرداخت، اثر آن بر درآمد و مخاطب را سنجیدند.",
            "پژوهش‌های سیاست عمومی، گزینه‌های حمایت از خبر را ارزیابی کردند.",
        ],
    ),
    "MC-062": dict(
        year=1980,
        summary="نیروهای پنج‌گانه، چارچوبی در تحلیل صنعت و راهبرد است که مایکل پورتر در کتاب راهبرد رقابتی در سال ۱۹۸۰ معرفی کرد و در سال ۲۰۰۸ در مقاله‌ای در هاروارد بیزینس ریویو بازنگری شد. ادعای مرکزی این است که جذابیت و سودآوری یک صنعت را پنج نیروی ساختاری تعیین می‌کند: رقابت میان رقبای موجود، تهدید ورود تازه‌واردان، تهدید کالاها و خدمات جایگزین، قدرت چانه‌زنی خریداران و قدرت چانه‌زنی تأمین‌کنندگان. مدیر باید با تحلیل این نیروها موقعیتی بسازد که در آن از فشار رقابتی در امان بماند یا بر آن غلبه کند؛ چارچوب، راهبرد را از سطح شرکت به سطح ساختار صنعت منتقل می‌کند. در صنایع رسانه‌ای، این مدل برای تحلیل رقابت میان شبکه‌ها، قدرت پلتفرم‌ها به‌عنوان تأمین‌کنندهٔ فناوری و توزیع، تهدید محتوای جایگزین و قدرت آگهی‌دهندگان و مخاطبان به کار رفته است. نقدهای اصلی به آن، ایستایی و توصیف لحظه‌ای صنعت، کم‌توجهی به مکمل‌ها و اکوسیستم‌های دیجیتال، سنجش‌پذیری دشوار نیروها و کم‌رنگ‌دیدن نقش نوآوری و نهادها مربوط می‌شود.",
        definition="نیروهای پنج‌گانه، چارچوبی است که جذابیت و سودآوری صنعت را با پنج نیروی ساختاری، یعنی رقابت درونی، تهدید ورود، تهدید جایگزین و قدرت خریدار و تأمین‌کننده، توضیح می‌دهد.",
        main_problem="چرا برخی صنایع سودآورتر از برخی دیگرند، و یک بنگاه چگونه می‌تواند موقعیت رقابتی خود را در برابر فشارهای ساختاری صنعت تعیین کند.",
        mechanism="هر یک از پنج نیرو، حاشیهٔ سود صنعت را از جهت متفاوتی تحت فشار می‌گذارد؛ ترکیب شدت این نیروها ساختار صنعت را می‌سازد و راهبرد بنگاه باید موقعیتی انتخاب کند که در برابر شدیدترین نیروها محافظت شود یا آن را به نفع خود تغییر دهد.",
        assumptions=[
            "ساختار صنعت، سودآوری بلندمدت را تعیین می‌کند.",
            "پنج نیروی ساختاری، فضای رقابت را قالب می‌زنند.",
            "بنگاه می‌تواند موقعیت خود را در برابر نیروها تغییر دهد.",
            "تحلیل صنعت پیش‌نیاز تدوین راهبرد است.",
            "رقابت فراتر از رقبای مستقیم، شامل ورود، جایگزین و زنجیرهٔ تأمین است.",
        ],
        principles=[
            "سودآوری را باید در سطح ساختار صنعت تحلیل کرد.",
            "پنج نیرو باید جداگانه و در ترکیب سنجیده شوند.",
            "راهبرد باید در برابر شدیدترین نیروها موقعیت بسازد.",
            "قدرت خریدار و تأمین‌کننده، حاشیهٔ سود را تعیین می‌کند.",
            "تهدید جایگزین و ورود، رقابت را از بیرون صنعت می‌سازد.",
            "تحلیل نیروها باید با شواهد و نه شهود انجام شود.",
        ],
        critiques=[
            "چارچوب ایستا و توصیف‌گر لحظه‌ای صنعت است.",
            "نقش مکمل‌ها و اکوسیستم‌های پلتفرمی را کم‌رنگ می‌کند.",
            "سنجش شدت نیروها به قضاوت کیفی وابسته است.",
            "نوآوری و تغییر سریع صنعت را به‌سختی دربرمی‌گیرد.",
            "نقش نهادها، مقررات و قدرت سیاسی کم‌بررسی می‌ماند.",
        ],
        critique_text="منتقدان می‌گویند نیروهای پنج‌گانه ابزار قدرتمندی برای تحلیل ساختار صنعت است اما تصویری ایستا می‌دهد و پویایی اکوسیستم‌های دیجیتال و نقش مکمل‌ها را پوشش نمی‌دهد. با این حال، همچنان یکی از پرکاربردترین چارچوب‌های تحلیل رقابت و راهبرد است.",
        applications=[
            "تحلیل رقابت در صنعت خبر و پخش.",
            "ارزیابی قدرت پلتفرم‌ها بر زنجیرهٔ ارزش رسانه.",
            "تحلیل تهدید محتوای جایگزین و سرگرمی رقیب.",
            "تدوین راهبرد بازاریابی و قیمت‌گذاری رسانه.",
            "آموزش مدیریت راهبردی رسانه.",
        ],
        example_text="یک شبکهٔ تلویزیونی در تحلیل نیروهای پنج‌گانه می‌بیند که رقابت درونی شدید است، پلتفرم‌های ویدئویی تهدید جایگزین‌اند، آگهی‌دهندگان قدرت چانه‌زنی بالایی دارند و تأمین‌کنندهٔ فناوری پخش، وابستگی ایجاد می‌کند؛ راهبرد آن باید بر تمایز محتوایی و تنوع درآمدی متمرکز شود. چارچوب پورتر همین تحلیل ساختاری را ممکن می‌کند.",
        evolution="کتاب سال ۱۹۸۰ چارچوب را تثبیت کرد و به متن کلاسیک راهبرد تبدیل شد. مقالهٔ سال ۲۰۰۸ آن را در برابر نقدها بازخوانی کرد و در دههٔ ۲۰۱۰ بحث مکمل‌ها و اکوسیستم پلتفرمی، بازنگری‌های بعدی را برانگیخت.",
        key_concepts=["رقابت درونی", "تهدید ورود", "کالای جایگزین", "قدرت خریدار", "قدرت تأمین‌کننده", "ساختار صنعت"],
        theorists="مایکل پورتر، سازندهٔ چارچوب نیروهای پنج‌گانه.",
        theorists_text="این چارچوب در سنت اقتصاد صنعتی و مدیریت راهبردی شکل گرفت و با تحلیل ساختار بازار پیوند خورد.",
        model="مدل پنج‌نیرویی: رقابت درونی، تهدید ورود، تهدید جایگزین، قدرت خریدار و قدرت تأمین‌کننده؛ شدت ترکیبی این نیروها جذابیت صنعت و فضای راهبردی بنگاه را تعیین می‌کند.",
        studies=[
            "کتاب سال ۱۹۸۰ چارچوب را با نمونه‌های صنعتی معرفی کرد.",
            "مقالهٔ سال ۲۰۰۸ چارچوب را بازخوانی و از سوءبرداشت‌ها دفاع کرد.",
            "پژوهش‌های مدیریت رسانه، مدل را برای صنعت خبر و پخش به کار بردند.",
            "مطالعات پلتفرم، بحث مکمل‌ها و بازنگری چارچوب را پیش بردند.",
        ],
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
                                       "verified": n_verified, "batch": 130}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH130 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
