# -*- coding: utf-8 -*-
"""Batch 202: MC-638, MC-642, MC-442, MC-645, MC-647 (FRAMEWORK)."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch202-20261117"
NOW = "2026-11-17 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch202.json"

S = {
    "MC-638": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="The CNN Effect: Can the News Media Drive Foreign Policy?",
             title_fa="اثر سیانان: آیا رسانهٔ خبری می‌تواند سیاست خارجی را هدایت کند؟",
             authors="Piers Robinson", year=1999,
             publisher="Review of International Studies",
             doi=None,
             url="https://www.cambridge.org/core/journals/review-of-international-studies/article/cnn-effect-can-the-news-media-drive-foreign-policy/82861CF3D16F66F2BB51A8591E6470EF",
             language="en", isbn=None,
             citation="Robinson, P. (1999). The CNN effect: Can the news media drive foreign policy? Review of International Studies, 25(2), 301-309.",
             locator="25(2), 301-309",
             locator_type="PAGE",
             supports="conditional CNN effect: agenda-setting, short-term and impediment effects bounded by elite consensus and policy certainty",
             verified=True),
        dict(kind="BOOK",
             title_en="The CNN Effect: The Myth of News, Foreign Policy and Intervention",
             title_fa="اثر سیانان: افسانهٔ خبر، سیاست خارجی و مداخله",
             authors="Piers Robinson", year=2002,
             publisher="Routledge",
             doi=None,
             url="https://www.routledge.com/The-CNN-Effect-The-Myth-of-News-Foreign-Policy-and-Intervention/Robinson/p/book/9780415259057",
             language="en", isbn=None,
             citation="Robinson, P. (2002). The CNN Effect: The Myth of News, Foreign Policy and Intervention. London: Routledge.",
             locator="book",
             locator_type="BOOK",
             supports="book-length development of the conditional media-policy model",
             verified=True),
    ],
    "MC-642": [
        dict(kind="REPORT",
             title_en="Report of the Working Group on Internet Governance",
             title_fa="گزارش گروه کاری حاکمیت اینترنت",
             authors="Working Group on Internet Governance", year=2005,
             publisher="United Nations",
             doi=None,
             url="https://www.wgig.org/docs/WGIGREPORT.pdf",
             language="en", isbn=None,
             citation="Working Group on Internet Governance. (2005). Report of the Working Group on Internet Governance. Geneva: United Nations.",
             locator="working definition of Internet governance",
             locator_type="SECTION",
             supports="working definition of Internet governance and multi-stakeholder model",
             verified=True),
        dict(kind="BOOK",
             title_en="The Global War for Internet Governance",
             title_fa="جنگ جهانی حاکمیت اینترنت",
             authors="Laura DeNardis", year=2014,
             publisher="Yale University Press",
             doi="10.2307/j.ctt5vkz4n",
             url="https://www.jstor.org/stable/j.ctt5vkz4n",
             language="en", isbn=None,
             citation="DeNardis, L. (2014). The Global War for Internet Governance. New Haven: Yale University Press. https://doi.org/10.2307/j.ctt5vkz4n",
             locator="book",
             locator_type="BOOK",
             supports="infrastructure-based account of Internet governance conflicts",
             verified=True),
    ],
    "MC-442": [
        dict(kind="BOOK",
             title_en="Culture's Consequences: International Differences in Work-Related Values",
             title_fa="پیامدهای فرهنگ: تفاوت‌های بین‌المللی در ارزش‌های کاری",
             authors="Geert Hofstede", year=1980,
             publisher="Sage",
             doi=None,
             url="https://books.google.com/books/about/Culture_s_Consequences.html?id=Cayp_Um4O9gC",
             language="en", isbn=None,
             citation="Hofstede, G. (1980). Culture's Consequences: International Differences in Work-Related Values. Beverly Hills: Sage.",
             locator="chs. 1-6",
             locator_type="CHAPTER",
             supports="four national culture dimensions derived from a multinational employee survey",
             verified=True),
        dict(kind="BOOK",
             title_en="Culture's Consequences: Comparing Values, Behaviors, Institutions, and Organizations Across Nations",
             title_fa="پیامدهای فرهنگ: مقایسهٔ ارزش‌ها، رفتارها، نهادها و سازمان‌ها در میان ملت‌ها",
             authors="Geert Hofstede", year=2001,
             publisher="Sage",
             doi=None,
             url="https://books.google.com/books/about/Culture_s_Consequences.html?id=w6z18LJ_1VsC",
             language="en", isbn=None,
             citation="Hofstede, G. (2001). Culture's Consequences: Comparing Values, Behaviors, Institutions, and Organizations Across Nations (2nd ed.). Thousand Oaks: Sage.",
             locator="chs. 1-8",
             locator_type="CHAPTER",
             supports="expanded five-dimension model and methodological discussion",
             verified=True),
    ],
    "MC-645": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Consumer Acceptance and Use of Information Technology: Extending the Unified Theory of Acceptance and Use of Technology",
             title_fa="پذیرش و کاربرد فناوری اطلاعات به‌دست مصرف‌کننده: گسترش نظریهٔ یکپارچهٔ پذیرش و کاربرد فناوری",
             authors="Viswanath Venkatesh; James Y. L. Thong; Xin Xu", year=2012,
             publisher="MIS Quarterly",
             doi="10.2307/41410412",
             url="https://aisel.aisnet.org/misq/vol36/iss1/13/",
             language="en", isbn=None,
             citation="Venkatesh, V., Thong, J. Y. L., & Xu, X. (2012). Consumer acceptance and use of information technology: Extending the unified theory of acceptance and use of technology. MIS Quarterly, 36(1), 157-178. https://doi.org/10.2307/41410412",
             locator="36(1), 157-178",
             locator_type="PAGE",
             supports="hedonic motivation, price value and habit extend UTAUT for consumer contexts",
             verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="User Acceptance of Information Technology: Toward a Unified View",
             title_fa="پذیرش فناوری اطلاعات به‌دست کاربر: به‌سوی دیدگاهی یکپارچه",
             authors="Viswanath Venkatesh; Michael G. Morris; Gordon B. Davis; Fred D. Davis", year=2003,
             publisher="MIS Quarterly",
             doi=None,
             url=None,
             language="en", isbn=None,
             citation="Venkatesh, V., Morris, M. G., Davis, G. B., & Davis, F. D. (2003). User acceptance of information technology: Toward a unified view. MIS Quarterly, 27(3), 425-478.",
             locator="27(3), 425-478",
             locator_type="PAGE",
             supports="original UTAUT synthesis of eight acceptance models",
             verified=True),
    ],
    "MC-647": [
        dict(kind="BOOK",
             title_en="Remediation: Understanding New Media",
             title_fa="بازواسازی: فهم رسانه‌های نو",
             authors="Jay David Bolter; Richard Grusin", year=1999,
             publisher="MIT Press",
             doi=None,
             url="https://mitpress.mit.edu/9780262024525/remediation/",
             language="en", isbn=None,
             citation="Bolter, J. D., & Grusin, R. (1999). Remediation: Understanding New Media. Cambridge, MA: MIT Press.",
             locator="book",
             locator_type="BOOK",
             supports="double logic of immediacy and hypermediacy in remediation",
             verified=True),
        dict(kind="BOOK",
             title_en="Understanding Media: The Extensions of Man",
             title_fa="فهم رسانه: امتدادهای انسان",
             authors="Marshall McLuhan", year=1964,
             publisher="McGraw-Hill",
             doi=None,
             url=None,
             language="en", isbn=None,
             citation="McLuhan, M. (1964). Understanding Media: The Extensions of Man. New York: McGraw-Hill.",
             locator="book",
             locator_type="BOOK",
             supports="media as extensions and prior genealogies of media forms",
             verified=True),
    ],
}

ENRICH = {
    "MC-638": dict(
        needs_enrichment=False,
        level="کلان",
        constructs=("• اثر تعیین دستور کار: پوشش خبری، موضوع را در فهرست اولویت دولت و افکار عمومی می‌گذارد.\n"
                    "• اثر کوتاه‌مدت: فشار آنی پوشش زنده، واکنش سریع اما گذرا می‌سازد.\n"
                    "• اثر بازدارنده: پوشش منفی، دولت را از گزینه‌های پرهزینه بازمی‌دارد.\n"
                    "• اجماع نخبگان و ابهام سیاست: شدت اثر رسانه به همبستگی نخبگان و روشن بودن سیاست بستگی دارد."),
        core_logic="اثر سیانان رابطه‌ای خطی و همه‌جایی نیست: رسانه هنگامی بر سیاست خارجی اثر می‌گذارد که سیاست رسمی مبهم و اجماع نخبگان ضعیف باشد؛ در این حالت پوشش زنده، فشار افکار عمومی را به تصمیم‌سازان منتقل می‌کند و می‌تواند دستور کار، سرعت یا دامنهٔ مداخله را تغییر دهد.",
        detailed_analysis=("۱. بنیان و منطق نظری\nاثر سیانان بر این ایده استوار است که ارتباطات آنی و زنده، فاصلهٔ میان رنج انسانی و تصمیم سیاسی را کوتاه می‌کند. "
                           "رابینسون (۱۹۹۹) نشان داد ادعای اثر یکپارچه مبالغه‌آمیز است و سه گونهٔ اثر را از هم جدا کرد: اثر تعیین دستور کار، اثر کوتاه‌مدت و اثر بازدارنده. "
                           "در مدل شرطی او، رسانه وقتی مؤثر است که سیاست رسمی مبهم و اجماع نخبگان ضعیف باشد؛ در غیر این صورت پوشش خبری، تصمیم از پیش گرفته‌شده را مشروعیت می‌بخشد یا بی‌اثر می‌ماند. "
                           "کتاب سال ۲۰۰۲ این مدل را با مطالعات موردی مداخله‌های دههٔ ۱۹۹۰ گسترش داد و نشان داد که تصویر «افسانهٔ» رسانهٔ قدرتمند، خود به ابزار مشروعیت‌سازی سیاست تبدیل می‌شود.\n\n"
                           "۲. کاربرد و نقد\nدر محیط رسانه‌ای امروز، پوشش زنده با تصاویر کاربران و شبکه‌های اجتماعی جایگزین انحصار تلویزیون کابلی شده است. "
                           "این تغییر، سرعت و کثرت منابع فشار را افزایش داده اما همان شرط بنیادی را برجسته می‌کند: اثر رسانه بدون در نظر گرفتن ساختار تصمیم‌گیری سیاسی قابل سنجش نیست. "
                           "نقد اصلی به این نظریه، دشواری جداسازی اثر رسانه از عوامل دیپلماتیک و راهبردی، و خطر تقلیل سیاست خارجی به واکنش به افکار عمومی است."),
        related_approaches="سیاست خارجی و رسانه؛ دیپلماسی عمومی؛ نظریهٔ دستور کار؛ مداخلهٔ بشردوستانه؛ سیاست‌گذاری رسانه‌ای؛ مطالعات جنگ و صلح.",
        recommended_sources="«اثر سیانان: آیا رسانهٔ خبری می‌تواند سیاست خارجی را هدایت کند؟» (رابینسون، ۱۹۹۹)؛ «اثر سیانان: افسانهٔ خبر، سیاست خارجی و مداخله» (رابینسون، ۲۰۰۲)؛ پژوهش‌های رسانه و مداخلهٔ بشردوستانه.",
    ),
    "MC-642": dict(
        needs_enrichment=False,
        level="کلان",
        constructs=("• حاکمیت چندذی‌نفعی: تصمیم‌گیری مشترک دولت‌ها، بخش خصوصی و جامعهٔ مدنی.\n"
                    "• منابع حیاتی: نام دامنه، نشانی‌های اینترنتی و پروتکل‌های بنیادی.\n"
                    "• لایهٔ زیرساخت: استانداردها و معماری فنی که سیاست در آن نهفته است.\n"
                    "• چندپارگی اینترنت: مرزهای ملی و فنی که یکپارچگی شبکه را تهدید می‌کند."),
        core_logic="حاکمیت اینترنت نه در یک مرکز واحد، بلکه در لایه‌های فنی، اقتصادی و حقوقی پراکنده است؛ هر تصمیم دربارهٔ استاندارد، نام دامنه یا محتوا، قدرت را میان دولت‌ها، شرکت‌ها و جامعهٔ مدنی بازتوزیع می‌کند و همین پراکندگی، سیاست اینترنت را هم مقاوم و هم مبهم می‌سازد.",
        detailed_analysis=("۱. بنیان و منطق نظری\nحاکمیت اینترنت بر خلاف حاکمیت سرزمینی، از یک مرکز فرماندهی پیروی نمی‌کند. "
                           "گروه کاری سازمان ملل در سال ۲۰۰۵ تعریفی کاری ارائه داد که تدوین و کاربرد اصول، هنجارها و رویه‌های مشترک را در دست دولت‌ها، بخش خصوصی و جامعهٔ مدنی می‌دید. "
                           "دناردیس (۲۰۱۴) با رویکردی زیرساختی نشان داد که قدرت واقعی در لایه‌های فنی نهفته است: تخصیص نام دامنه، استانداردهای پروتکل و مدیریت نشانی‌های اینترنتی، تصمیم‌هایی فنی‌اند که پیامدهای سیاسی و اقتصادی گسترده دارند. "
                           "به این معنا، حاکمیت اینترنت را نباید فقط در معاهدات و نهادها جست؛ باید در معماری فنی و مالکیت زیرساخت نیز کاوید.\n\n"
                           "۲. مناقشه و کاربرد\nپس از افشاگری‌های نظارتی و رشد پلتفرم‌های جهانی، پرسش از مرز میان حاکمیت ملی و اینترنت جهانی شدت گرفت. "
                           "مدل چندذی‌نفعی به‌عنوان بدیل حاکمیت دولتی مطرح شد، اما منتقدان می‌گویند این مدل قدرت نامتوازن بازیگران مسلط را پنهان می‌کند. "
                           "در پژوهش رسانه، چارچوب حاکمیت اینترنت ابزار تحلیل سیاست پلتفرم، حریم خصوصی، آزادی بیان و شکاف دیجیتال است و نشان می‌دهد که هر تصمیم فنی، تصمیمی دربارهٔ توزیع صدا و قدرت است."),
        related_approaches="اقتصاد سیاسی ارتباطات؛ سیاست اینترنت؛ حاکمیت پلتفرم؛ حقوق فناوری؛ نظریهٔ شبکهٔ کنشگر؛ سیاست حریم خصوصی.",
        recommended_sources="«گزارش گروه کاری حاکمیت اینترنت» (۲۰۰۵)؛ «جنگ جهانی حاکمیت اینترنت» (دناردیس، ۲۰۱۴)؛ اسناد اجلاس جهانی جامعهٔ اطلاعات.",
    ),
    "MC-442": dict(
        needs_enrichment=False,
        key_concepts=["فاصلهٔ قدرت", "فردگرایی و جمع‌گرایی", "مردانگی و زنانگی",
                      "اجتناب از عدم قطعیت", "جهت‌گیری بلندمدت", "خویشتن‌داری و لذت‌گرایی"],
        principles=["هر بعد یک پیوستار است، نه دوگانهٔ مطلق.", "فاصلهٔ قدرت، الگوی ارتباط با مرجع قدرت را شکل می‌دهد.",
                    "فردگرایی و جمع‌گرایی بر تعریف خود و گروه اثر می‌گذارد.", "مردانگی و زنانگی، ارزش‌های رقابت و مراقبت را از هم جدا می‌کند.",
                    "اجتناب از عدم قطعیت، تحمل ابهام و قاعده‌پذیری را می‌سنجد.", "جهت‌گیری بلندمدت، وزن آینده در تصمیم امروز را نشان می‌دهد.",
                    "امتیاز ملی را نباید به فرد تعمیم داد؛ خطای بوم‌شناختی ممنوع است.", "ابعاد فرهنگی ابزار مقایسه‌اند، نه برچسب هویتی برای افراد."],
        constructs=("• فاصلهٔ قدرت: میزان پذیرش توزیع نابرابر قدرت در نهادها.\n"
                    "• فردگرایی و جمع‌گرایی: اولویت منافع فرد یا گروه.\n"
                    "• مردانگی و زنانگی: تأکید بر رقابت و موفقیت یا کیفیت زندگی و مراقبت.\n"
                    "• اجتناب از عدم قطعیت: تحمل ابهام و قاعده‌گریزی.\n"
                    "• جهت‌گیری بلندمدت: تأکید بر آینده‌نگری و پایداری.\n"
                    "• خویشتن‌داری و لذت‌گرایی: مهار یا آزادسازی ارضای نیازها."),
        related_approaches="ارتباطات بین‌فرهنگی؛ مدیریت مقایسه‌ای؛ روان‌شناسی فرهنگی؛ بازاریابی بین‌المللی؛ ارزش‌های کاری.",
        recommended_sources="«پیامدهای فرهنگ» (هافستد، ۱۹۸۰)؛ «پیامدهای فرهنگ، ویرایش دوم» (هافستد، ۲۰۰۱)؛ پژوهش‌های ارتباطات بین‌فرهنگی.",
    ),
    "MC-645": dict(
        needs_enrichment=False,
        title_fa="نظریهٔ یکپارچهٔ پذیرش و کاربرد فناوری (نسخهٔ دوم)",
        constructs=("• انتظار عملکرد: باور به سودمندی فناوری در بهبود کار.\n"
                    "• انتظار تلاش: سهولت استفاده.\n"
                    "• تأثیر اجتماعی: فشار افراد مهم.\n"
                    "• شرایط تسهیل‌کننده: زیرساخت و پشتیبانی.\n"
                    "• انگیزهٔ لذت‌جویانه: لذت و سرگرمی استفاده.\n"
                    "• ارزش قیمتی: توازن هزینه و منفعت.\n"
                    "• عادت: خودکارشدن استفاده در گذر زمان."),
        core_logic="پذیرش فناوری به‌دست مصرف‌کننده، برخلاف کارمند سازمانی، تنها با سودمندی و سهولت توضیح داده نمی‌شود؛ لذت استفاده، ارزش قیمتی و عادت سه سازه‌ای هستند که قصد و رفتار استفاده را در بافت مصرف روزمره شکل می‌دهند.",
        detailed_analysis=("۱. بنیان و منطق نظری\nنسخهٔ دوم نظریهٔ یکپارچهٔ پذیرش و کاربرد فناوری، مدل سال ۲۰۰۳ را برای بافت مصرف‌کننده بازطراحی کرد. "
                           "ونکاتش، تونگ و شو (۲۰۱۲) چهار سازهٔ پایهٔ انتظار عملکرد، انتظار تلاش، تأثیر اجتماعی و شرایط تسهیل‌کننده را نگه داشتند و سه سازهٔ انگیزهٔ لذت‌جویانه، ارزش قیمتی و عادت را افزودند. "
                           "در این مدل، قصد رفتاری پیش‌بین استفاده است و سن، جنسیت و تجربه، رابطهٔ سازه‌ها را تعدیل می‌کنند. "
                           "نکتهٔ کلیدی آن است که در فناوری‌های رسانه‌ای و سرگرمی، لذت و هزینهٔ ادراک‌شده وزن بیشتری از سودمندی ابزاری می‌یابند.\n\n"
                           "۲. کاربرد و نقد\nاین مدل در پژوهش پذیرش اپلیکیشن‌های خبری، پیام‌رسان‌ها و سرویس‌های سرگرمی پرکاربرد است. "
                           "نقدها بر داده‌های مقطعی، اتکا به خودگزارشی و نادیده‌گرفتن عوامل ساختاری مانند دسترسی و سواد دیجیتال تمرکز دارند. "
                           "همچنین باید به خطر تفسیر علّی از همبستگی‌های مدل و تفاوت بافت فرهنگی توجه کرد؛ با این حال، نسخهٔ دوم همچنان یکی از منسجم‌ترین چارچوب‌ها برای توضیح پذیرش فناوری مصرفی است."),
        related_approaches="مدل پذیرش فناوری؛ نظریهٔ رفتار برنامه‌ریزی‌شده؛ انتشار نوآوری؛ تجربهٔ کاربری؛ شکاف دیجیتال.",
        recommended_sources="«پذیرش و کاربرد فناوری اطلاعات به‌دست مصرف‌کننده» (ونکاتش، تونگ و شو، ۲۰۱۲)؛ «پذیرش فناوری اطلاعات به‌دست کاربر» (ونکاتش و همکاران، ۲۰۰۳)؛ «سودمندی و سهولت ادراک‌شده در پذیرش فناوری» (دیویس، ۱۹۸۹).",
    ),
    "MC-647": dict(
        needs_enrichment=False,
        constructs=("• بازواسازی: بازنمایی و اصلاح رسانهٔ پیشین در رسانهٔ نو.\n"
                    "• بی‌واسطگی: پنهان‌کردن واسطه برای تجربهٔ مستقیم.\n"
                    "• فراواسطگی: نمایش آشکار کثرت واسطه‌ها.\n"
                    "• نسب‌نامهٔ رسانه: زنجیرهٔ وام‌گیری میان رسانه‌ها."),
        core_logic="رسانه‌های نو نه از خلأ، بلکه با بازسازی رسانه‌های پیشین پدید می‌آیند؛ هم‌زمان می‌کوشند واسطه را پنهان کنند (بی‌واسطگی) و آن را به رخ بکشند (فراواسطگی)، و همین تنش، موتور تحول رسانه است.",
        detailed_analysis=("۱. بنیان و منطق نظری\nبولتر و گروزین (۱۹۹۹) بازواسازی را فرایندی می‌دانند که در آن هر رسانهٔ نو، رسانه‌های پیشین را بازنمایی، بازسازی و اصلاح می‌کند. "
                           "این فرایند دو منطق هم‌زمان دارد: بی‌واسطگی، که می‌خواهد واسطه را نامرئی کند تا تجربهٔ مستقیم و بی‌مانند بسازد، و فراواسطگی، که کثرت واسطه‌ها را آشکار و جشن می‌گیرد. "
                           "وبگاه خبری، بازی دیجیتال و واقعیت مجازی هر یک به شیوهٔ خود این دو منطق را ترکیب می‌کنند. "
                           "ریشهٔ بحث به ایدهٔ مک‌لوهان (۱۹۶۴) دربارهٔ رسانه به‌عنوان امتداد انسان بازمی‌گردد، اما بولتر و گروزین به‌جای گسست، بر تداوم و وام‌گیری تأکید می‌کنند.\n\n"
                           "۲. کاربرد و نقد\nاین نظریه ابزار تحلیل طراحی رسانه‌های تازه، اقتباس میان پلتفرم‌ها و حافظهٔ رسانه‌ای است. "
                           "نقد اصلی، دشواری مرزبندی بازواسازی از سایر اشکال وام‌گیری فرهنگی، و ادعای جهان‌شمولی تاریخی است که شواهد تجربی کافی ندارد. "
                           "با این حال، تأکید آن بر اینکه هیچ رسانه‌ای بدون ارجاع به گذشته شکل نمی‌گیرد، همچنان یکی از بنیادی‌ترین بینش‌های مطالعات رسانه است."),
        related_approaches="تاریخ رسانه؛ نظریهٔ اقتباس؛ بینامتنیت؛ واقعیت مجازی؛ مطالعات بصری.",
        recommended_sources="«بازواسازی: فهم رسانه‌های نو» (بولتر و گروزین، ۱۹۹۹)؛ «فهم رسانه: امتدادهای انسان» (مک‌لوهان، ۱۹۶۴)؛ «زبان رسانه‌های نو» (مانوویچ، ۲۰۰۱).",
    ),
}

NAME_FIX = {}

YEAR_FIX = {
    "MC-638": "year=1999 (Robinson 1999); Robinson 2002 verified; removed contaminated constructs and generic media-power recommendations",
    "MC-642": "year=2005 (WGIG 2005); DeNardis 2014 verified (DOI 10.2307/j.ctt5vkz4n); removed contaminated constructs and generic recommendations",
    "MC-442": "year=1980 (Hofstede 1980); Hofstede 2001 verified; removed Latin glosses in key_concepts, contaminated constructs, irrelevant recommendations",
    "MC-645": "year=2012 (Venkatesh, Thong & Xu 2012); UTAUT 2003 verified; removed platform-template constructs/analysis and garbled recommendations",
    "MC-647": "year=1999 (Bolter & Grusin 1999); McLuhan 1964 verified; removed platform-template constructs/analysis and irrelevant recommendations",
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
                                       "verified": n_verified, "batch": 202}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH202 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
