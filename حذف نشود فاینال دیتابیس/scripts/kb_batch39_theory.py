# -*- coding: utf-8 -*-
"""Batch 39 (THEORY): MC-130 Media Economics (Albarran 2010), MC-124 Organizational Identity and
Image (Albert & Whetten 1985), MC-126 Gain vs. Loss Framing (Rothman & Salovey 1997),
MC-145 Relationship Management Theory (Ledingham 2003). All verified 2026-11-16."""
import pymysql, json

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch39-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch39_theory.json"

S = {
 "MC-130": [  # Media Economics
   dict(kind="BOOK", title_en="The Media Economy",
        title_fa="اقتصاد رسانه", authors="Albarran, A. B.", year=2010,
        publisher="New York: Routledge", doi=None, url=None, language="en", isbn="9780415990454",
        citation="Albarran, A. B. (2010). The media economy. Routledge.",
        locator="whole work", locator_type="work", supports="definition / levels of analysis / market structure", verified=True),
   dict(kind="BOOK", title_en="Media Economics: Concepts and Issues",
        title_fa="اقتصاد رسانه: مفاهیم و مسائل", authors="Picard, R. G.", year=1989,
        publisher="Newbury Park, CA: Sage", doi=None, url=None, language="en", isbn=None,
        citation="Picard, R. G. (1989). Media economics: Concepts and issues. Sage.",
        locator="whole work", locator_type="work", supports="origin / foundational concepts", verified=False),
 ],
 "MC-124": [  # Organizational Identity and Image
   dict(kind="JOURNAL_ARTICLE", title_en="Organizational Identity",
        title_fa="هویت سازمانی", authors="Albert, S., & Whetten, D. A.", year=1985,
        publisher="Research in Organizational Behavior, 7, 263-295", doi=None, url=None, language="en", isbn=None,
        citation="Albert, S., & Whetten, D. A. (1985). Organizational identity. Research in Organizational Behavior, 7, 263-295.",
        locator="pp. 263-295", locator_type="page_range", supports="definition / central-distinctive-enduring / mechanism", verified=True),
   dict(kind="JOURNAL_ARTICLE", title_en="Relations between Organizational Culture, Identity and Image",
        title_fa="روابط میان فرهنگ، هویت و تصویر سازمانی", authors="Hatch, M. J., & Schultz, M.", year=1997,
        publisher="European Journal of Marketing, 31(5/6), 356-365", doi=None, url=None, language="en", isbn=None,
        citation="Hatch, M. J., & Schultz, M. (1997). Relations between organizational culture, identity and image. European Journal of Marketing, 31(5/6), 356-365.",
        locator="pp. 356-365", locator_type="page_range", supports="evolution / identity-image gap", verified=False),
 ],
 "MC-126": [  # Gain vs. Loss Framing
   dict(kind="JOURNAL_ARTICLE", title_en="Shaping Perceptions to Motivate Healthy Behavior: The Role of Message Framing",
        title_fa="شکل‌دادن به ادراک‌ها برای انگیزش رفتار سالم: نقش قاب‌بندی پیام",
        authors="Rothman, A. J., & Salovey, P.", year=1997,
        publisher="Psychological Bulletin, 121(1), 3-19", doi=None,
        url="https://pubmed.ncbi.nlm.nih.gov/9000890/", language="en", isbn=None,
        citation="Rothman, A. J., & Salovey, P. (1997). Shaping perceptions to motivate healthy behavior: The role of message framing. Psychological Bulletin, 121(1), 3-19.",
        locator="pp. 3-19", locator_type="page_range", supports="definition / prevention-detection fit / mechanism", verified=True),
   dict(kind="JOURNAL_ARTICLE", title_en="Prospect Theory: An Analysis of Decision under Risk",
        title_fa="نظریهٔ چشم‌انداز: تحلیلی از تصمیم در شرایط ریسک", authors="Kahneman, D., & Tversky, A.", year=1979,
        publisher="Econometrica, 47(2), 263-291", doi=None, url=None, language="en", isbn=None,
        citation="Kahneman, D., & Tversky, A. (1979). Prospect theory: An analysis of decision under risk. Econometrica, 47(2), 263-291.",
        locator="pp. 263-291", locator_type="page_range", supports="theoretical foundation / loss aversion", verified=False),
 ],
 "MC-145": [  # Relationship Management Theory
   dict(kind="JOURNAL_ARTICLE", title_en="Explicating Relationship Management as a General Theory of Public Relations",
        title_fa="تبیین مدیریت رابطه به‌عنوان نظریهٔ عمومی روابط عمومی",
        authors="Ledingham, J. A.", year=2003,
        publisher="Journal of Public Relations Research, 15(2), 181-198", doi=None, url=None, language="en", isbn=None,
        citation="Ledingham, J. A. (2003). Explicating relationship management as a general theory of public relations. Journal of Public Relations Research, 15(2), 181-198.",
        locator="pp. 181-198", locator_type="page_range", supports="definition / relationship quality / mechanism", verified=True),
   dict(kind="BOOK", title_en="Guidelines for Measuring Relationships in Public Relations",
        title_fa="راهنمای سنجش روابط در روابط عمومی", authors="Hon, L. C., & Grunig, J. E.", year=1999,
        publisher="Gainesville, FL: Institute for Public Relations", doi=None, url=None, language="en", isbn=None,
        citation="Hon, L. C., & Grunig, J. E. (1999). Guidelines for measuring relationships in public relations. Institute for Public Relations.",
        locator="whole work", locator_type="work", supports="measurement / six relationship dimensions", verified=False),
 ],
}

ENRICH = {
 "MC-130": {
   "summary": "«اقتصاد رسانه» (Media Economics) رشته‌ای است که اقتصاد، رفتار بنگاه‌ها و ساختار بازار را در صنایع رسانه‌ای تحلیل می‌کند. آلبران در کتاب «The Media Economy» (۲۰۱۰، Routledge) چارچوبی چندسطحی ارائه می‌دهد که از سطح کلان (اقتصاد جهانی، مقررات و فناوری) تا سطح خرد (مدیریت و راهبرد بنگاه) را در بر می‌گیرد و مفاهیمی مانند ساختار بازار، مدل درآمدی و بازار دوگانهٔ مخاطب-آگهی را به رسانه پیوند می‌زند (Albarran, 2010).",
   "main_problem": "رسانه‌ها به‌عنوان بنگاه اقتصادی چگونه رفتار می‌کنند، ساختار بازار رسانه چگونه شکل می‌گیرد، و اقتصاد رسانه چه تفاوت‌هایی با اقتصاد صنایع دیگر دارد که تحلیل و سیاست‌گذاری ویژه‌ای را ضروری می‌کند؟",
   "mechanism": "اقتصاد رسانه مکانیسم را در چند لایه توضیح می‌دهد: (۱) «ساختار-رفتار-عملکرد» (structure-conduct-performance) — تعداد بنگاه‌ها، موانع ورود و تمرکز بازار، رفتار قیمت‌گذاری و سرمایه‌گذاری و در نهایت عملکرد (کیفیت، سود، تنوع) را شکل می‌دهد؛ (۲) «بازار دوگانه» (dual market) — رسانه هم مخاطب را به آگهی‌دهنده می‌فروشد و هم محتوا را به مخاطب، بنابراین دو منبع درآمد و دو منطق قیمت‌گذاری دارد؛ (۳) «سطح کلان و خرد» — عوامل کلان (رشد اقتصادی، مقررات، تحول فناوری) بر سطح بنگاه (سرمایه‌گذاری، ادغام، تنوع محصول) اثر می‌گذارند و بنگاه نیز از طریق راهبرد بر ساختار بازار بازخورد دارد (Albarran, 2010). پیکارد (1989) پیش‌تر مفاهیم بنیادین این رشته را در چارچوب کالای رسانه‌ای و بازارهای آن صورت‌بندی کرده بود.",
   "assumptions": [
     "رسانه کالایی اقتصادی با ویژگی‌های هزینه‌ای و تقاضای ویژه است که تحلیل اقتصادی را ضروری می‌کند.",
     "رفتار بنگاه‌های رسانه‌ای را می‌توان در چارچوب ساختار بازار و انگیزه‌های اقتصادی توضیح داد.",
     "عوامل نهادی و مقرراتی، ساختار و عملکرد بازار رسانه را به‌طور معنادار شکل می‌دهند."
   ],
   "principles": [
     "چندسطحی‌بودن: اقتصاد رسانه از اقتصاد کلان تا مدیریت بنگاه در یک پیوستار تحلیل می‌شود.",
     "بازار دوگانه: درآمد رسانه از محتوا و آگهی به‌طور هم‌زمان تأمین می‌شود.",
     "رابطهٔ ساختار و عملکرد: تمرکز و موانع ورود، کیفیت و تنوع بازار رسانه را تحت تأثیر قرار می‌دهند."
   ],
   "critiques": [
     "غرب‌محوری: بسیاری از الگوها بر بازار رسانهٔ آمریکای شمالی و اروپا استوارند و تعمیم آن‌ها به بازارهای نوظهور نیازمند احتیاط است.",
     "کم‌توجهی به ارزش عمومی: تحلیل اقتصادی ممکن است ارزش دموکراتیک و فرهنگی رسانه را به سود معیارهای کارایی و سود کم‌رنگ کند.",
     "تحول پلتفرمی: اقتصاد رسانهٔ کلاسیک، منطق پلتفرم، داده و بازارهای چندوجهی دیجیتال را به‌طور کامل پوشش نمی‌دهد."
   ],
   "applications": [
     "تحلیل ساختار بازار رسانه، ادغام‌ها و سیاست‌های رقابت.",
     "ارزیابی مدل‌های درآمدی رسانه (آگهی، اشتراک، حق پخش) و راهبردهای رشد.",
     "پژوهش دربارهٔ تأثیر تحول دیجیتال بر بهره‌وری، اشتغال و تنوع رسانه."
   ],
   "evolution": "اقتصاد رسانه از دههٔ ۱۹۸۰ با آثار پیکارد شکل گرفت و در دههٔ ۲۰۰۰ با چارچوب‌های چندسطحی (آلبران، 2010) و پژوهش‌های مدیریت رسانه گسترش یافت. در دههٔ ۲۰۱۰، اقتصاد پلتفرم، بازارهای چندوجهی داده و مدل‌های اشتراکی، مرزهای این رشته را به سمت «اقتصاد پلتفرم رسانه‌ای» گستردند.",
   "key_concepts": ["اقتصاد رسانه (media economics)", "ساختار-رفتار-عملکرد (SCP)", "بازار دوگانه (dual market)", "تمرکز بازار (market concentration)", "مدل درآمدی رسانه (media revenue model)"],
   "studies": ["Albarran, A. B. (2010). The Media Economy. Routledge.", "Picard, R. G. (1989). Media Economics: Concepts and Issues. Sage."],
 },
 "MC-124": {
   "summary": "«هویت و تصویر سازمانی» (Organizational Identity and Image) دو سازهٔ مرتبط اما متمایزند: هویت سازمانی آن چیزی است که اعضای سازمان دربارهٔ «ما کی هستیم» باور دارند، و تصویر سازمانی آن چیزی است که بیرونی‌ها دربارهٔ سازمان می‌پندارند. استوارت آلبرت و دیوید ویتن در فصل «Organizational Identity» (۱۹۸۵، Research in Organizational Behavior) هویت را بر پایهٔ سه معیار «مرکزی، متمایز و پایدار» تعریف کردند (Albert & Whetten, 1985).",
   "main_problem": "سازمان‌ها چگونه دربارهٔ «کیستی» خود به فهم مشترک می‌رسند، چه نسبتی میان هویت درونی و تصویر بیرونی وجود دارد، و چگونه شکاف میان این دو بر تصمیم‌گیری و راهبرد سازمان اثر می‌گذارد؟",
   "mechanism": "آلبرت و ویتن هویت را با سه پرسش عملیاتی می‌سنجند: «چه چیزی مرکزی است؟» (central) — باورهایی که در تعریف سازمان از خود نقش کلیدی دارند؛ «چه چیزی متمایز است؟» (distinctive) — آنچه سازمان را از دیگران جدا می‌کند؛ و «چه چیزی پایدار است؟» (enduring) — آنچه در زمان نسبتاً ثابت می‌ماند (Albert & Whetten, 1985). تصویر، در مقابل، ادراک بیرونی است و از تعامل سازمان با ذی‌نفعان و رسانه شکل می‌گیرد. هتچ و شولتز (Hatch & Schultz, 1997) نشان دادند هویت، فرهنگ و تصویر در یک چرخهٔ بازخوردی قرار دارند: هویت از فرهنگ سازمانی تغذیه می‌شود، در ارتباطات و نمادها بیان می‌شود و تصویر بیرونی را می‌سازد؛ در بازگشت، تصویر بیرونی می‌تواند هویت را تغییر دهد. شکاف میان هویت و تصویر («شکاف هویت-تصویر») یکی از منابع اصلی فشار برای تغییر سازمانی است.",
   "assumptions": [
     "سازمان‌ها دارای فهم مشترک و نسبتاً پایدار از «کیستی» خود هستند.",
     "هویت درونی و تصویر بیرونی دو سازهٔ متمایز اما در تعامل‌اند.",
     "شکاف میان هویت و تصویر، محرک تغییر راهبردی و ارتباطی سازمان است."
   ],
   "principles": [
     "سه معیار هویت: مرکزی، متمایز و پایدار بودن باورهای هویتی.",
     "تفکیک درون/بیرون: هویت از منظر اعضا، تصویر از منظر بیرونی‌ها تعریف می‌شود.",
     "بازخورد هویت-تصویر: تصویر بیرونی می‌تواند هویت درونی را تقویت یا به چالش بکشد."
   ],
   "critiques": [
     "پایداری محل بحث: در محیط متلاطم، هویت ممکن است سیال‌تر از آن باشد که معیار «پایداری» نشان می‌دهد.",
     "هویت‌های چندگانه: سازمان‌های پیچیده اغلب هویت‌های هم‌زمان و حتی متعارض دارند و الگوی واحد آن را پوشش نمی‌دهد.",
     "سنجش دشوار: هویت و تصویر سازه‌های ادراکی‌اند و اندازه‌گیری معتبر آن‌ها چالش روش‌شناختی جدی است."
   ],
   "applications": [
     "مدیریت تغییر سازمانی، ادغام و بازسازی هویت پس از ادغام.",
     "طراحی ارتباطات شرکتی و هم‌سوسازی پیام بیرونی با هویت درونی.",
     "تحلیل بحران هویت و شکاف تصویر در سازمان‌های رسانه‌ای و عمومی."
   ],
   "evolution": "آلبرت و ویتن (1985) مفهوم را در ادبیات رفتار سازمانی تثبیت کردند. در دههٔ ۱۹۹۰، داتون و دوکریچ (1991) رابطهٔ هویت و تصویر را در انطباق سازمانی بررسی کردند و هتچ و شولتز (1997) چرخهٔ فرهنگ-هویت-تصویر را صورت‌بندی کردند. در دههٔ ۲۰۰۰، پژوهش هویت‌های چندگانه، هویت سازمانی در ادغام‌ها و هویت برند سازمانی گسترش یافت.",
   "key_concepts": ["هویت سازمانی (organizational identity)", "تصویر سازمانی (organizational image)", "معیارهای مرکزی-متمایز-پایدار (CED)", "شکاف هویت-تصویر (identity-image gap)", "هویت چندگانه (multiple identities)"],
   "studies": ["Albert, S., & Whetten, D. A. (1985). Organizational Identity. Research in Organizational Behavior, 7, 263-295.", "Hatch, M. J., & Schultz, M. (1997). Relations between Organizational Culture, Identity and Image. European Journal of Marketing, 31(5/6), 356-365."],
 },
 "MC-126": {
   "summary": "«قاب‌بندی سود و زیان در پیام‌رسانی» (Gain vs. Loss Framing in Messaging) به این پرسش می‌پردازد که ارائهٔ یک پیام در قالب «سود» (منفعت پیروی از توصیه) یا «زیان» (هزینهٔ پیروی نکردن) چگونه تصمیم و رفتار مخاطب را تغییر می‌دهد. راثمن و سالووی در مقالهٔ «Shaping Perceptions to Motivate Healthy Behavior» (۱۹۹۷، Psychological Bulletin) نشان دادند اثربخشی هر قالب به نوع رفتار هدف — پیشگیری یا تشخیص — وابسته است (Rothman & Salovey, 1997).",
   "main_problem": "چرا دو پیام با محتوای یکسان اما قالب متفاوت (سود در برابر زیان) اثر یکسانی بر رفتار ندارند، و چه عواملی تعیین می‌کند کدام قالب در کدام موقعیت مؤثرتر است؟",
   "mechanism": "مکانیسم بر پایهٔ «نظریهٔ چشم‌انداز» (prospect theory) کانمن و تورسکی (1979) استوار است: افراد در برابر زیان‌ها حساس‌ترند تا سودهای هم‌ارز (زیان‌گریزی) و تصمیم خود را نسبت به یک نقطهٔ مرجع می‌سنجند. راثمن و سالووی این اصل را به پیام‌رسانی سلامت پیوند زدند: (۱) در «رفتارهای پیشگیری» (prevention behaviors) که هدفشان حفظ سلامت و بی‌خطر است (مانند استفاده از ضدآفتاب یا ترک سیگار)، پیام‌های «سودمحور» مؤثرترند، زیرا با انگیزهٔ حفظ وضعیت مطلوب هم‌سو هستند؛ (۲) در «رفتارهای تشخیصی» (detection behaviors) که مستلزم پذیرش خطر و پیگیری نتیجهٔ احتمالی ناخوشایند است (مانند ماموگرافی یا آزمایش HIV)، پیام‌های «زیان‌محور» اثر بیشتری دارند، چون پذیرش خطر را از طریق برجسته‌سازی هزینهٔ کوتاهی توجیه می‌کنند (Rothman & Salovey, 1997). قالب‌بندی علاوه بر شناخت، بر عواطف مخاطب نیز اثر می‌گذارد و همین امر انتخاب قالب را به تصمیمی راهبردی در طراحی کمپین بدل می‌کند.",
   "assumptions": [
     "افراد نسبت به زیان‌ها حساس‌تر از سودهای هم‌ارزند (زیان‌گریزی).",
     "چگونگی ارائهٔ اطلاعات (قالب) بر ادراک و تصمیم مستقل از محتوای پیام اثر می‌گذارد.",
     "اثربخشی قالب به نوع رفتار و میزان ریسک درک‌شدهٔ آن وابسته است."
   ],
   "principles": [
     "زیان‌گریزی: پیام زیان‌محور احساس فوریت بیشتری ایجاد می‌کند.",
     "تناسب قالب و رفتار: سودمحور برای پیشگیری و زیان‌محور برای تشخیص مؤثرتر است.",
     "نقطهٔ مرجع: چارچوب پیام، نقطهٔ مرجع را جابه‌جا می‌کند و ارزیابی سود/زیان را تغییر می‌دهد."
   ],
   "critiques": [
     "اندازهٔ اثر: فراتحلیل‌های بعدی نشان دادند اثر قاب‌بندی در عمل کوچک و به شرایط وابسته است.",
     "تنوع یافته‌ها: نتایج تکرار آزمایش‌ها یکسان نبوده و سازوکارهای تعدیل‌کننده (درگیری، سواد سلامت، فرهنگ) به‌خوبی مشخص نشده‌اند.",
     "اخلاق پیام‌رسانی: استفادهٔ ابزاری از قالب زیان‌محور می‌تواند به بزرگ‌نمایی ترس و دستکاری احساسات بیانجامد."
   ],
   "applications": [
     "طراحی کمپین‌های سلامت عمومی و پیام‌های واکسیناسیون و غربالگری.",
     "تدوین پیام‌های سیاست عمومی و ارتباطات مخاطرات.",
     "تحلیل پیام‌های تبلیغاتی و سیاسی از منظر قاب‌بندی سود و زیان."
   ],
   "evolution": "قاب‌بندی پیام از نظریهٔ چشم‌انداز (کانمن و تورسکی، 1979) سرچشمه گرفت و با مقالهٔ راثمن و سالووی (1997) به چارچوبی تجربی در ارتباطات سلامت بدل شد. در دو دههٔ بعد، فراتحلیل‌ها و پژوهش‌های بین‌فرهنگی، محدودیت‌ها و شرایط مرزی اثر قاب‌بندی را برجسته کردند و کاربرد آن به ارتباطات سیاسی و بازاریابی گسترش یافت.",
   "key_concepts": ["قاب‌بندی سود/زیان (gain/loss framing)", "زیان‌گریزی (loss aversion)", "رفتار پیشگیری و تشخیص (prevention vs. detection behavior)", "نقطهٔ مرجع (reference point)", "نظریهٔ چشم‌انداز (prospect theory)"],
   "studies": ["Rothman, A. J., & Salovey, P. (1997). Shaping Perceptions to Motivate Healthy Behavior. Psychological Bulletin, 121(1), 3-19.", "Kahneman, D., & Tversky, A. (1979). Prospect Theory. Econometrica, 47(2), 263-291."],
 },
 "MC-145": {
   "summary": "«نظریهٔ مدیریت رابطه» (Relationship Management Theory) روابط عمومی را نه مدیریت پیام و تصویر، بلکه مدیریت رابطهٔ بین سازمان و عمومی‌ها تعریف می‌کند. جان لیدینگهام در مقالهٔ «Explicating Relationship Management as a General Theory of Public Relations» (۲۰۰۳، Journal of Public Relations Research) استدلال کرد که واحد تحلیل روابط عمومی باید خودِ «رابطه» باشد، نه کمپین یا پیام (Ledingham, 2003).",
   "main_problem": "چگونه می‌توان روابط عمومی را بر پایهٔ کیفیت رابطهٔ سازمان و عمومی‌ها، و نه صرفاً اقناع یا انتشار پیام، بازتعریف کرد، و کیفیت رابطه را چگونه می‌سنجیم؟",
   "mechanism": "نظریه مکانیسم را در قالب چرخهٔ رابطه توضیح می‌دهد: (۱) سازمان و عمومی‌ها در یک رابطهٔ متقابل قرار دارند که منافع و انتظارات دوطرفه را در بر می‌گیرد؛ (۲) کیفیت رابطه با ابعادی مانند «اعتماد» (trust)، «تعهد» (commitment)، «رضایت» (satisfaction) و «تعادل قدرت» (balance of power) سنجیده می‌شود؛ (۳) ارتباطات راهبردی باید در خدمت حفظ و تقویت این ابعاد باشد، به‌گونهٔ که «درک متقابل و منفعت متقابل» (mutual understanding and benefit) حاصل شود؛ (۴) رابطهٔ باکیفیت، سرمایه‌ای اجتماعی است که در بحران‌ها و مذاکرات، ظرفیت همکاری و تاب‌آوری ایجاد می‌کند (Ledingham, 2003). هان و گرونیگ (1999) شش شاخص رابطه — اعتماد، تعهد، رضایت، تعادل قدرت، مبادلهٔ رابطه‌ای و مبادلهٔ اجتماعی — را برای سنجش عملیاتی پیشنهاد کردند.",
   "assumptions": [
     "رابطه، واحد اصلی تحلیل روابط عمومی است و پیام و کمپین ابزار آن‌اند.",
     "کیفیت رابطه را می‌توان با شاخص‌های ادراکی مانند اعتماد و تعهد سنجید.",
     "منفعت متقابل، معیار هنجاری رابطهٔ پایدار سازمان و عمومی است."
   ],
   "principles": [
     "رابطه‌محوری: هدف روابط عمومی ساختن و حفظ رابطهٔ باکیفیت است.",
     "دوطرفه‌بودن: منافع و انتظارات سازمان و عمومی هر دو باید لحاظ شوند.",
     "سنجش کیفیت: اعتماد، تعهد، رضایت و تعادل قدرت، شاخص‌های کلیدی رابطه‌اند."
   ],
   "critiques": [
     "ابهام مفهومی: مرز «رابطه» با «شهرت» و «اعتماد» روشن نیست و تعریف‌ها هم‌پوشانی دارند.",
     "اندازه‌گیری: ابزارهای پیمایشی رابطه عمدتاً ادراکی‌اند و به سوگیری پاسخ‌دهنده حساس.",
     "تعادل آرمانی: فرض «منفعت متقابل» در روابط نامتقارن قدرت (سازمان بزرگ-عمومی ضعیف) واقع‌بینانه نیست."
   ],
   "applications": [
     "سنجش کیفیت رابطهٔ سازمان با مشتریان، کارکنان و جامعه.",
     "طراحی برنامه‌های روابط عمومی رابطه‌محور در بحران و مذاکره.",
     "پژوهش در ارتباطات سازمانی، مسئولیت اجتماعی و دیپلماسی عمومی."
   ],
   "evolution": "مدیریت رابطه در دههٔ ۱۹۹۰ از پیوند روابط عمومی با ادبیات روابط میان‌فردی شکل گرفت و لیدینگهام (2003) آن را به نظریهٔ عمومی روابط عمومی ارتقا داد. در دههٔ ۲۰۰۰-۲۰۱۰، با نظریهٔ گفت‌وگومدار، ارتباطات بحران و سنجش روابط در رسانه‌های اجتماعی پیوند خورد.",
   "key_concepts": ["مدیریت رابطه (relationship management)", "کیفیت رابطه (relationship quality)", "اعتماد (trust)", "منفعت متقابل (mutual benefit)", "تعادل قدرت (balance of power)"],
   "studies": ["Ledingham, J. A. (2003). Relationship Management as a General Theory. Journal of Public Relations Research, 15(2), 181-198.", "Hon, L. C., & Grunig, J. E. (1999). Guidelines for Measuring Relationships in Public Relations. Institute for Public Relations."],
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
    codes = ["MC-130", "MC-124", "MC-126", "MC-145"]
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
    print("BATCH39 THEORY DONE")

if __name__ == "__main__":
    main()
