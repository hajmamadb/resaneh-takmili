# -*- coding: utf-8 -*-
"""Batch 172 (PERSON, cognitive and news-selection classics): th-25 Kahneman, th-26 Altheide, th-29 Tichenor, th-30 Manning White."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch172-person-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch172_person.json"

MAPPING = {"entity_type": "PERSON", "content_type": "شخصیت علمی (نظریه‌پرداز)", "needs_review": False}

S = {
    "th-25": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Prospect Theory: An Analysis of Decision under Risk",
             title_fa="نظریهٔ چشم‌انداز: تحلیلی از تصمیم‌گیری زیر ریسک",
             authors="Kahneman, D.; Tversky, A.", year=1979,
             publisher="Econometrica, 47(2), 263-291",
             doi="10.2307/1914185",
             url="https://www.econometricsociety.org/publications/econometrica/1979/03/01/prospect-theory-analysis-decision-under-risk",
             language="en", isbn=None,
             citation="Kahneman, D., & Tversky, A. (1979). Prospect theory: An analysis of decision under risk. Econometrica, 47(2), 263-291.",
             locator="47(2), pp. 263-291", locator_type="page_range",
             supports="loss aversion, reference dependence and probability weighting in risky choice", verified=True),
        dict(kind="BOOK",
             title_en="Thinking, Fast and Slow",
             title_fa="تفکر سریع و کند",
             authors="Kahneman, D.", year=2011,
             publisher="Farrar, Straus and Giroux",
             doi=None,
             url="https://books.google.com/books/about/Thinking_Fast_and_Slow.html?id=ZuKTvERuPG8C",
             language="en", isbn=None,
             citation="Kahneman, D. (2011). Thinking, Fast and Slow. New York: Farrar, Straus and Giroux.",
             locator="2011 edition", locator_type="edition",
             supports="two-system model of judgment and the heuristics-and-biases program", verified=True),
    ],
    "th-26": [
        dict(kind="BOOK",
             title_en="Media Logic",
             title_fa="منطق رسانه",
             authors="Altheide, D. L.; Snow, R. P.", year=1979,
             publisher="Sage",
             doi=None,
             url="https://archive.org/details/medialogic0000alth",
             language="en", isbn="9780803912960",
             citation="Altheide, D. L., & Snow, R. P. (1979). Media Logic. Beverly Hills, CA: Sage.",
             locator="1979 edition", locator_type="edition",
             supports="media logic as format and process shaping content and social institutions", verified=True),
        dict(kind="BOOK",
             title_en="Qualitative Media Analysis",
             title_fa="تحلیل کیفی رسانه",
             authors="Altheide, D. L.", year=1996,
             publisher="Sage",
             doi="10.4135/9781412985536",
             url="https://methods.sagepub.com/book/mono/qualitative-media-analysis/toc",
             language="en", isbn=None,
             citation="Altheide, D. L. (1996). Qualitative Media Analysis. Thousand Oaks, CA: Sage.",
             locator="1996 edition", locator_type="edition",
             supports="ethnographic content analysis and document analysis of media formats", verified=True),
    ],
    "th-29": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Mass Media Flow and Differential Growth in Knowledge",
             title_fa="جریان رسانهٔ جمعی و رشد متفاوت دانش",
             authors="Tichenor, P. J.; Donohue, G. A.; Olien, C. N.", year=1970,
             publisher="Public Opinion Quarterly, 34(2), 159-170",
             doi="10.1086/267786",
             url="https://academic.oup.com/poq/article-abstract/34/2/159/1843590",
             language="en", isbn=None,
             citation="Tichenor, P. J., Donohue, G. A., & Olien, C. N. (1970). Mass media flow and differential growth in knowledge. Public Opinion Quarterly, 34(2), 159-170.",
             locator="34(2), pp. 159-170", locator_type="page_range",
             supports="knowledge gap hypothesis and socioeconomic stratification of information gain", verified=True),
        dict(kind="BOOK",
             title_en="Community Conflict and the Press",
             title_fa="کشمکش اجتماعی و مطبوعات",
             authors="Tichenor, P. J.; Donohue, G. A.; Olien, C. N.", year=1980,
             publisher="Sage",
             doi=None,
             url="https://books.google.com.au/books?id=9Si7AAAAIAAJ",
             language="en", isbn=None,
             citation="Tichenor, P. J., Donohue, G. A., & Olien, C. N. (1980). Community Conflict and the Press. Beverly Hills, CA: Sage.",
             locator="1980 edition", locator_type="edition",
             supports="community structure, conflict and conditional knowledge-gap effects", verified=True),
    ],
    "th-30": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Gate Keeper: A Case Study in the Selection of News",
             title_fa="دروازه‌بان: مطالعهٔ موردی انتخاب خبر",
             authors="White, D. M.", year=1950,
             publisher="Journalism Quarterly, 27(4), 383-390",
             doi="10.1177/107769905002700403",
             url="https://journals.sagepub.com/doi/abs/10.1177/107769905002700403",
             language="en", isbn=None,
             citation="White, D. M. (1950). The gate keeper: A case study in the selection of news. Journalism Quarterly, 27(4), 383-390.",
             locator="27(4), pp. 383-390", locator_type="page_range",
             supports="subjective human selection at the news gate", verified=True),
        dict(kind="BOOK",
             title_en="The Funnies: An American Idiom",
             title_fa="کمیک‌ها: یک اصطلاح آمریکایی",
             authors="White, D. M.; Abel, R. H.", year=1963,
             publisher="Free Press of Glencoe",
             doi=None,
             url="https://archive.org/details/bwb_P9-DVF-543",
             language="en", isbn=None,
             citation="White, D. M., & Abel, R. H. (Eds.). (1963). The Funnies: An American Idiom. New York: Free Press of Glencoe.",
             locator="1963 edition", locator_type="edition",
             supports="popular culture and comic strip analysis within mass communication research", verified=True),
    ],
}

ENRICH = {
    "th-25": dict(
        year=1979,
        mapping=MAPPING,
        summary="دانیل کانمن (۱۹۳۴-۲۰۲۴) روان‌شناس اسرائیلی‌آمریکایی و برندهٔ نوبل اقتصاد در سال ۲۰۰۲ است که با آموس تورسکی نظریهٔ چشم‌انداز را در سال ۱۹۷۹ منتشر کرد. این نظریه نشان داد افراد تصمیم را نه بر پایهٔ ثروت نهایی، بلکه بر پایهٔ تغییر نسبت به نقطهٔ مرجع می‌سنجند و زیان را سنگین‌تر از سود هم‌ارز تجربه می‌کنند. کانمن و تورسکی همچنین برنامهٔ میان‌برها و سوگیری‌ها را ساختند و دسترس‌پذیری، نمایندگی و لنگر انداختن را توصیف کردند. کانمن در کتاب تفکر سریع و کند در سال ۲۰۱۱ دو نظام شناختی را از هم جدا کرد: نظام یک سریع و شهودی و نظام دو کند و تحلیلی. یافته‌های او دربارهٔ خطای ادراکی، سیاست‌گذاری مبتنی بر بینش رفتاری و ارتباطات سلامت را دگرگون کرد. نقدهای اصلی به او، مصنوعی‌بودن آزمایش‌ها، نمونهٔ محدود و بحران تکرارپذیری برخی یافته‌ها را برجسته می‌کنند.",
        definition="دانیل کانمن روان‌شناس شناختی و نظریه‌پرداز تصمیم است که با نظریهٔ چشم‌انداز و مدل دو نظامی، محدودیت‌های عقلانیت اقتصادی را نشان داد.",
        main_problem="چرا انسان‌ها در شرایط ریسک و عدم قطعیت به‌طور نظام‌مند از الگوی عقلانی انتخاب فاصله می‌گیرند.",
        mechanism="ادراک و داوری با میان‌برهای شناختی ساده می‌شود؛ نقطهٔ مرجع و زیان‌گریزی انتخاب را جهت می‌دهد و نظام سریع با پاسخ‌های آماده، خطاهای پیش‌بینی‌پذیر می‌سازد.",
        assumptions=[
            "تصمیم نسبت به نقطهٔ مرجع سنجیده می‌شود.",
            "زیان سنگین‌تر از سود هم‌ارز است.",
            "دو نظام شناختی مستقل وجود دارد.",
            "میان‌برها خطاهای نظام‌مند می‌سازند.",
            "احتمال‌ها ذهنی و وزن‌دار ادراک می‌شوند.",
            "داوری تحت عدم قطعیت خطاپذیر است.",
            "قالب ارائه بر انتخاب اثر دارد.",
            "خطاها پیش‌بینی‌پذیرند.",
        ],
        principles=[
            "نقطهٔ مرجع را در تصمیم مشخص کن.",
            "زیان و سود را نامتقارن ببین.",
            "نظام سریع و کند را تفکیک کن.",
            "قالب ارائه را متغیر تحلیل بگیر.",
            "میان‌برهای شناختی را شناسایی کن.",
            "خطای پیش‌بینی‌پذیر را اصلاح کن.",
            "یافته‌ها را با تکرار بسنج.",
        ],
        critiques=[
            "آزمایش‌ها مصنوعی‌اند.",
            "نمونه‌ها محدود و غربی‌اند.",
            "بخشی از یافته‌ها تکرار نشده است.",
            "به فرهنگ و نهاد کم توجه است.",
            "به احساسات پیچیده کم می‌پردازد.",
            "اثرها در جهان واقع کوچک‌ترند.",
            "به یادگیری و تجربه کم می‌پردازد.",
            "مدل دو نظامی ساده‌سازی است.",
            "به تصمیم جمعی کم توجه است.",
            "به تفاوت فردی کم می‌پردازد.",
            "کاربرد سیاستی آن گاه دستکاری است.",
            "به انگیزه و هدف کم توجه است.",
            "سنجه‌های آزمایشگاهی محدودند.",
        ],
        critique_text="منتقدان کانمن می‌گویند یافته‌های او در آزمایشگاه به‌دست آمده و تعمیم آن به تصمیم واقعی محدود است و بخشی از نتایج در بحران تکرارپذیری تأیید نشد؛ با این حال، نظریهٔ چشم‌انداز و مدل دو نظامی از بنیادی‌ترین دستاوردهای علوم شناختی و رفتاری است.",
        applications=[
            "طراحی سیاست عمومی رفتاری.",
            "ارتباط ریسک سلامت.",
            "تحلیل تصمیم مالی.",
            "پژوهش تبلیغات و قالب پیام.",
            "مطالعهٔ ادراک زیان در خبر.",
            "تحلیل تصمیم مصرف‌کننده.",
            "طراحی کمپین تغییر رفتار.",
            "پژوهش بیمه و پس‌انداز.",
            "تحلیل خطای داوری خبرنگار.",
            "مطالعهٔ قالب‌بندی پاداش.",
            "تحلیل تصمیم در بحران.",
            "پژوهش انتخاب درمان.",
            "مطالعهٔ ادراک تورم.",
            "تحلیل تصمیم رأی‌دهنده.",
            "پژوهش پیمانهٔ انرژی و تصمیم.",
            "تحلیل قالب‌بندی مالیات.",
            "مطالعهٔ سوگیری رسانه‌ای.",
            "پژوهش تصمیم در بازی.",
            "تحلیل سیاست‌های تشویقی.",
            "مطالعهٔ ادراک عدالت در تخصیص.",
        ],
        example_text="وقتی خبری یک درمان را با نرخ بقای نود درصد و خبری دیگر همان درمان را با نرخ مرگ ده درصد گزارش می‌کند، مخاطب دو داوری متفاوت می‌سازد؛ کانمن نشان داد قالب ارائه، انتخاب را جهت می‌دهد.",
        evolution="کانمن با تورسکی در سال ۱۹۷۹ نظریهٔ چشم‌انداز را منتشر کرد و در سال ۲۰۰۲ نوبل اقتصاد گرفت؛ در سال ۲۰۱۱ با تفکر سریع و کند یافته‌ها را برای مخاطب عمومی جمع کرد و پژوهش اقتصاد رفتاری بعدی، چارچوب او را به سیاست عمومی برد.",
        key_concepts=["نظریهٔ چشم‌انداز", "زیان‌گریزی", "نقطهٔ مرجع", "نظام یک", "نظام دو", "میان‌بر شناختی"],
        theorists="آموس تورسکی، هربرت سایمون و ریچارد تالر.",
        theorists_text="کانمن در سنت روان‌شناسی شناختی و اقتصاد رفتاری، در همکاری با تورسکی کار کرد.",
        model="داوری و تصمیم به‌عنوان برآیند دو نظام شناختی و ارزیابی نسبی سود و زیان.",
        studies=[
            "مقالهٔ نظریهٔ چشم‌انداز سال ۱۹۷۹.",
            "کتاب تفکر سریع و کند سال ۲۰۱۱.",
            "پژوهش میان‌برها و سوگیری‌ها.",
            "مطالعهٔ زیان‌گریزی.",
            "تحلیل قالب‌بندی پیام.",
            "پژوهش ادراک ریسک.",
            "مطالعهٔ تصمیم مالی.",
            "تحلیل داوری در عدم قطعیت.",
            "پژوهش ادراک زمانی و حافظه.",
            "مطالعهٔ سیاست رفتاری.",
            "تحلیل تصمیم سلامت.",
            "پژوهش خطای پیش‌بینی.",
        ],
    ),
    "th-26": dict(
        year=1979,
        mapping=MAPPING,
        summary="دیوید آلتهاید (زادهٔ ۱۹۳۸) استاد جامعه‌شناسی و عدالت اجتماعی دانشگاه ایالتی آریزونا است که با رابرت اسنو در کتاب منطق رسانه در سال ۱۹۷۹ مفهوم منطق رسانه را صورت‌بندی کرد. آن‌ها استدلال کردند رسانه‌ها منطق خاص خود را دارند: شکل ارائه، زمان‌بندی، قالب و قواعد تولید، نه فقط محتوا، معنای پیام را می‌سازد. آلتهاید نشان داد این منطق از خبر و سرگرمی فراتر می‌رود و سیاست، دین، ورزش و جرم را نیز بازسازمان می‌دهد. او در دههٔ ۱۹۹۰ بوم‌شناسی ارتباطات و تحلیل کیفی رسانه را گسترد و در پژوهش‌های خود پیوند ترس، بحران و کنترل اجتماعی را در پوشش خبری تحلیل کرد. آلتهاید روش تحلیل محتوای قوم‌نگارانه را برای مطالعهٔ قالب‌های رسانه‌ای پیشنهاد کرد. نقدهای اصلی به او، کارکردگرایی، رسانه‌محوری، ابهام مفهوم منطق و کم‌توجهی به پلتفرم‌های دیجیتال را برجسته می‌کنند.",
        definition="دیوید آلتهاید جامعه‌شناس رسانه است که با مفهوم منطق رسانه نشان داد قالب و قواعد تولید رسانه، محتوا و نهادهای اجتماعی را شکل می‌دهند.",
        main_problem="قالب و منطق تولید رسانه چگونه محتوای پیام و حتی سازمان حوزه‌های غیررسانه‌ای مانند سیاست و دین را تغییر می‌دهد.",
        mechanism="رسانه با تعیین قالب، زمان و قواعد ارائه، محتوا را برای جذب مخاطب بازسازمان می‌کند؛ نهادهای دیگر برای حضور رسانه‌ای، ساختار و کنش خود را با این منطق هم‌ساز می‌کنند.",
        assumptions=[
            "شکل ارائه به‌اندازهٔ محتوا اهمیت دارد.",
            "رسانه منطق تولید خاص خود دارد.",
            "منطق رسانه به حوزه‌های دیگر نفوذ می‌کند.",
            "نهادها برای رسانه بازسازمان می‌شوند.",
            "قالب خبر معنا را جهت می‌دهد.",
            "ترس و بحران در خبر سازمان می‌یابد.",
            "تحلیل قالب نیازمند روش کیفی است.",
            "منطق رسانه تاریخی و متغیر است.",
        ],
        principles=[
            "قالب ارائه را در تحلیل بگنجان.",
            "منطق تولید را از محتوا جدا کن.",
            "نفوذ منطق رسانه در نهادها را پی بگیر.",
            "روش قوم‌نگارانه را به کار بند.",
            "پیوند ترس و کنترل را بررسی کن.",
            "تاریخ قالب‌ها را در نظر بگیر.",
            "به تفاوت رسانه‌ها توجه کن.",
        ],
        critiques=[
            "کارکردگرا و رسانه‌محور است.",
            "مفهوم منطق رسانه مبهم است.",
            "به قدرت اقتصادی کم می‌پردازد.",
            "به مخاطب فعال کم بها می‌دهد.",
            "به پلتفرم دیجیتال نمی‌رسد.",
            "شواهد آن بیشتر موردی است.",
            "به تفاوت فرهنگی کم توجه است.",
            "به مقاومت نهادها کم می‌پردازد.",
            "به سیاست رسانه کم توجه است.",
            "به اثرهای بلندمدت کم می‌پردازد.",
            "به رسانهٔ محلی کمتر می‌پردازد.",
            "به نابرابری رسانه‌ای کم توجه است.",
            "به عاملیت خبرنگار کم می‌پردازد.",
        ],
        critique_text="منتقدان آلتهاید می‌گویند چارچوب او بیش از اندازه رسانه‌محور و کارکردگراست و مفهوم منطق رسانه را مبهم می‌گذارد؛ با این حال، او نشان داد قالب رسانه متغیری مستقل در تولید معنا و بازسازی نهادهای اجتماعی است.",
        applications=[
            "تحلیل قالب خبر تلویزیونی.",
            "پژوهش سیاست سرگرمی‌شده.",
            "مطالعهٔ پوشش جرم و ترس.",
            "تحلیل دین در رسانه.",
            "پژوهش قالب ورزش در تلویزیون.",
            "مطالعهٔ برنامهٔ گفت‌وگومحور.",
            "تحلیل قالب تبلیغات.",
            "پژوهش خبر بحران.",
            "مطالعهٔ رسانه و کنترل اجتماعی.",
            "تحلیل قالب شبکه‌های اجتماعی.",
            "پژوهش روش تحلیل محتوای کیفی.",
            "مطالعهٔ قالب ویدیوی کوتاه.",
            "تحلیل قالب پادکست.",
            "پژوهش قالب خبر سلامت.",
            "مطالعهٔ رسانه و هراس اخلاقی.",
            "تحلیل قالب مستند.",
        ],
        example_text="وقتی یک مناظرهٔ سیاسی به بخش‌های کوتاه و جملات چشمگیر برش می‌خورد، محتوای بحث با قالب تلویزیونی دگرگون می‌شود؛ آلتهاید این را اثر منطق رسانه بر سیاست می‌دانست.",
        evolution="آلتهاید در سال ۱۹۷۹ با اسنو منطق رسانه را نوشت و در سال ۱۹۹۶ تحلیل کیفی رسانه را منتشر کرد؛ پژوهش‌های او دربارهٔ ترس و بحران در دههٔ ۲۰۰۰ و ۲۰۱۰ چارچوب را به امنیت و کنترل اجتماعی گستراند.",
        key_concepts=["منطق رسانه", "قالب رسانه‌ای", "بوم‌شناسی ارتباطات", "تحلیل محتوای قوم‌نگارانه", "ترس و کنترل", "رسانه‌ای‌شدن نهادها"],
        theorists="مارشال مک‌لوهان، هارولد اینیس و رابرت اسنو.",
        theorists_text="آلتهاید در سنت بوم‌شناسی رسانه و جامعه‌شناسی ارتباطات شکل گرفت.",
        model="منطق رسانه به‌عنوان مجموعهٔ قالب‌ها و قواعد تولید که محتوا و نهادهای اجتماعی را بازسازمان می‌دهد.",
        studies=[
            "کتاب منطق رسانه سال ۱۹۷۹.",
            "کتاب تحلیل کیفی رسانه سال ۱۹۹۶.",
            "پژوهش بوم‌شناسی ارتباطات.",
            "مطالعهٔ پوشش جرم و ترس.",
            "تحلیل سیاست و رسانه.",
            "پژوهش دین و رسانه.",
            "مطالعهٔ ورزش و تلویزیون.",
            "تحلیل قالب خبر بحران.",
            "پژوهش کنترل اجتماعی و رسانه.",
            "مطالعهٔ قالب رسانهٔ دیجیتال.",
            "تحلیل هراس اخلاقی.",
            "پژوهش روش تحلیل محتوا.",
        ],
    ),
    "th-29": dict(
        year=1970,
        mapping=MAPPING,
        summary="فیلیپ تیچنور (۱۹۳۲-۲۰۱۰) استاد روزنامه‌نگاری و ارتباطات دانشگاه مینه‌سوتا است که با جورج دانوهیو و کلاریس اولین در سال ۱۹۷۰ فرضیهٔ شکاف دانش را صورت‌بندی کرد. آن‌ها در مقالهٔ جریان رسانهٔ جمعی و رشد متفاوت دانش نشان دادند وقتی جریان اطلاعات در یک نظام رسانه‌ای افزایش می‌یابد، بخش‌های دارای پایگاه اجتماعی و اقتصادی بالاتر اطلاعات را سریع‌تر جذب می‌کنند و شکاف دانش در برابر گروه‌های پایین‌تر بازتر می‌شود. تیچنور و همکارانش بعدها شرایط اقتضایی این فرضیه را بررسی کردند و نشان دادند نوع مسئله، تعارض اجتماعی و ساختار جامعهٔ محلی می‌تواند شکاف را کم یا زیاد کند. آن‌ها در کتاب کشمکش اجتماعی و مطبوعات در سال ۱۹۸۰ پیوند ساختار اجتماعی، تعارض و پوشش خبری را تحلیل کردند. نقدهای اصلی به او، یکسان‌نگری رسانه‌ها، سنجه‌های سادهٔ دانش و کم‌توجهی به انگیزهٔ مخاطب را برجسته می‌کنند.",
        definition="فیلیپ تیچنور از صورت‌بندی‌کنندگان فرضیهٔ شکاف دانش است که نشان داد رشد اطلاعات رسانه‌ای نابرابری دانش را میان گروه‌های اجتماعی بازتر می‌کند.",
        main_problem="چرا افزایش دسترسی به اطلاعات رسانه‌ای همیشه شکاف دانایی میان گروه‌های اجتماعی و اقتصادی را کم نمی‌کند.",
        mechanism="گروه‌های دارای سرمایهٔ اجتماعی و آموزشی بیشتر، اطلاعات را سریع‌تر و عمیق‌تر پردازش می‌کنند؛ رسانه با فرض مخاطب توانمند، همین برتری را بازتولید می‌کند و شکاف را می‌گستراند.",
        assumptions=[
            "دانش میان گروه‌ها نابرابر توزیع می‌شود.",
            "گروه‌های بالاتر اطلاعات را سریع‌تر می‌گیرند.",
            "رشد اطلاعات شکاف را باز می‌کند.",
            "ساختار اجتماعی بر دریافت اثر دارد.",
            "سطح تحصیلات دریافت را جهت می‌دهد.",
            "نوع مسئله شکاف را تعدیل می‌کند.",
            "تعارض اجتماعی شکاف را تغییر می‌دهد.",
            "رسانهٔ محلی ساختار جامعه را بازتاب می‌دهد.",
        ],
        principles=[
            "دانش را میان گروه‌ها مقایسه کن.",
            "سرمایهٔ اجتماعی را در تحلیل بگنجان.",
            "نوع مسئله را تعدیل‌گر بگیر.",
            "تعارض اجتماعی را زمینهٔ شکاف بدان.",
            "رشد اطلاعات را زمان‌مند بسنج.",
            "ساختار جامعهٔ محلی را بررسی کن.",
            "به انگیزهٔ مخاطب توجه کن.",
        ],
        critiques=[
            "رسانه‌ها را یکسان می‌بیند.",
            "سنجهٔ دانش ساده است.",
            "به انگیزهٔ مخاطب کم توجه است.",
            "به رسانهٔ دیجیتال نمی‌رسد.",
            "شواهد آن بیشتر پیمایشی است.",
            "به تفاوت موضوع کم می‌پردازد.",
            "به شکاف مهارت دیجیتال کم توجه است.",
            "به زمینهٔ غیرآمریکایی کم توجه است.",
            "به رسانهٔ سرگرمی کم می‌پردازد.",
            "نابرابری را گاه طبیعی‌سازی می‌کند.",
            "به سیاست اطلاعات کم می‌پردازد.",
            "به مخاطب کودک کم توجه است.",
            "به تغییرات بلندمدت کم می‌پردازد.",
        ],
        critique_text="منتقدان تیچنور می‌گویند فرضیهٔ او رسانه‌ها را یکسان فرض می‌کند و انگیزهٔ مخاطب و شکاف مهارت دیجیتال را کم می‌بیند؛ با این حال، او نشان داد دسترسی برابر به اطلاعات به برابری دانش نمی‌انجامد و همین بینش بنیاد پژوهش شکاف دیجیتال شد.",
        applications=[
            "پژوهش شکاف دیجیتال.",
            "تحلیل کمپین سلامت.",
            "مطالعهٔ سواد علمی.",
            "تحلیل دانش سیاسی.",
            "پژوهش آموزش رسانه‌ای.",
            "مطالعهٔ خبر و طبقهٔ اجتماعی.",
            "تحلیل کمپین واکسیناسیون.",
            "پژوهش شکاف دانش محیطی.",
            "مطالعهٔ رسانهٔ محلی.",
            "تحلیل اطلاعات بحران.",
            "پژوهش شکاف در شبکه‌های اجتماعی.",
            "مطالعهٔ دانش سلامت سالمندان.",
            "تحلیل سیاست اطلاعات عمومی.",
            "پژوهش شکاف دانش مهاجران.",
            "مطالعهٔ سواد رسانه‌ای مدرسه.",
        ],
        example_text="یک کمپین عمومی دربارهٔ تغذیه سالم ممکن است در مجموع دانش را بالا ببرد، اما گروه‌های تحصیل‌کرده سریع‌تر یاد می‌گیرند و شکاف با گروه‌های کم‌سواد بازتر می‌شود؛ تیچنور این را پارادوکس جریان اطلاعات می‌نامید.",
        evolution="تیچنور و همکارانش در سال ۱۹۷۰ فرضیهٔ شکاف دانش را منتشر کردند و در سال ۱۹۸۰ با کشمکش اجتماعی و مطبوعات شرایط اقتضایی آن را گستردند؛ پژوهش شکاف دیجیتال و سواد رسانه‌ای بعدی، چارچوب او را ادامه داد.",
        key_concepts=["شکاف دانش", "جریان اطلاعات", "سرمایهٔ اجتماعی", "شرایط اقتضایی", "ساختار جامعهٔ محلی", "نابرابری اطلاعاتی"],
        theorists="جورج دانوهیو، کلاریس اولین و ملوین دفلور.",
        theorists_text="تیچنور در سنت پژوهش ساختار اجتماعی ارتباطات و روزنامه‌نگاری جامعه‌محور کار کرد.",
        model="شکاف دانش به‌عنوان برآیند رشد اطلاعات و تفاوت توان جذب گروه‌های اجتماعی.",
        studies=[
            "مقالهٔ شکاف دانش سال ۱۹۷۰.",
            "کتاب کشمکش اجتماعی و مطبوعات سال ۱۹۸۰.",
            "پژوهش شرایط اقتضایی شکاف.",
            "مطالعهٔ ساختار جامعهٔ محلی.",
            "تحلیل خبر و تعارض اجتماعی.",
            "پژوهش کمپین اطلاعات سلامت.",
            "مطالعهٔ دانش سیاسی و تحصیلات.",
            "تحلیل رسانهٔ محلی.",
            "پژوهش شکاف دانش محیطی.",
            "مطالعهٔ شکاف دیجیتال.",
            "تحلیل سواد علمی.",
            "پژوهش شکاف دانش در بحران.",
        ],
    ),
    "th-30": dict(
        year=1950,
        mapping=MAPPING,
        summary="دیوید منینگ وایت (۱۹۱۷-۱۹۹۳) استاد روزنامه‌نگاری دانشگاه بوستون و از پیشگامان پژوهش انتخاب خبر است که در سال ۱۹۵۰ مطالعهٔ دروازه‌بان را منتشر کرد. او در این مطالعه، سردبیر تلگراف یک روزنامهٔ کوچک را که با نام مستعار آقای گیتس خوانده می‌شد، در طول یک هفته همراهی کرد و نشان داد از میان هزاران خبر دریافتی، تنها بخش کوچکی به صفحهٔ روزنامه می‌رسد. وایت دلایل حذف خبر را ثبت کرد و دید که انتخاب نه فقط بر پایهٔ معیارهای حرفه‌ای، بلکه بر پایهٔ قضاوت شخصی، حدس دربارهٔ علاقهٔ خواننده و ترجیح‌های ذهنی انجام می‌شود. این مطالعه نقطهٔ آغاز نظریهٔ دروازه‌بانی در ارتباطات شد و نشان داد خبری که به مخاطب می‌رسد، حاصل زنجیره‌ای از تصمیم‌های انسانی است. وایت بعدها به پژوهش فرهنگ عامه و کمیک استریپ روی آورد. نقدهای اصلی به او، تک‌موردی‌بودن، غفلت از فشار سازمانی و ساده‌سازی فرایند انتخاب را برجسته می‌کنند.",
        definition="دیوید منینگ وایت پژوهشگر روزنامه‌نگاری است که با مطالعهٔ دروازه‌بان نشان داد انتخاب خبر حاصل قضاوت انسانی سردبیر و نه بازتاب کامل واقعیت است.",
        main_problem="چرا از میان انبوه خبرهای دریافتی تنها بخش کوچکی به دست مخاطب می‌رسد و چه معیارهایی این انتخاب را هدایت می‌کند.",
        mechanism="سردبیر به‌عنوان دروازه‌بان، خبرهای دریافتی را بر پایهٔ معیارهای حرفه‌ای، حدس دربارهٔ علاقهٔ مخاطب و ترجیح شخصی غربال می‌کند؛ هر تصمیم کوچک در زنجیره، در نهایت تصویر خبری مخاطب را می‌سازد.",
        assumptions=[
            "خبر بازتاب کامل واقعیت نیست.",
            "انتخاب خبر تصمیم انسانی است.",
            "دروازه‌بان معیارهای شخصی دارد.",
            "علاقهٔ خواننده حدس زده می‌شود.",
            "زنجیرهٔ انتخاب تصویر خبر را می‌سازد.",
            "حجم خبر ورودی بیش از ظرفیت انتشار است.",
            "حذف خبر به‌اندازهٔ انتخاب آن مهم است.",
            "معیارهای حرفه‌ای و شخصی درهم می‌آمیزند.",
        ],
        principles=[
            "فرایند انتخاب را گام‌به‌گام ثبت کن.",
            "دلایل حذف خبر را بپرس.",
            "معیار حرفه‌ای و شخصی را تفکیک کن.",
            "نقش سازمان را در انتخاب ببین.",
            "به حدس دربارهٔ مخاطب توجه کن.",
            "زنجیرهٔ دروازه‌ها را تحلیل کن.",
            "انتخاب خبر را زمینه‌مند بسنج.",
        ],
        critiques=[
            "تک‌موردی و تعمیم‌ناپذیر است.",
            "به فشار سازمانی کم می‌پردازد.",
            "فرایند انتخاب را ساده می‌کند.",
            "به مالکیت رسانه کم توجه است.",
            "به مخاطب واقعی دسترسی ندارد.",
            "معیارها را نظام‌مند نسنجیده است.",
            "به خبر دیجیتال نمی‌رسد.",
            "به تنوع رسانه کم توجه است.",
            "به فرهنگ سازمانی کم می‌پردازد.",
            "به سیاست تحریریه کم توجه است.",
            "به دروازه‌بانی الگوریتمی نمی‌رسد.",
            "به زمینهٔ غیرآمریکایی کم توجه است.",
            "به اقتصاد خبر کم می‌پردازد.",
        ],
        critique_text="منتقدان وایت می‌گویند مطالعهٔ او تک‌موردی است و فشار سازمانی و مالکیت رسانه را نادیده می‌گیرد؛ با این حال، او نخستین پژوهش تجربی دربارهٔ انتخاب خبر را انجام داد و دروازه‌بانی را به یکی از مفاهیم بنیادی ارتباطات بدل کرد.",
        applications=[
            "تحلیل انتخاب خبر.",
            "پژوهش تحریریه.",
            "مطالعهٔ دروازه‌بانی خبری.",
            "تحلیل فیلترینگ محتوا.",
            "پژوهش الگوریتم خبر.",
            "مطالعهٔ سردبیری رسانهٔ محلی.",
            "تحلیل انتخاب خبر در بحران.",
            "پژوهش دروازه‌بان در شبکه‌های اجتماعی.",
            "مطالعهٔ مدیریت محتوا.",
            "تحلیل انتخاب تصویر خبری.",
            "پژوهش خبر و علاقهٔ مخاطب.",
            "مطالعهٔ کنترل دروازه در پلتفرم.",
            "تحلیل سیاست تحریریه.",
            "پژوهش انتخاب خبر سلامت.",
            "مطالعهٔ خبر و سانسور.",
            "تحلیل دروازه‌بانی الگوریتمی.",
        ],
        example_text="سردبیری که در یک روز صدها خبر خبرگزاری را می‌بیند و تنها بیست خبر را برای صفحهٔ اول برمی‌گزیند، در هر انتخاب هم معیار حرفه‌ای و هم سلیقهٔ شخصی و حدس دربارهٔ خواننده را به کار می‌برد؛ وایت این نقطه را دروازه نامید.",
        evolution="وایت در سال ۱۹۵۰ مطالعهٔ دروازه‌بان را منتشر کرد و در سال ۱۹۶۳ با رابرت آبل کتاب کمیک‌ها را ویرایش کرد؛ پژوهش دروازه‌بانی بعدی، از سطح فردی به سطح سازمانی و سپس به دروازه‌بانی الگوریتمی پلتفرم‌ها گسترانده شد.",
        key_concepts=["دروازه‌بانی", "انتخاب خبر", "سردبیر", "قضاوت انسانی", "معیار خبری", "زنجیرهٔ دروازه"],
        theorists="کرت لوین، والتر گیدینگ و پاملا شومیکر.",
        theorists_text="وایت مفهوم دروازه را از نظریهٔ کانال‌های لوین وام گرفت و آن را به انتخاب خبر تعمیم داد.",
        model="انتخاب خبر به‌عنوان زنجیرهٔ تصمیم‌های انسانی در دروازه‌های سازمان خبری.",
        studies=[
            "مقالهٔ دروازه‌بان سال ۱۹۵۰.",
            "کتاب کمیک‌ها سال ۱۹۶۳.",
            "مشاهدهٔ میدانی تحریریه.",
            "پژوهش انتخاب خبر.",
            "مطالعهٔ حذف خبر.",
            "تحلیل معیارهای سردبیری.",
            "پژوهش دروازه‌بانی سازمانی.",
            "مطالعهٔ خبر و علاقهٔ مخاطب.",
            "تحلیل دروازه‌بانی الگوریتمی.",
            "پژوهش تحریریهٔ دیجیتال.",
            "مطالعهٔ فیلترینگ محتوا.",
            "تحلیل انتخاب خبر در بحران.",
        ],
    ),
}

NAME_FIX = {}
YEAR_FIX = {
    "th-25": "year field normalised to Prospect Theory (1979); Persian-digit string replaced; life dates 1934-2024 stated in summary",
    "th-26": "year field normalised to Media Logic (1979); Persian-digit string replaced; birth year 1938 stated in summary",
    "th-29": "year field normalised to knowledge-gap article (1970); Persian-digit string replaced; life dates 1932-2010 stated in summary",
    "th-30": "year field normalised to The Gate Keeper (1950); life dates 1917-1993 stated in summary",
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
                                       "verified": n_verified, "batch": 172}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH172 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
