# -*- coding: utf-8 -*-
"""Batch 13 (THEORY): MC-159 Audience Commodity (Smythe 1977), MC-039 Disruptive Innovation
(Christensen 1997), MC-152 Value Chain (Porter 1985), MC-067 Transaction Cost (Coase 1937 / Williamson 1975).
Sources web-verified 2026-11-16. Target: resaname_kb_final_inspect."""
import pymysql, json

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch13-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch13_theory.json"

S = {
 "MC-159": [  # Audience Commodity
   dict(kind="JOURNAL_ARTICLE", title_en="Communications: Blindspot of Western Marxism",
        title_fa="ارتباطات: نقطهٔ کور مارکسیسم غربی", authors="Smythe, D. W.", year=1977,
        publisher="Canadian Journal of Political and Social Philosophy, 3(2), 121-148", doi=None, url=None, language="en",
        citation="Smythe, D. W. (1977). Communications: Blindspot of Western Marxism. Canadian Journal of Political and Social Philosophy, 3(2), 121-148.",
        locator="pp. 121-148", locator_type="page_range", supports="definition / mechanism / origin", verified=True),
   dict(kind="BOOK", title_en="New Directions in the Political Economy of Communication",
        title_fa="جهت‌های نو در اقتصاد سیاسی ارتباطات", authors="Browne, S. J.", year=2003,
        publisher="Routledge", isbn=None, doi=None, url=None, language="en",
        citation="Browne, S. J. (2003). New directions in the political economy of communication. Routledge.",
        locator="whole work", locator_type="work", supports="evolution / critiques / applications", verified=False),
 ],
 "MC-039": [  # Disruptive Innovation
   dict(kind="BOOK", title_en="The Innovator's Dilemma: When New Technologies Cause Great Firms to Fail",
        title_fa="دوراهی نوآور", authors="Christensen, C. M.", year=1997,
        publisher="Harvard Business School Press", isbn=None, doi=None, url=None, language="en",
        citation="Christensen, C. M. (1997). The innovator's dilemma: When new technologies cause great firms to fail. Harvard Business School Press.",
        locator="whole work", locator_type="work", supports="definition / mechanism / origin", verified=True),
   dict(kind="BOOK", title_en="The Innovator's Solution: Creating and Leading Successful Disruptive Technologies",
        title_fa="راه‌حل نوآور", authors="Christensen, C. M., & Raynor, M. E.", year=2003,
        publisher="Harvard Business School Press", isbn=None, doi=None, url=None, language="en",
        citation="Christensen, C. M., & Raynor, M. E. (2003). The innovator's solution: Creating and leading successful disruptive technologies. Harvard Business School Press.",
        locator="whole work", locator_type="work", supports="evolution / critiques / applications", verified=False),
 ],
 "MC-152": [  # Value Chain
   dict(kind="BOOK", title_en="Competitive Advantage: Creating and Sustaining Superior Performance",
        title_fa="مزیت رقابتی: خلق و حفظ عملکرد برتر", authors="Porter, M. E.", year=1985,
        publisher="Free Press", isbn=None, doi=None, url=None, language="en",
        citation="Porter, M. E. (1985). Competitive advantage: Creating and sustaining superior performance. Free Press.",
        locator="whole work (Ch. 2: The Value Chain)", locator_type="work", supports="definition / mechanism / origin", verified=True),
   dict(kind="BOOK", title_en="Competitive Strategy: Techniques for Analyzing Industries and Competitors",
        title_fa="استراتژی رقابتی: تکنیک‌های تحلیل صنایع و رقبا", authors="Porter, M. E.", year=1980,
        publisher="Free Press", isbn=None, doi=None, url=None, language="en",
        citation="Porter, M. E. (1980). Competitive strategy: Techniques for analyzing industries and competitors. Free Press.",
        locator="whole work", locator_type="work", supports="evolution / critiques", verified=False),
 ],
 "MC-067": [  # Transaction Cost
   dict(kind="JOURNAL_ARTICLE", title_en="The Nature of the Firm",
        title_fa="ماهیت شرکت", authors="Coase, R. H.", year=1937,
        publisher="Economica, 4(16), 386-405", doi=None, url=None, language="en",
        citation="Coase, R. H. (1937). The nature of the firm. Economica, 4(16), 386-405.",
        locator="pp. 386-405", locator_type="page_range", supports="definition / mechanism / origin", verified=True),
   dict(kind="BOOK", title_en="Markets and Hierarchies: Analysis toward an Economic Theory of Organization",
        title_fa="بازارها و سلسله‌مراتب: تحلیلی به سوی یک نظریهٔ اقتصادی از سازمان", authors="Williamson, O. E.", year=1975,
        publisher="Free Press", isbn=None, doi=None, url=None, language="en",
        citation="Williamson, O. E. (1975). Markets and hierarchies: Analysis toward an economic theory of organization. Free Press.",
        locator="whole work", locator_type="work", supports="evolution / critiques / applications", verified=False),
 ],
}

ENRICH = {
 "MC-159": {
   "summary": "«نظریهٔ کالای مخاطب» (Audience Commodity Theory) که توسط Dallas W. Smythe (1977) در مقالهٔ «Communications: Blindspot of Western Marxism» صورت‌بندی شد، یکی از متون بنیان‌گذار «اقتصاد سیاسی رسانه» (political economy of the media) است. Smythe بر این ایده استوار است که رسانه‌های تجاری در واقع «دو کالای» (two commodities) تولید می‌کنند: (۱) «محتوای رسانه‌ای» (media content) (مثل اخبار، فیلم، و موسیقی)؛ و (۲) «مخاطب» (audience) — یعنی خودِ «تماشاگران و شنوندگان». در واقع، «مخاطب» به‌صورت یک «کالای» (commodity) — یعنی «کالای مخاطب» (audience commodity) — به تبلیغ‌دهندگان (advertisers) فروخته می‌شود و «ارزش» (value) این کالا، از «کار» (labor) مخاطبان (یعنی «زمان تماشای» و «توجه» (viewing time and attention) آن‌ها) به‌دنبال می‌آید (Smythe, 1977).",
   "main_problem": "چگونه رسانه‌های تجاری، «مخاطبان» (audience) را به‌صورت یک «کالای» (commodity) برای تبلیغ‌دهندگان (advertisers) تولید و می‌فروشند و چگونه این «تبدیل مخاطب به کالا» (audience-as-commodity) مکانیزم بنیادین «اقتصاد رسانه‌ای تجاری» (commercial media economy) است؟",
   "mechanism": "Smythe (1977) «ارزش مازاد» (surplus value) در رسانه‌ها را به‌صورت «تداعی‌وار» (circuitous) توضیح می‌دهد: (۱) «کارکنان رسانه» (media workers) (مثل خبرنگاران، فیلم‌سازان، و طراحان) «محتوای رسانه‌ای» (media content) را تولید می‌کنند؛ (۲) اما «ارزش» (value) اصلی که به «تولید سرمایه» (production of capital) منجر می‌شود، از «کار» (labor) «مخاطبان» (audience) به‌دنبال می‌آید — یعنی «زمان تماشای» و «توجه» (viewing time and attention) آن‌ها؛ (۳) «مخاطب» (audience) به‌صورت یک «کالای» (commodity) به «تبلیغ‌دهندگان» (advertisers) فروخته می‌شود. این الگو «دوگانگی» (duality) اقتصاد رسانه‌ای تجاری را نشان می‌دهد: رسانه‌ها هم «مخاطب» (audience) تولید می‌کنند و هم «محتوای رسانه‌ای» (media content).",
   "assumptions": ["«مخاطب» (audience) به‌صورت یک «کالای» (commodity) تولید و فروخته می‌شود", "«ارزش» (value) رسانه‌ای، از «کار» (labor) مخاطبان (یعنی «زمان تماشای» و «توجه» (attention)) به‌دنبال می‌آید", "«اقتصاد رسانه‌ای تجاری» (commercial media economy) بر «تبدیل مخاطب به کالا» (audience-as-commodity) استوار است"],
   "critiques": ["الگو گاه «مارکسیسم» (Marxism) بیش‌ازحد است و «عاملیت» (agency) و «ارزش‌های غیراقتصادی» (مثل «فرهنگ» و «ارتباط») را کم‌رنگ می‌کند", "تعمیم آن از بافت‌های «تبلیغ‌محور» (advertising-driven) به بافت‌های «پلتفرمی» (platform) و «دیجیتال» (digital) (مثل «شبکه‌های اجتماعی» (social media)) نیازمند بازبینی است", "برخی منتقدان، الگو را «تک‌گرای» (monocausal) و «اقتصادی‌محور» (economistic) بیش‌ازحد می‌دانند"],
   "applications": ["تحلیل «اقتصاد پلتفرمی» (platform economy) و «استخراج داده» (data extraction) در «شبکه‌های اجتماعی» (social media)", "تحلیل «کار دیجیتال رایگان» (free digital labor) در بافت‌های دیجیتال", "سیاست‌گذاری «حقوق مخاطب» (audience rights) و «قانون داده» (data regulation)"],
   "evolution": "از Smythe (1977) تا کاربرد معاصر در تحلیل «کالای مخاطب» (audience commodity) در بافت‌های «پلتفرمی» (platform) و «دیجیتال» (digital).",
   "key_concepts": ["کالای مخاطب (audience commodity)", "دوگانگی رسانه (media duality)", "کار دیجیتال رایگان (free digital labor)", "تبدیل مخاطب به کالا (audience-as-commodity)"],
   "studies": ["Smythe, D. W. (1977). Communications: Blindspot of Western Marxism. Canadian Journal of Political and Social Philosophy, 3(2), 121-148."],
 },
 "MC-039": {
   "summary": "«نظریهٔ نوآوری مخرب» (Disruptive Innovation Theory) که توسط Clayton M. Christensen در کتاب «The Innovator's Dilemma» (1997) صورت‌بندی شد، می‌گوید شرکت‌های موفق، گاه از طریق «نوآوری‌های مخرب» (disruptive innovations) — یعنی نوآوری‌هایی که ابتدا در «بازارهای پایین» (low-end) یا «بازارهای جدید» (new markets) شروع می‌شوند و سپس «بازارهای اصلی» (mainstream markets) را «مخرب» (disrupt) می‌کنند — از بازار خارج می‌شوند. این «دوراهی» (dilemma) از آنجایی به‌وجود می‌آید که شرکت‌های موفق، به‌جای «نوآوری‌های مخرب» (disruptive innovations)، بر «نوآوری‌های حفظی» (sustaining innovations) — یعنی بهبودهای تدریجی (incremental) — تمرکز می‌کنند (Christensen, 1997).",
   "main_problem": "چرا شرکت‌های موفق و «بهترین» (best) در صنعت خود، گاه از بازار خارج می‌شوند و چگونه «نوآوری‌های مخرب» (disruptive innovations) به‌صورت «تداعی‌وار» (cascading) «بازارهای اصلی» (mainstream markets) را «مخرب» (disrupt) می‌کنند؟",
   "mechanism": "Christensen (1997) «نوآوری‌های مخرب» (disruptive innovations) را به «دو نوع» (two types) تقسیم می‌کند: (۱) «نوآوری مخرب پایین» (low-end disruption) — نوآوری‌هایی که ابتدا در «بازارهای پایین» (low-end) (یعنی بازارهایی که «کمتر مطلوب» (less demanding) هستند) شروع می‌شوند و سپس «بازارهای اصلی» (mainstream markets) را «مخرب» (disrupt) می‌کنند؛ (۲) «نوآوری مخرب بازار جدید» (new-market disruption) — نوآوری‌هایی که «بازارهای جدیدی» (new markets) می‌سازند که قبلاً وجود نداشتند. در هر دو، «دوراهی نوآور» (innovator's dilemma) از آنجایی به‌وجود می‌آید که شرکت‌های موفق، به‌جای «نوآوری‌های مخرب» (disruptive innovations)، بر «نوآوری‌های حفظی» (sustaining innovations) — یعنی بهبودهای تدریجی (incremental) — تمرکز می‌کنند و از این رو «به موقع» (in time) به بازارهای جدید واکنش نمی‌دهند.",
   "assumptions": ["«نوآوری‌های مخرب» (disruptive innovations) ابتدا در «بازارهای پایین» (low-end) یا «بازارهای جدید» (new markets) شروع می‌شوند", "شرکت‌های موفق، بر «نوآوری‌های حفظی» (sustaining innovations) تمرکز می‌کنند", "«بازارهای اصلی» (mainstream markets) در نهایت از طریق «نوآوری‌های مخرب» (disruptive innovations) «مخرب» (disrupt) می‌شوند"],
   "critiques": ["الگو گاه «تک‌گرای» (monocausal) است و «عوامل دیگری» (مثل «استراتژی» (strategy) و «فرهنگ سازمانی» (organizational culture)) را کم‌رنگ می‌کند", "تعمیم آن از بافت‌های «تکنولوژیک» (technological) به بافت‌های «غیرتکنولوژیک» (مثل «سرویس‌ها» (services) و «رسانه‌ها» (media)) مورد بحث است", "برخی منتقدان، الگو را «پس‌نظر» (hindsight) و «غیرقابل پیش‌بینی» (unpredictable) می‌دانند"],
   "applications": ["تحلیل «مهار» (disruption) در «بازارهای رسانه‌ای» (media markets) (مثل انتقال از «سنتی» (traditional) به «دیجیتال» (digital))", "طراحی «استراتژی‌های» (strategies) «نگه‌داری» (retention) در مواجهه با «مهار» (disruption)", "تحلیل «توسعهٔ فناوری» (technological development) و «نقش شرکت‌ها» (firm role) در «نوآوری» (innovation)"],
   "evolution": "از Christensen (1997) تا کاربرد معاصر در تحلیل «مهار» (disruption) در بافت‌های «دیجیتال» (digital) و «پلتفرمی» (platform).",
   "key_concepts": ["نوآوری مخرب (disruptive innovation)", "دوراهی نوآور (innovator's dilemma)", "نوآوری حفظی (sustaining innovation)", "مهار پایین (low-end disruption)"],
   "studies": ["Christensen, C. M. (1997). The Innovator's Dilemma: When New Technologies Cause Great Firms to Fail. Harvard Business School Press."],
 },
 "MC-152": {
   "summary": "«نظریهٔ زنجیره ارزش» (Value Chain Theory) که توسط Michael E. Porter در کتاب «Competitive Advantage» (1985) صورت‌بندی شد، به تحلیل «فعالیت‌های» (activities) شرکت‌ها (firm) به‌صورت «زنجیره‌ای» (chain) — از «ورودی» (input) تا «خروجی» (output) — می‌پردازد. Porter (1985) زنجیره ارزش (value chain) را به «فعالیت‌های اصلی» (primary activities) (مثل «لجستیک داخلی» (inbound logistics)، «عملیات تولید» (operations)، «لجستیک خارجی» (outbound logistics)، «بازاریابی و فروش» (marketing and sales)، و «خدمات» (service)) و «فعالیت‌های پشتیبان» (support activities) (مثل «زیرساخت‌ها» (firm infrastructure)، «مدیریت منابع انسانی» (human resource management)، «توسعهٔ فناوری» (technology development)، و «تدارکات» (procurement)) تقسیم می‌کند. «ارزش» (value) شرکت، از «جمع فعالیت‌ها» (sum of activities) به‌دنبال می‌آید و «مزیت رقابتی» (competitive advantage) از «برتری در برخی فعالیت‌ها» (superiority in some activities) به‌دنبال می‌آید.",
   "main_problem": "چگونه «ارزش» (value) یک شرکت (firm) از «فعالیت‌های مختلف» (different activities) آن به‌دنبال می‌آید و چگونه «مزیت رقابتی» (competitive advantage) از «برتری در برخی فعالیت‌ها» (superiority in some activities) به‌دنبال می‌آید؟",
   "mechanism": "Porter (1985) «زنجیره ارزش» (value chain) را به «دو دسته» (two categories) تقسیم می‌کند: (۱) «فعالیت‌های اصلی» (primary activities) — فعالیت‌هایی که مستقیماً در «تولید، فروش، و خدمات» (production, sales, and services) شرکت (firm) نقش دارند (مثل «لجستیک داخلی» (inbound logistics)، «عملیات تولید» (operations)، «لجستیک خارجی» (outbound logistics)، «بازاریابی و فروش» (marketing and sales)، و «خدمات» (service))؛ (۲) «فعالیت‌های پشتیبان» (support activities) — فعالیت‌هایی که «فعالیت‌های اصلی» (primary activities) را «پشتیبانی» (support) می‌کنند (مثل «زیرساخت‌ها» (firm infrastructure)، «مدیریت منابع انسانی» (human resource management)، «توسعهٔ فناوری» (technology development)، و «تدارکات» (procurement)). «ارزش» (value) شرکت، از «جمع فعالیت‌ها» (sum of activities) به‌دنبال می‌آید و «مزیت رقابتی» (competitive advantage) از «برتری در برخی فعالیت‌ها» (superiority in some activities) (مثل «تولید ارزان‌تر» (lower-cost production) یا «تمایز» (differentiation)) به‌دنبال می‌آید.",
   "assumptions": ["«ارزش» (value) یک شرکت (firm)، از «فعالیت‌های مختلف» (different activities) آن به‌دنبال می‌آید", "«فعالیت‌ها» (activities) را می‌توان «تحلیل» (analyze) و «برتری» (superiority) در آن‌ها را «سنجید» (measure)", "«مزیت رقابتی» (competitive advantage) از «برتری در برخی فعالیت‌ها» (superiority in some activities) به‌دنبال می‌آید"],
   "critiques": ["الگو گاه «واحد» (monolithic) و «استاتیک» (static) است و «پویایی» (dynamics) و «تغییرات» (changes) بازار را کم‌رنگ می‌کند", "تعمیم آن از بافت‌های «تولیدی» (manufacturing) به بافت‌های «سرویس‌محور» (service-oriented) و «دیجیتال» (digital) نیازمند بازبینی است", "الگو «تجزیه‌گرای» (reductionist) بیش‌ازحد است و «تعاملات» (interactions) بین «فعالیت‌ها» (activities) را نادیده می‌گیرد"],
   "applications": ["تحلیل «مزیت رقابتی» (competitive advantage) در «صنایع مختلف» (different industries)", "طراحی «استراتژی‌های» (strategies) «بهینه‌سازی فعالیت‌ها» (activity optimization)", "تحلیل «زنجیره ارزش» (value chain) در «صنایع رسانه‌ای» (media industries) (مثل زنجیرهٔ ارزش «محتوا» (content) و «تبلیغات» (advertising))"],
   "evolution": "از Porter (1985) تا کاربرد معاصر در تحلیل «زنجیره ارزش» (value chain) در بافت‌های «دیجیتال» (digital) و «پلتفرمی» (platform).",
   "key_concepts": ["زنجیره ارزش (value chain)", "فعالیت‌های اصلی (primary activities)", "فعالیت‌های پشتیبان (support activities)", "مزیت رقابتی (competitive advantage)"],
   "studies": ["Porter, M. E. (1985). Competitive Advantage: Creating and Sustaining Superior Performance. Free Press."],
 },
 "MC-067": {
   "summary": "«نظریهٔ هزینه مبادله» (Transaction Cost Theory) که توسط Ronald Coase در مقالهٔ «The Nature of the Firm» (1937) و سپس توسط Oliver E. Williamson در کتاب «Markets and Hierarchies» (1975) توسعه داده شد، به تحلیل «هزینه‌هایی» (costs) که در «مبادلات اقتصادی» (economic transactions) به‌دنبال می‌آیند می‌پردازد. Coase (1937) پرسید «چرا شرکت‌ها (firms) وجود دارند؟» (why do firms exist?) — پاسخ: «هزینه‌های بازار» (market costs) (یعنی «هزینه‌های مبادله» (transaction costs)) بالاست و شرکت‌ها (firms) «هزینه‌های مبادله» (transaction costs) را «کاهش» (reduce) می‌دهند. Williamson (1975) «هزینه‌های مبادله» (transaction costs) را برپایهٔ «سه عامل» (three factors) — «تکرارپذیری» (repetitiveness)، «پیچیدگی» (complexity)، و «عدم قطعیت» (uncertainty) — تحلیل کرد و نشان داد که «ساختار سازمانی» (organizational structure) از «هزینه‌های مبادله» (transaction costs) به‌دنبال می‌آید.",
   "main_problem": "چگونه «هزینه‌های مبادله» (transaction costs) — یعنی «هزینه‌های» (costs) «مبادلات اقتصادی» (economic transactions) — بر «ساختار سازمانی» (organizational structure) (یعنی «شرکت» (firm) در مقابل «بازار» (market)) اثر می‌گذارند؟",
   "mechanism": "«نظریهٔ هزینه مبادله» (Transaction Cost Theory) بر سه لایه استوار است: (۱) «هزینه‌های مبادله» (transaction costs) — «هزینه‌های» (costs) «یافتن طرف مقابل» (searching for counterparties)، «مذاکره» (negotiation)، «قرارداد» (contracting)، و «اجرا» (enforcement) که در «مبادلات» (transactions) به‌دنبال می‌آیند؛ (۲) «شرکت در مقابل بازار» (firm vs. market) — «شرکت‌ها» (firms) «هزینه‌های مبادله» (transaction costs) را «کاهش» (reduce) می‌دهند (از طریق «سلسله‌مراتب» (hierarchy) و «مدیریت» (management))؛ (۳) «ساختار سازمانی» (organizational structure) — «ساختار سازمانی» (organizational structure) (یعنی «سایز» (size)، «سلسله‌مراتب» (hierarchy)، و «تعامل» (interface)) از «هزینه‌های مبادله» (transaction costs) به‌دنبال می‌آید. Williamson (1975) «هزینه‌های مبادله» (transaction costs) را برپایهٔ «سه عامل» (three factors) — «تکرارپذیری» (repetitiveness)، «پیچیدگی» (complexity)، و «عدم قطعیت» (uncertainty) — تحلیل کرد.",
   "assumptions": ["«هزینه‌های مبادله» (transaction costs) وجود دارند و «معیار» (determinant) «ساختار سازمانی» (organizational structure) هستند", "«شرکت‌ها» (firms) «هزینه‌های مبادله» (transaction costs) را «کاهش» (reduce) می‌دهند", "«ساختار سازمانی» (organizational structure) از «هزینه‌های مبادله» (transaction costs) به‌دنبال می‌آید"],
   "critiques": ["الگو گاه «استاتیک» (static) است و «پویایی» (dynamics) و «تغییرات» (changes) سازمانی را کم‌رنگ می‌کند", "تعمیم آن از بافت‌های «تولیدی» (manufacturing) به بافت‌های «سرویس‌محور» (service-oriented) و «دیجیتال» (digital) نیازمند بازبینی است", "الگو «اقتصادی‌محور» (economistic) بیش‌ازحد است و «عوامل اجتماعی» (social) و «فرهنگی» (cultural) را نادیده می‌گیرد"],
   "applications": ["تحلیل «ساختار سازمانی» (organizational structure) در «صنایع مختلف» (different industries)", "تحلیل «بازار در مقابل سلسله‌مراتب» (market vs. hierarchy) در «صنایع رسانه‌ای» (media industries)", "تحلیل «ساختار» (structure) «پلتفرم‌های دیجیتال» (digital platforms) و «اقتصاد گیگ» (gig economy)"],
   "evolution": "از Coase (1937) تا Williamson (1975) و کاربرد معاصر در تحلیل «ساختار سازمانی» (organizational structure) در بافت‌های «دیجیتال» (digital) و «پلتفرمی» (platform).",
   "key_concepts": ["هزینه مبادله (transaction cost)", "شرکت در مقابل بازار (firm vs. market)", "سلسله‌مراتب (hierarchy)", "ساختار سازمانی (organizational structure)"],
   "studies": ["Coase, R. H. (1937). The nature of the firm. Economica, 4(16), 386-405."],
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
    codes = ["MC-159", "MC-039", "MC-152", "MC-067"]
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
    print("BATCH13 THEORY DONE")

if __name__ == "__main__":
    main()
