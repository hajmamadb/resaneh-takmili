# -*- coding: utf-8 -*-
"""Batch 211: repair foundational communication models MC-304, MC-307, MC-310, MC-462, MC-463."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch211-20261117"
NOW = "2026-11-17 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch211.json"

S = {
    "MC-304": [
        dict(kind="BOOK",
             title_en="Rhetoric",
             title_fa="فن خطابه",
             authors="Aristotle; W. Rhys Roberts (trans.)", year=-350,
             publisher="MIT Classics Archive",
             doi=None,
             url="http://classics.mit.edu/Aristotle/rhetoric.html",
             language="en", isbn=None,
             citation="Aristotle. (ca. 350 BCE). Rhetoric (W. Rhys Roberts, Trans.). MIT Classics Archive.",
             locator="Book I-II",
             locator_type="BOOK",
             supports="speaker, speech and audience as the three elements of persuasion",
             verified=True),
        dict(kind="BOOK",
             title_en="The Art of Rhetoric",
             title_fa="فن خطابه",
             authors="Aristotle; J. H. Freese (trans.)", year=1926,
             publisher="Loeb Classical Library; Perseus Digital Library",
             doi=None,
             url="https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0082",
             language="en", isbn=None,
             citation="Aristotle. (1926). The Art of Rhetoric (J. H. Freese, Trans.). Loeb Classical Library. Perseus Digital Library.",
             locator="Loeb edition",
             locator_type="BOOK",
             supports="ethical, emotional and logical proof in rhetorical address",
             verified=True),
    ],
    "MC-307": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="A Conceptual Model for Communications Research",
             title_fa="مدلی مفهومی برای پژوهش ارتباطات",
             authors="Bruce H. Westley; Malcolm S. MacLean Jr.", year=1957,
             publisher="Journalism Quarterly",
             doi="10.1177/107769905703400103",
             url="https://journals.sagepub.com/doi/10.1177/107769905703400103",
             language="en", isbn=None,
             citation="Westley, B. H., & MacLean, M. S., Jr. (1957). A conceptual model for communications research. Journalism Quarterly, 34(1), 31-38. https://doi.org/10.1177/107769905703400103",
             locator="34(1), 31-38",
             locator_type="PAGE",
             supports="source-channel-receiver model including gatekeeping and feedback",
             verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Westley-MacLean Model Revisited: A Technical Note",
             title_fa="بازنگری مدل وستلی–مکلین: یادداشتی فنی",
             authors="Roger A. Guillemette", year=1986,
             publisher="Journal of Technical Writing and Communication",
             doi=None,
             url="https://eric.ed.gov/?id=ED312681",
             language="en", isbn=None,
             citation="Guillemette, R. A. (1986). The Westley-MacLean model revisited: A technical note. Journal of Technical Writing and Communication, 16(1), 41-46.",
             locator="16(1), 41-46",
             locator_type="PAGE",
             supports="clarification of model components and feedback paths",
             verified=True),
    ],
    "MC-310": [
        dict(kind="BOOK_CHAPTER",
             title_en="A Transactional Model of Communication",
             title_fa="مدل تراکنشی ارتباطات",
             authors="Dean C. Barnlund", year=1970,
             publisher="Holt, Rinehart and Winston",
             doi=None,
             url="https://www.taylorfrancis.com/chapters/edit/10.4324/9781315080918-5/transactional-model-communication-dean-barnlund",
             language="en", isbn=None,
             citation="Barnlund, D. C. (1970). A transactional model of communication. In K. K. Sereno & C. C. Mortensen (Eds.), Foundations of Communication Theory (pp. 83-92). New York: Harper & Row.",
             locator="pp. 83-92",
             locator_type="PAGE",
             supports="simultaneous and circular communication between persons with private and public cues",
             verified=True),
        dict(kind="BOOK_CHAPTER",
             title_en="A Transactional Model of Communication (reprint)",
             title_fa="مدل تراکنشی ارتباطات (بازچاپ)",
             authors="Dean C. Barnlund", year=2017,
             publisher="Routledge",
             doi="10.4324/9781315080918-5",
             url="https://www.taylorfrancis.com/chapters/edit/10.4324/9781315080918-5/transactional-model-communication-dean-barnlund",
             language="en", isbn=None,
             citation="Barnlund, D. C. (2017). A transactional model of communication. In Communication Theory (reprint). London: Routledge. https://doi.org/10.4324/9781315080918-5",
             locator="chapter 5",
             locator_type="CHAPTER",
             supports="contemporary reprint of the transactional account",
             verified=True),
    ],
    "MC-462": [
        dict(kind="BOOK_CHAPTER",
             title_en="How Communication Works",
             title_fa="ارتباط چگونه کار می‌کند",
             authors="Wilbur Schramm", year=1954,
             publisher="University of Illinois Press",
             doi=None,
             url="https://www.worldradiohistory.com/BOOKSHELF-ARH/Education/The-Process-and-Effects-of-Mass-Communications-Schramm-1971.pdf",
             language="en", isbn=None,
             citation="Schramm, W. (1954). How communication works. In W. Schramm (Ed.), The Process and Effects of Mass Communication (pp. 3-26). Urbana: University of Illinois Press.",
             locator="pp. 3-26",
             locator_type="PAGE",
             supports="circular model with encoder, interpreter, decoder and feedback",
             verified=True),
        dict(kind="BOOK_CHAPTER",
             title_en="How Communication Works (revised edition)",
             title_fa="ارتباط چگونه کار می‌کند (ویراست بازنگری‌شده)",
             authors="Wilbur Schramm", year=1971,
             publisher="University of Illinois Press",
             doi=None,
             url="https://www.worldradiohistory.com/BOOKSHELF-ARH/Education/The-Process-and-Effects-of-Mass-Communications-Schramm-1971.pdf",
             language="en", isbn=None,
             citation="Schramm, W. (1971). How communication works. In W. Schramm & D. F. Roberts (Eds.), The Process and Effects of Mass Communication (rev. ed., pp. 3-26). Urbana: University of Illinois Press.",
             locator="pp. 3-26",
             locator_type="PAGE",
             supports="revised statement including mass communication loop",
             verified=True),
    ],
    "MC-463": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="An Approach to the Study of Communicative Acts",
             title_fa="رویکردی به مطالعهٔ کنش‌های ارتباطی",
             authors="Theodore M. Newcomb", year=1953,
             publisher="Psychological Review",
             doi="10.1037/h0063098",
             url="https://psycnet.apa.org/record/1954-05963-001",
             language="en", isbn=None,
             citation="Newcomb, T. M. (1953). An approach to the study of communicative acts. Psychological Review, 60(6), 393-404. https://doi.org/10.1037/h0063098",
             locator="60(6), 393-404",
             locator_type="PAGE",
             supports="A-B-X coorientation and equilibrium through communication",
             verified=True),
        dict(kind="BOOK_CHAPTER",
             title_en="Coorientation Theory",
             title_fa="نظریهٔ هم‌جهت‌گیری",
             authors="SAGE Publications", year=2009,
             publisher="SAGE",
             doi=None,
             url=None,
             language="en", isbn=None,
             citation="SAGE Publications. (2009). Coorientation theory. In Encyclopedia of Communication Theory. Thousand Oaks: SAGE.",
             locator="entry",
             locator_type="CHAPTER",
             supports="later codification of Newcomb's coorientation approach",
             verified=True),
    ],
}

ENRICH = {
    "MC-304": dict(
        needs_enrichment=False,
        level="پایه",
        related_approaches="بلاغت کلاسیک؛ نظریهٔ استدلال؛ اقناع؛ تحلیل گفتمان؛ بلاغت دیجیتال.",
        recommended_sources="«فن خطابه» (ارسطو، حدود ۳۵۰ پیش از میلاد)؛ ترجمهٔ فریز در کتابخانهٔ لوب (۱۹۲۶)؛ بلاغت انگیزه‌ها (کنت برک، ۱۹۵۰).",
        detailed_analysis=("۱. بنیان و منطق نظری\nارسطو در «فن خطابه» (حدود سدهٔ چهارم پیش از میلاد) خطابه را به سه رکن گوینده، گفتار و شنونده تقسیم کرد و اقناع را بر سه نوع شاهد استوار دانست: "
                           "اخلاق گوینده (اعتبار و منش)، احساس شنونده (حالت عاطفی) و استدلال خطابی (برهان ظنی). "
                           "این صورت‌بندی، نخستین چارچوب نظام‌مند برای تحلیل ارتباط اقناعی است و به همین دلیل آن را مدل خطی ارسطویی می‌نامند.\n\n"
                           "۲. ساختارهای مفهومی\nسه رکن گوینده، گفتار و شنونده، سه شاهد اقناعی و مفهوم برهان خطابی سازه‌های اصلی‌اند. "
                           "مدل، ارتباط را یک‌سویه و در خدمت تأثیر بر شنونده می‌بیند.\n\n"
                           "۳. نمونه‌های تحلیلی\nدر یک سخنرانی سیاسی، اعتبار گوینده، ساختار استدلال و انگیزش عاطفی مخاطب سه اهرم اقناع‌اند؛ در تبلیغ تجاری نیز همین سه اهرم در قالب چهرهٔ معتبر، ادعای منطقی و تصویر احساسی بازتولید می‌شود.\n\n"
                           "۴. نقدها و چالش‌ها\nمدل خطی و یک‌سویه است و بازخورد و مذاکرهٔ معنا را نادیده می‌گیرد؛ اقناع را بر فهم و گفت‌وگوی برابر مقدم می‌دارد؛ به بافت نهادی و رسانه‌ای توجه ندارد؛ و مفاهیم آن برای رسانه‌های تعاملی و چندرسانه‌ای امروز نیازمند بسط است.\n\n"
                           "۵. سیر تاریخی\nفن خطابه در یونان باستان پدید آمد، بلاغت رومی آن را بسط داد و در سدهٔ بیستم با بازگشت به بلاغت، بنیان تحلیل گفتمان و مطالعات اقناع شد.\n\n"
                           "۶. جایگاه در بحث روز\nدر بلاغت دیجیتال و تحلیل تبلیغات آنلاین، سه‌گانهٔ ارسطویی هنوز چارچوبی کارآمد برای تحلیل اعتبار، استدلال و احساس در محتوای شبکه‌های اجتماعی است."),
    ),
    "MC-307": dict(
        needs_enrichment=False,
        level="پایه",
        related_approaches="دروازه‌بانی خبر؛ مدل نیوکامب؛ مدل حلقه‌ای شرام؛ نظریهٔ برجسته‌سازی؛ اقتصاد رسانه.",
        recommended_sources="«مدلی مفهومی برای پژوهش ارتباطات» (وستلی و مکلین، ۱۹۵۷)؛ «بازنگری مدل وستلی–مکلین» (گیلمت، ۱۹۸۶)؛ «بازنگری مدل وستلی–مکلین» (لیسی، ۱۹۸۹).",
        detailed_analysis=("۱. بنیان و منطق نظری\nوستلی و مکلین (۱۹۵۷) در فصلنامهٔ روزنامه‌نگاری مدلی برای پژوهش ارتباطات عرضه کردند که بر پایهٔ مثلث منبع-موضوع-گیرندهٔ نیوکامب بنا شده بود، "
                           "اما عنصر کانال را به‌صورت جدی وارد کرد. در این مدل، منبع پیام‌هایی دربارهٔ موضوع‌های محیط به کانال می‌فرستد و کانال، نقش دروازه‌بان را ایفا می‌کند و گزیده‌ای از آن‌ها را به گیرنده می‌رساند. "
                           "بازخورد از گیرنده به کانال و منبع بازمی‌گردد و مدل را از خطی‌بودن صرف دور می‌کند.\n\n"
                           "۲. ساختارهای مفهومی\nمنبع، کانال، گیرنده، موضوع‌های جهت‌گیری، دروازه‌بانی و بازخورد سازه‌های اصلی‌اند. "
                           "نوآوری مدل، جای دادن حرفه‌مند رسانه‌ای به‌عنوان عاملی گزینش‌گر میان منبع و مخاطب است.\n\n"
                           "۳. نمونه‌های تحلیلی\nدر یک خبرگزاری، خبرنگار و ویراستار (کانال) از میان رویدادهای بی‌شمار (موضوع‌ها) گزینش می‌کنند و نسخهٔ نهایی را به مخاطب می‌رسانند؛ بازخورد مخاطب بر گزینش‌های بعدی اثر می‌گذارد.\n\n"
                           "۴. نقدها و چالش‌ها\nمدل هنوز نسبتاً خطی است و ساختار قدرت و مالکیت را درون کانال توضیح نمی‌دهد؛ محیط اجتماعی و رقابت رسانه‌ای را ساده می‌کند؛ به بازخورد غیرمستقیم و تأخیری کمتر می‌پردازد؛ و برای محیط پلتفرمی که هر کاربر هم منبع و هم کانال است، نیازمند بازنگری است.\n\n"
                           "۵. سیر تاریخی\nمقالهٔ ۱۹۵۷ مدل را در ادبیات پژوهش ارتباطات تثبیت کرد، گیلمت (۱۹۸۶) اجزای آن را روشن‌تر کرد و لیسی (۱۹۸۹) آن را برای حوزه‌های نوپدید بسط داد.\n\n"
                           "۶. جایگاه در بحث روز\nدر پلتفرم‌ها، الگوریتم مرتب‌سازی نقش دروازه‌بان را بر عهده گرفته است؛ مدل وستلی–مکلین هنوز چارچوبی مفید برای پرسش از «چه کسی گزینش می‌کند» فراهم می‌کند."),
    ),
    "MC-310": dict(
        needs_enrichment=False,
        level="پایه",
        related_approaches="مدل حلقه‌ای شرام؛ نظریهٔ هم‌جهت‌گیری؛ تعامل نمادین؛ ارتباط میان‌فردی؛ پدیدارشناسی ارتباط.",
        recommended_sources="«مدل تراکنشی ارتباطات» (بارنلوند، ۱۹۷۰)؛ بازچاپ ۲۰۱۷؛ «نظریه‌های ارتباطات انسانی» (لیتل‌جان و فاس).",
        detailed_analysis=("۱. بنیان و منطق نظری\nبارنلوند (۱۹۷۰) مدل تراکنشی را در واکنش به مدل‌های خطی و تعاملی عرضه کرد. "
                           "او استدلال کرد ارتباط امری هم‌زمان است: هر دو طرف در یک لحظه رمزگذار، مفسر و رمزگشا هستند و معنای مشترک در جریان تراکنش ساخته می‌شود، نه اینکه از فرستنده به گیرنده منتقل شود. "
                           "بارنلوند نشانه‌ها را به خصوصی (درونی) و عمومی (رفتاری) تقسیم کرد و میدان تجربهٔ هر طرف را تعیین‌کنندهٔ تفسیر دانست.\n\n"
                           "۲. ساختارهای مفهومی\nتراکنش هم‌زمان، میدان تجربه، نشانه‌های خصوصی و عمومی، و رمزگذاری-رمزگشایی متقابل سازه‌های اصلی‌اند.\n\n"
                           "۳. نمونه‌های تحلیلی\nدر یک گفت‌وگوی مشاوره، مشاور و مراجع هم‌زمان پیام می‌فرستند، تفسیر می‌کنند و به واکنش دیگری پاسخ می‌دهند؛ معنای جلسه در همین تراکنش متقابل ساخته می‌شود و نه در قصد اولیهٔ یکی از دو طرف.\n\n"
                           "۴. نقدها و چالش‌ها\nسنجش تجربی تراکنش هم‌زمان دشوار است؛ فرض هم‌زمانی کامل در رسانه‌های ناهمزمان برقرار نیست؛ مرز میان نشانهٔ خصوصی و عمومی مبهم است؛ و کاربرد آن در ارتباط جمعی یک‌به‌چند محدود می‌ماند.\n\n"
                           "۵. سیر تاریخی\nمقالهٔ ۱۹۷۰ به یکی از مدل‌های استاندارد کتاب‌های مبانی ارتباطات تبدیل شد، بارها بازچاپ شد و در دههٔ اخیر برای ارتباط دیجیتال هم‌زمان بازخوانی شده است.\n\n"
                           "۶. جایگاه در بحث روز\nدر ویدئوکنفرانس، پیام‌رسان هم‌زمان و محیط‌های مجازی، تراکنش هم‌زمان بار دیگر محور تحلیل ارتباط شده است و مدل بارنلوند چارچوبی برای فهم آن فراهم می‌کند."),
    ),
    "MC-462": dict(
        needs_enrichment=False,
        level="پایه",
        related_approaches="مدل شانون و ویور؛ مدل تراکنشی بارنلوند؛ ارتباط جمعی؛ بازخورد؛ سواد رسانه‌ای.",
        recommended_sources="«ارتباط چگونه کار می‌کند» (شرام، ۱۹۵۴)؛ ویراست بازنگری‌شده (شرام و رابرتس، ۱۹۷۱)؛ «نظریه‌های ارتباطات جمعی» (مک‌کوئیل).",
        detailed_analysis=("۱. بنیان و منطق نظری\nشرام (۱۹۵۴) در فصل «ارتباط چگونه کار می‌کند» مدل حلقه‌ای را با تکیه بر الگوی چارلز آزگود معرفی کرد. "
                           "برخلاف مدل خطی شانون و ویور، در این مدل هر طرف هم‌زمان رمزگذار، مفسر و رمزگشاست و پیام در حلقه‌ای از بازخورد میان آن‌ها می‌گردد. "
                           "شرام نسخهٔ ارتباط جمعی مدل را نیز عرضه کرد که در آن سازمان رسانه‌ای میان منبع و مخاطب قرار می‌گیرد و بازخورد تأخیری و غیرمستقیم است.\n\n"
                           "۲. ساختارهای مفهومی\nرمزگذار، مفسر، رمزگشا، بازخورد و میدان تجربهٔ مشترک سازه‌های اصلی‌اند. "
                           "حلقه، جانشین خط مستقیم انتقال می‌شود.\n\n"
                           "۳. نمونه‌های تحلیلی\nدر گفت‌وگوی تلفنی، هر دو طرف هم‌زمان می‌فرستند و می‌گیرند و معنا را اصلاح می‌کنند؛ در ارتباط جمعی، سازمان رسانه‌ای پیام را رمزگذاری می‌کند و بازخورد مخاطب با تأخیر به آن بازمی‌گردد.\n\n"
                           "۴. نقدها و چالش‌ها\nحلقه، توازن قدرت میان طرف‌ها را نشان نمی‌دهد؛ بازخورد در رسانه‌های جمعی ناقص و کند است؛ مدل بیشتر توصیفی است تا تبیینی؛ و برای محیط‌های چندکاناله و شبکه‌ای امروز ساده‌سازی‌شده به نظر می‌رسد.\n\n"
                           "۵. سیر تاریخی\nفصل ۱۹۵۴ به یکی از پراستنادترین متون مبانی ارتباطات تبدیل شد و ویراست ۱۹۷۱ آن را با ادبیات ارتباط جمعی روزآمد کرد.\n\n"
                           "۶. جایگاه در بحث روز\nدر شبکه‌های اجتماعی، حلقهٔ شرام به حلقه‌های چندلایه و هم‌زمان تبدیل شده است؛ بازخورد آنی و عمومی، مدل را همچنان برای تحلیل تعامل رسانه‌ای زنده نگه داشته است."),
    ),
    "MC-463": dict(
        needs_enrichment=False,
        level="پایه",
        related_approaches="نظریهٔ تعادل هایدر؛ هم‌جهت‌گیری؛ روان‌شناسی اجتماعی؛ ارتباط میان‌فردی؛ نظریهٔ شبکه‌های معنایی.",
        recommended_sources="«رویکردی به مطالعهٔ کنش‌های ارتباطی» (نیوکامب، ۱۹۵۳)؛ «نظریهٔ هم‌جهت‌گیری» در دانشنامهٔ نظریهٔ ارتباطات (۲۰۰۹)؛ پژوهش‌های هم‌جهت‌گیری و ادراک متقابل.",
        detailed_analysis=("۱. بنیان و منطق نظری\nنیوکامب (۱۹۵۳) ارتباط را کنشی برای حفظ تعادل میان دو شخص و یک موضوع مشترک دانست. "
                           "او با تکیه بر نظریهٔ تعادل هایدر استدلال کرد انسان‌ها می‌کوشند نگرش خود به دیگری و به موضوع را هم‌سو نگه دارند؛ "
                           "وقتی ناهم‌ترازی میان نگرش دو طرف به یکدیگر و به موضوع پدید می‌آید، ارتباط ابزار بازگرداندن تعادل است. این چارچوب بعدها به نظریهٔ هم‌جهت‌گیری گسترش یافت.\n\n"
                           "۲. ساختارهای مفهومی\nشخص نخست، شخص دوم، موضوع، جهت‌گیری، هم‌جهت‌گیری و تعادل سازه‌های اصلی‌اند. "
                           "تعادل زمانی برقرار است که نگرش دو طرف به یکدیگر و به موضوع سازگار باشد.\n\n"
                           "۳. نمونه‌های تحلیلی\nدو همکار که به یک سیاست عمومی نگرش یکسانی دارند، ارتباطی کم‌تنش دارند؛ اما وقتی یکی نگرش خود را تغییر می‌دهد، گفت‌وگو برای بازگرداندن هم‌سویی یا بازتعریف رابطه فعال می‌شود.\n\n"
                           "۴. نقدها و چالش‌ها\nتعادل همیشه مطلوب نیست و می‌تواند به هم‌رنگی و سرکوب اختلاف بینجامد؛ مدل بر دو نفر متمرکز است و گروه و رسانه را کمتر پوشش می‌دهد؛ سنجش عاطفه و ادراک متقابل دشوار است؛ و فرض عقلانی‌بودن کنشگر محل نقد است.\n\n"
                           "۵. سیر تاریخی\nمقالهٔ ۱۹۵۳ بنیان نظریهٔ هم‌جهت‌گیری شد؛ مک‌لاود و چفی آن را به پژوهش ادراک متقابل و ارتباط جمعی گسترش دادند و امروز در تحلیل قطبی‌سازی به‌کار می‌رود.\n\n"
                           "۶. جایگاه در بحث روز\nدر محیط شبکه‌های اجتماعی، تعادل نیوکامب توضیح می‌دهد چرا افراد هم‌نگر را تقویت می‌کنند و از اختلاف پرهیز می‌کنند؛ همین سازوکار یکی از ریشه‌های اتاق پژواک است."),
    ),
}

NAME_FIX = {}

YEAR_FIX = {
    "MC-304": "year=-350 (Aristotle Rhetoric); replaced generic sender-message template analysis and unrelated recommendations",
    "MC-307": "year=1957 (Westley & MacLean 1957); Guillemette 1986 verified; replaced generic template analysis",
    "MC-310": "year=1970 (Barnlund 1970); page range 83-92 verified; replaced generic template analysis",
    "MC-462": "year=1954 (Schramm 1954); replaced generic template analysis and unrelated recommendations",
    "MC-463": "year=1953 (Newcomb 1953); DOI verified; replaced generic template analysis and unrelated recommendations",
}
