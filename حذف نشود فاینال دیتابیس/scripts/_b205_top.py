# -*- coding: utf-8 -*-
"""Batch 205: MC-678, MC-694, card-403 (FRAMEWORK)."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch205-20261117"
NOW = "2026-11-17 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch205.json"

S = {
    "MC-678": [
        dict(kind="BOOK",
             title_en="Remembering to Forget: Holocaust Memory through the Camera's Eye",
             title_fa="یادآوری برای فراموشی: حافظهٔ هولوکاست از دریچهٔ دوربین",
             authors="Barbie Zelizer", year=1998,
             publisher="University of Chicago Press",
             doi=None,
             url=None,
             language="en", isbn=None,
             citation="Zelizer, B. (1998). Remembering to Forget: Holocaust Memory through the Camera's Eye. Chicago: University of Chicago Press.",
             locator="book",
             locator_type="BOOK",
             supports="press photographs of liberation as agents of collective memory and forgetting",
             verified=True),
        dict(kind="BOOK",
             title_en="On Collective Memory",
             title_fa="دربارهٔ حافظهٔ جمعی",
             authors="Maurice Halbwachs", year=1992,
             publisher="University of Chicago Press",
             doi=None,
             url="https://press.uchicago.edu/ucp/books/book/chicago/O/bo3619875.html",
             language="en", isbn=None,
             citation="Halbwachs, M. (1992). On Collective Memory (L. A. Coser, Ed. & Trans.). Chicago: University of Chicago Press.",
             locator="book",
             locator_type="BOOK",
             supports="social frameworks of memory and the selectivity of collective recollection",
             verified=True),
    ],
    "MC-694": [
        dict(kind="REPORT",
             title_en="Many Voices, One World: Towards a New, More Just, and More Efficient World Information and Communication Order",
             title_fa="صداهای بسیار، یک جهان: به‌سوی نظم نوین، عادلانه‌تر و کارآمدتر اطلاعات و ارتباطات جهانی",
             authors="International Commission for the Study of Communication Problems; Seán MacBride", year=1980,
             publisher="UNESCO",
             doi=None,
             url="https://unesdoc.unesco.org/ark:/48223/pf0000372754",
             language="en", isbn=None,
             citation="International Commission for the Study of Communication Problems. (1980). Many Voices, One World: Towards a New, More Just, and More Efficient World Information and Communication Order. Paris: UNESCO.",
             locator="report",
             locator_type="BOOK",
             supports="analysis of global information imbalance and the NWICO proposals",
             verified=True),
        dict(kind="BOOK",
             title_en="The Global Media: The New Missionaries of Corporate Capitalism",
             title_fa="رسانه‌های جهانی: مبلغان تازهٔ سرمایه‌داری شرکتی",
             authors="Edward S. Herman; Robert W. McChesney", year=1997,
             publisher="Cassell",
             doi=None,
             url="https://archive.org/details/globalmedianewmi0000herm",
             language="en", isbn=None,
             citation="Herman, E. S., & McChesney, R. W. (1997). The Global Media: The New Missionaries of Corporate Capitalism. London: Cassell.",
             locator="book",
             locator_type="BOOK",
             supports="political-economy account of global media concentration after NWICO",
             verified=True),
    ],
    "card-403": [
        dict(kind="REPORT",
             title_en="Many Voices, One World: Towards a New, More Just, and More Efficient World Information and Communication Order",
             title_fa="صداهای بسیار، یک جهان: به‌سوی نظم نوین، عادلانه‌تر و کارآمدتر اطلاعات و ارتباطات جهانی",
             authors="International Commission for the Study of Communication Problems; Seán MacBride", year=1980,
             publisher="UNESCO",
             doi=None,
             url="https://unesdoc.unesco.org/ark:/48223/pf0000372754",
             language="en", isbn=None,
             citation="International Commission for the Study of Communication Problems. (1980). Many Voices, One World. Paris: UNESCO.",
             locator="report",
             locator_type="BOOK",
             supports="origin statement of the New World Information and Communication Order",
             verified=True),
        dict(kind="BOOK",
             title_en="The Global Media: The New Missionaries of Corporate Capitalism",
             title_fa="رسانه‌های جهانی: مبلغان تازهٔ سرمایه‌داری شرکتی",
             authors="Edward S. Herman; Robert W. McChesney", year=1997,
             publisher="Cassell",
             doi=None,
             url="https://archive.org/details/globalmedianewmi0000herm",
             language="en", isbn=None,
             citation="Herman, E. S., & McChesney, R. W. (1997). The Global Media: The New Missionaries of Corporate Capitalism. London: Cassell.",
             locator="book",
             locator_type="BOOK",
             supports="corporate concentration as the counter-force to a balanced information order",
             verified=True),
    ],
}

ENRICH = {
    "MC-678": dict(
        needs_enrichment=False,
        constructs=("• حافظهٔ جمعی: بازسازی گذشته در قالب‌های اجتماعی مشترک.\n"
                    "• فراموشی جمعی: حذف یا حاشیه‌رانی روایت‌ها از حافظهٔ عمومی.\n"
                    "• چارچوب حافظه: ساختار تفسیری که تعیین می‌کند چه چیزی به‌یاد بماند.\n"
                    "• آرشیو و آیین یادبود: نهادها و آیین‌هایی که حافظه را تثبیت می‌کنند.\n"
                    "• تصویر شاهد: عکس و فیلم به‌عنوان مدرک و چارچوب روایت گذشته."),
        core_logic="رسانه‌ها نه مجرای خنثای گذشته، بلکه عامل ساختن حافظه‌اند: انتخاب تصویر، چارچوب‌بندی روایت، تکرار آیینی در سالگردها و منطق آرشیو، برخی روایت‌ها را تثبیت و برخی را به حاشیه می‌راند؛ آنچه به‌یاد می‌ماند و آنچه فراموش می‌شود، پیامد قدرت است.",
        detailed_analysis=("۱. بنیان و منطق نظری\nچارچوب یادآوری و فراموشی جمعی ریشه در بحث هالبواکس (۱۹۹۲) دربارهٔ چارچوب‌های اجتماعی حافظه دارد: حافظه در خلأ فردی عمل نمی‌کند، بلکه در گروه‌ها، زبان و آیین‌ها شکل می‌گیرد و همواره گزینشی است. "
                           "زلایزر (۱۹۹۸) با تحلیل عکس‌های آزادسازی اردوگاه‌های هولوکاست نشان داد که مطبوعات با انتخاب و چیدمان تصویر، حافظهٔ عمومی را می‌سازند و در همان حال ابعادی از رنج را از دید خارج می‌کنند. "
                           "رسانه از این منظر نه کانال انتقال گذشته، بلکه صحنهٔ رقابت روایت‌ها و منافع است؛ آرشیو، سالگرد و آیین یادبود، سازوکارهای تثبیت یا حذف حافظه‌اند.\n\n"
                           "۲. کاربرد و نقد\nاین چارچوب در تحلیل پوشش جنگ، فاجعه و بحران، سیاست سالگرد و آرشیو دیجیتال به‌کار می‌رود و به پژوهشگر یادآوری می‌کند که پرسش «چه چیزی پوشش داده شد؟» را با پرسش «چه چیزی از حافظه حذف شد؟» کامل کند. "
                           "نقد اصلی، رسانه‌محوری بیش از اندازه، سوگیری انتخاب نمونه در مطالعات موردی و ابهام مفهومی حافظهٔ جمعی است؛ با این حال، پیوند آن با قدرت و روایت، همچنان یکی از پرثمرترین چارچوب‌های مطالعات رسانه است."),
        related_approaches="مطالعات حافظهٔ جمعی؛ تاریخ بصری؛ جامعه‌شناسی حافظه؛ تحلیل روایت؛ مطالعات آرشیو.",
        recommended_sources="«یادآوری برای فراموشی» (زلایزر، ۱۹۹۸)؛ «دربارهٔ حافظهٔ جمعی» (هالبواکس، ۱۹۹۲)؛ پژوهش‌های حافظهٔ اجتماعی و رسانه.",
    ),
    "MC-694": dict(
        needs_enrichment=False,
        level="کلان",
        summary="گزارش مک‌براید، سند سال ۱۹۸۰ سازمان آموزشی، علمی و فرهنگی ملل متحد است که با عنوان «صداهای بسیار، یک جهان: به‌سوی نظم اطلاعاتی و ارتباطی جهانی عادلانه‌تر و کارآمدتر» منتشر شد. این گزارش حاصل کار کمیسیون بین‌المللی مطالعهٔ مسائل ارتباطات بود که شان مک‌براید، سیاستمدار و حقوق‌دان ایرلندی، ریاست آن را بر عهده داشت. گزارش، نابرابری جریان اطلاعات میان شمال و جنوب را نقد کرد و خواستار نظم نوین اطلاعات و ارتباطات جهانی شد: تعادل جریان خبر، دسترسی برابر به فناوری، حق ارتباط، مشارکت جوامع محلی در تولید محتوا و کاهش تمرکز مالکیت رسانه. این سند به‌سرعت به نماد جدال سیاسی تبدیل شد؛ کشورهای در حال توسعه آن را برنامهٔ عدالت ارتباطی خواندند و دولت‌های غربی و شرکت‌های رسانه‌ای آن را تهدید آزادی مطبوعات دانستند. پیامد سیاسی آن، خروج دو کشور بزرگ از سازمان آموزشی و فرهنگی ملل متحد در میانهٔ دههٔ ۱۹۸۰ بود. با این حال، ایده‌های گزارش در بحث‌های بعدی دربارهٔ شکاف دیجیتال، تنوع رسانه‌ای، حق ارتباط و قدرت پلتفرم‌ها بازتاب یافت. اهمیت آن برای پژوهش رسانه، پیوند دادن ارتباطات با عدالت اجتماعی و سیاست جهانی است. نقدهای اصلی به آرمان‌گرایی، ابهام سازوکارهای اجرا و خطر تبدیل حق ارتباط به ابزار کنترل دولتی مربوط می‌شود.",
        constructs=("• نظم نوین اطلاعات و ارتباطات: مجموعهٔ اصول و سیاست‌هایی برای متعادل‌سازی جریان جهانی اطلاعات.\n"
                    "• حق ارتباط: حق همهٔ انسان‌ها برای بیان، دسترسی و مشارکت در ارتباطات.\n"
                    "• تعادل جریان خبر: کاهش سلطهٔ خبرگزاری‌های شمال بر روایت جنوب.\n"
                    "• تمرکز مالکیت رسانه: تجمع رسانه در دست شرکت‌های معدود و پیامد آن برای تنوع.\n"
                    "• عدالت ارتباطی: توزیع برابر فرصت‌های ارتباطی میان جوامع."),
        related_approaches="اقتصاد سیاسی رسانه؛ سیاست جهانی ارتباطات؛ عدالت ارتباطی؛ شکاف دیجیتال؛ مطالعات پسااستعماری.",
        recommended_sources="«صداهای بسیار، یک جهان» (گزارش مک‌براید، ۱۹۸۰)؛ «رسانه‌های جهانی» (هرمن و مک‌چزنی، ۱۹۹۷)؛ پژوهش‌های عدالت ارتباطی و شکاف دیجیتال.",
    ),
    "card-403": dict(
        needs_enrichment=False,
        level="کلان",
        definition="نظم نوین جهانی اطلاعات و ارتباطات، چارچوبی است که در دههٔ ۱۹۷۰ و ۱۹۸۰ برای تحلیل و اصلاح نابرابری جریان اطلاعات میان شمال و جنوب شکل گرفت و تعادل خبری، حق ارتباط و تنوع مالکیت رسانه را در کانون سیاست جهانی قرار داد.",
        summary="نظم نوین جهانی اطلاعات و ارتباطات، چارچوبی نظری در سطح کلان برای تحلیل قدرت، سیاست و حاکمیت رسانه است که از بحث‌های دههٔ ۱۹۷۰ دربارهٔ نابرابری جریان اطلاعات برخاست و در گزارش مک‌براید (۱۹۸۰) صورت‌بندی شد.",
        recommended_sources="«صداهای بسیار، یک جهان» (گزارش مک‌براید، ۱۹۸۰)؛ «رسانه‌های جهانی» (هرمن و مک‌چزنی، ۱۹۹۷)؛ اسناد یونسکو دربارهٔ نظم نوین اطلاعات و ارتباطات.",
        theorists_text="کمیسیون بین‌المللی مطالعهٔ مسائل ارتباطات به ریاست شان مک‌براید، با همکاری کارشناسان چند کشور، گزارش ۱۹۸۰ را تدوین کرد؛ این سند در سنت نقد اقتصاد سیاسی رسانه و بحث عدالت جهانی ارتباطات جای می‌گیرد.",
        studies=["گزارش سال ۱۹۸۰ کمیسیون بین‌المللی مطالعهٔ مسائل ارتباطات، نابرابری جریان خبر و پیشنهادهای نظم نوین را منتشر کرد.", "پژوهش‌های اقتصاد سیاسی رسانه، تمرکز مالکیت جهانی را به‌عنوان مانع اصلی تحقق این نظم تحلیل کردند."],
    ),
}

NAME_FIX = {}

YEAR_FIX = {
    "MC-678": "year=1998 (Zelizer 1998); Halbwachs 1992 verified; removed uses-and-gratifications template fields and irrelevant recommendations",
    "MC-694": "year=1980 (MacBride Report); Herman & McChesney 1997 verified; fixed title typo, removed interpersonal-communication template fields",
    "card-403": "year=1980 (MacBride Report); added definition, citations, recommendations and theorist text; removed interpersonal misfire",
}
