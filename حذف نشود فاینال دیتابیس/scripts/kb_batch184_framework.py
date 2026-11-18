# -*- coding: utf-8 -*-
"""Batch 184 (PUBLICATION): pub-icjr, pub-joc, pub-journal-adv-studies, pub-journalism-studies."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch184-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch184.json"

PUBLICATION_MAPPING = {"entity_type": "PUBLICATION", "content_type": "نشریه (Publication)", "needs_review": False}

S = {
    "pub-icjr": [
        dict(kind="OTHER",
             title_en="International Journal of Communication",
             title_fa="مجلهٔ بین‌المللی ارتباطات",
             authors="USC Annenberg Press", year=2007,
             publisher="USC Annenberg Press",
             doi=None,
             url="https://ijoc.org/index.php/ijoc/about",
             language="en", isbn=None,
             citation="International Journal of Communication (IJoC). Los Angeles: USC Annenberg Press, since 2007.",
             locator="journal about page", locator_type="web_page",
             supports="open-access, interdisciplinary communication journal founded 2007", verified=True),
        dict(kind="WEBSITE",
             title_en="International Journal of Communication announces new editor",
             title_fa="اعلام سردبیر جدید مجلهٔ بین‌المللی ارتباطات",
             authors="USC Annenberg", year=2024,
             publisher="USC Annenberg News",
             doi=None,
             url="https://annenberg.usc.edu/news/research-and-impact/international-journal-communication-announces-new-editor",
             language="en", isbn=None,
             citation="USC Annenberg (2024). International Journal of Communication announces new editor. Annenberg News.",
             locator="news article", locator_type="web_page",
             supports="journal launched at USC Annenberg in 2007", verified=True),
    ],
    "pub-joc": [
        dict(kind="OTHER",
             title_en="Journal of Communication",
             title_fa="مجلهٔ ارتباطات",
             authors="International Communication Association", year=1951,
             publisher="Oxford University Press / International Communication Association",
             doi=None,
             url="https://onlinelibrary.wiley.com/journal/14602466",
             language="en", isbn=None,
             citation="Journal of Communication. International Communication Association (ISSN 0021-9916; online 1460-2466).",
             locator="journal record", locator_type="web_page",
             supports="flagship ICA journal with print ISSN 0021-9916", verified=True),
        dict(kind="WEBSITE",
             title_en="ICA History",
             title_fa="تاریخ انجمن ارتباطات بین‌المللی",
             authors="International Communication Association", year=2024,
             publisher="ICA",
             doi=None,
             url="https://www.icahdq.org/page/History",
             language="en", isbn=None,
             citation="International Communication Association. History. ICA website.",
             locator="history page", locator_type="web_page",
             supports="first issue of the Journal of Communication published in 1951", verified=True),
    ],
    "pub-journal-adv-studies": [
        dict(kind="OTHER",
             title_en="Journal of Advertising",
             title_fa="مجلهٔ تبلیغات",
             authors="Taylor & Francis", year=1972,
             publisher="Taylor & Francis",
             doi=None,
             url="https://library.wur.nl/WebQuery/eurbrowser/2303",
             language="en", isbn=None,
             citation="Journal of Advertising. Taylor & Francis (ISSN 0091-3367; online 1557-7805), since 1972.",
             locator="journal record", locator_type="web_page",
             supports="advertising theory journal published since 1972", verified=True),
        dict(kind="WEBSITE",
             title_en="Journal of Advertising: Scope and Submission Guide",
             title_fa="مجلهٔ تبلیغات: دامنه و راهنمای ارسال",
             authors="CASRAI", year=2026,
             publisher="CASRAI",
             doi=None,
             url="https://casrai.org/guides/journal-of-advertising",
             language="en", isbn=None,
             citation="CASRAI. Journal of Advertising: Scope and Submission Guide. CASRAI website.",
             locator="guide page", locator_type="web_page",
             supports="print ISSN 0091-3367 and hybrid open-access model under Taylor & Francis", verified=True),
    ],
    "pub-journalism-studies": [
        dict(kind="OTHER",
             title_en="Journalism Studies",
             title_fa="مطالعات روزنامه‌نگاری",
             authors="Taylor & Francis", year=2000,
             publisher="Routledge / Taylor & Francis",
             doi=None,
             url="https://www.taylorfrancis.com/series/journalism-studies-bob-franklin/JOURNALISM",
             language="en", isbn=None,
             citation="Journalism Studies. Routledge / Taylor & Francis (ISSN 1461-670X; online 1469-9699), since 2000.",
             locator="journal series page", locator_type="web_page",
             supports="journal established at the turn of the millennium by Bob Franklin", verified=True),
        dict(kind="WEBSITE",
             title_en="ISSN 1469-9699 - Journalism Studies (Online)",
             title_fa="شمارهٔ استاندارد بین‌المللی مطالعات روزنامه‌نگاری",
             authors="ISSN International Centre", year=2026,
             publisher="ISSN Portal",
             doi=None,
             url="https://portal.issn.org/resource/ISSN/1469-9699",
             language="en", isbn=None,
             citation="ISSN International Centre. Journalism Studies (Online), ISSN 1469-9699, 2000-.",
             locator="ISSN record", locator_type="web_page",
             supports="registration of the online edition and volume years", verified=True),
    ],
}

ENRICH = {
    "pub-icjr": dict(
        year=2007,
        mapping=PUBLICATION_MAPPING,
        summary="مجلهٔ بین‌المللی ارتباطات نشریه‌ای دانشگاهی و دسترسی‌آزاد است که از ۲۰۰۷ در مطبوعات دانشگاه کالیفرنیای جنوبی منتشر می‌شود. این نشریه با هدف فراهم کردن بستری چندرشته‌ای برای پژوهش ارتباطات تأسیس شد و از همان آغاز به صورت برخط و بدون هزینهٔ اشتراک در دسترس بود. دامنهٔ آن نظریهٔ ارتباطات، رسانه، فرهنگ، فناوری، سیاست و روش‌شناسی را در بر می‌گیرد و مقاله‌های تجربی و نظری هر دو پذیرفته می‌شوند. ساختار آن شامل بخش مقاله‌های داوری‌شده، شماره‌های ویژه و بخش‌های کوتاه‌تر است. ویراستاران آن از دانشگاه‌های گوناگون انتخاب می‌شوند و هیئت تحریریهٔ بین‌المللی بر تنوع موضوعی و جغرافیایی تأکید دارد. در پژوهش رسانه، این نشریه به سبب دسترسی آزاد و سرعت انتشار، محل انتشار پژوهش‌های روش‌شناختی و میان‌رشته‌ای است. دسترسی آزاد آن برای پژوهشگران کشورهای کمتر برخوردار و فارسی‌زبان فرصت پیگیری و انتشار پژوهش‌های جهانی را آسان‌تر کرده است. بخش‌های کوتاه‌تر نشریه نیز به یافته‌های مقدماتی و نقد کتاب اختصاص دارد. نقدها بر حجم بالای مقاله و گزینش‌گری پنهان در نشریات دسترسی‌آزاد تأکید دارند.",
        definition="مجلهٔ بین‌المللی ارتباطات نشریه‌ای دانشگاهی و دسترسی‌آزاد در حوزهٔ ارتباطات است که از ۲۰۰۷ با داوری همتا و دامنهٔ میان‌رشته‌ای منتشر می‌شود.",
        main_problem="چگونه می‌توان پژوهش ارتباطات را بدون مانع اشتراک و با دامنه‌ای چندرشته‌ای در اختیار پژوهشگران جهان قرار داد و سرعت گردش دانش را افزایش داد.",
        mechanism="مقاله‌ها پس از داوری همتا و ویرایش در قالب برخط منتشر می‌شوند؛ دسترسی آزاد و نمایه‌سازی گسترده، گردش یافته‌ها را سریع‌تر می‌کند و شماره‌های ویژه، پژوهش‌های میان‌رشته‌ای را گرد هم می‌آورند.",
        assumptions=[
            "دانش ارتباطات باید آزادانه در دسترس باشد.",
            "داوری همتا کیفیت را تضمین می‌کند.",
            "میان‌رشته‌ای بودن به فهم رسانه کمک می‌کند.",
            "انتشار برخط زمان گردش دانش را کوتاه می‌کند.",
            "تنوع جغرافیایی هیئت تحریریه مهم است.",
            "شمارهٔ ویژه می‌تواند میدان پژوهشی بسازد.",
            "نمایه‌سازی دیده‌شدن مقاله را زیاد می‌کند.",
            "دسترسی آزاد نابرابری علمی را کاهش می‌دهد.",
        ],
        principles=[
            "داوری همتا را شفاف اجرا کن.",
            "دسترسی آزاد را حفظ کن.",
            "تنوع موضوعی و جغرافیایی را بپذیر.",
            "شمارهٔ ویژه را هدفمند طراحی کن.",
            "اخلاق پژوهش را پایش کن.",
            "زمان داوری را کوتاه نگه دار.",
            "پیوند نظریه و روش را تشویق کن.",
        ],
        critiques=[
            "حجم بالای مقاله کیفیت داوری را تهدید می‌کند.",
            "دسترسی آزاد بدون هزینه، پایداری مالی را دشوار می‌کند.",
            "تمرکز بر نویسندگان انگلیسی‌زبان باقی می‌ماند.",
            "شماره‌های ویژه گاه به شبکهٔ سردبیران وابسته‌اند.",
            "معیارهای پذیرش همیشه صریح نیست.",
            "سرعت انتشار می‌تواند عمق داوری را کم کند.",
            "نمایه‌سازی بر انتخاب موضوع اثر می‌گذارد.",
        ],
        critique_text="منتقدان می‌گویند نشریات دسترسی‌آزاد با حجم بالای مقاله، پایداری مالی و عمق داوری را به چالش می‌کشند و تمرکز بر نویسندگان انگلیسی‌زبان باقی می‌ماند؛ با این حال مجلهٔ بین‌المللی ارتباطات دسترسی به پژوهش ارتباطات را برای پژوهشگران کشورهای کمتر برخوردار آسان‌تر کرده است.",
        applications=[
            "انتشار پژوهش روش‌های ترکیبی.",
            "مطالعهٔ سیاست رسانه.",
            "پژوهش ارتباطات سلامت.",
            "تحلیل رسانهٔ دیجیتال.",
            "مطالعهٔ ارتباطات بین‌فرهنگی.",
            "پژوهش روزنامه‌نگاری.",
            "تحلیل سیاست اینترنت.",
            "مطالعهٔ ارتباطات سیاسی.",
            "پژوهش مخاطب.",
            "تحلیل صنعت رسانه.",
            "مطالعهٔ اخلاق رسانه.",
            "پژوهش ارتباطات بحران.",
            "تحلیل تاریخ رسانه.",
        ],
        example_text="پژوهشگری مقاله‌ای دربارهٔ الگوریتم‌های خبری را در این نشریه منتشر می‌کند و چون مقاله دسترسی‌آزاد است، پژوهشگران کشورهای دیگر بی‌واسطه آن را می‌خوانند و در طرح‌های تطبیقی به کار می‌گیرند؛ گردش سریع یافته به اصلاح روش در پژوهش‌های بعدی می‌انجامد.",
        evolution="این نشریه در ۲۰۰۷ در دانشگاه کالیفرنیای جنوبی راه‌اندازی شد، در دههٔ ۲۰۱۰ با نمایه‌سازی بین‌المللی رشد کرد و امروز در کنار نسخهٔ برخط، شماره‌های ویژه و بخش‌های میان‌رشته‌ای را منتشر می‌کند.",
        key_concepts=["دسترسی آزاد", "داوری همتا", "میان‌رشته‌ای", "نمایه‌سازی", "شمارهٔ ویژه", "اخلاق نشر"],
        theorists="لری گراس و هیئت تحریریهٔ بین‌المللی.",
        theorists_text="لری گراس از دانشگاه کالیفرنیای جنوبی نخستین سردبیر بود و سنت دسترسی آزاد و دامنهٔ میان‌رشته‌ای را در نشریه نهاد.",
        model="مدل نشریهٔ دسترسی‌آزاد: داوری همتا، انتشار برخط و نمایه‌سازی، گردش دانش را سریع و کم‌هزینه می‌کند و شماره‌های ویژه میدان‌های پژوهشی را شکل می‌دهند.",
        studies=[
            "مقاله‌های بنیان‌گذار سال ۲۰۰۷.",
            "شماره‌های ویژهٔ روش‌شناسی.",
            "پژوهش سیاست رسانه.",
            "مطالعهٔ ارتباطات سلامت.",
            "تحلیل رسانهٔ دیجیتال.",
            "پژوهش ارتباطات بین‌فرهنگی.",
            "تحلیل روزنامه‌نگاری.",
            "مطالعهٔ سیاست اینترنت.",
            "پژوهش مخاطب.",
            "تحلیل صنعت رسانه.",
            "مطالعهٔ اخلاق رسانه.",
            "پژوهش بحران ارتباطی.",
            "تحلیل تاریخ رسانه.",
            "مطالعهٔ ارتباطات سیاسی.",
        ],
    ),
    "pub-joc": dict(
        year=1951,
        mapping=PUBLICATION_MAPPING,
        summary="مجلهٔ ارتباطات نشریهٔ رسمی انجمن ارتباطات بین‌المللی است که از ۱۹۵۱ منتشر می‌شود و یکی از معتبرترین نشریات حوزهٔ ارتباطات به شمار می‌رود. این نشریه در آغاز درون انجمن و پس از آن با ناشران دانشگاهی منتشر شد و امروز با داوری همتا و نمایه‌سازی گسترده در دسترس است. دامنهٔ آن نظریهٔ ارتباطات، روان‌شناسی رسانه، ارتباطات سیاسی، سلامت، میان‌فردی و روش‌شناسی را در بر می‌گیرد. مجلهٔ ارتباطات محل انتشار پژوهش‌های بنیادی و مرورهایی است که چارچوب‌های نظری حوزه را شکل داده‌اند. سیاست تحریریه بر کیفیت نظری، نوآوری روش و اهمیت عمومی تأکید دارد. پژوهشگران برای انتشار یافته‌های دارای پیامد نظری گسترده این نشریه را برمی‌گزینند. مجلهٔ ارتباطات علاوه بر مقاله‌های تجربی، میزبان مناظره‌های نظری و شماره‌های ویژه دربارهٔ وضعیت حوزه است. بسیاری از چارچوب‌های مرجع مانند نظریه‌های اثرات رسانه و ارتباطات سلامت نخست در همین نشریه صورت‌بندی و سپس در کتاب‌های درسی بازتاب یافته‌اند. برای پژوهشگران فارسی‌زبان، دسترسی به آن به‌سبب اشتراک کتابخانه‌های دانشگاهی گاه دشوار است. نقدها بر کندی داوری، تمرکز بر نویسندگان شناخته‌شده و فشار شاخص‌های استنادی تأکید دارند.",
        definition="مجلهٔ ارتباطات نشریهٔ علمی داوری‌شدهٔ انجمن ارتباطات بین‌المللی است که از ۱۹۵۱ پژوهش‌های بنیادی و نظری ارتباطات را منتشر می‌کند.",
        main_problem="چگونه می‌توان یافته‌های پژوهشی ارتباطات را با معیار نظری بالا گرد آورد و مرجع مشترکی برای انباشت دانش این حوزه فراهم کرد.",
        mechanism="مقاله‌ها با داوری همتا، ویرایش تخصصی و نمایه‌سازی در پایگاه‌های استنادی منتشر می‌شوند؛ شماره‌های موضوعی و مرورهای نظری، ادبیات حوزه را انسجام می‌بخشند و استناد متقابل، اقتدار علمی نشریه را تقویت می‌کند.",
        assumptions=[
            "داوری همتا کیفیت نظری را تضمین می‌کند.",
            "انباشت دانش به مرجع مشترک نیاز دارد.",
            "پیوند نظریه و داده ارزشمند است.",
            "اهمیت عمومی یافته معیار پذیرش است.",
            "نمایه‌سازی دیده‌شدن پژوهش را زیاد می‌کند.",
            "مرور نظری پیشرفت حوزه را ممکن می‌کند.",
            "استاندارد روش‌شناختی قابل اجراست.",
            "هیئت تحریریه نمایندهٔ حوزه است.",
        ],
        principles=[
            "کیفیت نظری را بر سرعت ترجیح بده.",
            "داوری را دو سوکور اجرا کن.",
            "نوآوری روش را تشویق کن.",
            "پیامد عمومی یافته را بسنج.",
            "تعارض منافع را شفاف کن.",
            "مرور نظری را جدی بگیر.",
            "استاندارد گزارش‌دهی را الزامی کن.",
        ],
        critiques=[
            "فرایند داوری کند و پرهزینه است.",
            "شبکهٔ نویسندگان شناخته‌شده مزیت دارد.",
            "فشار شاخص استنادی انتخاب موضوع را تحریف می‌کند.",
            "پژوهش‌های تکرارشونده کمتر پذیرفته می‌شوند.",
            "تمرکز بر انگلیسی، تنوع زبانی را محدود می‌کند.",
            "منطق نشریه‌محور دانش را قطعه‌قطعه می‌کند.",
            "دسترسی اشتراکی نابرابری خواندن می‌سازد.",
        ],
        critique_text="منتقدان می‌گویند نشریات معتبر با داوری کند، مزیت نویسندگان شناخته‌شده و فشار شاخص استنادی، تنوع و تکرارپذیری پژوهش را محدود می‌کنند؛ با این حال مجلهٔ ارتباطات همچنان مرجع اصلی انباشت نظری در حوزهٔ ارتباطات است.",
        applications=[
            "انتشار نظریهٔ ارتباطات.",
            "پژوهش روان‌شناسی رسانه.",
            "مطالعهٔ ارتباطات سیاسی.",
            "تحلیل ارتباطات سلامت.",
            "پژوهش ارتباط میان‌فردی.",
            "مرور نظری حوزه.",
            "مطالعهٔ اثرات رسانه.",
            "پژوهش روش‌شناسی.",
            "تحلیل ارتباطات سازمانی.",
            "مطالعهٔ افکار عمومی.",
            "پژوهش رسانه و نوجوان.",
            "تحلیل گفت‌وگوی عمومی.",
            "مطالعهٔ ارتباطات بین‌فرهنگی.",
        ],
        example_text="پژوهشی دربارهٔ اثر مواجههٔ انتخابی بر قطب‌بندی نگرش، پس از سه دور داوری و اصلاح روش نمونه‌گیری در این نشریه منتشر می‌شود و به سبب اقتدار نشریه، به سرعت در طرح‌های بعدی نقل می‌شود.",
        evolution="نخستین شماره در ۱۹۵۱ منتشر شد، نشریه در نیمهٔ دوم قرن بیستم به مرجع نظری حوزه بدل شد، در دههٔ ۲۰۰۰ با ناشران دانشگاهی و نسخهٔ برخط گسترش یافت و امروز همچنان از پرارجاع‌ترین نشریات ارتباطات است.",
        key_concepts=["داوری همتا", "نظریهٔ ارتباطات", "مرور نظری", "شاخص استنادی", "اهمیت عمومی", "اخلاق نشر"],
        theorists="ویراستاران انجمن ارتباطات بین‌المللی.",
        theorists_text="هیئت‌های تحریریهٔ متوالی انجمن ارتباطات بین‌المللی استاندارد نظری و روش‌شناختی نشریه را در طول دهه‌ها شکل دادند.",
        model="مدل نشریهٔ مرجع: داوری سخت‌گیرانه، مرور نظری و نمایه‌سازی، نشریه را به مرکز اقتدار علمی و انباشت دانش حوزه بدل می‌کند.",
        studies=[
            "نخستین شماره در ۱۹۵۱.",
            "مرورهای نظری ارتباطات.",
            "پژوهش اثرات رسانه.",
            "مطالعهٔ ارتباطات سیاسی.",
            "تحلیل ارتباطات سلامت.",
            "پژوهش روان‌شناسی رسانه.",
            "مطالعهٔ ارتباط میان‌فردی.",
            "تحلیل افکار عمومی.",
            "پژوهش رسانه و نوجوان.",
            "مطالعهٔ ارتباط سازمانی.",
            "تحلیل گفت‌وگوی عمومی.",
            "پژوهش روش‌شناسی.",
            "مطالعهٔ مواجههٔ انتخابی.",
            "تحلیل ارتباطات بین‌فرهنگی.",
        ],
    ),
    "pub-journal-adv-studies": dict(
        year=1972,
        mapping=PUBLICATION_MAPPING,
        summary="مجلهٔ تبلیغات نشریه‌ای علمی و داوری‌شده است که از ۱۹۷۲ منتشر می‌شود و به توسعهٔ نظریهٔ تبلیغات و پیوند آن با عمل حرفه‌ای اختصاص دارد. این نشریه پژوهش‌های کمی و کیفی دربارهٔ اثر تبلیغ، رفتار مصرف‌کننده، خلاقیت، رسانه و اخلاق تبلیغاتی را می‌پذیرد. ساختار آن شامل مقاله‌های تجربی، مرور و پژوهش‌های کاربردی است و شماره‌های ویژه به موضوع‌های نوظهور می‌پردازد. سیاست تحریریه بر استحکام روش، سهم نظری و کاربرد مدیریتی تأکید دارد. پژوهشگران ارتباطات بازاریابی، روان‌شناسی مصرف و سیاست‌گذاری تبلیغات از مخاطبان اصلی آن‌اند. نشریه هم مقاله‌های کمّی آزمایشی و هم پژوهش‌های کیفی دربارهٔ معنا و مصرف را می‌پذیرد و در سال‌های اخیر به تبلیغات برنامه‌ریزی‌شده با داده و مسئولیت اجتماعی برند نیز پرداخته است. برای پژوهشگران فارسی‌زبان، الگوی گزارش‌دهی و معیارهای روشی آن مرجعی برای طراحی پیمایش و آزمایش تبلیغاتی است. شماره‌های ویژهٔ آن دربارهٔ تبلیغات دیجیتال و هوش مصنوعی مرزهای تازهٔ حوزه را نشان می‌دهد. نقدها بر هم‌راستایی با منافع صنعت، کم‌توجهی به پیامدهای اجتماعی تبلیغ و فشار شاخص‌های استنادی تأکید دارند.",
        definition="مجلهٔ تبلیغات نشریهٔ علمی داوری‌شده‌ای است که از ۱۹۷۲ نظریه، روش و کاربرد پژوهش تبلیغات را منتشر می‌کند.",
        main_problem="چگونه می‌توان پژوهش تبلیغات را از وابستگی صرف به گزارش‌های صنعتی رهاند، به نظریهٔ آزمون‌پذیر پیوند زد و در همان حال برای عمل حرفه‌ای سودمند ساخت.",
        mechanism="مقاله‌ها با داوری همتا و ویرایش تخصصی منتشر می‌شوند؛ شماره‌های ویژه موضوع‌های نوظهور را گرد می‌آورند و پیوند نظریه، داده و کاربرد مدیریتی، دانش تبلیغات را انباشته می‌کند.",
        assumptions=[
            "تبلیغ پدیده‌ای نظریه‌پذیر است.",
            "روش تجربی به فهم اثر کمک می‌کند.",
            "پیوند پژوهش و عمل تبلیغاتی ارزشمند است.",
            "مصرف‌کننده کنشگری تفسیرگر است.",
            "اخلاق تبلیغات موضوع پژوهش است.",
            "رسانه و قالب بر اثر تبلیغ اثر دارد.",
            "داوری همتا کیفیت را تضمین می‌کند.",
            "کاربرد مدیریتی معیار پذیرش است.",
        ],
        principles=[
            "سهم نظری مقاله را روشن کن.",
            "روش و نمونه را شفاف گزارش کن.",
            "پیامد اخلاقی را بررسی کن.",
            "کاربرد مدیریتی را نشان بده.",
            "تعارض منافع با صنعت را افشا کن.",
            "قالب رسانه‌ای را در تحلیل بگنجان.",
            "اثر بلندمدت را نیز بسنج.",
        ],
        critiques=[
            "با منافع صنعت تبلیغات هم‌راستا می‌شود.",
            "پیامدهای اجتماعی تبلیغ را کم‌برآورد می‌کند.",
            "تمرکز بر اثر کوتاه‌مدت فروش غالب است.",
            "نمونهٔ راحت‌الوصول تعمیم را محدود می‌کند.",
            "فشار شاخص استنادی موضوع را تحریف می‌کند.",
            "اخلاق تبلیغات اغلب حاشیه‌ای می‌ماند.",
            "تنوع فرهنگی در پژوهش این نشریه کم است.",
        ],
        critique_text="منتقدان می‌گویند پژوهش تبلیغات در این نشریه گاه با منافع صنعت هم‌راستا می‌شود، بر اثر کوتاه‌مدت فروش متمرکز می‌ماند و پیامدهای اجتماعی و اخلاقی را کم‌برآورد می‌کند؛ با این حال نشریه استاندارد نظری و روشی پژوهش تبلیغات را بالا برده است.",
        applications=[
            "سنجش اثر آگهی تلویزیونی.",
            "پژوهش تبلیغات دیجیتال.",
            "مطالعهٔ رفتار مصرف‌کننده.",
            "تحلیل خلاقیت تبلیغاتی.",
            "پژوهش برند.",
            "مطالعهٔ تبلیغات سیاسی.",
            "تحلیل اخلاق تبلیغ.",
            "پژوهش تبلیغات سلامت.",
            "مطالعهٔ قالب بومی.",
            "تحلیل بازاریابی شبکهٔ اجتماعی.",
            "پژوهش مخاطب هدف.",
            "تحلیل تبلیغات خیریه.",
            "مطالعهٔ تبلیغات کودکان.",
            "مطالعهٔ تبلیغات محیطی.",
        ],
        example_text="پژوهشی دو نسخهٔ یک آگهی را با قالب روایی و آماری مقایسه می‌کند، اثر آن را بر یادآوری و قصد خرید می‌سنجد و پس از داوری، پیامد مدیریتی و محدودیت اخلاقی کاربرد آن را گزارش می‌کند.",
        evolution="نشریه در ۱۹۷۲ راه‌اندازی شد، در دههٔ ۱۹۸۰ و ۱۹۹۰ با رشد پژوهش مصرف‌کننده تثبیت شد، از دههٔ ۲۰۰۰ تبلیغات دیجیتال و شبکهٔ اجتماعی به دامنهٔ آن افزوده شد و امروز با دسترسی ترکیبی منتشر می‌شود.",
        key_concepts=["اثر تبلیغ", "قصد خرید", "خلاقیت تبلیغاتی", "برند", "اخلاق تبلیغ", "مخاطب هدف"],
        theorists="هیئت تحریریهٔ مجلهٔ تبلیغات.",
        theorists_text="ویراستاران متوالی نشریه استاندارد پژوهش تجربی و نظری تبلیغات را شکل دادند و پیوند آن با عمل حرفه‌ای را حفظ کردند.",
        model="مدل پژوهش تبلیغات: نظریهٔ اثر، دادهٔ تجربی و پیامد مدیریتی در یک چرخهٔ انتشار و کاربرد به هم پیوند می‌خورند.",
        studies=[
            "مقاله‌های نخستین دوره.",
            "پژوهش اثر آگهی تلویزیونی.",
            "تحلیل تبلیغات دیجیتال.",
            "مطالعهٔ رفتار مصرف‌کننده.",
            "پژوهش خلاقیت تبلیغاتی.",
            "تحلیل برند.",
            "مطالعهٔ تبلیغات سیاسی.",
            "پژوهش اخلاق تبلیغ.",
            "تحلیل تبلیغات سلامت.",
            "مطالعهٔ قالب بومی.",
            "پژوهش بازاریابی شبکهٔ اجتماعی.",
            "تحلیل تبلیغات خیریه.",
            "مطالعهٔ تبلیغات کودکان.",
            "پژوهش اثر بلندمدت.",
        ],
    ),
    "pub-journalism-studies": dict(
        year=2000,
        mapping=PUBLICATION_MAPPING,
        summary="مطالعات روزنامه‌نگاری نشریه‌ای علمی و داوری‌شده است که در آغاز هزارهٔ سوم با تلاش باب فرانکلین راه‌اندازی شد و به مطالعهٔ انتقادی روزنامه‌نگاری اختصاص دارد. دامنهٔ آن نظریهٔ خبر، اخلاق حرفه‌ای، اقتصاد رسانه، فناوری انتشار، مخاطب و روش‌های پژوهش روزنامه‌نگاری را در بر می‌گیرد. نشریه به‌سرعت به یکی از مراجع اصلی حوزهٔ مطالعات روزنامه‌نگاری بدل شد و پژوهش‌های بین‌المللی و تطبیقی را تشویق می‌کند. ساختار آن شامل مقاله‌های تجربی، مرور و شماره‌های ویژه است و شمارهٔ برخط آن از ۲۰۰۰ ثبت شده است. سیاست تحریریه بر استقلال حرفه‌ای، تنوع جغرافیایی و پیوند پژوهش با بحران‌های واقعی روزنامه‌نگاری تأکید دارد. نشریه در سال‌های اخیر شماره‌هایی دربارهٔ بحران اعتماد، تحولات پلتفرمی و روزنامه‌نگاری داده منتشر کرده و برای پژوهشگران فارسی‌زبان الگویی برای پیوند نقد حرفه‌ای با دادهٔ میدانی فراهم می‌کند. شماره‌های تطبیقی آن به مقایسهٔ نظام‌های خبری کشورهای گوناگون می‌پردازد و دسترسی به شماره‌های قدیمی از راه آرشیو ناشر ممکن است. نقدها بر تمرکز بر رسانه‌های غربی، فشار شاخص استنادی و کندی داوری تأکید دارند.",
        definition="مطالعات روزنامه‌نگاری نشریهٔ علمی داوری‌شده‌ای است که از ۲۰۰۰ پژوهش نظری و تجربی دربارهٔ خبر، حرفه و نهاد روزنامه‌نگاری را منتشر می‌کند.",
        main_problem="چگونه می‌توان روزنامه‌نگاری را هم‌زمان به‌عنوان حرفه، نهاد و متن مطالعه کرد و پاسخ پژوهشی برای بحران‌های اعتماد، اقتصاد و فناوری خبر ساخت.",
        mechanism="مقاله‌ها با داوری همتا منتشر می‌شوند؛ دامنهٔ میان‌رشته‌ای، پژوهش‌های جامعه‌شناختی، تاریخی و اقتصادی خبر را کنار هم می‌نشاند و شماره‌های ویژه، بحران‌های جاری حوزه را به پرسش پژوهشی بدل می‌کنند.",
        assumptions=[
            "روزنامه‌نگاری نهاد اجتماعی است.",
            "خبر برساخته و قابل تحلیل است.",
            "استقلال حرفه‌ای ارزش پژوهشی دارد.",
            "فناوری سازمان خبر را تغییر می‌دهد.",
            "مخاطب در تولید خبر نقش دارد.",
            "اخلاق حرفه‌ای موضوع پژوهش است.",
            "مطالعهٔ تطبیقی به فهم خبر کمک می‌کند.",
            "داوری همتا کیفیت را تضمین می‌کند.",
        ],
        principles=[
            "پیوند نظریه و میدان خبر را روشن کن.",
            "روش و نمونه را شفاف گزارش کن.",
            "بافت ملی و تطبیقی را بگنجان.",
            "اخلاق حرفه‌ای را بررسی کن.",
            "نقش فناوری را در تحلیل بیاور.",
            "تعارض منافع را افشا کن.",
            "یافته را به سیاست خبر پیوند بزن.",
        ],
        critiques=[
            "بر رسانه‌های غربی متمرکز می‌ماند.",
            "فشار شاخص استنادی موضوع را تحریف می‌کند.",
            "داوری آن کند است.",
            "پژوهش‌های تکرارشونده کمتر پذیرفته می‌شوند.",
            "بحران اقتصادی خبر را کم‌برآورد می‌کند.",
            "به تجربهٔ روزنامه‌نگاران کمتر می‌پردازد.",
            "دسترسی اشتراکی خواندن را محدود می‌کند.",
        ],
        critique_text="منتقدان می‌گویند مطالعات روزنامه‌نگاری همچنان بر رسانه‌های غربی متمرکز است، تحت فشار شاخص استنادی به موضوع‌های جذاب گرایش دارد و تجربهٔ زیستهٔ روزنامه‌نگاران را کم‌برآورد می‌کند؛ با این حال نشریه مرجع اصلی پژوهش انتقادی خبر شده است.",
        applications=[
            "پژوهش تحریریهٔ خبر.",
            "مطالعهٔ اعتماد به خبر.",
            "تحلیل خبر جعلی.",
            "پژوهش اقتصاد خبر.",
            "مطالعهٔ روزنامه‌نگاری داده.",
            "تحلیل اخلاق خبر.",
            "پژوهش خبر و شبکهٔ اجتماعی.",
            "مطالعهٔ تطبیقی خبر.",
            "تحلیل حرفه‌ای‌شدن روزنامه‌نگار.",
            "پژوهش خبر محلی.",
            "مطالعهٔ آزادی مطبوعات.",
            "تحلیل خبر بحران.",
            "پژوهش مخاطب خبر.",
        ],
        example_text="پژوهشی تحریریه‌های سه کشور را مقایسه می‌کند و نشان می‌دهد سنجه‌های تحلیلی ترافیک چگونه اولویت خبری را از گزارش تحقیقی به محتوای سریع‌مصرف می‌برد؛ یافته در شماره‌ای دربارهٔ آیندهٔ خبر منتشر می‌شود.",
        evolution="نشریه در ۲۰۰۰ به‌دست باب فرانکلین راه‌اندازی شد، در دههٔ ۲۰۰۰ با رشد مطالعات خبر تثبیت شد، از دههٔ ۲۰۱۰ بحران اعتماد و پلتفرم‌ها به محور آن بدل شد و امروز یکی از پرارجاع‌ترین نشریات حوزه است.",
        key_concepts=["تحریریه", "اعتبار خبر", "اخلاق حرفه‌ای", "اقتصاد خبر", "روزنامه‌نگاری داده", "خبر جعلی"],
        theorists="باب فرانکلین و هیئت تحریریهٔ بین‌المللی.",
        theorists_text="باب فرانکلین نشریه را در آغاز هزاره بنیان نهاد و سنت پژوهش انتقادی و تطبیقی دربارهٔ خبر را در آن تثبیت کرد.",
        model="مدل مطالعات خبر: حرفه، نهاد و متن خبر در بستر اقتصاد و فناوری تحلیل می‌شوند و یافته به سیاست تحریریه بازمی‌گردد.",
        studies=[
            "شماره‌های آغازین سال ۲۰۰۰.",
            "پژوهش تحریریهٔ خبر.",
            "مطالعهٔ اعتماد به خبر.",
            "تحلیل خبر جعلی.",
            "پژوهش اقتصاد خبر.",
            "مطالعهٔ روزنامه‌نگاری داده.",
            "تحلیل اخلاق خبر.",
            "پژوهش خبر و شبکهٔ اجتماعی.",
            "مطالعهٔ تطبیقی خبر.",
            "تحلیل حرفه‌ای‌شدن.",
            "پژوهش خبر محلی.",
            "مطالعهٔ آزادی مطبوعات.",
            "تحلیل خبر بحران.",
            "پژوهش مخاطب خبر.",
        ],
    ),
}

NAME_FIX = {}
YEAR_FIX = {
    "pub-icjr": "year added 2007 (verified anchor: IJoC launched at USC Annenberg in 2007); card had no year value",
    "pub-joc": "year added 1951 (verified anchor: first issue of Journal of Communication, 1951); card had no year value",
    "pub-journal-adv-studies": "year added 1972 (verified anchor: Journal of Advertising published since 1972); card had no year value",
    "pub-journalism-studies": "year added 2000 (verified anchor: Journalism Studies established 2000); card had no year value",
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
                                       "verified": n_verified, "batch": 184}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH184 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
