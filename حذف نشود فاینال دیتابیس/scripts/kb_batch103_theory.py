# -*- coding: utf-8 -*-
"""Batch 103: full documentation for MC-634, MC-635, MC-636, MC-646."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch103-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch103_theory.json"

S = {
    "MC-634": [
        dict(kind="OTHER",
             title_en="The Servant as Leader",
             title_fa="خدمتگزار در نقش رهبر",
             authors="Greenleaf, R. K.", year=1970, publisher="Robert K. Greenleaf Center",
             doi=None, url="https://greenleaf.org/what-is-servant-leadership/",
             language="en", isbn=None,
             citation="Greenleaf, R. K. (1970). The servant as leader. Robert K. Greenleaf Center.",
             locator="work", locator_type="work",
             supports="servant-first orientation / test of follower growth", verified=True),
        dict(kind="BOOK",
             title_en="Servant Leadership: A Journey into the Nature of Legitimate Power and Greatness",
             title_fa="رهبری خدمتگزار: سفری به سرشت قدرت مشروع و بزرگی",
             authors="Greenleaf, R. K.", year=1977, publisher="Paulist Press",
             doi=None, url=None, language="en", isbn=None,
             citation="Greenleaf, R. K. (1977). Servant leadership: A journey into the nature of legitimate power and greatness. Paulist Press.",
             locator="work", locator_type="work",
             supports="book-length elaboration of servant leadership", verified=False),
    ],
    "MC-635": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Emotional Intelligence",
             title_fa="هوش عاطفی",
             authors="Salovey, P.; Mayer, J. D.", year=1990,
             publisher="Imagination, Cognition and Personality",
             doi="10.2190/DUGG-P24E-52WK-6CDG",
             url="https://journals.sagepub.com/doi/10.2190/dugg-p24e-52wk-6cdg",
             language="en", isbn=None,
             citation="Salovey, P., & Mayer, J. D. (1990). Emotional intelligence. Imagination, Cognition and Personality, 9(3), 185-211. https://doi.org/10.2190/DUGG-P24E-52WK-6CDG",
             locator="9(3):185-211", locator_type="page_range",
             supports="emotional intelligence as a set of emotion-related abilities", verified=True),
        dict(kind="BOOK_CHAPTER",
             title_en="What Is Emotional Intelligence?",
             title_fa="هوش عاطفی چیست؟",
             authors="Mayer, J. D.; Salovey, P.", year=1997,
             publisher="Basic Books",
             doi=None, url=None, language="en", isbn=None,
             citation="Mayer, J. D., & Salovey, P. (1997). What is emotional intelligence? In P. Salovey & D. Sluyter (Eds.), Emotional development and emotional intelligence. Basic Books.",
             locator="work", locator_type="work",
             supports="four-branch ability model of emotional intelligence", verified=False),
    ],
    "MC-636": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Employer Brand",
             title_fa="برند کارفرما",
             authors="Ambler, T.; Barrow, S.", year=1996,
             publisher="Journal of Brand Management",
             doi="10.1057/bm.1996.42",
             url="https://link.springer.com/article/10.1057/bm.1996.42",
             language="en", isbn=None,
             citation="Ambler, T., & Barrow, S. (1996). The employer brand. Journal of Brand Management, 4(3), 185-206. https://doi.org/10.1057/bm.1996.42",
             locator="4(3):185-206", locator_type="page_range",
             supports="functional, economic and psychological employment benefits", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Conceptualizing and Researching Employer Branding",
             title_fa="مفهوم‌سازی و پژوهش برندسازی کارفرما",
             authors="Backhaus, K.; Tikoo, S.", year=2004,
             publisher="Career Development International",
             doi=None, url=None, language="en", isbn=None,
             citation="Backhaus, K., & Tikoo, S. (2004). Conceptualizing and researching employer branding. Career Development International, 9(5), 501-517.",
             locator="9(5):501-517", locator_type="page_range",
             supports="employer branding framework for attraction and retention", verified=False),
    ],
    "MC-646": [
        dict(kind="BOOK",
             title_en="The Ecological Approach to Visual Perception",
             title_fa="رویکرد بوم‌شناختی به ادراک دیداری",
             authors="Gibson, J. J.", year=1979, publisher="Houghton Mifflin",
             doi=None, url="https://monoskop.org/images/c/c6/Gibson_James_J_1977_1979_The_Theory_of_Affordances.pdf",
             language="en", isbn=None,
             citation="Gibson, J. J. (1979). The ecological approach to visual perception. Houghton Mifflin.",
             locator="work", locator_type="work",
             supports="affordances as directly perceived action possibilities", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Technologies, Texts and Affordances",
             title_fa="فناوری‌ها، متن‌ها و امکانات عمل",
             authors="Hutchby, I.", year=2001, publisher="Sociology",
             doi=None, url=None, language="en", isbn=None,
             citation="Hutchby, I. (2001). Technologies, texts and affordances. Sociology, 35(2), 441-456.",
             locator="35(2):441-456", locator_type="page_range",
             supports="affordance concept extended to communication technologies", verified=False),
    ],
}

ENRICH = {
    "MC-634": {
        "summary": "(گرین‌لیف، ۱۹۷۰) رهبری خدمتگزار با این پرسش آغاز می‌شود که رهبر نخست خدمتگزار است یا نخست رهبر. گرین‌لیف می‌گوید خدمت پیش از رهبری می‌آید و معیار موفقیت، رشد پیروان است: آیا کسانی که خدمت می‌شوند سالم‌تر، خردمندتر، آزادتر و خودمختارتر می‌شوند و خود خدمتگزار دیگران می‌شوند؟ رهبر خدمتگزار با شنیدن، همدلی، اقناع و پیش‌بینی هدایت می‌کند، نه با کنترل. این رویکرد، رهبری را از قدرت به مسئولیت و از پیرو به شهروند سازمانی منتقل می‌کند. این چارچوب در پژوهش رهبری به‌عنوان بدیل اخلاقی رهبری کاریزماتیک و مبادله‌ای مطرح شد و مبنای مدل‌های بعدی رهبری خدمتگزار قرار گرفت.",
        "definition": "رهبری خدمتگزار، رویکردی است که رهبر را نخست خدمتگزار می‌داند و موفقیت او را با رشد، آزادی و توانمندی کسانی که خدمت می‌شوند می‌سنجد.",
        "main_problem": "مسئله این است که رهبری اغلب به کنترل و منزلت رهبر می‌پردازد و نه به نیاز پیروان. پاسخ گرین‌لیف، جابه‌جایی ترتیب خدمت و رهبری است. پرسش دوم، مرز است: خدمتگزار بودن چه زمانی به ضعف تصمیم و بی‌مرزی سازمانی می‌انجامد.",
        "mechanism": "۱. خدمت نخست: انگیزه اصلی رهبر، خدمت است و رهبری ابزار تحقق آن.\n۲. شنیدن: رهبر پیش از سخن گفتن می‌شنود و معنای واقعی نیاز را می‌فهمد.\n۳. همدلی و پذیرش: فرد در تمامیت خود پذیرفته می‌شود، نه فقط در نقش کاری.\n۴. اقناع: رهبر با استدلال و اعتماد هدایت می‌کند، نه با اجبار و پاداش.\n۵. پیش‌بینی: رهبر پیامدهای آینده تصمیم را می‌بیند و از بحران پیشگیری می‌کند.\n۶. رشد و جامعه‌سازی: رهبر ظرفیت پیروان را می‌سازد و اجتماع سازمانی را تقویت می‌کند.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا سردبیری که رشد خبرنگاران را بر منزلت خود مقدم می‌داند، تحریریه‌ای یادگیرنده می‌سازد و چرا رهبری مبتنی بر ترس، خلاقیت را می‌کشد. در رسانه عمومی که مأموریت خدمت به مخاطب دارد، این رویکرد با هویت سازمان هم‌خوان است. نکته مهم این است که خدمت بی مرز به فرسودگی رهبر و ابهام مسئولیت می‌انجامد؛ رهبر خدمتگزار باید هم پاسخگو باشد و هم مرزگذار.",
        "assumptions": [
            "خدمت، انگیزه اصلی رهبری است.",
            "رشد پیرو، معیار موفقیت رهبری است.",
            "اقناع بر اجبار مقدم است.",
        ],
        "principles": [
            "رهبری پیش از خدمت نمی‌آید.",
            "شنیدن، ابزار اصلی رهبر است.",
            "رشد پیروان، سنجه رهبری است.",
        ],
        "critiques": [
            "۱. آرمان‌گرایی: مدل، رهبری را بیش از اندازه اخلاقی و بی‌منفعت فرض می‌گیرد.\n۲. سنجش: رشد پیرو و خدمت، سخت اندازه‌گیری می‌شوند.\n۳. قدرت پنهان: خدمت می‌تواند پوششی برای نفوذ و کنترل نرم باشد.\n۴. شواهد: پیوند با عملکرد سازمانی یکدست نیست.\n۵. زمینه فرهنگی: معنای خدمت و قدرت در فرهنگ‌ها یکسان نیست.",
        ],
        "applications": [
            "مدیریت تحریریه: اولویت رشد حرفه‌ای خبرنگاران.",
            "رهبری رسانه عمومی: هم‌راستایی رهبری با مأموریت خدمت.",
            "توسعه رهبر: آموزش شنیدن، اقناع و پیش‌بینی.",
            "اخلاق حرفه‌ای: تحلیل مسئولیت رهبر در برابر منزلت.",
        ],
        "evolution": "گرین‌لیف در ۱۹۷۰ مقاله خدمتگزار در نقش رهبر را منتشر کرد و در ۱۹۷۷ آن را در کتابی درباره قدرت مشروع و بزرگی گسترد. بعدها اسپیرز ده ویژگی رهبر خدمتگزار را صورت‌بندی کرد و پژوهش تجربی، مدل را با اعتماد، رفتار شهروندی و عملکرد پیوند داد.",
        "key_concepts": [
            "رهبری خدمتگزار (Servant Leadership)",
            "خدمت نخست (Servant First)",
            "شنیدن (Listening)",
            "اقناع (Persuasion)",
            "پیش‌بینی (Foresight)",
            "رشد پیرو (Follower Growth)",
        ],
        "studies": [
            "Greenleaf, R. K. (1970). The servant as leader. Robert K. Greenleaf Center.",
            "Greenleaf, R. K. (1977). Servant leadership. Paulist Press.",
        ],
        "theorists": "رابرت گرین‌لیف",
        "theorists_text": "رابرت گرین‌لیف (۱۹۷۰؛ ۱۹۷۷)",
        "year": 1970,
        "model": "خدمت نخست → شنیدن و همدلی → اقناع و پیش‌بینی → رشد پیرو و جامعه‌سازی؛ معیار: آزادتر و خدمتگزارتر شدن پیروان.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nگرین‌لیف انگیزه رهبری را از قدرت به خدمت منتقل کرد و معیار موفقیت را از نتیجه به رشد پیرو برد. نوآوری چارچوب، وارونه کردن رابطه رهبر و پیرو است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با تحلیل روایت پیروان، شاخص رشد و بررسی رفتار خدمتگزارانه انجام می‌شود. پژوهشی که تنها رضایت پیرو را می‌سنجد، رشد بلندمدت را از دست می‌دهد؛ و پژوهشی که خدمت را با ضعف تصمیم یکی می‌گیرد، مفهوم را بد می‌خواند.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در رهبری تحریریه و رسانه عمومی است، اما باید با تحلیل ساختار تکمیل شود. خدمت بی پاسخ‌گویی، به وابستگی و فرسودگی می‌انجامد.",
        "critique_text": "\n".join([
            "۱. آرمان‌گرایی: رهبری بی‌منفعت فرض می‌شود.",
            "۲. سنجش: رشد پیرو و خدمت سخت اندازه‌گیری می‌شوند.",
            "۳. قدرت پنهان: خدمت پوشش کنترل نرم می‌شود.",
            "۴. شواهد: پیوند با عملکرد یکدست نیست.",
            "۵. فرهنگ: معنای خدمت و قدرت یکسان نیست.",
        ]),
        "example_text": "سردبیری در بحران، پیش از تصمیم جلسه شنیدن می‌گذارد و رشد دبیران جوان را به جای جلب اعتبار شخصی دنبال می‌کند؛ تیم در تصمیم شریک می‌شود و مرز مسئولیت انتشار همچنان روشن می‌ماند.",
    },
    "MC-635": {
        "summary": "(سالووی و مایر، ۱۹۹۰) هوش عاطفی، توانایی شناخت، تنظیم و به‌کارگیری هیجان در اندیشه و عمل است. سالووی و مایر چهار توانش را تفکیک کردند: ادراک هیجان، استفاده از هیجان برای تسهیل تفکر، فهم هیجان و مدیریت هیجان. مدل توانشی، هوش عاطفی را مهارت می‌داند نه ویژگی شخصیتی؛ مدل‌های آمیخته، آن را با انگیزش و شخصیت درمی‌آمیزند. گلمن در ۱۹۹۵ مفهوم را عمومی کرد و آن را با موفقیت شغلی گره زد. هوش عاطفی، مکمل هوش شناختی است نه جانشین آن. این مدل، بنیان پژوهش سنجش توانش هیجانی و آموزش همدلی حرفه‌ای شد.",
        "definition": "هوش عاطفی، مجموعه توانایی‌هایی است برای ادراک دقیق هیجان خود و دیگران، استفاده از هیجان در پردازش اطلاعات، فهم علل و مسیر هیجان و مدیریت آن در موقعیت.",
        "main_problem": "مسئله این است که چرا افراد با هوش شناختی بالا در روابط کاری شکست می‌خورند. پاسخ، توانش هیجانی جداگانه است. پرسش دوم، سنجش است: آیا هوش عاطفی سازه‌ای مستقل است یا ترکیبی از شخصیت و هوش.",
        "mechanism": "۱. ادراک هیجان: شناسایی هیجان در چهره، صدا و متن و تفکیک آن از هیجان‌های مشابه.\n۲. استفاده از هیجان: به‌کارگیری حال هیجانی برای هدایت توجه و تسهیل تفکر.\n۳. فهم هیجان: شناخت علل، مسیر و ترکیب هیجان‌ها.\n۴. مدیریت هیجان: تنظیم هیجان خود و اثرگذاری بر هیجان دیگران.\n۵. مدل توانشی: هوش عاطفی مهارتی آزمون‌پذیر است، نه صفتی خودگزارشی.\n۶. رشدپذیری: توانش هیجانی با آموزش و تجربه قابل تقویت است.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا خبرنگار در مصاحبه با داغ‌دیدگان باید هیجان را بفهمد بی آنکه در آن غرق شود، چرا مدیریت هیجان مخاطب در بحران بخشی از ارتباطات بحران است و چرا تحریریه پرتنش، خطای قضاوت را زیاد می‌کند. نکته مهم این است که هوش عاطفی ابزار دستکاری هیجان مخاطب نیست؛ مرز همدلی و مهندسی احساس، اخلاقی است.",
        "assumptions": [
            "هیجان، اطلاعاتی قابل پردازش است.",
            "هوش عاطفی مجموعه‌ای از توانایی‌هاست.",
            "توانش هیجانی با آموزش قابل تقویت است.",
        ],
        "principles": [
            "ادراک هیجان، پیش‌شرط مدیریت آن است.",
            "هیجان، تفکر را هدایت می‌کند.",
            "هوش عاطفی، جانشین هوش شناختی نیست.",
        ],
        "critiques": [
            "۱. سنجش: آزمون توانش، وابسته به فرهنگ و زبان است.\n۲. هم‌پوشانی: سازه با شخصیت و هوش شناختی همبستگی دارد.\n۳. خودگزارشی: مدل‌های آمیخته، نمره را متورم می‌کنند.\n۴. ادعای بیش از اندازه: پیوند با موفقیت شغلی بیش‌برآورد شده است.\n۵. قواعد نمایش: بیان هیجان در فرهنگ‌ها یکسان نیست.",
        ],
        "applications": [
            "آموزش خبرنگار: همدلی حرفه‌ای در مصاحبه حساس.",
            "ارتباطات بحران: مدیریت هیجان مخاطب و پیام آرام‌بخش.",
            "رهبری تحریریه: کاهش تنش و خطای قضاوت.",
            "سواد رسانه‌ای: شناخت تحریک هیجانی محتوا.",
        ],
        "evolution": "سالووی و مایر در ۱۹۹۰ چارچوب توانشی را عرضه کردند و در ۱۹۹۷ آن را به چهار شاخه گستردند. گلمن در ۱۹۹۵ مفهوم را عمومی کرد و مدل آمیخته را با رهبری و موفقیت گره زد. بعدها پژوهش سنجش، عصب‌شناسی هیجان و آموزش هوش عاطفی گسترش یافت.",
        "key_concepts": [
            "هوش عاطفی (Emotional Intelligence)",
            "ادراک هیجان (Emotion Perception)",
            "مدیریت هیجان (Emotion Regulation)",
            "مدل توانشی (Ability Model)",
            "همدلی (Empathy)",
            "مدل آمیخته (Mixed Model)",
        ],
        "studies": [
            "Salovey, P., & Mayer, J. D. (1990). Emotional intelligence. Imagination, Cognition and Personality, 9(3), 185-211.",
            "Mayer, J. D., & Salovey, P. (1997). What is emotional intelligence? In Emotional development and emotional intelligence. Basic Books.",
        ],
        "theorists": "پیتر سالووی؛ جان مایر",
        "theorists_text": "سالووی و مایر (۱۹۹۰؛ ۱۹۹۷)",
        "year": 1990,
        "model": "چهار شاخه: ادراک هیجان → استفاده از هیجان → فهم هیجان → مدیریت هیجان؛ توانشی، آزمون‌پذیر و رشدپذیر.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nسالووی و مایر هیجان را اطلاعاتی قابل پردازش دانستند و هوش عاطفی را از صفت به توانش منتقل کردند. نوآوری چارچوب، تفکیک چهار مهارت قابل آموزش است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با آزمون عملکردی توانش و پرسش‌نامه خودگزارشی انجام می‌شود. پژوهشی که تنها خودگزارشی را می‌سنجد، سوگیری را وارد نتیجه می‌کند؛ و پژوهشی که آزمون را بی فرهنگ‌سنجی به کار می‌برد، تفاوت قواعد نمایش را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در آموزش همدلی حرفه‌ای است، اما باید با اخلاق رسانه تکمیل شود. هوش عاطفی بی مرز اخلاقی، به دستکاری هیجان مخاطب بدل می‌شود.",
        "critique_text": "\n".join([
            "۱. سنجش: آزمون وابسته به فرهنگ و زبان است.",
            "۲. هم‌پوشانی: سازه با شخصیت و هوش همبسته است.",
            "۳. خودگزارشی: نمره متورم می‌شود.",
            "۴. ادعای بیش از اندازه: پیوند با موفقیت مبالغه شده است.",
            "۵. قواعد نمایش: بیان هیجان یکسان نیست.",
        ]),
        "example_text": "خبرنگاری در مصاحبه با خانواده داغ‌دیده، هیجان خود را می‌شناسد و آن را به سؤال هدایت‌کننده بدل نمی‌کند؛ همدلی می‌کند اما فاصله حرفه‌ای را حفظ می‌کند. این، کاربرد توانش هیجانی است نه سردی حرفه‌ای.",
    },
    "MC-636": {
        "summary": "(آمبلر و بارو، ۱۹۹۶) برند کارفرما، مجموعه مزایای کارکردی، اقتصادی و روان‌شناختی است که استخدام در یک سازمان عرضه می‌کند و با آن سازمان شناسایی می‌شود. آمبلر و بارو مدیریت برند را به مدیریت منابع انسانی آوردند و گفتند شهرت کارفرما بر جذب و نگهداشت اثر می‌گذارد. برند کارفرما از هویت سازمان، تجربه کارکنان و تصویر بیرونی ساخته می‌شود. وعده برند بی تجربه هم‌خوان، به بدبینی کارکنان می‌انجامد. در بازار استعداد، برند کارفرما ابزار رقابت است. این مفهوم، مدیریت منابع انسانی را از کار اداری به کار راهبردی منتقل کرد. برند کارفرما امروز در گفت‌وگوی عمومی کارکنان شکل می‌گیرد و از کنترل مستقیم سازمان خارج شده است. سازمان ناچار است درباره تجربه واقعی کار پاسخگو باشد.",
        "definition": "برند کارفرما، مجموعه مزایای کارکردی، اقتصادی و روان‌شناختی استخدام است که سازمان را به‌عنوان محل کار متمایز می‌کند و بر جذب، تعهد و نگهداشت کارکنان اثر می‌گذارد.",
        "main_problem": "مسئله این است که چرا سازمان‌ها با حقوق مشابه، جذب و نگهداشت متفاوت دارند. پاسخ، تصویر و وعده کارفرماست. پرسش دوم، شکاف وعده و تجربه است: برند بی صداقت چگونه اعتماد را از بین می‌برد.",
        "mechanism": "۱. مزایای کارکردی: رشد، آموزش و معنای کار.\n۲. مزایای اقتصادی: حقوق، مزایا و امنیت شغلی.\n۳. مزایای روان‌شناختی: تعلق، احترام و هویت سازمانی.\n۴. تصویر بیرونی: شهرت کارفرما در بازار کار و رسانه.\n۵. تجربه درونی: رفتار واقعی سازمان با کارکنان، منبع اصلی اعتبار.\n۶. هم‌خوانی: وعده برند باید با تجربه روزمره کارکنان یکی باشد.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا سازمان‌های رسانه‌ای برای جذب روزنامه‌نگار برجسته بر هویت حرفه‌ای خود تأکید می‌کنند، چرا بازخورد کارکنان در پلتفرم‌های ارزیابی، برند را می‌سازد یا می‌شکند و چرا اخراج ناگهانی، برند کارفرما را سال‌ها تخریب می‌کند. نکته مهم این است که برند کارفرما با تبلیغ ساخته نمی‌شود؛ با رفتار روزمره ساخته می‌شود و تبلیغ تنها آن را روایت می‌کند.",
        "assumptions": [
            "کارفرما می‌تواند مانند برند مدیریت شود.",
            "وعده ادراک‌شده بر جذب و ماندن اثر می‌گذارد.",
            "تجربه کارکنان، اعتبار برند را تعیین می‌کند.",
        ],
        "principles": [
            "برند کارفرما سه‌بعدی است.",
            "وعده بی تجربه، بدبینی می‌سازد.",
            "کارکنان، سفیران برندند.",
        ],
        "critiques": [
            "۱. سنجش: اثر برند بر عملکرد، سخت تفکیک‌پذیر است.\n۲. شکاف وعده و تجربه: برندسازی به تبلیغ بدل می‌شود.\n۳. تمرکز بر جذب: نگهداشت کم‌تر دیده می‌شود.\n۴. اخلاق بازاریابی کار: کار به کالای تبلیغاتی بدل می‌شود.\n۵. زمینه بازار کار: اثر برند به کمیابی مهارت وابسته است.",
        ],
        "applications": [
            "جذب خبرنگار: طراحی وعده ارزش و روایت هویت حرفه‌ای.",
            "رسانه عمومی: هم‌راستایی برند با مأموریت خدمت.",
            "نگهداشت استعداد: هم‌خوانی تجربه روزمره با وعده.",
            "ارتباطات داخلی: شنیدن بازخورد کارکنان و اصلاح برند.",
        ],
        "evolution": "آمبلر و بارو در ۱۹۹۶ مفهوم را در مجله مدیریت برند عرضه کردند؛ بک‌هاوس و تیکو در ۲۰۰۴ چارچوب جذب و نگهداشت را گستردند. بعدها پلتفرم‌های ارزیابی کارفرما و شبکه‌های اجتماعی، برند کارفرما را به گفت‌وگوی عمومی بدل کردند.",
        "key_concepts": [
            "برند کارفرما (Employer Brand)",
            "وعده ارزش کارمند (Employee Value Proposition)",
            "تصویر کارفرما (Employer Image)",
            "هویت کارفرما (Employer Identity)",
            "جذب استعداد (Talent Attraction)",
            "نگهداشت (Retention)",
        ],
        "studies": [
            "Ambler, T., & Barrow, S. (1996). The employer brand. Journal of Brand Management, 4(3), 185-206.",
            "Backhaus, K., & Tikoo, S. (2004). Conceptualizing and researching employer branding. Career Development International, 9(5), 501-517.",
        ],
        "theorists": "تیم آمبلر؛ سایمون بارو",
        "theorists_text": "آمبلر و بارو (۱۹۹۶)",
        "year": 1996,
        "model": "مزایای کارکردی + اقتصادی + روان‌شناختی → وعده برند کارفرما → تصویر بیرونی و تجربه درونی → جذب، تعهد و نگهداشت.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nآمبلر و بارو منطق برند را به رابطه استخدام بردند و کارفرما را صاحب هویتی قابل مدیریت کردند. نوآوری چارچوب، پیوند بازاریابی و منابع انسانی است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با تصویر برند، قصد درخواست شغل و نرخ ماندن انجام می‌شود. پژوهشی که تنها تبلیغ را می‌سنجد، تجربه کارکنان را از دست می‌دهد؛ و پژوهشی که برند را با حقوق یکی می‌گیرد، ابعاد روانی را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در جذب استعداد رسانه‌ای است، اما باید با اخلاق کار تکمیل شود. برند بی صداقت، انتظار بلندمدت می‌سازد و سرخوردگی می‌آفریند.",
        "critique_text": "\n".join([
            "۱. سنجش: اثر برند از عملکرد تفکیک نمی‌شود.",
            "۲. شکاف وعده و تجربه: برند به تبلیغ بدل می‌شود.",
            "۳. تمرکز بر جذب: نگهداشت کم دیده می‌شود.",
            "۴. اخلاق: کار به کالای تبلیغاتی بدل می‌شود.",
            "۵. بازار کار: اثر برند به کمیابی مهارت وابسته است.",
        ]),
        "example_text": "سازمان رسانه‌ای در آگهی استخدام آزادی تحریریه را برجسته می‌کند اما در عمل سانسور داخلی دارد؛ کارکنان تازه، وعده شکسته را در پلتفرم‌های ارزیابی عمومی می‌کنند و برند کارفرما آسیب می‌بیند.",
    },
    "MC-646": {
        "summary": "(گیبسون، ۱۹۷۹) نظریه امکانات می‌گوید محیط، فرصت‌های عمل را در خود دارد و موجود زنده آن‌ها را مستقیم ادراک می‌کند. امکان عمل، ویژگی رابطه میان محیط و توانایی موجود است، نه ویژگی ذهنی و نه عینی محض. گیبسون این را در برابر تفکیک سنتی محرک و پاسخ گذاشت. در مطالعات رسانه و فناوری، این مفهوم به امکان‌های عمل پلتفرم تعمیم یافت: چه کاری با یک ابزار ممکن، آسان یا دشوار است. نظریه، رابطه کاربر و فناوری را از جبر فناورانه و از ساخت‌گرایی محض جدا می‌کند.",
        "definition": "نظریه امکانات، چارچوبی است که محیط را مجموعه فرصت‌های عمل برای موجود می‌داند و ادراک را دریافت مستقیم همین فرصت‌ها، نه بازسازی ذهنی محرک‌های جدا.",
        "main_problem": "مسئله این است که ادراک چگونه معنادار است. پاسخ، محیط در نسبت با توانایی موجود، امکان عمل عرضه می‌کند. پرسش دوم، تعمیم به فناوری است: آیا امکان عمل ویژگی ابزار است یا محصول تفسیر کاربر.",
        "mechanism": "۱. امکان عمل: محیط برای موجود، فرصت و مانع عمل می‌سازد.\n۲. رابطه‌گرایی: امکان، در رابطه میان ویژگی محیط و توانایی موجود است، نه در یکی از آن دو.\n۳. ادراک مستقیم: امکان‌ها بی استنتاج پیچیده ادراک می‌شوند.\n۴. تغییر با توانایی: همان محیط برای کودک و بزرگسال امکانات متفاوت دارد.\n۵. طراحی: طراح با تغییر ویژگی، امکان عمل تازه می‌سازد یا مسدود می‌کند.\n۶. امکان‌های ارتباطی: ابزار، امکان دیده‌شدن، تکرار، جست‌وجو و پیوند را تغییر می‌دهد.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا دکمه پسندیدن، اشتراک‌گذاری و اعلان، رفتار مخاطب را شکل می‌دهند، چرا ناشناسی و ماندگاری محتوا امکان‌های متفاوت می‌سازند و چرا طراحی دسترس‌پذیر، امکان مشارکت را برای گروه‌های حاشیه‌ای باز می‌کند. پژوهش رسانه شبکه‌ای، امکان‌های پلتفرم را با ماندگاری، تکرارپذیری، مقیاس‌پذیری و قابلیت جست‌وجو تحلیل می‌کند. نکته مهم این است که امکان عمل، تقدیر نیست؛ کاربر می‌تواند امکان را بپذیرد، دور بزند یا بازتعریف کند.",
        "assumptions": [
            "محیط، فرصت‌های عمل عرضه می‌کند.",
            "امکان عمل، رابطه‌ای است نه ذهنی یا عینی محض.",
            "امکان‌ها مستقیم ادراک می‌شوند.",
        ],
        "principles": [
            "امکان، به توانایی موجود وابسته است.",
            "طراحی، امکان عمل می‌سازد یا مسدود می‌کند.",
            "امکان عمل، تقدیر نیست.",
        ],
        "critiques": [
            "۱. ابهام مفهومی: مرز امکان و تفسیر کاربر روشن نیست.\n۲. تعمیم: انتقال از ادراک بینایی به فناوری سهل‌انگارانه است.\n۳. خطر جبرگرایی: امکان‌ها می‌توانند تعیین‌کننده رفتار خوانده شوند.\n۴. سنجش: امکان عمل سخت عملیاتی و مقایسه می‌شود.\n۵. تورم مفهومی: اصطلاح برای هر ویژگی ابزار به کار می‌رود.",
        ],
        "applications": [
            "طراحی رابط: تحلیل امکان عمل پیش از طراحی.",
            "سواد پلتفرم: شناخت امکان‌ها و محدودیت‌های ابزار.",
            "دسترس‌پذیری: بازکردن امکان مشارکت برای گروه‌های حاشیه‌ای.",
            "سیاست طراحی: تحلیل طراحی فریبنده و امکان‌های مسدود.",
        ],
        "evolution": "گیبسون در ۱۹۷۹ نظریه امکانات را در رویکرد بوم‌شناختی به ادراک دیداری عرضه کرد. نورمن در ۱۹۸۸ آن را به طراحی تعاملی برد و هاچبی در ۲۰۰۱ به فناوری ارتباطی تعمیم داد. بعدها پژوهش رسانه شبکه‌ای، امکان‌های پلتفرم را به تحلیل رفتار کاربر گره زد.",
        "key_concepts": [
            "امکان عمل (Affordance)",
            "ادراک مستقیم (Direct Perception)",
            "رابطه موجود و محیط (Organism-Environment Relation)",
            "امکان‌های پلتفرم (Platform Affordances)",
            "طراحی تعاملی (Interaction Design)",
            "ماندگاری و قابلیت جست‌وجو (Persistence and Searchability)",
        ],
        "studies": [
            "Gibson, J. J. (1979). The ecological approach to visual perception. Houghton Mifflin.",
            "Hutchby, I. (2001). Technologies, texts and affordances. Sociology, 35(2), 441-456.",
        ],
        "theorists": "جیمز گیبسون؛ ایان هاچبی",
        "theorists_text": "گیبسون (۱۹۷۹)؛ هاچبی (۲۰۰۱)",
        "year": 1979,
        "model": "ویژگی محیط × توانایی موجود → امکان عمل → ادراک مستقیم → رفتار؛ طراحی، امکان‌ها را می‌سازد یا مسدود می‌کند.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nگیبسون ادراک را از پردازش محرک جدا کرد و محیط را معنادار و عمل‌پذیر دید. نوآوری چارچوب، تعریف امکان در رابطه موجود و محیط است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با مشاهده رفتار در محیط، تحلیل طراحی و آزمون کاربردپذیری انجام می‌شود. پژوهشی که تنها ویژگی فنی را می‌سنجد، تفسیر کاربر را از دست می‌دهد؛ و پژوهشی که هر رفتار را امکان ابزار می‌خواند، مفهوم را تورم می‌دهد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در تحلیل طراحی پلتفرم است، اما باید با تحلیل قدرت تکمیل شود. امکان بی انتخاب، به معماری اجبار نرم بدل می‌شود.",
        "critique_text": "\n".join([
            "۱. ابهام: مرز امکان و تفسیر روشن نیست.",
            "۲. تعمیم: انتقال از ادراک بینایی سهل‌انگارانه است.",
            "۳. جبرگرایی: امکان تعیین‌کننده رفتار خوانده می‌شود.",
            "۴. سنجش: عملیاتی‌سازی دشوار است.",
            "۵. تورم مفهومی: هر ویژگی ابزار امکان خوانده می‌شود.",
        ]),
        "example_text": "شبکه اجتماعی با دکمه پسندیدن، امکان واکنش سریع می‌سازد و با نبود دکمه ویرایش، امکان اصلاح را محدود می‌کند؛ کاربر عادت خود را با همین امکان‌ها تنظیم می‌کند، هرچند می‌تواند آن‌ها را دور بزند.",
    },
}

REQUIRED_SECTIONS = ["summary", "definition", "main_problem", "mechanism", "assumptions",
                     "principles", "critiques", "applications", "evolution", "key_concepts",
                     "theorists", "model", "studies"]
WORD_KEYS = ["summary", "definition", "main_problem", "mechanism", "critiques", "applications",
             "evolution", "key_concepts", "principles", "studies", "assumptions"]


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


NAME_FIX = {
    "MC-646": ("نظریه امکانات (آفوردنس)", "Affordance Theory",
               "canonical_name repaired: 'Affordances/Functions Theory' conflated affordances with functions; aligned to Gibson's affordance theory"),
}


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

        cur.execute("UPDATE kb_entities SET properties=%s, version=version+1, updated_at=%s WHERE id=%s",
                    (json.dumps(p, ensure_ascii=False), NOW, eid))
        cur.execute("SELECT version FROM kb_entities WHERE id=%s", (eid,))
        new_version = cur.fetchone()[0]

        for src in S[code]:
            sid = ensure_source(cur, src)
            cur.execute("SELECT id FROM kb_evidence WHERE about_code=%s AND source_id=%s LIMIT 1", (code, sid))
            if cur.fetchone():
                continue
            lt = {"work": "SECTION", "page_range": "PAGE", "CHAPTER": "CHAPTER"}.get(src["locator_type"], "SECTION")
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
                                       "verified": n_verified, "batch": 103}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH103 THEORY DONE")


if __name__ == "__main__":
    main()
