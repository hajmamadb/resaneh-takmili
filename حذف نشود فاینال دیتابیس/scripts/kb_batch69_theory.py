# -*- coding: utf-8 -*-
"""Batch 69: MC-365 (data journalism), MC-366 (participatory journalism),
MC-369 (engineering consent), MC-370 (propaganda & opinion manipulation).
All four carried garbled boilerplate in critique/example -> rewritten.
MC-370's core_logic actually describes Herman & Chomsky's five filters while crediting
Bernays; content documents Bernays accurately and attributes the filter model correctly."""
import pymysql, json

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch69-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch69_theory.json"

S = {
 "MC-365": [
   dict(kind="BOOK", title_en="The Data Journalism Handbook",
        title_fa="راهنمای روزنامه‌نگاری داده‌محور",
        authors="Gray, J., Bounegru, L., & Chambers, L. (Eds.)", year=2012,
        publisher="O'Reilly Media", doi=None,
        url="https://datajournalismhandbook.org/uploads/first_book/DataJournalismHandbook-2012.pdf",
        language="en", isbn="978-1449330064",
        citation="Gray, J., Bounegru, L., & Chambers, L. (Eds.). (2012). The data journalism handbook. O'Reilly Media.",
        locator="whole work", locator_type="work",
        supports="definition / workflow / tools", verified=True),
   dict(kind="JOURNAL_ARTICLE", title_en="Clarifying Journalism's Quantitative Turn",
        title_fa="روشن‌سازی چرخش کمّی روزنامه‌نگاری",
        authors="Coddington, M.", year=2015,
        publisher="Digital Journalism, 3(3), 331-348",
        doi=None, url=None, language="en", isbn=None,
        citation="Coddington, M. (2015). Clarifying journalism's quantitative turn. Digital Journalism, 3(3), 331-348.",
        locator="pp. 331-348", locator_type="page_range",
        supports="critique / typology", verified=False),
 ],
 "MC-366": [
   dict(kind="BOOK", title_en="Participatory Journalism: Guarding Open Gates at Online Newspapers",
        title_fa="روزنامه‌نگاری مشارکتی: نگهبانی از دروازه‌های باز در روزنامه‌های آنلاین",
        authors="Singer, J. B., Domingo, D., Heinonen, A., Hermida, A., Paulussen, S., et al.", year=2011,
        publisher="Wiley-Blackwell", doi="10.1002/9781444340747",
        url="https://www.wiley.com/en-au/Participatory+Journalism:+Guarding+Open+Gates+at+Online+Newspapers-p-9781444332261",
        language="en", isbn="978-1-4443-3227-8",
        citation="Singer, J. B., Domingo, D., Heinonen, A., Hermida, A., Paulussen, S., et al. (2011). Participatory journalism: Guarding open gates at online newspapers. Wiley-Blackwell. https://doi.org/10.1002/9781444340747",
        locator="whole work", locator_type="work",
        supports="definition / gatekeeping / cross-national evidence", verified=True),
   dict(kind="BOOK", title_en="We the Media: Grassroots Journalism by the People, for the People",
        title_fa="ما رسانه‌ایم: روزنامه‌نگاری مردمی از سوی مردم برای مردم",
        authors="Gillmor, D.", year=2004,
        publisher="O'Reilly Media", doi=None, url=None, language="en", isbn=None,
        citation="Gillmor, D. (2004). We the media: Grassroots journalism by the people, for the people. O'Reilly Media.",
        locator="whole work", locator_type="work",
        supports="evolution / grassroots journalism", verified=False),
 ],
 "MC-369": [
   dict(kind="JOURNAL_ARTICLE", title_en="The Engineering of Consent",
        title_fa="مهندسی رضایت",
        authors="Bernays, E. L.", year=1947,
        publisher="The ANNALS of the American Academy of Political and Social Science, 250(1), 113-120",
        doi="10.1177/000271624725000116", url="https://journals.sagepub.com/doi/10.1177/000271624725000116",
        language="en", isbn=None,
        citation="Bernays, E. L. (1947). The engineering of consent. The ANNALS of the American Academy of Political and Social Science, 250(1), 113-120. https://doi.org/10.1177/000271624725000116",
        locator="pp. 113-120", locator_type="page_range",
        supports="definition / mechanism / ethics", verified=True),
   dict(kind="BOOK", title_en="Propaganda", title_fa="پروپاگاندا",
        authors="Bernays, E. L.", year=1928,
        publisher="Horace Liveright", doi=None, url=None, language="en", isbn=None,
        citation="Bernays, E. L. (1928). Propaganda. Horace Liveright.",
        locator="whole work", locator_type="work",
        supports="origin / invisible government", verified=False),
 ],
 "MC-370": [
   dict(kind="BOOK", title_en="Propaganda", title_fa="پروپاگاندا",
        authors="Bernays, E. L.", year=1928,
        publisher="Horace Liveright", doi=None, url=None, language="en", isbn=None,
        citation="Bernays, E. L. (1928). Propaganda. Horace Liveright.",
        locator="whole work", locator_type="work",
        supports="definition / psychological mechanism / origin", verified=True),
   dict(kind="BOOK", title_en="Manufacturing Consent: The Political Economy of the Mass Media",
        title_fa="ساخت رضایت: اقتصاد سیاسی رسانه‌های جمعی",
        authors="Herman, E. S., & Chomsky, N.", year=1988,
        publisher="Pantheon Books", doi=None, url="https://chomsky.info/consent01/",
        language="en", isbn=None,
        citation="Herman, E. S., & Chomsky, N. (1988). Manufacturing consent: The political economy of the mass media. Pantheon Books.",
        locator="A Propaganda Model", locator_type="CHAPTER",
        supports="evolution / five filters", verified=False),
 ],
}

VOID = "در بستر رسانه، "
ENRICH = {
 "MC-365": {
  "summary": "(گری، بوگنرو و چمبرز، ۲۰۱۲؛ کادینگتون، ۲۰۱۵) روزنامه‌نگاری داده‌محور شاخه‌ای از روزنامه‌نگاری است که گزارش را بر پایهٔ جمع‌آوری، پالایش، تحلیل آماری و بصری‌سازی مجموعه‌داده‌ها بنا می‌کند. در این الگو، داستان خبری نه از نقل‌قول یک منبع، بلکه از الگوی نهفته در داده بیرون می‌آید و روزنامه‌نگار باید مهارت تحلیل و نمایش داده را نیز داشته باشد.",
  "definition": "روزنامه‌نگاری داده‌محور، فرایندی است شامل دسترسی به داده، پالایش آن، تحلیل برای کشف الگو و روایت‌سازی بصری، به‌گونه‌ای که گزاره‌های خبری با شواهد عددی قابل بازتولید پشتیبانی شوند.",
  "main_problem": "چگونه می‌توان از داده‌های فراوانِ عمومی و سازمانی، روایتی خبری ساخت که هم دقیق باشد و هم برای مخاطب عام قابل فهم؟ این پرسش، سه مسئلهٔ به‌هم‌پیوستهٔ کیفیت داده، مهارت تحلیلی روزنامه‌نگار و شفافیت روش را پیش می‌آورد.",
  "mechanism": "\n".join([
   "(۱) زنجیرهٔ داده: از منبع داده (سازمان، درخواست آزادی اطلاعات، دادهٔ عمومی) به پالایش، تحلیل، تجسم و انتشار؛ هر حلقه، تصمیم روش‌شناختی است که باید مستند شود.",
   "(۲) تحلیل به‌عنوان گزارش: کشف الگو، همبستگی و روند در داده، جانشین نقل‌قول می‌شود؛ بنابراین اعتبار گزارش به اعتبار روش آماری آن وابسته است.",
   "(۳) تجسم به‌عنوان استدلال: نمودار و نقشه فقط تزیین نیست؛ انتخاب مقیاس، رنگ و بازهٔ زمانی، خود ادعایی دربارهٔ اهمیت و روند است.",
   "(۴) شفافیت روش: بهترین نمونه‌ها دادهٔ خام و روش تحلیل را منتشر می‌کنند؛ بازتولیدپذیری، معیار تازهٔ صحت خبری است.",
   "(۵) همکاری میان‌رشته‌ای: روزنامه‌نگار با تحلیل‌گر داده و طراح هم‌نشسته کار می‌کند و مرز میان نویسنده و متخصص فنی جابه‌جا می‌شود.",
   VOID + "گزارش‌های حساب‌رسی مبتنی بر داده — از بودجهٔ شهرداری تا آمار مرگ‌ومیر — نمونه‌های عینی‌اند: همان عدد که در گزارش کلامی نامفهوم است، با تجسم و مقایسه به داستانی قابل پیگیری بدل می‌شود.",
  ]),
  "assumptions": [
   "داده، شاهد معتبری برای گزاره‌های خبری است، به شرط مستندبودن منبع و روش.",
   "مخاطب عام می‌تواند با تجسم مناسب، الگوهای پیچیده را درک کند.",
   "شفافیت روش، اعتماد مخاطب را افزایش می‌دهد.",
  ],
  "principles": [
   "هر گزارش داده باید منبع، روش پالایش و محدودیت‌های خود را بازگو کند.",
   "تجسم باید متناسب با پرسش تحلیلی انتخاب شود، نه با جذابیت بصری.",
   "داده پیش از تحلیل، نیازمند بازرسی برای خطا و سوگیری است.",
  ],
  "critiques": [
   "همبستگی به‌جای علیت: تجسم الگوی همبستگی می‌تواند به استنتاج علّی بی‌پشتوانه منجر شود.",
   "سوگیری داده: داده‌های عمومی معمولاً نامتقارن‌اند؛ گروه‌هایی که ثبت نمی‌شوند، در گزارش دیده نمی‌شوند.",
   "فقدان مهارت روش‌شناختی: روزنامه‌نگارِ بی‌آموزش آماری، خطای تحلیل را در قالب خبر منتشر می‌کند.",
   "فاصله از روایت: تکیهٔ بیش‌ازحد بر داده، تجربهٔ انسانی و زمینهٔ رخداد را کم‌رنگ می‌کند.",
  ],
  "applications": [
   "گزارش‌های نظارتی: بودجه، قراردادها، عملکرد نهادها و فساد سیستماتیک.",
   "تحلیل انتخابات و نظرسنجی: کیفیت نمونه، سوگیری و تفسیر نتایج.",
   "جست‌وجوی خبری قابل بازتولید: انتشار دادهٔ خام به‌همراه روش برای بازرسی عمومی.",
   "پایش بحران: جمع‌آوری و تجسم سریع داده‌های محلی در سانحه و بیماری.",
  ],
  "evolution": "از گزارش‌های حساب‌رسی دههٔ ۱۹۹۰ به «راهنمای روزنامه‌نگاری داده» (۲۰۱۲) و سپس به تثبیت آن به‌عنوان مهارت حرفه‌ای در اتاق‌های خبر و امروز به تحلیل دادهٔ بزرگ و تعامل با مدل‌های زبانی برای پردازش داده.",
  "key_concepts": ["دادهٔ باز (Open Data)", "پالایش داده (Data Cleaning)", "تحلیل اکتشافی (Exploratory Analysis)", "تجسم داده (Data Visualization)", "بازتولیدپذیری (Reproducibility)", "دروازه‌بانی داده (Data Gatekeeping)"],
  "studies": [
   "Coddington, M. (2015). Clarifying journalism's quantitative turn. Digital Journalism, 3(3), 331-348.",
   "Gray, J., Bounegru, L., & Chambers, L. (Eds.). (2012). The data journalism handbook. O'Reilly Media.",
  ],
  "detailed_analysis": "\n".join([
   "۱. بنیان و منطق نظری: روزنامه‌نگاری داده‌محور در تقاطع سه سنت قرار دارد: روزنامه‌نگاری تحقیقی، آمار عمومی و طراحی اطلاعات؛ نقطهٔ پیوند آن‌ها، ایدهٔ «شاهد داده» به‌جای شاهد نقل‌قولی است.",
   "۲. روش و اعتبار: اعتبار گزارش داده به سه چیز وابسته است: کیفیت منبع، درستی روش و شفافیت مستندات. غفلت از هر سه، گزارش را از تحلیل به تفسیر ذهنی عدد بدل می‌کند.",
   "۳. افق امروز: با فراگیری دادهٔ کلان و مدل‌های زبانی، پرسش‌های تازه‌ای مطرح شده است: چه کسی داده را پردازش می‌کند، خروجی مدل چه سوگیری‌هایی دارد و مخاطب چگونه می‌تواند تحلیل را بازرسی کند.",
  ]),
  "critique_text": "\n".join([
   "۱. همبستگی به‌جای علیت: تجسم الگوی همبستگی می‌تواند به استنتاج علّی بی‌پشتوانه منجر شود.",
   "۲. سوگیری داده: داده‌های عمومی معمولاً نامتقارن‌اند؛ گروه‌هایی که ثبت نمی‌شوند، در گزارش دیده نمی‌شوند.",
   "۳. فقدان مهارت روش‌شناختی: روزنامه‌نگارِ بی‌آموزش آماری، خطای تحلیل را در قالب خبر منتشر می‌کند.",
   "۴. فاصله از روایت: تکیهٔ بیش‌ازحد بر داده، تجربهٔ انسانی و زمینهٔ رخداد را کم‌رنگ می‌کند.",
  ]),
  "example_text": "\n".join([
   "گزارشی دربارهٔ افزایش اجاره‌بها وقتی با دادهٔ ثبت قراردادها و نقشهٔ محله‌ها همراه می‌شود، از گلایهٔ عمومی به الگویی قابل مکان‌یابی تبدیل می‌شود؛ مخاطب می‌بیند کجا و برای چه کسی افزایش شدیدتر بوده است.",
   "در یک کمپین انتخاباتی، نمودار نظرسنجی بدون ذکر بازهٔ خطا، تفاوت دو درصدی را «صعود» می‌نامد؛ همان داده با بازهٔ اطمینان، «ثبات» خوانده می‌شود — نشانهٔ آنکه تجسم، خود ادعای تحلیلی است.",
   "یک روزنامهٔ محلی دادهٔ خام بودجه را منتشر می‌کند تا خوانندگان خودشان بازرسی کنند؛ همین شفافیت، نمونهٔ عملی معیار بازتولیدپذیری در روزنامه‌نگاری داده است.",
  ]),
 },
 "MC-366": {
  "summary": "(سینگر و همکاران، ۲۰۱۱؛ گیلمور، ۲۰۰۴) روزنامه‌نگاری مشارکتی الگویی است که در آن مخاطبان در تولید خبر — از ارسال عکس و ویدئو تا نگارش گزارش و تدقیق اطلاعات — مشارکت مستقیم دارند. در این الگو، دروازه‌بانی خبر نه حذف می‌شود و نه دست‌نخورده می‌ماند، بلکه به دروازه‌بانی «باز» میان اتاق خبر و مخاطبان بدل می‌شود.",
  "definition": "روزنامه‌نگاری مشارکتی، مجموعه‌ای از رویه‌هاست که در آن رسانهٔ حرفه‌ای، مشارکت مخاطب را در مراحل گردآوری، تولید یا ارزیابی خبر سازمان می‌دهد، در حالی که مسئولیت ویرایش و اعتبارسنجی نهایی نزد نهاد خبری می‌ماند.",
  "main_problem": "اگر هر شهروندی می‌تواند خبر بسازد و منتشر کند، نقش روزنامه‌نگار حرفه‌ای چه می‌شود؟ پرسش اصلی این نظریه، مدیریت تنش میان گشودگی مشارکت و حفظ اعتبار و مسئولیت حرفه‌ای است.",
  "mechanism": "\n".join([
   "(۱) دروازه‌بانی باز: خبرنگار همچنان تصمیم می‌گیرد چه چیزی منتشر شود، اما منابع تصمیم را از خودرویداد و شهروند هم می‌گیرد؛ دروازه باز می‌شود، ولی حذف نمی‌شود.",
   "(۲) تقسیم کار مشارکتی: مخاطب عمدتاً در گردآوری (عکس، شهادت، دادهٔ محلی) و در ارزیابی پس از انتشار (تصحیح، تکذیب) مشارکت می‌کند، نه در تصمیم نهایی انتشار.",
   "(۳) مدیریت اعتبار: رسانه با راستی‌آزمایی، برچسب‌گذاری منبع و شفاف‌سازی سهم مشارکت، اعتبار خود را حفظ می‌کند؛ بی‌توجهی به این سازوکار، اعتماد را از دست می‌دهد.",
   "(۴) تغییر نقش خبرنگار: از «تولیدکنندهٔ انحصاری محتوا» به «تسهیل‌گر، راستی‌آزما و ویراستار مشارکت»؛ مهارت‌های مدیریت جامعه و اعتبارسنجی پررنگ می‌شود.",
   "(۵) انگیزهٔ مخاطب: مشارکت با احساس تعلق، دیده‌شدن و نفوذ در روایت محلی تقویت می‌شود؛ ازاین‌رو طراحی تجربهٔ مشارکت، بخشی از کار حرفه‌ای است.",
   VOID + "در سانحه، رسانه ابتدا از عکس و ویدئوی شاهدان استفاده می‌کند و سپس آن‌ها را راستی‌آزمایی و با گزارش خبرنگار تکمیل می‌کند؛ همین توالی، نسخهٔ عملی دروازه‌بانی باز است.",
  ]),
  "assumptions": [
   "مخاطب انگیزه و توان مشارکت در تولید خبر را دارد.",
   "رسانهٔ حرفه‌ای همچنان مرجع اعتبارسنجی و مسئولیت حقوقی است.",
   "مشارکت، در صورت سازمان‌یافتگی، کیفیت و گسترهٔ پوشش را افزایش می‌دهد.",
  ],
  "principles": [
   "دروازه‌بانی حذف نمی‌شود، باز و شفاف می‌شود.",
   "سهم مشارکت مخاطب باید در متن خبر مشخص باشد.",
   "راستی‌آزمایی پیش از انتشار، همچنان وظیفهٔ نهاد خبری است.",
  ],
  "critiques": [
   "مشارکت نابرابر: کسانی که وقت، مهارت و فناوری دارند بیشتر مشارکت می‌کنند؛ صدای گروه‌های کم‌برخوردار کمتر شنیده می‌شود.",
   "خطر misinformation: محتوای مشارکتی بدون راستی‌آزمایی، می‌تواند به سرعت در رسانه و شبکه‌ها منتشر شود.",
   "کار بدون مزد: استفادهٔ رسانه از محتوای مخاطب، اغلب بدون پرداخت دستمزد است و مرز بهره‌کشی از مشارکت را مبهم می‌کند.",
   "فشار بر منابع: مدیریت مشارکت، بار راستی‌آزمایی و ویرایش را بر اتاق خبر افزایش می‌دهد.",
  ],
  "applications": [
   "پوشش سانحه و بحران: گردآوری سریع شاهدان و راستی‌آزمایی سازمان‌یافته.",
   "روزنامه‌نگاری محلی: شبکهٔ خبرنگاران شهروند برای موضوعات کم‌پوشش.",
   "راستی‌آزمایی مشارکتی: استفاده از دانش مخاطبان متخصص برای بررسی ادعاها.",
   "طراحی پلتفرم خبری: فرم‌های ارسال، برچسب سهم مشارکت و سازوکار بازخورد و تصحیح.",
  ],
  "evolution": "از ایدهٔ «ما رسانه‌ایم» گیلمور (۲۰۰۴) به پژوهش تطبیقی سینگر و همکاران (۲۰۱۱) در روزنامه‌های آنلاین اروپا و آمریکا، و سپس به ادغام مشارکت در استراتژی پلتفرم‌های خبری و مدل‌های عضویت.",
  "key_concepts": ["دروازه‌بانی باز (Open Gatekeeping)", "خبرنگار شهروند (Citizen Journalist)", "راستی‌آزمایی مشارکتی (Collaborative Verification)", "اتاق خبر مشارکتی (Participatory Newsroom)", "شفافیت منبع (Source Transparency)", "اعتماد خبری (News Trust)"],
  "studies": [
   "Gillmor, D. (2004). We the media: Grassroots journalism by the people, for the people. O'Reilly Media.",
   "Singer, J. B., et al. (2011). Participatory journalism: Guarding open gates at online newspapers. Wiley-Blackwell.",
  ],
  "detailed_analysis": "\n".join([
   "۱. بنیان و منطق نظری: روزنامه‌نگاری مشارکتی وارث دو جریان است: نقد انحصار دروازه‌بانی حرفه‌ای و ظهور ابزارهای انتشار همگانی؛ نقطهٔ تعادل آن، نگه‌داشتن استاندارد اعتبار همراه با گشودگی است.",
   "۲. شواهد تطبیقی: پژوهش سینگر و همکاران در چند کشور نشان داد نگرش حرفه‌ای‌ها به مشارکت مخاطب متفاوت است و بیشتر رسانه‌ها مشارکت را در حاشیهٔ فرایند (گردآوری و پس از انتشار) پذیرفته‌اند، نه در هستهٔ تصمیم.",
   "۳. افق امروز: پلتفرم‌های خبری، مشارکت را به داده و تعامل تبدیل کرده‌اند؛ چالش تازه این است که مشارکت واقعی از «تعامل سنجیده‌شده» تفکیک شود و منافع اقتصادی آن به مشارکت‌کنندگان بازگردد.",
  ]),
  "critique_text": "\n".join([
   "۱. مشارکت نابرابر: کسانی که وقت، مهارت و فناوری دارند بیشتر مشارکت می‌کنند؛ صدای گروه‌های کم‌برخوردار کمتر شنیده می‌شود.",
   "۲. خطر اطلاعات نادرست: محتوای مشارکتی بدون راستی‌آزمایی، می‌تواند به سرعت در رسانه و شبکه‌ها منتشر شود.",
   "۳. کار بدون مزد: استفادهٔ رسانه از محتوای مخاطب، اغلب بدون پرداخت دستمزد است و مرز بهره‌کشی از مشارکت را مبهم می‌کند.",
   "۴. فشار بر منابع: مدیریت مشارکت، بار راستی‌آزمایی و ویرایش را بر اتاق خبر افزایش می‌دهد.",
  ]),
  "example_text": "\n".join([
   "در یک سیل شهری، رسانهٔ محلی ابتدا ویدئوی شهروندان را دریافت می‌کند، سپس موقعیت و زمان هر ویدئو را راستی‌آزمایی می‌کند و آن را با گزارش خبرنگار ترکیب می‌کند — دروازه‌بانی باز در عمل.",
   "یک روزنامهٔ محلی از خوانندگان می‌خواهد وضعیت خیابان‌های محله را گزارش دهند و در ازای آن، نقشهٔ روزانهٔ خدمات شهری را منتشر می‌کند؛ مشارکت با منفعت متقابل، انگیزهٔ مخاطب را پایدار می‌کند.",
   "در یک گزارش تحقیقی، رسانه از متخصصان مخاطب برای بررسی دادهٔ فنی کمک می‌گیرد و سهم آن‌ها را در پایان گزارش ذکر می‌کند؛ نمونهٔ راستی‌آزمایی مشارکتی با شفافیت منبع.",
  ]),
 },
 "MC-369": {
  "summary": "(برنیز، ۱۹۴۷؛ ۱۹۲۸) «مهندسی رضایت» نام رویکردی است که برنیز آن را در ۱۹۴۷ صورت‌بندی کرد: اگر جامعهٔ مدرن دموکراتیک است، تصمیم‌های عمومی را نمی‌توان به تصادف سپرد؛ بلکه باید با ابزارهای روان‌شناسی و جامعه‌شناسی، تمایلات و آرای ناخودآگاه عمومی را به‌گونه‌ای ساخت که رضایت آگاهانه نسبت به اهداف سازمان یا دولت شکل بگیرد.",
  "definition": "مهندسی رضایت، فرایند برنامه‌ریزی‌شدهٔ ساخت نگرش و رفتار عمومی از طریق تحلیل انگیزه‌های ناخودآگاه، طراحی پیام و استفادهٔ هدفمند از رسانه است، به‌گونه‌ای که مخاطب تصمیم را از آنِ خود بداند.",
  "main_problem": "در جامعهٔ توده‌ای، چگونه می‌توان میان ارادهٔ فردی و تصمیم جمعی هماهنگی ساخت؟ برنیز پرسش را با فرضی هنجاری پاسخ می‌دهد: رهبران دموکراتیک باید افکار عمومی را به سوی اهداف «سازنده» هدایت کنند؛ همان فرضی که بنیاد نقد اخلاقی او شد.",
  "mechanism": "\n".join([
   "(۱) تحلیل انگیزهٔ ناخودآگاه: برنیز با تکیه بر روان‌کاوی، تصمیم خرید و رأی را نه انتخاب عقلانی، بلکه محصول سائق‌ها و تصاویر ناخودآگاه می‌داند.",
   "(۲) طراحی گروه مرجع و نماد: پیوند دادن محصول یا سیاست به نمادهای اعتبار، منزلت و تعلق، سازوکار اصلی تغییر نگرش است.",
   "(۳) مشاورهٔ پنهان: مهندس رضایت به‌عنوان مشاور سازمان، در پس‌زمینه تصمیم می‌گیرد و در جلوی صحنه، منبع رسمی ظاهر می‌شود.",
   "(۴) اقناع دوطرفه‌نما: پیام باید هم‌زمان منفعت سازمان و خیر عمومی را روایت کند؛ همین روایت، پذیرش اخلاقی را برای مخاطب فراهم می‌کند.",
   "(۵) فرض «حکومت نامرئی»: برنیز حکومت را نه فقط نهادهای رسمی، بلکه شبکهٔ نامرئی مشاوران و متخصصان افکار عمومی می‌داند؛ ازاین‌رو شفافیت، اولین قربانی این مدل است.",
   VOID + "کمپین‌های بهداشتی، کمپین‌های انتخاباتی و بازاریابی برند، همه از منطق برنیز استفاده می‌کنند؛ تفاوت اخلاقی آن‌ها در میزان شفافیت منبع و امکان بررسی ادعاهاست.",
  ]),
  "assumptions": [
   "تصمیم‌های عمومی به‌طور طبیعی از انگیزه‌های ناخودآگاه پیروی می‌کنند، نه از استدلال.",
   "متخصص ارتباطات می‌تواند نگرش عمومی را به‌طور برنامه‌ریزی‌شده شکل دهد.",
   "رهبری افکار عمومی وظیفهٔ دموکراتیک است، نه استثنای آن.",
  ],
  "principles": [
   "پیش از هر پیام، تحلیل مخاطب و انگیزه‌های او ضروری است.",
   "نماد و گروه مرجع، مؤثرتر از استدلال مستقیم‌اند.",
   "مهندسی رضایت باید در خدمت اهداف «سازنده» باشد — معیاری که خود برنیز برای مشروعیت آن گذاشت.",
  ],
  "critiques": [
   "تقلیل دموکراسی به فنی‌گری: اگر رضایت «مهندسی» شود، مرز میان اقناع و دستکاری از میان می‌رود و شهروند به موضوع مدیریت بدل می‌شود.",
   "فرض پدرسالارانه: «اهداف سازنده» را چه کسی تعیین می‌کند؟ معیار، عملاً به اختیار مشاور و کارفرما می‌افتد.",
   "نادیده‌گرفتن عاملیت: مدل، مقاومت و استدلال مخاطب را کم‌رنگ می‌کند و قدرت رسانه را مطلق می‌انگارد.",
   "شواهد تجربی ناکافی: ادعای اثر عمیق بر ناخودآگاه همیشه با شواهد تجربی پشتیبانی نشده و در پژوهش‌های اثر، اثر محدودتر نشان داده شده است.",
  ],
  "applications": [
   "تحلیل کمپین‌های انتخاباتی: ردیابی نماد، گروه مرجع و مشاوران پنهان.",
   "اخلاق روابط عمومی و بازاریابی: مرز میان اقناع شفاف و دستکاری.",
   "سواد رسانه‌ای: آموزش تشخیص پیام‌های طراحی‌شده برای انگیزهٔ ناخودآگاه.",
   "پژوهش تاریخ رسانه: نقش برنیز در شکل‌گیری حرفهٔ روابط عمومی.",
  ],
  "evolution": "از «پروپاگاندا» (۱۹۲۸) به «مهندسی رضایت» (۱۹۴۷) و سپس به نقد آن در سنت انتقادی؛ امروز، منطق آن در بازاریابی داده‌محور و کمپین‌های هدفمند رسانه‌های اجتماعی بازتولید می‌شود.",
  "key_concepts": ["مهندسی رضایت (Engineering of Consent)", "حکومت نامرئی (Invisible Government)", "گروه مرجع (Reference Group)", "انگیزهٔ ناخودآگاه (Unconscious Motive)", "اقناع (Persuasion)", "مشاور افکار عمومی (Public Opinion Counsel)"],
  "studies": [
   "Bernays, E. L. (1928). Propaganda. Horace Liveright.",
   "Bernays, E. L. (1947). The engineering of consent. The ANNALS of the American Academy of Political and Social Science, 250(1), 113-120.",
  ],
  "detailed_analysis": "\n".join([
   "۱. بنیان و منطق نظری: برنیز مهندسی رضایت را در سنت «دموکراسی مدیریت‌شده» صورت‌بندی کرد؛ واکنش او به هرج‌ومرج جنگ و تبلیغات توده‌ای بود: افکار عمومی اگر رها شود، خطرناک است و اگر مهندسی شود، مفید.",
   "۲. تنش اخلاقی: خود برنیز رضایت را مشروع می‌دانست اگر در خدمت اهداف سازنده باشد؛ منتقدان همین معیار را نقد می‌کنند که تعیین منفعت عمومی را به مدعی آن واگذار می‌کند.",
   "۳. بازگشت امروز: با هدف‌گیری ریزداده و آزمون A/B، انگیزه‌ها دقیق‌تر از برنیز سنجیده می‌شوند؛ مسئلهٔ اخلاقی همان است: چه کسی به چه کسی، چه تصویری از خیر عمومی عرضه می‌کند.",
  ]),
  "critique_text": "\n".join([
   "۱. تقلیل دموکراسی به فنی‌گری: اگر رضایت «مهندسی» شود، مرز میان اقناع و دستکاری از میان می‌رود و شهروند به موضوع مدیریت بدل می‌شود.",
   "۲. فرض پدرسالارانه: «اهداف سازنده» را چه کسی تعیین می‌کند؟ معیار، عملاً به اختیار مشاور و کارفرما می‌افتد.",
   "۳. نادیده‌گرفتن عاملیت: مدل، مقاومت و استدلال مخاطب را کم‌رنگ می‌کند و قدرت رسانه را مطلق می‌انگارد.",
   "۴. شواهد تجربی ناکافی: ادعای اثر عمیق بر ناخودآگاه همیشه با شواهد تجربی پشتیبانی نشده و در پژوهش‌های اثر، اثر محدودتر نشان داده شده است.",
  ]),
  "example_text": "\n".join([
   "در کمپین «زنان سیگار می‌کشند» دههٔ ۱۹۲۰، سیگار به «مشعل آزادی» بدل شد؛ برنیز با پیوند دادن محصول به نماد استقلال، رفتار را نه با دستور، بلکه با روایت و گروه مرجع تغییر داد.",
   "در یک کمپین انتخاباتی، مشاور پیام را نه وعدهٔ سیاست، بلکه به نماد «امنیت» گره می‌زند؛ رأی‌دهنده احساس می‌کند تصمیم را خود گرفته است — همان رضایت مهندسی‌شده.",
   "در بازاریابی داده‌محور، آزمون A/B برای انتخاب پیام، نسخهٔ دیجیتال همان منطق است: پیش‌بینی واکنش ناخودآگاه مخاطب و تنظیم پیام بر اساس آن.",
  ]),
 },
 "MC-370": {
  "summary": "(برنیز، ۱۹۲۸؛ هرمن و چامسکی، ۱۹۸۸) پروپاگاندا و دستکاری افکار عمومی به مجموعهٔ روش‌هایی گفته می‌شود که نگرش و باور جمعی را بدون استدلال شفاف، در جهت اهداف گروهی خاص هدایت می‌کنند. برنیز آن را هنر «شکل‌دهی ناخودآگاه» افکار عمومی می‌دانست؛ هرمن و چامسکی بعدها توضیح دادند که این کار از طریق پنج فیلتر ساختاری رسانه‌های خبری انجام می‌شود.",
  "definition": "پروپاگاندا، ارتباط هدفمند و سازمان‌یافته برای شکل‌دهی نگرش به‌گونه‌ای که منبع، محتوای آن را فاش نکند یا به‌مرور به‌عنوان واقعیت طبیعی پذیرفته شود؛ دستکاری افکار عمومی، شکل پنهان و بدون برچسب آن است.",
  "main_problem": "چگونه در جامعه‌ای که رسانه آزاد است، افکار عمومی هنوز هم می‌تواند در جهت منافع خاص شکل گیرد؟ نظریه، پرسش را از سطح «دروغ مستقیم» به سطح «ساختار و فیلتر» منتقل می‌کند.",
  "mechanism": "\n".join([
   "(۱) سازوکار روان‌شناختی: برنیز با تکیه بر روان‌کاوی، باور عمومی را تابع انگیزه‌های ناخودآگاه می‌داند؛ پروپاگاندا با فعال‌سازی نمادها، این انگیزه‌ها را جهت می‌دهد.",
   "(۲) فیلتر مالکیت: رسانه‌های خبری بخشی از شرکت‌های بزرگ‌اند؛ منافع مالک، هم‌زمان تعیین‌کنندهٔ سیاست خبری و مرزهای پرسش‌گری است.",
   "(۳) فیلتر تبلیغات: اتکا به درآمد آگهی، آستانهٔ تحمل رسانه در برابر نقد منافع آگهی‌دهندگان را بالا می‌برد.",
   "(۴) فیلتر منابع رسمی: تکیه بر منابع دولتی و نهادی، هزینه و زمان گردآوری خبر را کاهش می‌دهد و به قیمت پذیرش چارچوب آن‌ها تمام می‌شود.",
   "(۵) فیلترهای «ترس» و «ضدیت مشترک»: تهدید بیرونی مشترک، انسجام داخلی می‌سازد و نقد را به «خیانت» بدل می‌کند؛ هرمن و چامسکی این پنج فیلتر را در مدل پروپاگاندا صورت‌بندی کردند.",
   VOID + "در پوشش بحران، وقتی رسانه‌ها صرفاً از منابع رسمی و واژه‌های دولتی استفاده می‌کنند، مرز بحث پیش از آنکه منتقدان حذف شوند، تنگ شده است — همان‌جایی که پروپاگاندا از دروغ آشکار به ساختار پنهان منتقل می‌شود.",
  ]),
  "assumptions": [
   "افکار عمومی از راه انگیزه و نماد شکل می‌گیرد، نه فقط استدلال.",
   "ساختار مالکیت و منافع تجاری، سیاست خبری را مقید می‌کند.",
   "به‌جای توطئهٔ مستقیم، فیلترهای ساختاری می‌توانند نتیجهٔ پروپاگاندا ایجاد کنند.",
  ],
  "principles": [
   "تحلیل پروپاگاندا باید هم محتوا (پیام) و هم ساختار (فیلترها) را شامل شود.",
   "برچسب پروپاگاندا معیار اخلاقی شفافیت منبع است.",
   "تکیه بر منبع رسمی، خود سازوکار انتقال چارچوب است.",
  ],
  "critiques": [
   "ابهام مرز پروپاگاندا و اقناع: هر ارتباط هدفمند را می‌توان پروپاگاندا نامید و همین، ماشه را برای سوءاستفاده از واژه چکانده است.",
   "جبرگرایی ساختاری: مدل پنج‌فیلتری، عاملیت روزنامه‌نگار و تنوع رسانه را کم‌رنگ می‌کند.",
   "احتمال ابطال‌ناپذیری: مدل‌های پروپاگاندا به‌سختی با شواهد نقض، آزمون‌پذیر می‌شوند.",
   "تغییر محیط رسانه: با پلتفرم‌ها، فیلترها از مالکیت رسانه به الگوریتم و اقتصاد توجه منتقل شده‌اند و مدل کلاسیک نیازمند بازنگری است.",
  ],
  "applications": [
   "نقد رسانه: بررسی سهم منبع رسمی و آگهی‌دهنده در شکل‌گیری چارچوب خبر.",
   "سواد رسانه‌ای: آموزش تشخیص برچسب‌گذاری ناقص و چارچوب پنهان.",
   "تحلیل تبلیغات سیاسی: ردیابی نمادها و فیلترهای ساختاری در کمپین‌ها.",
   "مطالعهٔ الگوریتم: چگونه اقتصاد توجه، فیلتر ششم پلتفرمی را ساخته است.",
  ],
  "evolution": "از «پروپاگاندا» برنیز (۱۹۲۸) و «مهندسی رضایت» (۱۹۴۷) به «مدل پروپاگاندا» هرمن و چامسکی (۱۹۸۸)، سپس به تحلیل پروپاگاندای دیجیتال، حساب‌های هماهنگ و دستکاری الگوریتمی.",
  "key_concepts": ["پروپاگاندا (Propaganda)", "فیلترهای مدل پروپاگاندا (Propaganda Model Filters)", "ساخت رضایت (Manufacturing Consent)", "دستکاری افکار عمومی (Opinion Manipulation)", "ضدیت مشترک (Common Antagonism)", "پروپاگاندای دیجیتال (Computational Propaganda)"],
  "studies": [
   "Herman, E. S., & Chomsky, N. (1988). Manufacturing consent: The political economy of the mass media. Pantheon Books.",
   "Bernays, E. L. (1928). Propaganda. Horace Liveright.",
  ],
  "detailed_analysis": "\n".join([
   "۱. بنیان و منطق نظری: برنیز پروپاگاندا را ابزاری فنی و اخلاقاً خنثی می‌دانست که می‌تواند در خدمت خیر عمومی قرار گیرد؛ هرمن و چامسکی همین ابزار را به ساختار اقتصاد رسانه گره زدند و نشان دادند نتیجهٔ آن، ساخت رضایت است، نه انتخاب آزاد.",
   "۲. ریشهٔ انتساب: مفهوم پنج فیلتر متعلق به هرمن و چامسکی (۱۹۸۸) است، نه برنیز (۱۹۲۸)؛ تفکیک این دو، برای دقت نظری ضروری است — برنیز روان‌شناختی و مشاوره‌محور است، هرمن و چامسکی ساختاری و اقتصادمحور.",
   "۳. افق امروز: مدل پنج‌فیلتری در محیط پلتفرمی با فیلترهای تازه‌ای مانند بهینه‌سازی تعامل و هوش مصنوعی مواجه شده است؛ پرسش برنیزی همچنان باقی است: چه کسی رضایت را مهندسی می‌کند و بر چه مبنایی.",
  ]),
  "critique_text": "\n".join([
   "۱. ابهام مرز پروپاگاندا و اقناع: هر ارتباط هدفمند را می‌توان پروپاگاندا نامید و همین، ماشه را برای سوءاستفاده از واژه چکانده است.",
   "۲. جبرگرایی ساختاری: مدل پنج‌فیلتری، عاملیت روزنامه‌نگار و تنوع رسانه را کم‌رنگ می‌کند.",
   "۳. احتمال ابطال‌ناپذیری: مدل‌های پروپاگاندا به‌سختی با شواهد نقض، آزمون‌پذیر می‌شوند.",
   "۴. تغییر محیط رسانه: با پلتفرم‌ها، فیلترها از مالکیت رسانه به الگوریتم و اقتصاد توجه منتقل شده‌اند و مدل کلاسیک نیازمند بازنگری است.",
  ]),
  "example_text": "\n".join([
   "در پوشش یک مناقشهٔ خارجی، استفادهٔ یکسان از واژه‌های دولتی در همهٔ رسانه‌ها نشان می‌دهد فیلتر منابع رسمی پیش از هر سانسوری عمل کرده است؛ منتقدان وقتی وارد گفت‌وگو می‌شوند که چارچوب از پیش تثبیت شده است.",
   "یک تهدید بیرونی مشترک، انتقاد داخلی را به «خیانت به وطن» بدل می‌کند؛ همین سازوکار ضدیت مشترک، مرز بحث را می‌بندد، بی‌آنکه کسی دستور حذفی داده باشد.",
   "در شبکه‌های اجتماعی، هماهنگی حساب‌ها برای تکرار یک روایت، نسخهٔ محاسباتی پروپاگاندا است؛ حجم تکرار جای شاهد را می‌گیرد و مخاطب آن حجم را نشانهٔ حقیقت می‌پندارد.",
  ]),
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
    codes = list(S.keys())
    cur.execute("SELECT id, code, properties FROM kb_entities WHERE code IN (%s)" % ",".join(["%s"]*len(codes)), codes)
    rows = {code:(eid, json.loads(pr)) for (eid, code, pr) in cur.fetchall()}
    with open(BACKUP, "w", encoding="utf-8") as f:
        json.dump([{"code": cd, "props": rows[cd][1]} for cd in codes if cd in rows], f, ensure_ascii=False, indent=1)
    print("backup ->", len(rows), "rows")

    for code in codes:
        if code not in rows:
            print("MISSING", code); continue
        eid, p = rows[code]
        e = ENRICH[code]
        if "critique_text" in e: p["critique"] = e["critique_text"]
        if "example_text" in e: p["example"] = e["example_text"]
        for k, v in e.items():
            if k in ("critique_text", "example_text"): continue
            p[k] = v
        if not has_content(p.get("definition")) and has_content(p.get("summary")): p["definition"] = p["summary"]
        spec = S[code]
        p["sources"] = [dict(citation=s["citation"], language=("انگلیسی" if s["language"]=="en" else "فارسی"),
                             doi=s.get("doi") or "", url=s.get("url") or "", year=s.get("year")) for s in spec]
        p["citations"] = [dict(source=s["citation"], locator=s["locator"], supports=s["supports"],
                               verified=bool(s.get("verified"))) for s in spec]
        n_sources = len(spec); n_verified = sum(1 for s in spec if s.get("verified"))
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
                cur.execute("SELECT id FROM kb_sources WHERE doi=%s LIMIT 1", (s["doi"],)); r = cur.fetchone()
                if r: sid = r[0]
            if sid is None:
                cur.execute("SELECT id FROM kb_sources WHERE title_en=%s AND year=%s LIMIT 1", (s["title_en"], s["year"])); r = cur.fetchone()
                if r: sid = r[0]
            if sid is None:
                bib = json.dumps({"authors": s["authors"], "citation": s["citation"]}, ensure_ascii=False)
                cur.execute("INSERT INTO kb_sources (kind,title_fa,title_en,year,publisher,doi,isbn,url,language,access_type,bibliographic) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (s["kind"], s["title_fa"], s["title_en"], s["year"], s["publisher"], s.get("doi"), s.get("isbn"), s.get("url"),
                     s["language"], "open" if s.get("url") else "unknown", bib))
                sid = cur.lastrowid
            cur.execute("SELECT id FROM kb_evidence WHERE about_code=%s AND source_id=%s LIMIT 1", (code, sid))
            if cur.fetchone():
                continue
            lt = "CHAPTER" if s["locator_type"] == "CHAPTER" else ("PAGE" if s["locator_type"] == "page_range" else "SECTION")
            cur.execute("INSERT INTO kb_citations (source_id,locator_type,locator_value,paraphrase,citation_style,language,accessed_at) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                (sid, lt, s["locator"], "پشتیبانی از بخش: " + s["supports"], "apa", s["language"], NOW))
            cid = cur.lastrowid
            cur.execute("INSERT INTO kb_evidence (source_id,citation_id,about_code,evidence_type,evidence_summary,locator,direction,extraction_method,verification_status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (sid, cid, code, "bibliographic_reference", "منبع اصلی برای بخش: " + s["supports"], s["locator"], "supports",
                 "ai_extraction", "verified" if s.get("verified") else "unverified"))
        cur.execute("SELECT COALESCE(MAX(version),0)+1 FROM kb_entity_versions WHERE entity_id=%s", (eid,))
        ver = cur.fetchone()[0]
        cur.execute("INSERT INTO kb_entity_versions (entity_id, version, snapshot, change_reason, changed_by, created_at) VALUES (%s,%s,%s,%s,%s,%s)",
                    (eid, ver, json.dumps({"quality_score": score, "words": words, "sources": n_sources, "verified": n_verified}, ensure_ascii=False),
                     "full documentation enrichment + verified sources", STAMP, NOW))
        cur.execute("INSERT INTO kb_audit_log (entity_code, action, detail, source) VALUES (%s,%s,%s,%s)",
                    (code, "DOC_ENRICH", json.dumps({"quality_score": score, "words": words, "sources": n_sources, "verified": n_verified, "relations": n_relations, "breakdown": detail}, ensure_ascii=False), STAMP))
        print(f"{code}: score={score} words={words} sources={n_sources} verified={n_verified} relations={n_relations} | {detail}")
    c.commit(); c.close()
    print("BATCH69 THEORY DONE")

if __name__ == "__main__":
    main()
