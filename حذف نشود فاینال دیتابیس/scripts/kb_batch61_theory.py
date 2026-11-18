# -*- coding: utf-8 -*-
"""Batch 61 (THEORY): MC-311 Cybernetics (Wiener 1948), MC-312 General Systems Theory
(Bertalanffy 1968), MC-313 Social Constructivism (Berger & Luckmann 1966),
MC-314 Symbolic Interactionism (Blumer 1969; Mead 1934). Anchors verified 2026-11-16.
Overwrites the mismatched generic critique/example boilerplate found on all four records."""
import pymysql, json

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch61-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch61_theory.json"

S = {
 "MC-311": [
   dict(kind="BOOK", title_en="Cybernetics: Or Control and Communication in the Animal and the Machine",
        title_fa="سایبرنتیک: یا کنترل و ارتباط در حیوان و ماشین",
        authors="Wiener, N.", year=1948, publisher="Cambridge, MA: The MIT Press", doi=None,
        url="https://mitpress.mit.edu/9780262537841/cybernetics-or-control-and-communication-in-the-animal-and-the-machine/",
        language="en", isbn=None,
        citation="Wiener, N. (1948). Cybernetics: Or control and communication in the animal and the machine. The MIT Press.",
        locator="whole work", locator_type="work", supports="definition / feedback / entropy and information", verified=True),
   dict(kind="BOOK", title_en="The Human Use of Human Beings: Cybernetics and Society",
        title_fa="کاربرد انسانی انسان‌ها: سایبرنتیک و جامعه",
        authors="Wiener, N.", year=1950, publisher="Boston: Houghton Mifflin", doi=None, url=None,
        language="en", isbn=None,
        citation="Wiener, N. (1950). The human use of human beings: Cybernetics and society. Houghton Mifflin.",
        locator="whole work", locator_type="work", supports="evolution / social and ethical extension", verified=False),
 ],
 "MC-312": [
   dict(kind="BOOK", title_en="General System Theory: Foundations, Development, Applications",
        title_fa="نظریهٔ عمومی سیستم‌ها: بنیادها، تحول و کاربردها",
        authors="von Bertalanffy, L.", year=1968, publisher="New York: George Braziller", doi=None,
        url="https://monoskop.org/File:Von_Bertalanffy_Ludwig_General_System_Theory_1968.pdf",
        language="en", isbn=None,
        citation="von Bertalanffy, L. (1968). General system theory: Foundations, development, applications. George Braziller.",
        locator="whole work", locator_type="work", supports="definition / open systems / equifinality", verified=True),
   dict(kind="JOURNAL_ARTICLE", title_en="An Outline of General System Theory",
        title_fa="طرحی از نظریهٔ عمومی سیستم",
        authors="von Bertalanffy, L.", year=1950,
        publisher="The British Journal for the Philosophy of Science, 1(2), 134-165", doi=None, url=None,
        language="en", isbn=None,
        citation="von Bertalanffy, L. (1950). An outline of general system theory. The British Journal for the Philosophy of Science, 1(2), 134-165.",
        locator="pp. 134-165", locator_type="page_range", supports="early statement / isomorphism across disciplines", verified=False),
 ],
 "MC-313": [
   dict(kind="BOOK", title_en="The Social Construction of Reality: A Treatise in the Sociology of Knowledge",
        title_fa="برساخت اجتماعی واقعیت: رساله‌ای در جامعه‌شناسی معرفت",
        authors="Berger, P. L., & Luckmann, T.", year=1966, publisher="Garden City, NY: Doubleday", doi=None,
        url="https://en.wikipedia.org/wiki/The_Social_Construction_of_Reality",
        language="en", isbn=None,
        citation="Berger, P. L., & Luckmann, T. (1966). The social construction of reality: A treatise in the sociology of knowledge. Doubleday.",
        locator="whole work", locator_type="work", supports="definition / externalization, objectivation, internalization", verified=True),
   dict(kind="BOOK", title_en="The Social Construction of What?",
        title_fa="برساخت اجتماعی چه چیزی؟",
        authors="Hacking, I.", year=1999, publisher="Cambridge, MA: Harvard University Press", doi=None, url=None,
        language="en", isbn=None,
        citation="Hacking, I. (1999). The social construction of what? Harvard University Press.",
        locator="whole work", locator_type="work", supports="critique / limits of the construction thesis", verified=False),
 ],
 "MC-314": [
   dict(kind="BOOK", title_en="Symbolic Interactionism: Perspective and Method",
        title_fa="کنش متقابل نمادین: چشم‌انداز و روش",
        authors="Blumer, H.", year=1969, publisher="Englewood Cliffs, NJ: Prentice-Hall", doi=None,
        url="https://archive.org/details/symbolicinteract0000unse_t4t1",
        language="en", isbn=None,
        citation="Blumer, H. (1969). Symbolic interactionism: Perspective and method. Prentice-Hall.",
        locator="whole work", locator_type="work", supports="definition / three premises / interpretation", verified=True),
   dict(kind="BOOK", title_en="Mind, Self, and Society from the Standpoint of a Social Behaviorist",
        title_fa="ذهن، خود و جامعه از دیدگاه رفتارگرایی اجتماعی",
        authors="Mead, G. H.", year=1934, publisher="Chicago: University of Chicago Press", doi=None, url=None,
        language="en", isbn=None,
        citation="Mead, G. H. (1934). Mind, self, and society from the standpoint of a social behaviorist. University of Chicago Press.",
        locator="whole work", locator_type="work", supports="origin / self and generalized other", verified=False),
 ],
}

ENRICH = {
 "MC-311": {
   "summary": "سایبرنتیک (Cybernetics) علم کنترل و ارتباط در ماشین و موجود زنده است و کانون آن، مفهوم حلقهٔ بازخورد است: سیستمی که خروجی خود را می‌سنجد و رفتارش را بر پایهٔ آن اصلاح می‌کند. نوربرت وینر در «Cybernetics: Or Control and Communication in the Animal and the Machine» (۱۹۴۸، MIT Press) این چارچوب را بنیان گذاشت و ارتباط را از منظر تنظیم و کنترل، نه انتقال معنا، تحلیل کرد (Wiener, 1948).",
   "definition": "سایبرنتیک مطالعهٔ سیستم‌هایی است که با دریافت اطلاعات از محیط و بازخورد از نتایج خود، رفتارشان را تنظیم می‌کنند؛ مفهوم بنیادی آن بازخورد است و واحد تحلیلی آن، حلقهٔ کنترل-ارتباط، نه پیام منفرد (Wiener, 1948).",
   "main_problem": "موجود زنده و ماشین چگونه رفتار هدفمند را حفظ می‌کنند، در حالی که محیط و نتیجهٔ کنش پیوسته تغییر می‌کند؛ و چه منطق مشترکی میان تنظیم در ارگانیسم و کنترل در دستگاه مصنوعی وجود دارد؟",
   "mechanism": "سایبرنتیک بر پنج سازوکار بنا شده است. (۱) سیستم به‌عنوان جعبهٔ ورودی-خروجی: به‌جای گشودن جعبه به اجزای درونی، رفتار سیستم از رابطهٔ ورودی و خروجی توصیف می‌شود؛ همین چرخش روش‌شناختی، مقایسهٔ ارگانیسم و ماشین را ممکن می‌کند. (۲) بازخورد منفی: خروجی با هدف سنجیده و انحراف آن به ورودی بازگردانده می‌شود؛ نتیجه، خودتنظیمی و حفظ تعادل (هومئوستازی) است، همان‌گونه که ترموستات دما را ثابت نگه می‌دارد. (۳) بازخورد مثبت: تقویت انحراف به رشد یا ناپایداری می‌انجامد؛ بسیاری از پدیده‌های رسانه‌ای امروز — از وایرال‌شدن تا تشدید قطب‌بندی — از این نوع‌اند. (۴) اطلاعات به‌عنوان کاهش آنتروپی: وینر پیام را عاملی نظم‌بخش می‌دید که بی‌نظمی سیستم را می‌کاهد؛ ازاین‌رو اطلاعات و کنترل به هم گره می‌خورند. (۵) تنوع لازم: اشبی (۱۹۵۶) نشان داد که تنها تنوع می‌تواند تنوع را مهار کند و ظرفیت کنترل یک سیستم باید با پیچیدگی محیط آن هم‌خوان باشد؛ این اصل، بنیان تحلیل ظرفیت سازمانی است. در بستر رسانه، سازمان خبری را می‌توان حلقهٔ بازخورد دید: سنجش مخاطب، نظرسنجی و تحلیل ترافیک، ورودی تنظیمِ خط مشی تحریریه‌اند. وقتی بازخورد منفی کار کند، رسانه خطا را اصلاح می‌کند؛ وقتی بازخورد مثبت غالب شود — مانند الگوریتم پیشنهاد محتوا که تعامل را تقویت و تعامل بیشتر را پاداش می‌دهد — سیستم به سمت افراط حرکت می‌کند و اتاق پژواک محصول همین حلقه است.",
   "assumptions": [
     "رفتار سیستم را می‌توان از الگوی ورودی-خروجی و بازخورد توصیف کرد.",
     "اطلاعات، عامل کاهش بی‌نظمی و شرط کنترل مؤثر است.",
     "ظرفیت کنترل باید با تنوع و پیچیدگی محیط هم‌خوان باشد."
   ],
   "principles": [
     "بازخورد، سازوکار بنیادی خودتنظیمی است.",
     "کنترل بدون ظرفیت پردازش اطلاعات کافی ممکن نیست.",
     "مرز میان ناظر و سیستم در تحلیل مرتبهٔ دوم مسئله‌ساز می‌شود."
   ],
   "critiques": [
     "انتقال استعارهٔ کنترل از ماشین به جامعه، روابط قدرت و تعارض منافع را به «اختلال تنظیم» فرو می‌کاهد و سیاسی‌زدایی می‌کند.",
     "مدل، معنا و تفسیر را به اطلاعات کمّی تقلیل می‌دهد و از تفاوت میان سیگنال و فهم غافل است.",
     "وینر خود نسبت به کاربرد نظامی و اجتماعی سایبرنتیک هشدار داد؛ با این حال، ادبیات بعدی غالباً این هشدار را کنار گذاشت."
   ],
   "applications": [
     "تحلیل سازمان رسانه‌ای به‌عنوان سیستم بازخوردی.",
     "پژوهش دربارهٔ الگوریتم توصیه و تشدید قطب‌بندی به‌عنوان بازخورد مثبت.",
     "طراحی سنجش مخاطب و شاخص‌های عملکرد تحریریه.",
     "مدیریت بحران و ارتباطات ریسک با چرخهٔ اصلاح پیام."
   ],
   "evolution": "وینر (۱۹۴۸) چارچوب فنی را بنیان نهاد و در «The Human Use of Human Beings» (۱۹۵۰) آن را به جامعه گسترد؛ اشبی (۱۹۵۶) اصل تنوع لازم را افزود و سایبرنتیک مرتبهٔ دوم، ناظر را وارد سیستم کرد. این خط، بعدها به نظریهٔ سیستم‌های اجتماعی و پژوهش بازخورد الگوریتمی انجامید.",
   "key_concepts": ["بازخورد (feedback)", "هومئوستازی (homeostasis)", "تنوع لازم (requisite variety)", "آنتروپی و آنتروپی منفی (entropy/negentropy)", "حلقهٔ کنترل (control loop)", "سایبرنتیک مرتبهٔ دوم (second-order cybernetics)"],
   "studies": ["Wiener, N. (1948). Cybernetics: Or control and communication in the animal and the machine. MIT Press.", "Wiener, N. (1950). The human use of human beings: Cybernetics and society. Houghton Mifflin."],
   "detailed_analysis": "۱. بنیان و منطق نظری\nپرسش وینر در جنگ جهانی دوم شکل گرفت: چگونه می‌توان رفتار هدفمند را در ماشین و ارگانیسم با یک زبان توصیف کرد؟ پاسخ او، جایگزینی زبان «اجزا» با زبان «حلقهٔ بازخورد» بود؛ سیستمی که خطای خود را می‌سنجد و اصلاح می‌کند، بدون آنکه به درونش نگاه کنیم، هدفمند است.\n\n۲. از ماشین به جامعه\nوینر در ۱۹۵۰ پرسید که اتوماسیون و ارتباط ماشینی چه اثری بر انسان دارد. همین پرسش، سایبرنتیک را از مهندسی به علوم اجتماعی کشاند، اما با هزینه‌ای: استعارهٔ خودتنظیمی می‌تواند مسئولیت و قدرت را پنهان کند، زیرا جامعهٔ «خودتنظیم» ممکن است در واقع تحت کنترل گروهی خاص باشد.\n\n۳. پیوند رسانه‌ای و نقد\nبرای رسانه، سایبرنتیک زبان تحلیلی نیرومندی فراهم می‌کند: رسانه سیستم بازخوردی است و مخاطب، هم ورودی و هم خروجی آن. اما همین زبان، اگر به‌جای پرسش از منافع، به پرسش از «تنظیم بهینه» بسنده کند، نقد سیاسی را جایگزین مدیریت می‌کند. سایبرنتیک مرتبهٔ دوم دقیقاً برای ترمیم همین نقطه شکل گرفت."
 },
 "MC-312": {
   "summary": "«نظریهٔ عمومی سیستم‌ها» (General Systems Theory) می‌کوشد قوانین مشترک سازمان‌یافتگی را در سطوح مختلف واقعیت — از سلول تا سازمان و جامعه — صورت‌بندی کند و به‌جای تقلیل پدیده به اجزا، کل را واحد تحلیل بگیرد. لودویگ فون برتالانفی در «General System Theory: Foundations, Development, Applications» (۱۹۶۸، George Braziller) این برنامه را جامع‌ترین شکل خود رساند (von Bertalanffy, 1968).",
   "definition": "نظریهٔ عمومی سیستم‌ها مطالعهٔ اصول و قوانینی است که برای سیستم‌ها، مستقل از نوع اجزا و سطح سازمان‌یافتگی، صادق‌اند؛ سیستم مجموعه‌ای از عناصر در تعامل است که خواص کل آن به خواص اجزا فروکاستنی نیست (von Bertalanffy, 1968).",
   "main_problem": "آیا می‌توان زبان مشترکی برای تحلیل سازمان‌یافتگی در زیست‌شناسی، روان‌شناسی، سازمان و جامعه ساخت تا رشته‌های تخصصی از انزوا خارج شوند و پدیده‌های پیچیده به‌جای تقلیل به اجزا، در سطح کل فهمیده شوند؟",
   "mechanism": "برنامهٔ برتالانفی بر پنج مفهوم استوار است. (۱) سیستم به‌عنوان کل متعامل: عناصر از طریق روابط به هم وابسته‌اند و تغییر یکی بر کل اثر می‌گذارد؛ بنابراین تحلیل باید روابط را در مرکز بگذارد، نه فقط اجزا را. (۲) سیستم باز: برخلاف سیستم بسته که به تعادل ترمودینامیکی می‌رسد، سیستم باز با محیط مبادلهٔ ماده و انرژی و اطلاعات دارد و می‌تواند در «حالت پایدار» (Fließgleichgewicht) بماند؛ همین مفهوم، توضیح می‌دهد که چگونه موجود زنده با وجود افزایش آنتروپی محیط، نظم خود را حفظ می‌کند. (۳) هم‌پایانی: سیستم‌های باز می‌توانند از شرایط آغازین متفاوت و مسیرهای گوناگون به حالت نهایی یکسان برسند؛ نتیجه، ضرورتاً از شرایط اولیه قابل پیش‌بینی نیست. (۴) هم‌ریختی: ساختارهای مشابه در سطوح مختلف — مانند سلسله‌مراتب و بازخورد — امکان انتقال مفاهیم میان رشته‌ها را فراهم می‌کنند. (۵) کل‌گرایی روش‌شناختی: خواص نوظهور کل، از جمع خواص اجزا حاصل نمی‌شود. در بستر رسانه، این چارچوب رسانه را به‌عنوان زیرسیستمی از نظام اجتماعی می‌بیند که با اقتصاد، سیاست و فرهنگ مبادله می‌کند؛ خبرگزاری، شبکهٔ توزیع و مخاطب، اجزای یک سیستم بازند و اختلال در یک زیرسیستم — قطع اینترنت، تحریم تبلیغات یا سانسور — به کل نظام انتشار منتقل می‌شود. مفهوم هم‌پایانی نیز توضیح می‌دهد که رسانه‌های با ساختار اولیهٔ متفاوت می‌توانند به الگوهای مشابه مالکیت و محتوا برسند.",
   "assumptions": [
     "قوانین سازمان‌یافتگی در سطوح مختلف واقعیت هم‌ریخت‌اند.",
     "سیستم‌های زنده و اجتماعی به‌صورت باز با محیط مبادله می‌کنند.",
     "خواص کل به خواص اجزا فروکاستنی نیستند."
   ],
   "principles": [
     "کل، بیش از جمع اجزاست.",
     "سیستم باز، نظم خود را با مبادلهٔ مداوم با محیط حفظ می‌کند.",
     "هم‌پایانی، پیش‌بینی خطی از شرایط اولیه را ناممکن می‌کند."
   ],
   "critiques": [
     "کلیت نظریه، آن را به سطح استعاره و اصول عام فرومی‌کاهد و آزمون‌پذیری تجربی ضعیفی دارد.",
     "تأکید بر تعادل و نظم، تعارض، تغییر رادیکال و قدرت را در حاشیه نگه می‌دارد.",
     "هم‌ریختی میان سیستم‌های زیستی و اجتماعی، تفاوت‌های بنیادی معنا و عاملیت را نادیده می‌گیرد."
   ],
   "applications": [
     "تحلیل رسانه به‌عنوان زیرسیستم نظام اجتماعی.",
     "پژوهش دربارهٔ اثر اختلال در یک زیرسیستم بر کل زنجیرهٔ انتشار.",
     "طراحی سازمان رسانه‌ای با تمرکز بر روابط میان واحدها.",
     "مطالعهٔ هم‌پایانی الگوهای مالکیت و محتوا در بافت‌های متفاوت."
   ],
   "evolution": "برتالانفی ایدهٔ «سیستم باز» را از دههٔ ۱۹۳۰ و در مقالهٔ ۱۹۵۰ صورت‌بندی کرد و در ۱۹۶۸ به کتاب جامع رساند؛ لومان آن را به‌صورت گزینشی برای نظریهٔ سیستم‌های اجتماعی به‌کار گرفت و نقدهای ایدئولوژیک (لیلی‌نفلد، ۱۹۷۸) بر ادعای کلیت آن شکل گرفت.",
   "key_concepts": ["سیستم باز (open system)", "حالت پایدار (steady state)", "هم‌پایانی (equifinality)", "هم‌ریختی (isomorphism)", "خواص نوظهور (emergent properties)", "کل‌گرایی (holism)"],
   "studies": ["von Bertalanffy, L. (1968). General system theory: Foundations, development, applications. George Braziller.", "von Bertalanffy, L. (1950). An outline of general system theory. British Journal for the Philosophy of Science, 1(2), 134-165."],
   "detailed_analysis": "۱. بنیان و منطق نظری\nبرتالانفی زیست‌شناسی را نقطهٔ آغاز گرفت: موجود زنده نه ماشینی است که با قوانین فیزیکی توضیح داده شود و نه مجموعه‌ای بی‌نظم؛ سیستمی است که با محیط مبادله می‌کند و نظم خود را در حرکت حفظ می‌کند. از این مشاهده، ادعای بزرگ‌تری زاده شد: قوانین مشترک سازمان‌یافتگی در همهٔ سطوح.\n\n۲. جاه‌طلبی و هزینهٔ آن\nنظریهٔ عمومی سیستم‌ها می‌خواست زبان مشترک رشته‌ها بسازد. اما هرچه ادعا کلی‌تر شد، آزمون‌پذیری کمتر شد؛ نتیجه این شد که بخشی از علوم اجتماعی، آن را به‌عنوان چارچوب مفهومی پذیرفت و در مقام نظریهٔ تجربی، به آن بدگمان ماند.\n\n۳. پیوند رسانه‌ای و نقد\nبرای مطالعهٔ رسانه، ارزش نظریه در همین چارچوب‌بودن است: به‌جای تحلیل منفرد پیام یا مخاطب، زنجیرهٔ کامل را می‌بیند. اما نقد لی‌لی‌نفلد همچنان معتبر است: زبانی که همه‌چیز را «سیستم» بنامد، مرز میان نظم و ایدئولوژی را محو می‌کند."
 },
 "MC-313": {
   "summary": "برساخت‌گرایی اجتماعی (Social Constructivism) می‌گوید واقعیت اجتماعی نه دادهٔ پیشینی و طبیعی، بلکه محصول فرایندهای انسانی است: انسان‌ها جهان را با تعامل، نماد و نهادسازی می‌سازند و سپس آن را عینی و طبیعی تجربه می‌کنند. پیتر برگر و توماس لوکمان در «The Social Construction of Reality» (۱۹۶۶، Doubleday) این دیدگاه را در قالب جامعه‌شناسی معرفت صورت‌بندی کردند (Berger & Luckmann, 1966).",
   "definition": "برساخت‌گرایی اجتماعی نظری است که معنا، نهاد و مقوله‌های اجتماعی را نتیجهٔ کنش متقابل انسانی و توافق نمادین می‌داند، نه بازتاب ضروری واقعیت طبیعی؛ آنچه «واقعی» تلقی می‌شود، از طریق عینیتیابی و مشروعیت‌بخشی حفظ می‌شود (Berger & Luckmann, 1966).",
   "main_problem": "چگونه معنای ذهنی کنشگران به واقعیتی عینی و الزام‌آور بدل می‌شود؛ و چگونه نظم اجتماعی هم‌زمان ساختهٔ انسان و تجربه‌شده به‌عنوان واقعیتی مستقل است؟",
   "mechanism": "برگر و لوکمان دیالکتیکی سه‌گانه ترسیم می‌کنند. (۱) برونی‌سازی: انسان به‌طور فعال معنا و کنش را به بیرون از خود می‌افکند؛ جامعه محصول انسان است. (۲) عینیتیابی: کنش‌های تکرارشده عادت‌وار و سپس نهادینه می‌شوند، الگوها تیپ‌بندی می‌شوند و نقش‌ها شکل می‌گیرند؛ پس از آن، نسل بعد با نهادها به‌عنوان واقعیتی از پیش موجود روبه‌رو می‌شود، همان‌گونه که با زبان و قوانین روبه‌رو می‌شود. (۳) درونی‌سازی: فرد از طریق اجتماعی‌پذیری اولیه (خانواده) و ثانویه (مدرسه، رسانه، حرفه) جهان نمادین را می‌آموزد و آن را بدیهی می‌پندارد. (۴) مشروعیت‌بخشی: نهادها برای توجیه خود به تبیین‌های عقلانی، داستان‌های اسطوره‌ای و «جهان نمادین» متوسل می‌شوند؛ جهان نمادین، مرجع نهایی معنای همه‌چیز است. (۵) زبان: زبان مخزن اصلی عینیتیابی است و تجربه را طبقه‌بندی می‌کند؛ بی‌زبان، واقعیت اجتماعی منتقل نمی‌شود. در بستر رسانه، این چارچوب توضیح می‌دهد که چگونه یک رویداد به «خبر» بدل می‌شود: خبر، گزارش خام واقعیت نیست، بلکه محصول تیپ‌بندی‌های حرفه‌ای و مشروعیت‌یافته است. تاجمن (۱۹۷۸) در «Making News» نشان داد که روتین‌های خبری، «واقعیت» را می‌سازند؛ به همین معنا، رسانه سازندهٔ واقعیت و نه فقط آینهٔ آن است.",
   "assumptions": [
     "معنا در تعامل اجتماعی و از طریق زبان شکل می‌گیرد.",
     "نهادها و مقوله‌ها، انسان‌ساخته‌اند اما به‌عنوان واقعیت بیرونی تجربه می‌شوند.",
     "دانش روزمره، توزیع نابرابر و مشروعیت‌مند دارد و در جهان نمادین سازمان می‌یابد."
   ],
   "principles": [
     "جامعه محصول انسان است و انسان محصول جامعه.",
     "عینیتیابی، ساختهٔ انسانی را به واقعیت طبیعی بدل می‌کند.",
     "زبان و روتین، حاملان اصلی جهان اجتماعی‌اند."
   ],
   "critiques": [
     "نظریه گرایش به نسبیت‌گرایی معرفتی دارد و معیار مستقل ارزیابی رقابتی ادعاهای واقعیت را تضعیف می‌کند.",
     "کم‌توجهی به نقش تناقض‌های مادی و قدرت باعث می‌شود برساخت‌گرایی برای تحلیل سیاست رسانه ناتوان باشد.",
     "کاربرد عامه‌پسند آن به این جملهٔ ساده فروکاسته شده است که «همه چیز ساخته شده است»؛ هاکینگ (۱۹۹۹) نشان داد که این ادعا فقط با مشخص کردنی که «چه چیزی» و «در برابر چه کسانی» معنا دارد."
   ],
   "applications": [
     "تحلیل خبر و بازنمایی به‌عنوان ساخت واقعیت.",
     "پژوهش دربارهٔ بازنمایی جنسیت، قومیت و سلامت در رسانه.",
     "مطالعهٔ بحران اعتبار رسانه و فرایندهای مشروعیت‌بخشی.",
     "طراحی پیام در روابط عمومی و برندسازی معنا."
   ],
   "evolution": "برگر و لوکمان (۱۹۶۶) رویکرد را در جامعه‌شناسی معرفت تثبیت کردند؛ توماس تئودور تاجمن (۱۹۷۸) آن را به تولید خبر تعمیم داد؛ هاکینگ (۱۹۹۹) نقدی روش‌شناسانه بر دامنهٔ آن افزود و در دههٔ اخیر، پژوهش «خبر ساختگی» و «واقعیت‌مرجعی» دوباره به این چارچوب بازگشته است.",
   "key_concepts": ["برونی‌سازی (externalization)", "عینیتیابی (objectivation)", "درونی‌سازی (internalization)", "نهادینه‌شدن (institutionalization)", "جهان نمادین (symbolic universe)", "مشروعیت‌بخشی (legitimation)"],
   "studies": ["Berger, P. L., & Luckmann, T. (1966). The social construction of reality. Doubleday.", "Hacking, I. (1999). The social construction of what? Harvard University Press."],
   "detailed_analysis": "۱. بنیان و منطق نظری\nبرگر و لوکمان مسئلهٔ دیرینهٔ جامعه‌شناسی هنجارها و معرفت را از زاویهٔ دیگری طرح کردند: نه «چه چیزی واقعی است»، بلکه «چگونه چیزی واقعی می‌شود». پاسخ آنان، فرایندی است که در آن کنش به عادت، عادت به نهاد، نهاد به مشروعیت و مشروعیت به جهان نمادین تبدیل می‌شود.\n\n۲. نقطهٔ قوت و آسیب\nقوت نظریه در نشان دادن نبود ضرورت طبیعی در نظم اجتماعی است؛ نظم می‌توانست نباشد و می‌تواند تغییر کند. آسیب آن، لغزش به سمت این ادعاست که واقعیت زیستی یا علّی نیز فقط «ساخته» است، ادعایی که نه با متن برگر و لوکمان خوانا است و نه از نقد هاکینگ جان سالم به در می‌برد.\n\n۳. پیوند رسانه‌ای\nرسانه در دو مرحله در این فرایند دخیل است: در تولید (انتخاب و تیپ‌بندی رویداد) و در مشروعیت‌بخشی (اختصاص چارچوب تفسیری به آن). این همان حلقه‌ای است که پژوهش چارچوب‌بندی خبر بعدها آن را به‌تفصیل بررسی کرد."
 },
 "MC-314": {
   "summary": "کنش متقابل نمادین (Symbolic Interactionism) کنش انسانی را بر پایهٔ معانی‌ای توضیح می‌دهد که چیزها برای افراد دارند؛ این معانی در تعامل شکل می‌گیرند و در فرایند تفسیر مداوم تعدیل می‌شوند. هربرت بلومر در «Symbolic Interactionism: Perspective and Method» (۱۹۶۹، Prentice-Hall) سه اصل این رویکرد را تدوین کرد و ریشهٔ آن در کارهای جرج هربرت مید (۱۹۳۴) است (Blumer, 1969).",
   "definition": "کنش متقابل نمادین رویکردی است که رفتار اجتماعی را نتیجهٔ تفسیر معانی مشترک، ایفای نقش و مذاکرهٔ نمادین می‌داند؛ انسان به محرک واکنش مکانیکی نمی‌دهد، بلکه ابتدا آن را تفسیر می‌کند و سپس کنش را شکل می‌دهد (Blumer, 1969).",
   "main_problem": "چگونه نظم اجتماعی از تعامل روزمرهٔ افرادی پدید می‌آید که هر یک معنای موقعیت را تفسیر می‌کنند؛ و چگونه خودِ فرد در همین تعامل شکل می‌گیرد و تغییر می‌کند؟",
   "mechanism": "رویکرد بر سه اصل بلومر و مکانیسم خود بنا شده است. (۱) انسان‌ها بر پایهٔ معانی چیزها کنش می‌کنند؛ شیء، رفتار یا شخص، به‌واسطهٔ معنایی که برای کنشگر دارد، بر او اثر می‌گذارد. (۲) معنا از تعامل اجتماعی برمی‌آید، نه از ذات اشیا؛ همین‌جا رویکرد از رفتارگرایی و از تعریف ذاتی پدیده‌ها جدا می‌شود. (۳) معنا در فرایند تفسیر تعدیل می‌شود: کنشگر با خود گفت‌وگو می‌کند و معنای موقعیت را تغییر می‌دهد؛ به همین دلیل کنش، خطی و قابل پیش‌بینی مکانیکی نیست. (۴) خود و دیگری تعمیم‌یافته: مید نشان داد که فرد با ایفای نقش دیگران، «دیگری تعمیم‌یافته» را در خود می‌سازد و میان «منِ کنشگر» و «خودِ اجتماعی» گفت‌وگو برقرار می‌کند؛ خود، محصول همین گفت‌وگوی درونی است. (۵) موقعیت و مذاکره: نظم، پیش از کنش تعیین نمی‌شود بلکه در خود تعامل و از طریق تعریف مشترک موقعیت ساخته می‌شود. در بستر رسانه، این چارچوب توضیح می‌دهد که مخاطب قرص‌پذیر نیست: او پیام را بر پایهٔ تجربه و مناسبات خود تفسیر می‌کند و ممکن است معنایی متفاوت با نیت تولیدکننده بسازد. مطالعهٔ مصرف‌کنندگان محتوا، تعامل فرااجتماعی با شخصیت‌های رسانه‌ای و ساخته‌شدن هویت در شبکه‌های اجتماعی، همه بر همین منطق استوارند.",
   "assumptions": [
     "معنا، محصول تعامل است و نه ویژگی ذاتی اشیا.",
     "کنشگر در فرایند تفسیر فعال است و معنای موقعیت را مذاکره می‌کند.",
     "خود، در گفت‌وگوی درونی با دیگری تعمیم‌یافته شکل می‌گیرد."
   ],
   "principles": [
     "انسان بر پایهٔ معانی کنش می‌کند.",
     "معنا از تعامل برمی‌آید، نه از ذات اشیا.",
     "معنا در تفسیر مداوم تعدیل می‌شود."
   ],
   "critiques": [
     "رویکرد، ساختارهای کلان قدرت، طبقه و اقتصاد را نادیده می‌گیرد و نظم اجتماعی را بیش از حد مذاکره‌ای می‌بیند.",
     "روش‌های کیفی آن، تعمیم و پیش‌بینی تجربی را دشوار می‌کند.",
     "تأکید بر عاملیت فردی ممکن است مسئولیت ساختار در نابرابری را از نظر پنهان کند."
   ],
   "applications": [
     "پژوهش مخاطب و تفسیر رقیب از پیام رسانه‌ای.",
     "تحلیل تعامل فرااجتماعی و هواداری در رسانه‌های شبکه‌ای.",
     "مطالعهٔ هویت و خودنمایی در پلتفرم‌های اجتماعی.",
     "مطالعهٔ روش‌های کیفی و مشاهدهٔ مشارکتی در خبرنگاری."
   ],
   "evolution": "ریشهٔ رویکرد در مید (۱۹۳۴) و کولی است؛ بلومر (۱۹۶۹) آن را به‌عنوان برنامهٔ روش‌شناختی تدوین کرد؛ بعدها پژوهش مخاطب و مطالعات فرهنگی، مفاهیم تفسیر و مذاکرهٔ معنا را به مطالعات رسانه وارد کردند.",
   "key_concepts": ["معنا (meaning)", "ایفای نقش (role-taking)", "دیگری تعمیم‌یافته (generalized other)", "من و خود (I and me)", "تعریف موقعیت (definition of the situation)", "مذاکرهٔ معنا (negotiation of meaning)"],
   "studies": ["Blumer, H. (1969). Symbolic interactionism: Perspective and method. Prentice-Hall.", "Mead, G. H. (1934). Mind, self, and society. University of Chicago Press."],
   "detailed_analysis": "۱. بنیان و منطق نظری\nمید پرسید که خودآگاهی از کجا می‌آید. پاسخ او، اجتماع بود: فرد با پذیرش نگرش دیگران نسبت به خود، «خود» می‌سازد. بلومر این بینش را از فلسفه به روش‌شناسی اجتماعی منتقل کرد و سه اصل معروف را از آن استخراج کرد.\n\n۲. تفاوت با مدل انتقالی\nدر مدل انتقالی، پیام از فرستنده به گیرنده منتقل می‌شود و اثر آن اندازه‌گیری می‌شود. در کنش متقابل نمادین، گیرنده مترجم است: او پیام را در جهان معنایی خود جای می‌دهد و ممکن است آن را بپذیرد، رد کند یا دگرگون سازد. این تفاوت، بنیان تفکر مخاطب فعال است.\n\n۳. پیوند رسانه‌ای و نقد\nنقطهٔ قوت رویکرد در توضیح تفسیر و هویت است و نقطهٔ ضعف آن در قدرت: پلتفرم‌ها ساختارهایی دارند که میدان تفسیر را نامتقارن می‌کنند. کنش متقابل نمادین بدون افزودن تحلیل ساختاری، ممکن است عاملیت مخاطب را بزرگ‌تر از آنچه هست نشان دهد."
 },
}

REQUIRED_SECTIONS = ["summary", "definition", "main_problem", "mechanism", "assumptions",
                     "principles", "critiques", "applications", "evolution", "key_concepts",
                     "theorists", "model", "studies"]

def wc(v):
    if isinstance(v, str): return len(v.split())
    if isinstance(v, list):
        n = 0
        for it in v:
            if isinstance(it, str): n += len(it.split())
            elif isinstance(it, dict): n += len(' '.join(str(x) for x in it.values()).split())
        return n
    if isinstance(v, dict): return len(' '.join(str(x) for x in v.values()).split())
    return 0

def has_content(v):
    if v is None: return False
    if isinstance(v, str): return len(v.strip()) > 10
    if isinstance(v, (list, dict)): return len(v) > 0
    return True

def rubric(p, n_verified, n_sources, n_relations):
    detail = {}
    present = [k for k in REQUIRED_SECTIONS if has_content(p.get(k))]
    detail["structure_15"] = round(15 * min(1, len(present)/7))
    words = sum(wc(p.get(k)) for k in ["summary","definition","main_problem","mechanism",
                "critiques","applications","evolution","key_concepts","principles","studies","assumptions"])
    a = 15 if words>=500 else 13 if words>=300 else 11 if words>=180 else 8 if words>=100 else 3
    detail["analysis_15"] = a
    if n_verified>=1 and n_sources>=2: detail["citation_20"] = 20
    elif n_verified>=1: detail["citation_20"] = 17
    elif n_sources>=1: detail["citation_20"] = 10
    else: detail["citation_20"] = 0
    acc = 0
    if has_content(p.get("summary")) or has_content(p.get("definition")): acc += 10
    if n_verified>=1: acc += 9
    if len(present)>=6: acc += 6
    detail["accuracy_25_auto"] = min(25, acc)
    detail["relations_10"] = 10 if n_relations>=1 else 6
    detail["classification_5"] = 5 if (p.get("field") or p.get("mapping")) else 2
    detail["clarity_5"] = 5 if has_content(p.get("summary")) else 2
    detail["currency_5"] = 5
    return min(100, sum(detail.values())), detail, words

def main():
    c = pymysql.connect(host="127.0.0.1", user="root", password="433700", database=DB, charset="utf8mb4", autocommit=False)
    cur = c.cursor()
    codes = ["MC-311", "MC-312", "MC-313", "MC-314"]
    cur.execute("SELECT id, code, properties FROM kb_entities WHERE code IN (%s)" % ",".join(["%s"]*len(codes)), codes)
    rows = {code:(eid, json.loads(pr)) for (eid, code, pr) in cur.fetchall()}
    with open(BACKUP, "w", encoding="utf-8") as f:
        json.dump([{"code": cd, "props": rows[cd][1]} for cd in codes if cd in rows], f, ensure_ascii=False, indent=1)
    print("backup ->", len(rows), "rows")

    for code in codes:
        eid, p = rows[code]
        p["critique"] = "\n".join(ENRICH[code]["critiques"])
        p["example"] = ENRICH[code]["applications"][0] + "؛ " + ENRICH[code]["applications"][1]
        for k, v in ENRICH[code].items():
            p[k] = v
        if not has_content(p.get("definition")) and has_content(p.get("summary")):
            p["definition"] = p["summary"]
        spec = S[code]
        p["sources"] = [dict(citation=s["citation"], language=("انگلیسی" if s["language"]=="en" else "فارسی"),
                              doi=s.get("doi") or "", url=s.get("url") or "", year=s.get("year")) for s in spec]
        p["citations"] = [dict(source=s["citation"], locator=s["locator"], supports=s["supports"],
                               verified=bool(s.get("verified"))) for s in spec]
        n_sources = len(spec)
        n_verified = sum(1 for s in spec if s.get("verified"))
        cur.execute("SELECT COUNT(*) FROM kb_relations r JOIN kb_entities a ON r.source_id=a.id JOIN kb_entities b ON r.target_id=b.id WHERE a.code=%s OR b.code=%s", (code, code))
        n_relations = cur.fetchone()[0]
        score, detail, words = rubric(p, n_verified, n_sources, n_relations)
        p["quality_score"] = score
        p["quality_assessment"] = dict(breakdown=detail, total=score,
            method="SPEC §6.1 auto-structural (accuracy is auto-credit, NOT human verification)",
            scored_at=NOW, scored_by=STAMP)
        p["status_scientific_note"] = "score is structural/citation-based; requires human expert review for scientific verification (SPEC §6.4)"
        p["updated_at"] = NOW; p["updated_by"] = STAMP
        cur.execute("UPDATE kb_entities SET properties=%s, version=version+1, updated_at=%s, updated_by=%s WHERE id=%s",
                    (json.dumps(p, ensure_ascii=False), NOW, STAMP, eid))
        for s in spec:
            sid = None
            if s.get("doi"):
                cur.execute("SELECT id FROM kb_sources WHERE doi=%s", (s["doi"],))
                r = cur.fetchone(); sid = r[0] if r else None
            if sid is None:
                cur.execute("SELECT id FROM kb_sources WHERE title_en=%s AND year=%s", (s["title_en"], s.get("year")))
                r = cur.fetchone(); sid = r[0] if r else None
            if sid is None:
                cur.execute("""INSERT INTO kb_sources (kind,title_fa,title_en,year,publisher,doi,isbn,url,language,access_type,bibliographic)
                                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                    (s["kind"], s.get("title_fa"), s["title_en"], s.get("year"), s.get("publisher"),
                     s.get("doi"), s.get("isbn"), s.get("url"), s.get("language"),
                     "open" if (s.get("doi") or s.get("url")) else "unknown",
                     json.dumps({"authors": s.get("authors"), "citation": s["citation"]}, ensure_ascii=False)))
                sid = cur.lastrowid
            cur.execute("SELECT 1 FROM kb_evidence e WHERE e.about_code=%s AND e.source_id=%s LIMIT 1", (code, sid))
            if cur.fetchone(): continue
            lt = "PAGE" if s.get("locator_type") == "page_range" else ("CHAPTER" if s.get("locator_type") == "CHAPTER" else "SECTION")
            cur.execute("""INSERT INTO kb_citations (source_id,locator_type,locator_value,paraphrase,citation_style,language,accessed_at)
                            VALUES (%s,%s,%s,%s,'apa',%s,%s)""",
                        (sid, lt, s.get("locator"), "پشتیبانی از بخش: "+s.get("supports",""), s.get("language","en"), NOW))
            cid = cur.lastrowid
            cur.execute("""INSERT INTO kb_evidence (source_id,citation_id,about_code,evidence_type,evidence_summary,locator,verification_status,extraction_method,direction)
                            VALUES (%s,%s,%s,'bibliographic_reference',%s,%s,%s,'ai_extraction','supports')""",
                        (sid, cid, code, s["citation"], s.get("locator"), "verified" if s.get("verified") else "unverified"))
        cur.execute("SELECT COALESCE(MAX(version),0)+1 FROM kb_entity_versions WHERE entity_id=%s", (eid,))
        ver = cur.fetchone()[0]
        cur.execute("INSERT INTO kb_entity_versions (entity_id, version, snapshot, change_reason, changed_by, created_at) VALUES (%s,%s,%s,%s,%s,%s)",
                    (eid, ver, json.dumps({"quality_score": score, "words": words, "sources": n_sources, "verified": n_verified}, ensure_ascii=False),
                     "documented sourcing + rubric score; fixed mismatched boilerplate critique/example", STAMP, NOW))
        cur.execute("INSERT INTO kb_audit_log (entity_code, action, detail, source) VALUES (%s,%s,%s,%s)",
                    (code, "DOC_ENRICH", json.dumps({"quality_score": score, "words": words, "sources": n_sources, "verified": n_verified, "breakdown": detail}, ensure_ascii=False), STAMP))
        print(f"{code}: score={score} words={words} sources={n_sources} verified={n_verified} relations={n_relations} | {detail}")
    c.commit()
    c.close()
    print("BATCH61 THEORY DONE")

if __name__ == "__main__":
    main()
