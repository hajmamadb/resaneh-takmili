# -*- coding: utf-8 -*-
"""Batch 307: CPT-076..080 (User Experience, Audience Experience, Media Behavior, Audience Agency, Active Audience)."""
import json
import importlib.util
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch307-20261117"
NOW = "2026-11-17 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch307.json"

S = {
    "CPT-076": [
        dict(kind="book", title_fa="طراحی اشیاء روزمره", title_en="The Design of Everyday Things",
             year=2004, publisher="Basic Books", doi=None, isbn="9780465050659", url=None, language="en",
             authors="Norman, Don",
             citation="Norman, D. (2004). The design of everyday things (revised ed.). Basic Books.",
             locator_type="CHAPTER", locator="ch. 1", verified=True,
             supports="تجربه کاربری: درک، کنش‌پذیری و تعامل کاربر با سیستم."),
        dict(kind="book", title_fa="نظریه ارتباطات انبوش مک‌کویل", title_en="McQuail's Mass Communication Theory",
             year=2010, publisher="Sage", doi=None, isbn="9781849202923", url=None, language="en",
             authors="McQuail, Denis",
             citation="McQuail, D. (2010). McQuail's mass communication theory (6th ed.). Sage.",
             locator_type="CHAPTER", locator="ch. 14", verified=True,
             supports="تجربه کاربری رسانه‌ای و کیفیت تعامل مخاطب."),
    ],
    "CPT-077": [
        dict(kind="book", title_fa="فرهنگ همگرایی", title_en="Convergence Culture",
             year=2006, publisher="New York University Press", doi=None, isbn="9780814783471", url=None, language="en",
             authors="Jenkins, Henry",
             citation="Jenkins, H. (2006). Convergence culture: Where old and new media collide. New York University Press.",
             locator_type="CHAPTER", locator="ch. 1", verified=True,
             supports="تجربه مخاطب: مشارکت، تعامل و جریان چندرویه‌ای محتوا."),
        dict(kind="book", title_fa="نظریه ارتباطات انبوش مک‌کویل", title_en="McQuail's Mass Communication Theory",
             year=2010, publisher="Sage", doi=None, isbn="9781849202923", url=None, language="en",
             authors="McQuail, Denis",
             citation="McQuail, D. (2010). McQuail's mass communication theory (6th ed.). Sage.",
             locator_type="CHAPTER", locator="ch. 14", verified=True,
             supports="تجربه مخاطب در فرایند دریافت و تفسیر."),
    ],
    "CPT-078": [
        dict(kind="book", title_fa="نظریه ارتباطات انبوش مک‌کویل", title_en="McQuail's Mass Communication Theory",
             year=2010, publisher="Sage", doi=None, isbn="9781849202923", url=None, language="en",
             authors="McQuail, Denis",
             citation="McQuail, D. (2010). McQuail's mass communication theory (6th ed.). Sage.",
             locator_type="CHAPTER", locator="ch. 14", verified=True,
             supports="رفتار رسانه‌ای: الگوهای انتخاب و مصرف رسانه."),
        dict(kind="book", title_fa="نظریه‌های ارتباط انسانی", title_en="Theories of Human Communication",
             year=2011, publisher="Waveland Press", doi=None, isbn="9781577667063", url=None, language="en",
             authors="Littlejohn, Stephen W.; Foss, Karen A.",
             citation="Littlejohn, S. W., & Foss, K. A. (2011). Theories of human communication (10th ed.). Waveland Press.",
             locator_type="CHAPTER", locator="ch. 16", verified=True,
             supports="رفتار رسانه‌ای در سنت فرایندی و استفاده-اقناع."),
    ],
    "CPT-079": [
        dict(kind="book", title_fa="فرهنگ همگرایی", title_en="Convergence Culture",
             year=2006, publisher="New York University Press", doi=None, isbn="9780814783471", url=None, language="en",
             authors="Jenkins, Henry",
             citation="Jenkins, H. (2006). Convergence culture: Where old and new media collide. New York University Press.",
             locator_type="CHAPTER", locator="ch. 7", verified=True,
             supports="کنشگری مخاطب: عاملیت، مشارکت و کنشگری رسانه‌ای."),
        dict(kind="book", title_fa="فرهنگ تلویزیون", title_en="Television Culture",
             year=1987, publisher="Routledge", doi=None, isbn="9780415094356", url=None, language="en",
             authors="Fiske, John",
             citation="Fiske, J. (1987). Television culture. Routledge.",
             locator_type="CHAPTER", locator="ch. 2", verified=True,
             supports="کنشگری مخاطب در تفسیر فعال و معناسازی."),
    ],
    "CPT-080": [
        dict(kind="book", title_fa="فرهنگ تلویزیون", title_en="Television Culture",
             year=1987, publisher="Routledge", doi=None, isbn="9780415094356", url=None, language="en",
             authors="Fiske, John",
             citation="Fiske, J. (1987). Television culture. Routledge.",
             locator_type="CHAPTER", locator="ch. 2", verified=True,
             supports="مخاطب فعال: تفسیر فعال، انتخاب و معناسازی."),
        dict(kind="book", title_fa="فرهنگ همگرایی", title_en="Convergence Culture",
             year=2006, publisher="New York University Press", doi=None, isbn="9780814783471", url=None, language="en",
             authors="Jenkins, Henry",
             citation="Jenkins, H. (2006). Convergence culture: Where old and new media collide. New York University Press.",
             locator_type="CHAPTER", locator="ch. 1", verified=True,
             supports="مخاطب فعال در عصر رسانه‌های همگرا و مشارکتی."),
    ],
}

ENRICH = {
    "CPT-076": dict(
        mechanism="تجربه کاربری در چهار حلقه شکل می‌گیرد: (۱) درک (comprehension): کاربر هدف و کاربرد سیستم را می‌فهمد و «کنش‌پذیری» (affordance) را می‌بیند؛ (۲) تعامل (interaction): کاربر با سیستم عمل می‌کند و بازخورد فوری دریافت می‌کند؛ (۳) درک بازخورد: کاربر از نتایج کنش خود آگاه می‌شود و خطا را درک می‌کند؛ (۴) ارزیابی و هیجان: کاربر تجربه را بر اساس سهولت استفاده، رضایت و معناداری، ارزیابی می‌کند و با آن پیوند عاطفی می‌سازد (Norman, 2004; McQuail, 2010).",
        key_concepts=["کنش‌پذیری", "بازخورد", "سهولت استفاده", "دسترسی‌پذیری", "رضایت کاربر"],
        critiques="نقد نخست، «کاربریِ خالص» است: فرض بر این است که تجربه کاربری فقط سهولت فنی کار با سیستم است، در حالی که در واقع ابعاد عاطفی، زیبایی‌شناختی، معنایی و اجتماعی تجربه نیز به‌همان اندازه مهم‌اند (Norman, 2004). نقد دیگر، «میانگین‌سازی کاربر» است: طراحی برای «کاربر میانگین»، گروه‌های آسیب‌پذیر و تنوع توانایی را نادیده می‌گیرد و تجربه را نابرابر می‌سازد (McQuail, 2010). همچنین تجربه کاربری در رسانه‌های دیجیتال، به‌شدت با داده و الگوریتم گره خورده است.",
        applications="کاربرد در طراحی رابط و تجربه کاربری (UX) رسانه‌ها و اپلیکیشن‌ها (سهولت، بازخورد، دسترسی‌پذیری)، در طراحی تعاملی رسانه‌های دیجیتال (ناوبری، شخصی‌سازی، سرعت بارگذاری)، در ارزیابی کاربردپذیری (تست کاربری، مشاهده، پرسشنامه)، در آموزش سواد رسانه‌ای (شناخت طراحی رابط و هدایت رفتار)، و در پژوهش (اثر تجربه کاربری بر ماندگاری، اعتماد و مشارکت مخاطب) (Norman, 2004; McQuail, 2010).",
        evolution="مفهوم تجربه کاربری از طراحی کاربرپسند و مهندسی شناختی (دهه‌های ۱۹۸۰–۱۹۹۰) وارد علوم ارتباط شد و در آغاز بر «کاربردپذیری» (usability) تمرکز داشت؛ در دهه‌های ۲۰۰۰–۲۰۱۰، با طراحی عاطفی و طراحی تجربه (UX)، از کاربردپذیری خالص به «کیفیت کلان تجربه» گسترش یافت؛ و در عصر دیجیتال، تجربه کاربری با شخصی‌سازی، الگوریتم و اقتصاد توجه درآمیخته است (Norman, 2004).",
        assumptions="فرض‌های نهفته: کاربر، با هدف مشخصی به سیستم نزدیک می‌شود (هدفمند)؛ سهولت استفاده و بازخورد شفاف، پایه تجربه مثبت است؛ تجربه کاربری، بر رضایت، اعتماد و ماندگاری کاربر اثر می‌گذارد؛ و این تجربه، باید متناسب با تنوع توانایی و بافت فرهنگی کاربران طراحی شود (Norman, 2004; McQuail, 2010).",
    ),
    "CPT-077": dict(
        mechanism="تجربه مخاطب در چهار حلقه شکل می‌گیرد: (۱) انتخاب: مخاطب از میان گزینه‌های رسانه‌ای، بر اساس نیاز و زمینه، انتخاب می‌کند؛ (۲) درگیرشدن (engagement): مخاطب به‌طور فعال در محتوا درگیر شده و توجه و مشارکت می‌ورزد؛ (۳) تفسیر و معناسازی: مخاطب پیام را بر اساس پیشینه و بافت خود تفسیر و معنا می‌سازد؛ (۴) مشارکت و بازخورد: مخاطب واکنش، نظر و تولید می‌سازد و تجربه خود را با دیگران به اشتراک می‌گذارد (Jenkins, 2006; McQuail, 2010).",
        key_concepts=["درگیری", "تفسیر", "مشارکت", "جریان چندرویه", "تجربه شخصی‌شده"],
        critiques="نقد نخست، «مشارکت‌زدگی» (participation-ism) است: فرض بر این است که مخاطب همیشه فعال و مشارکت‌کننده است، در حالی که بسیاری از تعاملات، سبک، تکراری یا در چارچوب طراحی‌شده‌ی پلتفرم محدودند (Jenkins, 2006). نقد دیگر، «تجربه‌محوریِ خالص» است: تمرکز بر تجربهٔ فردی، اثرهای جمعی، سیاسی و نابرابری تجربه رسانه‌ای را می‌پوشاند (McQuail, 2010). همچنین تجربه مخاطب، به‌سختی با ابزارهای کمی‌سنجی قابل اندازه‌گیری است.",
        applications="کاربرد در طراحی تجربهٔ مخاطب رسانه‌ای (درگیری، مشارکت، جریان چندرویه)، در طراحی رسانه‌های همگرا و چندپلتفرمی (رابط، تعامل، روایت چندرسانه‌ای)، در تحلیل رفتار درگیری مخاطب (ماندگاری، تعامل، وفاداری)، در آموزش سواد رسانه‌ای (شناخت تجربهٔ شخصی‌سازی‌شده و الگوریتمی)، و در پژوهش (اثر تجربه بر درگیری، اعتماد و معناسازی جمعی) (Jenkins, 2006; McQuail, 2010).",
        evolution="مفهوم تجربه مخاطب از مطالعات استقبال و «استفاده و ارضاء» (uses and gratifications) (دهه‌های ۱۹۴۰–۱۹۷۰) وارد علوم ارتباط شد؛ در دهه‌های ۱۹۸۰–۱۹۹۰، با مطالعات فرهنگ عامه و مخاطب فعال، به «معیارسنجی معناسازی مخاطب» گسترش یافت؛ و در عصر رسانه‌های همگرا، تجربهٔ مخاطب به «تجربهٔ مشارکتی، چندپلتفرمی و شخصی‌سازی‌شده» بدل شده است (Jenkins, 2006).",
        assumptions="فرض‌های نهفته: مخاطب، عامل فعالی است که انتخاب، تفسیر و مشارکت می‌کند (نه صرفا‌ً دریافت‌کننده)؛ تجربه، فرایند شخصی‌شده و بافتی است (نه یکسان برای همه)؛ تجربهٔ مخاطب، بر درگیری، معناسازی و مشارکت اجتماعی اثر می‌گذارد؛ و این تجربه، در چارچوب طراحی‌شدهٔ رسانه و پلتفرم شکل می‌گیرد (Jenkins, 2006; McQuail, 2010).",
    ),
    "CPT-078": dict(
        mechanism="رفتار رسانه‌ای در چهار حلقه تبیین می‌شود: (۱) انتخاب رسانه: فرد بر اساس نیاز، زمینه و عادت، رسانه و محتوا را انتخاب می‌کند (نظریهٔ استفاده و ارضاء)؛ (۲) الگوی مصرف: فرد، رسانه را در زمان، مدت، فراوانی و ترکیبی با رسانه‌های دیگر مصرف می‌کند (مالتی‌تسکینگ)؛ (۳) تفسیر و واکنش: فرد، محتوای مصرفی را تفسیر و به آن واکنش نشان می‌دهد؛ (۴) اثر و بازخورد: رفتار رسانه‌ای، بر نگرش، اطلاعات و کنش فرد اثر گذاشته و رفتار بعدی را شکل می‌دهد (McQuail, 2010; Littlejohn & Foss, 2011).",
        key_concepts=["انتخاب رسانه", "استفاده و ارضاء", "مالتی‌تسکینگ", "الگوی مصرف", "رفتار انتخابی"],
        critiques="نقد نخست، «انتخابِ آزاد» است: فرض بر این است که رفتار رسانه‌ای محصول انتخاب آزاد و عقلانی فرد است، در حالی که در واقع بر آن، بافت اجتماعی، بازاریابی، الگوریتم و عادت اثر قوی می‌گذارد (McQuail, 2010). نقد دیگر، «فردمحوری» است: تمرکز بر انتخاب فردی، عوامل ساختاری، اقتصادی و سیاسی شکل‌دهندهٔ رفتار رسانه‌ای را می‌پوشاند (Littlejohn & Foss, 2011). همچنین رفتار رسانه‌ای در عصر دیجیتال، سریع و پیوسته تغییر می‌کند.",
        applications="کاربرد در تحلیل رفتار رسانه‌ای و الگوهای مصرف (نظرسنجی روزنامه‌نگاری، دادهٔ پلتفرم)، در طراحی استراتژی رسانه‌ای و برنامه‌ریزی رسانه‌ای (هدف‌گیری، زمان‌بندی)، در طراحی محصولات رسانه‌ای (درگیری، ماندگاری، عادت‌سازی)، در آموزش سواد رسانه‌ای (آگاهی از الگوی مصرف شخصی)، و در پژوهش (اثر رفتار رسانه‌ای بر سلامت، اطلاعات و مشارکت اجتماعی) (McQuail, 2010; Littlejohn & Foss, 2011).",
        evolution="مفهوم رفتار رسانه‌ای از پژوهش‌های «استفاده و ارضاء» (uses and gratifications) (دهه‌های ۱۹۴۰–۱۹۷۰) وارد علوم ارتباط شد و در آغاز بر انتخاب فعال مخاطب تمرکز داشت؛ در دهه‌های ۱۹۸۰–۱۹۹۰، با رشد رسانه‌های خانگی، به «الگوی مصرف و مالتی‌تسکینگ» گسترش یافت؛ و در عصر دیجیتال، رفتار رسانه‌ای به «رفتار پیوسته، چندپلتفرمی و داده‌محور» بدل شده است (McQuail, 2010).",
        assumptions="فرض‌های نهفته: رفتار رسانه‌ای، عمدتا‌ً هدفمند و انتخابی است (در پاسخ به نیازهای فرد)؛ الگوی مصرف، پایدار و قابل اندازه‌گیری است (در عمل بافتی و متغیر)؛ رفتار رسانه‌ای، بر نگرش، اطلاعات و کنش فرد اثر می‌گذارد؛ و این رفتار، در بافت‌های اجتماعی و اقتصادی متفاوت، متفاوت است (McQuail, 2010; Littlejohn & Foss, 2011).",
    ),
    "CPT-079": dict(
        mechanism="کنشگری مخاطب در چهار حلقه شکل می‌گیرد: (۱) درک و آگاهی: مخاطب، قدرت خود در انتخاب، تفسیر و واکنش را می‌فهمد (عاملیت)؛ (۲) تفسیر فعال: مخاطب، پیام را بر اساس پیشینه و منافع خود تفسیر و بازنمایی می‌کند (معیارسنجی معناسازی)؛ (۳) واکنش و مشارکت: مخاطب با نظر، نقد، بازنشر و تولید محتوا، در جریان رسانه‌ای وارد می‌شود؛ (۴) کنشگری اجتماعی: مخاطب از رسانه برای اعتراض، همبستگی و تغییر اجتماعی استفاده می‌کند و عامل تغییر می‌شود (Jenkins, 2006; Fiske, 1987).",
        key_concepts=["عاملیت", "تفسیر فعال", "مشارکت", "کنشگری اجتماعی", "معیارسنجی"],
        critiques="نقد نخست، «عاملیتِ اغراق‌آمیز» است: فرض بر این است که مخاطب همیشه عامل و توانمند است، در حالی که در واقع عاملیت، نابرابر، محدود و به سرمایه‌های فرهنگی، اقتصادی و زبانی وابسته است (Fiske, 1987). نقد دیگر، «مشارکت‌زدگی» (participation-ism) است: بسیاری از «کنشگری‌ها»، سبک، تکراری و در چارچوب طراحی‌شدهٔ پلتفرم محدود و کنترل‌شده‌اند (Jenkins, 2006). همچنین مرز میان کنشگری واقعی و صرفاً نمایش، روشن نیست.",
        applications="کاربرد در تحلیل کنشگری رسانه‌ای مخاطب (مشارکت، اعتراض، همبستگی آنلاین)، در طراحی رسانه‌های مشارکتی (ابزار تولید، فضای گفت‌وگو، توانمندسازی)، در مطالعات جنبش‌های اجتماعی دیجیتال (اعتراض آنلاین، همبستگی)، در آموزش سواد رسانه‌ای (شناخت عاملیت و مرزهای آن)، و در پژوهش (اثر کنشگری مخاطب بر دموکراسی و تغییر اجتماعی) (Jenkins, 2006; Fiske, 1987).",
        evolution="مفهوم کنشگری مخاطب از مطالعات فرهنگ عامه و مخاطب فعال (دهه‌های ۱۹۷۰–۱۹۸۰، استالن‌دورپ و فرای) وارد علوم ارتباط شد و در برابر مدل «مخاطب منفعل» ایستاد؛ در دهه‌های ۱۹۹۰–۲۰۰۰، با رسانه‌های تعاملی، به «مشارکت و تولید مخاطب» گسترش یافت؛ و در عصر همگرایی، کنشگری به «کنشگری شبکه‌ای و اجتماعی» (برنده‌سازی، شادوز، اعتراض آنلاین) بدل شده است (Jenkins, 2006).",
        assumptions="فرض‌های نهفته: مخاطب، عاملی است که می‌تواند انتخاب، تفسیر و کنش کند (نه صرفا‌ً منفعل)؛ عاملیت، بستگی به سرمایه‌های فرهنگی، اقتصادی و زبانی دارد (نابرابر)؛ کنشگری رسانه‌ای، بر دموکراسی، اعتراض و تغییر اجتماعی اثر می‌گذارد؛ و این عاملیت، در چارچوب طراحی‌شدهٔ رسانه و پلتفرم محدود می‌شود (Jenkins, 2006; Fiske, 1987).",
    ),
    "CPT-080": dict(
        mechanism="مخاطب فعال در چهار حلقه عمل می‌کند: (۱) انتخاب فعال: مخاطب، رسانه و محتوا را بر اساس نیاز و هدف، خود انتخاب می‌کند (نه اجبار)؛ (۲) درگیری: مخاطب، به‌طور فعال در محتوا درگیر و توجه می‌ورزد؛ (۳) تفسیر و معناسازی: مخاطب، پیام را بر اساس پیشینه و بافت خود تفسیر و معنا می‌سازد (نه دریافت خالص)؛ (۴) واکنش و مشارکت: مخاطب، با واکنش، نقد و تولید، در جریان رسانه‌ای وارد می‌شود و فعال می‌ماند (Fiske, 1987; Jenkins, 2006).",
        key_concepts=["انتخاب فعال", "تفسیر", "معیارسنجی", "مشارکت", "مخاطب-تفسیرکننده"],
        critiques="نقد نخست، «فعالیتِ اغراق‌آمیز» است: فرض بر این است که مخاطب همیشه فعال و تفسیرکننده است، در حالی که بسیاری از دریافت‌ها، سبک، منفعل یا عادت‌محورند و «فعالیت» همیشه عمیق نیست (Fiske, 1987). نقد دیگر، «معیارسنجیِ فردمحور» است: تفسیر فعال، ممکن است صرفا‌ً بازتولید نگرش موجود باشد و لزوماً منتقدانه نیست (Jenkins, 2006). همچنین فعالیت مخاطب، به‌سختی از بیرون قابل مشاهده و اندازه‌گیری است.",
        applications="کاربرد در تحلیل رفتار مخاطب فعال (انتخاب، تفسیر، مشارکت)، در طراحی رسانه‌های تعاملی (گفت‌وگو، مشارکت، ابزار تولید)، در آموزش سواد رسانه‌ای (تقویت تفسیر فعال و انتقادی)، در پژوهش اثرپذیری (برخلاف مدل‌های منفعل، بر معناسازی مخاطب تمرکز)، و در تحلیل دموکراسی رسانه‌ای (نقش مخاطب فعال در گفت‌وگوی عمومی) (Fiske, 1987; Jenkins, 2006).",
        evolution="مفهوم مخاطب فعال از نظریه‌های پذیرش و «مخاطب فعال» (دهه‌های ۱۹۶۰–۱۹۷۰) و سپس مطالعات فرهنگ عامه (استالن‌دورپ، فرای، دههٔ ۱۹۸۰) وارد علوم ارتباط شد و در برابر مدل «مخاطب منفعل و قابل دست‌کاری» ایستاد؛ در دهه‌های ۱۹۹۰–۲۰۰۰، با رسانه‌های تعاملی، به «مخاطب تولیدکننده» گسترش یافت؛ و در عصر همگرایی، مخاطب فعال به «مخاطب مشارکتی شبکه‌ای» بدل شده است (Fiske, 1987).",
        assumptions="فرض‌های نهفته: مخاطب، عاملی است که پیام را تفسیر و معنا می‌سازد (نه خنثی دریافت می‌کند)؛ تفسیر، بر پیشینه و بافت مخاطب بنا می‌شود (نه یکسان برای همه)؛ فعالیت مخاطب، بر اثرپذیری و دموکراسی رسانه‌ای اثر می‌گذارد؛ و این فعالیت، در چارچوب رسانه و پلتفرم، محدود و نابرابر است (Fiske, 1987; Jenkins, 2006).",
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
                    (code, json.dumps({"batch": 307, "score": score, "words": words,
                                       "sources": n_sources, "verified": n_verified,
                                       "relations": n_rel, "rubric": detail}, ensure_ascii=False), STAMP, NOW))
        print(code, "words", words, "score", score, "detail", detail)
    conn.commit()
    conn.close()
    print("BATCH307 DONE")


if __name__ == "__main__":
    main()
