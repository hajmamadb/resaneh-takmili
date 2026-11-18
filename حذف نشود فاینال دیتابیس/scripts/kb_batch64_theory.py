# -*- coding: utf-8 -*-
"""Batch 64 (THEORY): MC-334 The Medium Is the Message (McLuhan 1964),
MC-335 Global Village (McLuhan 1962), MC-336 Hot and Cool Media (McLuhan 1964 ch.2),
MC-337 Media Bias = bias of communication (Innis 1951). Anchors verified 2026-11-16.
Rewrites the mismatched boilerplate critique/example found on all four records."""
import pymysql, json

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch64-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch64_theory.json"

S = {
 "MC-334": [
   dict(kind="BOOK", title_en="Understanding Media: The Extensions of Man",
        title_fa="شناخت رسانه: گسترش‌های انسان",
        authors="McLuhan, M.", year=1964, publisher="New York: McGraw-Hill", doi=None,
        url="https://web.mit.edu/allanmc/www/mcluhan.mediummessage.pdf",
        language="en", isbn=None,
        citation="McLuhan, M. (1964). Understanding media: The extensions of man. McGraw-Hill.",
        locator="ch. 1 (pp. 7-21)", locator_type="CHAPTER", supports="definition / the medium is the message", verified=True),
   dict(kind="BOOK", title_en="The Medium Is the Massage: An Inventory of Effects",
        title_fa="رسانه همان ماساژ است: فهرستی از اثرها",
        authors="McLuhan, M., & Fiore, Q.", year=1967, publisher="New York: Bantam Books", doi=None, url=None,
        language="en", isbn=None,
        citation="McLuhan, M., & Fiore, Q. (1967). The medium is the massage: An inventory of effects. Bantam Books.",
        locator="whole work", locator_type="work", supports="evolution / popular restatement", verified=False),
 ],
 "MC-335": [
   dict(kind="BOOK", title_en="The Gutenberg Galaxy: The Making of Typographic Man",
        title_fa="کهکشان گوتنبرگ: ساخت انسان چاپی",
        authors="McLuhan, M.", year=1962, publisher="Toronto: University of Toronto Press", doi=None,
        url="https://archive.org/details/gutenberggalaxym0000mclu",
        language="en", isbn=None,
        citation="McLuhan, M. (1962). The Gutenberg galaxy: The making of typographic man. University of Toronto Press.",
        locator="whole work", locator_type="work", supports="origin / global village and retribalization", verified=True),
   dict(kind="BOOK", title_en="The Global Village: Transformations in World Life and Media in the 21st Century",
        title_fa="دهکدهٔ جهانی: دگرگونی‌های زندگی جهانی و رسانه در قرن بیست‌ویکم",
        authors="McLuhan, M., & Powers, B. R.", year=1989, publisher="New York: Oxford University Press", doi=None, url=None,
        language="en", isbn=None,
        citation="McLuhan, M., & Powers, B. R. (1989). The global village: Transformations in world life and media in the 21st century. Oxford University Press.",
        locator="whole work", locator_type="work", supports="evolution / posthumous extension", verified=False),
 ],
 "MC-336": [
   dict(kind="BOOK", title_en="Understanding Media: The Extensions of Man (ch. 2: Media Hot and Cold)",
        title_fa="شناخت رسانه: گسترش‌های انسان (فصل ۲: رسانه‌های گرم و سرد)",
        authors="McLuhan, M.", year=1964, publisher="New York: McGraw-Hill", doi=None,
        url="https://designopendata.wordpress.com/wp-content/uploads/2014/05/understanding-media-mcluhan.pdf",
        language="en", isbn=None,
        citation="McLuhan, M. (1964). Understanding media: The extensions of man. McGraw-Hill.",
        locator="ch. 2 (pp. 22-32)", locator_type="CHAPTER", supports="definition / hot and cool classification", verified=True),
   dict(kind="BOOK", title_en="The Gutenberg Galaxy: The Making of Typographic Man",
        title_fa="کهکشان گوتنبرگ: ساخت انسان چاپی",
        authors="McLuhan, M.", year=1962, publisher="Toronto: University of Toronto Press", doi=None,
        url="https://archive.org/details/gutenberggalaxym0000mclu",
        language="en", isbn=None,
        citation="McLuhan, M. (1962). The Gutenberg galaxy: The making of typographic man. University of Toronto Press.",
        locator="whole work", locator_type="work", supports="context / typographic and acoustic cultures", verified=False),
 ],
 "MC-337": [
   dict(kind="BOOK", title_en="The Bias of Communication",
        title_fa="سوگیری ارتباط",
        authors="Innis, H. A.", year=1951, publisher="Toronto: University of Toronto Press", doi="10.3138/9780802096067",
        url="https://utppublishing.com/doi/book/10.3138/9780802096067",
        language="en", isbn=None,
        citation="Innis, H. A. (1951). The bias of communication. University of Toronto Press. https://doi.org/10.3138/9780802096067",
        locator="whole work", locator_type="work", supports="definition / time and space bias / monopoly of knowledge", verified=True),
   dict(kind="BOOK", title_en="Empire and Communications",
        title_fa="امپراتوری و ارتباطات",
        authors="Innis, H. A.", year=1950, publisher="Oxford: Clarendon Press", doi=None, url=None,
        language="en", isbn=None,
        citation="Innis, H. A. (1950). Empire and communications. Clarendon Press.",
        locator="whole work", locator_type="work", supports="origin / media and imperial administration", verified=False),
 ],
}

ENRICH = {
 "MC-334": {
   "summary": "«رسانه پیام است» (The Medium Is the Message) تز مرکزی مارشال مک‌لوهان است: اثر اجتماعی و روانی هر رسانه، از محتوایی که حمل می‌کند برنمی‌آید، بلکه از مقیاس، سرعت و الگوی تازه‌ای می‌آید که رسانه به امور انسانی وارد می‌کند. این تز در فصل نخست «Understanding Media: The Extensions of Man» (۱۹۶۴، McGraw-Hill) صورت‌بندی شد (McLuhan, 1964).",
   "definition": "رسانه در این معنا، هر گسترش انسانی است — از خط و چاپ تا لباس و رایانه — و «پیام» آن، دگرگونی مقیاس و سرعت و الگویی است که در ادراک و سازمان اجتماعی ایجاد می‌کند، نه اطلاعاتی که حمل می‌شود (McLuhan, 1964).",
   "main_problem": "اگر اثر اصلی رسانه‌ها را با محتوای پیام‌ها توضیح ندهیم، آن اثر را باید با چه چیزی توضیح داد؛ و چرا خود رسانه، در تجربهٔ روزمره، نامرئی می‌ماند؟",
   "mechanism": "تز مک‌لوهان بر پنج سازوکار استوار است. (۱) رسانه به‌عنوان گسترش حواس: هر فناوری، امتداد یک حس یا توان انسانی است؛ چرخ، امتداد پا و دوربین، امتداد چشم. (۲) مقیاس، سرعت و الگو: هر رسانه، مقیاس و آهنگ و شکل تازه‌ای به کنش انسانی می‌دهد؛ جاده، سرعت را و ساعت، الگوی زمان را دگرگون می‌کند. (۳) محتوا به‌عنوان عامل انحراف: به تعبیر مشهور مک‌لوهان، محتوای رسانه «تکه‌گوشت آب‌داری است که دزد برای گمراه‌کردن سگ نگهبان ذهن حمل می‌کند»؛ توجه ما به محتوا، رسانه را از دید پنهان می‌کند. (۴) نامرئی‌بودن محیط: رسانه مانند آب برای ماهی است؛ ما درون آن هستیم، نه روبه‌روی آن. (۵) مثال لامپ برق: لامپ هیچ محتوایی ندارد، اما فضای شب را به روز قابل استفاده بدل می‌کند و الگوی فعالیت، کار و اجتماع را از نو سازمان می‌دهد؛ همین نشان می‌دهد که پیام در ساختار است، نه در برنامه. در بستر رسانه، این تز به پرسش طراحی می‌انجامد: رابط پلتفرم، قالب ویدئوی کوتاه و پیام‌رسان، پیش از هر محتوایی، الگوی توجه و تعامل را تعیین می‌کنند؛ فرمت «استوری بیست‌وچهارساعته» پیامی دربارهٔ زمان و حافظه است، مستقل از آنکه چه چیزی در آن منتشر شود.",
   "assumptions": [
     "فناوری رسانه، امتداد حواس و توان‌های انسانی است.",
     "اثر اصلی رسانه در سطح فرم و مقیاس رخ می‌دهد، نه محتوا.",
     "مردم معمولاً محتوا را می‌بینند و رسانه را نمی‌بینند."
   ],
   "principles": [
     "اثر اجتماعی رسانه از فرم آن می‌آید، نه از محتوا.",
     "هر رسانه، مقیاس و سرعت و الگوی تازه‌ای وارد زندگی می‌کند.",
     "رسانهٔ مسلط، محیط نامرئی تجربه است."
   ],
   "critiques": [
     "جبر فناورانه: تز، فناوری را عامل مستقل و تعیین‌کننده می‌بیند و روابط مالکیت، اقتصاد سیاسی و منافع را از تحلیل حذف می‌کند؛ ریموند ویلیامز در «Television: Technology and Cultural Form» (۱۹۷۴) دقیقاً همین را نقد کرد.",
     "انکار نقش محتوا: تجربه نشان می‌دهد محتوا در بسیاری از موارد تعیین‌کننده است؛ دو پیام متفاوت در یک رسانه، اثرهای متفاوت می‌سازند.",
     "ابهام و استعاره‌گویی: گزاره‌ها اغلب ادبی و غیرقابل آزمون‌اند و مک‌لوهان خود عامدانه از نظام اثباتی فاصله می‌گرفت."
   ],
   "applications": [
     "تحلیل فرمت پلتفرم و رابط کاربری به‌عنوان پیام.",
     "پژوهش دربارهٔ اثر ساختار رسانه بر ادراک و سازمان‌دهی.",
     "آموزش سواد رسانه‌ای با تمرکز بر فرم، نه فقط محتوا.",
     "طراحی سازمانی و انتخاب رسانهٔ درون‌سازمانی."
   ],
   "evolution": "مک‌لوهان تز را در «Understanding Media» (۱۹۶۴) بسط داد و در «The Medium Is the Massage» (۱۹۶۷) با کوئنتین فیوره به زبان بصری برگرداند؛ نقد ویلیامز (۱۹۷۴) و سپس پژوهش رسانه‌های دیجیتال، آن را هم‌زمان رد و بازخوانی کرد.",
   "key_concepts": ["رسانه به‌عنوان پیام (the medium is the message)", "گسترش انسان (extensions of man)", "مقیاس و سرعت (scale and pace)", "محیط رسانه (media environment)", "نامرئی‌بودن رسانه"],
   "studies": ["McLuhan, M. (1964). Understanding media: The extensions of man. McGraw-Hill.", "McLuhan, M., & Fiore, Q. (1967). The medium is the massage. Bantam Books."],
   "detailed_analysis": "۱. بنیان و منطق نظری\nمک‌لوهان می‌خواست توجه را از «چه می‌گوییم» به «با چه چیزی می‌گوییم» منتقل کند. استدلال او این بود که اثر بلندمدت هر فناوری ارتباطی، در سطح فرم و ادراک رخ می‌دهد، نه در سطح پیام.\n\n۲. مثال لامپ و منطق آن\nلامپ برق، محتوا ندارد اما زندگی شبانه را ممکن می‌کند. اگر اثر را با محتوا بسنجیم، لامپ «بی‌اثر» است؛ اما واقعیت این است که ساختار شبانه‌روز، کار و اجتماع را دگرگون کرده است. همین قیاس، جوهر تز است.\n\n۳. پیوند رسانه‌ای و نقد\nدر عصر پلتفرم، تز مک‌لوهان دوباره کارآمد شده است: فرمت، پیش از محتوا، رفتار را شکل می‌دهد. اما نقد ویلیامز پابرجاست: اگر مالکیت و اقتصاد را نادیده بگیریم، «رسانه» به عاملیت مستقل بدل می‌شود و مسئولیت نهادی گم می‌شود. تز را باید جدی گرفت، اما نه به‌عنوان جانشین تحلیل سیاسی.",
   "critique_text": "\n".join([
     "۱. جبر فناورانه: فناوری به عاملی مستقل بدل می‌شود و مالکیت، اقتصاد سیاسی و منافع نهادی از تحلیل حذف می‌شوند؛ نقد کلاسیک این موضع، ریموند ویلیامز (۱۹۷۴) است.",
     "۲. انکار محتوا: دو پیام متفاوت در یک رسانه، اثرهای متفاوت می‌سازند؛ بنابراین محتوا را نمی‌توان به‌کلی از تحلیل حذف کرد.",
     "۳. استعاره‌گویی و آزمون‌ناپذیری: گزاره‌ها ادبی و کلی‌اند و مک‌لوهان خود از نظام اثبات تجربی فاصله می‌گرفت؛ همین، اعتبار علمی تز را محدود می‌کند."]),
   "example_text": "استوری بیست‌وچهارساعته در یک پیام‌رسان، پیش از آنکه بدانیم چه ویدئویی در آن است، پیامی دربارهٔ گذرا بودن زمان و حافظه می‌فرستد: محتوا محو می‌شود، اما فرمت، انتظار ما از دوام و توجه را دگرگون می‌کند.",
 },
 "MC-335": {
   "summary": "«دهکدهٔ جهانی» (Global Village) استعارهٔ مک‌لوهان برای جهانی است که رسانه‌های الکترونیک، فاصلهٔ زمان و مکان را در آن فروریخته و همه را به همسایگانی هم‌زمان بدل کرده است. این اصطلاح در «The Gutenberg Galaxy» (۱۹۶۲، University of Toronto Press) معرفی شد (McLuhan, 1962).",
   "definition": "دهکدهٔ جهانی، وضعیتی است که در آن انتقال هم‌زمان اطلاعات، جهان را به واحد ارتباطی به‌هم‌پیوسته‌ای بدل می‌کند که در آن رویدادهای دور، بی‌واسطه و هم‌زمان تجربه می‌شوند (McLuhan, 1962).",
   "main_problem": "وقتی رسانه‌های الکترونیک فاصله را از میان برمی‌دارند و همه را هم‌زمان به هم متصل می‌کنند، چه اتفاقی برای هویت، اجتماع و سیاست می‌افتد؛ آیا نتیجه، همبستگی جهانی است یا تنش محلی؟",
   "mechanism": "مفهوم بر پنج سازوکار استوار است. (۱) فروپاشی زمان و مکان: پیام الکترونیک هم‌زمان به همه جا می‌رسد و فاصلهٔ جغرافیایی، مانع تجربهٔ مشترک نمی‌ماند. (۲) هم‌زمانی: رویدادهای دور، در لحظهٔ وقوع تجربه می‌شوند؛ خبر، به تجربهٔ جمعی جهانی بدل می‌شود. (۳) بازقبیله‌ای‌شدن: مک‌لوهان معتقد بود الکترونیک، انسان را از فردیت چاپی به ساختار قبیله‌ای شنیداری بازمی‌گرداند؛ صدا، هم‌زمانی و مشارکت را بازمی‌آورد. (۴) به‌هم‌پیوستگی و مسئولیت: وقتی همه در یک دهکده‌اند، رویداد یک نقطه، مسئلهٔ همه می‌شود. (۵) تنش درونی دهکده: دهکده، مکان صمیمیت نیست؛ مکان نظارت، شایعه و درگیری است. مک‌لوهان همین تنش را با مفهوم «ترور بی‌تمدن» (tribal terror) هشدار داد. در بستر رسانه، این استعاره هم وعدهٔ همبستگی جهانی (همبستگی در بلایای طبیعی، جنبش‌های فراملی) و هم واقعیت قطب‌بندی و نفرت را توضیح می‌دهد؛ پلتفرم‌ها هم‌زمان دهکده و میدان نزاع می‌سازند.",
   "assumptions": [
     "رسانه‌های الکترونیک فاصلهٔ زمان و مکان را بی‌اثر می‌کنند.",
     "هم‌زمانی تجربه، نوع تازه‌ای از اجتماع می‌سازد.",
     "الکترونیک، ساختار حسی انسان را به سمت شنیداری-مشارکتی بازمی‌گرداند."
   ],
   "principles": [
     "جهان به واحد ارتباطی به‌هم‌پیوسته بدل می‌شود.",
     "هم‌زمانی، مسئولیت و درگیری جهانی می‌آورد.",
     "دهکده، همبستگی و تنش را هم‌زمان تولید می‌کند."
   ],
   "critiques": [
     "آرمانی‌سازی: استعاره، نابرابری دسترسی، شکاف دیجیتال و سلطهٔ زیرساختی را نادیده می‌گیرد و جهانِ «متصل» را با جهانِ برابر اشتباه می‌گیرد.",
     "تجربهٔ معاصر خلاف آن را نشان می‌دهد: قطب‌بندی، اطلاعات نادرست و نفرت آنلاین نشان می‌دهد دهکدهٔ جهانی می‌تواند میدان نزاع باشد، نه همسایگی همدلانه.",
     "جبر فناورانه و ابهام تجربی: مفهوم، ادبی و غیرقابل سنجش است و معلوم نمی‌کند چه کسی و با چه منافعی این دهکده را اداره می‌کند."
   ],
   "applications": [
     "تحلیل جریان خبری جهانی و پوشش هم‌زمان رویدادها.",
     "پژوهش دربارهٔ رسانهٔ دیاسپورا و هویت فراملی.",
     "نقد گفتمان «اتصال جهانی» در سیاست فناوری.",
     "آموزش سواد رسانه‌ای دربارهٔ همبستگی و قطب‌بندی آنلاین."
   ],
   "evolution": "مک‌لوهان اصطلاح را در ۱۹۶۲ معرفی کرد و در «Understanding Media» (۱۹۶۴) بسط داد؛ پس از مرگ او، پاورز آن را در «The Global Village» (۱۹۸۹) گسترد. در دههٔ ۱۹۹۰، گفتمان اینترنت آن را بازتولید کرد و در دههٔ ۲۰۲۰، بحث پلتفرم‌های فراملی و حاکمیت داده آن را دوباره مسئله‌مند ساخت.",
   "key_concepts": ["دهکدهٔ جهانی (global village)", "بازقبیله‌ای‌شدن (retribalization)", "هم‌زمانی (simultaneity)", "فضای شنیداری (acoustic space)", "فروپاشی زمان و مکان", "ترور قبیله‌ای (tribal terror)"],
   "studies": ["McLuhan, M. (1962). The Gutenberg galaxy. University of Toronto Press.", "McLuhan, M., & Powers, B. R. (1989). The global village. Oxford University Press."],
   "detailed_analysis": "۱. بنیان و منطق نظری\nمک‌لوهان تاریخ رسانه را به سه دوره تقسیم کرد: شفاهی، چاپی و الکترونیک. در دورهٔ چاپ، فردگرایی و خطی‌بودن غالب شد؛ در دورهٔ الکترونیک، هم‌زمانی و مشارکت بازگشت. دهکدهٔ جهانی، نام همین بازگشت در مقیاس سیاره‌ای است.\n\n۲. دو خوانش از یک استعاره\nخوانش خوش‌بینانه، دهکدهٔ جهانی را مقدمهٔ همبستگی می‌بیند؛ خوانش بدبینانه، آن را بازگشت به نظارت و شایعهٔ قبیله‌ای می‌بیند. خود مک‌لوهان، هر دو را در متن خود دارد و همین دوگانگی، دلیل زنده‌ماندن استعاره است.\n\n۳. پیوند رسانه‌ای و نقد\nدر عصر پلتفرم، جهان هم‌زمان به هم متصل و قطبی است. استعاره، اتصال را می‌بیند اما نابرابری زیرساخت و قدرت پلتفرم را نه؛ ازاین‌رو باید آن را با اقتصاد سیاسی رسانه تکمیل کرد.",
   "critique_text": "\n".join([
     "۱. آرمانی‌سازی اتصال: نابرابری دسترسی، شکاف دیجیتال و سلطهٔ زیرساختی نادیده گرفته می‌شود؛ جهانِ متصل با جهانِ برابر یکی گرفته می‌شود.",
     "۲. شواهد معاصر: قطب‌بندی، اطلاعات نادرست و نفرت آنلاین نشان می‌دهد دهکدهٔ جهانی می‌تواند میدان نزاع باشد، نه همسایگی همدلانه.",
     "۳. ابهام و جبر فناورانه: مفهوم ادبی و غیرقابل سنجش است و روشن نمی‌کند چه کسی و با چه منافعی این دهکده را اداره می‌کند."]),
   "example_text": "یک بلای طبیعی در نیم‌کرهٔ دیگر، در همان لحظه در گوشی مخاطب حاضر می‌شود و کمک‌های مردمی فراملی را برمی‌انگیزد؛ اما همان زیرساخت، در همان روز می‌تواند ویدئویی تبلیغاتی و قطبی‌کننده را به میلیون‌ها نفر برساند. دهکدهٔ جهانی، هر دو را هم‌زمان ممکن می‌کند.",
 },
 "MC-336": {
   "summary": "«رسانه‌های گرم و سرد» (Hot and Cool Media) تقسیم‌بندی مک‌لوهان است: رسانهٔ گرم، یک حس را با وضوح بالا پر می‌کند و مشارکت مخاطب را کم می‌کند؛ رسانهٔ سرد، وضوح پایینی دارد و برای تکمیل معنا، مشارکت تفسیری بالایی می‌طلبد. این تقسیم‌بندی در فصل دوم «Understanding Media» (۱۹۶۴) آمده است (McLuhan, 1964).",
   "definition": "رسانهٔ گرم، رسانه‌ای است با «تعریف بالا» که داده را چنان کامل می‌دهد که مخاطب ناچار به تکمیل آن نیست؛ رسانهٔ سرد، «تعریف پایین» دارد و مخاطب را به پرکردن شکاف‌ها فرامی‌خواند (McLuhan, 1964).",
   "main_problem": "چرا رسانه‌های متفاوت، میزان مشارکت متفاوتی از مخاطب می‌طلبند؛ و این تفاوت در وضوح و مشارکت، چه پیامدهایی برای ادراک و فرهنگ دارد؟",
   "mechanism": "مفهوم بر چهار سازوکار استوار است. (۱) درجهٔ تعریف: میزان داده‌ای که رسانه فراهم می‌کند؛ عکس، دادهٔ بصری کامل می‌دهد و کاریکاتور، شکاف می‌گذارد. (۲) پراکندگی حواس: رسانهٔ گرم یک حس را اشباع می‌کند و رسانهٔ سرد، چند حس را درگیر می‌کند. (۳) مشارکت تکمیل‌کننده: مخاطب رسانهٔ سرد باید معنا را بسازد و همین مشارکت، او را عمیق‌تر درگیر می‌کند؛ تلفن نمونهٔ کلاسیک رسانهٔ سرد است. (۴) نمونه‌های مک‌لوهان: رادیو و چاپ و فیلم را گرم و تلفن و تلویزیون زمانهٔ او را سرد می‌دانست؛ تلویزیون، تصویر نقطه‌ای و کم‌وضوح می‌داد و مخاطب باید آن را در ذهن «ببست». (۵) پیامد فرهنگی: رسانهٔ گرم، تخصصی‌سازی و تفکیک حواس می‌آورد؛ رسانهٔ سرد، درگیری کل شخص و ساختار قبیله‌ای. در بستر رسانه، این تمایز برای تحلیل پادکست (صدای گرم و صمیمی، مشارکت خیال‌پردازانه)، ویدئوی کوتاه با تدوین سریع (گرم)، و بازی ویدئویی یا واقعیت مجازی (سرد، نیازمند تعامل) به‌کار می‌رود؛ هرچند فناوری‌های جدید، مرزهای این طبقه‌بندی را جابه‌جا می‌کنند.",
   "assumptions": [
     "رسانه‌ها در میزان داده‌ای که فراهم می‌کنند با هم تفاوت دارند.",
     "میزان مشارکت مخاطب، تابع وضوح رسانه است.",
     "تفاوت گرم و سرد، پیامدهای فرهنگی و ادراکی دارد."
   ],
   "principles": [
     "رسانهٔ گرم، دادهٔ کامل و مشارکت کم می‌دهد.",
     "رسانهٔ سرد، شکاف می‌گذارد و مشارکت می‌طلبد.",
     "درجهٔ مشارکت، تجربهٔ ادراکی را تعیین می‌کند."
   ],
   "critiques": [
     "طبقه‌بندی ناپایدار است: تلویزیون با ظهور تلویزیون با کیفیت بالا و بعدها ویدئوی دیجیتال، از «سرد» به «گرم» حرکت کرد و همین، معیار مک‌لوهان را متزلزل می‌کند.",
     "تعریف‌ها مبهم‌اند: «وضوح پایین» و «مشارکت» به‌طور عملیاتی سنجیده نشده‌اند و طبقه‌بندی تا حدی شهودی است.",
     "جبر فناورانه و غفلت از محتوا: تجربهٔ مشارکت، به محتوا و زمینهٔ فرهنگی نیز بستگی دارد، نه فقط به فرم رسانه."
   ],
   "applications": [
     "تحلیل تجربهٔ پادکست و رسانهٔ صوتی.",
     "طراحی تجربهٔ تعاملی در بازی، واقعیت مجازی و رابط کاربری.",
     "پژوهش دربارهٔ مشارکت مخاطب در رسانه‌های دیجیتال.",
     "آموزش تحلیل فرم رسانه و درجهٔ مشارکت."
   ],
   "evolution": "مک‌لوهان تقسیم‌بندی را در ۱۹۶۴ مطرح کرد و در نوشته‌های بعدی بسط داد؛ با ظهور رسانه‌های تعاملی، مفهوم «سرد» به تحلیل بازی و واقعیت مجازی منتقل شد و در دههٔ اخیر، بحث «رسانهٔ گرم» در تحلیل پادکست و ویدئوی کوتاه بازتولید شده است.",
   "key_concepts": ["رسانهٔ گرم (hot medium)", "رسانهٔ سرد (cool medium)", "تعریف بالا و پایین (high/low definition)", "مشارکت مخاطب (participation)", "اشباع حسی (sensory saturation)"],
   "studies": ["McLuhan, M. (1964). Understanding media (ch. 2: Media hot and cold). McGraw-Hill.", "McLuhan, M. (1962). The Gutenberg galaxy. University of Toronto Press."],
   "detailed_analysis": "۱. بنیان و منطق نظری\nمک‌لوهان از تفاوت تجربهٔ رادیو و تلفن آغاز کرد: رادیو، صدا را در فضایی پر می‌کند و تلفن، فقط رشته‌ای از صدا می‌دهد که شنونده باید آن را کامل کند. از همین تفاوت شهودی، دوگانهٔ گرم/سرد ساخته شد.\n\n۲. چرا طبقه‌بندی می‌لرزد\nفناوری‌ها ثابت نیستند: تلویزیون از تصویر نقطه‌ای به تصویر پرتعریف حرکت کرد و بازی ویدئویی، مشارکت را به کنش بدل کرد. بنابراین گرم/سرد بیشتر یک محور نسبی است تا دو دستهٔ ثابت.\n\n۳. پیوند رسانه‌ای و نقد\nارزش مفهوم در این است که مشارکت مخاطب را به فرم رسانه گره می‌زند. اما بدون سنجش عملیاتی و با نادیده‌گرفتن محتوا، خطر آن هست که به برچسبی شهودی بدل شود. بهترین کاربرد آن، پرسش تحلیلی است: این رسانه چه اندازه از معنا را می‌دهد و چه اندازه را به مخاطب وامی‌گذارد؟",
   "critique_text": "\n".join([
     "۱. ناپایداری طبقه‌بندی: تلویزیون با ارتقای کیفیت تصویر از «سرد» به «گرم» حرکت کرد و همین نشان می‌دهد معیار مک‌لوهان ثابت نیست.",
     "۲. ابهام عملیاتی: «وضوح پایین» و «مشارکت» سنجهٔ روشنی ندارند و طبقه‌بندی تا حدی شهودی و وابسته به داوری است.",
     "۳. غفلت از محتوا و زمینه: تجربهٔ مشارکت به محتوا و فرهنگ نیز بستگی دارد، نه فقط به فرم رسانه."]),
   "example_text": "پادکست، رسانه‌ای گرم و صمیمی است: صدا در گوش مخاطب حاضر است و او را به همسخنی نزدیک می‌کند؛ در برابر آن، بازی ویدئویی رسانه‌ای سرد است، زیرا تا مخاطب دست به کار نشود، رویداد کامل نمی‌شود. همین تفاوت، شکل مشارکت و وفاداری مخاطب را توضیح می‌دهد.",
 },
 "MC-337": {
   "summary": "«سوگیری رسانه‌ها» در معنای اینیس به معنای جانبداری حزبی نیست، بلکه به گرایش ساختاری هر رسانه اشاره دارد: جنس و شکل رسانه، به برخی روابط اجتماعی جهت می‌دهد. هارولد اینیس در «The Bias of Communication» (۱۹۵۱، University of Toronto Press) رسانه‌ها را به دو دستهٔ «دارای سوگیری زمانی» و «دارای سوگیری مکانی» تقسیم کرد (Innis, 1951).",
   "definition": "سوگیری رسانه، تمایل ساختاری یک رسانه به حفظ یا گسترش نوع خاصی از نظم اجتماعی است: رسانه‌های سنگین و بادوام به زمان و سنت سوگیری دارند و رسانه‌های سبک و قابل حمل به مکان و ادارهٔ قلمرو (Innis, 1951).",
   "main_problem": "چرا تمدن‌ها با تغییر رسانه‌های ارتباطی، دگرگون می‌شوند؛ و چگونه جنس مادی رسانه، ساختار قدرت، حافظه و گسترش امپراتوری را تعیین می‌کند؟",
   "mechanism": "تحلیل اینیس بر پنج سازوکار استوار است. (۱) مادیت رسانه: سنگ، خشت، پوست و کاغذ، هر یک قابلیت‌های متفاوتی برای دوام و حمل دارند. (۲) سوگیری زمانی: رسانه‌های سنگین و بادوام — سنگ‌نوشته، خشت، دست‌نوشتهٔ پوستی — حافظه را در طول نسل‌ها حفظ می‌کنند و به سنت، دین و سلسله‌مراتب پایدار جهت می‌دهند. (۳) سوگیری مکانی: رسانه‌های سبک و قابل حمل — پاپیروس، کاغذ، چاپ — انتقال سریع در پهنهٔ جغرافیایی را ممکن می‌کنند و به ادارهٔ امپراتوری، تجارت و گسترش قلمرو جهت می‌دهند. (۴) انحصار دانش: گروهی که رسانه را در اختیار دارد، دانش و قدرت را انحصاری می‌کند؛ کاهنان، کاتبان و دیوان‌سالاران نمونه‌های تاریخی آن‌اند. (۵) تعادل و فروپاشی: تمدن‌های پایدار، میان سوگیری زمانی و مکانی تعادل برقرار می‌کنند و فروپاشی، اغلب هنگام غلبهٔ یک سوگیری رخ می‌دهد. در بستر رسانه، این چارچوب برای تحلیل آرشیو و سیاست حفظ حافظه، مقررات پخش (طیف فرکانس به‌عنوان منبع مکانی) و پلتفرم‌های دیجیتال (انتقال آنی و فرامرزی) به‌کار می‌رود؛ پلتفرم، هم‌زمان سوگیری مکانی شدید و حافظهٔ کوتاه دارد، ترکیبی که پرسش‌های تازه‌ای دربارهٔ تداوم فرهنگی می‌سازد.",
   "assumptions": [
     "جنس مادی رسانه، قابلیت‌های اجتماعی آن را محدود و جهت‌دار می‌کند.",
     "سوگیری رسانه به ساختار قدرت و نوع دانش شکل می‌دهد.",
     "تعادل میان سوگیری‌ها، شرط پایداری تمدن است."
   ],
   "principles": [
     "هر رسانه، سوگیری زمانی یا مکانی دارد.",
     "کنترل رسانه، امکان انحصار دانش می‌سازد.",
     "غلبهٔ یک سوگیری، تمدن را آسیب‌پذیر می‌کند."
   ],
   "critiques": [
     "جبر فناورانه و تعمیم تاریخی: نظریه با شواهد تاریخی گسترده اما گزینشی کار می‌کند و عوامل اقتصادی، سیاسی و انسانی را کم‌رنگ می‌بیند.",
     "دوگانهٔ زمانی/مکانی، طیف پیچیدهٔ رسانه‌های امروز را ساده می‌کند؛ رسانهٔ دیجیتال هم‌زمان مکان و زمان را دگرگون می‌کند.",
     "مفهوم، بیشتر چارچوب تفسیری است تا نظریهٔ آزمون‌پذیر؛ سنجش «سوگیری» یک رسانهٔ مشخص دشوار است."
   ],
   "applications": [
     "تحلیل سیاست آرشیو و حفظ حافظهٔ رسانه‌ای.",
     "پژوهش دربارهٔ مقررات پخش و تخصیص طیف فرکانس.",
     "نقد حافظهٔ کوتاه و گذرایی در پلتفرم‌های دیجیتال.",
     "مطالعهٔ رابطهٔ رسانه، قدرت و گسترش قلمرو."
   ],
   "evolution": "اینیس اندیشه را در «Empire and Communications» (۱۹۵۰) آغاز کرد و در «The Bias of Communication» (۱۹۵۱) نظام‌مند ساخت؛ مک‌لوهان، همکار و وارث او در تورنتو، آن را به سمت نظریهٔ رسانه و ادراک برد و در دههٔ اخیر، مطالعات زیرساخت رسانه آن را بازخوانی کرده است.",
   "key_concepts": ["سوگیری رسانه (bias of communication)", "سوگیری زمانی (time bias)", "سوگیری مکانی (space bias)", "انحصار دانش (monopoly of knowledge)", "مادیت رسانه (materiality of media)", "تعادل رسانه‌ای"],
   "studies": ["Innis, H. A. (1951). The bias of communication. University of Toronto Press.", "Innis, H. A. (1950). Empire and communications. Clarendon Press."],
   "detailed_analysis": "۱. بنیان و منطق نظری\nاینیس، اقتصاددان تاریخ‌نگار، از تحلیل تجارت و امپراتوری به رسانه رسید: هر امپراتوری برای ادارهٔ پهنهٔ گسترده، به رسانهٔ قابل حمل نیاز دارد و هر سنت دینی برای دوام، به رسانهٔ بادوام. از همین دو نیاز، دو سوگیری زاده شد.\n\n۲. مفهوم انحصار دانش\nرسانه فقط ابزار انتقال نیست؛ دسترسی به آن، قدرت می‌سازد. کاهنان مصر با کنترل نوشتار، دانش را انحصاری کردند و دیوان‌سالاری با کنترل بایگانی، اقتدار خود را تثبیت کرد. این ایده، بنیان تحلیل رابطهٔ دانش و قدرت در رسانه است.\n\n۳. پیوند رسانه‌ای و نقد\nدر عصر دیجیتال، سوگیری‌ها در هم تنیده‌اند: پلتفرم، انتقال مکانی آنی می‌دهد و حافظهٔ زمانی کوتاه. این ترکیب، پرسش اینیس را زنده می‌کند: چه کسی دانش را در انحصار دارد و تمدن، برای تعادل چه می‌کند؟ نقد اصلی، تعمیم تاریخی و کم‌توجهی به عاملیت انسانی است.",
   "critique_text": "\n".join([
     "۱. جبر فناورانه و تعمیم گزینشی: نظریه با نمونه‌های تاریخی گسترده اما انتخابی کار می‌کند و نقش عوامل اقتصادی، سیاسی و انسانی را کم‌رنگ می‌بیند.",
     "۲. ساده‌سازی دوگانه: تقسیم زمانی/مکانی، رسانه‌های دیجیتال را که هم‌زمان زمان و مکان را دگرگون می‌کنند، به‌سختی توضیح می‌دهد.",
     "۳. آزمون‌ناپذیری: مفهوم بیشتر چارچوب تفسیری است تا نظریهٔ قابل سنجش؛ تعیین دقیق سوگیری یک رسانهٔ مشخص دشوار است."]),
   "example_text": "کتیبهٔ سنگی، پیامی برای نسل‌های آینده و تثبیت اقتدار دینی است؛ روزنامهٔ چاپی، پیامی برای گسترش سریع در پهنهٔ ملی و ادارهٔ افکار است. هر دو رسانه‌اند، اما سوگیری‌شان متفاوت است و ساختار قدرت متفاوتی را ممکن می‌کنند.",
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
    codes = ["MC-334", "MC-335", "MC-336", "MC-337"]
    cur.execute("SELECT id, code, properties FROM kb_entities WHERE code IN (%s)" % ",".join(["%s"]*len(codes)), codes)
    rows = {code:(eid, json.loads(pr)) for (eid, code, pr) in cur.fetchall()}
    with open(BACKUP, "w", encoding="utf-8") as f:
        json.dump([{"code": cd, "props": rows[cd][1]} for cd in codes if cd in rows], f, ensure_ascii=False, indent=1)
    print("backup ->", len(rows), "rows")

    for code in codes:
        eid, p = rows[code]
        e = ENRICH[code]
        if "critique_text" in e: p["critique"] = e["critique_text"]
        if "example_text" in e: p["example"] = e["example_text"]
        for k, v in e.items():
            if k in ("critique_text", "example_text"): continue
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
                     "documented sourcing + rubric score; corrected mismatched boilerplate where present", STAMP, NOW))
        cur.execute("INSERT INTO kb_audit_log (entity_code, action, detail, source) VALUES (%s,%s,%s,%s)",
                    (code, "DOC_ENRICH", json.dumps({"quality_score": score, "words": words, "sources": n_sources, "verified": n_verified, "breakdown": detail}, ensure_ascii=False), STAMP))
        print(f"{code}: score={score} words={words} sources={n_sources} verified={n_verified} relations={n_relations} | {detail}")
    c.commit()
    c.close()
    print("BATCH64 THEORY DONE")

if __name__ == "__main__":
    main()
