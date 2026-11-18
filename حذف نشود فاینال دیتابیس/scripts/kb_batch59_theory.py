# -*- coding: utf-8 -*-
"""Batch 59 (THEORY): MC-290 Public Service Media (Tracey 1998), MC-291 Lukes' Three-Dimensional Power (2005),
MC-292 Symbolic Power (Bourdieu 1991), MC-293 Privacy Paradox (Norberg, Horne & Horne 2007).
Anchors verified 2026-11-16."""
import pymysql, json

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch59-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch59_theory.json"

S = {
 "MC-290": [
   dict(kind="BOOK", title_en="The Decline and Fall of Public Service Broadcasting",
        title_fa="افول و سقوط پخش خدمات عمومی",
        authors="Tracey, M.", year=1998, publisher="Oxford: Oxford University Press", doi=None,
        url="https://global.oup.com/academic/product/decline-and-fall-of-public-service-broadcasting-9780198159247",
        language="en", isbn="9780198159247",
        citation="Tracey, M. (1998). The decline and fall of public service broadcasting. Oxford University Press.",
        locator="whole work", locator_type="work", supports="definition / normative case / decline thesis", verified=True),
   dict(kind="BOOK", title_en="The Media Welfare State: Nordic Media in the Digital Era",
        title_fa="دولت رفاه رسانه‌ای: رسانهٔ نوردیک در عصر دیجیتال",
        authors="Syvertsen, T., Enli, G., Mjos, O. J., & Moe, H.", year=2014,
        publisher="Ann Arbor: University of Michigan Press", doi=None, url=None,
        language="en", isbn=None,
        citation="Syvertsen, T., Enli, G., Mjos, O. J., & Moe, H. (2014). The media welfare state: Nordic media in the digital era. University of Michigan Press.",
        locator="whole work", locator_type="work", supports="evolution / universalism and editorial independence", verified=False),
 ],
 "MC-291": [
   dict(kind="BOOK", title_en="Power: A Radical View (2nd ed.)",
        title_fa="قدرت: دیدگاهی رادیکال (ویراست دوم)",
        authors="Lukes, S.", year=2005, publisher="Basingstoke: Palgrave Macmillan", doi=None,
        url="https://voidnetwork.gr/wp-content/uploads/2016/09/Power-A-Radical-View-Steven-Lukes.pdf",
        language="en", isbn="9780333420928",
        citation="Lukes, S. (2005). Power: A radical view (2nd ed.). Palgrave Macmillan.",
        locator="whole work", locator_type="work", supports="definition / three dimensions / latent conflict", verified=True),
   dict(kind="JOURNAL_ARTICLE", title_en="Two Faces of Power",
        title_fa="دو چهرهٔ قدرت",
        authors="Bachrach, P., & Baratz, M. S.", year=1962,
        publisher="American Political Science Review, 56(4), 947-952", doi=None, url=None, language="en", isbn=None,
        citation="Bachrach, P., & Baratz, M. S. (1962). Two faces of power. American Political Science Review, 56(4), 947-952.",
        locator="pp. 947-952", locator_type="page_range", supports="evolution / nondecision-making", verified=False),
 ],
 "MC-292": [
   dict(kind="BOOK", title_en="Language and Symbolic Power",
        title_fa="زبان و قدرت نمادین",
        authors="Bourdieu, P. (J. B. Thompson, Ed.)", year=1991, publisher="Cambridge, MA: Harvard University Press", doi=None,
        url="https://www.hup.harvard.edu/books/9780674510418",
        language="en", isbn="9780674510418",
        citation="Bourdieu, P. (1991). Language and symbolic power (J. B. Thompson, Ed.). Harvard University Press.",
        locator="whole work", locator_type="work", supports="definition / legitimate language / misrecognition", verified=True),
   dict(kind="JOURNAL_ARTICLE", title_en="Social Space and Symbolic Power",
        title_fa="فضای اجتماعی و قدرت نمادین",
        authors="Bourdieu, P.", year=1989,
        publisher="Sociological Theory, 7(1), 14-25", doi=None, url=None, language="en", isbn=None,
        citation="Bourdieu, P. (1989). Social space and symbolic power. Sociological Theory, 7(1), 14-25.",
        locator="pp. 14-25", locator_type="page_range", supports="evolution / social space and classification", verified=False),
 ],
 "MC-293": [
   dict(kind="JOURNAL_ARTICLE", title_en="The Privacy Paradox: Personal Information Disclosure Intentions versus Behaviors",
        title_fa="پارادوکس حریم خصوصی: نیت افشای اطلاعات شخصی در برابر رفتار",
        authors="Norberg, P. A., Horne, D. R., & Horne, D. A.", year=2007,
        publisher="Journal of Consumer Affairs, 41(1), 100-126", doi="10.1111/j.1745-6606.2006.00070.x",
        url="https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1745-6606.2006.00070.x",
        language="en", isbn=None,
        citation="Norberg, P. A., Horne, D. R., & Horne, D. A. (2007). The privacy paradox: Personal information disclosure intentions versus behaviors. Journal of Consumer Affairs, 41(1), 100-126.",
        locator="pp. 100-126", locator_type="page_range", supports="definition / intention-behavior gap / evidence", verified=True),
   dict(kind="JOURNAL_ARTICLE", title_en="Privacy and Human Behavior in the Age of Information",
        title_fa="حریم خصوصی و رفتار انسانی در عصر اطلاعات",
        authors="Acquisti, A., Brandimarte, L., & Loewenstein, G.", year=2015,
        publisher="Science, 347(6221), 509-514", doi=None, url=None, language="en", isbn=None,
        citation="Acquisti, A., Brandimarte, L., & Loewenstein, G. (2015). Privacy and human behavior in the age of information. Science, 347(6221), 509-514.",
        locator="pp. 509-514", locator_type="page_range", supports="evolution / behavioral explanations", verified=False),
 ],
}

ENRICH = {
 "MC-290": {
   "summary": "«رسانهٔ عمومی» (Public Service Media) الگویی از سازمان رسانه‌ای است که با بودجهٔ عمومی یا شبه‌عمومی، دسترسی همگانی و استقلال تحریریه، هدفش خدمت به شهروندی است، نه بیشینه‌سازی مخاطب یا سود. مایکل تریسی در «The Decline and Fall of Public Service Broadcasting» (۱۹۹۸، Oxford University Press) بنیاد هنجاری این نهاد و فشارهای سیاسی، ایدئولوژیک و فناورانه‌ای را که آیندهٔ آن را تهدید می‌کند تحلیل کرد (Tracey, 1998).",
   "definition": "رسانهٔ عمومی نهادی رسانه‌ای است که با منابع عمومی تأمین می‌شود، به همهٔ شهروندان دسترسی برابر می‌دهد و با استقلال از دولت و بازار، خدمات اطلاعاتی، فرهنگی و آموزشی عرضه می‌کند (Tracey, 1998).",
   "main_problem": "اگر رسانهٔ عمومی نه از فروش تبلیغات و نه از وفاداری سیاسی تغذیه می‌شود، مشروعیت و پایداری آن از کجا می‌آید، و چگونه می‌تواند در محیط چندرسانه‌ای و رقابت پلتفرم‌های جهانی، مأموریت عمومی خود را حفظ کند؟",
   "mechanism": "الگو بر چهار ستون استوار است. (۱) تأمین مالی غیربازاری: بودجهٔ عمومی، حق اشتراک یا ترکیبی از این دو، رسانه را از فشار مستقیم بازار رها می‌کند و امکان تولید محتوایی را می‌دهد که بازار تجاری تأمین نمی‌کند — از خبر محلی و برنامهٔ کودکان تا پژوهش عمیق. (۲) جهان‌شمولی: دسترسی جغرافیایی و اجتماعی برای همهٔ گروه‌ها، نه فقط بخش‌های پرسود؛ همین اصل، رسانهٔ عمومی را از رسانهٔ نخبه‌پسند متمایز می‌کند. (۳) استقلال تحریریه: فاصلهٔ نهادی از دولت و مالکیت خصوصی، با سازوکارهایی مانند هیئت امنا، منشور و قواعد ویرایشی تضمین می‌شود. (۴) خدمت به شهروندی: معیار موفقیت، منفعت عمومی است، نه سهم بازار؛ تریسی (۱۹۹۸) این را بنیاد اخلاقی و دموکراتیک نهاد می‌داند و هشدار می‌دهد که فشارهای سیاسی، تجاری‌سازی و فناورانه می‌توانند آن را به پخش صرفاً سرگرم‌کننده فروبکاهند. گذار از «پخش خدمات عمومی» به «رسانهٔ عمومی» به معنای گسترش مأموریت به پلتفرم‌های دیجیتال، خدمات برخط و تعامل است؛ سیورتسن و همکاران (۲۰۱۴) در تحلیل کشورهای نوردیک نشان می‌دهند که جهان‌شمولی، استقلال تحریریه و سیاست فرهنگی، وقتی در قانون و نظام تأمین مالی نهادینه شوند، رسانهٔ عمومی را به بخشی از «دولت رفاه رسانه‌ای» تبدیل می‌کنند. در بستر رسانه، مشروعیت این الگو به «ارزش عمومی» گره می‌خورد: آزمون ارزش عمومی پیش از راه‌اندازی خدمات تازه، سنجش منفعت اجتماعی و پاسخ‌گویی به مخاطب، سازوکارهایی‌اند که رسانهٔ عمومی را در برابر اتهام سواری مجانی بر بازار و وابستگی به دولت محافظت می‌کنند.",
   "assumptions": [
     "بخشی از نیازهای اطلاعاتی و فرهنگی جامعه را بازار تجاری تأمین نمی‌کند.",
     "استقلال نهادی از دولت و بازار، با طراحی حقوقی و مالی امکان‌پذیر است.",
     "منفعت عمومی قابل تعریف و تا اندازه‌ای قابل سنجش است."
   ],
   "principles": [
     "چهار ستون: تأمین مالی غیربازاری، جهان‌شمولی، استقلال تحریریه و خدمت به شهروندی.",
     "معیار موفقیت، ارزش عمومی است نه سهم بازار.",
     "گذار از پخش به خدمات چندرسانه‌ای، مأموریت را گسترش می‌دهد نه لغو."
   ],
   "critiques": [
     "«ارزش عمومی» مفهومی مبهم است و می‌تواند به ابزار توجیه تصمیم‌های سیاسی یا مدیریتی بدل شود.",
     "رسانهٔ عمومی در برخی کشورها به کانال تبلیغ دولت تبدیل شده و استقلال ادعایی آن محل مناقشه است.",
     "در رقابت با پلتفرم‌های جهانی، رسانهٔ عمومی هم به جذب مخاطب نیاز دارد و هم به حفظ مأموریت؛ این تنش به‌سادگی حل نمی‌شود."
   ],
   "applications": [
     "ارزیابی «آزمون ارزش عمومی» برای خدمات دیجیتال تازه.",
     "تحلیل سیاست رسانه و بازنگری منشور و نظام تأمین مالی.",
     "پژوهش مقایسه‌ای دربارهٔ استقلال تحریریه و جهان‌شمولی.",
     "طراحی خدمات خبری عمومی برای گروه‌های کم‌بهره از بازار."
   ],
   "evolution": "الگوی پخش خدمات عمومی در نیمهٔ نخست قرن بیستم شکل گرفت؛ تریسی (۱۹۹۸) بحران آن را در برابر تجاری‌سازی و فناوری تحلیل کرد. در دههٔ ۲۰۰۰-۲۰۱۰، مفهوم به «رسانهٔ عمومی» گسترش یافت و پژوهش‌های دولت رفاه رسانه‌ای، پیوند آن با سیاست فرهنگی و رفاه اجتماعی را نشان دادند.",
   "key_concepts": ["رسانهٔ عمومی (public service media)", "جهان‌شمولی (universality)", "استقلال تحریریه (editorial independence)", "ارزش عمومی (public value)", "دولت رفاه رسانه‌ای (media welfare state)", "خدمت به شهروندی (citizenship)"],
   "studies": ["Tracey, M. (1998). The Decline and Fall of Public Service Broadcasting. Oxford University Press.", "Syvertsen, T., Enli, G., Mjos, O. J., & Moe, H. (2014). The Media Welfare State. University of Michigan Press."],
   "detailed_analysis": "۱. بنیان و منطق نظری\nرسانهٔ عمومی بر این فرض استوار است که ارتباط جمعی کالایی نیست که تنها با منطق بازار توزیع شود. اگر تأمین خبر، آموزش و فرهنگ تنها به تقاضای پرداخت‌کننده وابسته باشد، گروه‌هایی که قدرت خرید یا توجه کمتری دارند از دسترسی محروم می‌شوند. رسانهٔ عمومی پاسخی نهادی به این شکست بازار است.\n\n۲. مشروعیت و پاسخ‌گویی\nچون منابع آن عمومی است، رسانهٔ عمومی باید هم منفعت خود را نشان دهد و هم از دخالت سیاسی محافظت شود. همین دو نیاز در تنش‌اند: پاسخ‌گویی زیاد به دولت، استقلال را تهدید می‌کند و پاسخ‌گویی کم، مشروعیت مالی را. طراحی نهادی خوب، این تنش را با سازوکارهای مستقل نظارت و سنجش اثر مدیریت می‌کند.\n\n۳. پیوند رسانه‌ای امروز\nدر محیط پلتفرمی، مأموریت عمومی از پخش به حضور دیجیتال گسترش یافته است. پرسش کلیدی این است که آیا رسانهٔ عمومی می‌تواند در همان زمین بازی الگوریتمی، ارزش عمومی را حفظ کند یا منطق تعامل، مأموریت را به حاشیه می‌راند."
 },
 "MC-291": {
   "summary": "«قدرت سه‌بعدی» (Three-Dimensional Power) چارچوبی است که قدرت را نه فقط در تصمیم‌های آشکار، بلکه در کنترل دستور کار و شکل‌دادن به ترجیحات و باورهای افراد می‌بیند. استیون لوکس در «Power: A Radical View» (ویراست دوم، ۲۰۰۵، Palgrave Macmillan) بعد سوم را معرفی کرد: قدرتی که مانع شکل‌گیری شکایت می‌شود و منافع گروه مسلط را طبیعی جلوه می‌دهد (Lukes, 2005).",
   "definition": "قدرت، ظرفیت تأثیرگذاری بر دیگران است؛ بعد سوم قدرت آن است که با شکل‌دادن به ادراک، ترجیح و باور، افراد را چنان بسازد که منافع گروه مسلط را منافع خود بپندارند و حتی از وجود تعارض آگاه نشوند (Lukes, 2005).",
   "main_problem": "اگر قدرت را تنها با تصمیم‌های قابل مشاهده بسنجیم، بخش بزرگی از آن نادیده می‌ماند؛ چگونه می‌توان قدرتی را تحلیل کرد که با جلوگیری از طرح موضوع، تعریف مسئله و شکل‌دادن به ترجیحات عمل می‌کند، و معیار تشخیص آن چیست؟",
   "mechanism": "لوکس سه بعد را به‌صورت لایه‌ای می‌سازد. (۱) بعد اول، قدرت تصمیم: در موقعیت‌های تعارض آشکار، کسی که تصمیم نهایی را می‌گیرد قدرت دارد؛ این همان تحلیل رفتاری رایج در علوم سیاسی است. (۲) بعد دوم، قدرت غیرتصمیم‌گیری: برخی موضوعات هرگز به دستور کار نمی‌رسند؛ با کنترل دستور کار، گروه مسلط می‌تواند مسئله‌ای را پیش از آنکه به تصمیم برسد، از میدان بیرون کند. این بعد وام‌دار بچراک و باراتز (۱۹۶۲) است. (۳) بعد سوم، قدرت ایدئولوژیک: عمیق‌ترین شکل قدرت، شکل‌دادن به ترجیحات و باورهاست؛ افراد ممکن است منافع خود را نشناسند و وضع موجود را طبیعی بدانند. لوکس (۲۰۰۵) این را «تعارض پنهان» می‌نامد: تعارضی که در آگاهی کنشگران حاضر نیست، اما با منافع «واقعی» آن‌ها در تضاد است. (۴) قدرت به‌عنوان ظرفیت: لوکس تأکید می‌کند که قدرت هم می‌تواند «قدرت بر» (سلطه) باشد و هم «قدرت برای» (توانمندسازی)؛ بعد سوم خطرناک‌ترین شکل سلطه است، زیرا قربانی خود را قربانی نمی‌بیند. در بستر رسانه، این چارچوب تحلیل را از سانسور آشکار به چارچوب‌بندی فراتر می‌برد: پوشش اقلیم که تنها راه‌حل فناورانه را برجسته می‌کند و تغییر الگوهای تولید را از دستور کار بیرون می‌گذارد، نمونهٔ بعد دوم است؛ و پذیرش عمومی این چارچوب، نمونهٔ بعد سوم.",
   "assumptions": [
     "قدرت را نمی‌توان تنها با تصمیم‌های مشاهده‌پذیر سنجید.",
     "منافع «واقعی» کنشگران را می‌توان جدا از ترجیحات بیان‌شدهٔ آن‌ها تحلیل کرد.",
     "شکل‌دادن به ادراک و ترجیح، شکلی از اعمال قدرت است."
   ],
   "principles": [
     "سه بعد: تصمیم آشکار، کنترل دستور کار و شکل‌دادن به ترجیحات.",
     "تعارض پنهان، نشانهٔ اعمال بعد سوم است.",
     "قدرت می‌تواند سلطه یا توانمندسازی باشد."
   ],
   "critiques": [
     "فرض «منافع واقعی» جدی‌ترین نقد است: چه کسی تعیین می‌کند منفعت واقعی فرد چیست؟",
     "بعد سوم به‌سختی آزمون‌پذیر است، زیرا نبود آگاهی را نمی‌توان به‌سادگی از نبود تعارض تفکیک کرد.",
     "تحلیل فوکو نشان می‌دهد قدرت محصول رابطه است، نه دارایی کسی؛ تمرکز لوکس بر عامل مسلط، بخشی از این پیچیدگی را نادیده می‌گیرد."
   ],
   "applications": [
     "تحلیل دستور کار خبری و موضوعاتی که از پوشش بیرون می‌مانند.",
     "پژوهش دربارهٔ چارچوب‌بندی اقلیم و حذف گزینه‌های ساختاری.",
     "نقد اولویت‌دهی الگوریتمی و تعریف مسئله در پلتفرم‌ها.",
     "مطالعهٔ پذیرش عمومی سیاست‌ها و شکل‌گیری ترجیحات."
   ],
   "evolution": "لوکس (۱۹۷۴) ایده را در پاسخ به رفتارگرایی و به بچراک و باراتز عرضه کرد؛ ویراست ۲۰۰۵ با دو مقالهٔ تازه، نقدها — از جمله نقد فوکو و مسئلهٔ عاملیت — را بررسی کرد. در مطالعات رسانه، چارچوب به تحلیل دستور کار، چارچوب‌بندی و قدرت الگوریتمی راه یافت.",
   "key_concepts": ["سه بعد قدرت (three dimensions of power)", "غیرتصمیم‌گیری (nondecision-making)", "تعارض پنهان (latent conflict)", "منافع واقعی (real interests)", "دستور کار (agenda)", "قدرت بر/قدرت برای (power over / power to)"],
   "studies": ["Lukes, S. (2005). Power: A Radical View (2nd ed.). Palgrave Macmillan.", "Bachrach, P., & Baratz, M. S. (1962). Two faces of power. American Political Science Review, 56(4), 947-952."],
   "detailed_analysis": "۱. بنیان و منطق نظری\nلوکس در برابر دو تقلیل موضع می‌گیرد: تقلیل قدرت به تصمیم آشکار (بعد اول) و تقلیل آن به کنترل دستور کار (بعد دوم). استدلال او این است که هر دو، قدرت را در سطح رفتار و تعارض آشکار می‌بینند و از لایهٔ عمیق‌تر — شکل‌دادن به خودِ ترجیحات — غافل می‌مانند.\n\n۲. مسئلهٔ روش\nبعد سوم یک ادعای تجربی ساده نیست؛ ادعایی دربارهٔ آگاهی و منافع است. به همین دلیل، لوکس به تحلیل تاریخی و تفسیری نیاز دارد و صرف پیمایش یا مشاهدهٔ رفتار کافی نیست. این ویژگی، هم غنای تحلیلی می‌آفریند و هم آسیب‌پذیری روش‌شناختی.\n\n۳. پیوند رسانه‌ای\nرسانه مهم‌ترین میدان بعد سوم است، زیرا چارچوب‌بندی خبری می‌تواند گزینه‌ها را از پیش حذف کند. پرسش انتقادی درست این است که چه موضوعاتی هرگز به بحث عمومی راه نمی‌یابند و چه کسی از این سکوت سود می‌برد."
 },
 "MC-292": {
   "summary": "«قدرت نمادین» (Symbolic Power) توانایی تعریف واقعیت اجتماعی و مشروع‌سازی آن تعریف است، به‌گونه‌ای که سلطه پذیرفته و «طبیعی» به نظر برسد. پیر بوردیو در «Language and Symbolic Power» (۱۹۹۱، Harvard University Press) نشان داد این قدرت از طریق زبان مشروع، سرمایهٔ نمادین و جایگاه نهادی گوینده اعمال می‌شود (Bourdieu, 1991).",
   "definition": "قدرت نمادین ظرفیت تحمیل طبقه‌بندی‌ها و معناهایی است که به‌عنوان بدیهی پذیرفته می‌شوند؛ قدرتی که با «به‌رسمیت‌شناختن» و نه با اجبار فیزیکی، جهان اجتماعی را می‌سازد (Bourdieu, 1991).",
   "main_problem": "چرا سلطه اغلب بدون مقاومت آشکار پذیرفته می‌شود، و چگونه زبان، طبقه‌بندی و مرجعیت نهادی، نظم اجتماعی را به‌عنوان امری طبیعی و بدیهی بازتولید می‌کنند؟",
   "mechanism": "چارچوب چهار سازوکار به‌هم‌پیوسته دارد. (۱) میدان و سرمایه: کنشگران در میدان‌های اجتماعی برای سرمایهٔ اقتصادی، فرهنگی، اجتماعی و نمادین رقابت می‌کنند؛ سرمایهٔ نمادین، اعتبار و شناخته‌شدگی است که به سایر سرمایه‌ها ارزش اجتماعی می‌دهد. (۲) زبان مشروع: بوردیو (۱۹۹۱) استدلال می‌کند قدرت کلام از خود واژه‌ها نمی‌آید، بلکه از جایگاه نهادی گوینده و پذیرش شنوندگان می‌آید؛ همان جمله‌ای که از یک مقام رسمی «معتبر» است، از یک فرد عادی فاقد اثر است. (۳) نادیده‌انگاری (misrecognition) و دُکسا (doxa): سلطه نمادین با «نشناختن» آن به‌عنوان سلطه عمل می‌کند؛ باورهای بدیهی و پیشاتأملی (doxa) چارچوب ممکن اندیشیدن را می‌سازند و بدیل‌ها را نامرئی می‌کنند. (۴) خشونت نمادین: اعمال خشونت از طریق طبقه‌بندی و تحقیر، که قربانی نیز در آن مشارکت می‌کند، زیرا معیارهای ارزیابی را درونی کرده است. بوردیو در «Social Space and Symbolic Power» (۱۹۸۹) این را به ساختار فضای اجتماعی و طبقه‌بندی‌های آن گره می‌زند. در بستر رسانه، این چارچوب توضیح می‌دهد چرا برخی صداها «کارشناس» و برخی «منبع مردمی» نامیده می‌شوند، چرا لهجه و لحن در رسانه نشانهٔ اعتبار است، و چرا چارچوب‌های مسلط خبری بدون سانسور آشکار، بدیل‌ها را به حاشیه می‌رانند.",
   "assumptions": [
     "کنشگران در میدان‌های اجتماعی برای سرمایه و اعتبار رقابت می‌کنند.",
     "زبان و طبقه‌بندی، واقعیت اجتماعی را می‌سازند، نه فقط توصیف می‌کنند.",
     "سلطه اغلب با پذیرش ناآگاهانهٔ قربانی بازتولید می‌شود."
   ],
   "principles": [
     "قدرت نمادین با مشروعیت عمل می‌کند، نه با اجبار.",
     "ارزش زبان از جایگاه نهادی گوینده می‌آید.",
     "دُکسا و نادیده‌انگاری، سلطه را نامرئی می‌کنند."
   ],
   "critiques": [
     "چارچوب گرایش به بازتولیدگرایی دارد و امکان مقاومت و تغییر را کم‌رنگ می‌کند.",
     "مفاهیم آن (سرمایهٔ نمادین، دُکسا) به‌سختی قابل سنجش تجربی‌اند.",
     "هم‌پوشانی با مفهوم هژمونی گرامشی، مرز تحلیلی و ارزش افزودهٔ آن را مبهم می‌کند."
   ],
   "applications": [
     "تحلیل سلسله‌مراتب منابع و کارشناسان در خبر.",
     "پژوهش دربارهٔ زبان مشروع، لهجه و اعتبار در رسانه.",
     "نقد بازنمایی طبقات و گروه‌های حاشیه‌ای.",
     "تحلیل میدان رسانه و استقلال نسبی آن از میدان قدرت."
   ],
   "evolution": "بوردیو مفهوم را در دههٔ ۱۹۷۰-۱۹۸۰ در آثار نظریهٔ عمل پرورد؛ مجموعهٔ ۱۹۹۱ آن را به‌صورت منسجم در زبان و قدرت گرد آورد. پژوهش‌های بعدی، چارچوب را در مطالعات خبر، موسیقی، سینما و رسانهٔ دیجیتال به‌کار گرفتند.",
   "key_concepts": ["قدرت نمادین (symbolic power)", "خشونت نمادین (symbolic violence)", "سرمایهٔ نمادین (symbolic capital)", "دُکسا (doxa)", "نادیده‌انگاری (misrecognition)", "زبان مشروع (legitimate language)", "میدان (field)"],
   "studies": ["Bourdieu, P. (1991). Language and Symbolic Power. Harvard University Press.", "Bourdieu, P. (1989). Social space and symbolic power. Sociological Theory, 7(1), 14-25."],
   "detailed_analysis": "۱. بنیان و منطق نظری\nبوردیو می‌کوشد از دوگانهٔ ذهن‌گرایی و عینیت‌گرایی فراتر رود: واقعیت اجتماعی نه فقط در ساختارهای عینی، بلکه در طبقه‌بندی‌های ذهنی ساخته می‌شود. قدرت نمادین، همان جایی است که این دو به هم می‌رسند؛ ساختار در بدن و ادراک کنشگران جاسازی می‌شود.\n\n۲. زبان و مرجعیت\nنکتهٔ رادیکال بوردیو این است که زبان، ابزار انتقال معنا نیست، بلکه ابزار قدرت است. اثربخشی کلام از «قدرت واژه‌ها» نمی‌آید، بلکه از قدرت نهادی گوینده و همدستی شنونده می‌آید. ازاین‌رو تحلیل رسانه باید به‌جای تحلیل متن، جایگاه گوینده و اقتصاد اعتبار را ببیند.\n\n۳. پیوند رسانه‌ای و نقد\nرسانه، میدان تولید سرمایهٔ نمادین است: تعیین اینکه چه کسی معتبر است، چه روایتی رسمی است و چه سبکی «حرفه‌ای» است. نقد اصلی این است که چارچوب بوردیو ممکن است بیش از حد بر بازتولید تأکید کند و ظرفیت بازتعریف و مقاومت را نادیده بگیرد."
 },
 "MC-293": {
   "summary": "«پارادوکس حریم خصوصی» (Privacy Paradox) به شکاف میان ابراز نگرانی دربارهٔ حریم خصوصی و افشای واقعی اطلاعات شخصی اشاره دارد: افراد می‌گویند برای دادهٔ خود ارزش قائل‌اند، اما در عمل آن را می‌دهند. پاتریشیا نوربرگ، دانیل هورن و دیوید هورن در «The Privacy Paradox» (۲۰۰۷، Journal of Consumer Affairs) این شکاف را به‌صورت تجربی سنجیدند (Norberg, Horne & Horne, 2007).",
   "definition": "پارادوکس حریم خصوصی، ناسازگاری میان نیت اعلام‌شدهٔ افراد برای محافظت از داده و رفتار واقعی آن‌ها در افشای اطلاعات است (Norberg, Horne & Horne, 2007).",
   "main_problem": "چرا افراد با وجود نگرانی اعلام‌شده دربارهٔ حریم خصوصی، اطلاعات شخصی خود را در پلتفرم‌ها افشا می‌کنند، و آیا این ناسازگاری ناشی از خطای شناختی افراد است یا از طراحی و محدودیت ساختاری محیط؟",
   "mechanism": "تبیین‌ها در چهار سطح حرکت می‌کنند. (۱) شکاف نیت-رفتار: نوربرگ و همکاران (۲۰۰۷) در مطالعه‌ای نیت افشا و رفتار واقعی را جدا سنجیدند و رابطهٔ ضعیف میان آن‌ها یافتند؛ نتیجه این است که نگرش اعلام‌شده پیش‌بینی‌کنندهٔ ضعیفی برای رفتار است. (۲) محاسبهٔ کوتاه‌مدت هزینه-فایده: پاداش فوری (تخفیف، دسترسی، شخصی‌سازی) بر هزینهٔ آتی و مبهم (نظارت، سوءاستفاده، تبعیض) غلبه می‌کند؛ همین عدم تقارن زمانی، ریشهٔ بخشی از شکاف است. (۳) سوگیری‌های شناختی: خوش‌بینی دربارهٔ ریسک («برای من اتفاق نمی‌افتد»)، سوگیری حال‌محور، اثر چارچوب و اطمینان بیش‌ازحد به کنترل، تصمیم را از الگوی عقلانی دور می‌کند. (۴) معماری انتخاب: فرض‌های پیش‌فرض، فرم‌های پیچیده، خستگی رضایت و طراحی فریب‌کارانه (dark patterns) هزینهٔ محافظت را بالا و افشا را آسان می‌کنند؛ آکوئیستی، برندیمارته و لوونشتاین (۲۰۱۵) نشان می‌دهند که تصمیم حریم خصوصی به‌شدت به بستر و لحظه وابسته است. در بستر رسانه، این چارچوب توضیح می‌دهد چرا کاربران با وجود نگرانی، رضایت به ردیابی برای دسترسی به خبر، تخفیف اشتراک یا محتوای شخصی‌شده می‌دهند، و چرا سیاست «خودمدیریتی» حریم خصوصی بر دوش کاربر، به‌تنهایی کارآمد نیست.",
   "assumptions": [
     "نیت اعلام‌شده و رفتار واقعی می‌توانند واگرا شوند.",
     "پاداش فوری و هزینهٔ آتی مبهم، در تصمیم حریم خصوصی نامتقارن عمل می‌کنند.",
     "طراحی محیط انتخاب، بر تصمیم افراد اثر معنادار دارد."
   ],
   "principles": [
     "نگرش حریم خصوصی، پیش‌بینی‌کنندهٔ ضعیف رفتار است.",
     "عدم تقارن زمانی پاداش و هزینه، شکاف را می‌سازد.",
     "معماری انتخاب و طراحی، رفتار حریم خصوصی را شکل می‌دهد."
   ],
   "critiques": [
     "نام «پارادوکس» ممکن است ناسازگاری ذاتی کاربر را مسلم فرض کند، در حالی که رفتار می‌تواند پاسخ عقلانی به اطلاعات ناقص و محدودیت باشد.",
     "بسیاری از مطالعات بر گزارش خودی تکیه دارند و شکاف نیت و رفتار را به‌درستی نمی‌سنجند.",
     "تأکید بر مسئولیت فردی می‌تواند مسئولیت پلتفرم و نهاد تنظیم‌گر را کم‌رنگ کند."
   ],
   "applications": [
     "تحلیل رضایت به ردیابی در سایت‌های خبری و اشتراک دیجیتال.",
     "طراحی شفاف‌تر رضایت و کاهش طراحی فریب‌کارانه.",
     "پژوهش دربارهٔ اثر پیام‌های حریم خصوصی بر رفتار کاربر.",
     "سیاست‌گذاری حفاظت از داده و ارزیابی کارآمدی خودمدیریتی."
   ],
   "evolution": "بارنز (۲۰۰۶) مفهوم را در شبکه‌های اجتماعی به‌کار برد و نوربرگ و همکاران (۲۰۰۷) آن را به‌صورت تجربی سنجیدند. در دههٔ ۲۰۱۰، پژوهش‌های اقتصاد رفتاری (Acquisti et al., 2015) تبیین تصمیم حریم خصوصی را غنی‌تر کرد و نقد سیاست خودمدیریتی رضایت را برجسته ساخت.",
   "key_concepts": ["پارادوکس حریم خصوصی (privacy paradox)", "شکاف نیت-رفتار (intention-behavior gap)", "محاسبهٔ حریم خصوصی (privacy calculus)", "سوگیری حال‌محور (present bias)", "طراحی فریب‌کارانه (dark patterns)", "خستگی رضایت (consent fatigue)"],
   "studies": ["Norberg, P. A., Horne, D. R., & Horne, D. A. (2007). The privacy paradox. Journal of Consumer Affairs, 41(1), 100-126.", "Acquisti, A., Brandimarte, L., & Loewenstein, G. (2015). Privacy and human behavior in the age of information. Science, 347(6221), 509-514."],
   "detailed_analysis": "۱. بنیان و منطق نظری\nپارادوکس حریم خصوصی در تقاطع روان‌شناسی مصرف‌کننده و اقتصاد اطلاعات شکل گرفت. مسئلهٔ اولیه ساده بود: چرا افراد در پیمایش‌ها نگرانی بالا نشان می‌دهند اما در عمل اطلاعات خود را می‌دهند؟ پاسخ‌های اولیه بر ناآگاهی یا بی‌عقلی کاربر تکیه می‌کردند.\n\n۲. بازتفسیر رفتارگرا\nپژوهش‌های بعدی نشان دادند که رفتار لزوماً غیرعقلانی نیست؛ در محیطی با اطلاعات ناقص، هزینهٔ محافظت بالا و پاداش فوری، افشا می‌تواند انتخاب معقولی باشد. ازاین‌رو کانون تحلیل از «خطای کاربر» به «طراحی محیط» منتقل شد.\n\n۳. پیوند رسانه‌ای و سیاست\nدر رسانه، درآمد تبلیغاتی و شخصی‌سازی، ساختار انگیزشی افشا را می‌سازد. نقد سیاستی مهم این است که مسئولیت را نمی‌توان تنها بر دوش کاربر گذاشت؛ طراحی، شفافیت و تنظیم‌گری، اجزای لازم حفاظت‌اند."
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
    codes = ["MC-290", "MC-291", "MC-292", "MC-293"]
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
    print("BATCH59 THEORY DONE")

if __name__ == "__main__":
    main()
