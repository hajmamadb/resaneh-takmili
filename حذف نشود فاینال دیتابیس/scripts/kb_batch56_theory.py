# -*- coding: utf-8 -*-
"""Batch 56 (THEORY): MC-263 Customer Lifetime Value (Gupta, Lehmann & Stuart 2004),
MC-266 Switching Costs and Customer Lock-in (Klemperer 1995),
MC-268 Recommender Systems and Churn in VOD (Gomez-Uribe & Hunt 2015),
MC-269 Jobs-to-be-Done (Christensen et al. 2016). Anchors verified 2026-11-16."""
import pymysql, json

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch56-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch56_theory.json"

S = {
 "MC-263": [
   dict(kind="JOURNAL_ARTICLE", title_en="Valuing Customers",
        title_fa="ارزش‌گذاری مشتریان",
        authors="Gupta, S., Lehmann, D. R., & Stuart, J. A.", year=2004,
        publisher="Journal of Marketing Research, 41(1), 7-18", doi="10.1509/jmkr.41.1.7.25084",
        url="https://journals.sagepub.com/doi/10.1509/jmkr.41.1.7.25084",
        language="en", isbn=None,
        citation="Gupta, S., Lehmann, D. R., & Stuart, J. A. (2004). Valuing customers. Journal of Marketing Research, 41(1), 7-18.",
        locator="pp. 7-18", locator_type="page_range", supports="definition / customer equity / retention economics", verified=True),
   dict(kind="JOURNAL_ARTICLE", title_en="Probability Models for Customer-Base Analysis",
        title_fa="مدل‌های احتمالی برای تحلیل پایهٔ مشتری",
        authors="Fader, P. S., & Hardie, B. G. S.", year=2009,
        publisher="Journal of Interactive Marketing, 23(1), 61-69", doi=None, url=None, language="en", isbn=None,
        citation="Fader, P. S., & Hardie, B. G. S. (2009). Probability models for customer-base analysis. Journal of Interactive Marketing, 23(1), 61-69.",
        locator="pp. 61-69", locator_type="page_range", supports="evolution / probabilistic customer-base models", verified=False),
 ],
 "MC-266": [
   dict(kind="JOURNAL_ARTICLE", title_en="Competition when Consumers have Switching Costs: An Overview with Applications to Industrial Organization, Macroeconomics, and International Trade",
        title_fa="رقابت هنگامی که مصرف‌کنندگان هزینهٔ جابه‌جایی دارند: مروری با کاربردها در سازمان صنعتی، اقتصاد کلان و تجارت بین‌الملل",
        authors="Klemperer, P.", year=1995,
        publisher="The Review of Economic Studies, 62(4), 515-539", doi="10.1093/restud/62.4.515",
        url="https://academic.oup.com/restud/article-abstract/62/4/515/1544107",
        language="en", isbn=None,
        citation="Klemperer, P. (1995). Competition when consumers have switching costs: An overview. The Review of Economic Studies, 62(4), 515-539.",
        locator="pp. 515-539", locator_type="page_range", supports="definition / competition dynamics / introductory pricing", verified=True),
   dict(kind="JOURNAL_ARTICLE", title_en="Consumer Switching Costs: A Typology, Antecedents, and Consequences",
        title_fa="هزینه‌های جابه‌جایی مصرف‌کننده: گونه‌شناسی، پیشایندها و پیامدها",
        authors="Burnham, T. A., Frels, J. K., & Mahajan, V.", year=2003,
        publisher="Journal of the Academy of Marketing Science, 31(2), 109-126", doi=None, url=None, language="en", isbn=None,
        citation="Burnham, T. A., Frels, J. K., & Mahajan, V. (2003). Consumer switching costs: A typology, antecedents, and consequences. Journal of the Academy of Marketing Science, 31(2), 109-126.",
        locator="pp. 109-126", locator_type="page_range", supports="evolution / typology of switching costs", verified=False),
 ],
 "MC-268": [
   dict(kind="JOURNAL_ARTICLE", title_en="The Netflix Recommender System: Algorithms, Business Value, and Innovation",
        title_fa="سامانهٔ توصیه‌گر نتفلیکس: الگوریتم‌ها، ارزش تجاری و نوآوری",
        authors="Gomez-Uribe, C. A., & Hunt, N.", year=2015,
        publisher="ACM Transactions on Management Information Systems, 6(4), Article 13", doi="10.1145/2843948",
        url="https://dl.acm.org/doi/10.1145/2843948",
        language="en", isbn=None,
        citation="Gomez-Uribe, C. A., & Hunt, N. (2015). The Netflix recommender system: Algorithms, business value, and innovation. ACM Transactions on Management Information Systems, 6(4), Article 13.",
        locator="Article 13", locator_type="work", supports="definition / algorithms / engagement and churn value", verified=True),
   dict(kind="BOOK", title_en="Recommender Systems Handbook (2nd ed.)",
        title_fa="راهنمای سامانه‌های توصیه‌گر (ویراست دوم)",
        authors="Ricci, F., Rokach, L., & Shapira, B. (Eds.)", year=2015,
        publisher="New York: Springer", doi=None, url=None, language="en", isbn=None,
        citation="Ricci, F., Rokach, L., & Shapira, B. (Eds.). (2015). Recommender systems handbook (2nd ed.). Springer.",
        locator="whole work", locator_type="work", supports="evolution / evaluation and beyond-accuracy objectives", verified=False),
 ],
 "MC-269": [
   dict(kind="BOOK", title_en="Competing Against Luck: The Story of Innovation and Customer Choice",
        title_fa="رقابت با شانس: داستان نوآوری و انتخاب مشتری",
        authors="Christensen, C. M., Hall, T., Dillon, K., & Duncan, D. S.", year=2016,
        publisher="New York: HarperBusiness", doi=None,
        url="https://www.christenseninstitute.org/book/competing-against-luck/",
        language="en", isbn=None,
        citation="Christensen, C. M., Hall, T., Dillon, K., & Duncan, D. S. (2016). Competing against luck: The story of innovation and customer choice. HarperBusiness.",
        locator="whole work", locator_type="work", supports="definition / job as unit of analysis / hire metaphor", verified=True),
   dict(kind="JOURNAL_ARTICLE", title_en="Marketing Malpractice: The Cause and the Cure",
        title_fa="قصور بازاریابی: علت و درمان",
        authors="Christensen, C. M., Cook, S., & Hall, T.", year=2005,
        publisher="Harvard Business Review, 83(12), 74-83", doi=None, url=None, language="en", isbn=None,
        citation="Christensen, C. M., Cook, S., & Hall, T. (2005). Marketing malpractice: The cause and the cure. Harvard Business Review, 83(12), 74-83.",
        locator="pp. 74-83", locator_type="page_range", supports="evolution / early jobs-based segmentation", verified=False),
 ],
}

ENRICH = {
 "MC-263": {
   "summary": "«ارزش طول عمر مشتری» (Customer Lifetime Value) برآورد ارزش اقتصادی حال‌شدهٔ جریان سود آتی یک مشتری در طول رابطه‌اش با شرکت است و مشتری را به‌جای هزینه‌ای گذرا، دارایی‌ای در ترازنامهٔ بازاریابی می‌بیند. سونیل گوپتا، دونالد لمن و جنیفر استوارت در «Valuing Customers» (۲۰۰۴، Journal of Marketing Research) نشان دادند ارزش‌گذاری مشتری امکان مقایسهٔ عقلانی هزینهٔ جذب، بودجهٔ نگهداشت و سرمایه‌گذاری در محتوا را فراهم می‌کند (Gupta, Lehmann & Stuart, 2004).",
   "definition": "ارزش طول عمر مشتری مجموع سودهای آتی مورد انتظار از یک مشتری است که با نرخ تنزیل به زمان حال برگردانده می‌شود؛ به بیان ساده، ارزش حال خالص رابطهٔ مشتری با شرکت (Gupta, Lehmann & Stuart, 2004).",
   "main_problem": "شرکت چگونه می‌تواند مشتریان را مانند دارایی ارزش‌گذاری کند و تصمیم‌های بازاریابی — از هزینهٔ جذب تا بودجهٔ نگهداشت و سرمایه‌گذاری در محتوا — را بر پایهٔ ارزش بلندمدت، نه فروش کوتاه‌مدت، بگیرد؟",
   "mechanism": "مدل بر سه سازوکار بنا شده است. (۱) ساختار جریان نقدی تنزیل‌شده: ارزش مشتری برابر است با مجموع حاشیهٔ سود هر دوره ضرب‌در احتمال باقی‌ماندن مشتری، تقسیم‌شده بر ضریب تنزیل؛ در ساده‌ترین شکل، ارزش برابر است با حاشیهٔ سود ضرب‌در نسبت نگهداشت تقسیم بر (نرخ تنزیل + نرخ ریزش) (Gupta, Lehmann & Stuart, 2004). این صورت‌بندی نشان می‌دهد که افزایش نرخ نگهداشت، اثری چندبرابری بر ارزش دارد، زیرا هم احتمال دریافت سود دوره‌های بعد را بالا می‌برد و هم افق زمانی رابطه را طولانی می‌کند. (۲) ارزش پایهٔ مشتری (customer equity): ارزش کل شرکت برابر مجموع ارزش عمر همهٔ مشتریان کنونی و آتی است؛ ازاین‌رو گوپتا و همکاران استدلال می‌کنند که ارزش شرکت را می‌توان از پایهٔ مشتری آن بازسازی کرد و میان ارزش بازار و ارزش پایهٔ مشتری همبستگی بالایی یافتند. (۳) هم‌سنجی جذب و نگهداشت: چون هزینهٔ جذب مشتری نو در مقایسه با هزینهٔ نگهداشت بالا است و نرخ نگهداشت بر ارزش عمر اثری چندبرابری دارد، مدل تخصیص بودجه را به سمت نگهداشت و افزایش «سهم مشتری از سبد» سوق می‌دهد. در بستر رسانه، این چارچوب به منطق اقتصادی اشتراک دیجیتال ترجمه می‌شود: پلتفرم ویدئو یا روزنامهٔ اشتراکی می‌تواند هزینهٔ تبلیغات جذب را با ارزش پیش‌بینی‌شدهٔ مشتری مقایسه کند، «دورهٔ بازگشت هزینهٔ جذب» را محاسبه کند و بفهمد که کاهش نرخ ریزش یک درصد، بیش از یک کمپین تبلیغاتی پرهزینه ارزش می‌آفریند.",
   "assumptions": [
     "رفتار مشتری در آینده با الگوهای گذشتهٔ او قابل پیش‌بینی است.",
     "نرخ نگهداشت و حاشیهٔ سود را می‌توان برای گروه‌های مشتری به‌طور پایدار برآورد کرد.",
     "نرخ تنزیل مناسب را می‌توان تعیین کرد و جریان نقدی آتی را به ارزش حال تبدیل کرد."
   ],
   "principles": [
     "مشتری دارایی است، نه هزینهٔ جاری.",
     "ارزش عمر = مجموع جریان سود تنزیل‌شدهٔ رابطه.",
     "نرخ نگهداشت اثری چندبرابری بر ارزش دارد، پس نگهداشت بر جذب مقدم است."
   ],
   "critiques": [
     "حساسیت به نرخ تنزیل: تغییر کوچک در نرخ تنزیل یا افق زمانی، برآورد ارزش را به‌شدت جابه‌جا می‌کند.",
     "درون‌زایی: کمپین‌های نگهداشت هم بر ریزش اثر می‌گذارند و هم بر حاشیهٔ سود؛ فرض ثبات این متغیرها سست است.",
     "همگن‌سازی: مدل‌های ساده مشتریان را یکسان می‌گیرند، در حالی که ناهمگنی شدید ارزش مشتری، میانگین را گمراه‌کننده می‌کند."
   ],
   "applications": [
     "ارزیابی بازده هزینهٔ جذب مشترک در سرویس‌های اشتراکی ویدئو و خبر.",
     "اولویت‌بندی بودجهٔ نگهداشت در برابر تخفیف جذب در رسانه‌های اشتراکی.",
     "ارزش‌گذاری رسانه بر پایهٔ پایهٔ مشتری برای مذاکرهٔ سرمایه‌گذاری.",
     "طراحی مدل درآمد ترکیبی تبلیغات و اشتراک با سنجش ارزش هر بخش."
   ],
   "evolution": "ریشهٔ مفهوم در بازاریابی پایگاه دادهٔ دههٔ ۱۹۹۰ است؛ گوپتا، لمن و استوارت (۲۰۰۴) آن را به چارچوب ارزش‌گذاری شرکت و ارزش پایهٔ مشتری گره زدند. در دههٔ ۲۰۱۰ مدل‌های احتمالی پایهٔ مشتری (Fader & Hardie, 2009) و در دههٔ ۲۰۲۰ مدل‌های یادگیری ماشین برای پیش‌بینی ریزش، دقت برآورد را بالا بردند.",
   "key_concepts": ["ارزش طول عمر مشتری (customer lifetime value)", "ارزش پایهٔ مشتری (customer equity)", "نرخ نگهداشت (retention rate)", "هزینهٔ جذب مشتری (customer acquisition cost)", "نرخ ریزش (churn rate)", "دورهٔ بازگشت هزینهٔ جذب (CAC payback)"],
   "studies": ["Gupta, S., Lehmann, D. R., & Stuart, J. A. (2004). Valuing customers. Journal of Marketing Research, 41(1), 7-18.", "Fader, P. S., & Hardie, B. G. S. (2009). Probability models for customer-base analysis. Journal of Interactive Marketing, 23(1), 61-69."],
   "detailed_analysis": "۱. بنیان و منطق نظری\nارزش طول عمر مشتری، بازاریابی را از منطق «معامله» به منطق «رابطه» منتقل می‌کند. در منطق معامله، سود هر فروش سنجهٔ موفقیت است؛ در منطق رابطه، هزینهٔ جذب سرمایه‌گذاری اولیه‌ای است که باید در طول سال‌ها بازگردد. همین جابه‌جایی، معیار تصمیم را از فروش دورهٔ جاری به ارزش حال جریان‌های آینده تغییر می‌دهد.\n\n۲. پیوند با ارزش شرکت\nگوپتا، لمن و استوارت (۲۰۰۴) استدلال می‌کنند که مشتریان، دارایی اصلی شرکت‌های خدماتی‌اند و ارزش پایهٔ مشتری می‌تواند بخش زیادی از ارزش بازار شرکت را توضیح دهد. این ادعا هم‌زمان روش‌شناختی و مدیریتی است: روش‌شناختی، زیرا ارزش‌گذاری را از ترازنامهٔ حسابداری به مدل‌سازی رفتاری می‌برد؛ مدیریتی، زیرا سرمایه‌گذاری در بازاریابی را به سرمایه‌گذاری در دارایی پیوند می‌زند.\n\n۳. محدودیت‌های عملی\nدقت مدل به کیفیت داده‌های رفتاری، تفکیک مشتریان و پایداری الگوها وابسته است. در بازارهای رسانه‌ای با ریزش فصلی و کمپین‌های متغیر، فرض ثبات نرخ‌ها به‌سختی برقرار می‌شود و برآورد باید با تحلیل حساسیت همراه شود."
 },
 "MC-266": {
   "summary": "«هزینهٔ جابه‌جایی و قفل‌شدگی مشتری» (Switching Costs and Customer Lock-in) توضیح می‌دهد چرا مشتری حتی با وجود گزینهٔ بهتر، به محصول فعلی وفادار می‌ماند: هزینهٔ مالی، زمانی، یادگیری، داده‌ای یا روانیِ تغییر، او را در جای خود نگه می‌دارد. پل کلمپرر در «Competition when Consumers have Switching Costs» (۱۹۹۵، Review of Economic Studies) نشان داد این هزینه‌ها ساختار رقابت، قیمت‌گذاری و سود صنعت را دگرگون می‌کنند (Klemperer, 1995).",
   "definition": "هزینهٔ جابه‌جایی، مجموع هزینه‌های آشکار و پنهانی است که مشتری برای تغییر از یک عرضه‌کننده به عرضه‌کنندهٔ دیگر متحمل می‌شود؛ قفل‌شدگی وضعیتی است که این هزینه‌ها مشتری را عملاً از تغییر بازمی‌دارند (Klemperer, 1995).",
   "main_problem": "چرا در بسیاری از بازارها، شرکت‌ها ابتدا با قیمت پایین مشتری جذب می‌کنند و سپس قیمت را بالا می‌برند، و چگونه هزینهٔ جابه‌جایی تعادل رقابتی، ورود بنگاه‌های تازه و سود صنعت را تغییر می‌دهد؟",
   "mechanism": "تحلیل در چهار گام پیش می‌رود. (۱) گونه‌شناسی هزینه‌ها: هزینهٔ «معامله‌ای» (هزینهٔ مالی و اداری تغییر)، «یادگیری» (زمان لازم برای تسلط بر محصول تازه)، «سازگاری» (نیاز به خرید تجهیزات یا نرم‌افزار مکمل)، «قراردادی» (جریمهٔ فسخ و تعهد دوره‌ای)، «عدم قطعیت» (ریسک کیفیت عرضه‌کنندهٔ ناشناس) و «هزینهٔ جست‌وجو» (زمان یافتن جایگزین). (۲) قفل‌شدگی پس از سرمایه‌گذاری: مشتری با ورود، موجودی داده، مهارت یا اعتبار انباشته می‌سازد که با تغییر از دست می‌رود؛ همین «سرمایهٔ خاص رابطه» قدرت چانه‌زنی عرضه‌کننده را پس از جذب بالا می‌برد. (۳) الگوی «ارزان وارد شو، گران بمان»: کلمپرر (۱۹۹۵) نشان می‌دهد بنگاه‌ها برای جذب مشتریان قفل‌نشده قیمت تهاجمی می‌گذارند، زیرا ارزش مشتری آتی از سود دورهٔ نخست بیشتر است؛ در مقابل، مشتریان قفل‌شده قیمت بالاتری می‌پردازند. پیامد، جنگ قیمت در مرحلهٔ ورود و آرامش رقابتی پس از تثبیت سهم بازار است. (۴) اثر بر ورود و رفاه: هزینهٔ جابه‌جایی می‌تواند ورود بنگاه تازه را پرهزینه کند و سود صنعت را بالا ببرد، اما هم‌زمان می‌تواند کارایی را کاهش دهد، زیرا مشتری در گزینهٔ نامناسب می‌ماند. در بستر رسانه، قفل‌شدگی در تاریخ تماشا و فهرست پخش، کتابخانهٔ موسیقی، آرشیو نشان‌شدهٔ خبر و شبکهٔ اجتماعی دوستان تجسم می‌یابد؛ تفاوت مهم این است که بخشی از این دارایی، «دادهٔ رفتاری» است و به همین دلیل قواعد «قابلیت حمل داده» در مقررات جدید، قفل‌شدگی را هدف گرفته‌اند.",
   "assumptions": [
     "مشتریان از وجود و اندازهٔ هزینهٔ جابه‌جایی آگاه‌اند و در تصمیم خود آن را می‌سنجند.",
     "هزینهٔ جابه‌جایی را می‌توان با نوع محصول و سرمایه‌گذاری مشتری مرتبط دانست.",
     "ساختار بازار را می‌توان از طریق این هزینه‌ها و نه فقط سهم بازار توضیح داد."
   ],
   "principles": [
     "هزینهٔ جابه‌جایی، تقاضا را به عرضه‌کنندهٔ فعلی گره می‌زند.",
     "قیمت پایین ورودی و قیمت بالای پس از قفل‌شدگی، الگوی رایج این بازارهاست.",
     "هزینهٔ جابه‌جایی می‌تواند هم‌زمان سود و ناکارایی را افزایش دهد."
   ],
   "critiques": [
     "اندازه‌گیری تجربی هزینهٔ جابه‌جایی دشوار است و بیشتر مدل‌ها نظری و مبتنی بر فروض ساده‌اند.",
     "قواعد قابلیت حمل داده، مانند مادهٔ ۲۰ مقررات عمومی حفاظت از داده اروپا، بخشی از قفل‌شدگی دیجیتال را کم‌اثر می‌کند.",
     "در پلتفرم‌های دوطرفه، قفل‌شدگی یک طرف به اثر شبکه‌ای وابسته است و تحلیل تک‌طرفه ناقص می‌ماند."
   ],
   "applications": [
     "تحلیل ریزش و قیمت‌گذاری در سرویس‌های اشتراکی ویدئو و موسیقی.",
     "طراحی قابلیت انتقال فهرست پخش و تاریخ تماشا برای جذب مشتری از رقیب.",
     "ارزیابی قدرت قیمت‌گذاری رسانه‌های مبتنی بر اشتراک با پایهٔ کاربری قفل‌شده.",
     "تحلیل اثر مقررات قابلیت حمل داده بر رقابت در بازارهای دیجیتال."
   ],
   "evolution": "کلمپرر در دههٔ ۱۹۸۰ مدل‌های رقابت با هزینهٔ جابه‌جایی را صورت‌بندی کرد و در ۱۹۹۵ مرور جامع آن را منتشر کرد؛ برنهام، فرلز و مهاجان (۲۰۰۳) گونه‌شناسی رفتارمصرف‌کننده را افزودند. در اقتصاد دیجیتال، بحث از قفل‌شدگی قراردادی به قفل‌شدگی داده و الگوریتمی منتقل شده و مقررات قابلیت حمل داده به‌عنوان پاسخ سیاستی مطرح است.",
   "key_concepts": ["هزینهٔ جابه‌جایی (switching cost)", "قفل‌شدگی مشتری (customer lock-in)", "سرمایهٔ خاص رابطه (relationship-specific investment)", "قیمت‌گذاری نفوذی (penetration pricing)", "قابلیت حمل داده (data portability)", "هزینهٔ جست‌وجو (search cost)"],
   "studies": ["Klemperer, P. (1995). Competition when consumers have switching costs. The Review of Economic Studies, 62(4), 515-539.", "Burnham, T. A., Frels, J. K., & Mahajan, V. (2003). Consumer switching costs. Journal of the Academy of Marketing Science, 31(2), 109-126."],
   "detailed_analysis": "۱. بنیان و منطق نظری\nاقتصاد صنعتی متعارف فرض می‌کند مشتری بی‌هزینه میان عرضه‌کنندگان جابه‌جا می‌شود. کلمپرر (۱۹۹۵) این فرض را کنار می‌گذارد و نشان می‌دهد که حتی هزینهٔ کوچک جابه‌جایی می‌تواند تعادل بازار را کیفی تغییر دهد: بنگاه‌ها ابتدا برای «خرید» سهم بازار رقابت می‌کنند و سپس از مشتریان قفل‌شده بهره می‌برند.\n\n۲. سازوکار قدرت بازار\nوقتی مشتری سرمایه‌گذاری خاصی در رابطه انجام داده است، عرضه‌کننده می‌داند که افزایش قیمت تا آستانهٔ هزینهٔ جابه‌جایی، مشتری را فراری نمی‌دهد. این «قدرت بازار پس از معامله» به بنگاه اجازه می‌دهد سود دوره‌های بعد را افزایش دهد و همین انتظار، انگیزهٔ قیمت‌گذاری تهاجمی در دورهٔ نخست را می‌سازد.\n\n۳. تبعات رفاهی و سیاستی\nهزینهٔ جابه‌جایی لزوماً بد نیست؛ می‌تواند سرمایه‌گذاری در رابطه و کیفیت را تشویق کند. اما وقتی از حد می‌گذرد، مشتری در گزینهٔ نامناسب می‌ماند و ورود نوآوری کند می‌شود. سیاست رقابتی مدرن، ازاین‌رو بر کاهش هزینه‌های ساختگی جابه‌جایی و تضمین انتقال داده متمرکز شده است."
 },
 "MC-268": {
   "summary": "«سامانهٔ توصیه‌گر و ریزش در ویدئوی درخواستی» به کارکرد دوگانهٔ الگوریتم‌های توصیه در پلتفرم‌های استریم اشاره دارد: کاهش هزینهٔ انتخاب برای کاربر و تبدیل شدن به ابزار نگهداشت برای کسب‌وکار. کارلوس گومز-اوریبه و نیل هانت در «The Netflix Recommender System» (۲۰۱۵، ACM Transactions on Management Information Systems) الگوریتم‌ها، ارزش تجاری و نوآوری این سامانه را از منظر درونی شرکت توصیف کردند (Gomez-Uribe & Hunt, 2015).",
   "definition": "توصیه‌گر سامانه‌ای است که با ترکیب سیگنال‌های رفتاری کاربر و ویژگی‌های محتوا، مجموعه‌ای شخصی‌شده و رتبه‌بندی‌شده از گزینه‌ها را در لحظهٔ انتخاب عرضه می‌کند تا احتمال یافتن محتوای رضایت‌بخش افزایش یابد (Gomez-Uribe & Hunt, 2015).",
   "main_problem": "در کاتالوگی با هزاران عنوان، کاربر چگونه محتوای مناسب خود را می‌یابد، و پلتفرم چگونه می‌تواند با کاهش هزینهٔ انتخاب، ساعت تماشا و در نتیجه احتمال تمدید اشتراک را بالا ببرد؟",
   "mechanism": "زنجیرهٔ اثر چهار حلقه دارد. (۱) کاهش هزینهٔ انتخاب: با رشد کاتالوگ، هزینهٔ جست‌وجو و «اضافه‌بار انتخاب» افزایش می‌یابد؛ توصیه‌گر با رتبه‌بندی شخصی‌شدهٔ صفحهٔ اصلی، فاصلهٔ میان کاربر و محتوای مناسب را کوتاه می‌کند. (۲) یادگیری از سیگنال‌های رفتاری: پلتفرم از تماشا، تکمیل، رهاکردن، امتیاز و زمان روز، ترجیحات را استنتاج می‌کند و الگوریتم‌های رتبه‌بندی و شباهت کاربران را به‌طور پیوسته به‌روز می‌کند. گومز-اوریبه و هانت (۲۰۱۵) توصیف می‌کنند که سامانه از ترکیبی از مدل‌های رتبه‌بندی شخصی، محبوبیت و تنوع استفاده می‌کند و ارزش هر جزء با آزمایش‌های کنترل‌شده سنجیده می‌شود. (۳) پیوند با نگهداشت: ارزش تجاری توصیه در نهایت به «ساعت تماشا» و «رضایت جلسهٔ تماشا» ترجمه می‌شود؛ افزایش تعامل، احتمال تمدید اشتراک را بالا می‌برد و ریزش را کاهش می‌دهد. بر پایهٔ گزارش خود شرکت، سهم بزرگی از ساعت‌های تماشا از طریق توصیه‌ها شکل می‌گیرد. (۴) بازخورد پیوسته: هر تعامل داده تولید می‌کند و مدل را دقیق‌تر می‌کند؛ همین حلقهٔ بازخورد، توصیه‌گر را از فهرست ویرایشی ثابت متمایز می‌سازد. در بستر رسانه، این سازوکار توضیح می‌دهد چرا پلتفرم‌های استریم توصیه را نه ویژگی رفاهی، بلکه زیرساخت اقتصادی می‌بینند: کاهش زمان «گشتن بی‌نتیجه»، مستقیماً به کاهش ریزش و افزایش ارزش عمر مشتری ترجمه می‌شود.",
   "assumptions": [
     "رفتار تماشای گذشته، پیش‌بینی‌کنندهٔ معتبر ترجیح آیندهٔ کاربر است.",
     "افزایش تعامل و ساعت تماشا با رضایت و کاهش ریزش رابطهٔ مثبت دارد.",
     "اثر توصیه را می‌توان با آزمایش کنترل‌شده از اثر محتوا تفکیک کرد."
   ],
   "principles": [
     "کاهش هزینهٔ انتخاب، کارکرد اصلی توصیه‌گر است.",
     "توصیه، ابزار نگهداشت است، نه فقط ویژگی کاربرپسند.",
     "ارزش هر جزء الگوریتم با آزمایش کنترل‌شده سنجیده می‌شود."
   ],
   "critiques": [
     "داده‌های ارزش تجاری عمدتاً از گزارش خود شرکت می‌آید و استقلال پژوهشی محدودی دارد.",
     "حباب فیلتر و کاهش تنوع مواجهه، پیامد احتمالی بهینه‌سازی برای تعامل است.",
     "تفکیک اثر توصیه از کیفیت خود محتوا و از فصل‌بندی انتشار، در عمل دشوار است."
   ],
   "applications": [
     "طراحی صفحهٔ اصلی و رتبه‌بندی کاتالوگ در سرویس‌های ویدئوی درخواستی.",
     "مدل‌سازی ریزش و سنجش اثر توصیه بر تمدید اشتراک.",
     "تحلیل تنوع مواجهه و پیامدهای حباب فیلتر در رسانه.",
     "به‌کارگیری منطق توصیه در خبر، موسیقی و کتاب صوتی."
   ],
   "evolution": "پیشینهٔ توصیه‌گر به پالایش مشارکتی دههٔ ۱۹۹۰ بازمی‌گردد؛ نتفلیکس با مسابقهٔ جایزهٔ ۲۰۰۶ و سپس سامانهٔ تولیدی خود، پژوهش را به عمل صنعتی پیوند زد. گومز-اوریبه و هانت (۲۰۱۵) منطق تجاری را مستند کردند و پس از آن، پژوهش‌های عدالت الگوریتمی و تنوع، پرسش‌های کیفیت مواجهه را به مرکز آوردند.",
   "key_concepts": ["توصیه‌گر (recommender system)", "پالایش مشارکتی (collaborative filtering)", "هزینهٔ انتخاب (choice cost)", "ریزش (churn)", "حباب فیلتر (filter bubble)", "آزمایش کنترل‌شده (A/B testing)"],
   "studies": ["Gomez-Uribe, C. A., & Hunt, N. (2015). The Netflix recommender system. ACM Transactions on Management Information Systems, 6(4), Article 13.", "Ricci, F., Rokach, L., & Shapira, B. (Eds.). (2015). Recommender Systems Handbook (2nd ed.). Springer."],
   "detailed_analysis": "۱. بنیان و منطق نظری\nتوصیه‌گر پاسخی فنی به یک مسئلهٔ اقتصادی است: در اقتصاد فراوانی محتوا، کمیابی از تولید به توجه و انتخاب منتقل شده است. وقتی کاتالوگ از توان مرور کاربر فراتر می‌رود، هزینهٔ یافتن گزینهٔ مناسب به‌اندازه‌ای بالا می‌رود که تجربهٔ مصرف را تهدید می‌کند.\n\n۲. از تعامل به نگهداشت\nپلتفرم‌های اشتراکی درآمد را از تمدید می‌گیرند، نه از هر تماشا. بنابراین سنجهٔ میانی «ساعت تماشا» تنها تا جایی معنا دارد که به رضایت و تمدید بینجامد؛ بهینه‌سازی صرف بر زمان می‌تواند به محتوای اعتیادآور و کاهش رضایت بلندمدت بیانجامد.\n\n۳. مسئلهٔ سنجش\nاثر توصیه در محیط تولیدی به‌سختی از اثر محتوا جدا می‌شود. راه‌حل صنعتی، آزمایش‌های کنترل‌شده و آزمون‌های بلندمدت است؛ اما همین وابستگی به سنجه‌های درونی، شفافیت بیرونی را کاهش می‌دهد و نقد مستقل را دشوار می‌کند."
 },
 "MC-269": {
   "summary": "«کار مشتری‌محور» (Jobs-to-be-Done) نظریه‌ای در نوآوری است که می‌گوید مشتریان محصول نمی‌خرند، بلکه آن را برای انجام «کاری» در موقعیتی مشخص «استخدام» می‌کنند. کلیتون کریستنسن، تدی هال، کارن دیلون و دیوید دانکن در «Competing Against Luck» (۲۰۱۶، HarperBusiness) این چارچوب را به‌عنوان توضیح علّی موفقیت و شکست نوآوری صورت‌بندی کردند (Christensen et al., 2016).",
   "definition": "کار (job) پیشرفتی است که مشتری در یک موقعیت مشخص می‌کوشد به آن برسد؛ محصول یا خدمت، ابزاری است که برای رسیدن به این پیشرفت استخدام می‌شود (Christensen et al., 2016).",
   "main_problem": "چرا نوآوری‌های پرهزینه شکست می‌خورند و برخی محصولات ساده بازار را تسخیر می‌کنند؟ اگر دسته‌بندی صنعتی و ویژگی‌های جمعیت‌شناختی، رفتار انتخاب را توضیح نمی‌دهد، واحد تحلیل درست برای نوآوری چیست؟",
   "mechanism": "چارچوب سه لایهٔ تحلیلی دارد. (۱) کار، نه محصول: مشتری در موقعیتی مشخص می‌کوشد پیشرفتی حاصل کند و محصول را برای این پیشرفت استخدام می‌کند؛ اگر محصول در انجام کار ناکام بماند، رها می‌شود، هرچند از نظر فنی بی‌عیب باشد. کریستنسن و همکاران (۲۰۱۶) نمونهٔ معروف میلک‌شیک را نقل می‌کنند: بخش بزرگی از خریداران صبحگاهی، آن را برای «سرگرم‌کردن خود در مسیر کار و سیر ماندن تا ظهر» می‌خریدند؛ نه به‌عنوان نوشیدنی دسر. (۲) سه بُعد کار: هر کار هم‌زمان «کارکردی» (انجام وظیفه)، «احساسی» (چگونه می‌خواهم احساس کنم) و «اجتماعی» (چگونه دیده می‌شوم) دارد؛ نوآوری موفق هر سه را هدف می‌گیرد. (۳) بازتعریف رقابت: رقبای یک محصول، همهٔ راه‌حل‌هایی‌اند که مشتری برای همان کار استخدام می‌کند، حتی اگر در صنعت دیگری باشند. ازاین‌رو تحلیل رقابت باید از مرزهای صنعتی فراتر رود و «مجموعهٔ گزینه‌های واقعی مشتری» را ببیند. (۴) پیامد روش‌شناختی: پژوهش بازار از پرسش دربارهٔ ویژگی‌های مطلوب به مشاهدهٔ موقعیت، انگیزه و معیارهای انتخاب در لحظهٔ واقعی تغییر می‌کند. در بستر رسانه، این چارچوب پرسش «چه نوع محتوایی می‌خواهید؟» را به «مخاطب در چه موقعیتی و برای چه پیشرفتی رسانه را انتخاب می‌کند؟» تبدیل می‌کند؛ پادکستی که برای «کاهش بی‌حوصلگی در مسیر رفت‌وآمد» استخدام می‌شود، رقیبش نه پادکست دیگر، بلکه موسیقی، شبکهٔ اجتماعی و سکوت است. همین نگاه، طراحی محصول رسانه‌ای و بسته‌بندی خبر را به سمت «موقعیت مصرف» می‌برد.",
   "assumptions": [
     "مشتری در انتخاب محصول، منطق ابزاری و هدف‌محور دارد.",
     "کار را می‌توان از موقعیت و انگیزهٔ مشتری استنتاج کرد.",
     "موفقیت نوآوری به توان انجام کار وابسته است، نه به ویژگی‌های فنی به‌تنهایی."
   ],
   "principles": [
     "واحد تحلیل، کار است نه مشتری یا محصول.",
     "هر کار سه بُعد کارکردی، احساسی و اجتماعی دارد.",
     "رقابت را مجموعهٔ راه‌حل‌های همان کار تعریف می‌کند، نه صنعت."
   ],
   "critiques": [
     "تعریف کار مبهم است و مرز «کار» با «نیاز» یا «هدف» روشن نیست؛ همین ابهام، اعتبارسنجی را دشوار می‌کند.",
     "شواهد چارچوب بیشتر مطالعهٔ موردی و پس‌نگر است و توان پیش‌بینی آن کمتر از توصیف آن است.",
     "مقیاس‌پذیری تحلیل کیفی کار برای بازارهای بزرگ، پرهزینه و وابسته به تفسیر پژوهشگر است."
   ],
   "applications": [
     "طراحی محصول رسانه‌ای بر پایهٔ موقعیت مصرف مخاطب.",
     "بسته‌بندی خبر و محتوا برای کارهای مشخص مانند به‌روز شدن در مسیر کار.",
     "تحلیل رقابت رسانه‌ای فراتر از مرزهای صنعتی.",
     "بازطراحی فرایند پژوهش مخاطب با تمرکز بر انگیزه و لحظهٔ انتخاب."
   ],
   "evolution": "ریشهٔ چارچوب در مقالهٔ «Marketing Malpractice» (Christensen, Cook & Hall, 2005) و پژوهش‌های کریستنسن دربارهٔ نوآوری مخرب است. کتاب ۲۰۱۶ آن را به نظریه‌ای مستقل با زبان «استخدام» و «پیشرفت» تبدیل کرد و در دههٔ ۲۰۲۰ به ابزار رایج طراحی محصول و پژوهش کاربر تبدیل شد.",
   "key_concepts": ["کار (job)", "استخدام محصول (hiring a product)", "پیشرفت (progress)", "بُعد کارکردی/احساسی/اجتماعی (functional/emotional/social)", "موقعیت مصرف (consumption situation)", "نظریهٔ کار (jobs theory)"],
   "studies": ["Christensen, C. M., Hall, T., Dillon, K., & Duncan, D. S. (2016). Competing Against Luck. HarperBusiness.", "Christensen, C. M., Cook, S., & Hall, T. (2005). Marketing malpractice: The cause and the cure. Harvard Business Review, 83(12), 74-83."],
   "detailed_analysis": "۱. بنیان و منطق نظری\nنظریهٔ کار در واکنش به ناکامی مدل‌های سنتی بخش‌بندی بازار شکل گرفت. بخش‌بندی بر پایهٔ جمعیت‌شناسی یا نگرش، همبستگی‌هایی می‌سازد که رفتار واقعی انتخاب را توضیح نمی‌دهند؛ دو مشتری با پروفایل یکسان می‌توانند محصول را به دو دلیل کاملاً متفاوت بخرند. چارچوب کار، توضیح را از «چه کسی» به «چرا در این موقعیت» منتقل می‌کند.\n\n۲. منطق علّی\nادعای اصلی این است که کار، علت انتخاب است و بنابراین باید واحد تحلیل نوآوری باشد. اگر شرکت کار را درست تشخیص دهد، ویژگی‌ها، قیمت و کانال توزیع از دل آن استنتاج می‌شوند، نه از نظرسنجی دربارهٔ ترجیحات انتزاعی.\n\n۳. محدودیت‌ها\nکار یک سازهٔ تفسیری است و تشخیص آن به مصاحبهٔ عمیق و مشاهدهٔ موقعیت وابسته است. همین وابستگی، هم غنای تحلیلی می‌آفریند و هم خطر سوگیری پس‌نگر را بالا می‌برد؛ بسیاری از روایت‌های موفقیت، کار را پس از موفقیت بازسازی می‌کنند."
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
    codes = ["MC-263", "MC-266", "MC-268", "MC-269"]
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
    print("BATCH56 THEORY DONE")

if __name__ == "__main__":
    main()
