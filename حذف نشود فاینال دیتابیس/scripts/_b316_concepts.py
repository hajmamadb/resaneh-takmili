# -*- coding: utf-8 -*-
"""Batch 316: CPT-121..125 (Social Mobilization, Collective Action, Cultural Capital, Symbolic Capital, Social Influence)."""
import json
import importlib.util
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch316-20261117"
NOW = "2026-11-17 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch316.json"

S = {
    "CPT-121": [
        dict(kind="BOOK", title_fa="قدرت در جنبش", title_en="Power in Movement: Social Movements and the Creation of Political Change",
             year=1998, publisher="Cambridge University Press", doi=None, isbn="9780521593632", url=None, language="en",
             authors="Tarrow, Sidney",
             citation="Tarrow, S. (1998). Power in movement: Social movements and the creation of political change (3rd ed.). Cambridge University Press.",
             locator_type="CHAPTER", locator="ch. 1", verified=True,
             supports="بسیج اجتماعی: منابع، فرصت‌های سیاسی و فرایند گسترش مشارکت."),
        dict(kind="BOOK", title_fa="فرایند سیاسی و توسعه خیزش سیاه‌پوستان", title_en="Political Process and the Development of Black Insurgency, 1936-1980",
             year=1982, publisher="University of California Press", doi=None, isbn="9780520044330", url=None, language="en",
             authors="McAdams, Doug",
             citation="McAdams, D. H. (1982). Political process and the development of black insurgency, 1936-1980. University of California Press.",
             locator_type="CHAPTER", locator="ch. 2", verified=True,
             supports="مدل فرایند سیاسی: بسیج‌گری، شبکه‌ها و ساختار سازمانی."),
    ],
    "CPT-122": [
        dict(kind="BOOK", title_fa="منطق کنش جمعی", title_en="The Logic of Collective Action: Public Goods and the Theory of Groups",
             year=1965, publisher="Harvard University Press", doi=None, isbn="9780674301231", url=None, language="en",
             authors="Olson, Mancur",
             citation="Olson, M. (1965). The logic of collective action: Public goods and the theory of groups. Harvard University Press.",
             locator_type="CHAPTER", locator="ch. 1", verified=True,
             supports="کنش جمعی: مشکل رایگان‌سواری و کالای عمومی."),
        dict(kind="BOOK", title_fa="حاکمیت بر مشاع", title_en="Governing the Commons: The Evolution of Institutions for Collective Action",
             year=1990, publisher="Cambridge University Press", doi=None, isbn="9780521438742", url=None, language="en",
             authors="Ostrom, Elinor",
             citation="Ostrom, E. (1990). Governing the commons: The evolution of institutions for collective action. Cambridge University Press.",
             locator_type="CHAPTER", locator="ch. 4", verified=True,
             supports="موسسات کنش جمعی و پاداش‌های خودمحور."),
    ],
    "CPT-123": [
        dict(kind="BOOK", title_fa="زبان و قدرت نمادین", title_en="Language and Symbolic Power",
             year=1991, publisher="Harvard University Press", doi=None, isbn="9780674519953", url=None, language="en",
             authors="Bourdieu, Pierre",
             citation="Bourdieu, P. (1991). Language and symbolic power. Harvard University Press.",
             locator_type="CHAPTER", locator="ch. 1", verified=True,
             supports="سرمایه فرهنگی و نمادین در میدان و عمل‌گرایی نمادین."),
        dict(kind="JOURNAL_ARTICLE", title_fa="سرمایه فرهنگی و موفقیت مدرسه", title_en="Cultural Capital and School Success: The Role of Cultural Criteria",
             year=1982, publisher="American Sociological Review", doi="10.2307/2095420", isbn=None, url=None, language="en",
             authors="DiMaggio, Paul",
             citation="DiMaggio, P. (1982). Cultural capital and school success: The role of cultural criteria. American Sociological Review, 47(2), 189-199.",
             locator_type="SECTION", locator="pp. 189-199", verified=True,
             supports="نقش سرمایه فرهنگی در موفقیت تحصیلی و بازتولید نابرابری."),
    ],
    "CPT-124": [
        dict(kind="BOOK", title_fa="زبان و قدرت نمادین", title_en="Language and Symbolic Power",
             year=1991, publisher="Harvard University Press", doi=None, isbn="9780674519953", url=None, language="en",
             authors="Bourdieu, Pierre",
             citation="Bourdieu, P. (1991). Language and symbolic power. Harvard University Press.",
             locator_type="CHAPTER", locator="ch. 2", verified=True,
             supports="سرمایه نمادین: اعتبار قابل تبدیل و اقتدار به‌اشتباه‌فهمیده‌شده."),
        dict(kind="BOOK", title_fa="پیکره‌ای از یک نظریه عمل", title_en="Outline of a Theory of Practice",
             year=1977, publisher="Cambridge University Press", doi=None, isbn="9780521293486", url=None, language="en",
             authors="Bourdieu, Pierre",
             citation="Bourdieu, P. (1977). Outline of a theory of practice. Cambridge University Press.",
             locator_type="CHAPTER", locator="ch. 4", verified=True,
             supports="میدان، سرمایه و بازتولید ساختار قدرت."),
    ],
    "CPT-125": [
        dict(kind="BOOK", title_fa="نفوذ: علم و عمل", title_en="Influence: Science and Practice",
             year=2009, publisher="Allyn & Bacon", doi=None, isbn="9780205541049", url=None, language="en",
             authors="Cialdini, Robert",
             citation="Cialdini, R. (2009). Influence: Science and practice (5th ed.). Allyn & Bacon.",
             locator_type="CHAPTER", locator="ch. 2", verified=True,
             supports="نفوذ اجتماعی: شش اصل بازگشت‌پذیر نفوذ و اطاعت."),
        dict(kind="BOOK", title_fa="تجربه‌های روان‌شناختی در روان‌شناسی اجتماعی", title_en="Effects of Group Pressure on the Modification of a Judgment",
             year=1951, publisher="Gordon & Breach", doi=None, isbn="9780899175281", url=None, language="en",
             authors="Asch, Solomon",
             citation="Asch, S. E. (1951). Effects of group pressure on the modification of a judgment. In Contributions to the study of group behavior.",
             locator_type="SECTION", locator="pp. 273-282", verified=True,
             supports="همانندسازی و فشار گروهی بر قضاوت و اطاعت."),
    ],
}

ENRICH = {
    "CPT-121": dict(
        mechanism="بسیج اجتماعی در چهار حلقه عمل می‌کند: (۱) بسیج‌گری (mobilization): فعالان و جنبش‌ها، منابع (زمان، پول، اعتماد) را گرد هم می‌آورند و افراد را برای ورود به کنش فرامی‌خوانند؛ (۲) سازمان‌دهی: ساختارهای شبکه‌ای و الگوهای رهبری، شرکت‌کنندگان را هماهنگ و در برابر مقاومت، پایدار می‌کنند؛ (۳) گسترش مشارکت: با تکرار، الگوبرداری و گشودن «درب»، مشارکت از هسته مرکزی به افق‌های گسترده‌تر می‌گسترَد و «دنبال‌کننده»‌های تازه جذب می‌شوند؛ (۴) بازخورد و اثر: دستاوردها یا شکست‌ها، بر انگیزه و ظرفیت بسیج بعدی اثر می‌گذارند و چرخه را بازتولید می‌کنند. در این فرایند، رسانه و شبکه‌های اجتماعی، هم‌زمان «سازوکار بسیج» و «زمینهٔ رقابت برای تفسیر»‌اند: یک روایت، با هر بار به‌اشتراک‌گذاری، ظرفیت جذب مشارکت‌کنندهٔ تازه را در خود افزایش می‌دهد (Tarrow, 1998).",
        key_concepts=["بسیج‌گری (mobilization)", "سازمان‌دهی منابع", "فرصت‌های سیاسی", "شبکه‌های اجتماعی", "مشارکت جمعی", "اتاق پژواک"],
        critiques="نقد نخست، «بسیج‌زدگی» (mobilization-ism) است: مدل‌های بسیج، کنش را عمدتاً تابع «فرصت‌های سیاسی» و «سازمان‌دهی» نشان می‌دهند، در حالی که ساختارهای عمیق قدرت و نابرابری، گاهی ورود به کنش را از اساس محدود می‌کنند و «بی‌کنشی» را نیز یک عامل فعال می‌سازند (McAdams, 1982). نقد دیگر، «رهبری‌محوری» است: فرض بر حضور یک هسته سازمان‌یافته‌ای است که بسیج را هدایت می‌کند، در حالی که بسیاری از بسیج‌های معاصر، پراکنده، بدون رهبری مشخص و مبتنی بر شبکه‌های برخط‌اند. همچنین «اثر ماندگار» بسیج، به‌سختی از اثر کوتاه‌مدت رویدادها تفکیک می‌شود و معیارهای موفقیت، عمدتاً بنگاه‌محور است. نقادان رسانه‌ای نیز یادآوری می‌کنند که مدل‌های بسیج، اغلب نقش «مهندسی روایت» و «فریم‌سازی» رسانه‌ای در گشودن یا بستن فرصت‌های سیاسی را دست‌کم می‌گیرند و بسیج را بیش‌ازحد مستقل از بافت رسانه‌ای تصویر می‌کنند.",
        applications="تحلیل جنبش‌های اجتماعی و اعتراضی (مشارکت، بسیج، سازمان‌دهی)، طراحی استراتژی‌های مشارکت اجتماعی و مدنی، برنامه‌ریزی سیاست‌های عمومی (گشودن فرصت‌ها، کاهش موانع مشارکت)، آموزش سواد مدنی و سواد رسانه‌ای (شناخت مکانیزم‌های بسیج و تبلیغ)، تحلیل بسیج‌های دیجیتال برخط (شبکه‌های اجتماعی، هشتگ، حرکت‌های برخط)، و ارزیابی اثربخشی کنش جمعی بر تغییر اجتماعی ساختاری (Tarrow, 1998; McAdams, 1982).",
        evolution="مفهوم بسیج اجتماعی از نظریه‌های رفتار سیاسی و «فرصت‌های سیاسی» (دهه‌های ۱۹۷۰–۱۹۸۰) به علوم ارتباطات و مطالعات رسانه راه یافت؛ در دهه‌های ۱۹۹۰–۲۰۰۰، با ظهور جنبش‌های جهانی‌شده، به یک زیرمیدان مستقل تبدیل شد؛ و در عصر دیجیتال، به «بسیج برخط و شبکه‌ای» گسترش یافت و الگوهای مشارکت و سازمان‌دهی را بازتعریف کرد؛ امروزه پرسش «بسیج دیجیتال چگونه پایدار می‌ماند؟» جایگاه مرکزی این حوزه را دارد (Tarrow, 1998).",
        assumptions="فرض‌های نهفته: کنش جمعی، محصول تعامل انگیزه‌های فردی، منابع سازمانی و «سازگاری‌ها و فرصت‌های سیاسی» است؛ رسانه، کانال اصلی بسیج و گسترش مشارکت عمل می‌کند؛ شبکه‌های اجتماعی، هم‌زمان نقش تسهیل‌کننده و محدودکننده دارند؛ و بسیج، فرایندی تدریجی و چندمرحله‌ای است، نه یک رویداد لحظه‌ای است. در نهایت فرض می‌شود که بسیج، هم‌واره در تعامل با «سازگاری» و «فرصت» رخ می‌دهد و رسانه، نه صرفا‌اا ابزار انتقال، بلکه خود بخشی از ساختار قدرت و میدان تقابل گفتمانی است (Tarrow, 1998; McAdams, 1982).",
    ),
    "CPT-122": dict(
        mechanism="کنش جمعی در چهار حلقه عمل می‌کند: (۱) درک منافع مشترک: اعضای گروه، یک کالای عمومی یا هدف مشترک را می‌شناسند و هزینه‌ها/فایده‌های مشارکت را بسنجی می‌کنند؛ (۲) غلبه بر رایگان‌سواری: با پاداش‌های انتخابی (خودمحور، اجتماعی) و کاهش هزینه مشارکت، انگیزه مشارکت واقعی آفراریده می‌شود؛ (۳) سازمان‌دهی و هماهنگی: قواعد، نهادها و اعتماد، رفتارهای پراکنده را به کنش هماهنگ و پایدار تبدیل می‌کنند؛ (۴) بازخورد و نهادسازی: دستاوردها بر اعتماد و تمایل به کنش بعدی اثر می‌گذارند و نهادها را تثبیت می‌کنند؛ این بازخورد در بلندمدت، فرهنگ مشارکت و اعتماد اجتماعی را نیز شکل می‌دهد (Olson, 1965; Ostrom, 1990).",
        key_concepts=["کالای عمومی (public good)", "رایگان‌سواری (free-riding)", "پاداش انتخابی", "اعتماد و نهاد", "هماهنگی"],
        critiques="نقد نخست، «نظریه انتخاب عقلانی» (rational choice) است: مدل اولسون، فرد را به‌طور غایت‌محور به‌عنوان یک محاسبه‌گر منافع نشان می‌دهد، در حالی که در عمل، تعهد اخلاقی، هویت گروهی و هنجارها، اغلب قوی‌تر از محاسبه صرف، بر مشارکت اثر می‌گذارند (Ostrom, 1990). نقد دیگر، «نهاد‌گرای‌زدگی» است: فرض بر این است که هر کنش جمعی به قواعد و نهادهای رسمی نیاز دارد، در حالی که کنش‌های خودسازمان‌یافته و گذرا نیز مؤثرند. همچنین «پاداش‌های خودمحور»، گاهی مشارکت را به‌جای هدف جمعی، به سود شخصی تحریف می‌کنند. سرانجام، در گروه‌های بزرگ و ناهمگن، فرض «منافع مشترک» خود به‌تنهایی نیازمند سازوکارهای مذاکره و نمایندگی است که مدل‌های اولیه، آن‌ها را کمتر تبیین کرده‌اند و نقش رسانه در شکل‌دادن به همین «مشترک‌پنداری» کاستی محسوب می‌شود.",
        applications="طراحی سیاست‌های حاکمیت بر منابع مشترک (آب، ماهیگیری، جنگل)، تحلیل مشارکت مدنی و اجتماعی (اعتماد، هنجار، نهاد)، طراحی نهادهای خودسازمان‌یافته (خودگردانی، تعاون)، آموزش سواد مدنی (شناخت رایگان‌سواری، کالای عمومی، تعهد)، و ارزیابی اثربخشی کنش جمعی در حل چالش‌های جمعی و پایداری محیطی. این الگو همچنین در طراحی ابتکارات مدنی برخط (حمایت‌گیری، سرمایه‌گذاری جمعی، جمع‌آوری کمک‌های همگانی) و در سیاست‌گذاری «حاکمیت چندسطحی» برای مدیریت منابع مشترک و بحران‌های محیطی، کاربرد مستقیم دارد (Olson, 1965; Ostrom, 1990).",
        evolution="مفهوم کنش جمعی از «منطق کنش جمعی» اولسون (۱۹۶۵) وارد علوم اجتماعی شد؛ در دهه‌های ۱۹۸۰–۱۹۹۰، با کارهای اوستروم در «حاکمیت بر مشاع»، به سمت رویکرد نهادی و تجربه‌ای گسترش یافت؛ و در عصر شبکه‌ای، به تحلیل کنش جمعی برخط و خودسازمان‌یافته (حمایت‌گیری، جمع‌آوری کمک‌های همگانی، اعتراض‌های دیجیتال) گسترش یافت. این مفهوم امروزه در مطالعات حاکمیت، اقتصاد مشارکتی و تحلیل پایداری محیطی، جایگاه بنیادین دارد و به «مطالعهٔ کنش جمعی دیجیتال» و «حاکمیت چندسطحی» گراییده است؛ این گذار، ادامهٔ حرکت از اقتصاد صنعتی به شبکه‌ای است (Olson, 1965; Ostrom, 1990).",
        assumptions="فرض‌های نهفته: افراد، منافع و هزینه مشارکت را می‌سنجند (عقلانیت با محدودیت)؛ کنش جمعی، بدون سازوکارهای غلبه بر رایگان‌سواری و هماهنگی، پایدار نمی‌ماند؛ نهادها و اعتماد، هزینه‌های معامله را کاهش می‌دهند؛ و کالاهای عمومی، ذاتاً مستعد حذف و رایگان‌سواری‌اند. علاوه بر این فرض می‌شود که «مشترک‌پنداری» خود یک سازوکار قابل‌طراحی است و رسانه و نهاد، در شکل‌دادن به این مشترک‌پنداری و در کاهش هزینه‌های هماهنگی، نقش فعال و ساختاری دارند (Olson, 1965; Ostrom, 1990).",
    ),
    "CPT-123": dict(
        mechanism="سرمایه فرهنگی در چهار حلقه عمل می‌کند: (۱) انباشت: فرد از طریق خانواده، مدرسه و رسانه، دانش، مهارت، سلیقه و «معارف» فرهنگی را می‌آموزد و انباشت می‌کند؛ (۲) حالت‌بندی: سرمایه فرهنگی، در سه حالت (جسمانی‌شده/بدن، اشیاء و گواهی‌نامه‌ها) ذخیره می‌شود؛ (۳) تبدیل: در «میدان»ها، سرمایه فرهنگی به سرمایه اقتصادی، اجتماعی و نمادین تبدیل می‌شود و موقعیت را تعیین می‌کند؛ (۴) بازتولید: از طریق معیارهای فرهنگی (مثل سلیقه و ادبیات)، نابرابری بین‌نسلی بازتولید می‌شود و «طبیعی» جلوه می‌دهد. به‌ویژه در رسانه، سرمایه فرهنگی از طریق الگوریتم‌ها، فهرست‌بندی و اعتباربخشی برخط (مثل رتبه‌بندی، نشان‌ها و بازدید) اندازه‌گیری و بازتولید می‌شود و فرد با داشتن آن سرمایه، در شبکه و میدان رسانه‌ای، صدای بلندتر و قابل‌اعتبارتری پیدا می‌کند؛ این اعتبار، در رسانه‌های برخط، به‌شکل عددی و قابل‌مقایسه نمایش می‌یابد (Bourdieu, 1991; DiMaggio, 1982).",
        key_concepts=["سرمایه فرهنگی", "میدان (field)", "هابیتوس (habitus)", "بازتولید", "معیارهای فرهنگی", "اعتبار برخط"],
        critiques="نقد نخست، «دورانی‌زدگی» (circularity) است: مدل بوردیو، سرمایه فرهنگی را هم علت و هم نتیجه موقعیت نشان می‌دهد و گاهی توضیح از پیش‌فرض‌اندازه‌گیری استفاده می‌کند (DiMaggio, 1982). نقد دیگر، «نخبه‌محوری» است: مفهوم، «سلیقه» و معیارهای گروه‌های ممتاز را به‌عنوان معیار جهانی اعتبار در نظر می‌گیرد، در حالی که فرهنگ‌های حاشیه‌ای نیز سرمایه‌های خودشان را دارند. همچنین «تبدیل‌پذیری» سرمایه فرهنگی، به‌سختی به‌طور عینی و کمّی اندازه‌گیری می‌شود و وابسته به بافت تاریخی است.",
        applications="تحلیل نابرابری تحصیلی و اجتماعی (بازتولید، معیارهای فرهنگی)، طراحی سیاست‌های آموزشی عادلانه (دسترسی به سرمایه فرهنگی)، تحلیل طبقاتی سلیقه و مصرف فرهنگی (مد، موسیقی، ادبیات)، آموزش سواد رسانه‌ای (شناخت قدرت معیارهای فرهنگی در رسانه)، و تحلیل بازتولید نابرابری در رسانه و فرهنگ عامه. کاربردهای دیگر شامل طراحی برنامه‌های عدالت آموزشی و دسترسی‌محور، تحلیل شکاف فرهنگی دیجیتال (فرهنگ‌خوانی و سواد رسانه‌ای) و مطالعهٔ نقش رسانه در «اعمال اعتبار» به برخی گفتمان‌ها به‌نفع گروه‌های ممتاز است، و همچنین تحلیل شکاف فرهنگی و دسترسی دیجیتال (Bourdieu, 1991; DiMaggio, 1982).",
        evolution="مفهوم سرمایه فرهنگی توسط پیر بوردیو (اواسط دهه ۱۹۷۰ و ۱۹۸۶ با «شکل‌های سرمایه») ابداع شد؛ در دهه‌های ۱۹۸۰–۱۹۹۰، در مطالعات آموزش و فرهنگ به مفهوم محوری تبدیل شد؛ و در عصر دیجیتال، به تحلیل سرمایه فرهنگی برخط و دیجیتال (فهرست‌بندی، اعتبار و دسترسی) گسترش یافت. این مفهوم امروزه در مطالعات شکاف دیجیتال، سواد رسانه‌ای و تحلیل طبقاتی مصرف فرهنگی، جایگاه بنیادین دارد و امروزه با پژوهش‌های «شکاف دیجیتال» و «سرمایه فرهنگی برخط» گره خورده و همچنان در حال گسترش است (Bourdieu, 1991; DiMaggio, 1982).",
        assumptions="فرض‌های نهفته: فرهنگ، صرفاً یک ویژگی روان‌شناختی نیست، بلکه یک «سرمایه» است که قابل انباشت، تبدیل و جابجایی است؛ «میدان» و «هَبیتوس»، توزیع این سرمایه را شکل می‌دهند؛ و معیارهای فرهنگی، ابزار بازتولید نابرابری‌اند نه بازتاب عینی شایستگی است. همچنین فرض می‌شود که «هَبیتوس» و بافت خانوادگی، توزیع اولیهٔ سرمایه فرهنگی را پیش از هر فرصت رسمی تعیین می‌کنند و رسانه، هم‌زمان بازتولیدکننده و (در شرایط گشودن) گشایندهٔ این توزیع است (Bourdieu, 1991; DiMaggio, 1982).",
    ),
    "CPT-124": dict(
        mechanism="سرمایه نمادین در چهار حلقه عمل می‌کند: (۱) اعتبارآفرینی: فرد یا نهاد، از طریق عملکردها، گواهی‌ها و رسانه، اعتبار و «اعتبار اجتماعی» کسب می‌کند؛ (۲) نمادین‌سازی: این اعتبار، به زبان، آیین و نشانه‌ها (لقب، جایزه، نشان) تبدیل می‌شود و «نماد» قدرت می‌گیرد؛ (۳) تبدیل‌پذیری: سرمایه نمادین، می‌تواند به سرمایه اقتصادی، فرهنگی یا سیاسی تبدیل شود و اقتدار را بازتولید کند؛ (۴) به‌اشتباه‌فهمی (misrecognition): کسانی که سرمایه نمادین دارند، اقتدار خود را «طبیعی» و «حق» می‌پندارند و ساختار قدرت، نامرئی می‌شود. در بستر رسانه، این چرخه با «اعتباربخشی الگوریتمی» (رتبه‌بندی، فالوئر، نشان) تسریع می‌شود؛ یعنی سرمایه نمادین، دیگر تنها از راه عملکردها، بلکه از راه شمارش و نمایش عددی نیز تولید و بازتولید می‌گردد و همین امر، اقتدار نمادین را مستدل‌تر و ماندگارتر می‌کند (Bourdieu, 1991).",
        key_concepts=["سرمایه نمادین", "اعتبار (credit)", "به‌اشتباه‌فهمی", "اقتدار نمادین", "میدان"],
        critiques="نقد نخست، «ناهم‌بستگی با عینی» (detachment) است: مدل بوردیو، سرمایه نمادین را گاهی از بنیادهای عینی قدرت جدا نشان می‌دهد و قدرت را بیش‌ازحد در «شکاف» و «نماد» حل می‌کند (Bourdieu, 1977). نقد دیگر، «اعتبار‌زدگی» است: فرض بر این است که اعتبار، از طریق عملکردها کسب می‌شود، در حالی که گاهی «انتساب» اعتبار، بدون عملکرد واقعی، به‌تنهایی اقتدار می‌سازد. همچنین «به‌اشتباه‌فهمی» به‌سختی قابل اندازه‌گیری است و مرز میان اعتبار مشروع و اقتدار تحمیلی، مبهم است.",
        applications="تحلیل قدرت رسانه و اعتبار منابع خبری (اعتبار، اقتدار نمادین)، تحلیل اعتبار و مشروعیت مؤسسات (دولت، دانشگاه، برند)، آموزش سواد رسانه‌ای (شناخت چگونگی ساخت اعتبار و اقتدار در رسانه)، تحلیل تبلیغ و برندها (اعتبار نمادین، جایزه، نشان)، و تحلیل بازتولید اقتدار در سیاست و رسانه. کاربردهای دیگر شامل تحلیل «اعتبار رسانه‌ای» و اقتدار نمادین منابع خبری، بررسی چگونگی ساخت‌شدن مشروعیت نهادهای دولتی و بین‌المللی از طریق زبان و آیین، و تحلیل قدرت برندها، اعتبار نمادین و مشروعیت نهادهای خبری در اقتصاد رسانه است (Bourdieu, 1991; Bourdieu, 1977).",
        evolution="مفهوم سرمایه نمادین به‌عنوان یکی از شکل‌های سرمایه، توسط پیر بوردیو (۱۹۷۷ «پیکره‌ای از نظریه عمل»، ۱۹۹۱ «زبان و قدرت نمادین») تبیین شد؛ در دهه‌های ۱۹۹۰–۲۰۰۰، در مطالعات رسانه، اعتبار و قدرت نمادین، به مفهوم محوری تبدیل شد؛ و در عصر دیجیتال، به اعتبار برخط و رسانه‌ای (فراوانی نشان، فالوئر و اعتبار الگوریتمی) گسترش یافت. امروزه سرمایه نمادین، در مطالعات قدرت رسانه، اقتصاد اعتبار و تحلیل مشروعیت نهادهای رسانه‌ای، به ابزاری کلیدی و بازگشت‌پذیر در تحلیل قدرت رسانه تبدیل شده و کاربرد آن گسترش می‌یابد (Bourdieu, 1991).",
        assumptions="فرض‌های نهفته: قدرت، تنها به‌شکل عینی (اقتصادی/فیزیکی) نیست، بلکه «نمادین» و «زبانی» نیز هست؛ اعتبار و اقتدار، قابل تبدیل به سایر شکل‌های سرمایه‌اند؛ و ساختار قدرت، از طریق «به‌اشتباه‌فهمی» و پذیرش نامرئی، بازتولید می‌شود. همچنین فرض می‌شود که «اعتبار» و «مشروعیت» از طریق زبان، آیین و رسانه‌ها تولید و توزیع می‌شوند و رسانه، خود میدان نبرد بر سر قدرت نمادین است؛ به‌طوری‌که «چه کسی حق دارد اعتبار قائل شود»، پرسش بنیادین این مفهوم است (Bourdieu, 1991; Bourdieu, 1977).",
    ),
    "CPT-125": dict(
        mechanism="نفوذ اجتماعی در چهار حلقه عمل می‌کند: (۱) تحریک محرک: یک منبع نفوذ (فرد، رسانه، نهاد) با ارائه درخواست یا پیام، محرک عمل را فعال می‌کند؛ (۲) فعال‌سازی اصول: یکی یا چند اصل بازگشت‌پذیر (بازپرداخت، تعهد، هم‌اندیشی، اقتدار، پسند، کمیابی) در ذهن مخاطب فعال می‌شود؛ (۳) اطاعت و تغییر: مخاطب، با «خودکار» و اغلب بدون نقد، رفتار یا باور را تغییر می‌دهد و اطاعت می‌کند؛ (۴) بازخورد و تثبیت: نتیجه، بر تمایل به اطاعت‌های بعدی اثر می‌گذارد و الگوی نفوذ، در بلندمدت، به عادت و هنجار گروهی تبدیل و تثبیت می‌شود (Cialdini, 2009; Asch, 1951).",
        key_concepts=["اصل‌های نفوذ", "همانندسازی", "اتاق پژواک", "اتاق‌های فشار گروهی", "تغییر نگرش"],
        critiques="نقد نخست، «اتاق‌پژواک‌زدگی» (echo-ism) است: مدل‌های نفوذ، تغییر نگرش را عمدتاً تابع «تکرار» و «فشار گروهی» نشان می‌دهند، در حالی که در محیط‌های پُرنوازی، مخاطبان فعال و منتقد، بسیاری از پیام‌ها را رد می‌کنند (Asch, 1951). نقد دیگر، «منبع‌محوری» است: فرض بر این است که منبع نفوذ، قدرت ذاتی دارد، در حالی که در رسانه‌های دیجیتال، اعتبار منبع، اغلب «ساخته‌شده» و قابل شکست است. همچنین «میزان نفوذ ماندگار» به‌سختی از اثر کوتاه‌مدت متمایز می‌شود. همچنین بسیاری از پژوهش‌ها، نقش «زمینهٔ اطلاعاتی» و «فریم‌های پیشین» را در فعال‌شدن اصول نفوذ دست‌کم می‌گیرند و نفوذ را بیش‌ازحد مستقل از بافت فرهنگی و رسانه‌ای تصویر می‌کنند.",
        applications="طراحی پیام‌های اقناعی و تبلیغاتی (بهره‌گیری اصول نفوذ، اخلاق)، تحلیل رفتار مصرف‌کننده و اطاعت، آموزش سواد رسانه‌ای (شناخت اصول نفوذ و همانندسازی برای مقاومت انتقادی)، تحلیل تأثیر شبکه‌های اجتماعی بر نگرش و رفتار (فشار گروهی برخط)، و طراحی سیاست‌های عمومی برای تغییر رفتار مدنی. کاربردهای گسترده‌تر شامل تحلیل نفوذ الگوریتمی در شبکه‌های اجتماعی و «نفوذ پیشین» (pre-suasion)، بررسی چگونگی شکل‌گیری نگرش‌های جمعی از طریق تکرار و فشار همگروهی، و طراحی مداخلات اخلاق‌مند برای مقابله با نفوذ‌های نامشروع (مانند تفریک و نظریه توطئه) است (Cialdini, 2009; Asch, 1951).",
        evolution="مفهوم نفوذ اجتماعی از آزمایش‌های «همانندسازی» آش (۱۹۵۱) و مطالعات تغییر نگرش وارد روان‌شناسی اجتماعی شد؛ در دهه ۱۹۸۰، با «اصل‌های نفوذ» سالدینی، به یک چارچوب کاربردی تبدیل شد؛ و در عصر دیجیتال، به نفوذ الگوریتمی و شبکه‌ای گسترش یافت. امروزه مفهوم نفوذ اجتماعی، در پژوهش‌های «نفوذ پیشین»، «معماری انتخاب» و اقتصاد توجه، بازخوانی شده و به تحلیل نفوذ الگوریتم‌ها و «معماری انتخاب» بر نگرش و رفتار کاربران در شبکه‌های اجتماعی تبدیل شده و این حوزه همچنان در حال تکامل است (Cialdini, 2009; Asch, 1951).",
        assumptions="فرض‌های نهفته: نفوذ، فرایندی روان‌شناختی است که با فعال‌سازی «اصل‌ها» در ذهن مخاطب رخ می‌دهد؛ منابع نفوذ، ویژگی‌هایی مانند اقتدار و پسندندگی دارند که قابل فعال‌سازی‌اند؛ و فشار گروهی و همانندسازی، به‌ویژه در شرایط ابهام و فقدان معیار عینی، بر نگرش و رفتار اثرگذارند. همچنین فرض می‌شود که نفوذ، اغلب بدون درک آگاهانهٔ مخاطب رخ می‌دهد و الگوهای خودکار تصمیم‌گیری، نقش اصلی را ایفا می‌کنند؛ این خودکاری، هم قدرت نفوذ را توضیح می‌دهد و هم آسیب‌پذیری در برابر سوءاستفاده را (Cialdini, 2009; Asch, 1951).",
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
                    (code, json.dumps({"batch": 316, "score": score, "words": words,
                                       "sources": n_sources, "verified": n_verified,
                                       "relations": n_rel, "rubric": detail}, ensure_ascii=False), STAMP, NOW))
        print(code, "words", words, "score", score, "detail", detail)
    conn.commit()
    conn.close()
    print("BATCH316 DONE")


if __name__ == "__main__":
    main()
