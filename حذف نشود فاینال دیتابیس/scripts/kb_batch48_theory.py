# -*- coding: utf-8 -*-
"""Batch 48 (THEORY): MC-194 Glocalization (Robertson 1995), MC-195 Peace Journalism (Lynch &
McGoldrick 2005), MC-197 Agonistic Pluralism (Mouffe 2000), MC-200 Strategic Narratives
(Miskimmon, O'Loughlin & Roselle 2013). Anchors verified 2026-11-16."""
import pymysql, json

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch48-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch48_theory.json"

S = {
 "MC-194": [
   dict(kind="BOOK_CHAPTER", title_en="Glocalization: Time-Space and Homogeneity-Heterogeneity",
        title_fa="جهانی‌محلی‌سازی: زمان-مکان و همگنی-ناهمگنی", authors="Robertson, R.", year=1995,
        publisher="In M. Featherstone, S. Lash, & R. Robertson (Eds.), Global Modernities (pp. 25-44). London: Sage",
        doi=None, url="https://sk.sagepub.com/book/edvol/global-modernities/chpt/glocalization-timespace-homogeneityheterogeneity",
        language="en", isbn=None,
        citation="Robertson, R. (1995). Glocalization: Time-space and homogeneity-heterogeneity. In M. Featherstone, S. Lash, & R. Robertson (Eds.), Global modernities (pp. 25-44). Sage.",
        locator="pp. 25-44", locator_type="page_range", supports="definition / simultaneity thesis", verified=True),
   dict(kind="BOOK", title_en="Globalization: Social Theory and Global Culture",
        title_fa="جهانی‌شدن: نظریهٔ اجتماعی و فرهنگ جهانی", authors="Robertson, R.", year=1992,
        publisher="London: Sage", doi=None, url=None, language="en", isbn=None,
        citation="Robertson, R. (1992). Globalization: Social theory and global culture. Sage.",
        locator="whole work", locator_type="work", supports="evolution / compression of the world", verified=False),
 ],
 "MC-195": [
   dict(kind="BOOK", title_en="Peace Journalism", title_fa="روزنامه‌نگاری صلح",
        authors="Lynch, J., & McGoldrick, A.", year=2005,
        publisher="Stroud: Hawthorn Press", doi=None,
        url="https://www.hawthornpress.com/books/changemaking/social-ecology-change/peace-journalism/",
        language="en", isbn="9781903458501",
        citation="Lynch, J., & McGoldrick, A. (2005). Peace journalism. Hawthorn Press.",
        locator="whole work", locator_type="work", supports="definition / war-vs-peaceorientation", verified=True),
   dict(kind="JOURNAL_ARTICLE", title_en="Peace Journalism: What, Why, Who, How, When, Where",
        title_fa="روزنامه‌نگاری صلح: چه، چرا، چه‌کسی، چگونه، چه‌زمان، کجا", authors="Galtung, J.", year=1998,
        publisher="TRANSCEND (working paper)", doi=None, url=None, language="en", isbn=None,
        citation="Galtung, J. (1998). Peace journalism: What, why, who, how, when, where. TRANSCEND.",
        locator="whole work", locator_type="work", supports="origin / conflict-analysis framework", verified=False),
 ],
 "MC-197": [
   dict(kind="BOOK", title_en="The Democratic Paradox", title_fa="پارادوکس دموکراتیک",
        authors="Mouffe, C.", year=2000, publisher="London: Verso", doi=None,
        url="https://www.versobooks.com/products/1696-the-democratic-paradox",
        language="en", isbn="9781859842799",
        citation="Mouffe, C. (2000). The democratic paradox. Verso.",
        locator="whole work", locator_type="work", supports="definition / agonism vs antagonism", verified=True),
   dict(kind="BOOK", title_en="The Return of the Political", title_fa="بازگشت امر سیاسی",
        authors="Mouffe, C.", year=1993, publisher="London: Verso", doi=None, url=None, language="en", isbn=None,
        citation="Mouffe, C. (1993). The return of the political. Verso.",
        locator="whole work", locator_type="work", supports="evolution / the political", verified=False),
 ],
 "MC-200": [
   dict(kind="BOOK", title_en="Strategic Narratives: Communication Power and the New World Order",
        title_fa="روایت‌های راهبردی: قدرت ارتباطی و نظم نوین جهانی",
        authors="Miskimmon, A., O'Loughlin, B., & Roselle, L.", year=2013,
        publisher="New York: Routledge", doi="10.4324/9781315871264",
        url="https://www.routledge.com/Strategic-Narratives-Communication-Power-and-the-New-World-Order/Miskimmon-OLoughlin-Roselle/p/book/9780415721882",
        language="en", isbn="9780415721882",
        citation="Miskimmon, A., O'Loughlin, B., & Roselle, L. (2013). Strategic narratives: Communication power and the new world order. Routledge.",
        locator="whole work", locator_type="work", supports="definition / narrative typology", verified=True),
   dict(kind="JOURNAL_ARTICLE", title_en="Strategic Narrative: A New Means to Understand Soft Power",
        title_fa="روایت راهبردی: ابزاری نو برای فهم قدرت نرم",
        authors="Roselle, L., Miskimmon, A., & O'Loughlin, B.", year=2014,
        publisher="Media, War & Conflict, 7(1), 70-84", doi=None, url=None, language="en", isbn=None,
        citation="Roselle, L., Miskimmon, A., & O'Loughlin, B. (2014). Strategic narrative: A new means to understand soft power. Media, War & Conflict, 7(1), 70-84.",
        locator="pp. 70-84", locator_type="page_range", supports="evolution / soft power link", verified=False),
 ],
}

ENRICH = {
 "MC-194": {
   "summary": "«جهانی‌محلی‌سازی» (Glocalization) به هم‌زمانی و هم‌حضوری گرایش‌های جهان‌شمول‌ساز و خاص‌ساز اشاره دارد: جهانی‌شدن نه یک‌سره همگن‌ساز است و نه یک‌سره ناهمگن‌ساز، بلکه فرایندی است که در آن امر جهانی و امر محلی یکدیگر را می‌سازند. رولند رابرتسون این مفهوم را در فصل «Glocalization: Time-Space and Homogeneity-Heterogeneity» در مجموعهٔ «Global Modernities» (۱۹۹۵، Sage) صورت‌بندی کرد (Robertson, 1995).",
   "main_problem": "آیا جهانی‌شدن به همگن‌سازی فرهنگی جهان (غربی‌شدن) می‌انجامد یا به برجسته‌شدن تفاوت‌ها و ناهمگنی، و چگونه می‌توان این دو ادعای متضاد را در یک چارچوب نظری واحد توضیح داد؟",
   "mechanism": "رابرتسون هر دو روایت رقیب را ناکافی می‌داند: «همگن‌سازی» (homogenization) که جهانی‌شدن را به گسترش یکسان الگوهای غربی فرو می‌کاهد و «ناهمگن‌سازی» (heterogenization) که آن را به تشدید تفاوت‌ها و برخورد تمدن‌ها تفسیر می‌کند. او به‌جای آن «هم‌زمانی امر جهان‌شمول و امر خاص» را پیشنهاد می‌کند: جهان‌شمول‌سازیِ خاص‌گرایی و خاص‌سازیِ جهان‌شمول‌گرایی (Robertson, 1995). اصطلاح glocalization از واژهٔ ژاپنی dochakuka (بومی‌سازی جهانی) گرفته شده و به فرایندی اشاره دارد که در آن محصولات، نهادها و قالب‌های جهانی در بسترهای محلی بازتفسیر و بازآفرینی می‌شوند و در همان حال، هویت‌های محلی در نسبت با آگاهی جهانی بازتعریف می‌گردند. رابرتسون جهانی‌شدن را «فشرده‌شدن جهان و تشدید آگاهی از جهان به‌عنوان یک کل» می‌داند (Robertson, 1992)؛ همین آگاهی جهانی است که محلی‌بودن را به امری بازتابی و نسبت‌مند بدل می‌کند. در نتیجه، «محلی» چیزی بیرون از جهانی‌شدن نیست، بلکه درون آن و در واکنش به آن ساخته می‌شود. در رسانه، این منطق در انطباق قالب‌های جهانی (مانند فرمت‌های تلویزیونی واقعیت‌نما) با فرهنگ‌های محلی، بومی‌سازی برندهای رسانه‌ای جهانی و پیدایش رسانه‌های دیاسپورایی به‌روشنی دیده می‌شود: محصول جهانی و معنا‌ی محلی در یک فرایند واحد ساخته می‌شوند.",
   "assumptions": [
     "جهانی‌شدن نه یک‌سره همگن‌ساز است و نه یک‌سره ناهمگن‌ساز.",
     "امر جهانی و امر محلی متقابلاً یکدیگر را می‌سازند.",
     "آگاهی از جهان به‌عنوان یک کل، هویت‌های محلی را بازتابی می‌کند."
   ],
   "principles": [
     "هم‌زمانی: جهان‌شمول‌سازی خاص و خاص‌سازی جهان‌شمول در هم تنیده‌اند.",
     "بازتابندگی: آگاهی جهانی، بازتعریف محلی را برمی‌انگیزد.",
     "بومی‌سازی: محصولات جهانی در بستر محلی بازآفرینی می‌شوند."
   ],
   "critiques": [
     "کاربرد شرکتی: مفهوم در گفتمان بازاریابی به شعار انطباق محصول فروکاسته و بار نظری خود را از دست داده است.",
     "کم‌رنگی قدرت: تأکید بر هم‌ساختی می‌تواند عدم تقارن قدرت میان شمال و جنوب جهانی را کم‌رنگ کند.",
     "ابهام تجربی: مرز میان بومی‌سازی اصیل و همگن‌سازی پنهان در عمل به‌سختی قابل تشخیص است."
   ],
   "applications": [
     "تحلیل انطباق قالب‌های تلویزیونی و برندهای رسانه‌ای جهانی در فرهنگ‌های محلی.",
     "پژوهش دربارهٔ رسانه‌های دیاسپورایی و هویت‌های پیوندی.",
     "مطالعهٔ محصولات فرهنگی ترکیبی و مصرف محلی رسانهٔ جهانی."
   ],
   "evolution": "رابرتسون (1992) مفهوم فشردگی جهان را صورت‌بندی کرد و (1995) آن را به هم‌زمانی جهان‌شمول-محلی گسترد. در دههٔ ۲۰۰۰، پژوهش رسانهٔ فراملی و مطالعات فرهنگی، منطق جهانی‌محلی را برای تحلیل گردش فرمت‌ها و مخاطبان پیوندی به کار گرفت.",
   "key_concepts": ["جهانی‌محلی‌سازی (glocalization)", "همگن‌سازی (homogenization)", "ناهمگن‌سازی (heterogenization)", "فشردگی جهان (compression of the world)", "بومی‌سازی (indigenization)"],
   "studies": ["Robertson, R. (1995). Glocalization. In Global Modernities (pp. 25-44). Sage.", "Robertson, R. (1992). Globalization. Sage."],
 },
 "MC-195": {
   "summary": "«روزنامه‌نگاری صلح» (Peace Journalism) رویکردی به پوشش خبری تعارض است که آگاهانه چارچوب‌های «روزنامه‌نگاری جنگ» را کنار می‌گذارد و به‌جای تمرکز بر خشونت، پیروزی و دشمن‌سازی، بر ریشه‌های تعارض، رنج غیرنظامیان و راه‌حل‌های ممکن متمرکز می‌شود. جیک لینچ و آنابل مک‌گولدریک این رویکرد را در کتاب «Peace Journalism» (۲۰۰۵، Hawthorn Press) نظام‌مند کردند (Lynch & McGoldrick, 2005).",
   "main_problem": "پوشش خبری متعارف تعارض چگونه با برجسته‌کردن خشونت، دشمن‌سازی و منطق پیروزی، خود به تشدید تعارض دامن می‌زند، و روزنامه‌نگاران چگونه می‌توانند بدون کنارگذاشتن حرفه‌گرایی، به صلح فرصت دهند؟",
   "mechanism": "لینچ و مک‌گولدریک بر پایهٔ چارچوب یوهان گالتونگ، «روزنامه‌نگاری جنگ» و «روزنامه‌نگاری صلح» را در چهار محور مقابل هم می‌گذارند: روزنامه‌نگاری جنگ «خشونت‌محور» است (بر زخم و تلفات به‌جای ریشه‌ها)، «نخبه‌محور» (بر سخنان رهبران و مقامات)، «تبلیغات‌محور» (بازتاب بی‌نقد روایت رسمی) و «پیروزی‌محور» (بردن و باختن)؛ روزنامه‌نگاری صلح در برابر آن «صلح/تعارض‌محور» است (کاوش ریشه‌ها و پیشینهٔ تعارض)، «مردم‌محور» (تجربهٔ مردم عادی در دو سوی منازعه)، «حقیقت‌محور» (کشف روایت‌های همهٔ طرف‌ها) و «راه‌حل‌محور» (گزینه‌های خروج از بحران و منطق برد-برد) (Lynch & McGoldrick, 2005). در عمل، این رویکرد به مجموعه‌ای از «انتخاب‌های تحریریه» تقلیل می‌یابد: انتخاب منبع، زبان و صفت، زاویهٔ روایت و فضایی که به صدای قربانیان و راه‌حل‌ها داده می‌شود. گالتونگ (Galtung, 1998) ریشهٔ نظری این تفکیک را در تحلیل تعارض و تفکیک «خشونت مستقیم، ساختاری و فرهنگی» می‌داند. در پوشش بحران‌های رسانه‌ای، این چارچوب توضیح می‌دهد چرا بازتولید مکرر تصاویر خشونت و زبان دشمن‌ساز، به جای روشن‌کردن ریشهٔ منازعه، به قطبی‌شدن و تشدید آن کمک می‌کند و چگونه می‌توان با گزارش‌گری ریشه‌محور و راه‌حل‌محور، فضای عمومی گفت‌وگو را گشود.",
   "assumptions": [
     "پوشش خبری تعارض بر مسیر و شدت آن اثر می‌گذارد.",
     "روزنامه‌نگار در انتخاب چارچوب روایت، عاملیت اخلاقی دارد.",
     "گزارش ریشه‌ها و راه‌حل‌ها با حرفه‌گرایی خبری سازگار است."
   ],
   "principles": [
     "چهار محور گالتونگ: صلح در برابر جنگ، مردم در برابر نخبه، حقیقت در برابر تبلیغ، راه‌حل در برابر پیروزی.",
     "ریشه‌محوری: کاوش زمینه و علل تعارض به‌جای تمرکز بر رویداد خشونت‌بار.",
     "چندصدایی: بازتاب تجربه و روایت همهٔ طرف‌ها و قربانیان."
   ],
   "critiques": [
     "اتهام جانب‌داری: منتقدان معتقدند این رویکرد روزنامه‌نگاری را به کنشگری صلح تبدیل می‌کند و بی‌طرفی خبری را تضعیف می‌کند.",
     "دشواری عملیاتی: سنجش و پیاده‌سازی «راه‌حل‌محوری» در فشار زمان و منابع خبری دشوار است.",
     "شواهد مختلط: پژوهش‌های تجربی دربارهٔ اثر واقعی این رویکرد بر مخاطب نتایج یکدستی نشان نمی‌دهند."
   ],
   "applications": [
     "پوشش حرفه‌ای بحران‌ها و درگیری‌های خشونت‌بار در رسانه‌های خبری.",
     "آموزش روزنامه‌نگاران و تدوین راهنماهای تحریریهٔ تعارض‌محور.",
     "تحلیل انتقادی چارچوب‌بندی خبری جنگ و صلح."
   ],
   "evolution": "گالتونگ (1998) چارچوب اولیه را تدوین کرد و لینچ و مک‌گولدریک (2005) آن را به راهنمای عملی روزنامه‌نگاری بدل کردند. در دههٔ ۲۰۱۰-۲۰۲۰، پژوهش تجربی دربارهٔ اثر پیام‌های صلح‌محور و کاربرد آن در پوشش بحران‌های جهانی گسترش یافت.",
   "key_concepts": ["روزنامه‌نگاری صلح (peace journalism)", "روزنامه‌نگاری جنگ (war journalism)", "چارچوب گالتونگ (Galtung's framework)", "راه‌حل‌محوری (solution orientation)", "چندصدایی (multivocality)"],
   "studies": ["Lynch, J., & McGoldrick, A. (2005). Peace Journalism. Hawthorn Press.", "Galtung, J. (1998). Peace Journalism: What, Why, Who, How, When, Where. TRANSCEND."],
 },
 "MC-197": {
   "summary": "«کثرت‌گرایی آگونیستیک» (Agonistic Pluralism) الگویی از دموکراسی است که به‌جای جست‌وجوی اجماع عقلانی، تعارض را امری سازنده و گریزناپذیر در سیاست می‌داند و می‌کوشد دشمنی را به رقابت مشروع میان «مخالفان» (adversaries) بدل کند. شانتال موف این دیدگاه را در «The Democratic Paradox» (۲۰۰۰، Verso) پروراند (Mouffe, 2000).",
   "main_problem": "چرا مدل‌های دموکراسی مشورتی که بر اجماع عقلانی تأکید می‌کنند در توضیح و مدیریت تعارض‌های سیاسی واقعی ناکام می‌مانند، و چگونه می‌توان بدون حذف تعارض، دموکراسی را زنده نگه داشت؟",
   "mechanism": "موف با تکیه بر مفهوم «امر سیاسی» (the political) — به پیروی از اشمیت — می‌گوید تعارض و تقسیم «ما/آن‌ها» سازندهٔ سیاست است و نمی‌توان آن را با گفت‌وگوی عقلانی از میان برداشت. اما او میان «آنتی‌گونیسم» (antagonism) و «آگونیسم» (agonism) تفکیک می‌کند: در آنتی‌گونیسم، طرف مقابل دشمنی است که باید حذف شود؛ در آگونیسم، او «مخالف مشروع» است که وجودش پذیرفته می‌شود و منازعه بر سر اصول دموکراتیک مشترک جریان می‌یابد (Mouffe, 2000). وظیفهٔ سیاست دموکراتیک، تبدیل آنتی‌گونیسم به آگونیسم است. موف به‌جای اجماع کامل، از «اجماع تعارضی» (conflictual consensus) سخن می‌گوید: توافق بر اصول اخلاقی-سیاسی آزادی و برابری، همراه با اختلاف پایدار بر تفسیر آن‌ها. او همچنین بر نقش «هژمونی» تأکید می‌کند — از دل آثار پیشینش با لاکلاو — یعنی هر نظم سیاسی، مفصل‌بندی موقتی از معناست که همیشه می‌تواند به چالش کشیده شود. موف مدل‌های عقلانیت‌محور را نقد می‌کند که نقش شور و عاطفه در سیاست را نادیده می‌گیرند؛ دموکراسی به جای حذف عاطفه، باید آن را در قالب رقابت آگونیستیک سازمان دهد. در رسانه، این دیدگاه توضیح می‌دهد چرا خبرِ «اجماع‌محور» اغلب صداهای مخالف را حذف می‌کند و چگونه رسانه می‌تواند با بازنمایی مخالف به‌عنوان «حریف» به‌جای «دشمن»، به سلامت فضای عمومی کمک کند — یا با دشمن‌سازی، آنتی‌گونیسم را بازتولید کند.",
   "assumptions": [
     "تعارض و تقسیم ما/آن‌ها سازندهٔ سیاست است و حذف‌شدنی نیست.",
     "دموکراسی نیازمند تبدیل دشمن به مخالف مشروع است.",
     "عاطفه و شور، نه فقط عقلانیت، در سیاست نقش دارند."
   ],
   "principles": [
     "امر سیاسی: تعارض، بنیاد سیاست است نه نقص آن.",
     "آگونیسم به‌جای آنتی‌گونیسم: رقابت مشروع جای دشمنی را می‌گیرد.",
     "اجماع تعارضی: توافق بر اصول با اختلاف بر تفسیرها."
   ],
   "critiques": [
     "ابهام مفهومی: مرز میان مخالف مشروع و دشمن در عمل مبهم می‌ماند.",
     "خطر قطبی‌شدن: تأکید بر تعارض ممکن است به توجیه شکاف‌افکنی و افراط‌گرایی بدل شود.",
     "طراحی نهادی نحیف: مدل، دستورکار نهادی مشخصی برای پیاده‌سازی ارائه نمی‌دهد."
   ],
   "applications": [
     "نقد رسانهٔ اجماع‌محور و تحلیل بازنمایی مخالفان سیاسی.",
     "پژوهش دربارهٔ فضای عمومی و کیفیت گفت‌وگوی دموکراتیک.",
     "تحلیل چارچوب‌بندی رسانه‌ای «ما/آن‌ها» در بحران‌های سیاسی."
   ],
   "evolution": "موف (1993) مفهوم امر سیاسی را طرح کرد و (2000) آن را در قالب کثرت‌گرایی آگونیستیک در برابر دموکراسی مشورتی صورت‌بندی کرد. در دههٔ ۲۰۱۰-۲۰۲۰، این چارچوب در نقد پوپولیسم و تحلیل رسانه‌های قطبی به‌کار رفت.",
   "key_concepts": ["کثرت‌گرایی آگونیستیک (agonistic pluralism)", "آنتی‌گونیسم (antagonism)", "امر سیاسی (the political)", "اجماع تعارضی (conflictual consensus)", "هژمونی (hegemony)"],
   "studies": ["Mouffe, C. (2000). The Democratic Paradox. Verso.", "Mouffe, C. (1993). The Return of the Political. Verso."],
 },
 "MC-200": {
   "summary": "«روایت‌های راهبردی» (Strategic Narratives) ابزاری برای تحلیل چگونگی ساخت و ترویج معنا توسط بازیگران سیاسی برای شکل‌دادن به درک مخاطبان از سیاست بین‌الملل است. آلیستر میسکیمون، بن او لاکلین و لورا روزل در کتاب «Strategic Narratives» (۲۰۱۳، Routledge) روایت راهبردی را به‌عنوان «ابزاری برای بازیگران سیاسی جهت ساختن معنای مشترک از گذشته، حال و آیندهٔ سیاست بین‌الملل و شکل‌دادن به رفتار بازیگران داخلی و بین‌المللی» تعریف کردند (Miskimmon, O'Loughlin, & Roselle, 2013).",
   "main_problem": "جامعه‌ها و بازیگران سیاسی چگونه از طریق روایت، نظم جهانی را معنا می‌بخشند، و چرا برخی روایت‌ها در جلب پذیرش و شکل‌دادن رفتار موفق‌ترند در حالی که برخی دیگر در «نبرد روایت‌ها» ناکام می‌مانند؟",
   "mechanism": "میسکیمون و همکاران روایت راهبردی را در سه نوع دسته‌بندی می‌کنند: «روایت‌های هویتی» (identity narratives) که پاسخ می‌دهند «ما کی هستیم» و ارزش‌ها و آرمان‌های یک بازیگر را می‌سازند؛ «روایت‌های موضوعی» (issue narratives) که توضیح می‌دهند یک موضوع (مانند تروریسم، تغییر اقلیم یا مهاجرت) چیست و چرا مهم است؛ و «روایت‌های نظام» (system narratives) که ساختار و قواعد کل نظم بین‌الملل را توصیف می‌کنند (Miskimmon et al., 2013). تحلیل روایت راهبردی در سه مرحله انجام می‌شود: «شکل‌گیری» (formation) — چگونه نخبگان روایت را در سیاست داخلی می‌سازند؛ «فرافکنی/ترویج» (projection) — چگونه روایت از طریق دیپلماسی عمومی، رسانه و ارتباطات راهبردی به مخاطبان خارجی منتقل می‌شود؛ و «دریافت/پذیرش» (reception) — چگونه مخاطبان روایت را می‌پذیرند، بازتفسیر یا رد می‌کنند. روایت از سه مؤلفهٔ «صورت» (ساختار و طرح)، «محتوا» و «گیرایی» تشکیل می‌شود. روزل و همکاران (Roselle et al., 2014) این چارچوب را به «قدرت نرم» پیوند زدند: قدرت ارتباطی، توانایی شکل‌دادن به آنچه دیگران می‌اندیشند و می‌خواهند است، و روایت راهبردی کانال اصلی اعمال این قدرت است. در رسانه، این نظریه چرایی موفقیت یا شکست کمپین‌های دیپلماسی عمومی، رسانه‌های دولتی فرامرزی و روایت‌سازی انتخاباتی را توضیح می‌دهد: روایتی که با تجربهٔ زیستهٔ مخاطب هم‌خوان نباشد، در مرحلهٔ دریافت شکست می‌خورد، هرچند در مرحلهٔ فرافکنی پرهزینه و گسترده بوده باشد.",
   "assumptions": [
     "بازیگران سیاسی آگاهانه و راهبردی روایت می‌سازند و ترویج می‌کنند.",
     "معنای سیاست بین‌الملل از طریق روایت‌ها ساخته و رقابتی می‌شود.",
     "اثربخشی روایت به مرحلهٔ دریافت و پذیرش مخاطب وابسته است."
   ],
   "principles": [
     "سه نوع روایت: هویتی، موضوعی و نظام.",
     "سه مرحله: شکل‌گیری، فرافکنی و دریافت.",
     "قدرت ارتباطی: روایت، کانال اعمال قدرت نرم است."
   ],
   "critiques": [
     "کم‌توجهی به دریافت: مرحلهٔ پذیرش مخاطب در مقایسه با شکل‌گیری و فرافکنی کم‌نظریه‌پردازی شده است.",
     "اغراق در عاملیت: فرض ساخت آگاهانهٔ روایت، نقش تصادف و ساختار را کم‌رنگ می‌کند.",
     "هم‌پوشانی مفهومی: مرز روایت راهبردی با چارچوب‌بندی و تبلیغات در عمل مبهم است."
   ],
   "applications": [
     "تحلیل دیپلماسی عمومی و کمپین‌های ارتباطات راهبردی دولت‌ها.",
     "پژوهش دربارهٔ رسانه‌های دولتی فرامرزی و نبرد روایت‌ها.",
     "تحلیل روایت‌سازی در انتخابات و بحران‌های سیاست خارجی."
   ],
   "evolution": "میسکیمون و همکاران (2013) چارچوب را نظام‌مند کردند و روزل و همکاران (2014) آن را به قدرت نرم پیوند زدند. در دههٔ ۲۰۲۰، پژوهش روایت راهبردی به تحلیل جنگ اوکراین، رقابت رسانه‌ای جهانی و روایت‌های هوش مصنوعی گسترش یافت.",
   "key_concepts": ["روایت راهبردی (strategic narrative)", "روایت هویتی (identity narrative)", "روایت نظام (system narrative)", "قدرت ارتباطی (communication power)", "فرافکنی و دریافت (projection and reception)"],
   "studies": ["Miskimmon, A., O'Loughlin, B., & Roselle, L. (2013). Strategic Narratives. Routledge.", "Roselle, L., Miskimmon, A., & O'Loughlin, B. (2014). Strategic narrative. Media, War & Conflict, 7(1), 70-84."],
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
    codes = ["MC-194", "MC-195", "MC-197", "MC-200"]
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
    print("BATCH48 THEORY DONE")

if __name__ == "__main__":
    main()
