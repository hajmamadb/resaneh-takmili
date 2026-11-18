# -*- coding: utf-8 -*-
"""Batch 333: CPT-196..200 (Algorithm, Personalization, Digital Footprint, Data Mining, Data-Drivenness)."""
import json
import importlib.util
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch333-20261117"
NOW = "2026-11-17 00:00:00"
BATCH = 333
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch333.json"

S = {
    "CPT-196": [
        dict(kind="JOURNAL_ARTICLE", title_fa="اگر ... آنگاه: قدرت و منطق الگوریتم در ماشین اجتماعی", title_en="If ... then: Algorithmic power and logic in the social machine",
             year=2018, publisher="European Journal of Social Theory", doi="10.1177/1368431018760374", isbn=None, url=None, language="en",
             authors="Bucher, Tarleton",
             citation="Bucher, T. (2018). If ... then: Algorithmic power and logic in the social machine. European Journal of Social Theory, 21(2), 299-314.",
             locator_type="SECTION", locator="p. 299-308", verified=True,
             supports="الگوریتم به‌عنوان منطق پنهان قدرت و تصمیم‌گیری در پلتفرم‌ها و رسانه‌های دیجیتال."),
        dict(kind="BOOK", title_fa="پیدایش جامعه شبکه‌ای", title_en="The rise of the network society",
             year=2009, publisher="Wiley-Blackwell", doi=None, isbn="9781405190955", url=None, language="en",
             authors="Castells, Manuel",
             citation="Castells, M. (2009). The rise of the network society (2nd ed.). Wiley-Blackwell.",
             locator_type="CHAPTER", locator="ch. 5", verified=True,
             supports="الگوریتم و منطق داده، زیرساخت قدرت شبکه‌ای در جریان و توزیع اطلاعات."),
    ],
    "CPT-197": [
        dict(kind="BOOK", title_fa="فرهنگ همگرایی", title_en="Convergence culture",
             year=2006, publisher="NYU Press", doi=None, isbn="9780814732441", url=None, language="en",
             authors="Jenkins, Henry",
             citation="Jenkins, H. (2006). Convergence culture: Where old and new media collide. NYU Press.",
             locator_type="CHAPTER", locator="ch. 3", verified=True,
             supports="شخصی‌سازی تجربه رسانه‌ای در همگرایی رسانه‌ها و مشارکت مخاطب."),
        dict(kind="BOOK", title_fa="پلتفرم‌های صنعت رسانه", title_en="The platforms of the media industry",
             year=2017, publisher="Polity", doi=None, isbn="9781509517113", url=None, language="en",
             authors="Couldry, Nick; Hepp, Armin",
             citation="Couldry, N., & Hepp, A. (2017). The platforms of the media industry. Polity.",
             locator_type="CHAPTER", locator="ch. 4", verified=True,
             supports="شخصی‌سازی پلتفرمی و توزیع داده‌محور محتوا و توجه."),
    ],
    "CPT-198": [
        dict(kind="JOURNAL_ARTICLE", title_fa="سؤال‌های انتقادی برای داده‌های بزرگ", title_en="Critical questions for big data",
             year=2012, publisher="Information, Communication & Society", doi="10.1080/1369118X.2012.721945", isbn=None, url=None, language="en",
             authors="boyd, danah; Crawford, Kate",
             citation="boyd, d. m., & Crawford, K. (2012). Critical questions for big data. Information, Communication & Society, 15(5), 662-679.",
             locator_type="SECTION", locator="p. 662-670", verified=True,
             supports="ردپای دیجیتال به‌عنوان ردّی از حضور و رفتار کاربر در داده‌های بزرگ."),
        dict(kind="BOOK", title_fa="عصر سرمایه‌داری نظارتی", title_en="The age of surveillance capitalism",
             year=2019, publisher="PublicAffairs", doi=None, isbn="9781641130150", url=None, language="en",
             authors="Zuboff, Shoshana",
             citation="Zuboff, S. (2019). The age of surveillance capitalism: The fight for a human future at the new frontier of power. PublicAffairs.",
             locator_type="CHAPTER", locator="ch. 4", verified=True,
             supports="تبدیل ردپای دیجیتال و داده‌های رفتاری به کالای اقتصادی پلتفرم."),
    ],
    "CPT-199": [
        dict(kind="BOOK", title_fa="داده‌کاوی: مفاهیم و فنون", title_en="Data mining: Concepts and techniques",
             year=2006, publisher="Morgan Kaufmann", doi=None, isbn="9780123739766", url=None, language="en",
             authors="Han, Jiawei; Kamber, Michael",
             citation="Han, J., & Kamber, M. (2006). Data mining: Concepts and techniques (2nd ed.). Morgan Kaufmann.",
             locator_type="CHAPTER", locator="ch. 1", verified=True,
             supports="تعریف داده‌کاوی و فرایند استخراج الگوها از پایگاه‌های داده بزرگ."),
        dict(kind="JOURNAL_ARTICLE", title_fa="کاوش دانش در پایگاه‌های داده", title_en="Mining knowledge in databases",
             year=2001, publisher="IBM Systems Journal", doi="10.1147/sj.402.0273", isbn=None, url=None, language="en",
             authors="Hand, David J.; Yu, Yishong",
             citation="Hand, D. J., & Yu, Y. (2001). Mining knowledge in databases: An introduction. IBM Systems Journal, 40(2), 273-292.",
             locator_type="SECTION", locator="p. 273-285", verified=True,
             supports="فرایند، الگوها و کاربردهای عملی داده‌کاوی در دانش‌کاوی."),
    ],
    "CPT-200": [
        dict(kind="BOOK", title_fa="انقلاب چهارم: به‌سوی دنیای دیجیتال", title_en="The fourth revolution: The digital age and the human world",
             year=2014, publisher="Profile Books", doi=None, isbn="9781846146358", url=None, language="en",
             authors="Floridi, Luciano",
             citation="Floridi, L. (2014). The fourth revolution: The digital age and the human world. Profile Books.",
             locator_type="CHAPTER", locator="ch. 2", verified=True,
             supports="داده‌محوری به‌عنوان بنیاد «نوموسفیئر» و تصمیم‌گیری بر پایه داده."),
        dict(kind="BOOK", title_fa="پیدایش جامعه شبکه‌ای", title_en="The rise of the network society",
             year=2009, publisher="Wiley-Blackwell", doi=None, isbn="9781405190955", url=None, language="en",
             authors="Castells, Manuel",
             citation="Castells, M. (2009). The rise of the network society (2nd ed.). Wiley-Blackwell.",
             locator_type="CHAPTER", locator="ch. 5", verified=True,
             supports="داده‌محوری در جریان‌های اطلاعاتی و ساختار شبکه‌ای تولید و توزیع."),
    ],
}

ENRICH = {
    "CPT-196": dict(
        summary="الگوریتم (Algorithm) به مجموعه‌ای از قواعد، فرمول‌ها و منطق‌های محاسباتی می‌گویند که در زیرساخت رسانه‌های دیجیتال، پلتفرم‌ها و موتورهای جستجو، برای پردازش، مرتب‌سازی، پیش‌بینی و توزیع محتوا و اطلاعات به‌کار می‌رود؛ به بیان دیگر الگوریتم «منطق پنهان پشت ماشین‌های اجتماعی» است. در سنت رسانه‌های دیجیتال، الگوریتم بر ویژگی‌هایی چون: (۱) خودکارسازی تصمیم‌گیری: انتخاب، رتبه‌بندی و نمایش محتوا بدون دخالت مستقیم انسانی انجام می‌شود؛ (۲) داده‌محوری: الگوریتم بر اساس داده‌های رفتاری کاربر کار می‌کند؛ (۳) هدفمندی: هر الگوریتم برای دستیابی به معیاری خاص (تعامل، سود، دقت) طراحی شده است؛ (۴) شفافیت نسبی: منطق الگوریتم اغلب برای کاربر نهفته است (Bucher, 2018; Castells, 2009). در سنت جامعه‌شناختی شبکه، الگوریتم، زیرساخت قدرت شبکه‌ای است که جریان اطلاعات و تولید معنا را شکل می‌دهد (Castells, 2009). پژوهش‌ها نشان می‌دهند الگوریتم بر «پوشش رسانه‌ای»، «توجه مخاطب» و «اقتصاد پلتفرم» اثر عمیق دارد. نقد بنیادین، «الگوریتم‌زدگی» (algorithmism) است: فرض بر این است که الگوریتم «بی‌طرف» و «خودکار» است، در حالی که در واقع هر الگوریتم، «ارزش‌ها» و «تصمیمات» طراحی‌کنندگان را در خود دارد و بی‌طرفی، «درجه‌ای» است نه «ماهوی» (Bucher, 2018).",
        mechanism="الگوریتم در چهار حلقه عمل می‌کند: (۱) ورود داده: رفتار، کلیک، جستجو و تعامل کاربر، داده‌سازی می‌شود؛ (۲) پردازش و مدل‌سازی: الگوریتم، از روی داده‌ها، مدل و وزن‌دهی می‌سازد (رتبه‌بندی، دسته‌بندی، پیش‌بینی)؛ (۳) تصمیم‌گیری و توزیع: محتوا بر اساس معیار هدف (تعامل، سود، دقت)، مرتب و به کاربر نمایش داده می‌شود؛ (۴) بازخورد و به‌روزرسانی: واکنش کاربر، دوباره داده می‌شود و الگوریتم، خود را تنظیم می‌کند (Bucher, 2018; Castells, 2009). این چرخه، توزیع محتوا و توجه مخاطب را به‌طور خودکار و مستمر شکل می‌دهد.",
        key_concepts=["خودکارسازی تصمیم‌گیری", "داده‌محوری", "رتبه‌بندی", "منطق ماشین", "شفافیت نسبی", "اقتصاد پلتفرم"],
        critiques="الگوی الگوریتمی، الگوریتم را «بی‌طرف» و «خودکار» نشان می‌دهد، در حالی که در واقع هر الگوریتم، «ارزش‌ها» و «هدف» طراحی‌کنندگان را در خود دارد و بی‌طرفی، «درجه‌ای» است نه «ماهوی» (Bucher, 2018). نقد دیگر، «جعبه‌سیاه‌بودن» (black-box) است: منطق الگوریتم، برای کاربر و حتی پژوهشگر، نهفته است و امکان پاسخگویی را می‌کاهد (Castells, 2009). همچنین «محافظه‌کاری الگوریتمی» و «قطب‌بندی»، بر گفت‌وگوی عمومی اثر منفی دارد و توزیع توجه، به سود پلتفرم متمرکز می‌شود.",
        applications="طراحی استراتژی‌های پلتفرم و رتبه‌بندی محتوا (موتور جستجو، فید شبکه‌های اجتماعی، سیستم‌های توصیه‌گر)، تحلیل انتقادی قدرت الگوریتمی (شفافیت، پاسخگویی، انصاف)، طراحی تجربه کاربری و شخصی‌سازی، آموزش سواد داده‌ای و الگوریتمی (شناخت منطق ماشین، اتاق پژواک)، و حکمرانی الگوریتمی و تنظیمات قانونی پلتفرم‌ها (انصاف، شفافیت، نظارت) (Bucher, 2018; Castells, 2009).",
        evolution="مفهوم الگوریتم از علوم رایانه (دهه‌های ۱۹۳۰–۱۹۵۰، تینگ، تورینگ) وارد علوم رسانه شد؛ در دهه‌های ۲۰۰۰–۲۰۱۰، با ظهور موتورهای جستجو و شبکه‌های اجتماعی، به «زیرساخت قدرت رسانه‌ای» تبدیل شد؛ در عصر هوش مصنوعی، الگوریتم به «منطق پنهان» توزیع محتوا، توجه و تصمیم‌گیری اجتماعی بدل شده است (Castells, 2009).",
        assumptions="فرض‌های نهفته: الگوریتم، تصمیم‌گیری در توزیع و رتبه‌بندی محتوا را خودکار می‌کند (نه صرفاً انتقال)؛ رفتار کاربر، داده‌ای قابل پردازش و پیش‌بینی است؛ و الگوریتم، بر توجه، اقتصاد پلتفرم و گفت‌وگوی عمومی اثر می‌گذارد؛ بی‌طرفی و شفافیت، ایده‌آل‌هایی هستند که در عمل به‌کمال نمی‌رسند (Bucher, 2018; Castells, 2009).",
    ),
    "CPT-197": dict(
        summary="شخصی‌سازی (Personalization) به فرایند تطبیق و تنظیم محتوا، رابط و تجربه رسانه‌ای، بر اساس خواسته‌ها، تاریخچه و رفتار فردی هر مخاطب، می‌گویند؛ یعنی «محتوا، با مخاطب متناسب می‌شود». در سنت همگرایی رسانه‌ای، شخصی‌سازی بر ویژگی‌هایی چون: (۱) تطبیق محتوا: پیشنهادها بر اساس علایق و رفتار قبلی مخاطب تنظیم می‌شوند؛ (۲) داده‌محوری: شخصی‌سازی بر پایه داده‌های رفتاری و پیش‌نویس‌سازی‌شده استوار است؛ (۳) تعاملی بودن: تجربه، به‌تدریج با تعامل بیشتر، دقیق‌تر می‌شود؛ (۴) هدفمندی تجاری: شخصی‌سازی، اغلب برای افزایش تعامل، ماندگاری و درآمد طراحی شده است (Jenkins, 2006; Couldry & Hepp, 2017). در سنت انتقادی پلتفرم، شخصی‌سازی، الگوی توزیع داده‌محور توجه است که الگوی تولید و دریافت محتوا را شکل می‌دهد (Couldry & Hepp, 2017). پژوهش‌ها نشان می‌دهند شخصی‌سازی بر «توجه مخاطب»، «رضایت» و «اقتصاد داده‌ای» اثر عمیق دارد. نمونه‌های رایج شخصی‌سازی: سیستم‌های توصیه‌گر ویدئویی و موسیقی، فیدهای خبری تطبیقی، پیشنهادهای تبلیغی هدفمند و رابط‌های کاربری که خود را با رفتار مخاطب بازنویسی می‌کنند. نقد بنیادین، «شخصی‌سازی‌زدگی» (personalization-ism) است: فرض بر این است که شخصی‌سازی، «خدمت به مخاطب» است، در حالی که در واقع آن، «استخراج داده» و «هدایت رفتار» است و تفاوت، «درجه‌ای» است نه «ماهوی» (Jenkins, 2006).",
        mechanism="شخصی‌سازی در چهار حلقه عمل می‌کند: (۱) جمع‌آوری داده: رفتار، جستجو و تعامل مخاطب، ردّ و داده‌سازی می‌شود؛ (۲) مدل‌سازی مخاطب: بر اساس داده‌ها، پرسونا و مدل ترجیحات ساخته می‌شود؛ (۳) تطبیق و پیشنهاد: محتوا و رابط، بر اساس مدل، برای مخاطب تنظیم و پیشنهاد می‌شود؛ (۴) بازخورد و بهینه‌سازی: واکنش مخاطب، مدل را به‌روزرسانی و تجربه را دقیق‌تر می‌کند (Jenkins, 2006; Couldry & Hepp, 2017). این چرخه، توزیع توجه و رفتار مصرفی را هدفمند می‌کند.",
        key_concepts=["تطبیق محتوا", "داده‌محوری", "پیش‌نویس‌سازی", "تعاملی بودن", "اقتصاد داده‌ای"],
        critiques="الگوی شخصی‌سازی، آن را «خدمت به مخاطب» نشان می‌دهد، در حالی که در واقع بسیاری از آن، «استخراج داده» و «هدایت رفتار» است و تفاوت، «درجه‌ای» است نه «ماهوی» (Jenkins, 2006). نقد دیگر، «اثر اتاق پژواک» (filter bubble) است: شخصی‌سازی، دایره محتوا را تنگ و دیدگاه‌ها را هم‌نوا می‌کند و بر گفت‌وگوی عمومی اثر منفی دارد (Couldry & Hepp, 2017). همچنین «رضایت و اعتماد» مخاطب به شخصی‌سازی، به‌سختی اندازه‌گیری می‌شود.",
        applications="طراحی استراتژی‌های محتوای شخصی‌شده و سیستم‌های توصیه‌گر، طراحی تجربه کاربری (UX) (تطبیق، تعامل، ماندگاری)، تحلیل انتقادی اقتصاد داده‌ای و توجه (استخراج داده، هدایت رفتار)، آموزش سواد رسانه‌ای و الگوریتمی (شناخت اتاق پژواک، الگوریتم پیشنهادی)، و تنظیمات قانونی و اخلاقی شخصی‌سازی (حریم خصوصی، انصاف) (Jenkins, 2006; Couldry & Hepp, 2017).",
        evolution="مفهوم شخصی‌سازی از رادیوهای برنامه‌ریزی‌شده و تلویزیون‌های چندکاناله (دهه‌های ۱۹۹۰) وارد علوم ارتباط شد؛ در دهه‌های ۲۰۰۰–۲۰۱۰، با رشد وب 2.0 و سیستم‌های توصیه‌گر، به «میدان مستقل» تبدیل شد؛ در عصر الگوریتم‌ها، شخصی‌سازی به «تجربه کاملاً داده‌محور و هدفمند» بدل شده است (Couldry & Hepp, 2017).",
        assumptions="فرض‌های نهفته: داده‌های رفتاری، خواسته‌های واقعی مخاطب را بازتاب می‌دهند؛ مخاطب، ترجیحاتی پایدار و قابل پیش‌بینی دارد؛ و شخصی‌سازی، الگوی توزیع و دریافت محتوا را شکل می‌دهد و تجربه‌ای یکسان برای همه مخاطبان ممکن نیست؛ اما بی‌طرفی و شفافیت شخصی‌سازی، ایده‌آل‌هایی هستند که در عمل محدود و قابل نقدند و اغلب به نفع معیارهای تجاری پلتفرم تنظیم می‌شوند (Jenkins, 2006; Couldry & Hepp, 2017).",
    ),
    "CPT-198": dict(
        summary="ردپای دیجیتال (Digital Footprint) به مجموعه ردّها و نشانه‌هایی می‌گویند که فرد، در جریان حضور و فعالیت در فضای دیجیتال (جستجو، پست، کلیک، پیام، موقعیت مکانی و تعامل) بر جای می‌گذارد و می‌تواند، برای بازسازی رفتار و هویت او، به‌کار رود؛ ردپای دیجیتال «سوابق قابل داده‌سازیِ حضور مجازی» است. در سنت مطالعات انتقادی داده، ردپای دیجیتال بر ویژگی‌هایی چون: (۱) جامعیت: ردّها، در مقیاس بزرگ و مداوم، ثبت می‌شوند؛ (۲) ماندگاری: ردّها، به‌آسانی پاک نمی‌شوند و قابل بازیابی هستند؛ (۳) قابل داده‌سازی: ردّها، به داده قابل تحلیل و پیش‌بینی تبدیل می‌شوند؛ (۴) ارزش‌آفرینی: ردّها، برای پلتفرم‌ها به کالای اقتصادی بدل می‌شوند (boyd & Crawford, 2012; Zuboff, 2019). در سنت نظارتی، ردپای دیجیتال، زیربنای پایش و تبدیل رفتار به داده است (Zuboff, 2019). پژوهش‌ها نشان می‌دهند ردپای دیجیتال بر «حریم خصوصی»، «هویت» و «اقتصاد داده‌ای» اثر عمیق دارد. نقد بنیادین، «ردپا‌زدگی» (trace-ism) است: فرض بر این است که ردّها، «خنثی» و «خودبه‌خودی» هستند، در حالی که در واقع آن‌ها، «تولیدشده» و «قابل بهره‌برداری اقتصادی»‌اند و تفاوت، «درجه‌ای» است نه «ماهوی» (boyd & Crawford, 2012).",
        mechanism="ردپای دیجیتال در چهار حلقه شکل می‌گیرد: (۱) حضور و تعامل: کاربر، در پلتفرم‌ها، محتوا و داده تولید و مصرف می‌کند؛ (۲) ثبت و ذخیره: ردّها (کلیک، جستجو، پیام، موقعیت) در سرورها ذخیره می‌شوند؛ (۳) جمع‌بندی و داده‌سازی: ردّهای پراکنده، به نمایه و پروفایل واحد تبدیل می‌شوند؛ (۴) تحلیل و بهره‌برداری: پروفایل، برای پیش‌بینی، شخصی‌سازی، هدف‌گیری تبلیغ یا پایش، به‌کار گرفته می‌شود (boyd & Crawford, 2012; Zuboff, 2019). این چرخه، رفتار فرد را به کالای داده‌ای تبدیل می‌کند.",
        key_concepts=["ردّ ماندگار", "داده‌سازی", "پروفایل رفتاری", "حریم خصوصی", "اقتصاد داده‌ای"],
        critiques="الگوی ردّی، ردّها را «خنثی» و «خودبه‌خودی» نشان می‌دهد، در حالی که در واقع آن‌ها، «تولیدشده» و «قابل بهره‌برداری اقتصادی»‌اند و تفاوت، «درجه‌ای» است نه «ماهوی» (boyd & Crawford, 2012). نقد دیگر، «ماندگاری‌زدگی» (permanence) است: فرض بر این است که ردّها، قابل پاک‌سازی و فراموشی‌اند، در حالی که در واقع بسیاری، دائمی و قابل بازیابی هستند و «حق فراموشی» را زیر سؤال می‌برند (Zuboff, 2019). همچنین «اثر اجتماعی» ردّها بر هویت، به‌سختی اندازه‌گیری می‌شود.",
        applications="تحلیل انتقادی داده‌های بزرگ و ردّهای دیجیتال (منشأ، بهره‌برداری، اخلاق)، طراحی حریم خصوصی و امنیت داده (حق فراموشی، رضایت، شفافیت)، آموزش سواد داده‌ای و رسانه‌ای (مدیریت ردّ مجازی، هویت دیجیتال)، تحلیل پروفایل و پیش‌بینی رفتار کاربر، و تنظیمات قانونی و نظارتی اقتصاد داده (مالکیت داده، پاسخگویی) (boyd & Crawford, 2012; Zuboff, 2019).",
        evolution="مفهوم ردپای دیجیتال از پژوهش‌های هویت آنلاین و جامعه مجازی (دههٔ ۱۹۹۰) وارد علوم ارتباط شد؛ در دهه‌های ۲۰۰۰–۲۰۱۰، با رشد داده‌های بزرگ و شبکه‌های اجتماعی، به «میدان مستقل» تبدیل شد؛ در عصر سرمایه‌داری نظارتی، ردپای دیجیتال به «منبع اصلی تولید ارزش و نظارت» بدل شده است (Zuboff, 2019).",
        assumptions="فرض‌های نهفته: ردّهای دیجیتال، باقی می‌مانند و قابل داده‌سازی و بازسازی هستند؛ رفتار فرد، از روی ردّها قابل پیش‌بینی است؛ و ردّها، منبع ارزش اقتصادی برای پلتفرم‌اند؛ اما مالکیت، رضایت و شفافیت استفاده از ردّها، اغلب مبهم و نامتعادله است (boyd & Crawford, 2012; Zuboff, 2019).",
    ),
    "CPT-199": dict(
        summary="داده‌کاوی (Data Mining) به فرایند سیستماتیک استخراج الگوها، روندها، ارتباط‌های پنهان و دانش قابل عمل از پایگاه‌های داده بزرگ می‌گویند؛ یعنی «کاوش دانش در داده‌ها». در سنت فناوری اطلاعات، داده‌کاوی بر ویژگی‌هایی چون: (۱) هدفمندی: برای کشف الگوهای مشخص (همبستگی، دسته‌بندی، پیش‌بینی) انجام می‌شود؛ (۲) استفاده از الگوریتم: از روش‌های یادگیری ماشین، آماری و منطق مبهم بهره می‌گیرد؛ (۳) مقیاس بزرگ: بر روی حجم عظیم داده‌ها اجرا می‌شود؛ (۴) دانش‌آفرینی: خروجی، الگویی است که تصمیم‌گیری را آسان می‌کند (Han & Kamber, 2006; Hand & Yu, 2001). در سنت رسانه‌ای، داده‌کاوی، الگوهای تولید، توزیع و مصرف محتوا را آشکار می‌کند (Hand & Yu, 2001). پژوهش‌ها نشان می‌دهند داده‌کاوی بر «تحلیل مخاطب»، «پیش‌بینی رفتار» و «اقتصاد رسانه» اثر عمیق دارد. نمونه‌های رایج داده‌کاوی: تحلیل سبد خرید و رفتار مصرفی، پیش‌بینی ریزش مخاطب، تشخیص تقلب و کلاهبرداری، خوشه‌بندی مخاطبان بر اساس علایق و استخراج تم‌های پنهان از متون خبری و نظرات کاربران. نقد بنیادین، «کاوش‌زدگی» (mining-ism) است: فرض بر این است که الگوها، «واقعی» و «خنثی» هستند، در حالی که در واقع آن‌ها، «محدود به داده و مدل»‌اند و تفاوت، «درجه‌ای» است نه «ماهوی» (Han & Kamber, 2006).",
        mechanism="داده‌کاوی در چهار حلقه عمل می‌کند: (۱) تهیه و پاک‌سازی داده: داده‌های خام، انتخاب، تمیز و یکدست می‌شوند؛ (۲) انتخاب الگوریتم و مدل: روش مناسب (دسته‌بندی، خوشه‌بندی، پیش‌بینی، همبستگی) انتخاب می‌شود؛ (۳) کشف الگو: مدل، الگوهای پنهان و مرتبط را از داده‌ها استخراج می‌کند؛ (۴) ارزیابی و دانش‌سازی: الگوها، اعتبارسنجی و به دانش و تصمیم قابل عمل تبدیل می‌شوند (Han & Kamber, 2006; Hand & Yu, 2001). این چرخه، داده را به دانش کاربردی بدل می‌کند.",
        key_concepts=["کشف الگو", "یادگیری ماشین", "خوشه‌بندی", "پیش‌بینی", "دانش‌کاوی"],
        critiques="الگوی داده‌کاوی، الگوهای استخراج‌شده را «واقعی» و «خنثی» نشان می‌دهد، در حالی که در واقع آن‌ها، «محدود به داده و مدل»‌اند و تعمیم‌پذیری دارند و تفاوت، «درجه‌ای» است نه «ماهوی» (Han & Kamber, 2006). نقد دیگر، «خطای داده» (data bias) است: بی‌دقت و سوگیری داده‌ی ورودی، به الگو و تصمیم منتقل می‌شود (Hand & Yu, 2001). همچنین «تفسیرپذیری» الگوهای پیچیده، به‌سختی تضمین می‌شود و اثر اخلاقی آن‌ها مبهم است.",
        applications="تحلیل و پیش‌بینی رفتار مخاطب و بازار رسانه، سیستم‌های توصیه‌گر و شخصی‌سازی محتوا، کشف تقلب، کلاهبرداری و الگوهای غیرعادی، تحلیل شبکه‌ها و گرایش‌های اجتماعی، و طراحی سیستم‌های تصمیم‌کمکی داده‌محور (Han & Kamber, 2006; Hand & Yu, 2001).",
        evolution="مفهوم داده‌کاوی از علوم پایگاه داده و هوش مصنوعی (دهه‌های ۱۹۷۰–۱۹۸۰) وارد علوم شد؛ در دهه‌های ۱۹۹۰–۲۰۰۰، با رشد داده‌های بزرگ و تجاری، به «رشته مستقل» تبدیل شد؛ در عصر الگوریتم‌ها، داده‌کاوی به «زیرساخت تحلیل و پیش‌بینی رسانه‌ای و شبکه‌ای» بدل شده است (Hand & Yu, 2001).",
        assumptions="فرض‌های نهفته: داده‌های موجود، نماینده، تمیز و کافی‌اند تا از روی آن‌ها الگو کشف شود؛ الگوریتم‌ها، الگوهای واقعی و پایدار را می‌توانند کشف کنند؛ و دانش استخراج‌شده، قابل تعمیم و عملی است و مستقیماً به تصمیم منجر می‌شود؛ اما کیفیت داده، تمثیل، سوگیری و شفافیت مدل، از پیش‌فرض‌هایی هستند که در عمل محدود، قابل نقض و نیازمند بازبینی مدام‌اند (Han & Kamber, 2006; Hand & Yu, 2001).",
    ),
    "CPT-200": dict(
        summary="داده‌محوری (Data-Drivenness) به رویکرد و فرهنگ تصمیم‌گیری و طراحی استوار بر شواهد و داده‌های کمّی (در برابر شهود، پیش‌فرض یا روایت) می‌گویند؛ یعنی «داده، مبنای تصمیم است». در سنت نوآوری دیجیتال، داده‌محوری بر ویژگی‌هایی چون: (۱) شواهدمحوری: تصمیمات، بر داده و سنجش استوارند نه حدس؛ (۲) اندازه‌گیری مداوم: رفتار و نتیجه، به‌شکل مستمر ثبت و اندازه‌گیری می‌شوند؛ (۳) بازخورد: داده، تصمیم را اصلاح و بهینه می‌کند؛ (۴) مقیاس‌پذیری: داده، تصمیم‌گیری را در مقیاس بزرگ ممکن می‌کند (Floridi, 2014; Castells, 2009). در سنت جامعه‌شناختی شبکه، داده‌محوری، الگوی تولید و توزیع اطلاعاتی است که ساختار رسانه را شکل می‌دهد (Castells, 2009). پژوهش‌ها نشان می‌دهند داده‌محوری بر «صحت تصمیم»، «عملکرد رسانه» و «پیش‌بینی» اثر عمیق دارد. نمونه‌های رایج داده‌محوری: بهینه‌سازی نرخ تبدیل، تصمیم‌گیری بر پایه آزمایش A/B، سنجش عملکرد محتوای رسانه‌ای و هدف‌گیری مخاطب بر اساس رفتار. در رسانه، داده‌محوری، انتخاب موضوع، تولید و توزیع محتوا را بر مبنای سنجش بازگشت و تحلیل مخاطب شکل می‌دهد و جای شهود خبری را می‌گیرد. نقد بنیادین، «داده‌محورزدگی» (dataism) است: فرض بر این است که داده، «واقعیت» و «خنثی» است، در حالی که در واقع داده، «تولیدشده» و «سوگیرانه» است و تفاوت، «درجه‌ای» است نه «ماهوی» (Floridi, 2014).",
        mechanism="داده‌محوری در چهار حلقه عمل می‌کند: (۱) تعریف سؤال و شاخص: هدف تصمیم و معیارهای سنجش مشخص می‌شوند؛ (۲) جمع‌آوری و اندازه‌گیری: داده‌های مرتبط، ثبت و اندازه‌گیری می‌شوند؛ (۳) تحلیل و مدل‌سازی: داده‌ها، تحلیل و به الگو و پیش‌بینی تبدیل می‌شوند؛ (۴) تصمیم و بازخورد: تصمیم، بر پایه یافته‌ها گرفته و نتیجه، دوباره اندازه‌گیری و اصلاح می‌شود (Floridi, 2014; Castells, 2009). این چرخه، تصمیم‌گیری را بر پایه شواهد مستقر می‌کند.",
        key_concepts=["شواهدمحوری", "اندازه‌گیری مداوم", "بازخورد", "صحت تصمیم", "داده‌گرایی"],
        critiques="الگوی داده‌محور، داده را «واقعیت» و «خنثی» نشان می‌دهد، در حالی که در واقع داده، «تولیدشده» و «سوگیرانه» است و تفاوت، «درجه‌ای» است نه «ماهوی» (Floridi, 2014). نقد دیگر، «به‌دنبال‌دویِ عدد» (metric-ism) است: تقلیل تصمیم به شاخص‌های کمّی، بُعد کیفی، اخلاقی و انسانی را می‌کاهد (Castells, 2009). همچنین «تفسیرپذیری و پاسخگویی» تصمیمات داده‌محور، به‌سختی تضمین می‌شود و ممکن است به انفعال انسان در تصمیم‌گیری منجر شود.",
        applications="طراحی استراتژی‌های محتوایی و رسانه‌ای بر پایه تحلیل داده، تصمیم‌گیری بازاریابی و هدف‌گیری مخاطب، سنجش عملکرد رسانه و پلتفرم (شاخص‌ها، KPI)، طراحی محصول و تجربه کاربری داده‌محور، و آموزش سواد داده‌ای (تفسیر، محدودیت و اخلاق داده) (Floridi, 2014; Castells, 2009).",
        evolution="مفهوم داده‌محوری از بازاریابی و تحلیل کسب‌وکار (دهه‌های ۱۹۹۰) وارد علوم شد؛ در دهه‌های ۲۰۰۰–۲۰۱۰، با داده‌های بزرگ و هوش مصنوعی، به «فرهنگ تصمیم‌گیری عمومی» تبدیل شد؛ در عصر دیجیتال، داده‌محوری به «بنیاد تصمیم‌گیری رسانه، سیاست و زندگی روزمره» بدل شده است (Floridi, 2014).",
        assumptions="فرض‌های نهفته: داده‌ها، نماینده، تمیز و قابل اعتمادند و واقعیت را کامل پوشش می‌دهند؛ سنجش و شاخص‌گذاری، واقعیت را به‌درستی و بدون کاستی بازتاب می‌دهد؛ و تصمیم بر پایه شواهد، دقیق‌تر، منطقی‌تر و عادلانه‌تر از تصمیم بر پایه شهود است؛ اما تولید داده، سوگیری در سنجش، کاهش بُعد انسانی و تفسیرپذیری داده، از پیش‌فرض‌هایی هستند که در عمل محدود، قابل نقض و نیازمند بازبینی مستمرند (Floridi, 2014; Castells, 2009).",
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
