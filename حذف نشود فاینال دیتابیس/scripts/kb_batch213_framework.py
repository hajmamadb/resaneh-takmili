# -*- coding: utf-8 -*-
"""Batch 213: MC-495, MC-497, MC-345, MC-348, MC-367."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch213-20261117"
NOW = "2026-11-17 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch213.json"

S = {
    "MC-495": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Building Dialogic Relationships Through the World Wide Web",
             title_fa="ساختن روابط گفت‌وگویی از راه وب جهان‌گستر",
             authors="Michael L. Kent; Maureen Taylor", year=1998,
             publisher="Public Relations Review",
             doi=None,
             url="http://www.mlkent.com/PDFs/PRRTowardTheoryDialoguePR.pdf",
             language="en", isbn=None,
             citation="Kent, M. L., & Taylor, M. (1998). Building dialogic relationships through the World Wide Web. Public Relations Review, 24(3), 321-334.",
             locator="24(3), 321-334",
             locator_type="PAGE",
             supports="five principles of dialogic web communication",
             verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Toward a Dialogic Theory of Public Relations",
             title_fa="به‌سوی نظریه‌ای گفت‌وگویی برای روابط عمومی",
             authors="Michael L. Kent; Maureen Taylor", year=2002,
             publisher="Public Relations Review",
             doi="10.1016/S0363-8111(02)00108-X",
             url="https://www.sciencedirect.com/science/article/abs/pii/S036381110200108X",
             language="en", isbn=None,
             citation="Kent, M. L., & Taylor, M. (2002). Toward a dialogic theory of public relations. Public Relations Review, 28(1), 21-37. https://doi.org/10.1016/S0363-8111(02)00108-X",
             locator="28(1), 21-37",
             locator_type="PAGE",
             supports="dialogic orientation with mutuality, propinquity, empathy, risk and commitment",
             verified=True),
    ],
    "MC-497": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Choosing the Right Words: The Development of Guidelines for the Selection of the Appropriate Crisis-Response Strategies",
             title_fa="گزینش واژهٔ درست: تدوین رهنمودهایی برای انتخاب راهبردهای مناسب پاسخ به بحران",
             authors="W. Timothy Coombs", year=1995,
             publisher="Management Communication Quarterly",
             doi="10.1177/0893318995008004003",
             url="https://journals.sagepub.com/doi/10.1177/0893318995008004003",
             language="en", isbn=None,
             citation="Coombs, W. T. (1995). Choosing the right words: The development of guidelines for the selection of the appropriate crisis-response strategies. Management Communication Quarterly, 8(4), 447-476. https://doi.org/10.1177/0893318995008004003",
             locator="8(4), 447-476",
             locator_type="PAGE",
             supports="early guidelines linking crisis type to response strategy",
             verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Protecting Organization Reputations During a Crisis: The Development and Application of Situational Crisis Communication Theory",
             title_fa="حفاظت از شهرت سازمان در بحران: تدوین و کاربست نظریهٔ موقعیتی ارتباطات بحران",
             authors="W. Timothy Coombs", year=2007,
             publisher="Corporate Reputation Review",
             doi=None,
             url="https://link.springer.com/article/10.1057/palgrave.crr.1550049",
             language="en", isbn=None,
             citation="Coombs, W. T. (2007). Protecting organization reputations during a crisis: The development and application of situational crisis communication theory. Corporate Reputation Review, 10(3), 163-176.",
             locator="10(3), 163-176",
             locator_type="PAGE",
             supports="crisis clusters, crisis history and response strategy selection",
             verified=True),
    ],
    "MC-345": [
        dict(kind="BOOK",
             title_en="Collected Papers of Charles Sanders Peirce, Vol. II: Elements of Logic",
             title_fa="مقالات گردآوری‌شدهٔ چارلز سندرس پیرس، جلد دوم: عناصر منطق",
             authors="Charles Sanders Peirce; Charles Hartshorne (ed.); Paul Weiss (ed.)", year=1932,
             publisher="Harvard University Press",
             doi=None,
             url="https://colorysemiotica.files.wordpress.com/2014/08/peirce-collectedpapers.pdf",
             language="en", isbn=None,
             citation="Peirce, C. S. (1932). Collected Papers of Charles Sanders Peirce, Vol. II: Elements of Logic (C. Hartshorne & P. Weiss, Eds.). Cambridge, MA: Harvard University Press.",
             locator="vol. II",
             locator_type="BOOK",
             supports="representamen, object and interpretant as the triadic sign relation",
             verified=True),
        dict(kind="WEBSITE",
             title_en="Peirce's Theory of Signs",
             title_fa="نظریهٔ نشانه‌های پیرس",
             authors="Albert Atkin", year=2023,
             publisher="Stanford Encyclopedia of Philosophy",
             doi=None,
             url="https://plato.stanford.edu/entries/peirce-semiotics/",
             language="en", isbn=None,
             citation="Atkin, A. (2023). Peirce's theory of signs. In E. N. Zalta (Ed.), Stanford Encyclopedia of Philosophy.",
             locator="entry",
             locator_type="CHAPTER",
             supports="icon, index and symbol and unlimited semiosis",
             verified=True),
    ],
    "MC-348": [
        dict(kind="BOOK",
             title_en="The Role of the Reader: Explorations in the Semiotics of Texts",
             title_fa="نقش خواننده: کاوش‌هایی در نشانه‌شناسی متن‌ها",
             authors="Umberto Eco", year=1979,
             publisher="Indiana University Press",
             doi=None,
             url="https://iupress.org/9780253203182/the-role-of-the-reader/",
             language="en", isbn=None,
             citation="Eco, U. (1979). The Role of the Reader: Explorations in the Semiotics of Texts. Bloomington: Indiana University Press.",
             locator="book",
             locator_type="BOOK",
             supports="model reader and open versus closed texts",
             verified=True),
        dict(kind="BOOK",
             title_en="The Open Work",
             title_fa="اثر باز",
             authors="Umberto Eco", year=1989,
             publisher="Harvard University Press",
             doi=None,
             url=None,
             language="en", isbn=None,
             citation="Eco, U. (1989). The Open Work (A. Cancogni, Trans.). Cambridge, MA: Harvard University Press.",
             locator="book",
             locator_type="BOOK",
             supports="open text and interpretive cooperation",
             verified=True),
    ],
    "MC-367": [
        dict(kind="BOOK",
             title_en="The Life of P. T. Barnum, Written by Himself",
             title_fa="زندگی فینیاس تی. بارنوم به قلم خودش",
             authors="P. T. Barnum", year=1855,
             publisher="Redfield",
             doi=None,
             url="https://archive.org/details/lifeofptbarnumwr00barn",
             language="en", isbn=None,
             citation="Barnum, P. T. (1855). The Life of P. T. Barnum, Written by Himself. New York: Redfield.",
             locator="book",
             locator_type="BOOK",
             supports="publicity-driven promotion and press agentry practice",
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
             supports="press agentry as one of four historical models of public relations",
             verified=True),
    ],
}

ENRICH = {
    "MC-495": dict(
        needs_enrichment=False,
        level="میان",
        related_approaches="مدل‌های چهارگانهٔ روابط عمومی؛ روابط عمومی دوسویه؛ ارتباطات مشارکتی؛ اخلاق گفت‌وگو.",
        recommended_sources="«ساختن روابط گفت‌وگویی از راه وب» (کنت و تیلور، ۱۹۹۸)؛ «به‌سوی نظریه‌ای گفت‌وگویی برای روابط عمومی» (کنت و تیلور، ۲۰۰۲)؛ «پرورش مشارکت گفت‌وگویی» (کنت و تیلور، ۲۰۲۱).",
        detailed_analysis=("۱. بنیان و منطق نظری\nکنت و تیلور (۱۹۹۸) پنج اصل برای ارتباط گفت‌وگویی سازمان با مخاطب در وب پیشنهاد کردند: حلقهٔ گفت‌وگو، سودمندی اطلاعات، بازگرداندن بازدیدکننده، آسانی رابط و نگهداشت مخاطب. "
                           "در ۲۰۰۲ این اصول را به نظریه‌ای عمومی ارتقا دادند و گفت‌وگو را نه یک ابزار، بلکه جهت‌گیری سازمانی دانستند: متقابلیت، نزدیکی، همدلی، پذیرش ریسک و تعهد.\n\n"
                           "۲. ساختارهای مفهومی\nحلقهٔ گفت‌وگو، متقابلیت، نزدیکی، همدلی، ریسک و تعهد سازه‌های اصلی‌اند. "
                           "گفت‌وگوی واقعی مستلزم آن است که سازمان به پاسخ مخاطب واکنش معنادار بدهد و برای تغییر موضع خود آماده باشد.\n\n"
                           "۳. نمونه‌های تحلیلی\nسازمانی که در شبکهٔ اجتماعی به پرسش‌ها پاسخ می‌دهد اما سیاست خود را تغییر نمی‌دهد، حلقهٔ گفت‌وگو را ظاهری نگه می‌دارد؛ در مقابل، انتشار پیش‌نویس سیاست و دریافت بازخورد عمومی، نمونهٔ نزدیک‌تر به گفت‌وگوی واقعی است.\n\n"
                           "۴. نقدها و چالش‌ها\nمدل آرمان‌گراست و فرض می‌کند سازمان قدرت را با مخاطب تقسیم می‌کند؛ سنجش گفت‌وگوی واقعی دشوار است؛ در محیط رقابتی و بحرانی، سازمان‌ها اغلب به ارتباط یک‌سویه بازمی‌گردند؛ و تفاوت‌های فرهنگی در معنای گفت‌وگو کم‌بررسی مانده است.\n\n"
                           "۵. سیر تاریخی\nمقالهٔ ۱۹۹۸ گفت‌وگو را وارد پژوهش روابط عمومی دیجیتال کرد، نظریهٔ ۲۰۰۲ چارچوب هنجاری آن را تثبیت کرد و پژوهش‌های بعدی مشارکت گفت‌وگویی و سنجه‌های آن را توسعه دادند.\n\n"
                           "۶. جایگاه در بحث روز\nدر عصر پلتفرم‌ها، پرسش از گفت‌وگوی واقعی در برابر پاسخگویی نمایشی به یکی از محورهای نقد روابط عمومی دیجیتال تبدیل شده است."),
    ),
    "MC-497": dict(
        needs_enrichment=False,
        level="میان",
        related_approaches="نظریهٔ انتساب؛ مدیریت بحران؛ مدیریت شهرت؛ ارتباطات خطر؛ روابط عمومی دوسویه.",
        recommended_sources="«گزینش واژهٔ درست» (کومبز، ۱۹۹۵)؛ «نظریهٔ موقعیتی ارتباطات بحران» (کومبز، ۲۰۰۷)؛ «راهبرد و کاربست روابط عمومی» (کومبز و هالادی، ۲۰۱۰).",
        detailed_analysis=("۱. بنیان و منطق نظری\nکومبز (۱۹۹۵) با تکیه بر نظریهٔ انتساب، رهنمودهایی برای انتخاب راهبرد پاسخ به بحران عرضه کرد: پاسخ باید با میزان مسئولیت ادراک‌شدهٔ سازمان هم‌خوان باشد. "
                           "در ۲۰۰۷ این چارچوب را به نظریهٔ موقعیتی ارتباطات بحران ارتقا داد: نوع بحران (قربانی، حادثه، قابل‌پیشگیری)، تاریخ بحران‌های پیشین و شهرت پیشین، شدت تهدید شهرت را تعیین می‌کنند.\n\n"
                           "۲. ساختارهای مفهومی\nگونه‌های بحران، سابقهٔ بحران، شهرت پیشین و چهار خانوادهٔ راهبرد پاسخ — انکار، کاهش، بازسازی و تقویت — سازه‌های اصلی‌اند.\n\n"
                           "۳. نمونه‌های تحلیلی\nدر بحرانی که سازمان مقصر شناخته می‌شود، انکار معمولاً تهدید را تشدید می‌کند و راهبرد عذرخواهی و جبران مناسب‌تر است؛ در بحرانی که سازمان قربانی است، راهبرد کاهش و تقویت کافی به نظر می‌رسد.\n\n"
                           "۴. نقدها و چالش‌ها\nنوع‌شناسی بحران همیشه با ادراک عمومی هم‌خوان نیست؛ شواهد تجربی در بافت‌های فرهنگی متفاوت ناهمگون است؛ مدل بیشتر بر شهرت متمرکز است تا آسیب واقعی قربانیان؛ و سرعت و شفافیت در محیط شبکه‌های اجتماعی را کمتر توضیح می‌دهد.\n\n"
                           "۵. سیر تاریخی\nرهنمود ۱۹۹۵ نخستین صورت‌بندی بود، نظریهٔ ۲۰۰۷ آن را نظام‌مند کرد و پژوهش‌های بعدی آن را با رسانه‌های اجتماعی و بحران‌های سلامت گستردند.\n\n"
                           "۶. جایگاه در بحث روز\nدر بحران‌های اطلاعات نادرست و بحران‌های زیست‌محیطی، انتخاب راهبرد پاسخ بر پایهٔ مسئولیت ادراک‌شده هنوز چارچوبی کاربردی برای سازمان‌هاست."),
    ),
    "MC-345": dict(
        needs_enrichment=False,
        level="میان",
        related_approaches="نشانه‌شناسی سوسوری؛ نشانه‌شناسی فرهنگی؛ تحلیل گفتمان؛ نشانه‌شناسی بصری؛ عملگرایی.",
        recommended_sources="«مقالات گردآوری‌شده»، جلد دوم (پیرس، ۱۹۳۲)؛ «نظریهٔ نشانه‌های پیرس» در دانشنامهٔ فلسفهٔ استنفورد (اتکین، ۲۰۲۳)؛ «نشانه‌شناسی: مبانی» (چندلر، ۲۰۰۲).",
        detailed_analysis=("۱. بنیان و منطق نظری\nپیرس نشانه را رابطه‌ای سه‌جزئی دانست: بازنمون (صورت نشانه)، موضوع (آنچه نشانه به آن اشاره می‌کند) و تفسیر (اثری که نشانه در ذهن می‌سازد). "
                           "برخلاف الگوی دوجزئی دال و مدلول سوسور، در نشانه‌شناسی پیرس تفسیر خود به نشانه‌ای تازه تبدیل می‌شود و فرایند نشانه‌ای بی‌پایان ادامه می‌یابد.\n\n"
                           "۲. ساختارهای مفهومی\nسه‌گانهٔ بازنمون-موضوع-تفسیر، سه گونهٔ نشانه (شمایل، نمایه، نماد) و مفهوم معناشناسی نامحدود سازه‌های اصلی‌اند. "
                           "شمایل شباهت دارد، نمایه رابطهٔ علّی یا مجاورت دارد و نماد بر قرارداد استوار است.\n\n"
                           "۳. نمونه‌های تحلیلی\nعکس یک شخص شمایل است، دود نمایهٔ آتش است و واژهٔ «آزادی» نماد قراردادی است؛ یک آگهی می‌تواند هم‌زمان از هر سه گونه بهره ببرد و معنای چندلایه بسازد.\n\n"
                           "۴. نقدها و چالش‌ها\nمدل انتزاعی و دشوار است و کاربرد تجربی آن نیازمند تفسیر پژوهشگر است؛ مرز گونه‌های نشانه در عمل مبهم می‌شود؛ تفسیرهای مخاطب متفاوت‌اند؛ و کاربرد آن در تحلیل رسانه‌های چندرسانه‌ای پیچیده است.\n\n"
                           "۵. سیر تاریخی\nپیرس چارچوب را در اواخر سدهٔ نوزدهم پرورد، در مقالات گردآوری‌شدهٔ ۱۹۳۱ تا ۱۹۳۵ منتشر شد و پس از دههٔ ۱۹۸۰ به یکی از بنیان‌های نشانه‌شناسی رسانه بدل شد.\n\n"
                           "۶. جایگاه در بحث روز\nدر تحلیل تصویر، ایموجی و نشانه‌های رابط کاربری، سه‌گانهٔ پیرس ابزاری دقیق برای فهم لایه‌های معنایی و تفسیرهای متفاوت مخاطب است."),
    ),
    "MC-348": dict(
        needs_enrichment=False,
        level="میان",
        related_approaches="نشانه‌شناسی سه‌گانه پیرس؛ نشانه‌شناسی ساختگرا؛ نظریهٔ دریافت؛ تحلیل گفتمان؛ زیبایی‌شناسی دریافت.",
        recommended_sources="«نقش خواننده» (اکو، ۱۹۷۹)؛ «اثر باز» (اکو، ۱۹۸۹)؛ «نشانه‌شناسی: مبانی» (چندلر، ۲۰۰۲).",
        detailed_analysis=("۱. بنیان و منطق نظری\nاکو (۱۹۷۹) در «نقش خواننده» مفهوم خوانندهٔ الگو را عرضه کرد: متن، مخاطب آرمانی خود را می‌سازد و از او انتظار همکاری تفسیری دارد. "
                           "او متن‌ها را به باز و بسته تقسیم کرد: متن باز، خواننده را به تولید معنا و تکمیل متن فرا می‌خواند؛ متن بسته، مسیر تفسیر را تنگ می‌کند و خوانندهٔ از پیش تعیین‌شده می‌سازد.\n\n"
                           "۲. ساختارهای مفهومی\nخوانندهٔ الگو، متن باز، متن بسته، همکاری متنی و دانشنامهٔ فرهنگی سازه‌های اصلی‌اند. "
                           "معنا محصول تعامل راهبرد متن و توانش تفسیری خواننده است.\n\n"
                           "۳. نمونه‌های تحلیلی\nرمان‌های تجربی با پایان‌های چندگانه، خواننده را به هم‌آفرینی معنا دعوت می‌کنند؛ در مقابل، پیام تبلیغاتی با ساختار بسته، تفسیر واحد و رفتار خرید مشخص را هدف می‌گیرد.\n\n"
                           "۴. نقدها و چالش‌ها\nخوانندهٔ الگو با خوانندهٔ تجربی یکی نیست و مرز آن مبهم می‌ماند؛ قدرت متن در تعیین تفسیر بیش از حد برجسته می‌شود؛ سنجش تجربی باز و بسته بودن متن دشوار است؛ و بافت اجتماعی خوانش کم‌بررسی می‌ماند.\n\n"
                           "۵. سیر تاریخی\nکتاب ۱۹۷۹ نشانه‌شناسی متن را به نظریهٔ خوانش پیوند زد و «اثر باز» (۱۹۸۹) پیشینهٔ زیبایی‌شناختی آن را روشن کرد؛ پس از آن، نظریهٔ دریافت و مطالعات فرهنگی از آن بهره گرفتند.\n\n"
                           "۶. جایگاه در بحث روز\nدر تحلیل متن تعاملی، بازی ویدیویی و روایت‌های غیرخطی، مفهوم خوانندهٔ الگو برای فهم نقش مخاطب در تکمیل معنا همچنان کارآمد است."),
    ),
    "MC-367": dict(
        needs_enrichment=False,
        level="پایه",
        related_approaches="مدل‌های چهارگانهٔ روابط عمومی؛ ارتباطات اقناعی؛ اقتصاد توجه؛ اخلاق تبلیغات؛ رویدادسازی رسانه‌ای.",
        recommended_sources="«زندگی بارنوم» (بارنوم، ۱۸۵۵)؛ «مدیریت روابط عمومی» (گرونیگ و هانت، ۱۹۸۴)؛ «روابط عمومی مؤثر» (کاتلیپ و همکاران).",
        detailed_analysis=("۱. بنیان و منطق نظری\nمدل تبلیغ‌گری مطبوعاتی، کهن‌ترین الگوی روابط عمومی است و با نام فینیاس تی. بارنوم و نمایش‌های تبلیغاتی سدهٔ نوزدهم پیوند دارد. "
                           "در این مدل، هدف جلب توجه رسانه و مخاطب است و حقیقت کامل اطلاعات شرط نیست؛ بارنوم در زندگی‌نامهٔ ۱۸۵۵ خود شیوهٔ ساختن رویداد و هیاهوی رسانه‌ای را روایت کرد. "
                           "گرونیگ و هانت (۱۹۸۴) این الگو را نخستین مدل از چهار مدل تاریخی روابط عمومی نامیدند.\n\n"
                           "۲. ساختارهای مفهومی\nتبلیغ یک‌سویه، جلب توجه، رویداد ساختگی، اغراق و رابطهٔ ابزاری با رسانه سازه‌های اصلی‌اند.\n\n"
                           "۳. نمونه‌های تحلیلی\nنمایش‌های سیرک بارنوم نمونهٔ کلاسیک رویدادسازی برای جلب پوشش خبری است؛ در محیط دیجیتال، تیترهای اغراق‌آمیز و جنجال‌های برنامه‌ریزی‌شده همان منطق را بازتولید می‌کنند.\n\n"
                           "۴. نقدها و چالش‌ها\nمدل با فریب و نیمه‌حقیقت پیوند دارد و اعتماد عمومی را فرسوده می‌کند؛ اخلاق ارتباطی را نادیده می‌گیرد؛ برای بحران‌ها ناکارآمد است؛ و در محیطی که مخاطب به‌سرعت راستی‌آزمایی می‌کند، خطر بی‌اعتباری سازمان را بالا می‌برد.\n\n"
                           "۵. سیر تاریخی\nشیوهٔ بارنوم در سدهٔ نوزدهم رایج شد، در سدهٔ بیستم با مدل اطلاع‌رسانی عمومی و سپس مدل‌های دوسویه جایگزین شد و در گونه‌شناسی گرونیگ و هانت جایگاه تاریخی یافت.\n\n"
                           "۶. جایگاه در بحث روز\nمنطق تبلیغ‌گری در اقتصاد توجه و فرهنگ کلیک‌بیت بازگشته است؛ نقد این مدل امروز به بحث مسئولیت رسانه‌ای و راستی‌آزمایی محتوا گره خورده است."),
    ),
}

NAME_FIX = {}

YEAR_FIX = {
    "MC-495": "year=1998 (Kent & Taylor 1998); Kent & Taylor 2002 verified; replaced media-economics template analysis",
    "MC-497": "year=1995 (Coombs 1995); Coombs 2007 verified; replaced media-economics template analysis",
    "MC-345": "year=1931 (Peirce Collected Papers); replaced semiotic-template analysis",
    "MC-348": "year=1979 (Eco 1979); replaced semiotic-template analysis and duplicate source entry",
    "MC-367": "year=1855 (Barnum 1855); Grunig & Hunt 1984 verified; replaced garbled fragmentary analysis",
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
                                       "verified": n_verified, "batch": 213}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH213 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
