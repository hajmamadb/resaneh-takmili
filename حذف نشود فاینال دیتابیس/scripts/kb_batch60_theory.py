# -*- coding: utf-8 -*-
"""Batch 60 (THEORY): MC-294 Privacy Self-Management & the Consent Dilemma (Solove 2013),
MC-297 Data Trusts (Delacroix & Lawrence 2019), MC-298 Regulatory Capture (Stigler 1971),
MC-302 Mathematical Theory of Information (Shannon 1948). Anchors verified 2026-11-16."""
import pymysql, json

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch60-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch60_theory.json"

S = {
 "MC-294": [
   dict(kind="JOURNAL_ARTICLE", title_en="Introduction: Privacy Self-Management and the Consent Dilemma",
        title_fa="درآمدی بر خودمدیریتی حریم خصوصی و معضل رضایت",
        authors="Solove, D. J.", year=2013,
        publisher="Harvard Law Review, 126(7), 1880-1903", doi=None,
        url="https://harvardlawreview.org/print/vol-126/introduction-privacy-self-management-and-the-consent-dilemma/",
        language="en", isbn=None,
        citation="Solove, D. J. (2013). Introduction: Privacy self-management and the consent dilemma. Harvard Law Review, 126(7), 1880-1903.",
        locator="pp. 1880-1903", locator_type="page_range", supports="definition / consent dilemma / structural critique", verified=True),
   dict(kind="BOOK_CHAPTER", title_en="Big Data's End Run Around Anonymity and Consent",
        title_fa="عبور داده‌های کلان از گمنامی و رضایت",
        authors="Barocas, S., & Nissenbaum, H.", year=2014,
        publisher="In J. Lane et al. (Eds.), Privacy, Big Data, and the Public Good (pp. 44-75). Cambridge University Press",
        doi=None, url=None, language="en", isbn=None,
        citation="Barocas, S., & Nissenbaum, H. (2014). Big data's end run around anonymity and consent. In Privacy, big data, and the public good (pp. 44-75). Cambridge University Press.",
        locator="pp. 44-75", locator_type="page_range", supports="evolution / limits of consent and anonymity", verified=False),
 ],
 "MC-297": [
   dict(kind="JOURNAL_ARTICLE", title_en="Bottom-up Data Trusts: Disturbing the 'One Size Fits All' Approach to Data Governance",
        title_fa="امین‌های دادهٔ از پایین: برهم‌زدن رویکرد «یک اندازه برای همه» در حاکمیت داده",
        authors="Delacroix, S., & Lawrence, N. D.", year=2019,
        publisher="International Data Privacy Law, 9(4), 236-252", doi=None,
        url="https://academic.oup.com/idpl/article/9/4/236/5579842",
        language="en", isbn=None,
        citation="Delacroix, S., & Lawrence, N. D. (2019). Bottom-up data trusts: Disturbing the 'one size fits all' approach to data governance. International Data Privacy Law, 9(4), 236-252.",
        locator="pp. 236-252", locator_type="page_range", supports="definition / fiduciary model / pooled data rights", verified=True),
   dict(kind="REPORT", title_en="Data Trusts: Ethics, Architecture and Governance for Trustworthy Data Stewardship",
        title_fa="امین‌های داده: اخلاق، معماری و حاکمیت برای قیمومیت قابل اعتماد داده",
        authors="O'Hara, K.", year=2019, publisher="Southampton: Web Science Institute White Paper",
        doi=None, url=None, language="en", isbn=None,
        citation="O'Hara, K. (2019). Data trusts: Ethics, architecture and governance for trustworthy data stewardship. Web Science Institute White Paper.",
        locator="white paper", locator_type="work", supports="evolution / governance design", verified=False),
 ],
 "MC-298": [
   dict(kind="JOURNAL_ARTICLE", title_en="The Theory of Economic Regulation",
        title_fa="نظریهٔ تنظیم‌گری اقتصادی",
        authors="Stigler, G. J.", year=1971,
        publisher="The Bell Journal of Economics and Management Science, 2(1), 3-21", doi=None,
        url="https://bfi.uchicago.edu/wp-content/uploads/2023/02/3003160.pdf",
        language="en", isbn=None,
        citation="Stigler, G. J. (1971). The theory of economic regulation. The Bell Journal of Economics and Management Science, 2(1), 3-21.",
        locator="pp. 3-21", locator_type="page_range", supports="definition / industry demand for regulation / capture", verified=True),
   dict(kind="JOURNAL_ARTICLE", title_en="Toward a More General Theory of Regulation",
        title_fa="به‌سوی نظریهٔ عمومی‌تر تنظیم‌گری",
        authors="Peltzman, S.", year=1976,
        publisher="Journal of Law and Economics, 19(2), 211-240", doi=None, url=None, language="en", isbn=None,
        citation="Peltzman, S. (1976). Toward a more general theory of regulation. Journal of Law and Economics, 19(2), 211-240.",
        locator="pp. 211-240", locator_type="page_range", supports="evolution / regulator's balancing model", verified=False),
 ],
 "MC-302": [
   dict(kind="JOURNAL_ARTICLE", title_en="A Mathematical Theory of Communication",
        title_fa="نظریهٔ ریاضی ارتباط",
        authors="Shannon, C. E.", year=1948,
        publisher="Bell System Technical Journal, 27(3), 379-423 and 27(4), 623-656", doi="10.1002/j.1538-7305.1948.tb01338.x",
        url="https://onlinelibrary.wiley.com/doi/abs/10.1002/j.1538-7305.1948.tb01338.x",
        language="en", isbn=None,
        citation="Shannon, C. E. (1948). A mathematical theory of communication. Bell System Technical Journal, 27(3), 379-423; 27(4), 623-656.",
        locator="pp. 379-423, 623-656", locator_type="page_range", supports="definition / entropy / channel capacity", verified=True),
   dict(kind="BOOK", title_en="The Mathematical Theory of Communication",
        title_fa="نظریهٔ ریاضی ارتباط",
        authors="Shannon, C. E., & Weaver, W.", year=1949, publisher="Urbana: University of Illinois Press", doi=None, url=None,
        language="en", isbn=None,
        citation="Shannon, C. E., & Weaver, W. (1949). The mathematical theory of communication. University of Illinois Press.",
        locator="whole work", locator_type="work", supports="evolution / technical, semantic and effectiveness levels", verified=False),
 ],
}

ENRICH = {
 "MC-294": {
   "summary": "«خودمدیریتی حریم خصوصی و معضل رضایت» (Privacy Self-Management and the Consent Dilemma) نقدی ساختاری بر الگویی است که حفاظت از داده را به انتخاب آگاهانهٔ فرد و رضایت او واگذار می‌کند. دانیل سولو در مقالهٔ «Introduction: Privacy Self-Management and the Consent Dilemma» (۲۰۱۳، Harvard Law Review) نشان داد این الگو، نه به‌سبب بی‌توجهی کاربران، بلکه به‌سبب ساختار خود مسئله ناکام می‌ماند (Solove, 2013).",
   "definition": "خودمدیریتی حریم خصوصی، سپردن تصمیم دربارهٔ جمع‌آوری و استفاده از داده به خود فرد از طریق اطلاع‌رسانی و رضایت است؛ معضل رضایت به این معناست که هر تلاشی برای معنادارکردن رضایت، یا کاربر را با حجم غیرقابل‌مدیریتی از انتخاب روبه‌رو می‌کند یا رضایت را به تشریفات تهی فرومی‌کاهد (Solove, 2013).",
   "main_problem": "اگر رضایت آگاهانهٔ فرد مبنای مشروعیت پردازش داده باشد، چگونه می‌توان آن را در محیطی معنادار کرد که در آن پیامدهای داده نامعلوم، استفاده‌های آینده پیش‌بینی‌ناپذیر و تعداد تصمیم‌ها از توان هر فرد فراتر است؟",
   "mechanism": "سولو سه لایهٔ ناکارآمدی را نشان می‌دهد. (۱) آسیب جمعی و غیرفردی: بسیاری از آسیب‌های داده — تبعیض آماری، نظارت تودرتا و تحلیل رفتار جمعی — در سطح فرد قابل ارزیابی نیستند؛ فرد نمی‌تواند بهایی را که با رضایت خود به جامعه تحمیل می‌کند بسنجد (Solove, 2013). (۲) مقیاس و پیچیدگی: صدها سیاست و اطلاعیه، زبان حقوقی، استفاده‌های آیندهٔ نامعلوم و زنجیرهٔ واسطه‌ها، «آگاهی» را در عمل ناممکن می‌کنند؛ حتی کاربر تحصیل‌کرده نیز نمی‌تواند همهٔ پیامدها را پیش‌بینی کند. (۳) معضل رضایت: اگر الزامات رضایت سخت‌گیرانه باشد، کاربر زیر بار تصمیم غرق می‌شود و رضایت به کلیک تبدیل می‌شود؛ اگر ساده شود، رضایت معنای حمایتی خود را از دست می‌دهد. سولو نتیجه می‌گیرد که مسئله در «کم‌کاری کاربر» نیست، بلکه در طراحی نهادی است. (۴) راه‌حل ساختاری: او به‌جای اتکای صرف بر رضایت، قواعد ماهوی محدودکنندهٔ استفاده از داده، مسئولیت‌پذیری نهادی و توجه به آسیب‌های جمعی را پیشنهاد می‌کند؛ باروکاس و نیسنباوم (۲۰۱۴) نیز نشان می‌دهند که داده‌های کلان، گمنامی و رضایت را هم‌زمان دور می‌زنند، زیرا بازشناسی از داده‌های به‌ظاهر بی‌خطر ممکن است. در بستر رسانه، این چارچوب توضیح می‌دهد چرا بنرهای رضایت کوکی، سیاست‌های حریم در سایت‌های خبری و درخواست دسترسی به دادهٔ مخاطب، به‌ندرت انتخاب آگاهانه می‌سازند: کاربر با دیوار رضایت روبه‌روست، نه با گزینهٔ واقعی.",
   "assumptions": [
     "حفاظت از داده بر پایهٔ رضایت فردی، زمانی معنا دارد که فرد بتواند پیامدها را بفهمد و مقایسه کند.",
     "برخی آسیب‌های داده در سطح جمعی رخ می‌دهند و با رضایت فردی قابل مدیریت نیستند.",
     "قواعد ماهوی و مسئولیت نهادی می‌توانند جایگزین یا مکمل رضایت باشند."
   ],
   "principles": [
     "خودمدیریتی، مسئله را به فرد منتقل می‌کند و ساختار را نادیده می‌گیرد.",
     "معضل رضایت: سخت‌گیری، فلج تصمیم می‌سازد و سادگی، حمایت را تهی می‌کند.",
     "راه‌حل در قواعد ماهوی و مسئولیت نهادی است، نه فقط رضایت."
   ],
   "critiques": [
     "پیشنهادهای جایگزین نیز به ظرفیت نظارتی و اجرایی نهادها وابسته‌اند و تضمینی برای موفقیت ندارند.",
     "مرز میان «خطر» و «آسیب» در عمل مبهم است و تعیین آستانهٔ مداخله را به داوری سیاسی می‌سپارد.",
     "تأکید بر محدودیت ماهوی می‌تواند به پدرسالاری تنظیم‌گرانه بینجامد و انتخاب‌های مشروع کاربران را محدود کند."
   ],
   "applications": [
     "تحلیل کارآمدی بنرهای رضایت کوکی و طراحی جایگزین.",
     "سیاست‌گذاری حریم خصوصی در سایت‌های خبری و اشتراک دیجیتال.",
     "آموزش سواد داده و شفاف‌سازی سیاست‌های حریم برای مخاطب.",
     "طراحی سازوکارهای حاکمیت داده در سازمان‌های رسانه‌ای."
   ],
   "evolution": "سولو (۲۰۱۳) نقد را در پاسخ به ادبیات «اطلاع و رضایت» صورت‌بندی کرد؛ باروکاس و نیسنباوم (۲۰۱۴) محدودیت گمنامی را افزودند و مقررات اروپایی حفاظت از داده، بخشی از منطق قواعد ماهوی او را نهادینه کرد، هرچند اتکا به رضایت را نیز حفظ کرد.",
   "key_concepts": ["خودمدیریتی حریم خصوصی (privacy self-management)", "معضل رضایت (consent dilemma)", "آسیب جمعی (aggregate harm)", "رضایت آگاهانه (informed consent)", "محدودیت هدف (purpose limitation)", "خستگی رضایت (consent fatigue)"],
   "studies": ["Solove, D. J. (2013). Privacy self-management and the consent dilemma. Harvard Law Review, 126(7), 1880-1903.", "Barocas, S., & Nissenbaum, H. (2014). Big data's end run around anonymity and consent. In Privacy, Big Data, and the Public Good (pp. 44-75). Cambridge University Press."],
   "detailed_analysis": "۱. بنیان و منطق نظری\nالگوی «اطلاع و رضایت» از حقوق مصرف‌کننده وام گرفته شده است: اگر فرد بداند و بپذیرد، معامله منصفانه است. سولو نشان می‌دهد این قیاس در داده شکست می‌خورد، زیرا کالای مورد معامله نامعلوم است، اثر معامله بر دیگران ممکن است بزرگ باشد و تصمیم‌ها چنان متعددند که «آگاهی» به افسانه تبدیل می‌شود.\n\n۲. از فرد به ساختار\nنقد سولو یک جابه‌جایی تحلیلی مهم می‌سازد: مسئولیت از کاربر به طراحی نهادی منتقل می‌شود. پرسش درست این نیست که چرا کاربران رضایت می‌دهند، بلکه این است که چرا نظام حقوقی، بار حفاظت را بر دوش آنان گذاشته است.\n\n۳. پیوند رسانه‌ای\nرسانه‌های خبری در دو جبهه درگیرند: از یک سو دادهٔ مخاطب را برای تبلیغات و شخصی‌سازی جمع می‌کنند و از سوی دیگر باید اعتماد را حفظ کنند. نقد سولو نشان می‌دهد که رضایت فرمولی، این تنش را حل نمی‌کند؛ شفافیت واقعی و محدودیت استفاده، مسیر پایدارتری است."
 },
 "MC-297": {
   "summary": "«امین‌های داده» (Data Trusts) نهادهایی هستند که حقوق دادهٔ گروهی از افراد را در خود جمع می‌کنند و بر پایهٔ وظیفهٔ امانت‌داری، دربارهٔ دسترسی و استفاده از آن تصمیم می‌گیرند. سیلوی دلاکروا و نیل لارنس در «Bottom-up Data Trusts» (۲۰۱۹، International Data Privacy Law) این مدل را به‌عنوان جایگزینی برای رویکرد «یک اندازه برای همه» در حاکمیت داده پیشنهاد کردند (Delacroix & Lawrence, 2019).",
   "definition": "امین داده نهادی است که به‌صورت امانت‌دار، حقوق دادهٔ افرادی را که به آن پیوسته‌اند مدیریت می‌کند و در تصمیم‌های دسترسی و استفاده، به منافع ذی‌نفعان پایبند است، نه به منافع خریدار داده (Delacroix & Lawrence, 2019).",
   "main_problem": "وقتی رضایت فردی در برابر قدرت پلتفرم‌ها و پیچیدگی استفاده‌های داده ناکارآمد است، چگونه می‌توان قدرت چانه‌زنی افراد را جمعی کرد و در همان حال، حاکمیت داده را دموکراتیک و پاسخ‌گو نگه داشت؟",
   "mechanism": "مدل در چهار سازوکار عمل می‌کند. (۱) جمع‌سازی حقوق: افراد حقوق دادهٔ خود را به نهاد امانی منتقل می‌کنند و آن نهاد به نمایندگی از آنان مذاکره و تصمیم می‌گیرد؛ همین جمع‌سازی، عدم تقارن قدرت میان فرد و شرکت را کاهش می‌دهد. (۲) وظیفهٔ امانت‌داری: امین موظف است در جهت منافع ذی‌نفعان عمل کند و از منافع متعارض دور بماند؛ این تعهد حقوقی، فراتر از قرارداد خدماتی معمول است. (۳) ساخت «از پایین»: دلاکروا و لارنس (۲۰۱۹) تأکید می‌کنند که امین باید از سوی خود افراد و برای هدفی مشخص شکل گیرد، نه به‌عنوان نهاد دولتی متمرکز؛ همین ویژگی، تنوع بافت و اهداف را ممکن می‌کند. (۴) حاکمیت و پاسخ‌گویی: منشور، ترکیب هیئت امین، شفافیت تصمیم و سازوکار خروج اعضا، اجزای کلیدی طراحی‌اند؛ بدون آن‌ها، امین خود می‌تواند به نهاد قدرت بدل شود. ازاین‌رو ادبیات حاکمیت داده میان امین داده، تعاونی داده و مبادلهٔ داده تمایز می‌گذارد. در بستر رسانه، این مدل برای دادهٔ مخاطب، آرشیو خبری و دادهٔ سلامت کاربرد دارد: اتحادیه‌ای از خوانندگان می‌تواند حقوق دادهٔ رفتاری خود را به امینی بسپارد که با ناشران و پلتفرم‌ها بر سر شرایط استفاده مذاکره کند و از فروش داده به کارگزاران جلوگیری نماید.",
   "assumptions": [
     "حقوق داده را می‌توان به‌صورت جمعی و امانی مدیریت کرد.",
     "وظیفهٔ امانت‌داری می‌تواند انگیزهٔ سوءاستفادهٔ نهاد را مهار کند.",
     "افراد حاضرند در نهادهایی با هدف روشن و شفاف مشارکت کنند."
   ],
   "principles": [
     "جمع‌سازی حقوق، عدم تقارن قدرت را کاهش می‌دهد.",
     "امین به منافع ذی‌نفعان وفادار است، نه به خریدار داده.",
     "ساخت از پایین و شفافیت، امین را از بدل‌شدن به قدرت بازمی‌دارد."
   ],
   "critiques": [
     "وضعیت حقوقی داده در بسیاری از نظام‌ها روشن نیست و انطباق مدل امانت با داده، پیچیدگی حقوقی دارد.",
     "خطر تسخیر امین توسط بازیگران پرقدرت یا دولت، مشابه مسئلهٔ تنظیم‌گری‌ساختگی است.",
     "انگیزهٔ پیوستن افراد و مقیاس‌پذیری مالی این نهادها هنوز با شواهد گسترده پشتیبانی نمی‌شود."
   ],
   "applications": [
     "مدیریت جمعی دادهٔ مخاطب در سازمان‌های رسانه‌ای.",
     "حاکمیت دادهٔ آرشیو خبری و پژوهش رسانه‌ای.",
     "دسترسی پژوهشگران به دادهٔ پلتفرم با واسطهٔ نهاد امانی.",
     "طراحی تعاونی داده برای جوامع محلی و رسانه‌های اجتماع‌محور."
   ],
   "evolution": "مفهوم در دههٔ ۲۰۱۰ در پاسخ به ناکارآمدی رضایت شکل گرفت؛ دلاکروا و لارنس (۲۰۱۹) مدل «از پایین» را صورت‌بندی کردند و گزارش‌های سیاستی (O'Hara, 2019) طرح‌های حاکمیتی آن را بسط دادند. در دههٔ ۲۰۲۰، ایدهٔ امین داده در سیاست دادهٔ بریتانیا و بحث دسترسی پژوهشگران به دادهٔ پلتفرم مطرح شد.",
   "key_concepts": ["امین داده (data trust)", "وظیفهٔ امانت‌داری (fiduciary duty)", "جمع‌سازی حقوق داده (pooled data rights)", "تعاونی داده (data cooperative)", "حاکمیت از پایین (bottom-up governance)", "پاسخ‌گویی (accountability)"],
   "studies": ["Delacroix, S., & Lawrence, N. D. (2019). Bottom-up data trusts. International Data Privacy Law, 9(4), 236-252.", "O'Hara, K. (2019). Data Trusts: Ethics, Architecture and Governance. Web Science Institute."],
   "detailed_analysis": "۱. بنیان و منطق نظری\nامین داده از یک تشخیص ساده آغاز می‌شود: فرد به‌تنهایی در برابر پلتفرم قدرت چانه‌زنی ندارد و رضایت فردی، مسئلهٔ جمعی را حل نمی‌کند. راه‌حل پیشنهادی، انتقال منطق حقوق امانت به قلمرو داده است: کسی که در موقعیت امانت‌داری قرار می‌گیرد، نمی‌تواند منافع خود را بر منافع ذی‌نفعان مقدم کند.\n\n۲. تفاوت با مدل‌های دیگر\nامین داده از مبادلهٔ داده (که در آن داده خرید و فروش می‌شود) و از تنظیم‌گری دولتی متمایز است: نه بازار خام است و نه کنترل متمرکز. هدف، ساختن نهادی میانی است که هم قدرت جمع‌آوری کند و هم پاسخ‌گو بماند.\n\n۳. پیوند رسانه‌ای و نقد\nبرای رسانه، امین داده می‌تواند میان مخاطب و ناشر توازن بسازد، اما همان خطر تنظیم‌گری‌ساختگی را دارد: اگر امین به بازیگران بزرگ نزدیک شود، به ابزار مشروعیت‌بخشی به همان نظارت بدل می‌شود که قرار بود مهار کند. طراحی شفافیت و امکان خروج، شرط حیات آن است."
 },
 "MC-298": {
   "summary": "«تنظیم‌گری‌ساختگی» (Regulatory Capture) به وضعیتی اشاره دارد که نهاد تنظیم‌گر به‌جای خدمت به منافع عمومی، منافع گروه تنظیم‌شده را پیش می‌برد. جورج استیگلر در «The Theory of Economic Regulation» (۱۹۷۱، Bell Journal) استدلال کرد که صنایع اغلب تنظیم‌گری را «خریداری» می‌کنند و آن را به نفع خود شکل می‌دهند (Stigler, 1971).",
   "definition": "تنظیم‌گری‌ساختگی فرایندی است که در آن گروه دارای منافع متمرکز، بر تصمیم‌های نهاد تنظیم‌گر اثر می‌گذارد و قواعد را چنان تغییر می‌دهد که رقابت محدود یا هزینهٔ رقبا بالا رود (Stigler, 1971).",
   "main_problem": "چرا نهادهایی که برای حفاظت از منافع عمومی ساخته می‌شوند، به‌تدریج به حامی گروه‌های پرقدرت بدل می‌شوند، و چه سازوکارهایی این تغییر جهت را توضیح می‌دهند؟",
   "mechanism": "تحلیل استیگلر بر چهار سازوکار استوار است. (۱) تقاضای تنظیم‌گری از سوی صنعت: گروه‌های دارای منافع متمرکز، تنظیم‌گری را به‌عنوان ابزاری برای محدودکردن ورود، حمایت قیمتی و تثبیت موقعیت خود طلب می‌کنند. (۲) عرضهٔ تنظیم‌گری از سوی سیاست‌گذار: قانون‌گذار و نهاد تنظیم‌گر به رأی، منابع و حمایت سازمان‌یافته نیاز دارند و گروه‌های متمرکز می‌توانند این‌ها را بهتر از عموم پراکنده تأمین کنند. (۳) عدم تقارن کنش جمعی: هزینهٔ سازمان‌دهی برای صنعت کوچک و منافعش بزرگ است، در حالی که هزینهٔ فردی برای مصرف‌کننده ناچیز و انگیزهٔ سازمان‌دهی اندک است؛ همین عدم تقارن، نتیجه را تعیین می‌کند. (۴) پیامدها: موانع ورود، قیمت‌های بالاتر، کاهش نوآوری و انتقال رانت به گروه تنظیم‌شده. پلزمن (۱۹۷۶) مدل را تعدیل کرد: تنظیم‌گر میان گروه‌های ذی‌نفع تعادل برقرار می‌کند و نتیجه همیشه سلطهٔ کامل صنعت نیست؛ ازاین‌رو پژوهش‌های بعدی «ساختگی» را طیفی از نفوذ می‌بینند، نه وضعیتی دوتایی. در بستر رسانه، این چارچوب برای تحلیل قواعد مالکیت رسانه، تنظیم پلتفرم، بودجهٔ رسانهٔ عمومی و نهادهای حفاظت از داده به‌کار می‌رود: وقتی شرکت‌های بزرگ در مشورت‌های قانون‌گذاری حضور دائمی دارند و منافع پراکندهٔ کاربران حضور سازمان‌یافته ندارد، خطر ساختگی جدی است.",
   "assumptions": [
     "گروه‌های دارای منافع متمرکز، توان سازمان‌دهی بیشتری از منافع پراکنده دارند.",
     "سیاست‌گذاران و تنظیم‌گران به منابع، رأی و گزینه‌های شغلی آینده حساس‌اند.",
     "تنظیم‌گری را می‌توان به‌عنوان کالایی با عرضه و تقاضا تحلیل کرد."
   ],
   "principles": [
     "تنظیم‌گری اغلب به‌درخواست صنعت و به نفع آن شکل می‌گیرد.",
     "عدم تقارن کنش جمعی، منافع پراکنده را ناتوان می‌کند.",
     "ساختگی طیف است، نه وضعیت صفر و یک."
   ],
   "critiques": [
     "مدل با فرض انگیزه‌های صرفاً اقتصادی، استقلال نهادی و تعهد حرفه‌ای تنظیم‌گران را کم‌رنگ می‌کند.",
     "شواهد تجربی مختلط است و بسیاری از نهادها در برابر نفوذ مقاومت می‌کنند.",
     "تمرکز بر تجربهٔ آمریکا، تعمیم آن به نظام‌های حقوقی و سیاسی دیگر را محدود می‌کند."
   ],
   "applications": [
     "تحلیل قواعد مالکیت و ادغام در بازار رسانه.",
     "پژوهش دربارهٔ نفوذ شرکت‌های فناوری در قانون‌گذاری داده و رقابت.",
     "ارزیابی استقلال نهادهای تنظیم رسانه و پخش عمومی.",
     "طراحی سازوکارهای شفافیت و مشارکت عمومی در تنظیم‌گری."
   ],
   "evolution": "استیگلر (۱۹۷۱) چارچوب اقتصادی ساختگی را تثبیت کرد؛ پلزمن (۱۹۷۶) مدل تعادلی‌تری عرضه کرد و در دههٔ ۲۰۱۰ پژوهش‌های نهادی، مفهوم «ساختگی فرهنگی» و سازوکارهای پیشگیری را افزودند.",
   "key_concepts": ["تنظیم‌گری‌ساختگی (regulatory capture)", "منافع متمرکز و پراکنده (concentrated vs diffuse interests)", "کنش جمعی (collective action)", "درِ گردان (revolving door)", "رانت تنظیم‌گری (regulatory rent)", "استقلال نهادی (agency independence)"],
   "studies": ["Stigler, G. J. (1971). The theory of economic regulation. Bell Journal of Economics and Management Science, 2(1), 3-21.", "Peltzman, S. (1976). Toward a more general theory of regulation. Journal of Law and Economics, 19(2), 211-240."],
   "detailed_analysis": "۱. بنیان و منطق نظری\nنظریهٔ استیگلر در واکنش به «نظریهٔ منافع عمومی» تنظیم‌گری شکل گرفت که نهاد تنظیم‌گر را اصلاح‌کنندهٔ شکست بازار می‌دانست. استدلال او این بود که نهاد، خود بازیگری با انگیزه‌های سیاسی است و می‌تواند به ابزار انتقال رانت بدل شود.\n\n۲. سازوکار نفوذ\nنفوذ از راه‌های گوناگون عمل می‌کند: مشورت در تدوین قواعد، تأمین اطلاعات تخصصی، حمایت انتخاباتی، استخدام کارشناسان صنعت در نهاد و خروج مقام‌های نهاد به صنعت. همین تنوع، سنجش تجربی ساختگی را دشوار اما ممکن می‌کند.\n\n۳. پیوند رسانه‌ای و نقد\nرسانه هم موضوع تنظیم است و هم ابزار نظارت بر آن. وقتی قواعد مالکیت یا محتوا با مشورت نزدیک با بازیگران بزرگ تدوین می‌شود، ساختگی رخ می‌دهد. نقد اصلی این است که چارچوب اقتصادی، ممکن است تعهد عمومی و مقاومت نهادی را نادیده بگیرد؛ ساختگی را باید با شواهد رفتاری و نهادی سنجید، نه فقط با فرض."
 },
 "MC-302": {
   "summary": "«نظریهٔ ریاضی اطلاعات» (Mathematical Theory of Information) چارچوبی است که اطلاعات را به‌صورت کمّی و مستقل از معنای پیام تعریف می‌کند: اطلاعات، کاهش عدم قطعیت است و با آنتروپی سنجیده می‌شود. کلود شانون در «A Mathematical Theory of Communication» (۱۹۴۸، Bell System Technical Journal) این نظریه را بنیان گذاشت و ظرفیت کانال و رمزگذاری کارآمد را صورتبندی کرد (Shannon, 1948).",
   "definition": "اطلاعات در این نظریه، میزان کاهش عدم قطعیت گیرنده دربارهٔ پیام است؛ آنتروپی، میانگین عدم قطعیت منبع را اندازه می‌گیرد و ظرفیت کانال، بیشترین نرخی است که می‌توان با خطای ناچیز بر آن انتقال داد (Shannon, 1948).",
   "main_problem": "چگونه می‌توان انتقال پیام را، مستقل از محتوا و معنا، به‌صورت ریاضی تحلیل کرد: چه اندازه اطلاعات در یک پیام هست، یک کانال چه ظرفیتی دارد، و با وجود نویز تا چه حد می‌توان انتقال مطمئن را تضمین کرد؟",
   "mechanism": "نظریه بر چهار سازوکار بنا شده است. (۱) مدل ارتباطی: منبع، فرستنده، کانال، نویز، گیرنده و مقصد؛ پیام به نشانه تبدیل و از کانال عبور می‌کند و در مقصد بازسازی می‌شود. (۲) آنتروپی به‌عنوان سنجهٔ عدم قطعیت: اگر رویدادها با احتمالات مختلف رخ دهند، آنتروپی H برابر است با مجموع منفی احتمال هر رویداد ضرب‌در لگاریتم احتمال آن؛ بیشترین آنتروپی زمانی است که همهٔ گزینه‌ها هم‌احتمال باشند. واحد آن «بیت» است و همین سنجه، معنای شهودی «اطلاعات بیشتر = غافلگیری بیشتر» را ریاضی می‌کند. (۳) دو قضیهٔ بنیادی: قضیهٔ رمزگذاری منبع نشان می‌دهد پیام را می‌توان تا نزدیک آنتروپی فشرده کرد و قضیهٔ رمزگذاری کانال نشان می‌دهد تا زیر ظرفیت کانال، می‌توان با احتمال خطای دلخواه کوچک انتقال مطمئن داشت؛ افزونگی، ابزار مقابله با نویز است. (۴) استقلال از معنا: شانون (۱۹۴۸) تصریح می‌کند که «جنبه‌های معنایی ارتباط به مسئلهٔ مهندسی مربوط نیست»؛ همین محدودیت، نقطهٔ قوت و ضعف نظریه است. شانون و ویور (۱۹۴۹) سه سطح تحلیلی را از هم جدا کردند: سطح فنی (دقت انتقال نشانه)، سطح معنایی (دقت انتقال معنا) و سطح اثربخشی (اثر بر رفتار)؛ نظریهٔ ریاضی، سطح نخست را حل می‌کند و دو سطح دیگر را به علوم دیگر وامی‌گذارد. در بستر رسانه، این چارچوب زیربنای فشرده‌سازی ویدئو و صدا، تصحیح خطا در پخش دیجیتال، برنامه‌ریزی پهنای باند و سنجش کیفیت سیگنال است.",
   "assumptions": [
     "اطلاعات را می‌توان مستقل از معنای پیام و به‌صورت احتمالاتی سنجید.",
     "منبع و کانال را می‌توان با مدل آماری توصیف کرد.",
     "نویز، پدیده‌ای آماری است که با افزونگی و رمزگذاری قابل مهار است."
   ],
   "principles": [
     "اطلاعات، کاهش عدم قطعیت است و با آنتروپی سنجیده می‌شود.",
     "قضیهٔ رمزگذاری منبع و کانال، مرزهای فشرده‌سازی و انتقال مطمئن را تعیین می‌کنند.",
     "نظریه، سطح فنی را حل می‌کند و از معنا و اثر مستقل است."
   ],
   "critiques": [
     "نظریه، نظریهٔ انتقال نشانه است، نه نظریهٔ معنا یا ارتباط انسانی؛ تعمیم آن به ارتباطات اجتماعی نیازمند ترجمه است.",
     "مدل انتقالی، زمینهٔ اجتماعی، قدرت و تفسیر را کنار می‌گذارد و به همین دلیل برای تحلیل محتوای رسانه‌ای ناکافی است.",
     "کاربرد عامه‌پسند، «اطلاعات» را با «دانش» یکی می‌گیرد، در حالی که شانون خود این تفاوت را برجسته کرده بود."
   ],
   "applications": [
     "فشرده‌سازی ویدئو و صدا در پخش و استریم.",
     "تصحیح خطا و تضمین کیفیت در پخش دیجیتال.",
     "برنامه‌ریزی ظرفیت شبکه و پهنای باند.",
     "سنجش کیفیت سیگنال و طراحی سیستم‌های مخابراتی."
   ],
   "evolution": "شانون (۱۹۴۸) نظریه را در دو بخش منتشر کرد و شانون و ویور (۱۹۴۹) آن را با سطوح معنا و اثربخشی به خوانندگان گسترده‌تر معرفی کردند. در نیمهٔ دوم قرن بیستم، نظریه به بنیان مخابرات دیجیتال، فشرده‌سازی و رمزنگاری بدل شد.",
   "key_concepts": ["آنتروپی (entropy)", "بیت (bit)", "ظرفیت کانال (channel capacity)", "افزونگی (redundancy)", "نویز (noise)", "رمزگذاری منبع و کانال (source/channel coding)", "سطح فنی/معنایی/اثربخشی (technical/semantic/effectiveness)"],
   "studies": ["Shannon, C. E. (1948). A mathematical theory of communication. Bell System Technical Journal, 27(3), 379-423; 27(4), 623-656.", "Shannon, C. E., & Weaver, W. (1949). The Mathematical Theory of Communication. University of Illinois Press."],
   "detailed_analysis": "۱. بنیان و منطق نظری\nمسئلهٔ شانون مهندسی بود: چگونه می‌توان با وجود نویز، پیام را مطمئن منتقل کرد و چه اندازه اطلاعات از یک کانال می‌گذرد. پاسخ او، ارتباط را از مسئلهٔ معنا جدا کرد و آن را به مسئلهٔ احتمال و کدگذاری تبدیل کرد؛ همین جداکردن، امکان تحلیل ریاضی را فراهم ساخت.\n\n۲. معنای انقلاب مفهومی\nپیش از شانون، «اطلاعات» مفهومی مبهم و وابسته به محتوا بود. او نشان داد که اطلاعات، کاهش عدم قطعیت است و بنابراین یک پیام تکراری، اطلاعات کمی دارد، حتی اگر مهم به نظر برسد. این چرخش، بنیان اقتصاد اطلاعات و مخابرات دیجیتال شد.\n\n۳. پیوند رسانه‌ای و محدودیت\nنظریه، زیرساخت فنی رسانهٔ دیجیتال را ممکن کرد، اما برای تحلیل معنا، قدرت و تفسیر کافی نیست. تفکیک سه سطح شانون و ویور یادآوری می‌کند که حل مسئلهٔ فنی، به‌خودی‌خود مسئلهٔ ارتباط انسانی را حل نمی‌کند؛ این همان مرزی است که مدل‌های انتقالی رسانه از آن غفلت می‌کنند."
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
    codes = ["MC-294", "MC-297", "MC-298", "MC-302"]
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
    print("BATCH60 THEORY DONE")

if __name__ == "__main__":
    main()
