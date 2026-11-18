# -*- coding: utf-8 -*-
"""Batch 36 (THEORY): MC-506 Media as Creative Industry (Hesmondhalgh 2013), MC-036 Economies of
Scale & Scope (Picard 2002), MC-129 Risk Communication (Kasperson et al. 1988), MC-144 Agenda-
Building (Cobb & Elder 1972). All primary anchors web-verified 2026-11-16. DB: resaname_kb_final_inspect."""
import pymysql, json

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch36-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch36_theory.json"

S = {
 "MC-506": [  # Media as Creative Industry
   dict(kind="BOOK", title_en="The Cultural Industries",
        title_fa="صنایع فرهنگی", authors="Hesmondhalgh, D.", year=2013,
        publisher="London: Sage (3rd ed.)", doi=None, url=None, language="en", isbn="9781446209264",
        citation="Hesmondhalgh, D. (2013). The cultural industries (3rd ed.). Sage.",
        locator="whole work", locator_type="work", supports="definition / characteristics / mechanism", verified=True),
   dict(kind="BOOK", title_en="Creative Industries: Contracts between Art and Commerce",
        title_fa="صنایع خلاق: قراردادهای میان هنر و تجارت", authors="Caves, R. E.", year=2000,
        publisher="Cambridge, MA: Harvard University Press", doi=None, url=None, language="en", isbn=None,
        citation="Caves, R. E. (2000). Creative industries: Contracts between art and commerce. Harvard University Press.",
        locator="whole work", locator_type="work", supports="economics of creative industries / 'nobody knows'", verified=False),
 ],
 "MC-036": [  # Economies of Scale & Scope
   dict(kind="BOOK", title_en="The Economics and Financing of Media Companies",
        title_fa="اقتصاد و تأمین مالی شرکت‌های رسانه‌ای", authors="Picard, R. G.", year=2002,
        publisher="New York: Fordham University Press", doi=None, url=None, language="en", isbn="0823221741",
        citation="Picard, R. G. (2002). The economics and financing of media companies. Fordham University Press.",
        locator="whole work", locator_type="work", supports="media cost structure / dual market / scale and scope", verified=True),
   dict(kind="BOOK", title_en="Entertainment Industry Economics: A Guide for Financial Analysis",
        title_fa="اقتصاد صنعت سرگرمی: راهنمای تحلیل مالی", authors="Vogel, H. L.", year=2014,
        publisher="Cambridge: Cambridge University Press (10th ed.)", doi=None, url=None, language="en", isbn=None,
        citation="Vogel, H. L. (2014). Entertainment industry economics: A guide for financial analysis (10th ed.). Cambridge University Press.",
        locator="whole work", locator_type="work", supports="evolution / first-copy costs", verified=False),
 ],
 "MC-129": [  # Risk Communication
   dict(kind="JOURNAL_ARTICLE", title_en="The Social Amplification of Risk: A Conceptual Framework",
        title_fa="تقویت اجتماعی ریسک: یک چارچوب مفهومی", authors="Kasperson, R. E., Renn, O., Slovic, P., Brown, H. S., Emel, J., Goble, R., Kasperson, J. X., & Ratick, S.", year=1988,
        publisher="Risk Analysis, 8(2), 177-187", doi="10.1111/j.1539-6924.1988.tb01168.x",
        url="https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1539-6924.1988.tb01168.x", language="en", isbn=None,
        citation="Kasperson, R. E., Renn, O., Slovic, P., Brown, H. S., Emel, J., Goble, R., Kasperson, J. X., & Ratick, S. (1988). The social amplification of risk: A conceptual framework. Risk Analysis, 8(2), 177-187. https://doi.org/10.1111/j.1539-6924.1988.tb01168.x",
        locator="pp. 177-187", locator_type="page_range", supports="definition / amplification stations / mechanism", verified=True),
   dict(kind="BOOK", title_en="The Perception of Risk",
        title_fa="ادراک ریسک", authors="Slovic, P.", year=2000,
        publisher="London: Earthscan", doi=None, url=None, language="en", isbn=None,
        citation="Slovic, P. (2000). The perception of risk. Earthscan.",
        locator="whole work", locator_type="work", supports="evolution / risk perception factors", verified=False),
 ],
 "MC-144": [  # Agenda-Building
   dict(kind="BOOK", title_en="Participation in American Politics: The Dynamics of Agenda-Building",
        title_fa="مشارکت در سیاست آمریکا: پویایی‌های ساخت دستور کار",
        authors="Cobb, R. W., & Elder, C. D.", year=1972,
        publisher="Boston: Allyn and Bacon", doi=None, url=None, language="en", isbn=None,
        citation="Cobb, R. W., & Elder, C. D. (1972). Participation in American politics: The dynamics of agenda-building. Allyn and Bacon.",
        locator="whole work", locator_type="work", supports="definition / agenda types / mechanism", verified=True),
   dict(kind="BOOK", title_en="Agenda-Setting",
        title_fa="دستور کارگذاری", authors="Dearing, J. W., & Rogers, E. M.", year=1996,
        publisher="Thousand Oaks, CA: Sage", doi=None, url=None, language="en", isbn=None,
        citation="Dearing, J. W., & Rogers, E. M. (1996). Agenda-setting. Sage.",
        locator="whole work", locator_type="work", supports="evolution / link to media agenda-setting", verified=False),
 ],
}

ENRICH = {
 "MC-506": {
   "summary": "«رسانه به‌عنوان صنعت خلاق» (Media as Creative Industry) چارچوبی است که رسانه‌ها را در زمرهٔ «صنایع فرهنگی/خلاق» تحلیل می‌کند؛ صنایعی که کالاهای نمادین (متون، صدا، تصویر) تولید و توزیع می‌کنند. دیوید هسموندالغ در کتاب «The Cultural Industries» (ویراست سوم، ۲۰۱۳، Sage) نشان می‌دهد این صنایع به‌دلیل ساختار هزینهٔ ویژه، عدم‌قطعیت تقاضا و هم‌آمیزی هنر و تجارت، منطق اقتصادی متمایزی دارند (Hesmondhalgh, 2013).",
   "main_problem": "رسانه‌ها به‌عنوان صنعت، چه ویژگی‌های ساختاری آن‌ها را از دیگر صنایع متمایز می‌کند، و چگونه می‌توان میان ارزش فرهنگی و منطق تجاری در تولید کالاهای نمادین توازن برقرار کرد؟",
   "mechanism": "چارچوب صنایع خلاق بر سازوکارهای ویژهٔ اقتصادی و سازمانی استوار است: (۱) «هزینهٔ بالا و ریسک تقاضا» — تولید محصول نخست پرهزینه است و تقاضا برای متون نمادین به‌سختی پیش‌بینی می‌شود («هیچ‌کس نمی‌داند» — Caves, 2000)؛ (۲) «هزینهٔ تکثیر پایین» — نسخه‌های بعدی با هزینهٔ ناچیز تکثیر می‌شوند، بنابراین صرفه‌های مقیاس و دامنه تعیین‌کننده‌اند؛ (۳) «هم‌آمیزی هنر و تجارت» — آفرینش خلاق و مدیریت اقتصادی در یک سازمان جمع می‌شوند و کشمکش دائمی میان آزادی خلاق و الزام سودآوری ایجاد می‌کنند؛ (۴) «مدیریت ریسک از طریق تکرار و ستاره‌سازی» — صنایع فرهنگی با تولید مجموعه‌ها، فرمول‌های آشنا و برندسازی، عدم‌قطعیت را مهار می‌کنند (Hesmondhalgh, 2013). نتیجهٔ این سازوکارها، تمرکز مالکیت و همگن‌سازی نسبی محتوا در کنار دوره‌های نوآوری است.",
   "assumptions": [
     "رسانه‌ها کالاهای نمادین تولید می‌کنند که ارزش فرهنگی و اقتصادی هم‌زمان دارند.",
     "عدم‌قطعیت تقاضا در صنایع فرهنگی ساختاری است و مدیریت آن به سازوکارهای ویژه نیاز دارد.",
     "ساختار هزینهٔ ثابت بالا و تکثیر ارزان، به تمرکز و صرفه‌جویی مقیاس می‌انجامد."
   ],
   "principles": [
     "کالای نمادین: ارزش محصول رسانه‌ای هم از معنا و هم از بازار مشتق می‌شود.",
     "مدیریت ریسک خلاق: تکرار، برند و ستاره‌سازی ابزارهای کنترل عدم‌قطعیت‌اند.",
     "تنش هنر و تجارت: خلاقیت و سودآوری در سازمان رسانه‌ای در تعارض دائمی‌اند."
   ],
   "critiques": [
     "ابهام مقوله: مرز «صنایع خلاق» با صنایع فرهنگی و رسانه‌ای مبهم است و دامنهٔ شمول آن بسته به تعریف سیاست‌گذار تغییر می‌کند.",
     "سیاست‌محوری: چارچوب صنایع خلاق ممکن است ارزش اقتصادی را بر ارزش عمومی و دموکراتیک رسانه مقدم بدارد.",
     "کم‌توجهی به نیروی کار: برخی نقدها می‌گویند نظریهٔ صنایع فرهنگی، به‌رغم توجه به کار خلاق، نابرابری و پیشکاربودن نیروی کار را کم‌رنگ می‌کند."
   ],
   "applications": [
     "تحلیل سیاست‌های فرهنگی و اقتصاد خلاق و سنجش سهم رسانه در تولید ناخالص داخلی.",
     "مطالعهٔ سازمان‌های رسانه‌ای، مدیریت خلاقیت و استراتژی تولید محتوا.",
     "پژوهش دربارهٔ پیشکاربودن کار خلاق و رابطهٔ پلتفرم‌ها با صنایع فرهنگی."
   ],
   "evolution": "مفهوم «صنعت فرهنگ» در مکتب فرانکفورت (آدورنو و هورکهایمر) به‌عنوان نقد استانداردسازی فرهنگی مطرح شد و از دههٔ ۱۹۹۰ در سیاست‌های «صنایع خلاق» بریتانیا به مقوله‌ای سیاست‌گذارانه و اقتصادی تبدیل شد. هسموندالغ (2013) با تفکیک «صنایع فرهنگی» از روایت خوش‌بینانهٔ «اقتصاد خلاق»، نقد ساختاری را حفظ کرد و در ویراست‌های بعدی، پلتفرم‌ها و کار دیجیتال را به تحلیل افزود.",
   "key_concepts": ["صنایع فرهنگی (cultural industries)", "صنایع خلاق (creative industries)", "کالای نمادین (symbolic good)", "عدم‌قطعیت تقاضا (demand uncertainty)", "صرفه‌های مقیاس (economies of scale)"],
   "studies": ["Hesmondhalgh, D. (2013). The Cultural Industries (3rd ed.). Sage.", "Caves, R. E. (2000). Creative Industries. Harvard University Press."],
 },
 "MC-036": {
   "summary": "«صرفه‌های مقیاس و دامنه و ساختار هزینهٔ کالای رسانه‌ای» (Economies of Scale & Scope; Media Cost Structure) چارچوبی است در اقتصاد رسانه که نشان می‌دهد کالاهای رسانه‌ای ساختار هزینه‌ای ویژه‌ای دارند: هزینهٔ تولید نخستین نسخه بالاست، اما هزینهٔ تکثیر هر نسخهٔ بعدی بسیار پایین است. رابرت جی. پیکارد در «The Economics and Financing of Media Companies» (۲۰۰۲، Fordham University Press) این ویژگی‌ها را به ساختار بازار، درآمد و تأمین مالی رسانه پیوند می‌دهد (Picard, 2002).",
   "main_problem": "ساختار هزینهٔ ویژهٔ کالای رسانه‌ای چگونه رفتار شرکت‌ها، ساختار بازار و راهبردهای رشد را تعیین می‌کند، و چرا این ساختار به تمرکز، تنوع محصول و بازارهای دوجانبه می‌انجامد؟",
   "mechanism": "این چارچوب چند مکانیسم اقتصادی را به هم می‌پیوندد: (۱) «هزینهٔ نسخهٔ نخست» (first-copy cost) — نوشتن، تولید و ویرایش یک بار رخ می‌دهد و بخش عمدهٔ هزینه است؛ (۲) «هزینهٔ نهایی نزدیک به صفر» (near-zero marginal cost) — چاپ یا پخش نسخه‌های بعدی هزینهٔ ناچیزی دارد، پس «صرفه‌های مقیاس» (economies of scale) تولید هرچه بیشتر را ارزان‌تر می‌کند؛ (۳) «صرفه‌های دامنه» (economies of scope) — محتوای تولیدشده را می‌توان در چند رسانه و بازار بازاستفاده کرد و هزینهٔ مشترک را بر چند محصول توزیع نمود؛ (۴) «کالای عمومی و بازار دوجانبه» — محتوا خصلت کالای عمومی دارد (مصرف یک نفر، مصرف دیگران را کاهش نمی‌دهد) و رسانه معمولاً در دو بازار هم‌زمان فعالیت می‌کند: بازار مخاطب و بازار آگهی (Picard, 2002). پیامد ترکیبی این سازوکارها، گرایش ساختاری به تمرکز، ادغام و ورود دشوار رقبای کوچک است.",
   "assumptions": [
     "هزینهٔ تولید نخستین نسخهٔ کالای رسانه‌ای در مقایسه با هزینهٔ تکثیر آن بسیار بالاست.",
     "محتوای رسانه‌ای خصلت کالای عمومی دارد و مصرف آن رقیب‌پذیر نیست.",
     "شرکت‌های رسانه‌ای هم‌زمان در بازار مخاطب و بازار آگهی فعالیت می‌کنند."
   ],
   "principles": [
     "صرفه‌های مقیاس: با افزایش تولید، هزینهٔ متوسط کاهش می‌یابد و شرکت بزرگ‌تر مزیت هزینه‌ای می‌گیرد.",
     "صرفه‌های دامنه: بازاستفادهٔ محتوا در چند پلتفرم، هزینهٔ مشترک را کارآمدتر می‌کند.",
     "بازار دوجانبه: درآمد رسانه از فروش محتوا و فروش دسترسی به مخاطب به آگهی‌دهندگان تأمین می‌شود."
   ],
   "critiques": [
     "تحول دیجیتال: پلتفرم‌ها هزینهٔ تکثیر را به صفر نزدیک کرده‌اند و ساختار هزینهٔ سنتی را دگرگون ساخته‌اند؛ برخی تحلیل‌ها را باید بازبینی کرد.",
     "کاهش به اقتصاد: تحلیل هزینه ممکن است عوامل سیاسی، فرهنگی و نهادی مؤثر بر بازار رسانه را نادیده بگیرد.",
     "ابهام تجربی: سنجش دقیق صرفه‌های دامنه در شرکت‌های چندرسانه‌ای به‌دلیل نبود داده‌های تفکیکی دشوار است."
   ],
   "applications": [
     "تحلیل ساختار بازار رسانه، ادغام‌ها و راهبردهای چندرسانه‌ای.",
     "طراحی مدل درآمدی و تأمین مالی شرکت‌های رسانه‌ای و استارتاپ‌های محتوایی.",
     "سیاست‌گذاری رقابت و ارزیابی پیامدهای تمرکز بر تنوع محتوا."
   ],
   "evolution": "این چارچوب از اقتصاد رسانهٔ کلاسیک (پیکارد، 2002) و تحلیل صنعت سرگرمی (ووگل) سرچشمه می‌گیرد و در دههٔ ۲۰۱۰ با اقتصاد پلتفرم و بحث «هزینهٔ نهایی صفر» بازخوانی شد. امروزه در تحلیل مدل‌های اشتراکی، تبلیغاتی و ترکیبی و در سیاست‌گذاری رسانه به‌کار می‌رود.",
   "key_concepts": ["هزینهٔ نسخهٔ نخست (first-copy cost)", "صرفه‌های مقیاس (economies of scale)", "صرفه‌های دامنه (economies of scope)", "بازار دوجانبه (two-sided market)", "کالای عمومی (public good)"],
   "studies": ["Picard, R. G. (2002). The Economics and Financing of Media Companies. Fordham University Press.", "Vogel, H. L. (2014). Entertainment Industry Economics (10th ed.). Cambridge University Press."],
 },
 "MC-129": {
   "summary": "«ارتباطات ریسک» (Risk Communication) حوزه‌ای میان‌رشته‌ای است که به تبادل اطلاعات و معنا دربارهٔ خطرها میان متخصصان، سیاست‌گذاران، رسانه‌ها و عموم می‌پردازد. چارچوب «تقویت اجتماعی ریسک» (SARF) اثر کسپرسون و همکاران (۱۹۸۸، Risk Analysis) نشان داد که خطرهای فنی از فیلترهای روانی، اجتماعی، نهادی و فرهنگی می‌گذرند و ممکن است در ادراک عمومی «تقویت» یا «تضعیف» شوند (Kasperson et al., 1988).",
   "main_problem": "چرا ادراک عمومی از ریسک با ارزیابی فنی آن فاصله می‌گیرد، و ارتباطات رسانه‌ای و نهادی چگونه ریسک را تقویت یا تضعیف می‌کند و اعتماد عمومی را می‌سازد یا فرسایش می‌دهد؟",
   "mechanism": "چارچوب SARF مکانیسم را در قالب زنجیرهٔ انتقال معنا توضیح می‌دهد: (۱) رویداد خطر با «ایستگاه‌های تقویت» (amplification stations) — دانشمندان، رسانه‌ها، دولت، گروه‌های فشار و شبکه‌های اجتماعی — مواجه می‌شود؛ (۲) هر ایستگاه با رمزگذاری، تفسیر و بازنمایی، اطلاعات را پردازش می‌کند و شدت آن را تغییر می‌دهد؛ (۳) پیام‌های تقویت‌شده به «اثرات موجی» (ripple effects) می‌انجامند: نگرانی فراتر از گروه متأثر گسترش می‌یابد، اعتماد به نهادها کاهش می‌یابد و حتی صنایع و مناطق غیرمرتبط آسیب می‌بینند؛ (۴) این فرایند می‌تواند «داغ‌نگاری» (stigma) و پیامدهای اقتصادی و سیاسی پایدار ایجاد کند (Kasperson et al., 1988). ارتباطات مؤثر ریسک، به‌جای انتقال یک‌سویهٔ دادهٔ فنی، بر گفت‌وگو، شفافیت و اعتمادسازی استوار است.",
   "assumptions": [
     "ادراک ریسک صرفاً تابع داده‌های فنی نیست و عوامل روانی و فرهنگی در آن نقش دارند.",
     "رسانه‌ها و نهادها به‌عنوان «ایستگاه تقویت» در بازنمایی و شدت‌بخشی به ریسک اثرگذارند.",
     "اعتماد عمومی، شرط پیشین پذیرش پیام‌های ریسک و مدیریت بحران است."
   ],
   "principles": [
     "گفت‌وگومحوری: ارتباط ریسک فرایندی تعاملی است، نه انتقال یک‌سویهٔ اطلاعات.",
     "اعتماد و اعتبار: پیام از منبع مورد اعتماد بیشتر پذیرفته می‌شود.",
     "زمینه‌مندی: ادراک ریسک به تجربه، ارزش‌ها و بافت اجتماعی مخاطب وابسته است."
   ],
   "critiques": [
     "الگوی کمبود (deficit model): بسیاری از برنامه‌های ارتباط ریسک هنوز مخاطب را «ناآگاه» و متخصص را «آگاه» فرض می‌کنند و از گفت‌وگوی واقعی فاصله دارند.",
     "ابهام سنجش تقویت: تشخیص اینکه یک پیام، ریسک را تقویت یا تضعیف کرده، به‌سختی قابل اندازه‌گیری است.",
     "تمرکز بر رسانهٔ سنتی: چارچوب ۱۹۸۸ پیش از شبکه‌های اجتماعی نوشته شده و پویایی اشتراک‌گذاری و اطلاعات نادرست در محیط دیجیتال را کمتر پوشش می‌دهد."
   ],
   "applications": [
     "مدیریت ارتباطات بحران‌های سلامت، محیط‌زیست و فناوری (مانند پاندمی، آلودگی و انرژی هسته‌ای).",
     "طراحی کمپین‌های آگاهی عمومی و ارتباطات خطر در سیاست‌گذاری سلامت.",
     "تحلیل پوشش خبری خطرها و اطلاعات نادرست در شبکه‌های اجتماعی."
   ],
   "evolution": "از چارچوب SARF (کسپرسون و همکاران، 1988) و نقد «الگوی کمبود» در دههٔ ۱۹۹۰، تا رویکرد مشارکتی و داد‌محور (خطر و عدالت) و در دههٔ ۲۰۱۰ پیوند با ارتباطات بحران، اطلاعات نادرست و حکمرانی ریسک. اسلوویک (2000) با تحلیل عوامل ادراک ریسک، پشتوانهٔ روان‌شناختی این حوزه را تقویت کرد.",
   "key_concepts": ["ارتباطات ریسک (risk communication)", "تقویت اجتماعی ریسک (social amplification of risk)", "ایستگاه تقویت (amplification station)", "اثر موجی (ripple effect)", "ادراک ریسک (risk perception)"],
   "studies": ["Kasperson, R. E., et al. (1988). The Social Amplification of Risk. Risk Analysis, 8(2), 177-187.", "Slovic, P. (2000). The Perception of Risk. Earthscan."],
 },
 "MC-144": {
   "summary": "«نظریهٔ ساخت دستور کار» (Agenda-Building Theory) اثر راجر کاب و چارلز الدر در کتاب «Participation in American Politics» (۱۹۷۲، Allyn and Bacon) فرایندی را تبیین می‌کند که طی آن مطالبات گروه‌های اجتماعی به موضوعاتی تبدیل می‌شوند که نهادهای تصمیم‌گیر به آن‌ها توجه می‌کنند. کاب و الدر میان «دستور کار نظام‌مند» (systemic agenda) و «دستور کار نهادی» (institutional agenda) تمایز گذاشتند (Cobb & Elder, 1972).",
   "main_problem": "چگونه مسئله‌ها از فضای عمومی به دستور کار نهادهای تصمیم‌گیر وارد می‌شوند، چه بازیگرانی در این انتقال نقش دارند، و چه عواملی تعیین می‌کند کدام مسئله به مرحلهٔ تصمیم برسد و کدام کنار گذاشته شود؟",
   "mechanism": "کاب و الدر فرایند را در قالب مراحل و مرزهای متوالی توضیح می‌دهند: (۱) «دستور کار نظام‌مند» مجموعهٔ موضوعاتی است که در جامعه به‌عنوان مسئله مطرح‌اند و توجه عمومی را جلب می‌کنند؛ (۲) «دستور کار نهادی» مجموعهٔ موضوعاتی است که نهادهای رسمی برای بررسی و تصمیم‌گیری برمی‌گزینند؛ (۳) گذار از اولی به دومی از طریق «گسترش موضوع» (issue expansion) رخ می‌دهد: گروه‌ها با نمادسازی، رسانه‌ای کردن و ائتلاف‌سازی، دامنهٔ توجه به مسئله را گسترش می‌دهند تا نهادها را به واکنش وادارند؛ (۴) در مقابل، بازیگران مسلط می‌کوشند «دامنهٔ موضوع» را محدود نگه دارند («مهار موضوع» — issue containment) تا از ورود آن به دستور کار تصمیم جلوگیری کنند (Cobb & Elder, 1972). رسانه‌ها در این فرایند نقش میانجی و تشدیدکنندهٔ توجه را بازی می‌کنند.",
   "assumptions": [
     "دستور کار عمومی و نهادی دو عرصهٔ متمایز اما مرتبط‌اند.",
     "گسترش یا مهار دامنهٔ موضوع، متغیر کلیدی ورود مسئله به مرحلهٔ تصمیم است.",
     "بازیگران سازمان‌یافته و نمادها در جلب توجه نهادها نقش تعیین‌کننده دارند."
   ],
   "principles": [
     "تفکیک دستور کار نظام‌مند و نهادی: توجه عمومی با اولویت نهادی یکی نیست.",
     "گسترش موضوع: مسئله با افزایش دامنهٔ توجه، شانس ورود به دستور کار تصمیم را می‌یابد.",
     "مهار موضوع: بازیگران مسلط برای حفظ وضع موجود، دامنهٔ مسئله را محدود می‌کنند."
   ],
   "critiques": [
     "پیچیدگی و ابهام مراحل: تفکیک مراحل دستور کار در عمل مبهم است و مرز میان گسترش و مهار موضوع همیشه روشن نیست.",
     "تمرکز بر نخبگان: نظریه ممکن است نقش بازیگران نخبه و سازمان‌یافته را بر جنبش‌های مردمی و عاملیت شهروندان مقدم بدارد.",
     "بافت رسانه‌ای نو: پویایی دستور کار در محیط پلتفرمی و الگوریتمی با مدل ۱۹۷۲ به‌طور کامل توضیح داده نمی‌شود."
   ],
   "applications": [
     "تحلیل چگونگی ورود مسائل عمومی (محیط‌زیست، سلامت، فساد) به دستور کار دولت و مجلس.",
     "مطالعهٔ نقش رسانه‌ها و گروه‌های فشار در شکل‌گیری اولویت‌های سیاسی.",
     "پژوهش دربارهٔ دستور کارگذاری دیجیتال و نقش شبکه‌های اجتماعی در برجسته‌سازی مسائل."
   ],
   "evolution": "کاب و الدر (1972) نظریه را در چارچوب سیاست آمریکا صورت‌بندی کردند و در ادامه، پژوهش دستور کارگذاری رسانه‌ای (مک‌کامبز و شاو) و «ساخت دستور کار» رسانه‌ای به آن پیوند خورد. دیرینگ و راجرز (1996) آن را در چارچوب مطالعهٔ دستورکارگذاری نظام‌مند کردند و در عصر دیجیتال، بحث «دستور کار الگوریتمی» و نقش پلتفرم‌ها به آن افزوده شد.",
   "key_concepts": ["ساخت دستور کار (agenda-building)", "دستور کار نظام‌مند (systemic agenda)", "دستور کار نهادی (institutional agenda)", "گسترش موضوع (issue expansion)", "مهار موضوع (issue containment)"],
   "studies": ["Cobb, R. W., & Elder, C. D. (1972). Participation in American Politics. Allyn and Bacon.", "Dearing, J. W., & Rogers, E. M. (1996). Agenda-Setting. Sage."],
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
    codes = ["MC-506", "MC-036", "MC-129", "MC-144"]
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
    print("BATCH36 THEORY DONE")

if __name__ == "__main__":
    main()
