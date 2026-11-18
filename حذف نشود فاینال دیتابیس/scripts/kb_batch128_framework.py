# -*- coding: utf-8 -*-
"""Batch 128 (FRAMEWORK): full documentation for MC-728, MC-729, MC-731."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch128-framework-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch128_framework.json"

S = {
    "MC-728": [
        dict(kind="BOOK",
             title_en="Sensemaking in Organizations",
             title_fa="حس‌سازی در سازمان‌ها",
             authors="Weick, K. E.", year=1995,
             publisher="Sage Publications",
             doi=None,
             url="https://www.sagepub.com/shop/buy-a-book/sensemaking-in-organizations-1-4988",
             language="en", isbn=None,
             citation="Weick, K. E. (1995). Sensemaking in Organizations. Thousand Oaks, CA: Sage Publications.",
             locator="book", locator_type="SECTION",
             supports="seven properties of sensemaking and plausibility over accuracy", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Collapse of Sensemaking in Organizations: The Mann Gulch Disaster",
             title_fa="فروپاشی حس‌سازی در سازمان‌ها: فاجعهٔ مان‌گلچ",
             authors="Weick, K. E.", year=1993,
             publisher="Administrative Science Quarterly",
             doi=None, url=None, language="en", isbn=None,
             citation="Weick, K. E. (1993). The collapse of sensemaking in organizations: The Mann Gulch disaster. Administrative Science Quarterly, 38(4), 628-652.",
             locator="38(4):628-652", locator_type="page_range",
             supports="case study of sensemaking collapse under crisis", verified=False),
    ],
    "MC-729": [
        dict(kind="BOOK",
             title_en="Strategic Management in the Media: Theory to Practice",
             title_fa="مدیریت راهبردی در رسانه: از نظریه تا عمل",
             authors="Küng, L.", year=2017,
             publisher="SAGE Publications",
             doi=None,
             url="https://api.pageplace.de/preview/DT0400.9781473987364_A28765658/preview-9781473987364_A28765658.pdf",
             language="en", isbn=None,
             citation="Küng, L. (2017). Strategic Management in the Media: Theory to Practice (2nd ed.). London: SAGE Publications. (First edition 2008)",
             locator="book", locator_type="SECTION",
             supports="media-specific adaptation of strategic management theory", verified=True),
        dict(kind="BOOK",
             title_en="Strategic Management in the Media: Theory to Practice (First Edition)",
             title_fa="مدیریت راهبردی در رسانه: از نظریه تا عمل (ویرایش نخست)",
             authors="Küng, L.", year=2008,
             publisher="SAGE Publications",
             doi=None, url=None, language="en", isbn=None,
             citation="Küng, L. (2008). Strategic Management in the Media: Theory to Practice. London: SAGE Publications.",
             locator="book", locator_type="SECTION",
             supports="first systematic statement of media-specific strategic management", verified=False),
    ],
    "MC-731": [
        dict(kind="BOOK",
             title_en="Affective Publics: Sentiment, Technology, and Politics",
             title_fa="عمومیت‌های عاطفی: احساس، فناوری و سیاست",
             authors="Papacharissi, Z.", year=2015,
             publisher="Oxford University Press",
             doi=None,
             url="https://academic.oup.com/book/26400",
             language="en", isbn=None,
             citation="Papacharissi, Z. (2015). Affective Publics: Sentiment, Technology, and Politics. New York: Oxford University Press.",
             locator="book", locator_type="SECTION",
             supports="affective publics formed through storytelling and shared sentiment on platforms", verified=True),
        dict(kind="BOOK",
             title_en="Marxism and Literature",
             title_fa="مارکسیسم و ادبیات",
             authors="Williams, R.", year=1977,
             publisher="Oxford University Press",
             doi=None, url=None, language="en", isbn=None,
             citation="Williams, R. (1977). Marxism and Literature. Oxford: Oxford University Press.",
             locator="structures of feeling", locator_type="SECTION",
             supports="structures of feeling as pre-articulated social experience", verified=False),
    ],
}

ENRICH = {
    "MC-728": dict(
        year=1995,
        summary="حس‌سازی سازمانی، نظریه‌ای است که کارل وایک در کتاب سال ۱۹۹۵ صورت‌بندی کرد و می‌گوید سازمان‌ها و اعضای آنها واقعیت را در جریان کنش و ارتباط مداوم «می‌سازند» و «می‌فهمند». حس‌سازی فرایندی است که در آن افراد به تجربهٔ جاری معنا می‌دهند: با انتخاب نشانه‌ها، ساختن روایت، مقایسه با تجربهٔ گذشته و چانه‌زنی با دیگران، تصویری باورپذیر از موقعیت می‌سازند تا بتوانند عمل کنند. وایک هفت ویژگی برای حس‌سازی برمی‌شمارد: در هویت فرد ریشه دارد، بازنگرانه است، محیط را در همان حال که تفسیر می‌کند تغییر می‌دهد، اجتماعی است، پیوسته جریان دارد، بر نشانه‌های استخراج‌شده تمرکز می‌کند و به باورپذیری بیش از دقت نظر دارد. در بحران‌ها، وقتی قالب‌های معنایی پیشین از کار می‌افتند، حس‌سازی به مسئلهٔ حیاتی سازمان تبدیل می‌شود. اهمیت آن برای رسانه در تحلیل تحریریه‌ها در بحران، پوشش رویدادهای مبهم و مدیریت ارتباطات بحران است. نقدهای اصلی به آن، تأکید افراطی بر بازنگری، کم‌توجهی به قدرت و عاطفه، ابهام مفهومی و دشواری آزمون تجربی مربوط می‌شود.",
        definition="حس‌سازی سازمانی، فرایند پیوستهٔ ساختن معنای باورپذیر از موقعیت‌های مبهم از راه روایت، نشانه‌گزینی و تعامل اجتماعی است تا اعضای سازمان بتوانند عمل کنند.",
        main_problem="وقتی رویدادی مبهم یا بحرانی رخ می‌دهد و قالب‌های معنایی پیشین از کار می‌افتند، اعضای سازمان چگونه معنایی می‌سازند که به آن باور داشته باشند و بر پایهٔ آن عمل کنند.",
        mechanism="افراد نشانه‌هایی را از محیط برمی‌کشند، با تجربهٔ گذشته و هویت سازمانی مقایسه می‌کنند، در گفت‌وگو روایت‌های رقیب را می‌آزمایند و روایتی باورپذیر می‌سازند که مبنای کنش می‌شود؛ همان کنش، محیط را تغییر می‌دهد و چرخه از نو آغاز می‌شود. در بحران، شکست در ساخت روایت مشترک می‌تواند به فروپاشی هماهنگی بیانجامد.",
        assumptions=[
            "واقعیت سازمانی در جریان تفسیر فعال اعضا ساخته می‌شود.",
            "معنا از راه روایت و گفت‌وگو شکل می‌گیرد.",
            "هویت سازمانی، چارچوب اصلی تفسیر رویدادهاست.",
            "باورپذیری روایت، بیش از دقت کامل، مبنای کنش است.",
            "حس‌سازی پیوسته و بازنگرانه است و در بحران به مسئلهٔ حیاتی تبدیل می‌شود.",
        ],
        principles=[
            "حس‌سازی در هویت فرد و سازمان ریشه دارد.",
            "تفسیر رویدادها بازنگرانه و پس از وقوع آغاز می‌شود.",
            "کنش، محیط را تغییر می‌دهد و تفسیر تازه می‌سازد.",
            "حس‌سازی اجتماعی و مبتنی بر گفت‌وگوست.",
            "نشانه‌های استخراج‌شده، کانون توجه‌اند.",
            "روایت باورپذیر مبنای عمل است، حتی اگر کامل نباشد.",
        ],
        critiques=[
            "تأکید بر بازنگری، نقش پیش‌بینی و برنامه‌ریزی را کم‌رنگ می‌کند.",
            "قدرت، منافع و عاطفه در تحلیل جای کافی ندارند.",
            "مفاهیم نظریه مبهم و سنجش آنها دشوار است.",
            "آزمون تجربی نظام‌مند روایت‌های رقیب محدود مانده است.",
            "خطر تقلیل بحران به مسئلهٔ ارتباطی وجود دارد.",
        ],
        critique_text="منتقدان می‌گویند حس‌سازی توضیحی غنی از معناسازی ارائه می‌دهد اما کمتر روشن می‌کند که چه کسی قدرت تعریف موقعیت را در دست دارد و چرا برخی روایت‌ها بر روایت‌های دیگر چیره می‌شوند. با این حال، تأکید آن بر روایت، ابهام و باورپذیری، چارچوبی پرکاربرد برای تحلیل بحران در سازمان‌های رسانه‌ای ساخته است.",
        applications=[
            "تحلیل تصمیم‌گیری تحریریه در بحران‌های خبری.",
            "مدیریت ارتباطات بحران در سازمان‌ها.",
            "پژوهش تغییر سازمانی و ادغام رسانه‌ها.",
            "تحلیل روایت‌سازی در پوشش رویدادهای مبهم.",
            "آموزش رهبری و ارتباطات بحران.",
        ],
        example_text="وقتی یک خبرگزاری با انتشار خبر نادرست روبه‌رو می‌شود، اعضای تحریریه در گفت‌وگوهای پیاپی روایتی از آنچه رخ داده می‌سازند: خطا کجا بود، چه کسی مسئول است، پاسخ مناسب چیست. روایتی که باورپذیرتر باشد، مبنای عمل قرار می‌گیرد؛ حتی اگر همهٔ جزئیات روشن نباشد. این همان حس‌سازی در شرایط ابهام است.",
        evolution="ریشهٔ نظریه به پژوهش‌های وایک دربارهٔ سازمان‌های حادثه‌خیز و فاجعهٔ آتش‌سوزی مان‌گلچ در سال ۱۹۹۳ بازمی‌گردد. کتاب سال ۱۹۹۵ هفت ویژگی حس‌سازی را صورت‌بندی کرد و بعدها این چارچوب به مطالعات بحران، سلامت، فناوری و رسانه راه یافت.",
        key_concepts=["حس‌سازی", "باورپذیری", "نشانه‌های استخراج‌شده", "روایت سازمانی", "ابهام", "فروپاشی حس‌سازی", "هویت سازمانی"],
        theorists="کارل وایک، بنیان‌گذار نظریهٔ حس‌سازی سازمانی.",
        theorists_text="این نظریه در سنت تفسیری سازمان و پژوهش بحران شکل گرفت و با مطالعات روایت و ارتباطات بحران پیوند خورد.",
        model="مدل چرخه‌ای: نشانه‌گزینی از محیط، مقایسه با تجربه و هویت، گفت‌وگوی اجتماعی و ساخت روایت باورپذیر، کنش بر پایهٔ روایت، تغییر محیط و آغاز چرخهٔ تازه؛ در بحران، فروپاشی روایت مشترک خطر اصلی است.",
        studies=[
            "کتاب سال ۱۹۹۵ هفت ویژگی حس‌سازی را با نمونه‌های سازمانی صورت‌بندی کرد.",
            "پژوهش فاجعهٔ مان‌گلچ، فروپاشی حس‌سازی در بحران را تحلیل کرد.",
            "مطالعات بحران، چارچوب را به ارتباطات بحران و تصمیم‌گیری گستردند.",
            "پژوهش رسانه، حس‌سازی تحریریه در تغییرات فناورانه را بررسی کرده است.",
        ],
    ),
    "MC-729": dict(
        year=2008,
        summary="مدیریت راهبردی در رسانه، حوزه‌ای است که لوسی کونگ در کتاب سال ۲۰۰۸ با همین نام صورت‌بندی کرد و در ویرایش دوم سال ۲۰۱۷ بسط داد. ادعای مرکزی این است که نظریه‌های عمومی مدیریت راهبردی، که در محیط‌های خطی و پایدار شکل گرفته‌اند، پاسخگوی ویژگی‌های صنایع رسانه‌ای نیستند. رسانه‌ها چهار ویژگی متمایز دارند: محصول آنها نمادین و تجربه‌محور است و ارزشش به معنا وابسته است؛ بازار آنها دومرحله‌ای است و درآمد از مخاطب و تبلیغ‌دهنده می‌آید؛ نیروی انسانی خلاق، منبع اصلی ارزش است؛ و تحول فناورانه، غیرخطی و پیوسته است. بر این پایه، کونگ مفاهیم راهبردی مانند موقعیت‌یابی، منابع، توانمندی‌های پویا و نوآوری را برای رسانه بازخوانی می‌کند و بر رهبری خلاق، هویت برند و آمادگی تغییر تأکید می‌کند. این چارچوب برای تحلیل گذار رسانه‌های سنتی به دیجیتال، ادغام رسانه‌ای و راهبرد رسانه‌های بخش عمومی به کار می‌رود. نقدهای اصلی به آن، جهت‌گیری حرفه‌ای و نمونه‌محور، شواهد تجربی محدود و کم‌توجهی به شرایط کشورهای در حال توسعه مربوط می‌شود.",
        definition="مدیریت راهبردی در رسانه، چارچوبی است که نظریه‌های عمومی راهبرد را برای ویژگی‌های خاص رسانه بازخوانی می‌کند: محصول نمادین، بازار دومرحله‌ای، نیروی خلاق و تحول فناورانهٔ غیرخطی.",
        main_problem="چرا نظریه‌های عمومی راهبرد در رسانه‌ها به‌سختی به کار می‌روند و سازمان رسانه‌ای چگونه می‌تواند در محیطی با محصول نمادین و تحول فناورانهٔ سریع، مزیت پایدار بسازد.",
        mechanism="چارچوب، دو بازار را از هم تفکیک می‌کند: بازار مخاطب و بازار تبلیغ‌دهنده. ارزش در تولید نمادین ساخته می‌شود و به خلاقیت نیروی انسانی وابسته است. راهبرد با انتخاب دامنه، تمرکز بر منابع راهبردی مانند برند و قابلیت تحریریه، و توانمندی پویا برای بازآرایی مدل کسب‌وکار در برابر تغییر فناورانه ساخته می‌شود.",
        assumptions=[
            "صنایع رسانه‌ای ویژگی‌های متمایزی دارند که نظریهٔ عمومی راهبرد را ناکافی می‌کند.",
            "محصول رسانه‌ای نمادین است و ارزش آن به معنا و اعتماد وابسته است.",
            "درآمد رسانه از دو بازار مخاطب و تبلیغ‌دهنده می‌آید.",
            "خلاقیت نیروی انسانی، منبع اصلی مزیت است.",
            "تحول فناورانه، غیرخطی است و توانمندی پویا را ضروری می‌کند.",
        ],
        principles=[
            "راهبرد عمومی را باید برای ویژگی‌های رسانه بازخوانی کرد.",
            "دو بازار مخاطب و تبلیغ‌دهنده باید هم‌زمان مدیریت شوند.",
            "برند و اعتماد، منابع راهبردی کلیدی‌اند.",
            "رهبری خلاق، شرط اجرای راهبرد در تحریریه است.",
            "توانمندی پویا برای بازآرایی مدل کسب‌وکار ضروری است.",
            "هویت سازمانی و ارزش عمومی، بخشی از تحلیل راهبردی‌اند.",
        ],
        critiques=[
            "چارچوب بیشتر حرفه‌ای و نمونه‌محور است تا آزمون‌پذیر.",
            "شواهد تجربی نظام‌مند دربارهٔ اثربخشی آن محدود است.",
            "کشورهای در حال توسعه و رسانه‌های کوچک کم‌پوشش می‌مانند.",
            "خطر تقلیل راهبرد به مجموعه‌ای از بهترین رویه‌ها وجود دارد.",
            "نقش مقررات و سیاست عمومی رسانه کم‌رنگ می‌شود.",
        ],
        critique_text="منتقدان می‌گویند کتاب بیش از آنکه نظریه‌ای آزمون‌پذیر عرضه کند، راهنمایی حرفه‌ای برای مدیران رسانه است؛ با این حال، تشخیص چهار ویژگی متمایز رسانه و بازخوانی مفاهیم راهبردی بر پایهٔ آنها، سهم مهمی در تثبیت حوزهٔ مدیریت رسانه داشته است.",
        applications=[
            "تحلیل گذار رسانه‌های سنتی به دیجیتال.",
            "طراحی راهبرد رسانه‌های بخش عمومی.",
            "ارزیابی ادغام و خرید در صنعت رسانه.",
            "آموزش مدیریت رسانه و رهبری تحریریه.",
            "پژوهش مدل‌های کسب‌وکار خبری.",
        ],
        example_text="یک روزنامهٔ سنتی که به دیجیتال گذار می‌کند، باید هم‌زمان بازار مخاطب و بازار تبلیغ‌دهنده را بازطراحی کند، برند اعتماد را حفظ کند، تحریریه را برای مهارت‌های تازه توانمند سازد و مدل درآمدی تازه بیازماید؛ چارچوب مدیریت راهبردی در رسانه، این چهار جبهه را در یک تحلیل واحد به هم گره می‌زند.",
        evolution="ویرایش نخست کتاب در سال ۲۰۰۸ منتشر شد و ویرایش دوم در سال ۲۰۱۷ با توجه به تحول پلتفرم‌ها و هوش مصنوعی به‌روز شد. این اثر به متن مرجع دوره‌های مدیریت رسانه تبدیل شد و پژوهش‌های بعدی، چارچوب را با تحلیل مدل کسب‌وکار و نوآوری رسانه‌ای گستردند.",
        key_concepts=["محصول نمادین", "بازار دومرحله‌ای", "نیروی خلاق", "توانمندی پویا", "رهبری خلاق", "هویت برند", "گذار دیجیتال"],
        theorists="لوسی کونگ، پژوهشگر مدیریت رسانه و نویسندهٔ کتاب مرجع مدیریت راهبردی در رسانه.",
        theorists_text="این حوزه در تقاطع مدیریت راهبردی، اقتصاد رسانه و مطالعات سازمانی رسانه شکل گرفت.",
        model="مدل چهارویژگی: محصول نمادین، بازار دومرحله‌ای، نیروی خلاق و تحول فناورانهٔ غیرخطی؛ راهبرد با بازخوانی موقعیت‌یابی، منابع و توانمندی پویا برای این چهار ویژگی ساخته می‌شود.",
        studies=[
            "ویرایش نخست کتاب در سال ۲۰۰۸ چارچوب رسانه‌ای راهبرد را تثبیت کرد.",
            "ویرایش دوم در سال ۲۰۱۷ آن را برای محیط پلتفرمی بازخوانی کرد.",
            "پژوهش‌های مدل کسب‌وکار خبری، چارچوب را آزمودند و بسط دادند.",
            "مطالعات رسانهٔ عمومی، کاربرد آن را در ارزش عمومی بررسی کردند.",
        ],
    ),
    "MC-731": dict(
        year=2015,
        summary="عمومیت‌های عاطفی، مفهومی است که زیزی پاپاچاریسی در کتاب سال ۲۰۱۵ صورت‌بندی کرد و می‌گوید در بسترهای شبکه‌ای، اجتماعات انسانی بیش از آنکه حول استدلال‌های عقلانی گرد آیند، از راه هم‌طنین‌شدن عواطف، خشم‌ها و امیدهای مشترک شکل می‌گیرند. عاطفه، مادهٔ چسبندهٔ گفت‌وگوی شبکه‌ای است: کاربران با روایت‌گویی، هشتگ‌زنی و بازنشر احساس، عمومیتی می‌سازند که مرزهای آن با هر موج عاطفی جابه‌جا می‌شود. پاپاچاریسی با مطالعهٔ جنبش‌های اعتراضی در توییتر نشان داد که این عمومیت‌ها هم‌زمان امکانی برای همبستگی و مشارکت‌اند و هم شکننده و گذرا. او مفهوم ساختارهای احساس را از سنت فرهنگی وام می‌گیرد و آن را به جریان‌های خبری عاطفی در پلتفرم‌ها پیوند می‌زند. اهمیت آن در تحلیل جنبش‌های اجتماعی دیجیتال، رسانهٔ شهروندی و سیاست عاطفی است. نقدها به تمرکز بر نمونه‌های غربی، دشواری سنجش عاطفه، خطر بیش‌برآورد ظرفیت رهایی‌بخش پلتفرم‌ها و کم‌توجهی به قطب‌بندی و دستکاری عاطفی مربوط می‌شود.",
        definition="عمومیت‌های عاطفی، اجتماعاتی شبکه‌ای‌اند که از راه هم‌طنین‌شدن عاطفه و روایت‌گویی مشترک در پلتفرم‌ها شکل می‌گیرند و حول یک مسئله یا رویداد به‌طور موقت گرد هم می‌آیند.",
        main_problem="اگر عمومیت در فضای عمومی کلاسیک از راه استدلال عقلانی ساخته می‌شد، در پلتفرم‌های شبکه‌ای چه چیزی مردم را حول یک مسئله گرد هم می‌آورد و این گردهم‌آمدن چه محدودیت‌ها و امکاناتی دارد.",
        mechanism="کاربران با هشتگ، روایت شخصی، بازنشر و ابراز احساس، جریانی از خبر و عاطفه می‌سازند؛ هم‌طنینی عاطفی، پیوند موقت میان غریبه‌ها برقرار می‌کند و مرز عمومیت را با هر موج تازه جابه‌جا می‌کند. این عمومیت‌ها همبستگی می‌سازند اما شکننده و وابسته به لحظه‌اند.",
        assumptions=[
            "عاطفه، سازوکار اصلی پیوند در پلتفرم‌های شبکه‌ای است.",
            "روایت‌گویی شخصی، مادهٔ خام گفت‌وگوی سیاسی شبکه‌ای است.",
            "عمومیت‌ها موقت و جابه‌جاشونده‌اند.",
            "قابلیت‌های فنی پلتفرم، شکل عاطفی گفت‌وگو را قالب می‌زنند.",
            "تجربهٔ عاطفی جمعی می‌تواند به مشارکت سیاسی بیانجامد.",
        ],
        principles=[
            "عاطفه را باید بخشی از ساختار ارتباط سیاسی دانست و نه نقص آن.",
            "هشتگ و بازنشر، ابزارهای ساختن عمومیت عاطفی‌اند.",
            "هم‌طنینی عاطفی، پیوندی موقت و شکننده می‌سازد.",
            "ساختارهای احساس، تجربهٔ جمعی را پیش از بیان کامل شکل می‌دهند.",
            "پلتفرم، هم امکان مشارکت و هم محدودیت آن را می‌سازد.",
            "تحلیل عمومیت باید همبستگی و هم شکنندگی را با هم ببیند.",
        ],
        critiques=[
            "نمونه‌های اصلی غربی‌اند و تعمیم آن محدود است.",
            "سنجش عاطفه از داده‌های متنی دشوار و ناپایدار است.",
            "ظرفیت رهایی‌بخش پلتفرم‌ها بیش از اندازه برجسته می‌شود.",
            "قطب‌بندی، دستکاری و تبلیغات عاطفی کم‌بررسی می‌مانند.",
            "مرز میان عمومیت عاطفی و تودهٔ هیجانی مبهم است.",
        ],
        critique_text="منتقدان می‌گویند عمومیت عاطفی چارچوبی غنی برای فهم همبستگی شبکه‌ای است، اما می‌تواند همبستگی مترقی و قطب‌بندی مخرب را یکسان توصیف کند و از سنجش تجربی عاطفه فاصله بگیرد. با این حال، این مفهوم سنت فضای عمومی را از استدلال محض به تجربهٔ عاطفی گسترش داده است.",
        applications=[
            "تحلیل جنبش‌های اجتماعی دیجیتال و رسانهٔ شهروندی.",
            "پژوهش گفت‌وگوی سیاسی در پلتفرم‌ها.",
            "تحلیل کمپین‌های هشتگی و همبستگی آنلاین.",
            "مطالعهٔ سیاست عاطفی در بحران‌ها.",
            "آموزش سواد رسانه‌ای برای فهم دستکاری عاطفی.",
        ],
        example_text="در یک جنبش اعتراضی، هشتگی که روایت‌های شخصی و تصاویر احساسی را گرد هم می‌آورد، عمومیتی موقت می‌سازد که با هر موج تازه گسترده یا از هم می‌پاشد؛ کاربران ممکن است بدون شناخت یکدیگر، از راه خشم یا امید مشترک به کنش هماهنگ برسند. این همان سازوکاری است که عمومیت عاطفی توصیف می‌کند.",
        evolution="ریشهٔ مفهومی به بحث ساختارهای احساس در سنت مطالعات فرهنگی بازمی‌گردد. پاپاچاریسی در سال ۲۰۱۵ با مطالعهٔ جنبش‌های توییتری، عمومیت عاطفی را صورت‌بندی کرد و بعدها پژوهش‌های پلتفرم، آن را با تحلیل داده و نقد قطب‌بندی گستردند.",
        key_concepts=["عمومیت عاطفی", "هم‌طنینی عاطفی", "ساختارهای احساس", "هشتگ", "جریان خبری عاطفی", "عمومیت شبکه‌ای"],
        theorists="زیزی پاپاچاریسی، صورت‌بند نظریهٔ عمومیت‌های عاطفی؛ و ریموند ویلیامز، صاحب مفهوم ساختارهای احساس.",
        theorists_text="این نظریه در تقاطع مطالعات فضای عمومی، نظریهٔ عاطفه و پژوهش پلتفرم شکل گرفت.",
        model="مدل سه‌لایه: قابلیت فنی پلتفرم، روایت‌گویی و هشتگ‌زنی کاربران، و هم‌طنینی عاطفی؛ پیوند این سه، عمومیتی موقت و شکننده می‌سازد که با موج‌های عاطفی گسترده یا از هم می‌پاشد.",
        studies=[
            "کتاب سال ۲۰۱۵ عمومیت عاطفی را با مطالعهٔ جنبش‌های توییتری صورت‌بندی کرد.",
            "پژوهش‌های بعدی، نقش عاطفه در گفت‌وگوی سیاسی پلتفرم را آزمودند.",
            "مطالعات داده‌های کلان، الگوهای هشتگ و همبستگی آنلاین را بررسی کردند.",
            "نقدهای پلتفرمی، مرز عمومیت عاطفی و قطب‌بندی را تحلیل کردند.",
        ],
    ),
}

NAME_FIX = {}

YEAR_FIX = {}


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


REQUIRED_SECTIONS = ["summary", "definition", "main_problem", "mechanism", "assumptions",
                     "principles", "critiques", "applications", "evolution", "key_concepts",
                     "theorists", "model", "studies"]
WORD_KEYS = ["summary", "definition", "main_problem", "mechanism", "critiques",
             "applications", "evolution", "key_concepts", "principles", "studies", "assumptions"]


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

        if code in YEAR_FIX:
            cur.execute("""INSERT INTO kb_audit_log (entity_code,action,detail,source,created_at)
                VALUES (%s,'DOC_FIX',%s,%s,%s)""",
                        (code, json.dumps({"fix": YEAR_FIX[code]}, ensure_ascii=False), STAMP, NOW))

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
                                       "verified": n_verified, "batch": 128}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH128 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
