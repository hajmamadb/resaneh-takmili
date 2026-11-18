# -*- coding: utf-8 -*-
"""Batch 150 (MODEL): MC-567 conditioning, MC-569 EORM, MC-577 EPPM, MC-583 two-way symmetrical."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch150-model-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch150_model.json"

S = {
    "MC-567": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Attitudes Established by Classical Conditioning",
             title_fa="نگرش‌هایی که با شرطی‌سازی کلاسیک ساخته می‌شوند",
             authors="Staats, A. W.; Staats, C. K.", year=1958,
             publisher="The Journal of Abnormal and Social Psychology",
             doi=None,
             url="https://psycnet.apa.org/record/1959-07843-001",
             language="en", isbn=None,
             citation="Staats, A. W., & Staats, C. K. (1958). Attitudes established by classical conditioning. The Journal of Abnormal and Social Psychology, 57(1), 37-40.",
             locator="57(1):37-40", locator_type="page_range",
             supports="attitudes can be acquired by pairing a stimulus with valenced words", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Associative Learning of Likes and Dislikes: A Review of 25 Years of Research on Human Evaluative Conditioning",
             title_fa="یادگیری پیوندی پسندها و ناپسندها: مروری بر بیست‌وپنج سال پژوهش شرطی‌سازی ارزشیابی",
             authors="De Houwer, J.; Thomas, S.; Baeyens, F.", year=2001,
             publisher="Psychological Bulletin",
             doi=None,
             url="https://pubmed.ncbi.nlm.nih.gov/11726074/",
             language="en", isbn=None,
             citation="De Houwer, J., Thomas, S., & Baeyens, F. (2001). Associative learning of likes and dislikes: A review of 25 years of research on human evaluative conditioning. Psychological Bulletin, 127(6), 853-869.",
             locator="127(6):853-869", locator_type="page_range",
             supports="evaluative conditioning as a mechanism of attitude change through stimulus pairing", verified=True),
    ],
    "MC-569": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Toward a Theory of Entertainment Persuasion: Explaining the Persuasive Effects of Entertainment-Education Messages",
             title_fa="به‌سوی نظریه‌ای برای اقناع سرگرمی‌محور",
             authors="Moyer-Gusé, E.", year=2008,
             publisher="Communication Theory",
             doi=None,
             url="http://www.communicationcache.com/uploads/1/0/8/8/10887248/toward_a_theory_of_entertainment_persuasion-_explaining_the_persuasive_effects_of_entertainment-education_messages.pdf",
             language="en", isbn=None,
             citation="Moyer-Gusé, E. (2008). Toward a theory of entertainment persuasion: Explaining the persuasive effects of entertainment-education messages. Communication Theory, 18(3), 407-425.",
             locator="18(3):407-425", locator_type="page_range",
             supports="overcoming resistance through narrative involvement, identification and reduction of reactance", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Explaining the Effects of Narrative in an Entertainment Television Program: Overcoming Resistance to Persuasion",
             title_fa="تبیین اثر روایت در یک برنامهٔ سرگرمی تلویزیونی: غلبه بر مقاومت در برابر اقناع",
             authors="Moyer-Gusé, E.; Nabi, R. L.", year=2010,
             publisher="Human Communication Research",
             doi="10.1111/j.1468-2958.2009.01367.x",
             url="https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1468-2958.2009.01367.x",
             language="en", isbn=None,
             citation="Moyer-Gusé, E., & Nabi, R. L. (2010). Explaining the effects of narrative in an entertainment television program: Overcoming resistance to persuasion. Human Communication Research, 36(1), 26-52.",
             locator="36(1):26-52", locator_type="page_range",
             supports="empirical test of the entertainment overcoming resistance model", verified=True),
    ],
    "MC-577": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Effects of Fear-Arousing Communications",
             title_fa="اثرهای ارتباطات ترس‌برانگیز",
             authors="Janis, I. L.; Feshbach, S.", year=1953,
             publisher="The Journal of Abnormal and Social Psychology",
             doi="10.1037/h0060732",
             url="https://pubmed.ncbi.nlm.nih.gov/13022199/",
             language="en", isbn=None,
             citation="Janis, I. L., & Feshbach, S. (1953). Effects of fear-arousing communications. The Journal of Abnormal and Social Psychology, 48(1), 78-92.",
             locator="48(1):78-92", locator_type="page_range",
             supports="fear appeals can increase attention while excessive fear reduces compliance", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Putting the Fear Back into Fear Appeals: The Extended Parallel Process Model",
             title_fa="بازگرداندن ترس به پیام‌های ترس‌محور: مدل فرایند موازی گسترده",
             authors="Witte, K.", year=1992,
             publisher="Communication Monographs",
             doi="10.1080/03637759209376276",
             url="https://www.tandfonline.com/doi/abs/10.1080/03637759209376276",
             language="en", isbn=None,
             citation="Witte, K. (1992). Putting the fear back into fear appeals: The extended parallel process model. Communication Monographs, 59(4), 329-349.",
             locator="59(4):329-349", locator_type="page_range",
             supports="danger-control versus fear-control processes in fear appeal effects", verified=True),
    ],
    "MC-583": [
        dict(kind="BOOK",
             title_en="Managing Public Relations",
             title_fa="مدیریت روابط عمومی",
             authors="Grunig, J. E.; Hunt, T.", year=1984,
             publisher="Holt, Rinehart and Winston",
             doi=None,
             url="https://archive.org/details/managingpublicre0000unse",
             language="en", isbn=None,
             citation="Grunig, J. E., & Hunt, T. (1984). Managing Public Relations. New York: Holt, Rinehart and Winston.",
             locator="1984 edition", locator_type="edition",
             supports="the four models of public relations, including two-way symmetrical", verified=True),
        dict(kind="BOOK_CHAPTER",
             title_en="Two-Way Symmetrical Public Relations: Past, Present, and Future",
             title_fa="روابط عمومی دوسویهٔ متقارن: گذشته، حال و آینده",
             authors="Grunig, J. E.", year=2001,
             publisher="SAGE (Handbook of Public Relations)",
             doi=None,
             url="https://sk.sagepub.com/hnbk/edvol/handbook-of-public-relations/chpt/twoway-symmetrical-public-relations-past-present",
             language="en", isbn=None,
             citation="Grunig, J. E. (2001). Two-way symmetrical public relations: Past, present, and future. In R. L. Heath (Ed.), Handbook of Public Relations (pp. 11-32). Thousand Oaks: SAGE.",
             locator="chapter", locator_type="SECTION",
             supports="dialogic, research-based symmetry aiming at mutual change", verified=True),
    ],
}

ENRICH = {
    "MC-567": dict(
        year=1958,
        summary="مدل شرطی‌سازی رسانه‌ای، اثر رسانه را با سازوکار یادگیری پیوندی توضیح می‌دهد: وقتی نشانه‌های رسانه‌ای مکرر با محرک‌های خوشایند یا ناخوشایند همراه می‌شوند، واکنش هیجانی و ارزش‌گذاری مخاطب به همان نشانه‌ها منتقل می‌شود. ریشهٔ این مدل در پژوهش استیتس و استیتس در سال ۱۹۵۸ است که نشان دادند نگرش نسبت به یک محرک بی‌طرف را می‌توان با جفت‌سازی مکرر آن با واژه‌های مثبت یا منفی، به‌گونه‌ای نظام‌مند شکل داد و تغییر داد. پژوهش شرطی‌سازی ارزشیابی در دهه‌های بعد نشان داد که این تغییر پسند و ناپسند پایدار است، حتی وقتی فرد پیوند را آگاهانه به یاد نمی‌آورد. در رسانه، این سازوکار توضیح می‌دهد چرا موسیقی، چهرهٔ محبوب، نورپردازی و بافت روایت می‌توانند نگرش مخاطب به محصول، شخصیت یا ایده را بی‌آنکه استدلالی ارائه شود دگرگون کنند. تبلیغات، پویانمایی، خبر و حتی موسیقی متن از همین منطق بهره می‌گیرند. مدل، مخاطب را نه تحلیلگرِ پیام، بلکه موجودی یادگیرنده می‌بیند که پیوندهای مکرر محیط رسانه‌ای، نظام ارزشیابی او را شکل می‌دهند. نقدهای اصلی به مدل، تقلیل پیام رسانه‌ای به جفت محرک، کم‌توجهی به معنا و تفسیر، تمرکز بر موقعیت آزمایشگاهی و دشواری تعمیم به میدان رسانه‌ای را برجسته می‌کنند.",
        definition="مدل شرطی‌سازی رسانه‌ای، اثر رسانه را بر پایهٔ یادگیری پیوندی توضیح می‌دهد: جفت‌شدن مکرر نشانهٔ رسانه‌ای با محرک ارزش‌دار، ارزش آن محرک را به نشانه منتقل می‌کند.",
        main_problem="چگونه می‌توان تغییر نگرش و هیجان مخاطب را بدون استدلال صریح، صرفاً از راه همراه‌شدن مکرر نشانه‌های رسانه‌ای با محرک‌های ارزش‌دار توضیح داد.",
        mechanism="نشانهٔ رسانه‌ای به‌عنوان محرک شرطی با محرک بی‌شرط خوشایند یا ناخوشایند جفت می‌شود؛ پس از چند مواجهه، نشانه به‌تنهایی پاسخ ارزشیابی مشابه را برمی‌انگیزد و نگرش مخاطب را می‌سازد.",
        assumptions=[
            "نگرش را می‌توان با یادگیری پیوندی ساخت.",
            "جفت‌شدن مکرر، ارزش را منتقل می‌کند.",
            "این انتقال می‌تواند ناآگاهانه رخ دهد.",
            "نشانه‌های رسانه‌ای نقش محرک شرطی دارند.",
            "پاسخ ارزشیابی، رفتاری و قابل سنجش است.",
        ],
        principles=[
            "جفت‌شدن محرک را در زمان بسنج.",
            "نشانه و محرک ارزش‌دار را جدا مشخص کن.",
            "آگاهی مخاطب را کنترل کن.",
            "پایداری تغییر را در پیگیری بسنج.",
            "معنا را از سازوکار یادگیری جدا نکن.",
            "تعمیم آزمایشگاهی را با احتیاط گزارش کن.",
        ],
        critiques=[
            "پیام رسانه‌ای را به جفت محرک تقلیل می‌دهد.",
            "معنا و تفسیر مخاطب را کم‌بررسی می‌گذارد.",
            "بیشتر شواهد آزمایشگاهی است.",
            "تعمیم به میدان رسانه‌ای دشوار است.",
            "نقش استدلال و آگاهی را نادیده می‌گیرد.",
            "اثر بلندمدت آن به‌ندرت سنجیده شده است.",
            "تفاوت فردی در حساسیت به شرطی‌سازی را نادیده می‌گیرد.",
            "مرز آن با یادگیری اجتماعی روشن نیست.",
        ],
        critique_text="منتقدان می‌گویند مدل شرطی‌سازی رسانه‌ای سازوکار مهمی را روشن کرد اما پیام را به جفت محرک فروکاست و نقش معنا، گفتمان و انتخاب فعال مخاطب را کم‌بررسی گذاشت؛ با این حال، پژوهش شرطی‌سازی ارزشیابی نشان می‌دهد این سازوکار پایهٔ بسیاری از اثرهای تبلیغاتی و احساسی رسانه است.",
        applications=[
            "طراحی پیام تبلیغاتی.",
            "تحلیل موسیقی متن و هیجان.",
            "آموزش سواد رسانه‌ای.",
            "پژوهش نگرش مصرف‌کننده.",
            "تحلیل کمپین سلامت.",
            "طراحی بازی تبلیغاتی.",
            "تحلیل بسته‌بندی و رنگ.",
            "پژوهش عادت مصرف برند.",
        ],
        example_text="آهنگی محبوب، پیش از نمایش تصویر یک برند پخش می‌شود؛ پس از چند مواجهه، دیدن همان برند به‌تنهایی احساس خوشایندی برمی‌انگیزد، حتی اگر مخاطب پیوند را به یاد نیاورد. همین منطق در جفت‌شدن چهرهٔ خبرنگار با تصویر بحران نیز عمل می‌کند.",
        evolution="پژوهش سال ۱۹۵۸ استیتس و استیتس پایهٔ شرطی‌سازی نگرش را گذاشت. مرور سال ۲۰۰۱ شرطی‌سازی ارزشیابی را به بدنهٔ شناخته‌شدهٔ روان‌شناسی اجتماعی تبدیل کرد و پژوهش تبلیغات، سازوکار آن را به رسانه آورد.",
        key_concepts=["شرطی‌سازی کلاسیک", "شرطی‌سازی ارزشیابی", "انتقال ارزش", "نشانهٔ رسانه‌ای", "نگرش ناآگاهانه", "پیوند محرک"],
        theorists="آلبرت استیتس و کارولین استیتس.",
        theorists_text="مدل در سنت روان‌شناسی یادگیری و پژوهش تغییر نگرش شکل گرفت.",
        model="نشانهٔ رسانه‌ای به‌عنوان محرک شرطی که با جفت‌شدن مکرر، ارزش هیجانی محرک دیگر را جذب می‌کند و نگرش مخاطب را می‌سازد.",
        studies=[
            "پژوهش سال ۱۹۵۸ ساخت نگرش با شرطی‌سازی را نشان داد.",
            "مرور سال ۲۰۰۱ پایداری شرطی‌سازی ارزشیابی را تأیید کرد.",
            "مطالعات تبلیغات، انتقال ارزش برند را سنجیدند.",
            "پژوهش اخیر ماندگاری این اثر را در پیگیری بررسی کرد.",
        ],
    ),
    "MC-569": dict(
        year=2008,
        summary="مدل غلبه بر مقاومت سرگرمی، که امیلی مویر-گوزه در سال ۲۰۰۸ صورت‌بندی کرد، توضیح می‌دهد چگونه پیام‌های سرگرمی‌محور می‌توانند مقاومت مخاطب در برابر اقناع را کاهش دهند و نگرش او را دگرگون کنند. مخاطب معمولاً در برابر پیام اقناعی مستقیم مقاومت می‌کند، زیرا هدف اقناع را می‌بیند و آزادی خود را تهدیدشده می‌یابد. سرگرمی این مقاومت را از چند راه می‌شکند: روایت مخاطب را در داستان غرق می‌کند و توجه به قصد اقناعی را کم می‌کند؛ همانندسازی با شخصیت‌ها، نگرش آنان را به‌صورت غیرمستقیم منتقل می‌سازد؛ و ارتباط شبه‌اجتماعی با شخصیت، مخاطب را به‌جای رد پیام، به پذیرش آن سوق می‌دهد. مدل همچنین نقش درگیری روایی، واکنش عاطفی و کاهش مقاومت شناختی را در زنجیرهٔ اثر جای می‌دهد و پیش‌بینی می‌کند که هرچه این سازوکارها قوی‌تر باشند، تغییر نگرش و رفتار محتمل‌تر است. آموزش سرگرمی، سریال‌های سلامت، نمایش‌های اجتماعی و کمپین‌های روایی از کاربردهای اصلی این مدل‌اند. آزمون تجربی سال ۲۰۱۰ مویر-گوزه و نبی این زنجیره را در یک برنامهٔ تلویزیونی سنجید. نقدهای اصلی به مدل، دشواری تفکیک سازوکارها، کم‌توجهی به شرایط فرهنگی، اثر محدود در موضوع‌های حساس و ابهام سنجش مقاومت را برجسته می‌کنند.",
        definition="مدل غلبه بر مقاومت سرگرمی توضیح می‌دهد که روایت سرگرمی با درگیری، همانندسازی و ارتباط شبه‌اجتماعی، مقاومت مخاطب در برابر اقناع را کاهش می‌دهد و پذیرش پیام را محتمل‌تر می‌کند.",
        main_problem="چرا پیام‌های اقناعی مستقیم با مقاومت روبه‌رو می‌شوند اما پیام‌های سرگرمی‌محور می‌توانند نگرش و رفتار مخاطب را با مقاومت کمتری دگرگون کنند.",
        mechanism="روایت مخاطب را درگیر می‌کند و توجه به قصد اقناعی را کم می‌کند؛ همانندسازی با شخصیت و ارتباط شبه‌اجتماعی، نگرش را غیرمستقیم منتقل می‌سازد و مقاومت شناختی و واکنشی را کاهش می‌دهد.",
        assumptions=[
            "مخاطب در برابر اقناع مستقیم مقاومت می‌کند.",
            "روایت توجه به قصد اقناعی را کم می‌کند.",
            "همانندسازی با شخصیت نگرش را منتقل می‌کند.",
            "ارتباط شبه‌اجتماعی پذیرش را افزایش می‌دهد.",
            "کاهش مقاومت، تغییر نگرش را محتمل‌تر می‌کند.",
        ],
        principles=[
            "قصد اقناعی را از سطح روایت پنهان نگه دار.",
            "همانندسازی شخصیت را تقویت کن.",
            "درگیری روایی را بسنج.",
            "مقاومت را پیش و پس از پیام اندازه بگیر.",
            "ارتباط شبه‌اجتماعی را در مدل بگنجان.",
            "شرایط فرهنگی را در تفسیر لحاظ کن.",
            "پذیرش پیام را با رفتار بسنج.",
        ],
        critiques=[
            "تفکیک سازوکارها دشوار است.",
            "شرایط فرهنگی را کم‌بررسی می‌گذارد.",
            "در موضوع‌های حساس اثر محدود است.",
            "سنجش مقاومت مبهم است.",
            "اثر بلندمدت آن کم‌سنجیده مانده است.",
            "مرز سرگرمی و تبلیغ پنهان را روشن نمی‌کند.",
            "نقش پیش‌دانش مخاطب را کم‌بررسی می‌گذارد.",
            "اندازهٔ اثر در نمونه‌های کوچک ناپایدار است.",
        ],
        critique_text="منتقدان می‌گویند مدل غلبه بر مقاومت سرگرمی چارچوبی روشن برای فهم اقناع روایی فراهم کرد اما تفکیک سازوکارها و سنجش مقاومت را دشوار گذاشت و شرایط فرهنگی را کم‌بررسی کرد؛ با این حال، پژوهش آموزش سرگرمی را از توصیف توصیه‌ای به آزمون سازوکار ارتقا داد.",
        applications=[
            "طراحی سریال سلامت.",
            "کمپین آموزش سرگرمی.",
            "تحلیل تبلیغ روایی.",
            "پژوهش ارتباط شبه‌اجتماعی.",
            "طراحی محتوای اجتماعی.",
            "ارزیابی کمپین واکسیناسیون.",
            "طراحی پادکست روایی سلامت.",
        ],
        example_text="سریالی که زندگی یک خانواده را در مواجهه با بیماری نشان می‌دهد، بی‌آنکه پیام مستقیم بدهد، مخاطب را با شخصیت همراه می‌کند؛ مخاطب نگرش شخصیت را می‌پذیرد و مقاومت کمتری در برابر توصیهٔ سلامت نشان می‌دهد.",
        evolution="مقالهٔ سال ۲۰۰۸ مویر-گوزه مدل غلبه بر مقاومت سرگرمی را معرفی کرد و پژوهش آموزش سرگرمی را به چارچوبی سازوکارمحور تبدیل کرد. آزمون سال ۲۰۱۰ و پژوهش‌های بعدی، زنجیرهٔ درگیری، همانندسازی و کاهش مقاومت را بررسی کردند.",
        key_concepts=["درگیری روایی", "همانندسازی", "ارتباط شبه‌اجتماعی", "مقاومت در برابر اقناع", "آموزش سرگرمی", "واکنش روانی"],
        theorists="امیلی مویر-گوزه.",
        theorists_text="مدل در سنت پژوهش اقناع روایی و آموزش سرگرمی شکل گرفت.",
        model="روایت سرگرمی با درگیری، همانندسازی و ارتباط شبه‌اجتماعی، مقاومت را کاهش می‌دهد و پذیرش نگرشی و رفتاری را افزایش می‌دهد.",
        studies=[
            "مقالهٔ سال ۲۰۰۸ مدل را صورت‌بندی کرد.",
            "آزمون سال ۲۰۱۰ زنجیرهٔ اثر را در تلویزیون سنجید.",
            "مطالعات سلامت، کاربرد آن را در واکسیناسیون بررسی کردند.",
            "پژوهش اخیر سازوکار ارتباط شبه‌اجتماعی را آزمود.",
        ],
    ),
    "MC-577": dict(
        year=1992,
        summary="مدل فرایند موازی گسترده، که کیم ویت در سال ۱۹۹۲ برای تبیین پیام‌های ترس‌محور ارائه کرد، توضیح می‌دهد چه زمانی ترس، مخاطب را به محافظت از خود می‌کشاند و چه زمانی او را به کنترل ترس وامی‌دارد. ریشهٔ بحث به پژوهش یانیس و فشباخ در سال ۱۹۵۳ برمی‌گردد که نشان دادند ترس شدید همیشه به پذیرش بیشتر نمی‌انجامد و می‌تواند با کاهش توجه و برانگیختن واکنش دفاعی، اثر پیام را کم کند. ویت این تناقض را با تفکیک دو فرایند حل کرد: اگر مخاطب احساس کند تهدید جدی است و راه مقابلهٔ مؤثری در دست دارد، در مسیر کنترل خطر قرار می‌گیرد و نگرش و رفتار محافظتی را می‌پذیرد؛ اما اگر کارآمدی توصیه‌شده را باور نکند، در مسیر کنترل ترس می‌ماند و با انکار، اجتناب یا خوارشمردن پیام واکنش نشان می‌دهد. بنابراین، شدت ترس به‌تنهایی تعیین‌کننده نیست؛ ترکیب تهدید ادراک‌شده و کارآمدی ادراک‌شده سرنوشت پیام را روشن می‌کند. مدل در کمپین‌های سلامت، هشدارهای امنیتی، تبلیغات ترس‌محور و ارتباطات بحران به‌کار می‌رود. نقدهای اصلی به آن، دشواری سنجش هم‌زمان تهدید و کارآمدی، تفاوت‌های فرهنگی در پاسخ به ترس، خطر برانگیختن اضطراب ناسازگار و کم‌توجهی به بافت اجتماعی را برجسته می‌کنند.",
        definition="مدل فرایند موازی گسترده می‌گوید پیام ترس‌محور زمانی به رفتار محافظتی می‌انجامد که مخاطب هم تهدید را جدی بداند و هم راه مقابله را کارآمد ببیند؛ در غیر این صورت به کنترل ترس روی می‌آورد.",
        main_problem="چرا پیام‌های ترس‌محور گاه رفتار محافظتی می‌سازند و گاه به انکار و اجتناب می‌انجامند، و چه ترکیبی از تهدید و کارآمدی این تفاوت را توضیح می‌دهد.",
        mechanism="ادراک تهدید، ترس را برمی‌انگیزد؛ اگر کارآمدی توصیه بالا باشد، فرد در مسیر کنترل خطر رفتار محافظتی را می‌پذیرد، و اگر کارآمدی پایین باشد، در مسیر کنترل ترس با اجتناب و انکار واکنش نشان می‌دهد.",
        assumptions=[
            "ترس محرک اصلی پردازش پیام است.",
            "تهدید ادراک‌شده و کارآمدی ادراک‌شده تعیین‌کننده‌اند.",
            "دو مسیر کنترل خطر و کنترل ترس موازی‌اند.",
            "کارآمدی پایین به اجتناب می‌انجامد.",
            "شدت ترس به‌تنهایی کافی نیست.",
        ],
        principles=[
            "تهدید را با شواهد باورپذیر بساز.",
            "راه مقابله را مشخص و در دسترس نشان بده.",
            "کارآمدی ادراک‌شده را بسنج.",
            "از ترس بی‌راه حل پرهیز کن.",
            "پاسخ هیجانی را در پیگیری بسنج.",
            "بافت فرهنگی را در تفسیر بگنجان.",
        ],
        critiques=[
            "سنجش هم‌زمان تهدید و کارآمدی دشوار است.",
            "پاسخ به ترس در فرهنگ‌ها متفاوت است.",
            "خطر اضطراب ناسازگار را کم‌می‌شمارد.",
            "بافت اجتماعی را کم‌بررسی می‌گذارد.",
            "اثر بلندمدت آن کم‌سنجیده مانده است.",
            "مرز ترس و تهدید در سنجش روشن نیست.",
            "پیام ترس‌محور را به همهٔ مخاطبان تعمیم می‌دهد.",
            "سودمندی توصیه را بیش از حد یکدست فرض می‌کند.",
        ],
        critique_text="منتقدان می‌گویند مدل فرایند موازی گسترده تناقض پژوهش‌های پیشین دربارهٔ ترس را به‌خوبی حل کرد اما سنجش هم‌زمان تهدید و کارآمدی را دشوار گذاشت و بافت اجتماعی را کم‌بررسی کرد؛ با این حال، چارچوب اصلی طراحی کمپین‌های سلامت و هشدارهای عمومی است.",
        applications=[
            "طراحی کمپین سلامت.",
            "هشدار عمومی امنیت.",
            "ارتباطات بحران.",
            "آموزش پیشگیری.",
            "تبلیغات ترس‌محور.",
            "ارزیابی پیام واکسیناسیون.",
        ],
        example_text="کمپینی دربارهٔ خطر مصرف دخانیات، هم آسیب را با تصویر و شواهد جدی نشان می‌دهد و هم راه ترک را در دسترس و کارآمد معرفی می‌کند؛ اگر فقط ترس نشان دهد و راه حل نداشته باشد، مخاطب پیام را انکار می‌کند.",
        evolution="پژوهش سال ۱۹۵۳ یانیس و فشباخ تناقض ترس را نشان داد. مدل سال ۱۹۹۲ ویت دو مسیر کنترل خطر و کنترل ترس را تفکیک کرد و به چارچوب مسلط پژوهش پیام‌های ترس‌محور تبدیل شد.",
        key_concepts=["ترس", "تهدید ادراک‌شده", "کارآمدی ادراک‌شده", "کنترل خطر", "کنترل ترس", "پیام ترس‌محور"],
        theorists="کیم ویت، با تکیه بر پژوهش یانیس و فشباخ.",
        theorists_text="مدل در سنت پژوهش اقناع، پیام‌های ترس‌محور و ارتباطات سلامت شکل گرفت.",
        model="دو مسیر موازی کنترل خطر و کنترل ترس که با ترکیب تهدید ادراک‌شده و کارآمدی ادراک‌شده تعیین می‌شوند.",
        studies=[
            "پژوهش سال ۱۹۵۳ اثر ترس شدید را بررسی کرد.",
            "مدل سال ۱۹۹۲ دو مسیر را صورت‌بندی کرد.",
            "مطالعات سلامت، کارآمدی را در کمپین‌ها سنجیدند.",
            "پژوهش اخیر، پاسخ فرهنگی به ترس را بررسی کرد.",
        ],
    ),
    "MC-583": dict(
        year=1984,
        summary="مدل دوسویهٔ متقارن، که جیمز گرونیگ و تاد هانت در کتاب مدیریت روابط عمومی سال ۱۹۸۴ در کنار سه مدل دیگر صورت‌بندی کردند، ارتباط سازمان با مخاطبان را گفت‌وگویی دوسویه می‌داند که هدفش تغییر متقابل است، نه اقناع یک‌سویه. در این کتاب چهار مدل معرفی شد: عامل مطبوعاتی، اطلاع‌رسانی عمومی، دوسویهٔ نامتقارن و دوسویهٔ متقارن. در مدل متقارن، سازمان با پژوهش و گفت‌وگو، هم مخاطب را می‌فهمد و هم خود را در برابر او تغییر می‌دهد؛ ارتباط ابزاری برای کنترل مخاطب نیست، بلکه فرایندی برای رسیدن به فهم مشترک و حل تعارض است. این مدل به نظریهٔ تعالی در روابط عمومی راه برد و به‌عنوان معیار هنجاری عملکرد حرفه‌ای پذیرفته شد. در عمل، سازمان‌ها اغلب ترکیبی از مدل‌ها را به کار می‌گیرند و در بحران به تقارن نزدیک‌تر می‌شوند. ارتباطات دیجیتال و شبکه‌های اجتماعی، میدان آزمون تازه‌ای برای این مدل فراهم کردند. نقدهای اصلی به آن، آرمانی‌بودن، دشواری سنجش تقارن، نامتوازن‌بودن واقعی قدرت میان سازمان و مخاطب، کم‌توجهی به منافع مالکان و خطر تبدیل گفت‌وگو به ابزار مدیریت شهرت را برجسته می‌کنند.",
        definition="مدل دوسویهٔ متقارن، روابط عمومی را گفت‌وگویی دوسویه و پژوهش‌محور می‌داند که در آن سازمان و مخاطب هر دو تغییر می‌کنند و هدف، فهم مشترک و حل تعارض است.",
        main_problem="آیا ارتباط سازمان با مخاطبان باید اقناع یک‌سویه باشد یا گفت‌وگویی که در آن سازمان نیز نگرش و رفتار خود را بر پایهٔ فهم مخاطب تغییر می‌دهد.",
        mechanism="سازمان با پژوهش، نگرانی مخاطب را می‌فهمد، در گفت‌وگو با او وارد می‌شود و بر پایهٔ بازخورد، هم پیام و هم رفتار خود را تنظیم می‌کند؛ نتیجه، تغییر متقابل و کاهش تعارض است.",
        assumptions=[
            "مخاطب شریک گفت‌وگوست، نه هدف کنترل.",
            "پژوهش پایهٔ تصمیم ارتباطی است.",
            "تغییر باید دوسویه باشد.",
            "فهم مشترک بر اقناع یک‌سویه مقدم است.",
            "تعارض را می‌توان با گفت‌وگو حل کرد.",
        ],
        principles=[
            "پیش از پیام، مخاطب را پژوهش کن.",
            "گفت‌وگو را واقعی و دوسویه کن.",
            "آمادهٔ تغییر سازمان باش.",
            "بازخورد را در تصمیم وارد کن.",
            "تعارض را فرصت فهم مشترک ببین.",
            "تقارن را با شاخص بسنج.",
            "منافع ذی‌نفعان را همه‌جانبه بشنو.",
        ],
        critiques=[
            "آرمانی و دشوارتحقق است.",
            "سنجش تقارن مبهم است.",
            "قدرت واقعی طرفین نامتوازن است.",
            "منافع مالکان را کم‌می‌شمارد.",
            "خطر تبدیل گفت‌وگو به مدیریت شهرت وجود دارد.",
            "تفاوت فرهنگی در تقارن کم‌بررسی مانده است.",
            "انگیزهٔ اقتصادی سازمان را در تقارن نادیده می‌گیرد.",
            "سنجش گفت‌وگوی واقعی را به رضایت مخاطب فرو می‌کاهد.",
        ],
        critique_text="منتقدان می‌گویند مدل دوسویهٔ متقارن معیاری ارزشمند برای حرفه‌ای‌شدن روابط عمومی داد اما آرمانی ماند و قدرت نامتوازن سازمان و مخاطب را کم‌بررسی کرد؛ با این حال، همچنان چارچوب مرجع سنجش اخلاقی و گفت‌وگومحور ارتباط سازمانی است.",
        applications=[
            "طراحی راهبرد روابط عمومی.",
            "مدیریت بحران سازمانی.",
            "ارتباطات سلامت عمومی.",
            "مسئولیت اجتماعی شرکت.",
            "گفت‌وگوی دولت و شهروند.",
            "مدیریت شهرت در بحران.",
            "ارزیابی ارتباطات دیجیتال.",
            "آموزش اخلاق حرفه‌ای ارتباط.",
            "طراحی فرایند شنیدن صدای مخاطب.",
        ],
        example_text="شرکتی که پس از اعتراض مصرف‌کنندگان، نه فقط پیام دفاعی منتشر می‌کند بلکه نشست گفت‌وگو برگزار می‌کند و خط تولید را تغییر می‌دهد، در مسیر مدل متقارن گام برداشته است؛ تغییر پیام بدون تغییر رفتار، همان مدل نامتقارن است.",
        evolution="کتاب سال ۱۹۸۴ چهار مدل روابط عمومی را معرفی کرد و مدل متقارن را به معیار هنجاری تبدیل کرد. پژوهش‌های بعدی، آن را در نظریهٔ تعالی و ارتباطات دیجیتال گستردند و نقدهای مربوط به قدرت و فرهنگ را افزودند.",
        key_concepts=["مدل دوسویهٔ متقارن", "چهار مدل روابط عمومی", "گفت‌وگو", "تغییر متقابل", "نظریهٔ تعالی", "تعارض"],
        theorists="جیمز گرونیگ و تاد هانت.",
        theorists_text="مدل در سنت پژوهش روابط عمومی و مدیریت ارتباط سازمانی شکل گرفت.",
        model="ارتباط سازمانی گفت‌وگومحور و پژوهش‌بنیان که در آن سازمان و مخاطب هر دو تغییر می‌کنند و فهم مشترک جای اقناع یک‌سویه را می‌گیرد.",
        studies=[
            "کتاب سال ۱۹۸۴ چهار مدل را معرفی کرد.",
            "پژوهش تعالی، تقارن را در سازمان‌ها سنجید.",
            "مطالعات بحران، کاربرد تقارن را بررسی کردند.",
            "پژوهش دیجیتال، گفت‌وگوی آنلاین را تحلیل کرد.",
            "مطالعهٔ سلامت، تقارن را در کمپین عمومی سنجید.",
        ],
    ),
}

NAME_FIX = {
    "MC-569": ("مدل غلبه بر مقاومت سرگرمی", "Entertainment Overcoming Resistance Model (EORM)", "عنوان و انتساب کارت با پژوهش واقعی هم‌خوان نبود؛ عنوان دقیق مدل و صورت‌بندی سال ۲۰۰۸ ثبت شد."),
    "MC-577": ("مدل فرایند موازی گسترده", "Extended Parallel Process Model (EPPM)", "عنوان کارت ترکیبی از «اثر ترس» و سرواژه بود؛ نام دقیق مدل و انتساب آن به سال ۱۹۹۲ ثبت شد."),
}
YEAR_FIX = {
    "MC-567": "سال و نظریه‌پرداز کارت خالی بود؛ سال ۱۹۵۸ به‌عنوان نقطهٔ شاهد بنیادی مدل شرطی‌سازی نگرش ثبت شد.",
    "MC-569": "سال ۲۰۰۳ و انتساب «مایرز و تاد» در کارت با صورت‌بندی سال ۲۰۰۸ مویر-گوزه هم‌خوان نبود؛ سال درست ثبت شد.",
    "MC-577": "سال ۱۹۶۷ در کارت با پیشینهٔ ۱۹۵۳ یانیس و فشباخ و مدل ۱۹۹۲ ویت هم‌خوان نبود؛ سال ۱۹۹۲ ثبت شد.",
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
                                       "verified": n_verified, "batch": 150}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH150 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
