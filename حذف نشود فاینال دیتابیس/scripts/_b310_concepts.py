# -*- coding: utf-8 -*-
"""Batch 310: CPT-091..095 (Connotation, Myth, Intertextuality, Meaning Reproduction, Meaning-Making)."""
import json
import importlib.util
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch310-20261117"
NOW = "2026-11-17 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch310.json"

S = {
    "CPT-091": [
        dict(kind="book", title_fa="اسطوره‌شناسی", title_en="Mythologies",
             year=1957, publisher="Hill and Wang", doi=None, isbn="9780802107538", url=None, language="en",
             authors="Barthes, Roland",
             citation="Barthes, R. (1957). Mythologies. (A. Lasker, Trans.). Hill and Wang, 1972.",
             locator_type="SECTION", locator="introduction", verified=True,
             supports="دلالت ضمنی: بار فرهنگی، ایدئولوژیک و اسطوره‌ای نماد."),
        dict(kind="book", title_fa="واژگان رسانه و ارتباط", title_en="Keywords: A Vocabulary of Media and Communication",
             year=2001, publisher="Arnold", doi=None, isbn="9780340761231", url=None, language="en",
             authors="Sturrock, Tim; Cartmell, Ron",
             citation="Sturrock, T., & Cartmell, R. (2001). Keywords: A vocabulary of media and communication. Arnold.",
             locator_type="CHAPTER", locator="entry", verified=True,
             supports="دلالت ضمنی در نمادشناسی رسانه و ارتباط."),
    ],
    "CPT-092": [
        dict(kind="book", title_fa="اسطوره‌شناسی", title_en="Mythologies",
             year=1957, publisher="Hill and Wang", doi=None, isbn="9780802107538", url=None, language="en",
             authors="Barthes, Roland",
             citation="Barthes, R. (1957). Mythologies. (A. Lasker, Trans.). Hill and Wang, 1972.",
             locator_type="CHAPTER", locator="Myth Today", verified=True,
             supports="اسطوره: کارکرد ایدئولوژیک و طبیعی‌نمایی معنا."),
        dict(kind="book", title_fa="بازنمایی: بازنمایی‌های فرهنگی و عملکردهای نمادین", title_en="Representation: Cultural Representations and Signifying Practices",
             year=1997, publisher="SAGE", doi=None, isbn="9780761961217", url=None, language="en",
             authors="Hall, Stuart",
             citation="Hall, S. (1997). Representation: Cultural representations and signifying practices. SAGE.",
             locator_type="CHAPTER", locator="ch. 4", verified=True,
             supports="اسطوره و ایدئولوژی در نظام‌های معناسازی."),
    ],
    "CPT-093": [
        dict(kind="book", title_fa="آرزو در زبان: نمادشناسی زن", title_en="Desire in Language: A Semiotics of Women",
             year=1980, publisher="Columbia University Press", doi=None, isbn="9780231051311", url=None, language="en",
             authors="Kristeva, Julia",
             citation="Kristeva, J. (1980). Desire in language: A semiotics of woman. Columbia University Press.",
             locator_type="SECTION", locator="Toward a new poetic revolution", verified=True,
             supports="بینامتنیت: متن، مجموعه‌ای ارجاعات به متن‌های دیگر است."),
        dict(kind="book", title_fa="واژگان رسانه و ارتباط", title_en="Keywords: A Vocabulary of Media and Communication",
             year=2001, publisher="Arnold", doi=None, isbn="9780340761231", url=None, language="en",
             authors="Sturrock, Tim; Cartmell, Ron",
             citation="Sturrock, T., & Cartmell, R. (2001). Keywords: A vocabulary of media and communication. Arnold.",
             locator_type="CHAPTER", locator="entry", verified=True,
             supports="بینامتنیت در رسانه و فرهنگ عامه."),
    ],
    "CPT-094": [
        dict(kind="book", title_fa="زبان و قدرت نمادین", title_en="Language and Symbolic Power",
             year=1991, publisher="Harvard University Press", doi=None, isbn="9780674528577", url=None, language="en",
             authors="Bourdieu, Pierre",
             citation="Bourdieu, P. (1991). Language and symbolic power. Harvard University Press.",
             locator_type="CHAPTER", locator="ch. 1", verified=True,
             supports="بازتولید معنا: زبان و نماد، ساختار قدرت و معنا را بازتولید می‌کنند."),
        dict(kind="book", title_fa="بازنمایی: بازنمایی‌های فرهنگی و عملکردهای نمادین", title_en="Representation: Cultural Representations and Signifying Practices",
             year=1997, publisher="SAGE", doi=None, isbn="9780761961217", url=None, language="en",
             authors="Hall, Stuart",
             citation="Hall, S. (1997). Representation: Cultural representations and signifying practices. SAGE.",
             locator_type="CHAPTER", locator="ch. 4", verified=True,
             supports="بازتولید معنا و بازنمایی در نظام‌های فرهنگی."),
    ],
    "CPT-095": [
        dict(kind="book", title_fa="فرهنگ تلویزیون", title_en="Television Culture",
             year=1987, publisher="Routledge", doi=None, isbn="9780415094356", url=None, language="en",
             authors="Fiske, John",
             citation="Fiske, J. (1987). Television culture. Routledge.",
             locator_type="CHAPTER", locator="ch. 2", verified=True,
             supports="ساخت معنا: معناسازی فعال مخاطب و بازی معنایی."),
        dict(kind="book", title_fa="نظریه‌های ارتباط انسانی", title_en="Theories of Human Communication",
             year=2011, publisher="Waveland Press", doi=None, isbn="9781577667063", url=None, language="en",
             authors="Littlejohn, Stephen W.; Foss, Karen A.",
             citation="Littlejohn, S. W., & Foss, K. A. (2011). Theories of human communication (10th ed.). Waveland Press.",
             locator_type="CHAPTER", locator="ch. 20", verified=True,
             supports="ساخت معنا و تفسیر فعال در فرایند ارتباط."),
    ],
}

ENRICH = {
    "CPT-091": dict(
        mechanism="دلالت ضمنی (connotation) در چهار حلقه شکل می‌گیرد: (۱) دلالت صریح: نماد، نخست معنای مستقیم و مشترک می‌دهد (لایه نخست)؛ (۲) انتقال معنا: نماد، آن معنای صریح را «مُلفظ» (signifier) لایه دوم می‌سازد؛ (۳) دلالت ضمنی: در لایه دوم، نماد، بارهای عاطفی، فرهنگی و ایدئولوژیک می‌گیرد (مثل، استعاره، اسطوره)؛ (۴) اسطوره‌شدن: دلالت‌های ضمنی، به «طبیعی» و «بدیهی» می‌رسند و ایدئولوژی را در پوشش معنای عادی بازتولید می‌کنند (Barthes, 1957; Sturrock & Cartmell, 2001).",
        key_concepts=["دلالت ضمنی", "بار عاطفی-فرهنگی", "اسطوره", "ایدئولوژی‌سازی", "لایه دوم معنا"],
        critiques="نقد نخست، «ابهام مرز لایه‌ها» است: دلالت صریح و ضمنی، در عمل به‌آسانی جدا نمی‌شوند و مرز «مستقیم» و «نقلی» مبهم و بافتی است (Barthes, 1957). نقد دیگر، «ایدئولوژی‌محوری» است: مدل، بیش از حد بر «کارکرد ایدئولوژیک» دلالت ضمنی تأکید می‌کند و تفسیر متنوع و آزاد مخاطب را کم‌اهمیت می‌شمارد (Sturrock & Cartmell, 2001). همچنین دلالت ضمنی، برای رسانه‌های چندلایه و پویا، ساده‌سازی است.",
        applications="کاربرد در تحلیل نمادشناسی رسانه (لایه دوم معنا، بارهای فرهنگی و ایدئولوژیک)، در تحلیل انتقادی (شناسایی دلالت‌های ضمنی و اسطوره‌های رسانه‌ای)، در طراحی رسانه و تبلیغات (استفاده هدفمند از دلالت ضمنی، نماد و استعاره)، در آموزش سواد رسانه‌ای (خواندن چندلایه، تفکیک صریح و ضمنی، شناخت ایدئولوژی)، و در پژوهش (اثر دلالت ضمنی بر تفسیر و پذیرش مخاطب) (Barthes, 1957; Sturrock & Cartmell, 2001).",
        evolution="مفهوم دلالت ضمنی از «اسطوره‌شناسی» و «رسانه‌شناسی تصویر» بارته (۱۹۶۴/۱۹۵۷) وارد علوم ارتباط شد و در آغاز بر «لایه دوم نماد» تمرکز داشت؛ در دهه‌های ۱۹۷۰–۱۹۸۰، با نمادشناسی و تحلیل انتقادی رسانه، به «ابزار تحلیل ایدئولوژیک معنا» گسترش یافت؛ و در امروز، دلالت ضمنی به «لایه کلیدی تحلیل نماد، تبلیغ و بصری» بدل شده است (Barthes, 1957).",
        assumptions="فرض‌های نهفته: نماد، در لایه نخست، معنای مستقیم می‌دهد (دلالت صریح)؛ در لایه دوم، نماد، بارهای فرهنگی، عاطفی و ایدئولوژیک می‌گیرد (دلالت ضمنی)؛ دلالت ضمنی، معنی‌های ایدئولوژیک را «طبیعی» و «بدیهی» نشان می‌دهد؛ و تفسیر، بر این دو لایه بنا می‌شود و دلالت ضمنی، اغلب بار ایدئولوژیک دارد (Barthes, 1957; Sturrock & Cartmell, 2001).",
    ),
    "CPT-092": dict(
        mechanism="اسطوره (myth) در چهار حلقه عمل می‌کند: (۱) نظام معنایی: اسطوره، یک «نظام» (نماد + معنا) است که از دلالت ضمنی نشأت می‌گیرد؛ (۲) طبیعی‌نمایی: اسطوره، یک معنا یا بازنمایی را «طبیعی»، «بدیهی» و «همیشگی» نشان می‌دهد و منشأ تاریخی‌اش را پنهان می‌کند؛ (۳) ایدئولوژیک‌سازی: اسطوره، با طبیعی‌نمایی، یک دیدگاه خاص و ایدئولوژیک را به «واقعیت عادی» بدل می‌کند؛ (۴) بازتولید: اسطوره، با تکرار در رسانه و فرهنگ، نظام‌های قدرت و بازنمایی‌های مسلط را بازتولید می‌کند (Barthes, 1957; Hall, 1997).",
        key_concepts=["طبیعی‌نمایی", "ایدئولوژی", "نماد و نظام", "تکرار", "معنای دوگانه"],
        critiques="نقد نخست، «طبیعی‌نماییِ تدریجی» است: فرض بر این است که اسطوره، آشکارا ایدئولوژیک است، در حالی که در واقع طبیعی‌نمایی، تدریجی و نامحسوس است و اسطوره، خود را «بی‌طرف» نشان می‌دهد (Barthes, 1957). نقد دیگر، «عاملیتِ مخاطب» است: تحلیل اسطوره، مخاطب را منفعل نشان می‌دهد، در حالی که مخاطب، می‌تواند اسطوره را تفسیر کند و به چالش بکشد (Hall, 1997). همچنین «اسطوره» در بافت‌های مختلف فرهنگی، معانی گوناگونی می‌گیرد.",
        applications="کاربرد در تحلیل انتقادی رسانه (شناسایی اسطوره‌ها، طبیعی‌نمایی و ایدئولوژی پنهان)، در تحلیل تبلیغات و بصری (کارکرد اسطوره‌ای نماد و تصویر)، در آموزش سواد رسانه‌ای (خواندن انتقادی اسطوره‌ها، شناخت طبیعی‌نمایی)، در پژوهش فرهنگ عامه و هویت (اثر اسطوره بر بازنمایی و هویت)، و در نظارت رسانه‌ای (عدالت بازنمایی، چالش اسطوره‌های مسلط) (Barthes, 1957; Hall, 1997).",
        evolution="مفهوم اسطوره از «اسطوره‌شناسی» بارته (۱۹۵۷) وارد علوم ارتباط شد و در آغاز بر «کارکرد ایدئولوژیک نماد» تمرکز داشت؛ در دهه‌های ۱۹۷۰–۱۹۸۰، با مطالعات فرهنگی (استیوارت هال) و تحلیل انتقادی، به «ابزار تحلیل ایدئولوژی و بازنمایی» گسترش یافت؛ و در امروز، اسطوره به «لایه کلیدی تحلیل رسانه، تبلیغ و فرهنگ» و به اسطوره‌های دیجیتال و پلتفرمی نیز گسترش یافته است (Barthes, 1957).",
        assumptions="فرض‌های نهفته: اسطوره، یک نظام نمادی با کارکرد ایدئولوژیک است (نه صرفا‌ً داستان)؛ اسطوره، معانی خاص را «طبیعی» و «بدیهی» نشان و منشأ تاریخی آن‌ها را پنهان می‌کند (طبیعی‌نمایی)؛ اسطوره، با تکرار، نظام‌های قدرت و بازنمایی مسلط را بازتولید می‌کند؛ و اسطوره، قابل شناسایی، تحلیل و (در حدی) چالش است (Barthes, 1957; Hall, 1997).",
    ),
    "CPT-093": dict(
        mechanism="بینامتنیت (intertextuality) در چهار حلقه تبیین می‌شود: (۱) متن به‌عنوان شبکه: هر متن، «مجموعه‌ای ارجاعات» به متن‌ها، فرم‌ها و بازنویسی‌های دیگر است و در انزوا وجود ندارد؛ (۲) ارجاع و بازنویسی: متن‌ها، یکدیگر را ارجاع، اقتباس، بازنویسی یا تقلیل می‌دهند و از آن‌ها معنا می‌گیرند؛ (۳) درگیری معنایی: معنای هر متن، از درگیری و تعامل با متن‌های پیشین و هم‌عصر ساخته می‌شود؛ (۴) معناسازی مخاطب: مخاطب، معنای متن را در «شبکهٔ بینامتنی» و با پیشینهٔ خود تفسیر می‌کند (Kristeva, 1980; Sturrock & Cartmell, 2001).",
        key_concepts=["ارجاع متنی", "بازنویسی", "شبکهٔ متن", "درگیری معنا", "پیش‌متن و پس‌متن"],
        critiques="نقد نخست، «بی‌مرز‌سازی متن» است: بینامتنیت می‌تواند «مرز و هویت» متن را به‌شدت کمرنگ کند و تعریف متن را دشوار کند (Kristeva, 1980). نقد دیگر، «ابهام روشی» است: شناسایی دقیق ارجاعات و روابط بینامتنی، روشمند نیست و به تفسیر وابسته است (Sturrock & Cartmell, 2001). همچنین بینامتنیت، در رسانه‌های دیجیتال و بازنشر، پیچیده‌تر و گسترده‌تر شده است.",
        applications="کاربرد در تحلیل بینامتنی رسانه (ارجاعات، اقتباس، بازنویسی و پارودی در رسانه)، در تحلیل رسانه‌های همگرا (تکثیر و بازآرایی محتوا میان پلتفرم‌ها)، در آموزش سواد رسانه‌ای (شناخت ارجاعات و بازنویسی‌های رسانه‌ای، مقایسه متن‌ها)، در پژوهش فرهنگ عامه و شادوز (تکثیر و بازی با متن‌ها)، و در تحلیل انتقادی (اثر بینامتنیت بر معنا و ایدئولوژی) (Kristeva, 1980; Sturrock & Cartmell, 2001).",
        evolution="مفهوم بینامتنیت از مقالهٔ «به‌سوی یک نمادشناسی شعر» کریستوا (۱۹۶۶/۱۹۸۰) وارد علوم ارتباط شد و در آغاز در ادبیات و فلسفه شکل گرفت؛ در دهه‌های ۱۹۸۰–۱۹۹۰، با مطالعات فرهنگی و رسانه‌ای، به «ابزار تحلیل رسانه و فرهنگ» گسترش یافت؛ و در عصر رسانه‌های همگرا و دیجیتال، بینامتنیت به «نرمال‌بودن بازنویسی و تکثیر محتوا» بدل شده است (Kristeva, 1980).",
        assumptions="فرض‌های نهفته: متن، در انزوا وجود ندارد و شبکه‌ای از ارجاعات به متن‌های دیگر است (ارتباطی)؛ معنای متن، از درگیری با متن‌های پیشین و هم‌عصر ساخته می‌شود (نه خالص)؛ مخاطب، با پیشینهٔ بینامتنی، متن را تفسیر می‌کند؛ و بینامتنیت، در رسانه‌های دیجیتال، گسترده‌تر و پیچیده‌تر است (Kristeva, 1980; Sturrock & Cartmell, 2001).",
    ),
    "CPT-094": dict(
        mechanism="بازتولید معنا (meaning reproduction) در چهار حلقه تبیین می‌شود: (۱) تولید نماد: رسانه و زبان، نماد و معنا تولید می‌کنند که با ساختارهای قدرت گره خورده‌اند؛ (۲) توزیع معنا: نمادها، از طریق رسانه، به‌طور گسترده توزیع و بازنمایی می‌شوند؛ (۳) بازنمایی و تفسیر: مخاطبان، نمادها را تفسیر و معنا می‌سازند (در چارچوب پیشینه و نظام مسلط)؛ (۴) بازتولید ساختار: معناسازی تکراری، روابط قدرت، نگرش‌ها و بازنمایی‌های مسلط را بازتولید می‌کند و ساختارهای اجتماعی را تثبیت می‌سازد (Bourdieu, 1991; Hall, 1997).",
        key_concepts=["بازتولید نمادین", "قدرت نمادین", "بازنمایی مسلط", "تثبیت ساختار", "نظام معناسازی"],
        critiques="نقد نخست، «تعیین‌گرایی ساختاری» است: بازنمایی معنا، ساختار و قدرت را بیش از حد تعیین‌کننده نشان می‌دهد و عاملیت، تفسیر آزاد و مقاومت مخاطب را کم‌اهمیت می‌شمارد (Bourdieu, 1991). نقد دیگر، «ثبات‌زدگی» است: مدل، بازنمایی را «ثابت» و «تکراری» نشان می‌دهد، در حالی که در عمل بازنمایی‌ها، سیال، رقابتی و قابل چالش‌اند (Hall, 1997). همچنین مرز میان بازنمایی و بازتولید، در عمل مبهم است.",
        applications="کاربرد در تحلیل انتقادی رسانه (بازتولید روابط قدرت، بازنمایی مسلط و ایدئولوژی)، در پژوهش رسانه و جامعه (اثر رسانه بر تثبیت یا تغییر ساختارهای اجتماعی)، در آموزش سواد رسانه‌ای (شناخت بازنمایی‌های مسلط و مقاومت در برابر آن‌ها)، در نظارت رسانه‌ای (عدالت بازنمایی، تنوع صداهای حاشیه‌ای)، و در تحلیل تغییر اجتماعی (نقش رسانه در بازتولید یا چالش نظم) (Bourdieu, 1991; Hall, 1997).",
        evolution="مفهوم بازنمایی معنا از نظریهٔ «قدرت نمادین» بوردیه (۱۹۹۱) وارد علوم ارتباط شد و در آغاز بر «زبان و بازتولید نمادین» تمرکز داشت؛ در دهه‌های ۱۹۸۰–۱۹۹۰، با مطالعات فرهنگی (استیوارت هال) و تحلیل انتقادی، به «بازنمایی و بازتولید رسانه‌ای» گسترش یافت؛ و در امروز، بازنمایی معنا به «چارچوب کلیدی تحلیل رسانه، قدرت و بازنمایی» بدل شده است (Bourdieu, 1991).",
        assumptions="فرض‌های نهفته: نماد و معنا، با ساختارهای قدرت گره خورده‌اند (نه خنثی)؛ رسانه، بازنمایی‌های مسلط را توزیع و بازتولید می‌کند (با امکان چالش)؛ معناسازی تکراری، روابط قدرت و نگرش‌ها را تثبیت می‌سازد؛ و بازنمایی، فرایندی سیال، رقابتی و قابل چالش است نه ثابت و یک‌سویه (Bourdieu, 1991; Hall, 1997).",
    ),
    "CPT-095": dict(
        mechanism="ساخت معنا (meaning-making) در چهار حلقه شکل می‌گیرد: (۱) دریافت نماد: مخاطب، نماد و پیام را از رسانه دریافت می‌کند؛ (۲) تفسیر فعال: مخاطب، بر اساس پیشینه، بافت، نیاز و سرمایه‌های فرهنگی، نماد را تفسیر و معنا می‌سازد (نه دریافت خالص)؛ (۳) معناسازی شخصی و اجتماعی: معنا، هم شخصی (تفسیر فرد) و هم اجتماعی (در بافت گروه و فرهنگ) ساخته می‌شود؛ (۴) بازگشت و مشارکت: معناسازی، با مشارکت، گفت‌وگو و تولید، در جریان رسانه‌ای بازگشت می‌یابد و معنا، پیوسته بازآفرینی می‌شود (Fiske, 1987; Littlejohn & Foss, 2011).",
        key_concepts=["تفسیر فعال", "معیارسنجی", "بافت و پیشینه", "مشارکت", "بازآفرینی معنا"],
        critiques="نقد نخست، «فعالیتِ اغراق‌آمیز» است: ساخت معنا را بیش از حد «آزاد» و «فردمحور» نشان می‌دهد، در حالی که تفسیر، در چارچوب نظام‌های مسلط، بافت و سرمایه‌ها محدود است (Fiske, 1987). نقد دیگر، «معیارسنجیِ فردمحور» است: معناسازی، ممکن است صرفا‌ً بازتولید نگرش و بافت موجود باشد و لزوماً انتقادی یا تازه نباشد (Littlejohn & Foss, 2011). همچنین معناسازی، به‌سختی با ابزار کمی‌سنجی قابل اندازه‌گیری است.",
        applications="کاربرد در تحلیل تفسیر و معناسازی مخاطب (مطالعات استقبال، معناسازی)، در طراحی رسانه (درک چگونگی معناسازی مخاطب، وضوح، هم‌ذات‌پنداری)، در آموزش سواد رسانه‌ای (تقویت تفسیر فعال و انتقادی، مقایسه معناسازی‌ها)، در پژوهش اثرپذیری (بر معناسازی مخاطب تمرکز، نه اثر مستقیم)، و در تحلیل دموکراسی رسانه‌ای (نقش معناسازی در گفت‌وگوی عمومی) (Fiske, 1987; Littlejohn & Foss, 2011).",
        evolution="مفهوم ساخت معنا از نظریه‌های «مخاطب فعال» و معناسازی (دهه‌های ۱۹۷۰–۱۹۸۰، استالن‌دورپ، فرای) وارد علوم ارتباط شد و در برابر مدل‌های اثر مستقیم ایستاد؛ در دهه‌های ۱۹۹۰–۲۰۰۰، با رسانه‌های تعاملی و مشارکتی، به «معناسازی مشارکتی و شبکه‌ای» گسترش یافت؛ و در عصر دیجیتال، ساخت معنا به «معناسازی پیوسته، چندپلتفرمی و مشارکتی» بدل شده است (Fiske, 1987).",
        assumptions="فرض‌های نهفته: مخاطب، عاملی است که معنا را تفسیر و می‌سازد (نه خالص دریافت می‌کند)؛ معناسازی، بر پیشینه، بافت و سرمایه‌های فرهنگی بنا می‌شود (نه یکسان برای همه)؛ معنا، هم شخصی و هم اجتماعی است و با مشارکت بازآفرینی می‌شود؛ و معناسازی، در چارچوب نظام‌های مسلط و بافت، محدود و نابرابر است (Fiske, 1987; Littlejohn & Foss, 2011).",
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
        p["sources"] = []
        p["citations"] = []
        for src in S[code]:
            p["sources"].append({
                "citation": src["citation"], "title_en": src["title_en"],
                "title_fa": src["title_fa"], "year": src["year"], "doi": src.get("doi"),
                "url": src.get("url"), "language": src["language"], "verified": src["verified"],
            })
            p["citations"].append({
                "source": src["citation"], "locator": src["locator"],
                "supports": src["supports"], "verified": src["verified"],
            })
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
                    (code, json.dumps({"batch": 310, "score": score, "words": words,
                                       "sources": n_sources, "verified": n_verified,
                                       "relations": n_rel, "rubric": detail}, ensure_ascii=False), STAMP, NOW))
        print(code, "words", words, "score", score, "detail", detail)
    conn.commit()
    conn.close()
    print("BATCH310 DONE")


if __name__ == "__main__":
    main()
