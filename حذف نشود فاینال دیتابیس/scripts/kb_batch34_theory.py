# -*- coding: utf-8 -*-
"""Batch 34 (THEORY): MC-295 Information Fiduciaries (Balkin 2016), MC-434 Algorithmic Black Box
(Pasquale 2015), MC-669 Supra-Panopticon (Poster 1990), MC-415 Platformization (Helmond 2015).
All primary anchors web-verified 2026-11-16. Target: resaname_kb_final_inspect."""
import pymysql, json

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch34-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch34_theory.json"

S = {
 "MC-295": [  # Information Fiduciaries
   dict(kind="JOURNAL_ARTICLE", title_en="Information Fiduciaries and the First Amendment",
        title_fa="امین‌های اطلاعاتی و متمم اول قانون اساسی", authors="Balkin, J. M.", year=2016,
        publisher="UC Davis Law Review, 49(4), 1183-1234", doi=None,
        url="https://lawreview.law.ucdavis.edu/archives/49/4/information-fiduciaries-and-first-amendment",
        language="en", isbn=None,
        citation="Balkin, J. M. (2016). Information fiduciaries and the First Amendment. UC Davis Law Review, 49(4), 1183-1234.",
        locator="pp. 1183-1234", locator_type="page_range", supports="definition / fiduciary duties / legal mechanism", verified=True),
   dict(kind="BOOK", title_en="Privacy's Blueprint: The Battle to Control the Design of New Technologies",
        title_fa="نقشهٔ حریم خصوصی: نبرد برای کنترل طراحی فناوری‌های نو", authors="Hartzog, W.", year=2018,
        publisher="Cambridge, MA: Harvard University Press", doi=None, url=None, language="en", isbn=None,
        citation="Hartzog, W. (2018). Privacy's blueprint: The battle to control the design of new technologies. Harvard University Press.",
        locator="whole work", locator_type="work", supports="evolution / design-based regulation", verified=False),
 ],
 "MC-434": [  # Algorithmic Black Box
   dict(kind="BOOK", title_en="The Black Box Society: The Secret Algorithms That Control Money and Information",
        title_fa="جامعهٔ جعبهٔ سیاه: الگوریتم‌های پنهانی که پول و اطلاعات را کنترل می‌کنند",
        authors="Pasquale, F.", year=2015,
        publisher="Cambridge, MA: Harvard University Press", doi=None, url=None, language="en", isbn="9780674368279",
        citation="Pasquale, F. (2015). The black box society: The secret algorithms that control money and information. Harvard University Press.",
        locator="whole work", locator_type="work", supports="definition / types of opacity / mechanism", verified=True),
   dict(kind="JOURNAL_ARTICLE", title_en="How the Machine 'Thinks': Understanding Opacity in Machine Learning Algorithms",
        title_fa="چگونه ماشین «می‌اندیشد»: فهم کدری در الگوریتم‌های یادگیری ماشین", authors="Burrell, J.", year=2016,
        publisher="Big Data & Society, 3(1), 1-12", doi=None, url=None, language="en", isbn=None,
        citation="Burrell, J. (2016). How the machine 'thinks': Understanding opacity in machine learning algorithms. Big Data & Society, 3(1), 1-12.",
        locator="pp. 1-12", locator_type="page_range", supports="evolution / three forms of opacity", verified=False),
 ],
 "MC-669": [  # Supra-Panopticon
   dict(kind="BOOK", title_en="The Mode of Information: Poststructuralism and Social Context",
        title_fa="شیوهٔ اطلاعات: پساساختارگرایی و بافت اجتماعی", authors="Poster, M.", year=1990,
        publisher="Chicago: University of Chicago Press", doi=None, url=None, language="en", isbn=None,
        citation="Poster, M. (1990). The mode of information: Poststructuralism and social context. University of Chicago Press.",
        locator="Ch. 4: Database as Discourse, or Electronic Interpellations", locator_type="CHAPTER",
        supports="definition / superpanopticon / mechanism", verified=True),
   dict(kind="BOOK", title_en="Discipline and Punish: The Birth of the Prison",
        title_fa="مراقبت و تنبیه: تولد زندان", authors="Foucault, M.", year=1977,
        publisher="New York: Pantheon Books", doi=None, url=None, language="en", isbn=None,
        citation="Foucault, M. (1977). Discipline and punish: The birth of the prison. Pantheon Books.",
        locator="Part III: Discipline", locator_type="CHAPTER", supports="theoretical lineage / panopticon", verified=False),
 ],
 "MC-415": [  # Platformization
   dict(kind="JOURNAL_ARTICLE", title_en="The Platformization of the Web: Making Web Data Platform Ready",
        title_fa="پلتفرمیزاسیون وب: آماده‌سازی دادهٔ وب برای پلتفرم", authors="Helmond, A.", year=2015,
        publisher="Social Media + Society, 1(2), 1-11", doi="10.1177/2056305115603080",
        url="https://journals.sagepub.com/doi/10.1177/2056305115603080", language="en", isbn=None,
        citation="Helmond, A. (2015). The platformization of the web: Making web data platform ready. Social Media + Society, 1(2), 1-11. https://doi.org/10.1177/2056305115603080",
        locator="pp. 1-11", locator_type="page_range", supports="definition / double logic / mechanism", verified=True),
   dict(kind="JOURNAL_ARTICLE", title_en="The Platformization of Cultural Production: Theorizing the Contingent Cultural Commodity",
        title_fa="پلتفرمیزاسیون تولید فرهنگی: نظریه‌پردازی دربارهٔ کالای فرهنگی مشروط",
        authors="Nieborg, D. B., & Poell, T.", year=2018,
        publisher="New Media & Society, 20(11), 4275-4292", doi=None, url=None, language="en", isbn=None,
        citation="Nieborg, D. B., & Poell, T. (2018). The platformization of cultural production: Theorizing the contingent cultural commodity. New Media & Society, 20(11), 4275-4292.",
        locator="pp. 4275-4292", locator_type="page_range", supports="evolution / cultural industries", verified=False),
 ],
}

ENRICH = {
 "MC-295": {
   "summary": "«امین‌های اطلاعاتی» (Information Fiduciaries) نظریه‌ای حقوقی از جک بلکین است که در مقالهٔ «Information Fiduciaries and the First Amendment» (۲۰۱۶، UC Davis Law Review) مطرح شد. بلکین استدلال می‌کند شرکت‌های آنلاینی که اطلاعات شخصی کاربران را در مقیاس وسیع گردآوری و پردازش می‌کنند، باید همانند وکیل، پزشک و حسابدار «امین» (fiduciary) کاربران شمرده شوند و به «وظایف امانی» (fiduciary duties) — وفاداری و مراقبت — پایبند باشند (Balkin, 2016).",
   "main_problem": "چگونه می‌توان بدون نقض آزادی بیان، شرکت‌های پلتفرمی را به حفاظت از حریم خصوصی و پرهیز از سوءاستفاده از داده ملزم کرد، در حالی که سازوکار «اطلاع‌رسانی و رضایت» (notice and consent) به‌دلیل عدم تقارن دانش و قدرت ناکارآمد است؟",
   "mechanism": "بلکین مکانیسم را در سه گام توضیح می‌دهد: (۱) رابطهٔ کاربر و سرویس پلتفرمی، از نظر ساختاری به رابطهٔ امین و موکل شباهت دارد، زیرا کاربر اطلاعات محرمانه و حساس خود را در اختیار سرویس‌دهنده می‌گذارد و سرویس‌دهنده از این اطلاعات قدرت و نفوذ به دست می‌آورد؛ (۲) ازاین‌رو، سرویس‌دهنده موظف است «وظیفهٔ محرمانگی» (duty of confidentiality) را رعایت کند و از افشای اطلاعات سوءاستفاده نکند، «وظیفهٔ مراقبت» (duty of care) برای حفاظت امن از داده‌ها را بپذیرد و از «خودمعامله‌گری» (self-dealing) — یعنی استفاده از اطلاعات به زیان ذی‌نفع — بپرهیزد؛ (۳) از منظر حقوق اساسی آمریکا، تنظیم این وظایف، مقررات ناظر بر «رفتار» (conduct) است نه محتوای بیان، ازاین‌رو با متمم اول قانون اساسی تعارض پیدا نمی‌کند (Balkin, 2016). بلکین تأکید می‌کند این چارچوب مکمل قوانین حمایت از داده است، نه جانشین آن.",
   "assumptions": [
     "کاربران در برابر سرویس‌های آنلاین در موقعیت آسیب‌پذیری اطلاعاتی و عدم تقارن قدرت قرار دارند.",
     "روابط مبتنی بر اعتماد و واگذاری اطلاعات حساس، به‌طور ساختاری شبیه روابط امانی سنتی است.",
     "تنظیم وظایف رفتاری امین، برخلاف تنظیم محتوا، با آزادی بیان تعارض بنیادین ندارد."
   ],
   "principles": [
     "وفاداری: امین اطلاعاتی نباید از دادهٔ موکل برخلاف منافع او استفاده کند.",
     "مراقبت: امین موظف به حفاظت فنی و سازمانی از اطلاعات سپرده‌شده است.",
     "شفافیت محدود: منافع متعارض باید آشکار شود و تصمیم‌های داده‌محور قابل توضیح باشند."
   ],
   "critiques": [
     "ابهام در تعیین دامنه: مرز میان سرویس‌های «امین‌گونه» و بازیگران دیگر روشن نیست و تعیین اینکه چه کسی امین است، بحث‌برانگیز می‌ماند.",
     "تعارض ساختاری منافع: مدل کسب‌وکار آگهی‌محور، ذاتاً با وظیفهٔ وفاداری در تعارض است و اجرای آن را دشوار می‌کند.",
     "اجرای عملی: نبود نهاد نظارتی توانمند و سازوکار جبران خسارت، خطر تبدیل نظریه به شعاری حقوقی را ایجاد می‌کند."
   ],
   "applications": [
     "پیشنهاد اصلاحات قانونی در حوزهٔ حریم خصوصی و حمایت از داده در آمریکا و اتحادیهٔ اروپا.",
     "طراحی الزامات افشا و پاسخ‌گویی برای پلتفرم‌های داده‌محور.",
     "تحلیل حقوقی مسئولیت سرویس‌های ابری، موتور جست‌وجو و شبکه‌های اجتماعی در قبال دادهٔ کاربران."
   ],
   "evolution": "از مقالهٔ بلکین (2016) که چارچوب را در بستر متمم اول صورت‌بندی کرد، تا بحث‌های بعدی دربارهٔ «وظیفهٔ وفاداری» در حقوق حریم خصوصی و پیشنهادهای تنظیم‌گری مبتنی بر طراحی (Hartzog, 2018). امروزه این نظریه در ادبیات حقوق پلتفرم، پیش‌نویس‌های قانونی حمایت از داده و بحث دربارهٔ مدل‌های «امین داده» در اروپا و آمریکا حضور دارد.",
   "key_concepts": ["امین اطلاعاتی (information fiduciary)", "وظیفهٔ محرمانگی (duty of confidentiality)", "وظیفهٔ مراقبت (duty of care)", "خودمعامله‌گری (self-dealing)", "عدم تقارن اطلاعاتی (information asymmetry)"],
   "studies": ["Balkin, J. M. (2016). Information Fiduciaries and the First Amendment. UC Davis Law Review, 49(4), 1183-1234.", "Hartzog, W. (2018). Privacy's Blueprint. Harvard University Press."],
 },
 "MC-434": {
   "summary": "«نظریهٔ جعبهٔ سیاه الگوریتمی» (Algorithmic Black Box Theory) با کتاب «The Black Box Society» فرانک پاسکواله (۲۰۱۵، Harvard University Press) گره خورده است. پاسکواله نشان می‌دهد که در حوزه‌های مالی، جست‌وجوی آنلاین و اعتبارسنجی، الگوریتم‌های مهم در «جعبهٔ سیاه» (black box) پنهان‌اند و شهروندان نه از داده‌های ورودی و نه از منطق تصمیم آگاه‌اند؛ این کدری، قدرت را از پاسخ‌گویی می‌رهاند (Pasquale, 2015).",
   "main_problem": "الگوریتم‌ها چگونه بر زندگی افراد اثر می‌گذارند و چرا کدری و پنهان‌کاری الگوریتمی، پاسخ‌گویی و عدالت را تهدید می‌کند، در حالی که «شفافیت» به‌تنهایی درمان کافی نیست؟",
   "mechanism": "پاسکواله سه لایهٔ کدری را از هم تفکیک می‌کند: (۱) «کدری ناشی از راز تجاری» (proprietary secrecy) — کد الگوریتم دارایی شرکت است و از دید عمومی پنهان می‌ماند؛ (۲) «کدری فنی» (technical opacity) — در یادگیری ماشین حتی طراحان نیز نمی‌توانند به‌طور کامل توضیح دهند سیستم چگونه به خروجی رسیده است؛ (۳) «کدری نهادی» (institutional opacity) — پیچیدگی سازمانی و زنجیرهٔ داده، ردیابی مسئولیت را دشوار می‌کند. این سه لایه با هم «عدم تقارن اطلاعاتی» (information asymmetry) میان مؤسسه و شهروند را تولید و «مسئولیت‌پذیری» را تضعیف می‌کنند. پاسکواله راه‌حل را در ترکیبی از «شفافیت واجد شرایط» (qualified transparency)، حسابرسی مستقل، و «دادرسی داده» (data due process) می‌بیند، نه فقط انتشار کد (Pasquale, 2015).",
   "assumptions": [
     "تصمیم‌های الگوریتمی در حوزه‌های حساس (اعتبار، اشتغال، جست‌وجو) پیامدهای توزیعی و حقوقی معنادار دارند.",
     "کدری الگوریتمی به‌طور نظام‌مند به نفع صاحبان قدرت و به زیان شهروندان عمل می‌کند.",
     "شفافیت صرف، بدون سازوکار پاسخ‌گویی و جبران، برای عدالت کافی نیست."
   ],
   "principles": [
     "حسابرسی‌پذیری: سیستم‌های تصمیم‌ساز باید برای بازرسی مستقل و تخصصی باز باشند.",
     "توازن راز تجاری و منفعت عمومی: اسرار تجاری نمی‌تواند مانع مطلق پاسخ‌گویی در تصمیم‌های اثرگذار باشد.",
     "دادرسی داده: افراد حق دارند از منطق تصمیم در مورد خود و امکان اعتراض آگاه شوند."
   ],
   "critiques": [
     "شفافیت‌گرایی ساده‌انگارانه: منتقدان می‌گویند تمرکز بر «بازکردن جعبه» ممکن است از پرسش مهم‌تر — یعنی عدالت و قدرت — منحرف شود.",
     "ضرورت کدری: در برخی موارد، پنهان‌کاری برای امنیت، حریم خصوصی و پیشگیری از بازی‌کردن سیستم لازم است.",
     "مرز با تصمیم انسانی: تصمیم‌های انسانی نیز اغلب کدرند؛ بنابراین «جعبهٔ سیاه» پدیده‌ای منحصر به ماشین نیست."
   ],
   "applications": [
     "حاکمیت هوش مصنوعی، ارزیابی انطباق و الزامات «توضیح‌پذیری» در مقررات مانند قانون هوش مصنوعی اتحادیهٔ اروپا.",
     "تحلیل عدالت الگوریتمی در اعتبارسنجی، بیمه، استخدام و مدیریت محتوا.",
     "پژوهش پاسخ‌گویی پلتفرم و روزنامه‌نگاری داده‌محور دربارهٔ سیستم‌های تصمیم خودکار."
   ],
   "evolution": "از پاسکواله (2015) که کدری را در سه حوزهٔ مالی، جست‌وجو و شهرت تحلیل کرد، تا ادبیات گستردهٔ «عدالت الگوریتمی» و «توضیح‌پذیری» در دههٔ بعد. بورل (2016) سه شکل کدری — ناشی از مالکیت، فنی و ناشی از ناآشنایی سواد داده — را صورتبندی کرد و بحث را دقیق‌تر ساخت. امروزه نظریهٔ جعبهٔ سیاه یکی از مبانی حاکمیت الگوریتمی و مقررات هوش مصنوعی است.",
   "key_concepts": ["جعبهٔ سیاه (black box)", "کدری الگوریتمی (algorithmic opacity)", "عدم تقارن اطلاعاتی (information asymmetry)", "شفافیت واجد شرایط (qualified transparency)", "پاسخ‌گویی الگوریتمی (algorithmic accountability)"],
   "studies": ["Pasquale, F. (2015). The Black Box Society. Harvard University Press.", "Burrell, J. (2016). How the Machine 'Thinks'. Big Data & Society, 3(1)."],
 },
 "MC-669": {
   "summary": "«سوپاناپتیکن» (Supra-/Super-Panopticon) اصطلاحی است که مارک پستر در کتاب «The Mode of Information» (۱۹۹۰، University of Chicago Press) برای توصیف سازوکار نظارتی جوامع اطلاعاتی به‌کار برد. پستر با بازخوانی «پانوپتیکن» فوکو استدلال کرد که در عصر پایگاه‌های داده، نظارت دیگر به برج مرکزی و نگاه متمرکز نیاز ندارد؛ ثبت و پردازش داده در معاملات روزمره، سوژه‌ها را بدون آنکه بدانند، در شبکهٔ نظارتی جای می‌دهد (Poster, 1990).",
   "main_problem": "با گذار از جوامع انضباطی به جوامع اطلاعاتی، سازوکار قدرت نظارتی چگونه تغییر می‌کند و چرا مدل پانوپتیکن فوکو برای تحلیل نظارت داده‌محور کافی نیست؟",
   "mechanism": "پستر تفاوت را در سه سطح توضیح می‌دهد: (۱) در پانوپتیکن، نظارت بر «بدن‌های فردی در فضای فیزیکی» متمرکز است و سلول زندان، نظم را در سوژه درونی می‌کند؛ در سوپاناپتیکن، نظارت بر «جمعیت‌ها در پایگاه داده» جریان دارد و سوژه به مجموعه‌ای از رکوردها تجزیه می‌شود؛ (۲) نظارت دیگر از یک مرکز اعمال نمی‌شود، بلکه «پراکنده و غیرمتمرکز» است و در جریان معاملات روزمره — کارت اعتباری، فرم، پروندهٔ اداری — پراکنده می‌شود؛ (۳) افراد در نظارت «مشارکت» می‌کنند: با ارائهٔ داده در ازای خدمات، خود در تولید پروندهٔ نظارتی خویش سهیم می‌شوند. پستر نتیجه می‌گیرد که قدرت در جامعهٔ اطلاعاتی، بیش از آنکه از طریق انضباط بدنی اعمال شود، از طریق «قرار دادن افراد در گفتمان‌های داده‌ای» و بازسازی هویت آنان عمل می‌کند (Poster, 1990).",
   "assumptions": [
     "فناوری اطلاعات، شکل جدیدی از قدرت و کنترل اجتماعی پدید می‌آورد که با انضباط بدنی فوکویی متفاوت است.",
     "پایگاه داده، سوژه را به رکوردهای قابل پردازش تجزیه و بازآرایی می‌کند.",
     "افراد در جریان زندگی روزمره، ناخواسته و حتی داوطلبانه در نظارت مشارکت می‌کنند."
   ],
   "principles": [
     "غیرمتمرکز بودن نظارت: نگاه نظارتی به برج مرکزی نیاز ندارد.",
     "داده‌محوری: قدرت از طریق ثبت، دسته‌بندی و پردازش داده اعمال می‌شود.",
     "مشارکت سوژه: نظارت با همکاری ناخواستهٔ افراد در تولید داده پیش می‌رود."
   ],
   "critiques": [
     "جبر فناورانه: پستر ممکن است قدرت فناوری را بیش از حد تعیین‌کننده بداند و مقاومت، تنظیم‌گری و عاملیت کاربران را کم‌رنگ کند.",
     "ابهام مفهومی: «سوپاناپتیکن» به‌سختی عملیاتی و قابل‌سنجش شده و با مفاهیم همسایگی چون «داده‌پایی» (dataveillance) و «جامعهٔ کنترل» هم‌پوشانی دارد.",
     "تحول پلتفرمی: نظریهٔ ۱۹۹۰ پیش از پلتفرم‌های اجتماعی و اقتصاد نظارتی نوشته شده و نیازمند به‌روزرسانی با بحث‌هایی مانند «سرمایه‌داری نظارتی» است."
   ],
   "applications": [
     "تحلیل نظارت داده‌محور در پلتفرم‌های اجتماعی، اعتبارسنجی و خدمات دیجیتال دولتی.",
     "مطالعهٔ حریم خصوصی و قدرت در جوامع اطلاعاتی و اقتصاد نظارتی.",
     "پژوهش دربارهٔ رابطهٔ پایگاه داده، هویت و کنترل اجتماعی در رسانه‌های دیجیتال."
   ],
   "evolution": "پستر (1990) مفهوم را در امتداد پانوپتیکن فوکو (1977) و در نقد جوامع انضباطی صورت‌بندی کرد. در دههٔ ۱۹۹۰، بحث‌هایی مانند «سینوپتیکن» (نگاهِ بسیاری به اندک‌شمار) و «داده‌پایی» به آن افزوده شد و در دههٔ ۲۰۱۰، مفهوم «سرمایه‌داری نظارتی» زوبوف (2019) و بحث «جامعهٔ کنترل» دلوز، سوپاناپتیکن را به تحلیل اقتصاد داده و پلتفرم‌ها پیوند داد.",
   "key_concepts": ["سوپاناپتیکن (supra-/super-panopticon)", "پانوپتیکن (panopticon)", "نظارت داده‌محور (dataveillance)", "جامعهٔ انضباطی (disciplinary society)", "اقتصاد نظارتی (surveillance economy)"],
   "studies": ["Poster, M. (1990). The Mode of Information. University of Chicago Press.", "Foucault, M. (1977). Discipline and Punish. Pantheon Books."],
 },
 "MC-415": {
   "summary": "«پلتفرمیزاسیون» (Platformization) مفهومی است که آنه هلموند در مقالهٔ «The Platformization of the Web» (۲۰۱۵، Social Media + Society) برای توصیف «برآمدن پلتفرم به‌عنوان مدل زیرساختی و اقتصادی مسلط وب اجتماعی» به‌کار برد. پلتفرمیزاسیون فرایندی دوسویه است: پلتفرم‌ها زیرساخت خود را به سراسر وب گسترش می‌دهند و هم‌زمان دادهٔ وب را «آمادهٔ پلتفرم» (platform ready) می‌سازند تا در منطق آن‌ها قابل استفاده شود (Helmond, 2015).",
   "main_problem": "پلتفرم‌ها چگونه از مرزهای سرویس خود فراتر می‌روند و وب را به زیرساخت داده‌ای خویش تبدیل می‌کنند، و این فرایند چه پیامدهایی برای معماری، اقتصاد و حکمرانی وب دارد؟",
   "mechanism": "هلموند «منطق دوگانه» (double logic) پلتفرمیزاسیون را تحلیل می‌کند: (۱) «تمرکززدایی» (decentralization) — پلتفرم از طریق دکمه‌های اشتراک‌گذاری، ورود با حساب کاربری و رابط‌های برنامه‌نویسی (API) در سراسر وب پخش می‌شود و به زیرساختی نامرئی تبدیل می‌گردد؛ (۲) «تمرکز دوباره» (recentralization) — داده‌های گردآوری‌شده از این مسیرها به‌سوی خود پلتفرم بازمی‌گردد و قدرت داده‌ای را در مرکز متمرکز می‌کند. مطالعهٔ موردی هلموند، پروتکل «گراف باز» (Open Graph) فیسبوک است: وب‌سایت‌ها با نشانه‌گذاری داده‌های خود، آن‌ها را برای گردآوری توسط فیسبوک آماده می‌کنند و در نتیجه، منطق پلتفرم در سطح کد و داده به وب تحمیل می‌شود (Helmond, 2015).",
   "assumptions": [
     "پلتفرم به مدل زیرساختی و اقتصادی غالب وب اجتماعی تبدیل شده است.",
     "رابط‌های فنی (API، دکمه‌ها، پروتکل‌ها) سازوکار اصلی گسترش نفوذ پلتفرم‌اند.",
     "جریان داده، منبع اصلی قدرت و ارزش در پلتفرمیزاسیون است."
   ],
   "principles": [
     "دوگانگی تمرکززدایی/تمرکز دوباره: گسترش پلتفرم در وب، نفوذ مرکزی آن را تقویت می‌کند.",
     "آماده‌سازی داده: وب‌ها برای گردآوری داده توسط پلتفرم بازطراحی می‌شوند.",
     "زیرساخت‌شدن: پلتفرم به لایهٔ نامرئی و پیش‌فرض وب تبدیل می‌شود."
   ],
   "critiques": [
     "پلتفرم‌محوری: تحلیل ممکن است بیش از اندازه بر نقش پلتفرم تمرکز کند و کنش کاربران، مقاومت وب‌سایت‌ها و تنظیم‌گری را کم‌رنگ سازد.",
     "هم‌پوشانی مفهومی: تمایز پلتفرمیزاسیون از مفاهیم همسایگی چون «رسانه‌ای‌شدن» و «جامعهٔ پلتفرمی» همیشه روشن نیست.",
     "تمرکز بر وب غربی: تجربهٔ پلتفرمیزاسیون در بافت‌های غیرغربی و پلتفرم‌های منطقه‌ای کمتر بررسی شده است."
   ],
   "applications": [
     "تحلیل اقتصاد اپلیکیشن، توزیع خبر و صنایع فرهنگی در محیط پلتفرمی.",
     "مطالعهٔ زیرساخت‌های داده و حکمرانی وب، از جمله APIها و سیاست‌های دسترسی به داده.",
     "تحلیل پلتفرمیزاسیون خدمات عمومی و زیرساخت‌های شهری (دولت پلتفرمی)."
   ],
   "evolution": "هلموند (2015) مفهوم را برای تحلیل وب و فیسبوک صورت‌بندی کرد. نیبورگ و پول (2018) آن را به تولید فرهنگی و کالای فرهنگی مشروط گسترش دادند و ون‌دایک، پول و دی‌وال (2018) بحث را به سطح «جامعهٔ پلتفرمی» و ارزش‌های عمومی ارتقا دادند. امروزه پلتفرمیزاسیون چارچوبی کلیدی در اقتصاد سیاسی ارتباطات، مطالعات اینترنت و حاکمیت پلتفرم است.",
   "key_concepts": ["پلتفرمیزاسیون (platformization)", "آمادهٔ پلتفرم (platform ready)", "منطق دوگانه (double logic)", "زیرساخت‌شدن (infrastructuralization)", "گراف باز (Open Graph)"],
   "studies": ["Helmond, A. (2015). The Platformization of the Web. Social Media + Society, 1(2), 1-11.", "Nieborg, D. B., & Poell, T. (2018). The Platformization of Cultural Production. New Media & Society, 20(11), 4275-4292."],
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
    codes = ["MC-295", "MC-434", "MC-669", "MC-415"]
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
    print("BATCH34 THEORY DONE")

if __name__ == "__main__":
    main()
