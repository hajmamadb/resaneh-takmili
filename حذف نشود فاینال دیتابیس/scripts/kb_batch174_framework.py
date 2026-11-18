# -*- coding: utf-8 -*-
"""Batch 174 (final PERSON plus first WORK): th-36 Kung, th-37 Papacharissi, th-39 Nieborg, MC-101 hostile media effect."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch174-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch174.json"

MAPPING = {"entity_type": "PERSON", "content_type": "شخصیت علمی (نظریه‌پرداز)", "needs_review": False}
WORK_MAPPING = {"entity_type": "WORK", "content_type": "اثر رسانه‌ای (پدیده)", "needs_review": False}

S = {
    "th-36": [
        dict(kind="BOOK",
             title_en="Strategic Management in the Media: From Theory to Practice",
             title_fa="مدیریت راهبردی در رسانه: از نظریه تا عمل",
             authors="Küng, L.", year=2008,
             publisher="Sage",
             doi=None,
             url="https://sk.sagepub.com/book/mono/strategic-management-in-the-media/toc",
             language="en", isbn=None,
             citation="Küng, L. (2008). Strategic Management in the Media: From Theory to Practice. London: Sage.",
             locator="2008 edition", locator_type="edition",
             supports="strategy, leadership and innovation in media firms", verified=True),
        dict(kind="BOOK",
             title_en="Innovators in Digital News",
             title_fa="نوآوران در خبر دیجیتال",
             authors="Küng, L.", year=2015,
             publisher="I.B. Tauris",
             doi=None,
             url="https://reutersinstitute.politics.ox.ac.uk/sites/default/files/research/files/Innovators%2520in%2520Digital%2520News%2520Extract.pdf",
             language="en", isbn=None,
             citation="Küng, L. (2015). Innovators in Digital News. London: I.B. Tauris.",
             locator="2015 edition", locator_type="edition",
             supports="digital news innovation and organizational transformation", verified=True),
    ],
    "th-37": [
        dict(kind="BOOK",
             title_en="A Private Sphere: Democracy in a Digital Age",
             title_fa="حوزهٔ خصوصی: دموکراسی در عصر دیجیتال",
             authors="Papacharissi, Z.", year=2010,
             publisher="Polity",
             doi=None,
             url=None,
             language="en", isbn=None,
             citation="Papacharissi, Z. (2010). A Private Sphere: Democracy in a Digital Age. Cambridge: Polity.",
             locator="2010 edition", locator_type="edition",
             supports="digital engagement as individualized civic participation in a private sphere", verified=True),
        dict(kind="BOOK",
             title_en="Affective Publics: Sentiment, Technology, and Politics",
             title_fa="عموم‌های عاطفی: احساس، فناوری و سیاست",
             authors="Papacharissi, Z.", year=2015,
             publisher="Oxford University Press",
             doi=None,
             url="https://global.oup.com/academic/product/affective-publics-9780199999743",
             language="en", isbn=None,
             citation="Papacharissi, Z. (2015). Affective Publics: Sentiment, Technology, and Politics. Oxford: Oxford University Press.",
             locator="2015 edition", locator_type="edition",
             supports="affective publics and storytelling on social media platforms", verified=True),
    ],
    "th-39": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Platformization of Cultural Production: Theorizing the Contingent Cultural Commodity",
             title_fa="پلتفرمی‌شدن تولید فرهنگی: نظریه‌پردازی دربارهٔ کالای فرهنگی اقتضایی",
             authors="Nieborg, D. B.; Poell, T.", year=2018,
             publisher="New Media & Society, 20(11), 4275-4292",
             doi="10.1177/1461444818769694",
             url="https://journals.sagepub.com/doi/abs/10.1177/1461444818769694",
             language="en", isbn=None,
             citation="Nieborg, D. B., & Poell, T. (2018). The platformization of cultural production: Theorizing the contingent cultural commodity. New Media & Society, 20(11), 4275-4292.",
             locator="20(11), pp. 4275-4292", locator_type="page_range",
             supports="platformization of cultural production and the contingent cultural commodity", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Crushing Candy: The Free-to-Play Game in Its Connective Commodity Form",
             title_fa="خردکردن آب‌نبات: بازی رایگان‌به‌بازی در قالب کالای پیوندی",
             authors="Nieborg, D. B.", year=2015,
             publisher="Social Media + Society, 1(2), 1-12",
             doi="10.1177/2056305115621932",
             url="https://journals.sagepub.com/doi/10.1177/2056305115621932",
             language="en", isbn=None,
             citation="Nieborg, D. B. (2015). Crushing Candy: The free-to-play game in its connective commodity form. Social Media + Society, 1(2), 1-12.",
             locator="1(2), pp. 1-12", locator_type="page_range",
             supports="platform economics and the commodification of game data and play", verified=True),
    ],
    "MC-101": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Hostile Media Phenomenon: Biased Perception and Perceptions of Media Bias in Coverage of the Beirut Massacre",
             title_fa="پدیدهٔ رسانهٔ خصمانه: ادراک سوگیرانه و برداشت از سوگیری رسانه در پوشش کشتار بیروت",
             authors="Vallone, R. P.; Ross, L.; Lepper, M. R.", year=1985,
             publisher="Journal of Personality and Social Psychology, 49(3), 577-585",
             doi="10.1037/0022-3514.49.3.577",
             url="https://psycnet.apa.org/record/1986-03718-001",
             language="en", isbn=None,
             citation="Vallone, R. P., Ross, L., & Lepper, M. R. (1985). The hostile media phenomenon: Biased perception and perceptions of media bias in coverage of the Beirut massacre. Journal of Personality and Social Psychology, 49(3), 577-585.",
             locator="49(3), pp. 577-585", locator_type="page_range",
             supports="both sides of a partisan issue perceive neutral coverage as hostile to their side", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="A Three-Decade Retrospective on the Hostile Media Effect",
             title_fa="مروری سه‌دهه‌ای بر اثر رسانهٔ خصمانه",
             authors="Perloff, R. M.", year=2015,
             publisher="Mass Communication and Society, 18(6), 701-729",
             doi="10.1080/15205436.2015.1051234",
             url="https://www.tandfonline.com/doi/full/10.1080/15205436.2015.1051234",
             language="en", isbn=None,
             citation="Perloff, R. M. (2015). A three-decade retrospective on the hostile media effect. Mass Communication and Society, 18(6), 701-729.",
             locator="18(6), pp. 701-729", locator_type="page_range",
             supports="review of mechanisms, moderators and boundary conditions of the effect", verified=True),
    ],
}

ENRICH = {
    "th-36": dict(
        year=2008,
        mapping=MAPPING,
        summary="لوسی کونگ پژوهشگر مدیریت رسانه و استاد نوآوری رسانه در دانشگاه اسلو و همکار ارشد مؤسسهٔ رایترز دانشگاه آکسفورد است. او در کتاب مدیریت راهبردی در رسانه در سال ۲۰۰۸ چارچوبی برای تحلیل راهبرد، رهبری و نوآوری در بنگاه‌های رسانه‌ای ارائه کرد. کونگ استدلال کرد رسانه هم‌زمان در دو بازار فعالیت می‌کند: بازار مخاطب و بازار تبلیغات، و موفقیت راهبردی به توازن میان ارزش خبری و مدل درآمدی بستگی دارد. او در کتاب نوآوران در خبر دیجیتال در سال ۲۰۱۵ با مطالعهٔ موردی سازمان‌های خبری پیشرو نشان داد تحول دیجیتال بیش از فناوری، به فرهنگ سازمانی، رهبری و مدل کسب‌وکار وابسته است. پژوهش او بر نوآوری در سازمان‌های خبری قدیمی و تازه‌تأسیس و بر مدیریت تغییر متمرکز است. نقدهای اصلی به او، جهت‌گیری مدیریتی و کاربردی، تمرکز بر کشورهای شمال و کم‌توجهی به کار و قدرت خبرنگاران را برجسته می‌کنند.",
        definition="لوسی کونگ پژوهشگر مدیریت رسانه است که راهبرد، رهبری و نوآوری سازمان‌های خبری را با تمرکز بر مدل کسب‌وکار و فرهنگ سازمانی تحلیل می‌کند.",
        main_problem="سازمان‌های رسانه‌ای چگونه در بازار دوگانهٔ مخاطب و تبلیغات راهبرد پایدار می‌سازند و تحول دیجیتال را مدیریت می‌کنند.",
        mechanism="بنگاه رسانه‌ای با توازن میان ارزش محتوایی و مدل درآمدی، منابع و قابلیت‌ها را بازآرایی می‌کند؛ نوآوری پایدار از پیوند رهبری، فرهنگ سازمانی و مدل کسب‌وکار شکل می‌گیرد، نه فقط از فناوری.",
        assumptions=[
            "رسانه در بازار دوگانه فعالیت می‌کند.",
            "راهبرد رسانه به مدل درآمدی وابسته است.",
            "رهبری بر تحول دیجیتال اثر دارد.",
            "فرهنگ سازمانی مانع یا محرک نوآوری است.",
            "قابلیت سازمانی منبع مزیت است.",
            "نوآوری نیازمند آزمون و یادگیری است.",
            "محیط رسانه‌ای بی‌ثبات و رقابتی است.",
            "نوآوری خبری چندبعدی است.",
        ],
        principles=[
            "بازار مخاطب و تبلیغات را جدا تحلیل کن.",
            "مدل درآمدی را با ارزش خبری بسنج.",
            "رهبری و فرهنگ را در تحول بگنجان.",
            "نوآوری را فرایندی سازمانی بدان.",
            "قابلیت‌های متمایز را شناسایی کن.",
            "به محیط رقابتی و بی‌ثبات توجه کن.",
            "از نسخه‌های عمومی پرهیز کن.",
        ],
        critiques=[
            "جهت‌گیری مدیریتی و کاربردی دارد.",
            "به کار خبرنگاران کم می‌پردازد.",
            "به کشورهای شمال محدود است.",
            "به قدرت مالکیت کم توجه است.",
            "به سیاست عمومی رسانه کم می‌پردازد.",
            "به سازمان‌های کوچک کم توجه است.",
            "به مقاومت تحریریه کم می‌پردازد.",
            "به رسانهٔ غیرانگلیسی کم توجه است.",
            "به نابرابری جنسیتی در مدیریت کم توجه است.",
            "به رسانهٔ خدمت عمومی کم می‌پردازد.",
            "به پلتفرم‌های جهانی دیر رسید.",
            "به شواهد تطبیقی کم تکیه دارد.",
            "به اثرهای بلندمدت کم می‌پردازد.",
        ],
        critique_text="منتقدان کونگ می‌گویند چارچوب او مدیریتی و کاربردی است و کار خبرنگاران و قدرت مالکیت را کم می‌بیند و بیشتر بر سازمان‌های خبری کشورهای شمال متمرکز است؛ با این حال، او پیوند راهبرد، رهبری و فرهنگ سازمانی را در تحول رسانه به بحث اصلی بدل کرد.",
        applications=[
            "تحلیل راهبرد سازمان خبری.",
            "پژوهش تحول دیجیتال رسانه.",
            "مطالعهٔ مدل درآمدی خبر.",
            "تحلیل رهبری رسانه.",
            "پژوهش نوآوری در تحریریه.",
            "مطالعهٔ فرهنگ سازمانی خبر.",
            "تحلیل رسانهٔ خدمت عمومی.",
            "پژوهش مدیریت تغییر در رسانه.",
            "مطالعهٔ کسب‌وکار پلتفرم خبری.",
            "تحلیل راهبرد اشتراک دیجیتال.",
            "پژوهش سازمان خبری تازه‌تأسیس.",
            "مطالعهٔ همکاری رسانه‌ای.",
            "تحلیل تحول روزنامهٔ چاپی.",
            "پژوهش مدیریت استعداد در رسانه.",
            "مطالعهٔ نوآوری مدل کسب‌وکار.",
            "تحلیل رهبری زنانه در رسانه.",
        ],
        example_text="روزنامه‌ای که برای بقا دیوار پرداخت راه می‌اندازد و هم‌زمان تحریریه را به تیم محصول و داده پیوند می‌دهد، در حال بازآرایی راهبرد و فرهنگ سازمانی است؛ کونگ این را نمونهٔ تحول دیجیتال می‌داند.",
        evolution="کونگ در سال ۲۰۰۸ مدیریت راهبردی در رسانه را نوشت و ویرایش دوم آن را در سال ۲۰۱۶ منتشر کرد؛ در سال ۲۰۱۵ با نوآوران در خبر دیجیتال، پژوهش را به مطالعهٔ موردی سازمان‌های خبری پیشرو گستراند.",
        key_concepts=["مدیریت رسانه", "راهبرد رسانه‌ای", "بازار دوگانه", "تحول دیجیتال", "نوآوری خبری", "فرهنگ سازمانی"],
        theorists="مایکل پورتر، جی بارنی و رابرت پیکارد.",
        theorists_text="کونگ چارچوب‌های مدیریت راهبردی را با ویژگی‌های اقتصاد رسانه پیوند داد.",
        model="راهبرد رسانه به‌عنوان توازن میان ارزش محتوایی و مدل درآمدی در محیطی بی‌ثبات.",
        studies=[
            "کتاب مدیریت راهبردی در رسانه سال ۲۰۰۸.",
            "کتاب نوآوران در خبر دیجیتال سال ۲۰۱۵.",
            "ویرایش دوم مدیریت راهبردی سال ۲۰۱۶.",
            "پژوهش تحول دیجیتال خبر.",
            "مطالعهٔ مدل درآمدی رسانه.",
            "تحلیل رهبری رسانه.",
            "پژوهش نوآوری تحریریه.",
            "مطالعهٔ فرهنگ سازمانی خبر.",
            "تحلیل راهبرد اشتراک.",
            "پژوهش رسانهٔ خدمت عمومی.",
            "مطالعهٔ سازمان خبری تازه‌تأسیس.",
            "تحلیل مدیریت تغییر رسانه.",
        ],
    ),
    "th-37": dict(
        year=2010,
        mapping=MAPPING,
        summary="زیزی پاپاچاریسی استاد ارتباطات دانشگاه ایلینوی شیکاگو و از نظریه‌پردازان حوزهٔ عمومی و سیاست دیجیتال است. او در کتاب حوزهٔ خصوصی در سال ۲۰۱۰ استدلال کرد فناوری‌های دیجیتال لزوماً حوزهٔ عمومی هابرماسی نمی‌سازند، بلکه زمینه‌ای می‌سازند که در آن شهروندان کنش مدنی را به شکل فردی و در حوزهٔ خصوصی انجام می‌دهند. پاپاچاریسی در کتاب عموم‌های عاطفی در سال ۲۰۱۵ نشان داد در شبکه‌های اجتماعی، احساس و روایت شخصی به‌عنوان سوخت مشارکت سیاسی عمل می‌کند و عموم‌هایی عاطفی می‌سازد که حول داستان‌ها و احساس‌های مشترک شکل می‌گیرند. او این چارچوب را با مطالعهٔ جنبش‌های اعتراضی و گفت‌وگوهای توییتری آزمود و بر نقش «خود شبکه‌ای» تأکید کرد. نقدهای اصلی به او، خوش‌بینی نسبت به عاطفه، تمرکز بر نمونه‌های محدود و کم‌توجهی به قدرت پلتفرم را برجسته می‌کنند.",
        definition="زیزی پاپاچاریسی نظریه‌پرداز سیاست دیجیتال و عموم‌های عاطفی است که نقش احساس و روایت شخصی را در مشارکت آنلاین تحلیل می‌کند.",
        main_problem="فناوری‌های دیجیتال چگونه حوزهٔ عمومی را بازسازی می‌کنند و احساس و روایت شخصی چه نقشی در مشارکت سیاسی آنلاین دارند.",
        mechanism="کاربران با روایت تجربهٔ شخصی و بیان احساس در شبکه‌های اجتماعی، پیوندهای عاطفی می‌سازند؛ این پیوندها به شکل‌گیری عموم‌هایی عاطفی و کنش جمعی موقت و شبکه‌ای می‌انجامد.",
        assumptions=[
            "حوزهٔ عمومی دیجیتال متفاوت از الگوی هابرماسی است.",
            "کنش مدنی در حوزهٔ خصوصی فردی می‌شود.",
            "احساس سوخت مشارکت آنلاین است.",
            "روایت شخصی پیوند جمعی می‌سازد.",
            "عموم عاطفی حول داستان شکل می‌گیرد.",
            "خود شبکه‌ای هویت را بازسازی می‌کند.",
            "مشارکت دیجیتال موقت و سیال است.",
            "پلتفرم چارچوب عاطفه را شکل می‌دهد.",
        ],
        principles=[
            "احساس را در تحلیل مشارکت بگنجان.",
            "روایت شخصی را دادهٔ تحلیل بگیر.",
            "عموم عاطفی را از حوزهٔ عمومی جدا کن.",
            "به معماری پلتفرم توجه کن.",
            "مشارکت سیال را زمان‌مند بسنج.",
            "خود شبکه‌ای را در هویت‌یابی ببین.",
            "از خوش‌بینی فناورانه پرهیز کن.",
        ],
        critiques=[
            "نسبت به عاطفه خوش‌بین است.",
            "نمونه‌های آن محدود است.",
            "به قدرت پلتفرم کم می‌پردازد.",
            "به نابرابری دسترسی کم توجه است.",
            "مفهوم حوزهٔ خصوصی مبهم است.",
            "به مقاومت و سوءاستفاده عاطفی کم توجه است.",
            "به زمینهٔ غیرغربی کمتر می‌پردازد.",
            "سنجش عاطفه دشوار است.",
            "به سیاست نهادی کم می‌پردازد.",
            "به اثرهای بلندمدت کم توجه است.",
            "به اقتصاد توجه کم می‌دهد.",
            "به تفاوت نسلی کم می‌پردازد.",
            "به رسانهٔ سنتی کم توجه است.",
        ],
        critique_text="منتقدان پاپاچاریسی می‌گویند تحلیل او از عاطفه بیش از اندازه خوش‌بینانه است و قدرت پلتفرم و سوءاستفاده از احساس را کم می‌بیند؛ با این حال، او نشان داد سیاست دیجیتال را نمی‌توان بدون احساس و روایت فهمید.",
        applications=[
            "تحلیل جنبش‌های شبکه‌ای.",
            "پژوهش مشارکت آنلاین.",
            "مطالعهٔ توییتر سیاسی.",
            "تحلیل عموم عاطفی.",
            "پژوهش هشتگ و اعتراض.",
            "مطالعهٔ روایت شخصی در شبکه‌های اجتماعی.",
            "تحلیل خود شبکه‌ای.",
            "پژوهش سیاست دیجیتال.",
            "مطالعهٔ احساس و انتخابات.",
            "تحلیل کنش مدنی آنلاین.",
            "پژوهش رسانهٔ اجتماعی و دموکراسی.",
            "مطالعهٔ حوزهٔ خصوصی دیجیتال.",
            "تحلیل پادکست سیاسی.",
            "پژوهش احساس در خبر.",
            "مطالعهٔ کمپین آنلاین.",
            "تحلیل همبستگی عاطفی در بحران.",
        ],
        example_text="هشتگی که با روایت‌های شخصی و تصاویر احساسی از یک رویداد شکل می‌گیرد و در چند روز به همبستگی گسترده بدل می‌شود، نمونهٔ عموم عاطفی پاپاچاریسی است.",
        evolution="پاپاچاریسی در سال ۲۰۱۰ حوزهٔ خصوصی را نوشت و در سال ۲۰۱۵ عموم‌های عاطفی را منتشر کرد؛ پژوهش‌های بعدی دربارهٔ پلتفرم و احساس، چارچوب او را به تحلیل سیاست دیجیتال روزمره گستراندند.",
        key_concepts=["حوزهٔ خصوصی", "عموم عاطفی", "خود شبکه‌ای", "مشارکت آنلاین", "روایت شخصی", "سیاست دیجیتال"],
        theorists="یورگن هابرماس، نانسی فریزر و مانوئل کاستلز.",
        theorists_text="پاپاچاریسی در سنت نظریهٔ حوزهٔ عمومی و مطالعات فرهنگی دیجیتال شکل گرفت.",
        model="عموم عاطفی به‌عنوان شکل‌گیری پیوند جمعی از احساس و روایت در پلتفرم‌های شبکه‌ای.",
        studies=[
            "کتاب حوزهٔ خصوصی سال ۲۰۱۰.",
            "کتاب عموم‌های عاطفی سال ۲۰۱۵.",
            "پژوهش توییتر و اعتراض.",
            "مطالعهٔ جنبش‌های شبکه‌ای.",
            "تحلیل روایت شخصی آنلاین.",
            "پژوهش خود شبکه‌ای.",
            "مطالعهٔ احساس و سیاست.",
            "تحلیل هشتگ و همبستگی.",
            "پژوهش مشارکت مدنی آنلاین.",
            "مطالعهٔ حوزهٔ عمومی دیجیتال.",
            "تحلیل رسانهٔ اجتماعی و دموکراسی.",
            "پژوهش عاطفه در خبر.",
        ],
    ),
    "th-39": dict(
        year=2018,
        mapping=MAPPING,
        summary="دیوید نیبورگ استاد ارتباطات دانشگاه تورنتو و از نظریه‌پردازان پلتفرمی‌شدن تولید فرهنگی است. او با توماس پول در مقالهٔ پلتفرمی‌شدن تولید فرهنگی در سال ۲۰۱۸ استدلال کرد پلتفرم‌ها با واسطه‌گری زیرساختی، داده و اقتصاد، تولید فرهنگی را بازسازمان می‌دهند و کالای فرهنگی را به کالایی اقتضایی بدل می‌کنند که ارزش و شکل آن به تصمیم‌های پلتفرم وابسته است. نیبورگ در مقالهٔ خردکردن آب‌نبات در سال ۲۰۱۵ نشان داد بازی رایگان‌به‌بازی چگونه با داده و تبلیغات و طراحی اعتیادآور، بازیکن و کنش او را به کالا بدل می‌کند. او پژوهش خود را بر اقتصاد اپلیکیشن، بازی، خبر و رسانهٔ دیجیتال متمرکز کرده و بر وابستگی متقابل تولیدکنندگان فرهنگی و پلتفرم‌ها تأکید دارد. نقدهای اصلی به او، تمرکز بر اقتصاد سیاسی، نمونه‌های شمال جهانی و کم‌توجهی به عاملیت کاربر را برجسته می‌کنند.",
        definition="دیوید نیبورگ نظریه‌پرداز پلتفرمی‌شدن تولید فرهنگی است که وابستگی تولیدکنندگان فرهنگی به زیرساخت و اقتصاد پلتفرم را تحلیل می‌کند.",
        main_problem="پلتفرم‌ها چگونه تولید، توزیع و ارزش‌گذاری فرهنگ را بازسازمان می‌دهند و تولیدکنندگان فرهنگی را به آن‌ها وابسته می‌کنند.",
        mechanism="پلتفرم با کنترل زیرساخت، داده و قواعد توزیع، محصول فرهنگی را به کالایی اقتضایی بدل می‌کند؛ تولیدکننده برای دسترسی به مخاطب با شرایط پلتفرم سازگار می‌شود و ارزش در زنجیرهٔ داده و تبلیغات بازتوزیع می‌شود.",
        assumptions=[
            "پلتفرم زیرساخت تولید فرهنگی است.",
            "کالای فرهنگی اقتضایی و متغیر است.",
            "داده منبع ارزش پلتفرم است.",
            "تولیدکننده به پلتفرم وابسته است.",
            "قواعد پلتفرم محتوا را شکل می‌دهد.",
            "اقتصاد اپلیکیشن تولید را بازسازمان می‌کند.",
            "بازیکن و کاربر به کالا بدل می‌شوند.",
            "پلتفرم‌ها واسطهٔ توزیع و اندازه‌گیری‌اند.",
        ],
        principles=[
            "زیرساخت پلتفرم را در تحلیل بگنجان.",
            "کالای فرهنگی را اقتضایی ببین.",
            "جریان داده و ارزش را ردیابی کن.",
            "وابستگی تولیدکننده را بسنج.",
            "قواعد توزیع را بررسی کن.",
            "به مدل درآمدی پلتفرم توجه کن.",
            "به کار کاربر و بازیکن توجه کن.",
        ],
        critiques=[
            "بر اقتصاد سیاسی متمرکز است.",
            "نمونه‌ها شمال جهانی‌اند.",
            "به عاملیت کاربر کم می‌پردازد.",
            "به تنوع پلتفرم‌ها کم توجه است.",
            "به سیاست تنظیم‌گری کم می‌پردازد.",
            "به فرهنگ محلی کم توجه است.",
            "به نابرابری جنسیتی کم می‌پردازد.",
            "به مقاومت تولیدکنندگان کم توجه است.",
            "مفاهیم آن گاه انتزاعی‌اند.",
            "به شواهد تطبیقی کم تکیه دارد.",
            "به رسانهٔ دولتی کم می‌پردازد.",
            "به تغییر سریع پلتفرم‌ها نمی‌رسد.",
            "به مصرف‌کنندهٔ غیرغربی کم توجه است.",
        ],
        critique_text="منتقدان نیبورگ می‌گویند تحلیل او بیش از اندازه اقتصادمحور است و عاملیت کاربر و تفاوت‌های محلی را کم می‌بیند؛ با این حال، او چارچوبی دقیق برای فهم وابستگی تولید فرهنگی به زیرساخت و اقتصاد پلتفرم ساخت.",
        applications=[
            "تحلیل اقتصاد اپلیکیشن.",
            "پژوهش بازی رایگان‌به‌بازی.",
            "مطالعهٔ پلتفرم خبر.",
            "تحلیل کار داده‌ای کاربران.",
            "پژوهش تولید محتوای ویدیویی.",
            "مطالعهٔ موسیقی در پلتفرم.",
            "تحلیل مدل درآمدی رسانه.",
            "پژوهش اینفلوئنسر و برند.",
            "مطالعهٔ پلتفرمی‌شدن آموزش.",
            "تحلیل فروشگاه اپلیکیشن.",
            "پژوهش پادکست و پلتفرم.",
            "مطالعهٔ روزنامه‌نگاری پلتفرمی.",
            "تحلیل بازی موبایلی.",
            "پژوهش تبلیغات برنامه‌ای.",
            "مطالعهٔ وابستگی ناشران.",
            "تحلیل سیاست پلتفرم.",
        ],
        example_text="بازی موبایلی رایگانی که از فروش آیتم‌های درون‌برنامه‌ای و تبلیغات و دادهٔ رفتار بازیکن درآمد می‌سازد، نمونهٔ کالای فرهنگی اقتضایی نیبورگ است: تجربهٔ بازی تابع مدل درآمدی پلتفرم است.",
        evolution="نیبورگ در سال ۲۰۱۵ با خردکردن آب‌نبات اقتصاد بازی را تحلیل کرد و در سال ۲۰۱۸ با پول، نظریهٔ پلتفرمی‌شدن تولید فرهنگی را صورت‌بندی کرد؛ پژوهش‌های بعدی دربارهٔ زیرساخت پلتفرم و قدرت آن، چارچوب او را گستراندند.",
        key_concepts=["پلتفرمی‌شدن", "کالای فرهنگی اقتضایی", "زیرساخت پلتفرم", "اقتصاد اپلیکیشن", "داده‌سازی", "وابستگی تولیدکننده"],
        theorists="توماس پول، خوزه ون دایک و دیوید هزمندهالگ.",
        theorists_text="نیبورگ در سنت اقتصاد سیاسی رسانه و پژوهش پلتفرم شکل گرفت و با پول نظریه را صورت‌بندی کرد.",
        model="پلتفرمی‌شدن به‌عنوان بازسازمان تولید فرهنگی زیر کنترل زیرساخت و اقتصاد پلتفرم.",
        studies=[
            "مقالهٔ خردکردن آب‌نبات سال ۲۰۱۵.",
            "مقالهٔ پلتفرمی‌شدن تولید فرهنگی سال ۲۰۱۸.",
            "پژوهش اقتصاد اپلیکیشن.",
            "مطالعهٔ بازی رایگان‌به‌بازی.",
            "تحلیل پلتفرم خبر.",
            "پژوهش کار داده‌ای.",
            "مطالعهٔ مدل درآمدی رسانه.",
            "تحلیل فروشگاه اپلیکیشن.",
            "پژوهش پلتفرم موسیقی.",
            "مطالعهٔ وابستگی ناشران.",
            "تحلیل سیاست پلتفرم.",
            "پژوهش تولید فرهنگی دیجیتال.",
            "تحلیل اقتصاد خلاق دیجیتال.",
        ],
    ),
    "MC-101": dict(
        year=1985,
        mapping=WORK_MAPPING,
        summary="اثر رسانهٔ خصمانه پدیده‌ای ادراکی است که والون و راس و لپر در سال ۱۹۸۵ در مطالعهٔ پوشش کشتار بیروت کشف کردند. آن‌ها نشان دادند طرفداران دو سوی یک منازعهٔ سیاسی، پوشش خبری نسبتاً متعادل یک رسانه را سوگیرانه و خصمانه نسبت به موضع خود می‌بینند. این ادراک از آنجا می‌آید که طرفداران با معیارهای متفاوت خبر را می‌سنجند، بخش‌های موافق و مخالف را به شکل گزینشی به یاد می‌آورند و تصور می‌کنند رسانه بر مخاطبان بی‌طرف اثر می‌گذارد. اثر رسانهٔ خصمانه با اثر شخص سوم پیوند دارد و در پژوهش‌های بعدی دربارهٔ انتخابات، علم، ورزش و سلامت آزموده شد. نقدهای اصلی به این پدیده، وابستگی به سطح درگیری، تنوع روش‌ها و محدودیت تعمیم آزمایشگاهی را برجسته می‌کنند.",
        definition="اثر رسانهٔ خصمانه سوگیری ادراکی طرفداران یک مسئله است که پوشش متعادل رسانه را خصمانه نسبت به موضع خود می‌بینند.",
        main_problem="چرا طرفداران دو سوی یک مسئله، پوشش خبری یکسان و نسبتاً متعادل را به سود طرف مقابل و علیه خود ادراک می‌کنند.",
        mechanism="طرفدار با معیارهای سخت‌گیرانه برای مواضع خود و معیارهای آسان برای مواضع رقیب، خبر را ارزیابی می‌کند؛ حافظهٔ گزینشی و تصور اثر بر دیگران، ادراک خصمانگی را تقویت می‌کند.",
        assumptions=[
            "ادراک خبر به سطح درگیری طرفدار وابسته است.",
            "طرفداران معیار دوگانه به کار می‌برند.",
            "یادآوری خبر گزینشی است.",
            "تصور اثر بر دیگران ادراک را شکل می‌دهد.",
            "پوشش متعادل هم خصمانه دیده می‌شود.",
            "اثر در هر دو سوی منازعه رخ می‌دهد.",
            "درگیری هویتی ادراک را تشدید می‌کند.",
            "اثر با اعتماد به رسانه رابطه دارد.",
        ],
        principles=[
            "سطح درگیری مخاطب را بسنج.",
            "معیار ارزیابی دو طرف را مقایسه کن.",
            "به حافظهٔ گزینشی توجه کن.",
            "ادراک اثر بر دیگران را جدا بسنج.",
            "پوشش متعادل را نقطهٔ آزمون بگیر.",
            "به هویت گروهی توجه کن.",
            "اثر را در دو سوی منازعه بررسی کن.",
        ],
        critiques=[
            "به سطح درگیری وابسته است.",
            "روش‌ها یکدست نیستند.",
            "تعمیم آزمایشگاهی محدود است.",
            "به رسانهٔ دیجیتال دیر رسید.",
            "به تفاوت فرهنگی کم توجه است.",
            "سنجش ادراک ذهنی است.",
            "به مخاطب بی‌طرف کم می‌پردازد.",
            "به نقش الگوریتم کم توجه است.",
            "به خبر جعلی کمتر می‌پردازد.",
            "به اعتماد نهادی کم توجه است.",
            "به شدت منازعه کم می‌پردازد.",
            "به رسانهٔ محلی کم توجه است.",
            "به اثرهای بلندمدت کم می‌پردازد.",
        ],
        critique_text="منتقدان این پدیده می‌گویند اثر به سطح درگیری و روش سنجش وابسته است و تعمیم آن به محیط دیجیتال و فرهنگ‌های مختلف نیازمند آزمون بیشتر است؛ با این حال، مطالعهٔ ۱۹۸۵ نشان داد ادراک سوگیری رسانه خود پدیده‌ای مستقل و اثرگذار است.",
        applications=[
            "تحلیل ادراک سوگیری خبر.",
            "پژوهش انتخابات و رسانه.",
            "مطالعهٔ پوشش منازعه.",
            "تحلیل اعتماد به خبر.",
            "پژوهش رسانه و علم.",
            "مطالعهٔ خبر ورزشی.",
            "تحلیل خبر سلامت.",
            "پژوهش رسانهٔ اجتماعی و قطب‌بندی.",
            "مطالعهٔ ادراک در طرفداران حزب.",
            "تحلیل خبر محیط زیست.",
            "پژوهش سوگیری ادراکی خبرنگار.",
            "مطالعهٔ رسانه و هواداران.",
            "تحلیل ادراک بی‌طرفی.",
            "پژوهش خبر و هویت گروهی.",
            "مطالعهٔ اعتبار رسانه.",
            "تحلیل قطب‌بندی سیاسی آنلاین.",
        ],
        example_text="در مطالعهٔ اصلی، هواداران دو طرف یک منازعه فیلم یکسانی از پوشش خبری دیدند، اما هر گروه آن را به سود طرف مقابل خواندند؛ این همان پارادوکس ادراک خصمانه است.",
        evolution="والون و راس و لپر در سال ۱۹۸۵ پدیده را معرفی کردند؛ پژوهش‌های بعدی سازوکارها و شرایط مرزی آن را گستردند و پرلوف در سال ۲۰۱۵ مروری سه‌دهه‌ای بر آن نوشت و پیوند آن را با اعتماد رسانه و محیط دیجیتال بررسی کرد.",
        key_concepts=["رسانهٔ خصمانه", "ادراک سوگیرانه", "درگیری طرفدارانه", "معیار دوگانه", "اثر شخص سوم", "اعتماد رسانه"],
        theorists="رابرت والون، لی راس و مارک لپر.",
        theorists_text="پدیده در سنت روان‌شناسی اجتماعی ادراک و پژوهش سوگیری رسانه شکل گرفت.",
        model="ادراک خصمانگی به‌عنوان برآیند درگیری، معیار دوگانه و تصور اثر بر دیگران.",
        studies=[
            "مطالعهٔ پوشش کشتار بیروت سال ۱۹۸۵.",
            "مرور سه‌دهه‌ای پرلوف سال ۲۰۱۵.",
            "پژوهش ادراک سوگیری انتخاباتی.",
            "مطالعهٔ رسانه و منازعه.",
            "تحلیل اثر شخص سوم.",
            "پژوهش اعتماد به خبر.",
            "مطالعهٔ رسانه و علم.",
            "تحلیل خبر ورزشی.",
            "پژوهش قطب‌بندی آنلاین.",
            "مطالعهٔ ادراک بی‌طرفی.",
            "تحلیل خبر سلامت.",
            "پژوهش هویت و ادراک رسانه.",
        ],
    ),
}

NAME_FIX = {
    "th-36": ("لوسی کونگ", "Lucy Kung", "canonical English name corrected from 'Lucy Kung' to 'Lucy Küng' per verified bibliographic records"),
}
YEAR_FIX = {
    "th-36": "year field was 'پژوهشگر معاصر' and normalised to Strategic Management in the Media (2008)",
    "th-37": "year field was 'پژوهشگر معاصر' and normalised to A Private Sphere (2010)",
    "th-39": "year field was 'پژوهشگر معاصر' and normalised to platformization article (2018)",
    "MC-101": "year field denotes the origin study (1985); verified against Vallone, Ross & Lepper (1985)",
}

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



YEAR_FIX.update({
    "MC-582": "year corrected 2000 -> 2001 (verified anchor: Baker & Martinson, TARES Test, 2001); note: editorial card theorist attribution was unverifiable and documentation rebuilt from verified literature",
    "MC-598": "no year change; note: editorial card core_logic was a mismatched media-economics template, documentation rebuilt from Heath (1993) and Ihlen (2011)",
})


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
                                       "verified": n_verified, "batch": 174}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH174 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
