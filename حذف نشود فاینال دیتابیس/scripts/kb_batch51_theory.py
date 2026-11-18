# -*- coding: utf-8 -*-
"""Batch 51 (THEORY): MC-210 Informational Shortcuts (Lupia 1994), MC-213 Global Civil Society
(Keane 2003), MC-214 Transnational Public Sphere (Fraser 2007), MC-215 Cosmopolitanism
(Beck 2006). Anchors verified 2026-11-16."""
import pymysql, json

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch51-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch51_theory.json"

S = {
 "MC-210": [
   dict(kind="JOURNAL_ARTICLE", title_en="Shortcuts Versus Encyclopedias: Information and Voting Behavior in California Insurance Reform Elections",
        title_fa="میان‌بُرها در برابر دانشنامه‌ها: اطلاعات و رفتار رأی‌دهی در انتخابات اصلاح بیمهٔ کالیفرنیا",
        authors="Lupia, A.", year=1994,
        publisher="American Political Science Review, 88(1), 63-76", doi="10.2307/2944882",
        url="https://www.cambridge.org/core/journals/american-political-science-review/article/shortcuts-versus-encyclopedias-information-and-voting-behavior-in-california-insurance-reform-elections/75776D189E80711664254A02BC0573F4",
        language="en", isbn=None,
        citation="Lupia, A. (1994). Shortcuts versus encyclopedias: Information and voting behavior in California insurance reform elections. American Political Science Review, 88(1), 63-76.",
        locator="pp. 63-76", locator_type="page_range", supports="definition / cue-taking evidence", verified=True),
   dict(kind="BOOK", title_en="The Reasoning Voter: Communication and Persuasion in Presidential Campaigns",
        title_fa="رأی‌دهندهٔ استدلال‌گر: ارتباط و اقناع در کارزارهای ریاست‌جمهوری",
        authors="Popkin, S. L.", year=1991, publisher="Chicago: University of Chicago Press", doi=None,
        url=None, language="en", isbn=None,
        citation="Popkin, S. L. (1991). The reasoning voter: Communication and persuasion in presidential campaigns. University of Chicago Press.",
        locator="whole work", locator_type="work", supports="evolution / low-information rationality", verified=False),
 ],
 "MC-213": [
   dict(kind="BOOK", title_en="Global Civil Society?", title_fa="جامعهٔ مدنی جهانی؟",
        authors="Keane, J.", year=2003, publisher="Cambridge: Cambridge University Press", doi=None,
        url="https://www.cambridge.org/core/books/global-civil-society/7FC3F5B3503F7EFAA5DAA5099A002DE4",
        language="en", isbn="9780521894623",
        citation="Keane, J. (2003). Global civil society? Cambridge University Press.",
        locator="whole work", locator_type="work", supports="definition / cross-border non-state sphere", verified=True),
   dict(kind="BOOK_CHAPTER", title_en="Introducing Global Civil Society",
        title_fa="معرفی جامعهٔ مدنی جهانی",
        authors="Anheier, H., Glasius, M., & Kaldor, M.", year=2001,
        publisher="In H. Anheier, M. Glasius, & M. Kaldor (Eds.), Global Civil Society 2001 (pp. 3-22). Oxford University Press",
        doi=None, url=None, language="en", isbn=None,
        citation="Anheier, H., Glasius, M., & Kaldor, M. (2001). Introducing global civil society. In Global civil society 2001 (pp. 3-22). Oxford University Press.",
        locator="pp. 3-22", locator_type="page_range", supports="evolution / empirical measurement", verified=False),
 ],
 "MC-214": [
   dict(kind="JOURNAL_ARTICLE", title_en="Transnationalizing the Public Sphere: On the Legitimacy and Efficacy of Public Opinion in a Post-Westphalian World",
        title_fa="فراملی‌کردن حوزهٔ عمومی: دربارهٔ مشروعیت و کارآمدی افکار عمومی در جهان پساوستفالیایی",
        authors="Fraser, N.", year=2007,
        publisher="Theory, Culture & Society, 24(4), 7-30", doi="10.1177/0263276407080090",
        url="https://journals.sagepub.com/doi/10.1177/0263276407080090",
        language="en", isbn=None,
        citation="Fraser, N. (2007). Transnationalizing the public sphere: On the legitimacy and efficacy of public opinion in a post-Westphalian world. Theory, Culture & Society, 24(4), 7-30.",
        locator="pp. 7-30", locator_type="page_range", supports="definition / all-affected principle", verified=True),
   dict(kind="JOURNAL_ARTICLE", title_en="Rethinking the Public Sphere: A Contribution to the Critique of Actually Existing Democracy",
        title_fa="بازاندیشی در حوزهٔ عمومی: سهمی در نقد دموکراسی واقعاً موجود",
        authors="Fraser, N.", year=1990,
        publisher="Social Text, 25/26, 56-80", doi=None, url=None, language="en", isbn=None,
        citation="Fraser, N. (1990). Rethinking the public sphere: A contribution to the critique of actually existing democracy. Social Text, 25/26, 56-80.",
        locator="pp. 56-80", locator_type="page_range", supports="mechanism / subaltern counterpublics", verified=False),
 ],
 "MC-215": [
   dict(kind="BOOK", title_en="Cosmopolitan Vision", title_fa="چشم‌انداز جهان‌وطنی",
        authors="Beck, U.", year=2006, publisher="Cambridge: Polity Press", doi=None,
        url="https://www.politybooks.com/bookdetail?book_slug=cosmopolitan-vision--9780745633985",
        language="en", isbn="9780745633985",
        citation="Beck, U. (2006). Cosmopolitan vision. Polity Press.",
        locator="whole work", locator_type="work", supports="definition / methodological cosmopolitanism", verified=True),
   dict(kind="JOURNAL_ARTICLE", title_en="The Cosmopolitan Society and Its Enemies",
        title_fa="جامعهٔ جهان‌وطن و دشمنانش", authors="Beck, U.", year=2002,
        publisher="Theory, Culture & Society, 19(1-2), 17-44", doi=None, url=None, language="en", isbn=None,
        citation="Beck, U. (2002). The cosmopolitan society and its enemies. Theory, Culture & Society, 19(1-2), 17-44.",
        locator="pp. 17-44", locator_type="page_range", supports="evolution / cosmopolitanization", verified=False),
 ],
}

ENRICH = {
 "MC-210": {
   "summary": "«میان‌بُرهای اطلاعاتی» (Informational Shortcuts) به نشانه‌ها و سرنخ‌های ساده‌ای اشاره دارد که شهروندان کم‌اطلاع با تکیه بر آن‌ها تصمیم سیاسی می‌گیرند و رفتاری نزدیک به رأی‌دهندگان آگاه از خود نشان می‌دهند. آرتور لوپیا در مطالعهٔ انتخابات اصلاح بیمهٔ کالیفرنیا (۱۹۹۴، APSR) نشان داد رأی‌دهندگان کم‌اطلاع با استفاده از سرنخ‌هایی مانند تأیید افراد مورد اعتماد، رفتار رأی‌دهندگان آگاه را «تقليد» می‌کنند (Lupia, 1994).",
   "main_problem": "اگر شهروندان به‌طور معمول اطلاعات کامل و دانشنامه‌ای از مسائل سیاسی ندارند، چگونه می‌توانند تصمیم‌های معقول بگیرند، و چه شرایطی باعث می‌شود میان‌بُرهای اطلاعاتی به‌جای گمراهی، تصمیم درست را ممکن کنند؟",
   "mechanism": "لوپیا در همه‌پرسی‌های اصلاح بیمهٔ خودرو در کالیفرنیا نشان داد که رأی‌دهندگانِ کم‌اطلاع، با تکیه بر «سرنخ‌های اطلاعاتی» — مانند موضع افراد و گروه‌های مورد اعتماد، نامزدهای کمیسر بیمه و سازمان‌های مصرف‌کننده — توانستند تا حدی مانند رأی‌دهندگان آگاه رأی دهند (Lupia, 1994). سازوکار سه‌گانه است: نخست، فرد یک «منبع سرنخ» (cue-giver) را برمی‌گزیند که به آن اعتماد دارد؛ دوم، موضع آن منبع را به‌عنوان راهنمای تصمیم خود به‌کار می‌گیرد؛ سوم، این میان‌بُر زمانی مؤثر است که منبع سرنخ هم قابل‌اعتماد باشد و هم منافعش با منافع رأی‌دهنده هم‌راستا باشد. پاپکین (Popkin, 1991) این منطق را «عقلانیت کم‌اطلاعات» (low-information rationality) نامید: شهروندان به‌جای انبار کردن دانش سیاسی، از سرنخ‌هایی مانند هویت حزبی، موضع گروه‌های ذی‌نفع و endorsement رسانه‌ای استفاده می‌کنند. در بستر رسانه، این نظریه نقش رسانه را از «انتقال اطلاعات کامل» به «فراهم‌کردن سرنخ‌های قابل‌اعتماد» تغییر می‌دهد: تأیید تحریریه، برچسب حزبی و موضع گروه‌های مورد اعتماد، میان‌بُرهایی‌اند که به شهروندان کم‌اطلاع امکان تصمیم‌گیری می‌دهند، اما در همان حال، آسیب‌پذیری آن‌ها را در برابر سرنخ‌های گمراه‌کننده و دستکاری‌شده افزایش می‌دهند.",
   "assumptions": [
     "شهروندان معمولاً دانش سیاسی کامل و دانشنامه‌ای ندارند.",
     "سرنخ‌های قابل‌اعتماد می‌توانند کمبود اطلاعات را جبران کنند.",
     "اثربخشی میان‌بُر به اعتبار منبع و هم‌راستایی منافع آن بستگی دارد."
   ],
   "principles": [
     "عقلانیت کم‌اطلاعات: تصمیم بر پایهٔ سرنخ، نه دانش کامل.",
     "انتخاب منبع سرنخ: رأی‌دهنده به افراد و گروه‌های مورد اعتماد تکیه می‌کند.",
     "شرط اثربخشی: منبع سرنخ باید قابل‌اعتماد و هم‌منافع باشد."
   ],
   "critiques": [
     "خطر گمراهی: سرنخ‌های نامعتبر یا دستکاری‌شده می‌توانند تصمیم را به‌شدت منحرف کنند.",
     "نابرابری منافع: منبع سرنخ ممکن است منافع متفاوتی از رأی‌دهنده داشته باشد.",
     "نادیده‌گرفتن محدودیت: میان‌بُرها جایگزین کامل دانش نیستند و در مسائل پیچیده کافی نیستند."
   ],
   "applications": [
     "تحلیل نقش endorsement و برچسب حزبی در تصمیم رأی‌دهنده.",
     "پژوهش دربارهٔ آسیب‌پذیری شهروندان کم‌اطلاع در برابر اطلاعات نادرست.",
     "طراحی ارتباطات عمومی برای ارائهٔ سرنخ‌های قابل‌اعتماد."
   ],
   "evolution": "پاپکین (1991) عقلانیت کم‌اطلاعات را صورت‌بندی کرد و لوپیا (1994) شواهد تجربی میان‌بُرها را ارائه داد. در دههٔ ۲۰۰۰-۲۰۱۰، پژوهش میان‌بُرها به رسانه‌های دیجیتال، سرنخ‌های آنلاین و آسیب‌پذیری در برابر دستکاری گسترش یافت.",
   "key_concepts": ["میان‌بُر اطلاعاتی (informational shortcut)", "عقلانیت کم‌اطلاعات (low-information rationality)", "منبع سرنخ (cue-giver)", "تأیید/endorsement", "جهل عقلانی (rational ignorance)"],
   "studies": ["Lupia, A. (1994). Shortcuts versus encyclopedias. APSR, 88(1), 63-76.", "Popkin, S. L. (1991). The Reasoning Voter. University of Chicago Press."],
 },
 "MC-213": {
   "summary": "«جامعهٔ مدنی جهانی» (Global Civil Society) به شبکهٔ پویا و فرامرزی نهادهای غیردولتی، جنبش‌ها و شبکه‌های اجتماعی اشاره دارد که بیرون از دولت و بازار عمل می‌کنند و در مسائل جهانی کنشگری می‌کنند. جان کین در «Global Civil Society?» (۲۰۰۳، Cambridge University Press) این ایده را به‌طور انتقادی بررسی و از آن دفاع کرد (Keane, 2003).",
   "main_problem": "آیا «جامعهٔ مدنی» را می‌توان از سطح ملی به سطح جهانی گسترد، این گسترش چه امکانات و چه محدودیت‌هایی دارد، و آیا نهادهای فرامرزی غیردولتی می‌توانند شکاف دموکراتیک جهانی را پر کنند؟",
   "mechanism": "کین جامعهٔ مدنی جهانی را نه یک نهاد یگانه، بلکه «مجموعه‌ای درهم‌تنیده از نهادهای اجتماعی-اقتصادی غیردولتی» می‌داند که از مرزها می‌گذرد: سازمان‌های غیردولتی، جنبش‌های اجتماعی، شبکه‌های حمایت‌گری (advocacy networks)، اتحادیه‌ها و انجمن‌های حرفه‌ای (Keane, 2003). او تأکید می‌کند که این حوزه یکپارچه نیست و شامل عناصر «غیرمدنی» (uncivil) نیز می‌شود؛ بنابراین «جامعهٔ مدنی جهانی» نه آرمانی همگن، بلکه میدانی متنازع است. سه سازوکار عمل آن را می‌توان بازشناخت: نخست، شبکه‌سازی فرامرزی که با زیرساخت ارتباطی و رسانه‌ای ممکن می‌شود؛ دوم، کارکرد نظارتی و حمایت‌گرانه در برابر قدرت‌های دولتی و شرکتی و شکل‌دادن به «افکار عمومی جهانی»؛ سوم، واسطه‌گری میان نهادهای جهانی و شهروندان محلی. آنهیر، گلاسیوس و کالدور (Anheier et al., 2001) کوشیدند این حوزه را به‌طور تجربی اندازه‌گیری کنند و نشان دادند که رشد سریع آن پس از پایان جنگ سرد، هم فرصت‌های دموکراتیک و هم مسائل نمایندگی و مشروعیت پدید آورده است. در بستر رسانه، نظریهٔ شبکه‌های حمایت‌گری فرامرزی توضیح می‌دهد چگونه کمپین‌های جهانی — از حقوق بشر تا محیط زیست — از طریق رسانه، نمادسازی و فشار عمومی، بر سیاست‌های فراملی اثر می‌گذارند و «افکار عمومی جهانی» را به‌عنوان نیرویی سیاسی فعال می‌کنند.",
   "assumptions": [
     "جامعهٔ مدنی را می‌توان از سطح ملی به سطح فراملی گسترد.",
     "شبکه‌های غیردولتی فرامرزی در مسائل جهانی کنشگر و اثرگذارند.",
     "این حوزه متنوع و متنازع است و شامل عناصر غیرمدنی نیز می‌شود."
   ],
   "principles": [
     "فرامرزی‌بودن: نهادهای غیردولتی از مرزهای ملی می‌گذرند.",
     "کارکرد نظارتی: جامعهٔ مدنی جهانی بر قدرت دولتی و شرکتی نظارت می‌کند.",
     "تنوع و تنازع: این حوزه یکپارچه نیست و دربرگیرندهٔ عناصر غیرمدنی است."
   ],
   "critiques": [
     "تسلط شمال: نهادهای جهانی جامعهٔ مدنی عمدتاً در کشورهای ثروتمند مستقر و منابع‌شان نامتوازن است.",
     "کسر نمایندگی: سازمان‌های غیردولتی پاسخ‌گویی روشنی به مخاطبان خود ندارند.",
     "اطلاعات‌گرایی: گرایش به حرفه‌ای‌شدن و NGO‌سازی، رادیکالیسم جنبشی را تضعیف می‌کند."
   ],
   "applications": [
     "تحلیل کمپین‌های جهانی و شبکه‌های حمایت‌گری فرامرزی.",
     "پژوهش دربارهٔ نقش رسانه در شکل‌دادن به افکار عمومی جهانی.",
     "بررسی مشروعیت و پاسخ‌گویی نهادهای غیردولتی فراملی."
   ],
   "evolution": "مفهوم در دههٔ ۱۹۹۰ با رشد سازمان‌های غیردولتی و جنبش‌های جهانی شکل گرفت؛ کین (2003) آن را به‌طور انتقادی صورت‌بندی کرد و آنهیر و همکاران (2001) به سنجش تجربی آن پرداختند. در دههٔ ۲۰۱۰-۲۰۲۰، کنشگری دیجیتال و شبکه‌های اجتماعی، شکل تازه‌ای به آن بخشید.",
   "key_concepts": ["جامعهٔ مدنی جهانی (global civil society)", "شبکهٔ حمایت‌گری فرامرزی (transnational advocacy network)", "افکار عمومی جهانی (global public opinion)", "جامعهٔ غیرمدنی (uncivil society)", "NGO‌سازی (NGOization)"],
   "studies": ["Keane, J. (2003). Global Civil Society? Cambridge University Press.", "Anheier, H., Glasius, M., & Kaldor, M. (2001). Introducing global civil society. In Global Civil Society 2001."],
 },
 "MC-214": {
   "summary": "«حوزهٔ عمومی فراملی» (Transnational Public Sphere) به گسترش فضای ارتباطی و گفت‌وگوی عمومی از سطح ملی به سطح فراملی اشاره دارد، جایی که افکار عمومی دربارهٔ مسائل فرامرزی شکل می‌گیرد و بر تصمیم‌های فراتر از مرزهای ملی اثر می‌گذارد. نانسی فریزر در «Transnationalizing the Public Sphere» (۲۰۰۷، Theory, Culture & Society) چارچوب وستفالیایی حوزهٔ عمومی را به چالش کشید (Fraser, 2007).",
   "main_problem": "وقتی تصمیم‌های سیاسی و اقتصادی از مرزهای ملی فراتر می‌روند، آیا حوزهٔ عمومی ملی می‌تواند مشروعیت و کارآمدی افکار عمومی را تأمین کند، و «حوزهٔ عمومی فراملی» چگونه باید مشروعیت و اثرگذاری خود را بسازد؟",
   "mechanism": "فریزر نشان می‌دهد که الگوی هابرماسی حوزهٔ عمومی در چارچوب «وستفالیایی» — یعنی درون مرزهای دولت-ملت — شکل گرفته و سه پرسش بنیادین را پیش می‌گذارد: چه کسانی حق مشارکت دارند (مسئلهٔ عضویت و مرز)، چه موضوعاتی «عمومی» شمرده می‌شوند (مسئلهٔ دستورکار)، و چگونه نظر عمومی به «افکار عمومی» مشروع و مؤثر بدل می‌شود (مسئلهٔ مشروعیت) (Fraser, 2007). او استدلال می‌کند که در جهان پساوستفالیایی، تصمیم‌ها بر کسانی اثر می‌گذارند که در فرایند تصمیم‌گیری حضور ندارند؛ بنابراین اصل مشروعیت باید از «اصل همهٔ متأثران» (all-affected principle) به «اصل همهٔ فرمان‌برداران» (all-subjected principle) گسترش یابد. فریزر با تکیه بر مفهوم پیشین خود «حوزه‌های عمومی فرعی/رقیب» (subaltern counterpublics) (Fraser, 1990) تأکید می‌کند که حوزهٔ عمومی یکپارچه نیست و گروه‌های حاشیه‌ای، فضای گفت‌وگوی موازی می‌سازند. حوزهٔ عمومی فراملی، در این معنا، نه یک فضای جهانی یکدست، بلکه مجموعه‌ای از عرصه‌های ارتباطی چندلایه است که با زیرساخت رسانه‌ای، ترجمه و شبکه‌های ارتباطی ممکن می‌شود. در بستر رسانه، این نظریه پرسش‌هایی دربارهٔ دموس جهانی، سلطهٔ زبان انگلیسی، نابرابری زیرساخت ارتباطی و امکان «افکار عمومی جهانی» مشروع پیش می‌گذارد و چارچوبی برای تحلیل پوشش فرامرزی مسائلی مانند تغییر اقلیم و حقوق بشر فراهم می‌کند.",
   "assumptions": [
     "چارچوب وستفالیایی حوزهٔ عمومی برای جهان فراملی کافی نیست.",
     "اثرگذاری تصمیم‌ها بر افراد بیرون از مرز، مسئلهٔ مشروعیت می‌سازد.",
     "حوزهٔ عمومی چندلایه و شامل عرصه‌های فرعی رقیب است."
   ],
   "principles": [
     "پساوستفالیایی: تصمیم‌ها از مرزهای ملی فراتر می‌روند.",
     "اصل همهٔ فرمان‌برداران: مشروعیت به کسانی تعلق دارد که تابع تصمیم‌اند.",
     "حوزه‌های فرعی: گروه‌های حاشیه‌ای فضای گفت‌وگوی موازی می‌سازند."
   ],
   "critiques": [
     "نبود دموس جهانی: نبود اجتماع سیاسی جهانی، مشروعیت دموکراتیک فراملی را مسئله‌دار می‌کند.",
     "نابرابری زبانی و زیرساختی: سلطهٔ انگلیسی و شکاف دیجیتال، مشارکت برابر را محدود می‌کند.",
     "آرمانی‌بودن: حوزهٔ عمومی فراملی بیش از آنکه واقعیتی نهادی باشد، افقی هنجاری است."
   ],
   "applications": [
     "تحلیل پوشش فرامرزی مسائل جهانی مانند تغییر اقلیم.",
     "پژوهش دربارهٔ رسانه‌های دیاسپورایی و عرصه‌های عمومی فرعی.",
     "نقد مشروعیت تصمیم‌گیری فراملی و افکار عمومی جهانی."
   ],
   "evolution": "هابرماس حوزهٔ عمومی را در چارچوب ملی صورت‌بندی کرد؛ فریزر (1990) با نقد آن، حوزه‌های فرعی را افزود و (2007) پرسش فراملی‌سازی را پیش گذاشت. در دههٔ ۲۰۱۰-۲۰۲۰، رسانه‌های دیجیتال و بحران‌های جهانی، بحث حوزهٔ عمومی فراملی را زنده نگه داشتند.",
   "key_concepts": ["حوزهٔ عمومی فراملی (transnational public sphere)", "چارچوب وستفالیایی (Westphalian frame)", "اصل همهٔ فرمان‌برداران (all-subjected principle)", "حوزهٔ عمومی فرعی (subaltern counterpublic)", "افکار عمومی (public opinion)"],
   "studies": ["Fraser, N. (2007). Transnationalizing the public sphere. Theory, Culture & Society, 24(4), 7-30.", "Fraser, N. (1990). Rethinking the public sphere. Social Text, 25/26, 56-80."],
 },
 "MC-215": {
   "summary": "«جهان‌وطنی» (Cosmopolitanism) در ارتباطات و علوم اجتماعی به نگرش و فرایندی اشاره دارد که شهروند را عضو جامعهٔ جهانی و نه فقط ملت-دولت می‌بیند. اولریش بک در «Cosmopolitan Vision» (۲۰۰۶، Polity) «جهان‌وطنی روش‌شناختی» را در برابر «ملی‌گرایی روش‌شناختی» قرار داد و فرایند «جهان‌وطنی‌شدن» را از آرمان هنجاری جهان‌وطنی تفکیک کرد (Beck, 2006).",
   "main_problem": "آیا جهان‌وطنی صرفاً یک آرمان اخلاقی است یا فرایندی واقعی که در زندگی روزمره، رسانه و مخاطرات جهانی رخ می‌دهد، و چگونه می‌توان از چارچوب ملی‌گرایانه در تحلیل اجتماعی و ارتباطی فراتر رفت؟",
   "mechanism": "بک دو سطح را از هم جدا می‌کند: «جهان‌وطنی» (cosmopolitanism) به‌عنوان پروژهٔ هنجاری و «جهان‌وطنی‌شدن» (cosmopolitanization) به‌عنوان فرایند واقعی و اغلب ناخواسته‌ای که در آن مرزهای ملی در زندگی روزمره درهم می‌آمیزند (Beck, 2006). او «ملی‌گرایی روش‌شناختی» (methodological nationalism) را نقد می‌کند — یعنی فرض بدیهی که جامعه و سیاست را در قالب ملت-دولت می‌بیند — و «جهان‌وطنی روش‌شناختی» را پیشنهاد می‌کند که هم ملی و هم فراملی را در یک چارچوب تحلیل می‌گیرد. سه سازوکار جهان‌وطنی‌شدن را می‌توان بازشناخت: نخست، «جهانی‌شدن از درون» (internal globalization) که در آن امر جهانی درون زندگی محلی نفوذ می‌کند؛ دوم، مخاطرات جهانی (مانند تغییر اقلیم و همه‌گیری) که آگاهی جهان‌وطنی و «لحظهٔ جهان‌وطنی» می‌سازند؛ سوم، «جهان‌وطنی پیش‌پاافتاده» (banal cosmopolitanism) که در مصرف روزمرهٔ رسانه، غذا و کالای فرهنگی تجربه می‌شود. در بستر رسانه، این نظریه توضیح می‌دهد چگونه مخاطبان با مصرف رسانه‌های فراملی، همدلی و آگاهی فراتر از مرزهای ملی می‌سازند، و چگونه خبر و سرگرمی جهانی می‌توانند هویت‌های «پیوندی» و هم‌زیستی جهان‌وطنی را تقویت کنند — هرچند جهان‌وطنی‌شدن، به‌سبب نابرابری دسترسی و قدرت، ناهموار و متنازع باقی می‌ماند.",
   "assumptions": [
     "جهان‌وطنی‌شدن فرایندی واقعی است، نه فقط آرمانی هنجاری.",
     "ملی‌گرایی روش‌شناختی در تحلیل اجتماعی محدودکننده است.",
     "مخاطرات جهانی و رسانه، آگاهی جهان‌وطنی می‌سازند."
   ],
   "principles": [
     "تفکیک آرمان و فرایند: جهان‌وطنی از جهان‌وطنی‌شدن جداست.",
     "جهان‌وطنی روش‌شناختی: تحلیل باید ملی و فراملی را در هم ببیند.",
     "جهان‌وطنی پیش‌پاافتاده: آگاهی جهانی در زندگی روزمره جاری است."
   ],
   "critiques": [
     "خوش‌بینی هنجاری: فرض گسترش همدلی جهانی، نابرابری قدرت و طرد را کم‌رنگ می‌کند.",
     "اروپامحوری: مفهوم جهان‌وطنی و شکل حقوقی آن، ریشه در تجربهٔ اروپایی دارد.",
     "نحیفی تجربی: شواهد تجربی دربارهٔ گسترش واقعی جهان‌وطنی‌شدن ناهمگون است."
   ],
   "applications": [
     "تحلیل مخاطبان رسانه‌های فراملی و همدلی فرامرزی.",
     "پژوهش دربارهٔ رسانه و هویت‌های جهان‌وطنی/پیوندی.",
     "نقد ملی‌گرایی روش‌شناختی در مطالعات ارتباطات."
   ],
   "evolution": "بک (2002) مفاهیم جهان‌وطنی‌شدن را پیش برد و (2006) آن را به «چشم‌انداز جهان‌وطنی» و «جهان‌وطنی روش‌شناختی» گسترد. در دههٔ ۲۰۱۰-۲۰۲۰، پژوهش رسانهٔ فراملی و همدلی جهانی، این چارچوب را برای تحلیل مخاطبان دیجیتال به کار گرفت.",
   "key_concepts": ["جهان‌وطنی (cosmopolitanism)", "جهان‌وطنی‌شدن (cosmopolitanization)", "ملی‌گرایی روش‌شناختی (methodological nationalism)", "مخاطرهٔ جهانی (global risk)", "جهان‌وطنی پیش‌پاافتاده (banal cosmopolitanism)"],
   "studies": ["Beck, U. (2006). Cosmopolitan Vision. Polity Press.", "Beck, U. (2002). The cosmopolitan society and its enemies. Theory, Culture & Society, 19(1-2), 17-44."],
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
    codes = ["MC-210", "MC-213", "MC-214", "MC-215"]
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
    print("BATCH51 THEORY DONE")

if __name__ == "__main__":
    main()
