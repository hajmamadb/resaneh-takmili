# -*- coding: utf-8 -*-
"""Batch 166 (PERSON, agenda-setting genealogy): th-1 McCombs, th-2 Shaw, th-15 Lippmann, th-10 Lasswell."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch166-person-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch166_person.json"

S = {
    "th-1": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Agenda-Setting Function of Mass Media",
             title_fa="کارکرد برجسته‌سازی رسانه‌های جمعی",
             authors="McCombs, M. E.; Shaw, D. L.", year=1972,
             publisher="Public Opinion Quarterly",
             doi="10.1086/267990",
             url="https://academic.oup.com/poq/article-abstract/36/2/176/1853310",
             language="en", isbn=None,
             citation="McCombs, M. E., & Shaw, D. L. (1972). The agenda-setting function of mass media. Public Opinion Quarterly, 36(2), 176-187.",
             locator="36(2):176-187", locator_type="page_range",
             supports="Chapel Hill study: media issue salience predicts public issue salience", verified=True),
        dict(kind="BOOK",
             title_en="Setting the Agenda: The Mass Media and Public Opinion",
             title_fa="تعیین دستور کار: رسانه‌های جمعی و افکار عمومی",
             authors="McCombs, M. E.", year=2004,
             publisher="Polity Press",
             doi=None,
             url="https://archive.org/details/settingagendamas0000mcco",
             language="en", isbn=None,
             citation="McCombs, M. E. (2004). Setting the Agenda: The Mass Media and Public Opinion. Cambridge: Polity Press.",
             locator="2004 edition", locator_type="edition",
             supports="systematic statement of first- and second-level agenda setting", verified=True),
    ],
    "th-2": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Agenda-Setting Function of Mass Media",
             title_fa="کارکرد برجسته‌سازی رسانه‌های جمعی",
             authors="McCombs, M. E.; Shaw, D. L.", year=1972,
             publisher="Public Opinion Quarterly",
             doi="10.1086/267990",
             url="https://academic.oup.com/poq/article-abstract/36/2/176/1853310",
             language="en", isbn=None,
             citation="McCombs, M. E., & Shaw, D. L. (1972). The agenda-setting function of mass media. Public Opinion Quarterly, 36(2), 176-187.",
             locator="36(2):176-187", locator_type="page_range",
             supports="co-authored founding study of agenda-setting research", verified=True),
        dict(kind="BOOK",
             title_en="The Emergence of American Political Issues: The Agenda-Setting Function of the Press",
             title_fa="پیدایش مسائل سیاسی آمریکا: کارکرد برجسته‌سازی مطبوعات",
             authors="Shaw, D. L.; McCombs, M. E. (Eds.)", year=1977,
             publisher="West Publishing",
             doi=None,
             url="https://archive.org/details/emergenceofameri0000shaw",
             language="en", isbn="0829901426",
             citation="Shaw, D. L., & McCombs, M. E. (Eds.). (1977). The Emergence of American Political Issues: The Agenda-Setting Function of the Press. St. Paul, MN: West Publishing.",
             locator="1977 edition", locator_type="edition",
             supports="consolidation of the agenda-setting research program", verified=True),
    ],
    "th-15": [
        dict(kind="BOOK",
             title_en="Public Opinion",
             title_fa="افکار عمومی",
             authors="Lippmann, W.", year=1922,
             publisher="Harcourt, Brace",
             doi=None,
             url="https://archive.org/details/publicopinionhar0000walt",
             language="en", isbn=None,
             citation="Lippmann, W. (1922). Public Opinion. New York: Harcourt, Brace.",
             locator="1922 edition", locator_type="edition",
             supports="pictures in our heads, pseudo-environment and stereotypes", verified=True),
        dict(kind="BOOK",
             title_en="The Phantom Public",
             title_fa="افکار عمومی پنداری",
             authors="Lippmann, W.", year=1925,
             publisher="Harcourt, Brace",
             doi=None,
             url="https://archive.org/details/phantompublic0000walt",
             language="en", isbn=None,
             citation="Lippmann, W. (1925). The Phantom Public. New York: Harcourt, Brace.",
             locator="1925 edition", locator_type="edition",
             supports="critique of the omnicompetent citizen and the phantom public", verified=True),
    ],
    "th-10": [
        dict(kind="BOOK",
             title_en="Propaganda Technique in the World War",
             title_fa="فنون تبلیغات در جنگ جهانی",
             authors="Lasswell, H. D.", year=1927,
             publisher="Alfred A. Knopf",
             doi=None,
             url="https://archive.org/details/dli.ernet.233727",
             language="en", isbn=None,
             citation="Lasswell, H. D. (1927). Propaganda Technique in the World War. New York: Alfred A. Knopf.",
             locator="1927 edition", locator_type="edition",
             supports="early systematic analysis of wartime propaganda", verified=True),
        dict(kind="BOOK_CHAPTER",
             title_en="The Structure and Function of Communication in Society",
             title_fa="ساختار و کارکرد ارتباطات در جامعه",
             authors="Lasswell, H. D.", year=1948,
             publisher="Harper & Brothers",
             doi=None,
             url=None,
             language="en", isbn=None,
             citation="Lasswell, H. D. (1948). The structure and function of communication in society. In L. Bryson (Ed.), The Communication of Ideas (pp. 37-51). New York: Harper & Brothers.",
             locator="pp. 37-51", locator_type="page_range",
             supports="five-question model and three functions of communication", verified=True),
    ],
}

ENRICH = {
    "th-1": dict(
        year=1972,
        summary="ماکسول مک‌کامبز (زادهٔ ۱۹۳۸) پژوهشگر ارتباطات و پایه‌گذار نظریهٔ برجسته‌سازی است. او دکترای خود را در سال ۱۹۶۶ از دانشگاه استنفورد گرفت و در دانشگاه‌های سیراکیوز، کارولینای شمالی و تگزاس در آستین تدریس کرد. در سال ۱۹۶۸ همراه دونالد شاو در چپل هیل پژوهشی میدانی در جریان انتخابات ریاست‌جمهوری انجام داد و دید که رتبه‌بندی موضوعات مورد توجه رأی‌دهندگان با رتبه‌بندی پوشش خبری همان موضوعات همخوانی دارد. این پژوهش در سال ۱۹۷۲ در فصلنامهٔ افکار عمومی منتشر شد و به یکی از پراستنادترین مقاله‌های ارتباطات بدل گشت. مک‌کامبز در سال ۱۹۹۷ سطح دوم برجسته‌سازی را مطرح کرد: رسانه نه تنها برجستگی موضوع، بلکه برجستگی صفات و چارچوب‌های آن را نیز به افکار عمومی منتقل می‌کند. او در کتاب سال ۲۰۰۴ این برنامهٔ پژوهشی را نظام‌مند کرد و در دههٔ بعد با لی گوو سطح سوم شبکه را افزود. مک‌کامبز کرسی استادی ارتباطات را در تگزاس داشت و جایزهٔ یک عمر دستاورد را از انجمن جهانی پژوهش افکار عمومی گرفت. کار او نقطهٔ گذار از فرضیهٔ تأثیرات محدود به بازشناسی نقش رسانه در ساخت شناخت عمومی شمرده می‌شود.",
        definition="ماکسول مک‌کامبز بنیان‌گذار نظریهٔ برجسته‌سازی است که نشان می‌دهد رسانه با پررنگ کردن برخی موضوعات، اهمیت آن‌ها را به افکار عمومی منتقل می‌کند.",
        main_problem="آیا رسانه‌های جمعی تعیین می‌کنند مردم به چه چیزهایی فکر کنند و برجستگی موضوعات خبری چگونه به برجستگی موضوعات ذهنی شهروندان بدل می‌شود.",
        mechanism="رسانه با تکرار و برجسته‌سازی برخی موضوعات، دسترس‌پذیری آن‌ها در ذهن مخاطب را افزایش می‌دهد و معیار اهمیت‌سنجی عمومی را تغییر می‌دهد؛ این انتقال برجستگی در سطح موضوع و در سطح صفت رخ می‌دهد.",
        assumptions=[
            "خبرگزاری‌ها قادرند توجه عمومی را هدایت کنند.",
            "برجستگی رسانه‌ای با برجستگی عمومی همبسته است.",
            "مخاطب برای فهم سیاست به رسانه نیاز دارد.",
            "صفات در کنار موضوعات منتقل می‌شوند.",
            "شبکهٔ ارتباط موضوعات نیز برجسته می‌شود.",
            "نیاز به جهت‌یابی، شدت اثر را تعیین می‌کند.",
        ],
        principles=[
            "برجستگی را در دو سطح بسنج.",
            "معیار اهمیت‌سنجی عمومی را بساز.",
            "همبستگی را با دادهٔ پنلی تقویت کن.",
            "اثر رسانهٔ متفاوت را جدا تحلیل کن.",
            "نیاز به جهت‌یابی مخاطب را بگنجان.",
            "به پویایی رسانهٔ دیجیتال توجه کن.",
        ],
        critiques=[
            "همبستگی را با علیت اشتباه می‌گیرد.",
            "رسانه‌محور و کمی نخبه‌گراست.",
            "عوامل رقیب را کم می‌بیند.",
            "سنجش برجستگی ساده‌انگارانه است.",
            "به مخاطب فعال کم بها می‌دهد.",
            "به محتوای شبکه‌ای کمتر توجه دارد.",
            "تعمیم آن به رسانهٔ غیرآمریکایی محدود است.",
            "به رابطهٔ برجسته‌سازی و چارچوب‌بندی کم می‌پردازد.",
        ],
        critique_text="منتقدان برجسته‌سازی می‌گویند همبستگی دو فهرست، علیت را اثبات نمی‌کند و عوامل رقیب مانند تجربهٔ مستقیم و شبکهٔ اجتماعی کم‌شمرده می‌مانند؛ با این حال، برنامهٔ پژوهشی مک‌کامبز یکی از پرتکرارترین سنت‌های تجربی ارتباطات است.",
        applications=[
            "تحلیل دستور کار انتخابات.",
            "پژوهش سیاست‌گذاری سلامت.",
            "مطالعهٔ پوشش بحران.",
            "تحلیل دستور کار شبکه‌های اجتماعی.",
            "پژوهش ارتباطات توسعه.",
            "آموزش روزنامه‌نگاری.",
            "تحلیل کمپین انتخاباتی.",
            "مطالعهٔ مالکیت رسانه و تنوع موضوع.",
            "تحلیل برجسته‌سازی شبکه‌ای خبر.",
            "پژوهش افکار عمومی تطبیقی.",
        ],
        example_text="در سال ۱۹۶۸ رأی‌دهندگان چپل هیل موضوعاتی را مهم‌تر می‌دانستند که رسانه‌های محلی بیشتر دربارهٔ آن‌ها گزارش کرده بودند؛ همین هم‌خوانی، هستهٔ نخستین شاهد تجربی برجسته‌سازی شد.",
        evolution="پژوهش چپل هیل در سال ۱۹۶۸ طراحی و در سال ۱۹۷۲ منتشر شد؛ سطح دوم در سال ۱۹۹۷ با مطالعهٔ انتخابات اسپانیا گسترش یافت، کتاب سال ۲۰۰۴ برنامهٔ پژوهشی را نظام‌مند کرد و سطح سوم شبکه در دههٔ ۲۰۱۰ افزوده شد.",
        key_concepts=["برجسته‌سازی", "انتقال برجستگی", "دستور کار عمومی", "نیاز به جهت‌یابی", "برجسته‌سازی صفات", "برجسته‌سازی شبکه‌ای"],
        theorists="دانلد شاو، دیوید ویور و لی گوو.",
        theorists_text="برنامهٔ پژوهشی مک‌کامبز با همکاری شاو، ویور و گوو گسترش یافت.",
        model="انتقال برجستگی از دستور کار رسانه به دستور کار عمومی در سه سطح موضوع، صفت و شبکه.",
        studies=[
            "پژوهش چپل هیل در سال ۱۹۶۸.",
            "مقالهٔ سال ۱۹۷۲ در فصلنامهٔ افکار عمومی.",
            "مطالعهٔ سطح دوم در سال ۱۹۹۷.",
            "کتاب سال ۲۰۰۴ دربارهٔ دستور کار.",
            "پژوهش برجسته‌سازی شبکه‌ای سال ۲۰۱۱.",
            "مطالعهٔ تطبیقی افکار عمومی.",
        ],
    ),
    "th-2": dict(
        year=1972,
        summary="دانلد لوئیس شاو (زادهٔ ۱۹۳۶) روزنامه‌نگار و استاد ارتباطات دانشگاه کارولینای شمالی در چپل هیل بود که همراه ماکسول مک‌کامبز نظریهٔ برجسته‌سازی را بنیان گذاشت. او در سال ۱۹۶۸ در جریان انتخابات ریاست‌جمهوری، پژوهشی میدانی در چپل هیل طراحی کرد که در آن رأی‌دهندگان تازه‌وارد دربارهٔ موضوعات مهم و منابع خبری خود پرسیده شدند و پاسخ‌ها با محتوای رسانه‌های محلی مقایسه گردید. یافتهٔ مقالهٔ سال ۱۹۷۲ نشان داد که رسانه‌ها نه لزوماً چه بیندیشیم، بلکه دربارهٔ چه بیندیشیم را تعیین می‌کنند. شاو در کتاب سال ۱۹۷۷ همراه مک‌کامبز یافته‌های این برنامه را در قالب کارکرد برجسته‌سازی مطبوعات گرد آورد. او در دهه‌های بعد برجسته‌سازی را به آگاهی سیاسی، رفتار رأی‌دهی و انتخابات محلی گستراند و به آموزش روزنامه‌نگاری و ارتباطات مدنی علاقه داشت. سهم او در نظریه، پیوند دادن شواهد تجربی با پرسش هنجاری دربارهٔ نقش مطبوعات در دموکراسی بود. نقدهای اصلی به این سنت، همبستگی به‌جای علیت، رسانه‌محوری و کم‌توجهی به عوامل ساختاری را برجسته می‌کنند.",
        definition="دانلد شاو پژوهشگر ارتباطات و هم‌بنیان‌گذار برجسته‌سازی است که با پژوهش میدانی چپل هیل نشان داد دستور کار رسانه به دستور کار عمومی منتقل می‌شود.",
        main_problem="مطبوعات چگونه بر آنچه شهروندان مهم می‌دانند اثر می‌گذارند و این اثر در جریان یک کارزار انتخاباتی چگونه قابل مشاهده است.",
        mechanism="مخاطبان برای فهم موضوعات دور از تجربهٔ روزمره به خبر وابسته‌اند؛ تکرار و جایگاه خبری، دسترس‌پذیری موضوع در حافظه را بالا می‌برد و معیار اهمیت رأی‌دهنده را می‌سازد.",
        assumptions=[
            "رسانه منبع اصلی شناخت سیاسی است.",
            "رأی‌دهندگان تازه‌وارد وابسته‌ترند.",
            "برجستگی خبر با اهمیت ادراکی همبسته است.",
            "کارزار انتخاباتی زمان مناسب آزمون است.",
            "مطبوعات محلی نمایندهٔ دستور کارند.",
            "اثر برجسته‌سازی کوتاه‌مدت نیست.",
        ],
        principles=[
            "دادهٔ پیمایشی را با تحلیل محتوا پیوند بزن.",
            "رأی‌دهندگان تازه‌وارد را جدا تحلیل کن.",
            "منابع خبری پاسخ‌دهندگان را ثبت کن.",
            "رسانهٔ محلی و ملی را مقایسه کن.",
            "کارکرد مطبوعات را در دموکراسی ببین.",
            "آموزش روزنامه‌نگاری را جدی بگیر.",
        ],
        critiques=[
            "همبستگی، علیت نیست.",
            "رسانه‌محوری در آن دیده می‌شود.",
            "به تجربهٔ مستقیم کم توجه است.",
            "به شبکهٔ اجتماعی رأی‌دهنده کم می‌پردازد.",
            "سنجش اهمیت ادراکی ساده است.",
            "به تغییرات رسانهٔ دیجیتال کم توجه دارد.",
            "به قدرت رسانهٔ محلی کمتر می‌پردازد.",
            "به رسانهٔ تلویزیونی کمتر می‌پردازد.",
            "تعمیم آن به نظام‌های دیگر محدود است.",
        ],
        critique_text="منتقدان می‌گویند پژوهش چپل هیل رابطهٔ همبستگی را نشان داد نه علیت را و عوامل رقیب را کم‌شمرد، اما طراحی آن استانداردی برای پژوهش تجربی برجسته‌سازی ساخت.",
        applications=[
            "تحلیل انتخابات محلی.",
            "پژوهش آگاهی سیاسی.",
            "مطالعهٔ مطبوعات محلی.",
            "آموزش روزنامه‌نگاری.",
            "تحلیل ارتباطات مدنی.",
            "پژوهش رفتار رأی‌دهی.",
            "مطالعهٔ منابع خبری شهروندان.",
            "تحلیل کمپین انتخاباتی.",
            "پژوهش روزنامه‌نگاری و دموکراسی.",
            "مطالعهٔ دستور کار رسانهٔ منطقه‌ای.",
            "تحلیل پوشش خبری انتخابات ریاست‌جمهوری.",
            "پژوهش مطبوعات محلی و مشارکت رأی‌دهنده.",
            "مطالعهٔ دستور کار در رسانهٔ منطقه‌ای.",
            "تحلیل کمپین روزنامه‌ای.",
            "پژوهش ارتباطات مدنی و اعتماد.",
        ],
        example_text="در پژوهش چپل هیل، رأی‌دهندگان تازه‌وارد موضوعاتی را مهم می‌دانستند که روزنامه‌های محلی بیشتر پوشش داده بودند؛ شاو این هم‌خوانی را شاهد کارکرد برجسته‌سازی مطبوعات دانست.",
        evolution="شاو پژوهش چپل هیل را در سال ۱۹۶۸ طراحی کرد و در سال ۱۹۷۲ با مک‌کامبز منتشر ساخت؛ کتاب سال ۱۹۷۷ برنامه را تثبیت کرد و پژوهش‌های بعدی او برجسته‌سازی را به آگاهی سیاسی و انتخابات محلی گسترد.",
        key_concepts=["برجسته‌سازی", "چپل هیل", "آگاهی سیاسی", "دستور کار مطبوعات", "رأی‌دهندهٔ تازه‌وارد", "ارتباطات مدنی"],
        theorists="ماکسول مک‌کامبز و دیوید ویور.",
        theorists_text="شاو بیشتر با مک‌کامبز و در سنت پژوهشی کارولینای شمالی کار کرد.",
        model="مطبوعات به‌عنوان تعیین‌کنندهٔ دستور کار عمومی در کارزار انتخاباتی.",
        studies=[
            "پژوهش میدانی چپل هیل سال ۱۹۶۸.",
            "مقالهٔ مشترک سال ۱۹۷۲.",
            "کتاب سال ۱۹۷۷ دربارهٔ مسائل سیاسی.",
            "مطالعهٔ انتخابات محلی.",
            "پژوهش آگاهی سیاسی رأی‌دهندگان.",
            "مطالعهٔ مطبوعات محلی و مشارکت.",
            "مطالعهٔ برجسته‌سازی در انتخابات میاندوره‌ای.",
            "پژوهش روزنامه‌نگاری محلی و آگاهی.",
            "تحلیل دادهٔ پیمایشی چپل هیل.",
        ],
    ),
    "th-15": dict(
        year=1922,
        summary="والتر لیپمن (۱۸۸۹-۱۹۷۴) روزنامه‌نگار، نویسنده و نظریه‌پرداز آمریکایی است که با کتاب افکار عمومی در سال ۱۹۲۲ پایهٔ بحث مدرن دربارهٔ تأثیر رسانه بر شناخت را گذاشت. او استدلال کرد که انسان‌ها با جهان واقعی بی‌واسطه روبه‌رو نمی‌شوند، بلکه با تصاویری در ذهن خود عمل می‌کنند که «تصاویر در سر ما» نام گرفت. این تصاویر از کلیشه‌ها ساخته می‌شوند و محیط شبه‌واقعی می‌سازند که رفتار عمومی بر پایهٔ آن شکل می‌گیرد. لیپمن در کتاب افکار عمومی پنداری در سال ۱۹۲۵ تیزتر گفت که شهروند عادی نمی‌تواند در همهٔ مسائل عمومی متخصص باشد و شهروندی که همه‌چیز را می‌داند، پنداری بیش نیست. او به جای دموکراسی مستقیم، حکومت خبرگان و نهادهای واسط را پیشنهاد کرد و اصطلاح ساخت رضایت را در نقد دموکراسی جاری ساخت. پژوهش برجسته‌سازی، چارچوب‌بندی و کلیشه‌سازی رسانه‌ای همه خود را وامدار او می‌دانند. نقدهای اصلی به او، نخبه‌گرایی، کم‌بها دادن به توان شهروند و نگاه نسبتاً منفعل به مخاطب را برجسته می‌کنند.",
        definition="والتر لیپمن بنیان‌گذار بحث مدرن دربارهٔ تصاویر ذهنی و افکار عمومی است که نشان داد شهروندان بر پایهٔ کلیشه‌ها و محیط شبه‌واقعی تصمیم می‌گیرند.",
        main_problem="چرا شهروندان در دموکراسی توده‌ای تصویری نادرست و ساده‌شده از جهان دارند و رسانه در ساخت این تصویر چه نقشی بازی می‌کند.",
        mechanism="رسانه روایت‌هایی گزینشی از جهان دور می‌سازد؛ این روایت‌ها کلیشه‌های ذهنی را تقویت می‌کنند و شهروند بر پایهٔ محیط شبه‌واقعی، نه واقعیت مستقیم، داوری و رفتار می‌کند.",
        assumptions=[
            "انسان با تصاویر ذهنی عمل می‌کند.",
            "جهان دور از تجربه، مستقیم شناخته نمی‌شود.",
            "کلیشه‌ها ادراک را ساده می‌کنند.",
            "رسانه تصویر جهان را می‌سازد.",
            "شهروند در همهٔ مسائل متخصص نیست.",
            "افکار عمومی آسیب‌پذیر است.",
        ],
        principles=[
            "تصویر ذهنی را از واقعیت جدا کن.",
            "کلیشه را در تحلیل محتوا رصد کن.",
            "رسانه را واسط شناخت بدان.",
            "ظرفیت شناختی شهروند را واقع‌بینانه بسنج.",
            "به نهادهای واسط توجه کن.",
            "نقد نخبه‌گرایی را جدی بگیر.",
        ],
        critiques=[
            "نخبه‌گرا و ضددمکراتیک خوانده شده است.",
            "شهروند را بیش از اندازه منفعل می‌بیند.",
            "به توان یادگیری عمومی کم بها می‌دهد.",
            "کلیشه را ایستا فرض می‌کند.",
            "به تنوع رسانه کم توجه است.",
            "به مقاومت مخاطب نمی‌پردازد.",
            "نقش تجربهٔ مستقیم را کم می‌بیند.",
            "به رسانهٔ دیجیتال کم توجه است.",
            "به تجربهٔ زیستهٔ شهروند کم بها می‌دهد.",
            "راه‌حل خبره‌محور او مناقشه‌برانگیز است.",
        ],
        critique_text="منتقدان لیپمن می‌گویند نگاه او به شهروند تحقیرآمیز و راه‌حل خبره‌محور او نخبه‌گرایانه است؛ با این حال، تشخیص او دربارهٔ واسطه‌گری تصاویر ذهنی، بنیان پژوهش تأثیر رسانه شد.",
        applications=[
            "تحلیل کلیشه در خبر.",
            "پژوهش افکار عمومی.",
            "مطالعهٔ تصویر ذهنی ملت‌ها.",
            "تحلیل تبلیغات سیاسی.",
            "پژوهش چارچوب‌بندی خبر.",
            "آموزش سواد رسانه‌ای.",
            "تحلیل تصویرسازی بحران.",
            "مطالعهٔ ادراک سیاست خارجی.",
            "پژوهش رسانه و دموکراسی.",
            "تحلیل کلیشه‌های قومی در رسانه.",
            "تحلیل گفتار دیویی و لیپمن.",
            "پژوهش کلیشه در سینما.",
            "مطالعهٔ تصویر مهاجران در خبر.",
            "تحلیل تبلیغات جنگ.",
            "پژوهش ادراک عمومی از سیاست.",
        ],
        example_text="شهروندی که هرگز یک کشور دور را ندیده است، دربارهٔ مردم آن کشور بر پایهٔ کلیشه‌های خبری داوری می‌کند؛ لیپمن این داوری را نتیجهٔ محیط شبه‌واقعی می‌دانست، نه مشاهدهٔ مستقیم.",
        evolution="لیپمن در سال ۱۹۲۲ افکار عمومی را منتشر کرد و در سال ۱۹۲۵ با افکار عمومی پنداری نقد دموکراسی توده‌ای را تیزتر کرد؛ پژوهش برجسته‌سازی و چارچوب‌بندی در نیمهٔ دوم قرن بیستم او را پیشگام خود خواندند.",
        key_concepts=["تصاویر در سر ما", "محیط شبه‌واقعی", "کلیشه", "افکار عمومی", "ساخت رضایت", "شهروند ناظر"],
        theorists="جان دیویی و ادوارد برنیز.",
        theorists_text="لیپمن در گفت‌وگوی انتقادی با جان دیویی و در بافت تبلیغات دورهٔ جنگ اول نوشت.",
        model="شهروند به‌عنوان ناظری که بر پایهٔ تصاویر رسانه‌ای، نه واقعیت مستقیم، داوری می‌کند.",
        studies=[
            "کتاب افکار عمومی سال ۱۹۲۲.",
            "کتاب افکار عمومی پنداری سال ۱۹۲۵.",
            "مناظرهٔ لیپمن و دیویی در دههٔ ۱۹۲۰.",
            "پژوهش کلیشه در ارتباطات.",
            "مطالعهٔ تصویر ملت‌ها در خبر.",
            "پژوهش رسانه و ادراک سیاست خارجی.",
            "مطالعهٔ ادراک بحران بین‌المللی.",
        ],
    ),
    "th-10": dict(
        year=1948,
        summary="هارولد لاسول (۱۹۰۲-۱۹۷۸) دانشمند علوم سیاسی و ارتباطات آمریکایی است که پایه‌های تحلیل محتوا، پژوهش تبلیغات و مدل انتقالی ارتباطات را گذاشت. او دکترای خود را در سال ۱۹۲۶ از دانشگاه شیکاگو گرفت و در کتاب فنون تبلیغات در جنگ جهانی در سال ۱۹۲۷ نشان داد که تبلیغات جنگی با نمادسازی هدفمند، وفاداری و دشمن‌سازی را مدیریت می‌کند. لاسول در سال ۱۹۴۸ در فصل ساختار و کارکرد ارتباطات در جامعه، ارتباط را با پنج پرسش صورت‌بندی کرد: چه کسی، چه می‌گوید، در چه مجرایی، به چه کسی و با چه اثری. او سه کارکرد برای ارتباطات برشمرد: نظارت بر محیط، همبستگی بخش‌های جامعه و انتقال میراث اجتماعی. لاسول ارتباطات را ابزار مدیریت اجتماعی می‌دانست و به همین دلیل، پژوهش او دربارهٔ تبلیغات و نمادها با پرسش قدرت گره خورد. او در کتاب سیاست: چه کسی چه چیزی را، چه زمانی و چگونه به دست می‌آورد، تحلیل قدرت را با توزیع ارزش‌ها پیوند داد. نقدهای اصلی به مدل او، خطی بودن، غفلت از بازخورد و معناسازی مخاطب و نگاه ابزاری به ارتباط را برجسته می‌کنند.",
        definition="هارولد لاسول بنیان‌گذار تحلیل محتوا و صورت‌بند مدل پنج‌پرسشی ارتباط است که ارتباط را به‌عنوان ابزار مدیریت نمادها و قدرت تحلیل کرد.",
        main_problem="تبلیغات و ارتباطات جمعی چگونه نمادها را مدیریت می‌کنند و ارتباط چه کارکردهایی برای بقا و نظم جامعه دارد.",
        mechanism="فرستنده با انتخاب نمادها و مجرا، توجه و وفاداری گیرنده را شکل می‌دهد؛ ارتباط با نظارت، همبستگی و انتقال میراث، جامعه را در برابر محیط تنظیم می‌کند.",
        assumptions=[
            "ارتباط با نمادها عمل می‌کند.",
            "تبلیغات مدیریت نمادین است.",
            "اثر ارتباط قابل سنجش است.",
            "ارتباط کارکرد نظارتی دارد.",
            "جامعه به همبستگی نمادین نیاز دارد.",
            "قدرت با توزیع ارزش‌ها گره دارد.",
        ],
        principles=[
            "پنج پرسش ارتباط را جدا تحلیل کن.",
            "محتوا را نظام‌مند کدگذاری کن.",
            "کارکرد اجتماعی پیام را ببین.",
            "نماد و قدرت را به هم پیوند بزن.",
            "بازخورد را به مدل بیفزا.",
            "معناسازی مخاطب را جدی بگیر.",
        ],
        critiques=[
            "مدل او خطی و یک‌سویه است.",
            "بازخورد را نادیده می‌گیرد.",
            "معناسازی مخاطب را کم می‌بیند.",
            "نگاه ابزاری به ارتباط دارد.",
            "به زمینهٔ فرهنگی کم توجه است.",
            "اثر را ساده می‌سنجد.",
            "تبلیغات را بیش از اندازه تعیین‌کننده می‌داند.",
            "به نقش مخاطب فعال کم توجه است.",
            "به سکوت و مقاومت پیام نمی‌پردازد.",
            "به مقاومت گیرنده نمی‌پردازد.",
        ],
        critique_text="منتقدان مدل لاسول را خطی و فرستنده‌محور می‌دانند که بازخورد و تفسیر مخاطب را کم‌رنگ می‌کند؛ با این حال، پنج پرسش او چارچوب آموزش و پژوهش ارتباطات را برای دهه‌ها ساخت.",
        applications=[
            "تحلیل محتوای تبلیغات.",
            "پژوهش تبلیغات سیاسی.",
            "آموزش مدل ارتباط.",
            "تحلیل کارکرد خبر.",
            "مطالعهٔ پروپاگاندا.",
            "تحلیل پیام جنگ.",
            "پژوهش ارتباطات توسعه.",
            "سنجش اثر کمپین.",
            "تحلیل نمادهای قدرت.",
            "آموزش روش تحلیل محتوا.",
            "تحلیل محتوای سخنرانی سیاسی.",
            "پژوهش تبلیغات رادیویی.",
            "مطالعهٔ نمادسازی در خبر.",
            "تحلیل پیام صلح.",
            "پژوهش ارتباطات سلامت.",
            "تحلیل پیام دیپلماتیک.",
        ],
        example_text="در تحلیل یک کمپین جنگی، پژوهشگر با پنج پرسش لاسول فرستنده، پیام، مجرا، مخاطب و اثر را جدا می‌کند و سپس نمادهای دشمن‌سازی را در محتوا می‌شمارد.",
        evolution="لاسول در سال ۱۹۲۷ تبلیغات جنگی را تحلیل کرد و در سال ۱۹۴۸ مدل پنج‌پرسشی و سه کارکرد را صورت‌بندی کرد؛ پس از او، تحلیل محتوا و پژوهش اثر، مدل را بازبینی و بازخورد را به آن افزودند.",
        key_concepts=["مدل پنج‌پرسشی", "تحلیل محتوا", "تبلیغات", "نظارت محیط", "همبستگی جامعه", "انتقال میراث"],
        theorists="چارلز مریام و برنارد برلسون.",
        theorists_text="لاسول در سنت مکتب شیکاگو و پژوهش تبلیغات جنگ کار کرد.",
        model="ارتباط به‌عنوان زنجیرهٔ فرستنده، پیام، مجرا، گیرنده و اثر با سه کارکرد اجتماعی.",
        studies=[
            "کتاب تبلیغات جنگی سال ۱۹۲۷.",
            "فصل ساختار و کارکرد سال ۱۹۴۸.",
            "کتاب سیاست سال ۱۹۳۶.",
            "پژوهش تحلیل محتوا در جنگ جهانی دوم.",
            "مطالعهٔ نمادهای قدرت.",
            "پژوهش ارتباطات توسعه.",
            "مطالعهٔ محتوای رادیو جنگ.",
            "پژوهش تبلیغات انتخاباتی.",
            "تحلیل کارکرد خبر در بحران.",
        ],
    ),
}

NAME_FIX = {}
YEAR_FIX = {
    "th-1": "year field denotes the landmark 1972 publication; birth year (1938) stated in summary",
    "th-2": "year field denotes the landmark 1972 publication; birth year (1936) stated in summary",
    "th-15": "year field denotes Public Opinion (1922); life dates 1889-1974 stated in summary",
    "th-10": "year field denotes the 1948 five-question formulation; life dates 1902-1978 stated in summary",
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
                                       "verified": n_verified, "batch": 166}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH166 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
