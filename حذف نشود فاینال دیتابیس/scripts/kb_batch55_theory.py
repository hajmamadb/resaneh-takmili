# -*- coding: utf-8 -*-
"""Batch 55 (THEORY): MC-242 Media Richness Theory (Daft & Lengel 1986),
MC-247 Uncertainty Reduction Theory (Berger & Calabrese 1975),
MC-260 Dunbar's Number (Dunbar 1992), MC-261 The Sharing Economy (Botsman & Rogers 2010).
Anchors verified 2026-11-16."""
import pymysql, json

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch55-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch55_theory.json"

S = {
 "MC-242": [
   dict(kind="JOURNAL_ARTICLE", title_en="Organizational Information Requirements, Media Richness and Structural Design",
        title_fa="نیازهای اطلاعاتی سازمان، غنای رسانه و طراحی ساختاری",
        authors="Daft, R. L., & Lengel, R. H.", year=1986,
        publisher="Management Science, 32(5), 554-571", doi="10.1287/mnsc.32.5.554",
        url="https://pubsonline.informs.org/doi/10.1287/mnsc.32.5.554",
        language="en", isbn=None,
        citation="Daft, R. L., & Lengel, R. H. (1986). Organizational information requirements, media richness and structural design. Management Science, 32(5), 554-571.",
        locator="pp. 554-571", locator_type="page_range", supports="definition / four richness criteria / structural design", verified=True),
   dict(kind="JOURNAL_ARTICLE", title_en="Message Equivocality, Media Selection, and Manager Performance: Implications for Information Systems",
        title_fa="ابهام پیام، انتخاب رسانه و عملکرد مدیران: دلالت‌ها برای نظام‌های اطلاعاتی",
        authors="Daft, R. L., Lengel, R. H., & Trevino, L. K.", year=1987,
        publisher="MIS Quarterly, 11(3), 355-366", doi=None, url=None, language="en", isbn=None,
        citation="Daft, R. L., Lengel, R. H., & Trevino, L. K. (1987). Message equivocality, media selection, and manager performance: Implications for information systems. MIS Quarterly, 11(3), 355-366.",
        locator="pp. 355-366", locator_type="page_range", supports="evolution / managerial performance test", verified=False),
 ],
 "MC-247": [
   dict(kind="JOURNAL_ARTICLE", title_en="Some Explorations in Initial Interaction and Beyond: Toward a Developmental Theory of Interpersonal Communication",
        title_fa="کاوش‌هایی در تعامل اولیه و فراتر از آن: به‌سوی نظریه‌ای تحولی در ارتباطات میان‌فردی",
        authors="Berger, C. R., & Calabrese, R. J.", year=1975,
        publisher="Human Communication Research, 1(2), 99-112", doi="10.1111/j.1468-2958.1975.tb00258.x",
        url="https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1468-2958.1975.tb00258.x",
        language="en", isbn=None,
        citation="Berger, C. R., & Calabrese, R. J. (1975). Some explorations in initial interaction and beyond: Toward a developmental theory of interpersonal communication. Human Communication Research, 1(2), 99-112.",
        locator="pp. 99-112", locator_type="page_range", supports="definition / seven axioms / twenty-one theorems", verified=True),
   dict(kind="BOOK_CHAPTER", title_en="Uncertainty and Communication",
        title_fa="عدم قطعیت و ارتباط",
        authors="Berger, C. R., & Gudykunst, W. B.", year=1991,
        publisher="In B. Dervin & M. J. Voigt (Eds.), Progress in Communication Sciences (Vol. 10, pp. 23-66). Norwood, NJ: Ablex",
        doi=None, url=None, language="en", isbn=None,
        citation="Berger, C. R., & Gudykunst, W. B. (1991). Uncertainty and communication. In B. Dervin & M. J. Voigt (Eds.), Progress in Communication Sciences (Vol. 10, pp. 23-66). Ablex.",
        locator="pp. 23-66", locator_type="page_range", supports="evolution / uncertainty and communication synthesis", verified=False),
 ],
 "MC-260": [
   dict(kind="JOURNAL_ARTICLE", title_en="Neocortex Size as a Constraint on Group Size in Primates",
        title_fa="اندازهٔ نئوکورتکس به‌عنوان محدودیت اندازهٔ گروه در نخستی‌ها",
        authors="Dunbar, R. I. M.", year=1992,
        publisher="Journal of Human Evolution, 22(6), 469-493", doi="10.1016/0047-2484(92)90081-J",
        url="https://www.sciencedirect.com/science/article/pii/004724849290081J",
        language="en", isbn=None,
        citation="Dunbar, R. I. M. (1992). Neocortex size as a constraint on group size in primates. Journal of Human Evolution, 22(6), 469-493.",
        locator="pp. 469-493", locator_type="page_range", supports="definition / neocortex ratio / group size prediction", verified=True),
   dict(kind="BOOK", title_en="How Many Friends Does One Person Need? Dunbar's Number and Other Evolutionary Quirks",
        title_fa="یک انسان چند دوست نیاز دارد؟ عدد دانبار و دیگر عجایب تکاملی",
        authors="Dunbar, R. I. M.", year=2010, publisher="London: Faber & Faber", doi=None, url=None,
        language="en", isbn=None,
        citation="Dunbar, R. I. M. (2010). How many friends does one person need? Dunbar's number and other evolutionary quirks. Faber & Faber.",
        locator="whole work", locator_type="work", supports="evolution / social layers and support cliques", verified=False),
 ],
 "MC-261": [
   dict(kind="BOOK", title_en="What's Mine Is Yours: The Rise of Collaborative Consumption",
        title_fa="آنچه مال من است مال توست: ظهور مصرف مشارکتی",
        authors="Botsman, R., & Rogers, R.", year=2010, publisher="New York: HarperBusiness", doi=None,
        url="https://www.harpercollins.com/products/whats-mine-is-yours-rachel-botsmanroo-rogers",
        language="en", isbn=None,
        citation="Botsman, R., & Rogers, R. (2010). What's mine is yours: The rise of collaborative consumption. HarperBusiness.",
        locator="whole work", locator_type="work", supports="definition / three systems of collaborative consumption", verified=True),
   dict(kind="REPORT", title_en="Debating the Sharing Economy",
        title_fa="مناقشه دربارهٔ اقتصاد اشتراکی",
        authors="Schor, J. B.", year=2014,
        publisher="Great Transition Initiative (Tellus Institute)", doi=None, url=None,
        language="en", isbn=None,
        citation="Schor, J. B. (2014). Debating the sharing economy. Great Transition Initiative.",
        locator="essay", locator_type="work", supports="critique / commercialization and labor precarity", verified=False),
 ],
}

ENRICH = {
 "MC-242": {
   "summary": "«نظریهٔ غنای رسانه» (Media Richness Theory) می‌گوید اثربخشی ارتباط سازمانی به تناسب «غنای» رسانه با «ابهامِ» پیام بستگی دارد و رسانه‌ها در ظرفیت انتقال معنا یکسان نیستند. ریچارد دفت و رابرت لنگل در «Organizational Information Requirements, Media Richness and Structural Design» (۱۹۸۶، Management Science) نشان دادند سازمان‌ها برای کاهش عدم قطعیت و رفع ابهام به پردازش اطلاعات نیاز دارند و طراحی ساختاری می‌تواند با این نیاز هم‌خوان شود (Daft & Lengel, 1986).",
   "definition": "غنای رسانه یعنی ظرفیت یک رسانه برای تغییر فهم مشترک در بازهٔ زمانی معین؛ رسانه‌ای غنی‌تر است که ابهام را سریع‌تر و کامل‌تر کاهش دهد (Daft & Lengel, 1986).",
   "main_problem": "دو پرسش بنیادی: چرا سازمان‌ها اطلاعات را پردازش می‌کنند، و چه معیاری نشان می‌دهد یک رسانه برای یک پیام مشخص «مناسب» است؟ دفت و لنگل می‌کوشند پیوندی میان ویژگی‌های پیام، ظرفیت رسانه و شکل ساختار سازمانی برقرار کنند (Daft & Lengel, 1986).",
   "mechanism": "نظریه بر چهار سازوکار پیوسته استوار است. (۱) تفکیک «عدم قطعیت» (uncertainty) از «ابهام» (equivocality): عدم قطعیت کمبود اطلاعات است و با دادهٔ بیشتر رفع می‌شود؛ ابهام چندمعنایی و تعارض تفسیرهاست و تنها با مذاکرهٔ معنا میان افراد کاهش می‌یابد (Daft & Lengel, 1986). این تفکیک، بنیاد کل نظریه است، زیرا یک پیام می‌تواند از نظر داده کامل و در همان حال مبهم باشد. (۲) چهار معیار غنا: ظرفیت «بازخورد فوری»، توانایی انتقال «چند نشانه» هم‌زمان (لحن، حالت چهره، ژست)، «تنوع زبان» (کلام طبیعی در برابر عدد و فرمول) و «تمرکز شخصی» (حضور احساسی و انسانی فرستنده). بر این پایه سلسله‌مراتبی ساخته می‌شود: گفت‌وگوی رودررو غنی‌ترین رسانه، سپس تلفن، سپس اسناد شخصی‌نویس‌شده و در انتها اسناد رسمی و داده‌های عددی کم‌غنا. (۳) تناسب رسانه و وظیفه: پیام مبهم باید با رسانهٔ غنی و پیام روشن با رسانهٔ کم‌غنا منتقل شود؛ ناهم‌خوانی در هر دو جهت هزینه دارد. رسانهٔ کم‌غنا برای ابهام به تفسیر نادرست و تعارض می‌انجامد و رسانهٔ غنی برای پیام روشن به اتلاف زمان، «بار ارتباطی» و جلسه‌های بی‌ثمر. (۴) پیامد ساختاری: سازمان برای رفع ابهام به ساختار «ارگانیک»، مذاکره و تماس رودررو گرایش دارد و برای کاهش عدم قطعیت به ساختار «مکانیکی»، قاعده و گزارش استاندارد؛ این همان پیوندی است که در عنوان مقاله به «طراحی ساختاری» اشاره شده است (Daft & Lengel, 1986). در بستر رسانه، نظریه توضیح می‌دهد چرا اعلام تغییر ساختار تحریریه در نشست حضوری انجام می‌شود و جزئیات اجرایی آن با بخشنامهٔ مکتوب می‌رسد: اولی ابهام دارد و به مذاکره نیازمند است، دومی اطلاعات را منتقل می‌کند.",
   "assumptions": [
     "درجهٔ ابهام ویژگی قابل تشخیص پیام است و میان پیام‌ها تفاوت معنادار دارد.",
     "رسانه‌ها ظرفیت نسبتاً ثابتی برای انتقال معنا دارند و این ظرفیت قابل رتبه‌بندی است.",
     "اثربخشی ارتباط را می‌توان با درجهٔ تناسب رسانه و وظیفه توضیح داد."
   ],
   "principles": [
     "تفکیک ابهام (چندمعنایی) از عدم قطعیت (کمبود اطلاعات).",
     "چهار معیار غنا: بازخورد فوری، چند نشانه، تنوع زبان و تمرکز شخصی.",
     "تناسب رسانه و وظیفه در دو جهت: کم‌غنایی برای ابهام و غنای زیاد برای پیام روشن هر دو پرهزینه‌اند."
   ],
   "critiques": [
     "نظریهٔ نفوذ اجتماعی (Fulk, Schmitz & Steinfield, 1990) نشان داد انتخاب رسانه تابع هنجارهای همکاران و فشار اجتماعی است، نه فقط محاسبهٔ عقلانی تناسب.",
     "مارکوس (Markus, 1994) در مطالعهٔ ایمیل سازمانی دید مدیران برای پیام‌های مبهم نیز از ایمیل استفاده می‌کنند و غنا را در عمل بازتعریف می‌کنند.",
     "نظریهٔ بسط کانال (Carlson & Zmud, 1999) اثبات کرد «غنای ادراک‌شده» با تجربهٔ کاربر از همان رسانه افزایش می‌یابد؛ پس غنا ثابت نیست."
   ],
   "applications": [
     "طراحی جریان اطلاع‌رسانی در تحریریه‌ها: تعیین خط مشی در نشست حضوری و اعلان قطعی با سند مکتوب.",
     "مدیریت بحران و ارتباط با ذی‌نفعان در وضعیت‌های مبهم و پرتنش.",
     "انتخاب ابزار در کار تیمی و دورکاری و سنجش هزینهٔ جلسه در برابر پیام نوشتاری.",
     "آموزش سواد ارتباطی سازمانی: چرا ایمیل جای گفت‌وگوی رودررو را نمی‌گیرد."
   ],
   "evolution": "مقالهٔ اصلی ۱۹۸۶ چارچوب را در نظریهٔ پردازش اطلاعات سازمانی جای داد؛ دفت، لنگل و تروینو (۱۹۸۷، MIS Quarterly) آن را به عملکرد مدیران پیوند زدند. در دههٔ ۱۹۹۰ نقدهای نفوذ اجتماعی و مطالعهٔ مارکوس (۱۹۹۴) فرض غنای عینی را متزلزل کرد و کارلسون و زمود (۱۹۹۹) با نظریهٔ بسط کانال، غنا را ادراکی و آموختنی خواندند. در عصر ویدئوکنفرانس و پیام‌رسان، پژوهش‌ها مفهوم را به «قابلیت‌های رسانه» و ترکیب هم‌زمان چند کانال گستردند.",
   "key_concepts": ["غنای رسانه (media richness)", "ابهام (equivocality)", "عدم قطعیت (uncertainty)", "تناسب رسانه و وظیفه (media-task fit)", "بازخورد فوری (instant feedback)", "تمرکز شخصی (personal focus)"],
   "studies": ["Daft, R. L., & Lengel, R. H. (1986). Organizational information requirements, media richness and structural design. Management Science, 32(5), 554-571.", "Daft, R. L., Lengel, R. H., & Trevino, L. K. (1987). Message equivocality, media selection, and manager performance. MIS Quarterly, 11(3), 355-366."],
   "detailed_analysis": "۱. بنیان و منطق نظری\nنظریهٔ غنای رسانه در سنت «نظریهٔ پردازش اطلاعات سازمان» ریشه دارد: سازمان نظامی اجتماعی است که برای بقا باید عدم قطعیت محیط و ابهام رویدادها را پردازش کند. دفت و لنگل (۱۹۸۶) دو نیروی متفاوت را از هم جدا می‌کنند: نیروی کاهش عدم قطعیت که با گردآوری داده پاسخ می‌گیرد و نیروی رفع ابهام که با گفت‌وگو، تفسیر مشترک و مذاکرهٔ معنا پاسخ می‌گیرد. از این تفکیک نتیجه می‌شود که «اطلاعات بیشتر» همیشه راه‌حل نیست؛ گاه مسئله کمبود داده نیست، بلکه نبود فهم مشترک است.\n\n۲. پیوند رسانه و ساختار\nنویسندگان رسانه را واسطهٔ میان پیام و فهم می‌بینند و معتقدند هر رسانه بستهٔ مشخصی از قابلیت‌ها را عرضه می‌کند. ساختار سازمانی نیز در همین منطق خوانده می‌شود: واحدهایی که با ابهام بالا سر و کار دارند به سازوکارهای تماس مستقیم و گروه‌های حل مسئله نیاز دارند و واحدهای با وظایف روشن به قاعده و سند استاندارد. بنابراین انتخاب رسانه صرفاً تصمیم فنی نیست، بلکه تصمیم طراحی سازمانی است.\n\n۳. محدودیت‌های مفهومی\nنظریه رسانه را با ظرفیتی نسبتاً ثابت تعریف می‌کند؛ همین فرض، نقطهٔ ضعف آن در برابر رسانه‌های دیجیتال شد که کاربران با تجربه و هنجار جمعی، غنای آن‌ها را بازتعریف می‌کنند."
 },
 "MC-247": {
   "summary": "«نظریهٔ کاهش عدم قطعیت» (Uncertainty Reduction Theory) توضیح می‌دهد افراد در نخستین تعامل با یک فرد ناشناس چگونه می‌کوشند عدم قطعیت دربارهٔ باورها و رفتار او را کاهش دهند و چرا این کوشش به الگوهای مشخصی از پرسش، خودافشایی و تقابل می‌انجامد. چارلز برگر و ریچارد کالابرس در «Some Explorations in Initial Interaction and Beyond» (۱۹۷۵، Human Communication Research) هفت اصل موضوعه و بیست‌ویک قضیه را برای توضیح این فرایند صورتبندی کردند (Berger & Calabrese, 1975).",
   "definition": "کاهش عدم قطعیت، فرایند شناختی و ارتباطی‌ای است که با افزایش اطلاعات دربارهٔ طرف مقابل، توان پیش‌بینی و تبیین رفتار او را بالا می‌برد (Berger & Calabrese, 1975).",
   "main_problem": "هنگام روبه‌روشدن با غریبه، افراد چگونه دربارهٔ او اطلاعات جمع می‌کنند، رفتارش را پیش‌بینی می‌کنند و چرا عدم قطعیت، جریان گفت‌وگو را به شکل‌های تکرارشونده هدایت می‌کند؟ نظریه می‌کوشد مرحلهٔ ورود به تعامل میان‌فردی را به نظریه‌ای قابل آزمون بدل کند (Berger & Calabrese, 1975).",
   "mechanism": "نظریه از چهار لایه ساخته می‌شود. (۱) دو نوع عدم قطعیت: «شناختی» یعنی ناتوانی در پیش‌بینی باورها، نگرش‌ها و ارزش‌های طرف مقابل، و «رفتاری» یعنی ناتوانی در پیش‌بینی کنش‌های او در موقعیت‌های گوناگون (Berger & Calabrese, 1975). این تفکیک نشان می‌دهد آشنایی اطلاعاتی با شناخت عمیق یکی نیست. (۲) هفت اصل موضوعه: با افزایش ارتباط کلامی، بیانگری غیرکلامی گرم، جست‌وجوی اطلاعات، خودافشایی، تقابل، شباهت ادراک‌شده و پسندیدن، عدم قطعیت کاهش می‌یابد. از ترکیب این اصول، بیست‌ویک قضیه استنتاج شد که پیش‌بینی‌های آزمون‌پذیر دربارهٔ رابطهٔ متغیرها می‌دهد (Berger & Calabrese, 1975). (۳) سه راهبرد جست‌وجوی اطلاعات که برگر بعدها صورت‌بندی کرد: «منفعل» (مشاهدهٔ طرف مقابل در موقعیت طبیعی)، «فعال» (پرس‌وجو از دیگران یا دست‌کاری محیط برای دیدن واکنش) و «تعاملی» (پرسش مستقیم در گفت‌وگو). افراد معمولاً از راهبرد کم‌هزینه به پرهزینه حرکت می‌کنند. (۴) منطق انگیزشی: عدم قطعیت تجربه‌ای آزارنده است و افراد می‌کوشند آن را کاهش دهند، اما هزینه و خطر هر راهبرد متفاوت است؛ ازاین‌رو پیش از گفت‌وگوی رودررو، مشاهده و پرس‌وجوی غیرمستقیم ترجیح داده می‌شود. در محیط رسانه‌ای دیجیتال، این منطق در پیمایش پروفایل، خواندن ردّ دیجیتال و پرس‌وجو در شبکه‌های اجتماعی بازتولید می‌شود: کاربر پیش از نخستین پیام، ماه‌ها «تماشاگر» می‌ماند و عدم قطعیت را با راهبرد منفعل کاهش می‌دهد. همین سازوکار توضیح می‌دهد چرا در پلتفرم‌های دوستیابی و شبکه‌های حرفه‌ای، بخش بزرگی از رفتار کاربران پیش از تعامل رخ می‌دهد.",
   "assumptions": [
     "افراد در تعامل اولیه با غریبه، انگیزهٔ کاهش عدم قطعیت دارند.",
     "عدم قطعیت با متغیرهای ارتباطی مانند خودافشایی و تقابل رابطهٔ منظم دارد.",
     "کاهش عدم قطعیت، پیش‌بینی و تبیین رفتار طرف مقابل را ممکن‌تر می‌کند."
   ],
   "principles": [
     "تفکیک عدم قطعیت شناختی از رفتاری.",
     "هفت اصل موضوعه و بیست‌ویک قضیهٔ استنتاجی به‌عنوان هستهٔ آزمون‌پذیر نظریه.",
     "سه راهبرد منفعل، فعال و تعاملی با هزینهٔ فزاینده."
   ],
   "critiques": [
     "نظریهٔ ارزش پیامد پیش‌بینی‌شده (Sunnafrank, 1986) نشان داد انگیزهٔ اصلی افراد انتظار پاداش رابطه است، نه کاهش عدم قطعیت به‌خودی‌خود.",
     "نظریهٔ مدیریت عدم قطعیت (Brashers, 2001) اثبات کرد افراد در موقعیت‌های تهدیدکننده آگاهانه عدم قطعیت را حفظ یا حتی افزایش می‌دهند.",
     "تعمیم بین‌فرهنگی نظریه محل بحث است؛ گودیکانست چارچوب را به «مدیریت اضطراب و عدم قطعیت» بازنویسی کرد."
   ],
   "applications": [
     "تحلیل رفتار کاربران در پلتفرم‌های اجتماعی و دوستیابی پیش از نخستین تعامل.",
     "طراحی فرایند آشناسازی کارکنان تازه‌وارد و مصاحبهٔ شغلی.",
     "آموزش ارتباطات بین‌فرهنگی و کاهش اضطراب در تعامل با فرهنگ ناآشنا.",
     "پژوهش دربارهٔ شکل‌گیری برداشت اولیه در محیط‌های کاملاً متنی."
   ],
   "evolution": "برگر و کالابرس (۱۹۷۵) هستهٔ اصل‌موضوعه‌ای را عرضه کردند؛ برگر (۱۹۷۹) راهبردهای جست‌وجوی اطلاعات را تفکیک کرد و برگر و گودیکانست (۱۹۹۱) نظریه را با پژوهش عدم قطعیت در ارتباطات پیوند زدند. در دههٔ ۱۹۸۰-۱۹۹۰ نقدهای سانافرانک و بعدها برشرز، فرض «کاهش همیشگی» را اصلاح کرد و در دههٔ ۲۰۰۰ پژوهش ارتباط کامپیوتری‌شده، راهبردهای منفعل را برای محیط آنلاین بازتعریف کرد.",
   "key_concepts": ["عدم قطعیت شناختی (cognitive uncertainty)", "عدم قطعیت رفتاری (behavioral uncertainty)", "اصل موضوعه (axiom)", "قضیه (theorem)", "راهبرد منفعل/فعال/تعاملی (passive/active/interactive)", "تقابل (reciprocity)", "خودافشایی (self-disclosure)"],
   "studies": ["Berger, C. R., & Calabrese, R. J. (1975). Some explorations in initial interaction and beyond. Human Communication Research, 1(2), 99-112.", "Berger, C. R., & Gudykunst, W. B. (1991). Uncertainty and communication. Progress in Communication Sciences, 10, 23-66."],
   "detailed_analysis": "۱. بنیان و منطق نظری\nنظریهٔ کاهش عدم قطعیت در سنت «نظریهٔ میان‌فردی پساتجربی» جای دارد: هدف آن نه توصیهٔ هنجاری، بلکه پیش‌بینی و تبیین است. برگر و کالابرس (۱۹۷۵) از این ایده آغاز می‌کنند که تعامل با غریبه وضعیتی ذاتاً نامطمئن است، زیرا فرد نه شناخت کافی از طرف مقابل دارد و نه می‌داند چه انتظاری باید داشته باشد. ازاین‌رو ارتباط نخستین، فعالیتی برای «کسب کنترل شناختی» بر موقعیت است.\n\n۲. شرایط پیشایند\nنظریه سه شرط را مؤثر می‌داند: انتظار پاداش یا هزینهٔ تعامل، انحراف طرف مقابل از هنجارهای مورد انتظار، و انتظار تعامل آینده. هرچه احتمال تعامل آینده بیشتر باشد، انگیزهٔ کاهش عدم قطعیت افزایش می‌یابد؛ همین نکته توضیح می‌دهد چرا افراد در موقعیت‌های یک‌باره سرمایه‌گذاری شناختی کمتری می‌کنند.\n\n۳. کارکرد ارتباط\nارتباط در این چارچوب ابزار اصلی کاهش عدم قطعیت است: پرسش، خودافشایی متقابل و تقابل، جریان اطلاعات را تنظیم می‌کنند. بااین‌حال، نظریه به «اقتصاد اطلاعات» باور دارد؛ افراد تا جایی اطلاعات می‌جویند که هزینهٔ جست‌وجو از سود پیش‌بینی بیشتر نشود."
 },
 "MC-260": {
   "summary": "«عدد دانبار» (Dunbar's Number) برآوردی است از تعداد روابط اجتماعی پایدار و معناداری که یک انسان می‌تواند هم‌زمان نگه دارد: حدود ۱۵۰ نفر. رابین دانبار در «Neocortex Size as a Constraint on Group Size in Primates» (۱۹۹۲، Journal of Human Evolution) با تحلیل رابطهٔ اندازهٔ نئوکورتکس و اندازهٔ گروه در نخستی‌ها این برآورد را برای انسان پیش‌بینی کرد (Dunbar, 1992).",
   "definition": "عدد دانبار سقف شناختی تقریبی شبکهٔ روابط پایدار انسانی است که از ظرفیت پردازش اجتماعی مغز و بودجهٔ زمانی نگهداری رابطه برمی‌آید (Dunbar, 1992).",
   "main_problem": "چرا اندازهٔ گروه اجتماعی در نخستی‌ها، از جمله انسان، به‌جای آنکه تنها تابع منابع محیطی باشد، با ظرفیت مغز محدود می‌شود؟ و اگر چنین محدودیتی وجود دارد، ساختار شبکهٔ اجتماعی انسان چگونه سازمان می‌یابد؟",
   "mechanism": "استدلال در چهار گام بسط می‌یابد. (۱) «فرضیهٔ مغز اجتماعی»: اندازهٔ گروه در نخستی‌ها با نسبت اندازهٔ نئوکورتکس به بقیهٔ مغز همبسته است، نه با متغیرهای بوم‌شناختی؛ تحلیل دانبار (۱۹۹۲) نشان داد گروه‌بندی تابع حجم نسبی نئوکورتکس است و این شواهد به سود توضیح اجتماعی، نه بوم‌شناختی، تکامل مغز بزرگ است. با کاربست این رابطه بر انسان، اندازهٔ گروه پیش‌بینی‌شده حدود ۱۵۰ نفر می‌شود. (۲) «بودجهٔ زمان»: پیوندهای اجتماعی در نخستی‌ها با آراستگی (grooming) حفظ می‌شود و آراستگی زمان‌بر است؛ با بزرگ‌شدن گروه، زمان لازم از ساعات بیداری فراتر می‌رود. دانبار استدلال می‌کند زبان در انسان جایگزین کارکردی آراستگی شد و با امکان «آراستگی چندنفره» هم‌زمان، سقف شناختی را از سقف زمانی جدا کرد (Dunbar, 1993). (۳) «لایه‌بندی شبکه»: روابط انسان در حلقه‌های تودرتو با اندازه‌های تقریبی ۵ (حمایت‌کنندگان صمیمی)، ۱۵ (دوستان نزدیک)، ۵۰ (دوستان)، ۱۵۰ (روابط معنادار) و سپس ۵۰۰ و ۱۵۰۰ (آشنایان) سازمان می‌یابند؛ هر لایه درونی‌تر، صمیمی‌تر و پرهزینه‌تر است. (۴) مکانیسم شناختی زیرین: نگهداری رابطه مستلزم حافظهٔ اجتماعی، مدل‌سازی ذهنی حالت‌های دیگری و مدیریت هم‌زمان تعهدات است؛ همین بار شناختی، سقف را تعیین می‌کند. در بستر رسانه، این چارچوب توضیح می‌دهد چرا شمار «دوستان» و «دنبال‌کنندگان» با شمار روابط واقعاً پایدار تفاوت دارد: پلتفرم‌ها ظرفیت نمایش شبکه را به‌شدت افزایش داده‌اند، اما دانبار (۲۰۱۶، Royal Society Open Science) نشان داد اندازهٔ شبکهٔ تعامل فعال کاربران در رسانه‌های اجتماعی همچنان در حدود همین سقف می‌ماند و لایه‌بندی درونی حفظ می‌شود.",
   "assumptions": [
     "ظرفیت شناختی مغز، سقف اندازهٔ شبکهٔ روابط پایدار را تعیین می‌کند.",
     "نگهداری هر رابطه هزینهٔ زمانی و شناختی دارد و این هزینه با صمیمیت افزایش می‌یابد.",
     "رابطهٔ تکاملی نخستی‌ها را می‌توان با احتیاط به انسان تعمیم داد."
   ],
   "principles": [
     "فرضیهٔ مغز اجتماعی: اندازهٔ گروه تابع ظرفیت پردازش اجتماعی است.",
     "بودجهٔ زمانی و جایگزینی کارکردی زبان به‌جای آراستگی.",
     "لایه‌بندی تودرتوی روابط با اندازه‌های ۵، ۱۵، ۵۰ و ۱۵۰."
   ],
   "critiques": [
     "لیندنفورس و همکاران (Lindenfors, Wartel & Lind, 2021, Biology Letters) نشان دادند با همان داده‌ها بازهٔ اطمینان برآورد از چند ده تا چند صد نفر گسترده است؛ «۱۵۰» نقطه‌ای دقیق نیست.",
     "اندازهٔ شبکه میان جوامع و افراد تفاوت زیادی دارد و عوامل فرهنگی و اقتصادی در آن اثر می‌گذارد.",
     "کاربرد مدیریتی عدد به‌عنوان «قانون» برای اندازهٔ تیم یا سازمان، فراتر از شواهد تجربی است."
   ],
   "applications": [
     "طراحی اندازهٔ تیم و واحد سازمانی با توجه به هزینهٔ نگهداری روابط.",
     "تحلیل تفاوت میان شبکهٔ نمایشی و شبکهٔ تعامل معنادار در پلتفرم‌ها.",
     "برنامه‌ریزی بازاریابی دهان‌به‌دهان و انتشار پیام در لایه‌های نزدیک شبکه.",
     "مدیریت بحران با تکیه بر شبکه‌های شخصی به‌جای انتشار انبوه."
   ],
   "evolution": "دانبار (۱۹۹۲) رابطهٔ نئوکورتکس و اندازهٔ گروه را منتشر کرد؛ او در ۱۹۹۳ نقش زبان را به‌عنوان جانشین کارکردی آراستگی توضیح داد. در دههٔ ۲۰۱۰ پژوهش رسانه‌های اجتماعی این پرسش را آزمود که آیا شبکه‌های دیجیتال سقف را جابه‌جا می‌کنند و پاسخ غالب منفی بود. از ۲۰۲۱ بازآزمایی‌های آماری، بر عدم قطعیت بالای برآورد تأکید کردند.",
   "key_concepts": ["فرضیهٔ مغز اجتماعی (social brain hypothesis)", "نسبت نئوکورتکس (neocortex ratio)", "لایه‌های روابط (social layers)", "بودجهٔ زمانی (time budget)", "آراستگی (grooming)", "شبکهٔ پشتیبان (support clique)"],
   "studies": ["Dunbar, R. I. M. (1992). Neocortex size as a constraint on group size in primates. Journal of Human Evolution, 22(6), 469-493.", "Dunbar, R. I. M. (2010). How Many Friends Does One Person Need? Faber & Faber."],
   "detailed_analysis": "۱. بنیان و منطق نظری\nعدد دانبار از یک مسئلهٔ تکاملی آغاز می‌شود: چرا نخستی‌ها مغزهای بزرگ‌تری نسبت به پستانداران هم‌اندازه دارند؟ پاسخ دانبار (۱۹۹۲) اجتماعی است، نه بوم‌شناختی: زندگی گروهی نیازمند پردازش هم‌زمان روابط، اتحادها، رقابت‌ها و تعهدات است و مغز بزرگ‌تر ظرفیت این پردازش را فراهم می‌کند. اندازهٔ نئوکورتکس، پس، شاخصی از ظرفیت اجتماعی است، نه صرفاً از هوش ابزارسازی.\n\n۲. از نخستی به انسان\nرابطهٔ تجربی میان حجم نسبی نئوکورتکس و اندازهٔ گروه در نخستی‌ها به انسان تعمیم داده می‌شود و عددی در حدود ۱۵۰ به دست می‌آید. این عدد «سقف» است، نه میانگین: یعنی بیشتر افراد امکان نگهداری چنین شماره‌ای را دارند، اما همه به آن نمی‌رسند.\n\n۳. کارکرد رسانه‌ای\nرسانه‌های اجتماعی هزینهٔ «نگهداری ظاهری» رابطه را کاهش داده‌اند، اما رابطهٔ پایدار به تعامل دوسویه و سرمایه‌گذاری زمانی نیاز دارد. ازاین‌رو پلتفرم‌ها می‌توانند آشنایان را انبار کنند، بی‌آنکه ظرفیت شناختی روابط صمیمی را گسترش دهند."
 },
 "MC-261": {
   "summary": "«اقتصاد اشتراکی» (The Sharing Economy) به مجموعه‌ای از بازارهای همتا-به-همتا گفته می‌شود که در آن‌ها دسترسی موقت به کالا، فضا، مهارت یا زمان جای مالکیت را می‌گیرد و پلتفرم‌های دیجیتال عرضهٔ خرد افراد را به تقاضا متصل می‌کنند. ریچل بوتسمن و روگرز روگرز در «What's Mine Is Yours» (۲۰۱۰، HarperBusiness) این پدیده را «مصرف مشارکتی» نامیدند و سه نظام آن را از هم جدا کردند (Botsman & Rogers, 2010).",
   "definition": "اقتصاد اشتراکی مجموعهٔ مبادلات مبتنی بر دسترسی است که در آن کاربران از طریق پلتفرم، ظرفیت بلااستفادهٔ دارایی یا مهارت خود را به دیگران عرضه می‌کنند و اعتماد با سازوکارهای امتیاز و بازخورد ساخته می‌شود (Botsman & Rogers, 2010).",
   "main_problem": "چرا مصرف مبتنی بر دسترسی در دههٔ ۲۰۱۰ رشد کرد، این بازارها بر چه سازوکاری اعتماد میان غریبه‌ها را ممکن می‌کنند، و مرز میان مصرف، کار و سرمایه‌گذاری در آن‌ها چگونه جابه‌جا می‌شود؟",
   "mechanism": "سازوکار در چهار سطح عمل می‌کند. (۱) جابه‌جایی محور ارزش از مالکیت به دسترسی: بوتسمن و روگرز (۲۰۱۰) استدلال می‌کنند بخشی از مصرف از خرید کالا به اجاره، اشتراک و مبادلهٔ موقت تغییر کرده است؛ آنچه مصرف‌کننده می‌خواهد «کارکرد» کالاست، نه سند مالکیت آن. (۲) سه نظام مصرف مشارکتی: «نظام‌های خدمات محصول» (اجارهٔ کالای بادوام مانند خودرو و خانه)، «بازارهای بازتوزیع» (فروش و مبادلهٔ کالای بلااستفاده) و «سبک‌های زندگی مشارکتی» (تبادل فضا، زمان، مهارت و پول مانند هم‌سفر شدن یا اشتراک محل کار). (۳) زیرساخت اعتماد: چون طرفین معامله غریبه‌اند، پلتفرم با پروفایل، نظام امتیاز و بازخورد، بیمه و تضمین پرداخت، ریسک را کاهش می‌دهد و «سرمایهٔ اعتبار» را قابل انتقال می‌سازد؛ همین سازوکار، تفاوت اصلی این بازارها با آگهی‌های طبقه‌بندی‌شدهٔ پیشین است. (۴) بهره‌برداری از ظرفیت بیکار و کاهش هزینهٔ مبادله: اتاق خالی، خودروی بی‌استفاده و ساعت آزاد به دارایی درآمدزا تبدیل می‌شوند و پلتفرم با کاهش هزینهٔ جست‌وجو و تطبیق، این ظرفیت را وارد بازار می‌کند. در بستر رسانه، منطق اقتصاد اشتراکی در گذار از خرید مالکیتی محتوا (دی‌وی‌دی، آلبوم) به دسترسی اشتراکی (استریم، اشتراک دیجیتال)، در اقتصاد سازنده و در تأمین مالی جمعی روزنامه‌نگاری بازتولید می‌شود؛ همان‌جا نیز پلتفرم با نظام اعتبار و شهرت، میان تولیدکنندهٔ خرد و مخاطب واسطه می‌شود.",
   "assumptions": [
     "دسترسی موقت می‌تواند کارکرد مالکیت را برای بخشی از مصرف برآورده کند.",
     "سازوکارهای اعتبار دیجیتال می‌توانند ریسک معامله با غریبه را به‌اندازهٔ کافی کاهش دهند.",
     "ظرفیت بلااستفادهٔ دارایی‌های فردی، منبع اقتصادی قابل بهره‌برداری است."
   ],
   "principles": [
     "دسترسی بر مالکیت مقدم است.",
     "سه نظام: خدمات محصول، بازارهای بازتوزیع و سبک‌های زندگی مشارکتی.",
     "اعتماد پلتفرمی جایگزین اعتماد چهره‌به‌چهره می‌شود."
   ],
   "critiques": [
     "شور (Schor, 2014) نشان داد بخش بزرگی از این بازارها تجاری و متمرکز بر سود سرمایه‌گذارند و «اشتراکی» بودن آن‌ها محل مناقشه است.",
     "پژوهش‌ها دربارهٔ تبعیض در پلتفرم‌ها (Edelman, Luca & Svirsky, 2017) نشان داد سازوکار اعتبار، سوگیری‌های نژادی و جنسیتی را حذف نمی‌کند.",
     "ادعای پایداری زیست‌محیطی متناقض است: مصرف بیشتر و سفرهای اضافی می‌تواند اثرات منفی ایجاد کند."
   ],
   "applications": [
     "تحلیل مدل درآمد و مالکیت در پلتفرم‌های رسانه‌ای و محتوای کاربرساخته.",
     "سیاست‌گذاری دربارهٔ کار مستقل و مقررات پلتفرمی.",
     "مطالعهٔ نظام اعتبار و شهرت در بازارهای دیجیتال.",
     "بررسی گذار از مالکیت به دسترسی در مصرف فرهنگی و رسانه‌ای."
   ],
   "evolution": "بوتسمن و روگرز (۲۰۱۰) مفهوم مصرف مشارکتی را عمومی کردند؛ در نیمهٔ دههٔ ۲۰۱۰ شرکت‌های بزرگ (Airbnb و Uber) آن را به بازارهای انبوه رساندند. شور (۲۰۱۴) نقد تجاری‌شدن را صورتبندی کرد و از ۲۰۱۷ پژوهش‌های تبعیض و کار پراکنده، چارچوب را به سمت مقررات و عدالت منتقل ساخت.",
   "key_concepts": ["دسترسی در برابر مالکیت (access over ownership)", "مصرف مشارکتی (collaborative consumption)", "بازار همتا-به-همتا (P2P market)", "سرمایهٔ اعتبار (reputation capital)", "ظرفیت بیکار (idle capacity)", "کار پراکنده (gig work)"],
   "studies": ["Botsman, R., & Rogers, R. (2010). What's Mine Is Yours. HarperBusiness.", "Schor, J. B. (2014). Debating the sharing economy. Great Transition Initiative."],
   "detailed_analysis": "۱. بنیان و منطق نظری\nاقتصاد اشتراکی در تلاقی دو تحول شکل گرفت: فناوری شبکه‌ای که هزینهٔ اتصال و تطبیق را کاهش داد، و بحران مالی ۲۰۰۸ که انگیزهٔ بهره‌گیری از ظرفیت بلااستفاده و درآمد مکمل را بالا برد. بوتسمن و روگرز (۲۰۱۰) این را تغییری در «منطق مصرف» خواندند: ارزش از تملک شیء به تجربهٔ استفاده از آن منتقل می‌شود.\n\n۲. مسئلهٔ اعتماد\nبازار همتا-به-همتا بدون اعتماد کار نمی‌کند، زیرا طرفین یکدیگر را نمی‌شناسند و نهاد واسط سنتی وجود ندارد. راه‌حل پلتفرم، تبدیل اعتماد به داده است: امتیاز، بازخورد عمومی، سابقهٔ معامله و بیمه. این سازوکار هم توانمندساز است و هم آسیب‌پذیر، زیرا امتیاز می‌تواند به سوگیری و «جریمهٔ اعتباری» بینجامد.\n\n۳. مرزهای مبهم\nدر این بازارها مصرف‌کننده می‌تواند تولیدکننده باشد، دارایی شخصی به سرمایهٔ مولد تبدیل شود و کار بدون قرارداد رسمی انجام گیرد. همین ابهام، هم نوآوری مقرراتی می‌آفریند و هم فضایی برای فرار از تعهدات کارگری و بیمه‌ای."
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
    codes = ["MC-242", "MC-247", "MC-260", "MC-261"]
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
    print("BATCH55 THEORY DONE")

if __name__ == "__main__":
    main()
