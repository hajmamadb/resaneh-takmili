# -*- coding: utf-8 -*-
"""Batch 177 (WORK): MC-576 confirmation bias, MC-578 false consensus, MC-579 repetition in persuasion, MC-580 halo effect."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch177-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch177.json"

WORK_MAPPING = {"entity_type": "WORK", "content_type": "اثر رسانه‌ای (پدیده)", "needs_review": False}

S = {
    "MC-576": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="On the Failure to Eliminate Hypotheses in a Conceptual Task",
             title_fa="دربارهٔ ناکامی در حذف فرضیه‌ها در یک تکلیف مفهومی",
             authors="Wason, P. C.", year=1960,
             publisher="Quarterly Journal of Experimental Psychology, 12(3), 129-140",
             doi="10.1080/17470216008416717",
             url="https://doi.org/10.1080/17470216008416717",
             language="en", isbn=None,
             citation="Wason, P. C. (1960). On the failure to eliminate hypotheses in a conceptual task. Quarterly Journal of Experimental Psychology, 12(3), 129-140.",
             locator="12(3), pp. 129-140", locator_type="page_range",
             supports="original 2-4-6 task evidence of hypothesis-confirming search", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Confirmation Bias: A Ubiquitous Phenomenon in Many Guises",
             title_fa="سوگیری تأیید: پدیده‌ای فراگیر در چهره‌های گوناگون",
             authors="Nickerson, R. S.", year=1998,
             publisher="Review of General Psychology, 2(2), 175-220",
             doi="10.1037/1089-2680.2.2.175",
             url="https://doi.org/10.1037/1089-2680.2.2.175",
             language="en", isbn=None,
             citation="Nickerson, R. S. (1998). Confirmation bias: A ubiquitous phenomenon in many guises. Review of General Psychology, 2(2), 175-220.",
             locator="2(2), pp. 175-220", locator_type="page_range",
             supports="comprehensive review across memory, judgment, science and policy", verified=True),
    ],
    "MC-578": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="The False Consensus Effect: An Egocentric Bias in Social Perception and Attribution Processes",
             title_fa="اثر اجماع کاذب: سوگیری خودمحور در ادراک اجتماعی و فرایندهای اسناد",
             authors="Ross, L., Greene, D., & House, P.", year=1977,
             publisher="Journal of Experimental Social Psychology, 13(3), 279-301",
             doi="10.1016/0022-1031(77)90049-X",
             url="https://doi.org/10.1016/0022-1031(77)90049-X",
             language="en", isbn=None,
             citation="Ross, L., Greene, D., & House, P. (1977). The false consensus effect: An egocentric bias in social perception and attribution processes. Journal of Experimental Social Psychology, 13(3), 279-301.",
             locator="13(3), pp. 279-301", locator_type="page_range",
             supports="original four-study demonstration and label", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Ten Years of Research on the False-Consensus Effect: An Empirical and Theoretical Review",
             title_fa="ده سال پژوهش دربارهٔ اثر اجماع کاذب: مروری تجربی و نظری",
             authors="Marks, G., & Miller, N.", year=1987,
             publisher="Psychological Bulletin, 102(1), 72-90",
             doi="10.1037/0033-2909.102.1.72",
             url="https://doi.org/10.1037/0033-2909.102.1.72",
             language="en", isbn=None,
             citation="Marks, G., & Miller, N. (1987). Ten years of research on the false-consensus effect: An empirical and theoretical review. Psychological Bulletin, 102(1), 72-90.",
             locator="102(1), pp. 72-90", locator_type="page_range",
             supports="review of mechanisms, moderators and measurement issues", verified=True),
    ],
    "MC-579": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Attitudinal Effects of Mere Exposure",
             title_fa="اثرهای نگرشی مواجههٔ صرف",
             authors="Zajonc, R. B.", year=1968,
             publisher="Journal of Personality and Social Psychology, 9(2, Pt. 2), 1-27",
             doi="10.1037/h0025848",
             url="https://doi.org/10.1037/h0025848",
             language="en", isbn=None,
             citation="Zajonc, R. B. (1968). Attitudinal effects of mere exposure. Journal of Personality and Social Psychology, 9(2, Pt. 2), 1-27.",
             locator="9(2, Pt. 2), pp. 1-27", locator_type="page_range",
             supports="frequency-affect hypothesis and mere exposure experiments", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Effects of Message Repetition and Position on Cognitive Response, Recall, and Persuasion",
             title_fa="اثر تکرار و جایگاه پیام بر پاسخ شناختی، یادآوری و اقناع",
             authors="Cacioppo, J. T., & Petty, R. E.", year=1979,
             publisher="Journal of Personality and Social Psychology, 37(1), 97-109",
             doi="10.1037/0022-3514.37.1.97",
             url="https://doi.org/10.1037/0022-3514.37.1.97",
             language="en", isbn=None,
             citation="Cacioppo, J. T., & Petty, R. E. (1979). Effects of message repetition and position on cognitive response, recall, and persuasion. Journal of Personality and Social Psychology, 37(1), 97-109.",
             locator="37(1), pp. 97-109", locator_type="page_range",
             supports="repetition effects on cognitive response and persuasion", verified=True),
    ],
    "MC-580": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="A Constant Error in Psychological Ratings",
             title_fa="خطای ثابت در ارزشیابی‌های روان‌شناختی",
             authors="Thorndike, E. L.", year=1920,
             publisher="Journal of Applied Psychology, 4(1), 25-29",
             doi="10.1037/h0071663",
             url="https://doi.org/10.1037/h0071663",
             language="en", isbn=None,
             citation="Thorndike, E. L. (1920). A constant error in psychological ratings. Journal of Applied Psychology, 4(1), 25-29.",
             locator="4(1), pp. 25-29", locator_type="page_range",
             supports="original observation of cross-trait rating contamination", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Halo Effect: Evidence for Unconscious Alteration of Judgments",
             title_fa="اثر هاله: شواهدی از تغییر ناخودآگاه قضاوت‌ها",
             authors="Nisbett, R. E., & Wilson, T. D.", year=1977,
             publisher="Journal of Personality and Social Psychology, 35(4), 250-256",
             doi="10.1037/0022-3514.35.4.250",
             url="https://doi.org/10.1037/0022-3514.35.4.250",
             language="en", isbn=None,
             citation="Nisbett, R. E., & Wilson, T. D. (1977). The halo effect: Evidence for unconscious alteration of judgments. Journal of Personality and Social Psychology, 35(4), 250-256.",
             locator="35(4), pp. 250-256", locator_type="page_range",
             supports="experimental evidence that halo operates without awareness", verified=True),
    ],
}

ENRICH = {
    "MC-576": dict(
        year=1960,
        mapping=WORK_MAPPING,
        summary="سوگیری تأیید تمایل به جست‌وجو، تفسیر و یادآوری اطلاعاتی است که باورهای موجود را تأیید می‌کند. واتسون در سال ۱۹۶۰ با تکلیف ۲-۴-۶ نشان داد شرکت‌کنندگان برای کشف قاعده، تنها نمونه‌های مثبت می‌آزمایند و از آزمون نمونه‌هایی که فرضیه را رد می‌کنند پرهیز می‌کنند. این راهبرد مثبت‌گرا سبب می‌شود فرضیه‌های نادرست حذف نشوند. نیکرسون در سال ۱۹۹۸ با مروری فراگیر نشان داد سوگیری تأیید در حافظه، قضاوت، پژوهش علمی، پزشکی، حقوق و سیاست در چهره‌های گوناگون ظاهر می‌شود. سازوکارهای آن شامل دسترسی گزینشی، تفسیر هم‌سو و مقاومت در برابر شواهد ناهم‌سو است. سوگیری تأیید با سوگیری خودی، مواجههٔ گزینشی و اثر تداوم باور پیوند دارد. نقدها بر ابهام مفهومی، تنوع تکالیف و تفکیک انگیزه از شناخت تأکید دارند.",
        definition="سوگیری تأیید تمایل نظام‌مند به جست‌وجو، تفسیر و به‌یادآوری شواهد هم‌سو با باور موجود و نادیده گرفتن شواهد ناهم‌سو است.",
        main_problem="چرا افراد به‌جای آزمون جدی فرضیه‌های رقیب، شواهد تأییدکننده را ترجیح می‌دهند و این تمایل چگونه در قضاوت و تصمیم نهادینه می‌شود.",
        mechanism="فرد فرضیهٔ محبوب را با نمونه‌های مثبت می‌آزماید؛ توجه و حافظه اطلاعات هم‌سو را برجسته می‌کند و شواهد ناهم‌سو با تفسیر دوباره بی‌اثر می‌شود، در نتیجه فرضیه بدون آزمون جدی پایدار می‌ماند.",
        assumptions=[
            "افراد فرضیهٔ محبوب را زودتر شکل می‌دهند.",
            "آزمون نمونه‌های مثبت آسان‌تر از آزمون نمونه‌های منفی است.",
            "توجه به شواهد هم‌سو گزینشی است.",
            "حافظه اطلاعات تأییدکننده را بهتر نگه می‌دارد.",
            "شواهد ناهم‌سو دوباره تفسیر می‌شود.",
            "سوگیری در قضاوت و تصمیم مشترک است.",
            "انگیزه و شناخت هر دو دخیل‌اند.",
            "آگاهی از سوگیری آن را کامل حذف نمی‌کند.",
        ],
        principles=[
            "فرضیهٔ رقیب را صریح بساز.",
            "شواهد ناهم‌سو را فعالانه جست‌وجو کن.",
            "آزمون منفی را در طرح بگنجان.",
            "تفسیر شواهد را کورکورانه بسنج.",
            "منبع و انگیزهٔ قضاوت را جدا کن.",
            "تصمیم را با معیار پیشین بسنج.",
            "از تأیید اجتماعی زودهنگام بپرهیز.",
        ],
        critiques=[
            "مفهوم آن بیش از اندازه گسترده است.",
            "تکالیف آزمایشگاهی ساختگی‌اند.",
            "تفکیک انگیزه و شناخت دشوار است.",
            "اندازهٔ اثر در زمینه‌ها متغیر است.",
            "به نقش فرهنگ کم توجه است.",
            "به تصمیم گروهی کم می‌پردازد.",
            "به شواهد میدانی کم تکیه دارد.",
            "برخی یافته‌ها بازآزمایی نشده‌اند.",
            "به نقش آموزش کم توجه است.",
            "مرز آن با سوگیری خودی روشن نیست.",
        ],
        critique_text="منتقدان می‌گویند سوگیری تأیید چتری برای پدیده‌های ناهمگون است و تکالیف آزمایشگاهی آن به زندگی واقعی تعمیم‌پذیری محدودی دارد؛ با این حال واتسون و نیکرسون نشان دادند ترجیح شواهد هم‌سو الگویی پایدار و فراگیر در قضاوت انسان است.",
        applications=[
            "تحلیل خبر جعلی و اتاق پژواک.",
            "پژوهش مواجههٔ گزینشی.",
            "مطالعهٔ تصمیم پزشکی.",
            "تحلیل خطای تحقیق جنایی.",
            "پژوهش سرمایه‌گذاری.",
            "مطالعهٔ داوری خبری.",
            "تحلیل استخدام و گزینش.",
            "پژوهش تحلیل اطلاعات.",
            "مطالعهٔ آموزش انتقادی.",
            "تحلیل تصمیم سازمانی.",
            "پژوهش آزمون فرضیه.",
            "مطالعهٔ قطب‌بندی سیاسی.",
            "مطالعهٔ سوگیری تأیید در گزارش‌دهی خبری و انتخاب منبع.",
            "پژوهش سوگیری تأیید در تصمیم سرمایه‌گذاران خرد و داوری همتا.",
            "تحلیل سوگیری تأیید در تشخیص پزشکی و بازبینی اسناد تاریخی.",
            "پژوهش سوگیری تأیید در گزینش کارکنان سازمان‌های دولتی.",
        ],
        example_text="خبرنگاری که فرضیهٔ فساد یک مدیر را در ذهن دارد، تنها اسناد هم‌سو را دنبال می‌کند و اسناد تبرئه‌کننده را نادیده می‌گیرد؛ همین چرخه فرضیه را بدون آزمون جدی تقویت می‌کند.",
        evolution="واتسون در ۱۹۶۰ راهبرد آزمون مثبت را در تکلیف ۲-۴-۶ نشان داد و در ۱۹۶۸ تکلیف انتخاب را افزود؛ نیکرسون در ۱۹۹۸ مرور فراگیری منتشر کرد و پژوهش‌های بعدی سوگیری را به رسانه، اینترنت و تصمیم الگوریتمی گستراندند.",
        key_concepts=["راهبرد آزمون مثبت", "تأیید فرضیه", "مواجههٔ گزینشی", "سوگیری خودی", "تداوم باور", "تفسیر هم‌سو"],
        theorists="پیتر واتسون و ریموند نیکرسون.",
        theorists_text="واتسون در سنت روان‌شناسی استدلال اثر را کشف کرد و نیکرسون آن را به مروری فراگیر در علوم و سیاست گسترد.",
        model="مدل آزمون مثبت: فرد فرضیه را با نمونه‌های هم‌سو می‌آزماید و شواهد ناهم‌سو را دوباره تفسیر می‌کند، در نتیجه فرضیه حذف نمی‌شود.",
        studies=[
            "تکلیف ۲-۴-۶ در ۱۹۶۰.",
            "تکلیف انتخاب واتسون در ۱۹۶۸.",
            "مرور نیکرسون در ۱۹۹۸.",
            "پژوهش راهبرد آزمون مثبت.",
            "مطالعهٔ مواجههٔ گزینشی.",
            "تحلیل تداوم باور.",
            "پژوهش تفسیر هم‌سو.",
            "مطالعهٔ قضاوت خبری.",
            "تحلیل تصمیم پزشکی.",
            "پژوهش سرمایه‌گذاری.",
            "مطالعهٔ تحلیل اطلاعات.",
            "تحلیل قطب‌بندی سیاسی.",
        ],
    ),
    "MC-578": dict(
        year=1977,
        mapping=WORK_MAPPING,
        summary="اثر اجماع کاذب سوگیری خودمحور در برآورد فراوانی باورها و رفتارهای دیگران است: افراد گمان می‌کنند موضع و انتخاب خودشان در جامعه شایع‌تر از آن است که هست. راس، گرین و هاوس در سال ۱۹۷۷ با چهار مطالعه نشان دادند افراد هنگام برآورد سهم دیگران، پاسخ خود را نقطهٔ مرجع می‌گیرند و کسانی که رفتار متفاوتی برمی‌گزینند، آن را نابهنجارتر می‌بینند. تبیین‌های رقیب شامل مواجههٔ گزینشی، دسترسی‌پذیری، اسناد علّی و انگیزهٔ حمایت اجتماعی است. مارکس و میلر در ۱۹۸۷ با مرور ده سال پژوهش، سازوکارها و مشکلات سنجش را نظام‌مند کردند. این اثر در ادراک سیاسی، نظرسنجی و شبکه‌های اجتماعی اهمیت دارد، زیرا تصور اجماع، مشارکت و قطب‌بندی را تقویت می‌کند. نقدها بر اشکال آماری، آمیختگی با خطای نرخ پایه و ناهمگونی اندازهٔ اثر تأکید دارند.",
        definition="اثر اجماع کاذب برآورد بیش از اندازهٔ فراوانی باورها، ترجیحات و رفتارهای خود فرد در جامعه است.",
        main_problem="چرا افراد سهم دیگرانی را که مانند آن‌ها فکر یا رفتار می‌کنند بیش از واقع برآورد می‌کنند و این برآورد بر ادراک اجتماعی چه اثری دارد.",
        mechanism="فرد پاسخ خود را در دسترس‌ترین نمونه می‌یابد، اطرافیان هم‌سو را بیشتر می‌بیند و علت رفتار خود را موقعیتی و رفتار مخالفان را شخصیتی می‌داند؛ این چرخه برآورد فراوانی را به سمت خود می‌کشاند.",
        assumptions=[
            "پاسخ خود فرد نقطهٔ مرجع برآورد است.",
            "اطرافیان هم‌سو بیشتر در دسترس‌اند.",
            "مواجههٔ گزینشی ادراک فراوانی را جهت می‌دهد.",
            "اسناد علّی رفتار خود و دیگران نامتقارن است.",
            "انگیزهٔ حمایت اجتماعی برآورد را تقویت می‌کند.",
            "اجماع ادراک‌شده بر تصمیم اثر می‌گذارد.",
            "اثر در باورهای مهم‌تر قوی‌تر است.",
            "برآورد با اطلاعات آماری اصلاح می‌شود.",
        ],
        principles=[
            "برآورد فراوانی را با داده مقایسه کن.",
            "مواجههٔ گزینشی را در تحلیل بگنجان.",
            "اسناد خود و دیگران را جدا بسنج.",
            "نقش انگیزه را کنترل کن.",
            "خطای نرخ پایه را تفکیک کن.",
            "به زمینهٔ فرهنگی توجه کن.",
            "از فرض اجماع در کمپین بپرهیز.",
        ],
        critiques=[
            "اشکال آماری در سنجش آن مطرح است.",
            "با خطای نرخ پایه آمیخته است.",
            "اندازهٔ اثر ناهمگون است.",
            "به تفاوت فرهنگی کم توجه است.",
            "به نقش شبکهٔ اجتماعی کم می‌پردازد.",
            "سنجش فراوانی واقعی دشوار است.",
            "به انگیزه کم توجه می‌کند.",
            "به موضوع‌های حساس کم پرداخته است.",
            "تعمیم آزمایشگاهی محدود است.",
            "مرز آن با خودمحوری روشن نیست.",
        ],
        critique_text="منتقدان می‌گویند بخشی از اثر اجماع کاذب به خطای نرخ پایه و اشکال آماری برمی‌گردد و سنجش فراوانی واقعی دشوار است؛ با این حال راس و همکاران و مرور مارکس و میلر نشان دادند خودمحوری در برآورد اجماع الگویی پایدار و اثرگذار است.",
        applications=[
            "تحلیل ادراک سیاسی.",
            "پژوهش نظرسنجی.",
            "مطالعهٔ اتاق پژواک.",
            "تحلیل مشارکت انتخاباتی.",
            "پژوهش مذاکره.",
            "مطالعهٔ ادراک ریسک.",
            "تحلیل بازاریابی.",
            "پژوهش کمپین سلامت.",
            "مطالعهٔ تصمیم هیئت‌منصفه.",
            "تحلیل سازمان و تیم.",
            "پژوهش رسانهٔ اجتماعی.",
            "مطالعهٔ قطب‌بندی سیاسی.",
            "مطالعهٔ اجماع کاذب در ادراک نتایج انتخابات.",
            "پژوهش اجماع کاذب در مصرف رسانه و انتخاب خبر.",
            "تحلیل اجماع کاذب در تصمیم گروه‌های کاری سازمان.",
            "مطالعهٔ اجماع کاذب در برآورد خطر سلامت عمومی.",
        ],
        example_text="کاربری که در شبکهٔ اجتماعی خود دیدگاه خاصی را پرتکرار می‌بیند، گمان می‌کند بیشتر جامعه همان دیدگاه را دارد و مخالفان را اقلیتی نابهنجار می‌پندارد؛ همین برآورد، قطب‌بندی را تشدید می‌کند.",
        evolution="راس و همکاران در ۱۹۷۷ اثر را نام‌گذاری و با چهار مطالعه نشان دادند؛ مارکس و میلر در ۱۹۸۷ مرور نظری و تجربی ارائه کردند و پژوهش‌های بعدی اثر را به شبکه‌های اجتماعی، نظرسنجی و کمپین گستراندند.",
        key_concepts=["برآورد اجماع", "خودمحوری", "مواجههٔ گزینشی", "دسترسی‌پذیری", "اسناد نامتقارن", "نرخ پایه"],
        theorists="لی راس، دیوید گرین و پاملا هاوس.",
        theorists_text="راس در سنت شناخت اجتماعی اثر را صورت‌بندی کرد و مارکس و میلر سازوکارهای آن را مرور کردند.",
        model="مدل خودمحوری در برآورد اجماع: پاسخ خود، نمونهٔ در دسترس است و با مواجههٔ گزینشی و اسناد نامتقارن به برآورد فراوانی تعمیم می‌یابد.",
        studies=[
            "چهار مطالعهٔ راس و همکاران در ۱۹۷۷.",
            "مرور مارکس و میلر در ۱۹۸۷.",
            "پژوهش برآورد فراوانی.",
            "مطالعهٔ مواجههٔ گزینشی.",
            "تحلیل ادراک سیاسی.",
            "پژوهش نظرسنجی.",
            "مطالعهٔ شبکهٔ اجتماعی.",
            "تحلیل تصمیم هیئت‌منصفه.",
            "پژوهش ادراک ریسک.",
            "مطالعهٔ کمپین سلامت.",
            "تحلیل مذاکره.",
            "پژوهش قطب‌بندی سیاسی.",
        ],
    ),
    "MC-579": dict(
        year=1968,
        mapping=WORK_MAPPING,
        summary="اثر تکرار در اقناع به تغییر نگرش در نتیجهٔ مواجههٔ مکرر با یک محرک یا پیام اشاره دارد. زایونس در سال ۱۹۶۸ با فرضیهٔ بسامد-احساس نشان داد مواجههٔ صرف و مکرر با یک محرک، نگرش فرد به آن را مثبت‌تر می‌کند، حتی وقتی محرک بی‌معنا و آگاهی از تکرار کم باشد. کاکیوپو و پتی در ۱۹۷۹ نشان دادند تکرار پیام اقناعی پاسخ شناختی و یادآوری را افزایش می‌دهد، اما اقناع تا حدی بالا می‌رود و با تکرار بیش از حد افت می‌کند و منحنی وارونه می‌سازد. پس تکرار متوسط معمولاً بهترین اثر را دارد و تکرار زیاد به خستگی و مقاومت می‌انجامد. این اثر در تبلیغات، کمپین سیاسی و پیام سلامت کاربرد گسترده دارد. نقدها بر تفاوت مواجههٔ صرف با اقناع، وابستگی اثر به محتوا و فرد و دشواری تعیین آستانهٔ بهینه تأکید دارند.",
        definition="اثر تکرار در اقناع تغییر نگرش یا افزایش یادآوری پیام در نتیجهٔ ارائهٔ مکرر آن است که تا آستانه‌ای افزایش و سپس کاهش می‌یابد.",
        main_problem="چرا تکرار پیام نگرش را تغییر می‌دهد، چرا این اثر تا حدی افزایش و سپس کاهش می‌یابد و آستانهٔ بهینهٔ تکرار چگونه تعیین می‌شود.",
        mechanism="تکرار دسترسی و روانی پردازش محرک را بالا می‌برد و پاسخ‌های شناختی بیشتری برمی‌انگیزد؛ تا وقتی پردازش تازه ادامه دارد اقناع افزایش می‌یابد، اما تکرار بیش از حد پاسخ‌های منفی و خستگی می‌سازد و اثر را برمی‌گرداند.",
        assumptions=[
            "مواجههٔ مکرر نگرش را مثبت‌تر می‌کند.",
            "آشنا بودن محرک احساس مثبت می‌سازد.",
            "تکرار پاسخ شناختی را افزایش می‌دهد.",
            "یادآوری با تکرار بهتر می‌شود.",
            "اقناع با تکرار متوسط بیشینه است.",
            "تکرار زیاد خستگی و مقاومت می‌آورد.",
            "اثر به محتوای پیام وابسته است.",
            "تفاوت فردی آستانهٔ بهینه را جابه‌جا می‌کند.",
        ],
        principles=[
            "بسامد تکرار را در طرح بسنج.",
            "منحنی وارونه را الگو بگیر.",
            "خستگی و عادت‌زدگی را پایش کن.",
            "تکرار را با محتوای تازه بیامیز.",
            "یادآوری را جدا از نگرش بسنج.",
            "تفاوت مخاطب را در بسامد بگنجان.",
            "از تکرار بی‌وقفه و یکنواخت بپرهیز.",
        ],
        critiques=[
            "مواجههٔ صرف با اقناع یکسان نیست.",
            "آستانهٔ بهینه یکدست نیست.",
            "به محتوای پیام کم توجه است.",
            "به تفاوت فردی کم می‌پردازد.",
            "بیشتر شواهد آزمایشگاهی است.",
            "اثر بلندمدت کم سنجیده شده است.",
            "به زمینهٔ فرهنگی کم توجه است.",
            "خستگی تبلیغاتی کم مدل شده است.",
            "سنجش نگرش ناهمگون است.",
            "به رسانهٔ چندکاناله کم می‌پردازد.",
        ],
        critique_text="منتقدان می‌گویند اثر تکرار بیش از آنکه قانونی ساده باشد، تابع محتوا، مخاطب و زمینه است و آستانهٔ بهینهٔ آن یکدست نیست؛ با این حال زایونس و کاکیوپو و پتی نشان دادند تکرار متوسط می‌تواند نگرش و یادآوری را واقعاً افزایش دهد.",
        applications=[
            "تحلیل بسامد تبلیغات.",
            "پژوهش کمپین انتخاباتی.",
            "مطالعهٔ شعار برند.",
            "تحلیل پیام سلامت.",
            "پژوهش آگهی تلویزیونی.",
            "مطالعهٔ موسیقی تبلیغاتی.",
            "تحلیل تبلیغات محیطی.",
            "پژوهش کمپین خیریه.",
            "مطالعهٔ ارتباطات بحران.",
            "تحلیل طراحی رابط کاربری.",
            "پژوهش پیام زیست‌محیطی.",
            "مطالعهٔ آموزش و تمرین.",
        ],
        example_text="آگهی‌ای که در هفتهٔ نخست چند بار پخش می‌شود نگرش مثبت می‌سازد، اما پخش بی‌وقفهٔ آن در ماه دوم مخاطب را خسته و بدبین می‌کند؛ همین منحنی وارونه، مسئلهٔ بسامد بهینه در تبلیغات است.",
        evolution="زایونس در ۱۹۶۸ فرضیهٔ بسامد-احساس را با مواجههٔ صرف صورت‌بندی کرد؛ کاکیوپو و پتی در ۱۹۷۹ تکرار پیام اقناعی را به پاسخ شناختی پیوند دادند و پژوهش‌های بعدی منحنی وارونه و خستگی تبلیغاتی را در رسانه‌های چندکاناله آزمودند.",
        key_concepts=["مواجههٔ صرف", "فرضیهٔ بسامد-احساس", "منحنی وارونه", "خستگی تبلیغاتی", "پاسخ شناختی", "روانی پردازش"],
        theorists="رابرت زایونس، جان کاکیوپو و ریچارد پتی.",
        theorists_text="زایونس در سنت روان‌شناسی اجتماعی اثر مواجهه را کشف کرد و کاکیوپو و پتی آن را به نظریهٔ اقناع پیوند دادند.",
        model="مدل وارونهٔ تکرار: اقناع با تکرار متوسط به بیشینه می‌رسد و با تکرار بیش از حد به سبب خستگی و پاسخ منفی کاهش می‌یابد.",
        studies=[
            "مقالهٔ زایونس در ۱۹۶۸.",
            "آزمایش کاکیوپو و پتی در ۱۹۷۹.",
            "پژوهش مواجههٔ صرف.",
            "مطالعهٔ بسامد تبلیغات.",
            "تحلیل کمپین انتخاباتی.",
            "پژوهش خستگی تبلیغاتی.",
            "مطالعهٔ شعار برند.",
            "تحلیل پیام سلامت.",
            "پژوهش یادآوری پیام.",
            "مطالعهٔ موسیقی تبلیغاتی.",
            "تحلیل رسانهٔ چندکاناله.",
            "پژوهش آستانهٔ بهینه.",
            "مطالعهٔ بسامد بهینه در تبلیغات دیجیتال و رسانهٔ اجتماعی.",
            "پژوهش تکرار پیام در آموزش و یادگیری بلندمدت.",
        ],
    ),
    "MC-580": dict(
        year=1920,
        mapping=WORK_MAPPING,
        summary="اثر هاله سوگیری قضاوت است که در آن یک ویژگی برجسته یا برداشت کلی از یک شخص یا شیء، ارزیابی ویژگی‌های دیگر را جهت می‌دهد. تورندایک در سال ۱۹۲۰ با بررسی ارزشیابی افسران نشان داد نمره‌های ویژگی‌های گوناگون یک فرد بیش از حد با هم همبسته‌اند و یک برداشت کلی، ارزیابی‌های جزئی را آلوده می‌کند؛ او این را خطای ثابت نامید. نیسبت و ویلسون در ۱۹۷۷ نشان دادند اثر هاله ناخودآگاه عمل می‌کند: تغییر گرمی رفتار یک معلم، ارزیابی دانشجویان از ظاهر و لهجهٔ او را نیز تغییر داد، بی‌آنکه دانشجویان علت را بدانند. اثر هاله در ارزشیابی کارکنان، تبلیغات برند، تصویر نامزد سیاسی و اعتبار منبع کاربرد دارد. نقدها بر تفکیک خطا از همبستگی واقعی ویژگی‌ها و وابستگی آن به زمینه و آموزش داور تأکید دارند.",
        definition="اثر هاله جهت‌گیری ارزیابی ویژگی‌های یک شخص یا شیء در نتیجهٔ یک برداشت کلی یا ویژگی برجسته است.",
        main_problem="چرا یک برداشت کلی یا ویژگی برجسته، ارزیابی ویژگی‌های نامرتبط را آلوده می‌کند و این سوگیری چگونه بدون آگاهی رخ می‌دهد.",
        mechanism="برداشت کلی به‌عنوان چارچوب تفسیر عمل می‌کند؛ اطلاعات مبهم به سمت برداشت اولیه خوانده می‌شود و حافظه و قضاوت ویژگی‌های جزئی با آن هم‌راستا می‌شوند، بدون آنکه فرد از این جهت‌گیری آگاه باشد.",
        assumptions=[
            "برداشت کلی ارزیابی جزئی را جهت می‌دهد.",
            "ویژگی برجسته بر ویژگی‌های دیگر سرریز می‌کند.",
            "اثر بدون آگاهی فرد رخ می‌دهد.",
            "همبستگی نمره‌های ویژگی‌ها بیش از واقع است.",
            "جذابیت و گرمی بر شایستگی اثر می‌گذارند.",
            "اثر در ارزشیابی رسمی هم دیده می‌شود.",
            "آموزش داور اثر را کاهش می‌دهد.",
            "زمینه و ترتیب اطلاعات اثر را تعدیل می‌کند.",
        ],
        principles=[
            "ویژگی‌ها را جداگانه بسنج.",
            "داوران را نسبت به برداشت کلی آگاه کن.",
            "همبستگی واقعی و خطا را تفکیک کن.",
            "ترتیب ارائه اطلاعات را کنترل کن.",
            "از یک ویژگی به ویژگی دیگر تعمیم نده.",
            "ارزیابی چندمنبعی را به کار ببر.",
            "نقش جذابیت و گرمی را کنترل کن.",
        ],
        critiques=[
            "تفکیک خطا از همبستگی واقعی دشوار است.",
            "اندازهٔ اثر به زمینه وابسته است.",
            "به تفاوت فرهنگی کم توجه است.",
            "به آموزش داور کم می‌پردازد.",
            "سنجش برداشت کلی دشوار است.",
            "به نقش رسانه کم توجه شده است.",
            "اثر در ارزیابی تخصصی تضعیف می‌شود.",
            "به سوگیری جنسیتی کم می‌پردازد.",
            "بیشتر شواهد آزمایشگاهی است.",
            "مرز آن با کلیشه روشن نیست.",
        ],
        critique_text="منتقدان می‌گویند اثر هاله همیشه خطا نیست و بخشی از همبستگی ارزیابی‌ها می‌تواند واقعی باشد؛ همچنین اندازهٔ آن به زمینه و آموزش داور وابسته است. با این حال تورندایک و نیسبت و ویلسون نشان دادند برداشت کلی می‌تواند ارزیابی جزئی را ناخودآگاه جهت دهد.",
        applications=[
            "تحلیل ارزشیابی کارکنان.",
            "پژوهش استخدام.",
            "مطالعهٔ تبلیغات برند.",
            "تحلیل تصویر نامزد سیاسی.",
            "پژوهش اعتبار منبع.",
            "مطالعهٔ ارزشیابی معلم.",
            "تحلیل نقد محصول.",
            "پژوهش تأییدکنندهٔ مشهور.",
            "مطالعهٔ شهادت شاهد.",
            "تحلیل تصمیم پزشکی.",
            "پژوهش طراحی رابط کاربری.",
            "مطالعهٔ بررسی عملکرد.",
        ],
        example_text="مصرف‌کننده‌ای که از طراحی زیبای یک گوشی خوشش می‌آید، کیفیت دوربین و دوام آن را نیز بالاتر می‌ارزیابی می‌کند؛ برداشت کلی از ظاهر، ارزیابی ویژگی‌های نامرتبط را جهت داده است.",
        evolution="تورندایک در ۱۹۲۰ خطای ثابت را در ارزشیابی‌های روان‌شناختی نشان داد؛ نیسبت و ویلسون در ۱۹۷۷ ماهیت ناخودآگاه آن را آزمودند و پژوهش‌های بعدی اثر را به برند، سیاست و ارزیابی سازمانی گستراندند.",
        key_concepts=["برداشت کلی", "خطای ثابت", "کلیشهٔ جذابیت", "هالهٔ برند", "سوگیری داور", "قضاوت ناخودآگاه"],
        theorists="ادوارد تورندایک، ریچارد نیسبت و تیموتی ویلسون.",
        theorists_text="تورندایک در سنت روان‌شناسی کاربردی اثر را کشف کرد و نیسبت و ویلسون سازوکار ناخودآگاه آن را روشن کردند.",
        model="مدل برداشت کلی: یک ویژگی برجسته چارچوب تفسیر می‌سازد و ارزیابی ویژگی‌های جزئی را هم‌راستا می‌کند.",
        studies=[
            "مقالهٔ تورندایک در ۱۹۲۰.",
            "آزمایش نیسبت و ویلسون در ۱۹۷۷.",
            "پژوهش جذابیت و شایستگی.",
            "مطالعهٔ ارزشیابی کارکنان.",
            "تحلیل هالهٔ برند.",
            "پژوهش تصویر سیاسی.",
            "مطالعهٔ ارزشیابی معلم.",
            "تحلیل اعتبار منبع.",
            "پژوهش نقد محصول.",
            "مطالعهٔ شهادت شاهد.",
            "تحلیل تصمیم پزشکی.",
            "پژوهش آموزش داور.",
            "مطالعهٔ اثر هاله در ارزیابی عملکرد کارکنان سازمان.",
            "پژوهش اثر هاله در انتخاب محصول و نقد آنلاین.",
            "تحلیل اثر هاله در برآورد اعتبار رسانه و منبع خبر.",
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
                                       "verified": n_verified, "batch": 177}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH177 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
