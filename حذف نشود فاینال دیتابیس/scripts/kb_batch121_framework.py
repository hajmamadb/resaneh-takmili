# -*- coding: utf-8 -*-
"""Batch 121 (FRAMEWORK): full documentation for MC-432, MC-442, MC-461, MC-481."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch121-framework-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch121_framework.json"

S = {
    "MC-432": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Affect, Not Ideology: A Social Identity Perspective on Polarization",
             title_fa="عاطفه، نه ایدئولوژی: چشم‌اندازی هویتی بر قطب‌بندی",
             authors="Iyengar, S.; Sood, G.; Lelkes, Y.", year=2012,
             publisher="Public Opinion Quarterly",
             doi=None,
             url="https://academic.oup.com/poq/article/76/3/405/1894274",
             language="en", isbn=None,
             citation="Iyengar, S., Sood, G., & Lelkes, Y. (2012). Affect, not ideology: A social identity perspective on polarization. Public Opinion Quarterly, 76(3), 405-431.",
             locator="76(3):405-431", locator_type="page_range",
             supports="partisan affect and social distance, rather than issue positions, drive contemporary polarization", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Origins and Consequences of Affective Polarization in the United States",
             title_fa="خاستگاه‌ها و پیامدهای قطب‌بندی عاطفی در ایالات متحده",
             authors="Iyengar, S.; Lelkes, Y.; Levendusky, M.; Malhotra, N.; Westwood, S. J.", year=2019,
             publisher="Annual Review of Political Science",
             doi=None, url=None, language="en", isbn=None,
             citation="Iyengar, S., Lelkes, Y., Levendusky, M., Malhotra, N., & Westwood, S. J. (2019). The origins and consequences of affective polarization in the United States. Annual Review of Political Science, 22, 129-146.",
             locator="22:129-146", locator_type="page_range",
             supports="review of measures, causes and consequences of affective polarization", verified=False),
    ],
    "MC-442": [
        dict(kind="BOOK",
             title_en="Culture's Consequences: International Differences in Work-Related Values",
             title_fa="پیامدهای فرهنگ: تفاوت‌های بین‌المللی در ارزش‌های مرتبط با کار",
             authors="Hofstede, G.", year=1980,
             publisher="Sage",
             doi=None,
             url="https://books.google.com/books/about/Culture_s_Consequences.html?id=Cayp_Um4O9gC",
             language="en", isbn=None,
             citation="Hofstede, G. (1980). Culture's consequences: International differences in work-related values. Sage.",
             locator="chs. 1-6", locator_type="work",
             supports="four national culture dimensions derived from a multinational employee survey", verified=True),
        dict(kind="BOOK",
             title_en="Culture's Consequences: Comparing Values, Behaviors, Institutions, and Organizations Across Nations",
             title_fa="پیامدهای فرهنگ: مقایسه ارزش‌ها، رفتارها، نهادها و سازمان‌ها در میان ملت‌ها",
             authors="Hofstede, G.", year=2001,
             publisher="Sage",
             doi=None, url=None, language="en", isbn=None,
             citation="Hofstede, G. (2001). Culture's consequences: Comparing values, behaviors, institutions, and organizations across nations (2nd ed.). Sage.",
             locator="chs. 1-8", locator_type="work",
             supports="expanded five-dimension model and methodological revisions", verified=False),
    ],
    "MC-461": [
        dict(kind="BOOK",
             title_en="Orientalism",
             title_fa="شرق‌شناسی",
             authors="Said, E. W.", year=1978,
             publisher="Pantheon Books",
             doi=None,
             url="https://monoskop.org/images/4/4e/Said_Edward_Orientalism_1979.pdf",
             language="en", isbn=None,
             citation="Said, E. W. (1978). Orientalism. Pantheon Books.",
             locator="Introduction; ch. 1", locator_type="work",
             supports="Orientalism as a corporate discourse reproducing Western superiority over the Orient", verified=True),
        dict(kind="BOOK",
             title_en="Culture and Imperialism",
             title_fa="فرهنگ و امپریالیسم",
             authors="Said, E. W.", year=1993,
             publisher="Knopf",
             doi=None, url=None, language="en", isbn=None,
             citation="Said, E. W. (1993). Culture and imperialism. Knopf.",
             locator="Introduction", locator_type="work",
             supports="extension of the critique to cultural forms and narrative resistance", verified=False),
    ],
    "MC-481": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="On a New List of Categories",
             title_fa="دربارهٔ فهرستی تازه از مقولات",
             authors="Peirce, C. S.", year=1867,
             publisher="Proceedings of the American Academy of Arts and Sciences",
             doi=None, url=None, language="en", isbn=None,
             citation="Peirce, C. S. (1867). On a new list of categories. Proceedings of the American Academy of Arts and Sciences, 7, 287-298.",
             locator="7:287-298", locator_type="page_range",
             supports="three-place sign relation of sign, object and interpretant", verified=True),
        dict(kind="BOOK",
             title_en="Collected Papers of Charles Sanders Peirce",
             title_fa="مقالات گردآوری‌شدهٔ چارلز سندرس پیرس",
             authors="Peirce, C. S.", year=1931,
             publisher="Harvard University Press",
             doi=None, url=None, language="en", isbn=None,
             citation="Peirce, C. S. (1931-1958). Collected papers of Charles Sanders Peirce (Vols. 1-8). Harvard University Press.",
             locator="vols. 1-8", locator_type="work",
             supports="systematic elaboration of semiosis and the icon/index/symbol trichotomy", verified=False),
    ],
}

ENRICH = {
    "MC-432": dict(
        summary="قطب‌بندی عاطفی چارچوبی است که تنش سیاسی معاصر را نه با فاصلهٔ ایدئولوژیک، بلکه با بیزاری و بی‌اعتمادی عاطفی میان گروه‌های حزبی توضیح می‌دهد. شانتو اینگار، گوراو سود و یِفتاخ للکز در مقالهٔ سال ۲۰۱۲ نشان دادند که در ایالات متحده، دموکرات‌ها و جمهوری‌خواهان بیش از آنکه در مواضع سیاسی از هم دور شده باشند، احساسات منفی نسبت به حزب رقیب را تشدید کرده‌اند. آن‌ها این پدیده را با نظریهٔ هویت اجتماعی تفسیر کردند: حزب سیاسی به یک هویت گروهی تبدیل می‌شود و بیزاری از بیرون‌گروه، بخشی از تعریف خود گروه است. سنجه‌های رایج این چارچوب شامل دماسنج احساسی نسبت به حزب رقیب، فاصلهٔ اجتماعی در ازدواج فرزند با عضو حزب مقابل و ارزیابی صفات گروه مقابل است. یافتهٔ کلیدی آن بود که قطب‌بندی عاطفی از قطب‌بندی موضعی جدا است و می‌تواند حتی با میانه‌روی در سیاست‌ها هم‌زمان باشد. رسانه‌های حزبی، شبکه‌های اجتماعی و هم‌رنگی هویتی، این شکاف را تقویت می‌کنند و پیامدهایی مانند کاهش اعتماد به نهادهای دموکراتیک، بی‌اعتنایی به هنجارهای مدنی و دشواری سازش سیاسی دارند. کاربرد آن در تحلیل انتخابات، گفت‌وگوی عمومی، برنامه‌های کاهش قطب‌بندی و سیاست‌گذاری رسانه‌ای است. نقد اصلی به این چارچوب، وابستگی سنجه‌ها به زمینهٔ دوحزبی آمریکا، ابهام مرز عاطفه و ایدئولوژی و کم‌توجهی به نظام‌های چندحزبی است.",
        definition="قطب‌بندی عاطفی، فاصلهٔ احساسی و اجتماعی فزاینده میان هواداران گروه‌های سیاسی رقیب است که با بیزاری، بی‌اعتمادی و انزجار از بیرون‌گروه سنجیده می‌شود و لزوماً با فاصلهٔ مواضع سیاسی یکسان نیست.",
        main_problem="چرا شکاف سیاسی امروز بیش از اختلاف در سیاست‌ها، شکل دشمنی عاطفی میان گروه‌ها به خود گرفته و این دشمنی چه پیامدهایی برای گفت‌وگوی عمومی و نهادهای دموکراتیک دارد.",
        mechanism="حزب به هویتی اجتماعی تبدیل می‌شود که عزت نفس فرد را به موفقیت گروه گره می‌زند؛ رسانه‌های هم‌سو، شبکه‌های اجتماعی و هم‌رنگی با همتایان، تصویر منفی بیرون‌گروه را تکرار و تقویت می‌کنند و فاصلهٔ اجتماعی را گسترش می‌دهند.",
        assumptions=[
            "هویت حزبی به‌مثابه هویت گروهی عمل می‌کند.",
            "عاطفهٔ منفی به بیرون‌گروه از اختلاف موضع مستقل است.",
            "سنجه‌های احساسی، ابعادی از قطب‌بندی را می‌سنجند که سنجه‌های موضعی نمی‌بینند.",
            "رسانه و شبکهٔ همتایان در تشدید عاطفه نقش دارند.",
        ],
        principles=[
            "قطب‌بندی عاطفی و قطب‌بندی موضعی دو پدیدهٔ متمایزند.",
            "بیزاری از بیرون‌گروه، بخشی از هویت درون‌گروه است.",
            "فاصلهٔ اجتماعی، شاخصی قوی‌تر از اختلاف سیاستی است.",
            "کاهش قطب‌بندی نیازمند مداخله در هویت و عاطفه است، نه فقط در محتوا.",
        ],
        critiques=[
            "سنجه‌ها بر نظام دوحزبی آمریکا متمرکزند و تعمیم آن‌ها دشوار است.",
            "مرز میان عاطفه و ایدئولوژی در عمل مبهم است.",
            "نقش انگیزه‌های اقتصادی و نابرابری کمتر تحلیل می‌شود.",
            "برخی پژوهش‌ها شدت قطب‌بندی در افکار عمومی را کمتر از نخبگان می‌یابند.",
        ],
        applications=[
            "تحلیل شکاف حزبی در پوشش خبری و شبکه‌های اجتماعی.",
            "طراحی برنامه‌های گفت‌وگوی میان‌گروهی و کاهش دشمنی.",
            "ارزیابی اثر رسانه‌های حزبی بر نگرش مخاطبان.",
            "سنجش سلامت دموکراتیک و اعتماد نهادی.",
        ],
        evolution="پژوهش قطب‌بندی نخست بر فاصلهٔ مواضع سیاستی متمرکز بود؛ اینگار و همکاران (۲۰۱۲) با افزودن مفهوم عاطفه و هویت اجتماعی، کانون را جابه‌جا کردند و مرور ۲۰۱۹ آن را به چارچوبی برای سنجش، علل و پیامدها تبدیل کرد.",
        key_concepts=[
            "هویت حزبی (Partisan Identity)",
            "دماسنج احساسی (Feeling Thermometer)",
            "فاصلهٔ اجتماعی (Social Distance)",
            "بیرون‌گروه (Out-Group)",
            "هم‌رنگی هویتی (Identity Sorting)",
        ],
        theorists="شانتو اینگار؛ گوراو سود؛ یِفتاخ للکز",
        theorists_text="اینگار، سود و للکز (۲۰۱۲)؛ اینگار و همکاران (۲۰۱۹)",
        model="هویت حزبی → ارزیابی عاطفی بیرون‌گروه → فاصلهٔ اجتماعی → کاهش اعتماد و سازش سیاسی.",
        studies=[
            "اینگار و همکاران (۲۰۱۲) نشان دادند قطب‌بندی عاطفی از قطب‌بندی موضعی مستقل است.",
            "اینگار و همکاران (۲۰۱۹) سنجه‌ها، علل و پیامدهای قطب‌بندی عاطفی را مرور کردند.",
        ],
        detailed_analysis="تحلیل عمیق نشان می‌دهد قطب‌بندی عاطفی بیش از آنکه محصول اختلاف نظر باشد، محصول مرزبندی هویتی است. وقتی حزب به بخشی از «ما» تبدیل می‌شود، نقد حزب رقیب به دفاع از خود تعبیر می‌شود و سازش به خیانت می‌انجامد. رسانه‌های حزبی با برجسته‌سازی بدترین نمونه‌های گروه مقابل، این مرزبندی را تقویت می‌کنند. از این رو مداخله‌های مؤثر بر بازسازی هویت مشترک و تجربهٔ تعامل میان‌گروهی تأکید می‌کنند، نه فقط بر تصحیح اطلاعات.",
        critique_text="نقد اصلی آن است که سنجه‌ها بر نظام دوحزبی آمریکا متمرکزند، مرز عاطفه و ایدئولوژی مبهم است و نقش نابرابری اقتصادی در تولید دشمنی کمتر تحلیل می‌شود.",
        example_text="دو شهروند که در بیشتر سیاست‌ها میانه‌رو هستند، ممکن است از ازدواج فرزندشان با هوادار حزب رقیب ابراز نگرانی کنند؛ همین فاصلهٔ اجتماعی، نمونهٔ عملی قطب‌بندی عاطفی است.",
        year=2012,
    ),
    "MC-442": dict(
        summary="ابعاد فرهنگی هافستد چارچوبی برای مقایسهٔ فرهنگ‌های ملی بر پایهٔ ارزش‌های کاری است. خرت هافستد در کتاب سال ۱۹۸۰ خود داده‌های پیمایشی حدود صد هزار کارمند یک شرکت چندملیتی در بیش از چهل کشور را تحلیل کرد و چهار بعد را شناسایی کرد: فاصلهٔ قدرت، یعنی میزان پذیرش توزیع نابرابر قدرت در نهادها؛ فردگرایی در برابر جمع‌گرایی، یعنی اولویت منافع فرد یا گروه؛ مردانگی در برابر زنانگی، یعنی تأکید بر رقابت و دستاورد یا بر همکاری و کیفیت زندگی؛ و اجتناب از عدم قطعیت، یعنی تحمل ابهام و تهدید. بعد پنجم، جهت‌گیری بلندمدت در برابر کوتاه‌مدت، در همکاری با مایکل باند و با داده‌های ارزش‌های آسیایی افزوده شد و بعد ششم، آسان‌گیری در برابر مهار، از پژوهش‌های مینکوف در سال ۲۰۱۰ به چارچوب وارد شد. هر کشور در هر بعد امتیازی نسبی می‌گیرد و ترکیب این امتیازها، نیمرخ فرهنگی آن را می‌سازد. این چارچوب در ارتباطات بین‌فرهنگی، مدیریت سازمانی، بازاریابی بین‌المللی و تحلیل سبک ارتباطی کاربرد گسترده دارد؛ برای نمونه، تفاوت در فاصلهٔ قدرت با تفاوت در انتظار سلسله‌مراتب در ارتباط سازمانی پیوند می‌یابد. نقدهای اصلی به آن، خطای بوم‌شناختی در تعمیم امتیاز ملی به فرد، فرض همگنی فرهنگ ملی، سوگیری نمونهٔ کارمندان یک شرکت و قدمت داده‌های پایه است.",
        definition="ابعاد فرهنگی هافستد، مجموعه‌ای از شش بعد ارزشی است که تفاوت‌های فرهنگ‌های ملی را در نگرش به قدرت، گروه، جنسیت، ابهام، زمان و لذت قابل مقایسه می‌سازد.",
        main_problem="چگونه می‌توان تفاوت‌های فرهنگی میان کشورها را به‌صورت نظام‌مند و قابل مقایسه سنجید، بدون فروکاستن فرهنگ به مجموعه‌ای از کلیشه‌های ثابت.",
        mechanism="پیمایش ارزش‌های کاری، پاسخ‌ها را در قالب امتیازهای نسبی در هر بعد سازمان می‌دهد؛ ترکیب امتیازها نیمرخ فرهنگی می‌سازد و پژوهشگر تفاوت انتظارهای ارتباطی و سازمانی را از این نیمرخ استنتاج می‌کند.",
        assumptions=[
            "فرهنگ ملی را می‌توان در قالب ابعاد ارزشی مقایسه کرد.",
            "ارزش‌های کاری، بازتاب فرهنگ گسترده‌تر جامعه‌اند.",
            "امتیازهای ملی، میانگین گرایش‌ها را نشان می‌دهند نه ویژگی هر فرد.",
            "ابعاد نسبتاً پایدارند و در بازه‌های زمانی کوتاه تغییر نمی‌کنند.",
        ],
        principles=[
            "هر بعد یک پیوستار است، نه دوگانهٔ مطلق.",
            "فاصلهٔ قدرت، الگوی ارتباط با مرجع قدرت را شکل می‌دهد.",
            "فردگرایی و جمع‌گرایی، مرز میان من و گروه را تعیین می‌کند.",
            "اجتناب از عدم قطعیت، تحمل ابهام و قاعده‌مندی را می‌سنجد.",
        ],
        critiques=[
            "خطای بوم‌شناختی: امتیاز ملی را نمی‌توان به فرد تعمیم داد.",
            "فرض همگنی فرهنگ ملی، تنوع درونی و اقلیت‌ها را نادیده می‌گیرد.",
            "نمونهٔ کارمندان یک شرکت، بازنمایی کل جامعه نیست.",
            "داده‌های پایه قدیمی‌اند و تغییرات فرهنگی را کم‌تر بازتاب می‌دهند.",
        ],
        applications=[
            "تحلیل تفاوت سبک ارتباط سازمانی در شرکت‌های چندملیتی.",
            "طراحی پیام و کمپین بازاریابی بین‌فرهنگی.",
            "آموزش ارتباطات بین‌فرهنگی و مدیریت تنوع.",
            "پژوهش تطبیقی دربارهٔ اعتماد و سلسله‌مراتب در رسانه.",
        ],
        evolution="هافستد (۱۹۸۰) چهار بعد را از داده‌های پیمایش کارمندان استخراج کرد؛ بعد پنجم با همکاری باند و داده‌های آسیایی افزوده شد و بعد ششم از پژوهش مینکوف (۲۰۱۰) به مدل وارد شد.",
        key_concepts=[
            "فاصلهٔ قدرت (Power Distance)",
            "فردگرایی/جمع‌گرایی (Individualism/Collectivism)",
            "مردانگی/زنانگی (Masculinity/Femininity)",
            "اجتناب از عدم قطعیت (Uncertainty Avoidance)",
            "جهت‌گیری بلندمدت (Long-Term Orientation)",
        ],
        theorists="خرت هافستد؛ مایکل باند؛ گرت مینکوف",
        theorists_text="هافستد (۱۹۸۰)؛ هافستد (۲۰۰۱)؛ مینکوف (۲۰۱۰)",
        model="پیمایش ارزش‌های کاری → امتیاز در شش بعد → نیمرخ فرهنگی ملی → استنتاج الگوهای ارتباطی و سازمانی.",
        studies=[
            "هافستد (۱۹۸۰) چهار بعد فرهنگی را از پیمایش کارمندان یک شرکت چندملیتی استخراج کرد.",
            "هافستد (۲۰۰۱) مدل را بازنگری و بسط داد و مینکوف (۲۰۱۰) بعد ششم را افزود.",
        ],
        detailed_analysis="تحلیل عمیق نشان می‌دهد ارزش چارچوب در زبان مشترکی است که مقایسهٔ فرهنگ‌ها را ممکن می‌کند، اما خطر آن در تبدیل ابزار تحلیلی به کلیشهٔ فردی است. امتیاز ملی، گرایش میانگین است و نمی‌تواند رفتار یک فرد را پیش‌بینی کند. در پژوهش رسانه، این ابعاد برای تفسیر تفاوت انتظار از اقتدار در خبر، سبک گفت‌وگوی سیاسی و پذیرش هنجارهای تبلیغاتی به کار می‌رود، به شرط آنکه با داده‌های بومی و زمینهٔ تاریخی همراه شود.",
        critique_text="نقد اصلی آن است که چارچوب به خطای بوم‌شناختی دامن می‌زند، فرهنگ ملی را همگن فرض می‌کند و داده‌های پایهٔ آن از نمونه‌ای محدود و قدیمی می‌آید.",
        example_text="در سازمانی با فاصلهٔ قدرت بالا، کارمند ممکن است انتقاد از تصمیم مدیر را حتی در جلسهٔ آزاد بیان نکند؛ همین تفاوت در الگوی ارتباط، پیامد مستقیم بعد فاصلهٔ قدرت است.",
        year=1980,
    ),
    "MC-461": dict(
        summary="پسااستعمارگرایی و بازنمایی دیگری، چارچوبی است که نشان می‌دهد چگونه غرب از طریق گفتمان شرق‌شناسی، تصویری خاص از شرق و شرقیان ساخت و آن را به‌عنوان حقیقت جا انداخت. ادوارد سعید در کتاب سال ۱۹۷۸ خود شرق‌شناسی را نه رشته‌ای بی‌طرف، بلکه سبکی از اندیشیدن و نهادی از قدرت دانست که با تولید متن، تصویر و دانش، برتری غرب را توجیه می‌کند. او سه معنای پیوسته برای شرق‌شناسی تشخیص داد: مطالعهٔ آکادمیک شرق، شیوهٔ اندیشیدن بر پایهٔ تمایز هستی‌شناختی شرق و غرب، و نهاد شرکتی برای سلطه بر شرق. چارچوب او از فوکو و گرامشی وام می‌گیرد: دانش با قدرت درهم‌تنیده است و سلطه از راه رضایت و هژمونی فرهنگی بازتولید می‌شود. سعید میان شرق‌شناسی نهفته و آشکار تمایز گذاشت: لایهٔ پایدار و تکرارشوندهٔ پیش‌داوری‌ها و لایهٔ متغیر ادعاهای روز. در این نگاه، شرق به‌عنوان موجودیتی غیرمنطقی، زنانه، بدوی و متزلزل بازنمایی می‌شود تا سوژهٔ غربی عقلانی و برتر جلوه کند. کاربرد آن در تحلیل بازنمایی شرق و اسلام در خبر و سینما، نقد تصویر مهاجر، مطالعهٔ گفتمان سیاست خارجی و سیاست هویت است. نقدهای اصلی، از یک سو به تعمیم بیش‌ازحد غرب و کم‌توجهی به مقاومت و از سوی دیگر به نادیده‌گرفتن تنوع درونی جوامع شرقی اشاره می‌کنند؛ از این رو پژوهش رسانه‌ای امروز این چارچوب را با تحلیل مخاطب و مطالعهٔ مقاومت روزمره ترکیب می‌کند.",
        definition="پسااستعمارگرایی، چارچوبی است برای تحلیل بازنمایی «دیگری» در گفتمان‌های استعماری و پسااستعماری که نشان می‌دهد دانش و تصویر، سازوکار مشروعیت‌بخشی به سلطه بوده‌اند.",
        main_problem="چگونه رسانه و دانش غربی، تصویری از شرق و شرقیان ساختند که سلطهٔ استعماری را طبیعی جلوه دهد و این تصویر چگونه در بازنمایی معاصر بازتولید می‌شود.",
        mechanism="متن‌ها، تصاویر و دانش تخصصی با تکرار نشانه‌های ثابت، شرق را به‌عنوان دیگری غیرمنطقی و نیازمند هدایت بازنمایی می‌کنند؛ این تکرار نهادی، چارچوبی می‌سازد که هر خبر و رویداد تازه در آن تفسیر می‌شود.",
        assumptions=[
            "دانش و بازنمایی از قدرت جدا نیستند.",
            "گفتمان با تکرار نهادی، حقیقت خود را تثبیت می‌کند.",
            "تمایز شرق و غرب ساختهٔ تاریخی است، نه واقعیتی طبیعی.",
            "رسانه یکی از نهادهای بازتولید این گفتمان است.",
        ],
        principles=[
            "دیگری‌سازی، پیش‌شرط توجیه سلطه است.",
            "شرق‌شناسی نهفته، لایهٔ پایدار پیش‌داوری‌ها را حفظ می‌کند.",
            "بازنمایی، کنشی سیاسی است و نه آیینهٔ واقعیت.",
            "نقد پسااستعماری به دنبال شنیدن صدای دیگری است، نه سخن‌گفتن به‌جای او.",
        ],
        critiques=[
            "تعمیم یکپارچهٔ «غرب» تنوع و نقدهای درونی آن را نادیده می‌گیرد.",
            "به مقاومت و عاملیت جوامع شرقی کم‌تر می‌پردازد.",
            "خطر تقلیل تحلیل‌های پیچیده به دوگانهٔ سادهٔ سلطه و قربانی.",
            "تنوع درونی و تعارض‌های جوامع پسااستعماری کمتر دیده می‌شود.",
        ],
        applications=[
            "تحلیل بازنمایی اسلام و شرق در خبر و سرگرمی.",
            "نقد تصویر مهاجر و اقلیت در رسانه.",
            "مطالعهٔ گفتمان سیاست خارجی و مستندسازی سفر.",
            "پژوهش سیاست هویت و روایت‌های پسااستعماری.",
        ],
        evolution="چارچوب با کتاب شرق‌شناسی (۱۹۷۸) بنیان گذاشته شد؛ سعید در فرهنگ و امپریالیسم (۱۹۹۳) آن را به فرم‌های فرهنگی و روایت مقاومت گسترد؛ پژوهش‌های بعدی آن را به مطالعات رسانه، نژاد و مهاجرت پیوند زدند.",
        key_concepts=[
            "شرق‌شناسی (Orientalism)",
            "دیگری‌سازی (Othering)",
            "هژمونی (Hegemony)",
            "گفتمان استعماری (Colonial Discourse)",
            "شرق‌شناسی نهفته/آشکار (Latent/Manifest Orientalism)",
        ],
        theorists="ادوارد سعید",
        theorists_text="سعید (۱۹۷۸)؛ سعید (۱۹۹۳)",
        model="گفتمان نهادی → تکرار نشانه‌های دیگری → طبیعی‌سازی سلطه → بازتولید برتری سوژهٔ غربی.",
        studies=[
            "سعید (۱۹۷۸) سه معنای پیوستهٔ شرق‌شناسی و سازوکار بازتولید آن را تحلیل کرد.",
            "سعید (۱۹۹۳) نقد را به فرم‌های فرهنگی و روایت‌های مقاومت گسترش داد.",
        ],
        detailed_analysis="تحلیل عمیق نشان می‌دهد خطر گفتمان شرق‌شناسانه در توزیع نابرابر حق روایت است: رویداد یکسان، بسته به گوینده، به روایت ترقی یا خشونت تبدیل می‌شود. رسانه با انتخاب منبع، واژگان و تصویر، این توزیع را بازتولید می‌کند. نقد پسااستعماری از پژوهشگر می‌خواهد نگاه خود را نیز به‌عنوان بخشی از میدان قدرت بازبینی کند و از بازتولید دوگانه‌های ساده بپرهیزد.",
        critique_text="نقد اصلی آن است که تعمیم یکپارچهٔ غرب و کم‌توجهی به مقاومت و تنوع درونی جوامع شرقی، خطر تقلیل تحلیل به دوگانهٔ سادهٔ سلطه و قربانی را ایجاد می‌کند.",
        example_text="وقتی رسانه‌ای برای پوشش یک اعتراض در کشوری شرقی، واژگان هرج‌ومرج و نیاز به مداخلهٔ بیرونی را برجسته می‌کند اما برای اعتراض مشابه در غرب از واژهٔ مطالبهٔ مدنی استفاده می‌کند، تفاوت واژگان، بازتولید چارچوب شرق‌شناسانه است.",
        year=1978,
    ),
    "MC-481": dict(
        summary="سه‌گانهٔ نشانه، هستهٔ نشانه‌شناسی چارلز سندرس پیرس است و نشانه را نه یک چیز، بلکه یک رابطهٔ سه‌جزئی می‌داند. پیرس در مقالهٔ سال ۱۸۶۷ خود نشان داد که معناداری در نسبتی میان سه عنصر شکل می‌گیرد: نشانه یا نماینده، یعنی آنچه به کار می‌رود؛ موضوع، یعنی آنچه نشانه به آن ارجاع می‌دهد؛ و تفسیرگر، یعنی اثر یا معنایی که نشانه در ذهن یا در نشانهٔ بعدی می‌سازد. برخلاف الگوی دوجزئی که تنها نشانه و مصداق را می‌بیند، مدل پیرس توضیح می‌دهد که چگونه معنا در زنجیرهٔ تفسیرها ساخته می‌شود: هر تفسیرگر خود می‌تواند نشانه‌ای تازه شود و فرایند نشانه‌ای بی‌پایان ادامه یابد. پیرس سه‌گانهٔ دوم را نیز برای نسبت نشانه با موضوع عرضه کرد: شمایل که شباهت دارد، نمایه که رابطهٔ علّی یا مجاورت دارد و نماد که بر پایهٔ قرارداد معنا می‌یابد. این تمایز امروز پایهٔ تحلیل عکس، نقشه، رد پا، پرچم و واژه است. سه‌گانهٔ نشانه با مقولات سه‌گانهٔ پیرس نیز پیوند دارد: اولی بودن، دومی بودن و سومی بودن. کاربرد چارچوب در تحلیل نشانه‌شناختی تبلیغات، عکاسی خبری، رابط کاربری و نشانه‌های فرهنگی گسترده است. نقد اصلی به آن، ناپایداری اصطلاح‌ها در آثار مختلف پیرس، دشواری کاربرد عملی سه‌گانه در تحلیل تجربی و خطر تفسیر ذهنی و بی‌مرز از زنجیرهٔ تفسیرگرهاست.",
        definition="سه‌گانهٔ نشانه، مدلی است که معناداری را حاصل رابطهٔ سه‌جزئی نشانه، موضوع و تفسیرگر می‌داند و برخلاف مدل دوجزئی، فرایند تفسیر را بخشی از خود نشانه می‌شمارد.",
        main_problem="چگونه یک چیز به نشانه تبدیل می‌شود و معنا در چه فرایندی ساخته می‌شود، بدون آنکه نشانه به رابطهٔ سادهٔ واژه و مصداق فروکاسته شود.",
        mechanism="نشانه در برابر موضوع قرار می‌گیرد و در مفسر یا نشانهٔ بعدی اثری می‌سازد؛ این اثر، تفسیرگر نام دارد و خود می‌تواند نشانه‌ای تازه شود. زنجیرهٔ پیوستهٔ تفسیرگرها، فرایند نشانه‌ای را می‌سازد.",
        assumptions=[
            "نشانه بودن یک رابطه است، نه ویژگی ذاتی یک چیز.",
            "تفسیرگر، عنصر سازندهٔ معناست و نه افزوده‌ای بیرونی.",
            "نشانه‌ها در سه نسبت شمایلی، نمایه‌ای و نمادین با موضوع پیوند می‌یابند.",
            "فرایند نشانه‌ای می‌تواند بی‌پایان ادامه یابد.",
        ],
        principles=[
            "هر نشانه سه‌جزئی است: نماینده، موضوع و تفسیرگر.",
            "شمایل با شباهت، نمایه با رابطهٔ واقعی و نماد با قرارداد معنا می‌یابد.",
            "معنا در زنجیرهٔ تفسیر ساخته می‌شود، نه در یک نقطهٔ ثابت.",
            "مخاطب، خود بخشی از فرایند تفسیر است.",
        ],
        critiques=[
            "اصطلاح‌های پیرس در دوره‌های مختلف آثارش تغییر کرده‌اند.",
            "سه‌گانه برای تحلیل تجربی و کمی دشوار عملیاتی می‌شود.",
            "زنجیرهٔ نامحدود تفسیر می‌تواند به تفسیر ذهنی و بی‌مرز بینجامد.",
            "مرز دقیق میان شمایل، نمایه و نماد در نمونه‌های ترکیبی مبهم است.",
        ],
        applications=[
            "تحلیل نشانه‌شناختی تبلیغات و عکاسی خبری.",
            "طراحی رابط کاربری و ارزیابی شفافیت نمادها.",
            "خوانش نشانه‌های فرهنگی و آیینی در رسانه.",
            "آموزش سواد بصری و تحلیل معنای تصویر.",
        ],
        evolution="پیرس سه‌گانه را در مقالهٔ ۱۸۶۷ صورت‌بندی کرد و در دوره‌های بعدی با مقولات و سه‌گانهٔ شمایل، نمایه و نماد بسط داد؛ مقاله‌های گردآوری‌شدهٔ او در نیمهٔ نخست سدهٔ بیستم، این چارچوب را به پایهٔ نشانه‌شناسی معاصر تبدیل کرد.",
        key_concepts=[
            "نشانه (Sign/Representamen)",
            "موضوع (Object)",
            "تفسیرگر (Interpretant)",
            "شمایل، نمایه، نماد (Icon, Index, Symbol)",
            "فرایند نشانه‌ای (Semiosis)",
        ],
        theorists="چارلز سندرس پیرس",
        theorists_text="پیرس (۱۸۶۷)؛ مقالات گردآوری‌شدهٔ پیرس",
        model="نشانه → موضوع → تفسیرگر → نشانهٔ تازه؛ در سه نسبت شمایلی، نمایه‌ای و نمادین.",
        studies=[
            "پیرس (۱۸۶۷) رابطهٔ سه‌جزئی نشانه را در فهرست تازهٔ مقولات صورت‌بندی کرد.",
            "مجموعهٔ مقالات پیرس، سه‌گانهٔ شمایل، نمایه و نماد و فرایند نشانه‌ای را بسط داد.",
        ],
        detailed_analysis="تحلیل عمیق نشان می‌دهد قدرت مدل پیرس در آن است که معنا را از رابطهٔ دوتایی واژه و شیء جدا می‌کند و مخاطب را وارد ساخت معنا می‌سازد. در عکاسی خبری، یک تصویر می‌تواند هم‌زمان شمایل باشد، زیرا شبیه صحنه است؛ نمایه باشد، زیرا رد نور واقعی است؛ و نماد باشد، زیرا در چارچوب خبری معنای قراردادی می‌گیرد. همین هم‌زمانی، مدل سه‌گانه را برای تحلیل رسانه کارآمدتر از تقسیم‌بندی‌های ساده می‌کند.",
        critique_text="نقد اصلی آن است که اصطلاح‌های پیرس در دوره‌های مختلف آثارش ناپایدارند، سه‌گانه به‌سختی عملیاتی می‌شود و زنجیرهٔ نامحدود تفسیر می‌تواند به تفسیر ذهنی بیانجامد.",
        example_text="دود در دوردست، نمایهٔ آتش است؛ تصویر شعله روی جلد مجله، شمایل آن است؛ و واژهٔ «آتش‌سوزی» در تیتر، نمادی قراردادی برای همان رویداد است.",
        year=1867,
    ),
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


NAME_FIX = {
    "MC-432": ("قطب‌بندی عاطفی", "Affective Polarization",
               "name normalized: 'دوقطبی‌سازی عاطفی' -> 'قطب‌بندی عاطفی' (standard Persian term for affective polarization)"),
    "MC-442": ("ابعاد فرهنگی هافستد", "Hofstede's Cultural Dimensions",
               "name corrected: 'هافستده' -> 'هافستد' (transliteration of Hofstede)"),
    "MC-481": ("سه‌گانهٔ نشانه (پیرس)", "The Semiotic Triad",
               "name normalized: 'نشانه سه‌گانه' -> 'سه‌گانهٔ نشانه (پیرس)'"),
}
YEAR_FIX = {
    "MC-481": "year filled: none -> 1867 (Peirce, On a New List of Categories, 1867)",
}


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
                                       "verified": n_verified, "batch": 121}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH121 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
