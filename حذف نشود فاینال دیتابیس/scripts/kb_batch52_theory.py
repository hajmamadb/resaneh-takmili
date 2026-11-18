# -*- coding: utf-8 -*-
"""Batch 52 (THEORY): MC-216 Cultural Proximity (Straubhaar 1991), MC-217 Nation Branding
(Anholt 2007), MC-218 Mass-Mediated Terrorism (Weimann & Winn 1994), MC-219 Humanitarian
Spectatorship (Boltanski 1999). Anchors verified 2026-11-16."""
import pymysql, json

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch52-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch52_theory.json"

S = {
 "MC-216": [
   dict(kind="JOURNAL_ARTICLE", title_en="Beyond Media Imperialism: Assymetrical Interdependence and Cultural Proximity",
        title_fa="فراتر از امپریالیسم رسانه‌ای: وابستگی متقابل نامتقارن و نزدیکی فرهنگی",
        authors="Straubhaar, J. D.", year=1991,
        publisher="Critical Studies in Mass Communication, 8(1), 39-59", doi="10.1080/15295039109366779",
        url="https://www.tandfonline.com/doi/abs/10.1080/15295039109366779",
        language="en", isbn=None,
        citation="Straubhaar, J. D. (1991). Beyond media imperialism: Assymetrical interdependence and cultural proximity. Critical Studies in Mass Communication, 8(1), 39-59.",
        locator="pp. 39-59", locator_type="page_range", supports="definition / cultural proximity thesis", verified=True),
   dict(kind="BOOK", title_en="Recentering Globalization: Popular Culture and Japanese Transnationalism",
        title_fa="بازمرکزیت‌بخشی به جهانی‌شدن: فرهنگ عامه و فراملی‌گرایی ژاپنی",
        authors="Iwabuchi, K.", year=2002, publisher="Durham, NC: Duke University Press", doi=None, url=None,
        language="en", isbn=None,
        citation="Iwabuchi, K. (2002). Recentering globalization: Popular culture and Japanese transnationalism. Duke University Press.",
        locator="whole work", locator_type="work", supports="evolution / regional cultural flows", verified=False),
 ],
 "MC-217": [
   dict(kind="BOOK", title_en="Competitive Identity: The New Brand Management for Nations, Cities and Regions",
        title_fa="هویت رقابتی: مدیریت برند نوین برای ملت‌ها، شهرها و مناطق",
        authors="Anholt, S.", year=2007, publisher="Basingstoke: Palgrave Macmillan", doi="10.1057/9780230627727",
        url="https://link.springer.com/book/10.1057/9780230627727", language="en", isbn="9780230500280",
        citation="Anholt, S. (2007). Competitive identity: The new brand management for nations, cities and regions. Palgrave Macmillan.",
        locator="whole work", locator_type="work", supports="definition / competitive identity hexagon", verified=True),
   dict(kind="JOURNAL_ARTICLE", title_en="Nation Branding: Toward an Agenda for Critical Research",
        title_fa="برندسازی ملی: به سوی دستورکاری برای پژوهش انتقادی",
        authors="Kaneva, N.", year=2011,
        publisher="International Journal of Communication, 5, 117-141", doi=None,
        url="https://ijoc.org/index.php/ijoc/article/view/786", language="en", isbn=None,
        citation="Kaneva, N. (2011). Nation branding: Toward an agenda for critical research. International Journal of Communication, 5, 117-141.",
        locator="pp. 117-141", locator_type="page_range", supports="critiques / critical agenda", verified=False),
 ],
 "MC-218": [
   dict(kind="BOOK", title_en="The Theater of Terror: Mass Media and International Terrorism",
        title_fa="تئاتر وحشت: رسانه‌های جمعی و تروریسم بین‌المللی",
        authors="Weimann, G., & Winn, C.", year=1994, publisher="New York: Longman", doi=None,
        url="https://search.worldcat.org/title/theater-of-terror-mass-media-and-international-terrorism/oclc/27388735",
        language="en", isbn="9780801311017",
        citation="Weimann, G., & Winn, C. (1994). The theater of terror: Mass media and international terrorism. Longman.",
        locator="whole work", locator_type="work", supports="definition / theater metaphor", verified=True),
   dict(kind="BOOK", title_en="Mass-Mediated Terrorism: The Central Role of the Media in Terrorism and Counterterrorism",
        title_fa="تروریسم رسانه‌ای‌شده: نقش محوری رسانه در تروریسم و ضدتروریسم",
        authors="Nacos, B. L.", year=2007, publisher="Lanham, MD: Rowman & Littlefield", doi=None, url=None,
        language="en", isbn=None,
        citation="Nacos, B. L. (2007). Mass-mediated terrorism: The central role of the media in terrorism and counterterrorism (2nd ed.). Rowman & Littlefield.",
        locator="whole work", locator_type="work", supports="evolution / policy and counterterrorism", verified=False),
 ],
 "MC-219": [
   dict(kind="BOOK", title_en="Distant Suffering: Morality, Media and Politics",
        title_fa="رنج دور: اخلاق، رسانه و سیاست",
        authors="Boltanski, L.", year=1999, publisher="Cambridge: Cambridge University Press", doi=None,
        url="https://www.cambridge.org/core/books/distant-suffering/1384CA9A618DF8C0D7644AA1FC4B6323",
        language="en", isbn="9780521659536",
        citation="Boltanski, L. (1999). Distant suffering: Morality, media and politics. Cambridge University Press.",
        locator="whole work", locator_type="work", supports="definition / politics of pity", verified=True),
   dict(kind="BOOK", title_en="The Spectatorship of Suffering", title_fa="تماشاگری رنج",
        authors="Chouliaraki, L.", year=2006, publisher="London: Sage", doi=None, url=None, language="en", isbn=None,
        citation="Chouliaraki, L. (2006). The spectatorship of suffering. Sage.",
        locator="whole work", locator_type="work", supports="evolution / spectatorship regimes", verified=False),
 ],
}

ENRICH = {
 "MC-216": {
   "summary": "«نزدیکی فرهنگی» (Cultural Proximity) به گرایش مخاطبان به ترجیح محتوا و رسانه‌هایی اشاره دارد که از نظر زبان، فرهنگ، دین، تاریخ و تجربهٔ زیسته به آن‌ها نزدیک‌ترند. جوزف استرابهار در «Beyond Media Imperialism» (۱۹۹۱، Critical Studies in Mass Communication) این مفهوم را در برابر تز یک‌سویهٔ امپریالیسم رسانه‌ای مطرح کرد (Straubhaar, 1991).",
   "main_problem": "اگر جریان رسانه‌ای جهان به سمت محصولات غربی گرایش دارد، چرا مخاطبان در بسیاری از کشورها محتوای ملی و منطقه‌ای را ترجیح می‌دهند، و چگونه می‌توان جریان‌های رسانه‌ای جهان را بدون فروکاستن به سلطهٔ یک‌سویه توضیح داد؟",
   "mechanism": "استرابهار دو مفهوم رقیب را جایگزین تز امپریالیسم رسانه‌ای می‌کند: نخست، «وابستگی متقابل نامتقارن» (asymmetrical interdependence) — جریان رسانه‌ای دوطرفه اما نابرابر است، نه یک‌سویهٔ محض؛ دوم، «نزدیکی فرهنگی» (cultural proximity) — مخاطبان به‌طور فعال محتوایی را برمی‌گزینند که با زبان، قومیت، دین، پوشش، موسیقی، طنز، مرجع تاریخی و ارزش‌هایشان هم‌خوان باشد (Straubhaar, 1991). نتیجهٔ این گرایش، رشد تولید ملی و منطقه‌ای و شکل‌گیری «بازارهای فرهنگی-زبانی» لایه‌ای است: محتوای محلی در لایهٔ نخست، محتوای منطقه‌ای هم‌زبان و هم‌فرهنگ در لایهٔ دوم، و محتوای جهانی در لایهٔ سوم قرار می‌گیرد. ایوابوچی (Iwabuchi, 2002) با مطالعهٔ موج کره‌ای و فرهنگ عامهٔ ژاپنی نشان داد که جریان‌های منطقه‌ای می‌توانند مرکزیت رسانه‌ای غرب را به چالش بکشند و «جهانی‌شدن از درون منطقه» را بسازند. در بستر رسانه، نظریهٔ نزدیکی فرهنگی توضیح می‌دهد چرا سریال‌های ترکی، کره‌ای و لاتین در بازارهای منطقه‌ای موفق‌ترند و چرا قالب‌های جهانی برای موفقیت باید بومی‌سازی شوند؛ با این حال، نزدیکی فرهنگی نه ثابت است و نه ذاتی، بلکه در تعامل تولید، مصرف و بازنمایی ساخته می‌شود.",
   "assumptions": [
     "مخاطبان محتوای culturally نزدیک به تجربهٔ خود را ترجیح می‌دهند.",
     "جریان رسانه‌ای جهان دوطرفه اما نامتقارن است.",
     "نزدیکی فرهنگی در بازارهای لایه‌ای ملی، منطقه‌ای و جهانی عمل می‌کند."
   ],
   "principles": [
     "وابستگی متقابل نامتقارن: جریان رسانه‌ای نه یک‌سویهٔ محض است.",
     "ترجیح نزدیکی: زبان و فرهنگ مشترک، انتخاب مخاطب را شکل می‌دهد.",
     "بازارهای لایه‌ای: محلی، منطقه‌ای و جهانی در سه لایه رقابت می‌کنند."
   ],
   "critiques": [
     "ذات‌گرایی فرهنگی: فرض «فرهنگ نزدیک» ممکن است تصویری ذات‌گرا و همگن از فرهنگ بسازد.",
     "دشواری سنجش: نزدیکی فرهنگی مفهومی کیفی است که عملیاتی‌سازی آن دشوار است.",
     "ساختگی نزدیکی: نزدیکی می‌تواند از سوی صنعت رسانه ساخته یا دستکاری شود."
   ],
   "applications": [
     "تحلیل موفقیت محصولات رسانه‌ای منطقه‌ای مانند سریال‌های ترکی و کره‌ای.",
     "پژوهش دربارهٔ بومی‌سازی قالب‌های جهانی رسانه.",
     "سیاست‌گذاری تولید ملی و حمایت از بازار فرهنگی-زبانی."
   ],
   "evolution": "استرابهار (1991) تز نزدیکی فرهنگی را در نقد امپریالیسم رسانه‌ای صورت‌بندی کرد و ایوابوچی (2002) جریان‌های منطقه‌ای آسیایی را برجسته کرد. در دههٔ ۲۰۱۰-۲۰۲۰، پلتفرم‌های استریمینگ و موج‌های فرهنگی منطقه‌ای، منطق نزدیکی را در مقیاس جهانی بازتولید کردند.",
   "key_concepts": ["نزدیکی فرهنگی (cultural proximity)", "وابستگی متقابل نامتقارن (asymmetrical interdependence)", "بازار فرهنگی-زبانی (cultural-linguistic market)", "امپریالیسم رسانه‌ای (media imperialism)", "بومی‌سازی (localization)"],
   "studies": ["Straubhaar, J. D. (1991). Beyond media imperialism. Critical Studies in Mass Communication, 8(1), 39-59.", "Iwabuchi, K. (2002). Recentering Globalization. Duke University Press."],
 },
 "MC-217": {
   "summary": "«برندسازی ملی» (Nation Branding) به کوشش آگاهانه برای مدیریت تصویر و اعتبار یک کشور در نظر مخاطبان خارجی اشاره دارد تا سرمایه‌گذاری، گردشگری، استعداد و اعتماد جذب شود. سایمون آنهولت در «Competitive Identity» (۲۰۰۷، Palgrave Macmillan) برندسازی ملی را به «هویت رقابتی» و عمل — نه تبلیغ — گره زد (Anholt, 2007).",
   "main_problem": "آیا تصویر یک کشور را می‌توان همچون یک برند تجاری مدیریت کرد، چه چیزهایی این تصویر را می‌سازند، و مرز میان دیپلماسی عمومی مشروع و بازاریابی تبلیغاتی کجاست؟",
   "mechanism": "آنهولت مفهوم «هویت رقابتی» (competitive identity) را پیشنهاد می‌کند: تصویر یک کشور در بیرون، برآیند شش کانال است — گردشگری، صادرات، حکمرانی، سرمایه‌گذاری و مهاجرت، فرهنگ و میراث، و مردم (Anholt, 2007). نکتهٔ کلیدی این است که برند ملی «ساخته» نمی‌شود، بلکه «کسب» می‌شود: کمپین تبلیغاتی بدون عمل و سیاست واقعی، تصویری پایدار نمی‌سازد، و شهرت ملی از رهگذر کردار — کیفیت محصولات، رفتار دولت، دستاورد فرهنگی و تجربهٔ بازدیدکنندگان — شکل می‌گیرد. تصویر ملی کندتغییر و مقاوم است و تنها با هماهنگی طولانی‌مدت بازیگران دولتی و غیردولتی تغییر می‌کند. کانوا (Kaneva, 2011) با رویکردی انتقادی نشان می‌دهد که برندسازی ملی اغلب در چارچوب نئولیبرالی و با کاهش ملت به کالا عمل می‌کند، کلیشه‌های موجود را بازتولید می‌کند و شواهد تجربی کافی برای اثربخشی آن وجود ندارد. در بستر رسانه، برندسازی ملی با دیپلماسی عمومی و رسانه‌های فرامرزی (مانند BBC، DW یا CGTN) درهم می‌آمیزد: رسانه نه‌تنها روایت ملی را منتقل می‌کند، بلکه خود بخشی از زیرساخت هویت رقابتی است و از طریق پوشش خبری، مستند و سرگرمی، تصویر کشور را در ذهن مخاطب جهانی می‌سازد یا تخریب می‌کند.",
   "assumptions": [
     "تصویر ملی بر جذب سرمایه، گردشگری و اعتماد اثر می‌گذارد.",
     "شهرت ملی از کردار و سیاست ساخته می‌شود، نه فقط تبلیغ.",
     "تصویر ملی مقاوم و کندتغییر است و هماهنگی بلندمدت می‌خواهد."
   ],
   "principles": [
     "شش کانال: گردشگری، صادرات، حکمرانی، سرمایه‌گذاری، فرهنگ و مردم.",
     "کردار بر تبلیغ مقدم است: شهرت از عمل می‌آید.",
     "هماهنگی بازیگران: دولت و جامعهٔ مدنی با هم تصویر می‌سازند."
   ],
   "critiques": [
     "نئولیبرالیسم: برندسازی ملی ملت را به کالای بازارپسند فرو می‌کاهد.",
     "بازتولید کلیشه: کمپین‌ها اغلب تصاویر قالبی و اروپامحور را تقویت می‌کنند.",
     "کمبود شواهد: اثربخشی تجربی برندسازی ملی به‌سختی اثبات‌پذیر است."
   ],
   "applications": [
     "تحلیل دیپلماسی عمومی و رسانه‌های فرامرزی یک کشور.",
     "پژوهش دربارهٔ بازنمایی رسانه‌ای ملت‌ها و تصویر بین‌المللی.",
     "نقد کمپین‌های برندسازی و پیامدهای فرهنگی آن."
   ],
   "evolution": "آنهولت (2007) چارچوب هویت رقابتی را تثبیت کرد و شاخص برند ملی را توسعه داد؛ کانوا (2011) دستورکار انتقادی را پیش گذاشت. در دههٔ ۲۰۱۰-۲۰۲۰، رسانه‌های اجتماعی و دیپلماسی دیجیتال، برندسازی ملی را به عرصهٔ تعامل روزمره کشاندند.",
   "key_concepts": ["برندسازی ملی (nation branding)", "هویت رقابتی (competitive identity)", "شاخص برند ملی (Nation Brands Index)", "دیپلماسی عمومی (public diplomacy)", "قدرت نرم (soft power)"],
   "studies": ["Anholt, S. (2007). Competitive Identity. Palgrave Macmillan.", "Kaneva, N. (2011). Nation branding: Toward an agenda for critical research. IJoC, 5, 117-141."],
 },
 "MC-218": {
   "summary": "«تروریسم رسانه‌ای‌شده» (Mass-Mediated Terrorism) به رابطهٔ هم‌زیستی و وابستگی متقابل تروریسم و رسانه‌های جمعی اشاره دارد: کنش تروریستی همچون نمایشی برای جلب توجه رسانه‌ای طراحی می‌شود و رسانه نیز به‌سبب درام و خشونت به آن جذب می‌شود. گابریل وایمن و کنراد وین در «The Theater of Terror» (۱۹۹۴، Longman) این رابطه را «تئاتر وحشت» نامیدند (Weimann & Winn, 1994).",
   "main_problem": "چرا تروریسم و رسانه‌های جمعی به یکدیگر وابسته‌اند، پوشش رسانه‌ای تروریسم چه پیامدهایی برای افکار عمومی، سیاست و امنیت دارد، و رسانه‌ها چگونه می‌توانند بدون پنهان‌کاری، خشونت را تقویت نکنند؟",
   "mechanism": "وایمن و وین تروریسم را کنشی نمادین و ارتباطی می‌بینند که هدفش نه فقط قربانی مستقیم، بلکه مخاطب گسترده و افکار عمومی است؛ از این رو «تئاتر» استعارهٔ مناسبی است: صحنه، بازیگر، تماشاگر و درام (Weimann & Winn, 1994). سه سازوکار این رابطه را شکل می‌دهد: نخست، منطق رسانه‌ای — خشونت، بحران و درام ارزش خبری بالا دارند و رقابت بر سر بیننده، پوشش گسترده را پاداش می‌دهد؛ دوم، هم‌زیستی متقابل — تروریست برای رسیدن به «تبلیغ» به رسانه نیاز دارد و رسانه برای «خبر» به رویداد؛ سوم، پیامدهای شناختی — پوشش مکرر، ترس، برجسته‌سازی تهدید و گاه «اثر سرایت» (contagion) و تقلید (copycat) را تقویت می‌کند. ناکوس (Nacos, 2007) این چارچوب را به سیاست ضدتروریستی و رسانه‌های دیجیتال گسترد و نشان داد که پوشش «تروریسم رسانه‌ای‌شده» در عصر اینترنت به شبکه‌های اجتماعی و رسانهٔ شهروندی نیز کشیده شده است. در بستر رسانه، نظریه پرسش‌های اخلاقی مهمی پیش می‌گذارد: چگونه می‌توان بدون سانسور، از تبدیل خشونت به نمایش و از تقویت روایت تروریستی پرهیز کرد، و چگونه می‌توان بین «حق آگاهی عمومی» و «مسئولیت در قبال آسیب» تعادل برقرار کرد.",
   "assumptions": [
     "تروریسم کنشی ارتباطی است که مخاطب گسترده را هدف می‌گیرد.",
     "تروریسم و رسانه به یکدیگر وابسته‌اند.",
     "پوشش مکرر خشونت بر ترس و رفتار عمومی اثر می‌گذارد."
   ],
   "principles": [
     "تئاتر وحشت: تروریسم نمایشی برای جلب توجه رسانه‌ای است.",
     "هم‌زیستی متقابل: تروریست به تبلیغ و رسانه به خبر نیاز دارد.",
     "پیامد شناختی: پوشش مکرر ترس و تقلید را تقویت می‌کند."
   ],
   "critiques": [
     "جبرگرایی رسانه‌ای: فرض رابطهٔ خطی میان پوشش و تروریسم، عوامل دیگر را نادیده می‌گیرد.",
     "ناهمگونی پوشش: میزان و شیوهٔ پوشش تروریسم در رسانه‌ها و کشورها بسیار متفاوت است.",
     "شواهد مختلط: رابطهٔ تجربی میان پوشش و «اثر سرایت» محل بحث است."
   ],
   "applications": [
     "تدوین راهنماهای اخلاقی پوشش تروریسم و بحران.",
     "تحلیل چارچوب‌بندی خبری خشونت سیاسی و اثر آن بر افکار عمومی.",
     "پژوهش دربارهٔ تروریسم در رسانه‌های اجتماعی و رسانهٔ شهروندی."
   ],
   "evolution": "وایمن و وین (1994) استعارهٔ تئاتر را تثبیت کردند و ناکوس (2007) چارچوب را به سیاست و رسانهٔ دیجیتال گسترد. در دههٔ ۲۰۱۰-۲۰۲۰، تبلیغات آنلاین گروه‌های خشونت‌طلب، مسئلهٔ «تروریسم رسانه‌ای‌شده» را به پلتفرم‌ها و الگوریتم‌ها کشاند.",
   "key_concepts": ["تروریسم رسانه‌ای‌شده (mass-mediated terrorism)", "تئاتر وحشت (theater of terror)", "اثر سرایت (contagion effect)", "ارزش خبری خشونت (violence news value)", "اخلاق پوشش (reporting ethics)"],
   "studies": ["Weimann, G., & Winn, C. (1994). The Theater of Terror. Longman.", "Nacos, B. L. (2007). Mass-Mediated Terrorism (2nd ed.). Rowman & Littlefield."],
 },
 "MC-219": {
   "summary": "«تماشاگری بشردوستانه» (Humanitarian Spectatorship) به موقعیت اخلاقی و سیاسی تماشاگرِ رنجِ دور اشاره دارد که از طریق رسانه با مصیبت دیگران روبه‌رو می‌شود و باید تصمیم بگیرد چگونه پاسخ دهد. لوك بولتانسکی در «Distant Suffering» (۱۹۹۹، Cambridge University Press) این موقعیت را در چارچوب «سیاست ترحم» تحلیل کرد (Boltanski, 1999).",
   "main_problem": "وقتی رسانه رنج مردمان دور را به خانهٔ ما می‌آورد، پاسخ اخلاقی مناسب چیست، و چگونه می‌توان میان احساس همدلی، نکوهش و کنش سیاسی تعادل برقرار کرد، بدون آنکه رنج به تماشا و مصرف تبدیل شود؟",
   "mechanism": "بولتانسکی موقعیت تماشاگر را در سه «تاپوس» (topos) پاسخ اخلاقی صورت‌بندی می‌کند: «نکوهش» (denunciation) — محکوم‌کردن عاملان رنج؛ «احساس» (sentiment) — همدلی و شفقت بی‌واسطه؛ و «زیبایی‌شناسی» (aesthetic) — تأمل زیبایی‌شناختی در بازنمایی رنج (Boltanski, 1999). او نشان می‌دهد که هر یک از این پاسخ‌ها در معرض انحراف است: نکوهش می‌تواند به سیاست‌زدگی، احساس به «شفقت ارزان» و زیبایی‌شناسی به زیبایی‌سازی رنج فروکاسته شود. چولیااراکی (Chouliaraki, 2006) چارچوب را با «رژیم‌های تماشاگری» گسترد: «ماجراجویی» (adventure)، «اضطرار» (emergency) و «وجدانی/شورانگیز» (ecstatic)، که هر یک رابطهٔ متفاوتی میان تماشاگر، رنج‌دیده و کنش می‌سازند. سازوکار مرکزی، میانجی‌گری رسانه‌ای رنج است: نحوهٔ نمایش چهره، صدا و روایت رنج‌دیده — و میزان فضایی که به عاملیت او داده می‌شود — پاسخ اخلاقی تماشاگر را شکل می‌دهد. در بستر رسانه، این نظریه به تحلیل کمپین‌های بشردوستانه، پوشش فاجعه و «خستگی شفقت» (compassion fatigue) می‌پردازد و می‌پرسد چگونه ارتباط بشردوستانه می‌تواند از بازتولید رابطهٔ نابرابر «ما/آن‌ها» فراتر رود و به همبستگی کنشگر بدل شود، نه مصرف احساسی رنج.",
   "assumptions": [
     "رسانه تماشاگر را در موقعیت اخلاقی روبه‌رویی با رنج دور قرار می‌دهد.",
     "شیوهٔ بازنمایی رنج، پاسخ اخلاقی تماشاگر را شکل می‌دهد.",
     "همدلی و کنش سیاسی می‌توانند در تنش باشند."
   ],
   "principles": [
     "سیاست ترحم: پاسخ تماشاگر به رنج، امری سیاسی است.",
     "سه تاپوس: نکوهش، احساس و زیبایی‌شناسی.",
     "میانجی‌گری رنج: نمایش رسانه‌ای، رابطهٔ تماشاگر و رنج‌دیده را می‌سازد."
   ],
   "critiques": [
     "اروپامحوری تماشاگر: چارچوب، تماشاگر غربی را مرکز تحلیل قرار می‌دهد.",
     "احساس‌گرایی: تأکید بر شفقت می‌تواند به جای کنش، به مصرف احساسی رنج بینجامد.",
     "عاملیت رنج‌دیده: بازنمایی رسانه‌ای اغلب صدای رنج‌دیده را به حاشیه می‌راند."
   ],
   "applications": [
     "تحلیل اخلاقی کمپین‌های بشردوستانه و تبلیغات NGO.",
     "پژوهش دربارهٔ پوشش فاجعه و خستگی شفقت.",
     "نقد ارتباط بشردوستانه و بازنمایی رنج‌دیدگان."
   ],
   "evolution": "بولتانسکی (1999) سیاست ترحم را صورت‌بندی کرد و چولیااراکی (2006) رژیم‌های تماشاگری را افزود. در دههٔ ۲۰۱۰-۲۰۲۰، رسانه‌های دیجیتال و کمپین‌های بشردوستانهٔ تعاملی، پرسش‌های تازه‌ای دربارهٔ همبستگی و مصرف رنج پیش گذاشتند.",
   "key_concepts": ["تماشاگری بشردوستانه (humanitarian spectatorship)", "رنج دور (distant suffering)", "سیاست ترحم (politics of pity)", "خستگی شفقت (compassion fatigue)", "رژیم تماشاگری (spectatorship regime)"],
   "studies": ["Boltanski, L. (1999). Distant Suffering. Cambridge University Press.", "Chouliaraki, L. (2006). The Spectatorship of Suffering. Sage."],
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
    codes = ["MC-216", "MC-217", "MC-218", "MC-219"]
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
    print("BATCH52 THEORY DONE")

if __name__ == "__main__":
    main()
