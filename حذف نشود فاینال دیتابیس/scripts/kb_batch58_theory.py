# -*- coding: utf-8 -*-
"""Batch 58 (THEORY): MC-283 The New Jim Code (Benjamin 2019), MC-284 Data Justice (Taylor 2017),
MC-287 Commons Governance & Design Principles (Ostrom 1990), MC-288 Value Sensitive Design (Friedman, Kahn & Borning 2006).
Anchors verified 2026-11-16."""
import pymysql, json

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch58-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch58_theory.json"

S = {
 "MC-283": [
   dict(kind="BOOK", title_en="Race After Technology: Abolitionist Tools for the New Jim Code",
        title_fa="نژاد پس از فناوری: ابزارهای الغاگرایانه برای کد جیم جدید",
        authors="Benjamin, R.", year=2019, publisher="Cambridge: Polity Press", doi=None,
        url="https://www.politybooks.com/bookdetail?book_slug=race-after-technology-abolitionist-tools-for-the-new-jim-code--9781509526390",
        language="en", isbn="9781509526390",
        citation="Benjamin, R. (2019). Race after technology: Abolitionist tools for the New Jim Code. Polity Press.",
        locator="whole work", locator_type="work", supports="definition / engineered inequity / coded exposure", verified=True),
   dict(kind="BOOK", title_en="Algorithms of Oppression: How Search Engines Reinforce Racism",
        title_fa="الگوریتم‌های ستم: چگونه موتورهای جست‌وجو نژادپرستی را بازتولید می‌کنند",
        authors="Noble, S. U.", year=2018, publisher="New York: New York University Press", doi=None, url=None,
        language="en", isbn=None,
        citation="Noble, S. U. (2018). Algorithms of oppression: How search engines reinforce racism. New York University Press.",
        locator="whole work", locator_type="work", supports="evolution / search engine bias", verified=False),
 ],
 "MC-284": [
   dict(kind="JOURNAL_ARTICLE", title_en="What Is Data Justice? The Case for Connecting Digital Rights and Freedoms Globally",
        title_fa="عدالت داده چیست؟ دعوی پیوند حقوق و آزادی‌های دیجیتال در سطح جهانی",
        authors="Taylor, L.", year=2017,
        publisher="Big Data & Society, 4(2), 1-14", doi="10.1177/2053951717736335",
        url="https://journals.sagepub.com/doi/full/10.1177/2053951717736335",
        language="en", isbn=None,
        citation="Taylor, L. (2017). What is data justice? The case for connecting digital rights and freedoms globally. Big Data & Society, 4(2), 1-14.",
        locator="pp. 1-14", locator_type="page_range", supports="definition / three pillars / global framing", verified=True),
   dict(kind="JOURNAL_ARTICLE", title_en="Data Justice for Development: What Would It Mean?",
        title_fa="عدالت داده برای توسعه: چه معنایی می‌تواند داشته باشد؟",
        authors="Heeks, R., & Renken, J.", year=2018,
        publisher="Information Development, 34(1), 90-102", doi=None, url=None, language="en", isbn=None,
        citation="Heeks, R., & Renken, J. (2018). Data justice for development: What would it mean? Information Development, 34(1), 90-102.",
        locator="pp. 90-102", locator_type="page_range", supports="evolution / data justice in development", verified=False),
 ],
 "MC-287": [
   dict(kind="BOOK", title_en="Governing the Commons: The Evolution of Institutions for Collective Action",
        title_fa="حاکمیت مشترکات: تکامل نهادها برای کنش جمعی",
        authors="Ostrom, E.", year=1990, publisher="Cambridge: Cambridge University Press",
        doi="10.1017/CBO9780511807763",
        url="https://www.cambridge.org/core/books/governing-the-commons/7AB7AE11BADA84409C34815CC288CD79",
        language="en", isbn="9780521405997",
        citation="Ostrom, E. (1990). Governing the commons: The evolution of institutions for collective action. Cambridge University Press.",
        locator="whole work", locator_type="work", supports="definition / design principles / polycentric governance", verified=True),
   dict(kind="JOURNAL_ARTICLE", title_en="Beyond Markets and States: Polycentric Governance of Complex Economic Systems",
        title_fa="فراتر از بازار و دولت: حاکمیت چندمرکزی نظام‌های اقتصادی پیچیده",
        authors="Ostrom, E.", year=2010,
        publisher="American Economic Review, 100(3), 641-672", doi=None, url=None, language="en", isbn=None,
        citation="Ostrom, E. (2010). Beyond markets and states: Polycentric governance of complex economic systems. American Economic Review, 100(3), 641-672.",
        locator="pp. 641-672", locator_type="page_range", supports="evolution / polycentricity", verified=False),
 ],
 "MC-288": [
   dict(kind="BOOK_CHAPTER", title_en="Value Sensitive Design and Information Systems",
        title_fa="طراحی حساس به ارزش و نظام‌های اطلاعاتی",
        authors="Friedman, B., Kahn, P. H., Jr., & Borning, A.", year=2006,
        publisher="In P. Zhang & D. Galletta (Eds.), Human-Computer Interaction and Management Information Systems: Foundations (pp. 348-372). Armonk, NY: M.E. Sharpe",
        doi=None, url="https://cseweb.ucsd.edu/~goguen/courses/271/friedman04.pdf",
        language="en", isbn=None,
        citation="Friedman, B., Kahn, P. H., Jr., & Borning, A. (2006). Value sensitive design and information systems. In P. Zhang & D. Galletta (Eds.), Human-computer interaction and management information systems: Foundations (pp. 348-372). M.E. Sharpe.",
        locator="pp. 348-372", locator_type="page_range", supports="definition / tripartite methodology / value tensions", verified=True),
   dict(kind="BOOK", title_en="Human Values and the Design of Computer Technology",
        title_fa="ارزش‌های انسانی و طراحی فناوری رایانه",
        authors="Friedman, B. (Ed.)", year=2004, publisher="Stanford, CA: CSLI Publications", doi=None, url=None,
        language="en", isbn=None,
        citation="Friedman, B. (Ed.). (2004). Human values and the design of computer technology. CSLI Publications.",
        locator="whole work", locator_type="work", supports="evolution / origins of value sensitive design", verified=False),
 ],
}

ENRICH = {
 "MC-283": {
   "summary": "«کد جیم جدید» (The New Jim Code) مفهومی است برای توضیح اینکه چگونه فناوری‌های دیجیتال — از الگوریتم و هوش مصنوعی تا طراحی رابط — می‌توانند نابرابری نژادی را بازتولید یا عمیق‌تر کنند، آن هم در حالی که ظاهری بی‌طرف و حتی خیرخواهانه دارند. روها بنجامین در «Race After Technology» (۲۰۱۹، Polity) این مفهوم را با تکیه بر سنت نقد نژاد و الغاگری صورت‌بندی کرد (Benjamin, 2019).",
   "definition": "کد جیم جدید، بازتولید نژادپرستی از طریق طراحی فناورانه است؛ نه با قوانین تبعیض‌آمیز آشکار، بلکه با سوگیری‌های رمزگذاری‌شده، پیش‌فرض‌های نامرئی و ادعای بی‌طرفی فنی که تبعیض را پنهان و مشروع می‌کند (Benjamin, 2019).",
   "main_problem": "اگر فناوری به‌ظاهر خنثی است و تبعیض نژادی آشکار در آن وجود ندارد، چگونه نابرابری در خروجی الگوریتم‌ها، طراحی محصول و سیاست پلتفرم بازتولید می‌شود، و چه ابزارهای نظری و عملی برای مقاومت و بازطراحی وجود دارد؟",
   "mechanism": "استدلال بنجامین در چهار سطح کار می‌کند. (۱) سه شیوهٔ رمزگذاری نابرابری: طراحی می‌تواند نژادپرستی را «آشکارا تقویت کند» (مانند بازاریابی هدفمند تبعیض‌آمیز)، می‌تواند تفاوت نژادی را «نادیده بگیرد و در همان حال رمزگذاری کند» (نظام‌هایی که با فرض بی‌طرفی، الگوهای نابرابر را بازتولید می‌کنند)، و می‌تواند سوگیری را «پشت پوشش فنی پنهان کند» — همان چیزی که بنجامین (۲۰۱۹) «کد جیم جدید» می‌نامد. (۲) تقابل با نژادپرستی آشکار: همان‌گونه که نظام جیم کرو با قوانین صریح جداسازی کار می‌کرد، کد جیم جدید با سازوکارهای غیرشخصی و ادعای علمی عمل می‌کند؛ همین ادعای بی‌طرفی، نقد را دشوارتر و مشروعیت تبعیض را بیشتر می‌کند. (۳) مفاهیم تحلیلی: «نابرابری مهندسی‌شده» (engineered inequity) اشاره به طراحی‌ای دارد که نابرابری را در پیش‌فرض‌های خود می‌گنجاند؛ «تبعیض پیش‌فرض» (default discrimination) به سوگیری‌هایی اشاره دارد که بی‌آنکه کسی تصمیم تبعیض‌آمیز گرفته باشد، از داده و طراحی برمی‌آیند؛ و «مواجههٔ کدگذاری‌شده» (coded exposure) به آسیب‌پذیری افتراقی گروه‌ها در برابر نظارت و خطای سیستم‌ها. (۴) ابزارهای الغاگری: بنجامین از «تخیل الغاگرایانه» و «فناوری مردمی» دفاع می‌کند: طراحی از پایین، مشارکت جوامع آسیب‌دیده و ساخت جایگزین‌هایی که نابرابری را بازتولید نکنند. در بستر رسانه، این چارچوب به تحلیل بازنمایی الگوریتمی، تبلیغات هدفمند، تشخیص چهره در تحریریه و تعدیل محتوا راه می‌برد و توضیح می‌دهد چرا بی‌طرفی ادعایی سیستم، تضمینی برای عدالت نیست.",
   "assumptions": [
     "فناوری محصول انتخاب‌های انسانی و روابط اجتماعی است، نه ابزاری خنثی.",
     "سوگیری می‌تواند بدون قصد تبعیض‌آمیز فردی، در داده و طراحی بازتولید شود.",
     "ادعای بی‌طرفی فنی، نقد و اصلاح تبعیض را دشوارتر می‌کند."
   ],
   "principles": [
     "طراحی فناوری می‌تواند نابرابری را تقویت، نادیده یا پنهان کند.",
     "تبعیض پیش‌فرض از داده و طراحی برمی‌آید، نه لزوماً از نیت عامل انسانی.",
     "اصلاح تبعیض به مشارکت جوامع آسیب‌دیده و طراحی جایگزین نیازمند است."
   ],
   "critiques": [
     "چارچوب عمدتاً بر تجربهٔ آمریکا متمرکز است و تعمیم آن به دیگر بسترهای نژادی و قومیتی نیازمند تعدیل است.",
     "مفهوم بیشتر تحلیلی و تفسیری است و شواهد سیستماتیک و مقایسه‌ای محدودی عرضه می‌کند.",
     "خطر اغراق در عاملیت طراحی: ممکن است نقش ساختارهای اقتصادی و سیاسی گسترده‌تر کم‌رنگ شود."
   ],
   "applications": [
     "تحلیل سوگیری نژادی در سامانه‌های تشخیص چهره و جست‌وجوی تصویر در تحریریه.",
     "بررسی اثر تبعیض‌آمیز تبلیغات هدفمند و توصیه‌گر محتوا.",
     "نقد سیاست تعدیل محتوا و تصمیم‌های خودکار در پلتفرم‌ها.",
     "طراحی پژوهش مشارکتی با جوامع آسیب‌دیده در فناوری رسانه."
   ],
   "evolution": "مفهوم در سنت نقد نژاد و فناوری شکل گرفت: «الگوریتم‌های ستم» (Noble, 2018) سوگیری موتور جست‌وجو را نشان داد و بنجامین (۲۰۱۹) آن را به چارچوبی گسترده‌تر برای طراحی تبدیل کرد. پژوهش‌های سنجش سوگیری الگوریتمی در سال‌های بعد، شواهد تجربی تازه‌ای افزودند.",
   "key_concepts": ["کد جیم جدید (New Jim Code)", "نابرابری مهندسی‌شده (engineered inequity)", "تبعیض پیش‌فرض (default discrimination)", "مواجههٔ کدگذاری‌شده (coded exposure)", "طراحی تبعیض‌آمیز (discriminatory design)", "تخیل الغاگرایانه (abolitionist imagination)"],
   "studies": ["Benjamin, R. (2019). Race After Technology. Polity Press.", "Noble, S. U. (2018). Algorithms of Oppression. New York University Press."],
   "detailed_analysis": "۱. بنیان و منطق نظری\nنقد بنجامین بر یک تناقض تمرکز دارد: فناوری مدرن خود را بی‌طرف و حتی رهایی‌بخش معرفی می‌کند، در حالی که الگوهای نابرابری را بازتولید می‌کند. او این تناقض را نه به‌عنوان خطای فنی، بلکه به‌عنوان شکل تازه‌ای از حکومت نژادی می‌خواند که با زبان داده و کارایی مشروعیت می‌یابد.\n\n۲. پیوند با نقد نژاد\nمفهوم «کد جیم جدید» وام‌دار نقد «جیم کرو جدید» است: همان‌گونه که زندان و مجازات جای جداسازی رسمی را گرفت، الگوریتم و طراحی جای قوانین تبعیض‌آمیز را می‌گیرد. تفاوت کلیدی این است که سازوکار تازه، پراکنده و غیرشخصی است و بنابراین مسئولیت را پنهان می‌کند.\n\n۳. پیوند رسانه‌ای\nبرای رسانه، مهم‌ترین پیام این است که بی‌طرفی ادعایی سیستم، تضمین عدالت نیست. جست‌وجو، توصیه، تبلیغ و تعدیل محتوا همه انتخاب می‌کنند و انتخاب، همیشه ارزشی است؛ پرسش درست این است که چه کسی این انتخاب را می‌کند و چه کسی پاسخ‌گوی پیامد آن است."
 },
 "MC-284": {
   "summary": "«عدالت داده» (Data Justice) چارچوبی هنجاری است که می‌پرسد نظام‌های داده‌محور چگونه افراد را «قابل مشاهده، بازنمایی و رفتار» می‌کنند و عدالت در این فرایند چه اقتضایی دارد. لینت تیلور در «What Is Data Justice?» (۲۰۱۷، Big Data & Society) این مفهوم را برای پیوند دادن حقوق دیجیتال با آزادی‌های جهانی و پرهیز از چارچوب محدود به حریم خصوصی شمال جهانی صورت‌بندی کرد (Taylor, 2017).",
   "definition": "عدالت داده یعنی انصاف در شیوه‌ای که افراد از طریق تولید دادهٔ دیجیتال دیده، بازنمایی و با آن‌ها رفتار می‌شود؛ مفهومی که هم توزیع منافع و آسیب داده را و هم قدرت طبقه‌بندی و پیش‌بینی را در بر می‌گیرد (Taylor, 2017).",
   "main_problem": "اگر آسیب داده‌محور فراتر از نقض حریم خصوصی است — از تبعیض الگوریتمی تا حاشیه‌رانی گروه‌ها در نظام‌های طبقه‌بندی — چارچوب هنجاری مناسبی برای سنجش بی‌عدالتی داده و پیوند آن با حقوق و آزادی‌های جهانی چیست؟",
   "mechanism": "چارچوب تیلور سه ستون تحلیلی دارد. (۱) دیده‌شدن و نادیده‌ماندن (visibility): پرسش این است که چه کسی در نظام داده دیده می‌شود، چه کسی نادیده می‌ماند و چه کسی حق دارد نامرئی بماند؛ عدالت داده هم حق بازنمایی گروه‌های حاشیه‌ای را می‌طلبد و هم حق «تاریکی» و نبود نظارت را محترم می‌شمارد. (۲) مشارکت و خودمختاری دیجیتال (digital engagement): امکان انتخاب آگاهانهٔ حضور یا عدم حضور در نظام‌های داده، دسترسی به زیرساخت و توان مقاومت در برابر استخراج داده؛ تمرکز بر این است که آیا افراد در تصمیم دربارهٔ دادهٔ خود عاملیت دارند یا نه. (۳) عدم تبعیض و ضدتبعیض: داده و مدل می‌توانند گروه‌ها را به‌طور غیرمستقیم حاشیه‌ران کنند، حتی وقتی متغیر حساسی در مدل نیست؛ عدالت داده پرسش از اثر افتراقی و سازوکارهای اصلاح را مطرح می‌کند. تیلور (۲۰۱۷) تأکید می‌کند که این سه ستون باید در بستر جهانی و نه صرفاً در چارچوب حقوقی شمال جهانی خوانده شوند، زیرا بخش بزرگی از جمعیت جهان در نظام‌های داده‌ای زندگی می‌کنند که بیرون از حمایت‌های حقوقی شکل گرفته‌اند. در بستر رسانه، عدالت داده پرسش‌هایی دربارهٔ اندازه‌گیری مخاطب، نمایش گروه‌ها در توصیه‌گر، دسترسی پژوهشگران به دادهٔ پلتفرم و حفاظت از دادهٔ روزنامه‌نگاران و منابع خبری مطرح می‌کند.",
   "assumptions": [
     "آسیب داده‌محور فراتر از حریم خصوصی فردی است و ابعاد جمعی و ساختاری دارد.",
     "طبقه‌بندی، پیش‌بینی و توصیه، تصمیم‌هایی ارزشی‌اند و بی‌طرف نیستند.",
     "چارچوب حقوقی جهانی برای عدالت داده لازم است، نه فقط چارچوب‌های ملی."
   ],
   "principles": [
     "سه ستون: دیده‌شدن، مشارکت دیجیتال و عدم تبعیض.",
     "حق دیده‌شدن در کنار حق نامرئی‌ماندن.",
     "عدالت داده باید در بستر جهانی و نه شمال‌محور خوانده شود."
   ],
   "critiques": [
     "مفهوم هنجاری گسترده است و معیار توزیعی روشنی برای سنجش «عادلانه بودن» عرضه نمی‌کند.",
     "مرز آن با حقوق دیجیتال و اخلاق داده مبهم است و خطر هم‌پوشانی مفهومی وجود دارد.",
     "عملیاتی‌سازی تجربی دشوار است و بیشتر به تحلیل کیفی و موردی محدود مانده است."
   ],
   "applications": [
     "تحلیل انصاف در اندازه‌گیری مخاطب و سنجه‌های تعامل.",
     "پژوهش دربارهٔ بازنمایی گروه‌ها در سامانه‌های توصیهٔ خبر و سرگرمی.",
     "سیاست‌گذاری دسترسی پژوهشگران به دادهٔ پلتفرم.",
     "حفاظت از دادهٔ منابع خبری و روزنامه‌نگاران در محیط دیجیتال."
   ],
   "evolution": "مفهوم در واکنش به کاستی چارچوب حریم خصوصی شکل گرفت و با پژوهش‌های عدالت داده در توسعه (Heeks & Renken, 2018) و نقد «استعمار داده» گسترش یافت. در دههٔ ۲۰۲۰، سیاست‌گذاری هوش مصنوعی، عدالت داده را به یکی از مبانی ارزیابی اثر الگوریتمی تبدیل کرد.",
   "key_concepts": ["عدالت داده (data justice)", "دیده‌شدن (visibility)", "مشارکت دیجیتال (digital engagement)", "اثر افتراقی (disparate impact)", "استعمار داده (data colonialism)", "حق نامرئی‌ماندن (right to opacity)"],
   "studies": ["Taylor, L. (2017). What is data justice? Big Data & Society, 4(2), 1-14.", "Heeks, R., & Renken, J. (2018). Data justice for development. Information Development, 34(1), 90-102."],
   "detailed_analysis": "۱. بنیان و منطق نظری\nعدالت داده از این مشاهده آغاز می‌شود که چارچوب حریم خصوصی، مسئله را به رضایت فردی و انتقال داده محدود می‌کند، در حالی که آسیب اصلی در طبقه‌بندی، پیش‌بینی و تصمیم‌گیری جمعی رخ می‌دهد. ازاین‌رو پرسش از «رضایت» به پرسش از «انصاف» منتقل می‌شود.\n\n۲. سه ستون و پیوند آن‌ها\nسه ستون تیلور مکمل‌اند: بدون دیده‌شدن، گروه‌های حاشیه‌ای در داده غایب می‌مانند؛ بدون مشارکت، افراد موضوع تصمیم‌هایی‌اند که در آن‌ها نقشی ندارند؛ و بدون ضدتبعیض، نظام داده می‌تواند نابرابری را بازتولید کند. عدالت داده، پیوند این سه را در یک چارچوب واحد می‌بیند.\n\n۳. پیوند رسانه‌ای\nدر رسانه، داده هم ابزار تولید است و هم ابزار حکمرانی. سنجش مخاطب، تخصیص بودجهٔ تبلیغات و تصمیم دربارهٔ پوشش، همه بر پایهٔ داده انجام می‌شوند؛ عدالت داده می‌پرسد چه کسانی در این داده دیده می‌شوند و چه کسانی به حاشیه می‌روند."
 },
 "MC-287": {
   "summary": "«حاکمیت مشترکات و اصول طراحی» (Commons Governance & Design Principles) نظریه‌ای است که نشان می‌دهد جوامع می‌توانند منابع مشترک را بدون خصوصی‌سازی یا مالکیت دولتی، با نهادهای خودساخته و قواعد جمعی اداره کنند. الینور استروم در «Governing the Commons» (۱۹۹۰، Cambridge University Press) با مطالعهٔ منابع مشترک پایدار، هشت اصل طراحی نهادی را استخراج کرد (Ostrom, 1990).",
   "definition": "مشترکات (commons) منابعی هستند که از آن‌ها نمی‌توان به‌سادگی دیگران را محروم کرد و مصرف یک نفر، سهم دیگری را کم می‌کند؛ حاکمیت مشترکات، مجموعهٔ قواعد و نهادهای جمعی برای بهره‌برداری پایدار از چنین منابعی است (Ostrom, 1990).",
   "main_problem": "اگر هر فرد عقلانی در بهره‌برداری از منبع مشترک بیشتر ببرد، منبع نابود می‌شود (تراژدی مشترکات)، و اگر دولت یا بازار تنها راه‌حل باشند، چرا بسیاری از جوامع توانسته‌اند منابع مشترک را قرن‌ها پایدار نگه دارند و چه اصولی این موفقیت را توضیح می‌دهد؟",
   "mechanism": "استدلال استروم در سه لایه بسط می‌یابد. (۱) رد دوگانهٔ دولت/بازار: استروم (۱۹۹۰) نشان داد «تراژدی مشترکات» هاردین یک نتیجهٔ ممکن است، نه یک قانون حتمی؛ جوامع محلی در سراسر جهان نهادهایی ساخته‌اند که بدون مالکیت خصوصی کامل و بدون کنترل دولتی، بهره‌برداری پایدار را ممکن کرده‌اند. (۲) هشت اصل طراحی: مرزهای روشن منبع و گروه بهره‌بردار؛ تناسب قواعد با شرایط محلی؛ ترتیبات انتخاب جمعی برای کسانی که تحت قواعد‌اند؛ نظارت بر منبع و رفتار؛ مجازات‌های تدریجی؛ سازوکار حل تعارض با هزینهٔ کم؛ به‌رسمیت‌شناختن حق سازمان‌دهی خودگردان؛ و نظام‌های تودرتو برای منابع بزرگ‌تر. این اصول «تشخیصی» هستند، نه دستورالعمل مکانیکی. (۳) نهاد به‌عنوان قواعد در عمل: نهاد تنها سازمان رسمی نیست، بلکه مجموعهٔ قواعد، هنجارها و راهبردهای مشترکی است که کنش را تنظیم می‌کند؛ پایداری به کیفیت این قواعد و به یادگیری و سازگاری مستمر وابسته است. (۴) حاکمیت چندمرکزی: در سطح بزرگ‌تر، تصمیم‌گیری در چند مرکز مستقل اما هم‌پیوند توزیع می‌شود و همین ساختار، خطا و انحصار را کاهش می‌دهد. در بستر رسانه، منطق مشترکات برای تحلیل «مشترکات دانشی» به‌کار می‌رود: ویکی‌پدیا، نرم‌افزار آزاد و آرشیوهای عمومی با قواعد مشارکت، نظارت همتا، مجازات تدریجی و مرزهای روشن عضویت اداره می‌شوند؛ در برابر، محصورسازی داده و محتوای عمومی، مشترکات را به دارایی خصوصی تبدیل می‌کند.",
   "assumptions": [
     "افراد فقط به‌دنبال بیشینه‌سازی نفع کوتاه‌مدت نیستند و می‌توانند به قواعد جمعی پایبند شوند.",
     "پایداری منابع مشترک به کیفیت نهادهای محلی وابسته است، نه فقط به نوع مالکیت.",
     "قواعد مؤثر باید با شرایط بومی سازگار باشند و از پایین شکل بگیرند."
   ],
   "principles": [
     "هشت اصل طراحی: مرز، تناسب، انتخاب جمعی، نظارت، مجازات تدریجی، حل تعارض، حق سازمان‌دهی و تودرتویی.",
     "رد دوگانهٔ دولت/بازار و به‌رسمیت‌شناختن خودگردانی.",
     "نهاد مجموعهٔ قواعد در عمل است، نه فقط سازمان."
   ],
   "critiques": [
     "مطالعات موردی استروم عمدتاً منابع محلی و کوچک‌اند و تعمیم به مشترکات جهانی دیجیتال نیازمند تعدیل است.",
     "اصول طراحی، شرایط لازم را توصیف می‌کنند اما سازوکار گذار به نهاد پایدار را به‌طور کامل توضیح نمی‌دهند.",
     "مرزهای مشترکات دانشی مبهم‌اند و مسئلهٔ سواری مجانی و قدرت کاربران پرقدرت در آن‌ها جدی‌تر است."
   ],
   "applications": [
     "تحلیل حاکمیت ویکی‌پدیا و پروژه‌های دانش مشارکتی.",
     "طراحی قواعد مشارکت در آرشیوهای عمومی و بانک‌های دادهٔ باز.",
     "نقد محصورسازی داده و محتوای عمومی در اقتصاد پلتفرمی.",
     "پژوهش دربارهٔ حاکمیت جامعه‌ای منابع محلی رسانه."
   ],
   "evolution": "استروم (۱۹۹۰) با رد تراژدی مشترکات، سنت پژوهش نهادگرایی را دگرگون کرد؛ او در ۲۰۰۹ جایزهٔ نوبل اقتصاد را دریافت کرد و در ۲۰۱۰ چارچوب حاکمیت چندمرکزی را جمع‌بندی کرد. در دههٔ ۲۰۰۰، پژوهش مشترکات دانشی، چارچوب را به نرم‌افزار آزاد و تولید همتا گسترد.",
   "key_concepts": ["مشترکات (commons)", "اصل طراحی (design principle)", "حاکمیت چندمرکزی (polycentric governance)", "کنش جمعی (collective action)", "قواعد در عمل (rules-in-use)", "تراژدی مشترکات (tragedy of the commons)"],
   "studies": ["Ostrom, E. (1990). Governing the Commons. Cambridge University Press.", "Ostrom, E. (2010). Beyond markets and states. American Economic Review, 100(3), 641-672."],
   "detailed_analysis": "۱. بنیان و منطق نظری\nمدل متعارف، انسان اقتصادی را کوتاه‌بین و منفعت‌جو می‌دانست و نتیجه می‌گرفت که منابع مشترک ناگزیر نابود می‌شوند، مگر با خصوصی‌سازی یا کنترل دولتی. استروم این نتیجه را با شواهد تجربی به چالش کشید و نشان داد که کنشگران می‌توانند با ساختن قواعد، تعهد و نظارت، مسئلهٔ کنش جمعی را حل کنند.\n\n۲. نهاد و یادگیری\nنکتهٔ کلیدی، پویایی است: نهادها ثابت نیستند و در فرایند آزمون و خطا، سازگاری و مذاکره شکل می‌گیرند. همین ویژگی، مدل استروم را از توصیهٔ نسخهٔ واحد جدا می‌کند؛ اصول طراحی، ابزار تشخیص وضعیت‌اند، نه فهرست دستور.\n\n۳. پیوند رسانه‌ای\nرسانهٔ دیجیتال هم مشترکات می‌سازد و هم آن را محصور می‌کند. ویکی‌پدیا نمونهٔ موفق قواعد مشارکت و نظارت همتاست؛ در مقابل، بسته‌بندی داده و محتوا در پلتفرم‌ها، مشترکات را به منبع اختصاصی تبدیل می‌کند. پرسش استرومی این است که چه قواعدی این دو مسیر را تعیین می‌کنند."
 },
 "MC-288": {
   "summary": "«طراحی حساس به ارزش» (Value Sensitive Design) روشی نظام‌مند برای گنجاندن ارزش‌های انسانی در فرایند طراحی فناوری است: ارزش‌ها نه پس از ساخت، بلکه از آغاز در تحلیل، سنجش و طراحی وارد می‌شوند. باتیّا فریدمن، پیتر کان و آلن بورنینگ در «Value Sensitive Design and Information Systems» (۲۰۰۶) این روش را به‌صورت سه‌مرحله‌ای صورت‌بندی کردند (Friedman, Kahn & Borning, 2006).",
   "definition": "طراحی حساس به ارزش، رویکردی نظری و روش‌شناختی است که ارزش‌های انسانی با اهمیت اخلاقی را در تمام مراحل طراحی نظام اطلاعاتی شناسایی، تحلیل و در تصمیم‌های فنی ترجمه می‌کند (Friedman, Kahn & Borning, 2006).",
   "main_problem": "چگونه می‌توان پیش از آنکه آسیب ارزشی در فناوری آشکار شود، ارزش‌های انسانی — مانند حریم خصوصی، عدالت، اعتماد و خودمختاری — را شناسایی و در طراحی فنی وارد کرد، در حالی که ذی‌نفعان گوناگون ارزش‌های متعارض دارند؟",
   "mechanism": "روش سه مرحلهٔ هم‌پیوند دارد که به‌طور چرخه‌ای تکرار می‌شوند. (۱) پژوهش مفهومی: شناسایی ذی‌نفعان مستقیم و غیرمستقیم، ارزش‌های درگیر و تعارض‌های میان آن‌ها؛ پرسش کلیدی این است که چه کسانی از طراحی سود می‌برند و چه کسانی هزینه می‌پردازند، از جمله کسانی که هرگز کاربر نمی‌شوند. (۲) پژوهش تجربی: سنجش اینکه ذی‌نفعان چگونه ارزش‌ها را می‌فهمند، چه اولویتی می‌دهند و طراحی چگونه بر تجربهٔ آن‌ها اثر می‌گذارد؛ ابزارها از مصاحبه و پیمایش تا آزمون کاربردپذیری و مشاهدهٔ میدانی گسترده‌اند. (۳) پژوهش فنی: تحلیل اینکه معماری و سازوکارهای فنی، ارزش‌ها را پشتیبانی یا تضعیف می‌کنند — مثلاً آیا طراحی پایگاه داده، ناشناسی را تضمین می‌کند یا آن را بی‌اثر می‌سازد. فریدمن و همکاران (۲۰۰۶) دوازده ارزش با اهمیت اخلاقی را برمی‌شمارند، از جمله رفاه انسانی، مالکیت، حریم خصوصی، آزادی از سوگیری، کاربردپذیری همگانی، اعتماد، خودمختاری، رضایت آگاهانه، پاسخ‌گویی و آرامش. مرحلهٔ چهارم غیررسمی، «طراحی» است: انتخاب میان گزینه‌ها با آگاهی از تعارض ارزش‌ها. در بستر رسانه، این روش در طراحی شخصی‌سازی خبر (تعادل بین ربط و تنوع)، سامانهٔ تعدیل محتوا (تعادل بین ایمنی و آزادی بیان)، سنجش مخاطب (تعادل بین دقت و حریم خصوصی) و دسترسی‌پذیری کاربرد دارد.",
   "assumptions": [
     "فناوری همیشه ارزش‌بار است و بی‌طرف نیست.",
     "ارزش‌های انسانی را می‌توان پیش از پیاده‌سازی، شناسایی و تحلیل کرد.",
     "ذی‌نفعان غیرمستقیم نیز باید در تحلیل ارزش وارد شوند."
   ],
   "principles": [
     "روش سه‌مرحله‌ای: مفهومی، تجربی و فنی.",
     "شناسایی ذی‌نفعان مستقیم و غیرمستقیم و تعارض ارزش‌ها.",
     "ترجمهٔ ارزش‌ها به تصمیم فنی، نه فقط بیانیهٔ اخلاقی."
   ],
   "critiques": [
     "تعدد ارزش‌ها و تعارض میان آن‌ها، تصمیم نهایی را به داوری ارزشی سپرده می‌کند که معیار روشنی ندارد.",
     "در فرایندهای چابک و سریع تولید، اجرای کامل سه مرحله پرهزینه و دشوار است.",
     "خطر «شست‌وشوی اخلاقی»: اعلام حساسیت به ارزش‌ها بدون تغییر واقعی در طراحی و توزیع قدرت."
   ],
   "applications": [
     "طراحی شخصی‌سازی خبر با تعادل ربط و تنوع.",
     "طراحی سامانهٔ تعدیل محتوا با تعادل ایمنی و آزادی بیان.",
     "تحلیل حریم خصوصی در سنجش مخاطب و تحلیل داده.",
     "ارزیابی دسترسی‌پذیری و کاربردپذیری همگانی محصولات رسانه‌ای."
   ],
   "evolution": "ریشهٔ روش در پژوهش‌های دههٔ ۱۹۹۰ فریدمن دربارهٔ ارزش‌ها در طراحی رایانه است و کتاب ۲۰۰۴ آن را گرد آورد. صورت‌بندی سه‌مرحله‌ای ۲۰۰۶ به روش مرجع تبدیل شد و پژوهش‌های بعدی، ابزارهایی مانند «سدها و جریان‌های ارزش» و کاربرد در هوش مصنوعی و حکمرانی داده افزودند.",
   "key_concepts": ["طراحی حساس به ارزش (value sensitive design)", "ذی‌نفع غیرمستقیم (indirect stakeholder)", "تعارض ارزش (value tension)", "پژوهش مفهومی/تجربی/فنی (conceptual/empirical/technical)", "ارزش‌های با اهمیت اخلاقی (values of ethical import)", "شست‌وشوی اخلاقی (ethics washing)"],
   "studies": ["Friedman, B., Kahn, P. H., Jr., & Borning, A. (2006). Value sensitive design and information systems. In Zhang & Galletta (Eds.), HCI and MIS: Foundations (pp. 348-372). M.E. Sharpe.", "Friedman, B. (Ed.). (2004). Human Values and the Design of Computer Technology. CSLI Publications."],
   "detailed_analysis": "۱. بنیان و منطق نظری\nطراحی حساس به ارزش در برابر دو نگرش شکل گرفت: نگرش «بی‌طرفی فناوری» که طراحی را صرفاً مسئلهٔ کارایی می‌داند، و نگرش «جبر اخلاقی پسینی» که اصلاح را به پس از بروز آسیب موکول می‌کند. فریدمن و همکاران (۲۰۰۶) استدلال می‌کنند که ارزش‌ها در جزئیات فنی نهفته‌اند و بنابراین باید در همان جزئیات دیده شوند.\n\n۲. روش به‌عنوان چرخه\nسه مرحله، ترتیبی خطی نیستند؛ یافتهٔ مرحلهٔ تجربی می‌تواند تحلیل مفهومی را بازنگری کند و بررسی فنی می‌تواند پرسش تجربی تازه بسازد. همین چرخه، روش را با طراحی تکرارشونده سازگار می‌کند.\n\n۳. پیوند رسانه‌ای و نقد\nبرای رسانه، سنجه‌های تعامل نمونهٔ روشنی از تعارض ارزش‌اند: بهینه‌سازی زمان تماشا ممکن است حریم خصوصی، خودمختاری و تنوع را تضعیف کند. نقد اصلی این است که روش، ارزش‌ها را شناسایی می‌کند اما دربارهٔ اولویت آن‌ها تصمیم نمی‌گیرد؛ تصمیم نهایی به فرایند سیاسی و اخلاقی بیرون از روش وابسته است."
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
    return min(100, sum(detail.values())), detail, words

def main():
    c = pymysql.connect(host="127.0.0.1", user="root", password="433700", database=DB, charset="utf8mb4", autocommit=False)
    cur = c.cursor()
    codes = ["MC-283", "MC-284", "MC-287", "MC-288"]
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
        score, detail, words = rubric(p, n_verified, n_sources, n_relations)
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
                    (eid, ver, json.dumps({"quality_score": score, "words": words, "sources": n_sources, "verified": n_verified}, ensure_ascii=False),
                     "documented sourcing + rubric score", STAMP, NOW))
        cur.execute("INSERT INTO kb_audit_log (entity_code, action, detail, source) VALUES (%s,%s,%s,%s)",
                    (code, "DOC_ENRICH", json.dumps({"quality_score": score, "words": words, "sources": n_sources, "verified": n_verified, "breakdown": detail}, ensure_ascii=False), STAMP))
        print(f"{code}: score={score} words={words} sources={n_sources} verified={n_verified} relations={n_relations} | {detail}")
    c.commit()
    c.close()
    print("BATCH58 THEORY DONE")

if __name__ == "__main__":
    main()
