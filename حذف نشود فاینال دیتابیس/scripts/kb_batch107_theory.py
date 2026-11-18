# -*- coding: utf-8 -*-
"""Batch 107: full documentation for MC-680, MC-681, MC-683, MC-684."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch107-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch107_theory.json"

S = {
    "MC-680": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Some Explorations in Initial Interaction and Beyond: Toward a Developmental Theory of Interpersonal Communication",
             title_fa="کاوش‌هایی در تعامل آغازین و فراتر از آن: به سوی نظریه‌ای تحولی در ارتباط میان‌فردی",
             authors="Berger, C. R.; Calabrese, R. J.", year=1975,
             publisher="Human Communication Research",
             doi=None, url="https://en.wikipedia.org/wiki/Uncertainty_reduction_theory",
             language="en", isbn=None,
             citation="Berger, C. R., & Calabrese, R. J. (1975). Some explorations in initial interaction and beyond: Toward a developmental theory of interpersonal communication. Human Communication Research, 1(2), 99-112.",
             locator="1(2):99-112", locator_type="page_range",
             supports="uncertainty reduction axioms in initial interaction", verified=True),
        dict(kind="BOOK_CHAPTER",
             title_en="An Anxiety/Uncertainty Management Theory of Effective Communication",
             title_fa="نظریه مدیریت اضطراب و عدم‌قطعیت در ارتباط اثربخش",
             authors="Gudykunst, W. B.", year=2005, publisher="Sage",
             doi=None, url=None, language="en", isbn=None,
             citation="Gudykunst, W. B. (2005). An anxiety/uncertainty management theory of effective communication. In W. B. Gudykunst (Ed.), Theorizing about intercultural communication (pp. 281-322). Sage.",
             locator="pp. 281-322", locator_type="PAGE",
             supports="extension of uncertainty reduction to intercultural communication", verified=False),
    ],
    "MC-681": [
        dict(kind="BOOK",
             title_en="Social Penetration: The Development of Interpersonal Relationships",
             title_fa="نفوذ اجتماعی: شکل‌گیری روابط میان‌فردی",
             authors="Altman, I.; Taylor, D. A.", year=1973,
             publisher="Holt, Rinehart and Winston",
             doi=None, url="https://archive.org/details/socialpenetratio00altm",
             language="en", isbn=None,
             citation="Altman, I., & Taylor, D. A. (1973). Social penetration: The development of interpersonal relationships. Holt, Rinehart and Winston.",
             locator="work", locator_type="work",
             supports="onion model of self-disclosure breadth and depth", verified=True),
        dict(kind="BOOK",
             title_en="Boundaries of Privacy: Dialectics of Disclosure",
             title_fa="مرزهای حریم خصوصی: دیالکتیک افشا",
             authors="Petronio, S.", year=2002,
             publisher="State University of New York Press",
             doi=None, url=None, language="en", isbn=None,
             citation="Petronio, S. (2002). Boundaries of privacy: Dialectics of disclosure. State University of New York Press.",
             locator="work", locator_type="work",
             supports="communication privacy management as extension of disclosure theory", verified=False),
    ],
    "MC-683": [
        dict(kind="BOOK",
             title_en="How to Do Things with Words",
             title_fa="چگونه با واژه‌ها کار انجام می‌دهیم",
             authors="Austin, J. L.", year=1962, publisher="Oxford University Press",
             doi=None, url="https://global.oup.com/academic/product/how-to-do-things-with-words-9780198245537",
             language="en", isbn="978-0-19-824553-7",
             citation="Austin, J. L. (1962). How to do things with words. Oxford University Press.",
             locator="work", locator_type="work",
             supports="performatives and locutionary/illocutionary/perlocutionary acts", verified=True),
        dict(kind="BOOK",
             title_en="Speech Acts: An Essay in the Philosophy of Language",
             title_fa="کنش‌های گفتاری: جستاری در فلسفه زبان",
             authors="Searle, J. R.", year=1969, publisher="Cambridge University Press",
             doi=None, url=None, language="en", isbn=None,
             citation="Searle, J. R. (1969). Speech acts: An essay in the philosophy of language. Cambridge University Press.",
             locator="work", locator_type="work",
             supports="taxonomy of illocutionary acts and constitutive rules", verified=False),
    ],
    "MC-684": [
        dict(kind="BOOK_CHAPTER",
             title_en="Logic and Conversation",
             title_fa="منطق و گفت‌وگو",
             authors="Grice, H. P.", year=1975, publisher="Academic Press",
             doi=None, url="https://www.sfu.ca/~jeffpell/Cogs300/GriceLogicConvers75.pdf",
             language="en", isbn=None,
             citation="Grice, H. P. (1975). Logic and conversation. In P. Cole & J. L. Morgan (Eds.), Syntax and semantics, Vol. 3: Speech acts (pp. 41-58). Academic Press.",
             locator="pp. 41-58", locator_type="PAGE",
             supports="cooperative principle and four conversational maxims", verified=True),
        dict(kind="BOOK",
             title_en="Relevance: Communication and Cognition",
             title_fa="مربوط‌بودن: ارتباط و شناخت",
             authors="Sperber, D.; Wilson, D.", year=1986, publisher="Blackwell",
             doi=None, url=None, language="en", isbn=None,
             citation="Sperber, D., & Wilson, D. (1986). Relevance: Communication and cognition. Blackwell.",
             locator="work", locator_type="work",
             supports="relevance-theoretic revision of Gricean maxims", verified=False),
    ],
}

ENRICH = {
    "MC-680": {
        "summary": "(برگر و کالابریز، ۱۹۷۵) نظریه تقلیل عدم‌قطعیت می‌گوید در تعامل آغازین با غریبه، دغدغه اصلی کاهش عدم‌قطعیت است. عدم‌قطعیت دو چهره دارد: شناختی، یعنی باورهای مبهم درباره طرف مقابل، و رفتاری، یعنی پیش‌بینی‌ناپذیری کنش او. برگر و کالابریز اصل‌هایی عرضه کردند که ارتباط کلامی و بیان‌گری غیرکلامی را به کاهش عدم‌قطعیت گره می‌زد؛ شباهت، جذابیت و شبکه مشترک نیز عدم‌قطعیت را کم می‌کردند. افراد برای کاهش عدم‌قطعیت سه راهبرد به کار می‌برند: مشاهده غیرفعال، پرس‌وجوی فعال از دیگران و پرسش مستقیم تعاملی. نظریه، ارتباط را ابزار اصلی شناخت دیگری در آغاز رابطه می‌داند. این نظریه، آغازگر سنت پژوهش تجربی در ارتباط میان‌فردی شد.",
        "definition": "نظریه تقلیل عدم‌قطعیت، چارچوبی است که تعامل آغازین را تلاش برای کم‌کردن ابهام شناختی و رفتاری درباره طرف مقابل می‌داند و ارتباط، شباهت، جذابیت و شبکه مشترک را به این کاهش پیوند می‌دهد.",
        "main_problem": "مسئله این است که افراد در برخورد نخست با غریبه چگونه ابهام را کم می‌کنند. پاسخ، ارتباط و راهبردهای جست‌وجوی اطلاعات است. پرسش دوم، مرز است: آیا کاهش عدم‌قطعیت همیشه مطلوب است یا عدم‌قطعیت می‌تواند تجربه‌ای پذیرفتنی و حتی لذت‌بخش باشد.",
        "mechanism": "۱. عدم‌قطعیت شناختی: باورهای مبهم درباره نگرش و ویژگی طرف.\n۲. عدم‌قطعیت رفتاری: ناتوانی در پیش‌بینی کنش طرف.\n۳. ارتباط کلامی: افزایش گفت‌وگو، عدم‌قطعیت را کم می‌کند.\n۴. بیان‌گری غیرکلامی: گرمی و نشانه‌های پیوند، ابهام را کاهش می‌دهد.\n۵. شباهت و جذابیت: شباهت ادراک‌شده و کشش متقابل، عدم‌قطعیت را کم می‌کند.\n۶. راهبردهای جست‌وجو: مشاهده، پرس‌وجو از دیگران و پرسش مستقیم.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا خبرنگار پیش از مصاحبه درباره منبع جست‌وجو می‌کند، چرا اولین تماس با یک منبع ناآشنا با احتیاط و پرسش‌های کوتاه آغاز می‌شود و چرا پروفایل شبکه اجتماعی به راهبرد جست‌وجوی غیرفعال بدل شده است. نکته مهم این است که عدم‌قطعیت همیشه دشمن رابطه نیست؛ در برخی موقعیت‌ها کنجکاوی و تازگی، ارزش خود را دارند.",
        "assumptions": [
            "در تعامل آغازین، کاهش ابهام انگیزه اصلی است.",
            "ارتباط، ابزار اصلی جست‌وجوی اطلاعات است.",
            "کاهش عدم‌قطعیت به ادامه رابطه کمک می‌کند.",
        ],
        "principles": [
            "عدم‌قطعیت شناختی و رفتاری متمایزند.",
            "شباهت و جذابیت، ابهام را کم می‌کنند.",
            "جست‌وجوی اطلاعات سه راهبرد اصلی دارد.",
        ],
        "critiques": [
            "۱. تمرکز بر تعامل آغازین: رابطه بلندمدت کم‌تر پوشش می‌یابد.\n۲. فرض ارزش: کاهش عدم‌قطعیت همیشه مطلوب فرض می‌شود.\n۳. فرهنگ: الگوی جست‌وجو در فرهنگ‌ها یکسان نیست.\n۴. تفاوت فردی: تحمل ابهام افراد متفاوت است.\n۵. رسانه دیجیتال: جست‌وجوی غیرفعال، نظریه را پیچیده کرده است.",
        ],
        "applications": [
            "مصاحبه خبری: آماده‌سازی و پرسش تدریجی از منبع ناآشنا.",
            "روابط عمومی: کاهش ابهام ذی‌نفعان در تماس نخست.",
            "تحلیل شبکه اجتماعی: شناخت راهبردهای جست‌وجوی پروفایل.",
            "آموزش ارتباط: مدیریت تحمل ابهام در تعامل تازه.",
        ],
        "evolution": "برگر و کالابریز در ۱۹۷۵ نظریه را در پژوهش ارتباط انسانی عرضه کردند. بعدها گودیکانست آن را به ارتباط بین‌فرهنگی و مدیریت اضطراب گسترد و پژوهش‌های رسانه شبکه‌ای، جست‌وجوی اطلاعات آنلاین را به چارچوب افزودند.",
        "key_concepts": [
            "عدم‌قطعیت شناختی (Cognitive Uncertainty)",
            "عدم‌قطعیت رفتاری (Behavioral Uncertainty)",
            "راهبرد غیرفعال (Passive Strategy)",
            "راهبرد فعال (Active Strategy)",
            "راهبرد تعاملی (Interactive Strategy)",
            "تحمل ابهام (Ambiguity Tolerance)",
        ],
        "studies": [
            "Berger, C. R., & Calabrese, R. J. (1975). Some explorations in initial interaction and beyond. Human Communication Research, 1(2), 99-112.",
            "Gudykunst, W. B. (2005). Anxiety/uncertainty management theory. In Theorizing about intercultural communication. Sage.",
        ],
        "theorists": "چارلز برگر؛ ریچارد کالابریز",
        "theorists_text": "برگر و کالابریز (۱۹۷۵)",
        "year": 1975,
        "model": "تعامل آغازین → عدم‌قطعیت شناختی و رفتاری → ارتباط، شباهت و جذابیت → کاهش ابهام → ادامه یا قطع رابطه.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nبرگر و کالابریز ارتباط را ابزار شناخت اجتماعی دیدند و تعامل نخست را مرحله‌ای مستقل کردند. نوآوری چارچوب، تفکیک ابهام شناختی از رفتاری است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با مقیاس عدم‌قطعیت، مشاهده تعامل و تحلیل راهبرد جست‌وجو انجام می‌شود. پژوهشی که تنها ابهام شناختی را می‌سنجد، پیش‌بینی رفتاری را از دست می‌دهد؛ و پژوهشی که کاهش ابهام را همیشه خوب می‌داند، ارزش ابهام را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در تحلیل اولین تماس است، اما باید با مطالعه رابطه بلندمدت تکمیل شود. جست‌وجوی بی مرز، به نظارت و نقض حریم بدل می‌شود.",
        "critique_text": "\n".join([
            "۱. تمرکز بر تعامل آغازین: رابطه بلندمدت کم‌تر پوشش می‌یابد.",
            "۲. فرض ارزش: کاهش ابهام همیشه مطلوب نیست.",
            "۳. فرهنگ: الگوی جست‌وجو یکسان نیست.",
            "۴. تفاوت فردی: تحمل ابهام متفاوت است.",
            "۵. رسانه دیجیتال: جست‌وجوی غیرفعال پیچیده شده است.",
        ]),
        "example_text": "خبرنگاری پیش از مصاحبه با یک مقام ناآشنا، سخنرانی‌های گذشته او را می‌خواند و با همکارانش گفت‌وگو می‌کند؛ در مصاحبه با پرسش‌های کوتاه آغاز می‌کند و به‌تدریج به موضوع حساس می‌رسد.",
    },
    "MC-681": {
        "summary": "(آلتمن و تیلور، ۱۹۷۳) نظریه نفوذ اجتماعی، رابطه میان‌فردی را به پیازی تشبیه می‌کند که لایه‌های آن از سطح عمومی تا هسته خصوصی ادامه دارد. نفوذ در رابطه با افشای خود پیش می‌رود و دو بُعد دارد: گستره، یعنی شمار موضوع‌ها، و عمق، یعنی میزان صمیمیت هر موضوع. افشا معمولاً تدریجی و دوسویه است و بر سنجش پاداش و هزینه تکیه دارد. رابطه می‌تواند پیشروی کند یا پس‌رفت و لایه‌های افشاشده بسته شود. نظریه، صمیمیت را حاصل مبادله تدریجی اطلاعات شخصی می‌داند و مسیر رابطه را از سطحی به عمیق ترسیم می‌کند. نفوذ اجتماعی، پیوند میان افشا، اعتماد و آسیب‌پذیری را توضیح می‌دهد. این نظریه، پایه پژوهش حریم خصوصی و خودافشایی در رسانه شد. نقدهای بعدی، آن را با مدل دیالکتیکی افشا و پنهان‌کاری ترکیب کردند.",
        "definition": "نفوذ اجتماعی، فرایندی است که در آن دو طرف با افشای تدریجی و دوسویه اطلاعات شخصی، از لایه‌های سطحی به لایه‌های عمیق شخصیت یکدیگر نفوذ می‌کنند و صمیمیت می‌سازند.",
        "main_problem": "مسئله این است که صمیمیت چگونه ساخته می‌شود و چرا برخی روابط سطحی می‌مانند. پاسخ، الگوی گستره و عمق افشا است. پرسش دوم، مرز است: افشای سریع و بی تناسب، چه هزینه‌ای برای رابطه و حریم خصوصی دارد.",
        "mechanism": "۱. لایه‌های شخصیت: از ویژگی‌های عمومی تا هسته خصوصی.\n۲. گستره افشا: شمار حوزه‌های زندگی که به اشتراک گذاشته می‌شود.\n۳. عمق افشا: میزان صمیمیت و آسیب‌پذیری هر حوزه.\n۴. تدریجی‌بودن: افشا در طول زمان و مرحله‌به‌مرحله پیش می‌رود.\n۵. دوسویگی: افشای متقابل، اعتماد و تعادل می‌سازد.\n۶. پاداش و هزینه: سنجش سود و خطر افشا، سرعت رابطه را تعیین می‌کند.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا مصاحبه عمیق با منبع، چند جلسه و اعتماد تدریجی می‌خواهد، چرا برنامه گفت‌وگومحور از افشای تدریجی مهمان استفاده می‌کند و چرا شبکه اجتماعی افشای سریع را آسان اما کنترل حریم را سخت می‌کند. نکته مهم این است که افشا همیشه خطی پیش نمی‌رود؛ ضربه، خیانت یا تغییر شرایط می‌تواند رابطه را پس‌رفت دهد.",
        "assumptions": [
            "شخصیت لایه‌ای و چندسطحی است.",
            "افشای خود، صمیمیت می‌سازد.",
            "افشا تدریجی و دوسویه است.",
        ],
        "principles": [
            "گستره و عمق دو بُعد افشا هستند.",
            "افشای متقابل، اعتماد می‌سازد.",
            "رابطه می‌تواند پس‌رفت کند.",
        ],
        "critiques": [
            "۱. خطی‌بودن: رابطه همیشه مرحله‌به‌مرحله پیش نمی‌رود.\n۲. سوگیری فردگرا: الگوی افشا در فرهنگ‌ها متفاوت است.\n۳. جنسیت: تفاوت الگوی افشا کم‌تر دیده می‌شود.\n۴. مدل پیاز: همه روابط با استعاره لایه‌ای توضیح داده نمی‌شوند.\n۵. رسانه دیجیتال: افشای سریع و گسترده، نظریه را به چالش می‌کشد.",
        ],
        "applications": [
            "مصاحبه عمیق: ساخت اعتماد و افشای تدریجی منبع.",
            "گفت‌وگوی رسانه‌ای: مدیریت ریتم افشای مهمان.",
            "حریم خصوصی: شناخت هزینه افشای سریع در شبکه اجتماعی.",
            "آموزش ارتباط: تنظیم گستره و عمق گفت‌وگو.",
        ],
        "evolution": "آلتمن و تیلور در ۱۹۷۳ نظریه را در کتاب نفوذ اجتماعی عرضه کردند. بعدها پژوهش حریم خصوصی و مدیریت ارتباط، مدل پیاز را با دیالکتیک افشا و پنهان‌کاری ترکیب کرد و رسانه دیجیتال، الگوهای افشای تازه را پیش کشید.",
        "key_concepts": [
            "نفوذ اجتماعی (Social Penetration)",
            "افشای خود (Self-Disclosure)",
            "گستره افشا (Breadth)",
            "عمق افشا (Depth)",
            "دوسویگی افشا (Reciprocity)",
            "پس‌رفت رابطه (Depenetration)",
        ],
        "studies": [
            "Altman, I., & Taylor, D. A. (1973). Social penetration. Holt, Rinehart and Winston.",
            "Petronio, S. (2002). Boundaries of privacy. State University of New York Press.",
        ],
        "theorists": "اروین آلتمن؛ دالماس تیلور",
        "theorists_text": "آلتمن و تیلور (۱۹۷۳)",
        "year": 1973,
        "model": "لایه‌های شخصیت + گستره و عمق افشا → افشای تدریجی و دوسویه → اعتماد و صمیمیت → ادامه یا پس‌رفت رابطه.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nآلتمن و تیلور صمیمیت را حاصل مبادله اطلاعات شخصی دیدند و آن را در مدل لایه‌ای صورت‌بندی کردند. نوآوری چارچوب، تفکیک گستره از عمق افشا است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با مقیاس افشای خود، تحلیل گفت‌وگو و پیگیری طولی انجام می‌شود. پژوهشی که تنها گستره را می‌سنجد، عمق را از دست می‌دهد؛ و پژوهشی که پیشروی خطی را فرض می‌کند، پس‌رفت را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در ساخت اعتماد در مصاحبه است، اما باید با اخلاق حریم تکمیل شود. افشای بی تناسب، آسیب‌پذیری بی حمایت می‌سازد.",
        "critique_text": "\n".join([
            "۱. خطی‌بودن: رابطه همیشه مرحله‌به‌مرحله نیست.",
            "۲. فردگرایی: الگوی افشا فرهنگی است.",
            "۳. جنسیت: تفاوت الگو کم دیده می‌شود.",
            "۴. مدل پیاز: همه روابط لایه‌ای نیستند.",
            "۵. رسانه دیجیتال: افشای سریع نظریه را به چالش می‌کشد.",
        ]),
        "example_text": "خبرنگاری برای پرونده‌ای حساس، در جلسه نخست درباره موضوع عمومی گفت‌وگو می‌کند و در جلسه‌های بعد با افشای متقابل و تضمین حمایت، اعتماد منبع را برای روایت شخصی می‌سازد.",
    },
    "MC-683": {
        "summary": "(آستین، ۱۹۶۲) نظریه کنش گفتاری می‌گوید زبان فقط توصیف واقعیت نیست؛ سخن گفتن، انجام دادن است. آستین میان کنش گفتاری تمایز نهاد: آنچه گفته می‌شود، کنش درون آن (مانند اعلام، قول دادن و دستور) و اثر آن (مانند قانع کردن) تفکیک کرد. او نشان داد شرایط مناسب، اجرای موفق کنش را ممکن می‌کند و برخی گفته‌ها در صورت نبود این شرایط، بی‌اثرند. سرل در ۱۹۶۹ طبقه‌بندی کنش‌ها را نظام‌مند کرد و قواعد سازنده زبان را پیش کشید. نظریه، خبر، وعده، تهدید و عذرخواهی را کنش می‌بیند، نه فقط انتقال اطلاعات. این نظریه، تحلیل رسانه را از سطح واژه به سطح مسئولیت کنش برد.",
        "definition": "کنش گفتاری، چارچوبی است که هر گفته را نه فقط جمله‌ای درباره جهان، بلکه کنشی می‌داند که با شرایط مناسب، تعهد، دستور، اعلام یا اثر بر مخاطب می‌سازد.",
        "main_problem": "مسئله این است که چرا برخی جمله‌ها فقط خبر می‌دهند و برخی تعهد یا تغییر وضعیت می‌سازند. پاسخ، تفکیک لایه‌های کنش گفتاری است. پرسش دوم، اعتبار است: چه شرایطی لازم است تا خبر، عذرخواهی یا وعده، کنشی معتبر شمرده شود.",
        "mechanism": "۱. کنش گفتاری: تولید گفته با معنا و ارجاع.\n۲. کنش درون گفتار: آنچه گوینده با گفته انجام می‌دهد؛ اعلام، دستور، قول.\n۳. اثر گفتار: پیامد گفته بر مخاطب؛ اقناع، شرم، اقدام.\n۴. شرایط مناسب: صلاحیت گوینده، نیت و زمینه، اجرای کنش را ممکن می‌کند.\n۵. طبقه‌بندی: اظهاری، دستوری، تعهدی، بیان احساسی و اعلامی.\n۶. کنش غیرمستقیم: جمله خبری می‌تواند درخواست یا تهدید باشد.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا تیتر خبری می‌تواند اتهام بزند، چرا عذرخواهی رسمی کنشی حقوقی و اخلاقی است و چرا نقل قول تحریف‌شده، کنشی متفاوت از نیت گوینده می‌سازد. در تحلیل تبلیغات و سخنرانی سیاسی، تمایز خبر و کنش، ابزار مهمی است. نکته مهم این است که کنش گفتاری بی شرایط مناسب، معتبر نیست؛ اما ممکن است همچنان اثر روانی و اجتماعی بگذارد.",
        "assumptions": [
            "زبان فقط ابزار توصیف نیست.",
            "گفته‌ها در شرایط مناسب کنش می‌سازند.",
            "کنش گفتاری لایه‌های متمایز دارد.",
        ],
        "principles": [
            "گفتن، در شرایطی انجام دادن است.",
            "شرایط مناسب، اعتبار کنش را می‌سازد.",
            "جمله خبری می‌تواند کنش غیرمستقیم باشد.",
        ],
        "critiques": [
            "۱. تمرکز بر زبان روزمره: کنش نهادی و حقوقی پیچیده‌تر است.\n۲. فرهنگ: شرایط مناسب در فرهنگ‌ها متفاوت است.\n۳. نیت: دسترسی به نیت گوینده همیشه ممکن نیست.\n۴. قدرت: نقش نابرابری و اجبار کم‌تر دیده می‌شود.\n۵. کاربرد رسانه‌ای: تعمیم از گفت‌وگو به متن رسانه‌ای نیازمند احتیاط است.",
        ],
        "applications": [
            "تحلیل خبر: تفکیک اتهام، نقل قول و اعلام.",
            "اخلاق رسانه: سنجش اعتبار عذرخواهی و وعده عمومی.",
            "تحلیل تبلیغات: شناخت کنش پنهان در پیام.",
            "حقوق رسانه: ارزیابی تهمت و افترا در چارچوب کنش.",
        ],
        "evolution": "آستین در ۱۹۶۲ درس‌های خود را در کتاب چگونه با واژه‌ها کار انجام می‌دهیم منتشر کرد. سرل در ۱۹۶۹ طبقه‌بندی و قواعد را نظام‌مند کرد و بعدها کاربردشناسی، کنش گفتاری را به تحلیل گفتمان و رسانه برد.",
        "key_concepts": [
            "کنش گفتاری (Speech Act)",
            "کنش درون گفتار (Illocutionary Act)",
            "اثر گفتار (Perlocutionary Act)",
            "شرایط مناسب (Felicity Conditions)",
            "کنش غیرمستقیم (Indirect Speech Act)",
            "قواعد سازنده (Constitutive Rules)",
        ],
        "studies": [
            "Austin, J. L. (1962). How to do things with words. Oxford University Press.",
            "Searle, J. R. (1969). Speech acts. Cambridge University Press.",
        ],
        "theorists": "جان آستین؛ جان سرل",
        "theorists_text": "آستین (۱۹۶۲)؛ سرل (۱۹۶۹)",
        "year": 1962,
        "model": "گفته → کنش درون گفتار → اثر بر مخاطب؛ اعتبار کنش به شرایط مناسب و صلاحیت گوینده وابسته است.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nآستین تفکیک جمله خبری و کنشی را فروریخت و گفتن را انجام دادن دید. نوآوری چارچوب، تفکیک سه لایه کنش و طرح شرایط اعتبار است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با تحلیل متن، بررسی شرایط و مقایسه نیت و اثر انجام می‌شود. پژوهشی که تنها معنا را می‌سنجد، کنش را از دست می‌دهد؛ و پژوهشی که نیت گوینده را قطعی می‌خواند، تفسیر مخاطب را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در تحلیل اتهام و عذرخواهی است، اما باید با حقوق و اخلاق تکمیل شود. کنش بی مسئولیت، به آسیب رسانه‌ای بدل می‌شود.",
        "critique_text": "\n".join([
            "۱. زبان روزمره: کنش نهادی پیچیده‌تر است.",
            "۲. فرهنگ: شرایط مناسب یکسان نیست.",
            "۳. نیت: دسترسی به نیت دشوار است.",
            "۴. قدرت: نابرابری کم دیده می‌شود.",
            "۵. تعمیم: انتقال به متن رسانه‌ای نیازمند احتیاط است.",
        ]),
        "example_text": "تیتری که مقام را متهم می‌کند، تنها خبر نمی‌دهد؛ کنش اتهام می‌سازد. اگر منبع اتهام روشن نباشد، رسانه مسئول اثر حقوقی و اخلاقی آن کنش است.",
    },
    "MC-684": {
        "summary": "(گرایس، ۱۹۷۵) اصل تعاون می‌گوید سخنگو و شنونده در گفت‌وگو، در هر مرحله سهمی می‌گذارند که با هدف مشترک گفت‌وگو سازگار باشد. گرایس چهار اصل فرعی را صورتبندی کرد: کمیت، یعنی به‌اندازه لازم گفتن؛ کیفیت، یعنی راست گفتن؛ ربط، یعنی مربوط گفتن؛ و شیوه، یعنی روشن و بی‌ابهام گفتن. وقتی گوینده اصلی را آشکارا نقض کند، شنونده از آن نقض، معنای ضمنی می‌سازد. این معنای ضمنی، استلزام مکالمه‌ای نامیده می‌شود. نظریه، فهم گفت‌وگو را از معنای واژه‌ها فراتر می‌برد. گرایس نشان داد معنای گفت‌وگو، حاصل همکاری است نه فقط رمزگان. این چارچوب، پایه کاربردشناسی و تحلیل گفتمان شد. کاربرد آن در رسانه، خواندن پیام پنهان را ممکن می‌کند و مسئولیت تفسیر را بر دوش خواننده می‌گذارد.",
        "definition": "اصل تعاون، چارچوبی است که گفت‌وگوی موفق را بر پایه سهم متناسب طرفین با هدف مشترک توضیح می‌دهد و چهار اصل کمیت، کیفیت، ربط و شیوه را برای سهم مناسب صورتبندی می‌کند.",
        "main_problem": "مسئله این است که چرا شنونده از جمله‌ای که معنای ظاهری‌اش ناقص است، معنایی کامل می‌فهمد. پاسخ، استلزام مکالمه‌ای است. پرسش دوم، مرز است: آیا اصول گرایس قواعد جهان‌شمول‌اند یا به فرهنگ و زمینه وابسته‌اند.",
        "mechanism": "۱. اصل تعاون: سهم گفت‌وگو باید با هدف مشترک سازگار باشد.\n۲. کمیت: نه بیشتر و نه کمتر از نیاز اطلاعات دادن.\n۳. کیفیت: گفتن آنچه درست می‌دانیم و پرهیز از بی‌پایه.\n۴. ربط: سخن باید با موضوع گفت‌وگو مرتبط باشد.\n۵. شیوه: روشنی، کوتاهی و پرهیز از ابهام.\n۶. استلزام: نقض آشکار اصل، معنای ضمنی می‌سازد.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا پاسخ مبهم یک مقام به معنای طفره تعبیر می‌شود، چرا تیتر با حذف اطلاعات، استلزام می‌سازد و چرا تبلیغ با نقض کیفیت، ادعای ضمنی می‌کند. در مصاحبه، پرسش خبرنگار و پاسخ گریزان، بازی استلزام است. نکته مهم این است که نقض اصل همیشه فریب نیست؛ طنز، ادب و نقد اجتماعی نیز از همین نقض ساخته می‌شوند.",
        "assumptions": [
            "گفت‌وگو با همکاری طرفین پیش می‌رود.",
            "سخن، معمولاً اطلاعات کافی و درست می‌دهد.",
            "نقض اصل، معنای ضمنی می‌سازد.",
        ],
        "principles": [
            "کمیت، کیفیت، ربط و شیوه، سهم را تنظیم می‌کنند.",
            "شنونده از نقض، معنا می‌سازد.",
            "نقض اصل همیشه فریب نیست.",
        ],
        "critiques": [
            "۱. جهان‌شمولی: اصول در فرهنگ‌ها یکسان کار نمی‌کنند.\n۲. هم‌پوشانی: اصول کمیت و ربط به هم می‌آمیزند.\n۳. جایگزین: نظریه ربط، اصول را به یک اصل فروکاست.\n۴. ادب: گرایس نقش ادب و قدرت را کم‌تر دیده است.\n۵. سنجش: استلزام از تفسیر شنونده برمی‌آید و قطعی نیست.",
        ],
        "applications": [
            "تحلیل مصاحبه: شناخت طفره و پاسخ گریزان.",
            "نقد تیتر: بررسی استلزام ناشی از حذف اطلاعات.",
            "اخلاق تبلیغات: سنجش ادعای ضمنی و نقض کیفیت.",
            "آموزش سواد رسانه‌ای: خواندن معنای پنهان پیام.",
        ],
        "evolution": "گرایس در ۱۹۷۵ اصل تعاون را در مجموعه کنش‌های گفتاری منتشر کرد. بعدها نظریه ربط، ادب و کاربردشناسی بین‌فرهنگی، اصول را بازبینی کردند و پژوهش رسانه، استلزام را به تحلیل خبر و تبلیغ برد.",
        "key_concepts": [
            "اصل تعاون (Cooperative Principle)",
            "اصل کمیت (Maxim of Quantity)",
            "اصل کیفیت (Maxim of Quality)",
            "اصل ربط (Maxim of Relation)",
            "اصل شیوه (Maxim of Manner)",
            "استلزام مکالمه‌ای (Conversational Implicature)",
        ],
        "studies": [
            "Grice, H. P. (1975). Logic and conversation. In Syntax and semantics, Vol. 3. Academic Press.",
            "Sperber, D., & Wilson, D. (1986). Relevance: Communication and cognition. Blackwell.",
        ],
        "theorists": "پل گرایس",
        "theorists_text": "گرایس (۱۹۷۵)",
        "year": 1975,
        "model": "اصل تعاون + چهار اصل → سهم متناسب → نقض آشکار → استلزام مکالمه‌ای → معنای فراتر از واژه‌ها.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nگرایس معنای گفت‌وگو را از معنای جمله جدا کرد و همکاری را پایه فهم دید. نوآوری چارچوب، صورت‌بندی استلزام مکالمه‌ای است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با تحلیل گفت‌وگو، آزمون تفسیر و مقایسه فرهنگ انجام می‌شود. پژوهشی که تنها معنای ظاهری را می‌سنجد، استلزام را از دست می‌دهد؛ و پژوهشی که استلزام را قطعی می‌خواند، تفسیر شنونده را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در خواندن پیام پنهان است، اما باید با نظریه ادب و قدرت تکمیل شود. استلزام بی زمینه، به تفسیر دلخواه بدل می‌شود.",
        "critique_text": "\n".join([
            "۱. جهان‌شمولی: اصول فرهنگی‌اند.",
            "۲. هم‌پوشانی: کمیت و ربط در هم می‌آمیزند.",
            "۳. جایگزین: نظریه ربط اصول را فروکاست.",
            "۴. ادب: قدرت و ادب کم دیده می‌شود.",
            "۵. سنجش: استلزام قطعی نیست.",
        ]),
        "example_text": "خبرنگار می‌پرسد آیا گزارش را خوانده‌اید و مقام پاسخ می‌دهد جلسه طولانی بود؛ پاسخ با نقض اصل ربط، طفره را ضمنی می‌کند و خبرنگار آن را می‌فهمد.",
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
                                       "verified": n_verified, "batch": 107}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH107 THEORY DONE")


if __name__ == "__main__":
    main()
