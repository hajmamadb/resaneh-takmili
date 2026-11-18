# -*- coding: utf-8 -*-
"""Batch 207: MC-121, MC-131, MC-133, MC-135, MC-143 (MODEL)."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch207-20261117"
NOW = "2026-11-17 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch207.json"

S = {
    "MC-121": [
        dict(kind="BOOK",
             title_en="Managing Public Relations",
             title_fa="مدیریت روابط عمومی",
             authors="James E. Grunig; Todd Hunt", year=1984,
             publisher="Holt, Rinehart and Winston",
             doi=None,
             url="https://archive.org/details/managingpublicre0000unse",
             language="en", isbn=None,
             citation="Grunig, J. E., & Hunt, T. (1984). Managing Public Relations. New York: Holt, Rinehart and Winston.",
             locator="four models chapter",
             locator_type="CHAPTER",
             supports="classification of press agentry, public information, two-way asymmetrical and two-way symmetrical models",
             verified=True),
        dict(kind="BOOK",
             title_en="Excellence in Public Relations and Communication Management",
             title_fa="تعالی در روابط عمومی و مدیریت ارتباطات",
             authors="James E. Grunig (ed.)", year=1992,
             publisher="Lawrence Erlbaum Associates",
             doi="10.4324/9780203812303",
             url="https://www.routledge.com/Excellence-in-Public-Relations-and-Communication-Management/Grunig/p/book/9780805802276",
             language="en", isbn=None,
             citation="Grunig, J. E. (Ed.). (1992). Excellence in Public Relations and Communication Management. Hillsdale, NJ: Lawrence Erlbaum Associates.",
             locator="book",
             locator_type="BOOK",
             supports="normative argument that two-way symmetrical practice characterises excellent public relations",
             verified=True),
    ],
    "MC-131": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Persuasion Knowledge Model: How People Cope with Persuasion Attempts",
             title_fa="مدل دانش اقناع: چگونه افراد با کوشش‌های اقناعی مقابله می‌کنند",
             authors="Marian Friestad; Peter Wright", year=1994,
             publisher="Journal of Consumer Research",
             doi=None,
             url="https://academic.oup.com/jcr/article-abstract/21/1/1/1853712",
             language="en", isbn=None,
             citation="Friestad, M., & Wright, P. (1994). The persuasion knowledge model: How people cope with persuasion attempts. Journal of Consumer Research, 21(1), 1-31.",
             locator="21(1), 1-31",
             locator_type="PAGE",
             supports="topic, persuasion and agent knowledge guiding coping with persuasion attempts",
             verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Persuasion Knowledge: Lay People's and Researchers' Beliefs about the Psychology of Advertising",
             title_fa="دانش اقناع: باورهای مردم عادی و پژوهشگران دربارهٔ روان‌شناسی تبلیغ",
             authors="Marian Friestad; Peter Wright", year=1995,
             publisher="Journal of Consumer Research",
             doi=None,
             url="https://academic.oup.com/jcr/article-abstract/22/1/62/1808120",
             language="en", isbn=None,
             citation="Friestad, M., & Wright, P. (1995). Persuasion knowledge: Lay people's and researchers' beliefs about the psychology of advertising. Journal of Consumer Research, 22(1), 62-74.",
             locator="22(1), 62-74",
             locator_type="PAGE",
             supports="everyday persuasion knowledge as culturally shared folk knowledge",
             verified=True),
    ],
    "MC-133": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Historical Origins of the Health Belief Model",
             title_fa="خاستگاه‌های تاریخی مدل باور سلامت",
             authors="Irwin M. Rosenstock", year=1974,
             publisher="Health Education Monographs",
             doi="10.1177/109019817400200403",
             url="https://journals.sagepub.com/doi/10.1177/109019817400200403",
             language="en", isbn=None,
             citation="Rosenstock, I. M. (1974). Historical origins of the health belief model. Health Education Monographs, 2(4), 328-335. https://doi.org/10.1177/109019817400200403",
             locator="2(4), 328-335",
             locator_type="PAGE",
             supports="historical origins of the model in U.S. Public Health Service screening research",
             verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Social Learning Theory and the Health Belief Model",
             title_fa="نظریهٔ یادگیری اجتماعی و مدل باور سلامت",
             authors="Irwin M. Rosenstock; Victor J. Strecher; Marshall H. Becker", year=1988,
             publisher="Health Education Quarterly",
             doi="10.1177/109019818801500203",
             url="https://journals.sagepub.com/doi/10.1177/109019818801500203",
             language="en", isbn=None,
             citation="Rosenstock, I. M., Strecher, V. J., & Becker, M. H. (1988). Social learning theory and the health belief model. Health Education Quarterly, 15(2), 175-183. https://doi.org/10.1177/109019818801500203",
             locator="15(2), 175-183",
             locator_type="PAGE",
             supports="addition of self-efficacy and integration with social learning theory",
             verified=True),
    ],
    "MC-135": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="A Model for Predictive Measurements of Advertising Effectiveness",
             title_fa="مدلی برای سنجش پیش‌بین اثربخشی تبلیغ",
             authors="Robert J. Lavidge; Gary A. Steiner", year=1961,
             publisher="Journal of Marketing",
             doi="10.1177/002224296102500611",
             url="https://journals.sagepub.com/doi/abs/10.1177/002224296102500611",
             language="en", isbn=None,
             citation="Lavidge, R. J., & Steiner, G. A. (1961). A model for predictive measurements of advertising effectiveness. Journal of Marketing, 25(6), 59-62. https://doi.org/10.1177/002224296102500611",
             locator="25(6), 59-62",
             locator_type="PAGE",
             supports="six-stage hierarchy from awareness to purchase and stage-wise measurement",
             verified=True),
        dict(kind="BOOK",
             title_en="Defining Advertising Goals for Measured Advertising Results",
             title_fa="تعریف اهداف تبلیغ برای سنجش نتایج تبلیغ",
             authors="Russell H. Colley", year=1961,
             publisher="Association of National Advertisers",
             doi=None,
             url="https://archive.org/details/dagmardefiningad0000dutk",
             language="en", isbn=None,
             citation="Colley, R. H. (1961). Defining Advertising Goals for Measured Advertising Results. New York: Association of National Advertisers.",
             locator="book",
             locator_type="BOOK",
             supports="DAGMAR approach linking advertising objectives to measurable communication effects",
             verified=True),
    ],
    "MC-143": [
        dict(kind="BOOK",
             title_en="The Presentation of Self in Everyday Life",
             title_fa="ارائهٔ خود در زندگی روزمره",
             authors="Erving Goffman", year=1959,
             publisher="Doubleday",
             doi=None,
             url=None,
             language="en", isbn=None,
             citation="Goffman, E. (1959). The Presentation of Self in Everyday Life. Garden City, NY: Doubleday.",
             locator="book",
             locator_type="BOOK",
             supports="dramaturgical model of front stage, back stage and impression management",
             verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="On Face-Work: An Analysis of Ritual Elements in Social Interaction",
             title_fa="حفظ آبرو: تحلیلی از عناصر آیینی در تعامل اجتماعی",
             authors="Erving Goffman", year=1955,
             publisher="Psychiatry",
             doi="10.1080/00332747.1955.11023008",
             url="https://www.tandfonline.com/doi/abs/10.1080/00332747.1955.11023008",
             language="en", isbn=None,
             citation="Goffman, E. (1955). On face-work: An analysis of ritual elements in social interaction. Psychiatry, 18(3), 213-231. https://doi.org/10.1080/00332747.1955.11023008",
             locator="18(3), 213-231",
             locator_type="PAGE",
             supports="face-work and ritual repair as antecedents of impression management",
             verified=True),
    ],
}

ENRICH = {
    "MC-121": dict(
        needs_enrichment=False,
        related_approaches="نظریهٔ تعالی روابط عمومی؛ ارتباطات سازمانی؛ ارتباطات راهبردی؛ مدیریت بحران؛ نظریهٔ ذی‌نفعان.",
        core_logic=("گرونیگ و هانت چهار الگوی روابط عمومی را بر دو محور طبقه‌بندی کردند: جهت ارتباط (یک‌طرفه یا دوطرفه) و تقارن (متقارن یا نامتقارن). "
                    "انتشاراتی، اطلاع‌رسانی عمومی، دوطرفهٔ نامتقارن و دوطرفهٔ متقارن، چهار خانهٔ این جدول‌اند. "
                    "الگوهای نخست بر انتقال یک‌سویهٔ پیام تکیه دارند و الگوهای دوطرفه بر تبادل؛ تنها الگوی دوطرفهٔ متقارن، تغییر سازمان و جمهور را هم‌زمان ممکن می‌داند و به‌عنوان الگوی هنجاری مطلوب معرفی شد."),
        recommended_sources="«مدیریت روابط عمومی» (گرونیگ و هانت، ۱۹۸۴)؛ «تعالی در روابط عمومی و مدیریت ارتباطات» (گرونیگ، ۱۹۹۲)؛ «راهنمای مدیران برای تعالی در روابط عمومی و مدیریت ارتباطات» (دوزیر، گرونیگ و گرونیگ، ۱۹۹۵).",
        detailed_analysis=("۱. بنیان و منطق نظری\nمدل‌های چهارگانهٔ روابط عمومی، چارچوبی کلاسیک برای درک ماهیت و کارکرد روابط عمومی در سازمان‌ها است. "
                           "جیمز گرونیگ و تاد هانت در سال ۱۹۸۴، بر اساس دو محور «جهت جریان ارتباط» (یک‌طرفه یا دوطرفه) و «تقارن در تأثیرگذاری» (متقارن یا نامتقارن)، چهار مدل را تعریف کردند. "
                           "این طبقه‌بندی نشان می‌دهد سازمان‌ها چگونه با مخاطبان خود تعامل می‌کنند و چه اهدافی را دنبال می‌کنند.\n\n"
                           "۲. ساختارهای مفهومی\n• مدل انتشاراتی: تمرکز بر جلب توجه و تبلیغ، بدون دغدغهٔ صحت اطلاعات؛ ارتباط یک‌طرفه و نامتقارن.\n"
                           "• مدل اطلاع‌رسانی عمومی: انتشار اطلاعات دقیق و یک‌طرفه؛ هدف آگاه‌سازی است، نه تغییر نگرش.\n"
                           "• مدل دوطرفهٔ نامتقارن: پژوهش دربارهٔ مخاطب برای طراحی پیام اقناعی؛ ارتباط دوطرفه، اما هدف تغییر نگرش مخاطب به سود سازمان است.\n"
                           "• مدل دوطرفهٔ متقارن: تعامل متقابل و عادلانه؛ هدف درک متقابل و حل تعارض از راه گفت‌وگو است.\n\n"
                           "۳. نمونه‌های تحلیلی\nدر بحران‌های سازمانی، بیانیهٔ یک‌سویه اغلب ناکافی است. سازمان‌هایی که با شنیدن صدای ذی‌نفعان و تعدیل مواضع خود عمل می‌کنند، اعتماد را بازسازی می‌کنند؛ در مقابل، مدل‌های یک‌طرفه در کوتاه‌مدت کم‌هزینه‌ترند، اما در بلندمدت به بی‌اعتمادی می‌انجامند.\n\n"
                           "۴. نقدها و چالش‌ها\nهنجاری بودن مدل متقارن، سنجش دشوار «تقارن» در عمل، کم‌توجهی به قدرت، فرهنگ سازمانی و محیط سیاسی-اقتصادی، و شواهد تجربی ناهمگون دربارهٔ برتری عملکردی الگوی متقارن، مهم‌ترین نقدهای وارد بر این طبقه‌بندی‌اند.\n\n"
                           "۵. سیر تاریخی\nمدل‌ها در دههٔ ۱۹۸۰ مطرح شدند و پایهٔ نظریهٔ تعالی شدند. پژوهش‌های بعدی، اجرای الگوی متقارن را به عواملی چون حمایت مدیر ارشد، فرهنگ مشارکتی و ساختار سازمانی گره زدند."),
    ),
    "MC-131": dict(
        needs_enrichment=False,
        title_fa="مدل دانش اقناع",
        related_approaches="سواد تبلیغاتی؛ روان‌شناسی مصرف‌کننده؛ نظریهٔ اقناع؛ تبلیغات بومی؛ نظریهٔ واکنش‌پذیری.",
        core_logic=("افراد در طول زندگی، دانشی دربارهٔ شیوه‌های اقناع می‌سازند: می‌آموزند فرستنده چه اهدافی دارد، از چه فنونی استفاده می‌کند و چه ویژگی‌هایی دارد. "
                    "وقتی نشانه‌های اقناع در پیام تشخیص داده شود، این دانش فعال می‌شود و راهبردهای مقابله — تردید، بررسی انتقادی، کنارگذاری پیام یا واکنش دفاعی — به‌کار می‌رود. "
                    "نتیجهٔ معمول، کاهش اعتماد به فرستنده و کاهش پذیرش پیام است."),
        recommended_sources="«مدل دانش اقناع» (فریستد و رایت، ۱۹۹۴)؛ «دانش اقناع: باورهای مردم عادی و پژوهشگران» (فریستد و رایت، ۱۹۹۵)؛ پژوهش‌های سواد تبلیغاتی و تبلیغات بومی.",
        detailed_analysis=("۱. بنیان و منطق نظری\nمدل دانش اقناع را ماریان فریستد و پیتر رایت در سال ۱۹۹۴ در مجلهٔ پژوهش مصرف صورت‌بندی کردند. "
                           "فرض بنیادین این است که مخاطب، گیرندهٔ منفعل نیست؛ او در طول تجربهٔ مصرف و رسانه، سه نوع دانش می‌سازد: دانش موضوعی (دربارهٔ محصول یا موضوع پیام)، دانش اقناع (دربارهٔ فنون و انگیزه‌های اقناع) و دانش عامل (دربارهٔ فرستنده). "
                           "این سه دانش در کنار هم، تفسیر مخاطب از کوشش اقناعی و پاسخ او را شکل می‌دهند.\n\n"
                           "۲. ساختارهای مفهومی\n• دانش موضوعی: اطلاعات فرد دربارهٔ محصول، موضوع یا گزینه‌های تصمیم.\n"
                           "• دانش اقناع: شناخت شیوه‌هایی مانند تبلیغ، تعریف از محصول، اثبات اجتماعی و چارچوب‌بندی.\n"
                           "• دانش عامل: باورها دربارهٔ فرستنده، انگیزه‌ها و اعتبار او.\n"
                           "• راهبرد مقابله: تردید، بررسی انتقادی، کنارگذاری پیام یا واکنش دفاعی.\n\n"
                           "۳. نمونه‌های تحلیلی\nدر بازاریابی تأثیرگذار، معرفی محصول بدون برچسب تبلیغاتی از سوی مخاطبان آگاه به‌عنوان فریب تفسیر می‌شود و اعتماد را فرومی‌ریزد؛ افشای شفاف همکاری، جذابیت لحظه‌ای را کم می‌کند اما اعتماد بلندمدت را حفظ می‌کند. "
                           "در سیاست نیز زبان احساسی و تکراری نامزدها، برای ناظران آگاه، نشانهٔ فن اقناعی و دلیل کاهش اعتبار پیام است.\n\n"
                           "۴. نقدها و چالش‌ها\nآستانهٔ تشخیص اقناع روشن نیست؛ تفاوت‌های فردی و فرهنگی کم‌بررسی مانده است؛ مدل عمدتاً شناختی است و نقش هیجان را کمتر توضیح می‌دهد؛ و سنجش دانش اقناع در پژوهش میدانی دشوار و وابسته به خودگزارشی است.\n\n"
                           "۵. سیر تاریخی\nریشهٔ مدل در پژوهش اقناع و رفتار مصرف‌کنندهٔ دههٔ ۱۹۸۰ است. مقالهٔ ۱۹۹۴ چارچوب را تثبیت کرد و مقالهٔ ۱۹۹۵ نشان داد این دانش، شکلی فرهنگی و مشترک دارد. "
                           "پژوهش‌های بعدی، مدل را به سواد تبلیغاتی کودکان، تبلیغات بومی، بازاریابی تأثیرگذار و الگوهای تاریک رابط کاربری گستردند.\n\n"
                           "۶. جایگاه در بحث روز\nدر اقتصاد توجه و محیط الگوریتمی، تشخیص مرز محتوا و تبلیغ دشوارتر شده است؛ مدل دانش اقناع ابزار مفهومی مهمی برای فهم مقاومت مخاطب در برابر تبلیغ پنهان و پروپاگاندای دیجیتال است."),
    ),
    "MC-133": dict(
        needs_enrichment=False,
        recommended_sources="«خاستگاه‌های تاریخی مدل باور سلامت» (روزنستاک، ۱۹۷۴)؛ «نظریهٔ یادگیری اجتماعی و مدل باور سلامت» (روزنستاک، استرچر و بکر، ۱۹۸۸)؛ «مدل باور سلامت: یک دهه بعد» (جانز و بکر، ۱۹۸۴).",
        detailed_analysis=("۱. بنیان و منطق نظری\nمدل باور سلامت یکی از نخستین مدل‌های روان‌شناختی برای پیش‌بینی و توضیح رفتار سلامت است. "
                           "ریشهٔ آن به پژوهش‌های خدمات بهداشت عمومی آمریکا در دههٔ ۱۹۵۰ بازمی‌گردد که می‌کوشیدند توضیح دهند چرا افراد از برنامه‌های غربالگری رایگان سل استقبال نمی‌کنند. "
                           "روزنستاک (۱۹۷۴) این یافته‌ها را در یک چارچوب صورت‌بندی کرد: افراد زمانی اقدام می‌کنند که خود را در معرض خطر بدانند (حساسیت درک‌شده)، خطر را جدی بگیرند (شدت درک‌شده)، اقدام را سودمند بدانند (منافع درک‌شده)، موانع را قابل‌تحمل ببینند (موانع درک‌شده) و محرکی برای عمل داشته باشند (نشانه‌های عمل).\n\n"
                           "۲. ساختارهای مفهومی\n• حساسیت درک‌شده: ادراک احتمال ابتلا.\n"
                           "• شدت درک‌شده: ادراک پیامدهای جسمی، اجتماعی و روانی بیماری.\n"
                           "• منافع و موانع درک‌شده: سنجش سود و هزینهٔ اقدام.\n"
                           "• نشانه‌های عمل: محرک‌های درونی یا بیرونی مانند توصیهٔ پزشک و پیام رسانه‌ای.\n"
                           "• خودکارآمدی: باور به توان انجام رفتار که روزنستاک، استرچر و بکر (۱۹۸۸) با تکیه بر نظریهٔ یادگیری اجتماعی افزودند.\n\n"
                           "۳. نمونه‌های تحلیلی\nدر کمپین واکسیناسیون، اگر حساسیت درک‌شده پایین باشد، حتی شدت بالا به اقدام نمی‌انجامد؛ از این رو پیام رسانه‌ای باید هم‌زمان حساسیت را بالا ببرد، موانع را کم کند و خودکارآمدی را تقویت کند. "
                           "در غربالگری نیز پیام مؤثر، موانع عملی مانند هزینه و دسترسی را هدف می‌گیرد، نه فقط ترس را.\n\n"
                           "۴. نقدها و چالش‌ها\nفردگرایی و غفلت از عوامل ساختاری، توان پیش‌بینی محدود در رفتارهای عادت‌شده، ناسازگاری در عملیاتی‌سازی سازه‌ها، و کم‌توجهی به عاطفه، هنجار اجتماعی و محیط از نقدهای اصلی‌اند.\n\n"
                           "۵. سیر تاریخی\nمدل در دههٔ ۱۹۵۰ در پژوهش غربالگری شکل گرفت، در ۱۹۷۴ صورت‌بندی شد، در ۱۹۸۸ با خودکارآمدی و نظریهٔ یادگیری اجتماعی گسترش یافت و در دهه‌های بعد با نقدهای ساختاری و بسط‌های یکپارچه روبه‌رو شد.\n\n"
                           "۶. جایگاه در بحث روز\nمدل باور سلامت همچنان چارچوب پرکاربردی در ارتباطات سلامت است؛ در محیط شبکه‌های اجتماعی، پژوهش‌ها بر نشانه‌های عمل دیجیتال، خودکارآمدی و مقابله با اطلاعات نادرست سلامت تمرکز کرده‌اند."),
    ),
    "MC-135": dict(
        needs_enrichment=False,
        recommended_sources="«مدلی برای سنجش پیش‌بین اثربخشی تبلیغ» (لاویدج و اشتاینر، ۱۹۶۱)؛ «تعریف اهداف تبلیغ برای سنجش نتایج تبلیغ» (کالی، ۱۹۶۱)؛ پژوهش‌های قیف بازاریابی و اثربخشی تبلیغات دیجیتال.",
        detailed_analysis=("۱. بنیان و منطق نظری\nمدل سلسله‌مراتب اثرات را رابرت لاویدج و گری اشتاینر در سال ۱۹۶۱ در مجلهٔ بازاریابی معرفی کردند. "
                           "فرض اصلی این است که تبلیغ اثر خود را تدریجی و مرحله‌ای اعمال می‌کند: آگاهی، شناخت، دوست‌داشتن، ترجیح، اعتقاد و خرید. "
                           "سه مرحلهٔ نخست شناختی، دو مرحلهٔ میانی عاطفی و مرحلهٔ آخر رفتاری‌اند؛ هر مرحله پیش‌نیاز مرحلهٔ بعد است و سنجش جداگانهٔ هر مرحله، تصویری دقیق‌تر از اثربخشی می‌دهد.\n\n"
                           "۲. ساختارهای مفهومی\n• آگاهی: شناسایی نام برند یا محصول.\n"
                           "• شناخت و دوست‌داشتن: درک ویژگی‌ها و شکل‌گیری نگرش مثبت.\n"
                           "• ترجیح و اعتقاد: برگزیدن برند در برابر رقبا و قصد خرید.\n"
                           "• خرید: اقدام رفتاری نهایی.\n\n"
                           "۳. نمونه‌های تحلیلی\nدر کمپین محصول تازه، پیام‌های آغازین آگاهی می‌سازند، پیام‌های میانی نگرش و ترجیح را شکل می‌دهند و پیام‌های پایانی قصد و خرید را تقویت می‌کنند. "
                           "رویکرد داگمار کالی (۱۹۶۱) همین منطق را به تعریف اهداف تبلیغاتی قابل‌اندازه‌گیری گره زد و در صنعت رواج داد.\n\n"
                           "۴. نقدها و چالش‌ها\nخطی‌بودن مسیر، نامناسب‌بودن برای خریدهای کم‌درگیری و تکانشی، سنجش دشوار مرز مراحل، نادیده‌گرفتن عوامل بیرونی مانند قیمت و دسترسی، و شواهد ناهمگون دربارهٔ ترتیب دقیق مراحل، مهم‌ترین نقدهاست.\n\n"
                           "۵. سیر تاریخی\nمدل آیدا با مراحل توجه، علاقه، تمایل و عمل پیشینهٔ تاریخی این منطق است. لاویدج و اشتاینر در ۱۹۶۱ آن را با افزودن مراحل شناختی و عاطفی و تأکید بر سنجش مرحله‌ای تکمیل کردند و کالی در همان سال چارچوب داگمار را برای تعیین اهداف اندازه‌پذیر عرضه کرد. "
                           "از دههٔ ۲۰۰۰، قیف دیجیتال و مسیرهای غیرخطی، این سلسله‌مراتب را بازخوانی کرده‌اند.\n\n"
                           "۶. جایگاه در بحث روز\nمدل سلسله‌مراتب همچنان ستون فقرات برنامه‌ریزی کمپین و قیف فروش است؛ در بازاریابی دیجیتال، شاخص‌های هر مرحله به داده‌های لحظه‌ای و آزمایش‌های مقایسه‌ای گره خورده‌اند."),
    ),
    "MC-143": dict(
        needs_enrichment=False,
        related_approaches="کنش متقابل نمادین؛ خودارائه‌گری؛ برندسازی شخصی؛ ارتباطات سازمانی؛ تحلیل نمایشی رسانه.",
        core_logic=("گافمن تعامل اجتماعی را مانند نمایش تحلیل می‌کند: افراد در «صحنهٔ جلو» با ظاهر، رفتار و ابزار نقش، تصویر مطلوبی از خود می‌سازند و در «پشت صحنه» آماده می‌شوند و از نقش خارج می‌شوند. "
                    "اجراکنندگان به‌صورت تیمی هماهنگ می‌کنند تا برداشت تماشاگران را مدیریت کنند. "
                    "افشای پشت صحنه یا ناهماهنگی دو صحنه، اعتبار اجرا و فرد را فرومی‌ریزد."),
        recommended_sources="«ارائهٔ خود در زندگی روزمره» (گافمن، ۱۹۵۹)؛ «حفظ آبرو: تحلیل عناصر آیینی در تعامل اجتماعی» (گافمن، ۱۹۵۵)؛ «ارائهٔ خود در جهان آنلاین: گافمن و مطالعهٔ هویت‌های آنلاین» (بولینگهام و واسکونسلوس، ۲۰۱۳).",
        detailed_analysis=("۱. بنیان و منطق نظری\nمدیریت برداشت، چارچوبی در جامعه‌شناسی تعامل است که اروینگ گافمن در کتاب ارائهٔ خود در زندگی روزمره (۱۹۵۹) صورت‌بندی کرد. "
                           "او تعامل را مانند نمایش تحلیل می‌کند: صحنهٔ جلو جایی است که فرد با ظاهر، لباس، لحن و ابزار نقش، تعریفی از موقعیت به تماشاگران عرضه می‌کند؛ پشت صحنه جایی است که آماده‌سازی و استراحت رخ می‌دهد و اجرا کنار گذاشته می‌شود. "
                           "اجرا معمولاً تیمی است و هماهنگی اجراکنندگان، شرط حفظ تعریف مشترک موقعیت است.\n\n"
                           "۲. ساختارهای مفهومی\n• صحنهٔ جلو و پشت صحنه: دو قلمرو نمایش و آماده‌سازی.\n"
                           "• نقش و اجرا: مجموعهٔ انتظارها و رفتارهای متناسب با موقعیت.\n"
                           "• هماهنگی تیمی: مدیریت مشترک برداشت تماشاگران.\n"
                           "• حفظ آبرو: آیین‌های پرهیز و ترمیم که تصویر خود و دیگری را حفظ می‌کنند (گافمن، ۱۹۵۵).\n"
                           "• افشا و شکست اجرا: ناهماهنگی صحنه‌ها که اعتبار را تهدید می‌کند.\n\n"
                           "۳. نمونه‌های تحلیلی\nدر ارتباطات سیاسی، تیم کمپین صحنهٔ جلو (سخنرانی، مصاحبه، تصویررسانی) و پشت صحنه (آماده‌سازی پیام و مدیریت بحران) را هماهنگ می‌کند؛ افشای ناسازگاری میان این دو، بحران اعتبار می‌آفریند. "
                           "در شبکه‌های اجتماعی، پروفایل شخصی صحنهٔ جلو و پیام‌های خصوصی و آرشیو قدیمی، پشت صحنه‌ای است که با افشا، تعریف ارائه‌شده را فرو می‌ریزد.\n\n"
                           "۴. نقدها و چالش‌ها\nمرز صحنه‌ها همیشه روشن نیست؛ قدرت و نابرابری ساختاری کم‌بررسی می‌ماند؛ مدیریت برداشت راهبردی با بیان اصیل خود خلط می‌شود؛ در محیط دیجیتال، مرز صحنه‌ها مبهم‌تر شده است؛ و سنجش تجربی برداشت تماشاگر دشوار است.\n\n"
                           "۵. سیر تاریخی\nریشهٔ چارچوب در مقالهٔ حفظ آبرو (۱۹۵۵) و سنت کنش متقابل نمادین است. کتاب ۱۹۵۹ نسخهٔ نمایشی را تثبیت کرد. "
                           "پژوهش‌های بعدی، آن را به ارتباطات سازمانی، برندسازی شخصی و خودارائه‌گری دیجیتال گستردند؛ بولینگهام و واسکونسلوس (۲۰۱۳) نشان دادند منطق گافمن برای هویت آنلاین نیز کارآمد است.\n\n"
                           "۶. جایگاه در بحث روز\nدر محیط پلتفرمی، مدیریت برداشت به کار روزمرهٔ افراد، برندها و سیاستمداران تبدیل شده است؛ تحلیل مرز صحنه و پشت صحنه، کلید فهم رسوایی‌های دیجیتال و بحران‌های اعتبار است."),
    ),
}

NAME_FIX = {
    "MC-131": ("مدل دانش اقناع", "Persuasion Knowledge Model",
               "title_fa was an awkward «دانش شیوه‌ی ترغیب»; aligned with canonical model name used in body and sources"),
}

YEAR_FIX = {
    "MC-121": "year=1984 (Grunig & Hunt 1984); Grunig 1992 Excellence verified; Persianized glosses and recommendations",
    "MC-131": "year=1994 (Friestad & Wright 1994); replaced fabricated Entman attribution and non-existent «Everyday Persuasion» with verified Friestad & Wright 1995",
    "MC-133": "year=1974 (Rosenstock 1974); corrected garbled authors and self-efficacy attribution to Rosenstock, Strecher & Becker 1988",
    "MC-135": "year=1961 (Lavidge & Steiner 1961); corrected author names, journal venue (Journal of Marketing 25(6):59-62) and DAGMAR attribution to Colley 1961",
    "MC-143": "year=1959 (Goffman 1959); rebuilt media-economics template analysis as dramaturgical impression management; removed garbled recommendations with «پarker»",
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
                                       "verified": n_verified, "batch": 207}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH207 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
