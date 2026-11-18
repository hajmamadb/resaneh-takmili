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


def wc(v):
    if v is None:
        return 0
    if isinstance(v, str):
        return len(v.split())
    if isinstance(v, (list, tuple)):
        return sum(len(str(x).split()) for x in v)
    return 0


def has_content(v):
    if v is None:
        return False
    if isinstance(v, str):
        return bool(v.strip())
    if isinstance(v, (list, dict)):
        return len(v) > 0
    return True


REQUIRED_SECTIONS = ["summary", "definition", "main_problem", "mechanism", "assumptions",
                     "principles", "critiques", "applications", "evolution", "key_concepts",
                     "theorists", "model", "studies"]
WORD_KEYS = ["summary", "definition", "main_problem", "mechanism", "critiques",
             "applications", "evolution", "key_concepts", "principles", "studies", "assumptions"]


def rubric(p, n_verified, n_sources, n_relations):
    present = sum(1 for k in REQUIRED_SECTIONS if has_content(p.get(k)))
    structure = round(15 * min(1, present / 7))
    words = sum(wc(p.get(k)) for k in WORD_KEYS)
    if words >= 500:
        analysis = 15
    elif words >= 300:
        analysis = 13
    elif words >= 180:
        analysis = 11
    elif words >= 100:
        analysis = 8
    else:
        analysis = 3
    if n_verified >= 1 and n_sources >= 2:
        citation = 20
    elif n_verified >= 1:
        citation = 17
    elif n_sources >= 1:
        citation = 10
    else:
        citation = 0
    accuracy = 0
    if has_content(p.get("summary")) and has_content(p.get("definition")):
        accuracy += 10
    if n_verified >= 1:
        accuracy += 9
    if present >= 6:
        accuracy += 6
    accuracy = min(25, accuracy)
    relations = 10 if n_relations >= 1 else 6
    classification = 5 if (p.get("mapping") or p.get("category_id")) else 0
    clarity = 5 if has_content(p.get("summary")) else 0
    currency = 5
    score = structure + analysis + citation + accuracy + relations + classification + clarity + currency
    detail = "structure=%d analysis=%d citation=%d accuracy=%d relations=%d classification=%d clarity=%d currency=%d" % (
        structure, analysis, citation, accuracy, relations, classification, clarity, currency)
    return score, detail, words


def ensure_source(cur, src):
    if src.get("doi"):
        cur.execute("SELECT id FROM kb_sources WHERE doi=%s LIMIT 1", (src["doi"],))
        r = cur.fetchone()
        if r:
            return r[0]
    cur.execute("SELECT id FROM kb_sources WHERE title_en=%s AND year=%s LIMIT 1",
                (src["title_en"], src["year"]))
    r = cur.fetchone()
    if r:
        return r[0]
    cur.execute("""INSERT INTO kb_sources
        (kind,title_fa,title_en,year,publisher,doi,isbn,issn,url,language,access_type,bibliographic,work_id)
        VALUES (%s,%s,%s,%s,%s,%s,%s,NULL,%s,%s,'unknown',%s,NULL)""",
                (src["kind"], src["title_fa"], src["title_en"], src["year"], src["publisher"],
                 src.get("doi"), src.get("isbn"), src.get("url"), src["language"],
                 json.dumps({"authors": src["authors"], "citation": src["citation"]}, ensure_ascii=False)))
    return cur.lastrowid



YEAR_FIX.update({
    "MC-582": "year corrected 2000 -> 2001 (verified anchor: Baker & Martinson, TARES Test, 2001); note: editorial card theorist attribution was unverifiable and documentation rebuilt from verified literature",
    "MC-598": "no year change; note: editorial card core_logic was a mismatched media-economics template, documentation rebuilt from Heath (1993) and Ihlen (2011)",
})


def main():
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="433700",
                           database=DB, charset="utf8mb4", autocommit=False)
    cur = conn.cursor()
    codes = list(ENRICH.keys())
    ph = ",".join(["%s"] * len(codes))
    cur.execute("SELECT id,code,properties FROM kb_entities WHERE code IN (%s)" % ph, codes)
    rows = cur.fetchall()
    found = {r[1]: r for r in rows}
    missing = [c for c in codes if c not in found]
    assert not missing, "not found: %s" % missing

    snap = []
    for code, (eid, _c, props) in found.items():
        snap.append({"id": eid, "code": code, "properties": json.loads(props)})
    with open(BACKUP, "w", encoding="utf-8") as f:
        json.dump(snap, f, ensure_ascii=False, indent=1)
    print("backup ->", len(snap), "rows")

    for code in codes:
        eid, _c, props = found[code]
        p = json.loads(props)
        en = ENRICH[code]

        if "critique_text" in en:
            p["critique"] = en["critique_text"]
        if "example_text" in en:
            p["example"] = en["example_text"]
        for k, v in en.items():
            if k in ("critique_text", "example_text"):
                continue
            p[k] = v

        p["sources"] = []
        p["citations"] = []
        for src in S[code]:
            p["sources"].append({
                "citation": src["citation"],
                "title_en": src["title_en"],
                "title_fa": src["title_fa"],
                "year": src["year"],
                "doi": src.get("doi"),
                "url": src.get("url"),
                "language": src["language"],
                "verified": src["verified"],
            })
            p["citations"].append({
                "source": src["citation"],
                "locator": src["locator"],
                "supports": src["supports"],
                "verified": src["verified"],
            })

        cur.execute("SELECT COUNT(*) FROM kb_relations WHERE source_id=%s OR target_id=%s", (eid, eid))
        n_rel = cur.fetchone()[0]
        n_sources = len(p["sources"])
        n_verified = sum(1 for x in p["citations"] if x.get("verified"))
        score, detail, words = rubric(p, n_verified, n_sources, n_rel)

        p["quality_score"] = score
        p["quality_assessment"] = "ارزیابی خودکار SPEC §6.1: %d/100 (نمره پایه؛ نیازمند بازبینی علمی انسانی)" % score
        p["status_scientific_note"] = "مستندسازی با منابع تأییدشده شبکه‌ای؛ نمره بر پایه سنجه خودکار است و جانشین داوری علمی (SPEC §6.4) نیست."
        p["updated_at"] = NOW
        p["updated_by"] = STAMP

        if code in NAME_FIX:
            fa_name, en_name, why = NAME_FIX[code]
            cur.execute("UPDATE kb_entities SET canonical_name_fa=%s, canonical_name_en=%s WHERE id=%s",
                        (fa_name, en_name, eid))
            cur.execute("""INSERT INTO kb_audit_log (entity_code,action,detail,source,created_at)
                VALUES (%s,'DOC_FIX',%s,%s,%s)""",
                        (code, json.dumps({"fix": why}, ensure_ascii=False), STAMP, NOW))

        if code in YEAR_FIX:
            cur.execute("""INSERT INTO kb_audit_log (entity_code,action,detail,source,created_at)
                VALUES (%s,'DOC_FIX',%s,%s,%s)""",
                        (code, json.dumps({"fix": YEAR_FIX[code]}, ensure_ascii=False), STAMP, NOW))

        cur.execute("UPDATE kb_entities SET properties=%s, version=version+1, updated_at=%s WHERE id=%s",
                    (json.dumps(p, ensure_ascii=False), NOW, eid))
        cur.execute("SELECT version FROM kb_entities WHERE id=%s", (eid,))
        new_version = cur.fetchone()[0]

        for src in S[code]:
            sid = ensure_source(cur, src)
            cur.execute("SELECT id FROM kb_evidence WHERE about_code=%s AND source_id=%s LIMIT 1", (code, sid))
            if cur.fetchone():
                continue
            lt = {"work": "SECTION", "page_range": "PAGE", "CHAPTER": "CHAPTER", "PAGE": "PAGE"}.get(src["locator_type"], "SECTION")
            cur.execute("""INSERT INTO kb_citations
                (source_id,locator_type,locator_value,quoted_text,paraphrase,citation_style,language,accessed_at)
                VALUES (%s,%s,%s,NULL,%s,'apa',%s,%s)""",
                        (sid, lt, src["locator"], src["supports"], src["language"], NOW))
            cid = cur.lastrowid
            cur.execute("""INSERT INTO kb_evidence
                (source_id,citation_id,about_code,evidence_type,evidence_summary,quoted_content,locator,
                 page_start,page_end,direction,extraction_method,verification_status,extraction_confidence)
                VALUES (%s,%s,%s,'bibliographic_reference',%s,NULL,%s,NULL,NULL,'supports','ai_extraction',%s,NULL)""",
                        (sid, cid, code, src["supports"], src["locator"],
                         "verified" if src["verified"] else "unverified"))

        cur.execute("""INSERT INTO kb_entity_versions
            (entity_id,version,snapshot,change_reason,changed_by,created_at)
            VALUES (%s,%s,%s,%s,%s,%s)""",
                    (eid, new_version, json.dumps(p, ensure_ascii=False),
                     "full documentation enrichment + verified sources", STAMP, NOW))

        cur.execute("""INSERT INTO kb_audit_log (entity_code,action,detail,source,created_at)
            VALUES (%s,'DOC_ENRICH',%s,%s,%s)""",
                    (code, json.dumps({"score": score, "words": words, "sources": n_sources,
                                       "verified": n_verified, "batch": 219}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH219 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
