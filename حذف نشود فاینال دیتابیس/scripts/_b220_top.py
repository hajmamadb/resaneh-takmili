# -*- coding: utf-8 -*-
"""Batch 220: MC-597 repair, MC-599/MC-609 dedupe pointers, MC-610/MC-611 repair."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch220-20261117"
NOW = "2026-11-17 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch220.json"

S = {
    "MC-597": [
        dict(kind="JOURNAL_ARTICLE", title_en="Furnishing the Edifice: Ongoing Research on Public Relations As a Strategic Management Function",
             title_fa="ساختن بنای نظریه: پژوهش پیوسته دربارهٔ روابط عمومی به‌عنوان کارکرد مدیریت راهبردی",
             authors="James E. Grunig", year=2006, publisher="Journal of Public Relations Research",
             doi="10.1207/s1532754xjprr1802_5",
             url="https://www.tandfonline.com/doi/abs/10.1207/s1532754xjprr1802_5",
             language="en", isbn=None,
             citation="Grunig, J. E. (2006). Furnishing the edifice: Ongoing research on public relations as a strategic management function. Journal of Public Relations Research, 18(2).",
             locator="18(2)", locator_type="PAGE",
             supports="public relations as a strategic management function tied to organizational effectiveness", verified=True),
        dict(kind="BOOK_CHAPTER", title_en="Furnishing the Edifice: Ongoing Research on Public Relations As a Strategic Management Function",
             title_fa="ساختن بنای نظریه: روابط عمومی به‌عنوان کارکرد مدیریت راهبردی",
             authors="James E. Grunig", year=2013, publisher="Routledge",
             doi="10.4324/9780203079256-1",
             url="https://www.taylorfrancis.com/chapters/edit/10.4324/9780203079256-1/furnishing-edifice-james-grunig",
             language="en", isbn=None,
             citation="Grunig, J. E. (2013). Furnishing the edifice: Ongoing research on public relations as a strategic management function. In Public Relations and Communication Management. London: Routledge.",
             locator="ch. 1", locator_type="CHAPTER",
             supports="book-chapter restatement of the strategic management argument", verified=True),
    ],
    "MC-599": [
        dict(kind="JOURNAL_ARTICLE", title_en="Platform Competition in Two-Sided Markets",
             title_fa="رقابت پلتفرم در بازارهای دوسویه",
             authors="Jean-Charles Rochet; Jean Tirole", year=2003,
             publisher="Journal of the European Economic Association",
             doi=None, url="https://academic.oup.com/jeea/article-abstract/1/4/990/2280902",
             language="en", isbn=None,
             citation="Rochet, J.-C., & Tirole, J. (2003). Platform competition in two-sided markets. Journal of the European Economic Association, 1(4), 990-1029.",
             locator="1(4), 990-1029", locator_type="PAGE",
             supports="price structure and platform competition in two-sided markets", verified=True),
        dict(kind="JOURNAL_ARTICLE", title_en="Two-Sided Network Effects: A Theory of Information Product Design",
             title_fa="اثرهای شبکه‌ای دوسویه: نظریه‌ای برای طراحی محصول اطلاعاتی",
             authors="Geoffrey G. Parker; Marshall W. Van Alstyne", year=2005,
             publisher="Management Science", doi="10.1287/mnsc.1050.0400",
             url="https://pubsonline.informs.org/doi/10.1287/mnsc.1050.0400",
             language="en", isbn=None,
             citation="Parker, G. G., & Van Alstyne, M. W. (2005). Two-sided network effects: A theory of information product design. Management Science, 51(10), 1494-1504.",
             locator="51(10), 1494-1504", locator_type="PAGE",
             supports="cross-side network effects in information product design", verified=True),
    ],
    "MC-609": [
        dict(kind="JOURNAL_ARTICLE", title_en="Stability in Competition",
             title_fa="ثبات در رقابت",
             authors="Harold Hotelling", year=1929, publisher="The Economic Journal",
             doi=None, url="https://www.math.toronto.edu/mccann/assignments/477/Hotelling29.pdf",
             language="en", isbn=None,
             citation="Hotelling, H. (1929). Stability in competition. The Economic Journal, 39(153), 41-57.",
             locator="39(153), 41-57", locator_type="PAGE",
             supports="spatial competition and minimum differentiation", verified=True),
        dict(kind="JOURNAL_ARTICLE", title_en="On Hotelling's Stability in Competition",
             title_fa="دربارهٔ ثبات در رقابت هاتلینگ",
             authors="Claude d'Aspremont; Jean Jaskold Gabszewicz; Jacques-François Thisse", year=1979,
             publisher="Econometrica", doi=None,
             url="https://www.di.ens.fr/~aspremon/Claude/PDFs/dAsp79a.pdf",
             language="en", isbn=None,
             citation="d'Aspremont, C., Gabszewicz, J. J., & Thisse, J. F. (1979). On Hotelling's stability in competition. Econometrica, 47(5).",
             locator="47(5)", locator_type="PAGE",
             supports="correction of Hotelling's central equilibrium with linear transport costs", verified=True),
    ],
    "MC-610": [
        dict(kind="BOOK", title_en="Makers: The New Industrial Revolution",
             title_fa="سازندگان: انقلاب صنعتی نوین",
             authors="Chris Anderson", year=2012, publisher="Crown Business",
             doi=None, url="https://en.wikipedia.org/wiki/Makers:_The_New_Industrial_Revolution",
             language="en", isbn=None,
             citation="Anderson, C. (2012). Makers: The New Industrial Revolution. New York: Crown Business.",
             locator="book", locator_type="BOOK",
             supports="maker movement and small-scale digital production", verified=True),
        dict(kind="WEBSITE", title_en="Makers: The New Industrial Revolution by Chris Anderson - review",
             title_fa="نقد کتاب سازندگان اثر کریس اندرسون",
             authors="The Guardian", year=2012, publisher="The Guardian",
             doi=None, url="https://www.theguardian.com/books/2012/dec/07/makers-chris-anderson-review",
             language="en", isbn=None,
             citation="The Guardian (2012, December 7). Makers: The New Industrial Revolution by Chris Anderson - review.",
             locator="review", locator_type="PAGE",
             supports="contemporary critical review of the maker-economy thesis", verified=True),
    ],
    "MC-611": [
        dict(kind="REPORT", title_en="What is the Public Value of Public Service Broadcasting? PEC Discussion Paper",
             title_fa="ارزش عمومی پخش عمومی چیست؟",
             authors="Tom Chivers", year=2022, publisher="Public Economics Centre",
             doi=None, url="https://pec.ac.uk/wp-content/uploads/2024/01/What-is-the-Public-Value-of-Public-Service-Broadcasting-PEC-Discussion-Paper-Jan-2022.pdf",
             language="en", isbn=None,
             citation="Chivers, T. (2022). What is the Public Value of Public Service Broadcasting? PEC Discussion Paper, January 2022.",
             locator="paper", locator_type="PAGE",
             supports="public value and market-failure rationale for public service broadcasting", verified=True),
        dict(kind="REPORT", title_en="BBC Royal Charter Review - House of Commons CMS Committee Report",
             title_fa="بازنگری منشور سلطنتی بی‌بی‌سی - گزارش کمیته رسانه مجلس بریتانیا",
             authors="House of Commons Culture, Media and Sport Committee", year=2026,
             publisher="UK Parliament", doi=None,
             url="https://publications.parliament.uk/pa/cm5902/cmselect/cmcumeds/140/report.html",
             language="en", isbn=None,
             citation="House of Commons Culture, Media and Sport Committee (2026). BBC Royal Charter Review. HC 140.",
             locator="HC 140", locator_type="PAGE",
             supports="current governance and funding debate around public media", verified=True),
    ],
}

ENRICH = {
    "MC-597": dict(
        needs_enrichment=False,
        level="میان",
        related_approaches="نظریهٔ تعالی؛ مدل دوسویهٔ متقارن؛ مدیریت راهبردی؛ ارتباطات سازمانی؛ سنجش اثربخشی.",
        recommended_sources="«ساختن بنای نظریه» (گرونیگ، ۲۰۰۶)؛ «مدیریت روابط عمومی» (گرونیگ و هانت، ۱۹۸۴)؛ «نظریهٔ تعالی و عمل روابط عمومی مؤثر» (گرونیگ، ۱۹۹۲).",
        detailed_analysis=("۱. بنیان و منطق نظری\nگرونیگ (۲۰۰۶) روابط عمومی را کارکردی راهبردی دانست که به بقا و اثربخشی سازمان کمک می‌کند، نه فعالیتی حاشیه‌ای برای ساختن تصویر. "
                           "در این مدل، روابط عمومی با پایش محیط، شناسایی عمومی‌های راهبردی و برقراری ارتباط متقارن، سازمان را در تصمیم‌گیری یاری می‌دهد.\n\n"
                           "۲. ساختارهای مفهومی\nعمومی راهبردی، پایش محیط، ارتباط متقارن، حضور در سطح مدیریت ارشد و اثربخشی سازمان سازه‌های اصلی‌اند. ارزش روابط عمومی زمانی آشکار می‌شود که پیش از تصمیم حاضر باشد، نه پس از آن برای توجیه.\n\n"
                           "۳. نمونه‌های تحلیلی\nسازمانی که پیش از تغییر سیاست با عمومی‌های متأثر گفت‌وگو می‌کند، هزینهٔ مقاومت و بحران را کاهش می‌دهد؛ روابط عمومی که فقط پس از تصمیم بیانیه می‌دهد، به کارکرد تشریفات فروکاسته می‌شود؛ در بحران، حضور در اتاق تصمیم تفاوت میان پاسخ‌گویی و پوزش‌خواهی را می‌سازد.\n\n"
                           "۴. نقدها و چالش‌ها\nمدل هنجاری است و توزیع واقعی قدرت در سازمان را مفروض می‌گیرد؛ سنجش اثربخشی راهبردی دشوار است؛ خطر تبدیل روابط عمومی به ابزار مدیریت شهرت به‌جای گفت‌وگوی واقعی وجود دارد؛ و در سازمان‌های کوچک، ساختار مدیریت ارشد همیشه در دسترس نیست.\n\n"
                           "۵. سیر تاریخی\nکتاب ۱۹۸۴ چارچوب چهار مدل را ساخت، نظریهٔ تعالی دههٔ ۱۹۹۰ آن را به برنامهٔ پژوهشی گسترد و مقالهٔ ۲۰۰۶ جمع‌بندی پژوهش‌های بعدی دربارهٔ کارکرد راهبردی بود.\n\n"
                           "۶. جایگاه در بحث روز\nدر بحث جایگاه روابط عمومی در تصمیم‌گیری سازمانی و سنجش ارزش آن، مدل عمومی گرونیگ چارچوبی برای پیوند ارتباط با اثربخشی سازمان فراهم می‌کند."),
    ),
    "MC-599": dict(
        needs_enrichment=False,
        summary=("این رکورد نسخهٔ دوم مدل بازار دوسویه است؛ نسخهٔ کامل، ارجاع‌محور و بازبینی‌شدهٔ همین مدل با کد MC-501 ثبت شده و برای استناد باید به آن مراجعه شود. "
                 "مدل بازار دوسویه، که ژان-شارل روشه و ژان تیرول در سال ۲۰۰۳ و جفری پارکر و مارشال ون آلستاین در سال ۲۰۰۵ صورت‌بندی کردند، بازارهایی را توصیف می‌کند که در آن‌ها یک پلتفرم دو گروه مختلف را به هم پیوند می‌دهد و حضور هر گروه، ارزش پلتفرم را برای گروه دیگر افزایش می‌دهد. نمونهٔ کلاسیک آن رسانه است: مخاطب و تبلیغ‌دهنده. ویژگی اصلی این بازارها، اثر شبکه‌ای متقاطع است: رشد یک طرف، سود طرف دیگر را بالا می‌برد. از این رو، پلتفرم اغلب یک طرف را با قیمت پایین یا رایگان جذب می‌کند و هزینه را از طرف دیگر یا از طریق تبلیغات و خدمات مکمل برمی‌دارد. ساختار قیمت، نه سطح قیمت، تعیین‌کنندهٔ موفقیت است. این مدل توضیح می‌دهد چرا روزنامه‌ها، شبکه‌های اجتماعی، موتورهای جست‌وجو و پلتفرم‌های خرید، مخاطب را رایگان نگه می‌دارند و از سوی دیگر درآمد می‌گیرند؛ قیمت صفر یک تصمیم راهبردی است، نه سخاوت. نقدهای اصلی به آن، فرض عقلانیت کامل بازیگران، کم‌توجهی به قدرت انحصاری پلتفرم‌ها، پیچیدگی سنجش اثر متقاطع و دشواری تعمیم به بازارهای چندطرفه را برجسته می‌کنند."),
        level="میان",
        related_approaches="اقتصاد پلتفرم؛ بازار دوسویه؛ اثر شبکه‌ای؛ طراحی محصول اطلاعاتی؛ سیاست رقابت.",
        recommended_sources="برای استناد به مدل بازار دوسویه به رکورد کامل MC-501 مراجعه شود؛ «رقابت پلتفرم در بازارهای دوسویه» (روشه و تیرول، ۲۰۰۳)؛ «اثرهای شبکه‌ای دوسویه» (پارکر و ون آلس‌تاین، ۲۰۰۵).",
        detailed_analysis=("این رکورد نسخهٔ دوم مدل بازار دوسویه است و نسخهٔ کامل، ارجاع‌محور و بازبینی‌شدهٔ همین مدل با کد MC-501 ثبت شده است؛ برای استناد علمی باید به آن رکورد مراجعه شود. "
                           "ارزش حفظ این رکورد در آن است که صورت‌بندی مکمل پارکر و ون آلس‌تاین (۲۰۰۵) را نگه می‌دارد: آنان اثر شبکه‌ای متقاطع را به نظریهٔ طراحی محصول اطلاعاتی پیوند دادند و نشان دادند انتخاب سمت یارانه‌ای، تصمیم طراحی است و نه فقط تصمیم قیمتی.\n\n"
                           "تفاوت تأکید دو رکورد این است که MC-501 بر رقابت پلتفرم و ساختار قیمت روشه و تیرول متمرکز است و این رکورد بر طراحی محصول و اثر متقاطع پارکر و ون آلس‌تاین. "
                           "برای تحلیل کامل سازوکار، نقدها و کاربردهای رسانه‌ای، به متن رکورد اصلی مراجعه کنید."),
    ),
    "MC-609": dict(
        needs_enrichment=False,
        level="میان",
        related_approaches="اقتصاد رسانه؛ رقابت مکانی؛ تمایز محصول؛ همگرایی مواضع سیاسی؛ طراحی پلتفرم.",
        recommended_sources="برای استناد به مدل هاتلینگ به رکورد کامل MC-185 مراجعه شود؛ «ثبات در رقابت» (هاتلینگ، ۱۹۲۹)؛ «دربارهٔ ثبات در رقابت هاتلینگ» (داسپرمون و همکاران، ۱۹۷۹).",
        detailed_analysis=("این رکورد نسخهٔ دوم مدل تمایز مکانی هاتلینگ است و نسخهٔ کامل، ارجاع‌محور و بازبینی‌شدهٔ همین مدل با کد MC-185 ثبت شده است؛ برای استناد علمی باید به آن رکورد مراجعه شود. "
                           "دلیل حفظ این رکورد، نگه‌داشتن ارجاع به تصحیح داسپرمون و همکاران (۱۹۷۹) است: آنان نشان دادند با هزینهٔ خطی حمل، تعادل مرکزی هاتلینگ پایدار نمی‌ماند و نتیجهٔ «تمایز حداقلی» را نمی‌توان بی‌قید تعمیم داد.\n\n"
                           "برای تحلیل کامل سازوکار، نقدها و کاربردهای رسانه‌ای مدل، به متن رکورد اصلی مراجعه کنید."),
    ),
    "MC-610": dict(
        needs_enrichment=False,
        level="میان",
        related_approaches="اقتصاد خالقان؛ تولید مشارکتی؛ پلتفرم‌های محتوا؛ نوآوری باز؛ اقتصاد اشتراکی.",
        recommended_sources="«سازندگان: انقلاب صنعتی نوین» (اندرسون، ۲۰۱۲)؛ «دُم بلند» (اندرسون، ۲۰۰۶)؛ «نقد کتاب سازندگان» (گاردین، ۲۰۱۲).",
        detailed_analysis=("۱. بنیان و منطق نظری\nاندرسون (۲۰۱۲) اقتصاد سازندگان را الگویی از تولید و توزیع دانست که در آن افراد و گروه‌های کوچک با ابزارهای دیجیتال ارزان، طراحی باز و پلتفرم‌های توزیع، از مصرف‌کننده به تولیدکننده تبدیل می‌شوند. "
                           "چاپ سه‌بعدی، برش لیزری، نرم‌افزار آزاد و بازارگاه‌های آنلاین تولید در مقیاس کوچک را ممکن می‌کنند.\n\n"
                           "۲. ساختارهای مفهومی\nتولید توزیع‌شده، ابزار ارزان، طراحی باز، بازارگاه آنلاین، اجتماع سازندگان و مرز حرفه‌ای-آماتور سازه‌های اصلی‌اند.\n\n"
                           "۳. نمونه‌های تحلیلی\nطراحی یک محصول در یک کارگاه خانگی و فروش آن در بازارگاه آنلاین نمونهٔ اجرای مدل است؛ در رسانه نیز تولید محتوای مستقل با ابزار ارزان و توزیع پلتفرمی همان منطق را نشان می‌دهد؛ چاپ سه‌بعدی قطعات یدکی نمونهٔ صنعتی آن است.\n\n"
                           "۴. نقدها و چالش‌ها\nمدل توان مالی و مهارت را بیش از واقع فرض می‌کند؛ دسترسی به سرمایه و مقیاس‌پذیری را کم‌بررسی می‌گذارد؛ نقد معاصر (گاردین، ۲۰۱۲) به شکاف میان رؤیا و واقعیت بازار اشاره کرد؛ و وابستگی به پلتفرم‌های توزیع، قدرت آن‌ها را بازتولید می‌کند.\n\n"
                           "۵. سیر تاریخی\nکتاب ۲۰۱۲ در ادامهٔ روایت دُم بلند نوشته شد و جنبش سازندگان و تولید توزیع‌شده را به اقتصاد دیجیتال پیوند داد؛ سال‌های بعد، اقتصاد خالقان و تولید هوش مصنوعی این خط را گستردند.\n\n"
                           "۶. جایگاه در بحث روز\nدر گفتمان اقتصاد خالقان و تولید توزیع‌شده، مدل سازندگان یادآوری می‌کند که کاهش هزینهٔ ابزار می‌تواند ساختار تولید را تغییر دهد، اما توزیع و توجه همچنان در دست پلتفرم‌ها متمرکز می‌ماند."),
    ),
    "MC-611": dict(
        needs_enrichment=False,
        level="میان",
        related_approaches="اقتصاد سیاسی رسانه؛ پخش عمومی؛ سیاست فرهنگی؛ منفعت عمومی؛ حکمرانی رسانه.",
        recommended_sources="«ارزش عمومی پخش عمومی چیست؟» (چیورز، ۲۰۲۲)؛ «بازنگری منشور سلطنتی بی‌بی‌سی» (کمیته رسانه مجلس بریتانیا، ۲۰۲۶)؛ «اقتصاد رسانه» (هاردوود).",
        detailed_analysis=("۱. بنیان و منطق نظری\nمدل رسانهٔ عمومی با تجربهٔ بی‌بی‌سی و پخش عمومی در اروپا شکل گرفت: رسانه خدمتی عمومی است، نه کالای بازاری. "
                           "بودجهٔ عمومی، دسترسی همگانی و استقلال از دولت و بازار، سه پایهٔ آن‌اند؛ پخش‌کنندهٔ عمومی از راه حق اشتراک یا مالیات تأمین می‌شود تا از فشار تبلیغ‌دهنده و وابستگی سیاسی رها بماند.\n\n"
                           "۲. ساختارهای مفهومی\nجهان‌شمولی، تنوع، کیفیت، بی‌طرفی، خدمت به اقلیت‌ها و پاسخ‌گویی عمومی اصول کلاسیک‌اند؛ معیار موفقیت سود نیست، بلکه ارزش عمومی است.\n\n"
                           "۳. نمونه‌های تحلیلی\nپوشش خبری بی‌طرف و آموزش کودکان نمونه‌های کارکرد خدمت عمومی‌اند؛ در بحران ملی، رسانهٔ عمومی می‌تواند اطلاعات همگانی و قابل اعتماد فراهم کند؛ در بازارهای کوچک زبانی، رسانهٔ تجاری صرفه ندارد و رسانهٔ عمومی تنوع را حفظ می‌کند.\n\n"
                           "۴. نقدها و چالش‌ها\nخطر نخبه‌گرایی و فاصله از مخاطب عام وجود دارد؛ تعریف بی‌طرفی محل مناقشه است؛ اثر بر رقابت بازار و رسانه‌های خصوصی بحث‌برانگیز است؛ وابستگی به بودجهٔ دولتی می‌تواند استقلال را تهدید کند؛ و در عصر پلتفرم، بحران مشروعیت و مخاطب جوان مسئلهٔ تازه است.\n\n"
                           "۵. سیر تاریخی\nمدل از دههٔ ۱۹۲۰ با بی‌بی‌سی شکل گرفت، در اروپا نهادینه شد و در دههٔ ۲۰۲۰ با بازنگری منشور و بحث ارزش عمومی بازخوانی شد.\n\n"
                           "۶. جایگاه در بحث روز\nدر بحث آیندهٔ بی‌بی‌سی و پخش عمومی در اروپا، مدل رسانهٔ عمومی پرسش را از «آیا بازار می‌تواند تأمین کند» به «چه ارزشی جز بازار برای جامعه ساخته می‌شود» تغییر می‌دهد."),
    ),
}

NAME_FIX = {
    "MC-599": ("مدل بازار دوسویه (رکورد دوم)", "Two-Sided Market Model (second record)",
               "duplicate of MC-501 detected; retained as second record with pointer to canonical entry"),
}

YEAR_FIX = {
    "MC-597": "replaced media-economics template analysis with Grunig-2006 strategic-management analysis; rebuilt recommendations",
    "MC-599": "deduplicated against MC-501; renamed as second record; template analysis replaced with pointer analysis",
    "MC-609": "deduplicated against MC-185; template analysis replaced with pointer analysis",
    "MC-610": "replaced media-economics template analysis with maker-economy analysis; rebuilt recommendations",
    "MC-611": "replaced media-economics template analysis with public-media analysis; rebuilt recommendations",
}
