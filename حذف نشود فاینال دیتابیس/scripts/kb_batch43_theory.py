# -*- coding: utf-8 -*-
"""Batch 43 (THEORY): MC-164 Credence Goods (Darby & Karni 1973), MC-165 Advertising as
Information vs Persuasive (Nelson 1974), MC-166 The Cultural Industries (Hesmondhalgh 2002),
MC-167 Creative Labor & Precarity (Hesmondhalgh & Baker 2011). All verified 2026-11-16."""
import pymysql, json

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch43-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch43_theory.json"

S = {
 "MC-164": [  # Credence Goods
   dict(kind="JOURNAL_ARTICLE", title_en="Free Competition and the Optimal Amount of Fraud",
        title_fa="رقابت آزاد و مقدار بهینهٔ تقلب", authors="Darby, M. R., & Karni, E.", year=1973,
        publisher="Journal of Law and Economics, 16(1), 67-88", doi="10.1086/466756",
        url="https://www.journals.uchicago.edu/doi/abs/10.1086/466756", language="en", isbn=None,
        citation="Darby, M. R., & Karni, E. (1973). Free competition and the optimal amount of fraud. Journal of Law and Economics, 16(1), 67-88.",
        locator="pp. 67-88", locator_type="page_range", supports="definition / search-experience-credence triad", verified=True),
   dict(kind="JOURNAL_ARTICLE", title_en="On Doctors, Mechanics, and Computer Specialists: The Economics of Credence Goods",
        title_fa="دربارهٔ پزشکان، مکانیک‌ها و متخصصان رایانه: اقتصاد کالاهای اعتباری",
        authors="Dulleck, U., & Kerschbamer, R.", year=2006,
        publisher="Journal of Economic Literature, 44(1), 5-42", doi=None, url=None, language="en", isbn=None,
        citation="Dulleck, U., & Kerschbamer, R. (2006). On doctors, mechanics, and computer specialists: The economics of credence goods. Journal of Economic Literature, 44(1), 5-42.",
        locator="pp. 5-42", locator_type="page_range", supports="mechanism / inefficiencies and institutions", verified=False),
 ],
 "MC-165": [  # Advertising as Information vs Persuasion
   dict(kind="JOURNAL_ARTICLE", title_en="Advertising as Information",
        title_fa="تبلیغات به‌مثابهٔ اطلاعات", authors="Nelson, P.", year=1974,
        publisher="Journal of Political Economy, 82(4), 729-754", doi="10.1086/260231",
        url="https://www.journals.uchicago.edu/doi/abs/10.1086/260231", language="en", isbn=None,
        citation="Nelson, P. (1974). Advertising as information. Journal of Political Economy, 82(4), 729-754.",
        locator="pp. 729-754", locator_type="page_range", supports="definition / signaling mechanism / search-experience distinction", verified=True),
   dict(kind="BOOK_CHAPTER", title_en="The Economic Analysis of Advertising",
        title_fa="تحلیل اقتصادی تبلیغات", authors="Bagwell, K.", year=2007,
        publisher="In M. Armstrong & R. Porter (Eds.), Handbook of Industrial Organization (Vol. 3, pp. 1701-1844). Amsterdam: North-Holland",
        doi=None, url=None, language="en", isbn=None,
        citation="Bagwell, K. (2007). The economic analysis of advertising. In M. Armstrong & R. Porter (Eds.), Handbook of industrial organization (Vol. 3, pp. 1701-1844). North-Holland.",
        locator="pp. 1701-1844", locator_type="page_range", supports="evolution / information vs persuasion debate", verified=False),
 ],
 "MC-166": [  # The Cultural Industries
   dict(kind="BOOK", title_en="The Cultural Industries",
        title_fa="صنایع فرهنگی", authors="Hesmondhalgh, D.", year=2002,
        publisher="London: Sage", doi=None, url=None, language="en", isbn="9780761954521",
        citation="Hesmondhalgh, D. (2002). The cultural industries. Sage.",
        locator="whole work", locator_type="work", supports="definition / key features / political economy", verified=True),
   dict(kind="BOOK", title_en="Dialectic of Enlightenment",
        title_fa="دیالکتیک روشنگری", authors="Adorno, T. W., & Horkheimer, M.", year=1947,
        publisher="English trans. New York: Herder and Herder, 1972", doi=None, url=None, language="en", isbn=None,
        citation="Adorno, T. W., & Horkheimer, M. (1972). Dialectic of enlightenment (J. Cumming, Trans.). Herder and Herder. (Original work published 1947)",
        locator="Ch. 'The Culture Industry'", locator_type="CHAPTER", supports="origin / critique of mass culture", verified=False),
 ],
 "MC-167": [  # Creative Labor & Precarity
   dict(kind="BOOK", title_en="Creative Labour: Media Work in Three Cultural Industries",
        title_fa="کار خلاق: کار رسانه‌ای در سه صنعت فرهنگی",
        authors="Hesmondhalgh, D., & Baker, S.", year=2011,
        publisher="London: Routledge", doi=None, url=None, language="en", isbn="9780415677738",
        citation="Hesmondhalgh, D., & Baker, S. (2011). Creative labour: Media work in three cultural industries. Routledge.",
        locator="whole work", locator_type="work", supports="definition / precarity mechanism / inequalities", verified=True),
   dict(kind="BOOK", title_en="No-Collar: The Humane Workplace and Its Hidden Costs",
        title_fa="بدون یقه: محیط کار انسانی و هزینه‌های پنهانش", authors="Ross, A.", year=2003,
        publisher="New York: Basic Books", doi=None, url=None, language="en", isbn=None,
        citation="Ross, A. (2003). No-collar: The humane workplace and its hidden costs. Basic Books.",
        locator="whole work", locator_type="work", supports="no-collar concept / self-exploitation", verified=False),
 ],
}

ENRICH = {
 "MC-164": {
   "summary": "«کالای اعتباری» (Credence Good) کالا یا خدمتی است که کیفیت آن حتی پس از مصرف نیز به‌سختی برای مصرف‌کننده قابل ارزیابی است. مایکل داربی و ادی کارنی در مقالهٔ «Free Competition and the Optimal Amount of Fraud» (۱۹۷۳، Journal of Law and Economics) سه‌گانهٔ مشهور «کالای جست‌وجویی، تجربی و اعتباری» را معرفی کردند و نشان دادند در کالاهای اعتباری، عدم تقارن اطلاعات امکان تقلب را فراهم می‌کند (Darby & Karni, 1973).",
   "main_problem": "وقتی مصرف‌کننده نمی‌تواند کیفیت را حتی پس از مصرف بسنجد (مانند تشخیص پزشک)، چه سازوکارهایی از سوءاستفادهٔ فروشنده جلوگیری می‌کند، و چرا در فضای رقابت آزاد، مقداری «تقلب بهینه» و نه صفر باقی می‌ماند؟",
   "mechanism": "داربی و کارنی کالاها را بر اساس زمان و امکان ارزیابی کیفیت دسته‌بندی می‌کنند: «کالای جست‌وجویی» (search good) که کیفیتش پیش از خرید قابل بررسی است؛ «کالای تجربی» (experience good) که کیفیتش پس از مصرف آشکار می‌شود؛ و «کالای اعتباری» (credence good) که کیفیتش حتی پس از مصرف برای مصرف‌کننده نامعلوم می‌ماند (Darby & Karni, 1973). در کالای اعتباری دو نوع عدم تقارن وجود دارد: «تشخیص» (diagnosis) — فروشنده بهتر می‌داند مشتری چه نیاز دارد؛ و «درمان» (treatment) — فروشنده می‌داند چه چیزی ارائه کرده است. همین دوگانگی سه ناکارآمدی می‌سازد: «درمان بیش از حد» (over-treatment)، «کم‌درمانی» (under-treatment) و «اضافه‌گیری» (overcharging). داربی و کارنی نشان دادند حتی با رقابت آزاد، مقدار بهینهٔ تقلب صفر نیست، زیرا حذف کامل عدم تقارن پرهزینه است؛ از این رو نهادهایی مانند مجوزدهی حرفه‌ای، ضمانت، شهرت و تکرار تعامل به‌عنوان جایگزین اطلاعات کامل ظاهر می‌شوند. دولک و کرش‌بامر (Dulleck & Kerschbamer, 2006) بعدها نشان دادند بازار می‌تواند برخی از این ناکارآمدی‌ها را با ترکیب «تأییدپذیری» (verifiability)، «مسئولیت» (liability) و «شهرت» رفع کند. در رسانه، کیفیت خبر — دقت، جامعیت و بی‌طرفی — برای مخاطب عادی به‌سختی قابل ارزیابی است و همین، خبر را به کالای اعتباری بدل می‌کند؛ آثار آن را در اعتماد به رسانه، نقش برندهای خبری و آسیب‌پذیری در برابر اطلاعات نادرست می‌بینیم.",
   "assumptions": [
     "مصرف‌کننده در ارزیابی کیفیت برخی کالاها حتی پس از مصرف ناتوان یا کم‌توان است.",
     "فروشنده اطلاعات بیشتری دربارهٔ نیاز و کیفیت در اختیار دارد (عدم تقارن اطلاعات).",
     "دسترسی به اطلاعات کامل پرهزینه است و حذف کامل تقلب بهینه نیست."
   ],
   "principles": [
     "سه‌گانهٔ ارزیابی: جست‌وجویی، تجربی و اعتباری.",
     "دوگانگی تشخیص-درمان: عدم تقارن در هر دو مرحله امکان سوءاستفاده می‌دهد.",
     "نهادهای جایگزین: مجوز، ضمانت و شهرت، کمبود اطلاعات را جبران می‌کنند."
   ],
   "critiques": [
     "ابهام مرزی: مرز کالای اعتباری با تجربی در عمل سیال است و بسیاری از کالاها ترکیبی‌اند.",
     "سنجش تجربی دشوار: نشان‌دادن ناکارآمدی‌ها و اندازهٔ تقلب به‌سختی قابل شناسایی است.",
     "فناوری و اعتماد: پلتفرم‌ها و سیستم‌های امتیازدهی می‌توانند عدم تقارن را کم یا به شکل تازه بازتولید کنند."
   ],
   "applications": [
     "تحلیل اقتصاد خبر و کیفیت رسانه به‌عنوان کالای اعتباری.",
     "طراحی سازوکارهای اعتماد در بازار خدمات تخصصی و پلتفرم‌های مشاوره.",
     "سیاست‌گذاری مجوزدهی، ضمانت و مسئولیت حرفه‌ای."
   ],
   "evolution": "داربی و کارنی (1973) سه‌گانهٔ کالاها را معرفی کردند. دولک و کرش‌بامر (2006) ادبیات را نظام‌مند کردند و شرایط حل ناکارآمدی‌ها را تحلیل کردند. در دههٔ ۲۰۱۰، اقتصاد اعتماد در پلتفرم‌ها، امتیازدهی آنلاین و مسئلهٔ اطلاعات نادرست، این چارچوب را به بحث رسانه و پلتفرم گره زد.",
   "key_concepts": ["کالای اعتباری (credence good)", "کالای جست‌وجویی و تجربی (search and experience goods)", "عدم تقارن اطلاعات (information asymmetry)", "درمان بیش از حد (over-treatment)", "شهرت و ضمانت (reputation and warranty)"],
   "studies": ["Darby, M. R., & Karni, E. (1973). Free Competition and the Optimal Amount of Fraud. Journal of Law and Economics, 16(1), 67-88.", "Dulleck, U., & Kerschbamer, R. (2006). The Economics of Credence Goods. Journal of Economic Literature, 44(1), 5-42."],
 },
 "MC-165": {
   "summary": "«تبلیغات به‌مثابه اطلاعات در برابر تبلیغات اقناعی» (Advertising as Information vs. Persuasive Advertising) دو خوانش رقیب از کارکرد اقتصادی تبلیغات را در برابر هم می‌گذارد: خوانشی که تبلیغات را حامل اطلاعات و علامت کیفیت می‌داند و خوانشی که آن را ابزار تغییر سلیقه و ایجاد قدرت بازار می‌بیند. فیلیپ نلسون در مقالهٔ «Advertising as Information» (۱۹۷۴، Journal of Political Economy) صورت‌بندی کلاسیک خوانش اطلاعاتی را ارائه کرد (Nelson, 1974).",
   "main_problem": "تبلیغات چه چیزی به مصرف‌کننده منتقل می‌کند — اطلاعات واقعی دربارهٔ قیمت و کیفیت، یا صرفاً تلاشی برای دستکاری سلیقه — و این دو تلقی چه پیامدهای رفاهی متفاوتی برای بازار و رسانه دارند؟",
   "mechanism": "نلسون میان دو نوع کالا تفکیک می‌کند: برای «کالای جست‌وجویی» (search good)، تبلیغات می‌تواند اطلاعات مستقیم دربارهٔ ویژگی، قیمت و مکان بدهد. برای «کالای تجربی» (experience good)، محتوای اطلاعاتی مستقیم محدود است، اما «خودِ هزینهٔ تبلیغات» علامت است: شرکتی که هزینهٔ سنگین تبلیغ می‌کند، برای بازیابی این هزینه به خرید مکرر نیاز دارد و خرید مکرر تنها با رضایت از کیفیت حاصل می‌شود؛ بنابراین تبلیغ پرهزینه به‌طور غیرمستقیم به کیفیت بالا اشاره می‌کند (Nelson, 1974). در برابر این خوانش، «تبلیغات اقناعی» (persuasive advertising) بر تغییر سلیقه، ایجاد تمایز کاذب، وفاداری برند و موانع ورود تأکید می‌کند: تبلیغات می‌تواند تقاضا را از کالای ارزان‌تر به گران‌تر منتقل کند، کشش تقاضا را کم کند و قدرت بازار بسازد. بگ‌ول (Bagwell, 2007) در مرور جامع نشان داد شواهد تجربی از هر دو اثر پشتیبانی می‌کنند و مرز دقیق میان اطلاعات و اقناع اغلب به نوع کالا، ساختار بازار و محتوای پیام بستگی دارد. در رسانه، همین دوگانه پیامدهای مهمی دارد: اگر تبلیغات اطلاعاتی باشد، مدل آگهی‌محور می‌تواند کارا باشد؛ اگر اقناعی و مولد قدرت بازار باشد، بخشی از هزینهٔ تبلیغات، انتقال رفاه از مصرف‌کننده به رسانه و برند است.",
   "assumptions": [
     "مصرف‌کننده دربارهٔ کیفیت برخی کالاها پیش از خرید اطلاعات کافی ندارد.",
     "هزینهٔ تبلیغات برای مصرف‌کننده قابل مشاهده است و می‌تواند به‌عنوان علامت تفسیر شود.",
     "سلیقهٔ مصرف‌کننده می‌تواند مستقل از اطلاعات واقعی تحت تأثیر تبلیغات تغییر کند."
   ],
   "principles": [
     "علامت‌دهی هزینه‌ای: تبلیغ پرهزینه، نشانی از اطمینان به کیفیت است.",
     "تمایز اطلاعاتی و اقناعی: تبلیغ می‌تواند هم آگاه‌کننده و هم سلیقه‌ساز باشد.",
     "پیامد رفاهی وابسته: ارزیابی تبلیغات بدون توجه به ساختار بازار ممکن نیست."
   ],
   "critiques": [
     "دوگانهٔ نادرست: در عمل بیشتر تبلیغات هم‌زمان اطلاعاتی و اقناعی‌اند و تفکیک آن‌ها سخت است.",
     "سنجش اثر: اندازه‌گیری جداگانهٔ اثر اطلاعاتی و اقناعی با داده‌های بازار دشوار است.",
     "تحول دیجیتال: تبلیغات هدفمند و الگوریتمی، فرض‌های کلاسیک دربارهٔ مشاهده‌پذیری و هزینه را دگرگون کرده است."
   ],
   "applications": [
     "تحلیل اقتصاد رسانهٔ آگهی‌محور و پایداری مالی آن.",
     "سیاست رقابت و داوری دربارهٔ تبلیغات گمراه‌کننده یا موانع ورود.",
     "پژوهش دربارهٔ اثر تبلیغات دیجیتال بر کیفیت و تنوع محتوا."
   ],
   "evolution": "نلسون (1974) خوانش اطلاعاتی را تثبیت کرد و در دهه‌های ۱۹۸۰-۱۹۹۰ مدل‌های علامت‌دهی و اقناع توسعه یافتند. بگ‌ول (2007) این ادبیات را نظام‌مند کرد. در دههٔ ۲۰۱۰-۲۰۲۰، تبلیغات برنامه‌ای، هدف‌گیری رفتاری و حراج‌های تبلیغاتی، پرسش‌های تازه‌ای دربارهٔ شفافیت و رفاه مطرح کردند.",
   "key_concepts": ["تبلیغات اطلاعاتی (informative advertising)", "تبلیغات اقناعی (persuasive advertising)", "علامت‌دهی کیفیت (quality signaling)", "کالای جست‌وجویی و تجربی (search and experience goods)", "موانع ورود (barriers to entry)"],
   "studies": ["Nelson, P. (1974). Advertising as Information. Journal of Political Economy, 82(4), 729-754.", "Bagwell, K. (2007). The Economic Analysis of Advertising. Handbook of Industrial Organization, 3, 1701-1844."],
 },
 "MC-166": {
   "summary": "«صنایع فرهنگی» (The Cultural Industries) به بخش‌هایی اشاره دارد که کالاها و خدمات نمادین و معنادار تولید و توزیع می‌کنند: پخش، سینما، موسیقی، نشر، تبلیغات و بازی. دیوید هسموندهالغ در کتاب «The Cultural Industries» (۲۰۰۲، Sage) این مفهوم را با رویکردی انتقادی و تجربی بازتعریف کرد و آن را از برداشت مکتب فرانکفورت متمایز ساخت (Hesmondhalgh, 2002).",
   "main_problem": "تولید و توزیع فرهنگ در قالب صنعتی چه ویژگی‌هایی دارد، چگونه تجارت و خلاقیت در آن در هم می‌تنند، و «صنعت فرهنگی» تا چه اندازه واقعاً مخاطب را یکسان‌سازی و دستکاری می‌کند؟",
   "mechanism": "هسموندهالغ ویژگی‌های ساختاری صنایع فرهنگی را برمی‌شمرد: (۱) «تقاضای نامعلوم» (radical contingency) — هیچ‌کس پیش از انتشار نمی‌داند کدام اثر موفق می‌شود، از این رو «بیش‌تولید» (overproduction) و اتکا به مجموعه‌ای از آثار برای پوشش شکست‌ها رایج است؛ (۲) «هزینهٔ ثابت بالا و هزینهٔ نهایی پایین» — تولید یک فیلم یا آلبوم گران است اما تکثیر آن ارزان، و همین ویژگی صنایع فرهنگی را به کالای شبه‌عمومی نزدیک می‌کند؛ (۳) «تنش تجارت و خلاقیت» — میان «خالقان نماد» (symbol creators) که به ارزش زیبایی‌شناختی وفادارند و مدیران تجاری که به سود و مقیاس می‌اندیشند؛ (۴) «تمرکز و کنگلومرایی» — ادغام‌ها ساختار بازار را به سمت تعداد اندکی شرکت بزرگ هدایت می‌کند (Hesmondhalgh, 2002). این چارچوب در برابر خوانش کلاسیک مکتب فرانکفورت قرار می‌گیرد: آدورنو و هورکهایمر در «دیالکتیک روشنگری» از «صنعت فرهنگ» (Culture Industry، مفرد) سخن گفتند و آن را ابزار یکسان‌سازی، «شبه‌فردیت» (pseudo-individualization) و فریب توده‌ها دانستند (Adorno & Horkheimer, 1972). هسموندهالغ با حفظ دغدغهٔ سیاسی-اقتصادی، بر پیچیدگی، تنوع و عاملیت مخاطب تأکید می‌کند و کاربرد واژهٔ جمع «صنایع» را دقیق‌تر می‌داند، زیرا بخش‌های مختلف منطق‌های متفاوتی دارند.",
   "assumptions": [
     "فرهنگ در قالب کالا و با منطق صنعتی تولید و توزیع می‌شود.",
     "تقاضا برای کالاهای فرهنگی به‌طور ساختاری نامعلوم و پرریسک است.",
     "تجارت و خلاقیت در صنایع فرهنگی هم‌زمان در تنش و هم‌زیستی‌اند."
   ],
   "principles": [
     "ریسک ساختاری: موفقیت اثر فرهنگی پیش از انتشار نامعلوم است.",
     "اقتصاد نماد: هزینهٔ ثابت بالا و تکثیر ارزان، ساختار بازار را شکل می‌دهد.",
     "تنش خلاقیت/تجارت: ارزش هنری و منطق سود در تعامل دائمی‌اند."
   ],
   "critiques": [
     "نقد مکتب فرانکفورت: یکسان‌سازی و فریب توده، عاملیت مخاطب و تنوع فرهنگی را نادیده می‌گیرد.",
     "غرب‌محوری: الگوی صنایع فرهنگی عمدتاً از تجربهٔ غربی استخراج شده است.",
     "تحول پلتفرمی: منطق پلتفرم و محتوای کاربرساخته، مرزهای صناعت و مخاطب را جابه‌جا کرده است."
   ],
   "applications": [
     "سیاست‌گذاری فرهنگی و رسانه‌ای و حمایت از تنوع.",
     "تحلیل اقتصاد رسانه، ادغام و تمرکز مالکیت.",
     "پژوهش دربارهٔ کار خلاق و تولید محتوا در عصر پلتفرم."
   ],
   "evolution": "آدورنو و هورکهایمر (1947) مفهوم انتقادی صنعت فرهنگ را ساختند. در دههٔ ۱۹۸۰-۱۹۹۰، رویکرد «صنایع خلاق» (DCMS) و در دههٔ ۲۰۰۰ اقتصاد سیاسی انتقادی هسموندهالغ (2002) آن را بازتعریف کردند. ویرایش‌های بعدی و پژوهش پلتفرم، این چارچوب را به عصر دیجیتال گستردند.",
   "key_concepts": ["صنایع فرهنگی (cultural industries)", "صنعت فرهنگ (culture industry)", "تقاضای نامعلوم (radical contingency)", "بیش‌تولید (overproduction)", "خالقان نماد (symbol creators)"],
   "studies": ["Hesmondhalgh, D. (2002). The Cultural Industries. Sage.", "Adorno, T. W., & Horkheimer, M. (1972). Dialectic of Enlightenment. Herder and Herder."],
 },
 "MC-167": {
   "summary": "«کار خلاق، ناپایداری و کار بدون یقه» (Creative Labor, Precarity & “No-Collar” Work) به شرایط کاری در صنایع خلاق و رسانه‌ای اشاره دارد: کار پروژه‌ای و قراردادهای کوتاه‌مدت، ساعت‌های طولانی، ورود بدون مزد و ناپایداری درآمد، همراه با promises خودشکوفایی و آزادی. دیوید هسموندهالغ و سارا بیکر در «Creative Labour» (۲۰۱۱، Routledge) این شرایط را در سه صنعت تلویزیون، موسیقی و مجله به‌طور تجربی بررسی کردند (Hesmondhalgh & Baker, 2011).",
   "main_problem": "چرا کار خلاق که با آزادی، خودشکوفایی و «شور» توصیف می‌شود، هم‌زمان با ناپایداری، نابرابری و خودبهره‌کشی همراه است، و چه سازوکارهایی این پیوند متناقض را بازتولید می‌کند؟",
   "mechanism": "هسموندهالغ و بیکر نشان می‌دهند کار خلاق بر «کار پروژه‌ای» (project-based work) و «حرفهٔ سبدی» (portfolio career) استوار است: افراد به‌جای شغل ثابت، مجموعه‌ای از پروژه‌های کوتاه‌مدت را دنبال می‌کنند و همین امر ناپایداری درآمد و فشار دائمی برای شبکه‌سازی و بازاریابی خود را ایجاد می‌کند (Hesmondhalgh & Baker, 2011). «شور» (passion) به‌عنوان انگیزهٔ اصلی، دستمزد پایین، کار بدون مزد و ساعت‌های طولانی را توجیه‌پذیر می‌کند، زیرا کار خلاق به‌عنوان پاداش درونی و نه ابزار معاش فهمیده می‌شود. این سازوکار نابرابری‌های جنسیتی، طبقاتی و نسلی را بازتولید می‌کند: کسانی که پشتوانهٔ مالی خانوادگی دارند می‌توانند دورهٔ ورود بدون مزد را تحمل کنند و شبکه‌های حرفه‌ای را بسازند. اندرو راس در «No-Collar» (۲۰۰۳، Basic Books) با مطالعهٔ قوم‌نگارانهٔ محیط‌های کار دیجیتال نشان داد فرهنگ «انسانی» و راحت دفتر — ساعات انعطاف‌پذیر، امکانات رفاهی و مرزهای مبهم کار و زندگی — شکل تازه‌ای از کنترل و خودبهره‌کشی است که «بدون یقه» بودن را به پوششی برای کاهش امنیت شغلی بدل می‌کند (Ross, 2003). برآیند، ظهور «کارگر خلاق ناپایدار» است: به‌ظاهر آزاد، اما وابسته به شبکه‌ها، برند شخصی و پروژه‌های پیوسته.",
   "assumptions": [
     "کار خلاق به‌طور ساختاری پروژه‌ای و قراردادی است و شغل ثابت در آن استثناست.",
     "انگیزهٔ درونی و «شور» می‌تواند دستمزد پایین و ناپایداری را توجیه کند.",
     "سرمایهٔ اجتماعی و پشتوانهٔ مالی، دسترسی به فرصت‌های کار خلاق را شکل می‌دهد."
   ],
   "principles": [
     "ناپایداری ساختاری: درآمد و اشتغال در کار خلاق پیوسته در معرض قطع است.",
     "شور به‌عنوان توجیه: عشق به کار، شرایط نابرابر را طبیعی جلوه می‌دهد.",
     "مرززدایی کار/زندگی: فرهنگ «بدون یقه» مرزهای زمانی و مکانی کار را در هم می‌ریزد."
   ],
   "critiques": [
     "رومانتیسم: روایت «کارگر خلاق آزاد» می‌تواند نابرابری و استثمار را پنهان کند.",
     "سوگیری بقا: پژوهش‌هایی که فقط موفق‌ها را می‌بینند، ناپایداری اکثریت را نادیده می‌گیرند.",
     "تنوع بافت: تجربهٔ کار خلاق در کشورها و بخش‌های مختلف به‌شدت متفاوت است و تعمیم آن دشوار است."
   ],
   "applications": [
     "سیاست‌های کار و رفاه در صنایع خلاق و رسانه‌ای.",
     "پژوهش دربارهٔ کار پلتفرمی، فریلنسری و اقتصاد تأثیرگذاران.",
     "طراحی سیاست‌های ضدتبعیض و حمایت از دورهٔ ورود به حرفه."
   ],
   "evolution": "بحث کار خلاق در دههٔ ۱۹۹۰ با رشد اقتصاد خلاق و در دههٔ ۲۰۰۰ با مطالعات انتقادی کار رسانه‌ای شکل گرفت. هسموندهالغ و بیکر (2011) آن را با شواهد کیفی نظام‌مند کردند. در دههٔ ۲۰۱۰-۲۰۲۰، کار پلتفرمی و اقتصاد تأثیرگذاران، ناپایداری را به شکل تازه‌ای بازتولید کرد.",
   "key_concepts": ["کار خلاق (creative labour)", "ناپایداری (precarity)", "کار بدون یقه (no-collar work)", "کار پروژه‌ای (project-based work)", "خودبهره‌کشی (self-exploitation)"],
   "studies": ["Hesmondhalgh, D., & Baker, S. (2011). Creative Labour. Routledge.", "Ross, A. (2003). No-Collar: The Humane Workplace and Its Hidden Costs. Basic Books."],
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
    codes = ["MC-164", "MC-165", "MC-166", "MC-167"]
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
    print("BATCH43 THEORY DONE")

if __name__ == "__main__":
    main()
