# -*- coding: utf-8 -*-
"""Batch 66: MC-343 (Simmel, forms & space), MC-347 (Death of the Author),
MC-349 (Foucauldian discourse analysis), MC-351 (social semiotics).
All four carry mismatched boilerplate in critique/example -> overwritten."""
import pymysql, json

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch66-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch66_theory.json"

S = {
 "MC-343": [
   dict(kind="BOOK_CHAPTER", title_en="The Metropolis and Mental Life",
        title_fa="کلان‌شهر و حیات ذهنی",
        authors="Simmel, G.", year=1903,
        publisher="The Free Press (in K. Wolff, Ed., The Sociology of Georg Simmel, 1950)",
        doi=None, url="https://www.tandfonline.com/doi/full/10.1080/1369118X.2015.1042394",
        language="en", isbn=None,
        citation="Simmel, G. (1950). The metropolis and mental life. In K. Wolff (Ed.), The sociology of Georg Simmel (pp. 409-426). The Free Press. (Original lecture 1903)",
        locator="pp. 409-426", locator_type="page_range",
        supports="definition / mechanism / origin", verified=True),
   dict(kind="BOOK", title_en="Soziologie: Untersuchungen über die Formen der Vergesellschaftung",
        title_fa="جامعه‌شناسی: پژوهش در صورت‌های اجتماعی‌شدن",
        authors="Simmel, G.", year=1908,
        publisher="Duncker & Humblot", doi=None, url=None, language="de", isbn=None,
        citation="Simmel, G. (1908). Soziologie: Untersuchungen über die Formen der Vergesellschaftung. Duncker & Humblot.",
        locator="Der Raum und die räumlichen Ordnungen der Gesellschaft", locator_type="CHAPTER",
        supports="space / the stranger / sociology of the senses", verified=False),
 ],
 "MC-347": [
   dict(kind="BOOK_CHAPTER", title_en="The Death of the Author",
        title_fa="مرگ مؤلف",
        authors="Barthes, R. (trans. S. Heath)", year=1968,
        publisher="Hill & Wang (in Image-Music-Text, 1977)",
        doi=None, url=None, language="en", isbn=None,
        citation="Barthes, R. (1977). The death of the author. In Image, music, text (S. Heath, Trans., pp. 142-148). Hill & Wang. (Original work published 1968 in Manteia, 5)",
        locator="pp. 142-148", locator_type="page_range",
        supports="definition / mechanism / reader", verified=True),
   dict(kind="JOURNAL_ARTICLE", title_en="What Is an Author?",
        title_fa="نویسنده چیست؟",
        authors="Foucault, M.", year=1969,
        publisher="Bulletin de la Société française de philosophie, 63(3), 73-104",
        doi=None, url=None, language="fr", isbn=None,
        citation="Foucault, M. (1969). Qu'est-ce qu'un auteur? Bulletin de la Société française de philosophie, 63(3), 73-104.",
        locator="pp. 73-104", locator_type="page_range",
        supports="evolution / author function", verified=False),
 ],
 "MC-349": [
   dict(kind="BOOK", title_en="The Archaeology of Knowledge",
        title_fa="دیرینه‌شناسی دانش",
        authors="Foucault, M.", year=1969,
        publisher="Éditions Gallimard (English trans. Tavistock, 1972)", doi=None, url=None,
        language="fr", isbn=None,
        citation="Foucault, M. (1969). L'archéologie du savoir. Éditions Gallimard.",
        locator="whole work", locator_type="work",
        supports="definition / statement / discursive formation / archive", verified=True),
   dict(kind="BOOK", title_en="Discipline and Punish: The Birth of the Prison",
        title_fa="مراقبت و تنبیه: تولد زندان",
        authors="Foucault, M.", year=1975,
        publisher="Éditions Gallimard", doi=None, url=None, language="fr", isbn=None,
        citation="Foucault, M. (1975). Surveiller et punir: Naissance de la prison. Éditions Gallimard.",
        locator="whole work", locator_type="work",
        supports="evolution / power-knowledge", verified=False),
 ],
 "MC-351": [
   dict(kind="BOOK", title_en="Social Semiotics",
        title_fa="نشانه‌شناسی اجتماعی",
        authors="Hodge, R., & Kress, G.", year=1988,
        publisher="Polity Press (Cornell University Press in the US)",
        doi=None, url="https://books.google.com/books/about/Social_Semiotics.html?id=UPXangEACAAJ",
        language="en", isbn="9780745603735",
        citation="Hodge, R., & Kress, G. (1988). Social semiotics. Polity Press.",
        locator="whole work", locator_type="work",
        supports="definition / semiotic resources / logonomic system", verified=True),
   dict(kind="BOOK", title_en="Reading Images: The Grammar of Visual Design",
        title_fa="خواندن تصاویر: دستور زبان طراحی بصری",
        authors="Kress, G., & van Leeuwen, T.", year=2006,
        publisher="Routledge (2nd ed.)", doi=None, url=None, language="en", isbn=None,
        citation="Kress, G., & van Leeuwen, T. (2006). Reading images: The grammar of visual design (2nd ed.). Routledge.",
        locator="whole work", locator_type="work",
        supports="evolution / visual grammar", verified=False),
 ],
}

VOID = "در بستر رسانه، "
ENRICH = {
 "MC-343": {
  "summary": "(زیمل، ۱۹۰۳/۱۹۵۰؛ ۱۹۰۸) جامعه را نه مجموعه‌ای از افراد و نه محصول ساختارهای کلان، بلکه مجموعه‌ای از «صورت‌های اجتماعی‌شدن» می‌بیند: قالب‌های تکرارشونده‌ای که آدمیان از طریق آن‌ها به یکدیگر پیوند می‌خورند. صورت‌های کوچک — نگاه رد و بدل‌شده، پول، فاصلهٔ فضایی، غریبه — حاملان اصلی معنا و نظم اجتماعی‌اند؛ و فضا، نه ظرف بی‌اثر کنش، بلکه سازندهٔ آن است.",
  "definition": "جامعه‌شناسی صورت‌ها و فضا در سنت زیمل، مطالعهٔ قالب‌های پایدار تعامل (احساس، مبادله، سلسله‌مراتب، هم‌جواری و دوری) و شیوه‌ای است که چیدمان فضایی و حسی این قالب‌ها را ممکن یا دگرگون می‌کند.",
  "main_problem": "چگونه پیوند اجتماعی در جهانی که در آن فرد مدرن بیش از هر زمان تنها، متحرک و تحریک‌شده است، همچنان ممکن می‌ماند؟ زیمل این پرسش را با واژگون‌کردن پرسش کلاسیک «جامعه چیست؟» به «اجتماع‌شدن چگونه رخ می‌دهد؟» صورت‌بندی می‌کند.",
  "mechanism": "\n".join([
   "(۱) صورت در برابر محتوا: آنچه جامعه‌شناس می‌خواند نه انگیزهٔ منفرد، بلکه قالبی است که انگیزه‌ها در آن به هم می‌رسند — همان‌گونه که زبان قالبی است مستقل از آنچه هر گوینده می‌خواهد بگوید.",
   "(۲) فضای اجتماعی: زیمل در «جامعه‌شناسی» (۱۹۰۸) نشان می‌دهد فضا بی‌واسطه اجتماعی نیست؛ مرز، همسایگی، پل و در، و «فاصله» ابزارهایی‌اند که گروه‌ها با آن‌ها نظم خود را می‌سازند. صورت‌های فضایی، صورت‌های اجتماعی‌اند.",
   "(۳) غریبه: کسی که امروز می‌آید و فردا می‌ماند؛ ترکیبی از نزدیکی و دوری که او را در موقعیتی سیال و در عین حال توانا در داوری بی‌طرف قرار می‌دهد.",
   "(۴) حساسیت حسی و sociability: در «کاوش در جامعه‌شناسی حواس»، نگاه و شنیدن مبنای آگاهی متقابل‌اند؛ و «معاشرت» صورت بازی‌گونهٔ اجتماع است که در آن تعامل، هدف خودش می‌شود.",
   "(۵) کلان‌شهر و نگرش بی‌اعتنا: ازدیاد محرک‌های عصبی در کلان‌شهر، سپری حسی («blasé») می‌سازد و اقتصاد پول، فاصله‌گذاری عقلانی را جایگزین رابطهٔ شخصی می‌کند؛ پول نخستین رسانهٔ انتزاعیِ فاصله و مبادله است.",
   VOID + "زیمل به ما می‌آموزد رسانه را همچون صورت اجتماعی و همچون فضا بخوانیم: صفحهٔ نمایش، نه ظرف محتوا بلکه چیدمانی از مرز، فاصله، نگاه و غریبه است؛ و «اسکرول» خود قالبی است که نزدیکی و دوری را هم‌زمان تولید می‌کند.",
  ]),
  "assumptions": [
   "جامعه پیش از هر چیز در تعامل رخ می‌دهد؛ ساختار بدون صورت‌های خرد تعامل، انتزاعی است.",
   "صورت‌های اجتماعی از محتوای انگیزه‌ها مستقل و قابل مقایسه‌اند؛ همان قالب در بسترهای تاریخی متفاوت بازتولید می‌شود.",
   "فضا، حس و فاصله ابعادی سازنده در تعامل‌اند، نه صحنهٔ بی‌اثر آن.",
  ],
  "principles": [
   "تحلیل از صورت‌های خرد (نگاه، مبادله، هم‌جواری) آغاز می‌شود، نه از کل اجتماعی.",
   "دوگانگی‌ها (نزدیک/دور، فرد/جمع، آزادی/قید) به‌جای حل‌شدن، به‌عنوان تنش سازنده تحلیل می‌شوند.",
   "پول و رسانه‌های انتزاعی، فاصلهٔ اجتماعی را بازآرایی می‌کنند و رابطهٔ شخصی را به محاسبه تبدیل می‌کنند.",
  ],
  "critiques": [
   "صورت‌گرایی: تمرکز بر قالب تعامل، محتوای تاریخی، مناسبات تولید و ساختار طبقاتی را کم‌رنگ می‌کند و به توصیفِ تمثیلی نزدیک می‌شود.",
   "فقدان سازوکار آزمون: مفاهیمی مانند «نگرش بی‌اعتنا» یا «غریبه» بیشتر شهود هنری‌اند تا سازه‌های سنجش‌پذیر.",
   "بافت‌وابستگی: نمونه‌ها برگرفته از برلین اوایل قرن بیستم‌اند و تعمیم آن‌ها به شهرهای جهانی جنوب و به فضاهای دیجیتال نیازمند بازتعریف است.",
   "ابهام سیاسی: زیمل تنش‌ها را توصیف می‌کند بی‌آنکه موضع انتقادی روشنی در برابر قدرت بگیرد؛ همین نکته او را از سنت انتقادی فرانکفورت جدا می‌کند.",
  ],
  "applications": [
   "طراحی و تحلیل فضای شهری و رسانه‌های محیطی (تبلیغات بیرونی، نمایشگرهای عمومی): فاصله، زاویهٔ دید و مرز به‌مثابهٔ صورت تعامل.",
   "خوانش پلتفرم به‌عنوان فضا: صفحهٔ پروفایل، دیوار کامنت و «غریبهٔ آنلاین» بازتولید صورت‌های زیملی‌اند.",
   "تحلیل اقتصاد توجه با استعارهٔ پول: متریک‌ها همان کارکرد انتزاعی و فاصله‌گذارِ پول را برای رابطهٔ اجتماعی ایفا می‌کنند.",
   "مطالعهٔ تجربهٔ کاربر در فضاهای هم‌زمان حضوری و دیجیتال (phubbing، هم‌حضوری تکه‌تکه).",
  ],
  "evolution": "از «صورت‌های اجتماعی‌شدن» (۱۹۰۸) به مکتب شیکاگو و جامعه‌شناسی شهری، سپس به گافمن (نظم تعامل)، تحلیل شبکهٔ اجتماعی و در دههٔ اخیر به بازخوانی زیمل به‌عنوان نظریه‌پرداز پیشرو فضای دیجیتال (چایکو، ۲۰۱۵).",
  "key_concepts": ["صورت اجتماعی‌شدن (Form of Sociation)", "نگرش بی‌اعتنا (Blasé Attitude)", "غریبه (The Stranger)", "معاشرت (Sociability)", "فاصلهٔ اجتماعی (Social Distance)", "جامعه‌شناسی حواس (Sociology of the Senses)", "پول به‌مثابهٔ رسانهٔ انتزاعی (Money as Abstract Medium)"],
  "studies": [
   "Chayko, M. (2015). The first web theorist? Georg Simmel and the legacy of \"The Metropolis and Mental Life\". Information, Communication & Society. https://doi.org/10.1080/1369118X.2015.1042394",
   "Frisby, D. (1985). Fragments of modernity: Theories of modernity in the work of Simmel, Kracauer and Benjamin. Polity Press.",
  ],
  "detailed_analysis": "\n".join([
   "۱. بنیان و منطق نظری: زیمل جامعه‌شناسی را علم صورت‌ها می‌داند؛ همان نسبت که هندسه با مواد دارد، جامعه‌شناسی با محتوای انگیزه‌ها دارد. این چرخش، سطح تحلیل را از فرد و از کل به «میان‌سطحِ» تعامل می‌برد و راه را برای نظریه‌های خردِ قرن بیستم باز می‌کند.",
   "۲. فضا، حس و رسانه: در سنت زیمل، رسانه صرفاً وسیلهٔ انتقال نیست؛ قالبی است که هم‌جواری، فاصله و ریتم ادراک را سازمان می‌دهد. خوانش زیملی از کلان‌شهر، الگویی برای خوانش پلتفرم است: ازدیاد محرک، اقتصاد توجه و سپر حسی، سه سازوکار قابل مشاهده در مصرف امروز رسانه‌اند.",
   "۳. میراث و محدودیت: زیمل هیچ‌گاه دستگاه منظم و آزمون‌پذیری نساخت و همین او را در حاشیهٔ آکادمی زمانه نگه داشت؛ اما همین خصلت جستارگونه، خوانش او را برای مطالعهٔ پدیده‌های نوظهور انعطاف‌پذیر کرده است.",
  ]),
  "critique_text": "\n".join([
   "۱. صورت‌گرایی: تمرکز بر قالب تعامل، محتوای تاریخی، مناسبات تولید و ساختار طبقاتی را کم‌رنگ می‌کند و تحلیل را به توصیف تمثیلی نزدیک می‌سازد.",
   "۲. فقدان سازوکار آزمون: مفاهیمی مانند «نگرش بی‌اعتنا» یا «غریبه» بیشتر شهود هنری‌اند تا سازه‌های سنجش‌پذیر.",
   "۳. بافت‌وابستگی: نمونه‌ها برگرفته از برلین اوایل قرن بیستم‌اند و تعمیم آن‌ها به فضاهای دیجیتال نیازمند بازتعریف مفاهیم است.",
   "۴. ابهام سیاسی: زیمل تنش‌ها را توصیف می‌کند بی‌آنکه موضع انتقادی روشنی در برابر قدرت بگیرد؛ تفاوت او با سنت فرانکفورت همین‌جاست.",
  ]),
  "example_text": "\n".join([
   "در یک نمایشگر تبلیغاتی ایستگاه مترو، آنچه پیام نامیده می‌شود فقط تصویر نیست: فاصلهٔ دید عابر، مدت ماندن او، و هم‌جواری با غریبه‌ها همان «صورت فضایی» است که معنا را ممکن می‌کند — همان‌گونه که زیمل «پل و در» را صورت‌های اجتماعی می‌خواند.",
   "در شبکه‌های اجتماعی، «غریبهٔ زیملی» به پروفایل بدون رابطهٔ دوطرفه بدل شده است: کسی که نزدیک است ولی بیرون از حلقه؛ و همین وضعیت سیال، هم امکان داوری بی‌طرف را می‌دهد و هم زمینهٔ بی‌اعتمادی را.",
   "وقتی عدد فالوور جای رابطهٔ شخصی را می‌گیرد، کارکرد پول در تحلیل زیمل تکرار می‌شود: سنجه‌ای انتزاعی که فاصله می‌سازد و هر چیز را قابل‌مبادله می‌کند.",
  ]),
 },
 "MC-347": {
  "summary": "(بارت، ۱۹۶۸/۱۹۷۷) اعلام می‌کند که در نقد ادبی مدرن، «مؤلف» دیگر صاحب معنای متن نیست. متن بافتی از نقل‌قول‌های بینامتنی است و معنا نه در نیت نویسنده، بلکه در لحظهٔ خوانش و در ذهن خواننده شکل می‌گیرد. بارت این چرخش را با جملهٔ معروف «تولد خواننده باید به بهای مرگ مؤلف باشد» خلاصه می‌کند.",
  "definition": "«مرگ مؤلف» نام موضعی است که در آن اقتدار تفسیری مؤلف کنار گذاشته می‌شود و معنای متن به‌عنوان نتیجهٔ فعال خواننده و شبکهٔ ارجاعات موجود در متن — نه افشای نیت نویسنده — فهم می‌شود.",
  "main_problem": "نقد ادبی قرن نوزدهم معنای متن را به نیت و زندگی مؤلف گره زده بود و ازاین‌رو متن را به زندگینامه فرو می‌کاست. بارت می‌پرسد اگر اثر مال مؤلف نباشد، معنای آن از کجا می‌آید و اختیار تفسیر باید به چه کسی سپرده شود.",
  "mechanism": "\n".join([
   "(۱) اسکریپتور به‌جای مؤلف: نویسندهٔ مدرن دیگر «پدر» معنای متن نیست؛ او تنها کسی است که مجموعهٔ نشانه‌ها را در کنار هم می‌گذارد.",
   "(۲) متن به‌مثابهٔ بافت نقل‌قول: هر متن انباشتی از ارجاعات، کلیشه‌ها و صدای فرهنگ است؛ هیچ معنایی اصیل و از پیش موجود نیست.",
   "(۳) زمان اسطوره‌ای: بارت می‌گوید مؤلف یک زمان پیشاتاریخی دارد (پیش از متن)، در حالی که اسکریپتور هم‌زمان با متن زاده می‌شود؛ پس متن همیشه «اکنون» است.",
   "(۴) خواننده به‌مثابهٔ جایگاه: معنا در خواننده تحقق می‌یابد، ولی بارت این خواننده را نه یک فرد تجربی، بلکه جایگاهی صوری می‌داند که تمام ارجاعات را گرد می‌آورد.",
   "(۵) نقد ایدئولوژی تفسیر: کنار گذاشتن مؤلف، به معنای رد اقتدار نهاد نقد است که با نام مؤلف، تفسیرهای خود را جاودانه می‌کند.",
   VOID + "با ظهور وب، ایدهٔ بارت به عمل درآمد: محتوای کاربرساخته، میم، فن‌فیکشن و بازترکیب، متنی می‌سازند که نویسندهٔ واحدی ندارد و خواننده‌ها با هر اشتراک‌گذاری، معنای تازه‌ای به آن می‌افزایند.",
  ]),
  "assumptions": [
   "نیت مؤلف در دسترس نیست و حتی اگر باشد، معیار معتبر معنا نیست.",
   "متن خودبسنده است؛ معنا از روابط درونی نشانه‌ها و از خوانش برمی‌آید.",
   "خواننده نه گیرندهٔ منفعل، بلکه محل تولید معناست.",
  ],
  "principles": [
   "تفسیر باید از زندگی‌نامه به ساختمان متن منتقل شود.",
   "معنا کثیر و ناتمام است؛ هر خوانش معتبر به‌شمار می‌آید.",
   "اقتدار تفسیری نهادها باید در برابر کثرت خوانش‌ها نقد شود.",
  ],
  "critiques": [
   "افراط در نفی مؤلف: در تولید رسانه‌ای، نیت، طراحی و مسئولیت تولیدکننده نقش تعیین‌کننده‌ای دارد و حذف کامل آن تحلیل را ناقص می‌کند.",
   "خطر نسبی‌گرایی: اگر هر خوانشی معتبر باشد، معیاری برای تمایز تفسیر معقول از تفسیر دلبخواه باقی نمی‌ماند.",
   "حذف مسئولیت اخلاقی و حقوقی: در تهمت، جعل و حقوق مؤلف، پرسش «چه کسی این را گفته» اساسی است و مرگ مؤلف آن را مبهم می‌کند.",
   "شاهد تجربی ناکافی: پژوهش‌های دریافت مخاطب نشان می‌دهند خوانندگان واقعی از نشانه‌های مؤلف (برند، نام، اعتبار) برای تفسیر استفاده می‌کنند.",
  ],
  "applications": [
   "تحلیل محتوای کاربرساخته و میم: معنا در بازترکیب و اشتراک‌گذاری دوباره ساخته می‌شود، نه در نیت سازندهٔ اولیه.",
   "پرسش از مؤلفگی در محتوای هوش مصنوعی: وقتی خروجی از آموزش توده‌ای متن‌ها برمی‌آید، «مؤلف» کیست؟",
   "نقد نظام ستاره‌سازی بازاریابی و برند مؤلف: اعتبار نام، خود یک اثر تفسیری است.",
   "مطالعهٔ بای‌لاین و اعتماد خبری: خوانندگان از نام خبرنگار به‌عنوان نشانهٔ صحت استفاده می‌کنند و مرگ مؤلف این سازوکار را نادیده می‌گیرد.",
  ],
  "evolution": "بارت در دههٔ ۱۹۷۰ از «متن خواندنی» به «متن نوشتنی» و سپس به دلمشغولی با «عکاسی و نشانه» حرکت کرد. فوکو (۱۹۶۹) با پرسش «نویسنده چیست؟» مؤلف را از شخص به «کارکرد» بدل کرد؛ نظریهٔ دریافت (ایزر، فیش) و سپس پژوهش‌های مخاطب در مطالعات فرهنگی، خوانندهٔ بارت را تجربی‌تر کردند.",
  "key_concepts": ["مرگ مؤلف (Death of the Author)", "اسکریپتور (Scriptor)", "بینامتنیت (Intertextuality)", "متن نوشتنی (Writerly Text)", "جایگاه خواننده (Reader as Locus)", "نقد زندگینامه‌ای (Biographical Criticism)"],
  "studies": [
   "Foucault, M. (1969). Qu'est-ce qu'un auteur? Bulletin de la Société française de philosophie, 63(3), 73-104.",
   "Bennett, A. (2005). The author. Routledge.",
  ],
  "detailed_analysis": "\n".join([
   "۱. بنیان و منطق نظری: مرگ مؤلف ادامهٔ منطقی نقد ساختارگرای بارت بر «اسطوره» است؛ همان‌گونه که در اسطوره‌شناسی، معنای ضمنی از تاریخ پاک می‌شود، در نقد ادبی نیز نام مؤلف تاریخ تولید متن را از تحلیل پاک می‌کند.",
   "۲. چرخش از تولید به دریافت: با انتقال کانون از مؤلف به خواننده، سؤال پژوهش تغییر می‌کند: از «چه کسی چه می‌خواست بگوید» به «چه کسانی چگونه می‌خوانند». این چرخش، بنیاد نظری مطالعات دریافت و پژوهش مخاطب در مطالعات فرهنگی شد.",
   "۳. تنش امروز: در دوران پلتفرم، مرگ مؤلف هم تحقق یافته و هم نقض شده است — محتوا بی‌مؤلف بازترکیب می‌شود، اما اقتصاد توجه دوباره بر «شخصیت برند» و «اینفلوئنسر» سرمایه‌گذاری می‌کند.",
  ]),
  "critique_text": "\n".join([
   "۱. افراط در نفی مؤلف: در تولید رسانه‌ای، نیت، طراحی و مسئولیت تولیدکننده نقش تعیین‌کننده دارد و حذف کامل آن تحلیل را ناقص می‌کند.",
   "۲. خطر نسبی‌گرایی: اگر هر خوانشی معتبر باشد، معیاری برای تمایز تفسیر معقول از تفسیر دلبخواه باقی نمی‌ماند.",
   "۳. حذف مسئولیت اخلاقی و حقوقی: در تهمت، جعل و حقوق مؤلف، پرسش «چه کسی این را گفته» اساسی است و مرگ مؤلف آن را مبهم می‌کند.",
   "۴. شاهد تجربی ناکافی: پژوهش دریافت مخاطب نشان می‌دهد خوانندگان واقعی از نشانه‌های مؤلف — برند، نام، اعتبار — برای تفسیر استفاده می‌کنند.",
  ]),
  "example_text": "\n".join([
   "یک میم اینترنتی را در نظر بگیرید: تصویری که هزاران بار بازنشر می‌شود و هر بار با متن تازه‌ای همراه می‌شود؛ پرسش «نیت سازندهٔ اولیه چه بود؟» بی‌فایده است، چون معنا در هر بازترکیب دوباره ساخته می‌شود.",
   "در بازاریابی، برند مؤلف را نمی‌کشد بلکه آن را به یک شخصیت تبدیل می‌کند: مخاطب با دنبال‌کردن یک اینفلوئنسر، هم متن و هم مؤلف را مصرف می‌کند — نمونهٔ نقض تجربی مرگ مؤلف.",
   "در خبر، نام خبرنگار و رسانه به‌عنوان نشانهٔ صحت عمل می‌کند؛ اگر این نشانه حذف شود، خواننده معیار تفسیر خود را از دست می‌دهد. همین‌جا مرزهای نظریهٔ بارت آشکار می‌شود.",
  ]),
 },
 "MC-349": {
  "summary": "(فوکو، ۱۹۶۹) تحلیل گفتمان، روشی است برای مطالعهٔ قواعدی که در یک دورهٔ تاریخی تعیین می‌کنند چه چیزی می‌تواند گفته شود، چه کسی حق گفتن دارد و کدام ابژه‌ها و سوژه‌ها «واقعی» شمرده می‌شوند. گفتمان نه بازتاب واقعیت، بلکه سازندهٔ آن است و همیشه با قدرت و نهاد پیوند دارد.",
  "definition": "تحلیل گفتمان فوکویی مطالعهٔ نظام‌مند «صورت‌بندی‌های گفتمانی» است: مجموعهٔ قواعد پراکنده‌ای که گزاره‌ها را ممکن می‌کند و از خلال آن‌ها دانش، ابژه و سوژه در یک دوره شکل می‌گیرند.",
  "main_problem": "چگونه است که در هر دوره، برخی گفته‌ها بدیهی و برخی ناممکن می‌شوند؟ فوکو می‌پرسد پیش از آنکه کسی «حقیقت» را بگوید، چه نظامی تعیین کرده است که این گزاره اصلاً قابل بیان باشد؛ و چرا این نظام در دوره‌های دیگر تغییر می‌کند.",
  "mechanism": "\n".join([
   "(۱) گزاره به‌جای جمله: واحد تحلیل، «گزاره» است — نه جملهٔ دستوری و نه قضیهٔ منطقی — بلکه رخدادی که در شبکهٔ نهادی جایگاه دارد و اثر می‌گذارد.",
   "(۲) صورت‌بندی گفتمانی: پراکندگی گفته‌ها را قواعدی مشترک سازمان می‌دهد؛ همان ابژه، همان مفاهیم و همان راهبردها در متن‌های پراکنده بازتولید می‌شوند.",
   "(۳) آرشیو: مجموعهٔ شرایطی که تعیین می‌کند چه چیزی در یک دوره «قابل گفته‌شدن» است؛ آرشیو نه کتابخانه، بلکه نظام امکان‌هاست.",
   "(۴) قدرت/دانش: گفتمان با تولید دانش، ابژه‌ها را می‌سازد (دیوانه، مجرم، بیمار) و از طریق نهادها آن‌ها را مدیریت می‌کند؛ قدرت نه سرکوب، بلکه تولیدکنندهٔ حقیقت است.",
   "(۵) سوژه‌گاه: فرد در گفتمان، نه منبع معنا، بلکه جایگاهی است که به او داده می‌شود («بیمار»، «مصرف‌کننده»، «کاربر») و از همان جایگاه سخن می‌گوید.",
   VOID + "در تحلیل خبر، انتخاب واژه («شورش» یا «اعتصاب»، «مهاجر» یا «پناهنده») نه انتخاب سبکی، بلکه عملی گفتمانی است که مشروعیت کنشگران را تعیین می‌کند؛ و در سیاست‌گذاری محتوا، همان قواعد آرشیوی، مرزهای گفتنی و نگفتنی را می‌کشد.",
  ]),
  "assumptions": [
   "معنا در سطح متن منفرد نیست؛ در نظام قواعدی است که متن‌ها را ممکن می‌کند.",
   "دانش و قدرت جدایی‌ناپذیرند؛ هر نظام دانش، سازوکار نظم‌دهی به رفتار را در خود دارد.",
   "سوژه محصول گفتمان است، نه منبع خودبنیاد معنا.",
  ],
  "principles": [
   "تحلیل از سطح واژه و جمله به سطح قواعد صورت‌بندی و شرایط امکان منتقل می‌شود.",
   "نهادها، آرشیو و رویه‌های گفتاری باید با هم مطالعه شوند.",
   "تاریخ‌مندی: هیچ گفتمانی طبیعی نیست؛ هر کدام در دوره‌ای خاص و با گسست‌هایی شکل گرفته است.",
  ],
  "critiques": [
   "فقدان رویهٔ روشن: فوکو دستور کار تحلیلی دقیقی ارائه نمی‌دهد؛ همین ابهام، تکرارپذیری پژوهش را پایین می‌آورد و آن را به تفسیر تحلیل‌گر وابسته می‌کند.",
   "حذف عاملیت: اگر سوژه محصول گفتمان است، مقاومت و تغییر نیز باید توضیح داده شود، اما در دیرینه‌شناسی فوکو کم‌رنگ می‌ماند.",
   "خطر گزینش تأییدی: پژوهشگر متن‌هایی را برمی‌گزیند که گفتمان مورد نظرش را نشان می‌دهند و متن‌های ناهمخوان کنار می‌مانند.",
   "ابهام تجربی: ادعاهای تاریخی گسترده، بدون معیار مستقل برای ارزیابی، در برابر نقد تاریخی آسیب‌پذیرند.",
  ],
  "applications": [
   "تحلیل گفتمان خبری و برجسته‌سازی: چگونه یک رخداد در قالب «بحران» یا «فرصت» صورت‌بندی می‌شود.",
   "مطالعهٔ سیاست‌گذاری محتوا در پلتفرم‌ها: چه گفتارهایی «امن» و چه گفتارهایی «مخل» تعریف می‌شوند.",
   "تحلیل رسانه‌ای سلامت و بدن: چگونه گفتمان پزشکی، سوژهٔ «بیمار» و «سالم» را می‌سازد.",
   "پژوهش سازمانی و منابع انسانی: گفتمان «کارایی» و «استعداد» چگونه رفتار کارکنان را نظم می‌دهد.",
  ],
  "evolution": "از دیرینه‌شناسی (۱۹۶۹) به تبارشناسی در «مراقبت و تنبیه» (۱۹۷۵) و «تاریخ جنسیت»؛ در دههٔ ۱۹۹۰ تحلیل گفتمان انتقادی (فرکلاف، وداک) مفاهیم فوکو را با زبان‌شناسی نظام‌مند ترکیب کرد و امروز تحلیل گفتمان پلتفرم، نسخهٔ دیجیتال همین سنت است.",
  "key_concepts": ["گزاره (Statement/Énoncé)", "صورت‌بندی گفتمانی (Discursive Formation)", "آرشیو (Archive)", "قدرت/دانش (Power/Knowledge)", "سوژه‌گاه (Subject Position)", "نظم گفتار (Order of Discourse)", "تبارشناسی (Genealogy)"],
  "studies": [
   "Foucault, M. (1975). Surveiller et punir: Naissance de la prison. Éditions Gallimard.",
   "Fairclough, N. (1992). Discourse and social change. Polity Press.",
  ],
  "detailed_analysis": "\n".join([
   "۱. بنیان و منطق نظری: فوکو با رد پیوستگی «مؤلف-اثر» و «سنت» و «تأثیر»، واحد تحلیل را به گزاره منتقل می‌کند؛ هدف نه بازسازی اندیشهٔ یک نویسنده، بلکه نقشه‌برداری از نظامی است که گفته‌ها را ممکن می‌سازد.",
   "۲. از دیرینه‌شناسی به تبارشناسی: در ۱۹۶۹ قدرت تقریباً غایب است؛ از ۱۹۷۵ فوکو گفتمان را در نهادها، بدن و رویه‌های تنبیهی جای می‌دهد و نشان می‌دهد دانش، ابزار مدیریت جمعیت می‌شود.",
   "۳. کاربرد رسانه‌ای: تحلیل گفتمان به پژوهش رسانه ابزاری می‌دهد تا از «چه گفت» به «چگونه گفتن ممکن شد» برود؛ همین پرسش، تحلیل محتوای کمی را به تحلیل شرایط تولید معنا پیوند می‌زند.",
  ]),
  "critique_text": "\n".join([
   "۱. فقدان رویهٔ روشن: فوکو دستور کار تحلیلی دقیقی ارائه نمی‌دهد؛ همین ابهام، تکرارپذیری پژوهش را پایین می‌آورد و آن را به تفسیر تحلیل‌گر وابسته می‌کند.",
   "۲. حذف عاملیت: اگر سوژه محصول گفتمان است، مقاومت و تغییر نیز باید توضیح داده شود، اما در دیرینه‌شناسی فوکو کم‌رنگ می‌ماند.",
   "۳. خطر گزینش تأییدی: پژوهشگر متن‌هایی را برمی‌گزیند که گفتمان مورد نظرش را نشان می‌دهند و متن‌های ناهمخوان کنار می‌مانند.",
   "۴. ابهام تجربی: ادعاهای تاریخی گسترده، بدون معیار مستقل برای ارزیابی، در برابر نقد تاریخی آسیب‌پذیرند.",
  ]),
  "example_text": "\n".join([
   "دو خبر از یک رخداد را مقایسه کنید: «معترضان خیابان‌ها را بستند» و «اغتشاشگران نظم عمومی را برهم زدند». ابژه یکی است، اما صورت‌بندی گفتمانی متفاوت، کنشگر را مشروع یا نامشروع می‌سازد — دقیقاً همان چیزی که فوکو «نظم گفتار» می‌نامد.",
   "در پلتفرم‌های اجتماعی، واژه‌نامهٔ سیاست محتوا (چه چیزی «اطلاعات نادرست» است، چه چیزی «اظهارنظر») عملی گفتمانی است: تعریف واژه، مرز گفتنی و نگفتنی را می‌کشد.",
   "در گفتمان پزشکی رسانه‌ای، «بیمار» نه فقط فردی با نشانه، بلکه سوژه‌ای است که باید خود را زیر نظر بگیرد؛ رسانهٔ سلامت با همین صورت‌بندی، رفتار روزمره را نظم می‌دهد.",
  ]),
 },
 "MC-351": {
  "summary": "(هاج و کرس، ۱۹۸۸) نشانه‌شناسی اجتماعی، مطالعهٔ نشانه‌ها را از نظام انتزاعی زبان جدا می‌کند و به بستر اجتماعی، مادی و مناسبات قدرت برمی‌گرداند. نشانه‌ها «برانگیخته»اند: نشانه‌ساز از میان منابع نشانه‌ای موجود، انتخاب می‌کند تا منفعت و موقعیت خود را بیان کند؛ ازاین‌رو هر نشانه، اثری از عمل اجتماعی است.",
  "definition": "نشانه‌شناسی اجتماعی بررسی شیوه‌ای است که کنشگران در بسترهای نهادی، از منابع نشانه‌ای (زبان، تصویر، رنگ، چیدمان، صدا) برای تولید معنا استفاده می‌کنند و نظام‌های منظمِ تولید و دریافت، این استفاده را محدود و جهت‌دار می‌کنند.",
  "main_problem": "نشانه‌شناسی ساختارگرا معنا را در نظام انتزاعی زبان می‌جست و کاربر را بیرون از تحلیل می‌گذاشت. هاج و کرس می‌پرسند چگونه معنا در عمل اجتماعی، در مناسبات نابرابر و در بسترهای مادی ساخته می‌شود و چرا برخی منابع نشانه‌ای در دسترس برخی گروه‌ها نیستند.",
  "mechanism": "\n".join([
   "(۱) نشانهٔ برانگیخته: برخلاف قرارداد دلبخواه سوسوری، نشانه‌ساز در هر لحظه از میان گزینه‌های ممکن، صورتی را برمی‌گزیند که «منفعت» او را بهتر بیان کند؛ پس صورت نشانه، انگیزه‌دار است.",
   "(۲) منابع نشانه‌ای: معناسازی از مجموعهٔ محدودی از امکانات موجود در یک فرهنگ تغذیه می‌کند؛ این مجموعه، خود محصول تاریخ و نابرابری است.",
   "(۳) منطق‌نامه (logonomic system): قواعدی که تعیین می‌کنند چه کسی حق تولید کدام معنا را دارد و چه کسی حق دریافت آن را؛ همان‌گونه که آداب سخن‌گفتن، جایگاه اجتماعی را بازتولید می‌کند.",
   "(۴) وجهیت (modality): هر متن با نشانه‌هایی (واقع‌نمایی، نور، زاویه، لحن) ادعایی دربارهٔ صدق خود می‌سازد؛ وجهیت، سازوکار اصلی «حقیقت‌نمایی» رسانه است.",
   "(۵) چندوجهی‌بودن: معنا در ترکیب وجه‌ها (تصویر، متن، صدا، چیدمان صفحه) ساخته می‌شود، نه در یک وجه به‌تنهایی؛ پس تحلیل باید هم‌زمان همهٔ وجه‌ها را بخواند.",
   VOID + "یک پست اینستاگرامی مجموعه‌ای از انتخاب‌های نشانه‌ای است: قاب، رنگ، نوع فونت، محل برچسب قیمت — هر انتخاب، در نظام منطق‌نامه‌ای پلتفرم، ادعایی دربارهٔ سبک زندگی، اعتبار و مخاطبِ شایسته می‌سازد.",
  ]),
  "assumptions": [
   "معنا در عمل اجتماعی ساخته می‌شود، نه در نظام انتزاعی نشانه‌ها.",
   "منابع نشانه‌ای نامتقارن توزیع شده‌اند؛ دسترسی به آن‌ها، خود مسئله‌ای اجتماعی است.",
   "هر متن چندوجهی است و تحلیل تک‌وجهی آن را ناقص می‌کند.",
  ],
  "principles": [
   "نشانه را باید همراه با منفعت نشانه‌ساز و بستر نهادی آن تحلیل کرد.",
   "قواعد تولید و دریافت (منطق‌نامه) بخشی از تحلیل است، نه حاشیهٔ آن.",
   "وجهیت متن را باید از نشانه‌های صوری آن بازخواند.",
  ],
  "critiques": [
   "توصیف‌گرایی: تحلیل بیشتر توصیفی است و سازوکار علّی تولید معنا را کمتر نشان می‌دهد.",
   "جانشینی مخاطب با تحلیل‌گر: تفسیر پژوهشگر به‌جای ادراک واقعی خواننده می‌نشیند و آزمون دریافت انجام نمی‌شود.",
   "انتقال بی‌قید دستور زبان هلیدی به تصویر: فرض هم‌ارزی ساختار زبان و تصویر محل مناقشه است.",
   "گسترش بی‌مرز چندوجهی‌بودن: با افزودن وجه‌های تازه، معیار روشن تحلیل و مرز آن مبهم شده است.",
  ],
  "applications": [
   "تحلیل آگهی و برندسازی: خواندن ترکیب رنگ، شخصیت و متن به‌مثابهٔ ادعای هویتی.",
   "نشانه‌شناسی رابط کاربری: آیکون‌ها، چیدمان و استعاره‌های ناوبری چه معنایی دربارهٔ کاربر و کنترل او می‌سازند.",
   "تحلیل عکاسی خبری و وجهیت تصویری: زاویهٔ دوربین و قاب‌بندی چگونه ادعای صدق می‌سازد.",
   "طراحی متن جانشین (alt text) به‌عنوان تصمیم نشانه‌ای: کدام معنا برای مخاطب نابینا انتخاب می‌شود.",
  ],
  "evolution": "از زبان‌شناسی نقش‌گرای هلیدی (۱۹۷۸) به نشانه‌شناسی اجتماعی هاج و کرس (۱۹۸۸)، سپس به دستور زبان بصری کرس و ون‌لیوون (۱۹۹۶/۲۰۰۶) و امروز به چندوجهی‌بودن دیجیتال و نشانه‌شناسی رابط و پلتفرم.",
  "key_concepts": ["نشانهٔ برانگیخته (Motivated Sign)", "منبع نشانه‌ای (Semiotic Resource)", "منطق‌نامه (Logonomic System)", "وجهیت (Modality)", "چندوجهی‌بودن (Multimodality)", "کارکرد سه‌گانه (Representational/Interpersonal/Compositional)", "بازتولید نمادین (Symbolic Reproduction)"],
  "studies": [
   "Kress, G., & van Leeuwen, T. (2006). Reading images: The grammar of visual design (2nd ed.). Routledge.",
   "Halliday, M. A. K. (1978). Language as social semiotic: The social interpretation of language and meaning. Edward Arnold.",
  ],
  "detailed_analysis": "\n".join([
   "۱. بنیان و منطق نظری: نشانه‌شناسی اجتماعی، وارث دو سنت است: نشانه‌شناسی پراگی و زبان‌شناسی نقش‌گرای هلیدی. سهم هاج و کرس، افزودن ایدئولوژی و نابرابری به تحلیل نشانه است؛ نشانه دیگر بی‌طرف نیست، بلکه موضع نشانه‌ساز را حمل می‌کند.",
   "۲. چندوجهی‌بودن و رسانه: با گسترش رسانه‌های تصویری، ابزار تحلیل زبان به‌تنهایی ناکافی شد؛ نشانه‌شناسی اجتماعی چارچوبی داد تا تصویر، صدا و چیدمان هم‌زمان خوانده شوند و همین چارچوب پایهٔ مطالعات چندوجهی امروز شد.",
   "۳. نقد و افق: ضعف آزمون تجربی همچنان پاشنهٔ آشیل این سنت است؛ اما پیوند آن با پژوهش دریافت و تحلیل داده‌های تعامل کاربر، می‌تواند فاصلهٔ تحلیل‌گر و مخاطب را کم کند.",
  ]),
  "critique_text": "\n".join([
   "۱. توصیف‌گرایی: تحلیل بیشتر توصیفی است و سازوکار علّی تولید معنا را کمتر نشان می‌دهد.",
   "۲. جانشینی مخاطب با تحلیل‌گر: تفسیر پژوهشگر به‌جای ادراک واقعی خواننده می‌نشیند و آزمون دریافت انجام نمی‌شود.",
   "۳. انتقال بی‌قید دستور زبان هلیدی به تصویر: فرض هم‌ارزی ساختار زبان و تصویر محل مناقشه است.",
   "۴. گسترش بی‌مرز چندوجهی‌بودن: با افزودن وجه‌های تازه، معیار روشن تحلیل و مرز آن مبهم شده است.",
  ]),
  "example_text": "\n".join([
   "در آگهی یک خودرو، نور طلایی غروب و زاویهٔ پایین دوربین، پیش از هر جمله‌ای ادعای «قدرت و اصالت» می‌سازند؛ وجهیت تصویری، همان کاری را می‌کند که در خبر، صفت «معتبر» در متن انجام می‌دهد.",
   "در رابط کاربری یک اپلیکیشن مالی، آیکون قفل و رنگ سبز، نه فقط کارکرد، بلکه وعدهٔ امنیت می‌دهند؛ منطق‌نامهٔ پلتفرم تعیین می‌کند کدام نشانه‌ها «قابل اعتماد» به نظر برسند.",
   "در پست یک فروشگاه، انتخاب فونت دست‌نویس برای قیمت، به‌جای فونت رسمی، حس «صمیمیت محلی» می‌سازد — نشانه‌ای برانگیخته که منفعت فروشنده را بیان می‌کند.",
  ]),
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
    codes = list(S.keys())
    cur.execute("SELECT id, code, properties FROM kb_entities WHERE code IN (%s)" % ",".join(["%s"]*len(codes)), codes)
    rows = {code:(eid, json.loads(pr)) for (eid, code, pr) in cur.fetchall()}
    with open(BACKUP, "w", encoding="utf-8") as f:
        json.dump([{"code": cd, "props": rows[cd][1]} for cd in codes if cd in rows], f, ensure_ascii=False, indent=1)
    print("backup ->", len(rows), "rows")

    for code in codes:
        if code not in rows:
            print("MISSING", code); continue
        eid, p = rows[code]
        e = ENRICH[code]
        if "critique_text" in e: p["critique"] = e["critique_text"]
        if "example_text" in e: p["example"] = e["example_text"]
        for k, v in e.items():
            if k in ("critique_text", "example_text"): continue
            p[k] = v
        if not has_content(p.get("definition")) and has_content(p.get("summary")): p["definition"] = p["summary"]
        spec = S[code]
        p["sources"] = [dict(citation=s["citation"], language=("انگلیسی" if s["language"]=="en" else "فارسی"),
                             doi=s.get("doi") or "", url=s.get("url") or "", year=s.get("year")) for s in spec]
        p["citations"] = [dict(source=s["citation"], locator=s["locator"], supports=s["supports"],
                               verified=bool(s.get("verified"))) for s in spec]
        n_sources = len(spec); n_verified = sum(1 for s in spec if s.get("verified"))
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
                cur.execute("SELECT id FROM kb_sources WHERE doi=%s LIMIT 1", (s["doi"],)); r = cur.fetchone()
                if r: sid = r[0]
            if sid is None:
                cur.execute("SELECT id FROM kb_sources WHERE title_en=%s AND year=%s LIMIT 1", (s["title_en"], s["year"])); r = cur.fetchone()
                if r: sid = r[0]
            if sid is None:
                bib = json.dumps({"authors": s["authors"], "citation": s["citation"]}, ensure_ascii=False)
                cur.execute("INSERT INTO kb_sources (kind,title_fa,title_en,year,publisher,doi,isbn,url,language,access_type,bibliographic) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (s["kind"], s["title_fa"], s["title_en"], s["year"], s["publisher"], s.get("doi"), s.get("isbn"), s.get("url"),
                     s["language"], "open" if s.get("url") else "unknown", bib))
                sid = cur.lastrowid
            cur.execute("SELECT id FROM kb_evidence WHERE about_code=%s AND source_id=%s LIMIT 1", (code, sid))
            if cur.fetchone():
                continue
            lt = "CHAPTER" if s["locator_type"] == "CHAPTER" else ("PAGE" if s["locator_type"] == "page_range" else "SECTION")
            cur.execute("INSERT INTO kb_citations (source_id,locator_type,locator_value,paraphrase,citation_style,language,accessed_at) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                (sid, lt, s["locator"], "پشتیبانی از بخش: " + s["supports"], "apa", s["language"], NOW))
            cid = cur.lastrowid
            cur.execute("INSERT INTO kb_evidence (source_id,citation_id,about_code,evidence_type,evidence_summary,locator,direction,extraction_method,verification_status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (sid, cid, code, "bibliographic_reference", "منبع اصلی برای بخش: " + s["supports"], s["locator"], "supports",
                 "ai_extraction", "verified" if s.get("verified") else "unverified"))
        cur.execute("SELECT COALESCE(MAX(version),0)+1 FROM kb_entity_versions WHERE entity_id=%s", (eid,))
        ver = cur.fetchone()[0]
        cur.execute("INSERT INTO kb_entity_versions (entity_id, version, snapshot, change_reason, changed_by, created_at) VALUES (%s,%s,%s,%s,%s,%s)",
                    (eid, ver, json.dumps({"quality_score": score, "words": words, "sources": n_sources, "verified": n_verified}, ensure_ascii=False),
                     "full documentation enrichment + verified sources", STAMP, NOW))
        cur.execute("INSERT INTO kb_audit_log (entity_code, action, detail, source) VALUES (%s,%s,%s,%s)",
                    (code, "DOC_ENRICH", json.dumps({"quality_score": score, "words": words, "sources": n_sources, "verified": n_verified, "relations": n_relations, "breakdown": detail}, ensure_ascii=False), STAMP))
        print(f"{code}: score={score} words={words} sources={n_sources} verified={n_verified} relations={n_relations} | {detail}")
    c.commit(); c.close()
    print("BATCH66 THEORY DONE")

if __name__ == "__main__":
    main()
