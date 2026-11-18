# -*- coding: utf-8 -*-
"""Batch 254: CPT-011..015 (Noise, Communication Context, Communicative Context, Meaning, Sign).
Sources already in kb_sources (deduped)."""
import json
import importlib.util
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch254-20261117"
NOW = "2026-11-17 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch254.json"

S = {
    "CPT-011": [
        dict(kind="book", title_fa="نظریه ریاضی ارتباطات", title_en="The Mathematical Theory of Communication",
             year=1949, publisher="University of Illinois Press", doi=None, isbn=None, url=None, language="en",
             authors="Shannon, Claude E.; Weaver, Warren",
             citation="Shannon, C. E., & Weaver, W. (1949). The mathematical theory of communication. University of Illinois Press.",
             locator_type="page_range", locator="pp. 29–40", verified=True,
             supports="نویز به‌مثابه تشویش تصادفی سیگنال در کانال و عامل افزایش احتمال خطا."),
        dict(kind="book", title_fa="نظریه ارتباطات انبوه مک‌کویل", title_en="McQuail's Mass Communication Theory",
             year=2010, publisher="Sage", doi=None, isbn="9781849202923", url=None, language="en",
             authors="McQuail, Denis",
             citation="McQuail, D. (2010). McQuail's mass communication theory (6th ed.). Sage.",
             locator_type="CHAPTER", locator="ch. 2", verified=True,
             supports="نویزهای اجتماعی و فرهنگی (سوگیری، کلیشه، زمینه) به‌عنوان موانع تفسیری در ارتباط جمعی."),
    ],
    "CPT-012": [
        dict(kind="book", title_fa="نظریه‌های ارتباط انسانی", title_en="Theories of Human Communication",
             year=2011, publisher="Waveland Press", doi=None, isbn="9781577667063", url=None, language="en",
             authors="Littlejohn, Stephen W.; Foss, Karen A.",
             citation="Littlejohn, S. W., & Foss, K. A. (2011). Theories of human communication (10th ed.). Waveland Press.",
             locator_type="CHAPTER", locator="ch. 1", verified=True,
             supports="زمینه به‌مثابه ساختار اجتماعی-فرهنگی و تاریخی که بر معنا و تفسیر ارتباط اثر می‌گذارد."),
        dict(kind="book", title_fa="نظریه ارتباطات انبوه مک‌کویل", title_en="McQuail's Mass Communication Theory",
             year=2010, publisher="Sage", doi=None, isbn="9781849202923", url=None, language="en",
             authors="McQuail, Denis",
             citation="McQuail, D. (2010). McQuail's mass communication theory (6th ed.). Sage.",
             locator_type="CHAPTER", locator="ch. 1", verified=True,
             supports="زمینه‌ی اجتماعی-اقتصادی رسانه‌های جمعی و اثر آن بر تولید و مصرف پیام."),
    ],
    "CPT-013": [
        dict(kind="book", title_fa="مقدمه‌ای بر مطالعات ارتباط", title_en="Introduction to Communication Studies",
             year=2011, publisher="Routledge", doi="10.4324/9780203837382", isbn="9780415596497", url=None, language="en",
             authors="Fiske, John",
             citation="Fiske, J. (2011). Introduction to communication studies (3rd ed.). Routledge.",
             locator_type="CHAPTER", locator="ch. 2", verified=True,
             supports="بافت به‌مثابه شبکه‌ی هم‌زمانِ نشانه‌ها و بافت‌های فرهنگی که معنای هر پیام را می‌سازد."),
        dict(kind="book", title_fa="نظریه‌های ارتباط انسانی", title_en="Theories of Human Communication",
             year=2011, publisher="Waveland Press", doi=None, isbn="9781577667063", url=None, language="en",
             authors="Littlejohn, Stephen W.; Foss, Karen A.",
             citation="Littlejohn, S. W., & Foss, K. A. (2011). Theories of human communication (10th ed.). Waveland Press.",
             locator_type="CHAPTER", locator="ch. 2", verified=True,
             supports="بافت ارتباطی در سنت‌های ساختاری و نشانه‌شناختی."),
    ],
    "CPT-014": [
        dict(kind="book", title_fa="مقدمه‌ای بر مطالعات ارتباط", title_en="Introduction to Communication Studies",
             year=2011, publisher="Routledge", doi="10.4324/9780203837382", isbn="9780415596497", url=None, language="en",
             authors="Fiske, John",
             citation="Fiske, J. (2011). Introduction to communication studies (3rd ed.). Routledge.",
             locator_type="CHAPTER", locator="ch. 2", verified=True,
             supports="معنا به‌مثابه محصول تفسیر نشانه‌ها در بافت؛ معنا در ذهن گیرنده ساخته می‌شود."),
        dict(kind="book", title_fa="نظریه‌های ارتباط انسانی", title_en="Theories of Human Communication",
             year=2011, publisher="Waveland Press", doi=None, isbn="9781577667063", url=None, language="en",
             authors="Littlejohn, Stephen W.; Foss, Karen A.",
             citation="Littlejohn, S. W., & Foss, K. A. (2011). Theories of human communication (10th ed.). Waveland Press.",
             locator_type="CHAPTER", locator="ch. 1", verified=True,
             supports="تعریف‌های مختلف معنا در سنت‌های فرایندی، نشانه‌شناختی و گفتمانی."),
    ],
    "CPT-015": [
        dict(kind="book", title_fa="مقدمه‌ای بر مطالعات ارتباط", title_en="Introduction to Communication Studies",
             year=2011, publisher="Routledge", doi="10.4324/9780203837382", isbn="9780415596497", url=None, language="en",
             authors="Fiske, John",
             citation="Fiske, J. (2011). Introduction to communication studies (3rd ed.). Routledge.",
             locator_type="CHAPTER", locator="ch. 2", verified=True,
             supports="نشانه به‌مثابه واحد بنیادین معنا: پیوند نشانه‌دهنده و معنای آن در بافت فرهنگی."),
        dict(kind="book", title_fa="نظریه‌های ارتباط انسانی", title_en="Theories of Human Communication",
             year=2011, publisher="Waveland Press", doi=None, isbn="9781577667063", url=None, language="en",
             authors="Littlejohn, Stephen W.; Foss, Karen A.",
             citation="Littlejohn, S. W., & Foss, K. A. (2011). Theories of human communication (10th ed.). Waveland Press.",
             locator_type="CHAPTER", locator="ch. 2", verified=True,
             supports="نشانه‌شناسی در نظریه‌های ارتباط: علائم، نمادها و نظام‌های نمادین."),
    ],
}

ENRICH = {
    "CPT-011": dict(
        definition="هر عاملی — فیزیکی، روانی یا اجتماعی — که سیگنال ارتباطی را تشویش، برهم می‌زند یا تفسیر آن را مختل می‌کند و احتمال خطا و انحراف معنایی را افزایش می‌دهد (Shannon & Weaver, 1949). نویز در کانال فنی تشویش سیگنال است و در ارتباط انسانی، موانع تفسیری و شناختی است (McQuail, 2010).",
        summary="نویز از مفاهیم کلیدی الگوی فرایندی است. در نظریه‌ی ریاضی ارتباطات (شانون، ۱۹۴۸/۱۹۴۹)، نویز «هر سیگنال تصادفی یا ناخواسته‌ای است که در کانال روی سیگنال اصلی اثر می‌گذارد و صحت انتقال را کاهش می‌دهد»؛ مسئله‌ی بنیادین ارتباط، بازتولید پیام با حداکثر صحت در حضور نویز است (Shannon & Weaver, 1949). نویز فنی (تشویش الکترونیکی، نویز هوا) قابل اندازه‌گیری و کنترل است و مهندسی کانال (فشرده‌سازی، تکرار، خطایاب) برای کاهش آن توسعه یافته است. اما در سنت اجتماعی و فرهنگی، «نویز» مفهوم گسترده‌تری است: کلیشه‌ها، سوگیری‌های شناختی، تفاوت زبان و فرهنگ، حواس‌پرتی محیطی و حتی ساختار قدرت، همگی «نویزهای تفسیری» هستند که بر معنای درک‌شده اثر می‌گذارند (McQuail, 2010). نقد بنیادین، تقلیل نویز به «خطای فنی» است: در ارتباط انسانی، نویز اغلب ساختاری و فرهنگی است و نه صرفا‌ً تصادفی. همچنین در رسانه‌های دیجیتال، حجم اطلاعات و سرعت پخش خود نوعی «نویز» شده و «پدافند شناختی» مخاطب را تضعیف می‌کند.",
        mechanism="نویز در سه لایه عمل می‌کند: (۱) لایه‌ی فنی: تشویش سیگنال در کانال (نویز هوا، افت ولتاژ، پهنای باند محدود) که احتمال خطا را بالا می‌برد؛ (۲) لایه‌ی نمادین: ابهام، دوپهلوئی و ناهماهنگی در کد و نشانه‌ها که رمزگشایی را دشوار می‌کند؛ (۳) لایه‌ی شناختی-اجتماعی: حواس‌پرتی، خستگی، سوگیری، تفاوت فرهنگی و ساختار قدرت که تفسیر گیرنده را منحرف می‌کنند (Shannon & Weaver, 1949; McQuail, 2010).",
        key_concepts=["تشویش سیگنال", "احتمال خطا", "نویز فنی و فرهنگی", "پدافند شناختی", "محدودیت کانال"],
        critiques="الگوی فنی نویز را «تصادفی و بی‌جهت» می‌بیند، در حالی که در ارتباط انسانی نویز اغلب ساختاری، فرهنگی و جهت‌دار است (Shannon & Weaver, 1949). نقد دیگر، خلط «نویز» و «گوناگونی» است: تنوع نشانه‌ها و بافت‌ها لزوماً نویز نیست و گاه غنای معنا را می‌سازد (McQuail, 2010). همچنین در محیط دیجیتال، مرز «اطلاعات» و «نویز» مبهم است و «فیلتر» و «الگوریتم» خود نویز تازه‌ای می‌سازند.",
        applications="طراحی پیام‌های واضح و کم‌ابهام برای کاهش نویز نمادین، بهینه‌سازی کانال‌های ارتباطی (مهندسی سیگنال، انتخاب رسانه مناسب)، طراحی آموزشی با کاهش حواس‌پرتی، و تحلیل شکست‌های ارتباطی در بحران (کجا و چگونه نویز غلبه کرد) (Shannon & Weaver, 1949; McQuail, 2010).",
        evolution="از «نویز» به‌مثابه تشویش فنی سیگنال در مهندسی مخابرات (شانون، ۱۹۴۸)، به «موانع ارتباطی» در علوم ارتباط (دهه‌های ۱۹۵۰–۱۹۶۰) و سپس به «نویزهای شناختی، فرهنگی و الگوریتمی» در مطالعات رسانه و شناخت تکامل یافت؛ امروزه نویز به «حجم و سرعت اطلاعات» در عصر دیجیتال گره خورده است (McQuail, 2010).",
        assumptions="فرض‌های نهفته: نویز از سیگنال قابل تمایز است؛ نویز تصادفی و قابل‌اندازه‌گیری است (در لایه فنی)؛ و کاهش نویز، صحت انتقال را افزایش می‌دهد (Shannon & Weaver, 1949)؛ در لایه اجتماعی، فرض بر این است که نویز فرهنگی و شناختی قابل شناسایی و کاهش است (McQuail, 2010).",
    ),
    "CPT-012": dict(
        definition="مجموعه‌ی شرایط، ساختارها و عوامل اجتماعی، فرهنگی، تاریخی و فیزیکی که در دورۀ وقوع یک تعامل ارتباطی حضور دارند و بر تولید، انتقال و تفسیر پیام اثر می‌گذارند؛ زمینه به معنا و تفسیر «چارچوب» می‌دهد (Littlejohn & Foss, 2011).",
        summary="زمینه (context) مفهومی است که ارتباط را از یک زنجیره‌ی فری‌از-بافت به پدیده‌ای در بافت تبدیل می‌کند. در سنت فرایندی، زمینه «شرایط محیطی و موقعیتی» است که بر موفقیت انتقال اثر می‌گذارد؛ اما در سنت‌های ساختاری و گفتمانی، زمینه «ساختار اجتماعی-فرهنگی و تاریخی» است که خود معنا را می‌سازد — نه فقط آن را منتقل می‌کند (Littlejohn & Foss, 2011). زمینه چندلایه است: موقعیتی (مکان، زمان، فاصله فیزیکی)، رابطه‌ای (نقش، قدرت، سابقه‌ی تعامل)، فرهنگی (ارزش‌ها، باورها، کدها) و تاریخی (رویدادها، ساختارهای نهادی). در رسانه‌های جمعی، زمینه اقتصادی، سیاسی و مالکیتی رسانه بر تولید و قاب‌بندی محتوا اثر مستقیم دارد (McQuail, 2010). نقد بنیادین بر الگوهای فرایندی، حذف زمینه است: الگوهای خطی ارتباط را در خلأ نشان می‌دهند و اثر ساختار و قدرت را نادیده می‌گیرند. همچنین مرز «زمینه» و «محتوا» در رسانه‌های دیجیتال مبهم شده است: بافت مصرف (پلتفرم، الگوریتم، گفت‌وگوی اطراف) خود بخشی از معنای پیام است (Littlejohn & Foss, 2011).",
        mechanism="زمینه بر ارتباط در سه حلقه اثر می‌گذارد: (۱) پیش از انتقال: زمینه بر انتخاب پیام و رمزگذاری اثر می‌گذارد (فرستنده بر اساس موقعیت و بافت، پیام را انتخاب می‌کند)؛ (۲) در حین انتقال: زمینه بر انتخاب کانال، لحن و قالب اثر می‌گذارد؛ (۳) پس از دریافت: زمینه بر رمزگشایی و تفسیر اثر می‌گذارد (گیرنده پیام را در بافت موقعیت، رابطه و فرهنگ تفسیر می‌کند) (Littlejohn & Foss, 2011; McQuail, 2010).",
        key_concepts=["موقعیت", "رابطه و نقش", "ساختار اجتماعی-فرهنگی", "زمینه تاریخی", "زمینه اقتصادی رسانه"],
        critiques="مفهوم «زمینه» مرز روشنی با «بافت»، «حالت» و «شرایط» ندارد و در ادبیات اغلب خلط می‌شود (Littlejohn & Foss, 2011). نقد دیگر، «ساختاری‌زدگی» بیش از حد است: وقتی زمینه را «ساختار» می‌نامیم، خطر تقلیل ارتباط به تعیین‌گرگی و کم‌بینان‌بودن عاملیت فردی وجود دارد. همچنین در رسانه‌های دیجیتال، زمینه از «موقعیت ثابت» به «بافت سیال و شخصی‌سازی‌شده» تبدیل شده و مفهوم زمینه باید بازتعریف شود (McQuail, 2010).",
        applications="طراحی پیام‌های رسانه‌ای با توجه به بافت مخاطب (مناسب‌سازی لحن، قالب و زمان)، تحلیل انتقادی رسانه (اثر زمینه اقتصادی-سیاسی بر قاب‌بندی)، آموزش ارتباط مؤثر در موقعیت‌های مختلف (سازمانی، بحران، بین‌فرهنگی)، و طراحی تجربه کاربری در پلتفرم‌های دیجیتال (Littlejohn & Foss, 2011).",
        evolution="از «زمینه» به‌مثابه شرایط محیطی در الگوهای فرایندی اولیه، به «ساختار اجتماعی-فرهنگی» در نظریه‌های انتقادی و گفتمانی (دهه‌های ۱۹۶۰–۱۹۷۰) و سپس به «بافت سیال و شخصی‌سازی‌شده» در عصر دیجیتال تکامل یافت؛ امروزه زمینه از «موقعیت» به «سیستم پویا» ارتقا یافته است (Littlejohn & Foss, 2011).",
        assumptions="فرض‌های نهفته: زمینه وجود خارجی و قابل‌تحلیل است؛ زمینه بر معنا و تفسیر اثر می‌گذارد (نه صرفا‌ً بر انتقال)؛ و زمینه قابل‌تغییر و قابل‌تأثیرگذاری است (Littlejohn & Foss, 2011; McQuail, 2010).",
    ),
    "CPT-013": dict(
        definition="شبکه‌ی هم‌زمانِ نشانه‌ها، بافت‌ها و روابط فرهنگی که معنای هر پیام را در آن ساخته و حفظ می‌شود؛ بافت «سیستمی از هم‌بستگی‌ها» است که در آن هیچ نشانه‌ای به‌تنهایی معنا ندارد (Fiske, 2011). در سنت نشانه‌شناختی، بافت «نظام تفاوت‌ها» است که نشانه‌ها را از یکدیگر متمایز و معنا می‌بخشد (Littlejohn & Foss, 2011).",
        summary="بافت (context) در سنت نشانه‌شناختی و ساختاری، مفهوم بنیادی‌تری از «زمینه» است: بافت نه «شرایط» بلکه «سیستم نشانه‌ها و بافت‌ها» است که در آن هر پیام به معنای خود می‌رسد. فیسک (۲۰۱۱) توضیح می‌دهد که معنا از «تفاوت» و «هم‌بستگی» نشانه‌ها با یکدیگر در یک بافت فرهنگی ساخته می‌شود؛ هیچ نشانه‌ای معنای ذاتی ندارد، بلکه معنایش از جایگاهش در شبکه‌ی نشانه‌ها (بافت) می‌آید. در رسانه، بافت یعنی: «مجموعه‌ی بافت‌های اطراف پیام» — خبرهای دیگر، گفت‌وگوهای اجتماعی، بافت‌های بصری و صوتی، الگوریتم‌های پلتفرم — که همگی بر تفسیر پیام اثر می‌گذارند (Fiske, 2011). نقد بنیادین، «بافت‌زدگی» (contextualization) بیش از حد است: اگر هر معنای از بافت می‌آید، خطر نسبی‌سازی مطلق و ناتوانی از گفتن «معنای واقعی» وجود دارد. همچنین مرز «بافت» و «محتوا» در رسانه‌های دیجیتال محو شده است: بافت مصرف (پلتفرم، کامنت‌ها، الگوریتم) خود بخشی از معنای پیام است (Littlejohn & Foss, 2011).",
        mechanism="بافت به دو مکانیزم معنا می‌سازد: (۱) تفاوت: نشانه با متمایزبودن از نشانه‌های دیگر معنا پیدا می‌کند (مثل حروف الفبا که معنایشان از جایگاهشان در کلمه می‌آید)؛ (۲) هم‌بستگی: نشانه در شبکه‌ی بافت‌های هم‌زمان، معنای خود را حفظ و گسترش می‌دهد (Fiske, 2011). در رسانه، بافت اطراف پیام (خبرهای هم‌زمان، گفت‌وگوی اجتماعی، بافت بصری) بر تفسیر آن اثر می‌گذارد و «معنای نهایی» در تقاطع پیام و بافت ساخته می‌شود (Littlejohn & Foss, 2011).",
        key_concepts=["سیستم نشانه", "تفاوت و هم‌بستگی", "بافت فرهنگی", "بافت رسانه‌ای", "بافت الگوریتمی"],
        critiques="مفهوم «بافت» مرز روشنی با «زمینه»، «سیستم» و «فرهنگ» ندارد و در ادبیات اغلب خلط می‌شود (Littlejohn & Foss, 2011). نقد دیگر، «نسبیت‌گرایی مطلق» است: اگر هر معنا از بافت می‌آید، گفتن از «معنای واقعی» یا «درستی» تفسیر دشوار می‌شود. همچنین در رسانه‌های دیجیتال، بافت به‌شدت الگوریتمی و شخصی‌سازی‌شده است و «بافت مشترک» که شرط درک مشترک است، از بین می‌رود (Fiske, 2011).",
        applications="تحلیل انتقادی رسانه (چگونه بافت اطراف پیام، تفسیر آن را شکل می‌دهد)، طراحی پیام با توجه به بافت مخاطب (بافت فرهنگی، رسانه‌ای و الگوریتمی)، آموزش سواد رسانه‌ای (بهبود توانایی خواندن بافت)، و تحلیل گفتمانی (چگونه بافت‌های گفتمانی معنای سیاست و رسانه را می‌سازند) (Fiske, 2011).",
        evolution="مفهوم بافت از نشانه‌شناسی (سوسور، ۱۹۱۶) و ساختاری‌سازی (دهه‌های ۱۹۵۰–۱۹۶۰) وارد مطالعات رسانه شد و با فیسک (۱۹۸۷، ویرایش ۲۰۱۱) به «بافت رسانه‌ای و فرهنگی» گسترش یافت؛ در عصر دیجیتال، بافت به «بافت الگوریتمی و شخصی‌سازی‌شده» تبدیل شده است (Fiske, 2011; Littlejohn & Foss, 2011).",
        assumptions="فرض‌های نهفته: معنا از بافت می‌آید (نه ذات نشانه)؛ بافت‌ها ساختار و نظام دارند؛ و بافت مشترک میان فرستنده و گیرنده، شرط درک مشترک است (Fiske, 2011; Littlejohn & Foss, 2011).",
    ),
    "CPT-014": dict(
        definition="محصولی است که گیرنده از تفسیر نشانه‌ها در یک بافت فرهنگی و اجتماعی می‌سازد؛ معنا نه در پیام، بلکه در ذهن گیرنده و در تقاطع نشانه، کد و بافت تولید می‌شود (Fiske, 2011). معنا «آنچه در ذهن مخاطب ساخته می‌شود» است نه آنچه فرستنده «در ذهن دارد» (Littlejohn & Foss, 2011).",
        summary="معنا (meaning) از بنیادی‌ترین و در عین حال پُرچالش‌ترین مفاهیم علم ارتباط است. در سنت فرایندی، معنا «محتوای پیام» است که از فرستنده به گیرنده منتقل می‌شود؛ اما در سنت نشانه‌شناختی و گفتمانی، معنا محصول تفسیر است: گیرنده با کد و بافت خود، نشانه‌ها را تفسیر می‌کند و معنای نهایی را می‌سازد — گاه متفاوت از قصد فرستنده (Fiske, 2011). فیسک (۲۰۱۱) توضیح می‌دهد که معنا از «تفاوت» و «هم‌بستگی» نشانه‌ها در بافت فرهنگی ساخته می‌شود و هیچ نشانه‌ای معنای ثابت و ذاتی ندارد. در مطالعات رسانه، «معنا» به «معنای تولیدشده توسط مخاطب» می‌گوید: تفسیر غالب، مذاکره‌شده و مقاومتی (Fiske, 2011). نقد بنیادین، «معنازدایی» (de-reification) است: معنا را نمی‌توان به‌مثابه «چیز» درون پیام دید؛ معنا فرایند است نه کالاست. همچنین مرز «معنای قصدی فرستنده» و «معنای تفسیرشده توسط گیرنده» در رسانه‌های دیجیتال به‌شدت گسترده شده است: معنای یک پیام، به بافت مصرف، گفت‌وگوی اطراف و الگوریتم پلتفرم گره خورده است (Littlejohn & Foss, 2011).",
        mechanism="تولید معنا در سه حلقه اتفاق می‌افتد: (۱) رمزگذاری: فرستنده نشانه‌ها را بر اساس کد و بافت انتخاب و ترکیب می‌کند و «معنای قصدی» را می‌سازد؛ (۲) انتقال: سیگنال‌ها از کانال عبور می‌کنند و در معرض نویز قرار می‌گیرند؛ (۳) رمزگشایی: گیرنده نشانه‌ها را در بافت خود تفسیر می‌کند و «معنای تفسیرشده» را می‌سازد (Fiske, 2011). معنای نهایی، تقاطع کد، بافت و تجربه‌ی گیرنده است — نه صرفا‌ً قصد فرستنده (Littlejohn & Foss, 2011).",
        key_concepts=["معنای قصدی و تفسیرشده", "تفاوت و هم‌بستگی", "کد و بافت", "تولید معنا", "معنای جمعی"],
        critiques="الگوی فرایندی معنا را «کالایی» می‌بیند که از فرستنده به گیرنده منتقل می‌شود، در حالی که معنا فرایند تفسیری است (Fiske, 2011). نقد دیگر، «معنازدایی مطلق» است: اگر معنا همیشه از بافت می‌آید و ثابت نیست، گفتن از «درستی» تفسیر و «معنای واقعی» دشوار می‌شود (Littlejohn & Foss, 2011). همچنین در رسانه‌های دیجیتال، معنای یک پیام به‌شدت سیال و شخصی‌سازی‌شده است و «معنای واحد» فرضی است.",
        applications="تحلیل انتقادی رسانه (چگونه معنای رسانه‌ای ساخته و تفسیر می‌شود)، نگارش و طراحی پیام با توجه به بافت مخاطب، آموزش سواد رسانه‌ای (بهبود توانایی تفسیر و تولید معنا)، و تحلیل گفتمانی (چگونه معنای سیاست، فرهنگ و رسانه در بافت گفتمانی می‌سازد) (Fiske, 2011).",
        evolution="مفهوم معنا از فلسفه و منطق (معنا به‌مثابه «مرجع» و «مضمون») وارد نشانه‌شناسی و علوم ارتباط شد؛ در دهه‌های ۱۹۶۰–۱۹۷۰، با مکتب فرهنگی و گفتمانی، معنا از «مرجع ثابت» به «محصول تفسیر و بافت» بدل شد؛ در عصر دیجیتال، معنا به «فرایند سیال و الگوریتمی‌شده» تبدیل شده است (Fiske, 2011; Littlejohn & Foss, 2011).",
        assumptions="فرض‌های نهفته: معنا از تفسیر نشانه در بافت می‌آید (نه ذات نشانه)؛ کد و بافت مشترک میان فرستنده و گیرنده، شرط درک مشترک است؛ و گیرنده کنشگر فعال تولید معناست (Fiske, 2011; Littlejohn & Foss, 2011).",
    ),
    "CPT-015": dict(
        definition="هر چیزی — کلمه، تصویر، صدا، حرکت، شیء — که در یک بافت فرهنگی، حامل معناست و با نشانه‌های دیگر در شبکه‌ای از هم‌بستگی و تفاوت معنا می‌یابد؛ نشانه «واحد بنیادین معنا» است (Fiske, 2011). در سنت ریاضی، نشانه (signal) به سیگنال قابل انتقال می‌گوید (Shannon & Weaver, 1949).",
        summary="نشانه (sign) از بنیادی‌ترین مفاهیم نشانه‌شناسی و مطالعات رسانه است. در سنت سوسوری، نشانه «پیوند نشانه‌دهنده» (signifier، شکل صوتی یا تصویری) و «نشانه‌دهی‌شده» (signified، مفهوم) است که هیچ‌کدام معنای ذاتی ندارند و معنا از تفاوت و هم‌بستگی نشانه‌ها در نظام (بافت فرهنگی) می‌آید (Fiske, 2011). در سنت ریاضی ارتباطات، «نشانه» (signal) به سیگنال قابل انتقال و اندازه‌گیری می‌گوید — مفهوم فنی‌تر و کمّی‌تر (Shannon & Weaver, 1949). در رسانه، نشانه به «هر عنصر بصری، صوتی، کلامی و رفتاری در پیام رسانه‌ای» می‌گوید که با سایر عناصر در بافت، معنای کل را می‌سازد (Fiske, 2011). نقد بنیادین، «دوگانگی نشانه/سیگنال» است: در سنت فنی، نشانه قابل اندازه‌گیری و انتقال است؛ در سنت نشانه‌شناختی، نشانه حامل معناست و معنایش از بافت می‌آید — این دو تعریف هم‌پوشانی دارند اما مبنای متفاوتی دارند. همچنین در رسانه‌های دیجیتال، «نشانه‌سازی» (semiotization) خود فرایندی است: الگوریتم‌ها و پلتفرم‌ها نشانه‌ها را تولید، ترکیب و معنا می‌کنند و مرز «تولید نشانه توسط انسان» و «تولید نشانه توسط الگوریتم» مبهم شده است (Littlejohn & Foss, 2011).",
        mechanism="نشانه در سه سطح عمل می‌کند: (۱) نشانه‌دهنده: شکل فیزیکی نشانه (صدا، تصویر، حرکت، کلمه) که در کانال منتقل می‌شود؛ (۲) نشانه‌دهی‌شده: مفهوم یا معنا که در ذهن گیرنده از تفسیر نشانه‌دهنده ساخته می‌شود؛ (۳) بافت: نظام نشانه‌ها و هم‌بستگی‌ها که معنای هر نشانه را از تفاوت با سایر نشانه‌ها می‌سازد (Fiske, 2011). در رسانه، ترکیب و چینش نشانه‌ها (کلام، تصویر، صدا، حرکت) بر اساس قواعد کد، معنای کل پیام را می‌سازد (Littlejohn & Foss, 2011).",
        key_concepts=["نشانه‌دهنده و نشانه‌دهی‌شده", "تفاوت و هم‌بستگی", "نظام نشانه", "کد", "نشانه‌سازی الگوریتمی"],
        critiques="مفهوم نشانه مرز روشنی با «سیگنال»، «نماد»، «عنوان» و «نشانه» ندارد و در ادبیات اغلب خلط می‌شود (Littlejohn & Foss, 2011). نقد دیگر، «بافت‌زدگی مطلق» است: اگر معنای هر نشانه از بافت می‌آید، خطر نسبی‌سازی مطلق وجود دارد. همچنین در رسانه‌های دیجیتال، مرز «نشانه‌سازی انسانی» و «نشانه‌سازی الگوریتمی» مبهم است و مسئولیت معنا و نشانه مبهم شده است (Fiske, 2011).",
        applications="تحلیل انتقادی رسانه (چگونه نشانه‌ها معنای رسانه‌ای را می‌سازند)، طراحی پیام و بصری (انتخاب و ترکیب نشانه‌ها بر اساس بافت مخاطب)، آموزش سواد رسانه‌ای و نشانه‌شناختی، و تحلیل گفتمانی (چگونه نشانه‌های گفتمانی معنای سیاست و فرهنگ را می‌سازند) (Fiske, 2011).",
        evolution="مفهوم نشانه از نشانه‌شناسی (سوسور، ۱۹۱۶؛ پیرس، ۱۹۰۳) وارد علوم ارتباط و مطالعات رسانه شد؛ در دهه‌های ۱۹۶۰–۱۹۷۰، با مکتب فرهنگی (فیسک، ۱۹۸۷)، نشانه به «واحد تحلیل رسانه» تبدیل شد؛ در عصر دیجیتال، نشانه به «واحد الگوریتمی و داده‌محور» بدل شده و «نشانه‌سازی الگوریتمی» پدیده‌ای تازه است (Fiske, 2011; Littlejohn & Foss, 2011).",
        assumptions="فرض‌های نهفته: نشانه معنای ذاتی ندارد و معنایش از بافت و تفاوت می‌آید؛ نظام نشانه‌ها ساختار و قواعد دارد؛ و تفسیر نشانه، فرایند فعال و فرهنگی است نه صرفا‌ً بازیابی فنی (Fiske, 2011; Littlejohn & Foss, 2011).",
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
                    (code, json.dumps({"batch": 254, "score": score, "words": words,
                                       "sources": n_sources, "verified": n_verified,
                                       "relations": n_rel, "rubric": detail}, ensure_ascii=False), STAMP, NOW))
        print(code, "words", words, "score", score, "detail", detail)

    conn.commit()
    conn.close()
    print("BATCH254 DONE")


if __name__ == "__main__":
    main()
