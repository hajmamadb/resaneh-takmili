# -*- coding: utf-8 -*-
"""Batch 63 (THEORY): MC-328 News Framing (Entman 1993; Goffman 1974),
MC-330 Work of Art in the Age of Mechanical Reproduction (Benjamin 1968),
MC-331 One-Dimensional Man / Instrumental Rationality (Marcuse 1964),
MC-332 Communicative Action (Habermas 1981). Anchors verified 2026-11-16.
Rewrites the mismatched boilerplate critique/example found on all four records."""
import pymysql, json

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch63-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch63_theory.json"

S = {
 "MC-328": [
   dict(kind="JOURNAL_ARTICLE", title_en="Framing: Toward Clarification of a Fractured Paradigm",
        title_fa="چارچوب‌بندی: به‌سوی شفاف‌سازی یک پارادایم پراکنده",
        authors="Entman, R. M.", year=1993, publisher="Journal of Communication, 43(4), 51-58",
        doi="10.1111/j.1460-2466.1993.tb01304.x",
        url="https://academic.oup.com/joc/article-abstract/43/4/51/4160153",
        language="en", isbn=None,
        citation="Entman, R. M. (1993). Framing: Toward clarification of a fractured paradigm. Journal of Communication, 43(4), 51-58. https://doi.org/10.1111/j.1460-2466.1993.tb01304.x",
        locator="pp. 51-58", locator_type="page_range", supports="definition / selection and salience / four functions", verified=True),
   dict(kind="BOOK", title_en="Frame Analysis: An Essay on the Organization of Experience",
        title_fa="تحلیل چارچوب: جستاری در سازمان‌یابی تجربه",
        authors="Goffman, E.", year=1974, publisher="Cambridge, MA: Harvard University Press", doi=None, url=None,
        language="en", isbn=None,
        citation="Goffman, E. (1974). Frame analysis: An essay on the organization of experience. Harvard University Press.",
        locator="whole work", locator_type="work", supports="origin / frames as schemes of interpretation", verified=False),
 ],
 "MC-330": [
   dict(kind="BOOK_CHAPTER", title_en="The Work of Art in the Age of Mechanical Reproduction",
        title_fa="اثر هنری در عصر بازتولید مکانیکی",
        authors="Benjamin, W.", year=1968,
        publisher="In H. Arendt (Ed.), Illuminations (pp. 217-251). New York: Harcourt, Brace & World",
        doi=None, url="https://web.mit.edu/allanmc/www/benjamin.pdf", language="en", isbn=None,
        citation="Benjamin, W. (1968). The work of art in the age of mechanical reproduction. In H. Arendt (Ed.), Illuminations (pp. 217-251). Harcourt, Brace & World.",
        locator="pp. 217-251", locator_type="page_range", supports="definition / aura / cult and exhibition value", verified=True),
   dict(kind="JOURNAL_ARTICLE", title_en="Das Kunstwerk im Zeitalter seiner technischen Reproduzierbarkeit",
        title_fa="اثر هنری در عصر بازتولید تکنیکی آن",
        authors="Benjamin, W.", year=1936, publisher="Zeitschrift für Sozialforschung, 5(1), 40-68", doi=None, url=None,
        language="de", isbn=None,
        citation="Benjamin, W. (1936). Das Kunstwerk im Zeitalter seiner technischen Reproduzierbarkeit. Zeitschrift für Sozialforschung, 5(1), 40-68.",
        locator="pp. 40-68", locator_type="page_range", supports="origin / first published version", verified=False),
 ],
 "MC-331": [
   dict(kind="BOOK", title_en="One-Dimensional Man: Studies in the Ideology of Advanced Industrial Society",
        title_fa="انسان تک‌ساحتی: پژوهش‌هایی در ایدئولوژی جامعهٔ صناعتی پیشرفته",
        authors="Marcuse, H.", year=1964, publisher="Boston: Beacon Press", doi=None,
        url="https://www.marxists.org/ebooks/marcuse/one-dimensional-man.pdf",
        language="en", isbn=None,
        citation="Marcuse, H. (1964). One-dimensional man: Studies in the ideology of advanced industrial society. Beacon Press.",
        locator="whole work", locator_type="work", supports="definition / technological rationality / happy consciousness", verified=True),
   dict(kind="BOOK", title_en="Eros and Civilization: A Philosophical Inquiry into Freud",
        title_fa="اروس و تمدن: پژوهشی فلسفی در فروید",
        authors="Marcuse, H.", year=1955, publisher="Boston: Beacon Press", doi=None, url=None,
        language="en", isbn=None,
        citation="Marcuse, H. (1955). Eros and civilization: A philosophical inquiry into Freud. Beacon Press.",
        locator="whole work", locator_type="work", supports="evolution / surplus repression and performance principle", verified=False),
 ],
 "MC-332": [
   dict(kind="BOOK", title_en="Theorie des kommunikativen Handelns (2 vols.)",
        title_fa="نظریهٔ کنش ارتباطی (دو جلد)",
        authors="Habermas, J.", year=1981, publisher="Frankfurt am Main: Suhrkamp", doi=None,
        url="https://www.suhrkamp.de/buch/juergen-habermas-theorie-des-kommunikativen-handelns-t-9783518287750",
        language="de", isbn=None,
        citation="Habermas, J. (1981). Theorie des kommunikativen Handelns (Bd. 1-2). Suhrkamp.",
        locator="Bd. 1-2", locator_type="work", supports="definition / validity claims / system and lifeworld", verified=True),
   dict(kind="BOOK", title_en="The Structural Transformation of the Public Sphere: An Inquiry into a Category of Bourgeois Society",
        title_fa="دگرگونی ساختاری حوزهٔ عمومی: پژوهشی در مقولهٔ جامعهٔ بورژوایی",
        authors="Habermas, J.", year=1989, publisher="Cambridge, MA: MIT Press", doi=None, url=None,
        language="en", isbn=None,
        citation="Habermas, J. (1989). The structural transformation of the public sphere: An inquiry into a category of bourgeois society. MIT Press.",
        locator="whole work", locator_type="work", supports="evolution / public sphere and rational debate", verified=False),
 ],
}

ENRICH = {
 "MC-328": {
   "summary": "«چارچوب‌بندی خبر» (News Framing) می‌گوید رسانه واقعیت را نه بازتاب کامل، بلکه از دریچهٔ چارچوب‌هایی منتقل می‌کند که بخش‌هایی از رویداد را برجسته و بخش‌هایی را حذف می‌کنند. رابرت انتمن در «Framing: Toward Clarification of a Fractured Paradigm» (۱۹۹۳، Journal of Communication) تعریفی مضبوط از چارچوب ارائه داد و ریشهٔ مفهومی آن به «تحلیل چارچوب» اروینگ گافمن (۱۹۷۴) بازمی‌گردد (Entman, 1993).",
   "definition": "چارچوب‌بندی، گزینش جنبه‌هایی از واقعیت ادراک‌شده و برجسته‌سازی آن‌ها در متن است، به‌گونه‌ای که تعریف مسئله، تفسیر علت، داوری اخلاقی و توصیهٔ راه‌حل خاصی را ترویج کند (Entman, 1993).",
   "main_problem": "اگر خبر ادعای بی‌طرفی دارد، چگونه است که رسانه‌های متفاوت از یک رویداد واحد، روایت‌های متفاوت و گاه متناقض می‌سازند؛ و این تفاوت از کدام سازوکارهای گزینش و برجسته‌سازی برمی‌آید؟",
   "mechanism": "چارچوب‌بندی بر چهار کارکرد و چند سازوکار متنی عمل می‌کند. (۱) تعریف مسئله: چارچوب تعیین می‌کند چه چیزی «مسئله» است و چه چیزی زمینهٔ بی‌ربط؛ اعتراضی که «آسیب اقتصادی» نامیده شود، با همان اعتراضی که «بی‌نظمی عمومی» خوانده شود، مسیر سیاسی متفاوتی می‌گیرد. (۲) تشخیص علت: چارچوب، عامل را در فرد، ساختار یا محیط جست‌وجو می‌کند؛ انتساب علت به فرد یا به نظام، مسئولیت را جابه‌جا می‌کند. (۳) داوری اخلاقی: متن، کنشگران را قربانی، مقصر یا قهرمان می‌نامد و ارزیابی اخلاقی مخاطب را جهت می‌دهد. (۴) توصیهٔ راه‌حل: چارچوب، دامنهٔ راه‌حل‌های ممکن را محدود می‌کند؛ اگر مسئله «خطای فردی» تعریف شود، راه‌حل «آموزش» است و نه «تغییر سیاست». سازوکارهای متنی شامل عنوان، برجسته‌سازی آماری، انتخاب منبع، واژگان و تصویر است. در بستر رسانه، این چارچوب توضیح می‌دهد چرا پوشش یک اعتصاب کارگری می‌تواند بر «اختلال در ترافیک» یا بر «دستمزد ناعادلانه» متمرکز شود: هر دو گزارش از رویداد واحد، دو چارچوب رقیب و دو دستور کار سیاسی متفاوت می‌سازند. پژوهش‌های آینگار (۱۹۹۱) نیز نشان داد که چارچوب «رویدادمحور» (episodic) مسئولیت را فردی می‌کند و چارچوب «موضوع‌محور» (thematic) آن را به ساختار نسبت می‌دهد.",
   "assumptions": [
     "واقعیت خبری همیشه گزینش‌شده و برجسته‌شده است.",
     "چارچوب‌ها در متن قابل شناسایی‌اند و بر تفسیر مخاطب اثر می‌گذارند.",
     "چهار کارکرد تعریف مسئله، علت، داوری و راه‌حل، ساختار چارچوب را می‌سازند."
   ],
   "principles": [
     "چارچوب‌بندی، گزینش و برجسته‌سازی است، نه دروغ‌گویی.",
     "هر چارچوب، دامنهٔ راه‌حل‌های ممکن را محدود می‌کند.",
     "چارچوب‌ها رقیب‌اند و در میدان عمومی با هم مبارزه می‌کنند."
   ],
   "critiques": [
     "گسترش مفهومی: چارچوب‌بندی به مفهومی چنان فراگیر بدل شده که گاه با ایدئولوژی، طرح‌وارهٔ ذهنی و دستور کار یکسان گرفته می‌شود؛ خود انتمن این «پارادایم پراکنده» را مشکل اصلی دانست.",
     "مسئلهٔ سنجش: شناسایی و اندازه‌گیری چارچوب، به داوری پژوهشگر وابسته است و بازتولید یافته‌ها را دشوار می‌کند.",
     "اثر بر مخاطب: وجود چارچوب در متن، به‌خودی‌خود اثبات اثر بر مخاطب نیست؛ مخاطبان با طرح‌واره‌های پیشین خود چارچوب‌ها را تفسیر و تعدیل می‌کنند."
   ],
   "applications": [
     "تحلیل تطبیقی پوشش خبری یک رویداد در رسانه‌های رقیب.",
     "پژوهش دربارهٔ چارچوب‌بندی سلامت، مهاجرت و تغییر اقلیم.",
     "آموزش سواد رسانه‌ای برای شناسایی چارچوب‌های پنهان.",
     "طراحی پیام در روابط عمومی و کمپین با آگاهی از چارچوب رقیب."
   ],
   "evolution": "گافمن (۱۹۷۴) مفهوم چارچوب را در جامعه‌شناسی تجربه معرفی کرد؛ انتمن (۱۹۹۳) آن را برای پژوهش رسانه مضبوط کرد؛ گیتلین (۱۹۸۰) و آینگار (۱۹۹۱) تحلیل چارچوب در خبر و اثر آن را گستردند و امروز چارچوب‌بندی یکی از پرکاربردترین مفاهیم ارتباطات سیاسی است.",
   "key_concepts": ["چارچوب (frame)", "برجسته‌سازی (salience)", "تعریف مسئله (problem definition)", "انتساب علت (causal attribution)", "چارچوب رویدادمحور و موضوع‌محور (episodic/thematic)", "دستور کار (agenda)"],
   "studies": ["Entman, R. M. (1993). Framing: Toward clarification of a fractured paradigm. Journal of Communication, 43(4), 51-58.", "Goffman, E. (1974). Frame analysis: An essay on the organization of experience. Harvard University Press."],
   "detailed_analysis": "۱. بنیان و منطق نظری\nچارچوب‌بندی از این واقعیت آغاز می‌شود که هیچ گزارشی نمی‌تواند همهٔ واقعیت را حمل کند. خبر ناچار انتخاب می‌کند و هر انتخاب، معنایی می‌سازد. انتمن همین را به تعریفی عملیاتی بدل کرد: گزینش و برجسته‌سازی، به‌همراه چهار کارکردی که چارچوب را از «موضوع» متمایز می‌کند.\n\n۲. چارچوب در برابر دستور کار\nدستور کار می‌گوید «چه چیزی مهم است»؛ چارچوب می‌گوید «آن چیز چگونه فهمیده شود». یک موضوع می‌تواند در دستور کار همهٔ رسانه‌ها باشد و در هر یک، چارچوب متفاوتی بگیرد؛ همین تفکیک، ارزش تحلیلی مفهوم را می‌سازد.\n\n۳. پیوند رسانه‌ای و نقد\nدر محیط خبری امروز، چارچوب‌ها نه فقط در متن، بلکه در سرتیتر algorithmic و انتخاب تصویر بازتولید می‌شوند. نقد اصلی بر پژوهش چارچوب، مسئلهٔ سنجش است: اگر چارچوب را پژوهشگر تعریف کند، خطر آن هست که یافته، بازتاب پیش‌فرض او باشد. راه‌حل، شفاف‌سازی معیارهای کدگذاری و آزمون چند پژوهشگر است.",
   "critique_text": "\n".join([
     "۱. گسترش مفهومی: چارچوب‌بندی گاه با ایدئولوژی، طرح‌وارهٔ ذهنی و دستور کار یکی گرفته می‌شود و همین، «پارادایم پراکنده»ای ساخته که خود انتمن هشدار داده بود.",
     "۲. مسئلهٔ سنجش: شناسایی چارچوب به داوری پژوهشگر وابسته است و بدون معیار شفاف، بازتولید یافته دشوار می‌شود.",
     "۳. شکاف متن و اثر: وجود چارچوب در متن، اثبات تأثیر آن بر مخاطب نیست؛ مخاطبان با طرح‌واره‌های پیشین، چارچوب را تفسیر و تعدیل می‌کنند."]),
   "example_text": "دو گزارش از یک اعتصاب کارگری: یکی با عنوان «اختلال در خطوط حمل‌ونقل» و تمرکز بر هزینهٔ اقتصادی، دیگری با عنوان «دستمزد ناعادلانه» و تمرکز بر شرایط کارگران. هر دو از رویداد واحد گزارش می‌دهند، اما چارچوب اول مسئله را «بی‌نظمی» و راه‌حل را «برخورد انتظامی» تعریف می‌کند و چارچوب دوم مسئله را «بی‌عدالتی» و راه‌حل را «مذاکره» می‌بیند.",
 },
 "MC-330": {
   "summary": "والتر بنیامین در «اثر هنری در عصر بازتولید مکانیکی» استدلال می‌کند که تکثیر تکنیکی، «هاله» اثر هنری — یعنی یکتایی، اصالت و اقتدار مناسکی آن — را فرومی‌ریزد و در همان حال، امکان دسترسی توده‌ای و سیاسی‌شدن هنر را فراهم می‌کند. این جستار که نخست در ۱۹۳۶ منتشر شد و در «Illuminations» (۱۹۶۸) در دسترس انگلیسی‌زبانان قرار گرفت، بنیان نظریهٔ رسانهٔ انتقادی است (Benjamin, 1968).",
   "definition": "هاله، ویژگی یکتایی و اصالت اثری است که در مکان و زمان معین حضور دارد و اقتدار مناسکی‌اش را از همین یکتایی می‌گیرد؛ بازتولید مکانیکی، این یکتایی را از اثر جدا می‌کند و معنا و کارکرد آن را دگرگون می‌سازد (Benjamin, 1968).",
   "main_problem": "وقتی اثر هنری به‌طور نامحدود تکثیر می‌شود، چه چیزی از آن باقی می‌ماند؛ و این دگرگونی، چه پیامدهایی برای سیاست، ادراک و تجربهٔ زیبایی‌شناختی دارد؟",
   "mechanism": "تحلیل بنیامین بر پنج سازوکار استوار است. (۱) فروپاشی هاله: بازتولید، اثر را از «اینجا و اکنونِ» یگانه‌اش جدا می‌کند؛ نسخهٔ بازتولیدشده هر جا حاضر است و در نتیجه، اقتدار و فاصلهٔ مناسکی اثر از میان می‌رود. (۲) حرکت از ارزش مناسکی به ارزش نمایشی: هنر پیشامدرن در خدمت آیین بود و ارزش آن در پنهان‌بودن و تقدس؛ با بازتولید، معیار به «قابل نمایش بودن» تغییر می‌کند و اثر به سمت توده حرکت می‌کند. (۳) دگرگونی ادراک: رسانهٔ جدید، حس توده‌ای را بازآرایی می‌کند؛ فیلم با مونتاژ، ضربه و حرکت، ادراکی حسی-حرکتی می‌سازد که با تأمل آرام در برابر نقاشی متفاوت است. (۴) دموکراتیک‌شدن و خطر هم‌زمان: تکثیر، دسترسی را گسترده می‌کند و امکان مشارکت توده در فرهنگ را می‌دهد، اما همان توده، در معرض زیبایی‌شناسی‌شدن سیاست قرار می‌گیرد. (۵) دو راه سیاست: فاشیسم، سیاست را زیبایی‌شناختی می‌کند و جنگ را به نمایش بدل می‌سازد؛ کمونیسم، هنر را سیاسی می‌کند. این تقابل، تز پایانی جستار است. در بستر رسانه، این چارچوب برای تحلیل عکس خبری، پخش زنده، بازنشر بی‌پایان تصویر در شبکه‌های اجتماعی و «تجربهٔ حضور» در کنسرت و ورزشگاه به‌کار می‌رود: هر جا نسخهٔ بی‌شمار در دسترس است و باز هم مخاطب برای «اصل» هزینه می‌کند، در واقع اثر هاله در حال بازسازی است.",
   "assumptions": [
     "اثر هنری، اقتدار خود را از یکتایی و حضور آیینی می‌گیرد.",
     "فناوری بازتولید، نه فقط واسطه، بلکه شکل ادراک را تغییر می‌دهد.",
     "دگرگونی فنی هنر، پیامدهای سیاسی دارد."
   ],
   "principles": [
     "بازتولید، هاله را از اثر جدا می‌کند.",
     "معیار ارزش از مناسکی به نمایشی حرکت می‌کند.",
     "رسانهٔ توده‌ای هم رهایی‌بخش و هم مستعد کنترل است."
   ],
   "critiques": [
     "مفهوم هاله مبهم و رمانتیک است و معلوم نیست دقیقاً چه چیزی از اثر می‌رود؛ منتقدان می‌گویند بنیامین نوستالژی پیشامدرن را با تحلیل فنی درهم می‌آمیزد.",
     "تحلیل، بازار و صنعت فرهنگ را کم‌رنگ می‌بیند: آدورنو در نامهٔ ۱۹۳۶ خود به بنیامین هشدار داد که فناوری را بیش از حد بی‌طرف و «مترقی» فرض کرده و دیالکتیک سلطه و رهایی را نادیده گرفته است.",
     "مخاطب توده‌ای در تحلیل، بیشتر یک مقولهٔ جمعی است تا کنشگری مفسر؛ پژوهش‌های بعدی دربارهٔ مصرف و تفسیر، این خلأ را پر کردند."
   ],
   "applications": [
     "تحلیل عکس خبری و اعتبار «بودن در محل».",
     "پژوهش دربارهٔ بازنشر تصویر و بازسازی هاله در شبکه‌های اجتماعی.",
     "نقد اقتصاد «تجربهٔ زنده» در کنسرت، تئاتر و ورزش.",
     "تحلیل زیبایی‌شناسی‌شدن سیاست در تبلیغات و پروپاگاندا."
   ],
   "evolution": "جستار در ۱۹۳۶ منتشر شد و پس از ترجمه در «Illuminations» (۱۹۶۸) به یکی از متون بنیادی مطالعات رسانه بدل شد؛ مکتب فرانکفورت آن را با نقد صنعت فرهنگ پیوند داد و در دههٔ اخیر، بحث «هالهٔ دیجیتال» و «اصالت در عصر بازنشر» آن را دوباره زنده کرده است.",
   "key_concepts": ["هاله (aura)", "اصالت (authenticity)", "ارزش مناسکی و نمایشی (cult/exhibition value)", "بازتولید مکانیکی (mechanical reproduction)", "سیاسی‌شدن هنر (politicization of art)", "زیبایی‌شناسی‌شدن سیاست (aestheticization of politics)"],
   "studies": ["Benjamin, W. (1968). The work of art in the age of mechanical reproduction. In Illuminations (pp. 217-251). Harcourt, Brace & World.", "Benjamin, W. (1936). Das Kunstwerk im Zeitalter seiner technischen Reproduzierbarkeit. Zeitschrift für Sozialforschung, 5(1), 40-68."],
   "detailed_analysis": "۱. بنیان و منطق نظری\nبنیامین می‌خواست نشان دهد که تحول فنی هنر، فقط تغییر وسیله نیست؛ رابطهٔ اثر با آیین، سنت و اقتدار را دگرگون می‌کند. هاله، نام همان رابطه است: اثر در جایی و زمانی یگانه است و همین یگانگی، اقتدارش را می‌سازد.\n\n۲. دو پیامد هم‌زمان\nفروپاشی هاله، هم رهایی است و هم خطر: رهایی، زیرا دسترسی از انحصار خارج می‌شود؛ خطر، زیرا تودهٔ بی‌هاله، آمادهٔ زیبایی‌شناسی‌شدن سیاست است. بنیامین این دو را در برابر هم می‌گذارد و خواننده را با انتخاب روبه‌رو می‌کند، نه با پیش‌بینی.\n\n۳. پیوند رسانه‌ای و نقد\nدر عصر بازنشر دیجیتال، هاله بازسازی می‌شود: نسخهٔ بی‌شمار در دسترس است، اما مخاطب برای «حضور در محل» هزینه می‌کند. نقد آدورنو همچنان مهم است: اگر فناوری را بی‌طرف فرض کنیم، صنعت فرهنگ را از دست می‌دهیم. بنیامین این را می‌دانست، اما پاسخش به آن، وعدهٔ سیاسی است، نه تحلیل اقتصادی.",
   "critique_text": "\n".join([
     "۱. ابهام «هاله»: روشن نیست هاله دقیقاً چه چیزی است و چه اندازه از آن با بازتولید از میان می‌رود؛ مفهوم، شهودی و ادبی است، نه قابل سنجش.",
     "۲. نقد آدورنو (نامهٔ ۱۹۳۶): بنیامین فناوری را بیش از حد مترقی و بی‌طرف فرض کرده و دیالکتیک سلطه و رهایی در صنعت فرهنگ را نادیده گرفته است.",
     "۳. غیبت مخاطب مفسر: توده در تحلیل، مقوله‌ای جمعی و تا حدی منفعل است؛ عاملیت تفسیری مخاطب در نظریهٔ او جای چندانی ندارد."]),
   "example_text": "یک عکس خبری از یک رویداد، وقتی در هزاران بازنشر دیده می‌شود، «حضور» خود را از دست می‌دهد و به نشانه‌ای در گردش بدل می‌شود؛ اما همان رسانه برای «عکس اختصاصی» یا حضور خبرنگار در محل هزینه می‌کند. این تنش، دقیقاً همان بازسازی هاله در عصر بازتولید است.",
 },
 "MC-331": {
   "summary": "«انسان تک‌ساحتی» (One-Dimensional Man) هربرت مارکوزه تحلیل انتقادی جامعهٔ صناعتی پیشرفته است: نظام، با تولید نیازهای کاذب، رفاه و «عقلانیت تکنولوژیک»، نیروهای مخالف را در خود جذب می‌کند و انسان را به موجودی تک‌بعدی — بی‌توان در نفی و تخیل رادیکال — بدل می‌سازد (Marcuse, 1964).",
   "definition": "عقلانیت ابزاری، صورت عقلانیتی است که کارآمدی و کنترل فنی را معیار همهٔ امور می‌کند و ارزش‌ها، اهداف و روابط اجتماعی را به مسئلهٔ «بهینه‌سازی» فرو می‌کاهد؛ انسان تک‌ساحتی، سوژه‌ای است که در همین چارچوب می‌اندیشد و بدیل را تصور نمی‌کند (Marcuse, 1964).",
   "main_problem": "چگونه جامعهٔ صناعتی پیشرفته، با وجود رفاه و آزادی‌های صوری، صورتی نو از سلطه می‌سازد که نه با سرکوب آشکار، بلکه با ارضای نیازهای مدیریت‌شده و جذب مخالفت عمل می‌کند؟",
   "mechanism": "تحلیل مارکوزه بر پنج سازوکار استوار است. (۱) نیازهای کاذب: نظام نیازهایی تولید می‌کند که ارضای آن‌ها به بقای نظام کمک می‌کند، نه به رهایی فرد؛ مصرف، به جای ابزار زندگی، به هدف زندگی بدل می‌شود. (۲) جذب مخالفت: نیروهای رادیکال — کارگر، روشنفکر، حزب — در ساختار رفاه و مصرف ادغام می‌شوند و تضاد طبقاتی از صورت سیاسی خود تهی می‌گردد. (۳) عقلانیت تکنولوژیک: کارآمدی فنی، معیار مشروعیت می‌شود و پرسش از هدف و ارزش، «غیرعلمی» و «احساسی» تلقی می‌گردد؛ سلطه، در قالب مدیریت و کارشناسی عمل می‌کند. (۴) واپس‌رانی سرکوب‌گر: مارکوزه نشان می‌دهد که آزادی جنسی و فرهنگی، به‌جای رهایی، به کانالی برای تخلیهٔ انرژی اعتراض بدل می‌شود؛ همین ایده، بعدها با مفهوم «واپس‌رانی سرکوب‌گر» (repressive desublimation) شناخته شد. (۵) آگاهی خوش‌بین: فرد، وضع موجود را «عقلانی» و بدیل را «غیرواقع‌بینانه» می‌بیند؛ نتیجه، زوال توان نفی است. در بستر رسانه، این چارچوب در نقد سرگرمی، تبلیغات و «فرهنگ مصرف» به‌کار می‌رود: پلتفرم‌ها با شخصی‌سازی، آزادی انتخاب را به آزادی انتخاب از میان گزینه‌های از پیش تعیین‌شده فرومی‌کاهند و اعتراض را نیز به قالب محتوایی و ترند تبدیل می‌کنند.",
   "assumptions": [
     "نیازهای مصرفی می‌توانند ساختهٔ نظام باشند و رهایی فرد را به تعویق اندازند.",
     "کارآمدی فنی، به‌تنهایی نمی‌تواند معیار مشروعیت باشد.",
     "سلطهٔ مدرن، بیشتر با ادغام و مدیریت عمل می‌کند تا با سرکوب آشکار."
   ],
   "principles": [
     "رفاه می‌تواند شکل نوینی از سلطه باشد.",
     "عقلانیت ابزاری، پرسش از هدف را از میدان عمومی بیرون می‌کند.",
     "توان نفی، شرط آزادی است."
   ],
   "critiques": [
     "تشخیص «تک‌بعدی‌شدن» بیش از حد کلی و آزمون‌ناپذیر است و تفاوت‌های طبقه، نژاد، جنسیت و بافت ملی را نادیده می‌گیرد.",
     "ترسیم مخاطب به‌عنوان سوژهٔ منفعل و فریب‌خورده، عاملیت تفسیری و مقاومت روزمره را کم‌رنگ می‌کند.",
     "مارکوزه خود در «جستاری در رهایی» (۱۹۶۹) با ظهور جنبش‌های دانشجویی و ضدجنگ، بخشی از پیش‌بینی خود را تجدید نظر کرد و امکان نفی را دوباره دید."
   ],
   "applications": [
     "نقد فرهنگ مصرف و تبلیغات تجاری.",
     "تحلیل شخصی‌سازی الگوریتمی به‌عنوان محدودسازی انتخاب.",
     "پژوهش دربارهٔ جذب اعتراض در رسانه‌های شبکه‌ای.",
     "نقد زبان مدیریتی و کارشناسی در سیاست‌گذاری رسانه."
   ],
   "evolution": "مارکوزه (۱۹۶۴) تحلیل را در اوج جنگ سرد و جامعهٔ رفاهی آمریکا نوشت؛ در ۱۹۶۹ با «جستاری در رهایی» آن را تعدیل کرد و در دههٔ ۱۹۷۰ نسل نقد رسانه‌ای بر او تکیه کرد. امروز، بحث «سرمایه‌داری نظارتی» و «کالایی‌شدن توجه» وارث همین چارچوب است.",
   "key_concepts": ["انسان تک‌ساحتی (one-dimensional man)", "عقلانیت ابزاری (instrumental rationality)", "نیاز کاذب (false need)", "واپس‌رانی سرکوب‌گر (repressive desublimation)", "آگاهی خوش‌بین (happy consciousness)", "توان نفی (negative thinking)"],
   "studies": ["Marcuse, H. (1964). One-dimensional man. Beacon Press.", "Marcuse, H. (1955). Eros and civilization. Beacon Press."],
   "detailed_analysis": "۱. بنیان و منطق نظری\nمارکوزه تحلیل هگلی-فرویدی خود را بر یک پرسش بنا کرد: چرا در جامعه‌ای که ابزار مادی رهایی فراهم است، رهایی رخ نمی‌دهد؟ پاسخ او، ترکیبی از اقتصاد سیاسی و روان‌کاوی بود: نظام، نیاز می‌سازد و اعتراض را تخلیه می‌کند.\n\n۲. چرا هنوز خوانده می‌شود\nزبان مارکوزه برای توصیف پدیده‌های امروز کارآمد است: «آزادی انتخاب» میان گزینه‌های الگوریتمی، و تبدیل اعتراض به ترند. اما همین کارآمدی، دام او نیز هست: هر پدیده‌ای را می‌توان مصداق «ادغام» خواند، بی‌آنکه ادعا ابطال‌پذیر شود.\n\n۳. پیوند رسانه‌ای و نقد\nنقد مارکوزه به ما یادآوری می‌کند که پرسش «آیا این رسانه کارآمد است؟» کافی نیست؛ باید پرسید «کارآمد برای چه هدفی و برای چه کسی؟». اما پاسخ او، مخاطب را بیش از اندازه منفعل می‌بیند و همین، نقطهٔ ورود پژوهش‌های بعدی دربارهٔ تفسیر و مقاومت است.",
   "critique_text": "\n".join([
     "۱. آزمون‌ناپذیری: تشخیص «تک‌بعدی‌شدن» چنان کلی است که هر شاهد را می‌توان تأیید آن خواند؛ تفاوت‌های طبقه، نژاد و بافت ملی نیز نادیده گرفته می‌شود.",
     "۲. مخاطب منفعل: تحلیل، سوژه را فریب‌خورده و بی‌عاملیت ترسیم می‌کند و مقاومت روزمره و تفسیر رقیب را کم‌رنگ می‌سازد.",
     "۳. تجدید نظر خود نویسنده: مارکوزه در «جستاری در رهایی» (۱۹۶۹) با دیدن جنبش‌های دانشجویی، امکان نفی را بازبینی کرد — نشانهٔ آنکه تشخیص ۱۹۶۴، تاریخی و موقت بود."]),
   "example_text": "پلتفرمی که به کاربر «آزادی انتخاب» میان هزاران ویدئوی پیشنهادی می‌دهد، در واقع دامنهٔ انتخاب را از پیش تعیین کرده است؛ همان سازوکاری که مارکوزه «آزادی در چارچوب مدیریت‌شده» می‌نامید. اعتراض کاربران نیز، با تبدیل به ترند و محتوا، در همان چرخه جذب می‌شود.",
 },
 "MC-332": {
   "summary": "«کنش ارتباطی» (Communicative Action) نظریهٔ یورگن هابرماس است که کنش معطوف به تفاهم را در برابر کنش ابزاری و استراتژیک قرار می‌دهد و نشان می‌دهد که «زیست‌جهان» چگونه با ورود پول و قدرت به‌عنوان رسانه‌های سیستمی، مستعمره می‌شود. این نظریه در «Theorie des kommunikativen Handelns» (۱۹۸۱، Suhrkamp) صورت‌بندی شد (Habermas, 1981).",
   "definition": "کنش ارتباطی، کنشی است که کنشگران در آن با زبان، به‌جای اعمال قدرت یا مبادله، به دنبال تفاهم مشترک دربارهٔ موقعیت و برنامهٔ عمل‌اند و در آن سه ادعای اعتبار — درستی، صحت و صداقت — به‌طور ضمنی مطرح و قابل نقد می‌شود (Habermas, 1981).",
   "main_problem": "چگونه می‌توان در جامعه‌ای که سیستم (بازار و دولت) با پول و قدرت آن را هماهنگ می‌کند، فضایی برای هماهنگی مبتنی بر تفاهم و استدلال عمومی حفظ کرد و از استعمار زیست‌جهان جلوگیری کرد؟",
   "mechanism": "نظریه بر پنج سازوکار استوار است. (۱) تفکیک کنش: کنش ابزاری به موفقیت و کنترل نظر دارد، کنش استراتژیک به تأثیر بر دیگری برای رسیدن به هدف، و کنش ارتباطی به تفاهم؛ تنها نوع سوم، امکان هماهنگی بدون اجبار را می‌دهد. (۲) ادعاهای اعتبار: هر گفتار فهم‌پذیر، سه ادعای ضمنی دارد — حقیقت گزاره، درستی هنجار و صداقت گوینده؛ این ادعاها قابل نقد و دفاع‌اند و همین، عقلانیت ارتباطی را می‌سازد. (۳) زیست‌جهان: مخزن پیش‌فهم‌های مشترک (فرهنگ، جامعه و شخصیت) که کنش ارتباطی از آن تغذیه می‌کند و آن را بازتولید می‌کند. (۴) سیستم و رسانه‌های سیستمی: بازار با پول و دولت با قدرت، کنش‌ها را هماهنگ می‌کنند؛ این رسانه‌ها کارآمدند اما نسبت به معنا بی‌اعتنا هستند. (۵) استعمار زیست‌جهان: وقتی منطق پول و بوروکراسی به حوزه‌های تفاهم — خانواده، مدرسه، رسانه و حوزهٔ عمومی — نفوذ کند، معنا به‌جای تفاهم، با «قدرت خرید» و «مقررات» تولید می‌شود. در بستر رسانه، این چارچوب امکان نقد «رسانهٔ بازارمحور» را می‌دهد: وقتی خبر به کالا و مخاطب به داده بدل شود، منطق سیستم جای منطق تفاهم را می‌گیرد و بحث عمومی به رقابت برای جلب توجه فرومی‌کاهد. در برابر، رسانهٔ خدمت عمومی و روزنامه‌نگاری حرفه‌ای می‌توانند فضایی برای ادعاهای اعتبار و نقد عمومی بسازند.",
   "assumptions": [
     "زبان، به‌طور درونی، امکان تفاهم بدون اجبار را در خود دارد.",
     "هر گفتار فهم‌پذیر، ادعاهای اعتبار قابل نقد را مطرح می‌کند.",
     "زیست‌جهان و سیستم دو منطق متفاوت هماهنگی‌اند که می‌توانند در تعارض قرار گیرند."
   ],
   "principles": [
     "تفاهم، به‌جای موفقیت، معیار کنش ارتباطی است.",
     "عقلانیت ارتباطی در نقدپذیری ادعاهای اعتبار نهفته است.",
     "نفوذ پول و قدرت در زیست‌جهان، آن را مستعمره می‌کند."
   ],
   "critiques": [
     "ایده‌آل‌سازی تفاهم: نظریه، وضعیت گفت‌وگوی آزاد از قدرت را پیش‌فرض می‌گیرد، در حالی که نابرابری‌های ساختاری در خود گفت‌وگو حضور دارند.",
     "تفکیک دوگانه: مرز زیست‌جهان و سیستم بسیار صُلب است و پدیده‌های میانی (رسانه، سازمان، پلتفرم) را نمی‌توان به‌راحتی در یکی از دو دسته جای داد.",
     "نقد فمینیستی و پسااستعماری: فرِیزر (۱۹۹۰) نشان داد حوزهٔ عمومی بورژوایی، نابرابری‌ها را پنهان می‌کند و حوزهٔ عمومی بدیل و رقیب را نادیده می‌گیرد."
   ],
   "applications": [
     "نقد رسانهٔ بازارمحور و تجاری‌شدن خبر.",
     "تحلیل گفت‌وگوی عمومی و کیفیت استدلال در فضای شبکه‌ای.",
     "طراحی رسانهٔ خدمت عمومی و اصول حرفه‌ای روزنامه‌نگاری.",
     "پژوهش دربارهٔ اخلاق گفت‌وگو و مشروعیت تصمیم عمومی."
   ],
   "evolution": "هابرماس (۱۹۸۱) نظریه را در دو جلد منتشر کرد و در «میان واقعیت و هنجار» (۱۹۹۲) آن را به حقوق و دموکراسی گستراند؛ نقد فرِیزر (۱۹۹۰) و بحث «حوزهٔ عمومی دیجیتال» پاسخ‌های انتقادی مهمی به آن‌اند.",
   "key_concepts": ["کنش ارتباطی (communicative action)", "ادعای اعتبار (validity claim)", "زیست‌جهان (lifeworld)", "سیستم (system)", "رسانه‌های سیستمی (steering media)", "استعمار زیست‌جهان (colonization of the lifeworld)", "حوزهٔ عمومی (public sphere)"],
   "studies": ["Habermas, J. (1981). Theorie des kommunikativen Handelns (Bd. 1-2). Suhrkamp.", "Habermas, J. (1989). The structural transformation of the public sphere. MIT Press."],
   "detailed_analysis": "۱. بنیان و منطق نظری\nهابرماس می‌خواست نظریهٔ انتقادی را بر پایه‌ای غیر از تاریخ‌مندی رادیکال بازسازی کند: عقلانیت نه فقط ابزاری، بلکه ارتباطی است و در ساختار زبان ریشه دارد. از همین‌جا، معیاری برای نقد جامعه به دست می‌آید: آیا حوزه‌های تفاهم، به منطق پول و قدرت تسلیم شده‌اند؟\n\n۲. دو مفهوم کلیدی\nزیست‌جهان، زمینهٔ نادیده‌گرفته‌شدهٔ معناست و سیستم، سازوکار هماهنگی کارآمد. مسئله این نیست که یکی خوب و دیگری بد است؛ مسئله این است که منطق یکی، در قلمرو دیگری عمل کند.\n\n۳. پیوند رسانه‌ای و نقد\nدر محیط پلتفرمی، همان نقد زنده است: تعامل کاربر با منطق تبلیغات سنجیده می‌شود و کیفیت گفت‌وگو به معیار ثانویه بدل می‌شود. نقد فرِیزر نیز مهم است: پیش از پرسش از استعمار سیستم، باید پرسید چه کسانی در حوزهٔ عمومی اصلاً حضور دارند و چه کسانی از آن حذف شده‌اند.",
   "critique_text": "\n".join([
     "۱. ایده‌آل‌سازی گفت‌وگو: نظریه، موقعیت گفت‌وگوی آزاد از قدرت را پیش‌فرض می‌گیرد، در حالی که نابرابری‌های ساختاری در خود زبان و دسترسی حضور دارند.",
     "۲. دوگانهٔ صُلب سیستم/زیست‌جهان: پدیده‌های میانی مانند رسانه، سازمان و پلتفرم به‌سختی در یکی از دو دسته جای می‌گیرند.",
     "۳. نقد فرِیزر (۱۹۹۰): حوزهٔ عمومی بورژوایی، نابرابری‌های جنسیتی و طبقاتی را پنهان می‌کند و حوزه‌های عمومی بدیل را نادیده می‌گیرد."]),
   "example_text": "وقتی یک رسانه برای افزایش تعامل، تیتر را به‌گونه‌ای بازنویسی می‌کند که خشم مخاطب را برانگیزد، منطق سیستم (سنجش توجه و درآمد) در قلمرو زیست‌جهان (تفاهم و گفت‌وگوی عمومی) عمل کرده است؛ اعتماد مخاطب، هزینهٔ این استعمار است.",
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
    codes = ["MC-328", "MC-330", "MC-331", "MC-332"]
    cur.execute("SELECT id, code, properties FROM kb_entities WHERE code IN (%s)" % ",".join(["%s"]*len(codes)), codes)
    rows = {code:(eid, json.loads(pr)) for (eid, code, pr) in cur.fetchall()}
    with open(BACKUP, "w", encoding="utf-8") as f:
        json.dump([{"code": cd, "props": rows[cd][1]} for cd in codes if cd in rows], f, ensure_ascii=False, indent=1)
    print("backup ->", len(rows), "rows")

    for code in codes:
        eid, p = rows[code]
        e = ENRICH[code]
        if "critique_text" in e: p["critique"] = e["critique_text"]
        if "example_text" in e: p["example"] = e["example_text"]
        for k, v in e.items():
            if k in ("critique_text", "example_text"): continue
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
                     "documented sourcing + rubric score; corrected mismatched boilerplate where present", STAMP, NOW))
        cur.execute("INSERT INTO kb_audit_log (entity_code, action, detail, source) VALUES (%s,%s,%s,%s)",
                    (code, "DOC_ENRICH", json.dumps({"quality_score": score, "words": words, "sources": n_sources, "verified": n_verified, "breakdown": detail}, ensure_ascii=False), STAMP))
        print(f"{code}: score={score} words={words} sources={n_sources} verified={n_verified} relations={n_relations} | {detail}")
    c.commit()
    c.close()
    print("BATCH63 THEORY DONE")

if __name__ == "__main__":
    main()
