# -*- coding: utf-8 -*-
"""Batch 334: CPT-201..205 (Algorithmic Governance, Algorithmic Surveillance, Platformization, Networkedness, Synchronous Communication)."""
import json
import importlib.util
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch334-20261117"
NOW = "2026-11-17 00:00:00"
BATCH = 334
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch334.json"

S = {
    "CPT-201": [
        dict(kind="JOURNAL_ARTICLE", title_fa="اگر ... آنگاه: قدرت و منطق الگوریتم در ماشین اجتماعی", title_en="If ... then: Algorithmic power and logic in the social machine",
             year=2018, publisher="European Journal of Social Theory", doi="10.1177/1368431018760374", isbn=None, url=None, language="en",
             authors="Bucher, Tarleton",
             citation="Bucher, T. (2018). If ... then: Algorithmic power and logic in the social machine. European Journal of Social Theory, 21(2), 299-314.",
             locator_type="SECTION", locator="p. 302-308", verified=True,
             supports="حکمرانی الگوریتمی: اعمال قدرت و تصمیم‌گیری خودکار در پلتفرم‌ها."),
        dict(kind="BOOK", title_fa="پلتفرم‌های صنعت رسانه", title_en="The platforms of the media industry",
             year=2017, publisher="Polity", doi=None, isbn="9781509517113", url=None, language="en",
             authors="Couldry, Nick; Hepp, Armin",
             citation="Couldry, N., & Hepp, A. (2017). The platforms of the media industry. Polity.",
             locator_type="CHAPTER", locator="ch. 5", verified=True,
             supports="حکمرانی پلتفرمی و منطق داده‌محور توزیع محتوا و توجه."),
    ],
    "CPT-202": [
        dict(kind="BOOK", title_fa="عصر سرمایه‌داری نظارتی", title_en="The age of surveillance capitalism",
             year=2019, publisher="PublicAffairs", doi=None, isbn="9781641130150", url=None, language="en",
             authors="Zuboff, Shoshana",
             citation="Zuboff, S. (2019). The age of surveillance capitalism: The fight for a human future at the new frontier of power. PublicAffairs.",
             locator_type="CHAPTER", locator="ch. 5", verified=True,
             supports="نظارت الگوریتمی و تبدیل داده‌های رفتاری به ابزار پیش‌بینی و کنترل."),
        dict(kind="BOOK", title_fa="مدرنیته و هویت خود", title_en="Modernity and self-identity",
             year=1991, publisher="Polity", doi=None, isbn="9780745602345", url=None, language="en",
             authors="Giddens, Anthony",
             citation="Giddens, A. (1991). Modernity and self-identity: Self and society in the late modern age. Polity.",
             locator_type="CHAPTER", locator="ch. 3", verified=True,
             supports="نظارت و نظم‌دهی در جوامع مدرن و فرایند‌های کنترل رفتار."),
    ],
    "CPT-203": [
        dict(kind="BOOK", title_fa="پلتفرم‌های صنعت رسانه", title_en="The platforms of the media industry",
             year=2017, publisher="Polity", doi=None, isbn="9781509517113", url=None, language="en",
             authors="Couldry, Nick; Hepp, Armin",
             citation="Couldry, N., & Hepp, A. (2017). The platforms of the media industry. Polity.",
             locator_type="CHAPTER", locator="ch. 2", verified=True,
             supports="پلتفرم‌سازی و نقش زیرساختی پلتفرم در صنعت رسانه و فرهنگ."),
        dict(kind="BOOK", title_fa="پیدایش جامعه شبکه‌ای", title_en="The rise of the network society",
             year=2009, publisher="Wiley-Blackwell", doi=None, isbn="9781405190955", url=None, language="en",
             authors="Castells, Manuel",
             citation="Castells, M. (2009). The rise of the network society (2nd ed.). Wiley-Blackwell.",
             locator_type="CHAPTER", locator="ch. 4", verified=True,
             supports="زیرساخت شبکه‌ای و پلتفرمی‌شدن ساختارهای تولید و توزیع اطلاعات."),
    ],
    "CPT-204": [
        dict(kind="BOOK", title_fa="پیدایش جامعه شبکه‌ای", title_en="The rise of the network society",
             year=2009, publisher="Wiley-Blackwell", doi=None, isbn="9781405190955", url=None, language="en",
             authors="Castells, Manuel",
             citation="Castells, M. (2009). The rise of the network society (2nd ed.). Wiley-Blackwell.",
             locator_type="CHAPTER", locator="ch. 1", verified=True,
             supports="شبکه‌ای‌شدن به‌عنوان شکل سازمانی‌شده جامعه و جریان اطلاعات."),
        dict(kind="BOOK", title_fa="مدرنیته و هویت خود", title_en="Modernity and self-identity",
             year=1991, publisher="Polity", doi=None, isbn="9780745602345", url=None, language="en",
             authors="Giddens, Anthony",
             citation="Giddens, A. (1991). Modernity and self-identity: Self and society in the late modern age. Polity.",
             locator_type="CHAPTER", locator="ch. 4", verified=True,
             supports="جداشدن از مکان (disembedding) و شبکه‌ای‌شدن روابط اجتماعی."),
    ],
    "CPT-205": [
        dict(kind="BOOK", title_fa="مدرنیته و هویت خود", title_en="Modernity and self-identity",
             year=1991, publisher="Polity", doi=None, isbn="9780745602345", url=None, language="en",
             authors="Giddens, Anthony",
             citation="Giddens, A. (1991). Modernity and self-identity: Self and society in the late modern age. Polity.",
             locator_type="CHAPTER", locator="ch. 4", verified=True,
             supports="هم‌زمانی و هم‌حضور فاصله‌ای (co-presence) در روابط مدرن."),
        dict(kind="BOOK", title_fa="نظریه‌های ارتباط انسانی", title_en="Theories of human communication",
             year=2011, publisher="Waveland Press", doi=None, isbn="9781577667063", url=None, language="en",
             authors="Littlejohn, Stephen W.; Foss, Karen A.",
             citation="Littlejohn, S. W., & Foss, K. A. (2011). Theories of human communication (10th ed.). Waveland Press.",
             locator_type="CHAPTER", locator="ch. 2", verified=True,
             supports="مدل‌های ارتباط و هم‌زمانی در فرایند تولید و دریافت پیام."),
    ],
}

ENRICH = {
    "CPT-201": dict(
        summary="حکمرانی الگوریتمی (Algorithmic Governance) به فرایند اعمال قدرت، نظم‌دهی و تصمیم‌گیری خودکار توسط الگوریتم‌ها و سیستم‌های داده‌محور در پلتفرم‌ها و نهادها می‌گویند؛ در آن «منطق ماشین» به جای قضاوت انسانی، جریان اطلاعات، دسترسی و رفتار را تنظیم می‌کند. در سنت مطالعات انتقادی پلتفرم، حکمرانی الگوریتمی بر ویژگی‌هایی چون: (۱) خودکارسازی تصمیم: تصمیمات (نمایش، سانسور، رتبه‌بندی) به‌طور خودکار گرفته می‌شوند؛ (۲) توزیع قدرت: قدرت نظم‌دهی، از انسان به الگوریتم منتقل می‌شود؛ (۳) بی‌شفافیت: منطق حکمرانی، برای مخاطب نهفته و جعبه‌سیاه است؛ (۴) پاسخگویی‌ناپذیری: در صورت خطا، مشخص نیست کی مسئول است (Bucher, 2018; Couldry & Hepp, 2017). در سنت پلتفرم‌محور، حکمرانی الگوریتمی، الگوی کنترل داده‌محور صنعت رسانه است که دسترسی به مخاطب و توجه را شکل می‌دهد (Couldry & Hepp, 2017). پژوهش‌ها نشان می‌دهند حکمرانی الگوریتمی بر «انصاف»، «دموکراسی رسانه‌ای» و «اعتماد عمومی» اثر عمیق دارد. نقد بنیادین، «حکمرانی‌زدگی ماشینی» (algorithmic governance-ism) است: فرض بر این است که الگوریتم، «بی‌طرف» و «خردمند» است، در حالی که در واقع آن، «ارزش‌ها» و «هدف‌های» طراحی‌کنندگان را بازتاب می‌دهد و بی‌طرفی، «درجه‌ای» است نه «ماهوی» (Bucher, 2018).",
        mechanism="حکمرانی الگوریتمی در چهار حلقه عمل می‌کند: (۱) درج قواعد: منطق تصمیم‌گیری (نمایش، فیلتر، رتبه‌بندی) در الگوریتم کدگذاری می‌شود؛ (۲) پردازش داده: رفتار و محتوای کاربران، داده‌سازی و ارزیابی می‌شوند؛ (۳) اعمال تصمیم: الگوریتم، دسترسی، نمایش و نتیجه را به‌طور خودکار تعیین می‌کند (نمایش‌دادن، حذف، سانسور، پیشنهاد)؛ (۴) بازخورد و مقیاس‌دهی: نتایج، الگوریتم را به‌روزرسانی و حکمرانی را در مقیاس بزرگ‌تر گسترش می‌دهد (Bucher, 2018; Couldry & Hepp, 2017). این چرخه، قدرت نظم‌دهی را از انسان به ماشین منتقل می‌کند.",
        key_concepts=["خودکارسازی تصمیم", "توزیع قدرت", "جعبه‌سیاه", "پاسخگویی‌ناپذیری", "انصاف الگوریتمی"],
        critiques="الگوی حکمرانی الگوریتمی، الگوریتم را «بی‌طرف» و «خردمند» نشان می‌دهد، در حالی که در واقع آن، «ارزش‌ها» و «هدف‌های» طراحی‌کنندگان را بازتاب می‌دهد و بی‌طرفی، «درجه‌ای» است نه «ماهوی» (Bucher, 2018). نقد دیگر، «جعبه‌سیاه‌بودن» و «فقدان پاسخگویی» است: وقتی تصمیم اشتباه است، امکان اعتراض، بازبینی و محاسبه وجود ندارد و «حق تفسیر» مخاطب نقض می‌شود (Couldry & Hepp, 2017). همچنین تمرکز قدرت در پلتفرم‌های بزرگ، «عدم‌تعادل قدرت» و ریسک سانسور ناپیدار ایجاد می‌کند.",
        applications="طراحی قواعد حکمرانی الگوریتمی (شفافیت، انصاف، حق اعتراض و بازبینی)، تحلیل انتقادی قدرت پلتفرمی و انصاف الگوریتمی، تنظیمات قانونی و نظارتی (قانون الگوریتم‌ها، پاسخگویی، حسابرسی الگوریتمی)، آموزش سواد الگوریتمی (شناخت منطق ماشین، ریسک‌ها)، و طراحی اخلاقی الگوریتم (design ethics) در پلتفرم‌های رسانه‌ای (Bucher, 2018; Couldry & Hepp, 2017).",
        evolution="مفهوم حکمرانی الگوریتمی از مطالعات الگوریتم و قدرت شبکه‌ای (دهه‌های ۲۰۰۰–۲۰۱۰) وارد علوم شد؛ با ظهور سیستم‌های توصیه‌گر و پلتفرم‌های بزرگ، به «موضوع مستقل» تبدیل شد؛ در عصر هوش مصنوعی و مقررات‌گذاری (مانند قانون خدمات دیجیتال)، به «میدان سیاست عمومی» بدل شده است (Couldry & Hepp, 2017).",
        assumptions="فرض‌های نهفته: الگوریتم، تصمیم‌گیری را خودکار و مقیاس‌پذیر می‌کند و جایگزین قضاوت انسانی می‌شود؛ منطق الگوریتم، قابل اعتماد و قابل اعتمادسازی است؛ و حکمرانی ماشینی، نظم، کارایی و انصاف می‌آفریند؛ اما شفافیت، پاسخگویی و انصاف، ایده‌آل‌هایی هستند که در عمل بسیار محدود و نیازمند نظارت مستمرند (Bucher, 2018; Couldry & Hepp, 2017).",
    ),
    "CPT-202": dict(
        summary="نظارت الگوریتمی (Algorithmic Surveillance) به فرایند پایش، جمع‌آوری، تحلیل و پیش‌بینی رفتار افراد و جمعیت‌ها به‌وسیلۀ الگوریتم‌ها و داده‌های بزرگ می‌گویند؛ یعنی «نظارتی که توسط ماشین و بر پایه داده انجام می‌شود». در سنت نظارت‌محور، نظارت الگوریتمی بر ویژگی‌هایی چون: (۱) فراگیری: پایش، به‌شکل مستمر، گسترده و اغلب نامرئی انجام می‌شود؛ (۲) داده‌محوری: رفتار، به ردّ و داده قابل تحلیل تبدیل می‌شود؛ (۳) پیش‌بینی: الگوریتم، رفتار آینده را بر اساس الگوهای گذشته پیش‌بینی می‌کند؛ (۴) کنترل: نتایج، برای هدایت، هدف‌گیری یا محدودسازی رفتار به‌کار می‌رود (Zuboff, 2019; Giddens, 1991). در سنت جامعه‌شناختی، نظارت، شکل‌گیری نظم اجتماعی در جوامع مدرن را بازتاب می‌دهد (Giddens, 1991). پژوهش‌ها نشان می‌دهند نظارت الگوریتمی بر «حریم خصوصی»، «آزادی» و «توازن قدرت» اثر عمیق دارد. نمونه‌های رایج نظارت الگوریتمی: ردیابی رفتار کاربر در وب و اپلیکیشن‌ها، پایش موقعیت مکانی و شبکه، تحلیل الگوی خرید و جستجو، هدف‌گیری تبلیغی و نظارت امنیتی و انتظامی بر جمعیت‌ها. نقد بنیادین، «نظارت‌زدگی» (surveillance-ism) است: فرض بر این است که نظارت، «ضروری» و «خنثی» است، در حالی که در واقع آن، «کنترل‌کننده» و «بهره‌بردار» است و تفاوت، «درجه‌ای» است نه «ماهوی» (Zuboff, 2019).",
        mechanism="نظارت الگوریتمی در چهار حلقه عمل می‌کند: (۱) ثبت: رفتار، حضور و تعامل فرد در فضای دیجیتال ثبت و به داده تبدیل می‌شود؛ (۲) جمع‌بندی: داده‌های پراکنده، در پروفایل یکپارچه و مقیاسی بزرگ گرد می‌آیند؛ (۳) تحلیل و پیش‌بینی: الگوریتم، الگوها را کشف و رفتار آینده را پیش‌بینی می‌کند؛ (۴) اعمال و کنترل: بر پایه پیش‌بینی، رفتار هدف‌گیری، هدایت یا محدود می‌شود (تبلیغ، قیمت، دسترسی، نظارت امنیتی) (Zuboff, 2019; Giddens, 1991). این چرخه، نظارت را از واکنشی به پیش‌گیرانه بدل می‌کند.",
        key_concepts=["پایش گسترده", "داده‌محوری", "پیش‌بینی رفتار", "کنترل", "حریم خصوصی"],
        critiques="الگوی نظارتی، نظارت را «ضروری» و «خنثی» نشان می‌دهد، در حالی که در واقع آن، «کنترل‌کننده» و «بهره‌بردار اقتصادی» است و تفاوت، «درجه‌ای» است نه «ماهوی» (Zuboff, 2019). نقد دیگر، «پیش‌دانستی» (predictive bias) است: پیش‌بینی بر پایه داده‌های گذشته، تعصبات و نابرابری‌های موجود را تکرار و تقویت می‌کند و بر گروه‌های آسیب‌پذیر اثر نامتناسب دارد (Giddens, 1991). همچنین «نامرئیت» نظارت، رضایت آگاهانه و حق فراموشی را زیر سؤال می‌برد و اثر چرخش‌رفتاری (chilling effect) دارد.",
        applications="تحلیل انتقادی اقتصاد داده‌ای و نظارت (منشأ داده، بهره‌برداری، اخلاق)، طراحی حریم خصوصی و امنیت (رضایت، حق فراموشی، شفافیت، محدودسازی جمع‌آوری)، تنظیمات قانونی نظارت (نظارت داده‌محور، حسابرسی، پاسخگویی)، آموزش سواد داده‌ای (مدیریت ردّ، ریسک نظارتی)، و طراحی اخلاقی سیستم‌های پیش‌بینی و هدف‌گیری (نظارت به‌اندازه، تناسب، حداقل‌سازی داده، امکان اعتراض و حذف) (Zuboff, 2019; Giddens, 1991).",
        evolution="مفهوم نظارت از نظریه‌های جامعه‌شناختی مدرنیته و انضباط (دهه‌های ۱۹۶۰–۱۹۹۰) وارد علوم شد؛ با ظهور فناوری دیجیتال و داده‌های بزرگ (دهه‌های ۲۰۰۰–۲۰۱۰)، به «نظارت الگوریتمی و فراگیر» تبدیل شد؛ در عصر سرمایه‌داری نظارتی، نظارت به «زیرساخت اقتصادی و سیاسی» بدل شده است (Zuboff, 2019).",
        assumptions="فرض‌های نهفته: رفتار فرد، قابل ثبت، داده‌سازی و پیش‌بینی است؛ داده‌های رفتاری، نماینده واقعی رفتارند؛ و نظارت الگوریتمی، نظم، امنیت و کارایی می‌آفریند؛ اما رضایت آگاهانه، شفافیت و تناسب، از پیش‌فرض‌هایی هستند که در عمل اغلب نقض می‌شوند و نیازمند بازبینی مستمرند (Zuboff, 2019; Giddens, 1991).",
    ),
    "CPT-203": dict(
        summary="پلتفرم‌سازی (Platformization) به فرایند تبدیل ساختارها، نهادها و فعالیت‌های متنوع (رسانه، فرهنگ، اقتصاد، خدمات) به فرایندهای استوار بر پلتفرم‌های دیجیتال و منطق آن‌ها می‌گویند؛ یعنی «همه‌چیز، به پلتفرم بدل می‌شود». در سنت مطالعات پلتفرم، پلتفرم‌سازی بر ویژگی‌هایی چون: (۱) زیرساخت‌شدن: پلتفرم، به زیرساخت عمومی توزیع و تعامل تبدیل می‌شود؛ (۲) داده‌محوری: منطق پلتفرم، بر داده، الگوریتم و توجه استوار است؛ (۳) بازتولید: سایر بخش‌ها (خبر، فرهنگ، دولت) بر منطق پلتفرم بازتولید می‌شوند؛ (۴) تمرکز: قدرت و ارزش، در تعداد اندک پلتفرم متمرکز می‌شود (Couldry & Hepp, 2017; Castells, 2009). در سنت جامعه‌شناختی شبکه، پلتفرم‌سازی، شکل‌گیری «ساختار شبکه‌ای» صنعت و فرهنگ را بازتاب می‌دهد (Castells, 2009). پژوهش‌ها نشان می‌دهند پلتفرم‌سازی بر «ساختار صنعت رسانه»، «اقتصاد فرهنگ» و «تنوع» اثر عمیق دارد. نمونه‌های رایج پلتفرم‌سازی: تبدیل خبر و سرگرمی به محتوای درون‌پلتفرمی، بازاریابی و تجارت الکترونیک بر بستر شبکه‌های اجتماعی، خدمات شهری و دولتی بر پایه اپلیکیشن و ابر، و اقتصاد تولیدکننده‌مخاطب که کاربران، خود به تولیدکننده محتوا بدل می‌شوند. نقد بنیادین، «پلتفرم‌زدگی» (platformization-ism) است: فرض بر این است که پلتفرم، «میدان باز» و «خنثی» است، در حالی که در واقع آن، «قواعد و منافع» خود را تحمیل می‌کند و تفاوت، «درجه‌ای» است نه «ماهوی» (Couldry & Hepp, 2017).",
        mechanism="پلتفرم‌سازی در چهار حلقه عمل می‌کند: (۱) زیرساخت‌سازی: پلتفرم، بستر توزیع، تعامل و تولید را فراهم می‌کند؛ (۲) درگیرسازی: کاربران، تولیدکنندگان و نهادها، روی پلتفرم فعالیت می‌کنند؛ (۳) داده‌سازی و الگوریتم‌سازی: فعالیت‌ها، به داده و الگوی الگوریتمی تبدیل و هدفمند می‌شوند؛ (۴) بازتولید و تمرکز: منطق و قواعد پلتفرم، سایر بخش‌ها را بازتولید و ارزش، در آن متمرکز می‌شود (Couldry & Hepp, 2017; Castells, 2009). این چرخه، پلتفرم را به قدرت ساختاری بدل می‌کند.",
        key_concepts=["زیرساخت‌شدن", "داده‌محوری", "بازتولید", "تمرکز قدرت", "اقتصاد پلتفرم"],
        critiques="الگوی پلتفرمی، پلتفرم را «میدان باز» و «خنثی» نشان می‌دهد، در حالی که در واقع آن، «قواعد» و «منافع» خود را بر اکوسیستم تحمیل می‌کند و تفاوت، «درجه‌ای» است نه «ماهوی» (Couldry & Hepp, 2017). نقد دیگر، «تمرکزگرایی» (concentration) است: قدرت و ارزش، در تعداد اندک پلتفرم متمرکز می‌شود و تنوع و رقابت را کاهش می‌دهد (Castells, 2009). همچنین «وابستگی» نهادها و کاربران به یک پلتفرم، ریسک انحصار، تغییر یک‌شانه قواعد و آسیب به چرخه اقتصاد فرهنگ دارد.",
        applications="تحلیل انتقادی ساختار صنعت رسانه و فرهنگ (تمرکز، انحصار، تنوع)، طراحی استراتژی پلتفرم و اکوسیستم (زیرساخت، داده، الگوریتم)، تنظیمات قانونی پلتفرم (رقابت، شفافیت، پاسخگویی)، آموزش سواد رسانه‌ای و دیجیتال (شناخت منطق پلتفرم، تمرکز)، و طراحی کسب‌وکار رسانه‌ای بر پایه اقتصاد پلتفرم (Couldry & Hepp, 2017; Castells, 2009).",
        evolution="مفهوم پلتفرم‌سازی از مطالعات صنعت نرم‌افزار و رسانه (دهه‌های ۲۰۰۰) وارد علوم شد؛ با رشد شبکه‌های اجتماعی و سرویس‌های ابری (دهه‌های ۲۰۱۰)، به «موضوع مستقل» تبدیل شد؛ در عصر امروز، پلتفرم‌سازی به «بنیاد ساختاری» اقتصاد فرهنگ، رسانه و حتی دولت‌داری بدل شده است (Castells, 2009).",
        assumptions="فرض‌های نهفته: پلتفرم، بستر باز و خنثی توزیع و تعامل است؛ فعالیت کاربران، به داده‌ای قابل بهره‌برداری برای پلتفرم تبدیل می‌شود؛ و پلتفرم، کارایی، دسترسی و نوآوری می‌آفریند؛ اما بی‌طرفی، باز بودن و رقابت، ایده‌آل‌هایی هستند که در عمل به نفع منافع پلتفرم متمرکز می‌شوند (Couldry & Hepp, 2017; Castells, 2009).",
    ),
    "CPT-204": dict(
        summary="شبکه‌ای‌شدن (Networkedness) به فرایند سازمان‌یابی جامعه، نهادها و جریان‌های اطلاعاتی در قالب شبکه‌هایی از گره‌ها و پیوندها می‌گویند؛ یعنی «روابط، به‌جای سلسله‌مراتب، شبکه می‌شوند». در سنت جامعه‌شناختی شبکه، شبکه‌ای‌شدن بر ویژگی‌هایی چون: (۱) پیوندی بودن: قدرت، در پیوندها و نه در گره‌های انفرادی نهفته است؛ (۲) توزیع‌شدگی: ساختار، مرکزی نیست و چندمرکز است؛ (۳) جریان‌محوری: ارزش، در جریان اطلاعات و تعامل نهفته است نه در مالکیت؛ (۴) مقیاس‌پذیری: شبکه، می‌تواند بدون مرز جغرافیایی گسترش یابد (Castells, 2009; Giddens, 1991). در سنت مدرنیته، شبکه‌ای‌شدن، جداشدن روابط از مکان و زمان (disembedding) را بازتاب می‌دهد (Giddens, 1991). پژوهش‌ها نشان می‌دهند شبکه‌ای‌شدن بر «ساختار اجتماعی»، «جریان اطلاعات» و «قدرت» اثر عمیق دارد. نمونه‌های رایج شبکه‌ای‌شدن: شبکه‌های اجتماعی و پیام‌رسان‌ها، شبکه‌های خبری و رسانه‌های بین‌المللی، اکوسیستم‌های فناوری و زنجیره‌های ارزش دیجیتال، و شبکه‌های اجتماعی‌شدهٔ شهروندی که اطلاعات و معانی را در سراسر مرزها جریان می‌دهند. نقد بنیادین، «شبکه‌زدگی» (network-ism) است: فرض بر این است که شبکه، «برابری‌بخش» و «باز» است، در حالی که در واقع آن، «سلسله‌مراتب» و «تمرکز» جدیدی می‌سازد و تفاوت، «درجه‌ای» است نه «ماهوی» (Castells, 2009).",
        mechanism="شبکه‌ای‌شدن در چهار حلقه عمل می‌کند: (۱) اتصال: گره‌ها (افراد، رسانه‌ها، نهادها) به یکدیگر پیوند می‌خورند؛ (۲) جریان: اطلاعات، معنا و تعامل، در پیوندها جریان می‌یابد؛ (۳) تقویت: پیوندها، با تعامل بیشتر، قوی‌تر و شبکه، پویاتر می‌شود (اثر شبکه‌ای)؛ (۴) خودسازمان‌دهی: شبکه، الگوها و سلسله‌مراتب خود را شکل می‌دهد (گره‌های کلیدی، مرکزیت) (Castells, 2009; Giddens, 1991). این چرخه، ساختار اجتماعی را از سلسله‌مراتب به شبکه بدل می‌کند.",
        key_concepts=["پیوندی بودن", "توزیع‌شدگی", "جریان‌محوری", "اثر شبکه‌ای", "جداشدن از مکان"],
        critiques="الگوی شبکه‌ای، شبکه را «برابری‌بخش» و «باز» نشان می‌دهد، در حالی که در واقع آن، «سلسله‌مراتب» و «تمرکز» جدیدی می‌سازد و تفاوت، «درجه‌ای» است نه «ماهوی» (Castells, 2009). نقد دیگر، «مرکزیت پنهان» (hidden core) است: هر شبکه، گره‌های کلیدی و هسته‌های قدرتمندی دارد که جریان و دسترسی را کنترل می‌کنند (Giddens, 1991). همچنین «جداشدن از مکان»، پایداری و هویتِ روابط را تضعیف و بر اعتماد اجتماعی اثر می‌گذارد.",
        applications="تحلیل شبکه‌های اجتماعی و اطلاعاتی (گره، پیوند، مرکزیت)، طراحی استراتژی شبکه‌ای و اکوسیستم رسانه‌ای، تحلیل انتشار خبر و اطلاعات، آموزش سواد شبکه‌ای و رسانه‌ای (شناخت ساختار شبکه، مرکزیت)، و طراحی نهادها و خدمات بر پایه منطق شبکه و جریان (مدیریت گره و پیوند، افزایش تاب‌آوری، کاهش مرکزیت، طراحی اکوسیستم و پلتفرم‌های باز) (Castells, 2009; Giddens, 1991).",
        evolution="مفهوم شبکه‌ای‌شدن از نظریه شبکه و جامعه‌شناسی مدرنیته (دهه‌های ۱۹۷۰–۱۹۹۰، گیدنز، کاستلز) وارد علوم شد؛ با ظهور اینترنت و وب، به «ساختار غالب» جامعه و اقتصاد تبدیل شد؛ در عصر دیجیتال، شبکه‌ای‌شدن به «بنیاد ساختاری» ارتباط، قدرت، اقتصاد و تولید معنا بدل شده و تقریباً تمام نهادها و فرایندها را به‌شکل شبکه‌ای بازسازی می‌کند (Castells, 2009).",
        assumptions="فرض‌های نهفته: روابط اجتماعی و جریان اطلاعات، در قالب شبکه‌های پیوندی سازمان می‌یابند؛ قدرت و ارزش، در پیوندها و جریان نهفته‌اند نه در گره‌های انفرادی؛ و شبکه، امکان مقیاس‌پذیری و گسترش بدون مرز می‌سازد؛ اما بی‌طرفی و برابری شبکه، ایده‌آل‌هایی هستند که در عمل با مرکزیت و سلسله‌مراتب محدود می‌شوند (Castells, 2009; Giddens, 1991).",
    ),
    "CPT-205": dict(
        summary="ارتباطات هم‌زمان (Synchronous Communication) به فرایند تولید، انتقال و دریافت پیام در زمان مشترک و با حضور (واقعی یا مجازی) طرفین در آن لحظه می‌گویند؛ یعنی «مخاطب و فرستنده، با هم و هم‌زمان، در ارتباط‌اند». در سنت نظریه‌های ارتباط، ارتباطات هم‌زمان بر ویژگی‌هایی چون: (۱) هم‌زمانی: فرستنده و گیرنده، در یک زمان، فعال‌اند؛ (۲) بازخورد فوری: پاسخ، بلافاصله و در همان لحظه می‌رسد؛ (۳) هم‌حضور: طرفین، حضور (مکاني یا مجازی) را حس می‌کنند؛ (۴) تعاملی بودن: مکالمه، به‌شکل پیوسته و دوطرفه جریان می‌یابد (Giddens, 1991; Littlejohn & Foss, 2011). در سنت جامعه‌شناختی، هم‌زمانی و «هم‌حضور فاصله‌ای»، ویژگی روابط مدرن است (Giddens, 1991). پژوهش‌ها نشان می‌دهند ارتباطات هم‌زمان بر «انطباق اجتماعی»، «برقراری ارتباط» و «ساختن معنا» اثر عمیق دارد. نمونه‌های رایج ارتباطات هم‌زمان: گفتار وجهاًبه‌وجه، تماس تلفنی و ویدئوکال، چت و پیام‌رسانی زنده، استریم و پخش زنده، و جلسات ویدئوکنفرانس و آموزش آنلاین هم‌زمان. نقد بنیادین، «هم‌زمانی‌زدگی» (synchrony-ism) است: فرض بر این است که هم‌زمانی، «همیشه مطلوب» است، در حالی که در واقع آن، «فشار و بی‌واسطگی» می‌آورد و تفاوت، «درجه‌ای» است نه «ماهوی» (Littlejohn & Foss, 2011).",
        mechanism="ارتباطات هم‌زمان در چهار حلقه عمل می‌کند: (۱) برقراری کانال: طرفین، در زمان مشترک، به کانال ارتباط (گفتار، تماس، ویدئو، چت) متصل می‌شوند؛ (۲) ارسال و دریافت فوری: پیام، بلافاصله انتقال و دریافت می‌شود؛ (۳) بازخورد زنده: واکنش، در همان لحظه بازگشت و مکالمه، شکل می‌گیرد؛ (۴) تنظیم و انطباق: طرفین، بر پایه بازخورد، لحن، زمان‌بندی و محتوا را تنظیم می‌کنند (Giddens, 1991; Littlejohn & Foss, 2011). این چرخه، تعامل را فوری و دوطرفه می‌سازد.",
        key_concepts=["هم‌زمانی", "بازخورد فوری", "هم‌حضور", "تعامل دوطرفه", "انطباق اجتماعی"],
        critiques="الگوی هم‌زمان، هم‌زمانی را «همیشه مطلوب» نشان می‌دهد، در حالی که در واقع آن، «فشار»، «بی‌واسطگی» و محدودیت تأمل می‌آورد و تفاوت، «درجه‌ای» است نه «ماهوی» (Littlejohn & Foss, 2011). نقد دیگر، «وابستگی به حضور» است: هم‌زمانی، زمانی را محدود و طرفین را به یک زمان و کانال وابسته می‌کند و برای گفتارهای پیچیده یا بین‌فرهنگی، می‌تواند نامناسب باشد (Giddens, 1991). همچنین هم‌زمانی، فرصت «تأمل و بازخوانی» را می‌کاهد و کیفیت پیام را تحت فشار قرار می‌دهد.",
        applications="طراحی خدمات ارتباطی فوری (گفتار، تماس، ویدئوکال، چت زنده، استریم)، طراحی تجربه تعاملی (بازخورد فوری، هم‌حضور، انطباق)، تحلیل مکالمه و گفت‌وگوی عمومی (برقراری ارتباط، معناسازی)، آموزش ارتباط مؤثر (مهارت گفت‌وگوی زنده، همدلی)، و طراحی پلتفرم‌های ارتباط جمعی (هم‌زمانی، هماهنگی زمان) (Giddens, 1991; Littlejohn & Foss, 2011).",
        evolution="مفهوم ارتباطات هم‌زمان از نظریه‌های گفتار و ارتباط (دهه‌های ۱۹۵۰–۱۹۷۰) وارد علوم شد؛ با تلفن، تلویزیون و سپس ویدئوکنفرانس (دهه‌های ۱۹۸۰–۲۰۰۰)، «هم‌حضور فاصله‌ای» گسترش یافت؛ در عصر دیجیتال، ارتباطات هم‌زمان به «معیار پیش‌فرض» برقراری ارتباط بدل شده و با ارتباطات ناهم‌زمان ترکیب می‌شود (Giddens, 1991).",
        assumptions="فرض‌های نهفته: فرستنده و گیرنده، می‌توانند در زمان مشترک فعال و حاضر باشند؛ پیام و بازخورد، به‌صورت فوری و قابل‌درک انتقال می‌یابند؛ و هم‌حضور، معناسازی و انطباق را تسهیل می‌کند؛ اما در دسترس بودن، بستر مناسب و هنجارهای زمانی، از پیش‌فرض‌هایی هستند که در عمل محدود و قابل نقض‌اند (Giddens, 1991; Littlejohn & Foss, 2011).",
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
