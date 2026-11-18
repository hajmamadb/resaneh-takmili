# -*- coding: utf-8 -*-
"""Batch 191: th-16 Lewin, th-27 Barthes, th-32 Smythe, th-38 Hesmondhalgh (PERSON)."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch191-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch191.json"

PERSON_MAPPING = {"entity_type": "PERSON", "family_code": "INTELLECTUAL_AGENT",
                  "content_type": "شخصیت علمی (نظریه‌پرداز)", "needs_review": False}

S = {
    "th-16": [
        dict(kind="BOOK",
             title_en="Field Theory in Social Science: Selected Theoretical Papers",
             title_fa="نظریهٔ میدان در علم اجتماعی: مقالات نظری برگزیده",
             authors="Kurt Lewin", year=1951,
             publisher="Harper & Brothers",
             doi=None,
             url="https://archive.org/details/dli.ernet.503983",
             language="en", isbn=None,
             citation="Lewin, K. (1951). Field Theory in Social Science: Selected Theoretical Papers (D. Cartwright, Ed.). New York: Harper & Brothers.",
             locator="papers on field theory and the life space", locator_type="CHAPTER",
             supports="field theory, the life space and the person-environment formula", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Patterns of Aggressive Behavior in Experimentally Created \"Social Climates\"",
             title_fa="الگوهای رفتار پرخاشگرانه در «جوهای اجتماعی» آزمایشگاهی",
             authors="Kurt Lewin; Ronald Lippitt; Ralph K. White", year=1939,
             publisher="The Journal of Social Psychology",
             doi="10.1080/00224545.1939.9713366",
             url="https://www.tandfonline.com/doi/abs/10.1080/00224545.1939.9713366",
             language="en", isbn=None,
             citation="Lewin, K., Lippitt, R., & White, R. K. (1939). Patterns of aggressive behavior in experimentally created \"social climates\". The Journal of Social Psychology, 10(2), 269-299.",
             locator="pp. 269-299", locator_type="PAGE",
             supports="the Iowa experiments comparing autocratic, democratic and laissez-faire leadership climates", verified=True),
    ],
    "th-27": [
        dict(kind="BOOK",
             title_en="Mythologies",
             title_fa="اسطوره‌شناسی‌ها",
             authors="Roland Barthes", year=1957,
             publisher="Éditions du Seuil",
             doi=None,
             url="https://archive.org/details/BarthesRolandMythologies1957_201612",
             language="fr", isbn=None,
             citation="Barthes, R. (1957). Mythologies. Paris: Éditions du Seuil.",
             locator="essays on myth as a second-order sign system", locator_type="CHAPTER",
             supports="myth as a second-order semiological system that naturalizes culture", verified=True),
        dict(kind="BOOK",
             title_en="Image, Music, Text",
             title_fa="تصویر، موسیقی، متن",
             authors="Roland Barthes (trans. Stephen Heath)", year=1977,
             publisher="Fontana Press",
             doi=None,
             url="https://archive.org/details/imagemusictext0000rola",
             language="en", isbn=None,
             citation="Barthes, R. (1977). Image, Music, Text (S. Heath, Trans.). London: Fontana Press.",
             locator="The Rhetoric of the Image; The Death of the Author", locator_type="CHAPTER",
             supports="denotation and connotation in the photographic image, and the critique of authorial intention", verified=True),
    ],
    "th-32": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Communications: Blindspot of Western Marxism",
             title_fa="ارتباطات: نقطهٔ کور مارکسیسم غربی",
             authors="Dallas W. Smythe", year=1977,
             publisher="Canadian Journal of Political and Social Theory",
             doi=None,
             url="https://journals.uvic.ca/index.php/ctheory/article/view/13715",
             language="en", isbn=None,
             citation="Smythe, D. W. (1977). Communications: Blindspot of Western Marxism. Canadian Journal of Political and Social Theory, 1(3), 1-27.",
             locator="pp. 1-27", locator_type="PAGE",
             supports="the audience commodity thesis and the critique of Western Marxism's neglect of communication", verified=True),
        dict(kind="WEBSITE",
             title_en="Dallas Smythe Reloaded: Critical Media and Communication Studies Today",
             title_fa="دالاس اسمایث بازخوانی‌شده: مطالعات انتقادی رسانه و ارتباطات امروز",
             authors="Christian Fuchs", year=2012,
             publisher="Christian Fuchs (author's site)",
             doi=None,
             url="https://fuchsc.net/wp-content/dsmythe.pdf",
             language="en", isbn=None,
             citation="Fuchs, C. Dallas Smythe Reloaded: Critical Media and Communication Studies Today.",
             locator="sections on the audience commodity and digital labour", locator_type="SECTION",
             supports="scholarly assessment of Smythe's audience commodity thesis and its extension to digital labour", verified=True),
    ],
    "th-38": [
        dict(kind="BOOK",
             title_en="The Cultural Industries",
             title_fa="صنایع فرهنگی",
             authors="David Hesmondhalgh", year=2002,
             publisher="SAGE Publications",
             doi=None,
             url="https://archive.org/details/culturalindustri0000hesm",
             language="en", isbn=None,
             citation="Hesmondhalgh, D. (2002). The Cultural Industries. London: SAGE Publications.",
             locator="chapters on symbolic creativity, risk and the cultural industries", locator_type="CHAPTER",
             supports="the cultural industries framework: symbolic creativity, risk and market organization", verified=True),
        dict(kind="WEBSITE",
             title_en="The Cultural Industries (Google Books record)",
             title_fa="صنایع فرهنگی (رکورد گوگل بوکس)",
             authors="David Hesmondhalgh", year=2002,
             publisher="SAGE Publications",
             doi=None,
             url="https://books.google.com/books/about/The_Cultural_Industries.html?id=AlEig8UERpEC",
             language="en", isbn=None,
             citation="Hesmondhalgh, D. The Cultural Industries. SAGE Publications (Google Books record).",
             locator="edition and publication record", locator_type="SECTION",
             supports="publication history across editions (2002, 2007, 2013, 2019)", verified=True),
    ],
}

ENRICH = {
    "th-16": dict(
        mapping=PERSON_MAPPING,
        summary="کرت لوین روان‌شناس اجتماعی آلمانی-آمریکایی و بنیان‌گذار نظریهٔ میدان و پویایی گروه است. او رفتار را تابعی از شخص و محیط روان‌شناختی می‌دانست و مفهوم فضای زندگی را برای توصیف کلیت ادراک‌شدهٔ فرد به کار برد. لوین پس از مهاجرت به آمریکا در ۱۹۳۳، پژوهش گروهی را در دانشگاه آیووا گسترد و با رونالد لیپیت و رالف وایت در ۱۹۳۹ جوهای رهبری خودکامه، دموکراتیک و آزادگذار را در آزمایش مقایسه کرد. این پژوهش نشان داد جو دموکراتیک مشارکت و رضایت بیشتری می‌سازد و جو خودکامه پرخاشگری و وابستگی را افزایش می‌دهد. لوین پژوهش کنشی را پیش برد: پژوهش و تغییر اجتماعی در یک فرایند مشارکتی پیوند می‌خورند. مدل سه‌مرحله‌ای انجمادزدایی، تغییر و انجماد مجدد به او نسبت داده می‌شود، هرچند صورت‌بندی دقیق آن پس از او رواج یافت. او مرکز پژوهش پویایی گروه را در دانشگاه ام آی تی بنیان گذاشت و بر سازمان‌ها، آموزش و ارتباطات گروهی اثر گذاشت. در مطالعات رسانه، مفاهیم او برای فهم مخاطب به‌مثابه گروه، تغییر رفتار جمعی و طراحی کمپین مشارکتی به کار می‌رود. نقدها بر سنجش‌پذیری فضای زندگی، ساده‌سازی مدل سه‌مرحله‌ای و بافت‌مندی آزمایش‌های رهبری تأکید دارند.",
        definition="نظریهٔ میدان لوین رفتار را تابعی از شخص و محیط روان‌شناختی او می‌داند و تغییر را حاصل بازآرایی نیروهای موجود در فضای زندگی می‌شمارد.",
        main_problem="چگونه می‌توان رفتار فرد و گروه را در میدان نیروهای روانی و اجتماعی تبیین کرد و تغییر پایدار را با مشارکت خود کنشگران ممکن ساخت.",
        mechanism="فضای زندگی از شخص و محیط ادراک‌شده ساخته می‌شود؛ هدف‌ها و موانع نیروهایی می‌سازند که تعادل رفتار را تعیین می‌کنند و بازتعریف میدان یا مشارکت گروهی، این تعادل را جابه‌جا می‌کند.",
        assumptions=[
            "رفتار تابع شخص و محیط است.",
            "محیط روان‌شناختی با محیط عینی یکی نیست.",
            "گروه، میدانی از نیروهای متقابل است.",
            "تنش میان هدف و مانع رفتار را جهت می‌دهد.",
            "مشارکت، مقاومت در برابر تغییر را کاهش می‌دهد.",
            "تغییر پایدار به بازآرایی میدان نیاز دارد.",
            "پژوهش و کنش می‌توانند یکی شوند.",
            "جو رهبری بر رفتار گروه اثر می‌گذارد.",
        ],
        principles=[
            "میدان نیروها را پیش از مداخله ترسیم کن.",
            "محیط ادراک‌شدهٔ کنشگر را بشناس.",
            "مشارکت گروهی را در تغییر بگنجان.",
            "از تغییر تحمیلی بپرهیز.",
            "جو رهبری را با هدف هم‌سو کن.",
            "پژوهش را با کنش پیوند بزن.",
            "تغییر را مرحله‌ای و پایش‌شده پیش ببر.",
        ],
        critiques=[
            "سنجش تجربی فضای زندگی دشوار است.",
            "مدل سه‌مرحله‌ای به لوین نسبت داده شده و ساده‌سازی است.",
            "آزمایش‌های رهبری به بافت و گروه محدودند.",
            "استعارهٔ میدان بیش از حد فیزیکی است.",
            "عوامل ساختاری و فرهنگی کم‌رنگ می‌شوند.",
            "تعمیم یافته‌های آزمایشگاهی به میدان دشوار است.",
            "نقش احساس و بدن کمتر تحلیل شده است.",
        ],
        critique_text="منتقدان می‌گویند سنجش فضای زندگی دشوار است، مدل سه‌مرحله‌ای ساده‌سازی شده و آزمایش‌های رهبری به بافت محدودند؛ با این حال مفاهیم میدان، پویایی گروه و پژوهش کنشی لوین بنیادی برای مطالعهٔ تغییر رفتار جمعی و ارتباطات گروهی شده است.",
        applications=[
            "طراحی کمپین مشارکتی.",
            "تغییر سازمانی.",
            "مطالعهٔ ارتباطات گروهی.",
            "پژوهش کنشی رسانه.",
            "آموزش و جو کلاس.",
            "ارتباطات سلامت.",
            "توسعهٔ جامعهٔ محلی.",
            "تحلیل رهبری رسانه‌ای.",
            "پژوهش رفتار مصرف‌کننده.",
            "مدیریت تغییر فناوری.",
            "مطالعهٔ گروه‌های آنلاین.",
            "ارتباطات بحران.",
            "آموزش سازمانی.",
            "پژوهش مشارکت مدنی.",
        ],
        example_text="در آزمایش‌های آیووا، گروه‌های کودکانه زیر رهبری خودکامه پرخاشگری و وابستگی بیشتری نشان دادند، در حالی که جو دموکراتیک مشارکت و ابتکار را برانگیخت؛ این یافته الگویی برای فهم اثر سبک رهبری بر ارتباط گروهی شد.",
        evolution="لوین در سنت گشتالت برلین پرورش یافت، در ۱۹۳۳ به آمریکا مهاجرت کرد، در آیووا پژوهش رهبری و تغییر را پیش برد، در ۱۹۴۴ مرکز پویایی گروه را در دانشگاه ام آی تی بنیان گذاشت، پس از مرگش در ۱۹۴۷ میراث او به پژوهش کنشی و توسعهٔ سازمانی راه یافت و امروز در مطالعهٔ گروه‌های آنلاین بازخوانی می‌شود.",
        key_concepts=["نظریهٔ میدان", "فضای زندگی", "پویایی گروه", "پژوهش کنشی", "جو رهبری", "تعادل نیروها"],
        theorists="کرت لوین.",
        theorists_text="کرت لوین با پیوند روان‌شناسی گشتالت و پژوهش گروهی، نظریهٔ میدان، مفهوم فضای زندگی و روش پژوهش کنشی را صورت‌بندی کرد و مطالعهٔ تجربی جوهای رهبری را بنیان گذاشت.",
        model="مدل میدان: رفتار تابعی از شخص و محیط ادراک‌شده است؛ نیروهای هدف و مانع تعادل را می‌سازند و تغییر پایدار از بازآرایی میدان با مشارکت گروهی حاصل می‌شود.",
        studies=[
            "آزمایش جوهای رهبری.",
            "پژوهش نظریهٔ میدان.",
            "مطالعهٔ پویایی گروه.",
            "تحلیل پژوهش کنشی.",
            "پژوهش تغییر سازمانی.",
            "مطالعهٔ ارتباطات گروهی.",
            "تحلیل جو کلاس درس.",
            "پژوهش کمپین مشارکتی.",
            "مطالعهٔ گروه‌های آنلاین.",
            "تحلیل رهبری رسانه‌ای.",
            "پژوهش رفتار مصرف‌کننده.",
            "مطالعهٔ مدیریت تغییر.",
            "تحلیل ارتباطات بحران.",
            "پژوهش مشارکت مدنی.",
        ],
    ),
    "th-27": dict(
        mapping=PERSON_MAPPING,
        summary="رولان بارت نشانه‌شناس، منتقد ادبی و نظریه‌پرداز فرهنگی فرانسوی است که نقش محوری در گذار از نقد ادبی به نشانه‌شناسی رسانه و فرهنگ داشت. در اسطوره‌شناسی‌ها ۱۹۵۷ نشان داد چگونه فرهنگ عامه، نشانه‌ها را در نظامی مرتبه‌دوم به اسطوره بدل می‌کند و تاریخ را طبیعی جلوه می‌دهد. او میان دلالت صریح و دلالت ضمنی تفکیک کرد و در مقالهٔ بلاغت تصویر، پیام زبانی، پیام شمایلی رمزگذاری‌شده و پیام شمایلی غیررمزگذاری‌شده را در عکس تحلیل کرد. مقالهٔ مرگ مؤلف در ۱۹۶۷ اختیار معنا را از نیت نویسنده به خواننده منتقل کرد و در اس زد ۱۹۷۰ میان متن خواندنی و نوشتنی تمایز گذاشت. کتاب اتاق روشن ۱۹۸۰ با مفاهیم استودیوم و پونکتوم، تجربهٔ عکس را به عاطفه و فقدان گره زد. بارت الگویی برای تحلیل تبلیغات، عکاسی خبری، مد و فیلم فراهم کرد و در نوشته‌های متأخر خود از نظام نشانه‌شناختی به تجربهٔ شخصی خواننده و عاطفهٔ عکس گذر کرد. نقدها بر تاریخ‌گریزی، گزینش نمونه‌های نخبه‌گرا، ابهام روش و تغییر مواضع خود او تأکید دارند.",
        definition="نشانه‌شناسی بارت نظام‌های معنایی فرهنگ را تحلیل می‌کند و نشان می‌دهد چگونه اسطوره، دلالت ضمنی را به طبیعت بدل می‌کند.",
        main_problem="چگونه فرهنگ عامه و رسانه، معنای تاریخی و ایدئولوژیک را طبیعی و بدیهی جلوه می‌دهند و خواننده چگونه در تولید معنا مشارکت می‌کند.",
        mechanism="نشانه در مرتبهٔ دوم به نشانه‌ای تازه بدل می‌شود؛ اسطوره تاریخ و منشأ اجتماعی دلالت را می‌زداید و آن را واقعیتی طبیعی می‌نمایاند، در حالی که خواننده با رمزگان فرهنگی آن را بازمی‌خواند.",
        assumptions=[
            "فرهنگ نظامی از نشانه‌هاست.",
            "معنا در دلالت ضمنی ساخته می‌شود.",
            "اسطوره معنای ایدئولوژیک را طبیعی می‌کند.",
            "متن به خوانندهٔ فعال نیاز دارد.",
            "نیت مؤلف مرجع نهایی معنا نیست.",
            "تصویر نیز مانند زبان رمزگذاری می‌شود.",
            "رمزگان فرهنگی مشترک‌اند.",
            "تحلیل متن به نقد ایدئولوژی راه می‌برد.",
        ],
        principles=[
            "نشانه را در نظام کلی آن بخوان.",
            "دلالت ضمنی را از صریح جدا کن.",
            "طبیعی‌شدگی را آشکار کن.",
            "به رمزگان فرهنگی مخاطب توجه کن.",
            "تصویر را متن بخوان.",
            "نیت مؤلف را کنار بگذار.",
            "تاریخ منشأ معنا را بازیاب.",
        ],
        critiques=[
            "تحلیل‌ها تاریخ‌گریز و گزینشی‌اند.",
            "نمونه‌ها اغلب نخبه‌گرا انتخاب می‌شوند.",
            "روش تحلیل به‌سختی تکرارپذیر است.",
            "مرز دلالت صریح و ضمنی مبهم است.",
            "مواضع بارت در طول زمان تغییر کرده است.",
            "نقش نهادهای تولید معنا کم‌رنگ می‌شود.",
            "تعمیم تحلیل متنی به مخاطب واقعی دشوار است.",
        ],
        critique_text="منتقدان می‌گویند تحلیل بارت گزینشی و تکرارناپذیر است، مرز دلالت‌ها مبهم می‌ماند و مواضع او در طول زمان تغییر کرده؛ با این حال الگوی او برای آشکارسازی ایدئولوژی در تبلیغات و عکس خبری همچنان بنیادی است.",
        applications=[
            "تحلیل تبلیغات.",
            "نقد عکاسی خبری.",
            "مطالعهٔ مد و سبک.",
            "تحلیل فیلم.",
            "نقد برند.",
            "مطالعهٔ فرهنگ عامه.",
            "تحلیل جلد نشریه.",
            "پژوهش نشانه‌شناسی غذا.",
            "نقد گردشگری.",
            "تحلیل موسیقی عامه.",
            "مطالعهٔ معماری.",
            "پژوهش هویت بصری.",
            "تحلیل شبکه‌های اجتماعی.",
            "تحلیل آگهی چاپی.",
            "آموزش سواد رسانه‌ای.",
        ],
        example_text="تحلیل جلد یک مجله نمونهٔ روش بارت است: چهره، لباس، رنگ و چیدمان در مرتبهٔ نخست دیده می‌شوند، اما در مرتبهٔ دوم مجموعه‌ای از ارزش‌های طبیعی‌شده دربارهٔ خانواده، موفقیت یا ملت را حمل می‌کنند.",
        evolution="بارت در دههٔ ۱۹۵۰ با اسطوره‌شناسی‌ها نقد فرهنگی را به نشانه‌شناسی پیوند زد، در دههٔ ۱۹۶۰ ساختارگرایی و تحلیل روایت را گسترد، در اواخر دههٔ ۱۹۶۰ با مرگ مؤلف و اس زد به متانت و خواننده گرایید و در اتاق روشن ۱۹۸۰ به عاطفه و فقدان رسید.",
        key_concepts=["اسطوره", "دلالت صریح", "دلالت ضمنی", "مرگ مؤلف", "رمزگان", "استودیوم و پونکتوم"],
        theorists="رولان بارت.",
        theorists_text="رولان بارت با بسط نشانه‌شناسی به فرهنگ عامه، تحلیل اسطوره، دلالت تصویری و مرگ مؤلف را صورت‌بندی کرد و زبان نقد فرهنگی رسانه را دگرگون ساخت.",
        model="مدل دلالت دومرتبه‌ای: نشانه در مرتبهٔ نخست به دال و مدلول می‌رسد؛ در مرتبهٔ دوم همین نشانه به دالی برای معنای ایدئولوژیک بدل می‌شود و اسطوره آن را طبیعی می‌نمایاند.",
        studies=[
            "تحلیل اسطورهٔ فرهنگ عامه.",
            "پژوهش بلاغت تصویر.",
            "مطالعهٔ عکاسی خبری.",
            "تحلیل تبلیغات.",
            "پژوهش مد و سبک.",
            "مطالعهٔ جلد نشریه.",
            "تحلیل فیلم.",
            "پژوهش برند.",
            "مطالعهٔ موسیقی عامه.",
            "تحلیل گردشگری.",
            "پژوهش هویت بصری.",
            "مطالعهٔ معماری.",
            "تحلیل شبکهٔ اجتماعی.",
            "پژوهش سواد رسانه‌ای.",
        ],
    ),
    "th-32": dict(
        mapping=PERSON_MAPPING,
        summary="دالاس اسمایث اقتصاددان سیاسی ارتباطات کانادایی و نظریه‌پرداز کالای مخاطب در سنت اقتصاد سیاسی انتقادی است. او در مقالهٔ ارتباطات: نقطهٔ کور مارکسیسم غربی در ۱۹۷۷ استدلال کرد که در سرمایه‌داری انحصاری، رسانهٔ تبلیغاتی مخاطبان را گرد می‌آورد و توجه آنان را به تبلیغ‌دهنده می‌فروشد؛ از این رو مخاطب خود کالایی است که تولید و مبادله می‌شود. اسمایث مارکسیسم غربی را نقد کرد که به گفتهٔ او کار رسانه‌ای و صنعت آگاهی را نادیده گرفته است. او در وابستگی راه ۱۹۸۱ این تحلیل را به مناسبات جهانی ارتباطات و انتقال فناوری گسترد. پژوهش او بحث‌های بعدی دربارهٔ کار دیجیتال، داده و اقتصاد پلتفرم را ممکن ساخت و کریستیان فوکس آن را به شرایط امروز تعمیم داد. او همچنین از پیشگامان آموزش سیاست‌گذاری ارتباطات و اقتصاد رسانه در کانادا بود. نقدها بر تقلیل رسانه به تبلیغات، کارکردگرایی، نادیده‌گرفتن رسانهٔ عمومی و فعالیت مخاطب، و ساده‌سازی مناسبات پیچیدهٔ تولید معنا تأکید دارند.",
        definition="کالای مخاطب یعنی تبدیل توجه گردآمدهٔ مخاطبان به محصولی که رسانهٔ تبلیغاتی به تبلیغ‌دهنده می‌فروشد.",
        main_problem="منبع اصلی ارزش در رسانهٔ تجاری چیست و چگونه کار مخاطب در اقتصاد سیاسی ارتباطات پنهان می‌ماند.",
        mechanism="محتوای رسانه مخاطب را گرد می‌آورد، سنجش مخاطب این توجه را قابل‌فروش می‌کند و تبلیغ‌دهنده برای دسترسی به آن بهای می‌پردازد؛ در نتیجه توجه مخاطب به کالا بدل می‌شود.",
        assumptions=[
            "رسانهٔ تجاری با فروش توجه درآمد می‌گیرد.",
            "مخاطب در این فرایند کار انجام می‌دهد.",
            "اقتصاد سیاسی برای فهم رسانه ضروری است.",
            "مارکسیسم غربی کار رسانه را نادیده گرفته است.",
            "صنعت آگاهی بخشی از تولید سرمایه‌داری است.",
            "سنجش مخاطب توجه را قابل مبادله می‌کند.",
            "مناسبات جهانی ارتباطات نابرابرند.",
            "داده و کار دیجیتال ادامهٔ منطق کالای مخاطب‌اند.",
        ],
        principles=[
            "درآمد رسانه را ردیابی کن.",
            "کار مخاطب را آشکار کن.",
            "سنجش مخاطب را نقد کن.",
            "رسانهٔ عمومی را در تحلیل بگنجان.",
            "مناسبات جهانی را بسنج.",
            "داده را به‌مثابه کار تحلیل کن.",
            "از تقلیل معنا به اقتصاد بپرهیز.",
        ],
        critiques=[
            "رسانه را بیش از حد به تبلیغات تقلیل می‌دهد.",
            "کارکردگرایی و جبر اقتصادی در آن دیده می‌شود.",
            "رسانهٔ عمومی و غیرتجاری را کم‌رنگ می‌کند.",
            "فعالیت و تفسیر مخاطب را نادیده می‌گیرد.",
            "مناسبات تولید معنا را ساده می‌کند.",
            "سنجش تجربی کالای مخاطب دشوار است.",
            "تفاوت بافت‌های ملی را کم‌رنگ می‌کند.",
        ],
        critique_text="منتقدان می‌گویند اسمایث رسانه را بیش از حد به منطق تبلیغات فرو می‌کاهد، فعالیت مخاطب و رسانهٔ عمومی را کم‌رنگ می‌کند و مناسبات پیچیدهٔ معنا را ساده می‌سازد؛ با این حال تحلیل او دربارهٔ کالاشدن توجه، بنیاد بحث کار دیجیتال و اقتصاد داده شد.",
        applications=[
            "تحلیل اقتصاد رسانهٔ تبلیغاتی.",
            "نقد سنجش مخاطب.",
            "پژوهش کار دیجیتال.",
            "مطالعهٔ اقتصاد داده.",
            "تحلیل پلتفرم اجتماعی.",
            "پژوهش رسانهٔ عمومی.",
            "مطالعهٔ تبلیغات تلویزیونی.",
            "تحلیل روزنامهٔ رایگان.",
            "پژوهش تجارت توجه.",
            "مطالعهٔ نظارت تجاری.",
            "تحلیل بازار تبلیغات دیجیتال.",
            "پژوهش کار کاربر.",
            "مطالعهٔ رسانهٔ بین‌المللی.",
            "پژوهش آموزش سیاست ارتباطات.",
            "تحلیل تلویزیون کابلی.",
            "سیاست‌گذاری رسانه.",
        ],
        example_text="تلویزیون تجاری نمونهٔ کلاسیک است: برنامه برای گردآوردن مخاطب ساخته می‌شود، دادهٔ تماشا به آگهی‌دهنده فروخته می‌شود و برنامه‌سازی تابع بازار توجه می‌شود؛ همین منطق در پلتفرم دیجیتال با داده و الگوریتم پیچیده‌تر شده است.",
        evolution="اسمایث از اقتصاد نهادی و سیاست‌گذاری ارتباطات آغاز کرد، در ۱۹۷۷ تز کالای مخاطب را مطرح کرد، در ۱۹۸۱ آن را به وابستگی جهانی گسترد، در دههٔ ۲۰۰۰ بحث کار دیجیتال بر او بنا شد و امروز در نقد اقتصاد داده و نظارت تجاری بازخوانی می‌شود.",
        key_concepts=["کالای مخاطب", "صنعت آگاهی", "کار مخاطب", "سرمایه‌داری انحصاری", "وابستگی", "اقتصاد توجه"],
        theorists="دالاس اسمایث.",
        theorists_text="دالاس اسمایث با اقتصاد سیاسی ارتباطات نشان داد چگونه توجه مخاطب به کالا بدل می‌شود و صنعت آگاهی را در مناسبات سرمایه‌داری و وابستگی جهانی جای داد.",
        model="مدل کالای مخاطب: محتوا مخاطب را گرد می‌آورد، سنجش، توجه را قابل‌فروش می‌کند و تبلیغ‌دهنده بهای دسترسی را می‌پردازد؛ در نسخهٔ دیجیتال، داده و رفتار کاربر مادهٔ خام این مبادله است.",
        studies=[
            "پژوهش کالای مخاطب.",
            "تحلیل اقتصاد تبلیغات.",
            "مطالعهٔ سنجش مخاطب.",
            "پژوهش کار دیجیتال.",
            "تحلیل اقتصاد داده.",
            "مطالعهٔ پلتفرم اجتماعی.",
            "پژوهش رسانهٔ عمومی.",
            "تحلیل تبلیغات تلویزیونی.",
            "مطالعهٔ روزنامهٔ رایگان.",
            "پژوهش تجارت توجه.",
            "تحلیل نظارت تجاری.",
            "مطالعهٔ بازار تبلیغات دیجیتال.",
            "پژوهش کار کاربر.",
            "تحلیل سیاست رسانه.",
        ],
    ),
    "th-38": dict(
        mapping=PERSON_MAPPING,
        summary="دیوید هزماندهالگ پژوهشگر بریتانیایی صنایع فرهنگی و اقتصاد سیاسی رسانه است. او در کتاب صنایع فرهنگی ۲۰۰۲ نشان داد که تولید کالاهای نمادین با خلاقیت نمادین، ریسک بالا، هزینهٔ ثابت زیاد و هزینهٔ تکثیر پایین مشخص می‌شود و همین ویژگی‌ها ساختار بازار، ستاره‌سازی و نابرابری درآمد را شکل می‌دهند. او مفهوم صنایع خلاق را به‌دلیل مبهم‌کردن مناسبات کار و قدرت نقد کرد و بر عدالت در کار فرهنگی تأکید گذاشت. در کار خلاق ۲۰۱۱ با سارا بیکر شرایط کار در موسیقی، روزنامه‌نگاری و تولید تلویزیون را بررسی کرد و در چرا موسیقی مهم است ۲۰۱۳ ارزش اجتماعی موسیقی را فراتر از بازار تحلیل کرد. پژوهش او دربارهٔ دیجیتالی‌شدن، جریان و پلتفرم‌ها، سیاست فرهنگی و آموزش رسانه اثرگذار بوده است و به پرسش از نقش عمومی رسانه و کیفیت کار فرهنگی در سیاست‌گذاری مربوط می‌شود. نقدها بر تمرکز بر بریتانیا، اصلاح‌طلبی در سیاست‌گذاری، سنجش دشوار عدالت کاری و کم‌رنگ‌شدن تنوع تجربهٔ جهانی تأکید دارند.",
        definition="صنایع فرهنگی مجموعهٔ فعالیت‌هایی هستند که با خلاقیت نمادین، متن و معنا تولید می‌کنند و با ریسک تقاضا، هزینهٔ ثابت بالا و تکثیر ارزان روبه‌رویند.",
        main_problem="تولید کالاهای نمادین در بازار چگونه سازمان می‌یابد و این سازمان‌دهی چه پیامدهایی برای معنا، کار و عدالت دارد.",
        mechanism="خلاقیت نمادین با ریسک تقاضا و هزینهٔ تکثیر پایین ترکیب می‌شود؛ شرکت‌ها با سبد تولید، ستاره‌سازی و کنترل توزیع ریسک را مدیریت می‌کنند و همین الگو نابرابری و تمرکز را بازتولید می‌کند.",
        assumptions=[
            "کالای فرهنگی معنادار و نمادین است.",
            "تقاضای فرهنگی به‌شدت نامطمئن است.",
            "هزینهٔ تکثیر پس از تولید پایین است.",
            "ریسک با سبد تولید مدیریت می‌شود.",
            "ستاره‌سازی بخشی از منطق بازار است.",
            "کار خلاق به عدالت نیاز دارد.",
            "سیاست فرهنگی بر بازار اثر می‌گذارد.",
            "دیجیتالی‌شدن مناسبات تولید را دگرگون می‌کند.",
        ],
        principles=[
            "ریسک تقاضا را در تحلیل بگنجان.",
            "کار خلاق را جدی بگیر.",
            "از زبان مبهم صنایع خلاق بپرهیز.",
            "عدالت کاری را معیار بسنج.",
            "تمرکز بازار را پایش کن.",
            "سیاست فرهنگی را نقد کن.",
            "ارزش اجتماعی را فراتر از بازار ببین.",
        ],
        critiques=[
            "تحلیل بر بریتانیا متمرکز است.",
            "سیاست‌گذاری پیشنهادی اصلاح‌طلبانه است.",
            "سنجش عدالت کاری دشوار می‌ماند.",
            "تنوع تجربهٔ جهانی کم‌رنگ می‌شود.",
            "مرز صنایع فرهنگی و خلاق مبهم است.",
            "نقش مخاطب در تولید معنا کم‌رنگ می‌شود.",
            "سرعت تحول پلتفرم از تحلیل جلو می‌زند.",
        ],
        critique_text="منتقدان می‌گویند چارچوب هزماندهالگ بر بریتانیا متمرکز است، سنجش عدالت کاری در آن دشوار می‌ماند و سیاست پیشنهادی آن اصلاح‌طلبانه است؛ با این حال پیوند خلاقیت نمادین، ریسک بازار و کار فرهنگی، چارچوبی نیرومند برای تحلیل رسانه فراهم می‌کند.",
        applications=[
            "سیاست صنایع فرهنگی.",
            "تحلیل بازار موسیقی.",
            "پژوهش کار روزنامه‌نگاری.",
            "مطالعهٔ تولید تلویزیون.",
            "تحلیل جریان و پلتفرم.",
            "پژوهش اقتصاد خلاق.",
            "مطالعهٔ حق‌الامتیاز موسیقی.",
            "تحلیل کار خلاق.",
            "پژوهش سیاست فرهنگی.",
            "مطالعهٔ نشر کتاب.",
            "تحلیل بازی دیجیتال.",
            "پژوهش آموزش رسانه.",
            "مطالعهٔ تبلیغات.",
            "تحلیل رادیو عمومی.",
            "تحلیل تنوع فرهنگی.",
        ],
        example_text="جریان موسیقی نمونهٔ روشنی است: هزینهٔ تولید و تکثیر پایین با ریسک تقاضا و قدرت چانه‌زنی پلتفرم تلاقی می‌کند؛ نتیجه، تمرکز درآمد نزد ستاره‌ها و فشار بر کار خلاق است، در حالی که دسترسی شنونده گسترده شده است.",
        evolution="هزماندهالگ از مطالعات فرهنگی و اقتصاد سیاسی موسیقی آغاز کرد، در ۲۰۰۲ چارچوب صنایع فرهنگی را منتشر کرد، در ۲۰۰۷ و ۲۰۱۳ آن را به‌روز کرد، در ۲۰۱۱ با کار خلاق به شرایط کار پرداخت و امروز در بحث پلتفرم، هوش مصنوعی و عدالت کاری بازخوانی می‌شود.",
        key_concepts=["صنایع فرهنگی", "خلاقیت نمادین", "ریسک تقاضا", "کار خلاق", "صنایع خلاق", "عدالت کاری"],
        theorists="دیوید هزماندهالگ.",
        theorists_text="دیوید هزماندهالگ با پیوند اقتصاد سیاسی و مطالعات فرهنگی، چارچوب صنایع فرهنگی را بر پایهٔ خلاقیت نمادین، ریسک و کار صورت‌بندی کرد و نقد عدالت‌محور بر سیاست صنایع خلاق نوشت.",
        model="مدل صنایع فرهنگی: خلاقیت نمادین + تقاضای نامطمئن + هزینهٔ تکثیر پایین؛ شرکت‌ها با سبد تولید و ستاره‌سازی ریسک را مدیریت می‌کنند و ساختار کار و درآمد را شکل می‌دهند.",
        studies=[
            "پژوهش صنایع فرهنگی.",
            "تحلیل بازار موسیقی.",
            "مطالعهٔ کار روزنامه‌نگاری.",
            "پژوهش تولید تلویزیون.",
            "تحلیل جریان پلتفرمی.",
            "مطالعهٔ اقتصاد خلاق.",
            "پژوهش حق‌الامتیاز.",
            "تحلیل کار خلاق.",
            "مطالعهٔ سیاست فرهنگی.",
            "پژوهش نشر کتاب.",
            "تحلیل بازی دیجیتال.",
            "مطالعهٔ آموزش رسانه.",
            "پژوهش تبلیغات.",
            "تحلیل تنوع فرهنگی.",
        ],
    ),
}

NAME_FIX = {}
YEAR_FIX = {
    "th-16": "no year change; lifespan 1890-1947 verified; anchors: Field Theory in Social Science (1951) and Lewin, Lippitt & White (1939)",
    "th-27": "no year change; card year 1957 matches Mythologies; anchors: Mythologies (Seuil, 1957) and Image, Music, Text (Fontana, 1977)",
    "th-32": "no year change; lifespan 1907-1992; anchors: Smythe (1977), Canadian Journal of Political and Social Theory 1(3), 1-27",
    "th-38": "no year change; born 1963 verified; anchors: The Cultural Industries (SAGE, 2002) and later editions; legacy Persian spelling of the surname left unchanged because no verified Persian rendering was found",
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
                                       "verified": n_verified, "batch": 191}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH191 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
