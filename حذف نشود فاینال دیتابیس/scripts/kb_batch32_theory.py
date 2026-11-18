# -*- coding: utf-8 -*-
"""Batch 32 (THEORY): MC-139 Soft Power (Nye 1990), MC-140 Public Diplomacy (Melissen 2005),
MC-141 Excellence Theory (Grunig & Hunt 1984), MC-142 Image Repair Theory (Benoit 1995).
All primary anchors web-verified 2026-11-16. Target: resaname_kb_final_inspect."""
import pymysql, json

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch32-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch32_theory.json"

S = {
 "MC-139": [  # Soft Power
   dict(kind="JOURNAL_ARTICLE", title_en="Soft Power",
        title_fa="قدرت نرم", authors="Nye, J. S., Jr.", year=1990,
        publisher="Foreign Policy, No. 80 (Autumn 1990), pp. 153-171", doi=None, url=None, language="en", isbn=None,
        citation="Nye, J. S., Jr. (1990). Soft power. Foreign Policy, 80(Autumn), 153-171.",
        locator="pp. 153-171", locator_type="page_range", supports="definition / origin / mechanism", verified=True),
   dict(kind="BOOK", title_en="Soft Power: The Means to Success in World Politics",
        title_fa="قدرت نرم: ابزار موفقیت در سیاست جهانی", authors="Nye, J. S., Jr.", year=2004,
        publisher="New York: PublicAffairs", doi=None, url=None, language="en", isbn=None,
        citation="Nye, J. S., Jr. (2004). Soft power: The means to success in world politics. PublicAffairs.",
        locator="whole work", locator_type="work", supports="evolution / operationalization", verified=False),
 ],
 "MC-140": [  # Public Diplomacy
   dict(kind="BOOK", title_en="The New Public Diplomacy: Soft Power in International Relations",
        title_fa="دیپلماسی عمومی نوین: قدرت نرم در روابط بین‌الملل", authors="Melissen, J. (Ed.)", year=2005,
        publisher="Basingstoke: Palgrave Macmillan", doi="10.1057/9780230554931",
        url="https://link.springer.com/book/10.1057/9780230554931", language="en", isbn=None,
        citation="Melissen, J. (Ed.). (2005). The new public diplomacy: Soft power in international relations. Palgrave Macmillan. https://doi.org/10.1057/9780230554931",
        locator="whole work", locator_type="work", supports="definition / new public diplomacy / dialogue model", verified=True),
   dict(kind="BOOK", title_en="The Cold War and the United States Information Agency: American Propaganda and Public Diplomacy, 1945-1989",
        title_fa="جنگ سرد و آژانس اطلاعات ایالات متحده: تبلیغات آمریکایی و دیپلماسی عمومی، ۱۹۴۵-۱۹۸۹", authors="Cull, N. J.", year=2008,
        publisher="Cambridge: Cambridge University Press", doi=None, url=None, language="en", isbn=None,
        citation="Cull, N. J. (2008). The Cold War and the United States Information Agency: American propaganda and public diplomacy, 1945-1989. Cambridge University Press.",
        locator="whole work", locator_type="work", supports="history / five core practices", verified=False),
 ],
 "MC-141": [  # Excellence Theory
   dict(kind="BOOK", title_en="Managing Public Relations",
        title_fa="مدیریت روابط عمومی", authors="Grunig, J. E., & Hunt, T.", year=1984,
        publisher="New York: Holt, Rinehart and Winston", doi=None, url=None, language="en", isbn="0030583373",
        citation="Grunig, J. E., & Hunt, T. (1984). Managing public relations. Holt, Rinehart and Winston.",
        locator="whole work", locator_type="work", supports="definition / four models / symmetrical model", verified=True),
   dict(kind="BOOK", title_en="Excellence in Public Relations and Communication Management",
        title_fa="برتری در روابط عمومی و مدیریت ارتباطات", authors="Grunig, J. E. (Ed.)", year=1992,
        publisher="Hillsdale, NJ: Lawrence Erlbaum Associates", doi=None, url=None, language="en", isbn=None,
        citation="Grunig, J. E. (Ed.). (1992). Excellence in public relations and communication management. Lawrence Erlbaum Associates.",
        locator="whole work", locator_type="work", supports="IABC Excellence Study / evolution", verified=False),
 ],
 "MC-142": [  # Image Repair Theory
   dict(kind="BOOK", title_en="Accounts, Excuses, and Apologies: A Theory of Image Restoration Strategies",
        title_fa="بهانه‌ها، توجیه‌ها و عذرخواهی‌ها: نظریهٔ راهبردهای ترمیم تصویر", authors="Benoit, W. L.", year=1995,
        publisher="Albany, NY: State University of New York Press", doi=None, url=None, language="en", isbn="0791421864",
        citation="Benoit, W. L. (1995). Accounts, excuses, and apologies: A theory of image restoration strategies. State University of New York Press.",
        locator="whole work", locator_type="work", supports="definition / typology / mechanism", verified=True),
   dict(kind="BOOK", title_en="Accounts, Excuses, and Apologies: Image Repair Theory and Research",
        title_fa="بهانه‌ها، توجیه‌ها و عذرخواهی‌ها: نظریه و پژوهش ترمیم تصویر", authors="Benoit, W. L.", year=2014,
        publisher="Albany, NY: State University of New York Press", doi=None, url=None, language="en", isbn=None,
        citation="Benoit, W. L. (2014). Accounts, excuses, and apologies: Image repair theory and research (2nd ed.). State University of New York Press.",
        locator="whole work", locator_type="work", supports="evolution / digital-era revisions", verified=False),
 ],
}

ENRICH = {
 "MC-139": {
   "summary": "«قدرت نرم» (Soft Power) مفهوم و نظریه‌ای است که جوزف نای جونیور در مقالهٔ «Soft Power» در نشریهٔ Foreign Policy (شمارهٔ ۸۰، پاییز ۱۹۹۰، صص. ۱۵۳-۱۷۱) صورت‌بندی کرد. نای در بستر مناظرهٔ آن سال‌ها دربارهٔ «افول آمریکا» استدلال کرد که قدرت در سیاست بین‌الملل تنها با زور و پول سنجیده نمی‌شود؛ کشوری می‌تواند نتیجهٔ دلخواه خود را «بی‌آنکه دیگران را وادار کند یا بپردازد» به دست آورد، اگر فرهنگ، ارزش‌های سیاسی و سیاست خارجی‌اش برای دیگران «جذاب» (attractive) و «مشروع» (legitimate) به نظر برسد (Nye, 1990).",
   "main_problem": "چرا برخی بازیگران بین‌المللی بی‌آنکه به ابزارهای نظامی یا اقتصادی متوسل شوند، همکاری داوطلبانهٔ دیگران را جلب می‌کنند، و «جذابیت» چگونه به منبعی قابل‌مدیریت برای سیاست خارجی و ارتباطات راهبردی تبدیل می‌شود؟",
   "mechanism": "نای مکانیسم قدرت نرم را در تقابل با «قدرت سخت» (hard power) صورت‌بندی می‌کند: (۱) قدرت سخت بر «قدرت فرمان» (command power) تکیه دارد، یعنی توانایی تغییر رفتار دیگران با اجبار نظامی، تحریم اقتصادی یا پرداخت؛ (۲) قدرت نرم بر «قدرت هم‌سوسازی» (co-optive power) استوار است، یعنی شکل‌دهی به ترجیحات دیگران تا آنچه شما می‌خواهید را خودشان بخواهند (Nye, 1990)؛ (۳) منابع سه‌گانهٔ قدرت نرم عبارت‌اند از فرهنگ (در جاهایی که جذاب است)، ارزش‌های سیاسی (در جاهایی که در داخل و خارج مشروع به نظر می‌رسند) و سیاست خارجی (در جاهایی که مشروع و اخلاقی تلقی می‌شود). کانال‌های انتقال این منابع، ارتباطات رسانه‌ای، تبادلات فرهنگی و آموزشی و دیپلماسی عمومی است. نای تأکید می‌کند جذابیت، برخلاف زور، «مالکیت‌پذیر» (possessive) نیست؛ نمی‌توان آن را به‌سادگی خرید یا دستور داد، و به همین دلیل مدیریت آن دشوارتر از قدرت سخت است.",
   "assumptions": [
     "رفتار بازیگران بین‌المللی تنها تابع محاسبهٔ هزینه-فایدهٔ مادی نیست و «ترجیحات» (preferences) آنان از طریق جذابیت شکل‌پذیر است.",
     "فرهنگ، ارزش‌ها و سیاست خارجی می‌توانند در شرایطی به «دارایی» (asset) تبدیل شوند، اما جذابیت آن‌ها زمینه‌مند و وابسته به ادراک مخاطب است.",
     "مشروعیت (legitimacy) در نظام بین‌الملل ارزشی مستقل دارد و کاهش هزینهٔ تعامل را برای بازیگر جذاب ممکن می‌کند."
   ],
   "principles": [
     "قدرت نرم مکمل قدرت سخت است، نه جانشین آن؛ نای بعدها ترکیب هوشمندانهٔ هر دو را «قدرت هوشمند» (smart power) نامید.",
     "منابع بالقوهٔ قدرت نرم با قدرت نرم واقعی یکی نیستند؛ تبدیل منابع به نتیجه، به پذیرش و ادراک مخاطب وابسته است.",
     "اعتبار (credibility) و صداقت، شرط پیشین اثربخشی قدرت نرم‌اند؛ تبلیغ یک‌سویه و ناهمخوانی گفتار و کردار آن را فرسایش می‌دهد."
   ],
   "critiques": [
     "سنجش‌پذیری: جذابیت یک سازهٔ ادراکی است و شاخص‌های کمی روشنی برای اندازه‌گیری آن وجود ندارد؛ ازاین‌رو فرضیه‌های قدرت نرم به‌سختی ابطال‌پذیر می‌شوند.",
     "آمیختگی منابع و رفتار: منتقدان می‌گویند نای «دارایی‌های بالقوه» و «اثر رفتاری واقعی» را در یک مفهوم جمع می‌کند و همین امر تحلیل تجربی را مخدوش می‌سازد.",
     "جدایی‌ناپذیری از قدرت سخت: در عمل، سرمایه‌گذاری فرهنگی و رسانه‌ای اغلب در سایهٔ توان اقتصادی و امنیتی معنا پیدا می‌کند و تفکیک تحلیلی این دو دشوار است؛ افزون بر این، خطر لغزش قدرت نرم به «تبلیغ» و «دستکاری» ادراکی وجود دارد."
   ],
   "applications": [
     "تحلیل دیپلماسی عمومی و رسانه‌ای دولت‌ها و سنجش «جذابیت» تصویر ملی در افکار عمومی جهانی.",
     "مطالعهٔ «برندسازی ملی» (nation branding) و دیپلماسی فرهنگی و آموزشی (بورس‌ها، زبان، تبادل دانشجو).",
     "ارزیابی راهبردی صنایع فرهنگی و رسانه‌های فرامرزی به‌عنوان ابزار نفوذ غیرقهری در سیاست خارجی."
   ],
   "evolution": "نای مفهوم را نخست در Foreign Policy (1990) و هم‌زمان در کتاب Bound to Lead (1990) مطرح کرد و سپس در Soft Power: The Means to Success in World Politics (2004) آن را عملیاتی‌تر ساخت و به سیاست‌گذاری پیوند داد. در دههٔ ۲۰۰۰ با طرح «قدرت هوشمند» (smart power) در گزارش کمیسیون CSIS (۲۰۰۷) و در آثار بعدی نای، این نظریه به چارچوبی برای ترکیب ابزارهای سخت و نرم در راهبرد کلان تبدیل شد. امروزه قدرت نرم در ادبیات دیپلماسی عمومی، برندسازی ملی، رسانه‌های فرامرزی و مطالعات جنگ نرم/نفوذ به‌کار می‌رود و منتقدان نیز بر سنجش‌پذیری و خطر تبدیل آن به تبلیغ تأکید دارند.",
   "key_concepts": ["قدرت نرم (soft power)", "قدرت سخت (hard power)", "قدرت هم‌سوسازی (co-optive power)", "جذابیت (attraction)", "قدرت هوشمند (smart power)"],
   "studies": ["Nye, J. S., Jr. (1990). Soft power. Foreign Policy, 80, 153-171.", "Nye, J. S., Jr. (2004). Soft Power: The Means to Success in World Politics. PublicAffairs."],
 },
 "MC-140": {
   "summary": "«دیپلماسی عمومی» (Public Diplomacy) به مجموعهٔ فعالیت‌های ارتباطی یک دولت برای تعامل مستقیم با افکار عمومی و جوامع مدنیِ کشورهای دیگر — به‌جای تعامل صرف با دولت‌ها — گفته می‌شود. این مفهوم در ۱۹۶۵ توسط ادموند گالیون در مدرسهٔ فلچر (دانشگاه تافتس) برای پرهیز از بار منفی واژهٔ «تبلیغات» صورت‌بندی شد و در دههٔ ۲۰۰۰ با کتاب «The New Public Diplomacy» به ویراستاری یان ملیسن (۲۰۰۵، Palgrave Macmillan) به الگوی «دیپلماسی عمومی نوین» ارتقا یافت: ارتباط دوسویه، گفت‌وگو و اعتمادسازی به‌جای پیام‌رسانی یک‌سویه (Melissen, 2005).",
   "main_problem": "دولت‌ها چگونه می‌توانند در محیط رسانه‌ای جهانیِ چندبازیگری، با افکار عمومی خارجی ارتباط برقرار کنند، تصویر و اعتبار خود را مدیریت کنند و بدون اتکا به تبلیغ یک‌سویه، همدلی و همکاری ایجاد کنند؟",
   "mechanism": "دیپلماسی عمومی نوین بر مکانیسم گفت‌وگوی دوسویه استوار است: (۱) «گوش دادن» (listening) به‌عنوان پیش‌شرط درک مخاطب، نه فقط ابزار اقناع؛ (۲) «هم‌آفرینی پیام» با بازیگران غیردولتی — دانشگاه‌ها، رسانه‌ها، بنیادها، هنرمندان و کاربران شبکه‌های اجتماعی — تا پیام از حالت دولتی و رسمی خارج شود؛ (۳) «ساختن رابطهٔ بلندمدت» (relationship building) و اعتماد، به‌جای تمرکز بر کمپین‌های کوتاه‌مدت (Melissen, 2005). نیکلاس کال (Cull, 2008) پنج فعالیت محوری را از هم تفکیک می‌کند: گوش دادن، حمایت‌گری/تبلیغ (advocacy)، دیپلماسی فرهنگی، دیپلماسی تبادلی و پخش بین‌المللی (international broadcasting). در این چارچوب، دیپلماسی عمومی حلقهٔ وصل «قدرت نرم» نای با عمل سیاست خارجی است: رسانه‌ها و فرهنگ، جذابیت را به ادراک مخاطب تبدیل می‌کنند.",
   "assumptions": [
     "افکار عمومی خارجی متغیری اثرگذار بر سیاست خارجی دولت‌ها است و می‌توان از طریق ارتباط مستقیم به آن دسترسی یافت.",
     "اعتبار منبع پیام شرط اثربخشی است؛ پیام دولتیِ صرف، کمتر از پیام بازیگران غیردولتی و مستقل باورپذیر است.",
     "ارتباط مؤثر دیپلماسی عمومی دوسویه و تدریجی است و در قالب رابطهٔ بلندمدت، نه کمپین تبلیغی، معنا می‌یابد."
   ],
   "critiques": [
     "پیوند ساختاری با تبلیغات دولتی: مرز میان دیپلماسی عمومی و پروپاگاندا در عمل مبهم است و این مفهوم می‌تواند پوششی برای مدیریت ادراک و دستکاری اطلاعات شود.",
     "شکاف اعتبار: وقتی گفتمان رسمی با رفتار واقعی دولت ناهمخوان باشد، تلاش‌های دیپلماسی عمومی به ضد خود تبدیل می‌شود.",
     "سنجش‌ناپذیری و تمرکز دولتی: اثرگذاری بلندمدت آن به‌سختی قابل ارزیابی است و الگوی «نوین» بیش از حد بر کنش دولت متمرکز می‌ماند، در حالی که در محیط پلتفرمی، کنشگران غیردولتی و حتی مخاطبان خصمانه نیز پیام‌سازند."
   ],
   "applications": [
     "طراحی راهبرد رسانه‌ای و فرهنگی کشورها برای بهبود تصویر ملی و تعامل با جوامع خارجی.",
     "تحلیل دیپلماسی رسانه‌ای در بحران‌ها و منازعات بین‌المللی (مدیریت شهرت و روایت).",
     "مطالعهٔ دیپلماسی دیجیتال و تعامل دولت‌ها با کاربران شبکه‌های اجتماعی فرامرزی."
   ],
   "evolution": "از صورت‌بندی گالیون (۱۹۶۵) و تجربهٔ آژانس اطلاعات آمریکا در جنگ سرد (که کال، ۲۰۰۸، آن را مستند کرده) تا «دیپلماسی عمومی نوین» ملیسن (۲۰۰۵) که بر دوسویگی و اعتماد تأکید کرد، و سپس «دیپلماسی دیجیتال» و «دیپلماسی عمومی شبکه‌ای» در دههٔ ۲۰۱۰. در ادبیات معاصر، دیپلماسی عمومی به‌عنوان بازوی اجرایی قدرت نرم و مکمل دیپلماسی رسمی در سیاست خارجی تحلیل می‌شود.",
   "key_concepts": ["دیپلماسی عمومی (public diplomacy)", "دیپلماسی عمومی نوین (new public diplomacy)", "گوش دادن (listening)", "دیپلماسی فرهنگی (cultural diplomacy)", "دیپلماسی دیجیتال (digital diplomacy)"],
   "studies": ["Melissen, J. (Ed.). (2005). The New Public Diplomacy: Soft Power in International Relations. Palgrave Macmillan.", "Cull, N. J. (2008). The Cold War and the United States Information Agency. Cambridge University Press."],
 },
 "MC-141": {
   "summary": "«نظریهٔ برتری» (Excellence Theory) چارچوب هنجاری و تجربیِ جیمز گرونیگ و تاد هانت در کتاب «Managing Public Relations» (۱۹۸۴، Holt, Rinehart and Winston) است که می‌کوشد مشخص کند روابط عمومی «چگونه باید باشد» تا به سازمان در تحقق اهدافش یاری رساند. هستهٔ نظریه، الگوی «دوسویهٔ متقارن» (two-way symmetrical) است: روابط عمومی برتر، ارتباطی دوسویه و متوازن میان سازمان و عمومی‌ها برقرار می‌کند و منافع هر دو طرف را در تصمیم‌گیری سازمان لحاظ می‌کند (Grunig & Hunt, 1984).",
   "main_problem": "چه نوعی از روابط عمومی — با چه الگو، ساختار و جایگاهی در سازمان — واقعاً اثربخش است، و چگونه می‌توان از الگوهای تبلیغی و یک‌سویه به ارتباط دوسویه و متقارن به‌عنوان معیار برتری گذار کرد؟",
   "mechanism": "نظریه چهار الگوی تاریخی روابط عمومی را از هم متمایز می‌کند: (۱) «تبلیغ و آگهی‌گری» (press agentry/publicity) با هدف صرفاً جلب توجه؛ (۲) «اطلاع‌رسانی عمومی» (public information) با هدف انتشار صادقانهٔ اطلاعات یک‌سویه؛ (۳) «دوسویهٔ نامتقارن» (two-way asymmetrical) که پژوهش را برای اقناع مخاطب به‌کار می‌گیرد؛ و (۴) «دوسویهٔ متقارن» (two-way symmetrical) که ارتباط را برای «درک متقابل» و سازش دوطرفه به‌کار می‌گیرد (Grunig & Hunt, 1984). الگوی چهارم، معیار هنجاری برتری است. مکانیسم تکمیلی، «نظریهٔ موقعیتی عمومی‌ها» (situational theory of publics) است: عمومی‌ها بر پایهٔ سه متغیر — تشخیص مسئله، تشخیص محدودیت و سطح درگیری — از «نهفته» (latent) به «آگاه» (aware) و «فعال» (active) حرکت می‌کنند و ارتباط مؤثر باید با همین منطق بخش‌بندی شود. در سطح سازمانی، برتری مستلزم آن است که روابط عمومی کارکردی «مدیریتی و راهبردی» باشد که به ائتلاف غالب سازمان مشاوره می‌دهد، نه صرفاً واحد فنی انتشار پیام.",
   "assumptions": [
     "ارتباط متقارن دوسویه، هم برای سازمان و هم برای عمومی‌ها سودمندتر از ارتباط یک‌سویه در بلندمدت است.",
     "عمومی‌ها را می‌توان بر اساس موقعیت (درگیری، تشخیص مسئله و محدودیت) بخش‌بندی و پیش‌بینی کرد.",
     "جایگاه راهبردی روابط عمومی در ساختار سازمان و دسترسی آن به ائتلاف غالب، تعیین‌کنندهٔ برتری است."
   ],
   "principles": [
     "برتری زمانی محقق می‌شود که روابط عمومی کارکردی مدیریتی باشد و در تصمیم‌گیری راهبردی سازمان مشارکت کند.",
     "الگوی دوسویهٔ متقارن، آرمان هنجاری است؛ سازمان‌های برتر در عمل ترکیبی از الگوها را به‌کار می‌گیرند اما به سمت تقارن حرکت می‌کنند.",
     "پژوهش و گوش دادن، بخشی از فرایند ارتباط‌اند، نه ابزاری برای اقناع یک‌سویه."
   ],
   "critiques": [
     "مرکزیت آمریکایی: داده‌های مطالعهٔ برتری عمدتاً از سازمان‌های آمریکای شمالی و اروپایی گردآوری شده و تعمیم آن به بافت‌های دیگر نیازمند احتیاط است.",
     "آرمان‌گرایی: منتقدان (از جمله ژاکلین لیتانگ و لارنس سووس) می‌گویند در عمل، روابط عمومی غالباً منافع سازمان را بر منافع عمومی مقدم می‌دارد و «تقارن» بیش از آنکه واقعیت باشد، آرزو است.",
     "نادیده‌گرفتن قدرت: نظریه به‌اندازهٔ کافی به نامتقارنی‌های ساختاری قدرت، منافع متعارض و نقش حمایت‌گری/وکالت (advocacy) نمی‌پردازد و تقارن را در محیط‌های متخاصم دشوار می‌سازد."
   ],
   "applications": [
     "ارزیابی و طراحی ساختار و کارکردهای واحدهای روابط عمومی و ارتباطات سازمانی.",
     "بخش‌بندی عمومی‌ها و طراحی راهبرد ارتباطی مبتنی بر نظریهٔ موقعیتی عمومی‌ها.",
     "پژوهش در مدیریت بحران، مسئولیت اجتماعی سازمان و ارتباطات زیست‌محیطی و سلامت."
   ],
   "evolution": "پس از بنیان‌گذاری در ۱۹۸۴، نظریه در «مطالعهٔ برتری» (Excellence Study) بنیاد پژوهشی IABC (۱۹۸۵-۱۹۹۱) به سرپرستی جیمز گرونیگ و با همکاری دیوید دوزیر و همکاران، به‌صورت تجربی آزموده و در Excellence in Public Relations and Communication Management (1992) و سپس Excellent Public Relations and Effective Organizations (2002) منتشر شد. در دهه‌های بعد، مکتب برتری با نقدهای پسااستعماری، بافتی و قدرت‌محور روبه‌رو شد و در نسخه‌های متأخرتر، بر «ارتباط متقارن با تصحیح انحراف» (symmetrical with tweaking) و ترکیب وکالت و همکاری تأکید شد.",
   "key_concepts": ["الگوی دوسویهٔ متقارن (two-way symmetrical model)", "عمومی‌های فعال (active publics)", "نظریهٔ موقعیتی عمومی‌ها (situational theory of publics)", "کارکرد مدیریتی (managerial function)", "ائتلاف غالب (dominant coalition)"],
   "studies": ["Grunig, J. E., & Hunt, T. (1984). Managing Public Relations. Holt, Rinehart and Winston.", "Grunig, J. E. (Ed.). (1992). Excellence in Public Relations and Communication Management. Lawrence Erlbaum Associates."],
 },
 "MC-142": {
   "summary": "«نظریهٔ ترمیم تصویر» (Image Repair Theory) اثر ویلیام بنوا (Benoit, 1995) تبیین می‌کند که فرد یا سازمان متهم به خطا، چگونه با راهبردهای گفتمانی می‌کوشد «تصویر» (image) خود را نزد مخاطب بازسازی کند. بنوا بر این پایه استوار است که «تصویر» سرمایه‌ای ادراکی است که با اتهام آسیب می‌بیند و ترمیم آن مستلزم پاسخ کلامی هدفمند است؛ او مجموعه‌ای از پنج راهبرد کلان و چهارده تاکتیک را برای این پاسخ صورتبندی کرده است (Benoit, 1995).",
   "main_problem": "هنگامی که تصویر یک بازیگر در افکار عمومی آسیب می‌بیند، چه راهبردهای ارتباطی برای دفاع، کاهش آسیب و بازسازی اعتماد در دسترس است و چه عواملی انتخاب میان آن‌ها را هدایت می‌کند؟",
   "mechanism": "بنوا دو پیش‌فرض عملیاتی دارد: اتهام، تصویر را تهدید می‌کند، و ارتباط کلامی می‌تواند تصویر را ترمیم کند. بر همین اساس، پنج راهبرد کلان و چهارده تاکتیک را از هم تفکیک می‌کند: (۱) «انکار» (denial) با دو تاکتیک انکار ساده و جابه‌جایی تقصیر؛ (۲) «گریز از مسئولیت» (evasion of responsibility) با چهار تاکتیک تحریک، انکار عاملیت (defeasibility)، تصادف و حسن نیت؛ (۳) «کاهش رنجش‌زایی» (reducing offensiveness) با شش تاکتیک پشتیبان‌گیری (bolstering)، کم‌نمایی، تمایزگذاری، تعالی (transcendence)، حمله به متهم‌کننده و جبران؛ (۴) «اقدام اصلاحی» (corrective action) برای رفع اشتباه و پیشگیری از تکرار؛ و (۵) «خودسرزنش‌گری» (mortification) یعنی پذیرش مسئولیت و عذرخواهی (Benoit, 1995). اثربخشی هر راهبرد به نوع اتهام، مخاطب و سابقهٔ تصویر بازیگر وابسته است؛ بنوا می‌گوید راهبردها معمولاً در ترکیب، نه به‌تنهایی، به‌کار می‌روند.",
   "assumptions": [
     "تصویر یک دارایی ادراکی است که با اتهام عمومی آسیب می‌بیند و ارزش حفاظت دارد.",
     "پاسخ کلامی می‌تواند ادراک مخاطب را تغییر دهد و بنابراین ابزار اصلی ترمیم است.",
     "اثربخشی راهبردها زمینه‌مند است و به ماهیت اتهام، اعتبار پیشین منبع و انتظارات مخاطب بستگی دارد."
   ],
   "critiques": [
     "توصیفی‌بودن بیش از حد: نظریه بیشتر فهرستی از راهبردهاست تا مدلی علّی؛ کمتر توضیح می‌دهد چرا و در چه شرایطی یک راهبرد مؤثرتر از دیگری است.",
     "کم‌توجهی به پذیرش مخاطب: تحلیل اغلب بر متنِ پاسخ متمرکز است و واکنش و تفسیر مخاطب را کمتر در محاسبه می‌آورد.",
     "بافت رسانه‌ای نو: در محیط شبکه‌های اجتماعی، سرعت، تکثر صداها و منطق اشتراک‌گذاری، کاربرد و اثربخشی تاکسونومی کلاسیک را پیچیده کرده است."
   ],
   "applications": [
     "تحلیل ارتباطات بحران سازمانی و مدیریت شهرت (مانند پاسخ شرکت‌ها به بحران‌های زیست‌محیطی و محصول).",
     "مطالعهٔ عذرخواهی سیاسی و دفاع از تصویر مقامات در رسوایی‌ها و کمپین‌های انتخاباتی.",
     "تحلیل ترمیم تصویر افراد مشهور و برندها در رسانه‌های اجتماعی و مدیریت بحران آنلاین."
   ],
   "evolution": "بنوا سنت «آپولوژی» (apologia) و نظریهٔ «حساب‌دهی» (accounts) و بلاغت کلاسیک را در یک تاکسونومی یکپارچه جمع کرد (1995). او بعدها کاربرد نظریه را در کمپین‌های سیاسی و بحران‌های شرکتی گسترش داد و در ویراست دوم کتاب (2014) با عنوان Image Repair Theory and Research، تجربهٔ دو دههٔ پژوهش تجربی و نقدها را لحاظ کرد. امروزه ترمیم تصویر در ارتباطات بحران، روابط عمومی، تحلیل گفتمان سیاسی و ارتباطات سلامت به‌کار می‌رود.",
   "key_concepts": ["ترمیم تصویر (image repair)", "انکار (denial)", "گریز از مسئولیت (evasion of responsibility)", "کاهش رنجش‌زایی (reducing offensiveness)", "خودسرزنش‌گری (mortification)"],
   "studies": ["Benoit, W. L. (1995). Accounts, Excuses, and Apologies: A Theory of Image Restoration Strategies. SUNY Press.", "Benoit, W. L. (2014). Accounts, Excuses, and Apologies: Image Repair Theory and Research (2nd ed.). SUNY Press."],
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
    codes = ["MC-139", "MC-140", "MC-141", "MC-142"]
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
    print("BATCH32 THEORY DONE")

if __name__ == "__main__":
    main()
