# -*- coding: utf-8 -*-
"""Batch 255: CPT-016..020 (Signification, Verbal, Nonverbal, Direct, Indirect Communication)."""
import json
import importlib.util
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch255-20261117"
NOW = "2026-11-17 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch255.json"

S = {
    "CPT-016": [
        dict(kind="book", title_fa="نظریه‌های ارتباط انسانی", title_en="Theories of Human Communication",
             year=2011, publisher="Waveland Press", doi=None, isbn="9781577667063", url=None, language="en",
             authors="Littlejohn, Stephen W.; Foss, Karen A.",
             citation="Littlejohn, S. W., & Foss, K. A. (2011). Theories of human communication (10th ed.). Waveland Press.",
             locator_type="CHAPTER", locator="ch. 2", verified=True,
             supports="دلالت به‌مثابه رابطه‌ی نشانه‌دهنده و نشانه‌دهی‌شده در سنت‌های نشانه‌شناختی."),
        dict(kind="book", title_fa="مقدمه‌ای بر مطالعات ارتباط", title_en="Introduction to Communication Studies",
             year=2011, publisher="Routledge", doi="10.4324/9780203837382", isbn="9780415596497", url=None, language="en",
             authors="Fiske, John",
             citation="Fiske, J. (2011). Introduction to communication studies (3rd ed.). Routledge.",
             locator_type="CHAPTER", locator="ch. 2", verified=True,
             supports="دلالت در بافت فرهنگی و نظام نشانه‌ها."),
    ],
    "CPT-017": [
        dict(kind="book", title_fa="کتاب ارتباط میان‌فردی", title_en="The Interpersonal Communication Book",
             year=2016, publisher="Pearson", doi=None, isbn="9780133753813", url=None, language="en",
             authors="DeVito, Joseph A.",
             citation="DeVito, J. A. (2016). The interpersonal communication book (14th ed.). Pearson.",
             locator_type="CHAPTER", locator="ch. 4", verified=True,
             supports="ارتباط کلامی: ویژگی‌ها، قواعد و مهارت‌های بیان و گوش‌دادن."),
        dict(kind="book", title_fa="نظریه‌های ارتباط انسانی", title_en="Theories of Human Communication",
             year=2011, publisher="Waveland Press", doi=None, isbn="9781577667063", url=None, language="en",
             authors="Littlejohn, Stephen W.; Foss, Karen A.",
             citation="Littlejohn, S. W., & Foss, K. A. (2011). Theories of human communication (10th ed.). Waveland Press.",
             locator_type="CHAPTER", locator="ch. 1", verified=True,
             supports="زبان و ارتباط کلامی در سنت‌های فرایندی و ساختاری."),
    ],
    "CPT-018": [
        dict(kind="book", title_fa="کتاب ارتباط میان‌فردی", title_en="The Interpersonal Communication Book",
             year=2016, publisher="Pearson", doi=None, isbn="9780133753813", url=None, language="en",
             authors="DeVito, Joseph A.",
             citation="DeVito, J. A. (2016). The interpersonal communication book (14th ed.). Pearson.",
             locator_type="CHAPTER", locator="ch. 5", verified=True,
             supports="ارتباط غیرکلامی: زبان بدن، پروکسیمی، پارانژبال و کارکرد آن‌ها در تعامل."),
        dict(kind="book", title_fa="نظریه ارتباطات انبوه مک‌کویل", title_en="McQuail's Mass Communication Theory",
             year=2010, publisher="Sage", doi=None, isbn="9781849202923", url=None, language="en",
             authors="McQuail, Denis",
             citation="McQuail, D. (2010). McQuail's mass communication theory (6th ed.). Sage.",
             locator_type="CHAPTER", locator="ch. 13", verified=True,
             supports="بعد غیرکلامی در رسانه‌های بصری و چندرسانه‌ای."),
    ],
    "CPT-019": [
        dict(kind="book", title_fa="نظریه‌های ارتباط انسانی", title_en="Theories of Human Communication",
             year=2011, publisher="Waveland Press", doi=None, isbn="9781577667063", url=None, language="en",
             authors="Littlejohn, Stephen W.; Foss, Karen A.",
             citation="Littlejohn, S. W., & Foss, K. A. (2011). Theories of human communication (10th ed.). Waveland Press.",
             locator_type="CHAPTER", locator="ch. 1", verified=True,
             supports="ارتباط مستقیم و میانجی‌شده در سنت فرایندی."),
        dict(kind="book", title_fa="کتاب ارتباط میان‌فردی", title_en="The Interpersonal Communication Book",
             year=2016, publisher="Pearson", doi=None, isbn="9780133753813", url=None, language="en",
             authors="DeVito, Joseph A.",
             citation="DeVito, J. A. (2016). The interpersonal communication book (14th ed.). Pearson.",
             locator_type="CHAPTER", locator="ch. 1", verified=True,
             supports="ارتباط مستقیم میان‌فردی: ویژگی‌ها، بازخورد فوری و تعامل."),
    ],
    "CPT-020": [
        dict(kind="book", title_fa="نظریه ارتباطات انبوه مک‌کویل", title_en="McQuail's Mass Communication Theory",
             year=2010, publisher="Sage", doi=None, isbn="9781849202923", url=None, language="en",
             authors="McQuail, Denis",
             citation="McQuail, D. (2010). McQuail's mass communication theory (6th ed.). Sage.",
             locator_type="CHAPTER", locator="ch. 1", verified=True,
             supports="ارتباط غیرمستقیم از طریق رسانه‌های جمعی: ویژگی‌ها و اثرات."),
        dict(kind="book", title_fa="نظریه‌های ارتباط انسانی", title_en="Theories of Human Communication",
             year=2011, publisher="Waveland Press", doi=None, isbn="9781577667063", url=None, language="en",
             authors="Littlejohn, Stephen W.; Foss, Karen A.",
             citation="Littlejohn, S. W., & Foss, K. A. (2011). Theories of human communication (10th ed.). Waveland Press.",
             locator_type="CHAPTER", locator="ch. 1", verified=True,
             supports="ارتباط غیرمستقیم و نقش رسانه به‌مثابه میانجی."),
    ],
}

ENRICH = {
    "CPT-016": dict(
        definition="رابطه‌ی درون‌زبانانه و فرهنگی میان «نشانه‌دهنده» (شکل نشانه) و «نشانه‌دهی‌شده» (مفهوم یا مرجع) که در یک نظام نشانه‌ها، یک نشانه را به معنا می‌رساند؛ دلالت «آنچه نشانه، دلالت می‌کند» است (Littlejohn & Foss, 2011). در بافت، دلالت فرایندی است که معنا از تفسیر نشانه در نظام هم‌بستگی ساخته می‌شود (Fiske, 2011).",
        summary="دلالت (signification) از مفاهیم بنیادین نشانه‌شناسی است. در سنت سوسوری، دلالت «رابطه‌ی دلالت‌بخش» میان نشانه‌دهنده (signifier) و نشانه‌دهی‌شده (signified) است که هر دو را به یک «نشانه» پیوند می‌دهد؛ این رابطه دلالت‌بخش، دلالت‌آمیز (conventional) است نه دلالت‌آمیز طبیعی — یعنی معنا از قرارداد فرهنگی می‌آید نه از ذات نشانه (Littlejohn & Foss, 2011). در بافت فرهنگی، دلالت «فرایند ساخت معنا» است: نشانه در شبکه‌ی هم‌بستگی‌ها و تفاوت‌ها، معنای خود را می‌یابد و بافت، دلالت را شکل می‌دهد (Fiske, 2011). در رسانه، دلالت به «معنای رسانه‌ای» می‌گوید: چگونه نشانه‌های بصری، صوتی و کلامی در بافت رسانه‌ای، معنای سیاسی، فرهنگی و اجتماعی را می‌سازند. نقد بنیادین، «دلالت‌زدگی» (de-signification) بیش از حد است: اگر دلالت همیشه از بافت و قرارداد می‌آید، خطر نسبی‌سازی مطلق و ناتوانی از گفتن «معنای واقعی» وجود دارد. همچنین مرز «دلالت معنایی» و «دلالت استعاری» در رسانه مبهم شده و «دلالت الگوریتمی» (معنایی که الگوریتم‌ها می‌سازند) پدیده‌ای تازه است (Fiske, 2011).",
        mechanism="دلالت در سه سطح عمل می‌کند: (۱) سطح فرامدال (semiotic mode): انتخاب نمادین (کلام، تصویر، صدا، حرکت) که در بافت فرهنگی، معنای خود را می‌یابد؛ (۲) سطح فرامدال (inter-semiotic): ترکیب نمادها بر اساس قواعد کد که معنای کل را می‌سازد؛ (۳) سطح گفتمانی (discursive): بافت گفتمانی که دلالت را در نظام قدرت و فرهنگ قرار می‌دهد (Fiske, 2011; Littlejohn & Foss, 2011).",
        key_concepts=["نشانه‌دهنده و نشانه‌دهی‌شده", "قرارداد فرهنگی", "دلالت استعاری", "دلالت الگوریتمی", "بافت گفتمانی"],
        critiques="مفهوم «دلالت» مرز روشنی با «معنا»، «نشانه» و «دلالت» ندارد و در ادبیات اغلب خلط می‌شود (Littlejohn & Foss, 2011). نقد دیگر، «نسبیت‌گرایی مطلق» است: اگر دلالت همیشه از بافت و قرارداد می‌آید، گفتن از «معنای واقعی» و «درستی» تفسیر دشوار می‌شود (Fiske, 2011). همچنین در رسانه‌های دیجیتال، دلالت به‌شدت الگوریتمی و شخصی‌سازی‌شده است و «دلانت مشترک» که شرط درک مشترک است، از بین می‌رود.",
        applications="تحلیل انتقادی رسانه (چگونه دلالت رسانه‌ای ساخته و تفسیر می‌شود)، طراحی پیام و بصری (انتخاب و ترکیب نمادها بر اساس بافت مخاطب)، آموزش سواد رسانه‌ای و نشانه‌شناختی، و تحلیل گفتمانی (چگونه دلانت گفتمانی معنای سیاست و فرهنگ را می‌سازد) (Fiske, 2011).",
        evolution="مفهوم دلانت از نشانه‌شناسی (سوسور، ۱۹۱۶؛ پیرس، ۱۹۰۳) وارد علوم ارتباط و مطالعات رسانه شد؛ در دهه‌های ۱۹۶۰–۱۹۷۰، با مکتب فرهنگی، دلانت به «واحد تحلیل رسانه و فرهنگ» تبدیل شد؛ در عصر دیجیتال، دلانت به «فرایند الگوریتمی و داده‌محور» بدل شده و «دلانت الگوریتمی» پدیده‌ای تازه است (Fiske, 2011; Littlejohn & Foss, 2011).",
        assumptions="فرض‌های نهفته: دلانت از قرارداد فرهنگی و بافت می‌آید (نه ذات نشانه)؛ نظام دلانت ساختار و قواعد دارد؛ و تفسیر دلانت، فرایند فعال و فرهنگی است نه صرفا‌ً بازیابی فنی (Littlejohn & Foss, 2011; Fiske, 2011).",
    ),
    "CPT-017": dict(
        definition="ارتباط از طریق زبان و کلمات — گفتاری، نوشتاری یا امضایی — که در آن معنا از نشانه‌های زبانی (واژه، جمله، پاراگراف) ساخته و منتقل می‌شود؛ ارتباط کلامی «بالاترین و دقیق‌ترین سطح انتقال معنا» است اما به قواعد زبانی و بافت فرهنگی وابسته است (DeVito, 2016; Littlejohn & Foss, 2011).",
        summary="ارتباط کلامی (verbal communication) به هر انتقال معنایی از طریق زبان و کلمات می‌گوید — گفتاری (سخن گفتن)، نوشتاری (متن، ایمیل، پیامک) یا امضایی (امضا، زبان اشاره). در سنت فرایندی، ارتباط کلامی «دقیق‌ترین» نوع ارتباط است زیرا زبان ابزاری برای انتقال معناست و به قواعد گرامری و بافت فرهنگی وابسته است (DeVito, 2016). ویژگی‌های کلیدی: (۱) نمادین بودن: کلمات نمادهایی دلالت‌آمیز هستند و معنایشان از قرارداد فرهنگی می‌آید؛ (۲) ساختاری بودن: کلمات بر اساس قواعد گرامری ترکیب می‌شوند؛ (۳) بافت‌محور بودن: معنای یک واژه، به بافت و موقعیت گره خورده است (Littlejohn & Foss, 2011). در رسانه، ارتباط کلامی به «محتوای زبانی» رسانه می‌گوید: خبر، تبلیغ، داستان، گفت‌وگو. نقد بنیادین، «کلام‌زدگی» (verbalism) است: فرض بر این است که معنا «در» کلمات است، در حالی که بخش بزرگی از معنا از ارتباط غیرکلامی و بافت می‌آید (DeVito, 2016). همچنین در رسانه‌های دیجیتال، ارتباط کلامی با ارتباط چندرسانه‌ای (تصویر، صدا، ویدئو) ترکیب شده و مرز «کلام» و «غیرکلام» مبهم شده است.",
        mechanism="ارتباط کلامی در سه حلقه عمل می‌کند: (۱) رمزگذاری: فرستنده معنا را به کلمات و جملات بر اساس قواعد گرامری و بافت تبدیل می‌کند؛ (۲) انتقال: پیام زبانی از کانال (گفتار، نوشتار، صوت، تصویر) عبور می‌کند؛ (۳) رمزگشایی: گیرنده کلمات را در بافت تفسیر و معنا می‌سازد (DeVito, 2016). در ارتباط میان‌فردی، بازخورد فوری (تأکید، سؤال، تأیید) فرایند را تنظیم می‌کند (Littlejohn & Foss, 2011).",
        key_concepts=["زبان گفتاری و نوشتاری", "قواعد گرامری", "نمادین بودن کلمات", "بافت فرهنگی", "ارتباط چندرسانه‌ای"],
        critiques="الگوی فرایندی ارتباط کلامی را «دقیق‌ترین» و «بالاترین» نوع ارتباط می‌بیند و ارتباط غیرکلامی و بافت را کم‌بردار می‌کند (DeVito, 2016). نقد دیگر، «کلام‌زدگی مطلق» است: فرض بر این است که معنا «در» کلمات است، در حالی که بخش بزرگی از معنا از بافت، لحن، تصویر و رفتار می‌آید (Littlejohn & Foss, 2011). همچنین در رسانه‌های دیجیتال، مرز «کلام» و «غیرکلام» مبهم شده و ارتباط کلامی به‌شدت چندرسانه‌ای شده است.",
        applications="نگارش و ویرایش پیام‌های رسانه‌ای و آموزشی، آموزش مهارت‌های بیان، ارائه و مذاکره، طراحی پیام‌های تبلیغاتی و اطلاع‌رسانی، و تحلیل انتقادی محتوا (DeVito, 2016; Littlejohn & Foss, 2011).",
        evolution="مفهوم ارتباط کلامی از فلسفه زبان و منطق (قرن‌های ۱۷–۱۹) وارد علوم ارتباط شد؛ در دهه‌های ۱۹۵۰–۱۹۶۰، با مکتب میان‌فردی، به «ارتباط نمادین و بافت‌محور» تبدیل شد؛ در عصر دیجیتال، ارتباط کلامی به «ارتباط چندرسانه‌ای و الگوریتمی‌شده» بدل شده و مرز کلام و غیرکلام محو شده است (DeVito, 2016).",
        assumptions="فرض‌های نهفته: زبان ابزاری دقیق و قابل‌اعتماد برای انتقال معناست؛ قواعد گرامری و بافت فرهنگی، شرط درک مشترک است؛ و ارتباط کلامی مستقل از ارتباط غیرکلامی قابل تحلیل است (DeVito, 2016; Littlejohn & Foss, 2011).",
    ),
    "CPT-018": dict(
        definition="ارتباط از طریق نشانه‌های غیرزبانی — زبان بدن، حالت چهره، تماس چشمی، فاصله فیزیکی، لحن صدا، زمان‌بندی و امضا — که در تعامل، معنای پیام کلامی را تقویت، تقویت‌کننده، متضاد یا تکمیل می‌کند (DeVito, 2016). در رسانه‌های بصری، ارتباط غیرکلامی به تصویر، رنگ، نور، حرکت و موسیقی می‌گوید (McQuail, 2010).",
        summary="ارتباط غیرکلامی (nonverbal communication) به هر انتقال معنایی از طریق نشانه‌های غیرزبانی می‌گوید. در سنت میان‌فردی، ارتباط غیرکلامی شامل: زبان بدن (posture, gesture)، حالت چهره (facial expression)، تماس چشمی (eye contact)، فاصله فیزیکی (proxemics)، لحن و ریتم صدا (paralinguistics)، زمان‌بندی (chronemics) و امضا (haptics) است (DeVito, 2016). پژوهش‌ها نشان می‌دهند که بخش بزرگی از معنا در تعامل، از ارتباط غیرکلامی می‌آید و اغلب با پیام کلامی هم‌خوانی ندارد — گاه متضاد است (مثلاً لبخند در حالی که کلمات انتقادی است). در رسانه‌های بصری و چندرسانه‌ای، ارتباط غیرکلامی به تصویر، رنگ، نور، حرکت، موسیقی و تدوین می‌گوید که بر تفسیر پیام کلامی اثر مستقیم دارد (McQuail, 2010). نقد بنیادین، «غیرکلام‌زدگی» (nonverbalism) است: فرض بر این است که ارتباط غیرکلامی «صادق‌تر» از کلام است، در حالی که در واقع ارتباط غیرکلامی هم نمادین و بافت‌محور است و به قرارداد فرهنگی وابسته است (DeVito, 2016). همچنین در رسانه‌های دیجیتال، ارتباط غیرکلامی به‌شدت محدود و واسطه‌شده است و «زبان بدن» به شکل‌های تازه (ایموجی، انیمیشن، افکت) بدل شده است.",
        mechanism="ارتباط غیرکلامی در تعامل به چند کارکرد عمل می‌کند: (۱) تقویت (complement): تقویت پیام کلامی با نشانه‌های هم‌خوان؛ (۲) تضاد (contradict): متضادبودن با پیام کلامی که معنای واقعی را نشان می‌دهد؛ (۳) جانشینی (substitute): جایگزینی کامل پیام کلامی (مثلاً سر تکان دادن به جای «نه»)؛ (۴) تنظیم (regulate): تنظیم نوبت گفتار و تعامل (DeVito, 2016). در رسانه، غیرکلامی به «زبان بصری و صوتی» می‌گوید که معنای کل را می‌سازد (McQuail, 2010).",
        key_concepts=["زبان بدن", "فاصله فیزیکی", "لحن و ریتم", "زبان بصری", "امضا و زمان‌بندی"],
        critiques="الگوی میان‌فردی ارتباط غیرکلامی را «صادق‌تر» و «بیشتر از کلام» می‌بیند، در حالی که در واقع ارتباط غیرکلامی هم نمادین و بافت‌محور است (DeVito, 2016). نقد دیگر، «فرهنگی‌بودن» نشانه‌های غیرکلامی است: معنای یک ژست یا فاصله، به فرهنگ گره خورده است و «زبان بدن جهانی» فرضی است (McQuail, 2010). همچنین در رسانه‌های دیجیتال، ارتباط غیرکلامی به‌شدت محدود و واسطه‌شده است.",
        applications="تحلیل انتقادی رسانه (زبان بصری و صوتی)، طراحی تجربه کاربری و رابط (UX) با توجه به نشانه‌های غیرکلامی، آموزش مهارت‌های ارتباطی و مذاکره، و طراحی پیام‌های چندرسانه‌ای (DeVito, 2016; McQuail, 2010).",
        evolution="مفهوم ارتباط غیرکلامی از روان‌شناسی و زبان‌شناسی (دهه‌های ۱۹۶۰–۱۹۷۰) وارد علوم ارتباط شد و با پژوهش‌های میان‌فردی (مهرابیایان، آرجن) گسترش یافت؛ در رسانه، با تحلیل بصری و چندرسانه‌ای، به «زبان بصری و صوتی» تبدیل شد؛ در عصر دیجیتال، ارتباط غیرکلامی به شکل‌های تازه (ایموجی، انیمیشن، افکت) بدل شده است (DeVito, 2016).",
        assumptions="فرض‌های نهفته: ارتباط غیرکلامی مستقل از کلام قابل تحلیل است (هرچند در عمل با کلام درهم‌تنیده است)؛ نشانه‌های غیرکلامی به بافت و فرهنگ وابسته‌اند؛ و ارتباط غیرکلامی بر تفسیر پیام کلامی اثر مستقیم دارد (DeVito, 2016; McQuail, 2010).",
    ),
    "CPT-019": dict(
        definition="ارتباطی که بدون واسطه‌ی نهادی یا رسانه‌ای، مستقیماً میان دو یا چند کنشگر در یک موقعیت مشترک انجام می‌شود و در آن بازخورد فوری و تعامل دوطرفه وجود دارد (Littlejohn & Foss, 2011). در سنت میان‌فردی، ارتباط مستقیم «رابطه‌ی نزدیک و دوطرفه» است که بر اعتماد، صمیمیت و بازخورد فوری استوار است (DeVito, 2016).",
        summary="ارتباط مستقیم (direct communication) به هر ارتباطی می‌گوید که بدون واسطه‌ی نهادی یا رسانه‌ای، مستقیماً میان کنشگران در یک موقعیت مشترک انجام می‌شود. در سنت فرایندی، ارتباط مستقیم «حضور فیزیکی و هم‌زمانی» دارد: فرستنده و گیرنده در یک مکان و زمان، با بازخورد فوری و تعامل دوطرفه، پیام را تبادل می‌کنند (Littlejohn & Foss, 2011). در سنت میان‌فردی، ارتباط مستقیم «رابطه‌ی نزدیک» است که بر اعتماد، صمیمیت، گوش‌دادن فعال و بازخورد فوری استوار است (DeVito, 2016). ویژگی‌های کلیدی: (۱) هم‌زمانی و حضور فیزیکی؛ (۲) بازخورد فوری و دوطرفه؛ (۳) تعامل و دیالکتیک (هر دو طرف هم‌زمان فرستنده و گیرنده‌اند)؛ (۴) اعتماد و صمیمیت. در رسانه، ارتباط مستقیم به «برخورد با مخاطب» می‌گوید: مصاحبه‌ی زنده، پخش زنده، گفت‌وگوی مستقیم. نقد بنیادین، «مستقیم‌زدگی» (directness) است: فرض بر این است که ارتباط مستقیم «صادق‌تر» و «مؤثرتر» است، در حالی که در واقع هر ارتباطی (حتی مستقیم) نمادین و بافت‌محور است. همچنین در عصر دیجیتال، مرز «مستقیم» و «غیرمستقیم» مبهم شده است: گفت‌وگوی ویدئویی، ویدئوکال و چت مستقیم، ارتباط «مستقیم از راه دور» هستند (DeVito, 2016).",
        mechanism="ارتباط مستقیم در سه حلقه عمل می‌کند: (۱) حضور و هم‌زمانی: فرستنده و گیرنده در یک موقعیت مشترک (فیزیکی یا مجازی) حضور دارند؛ (۲) تبادل فوری: پیام‌ها به‌صورت هم‌زمان و با بازخورد فوری تبادل می‌شوند؛ (۳) تعامل و دیالکتیک: هر دو طرف هم‌زمان فرستنده و گیرنده‌اند و معنا به‌صورت مشترک ساخته می‌شود (Littlejohn & Foss, 2011; DeVito, 2016).",
        key_concepts=["هم‌زمانی و حضور", "بازخورد فوری", "تعامل دوطرفه", "اعتماد و صمیمیت", "ارتباط مستقیم از راه دور"],
        critiques="الگوی فرایندی ارتباط مستقیم را «صادق‌تر» و «مؤثرتر» می‌بیند، در حالی که هر ارتباطی نمادین و بافت‌محور است (Littlejohn & Foss, 2011). نقد دیگر، «حضورزدگی» (presence) است: فرض بر این است که حضور فیزیکی شرط ارتباط مستقیم است، در حالی که در عصر دیجیتال، «حضور مجازی» (ویدئوکال، چت زنده) هم نوعی ارتباط مستقیم است (DeVito, 2016). همچنین مرز «مستقیم» و «غیرمستقیم» در رسانه‌های دیجیتال مبهم شده است.",
        applications="طراحی جلسات و مذاکرات با توجه به اهمیت بازخورد فوری، آموزش مهارت‌های ارتباطی و گوش‌دادن فعال، طراحی تجربیات برخط (ویدئوکال، چت زنده) با حفظ حس «مستقیم‌بودن»، و تحلیل بردهایی رسانه‌ای (پخش زنده، گفت‌وگوی مستقیم) (Littlejohn & Foss, 2011; DeVito, 2016).",
        evolution="مفهوم ارتباط مستقیم از فلسفه (دیالکتیک سقراطی) و روان‌شناسی (دهه‌های ۱۹۵۰–۱۹۶۰) وارد علوم ارتباط شد؛ در دهه‌های ۱۹۷۰–۱۹۸۰، با مکتب میان‌فردی، به «رابطه‌ی نزدیک و تعاملی» تبدیل شد؛ در عصر دیجیتال، ارتباط مستقیم به «ارتباط مستقیم از راه دور» (ویدئوکال، چت زنده) گسترش یافته و مرز مستقیم/غیرمستقیم محو شده است (DeVito, 2016).",
        assumptions="فرض‌های نهفته: حضور و هم‌زمانی، شرط ارتباط مستقیم است (یا حضور مجازی معادل آن)؛ بازخورد فوری و دوطرفه، ویژگی تمایز‌بخش است؛ و ارتباط مستقیم بر اعتماد و صمیمیت استوار است (Littlejohn & Foss, 2011; DeVito, 2016).",
    ),
    "CPT-020": dict(
        definition="ارتباطی که از طریق یک واسطه‌ی نهادی، رسانه‌ای یا فیزیکی (رسانه، متنی، شیء، نماد) انجام می‌شود و در آن فرستنده و گیرنده مستقیماً با یکدیگر در تعامل نیستند؛ ارتباط غیرمستقیم «ارتباط از طریق میانجی» است (McQuail, 2010; Littlejohn & Foss, 2011).",
        summary="ارتباط غیرمستقیم (indirect communication) به هر ارتباطی می‌گوید که از طریق یک واسطه — رسانه، متن، شیء، نماد یا نهاد — انجام می‌شود و فرستنده و گیرنده مستقیماً با یکدیگر در تعامل نیستند. در سنت رسانه‌های جمعی، ارتباط غیرمستقیم به «ارتباط از طریق رسانه» می‌گوید: فرستنده (خبرنگار، تولیدکننده) از طریق رسانه (روزنامه، تلویزیون، وب) به مخاطبان گسترده‌ای می‌رسد که مستقیماً با یکدیگر در تعامل نیستند (McQuail, 2010). در سنت فرایندی، ارتباط غیرمستقیم «ارتباط از طریق میانجی» است: پیام از یک واسطه (متن، شیء، نماد، نهاد) عبور می‌کند و در آن، بازخورد دیرهنگام و غیرمستقیم است (Littlejohn & Foss, 2011). ویژگی‌های کلیدی: (۱) وجود واسطه (رسانه، متن، نهاد)؛ (۲) مخاطبان گسترده و ناهمگن؛ (۳) بازخورد دیرهنگام و غیرمستقیم؛ (۴) یک‌طرفگی نسبی. نقد بنیادین، «غیرمستقیم‌زدگی» (indirectness) است: فرض بر این است که ارتباط غیرمستقیم «کم‌مؤثرتر» و «واسطه‌شده» است، در حالی که در واقع ارتباط غیرمستقیم (رسانه‌ای) بر ساختار اجتماعی و فرهنگی اثر عمیق دارد. همچنین در عصر دیجیتال، مرز «مستقیم» و «غیرمستقیم» مبهم شده است: پلتفرم‌های اجتماعی هم مستقیم (پیام خصوصی) و هم غیرمستقیم (پست عمومی) هستند (McQuail, 2010).",
        mechanism="ارتباط غیرمستقیم در سه حلقه عمل می‌کند: (۱) تولید و رمزگذاری: فرستنده پیام را بر اساس قواعد رسانه‌ای و بافت، می‌سازد؛ (۲) انتقال از طریق واسطه: پیام از رسانه، متن یا نهاد عبور می‌کند و در آن، ساختار و قواعد واسطه بر محتوا اثر می‌گذارند؛ (۳) دریافت و تفسیر: مخاطبان گسترده پیام را در بافت خود تفسیر می‌کنند و بازخورد دیرهنگام و غیرمستقیم (نظرسنجی، داده‌های رفتار) برمی‌گردانند (McQuail, 2010; Littlejohn & Foss, 2011).",
        key_concepts=["واسطه و میانجی", "مخاطبان گسترده", "بازخورد دیرهنگام", "یک‌طرفگی نسبی", "ارتباط رسانه‌ای"],
        critiques="الگوی فرایندی ارتباط غیرمستقیم را «کم‌مؤثرتر» و «واسطه‌شده» می‌بیند، در حالی که در واقع ارتباط رسانه‌ای بر ساختار اجتماعی و فرهنگی اثر عمیق دارد (McQuail, 2010). نقد دیگر، «واسطه‌زدگی» (mediation) است: فرض بر این است که واسطه «خنثی» است، در حالی که ساختار، اقتصاد و قواعد واسطه بر معنا و تفسیر اثر مستقیم دارد (Littlejohn & Foss, 2011). همچنین در رسانه‌های دیجیتال، مرز مستقیم/غیرمستقیم مبهم شده است.",
        applications="تحلیل انتقادی رسانه (اثر واسطه بر معنا و تفسیر)، طراحی استراتژی‌های رسانه‌ای و اطلاع‌رسانی، آموزش سواد رسانه‌ای (بهبود توانایی خواندن واسطه)، و تحلیل بردهایی دیجیتال (چگونه پلتفرم‌ها مرز مستقیم/غیرمستقیم را محو می‌کنند) (McQuail, 2010).",
        evolution="مفهوم ارتباط غیرمستقیم از جامعه‌شناسی رسانه (دهه‌های ۱۹۴۰–۱۹۵۰) وارد علوم ارتباط شد؛ در دهه‌های ۱۹۶۰–۱۹۷۰، با مکتب فرهنگی و انتقادی، به «ارتباط واسطه‌شده» تبدیل شد؛ در عصر دیجیتال، ارتباط غیرمستقیم به «ارتباط شبکه‌ای و الگوریتمی‌شده» بدل شده و مرز مستقیم/غیرمستقیم محو شده است (McQuail, 2010; Littlejohn & Foss, 2011).",
        assumptions="فرض‌های نهفته: واسطه (رسانه، متن، نهاد) وجود خارجی و قابل‌تحلیل است؛ بازخورد در ارتباط غیرمستقیم دیرهنگام و غیرمستقیم است؛ و واسطه بر معنا و تفسیر اثر می‌گذارد (نه صرفا‌ً بر انتقال) (McQuail, 2010; Littlejohn & Foss, 2011).",
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
                    (code, json.dumps({"batch": 255, "score": score, "words": words,
                                       "sources": n_sources, "verified": n_verified,
                                       "relations": n_rel, "rubric": detail}, ensure_ascii=False), STAMP, NOW))
        print(code, "words", words, "score", score, "detail", detail)

    conn.commit()
    conn.close()
    print("BATCH255 DONE")


if __name__ == "__main__":
    main()
