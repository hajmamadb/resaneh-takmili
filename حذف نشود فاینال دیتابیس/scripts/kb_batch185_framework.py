# -*- coding: utf-8 -*-
"""Batch 185 (PUBLICATION): pub-mass-comm-society, pub-media-culture, pub-new-media-society, pub-public-relation-qr."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch185-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch185.json"

PUBLICATION_MAPPING = {"entity_type": "PUBLICATION", "content_type": "نشریه (Publication)", "needs_review": False}

S = {
    "pub-mass-comm-society": [
        dict(kind="WEBSITE",
             title_en="Mass Communication & Society (Online) - ISSN 1532-7825",
             title_fa="جامعه و ارتباطات توده‌ای (برخط) - شمارهٔ استاندارد بین‌المللی",
             authors="ISSN International Centre", year=2026,
             publisher="ISSN Portal",
             doi=None,
             url="https://portal.issn.org/resource/ISSN/1532-7825",
             language="en", isbn=None,
             citation="ISSN International Centre. Mass communication & society (Online), ISSN 1532-7825. ISSN Portal.",
             locator="ISSN record 1532-7825", locator_type="web_page",
             supports="print/online ISSN pair and LOCKSS archive coverage from 1998", verified=True),
        dict(kind="OTHER",
             title_en="Mass Communication and Society - Taylor & Francis subject title list entry",
             title_fa="جامعه و ارتباطات توده‌ای - مدخل فهرست موضوعی تیلور و فرانسیس",
             authors="Taylor & Francis", year=2026,
             publisher="Taylor & Francis",
             doi=None,
             url="https://files.taylorandfrancis.com/media-cultural-communication-studies-title-list.pdf",
             language="en", isbn=None,
             citation="Taylor & Francis. Media, cultural & communication studies subject title list [PDF].",
             locator="Mass Communication and Society entry (ISSN 1520-5436 / 1532-7825)", locator_type="SECTION",
             supports="journal listed under Taylor & Francis with print ISSN 1520-5436 and online ISSN 1532-7825", verified=True),
    ],
    "pub-media-culture": [
        dict(kind="WEBSITE",
             title_en="Media, Culture & Society - All Issues (SAGE Journals)",
             title_fa="رسانه، فرهنگ و جامعه - همهٔ شماره‌ها (نشریات سیج)",
             authors="SAGE Publications", year=2026,
             publisher="SAGE Publications",
             doi=None,
             url="https://journals.sagepub.com/loi/mcs",
             language="en", isbn=None,
             citation="SAGE Publications. Media, Culture & Society - All issues. SAGE Journals.",
             locator="all-issues index, January 1979 - November 2026", locator_type="web_page",
             supports="publication run starting January 1979; print ISSN 0163-4437 and online ISSN 1460-3675", verified=True),
        dict(kind="WEBSITE",
             title_en="Media, Culture & Society - Volume 1, Number 2 (April 1979)",
             title_fa="رسانه، فرهنگ و جامعه - جلد ۱، شمارهٔ ۲ (آوریل ۱۹۷۹)",
             authors="SAGE Publications", year=1979,
             publisher="SAGE Publications",
             doi=None,
             url="https://journals.sagepub.com/toc/mcsa/1/2",
             language="en", isbn=None,
             citation="SAGE Publications. Media, Culture & Society, Volume 1, Number 2, April 1979.",
             locator="volume 1, issue 2, April 1979", locator_type="web_page",
             supports="first volume published in 1979", verified=True),
    ],
    "pub-new-media-society": [
        dict(kind="WEBSITE",
             title_en="New Media & Society (Online) - ISSN 1461-7315",
             title_fa="جامعه و رسانه‌های نوین (برخط) - شمارهٔ استاندارد بین‌المللی",
             authors="ISSN International Centre", year=2026,
             publisher="ISSN Portal",
             doi=None,
             url="https://portal.issn.org/resource/ISSN/1461-7315",
             language="en", isbn=None,
             citation="ISSN International Centre. New media & society (Online), ISSN 1461-7315. ISSN Portal.",
             locator="ISSN record 1461-7315", locator_type="web_page",
             supports="online edition registered with print ISSN-L 1461-4448 and issue history from 1999 onward", verified=True),
        dict(kind="WEBSITE",
             title_en="New Media and Society - WUR Library journal record",
             title_fa="جامعه و رسانه‌های نوین - سابقهٔ کتابخانهٔ دانشگاه واگنینگن",
             authors="Wageningen University & Research Library", year=2026,
             publisher="WUR Library",
             doi=None,
             url="https://library.wur.nl/WebQuery/umbrowser/1074",
             language="en", isbn=None,
             citation="Wageningen University & Research Library. New Media and Society: journal record.",
             locator="journal record (SAGE Publications, 1999-)", locator_type="web_page",
             supports="publisher SAGE Publications and publication span from 1999", verified=True),
    ],
    "pub-public-relation-qr": [
        dict(kind="WEBSITE",
             title_en="Public Relations Quarterly - ISSN 0033-3700",
             title_fa="مطالعات روابط عمومی - شمارهٔ استاندارد بین‌المللی",
             authors="ISSN International Centre", year=2026,
             publisher="ISSN Portal",
             doi=None,
             url="https://portal.issn.org/resource/ISSN/0033-3700",
             language="en", isbn=None,
             citation="ISSN International Centre. Public relations quarterly, ISSN 0033-3700. ISSN Portal.",
             locator="ISSN record 0033-3700, archival status notes", locator_type="web_page",
             supports="confirmed print quarterly published in the United States; Internet Archive extent vols. 1-52 (1955-2008); notes cite vol. 29 no. 1 (spring 1984) and vol. 52 no. 4", verified=True),
        dict(kind="ARCHIVE",
             title_en="Public Relations Quarterly - Internet Archive collection",
             title_fa="مطالعات روابط عمومی - مجموعهٔ آرشیو اینترنت",
             authors="Internet Archive", year=2026,
             publisher="Internet Archive",
             doi=None,
             url="https://archive.org/details/pub_public-relations-quarterly",
             language="en", isbn=None,
             citation="Internet Archive. Public Relations Quarterly collection, volumes 1-52 (1955-2008). Linked from ISSN record 0033-3700.",
             locator="collection extent 1-52 (1955-2008)", locator_type="web_page",
             supports="digitized run of the journal preserved through 2008", verified=True),
    ],
}

ENRICH = {
    "pub-mass-comm-society": dict(
        year=1998,
        mapping=PUBLICATION_MAPPING,
        issn="1520-5436",
        issn_online="1532-7825",
        summary="مجلهٔ جامعه و ارتباطات توده‌ای نشریه‌ای علمی و داوری‌شده است که از ۱۹۹۸ دربارهٔ پیوند رسانه‌های جمعی با ساختارهای اجتماعی منتشر می‌شود. این نشریه در سنت پژوهش اجتماعی ارتباطات جای دارد و بر نظریه‌های اثرات رسانه، خبر و روزنامه‌نگاری، ارتباطات سیاسی، ارتباطات سلامت و جامعه‌شناسی رسانه تمرکز دارد. مقاله‌های آن بیشتر تجربی‌اند و از پیمایش، آزمایش، تحلیل محتوا و روش‌های ترکیبی بهره می‌گیرند، هرچند نوشتارهای نظری و مروری نیز در آن جای دارند. عنوان نشریه پیوند دوگانهٔ رسانه و جامعه را برجسته می‌کند: از یک سو رسانه چگونه از ساختار اجتماعی اثر می‌گیرد و از سوی دیگر چگونه آن را بازتولید یا دگرگون می‌کند. شماره‌های موضوعی دربارهٔ خبر جعلی، قطب‌بندی سیاسی، اعتماد به رسانه و سلامت عمومی در آن منتشر شده است. این نشریه با استانداردهای روشن گزارش‌دهی و داوری همتا شناخته می‌شود و برای پژوهشگرانی که یافته‌های تجربی خود را در چارچوب نظریهٔ اجتماعی صورت‌بندی می‌کنند جذاب است. دسترسی به آن از طریق اشتراک نهادی انجام می‌شود و پژوهشگران فارسی‌زبان بیشتر از راه کتابخانه‌های دانشگاهی به آن می‌رسند. نقدها بر تمرکز بر داده‌های آمریکای شمالی، غلبهٔ روش‌های کمی و فشار شاخص‌های استنادی تأکید دارند.",
        definition="مجلهٔ جامعه و ارتباطات توده‌ای نشریهٔ علمی داوری‌شده‌ای است که از ۱۹۹۸ پژوهش‌های نظری و تجربی دربارهٔ رابطهٔ رسانه‌های جمعی و جامعه را با ناشر تیلور و فرانسیس منتشر می‌کند.",
        main_problem="چگونه می‌توان پیوند علّی و تفسیری میان نهادهای رسانه‌ای و ساختار اجتماعی را با شواهد تجربی معتبر سنجید و یافته‌ها را در نظریهٔ اجتماعی ارتباطات جای داد.",
        mechanism="مقاله‌ها پس از داوری همتا و بازبینی روش‌شناختی منتشر می‌شوند؛ شماره‌های موضوعی پژوهش‌های هم‌موضوع را گرد می‌آورند و استاندارد گزارش‌دهی داده، مقایسهٔ یافته‌ها را در طرح‌های بعدی ممکن می‌کند.",
        assumptions=[
            "رسانه و جامعه دو نظام به‌هم‌پیوسته‌اند.",
            "شواهد تجربی مبنای معتبر شناخت اثر رسانه است.",
            "نظریهٔ اجتماعی چارچوب تفسیر یافته‌هاست.",
            "سنجش منظم مواجهه با رسانه ممکن است.",
            "داوری همتا کیفیت روش را تضمین می‌کند.",
            "تنوع روشی فهم پدیده را عمیق می‌کند.",
            "پیامدهای اجتماعی معیار اهمیت پژوهش‌اند.",
            "تکرارپذیری یافته اعتبار دانش را می‌سازد.",
        ],
        principles=[
            "نظریه را با داده آزمون کن.",
            "روش نمونه‌گیری را شفاف گزارش کن.",
            "اندازهٔ اثر را در کنار معناداری بنویس.",
            "پیامد اجتماعی یافته را توضیح بده.",
            "تعارض منافع را افشا کن.",
            "یافته‌های متناقض را منتشر کن.",
            "دامنهٔ تعمیم را محدود و صریح بیان کن.",
        ],
        critiques=[
            "داده‌ها بیش از اندازه آمریکای شمالی‌اند.",
            "روش‌های کمی بر تفسیر غلبه دارند.",
            "فشار شاخص استنادی موضوع را تحریف می‌کند.",
            "دسترسی اشتراکی نابرابری خواندن می‌سازد.",
            "مقاله‌ها گاه به آزمون فرضیه‌های کوچک محدود می‌شوند.",
            "پیوند با سیاست‌گذاری رسانه ضعیف می‌ماند.",
            "سرعت داوری با حجم ارسال هم‌خوان نیست.",
        ],
        critique_text="منتقدان می‌گویند این نشریه با غلبهٔ داده‌های آمریکای شمالی، روش‌های کمی و فشار شاخص استنادی، تنوع تفسیری و تعمیم‌پذیری یافته‌ها را محدود می‌کند؛ با این حال استاندارد روشن گزارش‌دهی و پیوند نظریهٔ اجتماعی با داده، آن را به مرجعی مهم در پژوهش اثرات رسانه بدل کرده است.",
        applications=[
            "مطالعهٔ اثر خبر جعلی بر اعتماد.",
            "تحلیل قطب‌بندی سیاسی مخاطب.",
            "پژوهش ارتباطات سلامت.",
            "بررسی بازنمایی گروه‌های اجتماعی.",
            "مطالعهٔ مصرف خبر در بحران.",
            "تحلیل سیاست‌گذاری رسانه.",
            "پژوهش خشونت رسانه‌ای.",
            "مطالعهٔ رسانه و مشارکت مدنی.",
            "تحلیل اعتماد به نهادهای خبری.",
            "پژوهش تبلیغات سیاسی.",
            "مطالعهٔ رسانهٔ قومی و مهاجرت.",
            "تحلیل سواد رسانه‌ای.",
            "پژوهش مخاطب خبر محلی.",
        ],
        example_text="پژوهشی سه‌ساله دربارهٔ اثر مواجههٔ تکراری با خبر جعلی بر اعتماد نهادی، با پیمایش پنلی و آزمایش آنلاین در این نشریه منتشر می‌شود؛ چون گام‌های نمونه‌گیری و اندازهٔ اثر کامل گزارش شده، پژوهشگران دیگر آن را در کشورهای خود تکرار می‌کنند.",
        evolution="این نشریه در ۱۹۹۸ آغاز شد، در دههٔ ۲۰۰۰ با نمایه‌سازی در پایگاه‌های استنادی تثبیت شد، در دههٔ ۲۰۱۰ شماره‌های موضوعی دربارهٔ رسانهٔ دیجیتال و اطلاعات نادرست منتشر کرد و امروز به‌عنوان یکی از نشریات مرجع پیوند رسانه و جامعه شناخته می‌شود.",
        key_concepts=["اثرات رسانه", "رسانه و جامعه", "ارتباطات سیاسی", "اعتماد به رسانه", "روش‌های ترکیبی", "سواد رسانه‌ای"],
        theorists="ویراستاران متوالی نشریه.",
        theorists_text="ویراستاران متوالی نشریه با تکیه بر سنت پژوهش تجربی ارتباطات، استاندارد گزارش‌دهی و داوری روش‌شناختی را شکل داده‌اند.",
        model="مدل نشریهٔ پیوند رسانه و جامعه: نظریهٔ اجتماعی چارچوب می‌دهد، دادهٔ تجربی فرضیه را می‌آزماید و استاندارد گزارش‌دهی، انباشت قابل مقایسهٔ دانش را ممکن می‌کند.",
        studies=[
            "شمارهٔ ویژهٔ اطلاعات نادرست.",
            "پژوهش پنلی اعتماد خبری.",
            "مطالعهٔ آزمایشی قطب‌بندی.",
            "تحلیل محتوای پوشش سلامت.",
            "پژوهش رسانه و مشارکت مدنی.",
            "مطالعهٔ مخاطب خبر محلی.",
            "تحلیل تبلیغات انتخاباتی.",
            "پژوهش بازنمایی مهاجران.",
            "مطالعهٔ خشونت رسانه‌ای.",
            "تحلیل سواد رسانه‌ای دانش‌آموزان.",
            "پژوهش رسانهٔ قومی.",
            "مطالعهٔ سیاست‌گذاری پخش.",
            "تحلیل اعتماد به روزنامه‌نگاری.",
            "پژوهش مصرف خبر در بحران.",
        ],
    ),
    "pub-media-culture": dict(
        year=1979,
        mapping=PUBLICATION_MAPPING,
        summary="رسانه، فرهنگ و جامعه نشریه‌ای علمی و میان‌رشته‌ای است که از ۱۹۷۹ با ناشر سیج منتشر می‌شود و در سنت مطالعات فرهنگی و اقتصاد سیاسی رسانه جای دارد. این نشریه رسانه را نه فقط ابزار انتقال پیام، بلکه میدان تولید معنا، قدرت و هویت می‌بیند و مقاله‌های نظری، تجربی و تاریخی دربارهٔ نهادهای رسانه‌ای، مخاطب، بازنمایی، سیاست فرهنگی و جهانی‌شدن منتشر می‌کند. دامنهٔ آن از تلویزیون و مطبوعات تا رسانه‌های دیجیتال گسترده است و پژوهش‌های کیفی، قوم‌نگارانه و انتقادی در آن جایگاه مهمی دارند. مجله در طول دهه‌ها میزبان مناظره‌های نظری دربارهٔ فرهنگ عامه، ایدئولوژی، مخاطب فعال و گذار دیجیتال بوده است. هیئت تحریریهٔ بین‌المللی و شماره‌های ویژه دربارهٔ بحران‌های فرهنگی و سیاست رسانه از ویژگی‌های آن است. برای پژوهشگران فارسی‌زبان، مقاله‌های آن مرجعی برای پیوند نظریهٔ انتقادی با مطالعهٔ تجربی رسانه است، هرچند دسترسی از طریق اشتراک نهادی فراهم می‌شود. نقدها بر تمرکز بر تجربهٔ بریتانیا و اروپا، پیچیدگی نظری و کندی داوری تأکید دارند.",
        definition="رسانه، فرهنگ و جامعه نشریهٔ علمی میان‌رشته‌ای سیج است که از ۱۹۷۹ پژوهش‌های انتقادی دربارهٔ رسانه، فرهنگ و قدرت منتشر می‌کند.",
        main_problem="چگونه می‌توان تولید معنا، روابط قدرت و تجربهٔ فرهنگی را در نهادها و متن‌های رسانه‌ای به‌گونه‌ای نظری و تجربی هم‌زمان مطالعه کرد.",
        mechanism="مقاله‌ها با داوری همتا و ویرایش نظری منتشر می‌شوند؛ شماره‌های ویژه و مناظره‌های مکتوب سنت انتقادی نشریه را بازتولید می‌کنند و پیوند تحلیل متن با اقتصاد سیاسی، فهم چندلایهٔ رسانه را ممکن می‌سازد.",
        assumptions=[
            "رسانه میدان تولید معناست نه فقط انتقال پیام.",
            "فرهنگ و اقتصاد به‌هم پیوسته‌اند.",
            "مخاطب تفسیرکنندهٔ فعال است.",
            "تحلیل انتقادی به شواهد تجربی نیاز دارد.",
            "زمینهٔ تاریخی فهم رسانه را ممکن می‌کند.",
            "سیاست فرهنگی بخشی از مطالعهٔ رسانه است.",
            "تنوع روشی فهم پدیده را غنی می‌کند.",
            "زبان و بازنمایی قدرت را بازتولید می‌کنند.",
        ],
        principles=[
            "متن را در زمینهٔ نهادی بخوان.",
            "اقتصاد سیاسی را در تحلیل بگنجان.",
            "صدای گروه‌های حاشیه‌ای را بشنو.",
            "روش کیفی را شفاف گزارش کن.",
            "مناظرهٔ نظری را زنده نگه دار.",
            "سیاست فرهنگی را نقد کن.",
            "دامنهٔ تعمیم را محدود بیان کن.",
        ],
        critiques=[
            "تجربهٔ بریتانیا محور تحلیل‌هاست.",
            "پیچیدگی نظری خواندن را دشوار می‌کند.",
            "داوری نشریه کند است.",
            "دسترسی اشتراکی مانع خواندن جهانی است.",
            "گاه تحلیل تجربی زیر وزن نظریه می‌ماند.",
            "تمرکز بر متن، نهادهای اقتصادی را کم‌رنگ می‌کند.",
            "شماره‌های ویژه به شبکهٔ سردبیران وابسته‌اند.",
        ],
        critique_text="منتقدان می‌گویند این نشریه با محوریت تجربهٔ بریتانیا، پیچیدگی نظری و کندی داوری، دسترسی و تعمیم یافته‌ها را محدود می‌کند؛ با این حال پیوند نظام‌مند تحلیل انتقادی با شواهد تجربی، آن را به مرجع مطالعهٔ فرهنگی رسانه بدل کرده است.",
        applications=[
            "تحلیل بازنمایی جنسیت در تلویزیون.",
            "مطالعهٔ سیاست فرهنگی پخش.",
            "پژوهش مخاطب و تفسیر متن.",
            "تحلیل اقتصاد سیاسی پلتفرم.",
            "مطالعهٔ رسانه و هویت ملی.",
            "پژوهش جهانی‌شدن رسانه.",
            "تحلیل فرهنگ عامه و سلبریتی.",
            "مطالعهٔ رسانهٔ اقلیت‌ها.",
            "پژوهش گذار دیجیتال مطبوعات.",
            "تحلیل تبلیغات و مصرف.",
            "مطالعهٔ رسانه و شهر.",
            "پژوهش سیاست حافظه.",
            "تحلیل صدا و سیاست گوش‌دادن.",
            "مطالعهٔ مخاطب کودکان.",
        ],
        example_text="پژوهشی قوم‌نگارانه دربارهٔ مصرف خبر در خانواده‌های کارگری نشان می‌دهد چگونه معنای سیاسی خبر در گفت‌وگوی روزمره بازتفسیر می‌شود؛ مقاله با پیوند تحلیل متن و مصاحبه در این نشریه منتشر می‌شود و الگویی برای پژوهش مخاطب انتقادی می‌سازد.",
        evolution="این نشریه در ۱۹۷۹ در اوج گسترش مطالعات فرهنگی بریتانیا آغاز شد، در دههٔ ۱۹۸۰ میزبان مناظرهٔ اقتصاد سیاسی و مطالعات فرهنگی بود، در دههٔ ۱۹۹۰ به جهانی‌شدن رسانه پرداخت، در دههٔ ۲۰۰۰ گذار دیجیتال را دنبال کرد و امروز هشت شماره در سال منتشر می‌کند.",
        key_concepts=["مطالعات فرهنگی", "اقتصاد سیاسی", "بازنمایی", "مخاطب فعال", "سیاست فرهنگی", "ایدئولوژی"],
        theorists="ویراستاران متوالی در سنت مطالعات فرهنگی بریتانیا.",
        theorists_text="هیئت‌های تحریریهٔ متوالی با تکیه بر میراث مطالعات فرهنگی بریتانیا و اقتصاد سیاسی انتقادی، سنت تحلیل فرهنگی رسانه را در نشریه نهادینه کردند.",
        model="مدل تحلیل انتقادی رسانه: متن، نهاد و مخاطب سه لایهٔ به‌هم‌پیوسته‌اند و تحلیل معتبر باید هر سه را در زمینهٔ تاریخی و اقتصادی ببیند.",
        studies=[
            "شمارهٔ ویژهٔ فرهنگ عامه.",
            "پژوهش مخاطب تلویزیون.",
            "تحلیل اقتصاد سیاسی مطبوعات.",
            "مطالعهٔ بازنمایی جنسیت.",
            "پژوهش سیاست پخش.",
            "تحلیل رسانه و هویت ملی.",
            "مطالعهٔ گذار دیجیتال.",
            "پژوهش جهانی‌شدن رسانه.",
            "تحلیل حافظه و رسانه.",
            "مطالعهٔ رسانهٔ اقلیت‌ها.",
            "پژوهش تبلیغات و مصرف.",
            "تحلیل سیاست فرهنگی.",
            "مطالعهٔ سلبریتی.",
            "پژوهش رسانه و شهر.",
        ],
    ),
    "pub-new-media-society": dict(
        year=1999,
        mapping=PUBLICATION_MAPPING,
        summary="جامعه و رسانه‌های نوین نشریه‌ای علمی است که از ۱۹۹۹ با ناشر سیج منتشر می‌شود و به مطالعهٔ رسانه‌های دیجیتال، اینترنت و پیامدهای اجتماعی آن‌ها می‌پردازد. این نشریه در زمانی آغاز شد که وب همگانی می‌شد و از همان آغاز کوشید پژوهش اینترنت را از توصیف فناوری به پرسش‌های اجتماعی، فرهنگی و سیاسی پیوند دهد. دامنهٔ آن شبکه‌های اجتماعی، پلتفرم‌ها، بازی، موبایل، جوامع مجازی، شکاف دیجیتال، الگوریتم‌ها و داده‌شدن زندگی روزمره را در بر می‌گیرد. مقاله‌ها ترکیبی از نظریه و شواهد تجربی‌اند و روش‌های کمی، کیفی و محاسباتی در آن دیده می‌شوند. نشریه میزبان شماره‌های ویژه دربارهٔ اعتراضات شبکه‌ای، حریم خصوصی، کار پلتفرمی و هوش مصنوعی بوده است. برای پژوهشگران رسانهٔ نو، این نشریه محل انتشار پژوهش‌های پیشگام دربارهٔ تعامل انسان و ماشین و فرهنگ شبکه است. دسترسی از طریق اشتراک نهادی فراهم می‌شود. نقدها بر تازگی‌محوری، تمرکز بر پلتفرم‌های غربی و سرعت انتشار تأکید دارند.",
        definition="جامعه و رسانه‌های نوین نشریهٔ علمی داوری‌شدهٔ سیج است که از ۱۹۹۹ پژوهش‌های اجتماعی، فرهنگی و سیاسی دربارهٔ رسانه‌های دیجیتال منتشر می‌کند.",
        main_problem="چگونه می‌توان دگرگونی‌های سریع رسانهٔ دیجیتال را با نظریهٔ اجتماعی پایدار سنجید و از توصیف تازه‌های فناوری به تبیین پیامدهای اجتماعی رسید.",
        mechanism="مقاله‌ها با داوری همتا و ویرایش روش‌شناختی منتشر می‌شوند؛ شماره‌های ویژه پدیده‌های نوپدید را سریع گرد می‌آورند و ترکیب روش‌های کمی، کیفی و محاسباتی، تبیین چندلایهٔ تعامل انسان و ماشین را ممکن می‌کند.",
        assumptions=[
            "فناوری و جامعه یکدیگر را می‌سازند.",
            "رسانهٔ نو پدیده‌ای اجتماعی است نه فقط فنی.",
            "دادهٔ دیجیتال ردپای کنش اجتماعی است.",
            "نظریهٔ اجتماعی باید با پدیدهٔ متغیر به‌روز شود.",
            "شکاف دیجیتال مسئلهٔ عدالت است.",
            "پلتفرم نهاد قدرت است.",
            "روش محاسباتی مکمل تحلیل کیفی است.",
            "تجربهٔ کاربر دادهٔ معتبر پژوهش است.",
        ],
        principles=[
            "از تازگی‌محوری بپرهیز.",
            "پدیده را در زمینهٔ نهادی ببین.",
            "داده و اخلاق حریم را رعایت کن.",
            "روش را متناسب با پدیده برگزین.",
            "یافتهٔ منفی را هم منتشر کن.",
            "دامنهٔ تعمیم را صریح بیان کن.",
            "صدای کاربران حاشیه‌ای را بشنو.",
        ],
        critiques=[
            "تازگی‌محوری عمر یافته را کوتاه می‌کند.",
            "پلتفرم‌های غربی محور پژوهش‌اند.",
            "سرعت انتشار عمق داوری را کم می‌کند.",
            "دسترسی اشتراکی نابرابری خواندن می‌سازد.",
            "دادهٔ پلتفرم وابسته به سیاست شرکت است.",
            "نظریه گاه از پدیده عقب می‌ماند.",
            "اخلاق پژوهش دیجیتال هنوز نهادینه نیست.",
        ],
        critique_text="منتقدان می‌گویند تازگی‌محوری، محوریت پلتفرم‌های غربی و سرعت انتشار، عمر و تعمیم‌پذیری یافته‌ها را محدود می‌کند؛ با این حال نشریه با گردآوری سریع پژوهش دربارهٔ پدیده‌های نوپدید، مرجع اصلی مطالعات رسانهٔ دیجیتال شده است.",
        applications=[
            "مطالعهٔ شبکه‌های اجتماعی.",
            "پژوهش شکاف دیجیتال.",
            "تحلیل الگوریتم و توصیه‌گری.",
            "مطالعهٔ حریم خصوصی آنلاین.",
            "پژوهش بازی و فرهنگ پلتفرم.",
            "تحلیل اعتراضات شبکه‌ای.",
            "مطالعهٔ کار پلتفرمی.",
            "پژوهش هویت در فضای مجازی.",
            "تحلیل خبر جعلی در پلتفرم.",
            "مطالعهٔ موبایل و زندگی روزمره.",
            "پژوهش هوش مصنوعی و تعامل.",
            "تحلیل جوامع آنلاین.",
            "مطالعهٔ سواد دیجیتال.",
            "پژوهش اعتماد به پلتفرم.",
        ],
        example_text="پژوهشی با ترکیب ردیابی رفتار مرورگر و مصاحبهٔ عمیق نشان می‌دهد کاربران چگونه الگوریتم توصیه را می‌فهمند و دور می‌زنند؛ مقاله در این نشریه منتشر می‌شود و الگویی برای مطالعهٔ آگاهی الگوریتمی می‌سازد.",
        evolution="این نشریه در ۱۹۹۹ هم‌زمان با گسترش وب آغاز شد، در دههٔ ۲۰۰۰ جوامع مجازی و شکاف دیجیتال را پوشش داد، در دههٔ ۲۰۱۰ به شبکه‌های اجتماعی و پلتفرم‌ها رو آورد و امروز با دورهٔ ماهانه، پژوهش الگوریتم و هوش مصنوعی را دنبال می‌کند.",
        key_concepts=["رسانهٔ دیجیتال", "پلتفرم", "شکاف دیجیتال", "تعامل انسان و ماشین", "حریم خصوصی", "الگوریتم"],
        theorists="ویراستاران متوالی و جامعهٔ پژوهشگران اینترنت.",
        theorists_text="ویراستاران متوالی با گردآوری پژوهش‌های میان‌رشته‌ای، مطالعهٔ اینترنت را از توصیف فناوری به پرسش اجتماعی و انتقادی پیوند دادند.",
        model="مدل رسانهٔ نو: فناوری، نهاد و کنش کاربر در هم‌ساخت‌اند و تبیین معتبر باید طراحی پلتفرم، اقتصاد و تجربهٔ کاربر را هم‌زمان ببیند.",
        studies=[
            "شمارهٔ ویژهٔ اعتراض شبکه‌ای.",
            "پژوهش شکاف دیجیتال.",
            "تحلیل الگوریتم توصیه.",
            "مطالعهٔ حریم خصوصی.",
            "پژوهش کار پلتفرمی.",
            "تحلیل خبر جعلی.",
            "مطالعهٔ بازی آنلاین.",
            "پژوهش هویت مجازی.",
            "تحلیل جوامع آنلاین.",
            "مطالعهٔ موبایل و خانواده.",
            "پژوهش هوش مصنوعی گفت‌وگویی.",
            "تحلیل اعتماد به پلتفرم.",
            "مطالعهٔ سواد دیجیتال.",
            "پژوهش داده‌شدن زندگی روزمره.",
        ],
    ),
    "pub-public-relation-qr": dict(
        year=1956,
        mapping=PUBLICATION_MAPPING,
        issn="0033-3700",
        publisher="Public Relations Quarterly",
        summary="مطالعات روابط عمومی فصل‌نامه‌ای حرفه‌ای و مستقل در حوزهٔ روابط عمومی بود که در ۱۹۵۶ به‌دست دنی گریزولد بنیان گذاشته شد و با شمارهٔ استاندارد ۰۰۳۳-۳۷۰۰ تا پایان دههٔ ۲۰۰۰ منتشر می‌شد. برخلاف نشریات دانشگاهی، این فصل‌نامه در میان متخصصان روابط عمومی گردش می‌کرد و مقاله‌های کاربردی، گزارش موارد واقعی، مصاحبه با مدیران ارتباطات، یادداشت‌های انتقادی و بحث‌های اخلاق حرفه‌ای را در بر می‌گرفت. ستون‌های آن به بحران‌های سازمانی، روابط با رسانه، ارتباطات داخلی، روابط عمومی بین‌المللی و سنجش اثربخشی اختصاص داشت. بسیاری از روایت‌های تاریخی دربارهٔ تکوین حرفهٔ روابط عمومی در آمریکا نخست در همین صفحات ثبت شده‌اند و امروز آرشیو آن منبعی برای پژوهش تاریخ حرفه است. نشریه داوری همتای دانشگاهی نداشت و اعتبار آن بر تجربهٔ نویسندگان و سابقهٔ ویراستار استوار بود. شماره‌های آن گاه به مناسبت سالگردها یا بحران‌های صنعتی منتشر می‌شد. در پایان دههٔ ۲۰۰۰ انتشار آن متوقف شد و جای خود را به نشریات داوری‌شده و برخط داد. نقدها بر فقدان روش نظام‌مند، سوگیری حرفه‌ای و روزآمدنبودن برخی مطالب تأکید دارند؛ با این حال برای پژوهش کیفی و تاریخی روابط عمومی ارزش سندی دارد.",
        definition="مطالعات روابط عمومی فصل‌نامه‌ای حرفه‌ای و مستقل در حوزهٔ روابط عمومی بود که از ۱۹۵۶ تا حدود ۲۰۰۸ منتشر شد و بر تجربهٔ عملی و تاریخ حرفه تمرکز داشت.",
        main_problem="چگونه می‌توان دانش عملی روابط عمومی را در میان متخصصان منتشر کرد و تجربهٔ سازمانی را بدون سازوکار داوری دانشگاهی به مرجع حرفه‌ای تبدیل کرد.",
        mechanism="متخصصان و مدیران ارتباطات مقاله‌های کاربردی و گزارش موارد واقعی می‌نوشتند؛ ویراستار مطالب را بر پایهٔ تجربه و ارتباط با صنعت گزینش می‌کرد و شماره‌ها در میان اعضای حرفه توزیع می‌شد.",
        assumptions=[
            "تجربهٔ حرفه‌ای منبع معتبر دانش است.",
            "مطالعهٔ موردی درس‌های قابل انتقال دارد.",
            "اخلاق حرفه‌ای بخشی از مهارت است.",
            "روابط با رسانه هستهٔ کار روابط عمومی است.",
            "سنجش اثربخشی ضروری است.",
            "بین‌المللی‌شدن حرفه گریزناپذیر است.",
            "مدیران ارشد مخاطب اصلی نشریه‌اند.",
            "تاریخ حرفه راهنمای عمل آینده است.",
        ],
        principles=[
            "تجربه را مستند کن.",
            "مورد واقعی را کامل روایت کن.",
            "اخلاق را در تصمیم نشان بده.",
            "رابطهٔ رسانه‌ای را حرفه‌ای نگه دار.",
            "اثربخشی را بسنج.",
            "صدای دیدگاه‌های مخالف را بشنو.",
            "مرز تبلیغ و اطلاع‌رسانی را روشن کن.",
        ],
        critiques=[
            "داوری همتای دانشگاهی وجود نداشت.",
            "سوگیری حرفه‌ای بر محتوا اثر می‌گذاشت.",
            "برخی مطالب با گذر زمان روزآمد نبودند.",
            "روش سنجش اثربخشی نظام‌مند نبود.",
            "دسترسی به آرشیو دشوار است.",
            "تمرکز بر تجربهٔ آمریکا غالب بود.",
            "انتشار نشریه در پایان دههٔ ۲۰۰۰ متوقف شد.",
        ],
        critique_text="منتقدان می‌گویند نبود داوری دانشگاهی، سوگیری حرفه‌ای و روزآمدنبودن بخشی از مطالب، اعتبار علمی نشریه را محدود می‌کرد؛ با این حال آرشیو آن سند ارزشمندی از تاریخ حرفهٔ روابط عمومی و شیوهٔ اندیشیدن متخصصان سدهٔ بیستم است.",
        applications=[
            "پژوهش تاریخ روابط عمومی.",
            "تحلیل موردی بحران سازمانی.",
            "مطالعهٔ روابط رسانه‌ای.",
            "بررسی اخلاق حرفه‌ای.",
            "تحلیل ارتباطات داخلی.",
            "پژوهش روابط عمومی بین‌المللی.",
            "مطالعهٔ سنجش اثربخشی.",
            "تحلیل تبلیغات شرکتی.",
            "پژوهش مدیریت شهرت.",
            "مطالعهٔ ارتباطات بحران.",
            "تحلیل روابط با ذی‌نفعان.",
            "بررسی حرفه‌ای‌شدن روابط عمومی.",
            "مطالعهٔ تصویر شرکت.",
            "تحلیل روایت‌های صنعتی.",
        ],
        example_text="پژوهشگر تاریخ حرفه، شماره‌ای از نشریه را می‌یابد که مدیر ارتباطات یک شرکت بزرگ بحران دههٔ ۱۹۷۰ را روایت کرده است؛ مقایسهٔ این روایت با اسناد سازمانی، شکاف میان تصویر عمومی و تصمیم درونی را آشکار می‌کند.",
        evolution="نشریه در ۱۹۵۶ بنیان گذاشته شد، در دهه‌های ۱۹۶۰ و ۱۹۷۰ به منبر بحث حرفه‌ای بدل شد، در دههٔ ۱۹۸۰ و ۱۹۹۰ شماره‌های بین‌المللی و اخلاقی منتشر کرد، در دههٔ ۲۰۰۰ با رقابت نشریات داوری‌شده و برخط روبه‌رو شد و انتشار آن در پایان آن دهه متوقف شد.",
        key_concepts=["روابط عمومی حرفه‌ای", "مطالعهٔ موردی", "ارتباطات بحران", "اخلاق حرفه‌ای", "روابط رسانه‌ای", "تاریخ حرفه"],
        theorists="دنی گریزولد و نویسندگان حرفه‌ای.",
        theorists_text="دنی گریزولد بنیان‌گذار و ویراستار نشریه بود و سنت روایت تجربهٔ حرفه‌ای و گفت‌وگوی انتقادی درون صنعت را شکل داد.",
        model="مدل نشریهٔ حرفه‌ای: تجربهٔ مستند، مورد واقعی و اخلاق عملی جای داوری دانشگاهی را می‌گیرد و دانش حرفه‌ای را از راه روایت میان متخصصان منتشر می‌کند.",
        studies=[
            "آرشیو شماره‌های بحران سازمانی.",
            "پروندهٔ روابط رسانه‌ای.",
            "شمارهٔ ویژهٔ اخلاق حرفه.",
            "گزارش ارتباطات داخلی.",
            "پژوهش روابط عمومی بین‌المللی.",
            "تحلیل شیوهٔ سنجش اثربخشی.",
            "پروندهٔ مدیریت شهرت.",
            "مطالعهٔ تاریخ حرفه در آمریکا.",
            "تحلیل تبلیغات شرکتی.",
            "پژوهش روابط با ذی‌نفعان.",
            "شمارهٔ سالگرد صنعت.",
            "تحلیل حرفه‌ای‌شدن روابط عمومی.",
            "مطالعهٔ تصویر شرکت.",
            "تحلیل روایت‌های صنعتی.",
        ],
    ),
}

NAME_FIX = {}
YEAR_FIX = {
    "pub-mass-comm-society": "year added 1998 (verified anchor: ISSN 1532-7825 record and Taylor & Francis title list covering the title from 1998); card had no year value; issn corrected 1520-5418 -> 1520-5436 and online issn 1532-7825 added (verified Taylor & Francis title list and ISSN Portal)",
    "pub-media-culture": "year added 1979 (verified anchor: SAGE Journals volume 1, issue 2, April 1979, and all-issues index starting January 1979); card had no year value",
    "pub-new-media-society": "year added 1999 (verified anchor: ISSN 1461-7315 record and WUR Library record 'SAGE Publications (1999-)'); card had no year value",
    "pub-public-relation-qr": "year added 1956 (verified anchor: ISSN 0033-3700 record, vols. 1-52 covering 1955-2008, with note vol. 29 no. 1 (spring 1984) implying vol. 1 = 1956); card had no year value; issn corrected 1046-1163 -> 0033-3700 (ISSN Portal); publisher corrected from PRSA to Public Relations Quarterly per ISSN archival record (independent journal founded by Denny Griswold; no PRSA publishing link verified)",
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
                                       "verified": n_verified, "batch": 185}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH185 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
