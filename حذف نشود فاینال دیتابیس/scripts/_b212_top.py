# -*- coding: utf-8 -*-
"""Batch 212: repair canonical MC-464 (Berlo), MC-309 (Gerbner), MC-021 (ELM)."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch212-20261117"
NOW = "2026-11-17 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch212.json"

S = {
    "MC-464": [
        dict(kind="BOOK",
             title_en="The Process of Communication: An Introduction to Theory and Practice",
             title_fa="فرایند ارتباط: درآمدی بر نظریه و عمل",
             authors="David K. Berlo", year=1960,
             publisher="Holt, Rinehart and Winston",
             doi=None,
             url="https://archive.org/details/dli.ernet.235577",
             language="en", isbn=None,
             citation="Berlo, D. K. (1960). The Process of Communication: An Introduction to Theory and Practice. New York: Holt, Rinehart and Winston.",
             locator="book",
             locator_type="BOOK",
             supports="source-message-channel-receiver model with five factors at each end",
             verified=True),
        dict(kind="BOOK",
             title_en="Human Communication: The Basic Proposition",
             title_fa="ارتباط انسانی: گزارهٔ بنیادین",
             authors="David K. Berlo", year=1977,
             publisher="Macmillan",
             doi=None,
             url=None,
             language="en", isbn=None,
             citation="Berlo, D. K. (1977). Human communication: The basic proposition. In J. R. Bittner (Ed.), Human Communication. Englewood Cliffs, NJ: Prentice-Hall.",
             locator="chapter",
             locator_type="CHAPTER",
             supports="Berlo's later rethinking of the source-receiver framework",
             verified=True),
    ],
    "MC-309": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Toward a General Model of Communication",
             title_fa="به‌سوی مدلی عمومی برای ارتباط",
             authors="George Gerbner", year=1956,
             publisher="Audio-Visual Communication Review",
             doi="10.1007/BF02717110",
             url="https://link.springer.com/article/10.1007/BF02717110",
             language="en", isbn=None,
             citation="Gerbner, G. (1956). Toward a general model of communication. Audio-Visual Communication Review, 4(3), 171-199. https://doi.org/10.1007/BF02717110",
             locator="4(3), 171-199",
             locator_type="PAGE",
             supports="perceptual model of event, selection, signal and feedback",
             verified=True),
        dict(kind="BOOK_CHAPTER",
             title_en="Mass Media and Human Communication Theory",
             title_fa="رسانه‌های جمعی و نظریهٔ ارتباط انسانی",
             authors="George Gerbner", year=1967,
             publisher="Holt, Rinehart and Winston",
             doi=None,
             url=None,
             language="en", isbn=None,
             citation="Gerbner, G. (1967). Mass media and human communication theory. In F. E. X. Dance (Ed.), Human Communication Theory. New York: Holt, Rinehart and Winston.",
             locator="chapter",
             locator_type="CHAPTER",
             supports="extension of the perceptual model to mass media",
             verified=True),
    ],
    "MC-021": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Elaboration Likelihood Model of Persuasion",
             title_fa="مدل احتمال بسط اقناع",
             authors="Richard E. Petty; John T. Cacioppo", year=1986,
             publisher="Advances in Experimental Social Psychology",
             doi="10.1016/S0065-2601(08)60214-2",
             url="https://www.sciencedirect.com/science/chapter/bookseries/pii/S0065260108602142",
             language="en", isbn=None,
             citation="Petty, R. E., & Cacioppo, J. T. (1986). The elaboration likelihood model of persuasion. Advances in Experimental Social Psychology, 19, 123-205. https://doi.org/10.1016/S0065-2601(08)60214-2",
             locator="19, 123-205",
             locator_type="PAGE",
             supports="central and peripheral routes as a function of elaboration likelihood",
             verified=True),
        dict(kind="BOOK",
             title_en="Communication and Persuasion: Central and Peripheral Routes to Attitude Change",
             title_fa="ارتباط و اقناع: مسیرهای مرکزی و پیرامونی تغییر نگرش",
             authors="Richard E. Petty; John T. Cacioppo", year=1986,
             publisher="Springer",
             doi="10.1007/978-1-4612-4964-1",
             url="https://link.springer.com/book/10.1007/978-1-4612-4964-1",
             language="en", isbn=None,
             citation="Petty, R. E., & Cacioppo, J. T. (1986). Communication and Persuasion: Central and Peripheral Routes to Attitude Change. New York: Springer. https://doi.org/10.1007/978-1-4612-4964-1",
             locator="book",
             locator_type="BOOK",
             supports="book-length statement of the dual-route model",
             verified=True),
    ],
}

ENRICH = {
    "MC-464": dict(
        needs_enrichment=False,
        level="پایه",
        related_approaches="مدل شانون و ویور؛ مدل لاسول؛ سواد رسانه‌ای؛ طراحی پیام؛ آموزش ارتباطات.",
        recommended_sources="«فرایند ارتباط: درآمدی بر نظریه و عمل» (برلو، ۱۹۶۰)؛ «ارتباط انسانی: گزارهٔ بنیادین» (برلو، ۱۹۷۷)؛ «نظریه‌های ارتباطات» (لیتل‌جان و فاس).",
        detailed_analysis=("۱. بنیان و منطق نظری\nدیوید برلو در کتاب ۱۹۶۰ خود، مدل منبع-پیام-کانال-گیرنده را به‌عنوان چارچوبی آموزشی برای فهم فرایند ارتباط عرضه کرد. "
                           "نکتهٔ متمایز مدل این است که هر چهار عنصر را مجموعه‌ای از عوامل می‌بیند: منبع و گیرنده هر دو دارای مهارت‌های ارتباطی، نگرش‌ها، دانش، نظام اجتماعی و فرهنگ‌اند؛ "
                           "پیام از رمز، محتوا و سازمان‌دهی ساخته می‌شود و کانال به حواس پنج‌گانه اشاره دارد.\n\n"
                           "۲. ساختارهای مفهومی\nمنبع، پیام، کانال، گیرنده و پنج عامل تأثیرگذار در دو سر مدل سازه‌های اصلی‌اند. "
                           "مدل تأکید می‌کند که تفاوت در تجربه و فرهنگ دو طرف، معنای دریافتی را تغییر می‌دهد.\n\n"
                           "۳. نمونه‌های تحلیلی\nدر یک آگهی، تفاوت مهارت رسانه‌ای و دانش مخاطب می‌تواند پیام یکسان را به دو معنای متفاوت بدل کند؛ در کلاس درس نیز معلم باید پیام را با نظام اجتماعی و فرهنگ دانش‌آموزان هم‌سو کند.\n\n"
                           "۴. نقدها و چالش‌ها\nمدل خطی است و بازخورد را به‌طور جدی وارد نمی‌کند؛ فرض می‌کند رمزگذاری و رمزگشایی همسان‌اند؛ به تعامل و مذاکرهٔ معنا کمتر می‌پردازد؛ و پنج عامل آن دشوار اندازه‌گیری می‌شوند. خود برلو بعدها بر محدودیت‌های این چارچوب تأکید کرد.\n\n"
                           "۵. سیر تاریخی\nکتاب ۱۹۶۰ سال‌ها متن درسی استاندارد ارتباطات بود و بر نسل‌های پژوهشگر اثر گذاشت؛ بازنگری برلو در ۱۹۷۷ نشان داد او خود مدل را نقطهٔ شروع می‌دانست، نه توصیف نهایی.\n\n"
                           "۶. جایگاه در بحث روز\nدر آموزش سواد رسانه‌ای و طراحی پیام سلامت، چک‌لیست پنج عامل برلو هنوز ابزار سادهٔ تحلیل مخاطب و فرستنده است."),
    ),
    "MC-309": dict(
        needs_enrichment=False,
        level="میان",
        related_approaches="مدل شانون و ویور؛ دروازه‌بانی خبر؛ نظریهٔ کاشت؛ ادراک رسانه‌ای؛ نشانه‌شناسی.",
        recommended_sources="«به‌سوی مدلی عمومی برای ارتباط» (گربر، ۱۹۵۶)؛ «رسانه‌های جمعی و نظریهٔ ارتباط انسانی» (گربر، ۱۹۶۷)؛ «نظریهٔ کاشت» (گربر و گراس، ۱۹۷۶).",
        detailed_analysis=("۱. بنیان و منطق نظری\nگربر (۱۹۵۶) در مقالهٔ «به‌سوی مدلی عمومی برای ارتباط» مدلی ادراکی عرضه کرد که ارتباط را فرایندی شامل رویداد بیرونی، ادراک و گزینش آن رویداد، تبدیل به پیام و انتقال آن می‌دید. "
                           "برخلاف مدل‌های انتقالی ساده، گربر بر ادراک فعال و گزینش تأکید کرد: آنچه منتقل می‌شود، خودِ رویداد نیست، بلکه ادراکی از رویداد است که به پیام تبدیل شده. "
                           "او مدل را در دو بُعد افقی (زنجیرهٔ رویداد تا گیرنده) و عمودی (بازخورد و تفسیر) صورت‌بندی کرد و در ۱۹۶۷ آن را برای رسانه‌های جمعی بسط داد.\n\n"
                           "۲. ساختارهای مفهومی\nرویداد، ادراک، گزینش، تبدیل به سیگنال، پیام، بازخورد و ابعاد افقی و عمودی سازه‌های اصلی‌اند.\n\n"
                           "۳. نمونه‌های تحلیلی\nدر پوشش خبری یک اعتراض، خبرنگار نه رویداد خام بلکه ادراک گزینش‌شدهٔ خود را به پیام تبدیل می‌کند؛ بازخورد مخاطب و سیاست رسانه، این گزینش را در چرخهٔ بعدی شکل می‌دهد.\n\n"
                           "۴. نقدها و چالش‌ها\nمدل پیچیده و پراجزاست و کاربرد تجربی آن دشوار است؛ سنجش ادراک و گزینش در عمل مبهم می‌ماند؛ فرض فعال‌بودن گیرنده همیشه برقرار نیست؛ و مرز میان پیام و سیگنال روشن نیست.\n\n"
                           "۵. سیر تاریخی\nمقالهٔ ۱۹۵۶ یکی از مدل‌های مرجع مبانی ارتباطات شد، بسط ۱۹۶۷ آن را به رسانه‌های جمعی گره زد و مسیر پژوهش‌های بعدی گربر در نظریهٔ کاشت را هموار کرد.\n\n"
                           "۶. جایگاه در بحث روز\nدر تحلیل بازنمایی رسانه‌ای و تولید تصویر از رویدادها، تأکید گربر بر ادراک و گزینش هنوز چارچوبی دقیق برای نقد بی‌طرفی ظاهری رسانه است."),
    ),
    "MC-021": dict(
        needs_enrichment=False,
        level="میان",
        related_approaches="نظریهٔ اقناع؛ مدل دانش اقناع؛ مدل ظرفیت محدود؛ سلسله‌مراتب اثرات؛ روان‌شناسی شناختی.",
        recommended_sources="«مدل احتمال بسط اقناع» (پتی و کاسیوپو، ۱۹۸۶)؛ «ارتباط و اقناع: مسیرهای مرکزی و پیرامونی» (پتی و کاسیوپو، ۱۹۸۶)؛ «نظریه‌های اقناع» (اوکیف، ۲۰۰۲).",
        detailed_analysis=("۱. بنیان و منطق نظری\nپتی و کاسیوپو (۱۹۸۶) مدل احتمال بسط را عرضه کردند تا توضیح دهند چرا گاهی استدلال قوی و گاهی نشانه‌های سطحی مانند جذابیت گوینده اقناع می‌کند. "
                           "ادعای مرکزی این است که احتمال بسط پیام — یعنی میزان پردازش شناختی آن — به انگیزش و توانایی گیرنده بستگی دارد. "
                           "در بسط بالا، مسیر مرکزی فعال می‌شود و کیفیت استدلال تعیین‌کننده است؛ در بسط پایین، مسیر پیرامونی با نشانه‌های ساده کار می‌کند.\n\n"
                           "۲. ساختارهای مفهومی\nمسیر مرکزی، مسیر پیرامونی، احتمال بسط، انگیزش، توانایی و نشانه‌های پیرامونی سازه‌های اصلی‌اند. "
                           "تغییر نگرش از مسیر مرکزی پایدارتر و مقاوم‌تر دانسته می‌شود.\n\n"
                           "۳. نمونه‌های تحلیلی\nدر تبلیغ یک محصول پرریسک و گران، مخاطب انگیزهٔ پردازش دارد و استدلال‌های محتوایی اثر می‌گذارد؛ در خرید کم‌ریسک، چهرهٔ معتبر یا موسیقی می‌تواند بدون پردازش عمیق تصمیم را تغییر دهد.\n\n"
                           "۴. نقدها و چالش‌ها\nمرز دو مسیر همیشه روشن نیست و پردازش مختلط را کم توضیح می‌دهد؛ سنجش احتمال بسط به شاخص‌های غیرمستقیم وابسته است؛ نقش احساس و عادت کم‌رنگ می‌شود؛ و برخی یافته‌های تجربی در بازتولید محدود بوده‌اند.\n\n"
                           "۵. سیر تاریخی\nپژوهش ۱۹۸۱ دربارهٔ درگیری شخصی و استدلال، مقدمهٔ مدل بود؛ مقاله و کتاب ۱۹۸۶ آن را تثبیت کردند و امروز یکی از پراستنادترین چارچوب‌های اقناع است.\n\n"
                           "۶. جایگاه در بحث روز\nدر تبلیغ هدفمند شبکه‌های اجتماعی و مقابله با اطلاعات نادرست، پرسش از انگیزش و توانایی پردازش مخاطب، محور طراحی پیام و مداخله شده است."),
    ),
}

NAME_FIX = {}

YEAR_FIX = {
    "MC-464": "year=1960 (Berlo 1960 verified via archive.org); replaced generic template analysis",
    "MC-309": "year=1956 (Gerbner 1956, DOI 10.1007/BF02717110); Gerbner 1967 verified; replaced generic template analysis",
    "MC-021": "year=1986 (Petty & Cacioppo 1986); both sources verified with DOIs; replaced generic template analysis",
}
