# -*- coding: utf-8 -*-
"""Batch 49 (THEORY): MC-202 Horse-Race Coverage (Patterson 1980), MC-203 Negativity Bias in
Political News (Soroka, Fournier & Nir 2019), MC-204 Issue Ownership (Petrocik 1996),
MC-205 Affective Polarization (Iyengar, Sood & Lelkes 2012). Anchors verified 2026-11-16."""
import pymysql, json

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch49-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch49_theory.json"

S = {
 "MC-202": [
   dict(kind="BOOK", title_en="The Mass Media Election: How Americans Choose Their President",
        title_fa="انتخابات رسانه‌ای: آمریکایی‌ها چگونه رئیس‌جمهور خود را انتخاب می‌کنند",
        authors="Patterson, T. E.", year=1980, publisher="New York: Praeger", doi=None,
        url="https://books.google.com/books?id=YVzny_M3HJcC", language="en", isbn="9780030577284",
        citation="Patterson, T. E. (1980). The mass media election: How Americans choose their president. Praeger.",
        locator="whole work", locator_type="work", supports="definition / game vs governing schema", verified=True),
   dict(kind="JOURNAL_ARTICLE", title_en="Consumer Demand for Election News: The Horserace Sells",
        title_fa="تقاضای مصرف‌کننده برای خبر انتخابات: مسابقهٔ اسب‌دوانی می‌فروشد",
        authors="Iyengar, S., Norpoth, H., & Hahn, K. S.", year=2004,
        publisher="Journal of Communication, 54(1), 157-175", doi=None, url=None, language="en", isbn=None,
        citation="Iyengar, S., Norpoth, H., & Hahn, K. S. (2004). Consumer demand for election news: The horserace sells. Journal of Communication, 54(1), 157-175.",
        locator="pp. 157-175", locator_type="page_range", supports="critiques / audience demand", verified=False),
 ],
 "MC-203": [
   dict(kind="JOURNAL_ARTICLE", title_en="Cross-National Evidence of a Negativity Bias in Psychophysiological Reactions to News",
        title_fa="شواهد بین‌کشوری از سوگیری منفی در واکنش‌های روان‌فیزیولوژیک به خبر",
        authors="Soroka, S., Fournier, P., & Nir, L.", year=2019,
        publisher="Proceedings of the National Academy of Sciences, 116(38), 18888-18892",
        doi="10.1073/pnas.1908369116", url="https://www.pnas.org/doi/10.1073/pnas.1908369116",
        language="en", isbn=None,
        citation="Soroka, S., Fournier, P., & Nir, L. (2019). Cross-national evidence of a negativity bias in psychophysiological reactions to news. Proceedings of the National Academy of Sciences, 116(38), 18888-18892.",
        locator="pp. 18888-18892", locator_type="page_range", supports="definition / physiological evidence", verified=True),
   dict(kind="JOURNAL_ARTICLE", title_en="Two Explanations for Negativity Effects in Political Behavior",
        title_fa="دو تبیین برای اثرهای منفی‌گرایی در رفتار سیاسی",
        authors="Lau, R. R.", year=1985,
        publisher="American Journal of Political Science, 29(1), 119-138", doi=None, url=None, language="en", isbn=None,
        citation="Lau, R. R. (1985). Two explanations for negativity effects in political behavior. American Journal of Political Science, 29(1), 119-138.",
        locator="pp. 119-138", locator_type="page_range", supports="mechanism / cost-orientation", verified=False),
 ],
 "MC-204": [
   dict(kind="JOURNAL_ARTICLE", title_en="Issue Ownership in Presidential Elections, with a 1980 Case Study",
        title_fa="مالکیت موضوع در انتخابات ریاست‌جمهوری، با مطالعهٔ موردی ۱۹۸۰",
        authors="Petrocik, J. R.", year=1996,
        publisher="American Journal of Political Science, 40(3), 825-850", doi=None,
        url="https://www.jstor.org/stable/2111797", language="en", isbn=None,
        citation="Petrocik, J. R. (1996). Issue ownership in presidential elections, with a 1980 case study. American Journal of Political Science, 40(3), 825-850.",
        locator="pp. 825-850", locator_type="page_range", supports="definition / issue ownership theory", verified=True),
   dict(kind="BOOK", title_en="Explaining and Predicting Elections: Issue Effects and Party Strategies in Twenty-Three Democracies",
        title_fa="تبیین و پیش‌بینی انتخابات: اثرهای موضوع و راهبردهای حزبی در بیست‌وسه دموکراسی",
        authors="Budge, I., & Farlie, D. J.", year=1983, publisher="London: Allen & Unwin", doi=None, url=None,
        language="en", isbn=None,
        citation="Budge, I., & Farlie, D. J. (1983). Explaining and predicting elections. Allen & Unwin.",
        locator="whole work", locator_type="work", supports="evolution / salience theory precursor", verified=False),
 ],
 "MC-205": [
   dict(kind="JOURNAL_ARTICLE", title_en="Affect, Not Ideology: A Social Identity Perspective on Polarization",
        title_fa="عاطفه، نه ایدئولوژی: دیدگاهی هویتی-اجتماعی به قطبی‌شدن",
        authors="Iyengar, S., Sood, G., & Lelkes, Y.", year=2012,
        publisher="Public Opinion Quarterly, 76(3), 405-431", doi="10.1093/poq/nfs038",
        url="https://academic.oup.com/poq/article/76/3/405/1894274", language="en", isbn=None,
        citation="Iyengar, S., Sood, G., & Lelkes, Y. (2012). Affect, not ideology: A social identity perspective on polarization. Public Opinion Quarterly, 76(3), 405-431.",
        locator="pp. 405-431", locator_type="page_range", supports="definition / social identity mechanism", verified=True),
   dict(kind="BOOK", title_en="Uncivil Agreement: How Politics Became Our Identity",
        title_fa="توافق نانجیب: چگونه سیاست به هویت ما بدل شد",
        authors="Mason, L.", year=2018, publisher="Chicago: University of Chicago Press", doi=None, url=None,
        language="en", isbn=None,
        citation="Mason, L. (2018). Uncivil agreement: How politics became our identity. University of Chicago Press.",
        locator="whole work", locator_type="work", supports="evolution / social sorting", verified=False),
 ],
}

ENRICH = {
 "MC-202": {
   "summary": "«پوشش مسابقه‌ای انتخابات» (Horse-Race Coverage) به تمرکز خبری بر رقابت، نظرسنجی‌ها، شانس پیروزی و راهبردهای انتخاباتی نامزدها اشاره دارد، به‌جای تمرکز بر برنامه‌ها، سیاست‌ها و مسائل عمومی. توماس پترسون در «The Mass Media Election» (۱۹۸۰، Praeger) نشان داد خبر انتخاباتی آمریکا عمدتاً در قالب «بازی» و نه «حکومت‌داری» بازنمایی می‌شود (Patterson, 1980).",
   "main_problem": "وقتی رسانه انتخابات را همچون مسابقه‌ای ورزشی پوشش می‌دهد، چه اتفاقی برای یادگیری سیاسی شهروندان، ارزیابی برنامه‌های نامزدها و اعتماد عمومی به سیاست می‌افتد؟",
   "mechanism": "پترسون در مطالعهٔ پوشش کارزار انتخاباتی ۱۹۷۶ تفکیک مهمی میان دو «طرحواره» (schema) خبری برقرار می‌کند: «طرحوارهٔ بازی» (game schema) که نامزدها را بازیکنانی تاکتیک‌باز می‌بیند که هدفشان بردن است، و «طرحوارهٔ حکومت‌داری» (governing schema) که بر توانایی ادارهٔ کشور و سیاست‌ها متمرکز است (Patterson, 1980). سه سازوکار این چرخش را توضیح می‌دهند: نخست، معیار خبری «تازگی» و «رقابت» نظرسنجی‌ها و تغییر جایگاه‌ها را به آسانی به خبر بدل می‌کند؛ دوم، «پوشش راهبردی» (strategy coverage) نامزد را به‌عنوان عامل تاکتیکی و نه صاحب برنامه بازنمایی می‌کند؛ سوم، این چارچوب‌بندی محتوای مسائل را به حاشیه می‌راند. پیامدها در تحلیل پترسون سه‌گانه است: کاهش یادگیری شهروندان از مواضع نامزدها، تقویت بدبینی و بی‌اعتمادی به سیاست، و اهمیت یافتن تصویر و «شتاب» (momentum) به‌جای شایستگی. پترسون این منطق را در «Out of Order» (Patterson, 1993) به صورتی گسترده‌تر به تحلیل زوال «نظام رسانهٔ مسئول» گره زد. با این حال، پژوهش بعدی نشان داد که بخشی از این چرخش از تقاضای خود مخاطبان برمی‌آید و پوشش مسابقه‌ای برای بسیاری از بینندگان جذاب‌تر از پوشش موضوعی است (Iyengar et al., 2004)؛ از این رو پرسش اصلی صرفاً «سوگیری رسانه» نیست، بلکه تعامل عرضهٔ خبری و تقاضای مخاطب است که چرخهٔ مسابقه‌محوری را بازتولید می‌کند.",
   "assumptions": [
     "چارچوب‌بندی خبری انتخاب میان طرحوارهٔ بازی و حکومت‌داری است.",
     "پوشش مسابقه‌ای بر یادگیری و ارزیابی سیاسی شهروندان اثر می‌گذارد.",
     "منطق «تازگی» و «رقابت» در ارزش‌های خبری، بازی‌محوری را تقویت می‌کند."
   ],
   "principles": [
     "طرحوارهٔ بازی در برابر طرحوارهٔ حکومت‌داری.",
     "پوشش راهبردی: نامزد به‌عنوان تاکتیک‌باز نه صاحب برنامه.",
     "پیامدهای بدبینی و کاهش یادگیری موضوعی."
   ],
   "critiques": [
     "نقش تقاضای مخاطب: تمایل بینندگان به خبر مسابقه‌ای، تحلیل صرفاً عرضه‌محور را ناکافی می‌کند.",
     "اثرهای ناهمگون: میزان اثر پوشش بازی‌محور بر یادگیری و اعتماد، بسته به مخاطب و زمینه متفاوت است.",
     "تفکیک مطلق: مرز میان پوشش بازی و حکومت‌داری در عمل سیال است و بسیاری از گزارش‌ها هر دو را درهم می‌آمیزند."
   ],
   "applications": [
     "تحلیل کیفیت پوشش انتخاباتی و سنجش سهم پوشش موضوعی در برابر مسابقه‌ای.",
     "آموزش روزنامه‌نگاران برای متعادل‌کردن پوشش رقابت و برنامه‌ها.",
     "پژوهش دربارهٔ اثر چارچوب‌بندی خبری بر بدبینی سیاسی."
   ],
   "evolution": "پترسون (1980) مفهوم را تثبیت کرد و (1993) آن را به نقد نظام رسانهٔ سیاسی گسترد. در دههٔ ۲۰۰۰-۲۰۱۰، پژوهش تقاضای خبری (Iyengar et al., 2004) و تحلیل رسانه‌های دیجیتال، نقش مخاطب و الگوریتم‌ها را در تقویت مسابقه‌محوری برجسته کرد.",
   "key_concepts": ["پوشش مسابقه‌ای (horse-race coverage)", "طرحوارهٔ بازی (game schema)", "طرحوارهٔ حکومت‌داری (governing schema)", "پوشش راهبردی (strategy coverage)", "شتاب رسانه‌ای (media momentum)"],
   "studies": ["Patterson, T. E. (1980). The Mass Media Election. Praeger.", "Iyengar, S., Norpoth, H., & Hahn, K. S. (2004). The horserace sells. Journal of Communication, 54(1), 157-175."],
 },
 "MC-203": {
   "summary": "«سوگیری منفی در اخبار سیاسی» (Negativity Bias in Political News) به برتری نظام‌مند اطلاعات منفی بر مثبت در جلب توجه، پردازش و واکنش مخاطب اشاره دارد. استوارت سوروکا، پاتریک فورنیه و لیلاخ نیر در مطالعهٔ «Cross-National Evidence of a Negativity Bias» (۲۰۱۹، PNAS) نشان دادند واکنش‌های روان‌فیزیولوژیک افراد به خبر منفی شدیدتر از خبر مثبت است (Soroka, Fournier, & Nir, 2019).",
   "main_problem": "چرا اخبار منفی مخاطبان را بیشتر جذب می‌کند، این سوگیری تا چه حد ریشه در سازوکارهای شناختی و فیزیولوژیک دارد، و چگونه با منطق تولید خبر ترکیب می‌شود تا فضای خبری را به سمت منفی‌گرایی سوق دهد؟",
   "mechanism": "سوروکا و همکاران با اندازه‌گیری رسانایی پوست (skin conductance) — شاخص برانگیختگی فیزیولوژیک — نشان دادند که پاسخ افراد به کلیپ‌های خبری منفی به‌طور معنادار قوی‌تر از پاسخ به خبر مثبت است و این الگو در نمونه‌های چندکشوری تکرار می‌شود (Soroka et al., 2019). لائو (Lau, 1985) دو تبیین رقیب را بررسی می‌کند: تبیین «شناختی» مبتنی بر برجستگی اطلاعات منفی در شکل‌گیری برداشت (اثر شکل-زمینه) و تبیین «انگیزشی/هزینه‌محور» که منفی‌گرایی را به اهمیت اجتناب از زیان نسبت می‌دهد. این سوگیری در سطح فردی با منطق تولید خبر در سطح سازمانی هم‌افزا می‌شود: معیارهای خبری «تضاد»، «شکست» و «بحران» را برجسته می‌کنند، رسانه‌ها به تقاضای توجه مخاطب پاسخ می‌دهند، و رقابت بر سر کلیک و بیننده، چرخهٔ منفی‌گرایی را تقویت می‌کند. پیامدها دوسویه است: از یک سو، منفی‌گرایی می‌تواند آگاهی از خطر و نظارت بر قدرت را افزایش دهد؛ از سوی دیگر، می‌تواند به بدبینی، بی‌اعتمادی سیاسی و فرسایش سرمایهٔ اجتماعی بینجامد. در محیط پلتفرمی، الگوریتم‌های تعامل‌محور همین سوگیری را تشدید می‌کنند، زیرا محتوای برانگیزانندهٔ احساس، تعامل بیشتری برمی‌انگیزد.",
   "assumptions": [
     "اطلاعات منفی برجستگی شناختی و فیزیولوژیک بیشتری از اطلاعات مثبت دارد.",
     "سوگیری فردی با معیارهای خبری سازمانی هم‌افزا می‌شود.",
     "منفی‌گرایی خبری می‌تواند هم نظارت مدنی و هم بدبینی را تقویت کند."
   ],
   "principles": [
     "برانگیختگی نامتقارن: خبر منفی پاسخ قوی‌تر برمی‌انگیزد.",
     "هم‌افزایی عرضه و تقاضا: معیار خبری و توجه مخاطب همدیگر را تقویت می‌کنند.",
     "پیامد دوسویه: منفی‌گرایی هم نظارت‌آور است و هم بدبینی‌زا."
   ],
   "critiques": [
     "اعتبار بیرونی: محرک‌های آزمایشگاهی با مصرف خبر روزمره در بستر طبیعی تفاوت دارند.",
     "اندازهٔ اثر: شدت سوگیری و شرایط تعدیل‌کنندهٔ آن (نگرش پیشین، اعتماد به رسانه) به‌روشنی مشخص نیست.",
     "خلط مفاهیم: منفی‌گرایی محتوایی با بی‌ادبی و حملات شخصی یکی گرفته می‌شود."
   ],
   "applications": [
     "تحلیل ارزش‌های خبری و سیاست‌های تحریریه در پوشش سیاست.",
     "پژوهش دربارهٔ اثر منفی‌گرایی بر اعتماد سیاسی و مشارکت.",
     "طراحی مداخلات رسانه‌ای برای متعادل‌کردن پوشش خبری."
   ],
   "evolution": "لائو (1985) تبیین‌های نظری را صورت‌بندی کرد و سوروکا و همکاران (2019) شواهد فیزیولوژیک بین‌کشوری ارائه دادند. در دههٔ ۲۰۲۰، پژوهش منفی‌گرایی به محیط پلتفرمی، سوگیری الگوریتمی و اقتصاد توجه گسترش یافت.",
   "key_concepts": ["سوگیری منفی (negativity bias)", "برانگیختگی فیزیولوژیک (physiological arousal)", "ارزش خبری منفی (negative news value)", "اقتصاد توجه (attention economy)", "بدبینی سیاسی (political cynicism)"],
   "studies": ["Soroka, S., Fournier, P., & Nir, L. (2019). Cross-national evidence of a negativity bias. PNAS, 116(38), 18888-18892.", "Lau, R. R. (1985). Two explanations for negativity effects. AJPS, 29(1), 119-138."],
 },
 "MC-204": {
   "summary": "«مالکیت موضوع» (Issue Ownership) نظریه‌ای است که می‌گوید احزاب سیاسی از نظر رأی‌دهندگان، مالکِ قلمروهای موضوعی معینی هستند و در انتخابات، رأی‌دهندگان نامزدها را بر پایهٔ صلاحیت مورد انتظار در همان موضوع‌ها ارزیابی می‌کنند. جان پتروچیک این نظریه را در مقالهٔ «Issue Ownership in Presidential Elections» (۱۹۹۶، AJPS) تدوین کرد (Petrocik, 1996).",
   "main_problem": "چرا برخی موضوع‌ها به‌طور پایدار به یک حزب گره می‌خورند، و کارزارهای انتخاباتی چگونه با برجسته‌کردن موضوع‌های «مالکیت‌شده» بر معیارهای ارزیابی رأی‌دهندگان اثر می‌گذارند؟",
   "mechanism": "پتروچیک استدلال می‌کند که هر حزب از رهگذر تاریخ، پایگاه اجتماعی و کارنامهٔ گذشته، «شهرت» موضوعی می‌سازد: دموکرات‌ها در موضوع‌هایی مانند رفاه و بهداشت و جمهوری‌خواهان در موضوع‌هایی مانند مالیات و دفاع، مالکیت دارند (Petrocik, 1996). سازوکار انتخاباتی سه‌مرحله‌ای است: نخست، حزب مالکیت موضوعی را از تاریخ و گروه‌های حامی به‌دست می‌آورد؛ دوم، کارزار با «برجسته‌سازی» (priming) موضوع‌های مالکیت‌شده می‌کوشد وزن آن‌ها را در ذهن رأی‌دهنده بالا ببرد؛ سوم، رأی‌دهنده بر پایهٔ همان موضوع‌ها به نامزد «اعتبار عملکرد» می‌دهد و رأی خود را شکل می‌دهد. پتروچیک میان «موضوع‌های عملکردی» (performance issues) مانند اقتصاد، جنگ و فساد که به کارنامهٔ حزب گره می‌خورند و «موضوع‌های سیاستی» که به موضع برنامه‌ای مربوط‌اند، تفکیک می‌کند. نظریهٔ مالکیت به سنت قدیمی‌تر «نظریهٔ برجستگی» (salience theory) باج (Budge & Farlie, 1983) وابسته است، اما تأکید آن بر «شهرت» و «صلاحیت» است، نه فقط بر وزن موضوع. در رسانه، این نظریه توضیح می‌دهد چرا چارچوب‌بندی خبری «چه کسی در اقتصاد بهتر است» یا پرسش‌های مناظره، نابرابری موضوعی را بازتولید می‌کند و چگونه نامزدها می‌کوشند با «ورود به قلمرو موضوعی رقیب» (issue trespassing) مالکیت را به چالش بکشند.",
   "assumptions": [
     "احزاب از نظر رأی‌دهندگان مالکِ قلمروهای موضوعی پایداری هستند.",
     "کارزار با برجسته‌سازی موضوع‌ها، معیارهای ارزیابی رأی‌دهنده را شکل می‌دهد.",
     "مالکیت از تاریخ، پایگاه اجتماعی و کارنامهٔ حزب سرچشمه می‌گیرد."
   ],
   "principles": [
     "شهرت موضوعی: هر حزب در موضوع‌های معینی صلاحیت تلقی‌شده دارد.",
     "برجسته‌سازی: کارزار موضوع‌های مالکیت‌شده را برمی‌کشد.",
     "موضوع عملکردی: کارنامهٔ حزب، معیار اصلی ارزیابی است."
   ],
   "critiques": [
     "پویایی مالکیت: مالکیت موضوعی ثابت نیست و با رویدادها، رهبری و بحران‌ها جابه‌جا می‌شود.",
     "چالش سنجش: اندازه‌گیری مالکیت با پرسش‌های باز، به تفسیر و آستانه‌گذاری حساس است.",
     "نادیده‌گرفتن تعامل: نظریه کمتر توضیح می‌دهد که پوشش رسانه‌ای چگونه مالکیت را می‌سازد یا تخریب می‌کند."
   ],
   "applications": [
     "تحلیل راهبرد انتخاباتی و انتخاب موضوع‌های کمپین.",
     "پژوهش دربارهٔ چارچوب‌بندی رسانه‌ای صلاحیت حزبی.",
     "تحلیل مناظره‌ها و پرسش‌های خبری از منظر مالکیت موضوعی."
   ],
   "evolution": "باج و فارلی (1983) نظریهٔ برجستگی را پیش بردند و پتروچیک (1996) آن را به مالکیت موضوعی و صلاحیت حزبی گره زد. پژوهش‌های بعدی، پویایی مالکیت و نقش «ورود به قلمرو رقیب» را برجسته کردند.",
   "key_concepts": ["مالکیت موضوع (issue ownership)", "برجسته‌سازی (priming)", "شهرت حزبی (party reputation)", "موضوع عملکردی (performance issue)", "ورود به قلمرو رقیب (issue trespassing)"],
   "studies": ["Petrocik, J. R. (1996). Issue ownership in presidential elections. AJPS, 40(3), 825-850.", "Budge, I., & Farlie, D. J. (1983). Explaining and Predicting Elections. Allen & Unwin."],
 },
 "MC-205": {
   "summary": "«قطبی‌شدن عاطفی» (Affective Polarization) به شکاف احساسی فزاینده میان هواداران احزاب سیاسی اشاره دارد: افراد حزب رقیب را نه فقط از نظر سیاستی مخالف، بلکه به‌عنوان گروهی ناخوشایند و بیگانه تجربه می‌کنند. شانتو آیینگار، گوراو سود و ییپتاخ لِلکِس در «Affect, Not Ideology» (۲۰۱۲، Public Opinion Quarterly) نشان دادند ریشهٔ این شکاف بیشتر هویت اجتماعی است تا اختلاف ایدئولوژیک (Iyengar, Sood, & Lelkes, 2012).",
   "main_problem": "چرا در بسیاری از دموکراسی‌ها فاصلهٔ عاطفی میان هواداران احزاب بیش از فاصلهٔ مواضع سیاستی آن‌ها شده است، و این قطبی‌شدن چه پیامدهایی برای گفتمان عمومی، اعتماد و سلامت دموکراسی دارد؟",
   "mechanism": "آیینگار و همکاران با داده‌های بلندمدت نظرسنجی ملی آمریکا نشان دادند که احساس هواداران نسبت به حزب رقیب به‌طور پیوسته سردتر شده، در حالی که ارزیابی آن‌ها از نامزد خودی گرم‌تر مانده است؛ یعنی «قطبی‌شدن نامتقارن» (asymmetric polarization) رخ داده است (Iyengar et al., 2012). تبیین آن‌ها هویتی-اجتماعی است: حزب سیاسی به یک هویت گروهی بدل می‌شود که وفاداری، تعلق و «ما/آن‌ها» می‌سازد، و بر پایهٔ سازوکارهای شناخت اجتماعی — سوگیری درون‌گروهی، برون‌گروه‌هراسی و ادراک تهدید — نفرت از رقیب مستقل از اختلاف برنامه‌ای شکل می‌گیرد. مِیسون (Mason, 2018) نشان می‌دهد که «مرتب‌سازی اجتماعی» (social sorting) — هم‌راستایی دین، نژاد، محل زندگی و رسانهٔ مصرفی با حزب — این شکاف را عمیق‌تر می‌کند، زیرا تفاوت حزبی با تفاوت‌های زیستی و فرهنگی درهم می‌آمیزد. پیامدها گسترده‌اند: تبعیض در استخدام و ازدواج، کاهش تمایل به گفت‌وگو با مخالف، پذیرش نقض هنجارهای دموکراتیک برای شکست رقیب، و شکنندگی مشروعیت نهادی. در بستر رسانه، انتخاب‌گری مخاطب و رسانه‌های حزبی، اتاق‌های پژواک (echo chamber) می‌سازند که تصویر رقیب را اغراق‌آمیز و دشمن‌ساز می‌کند و قطبی‌شدن عاطفی را بازتولید می‌کند.",
   "assumptions": [
     "هویت حزبی سازوکاری اجتماعی و عاطفی است، نه فقط مجموعه‌ای از باورهای سیاستی.",
     "هویت درون‌گروهی، سوگیری و برون‌گروه‌هراسی ایجاد می‌کند.",
     "مرتب‌سازی اجتماعی و رسانه‌ای، شکاف عاطفی را عمیق‌تر می‌کند."
   ],
   "principles": [
     "عاطفه به‌جای ایدئولوژی: نفرت حزبی مستقل از اختلاف برنامه‌ای است.",
     "قطبی‌شدن نامتقارن: احساس سردی عمدتاً متوجه حزب رقیب است.",
     "مرتب‌سازی اجتماعی: هم‌راستایی هویت‌ها شکاف را تشدید می‌کند."
   ],
   "critiques": [
     "مسئلهٔ سنجش: دماسنج احساسی و فاصلهٔ اجتماعی، سازه‌های پیچیدهٔ قطبی‌شدن را ساده می‌کنند.",
     "تازگی پدیده: برخی پژوهش‌ها نشان می‌دهند بخشی از این شکاف پیشینهٔ تاریخی دارد و «جدید» خواندن آن نیازمند احتیاط است.",
     "تفکیک از ایدئولوژی: رابطهٔ قطبی‌شدن عاطفی با قطبی‌شدن ایدئولوژیک و مسائل سیاستی هنوز محل بحث است."
   ],
   "applications": [
     "تحلیل رسانه‌های حزبی و اتاق‌های پژواک در تشدید شکاف.",
     "پژوهش دربارهٔ پیامدهای قطبی‌شدن بر اعتماد و مشارکت دموکراتیک.",
     "طراحی مداخلات برای کاهش دشمن‌سازی میان هواداران احزاب."
   ],
   "evolution": "آیینگار و همکاران (2012) چارچوب هویتی-اجتماعی را تثبیت کردند و میسون (2018) مرتب‌سازی اجتماعی را برجسته کرد. در دههٔ ۲۰۲۰، پژوهش قطبی‌شدن عاطفی به رسانه‌های اجتماعی، الگوریتم‌ها و مقایسهٔ بین‌کشوری گسترش یافت.",
   "key_concepts": ["قطبی‌شدن عاطفی (affective polarization)", "هویت حزبی (partisan identity)", "قطبی‌شدن نامتقارن (asymmetric polarization)", "مرتب‌سازی اجتماعی (social sorting)", "اتاق پژواک (echo chamber)"],
   "studies": ["Iyengar, S., Sood, G., & Lelkes, Y. (2012). Affect, not ideology. Public Opinion Quarterly, 76(3), 405-431.", "Mason, L. (2018). Uncivil Agreement. University of Chicago Press."],
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
    codes = ["MC-202", "MC-203", "MC-204", "MC-205"]
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
    print("BATCH49 THEORY DONE")

if __name__ == "__main__":
    main()
