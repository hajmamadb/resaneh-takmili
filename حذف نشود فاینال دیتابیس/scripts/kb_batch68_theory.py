# -*- coding: utf-8 -*-
"""Batch 68: MC-359 (imagined audience), MC-360 (diffuse media / itinerant audiences),
MC-362 (indexing theory), MC-364 (development journalism).
MC-360 had active-audience boilerplate and MC-362 garbled agenda-setting text -> rewritten."""
import pymysql, json

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch68-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch68_theory.json"

S = {
 "MC-359": [
   dict(kind="JOURNAL_ARTICLE", title_en="Knock, Knock. Who's There? The Imagined Audience",
        title_fa="تق‌تق، کیست؟ مخاطب خیالی",
        authors="Litt, E.", year=2012,
        publisher="Journal of Broadcasting & Electronic Media, 56(3), 330-345",
        doi="10.1080/08838151.2012.705195", url="https://www.tandfonline.com/doi/abs/10.1080/08838151.2012.705195",
        language="en", isbn=None,
        citation="Litt, E. (2012). Knock, knock. Who's there? The imagined audience. Journal of Broadcasting & Electronic Media, 56(3), 330-345. https://doi.org/10.1080/08838151.2012.705195",
        locator="pp. 330-345", locator_type="page_range",
        supports="definition / mechanism / empirical evidence", verified=True),
   dict(kind="JOURNAL_ARTICLE", title_en="I Tweet Honestly, I Tweet Passionately: Twitter Users, Context Collapse, and the Imagined Audience",
        title_fa="صادقانه توییت می‌کنم، پرشور توییت می‌کنم: کاربران توییتر، فروریزش بافت و مخاطب خیالی",
        authors="Marwick, A. E., & boyd, d.", year=2011,
        publisher="New Media & Society, 13(1), 114-133",
        doi=None, url=None, language="en", isbn=None,
        citation="Marwick, A. E., & boyd, d. (2011). I tweet honestly, I tweet passionately: Twitter users, context collapse, and the imagined audience. New Media & Society, 13(1), 114-133.",
        locator="pp. 114-133", locator_type="page_range",
        supports="evolution / context collapse", verified=False),
 ],
 "MC-360": [
   dict(kind="BOOK", title_en="Critique of Information", title_fa="نقد اطلاعات",
        authors="Lash, S.", year=2002,
        publisher="SAGE Publications", doi=None, url=None, language="en", isbn="0-7619-5269-1",
        citation="Lash, S. (2002). Critique of information. SAGE Publications.",
        locator="whole work", locator_type="work",
        supports="definition / disembodied information / itinerant audience", verified=True),
   dict(kind="BOOK", title_en="Another Modernity: A Different Rationality",
        title_fa="مدرنیته‌ای دیگر: عقلانیتی متفاوت",
        authors="Lash, S.", year=1999,
        publisher="Blackwell", doi=None, url=None, language="en", isbn=None,
        citation="Lash, S. (1999). Another modernity: A different rationality. Blackwell.",
        locator="whole work", locator_type="work",
        supports="evolution / reflexive modernization", verified=False),
 ],
 "MC-362": [
   dict(kind="JOURNAL_ARTICLE", title_en="Toward a Theory of Press-State Relations in the United States",
        title_fa="در جهت نظریه‌ای دربارهٔ روابط مطبوعات و دولت در آمریکا",
        authors="Bennett, W. L.", year=1990,
        publisher="Journal of Communication, 40(2), 103-127",
        doi="10.1111/j.1460-2466.1990.tb02265.x", url="https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1460-2466.1990.tb02265.x",
        language="en", isbn=None,
        citation="Bennett, W. L. (1990). Toward a theory of press-state relations in the United States. Journal of Communication, 40(2), 103-127. https://doi.org/10.1111/j.1460-2466.1990.tb02265.x",
        locator="pp. 103-127", locator_type="page_range",
        supports="definition / indexing hypothesis / methodology", verified=True),
   dict(kind="BOOK", title_en="When the Press Fails: Political Power and the News Media from Iraq to Katrina",
        title_fa="وقتی مطبوعات ناکام می‌مانند: قدرت سیاسی و رسانهٔ خبری از عراق تا کاترینا",
        authors="Bennett, W. L., Lawrence, R. G., & Livingston, S.", year=2007,
        publisher="University of Chicago Press", doi=None, url=None, language="en", isbn=None,
        citation="Bennett, W. L., Lawrence, R. G., & Livingston, S. (2007). When the press fails: Political power and the news media from Iraq to Katrina. University of Chicago Press.",
        locator="whole work", locator_type="work",
        supports="evolution / failures of indexing", verified=False),
 ],
 "MC-364": [
   dict(kind="BOOK_CHAPTER", title_en="Development Journalism", title_fa="روزنامه‌نگاری توسعه",
        authors="Xu Xiaoge", year=2009,
        publisher="Routledge (in K. Wahl-Jorgensen & T. Hanitzsch, Eds., The Handbook of Journalism Studies, pp. 357-369)",
        doi="10.4324/9780203877685-36", url="https://www.taylorfrancis.com/chapters/edit/10.4324/9780203877685-36/development-journalism-xu-xiaoge",
        language="en", isbn=None,
        citation="Xu, X. (2009). Development journalism. In K. Wahl-Jorgensen & T. Hanitzsch (Eds.), The handbook of journalism studies (pp. 357-369). Routledge.",
        locator="pp. 357-369", locator_type="CHAPTER",
        supports="definition / origin / critique", verified=True),
   dict(kind="REPORT", title_en="Many Voices, One World: Communication and Society Today and Tomorrow",
        title_fa="صداهای بسیار، جهانی یگانه: ارتباطات و جامعه امروز و فردا",
        authors="UNESCO (International Commission for the Study of Communication Problems)",
        year=1980, publisher="UNESCO", doi=None, url=None, language="en", isbn=None,
        citation="UNESCO. (1980). Many voices, one world: Communication and society today and tomorrow. UNESCO.",
        locator="whole work", locator_type="work",
        supports="context / new world information order debate", verified=False),
 ],
}

VOID = "در بستر رسانه، "
ENRICH = {
 "MC-359": {
  "summary": "(لیت، ۲۰۱۲؛ مارویک و بوید، ۲۰۱۱) «مخاطب خیالی» سازه‌ای است که توضیح می‌دهد کاربر در رسانهٔ اجتماعی، هنگام انتشار، تصویری ذهنی از گیرندگان می‌سازد و محتوا، لحن و سطح افشای خود را بر اساس همان تصویر تنظیم می‌کند — حتی اگر آن گیرندگان واقعی هرگز آنچه او می‌پندارد نبینند.",
  "definition": "مخاطب خیالی، بازنمایی ذهنی کاربر از خوانندگان بالقوهٔ پیام است که در غیاب بازخورد مستقیم و در میان مخاطبان نامرئی و ناهمگون، راهنمای تصمیم‌های او دربارهٔ «چه بگویم، چگونه بگویم و چه نگویم» می‌شود.",
  "main_problem": "در تعامل رودررو، مخاطب حاضر است و می‌توان واکنش او را دید؛ اما در شبکهٔ اجتماعی مخاطب غایب، کثیر و نامرئی است. کاربر چگونه این غیبت را جبران می‌کند و این جبران چه اثری بر شکل و صداقت محتوا دارد.",
  "mechanism": "\n".join([
   "(۱) غیبت مخاطب و ابهام زمینه: پلتفرم، مخاطبان ناهمگون را در یک فید جمع می‌کند؛ کاربر نمی‌داند چه کسی می‌بیند و ازاین‌رو ناچار به ساختن تصویر ذهنی است.",
   "(۲) فروریزش بافت: مارویک و بوید نشان دادند ناظران از پیش‌تعریف‌نشده، مرزهای مخاطب خصوصی و عمومی را در هم می‌ریزند و کاربر باید هم‌زمان برای گروه‌های ناهمگون اجرا کند.",
   "(۳) تنظیم اجرا: کاربر با توجه به مخاطب خیالی، موضوع، لحن، سطح صراحت و حتی زمان انتشار را برمی‌گزیند؛ مخاطب خیالی نقش «تماشاگر تعمیم‌یافته» گافمن را در فضای دیجیتال بازی می‌کند.",
   "(۴) سه‌گانهٔ برداشت، انتخاب و پالایش: پست روی صفحه، آینهٔ همهٔ اندیشه‌ها نیست؛ بخشی از آنچه به ذهن می‌رسد نه برداشت می‌شود، نه انتخاب، و نه در نهایت پالایش‌شده منتشر می‌شود.",
   "(۵) بازخورد ایموجی و متریک: لایک و بازدید، تنها نشانه‌های مبهم مخاطب‌اند و تصویر ذهنی را کامل اصلاح نمی‌کنند؛ ازاین‌رو مخاطب خیالی پایدار می‌ماند.",
   VOID + "یک دانشجو دربارهٔ وضعیت دانشگاه پست می‌نویسد و با آنکه پست «فقط برای دوستان» است، کارفرمای آینده را نیز در ذهنش حاضر می‌کند و لحن را تلطیف می‌کند — همان سازوکار مخاطب خیالی که شکل عمومی‌شدن پیام را تغییر می‌دهد.",
  ]),
  "assumptions": [
   "کاربر در محیط دیجیتال، به‌جای نشانه‌های واقعی مخاطب، بر تصویر ذهنی خود تکیه می‌کند.",
   "تصویر ذهنی مخاطب، رفتار انتشار را مستقل از ترکیب واقعی مخاطبان جهت می‌دهد.",
   "ابهام و فروریزش بافت، ویژگی ساختاری پلتفرم‌های اجتماعی است.",
  ],
  "principles": [
   "مخاطب رسانهٔ اجتماعی نه یک واقعیت شمارش‌پذیر، بلکه سازهٔ ادراکی کاربر است.",
   "اجرا و صداقت آنلاین، تابع پیش‌بینی واکنش مخاطب خیالی است.",
   "طراحی پلتفرم (حریم، مخاطب پیش‌فرض، متریک) تصویر خیالی را شکل می‌دهد.",
  ],
  "critiques": [
   "شکاف خودگزارش و رفتار واقعی: آنچه کاربران می‌گویند «در ذهن دارند» با آنچه واقعاً منتشر می‌کنند همیشه همخوان نیست.",
   "محدودیت فرهنگی و پلتفرمی: بیشتر پژوهش‌ها بر دانشجویان آمریکایی متمرکزند و تعمیم به فرهنگ‌ها و پلتفرم‌های با حریم سخت‌گیرانه نیازمند بررسی است.",
   "سنجش دشوار تصویر ذهنی: مخاطب خیالی سازه‌ای درونی است و اندازه‌گیری آن عمدتاً به گزارش خودِ کاربر وابسته می‌ماند.",
   "نامرئی‌ماندن ساختار: تمرکز بر ادراک کاربر، سهم الگوریتم و طراحی رابط را در ایجاد مخاطب نامرئی کم‌رنگ می‌کند.",
  ],
  "applications": [
   "طراحی حریم و کنترل مخاطب در پلتفرم: نشانه‌های دقیق‌تر از «چه کسی می‌بیند» می‌تواند تصویر خیالی را واقعی‌تر کند.",
   "آموزش سواد دیجیتال: آگاهی از مخاطب خیالی و فروریزش بافت، بخشی از مهارت انتشار مسئولانه است.",
   "پژوهش خودارزیابی آنلاین: تحلیل فاصلهٔ میان پست‌های منتشرشده و پیش‌بینی‌های کاربر از واکنش مخاطب.",
   "مدیریت بحران برند: پیش‌بینی اینکه یک پست در نگاه مخاطبان مختلف چگونه خوانده می‌شود.",
  ],
  "evolution": "از مفهوم «تماشاگر تعمیم‌یافته» گافمن و «مخاطب ساخته‌شده» در سنت دریافت، به پژوهش‌های تجربی رسانهٔ اجتماعی (لیت، ۲۰۱۲؛ مارویک و بوید، ۲۰۱۱) و امروز به مطالعهٔ مخاطب خیالی الگوریتمی و پیام‌های هوش مصنوعی.",
  "key_concepts": ["مخاطب خیالی (Imagined Audience)", "فروریزش بافت (Context Collapse)", "مخاطب نامرئی (Invisible Audience)", "اجرای خود (Self-presentation)", "پالایش پیام (Message Curation)", "حریم شبکه‌ای (Networked Privacy)"],
  "studies": [
   "Marwick, A. E., & boyd, d. (2011). I tweet honestly, I tweet passionately: Twitter users, context collapse, and the imagined audience. New Media & Society, 13(1), 114-133.",
   "Litt, E., & Hargittai, E. (2016). The imagined audience on social network sites. Social Media + Society, 2(1).",
  ],
  "detailed_analysis": "\n".join([
   "۱. بنیان و منطق نظری: مخاطب خیالی حلقهٔ واسط میان ساختار پلتفرم و کنش کاربر است؛ نه پلتفرم مستقیماً رفتار را تعیین می‌کند و نه کاربر کاملاً آزاد است — تصویر ذهنی، نقطهٔ تلاقی این دو است.",
   "۲. پیوند با سنت اجرا: گافمن توضیح داد که هر اجرا نیازمند تماشاگر ادراک‌شده است؛ لیت همان سازوکار را از صحنهٔ رودررو به فید دیجیتال منتقل کرد، جایی که تماشاگر واقعاً حاضر نیست.",
   "۳. پیامدهای طراحی و سیاست: اگر مخاطب خیالی نادرست باشد، حریم خصوصی واقعی با ادراک کاربر شکاف پیدا می‌کند؛ ازاین‌رو نشانه‌های شفاف مخاطب، نه فقط تسهیل‌گر، بلکه مسئله‌ای حقوقی است.",
  ]),
  "critique_text": "\n".join([
   "۱. شکاف خودگزارش و رفتار واقعی: آنچه کاربران می‌گویند «در ذهن دارند» با آنچه واقعاً منتشر می‌کنند همیشه همخوان نیست.",
   "۲. محدودیت فرهنگی و پلتفرمی: بیشتر پژوهش‌ها بر دانشجویان آمریکایی متمرکزند و تعمیم به فرهنگ‌ها و پلتفرم‌های با حریم سخت‌گیرانه نیازمند بررسی است.",
   "۳. سنجش دشوار تصویر ذهنی: مخاطب خیالی سازه‌ای درونی است و اندازه‌گیری آن عمدتاً به گزارش خودِ کاربر وابسته می‌ماند.",
   "۴. نامرئی‌ماندن ساختار: تمرکز بر ادراک کاربر، سهم الگوریتم و طراحی رابط را در ایجاد مخاطب نامرئی کم‌رنگ می‌کند.",
  ]),
  "example_text": "\n".join([
   "دانشجویی دربارهٔ شرایط سیاسی دانشگاه در صفحه‌اش می‌نویسد؛ حتی وقتی «فقط دوستان» پست رمی‌بینند، او کارفرمای آینده را «خیال» می‌کند و پست را حذف می‌کند یا آن را به اشارهٔ ضمنی بدل می‌سازد.",
   "یک اینفلوئنسر پیش از انتشار یک ویدئو، در ذهنش سه مخاطب را هم‌زمان حاضر می‌کند: هوادار، منتقد و خانواده؛ لحن نهایی در چانه‌زنی میان همین سه تصویر انتخاب می‌شود.",
   "در یک گروه خانوادگی پیام‌رسان، کاربر برای پست شوخ‌طبعانه روز گذشتهٔ خود، پیش از انتشار در گروه کاری، همان متن را با مخاطب خیالی دیگری بازنویسی می‌کند — نمونهٔ روزمرهٔ تنظیم اجرا بر اساس مخاطب خیالی.",
  ]),
 },
 "MC-360": {
  "summary": "(لش، ۲۰۰۲) «رسانه‌های پراکنده» اشاره به وضعیتی دارد که در آن اطلاعات از بافت‌های تاریخی، جغرافیایی و روایی خود کنده و همچون قطعات آمادهٔ مصرف توزیع می‌شود. مخاطب در این وضعیت دیگر در برابر متن می‌ایستد؛ خود میان رسانه‌ها «سرگردان» حرکت می‌کند و معنا را از قطعات جدا و بی‌بافت جمع می‌آورد.",
  "definition": "رسانهٔ پراکنده، نظام توزیع اطلاعاتی است که بر جداسازی اطلاعات از زمینه، حرکت آن در شبکه‌ها و انطباق آن با موقعیت‌های مصرف مقطعی استوار است؛ مخاطب غیرمستقر، مصرف‌کننده‌ای است که ثبات یا تعلق پایدار به رسانهٔ واحدی ندارد.",
  "main_problem": "چگونه اطلاعات در جامعهٔ داده‌محور، از بازنمایی معنادار به جریان فزایندهٔ داده تبدیل می‌شود و مخاطبی که این جریان را مصرف می‌کند، چه نوع تعلقی به رسانه‌ها دارد؟ لش این پرسش را دربارهٔ نسبت نقد فرهنگی با سرعت اطلاعات مطرح می‌کند.",
  "mechanism": "\n".join([
   "(۱) اطلاعات ازجا‌کنده: داده برخلاف روایت، خودبسنده و بی‌بافت است؛ همین بی‌بافتی، سرعت گردش آن را ممکن و بازسازی معنا را به مخاطب واگذار می‌کند.",
   "(۲) سرعت به‌جای عمق: در نظام اطلاعات، ارزش پیام کمتر به درک و بیشتر به انتقال سریع وابسته است؛ همین جابه‌جایی، اولویت‌های نقد فرهنگی را دگرگون می‌کند.",
   "(۳) مخاطب غیرمستقر: مخاطب در میان پلتفرم‌ها و شرایط مختلف مصرف جابه‌جا می‌شود و هویت رسانه‌ای ثابتی ندارد؛ تعلق او به جریان‌ها بیشتر موقتی است.",
   "(۴) نقد درون‌نظام: لش نشان می‌دهد نقد فرهنگی امروز از بیرون نظام ممکن نیست؛ اندیشه‌ها هم در همان نظام اطلاعاتی و با همان سرعت تولید و بازتوزیع می‌شوند.",
   "(۵) بازگشت خودآگاهانه به بافت: اگر اطلاعات بی‌بافت است، بازسازی بافت، کار اصلی مخاطب و پژوهشگر می‌شود؛ ازاین‌رو تعیین منبع و زمینه، خود کنشی تحلیلی است.",
   VOID + "فید خبری، اسکرین‌شات، تیکه‌کلیپ‌ها و بازنشرهای بی‌ارجاع، نمونه‌های عینی هستند: همان خبر در دو بافت مختلف، معنای متفاوت می‌سازد و مخاطب سرگردان میان فیدها، ناچار از تعیین دستی بافت است.",
  ]),
  "assumptions": [
   "جامعهٔ معاصر از بازنمایی به اطلاعات تغییر کرده است و این تغییر کیفیتی، نه کمّی است.",
   "اطلاعات به‌طور ساختاری از بافت جدا و قابل انتقال است.",
   "مخاطب امروزین، ثبات رسانه‌ای ندارد و در فضاهای مختلف جابه‌جا می‌شود.",
  ],
  "principles": [
   "نقد رسانه باید به سطح سازوکارهای اطلاعاتی، نه فقط محتوای بازنمایی‌ها، نفوذ کند.",
   "نسبت مخاطب و رسانه را باید با مفاهیم تحرک و مقطعی‌بودن توصیف کرد.",
   "بازسازی بافت، کار اصلی تفسیر در محیط داده‌محور است.",
  ],
  "critiques": [
   "ابهام تجربی: مفاهیمی مانند «اطلاعات‌محوری» و «سرگردانی» به‌سختی به شاخص‌های سنجش‌پذیر تبدیل می‌شوند.",
   "تعمیم از نمونه‌های نخبگانه: تحلیل لش بر تجربهٔ نخبگان فرهنگی استوار است و پوشش تجربهٔ گروه‌های دیگر را ادعا نمی‌کند.",
   "کم‌رنگی ساختار مالکیت: تحلیل اطلاعات از مناسبات مالکیت و اقتصاد توجه، تا حدی مستقل نقد می‌شود.",
   "پیش‌بینی دشوار: تغییرات سریع پلتفرم‌ها، نقد لش را با نسل بعدی رسانه‌ها ناسازگار کرده است.",
  ],
  "applications": [
   "تحلیل جریان خبری بی‌ارجاع: چگونه بریدن از بافت، تفسیرهای متناقض می‌سازد.",
   "مطالعهٔ مصرف رسانه‌ای چندپلتفرمی: مخاطبی که بین شبکه‌ها، پادکست و استریم جابه‌جا می‌شود.",
   "بازسازی بافت در روایت بصری: اهمیت زیرنویس، زمان و مکان در بازنشر ویدئو.",
   "نقد داده‌محور شدن خبر: از روایت رسانه‌ای به جریان داده و تغییر معیارهای اعتبار.",
  ],
  "evolution": "از نقد لش بر مدرنیتهٔ بازتابی (۱۹۹۹) به نقد اطلاعات (۲۰۰۲)، سپس به ادبیات حاکمیت داده و تحلیل‌های انتقادی پلتفرم؛ در پژوهش رسانه، به مطالعات کم‌توجهی به مفهوم مخاطب غیرمستقر راه یافت.",
  "key_concepts": ["اطلاعات مجرد (Disembodied Information)", "رسانهٔ پراکنده (Diffuse Media)", "مخاطب غیرمستقر (Itinerant Audience)", "نقد اطلاعات (Critique of Information)", "بازسازی بافت (Recontextualization)", "جامعهٔ داده‌محور (Data-Driven Society)"],
  "studies": [
   "Lash, S. (2002). Critique of information. SAGE Publications.",
   "Lash, S. (1999). Another modernity: A different rationality. Blackwell.",
  ],
  "detailed_analysis": "\n".join([
   "۱. بنیان و منطق نظری: لش در سنت جامعه‌شناسی فرهنگ و نظریهٔ اجتماعی می‌نویسد و می‌کوشد پاسخ «صنعت فرهنگ» آدورنو را برای دورهٔ شبکه‌ها بازنویسی کند: اگر فرهنگ دیگر از مرکزی واحد توزیع نمی‌شود، نقد هم نمی‌تواند از بیرون آن بایستد.",
   "۲. پیوند با مطالعات مخاطب: مفهوم مخاطب غیرمستقر، پاسخ لش به دوگانهٔ مخاطب فعال/منفعل است؛ در وضعیت اطلاعاتی، نه فعالیت تفسیری کافی است و نه منفعل‌بودن کامل — مخاطب در حرکت است و همین حرکت، منبع تنش اوست.",
   "۳. افق امروز: در عصر الگوریتم و بازنشر ماشینی، فاصلهٔ اطلاعات از بافت بیشتر شده است؛ تحلیل لش همچنان ابزاری برای پرسش از شرایط اعتبار و مسئولیت در جریان اطلاعات است.",
  ]),
  "critique_text": "\n".join([
   "۱. ابهام تجربی: مفاهیمی مانند «اطلاعات‌محوری» و «سرگردانی» به‌سختی به شاخص‌های سنجش‌پذیر تبدیل می‌شوند.",
   "۲. تعمیم از نمونه‌های نخبگانه: تحلیل لش بر تجربهٔ نخبگان فرهنگی استوار است و پوشش تجربهٔ گروه‌های دیگر را ادعا نمی‌کند.",
   "۳. کم‌رنگی ساختار مالکیت: تحلیل اطلاعات از مناسبات مالکیت و اقتصاد توجه، تا حدی مستقل نقد می‌شود.",
   "۴. پیش‌بینی دشوار: تغییرات سریع پلتفرم‌ها، نقد لش را با نسل بعدی رسانه‌ها ناسازگار کرده است.",
  ]),
  "example_text": "\n".join([
   "یک کلیپ کوتاه از کنفرانسی، بدون نام گوینده و تاریخ، در چند بازنشر معنای خود را از دست می‌دهد و به «دلیل» تبدیل می‌شود؛ لش این را جدایی اطلاعات از بافت می‌نامد.",
   "مخاطبی که پنجرهٔ اخبارش ترکیبی از فید خبری، پیام‌رسان و پادکست است، هر بار با قطعه‌ای از یک روایت روبه‌روست؛ اگر خودش بافت نسازد، معنایی شکل نمی‌گیرد.",
   "در یک کمپین تبلیغاتی، برند داده‌های مصرف را بی‌زمینه می‌خواند و مخاطب را «بازاری برای مرحلهٔ بعد» می‌بیند — نمونۀ مصرف مخاطب غیرمستقر در قالب داده.",
  ]),
 },
 "MC-362": {
  "summary": "(بنت، ۱۹۹۰) نظریهٔ نمایه‌کردن می‌گوید دامنهٔ صداهایی که رسانهٔ خبری منتشر می‌کند، تا حد زیادی بازتاب دامنهٔ اختلاف و اجماع درون نخبگان سیاسی است. هرگاه نخبگان دربارهٔ مسئله‌ای اختلافی جدی داشته باشند، مرزهای دیدگاه منتشرشده گسترده می‌شود؛ هرگاه اجماع داشته باشند، همان مرز تنگ باقی می‌ماند.",
  "definition": "نمایه‌کردن خبر، سازوکاری است که طی آن رسانهٔ خبری، طیف دیدگاه‌های منتشرشده را با «نمایه‌ای» از استدلال‌های منبع نخبگان دولتی تنظیم می‌کند؛ نه با مستقل‌سنجی مستقل واقعیت.",
  "main_problem": "چرا رسانه‌های حرفه‌ای در دوره‌های اجماع نخبگان، دیدگاه‌های بدیل را چندان منتشر نمی‌کنند و در دوره‌های اختلاف، ناگهان صدای گروه‌های دیگری شنیده می‌شود؟ بنت این تغییر را نه به تعادل بی‌طرفانه، بلکه به ساختار منابع قدرت نسبت می‌دهد.",
  "mechanism": "\n".join([
   "(۱) تکیه بر منبع رسمی: خبرنگاران برای دسترسی به اطلاعات، اعتبار و دسترسی، به منابع نهادی وابسته‌اند؛ همین وابستگی، مرزهای گفتار قابل نقل را تعیین می‌کند.",
   "(۲) نرم‌های حرفه‌ای نامتقارن: عینیت و تعادل، اغلب به معنای نقل همان نظام مباحثهٔ نخبگان است؛ پس تعادل رسانه‌ای، تعادل نیروهای اجتماعی نیست.",
   "(۳) اجماع و اختلاف: در اجماع نخبگان، رسانه دیدگاه‌های ناهمخوان را حاشیه‌ای می‌کند؛ در اختلاف، فضای مصاحبه و گزارش بازتر می‌شود.",
   "(۴) فرض‌های زمینه‌ای: آنچه همهٔ نخبگان می‌پذیرند، در خبر به‌عنوان پیش‌فرض باقی می‌ماند و از تحلیل خارج می‌شود؛ همین پیش‌فرض‌ها، حد نهایی نمایه‌کردن‌اند.",
   "(۵) شمشیر دو لبه: نمایه‌کردن هم محدودیت رسانه است و هم سازوکاری برای اتصال رسانه به نظام تصمیم‌گیری؛ ازاین‌رو نه «توطئه» است و نه «بی‌طرفی».",
   VOID + "در پوشش یک مناقشهٔ سیاست خارجی، رسانه تا زمانی که دو حزب اصلی در دولت اختلاف دارند، صدای مخالفان را منتشر می‌کند؛ اما پس از اجماع دو حزب، همان رسانه مخالفان را به حاشیه می‌راند — نمونهٔ روشن نمایه‌کردن.",
  ]),
  "assumptions": [
   "منابع اصلی خبر، نهادهای رسمی و نخبگان سیاسی‌اند.",
   "نرم‌های حرفه‌ای خبرنگاری، مرزهای نقل دیدگاه را مقید می‌کند.",
   "دامنهٔ دیدگاه‌های منتشرشده، تابع دامنهٔ اختلاف درون نخبگان است.",
  ],
  "principles": [
   "تحلیل خبر باید سطح نخبگان سیاسی و منابع رسمی را در مرکز قرار دهد.",
   "اجماع و اختلاف نخبگان، معیار سنجش فرصت گفتار بدیل است.",
   "پیش‌فرض‌های مشترک نخبگان، آنچه خارج از بحث می‌ماند را روشن می‌کند.",
  ],
  "critiques": [
   "کم‌رنگی صداهای غیرنخبگان: نظریه، رسانه را در برابر افکار عمومی و جنبش‌های اجتماعی نسبتاً ناتوان نشان می‌دهد و نقش منابع محلی و شهروندی را کم‌رنگ می‌کند.",
   "سنجش دشوار اجماع: تعریف عملیاتی «اختلاف نخبگان» و «مرز دیدگاه» محل مناقشه است و اعتبارسنجی آن دشوار می‌شود.",
   "تغییر محیط رسانه: با ظهور پلتفرم‌ها، منابع خبری از انحصار نخبگان خارج شده‌اند و نظریه نیازمند به‌روزرسانی است.",
   "خطر جبرگرایی: اگر همه‌چیز تابع نخبگان باشد، امکان استقلال و اصلاح را در رسانه‌های حرفه‌ای کافی نمی‌بیند.",
  ],
  "applications": [
   "تحلیل پوشش مناقشه‌های سیاسی: ردیابی تغییر دامنهٔ منابع در دوره‌های اختلاف و اجماع.",
   "پژوهش سیاست خارجی و رسانه: بررسی اینکه چگونه اجماع دو حزبی، افق بحث را تنگ می‌کند.",
   "مطالعهٔ منابع خبر در بحران: سهم مقامات، کارشناسان و نهادهای بین‌المللی در روایت بحران.",
   "نقد رسانه در دورهٔ پلتفرمی: گسترش منابع به بازیگران شبکه‌ای و تأثیر آن بر نظریه.",
  ],
  "evolution": "بنت در دههٔ ۲۰۰۰ نظریه را با شواهد پوشش عراق (۲۰۰۷) و نقص رسانه در بحران‌ها توسعه داد؛ پس از آن، پژوهش‌های پلتفرمی به بازتعریف نمایه‌کردن در محیط رسانه‌ای چندمنبعی پرداختند.",
  "key_concepts": ["نمایه‌کردن خبر (News Indexing)", "نخبگان سیاسی (Political Elites)", "نرم حرفه‌ای (Professional Norm)", "اجماع نخبگان (Elite Consensus)", "منبع رسمی (Official Source)", "افق گفتار (Range of Debate)"],
  "studies": [
   "Bennett, W. L. (1990). Toward a theory of press-state relations in the United States. Journal of Communication, 40(2), 103-127.",
   "Bennett, W. L., Lawrence, R. G., & Livingston, S. (2007). When the press fails. University of Chicago Press.",
  ],
  "detailed_analysis": "\n".join([
   "۱. بنیان و منطق نظری: نظریه در تقاطع دو سنت قرار دارد: مطالعات اثر رسانه و جامعه‌شناسی نهادهای سیاسی. سهم آن، توضیح چگونگی شکل‌گیری «حدود بحث» در خبر بدون نیاز به فرض توطئه است.",
   "۲. روش و شاهد: بنت پوشش رسانه‌ای یک مناقشهٔ نیکاراگوئه‌ای را مطالعه کرد و نشان داد تغییر در مرز دیدگاه، با اختلاف نخبگان همبستگی دارد؛ این الگو بعدها در پوشش جنگ عراق و بحران‌های دیگر بازتولید شد.",
   "۳. محدودیت امروز: در محیط خبری چندمنبعی، مرز دیدگاه دیگر فقط از نخبگان نمی‌آید؛ رسانه‌های حزبی، اینفلوئنسرها و محتوای کاربرساخته، هم‌زمان فرصت و آشفتگی جدید ساخته‌اند که نظریه باید آن را توضیح دهد.",
  ]),
  "critique_text": "\n".join([
   "۱. کم‌رنگی صداهای غیرنخبگان: نظریه، رسانه را در برابر افکار عمومی و جنبش‌های اجتماعی نسبتاً ناتوان نشان می‌دهد و نقش منابع محلی و شهروندی را کم‌رنگ می‌کند.",
   "۲. سنجش دشوار اجماع: تعریف عملیاتی «اختلاف نخبگان» و «مرز دیدگاه» محل مناقشه است و اعتبارسنجی آن دشوار می‌شود.",
   "۳. تغییر محیط رسانه: با ظهور پلتفرم‌ها، منابع خبری از انحصار نخبگان خارج شده‌اند و نظریه نیازمند به‌روزرسانی است.",
   "۴. خطر جبرگرایی: اگر همه‌چیز تابع نخبگان باشد، امکان استقلال و اصلاح را در رسانه‌های حرفه‌ای کافی نمی‌بیند.",
  ]),
  "example_text": "\n".join([
   "تا زمانی که دو حزب اصلی در دولت دربارهٔ یک مناقشهٔ خارجی اختلاف داشتند، خبرهای صداهای مخالف هم منتشر می‌شد؛ پس از اجماع دو حزب، همان خبرها به حاشیه رفتند — نمونهٔ کلاسیک نمایه‌کردن.",
   "در پوشش یک بحران طبیعی، رسانه از منبع رسمی، کارشناس و سازمان‌های امدادی نقل می‌کند؛ صدای آسیب‌دیدگان تا وقتی مقامی به آن اشاره نکند کمتر به خبر می‌رسد.",
   "در دورهٔ رسانه‌های پلتفرمی، منابع خبری دیگر محدود به نخبگان نیست؛ با این حال، سیاست‌های احراز اعتبار پلتفرم دوباره به سمت منابع رسمی برگشته است — بازتولید نمایه‌کردن به شکل تازه.",
  ]),
 },
 "MC-364": {
  "summary": "(شو شیائوژه، ۲۰۰۹؛ یونسکو، ۱۹۸۰) روزنامه‌نگاری توسعه، جریانی است که در اواخر دههٔ ۱۹۶۰ در آسیا شکل گرفت و خبر را ابزاری برای آموزش، همبستگی اجتماعی و پیشبرد برنامه‌های توسعه می‌دانست. در این نگاه، روزنامه‌نگار نه ناظر بی‌طرف، بلکه مشارکتی در پروژهٔ ملی توسعه است.",
  "definition": "روزنامه‌نگاری توسعه، الگویی از روزنامه‌نگاری است که اولویت خود را بر پوشش برنامه‌های عمرانی، آموزشی و بهداشتی و بر هم‌سویی با اهداف ملی توسعه می‌گذارد و خبرنگار را به‌عنوان عامل مشارکت‌کننده در تغییر اجتماعی می‌شناسد.",
  "main_problem": "کشورهای تازه‌استقلال‌یافتهٔ جنوب در دههٔ ۱۹۶۰ با کمبود زیرساخت، سواد و سرمایه روبه‌رو بودند. پرسش این بود: رسانه باید در خدمت توسعهٔ ملی باشد یا نظارتی بی‌طرف بر قدرت؟ روزنامه‌نگاری توسعه پاسخ نخست را انتخاب کرد.",
  "mechanism": "\n".join([
   "(۱) رسانه به‌عنوان ابزار توسعه: اولویت خبر، برنامه‌های توسعه — کشاورزی، بهداشت، سوادآموزی — است و ارزش خبری با سنجهٔ سودمندی توسعه‌ای تعیین می‌شود.",
   "(۲) روزنامه‌نگار مشارکت‌کننده: خبرنگار به‌جای فاصلهٔ حرفه‌ای، خود را بخشی از پروژهٔ ملی می‌داند و در انتقال دانش و تغییر رفتار مشارکت می‌کند.",
   "(۳) پیوند با سیاست دولتی: بودجه، دسترسی به منابع و آموزش خبرنگار زیر چتر دولت قرار می‌گیرد؛ همین پیوند، هم قوت و هم ضعف اصلی الگوست.",
   "(۴) آموزش مخاطب: الگو بر «چه باید دانست» متمرکز است و مخاطب را یادگیرنده‌ای می‌بیند که باید به رفتار مطلوب هدایت شود.",
   "(۵) چالش اعتماد: وقتی رسانه بخشی از پروژهٔ رسمی است، فاصلهٔ لازم برای نقد و نظارت کمرنگ می‌شود و اعتماد مخاطب به استقلال خبر کاهش می‌یابد.",
   VOID + "در دهه‌های ۱۹۶۰ و ۱۹۷۰، روزنامه‌های کرهٔ جنوبی و تایلند، پوشش گسترش کشاورزی و برنامه‌های بهداشتی را در صدر صفحات خود گذاشتند؛ مراکز آموزش روزنامه‌نگاری توسعه در کشورهای تازه‌استقلال‌یافته، همین مدل را آموزش می‌دادند.",
  ]),
  "assumptions": [
   "توسعهٔ ملی، هدف مشترک و بی‌منازعهٔ جامعه است.",
   "رسانه می‌تواند رفتار و نگرش مخاطب را به‌طور مستقیم تغییر دهد.",
   "دولت نمایندهٔ منافع جمعی است و هم‌سویی با آن معادل خدمت عمومی است.",
  ],
  "principles": [
   "ارزش خبری با سودمندی توسعه‌ای سنجیده می‌شود، نه با معیارهای حرفه‌ای سنتی.",
   "روزنامه‌نگار در قبال پیشرفت جامعه مسئول است و باید مشارکت کند.",
   "آموزش مخاطب، کارکرد اصلی رسانهٔ توسعه‌محور است.",
  ],
  "critiques": [
   "ابزاری‌شدن رسانه: منتقدان این مدل را پوششی برای کنترل دولتی مطبوعات می‌دانند؛ زبانی که آزادی مطبوعات را به نام توسعه محدود می‌کند.",
   "ارتباط یک‌سویه: جریان پیام از دولت به توده بدون بازخورد، عاملیت مخاطب و صدای جوامع محلی را نادیده می‌گیرد.",
   "یکنواختی نسخهٔ توسعه: فرض یک الگوی واحد توسعه، تفاوت‌های فرهنگی و محلی را از تحلیل حذف می‌کند.",
   "بی‌توجهی به تضاد منافع: در جوامعی با شکاف‌های طبقاتی و قومی، «منافع ملی» اغلب منافع گروه حاکم است، نه همهٔ جامعه.",
  ],
  "applications": [
   "تحلیل سیاست رسانه‌ای در کشورهای در حال توسعه: نسبت آموزش رسانه‌ای با اولویت‌های دولتی.",
   "پژوهش ارتباطات سلامت و کشاورزی: ارزیابی کمپین‌های تغییر رفتار و سهم رسانه در آن.",
   "نقد روزنامه‌نگاری توسعهٔ معاصر: بازگشت این الگو در پروژه‌های «توسعهٔ پایدار» و «سواد دیجیتال» دولتی.",
   "مطالعهٔ استقلال حرفه‌ای: چگونه فشار توسعه‌ای، مرزهای استقلال خبرنگار را جابه‌جا می‌کند.",
  ],
  "evolution": "از بحث «نظم نوین اطلاعاتی جهان» و گزارش مک‌براید یونسکو (۱۹۸۰) به بازنگری انتقادی در دههٔ ۱۹۹۰، و امروز به بازخوانی آن در قالب رسانه‌های توسعهٔ پایدار، روزنامه‌نگاری شهروندی و ارتباطات بحران.",
  "key_concepts": ["روزنامه‌نگاری توسعه (Development Journalism)", "ارتباطات توسعه (Development Communication)", "روزنامه‌نگار مشارکت‌کننده (Participatory Journalist)", "ارزش خبری توسعه‌ای (Developmental News Value)", "نظم نوین اطلاعاتی (NWICO)", "تغییر اجتماعی هدایت‌شده (Guided Social Change)"],
  "studies": [
   "Xu, X. (2009). Development journalism. In K. Wahl-Jorgensen & T. Hanitzsch (Eds.), The handbook of journalism studies (pp. 357-369). Routledge.",
   "UNESCO. (1980). Many voices, one world: Communication and society today and tomorrow. UNESCO.",
  ],
  "detailed_analysis": "\n".join([
   "۱. بنیان و منطق نظری: روزنامه‌نگاری توسعه وارث نظریهٔ نوسازی است؛ همان‌گونه که نوسازی، جوامع جنوب را در مسیر خطی توسعه می‌دید، این الگو هم رسانه را موتور همان مسیر می‌دانست.",
   "۲. تنش با استقلال حرفه‌ای: تقابل اصلی این نظریه با روزنامه‌نگاری نظارتی (watchdog) است؛ در یک سو، مسئولیت در قبال جامعه، در سوی دیگر، استقلال از قدرت — و مسئلهٔ عملی، یافتن مرز میان این دو است.",
   "۳. بازخوانی امروز: با بازگشت پرسش‌های توسعهٔ پایدار، بهداشت عمومی و بحران اقلیمی، الگوی توسعه‌محور با پوششی تازه بازمی‌گردد؛ اما درس تجربهٔ گذشته روشن است: بدون استقلال و بازخورد، رسانهٔ توسعه‌محور به ابزار تبلیغ بدل می‌شود.",
  ]),
  "critique_text": "\n".join([
   "۱. ابزاری‌شدن رسانه: منتقدان این مدل را پوششی برای کنترل دولتی مطبوعات می‌دانند؛ زبانی که آزادی مطبوعات را به نام توسعه محدود می‌کند.",
   "۲. ارتباط یک‌سویه: جریان پیام از دولت به توده بدون بازخورد، عاملیت مخاطب و صدای جوامع محلی را نادیده می‌گیرد.",
   "۳. یکنواختی نسخهٔ توسعه: فرض یک الگوی واحد توسعه، تفاوت‌های فرهنگی و محلی را از تحلیل حذف می‌کند.",
   "۴. بی‌توجهی به تضاد منافع: در جوامعی با شکاف‌های طبقاتی و قومی، «منافع ملی» اغلب منافع گروه حاکم است، نه همهٔ جامعه.",
  ]),
  "example_text": "\n".join([
   "در دهه‌های ۱۹۶۰ و ۱۹۷۰، روزنامه‌های کرهٔ جنوبی و تایلند پوشش گسترش کشاورزی، برنامه‌های خانوادهٔ سالم و کمپین‌های سوادآموزی را در صدر صفحات خود گذاشتند؛ مراکز آموزش روزنامه‌نگاری توسعه در بسیاری از کشورهای تازه‌استقلال‌یافته، همین مدل را آموزش می‌دادند.",
   "در یک کمپین واکسیناسیون ملی، رسانه‌ها آگاه‌سازی عمومی و اطمینان‌بخشی را بر عهده می‌گیرند؛ اینکه این پوشش به آموزش بهداشت بدل شود یا به تبلیغ بی‌نقد سیاست، تفاوت بین روزنامه‌نگاری توسعه و تبلیغ رسمی است.",
   "در پوشش پروژهٔ بزرگ عمرانی، خبرنگار توسعه‌محور بر منافع عمومی پروژه تمرکز می‌کند؛ خبرنگار نظارتی می‌پرسد چه کسی منفعت می‌برد و چه صدایی حذف شده است — تفاوت دو الگو در یک نمونهٔ واحد.",
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
    print("BATCH68 THEORY DONE")

if __name__ == "__main__":
    main()
