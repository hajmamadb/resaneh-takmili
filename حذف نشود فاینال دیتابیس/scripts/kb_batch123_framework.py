# -*- coding: utf-8 -*-
"""Batch 123 (FRAMEWORK): full documentation for MC-572, MC-582, MC-598, MC-600."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch123-framework-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch123_framework.json"

S = {
    "MC-572": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Transtheoretical Therapy: Toward a More Integrative Model of Change",
             title_fa="درمان فرانظری: به‌سوی مدلی یکپارچه‌تر برای تغییر",
             authors="Prochaska, J. O.; DiClemente, C. C.", year=1982,
             publisher="Psychotherapy: Theory, Research and Practice",
             doi=None,
             url="https://psycnet.apa.org/record/1984-26566-001",
             language="en", isbn=None,
             citation="Prochaska, J. O., & DiClemente, C. C. (1982). Transtheoretical therapy: Toward a more integrative model of change. Psychotherapy: Theory, Research and Practice, 19(3), 276-288.",
             locator="19(3):276-288", locator_type="page_range",
             supports="stages of change as a transtheoretical integrative model of behavior change", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="In Search of How People Change: Applications to Addictive Behaviors",
             title_fa="در جست‌وجوی چگونگی تغییر مردم: کاربردها در رفتارهای اعتیادی",
             authors="Prochaska, J. O.; DiClemente, C. C.; Norcross, J. C.", year=1992,
             publisher="American Psychologist",
             doi=None, url=None, language="en", isbn=None,
             citation="Prochaska, J. O., DiClemente, C. C., & Norcross, J. C. (1992). In search of how people change: Applications to addictive behaviors. American Psychologist, 47(9), 1102-1114.",
             locator="47(9):1102-1114", locator_type="page_range",
             supports="consolidated statement of stages, processes and levels of change", verified=False),
    ],
    "MC-582": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="The TARES Test: Five Principles for Ethical Persuasion",
             title_fa="آزمون تارس: پنج اصل برای اقناع اخلاقی",
             authors="Baker, S.; Martinson, D. L.", year=2001,
             publisher="Journal of Mass Media Ethics",
             doi="10.1080/08900523.2001.9679610",
             url="https://www.tandfonline.com/doi/abs/10.1080/08900523.2001.9679610",
             language="en", isbn=None,
             citation="Baker, S., & Martinson, D. L. (2001). The TARES test: Five principles for ethical persuasion. Journal of Mass Media Ethics, 16(2-3), 148-175.",
             locator="16(2-3):148-175", locator_type="page_range",
             supports="truthfulness, authenticity, respect, equity and social responsibility as tests of ethical persuasion", verified=True),
        dict(kind="BOOK",
             title_en="Ethics in Human Communication",
             title_fa="اخلاق در ارتباطات انسانی",
             authors="Johannesen, R. L.", year=2002,
             publisher="Waveland Press",
             doi=None, url=None, language="en", isbn=None,
             citation="Johannesen, R. L. (2002). Ethics in human communication (5th ed.). Waveland Press.",
             locator="chs. 1-3", locator_type="work",
             supports="ethical perspectives on persuasion, truth and human dignity", verified=False),
    ],
    "MC-598": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="A Rhetorical Approach to Zones of Meaning and Organizational Prerogatives",
             title_fa="رویکردی بلاغی به پهنه‌های معنا و اختیارات سازمانی",
             authors="Heath, R. L.", year=1993,
             publisher="Public Relations Review",
             doi=None,
             url="https://www.sciencedirect.com/science/article/pii/036381119390004V",
             language="en", isbn=None,
             citation="Heath, R. L. (1993). A rhetorical approach to zones of meaning and organizational prerogatives. Public Relations Review, 19(2), 141-155.",
             locator="19(2):141-155", locator_type="page_range",
             supports="public relations as rhetorical participation in the management of meaning", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Toward a Rhetoric of Public Relations",
             title_fa="به‌سوی بلاغتی برای روابط عمومی",
             authors="Ihlen, O.", year=2011,
             publisher="Management Communication Quarterly",
             doi=None, url=None, language="en", isbn=None,
             citation="Ihlen, O. (2011). Toward a rhetoric of public relations. Management Communication Quarterly, 25(3), 454-472.",
             locator="25(3):454-472", locator_type="page_range",
             supports="rhetorical grounding of public relations as agonistic meaning-making", verified=False),
    ],
    "MC-600": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Metcalfe's Law after 40 Years of Ethernet",
             title_fa="قانون متکالف پس از چهل سال اترنت",
             authors="Metcalfe, R. M.", year=2013,
             publisher="Computer",
             doi="10.1109/MC.2013.374",
             url="https://dl.acm.org/doi/10.5555/2635508.2635526",
             language="en", isbn=None,
             citation="Metcalfe, R. M. (2013). Metcalfe's law after 40 years of Ethernet. Computer, 46(12), 26-31.",
             locator="46(12):26-31", locator_type="page_range",
             supports="network value proportional to the square of connected users, with empirical qualifications", verified=True),
        dict(kind="BOOK",
             title_en="Information Rules: A Strategic Guide to the Network Economy",
             title_fa="قواعد اطلاعات: راهنمای راهبردی برای اقتصاد شبکه",
             authors="Shapiro, C.; Varian, H. R.", year=1999,
             publisher="Harvard Business School Press",
             doi=None, url=None, language="en", isbn=None,
             citation="Shapiro, C., & Varian, H. R. (1999). Information rules: A strategic guide to the network economy. Harvard Business School Press.",
             locator="ch. 7", locator_type="work",
             supports="network effects and positive feedback in information markets", verified=False),
    ],
}

ENRICH = {
    "MC-572": dict(
        summary="چارچوب مراحل تغییر رفتار، مدلی است که تغییر رفتار را نه رویدادی یک‌باره، بلکه مسیری مرحله‌ای می‌داند و برای هر مرحله، مداخلهٔ متناسب پیشنهاد می‌کند. جیمز پروچاسکا و کارلو دی‌کلمنته در مقالهٔ سال ۱۹۸۲ این مدل را با مقایسهٔ بیش از صد نظریهٔ روان‌درمانی ساختند و آن را «فرانظری» نامیدند. آن‌ها پنج مرحله را تشخیص دادند: پیش‌تفکر، یعنی نبود قصد تغییر در آیندهٔ نزدیک؛ تفکر، یعنی آگاهی از مشکل و سنجش فواید و هزینه‌ها؛ آماده‌سازی، یعنی قصد جدی تغییر در آیندهٔ نزدیک؛ عمل، یعنی تغییر رفتار در بازهٔ کوتاه؛ و حفظ، یعنی تثبیت تغییر و پیشگیری از بازگشت. مدل با سه سازوکار دیگر تکمیل می‌شود: فرایندهای تغییر، یعنی راهبردهای شناختی و رفتاری که در هر مرحله متفاوت‌اند؛ تعادل تصمیم، یعنی سنجش سود و زیان تغییر؛ و خودکارآمدی، یعنی باور به توان انجام تغییر. کاربرد رسانه‌ای آن در طراحی پیام‌های سلامت و کمپین‌های هم‌خوان با مرحلهٔ مخاطب است: پیام آگاهی‌بخش برای پیش‌تفکر و پیام مهارت‌آموزی برای مرحلهٔ عمل اثر متفاوتی دارند. نقد اصلی به این چارچوب، مرزهای دلبخواهی مراحل، فرض حرکت خطی، دشواری سنجش و شواهد ناهمگون دربارهٔ کارایی آن در مداخلات است؛ با این حال، این مدل در سیاست‌گذاری سلامت به‌عنوان چارچوب تقسیم مخاطب و زمان‌بندی پیام به کار می‌رود.",
        definition="چارچوب مراحل تغییر، مدلی است که افراد را بر پایهٔ آمادگی برای تغییر رفتار در پنج مرحلهٔ پیش‌تفکر، تفکر، آماده‌سازی، عمل و حفظ جای می‌دهد و مداخلهٔ متناسب با هر مرحله را پیشنهاد می‌کند.",
        main_problem="چگونه می‌توان مداخله‌ای طراحی کرد که با سطح آمادگی واقعی مخاطب هم‌خوان باشد، بی‌آنکه فرض شود همهٔ افراد در یک نقطه از مسیر تغییر قرار دارند.",
        mechanism="فرد از بی‌توجهی به مشکل به سنجش سود و زیان و سپس آماده‌سازی و عمل می‌رسد؛ فرایندهای شناختی و رفتاری در هر مرحله تغییر می‌کنند و تعادل تصمیم و خودکارآمدی، سرعت عبور از مراحل را تعیین می‌کنند.",
        assumptions=[
            "تغییر رفتار فرایندی مرحله‌ای است، نه رویدادی یک‌باره.",
            "مداخلهٔ هم‌خوان با مرحله، اثر بیشتری دارد.",
            "بازگشت بخشی از فرایند تغییر است، نه شکست مطلق.",
            "سود و زیان ادراک‌شده، گذار میان مراحل را توضیح می‌دهد.",
        ],
        principles=[
            "هر مرحله، فرایند تغییر و پیام مناسب خود را می‌طلبد.",
            "پیش از عمل، باید تعادل تصمیم به سمت سود تغییر جابه‌جا شود.",
            "خودکارآمدی، پیش‌بین مهمی برای حفظ تغییر است.",
            "بازگشت باید فرصت بازآموزی تلقی شود، نه پایان مداخله.",
        ],
        critiques=[
            "مرز میان مراحل دلبخواهی و سنجش آن دشوار است.",
            "حرکت خطی و یک‌جهته، تجربهٔ واقعی تغییر را ساده می‌کند.",
            "شواهد کارایی مداخلات مرحله‌محور ناهمگون است.",
            "عوامل ساختاری و محیطی در مدل کم‌رنگ می‌شوند.",
        ],
        applications=[
            "طراحی کمپین سلامت هم‌خوان با مرحلهٔ آمادگی مخاطب.",
            "برنامه‌های ترک اعتیاد و تغییر رفتار تغذیه‌ای.",
            "پیام‌های رسانه‌ای برای افزایش مشارکت مدنی.",
            "آموزش کارکنان و مدیریت تغییر سازمانی.",
        ],
        evolution="پروچاسکا و دی‌کلمنته (۱۹۸۲) مدل را با مقایسهٔ نظریه‌های درمانی عرضه کردند؛ نسخهٔ ۱۹۹۲ آن را برای رفتارهای اعتیادی بسط داد و پژوهش‌های سلامت عمومی آن را به ابزار طراحی مداخلهٔ مرحله‌محور تبدیل کردند.",
        key_concepts=[
            "پیش‌تفکر (Precontemplation)",
            "تفکر (Contemplation)",
            "آماده‌سازی (Preparation)",
            "عمل و حفظ (Action and Maintenance)",
            "تعادل تصمیم (Decisional Balance)",
        ],
        theorists="جیمز پروچاسکا؛ کارلو دی‌کلمنته؛ جان نورکراس",
        theorists_text="پروچاسکا و دی‌کلمنته (۱۹۸۲)؛ پروچاسکا، دی‌کلمنته و نورکراس (۱۹۹۲)",
        model="پیش‌تفکر → تفکر → آماده‌سازی → عمل → حفظ، با عبور مشروط بر تعادل تصمیم و خودکارآمدی.",
        studies=[
            "پروچاسکا و دی‌کلمنته (۱۹۸۲) مدل فرانظری و مراحل تغییر را معرفی کردند.",
            "پروچاسکا، دی‌کلمنته و نورکراس (۱۹۹۲) کاربرد مدل را در رفتارهای اعتیادی مستند کردند.",
        ],
        detailed_analysis="تحلیل عمیق نشان می‌دهد ارزش مدل در هم‌خوانی پیام با آمادگی مخاطب است: پیامی که بر عمل فوری تأکید می‌کند، برای فرد پیش‌تفکر مقاومت می‌سازد. در کمپین سلامت، تقسیم مخاطب بر پایهٔ مرحله و ارائهٔ پیام متناسب، اثربخشی را افزایش می‌دهد. اما مدل باید با شناخت بافت اجتماعی و دسترسی به خدمات همراه شود، زیرا تغییر رفتار تنها محصول تصمیم فردی نیست.",
        critique_text="نقد اصلی آن است که مرز مراحل دلبخواهی و سنجش آن دشوار است، فرض حرکت خطی تجربهٔ واقعی را ساده می‌کند و شواهد کارایی مداخلات مرحله‌محور ناهمگون است.",
        example_text="در کمپینی برای کاهش مصرف نمک، پیام «خطر فشار خون را بشناسید» برای فرد پیش‌تفکر مناسب است، در حالی که برای فرد در مرحلهٔ آماده‌سازی، دستور پخت کم‌نمک و راهنمای خرید اثر بیشتری دارد.",
        year=1982,
    ),
    "MC-582": dict(
        summary="چارچوب اخلاق اقناع، معیارهایی برای داوری دربارهٔ درستی و نادرستی پیام‌های ترغیبی عرضه می‌کند. شری بیکر و دیوید مارتینسون در مقالهٔ سال ۲۰۰۱ خود آزمون تارس را پیشنهاد کردند که پنج اصل را در بر می‌گیرد: راست‌گویی پیام، یعنی هم‌خوانی ادعا با واقعیت؛ اصالت اقناع‌گر، یعنی باور واقعی او به پیام؛ احترام به مخاطب، یعنی به‌رسمیت شناختن حق انتخاب و کرامت او؛ انصاف، یعنی توزیع عادلانهٔ سود و زیان میان فرستنده و گیرنده؛ و مسئولیت اجتماعی، یعنی سنجش پیامد پیام برای جامعه. این پنج اصل به‌صورت فهرست بازبینی به کار می‌روند: هر کمپین پیش از انتشار با آن‌ها سنجیده می‌شود. چارچوب بر این فرض استوار است که اقناع به‌خودی‌خود غیراخلاقی نیست، بلکه اخلاقی بودن آن به روش، قصد و پیامد بستگی دارد. تفاوت اقناع با دستکاری در همین جاست: دستکاری اطلاعات ناقص یا انگیزهٔ پنهان را برای تغییر رفتار به کار می‌گیرد، در حالی که اقناع اخلاقی مخاطب را شریک تصمیم می‌داند. کاربرد آن در تبلیغات، روابط عمومی، ارتباطات سلامت و کمپین‌های سیاسی گسترده است و در آموزش اخلاق رسانه به‌عنوان ابزار سنجش به کار می‌رود. نقد اصلی به این چارچوب، دشواری سنجش اصالت و انصاف، وابستگی داوری به زمینهٔ فرهنگی و خطر تبدیل آن به فهرست تشریفاتی است. یادآوری: انتساب کارت تحریریهٔ این مدخل با منابع معتبر هم‌خوان نبود و مستندسازی حاضر بر پایهٔ منابع تأییدشده بازنویسی شده است.",
        definition="چارچوب اخلاق اقناع، مجموعه‌ای از معیارها برای سنجش اخلاقی پیام ترغیبی است که درستی، اصالت، احترام، انصاف و مسئولیت اجتماعی را در کنار هم می‌سنجد.",
        main_problem="چگونه می‌توان مرز میان اقناع مشروع و دستکاری را تشخیص داد و پیش از انتشار پیام، اخلاقی بودن آن را با معیارهای روشن سنجید.",
        mechanism="پیام با پنج پرسش سنجیده می‌شود: آیا ادعا راست است؛ آیا فرستنده خود به آن باور دارد؛ آیا حق انتخاب مخاطب محترم است؛ آیا سود و زیان عادلانه تقسیم شده؛ و آیا پیامد اجتماعی آن پذیرفتنی است. پاسخ منفی به هر پرسش، بازنگری پیام را الزامی می‌کند.",
        assumptions=[
            "اقناع به‌خودی‌خود غیراخلاقی نیست.",
            "اخلاقی بودن پیام را می‌توان با معیارهای قابل بحث سنجید.",
            "مخاطب حق انتخاب آگاهانه دارد.",
            "پیامد اجتماعی پیام، بخشی از مسئولیت فرستنده است.",
        ],
        principles=[
            "راست‌گویی، شرط نخست اعتبار پیام است.",
            "اصالت فرستنده، پیام را از ریاکاری جدا می‌کند.",
            "احترام به مخاطب، اقناع را از دستکاری متمایز می‌سازد.",
            "انصاف و مسئولیت اجتماعی، سود کوتاه‌مدت را محدود می‌کنند.",
        ],
        critiques=[
            "سنجش اصالت و انصاف به‌سختی عملیاتی می‌شود.",
            "داوری اخلاقی به زمینهٔ فرهنگی و ارزش‌های جامعه وابسته است.",
            "خطر تبدیل چارچوب به فهرست تشریفاتی وجود دارد.",
            "تعارض میان سود سازمانی و مسئولیت اجتماعی کمتر حل شده است.",
        ],
        applications=[
            "بازبینی اخلاقی کمپین‌های تبلیغاتی و روابط عمومی.",
            "طراحی پیام سلامت و پیشگیری از دستکاری مصرف‌کننده.",
            "آموزش اخلاق رسانه به دانشجویان روزنامه‌نگاری و تبلیغات.",
            "ارزیابی اخلاقی تبلیغات سیاسی و کمپین‌های انتخاباتی.",
        ],
        evolution="سنت اخلاق ارتباطات از دههٔ ۱۹۷۰ با مباحث صداقت و کرامت مخاطب شکل گرفت؛ بیکر و مارتینسون (۲۰۰۱) پنج اصل را در آزمون تارس عملیاتی کردند و پژوهش‌های بعدی آن را به تبلیغات دیجیتال و الگوریتم‌های اقناع گستردند.",
        key_concepts=[
            "راست‌گویی (Truthfulness)",
            "اصالت (Authenticity)",
            "احترام (Respect)",
            "انصاف (Equity)",
            "مسئولیت اجتماعی (Social Responsibility)",
        ],
        theorists="شری بیکر؛ دیوید مارتینسون؛ ریچارد یوهانسن",
        theorists_text="بیکر و مارتینسون (۲۰۰۱)؛ یوهانسن (۲۰۰۲)",
        model="پیام اقناعی → آزمون پنج اصل → شناسایی نقض → بازنگری یا انتشار مسئولانه.",
        studies=[
            "بیکر و مارتینسون (۲۰۰۱) آزمون تارس را با پنج اصل و فهرست بازبینی عرضه کردند.",
            "یوهانسن (۲۰۰۲) دیدگاه‌های اخلاقی در ارتباطات انسانی را نظام‌مند کرد.",
        ],
        detailed_analysis="تحلیل عمیق نشان می‌دهد سخت‌ترین آزمون اخلاق اقناع، اصل انصاف است: بسیاری از پیام‌ها راست و محترمانه‌اند، اما سود و زیان را نابرابر توزیع می‌کنند. در تبلیغات دیجیتال، الگوریتم‌های هدف‌گیری همین عدم تعادل را پنهان می‌سازند، زیرا مخاطب از شیوهٔ گزینش پیام آگاه نیست. از این رو چارچوب باید با شفافیت الگوریتمی و حق آگاهی مخاطب تکمیل شود.",
        critique_text="نقد اصلی آن است که سنجش اصالت و انصاف دشوار است، داوری به زمینهٔ فرهنگی وابسته می‌ماند و خطر تبدیل چارچوب به فهرست تشریفاتی وجود دارد.",
        example_text="تبلیغ یک نوشیدنی انرژی‌زا که تنها فواید را برجسته می‌کند و عوارض را پنهان می‌گذارد، در اصل راست‌گویی و انصاف رد می‌شود؛ همان تبلیغ با اعلام کامل ترکیبات و هشدار مصرف، به اقناع اخلاقی نزدیک‌تر می‌شود.",
        year=2001,
    ),
    "MC-598": dict(
        summary="چارچوب «روابط عمومی به‌عنوان مدیریت معنا» روابط عمومی را نه انتقال پیام، بلکه مشارکت در ساختن و بازسازی معنای مشترک می‌داند. رابرت هیث در مقالهٔ سال ۱۹۹۳ خود رویکردی بلاغی به روابط عمومی پیشنهاد کرد و نشان داد سازمان‌ها در پهنه‌ای از معناها عمل می‌کنند که ذی‌نفعان، رسانه‌ها و نهادها در آن سهیم‌اند. در این نگاه، روابط عمومی کوششی است برای تعریف موضوع، تعیین واژگان و شکل‌دادن به چارچوبی که عموم در آن دربارهٔ سازمان داوری می‌کند. هیث این وضعیت را «کشمکش در بازار معنا» توصیف کرد: سازمان و منتقدانش در رقابتی بلاغی می‌کوشند معنای رفتار سازمانی را تعیین کنند. بنابراین ارتباطات سازمانی نه پوشش بیرونی واقعیت، بلکه بخشی از خود واقعیت سازمانی است. چارچوب سه وظیفه برای روابط عمومی تعریف می‌کند: ایجاد و حفظ پهنه‌های معنای مشترک، پاسخ‌گویی بلاغی به نقدها و مشارکت در گفت‌وگوی عمومی دربارهٔ منافع و مسئولیت‌ها. کاربرد آن در مدیریت بحران، ارتباطات مسئولیت اجتماعی، روابط با رسانه و تحلیل چارچوب‌بندی اخبار سازمانی گسترده است. نقد اصلی به این چارچوب، خطر تبدیل مدیریت معنا به مدیریت تصویر، کم‌توجهی به نابرابری قدرت میان سازمان و منتقدان و دشواری سنجش اثر بلاغی است؛ این چارچوب امروز در تحلیل روایت بحران و اعتبار سازمانی کاربرد گسترده دارد. یادآوری: متن کارت تحریریهٔ این مدخل با محتوای آن هم‌خوان نبود و مستندسازی حاضر بر پایهٔ منابع تأییدشده بازنویسی شده است.",
        definition="مدیریت معنا در روابط عمومی، فرایند مشارکت راهبردی سازمان در ساختن، تثبیت و بازسازی معناهایی است که ذی‌نفعان بر پایهٔ آن‌ها دربارهٔ سازمان داوری می‌کنند.",
        main_problem="چگونه سازمان می‌تواند در رقابت بلاغی بر سر معنای رفتار خود مشارکت کند و اعتماد بسازد، بی‌آنکه به دستکاری تصویر و پنهان‌سازی فروکاسته شود.",
        mechanism="سازمان با انتخاب واژگان، روایت و چارچوب، معنای رفتار خود را پیشنهاد می‌کند؛ ذی‌نفعان و رسانه‌ها آن را می‌پذیرند، تعدیل یا رد می‌کنند و معنای نهایی در تعامل این کنش‌ها شکل می‌گیرد.",
        assumptions=[
            "معنا در تعامل ساخته می‌شود، نه در پیام یک‌سویه.",
            "سازمان در بازار معنا با رقبا و منتقدان شریک است.",
            "زبان و چارچوب، ابزار اصلی مدیریت معناست.",
            "پاسخ‌گویی بلاغی، شرط مشروعیت سازمان است.",
        ],
        principles=[
            "روابط عمومی مشارکت در ساخت معناست، نه انتقال محض.",
            "پهنهٔ معنای مشترک، پیش‌شرط گفت‌وگوی مؤثر است.",
            "سازمان باید به نقدها پاسخ بلاغی و مستند بدهد.",
            "معنای رفتار سازمانی در گفت‌وگوی عمومی تعیین می‌شود.",
        ],
        critiques=[
            "مدیریت معنا می‌تواند به مدیریت تصویر و پنهان‌کاری تبدیل شود.",
            "نابرابری قدرت میان سازمان و منتقدان کم‌تر تحلیل می‌شود.",
            "سنجش اثر بلاغی دشوار و اغلب کیفی است.",
            "خطر تقلیل واقعیت سازمانی به روایت وجود دارد.",
        ],
        applications=[
            "مدیریت بحران و بازسازی معنا پس از رسوایی.",
            "طراحی روایت مسئولیت اجتماعی و پاسخ به نقد.",
            "تحلیل چارچوب‌بندی اخبار دربارهٔ سازمان‌ها.",
            "آموزش ارتباطات سازمانی با رویکرد بلاغی.",
        ],
        evolution="هیث (۱۹۹۳) رویکرد بلاغی و پهنه‌های معنا را به روابط عمومی معرفی کرد؛ پژوهش‌های بعدی آن را با نظریهٔ گفت‌وگو، شهرت و رسانه‌های اجتماعی ترکیب کردند و ایهلن (۲۰۱۱) پیوند بلاغت و روابط عمومی را نظام‌مند ساخت.",
        key_concepts=[
            "پهنهٔ معنا (Zone of Meaning)",
            "بازار معنا (Marketplace of Meaning)",
            "پاسخ‌گویی بلاغی (Rhetorical Accountability)",
            "چارچوب‌بندی سازمانی (Organizational Framing)",
            "گفت‌وگوی عمومی (Public Dialogue)",
        ],
        theorists="رابرت هیث؛ اویویند ایهلن",
        theorists_text="هیث (۱۹۹۳)؛ ایهلن (۲۰۱۱)",
        model="پیشنهاد معنا توسط سازمان → تفسیر ذی‌نفعان و رسانه → کشمکش بلاغی → تثبیت یا بازسازی معنای مشترک.",
        studies=[
            "هیث (۱۹۹۳) روابط عمومی را مشارکت بلاغی در پهنه‌های معنا تعریف کرد.",
            "ایهلن (۲۰۱۱) بنیان بلاغی روابط عمومی و پیوند آن با قدرت را تحلیل کرد.",
        ],
        detailed_analysis="تحلیل عمیق نشان می‌دهد سازمان در بحران، پیش از آنکه با واقعیت روبه‌رو شود، با معنای واقعیت روبه‌روست. انتخاب واژهٔ «خطا» یا «تخلف»، «جبران» یا «عذرخواهی»، چارچوب داوری عمومی را تعیین می‌کند. قدرت سازمان در پیشنهاد معناست، اما نتیجهٔ نهایی در گفت‌وگو تعیین می‌شود. از این رو مدیریت معنا زمانی مشروع است که با شفافیت و پذیرش نقد همراه باشد.",
        critique_text="نقد اصلی آن است که مدیریت معنا می‌تواند به مدیریت تصویر و پنهان‌کاری تبدیل شود، نابرابری قدرت را نادیده بگیرد و سنجش اثر بلاغی آن دشوار باشد.",
        example_text="شرکتی که پس از نقص فنی، حادثه را «رویدادی نادر» بنامد، معنایی متفاوت از «خطای قابل پیشگیری» پیشنهاد می‌کند؛ پذیرش یا رد این معنا توسط رسانه و عموم، نتیجهٔ همان کشمکش بلاغی است.",
        year=1993,
    ),
    "MC-600": dict(
        summary="قانون متکالف، قاعده‌ای برای ارزش‌گذاری شبکه است و می‌گوید ارزش یک شبکه با مربع تعداد کاربران متصل آن رشد می‌کند. رابرت متکالف، مخترع اترنت، این ایده را حدود سال ۱۹۸۰ در توضیح ارزش شبکه‌های ارتباطی مطرح کرد: با افزایش تعداد کاربران، شمار پیوندهای ممکن میان آن‌ها به‌صورت ترکیبی رشد می‌کند و بنابراین ارزش شبکه با توان دوم تعداد کاربران افزایش می‌یابد. این قانون در دههٔ ۱۹۹۰ با گسترش اینترنت و شبکه‌های اجتماعی به استدلالی رایج برای توجیه رشد انفجاری پلتفرم‌ها تبدیل شد. منطق آن بر اثر شبکه استوار است: هر کاربر تازه، نه فقط برای خود ارزش می‌آورد، بلکه برای همهٔ کاربران پیشین امکان پیوند تازه می‌سازد. کاربرد آن در تحلیل ارزش پلتفرم، توجیه سرمایه‌گذاری، ارزیابی سیاست اتصال اجباری و تحلیل رقابت شبکه‌ای است. نقدهای مهمی به آن وارد شده است: اودلیزکو و تیلی نشان دادند که ارزش شبکه احتمالاً با حاصل‌ضرب تعداد کاربران در لگاریتم آن رشد می‌کند، زیرا نه همهٔ پیوندهای ممکن ارزشمندند؛ برخی پژوهش‌ها نیز رشد ارزش را با محدودیت‌های ظرفیت، کیفیت و توجه محدود دانسته‌اند. متکالف خود در مقالهٔ ۲۰۱۳ پذیرفت که این قانون تقریبی است و با داده‌های واقعی باید سنجیده شود. نقد اصلی به کاربرد رسانه‌ای آن، نادیده‌گرفتن کیفیت پیوند، الگوریتم‌های گزینش و ارزش منفی برخی پیوندهاست.",
        definition="قانون متکالف، قاعده‌ای است که ارزش یک شبکهٔ ارتباطی را متناسب با مربع تعداد کاربران متصل آن می‌داند و رشد ارزش را نتیجهٔ افزایش نمایی پیوندهای ممکن میان کاربران می‌شمارد.",
        main_problem="چگونه می‌توان ارزش اقتصادی و ارتباطی یک شبکه را با اندازهٔ آن توضیح داد، بدون آنکه کیفیت پیوندها، محدودیت توجه و اثرهای منفی نادیده گرفته شود.",
        mechanism="با افزودن هر کاربر، پیوندهای ممکن میان او و کاربران پیشین افزوده می‌شود؛ مجموع این پیوندها با توان دوم تعداد کاربران رشد می‌کند و بنابراین ارزش شبکه برای هر عضو افزایش می‌یابد.",
        assumptions=[
            "همهٔ پیوندهای ممکن میان کاربران ارزشمندند.",
            "کاربران به‌طور برابر در شبکه مشارکت می‌کنند.",
            "ظرفیت شبکه و توجه کاربران محدودیت جدی ندارد.",
            "ارزش شبکه را می‌توان با تعداد کاربر سنجید.",
        ],
        principles=[
            "ارزش شبکه با افزایش کاربران به‌صورت غیرخطی رشد می‌کند.",
            "هر کاربر تازه برای کاربران پیشین ارزش می‌آفریند.",
            "اندازهٔ شبکه، مزیت رقابتی پلتفرم‌ها را توضیح می‌دهد.",
            "قانون تقریبی است و باید با دادهٔ واقعی سنجیده شود.",
        ],
        critiques=[
            "همهٔ پیوندها ارزشمند نیستند و ارزش با لگاریتم کاربران نیز رشد می‌کند.",
            "کیفیت پیوند، توجه محدود و هزینهٔ نگهداری نادیده گرفته می‌شود.",
            "ارزش منفی پیوندها مانند هرزنامه و اطلاعات نادرست حساب نمی‌شود.",
            "تعداد کاربر ثبت‌نام‌شده با کاربر فعال برابر نیست.",
        ],
        applications=[
            "ارزش‌گذاری پلتفرم‌های رسانه‌ای و شبکه‌های اجتماعی.",
            "تحلیل مزیت رقابتی و اثر شبکه در بازار پلتفرم.",
            "توجیه سرمایه‌گذاری در زیرساخت ارتباطی.",
            "نقد سنجه‌های رشد مبتنی بر تعداد کاربر.",
        ],
        evolution="متکالف ایده را حدود ۱۹۸۰ مطرح کرد؛ در دههٔ ۱۹۹۰ با رشد اینترنت رایج شد؛ نقدهای دههٔ ۲۰۰۰ رشد لگاریتمی را پیشنهاد کردند و متکالف (۲۰۱۳) قانون را با داده‌های واقعی بازبینی کرد.",
        key_concepts=[
            "اثر شبکه (Network Effect)",
            "رشد توان دوم (Quadratic Growth)",
            "پیوند ممکن (Potential Connection)",
            "کاربر فعال (Active User)",
            "بازخورد مثبت (Positive Feedback)",
        ],
        theorists="رابرت متکالف؛ اندرو اودلیزکو",
        theorists_text="متکالف (۲۰۱۳)؛ شاپیرو و واریان (۱۹۹۹)",
        model="افزایش کاربران → افزایش نمایی پیوندهای ممکن → رشد غیرخطی ارزش شبکه → مزیت رقابتی پلتفرم.",
        studies=[
            "متکالف (۲۰۱۳) قانون را با داده‌های واقعی شبکه بازبینی و محدودیت‌های آن را اعلام کرد.",
            "شاپیرو و واریان (۱۹۹۹) اثر شبکه و بازخورد مثبت را در اقتصاد اطلاعات تحلیل کردند.",
        ],
        detailed_analysis="تحلیل عمیق نشان می‌دهد قانون متکالف بیشتر استعاره‌ای راهبردی است تا فرمول دقیق ارزش. در پلتفرم‌های رسانه‌ای، ارزش برای هر کاربر به کیفیت محتوا، همتایان فعال و طراحی رابط بستگی دارد، نه فقط به شمار ثبت‌نام‌شدگان. از این رو سنجهٔ کاربر فعال و عمق تعامل، جایگزین بهتری برای ارزیابی ارزش شبکه است. قانون متکالف همچنان برای توضیح منطق رشد شبکه‌ها سودمند است، به شرط آنکه با شواهد تجربی و نقدهای نظری همراه شود.",
        critique_text="نقد اصلی آن است که همهٔ پیوندها ارزشمند نیستند، کیفیت پیوند و توجه محدود نادیده گرفته می‌شود و ارزش منفی برخی پیوندها در محاسبه نمی‌آید.",
        example_text="یک پیام‌رسان با دو برابر شدن کاربران، چهار برابر پیوند ممکن می‌سازد؛ اما اگر بیشتر پیوندها بی‌اثر یا هرزنامه باشد، ارزش واقعی به اندازهٔ پیش‌بینی قانون رشد نمی‌کند.",
        year=1980,
    ),
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


NAME_FIX = {}
YEAR_FIX = {
    "MC-582": "year corrected 2000 -> 2001 (verified anchor: Baker & Martinson, TARES Test, 2001); note: editorial card theorist attribution was unverifiable and documentation rebuilt from verified literature",
    "MC-598": "no year change; note: editorial card core_logic was a mismatched media-economics template, documentation rebuilt from Heath (1993) and Ihlen (2011)",
}


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
                                       "verified": n_verified, "batch": 123}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH123 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
