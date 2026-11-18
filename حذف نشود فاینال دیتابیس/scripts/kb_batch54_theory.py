# -*- coding: utf-8 -*-
"""Batch 54 (THEORY): MC-228 Synthetic Media and Deepfakes (Chesney & Citron 2019),
MC-231 Mediations (Martín-Barbero 1993), MC-232 Coloniality of Power (Quijano 2000),
MC-240 Provincializing Europe (Chakrabarty 2000). Anchors verified 2026-11-16."""
import pymysql, json

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch54-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch54_theory.json"

S = {
 "MC-228": [
   dict(kind="JOURNAL_ARTICLE", title_en="Deep Fakes: A Looming Challenge for Privacy, Democracy, and National Security",
        title_fa="جعل‌های عمیق: چالشی قریب‌الوقوع برای حریم خصوصی، دموکراسی و امنیت ملی",
        authors="Chesney, R., & Citron, D. K.", year=2019,
        publisher="California Law Review, 107(6), 1753-1820", doi="10.2307/26842025",
        url="https://www.californialawreview.org/print/deep-fakes-a-looming-challenge-for-privacy-democracy-and-national-security",
        language="en", isbn=None,
        citation="Chesney, R., & Citron, D. K. (2019). Deep fakes: A looming challenge for privacy, democracy, and national security. California Law Review, 107(6), 1753-1820.",
        locator="pp. 1753-1820", locator_type="page_range", supports="definition / harms taxonomy / liar's dividend", verified=True),
   dict(kind="JOURNAL_ARTICLE", title_en="The Emergence of Deepfake Technology: A Review",
        title_fa="پیدایش فناوری جعل عمیق: یک مرور",
        authors="Westerlund, M.", year=2019,
        publisher="Technology Innovation Management Review, 9(11), 39-52", doi=None, url=None, language="en", isbn=None,
        citation="Westerlund, M. (2019). The emergence of deepfake technology: A review. Technology Innovation Management Review, 9(11), 39-52.",
        locator="pp. 39-52", locator_type="page_range", supports="evolution / technical survey", verified=False),
 ],
 "MC-231": [
   dict(kind="BOOK", title_en="Communication, Culture and Hegemony: From the Media to Mediations",
        title_fa="ارتباطات، فرهنگ و هژمونی: از رسانه‌ها به میانجی‌گری‌ها",
        authors="Martín-Barbero, J.", year=1993, publisher="London: Sage", doi=None,
        url="https://archive.org/details/communicationcul0000mart", language="en", isbn="9780803984622",
        citation="Martín-Barbero, J. (1993). Communication, culture and hegemony: From the media to mediations. Sage.",
        locator="whole work", locator_type="work", supports="definition / from media to mediations", verified=True),
   dict(kind="JOURNAL_ARTICLE", title_en="A Latin American Perspective on Communication/Cultural Mediation",
        title_fa="دیدگاهی آمریکای لاتینی به میانجی‌گری ارتباطی/فرهنگی",
        authors="Martín-Barbero, J.", year=2006,
        publisher="Global Media and Communication, 2(3), 279-297", doi=None, url=None, language="en", isbn=None,
        citation="Martín-Barbero, J. (2006). A Latin American perspective on communication/cultural mediation. Global Media and Communication, 2(3), 279-297.",
        locator="pp. 279-297", locator_type="page_range", supports="evolution / digital mediations", verified=False),
 ],
 "MC-232": [
   dict(kind="JOURNAL_ARTICLE", title_en="Coloniality of Power, Eurocentrism, and Latin America",
        title_fa="استعمار قدرت، اروپامحوری و آمریکای لاتین",
        authors="Quijano, A.", year=2000,
        publisher="Nepantla: Views from South, 1(3), 533-580", doi=None,
        url="https://muse.jhu.edu/article/23906", language="en", isbn=None,
        citation="Quijano, A. (2000). Coloniality of power, Eurocentrism, and Latin America. Nepantla: Views from South, 1(3), 533-580.",
        locator="pp. 533-580", locator_type="page_range", supports="definition / race as axis of power", verified=True),
   dict(kind="BOOK", title_en="Local Histories/Global Designs: Coloniality, Subaltern Knowledges, and Border Thinking",
        title_fa="تاریخ‌های محلی/طرح‌های جهانی: استعمار، دانش‌های فرودست و اندیشیدن مرزی",
        authors="Mignolo, W. D.", year=2000, publisher="Princeton, NJ: Princeton University Press", doi=None, url=None,
        language="en", isbn=None,
        citation="Mignolo, W. D. (2000). Local histories/global designs: Coloniality, subaltern knowledges, and border thinking. Princeton University Press.",
        locator="whole work", locator_type="work", supports="evolution / colonial matrix and border thinking", verified=False),
 ],
 "MC-240": [
   dict(kind="BOOK", title_en="Provincializing Europe: Postcolonial Thought and Historical Difference",
        title_fa="ولایتی‌کردن اروپا: اندیشهٔ پسااستعماری و تفاوت تاریخی",
        authors="Chakrabarty, D.", year=2000, publisher="Princeton, NJ: Princeton University Press", doi=None,
        url="https://press.princeton.edu/books/paperback/9780691130019/provincializing-europe",
        language="en", isbn="9780691130019",
        citation="Chakrabarty, D. (2000). Provincializing Europe: Postcolonial thought and historical difference. Princeton University Press.",
        locator="whole work", locator_type="work", supports="definition / critique of historicism", verified=True),
   dict(kind="JOURNAL_ARTICLE", title_en="Postcoloniality and the Artifice of History: Who Speaks for \"Indian\" Pasts?",
        title_fa="پسااستعمارگرایی و مصنوعیت تاریخ: چه کسی از گذشته‌های «هندی» سخن می‌گوید؟",
        authors="Chakrabarty, D.", year=1992,
        publisher="Representations, 37, 1-26", doi=None, url=None, language="en", isbn=None,
        citation="Chakrabarty, D. (1992). Postcoloniality and the artifice of history: Who speaks for \"Indian\" pasts? Representations, 37, 1-26.",
        locator="pp. 1-26", locator_type="page_range", supports="evolution / Europe as silent referent", verified=False),
 ],
}

ENRICH = {
 "MC-228": {
   "summary": "«رسانهٔ مصنوعی و جعل عمیق» (Synthetic Media and Deepfakes) به محتوای دیداری و شنیداری تولیدشده یا دستکاری‌شده با هوش مصنوعی اشاره دارد که چنان واقع‌نماست که تفکیک آن از واقعیت برای مخاطب دشوار است. رابرت چزنی و دنیل سایترون در «Deep Fakes» (۲۰۱۹، California Law Review) ابعاد حقوقی و اجتماعی این پدیده را تحلیل کردند (Chesney & Citron, 2019).",
   "main_problem": "وقتی ساخت ویدئو و صدای جعلی واقع‌نما ارزان و آسان می‌شود، چه خطرهایی برای حریم خصوصی، اعتبار افراد و دموکراسی پدید می‌آید، و حقوق و سیاست‌گذاری چگونه می‌توانند بدون آسیب به آزادی بیان پاسخ دهند؟",
   "mechanism": "چزنی و سایترون سه دستهٔ آسیب را از هم جدا می‌کنند: آسیب به «حریم خصوصی و کرامت» — به‌ویژه پورنوگرافی غیرتوافقی که در سال‌های نخست شایع‌ترین کاربرد جعل عمیق بود؛ آسیب به «اعتبار و آرامش» افراد و سازمان‌ها از طریق جعل اظهارات؛ و آسیب به «دموکراسی و امنیت ملی» از طریق اطلاعات نادرست و بی‌ثبات‌سازی (Chesney & Citron, 2019). سازوکار فنی بر شبکه‌های مولد رقیب (GAN) استوار است که با یادگیری از داده‌های واقعی، چهره و صدای شبه‌انسانی می‌سازند. مهم‌تر از خود جعل، «سود دروغ‌گو» (liar's dividend) است: در جهانی که جعل ممکن می‌شود، افراد بدکار می‌توانند شواهد واقعی را نیز «جعلی» بخوانند و اعتبار سند و تصویر را به‌طور کلی تضعیف کنند. وسترلوند (Westerlund, 2019) پیشرفت فنی جعل عمیق و رشد سریع ابزارهای آن را مرور کرده است. در بستر رسانه، این پدیده بحران «اصالت» (authenticity) می‌سازد: روزنامه‌نگاری که بر شواهد دیداری تکیه می‌کرد، باید سازوکارهای راستی‌آزمایی و «زنجیرهٔ اصالت» را بازتعریف کند، و اعتماد عمومی به تصویر و صدا — که قرن‌ها ستون شهادت رسانه‌ای بود — در معرض فرسایش قرار می‌گیرد.",
   "assumptions": [
     "فناوری جعل عمیق ارزان، سریع و در دسترس می‌شود.",
     "آسیب جعل عمیق فراتر از فرد به اعتماد عمومی می‌رسد.",
     "پاسخ حقوقی باید هدفمند باشد تا آزادی بیان آسیب نبیند."
   ],
   "principles": [
     "سه دستهٔ آسیب: حریم خصوصی، اعتبار و دموکراسی.",
     "سود دروغ‌گو: جعل، اعتبار شواهد واقعی را نیز تضعیف می‌کند.",
     "تنظیم هدفمند: قانون باید به آسیب مشخص بپردازد، نه فناوری را ممنوع کند."
   ],
   "critiques": [
     "اغراق تهدید: برخی پژوهش‌ها گسترهٔ اثر واقعی جعل عمیق را کمتر از ادعاها می‌دانند.",
     "مسابقهٔ تشخیص: ابزارهای تشخیص و تولید جعل در چرخهٔ دائمی‌اند و تشخیص قطعی دشوار است.",
     "تعارض با آزادی بیان: قوانین سخت می‌تواند به سانسور و طنز سیاسی آسیب بزند."
   ],
   "applications": [
     "تدوین سیاست راستی‌آزمایی و اصالت‌سنجی در تحریریه‌ها.",
     "پژوهش دربارهٔ اثر جعل عمیق بر اعتماد به خبر و شواهد.",
     "تحلیل حقوقی و سیاست‌گذاری محتوای مصنوعی."
   ],
   "evolution": "جعل عمیق از ۲۰۱۷ با انتشار ویدئوهای جعلی چهره‌ها شناخته شد؛ چزنی و سایترون (2019) چارچوب حقوقی آن را ارائه کردند و وسترلوند (2019) پیشرفت فنی را مرور کرد. در دههٔ ۲۰۲۰، هوش مصنوعی مولد، جعل صدا و ویدئو را به سطح تولید انبوه رساند.",
   "key_concepts": ["جعل عمیق (deepfake)", "رسانهٔ مصنوعی (synthetic media)", "سود دروغ‌گو (liar's dividend)", "شبکهٔ مولد رقیب (GAN)", "اصالت رسانه‌ای (media authenticity)"],
   "studies": ["Chesney, R., & Citron, D. K. (2019). Deep Fakes. California Law Review, 107(6), 1753-1820.", "Westerlund, M. (2019). The emergence of deepfake technology. TIM Review, 9(11), 39-52."],
 },
 "MC-231": {
   "summary": "«میانجی‌گری‌ها» (Mediations) رویکردی در مطالعات ارتباطات است که توجه را از «رسانه‌ها» به فرایندهای فرهنگی و اجتماعیِ واسطه‌گری معنا منتقل می‌کند: خانواده، محله، طبقه، سنت شفاهی و تجربهٔ روزمره. خسوس مارتین-باربرو در «Communication, Culture and Hegemony» (۱۹۹۳، Sage) این چرخش «از رسانه‌ها به میانجی‌گری‌ها» را صورت‌بندی کرد (Martín-Barbero, 1993).",
   "main_problem": "اگر تحلیل رسانه به مالکیت، ساختار و ایدئولوژی محدود بماند، چگونه می‌توان فهمید که مخاطبان واقعی چگونه معنا می‌سازند، و فرهنگ عامه چگونه در فرایند هژمونی مشارکت می‌کند؟",
   "mechanism": "مارتین-باربرو با تکیه بر نظریهٔ هژمونی گرامشی، نشان می‌دهد که معنا نه از رسانه به مخاطب «تزریق» می‌شود و نه صرفاً محصول ساختار اقتصادی است، بلکه در «میانجی‌گری‌ها» شکل می‌گیرد: ساختارهای فرهنگی و اجتماعی که تجربهٔ رسانه‌ای را واسطه‌گری می‌کنند — زندگی روزمره، زمان‌مندی اجتماعی، صلاحیت فرهنگی مخاطب و سنت‌های عامه (Martín-Barbero, 1993). او «نقشهٔ میانجی‌گری‌ها» را پیشنهاد می‌کند که رسانه را در شبکهٔ روابط اجتماعی و فرهنگی جای می‌دهد؛ فرهنگ عامه در این چارچوب نه دست‌نشاندهٔ رسانه، بلکه فضایی فعال برای مذاکره، مقاومت و بازتفسیر است. هژمونی نیز نه سلطهٔ یک‌سویه، بلکه فرایندی از مذاکره و رضایت است که در زندگی روزمره ساخته می‌شود. مارتین-باربرو (2006) این چارچوب را در عصر دیجیتال به «میانجی‌گری‌های ارتباطی/فرهنگی» گسترد. در بستر رسانه، این رویکرد پژوهش مخاطب را از سنجش اثر به مطالعهٔ معنا تغییر می‌دهد: تله‌نوولای آمریکای لاتین، موسیقی محلی و رسانه‌های جامعه‌ای نمونه‌هایی‌اند که در آن‌ها مخاطب با سرمایهٔ فرهنگی خود، معنای رسانه را بازآفرینی می‌کند و رسانه در همان حال در بازتولید یا به‌چالش‌کشیدن هژمونی نقش دارد.",
   "assumptions": [
     "معنا در تعامل رسانه و بافت فرهنگی-اجتماعی مخاطب ساخته می‌شود.",
     "فرهنگ عامه فضایی فعال برای مذاکره و مقاومت است.",
     "هژمونی فرایندی از رضایت و مذاکره است، نه سلطهٔ محض."
   ],
   "principles": [
     "از رسانه به میانجی‌گری: کانون تحلیل، فرایند واسطه‌گری معناست.",
     "صلاحیت فرهنگی: مخاطب با سرمایهٔ فرهنگی خود معنا می‌سازد.",
     "هژمونی مذاکره‌ای: رضایت در زندگی روزمره ساخته می‌شود."
   ],
   "critiques": [
     "دشواری عملیاتی‌سازی: مفهوم میانجی‌گری گسترده و سنجش تجربی آن دشوار است.",
     "کم‌رنگی قدرت ساختاری: تأکید بر مخاطب فعال ممکن است نابرابری ساختاری رسانه را کم‌رنگ کند.",
     "نحیفی تجربی: شواهد تجربی گسترده برای نقش میانجی‌گری‌ها محدود است."
   ],
   "applications": [
     "پژوهش مخاطب و دریافت در رسانه‌های محلی و منطقه‌ای.",
     "تحلیل فرهنگ عامه و رسانه‌های جامعه‌ای.",
     "مطالعهٔ معنا‌سازی مخاطب در بستر فرهنگی."
   ],
   "evolution": "مارتین-باربرو (1993) چارچوب را در آمریکای لاتین تثبیت کرد و (2006) آن را به میانجی‌گری دیجیتال گسترد. در دههٔ ۲۰۱۰-۲۰۲۰، مطالعات رسانهٔ دیجیتال و پلتفرمی، منطق میانجی‌گری را برای تحلیل تعامل و بستر بازتفسیر کرد.",
   "key_concepts": ["میانجی‌گری (mediation)", "نقشهٔ میانجی‌گری‌ها (map of mediations)", "هژمونی (hegemony)", "فرهنگ عامه (popular culture)", "صلاحیت فرهنگی (cultural competence)"],
   "studies": ["Martín-Barbero, J. (1993). Communication, Culture and Hegemony. Sage.", "Martín-Barbero, J. (2006). A Latin American perspective on communication/cultural mediation. Global Media and Communication, 2(3), 279-297."],
 },
 "MC-232": {
   "summary": "«استعمار قدرت» (Coloniality of Power) به الگوی پایدار قدرت اشاره دارد که پس از پایان استعمار رسمی نیز ادامه یافته است: طبقه‌بندی نژادی جمعیت جهان و حاکمیت شناختی اروپامحور که ساختار اقتصاد، دانش و فرهنگ جهانی را شکل داده است. آنیبال کیخانو در «Coloniality of Power, Eurocentrism, and Latin America» (۲۰۰۰، Nepantla) این مفهوم را صورت‌بندی کرد (Quijano, 2000).",
   "main_problem": "چرا پایان استعمار رسمی به پایان سلطهٔ معرفتی و نژادی نیانجامید، و چگونه می‌توان ریشه‌های استعماریِ ساختار قدرت جهانی را در اقتصاد، دانش و رسانه بازشناخت؟",
   "mechanism": "کیخانو استدلال می‌کند که با فتح آمریکا در ۱۴۹۲، «نژاد» به محور بنیادین قدرت جهانی بدل شد و طبقه‌بندی نژادی، تقسیم کار جهانی و سلسله‌مراتب دانش را سازمان داد (Quijano, 2000). او «استعمار» (استعمار رسمی) را از «استعمارگرایی قدرت» (coloniality) تفکیک می‌کند: دومی الگویی است که پس از استقلال سیاسی باقی می‌ماند و در نهادها، دانش، زبان و بازنمایی بازتولید می‌شود. اروپامحوری (Eurocentrism) نه صرفاً یک نگرش، بلکه ساختار معرفتی است که تاریخ جهان را از منظر اروپا روایت می‌کند و دیگر دانش‌ها را به حاشیه می‌راند. کیخانو همچنین بر «هم‌زمانی ناهمگون» (heterogeneity of time) تأکید می‌کند: جوامع استعمارشده هم‌زمان در چند زمانِ تاریخی زندگی می‌کنند. مینیولو (Mignolo, 2000) این چارچوب را به «ماتریس استعماری قدرت» و «اندیشیدن مرزی» (border thinking) گسترد: تفکر از مرزهای نظام استعماری، فضایی برای دانش فرودست فراهم می‌کند. در بستر رسانه، نظریه به تحلیل «استعمارگرایی دانش» در خبر می‌پردازد: چارچوب‌بندی رویدادها از منظر شمال جهانی، حاشیه‌رانی منابع و روایت‌های جنوب، و بازتولید سلسله‌مراتب نژادی و معرفتی در بازنمایی رسانه‌ای، همگی نمونه‌هایی از تداوم استعمار قدرت در قلمرو ارتباطات‌اند.",
   "assumptions": [
     "نژاد محور بنیادین ساختار قدرت جهانی از ۱۴۹۲ بوده است.",
     "استعمار قدرت پس از پایان استعمار رسمی پایدار می‌ماند.",
     "اروپامحوری ساختاری معرفتی است، نه فقط نگرشی فردی."
   ],
   "principles": [
     "تفکیک استعمار از استعمارگرایی قدرت.",
     "نژاد به‌عنوان محور تقسیم کار و دانش جهانی.",
     "اروپامحوری به‌عنوان ساختار معرفتی حاکم."
   ],
   "critiques": [
     "تمرکز بر نژاد: برخی منتقدان، نقش عوامل طبقاتی و اقتصادی را کم‌رنگ می‌بینند.",
     "گستردگی مفهوم: استعمار قدرت چنان موسع است که سنجش تجربی آن دشوار می‌شود.",
     "تمرکز منطقه‌ای: چارچوب عمدتاً از تجربهٔ آمریکای لاتین برخاسته و تعمیم آن نیازمند احتیاط است."
   ],
   "applications": [
     "تحلیل بازنمایی رسانه‌ای جنوب جهانی و سلسله‌مراتب خبری.",
     "پژوهش دربارهٔ استعمارگرایی دانش در مطالعات ارتباطات.",
     "نقد اروپامحوری در نظریه و آموزش رسانه."
   ],
   "evolution": "کیخانو (2000) مفهوم را تثبیت کرد و مینیولو (2000) ماتریس استعماری و اندیشیدن مرزی را افزود. در دههٔ ۲۰۱۰-۲۰۲۰، گروه «مدرنیته/استعمارگرایی» و مطالعات رسانهٔ استعماری، چارچوب را به ارتباطات و رسانه‌های دیجیتال گستردند.",
   "key_concepts": ["استعمار قدرت (coloniality of power)", "اروپامحوری (Eurocentrism)", "ماتریس استعماری (colonial matrix)", "اندیشیدن مرزی (border thinking)", "هم‌زمانی ناهمگون (heterogeneity of time)"],
   "studies": ["Quijano, A. (2000). Coloniality of power, Eurocentrism, and Latin America. Nepantla, 1(3), 533-580.", "Mignolo, W. D. (2000). Local Histories/Global Designs. Princeton University Press."],
 },
 "MC-240": {
   "summary": "«ولایتی‌کردن اروپا» (Provincializing Europe) به کوشش نظری برای «استانی‌کردن» اروپا — یعنی کنار گذاشتن جایگاه اروپا به‌عنوان مرجع جهانی تاریخ و اندیشه — اشاره دارد، بدون آنکه دستاوردهای فکری اروپایی یکسره رد شوند. دیپش چاکرابارتی در «Provincializing Europe» (۲۰۰۰، Princeton University Press) این پروژه را صورت‌بندی کرد (Chakrabarty, 2000).",
   "main_problem": "چگونه می‌توان تاریخ و اندیشهٔ غیراروپایی را بدون تکیه بر اروپا به‌عنوان «مرجع خاموش» همهٔ روایت‌ها نوشت، و آیا رهایی از تاریخ‌نگاری اروپامحور بدون رد کامل مفاهیم اروپایی ممکن است؟",
   "mechanism": "چاکرابارتی «تاریخ‌گرایی» (historicism) را نقد می‌کند: الگویی که اروپا را «مرجع خاموش» (silent referent) همهٔ تاریخ‌ها می‌داند و جوامع دیگر را در قالب روایت «گذار» به مدرنیتهٔ اروپایی می‌سنجد (Chakrabarty, 2000). پروژهٔ او نه رد اندیشهٔ اروپایی، بلکه «ولایتی‌کردن» آن است: نشان‌دادن اینکه مفاهیم اروپایی — مانند شهروندی، سرمایه و تاریخ — محصول تجربهٔ خاص اروپایی‌اند و نمی‌توان آن‌ها را بی‌واسطه جهان‌شمول فرض کرد. او برای این کار دو نوع تاریخ را از هم جدا می‌کند: «تاریخ ۱» (History 1) — تاریخ انتزاعی سرمایه و مدرنیته که گرایش به جهان‌شمولی دارد — و «تاریخ ۲» (History 2) — جهان‌های زیسته، تفاوت‌ها، خدایان و ارواح که در برابر فروکاست به تاریخ ۱ مقاومت می‌کنند. چاکرابارتی با مطالعهٔ تاریخ بنگال نشان می‌دهد که زندگی سیاسی مدرن هم‌زمان در هر دو تاریخ مشارکت دارد و نمی‌توان تفاوت را به «بازماندهٔ سنت» فروکاست. در بستر رسانه، این چارچوب به نقد تاریخ‌نگاری و نظریهٔ رسانه کمک می‌کند: روایت‌های خطی «گذار» به رسانهٔ مدرن، فرض اروپا به‌عنوان الگو، و حذف تجربه‌ها و دانش‌های غیرغربی از نظریهٔ ارتباطات، نمونه‌هایی از همان تاریخ‌گرایی‌اند که «ولایتی‌کردن اروپا» به چالش می‌کشد.",
   "assumptions": [
     "اروپا در تاریخ‌نگاری متعارف، مرجع خاموش همهٔ روایت‌هاست.",
     "مفاهیم اروپایی محصول تجربهٔ خاص‌اند و جهان‌شمول بدیهی نیستند.",
     "تفاوت فرهنگی و جهان زیسته به تاریخ انتزاعی فروکاستنی نیست."
   ],
   "principles": [
     "نقد تاریخ‌گرایی: اروپا الگوی جهان‌شمول نیست.",
     "ولایتی‌کردن نه ردکردن: مفاهیم اروپایی بومی‌سازی می‌شوند، نه حذف.",
     "دو تاریخ: تاریخ سرمایه در کنار تاریخ جهان‌های زیسته."
   ],
   "critiques": [
     "تناقض روش: استفاده از نظریهٔ اروپایی برای نقد اروپامحوری، مسئله‌دار است.",
     "خطر ذات‌گرایی: تأکید بر تفاوت می‌تواند به تصویری ذات‌گرا از فرهنگ غیرغربی بینجامد.",
     "انتزاع: زبان نظری پیچیده، کاربرد تجربی چارچوب را دشوار می‌کند."
   ],
   "applications": [
     "نقد تاریخ‌نگاری رسانه و روایت‌های خطی مدرنیزاسیون.",
     "پژوهش دربارهٔ نظریهٔ رسانهٔ غیرغربی و پسااستعماری.",
     "تحلیل بازنمایی تفاوت فرهنگی در رسانه."
   ],
   "evolution": "چاکرابارتی (1992) نقد «مرجع خاموش» را آغاز کرد و (2000) پروژهٔ ولایتی‌کردن را کامل کرد. در دههٔ ۲۰۱۰-۲۰۲۰، مطالعات رسانهٔ پسااستعماری و جهانی‌شدن نظریه، این چارچوب را برای نقد اروپامحوری در ارتباطات به‌کار گرفتند.",
   "key_concepts": ["ولایتی‌کردن اروپا (provincializing Europe)", "تاریخ‌گرایی (historicism)", "مرجع خاموش (silent referent)", "تاریخ ۱ و تاریخ ۲ (History 1 and 2)", "تفاوت تاریخی (historical difference)"],
   "studies": ["Chakrabarty, D. (2000). Provincializing Europe. Princeton University Press.", "Chakrabarty, D. (1992). Postcoloniality and the artifice of history. Representations, 37, 1-26."],
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
    codes = ["MC-228", "MC-231", "MC-232", "MC-240"]
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
    print("BATCH54 THEORY DONE")

if __name__ == "__main__":
    main()
