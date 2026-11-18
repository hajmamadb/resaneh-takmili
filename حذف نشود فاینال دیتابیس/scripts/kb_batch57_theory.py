# -*- coding: utf-8 -*-
"""Batch 57 (THEORY): MC-270 The Experience Economy (Pine & Gilmore 1998),
MC-272 Governmentality & Biopower (Foucault 1978/1991), MC-273 Communication Power (Castells 2009),
MC-279 Code Is Law (Lessig 1999). Anchors verified 2026-11-16."""
import pymysql, json

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch57-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch57_theory.json"

S = {
 "MC-270": [
   dict(kind="JOURNAL_ARTICLE", title_en="Welcome to the Experience Economy",
        title_fa="به اقتصاد تجربه خوش آمدید",
        authors="Pine, B. J., II, & Gilmore, J. H.", year=1998,
        publisher="Harvard Business Review, 76(4), 97-105", doi=None,
        url="https://hbr.org/1998/07/welcome-to-the-experience-economy",
        language="en", isbn=None,
        citation="Pine, B. J., II, & Gilmore, J. H. (1998). Welcome to the experience economy. Harvard Business Review, 76(4), 97-105.",
        locator="pp. 97-105", locator_type="page_range", supports="definition / four realms / progression of economic value", verified=True),
   dict(kind="BOOK", title_en="The Experience Economy: Work Is Theatre and Every Business a Stage",
        title_fa="اقتصاد تجربه: کار نمایش است و هر کسب‌وکار صحنه‌ای",
        authors="Pine, B. J., II, & Gilmore, J. H.", year=1999,
        publisher="Boston, MA: Harvard Business School Press", doi=None, url=None, language="en", isbn=None,
        citation="Pine, B. J., II, & Gilmore, J. H. (1999). The experience economy: Work is theatre and every business a stage. Harvard Business School Press.",
        locator="whole work", locator_type="work", supports="evolution / staging and memorabilia", verified=False),
 ],
 "MC-272": [
   dict(kind="BOOK_CHAPTER", title_en="Governmentality",
        title_fa="حکمرانی‌مندی",
        authors="Foucault, M.", year=1991,
        publisher="In G. Burchell, C. Gordon, & P. Miller (Eds.), The Foucault Effect (pp. 87-104). Hemel Hempstead: Harvester Wheatsheaf",
        doi=None, url="https://press.uchicago.edu/ucp/books/book/chicago/F/bo3684463.html",
        language="en", isbn="9780226080451",
        citation="Foucault, M. (1991). Governmentality. In G. Burchell, C. Gordon, & P. Miller (Eds.), The Foucault effect (pp. 87-104). Harvester Wheatsheaf.",
        locator="pp. 87-104", locator_type="page_range", supports="definition / conduct of conduct / three levels", verified=True),
   dict(kind="BOOK", title_en="The History of Sexuality, Vol. 1: An Introduction",
        title_fa="تاریخ جنسیت، جلد اول: درآمدی",
        authors="Foucault, M.", year=1978, publisher="New York: Pantheon Books", doi=None, url=None,
        language="en", isbn=None,
        citation="Foucault, M. (1978). The history of sexuality, Vol. 1: An introduction. Pantheon Books.",
        locator="whole work", locator_type="work", supports="evolution / biopower and population", verified=False),
 ],
 "MC-273": [
   dict(kind="BOOK", title_en="Communication Power",
        title_fa="قدرت ارتباطی",
        authors="Castells, M.", year=2009, publisher="Oxford: Oxford University Press", doi=None,
        url="https://global.oup.com/academic/product/communication-power-9780199681938",
        language="en", isbn="9780199567041",
        citation="Castells, M. (2009). Communication power. Oxford University Press.",
        locator="whole work", locator_type="work", supports="definition / programming and switching / mass self-communication", verified=True),
   dict(kind="BOOK", title_en="Networks of Outrage and Hope: Social Movements in the Internet Age",
        title_fa="شبکه‌های خشم و امید: جنبش‌های اجتماعی در عصر اینترنت",
        authors="Castells, M.", year=2012, publisher="Cambridge: Polity Press", doi=None, url=None,
        language="en", isbn=None,
        citation="Castells, M. (2012). Networks of outrage and hope: Social movements in the internet age. Polity Press.",
        locator="whole work", locator_type="work", supports="evolution / networked social movements", verified=False),
 ],
 "MC-279": [
   dict(kind="BOOK", title_en="Code and Other Laws of Cyberspace",
        title_fa="کد و دیگر قوانین فضای سایبر",
        authors="Lessig, L.", year=1999, publisher="New York: Basic Books", doi=None,
        url="https://lessig.org/images/resources/1999-Code.pdf",
        language="en", isbn="9780465039135",
        citation="Lessig, L. (1999). Code and other laws of cyberspace. Basic Books.",
        locator="whole work", locator_type="work", supports="definition / four modalities of regulation / code as architecture", verified=True),
   dict(kind="BOOK", title_en="Code: Version 2.0",
        title_fa="کد: نسخهٔ ۲.۰",
        authors="Lessig, L.", year=2006, publisher="New York: Basic Books", doi=None, url=None,
        language="en", isbn=None,
        citation="Lessig, L. (2006). Code: Version 2.0. Basic Books.",
        locator="whole work", locator_type="work", supports="evolution / revision of the argument", verified=False),
 ],
}

ENRICH = {
 "MC-270": {
   "summary": "«اقتصاد تجربه» (The Experience Economy) استدلال می‌کند ارزش اقتصادی از کالا و خدمت فراتر رفته و به «تجربهٔ به‌یادماندنی» رسیده است: عرضه‌ای که مشتری را در زمان و مکان درگیر می‌کند و خاطره‌ای قابل فروش می‌سازد. ب. جوزف پاین دوم و جیمز گیلمور در «Welcome to the Experience Economy» (۱۹۹۸، Harvard Business Review) این گذار را به‌عنوان مرحلهٔ بعدی پیشرفت ارزش اقتصادی صورت‌بندی کردند (Pine & Gilmore, 1998).",
   "definition": "تجربه، عرضهٔ اقتصادی متمایزی است که در آن شرکت از کالا به‌عنوان ابزار و از خدمت به‌عنوان صحنه استفاده می‌کند تا مشتری را در رویدادی به‌یادماندنی درگیر کند؛ ارزش آن از موضوعِ فروش به «حالتِ ادراکی مشتری» منتقل می‌شود (Pine & Gilmore, 1998).",
   "main_problem": "اگر خدمات نیز به‌سرعت به کالایی همسان‌شده تبدیل می‌شوند، شرکت‌ها چگونه می‌توانند ارزش متمایز و پایدار بسازند، و چه چیزی مشتری را به پرداخت بهای بالاتر برای یک رویداد — به‌جای یک کالا یا خدمت — وادار می‌کند؟",
   "mechanism": "استدلال در چهار گام بسط می‌یابد. (۱) پیشرفت ارزش اقتصادی: پاین و گیلمور (۱۹۹۸) توالی کالای خام، کالا، خدمت و تجربه را ترسیم می‌کنند و «همسان‌شدگی» (commoditization) را موتور این توالی می‌دانند؛ هر مرحله که همسان می‌شود، ارزش به مرحلهٔ بعد مهاجرت می‌کند. تجربه، آخرین حلقهٔ این زنجیره در مقالهٔ ۱۹۹۸ است. (۲) تمایز تجربه از خدمت: خدمت «نامشهود» است و از آن خریدار انتظار عملکرد دارد، در حالی که تجربه «به‌یادماندنی» است و خریدار برای احساس و روایت آن پول می‌دهد؛ همین تفاوت، امکان قیمت‌گذاری بر پایهٔ ارزش ادراکی را فراهم می‌کند. (۳) چهار قلمرو تجربه: «سرگرمی» (جذب منفعل و تماشا)، «آموزشی» (جذب فعال و یادگیری)، «گریز از واقعیت» (غرق‌شدن فعال) و «زیبایی‌شناختی» (غرق‌شدن منفعل و حضور در محیط). این چهار قلمرو روی دو محور قرار می‌گیرند: میزان مشارکت (فعال/منفعل) و نوع ارتباط (جذب/غرق‌شدن)؛ تجربهٔ غنی، چند قلمرو را هم‌زمان درمی‌نوردد. (۴) صحنه‌آرایی و شخصی‌سازی: شرکت به «صحنه‌آرا» بدل می‌شود و با شخصی‌سازی انبوه، نشانه‌های فیزیکی و یادگاری، تجربه را از یکسان‌سازی بیرون می‌کشد. در بستر رسانه، این چارچوب توضیح می‌دهد چرا پلتفرم‌ها از پخش سادهٔ محتوا به رویداد زنده، اکران ویژه، نمایش مشترک، تجربهٔ تعاملی و بستهٔ هواداری حرکت می‌کنند: رقابت دیگر بر سر دسترسی به فایل نیست، بلکه بر سر ساختن لحظه‌ای است که مخاطب بخواهد دربارهٔ آن حرف بزند.",
   "assumptions": [
     "همسان‌شدن عرضه‌ها، ارزش اقتصادی را به لایهٔ تجربه منتقل می‌کند.",
     "مشتری حاضر است برای خاطره و احساس، بیش از کارکرد خالص بپردازد.",
     "تجربه را می‌توان با صحنه‌آرایی و شخصی‌سازی طراحی و تا اندازه‌ای کنترل کرد."
   ],
   "principles": [
     "تجربه عرضهٔ اقتصادی متمایزی است، نه افزوده‌ای بر خدمت.",
     "چهار قلمرو سرگرمی، آموزشی، گریز از واقعیت و زیبایی‌شناختی.",
     "صحنه‌آرایی و شخصی‌سازی، تجربه را از همسان‌شدگی حفظ می‌کند."
   ],
   "critiques": [
     "چارچوب بیشتر مشاوره‌ای است و آزمون تجربی مستقل و سنجهٔ روشنی برای «کیفیت تجربه» عرضه نمی‌کند.",
     "مرز تجربه و خدمت در عمل مبهم است و بسیاری از خدمت‌های خوب نیز به‌یادماندنی‌اند.",
     "تأکید بر طراحی تجربه می‌تواند به کار احساسی و مدیریت عاطفهٔ کارکنان و کاربران بیانجامد، بی‌آنکه هزینه‌های انسانی آن دیده شود."
   ],
   "applications": [
     "طراحی رویدادهای زنده و اکران‌های ویژه برای هواداران یک برند رسانه‌ای.",
     "بازطراحی تجربهٔ اشتراک با بسته‌های تعاملی و محتوای پس‌ازپرده.",
     "تحلیل موزه، جشنواره و نمایشگاه به‌عنوان عرضهٔ تجربی.",
     "برنامه‌ریزی بازاریابی تجربی برای رسانه‌های محلی و جامعه‌ای."
   ],
   "evolution": "مقالهٔ ۱۹۹۸ توالی ارزش را معرفی کرد و کتاب ۱۹۹۹ آن را با استعارهٔ «کار به‌مثابهٔ نمایش» و مفهوم یادگاری بسط داد. در ویراست‌های بعدی، پاین و گیلمور مرحلهٔ پنجم یعنی «تحول» را افزودند. در اقتصاد پلتفرمی، مفهوم تجربه به تجربهٔ کاربری، طراحی احساس و رویدادهای دیجیتال گسترش یافت.",
   "key_concepts": ["اقتصاد تجربه (experience economy)", "همسان‌شدگی (commoditization)", "چهار قلمرو تجربه (four realms)", "صحنه‌آرایی (staging)", "شخصی‌سازی انبوه (mass customization)", "یادگاری (memorabilia)"],
   "studies": ["Pine, B. J., II, & Gilmore, J. H. (1998). Welcome to the experience economy. Harvard Business Review, 76(4), 97-105.", "Pine, B. J., II, & Gilmore, J. H. (1999). The Experience Economy. Harvard Business School Press."],
   "detailed_analysis": "۱. بنیان و منطق نظری\nنظریهٔ اقتصاد تجربه در سنت اقتصاد خدمت و بازاریابی رابطه‌ای ریشه دارد، اما گامی فراتر می‌گذارد: در اقتصاد خدمت، ارزش در تعامل انسانی نهفته است؛ در اقتصاد تجربه، ارزش در حالتی است که در مشتری برانگیخته می‌شود. ازاین‌رو کالا و خدمت به «مواد اولیه» تجربه فرومی‌کاهند.\n\n۲. سازوکار ارزش\nتجربه سه ویژگی اقتصادی دارد: شخصی است (نمی‌توان آن را به دیگری منتقل کرد)، به‌یادماندنی است (ارزش در حافظه می‌ماند) و در زمان و مکان رخ می‌دهد (نمونه‌پذیر نیست). همین سه ویژگی، آن را از کالای قابل تکثیر متمایز می‌کند و قدرت قیمت‌گذاری می‌آفریند.\n\n۳. پیوند رسانه‌ای و نقد\nبرای رسانه، تجربه هم فرصت است و هم خطر: فرصت، چون رویداد و تجربهٔ مشترک وفاداری می‌سازد؛ خطر، چون طراحی تجربه می‌تواند به دستکاری احساس و افزایش هزینهٔ زمانی مخاطب بینجامد. پژوهش انتقادی رسانه باید بپرسد چه کسی صحنه را می‌آراید و چه کسی هزینهٔ آن را می‌پردازد."
 },
 "MC-272": {
   "summary": "«حکمرانی‌مندی و قدرت زیستی» (Governmentality & Biopower) دو مفهوم فوکویی برای توضیح شیوهٔ حکومت در دوران مدرن است: قدرت نه با فرمان و زور، بلکه با «هدایت رفتار» آزادانهٔ افراد و مدیریت «جمعیت» به‌عنوان یک کل عمل می‌کند. میشل فوکو در درس‌گفتار «Governmentality» (۱۹۷۸، منتشرشده در The Foucault Effect، ۱۹۹۱) و در «تاریخ جنسیت» (۱۹۷۸) این دو مفهوم را صورت‌بندی کرد (Foucault, 1991؛ Foucault, 1978).",
   "definition": "حکمرانی‌مندی، «هدایتِ هدایت‌پذیری» است: مجموعهٔ اندیشه‌ها، نهادها و فنونی که رفتار افراد و جمعیت را با تکیه بر آزادی آنان شکل می‌دهند؛ قدرت زیستی، شکل مدرن قدرتی است که زندگی جمعیت — سلامت، زاد و ولد، مرگ‌ومیر و ریسک — را موضوع مدیریت خود می‌سازد (Foucault, 1991).",
   "main_problem": "چرا قدرت مدرن به‌جای سرکوب و مجازات، به‌سراغ مدیریت زندگی، سلامت و رفتار روزمره می‌رود، و چگونه دانش آماری و هنجارهای جمعیتی، افراد را به سوژه‌هایی خودگردان تبدیل می‌کنند که خودشان رفتار خود را تنظیم می‌کنند؟",
   "mechanism": "مفهوم در چهار لایه کار می‌کند. (۱) «هدایت رفتار» (conduct of conduct): قدرت مدرن نه با ممانعت، بلکه با شکل‌دادن به میدان امکان‌ها عمل می‌کند؛ افراد آزاد فرض می‌شوند، اما گزینه‌ها، معیارها و خودفهمی‌شان چنان ساخته می‌شود که رفتار مطلوب را «انتخاب» کنند. (۲) سه سطح حکومت: فوکو سه شکل تاریخی را از هم جدا می‌کند — قدرت حاکمیتی مبتنی بر سرزمین و فرمان، قدرت انضباطی مبتنی بر بدن فردی و نهادهای بسته، و حکمرانی‌مندی مبتنی بر جمعیت و اقتصاد سیاسی. سطح سوم است که با ظهور آمار، جمعیت‌شناسی و اقتصاد سیاسی شکل می‌گیرد. (۳) دستگاه‌های امنیت (apparatuses of security): برخلاف انضباط که می‌کوشد همه‌چیز را دقیق تنظیم کند، امنیت با «نرخ‌ها» و «احتمال‌ها» کار می‌کند: نرخ زاد و ولد، مرگ‌ومیر، جرم و بیماری را می‌سنجد، بازهٔ قابل قبول تعیین می‌کند و انحراف را با مداخلهٔ هدفمند تنظیم می‌کند. (۴) قدرت زیستی: دو قطب مکمل — «سیاست بدن» (anatomo-politics) که بدن فردی را آموزش و بهینه می‌کند و «تنظیم جمعیت» (regulatory controls) که زاد و ولد، سلامت و طول عمر جمعیت را مدیریت می‌کند؛ نتیجه، گذار از «حق مرگ» حاکم به «قدرت بر زندگی» است. (۵) خودگردانی: تکنولوژی‌های خود، افراد را به بازبینی و مدیریت خویش وامی‌دارند و مسئولیت‌پذیر می‌سازند. در بستر رسانه، داشبوردهای تحلیلی نمونهٔ روشنی از دستگاه امنیت دیجیتال‌اند: سنجه‌هایی مانند نرخ کلیک و زمان تماشا، هنجار می‌سازند و رفتار تحریریه را بدون دستور صریح تنظیم می‌کنند.",
   "assumptions": [
     "قدرت مدرن بیش از سرکوب، از طریق شکل‌دادن به رفتار آزاد عمل می‌کند.",
     "جمعیت، موجودیتی قابل اندازه‌گیری و مدیریت است که با آمار و هنجار شناخته می‌شود.",
     "دانش (آمار، جمعیت‌شناسی، اقتصاد) و قدرت، یکدیگر را تولید می‌کنند."
   ],
   "principles": [
     "حکمرانی‌مندی هدایت هدایت‌پذیری است، نه فرمان.",
     "سه سطح حاکمیتی، انضباطی و حکمرانی‌مندی.",
     "قدرت زیستی، زندگی جمعیت را موضوع مدیریت می‌سازد."
   ],
   "critiques": [
     "مفهوم چنان گسترده است که مرز آن با سایر اشکال قدرت روشن نیست و سنجش تجربی آن دشوار می‌شود.",
     "فوکو تفاوت‌های نهادی و تاریخی میان دولت‌ها را کم‌رنگ می‌کند و تعمیم او به جنوب جهانی محل بحث است.",
     "کم‌توجهی به عاملیت و مقاومت: اگر قدرت همه‌جا حاضر است، امکان تغییر چگونه تصور می‌شود؟"
   ],
   "applications": [
     "تحلیل سنجه‌های تحلیلی و داشبورد به‌عنوان دستگاه هنجارساز در تحریریه.",
     "پژوهش دربارهٔ کمپین‌های سلامت عمومی و مدیریت جمعیت از طریق رسانه.",
     "نقد حکمرانی الگوریتمی و مسئولیت‌پذیرسازی کاربران در پلتفرم‌ها.",
     "مطالعهٔ آمار رسمی و پیمایش افکار عمومی به‌عنوان فناوری قدرت."
   ],
   "evolution": "فوکو مفاهیم را در درس‌گفتارهای ۱۹۷۶-۱۹۷۹ صورت‌بندی کرد؛ انتشار انگلیسی «Governmentality» در ۱۹۹۱ مکتب «مطالعات حکمرانی‌مندی» را شکل داد. در دههٔ ۲۰۱۰، پژوهش‌های حکمرانی الگوریتمی و داده‌محور، چارچوب را برای تحلیل پلتفرم‌ها و نظارت دیجیتال به‌کار گرفتند.",
   "key_concepts": ["حکمرانی‌مندی (governmentality)", "قدرت زیستی (biopower)", "هدایت رفتار (conduct of conduct)", "دستگاه امنیت (apparatus of security)", "جمعیت (population)", "خودگردانی (technologies of the self)"],
   "studies": ["Foucault, M. (1991). Governmentality. In G. Burchell, C. Gordon, & P. Miller (Eds.), The Foucault Effect (pp. 87-104). Harvester Wheatsheaf.", "Foucault, M. (1978). The History of Sexuality, Vol. 1. Pantheon Books."],
   "detailed_analysis": "۱. بنیان و منطق نظری\nفوکو در این آثار از پرسش «قدرت چیست؟» به پرسش «قدرت چگونه کار می‌کند؟» می‌رود. پاسخ او روابط قدرت را نه مالکیت بلکه راهبرد می‌داند: قدرت در شبکهٔ pratiques، دانش‌ها و نهادها جریان دارد و محصول آن، شکل‌گیری سوژه‌هایی است که خود را می‌شناسند و اداره می‌کنند.\n\n۲. از انضباط به امنیت\nدر آثار پیشین، فوکو بر نهادهای بسته (زندان، بیمارستان، پادگان) و انضباط بدن متمرکز بود. در درس‌گفتار حکمرانی‌مندی، توجه به سطح جمعیت و مکانیسم‌های امنیتی جابه‌جا می‌شود که با نرخ و احتمال و بازهٔ نرمال کار می‌کنند. این جابه‌جایی، تحلیل رسانه را از «اثر پیام بر فرد» به «مدیریت جمعیت مخاطب» منتقل می‌کند.\n\n۳. پیوند با رسانه و داده\nاندازه‌گیری مخاطب از ابتدا فناوری حکومت بود: رتبه‌بندی، سهم بازار و نرخ نفوذ، جمعیت مخاطب را به عدد و هنجار تبدیل می‌کردند. در محیط الگوریتمی، این منطق به سطح فردی و پیوسته گسترش یافته است؛ همان چیزی که پژوهشگران آن را «حکمرانی الگوریتمی» نامیده‌اند."
 },
 "MC-273": {
   "summary": "«قدرت ارتباطی» (Communication Power) نظریه‌ای است که قدرت را در جامعهٔ شبکه‌ای از کنترل بر شبکه‌های ارتباطی می‌بیند: هر کس بتواند اهداف و قواعد شبکه را تعیین کند یا شبکه‌ها را به هم وصل و از هم جدا کند، قدرت را در دست دارد. مانوئل کاستلز در «Communication Power» (۲۰۰۹، Oxford University Press) این نظریه را با تحلیل صنعت رسانه، سیاست و جنبش‌های اجتماعی بسط داد (Castells, 2009).",
   "definition": "قدرت ارتباطی، ظرفیت ساخت معنا در ذهن افراد از طریق برنامه‌ریزی شبکه‌های ارتباطی و اتصال یا قطع آن‌هاست؛ قدرت در جامعهٔ شبکه‌ای نه در نهاد واحد، بلکه در هندسهٔ متغیر شبکه‌ها قرار دارد (Castells, 2009).",
   "main_problem": "در جامعه‌ای که نهادها و افراد در شبکه‌های جهانی ارتباطی سازمان یافته‌اند، قدرت چگونه اعمال می‌شود، چه کسی معنا را برنامه‌ریزی می‌کند، و جنبش‌های اجتماعی چگونه می‌توانند در برابر قدرت شبکه‌ای مقاومت کنند؟",
   "mechanism": "نظریه چهار عنصر به‌هم‌پیوسته دارد. (۱) قدرت در شبکه: کاستلز (۲۰۰۹) چهار شکل قدرت را از هم جدا می‌کند — «قدرت شبکه‌سازی» (توان پیوستن به شبکه)، «قدرت شبکه» (قدرت شبکه بر اعضای خود از طریق قواعد)، «قدرت شبکه‌ای» (قدرت برخی گره‌ها بر دیگران) و «قدرت شبکه‌سازی مجدد» (توان برنامه‌ریزی و تغییر اتصال‌ها). شکل چهارم، بالاترین سطح است. (۲) دو مکانیسم عملی: «برنامه‌ریزی» (programming) یعنی تعیین اهداف، قواعد و پروتکل‌های شبکه، و «اتصال‌دهی» (switching) یعنی وصل‌کردن یا قطع‌کردن شبکه‌ها و منابع. هر دو مکانیسم در مالکیت پلتفرم، الگوریتم و زیرساخت فنی تجسم می‌یابند. (۳) ارتباط خودمختار انبوه: در کنار شبکه‌های رسانه‌ای شرکتی، شکل تازه‌ای از ارتباط افقی پدید آمده که کاربران تولیدکنندهٔ محتوا و توزیع‌کنندهٔ آن‌اند؛ این ارتباط خودمختار، امکان به‌چالش‌کشیدن برنامه‌ریزی قدرت را فراهم می‌کند، اما خود در بستر همان پلتفرم‌ها محصور است. (۴) قدرت معنا: سیاست در نهایت بر «ذهن‌ها» اعمال می‌شود و چارچوب‌بندی مسئله، برجسته‌سازی و روایت، ابزار اصلی است؛ ازاین‌رو مبارزهٔ سیاسی، مبارزه بر سر برنامه‌ریزی معناست. در بستر رسانه، این چارچوب توضیح می‌دهد چرا اولویت‌دهی الگوریتمی «برنامه‌ریزی» است، حذف یک حساب یا قطع دسترسی به کانال خبری «اتصال‌دهی» است، و جنبش‌های هشتگ‌محور می‌کوشند با اتصال شبکه‌های افقی، برنامه‌ریزی رسانه‌ای مسلط را دور بزنند.",
   "assumptions": [
     "سازمان اجتماعی معاصر در قالب شبکه‌ها شکل گرفته است.",
     "قدرت از طریق ساخت معنا و کنترل جریان ارتباط اعمال می‌شود.",
     "برنامه‌ریزی و اتصال‌دهی، دو مکانیسم کافی برای توضیح قدرت شبکه‌ای‌اند."
   ],
   "principles": [
     "قدرت در هندسهٔ شبکه‌هاست، نه فقط در نهادها.",
     "برنامه‌ریزی و اتصال‌دهی دو مکانیسم اصلی قدرت ارتباطی‌اند.",
     "مبارزهٔ سیاسی، مبارزه بر سر برنامه‌ریزی معناست."
   ],
   "critiques": [
     "چهار شکل قدرت، انتزاعی‌اند و تفکیک تجربی آن‌ها در پژوهش میدانی دشوار است.",
     "نظریه به تعیین‌گرایی شبکه‌ای نزدیک می‌شود و مالکیت زیرساخت و منطق سرمایه را کم‌رنگ می‌کند.",
     "تأکید بر ارتباط خودمختار انبوه ممکن است توان پلتفرم‌ها در کنترل زیرساختی این ارتباط را دست‌کم بگیرد."
   ],
   "applications": [
     "تحلیل اولویت‌دهی الگوریتمی و حذف حساب به‌عنوان برنامه‌ریزی و اتصال‌دهی.",
     "پژوهش دربارهٔ جنبش‌های اجتماعی هشتگ‌محور و ارتباط خودمختار.",
     "نقد تمرکز مالکیت زیرساخت رسانه‌ای و قدرت پلتفرم.",
     "تحلیل سیاست چارچوب‌بندی و روایت در خبر."
   ],
   "evolution": "کاستلز پیش‌تر در سه‌گانهٔ «عصر اطلاعات» منطق شبکه را صورت‌بندی کرده بود؛ «Communication Power» (۲۰۰۹) آن را به نظریهٔ قدرت گره زد. در ۲۰۱۲ با «Networks of Outrage and Hope» چارچوب را برای جنبش‌های شبکه‌ای به‌کار گرفت و پژوهش‌های بعدی دربارهٔ پلتفرم‌ها، بحث را به قدرت زیرساختی گستردند.",
   "key_concepts": ["قدرت ارتباطی (communication power)", "برنامه‌ریزی (programming)", "اتصال‌دهی (switching)", "ارتباط خودمختار انبوه (mass self-communication)", "جامعهٔ شبکه‌ای (network society)", "قدرت شبکه‌سازی مجدد (network-making power)"],
   "studies": ["Castells, M. (2009). Communication Power. Oxford University Press.", "Castells, M. (2012). Networks of Outrage and Hope. Polity Press."],
   "detailed_analysis": "۱. بنیان و منطق نظری\nکاستلز قدرت را نه صرفاً در دولت یا طبقه، بلکه در «ظرفیت سازمان‌دهی» می‌بیند. در جامعهٔ شبکه‌ای، برنامه‌ها و ارزش‌ها در شبکه‌ها جاسازی شده‌اند و تغییر اجتماعی بدون تغییر برنامه‌ریزی شبکه ممکن نیست. ازاین‌رو تحلیل قدرت باید تحلیل پروتکل، الگوریتم و اتصال باشد.\n\n۲. رابطهٔ قدرت و ارتباط\nارتباط، مادهٔ خام قدرت است، زیرا معنا را می‌سازد و کنش را جهت می‌دهد. کاستلز این را با مثال رسانه‌های شرکتی و شبکه‌های افقی هم‌زمان نشان می‌دهد: قدرت از بالا برنامه‌ریزی می‌کند و از پایین با اتصال شبکه‌های تازه به چالش کشیده می‌شود.\n\n۳. محدودیت تحلیل\nنظریه غنی توصیفی است، اما سنجهٔ تجربی روشنی برای «قدرت برنامه‌ریزی» عرضه نمی‌کند. افزون بر این، با تمرکز بر منطق شبکه، ممکن است سؤال مالکیت و سرمایه را که زیرساخت شبکه را می‌سازد، به حاشیه براند."
 },
 "MC-279": {
   "summary": "«کد قانون است» (Code Is Law) بیان فشردهٔ این ایده است که در فضای سایبر، معماری فنی — یعنی کد، پروتکل و طراحی نرم‌افزار — رفتار کاربران را مستقیماً تنظیم می‌کند و در بسیاری از موارد کارکردی هم‌سنگ قانون دارد، بی‌آنکه فرایند قانون‌گذاری را طی کرده باشد. لارنس لسیگ در «Code and Other Laws of Cyberspace» (۱۹۹۹، Basic Books) این استدلال را در قالب نظریهٔ چهار شیوهٔ تنظیم صورت‌بندی کرد (Lessig, 1999).",
   "definition": "کد، مجموعهٔ قواعد فنی‌ای است که فضای ممکن کنش را در محیط دیجیتال تعیین می‌کند؛ چون می‌تواند رفتاری را ناممکن یا پرهزینه سازد، کد نوعی معماری تنظیم‌گر و در نتیجه شکلی از قانون است (Lessig, 1999).",
   "main_problem": "اگر فضای سایبر ذاتاً آزاد نیست و معماری آن را می‌توان چنان طراحی کرد که کنترل کامل ممکن شود، چه کسی و با چه مشروعیتی این معماری را تعیین می‌کند، و چگونه می‌توان ارزش‌های عمومی و حقوق اساسی را در کد ترجمه و تضمین کرد؟",
   "mechanism": "چارچوب با چهار عنصر کار می‌کند. (۱) چهار شیوهٔ تنظیم: رفتار را می‌توان با «قانون» (فرمان همراه با ضمانت اجرا)، «هنجار اجتماعی» (فشار اجتماعی)، «بازار» (قیمت و هزینه) و «معماری» (محدودیت فیزیکی یا فنی) تنظیم کرد. لسیگ (۱۹۹۹) تأکید می‌کند که این چهار عامل هم‌زمان عمل می‌کنند و هر مداخله باید اثر خود را بر هر چهار بسنجد. (۲) معماریِ فضای سایبر همان کد است: در جهان فیزیکی معماری، محدودیت مادی می‌سازد (دیوار نمی‌گذارد عبور کنید) و در فضای سایبر کد همان کار را می‌کند (فرمت رمزگذاری‌شده اجازهٔ کپی نمی‌دهد). ازاین‌رو کد، «قانون طبیعت» این فضا نیست، بلکه انتخابی انسانی و قابل تغییر است. (۳) قدرت تنظیم کامل: برخلاف قانون که پس از تخلف عمل می‌کند و هنجار که ناقص اجرا می‌شود، معماری می‌تواند پیش از وقوع، رفتار را ناممکن کند؛ همین ویژگی، کد را به ابزاری قدرتمند برای کنترل بدل می‌کند. (۴) ترجمهٔ ارزش‌ها: اگر کد قانون است، ارزش‌های عمومی — آزادی بیان، حریم خصوصی، دسترسی — باید آگاهانه در طراحی ترجمه شوند، نه آنکه نتیجهٔ جانبی تصمیم‌های فنی باشند. لسیگ از همین استدلال برای دفاع از نرم‌افزار آزاد و طراحی حساس به ارزش بهره می‌گیرد. در بستر رسانه، مدیریت حق دیجیتال (DRM)، معماری اشتراک‌گذاری محتوا، محدودیت کپی و سازوکار تأیید سن، نمونه‌هایی از قانون‌گذاری از طریق معماری‌اند که سیاست محتوای یک پلتفرم را بدون متن قانونی تعیین می‌کنند.",
   "assumptions": [
     "معماری فنی فضای سایبر، ساختهٔ انسان و قابل تغییر است.",
     "رفتار را می‌توان با محدودکردن فضای ممکن کنش، مؤثرتر از مجازات پسینی تنظیم کرد.",
     "ارزش‌های عمومی را می‌توان و باید در طراحی فنی ترجمه کرد."
   ],
   "principles": [
     "چهار شیوهٔ تنظیم: قانون، هنجار، بازار و معماری.",
     "کد، معماری فضای سایبر و شکلی از قانون است.",
     "تنظیم از طریق معماری می‌تواند کامل‌تر از قانون باشد، پس نیازمند نظارت است."
   ],
   "critiques": [
     "کد را غالباً شرکت‌های خصوصی و بدون شفافیت می‌نویسند؛ «قانون‌گذاری» بی‌مشروعیت، خطر اصلی است.",
     "استعارهٔ کد-قانون می‌تواند عاملیت کاربر و امکان مقاومت و بازطراحی را کم‌رنگ کند.",
     "در ویراست ۲۰۰۶ لسیگ خود بخشی از استدلال را تعدیل کرد و بر تعامل پیچیدهٔ قانون و کد و امکان تنظیم کد توسط قانون تأکید بیشتری گذاشت."
   ],
   "applications": [
     "تحلیل مدیریت حق دیجیتال و معماری محدودکنندهٔ استفاده از محتوا.",
     "طراحی حریم خصوصی و معماری حفاظت از داده در پلتفرم‌ها.",
     "نقد سازوکارهای تعدیل محتوا و حذف پیشینی محتوا.",
     "تحلیل سیاست دسترسی‌پذیری و ترجمهٔ ارزش‌های عمومی به طراحی فنی."
   ],
   "evolution": "کتاب ۱۹۹۹ استدلال را در بستر حقوق اینترنت طرح کرد؛ ویراست ۲۰۰۶ با عنوان «Code: Version 2.0» آن را بازنویسی و در بخش‌هایی تعدیل کرد. پس از آن، پژوهش‌های حکمرانی پلتفرم و طراحی حساس به ارزش، چارچوب را به تحلیل الگوریتم و زیرساخت گستردند.",
   "key_concepts": ["کد به‌عنوان قانون (code as law)", "چهار شیوهٔ تنظیم (four modalities)", "معماری (architecture)", "ترجمهٔ ارزش‌ها (value translation)", "مدیریت حق دیجیتال (DRM)", "نرم‌افزار آزاد (free software)"],
   "studies": ["Lessig, L. (1999). Code and Other Laws of Cyberspace. Basic Books.", "Lessig, L. (2006). Code: Version 2.0. Basic Books."],
   "detailed_analysis": "۱. بنیان و منطق نظری\nلسیگ در برابر دو دیدگاه رقیب موضع می‌گیرد: دیدگاهی که فضای سایبر را ذاتاً آزاد و غیرقابل تنظیم می‌داند و دیدگاهی که آن را با قانون سنتی قابل مهار می‌پندارد. استدلال او این است که فضای سایبر «طبیعت» ندارد؛ معماری آن انتخاب می‌شود و همین انتخاب، تعیین می‌کند چه رفتاری ممکن و چه رفتاری ناممکن باشد.\n\n۲. رابطهٔ متقابل قانون و کد\nقانون می‌تواند کد را تنظیم کند، همان‌گونه که کد می‌تواند اجرای قانون را ممکن یا ناممکن سازد. این رابطهٔ دوسویه، هستهٔ تحلیل تنظیم‌گری است: مداخلهٔ حقوقی بدون درک معماری فنی بی‌اثر می‌ماند و طراحی فنی بدون ملاحظهٔ حقوق، می‌تواند حقوق را دور بزند.\n\n۳. پیوند رسانه‌ای و نقد\nبرای رسانه، پرسش اصلی این است که چه کسی معماری توزیع و نمایش را تعیین می‌کند. وقتی پلتفرم با طراحی فنی، کپی، نقل و آرشیو را محدود می‌کند، سیاست محتوایی را بی‌آنکه قانونی نوشته باشد، عملی می‌سازد. نقد کلیدی، افزودن پرسش مشروعیت و شفافیت به تحلیل است: چه کسی این قانون را نوشته و چه کسی می‌تواند آن را تغییر دهد؟"
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
    codes = ["MC-270", "MC-272", "MC-273", "MC-279"]
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
    print("BATCH57 THEORY DONE")

if __name__ == "__main__":
    main()
