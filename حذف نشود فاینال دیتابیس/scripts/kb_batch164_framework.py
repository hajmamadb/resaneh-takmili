# -*- coding: utf-8 -*-
"""Batch 164 (HYPOTHESIS): MC-560 bandwagon, MC-561 underdog, MC-562 congruence/reinforcement, MC-563 catharsis."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch164-hypothesis-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch164_hypothesis.json"

S = {
    "MC-560": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Bandwagon and Underdog Effects and the Possibility of Election Predictions",
             title_fa="اثرهای ارابه و زیردست و امکان پیش‌بینی انتخابات",
             authors="Simon, H. A.", year=1954,
             publisher="Public Opinion Quarterly",
             doi="10.1086/266513",
             url="https://academic.oup.com/poq/article-abstract/18/3/245/1907955",
             language="en", isbn=None,
             citation="Simon, H. A. (1954). Bandwagon and underdog effects and the possibility of election predictions. Public Opinion Quarterly, 18(3), 245-253.",
             locator="18(3):245-253", locator_type="page_range",
             supports="formal account of bandwagon and underdog reactions to published predictions", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Jumping on the Bandwagon with the Underdog: The Impact of Attitude Polls on Polling Behavior",
             title_fa="سوار شدن بر ارابه با زیردست: اثر نظرسنجی‌ها بر رفتار پاسخ‌دهی",
             authors="Ceci, S. J.; Kain, E. L.", year=1982,
             publisher="Public Opinion Quarterly",
             doi=None,
             url="https://academic.oup.com/poq/article-abstract/46/2/228/1923849",
             language="en", isbn=None,
             citation="Ceci, S. J., & Kain, E. L. (1982). Jumping on the bandwagon with the underdog: The impact of attitude polls on polling behavior. Public Opinion Quarterly, 46(2), 228-242.",
             locator="46(2):228-242", locator_type="page_range",
             supports="experimental evidence that poll information shifts subsequent responses", verified=True),
    ],
    "MC-561": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Bandwagon and Underdog Effects and the Possibility of Election Predictions",
             title_fa="اثرهای ارابه و زیردست و امکان پیش‌بینی انتخابات",
             authors="Simon, H. A.", year=1954,
             publisher="Public Opinion Quarterly",
             doi="10.1086/266513",
             url="https://academic.oup.com/poq/article-abstract/18/3/245/1907955",
             language="en", isbn=None,
             citation="Simon, H. A. (1954). Bandwagon and underdog effects and the possibility of election predictions. Public Opinion Quarterly, 18(3), 245-253.",
             locator="18(3):245-253", locator_type="page_range",
             supports="conceptual statement of the underdog effect alongside the bandwagon effect", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Jumping on the Bandwagon with the Underdog: The Impact of Attitude Polls on Polling Behavior",
             title_fa="سوار شدن بر ارابه با زیردست: اثر نظرسنجی‌ها بر رفتار پاسخ‌دهی",
             authors="Ceci, S. J.; Kain, E. L.", year=1982,
             publisher="Public Opinion Quarterly",
             doi=None,
             url="https://academic.oup.com/poq/article-abstract/46/2/228/1923849",
             language="en", isbn=None,
             citation="Ceci, S. J., & Kain, E. L. (1982). Jumping on the bandwagon with the underdog: The impact of attitude polls on polling behavior. Public Opinion Quarterly, 46(2), 228-242.",
             locator="46(2):228-242", locator_type="page_range",
             supports="experimental evidence of underdog shifts after poll information", verified=True),
    ],
    "MC-562": [
        dict(kind="BOOK",
             title_en="The People's Choice: How the Voter Makes Up His Mind in a Presidential Campaign",
             title_fa="انتخاب مردم: رأی‌دهنده چگونه در کارزار انتخاباتی تصمیم می‌گیرد",
             authors="Lazarsfeld, P. F.; Berelson, B.; Gaudet, H.", year=1948,
             publisher="Columbia University Press",
             doi=None,
             url="https://cup.columbia.edu/book/the-peoples-choice/9780231197953/",
             language="en", isbn="9780231197953",
             citation="Lazarsfeld, P. F., Berelson, B., & Gaudet, H. (1948). The People's Choice: How the Voter Makes Up His Mind in a Presidential Campaign (2nd ed.). New York: Columbia University Press.",
             locator="2nd edition", locator_type="edition",
             supports="reinforcement predominance in campaign communication effects", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Selective Exposure to Information: A Critical Review",
             title_fa="مواجههٔ گزینشی با اطلاعات: مروری انتقادی",
             authors="Sears, D. O.; Freedman, J. L.", year=1967,
             publisher="Public Opinion Quarterly",
             doi=None,
             url="https://academic.oup.com/poq/article-abstract/31/2/194/1813651",
             language="en", isbn=None,
             citation="Sears, D. O., & Freedman, J. L. (1967). Selective exposure to information: A critical review. Public Opinion Quarterly, 31(2), 194-213.",
             locator="31(2):194-213", locator_type="page_range",
             supports="critical review of selective exposure and reinforcement evidence", verified=True),
    ],
    "MC-563": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Stimulating Versus Cathartic Effects of a Vicarious Aggressive Activity",
             title_fa="اثرهای برانگیزاننده در برابر تخلیه‌ای فعالیت پرخاشگرانهٔ جانشینی",
             authors="Feshbach, S.", year=1961,
             publisher="Journal of Abnormal and Social Psychology",
             doi="10.1037/h0048863",
             url="https://doi.apa.org/doi/10.1037/h0048863",
             language="en", isbn=None,
             citation="Feshbach, S. (1961). The stimulating versus cathartic effects of a vicarious aggressive activity. Journal of Abnormal and Social Psychology, 63(2), 381-385.",
             locator="63(2):381-385", locator_type="page_range",
             supports="classic test of catharsis through vicarious aggression", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Catharsis, Aggression, and Persuasive Influence: Self-Fulfilling or Self-Defeating Prophecies?",
             title_fa="کاتارسیس، پرخاشگری و نفوذ اقناعی: پیش‌بینی خودمحقق یا خودشکن؟",
             authors="Bushman, B. J.; Baumeister, R. F.; Stack, A. D.", year=1999,
             publisher="Journal of Personality and Social Psychology",
             doi="10.1037/0022-3514.76.3.367",
             url="https://psycnet.apa.org/doiLanding?doi=10.1037/0022-3514.76.3.367",
             language="en", isbn=None,
             citation="Bushman, B. J., Baumeister, R. F., & Stack, A. D. (1999). Catharsis, aggression, and persuasive influence: Self-fulfilling or self-defeating prophecies? Journal of Personality and Social Psychology, 76(3), 367-376.",
             locator="76(3):367-376", locator_type="page_range",
             supports="experimental evidence that catharsis beliefs increase rather than reduce aggression", verified=True),
    ],
}

ENRICH = {
    "MC-560": dict(
        year=1954,
        summary="فرضیهٔ اثر ارابه، که هربرت سایمون در سال ۱۹۵۴ در فصل‌نامهٔ افکار عمومی صورت‌بندی کرد، می‌گوید انتشار پیش‌بینی‌ها و نظرسنجی‌ها می‌تواند خودِ نتیجه را تغییر دهد، زیرا بخشی از رأی‌دهندگان به سمت نامزد پیشتاز می‌روند. سایمون این واکنش را اثر ارابه نامید و در کنار آن اثر زیردست را قرار داد که در آن بخشی از رأی‌دهندگان از نامزد عقب‌مانده حمایت می‌کنند. او نشان داد اگر چنین واکنش‌هایی وجود داشته باشد، پیش‌بینی انتخاباتی می‌تواند خودش را نقض کند و همین مسئله، اعتبار پیش‌بینی‌ها را به مسئله‌ای منطقی و تجربی بدل می‌کند. پژوهش انتخاباتی لازارسفلد و همکاران در همان سال‌ها بیشتر تقویت نگرش موجود را یافت تا تغییر آن، و اثر ارابه را کوچک نشان داد. سیچی و کین در سال ۱۹۸۲ با آزمایش نشان دادند که اطلاعات نظرسنجی می‌تواند پاسخ‌دهی بعدی را هم به سمت پیشتاز و هم به سمت زیردست جابه‌جا کند. در رسانه، فرضیه برای تحلیل انتشار نظرسنجی، پوشش مسابقه‌ای انتخابات، اثبات اجتماعی در شبکه‌های اجتماعی و ترند الگوریتمی به کار می‌رود. نقدهای اصلی به آن، کوچکی اثر در میدان، ابهام جهت واکنش، تفاوت زمینهٔ ملی و خطر سوءاستفادهٔ سیاسی از نظرسنجی را برجسته می‌کنند.",
        definition="فرضیهٔ اثر ارابه می‌گوید انتشار نظرسنجی و پیش‌بینی برنده، بخشی از رأی‌دهندگان را به سمت نامزد پیشتاز می‌کشاند و می‌تواند نتیجه را تغییر دهد.",
        main_problem="آیا انتشار پیش‌بینی‌ها و نظرسنجی‌ها بر رأی‌دهندگان اثر می‌گذارد، جهت این اثر چیست و آیا پیش‌بینی انتخاباتی با واکنش مخاطب نقض می‌شود.",
        mechanism="فرد پیشتازی نامزد را نشانهٔ برنده‌شدن احتمالی می‌بیند؛ تمایل به همراهی با اکثریت یا ترس از هدر دادن رأی، او را به سمت پیشتاز می‌برد و در نتیجه توزیع آرا در جهت پیش‌بینی جابه‌جا می‌شود.",
        assumptions=[
            "نظرسنجی به مخاطب می‌رسد.",
            "فرد پیشتاز را می‌شناسد.",
            "همراهی با اکثریت انگیزه دارد.",
            "رأی قابل تغییر است.",
            "انتشار پیش‌بینی بر نتیجه اثر دارد.",
        ],
        principles=[
            "منبع نظرسنجی را شفاف کن.",
            "حاشیهٔ خطا را منتشر کن.",
            "اثر را در بافت ملی بسنج.",
            "جهت واکنش را تجربی بررسی کن.",
            "از انتشار زودهنگام پرهیز کن.",
            "اثر شبکه‌ای را رصد کن.",
        ],
        critiques=[
            "اثر در میدان کوچک است.",
            "جهت واکنش روشن نیست.",
            "تفاوت زمینهٔ ملی را کم می‌بیند.",
            "خودگزینی پاسخ‌دهنده را نادیده می‌گیرد.",
            "خطر سوءاستفادهٔ سیاسی دارد.",
            "به رسانهٔ دیجیتال کم توجه دارد.",
            "سنجش علّی دشوار است.",
            "به رأی‌دهندهٔ بی‌تصمیم کم می‌پردازد.",
        ],
        critique_text="منتقدان می‌گویند اثر ارابه در آزمایش دیده می‌شود اما در انتخابات واقعی کوچک و نامعین است و جهت آن به زمینه و ویژگی رأی‌دهنده بستگی دارد؛ با این حال، بحث انتشار نظرسنجی بدون آن کامل نیست.",
        applications=[
            "تحلیل پوشش نظرسنجی.",
            "پژوهش پوشش مسابقه‌ای.",
            "مطالعهٔ اثبات اجتماعی.",
            "تحلیل ترند الگوریتمی.",
            "سیاست انتشار نظرسنجی.",
            "پژوهش رأی راهبردی.",
            "تحلیل کمپین انتخاباتی.",
            "مطالعهٔ نظرسنجی در شبکه‌های اجتماعی.",
            "تحلیل اثر نظرسنجی بر رأی‌دهندهٔ بی‌تصمیم.",
            "پژوهش پوشش رسانه‌ای پیش‌بینی انتخابات.",
            "تحلیل اثر نظرسنجی بر مشارکت.",
        ],
        example_text="وقتی رسانه‌ها هفته‌ها از پیشتازی یک نامزد خبر می‌دهند، بخشی از رأی‌دهندگان نامزد رقیب را بازنده می‌بینند و به سمت برنده می‌روند؛ فرضیه می‌گوید همین حرکت، پیش‌بینی را به پیش‌گویی خودمحقق بدل می‌کند.",
        evolution="سایمون در سال ۱۹۵۴ اثر ارابه و زیردست را صورت‌بندی کرد و پژوهش انتخاباتی دههٔ ۱۹۴۰ آن را کوچک یافت؛ سیچی و کین در سال ۱۹۸۲ شواهد آزمایشگاهی دادند و پژوهش‌های بعدی، اثر را در رسانهٔ دیجیتال و نظرسنجی آنی بازبینی کردند.",
        key_concepts=["اثر ارابه", "اثر زیردست", "نظرسنجی", "پیش‌بینی انتخاباتی", "همراهی با اکثریت", "رأی راهبردی"],
        theorists="هربرت سایمون، استیون سیچی و ادوارد کین.",
        theorists_text="فرضیه در سنت پژوهش افکار عمومی و رفتار انتخاباتی شکل گرفت.",
        model="انتشار پیش‌بینی به‌عنوان محرک جابه‌جایی رأی به سمت پیشتاز.",
        studies=[
            "مقالهٔ سال ۱۹۵۴ فرضیه را ساخت.",
            "پژوهش انتخاباتی، اثر کوچک را یافت.",
            "آزمایش سال ۱۹۸۲ جابه‌جایی را نشان داد.",
            "مطالعهٔ رأی راهبردی، انگیزه را بررسی کرد.",
            "پژوهش دیجیتال، ترند را تحلیل کرد.",
            "مطالعهٔ تطبیقی، تفاوت ملی را سنجید.",
            "مطالعهٔ رسانه، پوشش پیشتاز را تحلیل کرد.",
        ],
    ),
    "MC-561": dict(
        year=1954,
        summary="فرضیهٔ اثر زیردست، که هربرت سایمون در سال ۱۹۵۴ در همان مقالهٔ اثر ارابه مطرح کرد، می‌گوید انتشار نظرسنجی و پیش‌بینی می‌تواند گروهی از رأی‌دهندگان را به حمایت از نامزد عقب‌مانده بکشاند. منطق این واکنش با اثر ارابه متفاوت است: در اثر ارابه فرد به برنده می‌پیوندد تا در اردوگاه پیروز باشد، اما در اثر زیردست همدلی با بازنده، احساس بی‌عدالتی نسبت به پوشش رسانه‌ای و میل به حفظ رقابت، فرد را به سمت نامزد ضعیف می‌برد. سایمون نشان داد که وجود هم‌زمان این دو تمایل، پیش‌بینی انتخاباتی را به مسئله‌ای پیچیده بدل می‌کند، زیرا واکنش‌ها ممکن است یکدیگر را خنثی کنند. سیچی و کین در سال ۱۹۸۲ در آزمایشی دیدند که اطلاعات نظرسنجی می‌تواند پاسخ‌دهی بعدی را به سمت زیردست هم جابه‌جا کند، به‌ویژه هنگامی که نامزد عقب‌مانده در نظرسنجی ضعیف نشان داده شود. در رسانه، فرضیه برای تحلیل پوشش همدلانهٔ بازنده، روایت قربانی، کمپین‌های کوچک و واکنش به نظرسنجی به کار می‌رود. نقدهای اصلی به آن، کوچکی و ناپایداری اثر، وابستگی به نوع پیام و شخصیت نامزد، دشواری تفکیک آن از همدلی عمومی و کم‌توجهی به بافت فرهنگی را برجسته می‌کنند.",
        definition="فرضیهٔ اثر زیردست می‌گوید انتشار نظرسنجی می‌تواند بخشی از رأی‌دهندگان را به حمایت از نامزد عقب‌مانده وادارد و نتیجه را در جهت معکوس پیش‌بینی جابه‌جا کند.",
        main_problem="چرا و تحت چه شرایطی رأی‌دهندگان از نامزد عقب‌مانده حمایت می‌کنند و این واکنش چگونه پیش‌بینی انتخاباتی را مختل می‌کند.",
        mechanism="دیدن عقب‌ماندگی نامزد، همدلی و احساس بی‌عدالتی را برمی‌انگیزد؛ فرد برای حفظ رقابت یا حمایت از ضعیف، رأی خود را به او می‌دهد و توزیع آرا در جهت معکوس پیش‌بینی حرکت می‌کند.",
        assumptions=[
            "نظرسنجی به مخاطب می‌رسد.",
            "همدلی با بازنده انگیزه دارد.",
            "احساس بی‌عدالتی رسانه‌ای وجود دارد.",
            "فرد به حفظ رقابت اهمیت می‌دهد.",
            "رأی قابل تغییر است.",
        ],
        principles=[
            "عقب‌ماندگی را برجسته نکن.",
            "همدلی را در تحلیل بگنجان.",
            "پوشش منصفانه را تضمین کن.",
            "اثر را در بافت ملی بسنج.",
            "شخصیت نامزد را کنترل کن.",
            "از روایت قربانی سوءاستفاده نکن.",
        ],
        critiques=[
            "اثر کوچک و ناپایدار است.",
            "به نوع پیام وابسته است.",
            "از همدلی عمومی تفکیک‌پذیر نیست.",
            "بافت فرهنگی را کم می‌بیند.",
            "سنجش علّی دشوار است.",
            "به رأی‌دهندهٔ بی‌تصمیم کم می‌پردازد.",
            "خطر روایت نمایشی دارد.",
            "تعمیم آزمایشگاهی محدود است.",
        ],
        critique_text="منتقدان می‌گویند اثر زیردست در آزمایش دیده می‌شود اما در انتخابات واقعی کوچک و وابسته به زمینه است و از همدلی عمومی به‌سختی جدا می‌شود؛ با این حال، مکمل ضروری اثر ارابه در تحلیل نظرسنجی است.",
        applications=[
            "تحلیل پوشش بازنده.",
            "پژوهش کمپین کوچک.",
            "مطالعهٔ روایت قربانی.",
            "تحلیل نظرسنجی انتخاباتی.",
            "پژوهش همدلی سیاسی.",
            "مطالعهٔ پوشش منصفانه.",
            "تحلیل واکنش به پیش‌بینی.",
            "پژوهش رأی اعتراضی.",
            "تحلیل حمایت از نامزد ضعیف در شبکه‌های اجتماعی.",
            "مطالعهٔ اثر نظرسنجی بر مشارکت رأی‌دهندگان معترض.",
            "مطالعهٔ همدلی در رسانهٔ بحران.",
            "پژوهش کمپین نامزد مستقل.",
        ],
        example_text="نامزدی که در نظرسنجی‌ها عقب است، در یک مناظره خوب ظاهر می‌شود و رسانه‌ها او را بازندهٔ احتمالی می‌خوانند؛ بخشی از رأی‌دهندگان به همدلی با او رأی می‌دهند و همین حرکت، پیش‌بینی را به هم می‌ریزد.",
        evolution="سایمون در سال ۱۹۵۴ اثر زیردست را در کنار اثر ارابه مطرح کرد و پژوهش انتخاباتی دههٔ ۱۹۴۰ آن را کوچک یافت؛ سیچی و کین در سال ۱۹۸۲ شواهد آزمایشگاهی دادند و پژوهش‌های بعدی، آن را در رسانهٔ دیجیتال و کمپین‌های کوچک بازبینی کردند.",
        key_concepts=["اثر زیردست", "اثر ارابه", "همدلی", "نظرسنجی", "رأی اعتراضی", "پوشش منصفانه"],
        theorists="هربرت سایمون، استیون سیچی و ادوارد کین.",
        theorists_text="فرضیه در سنت پژوهش افکار عمومی و رفتار انتخاباتی شکل گرفت.",
        model="انتشار عقب‌ماندگی نامزد به‌عنوان محرک همدلی و جابه‌جایی رأی به سمت بازنده.",
        studies=[
            "مقالهٔ سال ۱۹۵۴ فرضیه را ساخت.",
            "آزمایش سال ۱۹۸۲ جابه‌جایی را نشان داد.",
            "مطالعهٔ همدلی، انگیزه را بررسی کرد.",
            "پژوهش رسانه، روایت بازنده را تحلیل کرد.",
            "مطالعهٔ دیجیتال، رأی اعتراضی را بررسی کرد.",
            "پژوهش تطبیقی، تفاوت ملی را سنجید.",
            "مطالعهٔ رسانه، پوشش ضعیف را تحلیل کرد.",
        ],
    ),
    "MC-562": dict(
        year=1948,
        summary="فرضیهٔ همسویی و تقویت، که پل لازارسفلد، برنارد برلسون و هیزل گودت در سال ۱۹۴۸ در کتاب انتخاب مردم صورت‌بندی کردند، می‌گوید کارزار انتخاباتی و رسانه بیشتر نگرش‌های موجود را تقویت می‌کنند تا اینکه آن‌ها را تغییر دهند. پژوهش پنلی آنان در شهر ایلی نشان داد که بیشتر رأی‌دهندگان در طول کارزار بر موضع خود ماندند و تغییر واقعی رأی کم بود؛ آنان اثر کارزار را به سه دسته تقسیم کردند: فعال‌سازی، یعنی تبدیل تمایل پنهان به رأی آشکار، تقویت، یعنی استوارتر شدن نگرش موجود، و تغییر، یعنی جابه‌جایی واقعی از یک نامزد به نامزد دیگر. سهم تقویت بیش از دو دستهٔ دیگر بود و همین یافته، پایهٔ فرضیهٔ همسویی شد: فرد اطلاعات هم‌سو با نگرش خود را بیشتر می‌جوید و از اطلاعات ناهمسو می‌پرهیزد. سیرز و فریدمن در سال ۱۹۶۷ شواهد مواجههٔ گزینشی را به‌طور انتقادی مرور کردند و نشان دادند این گرایش همگانی نیست و به اطمینان، اهمیت موضوع و دسترسی به اطلاعات بستگی دارد. در رسانه، فرضیه برای تحلیل اتاق پژواک، رسانهٔ حزبی، هدف‌گیری تبلیغات و قطبی‌شدن به کار می‌رود. نقدهای اصلی به آن، کم‌برآورد تغییر در محیط دیجیتال، فرض فعال‌بودن کامل مخاطب و دشواری سنجش مواجههٔ واقعی را برجسته می‌کنند.",
        definition="فرضیهٔ همسویی و تقویت می‌گوید مخاطب اطلاعات هم‌سو با نگرش خود را بیشتر می‌جوید و رسانه در بیشتر موارد نگرش موجود را تقویت می‌کند، نه اینکه آن را تغییر دهد.",
        main_problem="رسانه و کارزار انتخاباتی چگونه بر نگرش موجود اثر می‌گذارند و چرا تقویت نگرش بیش از تغییر آن رخ می‌دهد.",
        mechanism="فرد به اطلاعات هم‌سو با باور خود توجه و از اطلاعات ناهمسو پرهیز می‌کند؛ این گزینش، نگرش را استوارتر می‌کند و در نتیجه سهم تقویت از سهم تغییر بیشتر می‌شود.",
        assumptions=[
            "مخاطب فعال و گزینشگر است.",
            "اطلاعات هم‌سو جذاب‌تر است.",
            "نگرش پیشین پایدار است.",
            "کارزار بیشتر فعال‌سازی می‌کند.",
            "تغییر رأی کم است.",
        ],
        principles=[
            "تقویت و تغییر را جدا بسنج.",
            "مواجههٔ واقعی را اندازه بگیر.",
            "اطمینان مخاطب را کنترل کن.",
            "اهمیت موضوع را در تحلیل بگنجان.",
            "به محیط دیجیتال توجه کن.",
            "اتاق پژواک را تجربی بررسی کن.",
        ],
        critiques=[
            "تغییر در محیط دیجیتال را کم می‌بیند.",
            "فعال‌بودن کامل مخاطب را فرض می‌کند.",
            "سنجش مواجههٔ واقعی دشوار است.",
            "به مواجههٔ تصادفی کم توجه دارد.",
            "به تفاوت نسل‌ها کم می‌پردازد.",
            "به رسانهٔ سرگرمی کم توجه است.",
            "تعمیم آن به غیرآمریکا محدود است.",
            "نقش الگوریتم را نادیده می‌گیرد.",
        ],
        critique_text="منتقدان می‌گویند فرضیهٔ همسویی و تقویت سهم تقویت را درست نشان داد اما در محیط دیجیتال با مواجههٔ تصادفی و الگوریتمی، مرز تقویت و تغییر مبهم‌تر شده است؛ با این حال، چارچوب پایهٔ پژوهش گزینشگری است.",
        applications=[
            "تحلیل اتاق پژواک.",
            "پژوهش رسانهٔ حزبی.",
            "مطالعهٔ هدف‌گیری تبلیغات.",
            "تحلیل قطبی‌شدن.",
            "پژوهش کمپین انتخاباتی.",
            "مطالعهٔ مواجههٔ گزینشی.",
            "تحلیل فید الگوریتمی.",
            "پژوهش تغییر رأی.",
            "تحلیل تقویت نگرش در شبکه‌های اجتماعی.",
            "مطالعهٔ مواجههٔ تصادفی با خبر در پلتفرم‌ها.",
        ],
        example_text="رأی‌دهنده‌ای که به یک نامزد گرایش دارد، در طول کارزار بیشتر برنامه‌ها و صفحات هم‌سو با او را دنبال می‌کند و کمتر خبر ناهمسو می‌بیند؛ فرضیه می‌گوید این گزینش، نگرش او را تقویت می‌کند و تغییر رأی را کم می‌سازد.",
        evolution="لازارسفلد و همکاران در سال ۱۹۴۸ تقویت را در پژوهش پنلی نشان دادند و کلاپر در سال ۱۹۶۰ آن را به فرضیهٔ تأثیر محدود گره زد؛ سیرز و فریدمن در سال ۱۹۶۷ شواهد گزینشگری را مرور کردند و پژوهش دیجیتال، بحث را به اتاق پژواک و الگوریتم کشاند.",
        key_concepts=["تقویت", "همسویی", "مواجههٔ گزینشی", "فعال‌سازی", "تغییر رأی", "اتاق پژواک"],
        theorists="پل لازارسفلد، برنارد برلسون، هیزل گودت، دیوید سیرز و جاناتان فریدمن.",
        theorists_text="فرضیه در سنت پژوهش پنلی ارتباطات و روان‌شناسی گزینشگری شکل گرفت.",
        model="رسانه به‌عنوان عامل تقویت نگرش هم‌سو در میدان مواجههٔ گزینشی مخاطب.",
        studies=[
            "پژوهش سال ۱۹۴۸ تقویت را نشان داد.",
            "کتاب سال ۱۹۶۰ آن را به تأثیر محدود گره زد.",
            "مرور سال ۱۹۶۷ گزینشگری را بازبینی کرد.",
            "مطالعهٔ رسانهٔ حزبی، همسویی را سنجید.",
            "پژوهش دیجیتال، اتاق پژواک را تحلیل کرد.",
            "مطالعهٔ تطبیقی، تغییر رأی را بررسی کرد.",
        ],
    ),
    "MC-563": dict(
        year=1961,
        summary="فرضیهٔ کاتارسیس، که ریشهٔ آن به روان‌کاوی و بحث تخلیهٔ هیجانی بازمی‌گردد و سیمور فشباخ در سال ۱۹۶۱ آن را در پژوهش رسانه آزمود، می‌گوید مواجهه با خشونت جانشینی می‌تواند انگیزهٔ پرخاشگری را تخلیه و رفتار پرخاشگرانه را کاهش دهد. در این دیدگاه، تماشای خشونت یا بازی خشونت‌آمیز، احساس خشم را بیرون می‌ریزد و فرد را آرام می‌کند؛ از این رو طرفداران آن گاه کاهش خشونت رسانه‌ای را زیان‌آور دانسته‌اند. فشباخ در آزمایش خود دید که اثر تخلیه‌ای مشروط و محدود است و در برخی شرایط، فعالیت جانشینی پرخاشگری را برمی‌انگیزد نه اینکه آن را کاهش دهد. پژوهش‌های بعدی، به‌ویژه مرور گین و کوانتی و آزمایش بوشمن، بامایستر و استک در سال ۱۹۹۹، نشان دادند باور به کاتارسیس خودش را محقق می‌کند: فردی که برای آرام شدن به خشونت روی می‌آورد، خشم و پرخاشگری او بیشتر می‌شود. در رسانه، فرضیه برای تحلیل بازی خشونت‌آمیز، ورزش، برنامهٔ خشم و بحث تنظیم محتوا به کار می‌رود. نقدهای اصلی به آن، ضعف شواهد تجربی، دشواری سنجش تخلیه، تفاوت فردی در تنظیم هیجان و خطر توجیه خشونت با زبان علم را برجسته می‌کنند.",
        definition="فرضیهٔ کاتارسیس می‌گوید مواجهه با خشونت جانشینی انگیزهٔ پرخاشگری را تخلیه می‌کند و رفتار پرخاشگرانه را کاهش می‌دهد، هرچند شواهد تجربی این ادعا را ضعیف می‌دانند.",
        main_problem="آیا تماشای خشونت یا فعالیت جانشینی می‌تواند خشم را تخلیه و پرخاشگری را کاهش دهد یا برعکس آن را برمی‌انگیزد.",
        mechanism="فرد خشم خود را با تماشای خشونت یا بازی خشونت‌آمیز بیرون می‌ریزد و تنش او کم می‌شود؛ اما اگر محتوای خشونت‌آمیز الگوی رفتاری و برانگیختگی بدهد، همان تجربه می‌تواند پرخاشگری بعدی را افزایش دهد.",
        assumptions=[
            "خشم انرژی روانی انباشته است.",
            "تخلیه انرژی خشم را کم می‌کند.",
            "تماشای خشونت جانشین عمل است.",
            "کاهش تنش رفتار را کم می‌کند.",
            "اثر تخلیه کوتاه‌مدت است.",
        ],
        principles=[
            "شواهد تخلیه را با احتیاط بخوان.",
            "تنظیم هیجان را جای تخلیه بگذار.",
            "به برانگیختگی محتوا توجه کن.",
            "تفاوت فردی را بسنج.",
            "از توجیه علمی خشونت پرهیز کن.",
            "اثر بلندمدت را نیز بررسی کن.",
        ],
        critiques=[
            "شواهد تجربی ضعیف است.",
            "سنجش تخلیه دشوار است.",
            "تفاوت فردی را کم می‌بیند.",
            "به برانگیختگی محتوا کم توجه دارد.",
            "خطر توجیه خشونت دارد.",
            "به تنظیم هیجان کم می‌پردازد.",
            "به اثر بلندمدت کم توجه است.",
            "نمونه‌های آزمایشگاهی محدودند.",
        ],
        critique_text="منتقدان می‌گویند فرضیهٔ کاتارسیس با شواهد تجربی ضعیف روبه‌روست و پژوهش‌های جدیدتر نشان می‌دهند تخلیه خشونت، پرخاشگری را افزایش می‌دهد؛ با این حال، بحث آن در سیاست رسانه و روان‌شناسی خشم همچنان زنده است.",
        applications=[
            "تحلیل بازی خشونت‌آمیز.",
            "پژوهش تماشای خشونت.",
            "مطالعهٔ ورزش رقابتی.",
            "تحلیل برنامهٔ خشم.",
            "سیاست تنظیم محتوا.",
            "پژوهش تنظیم هیجان.",
            "آموزش مدیریت خشم.",
            "تحلیل بحث خشونت رسانه‌ای.",
            "مطالعهٔ باور عمومی به تخلیه خشم.",
            "پژوهش اثر بازی خشونت‌آمیز بر خشم بازیکن.",
            "تحلیل طراحی بازی برای تنظیم هیجان.",
            "پژوهش اثر تماشای ورزش بر خشم.",
        ],
        example_text="فردی که پس از یک روز پرتنش به بازی خشونت‌آمیز روی می‌آورد، ممکن است احساس آرامش کوتاه‌مدت کند؛ اما پژوهش‌ها نشان می‌دهند همین بازی می‌تواند برانگیختگی و پرخاشگری بعدی او را بیشتر کند.",
        evolution="فروید و سنت روان‌کاوی مفهوم تخلیه را ساختند و فشباخ در سال ۱۹۶۱ آن را در رسانه آزمود؛ مرورهای دههٔ ۱۹۷۰ شواهد را محدود یافتند و بوشمن و همکاران در سال ۱۹۹۹ نشان دادند باور به کاتارسیس خودشکن است.",
        key_concepts=["کاتارسیس", "تخلیه هیجانی", "خشونت رسانه‌ای", "برانگیختگی", "تنظیم هیجان", "پرخاشگری"],
        theorists="زیگموند فروید، سیمور فشباخ، برد بوشمن و روی بامایستر.",
        theorists_text="فرضیه در سنت روان‌کاوی و روان‌شناسی پرخاشگری شکل گرفت.",
        model="تماشای خشونت به‌عنوان تخلیهٔ انگیزهٔ پرخاشگری، در برابر شواهدی که افزایش آن را نشان می‌دهند.",
        studies=[
            "آزمایش سال ۱۹۶۱ اثر مشروط را یافت.",
            "مرور دههٔ ۱۹۷۰ شواهد را محدود دید.",
            "آزمایش سال ۱۹۹۹ خودشکنی را نشان داد.",
            "مطالعهٔ بازی، پرخاشگری را سنجید.",
            "پژوهش ورزش، تخلیهٔ خشم را بررسی کرد.",
            "مطالعهٔ باور عمومی، کاتارسیس را تحلیل کرد.",
            "مطالعهٔ بلندمدت، عادت بازی را بررسی کرد.",
        ],
    ),
}

NAME_FIX = {
    "MC-560": ("فرضیهٔ اثر ارابه (همراهی با اکثریت)", "Bandwagon Effect Hypothesis", "عنوان کارت ترکیبی و مبهم بود و سال و نظریه‌پرداز نداشت؛ عنوان به صورت‌بندی سایمون ۱۹۵۴ اصلاح شد."),
    "MC-561": ("فرضیهٔ اثر زیردست (حمایت از بازنده)", "Underdog Effect Hypothesis", "عنوان کارت با واژهٔ نامأنوس «زیردستی» ثبت شده بود و سال نداشت؛ عنوان به مفهوم رایج اثر زیردست اصلاح شد."),
}
YEAR_FIX = {
    "MC-560": "کارت بدون سال و نظریه‌پرداز بود؛ صورت‌بندی اثر ارابه از سایمون ۱۹۵۴ است و محتوا بر پایهٔ سایمون ۱۹۵۴ و سیچی و کین ۱۹۸۲ بازنویسی شد.",
    "MC-561": "کارت بدون سال و نظریه‌پرداز بود؛ اثر زیردست در سایمون ۱۹۵۴ مطرح شد و محتوا بر پایهٔ همان منبع و سیچی و کین ۱۹۸۲ بازنویسی شد.",
    "MC-562": "بدنهٔ کارت برخلاف عنوان، اثر رسانه را تغییردهندهٔ باور توصیف کرده بود؛ محتوا بر پایهٔ لازارسفلد و همکاران ۱۹۴۸ و سیرز و فریدمن ۱۹۶۷ بازنویسی شد.",
    "MC-563": "بدنهٔ کارت قالب عمومی اقناع بود و به کاتارسیس مربوط نبود؛ محتوا بر پایهٔ فشباخ ۱۹۶۱ و بوشمن و همکاران ۱۹۹۹ بازنویسی و سال به ۱۹۶۱ اصلاح شد.",
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
                                       "verified": n_verified, "batch": 164}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH164 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
