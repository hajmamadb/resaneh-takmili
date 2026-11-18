# -*- coding: utf-8 -*-
"""Batch 70: MC-371 (excellence theory), MC-372 (situational theory of publics),
MC-373 (dialogic PR), MC-374 (contingency theory). All had garbled boilerplate -> rewritten."""
import pymysql, json

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch70-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch70_theory.json"

S = {
 "MC-371": [
   dict(kind="BOOK", title_en="Excellence in Public Relations and Communication Management",
        title_fa="تعالی در روابط عمومی و مدیریت ارتباطات",
        authors="Grunig, J. E. (Ed.)", year=1992,
        publisher="Lawrence Erlbaum Associates", doi="10.4324/9780203812303",
        url="https://www.routledge.com/Excellence-in-Public-Relations-and-Communication-Management/Grunig/p/book/9780805802276",
        language="en", isbn="978-0805802276",
        citation="Grunig, J. E. (Ed.). (1992). Excellence in public relations and communication management. Lawrence Erlbaum Associates.",
        locator="whole work", locator_type="work",
        supports="definition / models / dominant coalition", verified=True),
   dict(kind="JOURNAL_ARTICLE", title_en="Symmetrical Systems of Internal Communication",
        title_fa="نظام‌های متقارن ارتباطات درون‌سازمانی",
        authors="Grunig, J. E.", year=1992,
        publisher="In J. E. Grunig (Ed.), Excellence in public relations and communication management (pp. 531-575). Lawrence Erlbaum",
        doi=None, url=None, language="en", isbn=None,
        citation="Grunig, J. E. (1992). Symmetrical systems of internal communication. In J. E. Grunig (Ed.), Excellence in public relations and communication management (pp. 531-575). Lawrence Erlbaum Associates.",
        locator="pp. 531-575", locator_type="CHAPTER",
        supports="symmetrical communication / employee relations", verified=False),
 ],
 "MC-372": [
   dict(kind="BOOK_CHAPTER", title_en="A Situational Theory of Publics: Conceptual History, Recent Challenges and New Research",
        title_fa="نظریهٔ موقعیتی توده‌ها: تاریخ مفهومی، چالش‌های اخیر و پژوهش تازه",
        authors="Grunig, J. E.", year=1997,
        publisher="International Thomson Business Press (in D. Moss, T. MacManus & D. Verčič, Eds., Public Relations Research: An International Perspective)",
        doi=None, url="https://sk.sagepub.com/ency/edvol/publicrelations/chpt/situational-theory-publics",
        language="en", isbn=None,
        citation="Grunig, J. E. (1997). A situational theory of publics: Conceptual history, recent challenges and new research. In D. Moss, T. MacManus, & D. Verčič (Eds.), Public relations research: An international perspective (pp. 3-48). International Thomson Business Press.",
        locator="pp. 3-48", locator_type="CHAPTER",
        supports="definition / three variables / typology", verified=True),
   dict(kind="BOOK", title_en="Managing Public Relations", title_fa="مدیریت روابط عمومی",
        authors="Grunig, J. E., & Hunt, T.", year=1984,
        publisher="Holt, Rinehart and Winston", doi=None, url=None, language="en", isbn=None,
        citation="Grunig, J. E., & Hunt, T. (1984). Managing public relations. Holt, Rinehart and Winston.",
        locator="whole work", locator_type="work",
        supports="origin / four models", verified=False),
 ],
 "MC-373": [
   dict(kind="JOURNAL_ARTICLE", title_en="Building Dialogic Relationships Through the World Wide Web",
        title_fa="ساختن روابط گفت‌وگومحور از طریق وب جهان‌گستر",
        authors="Kent, M. L., & Taylor, M.", year=1998,
        publisher="Public Relations Review, 24(3), 321-334",
        doi="10.1016/S0363-8111(99)80143-X", url="https://www.sciencedirect.com/science/article/pii/S036381119980143X",
        language="en", isbn=None,
        citation="Kent, M. L., & Taylor, M. (1998). Building dialogic relationships through the World Wide Web. Public Relations Review, 24(3), 321-334. https://doi.org/10.1016/S0363-8111(99)80143-X",
        locator="pp. 321-334", locator_type="page_range",
        supports="definition / five principles / dialogic loop", verified=True),
   dict(kind="JOURNAL_ARTICLE", title_en="Toward a Dialogic Theory of Public Relations",
        title_fa="در جهت نظریه‌ای گفت‌وگومحور برای روابط عمومی",
        authors="Kent, M. L., & Taylor, M.", year=2002,
        publisher="Public Relations Review, 28(1), 21-37",
        doi=None, url=None, language="en", isbn=None,
        citation="Kent, M. L., & Taylor, M. (2002). Toward a dialogic theory of public relations. Public Relations Review, 28(1), 21-37.",
        locator="pp. 21-37", locator_type="page_range",
        supports="evolution / dialogue as orientation", verified=False),
 ],
 "MC-374": [
   dict(kind="JOURNAL_ARTICLE", title_en="It Depends: A Contingency Theory of Accommodation in Public Relations",
        title_fa="بستگی دارد: نظریهٔ اقتضایی سازگاری در روابط عمومی",
        authors="Cancel, A. E., Cameron, G. T., Sallot, L. M., & Mitrook, M. A.", year=1997,
        publisher="Journal of Public Relations Research, 9(1), 31-63",
        doi="10.1207/s1532754xjprr0901_02", url="https://www.tandfonline.com/doi/abs/10.1207/s1532754xjprr0901_02",
        language="en", isbn=None,
        citation="Cancel, A. E., Cameron, G. T., Sallot, L. M., & Mitrook, M. A. (1997). It depends: A contingency theory of accommodation in public relations. Journal of Public Relations Research, 9(1), 31-63. https://doi.org/10.1207/s1532754xjprr0901_02",
        locator="pp. 31-63", locator_type="page_range",
        supports="definition / continuum / variables", verified=True),
   dict(kind="JOURNAL_ARTICLE", title_en="Testing the Contingency Theory of Accommodation in Public Relations",
        title_fa="آزمون نظریهٔ اقتضایی سازگاری در روابط عمومی",
        authors="Cancel, A. E., Mitrook, M. A., & Cameron, G. T.", year=1999,
        publisher="Public Relations Review, 25(2), 171-197",
        doi=None, url=None, language="en", isbn=None,
        citation="Cancel, A. E., Mitrook, M. A., & Cameron, G. T. (1999). Testing the contingency theory of accommodation in public relations. Public Relations Review, 25(2), 171-197.",
        locator="pp. 171-197", locator_type="page_range",
        supports="empirical test / refinement", verified=False),
 ],
}

VOID = "در بستر رسانه، "
ENRICH = {
 "MC-371": {
  "summary": "(گرونیگ، ۱۹۹۲) نظریهٔ تعالی، حاصل پروژهٔ پانزده‌سالهٔ انجمن بین‌المللی ارتباطات تجاری است و می‌پرسد چه ویژگی‌هایی روابط عمومی را برای سازمان «ارزش‌آفرین» می‌کند. پاسخ آن چهار اصل است: ارتباط دوسویهٔ متقارن، حضور مدیر روابط عمومی در ائتلاف مسلط، تنوع نیروی انسانی و تعهد اخلاقی — که با هم، هم‌سازی سازمان و ذی‌نفعان را ممکن می‌کنند.",
  "definition": "نظریهٔ تعالی، چارچوبی هنجاری-تجربی است که اثربخشی روابط عمومی را بر پایهٔ گفت‌وگوی متقارن با ذی‌نفعان، مشارکت در تصمیم‌گیری سازمانی، تنوع و اخلاق حرفه‌ای تبیین می‌کند و ارزش آن را در کاهش تعارض و هزینهٔ تنظیم‌گری می‌بیند.",
  "main_problem": "چرا برخی واحدهای روابط عمومی ارزش راهبردی می‌آفرینند و برخی تنها به تبلیغ و تشریفات محدود می‌مانند؟ نظریهٔ تعالی این تفاوت را نه در مهارت فنی، بلکه در جایگاه سازمانی، الگوی ارتباطی و اخلاق حرفه‌ای جست‌وجو می‌کند.",
  "mechanism": "\n".join([
   "(۱) ارتباط دوسویهٔ متقارن: سازمان نه تنها پیام می‌فرستد، بلکه گوش می‌دهد و در صورت لزوم موضع خود را تغییر می‌دهد؛ هدف، توافق دوجانبه است، نه اقناع یک‌سویه.",
   "(۲) ائتلاف مسلط: مدیر روابط عمومی باید در حلقهٔ تصمیم‌گیری ارشد حضور داشته باشد؛ در غیر این صورت، ارتباطات به توجیه تصمیم‌های از پیش گرفته‌شده فرو می‌کاهد.",
   "(۳) تنوع و فرهنگ سازمانی: ترکیب متنوع کارکنان و فرهنگ مشارکتی، توان درک ذی‌نفعان ناهمگون را افزایش می‌دهد و کیفیت تصمیم را بالا می‌برد.",
   "(۴) تعهد اخلاقی: صداقت، شفافیت و مسئولیت در قبال جامعه، شرط اعتبار بلندمدت است؛ بدون آن، گفت‌وگو به تاکتیک بدل می‌شود.",
   "(۵) ارزش از راه کاهش تعارض: سازمان متقارن، هزینهٔ بحران و تنش با ذی‌نفعان را کاهش می‌دهد و همین، ارزش اقتصادی قابل سنجش روابط عمومی است.",
   VOID + "در مدیریت بحران شبکه‌های اجتماعی، سازمانی که پاسخ‌های عمومی را می‌خواند و در سیاست خود بازنگری می‌کند، نمونهٔ متقارن است؛ سازمانی که فقط بیانیه می‌فرستد و کامنت‌ها را می‌بندد، نمونهٔ نامتقارن — تفاوت همین دو رفتار، موضوع نظریه است.",
  ]),
  "assumptions": [
   "سازمان و ذی‌نفعان، منافع مشترکی دارند که از راه گفت‌وگو قابل شناسایی است.",
   "ارتباط متقارن، هم اخلاقی و هم از نظر اقتصادی اثربخش است.",
   "جایگاه سازمانی روابط عمومی، کیفیت ارتباط را تعیین می‌کند.",
  ],
  "principles": [
   "گفت‌وگو باید به تغییر موضع سازمان بینجامد، نه فقط تغییر مخاطب.",
   "روابط عمومی باید در تصمیم‌گیری راهبردی حضور داشته باشد.",
   "تنوع و اخلاق، لوازم ساختاری تعالی‌اند، نه فضیلت‌های اختیاری.",
  ],
  "critiques": [
   "فرض هم‌منفعتی: نظریه، تضاد بنیادین منافع (کارگر/کارفرما، ساکن/صنعت) را کم‌رنگ می‌کند و هم‌سازی را همیشه ممکن می‌انگارد.",
   "هنجارگرایی غربی: مدل از تجربهٔ شرکت‌های آمریکای شمالی و اروپا برآمده و تعمیم آن به بافت‌های اقتدارگرا نیازمند بازنگری است.",
   "سنجش دشوار: «تعالی» با شاخص‌های کیفی سنجیده می‌شود و آزمون تجربی آن، به تفسیر پژوهشگر وابسته است.",
   "نادیده‌گرفتن قدرت: متقارن‌بودن در شرایط نابرابری منابع، آرمانی است؛ سازمان قدرتمند می‌تواند گفت‌وگو را به آیین تشریفاتی بدل کند.",
  ],
  "applications": [
   "ارزیابی ساختار ارتباطات سازمانی: جایگاه مدیر ارتباطات، دسترسی به تصمیم‌گیر و رویهٔ گوش‌دادن.",
   "طراحی رویهٔ پاسخ‌گویی اجتماعی: سازوکار دریافت و پاسخ به دغدغهٔ ذی‌نفعان.",
   "آموزش حرفه‌ای روابط عمومی: تقویت مهارت گفت‌وگو، تحلیل ذی‌نفع و اخلاق.",
   "پژوهش ارزش روابط عمومی: سنجش رابطهٔ متقارن‌بودن با اعتماد و کاهش بحران.",
  ],
  "evolution": "از چهار مدل روابط عمومی (گرونیگ و هانت، ۱۹۸۴) به پروژهٔ تعالی (۱۹۹۲) و سپس به بازنگری آن با مفاهیم هم‌آفرینی، شبکه و روابط عمومی دیجیتال در دههٔ ۲۰۰۰.",
  "key_concepts": ["ارتباط متقارن (Symmetrical Communication)", "ائتلاف مسلط (Dominant Coalition)", "مدل دوسویه (Two-Way Model)", "ذی‌نفع (Stakeholder)", "ارزش راهبردی (Strategic Value)", "اخلاق حرفه‌ای (Professional Ethics)"],
  "studies": [
   "Grunig, J. E. (1992). Symmetrical systems of internal communication. In J. E. Grunig (Ed.), Excellence in public relations and communication management (pp. 531-575). Lawrence Erlbaum Associates.",
   "Grunig, J. E., & Hunt, T. (1984). Managing public relations. Holt, Rinehart and Winston.",
  ],
  "detailed_analysis": "\n".join([
   "۱. بنیان و منطق نظری: نظریهٔ تعالی، روابط عمومی را از «فن ترغیب» به «کارکرد مدیریت مرز» ارتقا می‌دهد؛ ارزش آن در تنظیم رابطهٔ سازمان با محیط است و همین، آن را با نظریهٔ سیستم‌ها پیوند می‌دهد.",
   "۲. شواهد و روش: پروژهٔ تعالی با مطالعهٔ تطبیقی صدها سازمان در چند کشور، رابطهٔ ساختار ارتباطی، فرهنگ سازمانی و کیفیت رابطه را بررسی کرد؛ یافتهٔ کلیدی آن، پیوند میان حضور در تصمیم‌گیری و اثربخشی بود.",
   "۳. تنش امروز: پلتفرم‌ها، ذی‌نفعان را به مخاطبان فعال و ناهمگون بدل کرده‌اند؛ متقارن‌بودن دیگر یک انتخاب نیست، بلکه شرط بقای اعتبار در فضای عمومی شفاف است.",
  ]),
  "critique_text": "\n".join([
   "۱. فرض هم‌منفعتی: نظریه، تضاد بنیادین منافع (کارگر/کارفرما، ساکن/صنعت) را کم‌رنگ می‌کند و هم‌سازی را همیشه ممکن می‌انگارد.",
   "۲. هنجارگرایی غربی: مدل از تجربهٔ شرکت‌های آمریکای شمالی و اروپا برآمده و تعمیم آن به بافت‌های اقتدارگرا نیازمند بازنگری است.",
   "۳. سنجش دشوار: «تعالی» با شاخص‌های کیفی سنجیده می‌شود و آزمون تجربی آن، به تفسیر پژوهشگر وابسته است.",
   "۴. نادیده‌گرفتن قدرت: متقارن‌بودن در شرایط نابرابری منابع، آرمانی است؛ سازمان قدرتمند می‌تواند گفت‌وگو را به آیین تشریفاتی بدل کند.",
  ]),
  "example_text": "\n".join([
   "سازمانی که در بحران آلودگی، نخست بیانیه می‌فرستد و سپس با ساکنان محلی گفت‌وگوی باز می‌گذارد و برنامهٔ خود را بازنگری می‌کند، نمونهٔ متقارن است؛ سازمانی که فقط پیام می‌فرستد، نمونهٔ نامتقارن.",
   "در یک شرکت، مدیر ارتباطات عضوی از تیم تصمیم‌گیری است و پیش از نهایی‌شدن یک سیاست، نگرانی ذی‌نفعان را وارد بحث می‌کند؛ همین حضور در ائتلاف مسلط، ارزش تعالی را محقق می‌سازد.",
   "در کمپینی برای انتخاب نام محصول، مشارکت کارکنان از فرهنگ‌های مختلف، حساسیت‌های زبانی و فرهنگی را پیش از انتشار کشف می‌کند — کارکرد تنوع در تصمیم ارتباطی.",
  ]),
 },
 "MC-372": {
  "summary": "(گرونیگ، ۱۹۹۷؛ گرونیگ و هانت، ۱۹۸۴) نظریهٔ موقعیتی توده‌ها توضیح می‌دهد چرا همهٔ «مخاطبان» یکسان نیستند و فقط بخشی از آن‌ها به «تودهٔ فعال» بدل می‌شوند. سه متغیر — بازشناسی مسئله، ادراک محدودیت و میزان درگیری — تعیین می‌کنند که افراد در برابر یک مسئله در چه وضعیتی قرار گیرند و چه رفتاری از خود نشان دهند.",
  "definition": "نظریهٔ موقعیتی، طبقه‌بندی ذی‌نفعان را بر پایهٔ ادراک موقعیت انجام می‌دهد: شناسایی مسئله، باور به امکان عمل و احساس درگیری، چهار گونهٔ توده (غیرتوده، نهفته، آگاه، فعال) می‌سازند که هر کدام الگوی ارتباطی متفاوتی می‌طلبند.",
  "main_problem": "برنامه‌ریزی ارتباطی معمولاً «مخاطب» را توده‌ای همگن می‌گیرد؛ اما در واقعیت، تنها بخش کوچکی از ذی‌نفعان فعال‌اند. نظریه می‌پرسد چگونه می‌توان این بخش را پیش از تبدیل‌شدن به بحران، شناسایی کرد و با آن گفت‌وگو کرد.",
  "mechanism": "\n".join([
   "(۱) بازشناسی مسئله: آیا فرد می‌داند مسئله‌ای وجود دارد و آن را مهم می‌داند؟ این آگاهی، نخستین شرط فعال‌شدن است.",
   "(۲) ادراک محدودیت: آیا فرد باور دارد که اقدامی می‌تواند اثر بگذارد؟ باور به محدودیت، انگیزهٔ اقدام را کاهش می‌دهد، حتی با آگاهی بالا.",
   "(۳) میزان درگیری: میزان وابستگی فرد به مسئله تعیین می‌کند چقدر حاضر است برای اطلاعات و کنش هزینه کند.",
   "(۴) چهار گونهٔ توده: غیرتوده در سه متغیر کم‌نمره است؛ تودهٔ نهفته تنها درگیری دارد؛ تودهٔ آگاه آگاهی و درگیری دارد؛ تودهٔ فعال در سه متغیر فعال است و بیشترین کنش ارتباطی را انجام می‌دهد.",
   "(۵) رفتار اطلاعاتی: تودهٔ فعال «جست‌وجو» می‌کند (منبع می‌طلبد)، تودهٔ نهفته «پردازش» می‌کند (پیام تصادفی را تحلیل می‌کند)؛ این تفکیک، طراحی پیام را دقیق‌تر می‌کند.",
   VOID + "در بحران یک محصول، مشتریان زیان‌دیده — نه همهٔ مشتریان — تودهٔ فعال‌اند؛ سازمانی که پیش از گسترش بحران با همین گروه گفت‌وگو کند، هزینهٔ اعتبار را به‌شدت کاهش می‌دهد.",
  ]),
  "assumptions": [
   "رفتار ارتباطی افراد از ادراک موقعیت برمی‌آید، نه از ویژگی‌های ثابت شخصیتی.",
   "منافع و درگیری افراد با مسئله، متفاوت است و ذی‌نفعان گلولهٔ برفگین نیستند.",
   "توده‌ها در طول زمان و با تغییر ادراک، جابه‌جا می‌شوند.",
  ],
  "principles": [
   "ذی‌نفعان را بر پایهٔ ادراک موقعیت قابل تقسیم‌بندی کرد.",
   "تودهٔ فعال نیازمند گفت‌وگوی مستقیم و پاسخ‌گویی است، نه فقط پیام همگانی.",
   "تودهٔ نهفته را می‌توان از راه پیام‌های سودمند، به پردازش فعال برانگیخت.",
  ],
  "critiques": [
   "فردمحوری: نظریه بر ادراک فرد متمرکز است و ساختارهای اجتماعی و شبکه‌ای را کم‌رنگ می‌کند.",
   "سنجش سه متغیر: تعریف عملیاتی بازشناسی مسئله و ادراک محدودیت در عمل دشوار و زمینه‌وابسته است.",
   "نسخهٔ تاریخی: توسعهٔ نظریه در بستر رسانه‌های سنتی انجام شده و شبکه‌های اجتماعی، سرعت گذار میان توده‌ها را بسیار افزایش داده‌اند.",
   "پیش‌بینی محدود: رابطهٔ سه متغیر با کنش واقعی در همهٔ بافت‌ها و فرهنگ‌ها یکسان مشاهده نشده است.",
  ],
  "applications": [
   "بخش‌بندی ذی‌نفعان در بحران: تشخیص گروه فعال و تمرکز پاسخ‌گویی بر آن.",
   "طراحی کمپین سلامت: ارتقای آگاهی و درگیری گروه‌هایی که در مرحلهٔ نهفته‌اند.",
   "تحلیل مخاطب رسانه‌های اجتماعی: تشخیص گروه‌هایی که مسئله را می‌پذیرند اما امکان عمل نمی‌بینند.",
   "پایش پیشرفتار بحران: ردیابی گذار از تودهٔ آگاه به فعال پیش از رسیدن به اعتراض عمومی.",
  ],
  "evolution": "از صورت‌بندی اولیه در «مدیریت روابط عمومی» (۱۹۸۴) به بازنگری و پژوهش‌های تازهٔ گرونیگ (۱۹۹۷) و سپس به کاربرد در ارتباطات بحران، سلامت و تحلیل پیشرفت‌های شبکه‌ای.",
  "key_concepts": ["تودهٔ فعال (Active Public)", "بازشناسی مسئله (Problem Recognition)", "ادراک محدودیت (Constraint Recognition)", "میزان درگیری (Level of Involvement)", "جست‌وجوی اطلاعات (Information Seeking)", "پردازش اطلاعات (Information Processing)"],
  "studies": [
   "Grunig, J. E. (1997). A situational theory of publics. In D. Moss, T. MacManus, & D. Verčič (Eds.), Public relations research: An international perspective (pp. 3-48). International Thomson Business Press.",
   "Grunig, J. E., & Hunt, T. (1984). Managing public relations. Holt, Rinehart and Winston.",
  ],
  "detailed_analysis": "\n".join([
   "۱. بنیان و منطق نظری: نظریهٔ موقعیتی پاسخ گرونیگ به مفهوم مبهم «مخاطب» است؛ او با سه متغیر نشان داد توده، نه یک موجودیت ثابت، بلکه وضعیتی گذرا و قابل تغییر است.",
   "۲. کاربرد در مدیریت بحران: تودهٔ فعال، منبع اصلی فشار عمومی است؛ سازمان باید پیش از بحران، این گروه را از راه گفت‌وگو و پاسخ‌گویی مدیریت کند، نه با پیام همگانی پس از بحران.",
   "۳. افق دیجیتال: شبکه‌های اجتماعی گذار از نهفته به فعال را سریع و قابل ردیابی کرده‌اند؛ ازاین‌رو نظریهٔ موقعیتی ابزاری برای پایش فضای عمومی و طراحی پاسخ پیش‌دستانه است.",
  ]),
  "critique_text": "\n".join([
   "۱. فردمحوری: نظریه بر ادراک فرد متمرکز است و ساختارهای اجتماعی و شبکه‌ای را کم‌رنگ می‌کند.",
   "۲. سنجش سه متغیر: تعریف عملیاتی بازشناسی مسئله و ادراک محدودیت در عمل دشوار و زمینه‌وابسته است.",
   "۳. نسخهٔ تاریخی: توسعهٔ نظریه در بستر رسانه‌های سنتی انجام شده و شبکه‌های اجتماعی، سرعت گذار میان توده‌ها را بسیار افزایش داده‌اند.",
   "۴. پیش‌بینی محدود: رابطهٔ سه متغیر با کنش واقعی در همهٔ بافت‌ها و فرهنگ‌ها یکسان مشاهده نشده است.",
  ]),
  "example_text": "\n".join([
   "در بحران یک محصول، مشتریان زیان‌دیده فعال‌اند و به‌سرعت بیانیه، جبران خسارت و پاسخ متهم می‌خواهند؛ سایر مشتریان در مرحلهٔ آگاه یا نهفته‌اند و با پیام شفاف، در آستانهٔ فعال‌شدن قرار می‌گیرند.",
   "در کمپین سلامت، گروه‌هایی که خطر را می‌دانند ولی باورند اقدامشان بی‌اثر است، تودهٔ آگاه با ادراک محدودیت‌اند؛ پیام مؤثر برای آن‌ها راه‌حل عملی است، نه وعظ دربارهٔ خطر.",
   "در یک اعتراض محلی، ساکنان مجاور محل دفن زباله به‌سرعت به تودهٔ فعال بدل می‌شوند؛ شهرداری که فقط بیانیه همگانی می‌فرستد، به‌جای گفت‌وگو با همین گروه، بحران را تشدید می‌کند.",
  ]),
 },
 "MC-373": {
  "summary": "(کنت و تیلور، ۱۹۹۸) روابط عمومی گفت‌وگومحور، وب و رسانه‌های دیجیتال را نه کانال تبلیغ یک‌سویه، بلکه فضایی برای گفت‌وگوی واقعی میان سازمان و ذی‌نفعان می‌داند. به باور آن‌ها، گفت‌وگو نه فن متقاعدسازی، بلکه «جهت‌گیری» اخلاقی است که بازخورد، گوش‌دادن و باز نگه‌داشتن کانال را شرط اعتبار روابط عمومی می‌کند.",
  "definition": "روابط عمومی گفت‌وگومحور، رویکردی است که تعامل سازمان و مخاطب را با معیارهای گفت‌وگوی اصیل می‌سنجد: پاسخ‌گویی، گوش‌دادن، باز بودن کانال و امکان تغییر موضع هر دو طرف.",
  "main_problem": "رسانه‌های دیجیتال، امکان تعامل دوطرفه را فراهم کرده‌اند؛ اما بسیاری از سازمان‌ها همان تبلیغ یک‌سویه را در قالب تازه تکرار می‌کنند. پرسش این است که چه معیاری تعامل را از تک‌گویی فناورانه تفکیک می‌کند.",
  "mechanism": "\n".join([
   "(۱) حلقهٔ گفت‌وگو: سازمان باید پرسش‌ها را دریافت، پردازش و پاسخ دهد؛ حلقهٔ بسته‌ناپذیر، به تبلیغ یک‌سویه تبدیل می‌شود.",
   "(۲) سودمندی اطلاعات: اطلاعات باید برای ذی‌نفع ارزش واقعی داشته باشد، نه فقط برای سازمان؛ معیار، مفیدبودن برای مخاطب است.",
   "(۳) ترغیب به بازگشت: به‌روزرسانی منظم، انجمن و محتوای تازه، پیوند پایدار می‌سازد و رابطه را از یک‌بار دیدن به تکرار تعامل می‌برد.",
   "(۴) سهولت رابط: طراحی ساده و قابل دسترس، شرط پایهٔ گفت‌وگوست؛ مانع فنی، پیام اخلاقی «گوش نمی‌دهیم» است.",
   "(۵) حفظ بازدیدکننده: ماندگاری مخاطب در فضای گفت‌وگو، نشانهٔ ارزش رابطه است؛ طراحی برای رفتن سریع، گفت‌وگو را نفی می‌کند.",
   VOID + "یک صفحهٔ ارتباط با ما که فقط آدرس می‌دهد، گفت‌وگو نیست؛ سازمانی که در همان صفحه سؤال می‌پرسد، پاسخ می‌دهد و پاسخ‌ها را عمومی منتشر می‌کند، حلقهٔ گفت‌وگو را بسته است.",
  ]),
  "assumptions": [
   "گفت‌وگو، جهت‌گیری اخلاقی است، نه تکنیک؛ ارزش آن به قصد و کیفیت پاسخ‌گویی بستگی دارد.",
   "رسانهٔ دیجیتال می‌تواند شرط فنی گفت‌وگو را فراهم کند، اما تضمین اخلاقی آن را نمی‌دهد.",
   "اساس روابط عمومی خوب، رابطه است، نه پیام.",
  ],
  "principles": [
   "همهٔ پرسش‌ها باید پاسخ دریافت کنند، حتی اگر پاسخ منفی باشد.",
   "اطلاعات باید برای ذی‌نفع سودمند باشد.",
   "کانال گفت‌وگو باید باز، قابل دسترس و پایدار بماند.",
  ],
  "critiques": [
   "آرمان‌گرایی: در بسترهای نابرابر، گفت‌وگوی اصیل با سازمان قدرتمند به سختی ممکن است.",
   "کم‌رنگی منابع: نظریه بر طراحی و اخلاق متمرکز است و به سنجش اثر و منابع سازمانی کمتر می‌پردازد.",
   "خطر آیین‌گرایی: شرکتی که فرم گفت‌وگو می‌گذارد اما پاسخ نمی‌دهد، معیارهای ظاهری نظریه را برمی‌آورد بی‌آنکه گفت‌وگو رخ دهد.",
   "فرهنگ‌وابستگی: معنای «گوش‌دادن» و «پاسخ‌گویی» در فرهنگ‌ها و نظام‌های سیاسی متفاوت است.",
  ],
  "applications": [
   "طراحی وب‌سایت و کانال رسمی سازمان: معیارهای پنج‌گانهٔ گفت‌وگو.",
   "ارزشیابی تعامل رسانه‌های اجتماعی: سنجش کیفیت پاسخ، نه فقط حجم تعامل.",
   "مدیریت بحران: انتشار عمومی پرسش‌ها و پاسخ‌ها برای بازسازی حلقهٔ اعتماد.",
   "آموزش اخلاق روابط عمومی: تفکیک گفت‌وگو از تبلیغ و اقناع.",
  ],
  "evolution": "از «ساختن روابط گفت‌وگومحور» (۱۹۹۸) به «نظریهٔ گفت‌وگو در روابط عمومی» (۲۰۰۲) و سپس به ادبیات گفت‌وگوی دیجیتال و مشارکت مخاطب در پلتفرم‌ها.",
  "key_concepts": ["حلقهٔ گفت‌وگو (Dialogic Loop)", "گوش‌دادن (Listening)", "بازخوردپذیری (Feedback)", "معیارهای پنج‌گانه (Five Dialogic Principles)", "باز بودن کانال (Channel Openness)", "رابطهٔ متقابل (Mutual Relationship)"],
  "studies": [
   "Kent, M. L., & Taylor, M. (2002). Toward a dialogic theory of public relations. Public Relations Review, 28(1), 21-37.",
   "Kent, M. L., & Taylor, M. (1998). Building dialogic relationships through the World Wide Web. Public Relations Review, 24(3), 321-334.",
  ],
  "detailed_analysis": "\n".join([
   "۱. بنیان و منطق نظری: کنت و تیلور، گفت‌وگو را از سنت فلسفی (باختین، بوبر) به روابط عمومی آوردند؛ سهم آن‌ها، تبدیل مفهوم انتزاعی گفت‌وگو به معیارهای قابل ارزیابی وب‌سایت و کانال است.",
   "۲. تقابل با تعالی: در نظریهٔ تعالی، متقارن‌بودن ابزار ارزش سازمانی است؛ در گفت‌وگومحوری، رابطه هدف است و ابزار نیست. همین تفاوت، مرز اخلاقی دو نظریه را نشان می‌دهد.",
   "۳. افق امروز: با پلتفرم‌ها، گفت‌وگو قابل اندازه‌گیری شده است؛ پرسش تازه این است که آیا میانگین زمان پاسخ و نرخ بازخورد، به معیار گفت‌وگوی اصیل بدل شده یا آن را به بهینه‌سازی عددی فرو کاسته است.",
  ]),
  "critique_text": "\n".join([
   "۱. آرمان‌گرایی: در بسترهای نابرابر، گفت‌وگوی اصیل با سازمان قدرتمند به سختی ممکن است.",
   "۲. کم‌رنگی منابع: نظریه بر طراحی و اخلاق متمرکز است و به سنجش اثر و منابع سازمانی کمتر می‌پردازد.",
   "۳. خطر آیین‌گرایی: شرکتی که فرم گفت‌وگو می‌گذارد اما پاسخ نمی‌دهد، معیارهای ظاهری نظریه را برمی‌آورد بی‌آنکه گفت‌وگو رخ دهد.",
   "۴. فرهنگ‌وابستگی: معنای «گوش‌دادن» و «پاسخ‌گویی» در فرهنگ‌ها و نظام‌های سیاسی متفاوت است.",
  ]),
  "example_text": "\n".join([
   "در صفحهٔ «ارتباط با ما» یک بانک، اگر پرسش‌ها فقط به فرم بی‌پاسخ هدایت شوند، حلقهٔ گفت‌وگو بسته نشده؛ بانکی که در همان صفحه پرسش‌های پرتکرار را عمومی پاسخ می‌دهد، حلقه را می‌بندد.",
   "در بحران یک رستوران زنجیره‌ای، انتشار عمومی استدلال مشتریان و پاسخ شفاف مدیر، حتی وقتی پاسخ سازمان را قانع نمی‌کند، گفت‌وگو را زنده نگه می‌دارد.",
   "در یک وب‌سایت سازمانی، منویی پیچیده و پر از تبلیغ، مخاطب را پیش از هر گفت‌وگویی دور می‌کند؛ سهولت رابط، شرط نخست گفت‌وگو است.",
  ]),
 },
 "MC-374": {
  "summary": "(کانسل، کامرون، سالوت و میتروک، ۱۹۹۷) نظریهٔ اقتضایی سازگاری می‌گوید روابط عمومی نمی‌تواند همیشه متقارن باشد؛ موضع سازمان در هر مسئله روی طیفی از «دفاع سرسختانه» تا «سازگاری کامل» قرار می‌گیرد و جای آن، تابع مجموعه‌ای از عوامل درونی، بیرونی و موقعیتی است.",
  "definition": "نظریهٔ اقتضایی، سنجش موقعیت سازمان در برابر یک ذی‌نفع را با یک پیوستار دو قطبی و مجموعه‌ای از متغیرهای اقتضایی تبیین می‌کند؛ پاسخ ارتباطی، نتیجهٔ بده‌بستان این متغیرها در لحظه است.",
  "main_problem": "نظریهٔ تعالی، متقارن‌بودن را هنجار می‌داند؛ اما سازمان‌ها در واقعیت گاهی دفاع می‌کنند و گاهی می‌پذیرند. پرسش این است که چه عواملی این تغییر موضع را توضیح می‌دهد و چگونه می‌توان آن را پیش‌بینی کرد.",
  "mechanism": "\n".join([
   "(۱) پیوستار مواضع: از دفاع سرسختانه تا سازگاری کامل، طیفی از مواضع ممکن است؛ سازمان در هر مسئله در نقطه‌ای از این طیف می‌ایستد، نه در یک قطب ثابت.",
   "(۲) متغیرهای بیرونی: تهدید خارجی، اندازهٔ مسئله، محیط صنعت، فشار رسانه‌ای و محیط سیاسی، سازمان را به سوی دفاع یا سازگاری می‌رانند.",
   "(۳) متغیرهای درونی: ساختار سازمانی، شخصیت مدیر، منافع و هنجارهای سازمان، منابع موجود و فرهنگ، مرزهای حرکت را تعیین می‌کنند.",
   "(۴) متغیرهای موقعیتی: مرحلهٔ بحران، اعتماد پیشین، زمان و امکان گفت‌وگو، تصمیم لحظه‌ای را تغییر می‌دهند.",
   "(۵) دینامیک در طول مسئله: موضع سازمان ثابت نیست؛ با تغییر فشار بیرونی و گفت‌وگوی درونی، می‌تواند در همان مسئله از دفاع به سازگاری (یا برعکس) جابه‌جا شود.",
   VOID + "در کمپین بایکوت یک برند، سازمان با اعتراض گسترده روبه‌روست؛ اگر فشار رسانه‌ای بالا و منفعت اقتصادی برند در خطر باشد، موضع به سازگاری می‌رود، و اگر مسئله کوچک و اعتماد پیشین بالا باشد، همان سازمان ممکن است به دفاع بایستد.",
  ]),
  "assumptions": [
   "هیچ موضع ارتباطی همیشه درست نیست؛ اثربخشی، تابع موقعیت است.",
   "موضع سازمان، نتیجهٔ مجموعه‌ای از متغیرهای شناخته‌شده است، نه انتخاب دلبخواه مدیر.",
   "طیف دفاع-سازگاری، ابزاری تحلیلی است و مرز دو قطب، تجربی است.",
  ],
  "principles": [
   "تحلیل پیش از پاسخ: متغیرهای بیرونی، درونی و موقعیتی باید پیش از تصمیم ارزیابی شوند.",
   "موضع را می‌توان در طول مسئله تغییر داد.",
   "سازگاری همیشه مطلوب نیست؛ گاهی دفاع از منافع مشروع، اقتضای اخلاقی است.",
  ],
  "critiques": [
   "پیچیدگی غیرقابل اجرا: شمار متغیرها چنان زیاد است که پیش‌بینی عملی تصمیم دشوار می‌شود.",
   "کم‌رنگی اخلاق: تمرکز بر «اقتضا» می‌تواند به توجیه فرصت‌طلبانهٔ دفاع در برابر منافع عمومی بدل شود.",
   "سنجش متغیرها: تعریف عملیاتی بسیاری از متغیرها مبهم است و آزمون تجربی را محدود می‌کند.",
   "بستر آمریکایی: نمونه‌های اصلی از سازمان‌های آمریکای شمالی‌اند و تعمیم به بافت‌های دیگر نیازمند بررسی است.",
  ],
  "applications": [
   "تحلیل پاسخ برند در بحران شبکه‌های اجتماعی: ردیابی موضع از دفاع به سازگاری.",
   "برنامه‌ریزی پاسخ‌گویی: انتخاب دامنهٔ سازگاری بر پایهٔ فشار بیرونی و منابع درونی.",
   "پژوهش روابط عمومی تطبیقی: مقایسهٔ مسیر موضع سازمان‌ها در مسئله‌های مشابه.",
   "آموزش مدیران: تفکیک اقتضای راهبردی از سازش فرصت‌طلبانه.",
  ],
  "evolution": "از صورت‌بندی اولیه (۱۹۹۷) به آزمون تجربی و پالایش مدل (۱۹۹۹) و سپس به مطالعات تطبیقی در بحران‌های پلتفرمی و مسئولیت اجتماعی شرکتی.",
  "key_concepts": ["طیف دفاع-سازگاری (Advocacy-Accommodation Continuum)", "متغیرهای اقتضایی (Contingency Variables)", "موضع سازمانی (Organizational Stance)", "دفاع سرسختانه (Pure Advocacy)", "سازگاری کامل (Pure Accommodation)", "پویایی مسئله (Issue Dynamics)"],
  "studies": [
   "Cancel, A. E., Mitrook, M. A., & Cameron, G. T. (1999). Testing the contingency theory of accommodation in public relations. Public Relations Review, 25(2), 171-197.",
   "Cancel, A. E., Cameron, G. T., Sallot, L. M., & Mitrook, M. A. (1997). It depends: A contingency theory of accommodation in public relations. Journal of Public Relations Research, 9(1), 31-63.",
  ],
  "detailed_analysis": "\n".join([
   "۱. بنیان و منطق نظری: نظریهٔ اقتضایی، نقد واقع‌گرایانه بر هنجار متقارن است؛ پرسش آن نه «چه باید کرد»، بلکه «چه چیزی موضع را تعیین می‌کند» است و همین، آن را به سنت تجربی نزدیک می‌کند.",
   "۲. روش و شاهد: پژوهش‌های تجربی، موضع سازمان‌ها را در مسئله‌های واقعی ردیابی و با متغیرهای اقتضایی مقایسه کردند؛ یافتهٔ کلیدی، پویایی موضع در طول یک مسئله بود.",
   "۳. افق امروز: در فضای پلتفرمی، فشار بیرونی سریع‌تر و قابل اندازه‌گیری‌تر شده است؛ ازاین‌رو نظریهٔ اقتضایی ابزاری برای تحلیل «چرخش موضع» برندها در چند ساعت است.",
  ]),
  "critique_text": "\n".join([
   "۱. پیچیدگی غیرقابل اجرا: شمار متغیرها چنان زیاد است که پیش‌بینی عملی تصمیم دشوار می‌شود.",
   "۲. کم‌رنگی اخلاق: تمرکز بر «اقتضا» می‌تواند به توجیه فرصت‌طلبانهٔ دفاع در برابر منافع عمومی بدل شود.",
   "۳. سنجش متغیرها: تعریف عملیاتی بسیاری از متغیرها مبهم است و آزمون تجربی را محدود می‌کند.",
   "۴. بستر آمریکایی: نمونه‌های اصلی از سازمان‌های آمریکای شمالی‌اند و تعمیم به بافت‌های دیگر نیازمند بررسی است.",
  ]),
  "example_text": "\n".join([
   "برندی که در برابر بایکوت نخست انکار می‌کند و سپس با فشار رسانه‌ای، عذرخواهی و تغییر سیاست را می‌پذیرد، در طول یک مسئله از دفاع به سازگاری حرکت کرده است؛ نظریه همین مسیر را توضیح می‌دهد.",
   "سازمانی با اعتماد پیشین بالا و مسئلهٔ کوچک، ممکن است به دفاع بایستد و درست هم عمل کند؛ سازمانی با اعتماد شکننده، همان دفاع را به تشدید بحران بدل می‌کند.",
   "در مدیریت یک شکایت عمومی، تصمیم به سازگاری وقتی گرفته می‌شود که منابع سازمان، فشار رسانه‌ای و هزینهٔ اعتبار سبک‌وسنگ شده باشند — نه فقط به این دلیل که «سازگاری اخلاقی‌تر است».",
  ]),
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
    codes = list(S.keys())
    cur.execute("SELECT id, code, properties FROM kb_entities WHERE code IN (%s)" % ",".join(["%s"]*len(codes)), codes)
    rows = {code:(eid, json.loads(pr)) for (eid, code, pr) in cur.fetchall()}
    with open(BACKUP, "w", encoding="utf-8") as f:
        json.dump([{"code": cd, "props": rows[cd][1]} for cd in codes if cd in rows], f, ensure_ascii=False, indent=1)
    print("backup ->", len(rows), "rows")

    for code in codes:
        if code not in rows:
            print("MISSING", code); continue
        eid, p = rows[code]
        e = ENRICH[code]
        if "critique_text" in e: p["critique"] = e["critique_text"]
        if "example_text" in e: p["example"] = e["example_text"]
        for k, v in e.items():
            if k in ("critique_text", "example_text"): continue
            p[k] = v
        if not has_content(p.get("definition")) and has_content(p.get("summary")): p["definition"] = p["summary"]
        spec = S[code]
        p["sources"] = [dict(citation=s["citation"], language=("انگلیسی" if s["language"]=="en" else "فارسی"),
                             doi=s.get("doi") or "", url=s.get("url") or "", year=s.get("year")) for s in spec]
        p["citations"] = [dict(source=s["citation"], locator=s["locator"], supports=s["supports"],
                               verified=bool(s.get("verified"))) for s in spec]
        n_sources = len(spec); n_verified = sum(1 for s in spec if s.get("verified"))
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
                cur.execute("SELECT id FROM kb_sources WHERE doi=%s LIMIT 1", (s["doi"],)); r = cur.fetchone()
                if r: sid = r[0]
            if sid is None:
                cur.execute("SELECT id FROM kb_sources WHERE title_en=%s AND year=%s LIMIT 1", (s["title_en"], s["year"])); r = cur.fetchone()
                if r: sid = r[0]
            if sid is None:
                bib = json.dumps({"authors": s["authors"], "citation": s["citation"]}, ensure_ascii=False)
                cur.execute("INSERT INTO kb_sources (kind,title_fa,title_en,year,publisher,doi,isbn,url,language,access_type,bibliographic) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (s["kind"], s["title_fa"], s["title_en"], s["year"], s["publisher"], s.get("doi"), s.get("isbn"), s.get("url"),
                     s["language"], "open" if s.get("url") else "unknown", bib))
                sid = cur.lastrowid
            cur.execute("SELECT id FROM kb_evidence WHERE about_code=%s AND source_id=%s LIMIT 1", (code, sid))
            if cur.fetchone():
                continue
            lt = "CHAPTER" if s["locator_type"] == "CHAPTER" else ("PAGE" if s["locator_type"] == "page_range" else "SECTION")
            cur.execute("INSERT INTO kb_citations (source_id,locator_type,locator_value,paraphrase,citation_style,language,accessed_at) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                (sid, lt, s["locator"], "پشتیبانی از بخش: " + s["supports"], "apa", s["language"], NOW))
            cid = cur.lastrowid
            cur.execute("INSERT INTO kb_evidence (source_id,citation_id,about_code,evidence_type,evidence_summary,locator,direction,extraction_method,verification_status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (sid, cid, code, "bibliographic_reference", "منبع اصلی برای بخش: " + s["supports"], s["locator"], "supports",
                 "ai_extraction", "verified" if s.get("verified") else "unverified"))
        cur.execute("SELECT COALESCE(MAX(version),0)+1 FROM kb_entity_versions WHERE entity_id=%s", (eid,))
        ver = cur.fetchone()[0]
        cur.execute("INSERT INTO kb_entity_versions (entity_id, version, snapshot, change_reason, changed_by, created_at) VALUES (%s,%s,%s,%s,%s,%s)",
                    (eid, ver, json.dumps({"quality_score": score, "words": words, "sources": n_sources, "verified": n_verified}, ensure_ascii=False),
                     "full documentation enrichment + verified sources", STAMP, NOW))
        cur.execute("INSERT INTO kb_audit_log (entity_code, action, detail, source) VALUES (%s,%s,%s,%s)",
                    (code, "DOC_ENRICH", json.dumps({"quality_score": score, "words": words, "sources": n_sources, "verified": n_verified, "relations": n_relations, "breakdown": detail}, ensure_ascii=False), STAMP))
        print(f"{code}: score={score} words={words} sources={n_sources} verified={n_verified} relations={n_relations} | {detail}")
    c.commit(); c.close()
    print("BATCH70 THEORY DONE")

if __name__ == "__main__":
    main()
