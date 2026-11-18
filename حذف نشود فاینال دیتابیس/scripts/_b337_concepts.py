# -*- coding: utf-8 -*-
"""Batch 337: CPT-216..220 (Behavior Change, Source Attractiveness, Source Expertise, Emotional Appeal, Rational Appeal)."""
import json
import importlib.util
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch337-20261117"
NOW = "2026-11-17 00:00:00"
BATCH = 337
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch337.json"

S = {
    "CPT-216": [
        dict(kind="BOOK", title_fa="باور، نگرش، قصد و رفتار", title_en="Belief, attitude, intention, and behavior",
             year=1975, publisher="Addison-Wesley", doi=None, isbn="9780201056922", url=None, language="en",
             authors="Fishbein, Martin; Ajzen, Icek",
             citation="Fishbein, M., & Ajzen, I. (1975). Belief, attitude, intention, and behavior: An introduction to theory and research. Addison-Wesley.",
             locator_type="CHAPTER", locator="ch. 4", verified=True,
             supports="فرایند تغییر رفتار از روی باور، نگرش و قصد."),
        dict(kind="BOOK", title_fa="بنیان‌های اجتماعی تفکر و عمل", title_en="Social foundations of thought and action",
             year=1986, publisher="Prentice-Hall", doi=None, isbn="9780138421845", url=None, language="en",
             authors="Bandura, Albert",
             citation="Bandura, A. (1986). Social foundations of thought and action: A social cognitive theory. Prentice-Hall.",
             locator_type="CHAPTER", locator="ch. 4", verified=True,
             supports="خودتنظیمی و تغییر رفتار از طریق خودکارآمدی و مدل‌سازی."),
    ],
    "CPT-217": [
        dict(kind="BOOK", title_fa="ارتباط و اقناع: مطالعات روان‌شناختی تغییر نظر", title_en="Communication and persuasion",
             year=1969, publisher="MIT Press", doi=None, isbn="9780262540194", url=None, language="en",
             authors="Hovland, Carl I.; West, Peter R.; Weinstein, Arthur",
             citation="Hovland, C. I., West, P. R., & Weinstein, A. (1969). Communication and persuasion: Psychological studies of opinion change (rev. ed.). MIT Press.",
             locator_type="CHAPTER", locator="ch. 6", verified=True,
             supports="جذابیت منبع به‌عنوان عامل اقناع و تغییر نگرش."),
        dict(kind="BOOK", title_fa="ارتباط و اقناع: مسیرهای مرکزی و محیطی", title_en="Communication and persuasion: Central and peripheral routes to attitude change",
             year=1986, publisher="Springer-Verlag", doi=None, isbn="9780387904254", url=None, language="en",
             authors="Petty, Richard E.; Cacioppo, John T.",
             citation="Petty, R. E., & Cacioppo, J. T. (1986). Communication and persuasion: Central and peripheral routes to attitude change. Springer-Verlag.",
             locator_type="CHAPTER", locator="ch. 4", verified=True,
             supports="جذابیت منبع به‌عنوان یه‌کنندۀ مسیر محیطی اقناع."),
    ],
    "CPT-218": [
        dict(kind="BOOK", title_fa="ارتباط و اقناع: مطالعات روان‌شناختی تغییر نظر", title_en="Communication and persuasion",
             year=1969, publisher="MIT Press", doi=None, isbn="9780262540194", url=None, language="en",
             authors="Hovland, Carl I.; West, Peter R.; Weinstein, Arthur",
             citation="Hovland, C. I., West, P. R., & Weinstein, A. (1969). Communication and persuasion: Psychological studies of opinion change (rev. ed.). MIT Press.",
             locator_type="CHAPTER", locator="ch. 5", verified=True,
             supports="تخصص منبع به‌عنوان مؤلفهٔ اعتبار و اقناع."),
        dict(kind="JOURNAL_ARTICLE", title_fa="نگرش‌ها و تغییر نگرش", title_en="Attitudes and attitude change",
             year=1985, publisher="Annual Review of Psychology", doi="10.1146/annurev.ps.36.020185.002441", isbn=None, url=None, language="en",
             authors="McGuire, William J.",
             citation="McGuire, W. J. (1985). Attitudes and attitude change. Annual Review of Psychology, 36, 491-514.",
             locator_type="SECTION", locator="p. 493-505", verified=True,
             supports="اعتبار منبع و تخصص در فرایند تغییر نگرش."),
    ],
    "CPT-219": [
        dict(kind="BOOK", title_fa="ارتباط و اقناع: مسیرهای مرکزی و محیطی", title_en="Communication and persuasion: Central and peripheral routes to attitude change",
             year=1986, publisher="Springer-Verlag", doi=None, isbn="9780387904254", url=None, language="en",
             authors="Petty, Richard E.; Cacioppo, John T.",
             citation="Petty, R. E., & Cacioppo, J. T. (1986). Communication and persuasion: Central and peripheral routes to attitude change. Springer-Verlag.",
             locator_type="CHAPTER", locator="ch. 5", verified=True,
             supports="جاذبه عاطفی و پردازش هیجانی در فرایند اقناع."),
        dict(kind="BOOK", title_fa="ارتباط و اقناع: مطالعات روان‌شناختی تغییر نظر", title_en="Communication and persuasion",
             year=1969, publisher="MIT Press", doi=None, isbn="9780262540194", url=None, language="en",
             authors="Hovland, Carl I.; West, Peter R.; Weinstein, Arthur",
             citation="Hovland, C. I., West, P. R., & Weinstein, A. (1969). Communication and persuasion: Psychological studies of opinion change (rev. ed.). MIT Press.",
             locator_type="CHAPTER", locator="ch. 8", verified=True,
             supports="القای عاطفی و ترس به‌عنوان عامل تغییر نگرش."),
    ],
    "CPT-220": [
        dict(kind="BOOK", title_fa="ارتباط و اقناع: مسیرهای مرکزی و محیطی", title_en="Communication and persuasion: Central and peripheral routes to attitude change",
             year=1986, publisher="Springer-Verlag", doi=None, isbn="9780387904254", url=None, language="en",
             authors="Petty, Richard E.; Cacioppo, John T.",
             citation="Petty, R. E., & Cacioppo, J. T. (1986). Communication and persuasion: Central and peripheral routes to attitude change. Springer-Verlag.",
             locator_type="CHAPTER", locator="ch. 3", verified=True,
             supports="جاذبه عقلانی و استدلال به‌عنوان هستۀ مسیر مرکزی اقناع."),
        dict(kind="BOOK", title_fa="ارتباط و اقناع: مطالعات روان‌شناختی تغییر نظر", title_en="Communication and persuasion",
             year=1969, publisher="MIT Press", doi=None, isbn="9780262540194", url=None, language="en",
             authors="Hovland, Carl I.; West, Peter R.; Weinstein, Arthur",
             citation="Hovland, C. I., West, P. R., & Weinstein, A. (1969). Communication and persuasion: Psychological studies of opinion change (rev. ed.). MIT Press.",
             locator_type="CHAPTER", locator="ch. 7", verified=True,
             supports="محتوای استدلالی و منطق در تغییر نگرش."),
    ],
}

ENRICH = {
    "CPT-216": dict(
        summary="تغییر رفتار (Behavior Change) به فرایند تغییر پایدار یا ناپایدار در الگوهای عملکردی، عادت‌ها و کنش‌های فرد در برابر محرک‌ها، زمینه‌ها و موقعیت‌ها می‌گویند؛ یعنی «از رفتار قدیم به رفتار جدید». در سنت روان‌شناسی اجتماعی و شناختی، تغییر رفتار بر ویژگی‌هایی چون: (۱) هدفمند: تغییر، به رفتار مشخص و در زمینه‌ای معین مربوط است؛ (۲) چندعاملی: تغییر، از باور، نگرش، قصد، انگیزه و کنترل درک‌شده شکل می‌گیرد؛ (۳) فرایندی: تغییر، در مراحل آگاهی، قصد، اجرا و تثبیت، رخ می‌دهد؛ (۴) زمینه‌ای: تغییر، به منابع، موانع و بستر بستگی دارد (Fishbein & Ajzen, 1975; Bandura, 1986). در سنت خودتنظیمی، تغییر رفتار، از طریق خودکارآمدی، مدل‌سازی و بازخورد شکل می‌گیرد (Bandura, 1986). پژوهش‌ها نشان می‌دهند تغییر رفتار بر «سلامت»، «مشارکت اجتماعی» و «مصرف» اثر عمیق دارد. نمونه‌های رایج تغییر رفتار: تغییر عادت‌های سلامت، رفتار مصرفی، رفتار رسانه‌ای (کاهش زمان صفحه‌نمایش)، و رفتار محیط‌زیستی. نقد بنیادین، «تغییررفتاری‌زدگی» (behavior-change-ism) است: فرض بر این است که تغییر رفتار، «همیشه پایدار و قابل تعمیم» است، در حالی که در واقع آن، «زمینه‌ای و ناپایدار» است و تفاوت، «درجه‌ای» است نه «ماهوی» (Bandura, 1986).",
        mechanism="تغییر رفتار در چهار حلقه عمل می‌کند: (۱) آگاهی و انگیزه: فرد، آگاهی و انگیزه برای تغییر می‌یابد؛ (۲) شکل‌گیری قصد: بر پایه باور، نگرش و کنترل درک‌شده، قصد رفتاری شکل می‌گیرد؛ (۳) اجرا: رفتار جدید، در زمینه مناسب، اجرا می‌شود؛ (۴) تثبیت و بازخورد: با خودتنظیمی، تقویت و بازخورد، رفتار جدید، پایدار و عادت می‌شود (Fishbein & Ajzen, 1975; Bandura, 1986). این چرخه، تغییر را از قصد به عادت تبدیل می‌کند.",
        key_concepts=["هدفمندی", "چندعاملی بودن", "خودتنظیمی", "خودکارآمدی", "تثبیت و عادت"],
        critiques="الگوی تغییر رفتار، آن را «همیشه پایدار و قابل تعمیم» نشان می‌دهد، در حالی که در واقع آن، «زمینه‌ای» و «ناپایدار» است و تفاوت، «درجه‌ای» است نه «ماهوی» (Bandura, 1986). نقد دیگر، «شکاف قصد-رفتار» و «بازگشت به رفتار قبلی» (relapse) است: رفتار جدید، می‌تواند در برابر موانع و زمینه‌های نامناسب، بازگشت کند (Fishbein & Ajzen, 1975). همچنین «اندازه‌گیری» پایداری و تعمیم‌پذیری تغییر، به‌سختی تضمین می‌شود و به منابع و حمایت محیطی وابسته است.",
        applications="طراحی مداخلات رفتاری (انگیزه، عادت‌سازی، کاهش موانع، تقویت)، برنامه‌های سلامت و رفتار (تغییر عادت، پیشگیری)، بازاریابی و رفتار مصرفی (هدایت، وفاداری، عادت برند)، آموزش روان‌شناسی رفتار (خودتنظیمی، خودکارآمدی، عادت)، و طراحی محیط‌ها و پیام‌های تقویتی (فرصت، بازخورد، انگیزه) (Fishbein & Ajzen, 1975; Bandura, 1986).",
        evolution="مفهوم تغییر رفتار از رفتارگرایی و روان‌شناسی اجتماعی (اواخر قرن نوزدهم) وارد علوم شد؛ با خودتنظیمی و شناخت اجتماعی (دهه‌های ۱۹۷۰–۱۹۸۰، باندورا)، «اراده و خودکارآمدی» در مرکز قرار گرفت؛ در عصر دیجیتال، تغییر رفتار به «موضوع کلیدی» مداخلات سلامت، محیط و رسانه بدل شده و با داده‌کاوی، دقیق‌تر اندازه‌گیری می‌شود (Bandura, 1986).",
        assumptions="فرض‌های نهفته: رفتار، قابل تغییر است و از باور، نگرش، قصد، انگیزه و کنترل درک‌شده شکل می‌گیرد؛ و تغییر، در صورت وجود منابع و زمینه مناسب، پایدار می‌شود؛ اما پایداری، تعمیم‌پذیری و یک‌جهت‌بودن تغییر، به خودتنظیمی، منابع و محیط وابسته است و به‌کمال نمی‌رسد (Fishbein & Ajzen, 1975; Bandura, 1986).",
    ),
    "CPT-217": dict(
        summary="جذابیت منبع (Source Attractiveness) به میزان تأثیر ویژگی‌های جذاب منبع (چهره، صدا، لباس، سبک، محبوبیت و جذابیت ظاهری یا شخصیتی) بر پذیرش پیام و نگرش مخاطب می‌گویند؛ یعنی «جذابیت، عامل اقناع است». در سنت مطالعات اقناع، جذابیت منبع بر ویژگی‌هایی چون: (۱) ویژگی منبع: جذابیت، از ویژگی‌های منبع (فرد، برند، رسانه) می‌آید نه از خود پیام؛ (۲) مسیر محیطی: جذابیت، عمدتاً از مسیر محیطی اقناع عمل می‌کند نه مرکزی؛ (۳) زمینه‌ای: اثر جذابیت، به زمینه و نوع پیام بستگی دارد؛ (۴) ناپایدار: تغییر ناشی از جذابیت، اغلب موقتی است (Hovland et al., 1969; Petty & Cacioppo, 1986). در سنت مسیرهای پردازش، جذابیت، از یه‌کننده‌های مسیر محیطی است (Petty & Cacioppo, 1986). پژوهش‌ها نشان می‌دهند جذابیت منبع بر «پذیرش پیام»، «اعتماد» و «رفتار مصرفی» اثر عمیق دارد. نمونه‌های رایج: جذابیت سلبریتی‌ها و نظیرین موثر، جذابیت خبرنگاران و مجریان، جذابیت برندها و لوگوها، و جذابیت بصری محتوا. نقد بنیادین، «جذابیت‌زدگی» (attractiveness-ism) است: فرض بر این است که جذابیت، «همیشه مؤثر و پایدار» است، در حالی که در واقع آن، «موقتی و زمینه‌ای» است و تفاوت، «درجه‌ای» است نه «ماهوی» (Petty & Cacioppo, 1986).",
        mechanism="جذابیت منبع در چهار حلقه عمل می‌کند: (۱) حضور منبع: منبع، با ویژگی‌های جذاب (چهره، صدا، سبک، محبوبیت) ظاهر می‌شود؛ (۲) ادراک جذابیت: مخاطب، منبع را جذاب، قابل‌اعتماد یا هم‌سان ادراک می‌کند؛ (۳) انتقال اعتبار: جذابیت، اعتبار و پذیرش را به پیام منتقل می‌کند (مسیر محیطی)؛ (۴) پذیرش یا فراموشی: نگرش، موقتاً تغییر می‌کند و در نبود پیام، ممکن است فراموش شود (Hovland et al., 1969; Petty & Cacioppo, 1986). این چرخه، جذابیت را به عامل اقناع تبدیل می‌کند.",
        key_concepts=["ویژگی منبع", "مسیر محیطی", "هم‌سانی", "موقعی بودن", "ناپایداری اثر"],
        critiques="الگوی جذابیت، آن را «همیشه مؤثر و پایدار» نشان می‌دهد، در حالی که در واقع آن، «موقتی» و «زمینه‌ای» است و تفاوت، «درجه‌ای» است نه «ماهوی» (Petty & Cacioppo, 1986). نقد دیگر، «جداگسیختگی از محتوا» (cue-content dissociation) است: وقتی مخاطب، می‌فهمد که پیام، صرفا‌ً به دلیل جذابیت منبع است، اثر آن کاهش می‌یابد (Hovland et al., 1969). همچنین «اثر پایدار» جذابیت، به‌سختی تضمین می‌شود و با شناخت مخاطب، تضعیف می‌گردد.",
        applications="طراحی استراتژی‌های بازاریابی و تبلیغات (برندسازی، تبلیغات سلبریتی، لوگو)، طراحی تصویر رسانه‌ای (خبرنگار، مجری، شخصیت رسانه‌ای)، تحلیل اعتماد و پذیرش مخاطب (جذابیت، هم‌سانی)، آموزش روان‌شناسی اقناع (ویژگی‌های منبع، مسیرهای پردازش)، و طراحی پیام‌های رسانه‌ای (بصری، صوتی، سبک) (Hovland et al., 1969; Petty & Cacioppo, 1986).",
        evolution="مفهوم جذابیت منبع از مطالعات ییل درباره ویژگی‌های منبع (دهه‌های ۱۹۵۰–۱۹۶۰، هاولاند) وارد علوم شد؛ با نظریه مسیرهای پردازش (دههٔ ۱۹۸۰، پتی و کازیوپو)، «مسیر محیطی» در مرکز قرار گرفت؛ در عصر شبکه‌ها و نظیرین موثر (دهه‌های ۲۰۱۰–۲۰۲۰)، جذابیت منبع به «ابزار اصلی» بازاریابی و اعتمادسازی بدل شده است (Petty & Cacioppo, 1986).",
        assumptions="فرض‌های نهفته: ویژگی‌های جذاب منبع، می‌توانند بر پذیرش پیام و نگرش اثر بگذارند؛ و این اثر، عمدتاً از مسیر محیطی و در زمینه‌های مناسب رخ می‌دهد؛ اما پایداری، یک‌جهت‌بودن و استقلال از محتوا، به زمینه و شناخت مخاطب وابسته است و همیشگی نیست (Hovland et al., 1969; Petty & Cacioppo, 1986).",
    ),
    "CPT-218": dict(
        summary="تخصص منبع (Source Expertise) به میزان دانش، مهارت و اعتبار علمی یا عملی منبع در یک حوزه که بر پذیرش پیام و نگرش مخاطب اثر می‌گذارد، می‌گویند؛ یعنی «تخصص، عامل اعتبار و اقناع است». در سنت مطالعات اقناع، تخصص منبع بر ویژگی‌هایی چون: (۱) ویژگی منبع: تخصص، از دانش و اعتبار منبع می‌آید نه از خود پیام؛ (۲) مسیر مرکزی-محیطی: تخصص، می‌تواند از هر دو مسیر (وقتی مخاطب پردازش می‌کند) عمل کند؛ (۳) زمینه‌ای: اثر تخصص، به حوزه و نوع مخاطب بستگی دارد؛ (۴) پایدارتر: تغییر ناشی از تخصص، معمولاً پایدارتر از تغییر ناشی از جذابیت است (Hovland et al., 1969; McGuire, 1985). در سنت تغییر نگرش، اعتبار و تخصص منبع، از اجزای محوری اعتبار هستند (McGuire, 1985). پژوهش‌ها نشان می‌دهند تخصص منبع بر «پذیرش پیام»، «اعتماد» و «تغییر نگرش» اثر عمیق دارد. نمونه‌های رایج: تخصص خبرنگاران و کارشناسان، اعتبار منابع خبری، تخصص پزشکان و متخصصان در تبلیغات سلامت، و اعتبار پژوهشگران و رسانه‌های تخصصی. نقد بنیادین، «تخصص‌زدگی» (expertise-ism) است: فرض بر این است که تخصص، «همیشه معتبر و پایدار» است، در حالی که در واقع آن، «زمینه‌ای و وابسته به اعتبار» است و تفاوت، «درجه‌ای» است نه «ماهوی» (McGuire, 1985).",
        mechanism="تخصص منبع در چهار حلقه عمل می‌کند: (۱) حضور منبع تخصصی: منبع، با نشانه‌های دانش و اعتبار (عنوان، سابقه، استناد) ظاهر می‌شود؛ (۲) ادراک تخصص: مخاطب، منبع را در حوزه مورد بحث، متخصص و قابل‌اعتماد می‌پندارد؛ (۳) انتقال اعتبار: تخصص، اعتبار و پذیرش را به پیام منتقل می‌کند؛ (۴) پذیرش پایدار: نگرش، بر پایه اعتبار، تغییر و غالباً پایدارتر می‌ماند (Hovland et al., 1969; McGuire, 1985). این چرخه، تخصص را به عامل اعتباری اقناع تبدیل می‌کند.",
        key_concepts=["ویژگی منبع", "اعتبار", "مسیر مرکزی و محیطی", "زمینه‌ای بودن", "پایداری اثر"],
        critiques="الگوی تخصص، آن را «همیشه معتبر و پایدار» نشان می‌دهد، در حالی که در واقع آن، «زمینه‌ای» و «وابسته به اعتبار و بافت» است و تفاوت، «درجه‌ای» است نه «ماهوی» (McGuire, 1985). نقد دیگر، «سوءاستفاده از تخصص» (false expertise) است: نمایش کاذب تخصص و اعتبار، می‌تواند به فریبکاری و کاهش اعتماد اجتماعی بینجامد (Hovland et al., 1969). همچنین «اثر تخصص»، به حوزه و میزان تخصص مخاطب بستگی دارد و تخصص در یک حوزه، لزوماً در حوزه دیگر اعتبار نمی‌آورد.",
        applications="طراحی استراتژی‌های اعتمادسازی (کارشناسان، استناد، اعتبار)، بازاریابی و تبلیغات (اعتبار، تخصص، سلامت و فناوری)، تحلیل اعتبار منابع خبری و رسانه‌ای (کارشناسان، منابع خبری)، آموزش سواد رسانه‌ای (تشخیص تخصص واقعی از کاذب، اعتبارسنجی)، و طراحی پیام‌های خبری و تخصصی (استناد، عنوان، شواهد) (Hovland et al., 1969; McGuire, 1985).",
        evolution="مفهوم تخصص منبع از مطالعات ییل درباره ویژگی‌های منبع (دهه‌های ۱۹۵۰–۱۹۶۰، هاولاند) وارد علوم شد؛ با مدل‌های اعتبار و تغییر نگرش (دههٔ ۱۹۸۰، ماگوایر)، «اعتبار و تخصص» در مرکز قرار گرفت؛ در عصر شبکه‌ها و اطلاعات، تخصص منبع به «معیار اصلی» اعتبارسنجی و اعتمادسازی بدل شده و با حواشی، پیچیده‌تر شده است (McGuire, 1985).",
        assumptions="فرض‌های نهفته: دانش و اعتبار منبع، می‌تواند بر پذیرش پیام و نگرش اثر بگذارد؛ و این اثر، از مسیرهای مرکزی و محیطی و در زمینه‌های مناسب رخ می‌دهد؛ اما اعتبار، یک‌جهت‌بودن و تعمیم‌پذیری تخصص، به حوزه، بافت و شناخت مخاطب وابسته است و در برابر تخصص کاذب، آسیب‌پذیر است (Hovland et al., 1969; McGuire, 1985).",
    ),
    "CPT-219": dict(
        summary="جاذبه عاطفی (Emotional Appeal) به استفاده از احساسات، هیجانات و تجربه‌های درونی مخاطب (ترس، امید، شادی، همدلی، خشم) برای اقناع و تغییر نگرش یا رفتار می‌گویند؛ یعنی «احساس، دروازه اقناع است». در سنت مطالعات اقناع، جاذبه عاطفی بر ویژگی‌هایی چون: (۱) محرک عاطفی: پیام، با ایجاد احساس، توجه و انگیزه مخاطب را برمی‌انگیزد؛ (۲) پردازش هیجانی: مخاطب، پیام را با درگیری هیجانی پردازش می‌کند؛ (۳) زمینه‌ای: اثر جاذبه عاطفی، به شدت و نوع احساس بستگی دارد؛ (۴) ناپایدار: تغییر عاطفی، اغلب موقتی است (Petty & Cacioppo, 1986; Hovland et al., 1969). در سنت الای و ترس، عاطفه، از یه‌کننده‌های اقناع است (Hovland et al., 1969). پژوهش‌ها نشان می‌دهند جاذبه عاطفی بر «توجه»، «پذیرش پیام» و «رفتار» اثر عمیق دارد. نمونه‌های رایج: تبلیغات احساسی (شادی، ترس، همدلی)، کمپین‌های اجتماعی و سلامت، روایت‌های خبری احساس‌برانگیز، و محتوای بازاریابی احساسی. نقد بنیادین، «عاطفی‌زدگی» (emotional-appeal-ism) است: فرض بر این است که جاذبه عاطفی، «همیشه مؤثر و پایدار» است، در حالی که در واقع آن، «موقتی و زمینه‌ای» است و تفاوت، «درجه‌ای» است نه «ماهوی» (Petty & Cacioppo, 1986).",
        mechanism="جاذبه عاطفی در چهار حلقه عمل می‌کند: (۱) ایجاد محرک عاطفی: پیام، با روایت، تصویر یا لحن، احساس را برمی‌انگیزد؛ (۲) درگیری هیجانی: مخاطب، با احساس (ترس، امید، همدلی) درگیر می‌شود؛ (۳) پردازش عاطفی: پیام، از طریق مسیر عاطفی (و محیطی) پردازش می‌شود؛ (۴) پذیرش یا واکنش: نگرش و رفتار، موقتاً تغییر و در صورت نبود تقویت، بازگشت می‌کند (Petty & Cacioppo, 1986; Hovland et al., 1969). این چرخه، عاطفه را دروازه اقناع می‌کند.",
        key_concepts=["محرک عاطفی", "پردازش هیجانی", "زمینه‌ای بودن", "ناپایداری", "توازن هیجانی"],
        critiques="الگوی جاذبه عاطفی، آن را «همیشه مؤثر و پایدار» نشان می‌دهد، در حالی که در واقع آن، «موقتی» و «زمینه‌ای» است و تفاوت، «درجه‌ای» است نه «ماهوی» (Petty & Cacioppo, 1986). نقد دیگر، «اضافه‌رانشی هیجانی» (emotional overload) است: هیجان شدید، می‌تواند به مقاومت، فرافکنی یا واکنش معکوس بینجامد (Hovland et al., 1969). همچنین «اثر پایدار» عاطفه، به‌سختی تضمین می‌شود و ممکن است به‌جای پردازش عقلانی، از آن جلوگیری کند.",
        applications="طراحی کمپین‌های اجتماعی و تبلیغاتی (روایت، احساس، همدلی، ترس و امید)، بازاریابی و برندسازی (احساسات برند، داستان‌سرایی)، تحلیل اثر رسانه و روایت (احساس، توجه، درگیری)، آموزش روان‌شناسی اقناع (مسیر عاطفی، توازن هیجانی، اخلاق)، و طراحی پیام‌های خبری و اجتماعی (روایت، احساس، زمینه) (Petty & Cacioppo, 1986; Hovland et al., 1969).",
        evolution="مفهوم جاذبه عاطفی از مطالعات ییل درباره الای و تغییر نگرش (دهه‌های ۱۹۵۰–۱۹۶۰، هاولاند) وارد علوم شد؛ با نظریه مسیرهای پردازش (دههٔ ۱۹۸۰، پتی و کازیوپو)، «پردازش هیجانی» شکل گرفت؛ در عصر دیجیتال، جاذبه عاطفی به «ابزار اصلی» روایت، بازاریابی و مقنعه‌سازی اجتماعی بدل شده و با شبکه‌ها، قوی‌تر شده است (Petty & Cacioppo, 1986).",
        assumptions="فرض‌های نهفته: احساس و هیجان، می‌تواند توجه، انگیزه و نگرش مخاطب را تغییر دهد؛ و این اثر، از طریق پردازش عاطفی و در زمینه‌های مناسب رخ می‌دهد؛ اما پایداری، یک‌جهت‌بودن و استقلال از شدت هیجان، به زمینه و توانایی پردازش عقلانی مخاطب وابسته است و همیشگی نیست (Petty & Cacioppo, 1986; Hovland et al., 1969).",
    ),
    "CPT-220": dict(
        summary="جاذبه عقلانی (Rational Appeal) به استفاده از منطق، استدلال، شواهد و پردازش شناختی مخاطب برای اقناع و تغییر نگرش یا رفتار می‌گویند؛ یعنی «استدلال، هسته اقناع است». در سنت مطالعات اقناع، جاذبه عقلانی بر ویژگی‌هایی چون: (۱) محتوایی: پیام، بر پایه استدلال و شواهد، ساخته می‌شود؛ (۲) پردازش مرکزی: مخاطب، پیام را از مسیر مرکزی (پردازش محتوا) ارزیابی می‌کند؛ (۳) زمینه‌ای: اثر جاذبه عقلانی، به انگیزه و توانایی پردازش مخاطب بستگی دارد؛ (۴) پایدارتر: تغییر ناشی از استدلال، غالباً پایدارتر از تغییر عاطفی است (Petty & Cacioppo, 1986; Hovland et al., 1969). در سنت مسیرهای پردازش، استدلال، هستۀ مسیر مرکزی است (Petty & Cacioppo, 1986). پژوهش‌ها نشان می‌دهند جاذبه عقلانی بر «پذیرش پیام»، «نگرش پایدار» و «تصمیم‌گیری» اثر عمیق دارد. نمونه‌های رایج: استدلال‌های خبری و تحلیلی، شواهد پژوهشی در تبلیغات سلامت و فناوری، محتوای آموزشی و خبری، و روایت‌های مبتنی بر داده. نقد بنیادین، «عقلانی‌زدگی» (rational-appeal-ism) است: فرض بر این است که جاذبه عقلانی، «همیشه مؤثر و برتر» است، در حالی که در واقع آن، «زمینه‌ای و وابسته به پردازش» است و تفاوت، «درجه‌ای» است نه «ماهوی» (Petty & Cacioppo, 1986).",
        mechanism="جاذبه عقلانی در چهار حلقه عمل می‌کند: (۱) ارائه استدلال: پیام، با منطق، شواهد و استدلال‌های قوی، ارائه می‌شود؛ (۲) پردازش مرکزی: مخاطب، در صورت انگیزه و توانایی، استدلال‌ها را ارزیابی می‌کند؛ (۳) قضاوت محتوا: بر پایه قوت استدلال، نگرش شکل می‌گیرد؛ (۴) پذیرش پایدار: تغییر نگرش، غالباً پایدارتر و مقاوم‌تر در برابر واکنش معکوس است (Petty & Cacioppo, 1986; Hovland et al., 1969). این چرخه، عقلانیت را هسته اقناع می‌کند.",
        key_concepts=["استدلال و شواهد", "پردازش مرکزی", "زمینه‌ای بودن", "پایداری تغییر", "قوت استدلال"],
        critiques="الگوی جاذبه عقلانی، آن را «همیشه مؤثر و برتر» نشان می‌دهد، در حالی که در واقع آن، «زمینه‌ای» و «وابسته به پردازش» است و تفاوت، «درجه‌ای» است نه «ماهوی» (Petty & Cacioppo, 1986). نقد دیگر، «وابستگی به انگیزه و توانایی» است: اگر مخاطب، انگیزه یا توانایی پردازش ندارد، استدلال قوی، اثر کمی دارد (Hovland et al., 1969). همچنین «سوگیری تأییدی» باعث می‌شود مخاطبان، استدلال‌های ناسازگار را رد و استدلال‌های سازگار را بپذیرند.",
        applications="طراحی کمپین‌های خبری و تحلیلی (استدلال، شواهد، داده)، بازاریابی مبتنی بر محتوا (استدلال، مقایسه، شواهد)، تحلیل اعتبار و درگیری مخاطب (پردازش، قضاوت، تصمیم)، آموزش سواد رسانه‌ای و فکری (انتقادی‌اندیشی، ارزیابی استدلال)، و طراحی پیام‌های خبری و آموزشی (منطق، شواهد، داده) (Petty & Cacioppo, 1986; Hovland et al., 1969).",
        evolution="مفهوم جاذبه عقلانی از مطالعات ییل درباره محتوا و تغییر نگرش (دهه‌های ۱۹۵۰–۱۹۶۰، هاولاند) وارد علوم شد؛ با نظریه مسیرهای پردازش (دههٔ ۱۹۸۰، پتی و کازیوپو)، «مسیر مرکزی و استدلال» در مرکز قرار گرفت؛ در عصر دیجیتال، جاذبه عقلانی به «معیار» اعتمادسازی و تصمیم‌گیری داده‌محور بدل شده و با تحلیل محتوا، دقیق‌تر قابل مطالعه است (Petty & Cacioppo, 1986).",
        assumptions="فرض‌های نهفته: استدلال و شواهد، می‌تواند نگرش و رفتار مخاطب را تغییر دهد؛ و این اثر، از مسیر مرکزی و در صورت وجود انگیزه و توانایی پردازش، رخ می‌دهد؛ اما پایداری، تعمیم‌پذیری و یک‌جهت‌بودن اثر، به زمینه، انگیزه و سوگیری مخاطب وابسته است و همیشگی نیست (Petty & Cacioppo, 1986; Hovland et al., 1969).",
    ),
}


def main():
    spec = importlib.util.spec_from_file_location("fw", "scripts/kb_batch238_framework.py")
    fw = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(fw)
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

    snap = [{"id": r[0], "code": r[1], "properties": json.loads(r[2])} for r in rows]
    with open(BACKUP, "w", encoding="utf-8") as f:
        json.dump(snap, f, ensure_ascii=False, indent=1)
    print("backup ->", len(snap), "rows")

    for code in codes:
        eid, _c, props = found[code]
        p = json.loads(props)
        en = ENRICH[code]
        for k, v in en.items():
            p[k] = v
        p["sources"] = p.get("sources", []) or []
        p["citations"] = p.get("citations", []) or []
        have_src = {s.get("citation") for s in p["sources"] if isinstance(s, dict)}
        have_cit = {c.get("source") for c in p["citations"] if isinstance(c, dict)}
        for src in S[code]:
            if src["citation"] not in have_src:
                p["sources"].append({
                    "citation": src["citation"], "title_en": src["title_en"],
                    "title_fa": src["title_fa"], "year": src["year"], "doi": src.get("doi"),
                    "url": src.get("url"), "language": src["language"], "verified": src["verified"],
                })
                have_src.add(src["citation"])
            if src["citation"] not in have_cit:
                p["citations"].append({
                    "source": src["citation"], "locator": src["locator"],
                    "supports": src["supports"], "verified": src["verified"],
                })
                have_cit.add(src["citation"])
        cur.execute("SELECT COUNT(*) FROM kb_relations WHERE source_id=%s OR target_id=%s", (eid, eid))
        n_rel = cur.fetchone()[0]
        n_sources = len(p["sources"])
        n_verified = sum(1 for x in p["citations"] if x.get("verified"))
        score, detail, words = fw.rubric(p, n_verified, n_sources, n_rel)
        p["quality_score"] = score
        p["quality_assessment"] = "ارزیابی خودکار SPEC §6.1: %d/100 (نمره پایه؛ نیازمند بازبینی علمی انسانی)" % score
        p["status_scientific_note"] = "مستندسازی با منابع تأییدشده شبکه‌ای؛ نمره بر پایه سنجه خودکار است و جانشین داوری علمی (SPEC §6.4) نیست."
        p["updated_at"] = NOW
        p["updated_by"] = STAMP
        cur.execute("UPDATE kb_entities SET properties=%s, version=version+1, updated_at=%s WHERE id=%s",
                    (json.dumps(p, ensure_ascii=False), NOW, eid))
        cur.execute("SELECT version FROM kb_entities WHERE id=%s", (eid,))
        new_version = cur.fetchone()[0]
        for src in S[code]:
            sid = fw.ensure_source(cur, src)
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
                     "full concept documentation (SPEC §4.3) + verified sources", STAMP, NOW))
        cur.execute("""INSERT INTO kb_audit_log (entity_code,action,detail,source,created_at)
            VALUES (%s,'DOC_ENRICH',%s,%s,%s)""",
                    (code, json.dumps({"batch": BATCH, "score": score, "words": words,
                                       "sources": n_sources, "verified": n_verified,
                                       "relations": n_rel, "rubric": detail}, ensure_ascii=False), STAMP, NOW))
        print(code, "words", words, "score", score, "detail", detail)
    conn.commit()
    conn.close()
    print("BATCH%d DONE" % BATCH)


if __name__ == "__main__":
    main()
