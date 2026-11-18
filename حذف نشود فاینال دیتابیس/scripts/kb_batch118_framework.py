# -*- coding: utf-8 -*-
"""Batch 118 (FRAMEWORK): full documentation for MC-031, MC-078, MC-120, MC-123."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch118-framework-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch118_framework.json"

S = {
    "MC-031": [
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
             supports="price structure, not only price level, drives platform competition; one side is often subsidized", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Competition in Two-Sided Markets",
             title_fa="رقابت در بازارهای دوسویه",
             authors="Armstrong, M.", year=2006,
             publisher="RAND Journal of Economics",
             doi=None, url=None, language="en", isbn=None,
             citation="Armstrong, M. (2006). Competition in two-sided markets. RAND Journal of Economics, 37(3), 668-691.",
             locator="37(3):668-691", locator_type="page_range",
             supports="competition for the market with cross-group network externalities and asymmetric pricing", verified=False),
    ],
    "MC-078": [
        dict(kind="BOOK",
             title_en="Experimental and Quasi-Experimental Designs for Research",
             title_fa="طرح‌های آزمایشی و شبه‌آزمایشی در پژوهش",
             authors="Campbell, D. T.; Stanley, J. C.", year=1963,
             publisher="Houghton Mifflin",
             doi=None,
             url="https://archive.org/details/experimentalquas00camp",
             language="en", isbn=None,
             citation="Campbell, D. T., & Stanley, J. C. (1963). Experimental and quasi-experimental designs for research. Houghton Mifflin.",
             locator="ch. 1-5", locator_type="work",
             supports="internal and external validity as twin criteria; twelve threats to valid inference across sixteen designs", verified=True),
        dict(kind="BOOK",
             title_en="Quasi-Experimentation: Design and Analysis Issues for Field Settings",
             title_fa="شبه‌آزمایش: مسائل طرح و تحلیل در موقعیت‌های میدانی",
             authors="Cook, T. D.; Campbell, D. T.", year=1979,
             publisher="Houghton Mifflin",
             doi=None, url=None, language="en", isbn=None,
             citation="Cook, T. D., & Campbell, D. T. (1979). Quasi-experimentation: Design and analysis issues for field settings. Houghton Mifflin.",
             locator="chs. 1-3", locator_type="work",
             supports="extension of the validity framework with statistical conclusion validity and construct validity", verified=False),
    ],
    "MC-120": [
        dict(kind="BOOK",
             title_en="Digital Divide: Civic Engagement, Information Poverty, and the Internet Worldwide",
             title_fa="شکاف دیجیتال: مشارکت مدنی، فقر اطلاعاتی و اینترنت در جهان",
             authors="Norris, P.", year=2001,
             publisher="Cambridge University Press",
             doi=None,
             url="https://www.cambridge.org/core/books/digital-divide/20EFED5574695AC79D1BBC6E295B1EC0",
             language="en", isbn=None,
             citation="Norris, P. (2001). Digital divide: Civic engagement, information poverty, and the Internet worldwide. Cambridge University Press.",
             locator="ch. 1-3", locator_type="work",
             supports="three-level digital divide (global, social, democratic) in a 179-country comparison", verified=True),
        dict(kind="BOOK",
             title_en="The Deepening Divide: Inequality in the Information Society",
             title_fa="شکاف عمیق‌شونده: نابرابری در جامعه اطلاعاتی",
             authors="van Dijk, J. A. G. M.", year=2005,
             publisher="Sage",
             doi=None, url=None, language="en", isbn=None,
             citation="van Dijk, J. A. G. M. (2005). The deepening divide: Inequality in the information society. Sage.",
             locator="ch. 2", locator_type="work",
             supports="successive access, skills and usage divides producing unequal outcomes", verified=False),
    ],
    "MC-123": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Social Amplification of Risk: A Conceptual Framework",
             title_fa="تقویت اجتماعی ریسک: یک چارچوب مفهومی",
             authors="Kasperson, R. E.; Renn, O.; Slovic, P.; Brown, H. S.; Emel, J.; Goble, R.; Kasperson, J. X.; Ratick, S.", year=1988,
             publisher="Risk Analysis",
             doi="10.1111/j.1539-6924.1988.tb01168.x",
             url="https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1539-6924.1988.tb01168.x",
             language="en", isbn=None,
             citation="Kasperson, R. E., Renn, O., Slovic, P., Brown, H. S., Emel, J., Goble, R., Kasperson, J. X., & Ratick, S. (1988). The social amplification of risk: A conceptual framework. Risk Analysis, 8(2), 177-187.",
             locator="8(2):177-187", locator_type="page_range",
             supports="social stations amplify or attenuate risk through information processing and ripple effects", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Social Amplification of Risk Framework: New Perspectives",
             title_fa="چارچوب تقویت اجتماعی ریسک: چشم‌اندازهای تازه",
             authors="Kasperson, R. E. et al.", year=2022,
             publisher="Risk Analysis",
             doi=None, url=None, language="en", isbn=None,
             citation="Kasperson, R. E., et al. (2022). The social amplification of risk framework: New perspectives. Risk Analysis.",
             locator="2022 review article", locator_type="work",
             supports="retrospective review and clarification of the framework's mechanisms and criticisms", verified=False),
    ],
}

ENRICH = {
    "MC-031": dict(
        summary="بازارهای دوسویه و چندسویه چارچوبی اقتصادی است که توضیح می‌دهد چگونه پلتفرم‌ها دو یا چند گروه کاربری ناهمگون را به یکدیگر متصل می‌کنند و ارزش حضور هر گروه به اندازه و ترکیب گروه دیگر وابسته است. ژان‌شارل روشه و ژان تیرول در مقاله سال ۲۰۰۳ نشان دادند که در این بازارها ساختار قیمت و نه فقط سطح آن تعیین‌کننده است: پلتفرم می‌تواند یک سمت را یارانه بدهد یا رایگان نگه دارد و هزینه را از سمت دیگر بگیرد، بی‌آنکه این عدم تقارن رفتار ضد رقابتی تلقی شود. مارک آرمسترانگ در ۲۰۰۶ همین منطق را با مفهوم رقابت برای جذب هر دو سمت و اثر متقابل تقاضا صورت‌بندی کرد. در رسانه، روزنامه‌های رایگان، تلویزیون تجاری و پلتفرم‌های دیجیتال مصداق کلاسیک این چارچوب‌اند: مخاطب محتوا می‌گیرد و آگهی‌دهنده بهای دسترسی به توجه او را می‌پردازد. مسئله کانونی، یافتن ترکیبی از قیمت‌ها و قواعد دسترسی است که هر دو سمت را هم‌زمان روی پلتفرم نگه دارد، زیرا جذب یک سمت بدون سمت دیگر بی‌ارزش است. این چارچوب همچنین توضیح می‌دهد چرا یارانهٔ یک سمت، سرمایه‌گذاری در تقاضای سمت دیگر است و چرا کیفیت حکمرانی پلتفرم بر رشد آن اثر می‌گذارد. کاربرد آن در سیاست‌گذاری رسانه، مقررات پلتفرم و تحلیل مدل درآمدی سازمان‌های خبری گسترده است. نقد اصلی به این چارچوب، ساده‌سازی انگیزه‌های فرهنگی مخاطب و کم‌توجهی به قدرت انحصاری پلتفرم‌های مسلط است.",
        definition="بازار دوسویه بازاری است که در آن یک واسطه یا پلتفرم دو گروه کاربری متمایز را به هم متصل می‌کند و تصمیم هر گروه به حضور گروه دیگر بستگی دارد؛ در نسخه چندسویه، سه گروه یا بیشتر در یک ساختار مبادله مشارکت دارند.",
        main_problem="پرسش اصلی این است که چگونه می‌توان هم‌زمان دو سمت بازار را روی پلتفرم نگه داشت و درآمد را از سمتی گرفت که کمتر به حضور حساس است، بدون آنکه سمت دیگر از چرخه خارج شود.",
        mechanism="پلتفرم ابتدا سمت حساس به قیمت را با دسترسی ارزان یا رایگان جذب می‌کند تا تقاضای سمت دیگر را فعال سازد؛ سپس با تعیین کارمزد، حق دسترسی یا فروش توجه در سمت پرداخت‌کننده، هزینهٔ زیرساخت و محتوا را بازیافت می‌کند. تعادل زمانی پایدار می‌شود که نرخ جذب دو سمت هم‌زمان رشد کند و هزینهٔ جابه‌جایی کاربران بالا برود.",
        assumptions=[
            "هر دو سمت از حضور سمت دیگر سود می‌برند و این سود متقابل قابل اندازه‌گیری است.",
            "هزینهٔ جابه‌جایی و اثر شبکه، ورود رقیب تازه را پرهزینه می‌کند.",
            "پلتفرم می‌تواند گروه‌های کاربری را تفکیک کند و برای هر سمت قیمت متفاوت بگذارد.",
            "تقاضای یک سمت با کیفیت و کمیت عرضهٔ سمت دیگر رابطهٔ مستقیم دارد.",
        ],
        principles=[
            "ساختار قیمت مهم‌تر از سطح قیمت است؛ توزیع هزینه میان دو سمت تعیین‌کننده است.",
            "سمت با کشش قیمتی بالاتر یارانه می‌گیرد و سمت با کشش کمتر هزینه را می‌پردازد.",
            "اثر شبکهٔ متقاطع، ارزش پلتفرم را به ترکیب دو سمت گره می‌زند.",
            "قواعد دسترسی و کیفیت، بخشی از محصول پلتفرم برای هر دو سمت است.",
        ],
        critiques=[
            "کاهش مخاطب به تقاضای قابل قیمت‌گذاری، ابعاد فرهنگی و مدنی مصرف رسانه را نادیده می‌گیرد.",
            "چارچوب کمتر به قدرت بازار پلتفرم‌های مسلط و اثرات انحصاری آن می‌پردازد.",
            "پیش‌بینی‌های تعادلی آن در بازارهای با ترجیحات ناهمگون به‌سختی آزمون‌پذیر است.",
            "یارانهٔ یک سمت می‌تواند به کیفیت پایین محتوا و وابستگی آگهی‌محور بینجامد.",
        ],
        applications=[
            "طراحی مدل درآمدی رسانه: تعیین سمت پرداخت‌کننده و سمت دریافت‌کنندهٔ یارانه.",
            "تحلیل مقرراتی پلتفرم‌های واسط و ارزیابی رفتار قیمتی آن‌ها.",
            "ارزیابی راهبرد رشد پلتفرم‌های محتوایی و خدمات اشتراکی.",
            "تحلیل بازار آگهی و رابطهٔ آن با دسترسی آزاد به محتوا.",
        ],
        evolution="ریشهٔ بحث به ادبیات اثر شبکه و اقتصاد باشگاه‌ها بازمی‌گردد؛ روشه و تیرول (۲۰۰۳) آن را به نظریهٔ رقابت پلتفرم تبدیل کردند، آرمسترانگ (۲۰۰۶) نسخهٔ رقابت برای بازار را افزود و از دههٔ ۲۰۱۰ این چارچوب به تحلیل پلتفرم‌های دیجیتال، اقتصاد توجه و حکمرانی داده گسترش یافت.",
        key_concepts=[
            "اثر شبکهٔ متقاطع (Cross-Side Network Effect)",
            "ساختار قیمت نامتقارن (Asymmetric Price Structure)",
            "سمت یارانه‌گیر (Subsidized Side)",
            "هزینهٔ جابه‌جایی (Switching Cost)",
            "چرخهٔ مرغ و تخم‌مرغ (Chicken-and-Egg Problem)",
        ],
        theorists="ژان‌شارل روشه؛ ژان تیرول؛ مارک آرمسترانگ",
        theorists_text="روشه و تیرول (۲۰۰۳)؛ آرمسترانگ (۲۰۰۶)",
        model="دو گروه کاربر → وابستگی متقابل تقاضا → ساختار قیمت نامتقارن → تعادل و اندازهٔ پلتفرم.",
        studies=[
            "روشه و تیرول (۲۰۰۳) نشان دادند ساختار قیمت در پلتفرم‌ها تعیین‌کنندهٔ سود است، نه سطح قیمت.",
            "آرمسترانگ (۲۰۰۶) رقابت پلتفرم‌ها را با اثر شبکهٔ متقاطع و کشش تقاضای دو سمت مدل کرد.",
        ],
        detailed_analysis="تحلیل عمیق این چارچوب نشان می‌دهد که پلتفرم رسانه‌ای سه تصمیم به‌هم‌پیوسته دارد: انتخاب سمت پرداخت‌کننده، تعیین قواعد دسترسی و کیفیت، و مدیریت ریسک خروج یک سمت. این سه تصمیم در بازارهای چندسویه به هم گره خورده‌اند و تغییر یکی، تعادل کل را جابه‌جا می‌کند. مدل‌های تجربی بعدی نشان دادند که پلتفرم‌های با محتوای تولیدشده توسط کاربر، سمت توجه را تقریباً رایگان نگه می‌دارند و درآمد را از تبلیغات و داده می‌گیرند، در حالی که خدمات اشتراکی هزینه را به هر دو سمت منتقل می‌کنند. از منظر سیاست‌گذاری، این چارچوب ابزار مقایسهٔ مدل‌های درآمدی و ارزیابی اثر یارانهٔ پنهان بر کیفیت اطلاعات است.",
        critique_text="نقد اصلی این است که چارچوب، مخاطب را به تقاضای قابل قیمت‌گذاری فرو می‌کاهد و ابعاد فرهنگی، مدنی و عادتی مصرف رسانه را کنار می‌گذارد؛ همچنین قدرت انحصاری پلتفرم‌های مسلط و پیامدهای آن برای تنوع محتوا کمتر موضوع تحلیل قرار می‌گیرد.",
        example_text="مثال روشن، روزنامهٔ رایگان شهری است: نسخهٔ کاغذی برای خواننده بی‌هزینه توزیع می‌شود تا شمارگان تضمین‌شده برای آگهی‌دهنده ساخته شود؛ در نسخهٔ دیجیتال همین منطق با ترافیک سایت و سامانهٔ آگهی برنامه‌ای بازتولید می‌شود.",
        year=2003,
    ),
    "MC-078": dict(
        summary="چارچوب اعتبار درونی و بیرونی، سنجه‌ای دوگانه برای داوری دربارهٔ ارزش شناختی طرح‌های آزمایشی است. دونالد کمپبل و ژولیان استنلی در کتاب سال ۱۹۶۳ خود پرسیدند یک پژوهش تجربی تا چه حد می‌تواند تفاوت مشاهده‌شده میان گروه‌ها را به متغیر مستقل نسبت دهد و تا چه حد می‌تواند نتیجه را به جمعیت‌ها و موقعیت‌های دیگر تعمیم دهد. پاسخ آن‌ها دو معیار جدا بود: اعتبار درونی، یعنی نبود تبیین‌های بدیل برای تغییر مشاهده‌شده، و اعتبار بیرونی، یعنی قابلیت تعمیم به افراد، زمان‌ها و مکان‌های دیگر. آن‌ها دوازده تهدید را فهرست کردند که اعتبار درونی را تضعیف می‌کنند؛ از جمله تاریخ (رویدادهای هم‌زمان)، بلوغ، آزمون‌گیری مکرر، تغییر ابزار اندازه‌گیری، افت آزمودنی، انتخاب سوگیرانه و رگرسیون به میانگین. برای مهار این تهدیدها، طرح‌های آزمایشی واقعی با گمارش تصادفی و گروه کنترل پیشنهاد شد و در کنار آن، طرح‌های شبه‌آزمایشی برای موقعیت‌هایی که تصادفی‌سازی ممکن نیست معرفی شدند. تنش بنیادی این چارچوب آن است که افزایش کنترل درونی معمولاً به کاهش تعمیم‌پذیری می‌انجامد و پژوهشگر باید میان این دو، آگاهانه تعادل برقرار کند. کوک و کمپبل در ۱۹۷۹ دو نوع اعتبار دیگر را افزودند: اعتبار نتیجه‌گیری آماری و اعتبار سازه. این چارچوب امروز بنیان روش‌شناختی پژوهش کمی در ارتباطات، روان‌شناسی رسانه و ارزیابی مداخلات رسانه‌ای است و مبنای داوری دربارهٔ دقت مطالعه‌های تجربی به شمار می‌رود.",
        definition="اعتبار درونی درجهٔ اطمینانی است که تفاوت مشاهده‌شده را به متغیر مستقل نسبت می‌دهد و اعتبار بیرونی درجهٔ تعمیم‌پذیری یافته‌ها به جمعیت‌ها، موقعیت‌ها و زمان‌های دیگر است.",
        main_problem="چگونه می‌توان مطمئن شد که تغییر نگرش یا رفتار مخاطب واقعاً از پیام رسانه‌ای ناشی شده و نتیجه در موقعیت‌های واقعی بیرون آزمایشگاه نیز برقرار می‌ماند، در حالی که هر دو ادعا به‌سادگی با طرح ضعیف مخدوش می‌شوند.",
        mechanism="طرح تجربی با گمارش تصادفی، تهدیدهای انتخاب و تاریخ را به‌طور هم‌زمان توزیع می‌کند؛ گروه کنترل تغییر پایه را آشکار می‌سازد؛ پیش‌آزمون و پس‌آزمون اثر بلوغ و آزمون‌گیری را قابل تفکیک می‌کنند. هر تهدید باقیمانده، دامنهٔ ادعای علّی را محدود می‌کند.",
        assumptions=[
            "متغیر مستقل قابل دستکاری و متغیر وابسته قابل اندازه‌گیری پایا است.",
            "گمارش تصادفی توزیع متغیرهای مخدوش را میان گروه‌ها متعادل می‌کند.",
            "گروه کنترل، وضعیت پایه را بدون مداخلهٔ موردنظر نمایندگی می‌کند.",
            "اهداف تعمیم، از پیش در انتخاب نمونه و موقعیت آزمایش مشخص شده‌اند.",
        ],
        principles=[
            "اعتبار درونی پیش‌شرط هر ادعای علّی است؛ بدون آن، تفسیر علّی بی‌پایه است.",
            "اعتبار بیرونی با اعتبار درونی تنش دارد؛ کنترل بیشتر، تعمیم کمتر.",
            "هر تهدید اعتبار باید در طرح، پیش از گردآوری داده، پیش‌بینی و مهار شود.",
            "طرح شبه‌آزمایشی پذیرفتنی است، به شرط آنکه محدودیت‌های آن صریح اعلام شود.",
        ],
        critiques=[
            "تفکیک مطلق درونی و بیرونی، پیوند نظری میان مکانیسم و تعمیم را نادیده می‌گیرد.",
            "تمرکز بر طرح، نقش بافت اجتماعی و معنای فرهنگی متغیرها را کم‌رنگ می‌کند.",
            "برخی تهدیدها مانند سرایت میان گروه‌ها در میدان رسانه‌ای به‌سختی مهارشدنی است.",
            "طرح‌های تصادفی در پژوهش رسانه اغلب به دلیل اخلاقی یا عملی ناممکن‌اند.",
        ],
        applications=[
            "طراحی آزمون تجربی اثر پیام بر نگرش یا رفتار مخاطب.",
            "ارزیابی طرح‌های شبه‌آزمایشی در پژوهش میدانی رسانه.",
            "داوری دربارهٔ اعتبار مطالعه‌های کارآزمایی مداخلات رسانه‌ای سلامت.",
            "آموزش روش‌شناسی پژوهش کمی در رشته‌های ارتباطات.",
        ],
        evolution="کمپبل و استنلی (۱۹۶۳) چارچوب دوگانه را با فهرست تهدیدها و مقایسهٔ شانزده طرح بنیان گذاشتند؛ کوک و کمپبل (۱۹۷۹) دو نوع اعتبار دیگر افزودند و شادیش، کوک و کمپبل (۲۰۰۲) آن را با تأکید بر تعمیم‌پذیری و استنتاج علّی بازنویسی کردند.",
        key_concepts=[
            "اعتبار درونی (Internal Validity)",
            "اعتبار بیرونی (External Validity)",
            "تهدید اعتبار (Threat to Validity)",
            "گمارش تصادفی (Random Assignment)",
            "طرح شبه‌آزمایشی (Quasi-Experimental Design)",
        ],
        theorists="دونالد کمپبل؛ ژولیان استنلی؛ توماس کوک",
        theorists_text="کمپبل و استنلی (۱۹۶۳)؛ کوک و کمپبل (۱۹۷۹)",
        model="متغیر مستقل → گمارش تصادفی → مقایسهٔ گروه آزمایش و کنترل → مهار تهدیدها → ادعای علّی معتبر.",
        studies=[
            "کمپبل و استنلی (۱۹۶۳) شانزده طرح را در برابر دوازده تهدید اعتبار سنجیدند.",
            "کوک و کمپبل (۱۹۷۹) اعتبار نتیجه‌گیری آماری و اعتبار سازه را به چارچوب افزودند.",
        ],
        detailed_analysis="نکتهٔ کلیدی این چارچوب آن است که اعتبار، ویژگی طرح نیست بلکه ویژگی استنباط است: یک طرح ثابت می‌تواند برای یک ادعا معتبر و برای ادعایی دیگر نامعتبر باشد. بنابراین پژوهشگر پیش از گردآوری داده باید دامنهٔ ادعای خود را مشخص کند و سپس تهدیدهای مرتبط را فهرست نماید. در پژوهش رسانه، تهدیدهایی مانند سرایت پیام میان گروه‌ها، انتظار آزمودنی و استفادهٔ هم‌زمان از رسانه‌های دیگر اهمیت ویژه دارند. افزودن اعتبار سازه توسط کوک و کمپبل این پرسش را وارد کرد که آیا سنجهٔ ما واقعاً همان سازهٔ نظری را می‌سنجد. این پیشرفت، پیوند میان نظریهٔ ارتباطات و روش آزمون را تقویت کرد.",
        critique_text="نقد اصلی آن است که تفکیک درونی و بیرونی، پیوند نظری میان مکانیسم علّی و قابلیت تعمیم را نادیده می‌گیرد و تمرکز بر کنترل طرح، نقش بافت اجتماعی و معنای فرهنگی متغیرها را کم‌رنگ می‌کند.",
        example_text="در آزمون اثر کمپین سلامت، اگر گروه کنترل نیز به‌طور تصادفی پیام را از رسانهٔ دیگر دریافت کند، تهدید سرایت رخ می‌دهد و تفاوت گروه‌ها کوچک‌تر از اثر واقعی می‌شود؛ گزارش این محدودیت، بخشی از اعتبار ادعا است.",
        year=1963,
    ),
    "MC-120": dict(
        summary="شکاف دیجیتال چارچوبی است برای تحلیل نابرابری در دسترسی به فناوری اطلاعات و ارتباطات و بهره‌مندی از آن. پیپا نوریس در کتاب سال ۲۰۰۱ با مقایسهٔ ۱۷۹ کشور نشان داد که شکاف دیجیتال سه سطح دارد: شکاف جهانی میان کشورهای صنعتی و در حال توسعه، شکاف اجتماعی درون هر کشور میان گروه‌های دارای منابع و محروم، و شکاف دموکراتیک میان شهروندان فعال و غیرفعال در استفادهٔ مدنی از اینترنت. یان ون دایک در ادامه، شکاف را فرایندی چندمرحله‌ای دانست: نخست انگیزهٔ استفاده، سپس دسترسی مادی به دستگاه و اتصال، آنگاه مهارت‌های دیجیتال و در نهایت تفاوت در استفاده و پیامدهای آن. بنابراین دسترسی فیزیکی تنها نخستین آستانه است و با گسترش آن، شکاف مهارت و کیفیت بهره‌برداری اهمیت بیشتری می‌یابد. این چارچوب توضیح می‌دهد چرا سیاست‌های صرفاً مبتنی بر توزیع سخت‌افزار به کاهش نابرابری نمی‌انجامند و آموزش سواد دیجیتال، طراحی بافت‌محور و حمایت از گروه‌های کم‌درآمد را ضروری می‌سازد. در عصر پلتفرم، شکاف به سطح الگوریتمی و داده‌ای نیز گسترش یافته و پرسش‌های تازه‌ای دربارهٔ عدالت داده و دسترسی به خدمات دیجیتال پدید آورده است. نقد اصلی به این چارچوب، تمرکز بر فرد و کم‌توجهی به ساختارهای اقتصادی و زیرساختی است که نابرابری را بازتولید می‌کنند.",
        definition="شکاف دیجیتال نابرابری نظام‌مند در دسترسی، مهارت و بهره‌مندی از فناوری اطلاعات و ارتباطات است که به نابرابری‌های پیشین درآمد، تحصیلات، جنسیت و منطقه گره می‌خورد.",
        main_problem="چرا گسترش اینترنت و ارزان‌شدن دستگاه‌ها به خودی خود نابرابری‌های اطلاعاتی را از میان نمی‌برد و چگونه می‌توان سطوح تازهٔ شکاف را در سیاست‌گذاری تشخیص داد.",
        mechanism="دسترسی مادی به اتصال و دستگاه، شرط لازم است ولی کافی نیست؛ مهارت‌های عملیاتی، اطلاعاتی و راهبردی تعیین می‌کند کاربر چه استفاده‌ای می‌کند و منابع اجتماعی، انگیزه و اعتماد، عمق این استفاده را شکل می‌دهد. تفاوت در استفاده به تفاوت در فرصت‌های شغلی، آموزشی و مدنی ترجمه می‌شود.",
        assumptions=[
            "دسترسی و استفاده مراحل متمایز و قابل اندازه‌گیری‌اند.",
            "شکاف‌ها با متغیرهای جمعیتی مانند درآمد، تحصیلات و منطقه همبسته‌اند.",
            "کیفیت استفاده، نه فقط کمیت آن، پیامدهای اجتماعی را تعیین می‌کند.",
            "سیاست عمومی می‌تواند انگیزه و مهارت را مستقل از دسترسی تغییر دهد.",
        ],
        principles=[
            "شکاف دیجیتال لایه‌ای است: دسترسی، مهارت، استفاده و پیامد.",
            "رفع شکاف دسترسی بدون آموزش مهارت، شکاف دوم را عمیق‌تر می‌کند و نابرابری را جابه‌جا می‌سازد.",
            "گروه‌های محروم معمولاً در هر لایه هم‌زمان عقب‌مانده‌اند و اثرها انباشته می‌شوند.",
            "عدالت دیجیتال مستلزم طراحی خدمات متناسب با بافت محلی است.",
        ],
        critiques=[
            "تمرکز بر شکاف فردی، نقش زیرساخت و قدرت اقتصادی را کم‌رنگ می‌کند.",
            "سنجش شکاف با شاخص‌های سادهٔ دسترسی، کیفیت و پیامد را نادیده می‌گیرد.",
            "مفهوم شکاف می‌تواند نابرابری را به تأخیر موقت در پذیرش فناوری فرو بکاهد.",
            "در عصر پلتفرم، شکاف داده و الگوریتم کمتر در چارچوب اصلی دیده شده است.",
        ],
        applications=[
            "طراحی برنامه‌های سواد دیجیتال برای گروه‌های کم‌درآمد و روستایی.",
            "ارزیابی سیاست‌های دسترسی عمومی به اینترنت و خدمات دولتی دیجیتال.",
            "تحلیل نابرابری آموزشی در آموزش مجازی و دسترسی به منابع آنلاین.",
            "سنجش عدالت داده در خدمات پلتفرمی و تصمیم‌گیری الگوریتمی.",
        ],
        evolution="بحث از دههٔ ۱۹۹۰ با تقابل «دارا و ندار» اطلاعاتی آغاز شد؛ نوریس (۲۰۰۱) آن را به سه سطح جهانی، اجتماعی و دموکراتیک بسط داد، ون دایک (۲۰۰۵) مدل چندمرحله‌ای انگیزه، دسترسی، مهارت و استفاده را ارائه کرد و پژوهش‌های بعدی شکاف داده و هوش مصنوعی را افزودند.",
        key_concepts=[
            "شکاف دسترسی (Access Divide)",
            "شکاف مهارت (Skills Divide)",
            "شکاف استفاده (Usage Divide)",
            "شکاف دموکراتیک (Democratic Divide)",
            "سواد دیجیتال (Digital Literacy)",
        ],
        theorists="پیپا نوریس؛ یان ون دایک",
        theorists_text="نوریس (۲۰۰۱)؛ ون دایک (۲۰۰۵)",
        model="انگیزه → دسترسی مادی → مهارت دیجیتال → کیفیت استفاده → پیامدهای اجتماعی.",
        studies=[
            "نوریس (۲۰۰۱) با مقایسهٔ ۱۷۹ کشور سه سطح شکاف جهانی، اجتماعی و دموکراتیک را نشان داد.",
            "ون دایک (۲۰۰۵) شکاف را به زنجیرهٔ انگیزه، دسترسی، مهارت و استفاده بازتعریف کرد.",
        ],
        detailed_analysis="تحلیل عمیق نشان می‌دهد شکاف دیجیتال بیشتر از آنکه مسئلهٔ فناوری باشد، مسئلهٔ توزیع فرصت است. سیاست‌هایی که فقط اتصال را ارزان می‌کنند، شکاف دسترسی را کم می‌کنند اما شکاف مهارت و استفاده را پایدار نگه می‌دارند، زیرا مهارت در بافت خانواده، مدرسه و شبکهٔ همسالان شکل می‌گیرد. در عصر پلتفرم، لایهٔ تازه‌ای افزوده شده است: کاربران با کیفیت داده و الگوریتم‌های متفاوت روبه‌رو می‌شوند و همین تفاوت، فرصت‌های دیده‌شدن و خدمات را نابرابر می‌کند. از این رو پژوهش‌های معاصر شکاف را به عدالت داده، شفافیت الگوریتمی و توانمندسازی کاربران پیوند می‌زنند.",
        critique_text="نقد اصلی این است که چارچوب بر فرد و کاستی‌های او تمرکز می‌کند و نقش زیرساخت، قدرت اقتصادی و طراحی پلتفرم را در بازتولید نابرابری کم‌رنگ می‌سازد.",
        example_text="در یک برنامهٔ آموزش مجازی، همهٔ دانش‌آموزان ممکن است تبلت دریافت کنند، اما نداشتن اینترنت پایدار در خانه، نبود فضای آرام مطالعه و نبود مهارت جست‌وجو، استفادهٔ گروه محروم را به سطحی نازل محدود می‌کند و شکاف را بازتولید می‌سازد.",
        year=2001,
    ),
    "MC-123": dict(
        summary="چارچوب تقویت اجتماعی ریسک توضیح می‌دهد چرا ریسک درک‌شده با ریسک فنی هم‌خوان نیست. روجر کاسپرسون و همکارانش در مقالهٔ سال ۱۹۸۸ نشان دادند که رویدادهای ریسک از ایستگاه‌های اجتماعی مانند رسانه‌ها، نهادها، دانشمندان، گروه‌های فشار و شبکه‌های میان‌فردی می‌گذرند و در هر ایستگاه، پیام گزینش، رمزگذاری، قاب‌بندی و تقویت یا تضعیف می‌شود. حاصل این زنجیره می‌تواند تقویت شدید نگرانی دربارهٔ خطری کوچک یا بی‌اعتنایی به خطری بزرگ باشد. تقویت به دو شکل رخ می‌دهد: تقویت اطلاعاتی، یعنی افزایش حجم، برجستگی و تکرار پیام، و تقویت پیامدی، یعنی گسترش اثر به حوزه‌های دیگر مانند بازار، سیاست و اعتبار نهادها. اثرهای موجی، داغ‌شدن نمادین موضوع، برچسب‌خوردگی مکان یا محصول و زیان‌های ثانویه، نمونه‌های این گسترش‌اند. این چارچوب رسانه را نه آینهٔ ریسک بلکه یکی از عوامل فعال شکل‌دهی به آن می‌داند و نشان می‌دهد چگونه ارتباطات خطر می‌تواند به بحران عمومی تبدیل شود. کاربرد آن در ارتباطات بحران، سلامت عمومی، امنیت غذا و مدیریت فاجعه گسترده است. نقد اصلی به این چارچوب، ابهام مفهومی، دشواری آزمون تجربی و کم‌توجهی به ساختار قدرت رسانه‌ای است؛ با این حال بازبینی‌های بعدی آن را به یکی از پراستنادترین چارچوب‌های تحلیل ریسک تبدیل کرده است.",
        definition="تقویت اجتماعی ریسک فرایندی است که در آن رویداد یا منبع خطر از مجرای نهادها، رسانه‌ها و شبکه‌های اجتماعی می‌گذرد و در نتیجه، شدت، شکل و پیامدهای اجتماعی آن بزرگ‌تر یا کوچک‌تر از پیش‌بینی فنی می‌شود.",
        main_problem="چگونه یک خطر کوچک به بحران عمومی و یک خطر بزرگ به بی‌اعتنایی جمعی تبدیل می‌شود و رسانه در این جابه‌جایی چه نقشی دارد.",
        mechanism="پیام ریسک در هر ایستگاه اجتماعی بازتفسیر می‌شود؛ ارزش‌های خبری، منطق نهادی و شبکه‌های میان‌فردی تعیین می‌کنند کدام جنبه برجسته شود. تکرار و برجستگی، حافظه و نگرانی را افزایش می‌دهد و واکنش‌های نهادی و بازار، موج تازه‌ای از پوشش و تفسیر می‌سازد.",
        assumptions=[
            "ریسک، سازه‌ای اجتماعی است و نه فقط ویژگی فنی یک رویداد.",
            "رسانه و نهادها ایستگاه‌های فعال تفسیرند، نه مجرای بی‌طرف انتقال.",
            "تقویت و تضعیف در زنجیرهٔ اطلاعاتی قابل ردیابی است.",
            "پیامدهای ثانویه، بخشی از خود ریسک محسوب می‌شوند.",
        ],
        principles=[
            "خطر فنی و خطر درک‌شده دو کمیت متمایزند و هم‌ارز فرض نمی‌شوند.",
            "هر ایستگاه اجتماعی می‌تواند نقش تقویت‌کننده یا تضعیف‌کننده بگیرد.",
            "برجستگی رسانه‌ای، نگرانی عمومی و فشار نهادی به‌صورت بازخوردی به هم وابسته‌اند.",
            "مدیریت ریسک باید ارتباطات خطر را بخشی از فرایند تصمیم بداند.",
        ],
        critiques=[
            "مفاهیم چارچوب چنان گسترده‌اند که آزمون‌پذیری تجربی آن دشوار است.",
            "سنجش تقویت و تضعیف با شاخص‌های روشن کمتر انجام شده است.",
            "نقش ساختار مالکیت و منافع رسانه در تقویت کم‌تر تحلیل شده است.",
            "چارچوب می‌تواند به ساده‌سازی رابطهٔ رسانه و افکار عمومی بیانجامد.",
        ],
        applications=[
            "مدیریت ارتباطات بحران و پاسخ به هشدارهای سلامت عمومی.",
            "تحلیل پوشش خبری مخاطرات محیطی و فناورانه.",
            "طراحی پیام‌های خطر برای گروه‌های با ادراک متفاوت.",
            "ارزیابی پیامدهای اقتصادی و سیاسی برچسب‌خوردگی مکان یا محصول.",
        ],
        evolution="کاسپرسون و همکاران (۱۹۸۸) چارچوب را برای پیوند ارزیابی فنی و تحلیل اجتماعی عرضه کردند؛ پژوهش‌های بعدی ایستگاه‌های تقویت، اثر موجی و برچسب‌خوردگی را گستردند و بازبینی ۲۰۲۲ چارچوب را با شواهد و نقدهای تازه بازخوانی کرد.",
        key_concepts=[
            "ایستگاه تقویت (Amplification Station)",
            "اثر موجی (Ripple Effect)",
            "تقویت اطلاعاتی و پیامدی (Informational/Consequential Amplification)",
            "برچسب‌خوردگی (Stigma)",
            "زیان ثانویه (Secondary Impact)",
        ],
        theorists="روجر کاسپرسون؛ اورت‌وین رن؛ پاول اسلوویچ؛ ژان کاسپرسون",
        theorists_text="کاسپرسون و همکاران (۱۹۸۸)",
        model="رویداد خطر → منابع و کانال‌های اطلاعات → ایستگاه‌های اجتماعی → تفسیر مخاطب → واکنش نهادی و بازخورد موجی.",
        studies=[
            "کاسپرسون و همکاران (۱۹۸۸) زنجیرهٔ تقویت و تضعیف ریسک را از منبع تا پیامدهای ثانویه ترسیم کردند.",
            "بازبینی کاسپرسون و همکاران (۲۰۲۲) شواهد سه دهه پژوهش و نقدهای روش‌شناختی را جمع‌بندی کرد.",
        ],
        detailed_analysis="تحلیل عمیق چارچوب نشان می‌دهد که تقویت ریسک اغلب از تعامل منطق خبری و منطق نهادی زاده می‌شود: رسانه به دنبال برجستگی و روایت است و نهاد به دنبال مدیریت مسئولیت؛ تقاطع این دو، چرخهٔ بازخوردی می‌سازد که در آن واکنش نهاد به پوشش خبری، موضوع تازه‌ای برای پوشش می‌آفریند. برچسب‌خوردگی نشان می‌دهد چگونه اثر ریسک از خود رویداد فراتر می‌رود و به مکان، محصول یا گروهی خاص می‌چسبد. از این رو ارتباطات خطر موفق نه تنها انتقال اطلاعات دقیق، بلکه مدیریت انتظارات، اعتماد و عدالت توزیعی است. پژوهش‌های دیجیتال معاصر، شبکه‌های اجتماعی را به عنوان ایستگاهی با سرعت و بازخورد بی‌سابقه به این زنجیره افزوده‌اند.",
        critique_text="نقد اصلی آن است که مفاهیم چارچوب چنان گسترده‌اند که آزمون تجربی را دشوار می‌کنند و نقش ساختار مالکیت و منافع رسانه در تقویت ریسک کم‌تر تحلیل می‌شود.",
        example_text="در ماجرای آلودگی یک محصول غذایی، انتشار یک گزارش اولیه می‌تواند با تکرار در رسانه‌های خبری، واکنش سازمان نظارتی، افت فروش و سپس پوشش خبری دربارهٔ افت فروش، موجی از تقویت بسازد که پیامدهای اقتصادی آن از خطر اولیه بزرگ‌تر باشد.",
        year=1988,
    ),
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


NAME_FIX = {}
YEAR_FIX = {}


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
                                       "verified": n_verified, "batch": 118}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH118 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
