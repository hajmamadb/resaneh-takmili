# -*- coding: utf-8 -*-
"""Batch 35 (THEORY): MC-383 & MC-502 Merchants of Attention (Wu 2016), MC-299 Sociotechnical
Imaginaries (Jasanoff & Kim 2015), MC-286 Platform Cooperativism (Scholz 2016).
All primary anchors web-verified 2026-11-16. Target: resaname_kb_final_inspect."""
import pymysql, json

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch35-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch35_theory.json"

S = {
 "MC-383": [  # Merchants of Attention
   dict(kind="BOOK", title_en="The Attention Merchants: The Epic Scramble to Get Inside Our Heads",
        title_fa="تاجران توجه: نبرد حماسی برای نفوذ به ذهن‌های ما", authors="Wu, T.", year=2016,
        publisher="New York: Alfred A. Knopf", doi=None, url=None, language="en", isbn=None,
        citation="Wu, T. (2016). The attention merchants: The epic scramble to get inside our heads. Alfred A. Knopf.",
        locator="whole work", locator_type="work", supports="definition / history / business model", verified=True),
   dict(kind="BOOK", title_en="The Attention Economy: Understanding the New Currency of Business",
        title_fa="اقتصاد توجه: درک ارز جدید کسب‌وکار", authors="Davenport, T. H., & Beck, J. C.", year=2001,
        publisher="Boston: Harvard Business School Press", doi=None, url=None, language="en", isbn=None,
        citation="Davenport, T. H., & Beck, J. C. (2001). The attention economy: Understanding the new currency of business. Harvard Business School Press.",
        locator="whole work", locator_type="work", supports="evolution / attention as scarce resource", verified=False),
 ],
 "MC-502": [  # Merchants of Attention (duplicate topic)
   dict(kind="BOOK", title_en="The Attention Merchants: The Epic Scramble to Get Inside Our Heads",
        title_fa="تاجران توجه: نبرد حماسی برای نفوذ به ذهن‌های ما", authors="Wu, T.", year=2016,
        publisher="New York: Alfred A. Knopf", doi=None, url=None, language="en", isbn=None,
        citation="Wu, T. (2016). The attention merchants: The epic scramble to get inside our heads. Alfred A. Knopf.",
        locator="whole work", locator_type="work", supports="definition / attention harvest cycle / mechanism", verified=True),
   dict(kind="BOOK", title_en="The Attention Economy: Understanding the New Currency of Business",
        title_fa="اقتصاد توجه: درک ارز جدید کسب‌وکار", authors="Davenport, T. H., & Beck, J. C.", year=2001,
        publisher="Boston: Harvard Business School Press", doi=None, url=None, language="en", isbn=None,
        citation="Davenport, T. H., & Beck, J. C. (2001). The attention economy: Understanding the new currency of business. Harvard Business School Press.",
        locator="whole work", locator_type="work", supports="evolution / attention scarcity", verified=False),
 ],
 "MC-299": [  # Sociotechnical Imaginaries
   dict(kind="BOOK", title_en="Dreamscapes of Modernity: Sociotechnical Imaginaries and the Fabrication of Power",
        title_fa="چشم‌اندازهای مدرنیته: تخیل‌های اجتماعی-فنی و برسازی قدرت",
        authors="Jasanoff, S., & Kim, S.-H. (Eds.)", year=2015,
        publisher="Chicago: University of Chicago Press", doi=None, url=None, language="en", isbn=None,
        citation="Jasanoff, S., & Kim, S.-H. (Eds.). (2015). Dreamscapes of modernity: Sociotechnical imaginaries and the fabrication of power. University of Chicago Press.",
        locator="whole work", locator_type="work", supports="definition / mechanism / case studies", verified=True),
   dict(kind="JOURNAL_ARTICLE", title_en="Containing the Atom: Sociotechnical Imaginaries and Nuclear Power in the United States and South Korea",
        title_fa="مهار اتم: تخیل‌های اجتماعی-فنی و انرژی هسته‌ای در ایالات متحده و کرهٔ جنوبی",
        authors="Jasanoff, S., & Kim, S.-H.", year=2009,
        publisher="Minerva, 47(2), 119-146", doi=None, url=None, language="en", isbn=None,
        citation="Jasanoff, S., & Kim, S.-H. (2009). Containing the atom: Sociotechnical imaginaries and nuclear power in the United States and South Korea. Minerva, 47(2), 119-146.",
        locator="pp. 119-146", locator_type="page_range", supports="origin / concept development", verified=False),
 ],
 "MC-286": [  # Platform Cooperativism
   dict(kind="BOOK", title_en="Platform Cooperativism: Challenging the Corporate Sharing Economy",
        title_fa="تعاونی‌گرایی پلتفرمی: به چالش کشیدن اقتصاد اشتراکی شرکتی",
        authors="Scholz, T.", year=2016,
        publisher="New York: Rosa Luxemburg Stiftung", doi=None,
        url="https://rosalux.nyc/wp-content/uploads/2020/11/RLS-NYC_platformcoop.pdf", language="en", isbn=None,
        citation="Scholz, T. (2016). Platform cooperativism: Challenging the corporate sharing economy. Rosa Luxemburg Stiftung.",
        locator="whole work", locator_type="work", supports="definition / principles / alternative model", verified=True),
   dict(kind="BOOK", title_en="Ours to Hack and to Own: The Rise of Platform Cooperativism",
        title_fa="از آنِ ما برای هک کردن و تملک: برآمدن تعاونی‌گرایی پلتفرمی",
        authors="Scholz, T., & Schneider, N. (Eds.)", year=2017,
        publisher="New York: OR Books", doi=None, url=None, language="en", isbn=None,
        citation="Scholz, T., & Schneider, N. (Eds.). (2017). Ours to hack and to own: The rise of platform cooperativism. OR Books.",
        locator="whole work", locator_type="work", supports="evolution / movement expansion", verified=False),
 ],
}

ENRICH = {
 "MC-383": {
   "summary": "«تاجران توجه» (Merchants of Attention) عنوان و چارچوب تحلیلی کتابی از تیم وو (۲۰۱۶، Alfred A. Knopf) است که تاریخ اقتصاد توجه را از روزنامه‌های پنی‌یک قرن نوزدهم تا پلتفرم‌های دیجیتال روایت می‌کند. وو نشان می‌دهد چگونه صناعتی شکل گرفت که محتوای رایگان یا ارزان تولید می‌کند تا «توجه» مخاطب را بگیرد و آن را به آگهی‌دهندگان بفروشد؛ به گفتهٔ او، توجه انسان به کالایی تبدیل شد که ارزش آن را بازار تعیین می‌کند (Wu, 2016).",
   "main_problem": "چرا و چگونه صنعت رسانه، «توجه» انسانی را به کالای اصلی خود تبدیل کرد، این الگوی کسب‌وکار چه پیامدهایی برای فرهنگ، سیاست و تجربهٔ فردی دارد، و چه نیروهایی در طول تاریخ آن را پیش برده یا مهار کرده‌اند؟",
   "mechanism": "وو چرخهٔ تکرارشوندهٔ «برداشت توجه» را توصیف می‌کند: (۱) تاجر توجه با محتوای رایگان یا ارزان — روزنامهٔ ارزان، رادیو، تلویزیون، شبکه‌های اجتماعی — مخاطب را جلب می‌کند؛ (۲) توجه گردآوری‌شده به آگهی‌دهنده فروخته می‌شود و منطق درآمدی بر پایهٔ «بیشترین توجه با کمترین هزینه» استوار می‌گردد؛ (۳) برای رشد درآمد، مرزهای عرفی و اخلاقی جابه‌جا می‌شوند — از ورود آگهی به حریم خصوصی خانه تا طراحی اعتیادآور پلتفرم‌ها. او نمونه‌هایی تاریخی مانند روزنامه‌های پنی‌یک، تبلیغات پتنت‌مدیسین، رادیو و تلویزیون تجاری آمریکا و در نهایت فیسبوک را در یک پیوستار تحلیلی می‌نشاند و «توجه» را به‌عنوان منبعی کمیاب و رقابتی صورتبندی می‌کند (Wu, 2016).",
   "assumptions": [
     "توجه انسانی منبعی کمیاب و رقابت‌پذیر است که می‌توان آن را گردآوری، اندازه‌گیری و فروخت.",
     "مدل کسب‌وکار مبتنی بر آگهی، به‌طور درونی به سمت گسترش مرزهای جلب توجه گرایش دارد.",
     "رسانه‌های تجاری، شکل و ریتم تجربهٔ فرهنگی و سیاسی را به سمت منطق توجه‌محور بازآرایی می‌کنند."
   ],
   "principles": [
     "توجه به‌عنوان کالا: ارزش رسانه از تعداد و کیفیت توجه جلب‌شده سنجیده می‌شود.",
     "چرخهٔ تکرارشونده: هر موج فناوری رسانه‌ای، چرخهٔ برداشت توجه را در مقیاسی بزرگ‌تر تکرار می‌کند.",
     "مقاومت مصرف‌کننده: در تاریخ، واکنش‌های عمومی و جنبش‌های اصلاح‌گر توانسته‌اند مرزهای برداشت توجه را محدود کنند."
   ],
   "critiques": [
     "روایت خطی و غرب‌محور: تاریخ وو عمدتاً بر تجربهٔ آمریکا متمرکز است و تنوع مسیرهای رسانه‌ای در دیگر بافت‌ها را کم‌رنگ می‌کند.",
     "کم‌توجهی ساختاری: تحلیل ممکن است نقش مقررات، مالکیت و سیاست‌گذاری را در برابر پویایی بازار و فناوری کم‌وزن کند.",
     "ابهام سنجش «توجه»: مفهوم توجه در سطح تجربی سیال است و پیوند آن با سنجه‌های تجاری و پیامدهای فرهنگی نیازمند تفکیک دقیق‌تر است."
   ],
   "applications": [
     "تحلیل اقتصاد سیاسی پلتفرم‌ها و مدل کسب‌وکار آگهی‌محور.",
     "مطالعهٔ تاریخ رسانه و تحول شکل‌های سرگرمی و تبلیغات.",
     "بحث دربارهٔ طراحی اعتیادآور، سلامت روان دیجیتال و سیاست‌های تنظیم تبلیغات."
   ],
   "evolution": "وو (2016) چارچوب تاریخی را برای فهم اقتصاد توجه معاصر ارائه کرد. پیش از آن، دیونپورت و بک (2001) «اقتصاد توجه» را به‌عنوان مدیریت کمیابی توجه در کسب‌وکار صورت‌بندی کرده بودند. پس از ۲۰۱۶، بحث تاجران توجه با ادبیات «اقتصاد نظارتی» و نقد طراحی اعتیادآور پیوند خورد و به سیاست‌گذاری دربارهٔ تبلیغات هدفمند و سلامت دیجیتال راه یافت.",
   "key_concepts": ["تاجر توجه (attention merchant)", "اقتصاد توجه (attention economy)", "توجه به‌عنوان کالا (attention as commodity)", "چرخهٔ برداشت توجه (attention harvest cycle)", "طراحی اعتیادآور (addictive design)"],
   "studies": ["Wu, T. (2016). The Attention Merchants. Alfred A. Knopf.", "Davenport, T. H., & Beck, J. C. (2001). The Attention Economy. Harvard Business School Press."],
 },
 "MC-502": {
   "summary": "«تجار توجه» (Merchants of Attention) اصطلاحی است که تیم وو در کتاب «The Attention Merchants» (۲۰۱۶، Alfred A. Knopf) برای بازیگران صنعتی به‌کار می‌برد که «توجه» انسان را می‌فروشند. استدلال محوری آن است که رسانهٔ تجاری مدرن، با ارائهٔ محتوای ارزان یا رایگان، توجه مخاطب را جذب و آن را به آگهی‌دهندگان می‌فروشد؛ در نتیجه توجه، به‌جای محتوا، کالای واقعی این صناعت است (Wu, 2016).",
   "main_problem": "تجار توجه چگونه تقاضای آگهی‌دهندگان و کمیابی توجه انسانی را به یک مدل کسب‌وکار پایدار تبدیل می‌کنند، و چه سازوکاری باعث می‌شود این مدل به‌طور مداوم مرزهای اخلاقی و حریم خصوصی را جابه‌جا کند؟",
   "mechanism": "این چارچوب مدل را در قالب یک زنجیرهٔ ارزش توضیح می‌دهد: (۱) «تولید جاذبه» (attraction production) — محتوای سرگرمی، خبر یا خدمات رایگان طراحی می‌شود تا بیشترین زمان و توجه را بگیرد؛ (۲) «اندازه‌گیری و بسته‌بندی» (measurement and packaging) — توجه مخاطب به سنجه‌های کمی (مخاطب، زمان، کلیک) تبدیل و در بازار آگهی بسته‌بندی می‌شود؛ (۳) «فروش به آگهی‌دهنده» (resale to advertisers) — آگهی‌دهنده برای دسترسی به این توجه پول می‌پردازد؛ (۴) «گسترش مرزها» (boundary expansion) — برای رشد درآمد، حوزه‌های تازه‌ای از زندگی روزمره و داده‌های شخصی وارد چرخه می‌شود. وو تأکید می‌کند این منطق در پلتفرم‌های دیجیتال به اوج خود می‌رسد، زیرا توجه را دقیق‌تر اندازه می‌گیرند و شخصی‌سازی آگهی را ممکن می‌سازند (Wu, 2016).",
   "assumptions": [
     "توجه انسانی کمیاب، محدود و قابل اندازه‌گیری است و می‌تواند در بازار مبادله شود.",
     "آگهی‌دهندگان حاضرند برای دسترسی هدفمند به توجه، هزینه بپردازند.",
     "رقابت بر سر توجه، انگیزهٔ ساختاری برای گسترش مرزهای جلب توجه و گردآوری داده است."
   ],
   "principles": [
     "کالایی‌شدن توجه: ارزش رسانه از توجه فروخته‌شده، نه از کیفیت محتوا، مشتق می‌شود.",
     "هم‌سویی محتوا با آگهی: شکل و محتوای رسانه به سمت حداکثرسازی زمان مواجهه بازطراحی می‌شود.",
     "گسترش تدریجی مرزها: هر دوره، حوزه‌ای تازه از زندگی را به بازار توجه وارد می‌کند."
   ],
   "critiques": [
     "تقلیل‌گرایی اقتصادی: تمرکز بر توجه ممکن است ابعاد فرهنگی، سیاسی و هویتی مصرف رسانه را نادیده بگیرد.",
     "نادیده‌گرفتن عاملیت مخاطب: مخاطب در این چارچوب بیشتر منبعی برای برداشت توجه دیده می‌شود تا کنشگری تفسیرگر.",
     "تعمیم تاریخی: برخی منتقدان می‌گویند روایت «تاجران توجه» بیش از حد بر تداوم تاریخی تأکید می‌کند و گسست‌های کیفی پلتفرم‌های داده‌محور را کم‌رنگ می‌سازد."
   ],
   "applications": [
     "تحلیل مدل درآمدی رسانه‌های اجتماعی و پیامدهای آن بر کیفیت خبر و گفت‌وگوی عمومی.",
     "پژوهش دربارهٔ تبلیغات هدفمند، حریم خصوصی و اقتصاد داده.",
     "سیاست‌گذاری دربارهٔ شفافیت الگوریتمی، طراحی اخلاقی و حمایت از سلامت روان دیجیتال."
   ],
   "evolution": "مفهوم در کتاب وو (2016) صورت‌بندی شد و در امتداد بحث «اقتصاد توجه» دیونپورت و بک (2001) قرار گرفت. پس از آن، با ادبیات «سرمایه‌داری نظارتی» و نقد اقتصاد آگهی پلتفرمی پیوند یافت و به مطالعات طراحی قانع‌کننده و سیاست‌های سلامت دیجیتال راه یافت.",
   "key_concepts": ["تاجر توجه (attention merchant)", "زنجیرهٔ ارزش توجه (attention value chain)", "تبلیغات هدفمند (targeted advertising)", "اقتصاد توجه (attention economy)", "گسترش مرزهای توجه (boundary expansion)"],
   "studies": ["Wu, T. (2016). The Attention Merchants. Alfred A. Knopf.", "Davenport, T. H., & Beck, J. C. (2001). The Attention Economy. Harvard Business School Press."],
 },
 "MC-299": {
   "summary": "«تخیل‌های اجتماعی-فنی» (Sociotechnical Imaginaries) مفهومی است که شیلا جاسانوف و سانگ-هیون کیم در کتاب «Dreamscapes of Modernity» (۲۰۱۵، University of Chicago Press) به‌صورت کتاب‌محور بسط دادند: «تصورات جمعی و نهادینه‌شده از آینده‌های مطلوب که با فهم مشترک از شکل زندگی اجتماعی و نظم اجتماعیِ دست‌یافتنی از طریق علم و فناوری زنده‌اند» (Jasanoff & Kim, 2015).",
   "main_problem": "چگونه تصورات جمعی دربارهٔ آیندهٔ مطلوب، مسیر توسعهٔ فناوری و سیاست‌گذاری را شکل می‌دهند، و چرا جوامع مختلف با فناوری‌های مشابه، مسیرها و پیامدهای متفاوتی را تجربه می‌کنند؟",
   "mechanism": "مفهوم بر سه خصیصه استوار است که در تعریف جاسانوف و کیم برجسته شده‌اند: (۱) «جمعی بودن» (collective) — تخیل اجتماعی-فنی محصول تصور مشترک گروه‌ها و نهادهاست، نه باور فردی؛ (۲) «نهادینه‌شدگی» (institutionally stabilized) — این تصورات در قوانین، سازمان‌ها، زیرساخت‌ها و بودجه‌ها تثبیت می‌شوند و از حالت آرزو به واقعیت نهادی می‌رسند؛ (۳) «اجرای عمومی» (publicly performed) — در گفتمان رسانه‌ای، سیاست و فرهنگ عمومی بازنمایی و بازتولید می‌شوند. جاسانوف و کیم با مقایسهٔ انرژی هسته‌ای در آمریکا و کرهٔ جنوبی نشان دادند که تخیل‌های متفاوت — «مهار خطر» در برابر «پیشرفت ملی» — دو مسیر نهادی و سیاسی متفاوت پدید آورد (Jasanoff & Kim, 2015).",
   "assumptions": [
     "تصورات جمعی دربارهٔ آینده، متغیری مستقل و اثرگذار در توسعهٔ فناوری است، نه صرفاً بازتاب منافع مادی.",
     "تخیل‌ها با نهادینه‌شدن در قوانین و زیرساخت‌ها، مسیرهای بعدی را محدود و ممکن می‌کنند.",
     "مقایسهٔ بین‌کشوری، روش مناسبی برای آشکارسازی تنوع تخیل‌های اجتماعی-فنی است."
   ],
   "principles": [
     "آینده‌محوری: تخیل‌ها تصویر آیندهٔ مطلوب را پیشاپیش در تصمیم‌های امروز وارد می‌کنند.",
     "نهادینه‌شدگی: تخیل‌ها فقط در ذهن نیستند؛ در سازمان‌ها و زیرساخت‌ها جسمیت می‌یابند.",
     "تنوع بافتی: فناوری مشابه در بافت‌های سیاسی و فرهنگی مختلف، تخیل‌ها و مسیرهای متفاوتی می‌سازد."
   ],
   "critiques": [
     "ابهام مفهومی: مرز تخیل اجتماعی-فنی با مفاهیم همسایگی چون «گفتمان»، «اسطورهٔ فناورانه» و «تصورات ذهنی» روشن نیست و خطر کشیدگی مفهوم وجود دارد.",
     "دشواری عملیاتی‌سازی: سنجش تجربی تخیل‌ها و تفکیک آن از نگرش عمومی یا سیاست رسمی، چالش روش‌شناختی جدی است.",
     "تمرکز بر نخبگان: تحلیل ممکن است تخیل‌های نهادینه و رسمی را بر تخیل‌های عامه، مقاومت و صداهای حاشیه‌ای مقدم بدارد."
   ],
   "applications": [
     "تحلیل سیاست‌گذاری فناوری‌های نوظهور مانند هوش مصنوعی، زیست‌فناوری و انرژی‌های تجدیدپذیر.",
     "مطالعهٔ رابطهٔ علم، فناوری و برسازی هویت ملی و قدرت دولتی.",
     "پژوهش دربارهٔ زیرساخت‌های دیجیتال و تصورات آینده در سیاست‌های داده و پلتفرم."
   ],
   "evolution": "مفهوم نخست در مقالهٔ جاسانوف و کیم (2009) دربارهٔ انرژی هسته‌ای صورت‌بندی شد و در کتاب ۲۰۱۵ به یک برنامهٔ پژوهشی گسترده در مطالعات علم و فناوری تبدیل شد. از آن پس در تحلیل سیاست فناوری، حکمرانی هوش مصنوعی، انرژی و سلامت به‌کار رفته و در ادبیات رسانه و زیرساخت دیجیتال نیز نفوذ کرده است.",
   "key_concepts": ["تخیل اجتماعی-فنی (sociotechnical imaginary)", "آیندهٔ مطلوب (desirable future)", "نهادینه‌شدگی (institutional stabilization)", "اجرای عمومی (public performance)", "برسازی هم‌آفرین (co-production)"],
   "studies": ["Jasanoff, S., & Kim, S.-H. (Eds.). (2015). Dreamscapes of Modernity. University of Chicago Press.", "Jasanoff, S., & Kim, S.-H. (2009). Containing the Atom. Minerva, 47(2), 119-146."],
 },
 "MC-286": {
   "summary": "«همکاری‌گرایی پلتفرمی» (Platform Cooperativism) چارچوبی است که تریبر شولتز در گزارش «Platform Cooperativism: Challenging the Corporate Sharing Economy» (۲۰۱۶، Rosa Luxemburg Stiftung) معرفی کرد. او استدلال می‌کند که اقتصاد «اشتراکی» شرکتی در واقع اقتصاد خدمات بر-demand با پیامدهای نابرابری‌زا است و بدیل آن، پلتفرم‌هایی است که مالکیت آن‌ها در دست کارگران و کاربران و بر پایهٔ اصول تعاونی اداره می‌شوند (Scholz, 2016).",
   "main_problem": "چگونه می‌توان از تمرکز مالکیت و قدرت در پلتفرم‌های سرمایه‌داری به مدلی رسید که درآمد، داده و حکمرانی پلتفرم را میان کارگران و کاربران توزیع کند، بدون آنکه کارایی و مقیاس فناورانه از دست برود؟",
   "mechanism": "شولتز سازوکار بدیل را در چند سطح توضیح می‌دهد: (۱) «مالکیت جمعی» (collective ownership) — پلتفرم متعلق به کارگران، تولیدکنندگان یا کاربران است و سود در میان آنان تقسیم می‌شود؛ (۲) «حکمرانی دموکراتیک» (democratic governance) — تصمیم‌های کلیدی از طریق سازوکارهای تعاونی و مشارکتی گرفته می‌شود، نه به‌صورت یک‌طرفه از سوی سرمایه‌گذار؛ (۳) «شفافیت و دادهٔ مشترک» (shared data and transparency) — داده و الگوریتم‌ها به‌عنوان منبع مشترک مدیریت می‌شوند؛ (۴) «پرداخت منصفانه و امنیت» (fair pay and security) — شرایط کار و حمایت‌های اجتماعی بازطراحی می‌شود. او نمونه‌هایی چون تعاونی‌های راننده، پلتفرم عکاسان و تعاونی‌های محلی را به‌عنوان مصداق‌های نوپا معرفی می‌کند و راهبرد «ترجمه و همانندسازی» (cloning) پلتفرم‌های موجود را برای ورود سریع‌تر به بازار پیشنهاد می‌دهد (Scholz, 2016).",
   "assumptions": [
     "مسئلهٔ اصلی پلتفرم‌ها فناوری نیست، بلکه الگوی مالکیت و توزیع ارزش است.",
     "کارگران و کاربران می‌توانند به‌طور مؤثر در حکمرانی پلتفرم مشارکت کنند.",
     "مدل تعاونی می‌تواند با طراحی مناسب، در رقابت با پلتفرم‌های سرمایه‌داری دوام بیاورد."
   ],
   "principles": [
     "مالکیت کاربر/کارگر: پلتفرم به‌عنوان دارایی مشترک، نه ابزار استخراج ارزش.",
     "حکمرانی دموکراتیک: تصمیم‌گیری جمعی و پاسخ‌گو در طراحی و سیاست‌های پلتفرم.",
     "پرداخت منصفانه و شفافیت: توزیع عادلانهٔ درآمد و دسترسی به دادهٔ مشترک."
   ],
   "critiques": [
     "مشکل مقیاس و شبکه: پلتفرم‌های تعاونی در جذب سرمایه و رقابت با اثر شبکه‌ای بازیگران مسلط با دشواری روبه‌رو هستند.",
     "پیچیدگی حکمرانی: تصمیم‌گیری جمعی می‌تواند کند و پرهزینه باشد و در شرایط بحرانی کارایی را کاهش دهد.",
     "خطر هم‌فرمایی: برخی نقدها هشدار می‌دهند که تعاونی‌گرایی پلتفرمی ممکن است بدون تغییر ساختار قدرت کلان، به الگویی اصلاح‌طلبانه و محدود تبدیل شود."
   ],
   "applications": [
     "طراحی و راه‌اندازی پلتفرم‌های تعاونی در حمل‌ونقل، خدمات خانگی، تولید محتوا و کشاورزی.",
     "سیاست‌گذاری برای حمایت از اقتصاد تعاونی دیجیتال و کار شایسته در پلتفرم‌ها.",
     "پژوهش دربارهٔ بدیل‌های اقتصاد پلتفرمی و مالکیت داده."
   ],
   "evolution": "شولتز (2016) مفهوم را به‌عنوان بدیل سیاست‌گذارانه برای «سرمایه‌داری پلتفرمی» طرح کرد. در سال‌های بعد، جنبش تعاونی‌گرایی پلتفرمی با کتاب «Ours to Hack and to Own» (2017) و شبکه‌های بین‌المللی تعاونی‌های دیجیتال گسترش یافت و به بحث‌های «اقتصاد پلتفرمی منصفانه» و «مالکیت داده» پیوند خورد.",
   "key_concepts": ["تعاونی‌گرایی پلتفرمی (platform cooperativism)", "مالکیت جمعی (collective ownership)", "حکمرانی دموکراتیک (democratic governance)", "سرمایه‌داری پلتفرمی (platform capitalism)", "همانندسازی پلتفرم (platform cloning)"],
   "studies": ["Scholz, T. (2016). Platform Cooperativism: Challenging the Corporate Sharing Economy. Rosa Luxemburg Stiftung.", "Scholz, T., & Schneider, N. (Eds.). (2017). Ours to Hack and to Own. OR Books."],
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
    codes = ["MC-383", "MC-502", "MC-299", "MC-286"]
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
    print("BATCH35 THEORY DONE")

if __name__ == "__main__":
    main()
