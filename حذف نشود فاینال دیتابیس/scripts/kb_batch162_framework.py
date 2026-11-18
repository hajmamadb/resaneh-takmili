# -*- coding: utf-8 -*-
"""Batch 162 (HYPOTHESIS): MC-011 knowledge gap, MC-466 limited effects, MC-551 multi-stage flow, MC-552 single-stage flow."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch162-hypothesis-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch162_hypothesis.json"

S = {
    "MC-011": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Mass Media Flow and Differential Growth in Knowledge",
             title_fa="جریان رسانه‌های جمعی و رشد افتراقی دانش",
             authors="Tichenor, P. J.; Donohue, G. A.; Olien, C. N.", year=1970,
             publisher="Public Opinion Quarterly",
             doi="10.1086/267786",
             url="https://academic.oup.com/poq/article-abstract/34/2/159/1843590",
             language="en", isbn=None,
             citation="Tichenor, P. J., Donohue, G. A., & Olien, C. N. (1970). Mass media flow and differential growth in knowledge. Public Opinion Quarterly, 34(2), 159-170.",
             locator="34(2):159-170", locator_type="page_range",
             supports="original statement of the knowledge gap hypothesis", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="A Meta-Analysis of the Knowledge Gap Hypothesis",
             title_fa="فراتحلیلی از فرضیهٔ شکاف دانش",
             authors="Lind, F.; Boomgaarden, H. G.", year=2019,
             publisher="Annals of the International Communication Association",
             doi="10.1080/23808985.2019.1614475",
             url="https://www.tandfonline.com/doi/full/10.1080/23808985.2019.1614475",
             language="en", isbn=None,
             citation="Lind, F., & Boomgaarden, H. G. (2019). A meta-analysis of the knowledge gap hypothesis. Annals of the International Communication Association, 43(3), 210-227.",
             locator="43(3):210-227", locator_type="page_range",
             supports="meta-analytic evidence on the size and moderators of the knowledge gap", verified=True),
    ],
    "MC-466": [
        dict(kind="BOOK",
             title_en="The Effects of Mass Communication",
             title_fa="اثرات ارتباطات جمعی",
             authors="Klapper, J. T.", year=1960,
             publisher="Free Press",
             doi=None,
             url="https://archive.org/details/effectsofmasscom0000klap",
             language="en", isbn=None,
             citation="Klapper, J. T. (1960). The Effects of Mass Communication. Glencoe, IL: Free Press.",
             locator="1960 edition", locator_type="edition",
             supports="synthesis of limited effects: reinforcement rather than change", verified=True),
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
             supports="panel evidence that campaign media mainly reinforced existing predispositions", verified=True),
    ],
    "MC-551": [
        dict(kind="BOOK",
             title_en="Personal Influence: The Part Played by People in the Flow of Mass Communications",
             title_fa="نفوذ شخصی: نقش افراد در جریان ارتباطات جمعی",
             authors="Katz, E.; Lazarsfeld, P. F.", year=1955,
             publisher="Free Press",
             doi="10.4324/9781315126234",
             url="https://www.taylorfrancis.com/books/mono/10.4324/9781315126234/personal-influence-elihu-katz-paul-lazarsfeld-elmo-roper",
             language="en", isbn=None,
             citation="Katz, E., & Lazarsfeld, P. F. (1955). Personal Influence: The Part Played by People in the Flow of Mass Communications. Glencoe, IL: Free Press.",
             locator="1955 edition", locator_type="edition",
             supports="two-step and multi-step flow through opinion leaders", verified=True),
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
             supports="discovery of interpersonal relays in the flow of campaign communication", verified=True),
    ],
    "MC-552": [
        dict(kind="BOOK",
             title_en="Propaganda Technique in the World War",
             title_fa="فن تبلیغات در جنگ جهانی",
             authors="Lasswell, H. D.", year=1927,
             publisher="Alfred A. Knopf",
             doi=None,
             url="https://archive.org/details/dli.ernet.233727",
             language="en", isbn=None,
             citation="Lasswell, H. D. (1927). Propaganda Technique in the World War. New York: Alfred A. Knopf.",
             locator="1927 edition", locator_type="edition",
             supports="early stimulus-response account of powerful direct propaganda effects", verified=True),
        dict(kind="BOOK_CHAPTER",
             title_en="Remembering the Straw Man: The Travels and Adventures of Hypodermic",
             title_fa="به یاد آوردن آدم‌کاهی: سفرها و ماجراهای الگوی سوزن تزریقی",
             authors="Lubken, D.", year=2008,
             publisher="Peter Lang",
             doi=None,
             url="https://dokumen.pub/the-history-of-media-and-communication-research-contested-memories-9780820488295-0820488291-9781433102400-1433102404.html",
             language="en", isbn="9780820488295",
             citation="Lubken, D. (2008). Remembering the straw man: The travels and adventures of hypodermic. In D. W. Park & J. Pooley (Eds.), The History of Media and Communication Research: Contested Memories. New York: Peter Lang.",
             locator=None, locator_type=None,
             supports="historical critique showing the hypodermic model was largely a retrospective straw man", verified=True),
    ],
}

ENRICH = {
    "MC-011": dict(
        year=1970,
        summary="فرضیهٔ شکاف دانش، که فیلیپ تیچنور، جورج دونوهو و کلارس اولین در سال ۱۹۷۰ در فصل‌نامهٔ افکار عمومی منتشر کردند، می‌گوید ورود اطلاعات بیشتر به یک نظام اجتماعی، شکاف آگاهی میان گروه‌های برخوردار و کم‌برخوردار را کاهش نمی‌دهد، بلکه اغلب آن را گسترده‌تر می‌کند. پژوهشگران دانشگاه مینه‌سوتا نشان دادند گروه‌های دارای پایگاه اجتماعی و اقتصادی بالاتر، اطلاعات رسانه‌ای را سریع‌تر جذب و در خود هضم می‌کنند، زیرا مهارت خواندن و پردازش، دانش پیشین، شبکهٔ تماس اجتماعی و عادت به پیگیری خبر در آنان بیشتر است. اتما و کلاین در سال ۱۹۷۷ انگیزه و نفع کارکردی را به‌عنوان تعدیل‌کننده افزودند: وقتی موضوعی به زندگی روزمرهٔ فرد گره بخورد، شکاف می‌تواند کوچک شود. اثر سقف نیز نشان می‌دهد که پس از اشباع یک موضوع، جذب گروه کم‌برخوردار شتاب می‌گیرد. در رسانه، فرضیه برای تحلیل سواد سلامت، شکاف دیجیتال، آموزش عمومی و بحران اطلاعات به کار می‌رود؛ همه‌گیری کووید۱۹ نمونهٔ روشنی از شکاف در دسترسی به اطلاعات معتبر بود. نقدهای اصلی به آن، نخبه‌گرایی موضوعات آزمون، کم‌توجهی به ارتباط محلی، آزمون‌های مقطعی و امکان جبران شکاف با انگیزه را برجسته می‌کنند.",
        definition="فرضیهٔ شکاف دانش می‌گوید با افزایش جریان اطلاعات رسانه‌ای، گروه‌های برخوردار دانش را سریع‌تر جذب می‌کنند و شکاف آگاهی میان گروه‌های اجتماعی و اقتصادی افزایش می‌یابد.",
        main_problem="چرا گسترش اطلاعات رسانه‌ای به برابری آگاهی نمی‌انجامد و چه سازوکارهایی شکاف دانش میان گروه‌های اجتماعی و اقتصادی را بازتولید می‌کنند.",
        mechanism="گروه‌های برخوردار با مهارت پردازش، دانش پیشین، شبکهٔ اجتماعی و انگیزهٔ بیشتر، اطلاعات نو را سریع‌تر جذب می‌کنند؛ گروه‌های کم‌برخوردار کندتر پیش می‌روند و شکاف در طول زمان گسترده‌تر می‌شود.",
        assumptions=[
            "اطلاعات رسانه‌ای به‌طور نامتوازن توزیع می‌شود.",
            "پایگاه اجتماعی و اقتصادی جذب را تعیین می‌کند.",
            "دانش پیشین یادگیری نو را تسهیل می‌کند.",
            "مواجههٔ رسانه‌ای انتخابی است.",
            "انگیزه می‌تواند شکاف را تعدیل کند.",
        ],
        principles=[
            "پایگاه اجتماعی را کنترل کن.",
            "دانش پیشین را بسنج.",
            "موضوع را به زندگی روزمره گره بزن.",
            "به مخاطب کم‌برخوردار دسترسی ویژه بده.",
            "اثر سقف را در تحلیل بگنجان.",
            "شکاف را در طول زمان پیگیری کن.",
        ],
        critiques=[
            "موضوعات آزمون نخبه‌گرایانه‌اند.",
            "ارتباط محلی را کم می‌بیند.",
            "بیشتر آزمون‌ها مقطعی‌اند.",
            "انگیزه را دیر افزوده است.",
            "به شکاف مهارت دیجیتال کم توجه دارد.",
            "به تفاوت رسانه‌ها کم می‌پردازد.",
            "سنجش دانش را ساده می‌کند.",
            "به زمینهٔ غیرغربی کم توجه دارد.",
        ],
        critique_text="منتقدان می‌گویند فرضیهٔ شکاف دانش نابرابری اطلاعات را آشکار کرد اما موضوعات آزمون و سنجش مقطعی آن محدود بود؛ پژوهش‌های فراتحلیلی بعدی نشان دادند شکاف واقعی است اما اندازه و جهت آن به موضوع، رسانه و انگیزه بستگی دارد.",
        applications=[
            "تحلیل سواد سلامت.",
            "پژوهش شکاف دیجیتال.",
            "طراحی کمپین آموزش عمومی.",
            "تحلیل بحران اطلاعات.",
            "سیاست دسترسی برابر.",
            "پژوهش خبر علمی.",
            "آموزش رسانه برای گروه‌های کم‌برخوردار.",
            "تحلیل شکاف دانش در انتخابات.",
            "مطالعهٔ سواد سلامت دیجیتال در همه‌گیری.",
            "ارزیابی برنامهٔ آموزش سلامت روستایی.",
            "تحلیل شکاف دانش در آموزش عمومی بزرگسالان.",
        ],
        example_text="در همه‌گیری، گروه‌های تحصیل‌کرده سریع پروتکل‌های رسمی را یافتند و ارزیابی کردند، در حالی که گروه‌های کم‌درآمد بیشتر با شایعه و ابهام روبه‌رو شدند؛ شکاف دانش نه از کمبود اطلاعات، بلکه از نابرابری مهارت و دسترسی می‌آمد.",
        evolution="تیچنور و همکاران در سال ۱۹۷۰ فرضیه را ساختند و اتما و کلاین در سال ۱۹۷۷ انگیزه را افزودند؛ پژوهش‌های دیجیتال آن را به شکاف دسترسی، مهارت و بهره‌مندی گستردند و فراتحلیل‌های سال ۲۰۰۹ و ۲۰۱۹ اندازه و تعدیل‌کننده‌های شکاف را بازبینی کردند.",
        key_concepts=["شکاف دانش", "پایگاه اجتماعی و اقتصادی", "مهارت ارتباطی", "دانش پیشین", "انگیزه", "اثر سقف"],
        theorists="فیلیپ تیچنور، جورج دونوهو، کلارس اولین، جیمز اتما و اف جرالد کلاین.",
        theorists_text="فرضیه در سنت جامعه‌شناسی ارتباطات و نابرابری اطلاعات شکل گرفت.",
        model="جریان اطلاعات به‌عنوان سازوکار بازتولید شکاف آگاهی میان گروه‌های اجتماعی.",
        studies=[
            "مقالهٔ سال ۱۹۷۰ فرضیه را ساخت.",
            "پژوهش سال ۱۹۷۷ انگیزه را افزود.",
            "فراتحلیل سال ۲۰۰۹ اندازهٔ شکاف را سنجید.",
            "فراتحلیل سال ۲۰۱۹ تعدیل‌کننده‌ها را بازبینی کرد.",
            "مطالعهٔ سلامت، شکاف واکسن را بررسی کرد.",
            "پژوهش دیجیتال، شکاف مهارت را تحلیل کرد.",
        ],
    ),
    "MC-466": dict(
        year=1960,
        summary="فرضیهٔ تأثیر محدود، که جوزف کلاپر در سال ۱۹۶۰ در کتاب اثرات ارتباطات جمعی صورت‌بندی کرد، می‌گوید رسانه‌های جمعی به‌طور معمول نگرش‌ها را تغییر نمی‌دهند، بلکه آن‌ها را تقویت می‌کنند. کلاپر یافته‌های پژوهش‌های پیشین را گرد آورد و نتیجه گرفت اثر رسانه مشروط و محدود است: مخاطب پیام را بر پایهٔ باورها و گروه‌های مرجع خود انتخاب و تفسیر می‌کند و بیشتر در معرض پیام‌های هم‌سو با نگرش پیشین خود قرار می‌گیرد. سه سازوکار گزینشگری، یعنی مواجههٔ گزینشی، ادراک گزینشی و یادسپاری گزینشی، و نیز نقش رهبران عقیده و هنجارهای گروهی، اثر رسانه را تعدیل می‌کنند. کلاپر رویکرد خود را پدیده‌محور خواند: به جای پرسیدن اینکه رسانه چه می‌کند، باید پرسید تحت چه شرایطی و برای چه کسی چه اثری دارد. این فرضیه وارث پژوهش‌های لازارسفلد و همکاران در انتخابات و پژوهش‌های هالند دربارهٔ اقناع بود و برای دو دهه چارچوب اصلی مطالعهٔ اثرات رسانه ماند. در رسانه، فرضیه برای تحلیل کمپین، تبلیغات، خبر و شبکه‌های اجتماعی به کار می‌رود. نقدهای اصلی به آن، تعمیم آزمایشگاهی، ابهام جهت علیت، نمونه‌های غربی و کم‌توجهی به بازگشت اثرات قوی در محیط الگوریتمی را برجسته می‌کنند.",
        definition="فرضیهٔ تأثیر محدود می‌گوید رسانه‌های جمعی بیشتر نگرش‌های موجود را تقویت می‌کنند تا اینکه آن‌ها را تغییر دهند و اثر آن‌ها مشروط به گزینشگری مخاطب و فشار گروهی است.",
        main_problem="رسانه‌های جمعی تحت چه شرایطی و برای چه مخاطبی نگرش را تغییر می‌دهند و چرا در بیشتر موارد تنها آن را تقویت می‌کنند.",
        mechanism="مخاطب پیام هم‌سو با باور پیشین خود را انتخاب و به شکل هم‌خوان تفسیر می‌کند؛ رهبران عقیده و هنجار گروهی پیام را پالایش می‌کنند؛ در نتیجه اثر رسانه محدود به تقویت می‌شود مگر آنکه شرایط پیام و مخاطب تغییر کند.",
        assumptions=[
            "مخاطب فعال و گزینشگر است.",
            "باور پیشین تفسیر پیام را هدایت می‌کند.",
            "گروه مرجع نگرش را تثبیت می‌کند.",
            "رهبران عقیده واسطهٔ اثرند.",
            "اثر رسانه مشروط و محدود است.",
        ],
        principles=[
            "شرایط اثر را مشخص کن.",
            "گزینشگری مخاطب را بسنج.",
            "گروه مرجع را در تحلیل بگنجان.",
            "تفاوت تقویت و تغییر را روشن کن.",
            "به میدان واقعی و آزمایشگاه هر دو نگاه کن.",
            "بازگشت اثرات قوی را رصد کن.",
        ],
        critiques=[
            "تعمیم آزمایشگاهی دارد.",
            "جهت علیت روشن نیست.",
            "نمونه‌های غربی را تعمیم می‌دهد.",
            "اثرات قوی جدید را کم می‌بیند.",
            "به رسانهٔ شخصی‌سازی‌شده کم توجه دارد.",
            "تفاوت ژانرها را نادیده می‌گیرد.",
            "به اثر بلندمدت کم می‌پردازد.",
            "فرهنگ جمع‌گرا را کم می‌بیند.",
        ],
        critique_text="منتقدان می‌گویند فرضیهٔ تأثیر محدود تصویر دقیقی از مقاومت مخاطب داد اما با بازگشت اثرات قوی در تلویزیون و شبکه‌های اجتماعی و با ابهام جهت علیت، توضیح کافی برای همهٔ موقعیت‌ها نیست؛ با این حال، نقطهٔ عطف پژوهش اثرات رسانه است.",
        applications=[
            "تحلیل کمپین انتخاباتی.",
            "پژوهش تبلیغات.",
            "مطالعهٔ اثر خبر.",
            "تحلیل شبکهٔ اجتماعی و حباب.",
            "طراحی پیام سلامت.",
            "پژوهش اقناع.",
            "آموزش سواد رسانه.",
            "تحلیل کمپین واکسیناسیون.",
            "پژوهش مقاومت مخاطب در برابر تبلیغات.",
            "تحلیل تقویت نگرش در شبکه‌های اجتماعی.",
        ],
        example_text="فردی که اقتصاد را خوب می‌داند، ویدیوی گرانی را نخست با تفسیری هم‌سو با باور خود می‌خواند و سپس نگرشش را تنها اندکی تعدیل می‌کند؛ فرضیه می‌گوید رسانه در چنین وضعی بیشتر تقویت می‌کند تا تغییر.",
        evolution="پژوهش‌های لازارسفلد و همکاران در دههٔ ۱۹۴۰ و هالند در دههٔ ۱۹۵۰ زمینه را ساختند و کلاپر در سال ۱۹۶۰ آن‌ها را در فرضیهٔ تأثیر محدود جمع کرد؛ از دههٔ ۱۹۷۰ با بازگشت اثرات قوی و از دههٔ ۲۰۱۰ با رسانهٔ الگوریتمی، این فرضیه بار دیگر به بحث گذاشته شد.",
        key_concepts=["تأثیر محدود", "تقویت", "مواجههٔ گزینشی", "رهبر عقیده", "گروه مرجع", "رویکرد پدیده‌محور"],
        theorists="جوزف کلاپر، پل لازارسفلد و الیهو کاتز.",
        theorists_text="فرضیه در سنت پژوهش تجربی اثرات رسانه و جامعه‌شناسی ارتباطات شکل گرفت.",
        model="رسانه به‌عنوان عامل تقویت نگرش موجود، نه تغییر آن، در میدان گزینشگری مخاطب.",
        studies=[
            "کتاب سال ۱۹۶۰ یافته‌ها را جمع کرد.",
            "پژوهش انتخاباتی، تقویت را نشان داد.",
            "مطالعهٔ اقناع، شرایط اثر را سنجید.",
            "پژوهش رهبر عقیده، واسطه‌گری را تحلیل کرد.",
            "مطالعهٔ تلویزیون، بازگشت اثرات قوی را بررسی کرد.",
            "پژوهش دیجیتال، حباب را تحلیل کرد.",
        ],
    ),
    "MC-551": dict(
        year=1955,
        summary="فرضیهٔ جریان چندمرحله‌ای، که در پژوهش‌های پل لازارسفلد و همکاران در دههٔ ۱۹۴۰ آغاز شد و الیهو کاتز و پل لازارسفلد در سال ۱۹۵۵ در کتاب نفوذ شخصی آن را صورت‌بندی کردند، می‌گوید پیام رسانه‌ای معمولاً مستقیم به همهٔ مخاطبان نمی‌رسد و از چند گره انسانی می‌گذرد. در پژوهش انتخاباتی شهر ایلی، پژوهشگران دیدند تغییر رأی بیشتر از طریق گفت‌وگو با افراد آشنا رخ می‌دهد تا از شنیدن مستقیم پیام رسانه. کاتز و لازارسفلد در پژوهش شهر دیکِیتور نشان دادند که رهبران عقیده، پیام رسانه را دریافت، تفسیر و به دیگران منتقل می‌کنند و خود نیز زیر نفوذ رسانه و شبکهٔ اجتماعی‌اند. از این رو جریان ارتباط نه دو مرحله‌ای ساده، بلکه چندمرحله‌ای است: رسانه به رهبران عقیده می‌رسد، آنان به پیروان و پیروان نیز به حلقه‌های بعدی. این فرضیه نقش واسطه‌های انسانی، اعتماد بین‌فردی و شبکه‌های اجتماعی را در برابر تصویر تزریق مستقیم پیام برجسته کرد. در رسانه، فرضیه برای تحلیل بازنشر خبر، اینفلوئنسر، شبکهٔ پیام‌رسان و انتشار نوآوری به کار می‌رود. نقدهای اصلی به آن، ابهام مرز رهبر و پیرو، تمرکز بر زنان در نمونهٔ اصلی، کم‌توجهی به رسانهٔ دیجیتال و دشواری سنجش زنجیرهٔ انتقال را برجسته می‌کنند.",
        definition="فرضیهٔ جریان چندمرحله‌ای می‌گوید پیام رسانه از طریق رهبران عقیده و شبکه‌های بین‌فردی در چند گره منتقل و تفسیر می‌شود و اثر آن به همین واسطه‌ها بستگی دارد.",
        main_problem="پیام رسانه‌ای از چه مسیری به مخاطب می‌رسد، چه کسانی آن را تفسیر و بازپخش می‌کنند و شبکهٔ بین‌فردی چگونه اثر رسانه را تعدیل می‌کند.",
        mechanism="رسانه پیام را به رهبران عقیده می‌رساند؛ آنان آن را تفسیر و به پیروان منتقل می‌کنند؛ پیروان نیز در حلقه‌های بعدی بازپخش می‌کنند و در هر گره، معنا و اثر پیام بازسازی می‌شود.",
        assumptions=[
            "مخاطب در شبکهٔ اجتماعی جای دارد.",
            "رهبران عقیده واسطهٔ پیام‌اند.",
            "اعتماد بین‌فردی اثر را تعیین می‌کند.",
            "انتقال در چند گره رخ می‌دهد.",
            "معنا در هر گره بازتفسیر می‌شود.",
        ],
        principles=[
            "شبکهٔ انتقال را نقشه‌برداری کن.",
            "رهبران عقیده را شناسایی کن.",
            "اعتماد بین‌فردی را بسنج.",
            "بازنشر را در چند گره پیگیری کن.",
            "تفاوت رسانه و گفت‌وگو را ببین.",
            "به پلتفرم دیجیتال تعمیم شتاب‌زده نده.",
        ],
        critiques=[
            "مرز رهبر و پیرو مبهم است.",
            "نمونهٔ اصلی بر زنان متمرکز بود.",
            "رسانهٔ دیجیتال را در بر نمی‌گیرد.",
            "سنجش زنجیره دشوار است.",
            "به رهبران چندگانه کم توجه دارد.",
            "به ساختار قدرت شبکه کم می‌پردازد.",
            "به بازنشر الگوریتمی کم توجه دارد.",
            "به زمینهٔ غیرغربی کم می‌پردازد.",
        ],
        critique_text="منتقدان می‌گویند فرضیهٔ جریان چندمرحله‌ای نقش واسطه‌های انسانی را آشکار کرد اما مرز رهبر و پیرو و انتقال در رسانهٔ الگوریتمی را روشن نکرد؛ با این حال، چارچوب پایهٔ مطالعهٔ انتشار و نفوذ اجتماعی است.",
        applications=[
            "تحلیل بازنشر خبر.",
            "پژوهش اینفلوئنسر.",
            "مطالعهٔ شبکهٔ پیام‌رسان.",
            "تحلیل انتشار نوآوری.",
            "طراحی کمپین سلامت.",
            "پژوهش رهبران عقیده محلی.",
            "تحلیل نفوذ در شبکهٔ اجتماعی.",
            "مطالعهٔ انتقال پیام در بحران.",
            "تحلیل کمپین واکسیناسیون در شبکهٔ خانوادگی.",
            "پژوهش بازنشر محتوای سیاسی در گروه‌های پیام‌رسان.",
        ],
        example_text="خبری که در تلویزیون پخش می‌شود، نخست در گروه خانوادگی توسط فردی که به او اعتماد دارند بازگو و تفسیر می‌شود و سپس دیگران آن را با همان تفسیر می‌پذیرند؛ فرضیه می‌گوید اثر خبر در همین گره‌های انسانی ساخته می‌شود.",
        evolution="پژوهش انتخاباتی دههٔ ۱۹۴۰ جریان دوشعویه را کشف کرد و کاتز و لازارسفلد در سال ۱۹۵۵ آن را به جریان چندمرحله‌ای و رهبری عقیده بسط دادند؛ پژوهش‌های انتشار نوآوری و سپس رسانهٔ دیجیتال، مدل را به شبکه‌های چندگانه و بازنشر الگوریتمی گستردند.",
        key_concepts=["جریان چندمرحله‌ای", "رهبر عقیده", "جریان دوشعویه", "شبکهٔ بین‌فردی", "اعتماد", "بازنشر"],
        theorists="پل لازارسفلد، برنارد برلسون، هِیزل گودت و الیهو کاتز.",
        theorists_text="فرضیه در سنت پژوهش تجربی ارتباطات و جامعه‌شناسی شبکه شکل گرفت.",
        model="پیام رسانه به‌عنوان جریانی چندگره‌ای که در هر گره تفسیر و بازپخش می‌شود.",
        studies=[
            "پژوهش انتخاباتی دههٔ ۱۹۴۰ جریان دوشعویه را یافت.",
            "کتاب سال ۱۹۵۵ رهبری عقیده را تحلیل کرد.",
            "پژوهش انتشار، مدل چندمرحله‌ای را گسترد.",
            "مطالعهٔ سلامت، نفوذ خانوادگی را سنجید.",
            "پژوهش دیجیتال، بازنشر شبکه‌ای را بررسی کرد.",
            "مطالعهٔ بحران، انتقال پیام را تحلیل کرد.",
        ],
    ),
    "MC-552": dict(
        year=1927,
        summary="فرضیهٔ جریان یک‌مرحله‌ای، که ریشهٔ آن به پژوهش هارولد لاسول در سال ۱۹۲۷ دربارهٔ تبلیغات جنگ جهانی بازمی‌گردد، تصویری از ارتباط جمعی می‌دهد که در آن پیام قدرتمند رسانه مستقیم، یکسان و فوری بر تودهٔ مخاطبان اثر می‌گذارد. در این تصویر، مخاطب منفعل و همگن فرض می‌شود و تفاوت‌های فردی، گروهی و فرهنگی جای چندانی ندارند؛ پیام همچون گلوله یا سوزنی به بدن اجتماعی نفوذ می‌کند و نگرش را می‌سازد. این الگو در دههٔ ۱۹۲۰ و ۱۹۳۰ با تجربهٔ تبلیغات جنگ، رادیو و سینما باورپذیری زیادی داشت و بعدها با نام مدل گلولهٔ جادویی یا سوزن تزریقی شناخته شد. پژوهش‌های تجربی دههٔ ۱۹۴۰ و ۱۹۵۰، از جمله مطالعهٔ انتخاباتی لازارسفلد و پژوهش اقناع هالند، نشان دادند که اثر رسانه معمولاً مشروط و محدود است و این الگو را به چالش کشیدند. لوبکن در سال ۲۰۰۸ نشان داد که الگوی سوزن تزریقی تا حد زیادی آدم‌کاهی ساختهٔ کتاب‌های درسی بوده و کمتر پژوهشی آن را به‌صورت جدی آزموده است. در رسانه، این فرضیه اکنون بیشتر به‌عنوان نقطهٔ مقابل نظریه‌های اثر محدود و مبنای بحث بازگشت اثرات قوی به کار می‌رود. نقدهای اصلی به آن، انفعال‌گرایی افراطی، نادیده‌گرفتن گزینشگری مخاطب و ساده‌سازی فرایند معنا را برجسته می‌کنند.",
        definition="فرضیهٔ جریان یک‌مرحله‌ای می‌گوید پیام رسانه مستقیم، یکسان و فوری بر تودهٔ منفعل مخاطبان اثر می‌گذارد و نگرش و رفتار آنان را می‌سازد.",
        main_problem="آیا رسانه می‌تواند پیام را بی‌واسطه و یکسان به همهٔ مخاطبان تزریق کند و نگرش آنان را به‌طور یکدست تغییر دهد.",
        mechanism="پیام قدرتمند و تکرارشونده از رسانه به تودهٔ همگن می‌رسد؛ مخاطب منفعل آن را بی‌واسطه می‌پذیرد؛ تفاوت‌های فردی و گروهی نادیده گرفته می‌شود و اثر یکسان و فوری پدید می‌آید.",
        assumptions=[
            "مخاطب منفعل است.",
            "توده همگن است.",
            "پیام رسانه قدرتمند است.",
            "اثر مستقیم و فوری است.",
            "واسطهٔ انسانی نقش ندارد.",
        ],
        principles=[
            "پیام را تکرار و پرتکرار کن.",
            "یک پیام برای همه بساز.",
            "اثر فوری را انتظار داشته باش.",
            "تفاوت مخاطب را نادیده بگیر.",
            "به رسانهٔ توده‌ای تکیه کن.",
            "نتیجه را با پیمایش ساده بسنج.",
        ],
        critiques=[
            "مخاطب را منفعل فرض می‌کند.",
            "توده را همگن می‌بیند.",
            "گزینشگری مخاطب را نادیده می‌گیرد.",
            "واسطهٔ بین‌فردی را حذف می‌کند.",
            "فرایند معنا را ساده می‌کند.",
            "شاهد تجربی کافی ندارد.",
            "بر خوانش کتاب‌های درسی تکیه دارد.",
            "به تفاوت فرهنگی کم توجه است.",
        ],
        critique_text="منتقدان می‌گویند فرضیهٔ جریان یک‌مرحله‌ای تصویری اغراق‌شده از قدرت رسانه ساخت و پژوهش تجربی آن را رد کرد؛ با این حال، به‌عنوان نقطهٔ مقابل نظریه‌های اثر محدود و مبنای بحث اثرات قوی، همچنان در آموزش ارتباطات حضور دارد.",
        applications=[
            "آموزش تاریخ نظریه‌های اثر.",
            "تحلیل تبلیغات جنگ.",
            "پژوهش تبلیغات سیاسی.",
            "مقایسه با نظریهٔ اثر محدود.",
            "تحلیل کمپین یک‌پیامی.",
            "مطالعهٔ پروپاگاندای تاریخی.",
            "نقد مدل‌های سادهٔ اثر.",
            "تحلیل فرض تودهٔ همگن.",
            "مبانی نظری بحث بازگشت اثرات قوی.",
            "آموزش نقد مدل گلولهٔ جادویی در کلاس ارتباطات.",
        ],
        example_text="پژوهشگران دههٔ ۱۹۲۰ گمان می‌کردند پیام رادیویی می‌تواند همهٔ شنوندگان را یکسان متقاعد کند؛ اما پژوهش انتخاباتی بعدی نشان داد مخاطبان بر پایهٔ باور و گروه خود پیام را می‌گزینند و همین یافته، الگوی تزریق مستقیم را فرو ریخت.",
        evolution="لاسول در سال ۱۹۲۷ الگوی تبلیغات قوی را صورت‌بندی کرد و این تصویر تا دههٔ ۱۹۳۰ غالب ماند؛ پژوهش‌های تجربی دههٔ ۱۹۴۰ و ۱۹۵۰ آن را به نظریهٔ اثر محدود بدل کردند و لوبکن در سال ۲۰۰۸ نشان داد بخشی از این الگو آدم‌کاهی کتاب‌های درسی بوده است.",
        key_concepts=["جریان یک‌مرحله‌ای", "گلولهٔ جادویی", "سوزن تزریقی", "مخاطب منفعل", "تودهٔ همگن", "تبلیغات"],
        theorists="هارولد لاسول، پل لازارسفلد و دبرا لوبکن.",
        theorists_text="فرضیه در سنت نظریهٔ جامعهٔ توده‌ای و پژوهش تبلیغات شکل گرفت.",
        model="رسانه به‌عنوان تزریق مستقیم پیام به تودهٔ منفعل با اثر یکسان و فوری.",
        studies=[
            "کتاب سال ۱۹۲۷ الگوی تبلیغات قوی را ساخت.",
            "پژوهش انتخاباتی دههٔ ۱۹۴۰ آن را به چالش کشید.",
            "مطالعهٔ اقناع، اثر مشروط را نشان داد.",
            "پژوهش سال ۲۰۰۸ آدم‌کاهی بودن آن را تحلیل کرد.",
            "مطالعهٔ کتاب‌های درسی، بازتولید الگو را بررسی کرد.",
            "پژوهش دیجیتال، فرض ویروسی‌شدن را بازبینی کرد.",
        ],
    ),
}

NAME_FIX = {
    "MC-552": ("فرضیهٔ جریان یک‌مرحله‌ای (مدل گلولهٔ جادویی)", "Single-Stage Flow Hypothesis (Magic Bullet Model)", "عنوان و بدنهٔ کارت ناقص بود و سال ثبت نشده بود؛ این فرضیه همان مدل گلولهٔ جادویی یا سوزن تزریقی است و عنوان برای شناسایی دقیق‌تر اصلاح شد."),
}
YEAR_FIX = {
    "MC-011": "شمارهٔ صفحه و شمارهٔ جلد منبع پیشنهادی کارت نادرست بود؛ مقاله در جلد ۳۴ شمارهٔ ۲ صفحات ۱۵۹ تا ۱۷۰ منتشر شده و استناد اصلاح شد.",
    "MC-466": "تحلیل تفصیلی کارت برخلاف منطق عنوان، اثر رسانه را تغییردهندهٔ باور توصیف کرده بود؛ محتوا بر پایهٔ کلاپر ۱۹۶۰ و لازارسفلد و همکاران ۱۹۴۸ بازنویسی شد.",
    "MC-551": "نظریه‌پرداز کارت «ویلیامز و همکاران» بود که با منبعی پشتیبانی نمی‌شود؛ فرضیه از لازارسفلد و همکاران و کاتز و لازارسفلد است و سال به ۱۹۵۵ اصلاح شد.",
    "MC-552": "کارت فاقد سال و نظریه‌پرداز مشخص بود و بدنهٔ آن قالب عمومی اقناع داشت؛ محتوا بر پایهٔ لاسول ۱۹۲۷ و لوبکن ۲۰۰۸ بازنویسی و سال ۱۹۲۷ ثبت شد.",
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
                                       "verified": n_verified, "batch": 162}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH162 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
