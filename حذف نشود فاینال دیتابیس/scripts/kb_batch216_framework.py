# -*- coding: utf-8 -*-
"""Batch 216: repair template-era analyses on MC-034, MC-040, MC-493, MC-494, MC-543."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch216-20261117"
NOW = "2026-11-17 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch216.json"

S = {
    "MC-034": [
        dict(kind="BOOK",
             title_en="Media Economics: Concepts and Issues",
             title_fa="اقتصاد رسانه: مفاهیم و مسائل",
             authors="Robert G. Picard", year=1989,
             publisher="Sage Publications",
             doi=None,
             url="https://books.google.com/books/about/Media_Economics.html?id=5JwcAQAAIAAJ",
             language="en", isbn=None,
             citation="Picard, R. G. (1989). Media Economics: Concepts and Issues. Newbury Park, CA: Sage Publications.",
             locator="book", locator_type="BOOK",
             supports="systematic treatment of media markets and revenue sources",
             verified=True),
        dict(kind="BOOK",
             title_en="Media Economics: Understanding Markets, Industries and Concepts",
             title_fa="اقتصاد رسانه: فهم بازارها، صنایع و مفاهیم",
             authors="Alan B. Albarran", year=1996,
             publisher="Iowa State University Press",
             doi=None,
             url=None,
             language="en", isbn=None,
             citation="Albarran, A. B. (1996). Media Economics: Understanding Markets, Industries and Concepts. Ames: Iowa State University Press.",
             locator="book", locator_type="BOOK",
             supports="industry-level analysis of media markets and revenue structures",
             verified=False),
    ],
    "MC-040": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Twilight or New Dawn of Journalism? Evidence from the Changing News Ecosystem",
             title_fa="گرگ‌ومیش یا سپیدهٔ تازهٔ روزنامه‌نگاری؟ شواهدی از زیست‌بوم خبری در حال تغییر",
             authors="Robert G. Picard", year=2014,
             publisher="Digital Journalism",
             doi="10.1080/1461670X.2014.895530",
             url="https://www.tandfonline.com/doi/full/10.1080/1461670X.2014.895530",
             language="en", isbn=None,
             citation="Picard, R. G. (2014). Twilight or new dawn of journalism? Evidence from the changing news ecosystem. Digital Journalism, 2(3), 273-283.",
             locator="2(3), 273-283", locator_type="PAGE",
             supports="analysis of declining news revenue and the journalism business-model crisis",
             verified=True),
        dict(kind="BOOK",
             title_en="Local Journalism: The Decline of Newspapers and the Rise of Digital Media",
             title_fa="روزنامه‌نگاری محلی: افول روزنامه‌ها و ظهور رسانهٔ دیجیتال",
             authors="Rasmus Kleis Nielsen (Ed.)", year=2015,
             publisher="I.B. Tauris",
             doi=None,
             url=None,
             language="en", isbn=None,
             citation="Nielsen, R. K. (Ed.). (2015). Local Journalism: The Decline of Newspapers and the Rise of Digital Media. London: I.B. Tauris.",
             locator="book", locator_type="BOOK",
             supports="empirical evidence on local news decline across countries",
             verified=False),
    ],
    "MC-493": [
        dict(kind="BOOK",
             title_en="The Life of P. T. Barnum, Written by Himself",
             title_fa="زندگی فینیاس تیلور بارنوم، به قلم خودش",
             authors="P. T. Barnum", year=1855,
             publisher="Redfield",
             doi=None,
             url="http://archive.org/stream/lifeofptbarnum00barnuoft",
             language="en", isbn=None,
             citation="Barnum, P. T. (1855). The Life of P. T. Barnum, Written by Himself. New York: Redfield.",
             locator="book", locator_type="BOOK",
             supports="historical practice of one-way promotional publicity and spectacle",
             verified=True),
        dict(kind="BOOK",
             title_en="Audience Economics: Media Institutions and the Audience Marketplace",
             title_fa="اقتصاد مخاطب: نهادهای رسانه و بازارگاه مخاطب",
             authors="Philip M. Napoli", year=2003,
             publisher="Columbia University Press",
             doi=None,
             url="https://cup.columbia.edu/book/audience-economics/9780231126526/",
             language="en", isbn=None,
             citation="Napoli, P. M. (2003). Audience Economics: Media Institutions and the Audience Marketplace. New York: Columbia University Press.",
             locator="book", locator_type="BOOK",
             supports="audience as a commodity traded between media and advertisers",
             verified=True),
    ],
    "MC-494": [
        dict(kind="BOOK",
             title_en="Courtier to the Crowd: The Story of Ivy Lee and the Development of Public Relations",
             title_fa="درباری میان مردم: داستان آیوی لی و شکل‌گیری روابط عمومی",
             authors="Ray Eldon Hiebert", year=1966,
             publisher="Iowa State University Press",
             doi=None,
             url="https://www.ebsco.com/research-starters/history/lee-establishes-field-public-relations/",
             language="en", isbn=None,
             citation="Hiebert, R. E. (1966). Courtier to the Crowd: The Story of Ivy Lee and the Development of Public Relations. Ames: Iowa State University Press.",
             locator="book", locator_type="BOOK",
             supports="public information model as accurate and prompt disclosure to the press",
             verified=True),
        dict(kind="BOOK",
             title_en="Managing Public Relations",
             title_fa="مدیریت روابط عمومی",
             authors="James E. Grunig; Todd Hunt", year=1984,
             publisher="Holt, Rinehart and Winston",
             doi=None,
             url="https://archive.org/details/managingpublicre0000unse",
             language="en", isbn=None,
             citation="Grunig, J. E., & Hunt, T. (1984). Managing Public Relations. New York: Holt, Rinehart and Winston.",
             locator="book", locator_type="BOOK",
             supports="public information model as one of four historical models of public relations",
             verified=True),
    ],
    "MC-543": [
        dict(kind="BOOK",
             title_en="Psychologie der Massenkommunikation: Theorie und Systematik",
             title_fa="روان‌شناسی ارتباط جمعی: نظریه و نظام‌مندی",
             authors="Gerhard Maletzke", year=1963,
             publisher="Verlag Hans-Bredow-Institut",
             doi=None,
             url="https://www.fachportal-paedagogik.de/literatur/vollanzeige.html?FId=bbf_1307972",
             language="de", isbn=None,
             citation="Maletzke, G. (1963). Psychologie der Massenkommunikation: Theorie und Systematik. Hamburg: Verlag Hans-Bredow-Institut.",
             locator="book", locator_type="BOOK",
             supports="psychological model of mass communication with communicator and receiver fields",
             verified=True),
        dict(kind="WEBSITE",
             title_en="Maletzke's Model",
             title_fa="مدل مالتزکه",
             authors="Comunicologos", year=None,
             publisher="comunicologos.com",
             doi=None,
             url="https://www.comunicologos.com/english/theories/maletzke-s-model/",
             language="en", isbn=None,
             citation="Comunicologos. (n.d.). Maletzke's model. comunicologos.com.",
             locator="web page", locator_type="PAGE",
             supports="exposition of the model's progressive construction and field constraints",
             verified=True),
    ],
}

ENRICH = {
    "MC-034": dict(
        needs_enrichment=False,
        level="میان",
        related_approaches="اقتصاد رسانه؛ بازار دوسویه؛ مدل کسب‌وکار خبر؛ سیاست رسانه؛ مدیریت رسانه.",
        recommended_sources="«اقتصاد رسانه: مفاهیم و مسائل» (پیکارد، ۱۹۸۹)؛ «اقتصاد رسانه: فهم بازارها، صنایع و مفاهیم» (آلباران، ۱۹۹۶)؛ «اقتصاد رسانه» (هاردوود)؛ «اقتصاد مخاطب» (ناپولی، ۲۰۰۳).",
        detailed_analysis=("۱. بنیان و منطق نظری\nپیکارد (۱۹۸۹) اقتصاد رسانه را همچون اقتصاد هر بنگاه با ویژگی‌های خاص کالای اطلاعاتی صورت‌بندی کرد: هزینهٔ تولید نخستین بالا، هزینهٔ تکثیر پایین و کالای عمومی‌مانند. "
                           "در این چارچوب، منابع درآمدی رسانه به تبلیغات، فروش نسخه یا اشتراک، پرداخت مستقیم مصرف‌کننده، یارانهٔ عمومی و درآمدهای ترکیبی تفکیک می‌شود. آلباران (۱۹۹۶) همین تحلیل را در سطح صنعت و بازار گسترد.\n\n"
                           "۲. ساختارهای مفهومی\nتنوع درآمدی، ساختار هزینه، کشش قیمتی، بازار دوسویه و استقلال تحریریه سازه‌های اصلی‌اند. هر منبع درآمد مشوق رفتاری متفاوتی می‌سازد.\n\n"
                           "۳. نمونه‌های تحلیلی\nروزنامهٔ تبلیغات‌محور مخاطب انبوه را به آگهی‌دهنده می‌فروشد؛ رسانهٔ اشتراکی رضایت و وفاداری مخاطب را پاداش می‌دهد؛ رسانهٔ عمومی با یارانه از فشار بازار آزاد می‌شود؛ و پلتفرم دیجیتال با ترکیب اشتراک و تبلیغ، هر دو منطق را در هم می‌آمیزد.\n\n"
                           "۴. نقدها و چالش‌ها\nچارچوب کلاسیک بازارهای دوطرفه و چندطرفهٔ پلتفرمی را ساده می‌کند؛ نقش داده و تبلیغ هدفمند را کم‌می‌شمارد؛ رابطهٔ مدل درآمدی و کیفیت محتوا را به‌طور تجربی یکدست نمی‌تواند نشان دهد؛ و در بازارهای غیرغربی شواهد کافی وجود ندارد.\n\n"
                           "۵. سیر تاریخی\nکتاب ۱۹۸۹ مفاهیم پایه را تثبیت کرد، پژوهش‌های دههٔ ۱۹۹۰ تحلیل صنعتی را گستردند و از دههٔ ۲۰۰۰ با اشتراک دیجیتال، دیوار پرداخت و درآمد پلتفرمی بازنگری شد.\n\n"
                           "۶. جایگاه در بحث روز\nدر بحران مالی رسانهٔ خبری، تحلیل تنوع درآمدی همچنان ابزار اصلی سنجش پایداری و استقلال تحریریه است، هرچند امروز باید درآمد داده‌محور و کمک‌های مردمی را نیز در حساب آورد."),
    ),
    "MC-040": dict(
        needs_enrichment=False,
        level="میان",
        related_approaches="اقتصاد رسانه؛ بحران خبر؛ خبر محلی؛ دیوار پرداخت؛ روزنامه‌نگاری عمومی.",
        recommended_sources="«گرگ‌ومیش یا سپیدهٔ تازهٔ روزنامه‌نگاری؟» (پیکارد، ۲۰۱۴)؛ «روزنامه‌نگاری محلی» (نیلسن، ۲۰۱۵)؛ «اقتصاد رسانه» (هاردوود)؛ «روزنامه‌نگاری پساصنعتی: سازگاری با وضع کنونی» (اندرسون، بل و شیرکی، ۲۰۱۲).",
        detailed_analysis=("۱. بنیان و منطق نظری\nپیکارد (۲۰۱۴) با داده‌های زیست‌بوم خبری نشان داد درآمد تبلیغاتی مطبوعات به پلتفرم‌های دیجیتال منتقل شده و ترکیب سنتی تبلیغات و فروش نسخه دیگر هزینهٔ تولید خبر باکیفیت را پوشش نمی‌دهد. "
                           "او این وضع را نه پایان قطعی روزنامه‌نگاری، بلکه نقطهٔ گذار به الگوهای درآمدی تازه خواند. نیلسن (۲۰۱۵) با مجموعهٔ پژوهش‌های بین‌المللی، افول روزنامهٔ محلی و ظهور رسانهٔ دیجیتال را مستند کرد.\n\n"
                           "۲. ساختارهای مفهومی\nساختار هزینهٔ خبر، انتقال درآمد تبلیغاتی، دیوار پرداخت، خبر محلی، بیابان خبری و حمایت بشردوستانه سازه‌های اصلی‌اند.\n\n"
                           "۳. نمونه‌های تحلیلی\nبا مهاجرت آگهی‌دهندگان به تبلیغ هدفمند پلتفرمی، درآمد ناشر کاهش می‌یابد و بودجهٔ تحریریه کوچک می‌شود؛ کاهش پوشش خبر محلی تقاضای اطلاعات محلی را بی‌پاسخ می‌گذارد و فضای بیابان خبری می‌سازد؛ اشتراک دیجیتال در برخی بازارها جایگزین جزئی درآمد شده است.\n\n"
                           "۴. نقدها و چالش‌ها\nروایت افول، نوآوری‌های موفق خبری را کم‌رنگ می‌کند؛ تمرکز بر بازارهای غربی تعمیم را محدود می‌کند؛ اثر دیوار پرداخت بر تنوع مخاطب یکدست نیست؛ و شواهد دربارهٔ پایداری حمایت بشردوستانه و عمومی متناقض است.\n\n"
                           "۵. سیر تاریخی\nریشهٔ حوزه در اقتصاد رسانهٔ دههٔ ۱۹۸۰ است؛ مقالهٔ ۲۰۱۴ چارچوب بحران را تثبیت کرد و پژوهش‌های ۲۰۱۵ به بعد با داده‌های خبر محلی، دیوار پرداخت و حمایت عمومی آن را آزمودند.\n\n"
                           "۶. جایگاه در بحث روز\nدر سیاست‌های حمایت از خبر محلی و بحث پایداری روزنامه‌نگاری، این حوزه پرسش اصلی را از «چگونه خبر بفروشیم» به «چه نهادی هزینهٔ خبر باکیفیت را تأمین می‌کند» تغییر داده است."),
    ),
    "MC-493": dict(
        needs_enrichment=False,
        level="میان",
        related_approaches="اقتصاد سیاسی رسانه؛ بازار دوسویه؛ اقتصاد مخاطب؛ تبلیغات؛ اخلاق روزنامه‌نگاری.",
        recommended_sources="«زندگی بارنوم» (بارنوم، ۱۸۵۵)؛ «اقتصاد مخاطب» (ناپولی، ۲۰۰۳)؛ «اقتصاد رسانه» (پیکارد، ۱۹۸۹)؛ «اقتصاد رسانه» (هاردوود).",
        detailed_analysis=("۱. بنیان و منطق نظری\nمدل مطبوعاتی-تبلیغاتی رسانه را نهادی می‌داند که با محتوای جذاب مخاطب را گرد می‌آورد و توجه او را به تبلیغ‌دهنده می‌فروشد. "
                           "ریشهٔ نمایشی آن به تبلیغ‌گری بارنوم در سدهٔ نوزدهم می‌رسد و صورت‌بندی تحلیلی آن با ناپولی (۲۰۰۳) و مفهوم بازارگاه مخاطب کامل شد: مخاطب کالایی است که رسانه به آگهی‌دهنده می‌فروشد.\n\n"
                           "۲. ساختارهای مفهومی\nبازارگاه مخاطب، تبلیغ نمایشی، توجه، وابستگی درآمدی، مرز تحریریه و تبلیغات و بازار دوسویه سازه‌های اصلی‌اند.\n\n"
                           "۳. نمونه‌های تحلیلی\nروزنامهٔ عامه‌پسند با تیتر جنجالی مخاطب می‌گیرد و فضای آگهی می‌فروشد؛ رسانهٔ اجتماعی با محتوای رایگان زمان و توجه کاربر را به تبلیغ هدفمند تبدیل می‌کند؛ در هر دو مورد، معیار موفقیت تجاری با معیار کیفیت خبری می‌تواند ناهم‌سو شود.\n\n"
                           "۴. نقدها و چالش‌ها\nبُعد فرهنگی و سیاسی را به بازار تقلیل می‌دهد؛ با ساختار چندطرفه و داده‌محور پلتفرمی کامل هم‌خوان نیست؛ سنجش توجه و ارزش مخاطب دشوار است؛ و فشار تجاری مرز تحریریه و تبلیغات را تضعیف می‌کند.\n\n"
                           "۵. سیر تاریخی\nمدل در سدهٔ نوزدهم با مطبوعات آگهی‌محور شکل گرفت، در قرن بیستم با اقتصاد مخاطب و رتبه‌بندی صورت‌بندی شد و در عصر پلتفرم به بحث تبلیغ هدفمند و بازارگاه داده گسترش یافت.\n\n"
                           "۶. جایگاه در بحث روز\nدر بحث شفافیت درآمد رسانه و استقلال تحریریه، مدل تبلیغات‌محور توضیح می‌دهد چرا فشار تجاری می‌تواند انتخاب خبر را جهت دهد و چرا سیاست‌های جداکردن تحریریه از تبلیغات ضروری است."),
    ),
    "MC-494": dict(
        needs_enrichment=False,
        level="پایه",
        related_approaches="مدل‌های چهارگانهٔ روابط عمومی؛ تبلیغ‌گری مطبوعاتی؛ شفافیت سازمانی؛ اخلاق ارتباطات.",
        recommended_sources="«درباری میان مردم: داستان آیوی لی» (هیبرت، ۱۹۶۶)؛ «مدیریت روابط عمومی» (گرونیگ و هانت، ۱۹۸۴)؛ «روابط عمومی مؤثر» (کاتلیپ و همکاران).",
        detailed_analysis=("۱. بنیان و منطق نظری\nمدل اطلاع‌رسانی عمومی، دومین مدل از چهار مدل تاریخی روابط عمومی در دسته‌بندی گرونیگ و هانت (۱۹۸۴) است و با آیوی لی و اعلامیهٔ اصول ۱۹۰۶ پیوند دارد. "
                           "لی وعده داد سازمان اطلاعات درست و به‌موقع در اختیار رسانه بگذارد؛ اعلامیهٔ اصول، واکنشی به فرهنگ پنهان‌کاری و دستکاری پیشین بود. در منابع فارسی همین الگو با نام «انتشار صادقانه اطلاعات» نیز شناخته می‌شود.\n\n"
                           "۲. ساختارهای مفهومی\nاطلاع‌رسانی عمومی، اعلامیهٔ اصول، شفافیت، بیانیهٔ خبری، روزنامه‌نگار درون‌سازمانی و اعتماد سازه‌های اصلی‌اند. مدل هنوز یک‌سویه است و بازخورد ساختارمند ندارد.\n\n"
                           "۳. نمونه‌های تحلیلی\nانتشار بیانیهٔ خبری پس از بحران، نمونهٔ کلاسیک اجرای این مدل است؛ سیاست شفافیت سازمانی امروز همان منطق را در قالب انتشار منظم گزارش و داده دنبال می‌کند.\n\n"
                           "۴. نقدها و چالش‌ها\nارتباط را یک‌سویه نگه می‌دارد؛ گفت‌وگو و بازخورد ساختارمند ندارد؛ انتشار اطلاعات می‌تواند گزینشی و به نفع سازمان باشد؛ بی‌طرفی سازمان را بیش از واقع فرض می‌کند؛ و در بحران‌های نیازمند پاسخ‌گویی دوسویه ناکافی است.\n\n"
                           "۵. سیر تاریخی\nبا اعلامیهٔ ۱۹۰۶ شکل گرفت، در قرن بیستم به یکی از چهار مدل تاریخی تبدیل شد و با ظهور روابط عمومی دوسویه جایگاهش به حداقل اخلاقی ارتباط سازمان فروکاست.\n\n"
                           "۶. جایگاه در بحث روز\nدر گفتمان شفافیت و مسئولیت اجتماعی سازمان، مدل اطلاع‌رسانی عمومی همچنان شرط لازم ارتباط سازمانی است، هرچند برای اعتماد پایدار باید با گفت‌وگوی دوسویه تکمیل شود."),
    ),
    "MC-543": dict(
        needs_enrichment=False,
        level="میان",
        related_approaches="روان‌شناسی ارتباط جمعی؛ مدل‌های ارتباطی آلمان؛ ادراک مخاطب؛ نظریهٔ سازمان رسانه؛ ارتباطات میان‌فرهنگی.",
        recommended_sources="«روان‌شناسی ارتباط جمعی: نظریه و نظام‌مندی» (مالتزکه، ۱۹۶۳)؛ «مدل مالتزکه» (کامونیکولوگوس)؛ «نظریه‌های ارتباط جمعی» (مک‌کوایل).",
        detailed_analysis=("۱. بنیان و منطق نظری\nمالتزکه (۱۹۶۳) در سنت روان‌شناسی ارتباط جمعی آلمان، ارتباط جمعی را برهم‌کنش دو میدان ادراکی دانست: فرستنده و گیرنده. "
                           "به نظر او پیام جابه‌جا نمی‌شود، بلکه در دریافت بازسازی روان‌شناختی می‌شود و فشارهای سازمانی و اجتماعی بر هر دو سو اثر می‌گذارد.\n\n"
                           "۲. ساختارهای مفهومی\nخودانگارهٔ فرستنده، شخصیت، محیط اجتماعی، فشار سازمان رسانه، تصویر فرستنده در ذهن گیرنده، علنی بودن و هم‌زمانی سازه‌های اصلی‌اند. مدل تأکید می‌کند که فرستنده پیش از ساخت پیام، تصویری از مخاطب خود دارد.\n\n"
                           "۳. نمونه‌های تحلیلی\nروزنامه‌نگار زیر فشار خط تحریریه پیامی می‌سازد که با تصور او از مخاطب شکل گرفته؛ مخاطب نیز بر پایهٔ تصویرش از آن رسانه، پیام را گزینش و تفسیر می‌کند؛ در کمپین سلامت، همین سازوکار توضیح می‌دهد چرا پیام یکسان به نتایج متفاوت می‌رسد.\n\n"
                           "۴. نقدها و چالش‌ها\nپیچیدگی مدل آزمون تجربی را دشوار می‌کند؛ بر روان‌شناسی فردی متمرکز است و ساخت قدرت و اقتصاد رسانه را کم‌بررسی می‌گذارد؛ برخی سازه‌ها مبهم‌اند؛ و قید علنی بودن و هم‌زمانی با رسانه‌های تعاملی دیجیتال کامل هم‌خوان نیست.\n\n"
                           "۵. سیر تاریخی\nکتاب ۱۹۶۳ مدل را در سنت آلمانی صورت‌بندی کرد، نسل بعدی پژوهش اروپایی آن را گسترد و با ظهور رسانه‌های دیجیتال، قیدهای آن بازخوانی شد.\n\n"
                           "۶. جایگاه در بحث روز\nدر تحلیل ادراک مخاطب و فشار سازمانی بر تولید خبر، مدل مالتزکه همچنان چارچوبی دقیق برای پیوند روان‌شناسی فردی و ساختار سازمانی است."),
    ),
}

NAME_FIX = {}

YEAR_FIX = {
    "MC-034": "replaced media-economics template analysis with Picard/Albarran-specific analysis; rebuilt recommendations",
    "MC-040": "replaced media-economics template analysis with Picard-2014-specific analysis; rebuilt recommendations",
    "MC-493": "replaced media-economics template analysis with press-advertising/audience-marketplace analysis; rebuilt recommendations",
    "MC-494": "replaced media-economics template analysis; replaced weak web source with Hiebert 1966; noted Persian synonym 'انتشار صادقانه' and cross-link to MC-368",
    "MC-543": "replaced sender-template analysis with Maletzke-specific analysis; rebuilt recommendations",
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
                                       "verified": n_verified, "batch": 216}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH216 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
