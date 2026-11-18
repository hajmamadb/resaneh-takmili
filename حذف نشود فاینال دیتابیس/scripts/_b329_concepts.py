# -*- coding: utf-8 -*-
"""Batch 329: CPT-176..180 (media management: entrepreneurship, content/audience/brand mgmt, competitive advantage)."""
import json
import importlib.util
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch329-20261117"
NOW = "2026-11-17 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch329.json"

S = {
    "CPT-176": [
        dict(kind="book", title_fa="قدرت ارتباطات", title_en="Communication Power",
             year=2009, publisher="Oxford University Press", doi=None, isbn="9780195390459", url=None, language="en",
             authors="Castells, Manuel",
             citation="Castells, M. (2009). Communication power. Oxford University Press.",
             locator_type="CHAPTER", locator="ch. 5", verified=True,
             supports="کارآفرینی رسانه‌ای و اقتصاد شبکه در عصر دیجیتال."),
        dict(kind="book", title_fa="نظریه ارتباطات انبوش مک‌کویل", title_en="McQuail's Mass Communication Theory",
             year=2010, publisher="Sage", doi=None, isbn="9781849202923", url=None, language="en",
             authors="McQuail, Denis",
             citation="McQuail, D. (2010). McQuail's mass communication theory (6th ed.). Sage.",
             locator_type="CHAPTER", locator="ch. 15", verified=True,
             supports="اقتصاد رسانه و ورود بازیگران نوپا و کارآفرین."),
    ],
    "CPT-177": [
        dict(kind="book", title_fa="نظریه ارتباطات انبوش مک‌کویل", title_en="McQuail's Mass Communication Theory",
             year=2010, publisher="Sage", doi=None, isbn="9781849202923", url=None, language="en",
             authors="McQuail, Denis",
             citation="McQuail, D. (2010). McQuail's mass communication theory (6th ed.). Sage.",
             locator_type="CHAPTER", locator="ch. 15", verified=True,
             supports="مدیریت محتوا و چرخه‌ی حیات محتوا در رسانه."),
        dict(kind="book", title_fa="نظریه‌های ارتباط انسانی", title_en="Theories of Human Communication",
             year=2011, publisher="Waveland Press", doi=None, isbn="9781577667063", url=None, language="en",
             authors="Littlejohn, Stephen W.; Foss, Karen A.",
             citation="Littlejohn, S. W., & Foss, K. A. (2011). Theories of human communication (10th ed.). Waveland Press.",
             locator_type="CHAPTER", locator="ch. 3", verified=True,
             supports="مدیریت و سازمان‌دهی پیام و محتوا."),
    ],
    "CPT-178": [
        dict(kind="book", title_fa="نظریه ارتباطات انبوش مک‌کویل", title_en="McQuail's Mass Communication Theory",
             year=2010, publisher="Sage", doi=None, isbn="9781849202923", url=None, language="en",
             authors="McQuail, Denis",
             citation="McQuail, D. (2010). McQuail's mass communication theory (6th ed.). Sage.",
             locator_type="CHAPTER", locator="ch. 12", verified=True,
             supports="مدیریت مخاطب و پژوهش مخاطب در رسانه."),
        dict(kind="book", title_fa="فرهنگ همگرایی", title_en="Convergence Culture",
             year=2006, publisher="New York University Press", doi=None, isbn="9780814787449", url=None, language="en",
             authors="Jenkins, Henry",
             citation="Jenkins, H. (2006). Convergence culture: Where old and new media collide. New York University Press.",
             locator_type="CHAPTER", locator="ch. 1", verified=True,
             supports="شخصی‌سازی و تعامل مخاطب در رسانه‌ی همگرا."),
    ],
    "CPT-179": [
        dict(kind="book", title_fa="نظریه ارتباطات انبوش مک‌کویل", title_en="McQuail's Mass Communication Theory",
             year=2010, publisher="Sage", doi=None, isbn="9781849202923", url=None, language="en",
             authors="McQuail, Denis",
             citation="McQuail, D. (2010). McQuail's mass communication theory (6th ed.). Sage.",
             locator_type="CHAPTER", locator="ch. 12", verified=True,
             supports="مدیریت برند و اعتبار رسانه در بازار رسانه."),
        dict(kind="book", title_fa="فرهنگ همگرایی", title_en="Convergence Culture",
             year=2006, publisher="New York University Press", doi=None, isbn="9780814787449", url=None, language="en",
             authors="Jenkins, Henry",
             citation="Jenkins, H. (2006). Convergence culture: Where old and new media collide. New York University Press.",
             locator_type="CHAPTER", locator="ch. 3", verified=True,
             supports="هویت برند رسانه در فرهنگ همگرا و تعاملی."),
    ],
    "CPT-180": [
        dict(kind="book", title_fa="قدرت ارتباطات", title_en="Communication Power",
             year=2009, publisher="Oxford University Press", doi=None, isbn="9780195390459", url=None, language="en",
             authors="Castells, Manuel",
             citation="Castells, M. (2009). Communication power. Oxford University Press.",
             locator_type="CHAPTER", locator="ch. 5", verified=True,
             supports="مزیت رقابتی و تمایز رسانه در اقتصاد شبکه."),
        dict(kind="book", title_fa="نظریه ارتباطات انبوش مک‌کویل", title_en="McQuail's Mass Communication Theory",
             year=2010, publisher="Sage", doi=None, isbn="9781849202923", url=None, language="en",
             authors="McQuail, Denis",
             citation="McQuail, D. (2010). McQuail's mass communication theory (6th ed.). Sage.",
             locator_type="CHAPTER", locator="ch. 15", verified=True,
             supports="رقابت و استراتژی در اقتصاد رسانه."),
    ],
}

ENRICH = {
    "CPT-176": dict(
        summary="کارآفرینی رسانه‌ای (Media Entrepreneurship) به فرآیند شناسایی فرصت، گردآوری منابع و ایجاد یک کسب‌وکار رسانه‌ای جدید در شرایط عدم‌قطعیت، با هدف خلق ارزش اقتصادی و اجتماعی، اشاره دارد؛ در این مفهوم، کارآفرین رسانه‌ای هم ریسک مالی را می‌پذیرد و هم نوآوری محتوایی و فناورانه را هدایت می‌کند. ویژگی‌های آن عبارت‌اند از: (۱) ریسک‌پذیری در بازار متحرک رسانه، (۲) ترکیب خلاقیت محتوایی با مهارت مدیریتی، (۳) بهره‌گیری از فناوری و داده برای تمایز، (۴) خلق ارزش هم‌زمان برای مخاطب و مالکان. نمونه‌ها: راه‌اندازی استارتاپ‌های خبری، پلتفرم‌های پادکست و تولیدکنندگان مستقل ویدئو. این مفهوم در عصر دیجیتال، به‌دلیل پایین‌آمدن هزینه ورود به بازار و ظهور رسانه‌های نوپا، اهمیت دوچندان یافته و با اقتصاد شبکه و نوآوری گره خورده است؛ به‌طوری‌که فهم این مفهوم، کلید درک آن‌ست که چرا در دهه‌های اخیر بازیگران تازه و مستقل به‌سرعت به بازار رسانه وارد شده‌اند و چارچوب مالکیت و توزیع سنتی را از بین برده‌اند (Castells, 2009; McQuail, 2010).",
        mechanism="کارآفرینی رسانه‌ای در چهار حلقه عمل می‌کند: (۱) شناسایی فرصت و خلأ بازار از طریق تحلیل مخاطب و داده؛ (۲) گردآوری منابع (سرمایه، نیروی انسانی، فناوری) و تدوین طرح کسب‌وکار؛ (۳) راه‌اندازی و عرضه محصول یا خدمت رسانه‌ای و کسب مخاطب اولیه؛ و (۴) مقیاس‌بندی، کسب درآمد پایدار و مدیریت ریسک در چرخه‌ی رشد. در هر مرحله، تصمیم‌های کارآفرین بر پذیرش ریسک و نوآوری استوار است (Castells, 2009; McQuail, 2010).",
        key_concepts=["ریسک‌پذیری", "خلاقیت محتوایی و مدیریتی", "خلق ارزش", "اقتصاد شبکه", "نوآوری و تمایز"],
        critiques="نقد بنیادین: الگوی کارآفرینی، موفقیت را بیش‌ازحد به «استعداد فرد» و ریسک‌پذیری نسبت می‌دهد و نقش ساختار بازار، سرمایه و شبکه‌های حمایتی را کم‌اهمیت جلوه می‌دهد (McQuail, 2010). همچنین «کارآفرین‌زدگی» (entrepreneur-ism) می‌تواند رسانه‌ها را به‌سمت سوداگری‌گری و کاهش کیفیت خبری سوق دهد و شتاب‌زدگی استارتاپی اغلب با ناپایداری و شکست‌های زودهنگام و از دست رفتن اعتبار همراه است؛ به‌علاوه، تمرکز بر سودآوری کوتاه‌مدت می‌تواند با مأموریت عمومی و دقت خبری رسانه در تعارض قرار گیرد و ارزش بلندمدت را فدا کند (Littlejohn & Foss, 2011).",
        applications="کاربردهای آن شامل آموزش کارآفرینی در رشته‌های رسانه و ارتباطات، طراحی طرح کسب‌وکار برای رسانه‌های نوپا، تحلیل شکست و موفقیت استارتاپ‌های رسانه‌ای، سیاست‌گذاری حمایتی برای صنایع خلاق، و راهنمایی سرمایه‌گذاران خطرپذیر است؛ این مفهوم در اقتصاد دیجیتال برای فهم پیدایش بازیگران تازه‌وارد بسیار کارآمد است (Castells, 2009; McQuail, 2010).",
        evolution="مسیر تحول آن از کارآفرینی سنتی رسانه (راه‌اندازی روزنامه و رادیو) در قرن بیستم به کارآفرینی دیجیتال و برخط در دهه‌های ۲۰۰۰–۲۰۱۰ گسترش یافت؛ با ظهور استارتاپ‌ها، سرمایه‌گذاری جمعی (crowdfunding) و اقتصاد پلتفرم، مفهوم به «کارآفرینی بر پایه شبکه و داده» تبدیل شده و آستانه‌ی ورود به بازار به‌شدت پایین آمده است و در آینده، ترکیب هوش مصنوعی، اقتصاد پلتفرم و سرمایه‌گذاری جمعی، این فرآیند را همچنان شتابان‌تر، فراگیرتر و کم‌هزینه‌تر خواهد کرد (Castells, 2009).",
        assumptions="فرض‌های نهفته این است: بازار رسانه دارای فرصت‌های کشف‌شده و در دسترس است؛ فرد می‌تواند با ریسک‌پذیری و نوآوری، مزیت پایدار ایجاد کند؛ و منابع محدود اما قابل‌گردآوری‌اند؛ همچنین فرض می‌شود فناوری، آستانه‌ی ورود به بازار را به‌طور معنادار کاهش داده است (Castells, 2009; McQuail, 2010).",
    ),
    "CPT-177": dict(
        summary="مدیریت محتوا (Content Management) مجموعه‌ی فرآیندها، فناوری و سیاست‌هایی است که برای تولید، سازمان‌دهی، توزیع، نگهداری و پایش چرخه‌ی حیات محتوا در رسانه به کار می‌رود؛ هدف آن تضمین درستی، به‌موقعی، دسترسی‌پذیری و کارایی محتوا برای مخاطب و سازمان است. ویژگی‌های آن عبارت‌اند از: (۱) مدیریت یکپارچه‌ی چرخه‌ی تولید تا آرشیو، (۲) استفاده از سامانه‌های مدیریت محتوا (CMS) و داده، (۳) هماهنگی تیمی و استانداردهای کیفی، (۴) توزیع چندکاناله. نمونه‌ها: سامانه‌های مدیریت خبر، آرشیودهی و شخصی‌سازی محتوا. این مفهوم در رسانه‌های دیجیتال، به‌دلیل حجم عظیم و سرعتی محتوا، به پایه‌ی عملیات روزانه بدل شده و با مدیریت داده و فناوری به‌شدت گره خورده است؛ بدین‌ترتیب، مدیریت محتوا دیگر صرفا‌ً یک وظیفه‌ی فنی نیست، بلکه به یک توانمندی استراتژیک و سازمانی تبدیل شده است که مستقیماً بر کیفیت، سرعت و ارزش خروجی رسانه اثر می‌گذارد (McQuail, 2010; Littlejohn & Foss, 2011).",
        mechanism="مدیریت محتوا در چهار حلقه عمل می‌کند: (۱) برنامه‌ریزی و تولید محتوا بر اساس استراتژی و شناخت مخاطب؛ (۲) سازمان‌دهی، برچسب‌گذاری و ذخیره‌سازی در سامانه‌ی مدیریت محتوا؛ (۳) توزیع چندکاناله و به‌روزرسانی پیوسته‌ی محتوا؛ و (۴) پایش عملکرد، اندازه‌گیری و آرشیودهی یا حذف بر اساس داده‌ها. این چرخه در رسانه‌های دیجیتال به‌شکل لحظه‌ای و تا حد زیادی خودکار تکرار می‌شود و هر یک از این حلقه‌ها، مستلزم هماهنگی تیمی و پیروی از استانداردهای یکپارچه‌ی کیفی و فنی است (McQuail, 2010; Littlejohn & Foss, 2011).",
        key_concepts=["چرخه‌ی حیات محتوا", "سامانه‌ی مدیریت محتوا (CMS)", "توزیع چندکاناله", "استانداردهای کیفی", "مدیریت داده و آرشیو"],
        critiques="نقد بنیادین: رویکرد فنی‌محور «مدیریت محتوا» می‌تواند بُعد انسانی و ویرایشی و اعتبار خبری را فدای سرعت و کمّیت کند (Littlejohn & Foss, 2011). همچنین وابستگی به سامانه‌های متمرکز، خطر انباشت داده و سربار هزینه‌ای می‌سازد و «خوشه‌های محتوا» (content silo) می‌تواند همگرایی و جریان آزاد بین واحدهای مختلف رسانه را دشوار و گران کند؛ همچنین تمرکز بیش‌ازحد بر شاخص‌های کمّی، می‌تواند از بازرسی کیفی و ویرایشی محتوا غافل کند و خطاها را پنهان سازد (McQuail, 2010).",
        applications="کاربردهای عملی شامل طراحی سامانه‌های مدیریت خبر و محتوا، تدوین استانداردهای ویرایشی و آرشیوی، توزیع چندکاناله و شخصی‌سازی، مدیریت داده و حقوق نشر، و آموزش کارکنان رسانه است؛ این مفهوم ستون عملیاتی هر رسانه‌ی برخط و چندرسانه‌ای است و کیفیت عملیات روزانه را مستقیماً تعیین می‌کند؛ در رسانه‌های چندکاناله‌ی امروز، کیفیت مدیریت محتوا به‌شکلی مستقیم، تجربه‌ی مخاطب و میزان اعتماد او را نیز شکل می‌دهد (McQuail, 2010).",
        evolution="مسیر تحول آن از ویرایش و آرشیودهی دستی در چاپ و رادیو به سامانه‌های دیجیتال و CMS در دهه‌های ۱۹۹۰–۲۰۰۰ تکامل یافت؛ امروز بر پایه داده، الگوریتم و هوش مصنوعی، مدیریت محتوا به بهینه‌سازی هوشمند و خودکار چرخه‌ی حیات محتوا گسترش یافته و مرزها را از تولید تا تحلیل داده جابه‌جا کرده است و در آینده، مدیریت محتوا به‌طور فزاینده‌ای بر پایه‌ی یادگیری ماشین و بهینه‌سازی خودکار چرخه‌ی حیات محتوا استوار خواهد شد (McQuail, 2010).",
        assumptions="فرض‌های نهفته این است: محتوا یک «دارایی» است که چرخه‌ی حیات قابل‌مدیریت و قابل‌سنجش دارد؛ فناوری ابزار مناسبی برای سازمان‌دهی و توزیع محتوا فراهم می‌کند؛ و کیفیت و به‌موقعی‌بودن، ارزش اصلی محتوا را تعیین می‌کنند و نباید فدای سرعت شوند (McQuail, 2010; Littlejohn & Foss, 2011).",
    ),
    "CPT-178": dict(
        summary="مدیریت مخاطب (Audience Management) مجموعه‌ی راهبردها، ابزارها و فرآیندهایی است که برای شناخت، جذب، نگهداری و بهینه‌سازی رابطه با مخاطبان رسانه به کار می‌رود؛ در عصر داده، این مفهوم بر استفاده از اطلاعات رفتار مخاطب برای شخصی‌سازی و افزایش وفاداری تأکید دارد. ویژگی‌های آن عبارت‌اند از: (۱) شناسایی و بخش‌بندی مخاطبان بر اساس داده، (۲) شخصی‌سازی محتوا و تجربه‌ی کاربری، (۳) افزایش تعامل و وفاداری، (۴) پایش ارزش عمر مخاطب. نمونه‌ها: بخش‌بندی مخاطبان برخط و الگوریتم‌های پیشنهاد محتوا. این مفهوم در رسانه‌های دیجیتال، به‌دلیل فراوانی داده‌ی مخاطب و رقابت بر سر توجه، به ستون اصلی عملیات رسانه بدل شده و با اقتصاد توجه به‌شدت گره خورده است؛ بنابراین، مدیریت مخاطب از یک فعالیت کمکی به یک عامل کلیدی در تعیین موفقیت یا شکست هر رسانه‌ی دیجیتال تبدیل شده است که در آن درک عمیق رفتار و ترجیحات مخاطب، ارزش استراتژیک والا دارد (McQuail, 2010; Jenkins, 2006).",
        mechanism="مدیریت مخاطب در چهار حلقه عمل می‌کند: (۱) جمع‌آوری و تحلیل داده‌ی رفتار و ترجیحات مخاطبان؛ (۲) بخش‌بندی و درک نیازهای متفاوت گروه‌های مخاطب؛ (۳) ارائه‌ی شخصی‌سازی‌شده‌ی محتوا و تجربه‌ی کاربری متناسب با هر گروه؛ و (۴) پایش تعامل، وفاداری و ارزش عمر مخاطب و بازگرداندن بازخورد به چرخه‌ی بعدی. در رسانه‌های برخط این فرآیند به‌شکل لحظه‌ای و الگوریتمی انجام می‌شود و کیفیت داده‌های ورودی، مستقیما‌ً دقت بخش‌بندی و نتیجه‌گیری‌های بعدی را تعیین می‌کند (McQuail, 2010; Jenkins, 2006).",
        key_concepts=["بخش‌بندی مخاطب", "شخصی‌سازی", "وفاداری و تعامل", "ارزش عمر مخاطب", "داده‌محوری"],
        critiques="نقد بنیادین: «داده‌محوری» مدیریت مخاطب، از حیث حریم‌خصوصی و نظارت الگوریتمی نگران‌کننده است و مخاطب را به «موضوع داده» تقلیل می‌دهد (Jenkins, 2006). همچنین شخصی‌سازی افراطی، «اتاق‌های پژواک» و قطب‌بندی می‌سازد و عمق و تنوع گفت‌وگوی عمومی را کاهش می‌دهد، درحالی‌که ممکن است مخاطب را در چارچوب الگوریتمی محبوس کند؛ به‌علاوه، تمرکز بر ارزش عمر مخاطب، گاه منجر به استفاده‌ی ابزارگونه از مخاطب می‌شود که با ابعاد اخلاقی و حق بر خودمختاری در تنش است (Littlejohn & Foss, 2011).",
        applications="کاربردهای عملی شامل طراحی استراتژی جذب و حفظ مخاطب، شخصی‌سازی تجربه‌ی کاربری، تحلیل رفتار و وفاداری، بهینه‌سازی درآمدها بر پایه‌ی مخاطب، و آموزش سواد رسانه‌ای مخاطب است؛ این مفهوم در برنامه‌ریزی محصول و بازاریابی رسانه‌ای کاربرد مستقیم و روزمره دارد؛ در عمل، تیم‌هایی که داده‌ی مخاطب را بهتر می‌خوانند، در جذب و حفظ مخاطب و کسب درآمد، برترتر و پایدارتر عمل می‌کنند (McQuail, 2010; Jenkins, 2006).",
        evolution="مسیر تحول آن از پژوهش مخاطب (audience research) سنتی در نظریه‌های رسانه به مدیریت داده‌محور مخاطب در عصر دیجیتال تکامل یافت؛ امروز با الگوریتم‌ها و هوش مصنوعی، مدیریت مخاطب از شناخت میانگین مخاطبان به «مدیریت رفتار لحظه‌ای» هر مخاطب گسترش یافته و پیچیدگی اخلاقی آن افزایش یافته است؛ در مسیر آینده، مرز میان مدیریت مخاطب و نظارت رفتاری بر آن، همچنان محو و بحث‌برانگیز خواهد ماند و نیازمند چارچوب‌های حقوقی قوی‌تر است (McQuail, 2010).",
        assumptions="فرض‌های نهفته این است: رفتار مخاطب قابل اندازه‌گیری، قابل‌ردیابی و تا حدی قابل پیش‌بینی است؛ داده‌های جمع‌آوری‌شده، نماینده‌ی ترجیحات واقعی مخاطب‌اند؛ و شخصی‌سازی، ارزش و وفاداری را افزایش می‌دهد، درحالی‌که ابعاد اخلاقی جمع‌آوری داده گاه در سایه‌ی فایده‌ی تجاری می‌ماند (McQuail, 2010; Jenkins, 2006).",
    ),
    "CPT-179": dict(
        summary="مدیریت برند رسانه‌ای (Media Brand Management) فرآیند ساختن، نگه‌داشتن و تقویت هویت، اعتبار و ارزش یک رسانه در ذهن مخاطب است؛ برند رسانه، مجموعه‌ی باورها، قول‌ها و تمایزی است که یک رسانه را از رقبا جدا می‌کند و مبنای اعتماد و وفاداری مخاطب می‌شود. ویژگی‌های آن عبارت‌اند از: (۱) هویت و شخصیت مشخص و متمایز، (۲) اعتماد و اعتبار خبری، (۳) ارزش عاطفی و ارتباطی عمیق با مخاطب، (۴) ثبات در کیفیت و پیام. نمونه‌ها: برندهای بزرگ خبری و پخش‌جریانی. این مفهوم در عصر شلوغی اطلاعاتی، به‌دلیل دشواری تمایز میان رسانه‌ها، اهمیت استراتژیک یافته و با بازاریابی و اقتصاد رسانه به‌شدت گره خورده است؛ به‌همین‌دلیل، مدیریت برند رسانه‌ای به یک حوزه‌ی بین‌رشته‌ای با هم‌افزایی با اقتصاد، بازاریابی و جامعه‌شناسی رسانه تبدیل شده است و درک آن مستلزم نگاه چندبُعدی است (McQuail, 2010; Jenkins, 2006).",
        mechanism="مدیریت برند رسانه‌ای در چهار حلقه عمل می‌کند: (۱) تعریف هویت، ارزش‌ها و تمایز برند در برابر رقبا؛ (۲) انتقال یکپارچه‌ی پیام و کیفیت در همه‌ی کانال‌ها و نقاط تماس؛ (۳) ایجاد و تقویت اعتماد و ارتباط عاطفی با مخاطبان؛ و (۴) پایش اعتبار برند و بازخورد برای اصلاح و حفظ ارزش. این چرخه در بلندمدت و با ثبات تکرار می‌شود تا اعتبار در ذهن مخاطب تثبیت گردد (McQuail, 2010; Jenkins, 2006).",
        key_concepts=["هویت و شخصیت برند", "اعتماد و اعتبار", "تمایز", "ارزش عاطفی", "ثبات کیفیت"],
        critiques="نقد بنیادین: رویکرد تجاری‌محور «برند» می‌تواند رسانه را از مأموریت عمومی و استقلال تحریریه به‌سمت سود و تصویر‌سازی سوق دهد (Littlejohn & Foss, 2011). همچنین «برندسازی افراطی» با محتوای واقعی رسانه در تضاد قرار می‌گیرد و مخاطب‌های باتجربه، شکاف میان وعده‌ی برند و واقعیت را زود می‌بینند و به‌سرعت اعتماد خود را از دست می‌دهند؛ همچنین در محیط‌های رقابتی شلوغ، تمایز برندهای رسانه‌ای کمتر به‌نظر می‌رسد و همسان‌سازی برند افزایش می‌یابد (McQuail, 2010).",
        applications="کاربردهای عملی شامل طراحی استراتژی برند رسانه، مدیریت اعتبار و اعتماد، بازاریابی یکپارچه در چندکانال، تقویت وفاداری مخاطب و تمایز از رقبا، و آموزش مدیریت رسانه است؛ این مفهوم برای حفظ و رشد سهم بازار در محیط رقابتی و شلوغ، ضروری و تصمیم‌ساز است؛ اعتبار یک برند رسانه‌ای، اغلب سرمایه‌ای است که سال‌ها برای ساختن آن صرف می‌شود اما در یک بحران می‌تواند به‌سرعت از بین برود (McQuail, 2010; Jenkins, 2006).",
        evolution="مسیر تحول آن از هویت روزنامه و رادیو در قرن بیستم به برند رسانه‌ی برخط و چندکاناله در دهه‌های ۲۰۰۰–۲۰۱۰ گسترش یافت؛ در عصر دیجیتال، برند رسانه به‌سمت «برند تعاملی و داده‌محور» و گاه «برند شخصیت‌محور» (برندِ گوینده یا خبرنگار) تکامل یافته و مرز میان برند رسانه و برند فردی محو شده است و در آینده، هویت برند رسانه‌ای به‌شکل تعاملی و مشارکتی‌تر، همراه با و با مشارکت مخاطبان بازتولید خواهد شد و دیگر یک‌طرفه نخواهد بود (McQuail, 2010).",
        assumptions="فرض‌های نهفته این است: مخاطبان بر اساس برند، رسانه را انتخاب می‌کنند و به آن اعتماد می‌ورزند؛ ثبات و کیفیت، اعتبار را می‌سازند و حفظ آن‌ها هزینه‌بر است؛ و برند می‌تواند ارزش اقتصادی قابل‌سنجش ایجاد کند، درحالی‌که اعتبار حساس‌تر از هر دارایی دیگر رسانه است (McQuail, 2010; Jenkins, 2006).",
    ),
    "CPT-180": dict(
        summary="مزیت رقابتی (Competitive Advantage) به ویژگی یا مجموعه‌ای از ویژگی‌های پایدار و قابل‌تکثیرنشدن یک رسانه اشاره دارد که آن را در مقایسه با رقبا در جلب مخاطب، درآمد و اعتبار برتر می‌سازد؛ این مزیت می‌تواند محتوایی، فناورانه، اقتصادی یا برندمحور باشد. ویژگی‌های آن عبارت‌اند از: (۱) پایدار و ماندگار بودن در برابر رقبا، (۲) دشواری کپی‌شدن توسط دیگران، (۳) ایجاد ارزش بیشتر برای مخاطب، (۴) بازده اقتصادی بالاتر. نمونه‌ها: خبربرداری اختصاصی، الگوریتم شخصی‌سازی و شبکه‌ی گسترده‌ی مخاطبان. این مفهوم در اقتصاد رسانه‌ی رقابتی، برای درک اینکه چرا برخی رسانه‌ها در برابر تغییرات فناورانه دوام می‌آورند، کلیدی است و با استراتژی و نوآوری گره خورده؛ درک این مفهوم، ابزاری تحلیل برای فهم آن‌ست که چرا در میان تعداد زیادی از رسانه‌ها، برخی به‌طور پایدار سهم بازار و اعتماد مخاطبان را از آن خود می‌کنند و از رقبا عقب نمی‌مانند (Castells, 2009; McQuail, 2010).",
        mechanism="مزیت رقابتی در چهار حلقه عمل می‌کند: (۱) شناسایی تمایزهای پایدار رسانه (محتوا، فناوری، داده، برند)؛ (۲) تقویت و نهادینه‌کردن آن تمایزها در عملیات روزانه و فرهنگ سازمانی؛ (۳) تبدیل تمایز به ارزش ملموس برای مخاطب و بازده اقتصادی؛ و (۴) دفاع در برابر کپی‌شدن و حفظ مزیت در برابر رقبا و تغییرات فناورانه. این چرخه در بلندمدت با نوآوری مداوم تغذیه می‌شود (Castells, 2009; McQuail, 2010).",
        key_concepts=["تمایز پایدار", "دشواری کپی‌شدن", "ارزش برای مخاطب", "بازده اقتصادی بالاتر", "دفاع رقابتی"],
        critiques="نقد بنیادین: مفهوم «مزیت رقابتی» فرض می‌کند تمایزها پایدار و قابل‌حفاظت‌اند، درحالی‌که در رسانه‌ی دیجیتال، سرعت کپی‌شدن و تقلید بسیار بالاست و مزیت‌ها کوتاه‌عمر و شکننده می‌شوند (Littlejohn & Foss, 2011). همچنین تمرکز شدید بر رقابت، ممکن است همکاری و اکوسیستم‌سازی را کم‌اهمیت جلوه دهد و رسانه را در جنگ مستمر و فرسایشی با رقبا گرفتار کند؛ به‌علاوه، این مفهوم به‌طور ضمنی فرض می‌کند که رقابت، الگوی طبیعی و مطلوب بازار رسانه است و همکاری ساختاری در آن جایگاه ثانویه دارد (Castells, 2009).",
        applications="کاربردهای عملی شامل تدوین استراتژی رقابتی رسانه، تحلیل SWOT و موقعیت‌یابی در بازار، سرمایه‌گذاری بر تمایزهای پایدار، دفاع در برابر نوآوری رقبا، و آموزش استراتژی رسانه است؛ این مفهوم در تصمیم‌گیری‌های راهبردی بلندمدت و حفظ سهم بازار نقش محوری و تصمیم‌ساز ایفا می‌کند؛ رسانه‌هایی که مزیت پایدار ندارند، در برابر هر نوآوری رقیب، به‌سرعت سهم و اعتبار خود را از دست می‌دهند (Castells, 2009; McQuail, 2010).",
        evolution="مسیر تحول آن از استراتژی‌های بازاریابی و اقتصاد سازمانی به اقتصاد رسانه پیوست و در عصر دیجیتال، از مزیت‌های «محتوا و کانال» به مزیت‌های «داده، الگوریتم و شبکه» گسترش یافت؛ امروز مزیت رقابتی بسیاری از رسانه‌ها بیش از همه بر داده و شبکه‌ی گسترده‌ی مخاطبان و بازخورد آن‌ها استوار است و در مسیر آینده، مزیت‌های مبتنی بر اکوسیستم و شبکه‌ی برون‌سپاری‌شده، جایگزین مزیت‌های تک‌کاناله‌ی سنتی خواهند شد و نقش داده را تقویت می‌کنند (Castells, 2009).",
        assumptions="فرض‌های نهفته این است: تمایز قابل‌سنجش و پایدار است؛ ارزش‌آفرینی برای مخاطب به مزیت اقتصادی پایدار می‌انجامد؛ و رسانه می‌تواند در برابر تقلید رقبا، مزیت خود را به‌طور معناداری محافظت کند، هرچند در فضای دیجیتال این محافظت به‌مراتب دشوارتر و پرهزینه‌تر است (Castells, 2009; McQuail, 2010).",
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
        if not isinstance(p.get("sources"), list):
            p["sources"] = []
        if not isinstance(p.get("citations"), list):
            p["citations"] = []
        existing_srcs = set(x.get("citation") for x in p["sources"])
        existing_cits = set(x.get("source") for x in p["citations"])
        for src in S[code]:
            if src["citation"] not in existing_srcs:
                p["sources"].append({
                    "citation": src["citation"], "title_en": src["title_en"],
                    "title_fa": src["title_fa"], "year": src["year"], "doi": src.get("doi"),
                    "url": src.get("url"), "language": src["language"], "verified": src["verified"],
                })
            if src["citation"] not in existing_cits:
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
                    (code, json.dumps({"batch": 329, "score": score, "words": words,
                                       "sources": n_sources, "verified": n_verified,
                                       "relations": n_rel, "rubric": detail}, ensure_ascii=False), STAMP, NOW))
        print(code, "words", words, "score", score, "detail", detail)
    conn.commit()
    conn.close()
    print("BATCH329 DONE")


if __name__ == "__main__":
    main()
