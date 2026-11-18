# -*- coding: utf-8 -*-
"""Batch 192: card-71 Grounded Theory, card-77 Q-Method, MTH-006 Digital Media Analysis, MTH-007 Computational Analysis (METHOD)."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch192-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch192.json"

METHOD_MAPPING = {"entity_type": "METHOD", "content_type": "روش پژوهش (Research Method)",
                  "needs_review": False}

S = {
    "card-71": [
        dict(kind="BOOK",
             title_en="The Discovery of Grounded Theory: Strategies for Qualitative Research",
             title_fa="کشف نظریهٔ داده‌بنیاد: راهبردهایی برای پژوهش کیفی",
             authors="Barney G. Glaser; Anselm L. Strauss", year=1967,
             publisher="Aldine Publishing",
             doi=None,
             url="http://www.sxf.uevora.pt/wp-content/uploads/2013/03/Glaser_1967.pdf",
             language="en", isbn=None,
             citation="Glaser, B. G., & Strauss, A. L. (1967). The Discovery of Grounded Theory: Strategies for Qualitative Research. Chicago: Aldine Publishing.",
             locator="chapters on constant comparison, theoretical sampling and theoretical saturation",
             locator_type="CHAPTER",
             supports="the original statement of grounded theory as theory generated from data through constant comparison",
             verified=True),
        dict(kind="BOOK",
             title_en="Basics of Qualitative Research: Grounded Theory Procedures and Techniques",
             title_fa="مبانی پژوهش کیفی: رویه‌ها و تکنیک‌های نظریهٔ داده‌بنیاد",
             authors="Anselm L. Strauss; Juliet M. Corbin", year=1990,
             publisher="Sage Publications",
             doi=None,
             url="https://archive.org/details/basicsofqualitat0000stra",
             language="en", isbn="0803932502",
             citation="Strauss, A., & Corbin, J. (1990). Basics of Qualitative Research: Grounded Theory Procedures and Techniques. Newbury Park, CA: Sage Publications.",
             locator="open coding, axial coding, selective coding, process and the conditional matrix",
             locator_type="CHAPTER",
             supports="the procedural codification of grounded theory: open, axial and selective coding plus the coding paradigm",
             verified=True),
    ],
    "card-77": [
        dict(kind="BOOK",
             title_en="The Study of Behavior: Q-Technique and Its Methodology",
             title_fa="مطالعهٔ رفتار: تکنیک کیو و روش‌شناسی آن",
             authors="William Stephenson", year=1953,
             publisher="University of Chicago Press",
             doi=None,
             url="https://archive.org/details/studyofbehaviorq0000step_w8l1",
             language="en", isbn=None,
             citation="Stephenson, W. (1953). The Study of Behavior: Q-Technique and Its Methodology. Chicago: University of Chicago Press.",
             locator="the original formulation of Q-technique and its factor-analytic rationale",
             locator_type="CHAPTER",
             supports="the founding statement of Q-methodology as the inverted factor analysis of persons rather than variables",
             verified=True),
        dict(kind="BOOK",
             title_en="Political Subjectivity: Applications of Q Methodology in Political Science",
             title_fa="ذهنیت سیاسی: کاربردهای روش کیو در علم سیاست",
             authors="Steven R. Brown", year=1980,
             publisher="Yale University Press",
             doi=None,
             url="https://qmethod.org/readings/",
             language="en", isbn=None,
             citation="Brown, S. R. (1980). Political Subjectivity: Applications of Q Methodology in Political Science. New Haven, CT: Yale University Press.",
             locator="concourse theory, the forced distribution and factor interpretation",
             locator_type="CHAPTER",
             supports="the standard application manual of Q-methodology, including concourse construction and factor interpretation",
             verified=True),
    ],
    "MTH-006": [
        dict(kind="BOOK",
             title_en="Digital Methods",
             title_fa="روش‌های دیجیتال",
             authors="Richard Rogers", year=2013,
             publisher="MIT Press",
             doi=None,
             url="https://mitpress.mit.edu/9780262018838/digital-methods/",
             language="en", isbn="9780262018838",
             citation="Rogers, R. (2013). Digital Methods. Cambridge, MA: MIT Press.",
             locator="chapters on the natively digital, issue mapping and the study of information flows",
             locator_type="CHAPTER",
             supports="the programmatic statement of digital methods: methods that follow the medium rather than importing offline methods",
             verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Critical Questions for Big Data: Provocations for a Cultural, Technological, and Scholarly Phenomenon",
             title_fa="پرسش‌های انتقادی دربارهٔ کلان‌داده: تحریک‌هایی برای یک پدیدهٔ فرهنگی، فناورانه و علمی",
             authors="danah boyd; Kate Crawford", year=2012,
             publisher="Information, Communication & Society",
             doi="10.1080/1369118X.2012.678878",
             url="https://www.tandfonline.com/doi/full/10.1080/1369118X.2012.678878",
             language="en", isbn=None,
             citation="boyd, d., & Crawford, K. (2012). Critical questions for big data: Provocations for a cultural, technological, and scholarly phenomenon. Information, Communication & Society, 15(5), 662-679.",
             locator="pp. 662-679", locator_type="PAGE",
             supports="six critical questions on big data, including sampling, context, ethics and the redefinition of knowledge",
             verified=True),
    ],
    "MTH-007": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Computational Social Science",
             title_fa="علوم اجتماعی محاسباتی",
             authors="David Lazer; Alex Pentland; Lada Adamic; Sinan Aral; Albert-Laszlo Barabasi; Devon Brewer; Nicholas Christakis; Noshir Contractor; James Fowler; Myron Gutmann; Tony Jebara; Gary King; Michael Macy; Deb Roy; Marshall Van Alstyne", year=2009,
             publisher="Science",
             doi="10.1126/science.1167742",
             url="https://www.science.org/doi/10.1126/science.1167742",
             language="en", isbn=None,
             citation="Lazer, D., Pentland, A., Adamic, L., Aral, S., Barabasi, A.-L., Brewer, D., Christakis, N., Contractor, N., Fowler, J., Gutmann, M., Jebara, T., King, G., Macy, M., Roy, D., & Van Alstyne, M. (2009). Computational social science. Science, 323(5915), 721-723.",
             locator="pp. 721-723", locator_type="PAGE",
             supports="the manifesto for computational social science built on digital traces and large-scale data",
             verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Critical Questions for Big Data: Provocations for a Cultural, Technological, and Scholarly Phenomenon",
             title_fa="پرسش‌های انتقادی دربارهٔ کلان‌داده: تحریک‌هایی برای یک پدیدهٔ فرهنگی، فناورانه و علمی",
             authors="danah boyd; Kate Crawford", year=2012,
             publisher="Information, Communication & Society",
             doi="10.1080/1369118X.2012.678878",
             url="https://www.tandfonline.com/doi/full/10.1080/1369118X.2012.678878",
             language="en", isbn=None,
             citation="boyd, d., & Crawford, K. (2012). Critical questions for big data: Provocations for a cultural, technological, and scholarly phenomenon. Information, Communication & Society, 15(5), 662-679.",
             locator="pp. 662-679", locator_type="PAGE",
             supports="the critique of validity, sampling and ethics that frames the limits of computational analysis",
             verified=True),
    ],
}

ENRICH = {
    "card-71": dict(
        year=1967,
        mapping=METHOD_MAPPING,
        summary="نظریهٔ داده‌بنیاد روش‌شناسی کیفی استقرایی است که گلیزر و استراوس آن را در ۱۹۶۷ برای ساختن نظریه از دل داده صورت‌بندی کردند. پژوهشگر بدون تحمیل چارچوب پیشین، داده را در میدان گرد می‌آورد، با مقایسهٔ مداوم کد می‌زند و تا اشباع نظری پیش می‌رود. امروز این روش در پرستاری، آموزش، مدیریت و مطالعات رسانه پرکاربردترین رویکرد کیفی است و چند شاخهٔ رقیب دارد.",
        definition="نظریهٔ داده‌بنیاد یک روش‌شناسی کیفی است که نظریه‌ای منظم دربارهٔ یک فرایند یا کنش اجتماعی را نه از فرضیه‌های قیاسی، بلکه از دل داده‌های میدانی می‌سازد؛ سازوکار آن کدگذاری باز، محوری و انتخابی در کنار مقایسهٔ مداوم و نمونه‌گیری نظری است.",
        main_problem="چگونه می‌توان نظریه‌ای علمی و مستند از داده‌های تجربی استخراج کرد، بدون اینکه پیش از پژوهش با فرضیه‌ها یا ادبیات موجود محدود شود؟",
        mechanism="پژوهشگر با جمع‌آوری داده‌های اولیه (مصاحبه، مشاهده) آغاز می‌کند، داده را کدگذاری باز می‌کند تا مفاهیم اولیه پدید آیند، سپس در کدگذاری محوری روابط میان مقوله‌ها را حول یک مقولهٔ مرکزی سازمان می‌دهد و در کدگذاری انتخابی نظریهٔ یکپارچه را می‌سازد. هم‌زمان با نمونه‌گیری نظری، موردهای بعدی بر پایهٔ نیاز تحلیلی انتخاب می‌شوند و نوشتن یادداشت تحلیلی در سراسر فرایند ادامه می‌یابد تا اشباع نظری حاصل شود.",
        critiques="۱. ادعای ورود بی‌پیش‌فرض به میدان در عمل ممکن نیست و پژوهشگر همیشه با پیشینهٔ نظری وارد می‌شود. ۲. تعمیم‌پذیری آماری ندارد و اعتبار بیرونی آن محدود است. ۳. فرایند زمان‌بر و پرهزینه است. ۴. تفسیرپذیری بالا می‌تواند سوگیری پژوهشگر را پنهان کند. ۵. تفاوت نسخهٔ گلیزر و استراوس بر سر نقش پیش‌فرض و اجبار کدگذاری، خود منشأ مناقشهٔ روش‌شناختی شده است.",
        applications="مطالعهٔ تجربهٔ روزنامه‌نگاران از فشار شبکه‌های اجتماعی، پژوهش در سلامت و پرستاری، علوم تربیتی، مدیریت سازمان و هر حوزه‌ای که نیاز به فهم فرایند و معنای کنشگران دارد.",
        evolution="پس از اختلاف گلیزر و استراوس دو شاخهٔ اصلی شکل گرفت: رویکرد گلیزر با تأکید بر کدگذاری و مقایسهٔ مداوم، و رویکرد استراوس با چارچوب فرایند، زمینه و نتیجه. نسخهٔ برساخت‌گرایانه، با تأکید بر نقش فعال پژوهشگر در ساختن مقوله‌ها، و نسخهٔ پساساختارگرا نیز در دو دههٔ اخیر افزوده شده‌اند.",
        principles=["استخراج نظریه از داده", "مقایسهٔ مداوم", "نمونه‌گیری نظری", "اشباع نظری", "نوشتن یادداشت تحلیلی", "انعطاف فرایند پژوهش"],
        assumptions=["واقعیت اجتماعی از طریق تعامل و تجربهٔ افراد فهم‌پذیر است.", "نظریه باید از داده برخیزد نه بر آن تحمیل شود.", "پژوهشگر با ذهن باز وارد میدان می‌شود.", "فرایند پژوهش رفت‌وبرگشتی میان گردآوری و تحلیل است.", "معنا در بافت کنشگر ساخته می‌شود."],
        theorists="بارنی گلیزر؛ آنسلم استراوس؛ جولیت کوربین",
        theorists_text="بارنی گلیزر و آنسلم استراوس بنیان‌گذاران نظریهٔ داده‌بنیاد در ۱۹۶۷ بودند؛ استراوس با جولیت کوربین نسخهٔ رویه‌محور و کدگذاری سه‌مرحله‌ای را در ۱۹۹۰ نظام‌مند کرد و همین نسخه در پژوهش رسانه و سلامت رایج‌تر است.",
        studies=[
            "کشف نظریهٔ داده‌بنیاد (گلیزر و استراوس، ۱۹۶۷): صورت‌بندی اصلی مقایسهٔ مداوم و نمونه‌گیری نظری.",
            "مبانی پژوهش کیفی (استراوس و کوربین، ۱۹۹۰): تدوین رویه‌های کدگذاری باز، محوری و انتخابی.",
            "پژوهش‌های روزنامه‌نگاری: کدگذاری مصاحبه‌های باز و برساختن مقوله‌هایی مانند سرعت و اعتبار.",
            "مطالعات پرستاری و سلامت: تحلیل فرایند مراقبت و تجربهٔ بیماری با نمونه‌گیری نظری.",
        ],
        key_concepts=[
            {"term_fa": "کدگذاری باز", "definition": "برچسب‌گذاری داده و شکستن آن به مفاهیم اولیه."},
            {"term_fa": "کدگذاری محوری", "definition": "سازمان‌دهی مقوله‌ها حول یک مقولهٔ مرکزی و روابط میان آن‌ها."},
            {"term_fa": "کدگذاری انتخابی", "definition": "یکپارچه‌سازی مقوله‌ها در یک نظریهٔ منسجم."},
            {"term_fa": "مقایسهٔ مداوم", "definition": "مقایسهٔ پیوستهٔ داده با داده، مقوله با مقوله و نظریه با داده."},
            {"term_fa": "اشباع نظری", "definition": "نقطه‌ای که دادهٔ تازه مقوله‌های موجود را غنی نمی‌کند."},
            {"term_fa": "یادداشت تحلیلی", "definition": "ثبت اندیشه‌های تحلیلی پژوهشگر در جریان کدگذاری."},
        ],
    ),
    "card-77": dict(
        year=1953,
        mapping=METHOD_MAPPING,
        summary="روش کیو روش‌شناسی کیفی-کمّی است که استفنسون آن را در ۱۹۵۳ معرفی کرد و براون در ۱۹۸۰ برای علوم سیاسی بسط داد. مشارکت‌کنندگان مجموعه‌ای از گزاره‌ها را در توزیع اجباری رتبه‌بندی می‌کنند و تحلیل عاملی معکوس روی افراد، نه متغیرها، گروه‌های دیدگاهی مشترک را آشکار می‌سازد. روش برای مطالعهٔ ذهنیت در موضوعات حساس و پیچیده مناسب است.",
        definition="روش کیو یک روش‌شناسی مطالعهٔ ذهنیت است که افراد را در برابر مجموعهٔ ساخت‌یافته‌ای از گزاره‌ها می‌نشاند، رتبه‌بندی آن‌ها را در توزیع اجباری ثبت می‌کند و با همبستگی و تحلیل عاملی میان افراد، الگوهای دیدگاهی یا عوامل را استخراج می‌کند.",
        main_problem="چگونه می‌توان دیدگاه‌های ذهنی و ساختارهای معنایی افراد را به‌صورت سیستماتیک شناسایی، دسته‌بندی و تحلیل کرد، بدون اینکه از پیش گروه‌های دیدگاهی را تعریف کرده باشیم؟",
        mechanism="پژوهشگر نخست مجموعهٔ گزاره‌ها را از مصاحبه، رسانه و ادبیات می‌سازد تا طیف دیدگاه‌ها پوشش یابد. مشارکت‌کنندگان این گزاره‌ها را بر اساس میزان هم‌خوانی با دیدگاه خود در توزیع اجباری رتبه‌بندی می‌کنند. ماتریس رتبه‌بندی میان افراد همبسته می‌شود و تحلیل عاملی روی ستون‌ها انجام می‌گیرد. عوامل چرخش داده می‌شوند و هر عامل با آرایهٔ عاملی و گزاره‌های متمایزش تفسیر می‌گردد.",
        critiques="۱. تعداد مشارکت‌کنندگان کم است و تعمیم نتایج به جمعیت بزرگ‌تر محدود می‌ماند. ۲. انتخاب و تنظیم گزاره‌ها در مرحلهٔ مجموعهٔ گزاره‌ها نتایج را به‌شدت شکل می‌دهد. ۳. توزیع اجباری ممکن است رتبه‌بندی طبیعی افراد را محدود کند. ۴. تفسیر عوامل به داوری پژوهشگر وابسته است و سنجهٔ استانداردی برای آن وجود ندارد. ۵. تفاوت تفسیر عاملمحور و فردمحور بر سر نقش مشارکت‌کننده در تحلیل، مناقشهٔ روش‌شناختی ایجاد کرده است.",
        applications="شناسایی دیدگاه روزنامه‌نگاران دربارهٔ مرزهای اخلاقی هوش مصنوعی در تولید خبر، مطالعهٔ نگرش سیاست‌گذاران به تنظیم پلتفرم، تحلیل ذهنیت مخاطبان دربارهٔ اعتماد به رسانه، و پژوهش دربارهٔ دیدگاه‌های رقیب در موضوعات حساس.",
        evolution="روش کیو از معرفی استفنسون در ۱۹۵۳ تا نظام‌مندسازی براون در ۱۹۸۰ به‌عنوان روش مطالعهٔ ذهنیت تثبیت شد. در دهه‌های اخیر با نرم‌افزارهای تحلیل عاملی، ترکیب با مصاحبهٔ پس‌ازمرتبه‌سازی و کاربرد در پژوهش رسانهٔ دیجیتال گسترش یافته و برنامهٔ روش‌شناختی آن به مطالعهٔ گفتمان و سیاست نزدیک شده است؛ همچنین شاخص‌های جدید برازش، دقت تفسیر عوامل را افزایش داده‌اند.",
        principles=["اولویت دیدگاه فرد", "تحلیل عاملی معکوس روی افراد", "کشف الگوهای پنهان", "توزیع اجباری", "تفسیر بافتی عوامل", "مشارکت هدفمند"],
        assumptions=["دیدگاه‌های افراد ساختارمند و قابل کشف‌اند.", "افراد می‌توانند گزاره‌ها را بر پایهٔ هم‌خوانی با دیدگاه خود رتبه‌بندی کنند.", "الگوهای مشترک رتبه‌بندی نشانهٔ گروه‌های دیدگاهی‌اند.", "تحلیل عاملی روی افراد این الگوها را آشکار می‌کند."],
        theorists="ویلیام استفنسون؛ استیون براون",
        theorists_text="ویلیام استفنسون روش کیو را در ۱۹۵۳ بنیان گذاشت و آن را بر پایهٔ تحلیل عاملی معکوس صورت‌بندی کرد؛ استیون براون در ۱۹۸۰ کاربرد و رویهٔ آن را برای علوم سیاسی و اجتماعی تدوین کرد.",
        studies=[
            "مطالعهٔ رفتار (استفنسون، ۱۹۵۳): صورت‌بندی اصلی تکنیک کیو و روش‌شناسی آن.",
            "ذهنیت سیاسی (براون، ۱۹۸۰): تدوین مجموعهٔ گزاره‌ها، توزیع اجباری و تفسیر عوامل.",
            "پژوهش‌های روزنامه‌نگاری: رتبه‌بندی گزاره‌های اخلاق هوش مصنوعی و یافتن سه گروه دیدگاهی.",
            "مطالعات سیاست رسانه: تحلیل دیدگاه‌های رقیب دربارهٔ تنظیم پلتفرم‌ها.",
        ],
        key_concepts=[
            {"term_fa": "مجموعهٔ گزاره‌ها", "definition": "عباراتی که طیف دیدگاه‌های ممکن دربارهٔ یک موضوع را پوشش می‌دهند."},
            {"term_fa": "توزیع اجباری", "definition": "قالب رتبه‌بندی که تعداد گزاره‌ها در هر رتبه را محدود می‌کند."},
            {"term_fa": "آرایهٔ عاملی", "definition": "امتیاز هر گزاره در یک عامل که مبنای تفسیر دیدگاه است."},
            {"term_fa": "عامل", "definition": "الگوی مشترک رتبه‌بندی که نمایندهٔ یک دیدگاه است."},
            {"term_fa": "گزاره‌های متمایز", "definition": "گزاره‌هایی که یک عامل را از عوامل دیگر جدا می‌کنند."},
        ],
    ),
    "MTH-006": dict(
        year=2013,
        mapping={"entity_type": "METHOD", "content_type": "روش پژوهش (Method)",
                 "needs_review": False, "taxonomy_section": "5"},
        summary="تحلیل رسانهٔ دیجیتال مجموعه‌ای از روش‌های مبتنی بر دادهٔ بومی دیجیتال است که خودِ تعامل کاربران — بازنشر، جست‌وجو، پیونددهی و فراداده — را مادهٔ خام پژوهش می‌داند. ریچارد راجرز آن را بدیل روش‌شناختی علوم انسانی دیجیتال صورت‌بندی کرد: به‌جای انتقال روش‌های کهنه به وب، ابزار را از دل خود بستر می‌سازیم. این رویکرد جریان اطلاعات، ساختار پیوندها و تعامل را در مقیاس میانی می‌سنجد.",
        definition="تحلیل رسانهٔ دیجیتال شاخه‌ای از روش‌شناسی رسانه است که واحد تحلیلش کنش‌های ثبت‌شده در بسترهای دیجیتال است؛ دادهٔ آن در جریان استفاده تولید می‌شود نه در آزمایشگاه، و تحلیلش ترکیبی از سنجه‌های کمی پلتفرم و تفسیر کیفی بافت است.",
        main_problem="چگونه می‌توان جریان اطلاعات، الگوهای تعامل و ساختار قدرت پلتفرم‌ها را با داده‌هایی که خود کاربران و زیرساخت‌های دیجیتال تولید می‌کنند سنجید، بی‌آنکه پدیدهٔ ارتباطی به سنجه‌های تجاری تقلیل یابد؟",
        mechanism="فرایند سه گام دارد. نخست پژوهشگر میدان دیجیتال و واحد تحلیل را تعیین می‌کند: صفحه، هشتگ، دامنه، حساب یا فایل فراداده. دوم داده از رابط برنامه‌نویسی، خزش یا آرشیو پلتفرم گردآوری و پاک‌سازی می‌شود و متغیرهای بومی مانند زمان، زبان، نوع حساب و مسیر بازنشر استخراج می‌گردد. سوم با تحلیل شبکه، تحلیل محتوای خودکار یا مصورسازی جریان، الگوها بازسازی و در بافت اجتماعی تفسیر می‌شوند. اعتبار کار به شفافیت گردآوری، مستندسازی نسخهٔ داده و مثلث‌سازی با مصاحبه یا مشاهده وابسته است.",
        critiques="۱. دسترسی به رابط برنامه‌نویسی پلتفرم‌ها نابرابر و وابسته به سیاست تجاری است و تکرارپذیری را تهدید می‌کند. ۲. سنجه‌های پلتفرم مانند لایک و اشتراک رفتار را به شمارش تقلیل می‌دهند و معنای آن را نادیده می‌گیرند. ۳. متغیرهای جمعیت‌شناختی و رضایت آگاهانه در دادهٔ ثانویه غایب‌اند. ۴. الگوریتم نمایش خودِ داده را سوگیری‌دار می‌کند؛ آنچه دیده می‌شود محصول رتبه‌بندی است.",
        applications="رصد جریان خبر و اطلاعات نادرست در انتخابات، سنجش تعامل برندها، نقشه‌کشی کنشگری و جنبش‌های اعتراضی، تحلیل مالکیت و پیوند دامنه‌های خبری، و ارزیابی سیاست پلتفرم در قبال محتوای آسیب‌زا.",
        evolution="این حوزه از وب‌سنجی و تحلیل ابرپیوند در دههٔ ۲۰۰۰ آغاز شد، با ظهور شبکه‌های اجتماعی به تحلیل تعامل و سپس به تحلیل بستر و بررسی الگوریتم رتبه‌بندی گسترش یافت. امروز با تحلیل محاسباتی و علوم داده ادغام شده و مباحث اخلاق داده، حاکمیت پلتفرم و دادهٔ تاریک به هستهٔ آن افزوده شده است.",
        principles=["بومی بودن روش نسبت به بستر", "تقدم دادهٔ رفتاری بر اظهارنظر", "شفافیت و تکرارپذیری گردآوری", "ترکیب سنجهٔ کمی با تفسیر کیفی", "رعایت حریم خصوصی و رضایت", "توجه به نقش زیرساخت و الگوریتم"],
        assumptions=["رفتار آنلاین ردپای قابل‌اندازه‌گیری بر جای می‌گذارد.", "این ردپا نمایندهٔ کافی برای مطالعهٔ تعامل است.", "بستر دیجیتال ظرف بی‌طرف نیست و شکل داده را می‌سازد.", "دادهٔ پلتفرم به بافت اجتماعی نیاز دارد."],
        theorists="ریچارد راجرز؛ دانا بوید؛ کیت کرافورد",
        theorists_text="ریچارد راجرز برنامهٔ روش‌های دیجیتال را در ۲۰۱۳ صورت‌بندی کرد؛ دانا بوید و کیت کرافورد در ۲۰۱۲ با نقد شش‌گانهٔ کلان‌داده، مرزهای اخلاقی و روش‌شناختی این حوزه را ترسیم کردند.",
        studies=[
            "روش‌های دیجیتال (راجرز، ۲۰۱۳): چارچوب و نمونه‌های تحلیل جریان اطلاعات و پیوندها.",
            "پرسش‌های انتقادی دربارهٔ کلان‌داده (بوید و کرافورد، ۲۰۱۲): نقد بافت، نمونه‌گیری و اخلاق داده.",
            "مطالعات نقشه‌کشی موضوع: ردیابی هشتگ و جریان خبر در بحران‌ها.",
            "پژوهش تعامل برند: سنجش پاسخ مخاطب در شبکه‌های اجتماعی.",
        ],
        key_concepts=[
            {"term_fa": "دادهٔ بومی دیجیتال", "definition": "داده‌ای که در خود بستر دیجیتال و به‌صورت طبیعی تولید شده است."},
            {"term_fa": "نقشه‌کشی موضوع", "definition": "بازسازی چیدمان بازیگران و گزاره‌ها حول یک مسئله در وب."},
            {"term_fa": "تحلیل ابرپیوند", "definition": "بررسی الگوی پیوند میان دامنه‌ها و منابع."},
            {"term_fa": "تحلیل تعامل", "definition": "سنجش بازنشر، پاسخ و مشارکت کاربران."},
            {"term_fa": "دادهٔ تاریک", "definition": "داده‌ای که پلتفرم عرضه نمی‌کند و دسترسی به آن محدود است."},
        ],
        detailed_analysis="تحلیل رسانهٔ دیجیتال از بستر بومی دیجیتال داده می‌گیرد؛ یعنی خودِ فعالیت آنلاین (بازنشر، کامنت، کلیک) ردپای قابل‌سنجی می‌گذارد. این امر پژوهش را از مشاهدهٔ نادرست به سنجش رفتار واقعی نزدیک می‌کند. چالش اصلی این حوزه اخلاقی و تفسیری است: حریم خصوصی داده، شفافیت محدود الگوریتم‌های پلتفرم، و خطر تقلیل تجربهٔ انسانی به ردپای عددی. به همین دلیل بهترین کار ترکیب دادهٔ کمّی دیجیتال با فهم کیفی (مصاحبه، مشاهده، تحلیل بافت) است. تفاوت آن با تحلیل محاسباتی در جهت پرسش است: تحلیل رسانهٔ دیجیتال از بستر و تعامل آغاز می‌شود، در حالی که تحلیل محاسباتی از مدل و الگوریتم.",
    ),
    "MTH-007": dict(
        year=2009,
        mapping={"entity_type": "METHOD", "content_type": "روش پژوهش (Method)",
                 "needs_review": False, "taxonomy_section": "5"},
        summary="تحلیل محاسباتی به کاربرد روش‌های خودکار پردازش زبان، یادگیری ماشین و مدل‌سازی آماری برای خوانش حجم‌های عظیم متن و رسانه گفته می‌شود. این رویکرد در دههٔ ۲۰۰۰ با علوم اجتماعی محاسباتی پا گرفت و اکنون ستون فقرات مطالعات کلان‌داده، تحلیل احساسات و رصد اطلاعات نادرست است. وعدهٔ آن مقیاس است و خطر اصلی‌اش جابه‌جایی اعتبار معنایی با دقت آماری.",
        definition="تحلیل محاسباتی مجموعه‌ای از تکنیک‌های الگوریتمی است که متن، تصویر یا شبکه را به بازنمایی عددی تبدیل و با مدل آماری یا یادگیری ماشین الگوهای آن را استخراج می‌کند؛ خروجی معمولاً طبقه‌بندی، خوشه‌بندی، پیش‌بینی یا رتبه‌بندی است.",
        main_problem="چگونه می‌توان الگوهای معنایی، احساسی و گفتمانی را در پیکره‌هایی که از توان خوانش دستی بسیار فراترند شناسایی کرد و در همان حال اعتبار، شفافیت و عدالت الگوریتمی را حفظ نمود؟",
        mechanism="چرخهٔ کار با تعریف پیکره و پرسش آغاز می‌شود: کدام متن‌ها، در چه بازهٔ زمانی و با چه معیار ورودی. سپس متن پیش‌پردازش می‌شود: نرمال‌سازی، قطعه‌بندی، حذف ایست‌واژه و برچسب‌زنی نحوی. در گام بعد بازنمایی عددی ساخته می‌شود؛ کیسهٔ واژه، جای‌گذاری برداری یا مدل زبانی از جملهٔ آن‌اند. مدل با نمونهٔ برچسب‌خورده آموزش می‌بیند و با سنجه‌هایی مانند دقت، فراخوانی و ضریب توافق ارزیابی می‌شود. سرانجام خروجی در بافت تفسیر و در صورت امکان با داوری انسانی راستی‌آزمایی می‌گردد.",
        critiques="۱. اعتبار سازه: هم‌خوانی واژگانی معنا نیست و مدل ممکن است طنز، کنایه یا بافت را از دست بدهد. ۲. سوگیری دادهٔ آموزشی: پیکره‌های عمومی صدای گروه‌های حاشیه‌ای را کم‌شنیده می‌کنند. ۳. جعبهٔ سیاه: تفسیرپذیری محدود، پاسخ‌گویی پژوهش را دشوار می‌کند. ۴. نبود کد و نسخهٔ مدل، بازتولید نتیجه را ناممکن می‌سازد. ۵. خطای اندازه‌گیری به‌صورت قطعیت عددی پنهان می‌شود.",
        applications="تحلیل احساسات در شبکه‌های اجتماعی، طبقه‌بندی خودکار موضوع و چارچوب‌بندی خبر، شناسایی هماهنگی و رفتار غیرانسانی، ردیابی اطلاعات نادرست، و تحلیل کلان گفتمان در پیکره‌های تاریخی و حقوقی.",
        evolution="لازر و همکاران در ۲۰۰۹ با فراخوان علوم اجتماعی محاسباتی این چرخش را اعلام کردند. مسیر پس از آن از مدل‌های واژه‌محور به جای‌گذاری برداری و سپس مدل‌های زبانی بزرگ رفت؛ هم‌زمان نقد اخلاقی و روش‌شناختی کلان‌داده رشد کرد و امروز ارزیابی انسانی، مستندسازی مدل و عدالت الگوریتمی بخشی از استاندارد کار شده است.",
        principles=["پرسش نظری پیش از ابزار", "شفافیت پیکره و کد", "اعتبارسنجی با داوری انسانی", "توجه به سوگیری و عدالت", "تفسیرپذیری به‌اندازهٔ نیاز", "بازتولیدپذیری و مستندسازی نسخه"],
        assumptions=["معنا و الگو به‌صورت کمّی از داده قابل استخراج‌اند.", "نمونهٔ آموزشی نمایندهٔ جامعهٔ هدف است.", "خطای مدل قابل سنجش و مهار است.", "الگوریتم ابزار بی‌طرف نیست."],
        theorists="دیوید لازر؛ دانا بوید؛ کیت کرافورد",
        theorists_text="دیوید لازر و همکارانش در ۲۰۰۹ چارچوب علوم اجتماعی محاسباتی را ترسیم کردند؛ دانا بوید و کیت کرافورد در ۲۰۱۲ با شش پرسش انتقادی، محدودیت‌های اعتبار و اخلاق این تحلیل را صورت‌بندی کردند.",
        studies=[
            "علوم اجتماعی محاسباتی (لازر و همکاران، ۲۰۰۹): فراخوان گردآوری و تحلیل دادهٔ دیجیتال در مقیاس بزرگ.",
            "پرسش‌های انتقادی دربارهٔ کلان‌داده (بوید و کرافورد، ۲۰۱۲): نقد قشربندی دسترسی، بافت و اخلاق.",
            "مطالعات تحلیل احساسات: سنجش لحن عمومی در بحران‌ها و انتخابات.",
            "پژوهش اطلاعات نادرست: شناسایی الگوهای هماهنگ انتشار محتوا.",
        ],
        key_concepts=[
            {"term_fa": "پردازش زبان طبیعی", "definition": "تحلیل و فهم زبان انسانی با الگوریتم."},
            {"term_fa": "یادگیری ماشین", "definition": "کشف الگو و پیش‌بینی از داده با مدل آماری."},
            {"term_fa": "تحلیل احساسات", "definition": "سنجش لحن و بار عاطفی متن."},
            {"term_fa": "جای‌گذاری برداری", "definition": "بازنمایی معنای واژه و متن به‌صورت بردار عددی."},
            {"term_fa": "جعبهٔ سیاه", "definition": "مدلی که منطق درونی تصمیم‌گیری‌اش برای پژوهشگر روشن نیست."},
        ],
        detailed_analysis="تحلیل محاسباتی چرخش محاسباتی علوم انسانی را نمایندگی می‌کند: به‌جای خوانش دستی، الگوریتم‌ها حجم‌های عظیم متن را می‌خوانند. پردازش زبان طبیعی و یادگیری ماشین ابزار اصلی‌اند و تحلیل احساسات یک کاربرد پرکاربرد است. قدرت این روش در مقیاس‌پذیری است، اما دو چالش جدی دارد: نخست اعتبار و روایی مدل (آیا الگوریتم واقعاً معنا را می‌فهمد یا فقط هم‌خوانی کلمات را می‌سنجد؟) و دوم سوگیری داده و الگوریتم که می‌تواند نتایج را نظام‌مندانه به سمت گروه‌های پرسروصداتر ببرد. پاسخ روش‌شناختی، ترکیب سنجهٔ خودکار با نمونه‌گیری دستی، گزارش شفاف خطا و مستندسازی نسخهٔ مدل است.",
    ),
}

NAME_FIX = {}
YEAR_FIX = {
    "card-71": "no year change; the placeholder QA-note summary was replaced with a sourced summary; anchors: Glaser & Strauss (1967) and Strauss & Corbin (1990)",
    "card-77": "no year change; the placeholder QA-note summary was replaced with a sourced summary; anchors: Stephenson (1953) and Brown (1980)",
    "MTH-006": "year set from empty to 2013; anchor: Rogers, Digital Methods (MIT Press, 2013); the existing detailed_analysis was retained with its correct content",
    "MTH-007": "year set from empty to 2009; anchor: Lazer et al., Computational Social Science (Science, 2009)",
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
                                       "verified": n_verified, "batch": 192}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH192 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
