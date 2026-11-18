# -*- coding: utf-8 -*-
"""Batch 145 (MODEL): full documentation for MC-494, MC-495, MC-497, MC-501."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch145-model-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch145_model.json"

S = {
    "MC-494": [
        dict(kind="WEBSITE",
             title_en="Ivy Lee's Declaration of Principles (1906)",
             title_fa="اعلامیهٔ اصول آیوی لی (۱۹۰۶)",
             authors="PR Academy", year=1906,
             publisher="PR Academy",
             doi=None,
             url="https://pracademy.co.uk/insights/ivy-lee-and-the-origins-of-the-press-release/",
             language="en", isbn=None,
             citation="PR Academy. (2014). Ivy Lee and the origins of the press release. Retrieved from PR Academy.",
             locator="article", locator_type="SECTION",
             supports="public information model as accurate and prompt disclosure to the press", verified=True),
        dict(kind="BOOK",
             title_en="Managing Public Relations",
             title_fa="مدیریت روابط عمومی",
             authors="Grunig, J. E.; Hunt, T.", year=1984,
             publisher="Holt, Rinehart and Winston",
             doi=None,
             url="https://archive.org/details/managingpublicre0000unse",
             language="en", isbn=None,
             citation="Grunig, J. E., & Hunt, T. (1984). Managing Public Relations. New York: Holt, Rinehart and Winston.",
             locator="book", locator_type="SECTION",
             supports="public information model as one of four historical models of public relations", verified=True),
    ],
    "MC-495": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Building Dialogic Relationships through the World Wide Web",
             title_fa="ساختن روابط گفت‌وگویی از راه وب جهانی",
             authors="Kent, M. L.; Taylor, M.", year=1998,
             publisher="Public Relations Review",
             doi=None,
             url="https://www.sciencedirect.com/science/article/pii/S036381119980143X",
             language="en", isbn=None,
             citation="Kent, M. L., & Taylor, M. (1998). Building dialogic relationships through the World Wide Web. Public Relations Review, 24(3), 321-334.",
             locator="24(3):321-334", locator_type="page_range",
             supports="five dialogic principles for organization-public relationships online", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Toward a Dialogic Theory of Public Relations",
             title_fa="به‌سوی نظریهٔ گفت‌وگویی روابط عمومی",
             authors="Kent, M. L.; Taylor, M.", year=2002,
             publisher="Public Relations Review",
             doi="10.1016/S0363-8111(02)00108-X",
             url="https://www.sciencedirect.com/science/article/abs/pii/S036381110200108X",
             language="en", isbn=None,
             citation="Kent, M. L., & Taylor, M. (2002). Toward a dialogic theory of public relations. Public Relations Review, 28(1), 21-37.",
             locator="28(1):21-37", locator_type="page_range",
             supports="dialogic theory grounded in mutuality, propinquity, empathy, risk and commitment", verified=True),
    ],
    "MC-497": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Choosing the Right Words: The Development of Guidelines for the Selection of the Appropriate Crisis-Response Strategies",
             title_fa="انتخاب واژه‌های درست: تدوین رهنمودهایی برای گزینش راهبردهای مناسب پاسخ به بحران",
             authors="Coombs, W. T.", year=1995,
             publisher="Management Communication Quarterly",
             doi="10.1177/0893318995008004003",
             url="https://journals.sagepub.com/doi/10.1177/0893318995008004003",
             language="en", isbn=None,
             citation="Coombs, W. T. (1995). Choosing the right words: The development of guidelines for the selection of the appropriate crisis-response strategies. Management Communication Quarterly, 8(4), 447-476.",
             locator="8(4):447-476", locator_type="page_range",
             supports="guidelines matching crisis types and responsibility attribution to response strategies", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Protecting Organization Reputations During a Crisis: The Development and Application of Situational Crisis Communication Theory",
             title_fa="حفاظت از شهرت سازمان در بحران: تدوین و کاربرد نظریهٔ موقعیتی ارتباطات بحران",
             authors="Coombs, W. T.", year=2007,
             publisher="Corporate Reputation Review",
             doi="10.1057/palgrave.crr.1550049",
             url="https://link.springer.com/article/10.1057/palgrave.crr.1550049",
             language="en", isbn=None,
             citation="Coombs, W. T. (2007). Protecting organization reputations during a crisis: The development and application of situational crisis communication theory. Corporate Reputation Review, 10(3), 163-176.",
             locator="10(3):163-176", locator_type="page_range",
             supports="situational matching of crisis clusters and response strategies", verified=True),
    ],
    "MC-501": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Platform Competition in Two-Sided Markets",
             title_fa="رقابت پلتفرم در بازارهای دوسویه",
             authors="Rochet, J.-C.; Tirole, J.", year=2003,
             publisher="Journal of the European Economic Association",
             doi=None,
             url="https://academic.oup.com/jeea/article-abstract/1/4/990/2280902",
             language="en", isbn=None,
             citation="Rochet, J.-C., & Tirole, J. (2003). Platform competition in two-sided markets. Journal of the European Economic Association, 1(4), 990-1029.",
             locator="1(4):990-1029", locator_type="page_range",
             supports="price structure and cross-side network effects in two-sided markets", verified=True),
        dict(kind="BOOK_CHAPTER",
             title_en="The Media and Advertising: A Tale of Two-Sided Markets",
             title_fa="رسانه و تبلیغات: حکایت بازارهای دوسویه",
             authors="Anderson, S. P.; Gabszewicz, J. J.", year=2006,
             publisher="Elsevier (Handbook of the Economics of Art and Culture, vol. 1)",
             doi=None,
             url="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=831807",
             language="en", isbn=None,
             citation="Anderson, S. P., & Gabszewicz, J. J. (2006). The media and advertising: A tale of two-sided markets. In V. Ginsburgh & D. Throsby (Eds.), Handbook of the Economics of Art and Culture (vol. 1, pp. 567-614). Amsterdam: Elsevier.",
             locator="vol. 1:567-614", locator_type="page_range",
             supports="media markets as two-sided markets linking audiences and advertisers", verified=True),
    ],
}

ENRICH = {
    "MC-494": dict(
        year=1906,
        summary="مدل اطلاع‌رسانی عمومی، که در تاریخ روابط عمومی با آیوی لی و اعلامیهٔ اصول او در سال ۱۹۰۶ پیوند دارد، دومین مدل از چهار مدل تاریخی روابط عمومی در دسته‌بندی گرونیگ و هانت است. در این مدل، سازمان اطلاعات دقیق و به‌موقع را در اختیار رسانه می‌گذارد و به‌جای دستکاری یا پنهان‌کاری، بر شفافیت تکیه می‌کند. لی اعلام کرد که دفتر او برای تأمین خبر باز است و اطلاعات دربارهٔ موضوعات مورد علاقهٔ عمومی را بدون هزینه در اختیار خبرنگاران می‌گذارد. کارگزار روابط عمومی در این مدل شبیه روزنامه‌نگار درون‌سازمانی عمل می‌کند: خبر را جمع‌آوری، تنظیم و منتشر می‌سازد. بیانیهٔ مطبوعاتی، ابزار اصلی انتقال این اطلاعات است و رسانه، کانال بازنشر آن. با این حال، ارتباط همچنان یک‌سویه است و بازخورد ساختارمند یا مذاکرهٔ معنادار با مخاطب پیش‌بینی نمی‌شود. نقدهای اصلی به این مدل، یک‌سویه‌بودن و نبود گفت‌وگو، گزینش اطلاعات مطلوب سازمان، فرض بی‌طرفی سازمان و کاربرد آن به‌عنوان ابزار مدیریت شهرت به‌جای پاسخ‌گویی واقعی را برجسته می‌کنند.",
        definition="مدل اطلاع‌رسانی عمومی، الگویی یک‌سویه از روابط عمومی است که سازمان را موظف به انتشار اطلاعات درست و به‌موقع برای رسانه و عموم می‌داند و کارگزار روابط عمومی را به روزنامه‌نگار درون‌سازمانی شبیه می‌کند.",
        main_problem="سازمان چگونه می‌تواند با انتشار اطلاعات درست و به‌موقع، اعتماد رسانه و عموم را جلب کند و از بدنامی ناشی از پنهان‌کاری بپرهیزد.",
        mechanism="سازمان اطلاعات دقیق را جمع‌آوری و در قالب بیانیه یا خبر منتشر می‌کند؛ رسانه آن را بازنشر می‌دهد و عموم بر پایهٔ شفافیت اعتماد می‌سازد؛ جریان ارتباط از سازمان به مخاطب و بدون بازخورد ساختارمند است.",
        assumptions=[
            "انتشار اطلاعات درست، اعتماد می‌سازد.",
            "رسانه کانال انتقال اطلاعات سازمان است.",
            "شفافیت جای دستکاری را می‌گیرد.",
            "سازمان می‌تواند اطلاعات را بی‌طرفانه منتشر کند.",
            "بازخورد ساختارمند ضروری نیست.",
        ],
        principles=[
            "اطلاعات درست و به‌موقع را منتشر کن.",
            "دسترسی رسانه به خبر را تسهیل کن.",
            "پنهان‌کاری و دستکاری را کنار بگذار.",
            "بیانیهٔ خبری را ابزار انتقال دقیق بدان.",
            "نقش روزنامه‌نگار درون‌سازمانی را بازشناس.",
            "محدودیت یک‌سویه‌بودن مدل را بپذیر.",
            "منافع عمومی را در انتخاب خبر در نظر بگیر.",
        ],
        critiques=[
            "ارتباط را یک‌سویه نگه می‌دارد.",
            "گفت‌وگو و بازخورد ساختارمند ندارد.",
            "انتشار اطلاعات را گزینشی و به نفع سازمان می‌کند.",
            "بی‌طرفی سازمان را بیش از واقع فرض می‌گیرد.",
            "می‌تواند به ابزار مدیریت شهرت بدل شود.",
            "سرعت انتشار می‌تواند دقت را قربانی کند.",
            "اعتماد به رسانه را به بازنشر وابسته می‌کند.",
        ],
        critique_text="منتقدان می‌گویند مدل اطلاع‌رسانی عمومی گامی اخلاقی از تبلیغ‌گری به شفافیت بود اما همچنان یک‌سویه است و سازمان می‌تواند با گزینش اطلاعات، تصویری مطلوب از خود بسازد؛ با این حال، پایهٔ روابط عمومی حرفه‌ای و شفافیت سازمانی شد.",
        applications=[
            "تدوین سیاست شفافیت سازمانی.",
            "آموزش نگارش بیانیهٔ خبری.",
            "مدیریت بحران با اطلاع‌رسانی سریع.",
            "تحلیل تاریخی روابط عمومی.",
            "مقایسهٔ مدل‌های یک‌سویه و دوسویه.",
            "آموزش شفافیت در نهادهای عمومی.",
            "طراحی سامانهٔ اطلاع‌رسانی عمومی.",
        ],
        example_text="دانشگاهی که پس از یک حادثه در آزمایشگاه، بی‌درنگ اطلاعات دقیق دربارهٔ علت، دامنه و اقدامات جبرانی منتشر می‌کند، با شفافیت اعتماد عمومی را حفظ می‌کند؛ اما اگر همان اطلاعات را گزینشی و بدون پذیرش مسئولیت منتشر کند، مدل به ابزار مدیریت شهرت فرو می‌کاهد.",
        evolution="مدل در سال ۱۹۰۶ با اعلامیهٔ اصول آیوی لی شکل گرفت و در قرن بیستم به یکی از چهار مدل تاریخی روابط عمومی تبدیل شد. با ظهور روابط عمومی دوسویه، جایگاه آن به‌عنوان حداقل اخلاقی شفافیت تثبیت شد.",
        key_concepts=["اطلاع‌رسانی عمومی", "اعلامیهٔ اصول", "شفافیت", "بیانیهٔ خبری", "روزنامه‌نگار درون‌سازمانی", "اعتماد"],
        theorists="آیوی لی.",
        theorists_text="مدل در سنت روابط عمومی سازمانی و اطلاع‌رسانی به رسانه شکل گرفت.",
        model="جریان یک‌سویهٔ اطلاعات درست و شفاف از سازمان به رسانه و عموم که اعتماد می‌سازد اما بازخورد ساختارمند ندارد.",
        studies=[
            "اعلامیهٔ سال ۱۹۰۶ اصول اطلاع‌رسانی شفاف را بیان کرد.",
            "پژوهش سال ۱۹۸۴ آن را مدل اطلاع‌رسانی عمومی نامید.",
            "مطالعات بحران، شفافیت سریع را عامل حفظ اعتماد یافتند.",
            "ادبیات روابط عمومی، محدودیت یک‌سویه‌بودن را نقد کرد.",
            "مطالعات بحران، بیانیه را ابزار پاسخ یافتند.",
            "پژوهش تاریخ روابط عمومی، لی را نقطهٔ گذار دانست.",
        ],
    ),
    "MC-495": dict(
        year=1998,
        summary="مدل گفت‌وگویی روابط عمومی، که مایکل کنت و مورین تیلور در سال ۱۹۹۸ برای روابط سازمان و مخاطب در وب معرفی کردند و در سال ۲۰۰۲ به نظریه‌ای عمومی گستردند، روابط عمومی را گفت‌وگویی برابر و دوسویه می‌داند، نه انتقال پیام از سازمان به مخاطب. آن‌ها پنج اصل برای وب پیشنهاد کردند: حلقهٔ گفت‌وگو، سودمندی اطلاعات، ایجاد انگیزهٔ بازگشت، سهولت رابط کاربری و حفظ بازدیدکننده. در نظریهٔ سال ۲۰۰۲، پنج ویژگی گفت‌وگوی اصیل را برشمردند: دوسویگی، نزدیکی، همدلی، پذیرش خطر و تعهد. گفت‌وگو در این معنا پیش از اقناع و مدیریت شهرت می‌آید و مستلزم آن است که سازمان امکان پاسخ واقعی و تغییر موضع را بپذیرد. مدل، وب و شبکه‌های اجتماعی را فضایی برای گفت‌وگوی مستقیم با مخاطب می‌بیند و بر تعامل پایدار در برابر کمپین یک‌باره تأکید می‌کند. نقدهای اصلی به آن، آرمانی‌بودن شرایط گفت‌وگوی برابر در سازمان‌های قدرت‌محور، دشواری سنجش گفت‌وگوی واقعی، خطر مصادرهٔ گفت‌وگو برای مدیریت تصویر، مقیاس‌ناپذیری در مخاطبان انبوه و کم‌توجهی به نابرابری منابع را برجسته می‌کنند.",
        definition="مدل گفت‌وگویی، روابط عمومی را تعامل دوسویه و برابر سازمان و مخاطب می‌داند که با دوسویگی، نزدیکی، همدلی، پذیرش خطر و تعهد، به فهم مشترک و رابطهٔ پایدار می‌رسد.",
        main_problem="چگونه سازمان می‌تواند به‌جای انتقال یک‌سویهٔ پیام، با مخاطب وارد گفت‌وگوی واقعی شود و امکان پاسخ و تغییر موضع را بپذیرد.",
        mechanism="سازمان فضایی برای شنیدن و پاسخ‌گویی می‌سازد، اطلاعات سودمند ارائه می‌کند و انگیزهٔ بازگشت مخاطب را فراهم می‌سازد؛ در گفت‌وگوی اصیل، هر دو طرف با همدلی و پذیرش خطر موضع خود را بازبینی می‌کنند و رابطه در طول زمان شکل می‌گیرد.",
        assumptions=[
            "مخاطب شریک گفت‌وگوست، نه هدف پیام.",
            "گفت‌وگوی اصیل مستلزم پذیرش خطر است.",
            "همدلی و نزدیکی، پیش‌شرط فهم مشترک‌اند.",
            "فضای دیجیتال امکان تعامل مستقیم می‌دهد.",
            "رابطهٔ پایدار بر کمپین یک‌باره مقدم است.",
        ],
        principles=[
            "حلقهٔ گفت‌وگو را در وب باز نگه دار.",
            "اطلاعات سودمند و قابل استفاده ارائه کن.",
            "انگیزهٔ بازگشت مخاطب را بساز.",
            "رابط کاربری را ساده و دعوت‌کننده کن.",
            "بازدیدکننده را در سایت حفظ کن.",
            "پذیرش خطر و امکان تغییر موضع را جدی بگیر.",
            "صداهای منتقد را در گفت‌وگو وارد کن.",
        ],
        critiques=[
            "گفت‌وگوی برابر در سازمان قدرت‌محور آرمانی است.",
            "سنجش گفت‌وگوی واقعی دشوار است.",
            "خطر مصادرهٔ گفت‌وگو برای مدیریت تصویر وجود دارد.",
            "در مخاطبان انبوه مقیاس‌پذیر نیست.",
            "نابرابری منابع دو طرف را کم‌بررسی می‌گذارد.",
            "گفت‌وگو با مخاطب سازمان‌یافته محدود می‌شود.",
        ],
        critique_text="منتقدان می‌گویند مدل گفت‌وگویی افق اخلاقی مهمی برای روابط عمومی گشود اما شرایط گفت‌وگوی برابر را بیش از واقع فرض می‌کند و می‌تواند به ابزار تازهٔ مدیریت تصویر بدل شود؛ با این حال، معیار سنجش تعامل سازمان و مخاطب در فضای دیجیتال شد.",
        applications=[
            "طراحی وب‌سایت و شبکه‌های اجتماعی سازمان.",
            "مدیریت تعامل با مشتری و پاسخ‌گویی.",
            "روابط عمومی بحران و گفت‌وگو با ذی‌نفعان.",
            "ارزیابی کیفیت تعامل سازمان و مخاطب.",
            "آموزش اخلاق گفت‌وگو در روابط عمومی.",
            "طراحی سامانهٔ بازخورد عمومی.",
        ],
        example_text="سازمانی که در شبکهٔ اجتماعی نه‌تنها اطلاعیه می‌گذارد بلکه به نقدها پاسخ می‌دهد، در صورت خطا عذرخواهی می‌کند و سیاست خود را تغییر می‌دهد، حلقهٔ گفت‌وگو را کامل می‌کند؛ اگر همان سازمان فقط نظرات را حذف کند، مدل به نمایش تعامل فرو می‌کاهد.",
        evolution="مدل در مقالهٔ سال ۱۹۹۸ برای وب معرفی شد و در مقالهٔ سال ۲۰۰۲ به نظریهٔ گفت‌وگویی عمومی گسترش یافت. با رشد شبکه‌های اجتماعی، به چارچوب اصلی ارزیابی تعامل سازمان و مخاطب تبدیل شد و پژوهش‌های بعدی آن را برای پلتفرم‌های جدید به کار بردند.",
        key_concepts=["گفت‌وگو", "دوسویگی", "نزدیکی", "همدلی", "پذیرش خطر", "تعهد", "حلقهٔ گفت‌وگو"],
        theorists="مایکل کنت و مورین تیلور.",
        theorists_text="مدل در سنت روابط عمومی دوسویه و ارتباطات دیجیتال شکل گرفت.",
        model="چرخهٔ گفت‌وگوی برابر سازمان و مخاطب که با پنج ویژگی گفت‌وگوی اصیل به فهم مشترک و رابطهٔ پایدار می‌رسد.",
        studies=[
            "مقالهٔ سال ۱۹۹۸ پنج اصل گفت‌وگو در وب را معرفی کرد.",
            "مقالهٔ سال ۲۰۰۲ نظریهٔ گفت‌وگویی را گسترد.",
            "مطالعات وب، کیفیت تعامل سازمان‌ها را سنجیدند.",
            "پژوهش شبکه‌های اجتماعی، گفت‌وگو را در پلتفرم‌ها آزمود.",
            "پژوهش رسانه، اصول پنج‌گانه را آزمود.",
        ],
    ),
    "MC-497": dict(
        year=1995,
        summary="مدل ارتباطات بحران، که تیموتی کومبز در سال ۱۹۹۵ با رهنمودهای گزینش راهبرد پاسخ و در سال ۲۰۰۷ با نظریهٔ موقعیتی ارتباطات بحران گسترد، ارتباط سازمان در بحران را بر پایهٔ میزان مسئولیت منتسب به سازمان توضیح می‌دهد. بحران‌ها در سه خوشه دسته‌بندی می‌شوند: قربانی، حادثه‌ای و قابل پیشگیری. هرچه مسئولیت سازمان بیشتر باشد، تهدید شهرت جدی‌تر است و راهبرد پاسخ قوی‌تر باید باشد. راهبردها چهار خانواده‌اند: انکار، تقلیل، بازسازی و تقویت. سازمان نخست باید اطلاعات هدایتی و تنظیمی در اختیار مخاطبان بگذارد و سپس بر پایهٔ موقعیت، راهبرد پاسخ را انتخاب کند. مدل بر هم‌خوانی پاسخ با نوع بحران و پیشینهٔ شهرت تأکید می‌کند و پاسخ ناهم‌خوان را تهدیدی برای اعتبار می‌داند. نقدهای اصلی به آن، تمرکز بر شهرت سازمان به‌جای آسیب دیدگان، سوگیری مدیریتی، نمونهٔ عمدتاً شرکتی و غربی، فرض ثبات بحران و کم‌توجهی به بحران‌های شبکه‌ای و چندصدایی را برجسته می‌کنند.",
        definition="مدل ارتباطات بحران، گزینش راهبرد پاسخ سازمان را بر پایهٔ نوع بحران، میزان مسئولیت منتسب و تهدید شهرت توضیح می‌دهد و چهار خانوادهٔ انکار، تقلیل، بازسازی و تقویت را از هم جدا می‌کند.",
        main_problem="سازمان در بحران چگونه باید پاسخ دهد تا هم اطلاعات لازم را برساند و هم تهدید شهرت را بر پایهٔ مسئولیت منتسب مدیریت کند.",
        mechanism="نوع بحران، مسئولیت منتسب و پیشینهٔ شهرت، تهدید ادراک‌شده را می‌سازند؛ سازمان با اطلاعات هدایتی و تنظیمی آغاز می‌کند و سپس راهبرد پاسخ متناسب با خوشهٔ بحران را برمی‌گزیند؛ پاسخ ناهم‌خوان، تهدید را تشدید می‌کند.",
        assumptions=[
            "مسئولیت منتسب، شدت تهدید را تعیین می‌کند.",
            "بحران‌ها در خوشه‌های قابل تشخیص جای می‌گیرند.",
            "پاسخ باید با نوع بحران هم‌خوان باشد.",
            "اطلاعات هدایتی بر پاسخ اقناعی مقدم است.",
            "پیشینهٔ شهرت بر تفسیر پاسخ اثر می‌گذارد.",
        ],
        principles=[
            "نوع بحران و مسئولیت منتسب را تشخیص بده.",
            "نخست اطلاعات هدایتی و تنظیمی بده.",
            "راهبرد پاسخ را با خوشهٔ بحران هم‌خوان کن.",
            "پاسخ ناهم‌خوان را به‌عنوان تهدید بشناس.",
            "پیشینهٔ شهرت را در انتخاب پاسخ لحاظ کن.",
            "منافع آسیب‌دیدگان را بر شهرت مقدم بدان.",
            "پیام بحران را با شواهد مستند کن.",
            "زمان‌بندی پاسخ را مدیریت کن.",
        ],
        critiques=[
            "بر شهرت سازمان به‌جای آسیب‌دیدگان تمرکز دارد.",
            "سوگیری مدیریتی و شرکتی دارد.",
            "نمونه‌ها عمدتاً غربی‌اند.",
            "ثبات بحران را بیش از واقع فرض می‌کند.",
            "بحران‌های شبکه‌ای و چندصدایی را کم‌بررسی می‌گذارد.",
            "نقش رسانه و افکار عمومی را کم‌بررسی می‌گذارد.",
            "راهبرد تقلیل می‌تواند به انکار عملی بدل شود.",
        ],
        critique_text="منتقدان می‌گویند مدل ارتباطات بحران ابزار دقیقی برای هم‌خوانی پاسخ و موقعیت ساخت اما تمرکز آن بر شهرت سازمان، خطر نادیده‌گرفتن آسیب‌دیدگان را دارد و بحران‌های دیجیتال چندصدایی را کامل پوشش نمی‌دهد؛ با این حال، چارچوب مرجع مدیریت بحران است.",
        applications=[
            "مدیریت ارتباطات بحران سازمانی.",
            "آموزش سخنگو و پیام بحران.",
            "ارزیابی پاسخ سازمان پس از بحران.",
            "طراحی برنامهٔ آمادگی بحران.",
            "تحلیل بحران در شبکه‌های اجتماعی.",
            "طراحی سناریوی پاسخ چندمرحله‌ای.",
            "آموزش هم‌دلی با آسیب‌دیدگان.",
        ],
        example_text="شرکتی که نقص فنی محصولش آسیب رسانده است، اگر مسئولیت را انکار کند و تنها بر شهرت خود تمرکز کند، بحران را تشدید می‌کند؛ اما اگر اطلاعات دقیق بدهد، مسئولیت را بپذیرد، جبران کند و سپس اقدامات اصلاحی را تقویت کند، پاسخش با خوشهٔ بحران قابل پیشگیری هم‌خوان می‌شود.",
        evolution="مدل در مقالهٔ سال ۱۹۹۵ کومبز با رهنمودهای گزینش راهبرد شکل گرفت و در مقالهٔ سال ۲۰۰۷ به نظریهٔ موقعیتی ارتباطات بحران گسترش یافت. پس از آن، به چارچوب اصلی پژوهش و آموزش مدیریت بحران تبدیل شد و در عصر شبکه‌های اجتماعی بازبینی شد.",
        key_concepts=["بحران", "مسئولیت منتسب", "انکار", "تقلیل", "بازسازی", "تقویت", "تهدید شهرت"],
        theorists="تیموتی کومبز.",
        theorists_text="مدل در سنت مدیریت بحران و ارتباطات سازمانی شکل گرفت.",
        model="هم‌خوانی خوشهٔ بحران، مسئولیت منتسب و راهبرد پاسخ برای مدیریت تهدید شهرت و اطلاع‌رسانی به مخاطبان.",
        studies=[
            "مقالهٔ سال ۱۹۹۵ رهنمودهای پاسخ بحران را تدوین کرد.",
            "مقالهٔ سال ۲۰۰۷ نظریهٔ موقعیتی را گسترد.",
            "مطالعات بحران، هم‌خوانی پاسخ و موقعیت را آزمودند.",
            "پژوهش شبکه‌های اجتماعی، بحران چندصدایی را بررسی کرد.",
            "مطالعات موردی، خوشه‌های بحران را مقایسه کردند.",
            "پژوهش رسانه، پوشش بحران را تحلیل کرد.",
        ],
    ),
    "MC-501": dict(
        year=2003,
        summary="مدل دو بازار، که ژان شارل روشه و ژان تیرول در سال ۲۰۰۳ برای تحلیل رقابت پلتفرم‌ها صورت‌بندی کردند و سایمون اندرسون و ژان گابژوویچ آن را به رسانه و تبلیغات گستردند، بازارهایی را توصیف می‌کند که یک پلتفرم دو گروه کاربری متمایز را به هم پیوند می‌دهد. در رسانه، این دو گروه مخاطب و تبلیغ‌دهنده‌اند: رسانه با محتوا مخاطب را جذب می‌کند و دسترسی به او را به تبلیغ‌دهنده می‌فروشد. ویژگی کلیدی، اثر شبکه‌ای بین‌گروهی است: ارزش پلتفرم برای یک گروه به شمار یا کیفیت گروه دیگر بستگی دارد. به همین دلیل، ساختار قیمت مهم‌تر از سطح کل قیمت است و پلتفرم ممکن است یک طرف را یارانه بدهد و هزینه را از طرف دیگر بگیرد. مدل نشان می‌دهد چرا خدمات رسانه‌ای رایگان برای مخاطب می‌تواند سودآور باشد و چرا پلتفرم‌ها بر رشد یک طرف بازار سرمایه‌گذاری می‌کنند. نقدهای اصلی به آن، تقلیل بُعد فرهنگی و سیاسی رسانه به منطق بازار، ناسازگاری نسبی با پلتفرم‌های چندطرفه و داده‌محور، دشواری سنجش توجه و ارزش مخاطب و کم‌توجهی به قدرت انحصاری پلتفرم‌ها را برجسته می‌کنند.",
        definition="مدل دو بازار، پلتفرم رسانه‌ای را واسطه‌ای می‌داند که دو گروه مخاطب و تبلیغ‌دهنده را به هم پیوند می‌دهد و با مدیریت ساختار قیمت و اثرهای شبکه‌ای بین‌گروهی، هر دو طرف را هم‌زمان تأمین می‌کند.",
        main_problem="پلتفرم رسانه‌ای چگونه با پیوند دو گروه مخاطب و تبلیغ‌دهنده و تعیین ساختار قیمت، هم مشارکت هر دو طرف و هم سودآوری خود را ممکن می‌سازد.",
        mechanism="محتوا مخاطب را جذب می‌کند و اندازهٔ مخاطب، ارزش دسترسی برای تبلیغ‌دهنده را می‌سازد؛ افزایش یک طرف، ارزش طرف دیگر را بالا می‌برد و پلتفرم با یارانهٔ یک طرف و قیمت‌گذاری طرف دیگر تعادل را مدیریت می‌کند.",
        assumptions=[
            "دو گروه کاربری متمایز وجود دارد.",
            "ارزش یک طرف به حضور طرف دیگر بستگی دارد.",
            "ساختار قیمت بر سطح کل قیمت مقدم است.",
            "پلتفرم می‌تواند یک طرف را یارانه بدهد.",
            "دسترسی به مخاطب کالای قابل فروش است.",
        ],
        principles=[
            "دو طرف بازار و نیازهایشان را جدا تحلیل کن.",
            "اثر شبکه‌ای بین‌گروهی را بسنج.",
            "ساختار قیمت را ابزار تعادل بدان.",
            "طرف کم‌کشش را با یارانه جذب کن.",
            "کیفیت مخاطب را فراتر از شمار بشمار.",
            "قدرت انحصاری پلتفرم را در تحلیل لحاظ کن.",
            "رفاه دو طرف را در تصمیم لحاظ کن.",
        ],
        critiques=[
            "بُعد فرهنگی و سیاسی را به بازار تقلیل می‌دهد.",
            "با پلتفرم‌های چندطرفه و داده‌محور کامل هم‌خوان نیست.",
            "سنجش توجه و ارزش مخاطب دشوار است.",
            "قدرت انحصاری پلتفرم‌ها را کم‌بررسی می‌گذارد.",
            "فرض دو طرف ثابت، پویایی بازار را ساده می‌کند.",
        ],
        critique_text="منتقدان می‌گویند مدل دو بازار منطق اقتصادی رسانه‌های آگهی‌محور را روشن کرد اما خطر دارد فرهنگ و سیاست را به اثر جانبی بازار فرو بکاهد و با پلتفرم‌های چندطرفهٔ امروز کامل هم‌خوان نیست؛ با این حال، پایهٔ تحلیل اقتصاد پلتفرم رسانه است.",
        applications=[
            "تحلیل مدل درآمدی رسانه و پلتفرم.",
            "سیاست‌گذاری رقابت در بازارهای دیجیتال.",
            "مطالعهٔ تبلیغات هدفمند و قیمت‌گذاری.",
            "ارزیابی اثر شبکه‌ای در شبکه‌های اجتماعی.",
            "تحلیل اقتصاد بازارگاه‌های محتوا.",
        ],
        example_text="شبکهٔ اجتماعی محتوای رایگان به کاربر می‌دهد و در برابر، دسترسی به توجه او را به تبلیغ‌دهنده می‌فروشد؛ هرچه کاربران بیشتر شوند، تبلیغ‌دهندگان بیشتری جذب می‌شوند و ارزش شبکه برای هر دو طرف بالا می‌رود. این چرخه، منطق مدل دو بازار است.",
        evolution="مدل در مقالهٔ سال ۲۰۰۳ روشه و تیرول صورت‌بندی شد و در فصل سال ۲۰۰۶ اندرسون و گابژوویچ به رسانه و تبلیغات گسترش یافت. پس از آن، به چارچوب اصلی اقتصاد پلتفرم و سیاست رقابت دیجیتال تبدیل شد.",
        key_concepts=["بازار دوسویه", "اثر شبکه‌ای بین‌گروهی", "ساختار قیمت", "مخاطب", "تبلیغ‌دهنده", "یارانهٔ متقابل"],
        theorists="ژان شارل روشه و ژان تیرول.",
        theorists_text="مدل در سنت اقتصاد صنعتی و اقتصاد رسانه شکل گرفت.",
        model="پلتفرم واسطه که با پیوند مخاطب و تبلیغ‌دهنده و مدیریت ساختار قیمت، اثر شبکه‌ای بین‌گروهی را به درآمد تبدیل می‌کند.",
        studies=[
            "مقالهٔ سال ۲۰۰۳ رقابت پلتفرم دوسویه را مدل کرد.",
            "فصل سال ۲۰۰۶ مدل را به رسانه و تبلیغات برد.",
            "پژوهش رقابت، ساختار قیمت را آزمود.",
            "مطالعات پلتفرم، اثر شبکه‌ای را بررسی کردند.",
        ],
    ),
}

NAME_FIX = {
    "MC-494": ("مدل اطلاع‌رسانی عمومی", "Public Information Model", "عنوان پیشین «مدل اطلاعات عمومی» مبهم بود؛ «اطلاع‌رسانی» معنای انتشار فعال و شفاف اطلاعات سازمانی را می‌رساند."),
    "MC-495": ("مدل گفت‌وگویی روابط عمومی", "The Dialogic Model of Public Relations", "قلمرو روابط عمومی به نام افزوده شد تا مدل از مفهوم عام گفت‌وگو جدا شود."),
    "MC-497": ("مدل ارتباطات بحران (نظریهٔ موقعیتی)", "Situational Crisis Communication Model", "عنوان پیشین «مدل بحران و ارتباطات بحران» دوری و مبهم بود؛ نام متعارف نظریهٔ موقعیتی ارتباطات بحران کومبز ثبت شد."),
}
YEAR_FIX = {}

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
                                       "verified": n_verified, "batch": 145}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH145 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
