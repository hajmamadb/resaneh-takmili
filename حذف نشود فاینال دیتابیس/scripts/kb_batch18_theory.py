# -*- coding: utf-8 -*-
"""Batch 18 (THEORY): MC-381 Two-Sided Market Economics of Media (Rochet & Tirole 2003),
MC-176 Strategic Groups (Porter 1981), MC-223 Datafication and Dataism (Harari 2015),
MC-361 Objectivity as Defensive Ritual (Tuchman 1972). Sources web-verified 2026-11-16.
Target: resaname_kb_final_inspect."""
import pymysql, json

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch18-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch18_theory.json"

S = {
 "MC-381": [  # Two-Sided Market Economics of Media
   dict(kind="JOURNAL_ARTICLE", title_en="Platform Competition in Two-Sided Markets",
        title_fa="رقابت پلتفرمی در بازارهای دوسویه", authors="Rochet, J.-C., & Tirole, J.", year=2003,
        publisher="Journal of the European Economic Association, 1(4), 990-1029",
        doi="10.1162/154247603322493212", url=None, language="en",
        citation="Rochet, J.-C., & Tirole, J. (2003). Platform competition in two-sided markets. The Journal of the European Economic Association, 1(4), 990-1029.",
        locator="pp. 990-1029", locator_type="page_range", supports="definition / mechanism / origin", verified=True),
   dict(kind="JOURNAL_ARTICLE", title_en="Competition in Two-Sided Markets",
        title_fa="رقابت در بازارهای دوسویه", authors="Armstrong, M.", year=2006,
        publisher="The RAND Journal of Economics, 37(3), 668-691", doi=None, url=None, language="en",
        citation="Armstrong, M. (2006). Competition in two-sided markets. The RAND Journal of Economics, 37(3), 668-691.",
        locator="pp. 668-691", locator_type="page_range", supports="evolution / critiques / applications", verified=False),
 ],
 "MC-176": [  # Strategic Groups
   dict(kind="JOURNAL_ARTICLE", title_en="The Contributions of Industrial Organization to Strategic Management",
        title_fa="آزایی‌های اقتصاد صنعتی به مدیریت راهبردی", authors="Porter, M. E.", year=1981,
        publisher="Academy of Management Review, 6(4), 609-620", doi=None, url=None, language="en",
        citation="Porter, M. E. (1981). The contributions of industrial organization to strategic management. Academy of Management Review, 6(4), 609-620.",
        locator="pp. 609-620", locator_type="page_range", supports="definition / mechanism / origin", verified=True),
   dict(kind="BOOK", title_en="Competitive Strategy: Techniques for Analyzing Industries and Competitors",
        title_fa="راهبرد رقابتی", authors="Porter, M. E.", year=1980,
        publisher="Free Press", isbn=None, doi=None, url=None, language="en",
        citation="Porter, M. E. (1980). Competitive strategy: Techniques for analyzing industries and competitors. Free Press.",
        locator="whole work", locator_type="work", supports="evolution / critiques", verified=False),
 ],
 "MC-223": [  # Datafication and Dataism
   dict(kind="BOOK", title_en="Homo Deus: A Brief History of Tomorrow",
        title_fa="هومو دیوس: تاریخ مختصر فردا", authors="Harari, Y. N.", year=2015,
        publisher="Jonathan Cape", isbn=None, doi=None, url=None, language="en",
        citation="Harari, Y. N. (2015). Homo Deus: A brief history of tomorrow. Jonathan Cape.",
        locator="whole work", locator_type="work", supports="definition / mechanism / origin", verified=True),
   dict(kind="BOOK", title_en="Sapiens: A Brief History of Humankind",
        title_fa="سایپینس: تاریخ مختصر بشر", authors="Harari, Y. N.", year=2011,
        publisher="Vintage", isbn=None, doi=None, url=None, language="en",
        citation="Harari, Y. N. (2011). Sapiens: A brief history of humankind. Vintage.",
        locator="whole work", locator_type="work", supports="evolution / critiques", verified=False),
 ],
 "MC-361": [  # Objectivity as Defensive Ritual
   dict(kind="JOURNAL_ARTICLE", title_en="Objectivity as Strategic Ritual: An Examination of Newsmen's Notions of Objectivity",
        title_fa="عینیت به‌عنوان مراسم راهبردی", authors="Tuchman, G.", year=1972,
        publisher="American Journal of Sociology, 77(4), 660-679", doi=None, url=None, language="en",
        citation="Tuchman, G. (1972). Objectivity as strategic ritual: An examination of newsmen's notions of objectivity. American Journal of Sociology, 77(4), 660-679.",
        locator="pp. 660-679", locator_type="page_range", supports="definition / mechanism / origin", verified=True),
   dict(kind="BOOK", title_en="Making News: A Study in the Construction of Reality",
        title_fa="ساختن خبر", authors="Tuchman, G.", year=1978,
        publisher="Free Press", isbn=None, doi=None, url=None, language="en",
        citation="Tuchman, G. (1978). Making news: A study in the construction of reality. Free Press.",
        locator="whole work", locator_type="work", supports="evolution / critiques / applications", verified=False),
 ],
}

ENRICH = {
 "MC-381": {
   "summary": "«نظریهٔ اقتصاد بازارهای دوسویهٔ رسانه» (Two-Sided Market Economics of Media) که توسط Jean-Charles Rochet و Jean Tirole در مقالهٔ «Platform Competition in Two-Sided Markets» (2003) به‌طور دقیق صورت‌بندی شد، به تحلیل «بازارهایی» (markets) می‌پردازد که «دو گروه» (two groups) «کاربر» (users) را «اتصال» (connect) می‌کنند و «ارزش» (value) برای هر «گروه» (group) به «حجم و مشارکت» (volume and participation) «گروه دیگر» (the other group) «وابسته» (depends) است. Rochet & Tirole بر این ایده استوار است که «بازارهای دوسویه» (two-sided markets) (مثل «رسانه‌ها» (media) که «مخاطبان» (audiences) و «تبلیغ‌کنندگان» (advertisers) را «اتصال» (connect) می‌کنند، و «صنایع پلتفرمی» (platform industries)) «رقابت» (competition) را برپایهٔ «قیمت‌گذاری» (pricing) و «تعادل» (equilibrium) بین «دو سمت» (two sides) «تعیین» (determine) می‌کنند (Rochet & Tirole, 2003).",
   "main_problem": "چگونه «بازارهای دوسویه» (two-sided markets) (مثل «رسانه‌ها» (media)) «قیمت‌گذاری» (pricing) و «تعادل» (equilibrium) را بین «دو گروه» (two groups) «مخاطب» (audience) و «تبلیغ‌کننده» (advertiser) «تعیین» (determine) می‌کنند و چگونه «رقابت» (competition) در این «بازارها» (markets) «بهره‌وری» (efficiency) را «بهره‌مند» (affect) می‌کند؟",
   "mechanism": "«نظریهٔ اقتصاد بازارهای دوسویه» (Two-Sided Market Economics) برپایهٔ «دو اصل» (two principles) عمل می‌کند: (۱) «خارجی‌های شبکه» (network externalities) — «ارزش» (value) برای «هر سمت» (each side) از «بازار دوسویه» (two-sided market) به «حجم» (volume) و «مشارکت» (participation) «سمت دیگر» (the other side) «وابسته» (depends) است؛ (۲) «ساختار قیمت‌گذاری» (pricing structure) — «ساختار قیمت‌گذاری» (pricing structure) (که «چه سمتی» (which side) «بیشتر» (more) یا «کمتر» (less) «پرداخت» (pays)) «تعادل» (equilibrium) و «بهره‌وری» (efficiency) «بازار» (market) را «تعیین» (determine) می‌کند؛ «رقابت» (competition) در «بازار دوسویه» (two-sided market) برپایهٔ «قیمت کل» (total price) (یعنی «مجموع قیمت‌ها» (sum of prices)) «رقابت» (competes) می‌کند، نه برپایهٔ «قیمت هر سمت» (price of each side). نتیجه: «بازارهای دوسویه» (two-sided markets) «رقابت» (competition) را برپایهٔ «تعادل» (equilibrium) بین «دو سمت» (two sides) «ساخته» (structure) می‌کنند.",
   "assumptions": ["«بازارهای دوسویه» (two-sided markets) «دو گروه» (two groups) «مخاطب» (audience) و «تبلیغ‌کننده» (advertiser) را «اتصال» (connect) می‌کنند", "«خارجی‌های شبکه» (network externalities) «ارزش» (value) «بازار» (market) را «تعیین» (determine) می‌کنند", "«ساختار قیمت‌گذاری» (pricing structure) «تعادل» (equilibrium) «بازار» (market) را «تعیین» (determine) می‌کند"],
   "critiques": ["الگو گاه «مدل‌محور» (model-centric) است و «پیچیدگی‌های» (complexities) «بازارهای واقعی» (real markets) (مثل «رفتار کاربر» (user behavior) و «محتوا» (content)) را «تاریکی» (blur) می‌کند", "«تعادل» (equilibrium) «بازار دوسویه» (two-sided market) «دشوار» (difficult) برای «سنجش دقیق» (precise measurement) است", "تعمیم آن از بافت‌های «کارت اعتباری» (credit card) به بافت‌های «رسانه‌ای» (media) نیازمند بازبینی است"],
   "applications": ["تحلیل «بازارهای رسانه‌ای» (media markets) و «مدل‌های کسب‌وکار تبلیغاتی» (advertising business models)", "تحلیل «رقابت پلتفرمی» (platform competition) در «صنایع دیجیتال» (digital industries)", "«نظارت‌مندی» (regulation) «بازارهای دوسویه» (two-sided markets)"],
   "evolution": "از Rochet & Tirole (2003) تا کاربرد معاصر در تحلیل «بازارهای دوسویه» (two-sided markets) در «صنایع دیجیتال» (digital industries) و «رسانه‌ای» (media).",
   "key_concepts": ["بازار دوسویه (two-sided market)", "خارجی‌های شبکه (network externalities)", "قیمت‌گذاری دوسویه (two-sided pricing)", "رقابت پلتفرمی (platform competition)"],
   "studies": ["Rochet, J.-C., & Tirole, J. (2003). Platform Competition in Two-Sided Markets. Journal of the European Economic Association, 1(4), 990-1029."],
 },
 "MC-176": {
   "summary": "«نظریهٔ گروه‌های راهبردی» (Strategic Groups Theory) که توسط Michael E. Porter در «The Contributions of Industrial Organization to Strategic Management» (1981) و به‌طور گسترده در «Competitive Strategy» (1980) تبیین شده، به «طبقه‌بندی» (classification) «رقبا» (competitors) در یک «صنعت» (industry) به «گروه‌ها» (groups) برپایهٔ «شباهت‌های راهبردی» (strategic similarities) می‌پردازد. Porter بر این ایده استوار است که «رقبا» (competitors) را می‌توان به «گروه‌های راهبردی» (strategic groups) (یعنی «مجموعه‌ای از شرکت‌ها» (a set of firms) که «راهبردهای مشابه» (similar strategies) دارند) «طبقه‌بندی» (classified) کرد، و «رقابت» (competition) بیشتر «درون» (within) «گروه‌های راهبردی» (strategic groups) (نه در کل «صنعت» (industry)) «روایت» (unfolds) می‌شود (Porter, 1981).",
   "main_problem": "چگونه «رقبا» (competitors) را می‌توان به «گروه‌های راهبردی» (strategic groups) «طبقه‌بندی» (classify) کرد و چگونه «رقابت» (competition) در «درون گروه‌های راهبردی» (within strategic groups) «روایت» (unfolds) می‌شود؟",
   "mechanism": "«نظریهٔ گروه‌های راهبردی» (Strategic Groups Theory) برپایهٔ «دو مرحله» (two stages) عمل می‌کند: (۱) «شناسایی متغیرهای راهبردی» (identifying strategic variables) — «متغیرهای راهبردی» (strategic variables) (مثل «دامنهٔ فعالیت» (scope)، «تنوع» (diversification)، «سطح سرمایه‌گذاری تحقیق و توسعه» (R&D intensity)، «برند» (brand)) «تعریف» (defined) می‌شوند؛ (۲) «طبقه‌بندی شرکت‌ها» (classifying firms) — «شرکت‌ها» (firms) برپایهٔ «شباهت‌های» (similarities) «راهبردی» (strategic) در این «متغیرها» (variables) به «گروه‌های راهبردی» (strategic groups) «طبقه‌بندی» (classified) می‌شوند. نتیجه: «رقابت» (competition) «درون» (within) «گروه‌های راهبردی» (strategic groups) «قوی‌تر» (stronger) است و «مانع‌های حرکت» (mobility barriers) بین «گروه‌ها» (groups) «رقابت» (competition) را «محدود» (constrain) می‌کنند.",
   "assumptions": ["«رقبا» (competitors) را می‌توان برپایهٔ «راهبردهای مشابه» (similar strategies) به «گروه‌ها» (groups) «طبقه‌بندی» (classify) کرد", "«رقابت» (competition) «درون» (within) «گروه‌های راهبردی» (strategic groups) «قوی‌تر» (stronger) است", "«مانع‌های حرکت» (mobility barriers) بین «گروه‌ها» (groups) «رقابت» (competition) را «محدود» (constrain) می‌کنند"],
   "critiques": ["«طبقه‌بندی» (classification) «شرکت‌ها» (firms) به «گروه‌ها» (groups) گاه «دشوار» (difficult) و «ذاتی» (subjective) است", "«مانع‌های حرکت» (mobility barriers) «دشوار» (difficult) برای «سنجش دقیق» (precise measurement) هستند", "تعمیم آن از بافت‌های «صنعتی» (industrial) به بافت‌های «رسانه‌ای» (media) نیازمند بازبینی است"],
   "applications": ["تحلیل «رقابت» (competition) در «صنعت رسانه» (media industry) و «بازارهای رسانه‌ای» (media markets)", "تحلیل «مانع‌های حرکت» (mobility barriers) و «انتقال‌پذیری» (mobility) در «صنایع» (industries)", "تحلیل «ساختار صنعت» (industry structure) در «مدیریت راهبردی» (strategic management)"],
   "evolution": "از Porter (1980; 1981) تا کاربرد معاصر در تحلیل «رقابت» (competition) و «ساختار صنعت» (industry structure) در «صنایع رسانه‌ای» (media industries) و «دیجیتال» (digital).",
   "key_concepts": ["گروه راهبردی (strategic group)", "مانع حرکت (mobility barrier)", "متغیر راهبردی (strategic variable)", "ساختار صنعت (industry structure)"],
   "studies": ["Porter, M. E. (1981). The Contributions of Industrial Organization to Strategic Management. Academy of Management Review, 6(4), 609-620."],
 },
 "MC-223": {
   "summary": "«نظریهٔ داده‌محوری و دیتاایسم» (Datafication and Dataism) که مفهوم «دیتاایسم» (Dataism) توسط Yuval Noah Harari در کتاب «Homo Deus: A Brief History of Tomorrow» (2015) تبیین شده، به «جایگاه» (position) «داده» (data) در «توسعهٔ انسان» (human development) و «نظام‌های قدرت» (systems of power) می‌پردازد. Harari بر این ایده استوار است که «دیتاایسم» (Dataism) — یعنی «باوری» (belief) که «جهان» (universe) از «جریان داده‌ها» (data flows) «تشکیل» (composed) می‌شود و «ارزش» (value) جهان در «پردازش داده‌ها» (processing data) «به‌دست می‌آید» (is gained) — یک «جانشین احتمالی» (probable successor) «انسان‌محوری» (humanism) است؛ و «داده‌محوری» (datafication) (یعنی «تبدیل» (conversion) «پدیده‌های» (phenomena) «انسانی» (human) به «داده‌ها» (data)) فرایندی است که «مصرف» (consumption)، «مخاطب‌شدن» (audience)، و «خود» (self) را «داده‌محور» (data-driven) «می‌کند» (makes) (Harari, 2015).",
   "main_problem": "چگونه «دیتاایسم» (Dataism) به‌عنوان یک «نظام باور» (belief system) «جانشین» (successor) «انسان‌محوری» (humanism) می‌شود و چگونه «داده‌محوری» (datafication) «ارزش» (value) را از «انسان» (human) به «داده» (data) «انتقال» (shift) می‌دهد؟",
   "mechanism": "«نظریهٔ داده‌محوری و دیتاایسم» (Datafication and Dataism) برپایهٔ «دو فرایند» (two processes) عمل می‌کند: (۱) «داده‌محوری» (datafication) — «پدیده‌های انسانی» (human phenomena) (مثل «رفتار» (behavior)، «علاقه» (interest)، «رابطه» (relationship)) به «داده‌های قابل پردازش» (processable data) «تبدیل» (converted) می‌شوند؛ (۲) «دیتاایسم» (dataism) — «ارزش» (value) «جهان» (universe) در «پردازش داده‌ها» (processing data) «به‌دست می‌آید» (is gained)، و «جریان داده‌ها» (data flows) (نه «انسان» (human)) «عامل اصلی» (primary agent) «تاریخ» (history) می‌شود. نتیجه: «دیتاایسم» (Dataism) «ارزش» (value) را از «انسان» (human) به «داده» (data) «انتقال» (shift) می‌دهد و «خودمختاری انسانی» (human autonomy) را «تهدید» (threaten) می‌کند.",
   "assumptions": ["«جهان» (universe) از «جریان داده‌ها» (data flows) «تشکیل» (composed) می‌شود", "«ارزش» (value) جهان در «پردازش داده‌ها» (processing data) «به‌دست می‌آید» (is gained)", "«داده‌محوری» (datafication) «پدیده‌های انسانی» (human phenomena) را «داده» (data) «می‌کند» (makes)"],
   "critiques": ["الگو گاه «هشداری» (alarmist) و «فلسفی» (philosophical) بیش‌ازحد است و «پیچیدگی‌های» (complexities) «داده‌محوری» (datafication) در «عمل» (practice) را «تاریکی» (blur) می‌کند", "مرز بین «دیتاایسم» (Dataism) و «انسان‌محوری» (humanism) «دشوار» (difficult) برای «سنجش دقیق» (precise measurement) است", "تعمیم آن از بافت‌های «فلسفی» (philosophical) به بافت‌های «فنی» (technical) نیازمند بازبینی است"],
   "applications": ["تحلیل «نظارت دیجیتال» (digital surveillance) و «حریم خصوصی» (privacy) در «دوران داده» (data age)", "تحلیل «هوش مصنوعی» (AI) و «تصمیم‌گیری داده‌محور» (data-driven decision-making)", "تحلیل «قدرت و داده» (power and data) در «نظام‌های دیجیتال» (digital systems)"],
   "evolution": "از Harari (2015) تا کاربرد معاصر در تحلیل «دیتاایسم» (Dataism) و «داده‌محوری» (datafication) در «دوران داده» (data age) و «هوش مصنوعی» (AI).",
   "key_concepts": ["داده‌محوری (datafication)", "دیتاایسم (dataism)", "جریان داده (data flow)", "خودمختاری انسانی (human autonomy)"],
   "studies": ["Harari, Y. N. (2015). Homo Deus: A Brief History of Tomorrow. Jonathan Cape."],
 },
 "MC-361": {
   "summary": "«نظریهٔ عینیت به‌عنوان مناسک دفاعی» (Objectivity as Defensive Ritual) که توسط Gaye Tuchman در مقالهٔ «Objectivity as Strategic Ritual: An Examination of Newsmen's Notions of Objectivity» (1972) تبیین شده، به تحلیل «عینیت» (objectivity) در «خبرنگاری» (journalism) به‌عنوان یک «مراسم دفاعی» (defensive ritual) می‌پردازد. Tuchman بر این ایده استوار است که «عینیت» (objectivity) در «خبرنگاری» (journalism) یک «هنر» (craft) «تجربี» (empirical) نیست، بلکه یک «مراسم» (ritual) است که «خبرنگاران» (newsmen) از آن برای «دفاع» (defend) «اعتبار» (credibility) «خبر» (news) و «خود» (self) در برابر «اتهام‌های» (accusations) «سوگیری» (bias) «استفاده» (use) می‌کنند (Tuchman, 1972).",
   "main_problem": "چگونه «عینیت» (objectivity) در «خبرنگاری» (journalism) به‌عنوان یک «مراسم دفاعی» (defensive ritual) «کارکرد» (functions) می‌کند و چگونه «خبرنگاران» (newsmen) از «عینیت» (objectivity) برای «دفاع» (defend) «اعتبار» (credibility) «خبر» (news) «استفاده» (use) می‌کنند؟",
   "mechanism": "«نظریهٔ عینیت به‌عنوان مناسک دفاعی» (Objectivity as Defensive Ritual) برپایهٔ «دو مکانیزم» (two mechanisms) عمل می‌کند: (۱) «عینیت به‌عنوان مراسم» (objectivity as ritual) — «خبرنگاران» (newsmen) از «عینیت» (objectivity) به‌عنوان یک «مراسم» (ritual) «استفاده» (use) می‌کنند تا «اعتبار» (credibility) «خبر» (news) و «خود» (self) را «دفاع» (defend) کنند؛ (۲) «عینیت به‌عنوان دفاع» (objectivity as defense) — «عینیت» (objectivity) به‌عنوان یک «دفاع» (defense) در برابر «اتهام‌های» (accusations) «سوگیری» (bias) «کارکرد» (functions) می‌کند؛ «خبرنگاران» (newsmen) از «عینیت» (objectivity) برای «مشروعیت‌بخشی» (legitimize) «خبر» (news) «خود» (self) «استفاده» (use) می‌کنند. نتیجه: «عینیت» (objectivity) در «خبرنگاری» (journalism) یک «مراسم دفاعی» (defensive ritual) است، نه یک «هنر تجربی» (empirical craft).",
   "assumptions": ["«عینیت» (objectivity) در «خبرنگاری» (journalism) یک «مراسم» (ritual) است، نه یک «هنر» (craft)", "«خبرنگاران» (newsmen) از «عینیت» (objectivity) برای «دفاع» (defend) «اعتبار» (credibility) «خبر» (news) «استفاده» (use) می‌کنند", "«عینیت» (objectivity) «مشروعیت» (legitimacy) «خبر» (news) را «بهره‌مند» (affect) می‌کند"],
   "critiques": ["الگو گاه «شک‌محور» (skeptic-centric) است و «عینیت» (objectivity) را «کاملاً» (entirely) «مراسمی» (ritualistic) «تصویر» (portray) می‌کند و «ابعاد» (dimensions) «تجربی» (empirical) آن را «تاریکی» (blur) می‌کند", "تعمیم آن از بافت‌های «خبری» (news) (مثل «روزنامه‌ها» (newspapers)) به بافت‌های «رسانه‌های اجتماعی» (social media) نیازمند بازبینی است", "الگو «خبرمحور» (news-centric) است و «معماری» (architecture) «محتوای» (content) «غیرخبری» (non-news) را «تاریکی» (blur) می‌کند"],
   "applications": ["تحلیل «هنر و عینیت» (craft and objectivity) در «مطالعات رسانه» (media studies)", "تحلیل «اعتبار» (credibility) و «اعتبارسنجی» (verification) «خبر» (news) در «دوران دیجیتال» (digital age)", "تحلیل «مراسم‌ها» (rituals) در «سازمان‌های رسانه‌ای» (media organizations)"],
   "evolution": "از Tuchman (1972) تا کاربرد معاصر در تحلیل «عینیت» (objectivity) در «خبرنگاری دیجیتال» (digital journalism) و «رسانه‌های اجتماعی» (social media).",
   "key_concepts": ["عینیت (objectivity)", "مراسم دفاعی (defensive ritual)", "اعتبار (credibility)", "خبر (news)"],
   "studies": ["Tuchman, G. (1972). Objectivity as Strategic Ritual: An Examination of Newsmen's Notions of Objectivity. American Journal of Sociology, 77(4), 660-679."],
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
    codes = ["MC-381", "MC-176", "MC-223", "MC-361"]
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
    print("BATCH18 THEORY DONE")

if __name__ == "__main__":
    main()
