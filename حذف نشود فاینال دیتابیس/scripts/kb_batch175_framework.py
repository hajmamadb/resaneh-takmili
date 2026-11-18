# -*- coding: utf-8 -*-
"""Batch 175 (WORK): MC-109 sleeper effect, MC-110 illusory truth, MC-211 CNN effect, MC-246 online disinhibition."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch175-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch175.json"

WORK_MAPPING = {"entity_type": "WORK", "content_type": "اثر رسانه‌ای (پدیده)", "needs_review": False}

S = {
    "MC-109": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Influence of Source Credibility on Communication Effectiveness",
             title_fa="تأثیر اعتبار منبع بر اثربخشی ارتباط",
             authors="Hovland, C. I., & Weiss, W.", year=1951,
             publisher="Public Opinion Quarterly, 15(4), 635-650",
             doi="10.1086/266350",
             url="https://doi.org/10.1086/266350",
             language="en", isbn=None,
             citation="Hovland, C. I., & Weiss, W. (1951). The influence of source credibility on communication effectiveness. Public Opinion Quarterly, 15(4), 635-650.",
             locator="15(4), pp. 635-650", locator_type="page_range",
             supports="origin formulation of the sleeper effect in source credibility experiments", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Sleeper Effect in Persuasion: A Meta-Analytic Review",
             title_fa="اثر خواب‌آلود در اقناع: مروری فراتحلیلی",
             authors="Kumkale, G. T., & Albarracín, D.", year=2004,
             publisher="Psychological Bulletin, 130(1), 143-172",
             doi="10.1037/0033-2909.130.1.143",
             url="https://doi.org/10.1037/0033-2909.130.1.143",
             language="en", isbn=None,
             citation="Kumkale, G. T., & Albarracín, D. (2004). The sleeper effect in persuasion: A meta-analytic review. Psychological Bulletin, 130(1), 143-172.",
             locator="130(1), pp. 143-172", locator_type="page_range",
             supports="meta-analytic evidence and boundary conditions of the effect", verified=True),
    ],
    "MC-110": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Frequency and the Conference of Referential Validity",
             title_fa="بسامد و اعتبار ارجاعی",
             authors="Hasher, L., Goldstein, D., & Toppino, T.", year=1977,
             publisher="Journal of Verbal Learning and Verbal Behavior, 16(1), 107-112",
             doi="10.1016/S0022-5371(77)80012-1",
             url="https://doi.org/10.1016/S0022-5371(77)80012-1",
             language="en", isbn=None,
             citation="Hasher, L., Goldstein, D., & Toppino, T. (1977). Frequency and the conference of referential validity. Journal of Verbal Learning and Verbal Behavior, 16(1), 107-112.",
             locator="16(1), pp. 107-112", locator_type="page_range",
             supports="first experimental demonstration of the illusory truth effect", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Truth About the Truth: A Meta-Analytic Review of the Truth Effect",
             title_fa="حقیقت دربارهٔ حقیقت: مرور فراتحلیلی اثر حقیقت",
             authors="Dechêne, A., Stahl, C., Hansen, J., & Wänke, M.", year=2010,
             publisher="Personality and Social Psychology Review, 14(2), 238-257",
             doi="10.1177/1088868309352251",
             url="https://doi.org/10.1177/1088868309352251",
             language="en", isbn=None,
             citation="Dechêne, A., Stahl, C., Hansen, J., & Wänke, M. (2010). The truth about the truth: A meta-analytic review of the truth effect. Personality and Social Psychology Review, 14(2), 238-257.",
             locator="14(2), pp. 238-257", locator_type="page_range",
             supports="meta-analysis of 51 studies on repetition-induced truth", verified=True),
    ],
    "MC-211": [
        dict(kind="BOOK",
             title_en="The CNN Effect: The Myth of News, Foreign Policy and Intervention",
             title_fa="اثر سی‌ان‌ان: اسطورهٔ خبر، سیاست خارجی و مداخله",
             authors="Robinson, P.", year=2002,
             publisher="Routledge",
             doi="10.4324/9780203995037",
             url="https://doi.org/10.4324/9780203995037",
             language="en", isbn="9780415259057",
             citation="Robinson, P. (2002). The CNN Effect: The Myth of News, Foreign Policy and Intervention. London: Routledge.",
             locator="2002 edition", locator_type="edition",
             supports="policy-media interaction model and case evidence", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="The CNN Effect: The Search for a Communication Theory of International Relations",
             title_fa="اثر سی‌ان‌ان: جست‌وجوی نظریهٔ ارتباطات روابط بین‌الملل",
             authors="Gilboa, E.", year=2005,
             publisher="Political Communication, 22(1), 27-44",
             doi="10.1080/10584600590908429",
             url="https://doi.org/10.1080/10584600590908429",
             language="en", isbn=None,
             citation="Gilboa, E. (2005). The CNN effect: The search for a communication theory of international relations. Political Communication, 22(1), 27-44.",
             locator="22(1), pp. 27-44", locator_type="page_range",
             supports="theoretical review and conditions for media influence on foreign policy", verified=True),
    ],
    "MC-246": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Online Disinhibition Effect",
             title_fa="اثر بی‌بازداری آنلاین",
             authors="Suler, J.", year=2004,
             publisher="CyberPsychology & Behavior, 7(3), 321-326",
             doi="10.1089/1094931041291295",
             url="https://doi.org/10.1089/1094931041291295",
             language="en", isbn=None,
             citation="Suler, J. (2004). The online disinhibition effect. CyberPsychology & Behavior, 7(3), 321-326.",
             locator="7(3), pp. 321-326", locator_type="page_range",
             supports="six-factor framework of online disinhibition", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Effects of anonymity, invisibility, and lack of eye-contact on toxic online disinhibition",
             title_fa="اثر ناشناسی، ناپیدایی و نبود تماس چشمی بر بی‌بازداری زیان‌بار آنلاین",
             authors="Lapidot-Lefler, N., & Barak, A.", year=2012,
             publisher="Computers in Human Behavior, 28(2), 434-443",
             doi="10.1016/j.chb.2011.10.014",
             url="https://doi.org/10.1016/j.chb.2011.10.014",
             language="en", isbn=None,
             citation="Lapidot-Lefler, N., & Barak, A. (2012). Effects of anonymity, invisibility, and lack of eye-contact on toxic online disinhibition. Computers in Human Behavior, 28(2), 434-443.",
             locator="28(2), pp. 434-443", locator_type="page_range",
             supports="experimental isolation of eye-contact as a driver of toxic disinhibition", verified=True),
    ],
}

ENRICH = {
    "MC-109": dict(
        year=1951,
        mapping=WORK_MAPPING,
        summary="اثر خواب‌آلود افزایش تأخیری اقناع است: پیامی که در آغاز به سبب منبع نامعتبر رد یا کم‌اثر می‌شود، پس از گذشت زمان اثر بیشتری می‌گذارد. این پدیده نخست در پژوهش هولاند و همکارانش دربارهٔ فیلم‌های تبلیغاتی ارتش آمریکا در جنگ جهانی دوم دیده شد؛ تفاوت نگرش سربازان نه هفته پس از نمایش فیلم بیشتر از پنج روز بعد بود. هولاند و ویس در سال ۱۹۵۱ در مطالعهٔ اعتبار منبع نشان دادند پیام منبع نامعتبر در آغاز کمتر اقناع می‌کند، اما با فاصله گرفتن از منبع اثر آن افزایش می‌یابد. تبیین اصلی، جدا شدن سرنخ تخفیف‌دهنده از محتوا در حافظه و افول سریع‌تر اثر منبع نسبت به پیام است. متاآنالیز کومکال و آلباریسین در سال ۲۰۰۴ نشان داد اثر تنها در شرایط مشخص، مانند تأثیر اولیهٔ قوی پیام و ارائهٔ سرنخ پس از پیام، رخ می‌دهد. نقدهای اصلی بر ناپایداری تکرارپذیری، اندازهٔ کوچک اثر و تکیه بر آزمایش کوتاه‌مدت تأکید دارند.",
        definition="اثر خواب‌آلود افزایش اقناع پیام در طول زمان است، هنگامی که سرنخ تخفیف‌دهنده مانند منبع نامعتبر از محتوا در حافظه جدا می‌شود.",
        main_problem="چرا پیامی که به سبب منبع نامعتبر در آغاز کم‌اثر است، بعدها اثر بیشتری بر نگرش می‌گذارد و این تأخیر چگونه تبیین می‌شود.",
        mechanism="گیرنده در آغاز پیام و سرنخ نامعتبر را با هم رمزگذاری می‌کند و سرنخ اثر پیام را سرکوب می‌کند؛ با گذشت زمان پیوند سرنخ و محتوا ضعیف می‌شود، محتوا در حافظه می‌ماند و اثر منبع سریع‌تر افول می‌کند، در نتیجه نگرش به سمت موضع پیام حرکت می‌کند.",
        assumptions=[
            "سرنخ تخفیف‌دهنده اثر پیام را در آغاز سرکوب می‌کند.",
            "پیام و سرنخ جداگانه در حافظه رمزگذاری می‌شوند.",
            "پیوند سرنخ و محتوا با زمان ضعیف می‌شود.",
            "اثر منبع سریع‌تر از محتوای پیام افول می‌کند.",
            "تأثیر اولیهٔ پیام باید به اندازهٔ کافی قوی باشد.",
            "جای سرنخ نسبت به پیام اهمیت دارد.",
            "پردازش عمیق پیام ماندگاری را افزایش می‌دهد.",
            "نگرش پس از تأخیر دوباره سنجیده می‌شود.",
        ],
        principles=[
            "سرنخ و محتوا را جداگانه بسنج.",
            "سنجش نگرش را در دو زمان انجام بده.",
            "قوت تأثیر اولیهٔ پیام را کنترل کن.",
            "جای سرنخ را در پیام مشخص کن.",
            "حافظهٔ منبع و پیام را اندازه بگیر.",
            "افول اثر را الگومند تحلیل کن.",
            "از تعمیم آزمایشگاهی بی‌هنگام بپرهیز.",
        ],
        critiques=[
            "تکرارپذیری اثر در پژوهش‌های بعدی ضعیف بود.",
            "شرایط مرزی اثر به‌سادگی فراهم نمی‌شود.",
            "سنجش حافظه در طرح‌ها ناهمگون است.",
            "تفکیک فراموشی و جدایی مفهومی دشوار است.",
            "بیشتر شواهد آزمایشگاهی و کوتاه‌مدت است.",
            "اثر اندازهٔ کوچکی دارد.",
            "تعمیم به رسانهٔ واقعی محدود است.",
            "نقش احساس و هویت کم دیده شده است.",
            "تفاوت فردی در پردازش کم سنجیده شده است.",
            "سنجش نگرش در فواصل گوناگون مقایسه‌پذیر نیست.",
        ],
        critique_text="منتقدان می‌گویند اثر خواب‌آلود بیش از آنکه قانونی عمومی باشد، پدیده‌ای وابسته به شرایط است: اندازهٔ اثر کوچک است، تکرارپذیری ضعیف بوده و بیشتر شواهد از آزمایش کوتاه‌مدت می‌آید؛ با این حال متاآنالیز ۲۰۰۴ نشان داد اثر در شرایط نظری مشخص واقعی است.",
        applications=[
            "تحلیل تبلیغات با منبع نامعتبر.",
            "پژوهش رسوایی سیاسی.",
            "مطالعهٔ اصلاح شایعه.",
            "تحلیل کمپین سلامت.",
            "پژوهش تبلیغات تجاری.",
            "مطالعهٔ بحران اعتماد به برند.",
            "تحلیل پیام انتخاباتی.",
            "پژوهش اقناع در رسانه.",
            "مطالعهٔ فراخوان محصول.",
            "تحلیل تأخیر در تغییر نگرش.",
            "پژوهش رسانه و افکار عمومی.",
            "مطالعهٔ ارتباطات بحران.",
        ],
        example_text="آگهی‌ای که شرکت سازندهٔ آن به فساد مالی متهم است در هفتهٔ نخست کم‌اثر می‌ماند، اما چند ماه بعد مصرف‌کنندگان نگرش مثبت‌تری به محصول نشان می‌دهند، زیرا نام شرکت از پیام جدا شده و محتوای آگهی در حافظه مانده است.",
        evolution="هولاند و همکاران در سال ۱۹۴۹ اثر را در فیلم‌های آموزشی ارتش دیدند و هولاند و ویس در ۱۹۵۱ با مطالعهٔ اعتبار منبع آن را صورت‌بندی کردند. ویس در ۱۹۵۳ اصطلاح را تثبیت کرد؛ پراتکانیس و گرینوالد در ۱۹۸۸ با هفده آزمایش شرط‌های اثر را روشن کردند و کومکال و آلباریسین در ۲۰۰۴ با متاآنالیز شواهد را نظام‌مند کردند.",
        key_concepts=["سرنخ تخفیف‌دهنده", "جدایی در حافظه", "افول افتراقی", "اقناع تأخیری", "اعتبار منبع", "اثر خواب‌آلود مطلق"],
        theorists="کارل هولاند، والتر ویس و آنتونی پراتکانیس.",
        theorists_text="هولاند در سنت پژوهش اقناع دانشگاه ییل اثر را کشف کرد و پژوهش‌های بعدی آن را به نظریهٔ حافظه و نگرش پیوند دادند.",
        model="مدل افول افتراقی: اثر پیام و سرنخ با سرعت‌های متفاوت افت می‌کند و موازنهٔ آن‌ها نگرش نهایی را می‌سازد.",
        studies=[
            "پژوهش فیلم‌های آموزشی ارتش در سال ۱۹۴۹.",
            "مطالعهٔ اعتبار منبع در سال ۱۹۵۱.",
            "پژوهش ویس دربارهٔ اثر خواب‌آلود در ۱۹۵۳.",
            "آزمایش‌های پراتکانیس در ۱۹۸۸.",
            "متاآنالیز کومکال و آلباریسین در ۲۰۰۴.",
            "پژوهش جای سرنخ در پیام.",
            "مطالعهٔ حافظهٔ منبع.",
            "تحلیل اقناع تأخیری.",
            "پژوهش تبلیغات منفی.",
            "مطالعهٔ نگرش و زمان.",
            "تحلیل افول اثر پیام.",
            "پژوهش شرایط مرزی اثر.",
        ],
    ),
    "MC-110": dict(
        year=1977,
        mapping=WORK_MAPPING,
        summary="اثر حقیقت‌نمایی یا اثر تکرار، سوگیری شناختی است که در آن تکرار یک گزاره باور به درستی آن را افزایش می‌دهد، حتی اگر گزاره نادرست باشد. هشر، گلدستاین و توپینو در سال ۱۹۷۷ با آزمون شصت گزاره نشان دادند گزاره‌هایی که پیش‌تر تکرار شده‌اند درست‌تر از گزاره‌های تازه ارزیابی می‌شوند. تبیین رایج، روانی پردازش است: تکرار پردازش گزاره را آسان‌تر می‌کند و این سهولت به اشتباه نشانهٔ درستی گرفته می‌شود. پژوهش بعدی نشان داد اثر حتی با دانش پیشین و هشدار دربارهٔ فریب از میان نمی‌رود و در رسانه و تبلیغات سیاسی اهمیت دارد. متاآنالیز دشنه و همکاران در سال ۲۰۱۰ با ۵۱ مطالعه اندازه و تعدیل‌گرهای اثر را نظام‌مند کرد. نقدها بر اندازهٔ کوچک اثر، استفاده از گزاره‌های عمومی و شرایط آزمایشگاهی متمرکزند.",
        definition="اثر حقیقت‌نمایی افزایش باور به درستی یک گزاره در نتیجهٔ تکرار پیشین آن است، مستقل از صدق واقعی گزاره.",
        main_problem="چرا تکرار یک گزاره، حتی گزارهٔ نادرست، آن را درست‌تر جلوه می‌دهد و این سوگیری چگونه در قضاوت روزمره عمل می‌کند.",
        mechanism="تکرار دسترسی و روانی پردازش گزاره را بالا می‌برد؛ فرد سهولت پردازش را به درستی نسبت می‌دهد و میان آشنایی و صدق تمایز نمی‌گذارد، در نتیجه گزارهٔ آشنا درست‌تر ارزیابی می‌شود.",
        assumptions=[
            "آشنایی با گزاره با تکرار افزایش می‌یابد.",
            "روانی پردازش نشانهٔ صدق تلقی می‌شود.",
            "قضاوت درستی به یادآوری منبع وابسته نیست.",
            "اثر برای گزارهٔ نادرست هم رخ می‌دهد.",
            "دانش پیشین محافظ کامل نیست.",
            "اثر در قضاوت سریع آشکارتر است.",
            "تکرار آشکار و پنهان هر دو اثر دارند.",
            "میزان اثر به فاصلهٔ زمانی حساس است.",
        ],
        principles=[
            "تکرار را در تحلیل باور بگنجان.",
            "روانی پردازش را از صدق جدا کن.",
            "منبع گزاره را بازگردان.",
            "هشدار دربارهٔ فریب را آزمون کن.",
            "قضاوت را در دو مرحله بسنج.",
            "اثر را از آشنایی صرف تفکیک کن.",
            "به زمینهٔ واقعی تعمیم بده.",
        ],
        critiques=[
            "اندازهٔ اثر کوچک است.",
            "گزاره‌های آزمون ساختگی‌اند.",
            "تعمیم به باورهای مهم محدود است.",
            "تبیین روانی پردازش کامل نیست.",
            "نقش منبع کم سنجیده شده است.",
            "اثر با تأخیر ضعیف می‌شود.",
            "تفاوت فردی کم بررسی شده است.",
            "شرایط آزمایشگاهی ساده‌شده است.",
            "تفکیک آشنایی و صدق دشوار است.",
            "به فرهنگ و زبان کم توجه شده است.",
        ],
        critique_text="منتقدان می‌گویند اثر حقیقت‌نمایی در آزمایش با گزاره‌های بی‌اهمیت و اندازهٔ کوچک سنجیده شده و تعمیم آن به باورهای سیاسی و دینی نیازمند احتیاط است؛ با این حال متاآنالیز ۲۰۱۰ نشان داد اثر پایدار و قابل تکرار است.",
        applications=[
            "تحلیل تبلیغات سیاسی.",
            "پژوهش خبر جعلی.",
            "مطالعهٔ شایعه در شبکه‌های اجتماعی.",
            "تحلیل تکرار پیام تبلیغاتی.",
            "پژوهش اصلاح اطلاعات نادرست.",
            "مطالعهٔ تیتر خبری.",
            "تحلیل باور سلامت.",
            "پژوهش اقناع در کمپین.",
            "مطالعهٔ برند و تکرار شعار.",
            "تحلیل رسانه و ادراک صدق.",
            "پژوهش آموزش و تکرار.",
            "مطالعهٔ گفتار عمومی در بحران.",
            "مطالعهٔ اثر تکرار در پیام‌های سلامت عمومی.",
            "تحلیل نقش تکرار در باورهای انتخاباتی.",
        ],
        example_text="شایعه‌ای که در چند کانال تلگرامی تکرار می‌شود، پس از چند روز برای مخاطب آشنا و باورپذیرتر از خبر تکذیب آن می‌شود، حتی اگر تکذیب مستند باشد؛ این همان اثر حقیقت‌نمایی است.",
        evolution="هشر و همکاران در ۱۹۷۷ اثر را با آزمون گزاره‌های تکراری نشان دادند. پژوهش‌های دههٔ ۱۹۸۰ نقش روانی پردازش را برجسته کردند؛ دشنه و همکاران در ۲۰۱۰ متاآنالیز ۵۱ مطالعه را منتشر کردند و پژوهش‌های پس از ۲۰۱۵ اثر را در خبر جعلی و رسانهٔ اجتماعی آزمودند.",
        key_concepts=["روانی پردازش", "آشنایی", "اعتبار ارجاعی", "اثر تکرار", "اطلاعات نادرست", "سوگیری شناختی"],
        theorists="لین هشر، دیوید گلدستاین و توماس توپینو.",
        theorists_text="هشر در سنت روان‌شناسی حافظه و زبان اثر را کشف کرد و پژوهش‌های بعدی آن را به سوگیری‌های قضاوت پیوند دادند.",
        model="مدل روانی پردازش: تکرار سهولت پردازش را بالا می‌برد و سهولت به‌عنوان نشانهٔ صدق تفسیر می‌شود.",
        studies=[
            "آزمون گزاره‌های تکراری در ۱۹۷۷.",
            "متاآنالیز دشنه و همکاران در ۲۰۱۰.",
            "پژوهش فازیو دربارهٔ دانش پیشین.",
            "تحلیل خبر جعلی تکراری.",
            "مطالعهٔ روانی پردازش.",
            "پژوهش هشدار فریب.",
            "تحلیل تکرار در تبلیغات.",
            "مطالعهٔ باور سلامت.",
            "پژوهش رسانهٔ اجتماعی.",
            "تحلیل حافظهٔ منبع.",
            "مطالعهٔ قضاوت سریع.",
            "پژوهش اصلاح اطلاعات.",
        ],
    ),
    "MC-211": dict(
        year=2002,
        mapping=WORK_MAPPING,
        summary="اثر سی‌ان‌ان اصطلاحی است برای تأثیر پوشش زندهٔ خبری جهانی بر سیاست خارجی و تصمیم به مداخلهٔ بشردوستانه. این مفهوم در دههٔ ۱۹۹۰ با پوشش بحران‌هایی مانند سومالی، بوسنی و کوزوو رواج یافت و گفته شد تصاویر تلویزیونی دولت‌ها را به اقدام وادار می‌کنند. رابینسون در کتاب اثر سی‌ان‌ان در سال ۲۰۰۲ این فرض را بازبینی کرد و نشان داد رسانه به‌طور یکسان عمل نمی‌کند: گاه دستور کار می‌سازد، گاه مانع مداخله می‌شود و گاه آن را شتاب می‌دهد. او استدلال کرد اثر رسانه مشروط به عدم قطعیت سیاستی است و مدل تعامل سیاست و رسانه را پیشنهاد کرد. گیلبوآ در سال ۲۰۰۵ با مرور پژوهش‌ها کوشید جایگاه نظری این مفهوم را در روابط بین‌الملل روشن کند. نقدها بر دشواری اثبات علیت، تکیه بر نمونه‌های موردی و کاهش سلطهٔ تلویزیون جهانی در محیط رسانه‌ای چندپاره تأکید دارند.",
        definition="اثر سی‌ان‌ان تأثیر پوشش خبری جهانی و زنده بر شکل‌گیری و اجرای سیاست خارجی، به‌ویژه تصمیم به مداخلهٔ بشردوستانه است.",
        main_problem="آیا و چگونه پوشش خبری جهانی می‌تواند سیاست خارجی دولت‌ها را به سمت مداخله یا عقب‌نشینی هدایت کند و این تأثیر تحت چه شرایطی رخ می‌دهد.",
        mechanism="پوشش زندهٔ بحران توجه عمومی و فشار سیاسی می‌سازد؛ در شرایط عدم قطعیت سیاستی تصمیم‌گیران به تصاویر و روایت رسانه وابسته‌تر می‌شوند؛ اما رسانه بسته به هم‌راستایی با سیاست دولت، دستورکار، مانع یا شتاب‌دهنده عمل می‌کند.",
        assumptions=[
            "تلویزیون جهانی توجه عمومی را بسیج می‌کند.",
            "تصویر بحران بر تصمیم‌گیران اثر می‌گذارد.",
            "اثر رسانه به عدم قطعیت سیاستی وابسته است.",
            "رسانه هم‌راستا با دولت عمل می‌کند.",
            "پوشش خبری می‌تواند مانع یا شتاب‌دهنده باشد.",
            "افکار عمومی کانال فشار بر سیاست است.",
            "بحران بشردوستانه توجه رسانه را جلب می‌کند.",
            "محیط رسانه‌ای جهانی رقابتی است.",
        ],
        principles=[
            "عدم قطعیت سیاستی را بسنج.",
            "جهت هم‌راستایی رسانه و دولت را مشخص کن.",
            "اثر را به دستورکار، مانع و شتاب تفکیک کن.",
            "شواهد موردی را با مقایسه پیوند بده.",
            "افکار عمومی را واسطهٔ تحلیل بگیر.",
            "به تنوع رسانه‌ها توجه کن.",
            "از استنتاج علیت از هم‌زمانی بپرهیز.",
        ],
        critiques=[
            "اثبات علیت دشوار است.",
            "شواهد بیشتر موردی و روایی است.",
            "نقش عوامل دیپلماتیک کم دیده می‌شود.",
            "سلطهٔ سی‌ان‌ان فروکش کرده است.",
            "محیط رسانه‌ای چندپاره شده است.",
            "سنجش افکار عمومی ناهمگون است.",
            "انتخاب موارد موفق سوگیری دارد.",
            "به رسانهٔ محلی کم توجه است.",
            "به سیاست پنهان دولت کم می‌پردازد.",
            "تعمیم به بحران‌های غیرغربی محدود است.",
        ],
        critique_text="منتقدان می‌گویند اثر سی‌ان‌ان بیش از یک نظریه، برهانی از چند مورد مشهور است و نقش عوامل دیپلماتیک و بوروکراتیک را کم میانگارد؛ رابینسون خود این نکته را پذیرفت و اثر را مشروط به تعامل رسانه و سیاست دانست.",
        applications=[
            "تحلیل مداخلهٔ بشردوستانه.",
            "پژوهش سیاست خارجی.",
            "مطالعهٔ پوشش بحران.",
            "تحلیل دیپلماسی رسانه‌ای.",
            "پژوهش افکار عمومی و جنگ.",
            "مطالعهٔ خبر جهانی.",
            "تحلیل بحران پناهندگان.",
            "پژوهش رسانه و تصمیم‌گیری.",
            "مطالعهٔ پوشش انتخابات خارجی.",
            "تحلیل ارتباطات بحران بین‌المللی.",
            "پژوهش رسانهٔ اجتماعی و سیاست.",
            "مطالعهٔ کمک بشردوستانه.",
        ],
        example_text="تصاویر زندهٔ قحطی و آوارگی در یک بحران فشار عمومی را بر دولت‌ها افزایش می‌دهد و در شرایطی که سیاست روشنی وجود ندارد تصمیم به کمک یا مداخله را شتاب می‌دهد؛ نمونه‌ای از تعامل سیاست و رسانه در چارچوب رابینسون.",
        evolution="اصطلاح در دههٔ ۱۹۹۰ با پوشش زندهٔ بحران‌ها رواج یافت. رابینسون در ۲۰۰۲ با بازبینی موارد مدل تعامل سیاست و رسانه را پیشنهاد کرد؛ گیلبوآ در ۲۰۰۵ مرور نظری ارائه داد و پژوهش‌های پس از ۲۰۱۰ اثر را به رسانهٔ اجتماعی و محیط چندپاره گستردند.",
        key_concepts=["تعامل سیاست و رسانه", "عدم قطعیت سیاستی", "اثر مانع", "اثر شتاب‌دهنده", "دستورکار رسانه", "مداخلهٔ بشردوستانه"],
        theorists="پیرز رابینسون و ایتان گیلبوآ.",
        theorists_text="رابینسون در سنت پژوهش سیاست و رسانه اثر را بازصورت‌بندی کرد و گیلبوآ آن را در چارچوب نظریهٔ ارتباطات بین‌الملل جای داد.",
        model="مدل تعامل سیاست و رسانه: اثر پوشش خبری بر سیاست خارجی مشروط به عدم قطعیت سیاستی و هم‌راستایی رسانه و دولت است.",
        studies=[
            "کتاب اثر سی‌ان‌ان در ۲۰۰۲.",
            "مرور گیلبوآ در ۲۰۰۵.",
            "مطالعهٔ بحران سومالی.",
            "پژوهش بحران بوسنی.",
            "تحلیل بحران کوزوو.",
            "مطالعهٔ نسل‌کشی رواندا.",
            "پژوهش رسانه و مداخله.",
            "تحلیل دیپلماسی رسانه‌ای.",
            "مطالعهٔ افکار عمومی و جنگ.",
            "پژوهش خبر جهانی.",
            "تحلیل رسانهٔ اجتماعی و بحران.",
            "مطالعهٔ کمک بشردوستانه.",
        ],
    ),
    "MC-246": dict(
        year=2004,
        mapping=WORK_MAPPING,
        summary="اثر بی‌بازداری آنلاین به کاهش مهارهای اجتماعی در ارتباط اینترنتی اشاره دارد. جان سولر در سال ۲۰۰۴ شش عامل را برای این پدیده برشمرد: ناشناسی تجزیه‌ای، ناپیدایی، ناهمزمانی، فرافکنی خیالین، خیال‌پردازی تجزیه‌ای و کم‌رنگ شدن اقتدار. او دو شکل متمایز تشخیص داد: بی‌بازداری سودمند که به خودافشایی و مهربانی می‌انجامد و بی‌بازداری زیان‌بار که به پرخاشگری، توهین و آزار بدل می‌شود. لاپیدوت-لفلر و باراک در سال ۲۰۱۲ با آزمایش نشان دادند از میان سه عامل ناشناسی، ناپیدایی و نبود تماس چشمی، نبود تماس چشمی نقش اصلی را در برانگیختن بی‌بازداری زیان‌بار دارد. این اثر در پژوهش آزار آنلاین، گفتار نفرت و طراحی سکوهای اجتماعی کاربرد گسترده یافته است. نقدها بر تکیه بر خودگزارشی، همپوشانی سازه‌ها و کم‌توجهی به طراحی پلتفرم و فرهنگ تأکید دارند.",
        definition="اثر بی‌بازداری آنلاین کاهش مهارهای اجتماعی و افزایش ابرازگری در ارتباط اینترنتی نسبت به ارتباط رودررو است.",
        main_problem="چرا افراد در محیط آنلاین رفتارهایی نشان می‌دهند که در حضور فیزیکی از آن‌ها پرهیز می‌کنند و چه عواملی این تغییر مهار را ایجاد می‌کند.",
        mechanism="ناشناسی، ناپیدایی، ناهمزمانی و کم‌رنگ شدن اقتدار هزینهٔ اجتماعی رفتار را در ادراک فرد کاهش می‌دهند؛ فرد پیامدهای کردار خود را کم‌برآورد می‌کند و مهار درونی سست می‌شود، در نتیجه ابرازگری سودمند یا زیان‌بار افزایش می‌یابد.",
        assumptions=[
            "مهار اجتماعی به حضور فیزیکی وابسته است.",
            "ناشناسی هزینهٔ رفتار را کاهش می‌دهد.",
            "ناپیدایی احساس مصونیت می‌سازد.",
            "ناهمزمانی تأمل و بازنگری را کم می‌کند.",
            "کم‌رنگ شدن اقتدار هنجارشکنی را آسان می‌کند.",
            "پیامد رفتار آنلاین کم‌برآورد می‌شود.",
            "بی‌بازداری دو شکل سودمند و زیان‌بار دارد.",
            "طراحی محیط بر مهار اثر می‌گذارد.",
        ],
        principles=[
            "شش عامل موقعیتی را جدا بسنج.",
            "بی‌بازداری سودمند و زیان‌بار را تفکیک کن.",
            "نقش تماس چشمی را در نظر بگیر.",
            "طراحی پلتفرم را متغیر تحلیل بدان.",
            "خودگزارشی را با مشاهدهٔ رفتار ترکیب کن.",
            "هنجار گروه را در تحلیل بگنجان.",
            "از تعمیم یکسان به همهٔ محیط‌های آنلاین بپرهیز.",
        ],
        critiques=[
            "شواهد اولیه بیشتر مفهومی بود.",
            "سازه‌ها با یکدیگر همپوشانی دارند.",
            "آزمایش‌ها نمونهٔ کوچک دارند.",
            "به طراحی پلتفرم کم توجه شده است.",
            "تفاوت فرهنگی کم سنجیده شده است.",
            "مرز سودمند و زیان‌بار مبهم است.",
            "اثر اندازهٔ یکسانی ندارد.",
            "به ناشناسی نهادی کم پرداخته شده است.",
            "به تنظیم‌گری و نظارت کم توجه است.",
            "تعمیم به محیط واقعی محدود است.",
        ],
        critique_text="منتقدان می‌گویند بی‌بازداری آنلاین بیش از یک اثر واحد، مجموعه‌ای از سازه‌های همپوشان است و نقش طراحی پلتفرم و فرهنگ را کم می‌بیند؛ با این حال چارچوب سولر و آزمایش ۲۰۱۲ نشان دادند عوامل موقعیتی مشخص می‌توانند مهار اجتماعی را به‌شکل اندازه‌پذیر تغییر دهند.",
        applications=[
            "تحلیل آزار آنلاین.",
            "پژوهش گفتار نفرت.",
            "مطالعهٔ ترولینگ.",
            "تحلیل طراحی پلتفرم.",
            "پژوهش خودافشایی آنلاین.",
            "مطالعهٔ آموزش مجازی.",
            "تحلیل بازی آنلاین.",
            "پژوهش سلامت روان دیجیتال.",
            "مطالعهٔ نظارت و تنظیم‌گری.",
            "تحلیل کمپین آنلاین.",
            "پژوهش روابط اجتماعی دیجیتال.",
            "مطالعهٔ امنیت کاربران.",
            "پژوهش رابطهٔ ناشناسی و رفتار در انجمن‌های بحث آنلاین.",
            "تحلیل سیاست‌های الزام هویت واقعی در سکوهای اجتماعی.",
            "مطالعهٔ بی‌بازداری سودمند در گروه‌های پشتیبانی آنلاین.",
        ],
        example_text="کاربری که در گفتار رودررو کم‌رو است در بخش دیدگاه‌های یک سکوی خبری با لحنی تند و توهین‌آمیز می‌نویسد؛ ناشناسی و ناپیدایی و نبود تماس چشمی مهار اجتماعی او را کاهش داده است.",
        evolution="سولر در ۲۰۰۴ چارچوب شش‌عاملی را منتشر کرد. لاپیدوت-لفلر و باراک در ۲۰۱۲ با آزمایش نقش نبود تماس چشمی را برجسته کردند؛ پژوهش‌های بعدی اثر را به طراحی پلتفرم، تنظیم‌گری و سلامت روان گستراندند.",
        key_concepts=["ناشناسی تجزیه‌ای", "ناپیدایی", "ناهمزمانی", "فرافکنی خیالین", "بی‌بازداری زیان‌بار", "کم‌رنگ شدن اقتدار"],
        theorists="جان سولر، نوام لاپیدوت-لفلر و آنی باراک.",
        theorists_text="سولر در سنت روان‌شناسی بالینی اینترنت اثر را صورت‌بندی کرد و پژوهش‌های آزمایشی بعدی آن را سنجیدند.",
        model="مدل شش‌عاملی: ناشناسی، ناپیدایی، ناهمزمانی، فرافکنی خیالین، خیال‌پردازی تجزیه‌ای و کم‌رنگ شدن اقتدار مهار اجتماعی را کاهش می‌دهند.",
        studies=[
            "مقالهٔ اصلی سولر در ۲۰۰۴.",
            "آزمایش لاپیدوت-لفلر و باراک در ۲۰۱۲.",
            "پژوهش آزار آنلاین.",
            "مطالعهٔ گفتار نفرت.",
            "تحلیل ترولینگ.",
            "پژوهش خودافشایی آنلاین.",
            "مطالعهٔ بازی آنلاین.",
            "تحلیل طراحی پلتفرم.",
            "پژوهش سلامت روان دیجیتال.",
            "مطالعهٔ تنظیم‌گری محتوا.",
            "تحلیل روابط دیجیتال.",
            "پژوهش ناشناسی و هنجار.",
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
                                       "verified": n_verified, "batch": 175}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH175 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
