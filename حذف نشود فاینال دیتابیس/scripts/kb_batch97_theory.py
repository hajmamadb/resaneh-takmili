# -*- coding: utf-8 -*-
"""Batch 97: full documentation for MC-533, MC-534, MC-539, MC-568."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch97-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch97_theory.json"

S = {
    "MC-533": [
        dict(kind="BOOK",
             title_en="The Science Question in Feminism",
             title_fa="پرسش علم در فمینیسم",
             authors="Harding, S.", year=1986, publisher="Cornell University Press",
             doi=None, url="https://cornellpress.cornell.edu/book/9780801418808/the-science-question-in-feminism/",
             language="en", isbn="9780801418808",
             citation="Harding, S. (1986). The science question in feminism. Cornell University Press.",
             locator="work", locator_type="work",
             supports="feminist standpoint / strong objectivity / three feminist epistemologies", verified=True),
        dict(kind="BOOK_CHAPTER",
             title_en="The Feminist Standpoint: Developing the Ground for a Specifically Feminist Historical Materialism",
             title_fa="نقطه‌نظر فمینیستی: ساختن بنیانی برای ماتریالیسم تاریخی مشخصاً فمینیستی",
             authors="Hartsock, N. C. M.", year=1983, publisher="D. Reidel",
             doi=None, url=None, language="en", isbn=None,
             citation="Hartsock, N. C. M. (1983). The feminist standpoint: Developing the ground for a specifically feminist historical materialism. In S. Harding & M. B. Hintikka (Eds.), Discovering reality: Feminist perspectives on epistemology, metaphysics, methodology, and philosophy of science (pp. 283-310). D. Reidel.",
             locator="pp. 283-310", locator_type="page_range",
             supports="standpoint from divided labour / mediated vision", verified=True),
    ],
    "MC-534": [
        dict(kind="BOOK",
             title_en="Sensemaking in Organizations",
             title_fa="معناسازی در سازمان‌ها",
             authors="Weick, K. E.", year=1995, publisher="Sage",
             doi=None, url=None, language="en", isbn=None,
             citation="Weick, K. E. (1995). Sensemaking in organizations. Sage.",
             locator="work", locator_type="work",
             supports="seven properties of sensemaking / enacted environment / plausibility", verified=True),
        dict(kind="BOOK",
             title_en="The Social Psychology of Organizing (2nd ed.)",
             title_fa="روان‌شناسی اجتماعی سازمان‌دهی (ویرایش دوم)",
             authors="Weick, K. E.", year=1979, publisher="McGraw-Hill",
             doi=None, url=None, language="en", isbn=None,
             citation="Weick, K. E. (1979). The social psychology of organizing (2nd ed.). McGraw-Hill.",
             locator="work", locator_type="work",
             supports="organizing as process / equivocality reduction / enactment", verified=False),
    ],
    "MC-539": [
        dict(kind="BOOK",
             title_en="Globalization: Social Theory and Global Culture",
             title_fa="جهانی‌شدن: نظریه اجتماعی و فرهنگ جهانی",
             authors="Robertson, R.", year=1992, publisher="Sage",
             doi=None, url="https://sk.sagepub.com/book/mono/preview/globalization.pdf",
             language="en", isbn=None,
             citation="Robertson, R. (1992). Globalization: Social theory and global culture. Sage.",
             locator="work", locator_type="work",
             supports="compression of the world / global field / glocalization", verified=True),
        dict(kind="BOOK",
             title_en="Modernity at Large: Cultural Dimensions of Globalization",
             title_fa="مدرنیته در مقیاس کلان: ابعاد فرهنگی جهانی‌شدن",
             authors="Appadurai, A.", year=1996, publisher="University of Minnesota Press",
             doi=None, url=None, language="en", isbn=None,
             citation="Appadurai, A. (1996). Modernity at large: Cultural dimensions of globalization. University of Minnesota Press.",
             locator="work", locator_type="work",
             supports="global cultural flows / mediascapes / hybridization", verified=False),
    ],
    "MC-568": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Affective Responses to the Emotions of a Protagonist",
             title_fa="پاسخ‌های عاطفی به هیجان‌های قهرمان داستان",
             authors="Zillmann, D.; Cantor, J. R.", year=1977,
             publisher="Journal of Experimental Social Psychology",
             doi=None, url="https://www.sciencedirect.com/science/article/pii/S0022103177800085",
             language="en", isbn=None,
             citation="Zillmann, D., & Cantor, J. R. (1977). Affective responses to the emotions of a protagonist. Journal of Experimental Social Psychology, 13(2), 155-165.",
             locator="13(2):155-165", locator_type="page_range",
             supports="affective disposition toward characters determines viewer emotion", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Expanding Disposition Theory: Reconsidering Character Liking, Moral Evaluations, and Enjoyment",
             title_fa="گسترش نظریه گرایش: بازنگری در دوست‌داشتن شخصیت، داوری اخلاقی و لذت",
             authors="Raney, A. A.", year=2004, publisher="Communication Theory",
             doi=None, url=None, language="en", isbn=None,
             citation="Raney, A. A. (2004). Expanding disposition theory: Reconsidering character liking, moral evaluations, and enjoyment. Communication Theory, 14(4), 348-369.",
             locator="14(4):348-369", locator_type="page_range",
             supports="moral evaluation and enjoyment in drama and sport", verified=False),
    ],
}

ENRICH = {
    "MC-533": {
        "summary": "(هارتساک، ۱۹۸۳؛ هاردینگ، ۱۹۸۶) نظریه نقطه‌نظر می‌گوید شناخت از موقعیت اجتماعی شناخت‌گر برمی‌آید و گروه‌های به‌حاشیه‌رانده‌شده، به سبب تجربه‌زیسته خود، دیدگاه ممتازتری برای دیدن روابط قدرت دارند. هاردینگ این را در برابر ادعای بی‌طرفی معرفت شناختی نهاد و «عینیت قوی» را پیشنهاد کرد: عینیتی که موقعیت خود پژوهشگر را نیز در حساب می‌آورد. هارتساک ریشه نقطه‌نظر را در تقسیم کار و تجربه مادری جست. مهم است که نقطه‌نظر، دیدگاه شخصی یا نسبی‌گرایی نیست؛ ادعایی درباره موقعیت ساختاری دانش است.",
        "definition": "نظریه نقطه‌نظر، رویکردی معرفت‌شناختی است که دانش را موقعیت‌مند می‌داند و بر آن است که موقعیت‌های حاشیه‌ای، به سبب دسترسی به تجربه‌ای که موقعیت مسلط پنهان می‌کند، می‌توانند بنیانی برای نقد و دانش معتبرتر بسازند.",
        "main_problem": "مسئله این است که دانش رسمی، ادعای بی‌طرفی دارد اما از موقعیت خاصی سخن می‌گوید. پرسش هاردینگ این است که چگونه می‌توان عینیت را حفظ کرد، بی‌آنکه موقعیت پژوهشگر را انکار کرد. پرسش دوم، سیاسی است: چه کسی حق دارد تجربه گروه خود را دانش عمومی بنامد و چه کسی فقط «دیدگاه» می‌نامد.",
        "mechanism": "۱. شناخت موقعیت‌مند: هر دانش از جایگاهی اجتماعی برمی‌آید و همین جایگاه، آنچه دیده می‌شود را محدود می‌کند.\n۲. مزیت معرفتی حاشیه: گروه حاشیه‌ای هم نظم مسلط و هم هزینه‌های آن را تجربه می‌کند و همین، دید دوگانه می‌سازد.\n۳. روابط سلطه: نقطه‌نظر، ساختار نابرابری را نه ویژگی افراد، بلکه نظمی نهادی می‌بیند.\n۴. عینیت قوی: پژوهشگر به‌جای پنهان‌کردن موقعیت خود، آن را آشکار و در تحلیل حساب می‌کند.\n۵. سه پاسخ فمینیستی: تجربه‌گرایی فمینیستی، نقطه‌نظر و پسامدرنیسم فمینیستی، هر یک پاسخ متفاوتی به ادعای عینیت می‌دهند.\n۶. دانش جانشین: هدف، اصلاح معیارهای اعتبار است، نه کنارگذاشتن داوری مستدل.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا خبر «بی‌طرف» اغلب از موقعیت صاحبان قدرت روایت می‌کند، چرا صدای گروه‌های حاشیه‌ای به «دیدگاه» تقلیل می‌یابد و چرا تولید دانش درباره مخاطب، بدون حضور خود او ناقص می‌ماند. نکته مهم این است که نقطه‌نظر، دعوت به جایگزینی یک تعصب با تعصب دیگر نیست؛ دعوت به شفاف‌کردن موقعیت است.",
        "assumptions": [
            "دانش، مستقل از موقعیت اجتماعی شناخت‌گر نیست.",
            "موقعیت حاشیه‌ای، دسترسی ویژه‌ای به سازوکار قدرت می‌دهد.",
            "شفاف‌کردن موقعیت، اعتبار دانش را افزایش می‌دهد.",
        ],
        "principles": [
            "بی‌طرفی ادعایی، خود موقعیتی است.",
            "عینیت با شفافیت موقعیت تقویت می‌شود، نه با پنهان‌کردن آن.",
            "تجربه گروه‌های حاشیه‌ای، منبع داده معتبر است.",
        ],
        "critiques": [
            "۱. خطر ماهیت‌انگاری: نسبت‌دادن مزیت معرفتی به یک گروه، می‌تواند هویت را ذاتی کند.\n۲. تنوع درون‌گروهی: تجربه زنان یا گروه‌های حاشیه‌ای یکسان نیست و طبقه و نژاد آن را تفکیک می‌کند.\n۳. معیار اعتبار: اگر همه دانش‌ها موقعیت‌مندند، معیار ترجیح یک روایت بر دیگری چیست.\n۴. دشواری سنجش: مزیت معرفتی به‌سختی در پژوهش تجربی قابل آزمون است.\n۵. کاربرد گزینشی: در عمل، ادعای نقطه‌نظر می‌تواند به ابزار مشروعیت‌بخشی به یک روایت بدل شود.",
        ],
        "applications": [
            "اخلاق روزنامه‌نگاری: بازبینی ادعای بی‌طرفی در انتخاب منبع و روایت.",
            "پژوهش مخاطب: مشارکت گروه‌های حاشیه‌ای در تولید تفسیر.",
            "مطالعات علم: تحلیل موقعیت نهادهای تولید دانش.",
            "سیاست رسانه: سنجش بازنمایی صداهای کم‌شنیده.",
        ],
        "evolution": "هارتساک در ۱۹۸۳ نقطه‌نظر را بر پایه ماتریالیسم تاریخی صورت‌بندی کرد و هاردینگ در ۱۹۸۶ آن را در چارچوب معرفت‌شناسی فمینیستی و مفهوم عینیت قوی گسترد. پژوهش بعدی، نقطه‌نظر را با مطالعات پسااستعماری، نژاد و رسانه پیوند داد و بحث درباره چندگانگی موقعیت را پیش کشید.",
        "key_concepts": [
            "نقطه‌نظر (Standpoint)",
            "شناخت موقعیت‌مند (Situated Knowledge)",
            "عینیت قوی (Strong Objectivity)",
            "دید دوگانه (Double Vision)",
            "روابط سلطه (Relations of Ruling)",
            "دانش جانشین (Successor Science)",
        ],
        "studies": [
            "Hartsock, N. C. M. (1983). The feminist standpoint. In Discovering reality (pp. 283-310). D. Reidel.",
            "Harding, S. (1986). The science question in feminism. Cornell University Press.",
        ],
        "theorists": "نانسی هارتساک؛ ساندرا هاردینگ",
        "theorists_text": "نانسی هارتساک (۱۹۸۳)؛ ساندرا هاردینگ (۱۹۸۶)",
        "year": 1986,
        "model": "مدل نقطه‌نظر: موقعیت ساختاری + تقسیم کار → تجربه متفاوت → دید دوگانه → نقد روایت مسلط → عینیت قوی و دانش جانشین.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nهارتساک نقطه‌نظر را از تحلیل تقسیم کار و تجربه زیسته زنان ساخت و هاردینگ آن را به بحثی معرفت‌شناختی درباره عینیت گسترد. نوآوری چارچوب، پیوند دادن موقعیت اجتماعی با معیار اعتبار دانش است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با تحلیل منبع، چارچوب روایت و دامنه صداهای حاضر انجام می‌شود. پژوهشی که تنها شمار حضور گروه‌ها را می‌سنجد، ساختار روایت را از دست می‌دهد؛ و پژوهشی که تنها متن را می‌خواند، موقعیت تولید را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در نقد ادعای بی‌طرفی است، اما باید با تحلیل نهاد و اقتصاد رسانه تکمیل شود. در عمل، نقطه‌نظر بدون بررسی ساختار مالکیت و منابع، به بیانیه هویتی تقلیل می‌یابد.",
        "critique_text": "\n".join([
            "۱. خطر ماهیت‌انگاری: مزیت معرفتی به گروه نسبت داده می‌شود.",
            "۲. تنوع درون‌گروهی: تجربه گروه‌ها یکسان نیست.",
            "۳. معیار اعتبار: ترجیح یک روایت بر دیگری بر چه پایه است.",
            "۴. دشواری سنجش: مزیت معرفتی آزمون‌پذیر نیست.",
            "۵. کاربرد گزینشی: ادعای نقطه‌نظر به ابزار مشروعیت بدل می‌شود.",
        ]),
        "example_text": "خبری درباره طرح بازآفرینی شهری، تنها با مقام‌ها و سرمایه‌گذار گفت‌وگو می‌کند و ساکنان محله را «ذی‌نفع» می‌نامد. نقطه‌نظر می‌پرسد چرا تجربه ساکنان، داده معتبر شمرده نمی‌شود و چه کسی حق روایت را در دست دارد.",
    },
    "MC-534": {
        "summary": "(ویک، ۱۹۷۹؛ ۱۹۹۵) ویک سازمان را نه ساختار، بلکه فرایند سازمان‌دهی می‌دید: فعالیت پیوسته کاهش ابهام از راه معناسازی. او نشان داد افراد نخست عمل می‌کنند و سپس به عمل خود معنا می‌دهند؛ محیطی که به آن واکنش می‌دهند نیز تا حدی ساخته خودشان است. معناسازی، گذشته‌نگر، اجتماعی و هویت‌محور است و بر پایه نشانه‌های آشنا و با معیار باورپذیری، نه دقت کامل، پیش می‌رود. همین خصلت، توضیح می‌دهد چرا سازمان‌ها در بحران، تفسیرهای ناسازگار می‌سازند.",
        "definition": "معناسازی سازمانی، فرایند مستمری است که اعضا از راه آن، رویدادهای مبهم را به روایتی قابل کنش تبدیل می‌کنند و از این راه، سازمان‌دهی به‌عنوان واقعیت مشترک ساخته می‌شود.",
        "main_problem": "مسئله این است که سازمان‌ها با ابهام و تعدد تفسیر روبه‌رو هستند، اما باید هماهنگ عمل کنند. پرسش ویک این است که هماهنگی بدون حقیقت واحد چگونه ممکن است. پرسش دوم، بحران است: چرا سازمان‌هایی با اطلاعات کافی، دیر یا غلط معنا می‌سازند و فرو می‌پاشند.",
        "mechanism": "۱. تصرف محیط: اعضا با کنش خود، بخشی از محیط را برمی‌گزینند و همان گزینش، محیط سازمان را می‌سازد.\n۲. گذشته‌نگری: معنا پس از عمل ساخته می‌شود؛ تجربه گذشته، اکنون را قابل فهم می‌کند.\n۳. کاهش ابهام: معناسازی، گزینه‌های بی‌شمار را به تفسیری قابل کنش تقلیل می‌دهد.\n۴. نشانه‌های آشنا: افراد به نشانه‌های در دسترس و آشنا تکیه می‌کنند، نه به همه اطلاعات موجود.\n۵. باورپذیری: روایت کافی و باورپذیر بر روایت دقیق ترجیح می‌یابد؛ دقت بی‌پایان، کنش را فلج می‌کند.\n۶. هویت و اجتماع: معناسازی در گفت‌وگو با دیگران رخ می‌دهد و به تصور اعضا از خودشان گره خورده است.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا یک خبر واحد در دو اتاق خبر تفسیرهای متفاوت می‌سازد، چرا سازمان‌ها در بحران به روایت‌های آشنای پیشین پناه می‌برند و چرا اطلاع‌رسانی بیشتر همیشه فهم بیشتر نمی‌آورد. نکته مهم این است که معناسازی، خطای شناختی نیست؛ سازوکار لازم برای کنش جمعی است.",
        "assumptions": [
            "سازمان، فرایند است نه شیء.",
            "معنا پس از کنش و در گفت‌وگو ساخته می‌شود.",
            "باورپذیری، معیار عملی پذیرش روایت است.",
        ],
        "principles": [
            "ابهام با تفسیر قابل کنش کاهش می‌یابد.",
            "هویت، جهت معناسازی را تعیین می‌کند.",
            "نشانه‌های آشنا بر داده کامل مقدم‌اند.",
        ],
        "critiques": [
            "۱. سنجش دشوار: فرایند معناسازی به‌سختی از بیرون قابل مشاهده است.\n۲. تمرکز بر تفسیر: نقش ساختار مادی و قدرت در محدودکردن تفسیر کم‌رنگ می‌شود.\n۳. خطر توجیه: تأکید بر باورپذیری می‌تواند سوگیری سازمانی را توجیه کند.\n۴. نمونه‌های بحرانی: بسیاری از شواهد از رویدادهای فاجعه‌بار و نمونه‌های محدود می‌آید.\n۵. کم‌توجهی به فناوری: پلتفرم و داده، معناسازی را از گفت‌وگوی انسانی جدا کرده‌اند.",
        ],
        "applications": [
            "مدیریت بحران: طراحی فضای تفسیر مشترک پیش از رویداد.",
            "مطالعات اتاق خبر: تحلیل روال‌های معناسازی خبری.",
            "ارتباطات سازمانی: سنجش فاصله روایت مدیریت و کارکنان.",
            "مدیریت تغییر: پیش‌بینی مقاومت به‌عنوان تفاوت تفسیر، نه نافرمانی.",
        ],
        "evolution": "ویک در ۱۹۶۹ و ۱۹۷۹ سازمان‌دهی را فرایندی از کاهش ابهام صورت‌بندی کرد و در ۱۹۹۵ معناسازی را با هفت ویژگی آن نظام‌مند ساخت. پژوهش بعدی، معناسازی را در بحران، فناوری و سازمان شبکه‌ای گسترد.",
        "key_concepts": [
            "سازمان‌دهی (Organizing)",
            "معناسازی (Sensemaking)",
            "تصرف محیط (Enactment)",
            "کاهش ابهام (Equivocality Reduction)",
            "باورپذیری (Plausibility)",
            "پیوند سست (Loose Coupling)",
        ],
        "studies": [
            "Weick, K. E. (1995). Sensemaking in organizations. Sage.",
            "Weick, K. E. (1979). The social psychology of organizing (2nd ed.). McGraw-Hill.",
        ],
        "theorists": "کارل ویک",
        "theorists_text": "کارل ویک (۱۹۷۹؛ ۱۹۹۵)",
        "year": 1979,
        "model": "چرخه معناسازی: کنش و تصرف محیط → نشانه‌های آشنا → تفسیر گذشته‌نگر و اجتماعی → روایت باورپذیر → کنش هماهنگ → محیط تازه.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nویک سازمان را از ساختار به فرایند منتقل کرد و همین جابه‌جایی، ارتباطات را از ابزار به سازوکار بنیادین سازمان ارتقا داد. نوآوری چارچوب، نشان‌دادن این نکته است که محیط سازمان، تا حدی محصول تفسیر اعضاست.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با تحلیل روایت، نقاط گسست تفسیر و زمان واکنش انجام می‌شود. پژوهشی که تنها ساختار رسمی را می‌خواند، معناسازی را از دست می‌دهد؛ و پژوهشی که تنها مصاحبه می‌کند، روال مادی را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در توضیح شکست اطلاع‌رسانی است، اما باید با تحلیل قدرت تکمیل شود. در محیط پلتفرمی، معناسازی میان انسان و الگوریتم تقسیم شده و همین، پرسش تازه‌ای پیش می‌گذارد.",
        "critique_text": "\n".join([
            "۱. سنجش دشوار: فرایند معناسازی از بیرون قابل مشاهده نیست.",
            "۲. تمرکز بر تفسیر: ساختار مادی و قدرت کم‌رنگ می‌شود.",
            "۳. خطر توجیه: باورپذیری، سوگیری را توجیه می‌کند.",
            "۴. نمونه‌های بحرانی: شواهد از رویدادهای فاجعه‌بار می‌آید.",
            "۵. کم‌توجهی به فناوری: داده، معناسازی را از گفت‌وگو جدا می‌کند.",
        ]),
        "example_text": "در یک بحران سازمانی، تیم حقوقی همان گزارش را «مسئله رویه» می‌خواند و تیم ارتباطات «مسئله اعتماد». هر دو از داده یکسان شروع می‌کنند، اما هویت حرفه‌ای و نشانه‌های آشنا، دو روایت متفاوت می‌سازد و هماهنگی را به تأخیر می‌اندازد.",
    },
    "MC-539": {
        "summary": "(رابرتسون، ۱۹۹۲) رابرتسون جهانی‌شدن را فشرده‌شدن جهان و تشدید آگاهی از جهان به‌عنوان یک کل تعریف کرد. او فرهنگ را نه پیامد فرعی اقتصاد، بلکه بُعدی مستقل دانست و نشان داد جهانی‌شدن، یکسان‌سازی یک‌طرفه نیست: خاص‌گرایی و عام‌گرایی هم‌زمان تقویت می‌شوند. مفهوم کلیدی او، پیوند امر جهانی و امر محلی است؛ جهانی‌شدن نه حذف محلیت، بلکه بازسازی آن در چارچوبی جهانی است.",
        "definition": "نظریه جهانی‌شدن فرهنگی، فرایند فشرده‌شدن جهان و شکل‌گیری آگاهی از آن به‌عنوان یک میدان واحد را تحلیل می‌کند؛ فرایندی که در آن امر جهانی و امر محلی یکدیگر را می‌سازند و فرهنگ، میدان اصلی این بازسازی است.",
        "main_problem": "مسئله این است که آیا جهانی‌شدن به همسانی فرهنگی می‌انجامد یا به تنوع. پاسخ رابرتسون این است که رابطه دوطرفه است: امر جهانی در قالب محلی اجرا می‌شود و امر محلی در چارچوبی جهانی بازتعریف می‌شود. پرسش دوم، قدرت است: چه کسی شرایط این میدان جهانی را تعیین می‌کند.",
        "mechanism": "۱. فشرده‌شدن جهان: افزایش وابستگی متقابل، فاصله و زمان را کوتاه می‌کند و همه را در یک میدان قرار می‌دهد.\n۲. آگاهی از کل: افراد و جوامع، خود را در چارچوبی جهانی تصور می‌کنند و هویت را در همان چارچوب می‌سازند.\n۳. میدان جهانی: رقابت بر سر تعریف جهان مشترک، به میدانی از موقعیت‌ها و روایت‌ها تبدیل می‌شود.\n۴. پیوند جهانی و محلی: امر جهانی فقط در قالب محلی قابل اجراست و امر محلی در نسبت با جهان معنا می‌یابد.\n۵. عام‌گرایی و خاص‌گرایی: هر دو هم‌زمان تقویت می‌شوند؛ نه همسانی کامل، نه جزیره‌ای‌شدن.\n۶. هویت و بنیادگرایی: فشار جهانی‌شدن، هویت‌های مرزبندی‌شده و بنیادگرا را نیز برمی‌انگیزد.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا قالب‌های جهانی تلویزیون در هر کشور بازسازی می‌شوند، چرا موسیقی و سینمای محلی با زبان جهانی رشد می‌کند و چرا مخاطب هم‌زمان محلی و جهانی است. نکته مهم این است که جهانی‌شدن فرهنگی، فرایندی ناهمگون و پرتنش است.",
        "assumptions": [
            "جهان به میدانی واحد و به‌هم‌پیوسته تبدیل شده است.",
            "فرهنگ، بُعدی مستقل از اقتصاد جهانی است.",
            "امر جهانی و امر محلی یکدیگر را شکل می‌دهند.",
        ],
        "principles": [
            "جهانی‌شدن، همسان‌سازی یک‌طرفه نیست.",
            "هر قالب جهانی، در اجرا محلی می‌شود.",
            "هویت در نسبت با چارچوب جهانی بازتعریف می‌شود.",
        ],
        "critiques": [
            "۱. تمرکز بر فرهنگ: نقش نابرابری اقتصادی و قدرت نظامی کم‌رنگ می‌شود.\n۲. ابهام مفهومی: مرز پیوند جهانی و محلی با ترکیب فرهنگی روشن نیست.\n۳. نمونه اروپامحور: شواهد اولیه بیشتر از تجربه غربی می‌آید.\n۴. سنجش دشوار: تقویت هم‌زمان عام و خاص به‌سختی قابل اندازه‌گیری است.\n۵. کم‌توجهی به پلتفرم: جریان داده‌محور امروز، سازوکار قدرت را تغییر داده است.",
        ],
        "applications": [
            "مطالعات رسانه جهانی: تحلیل بازسازی محلی قالب‌های جهانی.",
            "سیاست فرهنگی: حمایت از تولید محلی در بازار جهانی.",
            "هویت و مخاطب: تحلیل مصرف هم‌زمان محلی و جهانی.",
            "دیپلماسی فرهنگی: سنجش تصویر ملی در میدان جهانی.",
        ],
        "evolution": "رابرتسون در ۱۹۹۲ چارچوب جهانی‌شدن را با محوریت فرهنگ صورت‌بندی کرد و در میانه دهه ۱۹۹۰ مفهوم پیوند جهانی و محلی را برجسته ساخت. پژوهش بعدی، جریان‌های فرهنگی جهان، ترکیب فرهنگی و پلتفرم‌های فراملی را به این خط افزود.",
        "key_concepts": [
            "جهانی‌شدن (Globalization)",
            "میدان جهانی (Global Field)",
            "پیوند جهانی و محلی (Glocalization)",
            "فشرده‌شدن جهان (Compression of the World)",
            "عام‌گرایی و خاص‌گرایی (Universalism and Particularism)",
            "جهان به‌عنوان یک کل (World as a Whole)",
        ],
        "studies": [
            "Robertson, R. (1992). Globalization: Social theory and global culture. Sage.",
            "Appadurai, A. (1996). Modernity at large: Cultural dimensions of globalization. University of Minnesota Press.",
        ],
        "theorists": "رولاند رابرتسون",
        "theorists_text": "رولاند رابرتسون (۱۹۹۲)",
        "year": 1992,
        "model": "مدل جهانی‌شدن فرهنگی: فشرده‌شدن جهان + آگاهی از کل → میدان جهانی → پیوند جهانی و محلی → بازسازی هویت و فرهنگ، با تقویت هم‌زمان عام و خاص.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nرابرتسون فرهنگ را از حاشیه به مرکز تحلیل جهانی‌شدن آورد و نشان داد جهان‌شمولی و خاص‌گرایی دو روی یک فرایندند. نوآوری چارچوب، رد همسانی یک‌طرفه و پیشنهاد رابطه دوطرفه جهانی و محلی است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با تحلیل قالب، محتوا و مخاطب در سطح فراملی انجام می‌شود. پژوهشی که تنها جریان کالا را می‌سنجد، بازسازی محلی را از دست می‌دهد؛ و پژوهشی که تنها متن محلی را می‌خواند، چارچوب جهانی را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در توضیح ترکیب فرهنگی است، اما باید با تحلیل قدرت و مالکیت تکمیل شود. در محیط پلتفرمی، جریان جهانی از مسیر الگوریتم می‌گذرد و پرسش از مرکزیت را بازمی‌گرداند.",
        "critique_text": "\n".join([
            "۱. تمرکز بر فرهنگ: نابرابری اقتصادی کم‌رنگ می‌شود.",
            "۲. ابهام مفهومی: مرز پیوند جهانی و محلی روشن نیست.",
            "۳. نمونه اروپامحور: شواهد بیشتر از تجربه غربی است.",
            "۴. سنجش دشوار: تقویت هم‌زمان عام و خاص اندازه‌پذیر نیست.",
            "۵. کم‌توجهی به پلتفرم: جریان داده‌محور قدرت را بازآرایی کرده است.",
        ]),
        "example_text": "نسخه محلی یک مسابقه جهانی، قواعد قالب را نگه می‌دارد اما آیین‌ها و طنز بومی را وارد می‌کند. نتیجه نه کپی محض است و نه سنت دست‌نخورده؛ بازسازی محلی در چارچوبی جهانی است.",
    },
    "MC-568": {
        "summary": "(زیلمان و کانترل، ۱۹۷۷؛ رینی، ۲۰۰۴) نظریه گرایش عاطفی می‌گوید لذت تماشاگر از نمایش، به گرایش او به شخصیت‌ها وابسته است. تماشاگر بر پایه داوری اخلاقی رفتار شخصیت، او را می‌پسندد یا نمی‌پسندد و سپس از سرنوشت او هیجان می‌گیرد: شادی از کامیابی شخصیت محبوب و شادکامی از ناکامی شخصیت منفور. زیلمان و کانترل نشان دادند پاسخ عاطفی تماشاگر، آینه ساده هیجان شخصیت نیست؛ از گرایش او می‌گذرد. همین چارچوب، لذت نمایشی را به داوری اخلاقی گره می‌زند.",
        "definition": "نظریه گرایش عاطفی، چارچوبی است که لذت و هیجان تماشاگر را تابعی از گرایش او به شخصیت‌ها می‌داند؛ گرایشی که از داوری اخلاقی رفتار شخصیت ساخته می‌شود و جهت پاسخ عاطفی به سرنوشت او را تعیین می‌کند.",
        "main_problem": "مسئله این است که چرا تماشاگر از رنج یک شخصیت لذت می‌برد و از رنج دیگری اندوهگین می‌شود. پاسخ در گرایش عاطفی است: داوری اخلاقی، شخصیت را به قطب دوست‌داشتنی یا منفور می‌برد و هیجان تماشاگر را جهت می‌دهد. پرسش دوم، مرز اخلاقی است: چه زمانی لذت از رنج دیگری، پذیرفتنی می‌ماند و چه زمانی به بی‌حسی می‌انجامد.",
        "mechanism": "۱. داوری اخلاقی: تماشاگر رفتار شخصیت را با معیارهای اخلاقی می‌سنجد و بر همان پایه او را می‌پسندد یا رد می‌کند.\n۲. شکل‌گیری گرایش: گرایش، انتظاری درباره سرنوشت مطلوب شخصیت می‌سازد.\n۳. جهت هیجان: کامیابی شخصیت محبوب شادی و کامیابی شخصیت منفور ناخوشایند می‌آورد.\n۴. شادکامی از ناکامی: ناکامی شخصیت منفور، لذتی اخلاقاً موجه می‌سازد که به عدالت نمایشی گره خورده است.\n۵. نظارت اخلاقی: تماشاگر در طول روایت، گرایش خود را بر پایه رفتار تازه شخصیت بازبینی می‌کند.\n۶. شدت و زمینه: شدت لذت به شدت گرایش و میزان توجیه اخلاقی رویداد وابسته است.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا پایان خوش در سریال‌ها رضایت می‌سازد، چرا در ورزش، باخت حریف داوری‌شده لذت می‌آورد و چرا طنز سیاسی با شخصیت‌سازی اخلاقی کار می‌کند. نکته مهم این است که لذت نمایشی، بی‌ارتباط با اخلاق نیست؛ از آن تغذیه می‌کند.",
        "assumptions": [
            "تماشاگر شخصیت‌ها را بر پایه معیار اخلاقی داوری می‌کند.",
            "گرایش عاطفی، جهت هیجان را تعیین می‌کند.",
            "تماشاگر در طول روایت، گرایش خود را بازبینی می‌کند.",
        ],
        "principles": [
            "هیجان تماشاگر از گرایش او می‌گذرد، نه از همدلی محض.",
            "عدالت نمایشی، لذت را موجه می‌سازد.",
            "داوری اخلاقی، شرط ورود به تجربه نمایشی است.",
        ],
        "critiques": [
            "۱. ساده‌سازی داوری: معیار اخلاقی تماشاگر یکسان و ثابت فرض می‌شود.\n۲. نمونه آزمایشگاهی: شواهد اولیه از موقعیت کنترل‌شده و محرک کوتاه می‌آید.\n۳. کم‌توجهی به فرهنگ: تفاوت هنجارهای اخلاقی میان جوامع کم‌رنگ می‌شود.\n۴. شخصیت‌های خاکستری: روایت معاصر با شخصیت چندوجهی، مدل دو قطبی را به چالش می‌کشد.\n۵. پیامد اخلاقی: تأکید بر لذت از ناکامی، خطر عادی‌سازی بی‌حسی را نادیده می‌گیرد.",
        ],
        "applications": [
            "تحلیل درام: پیش‌بینی رضایت مخاطب از سرنوشت شخصیت.",
            "ورزش و هواداری: تحلیل لذت رقابتی و داوری اخلاقی حریف.",
            "طنز سیاسی: طراحی شخصیت منفور و عدالت نمایشی.",
            "آموزش اخلاق رسانه: بازبینی مرز لذت از رنج دیگری.",
        ],
        "evolution": "زیلمان و کانترل در ۱۹۷۷ گرایش عاطفی را با داده تجربی صورت‌بندی کردند و زیلمان در دهه‌های بعد آن را به طنز و نمایش گسترد. رینی در ۲۰۰۴ با افزودن داوری اخلاقی و لذت، چارچوب را برای درام و ورزش بازسازی کرد.",
        "key_concepts": [
            "گرایش عاطفی (Affective Disposition)",
            "نظارت اخلاقی (Moral Monitoring)",
            "لذت نمایشی (Drama Enjoyment)",
            "شادکامی از ناکامی (Schadenfreude)",
            "عدالت نمایشی (Poetic Justice)",
            "همذات‌پنداری (Identification)",
        ],
        "studies": [
            "Zillmann, D., & Cantor, J. R. (1977). Affective responses to the emotions of a protagonist. Journal of Experimental Social Psychology, 13(2), 155-165.",
            "Raney, A. A. (2004). Expanding disposition theory. Communication Theory, 14(4), 348-369.",
        ],
        "theorists": "دولف زیلمان؛ جوان کانترل؛ آرتور رینی",
        "theorists_text": "زیلمان و کانترل (۱۹۷۷)؛ رینی (۲۰۰۴)",
        "year": 1977,
        "model": "زنجیره گرایش: رفتار شخصیت → داوری اخلاقی → گرایش مثبت یا منفی → انتظار سرنوشت → هیجان هم‌سو با گرایش → لذت یا ناخوشنودی نمایشی.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nزیلمان و کانترل پرسش همدلی محض را کنار گذاشتند و نشان دادند پاسخ تماشاگر از گرایش او می‌گذرد. نوآوری چارچوب، پیوند دادن لذت نمایشی با داوری اخلاقی است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با گزارش هیجان، اندازه محبوبیت شخصیت و داوری رفتار انجام می‌شود. پژوهشی که تنها هیجان را می‌سنجد، گرایش را از دست می‌دهد؛ و پژوهشی که تنها محبوبیت را می‌سنجد، جهت هیجان را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در توضیح رضایت از پایان روایت است، اما باید با تحلیل فرهنگی تکمیل شود. در روایت معاصر با شخصیت خاکستری، مدل دو قطبی به بازنگری نیاز دارد.",
        "critique_text": "\n".join([
            "۱. ساده‌سازی داوری: معیار اخلاقی تماشاگر ثابت فرض می‌شود.",
            "۲. نمونه آزمایشگاهی: محرک کوتاه و کنترل‌شده است.",
            "۳. کم‌توجهی به فرهنگ: هنجارهای اخلاقی متفاوت‌اند.",
            "۴. شخصیت خاکستری: مدل دو قطبی محدود است.",
            "۵. پیامد اخلاقی: خطر عادی‌سازی بی‌حسی نادیده می‌ماند.",
        ]),
        "example_text": "در یک سریال، شخصیت منفور که به قهرمان آسیب زده، در پایان رسوا می‌شود و مخاطب رضایت شدیدی گزارش می‌کند. همین رضایت، لذت از رنج نیست؛ اجرای عدالت نمایشی بر پایه داوری اخلاقی است.",
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


NAME_FIX = {
    "MC-533": ("نظریه نقطه‌نظر (دیدگاه‌گرایی)", "Standpoint Theory",
               "canonical_name_fa/en repaired: 'Perspective-Taking' mislabels Harding's standpoint theory (theorist=Harding, 1986)"),
    "MC-568": ("نظریه گرایش عاطفی", "Affective Disposition Theory",
               "canonical_name_fa/en repaired: 'Emotional Disposition' aligned to Zillmann & Cantor's affective disposition theory"),
}


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
            lt = {"work": "SECTION", "page_range": "PAGE", "CHAPTER": "CHAPTER"}.get(src["locator_type"], "SECTION")
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
                                       "verified": n_verified, "batch": 97}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH97 THEORY DONE")


if __name__ == "__main__":
    main()
