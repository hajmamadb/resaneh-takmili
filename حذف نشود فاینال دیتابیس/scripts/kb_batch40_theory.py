# -*- coding: utf-8 -*-
"""Batch 40 (THEORY): MC-050 Citizen Journalism (Bowman & Willis 2003), MC-056 Data Sovereignty
(Couture & Toupin 2019), MC-148 Brand Personality (Aaker 1997), MC-149 Attribution Theory
(Heider 1958). All verified 2026-11-16."""
import pymysql, json

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch40-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch40_theory.json"

S = {
 "MC-050": [  # Citizen Journalism
   dict(kind="REPORT", title_en="We Media: How Audiences are Shaping the Future of News and Information",
        title_fa="ما رسانه‌ایم: مخاطبان چگونه آیندهٔ خبر و اطلاعات را شکل می‌دهند",
        authors="Bowman, S., & Willis, C.", year=2003,
        publisher="Reston, VA: The Media Center at the American Press Institute", doi=None,
        url="https://ict4peace.org/wp-content/uploads/2007/05/we_media.pdf", language="en", isbn=None,
        citation="Bowman, S., & Willis, C. (2003). We media: How audiences are shaping the future of news and information. The Media Center at the American Press Institute.",
        locator="whole work", locator_type="work", supports="definition / participatory forms", verified=True),
   dict(kind="BOOK", title_en="We the Media: Grassroots Journalism by the People, for the People",
        title_fa="ما رسانه‌ایم: روزنامه‌نگاری مردمی از سوی مردم برای مردم", authors="Gillmor, D.", year=2004,
        publisher="Sebastopol, CA: O'Reilly Media", doi=None, url=None, language="en", isbn=None,
        citation="Gillmor, D. (2004). We the media: Grassroots journalism by the people, for the people. O'Reilly Media.",
        locator="whole work", locator_type="work", supports="evolution / 'former audience'", verified=False),
 ],
 "MC-056": [  # Data Sovereignty
   dict(kind="JOURNAL_ARTICLE", title_en="What Does the Notion of \u201cSovereignty\u201d Mean When Referring to the Digital?",
        title_fa="مفهوم «حاکمیت» در اشاره به امر دیجیتال چه معنایی دارد؟",
        authors="Couture, S., & Toupin, S.", year=2019,
        publisher="New Media & Society, 21(10), 2305-2322", doi="10.1177/1461444819865984",
        url="https://journals.sagepub.com/doi/full/10.1177/1461444819865984", language="en", isbn=None,
        citation="Couture, S., & Toupin, S. (2019). What does the notion of \u201csovereignty\u201d mean when referring to the digital? New Media & Society, 21(10), 2305-2322.",
        locator="pp. 2305-2322", locator_type="page_range", supports="definition / three senses / mechanism", verified=True),
   dict(kind="JOURNAL_ARTICLE", title_en="Digital Sovereignty",
        title_fa="حاکمیت دیجیتال", authors="Pohle, J., & Thiel, T.", year=2020,
        publisher="Internet Policy Review, 9(4)", doi=None, url=None, language="en", isbn=None,
        citation="Pohle, J., & Thiel, T. (2020). Digital sovereignty. Internet Policy Review, 9(4).",
        locator="whole work", locator_type="work", supports="evolution / policy discourse", verified=False),
 ],
 "MC-148": [  # Brand Personality
   dict(kind="JOURNAL_ARTICLE", title_en="Dimensions of Brand Personality",
        title_fa="ابعاد شخصیت برند", authors="Aaker, J. L.", year=1997,
        publisher="Journal of Marketing Research, 34(3), 347-356", doi="10.1177/002224379703400304",
        url="https://journals.sagepub.com/doi/10.1177/002224379703400304", language="en", isbn=None,
        citation="Aaker, J. L. (1997). Dimensions of brand personality. Journal of Marketing Research, 34(3), 347-356.",
        locator="pp. 347-356", locator_type="page_range", supports="definition / five dimensions / measurement", verified=True),
   dict(kind="JOURNAL_ARTICLE", title_en="Consumers and Their Brands: Developing Relationship Theory in Consumer Research",
        title_fa="مصرف‌کنندگان و برندهایشان: توسعهٔ نظریهٔ رابطه در پژوهش مصرف", authors="Fournier, S.", year=1998,
        publisher="Journal of Consumer Research, 24(4), 343-373", doi=None, url=None, language="en", isbn=None,
        citation="Fournier, S. (1998). Consumers and their brands: Developing relationship theory in consumer research. Journal of Consumer Research, 24(4), 343-373.",
        locator="pp. 343-373", locator_type="page_range", supports="mechanism / brand as relationship partner", verified=False),
 ],
 "MC-149": [  # Attribution Theory
   dict(kind="BOOK", title_en="The Psychology of Interpersonal Relations",
        title_fa="روان‌شناسی روابط میان‌فردی", authors="Heider, F.", year=1958,
        publisher="New York: John Wiley & Sons", doi=None, url=None, language="en", isbn=None,
        citation="Heider, F. (1958). The psychology of interpersonal relations. John Wiley & Sons.",
        locator="whole work", locator_type="work", supports="origin / internal-external attribution", verified=True),
   dict(kind="JOURNAL_ARTICLE", title_en="An Attributional Theory of Achievement Motivation and Emotion",
        title_fa="نظریهٔ انتسابی انگیزش پیشرفت و هیجان", authors="Weiner, B.", year=1985,
        publisher="Psychological Review, 92(4), 548-573", doi=None, url=None, language="en", isbn=None,
        citation="Weiner, B. (1985). An attributional theory of achievement motivation and emotion. Psychological Review, 92(4), 548-573.",
        locator="pp. 548-573", locator_type="page_range", supports="evolution / dimensions of causality", verified=False),
 ],
}

ENRICH = {
 "MC-050": {
   "summary": "«روزنامه‌نگاری شهروندی» (Citizen Journalism) به فعالیت شهروندان غیرحرفه‌ای در گردآوری، تولید، تحلیل و انتشار خبر و اطلاعات اشاره دارد. شیمن بومن و کریس ویلیس در گزارش «We Media» (۲۰۰۳، مرکز رسانهٔ مؤسسهٔ مطبوعات آمریکا) این پدیده را در پیوند با فناوری‌های شبکه‌ای توصیف کردند که «مخاطب» را به مشارکت‌کنندهٔ فعال در فرایند خبر بدل می‌کنند (Bowman & Willis, 2003).",
   "main_problem": "وقتی ابزارهای تولید و انتشار خبر در دست همه قرار می‌گیرد، مرز میان روزنامه‌نگار حرفه‌ای و شهروند چه می‌شود، و این مشارکت چه فرصت‌ها و چه مخاطراتی برای دقت، اعتبار و دموکراسی خبری ایجاد می‌کند؟",
   "mechanism": "روزنامه‌نگاری شهروندی بر سه سازوکار استوار است: (۱) «کاهش موانع تولید» — دوربین موبایل، وبلاگ و شبکه‌های اجتماعی هزینهٔ گزارش‌گری را به‌شدت پایین آورده‌اند و فرد حاضر در صحنه می‌تواند پیش از رسانه‌های رسمی خبر را منتشر کند؛ (۲) «منطق مشارکتی» — محتوا در چرخه‌ای از انتشار، بازنشر، نقد و تکمیل توسط دیگران شکل می‌گیرد و رسانهٔ حرفه‌ای گاه نقش تسهیل‌گر یا صحت‌سنج این جریان را می‌پذیرد؛ (۳) «اقتصاد توجه و مشروعیت» — محتوای شهروندی وقتی به رسانه‌های بزرگ راه می‌یابد، هم دیده‌شدن می‌گیرد و هم با معیارهای حرفه‌ای سنجیده می‌شود (Bowman & Willis, 2003). دن گیل‌مور (Gillmor, 2004) این وضعیت را با تعبیر «مخاطب پیشین» (former audience) صورت‌بندی کرد: مخاطبی که دیگر مصرف‌کنندهٔ صرف نیست و در تولید خبر شریک است.",
   "assumptions": [
     "دسترسی به فناوری تولید و انتشار، مشارکت شهروندان در خبر را ممکن و گسترده می‌کند.",
     "شهروند حاضر در صحنه می‌تواند اطلاعاتی فراهم کند که رسانهٔ حرفه‌ای به آن دسترسی ندارد.",
     "مشارکت مخاطب، ارزش خبری و دموکراتیک تازه‌ای به فرایند اطلاع‌رسانی می‌افزاید."
   ],
   "principles": [
     "مشارکت‌محوری: مخاطب از مصرف‌کننده به تولیدکننده و توزیع‌کنندهٔ خبر بدل می‌شود.",
     "سرعت و حضور میدانی: شهروند اغلب پیش از رسانهٔ رسمی در صحنه حاضر است.",
     "هم‌آفرینی با رسانهٔ حرفه‌ای: اعتبار محتوای شهروندی معمولاً در گفت‌وگو با نهادهای خبری سنجیده می‌شود."
   ],
   "critiques": [
     "مسئلهٔ صحت‌سنجی: فقدان سازوکار تحریریه‌ای و راستی‌آزمایی، خطر انتشار اطلاعات نادرست را افزایش می‌دهد.",
     "کار بدون مزد و شکنندگی: بخشی از کار شهروندی بر دوش افراد بدون حمایت شغلی و حقوقی می‌افتد و می‌تواند به استثمار کار خبری بینجامد.",
     "سیاست برچسب: واژهٔ «شهروند» خود محل مناقشه است، زیرا مرز میان مشارکت دموکراتیک و روزنامه‌نگاری حرفه‌ای را مبهم می‌کند.",
   ],
   "applications": [
     "پوشش رخدادهایی که رسانه‌های رسمی به آن‌ها دسترسی ندارند (اعتراضات، بحران‌ها، مناطق دورافتاده).",
     "راهبرد رسانه‌های حرفه‌ای برای جلب مشارکت مخاطب و اعتبارسنجی محتوای کاربر.",
     "آموزش سواد خبری و رسانه‌ای برای ارزیابی محتوای شهروندی.",
   ],
   "evolution": "اصطلاح «We Media» در گزارش بومن و ویلیس (2003) رواج یافت و گیل‌مور (2004) آن را با تأکید بر وبلاگ‌ها و «مخاطب پیشین» گسترش داد. در دههٔ ۲۰۱۰، شبکه‌های اجتماعی و پلتفرم‌های ویدیویی کوتاه، روزنامه‌نگاری شهروندی را به جریان اصلی خبر بدل کردند و هم‌زمان بحث دربارهٔ اطلاعات نادرست و «روزنامه‌نگاری پلتفرمی» را برجسته ساختند.",
   "key_concepts": ["روزنامه‌نگاری شهروندی (citizen journalism)", "ما رسانه‌ایم (we media)", "مخاطب پیشین (former audience)", "روزنامه‌نگاری مشارکتی (participatory journalism)", "محتوای کاربرساخته (user-generated content)"],
   "studies": ["Bowman, S., & Willis, C. (2003). We Media. The Media Center at the American Press Institute.", "Gillmor, D. (2004). We the Media. O'Reilly Media."],
 },
 "MC-056": {
   "summary": "«حاکمیت داده» (Data Sovereignty) به صلاحیت و اقتدار یک واحد سیاسی یا جمعی بر داده‌ها اشاره دارد: اینکه داده در قلمرو چه کسی ذخیره، پردازش و کنترل می‌شود و قوانین کدام حوزه بر آن حاکم است. کوتور و توپن در مقالهٔ «What Does the Notion of “Sovereignty” Mean When Referring to the Digital?» (۲۰۱۹، New Media & Society) نشان دادند این مفهوم در دست‌کم سه معنای متفاوت به کار می‌رود (Couture & Toupin, 2019).",
   "main_problem": "در فضایی که داده از مرزهای ملی می‌گذرد و زیرساخت آن در اختیار شرکت‌های فراملی است، «حاکمیت» بر داده دقیقاً به چه معناست، چه کسی صاحب آن است، و چگونه می‌توان اقتدار حقوقی و کنترل فنی را بر داده اعمال کرد؟",
   "mechanism": "کوتور و توپن سه برداشت را از هم تفکیک می‌کنند: (۱) «حاکمیت دولتی بر داده» — دولت‌ها با قوانین محلی‌سازی داده، الزام نگهداری درون‌مرزی و کنترل دسترسی، اقتدار سرزمینی خود را بر داده‌های شهروندان و نهادها اعمال می‌کنند و در برابر دسترسی فرامرزی (مانند احضار داده توسط دولت‌های دیگر) مقاومت می‌کنند؛ (۲) «حاکمیت دادهٔ بومی» (indigenous data sovereignty) — جوامع بومی حق تعیین شیوهٔ گردآوری، مالکیت و استفاده از داده‌های مربوط به خود را مطالبه می‌کنند و حاکمیت را از دولت به اجتماع منتقل می‌سازند؛ (۳) «حاکمیت دادهٔ شخصی» — افراد بر داده‌های مربوط به خود حق کنترل و رضایت مطالبه می‌کنند (Couture & Toupin, 2019). سازوکار مشترک هر سه، پیوند «مالکیت/کنترل» با «قلمرو و اقتدار» است: داده به‌عنوان دارایی و به‌عنوان موضوع حق، نیازمند مرجعی است که مرزهای دسترسی و استفاده را تعیین کند. این چارچوب توضیح می‌دهد چرا قوانین حمایت از داده (مانند GDPR)، اختلافات حقوقی فرامرزی و سیاست‌های «حاکمیت دیجیتال» همگی حول یک پرسش واحد می‌چرخند: اقتدار نهایی بر داده از آنِ کیست؟",
   "assumptions": [
     "داده منبعی ارزشمند و قابل تملک یا کنترل است که پرسش اقتدار بر آن معنا دارد.",
     "مرزهای حقوقی و سرزمینی، حتی در فضای دیجیتال، همچنان بر دسترسی به داده اثر می‌گذارند.",
     "حاکمیت بر داده می‌تواند در سطوح مختلف (دولت، جامعهٔ بومی، فرد) مطالبه شود."
   ],
   "principles": [
     "پیوند داده و قلمرو: محل ذخیره و پردازش داده، پرسش صلاحیت حقوقی را تعیین می‌کند.",
     "تعدد سطح حاکمیت: دولت، اجتماع و فرد هر یک مدعی اقتدار بر داده‌اند.",
     "کنترل به‌جای مالکیت صرف: حاکمیت داده بیش از مالکیت، دربارهٔ حق تعیین شرایط دسترسی و استفاده است."
   ],
   "critiques": [
     "ابهام مفهومی: «حاکمیت» در فضای دیجیتال معنای کلاسیک وستفالیایی خود را از دست می‌دهد و کاربرد آن گاه شعارگونه است.",
     "تنش با جریان آزاد اطلاعات: محلی‌سازی داده می‌تواند به تجزیهٔ اینترنت، افزایش هزینه و محدودیت نوآوری بینجامد.",
     "نابرابری قدرت: حاکمیت داده در عمل اغلب به نفع دولت‌ها و شرکت‌های بزرگ و به زیان کاربران و جوامع کم‌توان اعمال می‌شود."
   ],
   "applications": [
     "تحلیل قوانین محلی‌سازی داده و اختلافات حقوقی فرامرزی بر سر دسترسی به داده.",
     "سیاست‌گذاری حفاظت از داده‌های شخصی و طراحی سازوکارهای رضایت و کنترل کاربر.",
     "پژوهش دربارهٔ حاکمیت دادهٔ بومی و حقوق جمعی جوامع بر داده‌های خود.",
   ],
   "evolution": "بحث حاکمیت داده با رشد رایانش ابری و جریان فرامرزی داده در دههٔ ۲۰۱۰ جدی شد. کوتور و توپن (2019) سه معنای آن را نظام‌مند کردند و پوهله و تیل (2020) مفهوم گسترده‌تر «حاکمیت دیجیتال» را در گفتمان سیاست اروپا تحلیل کردند. امروز حاکمیت داده به هستهٔ مناقشه‌های حقوقی، تجاری و امنیتی میان دولت‌ها و پلتفرم‌ها بدل شده است.",
   "key_concepts": ["حاکمیت داده (data sovereignty)", "حاکمیت دیجیتال (digital sovereignty)", "محلی‌سازی داده (data localization)", "حاکمیت دادهٔ بومی (indigenous data sovereignty)", "قلمرو حقوقی داده (data jurisdiction)"],
   "studies": ["Couture, S., & Toupin, S. (2019). What does the notion of \u201csovereignty\u201d mean when referring to the digital? New Media & Society, 21(10), 2305-2322.", "Pohle, J., & Thiel, T. (2020). Digital sovereignty. Internet Policy Review, 9(4)."],
 },
 "MC-148": {
   "summary": "«شخصیت برند» (Brand Personality) به مجموعه‌ای از ویژگی‌های انسانی اطلاق می‌شود که به یک برند نسبت داده می‌شود. جنیفر آکر در مقالهٔ «Dimensions of Brand Personality» (۱۹۹۷، Journal of Marketing Research) با تحلیل مقیاس‌های روان‌سنجی، پنج بُعد شخصیت برند را شناسایی کرد: صداقت، هیجان، شایستگی، پیچیدگی و سخت‌کوشی (Aaker, 1997).",
   "main_problem": "چگونه می‌توان ویژگی‌های انسانی را به‌طور نظام‌مند به برندها نسبت داد و سنجید، و این شخصیت چگونه بر ترجیح، وفاداری و تمایز برند در بازارهای اشباع اثر می‌گذارد؟",
   "mechanism": "مکانیسم بر «انسان‌انگاری» (anthropomorphism) استوار است: مصرف‌کنندگان برند را مانند یک شخص ادراک می‌کنند و به آن ویژگی‌های شخصیتی نسبت می‌دهند، حتی وقتی برند فاقد spokesperson انسانی است. آکر این سازه را با مقیاسی ۴۲-آیتمی و در قالب پنج بُعد عملیاتی کرد: «صداقت» (sincerity: صادق، صمیمی، اصیل)، «هیجان» (excitement: جسور، پرانرژی، به‌روز)، «شایستگی» (competence: قابل‌اعتماد، هوشمند، موفق)، «پیچیدگی» (sophistication: مجلل، جذاب) و «سخت‌کوشی» (ruggedness: سرسخت، در فضای باز) (Aaker, 1997). شخصیت برند از چند مسیر اثر می‌گذارد: (۱) «تمایز» — در دسته‌هایی که محصولات از نظر کارکردی شبیه‌اند، شخصیت راه تمایز است؛ (۲) «هم‌خوانی با خود» (self-congruity) — مصرف‌کنندگان برندی را ترجیح می‌دهند که با خودِ واقعی یا آرمانی‌شان هم‌خوان باشد؛ (۳) «رابطهٔ برند-مصرف‌کننده» — فورنیه (Fournier, 1998) نشان داد شخصیت برند بستر شکل‌گیری رابطه‌ای شبه‌میان‌فردی (اعتماد، تعهد، صمیمیت) میان مصرف‌کننده و برند است.",
   "assumptions": [
     "مصرف‌کنندگان برندها را به‌صورت انسان‌وار ادراک می‌کنند و به آن‌ها ویژگی شخصیتی نسبت می‌دهند.",
     "شخصیت برند سازه‌ای قابل اندازه‌گیری با ابزارهای روان‌سنجی است.",
     "هم‌خوانی شخصیت برند با خودپندارهٔ مصرف‌کننده، ترجیح و وفاداری را افزایش می‌دهد."
   ],
   "principles": [
     "پنج بُعد: صداقت، هیجان، شایستگی، پیچیدگی و سخت‌کوشی ابعاد اصلی شخصیت برندند.",
     "تمایز کارکردی-نمادین: شخصیت برند ابزار تمایز نمادین در بازارهای اشباع است.",
     "هم‌خوانی خود: جذابیت برند تابع تناسب شخصیت آن با خودپندارهٔ مصرف‌کننده است."
   ],
   "critiques": [
     "وابستگی فرهنگی: مقیاس اولیه بر داده‌های آمریکای شمالی استوار است و ابعاد آن در فرهنگ‌های دیگر (مانند ژاپن و اسپانیا) تفاوت نشان می‌دهد.",
     "اعتبار پیش‌بین: برخی پژوهش‌ها قدرت پیش‌بینی شخصیت برند برای رفتار واقعی خرید را محدودتر از انتظار یافته‌اند.",
     "ابهام مفهومی: مرز شخصیت برند با تصویر برند و هویت برند گاه مبهم می‌شود و تعریف‌ها هم‌پوشانی دارند."
   ],
   "applications": [
     "طراحی و بازطراحی هویت برند و تعیین جایگاه نمادین در بازار.",
     "تحقیقات بازاریابی برای سنجش ادراک مصرف‌کننده از برند در مقایسه با رقبا.",
     "هم‌سوسازی پیام تبلیغاتی با ویژگی‌های شخصیتی هدف‌مند برند."
   ],
   "evolution": "آکر (1997) مقیاس شخصیت برند را تثبیت کرد. در دو دههٔ بعد، نسخه‌های بین‌فرهنگی (آکر و همکاران) و انتقادهای روان‌سنجی به آن افزوده شد و مفهوم با نظریهٔ رابطهٔ برند (فورنیه، 1998) و برندسازی اجتماعی در شبکه‌های اجتماعی پیوند خورد.",
   "key_concepts": ["شخصیت برند (brand personality)", "انسان‌انگاری (anthropomorphism)", "هم‌خوانی با خود (self-congruity)", "ابعاد پنج‌گانهٔ آکر (Aaker's five dimensions)", "رابطهٔ برند-مصرف‌کننده (brand relationship)"],
   "studies": ["Aaker, J. L. (1997). Dimensions of brand personality. Journal of Marketing Research, 34(3), 347-356.", "Fournier, S. (1998). Consumers and their brands. Journal of Consumer Research, 24(4), 343-373."],
 },
 "MC-149": {
   "summary": "«نظریهٔ انتساب» (Attribution Theory) توضیح می‌دهد افراد چگونه علت رخدادها و رفتارها را به عوامل درونی (ویژگی‌های شخص، نیت) یا بیرونی (موقعیت، فشار محیطی) نسبت می‌دهند. فریتس هایدر در کتاب «The Psychology of Interpersonal Relations» (۱۹۵۸، Wiley) پایهٔ این نظریه را با مفهوم «روان‌شناسی عامیانه» (naive psychology) گذاشت (Heider, 1958).",
   "main_problem": "مردم چگونه علت‌ها را استنباط می‌کنند، چه سوگیری‌هایی در این استنباط رخ می‌دهد، و این انتساب‌ها چگونه بر احساس، قضاوت و رفتار بعدی آن‌ها اثر می‌گذارد؟",
   "mechanism": "هایدر دوگانگی بنیادین «نیروی شخصی» در برابر «نیروی محیطی» را مطرح کرد: رفتار را می‌توان به توانایی و انگیزهٔ فرد (can و try) یا به شرایط و فشار موقعیت نسبت داد (Heider, 1958). هارولد کلی (۱۹۶۷) با «مدل هم‌تغییری» (covariation) نشان داد افراد برای داوری علت، سه بُعد اطلاعاتی را می‌سنجند: «توافق» (consensus — آیا دیگران هم چنین رفتار می‌کنند؟)، «تمایز» (distinctiveness — آیا فرد در موقعیت‌های دیگر متفاوت رفتار می‌کند؟) و «ثبات» (consistency — آیا رفتار در زمان تکرار می‌شود؟). برنارد واینر (Weiner, 1985) سپس انتساب را به هیجان و انگیزش پیوند زد و سه بُعد «جایگاه» (locus)، «پایداری» (stability) و «کنترل‌پذیری» (controllability) را معرفی کرد: انتساب شکست به عامل درونی، پایدار و کنترل‌پذیر (مانند تنبلی) به شرم و کاهش تلاش می‌انجامد، در حالی که انتساب به عامل بیرونی یا کنترل‌ناپذیر (مانند بدشانسی) کمتر چنین اثری دارد. سواگیری شناخته‌شدهٔ این حوزه «خطای بنیادین انتساب» است: گرایش به تبیین رفتار دیگران با ویژگی‌های شخصی و نادیده‌گرفتن موقعیت.",
   "assumptions": [
     "افراد به‌طور طبیعی در پی تبیین علّی رخدادها و رفتارها هستند.",
     "انتساب‌ها بر پایهٔ اطلاعات محدود و اغلب سوگیرانه شکل می‌گیرند.",
     "انتساب‌ها بر هیجان، قضاوت اخلاقی و رفتار بعدی اثر علّی دارند."
   ],
   "principles": [
     "دوگانگی درونی/بیرونی: علت‌ها به شخص یا به موقعیت نسبت داده می‌شوند.",
     "هم‌تغییری: داوری علّی بر پایهٔ توافق، تمایز و ثبات اطلاعات استوار است.",
     "پیوند انتساب-هیجان: نوع انتساب، احساس و انگیزهٔ بعدی را تعیین می‌کند."
   ],
   "critiques": [
     "تنوع فرهنگی: پژوهش‌های بین‌فرهنگی نشان دادند سوگیری‌های انتسابی، از جمله خطای بنیادین، در فرهنگ‌های جمع‌گرا کمتر دیده می‌شوند.",
     "سادگی مدل: مدل‌های اولیه انتساب را فرایندی عقلانی می‌انگارند، در حالی که انتساب‌های واقعی اغلب خودکار و عاطفی‌اند.",
     "کاربرد ایدئولوژیک: انتساب به ویژگی‌های فردی می‌تواند مسئولیت ساختاری را پنهان کند (مانند سرزنش قربانی)."
   ],
   "applications": [
     "تحلیل پوشش خبری و چارچوب‌بندی مسئولیت در رسانه (سرزنش قربانی، انتساب بحران).",
     "ارتباطات بحران: نظریه‌های انتساب‌محور شهرت سازمانی، واکنش عمومی به خطاهای سازمان را تبیین می‌کنند.",
     "طراحی پیام‌های سلامت و تبلیغات با هدف تغییر انتساب مخاطب از کنترل‌ناپذیر به کنترل‌پذیر."
   ],
   "evolution": "هایدر (1958) بنیان را نهاد و کلی (1967) مدل هم‌تغییری را افزود. واینر (1985) انتساب را به هیجان و انگیزش پیوند داد. در دهه‌های بعد، نظریهٔ انتساب به ارتباطات بحران، رسانه، آموزش و سلامت راه یافت و پژوهش‌های بین‌فرهنگی محدودیت‌های آن را روشن کردند.",
   "key_concepts": ["انتساب (attribution)", "جایگاه علّی درونی/بیرونی (locus of causality)", "خطای بنیادین انتساب (fundamental attribution error)", "مدل هم‌تغییری (covariation model)", "کنترل‌پذیری (controllability)"],
   "studies": ["Heider, F. (1958). The Psychology of Interpersonal Relations. John Wiley & Sons.", "Weiner, B. (1985). An attributional theory of achievement motivation and emotion. Psychological Review, 92(4), 548-573."],
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
    codes = ["MC-050", "MC-056", "MC-148", "MC-149"]
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
    print("BATCH40 THEORY DONE")

if __name__ == "__main__":
    main()
