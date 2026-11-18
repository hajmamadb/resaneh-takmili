# -*- coding: utf-8 -*-
"""Batch 38 (THEORY): MC-049 Normative Theories of Journalism (Siebert, Peterson & Schramm 1956),
MC-079 Newsroom Ethnography (Tuchman 1978), MC-147 Customer-Based Brand Equity (Keller 1993),
MC-127 Corporate Reputation Management (Fombrun 1996). Verified 2026-11-16."""
import pymysql, json

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch38-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch38_theory.json"

S = {
 "MC-049": [  # Normative Theories of Journalism
   dict(kind="BOOK", title_en="Four Theories of the Press: The Authoritarian, Libertarian, Social Responsibility, and Soviet Communist Concepts of What the Press Should Be and Do",
        title_fa="چهار نظریهٔ مطبوعات: مفاهیم اقتدارگرا، آزادی‌خواه، مسئولیت اجتماعی و کمونیستی شوروی دربارهٔ آنچه مطبوعات باید باشد و انجام دهد",
        authors="Siebert, F. S., Peterson, T., & Schramm, W.", year=1956,
        publisher="Urbana: University of Illinois Press", doi=None, url=None, language="en", isbn=None,
        citation="Siebert, F. S., Peterson, T., & Schramm, W. (1956). Four theories of the press. University of Illinois Press.",
        locator="whole work", locator_type="work", supports="definition / four theories / normative typology", verified=True),
   dict(kind="BOOK", title_en="A Free and Responsible Press",
        title_fa="مطبوعاتی آزاد و مسئول", authors="Commission on Freedom of the Press", year=1947,
        publisher="Chicago: University of Chicago Press", doi=None, url=None, language="en", isbn=None,
        citation="Commission on Freedom of the Press. (1947). A free and responsible press. University of Chicago Press.",
        locator="whole work", locator_type="work", supports="social responsibility theory / origin", verified=False),
 ],
 "MC-079": [  # Newsroom Ethnography
   dict(kind="BOOK", title_en="Making News: A Study in the Construction of Reality",
        title_fa="ساختن خبر: پژوهشی در برساخت واقعیت", authors="Tuchman, G.", year=1978,
        publisher="New York: The Free Press", doi=None, url=None, language="en", isbn="0029329302",
        citation="Tuchman, G. (1978). Making news: A study in the construction of reality. The Free Press.",
        locator="whole work", locator_type="work", supports="definition / news net / routinization", verified=True),
   dict(kind="BOOK", title_en="Deciding What's News: A Study of CBS Evening News, NBC Nightly News, Newsweek, and Time",
        title_fa="تصمیم‌گیری دربارهٔ اینکه چه چیزی خبر است", authors="Gans, H. J.", year=1979,
        publisher="New York: Pantheon Books", doi=None, url=None, language="en", isbn=None,
        citation="Gans, H. J. (1979). Deciding what's news: A study of CBS Evening News, NBC Nightly News, Newsweek, and Time. Pantheon Books.",
        locator="whole work", locator_type="work", supports="evolution / values in news / comparative ethnography", verified=False),
 ],
 "MC-147": [  # Customer-Based Brand Equity
   dict(kind="JOURNAL_ARTICLE", title_en="Conceptualizing, Measuring, and Managing Customer-Based Brand Equity",
        title_fa="مفهوم‌سازی، سنجش و مدیریت برند‌ارزشی مشتری-بنیان",
        authors="Keller, K. L.", year=1993,
        publisher="Journal of Marketing, 57(1), 1-22", doi="10.1177/002224299305700101",
        url="https://journals.sagepub.com/doi/10.1177/002224299305700101", language="en", isbn=None,
        citation="Keller, K. L. (1993). Conceptualizing, measuring, and managing customer-based brand equity. Journal of Marketing, 57(1), 1-22. https://doi.org/10.1177/002224299305700101",
        locator="pp. 1-22", locator_type="page_range", supports="definition / brand knowledge / mechanism", verified=True),
   dict(kind="BOOK", title_en="Strategic Brand Management: Building, Measuring, and Managing Brand Equity",
        title_fa="مدیریت راهبردی برند: ساختن، سنجش و مدیریت برند‌ارزشی", authors="Keller, K. L.", year=2008,
        publisher="Upper Saddle River, NJ: Pearson Prentice Hall (3rd ed.)", doi=None, url=None, language="en", isbn=None,
        citation="Keller, K. L. (2008). Strategic brand management: Building, measuring, and managing brand equity (3rd ed.). Pearson Prentice Hall.",
        locator="whole work", locator_type="work", supports="evolution / CBBE pyramid", verified=False),
 ],
 "MC-127": [  # Corporate Reputation Management
   dict(kind="BOOK", title_en="Reputation: Realizing Value from the Corporate Image",
        title_fa="شهرت: تحقق ارزش از تصویر شرکتی", authors="Fombrun, C. J.", year=1996,
        publisher="Boston: Harvard Business School Press", doi=None, url=None, language="en", isbn="0875846335",
        citation="Fombrun, C. J. (1996). Reputation: Realizing value from the corporate image. Harvard Business School Press.",
        locator="whole work", locator_type="work", supports="definition / reputational capital / mechanism", verified=True),
   dict(kind="BOOK", title_en="Fame and Fortune: How Successful Companies Build Winning Reputations",
        title_fa="نام و ثروت: شرکت‌های موفق چگونه شهرت‌های برنده می‌سازند", authors="Fombrun, C. J., & van Riel, C. B. M.", year=2004,
        publisher="Upper Saddle River, NJ: Prentice Hall", doi=None, url=None, language="en", isbn=None,
        citation="Fombrun, C. J., & van Riel, C. B. M. (2004). Fame and fortune: How successful companies build winning reputations. Prentice Hall.",
        locator="whole work", locator_type="work", supports="evolution / drivers and measurement", verified=False),
 ],
}

ENRICH = {
 "MC-049": {
   "summary": "«نظریه‌های هنجاری روزنامه‌نگاری» (Normative Theories of Journalism) چارچوبی است که در کتاب «Four Theories of the Press» فرد سیبرت، تئودور پترسون و ویلبر شرام (۱۹۵۶، University of Illinois Press) ارائه شد. این اثر نظام‌های مطبوعاتی را بر پایهٔ مفروضات فلسفی دربارهٔ رابطهٔ مطبوعات با دولت و جامعه، به چهار نظریهٔ «اقتدارگرا»، «آزادی‌خواه»، «مسئولیت اجتماعی» و «کمونیستی شوروی» طبقه‌بندی کرد (Siebert, Peterson, & Schramm, 1956).",
   "main_problem": "معیارهای هنجاری مناسب برای سامان‌دهی مطبوعات و رسانه‌ها در چه چارچوب‌های فکری ریشه دارند، و چگونه می‌توان تفاوت‌های نظام‌های رسانه‌ای کشورها را بر پایهٔ رابطهٔ مطبوعات با قدرت توضیح داد؟",
   "mechanism": "کتاب چهار الگوی هنجاری را از هم متمایز می‌کند: (۱) «اقتدارگرا» (authoritarian) — مطبوعات تابع قدرت حاکم‌اند و مجوز، سانسور و مجازات رسمی ابزار کنترل‌اند؛ (۲) «آزادی‌خواه» (libertarian) — مطبوعات در «بازار افکار» (marketplace of ideas) آزادند و حقیقت از رقابت دیدگاه‌ها برمی‌آید؛ (۳) «مسئولیت اجتماعی» (social responsibility) — که پس از گزارش کمیسیون آزادی مطبوعات (1947) طرح شد و مطبوعات را آزاد اما «مسئول» در برابر منافع عمومی می‌داند: انتشار حقیقت، زمینه‌سازی برای گفت‌وگوی عمومی و پرهیز از آسیب؛ (۴) «کمونیستی شوروی» (Soviet communist) — رسانه ابزار حزب و دولت برای پروژهٔ اجتماعی است (Siebert, Peterson, & Schramm, 1956). در این چارچوب، هر نظریه ترکیبی از پاسخ به پرسش‌هایی دربارهٔ مالکیت، آزادی، نظارت و وظیفهٔ رسانه است.",
   "assumptions": [
     "نظام رسانه‌ای هر جامعه بازتاب مفروضات فلسفی و سیاسی آن دربارهٔ حقیقت، آزادی و اقتدار است.",
     "مطبوعات را می‌توان بر پایهٔ رابطه با دولت و وظیفهٔ اجتماعی، در الگوهای قابل‌مقایسه طبقه‌بندی کرد.",
     "نظریهٔ «مسئولیت اجتماعی» تعادلی هنجاری میان آزادی و پاسخ‌گویی است."
   ],
   "principles": [
     "چهارگانهٔ هنجاری: اقتدارگرا، آزادی‌خواه، مسئولیت اجتماعی و کمونیستی، الگوهای متمایز رابطهٔ رسانه و قدرت‌اند.",
     "آزادی مشروط: در الگوی مسئولیت اجتماعی، آزادی بدون مسئولیت در برابر منافع عمومی توجیه ندارد.",
     "بافت ملی: تعریف «وظیفهٔ مطبوعات» محصول تجربهٔ تاریخی هر جامعه است."
   ],
   "critiques": [
     "دوقطبی جنگ سرد: چهارگانه با منطق جنگ سرد ساخته شده و جهان را به دو قطب آزاد و غیرآزاد تقسیم می‌کند.",
     "نقصان پوشش: بسیاری از نظام‌های رسانه‌ای (از جمله الگوهای توسعه‌ای، اقتدارگرای نوین و رسانه‌های اجتماعی) در آن جای نمی‌گیرند.",
     "غرب‌محوری: نظریه از تجربهٔ آمریکا و اروپا استخراج شده و مفروضات آن در بافت‌های غیرغربی تعمیم‌پذیر نیست."
   ],
   "applications": [
     "مقایسهٔ نظام‌های رسانه‌ای کشورها و تحلیل سیاست‌های مطبوعاتی.",
     "آموزش اصول هنجاری روزنامه‌نگاری و اخلاق حرفه‌ای.",
     "تحلیل مبنایی در پژوهش‌های مقایسه‌ای رسانه و سیاست."
   ],
   "evolution": "کتاب ۱۹۵۶ به اثری بنیادین در مطالعات تطبیقی رسانه بدل شد. از دههٔ ۱۹۷۰، نقدهای پسااستعماری و مقایسه‌ای به چهارگانه افزودند و کوشش‌های بعدی (از جمله کریستینز و همکاران، ۲۰۰۹) الگوهای «پایشگر، تسهیل‌گر، رادیکال و مشارکتی» را پیشنهاد کردند. امروزه نظریه‌های هنجاری رسانه با پرسش‌هایی دربارهٔ حکمرانی پلتفرمی و تنوع نظام‌های رسانه‌ای غیرغربی بازخوانی می‌شوند.",
   "key_concepts": ["نظریهٔ اقتدارگرا (authoritarian theory)", "نظریهٔ آزادی‌خواه (libertarian theory)", "نظریهٔ مسئولیت اجتماعی (social responsibility theory)", "نظریهٔ کمونیستی شوروی (Soviet communist theory)", "بازار افکار (marketplace of ideas)"],
   "studies": ["Siebert, F. S., Peterson, T., & Schramm, W. (1956). Four Theories of the Press. University of Illinois Press.", "Commission on Freedom of the Press. (1947). A Free and Responsible Press. University of Chicago Press."],
 },
 "MC-079": {
   "summary": "«قوم‌نگاری تحریریه» (Newsroom Ethnography) رویکردی پژوهشی است که با مشاهدهٔ میدانی و مصاحبه در اتاق خبر، فرایند تولید خبر و ساخت اجتماعی واقعیت خبری را بررسی می‌کند. گای تاکمن در کتاب «Making News» (۱۹۷۸، The Free Press) با قوم‌نگاری تحریریه‌های روزنامه و تلویزیون نشان داد که «خبر» نه آینهٔ واقعیت، بلکه محصول رویه‌های سازمانی، شبکه‌ها و مقولات حرفه‌ای است (Tuchman, 1978).",
   "main_problem": "چه سازوکارهای سازمانی، حرفه‌ای و عملی در اتاق خبر تعیین می‌کنند که چه رویدادی «خبر» شود، و چگونه این سازوکارها به برساخت واقعیتی خاص می‌انجامند؟",
   "mechanism": "تاکمن مکانیسم را در سه سطح توضیح می‌دهد: (۱) «شبکهٔ خبری» (news net) — سازمان‌های خبری با تخصیص خبرنگار به منابع ثابت (پلیس، دولت، دادگاه) رویدادها را می‌پایند و ناگزیر بخشی از واقعیت را از شبکه عبور می‌دهند؛ (۲) «روتین‌سازی» (routinization) — مقولات خبری، برنامهٔ زمانی و معیارهای «ارزش خبری» به کار روزمره نظم می‌دهند و پیش‌بینی‌پذیر می‌سازند؛ (۳) «نوع‌سازی» (typification) — خبرنگاران رویدادها را در قالب‌های آشنا (جرم، بحران، سیاست) دسته‌بندی می‌کنند و معنای آن‌ها را بازسازی می‌کنند (Tuchman, 1978). تاکمن همچنین «عینیت» را «آیین راهبردی» توصیف کرد: مجموعه رویه‌هایی که روزنامه‌نگار را در برابر انتقاد محافظت می‌کند. نتیجه این است که خبر، «واقعیتِ نهادینه‌شده» است، نه انعکاس بی‌واسطهٔ جهان.",
   "assumptions": [
     "خبر محصول فرایند سازمانی است و در اتاق خبر ساخته و پردازش می‌شود.",
     "رویه‌ها و مقولات حرفه‌ای، مستقل از محتوای هر رویداد، گزینش و معناسازی خبر را شکل می‌دهند.",
     "مشاهدهٔ میدانی، روش مناسب برای فهم کنش روزمرهٔ روزنامه‌نگاران است."
   ],
   "principles": [
     "برساخت‌گرایی: خبر بازنمایی برساختهٔ واقعیت است، نه بازتاب بی‌واسطهٔ آن.",
     "روتین و نظم سازمانی: قواعد زمانی و منابع، گزینش خبر را ممکن و محدود می‌کنند.",
     "بازتاب نهادی: ساختار سازمان خبر، در محتوای خبر بازتاب می‌یابد."
   ],
   "critiques": [
     "تعمیم‌پذیری محدود: مطالعات موردی در تحریریه‌های خاص، ممکن است نمایندهٔ همهٔ سازمان‌های خبری نباشند.",
     "قدمت و تحول دیجیتال: یافته‌های دههٔ ۱۹۷۰ پیش از تحول دیجیتال و کار از راه دور تولید شده‌اند.",
     "کم‌توجهی به مخاطب: تمرکز بر درون تحریریه، نقش مخاطب و بافت دریافت خبر را کم‌رنگ می‌کند."
   ],
   "applications": [
     "مطالعهٔ تولید خبر و تحولات تحریریه در عصر دیجیتال و داده‌محور.",
     "تحلیل سوگیری رسانه و رابطهٔ سازمان خبر با منابع قدرت.",
     "پژوهش دربارهٔ کار روزنامه‌نگاران، فشارهای شغلی و اخلاق حرفه‌ای."
   ],
   "evolution": "قوم‌نگاری تحریریه از مطالعات دروازه‌بانی دههٔ ۱۹۵۰ و کار تاکمن (1978) و گنز (1979) شکل گرفت. در دهه‌های بعد، با ورود اینترنت، رسانه‌های اجتماعی و تحلیل داده، پژوهش‌های تحریریهٔ دیجیتال و «قوم‌نگاری خبر آنلاین» توسعه یافت و بحث «خبر به‌عنوان داده» و کار الگوریتمی به آن افزوده شد.",
   "key_concepts": ["قوم‌نگاری تحریریه (newsroom ethnography)", "شبکهٔ خبری (news net)", "روتین‌سازی خبر (routinization)", "نوع‌سازی (typification)", "برساخت اجتماعی واقعیت (social construction of reality)"],
   "studies": ["Tuchman, G. (1978). Making News. The Free Press.", "Gans, H. J. (1979). Deciding What's News. Pantheon Books."],
 },
 "MC-147": {
   "summary": "«برند‌ارزشی مشتری-بنیان» (Customer-Based Brand Equity - CBBE) چارچوبی است که کوین لین کلر در مقالهٔ «Conceptualizing, Measuring, and Managing Customer-Based Brand Equity» (۱۹۹۳، Journal of Marketing) معرفی کرد. برند‌ارزشی مشتری-بنیان را «اثر تفاضلی دانش برند بر واکنش مصرف‌کننده به بازاریابی برند» تعریف کرد؛ یعنی ارزش افزوده‌ای که برند در ذهن مصرف‌کننده و در پاسخ او به محصول ایجاد می‌کند (Keller, 1993).",
   "main_problem": "برند چگونه در ذهن مصرف‌کننده ارزش می‌سازد، این ارزش از چه اجزایی تشکیل می‌شود، و چگونه می‌توان آن را سنجید و مدیریت کرد؟",
   "mechanism": "کلر مکانیسم را از طریق «دانش برند» (brand knowledge) توضیح می‌دهد که دو مؤلفه دارد: (۱) «آگاهی از برند» (brand awareness) شامل تشخیص و یادآوری برند؛ (۲) «تصویر برند» (brand image) یعنی مجموعهٔ تداعی‌های ذهنی دربارهٔ برند. برند‌ارزشی زمانی بالا می‌رود که مصرف‌کننده با برند آشنا باشد و تداعی‌هایی «قوی، مطلوب و منحصربه‌فرد» (strong, favorable, unique) در ذهن او شکل گرفته باشد؛ این تداعی‌ها در مقایسه با برندهای رقیب، مزیت ذهنی می‌سازند (Keller, 1993). در توسعهٔ بعدی، کلر «هرم برند‌ارزشی» را معرفی کرد: برجستگی (salience) → عملکرد و تصویرسازی (performance/imagery) → داوری‌ها و احساسات (judgments/feelings) → طنین برند (resonance). بنابراین برند‌ارزشی، سازه‌ای چندلایه و سازگار با سنجش پیمایشی است.",
   "assumptions": [
     "دانش برند در حافظهٔ مصرف‌کننده نهفته است و واکنش او به بازاریابی را تغییر می‌دهد.",
     "تداعی‌های قوی، مطلوب و منحصربه‌فرد، ارزش ویژهٔ برند را می‌سازند و قابل‌سنجش‌اند.",
     "مدیریت برند مستلزم مدیریت نظام‌مند آگاهی و تصویر در طول زمان است."
   ],
   "principles": [
     "دانش برند: برند‌ارزشی از آگاهی و تصویر شکل می‌گیرد.",
     "تمایز تداعی: uniqueness در کنار strength و favorability، مزیت رقابتی ذهنی می‌سازد.",
     "سلسله‌مراتب: برند‌ارزشی در لایه‌های متوالی از برجستگی تا طنین ساخته می‌شود."
   ],
   "critiques": [
     "مصرف‌کننده‌محوری افراطی: مدل بیشتر بر ذهن مصرف‌کننده متمرکز است و ابعاد اجتماعی، فرهنگی و ذی‌نفعان دیگر را کم‌رنگ می‌کند.",
     "سنجش‌پذیری: پیوند تداعی‌های ذهنی با ارزش مالی برند و مدل‌سازی آن پیچیده است.",
     "بافت بازار: الگو در بازارهای مصرفی توسعه یافته و کاربرد آن در بازارهای صنعتی، B2B و عمومی نیازمند انطباق است."
   ],
   "applications": [
     "طراحی و ارزیابی راهبردهای برندسازی و کمپین‌های تبلیغاتی.",
     "پژوهش بازار و سنجش سلامت برند در صنایع مصرفی.",
     "مدیریت برند در رسانه‌ها و پلتفرم‌ها (برند شبکه، برنامه و شخصیت)."
   ],
   "evolution": "کلر (1993) مفهوم و سنجه‌های آن را بنیان نهاد و در «Strategic Brand Management» و مقالهٔ ۲۰۰۱، هرم برند‌ارزشی را به ابزاری عملیاتی بدل کرد. در دو دههٔ بعد، مدل با پژوهش‌های عصرشناختی، برند‌ارزشی کارکنان و برند‌ارزشی مبتنی بر داده گسترش یافت.",
   "key_concepts": ["برند‌ارزشی مشتری-بنیان (customer-based brand equity)", "دانش برند (brand knowledge)", "آگاهی از برند (brand awareness)", "تصویر برند (brand image)", "طنین برند (brand resonance)"],
   "studies": ["Keller, K. L. (1993). CBBE. Journal of Marketing, 57(1), 1-22.", "Keller, K. L. (2008). Strategic Brand Management (3rd ed.). Pearson Prentice Hall."],
 },
 "MC-127": {
   "summary": "«مدیریت شهرت شرکتی» (Corporate Reputation Management) حوزه‌ای است که در آن شهرت سازمان به‌عنوان دارایی راهبردی تلقی و به‌طور نظام‌مند ساخته، پایش و از آن حفاظت می‌شود. چارلز فامبرون در کتاب «Reputation: Realizing Value from the Corporate Image» (۱۹۹۶، Harvard Business School Press) شهرت را «بازنمایی جمعی از عملکرد گذشته و چشم‌انداز آیندهٔ شرکت» تعریف کرد که در صورت مثبت، «سرمایهٔ شهرتی» (reputational capital) می‌آفریند (Fombrun, 1996).",
   "main_problem": "شهرت چگونه شکل می‌گیرد و به ارزش اقتصادی و رقابتی تبدیل می‌شود، چه عواملی آن را می‌سازند، و سازمان‌ها چگونه می‌توانند آن را مدیریت و در بحران حفاظت کنند؟",
   "mechanism": "فامبرون مکانیسم را در قالب زنجیرهٔ ارزش شهرتی توضیح می‌دهد: (۱) شهرت از ادراک ذی‌نفعان دربارهٔ «عملکرد محصول/خدمت»، «عملکرد مالی»، «چشم‌انداز و رهبری»، «محیط کار»، «مسئولیت اجتماعی» و «جذابیت عاطفی» ساخته می‌شود؛ (۲) این ادراک‌ها در تعامل با رسانه، بازار و تجربهٔ مستقیم شکل می‌گیرند و در قالب «نمرهٔ شهرت» سازمان‌های سنجش تجمیع می‌شوند؛ (۳) شهرت مثبت هزینهٔ مبادله را کاهش می‌دهد، دسترسی به سرمایه و استعداد را آسان‌تر می‌کند و در بحران، «بالشتکی» برای جذب شوک فراهم می‌سازد؛ (۴) برعکس، بحران‌های شهرتی می‌توانند سرمایهٔ شهرتی را به‌سرعت فرسوده کنند (Fombrun, 1996). مدیریت شهرت بنابراین شامل پایش ادراک، هم‌سوسازی ارتباطات و رفتار، و آمادگی بحران است.",
   "assumptions": [
     "شهرت یک دارایی نامشهود و ارزش‌آفرین است که می‌توان آن را اندازه‌گیری و مدیریت کرد.",
     "ادراک ذی‌نفعان از عملکرد و رفتار سازمان، سازندهٔ شهرت است، نه صرفاً تبلیغات.",
     "شهرت مثبت، مزیت رقابتی و ظرفیت جذب شوک ایجاد می‌کند."
   ],
   "principles": [
     "شهرت بر پایهٔ رفتار ساخته می‌شود: گفتار بدون عملکرد، شهرت پایدار نمی‌سازد.",
     "چندذی‌نفعی: ادراک گروه‌های مختلف (مشتری، سرمایه‌گذار، کارمند، جامعه) به هم مرتبط است.",
     "پایش مستمر: شهرت نیازمند سنجش دوره‌ای و پاسخ به تغییر ادراک‌هاست."
   ],
   "critiques": [
     "ابهام مفهومی: مرز شهرت با «هویت»، «تصویر» و «برند» روشن نیست و تعاریف متعدد، مقایسهٔ پژوهش‌ها را دشوار می‌کند.",
     "مسئلهٔ سنجش: رتبه‌بندی‌های شهرت به‌شدت به روش و نمونه وابسته‌اند و ممکن است سوگیری داشته باشند.",
     "کوتاه‌مدت‌گرایی: تمرکز بر «مدیریت تصویر» می‌تواند به جای اصلاح رفتار، به آرایش ادراک و روابط عمومی نمایشی بیانجامد."
   ],
   "applications": [
     "مدیریت شهرت و ارتباطات بحران در شرکت‌ها و سازمان‌های عمومی.",
     "سنجش سرمایهٔ شهرتی و پایش رسانه‌ای و اجتماعی.",
     "راهبرد ارتباطات شرکتی، مسئولیت اجتماعی و جذب استعداد."
   ],
   "evolution": "فامبرون (1996) چارچوب سرمایهٔ شهرتی را تثبیت کرد و با همکارانش ابزارهای سنجش شهرت را توسعه داد. در ادامه، پژوهش‌های «شهرت در رسانه‌های اجتماعی»، مدیریت شهرت داده‌محور و پیوند شهرت با پایداری و ESG شکل گرفت. امروزه مدیریت شهرت به هستهٔ ارتباطات راهبردی سازمانی بدل شده است.",
   "key_concepts": ["شهرت شرکتی (corporate reputation)", "سرمایهٔ شهرتی (reputational capital)", "ادراک ذی‌نفعان (stakeholder perception)", "مدیریت بحران شهرتی (reputation crisis management)", "سنجش شهرت (reputation measurement)"],
   "studies": ["Fombrun, C. J. (1996). Reputation. Harvard Business School Press.", "Fombrun, C. J., & van Riel, C. B. M. (2004). Fame and Fortune. Prentice Hall."],
 },
}

REQUIRED_SECTIONS = ["summary", "definition", "main_problem", "mechanism", "assumptions",
                     "principles", "critiques", "applications", "evolution", "key_concepts",
                     "theorists", "model", "studies"]

def wc(v):
    if isinstance(v, str): return len(v.split())
    if isinstance(v, list):
        n = 0
        for it in v:
            if isinstance(it, str): n += len(it.split())
            elif isinstance(it, dict): n += len(' '.join(str(x) for x in it.values()).split())
        return n
    if isinstance(v, dict): return len(' '.join(str(x) for x in v.values()).split())
    return 0

def has_content(v):
    if v is None: return False
    if isinstance(v, str): return len(v.strip()) > 10
    if isinstance(v, (list, dict)): return len(v) > 0
    return True

def rubric(p, n_verified, n_sources, n_relations):
    detail = {}
    present = [k for k in REQUIRED_SECTIONS if has_content(p.get(k))]
    detail["structure_15"] = round(15 * min(1, len(present)/7))
    words = sum(wc(p.get(k)) for k in ["summary","definition","main_problem","mechanism",
                "critiques","applications","evolution","key_concepts","principles","studies","assumptions"])
    a = 15 if words>=500 else 13 if words>=300 else 11 if words>=180 else 8 if words>=100 else 3
    detail["analysis_15"] = a
    if n_verified>=1 and n_sources>=2: detail["citation_20"] = 20
    elif n_verified>=1: detail["citation_20"] = 17
    elif n_sources>=1: detail["citation_20"] = 10
    else: detail["citation_20"] = 0
    acc = 0
    if has_content(p.get("summary")) or has_content(p.get("definition")): acc += 10
    if n_verified>=1: acc += 9
    if len(present)>=6: acc += 6
    detail["accuracy_25_auto"] = min(25, acc)
    detail["relations_10"] = 10 if n_relations>=1 else 6
    detail["classification_5"] = 5 if (p.get("field") or p.get("mapping")) else 2
    detail["clarity_5"] = 5 if has_content(p.get("summary")) else 2
    detail["currency_5"] = 5
    return min(100, sum(detail.values())), detail

def main():
    c = pymysql.connect(host="127.0.0.1", user="root", password="433700", database=DB, charset="utf8mb4", autocommit=False)
    cur = c.cursor()
    codes = ["MC-049", "MC-079", "MC-147", "MC-127"]
    cur.execute("SELECT id, code, properties FROM kb_entities WHERE code IN (%s)" % ",".join(["%s"]*len(codes)), codes)
    rows = {code:(eid, json.loads(pr)) for (eid, code, pr) in cur.fetchall()}
    with open(BACKUP, "w", encoding="utf-8") as f:
        json.dump([{"code": cd, "props": rows[cd][1]} for cd in codes if cd in rows], f, ensure_ascii=False, indent=1)
    print("backup ->", len(rows), "rows")

    for code in codes:
        eid, p = rows[code]
        for k, v in ENRICH[code].items():
            p[k] = v
        if not has_content(p.get("definition")) and has_content(p.get("summary")):
            p["definition"] = p["summary"]
        spec = S[code]
        p["sources"] = [dict(citation=s["citation"], language=("انگلیسی" if s["language"]=="en" else "فارسی"),
                              doi=s.get("doi") or "", url=s.get("url") or "", year=s.get("year")) for s in spec]
        p["citations"] = [dict(source=s["citation"], locator=s["locator"], supports=s["supports"],
                               verified=bool(s.get("verified"))) for s in spec]
        n_sources = len(spec)
        n_verified = sum(1 for s in spec if s.get("verified"))
        cur.execute("SELECT COUNT(*) FROM kb_relations r JOIN kb_entities a ON r.source_id=a.id JOIN kb_entities b ON r.target_id=b.id WHERE a.code=%s OR b.code=%s", (code, code))
        n_relations = cur.fetchone()[0]
        score, detail = rubric(p, n_verified, n_sources, n_relations)
        p["quality_score"] = score
        p["quality_assessment"] = dict(breakdown=detail, total=score,
            method="SPEC §6.1 auto-structural (accuracy is auto-credit, NOT human verification)",
            scored_at=NOW, scored_by=STAMP)
        p["status_scientific_note"] = "score is structural/citation-based; requires human expert review for scientific verification (SPEC §6.4)"
        p["updated_at"] = NOW; p["updated_by"] = STAMP
        cur.execute("UPDATE kb_entities SET properties=%s, version=version+1, updated_at=%s, updated_by=%s WHERE id=%s",
                    (json.dumps(p, ensure_ascii=False), NOW, STAMP, eid))
        for s in spec:
            sid = None
            if s.get("doi"):
                cur.execute("SELECT id FROM kb_sources WHERE doi=%s", (s["doi"],))
                r = cur.fetchone(); sid = r[0] if r else None
            if sid is None:
                cur.execute("SELECT id FROM kb_sources WHERE title_en=%s AND year=%s", (s["title_en"], s.get("year")))
                r = cur.fetchone(); sid = r[0] if r else None
            if sid is None:
                cur.execute("""INSERT INTO kb_sources (kind,title_fa,title_en,year,publisher,doi,isbn,url,language,access_type,bibliographic)
                                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                    (s["kind"], s.get("title_fa"), s["title_en"], s.get("year"), s.get("publisher"),
                     s.get("doi"), s.get("isbn"), s.get("url"), s.get("language"),
                     "open" if (s.get("doi") or s.get("url")) else "unknown",
                     json.dumps({"authors": s.get("authors"), "citation": s["citation"]}, ensure_ascii=False)))
                sid = cur.lastrowid
            cur.execute("SELECT 1 FROM kb_evidence e WHERE e.about_code=%s AND e.source_id=%s LIMIT 1", (code, sid))
            if cur.fetchone(): continue
            lt = "PAGE" if s.get("locator_type") == "page_range" else ("CHAPTER" if s.get("locator_type") == "CHAPTER" else "SECTION")
            cur.execute("""INSERT INTO kb_citations (source_id,locator_type,locator_value,paraphrase,citation_style,language,accessed_at)
                            VALUES (%s,%s,%s,%s,'apa',%s,%s)""",
                        (sid, lt, s.get("locator"), "پشتیبانی از بخش: "+s.get("supports",""), s.get("language","en"), NOW))
            cid = cur.lastrowid
            cur.execute("""INSERT INTO kb_evidence (source_id,citation_id,about_code,evidence_type,evidence_summary,locator,verification_status,extraction_method,direction)
                            VALUES (%s,%s,%s,'bibliographic_reference',%s,%s,%s,'ai_extraction','supports')""",
                        (sid, cid, code, s["citation"], s.get("locator"), "verified" if s.get("verified") else "unverified"))
        cur.execute("SELECT COALESCE(MAX(version),0)+1 FROM kb_entity_versions WHERE entity_id=%s", (eid,))
        ver = cur.fetchone()[0]
        cur.execute("INSERT INTO kb_entity_versions (entity_id, version, snapshot, change_reason, changed_by, created_at) VALUES (%s,%s,%s,%s,%s,%s)",
                    (eid, ver, json.dumps({"quality_score": score, "sources": n_sources, "verified": n_verified}, ensure_ascii=False),
                     "documented sourcing + rubric score", STAMP, NOW))
        cur.execute("INSERT INTO kb_audit_log (entity_code, action, detail, source) VALUES (%s,%s,%s,%s)",
                    (code, "DOC_ENRICH", json.dumps({"quality_score": score, "sources": n_sources, "verified": n_verified, "breakdown": detail}, ensure_ascii=False), STAMP))
        print(f"{code}: score={score} sources={n_sources} verified={n_verified} relations={n_relations} | {detail}")
    c.commit()
    c.close()
    print("BATCH38 THEORY DONE")

if __name__ == "__main__":
    main()
