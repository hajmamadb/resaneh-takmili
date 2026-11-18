# -*- coding: utf-8 -*-
"""Batch 335: CPT-206..210 (Asynchronous Communication, Virtual Presence, Virtual Community, Online Community, Influence)."""
import json
import importlib.util
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch335-20261117"
NOW = "2026-11-17 00:00:00"
BATCH = 335
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch335.json"

S = {
    "CPT-206": [
        dict(kind="BOOK", title_fa="فرهنگ همگرایی", title_en="Convergence culture",
             year=2006, publisher="NYU Press", doi=None, isbn="9780814732441", url=None, language="en",
             authors="Jenkins, Henry",
             citation="Jenkins, H. (2006). Convergence culture: Where old and new media collide. NYU Press.",
             locator_type="CHAPTER", locator="ch. 2", verified=True,
             supports="ارتباطات ناهم‌زمان و مشارکتی در همگرایی رسانه‌ها."),
        dict(kind="BOOK", title_fa="نظریه‌های ارتباط انسانی", title_en="Theories of human communication",
             year=2011, publisher="Waveland Press", doi=None, isbn="9781577667063", url=None, language="en",
             authors="Littlejohn, Stephen W.; Foss, Karen A.",
             citation="Littlejohn, S. W., & Foss, K. A. (2011). Theories of human communication (10th ed.). Waveland Press.",
             locator_type="CHAPTER", locator="ch. 2", verified=True,
             supports="مدل‌های ارتباط و زمان‌بندی پیام در فرایند تولید و دریافت."),
    ],
    "CPT-207": [
        dict(kind="BOOK", title_fa="مدرنیته و هویت خود", title_en="Modernity and self-identity",
             year=1991, publisher="Polity", doi=None, isbn="9780745602345", url=None, language="en",
             authors="Giddens, Anthony",
             citation="Giddens, A. (1991). Modernity and self-identity: Self and society in the late modern age. Polity.",
             locator_type="CHAPTER", locator="ch. 3", verified=True,
             supports="مفهوم مجازی (virtuality) و حضور در غیاب فیزیکی."),
        dict(kind="BOOK", title_fa="زندگی روی صفحه", title_en="Life on the screen",
             year=1995, publisher="Simon & Schuster", doi=None, isbn="9780671526707", url=None, language="en",
             authors="Turkle, Sherry",
             citation="Turkle, S. (1995). Life on the screen: Identity in the age of the internet. Simon & Schuster.",
             locator_type="CHAPTER", locator="ch. 2", verified=True,
             supports="حضور مجازی و هویت در فضای آنلاین و روابط مبتنی بر متن."),
    ],
    "CPT-208": [
        dict(kind="BOOK", title_fa="اجتماع مجازی", title_en="The virtual community",
             year=1993, publisher="Addison-Wesley", doi=None, isbn="9780201544445", url=None, language="en",
             authors="Rheingold, Howard",
             citation="Rheingold, H. (1993). The virtual community: Homesteading on the computerized frontier. Addison-Wesley.",
             locator_type="CHAPTER", locator="ch. 1", verified=True,
             supports="اجتماع مجازی: گروه‌هایی از افراد در فضای دیجیتال که با تعامل شکل می‌گیرند."),
        dict(kind="BOOK", title_fa="فرهنگ همگرایی", title_en="Convergence culture",
             year=2006, publisher="NYU Press", doi=None, isbn="9780814732441", url=None, language="en",
             authors="Jenkins, Henry",
             citation="Jenkins, H. (2006). Convergence culture: Where old and new media collide. NYU Press.",
             locator_type="CHAPTER", locator="ch. 5", verified=True,
             supports="اجتماع‌های مجازی و مشارکت‌محور در فرهنگ همگرایی."),
    ],
    "CPT-209": [
        dict(kind="BOOK", title_fa="اجتماع مجازی", title_en="The virtual community",
             year=1993, publisher="Addison-Wesley", doi=None, isbn="9780201544445", url=None, language="en",
             authors="Rheingold, Howard",
             citation="Rheingold, H. (1993). The virtual community: Homesteading on the computerized frontier. Addison-Wesley.",
             locator_type="CHAPTER", locator="ch. 3", verified=True,
             supports="اجتماع آنلاین: شکل‌گیری هنجار، هویت و پیوند در گروه‌های برخط."),
        dict(kind="BOOK", title_fa="فرهنگ همگرایی", title_en="Convergence culture",
             year=2006, publisher="NYU Press", doi=None, isbn="9780814732441", url=None, language="en",
             authors="Jenkins, Henry",
             citation="Jenkins, H. (2006). Convergence culture: Where old and new media collide. NYU Press.",
             locator_type="CHAPTER", locator="ch. 5", verified=True,
             supports="اجتماع‌های آنلاین و فرهنگ مشارکتی مخاطبان."),
    ],
    "CPT-210": [
        dict(kind="BOOK_CHAPTER", title_fa="مبانی قدرت اجتماعی", title_en="The bases of social power",
             year=1959, publisher="University of Minnesota Press", doi=None, isbn=None, url=None, language="en",
             authors="French, John R. P.; Raven, Bertram",
             citation="French, J. R. P., & Raven, B. (1959). The bases of social power. In Studies in social power (pp. 150-167). University of Minnesota Press.",
             locator_type="CHAPTER", locator="pp. 150-167", verified=True,
             supports="مبانی و منابع نفوذ و قدرت در روابط بین‌فردی و گروهی."),
        dict(kind="BOOK", title_fa="ارتباط و اقناع: مسیرهای مرکزی و محیطی", title_en="Communication and persuasion: Central and peripheral routes to attitude change",
             year=1986, publisher="Springer-Verlag", doi=None, isbn="9780387904254", url=None, language="en",
             authors="Petty, Richard E.; Cacioppo, John T.",
             citation="Petty, R. E., & Cacioppo, J. T. (1986). Communication and persuasion: Central and peripheral routes to attitude change. Springer-Verlag.",
             locator_type="CHAPTER", locator="ch. 3", verified=True,
             supports="فرایندهای اقناع و نفوذ بر نگرش از طریق مسیرهای مرکزی و محیطی."),
    ],
}

ENRICH = {
    "CPT-206": dict(
        summary="ارتباطات ناهم‌زمان (Asynchronous Communication) به فرایند تولید، ارسال و دریافت پیام است که فرستنده و گیرنده، لازم نیست در یک زمان مشترک فعال باشند؛ یعنی پیام، «برای دریافت در زمان دیگری» ارسال می‌شود. در سنت نظریه‌های ارتباط، ارتباطات ناهم‌زمان بر ویژگی‌هایی چون: (۱) جدایی زمانی: ارسال و دریافت، از نظر زمانی جدا هستند؛ (۲) تأمل: فرستنده می‌تواند پیام را بسازد و گیرنده، فرصت پاسخ‌دهی دارد؛ (۳) انعطاف زمانی: طرفین، در زمان مناسب خود، دریافت و پاسخ می‌دهند؛ (۴) ماندگاری: پیام، تا زمان پاسخ، ذخیره می‌ماند (Jenkins, 2006; Littlejohn & Foss, 2011). در سنت همگرایی، ارتباطات ناهم‌زمان، به مشارکت و گفت‌وگوی پراکنده در زمان و مکان می‌انجامد (Jenkins, 2006). پژوهش‌ها نشان می‌دهند ارتباطات ناهم‌زمان بر «کیفیت پیام»، «دسترسی زمانی» و «مشارکت» اثر عمیق دارد. نمونه‌های رایج ارتباطات ناهم‌زمان: ایمیل، تابلوهای گفت‌وگو و انجمن‌ها، ارسال پیام صوتی و ویدئویی، کامنت‌ها و نوتیفیکیشن‌ها، و پست‌های شبکه‌های اجتماعی. نقد بنیادین، «ناهم‌زمانی‌زدگی» (asynchrony-ism) است: فرض بر این است که ناهم‌زمانی، «همیشه کارآمدتر» است، در حالی که در واقع آن، «تأخیر و گسست فوری» می‌آورد و تفاوت، «درجه‌ای» است نه «ماهوی» (Littlejohn & Foss, 2011).",
        mechanism="ارتباطات ناهم‌زمان در چهار حلقه عمل می‌کند: (۱) تولید پیام: فرستنده، در زمان مناسب خود، پیام را می‌سازد و ارسال می‌کند؛ (۲) ذخیره و انتقال: پیام، در بستر (ایمیل، انجمن، پیام‌رسان) ذخیره و منتقل می‌شود؛ (۳) دریافت تأخیری: گیرنده، در زمان مناسب خود، پیام را دریافت و پردازش می‌کند؛ (۴) پاسخ تأمل‌شده: گیرنده، پس از تأمل، پاسخ می‌دهد که به‌نوبه‌خود پیام ناهم‌زمانی است (Jenkins, 2006; Littlejohn & Foss, 2011). این چرخه، تعامل را از قید زمان هم‌زمان رها می‌کند.",
        key_concepts=["جدایی زمانی", "تأمل و بازخوانی", "انعطاف زمانی", "ماندگاری پیام", "مشارکت پراکنده"],
        critiques="الگوی ناهم‌زمان، آن را «همیشه کارآمدتر» نشان می‌دهد، در حالی که در واقع آن، «تأخیر» و «گسست فوری» می‌آورد و تفاوت، «درجه‌ای» است نه «ماهوی» (Littlejohn & Foss, 2011). نقد دیگر، «فقدان هم‌حضور» است: ناهم‌زمانی، سیگنال‌های غیرکلامی (لحن، حال) را می‌کاهد و بر اعتماد و درک عاطفی اثر می‌گذارد (Jenkins, 2006). همچنین «تأخیر در پاسخ» می‌تواند ارتباط را قطع، تعهد را کاهش و در برخی موارد به سوءتفاهم و کاهش انگیزه مشارکت بینجامد.",
        applications="طراحی خدمات ارتباطی ناهم‌زمان (ایمیل، انجمن، پیام‌رسانی، ویدئو/صوت تأخیری)، طراحی تجربه تعاملی (تأمل، ماندگاری، انعطاف زمانی)، تحلیل گفت‌وگو و مشارکت در فضای برخط (کیفیت پیام، درگیری)، آموزش ارتباط مؤثر (بازنویسی، تأمل، مدیریت انتظار)، و طراحی پلتفرم‌های گفت‌وگو و آموزش (نظارت، بازخورد تأخیری، کار گروهی پراکنده) (Jenkins, 2006; Littlejohn & Foss, 2011).",
        evolution="مفهوم ارتباطات ناهم‌زمان از پست و تلگراف (قرن نوزدهم) و سپس ایمیل (دهه‌های ۱۹۷۰–۱۹۹۰) وارد علوم ارتباط شد؛ با وب‌بورد و انجمن‌های آنلاین (دههٔ ۱۹۹۰)، «گفت‌وگوی پراکنده در زمان و مکان» شکل گرفت؛ در عصر دیجیتال، ارتباطات ناهم‌زمان به «مکمل اصلی» ارتباطات هم‌زمان و زیرساخت مشارکت و گفت‌وگوی عمومی بدل شده است (Jenkins, 2006).",
        assumptions="فرض‌های نهفته: فرستنده و گیرنده، نیازی به حضور هم‌زمان ندارند و پیام، تا زمان دریافت، حفظ می‌ماند؛ طرفین، در زمان مناسب خود، می‌توانند دریافت و پاسخ دهند؛ و ناهم‌زمانی، امکان تأمل، بازخوانی و مشارکت پراکنده می‌سازد؛ اما در دسترس بودن، هنجارهای پاسخ‌دهی و بستر مناسب، از پیش‌فرض‌هایی هستند که در عمل محدود و قابل نقض‌اند (Jenkins, 2006; Littlejohn & Foss, 2011).",
    ),
    "CPT-207": dict(
        summary="حضور مجازی (Virtual Presence) به تجربه حس‌کردن حضور فرد، هویت یا نهاد در فضایی است که در آن حضور فیزیکی وجود ندارد؛ یعنی «حضور در غیابِ حضور». در سنت جامعه‌شناختی، حضور مجازی بر ویژگی‌هایی چون: (۱) مجازی بودن: حضور، بدون مکان فیزیکی و به‌واسطه نماد، متن و تصویر شکل می‌گیرد؛ (۲) نمادین: هویت، از طریق آواتار، نام کاربری و محتوا بازتاب می‌شود؛ (۳) درک‌پذیری: مخاطب، فرد را «حاضر» می‌پندارد و با او ارتباط برقرار می‌کند؛ (۴) تعاملی: حضور، با پاسخ‌دهی و تعامل تقویت می‌شود (Giddens, 1991; Turkle, 1995). در سنت هویت‌محور، حضور مجازی، شکل‌گیری «هویت آنلاین» و روابط مبتنی بر متن را بازتاب می‌دهد (Turkle, 1995). پژوهش‌ها نشان می‌دهند حضور مجازی بر «ارتباط»، «اعتماد» و «هویت» اثر عمیق دارد. نمونه‌های رایج حضور مجازی: پروفایل‌ها و آواتارها، ویدئوکال و استریم زنده، شخصیت‌های مجازی و دیجیتال‌توین، و حضور سازمانی در شبکه‌های اجتماعی. نقد بنیادین، «مجازی‌زدگی» (virtual-presence-ism) است: فرض بر این است که حضور مجازی، «معادل کامل» حضور فیزیکی است، در حالی که در واقع آن، «حضور ناقص و نمادین» است و تفاوت، «درجه‌ای» است نه «ماهوی» (Giddens, 1991).",
        mechanism="حضور مجازی در چهار حلقه شکل می‌گیرد: (۱) نمادسازی: فرد یا نهاد، هویت خود را از طریق متن، تصویر و آواتار نمادین می‌کند؛ (۲) نمایش: حضور، در بستر دیجیتال به مخاطب نمایش داده می‌شود؛ (۳) ادراک حضور: مخاطب، آن را «حضور فعال» ادراک و با آن تعامل می‌کند؛ (۴) تقویت تعامل: پاسخ‌دهی و تعامل مستمر، حس حضور را قوی‌تر و پایدارتر می‌کند (Giddens, 1991; Turkle, 1995). این چرخه، حضور را بدون مکان فیزیکی ممکن می‌سازد.",
        key_concepts=["مجازی بودن", "نمادین بودن", "هویت آنلاین", "ادراک حضور", "تعاملی بودن"],
        critiques="الگوی حضور مجازی، آن را «معادل کامل» حضور فیزیکی نشان می‌دهد، در حالی که در واقع آن، «حضور ناقص و نمادین» است و تفاوت، «درجه‌ای» است نه «ماهوی» (Giddens, 1991). نقد دیگر، «هویت‌زدگی مجازی» (virtual identity-ism) است: حضور مجازی، هویت را قابل‌تغییر و قابل‌پنهان‌سازی می‌کند و بر صداقت و اعتماد اثر می‌گذارد (Turkle, 1995). همچنین «عمقِ» حضور مجازی، به‌سختی قابل اندازه‌گیری است و در موارد حساس (بهداشتی، آموزشی) نمی‌تواند جای حضور فیزیکی را بگیرد.",
        applications="طراحی تجربه‌های حضور مجازی (ویدئوکال، استریم، آواتار، دیجیتال‌توین)، طراحی هویت آنلاین و برند شخصی (پروفایل، آواتار، لحن)، تحلیل اعتماد و ارتباط در فضای مجازی، آموزش حضور مؤثر آنلاین (لحن، پاسخ‌دهی، همدلی)، و طراحی پلتفرم‌های تعاملی (حضور زنده، بازخورد، هم‌حضور) (Giddens, 1991; Turkle, 1995).",
        evolution="مفهوم حضور مجازی از جامعه‌شناسی مدرنیته و مفهوم «مجازی‌بودن» (دهه‌های ۱۹۸۰–۱۹۹۰، گیدنز) وارد علوم شد؛ با رایانه‌ها و وب (دهه‌های ۱۹۹۰–۲۰۰۰)، «هویت و حضور آنلاین» شکل گرفت؛ در عصر دیجیتال، حضور مجازی به «معیار معمول» حضور اجتماعی و سازمانی بدل شده و با واقعیت مجازی و هوش مصنوعی، عمیق‌تر شده است (Turkle, 1995).",
        assumptions="فرض‌های نهفته: حضور، بدون مکان فیزیکی و از طریق نماد و متن ممکن است؛ مخاطب، نماد را «حضور فعال» ادراک و با آن ارتباط برقرار می‌کند؛ و حضور مجازی، روابط و اعتماد را بازتولید می‌کند؛ اما یکسان‌بودن با حضور فیزیکی، عمق، صداقت و درک عاطفی، از پیش‌فرض‌هایی هستند که در عمل محدود و قابل نقض‌اند (Giddens, 1991; Turkle, 1995).",
    ),
    "CPT-208": dict(
        summary="اجتماع مجازی (Virtual Community) به گروهی از افراد می‌گویند که در فضای دیجیتال گرد هم می‌آیند و بر پایۀ تعامل، علایق، هدف یا هویت مشترک، پیوند می‌سازند؛ «گروهی که بدون مکان فیزیکی، به هم نزدیک‌اند». در سنت مطالعات جامعه مجازی، آن بر ویژگی‌هایی چون: (۱) پیوند برخط: اعضای گروه، از طریق رسانه دیجیتال با یکدیگر ارتباط برقرار می‌کنند؛ (۲) هویت مشترک: علایق، هدف یا هویت مشترک، گروه را گرد هم می‌آورد؛ (۳) هنجارهای گروهی: گروه، هنجارها، زبان و نقش‌های خود را شکل می‌دهد؛ (۴) حس تعلق: اعضا، حس تعلق و مشارکت در گروه را تجربه می‌کنند (Rheingold, 1993; Jenkins, 2006). در سنت همگرایی، اجتماع‌های مجازی، به مشارکت و فرهنگ مخاطبان می‌انجامد (Jenkins, 2006). پژوهش‌ها نشان می‌دهند اجتماع مجازی بر «تعهد»، «مشارکت» و «پشتیباری اجتماعی» اثر عمیق دارد. نمونه‌های رایج: انجمن‌های آنلاین، گروه‌های علاقه‌مند، جامعه‌های بازی‌کنندگان، و گروه‌های حمایتی برخط. نقد بنیادین، «اجتماعی‌زدگی مجازی» (virtual-community-ism) است: فرض بر این است که اجتماع مجازی، «معادل کامل» اجتماع فیزیکی است، در حالی که در واقع آن، «غیرحضوری و مقید به بستر» است و تفاوت، «درجه‌ای» است نه «ماهوی» (Rheingold, 1993).",
        mechanism="اجتماع مجازی در چهار حلقه شکل می‌گیرد: (۱) گردآمدن: افرادی با علاقه یا هدف مشترک، در فضای دیجیتال گرد هم می‌آیند؛ (۲) تعامل: اعضا، از طریق گفت‌وگو، محتوا و فعالیت، با یکدیگر تعامل می‌کنند؛ (۳) هنجارسازی: گروه، هنجارها، زبان، نقش‌ها و ساختار خود را شکل می‌دهد؛ (۴) تعلق و تعهد: حس تعلق، تعهد و مشارکت اعضای گروه را تقویت و پایدار می‌کند (Rheingold, 1993; Jenkins, 2006). این چرخه، گروه را به جامعه پایدار بدل می‌کند.",
        key_concepts=["پیوند برخط", "هویت مشترک", "هنجارهای گروهی", "حس تعلق", "پشتیباری اجتماعی"],
        critiques="الگوی اجتماع مجازی، آن را «معادل کامل» اجتماع فیزیکی نشان می‌دهد، در حالی که در واقع آن، «غیرحضوری» و «مقید به بستر دیجیتال» است و تفاوت، «درجه‌ای» است نه «ماهوی» (Rheingold, 1993). نقد دیگر، «مشارکت ناهمگون» (participation inequality) است: بخش کوچکی از اعضا، بیشتر تولیدکنندۀ محتوا و تعادل در مشارکت وجود ندارد (Jenkins, 2006). همچنین «پایداری» و «عمق پیوندها» در اجتماع مجازی، به‌سختی تضمین و اندازه‌گیری می‌شود.",
        applications="طراحی و مدیریت اجتماعات مجازی (هنجار، تعلق، مشارکت)، طراحی تجربه کاربری مشارکتی (تعامل، هویت، تعلق)، تحلیل تعهد و درگیری مخاطبان (پشتیباری اجتماعی، بازاریابی)، آموزش سواد رسانه‌ای و اجتماعی (برخورد امن، هنجار، احترام)، و طراحی پلتفرم‌های اجتماعی (نقش‌ها، پاداش، مدیریت هنجار) (Rheingold, 1993; Jenkins, 2006).",
        evolution="مفهوم اجتماع مجازی از نخستین گروه‌های آنلاین و انجمن‌های برخط (دهه‌های ۱۹۷۰–۱۹۹۰، راینگولد) وارد علوم شد؛ با وب 2.0 و شبکه‌های اجتماعی (دهه‌های ۲۰۰۰–۲۰۱۰)، به «پدیدهٔ رایج» تبدیل شد؛ در عصر دیجیتال، اجتماع‌های مجازی به «زیرساخت اصلی» مشارکت، فرهنگ، هویت و تولید معنا بدل شده‌اند و با الگوریتم‌های پیشنهاد، عمیق‌تر در بستر پلتفرم‌ها جای گرفته‌اند (Jenkins, 2006).",
        assumptions="فرض‌های نهفته: افراد، می‌توانند بدون مکان فیزیکی، بر پایه علاقه یا هویت مشترک، پیوند سازند؛ تعامل برخط، هنجار، تعلق و تعهد بازتولید می‌کند؛ و اجتماع مجازی، حمایت اجتماعی و مشارکت می‌آفریند؛ اما پایداری، عمق پیوند و برابری مشارکت، از پیش‌فرض‌هایی هستند که در عمل محدود و قابل نقض‌اند (Rheingold, 1993; Jenkins, 2006).",
    ),
    "CPT-209": dict(
        summary="اجتماع آنلاین (Online Community) به گروهی از کاربران می‌گویند که به‌طور مستمر در یک بستر دیجیتال (وب‌سایت، اپلیکیشن، پلتفرم) گرد هم می‌آیند، بر پایه موضوع یا برند مشترک تعامل می‌کنند و هویت و هنجارهای گروهی می‌سازند. در سنت مطالعات مخاطبان، آن بر ویژگی‌هایی چون: (۱) بستر مشخص: جامعه، روی یک پلتفرم یا وب‌سایت خاص شکل می‌گیرد؛ (۲) موضوع‌محوری: یک موضوع، برند، محصول یا علاقه، اعضای آن را گرد هم می‌آورد؛ (۳) تعامل مستمر: اعضا، به‌طور مداوم محتوا و تعامل تولید می‌کنند؛ (۴) هنجار و نقش: گروه، هنجارها، زبان و نقش‌های عضو و رهبر را شکل می‌دهد (Rheingold, 1993; Jenkins, 2006). در سنت همگرایی، اجتماعات آنلاین، به «فرهنگ مشارکتی» مخاطبان منجر می‌شوند (Jenkins, 2006). پژوهش‌ها نشان می‌دهند اجتماع آنلاین بر «تعهد برند»، «درگیری مخاطب» و «کلمه به کلمه» اثر عمیق دارد. نمونه‌های رایج: جامعه‌های برخط محصولات و برندها، گروه‌های طرفداران (fan communities)، انجمن‌های تخصصی و گروه‌های کاربری پلتفرم‌ها. نقد بنیادین، «آنلاینی‌زدگی» (online-community-ism) است: فرض بر این است که جامعه آنلاین، «همیشگی و پایدار» است، در حالی که در واقع آن، «وابسته به بستر و مدیریت» است و تفاوت، «درجه‌ای» است نه «ماهوی» (Rheingold, 1993).",
        mechanism="اجتماع آنلاین در چهار حلقه شکل می‌گیرد: (۱) شکل‌گیری در بستر: کاربران، روی یک پلتفرم یا وب‌سایت، گرد هم می‌آیند؛ (۲) تعامل موضوع‌محور: بر پایه موضوع یا برند مشترک، محتوا و گفت‌وگو تولید می‌شود؛ (۳) هنجارسازی: گروه، هنجارها، نقش‌ها و زبان مشترک خود را شکل می‌دهد؛ (۴) پایداری و رشد: تعامل مستمر، تعهد و مشارکت اعضا را افزایش و جامعه را رشد می‌دهد (Rheingold, 1993; Jenkins, 2006). این چرخه، گروه را به جامعه آنلاین فعال بدل می‌کند.",
        key_concepts=["بستر مشخص", "موضوع‌محوری", "تعامل مستمر", "هنجار و نقش", "تعهد برند"],
        critiques="الگوی جامعه آنلاین، آن را «همیشگی و پایدار» نشان می‌دهد، در حالی که در واقع آن، «وابسته به بستر و مدیریت فعال» است و تفاوت، «درجه‌ای» است نه «ماهوی» (Rheingold, 1993). نقد دیگر، «تولید ناهمگون» (uneven production) است: بخش کوچکی از اعضا، بخش بزرگی از محتوا و تعهد را تولید می‌کنند و تعادل مشارکت وجود ندارد (Jenkins, 2006). همچنین «نقش پلتفرم» در کنترل هنجار و حذف، بر آزادی و تنوع جامعه اثر می‌گذارد و پایداری آن به سرمایه‌گذاری مستمر وابسته است.",
        applications="طراحی و مدیریت جامعه آنلاین (هنجار، تعلق، درگیری)، بازاریابی و برندسازی مجتمعی (تعهد، کلمه به کلمه، وکالت مخاطب)، تحلیل درگیری و تعهد مخاطبان (مشارکت، تعامل)، آموزش مدیریت جامعه و ارتباط با مخاطب (نقش، پاسخ‌دهی، اعتمادسازی)، و طراحی پلتفرم‌های اجتماعی (پاداش، نقش‌ها، مدیریت هنجار) (Rheingold, 1993; Jenkins, 2006).",
        evolution="مفهوم جامعه آنلاین از انجمن‌های برخط و گروه‌های کاربری (دهه‌های ۱۹۹۰) وارد علوم شد؛ با وب 2.0 و شبکه‌های اجتماعی (دهه‌های ۲۰۰۰–۲۰۱۰)، به «ابزار اصلی» بازاریابی و مشارکت تبدیل شد؛ در عصر دیجیتال، جامعه آنلاین به «زیرساخت» برند، اعتماد و فرهنگ مشارکتی بدل شده و با الگوریتم‌ها، عمیق‌تر در بستر پلتفرم جای گرفته و به ابزار اصلی برندسازی، اعتمادسازی و گفت‌وگوی عمومی بدل شده است (Jenkins, 2006).",
        assumptions="فرض‌های نهفته: کاربران، روی یک بستر مشخص، بر پایه موضوع مشترک گرد هم می‌آیند و تعامل مستمر، هویت و هنجار بازتولید می‌کند؛ و جامعه آنلاین، تعهد، مشارکت و اعتماد می‌آفریند؛ اما پایداری، برابری مشارکت و استقلال از بستر و پلتفرم، از پیش‌فرض‌هایی هستند که در عمل محدود، وابسته و قابل نقض‌اند (Rheingold, 1993; Jenkins, 2006).",
    ),
    "CPT-210": dict(
        summary="نفوذ (Influence) به توانایی فرد، گروه یا رسانه است که بر نگرش، باور یا رفتار دیگری اثر می‌گذارد و آن را به سمت تغییر هدایت کند؛ «تأثیر بر دیگری برای تغییر نگرش یا عمل». در سنت روان‌شناسی اجتماعی، نفوذ بر ویژگی‌هایی چون: (۱) منبع نفوذ: نفوذ، از یک منبع (فرد، رسانه، نهاد) صادر می‌شود؛ (۲) مبانی قدرت: نفوذ، بر مبانی قدرت (کار، اجبار، جایزه، مشروعیت، تخصص، الهام) استوار است؛ (۳) فرایند اقناع: نفوذ، از طریق اقناع، تفسیر و تعامل رخ می‌دهد؛ (۴) پذیرش یا انکار: هدف‌گرفته، ممکن است نفوذ را بپذیرد، مقاومت کند یا با آن تعامل کند (French & Raven, 1959; Petty & Cacioppo, 1986). در سنت اقناع‌محور، نفوذ، از مسیرهای مرکزی (محتوایی) و محیطی (منبعی) شکل می‌گیرد (Petty & Cacioppo, 1986). پژوهش‌ها نشان می‌دهند نفوذ بر «تغییر نگرش»، «پذیرش پیام» و «رفتار» اثر عمیق دارد. نمونه‌های رایج نفوذ: رهبران و نظیرین موثر (influencer)، منابع خبری و رسانه‌ای، تبلیغات و کمپین‌های اجتماعی، و پیام‌های رهبران سازمانی. نقد بنیادین، «نفوذزدگی» (influence-ism) است: فرض بر این است که نفوذ، «همیشه موفق و یک‌جهت» است، در حالی که در واقع آن، «وابسته به زمینه و زمینه‌پذیر» است و تفاوت، «درجه‌ای» است نه «ماهوی» (Petty & Cacioppo, 1986).",
        mechanism="نفوذ در چهار حلقه عمل می‌کند: (۱) صدور پیام: منبع، پیام، نماد یا رفتار را صادر می‌کند؛ (۲) پردازش: هدف‌گرفته، پیام را از مسیر مرکزی (محتوا، استدلال) یا محیطی (اعتبار، جذابیت، تکرار) پردازش می‌کند؛ (۳) ارزیابی: بر پایه پردازش، نگرش، باور یا قصد شکل می‌گیرد؛ (۴) پذیرش یا مقاومت: هدف‌گرفته، تغییر را می‌پذیرد، با آن تعامل می‌کند یا مقاومت می‌نماید (French & Raven, 1959; Petty & Cacioppo, 1986). این چرخه، نفوذ را فرایندی دوطرفه و زمینه‌ای می‌سازد.",
        key_concepts=["مبانی قدرت", "اقناع", "مسیر مرکزی و محیطی", "پذیرش و مقاومت", "زمینه‌پذیری"],
        critiques="الگوی نفوذ، آن را «همیشه موفق و یک‌جهت» نشان می‌دهد، در حالی که در واقع آن، «وابسته به زمینه» و «دو‌جهت» است و تفاوت، «درجه‌ای» است نه «ماهوی» (Petty & Cacioppo, 1986). نقد دیگر، «نقش زمینه» (situational contingency) است: نفوذ، به انگیزه، توانایی و نوع مخاطب بستگی دارد و یک منبع، در زمینه‌های مختلف، اثر متفاوتی دارد (French & Raven, 1959). همچنین «مقاومت و واکنش معکوس» (boomerang) ممکن است نفوذ را به نتیجه برعکس برساند و اثر نفوذ، به‌سختی از اثر عوامل دیگر تفکیک می‌شود.",
        applications="طراحی استراتژی‌های اقناع و تأثیرگذاری (رهبری، بازاریابی، کمپین اجتماعی)، تحلیل قدرت و نفوذ رسانه‌ای و نظیرین موثر، مدیریت ارتباط و اعتمادسازی (منبع، محتوا، لحن)، آموزش روان‌شناسی اجتماعی و اقناع (مبانی قدرت، مسیرهای پردازش)، و طراحی پیام‌های اجتماعی و تبلیغاتی (محتوا، اعتبار، تکرار) (French & Raven, 1959; Petty & Cacioppo, 1986).",
        evolution="مفهوم نفوذ از مطالعات قدرت و اقناع (دهه‌های ۱۹۵۰–۱۹۶۰، فرنچ و راون) وارد علوم ارتباط شد؛ با نظریۀ مسیرهای پردازش (دههٔ ۱۹۸۰، پتی و کازیوپو)، «پردازش پیام» در مرکز قرار گرفت؛ در عصر شبکه‌ها و نظیرین موثر (دهه‌های ۲۰۱۰–۲۰۲۰)، نفوذ به «پدیدهٔ توزیع‌شده و تعاملی» بدل شده است (Petty & Cacioppo, 1986).",
        assumptions="فرض‌های نهفته: منبع، می‌تواند از طریق پیام یا رفتار، بر نگرش و رفتار دیگری اثر بگذارد؛ و نفوذ، از طریق مبانی قدرت و فرایند اقناع رخ می‌دهد؛ هدف‌گرفته، پیام را پردازش و بر آن واکنش نشان می‌دهد؛ اما موفقیت نفوذ، به انگیزه، توانایی و زمینه بستگی دارد و یک‌جهت و همیشگی نیست (French & Raven, 1959; Petty & Cacioppo, 1986).",
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
        p["sources"] = p.get("sources", []) or []
        p["citations"] = p.get("citations", []) or []
        have_src = {s.get("citation") for s in p["sources"] if isinstance(s, dict)}
        have_cit = {c.get("source") for c in p["citations"] if isinstance(c, dict)}
        for src in S[code]:
            if src["citation"] not in have_src:
                p["sources"].append({
                    "citation": src["citation"], "title_en": src["title_en"],
                    "title_fa": src["title_fa"], "year": src["year"], "doi": src.get("doi"),
                    "url": src.get("url"), "language": src["language"], "verified": src["verified"],
                })
                have_src.add(src["citation"])
            if src["citation"] not in have_cit:
                p["citations"].append({
                    "source": src["citation"], "locator": src["locator"],
                    "supports": src["supports"], "verified": src["verified"],
                })
                have_cit.add(src["citation"])
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
                    (code, json.dumps({"batch": BATCH, "score": score, "words": words,
                                       "sources": n_sources, "verified": n_verified,
                                       "relations": n_rel, "rubric": detail}, ensure_ascii=False), STAMP, NOW))
        print(code, "words", words, "score", score, "detail", detail)
    conn.commit()
    conn.close()
    print("BATCH%d DONE" % BATCH)


if __name__ == "__main__":
    main()
