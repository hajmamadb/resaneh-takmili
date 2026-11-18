# -*- coding: utf-8 -*-
"""Batch 142 (MODEL): full documentation for MC-350, MC-367, MC-368, MC-421."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch142-model-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch142_model.json"

S = {
    "MC-350": [
        dict(kind="BOOK",
             title_en="Ideology: A Multidisciplinary Approach",
             title_fa="ایدئولوژی: رویکردی میان‌رشته‌ای",
             authors="van Dijk, T. A.", year=1998,
             publisher="SAGE Publications",
             doi=None,
             url="https://sk.sagepub.com/dict/mono/preview/ideology.pdf",
             language="en", isbn=None,
             citation="van Dijk, T. A. (1998). Ideology: A Multidisciplinary Approach. London: SAGE Publications.",
             locator="book", locator_type="SECTION",
             supports="sociocognitive framework linking discourse, social cognition and power", verified=True),
        dict(kind="BOOK",
             title_en="Discourse and Context: A Sociocognitive Approach",
             title_fa="گفتمان و بافت: رویکردی شناختی-اجتماعی",
             authors="van Dijk, T. A.", year=2008,
             publisher="Cambridge University Press",
             doi="10.1017/CBO9780511481499",
             url="https://www.cambridge.org/core/books/discourse-and-context/CFF89959D40865995A8BE28F576D8CC9",
             language="en", isbn=None,
             citation="van Dijk, T. A. (2008). Discourse and Context: A Sociocognitive Approach. Cambridge: Cambridge University Press.",
             locator="book", locator_type="SECTION",
             supports="context models and mental models mediating discourse and society", verified=True),
    ],
    "MC-367": [
        dict(kind="BOOK",
             title_en="The Life of P. T. Barnum, Written by Himself",
             title_fa="زندگی فینیاس تیلور بارنوم، به قلم خودش",
             authors="Barnum, P. T.", year=1855,
             publisher="Redfield",
             doi=None,
             url="http://archive.org/stream/lifeofptbarnum00barnuoft",
             language="en", isbn=None,
             citation="Barnum, P. T. (1855). The Life of P. T. Barnum, Written by Himself. New York: Redfield.",
             locator="book", locator_type="SECTION",
             supports="primary account of Barnum's publicity stunts and sensational promotion", verified=True),
        dict(kind="BOOK",
             title_en="Managing Public Relations",
             title_fa="مدیریت روابط عمومی",
             authors="Grunig, J. E.; Hunt, T.", year=1984,
             publisher="Holt, Rinehart and Winston",
             doi=None,
             url="https://archive.org/details/managingpublicre0000unse",
             language="en", isbn=None,
             citation="Grunig, J. E., & Hunt, T. (1984). Managing Public Relations. New York: Holt, Rinehart and Winston.",
             locator="book", locator_type="SECTION",
             supports="press agentry/publicity model as the first of four historical PR models", verified=True),
    ],
    "MC-368": [
        dict(kind="WEBSITE",
             title_en="Ivy Lee's Declaration of Principles (1906)",
             title_fa="اعلامیهٔ اصول آیوی لی (۱۹۰۶)",
             authors="PR Academy", year=1906,
             publisher="PR Academy",
             doi=None,
             url="https://pracademy.co.uk/insights/ivy-lee-and-the-origins-of-the-press-release/",
             language="en", isbn=None,
             citation="PR Academy. (2014). Ivy Lee and the origins of the press release. Retrieved from PR Academy.",
             locator="article", locator_type="SECTION",
             supports="text and context of Lee's declaration promising accurate, prompt information", verified=True),
        dict(kind="BOOK",
             title_en="Managing Public Relations",
             title_fa="مدیریت روابط عمومی",
             authors="Grunig, J. E.; Hunt, T.", year=1984,
             publisher="Holt, Rinehart and Winston",
             doi=None,
             url="https://archive.org/details/managingpublicre0000unse",
             language="en", isbn=None,
             citation="Grunig, J. E., & Hunt, T. (1984). Managing Public Relations. New York: Holt, Rinehart and Winston.",
             locator="book", locator_type="SECTION",
             supports="public information model as one of four historical PR models", verified=True),
    ],
    "MC-421": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Robotic Reporter: Automated Journalism and the Redefinition of Labor, Compositional Forms, and Journalistic Authority",
             title_fa="خبرنگار رباتیک: روزنامه‌نگاری خودکار و بازتعریف کار، فرم‌های نگارشی و اقتدار روزنامه‌نگارانه",
             authors="Carlson, M.", year=2015,
             publisher="Digital Journalism",
             doi="10.1080/21670811.2014.976412",
             url="https://doi.org/10.1080/21670811.2014.976412",
             language="en", isbn=None,
             citation="Carlson, M. (2015). The robotic reporter: Automated journalism and the redefinition of labor, compositional forms, and journalistic authority. Digital Journalism, 3(3), 416-431.",
             locator="3(3):416-431", locator_type="page_range",
             supports="automated news production and its implications for labor and authority", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Automated Journalism 2.0: Event-driven Narratives",
             title_fa="روزنامه‌نگاری خودکار ۲: روایت‌های رویدادمحور",
             authors="Caswell, D.; Dörr, K.", year=2018,
             publisher="Journalism Practice",
             doi="10.1080/17512786.2017.1320773",
             url="https://www.tandfonline.com/doi/abs/10.1080/17512786.2017.1320773",
             language="en", isbn=None,
             citation="Caswell, D., & Dörr, K. (2018). Automated journalism 2.0: Event-driven narratives. Journalism Practice, 12(4), 477-496.",
             locator="12(4):477-496", locator_type="page_range",
             supports="data-driven and event-driven narrative generation in newsrooms", verified=True),
    ],
}

ENRICH = {
    "MC-350": dict(
        year=1998,
        summary="رویکرد شناختی-اجتماعی در تحلیل گفتمان، چارچوبی انتقادی است که تئون ون دایک در کتاب ایدئولوژی در سال ۱۹۹۸ و سپس در گفتمان و بافت در سال ۲۰۰۸ صورت‌بندی کرد. ادعای مرکزی این است که میان ساختارهای گفتمان و ساختارهای اجتماعی، حلقهٔ واسطی به نام شناخت اجتماعی قرار دارد. شناخت اجتماعی شامل بازنمایی‌های مشترک گروهی مانند دانش، نگرش‌ها و ایدئولوژی‌هاست که در حافظهٔ جمعی گروه جای می‌گیرد. ون دایک نشان می‌دهد نخبگان با تولید گفتمان، این بازنمایی‌ها را بازتولید می‌کنند و قدرت خود را حفظ می‌سازند. ابزار اصلی تحلیل، مربع ایدئولوژیک است: برجسته‌سازی ویژگی‌های مثبت گروه خودی و ویژگی‌های منفی گروه دیگران. او همچنین میان مدل‌های ذهنی رویداد و مدل‌های بافت تمایز می‌گذارد: مدل ذهنی، بازنمایی شخصی یک رویداد است و مدل بافت، بازنمایی شخصی موقعیت ارتباطی. این دو مدل توضیح می‌دهند چگونه ساختار اجتماعی به انتخاب واژه، ساختار نحوی و سازمان متن تبدیل می‌شود. چارچوب ون دایک، تحلیل گفتمان انتقادی خبر، نژادپرستی گفتمانی و تبلیغ سیاسی را عمیقاً تحت تأثیر قرار داد. نقدهای اصلی به آن، دشواری مشاهده و سنجش مستقیم شناخت اجتماعی، خطر استدلال دوری میان متن و ایدئولوژی، تمرکز بر نخبگان و کم‌توجهی به مقاومت مخاطب، و وابستگی تفسیر به تحلیل‌گر را برجسته می‌کنند.",
        definition="رویکرد شناختی-اجتماعی، گفتمان را میانجی‌شده با بازنمایی‌های شناختی مشترک گروهی می‌داند و بازتولید قدرت و ایدئولوژی را از راه تحلیل ساختارهای متن و شناخت اجتماعی توضیح می‌دهد.",
        main_problem="چگونه گفتمان نخبگان، ایدئولوژی و مناسبات قدرت را در ذهن اعضای جامعه بازتولید می‌کند و چه سازوکارهای شناختی این پیوند را ممکن می‌سازند.",
        mechanism="گفتمان با انتخاب واژه، ساختار و قطب‌بندی، مدل‌های ذهنی مخاطب را شکل می‌دهد؛ این مدل‌ها با بازنمایی‌های اجتماعی مشترک گروه پیوند می‌خورند و ایدئولوژی را تثبیت می‌کنند. مربع ایدئولوژیک، خودی مثبت و دیگری منفی را برجسته می‌سازد.",
        assumptions=[
            "میان گفتمان و جامعه، شناخت اجتماعی واسطه است.",
            "بازنمایی‌های گروهی در حافظهٔ جمعی ذخیره می‌شوند.",
            "نخبگان در تولید گفتمان قدرت بیشتری دارند.",
            "مدل‌های ذهنی و بافتی، تولید و تفسیر متن را هدایت می‌کنند.",
            "قطب‌بندی خودی و دیگری در متن قابل شناسایی است.",
        ],
        principles=[
            "گفتمان را با واسطهٔ شناخت اجتماعی تحلیل کن.",
            "مربع ایدئولوژیک را در متن جستجو کن.",
            "مدل ذهنی رویداد و مدل بافت را از هم جدا کن.",
            "نقش نخبگان در تولید گفتمان را بسنج.",
            "ساختار واژگانی و نحوی را به ایدئولوژی پیوند بده.",
            "تفسیر را با شواهد متنی مستند کن.",
        ],
        critiques=[
            "سنجش مستقیم شناخت اجتماعی دشوار است.",
            "خطر استدلال دوری میان متن و ایدئولوژی وجود دارد.",
            "تحلیل بر نخبگان متمرکز و مقاومت مخاطب کم‌بررسی است.",
            "تفسیر متن به داوری تحلیل‌گر وابسته است.",
            "پیوند علّی شناخت و ساختار اجتماعی به‌سختی آزمون‌پذیر است.",
        ],
        critique_text="منتقدان می‌گویند رویکرد ون دایک پیوندی نظری میان متن و قدرت برقرار کرد اما شناخت اجتماعی را نمی‌توان مستقیم مشاهده کرد و خطر دور استدلالی وجود دارد؛ با این حال، چارچوب مرجع تحلیل گفتمان انتقادی و رسانه است.",
        applications=[
            "تحلیل گفتمان خبر و بازنمایی گروه‌ها.",
            "پژوهش نژادپرستی و قطب‌بندی گفتمانی.",
            "تحلیل تبلیغ سیاسی و ایدئولوژی رسانه.",
            "آموزش تحلیل گفتمان انتقادی.",
            "مطالعهٔ گفتمان سازمانی و قدرت.",
        ],
        example_text="در پوشش خبری یک اعتراض، انتخاب واژهٔ «اغتشاشگر» به‌جای «معترض»، قطب‌بندی خودی و دیگری را می‌سازد و مدل ذهنی مخاطب را به سمت تفسیر منفی هدایت می‌کند؛ همین انتخاب واژگانی، ایدئولوژی پنهان متن را آشکار می‌سازد.",
        evolution="چارچوب در کتاب سال ۱۹۹۸ ون دایک شکل گرفت و در کتاب سال ۲۰۰۸ با مفهوم مدل بافت گسترش یافت. پس از آن، به یکی از رویکردهای اصلی تحلیل گفتمان انتقادی و پژوهش رسانه تبدیل شد و بر مطالعات نژاد، مهاجرت و تبلیغ اثر گذاشت.",
        key_concepts=["شناخت اجتماعی", "مربع ایدئولوژیک", "مدل ذهنی", "مدل بافت", "حافظهٔ جمعی", "بازتولید قدرت", "قطب‌بندی گفتمانی"],
        theorists="تئون ون دایک.",
        theorists_text="رویکرد در سنت تحلیل گفتمان انتقادی و روان‌شناسی اجتماعی شکل گرفت.",
        model="زنجیرهٔ گفتمان، شناخت اجتماعی و ساختار اجتماعی که با مدل‌های ذهنی و بافتی، ایدئولوژی و قدرت را بازتولید می‌کند.",
        studies=[
            "کتاب سال ۱۹۹۸ چارچوب شناختی-اجتماعی ایدئولوژی را معرفی کرد.",
            "کتاب سال ۲۰۰۸ مفهوم مدل بافت را گسترش داد.",
            "پژوهش‌های رسانه، قطب‌بندی خبری را با مربع ایدئولوژیک تحلیل کردند.",
            "مطالعات نژاد و مهاجرت، بازنمایی گفتمانی را با این رویکرد بررسی کردند.",
        ],
    ),
    "MC-367": dict(
        year=1855,
        summary="مدل تبلیغ‌گری مطبوعاتی، که در تاریخ روابط عمومی با نام فینیاس تی. بارنوم و سدهٔ نوزدهم پیوند دارد، الگویی یک‌سویه از ارتباط تجاری است که هدف اصلی آن جلب توجه و ایجاد هیجان است، نه انتقال کامل حقیقت. بارنوم با نمایش‌های عجایب، داستان‌های اغراق‌شده و رویدادهای ساختگی، الگویی از تبلیغ نمایشی ساخت که در آن مرز میان سرگرمی، فریب و تبلیغ مبهم می‌شد. در این مدل، سازمان پیام را به رسانه می‌فرستد و مخاطب تنها مصرف‌کنندهٔ تبلیغ است؛ بازخورد و گفت‌وگو جایی ندارد. معیار موفقیت، میزان پوشش خبری و جلب توجه عمومی است، نه دقت یا شفافیت. گرونیگ و هانت بعدها این الگو را نخستین مدل از چهار مدل تاریخی روابط عمومی نامیدند و آن را در برابر مدل اطلاع‌رسانی عمومی، مدل دوسویهٔ نامتقارن و مدل دوسویهٔ متقارن قرار دادند. این مدل، ریشهٔ تاریخی رویدادسازی رسانه‌ای، تیترهای جنجالی و کمپین‌های هیجانی است و در نقد اخلاق روابط عمومی جای مهمی دارد. نقدهای اصلی به آن، بی‌اعتنایی به حقیقت و فریب عمومی، تبدیل مخاطب به ابزار، ایجاد بی‌اعتمادی به رسانه و روابط عمومی، و ناسازگاری با اصول پاسخ‌گویی و شفافیت را برجسته می‌کنند.",
        definition="مدل تبلیغ‌گری مطبوعاتی، الگویی یک‌سویه از ارتباط سازمانی است که با جنجال، اغراق و رویدادسازی، توجه رسانه و عموم را جلب می‌کند و به انتقال کامل حقیقت متعهد نیست.",
        main_problem="سازمان چگونه می‌تواند با کمترین هزینه و بدون تعهد به شفافیت کامل، توجه رسانه و عموم را به خود جلب کند و در بازار رقابتی دیده شود.",
        mechanism="سازمان رویداد، داستان یا نمایشی جنجالی می‌سازد و آن را به رسانه عرضه می‌کند؛ ارزش خبری جنجال، پوشش رسانه‌ای را افزایش می‌دهد و توجه عمومی را جلب می‌کند. معیار موفقیت، حجم پوشش است نه دقت پیام.",
        assumptions=[
            "توجه عمومی، منبع اصلی ارزش سازمان است.",
            "جنجال و اغراق، پوشش رسانه‌ای را افزایش می‌دهد.",
            "مخاطب مصرف‌کنندهٔ منفعل تبلیغ است.",
            "بازخورد و گفت‌وگو ضروری نیست.",
            "معیار موفقیت، حجم پوشش خبری است.",
        ],
        principles=[
            "رویداد را برای پوشش رسانه‌ای طراحی کن.",
            "عنصر غافلگیری و نمایش را برجسته کن.",
            "پیام را ساده و هیجان‌انگیز بساز.",
            "رسانه را کانال یک‌سویهٔ تبلیغ بدان.",
            "موفقیت را با حجم پوشش بسنج.",
            "مرز اخلاقی تبلیغ و فریب را آگاهانه نقد کن.",
            "ارزش خبری رویداد را پیش از انتشار بسنج.",
        ],
        critiques=[
            "به حقیقت و منافع عمومی بی‌اعتناست.",
            "مخاطب را به ابزار تبلیغ تبدیل می‌کند.",
            "بی‌اعتمادی به رسانه و روابط عمومی می‌سازد.",
            "با پاسخ‌گویی و شفافیت ناسازگار است.",
            "اثر بلندمدت آن بر اعتبار سازمان منفی است.",
            "معیار توجه، جای معیار اعتماد را می‌گیرد.",
        ],
        critique_text="منتقدان می‌گویند مدل تبلیغ‌گری مطبوعاتی با اولویت‌دادن به توجه بر حقیقت، فریب و بی‌اعتمادی عمومی را نهادینه می‌کند و در بلندمدت به اعتبار سازمان آسیب می‌زند؛ با این حال، نقطهٔ آغاز تاریخی بحث اخلاق روابط عمومی است.",
        applications=[
            "تحلیل تاریخی روابط عمومی و تبلیغات.",
            "مطالعهٔ رویدادسازی و جنجال رسانه‌ای.",
            "نقد اخلاقی کمپین‌های هیجانی.",
            "آموزش مرز تبلیغ و فریب.",
            "مقایسهٔ چهار مدل تاریخی روابط عمومی.",
            "مطالعهٔ تاریخ نمایش و سرگرمی عامه.",
        ],
        example_text="تبلیغ یک نمایش عجایب با ادعای کشف موجودی ناشناخته، پیش از آنکه تماشاگر وارد شود توجه رسانه‌ها را جلب می‌کند؛ درستی ادعا کمتر از حجم تماشاگر اهمیت دارد. همین منطق، هستهٔ مدل تبلیغ‌گری مطبوعاتی است.",
        evolution="این الگو در سدهٔ نوزدهم با فعالیت بارنوم شکل گرفت و در اوایل قرن بیستم به‌عنوان مدل نخست روابط عمومی در پژوهش گرونیگ و هانت دسته‌بندی شد. پس از آن، به نمونهٔ هشداردهنده در آموزش اخلاق روابط عمومی تبدیل شد.",
        key_concepts=["تبلیغ‌گری مطبوعاتی", "جنجال", "رویدادسازی", "اغراق نمایشی", "ارتباط یک‌سویه", "پوشش رسانه‌ای"],
        theorists="فینیاس تی. بارنوم.",
        theorists_text="الگو در سنت نمایش‌های عمومی و تبلیغ تجاری سدهٔ نوزدهم شکل گرفت.",
        model="ارتباط یک‌سویهٔ سازمان به رسانه و عموم که با جنجال و اغراق، توجه را جلب می‌کند و به حقیقت کامل متعهد نیست.",
        studies=[
            "خودزندگی‌نامهٔ سال ۱۸۵۵ بارنوم شیوه‌های تبلیغ او را مستند کرد.",
            "پژوهش سال ۱۹۸۴ الگو را نخستین مدل روابط عمومی نامید.",
            "مطالعات اخلاق روابط عمومی، پیامدهای فریب را بررسی کردند.",
            "پژوهش رسانه، منطق جنجال و رویدادسازی را تحلیل کرد.",
        ],
    ),
    "MC-368": dict(
        year=1906,
        summary="مدل انتشار صادقانه اطلاعات، که با آیوی لی و اعلامیهٔ اصول او در سال ۱۹۰۶ پیوند دارد، الگویی یک‌سویه اما حقیقت‌محور از روابط عمومی است. ادعای مرکزی این است که سازمان باید اطلاعات درست، دقیق و به‌موقع را در اختیار رسانه و عموم بگذارد و به‌جای دستکاری یا پنهان‌کاری، شفافیت را مبنای اعتماد قرار دهد. لی در اعلامیهٔ خود اعلام کرد که دفتر او برای تأمین خبر به رسانه‌ها باز است و اطلاعات دربارهٔ موضوعات مورد علاقهٔ عمومی را بدون هزینه در اختیار می‌گذارد. این مدل، گام مهمی از تبلیغ‌گری نمایشی به اطلاع‌رسانی حرفه‌ای بود و زمینهٔ شکل‌گیری بیانیهٔ مطبوعاتی و روابط عمومی سازمانی مدرن را فراهم کرد. با این حال، ارتباط همچنان یک‌سویه است: سازمان پیام را منتشر می‌کند و بازخورد ساختارمند یا مذاکرهٔ معنادار با مخاطب پیش‌بینی نشده است. گرونیگ و هانت این الگو را مدل اطلاع‌رسانی عمومی نامیدند و آن را میان مدل تبلیغ‌گری و مدل‌های دوسویه جای دادند. نقدهای اصلی به آن، یک‌سویه‌بودن و نبود گفت‌وگو، انتخاب گزینشی اطلاعات مطلوب سازمان، فرض بی‌طرفی سازمان، و کاربرد آن به‌عنوان ابزار مدیریت شهرت به‌جای پاسخ‌گویی واقعی را برجسته می‌کنند.",
        definition="مدل انتشار صادقانه اطلاعات، الگویی یک‌سویه از روابط عمومی است که سازمان را موظف به انتشار اطلاعات درست و شفاف برای رسانه و عموم می‌داند، بدون آنکه بازخورد یا مذاکرهٔ دوسویه پیش‌بینی کند.",
        main_problem="سازمان چگونه می‌تواند با انتشار اطلاعات درست و به‌موقع، اعتماد رسانه و عموم را جلب کند و از بدنامی ناشی از پنهان‌کاری بپرهیزد.",
        mechanism="سازمان اطلاعات دقیق را جمع‌آوری و در قالب بیانیه یا خبر منتشر می‌کند؛ رسانه آن را بازنشر می‌دهد و عموم بر پایهٔ شفافیت، اعتماد می‌سازد. ارتباط در این مدل جریان یک‌سویه از سازمان به مخاطب است.",
        assumptions=[
            "انتشار اطلاعات درست، اعتماد می‌سازد.",
            "رسانه، کانال انتقال اطلاعات سازمان است.",
            "شفافیت جای دستکاری را می‌گیرد.",
            "سازمان می‌تواند اطلاعات را بی‌طرفانه منتشر کند.",
            "بازخورد ساختارمند ضروری نیست.",
        ],
        principles=[
            "اطلاعات درست و به‌موقع را منتشر کن.",
            "دسترسی رسانه به خبر را تسهیل کن.",
            "پنهان‌کاری و دستکاری را کنار بگذار.",
            "شفافیت را مبنای اعتماد قرار بده.",
            "بیانیهٔ خبری را ابزار انتقال دقیق اطلاعات بدان.",
            "محدودیت یک‌سویه‌بودن مدل را بازشناس.",
            "زمان‌بندی انتشار را برای پیشگیری از شایعه تنظیم کن.",
        ],
        critiques=[
            "ارتباط را یک‌سویه نگه می‌دارد.",
            "گفت‌وگو و بازخورد ساختارمند ندارد.",
            "انتشار اطلاعات را گزینشی و به نفع سازمان می‌کند.",
            "بی‌طرفی سازمان را بیش از واقع فرض می‌گیرد.",
            "می‌تواند به ابزار مدیریت شهرت بدل شود.",
            "پاسخ‌گویی را به انتشار بیانیه فرو می‌کاهد.",
        ],
        critique_text="منتقدان می‌گویند مدل انتشار صادقانه گامی اخلاقی از تبلیغ‌گری به اطلاع‌رسانی بود اما همچنان یک‌سویه است و سازمان می‌تواند با گزینش اطلاعات، تصویری مطلوب از خود بسازد؛ با این حال، پایهٔ روابط عمومی حرفه‌ای و شفافیت سازمانی شد.",
        applications=[
            "تدوین سیاست شفافیت سازمانی.",
            "آموزش نگارش بیانیهٔ خبری.",
            "مدیریت بحران با اطلاع‌رسانی سریع.",
            "تحلیل تاریخی روابط عمومی.",
            "مقایسهٔ مدل‌های یک‌سویه و دوسویه.",
            "طراحی خط‌مشی انتشار اطلاعات در سازمان.",
        ],
        example_text="شرکتی که پس از یک نقص فنی، بی‌درنگ اطلاعات دقیق دربارهٔ علت، دامنه و اقدامات جبرانی منتشر می‌کند، با شفافیت اعتماد عمومی را حفظ می‌کند؛ اما اگر همان اطلاعات را گزینشی و بدون پذیرش مسئولیت منتشر کند، مدل به ابزار مدیریت شهرت فرو می‌کاهد.",
        evolution="مدل در سال ۱۹۰۶ با اعلامیهٔ اصول آیوی لی شکل گرفت و در قرن بیستم به یکی از چهار مدل تاریخی روابط عمومی تبدیل شد. با ظهور روابط عمومی دوسویه، جایگاه آن به‌عنوان حداقل اخلاقی شفافیت تثبیت شد.",
        key_concepts=["اطلاع‌رسانی عمومی", "اعلامیهٔ اصول", "شفافیت", "بیانیهٔ خبری", "اعتماد", "ارتباط یک‌سویه"],
        theorists="آیوی لی.",
        theorists_text="مدل در سنت روابط عمومی سازمانی و اطلاع‌رسانی به رسانه شکل گرفت.",
        model="جریان یک‌سویهٔ اطلاعات درست و شفاف از سازمان به رسانه و عموم که اعتماد می‌سازد اما بازخورد ساختارمند ندارد.",
        studies=[
            "اعلامیهٔ سال ۱۹۰۶ اصول اطلاع‌رسانی شفاف را بیان کرد.",
            "پژوهش سال ۱۹۸۴ آن را مدل اطلاع‌رسانی عمومی نامید.",
            "مطالعات بحران، شفافیت سریع را عامل حفظ اعتماد یافتند.",
            "ادبیات روابط عمومی، محدودیت یک‌سویه‌بودن را نقد کرد.",
            "مطالعات موردی، اعلامیه را در بستر تاریخی تحلیل کردند.",
        ],
    ),
    "MC-421": dict(
        year=2015,
        summary="روزنامه‌نگاری خودکار و الگوریتمی، حوزه‌ای در مطالعات روزنامه‌نگاری دیجیتال است که تولید خبر توسط سامانه‌های نرم‌افزاری و الگوریتم‌ها را تحلیل می‌کند و متیاس کاستر و باب فرانکلین در پژوهش‌های خود آن را صورت‌بندی کردند. ادعای مرکزی این است که بخشی از گزارش‌های خبری، به‌ویژه در ورزش، بازار مالی، نتایج انتخاباتی و رویدادهای داده‌محور، می‌تواند بدون نویسندهٔ انسانی و بر پایهٔ الگوهای از پیش تعیین‌شده و دادهٔ ساختاریافته تولید شود. سامانه با دریافت داده، رویداد را تشخیص می‌دهد، قالب خبری مناسب را برمی‌گزیند و متن را با تولید زبان طبیعی می‌سازد. مزیت‌های اعلام‌شده شامل سرعت، مقیاس، کاهش خطای انسانی و آزادکردن زمان خبرنگار برای تحلیل عمیق‌تر است. با این حال، پرسش‌های مهمی دربارهٔ نویسندگی، مسئولیت حقوقی، اقتدار روزنامه‌نگارانه، شفافیت الگوریتم، سوگیری دادهٔ ورودی و یکسان‌سازی سبک خبری مطرح می‌شود. پژوهش‌های بعدی، نسل دوم این سامانه‌ها را با روایت‌های رویدادمحور و توان تولید داستان‌های پیچیده‌تر توصیف کردند. نقدهای اصلی به این حوزه، خطر جبرگرایی فناورانه، نادیده‌گرفتن انتخاب‌های اجتماعی و اقتصادی طراحی، ناهمگنی مفهوم الگوریتم، و کم‌توجهی به پیامدهای کار و اشتغال خبرنگاران را برجسته می‌کنند.",
        definition="روزنامه‌نگاری خودکار، تولید خبر توسط سامانه‌های نرم‌افزاری و الگوریتمی بر پایهٔ دادهٔ ساختاریافته و قالب‌های از پیش تعیین‌شده است که با دخالت محدود یا بدون دخالت نویسندهٔ انسانی انجام می‌شود.",
        main_problem="آیا و چگونه می‌توان تولید خبر را به سامانه‌های خودکار سپرد، و این سپردن چه پیامدهایی برای کیفیت، اقتدار، کار و مسئولیت روزنامه‌نگاری دارد.",
        mechanism="سامانه دادهٔ ساختاریافته را دریافت می‌کند، رویداد و الگوی خبری متناظر را تشخیص می‌دهد، قالب نگارشی را برمی‌گزیند و با تولید زبان طبیعی متن خبری می‌سازد؛ سپس متن برای انتشار یا بازبینی انسانی آماده می‌شود.",
        assumptions=[
            "بخشی از خبر را می‌توان با داده و قالب تولید کرد.",
            "دادهٔ ساختاریافته، ورودی قابل اتکاست.",
            "سرعت و مقیاس، ارزش خبری می‌سازند.",
            "بازبینی انسانی می‌تواند کیفیت را تضمین کند.",
            "الگوریتم در انتخاب قالب، بی‌طرف است.",
        ],
        principles=[
            "دامنهٔ مناسب خودکارسازی را مشخص کن.",
            "کیفیت دادهٔ ورودی را تضمین کن.",
            "قالب‌های خبری را شفاف و قابل بازبینی نگه دار.",
            "نقش بازبینی انسانی را در زنجیره حفظ کن.",
            "مسئولیت حقوقی و اخلاقی انتشار را تعیین کن.",
            "سوگیری داده و یکسان‌سازی سبک را بسنج.",
        ],
        critiques=[
            "خطر جبرگرایی فناورانه در تحلیل وجود دارد.",
            "انتخاب‌های اجتماعی و اقتصادی طراحی پنهان می‌ماند.",
            "مفهوم الگوریتم و خودکارسازی ناهمگن است.",
            "پیامدهای اشتغال و کار خبرنگاران کم‌بررسی است.",
            "شفافیت و مسئولیت سامانه‌های تجاری محدود است.",
        ],
        critique_text="منتقدان می‌گویند پژوهش روزنامه‌نگاری خودکار گاه فناوری را عامل تعیین‌کننده می‌داند و انتخاب‌های انسانی نهفته در طراحی و داده را نادیده می‌گیرد؛ با این حال، پرسش‌های مهمی دربارهٔ اقتدار، کار و مسئولیت خبری گشود.",
        applications=[
            "تولید گزارش‌های ورزشی و مالی.",
            "پوشش سریع نتایج انتخاباتی و داده‌های عمومی.",
            "طراحی گردش‌کار خبری داده‌محور.",
            "آموزش سواد الگوریتمی خبرنگاران.",
            "سیاست‌گذاری شفافیت و مسئولیت در انتشار خودکار.",
        ],
        example_text="یک خبرگزاری پس از پایان مسابقه، دادهٔ آمار بازی را به سامانه می‌دهد و سامانه در چند ثانیه گزارش نتیجه را با قالب ورزشی منتشر می‌کند؛ خبرنگار به‌جای نگارش نتیجه، بر تحلیل تاکتیکی تمرکز می‌کند. این تقسیم کار، نمونهٔ روزنامه‌نگاری خودکار است.",
        evolution="این حوزه در دههٔ ۲۰۱۰ با انتشار گزارش‌های خودکار در خبرگزاری‌ها شکل گرفت. پژوهش سال ۲۰۱۵ کارل‌سون، بازتعریف کار و اقتدار روزنامه‌نگاری را تحلیل کرد و پژوهش سال ۲۰۱۸ کازول و دور، نسل دوم روایت‌های رویدادمحور را توصیف کرد. در دههٔ ۲۰۲۰ با مدل‌های زبانی بزرگ، پرسش‌های تازه‌ای دربارهٔ کیفیت و مسئولیت مطرح شد.",
        key_concepts=["تولید زبان طبیعی", "دادهٔ ساختاریافته", "قالب خبری", "اقتدار روزنامه‌نگارانه", "الگوریتم خبری", "بازبینی انسانی", "شفافیت الگوریتم"],
        theorists="ماتیاس کاستر و باب فرانکلین.",
        theorists_text="حوزه در سنت مطالعات روزنامه‌نگاری دیجیتال و پژوهش تولید خبر شکل گرفت.",
        model="زنجیرهٔ داده، تشخیص رویداد، انتخاب قالب و تولید متن که خبر را با دخالت محدود انسانی می‌سازد و پرسش اقتدار و مسئولیت را پیش می‌آورد.",
        studies=[
            "پژوهش سال ۲۰۱۵ کارل‌سون، کار و اقتدار خبری را بازتعریف کرد.",
            "پژوهش سال ۲۰۱۸ کازول و دور، روایت رویدادمحور را توصیف کرد.",
            "مرورهای نظام‌مند، گسترهٔ پژوهش خودکارسازی خبر را نگاشت کردند.",
            "مطالعات کیفیت، خوانش مخاطب از خبر خودکار را سنجیدند.",
        ],
    ),
}

NAME_FIX = {"MC-367": ("مدل تبلیغ‌گری مطبوعاتی (بارنوم)", "Press Agentry (Publicity) Model", "عنوان پیشین «مدل مطبوعاتی و اغراق نمایشی» نویسه‌گردانی نادرست و نامفهوم بود؛ مفهوم کارت همان مدل تبلیغ‌گری مطبوعاتی بارنوم در دسته‌بندی چهارگانهٔ روابط عمومی است.")}
YEAR_FIX = {"MC-367": "سال دقیق پیدایش مدل در کارت ثبت نشده بود؛ ۱۸۵۵ سال انتشار خودزندگی‌نامهٔ بارنوم به‌عنوان منبع اصلی دورهٔ شکل‌گیری این الگو ثبت شده است."}

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
                                       "verified": n_verified, "batch": 142}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH142 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
