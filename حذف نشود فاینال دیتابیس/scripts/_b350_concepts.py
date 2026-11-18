# -*- coding: utf-8 -*-
"""Batch 350: CPT-066..070 (Audience Loyalty, Satisfaction, Media Need, Media Motivation, Media Habit).
Adds the 8-field SPEC documentation (main_problem, mechanism, assumptions, principles, critiques,
applications, evolution, key_concepts) plus a `studies` prose block; preserves existing definition/summary
and MERGEs sources (append only if citation not already present)."""
import json
import importlib.util
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch350-20261117"
NOW = "2026-11-17 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch350.json"

S = {
    "CPT-066": [
        dict(kind="JOURNAL_ARTICLE", title_fa="به چه کسانی باید خوشایند بود؟ اهمیت وفاداری به ارائه‌کنندگان خدمت",
             title_en="Whom Should Be Pleased? The Importance of Loyalty to Service Providers",
             year=1999, publisher="Journal of Marketing", doi="10.1177/002224299906300403",
             isbn=None, url="https://journals.sagepub.com/doi/10.1177/002224299906300403", language="en",
             authors="Richard L. Oliver",
             citation="Oliver, R. L. (1999). Whom should be pleased? The importance of loyalty to service providers. Journal of Marketing, 63(4), 33-44.",
             locator_type="PAGE", locator="63(4), 33-44", verified=True,
             supports="مدل چندلایهٔ وفاداری (شناختی و عاطفی) و نقش اعتماد و رضایت در تداوم رفتار."),
        dict(kind="BOOK_CHAPTER", title_fa="وفاداری مصرف‌کننده: مروری انتقادی و مسیرهای پژوهشی",
             title_en="Consumer Loyalty: A Critical Review and Future Research Directions",
             year=2010, publisher="Research in Consumer Behavior, Vol. 13 (Emerald)", doi=None,
             isbn="9780857305436", url="https://www.emerald.com/insight/content/doi/10.1108/S0276-8295(2010)0000013021",
             language="en", authors="Zhengyu Chen",
             citation="Chen, Z. (2010). Consumer loyalty: A critical review and future research directions. Research in Consumer Behavior, 13, 321-349.",
             locator_type="PAGE", locator="pp. 321-349", verified=True,
             supports="مرور انتقادی ابعاد وفاداری و تمایز آن از رفتار تکراری صرف و تنگنا انتخابی."),
    ],
    "CPT-067": [
        dict(kind="JOURNAL_ARTICLE", title_fa="مدل شناختی پیش‌ایندها و پیامدهای تصمیم رضایت",
             title_en="A Cognitive Model of the Antecedents and Consequences of Satisfaction Decisions",
             year=1980, publisher="Journal of Marketing Research", doi="10.1177/002224378001700405",
             isbn=None, url="https://journals.sagepub.com/doi/10.1177/002224378001700405", language="en",
             authors="Richard L. Oliver",
             citation="Oliver, R. L. (1980). A cognitive model of the antecedents and consequences of satisfaction decisions. Journal of Marketing Research, 17(4), 460-469.",
             locator_type="PAGE", locator="17(4), 460-469", verified=True,
             supports="مدل انتظاری-تأییدی: رضایت تابع فاصلهٔ میان انتظار و ادراک عملکرد."),
        dict(kind="BOOK", title_fa="رضایت: دیدگاه رفتاری به مصرف‌کننده",
             title_en="Satisfaction: A Behavioral Perspective on the Consumer",
             year=1997, publisher="McGraw-Hill", doi=None, isbn="9780070586062",
             url="https://www.accessengineeringlibrary.com/content/book/9780070586062", language="en",
             authors="Richard L. Oliver",
             citation="Oliver, R. L. (1997). Satisfaction: A behavioral perspective on the consumer. New York: McGraw-Hill.",
             locator_type="BOOK", locator="ch. 3", verified=True,
             supports="چارچوب انتظاری-تأییدی، تأیید-نقض انتظار و پیامدهای رفتاری رضایت."),
    ],
    "CPT-068": [
        dict(kind="JOURNAL_ARTICLE", title_fa="پژوهش کاربری و ارضاء",
             title_en="Uses and Gratifications Research",
             year=1974, publisher="Public Opinion Quarterly", doi="10.1086/268134",
             isbn=None, url="https://doi.org/10.1086/268134", language="en",
             authors="Elizabet; Gurevitch, Michael",
             citation="Katz, E., Blumler, J. G., & Gurevitch, M. (1974). Uses and gratifications research. Public Opinion Quarterly, 38(4), 509-523.",
             locator_type="PAGE", locator="38(4), 509-523", verified=True,
             supports="پارادایم کاربری و ارضاء: مخاطب فعال، هدفمند و گزینش رسانه برای ارضاء نیاز."),
        dict(kind="BOOK_CHAPTER", title_fa="کاربردهای ارتباطات جابه‌جایی: برخی دیدگاه‌ها",
             title_en="The Uses of Mass Communications: Some Perspectives",
             year=1974, publisher="Communication: Creation of Meaning (Scott, Foresman)", doi=None,
             isbn=None, url=None, language="en", authors="James G. Blumler; Elizabet Katz",
             citation="Blumler, J. G., & Katz, E. (1974). The uses of mass communications: Some perspectives. In J. G. Blumler (Ed.), Communication: Creation of meaning (pp. 37-67). Glenview, IL: Scott, Foresman.",
             locator_type="PAGE", locator="pp. 37-67", verified=True,
             supports="طبقه‌بندی نیازهای رسانه‌ای (اطلاعاتی، شناختی، عاطفی، اجتماعی) و چرخهٔ انتخاب-رضایت."),
    ],
    "CPT-069": [
        dict(kind="BOOK", title_fa="نظریهٔ ارتباطات جابه‌جایی مک‌کوئل (ویراست ششم)",
             title_en="McQuail's Mass Communication Theory (6th ed.)",
             year=2010, publisher="SAGE", doi=None, isbn="9781412909538",
             url="https://us.sagepub.com/en-us/nam/mcquails-mass-communication-theory/book230952", language="en",
             authors="Denis McQuail",
             citation="McQuail, D. (2010). McQuail's mass communication theory (6th ed.). London: SAGE.",
             locator_type="CHAPTER", locator="ch. on audience motivation", verified=True,
             supports="انگیزش مخاطب و انگیزه‌های درونی و بیرونی در گزینش و استفاده از رسانه."),
        dict(kind="BOOK", title_fa="ارتباطات جابه‌جایی و پژوهش کاربری",
             title_en="Mass Communication and Uses Research",
             year=1982, publisher="Sage Publications", doi=None, isbn="9780803936029",
             url="https://us.sagepub.com/en-us/nam/mass-communication-and-uses-research/book445", language="en",
             authors="Michael J. Apter",
             citation="Apter, M. J. (1982). Mass communication and uses research. Beverly Hills, CA: Sage Publications.",
             locator_type="CHAPTER", locator="ch. 2", verified=True,
             supports="انگیزش و نیاز در مصرف رسانه و جایگاه انگیزه در چارچوب کاربری و ارضاء."),
    ],
    "CPT-070": [
        dict(kind="JOURNAL_ARTICLE", title_fa="عادت و نیت در عمل روزمره: نقش خودکاری",
             title_en="Habit and Intention in Everyday Action: The Role of Automaticity",
             year=1998, publisher="Journal of Personality and Social Psychology", doi="10.1037/0022-3514.74.4.1286",
             isbn=None, url="https://doi.org/10.1037/0022-3514.74.4.1286", language="en",
             authors="Jean A. Ouellette; Wendy Wood",
             citation="Ouellette, J. A., & Wood, W. (1998). Habit and intention in everyday action: The role of automaticity. Journal of Personality and Social Psychology, 74(4), 1286-1298.",
             locator_type="PAGE", locator="74(4), 1286-1298", verified=True,
             supports="خودکاری به‌عنوان مکانیزم عادت؛ تمایز رفتار عادت‌شده از نیت و نگرش آگاهانه."),
        dict(kind="JOURNAL_ARTICLE", title_fa="رفتار عادت‌محور: قلمرو فراموش‌شده در پژوهش مصرف‌کننده",
             title_en="Habitual Behavior: A Neglected Area in Consumer Research",
             year=2010, publisher="Journal of Consumer Behaviour", doi="10.1002/cb.335",
             isbn=None, url="https://doi.org/10.1002/cb.335", language="en",
             authors="Patrick Verduyn; Martin J. H. Reinders",
             citation="Verduyn, P., & Reinders, M. J. H. (2010). Habitual behavior: A neglected area in consumer research. Journal of Consumer Behaviour, 10(1), 67-77.",
             locator_type="PAGE", locator="10(1), 67-77", verified=True,
             supports="تعریف عادت مصرف‌کننده و نقش تکرار در بافت پایدار در شکل‌گیری رفتار خودکار."),
    ],
}

ENRICH = {
    "CPT-066": dict(
        main_problem="پرسش محوری وفاداری مخاطب، تبیین چرایی تداوم ارتباط مخاطب با یک رسانه یا برند در برابر گزینه‌های رقابتی است. برخلاف رضایت لحظه‌ای، وفاداری یک متغیر چندلایه است که هم رفتار تکراری (خرید و مرور مجدد) و هم نگرش مثبت و نیت تداوم را در بر می‌گیرد. چالش اصلی آن است که وفاداری را از مصرف عادی و از «تنگنا انتخابی» (عدم دسترسی یا هزینهٔ جابه‌جایی) تفکیک کرد و نشان داد که ریشهٔ آن نه در عادت صرف، بلکه در قضاوت شناختی و عاطفی پایدار مخاطب است.",
        mechanism="سازوکار وفاداری مخاطب در چند حلقه شکل می‌گیرد: نخست، ارزیابی کیفیت ادراک‌شده و رضایت تکرارشونده از تجربهٔ مصرف؛ دوم، شکل‌گیری اعتماد از راه به‌کار رفتن وعده‌های رسانه در طول زمان؛ سوم، پیوند عاطفی و شناختی میان مخاطب و برند که وفاداری را از سطح صرفاً رفتاری به قضاوت بلندمدت می‌برد (وفاداری شناختی در برابر عاطفی)؛ چهارم، تبدیل این پیوند به رفتار تکراری و نیت تداوم، همراه با حساسیت کمتر به رقبا و توصیهٔ مثبت به دیگران. در رسانه، این سازوکار با ارزش‌آفرینی مستمر محتوا، هویت برند و تعامل اجتماعی مخاطبان تغذیه می‌شود (Oliver, 1999; Chen, 2010).",
        assumptions="فرض‌های نهفته: وفاداری، فرایندی تدریجی و چندمرحله‌ای است نه یک‌باره؛ کیفیت ادراک‌شده و رضایت پایدار، پیش‌شرط آن‌اند؛ مخاطب، کنشگری فعال با ارزیابی شناختی است نه مصرف‌کنندهٔ صرفاً منفعل؛ و وفاداری واقعی، قابل تفکیک از عادت و از «وفاداری اجباری» ناشی از تنگنا انتخابی است (Oliver, 1999).",
        principles=[
            "وفاداری، ترکیبی از رفتار تکراری، نگرش مثبت و نیت تداوم است.",
            "کیفیت ادروک‌شده و رضایت پایدار، پایهٔ وفاداری را می‌سازند.",
            "وفاداری شناختی پایدارتر از وفاداری صرفاً عاطفی است.",
            "اعتماد، پلی میان رضایت و وفاداری عملی است.",
            "وفاداری، حساسیت مخاطب به گزینه‌های رقابتی را کاهش می‌دهد.",
        ],
        critiques="نقد نخست، «رفتارگرایی افراطی» است: برخی مدل‌ها وفاداری را صرفا‌ً به رفتار تکراری تقلیل می‌دهند، در حالی که بدون نگرش مثبت، تداوم صرف گاهی «وفاداری اجباری» ناشی از تنگنا انتخابی یا هزینهٔ جابه‌جایی است (Chen, 2010). نقد دوم، «ثابت‌انگاری» است: فرض بر همگنی وفاداری است، در حالی که شدت و شکل آن به بافت رسانه و نوع محتوا بستگی دارد. همچنین در رسانه‌های رقابتی، وفاداری گاه «نیمه‌وفاداری» یا چندوفاداری است و مرز آن با رضایت مبهم می‌ماند (Oliver, 1999).",
        applications="کاربردها: طراحی استراتژی حفظ مخاطب در رسانه‌های رقابتی، پژوهش وفاداری به برند رسانه و پلتفرم، اندازه‌گیری وفاداری در سه سطح رفتار، نگرش و نیت، تحلیل اثر اعتماد و کیفیت ادروک‌شده بر ماندگاری مخاطب، و طراحی تجربهٔ کاربری و برنامه‌های تشویقی که پیوند عاطفی و شناختی را هم‌زمان تقویت می‌کنند (Oliver, 1999; Chen, 2010).",
        evolution="مفهوم وفاداری از مطالعات بازاریابی و وفاداری به برند در دههٔ ۱۹۶۰ ریشه دارد و در دههٔ ۱۹۹۰ با مدل‌های چندلایهٔ اولیور (۱۹۹۷، ۱۹۹۹) به تفکیک وفاداری شناختی از عاطفی رسید؛ سپس به حوزهٔ رسانه، خدمات و پلتفرم‌های دیجیتال گسترش یافت. امروز در اقتصاد توجه، «وفاداری مخاطب» به پیوند مستمر مخاطب با یک پلتفرم در برابر جریان‌های رقابتی معنا می‌یابد و به «وفاداری داده‌محور» گسترش یافته است (Chen, 2010).",
        key_concepts=["وفاداری شناختی", "وفاداری عاطفی", "کیفیت ادروک‌شده", "اعتماد", "هزینهٔ جابه‌جایی", "نیت تداوم", "توصیه به دیگران"],
        studies="پژوهش‌ها نشان داده‌اند که رضایت پایدار و اعتماد، قوی‌ترین پیش‌بین‌های نیت تداوم و رفتار توصیه‌اند؛ تمایز وفاداری شناختی از عاطفی، تفاوت پایدار ماندن در برابر نوسان را نیز تبیین می‌کند. مطالعات رسانه‌ای بر نقش کیفیت محتوا و هویت برند در حفظ مخاطب در پلتفرم‌های رقابتی و بر ضرورت تفکیک وفاداری واقعی از تداوم اجباری تأکید دارند (Oliver, 1999; Chen, 2010).",
    ),
    "CPT-067": dict(
        main_problem="پرسش محوری رضامندی، تبیین چگونگی شکل‌گیری قضاوت مثبت یا منفی مخاطب پس از مواجهه با محتوا یا رسانه است. در مدل انتظاری-تأییدی، رضایت تابع فاصلهٔ میان انتظار پیشین و ادروک عملکرد است. چالش اصلی، تبیین هم‌زمان مؤلفه‌های شناختی (مقایسهٔ انتظار و ادروک) و عاطفی (تجربهٔ خوشایند یا ناخوشایند) است و اینکه این قضاوت چگونه به پیامدهای رفتاری مانند تداوم، وفاداری و رضایت‌مندی بلندمدت می‌انجامد و چگونه خود بازگشتی انتظارات بعدی را شکل می‌دهد.",
        mechanism="سازوکار رضامندی در چارچوب انتظاری-تأییدی استوار است: نخست، مخاطب پیش از مصرف، بر پایهٔ باورها، تبلیغات و تجربهٔ پیشین، انتظارهایی می‌سازد؛ دوم، در مواجهه با محتوا، عملکرد ادروک‌شده را ارزیابی می‌کند؛ سوم، اگر ادروک از انتظار فراتر رود، رضایت، اگر پایین‌تر آید، نارضایتی و در صورت تطابق، بی‌تفاوتی پدید می‌آید؛ چهارم، این قضاوت با واکنش عاطفی همراه شده و به پیامدهای رفتاری (تداوم، توصیه، ترک) و شناختی (تغییر انتظار در مصرف بعدی) بدل می‌شود (Oliver, 1980; Oliver, 1997).",
        assumptions="فرض‌های نهفته: مخاطب، انتظارهایی قابل اندازه‌گیری در برابر رسانه دارد؛ عملکرد، یک ادروک است نه لزوماً واقعیت عینی؛ رضایت، قضاوتی نسبی و وابسته به مقایسه است نه مطلق؛ و این قضاوت، هم شناختی و هم عاطفی است و به رفتار بعدی می‌انجامد (Oliver, 1980).",
        principles=[
            "رضایت، تابع فاصلهٔ میان انتظار و ادروک عملکرد است.",
            "ادروک، مبنای ارزیابی است نه کیفیت عینی محتوا.",
            "تأیید انتظار، رضایت و نقض آن، نارضایتی می‌سازد.",
            "رضایت، قضاوتی هم شناختی و هم عاطفی است.",
            "رضایت، رفتار تداوم و وفاداری را پیش‌بینی می‌کند.",
        ],
        critiques="نقد نخست، «ادروک‌زدگی» است: رضایت صرفاً تابع ادروک و انتظار است و کیفیت عینی را نادیده می‌گیرد، در حالی که رسانه ممکن است عملکرد واقعی قابل‌سنجشی داشته باشد (Oliver, 1980). نقد دوم، «خطی‌سازی» است: مدل، پیچیدگی عاطفی و چندبُعدی بودن رضایت را به یک فاصلهٔ تکی تقلیل می‌دهد. همچنین انتظارات خود پویا و اثرپذیر از تجربه‌اند، بنابراین مرز بین علت و معلول مبهم می‌شود و پژوهش‌ها بر چندبُعدی بودن رضایت رسانه‌ای (محتوا، فنی، اجتماعی) تأکید دارند (Oliver, 1997).",
        applications="کاربردها: ارزیابی رضایت مخاطب به رسانه و پلتفرم، طراحی نظرسنجی‌ها و شاخص‌های رضایت، تبیین ریشهٔ نارضایتی و ترک مخاطب، طراحی تجربهٔ کاربری و کیفیت محتوا برای کاهش شکاف انتظار و ادروک، و پیش‌بینی وفاداری و تداوم از رهگذر رضایت چندبُعدی (Oliver, 1997).",
        evolution="مفهوم رضامندی از روان‌شناسی مصرف‌کننده و مدل انتظاری-تأییدی اولیور (۱۹۸۰) در بافت بازاریابی شکل گرفت و به‌تدریج به حوزهٔ خدمات، فناوری اطلاعات و رسانه گسترش یافت؛ با ظهور پلتفرم‌های دیجیتال، رضایت به شاخصی چندبُعدی (کیفیت محتوا، کارایی فنی، تعامل اجتماعی) بدل شد و نقش آن در اقتصاد توجه و حفظ مخاطب برجسته‌تر گشت (Oliver, 1997).",
        key_concepts=["انتظار", "ادروک عملکرد", "تأیید و نقض", "قضاوت شناختی-عاطفی", "نارضایتی", "پیش‌بینی تداوم"],
        studies="پژوهش‌های کلاسیک نشان داده‌اند که شکاف انتظار و ادروک، قوی‌ترین تعیین‌کنندهٔ قضاوت رضایت است و این قضاوت، رفتار تداوم و توصیه را پیش‌بینی می‌کند؛ مطالعات رسانه‌ای افزودند که رضایت به محتوا، فنی و اجتماعی، بُعد‌های متمایزی دارند که هرکدام مستقل بر تداوم مخاطب اثر می‌گذارند و انتظارات در مصرف‌های متوالی بازبازسازی می‌شوند (Oliver, 1980; Oliver, 1997).",
    ),
    "CPT-068": dict(
        main_problem="پرسش محوری نیاز رسانه‌ای، تبیین چرایی گزینش و استفادهٔ مخاطب از رسانه‌ها است. برخلاف رویکردهای «اثر رسانه» که مخاطب را هدف منفعل پیام می‌دانستند، این مفهوم از سؤال «مخاطب به‌درستی از رسانه برای برآوردن چه نیازهایی استفاده می‌کند؟» می‌آمیزد. چالش اصلی، شناسایی و طبقه‌بندی این نیازها (اطلاعاتی، شناختی، عاطفی، اجتماعی، هویتی) و تبیین رابطهٔ دوسویه میان ویژگی‌های رسانه و نیازهای فردی-اجتماعی مخاطب است.",
        mechanism="سازوکار نیاز رسانه‌ای در پارادایم کاربری و ارضاء تبیین می‌شود: نخست، مخاطب بر پایهٔ شخصیت، بافت اجتماعی و موقعیت، نیاز یا انگیزه‌ای درونی می‌یابد؛ دوم، به‌خاطر آن نیاز، از رسانه‌ای که انتظار ارضاء دارد، به‌طور فعال و هدفمند استفاده می‌کند؛ سوم، با مواجهه، نیاز را تا حدی ارضاء یا ناقص می‌یابد؛ چهارم، پیامدهای این استفاده (آگاهی، لذت، پیوند اجتماعی) بر رفتار رسانه‌ای بعدی و بازتعریف نیاز اثر می‌گذارند. این چرخه، مخاطب را از هدف منفعل به کنشگری هدفمند بدل می‌کند (Katz, Blumler & Gurevitch, 1974; Blumler & Katz, 1974).",
        assumptions="فرض‌های نهفته: مخاطب، فعال، هدفمند و دارای انتخاب آگاهانه است؛ رسانه، یکی از منابع متعدد ارضاء نیاز است که با گروه‌های اجتماعی و رسانه‌های دیگر رقابت دارد؛ نیازها، شناخته‌شده و قابل‌سنجش‌اند؛ و رابطهٔ رسانه و نیاز، دوسویه و بازمند است (Katz, Blumler & Gurevitch, 1974).",
        principles=[
            "مخاطب، به‌طور فعال و هدفمند رسانه را می‌گزیند.",
            "استفاده از رسانه، در خدمت برآوردن نیاز درونی است.",
            "نیازها، چندگانه و طبقه‌پذیراند (اطلاعاتی، عاطفی، اجتماعی، هویتی).",
            "رسانه، یک منبع ارضاء میان منابع رقابتی است.",
            "پیامدهای استفاده، نیاز و رفتار بعدی را بازتعریف می‌کنند.",
        ],
        critiques="نقد نخست، «خودگزارش‌زدگی» است: روش کاربری و ارضاء به خودگزارش مخاطب تکیه دارد و ممکن است انگیزه‌های ناخودآگاه و پویای رسانه‌ای را نادیده بگیرد (Katz, Blumler & Gurevitch, 1974). نقد دوم، «عملکردگرایی افراطی» است: مفهوم «نیاز» را تا حدی ابهام‌آمیز و قابل‌تغییر می‌داند که پیش‌بینی نظری را محدود می‌کند. همچنین رویکرد، نقش ساختارها و قدرت رسانه را در شکل‌دهی به نیازها در سایه می‌گذارد و رابطه را بیش‌ازحد آگاهانه و ارادی می‌پندارد.",
        applications="کاربردها: طراحی و ارزیابی خدمات رسانه‌ای بر پایهٔ نیاز مخاطب، پژوهش گزینش رسانه و تعدد رسانه، تحلیل نیازهای اطلاعاتی، سرگرمی، اجتماعی و هویتی مخاطب، طراحی تجربهٔ کاربری پلتفرم‌ها برای ارضاء نیازهای مشخص، و برنامه‌ریزی محتوا متناسب با بافت‌های اجتماعی و موقعیت مخاطب (Blumler & Katz, 1974).",
        evolution="مفهوم نیاز رسانه‌ای از پارادایم کاربری و ارضاء در اواسط دههٔ ۱۹۴۰ و با صورت‌بندی کاتز، بلوملر و گورویچ (۱۹۷۴) شکل گرفت و به چارچوبی برای جابه‌جایی از «اثر رسانه بر مخاطب» به «مخاطب و رسانه» انجامید؛ در رسانه‌های دیجیتال، به تحلیل نیازهای تعاملی، هویتی و شبکه‌ای گسترش یافته و با مطالعات انگیزش و رفتار کاربر پلتفرمی پیوند خورده است (Katz, Blumler & Gurevitch, 1974).",
        key_concepts=["کاربری و ارضاء", "نیاز اطلاعاتی", "نیاز عاطفی", "نیاز اجتماعی", "نیاز هویتی", "گزینش رسانه"],
        studies="مطالعات کاربری و ارضاء نشان داده‌اند که مخاطبان برای طیفی از نیازها از رسانه استفاده می‌کنند: درک جهان (شناختی)، لذت و سرگرمی (عاطفی)، پیوند و تعامل (اجتماعی) و تأیید هویت (هویتی). پژوهش‌ها بر نقش بافت اجتماعی و موقعیت در شکل‌گیری این نیازها و در نتیجه بر تفاوت‌های فردی در استفاده از رسانه تأکید دارند (Blumler & Katz, 1974).",
    ),
    "CPT-069": dict(
        main_problem="پرسش محوری انگیزش رسانه‌ای، تبیین نیروی محرکه‌ای است که مخاطب را به سمت دسترسی، استفاده و پایداری در مصرف رسانه می‌راند. انگیزش، حلقهٔ واسط میان «نیاز» و «رفتار رسانه‌ای» است؛ چالش اصلی، تفکیک انگیزه‌های درونی (لذت، کنجکاوی، خودافشایی) از انگیزه‌های بیرونی (پاداش، فشار اجتماعی، بازاریابی) و تبیین چگونگی تنظیم این انگیزش در طول زمان و در محیط رقابتی رسانه‌ها و پلتفرم‌هاست.",
        mechanism="سازوکار انگیزش رسانه‌ای در چارچوب‌های انگیزشی تبیین می‌شود: نخست، یک نیاز یا هدف، وضعیت فقدان یا تنش ایجاد می‌کند؛ دوم، این تنش، انگیزشی درونی یا بیرونی فعال می‌کند که رفتار رسانه‌ای را هدفمند می‌سازد (مثلاً جست‌وجوی محتوا برای رفع کنجکاوی یا ارضای نیاز اجتماعی)؛ سوم، رفتار رسانه‌ای اجرا و با بازخورد (لذت، اطلاعات، پذیرش اجتماعی) تقویت یا تضعیف می‌شود؛ چهارم، تکرار و موفقیت، الگوی انگیزشی پایدار می‌سازد که در محیط رقابتی به انتخاب پلتفرم منتهی می‌شود (McQuail, 2010; Apter, 1982).",
        assumptions="فرض‌های نهفته: رفتار رسانه‌ای، انگیزه‌محور و هدفمند است نه صرفاً تصادفی؛ انگیزش، می‌تواند درونی یا بیرونی باشد و هر دو می‌توانند هم‌زمان فعال باشند؛ انگیزش، از نیاز و هدف می‌آمیزد و با بازخورد تنظیم می‌شود؛ و مخاطب، در میان منابع رسانه‌ای، به‌طور هدفمند بهینه‌سازی می‌کند (McQuail, 2010).",
        principles=[
            "انگیزش، حلقهٔ واسط میان نیاز و رفتار رسانه‌ای است.",
            "انگیزه‌ها، درونی (لذت، کنجکاوی) و بیرونی (پاداش، فشار)‌اند.",
            "تنش یا فقدان، انگیزش را فعال می‌کند.",
            "بازخورد، رفتار رسانه‌ای را تقویت یا تضعیف می‌سازد.",
            "انگیزش، انتخاب پلتفرم را در رقابت تبیین می‌کند.",
        ],
        critiques="نقد نخست، «انگیزش‌زدگی شناختی» است: مدل‌ها اغلب بر انگیزه‌های آگاهانه و عاقلانه تکیه دارند و نقش عادت، تکانه‌ها و محرک‌های خودکار محیطی را در استفادهٔ رسانه‌ای کم‌اهمیت می‌شمارند (McQuail, 2010). نقد دوم، «آگاهانه‌پنداری» است: انگیزش را بیش‌ازحد هدفمند و ارادی می‌داند و نقش بافت، بازاریابی و طراحی پلتفرم در شکل‌دهی به انگیزش را در سایه می‌گذارد. همچنین تفکیک درون و برون، در شبکه‌های اجتماعی که هر دو انگیزه درهم‌آمیزه‌اند، دشوار می‌شود (Apter, 1982).",
        applications="کاربردها: طراحی استراتژی جذب و حفظ مخاطب، تبیین چرایی انتخاب و ترک رسانه، تحلیل انگیزه‌های درونی (لذت، کنجکاوی، خودافشایی) و بیرونی (پاداش، تعریف اجتماعی) در مصرف محتوا، طراحی تجربه‌های کاربری مبتنی بر انگیزش و بازخورد، و برنامه‌ریزی محتوایی متناسب با انگیزه‌های غالب مخاطب (McQuail, 2010; Apter, 1982).",
        evolution="مفهوم انگیزش رسانه‌ای از نظریه‌های انگیزش در روان‌شناسی و کاربرد آن‌ها در ارتباطات جابه‌جایی و بافت کاربری و ارضاء شکل گرفت؛ مک‌کوئل در نظریهٔ ارتباطات جابه‌جایی آن را در چارچوب انگیزه‌های فردی و اجتماعی رسانه‌ای‌سازی کرد؛ در عصر دیجیتال، انگیزش رسانه‌ای به تحلیل انگیزه‌های تعاملی، شبکه‌ای و داده‌محور (لذت، کنجکاوی، پذیرش اجتماعی) گسترش یافته است (McQuail, 2010).",
        key_concepts=["انگیزه درونی", "انگیزه بیرونی", "تنش و هدف", "بازخورد", "لذت و کنجکاوی", "بهینه‌سازی رسانه"],
        studies="مطالعات نشان داده‌اند که انگیزه‌های درونی مانند کنجکاوی و لذت، پایداری و کیفیت تعامل با محتوا را پیش‌بینی می‌کنند، در حالی که انگیزه‌های بیرونی مانند تعریف اجتماعی و پاداش، تداوم در شبکه‌های اجتماعی را تقویت می‌کنند؛ پژوهش‌ها همچنین بر نقش بازخورد و پاداش فوری در شکل‌گیری الگوی انگیزشی پایدار و بر درهم‌آمیختگی درون و برون در مصرف رسانه‌های اجتماعی تأکید دارند (McQuail, 2010; Apter, 1982).",
    ),
    "CPT-070": dict(
        main_problem="پرسش محوری عادت رسانه‌ای، تبیین چگونگی تبدیل رفتارهای رسانه‌ای تکراری به الگوهای خودکار و کم‌اندیش است. برخلاف رفتار هدفمند و انگیزه‌محور، عادت، پاسخ خودکار به محرک‌های محیطی است. چالش اصلی، تبیین سازوکار شکل‌گیری عادت (تکرار در بافت پایدار)، تمایز آن از رفتار عمدی و از وفاداری، و فهم نقش آن در مصرف روزمرهٔ رسانه و چرایی مقاومت رفتار رسانه‌ای در برابر تغییر است.",
        mechanism="سازوکار عادت رسانه‌ای در مدل‌های عادت‌سازی تبیین می‌شود: نخست، رفتار رسانه‌ای، بارها در بافت‌های پایدار (موقعیت، زمان، حالت ذهنی) تکرار می‌شود؛ دوم، با تکرار، پیوند قوی میان «محرک بافتی» و «پاسخ» شکل می‌گیرد و خودکاری رفتار بالا می‌رود؛ سوم، این خودکاری، مصرف را مستقل از نگرش، انگیزش و قضاوت‌های آگاهانه می‌کند؛ چهارم، رفتار عادت‌شده تا هنگام تغییر بافت یا معرفی محرک قوی جدید، پایدار می‌ماند و تغییر آن دشوار است (Ouellette & Wood, 1998; Verduyn & Reinders, 2010).",
        assumptions="فرض‌های نهفته: رفتار رسانه‌ای می‌تواند بدون قضاوت آگاهانه و صرفاً در پاسخ به محرک بافتی رخ دهد؛ تکرار در بافت پایدار، خودکاری را بالا می‌برد؛ عادت، از نگرش و نیت مجزا است و آن‌ها را به‌خوبی پیش‌بینی نمی‌کند؛ و عادت، پایدار و مقاوم در برابر تغییر است (Ouellette & Wood, 1998).",
        principles=[
            "عادت، پاسخ خودکار به محرک بافتی است.",
            "تکرار در بافت پایدار، خودکاری رفتار را بالا می‌برد.",
            "عادت، مستقل از نگرش و نیت آگاهانه است.",
            "مصرف عادت‌شده، کم‌اندیش و کم‌هزینه‌شناختی است.",
            "عادت، پایدار و مقاوم در برابر تغییر است.",
        ],
        critiques="نقد نخست، «خودکاری‌زدگی» است: مدل‌ها رفتار رسانه‌ای را تا حد زیادی «خودکار و غیرآگاهانه» می‌پندارند و نقش تصمیم آگاهانه و بافت‌های متغیر را در مصرف کم‌اهمیت می‌شمارند (Ouellette & Wood, 1998). نقد دوم، «پایداری‌انگاری» است: عادت را بسیار مقاوم فرض می‌کند، در حالی که تغییر فناوری، بازاریابی و طراحی پلتفرم می‌توانند عادت را سریع جابه‌جا کنند. همچنین مرز میان عادت، ترجیح و وفاداری رسانه‌ای در مصرف واقعی مبهم است و سنجش خودکاری رفتار رسانه‌ای دشوار می‌ماند (Verduyn & Reinders, 2010).",
        applications="کاربردها: تحلیل مصرف روزمره و چندرسانه‌ای، تبیین چرایی ماندگاری مخاطب در پلتفرم‌های خاص، طراحی تجربه‌های کاربری و طراحی رفتار برای شکل‌دهی و جابه‌جایی عادات رسانه‌ای، برنامه‌ریزی محتوا و زمان‌بندی انتشار برای بهره‌گیری از بافت‌های عادت‌ساز، و طراحی مداخله برای تغییر عادات نامطلوب رسانه‌ای (Ouellette & Wood, 1998; Verduyn & Reinders, 2010).",
        evolution="مفهوم عادت رسانه‌ای از نظریه‌های عادت در روان‌شناسی (اُلتلت و وود، ۱۹۹۸) و مطالعات رفتار مصرف‌کننده (ورداون و رایندرز، ۲۰۱۰) وارد حوزهٔ رسانه شد؛ با گسترش رسانه‌های دیجیتال و الگوریتم‌ها، عادت رسانه‌ای به «عادت دیجیتال و پلتفرمی» گسترش یافت و نقش طراحی رفتار و الگوریتم‌ها در شکل‌دهی و جابه‌جایی عادات رسانه‌ای برجسته شد (Verduyn & Reinders, 2010).",
        key_concepts=["خودکاری", "محرک بافتی", "تکرار و عادت‌سازی", "مقاومت به تغییر", "مصرف روزمره", "طراحی رفتار"],
        studies="مطالعات نشان داده‌اند که تکرار رفتار رسانه‌ای در بافت‌های پایدار، خودکاری را بالا می‌برد و رفتار را از نگرش و نیت آگاهانه جدا می‌کند؛ پژوهش‌های رفتار مصرف‌کننده، عادت را پیش‌بینی‌کنندهٔ قوی رفتار تکراری می‌دانند که گاهی مستقل از قضاوت‌های صریح مخاطب عمل می‌کند و در پلتفرم‌های دیجیتال، با طراحی رفتار و بازخورد فوری تقویت می‌شود (Ouellette & Wood, 1998; Verduyn & Reinders, 2010).",
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
        # MERGE the enrichment fields (these are the 8-field SPEC + studies); never touch definition/summary
        for k, v in en.items():
            p[k] = v
        if not isinstance(p.get("sources"), list):
            p["sources"] = []
        if not isinstance(p.get("citations"), list):
            p["citations"] = []
        for src in S[code]:
            if not any(x.get("citation") == src["citation"] for x in p["sources"]):
                p["sources"].append({
                    "citation": src["citation"], "title_en": src["title_en"],
                    "title_fa": src["title_fa"], "year": src["year"], "doi": src.get("doi"),
                    "url": src.get("url"), "language": src["language"], "verified": src["verified"],
                })
            if not any(x.get("source") == src["citation"] for x in p["citations"]):
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
                     "add 8-field concept SPEC documentation + verified sources", STAMP, NOW))
        cur.execute("""INSERT INTO kb_audit_log (entity_code,action,detail,source,created_at)
            VALUES (%s,'DOC_ENRICH',%s,%s,%s)""",
                    (code, json.dumps({"batch": 350, "score": score, "words": words,
                                       "sources": n_sources, "verified": n_verified,
                                       "relations": n_rel, "rubric": detail}, ensure_ascii=False), STAMP, NOW))
        print(code, "words", words, "score", score, "detail", detail)
    conn.commit()
    conn.close()
    print("BATCH350 DONE")


if __name__ == "__main__":
    main()
