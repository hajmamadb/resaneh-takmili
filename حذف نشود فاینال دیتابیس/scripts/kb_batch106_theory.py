# -*- coding: utf-8 -*-
"""Batch 106: full documentation for MC-644, MC-662, MC-663, MC-666."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch106-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch106_theory.json"

S = {
    "MC-644": [
        dict(kind="BOOK",
             title_en="No Sense of Place: The Impact of Electronic Media on Social Behavior",
             title_fa="بی‌حسی مکان: اثر رسانه‌های الکترونیک بر رفتار اجتماعی",
             authors="Meyrowitz, J.", year=1985, publisher="Oxford University Press",
             doi=None, url="https://global.oup.com/academic/product/no-sense-of-place-9780195042313",
             language="en", isbn="978-0-19-503474-5",
             citation="Meyrowitz, J. (1985). No sense of place: The impact of electronic media on social behavior. Oxford University Press.",
             locator="work", locator_type="work",
             supports="media as environments that reshape social situations and identities", verified=True),
        dict(kind="BOOK_CHAPTER",
             title_en="Medium Theory",
             title_fa="نظریه رسانه",
             authors="Meyrowitz, J.", year=1994,
             publisher="Polity Press",
             doi=None, url=None, language="en", isbn=None,
             citation="Meyrowitz, J. (1994). Medium theory. In D. Crowley & D. Mitchell (Eds.), Communication theory today (pp. 50-77). Polity Press.",
             locator="pp. 50-77", locator_type="PAGE",
             supports="systematic statement of medium theory", verified=False),
    ],
    "MC-662": [
        dict(kind="BOOK",
             title_en="Diffusion of Innovations",
             title_fa="پخش نوآوری‌ها",
             authors="Rogers, E. M.", year=2003, publisher="Free Press",
             doi=None, url="https://books.google.com/books/about/Diffusion_of_Innovations_5th_Edition.html?id=9U1K5LjUOwEC",
             language="en", isbn="978-0-7432-2209-9",
             citation="Rogers, E. M. (2003). Diffusion of innovations (5th ed.). Free Press.",
             locator="work", locator_type="work",
             supports="five adopter categories, adoption process and S-curve", verified=True),
        dict(kind="BOOK",
             title_en="Diffusion of Innovations",
             title_fa="پخش نوآوری‌ها",
             authors="Rogers, E. M.", year=1962, publisher="Free Press of Glencoe",
             doi=None, url=None, language="en", isbn=None,
             citation="Rogers, E. M. (1962). Diffusion of innovations. Free Press of Glencoe.",
             locator="work", locator_type="work",
             supports="original formulation of diffusion theory", verified=False),
    ],
    "MC-663": [
        dict(kind="BOOK",
             title_en="Affective Publics: Sentiment, Technology, and Politics",
             title_fa="عموم‌های عاطفی: احساس، فناوری و سیاست",
             authors="Papacharissi, Z.", year=2015, publisher="Oxford University Press",
             doi=None, url="https://global.oup.com/academic/product/affective-publics-9780199999743",
             language="en", isbn="978-0-19-999974-3",
             citation="Papacharissi, Z. (2015). Affective publics: Sentiment, technology, and politics. Oxford University Press.",
             locator="work", locator_type="work",
             supports="affective publics formed through digital storytelling and sentiment", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Affective Publics and Structures of Storytelling",
             title_fa="عموم‌های عاطفی و ساختارهای روایت",
             authors="Papacharissi, Z.", year=2015,
             publisher="Information, Communication & Society",
             doi=None, url="https://zizi.people.uic.edu/Site/Research_files/Papacharissi_Affective%20publics.pdf",
             language="en", isbn=None,
             citation="Papacharissi, Z. (2015). Affective publics and structures of storytelling: Sentiment, events and mediality. Information, Communication & Society, 19(3), 307-324.",
             locator="19(3):307-324", locator_type="page_range",
             supports="storytelling and sentiment as connective structures", verified=False),
    ],
    "MC-666": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="From Data to Wisdom",
             title_fa="از داده تا خرد",
             authors="Ackoff, R. L.", year=1989,
             publisher="Journal of Applied Systems Analysis",
             doi=None, url="https://www.researchgate.net/profile/Rob-Keller/post/Original_paper_of_From_data_to_wisdom_by_Ackoff_1989/attachment/63f67d8997e2867d5081d0de/AS%3A11431281121841684%401677098376991/download/Ackoff89.pdf",
             language="en", isbn=None,
             citation="Ackoff, R. L. (1989). From data to wisdom. Journal of Applied Systems Analysis, 16, 3-9.",
             locator="16:3-9", locator_type="page_range",
             supports="data, information, knowledge, understanding and wisdom hierarchy", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Wisdom Hierarchy: Representations of the DIKW Hierarchy",
             title_fa="سلسله‌مراتب خرد: بازنمایی‌های هرم داده-اطلاعات-دانش-خرد",
             authors="Rowley, J.", year=2007,
             publisher="Journal of Information Science",
             doi=None, url=None, language="en", isbn=None,
             citation="Rowley, J. (2007). The wisdom hierarchy: Representations of the DIKW hierarchy. Journal of Information Science, 33(2), 163-180.",
             locator="33(2):163-180", locator_type="page_range",
             supports="critical review of DIKW definitions and hierarchy", verified=False),
    ],
}

ENRICH = {
    "MC-644": {
        "summary": "(مایروویتز، ۱۹۸۵) نظریه رسانه می‌گوید رسانه‌ها کانال بی‌اثر انتقال پیام نیستند، بلکه محیط‌هایی هستند که موقعیت‌های اجتماعی را بازتعریف می‌کنند. هر رسانه با تغییر مرزهای دیدن و شنیدن، تعیین می‌کند چه کسی در چه موقعیتی حضور دارد. مایروویتز با تکیه بر سنت گافمن و مک‌لوهان نشان داد رسانه الکترونیک، موقعیت‌های مبتنی بر مکان را در هم می‌آمیزد، مرز عمومی و خصوصی را محو می‌کند و سلسله‌مراتب و هویت‌های سنتی مانند کودکی و اقتدار را تغییر می‌دهد. نتیجه، تجربه‌ای است که دیگر با مکان گره نخورده است. این چارچوب، رسانه را محیط تجربه دید، نه ابزار انتقال.",
        "definition": "نظریه رسانه، چارچوبی است که هر رسانه را محیطی اجتماعی می‌داند که با تغییر الگوی دسترسی به اطلاعات، مرز موقعیت‌ها، هویت‌ها و سلسله‌مراتب اجتماعی را بازآرایی می‌کند.",
        "main_problem": "مسئله این است که چرا رسانه‌های نو، رفتار اجتماعی را بی آنکه محتوای خاصی را تبلیغ کنند تغییر می‌دهند. پاسخ، تغییر ساختار موقعیت‌هاست. پرسش دوم، مرز است: چگونه می‌توان اثر رسانه را از اثر محتوا و زمینه اجتماعی جدا کرد.",
        "mechanism": "۱. رسانه به‌عنوان محیط: رسانه، فضای تجربه و دسترسی می‌سازد، نه فقط پیام.\n۲. موقعیت به‌عنوان نظام اطلاعاتی: موقعیت اجتماعی با الگوی دسترسی به اطلاعات تعریف می‌شود.\n۳. درهم‌آمیزی موقعیت‌ها: رسانه الکترونیک مرز صحنه‌های جدا را فرومی‌ریزد.\n۴. محو عمومی و خصوصی: آنچه پشت صحنه بود، به صحنه می‌آید.\n۵. بازآرایی اقتدار: گروه‌هایی که اطلاعات را در انحصار داشتند، انحصار خود را از دست می‌دهند.\n۶. هویت بازساخته: کودکی، جنسیت و نقش‌ها با تجربه رسانه‌ای مشترک بازتعریف می‌شوند.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا تلویزیون مرز خانه و جهان را برداشت، چرا شبکه اجتماعی صحنه‌های شخصی و عمومی را در یک قاب آورد و چرا رهبران دیگر نمی‌توانند اطلاعات را در انحصار نگه دارند. نکته مهم این است که نظریه، رسانه را تعیین‌کننده مطلق نمی‌داند؛ ساختار موقعیت، امکان رفتار تازه می‌سازد، اما انتخاب و زمینه همچنان اثر دارند.",
        "assumptions": [
            "رسانه، محیط اجتماعی می‌سازد.",
            "موقعیت اجتماعی با الگوی دسترسی به اطلاعات تعریف می‌شود.",
            "تغییر رسانه، مرز موقعیت‌ها را تغییر می‌دهد.",
        ],
        "principles": [
            "رسانه فقط کانال نیست.",
            "درهم‌آمیزی موقعیت‌ها، رفتار را تغییر می‌دهد.",
            "ساختار موقعیت، امکان می‌سازد نه جبر.",
        ],
        "critiques": [
            "۱. جبر فناورانه: اثر رسانه از محتوا و زمینه جدا فرض می‌شود.\n۲. تعمیم: ادعاهای گسترده با شواهد محدود آزموده شده‌اند.\n۳. سنجش: موقعیت اجتماعی و مرز آن سخت عملیاتی می‌شود.\n۴. زمان: نمونه‌های تلویزیونی با رسانه شبکه‌ای یکسان نیست.\n۵. محتوا: نقش پیام و ژانر کم‌تر دیده می‌شود.",
        ],
        "applications": [
            "تحلیل رسانه شبکه‌ای: بازتعریف مرز عمومی و خصوصی.",
            "مطالعه اقتدار: تغییر دسترسی به اطلاعات و اعتماد.",
            "سواد رسانه‌ای: شناخت محیط رسانه‌ای به‌جای محتوای تنها.",
            "طراحی سیاست: ارزیابی اثر محیط اطلاعاتی بر رفتار.",
        ],
        "evolution": "مایروویتز در ۱۹۸۵ چارچوب را در کتاب بی‌حسی مکان عرضه کرد و در ۱۹۹۴ صورت‌بندی نظام‌مند آن را ارائه داد. بعدها پژوهش رسانه شبکه‌ای، مفهوم موقعیت و مرز را به تعامل آنلاین و حریم خصوصی گسترد.",
        "key_concepts": [
            "نظریه رسانه (Medium Theory)",
            "رسانه به‌عنوان محیط (Media as Environment)",
            "موقعیت اجتماعی (Social Situation)",
            "درهم‌آمیزی موقعیت‌ها (Situation Merging)",
            "مرز عمومی و خصوصی (Public-Private Boundary)",
            "هویت رسانه‌ای (Mediated Identity)",
        ],
        "studies": [
            "Meyrowitz, J. (1985). No sense of place. Oxford University Press.",
            "Meyrowitz, J. (1994). Medium theory. In Communication theory today (pp. 50-77). Polity Press.",
        ],
        "theorists": "جاشوا مایروویتز",
        "theorists_text": "مایروویتز (۱۹۸۵؛ ۱۹۹۴)",
        "year": 1985,
        "model": "رسانه به‌عنوان محیط → تغییر الگوی دسترسی به اطلاعات → درهم‌آمیزی موقعیت‌ها → بازآرایی مرز عمومی/خصوصی، اقتدار و هویت.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nمایروویتز سنت موقعیت‌شناسی گافمن را با سنت رسانه‌شناسی مک‌لوهان ترکیب کرد. نوآوری چارچوب، تعریف موقعیت اجتماعی بر پایه الگوی اطلاعاتی است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با تحلیل تاریخی مرز موقعیت‌ها، مطالعه رفتار گروه‌ها و مقایسه رسانه‌ها انجام می‌شود. پژوهشی که تنها محتوا را می‌سنجد، محیط را از دست می‌دهد؛ و پژوهشی که رسانه را تعیین‌کننده مطلق می‌داند، انتخاب و زمینه را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در تحلیل محیط اطلاعاتی است، اما باید با مطالعه محتوا تکمیل شود. محیط بی محتوا، به جبرگرایی فناورانه بدل می‌شود.",
        "critique_text": "\n".join([
            "۱. جبر فناورانه: اثر رسانه از محتوا جدا فرض می‌شود.",
            "۲. تعمیم: شواهد محدود برای ادعای گسترده.",
            "۳. سنجش: عملیاتی‌سازی موقعیت دشوار است.",
            "۴. زمان: نمونه تلویزیونی با رسانه شبکه‌ای یکسان نیست.",
            "۵. محتوا: نقش پیام کم‌تر دیده می‌شود.",
        ]),
        "example_text": "والدینی که پیش از تلویزیون می‌توانستند اطلاعات را از کودکان پنهان کنند، با ورود تلویزیون این انحصار را از دست دادند؛ مرز موقعیت کودکی و بزرگسالی در همان محیط اطلاعاتی مشترک فروریخت.",
    },
    "MC-662": {
        "summary": "(راجرز، ۱۹۶۲) نظریه پخش نوآوری توضیح می‌دهد چگونه ایده، فناوری یا رفتار تازه در یک نظام اجتماعی منتشر می‌شود. راجرز چهار عنصر را تفکیک می‌کند: نوآوری، کانال‌های ارتباطی، زمان و نظام اجتماعی. فرایند تصمیم پذیرش پنج مرحله دارد: دانش، اقناع، تصمیم، اجرا و تأیید. پذیرندگان در پنج دسته نوآوران تا واپس‌ماندگان جای می‌گیرند و منحنی پذیرش تجمعی، شکل S دارد. پنج ویژگی ادراک‌شده نوآوری، سرعت پذیرش را تعیین می‌کند: مزیت نسبی، سازگاری، پیچیدگی، آزمون‌پذیری و مشاهده‌پذیری. بازآفرینی نوآوری نیز بخشی از فرایند است. پخش در نظام اجتماعی بی‌خنثی نیست؛ ساختار قدرت و دسترسی، مسیر آن را تعیین می‌کند. این نظریه، پایه برنامه‌های پذیرش فناوری و ارتباطات سلامت شد. نوآوری مردود نیز بخشی از داده پخش است و باید در تحلیل ثبت شود.",
        "definition": "پخش نوآوری، فرایندی است که در آن نوآوری از طریق کانال‌های ارتباطی در طول زمان میان اعضای یک نظام اجتماعی منتشر می‌شود و به پذیرش، بازآفرینی یا رد آن می‌انجامد.",
        "main_problem": "مسئله این است که چرا نوآوری مفید سریع پذیرفته نمی‌شود. پاسخ، ویژگی‌های نوآوری، کانال و ساختار اجتماعی است. پرسش دوم، عدالت است: آیا پخش، شکاف میان پذیرندگان سریع و کند را کم می‌کند یا عمیق‌تر می‌سازد.",
        "mechanism": "۱. نوآوری: ایده یا ابزار تازه با ویژگی‌های ادراک‌شده مشخص.\n۲. کانال ارتباطی: رسانه جمعی برای آگاهی و ارتباط میان‌فردی برای اقناع.\n۳. زمان: فرایند تصمیم و منحنی پذیرش در زمان شکل می‌گیرد.\n۴. نظام اجتماعی: هنجارها، رهبران نظر و ساختار، سرعت پخش را می‌سازند.\n۵. پنج ویژگی: مزیت نسبی، سازگاری، پیچیدگی، آزمون‌پذیری و مشاهده‌پذیری.\n۶. بازآفرینی: پذیرنده نوآوری را با نیاز خود تغییر می‌دهد و پخش را غنی می‌کند.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا ابزار تحریریه‌ای که سازگاری کم دارد کند پذیرفته می‌شود، چرا خبرنگاران پیشرو و پسرو در پذیرش فناوری تفاوت دارند و چرا پخش خبر از منحنی S پیروی می‌کند. نکته مهم این است که نظریه به پذیرش نوآوری جهت داده است؛ سوگیری نوآوری‌محور می‌تواند رد آگاهانه و نابرابری دسترسی را نادیده بگیرد.",
        "assumptions": [
            "نوآوری در طول زمان پخش می‌شود.",
            "پذیرش، فرایندی تصمیم‌گیرانه است.",
            "نظام اجتماعی، سرعت پخش را تعیین می‌کند.",
        ],
        "principles": [
            "مزیت نسبی و سازگاری، پذیرش را تسریع می‌کند.",
            "رسانه جمعی آگاهی و ارتباط میان‌فردی اقناع می‌سازد.",
            "منحنی پذیرش، شکل S دارد.",
        ],
        "critiques": [
            "۱. سوگیری نوآوری: فرض می‌شود نوآوری خوب است.\n۲. سرزنش فرد: پذیرش‌نکردن به کمبود فرد نسبت داده می‌شود.\n۳. خطای یادآوری: داده پخش بر گزارش گذشته تکیه دارد.\n۴. خطی‌بودن: فرایند همیشه پنج‌مرحله‌ای نیست.\n۵. نابرابری: دسترسی و قدرت ساختاری کم‌تر دیده می‌شود.",
        ],
        "applications": [
            "پذیرش فناوری در تحریریه: تحلیل سازگاری و آزمون‌پذیری.",
            "کمپین سلامت: ترکیب رسانه جمعی و رهبران نظر.",
            "خبر موبایلی: تحلیل منحنی پذیرش مخاطب.",
            "پخش راستی‌آزمایی: شناخت کانال‌های اقناع.",
        ],
        "evolution": "راجرز در ۱۹۶۲ نظریه را عرضه کرد و در ویرایش‌های بعدی آن را گسترد؛ ویرایش پنجم در ۲۰۰۳ جامع‌ترین صورت آن است. بعدها پژوهش شبکه، پخش دیجیتال و بازآفرینی، چارچوب را به رسانه نو گستراند.",
        "key_concepts": [
            "نوآوری (Innovation)",
            "پذیرنده پیشرو (Early Adopter)",
            "منحنی پذیرش (Adoption Curve)",
            "مزیت نسبی (Relative Advantage)",
            "بازآفرینی (Reinvention)",
            "رهبر نظر (Opinion Leader)",
        ],
        "studies": [
            "Rogers, E. M. (1962). Diffusion of innovations. Free Press of Glencoe.",
            "Rogers, E. M. (2003). Diffusion of innovations (5th ed.). Free Press.",
        ],
        "theorists": "اورت راجرز",
        "theorists_text": "راجرز (۱۹۶۲؛ ۲۰۰۳)",
        "year": 1962,
        "model": "نوآوری + کانال + زمان + نظام اجتماعی → پنج مرحله تصمیم → پنج دسته پذیرنده → منحنی S پذیرش.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nراجرز پخش را فرایند اجتماعی و ارتباطی دید، نه رویدادی فنی. نوآوری چارچوب، پیوند ویژگی‌های نوآوری با ساختار اجتماعی است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با داده پذیرش در زمان، مصاحبه پذیرندگان و تحلیل شبکه انجام می‌شود. پژوهشی که تنها پذیرش نهایی را می‌سنجد، فرایند تصمیم را از دست می‌دهد؛ و پژوهشی که نوآوری را خوب فرض می‌کند، رد آگاهانه را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در برنامه‌ریزی پذیرش است، اما باید با تحلیل نابرابری تکمیل شود. پخش بی عدالت، شکاف دیجیتال را عمیق می‌کند.",
        "critique_text": "\n".join([
            "۱. سوگیری نوآوری: نوآوری خوب فرض می‌شود.",
            "۲. سرزنش فرد: نابرابری به فرد نسبت داده می‌شود.",
            "۳. خطای یادآوری: داده گذشته سوگیرانه است.",
            "۴. خطی‌بودن: فرایند همیشه پنج‌مرحله‌ای نیست.",
            "۵. نابرابری: دسترسی ساختاری کم دیده می‌شود.",
        ]),
        "example_text": "تحریریه‌ای ابزار نگارش مشترک تازه را می‌آزماید؛ خبرنگاران پیشرو در دو هفته می‌پذیرند، اما گروهی با پیچیدگی ابزار و ناسازگاری با گردش کار موجود مقاومت می‌کنند تا نسخه ساده‌تر عرضه شود.",
    },
    "MC-663": {
        "summary": "(پاپاچاریسی، ۲۰۱۵) عموم‌های عاطفی، اجتماع‌هایی هستند که از راه بیان احساس در رسانه‌های شبکه‌ای شکل می‌گیرند. پاپاچاریسی نشان می‌دهد هشتگ و روایت دیجیتال، افراد پراکنده را با ساختارهای نرم احساس به هم پیوند می‌دهد؛ پیوندی که پیش از سازمان‌یابی رسمی، همبستگی می‌سازد. این عموم‌ها با روایت، احساس و توجه مشترک فعال می‌شوند و نه صرفاً با استدلال عقلانی. کتاب با مطالعه جنبش‌های اعتراضی در شبکه‌های اجتماعی، مفهوم عموم عاطفی را از عموم عقلانی هابرماسی جدا می‌کند. عاطفه در این چارچوب، مانع سیاست نیست؛ ماده خام مشارکت سیاسی است. عموم عاطفی، شکل ضعیف حوزه عمومی نیست؛ شکل دیگری از سیاست است که رسانه باید آن را بشناسد. پایداری آن به سازماندهی بعدی وابسته است.",
        "definition": "عموم عاطفی، اجتماعی شبکه‌ای است که از راه بیان و گردش احساس و روایت در سکوهای دیجیتال شکل می‌گیرد و پیش از سازمان‌یابی رسمی، همبستگی و توجه مشترک می‌سازد.",
        "main_problem": "مسئله این است که چرا جنبش‌های شبکه‌ای بی سازمان رسمی، همبستگی می‌سازند. پاسخ، ساختارهای نرم احساس و روایت است. پرسش دوم، پایداری است: آیا عموم عاطفی می‌تواند به کنش پایدار بدل شود یا در موج احساسی فرو می‌پاشد.",
        "mechanism": "۱. بیان احساس: کاربران تجربه و خشم و امید خود را عمومی می‌کنند.\n۲. روایت مشترک: داستان‌ها، تجربه‌های پراکنده را به هم می‌بافند.\n۳. هشتگ و سکو: نشانه مشترک، گردش محتوا را ممکن می‌کند.\n۴. ساختار نرم احساس: پیوند بدون سازمان رسمی، همبستگی می‌سازد.\n۵. توجه مشترک: موج توجه، کنش هم‌زمان را ممکن می‌کند.\n۶. فعال‌سازی و افول: عموم با موج شکل می‌گیرد و با فروکش توجه پراکنده می‌شود.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا یک هشتگ در ساعاتی به همبستگی عمومی بدل می‌شود، چرا رسانه خبری با روایت عاطفی مشارکت را زیاد می‌کند و چرا موج همدلی بی سازمان پایدار نمی‌ماند. نکته مهم این است که عاطفه در این چارچوب برابر بی‌خردی نیست؛ اما تحلیل بی‌احتیاط آن می‌تواند سیاست عاطفی را به دستکاری احساس فروکاست.",
        "assumptions": [
            "احساس، پیوند اجتماعی می‌سازد.",
            "روایت، تجربه‌های پراکنده را به هم می‌بندد.",
            "عموم می‌تواند پیش از سازمان رسمی شکل بگیرد.",
        ],
        "principles": [
            "عاطفه ماده خام مشارکت است.",
            "روایت، ساختار نرم همبستگی می‌سازد.",
            "توجه موج‌دار، فعال‌سازی و افول دارد.",
        ],
        "critiques": [
            "۱. دوگانه عقل/عاطفه: مرز عموم عقلانی و عاطفی ساده‌سازی می‌شود.\n۲. پایداری: موج عاطفی لزوماً به کنش پایدار نمی‌رسد.\n۳. نمونه: مطالعه بر جنبش‌های خاص و غربی متمرکز است.\n۴. سنجش: احساس از متن و هشتگ به‌طور کامل خوانده نمی‌شود.\n۵. پوپولیسم: سیاست عاطفی می‌تواند به تحریک بدل شود.",
        ],
        "applications": [
            "تحلیل جنبش هشتگی: شناخت روایت و ساختار احساس.",
            "ارتباطات بحران: مدیریت موج همدلی و اعتماد.",
            "مخاطب‌شناسی: تحلیل مشارکت عاطفی مخاطب.",
            "اخلاق رسانه: پرهیز از تحریک احساس بی روایت.",
        ],
        "evolution": "پاپاچاریسی مفهوم را در کتاب ۲۰۱۵ صورت‌بندی کرد و در مقاله‌ای ساختارهای روایت را گسترد. بعدها پژوهش جنبش دیجیتال، عاطفه سیاسی و اقتصاد توجه، چارچوب را به تحلیل پلتفرم و ماندگاری کنش گره زد.",
        "key_concepts": [
            "عموم عاطفی (Affective Public)",
            "ساختار احساس (Structure of Feeling)",
            "روایت دیجیتال (Digital Storytelling)",
            "همبستگی شبکه‌ای (Networked Solidarity)",
            "توجه مشترک (Shared Attention)",
            "کنش پیوندی (Connective Action)",
        ],
        "studies": [
            "Papacharissi, Z. (2015). Affective publics. Oxford University Press.",
            "Papacharissi, Z. (2015). Affective publics and structures of storytelling. Information, Communication & Society, 19(3), 307-324.",
        ],
        "theorists": "زیزی پاپاچاریسی",
        "theorists_text": "پاپاچاریسی (۲۰۱۵)",
        "year": 2015,
        "model": "بیان احساس → روایت مشترک → گردش هشتگی → ساختار نرم همبستگی → توجه و کنش هم‌زمان → فعال‌سازی یا افول.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nپاپاچاریسی عموم را از حوزه عمومی عقلانی جدا کرد و عاطفه را سازنده پیوند دید. نوآوری چارچوب، پیوند مطالعات جنبش با نظریه احساس است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با تحلیل هشتگ، روایت و مصاحبه کنشگران انجام می‌شود. پژوهشی که تنها شمار توییت را می‌سنجد، معنا را از دست می‌دهد؛ و پژوهشی که هر موج را جنبش پایدار می‌خواند، افول را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در تحلیل همبستگی شبکه‌ای است، اما باید با داده سازمان و پیامد تکمیل شود. عاطفه بی روایت، به تحریک تبلیغاتی بدل می‌شود.",
        "critique_text": "\n".join([
            "۱. دوگانه عقل/عاطفه: مرز ساده‌سازی می‌شود.",
            "۲. پایداری: موج به کنش پایدار نمی‌رسد.",
            "۳. نمونه: تمرکز بر جنبش‌های خاص.",
            "۴. سنجش: احساس از متن کامل خوانده نمی‌شود.",
            "۵. پوپولیسم: سیاست عاطفی به تحریک بدل می‌شود.",
        ]),
        "example_text": "هشتگی برای همدلی با قربانیان یک رویداد در چند ساعت شکل می‌گیرد؛ کاربران با روایت شخصی و تصویر، توجه عمومی می‌سازند، اما بی ساختار سازمانی، موج پس از چند روز فروکش می‌کند.",
    },
    "MC-666": {
        "summary": "(آکوف، ۱۹۸۹) هرم دانش، سلسله‌مراتبی از داده، اطلاعات، دانش، فهم و خرد را ترسیم می‌کند. داده، نماد خام است؛ اطلاعات، داده پردازش‌شده‌ای است که به پرسش چه، کجا و چه‌ زمانی پاسخ می‌دهد؛ دانش، دانستن چگونه است؛ فهم، دانستن چرا؛ و خرد، ارزیابی ارزشمند فهم است. آکوف این سلسله‌مراتب را نه فقط انباشت، بلکه افزایش معناداری و ارزش می‌دید. این هرم در مدیریت دانش و سواد اطلاعاتی به چارچوبی رایج بدل شد. با این حال، مرز مراحل و خطی‌بودن آن مورد نقد است. در داده‌نگاری و تحلیل رسانه، هرم به پرسش از کیفیت داده تا تصمیم کمک می‌کند. این هرم، پرسش از ارزش داده را پیش از انباشت آن مطرح می‌کند. نقدها اما، آن را به الگویی آموزشی فروکاسته‌اند که باید با احتیاط به کار رود.",
        "definition": "هرم دانش، سلسله‌مراتبی است که داده خام را با پردازش به اطلاعات، با یادگیری به دانش، با تبیین به فهم و با ارزش‌داوری به خرد پیوند می‌دهد و هر پله را افزودن معنا و ارزش می‌داند.",
        "main_problem": "مسئله این است که چرا داده بیشتر، تصمیم بهتر نمی‌سازد. پاسخ، تفاوت داده با دانش و خرد است. پرسش دوم، سنجش است: چگونه می‌توان فهم و خرد را از داده و اطلاعات جدا کرد بی آنکه به داوری شخصی فروکاسته شود.",
        "mechanism": "۱. داده: نمادهای خام بی زمینه.\n۲. اطلاعات: داده دسته‌بندی و پردازش‌شده با معنا.\n۳. دانش: دانستن چگونه انجام دادن و کاربرد.\n۴. فهم: دانستن چرا و شناخت رابطه‌ها.\n۵. خرد: ارزش‌داوری و انتخاب هدف درست.\n۶. بازخورد: خرد با پرسش تازه، داده و اطلاعات نو می‌طلبد.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا داشبورد تحلیلی پر از عدد، تصمیم سرمقاله نمی‌سازد، چرا خبرنگار داده باید از رقم به معنا و از معنا به ارزش برسد و چرا سواد اطلاعاتی، فراتر از جست‌وجوی منبع است. نکته مهم این است که هرم، مسیر خطی اجباری نیست؛ در عمل، تصمیم و پرسش ارزشی بر گردآوری داده اثر می‌گذارد و مراحل در هم می‌آمیزند.",
        "assumptions": [
            "داده، اطلاعات، دانش، فهم و خرد متمایزند.",
            "هر پله، معنا و ارزش افزوده می‌سازد.",
            "تصمیم بهتر به پله‌های بالاتر نیاز دارد.",
        ],
        "principles": [
            "داده بی زمینه، معنا ندارد.",
            "دانش، چگونه را می‌گوید.",
            "خرد، انتخاب ارزشی می‌سازد.",
        ],
        "critiques": [
            "۱. خطی‌بودن: مراحل در عمل در هم می‌آمیزند.\n۲. مرز مبهم: تفکیک دانش و فهم و خرد روشن نیست.\n۳. سنجش: خرد و فهم سخت اندازه‌گیری می‌شوند.\n۴. قدرت: نقش منافع و زمینه در تولید دانش نادیده می‌ماند.\n۵. جایگزین‌ها: مدل‌های حسی و بوم‌شناختی، سلسله‌مراتب را نقد می‌کنند.",
        ],
        "applications": [
            "داده‌نگاری: حرکت از عدد به معنا و ارزش خبری.",
            "مدیریت دانش: طراحی انتقال دانش در سازمان رسانه‌ای.",
            "سواد اطلاعاتی: آموزش ارزیابی و کاربرد اطلاعات.",
            "طراحی داشبورد: پرهیز از انباشت داده بی تصمیم.",
        ],
        "evolution": "آکوف در ۱۹۸۹ سلسله‌مراتب را در مقاله از داده تا خرد عرضه کرد. بعدها مدیریت دانش و علم اطلاعات آن را به هرم داده-اطلاعات-دانش-خرد بدل کردند و پژوهش‌های نقدی، خطی‌بودن و مرز مراحل را به پرسش گرفتند.",
        "key_concepts": [
            "داده (Data)",
            "اطلاعات (Information)",
            "دانش (Knowledge)",
            "فهم (Understanding)",
            "خرد (Wisdom)",
            "سلسله‌مراتب دانش (Knowledge Hierarchy)",
        ],
        "studies": [
            "Ackoff, R. L. (1989). From data to wisdom. Journal of Applied Systems Analysis, 16, 3-9.",
            "Rowley, J. (2007). The wisdom hierarchy. Journal of Information Science, 33(2), 163-180.",
        ],
        "theorists": "راسل آکوف",
        "theorists_text": "آکوف (۱۹۸۹)",
        "year": 1989,
        "model": "داده → اطلاعات (چه/کجا/چه‌ زمانی) → دانش (چگونه) → فهم (چرا) → خرد (ارزش‌داوری)؛ هر پله افزودن معنا.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nآکوف سلسله‌مراتب را از تحلیل سیستم‌های اطلاعاتی ساخت و آن را ابزار تصمیم دید. نوآوری چارچوب، افزودن فهم و خرد به زنجیره داده و اطلاعات است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با تحلیل کیفیت داده، کاربرد و تصمیم انجام می‌شود. پژوهشی که تنها حجم داده را می‌سنجد، معنا را از دست می‌دهد؛ و پژوهشی که خرد را با تجربه یکی می‌گیرد، ارزش‌داوری را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در سواد داده است، اما باید با تحلیل قدرت تکمیل شود. داده بی پرسش ارزشی، به انبار بی تصمیم بدل می‌شود.",
        "critique_text": "\n".join([
            "۱. خطی‌بودن: مراحل در هم می‌آمیزند.",
            "۲. مرز مبهم: دانش و فهم و خرد جدا نمی‌شوند.",
            "۳. سنجش: فهم و خرد اندازه‌پذیر نیستند.",
            "۴. قدرت: منافع در تولید دانش نادیده می‌ماند.",
            "۵. جایگزین‌ها: مدل‌های بوم‌شناختی سلسله‌مراتب را نقد می‌کنند.",
        ]),
        "example_text": "تحریریه‌ای داده بازدید صفحه را جمع می‌کند؛ عدد خام بی معناست، تحلیل روند اطلاعات می‌سازد، شناخت رفتار مخاطب دانش می‌آورد و تصمیم درباره ارزش خبری، خرد تحریریه را می‌آزماید.",
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
    "MC-644": ("نظریه رسانه (نظریه رسانه‌ها)", "Medium Theory",
               "canonical_name repaired: 'Media State Relations' was a mislabel; entity is Meyrowitz's medium theory of media as social environments"),
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
                                       "verified": n_verified, "batch": 106}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH106 THEORY DONE")


if __name__ == "__main__":
    main()
