# -*- coding: utf-8 -*-
"""Batch 159 (MODEL+THEORY): MC-711 internet addiction, MC-536 parasocial interaction, MC-537 play theory, MC-557 mean world syndrome."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch159-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch159_model.json"

S = {
    "MC-711": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Internet Addiction: The Emergence of a New Clinical Disorder",
             title_fa="اعتیاد به اینترنت: ظهور یک اختلال بالینی تازه",
             authors="Young, K. S.", year=1998,
             publisher="CyberPsychology & Behavior",
             doi="10.1089/cpb.1998.1.237",
             url="https://journals.sagepub.com/doi/10.1089/cpb.1998.1.237",
             language="en", isbn=None,
             citation="Young, K. S. (1998). Internet addiction: The emergence of a new clinical disorder. CyberPsychology & Behavior, 1(3), 237-244.",
             locator="1(3):237-244", locator_type="page_range",
             supports="clinical criteria and prevalence estimate for internet addiction", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="A 'Components' Model of Addiction within a Biopsychosocial Framework",
             title_fa="مدل مؤلفه‌ای اعتیاد در چارچوب زیست‌روان‌اجتماعی",
             authors="Griffiths, M.", year=2005,
             publisher="Journal of Substance Use",
             doi="10.1080/14659890500114359",
             url="https://www.tandfonline.com/doi/abs/10.1080/14659890500114359",
             language="en", isbn=None,
             citation="Griffiths, M. (2005). A 'components' model of addiction within a biopsychosocial framework. Journal of Substance Use, 10(4), 191-197.",
             locator="10(4):191-197", locator_type="page_range",
             supports="six components: salience, mood modification, tolerance, withdrawal, conflict, relapse", verified=True),
    ],
    "MC-536": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Mass Communication and Para-Social Interaction: Observations on Intimacy at a Distance",
             title_fa="ارتباط جمعی و تعامل فرااجتماعی: مشاهده‌هایی دربارهٔ صمیمیت از راه دور",
             authors="Horton, D.; Wohl, R. R.", year=1956,
             publisher="Psychiatry",
             doi="10.1080/00332747.1956.11023049",
             url="https://www.tandfonline.com/doi/abs/10.1080/00332747.1956.11023049",
             language="en", isbn=None,
             citation="Horton, D., & Wohl, R. R. (1956). Mass communication and para-social interaction. Psychiatry, 19(3), 215-229.",
             locator="19(3):215-229", locator_type="page_range",
             supports="one-sided intimacy between audience and media persona", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Loneliness, Parasocial Interaction, and Local Television News Viewing",
             title_fa="تنهایی، تعامل فرااجتماعی و تماشای خبر تلویزیون محلی",
             authors="Rubin, A. M.; Perse, E. M.; Powell, R. A.", year=1985,
             publisher="Human Communication Research",
             doi="10.1111/j.1468-2958.1985.tb00071.x",
             url="https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1468-2958.1985.tb00071.x",
             language="en", isbn=None,
             citation="Rubin, A. M., Perse, E. M., & Powell, R. A. (1985). Loneliness, parasocial interaction, and local television news viewing. Human Communication Research, 12(2), 155-180.",
             locator="12(2):155-180", locator_type="page_range",
             supports="operational scale and predictors of parasocial interaction", verified=True),
    ],
    "MC-537": [
        dict(kind="BOOK",
             title_en="The Play Theory of Mass Communication",
             title_fa="نظریهٔ بازی در ارتباطات جمعی",
             authors="Stephenson, W.", year=1967,
             publisher="University of Chicago Press",
             doi=None,
             url="https://books.google.com/books/about/The_Play_Theory_of_Mass_Communication.html?id=LJthAAAAMAAJ",
             language="en", isbn=None,
             citation="Stephenson, W. (1967). The Play Theory of Mass Communication. Chicago: University of Chicago Press.",
             locator="1967 edition", locator_type="edition",
             supports="media use as play and communication-pleasure rather than work", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Review of The Play Theory of Mass Communication",
             title_fa="مروری بر نظریهٔ بازی در ارتباطات جمعی",
             authors="Williams, T. A.", year=1971,
             publisher="American Political Science Review",
             doi=None,
             url="https://www.cambridge.org/core/journals/american-political-science-review/article/play-theory-of-mass-communication-by-william-stephenson-chicago-university-of-chicago-press-1967-pp-x-225-500/DA56F0ED3628C8DFE3B8AD9C2BDABCCC",
             language="en", isbn=None,
             citation="Williams, T. A. (1971). Review of The Play Theory of Mass Communication. American Political Science Review, 65(2).",
             locator="65(2)", locator_type="review",
             supports="contemporaneous scholarly assessment of the play theory", verified=True),
    ],
    "MC-557": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Living with Television: The Violence Profile",
             title_fa="زندگی با تلویزیون: نمای خشونت",
             authors="Gerbner, G.; Gross, L.", year=1976,
             publisher="Journal of Communication",
             doi="10.1111/j.1460-2466.1976.tb01397.x",
             url="https://academic.oup.com/joc/article-abstract/26/2/172/4553823",
             language="en", isbn=None,
             citation="Gerbner, G., & Gross, L. (1976). Living with television: The violence profile. Journal of Communication, 26(2), 172-199.",
             locator="26(2):172-199", locator_type="page_range",
             supports="cultivation of fear and overestimation of violence among heavy viewers", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="The 'Mainstreaming' of America: Violence Profile No. 11",
             title_fa="«جریان اصلی‌سازی» آمریکا: نمای خشونت شمارهٔ ۱۱",
             authors="Gerbner, G.; Gross, L.; Morgan, M.; Signorielli, N.", year=1980,
             publisher="Journal of Communication",
             doi="10.1111/j.1460-2466.1980.tb01987.x",
             url="https://academic.oup.com/joc/article-abstract/30/3/10/4371855",
             language="en", isbn=None,
             citation="Gerbner, G., Gross, L., Morgan, M., & Signorielli, N. (1980). The 'mainstreaming' of America: Violence profile no. 11. Journal of Communication, 30(3), 10-29.",
             locator="30(3):10-29", locator_type="page_range",
             supports="mainstreaming of heavy viewers' worldviews toward a mean world", verified=True),
    ],
}

ENRICH = {
    "MC-711": dict(
        year=1998,
        summary="مدل اعتیاد به اینترنت و رسانه، که کیمبرلی یانگ در سال ۱۹۹۸ با معرفی اعتیاد به اینترنت به‌عنوان اختلال بالینی تازه آغاز شد و مارک گریفیتس در سال ۲۰۰۵ صورت‌بندی مؤلفه‌ای آن را داد، استفادهٔ مسئله‌ساز از رسانه را با نشانه‌های اعتیاد رفتاری می‌سنجد. یانگ هشت نشانه را برشمرد: اشتغال ذهنی، نیاز به زمان فزاینده، تلاش ناموفق برای کنترل، بی‌قراری هنگام قطع، استفاده برای تنظیم خلق، پنهان‌کاری، از دست رفتن علاقه‌های دیگر و آسیب به کار و روابط. گریفیتس مدل را ساده‌تر و منظم‌تر کرد و شش مؤلفه را معرفی کرد: برجستگی، تغییر خلق، تحمل، نشانه‌های ترک، تعارض و بازگشت. مدل، اعتیاد را نه ویژگی رسانه، بلکه الگوی رابطهٔ کاربر با رسانه می‌داند: بیشتر کاربران مسئله‌دار به آن اعتراف نمی‌کنند و مشکل با افزایش استفاده آغاز می‌شود و به تعارض در کار و رابطه می‌رسد. مدل برای غربالگری، درمان شناختی رفتاری، طراحی سیاست استفادهٔ کودکان و تحلیل رسانه‌های اجتماعی به کار می‌رود. نقدهای اصلی به آن، آسیب‌شناختی‌کردن رفتار روزمره، وابستگی به خودگزارشی، تعمیم‌پذیری فرهنگی، همبودی با اختلال‌های دیگر و نبود اجماع طبقه‌بندی را برجسته می‌کنند.",
        definition="مدل اعتیاد به اینترنت و رسانه، استفادهٔ مسئله‌ساز از رسانه را با شش مؤلفهٔ اعتیاد رفتاری می‌سنجد و آن را الگوی رابطهٔ کاربر با رسانه می‌داند، نه ویژگی ذاتی رسانه.",
        main_problem="چه زمانی استفاده از اینترنت و رسانه از سرگرمی به الگوی اعتیادی با پیامدهای منفی می‌رسد و چگونه می‌توان آن را به‌طور معتبر سنجید و درمان کرد.",
        mechanism="استفادهٔ فزاینده، تحمل و برجستگی می‌سازد؛ قطع، نشانهٔ ترک و تغییر خلق ایجاد می‌کند؛ ادامهٔ چرخه به تعارض با کار، خواب و روابط می‌رسد و در نبود مداخله، الگو تثبیت می‌شود.",
        assumptions=[
            "اعتیاد رفتاری الگوی معتبری است.",
            "رسانه می‌تواند وابستگی بسازد.",
            "شش مؤلفه قابل سنجش‌اند.",
            "کاربر مسئله‌دار انکار می‌کند.",
            "مداخله زودهنگام اثر دارد.",
        ],
        principles=[
            "الگوی استفاده را بسنج، نه حجم را.",
            "شش مؤلفه را جدا بررسی کن.",
            "تعارض کار و رابطه را نشانه بگیر.",
            "مداخله را زودهنگام آغاز کن.",
            "به همبودی اختلال‌ها توجه کن.",
            "خودگزارشی را با داده ترکیب کن.",
            "به عوامل زمینه‌ای مانند تنهایی توجه کن.",
        ],
        critiques=[
            "رفتار روزمره را آسیب‌شناختی می‌کند.",
            "به خودگزارشی وابسته است.",
            "تعمیم‌پذیری فرهنگی محدود است.",
            "همبودی با اختلال‌های دیگر روشن نیست.",
            "اجماع طبقه‌بندی وجود ندارد.",
            "به طراحی پلتفرم و انگیزهٔ صنعت کم می‌پردازد.",
            "مرز استفادهٔ زیاد و اختلال را دقیق تعیین نمی‌کند.",
            "به نقش عوامل زمینه‌ای مانند تنهایی کم توجه دارد.",
            "نقش هنجار فرهنگی در مصرف را کم می‌بیند.",
        ],
        critique_text="منتقدان می‌گویند مدل اعتیاد به اینترنت سنجش الگوی استفاده را ممکن کرد اما مرز سرگرمی و اختلال را مبهم گذاشت و انگیزهٔ طراحی پلتفرم را کم‌بررسی کرد؛ با این حال، چارچوب پایهٔ پژوهش استفادهٔ مسئله‌ساز است.",
        applications=[
            "غربالگری اعتیاد اینترنتی.",
            "درمان شناختی رفتاری.",
            "سیاست استفادهٔ کودکان.",
            "تحلیل استفادهٔ رسانهٔ اجتماعی.",
            "آموزش بهداشت دیجیتال.",
            "پژوهش خواب و رسانه.",
            "طراحی برنامهٔ ترک استفاده.",
            "ارزیابی بازی آنلاین.",
            "سنجش استفادهٔ مسئله‌ساز در نوجوانان.",
            "طراحی سیاست مدرسه برای تلفن همراه.",
        ],
        example_text="کسی که شب‌ها بی‌قرارانه تلفن را باز می‌کند، خوابش را از دست می‌دهد و صبح از کار عقب می‌ماند، نشانه‌های ترک و تعارض را همزمان دارد؛ مدل می‌گوید مسئله حجم استفاده نیست، الگوی رابطه است.",
        evolution="یانگ در سال ۱۹۹۸ اعتیاد اینترنتی را به‌عنوان اختلال بالینی معرفی کرد و گریفیتس در سال ۲۰۰۵ مدل مؤلفه‌ای را ساخت؛ سپس پژوهش‌های اعتیاد به گوشی، بازی و رسانهٔ اجتماعی و طبقه‌بندی اختلال بازی آن را گستردند.",
        key_concepts=["اعتیاد اینترنتی", "برجستگی", "تحمل", "نشانهٔ ترک", "تعارض", "بازگشت"],
        theorists="کیمبرلی یانگ و مارک گریفیتس.",
        theorists_text="مدل در سنت روان‌شناسی اعتیاد رفتاری شکل گرفت.",
        model="استفادهٔ مسئله‌ساز از رسانه به‌عنوان الگوی اعتیاد رفتاری با شش مؤلفهٔ سنجش‌پذیر.",
        studies=[
            "مقالهٔ سال ۱۹۹۸ نشانه‌های بالینی را معرفی کرد.",
            "مقالهٔ سال ۲۰۰۵ مدل مؤلفه‌ای را ساخت.",
            "پژوهش خواب، استفادهٔ شبانه را سنجید.",
            "مطالعهٔ بازی، مؤلفه‌ها را در گیمرها آزمود.",
            "مطالعهٔ طولی، رابطهٔ استفاده و افسردگی را بررسی کرد.",
            "پژوهش نوجوان، غربالگری مدرسه را ارزیابی کرد.",
        ],
    ),
    "MC-536": dict(
        year=1956,
        summary="نظریهٔ تعامل فرااجتماعی، که دانلد هورتون و ریچارد وهل در سال ۱۹۵۶ با عنوان «صمیمیت از راه دور» معرفی کردند، توضیح می‌دهد که مخاطب چگونه با شخصیت رسانه‌ای رابطه‌ای یک‌سویه و صمیمی می‌سازد. در این رابطه، مخاطب گوینده یا شخصیت را همچون آشنایی واقعی می‌بیند، با او گفت‌وگوی خیالی می‌کند و واکنشش را پیش‌بینی می‌کند، در حالی که طرف رسانه‌ای از این رابطه آگاه نیست و پاسخ متقابل نمی‌دهد. هورتون و وهل این پدیده را در مجری تلویزیونی و ستارهٔ رسانه‌ای تحلیل کردند و آن را محصول ساختار خود رسانه دانستند که صمیمیت را شبیه‌سازی می‌کند. آلن روبین و همکارانش در سال ۱۹۸۵ مقیاس‌ای برای سنجش آن ساختند و نشان دادند که تعامل فرااجتماعی با نیاز به تعامل اجتماعی و تماشای خبر پیوند دارد. پژوهش‌های بعدی میان تعامل فرااجتماعی به‌عنوان رفتار کوتاه‌مدت و رابطهٔ فرااجتماعی به‌عنوان پیوند بلندمدت تفکیک کردند. مدل برای تحلیل مجری خبر، اینفلوئنسر، شخصیت سریال و ارتباط بحرانی به کار می‌رود. نقدهای اصلی به آن، آمیختگی مفهوم تعامل و رابطه، وابستگی به خودگزارشی، فرض یک‌سویگی ساده و کم‌توجهی به تعامل دوسویهٔ شبکه‌های اجتماعی را برجسته می‌کنند.",
        definition="نظریهٔ تعامل فرااجتماعی، رابطهٔ یک‌سویه و صمیمی مخاطب با شخصیت رسانه‌ای را توصیف می‌کند که در آن مخاطب احساس آشنایی و گفت‌وگو دارد اما پاسخ متقابل دریافت نمی‌کند.",
        main_problem="چرا مخاطب با شخصیت‌هایی که هرگز ملاقات نکرده است رابطهٔ صمیمی احساس می‌کند و این رابطه چه اثری بر باور، اعتماد و رفتار او دارد.",
        mechanism="رسانه با نمایش نزدیک، تکرار و خطاب مستقیم، صمیمیت را شبیه‌سازی می‌کند؛ مخاطب با تکمیل این فاصله، رابطه‌ای یک‌سویه می‌سازد که با تکرار مصرف تقویت می‌شود.",
        assumptions=[
            "مخاطب رابطهٔ اجتماعی می‌سازد.",
            "رابطهٔ فرااجتماعی یک‌سویه است.",
            "رسانه صمیمیت را شبیه‌سازی می‌کند.",
            "تکرار مصرف رابطه را تقویت می‌کند.",
            "رابطه بر باور و رفتار اثر دارد.",
        ],
        principles=[
            "صمیمیت شبیه‌سازی‌شده را تشخیص بده.",
            "تعامل را از رابطه جدا کن.",
            "تکرار مواجهه را در نظر بگیر.",
            "خطاب مستقیم را تحلیل کن.",
            "وفاداری مخاطب را با رابطه بسنج.",
            "مرز شخصیت و شخص را روشن کن.",
        ],
        critiques=[
            "تعامل و رابطه را می‌آمیزد.",
            "به خودگزارشی وابسته است.",
            "یک‌سویگی را ساده می‌گیرد.",
            "تعامل دوسویهٔ شبکه‌های اجتماعی را کم می‌بیند.",
            "اثر رفتاری را کم می‌سنجد.",
            "به تفاوت فرهنگی کم می‌پردازد.",
            "به نقش الگوریتم در ساختن رابطهٔ فرااجتماعی کم توجه دارد.",
            "رابطهٔ فرااجتماعی را با دوستی واقعی یکی می‌گیرد.",
            "به پایان رابطه و سوگ هواداران کم می‌پردازد.",
        ],
        critique_text="منتقدان می‌گویند نظریهٔ تعامل فرااجتماعی بینش بنیادی دربارهٔ صمیمیت رسانه‌ای داد اما مفهوم تعامل و رابطه را آمیخت و محیط دوسویهٔ دیجیتال را کم‌بررسی گذاشت؛ با این حال، پایهٔ پژوهش رابطهٔ مخاطب و شخصیت است.",
        applications=[
            "تحلیل مجری خبر.",
            "پژوهش اینفلوئنسر.",
            "مطالعهٔ شخصیت سریال.",
            "طراحی ارتباط بحرانی.",
            "سنجش وفاداری مخاطب.",
            "آموزش سواد رسانه‌ای.",
            "تحلیل تبلیغ با چهرهٔ آشنا.",
            "پژوهش هواداری ورزشی.",
            "تحلیل رابطهٔ مخاطب با پادکستر.",
            "مطالعهٔ سوگ مخاطب پس از مرگ ستاره.",
        ],
        example_text="بیننده هر شب مجری خبر را می‌بیند، به او اعتماد می‌کند و در ذهن با او حرف می‌زند؛ مدل می‌گوید این اعتماد از رابطهٔ واقعی نیامده، از شبیه‌سازی صمیمیت در قاب رسانه آمده است.",
        evolution="هورتون و وهل در سال ۱۹۵۶ پدیده را نام‌گذاری کردند و روبین و همکارانش در سال ۱۹۸۵ آن را سنجیدند؛ پژوهش‌های بعدی، تفکیک تعامل و رابطه و گسترش به اینفلوئنسرها و پلتفرم‌ها را افزودند.",
        key_concepts=["تعامل فرااجتماعی", "رابطهٔ فرااجتماعی", "صمیمیت از راه دور", "شخصیت رسانه‌ای", "یک‌سویگی", "وفاداری"],
        theorists="دانلد هورتون و ریچارد وهل.",
        theorists_text="نظریه در سنت پژوهش ارتباط جمعی و روان‌شناسی مخاطب شکل گرفت.",
        model="رابطهٔ یک‌سویهٔ مخاطب با شخصیت رسانه‌ای به‌عنوان محصول شبیه‌سازی صمیمیت در رسانه.",
        studies=[
            "مقالهٔ سال ۱۹۵۶ پدیده را معرفی کرد.",
            "مطالعهٔ سال ۱۹۸۵ مقیاس سنجش داد.",
            "پژوهش اینفلوئنسر، رابطه را در شبکهٔ اجتماعی سنجید.",
            "مطالعهٔ خبر، اعتماد به مجری را بررسی کرد.",
            "مطالعهٔ طولی، رابطهٔ فرااجتماعی را پیگیری کرد.",
            "پژوهش بحران، نقش چهرهٔ آشنا را سنجید.",
            "مطالعهٔ پلتفرم، رابطه با اینفلوئنسر را تحلیل کرد.",
        ],
    ),
    "MC-537": dict(
        year=1967,
        summary="نظریهٔ بازی در ارتباطات جمعی، که ویلیام استیونسون در سال ۱۹۶۷ ارائه کرد، مصرف رسانه را نه کار و نه انفعال، بلکه بازی می‌داند. در این نظریه، مخاطب برای لذت و نه برای وظیفه رسانه را انتخاب می‌کند و دو نوع ارتباط را از هم جدا می‌کند: ارتباط با لذت که بازی و آزادی می‌آورد و ارتباط با درد که کار و اجبار است. استیونسون با روش‌شناسی کیو و تحلیل ذهنیت، به‌جای شمارش اثر، به معنای تجربهٔ مخاطب پرداخت و نشان داد که خواندن روزنامه و تماشای تلویزیون می‌تواند شکلی از بازی و خودبیانگری باشد. نظریه، انتخاب مخاطب را فعال می‌داند اما برخلاف کاربردهای متأخر، بر لذت و آزادی فرهنگی تأکید می‌کند، نه بر سود و هدف. مدل برای تحلیل سرگرمی، بازی دیجیتال، هواداری و مصرف رسانه‌ای روزمره به کار می‌رود. نقدهای اصلی به آن، مفهوم مبهم بازی، آزمون تجربی محدود، کم‌توجهی به اقتصاد سیاسی و ایدئولوژی رسانه، و دشواری تعمیم به محیط تعاملی امروز را برجسته می‌کنند.",
        definition="نظریهٔ بازی در ارتباطات جمعی، مصرف رسانه را شکلی از بازی و لذت می‌داند که مخاطب آزادانه برای خودبیانگری انتخاب می‌کند و آن را از کار و اجبار جدا می‌کند.",
        main_problem="اگر مصرف رسانه نه کار است و نه صرفاً اثرپذیری، چگونه می‌توان آن را همچون بازی، انتخاب و تجربهٔ لذت‌بخش فهمید.",
        mechanism="مخاطب از میان محتواها آن را برمی‌گزیند که لذت و آزادی می‌دهد؛ بازی، فاصله از اجبار روزمره می‌سازد و تجربهٔ رسانه‌ای را به خودبیانگری بدل می‌کند.",
        assumptions=[
            "مصرف رسانه شکلی از بازی است.",
            "مخاطب فعال و گزینشگر است.",
            "لذت، انگیزهٔ اصلی مصرف است.",
            "ارتباط با لذت و درد تفکیک‌پذیرند.",
            "تجربهٔ ذهنی مخاطب دادهٔ معتبر است.",
        ],
        principles=[
            "مصرف را همچون بازی ببین.",
            "لذت را انگیزهٔ معتبر بدان.",
            "انتخاب مخاطب را جدی بگیر.",
            "تجربهٔ ذهنی را بسنج.",
            "کار و بازی را از هم جدا کن.",
            "به آزادی فرهنگی مخاطب توجه کن.",
        ],
        critiques=[
            "مفهوم بازی مبهم است.",
            "آزمون تجربی آن محدود است.",
            "اقتصاد سیاسی را کم می‌بیند.",
            "ایدئولوژی رسانه را نادیده می‌گیرد.",
            "به محیط تعاملی امروز کم می‌پردازد.",
            "تفاوت طبقاتی در دسترسی را کم می‌بیند.",
            "مرز بازی و اعتیاد رسانه‌ای را روشن نمی‌کند.",
            "به نقش تبلیغ و مصرف‌گرایی کم توجه دارد.",
            "نظریه را بیشتر توصیفی می‌داند تا تبیینی.",
            "به مخاطب غیرغربی و تجربهٔ بومی کم می‌پردازد.",
        ],
        critique_text="منتقدان می‌گویند نظریهٔ بازی مصرف رسانه را از انفعال رهانید اما مفهوم بازی را مبهم گذاشت و قدرت صنعت رسانه را کم‌بررسی کرد؛ با این حال، پیشگام پژوهش لذت و انتخاب مخاطب است.",
        applications=[
            "تحلیل سرگرمی تلویزیونی.",
            "پژوهش بازی دیجیتال.",
            "مطالعهٔ هواداری.",
            "تحلیل مصرف روزمرهٔ رسانه.",
            "آموزش سواد رسانه‌ای.",
            "پژوهش لذت و خشنودی.",
            "طراحی محتوای سرگرمی.",
            "تحلیل فرهنگ عامه.",
            "بررسی لذت در بازی موبایلی.",
            "پژوهش مصرف رسانه در اوقات فراغت.",
            "تحلیل طنز و سرگرمی سیاسی.",
        ],
        example_text="کسی که بعد از کار سریال می‌بیند، نه وظیفه‌ای انجام می‌دهد و نه فقط اثر می‌پذیرد؛ از نگاه استیونسون او بازی می‌کند و از میان محتواها آن را برمی‌گزیند که آزادی و لذت بیشتری بدهد.",
        evolution="استیونسون در سال ۱۹۶۷ نظریه را با روش کیو معرفی کرد؛ پژوهش‌های بعدی، آن را به بازی دیجیتال و فرهنگ طرفداران بردند و در برابر نظریه‌های اثر، بر فعال‌بودن مخاطب تأکید کردند.",
        key_concepts=["بازی", "ارتباط با لذت", "ارتباط با درد", "خودبیانگری", "گزینش مخاطب", "فرهنگ عامه"],
        theorists="ویلیام استیونسون.",
        theorists_text="نظریه در سنت روان‌شناسی ذهنیت و پژوهش مخاطب شکل گرفت.",
        model="مصرف رسانه به‌عنوان بازی، انتخاب آزاد و خودبیانگری لذت‌بخش.",
        studies=[
            "کتاب سال ۱۹۶۷ نظریه را معرفی کرد.",
            "مرور سال ۱۹۷۱ آن را ارزیابی کرد.",
            "پژوهش بازی، لذت تعاملی را بررسی کرد.",
            "مطالعهٔ هواداری، مصرف بازی‌گونه را یافت.",
            "مطالعهٔ کیو، ذهنیت مخاطب سرگرمی را تحلیل کرد.",
            "پژوهش اوقات فراغت، انتخاب لذت‌محور را نشان داد.",
            "پژوهش موبایل، بازی روزمره را تحلیل کرد.",
            "تحلیل پلتفرم، سرگرمی تعاملی را بررسی کرد.",
        ],
    ),
    "MC-557": dict(
        year=1976,
        summary="سندرم جهان خشن، که از برنامهٔ پژوهشی کشت جرج گربنر و لری گراس در دههٔ ۱۹۷۰ بیرون آمد و در مقالهٔ «زندگی با تلویزیون: نمای خشونت» در سال ۱۹۷۶ صورت‌بندی شد، نشان می‌دهد که تماشاگران پرمصرف تلویزیون جهان را خطرناک‌تر از واقعیت می‌بینند. در این مدل، تلویزیون تصویری از خشونت فراگیر و قربانی‌شدن پیاپی می‌سازد و کسانی که بیشتر تماشا می‌کنند، احتمال قربانی‌شدن خود را بالاتر تخمین می‌زنند، به دیگران کمتر اعتماد می‌کنند و سیاست سخت‌گیرانه‌تر می‌طلبند. گربنر و همکارانش در سال ۱۹۸۰ با مفهوم جریان اصلی‌سازی نشان دادند که تماشای سنگین، تفاوت‌های گروه‌های اجتماعی را به سمت جهان‌بینی مشترک و ترسناک هم‌سو می‌کند. مدل سه گام دارد: محتوای خشونت تلویزیونی، مواجههٔ سنگین و شکل‌گیری باور به جهان خشن. در رسانه، مدل برای تحلیل خبر جرم، ترس از جرم، نژاد و سیاست کیفری به کار می‌رود. نقدهای اصلی به آن، اندازهٔ اثر کوچک، احتمال متغیر پنهان، سنجش خام مواجهه، دشواری تفکیک علت و اثر و تکرارپذیری محدود را برجسته می‌کنند.",
        definition="سندرم جهان خشن، باور تماشاگران پرمصرف تلویزیون به خطرناک‌تر بودن جهان از واقعیت را توصیف می‌کند که با کشت ترس، بی‌اعتمادی و تقاضای سیاست سخت‌گیرانه همراه است.",
        main_problem="چرا تماشای زیاد تلویزیون، باور به خطر و بی‌اعتمادی اجتماعی را بالا می‌برد و این باور چه اثری بر ترس از جرم و سیاست عمومی دارد.",
        mechanism="تلویزیون خشونت را فراگیر و قربانی‌شدن را محتمل نشان می‌دهد؛ مواجههٔ سنگین، این تصویر را به باور بدل می‌کند و ترس، بی‌اعتمادی و تقاضای سخت‌گیری را افزایش می‌دهد.",
        assumptions=[
            "تلویزیون روایت مشترک می‌سازد.",
            "مواجههٔ سنگین باور را شکل می‌دهد.",
            "باور به خشونت با ترس پیوند دارد.",
            "جریان اصلی‌سازی رخ می‌دهد.",
            "اثر در بلندمدت انباشته می‌شود.",
        ],
        principles=[
            "میزان مواجهه را بسنج.",
            "باور به خطر را از واقعیت جدا کن.",
            "جریان اصلی‌سازی را بررسی کن.",
            "خشونت خبری را پایش کن.",
            "ترس و سیاست کیفری را پیوند بده.",
            "متغیرهای پنهان را کنترل کن.",
        ],
        critiques=[
            "اندازهٔ اثر آن کوچک است.",
            "متغیر پنهان را کم کنترل می‌کند.",
            "سنجش مواجهه خام است.",
            "تفکیک علت و اثر دشوار است.",
            "تکرارپذیری آن محدود است.",
            "به مصرف انتخابی کم می‌پردازد.",
            "به تغییر محیط رسانه‌ای چندکاناله کم توجه دارد.",
            "نقش خبر شبکه‌های اجتماعی را جدا نمی‌سنجد.",
            "اثر آن بر سیاست کیفری کم مستند است.",
            "به نقش رسانهٔ عمومی در تعدیل ترس کم توجه دارد.",
            "به بافت محلی و تفاوت کشورها کم می‌پردازد.",
        ],
        critique_text="منتقدان می‌گویند سندرم جهان خشن بینش مهمی دربارهٔ ترس رسانه‌ای داد اما اثر آن کوچک و سنجش مواجهه خام بود؛ با این حال، همچنان چارچوب مرجع پژوهش کشت ترس است.",
        applications=[
            "تحلیل خبر جرم.",
            "پژوهش ترس از جرم.",
            "بررسی سیاست کیفری.",
            "مطالعهٔ بازنمایی نژاد.",
            "آموزش سواد خبری.",
            "پژوهش کشت.",
            "تحلیل پوشش بحران.",
            "سیاست‌گذاری رسانه.",
            "پژوهش ترس در محله‌های شهری.",
            "طراحی گزارش جرم بدون تقویت ترس.",
        ],
        example_text="بیننده‌ای که هر شب چند ساعت خبر جرم می‌بیند، محلهٔ خود را خطرناک‌تر از آمار رسمی می‌بیند و به همسایه کمتر اعتماد می‌کند؛ مدل این شکاف میان باور و واقعیت را کشت می‌نامد.",
        evolution="گربنر و گراس در سال ۱۹۷۶ نمای خشونت را معرفی کردند و در سال ۱۹۸۰ جریان اصلی‌سازی را افزودند؛ پژوهش‌های بعدی، مدل را به خبر، نژاد و سیاست کیفری و همچنین نقد روش‌شناختی گستردند.",
        key_concepts=["کشت", "جهان خشن", "ترس از جرم", "جریان اصلی‌سازی", "مواجههٔ سنگین", "بی‌اعتمادی"],
        theorists="جرج گربنر و لری گراس.",
        theorists_text="مدل در سنت پژوهش کشت و تحلیل محتوای تلویزیون شکل گرفت.",
        model="باور به جهان خطرناک به‌عنوان محصول انباشتهٔ مواجههٔ سنگین با خشونت تلویزیونی.",
        studies=[
            "مقالهٔ سال ۱۹۷۶ نمای خشونت را ساخت.",
            "مقالهٔ سال ۱۹۸۰ جریان اصلی‌سازی را نشان داد.",
            "پژوهش ترس، باور به خطر را سنجید.",
            "مطالعهٔ نقدی، اندازهٔ اثر را بازبینی کرد.",
            "مطالعهٔ تطبیقی، جریان اصلی‌سازی را در دو کشور آزمود.",
            "پژوهش خبر، ترس از جرم را با پوشش سنجید.",
            "پژوهش طولی، اثر مواجهه را پیگیری کرد.",
        ],
    ),
}

NAME_FIX = {
    "MC-536": ("تعامل فرااجتماعی (پاراسوشیال)", "Parasocial Interaction", "عنوان پیشین «تعامل فرامرزی» ترجمهٔ نادرست بود و مفهوم هورتون و وهل را نمی‌رساند."),
    "MC-537": ("نظریهٔ بازی در ارتباطات جمعی", "Play Theory of Mass Communication", "عنوان پیشین «بازیگرایی/Gamism» به مفهوم بازیگرایی در بازی‌شناسی اشاره دارد و نه نظریهٔ استیونسون؛ عنوان به اثر ۱۹۶۷ اصلاح شد."),
}
YEAR_FIX = {
    "MC-711": "بدنهٔ کارت قالب عمومی فرهنگ دیجیتال و بازی بود و به اعتیاد اینترنتی ربطی نداشت؛ محتوا بر پایهٔ یانگ ۱۹۹۸ و گریفیتس ۲۰۰۵ بازنویسی شد.",
    "MC-536": "بدنهٔ کارت تنها یک جملهٔ ناقص داشت و ترجمهٔ عنوان نادرست بود؛ محتوا بر پایهٔ هورتون و وهل ۱۹۵۶ و روبین و همکاران ۱۹۸۵ بازنویسی شد.",
    "MC-537": "بدنهٔ کارت قالب عمومی بازی و فرهنگ دیجیتال بود و نام نظریه‌پرداز هم نیمه‌لاتین مانده بود؛ محتوا بر پایهٔ استیونسون ۱۹۶۷ بازنویسی شد.",
    "MC-557": "کارت سال نداشت و بدنهٔ آن کوتاه بود؛ سال ۱۹۷۶ و پژوهش گربنر و گراس مبنا قرار گرفت.",
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
                                       "verified": n_verified, "batch": 159}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH159 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
