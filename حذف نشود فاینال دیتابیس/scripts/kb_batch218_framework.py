# -*- coding: utf-8 -*-
"""Batch 218: repair MC-549, MC-583, MC-584, MC-587, MC-588."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch218-20261117"
NOW = "2026-11-17 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch218.json"

S = {
    "MC-549": [
        dict(kind="BOOK_CHAPTER", title_en="A Cultural Approach to Communication",
             title_fa="رهیافتی فرهنگی به ارتباط",
             authors="James W. Carey", year=1989, publisher="Unwin Hyman",
             doi=None, url="https://web.mit.edu/21l.432/www/readings/Carey_CulturalApproachCommunication.pdf",
             language="en", isbn=None,
             citation="Carey, J. W. (1989). A cultural approach to communication. In Communication as Culture: Essays on Media and Society. Boston: Unwin Hyman.",
             locator="chapter", locator_type="CHAPTER",
             supports="communication as a symbolic process that constructs a shared reality", verified=True),
        dict(kind="WEBSITE", title_en="Ritual View of Communication",
             title_fa="دیدگاه آیینی ارتباط",
             authors="EBSCO Research Starters", year=None, publisher="EBSCO",
             doi=None, url="https://www.ebsco.com/research-starters/communication-and-mass-media/ritual-view-communication",
             language="en", isbn=None,
             citation="EBSCO Research Starters. (n.d.). Ritual view of communication. EBSCO.",
             locator="web page", locator_type="PAGE",
             supports="definition and attribution of the ritual view to Carey", verified=True),
    ],
    "MC-583": [
        dict(kind="BOOK", title_en="Managing Public Relations",
             title_fa="مدیریت روابط عمومی",
             authors="James E. Grunig; Todd Hunt", year=1984, publisher="Holt, Rinehart and Winston",
             doi=None, url="https://archive.org/details/managingpublicre0000unse",
             language="en", isbn=None,
             citation="Grunig, J. E., & Hunt, T. (1984). Managing Public Relations. New York: Holt, Rinehart and Winston.",
             locator="book", locator_type="BOOK",
             supports="four models of public relations including two-way symmetrical", verified=True),
        dict(kind="BOOK_CHAPTER", title_en="Two-Way Symmetrical Public Relations: Past, Present, and Future",
             title_fa="روابط عمومی دوسویهٔ متقارن: گذشته، حال و آینده",
             authors="James E. Grunig", year=2001, publisher="SAGE",
             doi=None, url="https://sk.sagepub.com/hnbk/edvol/handbook-of-public-relations/chpt/twoway-symmetrical-public-relations-past-present",
             language="en", isbn=None,
             citation="Grunig, J. E. (2001). Two-way symmetrical public relations: Past, present, and future. In R. L. Heath (Ed.), Handbook of Public Relations (pp. 11-32). Thousand Oaks: SAGE.",
             locator="pp. 11-32", locator_type="PAGE",
             supports="normative statement and defense of the symmetrical model", verified=True),
    ],
    "MC-584": [
        dict(kind="JOURNAL_ARTICLE", title_en="The Limits of Symmetry: A Game Theory Approach to Symmetric and Asymmetric Public Relations",
             title_fa="حدود تقارن: رهیافتی از نظریهٔ بازی به روابط عمومی متقارن و نامتقارن",
             authors="Priscilla Murphy", year=1991, publisher="Public Relations Research Annual",
             doi=None, url="https://www.semanticscholar.org/paper/The-Limits-of-Symmetry%3A-A-Game-Theory-Approach-to-Murphy/bd81bb4ead94b703718a0899284ec426ade4a938",
             language="en", isbn=None,
             citation="Murphy, P. (1991). The limits of symmetry: A game theory approach to symmetric and asymmetric public relations. Public Relations Research Annual, 3, 115-131.",
             locator="3, 115-131", locator_type="PAGE",
             supports="mixed-motive game framing of symmetric and asymmetric public relations", verified=True),
        dict(kind="BOOK_CHAPTER", title_en="Game Theory",
             title_fa="نظریهٔ بازی",
             authors="SAGE Encyclopedia of Public Relations", year=None, publisher="SAGE Publications",
             doi=None, url="https://sk.sagepub.com/ency/edvol/download/encyclopedia-of-public-relations-2e/chpt/game-theory.pdf",
             language="en", isbn=None,
             citation="SAGE Encyclopedia of Public Relations (2nd ed.). Entry: Game theory. Thousand Oaks: SAGE Publications.",
             locator="entry", locator_type="CHAPTER",
             supports="definition of game-theoretic concepts applied to public relations", verified=True),
    ],
    "MC-587": [
        dict(kind="JOURNAL_ARTICLE", title_en="Interpersonal Approaches to Communication Research",
             title_fa="رهیافت‌های میان‌فردی در پژوهش ارتباط",
             authors="Jack M. McLeod; Steven H. Chaffee", year=1973, publisher="American Behavioral Scientist",
             doi="10.1177/000276427301600402",
             url="https://journals.sagepub.com/doi/abs/10.1177/000276427301600402",
             language="en", isbn=None,
             citation="McLeod, J. M., & Chaffee, S. H. (1973). Interpersonal approaches to communication research. American Behavioral Scientist, 16(4), 469-499.",
             locator="16(4), 469-499", locator_type="PAGE",
             supports="coorientation framework with agreement, accuracy and congruency", verified=True),
        dict(kind="REPORT", title_en="Family Communication Patterns: Measuring Intrapersonal Perceptions of Interpersonal Relationships",
             title_fa="الگوهای ارتباط خانوادگی: سنجش ادراک درون‌فردی از روابط میان‌فردی",
             authors="L. David Ritchie", year=1990, publisher="Portland State University",
             doi=None, url="https://pdxscholar.library.pdx.edu/cgi/viewcontent.cgi?article=1099&context=comm_fac",
             language="en", isbn=None,
             citation="Ritchie, L. D. (1990). Family communication patterns: Measuring intrapersonal perceptions of interpersonal relationships. Repository copy, Portland State University.",
             locator="report", locator_type="PAGE",
             supports="application of coorientation measures to family communication", verified=True),
    ],
    "MC-588": [
        dict(kind="JOURNAL_ARTICLE", title_en="Stormy Weather: Testing Stealing Thunder as a Crisis Communication Strategy to Improve Communication Flow Between Organizations and Journalists",
             title_fa="هوای طوفانی: آزمون دزدیدن رعد به‌عنوان راهبرد ارتباط بحران",
             authors="Laura M. Arpan; Donnalyn Pompper", year=2003, publisher="Public Relations Review",
             doi=None, url="https://www.sciencedirect.com/science/article/abs/pii/S0363811103000432",
             language="en", isbn=None,
             citation="Arpan, L. M., & Pompper, D. (2003). Stormy weather: Testing stealing thunder as a crisis communication strategy to improve communication flow between organizations and journalists. Public Relations Review, 29(3), 291-308.",
             locator="29(3), 291-308", locator_type="PAGE",
             supports="experimental evidence that self-disclosure improves journalist evaluations", verified=True),
        dict(kind="JOURNAL_ARTICLE", title_en="Weathering the Crisis: Effects of Stealing Thunder in Crisis Communication",
             title_fa="از سر گذراندن بحران: اثرهای دزدیدن رعد در ارتباط بحران",
             authors="Sang Yeal Lee", year=2016, publisher="Public Relations Review",
             doi=None, url="https://www.sciencedirect.com/science/article/abs/pii/S0363811115301661",
             language="en", isbn=None,
             citation="Lee, S. Y. (2016). Weathering the crisis: Effects of stealing thunder in crisis communication. Public Relations Review.",
             locator="article", locator_type="PAGE",
             supports="boundary conditions and mechanisms of the stealing-thunder effect", verified=True),
    ],
}

ENRICH = {
    "MC-549": dict(
        needs_enrichment=False,
        level="میان",
        related_approaches="چرخش فرهنگی در ارتباطات؛ نشانه‌شناسی؛ مطالعات فرهنگی؛ آیین رسانه‌ای؛ حافظهٔ جمعی.",
        recommended_sources="«ارتباط به‌مثابه فرهنگ» (کری، ۱۹۸۹)؛ «رهیافتی فرهنگی به ارتباط» (کری، ۱۹۸۹)؛ «دیدگاه آیینی ارتباط» (ای‌بی‌اس‌کو)؛ «بازنمایی» (هال).",
        detailed_analysis=("۱. بنیان و منطق نظری\nکری (۱۹۸۹) ارتباط را فرایندی نمادین دانست که در آن انسان‌ها تجربهٔ مشترک را بازنمایی می‌کنند و واقعیت اجتماعی را می‌سازند. "
                           "در این نگرش رسانه آینهٔ جهان نیست، بلکه با انتخاب، چارچوب‌بندی و روایت، نسخه‌ای نمادین از جهان می‌سازد. تمایز انتقالی-آیینی، پیش‌فرض این مدل است و در رکورد جداگانه‌ای تحلیل شده است.\n\n"
                           "۲. ساختارهای مفهومی\nفرایند نمادین، بازنمایی، فرهنگ مشترک، آیین، معنا و واقعیت اجتماعی سازه‌های اصلی‌اند. مدل پرسش خود را از «پیام چگونه منتقل می‌شود» به «چه معنایی مشترک ساخته می‌شود» تغییر می‌دهد.\n\n"
                           "۳. نمونه‌های تحلیلی\nخبر تنها گزارش رویداد نیست، بلکه آیینی است که جامعه را در تصور مشترک از واقعیت سهیم می‌کند؛ پوشش یک مناسک ملی یا بحران، هویت جمعی را بازسازی می‌کند؛ تبلیغ نیز افزون بر فروش، سبک زندگی و ارزش را بازنمایی می‌کند.\n\n"
                           "۴. نقدها و چالش‌ها\nخطر ایده‌آلیسم و کم‌رنگ‌شدن ساختار قدرت وجود دارد؛ مدل به تحلیل ایدئولوژی و مالکیت رسانه کمتر می‌پردازد؛ آزمون تجربی آن دشوار است؛ و ممکن است اثر پیام و اقناع را در سایهٔ فرهنگ کم‌بررسی بگذارد.\n\n"
                           "۵. سیر تاریخی\nکتاب ۱۹۸۹ به یکی از متون بنیادین چرخش فرهنگی تبدیل شد و پژوهش‌های آیین رسانه‌ای، حافظهٔ جمعی و تحلیل بازنمایی بر آن تکیه کردند.\n\n"
                           "۶. جایگاه در بحث روز\nدر تحلیل محتوای دیجیتال و آیین‌های شبکه‌های اجتماعی، مدل ارتباط به‌مثابه فرهنگ یادآوری می‌کند که رسانه تنها اطلاعات جابه‌جا نمی‌کند، بلکه جهان مشترک می‌سازد."),
    ),
    "MC-583": dict(
        needs_enrichment=False,
        level="میان",
        related_approaches="مدل‌های چهارگانهٔ روابط عمومی؛ نظریهٔ تعالی؛ گفت‌وگوی عمومی؛ اخلاق ارتباطات؛ مدیریت تعارض.",
        recommended_sources="«مدیریت روابط عمومی» (گرونیگ و هانت، ۱۹۸۴)؛ «روابط عمومی دوسویهٔ متقارن» (گرونیگ، ۲۰۰۱)؛ «نظریهٔ تعالی و عمل روابط عمومی مؤثر» (گرونیگ، ۱۹۹۲).",
        detailed_analysis=("۱. بنیان و منطق نظری\nگرونیگ و هانت (۱۹۸۴) چهار مدل تاریخی روابط عمومی را معرفی کردند: عامل مطبوعاتی، اطلاع‌رسانی عمومی، دوسویهٔ نامتقارن و دوسویهٔ متقارن. "
                           "در مدل متقارن، سازمان با پژوهش و گفت‌وگو هم مخاطب را می‌فهمد و هم خود را در برابر او تغییر می‌دهد؛ هدف فهم مشترک و حل تعارض است، نه اقناع یک‌سویه.\n\n"
                           "۲. ساختارهای مفهومی\nتقارن، پژوهش مخاطب، تغییر متقابل، فهم مشترک، مذاکره و حل تعارض سازه‌های اصلی‌اند. مدل، معیاری هنجاری برای حرفه‌ای‌گری است.\n\n"
                           "۳. نمونه‌های تحلیلی\nسازمانی که پیش از تغییر سیاست، نظرسنجی و جلسهٔ گفت‌وگو با گروه‌های ذی‌نفع برگزار می‌کند و سیاست را اصلاح می‌کند، در عمل مدل متقارن را اجرا می‌کند؛ در بحران نیز پاسخ‌گویی و پذیرش مسئولیت نمونهٔ آن است.\n\n"
                           "۴. نقدها و چالش‌ها\nاجرای تقارن کامل در سازمان‌های قدرت‌محور دشوار است؛ نقدهایی چون لی‌تانگ بر اروپامحوری و هنجاری‌بودن مدل تأکید کرده‌اند؛ سنجش تقارن تجربی سخت است؛ و برخی پژوهش‌ها نشان داده‌اند سازمان‌ها بیشتر به تقارن «پیرو منفعت» گرایش دارند تا تقارن واقعی.\n\n"
                           "۵. سیر تاریخی\nکتاب ۱۹۸۴ چارچوب را ساخت، نظریهٔ تعالی دههٔ ۱۹۹۰ آن را به برنامهٔ پژوهشی گسترد و بازنگری ۲۰۰۱ در کتاب راهنما پاسخ نویسنده به نقدها بود.\n\n"
                           "۶. جایگاه در بحث روز\nدر گفتمان اخلاق ارتباطات و مسئولیت اجتماعی، مدل دوسویهٔ متقارن همچنان معیار سنجش کیفیت روابط عمومی است، هرچند اجرای آن به توزیع واقعی قدرت وابسته است."),
    ),
    "MC-584": dict(
        needs_enrichment=False,
        level="میان",
        related_approaches="نظریهٔ بازی؛ مدل دوسویهٔ متقارن؛ مذاکره؛ مدیریت تعارض؛ روابط عمومی راهبردی.",
        recommended_sources="«حدود تقارن» (مورفی، ۱۹۹۱)؛ «نظریهٔ بازی» (دانشنامهٔ روابط عمومی سیج)؛ «مدیریت روابط عمومی» (گرونیگ و هانت، ۱۹۸۴)؛ «مذاکره» (فیشر و یوری).",
        detailed_analysis=("۱. بنیان و منطق نظری\nمورفی (۱۹۹۱) با تکیه بر نظریهٔ بازی استدلال کرد روابط عمومی واقعی معمولاً بازی مختلط‌انگیزه است: هر طرف هم انگیزهٔ همکاری دارد و هم انگیزهٔ پیشبرد منافع خود. "
                           "بنابراین تقارن مطلق نه همیشه ممکن است و نه همیشه مطلوب؛ ارتباط مؤثر، مدیریت هوشمندانهٔ ترکیب همکاری و رقابت است.\n\n"
                           "۲. ساختارهای مفهومی\nبازی مختلط‌انگیزه، منافع مشترک و متعارض، راهبرد غالب، تعادل و پیش‌بینی رفتار طرف مقابل سازه‌های اصلی‌اند. مدل تقارن را از حالت آرمانی به تصمیم راهبردی می‌آورد.\n\n"
                           "۳. نمونه‌های تحلیلی\nدر مذاکره با گروه معترض، سازمان می‌تواند هم‌زمان برای حفظ اعتماد همکاری کند و برای محدودکردن خسارت شهرت، منافع خود را پیش ببرد؛ انتخاب اینکه کدام راهبرد غالب شود به ساختار بازی و انتظارات طرف مقابل بستگی دارد.\n\n"
                           "۴. نقدها و چالش‌ها\nنظریهٔ بازی رفتار را عقلانی و منافع را قابل محاسبه فرض می‌کند؛ احساسات، ارزش‌ها و روابط بلندمدت را کم‌بررسی می‌گذارد؛ خطر توجیه رفتار نامتقارن با استدلال «بازی مختلط» وجود دارد؛ و سنجش تجربی مفروضات آن دشوار است.\n\n"
                           "۵. سیر تاریخی\nمقالهٔ ۱۹۹۱ نقطهٔ عطف نقد درونی نظریهٔ تقارن بود و پژوهش‌های بعدی دربارهٔ روابط عمومی راهبردی و مذاکره بر آن تکیه کردند.\n\n"
                           "۶. جایگاه در بحث روز\nدر روابط عمومی راهبردی و مدیریت بحران، مدل انگیزهٔ مختلط واقع‌بینانه‌تر از تقارن آرمانی است، به شرط آنکه بهانهٔ توجیه یک‌سویگی نشود."),
    ),
    "MC-587": dict(
        needs_enrichment=False,
        level="میان",
        related_approaches="ارتباطات میان‌فردی؛ ادراک اجتماعی؛ الگوهای ارتباط خانوادگی؛ ارتباطات سازمانی؛ پژوهش مخاطب.",
        recommended_sources="«رهیافت‌های میان‌فردی در پژوهش ارتباط» (مک‌لوید و چفی، ۱۹۷۳)؛ «الگوهای ارتباط خانوادگی» (ریچی، ۱۹۹۰)؛ «نظریهٔ هم‌جهت‌یابی» در پژوهش ارتباط.",
        detailed_analysis=("۱. بنیان و منطق نظری\nمک‌لوید و چفی (۱۹۷۳) هم‌جهت‌یابی را جایگزین مدل انتقالی ساده در پژوهش ارتباط میان‌فردی کردند. "
                           "در این مدل هر طرف سه عنصر دارد: خود، طرف دیگر و موضوع؛ و ارتباط مؤثر یعنی هم‌سوسازی ادراک دو طرف دربارهٔ موضوع.\n\n"
                           "۲. ساختارهای مفهومی\nسه مؤلفهٔ اصلی عبارت‌اند از توافق (نگرش مشابه به موضوع)، دقت (درست‌فهمیدن نگرش طرف دیگر) و هم‌خوانی (تصور درست از آنچه طرف دیگر دربارهٔ ما فکر می‌کند).\n\n"
                           "۳. نمونه‌های تحلیلی\nسازمان و افکار عمومی می‌توانند در نگرش به یک سیاست توافق داشته باشند اما هر یک تصور نادرستی از نگرش دیگری داشته باشد؛ چنین وضعی هم‌جهت‌یابی پایین است و ارتباط را مختل می‌کند؛ در خانواده نیز همین سه مؤلفه الگوی گفت‌وگو را می‌سازد.\n\n"
                           "۴. نقدها و چالش‌ها\nمدل ایستا است و پویایی تغییر نگرش را کم نشان می‌دهد؛ سنجش هم‌خوانی به گزارش خود افراد وابسته است؛ مرز نگرش و ادراک در عمل مبهم است؛ و در بافت‌های فرهنگی متفاوت، معیارهای توافق و دقت یکسان نیست.\n\n"
                           "۵. سیر تاریخی\nمقالهٔ ۱۹۷۳ چارچوب را در پژوهش ارتباط میان‌فردی تثبیت کرد و پژوهش‌های الگوهای ارتباط خانوادگی و ارتباط سازمانی آن را به کار بستند.\n\n"
                           "۶. جایگاه در بحث روز\nدر سنجش شکاف ادراکی میان سازمان و مخاطب، مدل هم‌جهت‌یابی ابزار دقیقی برای جداکردن «اختلاف واقعی» از «سوءبرداشت» است."),
    ),
    "MC-588": dict(
        needs_enrichment=False,
        level="میان",
        related_approaches="ارتباط بحران؛ شفافیت سازمانی؛ اس‌سی‌سی‌تی؛ مدیریت شهرت؛ روزنامه‌نگاری و منبع خبر.",
        recommended_sources="«هوای طوفانی: آزمون دزدیدن رعد» (آرپان و پامپر، ۲۰۰۳)؛ «از سر گذراندن بحران» (لی، ۲۰۱۶)؛ «ارتباط بحران» (کومبز).",
        detailed_analysis=("۱. بنیان و منطق نظری\n«دزدیدن رعد» راهبردی پیش‌دستانه در ارتباط بحران است: سازمان پیش از افشای خبر توسط رسانه یا دیگران، خودش بحران را اعلام می‌کند. "
                           "آرپان و پامپر (۲۰۰۳) در آزمایشی نشان دادند افشای خودخواسته ارزیابی خبرنگاران از سازمان را بهبود می‌دهد و پوشش منفی را کاهش می‌دهد؛ لی (۲۰۱۶) شرایط مرزی این اثر را بررسی کرد.\n\n"
                           "۲. ساختارهای مفهومی\nافشای پیش‌دستانه، منبع اولیه بودن، کنترل روایت، شفافیت، اعتبار و چارچوب‌بندی خبر سازه‌های اصلی‌اند.\n\n"
                           "۳. نمونه‌های تحلیلی\nشرکتی که پیش از انتشار گزارش رسانه‌ای دربارهٔ نقص محصول، خودش جزئیات و برنامهٔ اصلاح را اعلام می‌کند، روایت اول را می‌سازد؛ در مقابل، سازمانی که منتظر افشا می‌ماند در موضع پاسخ‌دهنده و مدافع قرار می‌گیرد.\n\n"
                           "۴. نقدها و چالش‌ها\nاثر مثبت به نوع بحران، مسئولیت سازمان و اعتبار پیشین آن بستگی دارد؛ افشای زودهنگام اطلاعات ناقص می‌تواند اعتماد را تخریب کند؛ خطر دستکاری روایت و پنهان‌کاری زیر پوشش شفافیت وجود دارد؛ و شواهد در بافت‌های غیرآزمایشی محدود است.\n\n"
                           "۵. سیر تاریخی\nپژوهش ۲۰۰۳ مفهوم را در ادبیات ارتباط بحران تثبیت کرد و مطالعات ۲۰۱۶ به بعد سازوکارها و شرایط مرزی آن را گستردند؛ این راهبرد با نظریه‌های پاسخ‌گویی و شهرت پیوند یافت.\n\n"
                           "۶. جایگاه در بحث روز\nدر محیط خبری سریع شبکه‌های اجتماعی، پیش‌دستی در افشا به راهبرد رایج سازمان‌ها تبدیل شده است، هرچند صداقت و کامل‌بودن اطلاعات شرط اثرگذاری آن است."),
    ),
}

NAME_FIX = {}

YEAR_FIX = {
    "MC-549": "replaced media-economics template analysis with Carey cultural-approach analysis; differentiated from MC-548 (transmission-vs-ritual record)",
    "MC-583": "replaced media-economics template analysis with Grunig-Hunt symmetrical-model analysis; rebuilt recommendations",
    "MC-584": "replaced media-economics template analysis with Murphy game-theory analysis; rebuilt recommendations",
    "MC-587": "replaced media-economics template analysis with coorientation analysis; rebuilt recommendations",
    "MC-588": "replaced media-economics template analysis with stealing-thunder analysis; rebuilt recommendations",
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
                                       "verified": n_verified, "batch": 218}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH218 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
