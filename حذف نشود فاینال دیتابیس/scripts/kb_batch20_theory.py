# -*- coding: utf-8 -*-
"""Batch 20 (THEORY): MC-250 Communication Privacy Management (Petronio 2002), MC-086 Diffusion of
Innovations (Rogers 2003), MC-198 Media Capture (Stigler 1971), MC-258 Networked Publics (boyd 2014).
Sources web-verified 2026-11-16. Target: resaname_kb_final_inspect."""
import pymysql, json

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch20-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch20_theory.json"

S = {
 "MC-250": [  # Communication Privacy Management Theory
   dict(kind="BOOK", title_en="Boundaries of Privacy: Dialectics of Disclosure",
        title_fa="مرزهای حریم خصوصی: دیالکتیک افشا", authors="Petronio, S.", year=2002,
        publisher="SUNY Press", isbn=None, doi=None, url=None, language="en",
        citation="Petronio, S. (2002). Boundaries of privacy: Dialectics of disclosure. SUNY Press.",
        locator="whole work", locator_type="work", supports="definition / mechanism / origin", verified=True),
   dict(kind="BOOK", title_en="Self-Disclosure",
        title_fa="خودافشایی", authors="Derlega, V. J., Metts, S., Petronio, S., & Margulis, S. T.", year=1993,
        publisher="McGraw-Hill", isbn=None, doi=None, url=None, language="en",
        citation="Derlega, V. J., Metts, S., Petronio, S., & Margulis, S. T. (1993). Self-disclosure. McGraw-Hill.",
        locator="whole work", locator_type="work", supports="evolution / critiques", verified=False),
 ],
 "MC-086": [  # Diffusion of Innovations
   dict(kind="BOOK", title_en="Diffusion of Innovations (5th ed.)",
        title_fa="انتشار نوآوری‌ها (ویرایش پنجم)", authors="Rogers, E. M.", year=2003,
        publisher="Free Press", isbn="0743222091", doi=None, url=None, language="en",
        citation="Rogers, E. M. (2003). Diffusion of innovations (5th ed.). Free Press.",
        locator="whole work", locator_type="work", supports="definition / mechanism / origin", verified=True),
   dict(kind="BOOK", title_en="Diffusion of Innovations (1st ed.)",
        title_fa="انتشار نوآوری‌ها (ویرایش اول)", authors="Rogers, E. M.", year=1962,
        publisher="Free Press", isbn=None, doi=None, url=None, language="en",
        citation="Rogers, E. M. (1962). Diffusion of innovations. Free Press.",
        locator="whole work", locator_type="work", supports="evolution / critiques", verified=False),
 ],
 "MC-198": [  # Media Capture
   dict(kind="JOURNAL_ARTICLE", title_en="The Theory of Economic Regulation",
        title_fa="نظریهٔ نظارت اقتصادی", authors="Stigler, G. J.", year=1971,
        publisher="The Bell Journal of Economics and Management Science, 2(1), 3-21", doi=None, url=None, language="en",
        citation="Stigler, G. J. (1971). The theory of economic regulation. The Bell Journal of Economics and Management Science, 2(1), 3-21.",
        locator="pp. 3-21", locator_type="page_range", supports="definition / mechanism / origin", verified=True),
   dict(kind="JOURNAL_ARTICLE", title_en="Toward a More General Theory of Regulation",
        title_fa="در راه نظریه‌ای عمومی‌تر از نظارت", authors="Peltzman, S.", year=1976,
        publisher="The Journal of Law and Economics, 19(2), 211-240", doi=None, url=None, language="en",
        citation="Peltzman, S. (1976). Toward a more general theory of regulation. The Journal of Law and Economics, 19(2), 211-240.",
        locator="pp. 211-240", locator_type="page_range", supports="evolution / critiques / applications", verified=False),
 ],
 "MC-258": [  # Social Network Sites & Networked Publics
   dict(kind="BOOK", title_en="It's Complicated: The Social Lives of Networked Teens",
        title_fa="پیچیده است: زندگی‌های اجتماعی نوجوانان شبکه‌ای", authors="boyd, d.", year=2014,
        publisher="Yale University Press", isbn="978-0-300-16631-6", doi=None, url=None, language="en",
        citation="boyd, d. (2014). It's complicated: The social lives of networked teens. Yale University Press.",
        locator="whole work", locator_type="work", supports="definition / mechanism / origin", verified=True),
   dict(kind="JOURNAL_ARTICLE", title_en="Social Network Sites: Definition, History, and Scholarship",
        title_fa="مناظر شبکه‌ای اجتماعی: تعریف، تاریخ و پژوهش", authors="boyd, d. m., & Ellison, N. B.", year=2007,
        publisher="Journal of Computer-Mediated Communication, 13(1), 210-230", doi=None, url=None, language="en",
        citation="boyd, d. m., & Ellison, N. B. (2007). Social network sites: Definition, history, and scholarship. Journal of Computer-Mediated Communication, 13(1), 210-230.",
        locator="pp. 210-230", locator_type="page_range", supports="evolution / critiques", verified=False),
 ],
}

ENRICH = {
 "MC-250": {
   "summary": "«نظریهٔ مدیریت حریم خصوصی ارتباطی» (Communication Privacy Management Theory, CPM) که توسط Sandra Petronio در کتاب «Boundaries of Privacy: Dialectics of Disclosure» (2002) صورت‌بندی شد، به تحلیل «مدیریت مرزهای حریم خصوصی» (management of privacy boundaries) در «رابطه‌های ارتباطی» (communication relationships) می‌پردازد. Petronio بر این ایده استوار است که «اطلاعات شخصی» (personal information) به‌طور طبیعی «حریم خصوصی» (private) است و «افراد» (individuals) «مالک» (owners) «اطلاعات» (information) خود هستند؛ وقتی «اطلاعات شخصی» (personal information) «اشتراک‌گذاری» (shared) می‌شود، «مالکان مشترک» (co-owners) «مرزهای حریم خصوصی» (privacy boundaries) را برپایهٔ «قوانین کنترل اطلاعات شخصی» (personal information control rules) «هماهنگ» (coordinate) می‌کنند (Petronio, 2002).",
   "main_problem": "چگونه «افراد» (individuals) «مرزهای حریم خصوصی» (privacy boundaries) خود را «مدیریت» (manage) می‌کنند و چگونه «مالکان مشترک» (co-owners) «اطلاعات شخصی» (personal information) «اشتراک‌گذاری‌شده» (shared) «مرزها» (boundaries) را «هماهنگ» (coordinate) می‌کنند؟",
   "mechanism": "«نظریهٔ مدیریت حریم خصوصی ارتباطی» (CPM) برپایهٔ «چرخهٔ کنترل مرز» (boundary control cycle) عمل می‌کند: (۱) «مالکیت اطلاعات» (information ownership) — «افراد» (individuals) «مالک» (owners) «اطلاعات شخصی» (personal information) خود هستند و «حق کنترل» (right to control) «اشتراک‌گذاری» (disclosure) را دارند؛ (۲) «اشتراک‌گذاری و مالکیت مشترک» (disclosure and co-ownership) — وقتی «اطلاعات» (information) «اشتراک‌گذاری» (shared) می‌شود، «مالک» (owner) «حق مالکیت» (ownership rights) را به «مالک مشترک» (co-owner) «منتقل» (transfers) می‌کند؛ (۳) «هماهنگ‌سازی مرز» (boundary coordination) — «مالکان مشترک» (co-owners) برپایهٔ «قوانین کنترل اطلاعات شخصی» (personal information control rules) (مثل «پاسخ‌پذیری مرز» (boundary permeability) و «پیوند مرز» (boundary linkage)) «مرزها» (boundaries) را «هماهنگ» (coordinate) می‌کنند. نتیجه: «مدیریت حریم خصوصی» (privacy management) یک «فرایند دیالکتیکی» (dialectical process) «کنترل» (control) و «اشتراک‌گذاری» (disclosure) است.",
   "assumptions": ["«اطلاعات شخصی» (personal information) به‌طور طبیعی «حریم خصوصی» (private) است", "«افراد» (individuals) «مالک» (owners) «اطلاعات» (information) خود هستند", "«مالکان مشترک» (co-owners) «مرزهای» (boundaries) را «هماهنگ» (coordinate) می‌کنند"],
   "critiques": ["الگو گاه «ارتباطی» (communication-centric) است و «عوامل اجتماعی و فرهنگی» (social and cultural factors) را «تاریکی» (blur) می‌کند", "«قوانین کنترل مرز» (boundary control rules) «دشوار» (difficult) برای «سنجش دقیق» (precise measurement) است", "تعمیم آن از بافت‌های «رابطه‌ای» (relational) (مثل «خانواده» (family)) به بافت‌های «رسانه‌های اجتماعی» (social media) نیازمند بازبینی است"],
   "applications": ["تحلیل «حریم خصوصی» (privacy) در «رسانه‌های اجتماعی» (social media) و «رسانه‌های دیجیتال» (digital media)", "تحلیل «اشتراک‌گذاری اطلاعات» (information sharing) و «مالکیت مشترک» (co-ownership)", "تحلیل «حریم خصوصی» (privacy) در «رابطه‌های نزدیک» (close relationships)"],
   "evolution": "از Petronio (2002) تا کاربرد معاصر در تحلیل «حریم خصوصی ارتباطی» (communication privacy) در «رسانه‌های دیجیتال» (digital media) و «رسانه‌های اجتماعی» (social media).",
   "key_concepts": ["مدیریت حریم خصوصی ارتباطی (communication privacy management)", "مرز حریم خصوصی (privacy boundary)", "مالکیت مشترک (co-ownership)", "قوانین کنترل اطلاعات شخصی (personal information control rules)"],
   "studies": ["Petronio, S. (2002). Boundaries of Privacy: Dialectics of Disclosure. SUNY Press."],
 },
 "MC-086": {
   "summary": "«نظریهٔ انتشار نوآوری» (Diffusion of Innovations) که توسط Everett M. Rogers در کتاب «Diffusion of Innovations» (2003, 5th ed.) صورت‌بندی شد، به تحلیل «نحوه‌ای» می‌پردازد که یک «نوآوری» (innovation) در «طول زمان» (over time) از طریق «کانال‌های ارتباطی» (communication channels) در یک «نظام اجتماعی» (social system) «انتشار» (diffused) می‌شود. Rogers بر این ایده استوار است که «انتشار» (diffusion) یک «فرایند» (process) است که در آن «افراد» (individuals) برپایهٔ «زمان پذیرش» (adoption time) به «نوپایندگان» (innovators)، «زودهنگام‌ها» (early adopters)، «اکثریت زودهنگام» (early majority)، «اکثریت دیرهنگام» (late majority)، و «خاکسپارندگان» (laggards) «دسته‌بندی» (categorized) می‌شوند (Rogers, 2003).",
   "main_problem": "چگونه یک «نوآوری» (innovation) در «طول زمان» (over time) در یک «نظام اجتماعی» (social system) «انتشار» (diffused) می‌شود و چگونه «افراد» (individuals) برپایهٔ «پذیرش» (adoption) «دسته‌بندی» (categorized) می‌شوند؟",
   "mechanism": "«نظریهٔ انتشار نوآوری» (Diffusion of Innovations) برپایهٔ «چهار عنصر» (four elements) عمل می‌کند: (۱) «نوآوری» (innovation) — «نوآوری» (innovation) برپایهٔ «پنج ویژگی» (five attributes) ارزیابی می‌شود: «مزیت نسبی» (relative advantage)، «سازگاری» (compatibility)، «پیچیدگی» (complexity)، «قابلیت آزمایش» (trialability)، و «قابلیت مشاهده» (observability)؛ (۲) «کانال‌ها» (channels) — «نوآوری» (innovation) از طریق «کانال‌های ارتباطی» (communication channels) (مثل «رسانه‌های جمعی» (mass media) و «ارتباطات بین‌فردی» (interpersonal communication)) «انتقال» (transmitted) می‌شود؛ (۳) «نظام اجتماعی» (social system) — «نظام اجتماعی» (social system) «چارچوب» (framework) «انتشار» (diffusion) است؛ (۴) «زمان» (time) — «افراد» (individuals) برپایهٔ «زمان پذیرش» (adoption time) به «نوپایندگان» (innovators)، «زودهنگام‌ها» (early adopters)، «اکثریت زودهنگام» (early majority)، «اکثریت دیرهنگام» (late majority)، و «خاکسپارندگان» (laggards) «دسته‌بندی» (categorized) می‌شوند. نتیجه: «انتشار نوآوری» (diffusion of innovations) یک «منحنی S» (S-curve) «به‌وجود می‌آورد» (produces).",
   "assumptions": ["«نوآوری» (innovation) برپایهٔ «پنج ویژگی» (five attributes) ارزیابی می‌شود", "«انتشار» (diffusion) از طریق «کانال‌های ارتباطی» (communication channels) «می‌شود» (occurs)", "«افراد» (individuals) برپایهٔ «زمان پذیرش» (adoption time) «دسته‌بندی» (categorized) می‌شوند"],
   "critiques": ["الگو گاه «پذیرش‌محور» (adoption-centric) است و «مقاومت» (resistance) و «مخالفان» (rejecters) را «تاریکی» (blur) می‌کند", "«منحنی پذیرش» (adoption curve) «دشوار» (difficult) برای «تعمیم» (generalize) به «نظام‌های دیجیتال» (digital systems) است", "تعمیم آن از بافت‌های «کشاورزی» (agricultural) به بافت‌های «رسانه‌ای» (media) نیازمند بازبینی است"],
   "applications": ["تحلیل «انتشار نوآوری» (diffusion of innovations) در «رسانه‌های دیجیتال» (digital media) و «فناوری‌های جدید» (new technologies)", "تحلیل «پذیرش» (adoption) «رسانه‌های اجتماعی» (social media) و «اپلیکیشن‌ها» (applications)", "تحلیل «انتشار» (diffusion) «دانش» (knowledge) و «محتوا» (content)"],
   "evolution": "از Rogers (1962; 2003) تا کاربرد معاصر در تحلیل «انتشار نوآوری» (diffusion of innovations) در «رسانه‌های دیجیتال» (digital media) و «فناوری‌های جدید» (new technologies).",
   "key_concepts": ["انتشار نوآوری (diffusion of innovations)", "پذیرش (adoption)", "کانال‌های ارتباطی (communication channels)", "منحنی S (S-curve)"],
   "studies": ["Rogers, E. M. (2003). Diffusion of Innovations (5th ed.). Free Press."],
 },
 "MC-198": {
   "summary": "«نظریهٔ تسخیر رسانه» (Media Capture Theory) که برپایهٔ «نظریهٔ تسخیر نظارتی» (regulatory capture theory) توسط George J. Stigler در «The Theory of Economic Regulation» (1971) شکل گرفته، به تحلیل «چگونگی تسخیر» (how capture occurs) «رسانه‌ها» (media) توسط «صنایع» (industries) یا «منافع قوی» (powerful interests) می‌پردازد. Stigler بر این ایده استوار است که «نظارت» (regulation) (و به‌طور گسترده‌تر «حاکمیت» (governance)) اغلب «توسط «صنعت» (industry) «تسخیر» (captured) می‌شود و برای «نفع» (benefit) آن «صنعت» (industry) «طراحی» (designed) و «کار» (operated) می‌شود، نه برای «نفع عمومی» (public benefit) (Stigler, 1971).",
   "main_problem": "چگونه «رسانه‌ها» (media) توسط «صنایع» (industries) یا «منافع قوی» (powerful interests) «تسخیر» (captured) می‌شوند و چگونه این «تسخیر» (capture) «اعتبار رسانه‌ای» (media credibility) و «منافع عمومی» (public interest) را «تهدید» (threaten) می‌کند؟",
   "mechanism": "«نظریهٔ تسخیر رسانه» (Media Capture Theory) برپایهٔ «دو مکانیزم» (two mechanisms) عمل می‌کند: (۱) «تسخیر نظارتی» (regulatory capture) — «صنعت» (industry) (یا «سازمان رسانه‌ای» (media organization)) «نظارت» (regulation) و «حاکمیت» (governance) خود را «تسخیر» (captured) می‌کند تا «نفع» (benefit) خود را «حفظ» (protect) کند؛ (۲) «تسخیر اقتصادی» (economic capture) — «سازمان‌های رسانه‌ای» (media organizations) توسط «مالکان» (owners) و «تبلیغ‌کنندگان بزرگ» (large advertisers) «تسخیر» (captured) می‌شوند و «محتوا» (content) را برپایهٔ «منافع تجاری» (commercial interests) «ساخته» (shape) می‌کنند. نتیجه: «تسخیر رسانه» (media capture) «اعتبار رسانه‌ای» (media credibility) و «منافع عمومی» (public interest) را «تهدید» (threaten) می‌کند.",
   "assumptions": ["«نظارت» (regulation) و «حاکمیت» (governance) اغلب «توسط «صنعت» (industry) «تسخیر» (captured) می‌شوند", "«سازمان‌های رسانه‌ای» (media organizations) تحت تأثیر «منافع تجاری» (commercial interests) «قرار می‌گیرند» (are influenced)", "«تسخیر» (capture) «منافع عمومی» (public interest) را «تهدید» (threaten) می‌کند"],
   "critiques": ["الگو گاه «اقتصادی‌محور» (economics-centric) است و «عوامل فرهنگی و اجتماعی» (cultural and social factors) را «تاریکی» (blur) می‌کند", "«تسخیر» (capture) «دشوار» (difficult) برای «سنجش دقیق» (precise measurement) است", "تعمیم آن از بافت‌های «نظارتی» (regulatory) به بافت‌های «رسانه‌ای» (media) نیازمند بازبینی است"],
   "applications": ["تحلیل «تمرکز مالکیت رسانه» (media ownership concentration) و «تأثیر تبلیغ‌کنندگان» (advertiser influence)", "تحلیل «اعتبار رسانه‌ای» (media credibility) و «استقلال رسانه» (media independence)", "تحلیل «حاکمیت رسانه» (media governance) و «نظارت» (regulation)"],
   "evolution": "از Stigler (1971) تا کاربرد معاصر در تحلیل «تسخیر رسانه» (media capture) در «بازارهای رسانه‌ای» (media markets) و «حاکمیت دیجیتال» (digital governance).",
   "key_concepts": ["تسخیر نظارتی (regulatory capture)", "تسخیر رسانه (media capture)", "منافع عمومی (public interest)", "حاکمیت رسانه (media governance)"],
   "studies": ["Stigler, G. J. (1971). The Theory of Economic Regulation. The Bell Journal of Economics and Management Science, 2(1), 3-21."],
 },
 "MC-258": {
   "summary": "«نظریهٔ جمعیت‌های شبکه‌ای» (Networked Publics Theory) که توسط danah boyd در کتاب «It's Complicated: The Social Lives of Networked Teens» (2014) به‌طور گسترده تبیین شده، به تحلیل «مناظر شبکه‌ای» (networked public spheres) می‌پردازد که «افراد» (individuals) در آن‌ها «ارتباط» (connect)، «مشارکت» (participate)، و «محتوا» (content) «تولید» (produce) می‌کنند. boyd بر این ایده استوار است که «مناظر شبکه‌ای» (networked publics) «فضاهایی» (spaces) هستند که در آن‌ها «افراد» (individuals) (مثل «نوجوانان» (teens)) «رابطه‌ها» (relationships) «برقرار» (establish)، «هویت‌ها» (identities) «ساخته» (construct)، و «اطلاعات» (information) را در «مرزهای» (boundaries) «عمومی و خصوصی» (public and private) «مدیریت» (manage) می‌کنند (boyd, 2014).",
   "main_problem": "چگونه «مناظر شبکه‌ای» (networked publics) «هویت» (identity)، «رابطه» (relationship)، و «حریم خصوصی» (privacy) «افراد» (individuals) را «بهره‌مند» (affect) می‌کنند و چگونه «نوجوانان» (teens) در این «مناظر» (publics) «عمل» (navigate) می‌کنند؟",
   "mechanism": "«نظریهٔ جمعیت‌های شبکه‌ای» (Networked Publics Theory) برپایهٔ «دو لایه» (two layers) عمل می‌کند: (۱) «ساخته‌شدن مناظر» (constructing publics) — «مناظر شبکه‌ای» (networked publics) برپایهٔ «مناظر شبکه‌ای اجتماعی» (social network sites) «ساخته» (constructed) می‌شوند که «افراد» (individuals) «اتصال» (connect) و «مشارکت» (participate) می‌کنند؛ (۲) «مدیریت مرزها» (managing boundaries) — «افراد» (individuals) در «مناظر شبکه‌ای» (networked publics) «مرزهای» (boundaries) «عمومی و خصوصی» (public and private) را «مدیریت» (manage) می‌کنند و «هویت‌ها» (identities) و «رابطه‌ها» (relationships) را «ساخته» (construct) می‌کنند. نتیجه: «مناظر شبکه‌ای» (networked publics) «فناوری» (technology) و «اجتماع» (society) را «بازتعریف» (redefine) می‌کنند.",
   "assumptions": ["«مناظر شبکه‌ای» (networked publics) «فضاهایی» (spaces) برای «اتصال» (connection) و «مشارکت» (participation) هستند", "«افراد» (individuals) در «مناظر شبکه‌ای» (networked publics) «هویت‌ها» (identities) و «رابطه‌ها» (relationships) را «ساخته» (construct) می‌کنند", "«مرزهای» (boundaries) «عمومی و خصوصی» (public and private) در «مناظر شبکه‌ای» (networked publics) «تاریکی» (blurred) هستند"],
   "critiques": ["الگو گاه «نوجوان‌محور» (teen-centric) است و «مناظر شبکه‌ای» (networked publics) «بالغان» (adults) را «تاریکی» (blur) می‌کند", "«مناظر شبکه‌ای» (networked publics) «دشوار» (difficult) برای «سنجش دقیق» (precise measurement) است", "تعمیم آن از بافت‌های «شبکه‌های اجتماعی» (social network sites) به بافت‌های «رسانه‌های دیجیتال» (digital media) نیازمند بازبینی است"],
   "applications": ["تحلیل «مناظر شبکه‌ای» (networked publics) در «رسانه‌های اجتماعی» (social media)", "تحلیل «هویت و رابطه» (identity and relationship) در «رسانه‌های دیجیتال» (digital media)", "تحلیل «حریم خصوصی» (privacy) در «رسانه‌های اجتماعی» (social media)"],
   "evolution": "از boyd (2010; 2014) تا کاربرد معاصر در تحلیل «مناظر شبکه‌ای» (networked publics) در «رسانه‌های اجتماعی» (social media) و «رسانه‌های دیجیتال» (digital media).",
   "key_concepts": ["جمعیت شبکه‌ای (networked public)", "مکان شبکه‌ای (networked site)", "مرز عمومی-خصوصی (public-private boundary)", "هویت دیجیتال (digital identity)"],
   "studies": ["boyd, d. (2014). It's Complicated: The Social Lives of Networked Teens. Yale University Press."],
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
    codes = ["MC-250", "MC-086", "MC-198", "MC-258"]
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
    print("BATCH20 THEORY DONE")

if __name__ == "__main__":
    main()
