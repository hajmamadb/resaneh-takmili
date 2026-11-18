# -*- coding: utf-8 -*-
"""Batch 203: MC-653, MC-660, MC-461, MC-363, MC-572 (FRAMEWORK)."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch203-20261117"
NOW = "2026-11-17 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch203.json"

S = {
    "MC-653": [
        dict(kind="BOOK",
             title_en="The Processes of Technological Innovation",
             title_fa="فرایندهای نوآوری فناورانه",
             authors="Louis G. Tornatzky; Mitchell Fleischer", year=1990,
             publisher="Lexington Books",
             doi=None,
             url=None,
             language="en", isbn=None,
             citation="Tornatzky, L. G., & Fleischer, M. (1990). The Processes of Technological Innovation. Lexington, MA: Lexington Books.",
             locator="ch. 3",
             locator_type="CHAPTER",
             supports="technology, organization and environment contexts of firm-level innovation adoption",
             verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Electronic Data Interchange and Small Organizations: Adoption and Impact of Technology",
             title_fa="تبادل الکترونیکی داده و سازمان‌های کوچک: پذیرش و اثر فناوری",
             authors="Charalambos L. Iacovou; Izak Benbasat; Albert S. Dexter", year=1995,
             publisher="MIS Quarterly",
             doi="10.2307/249629",
             url="https://misq.umn.edu/misq/article/19/4/465/1173/Electronic-Data-Interchange-and-Small",
             language="en", isbn=None,
             citation="Iacovou, C. L., Benbasat, I., & Dexter, A. S. (1995). Electronic data interchange and small organizations: Adoption and impact of technology. MIS Quarterly, 19(4), 465-485. https://doi.org/10.2307/249629",
             locator="19(4), 465-485",
             locator_type="PAGE",
             supports="perceived benefits, organizational readiness and external pressure as adoption drivers",
             verified=True),
    ],
    "MC-660": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Strength of Weak Ties",
             title_fa="قدرت پیوندهای ضعیف",
             authors="Mark S. Granovetter", year=1973,
             publisher="American Journal of Sociology",
             doi=None,
             url="https://www.jstor.org/stable/2776392",
             language="en", isbn=None,
             citation="Granovetter, M. S. (1973). The strength of weak ties. American Journal of Sociology, 78(6), 1360-1380.",
             locator="78(6), 1360-1380",
             locator_type="PAGE",
             supports="transitivity of strong ties and bridging role of weak ties",
             verified=True),
        dict(kind="BOOK",
             title_en="Soziologie: Untersuchungen über die Formen der Vergesellschaftung",
             title_fa="جامعه‌شناسی: پژوهش در صورت‌های اجتماعی‌شدن",
             authors="Georg Simmel", year=1908,
             publisher="Duncker & Humblot",
             doi=None,
             url="https://archive.org/details/soziologieunters00simmrich",
             language="de", isbn=None,
             citation="Simmel, G. (1908). Soziologie: Untersuchungen über die Formen der Vergesellschaftung. Leipzig: Duncker & Humblot.",
             locator="chapter on the triad",
             locator_type="CHAPTER",
             supports="the triad as the minimal social form and formal analysis of group relations",
             verified=True),
    ],
    "MC-461": [
        dict(kind="BOOK",
             title_en="Orientalism",
             title_fa="شرق‌شناسی",
             authors="Edward W. Said", year=1978,
             publisher="Pantheon Books",
             doi=None,
             url=None,
             language="en", isbn=None,
             citation="Said, E. W. (1978). Orientalism. New York: Pantheon Books.",
             locator="book",
             locator_type="BOOK",
             supports="three senses of Orientalism and its discursive reproduction",
             verified=True),
        dict(kind="BOOK",
             title_en="Culture and Imperialism",
             title_fa="فرهنگ و امپریالیسم",
             authors="Edward W. Said", year=1993,
             publisher="Alfred A. Knopf",
             doi=None,
             url="https://monoskop.org/images/f/f9/Said_Edward_Culture_and_Imperialism.pdf",
             language="en", isbn=None,
             citation="Said, E. W. (1993). Culture and Imperialism. New York: Alfred A. Knopf.",
             locator="book",
             locator_type="BOOK",
             supports="imperial structures in culture and narratives of resistance",
             verified=True),
    ],
    "MC-363": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Cascading Activation: Contesting the White House's Frame After 9/11",
             title_fa="فعال‌سازی آبشاری: نبرد بر سر چارچوب کاخ سفید پس از ۱۱ سپتامبر",
             authors="Robert M. Entman", year=2003,
             publisher="Political Communication",
             doi=None,
             url="https://www.tandfonline.com/doi/abs/10.1080/10584600390244176",
             language="en", isbn=None,
             citation="Entman, R. M. (2003). Cascading activation: Contesting the White House's frame after 9/11. Political Communication, 20(4), 415-432.",
             locator="20(4), 415-432",
             locator_type="PAGE",
             supports="cascading flow of frames across administration, elites, media and public",
             verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Framing: Toward Clarification of a Fractured Paradigm",
             title_fa="چارچوب‌بندی: به‌سوی روشن‌سازی یک پارادایم پراکنده",
             authors="Robert M. Entman", year=1993,
             publisher="Journal of Communication",
             doi="10.1111/j.1460-2466.1993.tb01304.x",
             url="https://academic.oup.com/joc/article-abstract/43/4/51/4160153",
             language="en", isbn=None,
             citation="Entman, R. M. (1993). Framing: Toward clarification of a fractured paradigm. Journal of Communication, 43(4), 51-58. https://doi.org/10.1111/j.1460-2466.1993.tb01304.x",
             locator="43(4), 51-58",
             locator_type="PAGE",
             supports="selection and salience as the core framing operations",
             verified=True),
    ],
    "MC-572": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Transtheoretical Therapy: Toward a More Integrative Model of Change",
             title_fa="درمان فرانظری: به‌سوی مدلی یکپارچه‌تر از تغییر",
             authors="James O. Prochaska; Carlo C. DiClemente", year=1982,
             publisher="Psychotherapy: Theory, Research & Practice",
             doi=None,
             url=None,
             language="en", isbn=None,
             citation="Prochaska, J. O., & DiClemente, C. C. (1982). Transtheoretical therapy: Toward a more integrative model of change. Psychotherapy: Theory, Research & Practice, 19(3), 276-288.",
             locator="19(3), 276-288",
             locator_type="PAGE",
             supports="stages and processes of change across therapy systems",
             verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="In Search of How People Change: Applications to Addictive Behaviors",
             title_fa="در جست‌وجوی چگونگی تغییر افراد: کاربردها در رفتارهای اعتیادی",
             authors="James O. Prochaska; Carlo C. DiClemente; John C. Norcross", year=1992,
             publisher="American Psychologist",
             doi=None,
             url="https://pubmed.ncbi.nlm.nih.gov/1329589/",
             language="en", isbn=None,
             citation="Prochaska, J. O., DiClemente, C. C., & Norcross, J. C. (1992). In search of how people change: Applications to addictive behaviors. American Psychologist, 47(9), 1102-1114.",
             locator="47(9), 1102-1114",
             locator_type="PAGE",
             supports="stage-matched interventions and relapse as part of the change cycle",
             verified=True),
    ],
}

ENRICH = {
    "MC-653": dict(
        needs_enrichment=False,
        title_fa="چارچوب فناوری، سازمان و محیط",
        level="سازمانی",
        constructs=("• زمینهٔ فناوری: مزیت نسبی، سازگاری و پیچیدگی ادراک‌شدهٔ نوآوری.\n"
                    "• زمینهٔ سازمانی: اندازه، منابع مالی و انسانی، ساختار و آمادگی سازمان.\n"
                    "• زمینهٔ محیطی: فشار رقابتی، شرکای تجاری، مقررات و زیرساخت صنعت."),
        core_logic="پذیرش نوآوری در بنگاه تنها تابع ویژگی فناوری نیست؛ سه زمینهٔ فناوری، سازمان و محیط هم‌زمان تصمیم پذیرش را قید می‌زنند و همین تعامل توضیح می‌دهد که چرا بنگاه‌های مشابه فناوری یکسان را با سرعت‌های متفاوت می‌پذیرند.",
        detailed_analysis=("۱. بنیان و منطق نظری\nچارچوب فناوری، سازمان و محیط در کتاب تورناتزکی و فلیشر (۱۹۹۰) صورت‌بندی شد و پذیرش نوآوری را در سطح بنگاه تحلیل می‌کند. "
                           "زمینهٔ فناوری به ویژگی‌های ادراک‌شدهٔ نوآوری می‌پردازد: مزیت نسبی، سازگاری با رویه‌های موجود و پیچیدگی. "
                           "زمینهٔ سازمانی به آمادگی درونی بنگاه، از اندازه و منابع تا ساختار ارتباطی و حمایت مدیریت ارشد، مربوط است. "
                           "زمینهٔ محیطی فشارهای بیرونی مانند رقابت، الزام شرکای تجاری و مقررات را در بر می‌گیرد. "
                           "ایاکوو، بن‌باسات و دکستر (۱۹۹۵) این منطق را در مطالعهٔ پذیرش تبادل الکترونیکی داده در سازمان‌های کوچک به‌کار بردند و نشان دادند سود ادراک‌شده، آمادگی سازمانی و فشار بیرونی سه پیش‌بین اصلی‌اند.\n\n"
                           "۲. کاربرد و نقد\nاین چارچوب در پژوهش پذیرش سامانه‌های تحریریه، ابزارهای تحلیلی و خودکارسازی خبر پرکاربرد است، زیرا پذیرش فناوری در رسانه را نه تصمیمی فردی، بلکه پیامد هم‌زمانی فشار بازار، ظرفیت سازمان و ویژگی ابزار می‌بیند. "
                           "نقد اصلی، ایستا بودن مدل و کم‌رنگ دیدن یادگیری سازمانی و نقش کنشگران فردی است؛ از این رو پژوهش‌های تازه آن را با رویکردهای پویا و نهادی ترکیب می‌کنند."),
        related_approaches="پذیرش فناوری در سازمان؛ انتشار نوآوری؛ ظرفیت جذب؛ نظام‌های اطلاعاتی؛ تحول دیجیتال رسانه.",
        recommended_sources="«فرایندهای نوآوری فناورانه» (تورناتزکی و فلیشر، ۱۹۹۰)؛ «تبادل الکترونیکی داده و سازمان‌های کوچک» (ایاکوو، بن‌باسات و دکستر، ۱۹۹۵)؛ «انتشار نوآوری» (راجرز، ۲۰۰۳).",
    ),
    "MC-660": dict(
        needs_enrichment=False,
        constructs=("• ساختار شبکه: الگوی روابط میان گره‌ها که رفتار و دسترسی به منابع را شکل می‌دهد.\n"
                    "• بستار سه‌گانه: گرایش به برقراری پیوند میان دو گره دارای همسایهٔ مشترک.\n"
                    "• تراگذری: نسبت مثلث‌های بسته به مسیرهای سه‌گانه.\n"
                    "• پیوند ضعیف و پل ساختاری: پیوندهایی که خوشه‌های جدا را به هم متصل می‌کنند."),
        core_logic="اگر دو گره با یک گرهٔ سوم پیوند داشته باشند، احتمال پیوند میان آن دو بالا می‌رود؛ این سازوکار ساده، خوشه‌شدگی، اعتماد درون‌گروهی و در همان حال شکاف میان خوشه‌ها را توضیح می‌دهد و نشان می‌دهد ساختار پیوندها مستقل از محتوای ارتباط، پیامد اجتماعی دارد.",
        detailed_analysis=("۱. بنیان و منطق نظری\nبستار سه‌گانه ریشه در صورت‌گرایی زیمل (۱۹۰۸) دارد که سه‌گانه را واحد کمینهٔ جامعه‌شناسی دانست. "
                           "در تحلیل شبکهٔ اجتماعی، این مفهوم به گرایش شبکه برای بستن مثلث میان گره‌های دارای همسایهٔ مشترک اشاره می‌کند و با سنجه‌هایی مانند ضریب خوشه‌بندی و تراگذری اندازه‌گیری می‌شود. "
                           "گرانووتر (۱۹۷۳) نشان داد پیوندهای قوی گرایش به بستن مثلث دارند، در حالی که پیوندهای ضعیف نقش پل میان خوشه‌ها را بازی می‌کنند و دسترسی به اطلاعات تازه را ممکن می‌سازند. "
                           "به این ترتیب، بستار هم منبع اعتماد و هم منبع انسداد اطلاعاتی است.\n\n"
                           "۲. کاربرد و نقد\nدر پژوهش رسانه، بستار سه‌گانه برای تحلیل خوشه‌های مخاطب، انتشار خبر و شکل‌گیری حباب‌های اطلاعاتی به‌کار می‌رود. "
                           "نقد اصلی، ایستا و مقطعی بودن سنجه‌ها و نادیده‌گرفتن محتوا، کیفیت و تاریخ پیوندهاست؛ شبکه‌های آنلاین نیز با پیوندهای ضعیف و الگوریتمی، منطق کلاسیک بستار را تغییر داده‌اند و پژوهش تازه باید این تفاوت را لحاظ کند."),
        related_approaches="تحلیل شبکهٔ اجتماعی؛ سرمایهٔ اجتماعی؛ پیوندهای ضعیف؛ حفره‌های ساختاری؛ شبکه‌های پیچیده.",
        recommended_sources="«قدرت پیوندهای ضعیف» (گرانووتر، ۱۹۷۳)؛ «جامعه‌شناسی» (زیمل، ۱۹۰۸)؛ «حفره‌های ساختاری» (بورت، ۱۹۹۲).",
    ),
    "MC-461": dict(
        needs_enrichment=False,
        level="کلان",
        key_concepts=["شرق‌شناسی", "دیگری‌سازی", "هژمونی", "گفتمان استعماری", "شرق‌شناسی نهفته و آشکار"],
        principles=["دیگری‌سازی، پیش‌شرط توجیه سلطه است.", "شرق‌شناسی نهفته، لایهٔ پایدار پیش‌داوری‌ها را حفظ می‌کند.",
                    "بازنمایی، کنشی سیاسی است، نه بازتاب واقعیت.", "دانش تخصصی می‌تواند ابزار سلطه شود.",
                    "مقاومت در روایت‌های بومی و پسااستعماری شکل می‌گیرد.", "نقد پسااستعماری باید از تعمیم یکپارچهٔ غرب بپرهیزد.",
                    "بازنمایی رسانه‌ای، میراث گفتمان استعماری را بازتولید یا به چالش می‌کشد."],
        constructs=("• شرق‌شناسی: گفتمان دانشی و هنری که شرق را به‌عنوان دیگری بازنمایی می‌کند.\n"
                    "• دیگری‌سازی: فرایند تعریف هویت خود از راه تمایز از دیگری.\n"
                    "• هژمونی: رهبری فرهنگی که سلطه را طبیعی می‌کند.\n"
                    "• گفتمان استعماری: مجموعهٔ نشانه‌ها و گزاره‌هایی که برتری غرب را بدیهی می‌سازد.\n"
                    "• شرق‌شناسی نهفته و آشکار: لایهٔ پایدار پیش‌داوری و بیان صریح آن."),
        core_logic="بازنمایی «دیگری» در گفتمان استعماری، کنشی سیاسی است: با تکرار نشانه‌های ثابت دربارهٔ شرق، برتری غرب طبیعی می‌شود و سلطه نه با زور، بلکه با دانش و تصویر مشروعیت می‌یابد.",
        detailed_analysis=("۱. بنیان و منطق نظری\nادوارد سعید در شرق‌شناسی (۱۹۷۸) نشان داد شرق‌شناسی فقط مجموعه‌ای از باورها نیست، بلکه گفتمانی نهادی است که با دانش تخصصی، ادبیات و رسانه، شرق را به‌عنوان دیگری غیرمنطقی و نیازمند هدایت بازنمایی می‌کند. "
                           "او سه معنای پیوسته را از هم جدا کرد: سنت دانشگاهی مطالعهٔ شرق، سبک اندیشیدن مبتنی بر تمایز هستی‌شناختی شرق و غرب، و سازوکار نهادی سلطهٔ غرب بر شرق. "
                           "در فرهنگ و امپریالیسم (۱۹۹۳) این نقد را به فرم‌های فرهنگی و روایت‌های مقاومت گسترش داد و نشان داد امپراتوری در رمان، اپرا و رسانه نیز حضور دارد. "
                           "مفهوم هژمونی گرامشی توضیح می‌دهد که چگونه این تصویر بدون اجبار آشکار پذیرفته می‌شود.\n\n"
                           "۲. کاربرد و نقد\nدر پژوهش رسانه، این چارچوب برای تحلیل بازنمایی اسلام، مهاجران و جنوب جهانی به‌کار می‌رود و نشان می‌دهد که کلیشه‌های خبری، میراث گفتمان استعماری‌اند. "
                           "نقد اصلی، تعمیم یکپارچهٔ غرب، کم‌توجهی به عاملیت جوامع شرقی و خطر تقلیل همهٔ بازنمایی‌ها به سلطه است؛ پژوهش پسااستعماری متأخر بر مقاومت، ترکیب و بازنمایی متقابل تأکید می‌کند."),
        related_approaches="مطالعات پسااستعماری؛ مطالعات فرهنگی؛ تحلیل گفتمان انتقادی؛ بازنمایی رسانه‌ای؛ امپریالیسم فرهنگی.",
        recommended_sources="«شرق‌شناسی» (سعید، ۱۹۷۸)؛ «فرهنگ و امپریالیسم» (سعید، ۱۹۹۳)؛ «بازنمایی: نشانه‌ها، معنا و فرهنگ» (هال، ۱۹۹۷).",
    ),
    "MC-363": dict(
        needs_enrichment=False,
        key_concepts=["چارچوب تفسیری", "آبشار چارچوب", "نخبگان غیردولتی", "هم‌خوانی فرهنگی", "بازخورد پایین به بالا"],
        constructs=("• فعال‌سازی چارچوب: برجسته‌سازی برخی جنبه‌های رویداد در ذهن مخاطب.\n"
                    "• آبشار: جریان چارچوب از دولت به نخبگان، رسانه و عموم.\n"
                    "• هم‌خوانی فرهنگی: تناسب چارچوب با ارزش‌های رایج جامعه.\n"
                    "• بازخورد: تأثیر ادراک عمومی بر چارچوب نخبگان و رسانه."),
        core_logic="چارچوب‌ها از بالا به پایین جریان می‌یابند، اما این جریان بی‌قید نیست: انسجام و تکرار پیام دولتی، هم‌خوانی فرهنگی و ضعف چارچوب‌های بدیل تعیین می‌کند که چارچوب غالب تا کجا نفوذ کند؛ بازخورد عمومی می‌تواند آبشار را کند یا منحرف کند.",
        detailed_analysis=("۱. بنیان و منطق نظری\nمدل فعال‌سازی آبشاری انتمن (۲۰۰۳) نشان می‌دهد چارچوب‌ها در سطوح نظام سیاسی جریان می‌یابند: دولت، نخبگان غیردولتی، رسانه و افکار عمومی. "
                           "در هر سطح، چارچوب با ارزش‌های خبری، هم‌خوانی فرهنگی و منافع نهادی بازتفسیر می‌شود. "
                           "انتمن با ردیابی پوشش پس از ۱۱ سپتامبر نشان داد چارچوب کاخ سفید با تکرار و انسجام به رسانه‌ها منتقل شد، اما مقاومت رسانه‌ای و بازخورد عمومی می‌تواند این جریان را مختل کند. "
                           "مفهوم گزینش و برجسته‌سازی از مقالهٔ ۱۹۹۳ او می‌آید: چارچوب‌بندی یعنی انتخاب برخی جنبه‌های واقعیت و برجسته‌کردن آن‌ها.\n\n"
                           "۲. کاربرد و نقد\nاین مدل در تحلیل پوشش سیاست خارجی، مدیریت بحران و رقابت روایت‌های دولتی کاربرد دارد و به پژوهشگر کمک می‌کند رد چارچوب را از سند رسمی تا تیتر خبر و نگرش مخاطب دنبال کند. "
                           "نقد اصلی، ساده‌سازی نظام رسانه‌ای و فرض ثابت بودن لایه‌هاست؛ در محیط چندکاناله و شبکه‌های اجتماعی، بازخورد پایین به بالا سریع‌تر و پیچیده‌تر شده و مدل نیازمند بازنگری است."),
        related_approaches="چارچوب‌بندی خبری؛ دروازه‌بانی؛ ارتباطات سیاسی؛ مدیریت بحران؛ نظریهٔ دستور کار.",
        recommended_sources="«فعال‌سازی آبشاری» (انتمن، ۲۰۰۳)؛ «چارچوب‌بندی: روشن‌سازی یک پارادایم پراکنده» (انتمن، ۱۹۹۳)؛ «چارچوب‌بندی به‌عنوان نظریهٔ اثرات رسانه‌ای» (شویفله، ۱۹۹۹).",
    ),
    "MC-572": dict(
        needs_enrichment=False,
        key_concepts=["پیش‌تفکر", "تفکر", "آماده‌سازی", "عمل و حفظ", "تعادل تصمیم", "فرایندهای تغییر"],
        principles=["هر مرحله، فرایند تغییر و پیام مناسب خود را می‌طلبد.", "پیش از عمل، باید تعادل تصمیم به سمت سود تغییر جابه‌جا شود.",
                    "خودکارآمدی، پیش‌بین گذر از مرحلهٔ عمل و حفظ است.", "بازگشت بخشی از چرخهٔ تغییر است، نه شکست نهایی.",
                    "مداخلهٔ هم‌خوان با مرحله، اثر بیشتری از پیام یکسان برای همه دارد.", "سنجش مرحله باید پیش از طراحی کمپین انجام شود."],
        constructs=("• مراحل تغییر: پیش‌تفکر، تفکر، آماده‌سازی، عمل، حفظ و پایان.\n"
                    "• فرایندهای تغییر: راهبردهای شناختی و رفتاری متناسب با هر مرحله.\n"
                    "• تعادل تصمیم: سنجش سود و زیان تغییر.\n"
                    "• خودکارآمدی: اطمینان فرد به توان حفظ رفتار تازه.\n"
                    "• وسوسه و بازگشت: گرایش به بازگشت به رفتار پیشین."),
        core_logic="تغییر رفتار یک رویداد نیست، مسیری مرحله‌ای است؛ فرد در هر مرحله تعادل تصمیم، خودکارآمدی و فرایندهای شناختی-رفتاری متفاوتی دارد و مداخله باید با همان مرحله هم‌خوان باشد تا از مقاومت و بازگشت بکاهد.",
        detailed_analysis=("۱. بنیان و منطق نظری\nچارچوب مراحل تغییر از مدل فرانظری پروچاسکا و دی‌کلمنته (۱۹۸۲) برخاست و در مقالهٔ ۱۹۹۲ برای رفتارهای اعتیادی بسط یافت. "
                           "مدل، تغییر را در مراحل پیش‌تفکر، تفکر، آماده‌سازی، عمل، حفظ و پایان سازمان می‌دهد و برای هر مرحله فرایندهای شناختی و رفتاری خاصی پیش‌بینی می‌کند. "
                           "در مرحلهٔ پیش‌تفکر، فرد مشکل را نمی‌بیند؛ در تفکر، تعادل تصمیم را می‌سنجد؛ در آماده‌سازی، برنامه و تعهد می‌سازد؛ در عمل، رفتار تازه را برقرار می‌کند و در حفظ، در برابر وسوسه مقاومت می‌کند. "
                           "بازگشت بخشی از چرخه است و مداخلهٔ هم‌خوان با مرحله، اثر بیشتری از پیام یکسان برای همه دارد.\n\n"
                           "۲. کاربرد و نقد\nاین چارچوب در کمپین‌های سلامت، ترک اعتیاد و ارتباطات اقناعی به‌کار می‌رود و به طراح پیام می‌آموزد که پیش از تولید محتوا، مرحلهٔ آمادگی مخاطب را بسنجد. "
                           "نقد اصلی، دلبخواهی بودن مرز مراحل، ساده‌سازی حرکت خطی و شواهد ناهمگون دربارهٔ کارایی مداخلات مرحله‌محور است؛ با این حال، تأکید آن بر تناسب پیام با آمادگی مخاطب همچنان در پژوهش تغییر رفتار اثرگذار است."),
        related_approaches="ارتباطات سلامت؛ اقناع و تغییر نگرش؛ بازاریابی اجتماعی؛ مدل باور سلامت؛ طراحی مداخلهٔ رفتاری.",
        recommended_sources="«درمان فرانظری» (پروچاسکا و دی‌کلمنته، ۱۹۸۲)؛ «در جست‌وجوی چگونگی تغییر افراد» (پروچاسکا، دی‌کلمنته و نورکراس، ۱۹۹۲)؛ «مدل فرانظری تغییر رفتار سلامت» (پروچاسکا و ولیسر، ۱۹۹۷).",
    ),
}

NAME_FIX = {}

YEAR_FIX = {
    "MC-653": "year=1990 (Tornatzky & Fleischer 1990); Iacovou et al. 1995 verified (DOI 10.2307/249629); removed contaminated platform-template fields and garbled recommendations",
    "MC-660": "year=1908 (Simmel 1908 origin); Granovetter 1973 verified; removed contaminated constructs/analysis and repaired recommendations",
    "MC-461": "year=1978 (Said 1978); Said 1993 verified; removed Latin glosses in key_concepts, contaminated constructs and irrelevant recommendations",
    "MC-363": "year=2003 (Entman 2003); Entman 1993 verified (DOI 10.1111/j.1460-2466.1993.tb01304.x); removed Latin glosses and gatekeeping-template fields",
    "MC-572": "year=1982 (Prochaska & DiClemente 1982); 1992 article verified; removed Latin glosses and persuasion-template fields",
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
                                       "verified": n_verified, "batch": 203}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH203 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
