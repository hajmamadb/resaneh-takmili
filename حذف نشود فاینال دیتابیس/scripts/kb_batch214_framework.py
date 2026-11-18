# -*- coding: utf-8 -*-
"""Batch 214: MC-368, MC-421, MC-489, MC-541, MC-542."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch214-20261117"
NOW = "2026-11-17 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch214.json"

S = {
    "MC-368": [
        dict(kind="BOOK",
             title_en="Courtier to the Crowd: The Story of Ivy Lee and the Development of Public Relations",
             title_fa="درباری میان مردم: داستان آیوی لی و شکل‌گیری روابط عمومی",
             authors="Ray Eldon Hiebert", year=1966,
             publisher="Iowa State University Press",
             doi=None,
             url="https://www.ebsco.com/research-starters/history/lee-establishes-field-public-relations/",
             language="en", isbn=None,
             citation="Hiebert, R. E. (1966). Courtier to the Crowd: The Story of Ivy Lee and the Development of Public Relations. Ames: Iowa State University Press.",
             locator="book",
             locator_type="BOOK",
             supports="Ivy Lee's 1906 declaration of principles and public information practice",
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
             locator="ch. 2",
             locator_type="CHAPTER",
             supports="public information as the second of four historical models",
             verified=True),
    ],
    "MC-421": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Robotic Reporter: Automated Journalism and the Redefinition of Labor, Compositional Forms, and Journalistic Authority",
             title_fa="خبرنگار رباتیک: روزنامه‌نگاری خودکار و بازتعریف کار، شکل‌های نگارش و اقتدار روزنامه‌نگاری",
             authors="Matt Carlson", year=2015,
             publisher="Digital Journalism",
             doi="10.1080/21670811.2014.976412",
             url="https://www.tandfonline.com/doi/abs/10.1080/21670811.2014.976412",
             language="en", isbn=None,
             citation="Carlson, M. (2015). The robotic reporter: Automated journalism and the redefinition of labor, compositional forms, and journalistic authority. Digital Journalism, 3(3), 416-431. https://doi.org/10.1080/21670811.2014.976412",
             locator="3(3), 416-431",
             locator_type="PAGE",
             supports="automated journalism reshapes labor, form and authority",
             verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Automated Journalism 2.0: Event-Driven Narratives",
             title_fa="روزنامه‌نگاری خودکار ۲.۰: روایت‌های رویدادمحور",
             authors="David Caswell; Konstantin Dörr", year=2018,
             publisher="Journalism Practice",
             doi=None,
             url="https://www.tandfonline.com/doi/full/10.1080/17512786.2017.1320773",
             language="en", isbn=None,
             citation="Caswell, D., & Dörr, K. (2018). Automated journalism 2.0: Event-driven narratives. Journalism Practice, 12(4), 477-496.",
             locator="12(4), 477-496",
             locator_type="PAGE",
             supports="second generation of automated journalism beyond template filling",
             verified=True),
    ],
    "MC-489": [
        dict(kind="BOOK",
             title_en="Comparing Media Systems: Three Models of Media and Politics",
             title_fa="مقایسهٔ نظام‌های رسانه‌ای: سه مدل رسانه و سیاست",
             authors="Daniel C. Hallin; Paolo Mancini", year=2004,
             publisher="Cambridge University Press",
             doi="10.1017/CBO9780511790867",
             url="https://www.cambridge.org/core/books/comparing-media-systems/B7A12371782B7A1D62BA1A72C1395E43",
             language="en", isbn=None,
             citation="Hallin, D. C., & Mancini, P. (2004). Comparing Media Systems: Three Models of Media and Politics. Cambridge: Cambridge University Press.",
             locator="book",
             locator_type="BOOK",
             supports="four dimensions and three models of media systems",
             verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Ten Years After Comparing Media Systems: What Have We Learned?",
             title_fa="ده سال پس از مقایسهٔ نظام‌های رسانه‌ای: چه آموخته‌ایم؟",
             authors="Daniel C. Hallin; Paolo Mancini", year=2017,
             publisher="Political Communication",
             doi=None,
             url="https://www.tandfonline.com/doi/full/10.1080/10584609.2017.1310317",
             language="en", isbn=None,
             citation="Hallin, D. C., & Mancini, P. (2017). Ten years after Comparing Media Systems: What have we learned? Political Communication, 34(2), 155-171.",
             locator="34(2), 155-171",
             locator_type="PAGE",
             supports="reassessment of the three-model framework",
             verified=True),
    ],
    "MC-541": [
        dict(kind="BOOK_CHAPTER",
             title_en="Mass Communication and the Social System",
             title_fa="ارتباط جمعی و نظام اجتماعی",
             authors="John W. Riley Jr.; Matilda White Riley", year=1959,
             publisher="Basic Books",
             doi=None,
             url="https://communicationtheory.org/riley-riley-model-of-communication/",
             language="en", isbn=None,
             citation="Riley, J. W., Jr., & Riley, M. W. (1959). Mass communication and the social system. In R. K. Merton, L. Broom, & L. S. Cottrell Jr. (Eds.), Sociology Today (pp. 537-578). New York: Basic Books.",
             locator="pp. 537-578",
             locator_type="PAGE",
             supports="sociological model embedding communication in social structure and primary groups",
             verified=True),
        dict(kind="BOOK",
             title_en="Mass Communication: A Sociological Perspective",
             title_fa="ارتباط جمعی: چشم‌اندازی جامعه‌شناختی",
             authors="Charles R. Wright", year=1986,
             publisher="Random House",
             doi=None,
             url="https://archive.org/details/masscommunicatio0000char",
             language="en", isbn=None,
             citation="Wright, C. R. (1986). Mass Communication: A Sociological Perspective (3rd ed.). New York: Random House.",
             locator="3rd ed.",
             locator_type="BOOK",
             supports="sociological framing of mass communication that situates the Riley model",
             verified=True),
    ],
    "MC-542": [
        dict(kind="BOOK_CHAPTER",
             title_en="Closing Statement: Linguistics and Poetics",
             title_fa="سخن پایانی: زبان‌شناسی و شعرشناسی",
             authors="Roman Jakobson", year=1960,
             publisher="MIT Press",
             doi=None,
             url="https://monoskop.org/images/8/84/Jakobson_Roman_1960_Closing_statement_Linguistics_and_Poetics.pdf",
             language="en", isbn=None,
             citation="Jakobson, R. (1960). Closing statement: Linguistics and poetics. In T. A. Sebeok (Ed.), Style in Language (pp. 350-377). Cambridge, MA: MIT Press.",
             locator="pp. 350-377",
             locator_type="PAGE",
             supports="six factors and six functions of verbal communication",
             verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="What Is the Proper Function of Language?",
             title_fa="کارکرد مناسب زبان چیست؟",
             authors="Eliot Michaelson", year=2024,
             publisher="Inquiry",
             doi="10.1080/0020174X.2024.2325616",
             url="https://doi.org/10.1080/0020174X.2024.2325616",
             language="en", isbn=None,
             citation="Michaelson, E. (2024). What is the proper function of language? Inquiry. https://doi.org/10.1080/0020174X.2024.2325616",
             locator="67(8), 2791-2814",
             locator_type="PAGE",
             supports="critical discussion of language functions",
             verified=True),
    ],
}

ENRICH = {
    "MC-368": dict(
        needs_enrichment=False,
        level="پایه",
        related_approaches="مدل‌های چهارگانهٔ روابط عمومی؛ تبلیغ‌گری مطبوعاتی؛ شفافیت سازمانی؛ اخلاق ارتباطات.",
        recommended_sources="«درباری میان مردم: داستان آیوی لی» (هیبرت، ۱۹۶۶)؛ «مدیریت روابط عمومی» (گرونیگ و هانت، ۱۹۸۴)؛ «روابط عمومی مؤثر» (کاتلیپ و همکاران).",
        detailed_analysis=("۱. بنیان و منطق نظری\nمدل انتشار صادقانه اطلاعات با آیوی لی و اعلامیهٔ اصول او در ۱۹۰۶ پیوند دارد. لی وعده داد اطلاعات درست و به‌موقع در اختیار رسانه و عموم گذاشته شود و برای این کار دفتر مطبوعاتی و اعلامیهٔ خبری را نهادینه کرد. "
                           "گرونیگ و هانت (۱۹۸۴) این الگو را دومین مدل تاریخی روابط عمومی نامیدند: هنوز یک‌سویه است، اما برخلاف تبلیغ‌گری مطبوعاتی، حقیقت‌محور است.\n\n"
                           "۲. ساختارهای مفهومی\nانتشار صادقانه، یک‌سویگی، شفافیت، دسترسی رسانه و اعتماد عمومی سازه‌های اصلی‌اند. "
                           "مدل، پژوهش مخاطب و بازخورد نظام‌مند را در بر نمی‌گیرد.\n\n"
                           "۳. نمونه‌های تحلیلی\nبیانیهٔ اصول لی پس از سانحهٔ راه‌آهن، نمونهٔ تاریخی گذار از پنهان‌کاری به انتشار اطلاعات درست است؛ در عمل امروز، انتشار منظم گزارش‌های شفافیت سازمانی همان منطق را دنبال می‌کند.\n\n"
                           "۴. نقدها و چالش‌ها\nمدل یک‌سویه است و به دیدگاه مخاطب گوش نمی‌دهد؛ فرض می‌کند انتشار حقیقت به‌تنهایی اعتماد می‌سازد؛ پژوهش مخاطب را جدی نمی‌گیرد؛ و در بحران‌هایی که نیاز به مذاکره و پاسخ‌گویی دوسویه است، ناکافی می‌ماند.\n\n"
                           "۵. سیر تاریخی\nاعلامیهٔ ۱۹۰۶ نقطهٔ عطف حرفه‌ای‌شدن روابط عمومی بود، در سدهٔ بیستم با مدل‌های دوسویه تکمیل شد و در گونه‌شناسی گرونیگ و هانت جایگاه تاریخی یافت.\n\n"
                           "۶. جایگاه در بحث روز\nدر گفتمان شفافیت سازمانی و مسئولیت اجتماعی، مدل انتشار صادقانه همچنان حداقل اخلاقی ارتباط سازمان است، هرچند برای گفت‌وگوی واقعی کافی نیست."),
    ),
    "MC-421": dict(
        needs_enrichment=False,
        level="میان",
        related_approaches="روزنامه‌نگاری داده‌محور؛ خودکارسازی خبر؛ هوش مصنوعی مولد؛ دروازه‌بانی الگوریتمی؛ اخلاق روزنامه‌نگاری.",
        recommended_sources="«خبرنگار رباتیک» (کارلسون، ۲۰۱۵)؛ «روزنامه‌نگاری خودکار ۲.۰» (کاسول و دور، ۲۰۱۸)؛ «روزنامه‌نگاری و هوش مصنوعی» (دیاکوپولوس، ۲۰۱۹).",
        detailed_analysis=("۱. بنیان و منطق نظری\nکارلسون (۲۰۱۵) با مطالعهٔ شرکت نریتیو ساینس و واکنش روزنامه‌نگاران نشان داد روزنامه‌نگاری خودکار سه چیز را بازتعریف می‌کند: تقسیم کار انسانی و ماشینی، شکل‌های نگارش خبر و اقتدار حرفه‌ای روزنامه‌نگار. "
                           "کاسول و دور (۲۰۱۸) نسل دوم این حوزه را با روایت‌های رویدادمحور توصیف کردند که از پرکردن قالب فراتر می‌رود و روایت را از دادهٔ ساختاریافته می‌سازد.\n\n"
                           "۲. ساختارهای مفهومی\nتولید الگوریتمی، دادهٔ ساختاریافته، قالب روایی، اقتدار حرفه‌ای و تقسیم کار سازه‌های اصلی‌اند.\n\n"
                           "۳. نمونه‌های تحلیلی\nگزارش‌های خودکار ورزشی و مالی، نمونهٔ رایج نسل نخست‌اند؛ با مدل‌های زبانی بزرگ، تولید پیش‌نویس خبر و خلاصه‌سازی به نسل تازه‌ای رسیده است که پرسش از صحت و مسئولیت را جدی‌تر می‌کند.\n\n"
                           "۴. نقدها و چالش‌ها\nسوگیری دادهٔ ورودی به خروجی منتقل می‌شود؛ شفافیت الگوریتم و قابلیت بازبینی محدود است؛ مسئولیت خطا مبهم می‌ماند؛ تنوع صداهای خبری کاهش می‌یابد؛ و اعتماد مخاطب به برچسب خودکار بودن محتوا حساس است.\n\n"
                           "۵. سیر تاریخی\nدههٔ ۲۰۱۰ با سامانه‌های گزارش‌نویسی خودکار آغاز شد، پژوهش‌های ۲۰۱۵ به بعد ابعاد کار و اقتدار را تحلیل کردند و نسل دوم در ۲۰۱۸ با روایت رویدادمحور و سپس مدل‌های زبانی بزرگ گسترش یافت.\n\n"
                           "۶. جایگاه در بحث روز\nبا فراگیرشدن هوش مصنوعی مولد، پرسش از برچسب‌گذاری، راستی‌آزمایی و مرز کار خبرنگار انسانی به محور سیاست رسانه‌ای تبدیل شده است."),
    ),
    "MC-489": dict(
        needs_enrichment=False,
        level="کلان",
        related_approaches="اقتصاد سیاسی رسانه؛ حرفه‌ای‌گرایی روزنامه‌نگاری؛ هم‌راستایی سیاسی؛ نظام‌های رسانه‌ای تطبیقی.",
        recommended_sources="«مقایسهٔ نظام‌های رسانه‌ای» (هالین و مانچینی، ۲۰۰۴)؛ «ده سال پس از مقایسهٔ نظام‌های رسانه‌ای» (هالین و مانچینی، ۲۰۱۷)؛ پژوهش‌های تطبیقی نظام رسانه و سیاست.",
        detailed_analysis=("۱. بنیان و منطق نظری\nهالین و مانچینی (۲۰۰۴) نظام‌های رسانه‌ای را در چهار بُعد مقایسه کردند: ساختار بازار رسانه، هم‌راستایی سیاسی، حرفه‌ای‌گرایی روزنامه‌نگاری و نقش دولت. "
                           "از ترکیب این ابعاد سه مدل برآمد: کثرت‌گرای قطبی، دموکراتیک-شرکتی و لیبرال. مدل، روزنامه‌نگاری را نه پدیده‌ای مستقل، بلکه درون تاریخ سیاسی و اقتصادی هر کشور تحلیل می‌کند.\n\n"
                           "۲. ساختارهای مفهومی\nچهار بُعد نظام رسانه و سه مدل، سازه‌های اصلی‌اند. "
                           "حرفه‌ای‌گرایی شامل استقلال، هنجارهای مشترک و جهت‌گیری خدمت عمومی است.\n\n"
                           "۳. نمونه‌های تحلیلی\nایتالیا و یونان نمونهٔ کثرت‌گرایی قطبی با پیوند تنگ رسانه و سیاست‌اند؛ آلمان و سوئد نمونهٔ دموکراتیک-شرکتی با حرفه‌ای‌گرایی بالا؛ آمریکا و بریتانیا نمونهٔ لیبرال با بازارمحوری بیشتر.\n\n"
                           "۴. نقدها و چالش‌ها\nچارچوب اروپامحور و غرب‌محور است و نظام‌های جنوب و شرق را کمتر پوشش می‌دهد؛ مرز سه مدل در عمل مبهم است؛ تحول دیجیتال و پلتفرم‌ها ابعاد جدیدی افزوده‌اند؛ و داده‌های تطبیقی در برخی کشورها ناقص است.\n\n"
                           "۵. سیر تاریخی\nکتاب ۲۰۰۴ چارچوب تطبیقی تازه‌ای ساخت، نقدهای دههٔ بعد آن را آزمودند و بازنگری ۲۰۱۷ در مجلهٔ «ارتباطات سیاسی» پاسخ نویسندگان به این نقدها بود.\n\n"
                           "۶. جایگاه در بحث روز\nدر پژوهش‌های همگرایی نظام‌های رسانه‌ای و اثر پلتفرم‌ها، چارچوب هالین و مانچینی همچنان نقطهٔ شروع مقایسهٔ بین‌کشوری است."),
    ),
    "MC-541": dict(
        needs_enrichment=False,
        level="میان",
        related_approaches="جامعه‌شناسی ارتباطات؛ مدل حلقه‌ای شرام؛ دروازه‌بانی خبر؛ نظریهٔ نظام‌های اجتماعی؛ ارتباطات میان‌فردی.",
        recommended_sources="«ارتباط جمعی و نظام اجتماعی» (رایلی و رایلی، ۱۹۵۹)؛ «مدل حلقه‌ای شرام» (شرام، ۱۹۵۴)؛ «جامعه‌شناسی ارتباطات جمعی» (رایت، ۱۹۸۶).",
        detailed_analysis=("۱. بنیان و منطق نظری\nرایلی و رایلی (۱۹۵۹) در فصل «ارتباط جمعی و نظام اجتماعی» استدلال کردند ارتباط جمعی را نمی‌توان زنجیره‌ای خطی از فرستنده به گیرنده دید؛ "
                           "فرستنده و گیرنده هر دو در گروه‌های اولیه و نظام اجتماعی گسترده‌تری جای دارند و پیام از میان این ساختارها می‌گذرد. "
                           "آن‌ها از دیدگاه جامعه‌شناختی خواستند که پژوهش ارتباط جمعی، بافت گروهی و نهادی مخاطب را جدی بگیرد.\n\n"
                           "۲. ساختارهای مفهومی\nنظام اجتماعی، گروه‌های اولیه، جایگاه فرستنده و گیرنده، دروازه‌بانان و بازخورد سازه‌های اصلی‌اند.\n\n"
                           "۳. نمونه‌های تحلیلی\nتفسیر یک خبر در خانواده و میان همسالان می‌تواند معنای دریافتی را دگرگون کند؛ همین سازوکار در گروه‌های پیام‌رسان دیجیتال نیز دیده می‌شود.\n\n"
                           "۴. نقدها و چالش‌ها\nمدل انتزاعی است و متغیرهای آن دشوار اندازه‌گیری می‌شوند؛ قدرت ساختاری را بیشتر توصیف می‌کند تا تبیین؛ برای پژوهش تجربی نیازمند عملیاتی‌سازی است؛ و مرز نظام اجتماعی و گروه اولیه مبهم می‌ماند.\n\n"
                           "۵. سیر تاریخی\nفصل ۱۹۵۹ یکی از متون بنیادین جامعه‌شناسی ارتباطات شد و پژوهش‌های بعدی دربارهٔ گروه‌های اولیه و دروازه‌بانی بر آن تکیه کردند.\n\n"
                           "۶. جایگاه در بحث روز\nدر تحلیل گروه‌های خانوادگی و شبکه‌های پیام‌رسان، تأکید رایلی و رایلی بر بافت اجتماعی تفسیر همچنان راهگشاست."),
    ),
    "MC-542": dict(
        needs_enrichment=False,
        level="میان",
        related_approaches="نشانه‌شناسی سه‌گانه پیرس؛ مدل ارگانون بولر؛ تحلیل گفتمان؛ شعرشناسی؛ نظریهٔ ارتباطات کلامی.",
        recommended_sources="«سخن پایانی: زبان‌شناسی و شعرشناسی» (یاکوبسون، ۱۹۶۰)؛ «مدل ارگانون بولر» (بولر، ۱۹۳۴)؛ «نشانه‌شناسی: مبانی» (چندلر، ۲۰۰۲).",
        detailed_analysis=("۱. بنیان و منطق نظری\nیاکوبسون (۱۹۶۰) در سخن پایانی کنفرانس «سبک در زبان»، ارتباط کلامی را بر پایهٔ شش عامل صورت‌بندی کرد: فرستنده، گیرنده، زمینه، پیام، تماس و رمزگان. "
                           "هر عامل با یک کارکرد زبان پیوند دارد: عاطفی، ترغیبی، ارجاعی، شعری، تماسی و فرازبانی. "
                           "این چارچوب، مدل سه‌جزئی بولر را گسترش داد و به تحلیل ساختار پیام در ادبیات و رسانه راه یافت.\n\n"
                           "۲. ساختارهای مفهومی\nشش عامل و شش کارکرد، سازه‌های اصلی‌اند. "
                           "کارکرد شعری بر خود پیام، کارکرد ارجاعی بر زمینه و کارکرد ترغیبی بر گیرنده متمرکز است.\n\n"
                           "۳. نمونه‌های تحلیلی\nخبر عمدتاً کارکرد ارجاعی دارد، تبلیغ کارکرد ترغیبی و شعر کارکرد شعری؛ پیام‌های روزمره اغلب ترکیبی از چند کارکردند.\n\n"
                           "۴. نقدها و چالش‌ها\nشش کارکرد سلسله‌مراتب و وزن یکسانی ندارند؛ مدل بر زبان کلامی متمرکز است و رسانه‌های بصری را کم پوشش می‌دهد؛ مرز کارکردها در عمل مبهم است؛ و بافت اجتماعی تولید معنا کمتر تحلیل می‌شود.\n\n"
                           "۵. سیر تاریخی\nسخن ۱۹۶۰ به یکی از متون کلاسیک نشانه‌شناسی و شعرشناسی تبدیل شد و در تحلیل ادبی، تبلیغ و رسانه بارها به‌کار رفت.\n\n"
                           "۶. جایگاه در بحث روز\nدر تحلیل محتوای دیجیتال، کارکرد تماسی (نگه‌داشتن ارتباط) و کارکرد شعری (فرم و جذابیت پیام) در شبکه‌های اجتماعی برجسته‌تر از گذشته شده‌اند."),
    ),
}

NAME_FIX = {}

YEAR_FIX = {
    "MC-368": "year=1906 (Ivy Lee declaration); replaced weak web source with Hiebert 1966; replaced garbled fragmentary analysis",
    "MC-421": "year=2015 (Carlson 2015, DOI verified); Caswell & Dörr 2018 verified; replaced generic template analysis",
    "MC-489": "year=2004 (Hallin & Mancini 2004); 2017 reassessment verified; replaced fragmentary analysis",
    "MC-541": "year=1959 (Riley & Riley 1959, pp. 537-578 verified); replaced generic template analysis",
    "MC-542": "year=1960 (Jakobson 1960, pp. 350-377 verified); replaced generic template analysis",
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
                                       "verified": n_verified, "batch": 214}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH214 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
