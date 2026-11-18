# -*- coding: utf-8 -*-
"""Batch 219: repair MC-590, MC-591, MC-593, MC-594, MC-595."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch219-20261117"
NOW = "2026-11-17 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch219.json"

S = {
    "MC-590": [
        dict(kind="JOURNAL_ARTICLE", title_en="The Determinants of Trust and Credibility in Environmental Risk Communication: An Empirical Study",
             title_fa="عوامل تعیین‌کنندهٔ اعتماد و اعتبار در ارتباطات خطر زیست‌محیطی",
             authors="Richard G. Peters; Vincent T. Covello; David B. McCallum", year=1997,
             publisher="Risk Analysis", doi="10.1111/j.1539-6924.1997.tb00842.x",
             url="https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1539-6924.1997.tb00842.x",
             language="en", isbn=None,
             citation="Peters, R. G., Covello, V. T., & McCallum, D. B. (1997). The determinants of trust and credibility in environmental risk communication: An empirical study. Risk Analysis, 17(1), 43-54.",
             locator="17(1), 43-54", locator_type="PAGE",
             supports="competence, care and honesty as dimensions of trust and credibility", verified=True),
        dict(kind="JOURNAL_ARTICLE", title_en="Risk Communication and Message Mapping: A New Tool for Communicating Effectively in Public Health Emergencies and Disasters",
             title_fa="ارتباطات خطر و نقشه‌سازی پیام: ابزاری تازه برای ارتباط مؤثر در بحران‌های سلامت عمومی",
             authors="Vincent T. Covello", year=2006, publisher="Journal of Emergency Management",
             doi="10.5055/jem.2006.0030", url="https://wmpllc.org/ojs/index.php/jem/article/view/1760",
             language="en", isbn=None,
             citation="Covello, V. T. (2006). Risk communication and message mapping: A new tool for communicating effectively in public health emergencies and disasters. Journal of Emergency Management, 4(3), 25-40.",
             locator="4(3), 25-40", locator_type="PAGE",
             supports="message mapping as structured risk communication practice", verified=True),
    ],
    "MC-591": [
        dict(kind="JOURNAL_ARTICLE", title_en="How Publics Respond to Crisis Communication Strategies: The Interplay of Information Form and Source",
             title_fa="واکنش عمومی‌ها به راهبردهای ارتباط بحران: درهم‌تنیدگی شکل و منبع اطلاعات",
             authors="Brooke Fisher Liu; Lucinda Austin; Yan Jin", year=2011,
             publisher="Public Relations Review", doi=None,
             url="https://www.sciencedirect.com/science/article/abs/pii/S0363811111000956",
             language="en", isbn=None,
             citation="Liu, B. F., Austin, L., & Jin, Y. (2011). How publics respond to crisis communication strategies: The interplay of information form and source. Public Relations Review, 37(4), 345-353.",
             locator="37(4), 345-353", locator_type="PAGE",
             supports="social-mediated crisis communication model with three public types", verified=True),
        dict(kind="BOOK_CHAPTER", title_en="Social-Mediated Crisis Communication Research",
             title_fa="پژوهش ارتباط بحران با میانجیگری رسانه‌های اجتماعی",
             authors="Yan Jin", year=2022, publisher="Wiley",
             doi="10.1002/9781119678953.ch11",
             url="https://onlinelibrary.wiley.com/doi/abs/10.1002/9781119678953.ch11",
             language="en", isbn=None,
             citation="Jin, Y. (2022). Social-mediated crisis communication research. In The Handbook of Crisis Communication (2nd ed.). Hoboken: Wiley.",
             locator="ch. 11", locator_type="CHAPTER",
             supports="review and update of the social-mediated crisis communication framework", verified=True),
    ],
    "MC-593": [
        dict(kind="JOURNAL_ARTICLE", title_en="The Reputational Landscape",
             title_fa="چشم‌انداز شهرت",
             authors="Charles J. Fombrun; Cees B. M. van Riel", year=1997,
             publisher="Corporate Reputation Review",
             doi="10.1057/palgrave.crr.1540024",
             url="https://link.springer.com/article/10.1057/palgrave.crr.1540024",
             language="en", isbn=None,
             citation="Fombrun, C. J., & van Riel, C. B. M. (1997). The reputational landscape. Corporate Reputation Review, 1(1), 5-13.",
             locator="1(1), 5-13", locator_type="PAGE",
             supports="reputation as collective and durable representation across disciplines", verified=True),
        dict(kind="JOURNAL_ARTICLE", title_en="Corporate Reputation: The Definitional Landscape",
             title_fa="شهرت شرکتی: چشم‌انداز تعریف‌ها",
             authors="Michael L. Barnett; John M. Jermier; Barbara A. Lafferty", year=2006,
             publisher="Corporate Reputation Review", doi=None,
             url="https://www.mv.helsinki.fi/home/aula/Top20/corp-reputation-definitional-landscape.pdf",
             language="en", isbn=None,
             citation="Barnett, M. L., Jermier, J. M., & Lafferty, B. A. (2006). Corporate reputation: The definitional landscape. Corporate Reputation Review.",
             locator="article", locator_type="PAGE",
             supports="analysis of competing definitions of corporate reputation", verified=True),
    ],
    "MC-594": [
        dict(kind="JOURNAL_ARTICLE", title_en="Building Dialogic Relationships Through the World Wide Web",
             title_fa="ساختن روابط گفت‌وگویی از راه وب جهانی",
             authors="Michael L. Kent; Maureen Taylor", year=1998,
             publisher="Public Relations Review", doi=None,
             url="https://www.sciencedirect.com/science/article/pii/S036381119980143X",
             language="en", isbn=None,
             citation="Kent, M. L., & Taylor, M. (1998). Building dialogic relationships through the World Wide Web. Public Relations Review, 24(3), 321-334.",
             locator="24(3), 321-334", locator_type="PAGE",
             supports="five dialogic principles for organizational websites", verified=True),
        dict(kind="JOURNAL_ARTICLE", title_en="Toward a Dialogic Theory of Public Relations",
             title_fa="به‌سوی نظریهٔ گفت‌وگویی روابط عمومی",
             authors="Michael L. Kent; Maureen Taylor", year=2002,
             publisher="Public Relations Review", doi=None,
             url="https://www.sciencedirect.com/science/article/abs/pii/S036381110200108X",
             language="en", isbn=None,
             citation="Kent, M. L., & Taylor, M. (2002). Toward a dialogic theory of public relations. Public Relations Review, 28(1), 21-37.",
             locator="28(1), 21-37", locator_type="PAGE",
             supports="dialogic theory as the normative basis of the web model", verified=True),
    ],
    "MC-595": [
        dict(kind="JOURNAL_ARTICLE", title_en="A Delphi Study of the Future of New Technology Research in Public Relations",
             title_fa="پژوهشی دلفی دربارهٔ آیندهٔ پژوهش فناوری‌های نو در روابط عمومی",
             authors="Michael L. Kent; Adam J. Saffer", year=2014,
             publisher="Public Relations Review", doi=None,
             url="http://mlkent.com/PDFs/Kent_Saffer_Delphi_2014B.pdf",
             language="en", isbn=None,
             citation="Kent, M. L., & Saffer, A. J. (2014). A Delphi study of the future of new technology research in public relations. Public Relations Review, 40(3), 568-576.",
             locator="40(3), 568-576", locator_type="PAGE",
             supports="expert consensus on technology, interaction and ethics in public relations", verified=True),
        dict(kind="WEBSITE", title_en="A Delphi Study of the Future of New Technology Research in Public Relations (record)",
             title_fa="رکورد پژوهش دلفی دربارهٔ آیندهٔ پژوهش فناوری‌های نو",
             authors="University of Minnesota Experts", year=2014, publisher="University of Minnesota",
             doi=None, url="https://experts.umn.edu/en/publications/a-delphi-study-of-the-future-of-new-technology-research-in-public",
             language="en", isbn=None,
             citation="University of Minnesota Experts. (2014). Record for A Delphi study of the future of new technology research in public relations.",
             locator="record", locator_type="PAGE",
             supports="institutional record confirming publication details", verified=True),
    ],
}

ENRICH = {
    "MC-590": dict(
        needs_enrichment=False,
        level="میان",
        related_approaches="ارتباط بحران؛ ارتباط سلامت؛ مدیریت ریسک؛ اعتماد عمومی؛ نقشه‌سازی پیام.",
        recommended_sources="«عوامل تعیین‌کنندهٔ اعتماد و اعتبار در ارتباطات خطر» (پیترز، کاوالو و مک‌کالم، ۱۹۹۷)؛ «ارتباطات خطر و نقشه‌سازی پیام» (کاوالو، ۲۰۰۶)؛ «ارتباط خطر: راهنمای عملی» (کاوالو و همکاران).",
        detailed_analysis=("۱. بنیان و منطق نظری\nکاوالو و همکاران در پژوهش ۱۹۹۷ نشان دادند ارتباط دربارهٔ خطر، انتقال اطلاعات فنی نیست، بلکه ساختن فهم مشترک و اعتماد است. "
                           "آن‌ها دریافتند در وضعیت خطر، مخاطب با اضطراب و اطلاعات ناقص روبه‌روست و اثربخشی پیام بیش از دقت عددی به اعتبار منبع بستگی دارد.\n\n"
                           "۲. ساختارهای مفهومی\nسه بُعد اعتبار شناسایی شد: شایستگی و تخصص، توجه و مراقبت، و صداقت و شفافیت. نقشه‌سازی پیام (کاوالو، ۲۰۰۶) این ابعاد را به قالب عملی پیام بحران تبدیل کرد.\n\n"
                           "۳. نمونه‌های تحلیلی\nدر بحران سلامت عمومی، پیامی که فقط آمار می‌دهد اما دلسوزی و شفافیت نشان نمی‌دهد اعتماد نمی‌سازد؛ پیام کوتاه و تک‌پیامی با منبع شناخته‌شده اثر بیشتری دارد؛ نقشهٔ پیام با سه کلید اصلی و سه پیام پشتیبان نمونهٔ اجرای آن است.\n\n"
                           "۴. نقدها و چالش‌ها\nمدل عمدتاً بر اعتبار منبع متمرکز است و شرایط ساختاری و بی‌اعتمادی نهادی را کم‌بررسی می‌کند؛ سنجش اعتماد در بحران واقعی دشوار است؛ تفاوت فرهنگ‌ها در ابراز مراقبت یکدست نیست؛ و خطر ساده‌سازی بیش از حد پیام علمی وجود دارد.\n\n"
                           "۵. سیر تاریخی\nپژوهش ۱۹۹۷ چارچوب اعتبار را تثبیت کرد و کارهای بعدی کاوالو آن را به نقشه‌سازی پیام و راهنمای عملی بحران گستردند.\n\n"
                           "۶. جایگاه در بحث روز\nدر بحران‌های سلامت و محیط زیست، مدل ارتباط خطر یادآوری می‌کند که اعتماد پیش از بحران ساخته می‌شود و در بحران تنها مصرف می‌شود."),
    ),
    "MC-591": dict(
        needs_enrichment=False,
        level="میان",
        related_approaches="ارتباط بحران؛ مدل اس‌سی‌سی‌تی؛ رسانه‌های اجتماعی؛ ارتباطات مخاطب؛ اعتبار منبع.",
        recommended_sources="«واکنش عمومی‌ها به راهبردهای ارتباط بحران» (لیو، آستین و جین، ۲۰۱۱)؛ «پژوهش ارتباط بحران با میانجیگری رسانه‌های اجتماعی» (جین، ۲۰۲۲)؛ «ارتباط بحران در عصر دیجیتال» (کومبز).",
        detailed_analysis=("۱. بنیان و منطق نظری\nلیو، آستین و جین (۲۰۱۱) نشان دادند در بحران، مخاطبان دیگر تنها از رسانه‌های رسمی اطلاعات نمی‌گیرند، بلکه از رسانه‌های اجتماعی، وبگاه‌ها، دوستان و منابع غیررسمی نیز بهره می‌برند. "
                           "بنابراین اثربخشی پیام رسمی را نمی‌توان جدا از جریان اطلاعات غیررسمی سنجید.\n\n"
                           "۲. ساختارهای مفهومی\nسه گروه عمومی از هم جدا می‌شوند: عمومی‌های مستقیم که مستقیماً درگیر بحران‌اند، عمومی‌های غیرمستقیم که از طریق دیگران خبر را می‌شنوند، و عمومی‌های دهان‌به‌دهان که خود اطلاعات را در شبکه بازنشر می‌کنند. سه عامل منشأ بحران، شکل اطلاعات و منبع اطلاعات واکنش آن‌ها را می‌سازد.\n\n"
                           "۳. نمونه‌های تحلیلی\nاطلاعاتی که از شبکهٔ اجتماعی و از تجربهٔ نزدیکان می‌آید، به‌ویژه در بحران محلی، اعتبار و اثر بیشتری از بیانیهٔ رسمی دارد؛ سازمانی که فقط بیانیه می‌دهد و در شبکه‌ها حاضر نیست، کنترل روایت را به دیگران می‌سپارد.\n\n"
                           "۴. نقدها و چالش‌ها\nمدل بیشتر توصیفی است و وزن دقیق هر منبع را تعیین نمی‌کند؛ پویایی سریع شبکه‌ها سنجش را دشوار می‌کند؛ تفاوت پلتفرم‌ها و الگوریتم‌ها کم‌بررسی می‌ماند؛ و تعمیم یافته‌های آزمایشی به بحران‌های واقعی محدود است.\n\n"
                           "۵. سیر تاریخی\nمقالهٔ ۲۰۱۱ چارچوب ارتباط بحران با میانجیگری رسانه‌های اجتماعی را ساخت و مرور ۲۰۲۲ جین آن را با شواهد دههٔ بعد به‌روز کرد.\n\n"
                           "۶. جایگاه در بحث روز\nدر بحران‌هایی که نخستین خبر از شبکه‌های اجتماعی منتشر می‌شود، مدل یادآوری می‌کند سازمان باید هم‌زمان در کانال رسمی و غیررسمی حاضر و پاسخ‌گو باشد."),
    ),
    "MC-593": dict(
        needs_enrichment=False,
        level="میان",
        related_approaches="مدیریت شهرت؛ هویت و تصویر سازمانی؛ اعتماد سازمانی؛ ارتباط بحران؛ ارزش برند.",
        recommended_sources="«چشم‌انداز شهرت» (فومبران و فان ریل، ۱۹۹۷)؛ «شهرت شرکتی: چشم‌انداز تعریف‌ها» (بارنت، جرمیر و لافرتی، ۲۰۰۶)؛ «شهرت: تحقق ارزش از هویت شرکت» (فومبران).",
        detailed_analysis=("۱. بنیان و منطق نظری\nفومبران و فان ریل (۱۹۹۷) شهرت را نه تصویر تبلیغاتی، بلکه بازنمایی جمعی و پایدار از سازمان در ذهن ذی‌نفعان دانستند که از ادراک عملکرد گذشته و انتظار عملکرد آینده ساخته می‌شود. "
                           "آن‌ها نشان دادند شهرت مفهومی چندرشته‌ای است و اقتصاد، راهبرد، بازاریابی، جامعه‌شناسی و روان‌شناسی هر یک بخشی از آن را روشن می‌کنند.\n\n"
                           "۲. ساختارهای مفهومی\nهویت (آنچه سازمان هست)، تصویر (آنچه مخاطب می‌بیند) و شهرت (ارزیابی جمعی پایدار) از هم جدا می‌شوند؛ اعتبار، بُعد ارتباطی و پیامی شهرت است.\n\n"
                           "۳. نمونه‌های تحلیلی\nسازمانی با عملکرد مالی خوب اما رسوایی اخلاقی می‌تواند شهرت کلی خود را از دست بدهد؛ شهرت مثبت در بحران مانند ذخیرهٔ اعتماد عمل می‌کند و هزینهٔ ترمیم را کاهش می‌دهد.\n\n"
                           "۴. نقدها و چالش‌ها\nسنجش شهرت به شاخص‌های ذهنی و نظرسنجی وابسته است؛ خطر اثر هاله‌ای و همبستگی کاذب ابعاد وجود دارد؛ تعریف‌های رقیب هنوز یکدست نیست (بارنت و همکاران، ۲۰۰۶)؛ و شهرت می‌تواند با تبلیغ و روایت مدیریتی دستکاری شود.\n\n"
                           "۵. سیر تاریخی\nمقالهٔ ۱۹۹۷ چارچوب چندرشته‌ای شهرت را ساخت، مرور تعریف‌ها در ۲۰۰۶ تنوع مفهومی را نشان داد و پژوهش‌های بعدی شهرت را به ارزش برند و ارتباط بحران پیوند دادند.\n\n"
                           "۶. جایگاه در بحث روز\nدر اقتصاد توجه و رسوایی‌های دیجیتال، شهرت دارایی راهبردی سازمان است و مدیریت آن به رفتار واقعی و شفافیت وابسته است، نه به تبلیغ تصویر."),
    ),
    "MC-594": dict(
        needs_enrichment=False,
        level="میان",
        related_approaches="نظریهٔ گفت‌وگویی؛ مدل دوسویهٔ متقارن؛ وب‌سایت سازمانی؛ طراحی تجربهٔ کاربر؛ روابط عمومی دیجیتال.",
        recommended_sources="«ساختن روابط گفت‌وگویی از راه وب جهانی» (کنت و تیلور، ۱۹۹۸)؛ «به‌سوی نظریهٔ گفت‌وگویی روابط عمومی» (کنت و تیلور، ۲۰۰۲)؛ «مدل گفت‌وگویی» (کنت و تیلور).",
        detailed_analysis=("۱. بنیان و منطق نظری\nکنت و تیلور (۱۹۹۸) وب را نه تابلوی تبلیغات، بلکه فضایی برای گفت‌وگوی واقعی سازمان با مخاطبان دانستند و پنج اصل گفت‌وگویی برای وبگاه سازمانی صورت‌بندی کردند: "
                           "حلقهٔ گفت‌وگو (امکان تعامل دوسویه و پاسخ)، سودمندی اطلاعات برای همهٔ مخاطبان، ایجاد انگیزهٔ بازگشت، آسانی استفاده و رابط شهودی، و حفظ بازدیدکننده در وبگاه.\n\n"
                           "۲. ساختارهای مفهومی\nاین پنج اصل، وبگاه را از آرشیو یک‌سویه به محیط رابطه‌سازی تبدیل می‌کنند. حلقهٔ گفت‌وگو هستهٔ مدل است و بقیه اصول آن را پشتیبانی می‌کنند.\n\n"
                           "۳. نمونه‌های تحلیلی\nوبگاهی که فقط بیانیه‌های مطبوعاتی می‌گذارد، پنج اصل را نقض می‌کند؛ وبگاهی که فرم پرسش، پاسخ عمومی، اطلاعات مفید و مسیر بازگشت روشن دارد، در عمل گفت‌وگویی است؛ شبکه‌های اجتماعی بعدی همین اصول را گستردند.\n\n"
                           "۴. نقدها و چالش‌ها\nفناوری به‌تنهایی گفت‌وگو نمی‌سازد؛ بسیاری از سازمان‌ها وبگاه را کانال یک‌سویه نگه داشته‌اند؛ مدل اصول را هنجاری بیان می‌کند و سنجش تجربی دشوار است؛ و به پویایی پلتفرم‌های اجتماعی و الگوریتم‌ها نمی‌پردازد.\n\n"
                           "۵. سیر تاریخی\nمقالهٔ ۱۹۹۸ مدل وب را ساخت، نظریهٔ گفت‌وگویی ۲۰۰۲ بنیاد هنجاری آن را گسترد و پژوهش‌های بعدی آن را به وب دو نقطه صفر و رسانه‌های اجتماعی بردند.\n\n"
                           "۶. جایگاه در بحث روز\nدر طراحی وبگاه و کانال‌های دیجیتال سازمان، پنج اصل گفت‌وگویی همچنان معیار سنجش کیفیت رابطه است، هرچند امروز باید در بستر پلتفرم‌های اجتماعی بازخوانی شود."),
    ),
    "MC-595": dict(
        needs_enrichment=False,
        level="میان",
        related_approaches="روابط عمومی دیجیتال؛ نظریهٔ گفت‌وگویی؛ مدیریت بحران در شبکه‌های اجتماعی؛ اخلاق ارتباطات؛ سنجش اثر.",
        recommended_sources="«پژوهشی دلفی دربارهٔ آیندهٔ پژوهش فناوری‌های نو در روابط عمومی» (کنت و سفر، ۲۰۱۴)؛ «ساختن روابط گفت‌وگویی از راه وب جهانی» (کنت و تیلور، ۱۹۹۸)؛ «ارتباط بحران با میانجیگری رسانه‌های اجتماعی» (جین).",
        detailed_analysis=("۱. بنیان و منطق نظری\nکنت و سافر (۲۰۱۴) در پژوهش دلفی با خبرگان نشان دادند رسانه‌های اجتماعی کانال تبلیغ اضافه نیستند، بلکه محیطی برای بازآرایی رابطهٔ سازمان و مخاطب‌اند. "
                           "فناوری‌های نو سه تغییر بنیادی می‌سازند: مخاطب از دریافت‌کننده به مشارکت‌کننده تبدیل می‌شود، سازمان ناچار به پاسخ‌گویی و شفافیت می‌شود و مرز ارتباط رسمی و گفت‌وگوی عمومی کم‌رنگ می‌شود.\n\n"
                           "۲. ساختارهای مفهومی\nمشارکت مخاطب، پاسخ‌گویی، شفافیت، اعتماد، اخلاق و سنجش اثر سازه‌های اصلی‌اند. خروجی دلفی بر تعامل و اخلاق به‌جای فناوری‌محوری تأکید داشت.\n\n"
                           "۳. نمونه‌های تحلیلی\nسازمانی که در شبکه‌های اجتماعی فقط اطلاعیه منتشر می‌کند، مشارکت نمی‌سازد؛ سازمانی که به پرسش‌ها پاسخ می‌دهد و اشتباه را می‌پذیرد، اعتماد می‌سازد؛ در بحران، پاسخ سریع و انسانی در همان کانال، نمونهٔ اجرای مدل است.\n\n"
                           "۴. نقدها و چالش‌ها\nدلفی اجماع خبرگان است و پیش‌بینی تجربی نیست؛ شکاف میان اصول هنجاری و عمل سازمان‌ها پایدار است؛ سنجش اثر رابطه در پلتفرم‌ها دشوار است؛ و مسائل حریم خصوصی، اخبار جعلی و الگوریتم‌ها در مدل کم‌بررسی مانده‌اند.\n\n"
                           "۵. سیر تاریخی\nپژوهش ۲۰۱۴ جمع‌بندی دو دههٔ پژوهش فناوری در روابط عمومی بود و مسیر آینده را به تعامل، اعتماد و اخلاق جهت داد.\n\n"
                           "۶. جایگاه در بحث روز\nدر عصر پلتفرم و هوش مصنوعی، مدل یادآوری می‌کند که ارزش رسانه‌های اجتماعی برای روابط عمومی در گفت‌وگو و اعتماد است، نه در حجم انتشار."),
    ),
}

NAME_FIX = {}

YEAR_FIX = {
    "MC-590": "replaced media-economics template analysis with Peters-Covello trust analysis; rebuilt recommendations",
    "MC-591": "replaced media-economics template analysis with SMCC analysis; rebuilt recommendations",
    "MC-593": "replaced media-economics template analysis with reputation-credibility analysis; rebuilt recommendations",
    "MC-594": "replaced media-economics template analysis with Kent-Taylor web dialogue analysis; cross-linked to MC-495",
    "MC-595": "replaced media-economics template analysis with Kent-Saffer Delphi analysis; rebuilt recommendations",
}
