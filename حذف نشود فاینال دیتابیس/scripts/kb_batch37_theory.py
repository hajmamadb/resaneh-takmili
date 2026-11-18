# -*- coding: utf-8 -*-
"""Batch 37 (THEORY): MC-083 Mass Society Theory (Kornhauser 1959), MC-043 Journalistic Objectivity
(Schudson 2001), MC-125 Situational Theory of Publics (Grunig 1997), MC-146 Dialogic Communication
(Kent & Taylor 1998). All primary anchors web-verified 2026-11-16."""
import pymysql, json

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch37-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch37_theory.json"

S = {
 "MC-083": [  # Mass Society Theory
   dict(kind="BOOK", title_en="The Politics of Mass Society",
        title_fa="سیاست جامعهٔ توده‌ای", authors="Kornhauser, W.", year=1959,
        publisher="Glencoe, IL: The Free Press", doi=None, url=None, language="en", isbn=None,
        citation="Kornhauser, W. (1959). The politics of mass society. The Free Press.",
        locator="whole work", locator_type="work", supports="definition / mechanism / critique of mass society", verified=True),
   dict(kind="BOOK", title_en="Personal Influence: The Part Played by People in the Flow of Mass Communications",
        title_fa="نفوذ شخصی: نقش افراد در جریان ارتباطات جمعی", authors="Katz, E., & Lazarsfeld, P. F.", year=1955,
        publisher="Glencoe, IL: The Free Press", doi=None, url=None, language="en", isbn=None,
        citation="Katz, E., & Lazarsfeld, P. F. (1955). Personal influence: The part played by people in the flow of mass communications. The Free Press.",
        locator="whole work", locator_type="work", supports="critique / limited effects counter-evidence", verified=False),
 ],
 "MC-043": [  # Journalistic Objectivity
   dict(kind="JOURNAL_ARTICLE", title_en="The Objectivity Norm in American Journalism",
        title_fa="هنجار عینیت در روزنامه‌نگاری آمریکایی", authors="Schudson, M.", year=2001,
        publisher="Journalism, 2(2), 149-170", doi="10.1177/146488490100200201",
        url="https://journals.sagepub.com/doi/10.1177/146488490100200201", language="en", isbn=None,
        citation="Schudson, M. (2001). The objectivity norm in American journalism. Journalism, 2(2), 149-170. https://doi.org/10.1177/146488490100200201",
        locator="pp. 149-170", locator_type="page_range", supports="definition / historical origin / norm", verified=True),
   dict(kind="JOURNAL_ARTICLE", title_en="Objectivity as Strategic Ritual: An Examination of Newsmen's Notions of Objectivity",
        title_fa="عینیت به‌عنوان آیین راهبردی: بررسی تلقی خبرنگاران از عینیت", authors="Tuchman, G.", year=1972,
        publisher="American Journal of Sociology, 77(4), 660-679", doi=None, url=None, language="en", isbn=None,
        citation="Tuchman, G. (1972). Objectivity as strategic ritual: An examination of newsmen's notions of objectivity. American Journal of Sociology, 77(4), 660-679.",
        locator="pp. 660-679", locator_type="page_range", supports="evolution / strategic ritual / critiques", verified=False),
 ],
 "MC-125": [  # Situational Theory of Publics
   dict(kind="BOOK", title_en="Public Relations Research: An International Perspective",
        title_fa="پژوهش روابط عمومی: چشم‌اندازی بین‌المللی", authors="Grunig, J. E.", year=1997,
        publisher="London: International Thomson Business Press (chapter: A situational theory of publics, pp. 3-48)",
        doi=None, url=None, language="en", isbn=None,
        citation="Grunig, J. E. (1997). A situational theory of publics: Conceptual history, recent challenges and new research. In D. Moss, T. MacManus, & D. Verčič (Eds.), Public relations research: An international perspective (pp. 3-48). International Thomson Business Press.",
        locator="pp. 3-48", locator_type="page_range", supports="definition / variables / typology", verified=True),
   dict(kind="BOOK", title_en="Excellence in Public Relations and Communication Management",
        title_fa="برتری در روابط عمومی و مدیریت ارتباطات", authors="Grunig, J. E. (Ed.)", year=1992,
        publisher="Hillsdale, NJ: Lawrence Erlbaum Associates", doi=None, url=None, language="en", isbn=None,
        citation="Grunig, J. E. (Ed.). (1992). Excellence in public relations and communication management. Lawrence Erlbaum Associates.",
        locator="whole work", locator_type="work", supports="evolution / integration with excellence theory", verified=False),
 ],
 "MC-146": [  # Dialogic Communication
   dict(kind="JOURNAL_ARTICLE", title_en="Building Dialogic Relationships through the World Wide Web",
        title_fa="ساختن روابط گفت‌وگومدار از طریق وب جهان‌گستر", authors="Kent, M. L., & Taylor, M.", year=1998,
        publisher="Public Relations Review, 24(3), 321-334", doi=None, url=None, language="en", isbn=None,
        citation="Kent, M. L., & Taylor, M. (1998). Building dialogic relationships through the World Wide Web. Public Relations Review, 24(3), 321-334.",
        locator="pp. 321-334", locator_type="page_range", supports="definition / five dialogic principles / mechanism", verified=True),
   dict(kind="JOURNAL_ARTICLE", title_en="Toward a Dialogic Theory of Public Relations",
        title_fa="به‌سوی نظریه‌ای گفت‌وگومدار از روابط عمومی", authors="Kent, M. L., & Taylor, M.", year=2002,
        publisher="Public Relations Review, 28(1), 21-37", doi=None, url=None, language="en", isbn=None,
        citation="Kent, M. L., & Taylor, M. (2002). Toward a dialogic theory of public relations. Public Relations Review, 28(1), 21-37.",
        locator="pp. 21-37", locator_type="page_range", supports="evolution / dialogic theory / critiques", verified=False),
 ],
}

ENRICH = {
 "MC-083": {
   "summary": "«نظریهٔ جامعهٔ توده‌ای» (Mass Society Theory) ریشه در واکنش فکری قرن نوزدهم و بیستم به صنعتی‌شدن، شهرنشینی و فروپاشی اجتماعات محلی دارد و در کتاب «The Politics of Mass Society» ویلیام کورنهاوزر (۱۹۵۹، The Free Press) صورت‌بندی کلاسیک یافت. کورنهاوزر استدلال کرد که هرچه جامعه بیشتر «توده‌ای» شود — یعنی هرچه پیوندهای میانی (خانواده، محله، انجمن‌ها) سست‌تر و نخبگان برای توده قابل‌دسترس‌تر شوند — آسیب‌پذیری آن در برابر جنبش‌های همه‌چیزخواه و اقتدارگرا بیشتر می‌شود (Kornhauser, 1959).",
   "main_problem": "چرا و چگونه تحول ساختار اجتماعی مدرن — تضعیف گروه‌های میانی و اتمیزه‌شدن افراد — جامعه را در برابر تبلیغات توده‌ای، جنبش‌های اقتدارگرا و دستکاری رسانه‌ای آسیب‌پذیر می‌کند؟",
   "mechanism": "کورنهاوزر مکانیسم را با دو متغیر توضیح می‌دهد: «دسترسی‌پذیری نخبگان» (accessibility of elites) و «تودهٔ در دسترس» (available masses). در جوامع کثرت‌گرا، گروه‌های میانی هم نخبگان را در برابر فشار مستقیم توده محافظت می‌کنند و هم افراد را به شبکه‌های اجتماعی و هنجارهای مشترک پیوند می‌دهند. در جامعهٔ توده‌ای، این پیوندهای میانی فرومی‌ریزند، افراد «اتمیزه» می‌شوند و نخبگان در برابر جلب مستقیم طرفداران آسیب‌پذیر می‌گردند؛ نتیجه، زمینهٔ مساعد برای جنبش‌های توده‌ای است (Kornhauser, 1959). در نسخهٔ ارتباطی این نظریه، رسانه‌های جمعی به‌عنوان عامل تشدیدکنندهٔ اتمیزه‌شدن و ابزار «تزریق» پیام به تودهٔ غیرمتمایز تصور می‌شدند — همان پیش‌فرضی که در «الگوی گلولهٔ جادویی» (hypodermic needle) بازتاب یافت و بعدها با شواهد «اثرات محدود» (Katz & Lazarsfeld, 1955) به چالش کشیده شد.",
   "assumptions": [
     "جامعهٔ مدرن به سمت اتمیزه‌شدن و تضعیف پیوندهای میانی حرکت می‌کند.",
     "افراد در جامعهٔ توده‌ای غیرمتمایز، منفعل و مستعد پذیرش مستقیم پیام‌های توده‌ای‌اند.",
     "رسانه‌های جمعی عامل تشدید اتمیزه‌شدن و ابزار دستکاری توده‌اند."
   ],
   "principles": [
     "پیوندهای میانی: انجمن‌ها و شبکه‌های اجتماعی، سپر دموکراسی در برابر توده‌ای‌شدن‌اند.",
     "دسترسی مستقیم نخبه-توده: فروپاشی واسطه‌ها، خطر اقتدارگرایی را افزایش می‌دهد.",
     "اثر یکسان رسانه: در نسخهٔ افراطی، پیام توده‌ای بر همهٔ مخاطبان یکسان اثر می‌گذارد."
   ],
   "critiques": [
     "نخبه‌گرایی و نوستالژی: نظریه اغلب جامعهٔ سنتی و اجتماع محلی را آرمانی می‌کند و مخاطب را منفعل فرض می‌گیرد.",
     "رد تجربی: پژوهش‌های جریان دو مرحله‌ای و رهبران عقیده نشان دادند که رسانه بر مخاطب به‌طور یکسان و مستقیم اثر نمی‌گذارد (Katz & Lazarsfeld, 1955).",
     "ساده‌سازی ساختار اجتماعی: اتمیزه‌شدن و توده‌ای‌شدن مفاهیمی کیفی و سنجش‌ناپذیرند و روابط علّی ادعاشده به‌سختی آزمون‌پذیر است."
   ],
   "applications": [
     "تحلیل تاریخی تبلیغات توده‌ای و جنبش‌های اقتدارگرا در قرن بیستم.",
     "مطالعهٔ پیامدهای اجتماعی رسانه‌های دیجیتال بر انزوای اجتماعی و قطبی‌شدن.",
     "نقد الگوهای سادهٔ اثر رسانه در آموزش سواد رسانه‌ای."
   ],
   "evolution": "نظریهٔ جامعهٔ توده‌ای در دههٔ ۱۹۵۰ به اوج رسید و سپس با پژوهش‌های اثرات محدود و جریان دو مرحله‌ای به حاشیه رفت. در دهه‌های بعد، در تحلیل‌های انتقادی رسانه و در مباحث معاصر دربارهٔ اتمیزه‌شدن کاربران شبکه‌های اجتماعی و قطبی‌شدن سیاسی بازخوانی شد.",
   "key_concepts": ["جامعهٔ توده‌ای (mass society)", "تودهٔ در دسترس (available masses)", "دسترسی‌پذیری نخبگان (accessibility of elites)", "اتمیزه‌شدن (atomization)", "الگوی گلولهٔ جادویی (hypodermic needle model)"],
   "studies": ["Kornhauser, W. (1959). The Politics of Mass Society. The Free Press.", "Katz, E., & Lazarsfeld, P. F. (1955). Personal Influence. The Free Press."],
 },
 "MC-043": {
   "summary": "«عینیت خبری» (Journalistic Objectivity) هنجاری حرفه‌ای در روزنامه‌نگاری است که می‌کوشد گزارش خبری را از ارزش‌داوری شخصی، جانب‌داری سیاسی و تحریف تفکیک کند. مایکل شودسون در مقالهٔ «The Objectivity Norm in American Journalism» (۲۰۰۱، Journalism) نشان می‌دهد که این هنجار نه از آغاز روزنامه‌نگاری، بلکه در حدود دههٔ ۱۹۲۰ در آمریکا و پس از تجربهٔ تبلیغات جنگ جهانی اول و رشد روابط عمومی، به‌عنوان یک «هنجار حرفه‌ای» شکل گرفت (Schudson, 2001).",
   "main_problem": "چرا و چگونه «عینیت» به هنجار مسلط روزنامه‌نگاری تبدیل شد، این هنجار چه چیزی را تضمین می‌کند و چه محدودیت‌ها و سوءبرداشت‌هایی دربارهٔ آن وجود دارد؟",
   "mechanism": "شودسون مکانیسم تاریخی-حرفه‌ای را توضیح می‌دهد: (۱) پیش از دههٔ ۱۹۲۰، روزنامه‌نگاری آمریکایی بیشتر حزبی و تفسیری بود؛ (۲) تجربهٔ پروپاگاندای جنگ جهانی اول و کشف اینکه «واقعیت» می‌تواند ساخته و دستکاری شود، اعتماد به «حقایق» را تضعیف کرد؛ (۳) در پاسخ، روزنامه‌نگاران مجموعه‌ای از رویه‌ها را برای حفاظت از حرفه در برابر اتهام جانب‌داری ابداع کردند: تفکیک خبر از نظر، استناد به منابع، ارائهٔ نقل‌قول مستقیم، توازن میان طرف‌ها و پرهیز از ارزش‌داوری (Schudson, 2001). تاکمن (Tuchman, 1972) بعدها این رویه‌ها را «آیین راهبردی» (strategic ritual) نامید: تشریفاتی که روزنامه‌نگار را در برابر انتقاد محافظت می‌کند، حتی اگر عینیت مطلق دست‌نیافتنی باشد. بنابراین عینیت در عمل، هنجاری رویه‌ای است: نه ادعای دسترسی به حقیقت مطلق، بلکه تعهد به فرایند قابل‌بازبینی و پاسخ‌گو.",
   "assumptions": [
     "تفکیک واقعیت از ارزش و خبر از نظر، در عمل امکان‌پذیر و مطلوب است.",
     "رویه‌های عینی (استناد، نقل‌قول، توازن) اعتماد عمومی و اعتبار حرفه را حفظ می‌کنند.",
     "مخاطب می‌تواند بر پایهٔ گزارش بی‌طرف، داوری مستقلی دربارهٔ رویداد بسازد."
   ],
   "principles": [
     "واقعیت‌محوری: گزارش باید بر شواهد قابل‌راستی‌آزمایی استوار باشد.",
     "بی‌طرفی و توازن: دیدگاه‌های رقیب باید بازنمایی شوند و جانب‌داری شخصی وارد خبر نشود.",
     "تفکیک خبر و نظر: تحلیل و ارزش‌داوری باید از گزارش خبری جدا بماند."
   ],
   "critiques": [
     "توازن کاذب: ارائهٔ یکسان دیدگاه اقلیت و اکثریت علمی یا واقعی می‌تواند تصویر نادرست بسازد.",
     "پنهان‌سازی موضع: منتقدان می‌گویند «عینیت» گاه به پوششی برای موضع‌گیری ضمنی یا سازش با قدرت تبدیل می‌شود.",
     "دست‌نیافتنی‌بودن: عینیت کامل ممکن نیست و تأکید افراطی بر آن می‌تواند به گزارش‌های بی‌روح و فاقد زمینه منجر شود؛ ازاین‌رو بدیل‌هایی مانند «شفافیت» و «تفسیر مستند» پیشنهاد شده است."
   ],
   "applications": [
     "تدوین منشورهای اخلاق حرفه‌ای و آیین‌نامه‌های تحریریه.",
     "آموزش راستی‌آزمایی و تفکیک خبر از نظر در روزنامه‌نگاری.",
     "تحلیل سواد رسانه‌ای و ارزیابی بی‌طرفی رسانه‌ها."
   ],
   "evolution": "هنجار عینیت در دههٔ ۱۹۲۰-۱۹۳۰ در آمریکا تثبیت شد و پس از جنگ جهانی دوم به معیار حرفه‌ای جهانی تبدیل شد. از دههٔ ۱۹۷۰ با نقدهای مکتب‌های انتقادی و «آیین راهبردی» تاکمن روبه‌رو شد و در دههٔ ۲۰۰۰ بحث «شفافیت به‌جای عینیت» و روزنامه‌نگاری تفسیری و داده‌محور به بازخوانی آن انجامید.",
   "key_concepts": ["عینیت (objectivity)", "واقعیت‌محوری (factuality)", "بی‌طرفی (impartiality)", "آیین راهبردی (strategic ritual)", "توازن خبری (balance)"],
   "studies": ["Schudson, M. (2001). The Objectivity Norm in American Journalism. Journalism, 2(2), 149-170.", "Tuchman, G. (1972). Objectivity as Strategic Ritual. American Journal of Sociology, 77(4), 660-679."],
 },
 "MC-125": {
   "summary": "«نظریهٔ وضعیت جمهورها» (Situational Theory of Publics) چارچوبی از جیمز گرونیگ است که توضیح می‌دهد «عمومی‌ها» (publics) چگونه حول مسئله‌ها شکل می‌گیرند و بر پایهٔ موقعیت ادراکی خود به گروه‌های نهفته، آگاه و فعال تقسیم می‌شوند. گرونیگ در فصل «A Situational Theory of Publics» (۱۹۹۷، در Public Relations Research) تاریخ مفهومی، چالش‌ها و پژوهش‌های تازهٔ این نظریه را صورت‌بندی کرد (Grunig, 1997).",
   "main_problem": "چرا برخی افراد و گروه‌ها نسبت به یک مسئله فعال و مطالبه‌گر می‌شوند و برخی بی‌تفاوت می‌مانند، و چگونه می‌توان بر پایهٔ موقعیت ادراکی، عمومی‌های هدف را برای ارتباطات راهبردی بخش‌بندی کرد؟",
   "mechanism": "نظریه سه متغیر مستقل را برای پیش‌بینی کنش ارتباطی معرفی می‌کند: (۱) «تشخیص مسئله» (problem recognition) — فرد مسئله را به‌عنوان مسئله‌ای واقعی و مرتبط با خود می‌بیند؛ (۲) «تشخیص محدودیت» (constraint recognition) — فرد احساس می‌کند موانع یا محدودیت‌هایی او را از اقدام بازمی‌دارد؛ (۳) «سطح درگیری» (level of involvement) — میزان ارتباط مسئله با منافع و زندگی فرد. ترکیب این سه متغیر، رفتار اطلاعاتی (جست‌وجو در برابر پردازش اطلاعات) و نوع عمومی را تعیین می‌کند: «نهفته» (latent) که مسئله را با منافع خود مرتبط نمی‌بیند، «آگاه» (aware) که مسئله را می‌شناسد اما دست به اقدام نمی‌زند، و «فعال» (active) که با تشخیص مسئله، درگیری بالا و محدودیت کم، به جست‌وجوی اطلاعات و کنش دست می‌زند (Grunig, 1997). این نظریه ابزار تجربی بخش‌بندی عمومی‌ها را در اختیار روابط عمومی راهبردی می‌گذارد.",
   "assumptions": [
     "عمومی‌ها حول مسئله‌ها و نه صرفاً بر پایهٔ ویژگی‌های جمعیت‌شناختی شکل می‌گیرند.",
     "ادراک فرد از مسئله، محدودیت و درگیری، رفتار اطلاعاتی و کنشی او را پیش‌بینی می‌کند.",
     "بخش‌بندی موقعیتی، اثربخشی ارتباطات راهبردی را افزایش می‌دهد."
   ],
   "principles": [
     "مسئله‌محوری: شناخت مسئله، نه تعلق جمعیتی، سازندهٔ عمومی است.",
     "سه‌گانهٔ ادراکی: تشخیص مسئله، تشخیص محدودیت و درگیری، رفتار را تعیین می‌کنند.",
     "طیف فعالیت: عمومی‌ها از نهفته به آگاه و فعال حرکت می‌کنند و ارتباط باید متناسب با هر مرحله طراحی شود."
   ],
   "critiques": [
     "سوگیری فرهنگی: کاربرد نظریه در بافت‌های غیرغربی نشان داده که متغیرها ممکن است معنای متفاوتی داشته باشند و الگو اروپامحور باشد.",
     "مسئلهٔ سنجش: اندازه‌گیری دقیق سه متغیر و تمایز آن‌ها به ابزارهای پرسشی حساس وابسته است.",
     "رسانهٔ دیجیتال: نظریهٔ دههٔ ۱۹۶۰-۱۹۹۰ بیشتر بر رسانه‌های سنتی استوار است و پویایی عمومی‌های آنلاین و کنش شبکه‌ای را کمتر پوشش می‌دهد."
   ],
   "applications": [
     "بخش‌بندی عمومی‌ها و طراحی کمپین‌های روابط عمومی و ارتباطات سلامت.",
     "تحلیل مشارکت عمومی در مسائل محیط‌زیست، سیاست و بحران.",
     "طراحی پیام و کانال ارتباطی متناسب با سطح فعالیت عمومی‌ها."
   ],
   "evolution": "گرونیگ نظریه را از رسالهٔ ۱۹۶۶ خود آغاز کرد و در دهه‌های ۱۹۸۰-۱۹۹۰ با نظریهٔ برتری روابط عمومی پیوند داد. فصل ۱۹۹۷ جمع‌بندی نقدها و پژوهش‌های تازه بود و در دههٔ ۲۰۰۰، پژوهش‌های بین‌فرهنگی و مطالعهٔ عمومی‌های آنلاین و فعال‌شدن شبکه‌ای، آن را گسترش داد.",
   "key_concepts": ["نظریهٔ وضعیت جمهورها (situational theory of publics)", "تشخیص مسئله (problem recognition)", "تشخیص محدودیت (constraint recognition)", "سطح درگیری (level of involvement)", "عمومی فعال (active public)"],
   "studies": ["Grunig, J. E. (1997). A Situational Theory of Publics. In Public Relations Research (pp. 3-48).", "Grunig, J. E. (Ed.). (1992). Excellence in Public Relations and Communication Management. Lawrence Erlbaum."],
 },
 "MC-146": {
   "summary": "«نظریهٔ ارتباط گفت‌وگومدار» (Dialogic Communication Theory) چارچوبی از مایکل کنت و مورین تیلور است که در مقالهٔ «Building Dialogic Relationships through the World Wide Web» (۱۹۹۸، Public Relations Review) مطرح شد. آن‌ها استدلال کردند که وب می‌تواند بستری برای «گفت‌وگو» (dialogue) میان سازمان و عمومی‌ها باشد و پنج اصل گفت‌وگومدار را برای طراحی وب‌سایت‌های روابط عمومی پیشنهاد کردند (Kent & Taylor, 1998).",
   "main_problem": "چگونه سازمان‌ها می‌توانند از ارتباط یک‌سویهٔ اقناعی به گفت‌وگوی دوسویه و رابطه‌محور با عمومی‌ها گذر کنند، و رسانه‌های تعاملی چه امکانی برای تحقق این گفت‌وگو فراهم می‌کنند؟",
   "mechanism": "کنت و تیلور گفت‌وگو را نه یک فن اقناع، بلکه یک «جهت‌گیری» (orientation) ارتباطی می‌بینند که در آن طرفین به‌عنوان سوژه‌های برابر به هم گوش می‌دهند. آن‌ها پنج اصل عملیاتی را برای محیط وب صورت‌بندی کردند: (۱) «حلقهٔ گفت‌وگو» (dialogic loop) — فراهم کردن امکان بازخورد و پاسخ سازمان به پرسش‌های مخاطب؛ (۲) «سودمندی اطلاعات» (usefulness of information) — انتشار اطلاعات مرتبط با منافع عمومی‌ها، نه صرفاً تبلیغ سازمان؛ (۳) «تولید بازدید مجدد» (generation of return visits) — به‌روزرسانی منظم و دعوت به بازگشت؛ (۴) «سهولت رابط کاربری» (intuitiveness/ease of interface) — دسترسی آسان و منطقی به محتوا؛ (۵) «قاعدهٔ حفظ بازدیدکنندگان» (rule of conservation of visitors) — حفظ مخاطب در سایت و پرهیز از هدایت عجولانه به بیرون (Kent & Taylor, 1998). در نظریهٔ گفت‌وگویی متأخرتر (2002)، آن‌ها پنج ویژگی رابطهٔ گفت‌وگومدار — دوسویگی، نزدیکی/تماس، همدلی، ریسک‌پذیری و تعهد — را صورتبندی کردند.",
   "assumptions": [
     "گفت‌وگوی واقعی مستلزم به‌رسمیت‌شناختن مخاطب به‌عنوان سوژه‌ای برابر است، نه هدفی برای اقناع.",
     "ارتباط دوسویه و رابطهٔ بلندمدت، اثربخشی ارتباطات سازمانی را پایدارتر می‌کند.",
     "رسانه‌های تعاملی امکان بازخورد و پاسخ‌گویی را در مقیاس گسترده فراهم می‌کنند."
   ],
   "principles": [
     "دوسویگی: ارتباط باید امکان گفت‌وگو و پاسخ برابر را فراهم کند.",
     "همدلی و احترام: سازمان باید منافع و دیدگاه عمومی‌ها را جدی بگیرد.",
     "تعهد و ریسک: پذیرش پیامدهای گفت‌وگوی واقعی، از جمله احتمال تغییر موضع سازمان."
   ],
   "critiques": [
     "شکاف نظر و عمل: پژوهش‌های تجربی نشان می‌دهند بسیاری از سازمان‌ها فقط «ظاهر» گفت‌وگو را برمی‌سازند و حلقهٔ پاسخ‌دهی واقعی را فراهم نمی‌کنند.",
     "عدم تقارن قدرت: در روابط سازمان-عمومی، قدرت نابرابر است و گفت‌وگوی «آرمانی» به‌سختی محقق می‌شود.",
     "سنجش دشوار: اثربخشی گفت‌وگو به‌سختی قابل اندازه‌گیری است و به شاخص‌های فرایندی و رابطه‌ای وابسته است."
   ],
   "applications": [
     "طراحی وب‌سایت و رسانه‌های اجتماعی سازمان‌ها با رویکرد گفت‌وگومدار.",
     "تحلیل ارتباط سازمان‌های غیردولتی و دولتی با عمومی‌ها و ذی‌نفعان.",
     "مدیریت بحران از طریق پاسخ‌گویی و شنیدن فعال؛ طراحی فرایندهای مشارکت عمومی."
   ],
   "evolution": "کنت و تیلور (1998) چارچوب گفت‌وگویی وب را ارائه کردند و در ۲۰۰۲ آن را به نظریهٔ عمومی گفت‌وگو در روابط عمومی گسترش دادند. در دههٔ ۲۰۱۰، پژوهش‌های رسانه‌های اجتماعی، گفت‌وگوی سازمانی را در بستر پلتفرمی و شبکه‌ای تحلیل کرد و بحث «گفت‌وگوی اجرایی» (executive dialogue) و فناوری‌های گفت‌وگوگستر شکل گرفت.",
   "key_concepts": ["گفت‌وگومداری (dialogic communication)", "حلقهٔ گفت‌وگو (dialogic loop)", "دوسویگی (mutuality)", "همدلی (empathy)", "حفظ بازدیدکننده (conservation of visitors)"],
   "studies": ["Kent, M. L., & Taylor, M. (1998). Building Dialogic Relationships through the World Wide Web. Public Relations Review, 24(3), 321-334.", "Kent, M. L., & Taylor, M. (2002). Toward a Dialogic Theory of Public Relations. Public Relations Review, 28(1), 21-37."],
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
    codes = ["MC-083", "MC-043", "MC-125", "MC-146"]
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
    print("BATCH37 THEORY DONE")

if __name__ == "__main__":
    main()
