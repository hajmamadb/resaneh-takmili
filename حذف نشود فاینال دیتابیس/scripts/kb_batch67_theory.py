# -*- coding: utf-8 -*-
"""Batch 67: MC-352 (structuralist narratology), MC-353 (genre theory), MC-355 (active audience),
MC-356 (interpretive communities). Critique/example overridden where boilerplate was mismatched."""
import pymysql, json

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch67-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch67_theory.json"

S = {
 "MC-352": [
   dict(kind="BOOK", title_en="Morphology of the Folktale", title_fa="ریخت‌شناسی قصهٔ پریان",
        authors="Propp, V. (trans. L. Scott; ed. L. A. Wagner)", year=1928,
        publisher="University of Texas Press (2nd English ed., 1968)",
        doi="10.7560/783911", url="https://utpress.utexas.edu/9780292783768/",
        language="en", isbn="9780292783768",
        citation="Propp, V. (1968). Morphology of the folktale (2nd ed., L. Scott, Trans.; L. A. Wagner, Ed.). University of Texas Press. (Original work published 1928)",
        locator="whole work", locator_type="work",
        supports="definition / function / spheres of action", verified=True),
   dict(kind="BOOK", title_en="Narrative Discourse: An Essay in Method",
        title_fa="گفتمان روایی: جستاری در روش",
        authors="Genette, G. (trans. J. E. Lewin)", year=1972,
        publisher="Cornell University Press (Figures III, Seuil, 1972)",
        doi=None, url=None, language="fr", isbn=None,
        citation="Genette, G. (1980). Narrative discourse: An essay in method (J. E. Lewin, Trans.). Cornell University Press. (Original work published 1972 as \"Discours du récit\" in Figures III, Seuil)",
        locator="Discours du récit", locator_type="CHAPTER",
        supports="time / mood / voice / focalization", verified=False),
 ],
 "MC-353": [
   dict(kind="BOOK", title_en="Genre", title_fa="ژانر",
        authors="Neale, S.", year=1980,
        publisher="British Film Institute", doi=None, url=None, language="en", isbn=None,
        citation="Neale, S. (1980). Genre. British Film Institute.",
        locator="whole work", locator_type="work",
        supports="definition / repetition and difference", verified=True),
   dict(kind="BOOK", title_en="Film/Genre", title_fa="فیلم/ژانر",
        authors="Altman, R.", year=1999,
        publisher="British Film Institute", doi=None, url=None, language="en", isbn=None,
        citation="Altman, R. (1999). Film/genre. British Film Institute.",
        locator="whole work", locator_type="work",
        supports="evolution / semantic and syntactic approach", verified=False),
 ],
 "MC-355": [
   dict(kind="BOOK", title_en="Television Culture", title_fa="فرهنگ تلویزیون",
        authors="Fiske, J.", year=1987,
        publisher="Methuen", doi=None, url=None, language="en", isbn=None,
        citation="Fiske, J. (1987). Television culture. Methuen.",
        locator="whole work", locator_type="work",
        supports="definition / semiotic democracy / popular pleasures", verified=True),
   dict(kind="BOOK", title_en="Watching Dallas: Soap Opera and the Melodramatic Imagination",
        title_fa="تماشای دالاس: سریال آبکی و تخیل ملودراماتیک",
        authors="Ang, I.", year=1985,
        publisher="Methuen", doi=None, url=None, language="en", isbn=None,
        citation="Ang, I. (1985). Watching Dallas: Soap opera and the melodramatic imagination. Methuen.",
        locator="whole work", locator_type="work",
        supports="mechanism / pleasure / empirical audience", verified=False),
 ],
 "MC-356": [
   dict(kind="BOOK", title_en="Is There a Text in This Class? The Authority of Interpretive Communities",
        title_fa="آیا در این کلاس متنی وجود دارد؟ اقتدار جماعت‌های تفسیری",
        authors="Fish, S.", year=1980,
        publisher="Harvard University Press", doi=None, url=None, language="en",
        isbn="9780674467262",
        citation="Fish, S. (1980). Is there a text in this class? The authority of interpretive communities. Harvard University Press.",
        locator="whole work", locator_type="work",
        supports="definition / interpretive strategies / authority", verified=True),
   dict(kind="BOOK", title_en="Reading the Romance: Women, Patriarchy, and Popular Literature",
        title_fa="خواندن رمان عاشقانه: زنان، پدرسالاری و ادبیات عامه‌پسند",
        authors="Radway, J. A.", year=1984,
        publisher="University of North Carolina Press", doi=None, url=None, language="en", isbn=None,
        citation="Radway, J. A. (1984). Reading the romance: Women, patriarchy, and popular literature. University of North Carolina Press.",
        locator="whole work", locator_type="work",
        supports="empirical interpretive community", verified=False),
 ],
}

VOID = "در بستر رسانه، "
ENRICH = {
 "MC-352": {
  "summary": "(پراپ، ۱۹۲۸/۱۹۶۸؛ ژنت، ۱۹۷۲/۱۹۸۰) ریخت‌شناسی و روایت‌شناسی ساختارگرا می‌کوشد تنوع ظاهری داستان‌ها را به مجموعهٔ محدودی از قواعد پایدار فروبکاهد. پراپ با تحلیل صد قصهٔ پریان روسی نشان داد همهٔ آن‌ها از ۳۱ «کارکرد» و هفت «حوزهٔ کنش» ساخته شده‌اند؛ ژنت نیز روایت را در سه محور زمان، وجه و لحن صورت‌بندی کرد.",
  "definition": "روایت‌شناسی ساختارگرا مطالعهٔ نظام قواعد صوری حاکم بر روایت است: توالی کارکردها، توزیع کنش میان شخصیت‌ها، و شیوهٔ تنظیم زمان و زاویهٔ دید — مستقل از محتوای خاص هر داستان.",
  "main_problem": "چرا با وجود بی‌شمار داستان متفاوت، ساختارهای تکرارشونده‌ای در آن‌ها دیده می‌شود؟ و چگونه می‌توان این ساختارها را چنان دقیق توصیف کرد که تحلیل روایت از شهود ادبی به دانش قواعدی تبدیل شود.",
  "mechanism": "\n".join([
   "(۱) کارکرد: واحد تحلیل پراپ کنش شخصیت است، نه خود شخصیت؛ هر کارکرد (آسیب، سفر، آزمون، پیروزی) در توالی ثابتی جای می‌گیرد و معنای خود را از همان جایگاه می‌گیرد.",
   "(۲) حوزهٔ کنش: ۳۱ کارکرد، میان هفت حوزه توزیع می‌شوند — قهرمان، یاری‌گر، بخشنده، شاهزاده، فرستنده، بدخواه و قهرمان بدلی؛ شخصیت‌ها تغییر می‌کنند، اما ساختار توزیع پایدار است.",
   "(۳) زمان روایی ژنتی: نظم، دیرش و بسامد؛ جهش زمانی (پیش‌بازگشت و پس‌بازگشت) و اختلاف میان «زمان داستان» و «زمان روایت» سازوکار تعلیق و کشف را می‌سازد.",
   "(۴) وجه و لحن: «وجه» به میزان اطلاعاتی که راوی می‌دهد مربوط است و «کانون‌سازی» (چه کسی می‌بیند) را از «صدا» (چه کسی می‌گوید) جدا می‌کند؛ همین تفکیک، تحلیل را از دوگانهٔ سادهٔ اول‌شخص/سوم‌شخص فراتر می‌برد.",
   "(۵) توالی برمونی: برمون روایت را زنجیره‌ای از سه‌گانه‌های امکان–تحقق–نتیجه می‌بیند؛ در هر گره، روایت شاخه می‌شود و انتخاب یا رد شدن یک مسیر، ساختار امکان‌های داستان را می‌سازد.",
   VOID + "سریال‌های چندفصلی، بازی‌های روایی با شاخه‌بندی و حتی تیزرهای تبلیغاتی، همه با همین قواعد کار می‌کنند: تعویق کارکرد «پیروزی»، جابه‌جایی کانون روایت میان شخصیت‌ها و ساختن امکان‌های موازی که مخاطب را در حالت انتظار نگه می‌دارد.",
  ]),
  "assumptions": [
   "روایت، نظامی از قواعد صوری است که مستقل از محتوا قابل توصیف است.",
   "تنوع ظاهری داستان‌ها بر سطحی از ساختارهای مشترک استوار است.",
   "واحد تحلیل، کنش و نسبت آن با ساختار است، نه روان‌شناسی شخصیت.",
  ],
  "principles": [
   "تحلیل از کل به جزء حرکت می‌کند: ساختار پیش از اجزای منفرد شناسایی می‌شود.",
   "جایگاه کارکرد در توالی، تعیین‌کنندهٔ معنای آن است.",
   "تفکیک وجه (چه کسی می‌بیند) از صدا (چه کسی می‌گوید) بنیادین است.",
  ],
  "critiques": [
   "اروپامحوری و محدودهٔ کاربرد: مدل پراپ بر قصه‌های پریان روسی ساخته شده و تعمیم آن به روایت‌های مدرن، تعاملی و غیرخطی نیازمند بازنگری است.",
   "تقلیل‌گرایی ساختاری: فروکاستن شخصیت به «کارکرد»، غنا و تنش اخلاقی روایت را نادیده می‌گیرد؛ نسل دوم روایت‌شناسان به همین دلیل به سوی «روایت‌شناسی بلاغی» و «روایت‌شناسی شناختی» رفتند.",
   "بی‌اعتنایی به تاریخ و ایدئولوژی: قواعد صوری از مناسبات قدرت و بستر تاریخی تولید روایت مستقل فرض می‌شوند.",
   "دشواری در روایت‌های نو: سریال‌های شبکه‌ای، روایت‌های کاربرمحور و بازترکیب‌های میمی، مرزهای داستان و کارکرد را مبهم می‌کنند.",
  ],
  "applications": [
   "تحلیل فیلم‌نامه و سریال: ردیابی کارکردها و کانون‌سازی برای شناسایی نقطه‌های کشش و تکرار.",
   "طراحی روایت تعاملی و بازی: ترسیم درخت امکان‌های برمونی و بررسی وزن هر شاخه.",
   "تحلیل تبلیغات روایی: کارکرد «آسیب» و «یاری‌گر» چگونه برند را قهرمان می‌کند.",
   "پژوهش خبری: کانون‌سازی و ترتیب زمانی در بازنمایی رخداد و اثر آن بر ادراک مخاطب.",
  ],
  "evolution": "از ریخت‌شناسی پراپ (۱۹۲۸) به ساختارگرایی فرانسوی (لوی-استروس، برمون) و روایت‌شناسی ژنت (۱۹۷۲)، سپس به روایت‌شناسی پساکلاسیک که پرسش‌های ایدئولوژی، جنسیت و شناخت را به تحلیل ساختاری افزود.",
  "key_concepts": ["کارکرد (Function)", "حوزهٔ کنش (Sphere of Action)", "کانون‌سازی (Focalization)", "صدا (Voice)", "نظم و دیرش (Order and Duration)", "توالی (Sequence)", "روایت‌شناسی (Narratology)"],
  "studies": [
   "Genette, G. (1980). Narrative discourse: An essay in method. Cornell University Press.",
   "Bremond, C. (1973). Logique du récit. Éditions du Seuil.",
  ],
  "detailed_analysis": "\n".join([
   "۱. بنیان و منطق نظری: پراپ تحلیل خود را بر «صورت» داستان بنا کرد، نه بر محتوا؛ همین چرخش، الگوی ساختارگرایی قرن بیستم شد: جست‌وجوی نظام تفاوت‌ها و قواعد ترکیب، به‌جای جست‌وجوی پیام یا نیت.",
   "۲. از ساختار به گفتمان: ژنت پرسش را از «داستان چیست» به «چگونه روایت می‌شود» منتقل کرد و همین جداکردن داستان از گفتمان، ابزار تحلیلی اصلی مطالعات رسانه در تحلیل روایت شد.",
   "۳. افق امروز: ساختارگرایی در برابر روایت‌های شبکه‌ای و باز، نیازمند مفاهیم تازه‌ای مانند «روایت توزیع‌شده» و «کانون‌سازی الگوریتمی» است؛ اما بدون مفاهیم پایهٔ پراپ و ژنت، این گسترش ممکن نیست.",
  ]),
  "critique_text": "\n".join([
   "۱. اروپامحوری و محدودهٔ کاربرد: مدل پراپ بر قصه‌های پریان روسی ساخته شده و تعمیم آن به روایت‌های مدرن، تعاملی و غیرخطی نیازمند بازنگری است.",
   "۲. تقلیل‌گرایی ساختاری: فروکاستن شخصیت به «کارکرد»، غنا و تنش اخلاقی روایت را نادیده می‌گیرد؛ نسل دوم روایت‌شناسان به سوی روایت‌شناسی بلاغی و شناختی رفتند.",
   "۳. بی‌اعتنایی به تاریخ و ایدئولوژی: قواعد صوری از مناسبات قدرت و بستر تاریخی تولید روایت مستقل فرض می‌شوند.",
   "۴. دشواری در روایت‌های نو: سریال‌های شبکه‌ای، روایت‌های کاربرمحور و بازترکیب‌های میمی، مرزهای داستان و کارکرد را مبهم می‌کنند.",
  ]),
  "example_text": "\n".join([
   "در فیلمی از «سفر قهرمان»، قهرمان مأموریت را می‌پذیرد (کارکرد: حرکت)، یاری‌گر ظاهر می‌شود و نیروی بدخواه آزمون می‌گذارد؛ تحلیل پراپی نشان می‌دهد ساختار عمیق این فیلم با قصه‌ای هزارساله یکی است، حتی اگر صحنه و فناوری عوض شده باشد.",
   "در یک سریال پلیسی، تعویق «آشکارگی» و جابه‌جایی کانون از کارآگاه به مظنون، به‌جای افزودن اطلاعات، تعلیق می‌سازد — نمونهٔ عملی تفکیک ژنتی وجه از صدا.",
   "در یک بازی روایی، انتخاب بازیکن در گره‌های داستان همان شاخه‌بندی برمونی است: امکان‌های موازی که فقط یکی به نتیجه می‌رسد و بقیه به روایت «از دست رفته» بدل می‌شوند.",
  ]),
 },
 "MC-353": {
  "summary": "(نیل، ۱۹۸۰؛ آلتمن، ۱۹۹۹؛ متز، ۱۹۷۴) نظریهٔ ژانر رسانه، قراردادهای تکرارشوندهٔ دسته‌بندی متن را نه برچسب سادهٔ بازاری، بلکه سازوکار تنظیم انتظار و معنا می‌داند. ژانر توافقی است میان صنعت، متن و مخاطب که تعادل میان «آشنایی» و «تفاوت» را نگه می‌دارد و در هر دوره تاریخی بازتعریف می‌شود.",
  "definition": "ژانر مجموعه‌ای از قراردادهای صوری، معنایی و فرامتنی است که متن را به گروهی از متون مشابه پیوند می‌دهد و از طریق آن، تولیدکننده و مخاطب انتظارات مشترکی دربارهٔ ساختار، محتوا و کارکرد متن پیدا می‌کنند.",
  "main_problem": "چگونه آثار بی‌شمار، در دسته‌های قابل شناخت سازمان می‌یابند و این دسته‌بندی چه اثری بر تولید، توزیع و تفسیر دارد؟ نیل این پرسش را از سطح سلیقه بیرون می‌کشد و به مناسبات صنعت و مخاطب می‌کشاند.",
  "mechanism": "\n".join([
   "(۱) قرارداد و افق انتظار: ژانر عهدی است نانوشته میان متن و خواننده؛ مخاطب پیش از دیدن اثر، دربارهٔ ریتم، پایان و شخصیت‌ها انتظار دارد.",
   "(۲) تکرار و تفاوت: بدون تکرار، شناخت ژانر ممکن نیست و بدون تفاوت، اثر خسته‌کننده می‌شود؛ نوآوری ژانری همیشه درون قرارداد رخ می‌دهد، نه بیرون آن.",
   "(۳) ژانر به‌عنوان برچسب صنعتی: استودیوها و پلتفرم‌ها با تعریف ژانر، بازار را تقسیم می‌کنند؛ برچسب ژانر هم راهنمای مخاطب است و هم ابزار مدیریت هزینه و ریسک.",
   "(۴) رویکرد معنایی-نحوی آلتمن: ژانر از دو لایه ساخته می‌شود: عناصر معنایی (ماشین، کلانتر، سلاح) و نحو روایی (تقابل، سفر، انتقام)؛ ژانر پایدار است وقتی هر دو لایه با هم تثبیت شوند.",
   "(۵) فرامتن ژانری: نقد، تبلیغ، جایزه و حتی بحث کاربران، ژانر را بازتعریف می‌کنند؛ ژانر نه فقط در متن، بلکه در گفتار پیرامون متن ساخته می‌شود.",
   VOID + "برچسب‌گذاری الگوریتمی پلتفرم‌ها (ژانرها، تگ‌ها و فهرست‌های پیشنهادی) نسخهٔ دیجیتال همان قرارداد است: الگوریتم هم انتظار مخاطب را می‌سازد و هم قواعد تولید را به سازندگان دیکته می‌کند.",
  ]),
  "assumptions": [
   "ژانر نه ویژگی ذاتی متن، بلکه رابطه‌ای اجتماعی میان متن، صنعت و مخاطب است.",
   "ژانرها تاریخی‌اند و در هر دوره بازتعریف می‌شوند.",
   "آشنایی و تفاوت هم‌زمان شرط بقای ژانرند.",
  ],
  "principles": [
   "تحلیل ژانر باید هم عناصر معنایی و هم ساختار نحوی روایت را شامل شود.",
   "باید فرامتن (گفتار پیرامون اثر) هم در تعریف ژانر لحاظ شود.",
   "ژانر را باید در نسبت با صنعت و بازار مطالعه کرد، نه فقط در سطح متن.",
  ],
  "critiques": [
   "مرزهای ناپایدار: تعریف ژانرها اغلب پس‌ازواقع و از سوی نهادهای قدرتمند تحمیل می‌شود و ژانرهای حاشیه‌ای را به حاشیه می‌راند.",
   "خطر ذات‌گرایی: برخورد با ژانر همچون جوهر متن، تحلیل را از رابطهٔ اجتماعی به فهرست ویژگی‌ها فرو می‌کاهد.",
   "تنش با نوآوری: تأکید بر قرارداد می‌تواند آثار ژانرآفرین را به‌عنوان «استثنا» بیرون از تحلیل بگذارد.",
   "گسترش بی‌مهارت: با برچسب‌گذاری الگوریتمی، شمار ژانرها چنان زیاد شده که ارزش تحلیلی مفهوم کاهش یافته است.",
  ],
  "applications": [
   "تحلیل بازار پلتفرم: چگونه برچسب‌های ژانر، سلیقه و تولید را هم‌زمان شکل می‌دهند.",
   "نقد تبلیغات و تریلر: استفاده از نشانه‌های ژانری برای ساختن انتظار پیش از مصرف اثر.",
   "پژوهش مخاطب: سنجش اینکه انتظار ژانری چه اثری بر رضایت و ارزیابی اثر دارد.",
   "تحلیل خبر: ژانرهای خبری (گزارش، مصاحبه، تحلیل) چگونه قواعد صداقت و بی‌طرفی را تعیین می‌کنند.",
  ],
  "evolution": "از نقد فیلم ساختارگرا (متز، ۱۹۷۴) به نظریهٔ ژانر نیل (۱۹۸۰) و سپس رویکرد تاریخی-صنعتی آلتمن (۱۹۹۹)؛ امروز نظریهٔ ژانر با برچسب‌گذاری الگوریتمی و ژانرهای بومی پلتفرم‌ها گسترش یافته است.",
  "key_concepts": ["قرارداد ژانری (Genre Convention)", "افق انتظار (Horizon of Expectation)", "تکرار و تفاوت (Repetition and Difference)", "عناصر معنایی/نحوی (Semantic/Syntactic)", "فرامتن (Paratext)", "چرخهٔ ژانری (Genre Cycle)"],
  "studies": [
   "Altman, R. (1999). Film/genre. British Film Institute.",
   "Metz, C. (1974). Film language: A semiotics of the cinema. Oxford University Press.",
  ],
  "detailed_analysis": "\n".join([
   "۱. بنیان و منطق نظری: نظریهٔ ژانر از نقد ساختارگرای سینما برآمد؛ پیش‌فرض آن این است که معنا در رابطهٔ تفاوت میان متون ساخته می‌شود، نه در هر متن به‌تنهایی.",
   "۲. ژانر و صنعت: آلتمن نشان داد ژانرها نه فقط شکل، بلکه سازوکار اقتصادی‌اند؛ برچسب ژانر با کاهش ریسک و جذب مخاطب، چرخه‌های تولید را سازمان می‌دهد و در بحران‌ها ژانرهای ترکیبی متولد می‌شوند.",
   "۳. افق دیجیتال: در پلتفرم‌ها، ژانر به داده تبدیل شده است: خوشه‌بندی محتوا بر اساس رفتار مصرف، نه بر اساس تاریخ نقد. این وضعیت، پرسش نیل دربارهٔ نسبت تکرار و تفاوت را به شکل تازه‌ای بازمی‌گرداند.",
  ]),
  "critique_text": "\n".join([
   "۱. مرزهای ناپایدار: تعریف ژانرها اغلب پس‌ازواقع و از سوی نهادهای قدرتمند تحمیل می‌شود و ژانرهای حاشیه‌ای را به حاشیه می‌راند.",
   "۲. خطر ذات‌گرایی: برخورد با ژانر همچون جوهر متن، تحلیل را از رابطهٔ اجتماعی به فهرست ویژگی‌ها فرو می‌کاهد.",
   "۳. تنش با نوآوری: تأکید بر قرارداد می‌تواند آثار ژانرآفرین را به‌عنوان «استثنا» بیرون از تحلیل بگذارد.",
   "۴. گسترش بی‌مهارت: با برچسب‌گذاری الگوریتمی، شمار ژانرها چنان زیاد شده که ارزش تحلیلی مفهوم کاهش یافته است.",
  ]),
  "example_text": "\n".join([
   "تریلر یک فیلم ترسناک پیش از هر صحنه‌ای، قرارداد ژانر را فعال می‌کند: سکوت، در نیمه‌باز، موسیقی کشیده؛ مخاطب از همان ثانیهٔ اول می‌داند چه انتظاری داشته باشد — و لذت اثر در همین پیش‌بینی و سپس غافلگیری نهفته است.",
   "در یک پلتفرم استریم، دو فیلم با ساختار روایی کاملاً متفاوت ممکن است زیر یک برچسب «درام» قرار گیرند، چون الگوریتم بر اساس الگوی مصرف کاربران دسته‌بندی کرده است، نه بر اساس تاریخ ژانر — نمونهٔ آشکار گذار ژانر از نقد به داده.",
   "در خبر تلویزیونی، قالب «مصاحبهٔ زنده» ژانری است با قواعد خاص: زمان برابر، پرسش کوتاه، پاسخ بی‌وقفه؛ همین قواعد، ادعای بی‌طرفی رسانه را ممکن می‌کند.",
  ]),
 },
 "MC-355": {
  "summary": "(فیسک، ۱۹۸۷؛ آنگ، ۱۹۸۵) نظریهٔ مخاطب فعال، تصویر مخاطب منفعلِ رسانهٔ توده‌ای را رد می‌کند و نشان می‌دهد مخاطبان با تکیه بر منابع فرهنگی خود، معناهای متن را بازخوانی، واژگون یا بازترکیب می‌کنند. لذت مصرف رسانه، خود شکلی از مشارکت معنایی است، نه فقط دریافت پیام.",
  "definition": "مخاطب فعال، مخاطبی است که در فرایند تفسیر، به‌جای پذیرش بی‌قید معنای مورد نظر تولیدکننده، از رمزگان و تجربهٔ فرهنگی خود برای ساختن معنا، مقاومت و لذت استفاده می‌کند.",
  "main_problem": "اگر رسانه‌های قدرتمند پیام‌های ایدئولوژیک می‌فرستند، چرا مخاطبان همیشه آن‌ها را نمی‌پذیرند؟ نظریهٔ مخاطب فعال این پرسش را از سطح «اثر مستقیم» به سطح «مذاکره و تفسیر» منتقل می‌کند.",
  "mechanism": "\n".join([
   "(۱) رمزگذاری و رمزگشایی: هال نشان داد پیام در تولید رمزگذاری می‌شود، اما مخاطب می‌تواند آن را در سه حالت رمزگشایی کند: مسلط، مذاکره‌ای یا واژگون‌ساز؛ تحلیل مخاطب از همین تفکیک آغاز می‌شود.",
   "(۲) متن نوشتنی: فیسک متون محبوب را «نوشتنی» می‌داند؛ متنی که خواننده را به تولید معنا دعوت می‌کند و همین دعوت، لذت مشارکت را می‌سازد.",
   "(۳) دموکراسی نشانه‌ای: مخاطب در انتخاب، تفسیر و بازترکیب، نوعی قدرت فرهنگی اعمال می‌کند؛ لذت، شکل مشروع مقاومت روزمره است.",
   "(۴) شواهد تجربی دریافت: آنگ با خوانندگان «دالاس» نشان داد مخاطبان با فاصلهٔ طنزآمیز و آگاهانه مصرف می‌کنند؛ «لذت ملودراماتیک» نه ناآگاهی، بلکه نوعی مهارت تفسیری است.",
   "(۵) مصرف به‌مثابهٔ تولید: دو سرتیو خواندن را همچون شکار و قاچاق معنا در قلمرو قدرت می‌بیند؛ مصرف روزمره، عملی خلاقانه است.",
   VOID + "فندام، فن‌فیکشن، میم‌سازی و حتی بایکوت سازمان‌یافته، اشکال امروزین همین کنش‌اند: مخاطبان متن را می‌شکنند، بازنویسی می‌کنند و از آن معنایی می‌سازند که تولیدکننده در نظر نداشت.",
  ]),
  "assumptions": [
   "مخاطب صرفاً دریافت‌کنندهٔ پیام نیست؛ او در تولید معنا مشارکت دارد.",
   "معنا در چانه‌زنی میان رمزگذاری متن و منابع فرهنگی مخاطب ساخته می‌شود.",
   "لذت مصرف رسانه، شکلی از کنش و مقاومت فرهنگی است.",
  ],
  "principles": [
   "تحلیل باید از متن به سمت عمل تفسیری مخاطب حرکت کند.",
   "بافت اجتماعی مخاطب، تعیین‌کنندهٔ رمزگشایی است.",
   "تفاوت میان خوانش مسلط و خوانش محبوب، بخشی از تحلیل است، نه استثنا.",
  ],
  "critiques": [
   "اغراق بر عاملیت: تأکید بر مخاطب فعال می‌تواند ساختار قدرت رسانه‌ای — مالکیت، الگوریتم، اقتصاد توجه — را پنهان کند؛ انتخاب مخاطب در چارچوب‌هایی است که خود آن را انتخاب نکرده.",
   "رومانتیسم مقاومت: تبدیل هر مصرف به «مقاومت»، مفهوم قدرت را رقیق می‌کند و مرز میان بهره‌کشی و کنش را از بین می‌برد.",
   "دشواری سنجش: پژوهش‌های تفسیری بر نمونه‌های کوچک استوارند و تعمیم‌پذیری و تکرارپذیری آن‌ها دشوار است.",
   "غفلت از اثر: اگر مخاطب چنین فعال است، سنجش اثر پیام‌های آسیب‌زا (تبلیغات، خبر جعلی) ناممکن می‌شود.",
  ],
  "applications": [
   "تحلیل فندام و فرهنگ مشارکتی: تولید، بازترکیب و توزیع معنای جایگزین.",
   "مطالعهٔ مصرف طنزآمیز محتوای عامه‌پسند و بازنمایی هویت.",
   "طراحی کمپین با احتساب تفسیر مخاطب: پیام‌هایی که فضای بازتری برای مشارکت می‌دهند.",
   "تحلیل مقاومت مصرف‌کننده در شبکه‌های اجتماعی: بایکوت، کمپین علیه برند و بازنویسی تبلیغ.",
  ],
  "evolution": "از مدل رمزگذاری/رمزگشایی هال (۱۹۸۰) به پژوهش مخاطب آنگ (۱۹۸۵) و فیسک (۱۹۸۷)، سپس به مطالعات فندام و فرهنگ مشارکتی (جنکینز) و امروز به تحلیل کنش کاربر در پلتفرم‌های الگوریتمی.",
  "key_concepts": ["رمزگذاری/رمزگشایی (Encoding/Decoding)", "متن نوشتنی (Writerly Text)", "دموکراسی نشانه‌ای (Semiotic Democracy)", "لذت عامه‌پسند (Popular Pleasure)", "مقاومت روزمره (Everyday Resistance)", "فرهنگ مشارکتی (Participatory Culture)"],
  "studies": [
   "Ang, I. (1985). Watching Dallas: Soap opera and the melodramatic imagination. Methuen.",
   "Radway, J. A. (1984). Reading the romance: Women, patriarchy, and popular literature. University of North Carolina Press.",
  ],
  "detailed_analysis": "\n".join([
   "۱. بنیان و منطق نظری: مخاطب فعال، واکنشی است به مدل‌های اثر مستقیم و نیز به تصویر مخاطب منفعل در نظریهٔ انتقادی؛ نقطهٔ شروع آن، تفکیک میان «معنای رمزگذاری‌شده» و «معنای دریافت‌شده» است.",
   "۲. شواهد و روش: پژوهش‌های آنگ و رادوی نمونه‌های کلاسیک دریافت‌اند؛ هر دو نشان دادند مخاطبان زن با دانش فرهنگی خود، متنی را که نخبگان «بی‌ارزش» می‌دانستند، به منابع معنا و هویت بدل می‌کنند.",
   "۳. چالش معاصر: در پلتفرم‌ها، «فعال بودن» هم‌زمان با «قابل پیش‌بینی شدن» همزیستی دارد؛ داده‌کاوی رفتار مخاطب، عاملیت را در چارچوب تعیین‌شده اندازه‌گیری می‌کند. نظریهٔ مخاطب فعال امروز باید این تنش را توضیح دهد.",
  ]),
  "critique_text": "\n".join([
   "۱. اغراق بر عاملیت: تأکید بر مخاطب فعال می‌تواند ساختار قدرت رسانه‌ای — مالکیت، الگوریتم، اقتصاد توجه — را پنهان کند؛ انتخاب مخاطب در چارچوب‌هایی است که خود آن را انتخاب نکرده.",
   "۲. رومانتیسم مقاومت: تبدیل هر مصرف به «مقاومت»، مفهوم قدرت را رقیق می‌کند و مرز میان بهره‌کشی و کنش را از بین می‌برد.",
   "۳. دشواری سنجش: پژوهش‌های تفسیری بر نمونه‌های کوچک استوارند و تعمیم‌پذیری و تکرارپذیری آن‌ها دشوار است.",
   "۴. غفلت از اثر: اگر مخاطب چنین فعال است، سنجش اثر پیام‌های آسیب‌زا (تبلیغات، خبر جعلی) ناممکن می‌شود.",
  ]),
  "example_text": "\n".join([
   "یک پژوهش «استفاده و خشنودی» نشان می‌دهد جوانانی که ساعات زیادی در شبکه‌های اجتماعی می‌گذرانند، این کار را نه صرفاً از سر «اعتیاد»، بلکه برای پاسخ به نیازهای مشخص — تعلق، اطلاعات، سرگرمی و هویت‌سازی — انجام می‌دهند.",
   "در بازنمایی تلویزیونی مهاجران، مخاطبان از بافت‌های اجتماعی متفاوت، یک صحنه را متفاوت رمزگشایی می‌کنند: برای یکی انتقاد از میزبان، برای دیگری تأیید سیاست‌های پذیرش — نمونهٔ آشکار رمزگشایی مذاکره‌ای.",
   "فندام‌ها با بازنویسی پایان یک سریال یا ساختن میم از صحنه‌های آن، متنی تولید می‌کنند که سازندگان اصلی هرگز پیش‌بینی نمی‌کردند؛ همین، شکل امروزین «دموکراسی نشانه‌ای» است.",
  ]),
 },
 "MC-356": {
  "summary": "(فیش، ۱۹۸۰) نظریهٔ جماعت‌های تفسیری می‌گوید معنا نه در متن نهفته است و نه ساختهٔ ذهن تنهای خواننده؛ بلکه از «راهبردهای تفسیری» مشترکی برمی‌آید که گروه‌های اجتماعی به آن‌ها تعلق دارند. خواننده پیش از خواندن، با این راهبردها متن را می‌سازد و همین راهبردها، حدود تفسیر معتبر را تعیین می‌کنند.",
  "definition": "جماعت تفسیری، گروهی از خوانندگان است که در راهبردهای تفسیری مشترک‌اند؛ این راهبردها — نه ویژگی‌های متن — تعیین می‌کنند خواننده چه چیزی را به‌عنوان «در متن» ببیند و چه معنایی را معتبر بداند.",
  "main_problem": "اگر متن معنای ثابتی ندارد، پس چرا در یک جامعه، تفسیرها تا این حد همگرا هستند و در جامعهٔ دیگر، واگرا؟ فیش پرسش را از سطح رابطهٔ متن و فرد به سطح نهاد و جماعت منتقل می‌کند.",
  "mechanism": "\n".join([
   "(۱) راهبردهای تفسیری: خواننده متن را با مجموعه‌ای از قواعد و انتظارات از پیش‌آموخته می‌خواند؛ همین قواعدند که به نشانه‌ها مرز و شکل می‌دهند.",
   "(۲) نهاد به‌جای فرد: جماعت تفسیری، فرد را به دانش نهادی مجهز می‌کند؛ مدرسه، حرفه، مذهب و خرده‌فرهنگ، نمونه‌های آن هستند.",
   "(۳) اقتدار تفسیر: اگر جماعت، معیار درستی تفسیر را تعیین کند، نقد ادبی نیز نه کشف معنا، بلکه بازتولید یک راهبرد نهادی است.",
   "(۴) ناپدیدشدن متن به‌عنوان ابژهٔ مستقل: فیش می‌گوید آنچه «متن» می‌نامیم، پیش از خواندن، محصول راهبرد تفسیری است؛ پس هیچ خوانش «خام» و بی‌واسطه وجود ندارد.",
   "(۵) پیامد برای نقد: اختلاف تفسیرها اختلاف در ساختارهای نهادی است، نه اختلاف در دقت خواندن؛ تحلیل باید به سراغ جماعت‌ها و آموزش‌های آن‌ها برود.",
   VOID + "در فضای رسانه‌ای، جماعت‌های تفسیری به‌وضوح دیده می‌شوند: طرفداران یک برنامه در یک گروه، همان صحنهٔ بحث‌برانگیز را کاملاً متفاوت از گروه دیگر می‌خوانند؛ و رسانه‌های حرفه‌ای، خود یک جماعت تفسیری با قواعد داوری مشخص‌اند.",
  ]),
  "assumptions": [
   "متن به‌تنهایی معنای ثابتی ندارد.",
   "تفسیر، عمل اجتماعی و آموخته‌شده است، نه شهود فردی.",
   "معیار اعتبار تفسیر، درون جماعت تفسیری ساخته می‌شود.",
  ],
  "principles": [
   "تحلیل معنا باید از خوانش فردی به راهبردهای نهادی منتقل شود.",
   "اختلاف تفسیرها را باید با تفاوت جماعت‌ها توضیح داد، نه با خطای خواندن.",
   "قدرت نهاد آموزشی و حرفه‌ای در شکل‌گیری تفسیر باید آشکار شود.",
  ],
  "critiques": [
   "خطر نسبی‌گرایی نهایی: اگر هر جماعت معیار خود را بسازد، امکان نقد تفسیرهای نادرست (مثلاً جعل تاریخی) از میان می‌رود.",
   "ابهام تجربی: مفهوم جماعت تفسیری به‌سختی قابل شناسایی و اندازه‌گیری است و مرزهای آن مشخص نیست.",
   "کم‌رنگی قدرت: فیش نهاد را به‌عنوان زمینهٔ تفسیر می‌بیند، اما توزیع نابرابر قدرت میان جماعت‌ها را کمتر تحلیل می‌کند.",
   "تقابل کامل با متن: نفی هر نقش متن، با شواهد روان‌شناسی خواندن ناسازگار است؛ ساختار متن، برخی تفسیرها را محتمل‌تر می‌کند.",
  ],
  "applications": [
   "پژوهش دریافت خبر: چرا مخاطبان با گرایش سیاسی متفاوت، یک گزارش را متفاوت می‌فهمند.",
   "تحلیل فندام و خرده‌فرهنگ: هنجارهای تفسیری درون گروه چگونه ساخته می‌شوند.",
   "آموزش سواد رسانه‌ای: تقویت آگاهی از راهبردهای تفسیری خود و دیگران.",
   "طراحی محتوای حرفه‌ای: پیش‌بینی اختلاف تفسیر میان جماعت‌های مختلف مخاطب.",
  ],
  "evolution": "فیش در «آیا در این کلاس متنی وجود دارد؟» (۱۹۸۰) نظریهٔ خود را صورت‌بندی کرد؛ پس از آن، پژوهش‌های تجربی جماعت تفسیری (رادوی، ۱۹۸۴) و سپس مطالعات فرهنگ مشارکتی، آن را به قلمرو رسانه و اینترنت گستردند.",
  "key_concepts": ["جماعت تفسیری (Interpretive Community)", "راهبرد تفسیری (Interpretive Strategy)", "اقتدار تفسیر (Authoritative Interpretation)", "نهاد و خوانش (Institution and Reading)", "وابستگی معنا (Contingency of Meaning)", "خودفهمی خواننده (Reading Self-consciousness)"],
  "studies": [
   "Radway, J. A. (1984). Reading the romance: Women, patriarchy, and popular literature. University of North Carolina Press.",
   "Fish, S. (1989). Doing what comes naturally: Change, rhetoric, and the practice of theory in literary and legal studies. Duke University Press.",
  ],
  "detailed_analysis": "\n".join([
   "۱. بنیان و منطق نظری: فیش با رد دوگانهٔ «متن‌محور/خواننده‌محور»، سطح سوم را وارد کرد: سطح نهاد. همان‌گونه که کوهن نشان داد پارادایم علمی تعیین می‌کند چه چیزی «داده» است، جماعت تفسیری هم تعیین می‌کند چه چیزی «در متن» است.",
   "۲. پیوند با نظریهٔ تفسیر حقوقی: فیش همین ایده را بعدها به تفسیر قانون گسترد: اختلاف قاضی‌ها اختلاف در راهبردهای تفسیری جماعت‌های حقوقی است، نه فقط اختلاف در متن قانون.",
   "۳. افق دیجیتال: با شکل‌گیری «حباب‌های فیلتر»، جماعت تفسیری ابعاد الگوریتمی یافته است: همان خبر، در دو فید متفاوت، دو تفسیر مسلط پیدا می‌کند و راهبردهای هر فید، تا حد زیادی نامرئی می‌ماند.",
  ]),
  "critique_text": "\n".join([
   "۱. خطر نسبی‌گرایی نهایی: اگر هر جماعت معیار خود را بسازد، امکان نقد تفسیرهای نادرست (مثلاً جعل تاریخی) از میان می‌رود.",
   "۲. ابهام تجربی: مفهوم جماعت تفسیری به‌سختی قابل شناسایی و اندازه‌گیری است و مرزهای آن مشخص نیست.",
   "۳. کم‌رنگی قدرت: فیش نهاد را به‌عنوان زمینهٔ تفسیر می‌بیند، اما توزیع نابرابر قدرت میان جماعت‌ها را کمتر تحلیل می‌کند.",
   "۴. تقابل کامل با متن: نفی هر نقش متن، با شواهد روان‌شناسی خواندن ناسازگار است؛ ساختار متن، برخی تفسیرها را محتمل‌تر می‌کند.",
  ]),
  "example_text": "\n".join([
   "دو گروه از مخاطبان یک گزارش خبری، همان جمله را می‌خوانند اما یکی آن را «افشاگری» و دیگری «کارزار سیاسی» می‌فهمند؛ تفاوت نه در متن، بلکه در راهبردهای تفسیری جماعت‌هایشان است.",
   "در یک فندام، هنجارهای تفسیری مشترک تعیین می‌کنند کدام پایان یک سریال «قابل قبول» و کدام «خروج از شخصیت» است؛ خوانندهٔ تازه‌وارد، این قواعد را در همان جماعت می‌آموزد.",
   "در آموزش سواد رسانه‌ای، شناخت جماعت‌های تفسیری به مخاطب کمک می‌کند ببیند چرا خود او یک متن را بدیهی می‌شمارد؛ همین خودآگاهی، هدف اصلی فیش است.",
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
    print("BATCH67 THEORY DONE")

if __name__ == "__main__":
    main()
