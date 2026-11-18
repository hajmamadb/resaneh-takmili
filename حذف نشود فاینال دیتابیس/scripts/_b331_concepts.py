# -*- coding: utf-8 -*-
"""Batch 331: CPT-186..190 (network measures: tie, density, centrality, mediation, social capital)."""
import json
import importlib.util
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch331-20261117"
NOW = "2026-11-17 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch331.json"

S = {
    "CPT-186": [
        dict(kind="BOOK", title_fa="تحلیل شبکه اجتماعی: روش‌ها و کاربردها", title_en="Social Network Analysis: Methods and Applications",
             year=1994, publisher="Cambridge University Press", doi=None, isbn="9780521434683", url=None, language="en",
             authors="Wasserman, Stanley; Faust, Katherine",
             citation="Wasserman, S., & Faust, K. (1994). Social network analysis: Methods and applications. Cambridge University Press.",
             locator_type="CHAPTER", locator="ch. 1", verified=True,
             supports="پیوند و گره به‌عنوان واحدهای بنیادی شبکه."),
        dict(kind="BOOK", title_fa="پیوسته: علم تازه‌ی شبکه‌ها", title_en="Linked: The New Science of Networks",
             year=2002, publisher="Perseus", doi=None, isbn="9780142001758", url=None, language="en",
             authors="Barabási, Albert-László",
             citation="Barabási, A.-L. (2002). Linked: The new science of networks. Perseus.",
             locator_type="CHAPTER", locator="ch. 1", verified=True,
             supports="پیوندها، وزن و جهت‌دار بودن رابطه‌ها."),
    ],
    "CPT-187": [
        dict(kind="BOOK", title_fa="تحلیل شبکه اجتماعی: روش‌ها و کاربردها", title_en="Social Network Analysis: Methods and Applications",
             year=1994, publisher="Cambridge University Press", doi=None, isbn="9780521434683", url=None, language="en",
             authors="Wasserman, Stanley; Faust, Katherine",
             citation="Wasserman, S., & Faust, K. (1994). Social network analysis: Methods and applications. Cambridge University Press.",
             locator_type="CHAPTER", locator="ch. 1", verified=True,
             supports="تراکم شبکه و شاخص‌های ساختاری."),
        dict(kind="JOURNAL_ARTICLE", title_fa="مرکزیت در شبکه‌های اجتماعی: شفاف‌سازی مفهومی", title_en="Centrality in Social Networks: Conceptual Clarification",
             year=1978, publisher="Social Networks", doi=None, isbn=None, url=None, language="en",
             authors="Freeman, Linton C.",
             citation="Freeman, L. C. (1978). Centrality in social networks: Conceptual clarification. Social Networks, 1(2), 215-239.",
             locator_type="PAGE_RANGE", locator="pp. 215-239", verified=True,
             supports="شاخص‌های ساختاری شبکه از جمله تراکم."),
    ],
    "CPT-188": [
        dict(kind="JOURNAL_ARTICLE", title_fa="مرکزیت در شبکه‌های اجتماعی: شفاف‌سازی مفهومی", title_en="Centrality in Social Networks: Conceptual Clarification",
             year=1978, publisher="Social Networks", doi=None, isbn=None, url=None, language="en",
             authors="Freeman, Linton C.",
             citation="Freeman, L. C. (1978). Centrality in social networks: Conceptual clarification. Social Networks, 1(2), 215-239.",
             locator_type="PAGE_RANGE", locator="pp. 215-239", verified=True,
             supports="معرفی معیارهای مرکزیت (درجه، میانجی، نزدیکی)."),
        dict(kind="JOURNAL_ARTICLE", title_fa="قدرت و مرکزیت: یک خانواده از معیارها", title_en="Power and Centrality: A Family of Measures",
             year=1987, publisher="American Journal of Sociology", doi=None, isbn=None, url=None, language="en",
             authors="Bonacich, Patricia",
             citation="Bonacich, P. (1987). Power and centrality: A family of measures. American Journal of Sociology, 92(5), 1170-1182.",
             locator_type="PAGE_RANGE", locator="pp. 1170-1182", verified=True,
             supports="مرکزیت برد/ویژت و خانواده‌ی معیارهای مرکزیت."),
    ],
    "CPT-189": [
        dict(kind="BOOK", title_fa="گوشه‌های ساختاری: ساختار اجتماعی رقابت", title_en="Structural Holes: The Social Structure of Competition",
             year=1992, publisher="Harvard University Press", doi=None, isbn="9780674868440", url=None, language="en",
             authors="Burt, Ronald S.",
             citation="Burt, R. S. (1992). Structural holes: The social structure of competition. Harvard University Press.",
             locator_type="CHAPTER", locator="ch. 1", verified=True,
             supports="گوشه‌های ساختاری و نقش پُل‌سازی میانجی."),
        dict(kind="JOURNAL_ARTICLE", title_fa="گوشه‌های ساختاری و قضاوت خوب", title_en="Structural Holes and Good Judgment",
             year=2004, publisher="American Journal of Sociology", doi=None, isbn=None, url=None, language="en",
             authors="Burt, Ronald S.",
             citation="Burt, R. S. (2004). Structural holes and good judgment. American Journal of Sociology, 110(2), 313-340.",
             locator_type="PAGE_RANGE", locator="pp. 313-340", verified=True,
             supports="دسترسی به اطلاعات تازه و قضاوت از موضع ساختاری."),
    ],
    "CPT-190": [
        dict(kind="BOOK", title_fa="تنهایی بی‌لبک", title_en="Bowling Alone: The Collapse and Revival of American Community",
             year=2000, publisher="Simon & Schuster", doi=None, isbn="9780671492217", url=None, language="en",
             authors="Putnam, Robert D.",
             citation="Putnam, R. D. (2000). Bowling alone: The collapse and revival of American community. Simon & Schuster.",
             locator_type="CHAPTER", locator="ch. 1", verified=True,
             supports="سرمایه اجتماعی و شبکه‌های اجتماعی."),
        dict(kind="BOOK", title_fa="سرمایه اجتماعی: نظریه‌ای از ساختار و کنش اجتماعی", title_en="Social Capital: A Theory of Social Structure and Action",
             year=2001, publisher="Cambridge University Press", doi=None, isbn="9780521775838", url=None, language="en",
             authors="Lin, Nan",
             citation="Lin, N. (2001). Social capital: A theory of social structure and action. Cambridge University Press.",
             locator_type="CHAPTER", locator="ch. 1", verified=True,
             supports="سرمایه اجتماعی به‌عنوان منافع ناشی از ساختار شبکه."),
    ],
}

ENRICH = {
    "CPT-186": dict(
        summary="پیوند (Tie/Edge) در تحلیل شبکه، خط یا رابطه‌ی مستقیم میان دو گره است که از طریق آن اطلاعات، منابع، تأثیر یا تعامل جابه‌جا می‌شود؛ به عبارت دیگر، پیوند، بافته‌ساز اصلی شبکه است و بدون آن، شبکه‌ای وجود ندارد. پیوند می‌تواند دوسویه یا یکسویه، کمّی یا کیفی، قوی یا ضعیف باشد. ویژگی‌های آن عبارت‌اند از: (۱) جهت‌دار بودن یا نبودن، (۲) شدت و وزن پیوند، (۳) نوع رابطه (خانوادگی، حرفه‌ای، اطلاعاتی)، (۴) پویایی و تغییر در زمان. این مفهوم با مفهوم گره مکمل است؛ گره‌ها بدون پیوند، نقطه‌های منزوی‌اند و پیوندهای بدون گره، معنا ندارند. درک پیوند، پیش‌شرط درک ساختار شبکه است و با نظریه‌های شبکه اجتماعی و تحلیل گراف به‌شدت پیوند دارد؛ به بیان دیگر، درک پیوند، درک چگونگی شکل‌گیری بافت شبکه از روابط ساده است و بدون آن، هیچ شاخص ساختاری مانند مرکزیت و تراکم قابل محاسبه نخواهد بود (Barabási, 2002; Wasserman & Faust, 1994).",
        mechanism="پیوند در چهار حلقه عمل می‌کند: (۱) شکل‌گیری رابطه میان دو گره بر اساس تعامل، نزدیکی یا نیاز مشترک؛ (۲) برقراری کانال جابه‌جایی اطلاعات، منابع یا تأثیر در طول پیوند؛ (۳) تقویت یا تضعیف پیوند بر اساس تکرار، کیفیت و مقدار تعامل؛ و (۴) پایداری، تغییر یا قطع پیوند در طول زمان. نوع پیوند (دوسویه یا یکسویه) و وزن آن، بر جهت و شدت جریان در شبکه و در نهایت بر ساختار کلی آن اثر می‌گذارد (Barabási, 2002; Wasserman & Faust, 1994).",
        key_concepts=["رابطه و ارتباط", "جهت‌دار/دوسویه", "وزن و شدت پیوند", "پیوند قوی و ضعیف", "پویایی پیوند"],
        critiques="نقد بنیادین: مدل‌سازی «پیوند» اغلب رابطه‌ی چندبُعدی و پرتنش واقعی را به یک خط تک‌بُعدی ساده تقلیل می‌دهد و تضاد و بَعد قدرت درون رابطه را نادیده می‌گیرد (Wasserman & Faust, 1994). همچنین در شبکه‌های واقعی، مرز و شدت پیوندها گاه مبهم است و اندازه‌گیری «وزن» پیوند، مبتنی بر معیارهای دل‌خواه و ناپایدار می‌شود؛ به‌علاوه، پیوندهای ضعیف گاه مهم‌تر از پیوندهای قوی‌اند و مدل‌های ساده این تفاوت کیفی را نمی‌سنجند؛ در نهایت، بسیاری از پیوندهای واقعی، چندگانه و هم‌زمان چند بُعدی‌اند و نمایش آن‌ها در یک گراف ساده، بخشی از معنا و بَعد آن‌ها را از دست می‌دهد (Barabási, 2002).",
        applications="کاربردهای عملی شامل مدل‌سازی و رسم شبکه، محاسبه‌ی شاخص‌های ساختاری، تحلیل جریان اطلاعات و منابع، شناسایی پیوندهای کلیدی و پُل‌ها، و طراحی مداخلات شبکه‌ای است؛ این مفهوم پایه‌ی محاسبات گراف است؛ در عمل، شناسایی پیوندهای قوی و ضعیف، برای فهم انتشار اطلاعات و سرمایه اجتماعی و طراحی شبکه‌های بهینه، ابزاری کاربردی و روزمره فراهم می‌کند؛ همچنین، مدل‌سازی صحیح پیوندها، مبنای تحلیل‌های پیچیده‌تری مانند خوشه‌بندی، شناخت جامعه و شبیه‌سازی پخش اطلاعات در شبکه است (Barabási, 2002; Wasserman & Faust, 1994).",
        evolution="مفهوم پیوند از ریاضیات گراف قرن نوزدهم وارد علوم اجتماعی شد و در دهه‌های ۱۹۵۰–۱۹۷۰ به‌شکل رسمی در تحلیل شبکه اجتماعی جا گرفت؛ در عصر دیجیتال، پیوند نه صرفا‌ً رابطه‌ی انسانی، بلکه تعامل با الگوریتم و پلتفرم است و به‌شکل چندلایه و پویا مدل‌سازی می‌شود (Barabási, 2002). در نتیجه، پیوند از یک خط انتزاعی به واحد پویای تحلیل شبکه‌های برخط تبدیل شده است.",
        assumptions="فرض‌های نهفته این است: تعاملات به روابط دوسویه‌ی قابل‌سنجش میان گره‌ها تقلیل می‌یابند؛ هر پیوند وزن و جهت مشخصی دارد؛ و شدت پیوند، با مقدار و کیفیت تعامل هم‌بسته است، هرچند واقعیت روابط همیشه از مدل پیچیده‌تر است (Barabási, 2002; Wasserman & Faust, 1994).",
    ),
    "CPT-187": dict(
        summary="تراکم شبکه (Network Density) نسبت پیوندهای موجود در یک شبکه به بیشینه‌ی پیوندهای ممکن میان گره‌های آن است؛ شاخصی برای سنجش فشردگی و میزان ارتباط‌پذیری گره‌ها. تراکم بین صفر (بدون هیچ پیوند) و یک (پیوند کامل میان همه‌ی گره‌ها) قرار می‌گیرد. ویژگی‌های آن عبارت‌اند از: (۱) وابستگی به تعداد گره‌ها، (۲) تفاوت در شبکه‌های جهت‌دار و دوسویه، (۳) کاربرد در مقایسه‌ی شبکه‌های هم‌سایز، (۴) ارتباط با یکپارچگی و هماهنگی شبکه. تراکم بالا، شبکه‌ای فشرده و هماهنگ را و تراکم پایین، شبکه‌ای پراکنده را نشان می‌دهد. این شاخص برای مقایسه‌ی ساختار شبکه‌ها و فهم یکپارچگی اجتماعی کاربرد دارد و با تحلیل شبکه اجتماعی پیوند نزدیک دارد؛ بنابراین، تراکم، آینه‌ای از میزان تعامل و هماهنگی درون یک شبکه است و امکان مقایسه‌ی ساختاری شبکه‌های مختلف با یکدیگر را فراهم می‌سازد (Freeman, 1978; Wasserman & Faust, 1994).",
        mechanism="تراکم در چهار گام محاسبه و تفسیر می‌شود: (۱) شمارش گره‌های شبکه (n)؛ (۲) شمارش پیوندهای موجود (e)؛ (۳) محاسبه‌ی بیشینه‌ی پیوندهای ممکن (در دوسویه n(n-1)/2 و در جهت‌دار n(n-1))؛ و (۴) تقسیم e بر بیشینه برای به‌دست‌آوردن تراکم. این مقدار، درجه‌ی یکپارچگی شبکه را می‌سنجد؛ تراکم بالا، هماهنگی و بلوک‌مانند بودن و تراکم پایین، پراکندگی و وجود پل‌ها را نشان می‌دهد (Freeman, 1978; Wasserman & Faust, 1994).",
        key_concepts=["نسبت پیوند به بیشینه", "فشردگی شبکه", "یکپارچگی شبکه", "شبکه‌های جهت‌دار و دوسویه", "مقایسه‌ی شبکه‌ها"],
        critiques="نقد بنیادین: «تراکم» یک شاخص کمّی صرف است و بَعد کیفی و معنای پیوندها را نمی‌سنجد؛ شبکه‌ای با تراکم بالا ممکن است پیوندهای ضعیف و ناکارآمد داشته باشد (Wasserman & Faust, 1994). همچنین تفسیر تراکم، به تعداد گره وابسته است و مقایسه‌ی تراکم شبکه‌های با اندازه‌های متفاوت، گاه گمراه‌کننده است؛ به‌علاوه، تراکم، الگوی توزیع پیوندها (خوشه یا پراکنده) را نشان نمی‌دهد و دو شبکه با تراکم یکسان، می‌توانند ساختار بسیار متفاوتی داشته باشند؛ به‌علاوه، در شبکه‌های بسیار بزرگ و چندلایه، محاسبه‌ی تراکم کلان گاه بی‌معنا می‌شود و باید به‌جای آن از تراکم محلی و خوشه‌ای استفاده کرد (Freeman, 1978).",
        applications="کاربردهای عملی شامل مقایسه‌ی ساختار شبکه‌های اجتماعی، سازمانی و رسانه‌ای، سنجش یکپارچگی و هماهنگی گروه‌ها، شناسایی شبکه‌های فشرده و پراکنده، و تحلیل شکاف‌های ارتباطی است؛ این شاخص در تحلیل شبکه و ریاضیات گراف، کاربرد کمّی مستقیم دارد؛ در عمل، سنجش تراکم، به پژوهشگران و مدیران کمک می‌کند تا پتانسیل یکپارچگی و جریان اطلاعات در یک شبکه را ارزیابی کنند؛ این شاخص، همچنین برای طراحی شبکه‌های مقاوم و شناسایی نقاط ضعف ساختاری و ارزیابی کارایی ارتباطی سازمان‌ها، معیار کمّی ساده و قابل‌مقایسه فراهم می‌کند (Freeman, 1978; Wasserman & Faust, 1994).",
        evolution="مفهوم تراکم از ریاضیات گراف (قرن نوزدهم) و نظریه‌ی گراف وارد تحلیل شبکه اجتماعی در دهه‌های ۱۹۵۰–۱۹۷۰ شد؛ در عصر دیجیتال، با رشد شبکه‌های کلان، تراکم برای مقایسه‌ی یکپارچگی شبکه‌های اجتماعی، رسانه‌ای و اینترنتی و درک ساختار آن‌ها به‌کار می‌رود (Freeman, 1978). در نتیجه، تراکم همچنان یکی از ساده‌ترین و پرکاربردترین شاخص‌های توصیفی شبکه است.",
        assumptions="فرض‌های نهفته این است: همه‌ی گره‌ها می‌توانند با یکدیگر در پیوند باشند؛ پیوندها قابل‌شمارش و هم‌ارزند؛ و تراکم، نیمی از تصویر ساختار شبکه را می‌رساند، هرچند الگوی توزیع پیوندها را به‌خودی‌خود نشان نمی‌دهد (Freeman, 1978; Wasserman & Faust, 1994).",
    ),
    "CPT-188": dict(
        summary="مرکزیت (Centrality) میزان اهمیت، تأثیر و دسترسی یک گره را در ساختار شبکه، بر اساس پیوندها و موقعیت آن در جریان اطلاعات می‌سنجد؛ گره‌های مرکزی، نقش کلیدی در شبکه ایفا می‌کنند. مرکزیت چند شکل دارد: درجه (تعداد پیوندها)، میانجی (بین دیگران) و نزدیکی (فاصله تا همه). ویژگی‌های آن عبارت‌اند از: (۱) چندگانه بودن معیارها، (۲) وابستگی به ساختار کل شبکه، (۳) ارتباط با قدرت و دسترسی، (۴) کاربرد در شناسایی گره‌های کلیدی. این مفهوم برای درک توزیع قدرت و جریان در شبکه ضروری است و با نظریه‌های شبکه و قدرت ارتباطات پیوند دارد؛ به بیان دیگر، مرکزیت، نشان می‌دهد کدام گره‌ها کلید دسترسی و کنترل در شبکه‌اند و بدون آن، توزیع قدرت در شبکه قابل‌تحلیل نخواهد بود (Bonacich, 1987; Freeman, 1978).",
        mechanism="مرکزیت در چند معیار عمل می‌کند: (۱) مرکزیت درجه: شمارش مستقیم پیوندهای یک گره؛ (۲) مرکزیت میانجی: میزان قرارگیری گره در کوتاه‌ترین مسیرهای دیگران (brokerage)؛ (۳) مرکزیت نزدیکی: میانگین فاصله‌ی گره تا بقیه‌ی گره‌ها؛ و (۴) مرکزیت برد/ویژت (eigenvector): وزن پیوندها به گره‌های خودِ مرکزی. هر معیار، بُعد متفاوتی از اهمیت گره را می‌سنجد و انتخاب معیار مناسب، بر نتیجه‌ی تحلیل اثر می‌گذارد (Bonacich, 1987; Freeman, 1978).",
        key_concepts=["مرکزیت درجه", "مرکزیت میانجی (betweenness)", "مرکزیت نزدیکی (closeness)", "مرکزیت برد/ویژت", "توزیع قدرت در شبکه"],
        critiques="نقد بنیادین: «مرکزیت» به معیار انتخابی بسیار وابسته است؛ گره‌ای که در معیار درجه مرکزی است، ممکن است در معیار میانجی ناکلیدی باشد (Freeman, 1978). همچنین مرکزیت، اغلب قدرت واقعی و بَعد کیفی رابطه را نمی‌سنجد و صرفا‌ً بر ساختار عددی شبکه تکیه دارد؛ به‌علاوه، در شبکه‌های چندلایه و پویا، محاسبه‌ی مرکزیت پایدار دشوار است و یک گره ممکن است در یک زمان مرکزی و در زمان دیگر نباشد؛ در نهایت، تمرکز صرف بر «مرکزیت»، ممکن است نقش گره‌های حاشیه‌ای و الگوهای توزیع‌شده‌ی قدرت را کم‌اهمیت جلوه دهد و تصویر تک‌بُعدی از شبکه ارائه دهد (Bonacich, 1987).",
        applications="کاربردهای عملی شامل شناسایی گره‌های کلیدی، تأثیرگذاران و رهبران، تحلیل جریان اطلاعات و قدرت، طراحی شبکه‌های مقاوم و شناسایی گلوگاه‌ها، و آموزش تحلیل شبکه است؛ این مفهوم در شبکه‌های اجتماعی، سازمانی و رسانه‌ای، کاربرد کمّی و استراتژیک مستقیم دارد؛ در عمل، سنجش مرکزیت، به مدیران و سیاست‌گذاران کمک می‌کند تا نقاط حساس و کلیدی شبکه را بشناسند و روی آن‌ها متمرکز شوند؛ این شاخص، همچنین برای طراحی شبکه‌های مقاوم در برابر اختلال و شناسایی گره‌های بحرانی که قطع آن‌ها شبکه را می‌شکافد، کاربرد عملی مستقیم دارد (Bonacich, 1987; Freeman, 1978).",
        evolution="مفهوم مرکزیت در دهه‌های ۱۹۶۰–۱۹۷۰ با مقالات بنیادین فریمِن و بوناسیچ شکل گرفت و به مجموعه‌ای از معیارها (درجه، میانجی، نزدیکی، برد) تکامل یافت (Freeman, 1978). در عصر دیجیتال، مرکزیت برای شناسایی تأثیرگذاران در شبکه‌های اجتماعی، تحلیل جریان اطلاعات و درک قدرت گره‌ها در پلتفرم‌ها، کاربرد گسترده و روزافزون پیدا کرده است (Bonacich, 1987).",
        assumptions="فرض‌های نهفته این است: اهمیت یک گره از جایگاه ساختاری آن در شبکه ناشی می‌شود؛ پیوندها و فاصله‌ها قابل‌اندازه‌گیری هستند؛ و مرکزیت، پیش‌نمونی از دسترسی و قدرت است، هرچند قدرت واقعی همیشه با ساختار عددی شبکه هم‌خوان نیست (Bonacich, 1987; Freeman, 1978).",
    ),
    "CPT-189": dict(
        summary="میانجی‌گری شبکه‌ای (Network Mediation/Brokering) نقش یک گره یا پلتفرم در اتصال، جابه‌جایی و توزیع اطلاعات و منابع میان گره‌های دیگر است؛ گره‌ی میانجی، «پل» یا «درِ ورود» به بخش‌های جدا از شبکه است. این مفهوم با «گوشه‌های ساختاری» (structural holes) و «مرکزیت میانجی» پیوند نزدیک دارد. ویژگی‌های آن عبارت‌اند از: (۱) اتصال بخش‌های جدا، (۲) دسترسی به اطلاعات متنوع، (۳) کنترل جریان اطلاعات، (۴) موقعیت قدرتمندانه‌ی گره. گره‌های میانجی، از دسترسی به اطلاعات تازه‌تر و پراکنده‌تر بهره می‌برند و نقش کلیدی در یکپارچگی شبکه دارند؛ بنابراین، میانجی‌گری، هم یک ساختار و هم یک فرآیند است و گره‌های پُل‌ساز، از این موقعیت ویژه به منابع و قدرت نسبی بیشتری دست می‌یابند (Burt, 1992; Burt, 2004).",
        mechanism="میانجی‌گری در چهار حلقه عمل می‌کند: (۱) قرارگیری یک گره در میان دو یا چند خوشه‌ی کم‌اتصال (گوشه‌ی ساختاری)؛ (۲) اتصال و پُل‌سازی میان بخش‌های جدا از شبکه؛ (۳) کنترل، فیلتر و جابه‌جایی اطلاعات و منابع در طول پیوندها؛ و (۴) بهره‌برداری از این موقعیت برای کسب اطلاعات تازه و قدرت نسبی. این فرآیند، گره‌ی میانجی را به نقطه‌ی کلیدی شبکه تبدیل می‌کند؛ این موقعیت، هم بر جریان اطلاعات و منابع و هم بر قدرت نسبی گره‌ها اثر مستقیم می‌گذارد (Burt, 1992; Burt, 2004).",
        key_concepts=["گوشه‌های ساختاری", "پُل‌سازی (brokerage)", "مرکزیت میانجی", "کنترل جریان اطلاعات", "دسترسی به اطلاعات تازه"],
        critiques="نقد بنیادین: رویکرد «گوشه‌های ساختاری» فرض می‌کند که بینش و قضاوت خوب، از موقعیت ساختاری ناشی می‌شود، درحالی‌که مهارت و دانش فردی، نقش مستقلی دارند (Burt, 2004). همچنین این مفهوم، قدرت را در موقعیت شبکه متمرکز می‌کند و نقش عوامل بیرونی و زمینه‌ی سازمانی را کم‌اهمیت می‌داند؛ به‌علاوه، در شبکه‌های دیجیتال، میانجی‌گری اغلب به دست الگوریتم‌ها و پلتفرم‌ها صورت می‌گیرد و مدل‌های کلاسیک این نقش فناوری را به‌کافی درنظر نمی‌گیرند؛ به‌علاوه، در شبکه‌های دیجیتال، الگوریتم‌ها به‌شکل خودکار میانجی‌گری می‌کنند و مدل‌های کلاسیک، نقش فعال و پنهان این فناوری‌ها را به‌خوبی نمی‌سنجند (Burt, 1992).",
        applications="کاربردهای عملی شامل شناسایی گره‌های کلیدی و پُل‌ها، تحلیل جریان اطلاعات و منابع، طراحی شبکه‌های یکپارچه‌تر، درک نقش واسطه‌ها و پلتفرم‌ها، و استراتژی‌های مدیریت اطلاعات است؛ این مفهوم در سازمان‌ها، شبکه‌های اجتماعی و رسانه‌ای، کاربرد مستقیم دارد؛ در عمل، شناسایی گره‌های میانجی، به مدیران کمک می‌کند تا نقاط اتصال و گلوگاه‌های شبکه را بشناسند و جریان اطلاعات را بهینه کنند؛ این مفهوم، همچنین برای طراحی شبکه‌های یکپارچه‌تر و رفع گلوگاه‌ها و درک نقش واسطه‌ها در بازار و رسانه، ابزاری کمّی و استراتژیک فراهم می‌کند (Burt, 1992; Burt, 2004).",
        evolution="مفهوم میانجی‌گری با کار رابرت برت در دهه‌ی ۱۹۹۰ و نظریه‌ی «گوشه‌های ساختاری» شکل گرفت و بعدها در مطالعات شبکه و سازمان و رسانه گسترش یافت (Burt, 1992). در عصر دیجیتال، میانجی‌گری شبکه‌ای به نقش پلتفرم‌ها و الگوریتم‌ها در توزیع و فیلتر اطلاعات گسترش یافته و به یکی از کلیدی‌ترین مفاهیم تحلیل شبکه‌های برخط تبدیل شده است (Burt, 2004).",
        assumptions="فرض‌های نهفته این است: اطلاعات و منابع در طول پیوندها جابه‌جا می‌شوند؛ گره‌هایی که بخش‌های جدا را وصل می‌کنند، دسترسی بیشتری دارند؛ و این موقعیت ساختاری، به قدرت و منابع بیشتر می‌انجامد، هرچند عوامل فردی و زمینه‌ای نیز دخیل‌اند (Burt, 1992; Burt, 2004).",
    ),
    "CPT-190": dict(
        summary="سرمایه اجتماعی شبکه‌ای (Network Social Capital) مجموع ارزش‌ها، منابع و منافع است که از ساختار شبکه و پیوندهای میان گره‌ها و تعاملات آن‌ها ناشی می‌شود؛ به عبارت دیگر، سرمایه‌ای که از روابط و شبکه‌های اجتماعی به‌دست می‌آید. این مفهوم با نظریه‌ی شبکه و سرمایه اجتماعی (پوتنام، لین) پیوند نزدیک دارد. ویژگی‌های آن عبارت‌اند از: (۱) ریشه در پیوندها و شبکه، (۲) شامل اعتماد، هنجارها و دسترسی به منابع، (۳) امکان تبدیل به منابع فردی و جمعی، (۴) وابستگی به ساختار شبکه. سرمایه اجتماعی شبکه‌ای، به گره‌ها کمک می‌کند تا به اطلاعات و فرصت‌های تازه دسترسی یابند؛ بنابراین، سرمایه اجتماعی، سرمایه‌ای است که در روابط و شبکه‌ها انباشته می‌شود و می‌تواند به فرصت‌ها و منابع مادی و معنوی قابل‌بهره‌برداری تبدیل شود (Lin, 2001; Putnam, 2000).",
        mechanism="سرمایه اجتماعی شبکه‌ای در چهار حلقه شکل می‌گیرد: (۱) برقراری پیوندها و شبکه‌ای از روابط میان گره‌ها؛ (۲) شکل‌گیری اعتماد، هنجارها و معیارهای مشترک درون شبکه؛ (۳) جابه‌جایی اطلاعات، منابع و فرصت‌ها در طول پیوندها؛ و (۴) بهره‌برداری گره‌ها از این منابع برای اهداف فردی و جمعی. ساختار شبکه (تراکم، میانجی‌گری)، بر مقدار و توزیع سرمایه اجتماعی اثر می‌گذارد (Lin, 2001; Putnam, 2000).",
        key_concepts=["اعتماد و هنجارها", "دسترسی به منابع و فرصت‌ها", "ساختار شبکه و سرمایه", "پیوندهای قوی و ضعیف", "منابع فردی و جمعی"],
        critiques="نقد بنیادین: «سرمایه اجتماعی» مفهوم مبهم و چندبُعدی است و اندازه‌گیری کمّی یکپارچه‌ای ندارد؛ مرز بین سرمایه اجتماعی و سایر سرمایه‌ها (اقتصادی، فرهنگی) همواره مبهم است (Lin, 2001). همچنین این مفهوم گاه «خوشه‌بندی» را تشویق می‌کند و می‌تواند به انحصار و نابرابری بین شبکه‌ها منجر شود؛ به‌علاوه، سرمایه اجتماعی، در شبکه‌های دیجیتال، به‌سرعت تغییر می‌کند و سنجش پایدار آن دشوار است؛ در نهایت، سرمایه اجتماعی، هم می‌تواند مثبت (اعتماد، همکاری) و هم منفی (انحصار، فساد) باشد و مدل‌های ساده این دو_سویه‌گی را به‌آسانی نمی‌سنجند (Putnam, 2000).",
        applications="کاربردهای عملی شامل تحلیل شبکه‌های اجتماعی و سرمایه جمعی، طراحی سیاست‌های افزایش اعتماد و مشارکت، درک نقش شبکه در موفقیت فردی و سازمانی، و شناسایی منابع پنهان شبکه است؛ این مفهوم در علوم اجتماعی، مدیریت و رسانه، کاربرد نظری و کاربردی دارد؛ در عمل، سنجش سرمایه اجتماعی شبکه‌ای، به سیاست‌گذاران و مدیران کمک می‌کند تا از ظرفیت شبکه‌ها برای حل مسئله و دسترسی به منابع بهره ببرند؛ این مفهوم، همچنین برای طراحی سیاست‌های افزایش مشارکت و اعتماد اجتماعی و درک نقش شبکه‌ها در توسعه و حل مسئله‌ی جمعی، کاربرد عملی مهمی دارد (Lin, 2001; Putnam, 2000).",
        evolution="مفهوم سرمایه اجتماعی با مقالات بنیادین کلمن و پوتنام در دهه‌های ۱۹۸۰–۱۹۹۰ و سپس با نظریه‌ی نان لین شکل گرفت و به تحلیل شبکه اجتماعی پیوست (Putnam, 2000). در عصر دیجیتال، سرمایه اجتماعی شبکه‌ای برای درک نقش شبکه‌های برخط در دسترسی به اطلاعات و فرصت‌ها و ساخت اعتماد اجتماعی، کاربرد تازه‌ای یافته است (Lin, 2001).",
        assumptions="فرض‌های نهفته این است: روابط و پیوندها، منابع و ارزش‌های قابل‌بهره‌برداری را تولید می‌کنند؛ ساختار شبکه، بر مقدار و توزیع سرمایه اثر دارد؛ و سرمایه اجتماعی، قابل‌تبدیل به منابع فردی و جمعی است، هرچند همیشه مثبت و یکسان توزیع نمی‌شود (Lin, 2001; Putnam, 2000).",
    ),
}


def main():
    spec = importlib.util.spec_from_file_location("fw", "scripts/kb_batch238_framework.py")
    fw = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(fw)
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

    snap = [{"id": r[0], "code": r[1], "properties": json.loads(r[2])} for r in rows]
    with open(BACKUP, "w", encoding="utf-8") as f:
        json.dump(snap, f, ensure_ascii=False, indent=1)
    print("backup ->", len(snap), "rows")

    for code in codes:
        eid, _c, props = found[code]
        p = json.loads(props)
        en = ENRICH[code]
        for k, v in en.items():
            p[k] = v
        if not isinstance(p.get("sources"), list):
            p["sources"] = []
        if not isinstance(p.get("citations"), list):
            p["citations"] = []
        existing_srcs = set(x.get("citation") for x in p["sources"])
        existing_cits = set(x.get("source") for x in p["citations"])
        for src in S[code]:
            if src["citation"] not in existing_srcs:
                p["sources"].append({
                    "citation": src["citation"], "title_en": src["title_en"],
                    "title_fa": src["title_fa"], "year": src["year"], "doi": src.get("doi"),
                    "url": src.get("url"), "language": src["language"], "verified": src["verified"],
                })
            if src["citation"] not in existing_cits:
                p["citations"].append({
                    "source": src["citation"], "locator": src["locator"],
                    "supports": src["supports"], "verified": src["verified"],
                })
        cur.execute("SELECT COUNT(*) FROM kb_relations WHERE source_id=%s OR target_id=%s", (eid, eid))
        n_rel = cur.fetchone()[0]
        n_sources = len(p["sources"])
        n_verified = sum(1 for x in p["citations"] if x.get("verified"))
        score, detail, words = fw.rubric(p, n_verified, n_sources, n_rel)
        p["quality_score"] = score
        p["quality_assessment"] = "ارزیابی خودکار SPEC §6.1: %d/100 (نمره پایه؛ نیازمند بازبینی علمی انسانی)" % score
        p["status_scientific_note"] = "مستندسازی با منابع تأییدشده شبکه‌ای؛ نمره بر پایه سنجه خودکار است و جانشین داوری علمی (SPEC §6.4) نیست."
        p["updated_at"] = NOW
        p["updated_by"] = STAMP
        cur.execute("UPDATE kb_entities SET properties=%s, version=version+1, updated_at=%s WHERE id=%s",
                    (json.dumps(p, ensure_ascii=False), NOW, eid))
        cur.execute("SELECT version FROM kb_entities WHERE id=%s", (eid,))
        new_version = cur.fetchone()[0]
        for src in S[code]:
            sid = fw.ensure_source(cur, src)
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
                     "full concept documentation (SPEC §4.3) + verified sources", STAMP, NOW))
        cur.execute("""INSERT INTO kb_audit_log (entity_code,action,detail,source,created_at)
            VALUES (%s,'DOC_ENRICH',%s,%s,%s)""",
                    (code, json.dumps({"batch": 331, "score": score, "words": words,
                                       "sources": n_sources, "verified": n_verified,
                                       "relations": n_rel, "rubric": detail}, ensure_ascii=False), STAMP, NOW))
        print(code, "words", words, "score", score, "detail", detail)
    conn.commit()
    conn.close()
    print("BATCH331 DONE")


if __name__ == "__main__":
    main()
