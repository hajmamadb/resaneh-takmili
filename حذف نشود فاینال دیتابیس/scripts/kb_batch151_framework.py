# -*- coding: utf-8 -*-
"""Batch 151 (MODEL): MC-584 mixed motive, MC-587 coorientation, MC-588 stealing thunder, MC-590 risk communication."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch151-model-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch151_model.json"

S = {
    "MC-584": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Limits of Symmetry: A Game Theory Approach to Symmetric and Asymmetric Public Relations",
             title_fa="حدود تقارن: رهیافتی از نظریهٔ بازی به روابط عمومی متقارن و نامتقارن",
             authors="Murphy, P.", year=1991,
             publisher="Public Relations Research Annual",
             doi=None,
             url="https://www.semanticscholar.org/paper/The-Limits-of-Symmetry%3A-A-Game-Theory-Approach-to-Murphy/bd81bb4ead94b703718a0899284ec426ade4a938",
             language="en", isbn=None,
             citation="Murphy, P. (1991). The limits of symmetry: A game theory approach to symmetric and asymmetric public relations. Public Relations Research Annual, 3, 115-131.",
             locator="3:115-131", locator_type="page_range",
             supports="mixed-motive games as a realistic middle path between pure cooperation and pure conflict", verified=True),
        dict(kind="BOOK_CHAPTER",
             title_en="Game Theory",
             title_fa="نظریهٔ بازی",
             authors="SAGE Encyclopedia of Public Relations", year=None,
             publisher="SAGE Publications",
             doi=None,
             url="https://sk.sagepub.com/ency/edvol/download/encyclopedia-of-public-relations-2e/chpt/game-theory.pdf",
             language="en", isbn=None,
             citation="SAGE Encyclopedia of Public Relations (2nd ed.). Entry: Game theory. Thousand Oaks: SAGE Publications.",
             locator="encyclopedia entry", locator_type="work",
             supports="bibliographic confirmation of Murphy's 1991 mixed-motive model", verified=True),
    ],
    "MC-587": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Interpersonal Approaches to Communication Research",
             title_fa="رهیافت‌های میان‌فردی در پژوهش ارتباط",
             authors="McLeod, J. M.; Chaffee, S. H.", year=1973,
             publisher="American Behavioral Scientist",
             doi="10.1177/000276427301600402",
             url="https://journals.sagepub.com/doi/abs/10.1177/000276427301600402",
             language="en", isbn=None,
             citation="McLeod, J. M., & Chaffee, S. H. (1973). Interpersonal approaches to communication research. American Behavioral Scientist, 16(4), 469-499.",
             locator="16(4):469-499", locator_type="page_range",
             supports="coorientation framework of agreement, accuracy and congruency", verified=True),
        dict(kind="OTHER",
             title_en="Family Communication Patterns: Measuring Intrapersonal Perceptions of Interpersonal Relationships",
             title_fa="الگوهای ارتباط خانوادگی: سنجش ادراک درون‌فردی از روابط میان‌فردی",
             authors="Ritchie, L. D.", year=1990,
             publisher="Portland State University (PDXScholar)",
             doi=None,
             url="https://pdxscholar.library.pdx.edu/cgi/viewcontent.cgi?article=1099&context=comm_fac",
             language="en", isbn=None,
             citation="Ritchie, L. D. (1990). Family communication patterns: Measuring intrapersonal perceptions of interpersonal relationships. Repository copy, Portland State University.",
             locator="repository copy", locator_type="work",
             supports="coorientation model as the basis for measuring mutual perception", verified=True),
    ],
    "MC-588": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Stormy Weather: Testing Stealing Thunder as a Crisis Communication Strategy to Improve Communication Flow Between Organizations and Journalists",
             title_fa="هوای طوفانی: آزمون دزدیدن رعد به‌عنوان راهبرد ارتباط بحران",
             authors="Arpan, L. M.; Pompper, D.", year=2003,
             publisher="Public Relations Review",
             doi=None,
             url="https://www.sciencedirect.com/science/article/abs/pii/S0363811103000432",
             language="en", isbn=None,
             citation="Arpan, L. M., & Pompper, D. (2003). Stormy weather: Testing stealing thunder as a crisis communication strategy to improve communication flow between organizations and journalists. Public Relations Review, 29(3), 291-308.",
             locator="29(3):291-308", locator_type="page_range",
             supports="proactive self-disclosure increases credibility and reduces negative coverage", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Weathering the Crisis: Effects of Stealing Thunder in Crisis Communication",
             title_fa="از سر گذراندن بحران: اثرهای دزدیدن رعد در ارتباط بحران",
             authors="Lee, S. Y.", year=2016,
             publisher="Public Relations Review",
             doi=None,
             url="https://www.sciencedirect.com/science/article/abs/pii/S0363811115301661",
             language="en", isbn=None,
             citation="Lee, S. Y. (2016). Weathering the crisis: Effects of stealing thunder in crisis communication. Public Relations Review.",
             locator="ScienceDirect article", locator_type="work",
             supports="later experimental evidence on the stealing-thunder effect", verified=True),
    ],
    "MC-590": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Determinants of Trust and Credibility in Environmental Risk Communication: An Empirical Study",
             title_fa="عوامل تعیین‌کنندهٔ اعتماد و اعتبار در ارتباطات خطر زیست‌محیطی",
             authors="Peters, R. G.; Covello, V. T.; McCallum, D. B.", year=1997,
             publisher="Risk Analysis",
             doi="10.1111/j.1539-6924.1997.tb00842.x",
             url="https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1539-6924.1997.tb00842.x",
             language="en", isbn=None,
             citation="Peters, R. G., Covello, V. T., & McCallum, D. B. (1997). The determinants of trust and credibility in environmental risk communication: An empirical study. Risk Analysis, 17(1), 43-54.",
             locator="17(1):43-54", locator_type="page_range",
             supports="competence, care and honesty as core dimensions of source credibility in risk messages", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Risk Communication and Message Mapping: A New Tool for Communicating Effectively in Public Health Emergencies and Disasters",
             title_fa="ارتباطات خطر و نقشه‌سازی پیام: ابزاری تازه برای ارتباط مؤثر در بحران‌های سلامت عمومی",
             authors="Covello, V. T.", year=2006,
             publisher="Journal of Emergency Management",
             doi="10.5055/jem.2006.0030",
             url="https://wmpllc.org/ojs/index.php/jem/article/view/1760",
             language="en", isbn=None,
             citation="Covello, V. T. (2006). Risk communication and message mapping: A new tool for communicating effectively in public health emergencies and disasters. Journal of Emergency Management, 4(3), 25-40.",
             locator="4(3):25-40", locator_type="page_range",
             supports="message mapping and trust-building principles in high-concern situations", verified=True),
    ],
}

ENRICH = {
    "MC-584": dict(
        year=1991,
        summary="مدل انگیزه مختلط، که پریسیلا مورفی در سال ۱۹۹۱ با تکیه بر نظریهٔ بازی صورت‌بندی کرد، مدل دوسویهٔ متقارن را از دوگانهٔ سادهٔ همکاری کامل و ستیز کامل بیرون می‌آورد. مورفی استدلال کرد که در روابط عمومی واقعی، سازمان و مخاطبان معمولاً در بازی مختلط‌انگیزه قرار دارند: هر طرف هم انگیزهٔ همکاری دارد و هم انگیزهٔ پیشبرد منافع خود. بنابراین، تقارن مطلق نه ممکن است و نه همیشه مطلوب؛ ارتباط مؤثر، مدیریت هوشمندانهٔ ترکیب همکاری و رقابت است. او از نظریهٔ بازی برای تحلیل راهبردهای سازمان در موقعیت‌های گوناگون بهره گرفت و نشان داد که انتخاب راهبرد به ساختار بازی، منافع طرف‌ها و پیش‌بینی رفتار دیگری بستگی دارد. مدل انگیزه مختلط، نقدی اصلاح‌گرانه بر مدل متقارن است، نه رد آن: هدف همچنان فهم متقابل است، اما ابزار آن واقع‌بینانه‌تر تعریف می‌شود. این مدل در مذاکره، مدیریت تعارض، گفت‌وگوی سازمانی و طراحی راهبرد ارتباطی کاربرد دارد. نقدهای اصلی به آن، انتقال کامل منطق سودمحور بازی به ارتباط انسانی، کم‌توجهی به ارزش‌ها و اخلاق، دشواری تعیین ساختار واقعی بازی و سنجش تجربی محدود را برجسته می‌کنند.",
        definition="مدل انگیزه مختلط، روابط عمومی را بازی مختلط‌انگیزه می‌داند که در آن سازمان و مخاطب هم‌زمان انگیزهٔ همکاری و رقابت دارند و راهبرد ارتباطی باید ترکیبی واقع‌بینانه از هر دو را مدیریت کند.",
        main_problem="چگونه می‌توان در روابط عمومی، بدون فرض همکاری کامل یا ستیز کامل، راهبرد ارتباطی را بر پایهٔ منافع مشترک و متعارض طرفین طراحی کرد.",
        mechanism="سازمان ساختار بازی، منافع خود و انتظار رفتار مخاطب را تحلیل می‌کند؛ سپس راهبردی برمی‌گزیند که در آن هم همکاری برای فهم مشترک حفظ شود و هم منافع اختصاصی پیش برده شود.",
        assumptions=[
            "انگیزه‌های طرفین مختلط است.",
            "سازمان و مخاطب بازیگران عقلانی‌اند.",
            "انتخاب راهبرد به ساختار بازی بستگی دارد.",
            "تقارن مطلق همیشه ممکن نیست.",
            "فهم متقابل با رقابت قابل جمع است.",
        ],
        principles=[
            "ساختار بازی را پیش از پیام تحلیل کن.",
            "منافع مشترک و متعارض را جدا کن.",
            "انتظار رفتار طرف مقابل را بسنج.",
            "همکاری را ابزار فهم متقابل بگیر.",
            "رقابت را پنهان نکن.",
            "راهبرد را با تغییر بازی بازنگری کن.",
        ],
        critiques=[
            "منطق سودمحور را به ارتباط انسانی تعمیم می‌دهد.",
            "ارزش‌ها و اخلاق را کم‌بررسی می‌گذارد.",
            "تعیین ساختار واقعی بازی دشوار است.",
            "سنجش تجربی مدل محدود است.",
            "قدرت نامتوازن طرفین را کم‌می‌شمارد.",
            "فرهنگ را در انتخاب راهبرد نادیده می‌گیرد.",
            "بازی‌های تکراری و بلندمدت را کم‌بررسی می‌گذارد.",
            "اعتماد را صرفاً منفعت عقلانی تعریف می‌کند.",
            "احساس اخلاقی طرفین را در محاسبهٔ سود نادیده می‌گیرد.",
        ],
        critique_text="منتقدان می‌گویند مدل انگیزه مختلط تصویر واقع‌بینانه‌تری از روابط عمومی داد اما منطق بازی را بیش از حد بر ارتباط انسانی تحمیل کرد و ارزش‌ها و قدرت را کم‌بررسی گذاشت؛ با این حال، چارچوبی مؤثر برای تحلیل مذاکره و تعارض سازمانی فراهم کرد.",
        applications=[
            "تحلیل مذاکره سازمانی.",
            "مدیریت تعارض با ذی‌نفعان.",
            "طراحی راهبرد بحران.",
            "آموزش روابط عمومی.",
            "تحلیل گفت‌وگوی سیاسی.",
            "پژوهش رفتار سازمانی.",
            "تحلیل اتحاد راهبردی.",
            "طراحی گفت‌وگوی چندجانبه.",
        ],
        example_text="سازمانی که برای تغییر یک مقرره با نهاد ناظر گفت‌وگو می‌کند، هم به دنبال توافق مشترک است و هم منافع خود را پیش می‌برد؛ مدل انگیزه مختلط این ترکیب را نه ریاکاری، بلکه واقعیت بازی ارتباطی می‌داند.",
        evolution="مقالهٔ سال ۱۹۹۱ مورفی مدل انگیزه مختلط را معرفی کرد و نقدی اصلاح‌گرانه بر تقارن مطلق ارائه داد. پژوهش‌های بعدی، آن را در مدیریت تعارض، مذاکره و راهبرد ارتباطی به کار گرفتند.",
        key_concepts=["بازی مختلط‌انگیزه", "نظریهٔ بازی", "تقارن", "همکاری و رقابت", "مذاکره", "منافع متعارض"],
        theorists="پریسیلا مورفی.",
        theorists_text="مدل در سنت پژوهش روابط عمومی و نظریهٔ بازی شکل گرفت.",
        model="ارتباط سازمانی به‌عنوان بازی مختلط‌انگیزه که راهبرد آن ترکیبی از همکاری برای فهم مشترک و رقابت برای منافع اختصاصی است.",
        studies=[
            "مقالهٔ سال ۱۹۹۱ مدل را صورت‌بندی کرد.",
            "پژوهش تعارض، کاربرد آن را سنجید.",
            "مطالعات مذاکره، راهبردهای مختلط را آزمودند.",
            "پژوهش سازمانی، نقش قدرت را بررسی کرد.",
            "مطالعهٔ دیجیتال، بازی مختلط در شبکه را تحلیل کرد.",
            "پژوهش میان‌فرهنگی، تفاوت راهبرد را سنجید.",
            "مطالعهٔ اعتماد، سابقهٔ همکاری را بررسی کرد.",
        ],
    ),
    "MC-587": dict(
        year=1973,
        summary="مدل هم‌جهت‌یابی، که جک مک‌لوید و استیون چفی در سال ۱۹۷۳ صورت‌بندی کردند، ارتباط را نه انتقال پیام، بلکه هم‌سوسازی ادراک دو طرف دربارهٔ یک موضوع می‌داند. در این مدل، هر طرف سه عنصر دارد: خود، طرف دیگر و موضوع مورد توجه. هم‌جهت‌یابی از سه مؤلفه ساخته می‌شود: توافق، یعنی داشتن نگرش مشابه به موضوع؛ دقت، یعنی درست‌فهمیدن نگرش طرف دیگر؛ و هم‌خوانی، یعنی تصور درست از آنچه طرف دیگر دربارهٔ ما فکر می‌کند. ارتباط مؤثر زمانی رخ می‌دهد که این سه مؤلفه در وضعیت متعادل باشند. مدل نخست در پژوهش ارتباط خانوادگی و میان‌فردی به کار رفت و سپس به تحلیل رابطهٔ سازمان و افکار عمومی گسترش یافت: سازمان باید بداند مخاطب چه می‌اندیشد، ادراک خود او از مخاطب چقدر درست است و فاصلهٔ نگرش‌ها کجاست. هم‌جهت‌یابی ابزار سنجش خوبی برای شکاف ادراکی میان سازمان و مخاطب فراهم می‌کند و نشان می‌دهد که سوءتفاهم، پیش از آنکه مسئلهٔ پیام باشد، مسئلهٔ ادراک است. نقدهای اصلی به مدل، تمرکز بر ادراک فردی به‌جای ساختار اجتماعی، دشواری سنجش هم‌زمان سه مؤلفه، ایستایی نسبی تصویر و کم‌توجهی به قدرت و منافع را برجسته می‌کنند.",
        definition="مدل هم‌جهت‌یابی، ارتباط را هم‌سوسازی ادراک دو طرف دربارهٔ یک موضوع می‌داند و آن را با سه مؤلفهٔ توافق، دقت و هم‌خوانی می‌سنجد.",
        main_problem="چگونه می‌توان کیفیت ارتباط میان دو طرف را نه با میزان پیام ردوبدل‌شده، بلکه با میزان هم‌سویی و درستی ادراک متقابل آنان دربارهٔ یک موضوع سنجید.",
        mechanism="هر طرف نگرشی به موضوع دارد و تصوری از نگرش طرف دیگر می‌سازد؛ مقایسهٔ این نگرش‌ها و تصورها سه مؤلفهٔ توافق، دقت و هم‌خوانی را می‌سازد و میزان هم‌جهت‌یابی را نشان می‌دهد.",
        assumptions=[
            "ارتباط ادراک متقابل می‌سازد.",
            "سه مؤلفهٔ توافق، دقت و هم‌خوانی قابل سنجش‌اند.",
            "هم‌جهت‌یابی بالا ارتباط مؤثرتر می‌سازد.",
            "تصور از دیگری بر رفتار اثر می‌گذارد.",
            "موضوع مشترک، واحد تحلیل است.",
        ],
        principles=[
            "نگرش هر طرف را جدا بسنج.",
            "تصور هر طرف از دیگری را ثبت کن.",
            "توافق را از دقت جدا تحلیل کن.",
            "هم‌خوانی را با پرسش مستقیم بسنج.",
            "شکاف ادراکی را گزارش کن.",
            "تغییر ادراک را در زمان پیگیری کن.",
        ],
        critiques=[
            "بر ادراک فردی متمرکز است.",
            "ساختار اجتماعی را کم‌بررسی می‌گذارد.",
            "سنجش هم‌زمان سه مؤلفه دشوار است.",
            "تصویر را نسبتاً ایستا فرض می‌کند.",
            "قدرت و منافع را نادیده می‌گیرد.",
            "تعمیم آن به مخاطبان انبوه محدود است.",
            "تغییر سریع نگرش را کم‌بررسی می‌گذارد.",
            "سنجش هم‌خوانی را به پاسخ کلامی محدود می‌کند.",
            "جنبهٔ احساسی هم‌جهت‌یابی را کم‌می‌سنجد.",
            "نقش رسانه در شکل‌دادن ادراک را کم‌بررسی می‌گذارد.",
        ],
        critique_text="منتقدان می‌گویند مدل هم‌جهت‌یابی ابزار دقیقی برای سنجش شکاف ادراکی داد اما ارتباط را به ادراک فردی فروکاست و ساختار قدرت و منافع را کم‌بررسی گذاشت؛ با این حال، همچنان پایهٔ پژوهش ارتباط خانوادگی و سنجش رابطهٔ سازمان و افکار عمومی است.",
        applications=[
            "سنجش شکاف سازمان و مخاطب.",
            "پژوهش ارتباط خانوادگی.",
            "طراحی پیام سلامت.",
            "تحلیل ارتباط میان‌فرهنگی.",
            "ارزیابی کمپین عمومی.",
            "آموزش مذاکره.",
            "سنجش اعتماد نهادی.",
            "تحلیل رابطهٔ پزشک و بیمار.",
        ],
        example_text="سازمانی می‌پندارد مخاطبان از برنامهٔ جدیدش راضی‌اند، اما پیمایش نشان می‌دهد مخاطبان نگرش منفی دارند و سازمان این نگرش را نادرست می‌فهمد؛ مدل هم‌جهت‌یابی این شکاف را در دقت و هم‌خوانی آشکار می‌کند.",
        evolution="مقالهٔ سال ۱۹۷۳ مک‌لوید و چفی مدل هم‌جهت‌یابی را تثبیت کرد و به پژوهش ارتباط خانوادگی و سازمانی راه یافت. پژوهش‌های بعدی، آن را در سنجش ادراک متقابل و ارزیابی کمپین به کار گرفتند.",
        key_concepts=["هم‌جهت‌یابی", "توافق", "دقت", "هم‌خوانی", "ادراک متقابل", "شکاف ادراکی"],
        theorists="جک مک‌لوید و استیون چفی.",
        theorists_text="مدل در سنت پژوهش ارتباط میان‌فردی و خانوادگی شکل گرفت.",
        model="سه‌گانهٔ خود، دیگری و موضوع که با توافق، دقت و هم‌خوانی، میزان هم‌سویی ادراک دو طرف را می‌سنجد.",
        studies=[
            "مقالهٔ سال ۱۹۷۳ مدل را صورت‌بندی کرد.",
            "پژوهش خانواده، سه مؤلفه را سنجید.",
            "مطالعات سازمانی، شکاف ادراکی را تحلیل کردند.",
            "پژوهش کمپین، دقت ادراک مخاطب را بررسی کرد.",
            "مطالعهٔ سلامت، هم‌خوانی پزشک و بیمار را سنجید.",
            "پژوهش سازمانی، ادراک کارکنان را اندازه گرفت.",
        ],
    ),
    "MC-588": dict(
        year=2003,
        summary="مدل دزدیدن رعد، که لورا آرپان و دِنا پامپر در سال ۲۰۰۳ آزمودند، راهبردی پیش‌دستانه در ارتباط بحران است: سازمان پیش از آنکه رسانه یا دیگران خبر بحران را افشا کنند، خودش آن را اعلام می‌کند. منطق این راهبرد آن است که افشای خودخواسته، سازمان را از موضع پاسخ‌دهنده به موضع منبع اولیه تبدیل می‌کند و اعتبار آن را بالا می‌برد. پژوهش آرپان و پامپر نشان داد افشای پیش‌دستانه، ارزیابی خبرنگاران و مخاطبان از سازمان را بهبود می‌دهد و پوشش خبری منفی را کاهش می‌دهد. این اثر با سازوکارهایی مانند افزایش شفافیت، کاهش احساس پنهان‌کاری، پیشی‌گرفتن از روایت رقیب و شکل‌دادن به چارچوب خبر توضیح داده می‌شود. با این حال، دزدیدن رعد برای هر بحرانی مناسب نیست: شدت بحران، مسئولیت سازمان، آمادگی پاسخ و اعتبار پیشین آن شرط‌های مهمی‌اند. این مدل در مدیریت بحران شرکت‌ها، ارتباطات سیاسی و روابط عمومی سازمان‌های عمومی به کار می‌رود. نقدهای اصلی به آن، خطر شتاب‌زدگی و افشای ناقص، کاهش اعتماد در صورت نادرستی اطلاعات، تفاوت اثر در فرهنگ‌های گوناگون و محدودیت شواهد تجربی را برجسته می‌کنند.",
        definition="مدل دزدیدن رعد، راهبردی است که در آن سازمان پیش از افشای بحران توسط دیگران، خودش خبر را اعلام می‌کند تا اعتبار، کنترل روایت و اعتماد مخاطب را حفظ کند.",
        main_problem="آیا افشای پیش‌دستانهٔ بحران توسط سازمان، بهتر از انتظار برای افشای رسانه‌ای است و این راهبرد تحت چه شرایطی اعتبار و اعتماد را حفظ می‌کند.",
        mechanism="سازمان خبر بحران را پیش از دیگران اعلام می‌کند، منبع اولیهٔ اطلاعات می‌شود، احساس پنهان‌کاری را کاهش می‌دهد و چارچوب روایت را شکل می‌دهد؛ در نتیجه ارزیابی مخاطب و پوشش خبری بهبود می‌یابد.",
        assumptions=[
            "افشای خودخواسته شفافیت می‌سازد.",
            "منبع اولیه از روایت رقیب پیش می‌افتد.",
            "اعتبار سازمان بر ارزیابی خبر اثر دارد.",
            "مخاطب پنهان‌کاری را تنبیه می‌کند.",
            "شدت بحران بر کارآمدی راهبرد اثر دارد.",
        ],
        principles=[
            "شدت بحران را پیش از افشا بسنج.",
            "اطلاعات پیش‌دستانه را کامل و درست کن.",
            "مسئولیت را شفاف بپذیر.",
            "زمان‌بندی افشا را دقیق تعیین کن.",
            "برنامهٔ پاسخ را همراه اعلام ارائه کن.",
            "پیگیری اطلاعات را تضمین کن.",
            "وضعیت بحران را در افشا روشن اعلام کن.",
        ],
        critiques=[
            "خطر شتاب‌زدگی و افشای ناقص دارد.",
            "اطلاعات نادرست اعتماد را نابود می‌کند.",
            "اثر آن در فرهنگ‌ها متفاوت است.",
            "شواهد تجربی آن محدود است.",
            "برای بحران‌های شدید مناسب نیست.",
            "منافع ذی‌نفعان را کم‌بررسی می‌گذارد.",
            "برای بحران‌های پیچیده و چندلایه قاعدهٔ روشنی ندارد.",
            "اثر آن بر اعتماد بلندمدت کم‌سنجیده مانده است.",
            "به سازمان‌های کوچک و کم‌منبع توصیهٔ یکسانی می‌دهد.",
            "نقش وکیل و مشاور حقوقی را در زمان‌بندی نادیده می‌گیرد.",
        ],
        critique_text="منتقدان می‌گویند مدل دزدیدن رعد راهبردی هوشمندانه برای کنترل روایت بحران ارائه داد اما خطر افشای ناقص و شتاب‌زدگی را کم‌بررسی گذاشت و شواهد آن محدود ماند؛ با این حال، به یکی از توصیه‌های رایج ارتباط بحران تبدیل شد.",
        applications=[
            "مدیریت بحران شرکت.",
            "ارتباطات سیاسی.",
            "روابط عمومی نهادهای عمومی.",
            "آموزش سخنگو.",
            "طراحی برنامهٔ افشا.",
            "پژوهش اعتماد سازمانی.",
            "ارزیابی بحران سلامت.",
            "طراحی پیام افشای خطا.",
        ],
        example_text="شرکتی که نقص فنی محصول را پیش از گزارش رسانه‌ها اعلام می‌کند و برنامهٔ فراخوان را همراه آن ارائه می‌دهد، روایت بحران را در دست می‌گیرد؛ افشای دیرهنگام همان نقص، معمولاً پنهان‌کاری تعبیر می‌شود.",
        evolution="پژوهش سال ۲۰۰۳ آرپان و پامپر راهبرد دزدیدن رعد را آزمود و به ادبیات ارتباط بحران وارد کرد. پژوهش‌های بعدی، شرایط و محدودیت‌های آن را در بحران‌های گوناگون بررسی کردند.",
        key_concepts=["دزدیدن رعد", "افشای پیش‌دستانه", "ارتباط بحران", "اعتبار", "شفافیت", "کنترل روایت"],
        theorists="لورا آرپان و دِنا پامپر.",
        theorists_text="مدل در سنت پژوهش ارتباط بحران و روابط عمومی شکل گرفت.",
        model="افشای خودخواستهٔ بحران پیش از افشای رسانه‌ای که اعتبار، کنترل روایت و اعتماد مخاطب را حفظ می‌کند.",
        studies=[
            "پژوهش سال ۲۰۰۳ اثر افشای پیش‌دستانه را آزمود.",
            "مطالعات بعدی شرایط کارآمدی آن را سنجیدند.",
            "پژوهش خبرنگاران، ارزیابی منبع را بررسی کرد.",
            "مطالعات میان‌فرهنگی، تفاوت اثر را نشان دادند.",
            "پژوهش رسانهٔ اجتماعی، سرعت افشا را بررسی کرد.",
            "مطالعهٔ بحران سلامت، اعتماد عمومی را سنجید.",
        ],
    ),
    "MC-590": dict(
        year=1997,
        summary="مدل ارتباطات خطر، که وینسنت کاوالو و همکارانش در پژوهش سال ۱۹۹۷ دربارهٔ عوامل اعتماد و اعتبار صورت‌بندی کردند، ارتباط دربارهٔ خطر را فرایندی برای ساختن فهم مشترک و اعتماد می‌داند، نه فقط انتقال اطلاعات فنی. در این مدل، مخاطب در وضعیت خطر با محدودیت شناختی روبه‌روست: اضطراب، اطلاعات ناقص و پیام‌های متناقض، ظرفیت پردازش او را کم می‌کند. از این رو، اثربخشی پیام بیش از دقت عددی، به اعتبار منبع بستگی دارد. پژوهش سال ۱۹۹۷ سه بُعد اصلی اعتبار را شناسایی کرد: شایستگی و تخصص، توجه و مراقبت، و صداقت و شفافیت. پیام مؤثر باید کوتاه، روشن، عملمحور و متناسب با سطح نگرانی مخاطب باشد. کاوالو در سال ۲۰۰۶ ابزار نقشه‌سازی پیام را برای موقعیت‌های پرنگرانی سلامت عمومی معرفی کرد که در آن پیام‌های کلیدی پیش از بحران آماده و آزموده می‌شوند. مدل در ارتباطات سلامت، مدیریت بحران، خطرهای زیست‌محیطی و ارتباطات علمی کاربرد دارد و نشان می‌دهد که بی‌اعتمادی، پیش از آنکه مسئلهٔ اطلاعات باشد، مسئلهٔ رابطه است. نقدهای اصلی به آن، تمرکز بر اعتماد منبع به‌جای ساختار اجتماعی خطر، کم‌توجهی به بی‌اعتمادی نهادی، دشواری سنجش ادراک خطر و تفاوت‌های فرهنگی در اعتماد را برجسته می‌کنند.",
        definition="مدل ارتباطات خطر، ارتباط دربارهٔ خطر را فرایندی برای ساختن فهم مشترک و اعتماد می‌داند که در آن اعتبار منبع و روشنی پیام، بیش از دقت فنی، رفتار مخاطب را شکل می‌دهد.",
        main_problem="چگونه می‌توان در وضعیت خطر، با وجود اضطراب و اطلاعات ناقص، پیامی ساخت که مخاطب آن را بفهمد، باور کند و بر پایهٔ آن عمل کند.",
        mechanism="مخاطبِ مضطرب ظرفیت پردازش محدودی دارد؛ پیام کوتاه و روشن از منبعی که شایسته، مراقب و صادق تلقی شود، اعتماد می‌سازد و احتمال پذیرش توصیهٔ محافظتی را افزایش می‌دهد.",
        assumptions=[
            "مخاطب در وضعیت خطر اضطراب دارد.",
            "ظرفیت پردازش اطلاعات محدود است.",
            "اعتبار منبع بر پذیرش پیام مقدم است.",
            "پیام روشن و عملمحور مؤثرتر است.",
            "اعتماد در زمان ساخته می‌شود.",
        ],
        principles=[
            "پیام را کوتاه و روشن نگه دار.",
            "اعتبار منبع را پیش از بحران بساز.",
            "نگرانی مخاطب را به رسمیت بشناس.",
            "توصیهٔ عملی مشخص ارائه کن.",
            "پیام را با ذی‌نفعان بیازما.",
            "اطلاعات ناقص را شفاف اعلام کن.",
        ],
        critiques=[
            "بر اعتماد منبع متمرکز است.",
            "ساختار اجتماعی خطر را کم‌بررسی می‌گذارد.",
            "بی‌اعتمادی نهادی را نادیده می‌گیرد.",
            "سنجش ادراک خطر دشوار است.",
            "تفاوت فرهنگی در اعتماد کم‌بررسی مانده است.",
            "خطر سیاسی‌شدن پیام را کم‌می‌شمارد.",
            "اعتماد نهادی را بیش از حد ایستا فرض می‌کند.",
            "نقش رسانه در ساختن خطر را کم‌بررسی می‌گذارد.",
            "نابرابری دسترسی به اطلاعات را کم‌می‌شمارد.",
            "اعتماد میان نهادها را ساده‌تر از واقع فرض می‌کند.",
        ],
        critique_text="منتقدان می‌گویند مدل ارتباطات خطر چارچوب عملی ارزشمندی برای پیام‌سازی در بحران داد اما اعتماد را بیش از حد به منبع فروکاست و بی‌اعتمادی نهادی و ساختار اجتماعی خطر را کم‌بررسی گذاشت؛ با این حال، پایهٔ آموزش ارتباط خطر و نقشه‌سازی پیام است.",
        applications=[
            "ارتباطات سلامت عمومی.",
            "مدیریت بحران زیست‌محیطی.",
            "آموزش خطر بلایا.",
            "طراحی پیام واکسیناسیون.",
            "ارتباطات علمی.",
            "آموزش سخنگوی نهاد.",
            "طراحی هشدار اقلیمی.",
            "ارزیابی اعتماد عمومی.",
            "طراحی پرسش‌نامهٔ ادراک خطر.",
        ],
        example_text="در هشدار دربارهٔ یک خطر زیست‌محیطی، پیامی که فقط عدد و نمودار نشان دهد کمتر از پیامی اثر دارد که از منبعی شناخته‌شده و قابل‌اعتماد، خطر را روشن توضیح دهد و بگوید مردم چه کاری می‌توانند انجام دهند.",
        evolution="پژوهش سال ۱۹۹۷ کاوالو و همکاران ابعاد اعتماد و اعتبار را تثبیت کرد. ابزار نقشه‌سازی پیام در سال ۲۰۰۶ چارچوب عملی برای بحران‌های سلامت عمومی فراهم کرد و پژوهش‌های بعدی آن را گستردند.",
        key_concepts=["اعتماد", "اعتبار منبع", "ادراک خطر", "نقشه‌سازی پیام", "ظرفیت پردازش", "ارتباط بحران"],
        theorists="وینسنت کاوالو و همکاران.",
        theorists_text="مدل در سنت پژوهش ارتباط خطر و سلامت عمومی شکل گرفت.",
        model="پیام خطر کوتاه، روشن و عملمحور از منبعی شایسته، مراقب و صادق که فهم مشترک و رفتار محافظتی می‌سازد.",
        studies=[
            "پژوهش سال ۱۹۹۷ ابعاد اعتبار را شناسایی کرد.",
            "ابزار سال ۲۰۰۶ نقشه‌سازی پیام را معرفی کرد.",
            "مطالعات سلامت، پیام‌سازی را آزمودند.",
            "پژوهش بحران، اعتماد نهادی را بررسی کرد.",
            "مطالعهٔ اقلیم، پیام خطر را در جامعه آزمود.",
        ],
    ),
}

NAME_FIX = {
    "MC-588": ("مدل دزدیدن رعد", "Stealing Thunder Model", "عنوان کارت با گیومهٔ تودرتو و انتساب نادرست ثبت شده بود؛ عنوان تمیز و انتساب مستند جایگزین شد."),
}
YEAR_FIX = {
    "MC-584": "سال ۱۹۹۴ و انتساب «مورفی و گرونیگ» در کارت با مقالهٔ سال ۱۹۹۱ مورفی هم‌خوان نبود؛ سال و انتساب درست ثبت شد.",
    "MC-588": "انتساب کارت به ویلیامز و همکاران در سال ۱۹۹۳ با ادبیات مستند دزدیدن رعد هم‌خوان نبود؛ سال ۲۰۰۳ به‌عنوان شاهد اصلی ثبت شد.",
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
                                       "verified": n_verified, "batch": 151}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH151 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
