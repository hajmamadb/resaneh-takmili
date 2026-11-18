# -*- coding: utf-8 -*-
"""Batch 196: SFL-011..SFL-015 (SUBFIELD)."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch196-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch196.json"

SFL_MAP = {"entity_type": "SUBFIELD", "content_type": "زیرحوزه نوظهور (Subfield)",
           "needs_review": False, "taxonomy_section": "3-1"}

S = {
    "SFL-011": [
        dict(kind="BOOK",
             title_en="Post-Broadcast Democracy: How Media Choice Increases Inequality in Political Involvement and Polarizes Elections",
             title_fa="دموکراسی پس از پخش فراگیر: چگونه انتخاب رسانه‌ای نابرابری مشارکت سیاسی را افزایش و انتخابات را قطبی می‌کند",
             authors="Markus Prior", year=2007,
             publisher="Cambridge University Press",
             doi=None,
             url="https://www.cambridge.org/core/books/postbroadcast-democracy/A0D17A3CD156A0D1BB4318EE5DBCC60B",
             language="en", isbn=None,
             citation="Prior, M. (2007). Post-Broadcast Democracy: How Media Choice Increases Inequality in Political Involvement and Polarizes Elections. Cambridge: Cambridge University Press.",
             locator="chapters on media choice, selective exposure and political polarization",
             locator_type="CHAPTER",
             supports="the argument that expanded media choice increases selective exposure and polarizes political involvement",
             verified=True),
        dict(kind="BOOK",
             title_en="#Republic: Divided Democracy in the Age of Social Media",
             title_fa="جمهوری هشتگ: دموکراسی تقسیم‌شده در عصر رسانه‌های اجتماعی",
             authors="Cass R. Sunstein", year=2017,
             publisher="Princeton University Press",
             doi=None,
             url="https://press.princeton.edu/books/hardcover/9780691175515/republic",
             language="en", isbn="9780691175515",
             citation="Sunstein, C. R. (2017). #Republic: Divided Democracy in the Age of Social Media. Princeton, NJ: Princeton University Press.",
             locator="chapters on echo chambers, filter bubbles and fragmentation of public debate",
             locator_type="CHAPTER",
             supports="the account of echo chambers and personalized media as threats to shared public deliberation",
             verified=True),
    ],
    "SFL-012": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Defining Strategic Communication",
             title_fa="تعریف ارتباطات راهبردی",
             authors="Kirk Hallahan; Derina Holtzhausen; Betteke van Ruler; Dejan Verčič; Krishnamurthy Sriramesh", year=2007,
             publisher="International Journal of Strategic Communication",
             doi="10.1080/15531180701285244",
             url="https://www.tandfonline.com/doi/abs/10.1080/15531180701285244",
             language="en", isbn=None,
             citation="Hallahan, K., Holtzhausen, D., van Ruler, B., Verčič, D., & Sriramesh, K. (2007). Defining Strategic Communication. International Journal of Strategic Communication, 1(1), 3-35. https://doi.org/10.1080/15531180701285244",
             locator="1(1), 3-35",
             locator_type="PAGE",
             supports="the definition of strategic communication as the purposeful use of communication by an organization to fulfill its mission",
             verified=True),
        dict(kind="BOOK",
             title_en="Strategic Communication: Origins, Concepts, and Current Debates",
             title_fa="ارتباطات راهبردی: خاستگاه‌ها، مفاهیم و مناقشات کنونی",
             authors="Christopher Paul", year=2011,
             publisher="Praeger",
             doi=None,
             url="https://books.google.com/books/about/Strategic_Communication_Origins_Concepts.html?id=gKRpfN_0ezQC",
             language="en", isbn=None,
             citation="Paul, C. (2011). Strategic Communication: Origins, Concepts, and Current Debates. Santa Barbara, CA: Praeger.",
             locator="chapters on the definitional debate and the role of actions as communication",
             locator_type="CHAPTER",
             supports="the argument that strategic communication includes actions and not only formal messages",
             verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Cognitive Warfare: A Conceptual Analysis of the NATO ACT Cognitive Warfare Concept",
             title_fa="جنگ شناختی: تحلیلی مفهومی از مفهوم جنگ شناختی فرماندهی تحول ناتو",
             authors="Christopher Deppe; et al.", year=2024,
             publisher="Frontiers in Big Data",
             doi="10.3389/fdata.2024.1452129",
             url="https://www.frontiersin.org/journals/big-data/articles/10.3389/fdata.2024.1452129/full",
             language="en", isbn=None,
             citation="Deppe, C., et al. (2024). Cognitive warfare: A conceptual analysis of the NATO ACT cognitive warfare concept. Frontiers in Big Data, 7, Article 1452129. https://doi.org/10.3389/fdata.2024.1452129",
             locator="7, Article 1452129",
             locator_type="PAGE",
             supports="the conceptual analysis of cognitive warfare and its defining attributes in the NATO framework",
             verified=True),
    ],
    "SFL-013": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="New Directions in Cryptography",
             title_fa="مسیرهای تازه در رمزنگاری",
             authors="Whitfield Diffie; Martin E. Hellman", year=1976,
             publisher="IEEE Transactions on Information Theory",
             doi="10.1109/TIT.1976.1055638",
             url="https://ieeexplore.ieee.org/document/1055638/",
             language="en", isbn=None,
             citation="Diffie, W., & Hellman, M. E. (1976). New directions in cryptography. IEEE Transactions on Information Theory, 22(6), 644-654. https://doi.org/10.1109/TIT.1976.1055638",
             locator="22(6), 644-654",
             locator_type="PAGE",
             supports="the public-key cryptography foundation that enables secure communication without prior shared secrets",
             verified=True),
        dict(kind="BOOK",
             title_en="Privacy in Context: Technology, Policy, and the Integrity of Social Life",
             title_fa="حریم خصوصی در بافت: فناوری، سیاست و یکپارچگی زندگی اجتماعی",
             authors="Helen Nissenbaum", year=2009,
             publisher="Stanford University Press",
             doi=None,
             url="https://www.sup.org/books/law/privacy-context",
             language="en", isbn=None,
             citation="Nissenbaum, H. (2009). Privacy in Context: Technology, Policy, and the Integrity of Social Life. Stanford, CA: Stanford University Press.",
             locator="chapters on contextual integrity and norms of information flow",
             locator_type="CHAPTER",
             supports="the theory of contextual integrity as the standard for evaluating privacy violations",
             verified=True),
    ],
    "SFL-014": [
        dict(kind="BOOK",
             title_en="The Hybrid Media System: Politics and Power",
             title_fa="نظام رسانه‌ای ترکیبی: سیاست و قدرت",
             authors="Andrew Chadwick", year=2017,
             publisher="Oxford University Press",
             doi=None,
             url="https://academic.oup.com/book/1922",
             language="en", isbn="9780190696733",
             citation="Chadwick, A. (2017). The Hybrid Media System: Politics and Power (2nd ed.). New York: Oxford University Press.",
             locator="chapters on older and newer media logics and hybridity in political communication",
             locator_type="CHAPTER",
             supports="the hybrid media system theory of interaction between older and newer media logics",
             verified=True),
        dict(kind="BOOK",
             title_en="Network Propaganda: Manipulation, Disinformation, and Radicalization in American Politics",
             title_fa="پروپاگاندای شبکه‌ای: دستکاری، اطلاعات نادرست و رادیکال‌شدن در سیاست آمریکا",
             authors="Yochai Benkler; Robert Faris; Hal Roberts", year=2018,
             publisher="Oxford University Press",
             doi=None,
             url="https://global.oup.com/academic/product/network-propaganda-9780190923631",
             language="en", isbn="9780190923631",
             citation="Benkler, Y., Faris, R., & Roberts, H. (2018). Network Propaganda: Manipulation, Disinformation, and Radicalization in American Politics. New York: Oxford University Press.",
             locator="chapters on asymmetric polarization and the architecture of the media ecosystem",
             locator_type="CHAPTER",
             supports="the empirical account of an asymmetric media ecosystem and its role in propaganda and radicalization",
             verified=True),
    ],
    "SFL-015": [
        dict(kind="BOOK",
             title_en="Convergence Culture: Where Old and New Media Collide",
             title_fa="فرهنگ همگرایی: جایی که رسانه‌های کهن و نوین به هم می‌رسند",
             authors="Henry Jenkins", year=2006,
             publisher="New York University Press",
             doi=None,
             url="https://nyupress.org/9780814742815/convergence-culture/",
             language="en", isbn=None,
             citation="Jenkins, H. (2006). Convergence Culture: Where Old and New Media Collide. New York: New York University Press.",
             locator="chapters on participatory culture, collective intelligence and transmedia storytelling",
             locator_type="CHAPTER",
             supports="the theory of convergence culture and participatory audiences as active producers of meaning",
             verified=True),
        dict(kind="BOOK",
             title_en="Participatory Culture in a Networked Era: A Conversation on Youth, Learning, Commerce, and Politics",
             title_fa="فرهنگ مشارکتی در عصر شبکه‌ای: گفت‌وگویی دربارهٔ جوانان، یادگیری، تجارت و سیاست",
             authors="Henry Jenkins; Mizuko Ito; danah boyd", year=2016,
             publisher="Polity Press",
             doi=None,
             url="https://www.politybooks.com/bookdetail?book_slug=participatory-culture-in-a-networked-era-a-conversation-on-youth-learning-commerce-and-politics--9780745660707",
             language="en", isbn="9780745660707",
             citation="Jenkins, H., Ito, M., & boyd, d. (2016). Participatory Culture in a Networked Era: A Conversation on Youth, Learning, Commerce, and Politics. Cambridge: Polity Press.",
             locator="chapters on participation gaps, learning ecologies and the politics of participatory culture",
             locator_type="CHAPTER",
             supports="the revisited account of participatory culture that foregrounds unequal access and political contestation",
             verified=True),
    ],
}

ENRICH = {
    "SFL-011": dict(
        mapping=dict(SFL_MAP),
        needs_enrichment=False,
        summary="به فرایندهای تقویت و تعمیق اختلافات سیاسی-گفتمانی در بستر دیجیتال می‌پردازد: نقش حباب فیلتر، اتاق پژواک، الگوریتم‌ها و شبکه‌های اجتماعی در تقویت جبهه‌گیری. این زیرحوزه به پیامدهای قطبی‌شدن برای دموکراسی می‌پردازد.",
        definition="مطالعات قطبی‌شدن دیجیتال حوزه‌ای است که شکل‌گیری و تشدید شکاف‌های سیاسی و گفتمانی را در محیط رسانه‌ای فراوان و شخصی‌شده بررسی می‌کند و می‌پرسد کدام سازوکارها — انتخاب کاربر، الگوریتم یا ساختار شبکه — بی‌طرفی و گفت‌وگوی مشترک را تضعیف می‌کنند.",
        mechanism="زنجیره با فراوانی انتخاب رسانه‌ای آغاز می‌شود: کاربر می‌تواند محتوای هم‌سو با باور خود را برگزیند و از محتوای ناهم‌سو بگریزد. سپس الگوریتم با پاداش تعامل، محتوای برانگیزاننده را بیشتر نشان می‌دهد. در گام بعد شبکهٔ روابط هم‌فکر، پیام‌های یکسان را تقویت و دیدگاه رقیب را کم‌رنگ می‌کند. سرانجام این چرخه به دوقطبی عاطفی، بی‌اعتمادی به رسانهٔ دیگر و کاهش گفت‌وگوی میان‌گروهی می‌انجامد.",
        critiques="۱. شواهد اثر حباب فیلتر ناهمگون و اغلب کوچک‌تر از ادعای رایج است. ۲. تقاضای کاربر و انتخاب او را می‌توان از عرضهٔ الگوریتمی تفکیک کرد و اغلب تفکیک نمی‌شود. ۳. بیشتر پژوهش‌ها بر آمریکا متمرکزند و تعمیم آن به نظام‌های چندرسانه‌ای دیگر اعتبار ندارد. ۴. قطبی‌شدن نگرشی با قطبی‌شدن رفتاری و انتخاباتی یکی گرفته می‌شود. ۵. سنجش مواجهه با محتوای ناهم‌سو به دادهٔ پلتفرم وابسته است که در دسترس نیست. ۶. نقش رسانه‌های حرفه‌ای و نخبگان سیاسی در کنار پلتفرم‌ها کم‌برجسته می‌شود. ۷. رسانه‌های حرفه‌ای می‌توانند با برجسته‌سازی منازعه، قطبی‌شدن را مستقل از پلتفرم تقویت کنند.",
        evolution="حوزه از پژوهش انتخاب رسانه‌ای و رأی‌دهی در دههٔ ۱۹۹۰ آغاز شد، با نظریهٔ دموکراسی پس از پخش فراگیر در ۲۰۰۷ چارچوب یافت، در دههٔ ۲۰۱۰ با اتاق پژواک و حباب فیلتر به بحث عمومی بدل شد و امروز بر سنجش مواجهه، قطبی‌شدن عاطفی و نقش رسانه‌های محلی متمرکز است؛ پژوهش تطبیقی نشان داد شدت قطبی‌شدن به ساختار نهادهای سیاسی و نظام انتخاباتی نیز وابسته است.",
        principles=["تفکیک انتخاب کاربر از عرضهٔ الگوریتمی", "سنجش مواجههٔ واقعی نه فقط نگرش", "توجه به بافت ملی و نظام رسانه‌ای", "پیوند قطبی‌شدن با اعتماد نهادی", "پرهیز از تعمیم یافته‌های یک کشور", "ارزیابی مداخله با گروه کنترل"],
        assumptions=["افزایش انتخاب رسانه‌ای، گزینش هم‌سو را آسان‌تر می‌کند.", "الگوریتم تعامل‌محور محتوای برانگیزاننده را تقویت می‌کند.", "شبکهٔ هم‌فکر بر نگرش و اعتماد اثر می‌گذارد.", "قطبی‌شدن نگرشی لزوماً به رفتار انتخاباتی یکسان نمی‌انجامد.",
            "رسانه‌های حرفه‌ای در شکل‌دهی دستور کار عمومی نقش مهمی دارند."],
        applications=["سنجش شکاف مواجهه در پلتفرم‌های خبری", "طراحی مداخله برای مواجههٔ متقابل", "پژوهش رسانهٔ محلی و پیوند اجتماعی", "ارزیابی سیاست تنوع محتوا در فید"],
        studies=[
            "پرایِر (۲۰۰۷) نشان داد افزایش انتخاب رسانه‌ای، گزینش هم‌سو را تسهیل می‌کند، نابرابری مشارکت سیاسی را بالا می‌برد و انتخابات را قطبی‌تر می‌سازد.",
            "سانستین (۲۰۱۷) اتاق پژواک و شخصی‌سازی را به‌عنوان تهدیدی برای گفت‌وگوی عمومی مشترک تحلیل کرد و بر ارزش مواجهه با دیدگاه‌های ناهم‌سو تأکید داشت.",
        ],
        detailed_analysis="قطبی‌شدن دیجیتال را نمی‌توان تنها به الگوریتم نسبت داد. بخشی از گزینش از سوی کاربر و ساختار شبکهٔ اجتماعی او می‌آید و بخشی از طراحی پلتفرم. پژوهش دقیق باید سهم هر یک را جدا کند، زیرا مداخلهٔ سیاستی برای هر کدام متفاوت است. همچنین باید میان قطب‌بندی نخبگان، قطب‌بندی توده‌ها و قطبی‌شدن عاطفی تمایز گذاشت؛ این سه همیشه با هم حرکت نمی‌کنند و سنجش یکی به‌جای دیگری تصویر نادرست می‌سازد.",
    ),
    "SFL-012": dict(
        mapping=dict(SFL_MAP),
        needs_enrichment=False,
        definition="مطالعات جنگ شناختی و ارتباطات راهبردی حوزه‌ای است که استفادهٔ هدفمند از ارتباطات، اطلاعات و روایت را برای شکل‌دهی ادراک، باور و تصمیم گروه‌های هدف بررسی می‌کند و مرز میان اقناع مشروع، تبلیغ و دستکاری را می‌سنجد.",
        mechanism="فرایند با تحلیل مخاطب هدف آغاز می‌شود: آسیب‌پذیری، شبکهٔ نفوذ و روایت‌های موجود. سپس پیام و روایت ساخته می‌شود و از کانال‌های رسمی، رسانه‌ای و شبکه‌ای توزیع می‌گردد. در گام بعد اثر بر نگرش، احساس و رفتار پایش می‌شود و پیام با بازخورد اصلاح می‌گردد. در سطح راهبردی، اقدام‌های عملیاتی و دیپلماتیک نیز به‌عنوان پیام تفسیر می‌شوند و هماهنگی میان گفتار و کردار، شرط اعتبار ارتباط راهبردی است.",
        critiques="۱. مرز ارتباطات راهبردی مشروع و دستکاری شناختی مبهم است و هر تعریفی بار هنجاری دارد. ۲. انتساب حملهٔ شناختی به بازیگر مشخص، مسئلهٔ اثبات و استناد است. ۳. ادعای اثرگذاری قوی اغلب با شواهد علّی ضعیف همراه است. ۴. تمرکز بر تهدید بیرونی می‌تواند کاستی‌های درونی و شکاف‌های اجتماعی را پنهان کند. ۵. عملیات اطلاعاتی می‌تواند به آسیب غیرنظامیان و محدودسازی آزادی بیان بینجامد. ۶. واژگان نظامی، گفت‌وگوی عمومی را به میدان نبرد تقلیل می‌دهد. ۷. ارزیابی اثربخشی کمپین راهبردی اغلب به سنجه‌های خروجی مانند تعداد بازدید بسنده می‌کند.",
        evolution="حوزه از پژوهش پروپاگاندا و جنگ روانی در قرن بیستم ریشه گرفت، در دههٔ ۲۰۰۰ با مفهوم ارتباطات راهبردی و هماهنگی سازمانی گسترش یافت و در دههٔ ۲۰۲۰ با اصطلاح جنگ شناختی و نگرانی دربارهٔ دستکاری داده‌محور به دستور کار امنیتی بدل شد؛ همچنین این مفهوم در ادبیات دفاعی به تاب‌آوری جامعه و حفاظت از تصمیم‌گیری جمعی پیوند خورد.",
        principles=["تفکیک اقناع مشروع از دستکاری", "هماهنگی گفتار و کردار سازمان", "استناد و شفافیت در انتساب تهدید", "توجه به آسیب غیرنظامیان", "حفاظت از آزادی بیان در پاسخ دفاعی", "ارزیابی علّی اثر پیش از ادعای موفقیت"],
        assumptions=["ادراک و باور هدف قابل تأثیرگذاری هدفمند است.", "اقدام سازمانی نیز به‌عنوان پیام تفسیر می‌شود.", "اثر عملیات شناختی با شواهد علّی قابل سنجش است.", "بازیگران دولتی و غیردولتی در این حوزه فعال‌اند."],
        applications=["طراحی کمپین ارتباطات بحران سازمانی", "ارزیابی تاب‌آوری شناختی جامعه", "آموزش سواد اطلاعاتی و رسانه‌ای", "تحلیل روایت در منازعهٔ بین‌المللی"],
        studies=[
            "هالاهان و همکاران (۲۰۰۷) ارتباطات راهبردی را استفادهٔ هدفمند از ارتباطات سازمانی برای تحقق مأموریت تعریف کردند و بر هم‌راستایی پیام و هدف تأکید داشتند.",
            "پال (۲۰۱۱) نشان داد ارتباطات راهبردی به پیام رسمی محدود نیست و کردار سازمان نیز معناساز است.",
            "دِپه و همکاران (۲۰۲۴) مفهوم جنگ شناختی در چارچوب ناتو را تحلیل کردند و شرایط لازم برای طبقه‌بندی یک حمله به‌عنوان حملهٔ شناختی را بررسی نمودند.",
        ],
        detailed_analysis="جنگ شناختی زمانی مفهوم تحلیلی مفیدی است که به سازوکار مشخص و شواهد قابل بررسی گره بخورد؛ در غیر این صورت به برچسبی فراگیر برای هر اختلاف اطلاعاتی بدل می‌شود. پژوهش دقیق باید میان تولید پیام، توزیع، مواجهه و تغییر رفتار تمایز بگذارد و نقش عامل انسانی و ساختار اجتماعی را در کنار عملیات بیرونی ببیند. پاسخ دفاعی مؤثر نیز بیشتر بر شفافیت، سواد رسانه‌ای و تاب‌آوری نهادی تکیه می‌کند تا بر سانسور و تقابل نظامی.",
    ),
    "SFL-013": dict(
        mapping=dict(SFL_MAP),
        needs_enrichment=False,
        definition="مطالعات امنیت اطلاعات و ارتباطات حوزه‌ای است که حفاظت از محرمانگی، یکپارچگی و دسترس‌پذیری اطلاعات را در پیوند با حریم خصوصی، اعتماد و رفتار کاربران بررسی می‌کند و می‌پرسد امنیت فنی چگونه با هنجارهای اجتماعی و سیاست‌گذاری درهم می‌آمیزد.",
        mechanism="چرخه با مدل‌سازی تهدید آغاز می‌شود: چه کسی، با چه توانی و به چه هدفی می‌تواند به داده و ارتباط دست یابد. سپس سازوکار حفاظت انتخاب می‌شود: رمزنگاری، احراز هویت، کنترل دسترسی یا جداسازی شبکه. در گام بعد سیاست سازمانی و رفتار کاربر تعیین می‌کند که این سازوکار چگونه به کار رود. سرانجام رخدادها پایش و نقض‌ها تحلیل می‌شوند و مدل تهدید بازنگری می‌گردد.",
        critiques="۱. امنیت و کاربردپذیری اغلب در تقابل قرار می‌گیرند و کاربر سازوکار پیچیده را دور می‌زند. ۲. مدل تهدید فنی می‌تواند تهدید انسانی و نهادی را نادیده بگیرد. ۳. حریم خصوصی را نمی‌توان فقط با رضایت یا کنترل داده سنجید؛ هنجار بافت مهم است. ۴. رمزنگاری قوی با درخواست دسترسی قانونی دولت‌ها تحت فشار است. ۵. سنجش امنیت به دادهٔ رخداد وابسته است که سازمان‌ها کمتر منتشر می‌کنند. ۶. پژوهش امنیت اغلب غرب‌محور است و الگوی نظارتی دیگر کشورها را پوشش نمی‌دهد. ۷. اتکا به رمزنگاری بدون احراز هویت، امنیت ارتباط را کامل نمی‌کند.",
        evolution="حوزه با رمزنگاری کلید عمومی در ۱۹۷۶ گام بنیادین برداشت، در دههٔ ۱۹۹۰ با گسترش وب به امنیت تجارت الکترونیک و ویروس‌های شبکه‌ای گسترش یافت، پس از افشاگری‌های ۲۰۱۳ به پرسش نظارت گسترده پیوند خورد و امروز بر رمزنگاری سرتاسری، حاکمیت داده و امنیت زنجیرهٔ تأمین متمرکز است؛ در همین دوره، حفاظت از زیرساخت حیاتی به موضوع اصلی سیاست‌گذاری بدل شد.",
        principles=["مدل‌سازی تهدید پیش از انتخاب سازوکار", "طراحی امن با در نظر گرفتن رفتار کاربر", "حریم خصوصی بر پایهٔ هنجار بافت", "شفافیت دربارهٔ گردآوری و نگهداری داده", "تناسب پاسخ قانونی با آسیب واقعی", "ارزیابی مستقل امنیت و انتشار رخداد",
        "آموزش و آگاهی کاربر به‌عنوان بخشی از امنیت",
        "پایش پیوسته رخدادهای امنیتی و بازنگری مدل تهدید"],
        assumptions=["محرمانگی، یکپارچگی و دسترس‌پذیری اهداف اصلی امنیت‌اند.", "رفتار کاربر بخشی از زنجیرهٔ امنیت است.", "هنجارهای بافت، مرز نقض حریم خصوصی را تعیین می‌کنند.", "تهدید امنیتی با توان و انگیزهٔ بازیگر تغییر می‌کند.",
            "امنیت مطلق ممکن نیست و مدیریت ریسک ضروری است."],
        applications=["طراحی سیاست رمزنگاری سازمان", "ارزیابی حریم خصوصی سامانهٔ پیام‌رسان", "آموزش کارکنان در برابر مهندسی اجتماعی", "تحلیل پیامد نظارتی قوانین دسترسی داده"],
        studies=[
            "دیفی و هلمن (۱۹۷۶) رمزنگاری کلید عمومی را معرفی کردند و امکان ارتباط امن بدون اشتراک پیشین کلید را فراهم ساختند.",
            "نیسنباوم (۲۰۰۹) نظریهٔ یکپارچگی بافتی را پیشنهاد کرد و نشان داد نقض حریم خصوصی، نقض هنجار جریان اطلاعات در بافت معین است.",
        ],
        detailed_analysis="امنیت اطلاعات مسئله‌ای صرفاً فنی نیست، زیرا سازوکار حفاظت همیشه در بستر نهاد، قانون و عادت کاربر عمل می‌کند. رمزنگاری قوی بدون سیاست نگهداری و آموزش کاربر، امنیت پایدار نمی‌سازد؛ سیاست سختگیرانه بدون توجه به کاربردپذیری نیز به دور زدن سازوکار می‌انجامد. پرسش ارتباطی کانونی این است که اعتماد دیجیتال چگونه ساخته می‌شود و کدام شفافیت، اعتماد را تقویت یا تضعیف می‌کند.",
    ),
    "SFL-014": dict(
        mapping=dict(SFL_MAP),
        needs_enrichment=False,
        definition="مطالعات زیست‌بوم رسانه‌ای حوزه‌ای است که مجموعهٔ وابستهٔ بسترها، بازیگران، جریان‌های اطلاعاتی و منابع مالی را به‌عنوان یک نظام بررسی می‌کند و می‌پرسد تغییر یک جزء چگونه بر کل جریان اطلاعات و قدرت اثر می‌گذارد.",
        mechanism="تحلیل با نقشهٔ بازیگران آغاز می‌شود: رسانه‌های حرفه‌ای، پلتفرم‌ها، تولیدکنندگان مستقل و واسطه‌های تبلیغاتی. سپس جریان اطلاعات میان آن‌ها و مسیر رسیدن به مخاطب ردیابی می‌شود. در گام بعد جریان توجه و پول بررسی می‌گردد، زیرا مدل درآمد تعیین می‌کند کدام محتوا پایدار می‌ماند. سرانجام حلقه‌های بازخورد — بازنشر، سنجهٔ تعامل و واکنش رقیب — و اثر آن بر تنوع و اعتماد سنجیده می‌شود.",
        critiques="۱. استعارهٔ زیست‌بوم می‌تواند روابط قدرت را طبیعی و گریزناپذیر جلوه دهد. ۲. مرز نظام مشخص نیست و تحلیل را به کل جامعه گسترش می‌دهد. ۳. بیشتر مدل‌ها بر آمریکا ساخته شده‌اند و انتقال آن‌ها به نظام‌های دیگر اعتبار ندارد. ۴. سنجش مواجههٔ مخاطب با دادهٔ پلتفرم محدود است. ۵. تمرکز بر شبکهٔ خبری، رسانهٔ سرگرمی و پیام‌رسان خصوصی را کم‌برجسته می‌کند. ۶. شفافیت پلتفرم ناکافی است و پژوهش را به استنباط وادار می‌کند. ۷. تحلیل زیست‌بوم بدون دادهٔ ترافیک واقعی، وابستگی بازیگران را بیش از حد یا کمتر از واقع برمی‌آورد.",
        evolution="حوزه از بوم‌شناسی رسانه و اقتصاد رسانه در دههٔ ۲۰۰۰ ریشه گرفت، در دههٔ ۲۰۱۰ با نظریهٔ نظام رسانه‌ای ترکیبی و تحلیل شبکه‌ای گسترش یافت و پس از ۲۰۱۸ با پژوهش پروپاگاندای شبکه‌ای به بررسی عدم تقارن جریان اطلاعات گرایش یافت؛ در دههٔ ۲۰۲۰، محدودیت دسترسی به پلتفرم‌ها آزمون طبیعی برای فرضیهٔ وابستگی زیست‌بوم فراهم کرد.",
        principles=["نقشه‌برداری کل بازیگران نه فقط رسانه‌های اصلی", "ردیابی جریان اطلاعات و پول هم‌زمان", "توجه به حلقه‌های بازخورد و سنجهٔ تعامل", "پرهیز از تعمیم مدل یک کشور", "شفافیت داده و روش در تحلیل شبکه", "پیوند تنوع محتوا با ساختار مالکیت",
        "مقایسهٔ نظام‌های ملی با توجه به تفاوت نهادها"],
        assumptions=["اجزای زیست‌بوم رسانه به یکدیگر وابسته‌اند.", "مدل درآمد بر پایداری و نوع محتوا اثر می‌گذارد.", "جریان اطلاعات از رسانه‌های حرفه‌ای به پلتفرم محدود نیست.", "تغییر یک جزء می‌تواند اثر نظام‌مند داشته باشد.",
            "جریان توجه و درآمد، پایداری بازیگران رسانه‌ای را تعیین می‌کند.",
            "بازیگران رسانه‌ای به قواعد پلتفرم وابسته‌اند."],
        applications=["تحلیل تنوع خبری در یک بازار محلی", "ارزیابی اثر قطع دسترسی به یک پلتفرم", "نقشه‌برداری جریان اطلاعات در انتخابات", "طراحی سیاست حمایت از روزنامه‌نگاری محلی"],
        studies=[
            "چدویک (۲۰۱۷) نظریهٔ نظام رسانه‌ای ترکیبی را با تأکید بر تعامل منطق رسانه‌های کهن و نوین صورت‌بندی کرد و نشان داد کنشگران سیاسی هم‌زمان از هر دو بهره می‌برند.",
            "بنکلر، فاریس و رابرتس (۲۰۱۸) با تحلیل شبکه‌ای نشان دادند زیست‌بوم رسانه‌ای آمریکا نامتقارن است و یک شاخهٔ آن نسبت به اطلاعات نادرست نفوذپذیرتر عمل می‌کند.",
        ],
        detailed_analysis="زیست‌بوم رسانه زمانی توضیحی است که مرز، بازیگران و جریان‌ها روشن تعریف شوند. بدون این دقت، استعاره به توصیف کلی «همه‌چیز به هم وصل است» فروکاسته می‌شود. پژوهش دقیق باید هم ساختار (مالکیت، پلتفرم، مقررات) و هم کنش (روزنامه‌نگار، کاربر، سیاست‌مدار) را ببیند و نشان دهد کدام حلقهٔ بازخورد تنوع را کم یا اعتماد را فرسوده می‌کند. مقایسهٔ نظام‌های ملی نیز باید تفاوت نهادهای دولتی و بازار را در نظر بگیرد.",
    ),
    "SFL-015": dict(
        mapping=dict(SFL_MAP),
        needs_enrichment=False,
        summary="به فرهنگ مشارکتی می‌پردازد: چگونه مخاطبان به تولیدکننده و مشارکت‌کنندهٔ فعال در ساخت معنای فرهنگی تبدیل شده‌اند. این زیرحوزه به الگوهای مشارکت (فاندوم، تولید مجدد، وایرال) و پیامدهای اجتماعی-فرهنگی آن‌ها می‌پردازد.",
        key_concepts=[
            {"term_fa": "فرهنگ مشارکتی", "definition": "مشارکت داوطلبانهٔ مخاطبان در تولید و توزیع فرهنگ."},
            {"term_fa": "تولیدکننده-مصرف‌کننده", "definition": "مخاطبی که هم مصرف و هم تولید می‌کند."},
            {"term_fa": "همگرایی رسانه‌ای", "definition": "هم‌افزایی تولید حرفه‌ای و کاربری در یک جریان."},
            {"term_fa": "شکاف مشارکت", "definition": "نابرابری در مهارت، دسترسی و فرصت مشارکت میان گروه‌های مخاطب."},
        ],
        theorists_text="هنری جنکینز، میزوکو ایتو و دانا بوید (فرهنگ مشارکتی)",
        definition="مطالعات فرهنگ مشارکتی حوزه‌ای است که تولید، بازترکیب و توزیع فرهنگ توسط مخاطبان را در بستر پلتفرم بررسی می‌کند و می‌پرسد مشارکت چه فرصت‌هایی برای یادگیری و بیان می‌سازد و چه نابرابری‌ها و منازعاتی را بازتولید می‌کند.",
        mechanism="چرخه با مواجههٔ مخاطب با اثر آغاز می‌شود: تماشا، خواندن یا بازی. سپس مخاطب با اقتباس، نقد، ویرایش یا بازنشر، معنای تازه می‌سازد. در گام بعد این تولید در شبکهٔ هم‌فکر دیده و اصلاح می‌شود و هنجارهای مشارکت شکل می‌گیرد. سرانجام پلتفرم با قواعد دسترسی، سنجهٔ تعامل و مالکیت، مرز مشارکت مجاز را تعیین می‌کند و بخشی از ارزش تولیدشده را جذب می‌نماید.",
        critiques="۱. روایت رهایی‌بخش مشارکت، کار بی‌دستمزد و بهره‌کشی پلتفرمی را کم‌رنگ می‌کند. ۲. شکاف مشارکت بر پایهٔ دسترسی، مهارت و سرمایهٔ فرهنگی، نابرابری را بازتولید می‌کند. ۳. مشارکت دیجیتال می‌تواند به آزار، هوچی‌گری و طرد گروه‌ها بینجامد. ۴. قواعد حق نسخه‌برداری و تعدیل محتوا، فضای کنش را نابرابر محدود می‌کند. ۵. تمرکز بر نمونه‌های خلاق، اکثریت مصرف‌کنندهٔ منفعل را نادیده می‌گیرد. ۶. سنجش مشارکت با سنجهٔ تعامل، کیفیت و معنای مشارکت را نشان نمی‌دهد. ۷. مالکیت پلتفرمی محتوای مشارکتی، مرز میان بیان کاربر و دارایی شرکت را مبهم می‌کند.",
        evolution="مفهوم در پژوهش فاندوم دههٔ ۱۹۹۰ شکل گرفت، در ۲۰۰۶ با نظریهٔ فرهنگ همگرایی به مخاطب فعال تعمیم یافت، در دههٔ ۲۰۱۰ با پلتفرم‌های اجتماعی و اقتصاد خالق گسترش یافت و در ۲۰۱۶ با بازخوانی انتقادی، بر شکاف مشارکت و سیاست فرهنگ متمرکز شد؛ در دههٔ ۲۰۲۰، هوش مصنوعی مولد پرسش نویسندگی و اصالت مشارکت را دوباره مطرح کرد.",
        principles=["توجه به شکاف دسترسی و مهارت", "تفکیک مشارکت خلاق از کار بی‌دستمزد", "پیوند فرهنگ مشارکتی با قواعد پلتفرم", "توجه به آزار و طرد در فضای مشارکت", "پرهیز از تعمیم نمونه‌های موفق", "سنجش کیفیت و معنای مشارکت نه فقط تعامل",
        "توجه به مالکیت و رضایت در بازترکیب"],
        assumptions=["مخاطب می‌تواند تولیدکنندهٔ فعال معنا باشد.", "پلتفرم با قواعد خود مرز مشارکت را تعیین می‌کند.", "مشارکت به مهارت، دسترسی و سرمایهٔ فرهنگی وابسته است.", "فرهنگ مشارکتی هم فرصت بیان و هم خطر طرد دارد.",
            "هنجارهای مشارکت در هر جامعهٔ آنلاین متفاوت است.",
            "مشارکت مخاطب تحت تأثیر طراحی رابط است."],
        applications=["طراحی فضای یادگیری مشارکتی", "تحلیل اقتصاد فاندوم و حمایت مالی", "سیاست حق نسخه‌برداری و اقتباس کاربر", "پژوهش آزار و تعدیل در جوامع آنلاین"],
        studies=[
            "جنکینز (۲۰۰۶) فرهنگ همگرایی را با مفاهیم هوش جمعی، روایت فرارسانه‌ای و مخاطب مشارکتی صورت‌بندی کرد.",
            "جنکینز، ایتو و بوید (۲۰۱۶) در بازخوانی انتقادی نشان دادند فرهنگ مشارکتی با شکاف دسترسی، تجاری‌شدن و منازعهٔ سیاسی درهم‌تنیده است.",
        ],
        detailed_analysis="فرهنگ مشارکتی را نباید با دسترسی برابر یکی گرفت. توانایی ساختن، دیده‌شدن و کسب درآمد از مشارکت به مهارت، زمان، ابزار و شبکهٔ اجتماعی وابسته است. از سوی دیگر، پلتفرم‌ها با سنجهٔ تعامل، برخی شکل‌های مشارکت را پاداش و برخی را حاشیه‌ای می‌کنند. پژوهش دقیق باید هم لحظهٔ خلاقیت مخاطب و هم شرایط ساختاری آن را ببیند و تفاوت میان مشارکت معنادار، کار بی‌دستمزد و کنش آسیب‌زا را روشن سازد.",
    ),
}

NAME_FIX = {}

YEAR_FIX = {
    "SFL-011": "no year set (subfield card); note: typo in summary corrected; documentation rebuilt from Prior (2007) and Sunstein (2017)",
    "SFL-012": "no year set (subfield card); documentation rebuilt from Hallahan et al. (2007), Paul (2011) and Deppe et al. (2024)",
    "SFL-013": "no year set (subfield card); documentation rebuilt from Diffie & Hellman (1976) and Nissenbaum (2009)",
    "SFL-014": "no year set (subfield card); documentation rebuilt from Chadwick (2017) and Benkler, Faris & Roberts (2018)",
    "SFL-015": "no year set (subfield card); note: typo in summary and Latin tokens in key concepts corrected, key concepts rewritten; documentation rebuilt from Jenkins (2006) and Jenkins, Ito & boyd (2016)",
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
                                       "verified": n_verified, "batch": 196}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH196 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
