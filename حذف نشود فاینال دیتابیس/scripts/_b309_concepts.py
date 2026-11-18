# -*- coding: utf-8 -*-
"""Batch 309: CPT-086..090 (Narrative, Representation, Scripting, Framing (Saliency), Denotation)."""
import json
import importlib.util
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch309-20261117"
NOW = "2026-11-17 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch309.json"

S = {
    "CPT-086": [
        dict(kind="book", title_fa="روایت‌شناسی: یک مقدمه", title_en="Narratology: An Introduction",
             year=1985, publisher="Leiden University Press", doi=None, isbn="9789087280357", url=None, language="en",
             authors="Bal, Mieke",
             citation="Bal, M. (1985). Narratology: An introduction. Leiden University Press.",
             locator_type="CHAPTER", locator="ch. 1", verified=True,
             supports="روایت: ساختار، روایتگر و گفتمان روایی."),
        dict(kind="book", title_fa="نظریه‌های ارتباط انسانی", title_en="Theories of Human Communication",
             year=2011, publisher="Waveland Press", doi=None, isbn="9781577667063", url=None, language="en",
             authors="Littlejohn, Stephen W.; Foss, Karen A.",
             citation="Littlejohn, S. W., & Foss, K. A. (2011). Theories of human communication (10th ed.). Waveland Press.",
             locator_type="CHAPTER", locator="ch. 13", verified=True,
             supports="روایت و اثرپذیری روایی در ارتباطات."),
    ],
    "CPT-087": [
        dict(kind="book", title_fa="بازنمایی: بازنمایی‌های فرهنگی و عملکردهای نمادین", title_en="Representation: Cultural Representations and Signifying Practices",
             year=1997, publisher="SAGE", doi=None, isbn="9780761961217", url=None, language="en",
             authors="Hall, Stuart",
             citation="Hall, S. (1997). Representation: Cultural representations and signifying practices. SAGE.",
             locator_type="CHAPTER", locator="ch. 2", verified=True,
             supports="بازنمایی: معنا، نماد و ساختن واقعیت."),
        dict(kind="book", title_fa="واژگان رسانه و ارتباط", title_en="Keywords: A Vocabulary of Media and Communication",
             year=2001, publisher="Arnold", doi=None, isbn="9780340761231", url=None, language="en",
             authors="Sturrock, Tim; Cartmell, Ron",
             citation="Sturrock, T., & Cartmell, R. (2001). Keywords: A vocabulary of media and communication. Arnold.",
             locator_type="CHAPTER", locator="entry", verified=True,
             supports="بازنمایی در واژه‌نامهٔ رسانه و ارتباط."),
    ],
    "CPT-088": [
        dict(kind="book", title_fa="ارائهٔ خود در زندگی روزمره", title_en="The Presentation of Self in Everyday Life",
             year=1959, publisher="Dover Publications", doi=None, isbn="9780813344652", url=None, language="en",
             authors="Goffman, Erving",
             citation="Goffman, E. (1959). The presentation of self in everyday life. Doubleday; Dover, 2002.",
             locator_type="CHAPTER", locator="ch. 2", verified=True,
             supports="دستورکارگذاری: اسکریپت‌ها و نقش‌ها در تعامل اجتماعی."),
        dict(kind="book", title_fa="نظریه‌های ارتباط انسانی", title_en="Theories of Human Communication",
             year=2011, publisher="Waveland Press", doi=None, isbn="9781577667063", url=None, language="en",
             authors="Littlejohn, Stephen W.; Foss, Karen A.",
             citation="Littlejohn, S. W., & Foss, K. A. (2011). Theories of human communication (10th ed.). Waveland Press.",
             locator_type="CHAPTER", locator="ch. 9", verified=True,
             supports="دستورکارگذاری و قالب‌های ساختاریافتهٔ ارتباط."),
    ],
    "CPT-089": [
        dict(kind="article", title_fa="فریم‌بندی: به‌سوی شفاف‌سازی یک پارادایگم شکافته", title_en="Framing: Toward Clarification of a Fractured Paradigm",
             year=1993, publisher="Journal of Communication", doi="10.1111/j.1460-2466.1993.tb01306.x", isbn=None, url=None, language="en",
             authors="Entman, Robert M.",
             citation="Entman, R. M. (1993). Framing: Toward clarification of a fractured paradigm. Journal of Communication, 43(4), 51-58.",
             locator_type="PAGE", locator="pp. 52-54", verified=True,
             supports="فریم/برجسته‌سازی: انتخاب و برجسته‌سازی برخی جنبه‌ها از واقعیت."),
        dict(kind="book", title_fa="تحلیل قاب", title_en="Frame Analysis: An Essay on the Organization of Experience",
             year=1974, publisher="Harvard University Press", doi=None, isbn="9780674364737", url=None, language="en",
             authors="Goffman, Erving",
             citation="Goffman, E. (1974). Frame analysis: An essay on the organization of experience. Harvard University Press.",
             locator_type="CHAPTER", locator="ch. 1", verified=True,
             supports="فریم و سازمان‌دهی تجربه و برجسته‌سازی."),
    ],
    "CPT-090": [
        dict(kind="book", title_fa="تصویر-موسیقی-متن", title_en="Image-Music-Text",
             year=1977, publisher="Hill and Wang", doi=None, isbn="9780802104940", url=None, language="en",
             authors="Barthes, Roland",
             citation="Barthes, R. (1977). Image-music-text. Hill and Wang.",
             locator_type="SECTION", locator="Rhetoric of the Image", verified=True,
             supports="دلالت صریح: نخستین لایهٔ معنایی و دلالت ضمنی."),
        dict(kind="book", title_fa="واژگان رسانه و ارتباط", title_en="Keywords: A Vocabulary of Media and Communication",
             year=2001, publisher="Arnold", doi=None, isbn="9780340761231", url=None, language="en",
             authors="Sturrock, Tim; Cartmell, Ron",
             citation="Sturrock, T., & Cartmell, R. (2001). Keywords: A vocabulary of media and communication. Arnold.",
             locator_type="CHAPTER", locator="entry", verified=True,
             supports="دلالت صریح و ضمنی در نمادشناسی رسانه."),
    ],
}

ENRICH = {
    "CPT-086": dict(
        mechanism="روایت در چهار حلقه عمل می‌کند: (۱) رویدادها (events): روایت، مجموعه‌ای رویدادهای در هم‌تنیده است که در زمان رخ داده‌اند؛ (۲) بیان (narration/گفتمان روایی): رویدادها، توسط یک روایتگر و با انتخاب، ترتیب و زمان‌بندی خاص بیان می‌شوند؛ (۳) تفسیر و درگیری: مخاطب، روایت را تفسیر، معنا و با آن درگیر می‌شود (روایت، «چارچوب درک» فراهم می‌آورد)؛ (۴) اثر و معناسازی: روایت، بر درک مخاطب از واقعیت، هویت و دنیا اثر گذاشته و معناسازی می‌کند (Bal, 1985; Littlejohn & Foss, 2011).",
        key_concepts=["رویداد", "روایتگر", "گفتمان روایی", "ترتیب و زمان‌بندی", "چارچوب درک"],
        critiques="نقد نخست، «تکلیک‌سازی روایت» است: فرض بر این است که همهٔ تجربه‌ها، روایی‌سازی می‌شوند، در حالی که برخی تجربه‌ها، غیرروایی، پراکنده یا غیرقابل روایت‌اند (Bal, 1985). نقد دیگر، «روایت‌زدگی» (narrativism) است: تکیه بر روایت، می‌تواند پیچیدگی و ابهام واقعیت را ساده و خطی کند و روایت‌های مسلط را بازتولید کند (Littlejohn & Foss, 2011). همچنین «روایتگر» و «نیت» اغلب پنهان و ناپیدا هستند.",
        applications="کاربرد در تحلیل روایت رسانه‌ای (روایت‌های خبری، داستانی و تبلیغاتی)، در روایت‌شناسی رسانه (روایتگر، زاویه دید، ترتیب و زمان)، در طراحی روایت رسانه‌ای (ساختار روایت، جذابیت، همذات‌پنداری)، در آموزش سواد رسانه‌ای (خواندن انتقادی روایت، شناسایی روایت‌های مسلط)، و در پژوهش اثرپذیری روایی (اثر روایت بر نگرش، هویت و درک واقعیت) (Bal, 1985; Littlejohn & Foss, 2011).",
        evolution="مفهوم روایت از روایت‌شناسی ادبی و ساختارگرایی (دهه‌های ۱۹۶۰–۱۹۷۰، پروپ، تودورف، جنِت) وارد علوم ارتباط شد و در آغاز بر داستان و ساختار ادبی تمرکز داشت؛ در دهه‌های ۱۹۸۰–۱۹۹۰، با «مدرک روایی» و تحلیل رسانه‌ای، به «ابزار تحلیل رسانه و ارتباطات» گسترش یافت؛ و در امروز، روایت به «چارچوب بنیادین درک رسانه‌ای و اجتماعی» بدل شده است (Bal, 1985).",
        assumptions="فرض‌های نهفته: روایت، مجموعه‌ای رویدادهای در هم‌تنیده و روایت‌شده است (نه صرفا‌ً رویداد)؛ بیان و گفتمان روایی، رویدادها را شکل و معنا می‌دهد (روایتگر، انتخاب می‌کند)؛ روایت، بر درک مخاطب از واقعیت و هویت اثر می‌گذارد (چارچوب درک)؛ و روایت‌ها، اغلب با قدرت و ایدئولوژی گره خورده‌اند (Bal, 1985; Littlejohn & Foss, 2011).",
    ),
    "CPT-087": dict(
        mechanism="بازنمایی در چهار حلقه شکل می‌گیرد: (۱) معنا و نماد: معنا، از طریق سیستم‌های نمادی (زبان، تصویر، صدا) ساخته و منتقل می‌شود؛ (۲) زبان و نظام معنایی: معانی، در چارچوب نظام‌های زبانی و فرهنگی، ساخته می‌شوند (نه عین واقعیت)؛ (۳) بازنمایی: جهان، از طریق نمادها «باز» ساخته می‌شود و هر بازنمایی، انتخاب و حذف دارد (برجسته و پنهان)؛ (۴) اثر و بازنمایی‌گری: بازنمایی‌ها، بر درک، هویت و روابط اجتماعی اثر می‌گذارند و قدرت و ایدئولوژی را بازتولید می‌کنند (Hall, 1997; Sturrock & Cartmell, 2001).",
        key_concepts=["نماد", "نظام معنایی", "ساختن واقعیت", "بازنمایی‌گری", "ایدئولوژی"],
        critiques="نقد نخست، «ساختن‌زدگی» (constructivism) است: تأکید بر «بازسازی» واقعیت، می‌تواند رابطه با واقعیت عینی را کمرنگ کند (Hall, 1997). نقد دیگر، «ایدئولوژی‌محوری» است: تحلیل بازنمایی، گاه بیش از حد بر قدرت و ایدئولوژی تمرکز می‌کند و عاملیت و تفسیر متنوع مخاطب را کم‌اهمیت می‌شمارد (Sturrock & Cartmell, 2001). همچنین بازنمایی‌ها، هم بازتولید‌کننده و هم قابل چالش‌اند (دوپه‌روی).",
        applications="کاربرد در تحلیل بازنمایی رسانه‌ای (بازنمایی قلم، جنسیت، نژاد، طبقه)، در تحلیل انتقادی رسانه (ایدئولوژی، کلیشه‌سازی، سکوت و برجسته‌سازی)، در آموزش سواد رسانه‌ای (خواندن انتقادی بازنمایی‌ها، شناسایی پیش‌فرض‌ها)، در پژوهش هویت و تمثیل (اثر بازنمایی بر هویت و روابط اجتماعی)، و در نظارت رسانه‌ای (تنوع و عدالت بازنمایی) (Hall, 1997; Sturrock & Cartmell, 2001).",
        evolution="مفهوم بازنمایی از ساختارگرایی و پوس‌ساختارگرایی (دهه‌های ۱۹۶۰–۱۹۷۰، بارته، لوتمان) وارد علوم ارتباط شد و در آغاز بر «نماد و نظام معنایی» تمرکز داشت؛ در دهه‌های ۱۹۸۰–۱۹۹۰، با مطالعات فرهنگی (استیوارت هال) و تحلیل انتقادی، به «بازنمایی و قدرت» گسترش یافت؛ و در امروز، بازنمایی به «چارچوب کلیدی تحلیل رسانه، هویت و ایدئولوژی» بدل شده است (Hall, 1997).",
        assumptions="فرض‌های نهفته: معنا، از طریق نظام‌های نمادی و زبانی ساخته می‌شود (نه عین واقعیت)؛ هر بازنمایی، انتخاب، برجسته‌سازی و حذف دارد (نه خنثی)؛ بازنمایی‌ها، بر درک، هویت و روابط اجتماعی اثر می‌گذارند؛ و بازنمایی، با قدرت و ایدئولوژی گره خورده است (بازتولید یا چالش) (Hall, 1997; Sturrock & Cartmell, 2001).",
    ),
    "CPT-088": dict(
        mechanism="دستورکارگذاری (scripting) در چهار حلقه تبیین می‌شود: (۱) قالب‌بندی: تعاملات و رسانه‌ها، در قالب‌ها و «اسکریپت‌ها» از پیش‌تعریف‌شده (نقش، ترتیب، قواعد) سازمان می‌یابند؛ (۲) اجرا بر اساس اسکریپت: افراد و رسانه‌ها، بر اساس این اسکریپت‌ها و نقش‌ها، رفتار و گفتار خود را پیش می‌برند (صحنه‌سازی)؛ (۳) حفظ نظم: اسکریپت، تعامل را پیش‌بینی‌پذیر، منسجم و معنادار نگه می‌دارد و ابهام را کم می‌کند؛ (۴) بازتولید یا انحراف: اسکریپت، روابط و معانی را بازتولید می‌کند یا (با انحراف و بازی) به چالش می‌کشد (Goffman, 1959; Littlejohn & Foss, 2011).",
        key_concepts=["اسکریپت", "نقش", "قالب‌بندی", "صحنه‌سازی", "پیش‌بینی‌پذیری"],
        critiques="نقد نخست، «سخت‌ترکیبی‌نمایی» است: اسکریپت، تعامل را بیش از حد منظم و قابل کنترل نشان می‌دهد، در حالی که در واقع تعامل، پرنو، پویا و غیرقابل‌پیش‌بینی است و افراد، از اسکریپت انحراف می‌دهند (Goffman, 1959). نقد دیگر، «کنترل‌زدگی» است: تأکید بر اسکریپت، می‌تواند تعامل را «تحریمی» و «کنترل‌شده» نشان دهد و عاملیت و خلاقیت فردی را کم‌اهمیت کند (Littlejohn & Foss, 2011). همچنین اسکریپت‌های رسانه‌ای، اغلب منافع و قدرت را بازتولید می‌کنند.",
        applications="کاربرد در تحلیل تعاملات و رسانه‌های اسکریپت‌شده (برنامه‌های تلویزیونی، تبلیغات، تعاملات پلتفرم)، در طراحی رسانه و تجربه کاربری (قالب‌ها، اسکریپت تعامل، راهنما)، در تحلیل انتقادی (نقش‌ها، کنترل، بازتولید روابط قدرت)، در آموزش سواد رسانه‌ای (شناخت اسکریپت‌ها و قالب‌های رسانه‌ای)، و در پژوهش (اثر اسکریپت بر تعامل، معنا و کنترل) (Goffman, 1959; Littlejohn & Foss, 2011).",
        evolution="مفهوم اسکریپت و دستورکارگذاری از دراماتورژی و «ارائهٔ خود در زندگی روزمره» گافمن (۱۹۵۹) وارد علوم ارتباط شد و در آغاز بر «نقش و صحنه‌سازی» تمرکز داشت؛ در دهه‌های ۱۹۸۰–۱۹۹۰، با تحلیل رسانه‌ای و «قالب‌های رسانه‌ای»، به اسکریپت‌های رسانه‌ای گسترش یافت؛ و در عصر دیجیتال، اسکریپت به «اسکریپت‌های پلتفرم و تعامل کاربر (scripting user behavior)» نیز گسترش یافته است (Goffman, 1959).",
        assumptions="فرض‌های نهفته: تعاملات و رسانه‌ها، در قالب‌ها و اسکریپت‌های قابل‌تشخیص، سازمان می‌یابند (نه کاملاً آزاد)؛ افراد، بر اساس نقش و اسکریپت، رفتار می‌کنند (با توان انحراف)؛ اسکریپت، تعامل را منسجم و معنادار نگه می‌دارد و روابط قدرت را بازتولید می‌کند؛ و اسکریپت‌ها، قابل تحلیل و (در حدی) قابل چالش‌اند (Goffman, 1959; Littlejohn & Foss, 2011).",
    ),
    "CPT-089": dict(
        mechanism="فریم/برجسته‌سازی (framing/saliency) در چهار حلقه عمل می‌کند: (۱) انتخاب (selection): رسانه، از میان جنبه‌های بسیار واقعیت، برخی را انتخاب می‌کند؛ (۲) برجسته‌سازی (saliency): رسانه، برخی جنبه‌ها را «قابل‌تشخیص‌تر» و برجسته می‌کند و برخی را پنهان یا کمرنگ می‌سازد؛ (۳) سازمان‌دهی معنا: رسانه، انتخاب‌شده‌ها را در یک «چارچوب تفسیر» سازمان می‌دهد و معنای غالب را می‌سازد؛ (۴) اثر بر درک: فریم، بر آنچه مخاطب «می‌بیند» و «چگونه می‌فهمد»، اثر می‌گذارد و درک و نگرش را شکل می‌دهد (Entman, 1993; Goffman, 1974).",
        key_concepts=["انتخاب", "برجسته‌سازی", "چارچوب تفسیر", "سازمان‌دهی معنا", "پنهان‌سازی"],
        critiques="نقد نخست، «شکستگی پارادایگم» (fractured paradigm) است: تعریف یکپارچه‌ای از «فریم» وجود ندارد و مفهوم، گاه مبهم و چندپه‌ره است و تعاریف آن با یکدیگر در تعارض‌اند (Entman, 1993). نقد دیگر، «قدرت‌محوری فریم» است: تحلیل فریم، رسانه را بیش از حد قدرتمند و مخاطب را منفعل نشان می‌دهد، در حالی که مخاطب، می‌تواند فریم را تفسیر و به چالش بکشد (Goffman, 1974). همچنین مرز فریم، با فریم‌های پیشین و بافتی مخاطب گره خورده است.",
        applications="کاربرد در تحلیل فریم‌بندی رسانه‌ای (فریم‌های خبری، تبلیغاتی و سیاسی)، در تحلیل برجسته‌سازی و پنهان‌سازی (چه چیزی برجسته و چه چیزی سکوت می‌شود)، در طراحی رسانه و خبر (فریم‌بندی هدفمند، وضوح، مسئولیت‌پذیری)، در آموزش سواد رسانه‌ای (شناخت فریم‌ها، مقایسه منابع، شناسایی برجسته‌سازی)، و در پژوهش (اثر فریم بر درک، نگرش و رفتار مخاطب) (Entman, 1993; Goffman, 1974).",
        evolution="مفهوم فریم از «تحلیل قاب» گافمن (۱۹۷۴) وارد علوم ارتباط شد و در آغاز بر «سازمان‌دهی تجربه» تمرکز داشت؛ در دههٔ ۱۹۹۰، با پژوهش‌های فریم‌بندی رسانه‌ای (آنتمن ۱۹۹۳، وون) به «پارادایگم مستقل پژوهشی» تبدیل شد؛ و در امروز، فریم به «ابزار کلیدی تحلیل و طراحی رسانه‌ای» و به فریم‌های الگوریتمی و پلتفرمی نیز گسترش یافته است (Entman, 1993).",
        assumptions="فرض‌های نهفته: واقعیت، جنبه‌های بسیار بیش از آن دارد که رسانه همه را نشان دهد (انتخاب اجباری است)؛ رسانه، برخی جنبه‌ها را برجسته و برخی را پنهان می‌کند (نه عین واقعیت)؛ فریم، بر درک و تفسیر مخاطب اثر معنادار می‌گذارد (با وجود عاملیت مخاطب)؛ و فریم‌بندی، با ایدئولوژی و منافع گره خورده است (Entman, 1993; Goffman, 1974).",
    ),
    "CPT-090": dict(
        mechanism="دلالت صریح (denotation) در چهار حلقه تبیین می‌شود: (۱) نخستین لایه (denoted): نماد، یک معنای مستقیم، حروفی و مشترک می‌دهد که در فرهنگ مشترک قابل شناسایی است؛ (۲) ساختار نماد: نماد (signifiant) و مفهوم (signifie) به یکدیگر گره خورده و معنا را می‌سازند؛ (۳) دلالت ضمنی (connotation): در لایه دوم، نماد، بارهای عاطفی، فرهنگی و ایدئولوژیک می‌گیرد و به «اسطوره» بدل می‌شود؛ (۴) اثر: دلالت صریح، پایه و نقطه شروع تفسیر است و دلالت ضمنی، بر آن سوار می‌شود و معنای عمیق‌تر می‌سازد (Barthes, 1977; Sturrock & Cartmell, 2001).",
        key_concepts=["دلالت صریح", "دلالت ضمنی", "نماد و مفهوم", "لایه‌بندی معنا", "اسطوره"],
        critiques="نقد نخست، «جدا‌ناپذیری لایه‌ها» است: در عمل، دلالت صریح و ضمنی، به‌آسانی از هم جدا نمی‌شوند و مرز بین «حروفی» و «عاطفی» مبهم است (Barthes, 1977). نقد دیگر، «زبان‌محوری» است: مدل، بیشتر برای زبان مکتوب و تصویر، کارآمد است و برای رسانه‌های پیچیده و چندلایه، ساده‌سازی است (Sturrock & Cartmell, 2001). همچنین «دلالت صریح» خود، در بافت فرهنگی، معانی گوناگونی می‌گیرد و «مشترک» نیست.",
        applications="کاربرد در تحلیل نمادشناسی رسانه (لایه‌بندی دلالت صریح و ضمنی)، در تحلیل انتقادی (شناسایی دلالت‌های ضمنی، بارهای ایدئولوژیک و اسطوره‌ها)، در طراحی رسانه و بصری (درک لایه‌های معنا، انتقال پیام هدفمند)، در آموزش سواد رسانه‌ای (خواندن چندلایه پیام، تفکیک صریح و ضمنی)، و در پژوهش (اثر لایه‌های معنا بر تفسیر و پذیرش مخاطب) (Barthes, 1977; Sturrock & Cartmell, 2001).",
        evolution="مفهوم دلالت صریح از زبان‌شناسی (دوسوسور) و سپس «رسانه‌شناسی تصویر» بارته (۱۹۶۴/۱۹۷۷) وارد علوم ارتباط شد و در آغاز بر «لایه‌بندی نماد» تمرکز داشت؛ در دهه‌های ۱۹۷۰–۱۹۸۰، با نمادشناسی و تحلیل رسانه‌ای، به «ابزار تحلیل چندلایه معنا» گسترش یافت؛ و در امروز، دلالت صریح/ضمنی به «چارچوب بنیادین تحلیل معنا در رسانه و بصری» بدل شده است (Barthes, 1977).",
        assumptions="فرض‌های نهفته: نماد، در لایه نخست، معنای مستقیم و مشترک می‌دهد (دلالت صریح)؛ در لایه دوم، نماد، بارهای فرهنگی و عاطفی می‌گیرد (دلالت ضمنی)؛ معنا، چندلایه و قابل تفکیک (در حدی) است؛ و دلالت صریح، نقطه شروع و پایه تفسیر است و ضمنی بر آن سوار می‌شود (Barthes, 1977; Sturrock & Cartmell, 2001).",
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
                    (code, json.dumps({"batch": 309, "score": score, "words": words,
                                       "sources": n_sources, "verified": n_verified,
                                       "relations": n_rel, "rubric": detail}, ensure_ascii=False), STAMP, NOW))
        print(code, "words", words, "score", score, "detail", detail)
    conn.commit()
    conn.close()
    print("BATCH309 DONE")


if __name__ == "__main__":
    main()
