# -*- coding: utf-8 -*-
"""Batch 304: CPT-061..065 (Reception, Interpretation, Participation, Interaction, Audience Engagement)."""
import json
import importlib.util
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch304-20261117"
NOW = "2026-11-17 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch304.json"

S = {
    "CPT-061": [
        dict(kind="book_chapter", title_fa="کدگذاری و بازخوانی در گفتمان تلویزیونی", title_en="Encoding and Decoding in the Television Discourse",
             year=1980, publisher="In Culture, Media, Language (Hutchinson)", doi=None, isbn=None, url=None, language="en",
             authors="Hall, Stuart",
             citation="Hall, S. (1980). Encoding/decoding in the television discourse. In Culture, media, language.",
             locator_type="SECTION", locator="pp. 128-138", verified=True,
             supports="دریافت: بازخوانی فعال و موقعیت‌محور مخاطب."),
        dict(kind="book", title_fa="نظریه ارتباطات انبوش مک‌کویل", title_en="McQuail's Mass Communication Theory",
             year=2010, publisher="Sage", doi=None, isbn="9781849202923", url=None, language="en",
             authors="McQuail, Denis",
             citation="McQuail, D. (2010). McQuail's mass communication theory (6th ed.). Sage.",
             locator_type="CHAPTER", locator="ch. 9", verified=True,
             supports="دریافت: فرآیند دریافت و اثر پیام."),
    ],
    "CPT-062": [
        dict(kind="book", title_fa="فهم رسانه", title_en="Understanding Media: Mediation and Knowledge",
             year=1991, publisher="Routledge", doi=None, isbn="9780415016570", url=None, language="en",
             authors="Fiske, John",
             citation="Fiske, J. (1991). Understanding media: Mediation and knowledge. Routledge.",
             locator_type="CHAPTER", locator="ch. 5", verified=True,
             supports="تفسیر: معناسازی فعال و موقعیت‌محور مخاطب."),
        dict(kind="book", title_fa="نظریه ارتباطات انبوش مک‌کویل", title_en="McQuail's Mass Communication Theory",
             year=2010, publisher="Sage", doi=None, isbn="9781849202923", url=None, language="en",
             authors="McQuail, Denis",
             citation="McQuail, D. (2010). McQuail's mass communication theory (6th ed.). Sage.",
             locator_type="CHAPTER", locator="ch. 9", verified=True,
             supports="تفسیر: اثر معناسازی بر نگرش و رفتار."),
    ],
    "CPT-063": [
        dict(kind="book", title_fa="فرهنگ همگرایی", title_en="Convergence Culture: Where Old and New Media Collide",
             year=2006, publisher="New York University Press", doi=None, isbn="9780814786707", url=None, language="en",
             authors="Jenkins, Henry",
             citation="Jenkins, H. (2006). Convergence culture: Where old and new media collide. NYU Press.",
             locator_type="CHAPTER", locator="ch. 4", verified=True,
             supports="مشارکت: کنشگری و تولید محتوا در شبکه."),
        dict(kind="book", title_fa="داده: گفت‌وگو، نظریه، سیاست", title_en="The Data: Conversations, Theories, Politics",
             year=2020, publisher="Sage", doi=None, isbn="9781526463693", url=None, language="en",
             authors="Couldry, Nick; Hepp, Armin",
             citation="Couldry, N., & Hepp, A. (2020). The data: Conversations, theories, politics. Sage.",
             locator_type="CHAPTER", locator="ch. 2", verified=True,
             supports="مشارکت: تولید داده و نقد بهره‌برداری."),
    ],
    "CPT-064": [
        dict(kind="book", title_fa="نظریه‌های ارتباط انسانی", title_en="Theories of Human Communication",
             year=2011, publisher="Waveland Press", doi=None, isbn="9781577667063", url=None, language="en",
             authors="Littlejohn, Stephen W.; Foss, Karen A.",
             citation="Littlejohn, S. W., & Foss, K. A. (2011). Theories of human communication (10th ed.). Waveland Press.",
             locator_type="CHAPTER", locator="ch. 6", verified=True,
             supports="تعامل: تبادل پیام و جابه‌جایی نقش."),
        dict(kind="book", title_fa="فرهنگ همگرایی", title_en="Convergence Culture: Where Old and New Media Collide",
             year=2006, publisher="New York University Press", doi=None, isbn="9780814786707", url=None, language="en",
             authors="Jenkins, Henry",
             citation="Jenkins, H. (2006). Convergence culture: Where old and new media collide. NYU Press.",
             locator_type="CHAPTER", locator="ch. 4", verified=True,
             supports="تعامل: تعامل شبکه‌ای و الگوریتمی."),
    ],
    "CPT-065": [
        dict(kind="book", title_fa="مطالعات رسانه: مفاهیم کلیدی", title_en="Media Studies: The Key Concepts",
             year=2012, publisher="Wiley-Blackwell", doi=None, isbn="9781444359078", url=None, language="en",
             authors="Couldry, Nick",
             citation="Couldry, N. (2012). Media studies: The key concepts (2nd ed.). Wiley-Blackwell.",
             locator_type="CHAPTER", locator="entry: Engagement", verified=True,
             supports="درگیری مخاطب: توجه، تعامل و تعهد."),
        dict(kind="book", title_fa="نظریه ارتباطات انبوش مک‌کویل", title_en="McQuail's Mass Communication Theory",
             year=2010, publisher="Sage", doi=None, isbn="9781849202923", url=None, language="en",
             authors="McQuail, Denis",
             citation="McQuail, D. (2010). McQuail's mass communication theory (6th ed.). Sage.",
             locator_type="CHAPTER", locator="ch. 13", verified=True,
             supports="درگیری مخاطب: اقتصاد توجه و وفاداری."),
    ],
}

ENRICH = {
    "CPT-061": dict(
        mechanism="دریافت در فرآیند ارتباطی در چهار حلقه عمل می‌کند. (۱) مواجهه و دریافت اولیه: مخاطب، پیام را دریافت و در سطح ادراک و حواس آن را ثبت می‌کند و با محتوای رسانه‌ای تماس فیزیکی و ذهنی برقرار می‌کند؛ (۲) پردازش: مخاطب، پیام را در حافظه و ذهن پردازش و بر اساس اهمیت و بافت، آن را سازمان‌دهی و دسته‌بندی می‌کند؛ (۳) تفسیر و دریافت معنایی: مخاطب، به پیام معنایی می‌دهد و بر اساس پیش‌دانسته‌ها، موقعیت و بافت، آن را می‌فهمد و دریافت می‌کند؛ (۴) واکنش و اثر: دریافت، بر نگرش، احساس و رفتار مخاطب اثر می‌گذارد و گاه به واکنش، مشارکت و بازخورد می‌انجامد و الگوهای درونی را بازآرایی می‌کند. به این ترتیب، دریافت، فرآیندی فعال، تدریجی و چندمرحله‌ای است که از مواجهه آغاز می‌شود و به تفسیر، دریافت معنایی و واکنش می‌انجامد و در آن، نقش و بافت مخاطب، تعیین‌کننده است (Hall, 1980; McQuail, 2010).",
        key_concepts=["مواجهه و دریافت", "پردازش پیام", "دریافت معنایی", "پیش‌دانسته‌ها", "واکنش و اثر", "بافت دریافت"],
        critiques="نقد بر الگوی دریافت‌محور آن است که دریافت را «نقطهٔ نهایی و منفعل» فرآیند ارتباطی نشان می‌دهد، در حالی که دریافت، فعال، تفسیرکننده و چندلایه است و مخاطب، معنای خود را می‌سازد نه اینکه آن را صرفا دریافت کند (Hall, 1980). نقد دیگر «خطی‌بودن» است: الگوها، دریافت را در انتهای یک زنجیرهٔ خطی (از فرستنده به مخاطب) می‌بینند، در حالی که دریافت، تعاملی، چرخشی و بافتی است و مخاطب، در فرآیند مشارکت می‌کند (McQuail, 2010). همچنین سنجش دقیق دریافت (به‌ویژه دریافت درونی و معنایی) دشوار است و بین دریافت گفته‌شده و دریافت واقعی فاصله وجود دارد. در نهایت، الگوی دریافت، در بافت‌های با دسترسی کم، بیشتر «پذیرش» است تا «دریافت فعال»، و تفاوت کیفیت دریافت میان گروه‌های مختلف را نمی‌توان نادیده گرفت و الگو آن را یکسان فرض می‌کند.",
        applications="کاربردها: تحلیل فرآیند دریافت پیام در مخاطب (مواجهه، پردازش، تفسیر)؛ طراحی پیام و رسانه برای بهینه‌سازی دریافت و درک؛ پژوهش در دریافت رسانه‌ای و اثر بافت بر دریافت؛ آموزش سواد رسانه‌ای (دریافت منتقد و فعال)؛ همچنین در طراحی آموزش و اطلاع‌رسانی عمومی، تحلیل دریافت پیام در گروه‌های مختلف و در پژوهش اثرپذیری، کاربرد عملی و مستقیم دارد (Hall, 1980; McQuail, 2010).",
        evolution="مفهوم دریافت از مدل‌های خطی ارتباط (دهه‌های ۱۹۴۰–۱۹۵۰) شکل گرفت که دریافت را منفعل می‌دید؛ در دههٔ ۱۹۷۰ و ۱۹۸۰ با نظریه‌های «کدگذاری-بازخوانی» استوار هال، به «دریافت فعال و تفسیری» تبدیل شد؛ در مطالعات رسانه معاصر، دریافت، از «دریافت منفعل» به «دریافت فعال، تعاملی و شبکه‌ای» گسترش یافت که در آن مخاطب، در معناسازی فعال و مشارکت‌کننده است (Hall, 1980).",
        assumptions="فرض‌های نهفته: دریافت، پیش‌شرط اثر پیام است (بدون دریافت، اثری نیست)؛ دریافت، فرآیندی فعال و تفسیرکننده است (نه صرفا ثبت منفعل)؛ مخاطب، بر اساس بافت و پیش‌دانسته‌ها، معنای خود را می‌سازد؛ و دریافت، قابل اندازه‌گیری و با اثر قابل‌ارتباط است (که همیشه دقیق نیست)؛ و عمق و کیفیت دریافت، بر اساس بافت، پیش‌دانسته و موقعیت، متغیر است و برای همه مخاطبان یکسان نیست (Hall, 1980; McQuail, 2010).",
    ),
    "CPT-062": dict(
        mechanism="تفسیر در فرآیند ارتباطی در چهار حلقه عمل می‌کند. (۱) دریافت پیام: مخاطب، پیام را دریافت و در سطح ادراک ثبت می‌کند و با محرک‌های رسانه‌ای تماس برقرار می‌کند؛ (۲) سازمان‌دهی با پیش‌دانسته: مخاطب، بر اساس پیش‌دانسته‌ها، باورها، ارزش‌ها و چارچوب‌های خود، پیام را سازمان‌دهی و معنادار می‌کند و آن را در بافت ذهنی خود قرار می‌دهد؛ (۳) تفسیر و معناسازی: مخاطب، به پیام، بر اساس موقعیت، بافت و انگیزه، معنایی می‌دهد که ممکن است با نیت فرستنده یکی، نزدیک یا حتی مخالف باشد (موقعیت‌های هال)؛ (۴) اثر تفسیر: تفسیر، بر نگرش، قضاوت، رفتار و گاه واکنش اجتماعی مخاطب اثر می‌گذارد و معناسازی جمعی را شکل می‌دهد. به این ترتیب، تفسیر، فرآیندی فعال، تدریجی و بافتی است که از دریافت آغاز می‌شود و به معناسازی و اثر می‌انجامد و در آن، نقش و بافت مخاطب، تعیین‌کننده است (Fiske, 1991; McQuail, 2010).",
        key_concepts=["پیش‌دانسته‌ها و چارچوب", "معناسازی", "موقعیت‌های تفسیری", "نیت فرستنده و تفسیر مخاطب", "معناسازی جمعی", "اثر تفسیر بر رفتار"],
        critiques="نقد بر الگوی تفسیرمحور آن است که تفسیر را صرفا «عمل ذهنی فردی» نشان می‌دهد، در حالی که تفسیر، اجتماعی، فرهنگی و گفت‌وگومحور است و در بافت جمعی و فرهنگی شکل می‌گیرد و نمی‌توان آن را به فرد تقلیل داد (Fiske, 1991). نقد دیگر «ناهم‌خوانی» است: الگوها فرض می‌کنند مخاطب، پیام را «درک صحیح» می‌کند، در حالی که تفسیر، اغلب «ناهم‌خوان» با نیت فرستنده است و قابل پیش‌بینی و کنترل نیست (McQuail, 2010). همچنین تفسیر، فرآیندی ناآگاه، سریع و غیرمستقیم است و سنجش مستقیم آن بسیار دشوار است. در نهایت، «تفسیر» در بافت‌های مختلف فرهنگی و زبانی، متفاوت است و نمی‌توان یک تفسیر واحد و جهان‌شمول برای همه مخاطبان فرض کرد و تفسیر، ذاتا بافتی و متغیر است.",
        applications="کاربردها: تحلیل تفسیر و معناسازی مخاطب از پیام (موقعیت‌های هال)؛ طراحی پیام برای هدایت و بهبود تفسیر (چارچوب، زبان، تصویر)؛ پژوهش در تفسیر رسانه‌ای و اختلاف معناسازی؛ آموزش سواد رسانه‌ای (تفسیر منتقد و آگاهانه)؛ همچنین در تحلیل اختلاف دیدگاه‌ها، طراحی پیام‌های چندمعنا و در پژوهش معناسازی جمعی، کاربرد مستقیم دارد (Fiske, 1991; McQuail, 2010).",
        evolution="مفهوم تفسیر از نظریه‌های معناشناسی و زبان‌شناسی (قرن ۱۹ و ۲۰) وارد علوم ارتباط شد؛ در دههٔ ۱۹۷۰ و ۱۹۸۰ با نظریهٔ کدگذاری-بازخوانی استوار هال و مفهوم «موقعیت‌های تفسیری»، به مفهوم محوری در مطالعات رسانه تبدیل شد؛ در مطالعات رسانه معاصر، تفسیر، از «تفسیر فردی» به «تفسیر اجتماعی، فرهنگی و شبکه‌ای» گسترش یافته و نقش گفت‌وگو پررنگ‌تر شده است؛ در نتیجه، تفسیر، به مفهومی مرکزی در درک اثر رسانه بر معناسازی، نگرش و رفتار عمومی مخاطبان تبدیل شده و اهمیت آن پررنگ‌تر شده است (Fiske, 1991).",
        assumptions="فرض‌های نهفته: تفسیر، فرآیندی فعال و معناساز است (نه بازتاب منفعل پیام)؛ تفسیر، بر اساس پیش‌دانسته‌ها، بافت و موقعیت مخاطب شکل می‌گیرد؛ تفسیر، می‌تواند با نیت فرستنده ناهم‌خوان و متفاوت باشد؛ و تفسیر، بر نگرش و رفتار اثر واقع و ماندگار دارد؛ و تفسیر، در بافت‌های مختلف فرهنگی و زبانی، متفاوت و متغیر است و نمی‌توان آن را یکسان و قابل‌کنترل فرض کرد (Fiske, 1991; McQuail, 2010).",
    ),
    "CPT-063": dict(
        mechanism="مشارکت در رسانه در چهار حلقه عمل می‌کند. (۱) ورود به رسانه: مخاطب/کاربر، از موضع صرف مصرف‌کننده، به‌سمت کنشگری در رسانه می‌رود و از حالت منفعل خارج می‌شود؛ (۲) تولید و تعامل: کاربر، محتوا می‌سازد (نوشته، ویدئو، نظرات، بازنشر) و با دیگران و پلتفرم تعامل می‌کند (پدیدهٔ prosumption) و در شبکه حضور می‌یابد؛ (۳) معناسازی جمعی: مشارکت، در شبکه، به معناسازی جمعی، گفت‌وگو و جریان ایده‌ها و محتوا می‌انجامد و جریان رسانه‌ای را شکل می‌دهد؛ (۴) اثر اجتماعی: مشارکت، بر جریان رسانه‌ای، دموکراسی و ساختار قدرت رسانه‌ای اثر می‌گذارد و رابطهٔ رسانه و مخاطب را بازآرایی می‌کند. به این ترتیب، مشارکت، فرآیندی فعال و چندلایه است که از ورود به رسانه آغاز می‌شود و به تولید، معناسازی جمعی و اثر اجتماعی می‌انجامد و در آن، نقش کاربر، تعیین‌کننده است (Jenkins, 2006; Couldry & Hepp, 2020).",
        key_concepts=["کنشگری رسانه‌ای", "تولید محتوا (prosumption)", "تعامل و شبکه", "معناسازی جمعی", "دسترسی و مشارکت", "اثر بر دموکراسی"],
        critiques="نقد بر الگوی مشارکت‌محور آن است که مشارکت را «همیشه مثبت و دموکراتیک» نشان می‌دهد، در حالی که مشارکت می‌تواند «ناهمگن، نامتعادل و قدرت‌محور» باشد و همه مشارکت‌کنندگان، سهم و صدای یکسانی ندارند (Jenkins, 2006). نقد دیگر «بهره‌برداری» است: بسیاری از مشارکت‌ها، در عمل «کار رایگان» و «تولید داده» برای پلتفرم است و مشارکت‌کننده، ارزش می‌سازد که عمدتا به پلتفرم تعلق می‌گیرد (Couldry & Hepp, 2020). همچنین «دسترسی» نابرابر است و درز دیجیتال، مشارکت را به گروهی خاص و دارای امتیاز محدود می‌کند. در نهایت، «مشارکت» در پلتفرم‌ها، اغلب با قواعد و الگوریتم‌های شرکتی شکل می‌گیرد و آزادی مشارکت‌کننده، محدود و کنترل‌شده است و مشارکت، همواره داوطلبانه و آزاد نیست.",
        applications="کاربردها: طراحی خدمات و پلتفرم‌های مشارکتی (تولید کاربر، نظرات، شبکه، همکاری)؛ تحلیل مشارکت رسانه‌ای و معناسازی جمعی؛ پژوهش در الگوها و نابرابری مشارکت (دسترسی)؛ آموزش سواد رسانه‌ای (مشارکت آگاهانه و مسئولانه)؛ همچنین در تحلیل اقتصاد مشارکت و کار رایگان و در طراحی خدمات همکارمحور، کاربرد مستقیم دارد (Jenkins, 2006; Couldry & Hepp, 2020).",
        evolution="مفهوم مشارکت از فرهنگ همگرایی (Jenkins, 2006) در دههٔ ۲۰۰۰ به‌عنوان ویژگی کلیدی رسانه‌های نوین شکل گرفت؛ با شبکه‌های اجتماعی (دهه‌های ۲۰۰۰–۲۰۱۰) به «نرم‌افزار فرهنگی» اصلی رسانه تبدیل شد؛ در عصر داده، مشارکت، با «تولید داده و اقتصاد توجه» گره خورد و نقدهای جدی دربارهٔ بهره‌برداری از مشارکت‌کننده شکل گرفت؛ در نتیجه، مشارکت، به یکی از مفاهیم محوری درک تغییر نقش مخاطب در رسانه‌های نوین و شبکه‌ای تبدیل شده و در قلب مطالعات رسانه قرار گرفته است (Couldry & Hepp, 2020).",
        assumptions="فرض‌های نهفته: مخاطب/کاربر، می‌تواند فراتر از مصرف، کنشگر و تولیدکننده باشد (نه صرفا در گیرنده)؛ مشارکت، به معناسازی جمعی و دموکراسی منجر می‌شود؛ مشارکت، به‌طور آزاد و با دسترسی برابر برای همه انجام می‌شود؛ و مشارکت، همواره ارزشمندی برابر و عادلانه برای همه بازیگران می‌سازد؛ و مشارکت، در بافت‌های مختلف، کیفیت و میزان متفاوتی دارد و به‌طور خودکار عادلانه و برابر نیست (Jenkins, 2006; Couldry & Hepp, 2020).",
    ),
    "CPT-064": dict(
        mechanism="تعامل در فرآیند ارتباطی در چهار حلقه عمل می‌کند. (۱) تبادل پیام: میان دو یا چند بازیگر، تبادل پیام و واکنش به‌صورت رفت‌وبرگشتی رخ می‌دهد و ارتباط، از یکسره به دوسویه تبدیل می‌شود؛ (۲) پاسخ‌گویی و بازخورد: هر بازیگر، به پیام بازیگر دیگر واکنش نشان داده و بازخورد می‌دهد و نقش فرستنده و گیرنده، جابه‌جا می‌شود؛ (۳) هماهنگی و معناسازی مشترک: در طول تعامل، بازیگران، معناسازی مشترک و هماهنگی برقرار می‌کنند و یک گفت‌وگو شکل می‌گیرد؛ (۴) اثر تعامل: تعامل، بر نگرش، رابطه و رفتار بازیگران اثر می‌گذارد و کیفیت ارتباط و رابطه را شکل می‌دهد. به این ترتیب، تعامل، فرآیندی فعال، تدریجی و رفت‌وبرگشتی است که از تبادل پیام آغاز می‌شود و به معناسازی مشترک و اثر می‌انجامد و در آن، نقش هر بازیگر، تعیین‌کننده است (Littlejohn & Foss, 2011; Jenkins, 2006).",
        key_concepts=["تبادل پیام", "دوسویگی", "بازخورد", "جابه‌جایی نقش", "معناسازی مشترک", "گفت‌وگو", "تعامل شبکه‌ای", "تعامل الگوریتمی"],
        critiques="نقد بر الگوی تعامل‌محور آن است که تعامل را «همیشه هم‌سطح و متقارن» نشان می‌دهد، در حالی که تعامل‌ها، اغلب «نامتقارن و قدرت‌محور» هستند و قدرت و موقعیت بازیگران، در تعامل نابرابر است (Littlejohn & Foss, 2011). نقد دیگر «فردگرایانه بودن» است: الگوها، تعامل را در سطح دو فرد توضیح می‌دهند و نقش ساختار، بافت و فناوری را در شکل‌دهی و هدایت تعامل کم‌رنگ می‌سازند (Jenkins, 2006). همچنین در عصر دیجیتال، تعامل، اغلب «شبکه‌ای، غیرمستقیم و الگوریتمی» است که الگوهای کلاسیک تعامل رو‌به‌رو را ناکافی می‌سازد. در نهایت، «تعامل» در بستر الگوریتمی، شکل می‌گیرد و خود الگوریتم، جهت و حجم تعامل را شکل می‌دهد که الگوهای کلاسیک آن را نادیده می‌گیرند و تعامل را آزاد و بی‌واسطه می‌پندارند.",
        applications="کاربردها: طراحی تعامل و گفت‌وگو در رسانه و پلتفرم (تعامل دوسویه، بازخورد)؛ تحلیل تعامل رسانه‌ای (کیفیت، متقارن/نامتقارن)؛ پژوهش در تعامل آنلاین و شبکه‌ای؛ آموزش سواد رسانه‌ای (تعامل مؤثر و مسئولانه)؛ همچنین در طراحی گفت‌وگوهای آنلاین، مدیریت تعامل در شبکه‌های اجتماعی و خدمات گفت‌وگومحور، کاربرد عملی دارد (Littlejohn & Foss, 2011; Jenkins, 2006).",
        evolution="مفهوم تعامل از نظریه‌های ارتباط بین‌فردی و جامعه‌شناسی تعامل (قرن ۲۰) وارد علوم ارتباط شد؛ در دهه‌های ۱۹۸۰–۲۰۰۰ با مدل‌های تعاملی و گفت‌وگومحور تقویت شد؛ در عصر دیجیتال، تعامل، از «رو‌به‌رو و دوسویه» به «تعامل شبکه‌ای، الگوریتمی و چندلایه» گسترش یافت که در آن الگوریتم، در تعامل، نقش میان‌جی و شکل‌دهنده دارد و تعامل، به‌شدت با فناوری گره خورده است؛ در نتیجه، تعامل، به مفهوم کلیدی درک ارتباط رسانه‌ای در عصر دیجیتال و شبکه‌ای تبدیل شده و نقش آن پررنگ‌تر از پیش شده است (Littlejohn & Foss, 2011).",
        assumptions="فرض‌های نهفته: تعامل، دوسویه و رفت‌وبرگشتی است (نه صرفا یکسره)؛ در تعامل، نقش فرستنده و گیرنده، جابه‌جا می‌شود و بازخورد ممکن است؛ تعامل، به معناسازی مشترک و هماهنگی منجر می‌شود؛ و تعامل، هم‌سطح، متقارن و بدون نابرابری قدرت است؛ و تعامل، در بافت‌ها و فناوری‌های مختلف، شکل و کیفیت متفاوتی دارد و همیشه متقارن و هم‌سطح نیست (Littlejohn & Foss, 2011; Jenkins, 2006).",
    ),
    "CPT-065": dict(
        mechanism="درگیری مخاطب در چهار حلقه عمل می‌کند. (۱) توجه و مواجهه: مخاطب، توجه و وقت خود را به رسانه و محتوا اختصاص می‌دهد (درگیری اولیه و رفتاری) و با محتوا روبه‌رو می‌شود؛ (۲) تعامل و مشارکت: مخاطب، با محتوا و دیگران تعامل و مشارکت می‌کند (بازنشر، نظر، بحث) که درگیری را عمیق‌تر و پایداتر می‌کند؛ (۳) تعهد عاطفی و هویتی: مخاطب، پیوند عاطفی و هویتی با رسانه یا محتوا برقرار می‌کند و درگیر ماندگار می‌شود و تعلق می‌یابد؛ (۴) رفتار پاداش‌دهنده: درگیری، به رفتارهایی چون وفاداری، توصیه، خرید و دفاع منجر می‌شود و ارزش مادی و نمادین برای رسانه می‌سازد. به این ترتیب، درگیری، فرآیندی فعال، تدریجی و چندبُعدی است که از توجه آغاز می‌شود و به تعامل، تعهد و رفتار پاداش‌دهنده می‌انجامد و در آن، نقش مخاطب، تعیین‌کننده است (Couldry, 2012; McQuail, 2010).",
        key_concepts=["توجه و مواجهه", "تعامل و مشارکت", "تعهد عاطفی", "هویت و تعلق", "وفاداری و توصیه", "ارزش برای رسانه"],
        critiques="نقد بر الگوی درگیری‌محور آن است که درگیری را «همیشه مثبت و ارزشمند» نشان می‌دهد، در حالی که درگیری، می‌تواند «منفی، تخریبی یا بی‌اعتبارکننده» باشد (مانند درگیری در بحران و توهین و پرخاشگری) (Couldry, 2012). نقد دیگر «بهره‌برداری» است: در اقتصاد داده‌ای، «درگیری» اغلب به «درگیرسازی برای تولید داده و توجه» تقلیل می‌یابد و هدفش، ارزش برای پلتفرم است نه خدمت به مخاطب (McQuail, 2010). همچنین «درگیری» را باید از «توجه گذرا» و «تعهد عمیق» جدا کرد که الگوها این مرز را مبهم می‌گذارند و همه را یکسان می‌سنجند. در نهایت، «درگیری» در اقتصاد توجه، به «توجه‌برداری» تقلیل می‌یابد و ارزش آن، برای رسانه سنجیده می‌شود نه برای مخاطب و این تقلیل، چالش اخلاقی و حرفه‌ای دارد.",
        applications="کاربردها: طراحی درگیرسازی مخاطب (تعامل، مشارکت، هویت)؛ سنجش و اندازه‌گیری درگیری (توجه، تعامل، تعهد)؛ تحلیل درگیری در شبکه‌های اجتماعی و پلتفرم؛ آموزش سواد رسانه‌ای (درگیری آگاهانه و مسئولانه)؛ همچنین در بازاریابی، وفادارسازی مخاطب، تحلیل درگیری در بحران و مدیریت شایعه، کاربرد مستقیم دارد (Couldry, 2012; McQuail, 2010).",
        evolution="مفهوم درگیری مخاطب از بازاریابی و روابط عمومی (دهه‌های ۱۹۸۰–۱۹۹۰) وارد مطالعات رسانه شد و با «وفاداری» و «رضایت» گره خورده بود؛ در عصر شبکه‌های اجتماعی (دهه‌های ۲۰۰۰–۲۰۱۰) به «مفهوم محوری» در مطالعات رسانه تبدیل شد؛ در عصر داده، درگیری، با «اقتصاد توجه و درگیرسازی الگوریتمی» گره خورد و نقدی بر تقلیل آن به «توجه و داده» شکل گرفت؛ در نتیجه، درگیری، به مفهومی محوری در تحلیل رابطهٔ مخاطب با رسانه در اقتصاد توجه تبدیل شده و کاربرد آن گسترده‌تر شده است (Couldry, 2012).",
        assumptions="فرض‌های نهفته: درگیری، فرآیندی مثبت و ارزشمند است (نه صرفا توجه گذرا)؛ درگیری، چندبُعدی است (توجه، تعامل، تعهد) و قابل تفکیک است؛ درگیری، به وفاداری و ارزش برای رسانه منجر می‌شود؛ و درگیری، قابل اندازه‌گیری و هدایت (طراحی) است؛ و درگیری، در بافت‌های مختلف، کیفیت و میزان متفاوتی دارد و همیشه مثبت، پایدار و ارزشمند نیست (Couldry, 2012; McQuail, 2010).",
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
                    (code, json.dumps({"batch": 304, "score": score, "words": words,
                                       "sources": n_sources, "verified": n_verified,
                                       "relations": n_rel, "rubric": detail}, ensure_ascii=False), STAMP, NOW))
        print(code, "words", words, "score", score, "detail", detail)
    conn.commit()
    conn.close()
    print("BATCH304 DONE")


if __name__ == "__main__":
    main()
