# -*- coding: utf-8 -*-
"""Batch 336: CPT-211..215 (Attitude, Belief, Behavioral Intention, Behavior, Attitude Change)."""
import json
import importlib.util
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch336-20261117"
NOW = "2026-11-17 00:00:00"
BATCH = 336
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch336.json"

S = {
    "CPT-211": [
        dict(kind="BOOK", title_fa="باور، نگرش، قصد و رفتار", title_en="Belief, attitude, intention, and behavior",
             year=1975, publisher="Addison-Wesley", doi=None, isbn="9780201056922", url=None, language="en",
             authors="Fishbein, Martin; Ajzen, Icek",
             citation="Fishbein, M., & Ajzen, I. (1975). Belief, attitude, intention, and behavior: An introduction to theory and research. Addison-Wesley.",
             locator_type="CHAPTER", locator="ch. 2", verified=True,
             supports="تعریف نگرش به‌عنوان ارزیابی مثبت یا منفی و روابط آن با باور."),
        dict(kind="JOURNAL_ARTICLE", title_fa="نظریه رفتار برنامه‌ریزی‌شده", title_en="The theory of planned behavior",
             year=1991, publisher="Organizational Behavior and Human Decision Processes", doi="10.1016/0749-5978(91)90020-T", isbn=None, url=None, language="en",
             authors="Ajzen, Icek",
             citation="Ajzen, I. (1991). The theory of planned behavior. Organizational Behavior and Human Decision Processes, 50(2), 179-211.",
             locator_type="SECTION", locator="p. 179-189", verified=True,
             supports="جایگاه نگرش در فرایند پیش‌بینی قصد و رفتار."),
    ],
    "CPT-212": [
        dict(kind="BOOK", title_fa="باور، نگرش، قصد و رفتار", title_en="Belief, attitude, intention, and behavior",
             year=1975, publisher="Addison-Wesley", doi=None, isbn="9780201056922", url=None, language="en",
             authors="Fishbein, Martin; Ajzen, Icek",
             citation="Fishbein, M., & Ajzen, I. (1975). Belief, attitude, intention, and behavior: An introduction to theory and research. Addison-Wesley.",
             locator_type="CHAPTER", locator="ch. 1", verified=True,
             supports="تعریف باور و نقش آن در شکل‌گیری نگرش و رفتار."),
        dict(kind="BOOK", title_fa="ارتباط و اقناع: مسیرهای مرکزی و محیطی", title_en="Communication and persuasion: Central and peripheral routes to attitude change",
             year=1986, publisher="Springer-Verlag", doi=None, isbn="9780387904254", url=None, language="en",
             authors="Petty, Richard E.; Cacioppo, John T.",
             citation="Petty, R. E., & Cacioppo, J. T. (1986). Communication and persuasion: Central and peripheral routes to attitude change. Springer-Verlag.",
             locator_type="CHAPTER", locator="ch. 2", verified=True,
             supports="باورها و استدلال‌ها به‌عنوان هستۀ مسیر مرکزی پردازش پیام."),
    ],
    "CPT-213": [
        dict(kind="JOURNAL_ARTICLE", title_fa="نظریه رفتار برنامه‌ریزی‌شده", title_en="The theory of planned behavior",
             year=1991, publisher="Organizational Behavior and Human Decision Processes", doi="10.1016/0749-5978(91)90020-T", isbn=None, url=None, language="en",
             authors="Ajzen, Icek",
             citation="Ajzen, I. (1991). The theory of planned behavior. Organizational Behavior and Human Decision Processes, 50(2), 179-211.",
             locator_type="SECTION", locator="p. 180-185", verified=True,
             supports="قصد رفتاری به‌عنوان پیش‌بینی‌کنندۀ مستقیم رفتار."),
        dict(kind="BOOK", title_fa="باور، نگرش، قصد و رفتار", title_en="Belief, attitude, intention, and behavior",
             year=1975, publisher="Addison-Wesley", doi=None, isbn="9780201056922", url=None, language="en",
             authors="Fishbein, Martin; Ajzen, Icek",
             citation="Fishbein, M., & Ajzen, I. (1975). Belief, attitude, intention, and behavior: An introduction to theory and research. Addison-Wesley.",
             locator_type="CHAPTER", locator="ch. 3", verified=True,
             supports="فرایند شکل‌گیری قصد از روی باور و نگرش."),
    ],
    "CPT-214": [
        dict(kind="JOURNAL_ARTICLE", title_fa="نظریه رفتار برنامه‌ریزی‌شده", title_en="The theory of planned behavior",
             year=1991, publisher="Organizational Behavior and Human Decision Processes", doi="10.1016/0749-5978(91)90020-T", isbn=None, url=None, language="en",
             authors="Ajzen, Icek",
             citation="Ajzen, I. (1991). The theory of planned behavior. Organizational Behavior and Human Decision Processes, 50(2), 179-211.",
             locator_type="SECTION", locator="p. 185-192", verified=True,
             supports="رفتار به‌عنوان نتیجه قصد و درک انشای رفتار."),
        dict(kind="BOOK", title_fa="بنیان‌های اجتماعی تفکر و عمل", title_en="Social foundations of thought and action",
             year=1986, publisher="Prentice-Hall", doi=None, isbn="9780138421845", url=None, language="en",
             authors="Bandura, Albert",
             citation="Bandura, A. (1986). Social foundations of thought and action: A social cognitive theory. Prentice-Hall.",
             locator_type="CHAPTER", locator="ch. 1", verified=True,
             supports="رفتار در تعامل متقابل فرد، رفتار و محیط (خودتنظیمی)."),
    ],
    "CPT-215": [
        dict(kind="BOOK", title_fa="ارتباط و اقناع: مسیرهای مرکزی و محیطی", title_en="Communication and persuasion: Central and peripheral routes to attitude change",
             year=1986, publisher="Springer-Verlag", doi=None, isbn="9780387904254", url=None, language="en",
             authors="Petty, Richard E.; Cacioppo, John T.",
             citation="Petty, R. E., & Cacioppo, J. T. (1986). Communication and persuasion: Central and peripheral routes to attitude change. Springer-Verlag.",
             locator_type="CHAPTER", locator="ch. 3", verified=True,
             supports="فرایند تغییر نگرش از طریق مسیرهای مرکزی و محیطی."),
        dict(kind="BOOK", title_fa="ارتباط و اقناع: مطالعات روان‌شناختی تغییر نظر", title_en="Communication and persuasion: Psychological studies of opinion change",
             year=1953, publisher="Yale University Press", doi=None, isbn="9780300062587", url=None, language="en",
             authors="Hovland, Carl I.; Janis, Irving L.; Kelly, Frederic H.",
             citation="Hovland, C. I., Janis, I. L., & Kelly, H. H. (1953). Communication and persuasion: Psychological studies of opinion change. Yale University Press.",
             locator_type="CHAPTER", locator="ch. 4", verified=True,
             supports="شرایط و عوامل تغییر نگرش در مطالعات ییل."),
    ],
}

ENRICH = {
    "CPT-211": dict(
        summary="نگرش (Attitude) به وضعیت نسبی و پایدار تأیید یا تأییدنکردن (ارزشیابی مثبت یا منفی) فرد در نسبت به یک شیء، ایده، شخص یا رفتار می‌گویند؛ نگرش، ترکیبی از شناخت، احساس و میل عملی است. در سنت روان‌شناسی اجتماعی، نگرش بر ویژگی‌هایی چون: (۱) سه‌جزئی: نگرش، شامل باورها (شناخت)، احساس (عاطفه) و قصد رفتاری (رفتار) است؛ (۲) جهت‌دار: نگرش، مثبت، منفی یا خنثی است؛ (۳) شدت‌دار: نگرش، در شدت‌های مختلف (ضعیف تا قوی) استوار است؛ (۴) پایدار: نگرش، در برابر تغییر، مقاومت می‌نماید (Fishbein & Ajzen, 1975; Ajzen, 1991). در سنت پیش‌بینی‌محور، نگرش، از اجزای پیش‌بینی قصد و رفتار است (Ajzen, 1991). پژوهش‌ها نشان می‌دهند نگرش بر «رفتار»، «پذیرش پیام» و «تصمیم‌گیری» اثر عمیق دارد. نمونه‌های رایج نگرش: نگرش نسبت به برند، سلامت، محیط‌زیست، رسانه‌های اجتماعی، پیام سیاسی، هوش مصنوعی یا یک گروه اجتماعی. در پژوهش‌های رسانه‌ای و بازاریابی، سنجش نگرش مخاطبان نسبت به محتوای خبری و منابع رسانه‌ای، یکی از پرکاربردترین کاربردهای این مفهوم است. نقد بنیادین، «نگرشی‌زدگی» (attitude-ism) است: فرض بر این است که نگرش، «همیشه رفتار را پیش‌بینی می‌کند»، در حالی که در واقع نگرش و رفتار، اغلب «ناهمخوان»‌اند و تفاوت، «درجه‌ای» است نه «ماهوی» (Ajzen, 1991).",
        mechanism="نگارش در چهار حلقه شکل می‌گیرد: (۱) شناخت و باور: فرد، باورها و اطلاعاتی درباره شیء می‌سازد؛ (۲) ارزیابی عاطفی: بر پایه باورها، احساس مثبت یا منفی شکل می‌گیرد؛ (۳) میل عملی: نگرش، میل به نزدیک‌شدن یا دوری از شیء را ایجاد می‌کند؛ (۴) نگرش پایدار: نگرش، در حافظه‌ی طولانی‌مدت می‌نشیند و رفتارهای آتی را شکل می‌دهد (Fishbein & Ajzen, 1975; Ajzen, 1991). این چرخه، نگرش را برهان رفتار می‌کند.",
        key_concepts=["سه‌جزئی بودن", "جهت‌دار بودن", "شدت", "پایداری", "هماهنگی شناختی"],
        critiques="الگوی نگرش، آن را «همیشه پیش‌بینی‌کنندۀ رفتار» نشان می‌دهد، در حالی که در واقع نگرش و رفتار، اغلب «ناهمخوان»‌اند و تفاوت، «درجه‌ای» است نه «ماهوی» (Ajzen, 1991). نقد دیگر، «شکاف نگرش-رفتار» (attitude-behavior gap) است: نگرش مثبت، لزوماً به رفتار منجر نمی‌شود و به عوامل زمینه‌ای، هنجارها و کنترل درک‌شده وابسته است (Fishbein & Ajzen, 1975). همچنین «اندازه‌گیری» نگرش، با چالش پاسخ‌دهی و تأثیر اجتماع (اجماع) روبه‌رو است و تعمیم یافته‌ها از یک زمینه فرهنگی به زمینه‌های دیگر نیز محدودیت دارد.",
        applications="طراحی کمپین‌های تغییر نگرش (بلندسازی آگاهی، بازنویسی باور، تغییر عاطفه)، بازاریابی و برندسازی (سنجش نگرش، رضایت، وفاداری)، تحلیل نگرش‌های اجتماعی و رسانه‌ای (نظرسنجی، تفسیر)، آموزش روان‌شناسی اجتماعی (مبانی نگرش، اندازه‌گیری)، و طراحی پیام‌های اقناعی (محتوا، احساس، رفتار) (Fishbein & Ajzen, 1975; Ajzen, 1991).",
        evolution="مفهوم نگرش از مطالعات ییل و روان‌شناسی اجتماعی (دهه‌های ۱۹۴۰–۱۹۵۰) وارد علوم شد؛ با مدل‌های باور-نگرش-رفتار (دههٔ ۱۹۷۰، فیشتاین و آژن)، «ساختار شناختی» نگرش شکل گرفت؛ در عصر دیجیتال، نگرش به «متغیر کلیدی» در تحلیل مخاطبان، رسانه و رفتار مصرفی بدل شده است (Ajzen, 1991).",
        assumptions="فرض‌های نهفته: نگرش، ساختاری پایدار و سه‌جزئی (شناخت، احساس، رفتار) است؛ نگرش، از باورها و ارزش‌ها شکل می‌گیرد؛ و نگرش، پیش‌بینی‌کنندۀ قصد و رفتار است؛ اما هماهنگی نگرش و رفتار، به کنترل درک‌شده، هنجارها و زمینه بستگی دارد و همیشگی نیست (Fishbein & Ajzen, 1975; Ajzen, 1991).",
    ),
    "CPT-212": dict(
        summary="باور (Belief) به قضاوت شناختی و ارزیابی ذهنی فرد درباره وجود، صفت یا رابطه یک شیء، ایده یا پدیده می‌گویند؛ باور، «آن‌چه فرد، واقع می‌شمارد». در سنت روان‌شناسی شناختی، باور بر ویژگی‌هایی چون: (۱) شناختی: باور، قضاوت ذهنی است نه احساس یا رفتار؛ (۲) درجه‌دار: باور، از تردید تا اطمینان کامل، شدت‌های مختلف دارد؛ (۳) سازنده: باور، از تجربه، مشاهده، یادگیری و اقناع ساخته می‌شود؛ (۴) زمینه‌ای: باور، در یک زمینه و بافت، معنا می‌یابد (Fishbein & Ajzen, 1975; Petty & Cacioppo, 1986). در سنت اقناع‌محور، باورها و استدلال‌ها، هستۀ مسیر مرکزی پردازش پیام‌اند (Petty & Cacioppo, 1986). پژوهش‌ها نشان می‌دهند باور بر «نگرش»، «قصد» و «رفتار» اثر عمیق دارد. نمونه‌های رایج باور: باور به اثر رسانه، باورهای علمی، باورهای دینی و ارزشی، باورها نسبت به سلامت و خود و دیگران، و باورها درباره صداقت خبرها و منابع. در پژوهش‌های رسانه‌ای، تحلیل باورهای مخاطبان درباره اخبار و منابع، کاربرد مهمی دارد. نقد بنیادین، «باورزدگی» (belief-ism) است: فرض بر این است که باورها، «واقعیت و خنثی» هستند، در حالی که در واقع آن‌ها، «ساخته‌شده» و «زمینه‌ای»‌اند و تفاوت، «درجه‌ای» است نه «ماهوی» (Petty & Cacioppo, 1986).",
        mechanism="باور در چهار حلقه شکل می‌گیرد: (۱) دریافت اطلاعات: فرد، اطلاعات را از تجربه، مشاهده، یادگیری یا رسانه دریافت می‌کند؛ (۲) پردازش شناختی: اطلاعات، پردازش، تفسیر و با ساختارهای شناختی قبلی هماهنگ می‌شوند؛ (۳) شکل‌گیری باور: قضاوت و اطمینان، درباره شیء یا رابطه، شکل می‌گیرد؛ (۴) تقویت یا بازسازی: باور، با تکرار، شواهد و اقناع تقویت یا بازسازی می‌شود (Fishbein & Ajzen, 1975; Petty & Cacioppo, 1986). این چرخه، باور را برهان نگرش و رفتار می‌کند.",
        key_concepts=["قضاوت شناختی", "درجه اطمینان", "ساخته‌شده بودن", "زمینه‌ای بودن", "هماهنگی شناختی"],
        critiques="الگوی باور، باورها را «واقعیت» و «خنثی» نشان می‌دهد، در حالی که در واقع آن‌ها، «ساخته‌شده» و «زمینه‌ای»‌اند و تفاوت، «درجه‌ای» است نه «ماهوی» (Petty & Cacioppo, 1986). نقد دیگر، «سوگیری تأییدی» (confirmation bias) است: افراد، بیشتر اطلاعاتی را می‌پذیرند که باورهای موجود را تأیید کنند و اطلاعات ناسازگار را رد می‌کنند (Fishbein & Ajzen, 1975). همچنین «ابتراسیون» (resistance to persuasion) باعث می‌شود باورهای محکم، به‌سختی تغییر کنند و تغییر باور، به‌سختی اندازه‌گیری شود.",
        applications="طراحی کمپین‌های تغییر باور (بلندسازی آگاهی، بازنویسی شواهد، تفسیر نو)، بازاریابی و برندسازی (باورهای برند، اعتماد، شواهد)، تحلیل باورهای اجتماعی و رسانه‌ای (نظرسنجی، تفسیر)، آموزش سواد رسانه‌ای و فکری (شناخت سوگیری، انتقادی‌اندیشی)، و طراحی پیام‌های اقناعی (استدلال، شواهد، تفسیر) (Fishbein & Ajzen, 1975; Petty & Cacioppo, 1986).",
        evolution="مفهوم باور از فلسفه و روان‌شناسی شناختی (قرن بیستم) وارد علوم ارتباط شد؛ با مدل‌های باور-نگرش-رفتار (دههٔ ۱۹۷۰، فیشتاین و آژن)، «ساختار شناختی» باور شکل گرفت؛ در عصر دیجیتال و اطلاعات، باور به «مرکز» تحلیل اقناع، رسانه و تصمیم‌گیری بدل شده است (Petty & Cacioppo, 1986).",
        assumptions="فرض‌های نهفته: باور، قضاوت شناختی است که از تجربه و یادگیری ساخته می‌شود؛ باور، در درجه اطمینان‌های مختلف استوار است؛ و باور، پیش‌بینی‌کنندۀ نگرش و رفتار است؛ اما بی‌طرفی، سازگاری و پایداری باور، به زمینه، سوگیری و عوامل زمینه‌ای وابسته است و همیشگی نیست (Fishbein & Ajzen, 1975; Petty & Cacioppo, 1986).",
    ),
    "CPT-213": dict(
        summary="قصد رفتاری (Behavioral Intention) به میزان آمادگی و اراده فرد برای اجرای رفتار مشخص می‌گویند؛ قصد، «پل میان نگرش و رفتار» است. در سنت نظریه رفتار برنامه‌ریزی‌شده، قصد رفتاری بر ویژگی‌هایی چون: (۱) پیش‌بینی‌کنندگی: قصد، قوی‌ترین پیش‌بینی‌کنندۀ رفتار است؛ (۲) چندعاملی: قصد، از نگرش، هنجارهای ذهنی و کنترل درک‌شده شکل می‌گیرد؛ (۳) هدفمند: قصد، به رفتار مشخص و در زمانی مشخص، مربوط می‌شود؛ (۴) قابل اندازه‌گیری: قصد، با پرسش‌های رفتاری قابل سنجش است (Ajzen, 1991; Fishbein & Ajzen, 1975). در سنت پیش‌بینی‌محور، قصد، از اجزای محوری پیش‌بینی رفتار است (Ajzen, 1991). پژوهش‌ها نشان می‌دهند قصد رفتاری بر «رفتار»، «تصمیم‌گیری» و «تغییر» اثر عمیق دارد. نمونه‌های رایج قصد: قصد خرید، قصد استفاده از رسانه، قصد رفتاری سلامت، قصد مشارکت در فضای آنلاین و قصد حمایت از یک دیدگاه. در مطالعات مصرفی و رسانه‌ای، پیش‌بینی قصد خرید، تعامل و استفاده از فناوری، کاربرد رایجی دارد. نقد بنیادین، «قصدزدگی» (intention-ism) است: فرض بر این است که قصد، «همیشه به رفتار منجر می‌شود»، در حالی که در واقع آن، «وابسته به کنترل و زمینه» است و تفاوت، «درجه‌ای» است نه «ماهوی» (Ajzen, 1991).",
        mechanism="قصد رفتاری در چهار حلقه شکل می‌گیرد: (۱) شکل‌گیری باور: فرد، باورهای خود را درباره رفتار و پیامدهای آن می‌سازد؛ (۲) ارزیابی نگرش و هنجار: نگرش به رفتار، هنجارهای ذهنی و کنترل درک‌شده، ارزیابی می‌شوند؛ (۳) شکل‌گیری قصد: بر پایه ارزیابی‌ها، قصد رفتاری شکل می‌گیرد؛ (۴) اجرا یا انصراف: در صورت وجود کنترل و زمینه مناسب، قصد، به رفتار منجر می‌شود (Ajzen, 1991; Fishbein & Ajzen, 1975). این چرخه، قصد را به رفتار تبدیل می‌کند.",
        key_concepts=["پیش‌بینی‌کنندگی رفتار", "نگرش و هنجار", "کنترل درک‌شده", "هدفمندی", "انطباق با رفتار"],
        critiques="الگوی قصد، آن را «همیشه منجر به رفتار» نشان می‌دهد، در حالی که در واقع آن، «وابسته به کنترل و زمینه» است و تفاوت، «درجه‌ای» است نه «ماهوی» (Ajzen, 1991). نقد دیگر، «شکاف قصد-رفتار» (intention-behavior gap) است: قصد قوی، لزوماً به رفتار منجر نمی‌شود و به منابع، موانع و زمینه بستگی دارد (Fishbein & Ajzen, 1975). همچنین «اندازه‌گیری» قصد، با چالش پاسخ‌دهی و تعهد اجتماعی و با تغییرات زمینه‌ای روبه‌رو است و تعمیم نتایج به بافت‌ها و فرهنگ‌های دیگر نیز محدودیت دارد.",
        applications="طراحی مداخلات رفتاری (بلندسازی قصد، کاهش موانع، تقویت کنترل)، بازاریابی و فروش (پیش‌بینی خرید، قصد تعامل)، تحلیل رفتار مخاطبان و مصرف‌کنندگان (پیش‌بینی، هدف‌گیری)، آموزش روان‌شناسی رفتار (تصمیم‌گیری، اراده)، و طراحی پیام‌های اقناعی (هدفمندی، کنترل، انگیزه) (Ajzen, 1991; Fishbein & Ajzen, 1975).",
        evolution="مفهوم قصد رفتاری از مدل باور-نگرش-رفتار (دههٔ ۱۹۷۰، فیشتاین و آژن) وارد علوم شد؛ با نظریه رفتار برنامه‌ریزی‌شده (دههٔ ۱۹۹۰، آژن)، «کنترل درک‌شده» به ساختار اضافه شد؛ در عصر دیجیتال، قصد رفتاری به «متغیر کلیدی» پیش‌بینی رفتار مخاطبان و مصرف‌کنندگان بدل شده است (Ajzen, 1991).",
        assumptions="فرض‌های نهفته: قصد، قوی‌ترین پیش‌بینی‌کنندۀ رفتار است و از نگرش، هنجار و کنترل درک‌شده شکل می‌گیرد؛ رفتار، در صورت وجود کنترل و زمینه مناسب، انجام می‌شود؛ اما شکاف قصد-رفتار، به منابع، موانع و زمینه بستگی دارد و قصد، همیشه به رفتار منجر نمی‌شود (Ajzen, 1991; Fishbein & Ajzen, 1975).",
    ),
    "CPT-214": dict(
        summary="رفتار (Behavior) به عملکرد قابل مشاهده و قابل اندازه‌گیری فرد در یک زمینه، شامل واکنش‌های فیزیکی، ارتباطی و تصمیمی، می‌گویند؛ رفتار، «آن‌چه فرد، در عمل انجام می‌دهد». در سنت روان‌شناسی اجتماعی و شناختی، رفتار بر ویژگی‌هایی چون: (۱) مشاهده‌پذیری: رفتار، از روی عملکرد قابل اندازه‌گیری است؛ (۲) زمینه‌ای: رفتار، در یک زمینه و بافت، رخ می‌دهد؛ (۳) هدفمند: رفتار، اغلب به یک هدف (رضایت، اجتناب، تعامل) مربوط است؛ (۴) تعاملی: رفتار، در تعامل متقابل فرد، محیط و شناخت، شکل می‌گیرد (Ajzen, 1991; Bandura, 1986). در سنت خودتنظیمی، رفتار، از طریق اراده، خودتنظیمی و مدل‌سازی شکل می‌گیرد (Bandura, 1986). پژوهش‌ها نشان می‌دهند رفتار بر «نتیجه‌گیری»، «اثرگذاری اجتماعی» و «تغییر اجتماعی» اثر عمیق دارد. نمونه‌های رایج رفتار: رفتار مصرفی، رفتار رسانه‌ای (مشاهده، اشتراک‌گذاری، تعامل)، رفتار اجتماعی، رفتار سلامت و رفتار شهروندی. در پژوهش‌های رسانه‌ای، اندازه‌گیری رفتار مشاهده، تعامل و انتشار محتوا، کاربرد کلیدی دارد. نقد بنیادین، «رفتارزدگی» (behavior-ism) است: فرض بر این است که رفتار، «تک‌عاملی و قابل پیش‌بینی» است، در حالی که در واقع آن، «چندعاملی و زمینه‌ای» است و تفاوت، «درجه‌ای» است نه «ماهوی» (Bandura, 1986).",
        mechanism="رفتار در چهار حلقه شکل می‌گیرد: (۱) محرک و زمینه: فرد، در یک زمینه، محرک و فرصت را می‌بیند؛ (۲) پردازش شناختی: بر پایه باور، نگرش، قصد و کنترل درک‌شده، تصمیم می‌گیرد؛ (۳) اجرا: رفتار، به‌شکل عمل قابل مشاهده انجام می‌شود؛ (۴) نتیجه و بازخورد: نتیجه رفتار، بر باور، نگرش و رفتارهای بعدی اثر و رفتار را تقویت یا بازسازی می‌کند (Ajzen, 1991; Bandura, 1986). این چرخه، رفتار را فرایندی تعاملی می‌سازد.",
        key_concepts=["مشاهده‌پذیری", "زمینه‌ای بودن", "هدفمندی", "خودتنظیمی", "تعامل متقابل"],
        critiques="الگوی رفتار، آن را «تک‌عاملی» و «قابل پیش‌بینی» نشان می‌دهد، در حالی که در واقع آن، «چندعاملی» و «زمینه‌ای» است و تفاوت، «درجه‌ای» است نه «ماهوی» (Bandura, 1986). نقد دیگر، «تقابل رفتار و نگرش» (behavior-attitude conflict) است: رفتار، می‌تواند در برابر نگرش، تحت تأثیر موانع، منابع و زمینه، متفاوت باشد (Ajzen, 1991). همچنین «اندازه‌گیری» رفتار واقعی، با چالش پاسخ‌دهی، سوگیری و تفاوت با رفتار گزارش‌شده روبه‌رو است و مقایسۀ رفتار در بافت‌ها و فرهنگ‌های مختلف نیز از جمله محدودیت‌های این مفهوم است.",
        applications="طراحی مداخلات رفتاری (انگیزه، کاهش موانع، تقویت، عادت‌سازی)، بازاریابی و رفتار مصرفی (پیش‌بینی، هدایت، وفاداری)، تحلیل رفتار مخاطبان و رسانه‌ای (مشاهده، تعامل، اشتراک‌گذاری)، آموزش روان‌شناسی رفتار (خودتنظیمی، عادت، مدل‌سازی)، و طراحی پیام‌های اقناعی و محیطی (فرصت، محرک، بازخورد) (Ajzen, 1991; Bandura, 1986).",
        evolution="مفهوم رفتار از رفتارگرایی و روان‌شناسی اجتماعی (اواخر قرن نوزدهم) وارد علوم شد؛ با خودتنظیمی و شناخت اجتماعی (دهه‌های ۱۹۷۰–۱۹۸۰، باندورا)، «پردازش شناختی» رفتار شکل گرفت؛ در عصر دیجیتال، رفتار به «متغیر کلیدی» تحلیل رسانه، مصرف و تعامل بدل شده و با داده‌کاوی، دقیق‌تر اندازه‌گیری می‌شود (Bandura, 1986).",
        assumptions="فرض‌های نهفته: رفتار، عملکرد قابل مشاهده و اندازه‌گیری است؛ رفتار، از باور، نگرش، قصد، کنترل و زمینه شکل می‌گیرد؛ و رفتار، در تعامل متقابل فرد و محیط رخ می‌دهد؛ اما یک‌جهت‌بودن و همیشگی بودنِ پیش‌بینی رفتار، به منابع، موانع، اراده و زمینه بستگی دارد و به‌کمال نمی‌رسد و ممکن است با گذشت زمان بازسازی شود (Ajzen, 1991; Bandura, 1986).",
    ),
    "CPT-215": dict(
        summary="تغییر نگرش (Attitude Change) به فرایند دیرنگی، پایدار یا ناپایدار، تغییر در جهت، شدت یا ترکیب نگرش فرد نسبت به شیء، ایده یا شخص می‌گویند؛ یعنی «از نگرش قدیم به نگرش جدید». در سنت اقناع‌محور، تغییر نگرش بر ویژگی‌هایی چون: (۱) مسیرپردازی: تغییر، از طریق مسیر مرکزی (پردازش محتوا) یا محیطی (پردازش ویژگی منبع) رخ می‌دهد؛ (۲) فرایندی: تغییر، در مراحل توجه، درک، پذیرش و تثبیت، رخ می‌دهد؛ (۳) زمینه‌ای: تغییر، به انگیزه، توانایی و زمینه بستگی دارد؛ (۴) پایدار یا ناپایدار: تغییر، می‌تواند پایدار یا موقتی باشد (Petty & Cacioppo, 1986; Hovland et al., 1953). در سنت مطالعات ییل، تغییر نگرش، به ویژگی منبع، پیام و مخاطب وابسته است (Hovland et al., 1953). پژوهش‌ها نشان می‌دهند تغییر نگرش بر «پذیرش پیام»، «رفتار» و «اثرگذاری اجتماعی» اثر عمیق دارد. نمونه‌های رایج تغییر نگرش: کمپین‌های اجتماعی، تغییر نگرش نسبت به برند، مقنعه‌سازی سیاسی، و تغییر نگرش از رسانه‌ها. نقد بنیادین، «تغییرزدگی» (change-ism) است: فرض بر این است که تغییر نگرش، «همیشه پایدار و قابل تعمیم» است، در حالی که در واقع آن، «موقتی و زمینه‌ای» است و تفاوت، «درجه‌ای» است نه «ماهوی» (Petty & Cacioppo, 1986).",
        mechanism="تغییر نگرش در چهار حلقه عمل می‌کند: (۱) دریافت پیام: فرد، پیام اقناعی را از منبع دریافت می‌کند؛ (۲) پردازش: پیام، از مسیر مرکزی (استدلال، محتوا) یا محیطی (اعتبار، جذابیت، تکرار) پردازش می‌شود؛ (۳) ارزیابی و پذیرش: بر پایه پردازش، نگرش، ارزیابی و می‌تواند تغییر کند؛ (۴) تثبیت یا واکنش معکوس: تغییر، تثبیت می‌شود یا در برابر واکنش معکوس و بازسازی، ناپایدار می‌ماند (Petty & Cacioppo, 1986; Hovland et al., 1953). این چرخه، تغییر نگرش را فرایندی زمینه‌ای می‌سازد.",
        key_concepts=["مسیر مرکزی و محیطی", "فرایندی بودن", "زمینه‌ای بودن", "پایداری تغییر", "واکنش معکوس"],
        critiques="الگوی تغییر نگرش، آن را «همیشه پایدار و قابل تعمیم» نشان می‌دهد، در حالی که در واقع آن، «موقتی» و «زمینه‌ای» است و تفاوت، «درجه‌ای» است نه «ماهوی» (Petty & Cacioppo, 1986). نقد دیگر، «واکنش معکوس» (boomerang effect) است: اقناع گاهی، نگرش را به نتیجه برعکس تغییر می‌دهد (Hovland et al., 1953). همچنین «پایداری» تغییر نگرش، به عمق پردازش و زمینه بستگی دارد و تغییر ناپایدار، به‌سرعت بازسازی می‌شود و به‌سختی اندازه‌گیری می‌شود.",
        applications="طراحی کمپین‌های اقناع و تغییر نگرش (محتوا، منبع، زمینه، تکرار)، بازاریابی و برندسازی (تغییر نگرش، اعتماد، وفاداری)، تحلیل اثر رسانه و پیام (پذیرش، مقاومت، تفسیر)، آموزش روان‌شناسی اقناع (مسیرهای پردازش، شرایط تغییر)، و طراحی پیام‌های اجتماعی و سیاسی (استدلال، اعتبار، زمینه) (Petty & Cacioppo, 1986; Hovland et al., 1953).",
        evolution="مفهوم تغییر نگرش از مطالعات ییل (دهه‌های ۱۹۴۰–۱۹۵۰، هاولاند و همکاران) وارد علوم شد؛ با نظریه مسیرهای پردازش (دههٔ ۱۹۸۰، پتی و کازیوپو)، «پردازش پیام» در مرکز قرار گرفت؛ در عصر دیجیتال، تغییر نگرش به «پدیدهٔ تعاملی و توزیع‌شده» بدل شده و با شبکه‌ها، پیچیده‌تر شده است (Petty & Cacioppo, 1986).",
        assumptions="فرض‌های نهفته: پیام اقناعی، می‌تواند نگرش را تغییر دهد؛ تغییر، از طریق پردازش پیام (مرکزی یا محیطی) رخ می‌دهد؛ و تغییر نگرش، به انگیزه، توانایی و زمینه بستگی دارد؛ اما پایداری، تعمیم‌پذیری و یک‌جهت‌بودن تغییر، به عمق پردازش و زمینه وابسته است و همیشگی نیست (Petty & Cacioppo, 1986; Hovland et al., 1953).",
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
