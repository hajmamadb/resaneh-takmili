# -*- coding: utf-8 -*-
"""Batch 53 (THEORY): MC-220 Narrative Policy Framework (Jones & McBeth 2010), MC-224
Technological Solutionism (Morozov 2013), MC-226 Visibility Labour (Abidin 2016), MC-227
Computational Propaganda (Woolley & Howard 2018). Anchors verified 2026-11-16."""
import pymysql, json

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch53-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch53_theory.json"

S = {
 "MC-220": [
   dict(kind="JOURNAL_ARTICLE", title_en="A Narrative Policy Framework: Clear Enough to Be Wrong?",
        title_fa="چارچوب روایت سیاستی: به‌قدر کافی روشن تا بتواند اشتباه باشد؟",
        authors="Jones, M. D., & McBeth, M. K.", year=2010,
        publisher="Policy Studies Journal, 38(2), 329-353", doi="10.1111/j.1541-0072.2010.00364.x",
        url="https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1541-0072.2010.00364.x",
        language="en", isbn=None,
        citation="Jones, M. D., & McBeth, M. K. (2010). A narrative policy framework: Clear enough to be wrong? Policy Studies Journal, 38(2), 329-353.",
        locator="pp. 329-353", locator_type="page_range", supports="definition / three-level structure", verified=True),
   dict(kind="JOURNAL_ARTICLE", title_en="How to Conduct a Narrative Policy Framework Study",
        title_fa="چگونه یک پژوهش چارچوب روایت سیاستی انجام دهیم",
        authors="Shanahan, E. A., Jones, M. D., & McBeth, M. K.", year=2018,
        publisher="The Social Science Journal, 55(3), 332-345", doi=None, url=None, language="en", isbn=None,
        citation="Shanahan, E. A., Jones, M. D., & McBeth, M. K. (2018). How to conduct a narrative policy framework study. The Social Science Journal, 55(3), 332-345.",
        locator="pp. 332-345", locator_type="page_range", supports="evolution / methodological guidance", verified=False),
 ],
 "MC-224": [
   dict(kind="BOOK", title_en="To Save Everything, Click Here: The Folly of Technological Solutionism",
        title_fa="برای نجات همه‌چیز، اینجا کلیک کنید: حماقت راه‌حل‌گرایی فناورانه",
        authors="Morozov, E.", year=2013, publisher="New York: PublicAffairs", doi=None,
        url="https://archive.org/details/tosaveeverything0000moro", language="en", isbn="9781610391382",
        citation="Morozov, E. (2013). To save everything, click here: The folly of technological solutionism. PublicAffairs.",
        locator="whole work", locator_type="work", supports="definition / solutionism critique", verified=True),
   dict(kind="BOOK", title_en="The Net Delusion: The Dark Side of Internet Freedom",
        title_fa="توهم شبکه: روی تاریک آزادی اینترنت", authors="Morozov, E.", year=2011,
        publisher="New York: PublicAffairs", doi=None, url=None, language="en", isbn=None,
        citation="Morozov, E. (2011). The net delusion: The dark side of internet freedom. PublicAffairs.",
        locator="whole work", locator_type="work", supports="evolution / internet-centrism", verified=False),
 ],
 "MC-226": [
   dict(kind="JOURNAL_ARTICLE", title_en="Visibility Labour: Engaging with Influencers' Fashion Brands and #OOTD Advertorial Campaigns on Instagram",
        title_fa="کار قابل‌رؤیت: تعامل با برندهای مد اینفلوئنسرها و کمپین‌های تبلیغی #OOTD در اینستاگرام",
        authors="Abidin, C.", year=2016,
        publisher="Media International Australia, 161(1), 86-100", doi="10.1177/1329878X16665177",
        url="https://journals.sagepub.com/doi/abs/10.1177/1329878x16665177",
        language="en", isbn=None,
        citation="Abidin, C. (2016). Visibility labour: Engaging with influencers' fashion brands and #OOTD advertorial campaigns on Instagram. Media International Australia, 161(1), 86-100.",
        locator="pp. 86-100", locator_type="page_range", supports="definition / influencer visibility work", verified=True),
   dict(kind="BOOK", title_en="(Not) Getting Paid to Do What You Love: Gender, Social Media, and Aspirational Work",
        title_fa="(نه) پول گرفتن برای کاری که دوست داری: جنسیت، رسانه‌های اجتماعی و کار آرمانی",
        authors="Duffy, B. E.", year=2017, publisher="New Haven, CT: Yale University Press", doi=None, url=None,
        language="en", isbn=None,
        citation="Duffy, B. E. (2017). (Not) getting paid to do what you love: Gender, social media, and aspirational work. Yale University Press.",
        locator="whole work", locator_type="work", supports="evolution / aspirational labour", verified=False),
 ],
 "MC-227": [
   dict(kind="BOOK", title_en="Computational Propaganda: Political Parties, Politicians, and Political Manipulation on Social Media",
        title_fa="پروپاگاندای محاسباتی: احزاب سیاسی، سیاستمداران و دستکاری سیاسی در رسانه‌های اجتماعی",
        authors="Woolley, S. C., & Howard, P. N. (Eds.)", year=2018,
        publisher="New York: Oxford University Press", doi=None,
        url="https://academic.oup.com/book/25859", language="en", isbn="9780190664407",
        citation="Woolley, S. C., & Howard, P. N. (Eds.). (2018). Computational propaganda: Political parties, politicians, and political manipulation on social media. Oxford University Press.",
        locator="whole work", locator_type="work", supports="definition / automation typology", verified=True),
   dict(kind="REPORT", title_en="The Global Disinformation Order: 2019 Global Inventory of Organised Social Media Manipulation",
        title_fa="نظم جهانی اطلاعات نادرست: سیاههٔ جهانی ۲۰۱۹ دستکاری سازمان‌یافتهٔ رسانه‌های اجتماعی",
        authors="Bradshaw, S., & Howard, P. N.", year=2019,
        publisher="Oxford: Oxford Internet Institute", doi=None, url=None, language="en", isbn=None,
        citation="Bradshaw, S., & Howard, P. N. (2019). The global disinformation order: 2019 global inventory of organised social media manipulation. Oxford Internet Institute.",
        locator="whole work", locator_type="work", supports="evolution / global prevalence", verified=False),
 ],
}

ENRICH = {
 "MC-220": {
   "summary": "«چارچوب روایت سیاستی» (Narrative Policy Framework, NPF) چارچوبی است که روایت‌ها را به‌عنوان مؤلفه‌ای ساختاری و قابل‌سنجش در فرایند سیاست‌گذاری تحلیل می‌کند و می‌کوشد مطالعهٔ روایت را از تفسیر کیفی به آزمون تجربی‌پذیر ببرد. مایکل جونز و مارک مک‌بث در مقالهٔ «A Narrative Policy Framework» (۲۰۱۰، Policy Studies Journal) این چارچوب را با پرسش «به‌قدر کافی روشن تا بتواند اشتباه باشد؟» معرفی کردند (Jones & McBeth, 2010).",
   "main_problem": "چگونه می‌توان نقش روایت‌ها را در شکل‌گیری، تثبیت و تغییر سیاست‌های عمومی به‌گونه‌ای نظام‌مند و تجربی سنجید، بدون فروکاستن به تفسیر کیفی یا ادعاهای اثبات‌ناپذیر دربارهٔ قدرت روایت؟",
   "mechanism": "NPF روایت را از چهار عنصر ساختاری می‌سازد: «صحنه/زمینه» (setting)، «شخصیت‌ها» (characters) شامل قهرمان، شرور و قربانی، «طرح/پی‌رنگ» (plot) و «درس اخلاقی/راه‌حل» (moral). تحلیل در سه سطح انجام می‌شود: سطح «خرد» (micro) که باورها و پردازش شناختی فرد را می‌سنجد، سطح «میانی» (meso) که گروه‌ها و ائتلاف‌های سیاستی و راهبردهای روایی‌شان را بررسی می‌کند، و سطح «کلان» (macro) که روایت‌های نهادی و فرهنگی گسترده را در بر می‌گیرد (Jones & McBeth, 2010). گروه‌های سیاستی دو راهبرد روایی اصلی دارند: «گسترش دامنهٔ تعارض» (scope of conflict expansion) برای جلب حمایت عمومی و «مهار دامنهٔ تعارض» (containment) برای محدود نگه‌داشتن آن. شاناهان و همکاران (Shanahan et al., 2018) راهنمای روش‌شناختی برای اجرای NPF ارائه کردند. در بستر رسانه، NPF نشان می‌دهد چگونه خبر و گزارش، حامل روایت‌های سیاستی‌اند: انتخاب قهرمان و شرور، تعیین قربانی و طرح راه‌حل، چارچوب درک عمومی از مسئله و امکان‌های سیاستی را شکل می‌دهد و ائتلاف‌ها با مدیریت روایت می‌کوشند توجه عمومی و دستورکار سیاست‌گذاری را به نفع خود بگردانند.",
   "assumptions": [
     "روایت ساختار مشخص و قابل‌سنجشی دارد.",
     "روایت‌ها در سه سطح خرد، میانی و کلان عمل می‌کنند.",
     "گروه‌های سیاستی آگاهانه روایت را برای گسترش یا مهار تعارض به‌کار می‌گیرند."
   ],
   "principles": [
     "چهار عنصر: صحنه، شخصیت، طرح و درس اخلاقی.",
     "سه سطح تحلیل: خرد، میانی و کلان.",
     "راهبرد روایی: گسترش یا مهار دامنهٔ تعارض."
   ],
   "critiques": [
     "صورت‌گرایی ساختاری: تأکید بر عناصر ساختاری ممکن است معنا و بافت روایت را کم‌رنگ کند.",
     "چالش علیت: اثبات رابطهٔ علّی میان روایت و نتیجهٔ سیاست دشوار است.",
     "عملیاتی‌سازی: سنجش عناصر روایی در متون پیچیده، نیازمند کدگذاری دقیق و هزینه‌بر است."
   ],
   "applications": [
     "تحلیل روایت‌های خبری در منازعات سیاستی مانند محیط زیست و سلامت.",
     "پژوهش دربارهٔ راهبرد روایی ائتلاف‌های سیاستی.",
     "طراحی پیام سیاستی و ارزیابی چارچوب‌بندی رسانه‌ای."
   ],
   "evolution": "جونز و مک‌بث (2010) چارچوب را معرفی کردند و شاناهان و همکاران (2018) راهنمای روش‌شناختی ارائه دادند. در دههٔ ۲۰۱۰-۲۰۲۰، NPF در پژوهش‌های سیاستی و ارتباطات دربارهٔ اقلیم، سلامت و رسانه به‌کار رفت.",
   "key_concepts": ["چارچوب روایت سیاستی (narrative policy framework)", "شخصیت روایی (narrative character)", "دامنهٔ تعارض (scope of conflict)", "سطح میانی (meso level)", "روایت سیاستی (policy narrative)"],
   "studies": ["Jones, M. D., & McBeth, M. K. (2010). A Narrative Policy Framework. PSJ, 38(2), 329-353.", "Shanahan, E. A., Jones, M. D., & McBeth, M. K. (2018). How to conduct a NPF study. The Social Science Journal, 55(3), 332-345."],
 },
 "MC-224": {
   "summary": "«راه‌حل‌گرایی فناورانه» (Technological Solutionism) به گرایش به بازتعریف مسائل پیچیدهٔ اجتماعی به‌صورت مسائل روشن و محاسبه‌پذیر و ارائهٔ راه‌حل فنی برای آن‌ها اشاره دارد. یوگنی موروزوف در «To Save Everything, Click Here» (۲۰۱۳، PublicAffairs) این گرایش را به‌عنوان ایدئولوژی سیلیکون‌ولی نقد کرد (Morozov, 2013).",
   "main_problem": "چرا راه‌حل‌های فناورانه اغلب مسئله را به‌جای حل، از نو تعریف می‌کنند، و چگونه این «راه‌حل‌گرایی» بحث سیاسی و عمومی را کنار می‌گذارد؟",
   "mechanism": "موروزوف نشان می‌دهد که راه‌حل‌گرایی از سه سازوکار عمل می‌کند: نخست، «تعریف مسئله بر پایهٔ قابلیت اندازه‌گیری» — مسائل اجتماعی به آنچه الگوریتم می‌تواند محاسبه کند فروکاسته می‌شوند و بخش‌های مبهم و ارزشی نادیده می‌مانند؛ دوم، «جایگزینی سیاست با بهینه‌سازی» — تصمیم‌های عمومی به مسئلهٔ فنی کارایی بدل می‌شوند و بحث دربارهٔ ارزش‌ها و اهداف به حاشیه می‌رود؛ سوم، «ایدئولوژی بی‌اصطکاک» (frictionless) — فرض می‌شود بهترین زندگی، روان‌ترین و بی‌مانع‌ترین آن است، در حالی که اصطکاک و ابهام بخشی از زندگی سیاسی‌اند (Morozov, 2013). موروزوف همچنین «اینترنت‌مرکزیت» (internet-centrism) را نقد می‌کند — یعنی نگاه به اینترنت همچون نیرویی یگانه و رهایی‌بخش — که پیش‌تر در «The Net Delusion» (Morozov, 2011) طرح کرده بود. در بستر رسانه، راه‌حل‌گرایی فناورانه در گفتمان نوآوری رسانه‌ای دیده می‌شود: ارائهٔ «راه‌حل» الگوریتمی برای بحران اعتماد خبری، «بهینه‌سازی» تعامل مخاطب یا «خودکارسازی» تحریریه، هر یک می‌تواند مسئلهٔ معرفتی و سیاسی را به مسئلهٔ فنی فرو بکاهد. نقد موروزوف مهم است زیرا نشان می‌دهد نوآوری فناورانه، به‌خودی‌خود، جایگزین بازاندیشی دربارهٔ ارزش‌ها و منافع عمومی نیست.",
   "assumptions": [
     "مسائل اجتماعی پیچیده و ارزش‌محورند و به‌سادگی محاسبه‌پذیر نیستند.",
     "راه‌حل فنی اغلب مسئله را از نو تعریف می‌کند.",
     "ایدئولوژی سیلیکون‌ولی خنثی نیست و اهداف خود را تحمیل می‌کند."
   ],
   "principles": [
     "تعریف مسئله بر پایهٔ اندازه‌پذیری: آنچه سنجیدنی است، مسئله می‌شود.",
     "جایگزینی سیاست با بهینه‌سازی: ارزش‌ها به کارایی فروکاسته می‌شوند.",
     "نقد اینترنت‌مرکزیت: فناوری نیرویی یگانه و رهایی‌بخش نیست."
   ],
   "critiques": [
     "قلدری جدلی: لحن تند و تعمیم‌های گسترده، قدرت تحلیلی نقد را کاهش می‌دهد.",
     "نادیده‌گرفتن منافع فناوری: نقد ممکن است دستاوردهای واقعی فناوری را کم‌رنگ کند.",
     "ابهام جایگزین: چارچوب کمتر راه‌حل جایگزین برای مسائل مطرح‌شده ارائه می‌دهد."
   ],
   "applications": [
     "نقد گفتمان نوآوری و راه‌حل‌های الگوریتمی برای بحران خبر.",
     "پژوهش دربارهٔ ایدئولوژی پلتفرم‌ها و حکمرانی محتوا.",
     "تحلیل پیامدهای «بهینه‌سازی» تعامل مخاطب در رسانه."
   ],
   "evolution": "موروزوف (2011) نقد اینترنت‌مرکزیت را آغاز کرد و (2013) راه‌حل‌گرایی فناورانه را صورت‌بندی کرد. در دههٔ ۲۰۱۰-۲۰۲۰، مطالعات انتقادی پلتفرم و هوش مصنوعی، منطق راه‌حل‌گرایی را به حکمرانی الگوریتمی و رسانهٔ خودکار گسترد.",
   "key_concepts": ["راه‌حل‌گرایی فناورانه (technological solutionism)", "اینترنت‌مرکزیت (internet-centrism)", "بی‌اصطکاک‌گرایی (frictionless)", "بهینه‌سازی (optimization)", "ایدئولوژی سیلیکون‌ولی (Silicon Valley ideology)"],
   "studies": ["Morozov, E. (2013). To Save Everything, Click Here. PublicAffairs.", "Morozov, E. (2011). The Net Delusion. PublicAffairs."],
 },
 "MC-226": {
   "summary": "«کار قابل‌رؤیت» (Visibility Labour) به کار مستمر و برنامه‌ریزی‌شده‌ای اشاره دارد که کاربران — به‌ویژه اینفلوئنسرها — برای دیده‌شدن، جلب توجه مخاطب و الگوریتم انجام می‌دهند. کریستال آبیدین در مطالعهٔ اینفلوئنسرهای مد در اینستاگرام (۲۰۱۶، Media International Australia) این مفهوم را معرفی کرد (Abidin, 2016).",
   "main_problem": "در اقتصاد پلتفرمی، دیده‌شدن چگونه به شکلی از کار بدل می‌شود، چه کسانی بار این کار را می‌کشند، و چه پیامدهایی برای هویت، پیشه و نابرابری دارد؟",
   "mechanism": "آبیدین نشان می‌دهد که اینفلوئنسرها برای «دیده‌شدن» کارهای چندلایه انجام می‌دهند: «کار خود-نمایشی» — انتخاب و آرایش مستمر تصویر، سبک و روایت شخصی؛ «کار رابطه‌ای» — ساختن و نگه‌داشتن رابطه با مخاطبان، برندها و همتایان از طریق تعامل روزمره؛ «کار الگوریتمی» — کشف، رمزگشایی و بازی با منطق پلتفرم برای افزایش نمایش؛ و «کار احساسی و زمانی» — حضور همیشگی و مدیریت احساسات در تعامل (Abidin, 2016). این کار نه یک‌باره بلکه پیوسته است، زیرا دیده‌شدن موقتی است و باید بازتولید شود. دافی (Duffy, 2017) با مفهوم «کار آرمانی» (aspirational labour) نشان داد که بسیاری از آفرینندگان محتوا، به امید شغلی خلاقانه، زمانی طولانی و بی‌مزد را صرف کار قابل‌رؤیت می‌کنند. در بستر رسانه، این نظریه اقتصاد توجه را از منظر کار تحلیل می‌کند: پلتفرم‌ها نمایش را به پاداش و درآمد گره می‌زنند، اما بار دیده‌شدن و هزینهٔ آن بر دوش کاربر می‌افتد؛ نتیجه، ترکیبی از فرصت خلاقانه و پیشه‌ای نامطمئن است که به‌طور نامتوازن میان گروه‌های اجتماعی توزیع می‌شود.",
   "assumptions": [
     "دیده‌شدن در پلتفرم‌ها نیازمند کار فعال و مستمر است.",
     "کار قابل‌رؤیت چندلایه و شامل کار الگوریتمی و رابطه‌ای است.",
     "نمایش پلتفرمی به درآمد و فرصت گره خورده است."
   ],
   "principles": [
     "دیده‌شدن به‌عنوان کار: نمایش، تلاشی برنامه‌ریزی‌شده است.",
     "چندلایه‌بودن: خود-نمایشی، رابطه، الگوریتم و احساس در هم تنیده‌اند.",
     "بازتولید مستمر: دیده‌شدن موقتی است و باید تکرار شود."
   ],
   "critiques": [
     "نابرابری جنسیتی و طبقاتی: بار کار قابل‌رؤیت به‌طور نامتوازن توزیع می‌شود.",
     "پیشگی نامطمئن: کار بدون حمایت نهادی و بی‌مزد، آسیب‌پذیری می‌آفریند.",
     "ابهام مرز: تفکیک کار از زندگی شخصی و اوقات فراغت دشوار می‌شود."
   ],
   "applications": [
     "تحلیل کار آفرینندگان محتوا و اقتصاد اینفلوئنسری.",
     "پژوهش دربارهٔ کار الگوریتمی و تعامل پلتفرمی.",
     "نقد پیشگی و نابرابری در اقتصاد توجه."
   ],
   "evolution": "آبیدین (2016) مفهوم را برای اینفلوئنسرهای اینستاگرام معرفی کرد و دافی (2017) کار آرمانی را افزود. در دههٔ ۲۰۲۰، پژوهش کار قابل‌رؤیت به تیک‌تاک، استریمینگ و اقتصاد خالق گسترش یافت.",
   "key_concepts": ["کار قابل‌رؤیت (visibility labour)", "کار آرمانی (aspirational labour)", "کار الگوریتمی (algorithmic labour)", "کار احساسی (emotional labour)", "اقتصاد توجه (attention economy)"],
   "studies": ["Abidin, C. (2016). Visibility labour. Media International Australia, 161(1), 86-100.", "Duffy, B. E. (2017). (Not) Getting Paid to Do What You Love. Yale University Press."],
 },
 "MC-227": {
   "summary": "«پروپاگاندای محاسباتی» (Computational Propaganda) به استفادهٔ سازمان‌یافته از خودکارسازی، الگوریتم‌ها و داده برای دستکاری افکار عمومی در رسانه‌های اجتماعی اشاره دارد: ربات‌ها، حساب‌های جعلی، ترول‌ها، تبلیغات هدفمند و رفتار ناهماهنگ هماهنگ‌شده. ساموئل وولی و فیلیپ هاوارد در «Computational Propaganda» (۲۰۱۸، Oxford University Press) این پدیده را نظام‌مند کردند (Woolley & Howard, 2018).",
   "main_problem": "چگونه بازیگران سیاسی و دولتی از خودکارسازی و دادهٔ پلتفرمی برای دستکاری افکار عمومی بهره می‌گیرند، این سازوکار چگونه عمل می‌کند، و چه پیامدهایی برای انتخابات، اعتماد عمومی و دموکراسی دارد؟",
   "mechanism": "وولی و هاوارد پروپاگاندای محاسباتی را بر پایهٔ سه مؤلفه تحلیل می‌کنند: «خودکارسازی» — استفاده از ربات‌ها، حساب‌های سایبورگ (نیمه‌خودکار) و حساب‌های جعلی برای تولید، تقویت و تکثیر محتوا؛ «الگوریتم‌ها» — بهره‌گیری از منطق توزیع پلتفرم برای دیده‌شدن و برجسته‌سازی؛ و «داده» — هدف‌گیری مخاطب بر اساس داده‌های جمعیتی، رفتاری و روان‌شناختی (Woolley & Howard, 2018). این مؤلفه‌ها در قالب «دستگاه سازمانی» عمل می‌کنند: احزاب، شرکت‌های روابط عمومی، آژانس‌های دولتی و شبکه‌های حامی. برادشاو و هاوارد (Bradshaw & Howard, 2019) در سیاههٔ جهانی نشان دادند که دستکاری سازمان‌یافتهٔ رسانه‌های اجتماعی به ده‌ها کشور گسترش یافته است. پیامدهای کلیدی شامل تقویت قطب‌شدگی، کاهش اعتماد به رسانه و نهادها، و ایجاد «عدم‌قطعیت معرفتی» است. در بستر رسانه، نظریه چارچوبی برای فهم «اطلاعات نادرست هماهنگ‌شده» فراهم می‌کند: نه فقط دروغ واحد، بلکه زیرساختی خودکار و هدفمند که فضای اطلاعاتی را دستکاری می‌کند و تشخیص مرز میان صدای واقعی مردم و صدای مصنوع را دشوار می‌سازد.",
   "assumptions": [
     "خودکارسازی، الگوریتم و داده به ابزار دستکاری سیاسی بدل شده‌اند.",
     "بازیگران سازمان‌یافته (حزب، دولت، شرکت) پشت این کمپین‌ها هستند.",
     "پروپاگاندای محاسباتی بر اعتماد و قطب‌شدگی اثر می‌گذارد."
   ],
   "principles": [
     "سه مؤلفه: خودکارسازی، الگوریتم و داده.",
     "دستگاه سازمانی: بازیگران نهادی پشت کمپین‌ها هستند.",
     "دستکاری زیرساختی: هدف، فضای اطلاعاتی است، نه فقط پیام."
   ],
   "critiques": [
     "دشواری سنجش: شناسایی ربات‌ها و تفکیک رفتار خودکار از انسانی خطاپذیر است.",
     "اغراق اثر: میزان واقعی اثر پروپاگاندای محاسباتی بر رفتار سیاسی محل بحث است.",
     "ابهام مفهومی: گسترهٔ مفهوم «پروپاگاندای محاسباتی» با تبلیغات و روابط عمومی هم‌پوشانی دارد."
   ],
   "applications": [
     "تحلیل کمپین‌های دستکاری در انتخابات و بحران‌های سیاسی.",
     "پژوهش دربارهٔ ربات‌ها، شبکه‌های هماهنگ و اطلاعات نادرست.",
     "سیاست‌گذاری پلتفرم و حکمرانی محتوای خودکار."
   ],
   "evolution": "وولی و هاوارد (2018) چارچوب را تثبیت کردند و برادشاو و هاوارد (2019) گسترهٔ جهانی آن را مستند کردند. در دههٔ ۲۰۲۰، هوش مصنوعی مولد و جعل عمیق، پروپاگاندای محاسباتی را به مرحلهٔ تازه‌ای بردند.",
   "key_concepts": ["پروپاگاندای محاسباتی (computational propaganda)", "ربات شبکه‌ای (bot)", "حساب سایبورگ (cyborg account)", "رفتار ناهماهنگ هماهنگ‌شده (coordinated inauthentic behaviour)", "هدف‌گیری روان‌شناختی (psychographic targeting)"],
   "studies": ["Woolley, S. C., & Howard, P. N. (Eds.). (2018). Computational Propaganda. Oxford University Press.", "Bradshaw, S., & Howard, P. N. (2019). The Global Disinformation Order. Oxford Internet Institute."],
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
    codes = ["MC-220", "MC-224", "MC-226", "MC-227"]
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
    print("BATCH53 THEORY DONE")

if __name__ == "__main__":
    main()
