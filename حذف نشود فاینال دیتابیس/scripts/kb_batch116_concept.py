# -*- coding: utf-8 -*-
"""Batch 116 (CONCEPT): full documentation for MC-054, MC-057, MC-249, MC-412."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch116-concept-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch116_concept.json"

S = {
    "MC-054": [
        dict(kind="BOOK",
             title_en="On Liberty",
             title_fa="درباره آزادی",
             authors="Mill, J. S.", year=1859,
             publisher="John W. Parker and Son",
             doi=None,
             url="https://books.google.com/books/about/On_Liberty.html?id=3xARAAAAYAAJ",
             language="en", isbn=None,
             citation="Mill, J. S. (1859). On liberty. John W. Parker and Son.",
             locator="work", locator_type="work",
             supports="the harm principle as the limit of legitimate power over the individual", verified=True),
        dict(kind="BOOK",
             title_en="Harm to Others: The Moral Limits of the Criminal Law",
             title_fa="آسیب به دیگران: محدودیت‌های اخلاقی حقوق کیفری",
             authors="Feinberg, J.", year=1984,
             publisher="Oxford University Press",
             doi=None, url=None, language="en", isbn=None,
             citation="Feinberg, J. (1984). Harm to others: The moral limits of the criminal law. Oxford University Press.",
             locator="work", locator_type="work",
             supports="analytic clarification of harm versus offense", verified=False),
    ],
    "MC-057": [
        dict(kind="BOOK",
             title_en="SLAPPs: Getting Sued for Speaking Out",
             title_fa="اسلپ‌ها: شکایت‌شدن برای سکوت",
             authors="Pring, G. W.; Canan, P.", year=1996,
             publisher="Temple University Press",
             doi=None,
             url="https://tupress.temple.edu/books/slapps",
             language="en", isbn=None,
             citation="Pring, G. W., & Canan, P. (1996). SLAPPs: Getting sued for speaking out. Temple University Press.",
             locator="work", locator_type="work",
             supports="definition and empirical study of strategic lawsuits against public participation", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Studying Strategic Litigation Against Public Participation: A Research Agenda",
             title_fa="مطالعه دعاوی راهبردی علیه مشارکت عمومی: یک دستور کار پژوهشی",
             authors="Canan, P.; Pring, G. W.", year=1988,
             publisher="Law & Social Inquiry",
             doi=None, url=None, language="en", isbn=None,
             citation="Canan, P., & Pring, G. W. (1988). Studying strategic litigation against public participation: A research agenda. Law & Social Inquiry, 13(2), 385-406.",
             locator="13(2):385-406", locator_type="page_range",
             supports="early research agenda defining SLAPP as litigation aimed at silencing participation", verified=False),
    ],
    "MC-249": [
        dict(kind="BOOK",
             title_en="The Media Equation: How People Treat Computers, Television, and New Media Like Real People and Places",
             title_fa="معادله رسانه: چگونه مردم با رایانه، تلویزیون و رسانه نو مانند انسان و مکان واقعی رفتار می‌کنند",
             authors="Reeves, B.; Nass, C.", year=1996,
             publisher="Cambridge University Press",
             doi=None,
             url="https://archive.org/details/mediaequationhow0000reev",
             language="en", isbn=None,
             citation="Reeves, B., & Nass, C. (1996). The media equation: How people treat computers, television, and new media like real people and places. Cambridge University Press.",
             locator="work", locator_type="work",
             supports="people apply social rules and expectations to media and computers", verified=True),
        dict(kind="BOOK_CHAPTER",
             title_en="Computers Are Social Actors",
             title_fa="رایانه‌ها کنشگران اجتماعی‌اند",
             authors="Nass, C.; Steuer, J.; Tauber, E. R.", year=1994,
             publisher="ACM",
             doi=None, url=None, language="en", isbn=None,
             citation="Nass, C., Steuer, J., & Tauber, E. R. (1994). Computers are social actors. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (pp. 72-78). ACM.",
             locator="pp. 72-78", locator_type="page_range",
             supports="experimental evidence for social responses to computers", verified=False),
    ],
    "MC-412": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Perceived Usefulness, Perceived Ease of Use, and User Acceptance of Information Technology",
             title_fa="سودمندی ادراک‌شده، سهولت استفاده ادراک‌شده و پذیرش فناوری اطلاعات توسط کاربر",
             authors="Davis, F. D.", year=1989,
             publisher="MIS Quarterly",
             doi="10.2307/249008",
             url="https://misq.umn.edu/misq/article/13/3/319/191/Perceived-Usefulness-Perceived-Ease-of-Use-and",
             language="en", isbn=None,
             citation="Davis, F. D. (1989). Perceived usefulness, perceived ease of use, and user acceptance of information technology. MIS Quarterly, 13(3), 319-340.",
             locator="13(3):319-340", locator_type="page_range",
             supports="perceived usefulness and ease of use predict intention to use technology", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="A Theoretical Extension of the Technology Acceptance Model: Four Longitudinal Field Studies",
             title_fa="گسترش نظری مدل پذیرش فناوری: چهار مطالعه میدانی طولی",
             authors="Venkatesh, V.; Davis, F. D.", year=2000,
             publisher="Management Science",
             doi=None, url=None, language="en", isbn=None,
             citation="Venkatesh, V., & Davis, F. D. (2000). A theoretical extension of the technology acceptance model: Four longitudinal field studies. Management Science, 46(2), 186-204.",
             locator="46(2):186-204", locator_type="page_range",
             supports="extension of the model with subjective norm and image", verified=False),
    ],
}

ENRICH = {
    "MC-054": {
        "summary": "اصل آسیب، که جان استوارت میل آن را در ۱۸۵۹ در رساله درباره آزادی صورت‌بندی کرد، مرز مشروع قدرت اجتماعی بر فرد را تعیین می‌کند: تنها دلیلی که می‌تواند اعمال قدرت بر عضوی از جامعه متمدن را در برابر خواست او توجیه کند، جلوگیری از آسیب به دیگران است. خیر خود فرد، جسمی یا اخلاقی، دلیل کافی نیست. میل این اصل را به آزادی بیان نیز گسترد: سکوت یک عقیده، فرض خطاناپذیری است؛ عقیده نادرست نیز ممکن است بخشی از حقیقت را در خود داشته باشد و برخورد آزاد عقاید، بهترین راه نزدیک‌شدن به حقیقت است. در این چارچوب، تفکیک آسیب از رنجش اهمیت دارد: رفتار نامطلوب یا آزاردهنده، به‌تنهایی مجوز سرکوب نیست. اصل آسیب در حقوق رسانه به بحث درباره هتک حرمت، نفرت‌پراکنی و محتوای زیان‌بار راه یافته و پرسش اصلی آن است که چه زیانی به دیگران، و با چه آستانه‌ای، مداخله را مجاز می‌کند. اهمیت معاصر آن در تعادل میان آزادی بیان و حفاظت از گروه‌های آسیب‌پذیر است.",
        "definition": "اصل آسیب، معیاری هنجاری است که مداخله قانونی یا اجتماعی در آزادی فرد را تنها زمانی مجاز می‌داند که رفتار او به دیگران آسیب برساند، نه صرفاً به سبب ناپسند بودن یا زیان به خود.",
        "main_problem": "مسئله این است که جامعه تا کجا می‌تواند آزادی فرد را محدود کند. پاسخ میل، آسیب به دیگران است. پرسش دوم، مرز است: چه چیزی آسیب است و چه چیزی تنها رنجش یا ناخوشایند بودن.",
        "mechanism": "۱. تفکیک قلمرو: رفتار خودمربوط از رفتار دیگرمربوط جدا می‌شود.\n۲. معیار مداخله: تنها آسیب به دیگران مجوز محدودیت است.\n۳. بار اثبات: مداخله‌کننده باید زیان را نشان دهد.\n۴. آزادی بیان: سکوت عقیده، ادعای خطاناپذیری است.\n۵. تبادل عقاید: برخورد آزاد دیدگاه‌ها، حقیقت را تصحیح می‌کند.\n۶. آستانه: رنجش و ناپسندی، به‌تنهایی آسیب نیست.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا هتک حرمت نیازمند اثبات زیان است، چرا نفرت‌پراکنی گاه در چارچوب آسیب به گروه تحلیل می‌شود و چرا سانسور پیشگیرانه با بار اثبات سنگین روبه‌روست. نکته مهم این است که اصل آسیب، آزادی مطلق نمی‌سازد؛ بلکه توزیع بار دلیل را روشن می‌کند؛ از این رو، در سیاست‌گذاری محتوای شبکه اجتماعی، پرسش درست این است که زیان چه کسی، با چه شواهدی و با چه حداقلی از مداخله اثبات می‌شود.",
        "assumptions": [
            "فرد، بهترین داور خیر خود است.",
            "مداخله نیازمند دلیل بیرونی است.",
            "آسیب به دیگران، مرز آزادی است.",
        ],
        "principles": [
            "خیر فرد، دلیل مداخله نیست.",
            "بار اثبات بر دوش مداخله‌کننده است.",
            "سکوت عقیده، ادعای خطاناپذیری است.",
        ],
        "critiques": [
            "۱. ابهام: مفهوم آسیب تعریف یکدست ندارد.\n۲. جمعی: زیان‌های تجمعی مانند اطلاعات نادرست کم دیده می‌شوند.\n۳. قدرت: تعریف آسیب گاه منافع گروه غالب را بازتولید می‌کند.\n۴. فرهنگ: آستانه رنجش میان جوامع متفاوت است.\n۵. مثبت: آزادی بدون توان مادی، آزادی صوری می‌ماند.",
        ],
        "applications": [
            "حقوق رسانه: سنجش زیان در هتک حرمت.",
            "سیاست محتوا: آستانه مداخله پلتفرم.",
            "اخلاق روزنامه‌نگاری: تفکیک رنجش و آسیب.",
            "آموزش حقوق: بار اثبات محدودیت بیان.",
        ],
        "evolution": "میل در ۱۸۵۹ اصل آسیب را صورت‌بندی کرد، فاینبرگ در ۱۹۸۴ تحلیل مفهومی آسیب و رنجش را گسترد و حقوق رسانه معاصر آن را به بحث نفرت‌پراکنی و اطلاعات نادرست پیوند زد.",
        "key_concepts": [
            "اصل آسیب (Harm Principle)",
            "خودمربوط (Self-Regarding)",
            "دیگرمربوط (Other-Regarding)",
            "آسیب و رنجش (Harm and Offense)",
            "خطاناپذیری (Infallibility)",
            "بازار عقاید (Marketplace of Ideas)",
        ],
        "studies": [
            "Mill, J. S. (1859). On liberty. John W. Parker and Son.",
            "Feinberg, J. (1984). Harm to others. Oxford University Press.",
        ],
        "theorists": "جان استوارت میل؛ جوئل فاینبرگ",
        "theorists_text": "میل (۱۸۵۹)؛ فاینبرگ (۱۹۸۴)",
        "year": 1859,
        "model": "رفتار خواص → آزمون آسیب به دیگران → مجاز یا ممنوع بودن مداخله.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nمیل اصل آسیب را در سنت لیبرالی و در برابر قیم‌مآبی اخلاقی و اجتماعی صورتبندی کرد. نوآوری آن، جابه‌جایی بار دلیل از آزادی‌خواه به مداخله‌کننده است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با تحلیل حقوقی و داوری هنجاری انجام می‌شود. تحلیلی که هر ناخوشایندی را آسیب می‌خواند، اصل را تهی می‌کند؛ و تحلیلی که تنها آسیب جسمی را می‌پذیرد، زیان‌های اجتماعی را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در محدودسازی سانسور است، اما باید با تحلیل قدرت و نابرابری تکمیل شود. آزادی بی توان، به آزادی صوری بدل می‌شود.",
        "critique_text": "\n".join([
            "۱. ابهام: آسیب تعریف یکدست ندارد.",
            "۲. جمعی: زیان تجمعی کم دیده می‌شود.",
            "۳. قدرت: تعریف آسیب جانبدارانه است.",
            "۴. فرهنگ: آستانه رنجش متفاوت است.",
            "۵. مثبت: آزادی بدون توان، صوری است.",
        ]),
        "example_text": "انتشار یک ادعای نادرست درباره سلامت، تنها یک نظر نامطلوب نیست؛ اگر زیان قابل اثبات به دیگران بسازد، اصل آسیب مداخله را مجاز می‌داند.",
    },
    "MC-057": {
        "summary": "دعاوی راهبردی علیه مشارکت عمومی، که پرینگ و کانان در ۱۹۹۶ آن را با عنوان اسلپ صورت‌بندی کردند، شکایت‌هایی‌اند که هدف اصلی آن‌ها نه پیروزی در دادگاه، بلکه خاموش‌کردن بیان سیاسی شهروندان است. سازوکار چنین نیست که ادعا همیشه باطل باشد؛ کافی است شکایت، هزینه، زمان و فشار روانی ایجاد کند تا شهروند از پیگیری موضوع دست بکشد. ویژگی‌های رایج عبارت‌اند از: ادعای بی‌پایه یا نامتناسب، هدف‌گرفتن ارتباط با نهادهای عمومی، شکایت از سوی بازیگر قدرتمند اقتصادی و اثر بازدارنده بر دیگران. در حوزه رسانه، خبرنگاران محیط‌زیست، افشاگران و رسانه‌های محلی بیش از همه در معرض‌اند. قوانین ضد اسلپ، مانند قانون کالیفرنیا در ۱۹۹۲، سازوکار توقف سریع دعاوی بی‌پایه و جبران هزینه را ساخته‌اند. نظریه توضیح می‌دهد چرا آزادی بیان تنها با نبود سانسور رسمی تأمین نمی‌شود و هزینه دادرسی نیز ابزار سرکوب است. اهمیت عملی آن، سنجش اثر بازدارنده و طراحی حمایت حقوقی است.",
        "definition": "اسلپ، شکایت راهبردی است که با ادعای حقوقی، معمولاً بی‌پایه یا نامتناسب، علیه بیان عمومی شهروندان اقامه می‌شود تا با تحمیل هزینه و فشار، مشارکت عمومی را خاموش کند.",
        "main_problem": "مسئله این است که چرا بیان آزاد، بی سانسور رسمی نیز خاموش می‌شود. پاسخ، هزینه راهبردی دعاوی است. پرسش دوم، درمان است: چگونه می‌توان دعاوی بی‌پایه را بی آنکه دسترسی به دادگاه محدود شود، سریع متوقف کرد.",
        "mechanism": "۱. هدف‌گیری بیان: شکایت علیه اظهارنظر عمومی یا شکایت به نهاد هدایت می‌شود.\n۲. ادعای نامتناسب: مبلغ خواسته یا دامنه ادعا از زیان واقعی فراتر می‌رود.\n۳. فشار هزینه: هزینه وکالت و زمان، شهروند را از پیگیری بازمی‌دارد.\n۴. کشف و اطاله: رویه دادرسی به ابزار فشار بدل می‌شود.\n۵. اثر بازدارنده: دیگران نیز از بیان خودداری می‌کنند.\n۶. پاسخ قانونی: سازوکار ضد اسلپ، توقف سریع و جبران هزینه می‌سازد.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا گزارش‌های محلی درباره پروژه‌های عمرانی با شکایت روبه‌رو می‌شوند، چرا روزنامه کوچک پیش از انتشار، هزینه حقوقی را می‌سنجد و چرا سکوت خبری گاه نتیجه ترس است نه بی‌اهمیتی. نکته مهم این است که اسلپ در ظاهر دعوای حقوقی است و در عمل ابزار سیاسی؛ از این رو، سنجش آن نیازمند داده درباره الگوی شکایت، نتیجه و اثر بازدارنده است، نه فقط شمار پرونده‌ها.",
        "assumptions": [
            "دسترسی به دادگاه می‌تواند ابزار سرکوب باشد.",
            "هزینه دادرسی بر بیان اثر بازدارنده دارد.",
            "ادعای حقوقی می‌تواند بی نیاز از پیروزی مؤثر باشد.",
        ],
        "principles": [
            "هدف شکایت، خاموش‌سازی است نه جبران.",
            "بی‌پایگی ادعا، معیار اصلی تشخیص است.",
            "حمایت قانونی باید سریع و کم‌هزینه باشد.",
        ],
        "critiques": [
            "۱. تشخیص: تفکیک اسلپ از دعوای مشروع دشوار است.\n۲. سنجش: اثر بازدارنده به‌سختی اندازه‌گیری می‌شود.\n۳. تعمیم: الگوی شکایت در نظام‌های حقوقی متفاوت است.\n۴. قدرت: شرکت‌های بزرگ، دسترسی حقوقی نابرابر دارند.\n۵. تعادل: حمایت افراطی می‌تواند حق دادخواهی زیان‌دیده را محدود کند.",
        ],
        "applications": [
            "حقوق رسانه: سازوکار توقف سریع دعاوی بی‌پایه.",
            "روزنامه‌نگاری تحقیقی: بیمه و پشتیبانی حقوقی.",
            "سیاست عمومی: ثبت و پایش الگوی شکایت.",
            "آموزش شهروندی: شناخت حق دادخواهی و خطر آن.",
        ],
        "evolution": "کانان و پرینگ در ۱۹۸۸ دستور کار پژوهش را نوشتند و در ۱۹۹۶ مطالعه جامع اسلپ را منتشر کردند. قوانین ضد اسلپ از دهه ۱۹۹۰ گسترش یافت و اتحادیه اروپا در دهه ۲۰۲۰ چارچوب حمایتی تازه‌ای افزود.",
        "key_concepts": [
            "اسلپ (SLAPP)",
            "مشارکت عمومی (Public Participation)",
            "اثر بازدارنده (Chilling Effect)",
            "ادعای بی‌پایه (Meritless Claim)",
            "قانون ضد اسلپ (Anti-SLAPP Statute)",
            "هزینه دادرسی (Litigation Cost)",
        ],
        "studies": [
            "Pring, G. W., & Canan, P. (1996). SLAPPs: Getting sued for speaking out. Temple University Press.",
            "Canan, P., & Pring, G. W. (1988). Studying strategic litigation against public participation. Law & Social Inquiry, 13(2), 385-406.",
        ],
        "theorists": "جورج پرینگ؛ پنه‌لوپه کانان",
        "theorists_text": "پرینگ و کانان (۱۹۸۸، ۱۹۹۶)",
        "year": 1996,
        "model": "بیان عمومی → شکایت نامتناسب → فشار هزینه → سکوت شهروند → اثر بازدارنده گسترده.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nپرینگ و کانان اسلپ را در تقاطع حقوق و مشارکت مدنی مطالعه کردند. نوآوری چارچوب، دیدن شکایت به‌عنوان ابزار ارتباطی و سیاسی است، نه فقط اختلاف حقوقی.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با تحلیل پرونده، مصاحبه با قربانیان و پیمایش خبرنگاران انجام می‌شود. پژوهشی که تنها نتیجه پرونده را می‌خواند، اثر بازدارنده را از دست می‌دهد؛ و پژوهشی که هر شکایت علیه رسانه را اسلپ می‌خواند، دعاوی مشروع را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در تحلیل سانسور غیررسمی است، اما باید با داده دادگاه تکمیل شود. حمایت بی معیار، حق دادخواهی را تضعیف می‌کند.",
        "critique_text": "\n".join([
            "۱. تشخیص: تفکیک از دعوای مشروع دشوار است.",
            "۲. سنجش: اثر بازدارنده سخت اندازه‌پذیر است.",
            "۳. تعمیم: نظام‌های حقوقی متفاوت‌اند.",
            "۴. قدرت: دسترسی حقوقی نابرابر است.",
            "۵. تعادل: حق دادخواهی زیان‌دیده محدود می‌شود.",
        ]),
        "example_text": "شهروندی که در جلسه شورای شهر از آلودگی یک کارخانه سخن می‌گوید، با شکایت سنگین حقوقی روبه‌رو می‌شود؛ پیشنهاد سازش با سکوت، هدف واقعی شکایت را آشکار می‌کند.",
    },
    "MC-249": {
        "summary": "معادله رسانه و پارادایم رایانه به‌مثابه کنشگر اجتماعی، که ریوز و نس آن را در دهه ۱۹۹۰ صورت‌بندی کردند، می‌گوید مردم با رسانه‌ها همان‌گونه رفتار می‌کنند که با انسان و مکان واقعی رفتار می‌کنند. ریوز و نس نشان دادند پاسخ‌های اجتماعی به رایانه، تلویزیون و رسانه نو، تنها استعاره یا خطای زبانی نیست؛ افراد در آزمایش‌ها ادب، تقابل، کلیشه جنسیتی و هویت نقش را به ماشین نسبت می‌دهند. پارادایم رایانه به‌مثابه کنشگر اجتماعی، شرط‌های این پاسخ را مشخص می‌کند: استفاده از زبان طبیعی، پاسخ‌گویی به ورودی، پرکردن نقش اجتماعی و تعامل پیوسته. این چارچوب به طراحی رابط، عامل‌های گفت‌وگویی و شخصیت‌سازی برند رسانه‌ای راه یافته است. نظریه توضیح می‌دهد چرا کاربر به دستیار صوتی سلام می‌کند، چرا رابط بی ادب، بی‌احترامی تلقی می‌شود و چرا اعتماد به ماشین با اعتماد به انسان سنجیده می‌شود. اهمیت آن، پیوند طراحی فنی با هنجار اجتماعی است.",
        "definition": "معادله رسانه، فرضیه‌ای است که پاسخ‌های اجتماعی افراد به رسانه و رایانه را با پاسخ به انسان و مکان واقعی قابل قیاس می‌داند و طراحی رابط را به هنجارهای تعامل انسانی گره می‌زند.",
        "main_problem": "مسئله این است که چرا کاربران با ماشین، رفتار اجتماعی و اخلاقی دارند. پاسخ، فعال‌شدن قواعد تعامل انسانی است. پرسش دوم، طراحی است: کدام ویژگی رابط، پاسخ اجتماعی را برمی‌انگیزد و کدام ویژگی آن را خنثی می‌کند.",
        "mechanism": "۱. نشانه اجتماعی: زبان طبیعی و پاسخ‌گویی، ماشین را کنشگر می‌سازد.\n۲. فعال‌سازی قاعده: ذهن، قواعد تعامل انسانی را به کار می‌گیرد.\n۳. نقش اجتماعی: ماشین در نقش معلم، همکار یا مشاور پذیرفته می‌شود.\n۴. ادب و تقابل: کاربر به ماشین ادب می‌کند و توهین را پاسخ می‌دهد.\n۵. هویت: جنسیت و شخصیت صدا، ارزیابی را تغییر می‌دهد.\n۶. تعمیم: اثر به تلویزیون، بازی و رسانه نو گسترش می‌یابد.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا دستیار صوتی با صدای انسانی پذیرفته‌تر است، چرا ربات خبری بی ادب اعتماد را از دست می‌دهد و چرا شخصیت‌سازی برند به رابطه پاراسوشیال می‌انجامد. نکته مهم این است که پاسخ اجتماعی، باور به هوشمندی نیست؛ کاربر می‌داند ماشین انسان نیست، اما قواعد تعامل را ناگزیر به کار می‌گیرد؛ از این رو، طراحی اخلاقی رابط باید این پاسخ ناخودآگاه را جدی بگیرد.",
        "assumptions": [
            "ذهن، قواعد تعامل انسانی را خودکار فعال می‌کند.",
            "نشانه اجتماعی، ماشین را کنشگر می‌سازد.",
            "پاسخ اجتماعی به آگاهی از ماشین بودن وابسته نیست.",
        ],
        "principles": [
            "رابط، رابطه اجتماعی می‌سازد.",
            "ادب و بی‌ادبی ماشین، معنا دارد.",
            "طراحی باید هنجار تعامل را جدی بگیرد.",
        ],
        "critiques": [
            "۱. تکرارپذیری: برخی آزمون‌ها در بازآزمایی تأیید نشدند.\n۲. اندازه اثر: اثرها اغلب کوچک‌اند.\n۳. زمینه: یافته‌ها بیشتر آزمایشگاهی و غربی‌اند.\n۴. فناوری: رابط امروز، انتظارات تازه ساخته است.\n۵. اخلاق: انسان‌انگاری طراحی‌شده می‌تواند فریبنده باشد.",
        ],
        "applications": [
            "طراحی رابط: شخصیت و لحن دستیار.",
            "رسانه خبری: ربات گفت‌وگو و اعتماد.",
            "بازاریابی: شخصیت برند رسانه‌ای.",
            "اخلاق فناوری: شفافیت در انسان‌انگاری.",
        ],
        "evolution": "نس و همکاران در ۱۹۹۴ پاسخ‌های اجتماعی به رایانه را آزمودند و ریوز و نس در ۱۹۹۶ چارچوب معادله رسانه را منتشر کردند. پژوهش عامل‌های گفت‌وگویی، آن را به تعامل روزمره گسترد.",
        "key_concepts": [
            "معادله رسانه (Media Equation)",
            "کنشگر اجتماعی (Social Actor)",
            "نشانه اجتماعی (Social Cue)",
            "انسان‌انگاری (Anthropomorphism)",
            "حضور اجتماعی (Social Presence)",
            "رابط گفت‌وگویی (Conversational Interface)",
        ],
        "studies": [
            "Reeves, B., & Nass, C. (1996). The media equation. Cambridge University Press.",
            "Nass, C., Steuer, J., & Tauber, E. R. (1994). Computers are social actors. In Proceedings of CHI 1994 (pp. 72-78). ACM.",
        ],
        "theorists": "بایرون ریوز؛ کلیفورد نس؛ جاناتان استویر؛ الن تابر",
        "theorists_text": "نس و همکاران (۱۹۹۴)؛ ریوز و نس (۱۹۹۶)",
        "year": 1994,
        "model": "نشانه اجتماعی → فعال‌شدن قاعده تعامل → نسبت نقش و هویت → پاسخ اجتماعی به رسانه.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nریوز و نس از روان‌شناسی اجتماعی و تعامل انسان و رایانه بهره گرفتند. نوآوری چارچوب، رد تفکیک مطلق انسان و ماشین در تجربه کاربر است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با آزمایش کنترل‌شده و مقیاس نگرش انجام می‌شود. پژوهشی که تنها نگرش صریح را می‌سنجد، پاسخ خودکار را از دست می‌دهد؛ و پژوهشی که هر رفتار مؤدبانه را پاسخ اجتماعی می‌خواند، هنجار موقعیتی را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در طراحی رابط است، اما باید با پژوهش میدانی تکمیل شود. انسان‌انگاری بی شفافیت، به فریب کاربر بدل می‌شود.",
        "critique_text": "\n".join([
            "۱. تکرارپذیری: برخی آزمون‌ها بازتولید نشدند.",
            "۲. اندازه اثر: اثرها کوچک‌اند.",
            "۳. زمینه: یافته‌ها آزمایشگاهی‌اند.",
            "۴. فناوری: انتظارات تازه شده است.",
            "۵. اخلاق: انسان‌انگاری فریبنده است.",
        ]),
        "example_text": "کاربری که به دستیار صوتی «لطفاً» می‌گوید و از پاسخ سرد آن آزرده می‌شود، با ماشین مانند یک همکار رفتار می‌کند؛ معادله رسانه در عمل رخ داده است.",
    },
    "MC-412": {
        "summary": "مدل پذیرش فناوری، که دیویس آن را در ۱۹۸۹ عرضه کرد، می‌کوشد توضیح دهد چرا کاربران فناوری اطلاعات را می‌پذیرند یا رد می‌کنند. دو سازه اصلی مدل، سودمندی ادراک‌شده و سهولت استفاده ادراک‌شده است: کاربر فناوری را می‌پذیرد اگر آن را برای عملکرد شغلی سودمند بداند و اگر کار با آن را دشوار نبیند. دیویس نشان داد سهولت ادراک‌شده بر سودمندی اثر می‌گذارد و هر دو بر نگرش و قصد استفاده. مدل بر نظریه کنش منطقی و رفتار برنامه‌ریزی‌شده تکیه دارد و نسخه‌های بعدی، هنجار ذهنی، تصویر اجتماعی و شرایط تسهیل‌کننده را افزودند. در پژوهش رسانه، مدل برای پذیرش اپلیکیشن خبری، رسانه اجتماعی و پلتفرم ویدئویی به کار می‌رود. نظریه توضیح می‌دهد چرا فناوری خوب گاه پذیرفته نمی‌شود و چرا آموزش و طراحی تجربه، پذیرش را تغییر می‌دهد. اهمیت آن، سادگی و قابلیت سنجش است؛ اما باید با عادت، احساس و دسترسی ساختاری تکمیل شود.",
        "definition": "مدل پذیرش فناوری، چارچوبی است که قصد استفاده از فناوری را از دو باور ادراکی توضیح می‌دهد: سودمندی برای عملکرد و سهولت کاربرد.",
        "main_problem": "مسئله این است که چرا فناوری مفید گاه رد و فناوری متوسط گاه پذیرفته می‌شود. پاسخ، ادراک کاربر است. پرسش دوم، طراحی است: کدام ویژگی تجربه، سودمندی و سهولت ادراک‌شده را بالا می‌برد.",
        "mechanism": "۱. سودمندی ادراک‌شده: فناوری، عملکرد را بهتر می‌کند.\n۲. سهولت ادراک‌شده: کار با فناوری، کم‌زحمت است.\n۳. اثر متقابل: سهولت، سودمندی ادراک‌شده را بالا می‌برد.\n۴. نگرش: باورها، نگرش مثبت یا منفی می‌سازند.\n۵. قصد استفاده: نگرش به قصد و رفتار می‌رسد.\n۶. تعدیل: هنجار، تجربه و شرایط تسهیل‌کننده اثر را تغییر می‌دهند.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا اپلیکیشن خبری با تجربه پیچیده رها می‌شود، چرا اشتراک ویدئویی با ارزش ادراک‌شده بالا می‌گیرد و چرا آموزش کاربر، پذیرش را تغییر می‌دهد. نکته مهم این است که مدل، باور را می‌سنجد نه کیفیت عینی فناوری؛ از این رو، شکاف میان کیفیت فنی و ادراک کاربر، خود موضوع طراحی ارتباطی است و تنها با بهبود مهندسی پر نمی‌شود.",
        "assumptions": [
            "قصد استفاده، پیش‌بین رفتار است.",
            "دو باور ادراکی، نگرش را می‌سازند.",
            "کاربر، سود و زحمت را می‌سنجد.",
        ],
        "principles": [
            "سودمندی، پیش‌بین اصلی پذیرش است.",
            "سهولت، سودمندی ادراک‌شده را تقویت می‌کند.",
            "ادراک کاربر، مستقل از کیفیت عینی است.",
        ],
        "critiques": [
            "۱. عادت: رفتار خودکار در مدل کم دیده می‌شود.\n۲. احساس: لذت و هویت، بیرون از دو سازه می‌مانند.\n۳. دسترسی: موانع ساختاری و اقتصادی کم تحلیل می‌شوند.\n۴. سنجش: مقیاس خودگزارشی، سوگیری دارد.\n۵. زمینه: یافته‌های اولیه بیشتر سازمانی‌اند.",
        ],
        "applications": [
            "طراحی محصول: سنجش سودمندی و سهولت.",
            "رسانه دیجیتال: پذیرش اپلیکیشن و پلتفرم.",
            "آموزش کاربر: کاهش زحمت ادراک‌شده.",
            "بازاریابی فناوری: پیام ارزش و تجربه.",
        ],
        "evolution": "دیویس در ۱۹۸۹ مدل را عرضه کرد، ونکاتش و دیویس در ۲۰۰۰ آن را با هنجار ذهنی گستردند و مدل یکپارچه پذیرش، سازه‌های بیشتری افزود. پژوهش رسانه، مدل را به اپلیکیشن و پلتفرم برد.",
        "key_concepts": [
            "سودمندی ادراک‌شده (Perceived Usefulness)",
            "سهولت استفاده ادراک‌شده (Perceived Ease of Use)",
            "قصد استفاده (Intention to Use)",
            "نگرش به فناوری (Attitude)",
            "هنجار ذهنی (Subjective Norm)",
            "شرایط تسهیل‌کننده (Facilitating Conditions)",
        ],
        "studies": [
            "Davis, F. D. (1989). Perceived usefulness, perceived ease of use, and user acceptance of information technology. MIS Quarterly, 13(3), 319-340.",
            "Venkatesh, V., & Davis, F. D. (2000). A theoretical extension of the technology acceptance model. Management Science, 46(2), 186-204.",
        ],
        "theorists": "فرد دیویس؛ ویسوانات ونکاتش",
        "theorists_text": "دیویس (۱۹۸۹)؛ ونکاتش و دیویس (۲۰۰۰)",
        "year": 1989,
        "model": "سودمندی و سهولت ادراک‌شده → نگرش → قصد استفاده → پذیرش فناوری.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nدیویس مدل را بر نظریه کنش منطقی بنا کرد و دو باور ادراکی را به پذیرش فناوری گره زد. نوآوری چارچوب، سادگی و قابلیت سنجش است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با پیمایش مقیاس باورها و قصد انجام می‌شود. پژوهشی که تنها استفاده واقعی را می‌سنجد، باور را از دست می‌دهد؛ و پژوهشی که هر پذیرش را سودمندی می‌خواند، اثر عادت و فشار اجتماعی را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در پیش‌بینی پذیرش اولیه است، اما باید با عادت و لذت تکمیل شود. پذیرش بی مصرف پایدار، به استفاده تشریفاتی بدل می‌شود.",
        "critique_text": "\n".join([
            "۱. عادت: رفتار خودکار کم دیده می‌شود.",
            "۲. احساس: لذت و هویت بیرون می‌مانند.",
            "۳. دسترسی: موانع ساختاری کم تحلیل است.",
            "۴. سنجش: خودگزارشی سوگیرانه است.",
            "۵. زمینه: یافته‌ها سازمانی‌اند.",
        ]),
        "example_text": "اپلیکیشن خبری که سودمند اما پیچیده است، کنار گذاشته می‌شود؛ ساده‌سازی تجربه، سهولت ادراک‌شده را بالا می‌برد و قصد استفاده را تغییر می‌دهد.",
    },
}

REQUIRED_SECTIONS = ["summary", "definition", "main_problem", "mechanism", "assumptions",
                     "principles", "critiques", "applications", "evolution", "key_concepts",
                     "theorists", "model", "studies"]
WORD_KEYS = ["summary", "definition", "main_problem", "mechanism", "critiques", "applications",
             "evolution", "key_concepts", "principles", "studies", "assumptions"]


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
                                       "verified": n_verified, "batch": 116}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH116 CONCEPT DONE")


if __name__ == "__main__":
    main()
