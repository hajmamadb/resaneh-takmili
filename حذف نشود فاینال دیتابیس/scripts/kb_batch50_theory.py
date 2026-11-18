# -*- coding: utf-8 -*-
"""Batch 50 (THEORY): MC-206 Populist Communication Style (Jagers & Walgrave 2007), MC-207
Market-Oriented Party (Lees-Marshment 2001), MC-208 Personalization of Politics (Van Aelst,
Shehata & Stanyer 2012), MC-209 Motivated Reasoning (Kunda 1990). Anchors verified 2026-11-16."""
import pymysql, json

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch50-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch50_theory.json"

S = {
 "MC-206": [
   dict(kind="JOURNAL_ARTICLE", title_en="Populism as Political Communication Style: An Empirical Study of Political Parties' Discourse in Belgium",
        title_fa="پوپولیسم به‌عنوان سبک ارتباط سیاسی: پژوهشی تجربی بر گفتمان احزاب در بلژیک",
        authors="Jagers, J., & Walgrave, S.", year=2007,
        publisher="European Journal of Political Research, 46(3), 319-345",
        doi="10.1111/j.1475-6765.2006.00690.x",
        url="https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1475-6765.2006.00690.x",
        language="en", isbn=None,
        citation="Jagers, J., & Walgrave, S. (2007). Populism as political communication style: An empirical study of political parties' discourse in Belgium. European Journal of Political Research, 46(3), 319-345.",
        locator="pp. 319-345", locator_type="page_range", supports="definition / four-dimension measure", verified=True),
   dict(kind="BOOK", title_en="The Global Rise of Populism: Performance, Political Style, and Representation",
        title_fa="خیزش جهانی پوپولیسم: اجرا، سبک سیاسی و بازنمایی",
        authors="Moffitt, B.", year=2016, publisher="Stanford, CA: Stanford University Press", doi=None, url=None,
        language="en", isbn=None,
        citation="Moffitt, B. (2016). The global rise of populism: Performance, political style, and representation. Stanford University Press.",
        locator="whole work", locator_type="work", supports="evolution / performative style", verified=False),
 ],
 "MC-207": [
   dict(kind="BOOK", title_en="Political Marketing and British Political Parties: The Party's Just Begun",
        title_fa="بازاریابی سیاسی و احزاب سیاسی بریتانیا", authors="Lees-Marshment, J.", year=2001,
        publisher="Manchester: Manchester University Press", doi=None,
        url="https://archive.org/details/politicalmarketi0000lees_e4h6", language="en", isbn=None,
        citation="Lees-Marshment, J. (2001). Political marketing and British political parties: The party's just begun. Manchester University Press.",
        locator="whole work", locator_type="work", supports="definition / POP-SOP-MOP typology", verified=True),
   dict(kind="JOURNAL_ARTICLE", title_en="The Marriage of Politics and Marketing",
        title_fa="پیوند سیاست و بازاریابی", authors="Lees-Marshment, J.", year=2001,
        publisher="Political Studies, 49(4), 692-713", doi=None, url=None, language="en", isbn=None,
        citation="Lees-Marshment, J. (2001). The marriage of politics and marketing. Political Studies, 49(4), 692-713.",
        locator="pp. 692-713", locator_type="page_range", supports="mechanism / marketing mix in politics", verified=False),
 ],
 "MC-208": [
   dict(kind="JOURNAL_ARTICLE", title_en="The Personalization of Mediated Political Communication: A Review of Concepts, Operationalizations and Key Findings",
        title_fa="شخصی‌سازی ارتباط سیاسی رسانه‌ای‌شده: مروری بر مفاهیم، عملیاتی‌سازی‌ها و یافته‌های کلیدی",
        authors="Van Aelst, P., Shehata, A., & Stanyer, J.", year=2012,
        publisher="Journalism, 13(2), 203-220", doi="10.1177/1464884911427802",
        url="https://journals.sagepub.com/doi/10.1177/1464884911427802", language="en", isbn=None,
        citation="Van Aelst, P., Shehata, A., & Stanyer, J. (2012). The personalization of mediated political communication: A review of concepts, operationalizations and key findings. Journalism, 13(2), 203-220.",
        locator="pp. 203-220", locator_type="page_range", supports="definition / three-dimension typology", verified=True),
   dict(kind="BOOK_CHAPTER", title_en="The Personalization of Politics",
        title_fa="شخصی‌سازی سیاست", authors="McAllister, I.", year=2007,
        publisher="In R. J. Dalton & H.-D. Klingemann (Eds.), The Oxford Handbook of Political Behavior (pp. 571-588). Oxford University Press",
        doi=None, url=None, language="en", isbn=None,
        citation="McAllister, I. (2007). The personalization of politics. In R. J. Dalton & H.-D. Klingemann (Eds.), The Oxford handbook of political behavior (pp. 571-588). Oxford University Press.",
        locator="pp. 571-588", locator_type="page_range", supports="evolution / institutional presidentialization", verified=False),
 ],
 "MC-209": [
   dict(kind="JOURNAL_ARTICLE", title_en="The Case for Motivated Reasoning",
        title_fa="استدلال برای استدلال انگیزشی", authors="Kunda, Z.", year=1990,
        publisher="Psychological Bulletin, 108(3), 480-498", doi="10.1037/0033-2909.108.3.480",
        url="https://psycnet.apa.org/record/1991-06436-001", language="en", isbn=None,
        citation="Kunda, Z. (1990). The case for motivated reasoning. Psychological Bulletin, 108(3), 480-498.",
        locator="pp. 480-498", locator_type="page_range", supports="definition / directional vs accuracy goals", verified=True),
   dict(kind="BOOK", title_en="The Rationalizing Voter", title_fa="رأی‌دهندهٔ عقلانی‌ساز",
        authors="Lodge, M., & Taber, C. S.", year=2013, publisher="Cambridge: Cambridge University Press", doi=None,
        url=None, language="en", isbn=None,
        citation="Lodge, M., & Taber, C. S. (2013). The rationalizing voter. Cambridge University Press.",
        locator="whole work", locator_type="work", supports="mechanism / hot cognition", verified=False),
 ],
}

ENRICH = {
 "MC-206": {
   "summary": "«سبک ارتباطی پوپولیستی» (Populist Communication Style) پوپولیسم را نه صرفاً یک ایدئولوژی، بلکه الگویی از گفتمان و ارتباط می‌بیند که در آن بازیگر سیاسی به «مردم» ارجاع می‌دهد، «نخبگان» را نکوهش می‌کند و بر حق حاکمیت مستقیم مردم تأکید می‌ورزد. یان یاگرز و استفان والگراو در مطالعهٔ احزاب بلژیک (۲۰۰۷، EJPR) پوپولیسم را به‌عنوان سبکی قابل اندازه‌گیری در گفتمان احزاب عملیاتی کردند (Jagers & Walgrave, 2007).",
   "main_problem": "آیا پوپولیسم ویژگی انحصاری احزاب رادیکال راست است یا سبکی ارتباطی که در درجات مختلف در گفتمان طیف گسترده‌ای از احزاب یافت می‌شود، و چگونه می‌توان آن را به‌گونه‌ای تجربی و مقایسه‌پذیر سنجید؟",
   "mechanism": "یاگرز و والگراو پوپولیسم را در چهار بُعد عملیاتی می‌کنند: (۱) «ارجاع به مردم» (reference to the people) به‌عنوان منبع مشروعیت و یکپارچگی؛ (۲) «ارجاع به نخبگان» (reference to the elite) به‌عنوان گروهی که منافع مردم را خیانت می‌کند؛ (۳) «تأکید بر حاکمیت مستقیم مردم» و ارادهٔ عمومی در برابر واسطه‌گری نهادی؛ (۴) «ضدیت با نظام/نخبگان» (anti-establishment) که در قالب نکوهش رسانه، روشنفکران و احزاب سنتی بیان می‌شود (Jagers & Walgrave, 2007). آن‌ها با تحلیل برنامه‌های انتخاباتی احزاب بلژیک نشان دادند که پوپولیسم نه یک وضعیت دوگانه بلکه «درجه‌ای» است که در سراسر طیف حزبی نوسان می‌کند؛ احزاب می‌توانند در دوره‌ای پوپولیست‌تر و در دوره‌ای کمتر باشند. موفیت (Moffitt, 2016) این خط را به «سبک سیاسی اجرایی» (political style) گسترد: پوپولیسم شامل «رفتار بد»، نمایش‌گری، ساده‌سازی و عامیانه‌سازی (bad manners) است که در رسانه‌های تلویزیونی و پلتفرمی به‌خوبی بازتاب می‌یابد. در بستر رسانه، منطق تجاری و سرگرم‌محور خبر — کشش به درام، تضاد و شخصیت جنجالی — سبک پوپولیستی را پاداش می‌دهد و به بازتولید آن کمک می‌کند؛ از این رو پوپولیسم را باید در تعامل گفتمان سیاسی و منطق رسانه‌ای فهمید، نه فقط در ایدئولوژی احزاب.",
   "assumptions": [
     "پوپولیسم سبکی ارتباطی است که در درجه‌های مختلف در گفتمان احزاب یافت می‌شود.",
     "گفتمان پوپولیستی حول تقابل «مردم اصیل» و «نخبگان فاسد» سازمان می‌یابد.",
     "سبک پوپولیستی با منطق رسانه‌ای درام‌محور هم‌افزا است."
   ],
   "principles": [
     "چهار بُعد: ارجاع به مردم، نخبگان، حاکمیت مستقیم و ضدنظام.",
     "درجه‌مندی: پوپولیسم پیوستار است، نه برچسب دوگانه.",
     "اجرا و سبک: نمایش‌گری و ساده‌سازی بخشی از سبک است."
   ],
   "critiques": [
     "مناقشهٔ سبک/ایدئولوژی: تقلیل پوپولیسم به سبک، بُعد ایدئولوژیک و پیوند آن با ناسیونالیسم را کم‌رنگ می‌کند.",
     "سنجش گفتمانی: تحلیل برنامه‌ها ممکن است سبک اجرایی و لحن رسانه‌ای را از دست بدهد.",
     "هم‌پوشانی: نشانگرهای سبک پوپولیستی با عوام‌گرایی و ضدیت عمومی با سیاست خلط می‌شود."
   ],
   "applications": [
     "تحلیل گفتمان احزاب و رهبران در پوشش خبری و شبکه‌های اجتماعی.",
     "پژوهش دربارهٔ پیوند سبک پوپولیستی و منطق رسانه‌ای.",
     "مقایسهٔ بین‌کشوری درجات پوپولیسم در گفتمان حزبی."
   ],
   "evolution": "یاگرز و والگراو (2007) سنجهٔ چهاربُعدی را معرفی کردند و موفیت (2016) پوپولیسم را به سبک اجرایی و بازنمایی گسترد. در دههٔ ۲۰۲۰، پژوهش سبک پوپولیستی به شبکه‌های اجتماعی و رسانه‌های پلتفرمی گسترش یافت.",
   "key_concepts": ["سبک ارتباطی پوپولیستی (populist communication style)", "مردم/نخبگان (people/elite)", "ضدنظام‌گرایی (anti-establishment)", "سبک سیاسی (political style)", "منطق رسانه‌ای (media logic)"],
   "studies": ["Jagers, J., & Walgrave, S. (2007). Populism as political communication style. EJPR, 46(3), 319-345.", "Moffitt, B. (2016). The Global Rise of Populism. Stanford University Press."],
 },
 "MC-207": {
   "summary": "«حزب بازارگرا» (Market-Oriented Party) الگویی از حزب سیاسی است که بازاریابی را نه فقط برای تبلیغ، بلکه برای «طراحی محصول» — یعنی سیاست و برنامه — به کار می‌گیرد و بر پایهٔ تقاضای رأی‌دهنده، پیشنهاد سیاسی خود را می‌سازد. جنیفر لیز-مارشمنت این مفهوم را در «Political Marketing and British Political Parties» (۲۰۰۱، Manchester University Press) در برابر احزاب «محصول‌گرا» و «فروش‌گرا» صورت‌بندی کرد (Lees-Marshment, 2001).",
   "main_problem": "وقتی احزاب سیاسی تکنیک‌های بازاریابی را وارد می‌کنند، این تکنیک‌ها فقط ابزار تبلیغ باقی می‌مانند یا محتوای سیاست و رابطهٔ حزب با رأی‌دهنده را دگرگون می‌کنند، و این دگرگونی چه پیامدهایی برای دموکراسی دارد؟",
   "mechanism": "لیز-مارشمنت سه نوع جهت‌گیری حزبی را از هم جدا می‌کند: «حزب محصول‌گرا» (Product-Oriented Party) که سیاست را بر پایهٔ باورهای درونی می‌سازد و سپس می‌کوشد آن را بفروشد؛ «حزب فروش‌گرا» (Sales-Oriented Party) که محصول را حفظ می‌کند اما با ابزارهای تبلیغاتی و اقناعی پیشرفته آن را به بازار عرضه می‌کند؛ و «حزب بازارگرا» (Market-Oriented Party) که نخست پژوهش بازار و افکارسنجی انجام می‌دهد، سپس «محصول سیاسی» (سیاست و برنامه) را بر پایهٔ تقاضای رأی‌دهنده طراحی می‌کند، بعد ارتباط و کمپین را می‌سازد و در نهایت به «تحویل» (delivery) — یعنی اجرای وعده‌ها در حکومت — متعهد می‌شود (Lees-Marshment, 2001). در این الگو، بازاریابی از حوزهٔ ترویج به حوزهٔ طراحی محصول و راهبرد کشیده می‌شود و پژوهش افکار عمومی به ابزاری برای شکل‌دادن به سیاست بدل می‌گردد. لیز-مارشمنت در مقالهٔ «The Marriage of Politics and Marketing» (Lees-Marshment, 2001b) نشان می‌دهد که آمیختهٔ بازاریابی سیاسی — محصول، قیمت (هزینهٔ رأی)، مکان (کانال ارتباط) و ترویج — در سیاست بازتعریف می‌شود و «تحویل» بخشی از بازاریابی است، نه پس از آن. در بستر رسانه، حزب بازارگرا رابطهٔ تنگاتنگی با نظرسنجی، تمرکز گروهی و ارتباطات مدیریت‌شده دارد و به همین دلیل در معرض اتهام «سیاست نظرسنجی‌محور» و فرسایش موضع‌گیری ایدئولوژیک قرار می‌گیرد.",
   "assumptions": [
     "رأی‌دهنده را می‌توان همچون مصرف‌کننده در بازار سیاسی مدل‌سازی کرد.",
     "بازاریابی می‌تواند طراحی سیاست را informed کند، نه فقط تبلیغ آن.",
     "تحویل وعده‌ها بخشی از فرایند بازاریابی سیاسی است."
   ],
   "principles": [
     "سه جهت‌گیری: محصول‌گرا، فروش‌گرا و بازارگرا.",
     "طراحی محصول: پژوهش بازار پیش از تدوین سیاست.",
     "تحویل: اجرای وعده بخشی از بازاریابی است."
   ],
   "critiques": [
     "فرسایش دموکراتیک: تبعیت از نظرسنجی می‌تواند رهبری سیاسی و موضع‌گیری اصولی را تضعیف کند.",
     "توهم تقاضا: «تقاضای رأی‌دهنده» خود تا حدی محصول ارتباطات و رسانه ساخته می‌شود.",
     "محدودیت تجربی: الگوی بازارگرا در عمل با مقاومت درون‌حزبی و محدودیت‌های ساختاری روبه‌روست."
   ],
   "applications": [
     "تحلیل کمپین‌های انتخاباتی و راهبرد ارتباطی احزاب.",
     "پژوهش دربارهٔ پیوند نظرسنجی، سیاست‌گذاری و مشاورهٔ رسانه‌ای.",
     "نقد بازاریابی سیاسی و پیامدهای آن برای نمایندگی."
   ],
   "evolution": "لیز-مارشمنت (2001) الگوی سه‌گانه را تثبیت کرد و پژوهش‌های بعدی، نسخه‌های ترکیبی و نقدهای دموکراتیک آن را گستردند. در دههٔ ۲۰۱۰-۲۰۲۰، تحلیل داده و هدف‌گیری ریز مخاطب، منطق بازارگرایی را به کمپین دیجیتال کشاند.",
   "key_concepts": ["حزب بازارگرا (market-oriented party)", "محصول سیاسی (political product)", "آمیختهٔ بازاریابی سیاسی (political marketing mix)", "تحویل (delivery)", "سیاست نظرسنجی‌محور (poll-driven politics)"],
   "studies": ["Lees-Marshment, J. (2001). Political Marketing and British Political Parties. Manchester University Press.", "Lees-Marshment, J. (2001). The marriage of politics and marketing. Political Studies, 49(4), 692-713."],
 },
 "MC-208": {
   "summary": "«شخصی‌سازی سیاست» (Personalization of Politics) به گرایش فزایندهٔ پوشش و کنش سیاسی به سوی شخصیت‌ها، ویژگی‌های فردی و زندگی خصوصی سیاستمداران در برابر احزاب، نهادها و مسائل اشاره دارد. پتر فان آلست، آدام شحاتا و جیمز استنیر در مرور نظام‌مند خود (۲۰۱۲، Journalism) مفهوم را به سه بُعد تفکیک کردند (Van Aelst, Shehata, & Stanyer, 2012).",
   "main_problem": "آیا سیاست واقعاً شخصی‌تر شده است، شخصی‌سازی در کدام بُعد و با چه شواهدی رخ می‌دهد، و این چرخه چه پیامدهایی برای کیفیت نمایندگی و آگاهی سیاسی شهروندان دارد؟",
   "mechanism": "فان آلست و همکاران سه بُعد متمایز را از هم جدا می‌کنند: «ریاستی‌شدن» (presidentialization) — تمرکز نهادی و رهبری‌محور بر نخست‌وزیر/رئیس‌جمهور؛ «فردی‌شدن» (individualization) — برجسته‌شدن نامزد و شخصیت سیاسی در برابر حزب و برنامه؛ و «خصوصی‌شدن» (privatization) — ورود زندگی خصوصی، خانواده و ویژگی‌های شخصی به پوشش سیاسی (Van Aelst et al., 2012). سازوکار اصلی، منطق رسانه‌ای است: ارزش‌های خبری درام، انسان‌محوری و علاقهٔ انسانی، پوشش را به سمت شخصیت و داستان فردی می‌کشد؛ در همان حال، خود سیاستمداران با اجرای هویت شخصی، رسانه‌های اجتماعی و روایت زندگی خصوصی، این چرخه را تقویت می‌کنند. مرور شواهد نشان می‌دهد که «خصوصی‌شدن» در برخی زمینه‌ها آشکارتر است، اما «فردی‌شدن» شواهد یکدستی ندارد و در بسیاری از کشورها پوشش حزبی و موضوعی پایدار مانده است (Van Aelst et al., 2012). مک‌آلیستر (McAllister, 2007) بُعد نهادی را با مفهوم «ریاستی‌شدن» نظام‌های پارلمانی پیوند می‌دهد. در بستر رسانه، شخصی‌سازی هم فرصت است — آشنایی و پاسخ‌گویی فردی — و هم خطر: کاهش محتوای سیاستی، تمرکز بر جذابیت و رسوایی، و تضعیف پیوند رأی‌دهنده با برنامه‌های حزبی.",
   "assumptions": [
     "شخصی‌سازی پدیده‌ای چندبُعدی است و نباید به یک شاخص فروکاسته شود.",
     "منطق رسانه‌ای و اجرای فردی سیاستمداران، شخصی‌سازی را تقویت می‌کنند.",
     "شدت و الگوی شخصی‌سازی بسته به زمینهٔ ملی متفاوت است."
   ],
   "principles": [
     "سه بُعد: ریاستی‌شدن، فردی‌شدن و خصوصی‌شدن.",
     "منطق رسانه‌ای: انسان‌محوری و درام، پوشش شخصی را تقویت می‌کند.",
     "شواهد ناهمگون: فردی‌شدن یکدست نیست و بسته به زمینه نوسان دارد."
   ],
   "critiques": [
     "کشش مفهومی: کاربرد موسع شخصی‌سازی، مرز آن با سلبریتی‌سازی و رسوایی‌محوری را مخدوش می‌کند.",
     "ناسازگاری سنجش: شاخص‌های مختلف، نتایج متفاوت و گاه متناقض تولید می‌کنند.",
     "تفکیک سطوح: شخصی‌سازی در پوشش رسانه‌ای با شخصی‌سازی در رفتار سیاسی و نهادی یکی گرفته می‌شود."
   ],
   "applications": [
     "تحلیل پوشش انتخاباتی و سهم شخصیت در برابر برنامه.",
     "پژوهش دربارهٔ رسانه‌های اجتماعی و روایت شخصی سیاستمداران.",
     "ارزیابی پیامدهای شخصی‌سازی بر آگاهی و مشارکت سیاسی."
   ],
   "evolution": "پژوهش شخصی‌سازی از دههٔ ۱۹۹۰ با مطالعات پوشش انتخاباتی رشد کرد؛ فان آلست و همکاران (2012) چارچوب سه‌بُعدی و مرور شواهد را ارائه کردند. در دههٔ ۲۰۲۰، رسانه‌های اجتماعی شخصی‌سازی را به سطح تعامل روزمره و برندسازی فردی کشاندند.",
   "key_concepts": ["شخصی‌سازی (personalization)", "ریاستی‌شدن (presidentialization)", "فردی‌شدن (individualization)", "خصوصی‌شدن (privatization)", "منطق رسانه‌ای (media logic)"],
   "studies": ["Van Aelst, P., Shehata, A., & Stanyer, J. (2012). The personalization of mediated political communication. Journalism, 13(2), 203-220.", "McAllister, I. (2007). The personalization of politics. In Oxford Handbook of Political Behavior."],
 },
 "MC-209": {
   "summary": "«استدلال انگیزشی» (Motivated Reasoning) به فرایندی اشاره دارد که در آن انگیزه‌ها و اهداف فرد، پردازش اطلاعات و استدلال او را سوگیری می‌کنند تا به نتیجهٔ دلخواه برسد. زیوا کوندا در مقالهٔ «The Case for Motivated Reasoning» (۱۹۹۰، Psychological Bulletin) نشان داد که انگیزه از رهگذر فرایندهای شناختی سوگیرانه — دسترسی، ساخت و ارزیابی باورها — بر استدلال اثر می‌گذارد (Kunda, 1990).",
   "main_problem": "اگر افراد به‌ظاهر منطقی فکر می‌کنند، چرا اغلب به نتیجه‌ای می‌رسند که با باورها و هویتشان هم‌خوان است، و چه سازوکارهای شناختی این «عقلانیت‌سازی» را ممکن می‌کند؟",
   "mechanism": "کوندا دو نوع هدف را از هم جدا می‌کند: «اهداف دقت» (accuracy goals) که فرد را به سمت پاسخ درست می‌کشاند، و «اهداف جهت‌دار» (directional goals) که فرد را به سمت نتیجهٔ دلخواه سوق می‌دهد (Kunda, 1990). در استدلال جهت‌دار، فرد اطلاعات و باورهای هم‌خوان را آسان‌تر به‌یاد می‌آورد، شواهد را با معیارهای سوگیرانه ارزیابی می‌کند و به «توهم عینیت» (illusion of objectivity) دچار می‌شود: باور دارد که بی‌طرفانه استدلال می‌کند. لاج و تِیبر (Lodge & Taber, 2013) این سازوکار را در سیاست با مفهوم «شناخت داغ» (hot cognition) گستردند: مفاهیم سیاسی با بار عاطفی ذخیره می‌شوند و ارزیابی خودکار و سریع «چگونه دربارهٔ آن احساس می‌کنم» جای استدلال دقیق را می‌گیرد؛ استدلال پس از داوری عاطفی، به «عقلانی‌سازی» (rationalization) بدل می‌شود. سازوکارهای کلیدی شامل جست‌وجوی اطلاعات سوگیرانه، «شک‌گرایی انگیزشی» (motivated skepticism) نسبت به شواهد ناهم‌خوان، و پافشاری بر باور پیشین است. در بستر رسانه، این یافته توضیح می‌دهد چرا تصحیح خبر (fact-checking) اغلب با مقاومت روبه‌رو می‌شود و چرا مخاطبان رسانه‌های حزبی اطلاعات هم‌خوان با هویت خود را آسان‌تر می‌پذیرند؛ استدلال انگیزشی، حلقهٔ پیوند میان هویت، رسانه و مقاومت در برابر اطلاعات نادرست است.",
   "assumptions": [
     "انگیزه از طریق فرایندهای شناختی سوگیرانه بر استدلال اثر می‌گذارد.",
     "اهداف جهت‌دار با اهداف دقت در تعامل‌اند و رفتار استدلالی را شکل می‌دهند.",
     "افراد به‌رغم سوگیری، خود را عینیت‌گرا می‌پندارند."
   ],
   "principles": [
     "دو نوع هدف: دقت و جهت‌دار.",
     "جست‌وجوی سوگیرانه: اطلاعات هم‌خوان آسان‌تر یافت می‌شود.",
     "توهم عینیت: فرد سوگیری خود را نمی‌بیند."
   ],
   "critiques": [
     "کم‌رنگی دقت: در شرایطی که انگیزهٔ دقت بالا باشد، افراد می‌توانند سوگیری را تعدیل کنند.",
     "سنجش دشوار: تفکیک استدلال انگیزشی از استدلال عادی به‌سختی ممکن است.",
     "کاربرد موسع: مفهوم در توضیح همهٔ مقاومت‌ها در برابر اطلاعات بیش از حد به‌کار می‌رود."
   ],
   "applications": [
     "تحلیل مقاومت در برابر تصحیح خبر و اطلاعات نادرست.",
     "پژوهش دربارهٔ رسانه‌های حزبی و انتخاب‌گری اطلاعات.",
     "طراحی مداخلات ارتباطی برای کاهش قطب‌شدگی باور."
   ],
   "evolution": "کوندا (1990) چارچوب شناختی-انگیزشی را بنیان نهاد و لاج و تِیبر (2013) آن را با شناخت داغ و مدل «رأی‌دهندهٔ عقلانی‌ساز» به سیاست گستردند. در دههٔ ۲۰۲۰، استدلال انگیزشی به محور پژوهش دربارهٔ اطلاعات نادرست و قطب‌شدگی بدل شد.",
   "key_concepts": ["استدلال انگیزشی (motivated reasoning)", "اهداف جهت‌دار (directional goals)", "شناخت داغ (hot cognition)", "توهم عینیت (illusion of objectivity)", "شک‌گرایی انگیزشی (motivated skepticism)"],
   "studies": ["Kunda, Z. (1990). The case for motivated reasoning. Psychological Bulletin, 108(3), 480-498.", "Lodge, M., & Taber, C. S. (2013). The Rationalizing Voter. Cambridge University Press."],
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
    codes = ["MC-206", "MC-207", "MC-208", "MC-209"]
    cur.execute("SELECT id, code, properties FROM kb_entities WHERE code IN (%s)" % ",".join(["%s"]*len(codes)), codes)
    rows = {code:(eid, json.loads(pr)) for (eid, code, pr) in cur.fetchall()}
    with open(BACKUP, "w", encoding="utf-8") as f:
        json.dump([{"code": cd, "props": rows[cd][1]} for cd in codes if cd in rows], f, ensure_ascii=False, indent=1)
    print("backup ->", len(rows), "rows")

    for code in codes:
        eid, p = rows[code]
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
                     "documented sourcing + rubric score", STAMP, NOW))
        cur.execute("INSERT INTO kb_audit_log (entity_code, action, detail, source) VALUES (%s,%s,%s,%s)",
                    (code, "DOC_ENRICH", json.dumps({"quality_score": score, "words": words, "sources": n_sources, "verified": n_verified, "breakdown": detail}, ensure_ascii=False), STAMP))
        print(f"{code}: score={score} words={words} sources={n_sources} verified={n_verified} relations={n_relations} | {detail}")
    c.commit()
    c.close()
    print("BATCH50 THEORY DONE")

if __name__ == "__main__":
    main()
