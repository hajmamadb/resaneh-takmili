# -*- coding: utf-8 -*-
"""Batch 62 (THEORY): MC-315 Magic Bullet / Hypodermic Needle (Lasswell 1927),
MC-321 Social Judgment Theory (Sherif & Hovland 1961), MC-324 Self-Perception Theory
(Bem 1967), MC-327 Narrative Transportation (Green & Brock 2000). Anchors verified 2026-11-16.
Rewrites the mismatched generic boilerplate critique/example on MC-315 and MC-324."""
import pymysql, json

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch62-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch62_theory.json"

S = {
 "MC-315": [
   dict(kind="BOOK", title_en="Propaganda Technique in the World War",
        title_fa="تکنیک پروپاگاندا در جنگ جهانی",
        authors="Lasswell, H. D.", year=1927, publisher="New York: Alfred A. Knopf", doi=None,
        url="https://www.mediastudies.press/pub/emet-lasswell-theory",
        language="en", isbn=None,
        citation="Lasswell, H. D. (1927). Propaganda technique in the world war. Alfred A. Knopf.",
        locator="whole work", locator_type="work", supports="origin / propaganda as direct shaping of mass opinion", verified=True),
   dict(kind="BOOK", title_en="The Invasion from Mars: A Study in the Psychology of Panic",
        title_fa="تهاجم از مریخ: پژوهشی در روان‌شناسی هراس جمعی",
        authors="Cantril, H.", year=1940, publisher="Princeton, NJ: Princeton University Press", doi=None, url=None,
        language="en", isbn=None,
        citation="Cantril, H. (1940). The invasion from Mars: A study in the psychology of panic. Princeton University Press.",
        locator="whole work", locator_type="work", supports="critique / differential rather than uniform response", verified=False),
 ],
 "MC-321": [
   dict(kind="BOOK", title_en="Social Judgment: Assimilation and Contrast Effects in Communication and Attitude Change",
        title_fa="قضاوت اجتماعی: اثرهای هم‌سازی و تضاد در ارتباط و تغییر نگرش",
        authors="Sherif, M., & Hovland, C. I.", year=1961, publisher="New Haven: Yale University Press", doi=None,
        url="https://archive.org/details/socialjudgmentas0000sher",
        language="en", isbn=None,
        citation="Sherif, M., & Hovland, C. I. (1961). Social judgment: Assimilation and contrast effects in communication and attitude change. Yale University Press.",
        locator="whole work", locator_type="work", supports="definition / latitudes / assimilation and contrast", verified=True),
   dict(kind="BOOK", title_en="Attitude and Attitude Change: The Social Judgment-Involvement Approach",
        title_fa="نگرش و تغییر نگرش: رویکرد قضاوت اجتماعی-درگیری",
        authors="Sherif, C. W., Sherif, M., & Nebergall, R. E.", year=1965, publisher="Philadelphia: W. B. Saunders", doi=None, url=None,
        language="en", isbn=None,
        citation="Sherif, C. W., Sherif, M., & Nebergall, R. E. (1965). Attitude and attitude change: The social judgment-involvement approach. W. B. Saunders.",
        locator="whole work", locator_type="work", supports="evolution / ego-involvement", verified=False),
 ],
 "MC-324": [
   dict(kind="JOURNAL_ARTICLE", title_en="Self-Perception: An Alternative Interpretation of Cognitive Dissonance Phenomena",
        title_fa="خودادراکی: تفسیری جایگزین برای پدیده‌های ناهماهنگی شناختی",
        authors="Bem, D. J.", year=1967,
        publisher="Psychological Review, 74(3), 183-200", doi="10.1037/h0024835",
        url="https://pubmed.ncbi.nlm.nih.gov/5342882/",
        language="en", isbn=None,
        citation="Bem, D. J. (1967). Self-perception: An alternative interpretation of cognitive dissonance phenomena. Psychological Review, 74(3), 183-200. https://doi.org/10.1037/h0024835",
        locator="pp. 183-200", locator_type="page_range", supports="definition / inference from own behavior", verified=True),
   dict(kind="BOOK_CHAPTER", title_en="Self-Perception Theory",
        title_fa="نظریهٔ خودادراکی",
        authors="Bem, D. J.", year=1972,
        publisher="In L. Berkowitz (Ed.), Advances in Experimental Social Psychology (Vol. 6, pp. 1-62). New York: Academic Press",
        doi=None, url="https://www.sciencedirect.com/science/chapter/bookseries/pii/S0065260108600246", language="en", isbn=None,
        citation="Bem, D. J. (1972). Self-perception theory. In L. Berkowitz (Ed.), Advances in experimental social psychology (Vol. 6, pp. 1-62). Academic Press.",
        locator="pp. 1-62", locator_type="page_range", supports="evolution / boundary conditions", verified=False),
 ],
 "MC-327": [
   dict(kind="JOURNAL_ARTICLE", title_en="The Role of Transportation in the Persuasiveness of Public Narratives",
        title_fa="نقش غرق‌شدگی در اقناع‌گری روایت‌های عمومی",
        authors="Green, M. C., & Brock, T. C.", year=2000,
        publisher="Journal of Personality and Social Psychology, 79(5), 701-721", doi=None,
        url="https://pubmed.ncbi.nlm.nih.gov/11079236/",
        language="en", isbn=None,
        citation="Green, M. C., & Brock, T. C. (2000). The role of transportation in the persuasiveness of public narratives. Journal of Personality and Social Psychology, 79(5), 701-721.",
        locator="pp. 701-721", locator_type="page_range", supports="definition / transportation scale / belief change", verified=True),
   dict(kind="JOURNAL_ARTICLE", title_en="The Extended Transportation-Imagery Model: A Meta-Analysis of the Antecedents and Consequences of Consumers' Narrative Transportation",
        title_fa="الگوی گستردهٔ غرق‌شدگی-تصویرسازی: فراتحلیل پیشایندها و پیامدهای غرق‌شدگی روایی مصرف‌کننده",
        authors="van Laer, T., de Ruyter, K., Visconti, L. M., & Wetzels, M.", year=2014,
        publisher="Journal of Consumer Research, 40(5), 797-817", doi=None, url=None, language="en", isbn=None,
        citation="van Laer, T., de Ruyter, K., Visconti, L. M., & Wetzels, M. (2014). The extended transportation-imagery model. Journal of Consumer Research, 40(5), 797-817.",
        locator="pp. 797-817", locator_type="page_range", supports="evolution / meta-analytic generalization", verified=False),
 ],
}

ENRICH = {
 "MC-315": {
   "summary": "«گلولهٔ جادویی» یا «سوزن تزریقی» (Magic Bullet / Hypodermic Needle) نخستین تصور رایج دربارهٔ اثر رسانه‌های جمعی است: رسانه پیام را مستقیم، یکسان و نیرومند به ذهن مخاطب منفعل تزریق می‌کند و واکنش همگن می‌سازد. این تصور را معمولاً به اثر هارولد لاسول، «Propaganda Technique in the World War» (۱۹۲۷)، بازمی‌گردانند، هرچند خود اصطلاح «گلولهٔ جادویی» بعدها ساخته شد (Lasswell, 1927).",
   "definition": "الگوی گلولهٔ جادویی/سوزن تزریقی مدعی است پیام رسانه‌ای بر مخاطب توده‌ای اثری مستقیم، فوری، یکسان و قوی دارد، بی‌آنکه میانجی‌های اجتماعی، تفسیر فردی یا مقاومت شناختی در نظر گرفته شود (Lasswell, 1927).",
   "main_problem": "چرا در دهه‌های آغازین قرن بیستم، تبلیغات جنگ و پروپاگاندا چنان قدرتمند تصور می‌شد که گمان می‌رفت بتواند افکار میلیون‌ها نفر را به‌طور یکسان شکل دهد، و این تصور بر چه فرضیاتی دربارهٔ مخاطب و جامعه استوار بود؟",
   "mechanism": "این الگو بر چهار فرض استوار است. (۱) جامعهٔ توده‌ای و مخاطب اتمیزه: افراد از پیوندهای محلی و گروه‌های میانجی جدا شده و به اتم‌هایی منفرد بدل شده‌اند؛ در چنین جامعه‌ای، هر فرد جداگانه در معرض پیام قرار می‌گیرد. (۲) منطق محرک-پاسخ: پیام، محرکی یکسان است که پاسخ روانی مشابه تولید می‌کند؛ تمایز فردی و زمینهٔ فرهنگی، متغیرهای مزاحم به شمار نمی‌آیند. (۳) رسانه به‌عنوان مجرای تزریق: رسانهٔ جمعی کانالی است که محتوا را بی‌واسطه به روان مخاطب می‌رساند و «اثر» آن قابل اندازه‌گیری و پیش‌بینی است. (۴) کارکرد اقناعی یک‌سویه: فرستنده فعال و گیرندهٔ منفعل است؛ بازخورد، مقاومت و تفسیر رقیب در مدل جایی ندارد. زمینهٔ تاریخی این الگو، تجربهٔ پروپاگاندای جنگ جهانی اول و رشد تبلیغات تجاری بود؛ مشاهدهٔ آنکه دولت‌ها توانستند افکار عمومی را بسیج کنند، به این نتیجه انجامید که رسانه «قدرت مطلق» دارد. در بستر رسانه، این الگو امروز بیشتر پرسش تحلیلی است تا توصیف واقعیت: هر بار که گفته می‌شود «رسانه ذهن مردم را شست‌وشو می‌دهد» یا «یک ویدئو همه را قانع کرد»، در واقع فرض گلولهٔ جادویی بازتولید می‌شود. شواهد تجربی — از واکنش متفاوت شنوندگان «تهاجم از مریخ» در ۱۹۳۸ تا پژوهش‌های دوپله‌ای کاتز و لازارسفلد — نشان دادند که مخاطب در شبکهٔ روابط اجتماعی و تفسیر شخصی عمل می‌کند و اثر یکسان رخ نمی‌دهد.",
   "assumptions": [
     "مخاطب، توده‌ای اتمیزه و منفعل است.",
     "پیام رسانه‌ای بر همهٔ افراد اثر یکسان و مستقیم دارد.",
     "میانجی‌های اجتماعی و تفسیر فردی در فرایند اثر، نقشی تعیین‌کننده ندارند."
   ],
   "principles": [
     "رسانه، محرکی نیرومند با پاسخ همگن است.",
     "اثر رسانه مستقیم و بی‌واسطه است.",
     "مخاطب فاقد مقاومت شناختی و تفسیر فعال است."
   ],
   "critiques": [
     "شواهد تجربی، فرض واکنش یکسان را رد کرد: کانتریل (۱۹۴۰) نشان داد شنوندگان برنامهٔ رادیویی «تهاجم از مریخ» واکنش‌های بسیار متفاوتی داشتند و تفاوت آن‌ها با اعتماد به رسانه، مذهب و شبکهٔ اجتماعی توضیح‌پذیر بود.",
     "پژوهش جریان دوپله‌ای نشان داد پیام از رهبران عقیده و روابط میان‌فردی می‌گذرد؛ بنابراین اثر مستقیم و یکسان، از نظر تجربی نادر است.",
     "بخش مهمی از این الگو، بازسازیِ بعدیِ تاریخ‌نگاری ارتباطات است؛ خود لاسول در تحلیل ۱۹۲۷ خود مخاطب را کاملاً بی‌تمایز نمی‌دید و اصطلاح «گلولهٔ جادویی» بعدها برساخته شد."
   ],
   "applications": [
     "نقد فرض‌های ضمنی در گفتمان عمومی دربارهٔ «شست‌وشوی ذهن» رسانه‌ای.",
     "آموزش سواد رسانه‌ای با نشان دادن ناکارآمدی مدل تزریقی.",
     "تحلیل تاریخی پروپاگاندا و تبلیغات جنگ.",
     "مقایسهٔ الگوهای اثر رسانه در پژوهش تجربی."
   ],
   "evolution": "الگو در دههٔ ۱۹۲۰ و ۱۹۳۰ غالب بود؛ از دههٔ ۱۹۴۰ با پژوهش‌های کانتریل، لازارسفلد و مرتن جای خود را به مدل‌های محدود و دوپله‌ای داد و از دههٔ ۱۹۷۰ به‌عنوان «نمونهٔ منفی» در آموزش نظریه‌های ارتباطات بازتولید شد.",
   "key_concepts": ["مخاطب توده‌ای (mass audience)", "محرک-پاسخ (stimulus-response)", "پیام یکسان و اثر همگن", "پروپاگاندا (propaganda)", "مخاطب منفعل (passive audience)", "مدل تزریقی (hypodermic model)"],
   "studies": ["Lasswell, H. D. (1927). Propaganda technique in the world war. Alfred A. Knopf.", "Cantril, H. (1940). The invasion from Mars: A study in the psychology of panic. Princeton University Press."],
   "detailed_analysis": "۱. بنیان و منطق نظری\nالگوی گلولهٔ جادویی از تلاقی روان‌شناسی محرک-پاسخ، جامعه‌شناسی توده و تجربهٔ پروپاگاندای جنگی زاده شد. منطق آن ساده بود: اگر پیام به همه یکسان برسد و همه در وضعیت روانی مشابه باشند، اثر نیز یکسان خواهد بود.\n\n۲. چرا ناکام ماند\nپژوهش تجربی نشان داد که «همه» هرگز یکسان نیستند. اعتماد به منبع، شبکهٔ اجتماعی، پیش‌داوری و تفسیر فردی، اثر پیام را تعدیل می‌کنند. به بیان دقیق، الگو به‌جای توصیف مخاطب، توصیف ترس نخبگان از مخاطب بود.\n\n۳. پیوند رسانه‌ای و درس روش‌شناختی\nاهمیت امروزی الگو نه در درست بودن، بلکه در هشدار روش‌شناختی آن است: هر تحلیل رسانه‌ای که مخاطب را بی‌تمایز و منفعل فرض کند، همان خطای ۱۹۲۷ را تکرار می‌کند. بازتولید این الگو در گفتمان «الگوریتم‌ها همه را کنترل می‌کنند» نشان می‌دهد که درس آن هنوز کامل آموخته نشده است.",
   "critique_text": "\n".join([
     "۱. رد تجربی: فرض واکنش یکسان با شواهد سازگار نیست؛ کانتریل (۱۹۴۰) در مطالعهٔ «تهاجم از مریخ» واکنش‌های بسیار متفاوت و وابسته به اعتماد، مذهب و شبکهٔ اجتماعی یافت.",
     "۲. غفلت از میانجی‌ها: مدل جریان دوپله‌ای نشان داد که پیام از رهبران عقیده و روابط میان‌فردی می‌گذرد و اثر مستقیم، استثناست نه قاعده.",
     "۳. برساختهٔ تاریخ‌نگاری: خود لاسول مخاطب را کاملاً بی‌تمایز نمی‌دید و اصطلاح «گلولهٔ جادویی» بعدها ساخته شد؛ الگو بیشتر آینهٔ ترس نخبگان است تا توصیف مخاطب واقعی."]),
   "example_text": "در پخش رادیویی «جنگ دنیاها» در ۱۹۳۸، گروهی از شنوندگان هراسان شدند و گروهی دیگر آن را نمایشی داستانی دانستند؛ همین تفاوت واکنش در یک پیام مشترک، فرض اثر یکسان و تزریق مستقیم را نقض می‌کند و نشان می‌دهد اعتماد به رسانه و زمینهٔ اجتماعی، اثر پیام را تعیین می‌کنند.",
 },
 "MC-321": {
   "summary": "«نظریهٔ قضاوت اجتماعی» (Social Judgment Theory) می‌گوید مخاطب پیام را در مقایسه با موضع پیشین خود (لنگر) ارزیابی می‌کند و پیام را در یکی از سه حوزهٔ پذیرش، بی‌تعهدی یا رد جای می‌دهد. مظفر شریف و کارل هوفلند در «Social Judgment» (۱۹۶۱، Yale University Press) این چارچوب را با مفاهیم هم‌سازی و تضاد صورت‌بندی کردند (Sherif & Hovland, 1961).",
   "definition": "قضاوت اجتماعی نظریه‌ای است که تغییر نگرش را تابع فاصلهٔ پیام از لنگر نگرشی فرد و درگیری ذهنی (ego-involvement) او می‌داند؛ پیام نزدیک به لنگر، هم‌سازی و پیام دور از آن، تضاد و اثر بومرنگ تولید می‌کند (Sherif & Hovland, 1961).",
   "main_problem": "چرا پیام یکسان بر افراد مختلف اثرهای متفاوت و حتی معکوس می‌گذارد؛ و چه عاملی تعیین می‌کند که مخاطب پیام را بپذیرد، نادیده بگیرد یا در جهت مخالف آن سخت‌تر شود؟",
   "mechanism": "نظریه بر چهار سازوکار استوار است. (۱) لنگر نگرشی: هر فرد موضعی مرجع دارد که قضاوت پیام‌های جدید نسبت به آن سنجیده می‌شود؛ لنگر، نقطهٔ صفرِ درونی فرد است. (۲) سه حوزه: پیام‌ها در حوزهٔ پذیرش (قابل قبول)، حوزهٔ بی‌تعهدی (بی‌تفاوت) یا حوزهٔ رد (غیرقابل قبول) قرار می‌گیرند؛ مرزهای این حوزه‌ها را میزان درگیری فرد تعیین می‌کند. (۳) هم‌سازی و تضاد: پیام نزدیک به لنگر، نزدیک‌تر از واقع ادراک می‌شود (هم‌سازی) و پیام دور، دورتر از واقع (تضاد)؛ به همین دلیل ارزیابی مخاطب همیشه دقیق نیست. (۴) اثر بومرنگ: اگر پیام در حوزهٔ رد بیفتد، ممکن است موضع فرد را از لنگر دورتر کند، نه نزدیک‌تر. پیامد کاربردی این است که اقناع مؤثر، پیامِ «دور» نیست، بلکه پیامی است که در لبهٔ حوزهٔ پذیرش یا بی‌تعهدی قرار گیرد و به‌تدریج لنگر را جابه‌جا کند. در بستر رسانه، این نظریه توضیح می‌دهد چرا کمپین‌های سلامت یا اقناع سیاسی که با لحن تند و موضع حداکثری طراحی می‌شوند، گاه مقاومت را تشدید می‌کنند: آن‌ها وارد حوزهٔ رد مخاطب هدف می‌شوند. برعکس، پیام‌های «پل‌زن» که موضعی نزدیک به میانهٔ حوزهٔ بی‌تعهدی دارند، شانس تغییر تدریجی بیشتری دارند.",
   "assumptions": [
     "فرد موضع مرجعی دارد که پیام‌ها نسبت به آن سنجیده می‌شوند.",
     "مرزهای حوزهٔ پذیرش و رد را میزان درگیری فرد با موضوع تعیین می‌کند.",
     "فاصلهٔ ادراک‌شده از لنگر، جهت و اندازهٔ تغییر نگرش را تعیین می‌کند."
   ],
   "principles": [
     "قضاوت پیام، نسبی و وابسته به لنگر است.",
     "درگیری بالا، حوزهٔ پذیرش را باریک و حوزهٔ رد را گسترده می‌کند.",
     "پیام فراتر از حوزهٔ پذیرش، اثر بومرنگ می‌سازد."
   ],
   "critiques": [
     "عملیاتی‌سازی: ساخت مقیاس نگرش با چند لنگر و تعیین مرزهای حوزه‌ها روش‌شناختی دشوار است و برخی پژوهش‌ها سه‌گانهٔ طول‌ها را بازتولید نکردند.",
     "محدودهٔ کاربرد: نظریه در بافت گروه‌های کوچک و مسائل مشخص شکل گرفت و تعمیم آن به ارتباطات توده‌ای بحث‌برانگیز است.",
     "پایداری طول‌ها: روشن نیست اندازهٔ حوزه‌ها را چه چیزی تعیین می‌کند — شخصیت، ساختار اجتماعی یا خود پیام."
   ],
   "applications": [
     "طراحی پیام کمپین سلامت و سیاست‌گذاری عمومی.",
     "تحلیل اثر بومرنگ در ارتباطات سیاسی و بحث‌های شبکه‌های اجتماعی.",
     "آموزش مذاکره و میانجی‌گری با تمرکز بر حوزهٔ پذیرش طرف مقابل.",
     "پژوهش دربارهٔ قطب‌بندی و مقاومت در برابر اطلاعات اصلاحی."
   ],
   "evolution": "شریف و هوفلند (۱۹۶۱) چارچوب را تثبیت کردند و شریف، شریف و نبرگال (۱۹۶۵) مفهوم درگیری را بسط دادند؛ در پژوهش معاصر، نظریه برای تحلیل اثر بومرنگ در محیط‌های قطبی و اطلاعات نادرست به‌کار می‌رود.",
   "key_concepts": ["لنگر (anchor)", "حوزهٔ پذیرش (latitude of acceptance)", "حوزهٔ رد (latitude of rejection)", "حوزهٔ بی‌تعهدی (latitude of noncommitment)", "هم‌سازی و تضاد (assimilation/contrast)", "درگیری ذهنی (ego-involvement)", "اثر بومرنگ (boomerang effect)"],
   "studies": ["Sherif, M., & Hovland, C. I. (1961). Social judgment: Assimilation and contrast effects in communication and attitude change. Yale University Press.", "Sherif, C. W., Sherif, M., & Nebergall, R. E. (1965). Attitude and attitude change. W. B. Saunders."],
   "detailed_analysis": "۱. بنیان و منطق نظری\nشریف از روان‌شناسی گشتالت آمد و قضاوت را نسبی دید: فرد پیام را نه در خلأ، بلکه نسبت به چارچوب مرجع خود ارزیابی می‌کند. هوفلند این بینش را به پژوهش تجربی تغییر نگرش پیوند داد و نتیجه، نظریه‌ای شد که هم ادراک و هم انگیزه را در بر می‌گیرد.\n\n۲. چرا اثر بومرنگ مهم است\nاگر پیام دور از لنگر باشد، فرد نه‌تنها آن را نمی‌پذیرد، بلکه برای دفاع از موضع خود، لنگر را دورتر می‌برد. این سازوکار، تبیین روان‌شناختی مقاومت در برابر اقناع است و توضیح می‌دهد که شدت پیام، همیشه به نفع اقناع نیست.\n\n۳. پیوند رسانه‌ای و نقد\nدر محیط شبکه‌ای، حوزهٔ رد کاربران با درگیری بالا باریک می‌شود و پیام‌های اصلاحی اغلب در همان حوزهٔ رد می‌افتند. نقد اصلی، محدودیت روش‌شناختی است: اندازه‌گیری مرزهای حوزه‌ها دشوار است، اما سازوکار بومرنگ از پرتکرارترین یافته‌های تجربی ارتباطات باقی مانده است."
 },
 "MC-324": {
   "summary": "«نظریهٔ خودادراکی» (Self-Perception Theory) می‌گوید افراد همیشه به حالات درونی خود دسترسی مستقیم ندارند و نگرش‌ها و احساسات خود را، مانند یک ناظر بیرونی، از رفتار و شرایط آن استنباط می‌کنند. داریل بم در مقالهٔ ۱۹۶۷ خود در Psychological Review این نظریه را به‌عنوان تفسیری جایگزین برای پدیده‌های ناهماهنگی شناختی پیشنهاد کرد (Bem, 1967).",
   "definition": "خودادراکی، فرایندی است که در آن فرد از مشاهدهٔ رفتار خود و اوضاعی که رفتار در آن رخ داده، به نگرش، احساس یا انگیزهٔ خود پی می‌برد؛ به همین دلیل تغییر رفتار می‌تواند مقدم بر تغییر نگرش باشد (Bem, 1967).",
   "main_problem": "آیا نگرش، علت رفتار است یا خود رفتار، منبعی است که فرد نگرش خود را از آن استنباط می‌کند؛ و اگر دسترسی درونی محدود باشد، چگونه می‌توان تغییر نگرش را بدون توسل به انگیزهٔ کاهش تنش توضیح داد؟",
   "mechanism": "نظریه در پنج گام عمل می‌کند. (۱) دسترسی محدود به حالات درونی: فرد همیشه از نگرش و انگیزهٔ خود آگاه نیست؛ بسیاری از حالات درونی، مبهم، ضعیف یا چندپهلو هستند. (۲) استنباط از رفتار: فرد نشانه‌های بیرونی رفتار خود را، همان‌گونه که ناظر می‌بیند، می‌خواند و از آن به حالت درونی می‌رسد — «چون این کار را کردم، پس به آن علاقه دارم». (۳) نقش شرایط: اگر برای رفتار تبیین بیرونی روشنی وجود داشته باشد (پاداش، فشار)، فرد آن را به انگیزهٔ درونی نسبت نمی‌دهد؛ برعکس، رفتار بدون توجیه بیرونی، بیشتر به نگرش درونی نسبت داده می‌شود، همان‌طور که پاداش بیش‌ازحد، انگیزهٔ درونی را تضعیف می‌کند. (۴) بازتفسیر ناهماهنگی: بم نشان داد پدیده‌های «ناهماهنگی شناختی» را می‌توان بدون فرض انگیزهٔ کاهش تنش توضیح داد: فرد پس از انتخاب، رفتار خود را مشاهده و نگرشش را با آن هم‌ساز می‌کند. (۵) پیامد کاربردی: رفتار می‌تواند پیش از نگرش تغییر کند؛ «پای در در» و برچسب‌گذاری مثبت با همین منطق کار می‌کنند. در بستر رسانه، این نظریه توضیح می‌دهد چرا تعامل کوچک با محتوا — کلیک، اشتراک‌گذاری، پیوستن به گروه — می‌تواند نگرش را تغییر دهد: فرد از رفتار خود نتیجه می‌گیرد که به آن موضوع علاقه دارد و سپس نگرشش را با رفتارش هم‌ساز می‌کند.",
   "assumptions": [
     "دسترسی فرد به حالات درونی خود، محدود و نامطمئن است.",
     "رفتار و شرایط آن، منبع اطلاعاتی معتبری برای استنباط نگرش‌اند.",
     "تغییر رفتار می‌تواند مقدم بر و مستقل از تغییر نگرش رخ دهد."
   ],
   "principles": [
     "نگرش، گاه معلول رفتار است، نه علت آن.",
     "انگیزهٔ درونی از رفتار بدون توجیه بیرونی استنباط می‌شود.",
     "پاداش و فشار بیرونی، انتساب به انگیزهٔ درونی را کاهش می‌دهد."
   ],
   "critiques": [
     "پرسش اصلی این است که آیا خودادراکی جایگزین ناهماهنگی شناختی است یا مکمل آن؛ شواهد به نفع دو فرایند متفاوت با شرایط مرزی مختلف است، نه حذف یکی.",
     "شرایط مرزی محدودکننده است: خودادراکی بیشتر وقتی رخ می‌دهد که نشانه‌های درونی ضعیف یا مبهم باشند.",
     "بخش مهمی از شواهد کلاسیک از مطالعات آزمایشگاهی با گزارش خود ساخته شده است و تعمیم آن به رفتار رسانه‌ای واقعی نیازمند احتیاط است."
   ],
   "applications": [
     "طراحی تعامل کوچک برای تشویق مشارکت عمومی.",
     "تحلیل اثر «پای در در» و برچسب‌گذاری در کمپین‌های اجتماعی.",
     "پژوهش دربارهٔ رابطهٔ تعامل با محتوا و شکل‌گیری نگرش.",
     "آموزش و تغییر رفتار سازمانی از طریق عمل، نه فقط اقناع کلامی."
   ],
   "evolution": "بم (۱۹۶۷) نظریه را در برابر ناهماهنگی شناختی مطرح کرد و در ۱۹۷۲ چارچوب کامل‌تری ارائه داد؛ پژوهش‌های بعدی، شرایط مرزی و رابطهٔ آن با نظریهٔ ناهماهنگی را روشن‌تر کردند و ایدهٔ «تغییر رفتار مقدم بر تغییر نگرش» به ادبیات سیاست‌گذاری رفتاری راه یافت.",
   "key_concepts": ["خودادراکی (self-perception)", "استنباط از رفتار (inference from behavior)", "انتساب (attribution)", "ناهماهنگی شناختی (cognitive dissonance)", "انگیزهٔ درونی و بیرونی (intrinsic/extrinsic motivation)", "شرایط مرزی (boundary conditions)"],
   "studies": ["Bem, D. J. (1967). Self-perception: An alternative interpretation of cognitive dissonance phenomena. Psychological Review, 74(3), 183-200.", "Bem, D. J. (1972). Self-perception theory. In Advances in Experimental Social Psychology (Vol. 6, pp. 1-62). Academic Press."],
   "detailed_analysis": "۱. بنیان و منطق نظری\nبم از رفتارگرایی و نظریهٔ خود رادیکال‌تری ساخت: اگر فرد نمی‌تواند به درون خود نگاه کند، پس باید رفتار خود را، مثل رفتار دیگری، تفسیر کند. این پیش‌فرض، نگرش را از «حالت درونی» به «استنباط» تبدیل می‌کند.\n\n۲. پیامد نظری\nاگر نگرش استنباطی باشد، اقناع کلامی تنها راه نیست؛ تغییر موقعیت رفتاری نیز می‌تواند نگرش را دگرگون کند. همین ایده، بنیان سیاست‌های رفتاری و رویکرد «عمل مقدم بر باور» شد.\n\n۳. پیوند رسانه‌ای و نقد\nدر محیط رسانه‌ای، کاربر با کلیک و اشتراک، نشانه‌ای از هویت خود تولید می‌کند و از آن نتیجه می‌گیرد که «چنین کسی است». نقد اصلی، ادعای جایگزینی است: شواهد بیشتر با هم‌زیستی دو سازوکار سازگار است تا با حذف یکی؛ بنابراین نظریه را باید مکمل ناهماهنگی شناختی دانست.",
   "critique_text": "\n".join([
     "۱. ادعای جایگزینی: شواهد نشان می‌دهد خودادراکی و ناهماهنگی شناختی دو فرایند با شرایط مرزی متفاوت‌اند، نه یکی جانشین دیگری.",
     "۲. شرایط مرزی: خودادراکی بیشتر زمانی رخ می‌دهد که نشانه‌های درونی ضعیف یا مبهم باشند و در موارد با واکنش هیجانی روشن، کاربرد محدودی دارد.",
     "۳. اتکا به گزارش خود و آزمایشگاه: بخش مهمی از شواهد از مطالعات آزمایشگاهی با گزارش خود ساخته شده و تعمیم آن به رفتار رسانه‌ای واقعی نیازمند احتیاط است."]),
   "example_text": "کسی که چند بار در گفت‌وگوهای سیاسی شرکت کرده است، از رفتار خود نتیجه می‌گیرد که «شخصی سیاسی» است و نگرشش را با این هویت هم‌ساز می‌کند؛ همین منطق توضیح می‌دهد چرا دعوت به یک اقدام کوچک — امضای یک طومار یا پیوستن به یک گروه — می‌تواند مقدمهٔ درگیری بیشتر شود.",
 },
 "MC-327": {
   "summary": "«نظریهٔ غرق‌شدگی روایی» (Narrative Transportation) می‌گوید وقتی مخاطب عمیقاً در جهان یک روایت فرومی‌رود، توجه، تصویرسازی و هیجان او درگیر می‌شود و مقاومت شناختی‌اش کاهش می‌یابد؛ در نتیجه، باورها بیش از استدلال مستقیم تغییر می‌کنند. ملانی گرین و تیموتی بروک در «The Role of Transportation in the Persuasiveness of Public Narratives» (۲۰۰۰، JPSP) این سازوکار را تجربی آزمودند (Green & Brock, 2000).",
   "definition": "غرق‌شدگی، جذب کامل ذهنی در روایت است که سه مؤلفهٔ تصویرسازی ذهنی، درگیری هیجانی و توجه متمرکز را در بر می‌گیرد و مخاطب را از جهان واقعی به جهان داستان منتقل می‌کند (Green & Brock, 2000).",
   "main_problem": "چرا روایت‌ها، بیش از آمار و استدلال، باور و نگرش را تغییر می‌دهند؛ و چه سازوکار روانی‌ای توضیح می‌دهد که خواننده، حتی با آگاهی از داستانی بودن متن، تحت تأثیر آن قرار می‌گیرد؟",
   "mechanism": "نظریه بر پنج سازوکار بنا شده است. (۱) جذب کامل: توجه مخاطب به جهان داستان منتقل می‌شود و منابع شناختی او صرف پیگیری رویدادها، شخصیت‌ها و تصاویر می‌شود؛ فرد در حین غرق‌شدگی، «حضور» در داستان را تجربه می‌کند. (۲) مؤلفه‌های سه‌گانه: تصویرسازی ذهنی، درگیری هیجانی و توجه متمرکز، سه رکن غرق‌شدگی‌اند و با مقیاس چندگانه سنجیده می‌شوند. (۳) توقف نقد: در حالت غرق‌شدگی، شمارش استدلال‌ها، شک به منبع و «حاشیه‌نویسی انتقادی» کاهش می‌یابد؛ مخاطب به‌جای ارزیابی ادعا، رویداد را تجربه می‌کند. (۴) همسویی باور: پس از پایان داستان، باورهای مخاطب به سمت معنای داستان حرکت می‌کند و این اثر حتی زمانی که مخاطب می‌داند داستان واقعی نیست، پایدار می‌ماند. (۵) قدرت روایت: روایت، تجربهٔ زیستهٔ شخصیت را شبیه‌سازی می‌کند و از این راه، همدلی و درک موقعیت را ممکن می‌سازد. در بستر رسانه، این چارچوب توضیح می‌دهد چرا مستند روایی، پادکست داستانی و تبلیغات روایت‌محور بر آگهی آماری برتری دارند: آن‌ها مخاطب را وارد جهان داستان می‌کنند. همین سازوکار، در تبلیغات سلامت، کمپین‌های اجتماعی و حتی انتشار اطلاعات نادرست روایی نیز کار می‌کند و به همین دلیل، تحلیل انتقادی روایت‌های رسانه‌ای اهمیت دارد.",
   "assumptions": [
     "مخاطب در حالت غرق‌شدگی، به‌طور شناختی در جهان داستان حاضر است.",
     "کاهش نقد و ارزیابی استدلال‌ها، اثر اقناعی روایت را افزایش می‌دهد.",
     "اثر روایت بر باور، حتی با آگاهی از داستانی بودن آن پایدار می‌ماند."
   ],
   "principles": [
     "غرق‌شدگی، سازوکار اصلی اثر اقناعی روایت است.",
     "تصویرسازی، هیجان و توجه متمرکز، ارکان غرق‌شدگی‌اند.",
     "روایت، باور را از راه تجربهٔ شبیه‌سازی‌شده تغییر می‌دهد، نه از راه استدلال."
   ],
   "critiques": [
     "مسئلهٔ خودگزارش: غرق‌شدگی عمدتاً با پرسشنامه سنجیده می‌شود و احساس ذهنی فرورفتگی لزوماً با اثر شناختی واقعی یکی نیست.",
     "همپوشانی با شناسایی شخصیت: منتقدان می‌گویند غرق‌شدگی و شناسایی با شخصیت از نظر عملیاتی قابل تفکیک نیستند.",
     "تعمیم‌پذیری در عصر دیجیتال: مطالعات بنیادین روی داستان‌های چاپی کوتاه انجام شده و اثر مصرف تکه‌تکه و چندوظیفگی بر غرق‌شدگی روشن نیست."
   ],
   "applications": [
     "طراحی کمپین سلامت و ارتباطات تغییر رفتار با روایت شخصی.",
     "تحلیل اثر مستند روایی و پادکست داستانی.",
     "پژوهش دربارهٔ اقناع‌گری روایت‌های رسانه‌ای و اطلاعات نادرست.",
     "آموزش سواد رسانه‌ای با تمرکز بر تحلیل غرق‌شدگی روایی."
   ],
   "evolution": "گرین و بروک (۲۰۰۰) سازوکار و مقیاس را معرفی کردند؛ پژوهش‌های بعدی آن را به بازاریابی، سلامت و سیاست تعمیم دادند و فراتحلیل ون لار و همکاران (۲۰۱۴) پیشایندها و پیامدهای آن را نظام‌مند کرد.",
   "key_concepts": ["غرق‌شدگی (transportation)", "تصویرسازی ذهنی (imagery)", "درگیری هیجانی (affective engagement)", "توقف نقد (suspension of critical thought)", "همدلی روایی (narrative empathy)", "اقناع روایی (narrative persuasion)"],
   "studies": ["Green, M. C., & Brock, T. C. (2000). The role of transportation in the persuasiveness of public narratives. Journal of Personality and Social Psychology, 79(5), 701-721.", "van Laer, T., de Ruyter, K., Visconti, L. M., & Wetzels, M. (2014). The extended transportation-imagery model. Journal of Consumer Research, 40(5), 797-817."],
   "detailed_analysis": "۱. بنیان و منطق نظری\nگرین و بروک پرسیدند چرا روایت اثر می‌گذارد. پاسخ آنان، استعارهٔ «حمل شدن» بود: خواننده از جهان واقعی به جهان داستان منتقل می‌شود و در آنجا، تجربهٔ شخصیت را به‌جای استدلال دربارهٔ آن، از سر می‌گذراند.\n\n۲. نقد و تفاوت با اقناع استدلالی\nدر اقناع استدلالی، مخاطب استدلال‌ها را می‌سنجد و ممکن است رد کند. در غرق‌شدگی روایی، سنجش متوقف می‌شود، زیرا مخاطب در حال تجربه است، نه ارزیابی. همین ویژگی، روایت را از یک سو قدرتمند و از سوی دیگر، ابزار مستعد سوءاستفاده می‌سازد.\n\n۳. پیوند رسانه‌ای و هشدار\nاین نظریه هم فرصت و هم خطر رسانه را نشان می‌دهد: روایت می‌تواند همدلی و فهم را بالا ببرد، اما همین سازوکار می‌تواند روایت‌های نادرست را نیز باورپذیر کند. آموزش سواد رسانه‌ای باید مخاطب را با سازوکار غرق‌شدگی آشنا کند، نه با انکار قدرت روایت.",
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
    codes = ["MC-315", "MC-321", "MC-324", "MC-327"]
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
    print("BATCH62 THEORY DONE")

if __name__ == "__main__":
    main()
