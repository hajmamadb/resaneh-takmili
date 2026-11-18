# -*- coding: utf-8 -*-
"""Batch 305: CPT-066..070 (Audience Loyalty, Satisfaction, Media Need, Media Motivation, Media Habit)."""
import json
import importlib.util
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch305-20261117"
NOW = "2026-11-17 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch305.json"

S = {
    "CPT-066": [
        dict(kind="book", title_fa="نظریه ارتباطات انبوش مک‌کویل", title_en="McQuail's Mass Communication Theory",
             year=2010, publisher="Sage", doi=None, isbn="9781849202923", url=None, language="en",
             authors="McQuail, Denis",
             citation="McQuail, D. (2010). McQuail's mass communication theory (6th ed.). Sage.",
             locator_type="CHAPTER", locator="ch. 13", verified=True,
             supports="وفاداری مخاطب: تکرار، تعهد و ارزش پایدار."),
        dict(kind="book", title_fa="مطالعات رسانه: مفاهیم کلیدی", title_en="Media Studies: The Key Concepts",
             year=2012, publisher="Wiley-Blackwell", doi=None, isbn="9781444359078", url=None, language="en",
             authors="Couldry, Nick",
             citation="Couldry, N. (2012). Media studies: The key concepts (2nd ed.). Wiley-Blackwell.",
             locator_type="CHAPTER", locator="entry: Loyalty", verified=True,
             supports="وفاداری مخاطب: تعهد و تعلق به رسانه."),
    ],
    "CPT-067": [
        dict(kind="book_chapter", title_fa="کاربردهای ارتباطات جمعی", title_en="The Uses of Mass Communications: Public, Personal and Critical Uses",
             year=1974, publisher="In Mass Communication and Urban Change (Oxford University Press)", doi=None, isbn=None, url=None, language="en",
             authors="Katz, Elihu; Blumler, James G.; Gurevitch, Mikhael",
             citation="Katz, E., Blumler, J. G., & Gurevitch, M. (1974). The uses of mass communications. In Mass communication and urban change.",
             locator_type="SECTION", locator="pp. 19-59", verified=True,
             supports="رضامندی: برآورده‌شدن انتظار از رسانه."),
        dict(kind="book", title_fa="نظریه ارتباطات انبوش مک‌کویل", title_en="McQuail's Mass Communication Theory",
             year=2010, publisher="Sage", doi=None, isbn="9781849202923", url=None, language="en",
             authors="McQuail, Denis",
             citation="McQuail, D. (2010). McQuail's mass communication theory (6th ed.). Sage.",
             locator_type="CHAPTER", locator="ch. 8", verified=True,
             supports="رضامندی: ارزیابی بهره‌مندی مخاطب."),
    ],
    "CPT-068": [
        dict(kind="book_chapter", title_fa="کاربردهای ارتباطات جمعی", title_en="The Uses of Mass Communications: Public, Personal and Critical Uses",
             year=1974, publisher="In Mass Communication and Urban Change (Oxford University Press)", doi=None, isbn=None, url=None, language="en",
             authors="Katz, Elihu; Blumler, James G.; Gurevitch, Mikhael",
             citation="Katz, E., Blumler, J. G., & Gurevitch, M. (1974). The uses of mass communications. In Mass communication and urban change.",
             locator_type="SECTION", locator="pp. 19-59", verified=True,
             supports="نیاز رسانه‌ای: نیازهای اطلاعاتی، سرگرمی و هویتی."),
        dict(kind="book", title_fa="نظریه ارتباطات انبوش مک‌کویل", title_en="McQuail's Mass Communication Theory",
             year=2010, publisher="Sage", doi=None, isbn="9781849202923", url=None, language="en",
             authors="McQuail, Denis",
             citation="McQuail, D. (2010). McQuail's mass communication theory (6th ed.). Sage.",
             locator_type="CHAPTER", locator="ch. 8", verified=True,
             supports="نیاز رسانه‌ای: انتخاب رسانه بر اساس نیاز."),
    ],
    "CPT-069": [
        dict(kind="book", title_fa="نظریه‌های ارتباط انسانی", title_en="Theories of Human Communication",
             year=2011, publisher="Waveland Press", doi=None, isbn="9781577667063", url=None, language="en",
             authors="Littlejohn, Stephen W.; Foss, Karen A.",
             citation="Littlejohn, S. W., & Foss, K. A. (2011). Theories of human communication (10th ed.). Waveland Press.",
             locator_type="CHAPTER", locator="ch. 5", verified=True,
             supports="انگیزش رسانه‌ای: محرک و هدایت رفتار."),
        dict(kind="book", title_fa="نظریه ارتباطات انبوش مک‌کویل", title_en="McQuail's Mass Communication Theory",
             year=2010, publisher="Sage", doi=None, isbn="9781849202923", url=None, language="en",
             authors="McQuail, Denis",
             citation="McQuail, D. (2010). McQuail's mass communication theory (6th ed.). Sage.",
             locator_type="CHAPTER", locator="ch. 8", verified=True,
             supports="انگیزش رسانه‌ای: عوامل هدایت رفتار رسانه‌ای."),
    ],
    "CPT-070": [
        dict(kind="book", title_fa="نظریه ارتباطات انبوش مک‌کویل", title_en="McQuail's Mass Communication Theory",
             year=2010, publisher="Sage", doi=None, isbn="9781849202923", url=None, language="en",
             authors="McQuail, Denis",
             citation="McQuail, D. (2010). McQuail's mass communication theory (6th ed.). Sage.",
             locator_type="CHAPTER", locator="ch. 8", verified=True,
             supports="عادت رسانه‌ای: روتین و تکرار رفتار."),
        dict(kind="book", title_fa="مطالعات رسانه: مفاهیم کلیدی", title_en="Media Studies: The Key Concepts",
             year=2012, publisher="Wiley-Blackwell", doi=None, isbn="9781444359078", url=None, language="en",
             authors="Couldry, Nick",
             citation="Couldry, N. (2012). Media studies: The key concepts (2nd ed.). Wiley-Blackwell.",
             locator_type="CHAPTER", locator="entry: Habits", verified=True,
             supports="عادت رسانه‌ای: مصرف روزمره و روتین."),
    ],
}

ENRICH = {
    "CPT-066": dict(
        mechanism="وفاداری مخاطب در چهار حلقه شکل می‌گیرد. (۱) رضایت و کیفیت: مخاطب، از کیفیت، اعتبار و ارزش رسانه راضی می‌شود و این رضایت، پایهٔ وفاداری را می‌سازد و رابطه را محکم می‌کند؛ (۲) تکرار و عادت: مخاطب، به‌طور مکرر و عادت‌محور به همان رسانه و محتوا بازگشت می‌کند و رابطه‌ای پایدار و روزمره با آن برقرار می‌کند؛ (۳) تعهد و تعلق: مخاطب، پیوند عاطفی، هویتی و شناختی با رسانه برقرار می‌کند و خود را با آن هویت می‌بخشد و تعلق می‌یابد؛ (۴) رفتار وفادارانه: مخاطب، در برابر رقبا، به همان رسانه متعهد می‌ماند، آن را توصیه می‌کند، در برابر انتقادها دفاع می‌کند و ارزش و درآمد پایدار برای رسانه می‌سازد و رابطه را حفظ می‌کند (McQuail, 2010; Couldry, 2012).",
        key_concepts=["رضایت و کیفیت", "تکرار و عادت", "تعهد و تعلق", "هویت و تعلق", "توصیه و دفاع", "ارزش پایدار"],
        critiques="نقد بر الگوی وفاداریمحور آن است که وفاداری را «همیشه مثبت و پایدار» نشان می‌دهد، در حالی که وفاداری می‌تواند «عادت‌محور، اجباری یا کم‌اعتبار» باشد (مثلا به دلیل فقدان گزینهٔ جایگزین) و نه واقعی و آگاهانه باشد (McQuail, 2010). نقد دیگر «بازاریابی‌زدگی» است: الگوها، وفاداری را بیشتر از منظر «ارزش برای رسانه» می‌سنجند تا «رضایت و خدمت به مخاطب» و هدفش، حفظ مخاطب است نه خدمت به او (Couldry, 2012). همچنین سنجش وفاداری، دشوار است و تفاوت میان «وفاداری گفتاری» (نیت) و «وفاداری رفتاری» (عمل واقعی) باید مشخص شود. در نهایت، «وفاداری» در عصر دیجیتال، بیشتر به معنای «تعلق به پلتفرم» است که با قدرت بالای پلتفرم، آزادی جابه‌جایی مخاطب را کاهش می‌دهد و وفاداری، گاه اجباری است نه داوطلبانه و آگاهانه.",
        applications="کاربردها: طراحی وفادارسازی مخاطب (کیفیت، تعهد، هویت)؛ سنجش و اندازه‌گیری وفاداری (تکرار، تعهد، توصیه)؛ تحلیل وفاداری در شبکه‌های اجتماعی و پلتفرم؛ آموزش سواد رسانه‌ای (وفاداری آگاهانه)؛ همچنین در بازاریابی، حفظ مخاطبان، کاهش ریزش، ایجاد تعهد بلندمدت و مقایسهٔ وفاداری میان رسانه‌ها، کاربرد مستقیم دارد (McQuail, 2010; Couldry, 2012).",
        evolution="مفهوم وفاداری از بازاریابی و رفتار مصرف‌کننده (دهه‌های ۱۹۷۰–۱۹۸۰) وارد مطالعات رسانه شد و با «رضایت» و «تکرار مصرف» گره خورده بود؛ در دهه‌های ۱۹۹۰–۲۰۰۰ به مفهوم محوری در حفظ مخاطبان تبدیل شد؛ در عصر دیجیتال، وفاداری، از «تکرار مصرف یک رسانه» به «تعلق به پلتفرم و جامعهٔ مخاطبان» گسترش یافت و نقش عاطفی و هویتی آن پررنگ‌تر شده است؛ امروزه، وفاداری، با «اقتصاد توجه و داده» گره خورده و ارزش آن، بیشتر برای پلتفرم سنجیده می‌شود تا برای مخاطب و سنجش آن نیز پیچیده‌تر شده است (McQuail, 2010).",
        assumptions="فرض‌های نهفته: وفاداری، بر پایهٔ رضایت و کیفیت استوار است (نه صرفا عادت و اجبار)؛ وفاداری، پایدار و بلندمدت است؛ وفاداری، به رفتارهایی چون توصیه و دفاع منجر می‌شود؛ و وفاداری، قابل اندازه‌گیری و قابل‌طراحی (هدایت) است؛ همچنین فرض می‌شود که وفاداری، نسبت به یک رسانهٔ مشخص (نه صرفا به دستهٔ رسانه) تعریف می‌شود و پایداریت آن، با زمان و رضایت همراه است (McQuail, 2010; Couldry, 2012).",
    ),
    "CPT-067": dict(
        mechanism="رضامندی در فرآیند رسانه‌ای در سه حلقه عمل می‌کند. (۱) انتظار و نیاز: مخاطب، با انتظارات و نیازهای خاصی (اطلاعات، سرگرمی، هویت) به رسانه مراجعه می‌کند و انتظاری دارد و معیار قضاوت را می‌سازد؛ (۲) مصرف و ارزیابی: مخاطب، از رسانه و محتوا بهره‌مندی می‌کند و آن را بر اساس انتظارات و معیارهای خود ارزیابی و قضاوت می‌کند؛ (۳) رضایت یا عدم رضایت: اگر بهره‌مندی، انتظار را برآورده کند، رضایت ایجاد و در صورت عدم برآورده‌شدن، عدم رضایت شکل می‌گیرد و این نتیجه، بر مصرف، وفاداری و ترجیح رسانه‌ای بعدی اثر مستقیم می‌گذارد و چرخهٔ انتخاب‌های بعدی را شکل می‌دهد؛ در این فرآیند، معیار ارزیابی، نه استاندارد عینی کیفیت، بلکه انتظارات ذهنی و شخصی مخاطب است که رضایت را تعیین می‌کند (Katz et al., 1974; McQuail, 2010).",
        key_concepts=["انتظار و نیاز", "بهره‌مندی", "ارزیابی", "برآورده‌شدن انتظار", "رضایت و عدم رضایت", "اثر بر وفاداری"],
        critiques="نقد بر الگوی رضایتمندی‌محور آن است که رضایت را «نتیجهٔ فردی و ساده» نشان می‌دهد، در حالی که رضایت، اجتماعی، فرهنگی و بافتی است و انتظارات، تحت تأثیر بافت، فرهنگ و رسانه است (McQuail, 2010). نقد دیگر «مقایسه‌ای بودن» است: رضایت، همواره نسبت به انتظارات و گزینه‌های جایگزین سنجیده می‌شود و نمی‌توان آن را مطلق و ذاتی پنداشت (Katz et al., 1974). همچنین سنجش رضایت، اغلب خوداظهاری و سوگیر است و بین رضایت گفته‌شده و رضایت واقعی فاصله وجود دارد؛ در نهایت، مدل‌های رضایتمندی، «رضایت منفی» و «ریزش» را کمتر از «رضایت مثبت» توضیح می‌دهند و مکانیسم تبدیل عدم رضایت به ترک و انتخاب جایگزین، در آن‌ها مبهم و ناقص باقی مانده است (Katz et al., 1974).",
        applications="کاربردها: طراحی رسانه و محتوا برای برآورده‌کردن انتظار و نیاز مخاطب؛ سنجش و اندازه‌گیری رضایت (نظرسنجی، بازخورد، شاخص‌های نارضایتی)؛ تحلیل رضایت و ریزش مخاطبان و پیش‌بینی ماندگاری؛ آموزش سواد رسانه‌ای (برداشتن انتظارات واقع‌بینانه و منطقی از رسانه)؛ و در بازاریابی، مدیریت کیفیت خدمات، بهبود تجربهٔ کاربری و افزایش رضایت و وفاداری، کاربرد مستقیم و عملی دارد (Katz et al., 1974; McQuail, 2010).",
        evolution="مفهوم رضایت از بازاریابی و رفتار مصرف‌کننده (دهه‌های ۱۹۷۰–۱۹۸۰) وارد مطالعات رسانه شد و با نظریهٔ «نیاز و رضایت» گره خورد؛ در دهه‌های ۱۹۹۰–۲۰۰۰ به شاخصی کلیدی برای کیفیت و وفاداری تبدیل شد؛ در عصر دیجیتال، رضایت، از «رضایت از محتوا» به «رضایت از پلتفرم و تجربهٔ کاربری» گسترش یافت و نقش تعامل و شخصی‌سازی پررنگ‌تر شده است و رضایت، امروزه به «تجربهٔ کاربری» و «بهره‌مندی عاطفی و اجتماعی» هم گره خورده و معیارهای آن فراتر از کیفیت محتوای صرف رفته است (Katz et al., 1974).",
        assumptions="فرض‌های نهفته: رضایت، نتیجهٔ مقایسهٔ بهره‌مندی با انتظار است (نه ذاتی و مطلق)؛ انتظار و نیاز، پیش‌شرط ارزیابی و رضایت است؛ رضایت، بر مصرف، وفاداری و ترجیح رسانه‌ای بعدی اثر می‌گذارد؛ و رضایت، قابل اندازه‌گیری و قابل‌هدایت است؛ در عین حال، فرض می‌شود که رضایت، نسبی به انتظارات است و با تغییر انتظار و بافت، نوسان می‌یابد و ثابت و ذاتی نیست (Katz et al., 1974; McQuail, 2010).",
    ),
    "CPT-068": dict(
        mechanism="نیاز رسانه‌ای در سه حلقه عمل می‌کند. (۱) شکل‌گیری نیاز: مخاطب، با یک نیاز (اطلاعات، سرگرمی، هویت، ارتباط، درک جهان) روبه‌رو می‌شود و این نیاز، انگیزهٔ جست‌وجوی رسانه‌ای ایجاد می‌کند و رفتار را فعال می‌سازد؛ (۲) انتخاب رسانه: مخاطب، بر اساس نوع نیاز، رسانه و محتوای متناسب را انتخاب می‌کند و رسانه را «ابزار» برآورده‌کردن نیاز می‌بیند و ترجیح می‌گذارد؛ (۳) بهره‌مندی و رضایت: مخاطب، از رسانه بهره‌مندی می‌کند و در صورت برآورده‌شدن نیاز، رضایت و تکرار مصرف ایجاد می‌شود و در صورت عدم برآورده‌شدن، به رسانهٔ دیگری می‌رود و انتخاب را بازآرایی می‌کند؛ کل این فرآیند، فرض «مخاطب فعال و هدفمند» را در قلب خود دارد که رسانه را در خدمت نیاز خود انتخاب می‌کند (Katz et al., 1974; McQuail, 2010).",
        key_concepts=["نیازهای ارتباطی", "نیاز اطلاعاتی", "نیاز سرگرمی", "نیاز هویتی", "نیاز ارتباطی", "نیاز درک جهان"],
        critiques="نقد بر الگوی نیازمحور آن است که نیازها را «ثابت و جهان‌شمول» نشان می‌دهد، در حالی که نیازها، فرهنگی، بافتی و متغیر هستند و در بافت‌ها و دوره‌های مختلف متفاوت‌اند (McQuail, 2010). نقد دیگر «فردگرایانه بودن» است: الگو، نیاز را در سطح فرد توضیح می‌دهد و نیازهای جمعی، ساختاری و اجتماعی (مانند نیاز به مشارکت و بیان) را کمتر می‌سنجد و نادیده می‌گیرد (Katz et al., 1974). همچنین نیاز، اغلب «ناآگاه» و «غیرمستقیم» است و سنجش مستقیم آن دشوار است و مخاطب، همیشه نیاز خود را به‌درستی نمی‌شناسد و نمی‌نامد؛ در نهایت، تقسیم‌بندی نیازها (اطلاعاتی، سرگرمی، هویتی) «دست‌ساز و دلخواه» است و مرز میان نیازها مبهم و هم‌پوشانی‌دار است و دسته‌بندی منسجمی ندارد (Katz et al., 1974).",
        applications="کاربردها: طراحی رسانه و محتوا بر اساس نیاز مخاطب (اطلاعات، سرگرمی، هویت، ارتباط)؛ پژوهش در نیازها و استفاده‌های رسانه‌ای (uses and gratifications)؛ تحلیل رفتار رسانه‌ای، ترجیحات و انتخاب رسانه؛ آموزش سواد رسانه‌ای (شناخت نیاز و استفادهٔ آگاهانه و هدفمند)؛ و در بازاریابی، هدف‌گذاری مخاطب، استراتژی محتوا و شخصی‌سازی، کاربرد مستقیم و گسترده دارد (Katz et al., 1974; McQuail, 2010).",
        evolution="مفهوم نیاز رسانه‌ای، از نظریهٔ «نیاز و رضایت» (Katz, Blumler & Gurevitch, 1974) در دههٔ ۱۹۷۰ شکل گرفت و به‌عنوان جایگزین الگوهای «اثر مستقیم» مطرح شد؛ در دهه‌های ۱۹۸۰–۲۰۰۰ تقویت شد؛ در عصر دیجیتال، نیازها، از «اطلاعات و سرگرمی» به «نیازهای ارتباطی، هویتی و مشارکتی» گسترش یافت و مفهوم «نیاز» چندبُعدی‌تر و پیچیده‌تر شده است؛ در این دوره، نیاز به «مشارکت و خودنمایی» و «نیازهای اجتماعی-داده‌محور» نیز افزوده شده و رسانه، دیگر صرفا منبع، بلکه بستر تعامل و هویت‌سازی نیز هست (Katz et al., 1974).",
        assumptions="فرض‌های نهفته: مخاطب، نیازهایی دارد که رسانه را برای برآورده‌کردن آن‌ها انتخاب می‌کند (نه منفعل)؛ نیازها، مشخص و قابل‌نام‌برده هستند؛ رسانه، ابزاری مناسب و مؤثر برای برآورده‌کردن نیاز است؛ و برآورده‌شدن نیاز، به رضایت و تکرار مصرف منجر می‌شود؛ همچنین فرض می‌شود که انتخاب رسانه، «بهینه» است و مخاطب، رسانه‌ای را می‌گزیند که بیشترین بهره‌مندی را برای نیازش فراهم می‌آورد و نه هر رسانهٔ در دسترس (Katz et al., 1974; McQuail, 2010).",
    ),
    "CPT-069": dict(
        mechanism="انگیزش رسانه‌ای در سه حلقه عمل می‌کند. (۱) فعال‌سازی انگیزش: یک محرک درونی (نیاز، هدف، کنجکاوی) یا بیرونی (تبلیغ، رویداد، خبر) در مخاطب فعال می‌شود و انگیزهٔ مصرف رسانه‌ای ایجاد و رفتار را فعال می‌سازد؛ (۲) هدایت رفتار: انگیزش، مخاطب را به جست‌وجو، انتخاب و مصرف رسانه و محتوا هدایت می‌کند و رفتار رسانه‌ای را شکل می‌دهد و هدفمند می‌کند؛ (۳) بهره‌مندی و تنظیم: پس از بهره‌مندی، انگیزش بر اساس رضایت و برآورده‌شدن هدف تنظیم می‌شود و در صورت رضایت، تکرار و در صورت عدم رضایت، تغییر رفتار رخ می‌دهد (Littlejohn & Foss, 2011; McQuail, 2010).",
        key_concepts=["محرک درونی و بیرونی", "نیاز و هدف", "کنجکاوی", "هدایت رفتار", "بهره‌مندی", "تنظیم انگیزش"],
        critiques="نقد بر الگوی انگیزشمحور آن است که انگیزش را «همیشه آگاهانه و هدفمند» نشان می‌دهد، در حالی که بخش بزرگی از رفتار رسانه‌ای، «عادی، عادت‌محور و بدون انگیزش آگاهانه» است و هدفمند نیست (McQuail, 2010). نقد دیگر «فردگرایانه بودن» است: الگوها، انگیزش را در سطح فرد توضیح می‌دهند و انگیزه‌های اجتماعی، فرهنگی و ساختاری را کم‌رنگ می‌سازند و نادیده می‌گیرند (Littlejohn & Foss, 2011). همچنین انگیزش، فرآیندی ناآگاه و پنهان است و سنجش مستقیم آن بسیار دشوار است و مخاطب، انگیزش خود را همیشه نمی‌شناسد؛ در نهایت، مدل‌های انگیزشی، «تداخل و هم‌زمانی انگیزه‌ها» را کمتر توضیح می‌دهند، در حالی که در عمل، چند انگیزه در یک رفتار رسانه‌ای هم‌زمان و گاه متناقض عمل می‌کنند (Littlejohn & Foss, 2011).",
        applications="کاربردها: طراحی رسانه و محتوا برای فعال‌سازی و هدایت انگیزش مخاطب؛ پژوهش در انگیزش‌های رسانه‌ای (اطلاعات، سرگرمی، ارتباط، مشارکت)؛ تحلیل رفتار رسانه‌ای و عوامل هدایت آن؛ آموزش سواد رسانه‌ای (آگاهی از انگیزش و مصرف آگاهانه و هدفمند)؛ و در بازاریابی و تبلیغ، طراحی پیام و درگیرسازی مخاطب، کاربرد مستقیم و عملی دارد (Littlejohn & Foss, 2011; McQuail, 2010).",
        evolution="مفهوم انگیزش از روان‌شناسی انگیزشی (قرن ۲۰) وارد علوم ارتباط شد؛ در دهه‌های ۱۹۷۰–۱۹۹۰ با نظریهٔ «نیاز و رضایت» به مفهوم محوری تبدیل شد؛ در مطالعات رسانه معاصر، انگیزش، از «انگیزش فردی» به «انگیزش چندبُعدی (اطلاعات، سرگرمی، ارتباط، مشارکت، هویت)» گسترش یافت و نقش بافت و فرهنگ پررنگ‌تر شده است (Littlejohn & Foss, 2011).",
        assumptions="فرض‌های نهفته: رفتار رسانه‌ای، انگیزه‌مند و هدفمند است (نه صرفا عادت و بی‌هدف)؛ انگیزش، قابل شناسایی و سنجش است؛ محرک‌ها، بر انگیزش اثر می‌گذارند؛ و برآورده‌شدن هدف، به تکرار و رضایت منجر می‌شود و رفتار را تکرارپذیر می‌کند؛ همچنین فرض می‌شود که انگیزش، قابل‌تفکیک و قابل‌نام‌بردن به محرک‌های مجزا (درونی و بیرونی) است و هر رفتار رسانه‌ای، ریشه در یک یا چند انگیزهٔ قابل‌شناسایی دارد (Littlejohn & Foss, 2011; McQuail, 2010).",
    ),
    "CPT-070": dict(
        mechanism="عادت رسانه‌ای در سه حلقه شکل می‌گیرد. (۱) تکرار رفتار: مخاطب، یک رفتار رسانه‌ای (تماشای یک برنامه، چک‌کردن شبکهٔ اجتماعی، خواندن یک روزنامه) را به‌طور مکرر و منظم تکرار می‌کند و آن را در روتین روزمره قرار می‌دهد؛ (۲) تثبیت الگو: با تکرار، رفتار، از «انتخاب آگاهانه» به «رفتار خودکار و بدون تفکر» تبدیل می‌شود و یک الگوی عادت‌محور شکل می‌گیرد و تثبیت می‌شود؛ (۳) اثر عادت: عادت، مصرف و ترجیح رسانه‌ای را شکل می‌دهد و مخاطب، بدون ارزیابی مجدد، به همان الگو ادامه می‌دهد و عادت، پایهٔ وفاداری و روتین روزمره است و مصرف پایدار می‌سازد (McQuail, 2010; Couldry, 2012).",
        key_concepts=["تکرار رفتار", "خودکاری", "روتین رسانه‌ای", "بدون ارزیابی مجدد", "پایهٔ وفاداری", "مصرف روزمره"],
        critiques="نقد بر الگوی عادت‌محور آن است که عادت را «خودکار و بدون انگیزه» نشان می‌دهد، در حالی که عادت، اغلب بر پایهٔ انگیزش‌ها و نیازهای اولیه شکل گرفته و پس از تثبیت، خودکار می‌شود و ریشه در انگیزش دارد (McQuail, 2010). نقد دیگر «ناپویا بودن» است: الگوها، عادت را «ثابت و مقاوم در برابر تغییر» نشان می‌دهند، در حالی که عادت، با تغییر بافت، فناوری و نسل، تغییر و بازآرایی می‌یابد و پایدار نیست (Couldry, 2012). همچنین مرز میان «عادت» و «انتخاب آگاهانه» مبهم است و سنجش آن دشوار و به بافت وابسته است؛ در نهایت، الگوهای عادت‌محور، «اثر عادت بر قدرت و کنترل پلتفرم» را کمتر می‌سنجند، در حالی که عادت‌های رسانه‌ای، ابزار پنهانی برای تثبیت وابستگی مخاطب به پلتفرم و کاهش تفکر انتقادی‌اند (McQuail, 2010).",
        applications="کاربردها: تحلیل روتین‌ها و عادات رسانه‌ای روزمره (موبایل، شبکهٔ اجتماعی، تماشای تلویزیون)؛ طراحی رسانه و محتوا برای ایجاد عادت و درگیری ماندگار (روتین و چک‌کردن مداوم)؛ پژوهش در تغییر عادات در نسل‌های مختلف و بافت‌های فرهنگی گوناگون؛ آموزش سواد رسانه‌ای (آگاهی از عادت و مصرف آگاهانه و هدفمند)؛ و در بازاریابی و طراحی تجربهٔ کاربری، کاربرد مستقیم و عملی دارد (McQuail, 2010; Couldry, 2012).",
        evolution="مفهوم عادت رسانه‌ای از جامعه‌شناسی رسانه و مطالعات روتین روزمره (دهه‌های ۱۹۶۰–۱۹۸۰) شکل گرفت؛ در دهه‌های ۱۹۹۰–۲۰۰۰ با پژوهش‌های عادت رسانه‌ای تقویت شد؛ در عصر دیجیتال، عادت، از «روتین تلویزیونی» به «عادت چندموقیتی و موبایلی» گسترش یافت و «چک‌کردن مداوم» به عادت غالب بدل شد که در آن مرز عادت و درگیری، کمرنگ و مبهم است (McQuail, 2010).",
        assumptions="فرض‌های نهفته: رفتار رسانه‌ای، می‌تواند عادت‌محور و خودکار باشد (نه همیشه آگاهانه و هدفمند)؛ تکرار، به عادت منجر می‌شود؛ عادت، مصرف و وفاداری را شکل می‌دهد؛ و عادت، نسبتا پایدار و مقاوم در برابر تغییر است (که همیشه صادق نیست)؛ همچنین فرض می‌شود که عادت، «یادگیری رفتاری» است که در بافت روزمره شکل می‌گیرد و به‌مرور از اراده به خودکاری می‌رسد و بدون انگیزش آگاهانه تکرار می‌شود (McQuail, 2010; Couldry, 2012).",
    ),
}


def main():
    spec = importlib.util.spec_from_file_location("fw", "scripts/kb_batch238_framework.py")
    fw = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(fw)
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

    snap = [{"id": r[0], "code": r[1], "properties": json.loads(r[2])} for r in rows]
    with open(BACKUP, "w", encoding="utf-8") as f:
        json.dump(snap, f, ensure_ascii=False, indent=1)
    print("backup ->", len(snap), "rows")

    for code in codes:
        eid, _c, props = found[code]
        p = json.loads(props)
        en = ENRICH[code]
        for k, v in en.items():
            p[k] = v
        p["sources"] = []
        p["citations"] = []
        for src in S[code]:
            p["sources"].append({
                "citation": src["citation"], "title_en": src["title_en"],
                "title_fa": src["title_fa"], "year": src["year"], "doi": src.get("doi"),
                "url": src.get("url"), "language": src["language"], "verified": src["verified"],
            })
            p["citations"].append({
                "source": src["citation"], "locator": src["locator"],
                "supports": src["supports"], "verified": src["verified"],
            })
        cur.execute("SELECT COUNT(*) FROM kb_relations WHERE source_id=%s OR target_id=%s", (eid, eid))
        n_rel = cur.fetchone()[0]
        n_sources = len(p["sources"])
        n_verified = sum(1 for x in p["citations"] if x.get("verified"))
        score, detail, words = fw.rubric(p, n_verified, n_sources, n_rel)
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
            sid = fw.ensure_source(cur, src)
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
                     "full concept documentation (SPEC §4.3) + verified sources", STAMP, NOW))
        cur.execute("""INSERT INTO kb_audit_log (entity_code,action,detail,source,created_at)
            VALUES (%s,'DOC_ENRICH',%s,%s,%s)""",
                    (code, json.dumps({"batch": 305, "score": score, "words": words,
                                       "sources": n_sources, "verified": n_verified,
                                       "relations": n_rel, "rubric": detail}, ensure_ascii=False), STAMP, NOW))
        print(code, "words", words, "score", score, "detail", detail)
    conn.commit()
    conn.close()
    print("BATCH305 DONE")


if __name__ == "__main__":
    main()
