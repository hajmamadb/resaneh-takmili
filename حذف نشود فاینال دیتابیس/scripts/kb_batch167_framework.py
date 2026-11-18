# -*- coding: utf-8 -*-
"""Batch 167 (PERSON, critical/cultural tradition): th-19 Adorno, th-4 Habermas, th-5 Hall, th-17 Bourdieu."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch167-person-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch167_person.json"

S = {
    "th-19": [
        dict(kind="BOOK",
             title_en="Dialectic of Enlightenment: Philosophical Fragments",
             title_fa="دیالکتیک روشنگری: قطعه‌های فلسفی",
             authors="Horkheimer, M.; Adorno, T. W.", year=1947,
             publisher="Querido",
             doi=None,
             url="https://archive.org/details/dialecticofenlig0000hork_o6y4",
             language="en", isbn=None,
             citation="Horkheimer, M., & Adorno, T. W. (1947). Dialektik der Aufklärung: Philosophische Fragmente. Amsterdam: Querido. English ed.: New York: Herder and Herder, 1972.",
             locator="1947 edition; ch. 'The Culture Industry'", locator_type="CHAPTER",
             supports="culture industry thesis and critique of mass deception", verified=True),
        dict(kind="BOOK",
             title_en="The Culture Industry: Selected Essays on Mass Culture",
             title_fa="صنعت فرهنگ: مقاله‌های برگزیده دربارهٔ فرهنگ توده",
             authors="Adorno, T. W.; Bernstein, J. M. (Ed.)", year=1991,
             publisher="Routledge",
             doi=None,
             url="https://www.routledge.com/The-Culture-Industry-Selected-Essays-on-Mass-Culture/Bernstein-Adorno/p/book/9780415253802",
             language="en", isbn="9780415253802",
             citation="Adorno, T. W. (1991). The Culture Industry: Selected Essays on Mass Culture (J. M. Bernstein, Ed.). London: Routledge.",
             locator="1991 edition", locator_type="edition",
             supports="standardization, pseudo-individualization and regression of listening", verified=True),
    ],
    "th-4": [
        dict(kind="BOOK",
             title_en="The Structural Transformation of the Public Sphere: An Inquiry into a Category of Bourgeois Society",
             title_fa="دگرگونی ساختاری حوزهٔ عمومی: پژوهشی در باب مقوله‌ای از جامعهٔ بورژوایی",
             authors="Habermas, J.", year=1989,
             publisher="MIT Press",
             doi=None,
             url="https://mitpress.mit.edu/9780262081801/the-structural-transformation-of-the-public-sphere/",
             language="en", isbn="9780262081801",
             citation="Habermas, J. (1989). The Structural Transformation of the Public Sphere: An Inquiry into a Category of Bourgeois Society (T. Burger, Trans.). Cambridge, MA: MIT Press. (Original work published 1962)",
             locator="1989 English edition", locator_type="edition",
             supports="rise and decline of the bourgeois public sphere; refeudalization", verified=True),
        dict(kind="BOOK",
             title_en="The Theory of Communicative Action, Vol. 1: Reason and the Rationalization of Society",
             title_fa="نظریهٔ کنش ارتباطی، جلد نخست: عقلانیت و عقلانی‌شدن جامعه",
             authors="Habermas, J.", year=1984,
             publisher="Beacon Press",
             doi=None,
             url="https://books.google.com/books/about/The_Theory_of_Communicative_Action_Volum.html?hl=en&id=16ntg728ZdAC",
             language="en", isbn="9780807015070",
             citation="Habermas, J. (1984). The Theory of Communicative Action, Vol. 1: Reason and the Rationalization of Society (T. McCarthy, Trans.). Boston: Beacon Press.",
             locator="Vol. 1", locator_type="work",
             supports="communicative versus strategic action; lifeworld and system", verified=True),
    ],
    "th-5": [
        dict(kind="REPORT",
             title_en="Encoding and Decoding in the Television Discourse",
             title_fa="رمزگذاری و رمزگشایی در گفتمان تلویزیونی",
             authors="Hall, S.", year=1973,
             publisher="Centre for Contemporary Cultural Studies, University of Birmingham",
             doi=None,
             url="https://epapers.bham.ac.uk/2962/",
             language="en", isbn=None,
             citation="Hall, S. (1973). Encoding and Decoding in the Television Discourse (CCCS Stencilled Paper 7). Birmingham: Centre for Contemporary Cultural Studies, University of Birmingham.",
             locator="Stencilled Paper 7", locator_type="work",
             supports="encoding/decoding model and three reading positions", verified=True),
        dict(kind="BOOK",
             title_en="Representation: Cultural Representations and Signifying Practices",
             title_fa="بازنمایی: بازنمودهای فرهنگی و رویه‌های معناسازی",
             authors="Hall, S. (Ed.)", year=1997,
             publisher="Sage",
             doi=None,
             url="https://psycnet.apa.org/record/1997-36930-000",
             language="en", isbn=None,
             citation="Hall, S. (Ed.). (1997). Representation: Cultural Representations and Signifying Practices. London: Sage.",
             locator="1997 edition", locator_type="edition",
             supports="constructionist approach to representation and the work of representation", verified=True),
    ],
    "th-17": [
        dict(kind="BOOK",
             title_en="On Television",
             title_fa="دربارهٔ تلویزیون",
             authors="Bourdieu, P.", year=1996,
             publisher="Liber-Raisons d'agir",
             doi=None,
             url="https://monoskop.org/images/1/13/Bourdieu_Pierre_On_Television.pdf",
             language="en", isbn=None,
             citation="Bourdieu, P. (1996). Sur la télévision. Paris: Liber-Raisons d'agir. English ed.: On Television. New York: New Press, 1998.",
             locator="1996 edition", locator_type="edition",
             supports="journalistic field, invisible censorship and ratings pressure", verified=True),
        dict(kind="BOOK",
             title_en="The Field of Cultural Production: Essays on Art and Literature",
             title_fa="میدان تولید فرهنگی: مقاله‌هایی دربارهٔ هنر و ادبیات",
             authors="Bourdieu, P.; Johnson, R. (Ed.)", year=1993,
             publisher="Columbia University Press",
             doi=None,
             url="https://archive.org/details/fieldofculturalp00bour",
             language="en", isbn="9780231082877",
             citation="Bourdieu, P. (1993). The Field of Cultural Production: Essays on Art and Literature (R. Johnson, Ed.). New York: Columbia University Press.",
             locator="1993 edition", locator_type="edition",
             supports="field theory of cultural production and autonomy", verified=True),
    ],
}

ENRICH = {
    "th-19": dict(
        year=1947,
        summary="تئودور آدورنو (۱۹۰۳-۱۹۶۹) فیلسوف، موسیقی‌شناس و نظریه‌پرداز اجتماعی مکتب فرانکفورت است که با ماکس هورکهایمر در کتاب دیالکتیک روشنگری، مفهوم صنعت فرهنگ را در نقد فرهنگ توده صورت‌بندی کرد. او در مؤسسهٔ پژوهش اجتماعی فرانکفورت پرورش یافت، با روی کار آمدن نازیسم به بریتانیا و سپس آمریکا رفت و در پروژهٔ پژوهش رادیویی پرینستون با پل لازارسفلد همکاری کرد؛ همین تجربه، تقابل مشهور پژوهش انتقادی و پژوهش اداری را در پی آورد. آدورنو در فصل صنعت فرهنگ استدلال کرد که تولید انبوه محصولات فرهنگی، استانداردسازی و شبه‌فردیت می‌سازد: تفاوت‌های ظاهری، تنوعی کاذب است که مصرف‌کننده را به پذیرش نظم موجود عادت می‌دهد. او مفهوم تحلیل رفتن شنیدن را برای موسیقی مردمی به کار برد و گفت شنونده به مصرف‌کنندهٔ منفعل بدل می‌شود. نقدهای اصلی به او، نخبه‌گرایی، نگاه یک‌سویه به مخاطب، فقدان شاهد تجربی و نادیده گرفتن مقاومت و لذت مخاطب را برجسته می‌کنند؛ با این حال، مفهوم صنعت فرهنگ پایهٔ اقتصاد سیاسی ارتباطات و مطالعات فرهنگی شد.",
        definition="تئودور آدورنو نظریه‌پرداز مکتب فرانکفورت و صورت‌بند مفهوم صنعت فرهنگ است که تولید انبوه فرهنگ را ابزار بازتولید نظم اجتماعی می‌دانست.",
        main_problem="چرا فرهنگ توده‌ای در جامعهٔ سرمایه‌داری به کالایی استاندارد و ایدئولوژیک بدل می‌شود و این وضع چگونه آگاهی انتقادی را تضعیف می‌کند.",
        mechanism="صنعت فرهنگ با استانداردسازی تولید، شبه‌فردیت ظاهری و تکرار فرمول‌های موفق، نیاز مخاطب را به محصولی قابل پیش‌بینی شکل می‌دهد و او را به مصرف منفعل و پذیرش وضع موجود عادت می‌دهد.",
        assumptions=[
            "فرهنگ توده‌ای کالاست.",
            "سرمایه در تولید فرهنگ مداخله می‌کند.",
            "استانداردسازی ذوق را یکسان می‌کند.",
            "تفاوت ظاهری، تنوع کاذب است.",
            "مخاطب به مصرف منفعل گرایش دارد.",
            "آگاهی انتقادی آسیب‌پذیر است.",
        ],
        principles=[
            "تولید فرهنگی را در بافت سرمایه تحلیل کن.",
            "فرم و استاندارد را با هم ببین.",
            "شبه‌فردیت را واشکافی کن.",
            "از توصیف صرف به نقد ایدئولوژی برو.",
            "اقتصاد سیاسی فرهنگ را جدی بگیر.",
            "مقاومت مخاطب را نیز بررسی کن.",
        ],
        critiques=[
            "نخبه‌گرا و ضد فرهنگ عامه است.",
            "مخاطب را کاملاً منفعل می‌بیند.",
            "شاهد تجربی نظام‌مند ندارد.",
            "مقاومت و لذت مخاطب را نادیده می‌گیرد.",
            "به تنوع بازار فرهنگ کم بها می‌دهد.",
            "معیار زیبایی‌شناختی آن اروپامحور است.",
            "نقد آن به‌سختی آزمون‌پذیر است.",
            "به نقش رسانه‌های محلی کم توجه است.",
            "به نقش دولت در فرهنگ کم توجه است.",
        ],
        critique_text="منتقدان آدورنو می‌گویند نگاه او به فرهنگ عامه نخبه‌گرایانه و به مخاطب تحقیرآمیز است و شاهد تجربی کافی ندارد؛ با این حال، تحلیل او دربارهٔ کالایی‌شدن فرهنگ، چارچوب پایهٔ اقتصاد سیاسی رسانه شد.",
        applications=[
            "نقد صنعت موسیقی.",
            "تحلیل تلویزیون تجاری.",
            "پژوهش تبلیغات و مصرف.",
            "تحلیل تمرکز مالکیت رسانه.",
            "مطالعهٔ فرهنگ عامه‌پسند.",
            "نقد سرگرمی سیاسی.",
            "تحلیل استانداردسازی ذوق.",
            "پژوهش رسانه و ایدئولوژی.",
            "آموزش اقتصاد سیاسی ارتباطات.",
            "تحلیل بازتولید فرهنگی.",
            "تحلیل تولید موسیقی پاپ.",
            "نقد برنامه‌های سرگرمی رادیو.",
            "پژوهش کالایی‌شدن خبر.",
            "تحلیل قدرت برند در رسانه.",
            "مطالعهٔ استانداردسازی فیلم.",
            "نقد فرهنگ مصرف در تبلیغات.",
            "تحلیل بازتولید در آموزش رسانه.",
            "پژوهش سانسور بازار فرهنگی.",
        ],
        example_text="برنامه‌های سرگرمی تجاری با وجود تنوع ظاهری، ساختار و ریتم یکسانی دارند؛ آدورنو این شباهت را نشانهٔ استانداردسازی صنعت فرهنگ و شبه‌فردیت می‌دانست.",
        evolution="آدورنو و هورکهایمر قطعه‌های فلسفی را در سال ۱۹۴۴ نوشتند و در سال ۱۹۴۷ منتشر کردند؛ ترجمهٔ انگلیسی در سال ۱۹۷۲ منتشر شد و مجموعهٔ مقاله‌های صنعت فرهنگ در سال ۱۹۹۱ چارچوب را به مطالعات فرهنگی و اقتصاد سیاسی رسانه آورد.",
        key_concepts=["صنعت فرهنگ", "شبه‌فردیت", "استانداردسازی", "تحلیل رفتن شنیدن", "کالایی‌شدن", "پژوهش انتقادی"],
        theorists="ماکس هورکهایمر، هربرت مارکوزه و والتر بنیامین.",
        theorists_text="آدورنو در سنت نظریهٔ انتقادی مکتب فرانکفورت و در گفت‌وگو با بنیامین نوشت.",
        model="فرهنگ توده‌ای به‌عنوان صنعتی که با استانداردسازی، آگاهی انتقادی را تضعیف می‌کند.",
        studies=[
            "دیالکتیک روشنگری سال ۱۹۴۷.",
            "پژوهش رادیوی پرینستون.",
            "مقالهٔ موسیقی مردمی سال ۱۹۴۱.",
            "کتاب شخصیت اقتدارگرا سال ۱۹۵۰.",
            "مجموعهٔ صنعت فرهنگ سال ۱۹۹۱.",
            "پژوهش نقد فرهنگ توده.",
            "مطالعهٔ موسیقی جاز و صنعت فرهنگ.",
            "پژوهش تبلیغات و ذوق عمومی.",
        ],
    ),
    "th-4": dict(
        year=1962,
        summary="یورگن هابرماس (زادهٔ ۱۹۲۹) فیلسوف و نظریه‌پرداز اجتماعی آلمانی و وارث نسل دوم مکتب فرانکفورت است که با کتاب دگرگونی ساختاری حوزهٔ عمومی در سال ۱۹۶۲، مفهوم حوزهٔ عمومی را به کانون بحث ارتباطات و دموکراسی بدل کرد. او نشان داد که حوزهٔ عمومی بورژوایی در سدهٔ هجدهم در قهوه‌خانه‌ها، سالن‌ها و مطبوعات شکل گرفت و عرصهٔ بحث عقلانی و انتقادی شهروندان بود. با تجاری‌شدن رسانه و گسترش فرهنگ مصرف، این حوزه به عرصهٔ نمایش و مدیریت تبلیغاتی بدل شد؛ فرایندی که هابرماس آن را بازفئودالی‌شدن خواند. او در نظریهٔ کنش ارتباطی در سال ۱۹۸۱ میان کنش ارتباطی، که بر تفاهم آزاد استوار است، و کنش راهبردی، که ابزار دستیابی به هدف است، تمایز گذاشت و از وضعیت گفتار آرمانی سخن گفت. هابرماس در دههٔ ۱۹۹۰ نظریهٔ دموکراسی مشورتی را پیش برد و بر نقش رسانهٔ آزاد در شکل‌گیری ارادهٔ عمومی تأکید کرد. نقدهای اصلی به او، آرمانی‌سازی حوزهٔ عمومی بورژوایی، طرد زنان و طبقات فرودست از آن و کم‌توجهی به تنوع فرهنگی را برجسته می‌کنند.",
        definition="یورگن هابرماس نظریه‌پرداز حوزهٔ عمومی و کنش ارتباطی است که بحث عقلانی و آزاد شهروندان را شرط مشروعیت دموکراسی می‌دانست.",
        main_problem="حوزهٔ عمومی چگونه شکل گرفت، چرا با تجاری‌شدن رسانه به عرصهٔ نمایش بدل شد و چه شرایطی برای گفت‌وگوی آزاد و عقلانی لازم است.",
        mechanism="شهروندان در عرصهٔ عمومی با استدلال و بدون سلطهٔ مقام، دربارهٔ مسائل مشترک به تفاهم می‌رسند؛ تجاری‌شدن رسانه و روابط مشتری‌مدار این عرصه را به نمایش و مدیریت تبلیغاتی بدل می‌کند و کنش ارتباطی را به کنش راهبردی فرومی‌کاهد.",
        assumptions=[
            "شهروندان توان استدلال عمومی دارند.",
            "حوزهٔ عمومی مستقل از دولت و بازار است.",
            "رسانهٔ آزاد واسط بحث عمومی است.",
            "تفاهم بدون اجبار ممکن است.",
            "تجاری‌شدن، بحث را به نمایش بدل می‌کند.",
            "مشروعیت از گفت‌وگوی آزاد می‌آید.",
        ],
        principles=[
            "استدلال را از تبلیغ جدا کن.",
            "دسترسی برابر به حوزهٔ عمومی را بسنج.",
            "رسانه را در خدمت تفاهم ببین.",
            "بازفئودالی‌شدن را رصد کن.",
            "وضعیت گفتار آرمانی را معیار بگیر.",
            "به حاشیه‌رانده‌شدگان صدا بده.",
        ],
        critiques=[
            "حوزهٔ عمومی بورژوایی را آرمانی می‌کند.",
            "زنان و کارگران را از آن طرد می‌کند.",
            "به تنوع فرهنگی کم توجه است.",
            "مرز کنش ارتباطی و راهبردی مبهم است.",
            "به رسانهٔ سرگرمی کم بها می‌دهد.",
            "به ساختار مالکیت رسانه کم می‌پردازد.",
            "معیار گفتار آرمانی آزمون‌ناپذیر است.",
            "به زمینهٔ غیراروپایی کم توجه دارد.",
        ],
        critique_text="منتقدان هابرماس می‌گویند حوزهٔ عمومی او آرمانی و طردکننده است و رسانهٔ واقعی را کم می‌بیند؛ با این حال، چارچوب او زبان مشترک بحث دربارهٔ رسانه و دموکراسی در سراسر جهان شد.",
        applications=[
            "تحلیل حوزهٔ عمومی دیجیتال.",
            "پژوهش دموکراسی مشورتی.",
            "تحلیل رسانه و انتخابات.",
            "مطالعهٔ گفت‌وگوی آنلاین.",
            "نقد تبلیغات سیاسی.",
            "پژوهش سیاست‌گذاری رسانه.",
            "تحلیل رسانهٔ عمومی.",
            "مطالعهٔ اخلاق روزنامه‌نگاری.",
            "پژوهش افکار عمومی.",
            "تحلیل شکاف گفت‌وگو و مدیریت.",
            "تحلیل گفت‌وگوی عمومی شهری.",
            "مطالعهٔ رسانهٔ خدمت عمومی.",
            "پژوهش مشارکت سیاسی آنلاین.",
            "تحلیل اخلاق گفت‌وگو.",
        ],
        example_text="وقتی رسانه در انتخابات به نمایش نظرسنجی و تبلیغات شخصیتی بدل می‌شود و بحث دربارهٔ برنامه‌ها کنار می‌رود، هابرماس این وضع را بازفئودالی‌شدن حوزهٔ عمومی می‌نامد.",
        evolution="هابرماس در سال ۱۹۶۲ دگرگونی ساختاری را نوشت و در سال ۱۹۸۱ نظریهٔ کنش ارتباطی را بسط داد؛ ترجمهٔ انگلیسی در سال ۱۹۸۹ بحث حوزهٔ عمومی را به پژوهش ارتباطات آورد و در دههٔ ۱۹۹۰ به دموکراسی مشورتی گره خورد.",
        key_concepts=["حوزهٔ عمومی", "کنش ارتباطی", "بازفئودالی‌شدن", "وضعیت گفتار آرمانی", "دموکراسی مشورتی", "کنش راهبردی"],
        theorists="ماکس هورکهایمر، تئودور آدورنو و کارل اُتو آپل.",
        theorists_text="هابرماس وارث نسل دوم مکتب فرانکفورت و در گفت‌وگو با آپل بود.",
        model="حوزهٔ عمومی به‌عنوان عرصهٔ استدلال آزاد که با تجاری‌شدن رسانه به نمایش بدل می‌شود.",
        studies=[
            "کتاب سال ۱۹۶۲ در آلمان.",
            "ترجمهٔ انگلیسی سال ۱۹۸۹.",
            "نظریهٔ کنش ارتباطی سال ۱۹۸۱.",
            "مجموعهٔ اخلاق گفت‌وگو در دههٔ ۱۹۸۰.",
            "پژوهش حوزهٔ عمومی دیجیتال.",
            "مطالعهٔ دموکراسی مشورتی.",
            "مطالعهٔ کنش ارتباطی در سازمان.",
        ],
    ),
    "th-5": dict(
        year=1973,
        summary="استوارت هال (۱۹۳۲-۲۰۱۴) نظریه‌پرداز فرهنگی جامائیکایی-بریتانیایی و از بنیان‌گذاران مطالعات فرهنگی است که مدل رمزگذاری و رمزگشایی را در سال ۱۹۷۳ عرضه کرد. او در سال ۱۹۵۱ با بورس رودز به آکسفورد رفت و در سال ۱۹۶۴ به دانشگاه بیرمنگام پیوست و از سال ۱۹۶۸ تا ۱۹۷۹ مدیر مرکز مطالعات فرهنگی معاصر آن دانشگاه بود؛ مرکزی که به کانون نقد فرهنگی و رسانه‌ای بدل شد. هال گفت معنا در متن رسانه‌ای ثابت نیست: تولیدکننده پیام را رمزگذاری می‌کند و مخاطب آن را رمزگشایی می‌کند و سه موقعیت خوانش ممکن است: خوانش غالب، خوانش مذاکره‌شده و خوانش متضاد. او در کتاب پلیس‌کردن بحران در سال ۱۹۷۸ نشان داد چگونه رسانه با برچسب زدن و ترویج هراس اخلاقی، بحران اجتماعی می‌سازد. هال در بازنمایی در سال ۱۹۹۷ رویکرد برساخت‌گرا به معناسازی را نظام‌مند کرد و بر نقش قدرت و تفاوت در بازنمایی تأکید گذاشت. نقدهای اصلی به او، ابهام در سازوکار رمزگشایی، متن‌محوری و دشواری عملیاتی‌کردن مدل را برجسته می‌کنند.",
        definition="استوارت هال بنیان‌گذار مطالعات فرهنگی بریتانیا و صورت‌بند مدل رمزگذاری و رمزگشایی است که معنا را نتیجهٔ برهم‌کنش متن و مخاطب می‌داند.",
        main_problem="معنای پیام رسانه‌ای چگونه ساخته می‌شود و چرا مخاطبان با وجود پیام یکسان، قرائت‌های متفاوت و گاه متضاد دارند.",
        mechanism="تولیدکننده با رمزگان فرهنگی مشترک پیام را رمزگذاری می‌کند؛ مخاطب با رمزگان خود آن را رمزگشایی می‌کند و بسته به پیشینه، قرائت غالب، مذاکره‌شده یا متضاد پدید می‌آید.",
        assumptions=[
            "معنا در متن ثابت نیست.",
            "رمزگان فرهنگی مشترک نیستند.",
            "مخاطب فعال و مفسر است.",
            "قدرت در رمزگذاری اثر می‌گذارد.",
            "قرائت‌های رقیب ممکن‌اند.",
            "هراس اخلاقی برساختهٔ رسانه است.",
        ],
        principles=[
            "رمزگذاری را از رمزگشایی جدا کن.",
            "موضع مخاطب را بسنج.",
            "قرائت غالب را طبیعی‌شده مپندار.",
            "رمزگان فرهنگی را زمینه‌مند کن.",
            "بازنمایی را با قدرت پیوند بزن.",
            "هراس اخلاقی را تاریخی بررسی کن.",
        ],
        critiques=[
            "سازوکار رمزگشایی مبهم است.",
            "متن را بیش از اندازه کانونی می‌کند.",
            "عملیاتی‌کردن مدل دشوار است.",
            "به اقتصاد رسانه کم می‌پردازد.",
            "قرائت مخاطب را تجربی نمی‌سنجد.",
            "به زمینهٔ غیربریتانیایی کمتر توجه دارد.",
            "مفهوم رمزگان را سیال رها می‌کند.",
            "به رسانهٔ دیجیتال کم توجه است.",
            "به نقش اقتصاد رسانه کم توجه است.",
            "به قدرت مالکیت رسانه کمتر می‌پردازد.",
            "به زمینهٔ رسانهٔ جهانی کم توجه است.",
        ],
        critique_text="منتقدان هال می‌گویند مدل او مخاطب فعال را نشان داد اما سازوکار رمزگشایی و سنجش تجربی آن مبهم ماند؛ با این حال، چرخش او از اثر رسانه به معناسازی، بنیان مطالعات مخاطب شد.",
        applications=[
            "تحلیل مخاطب تلویزیون.",
            "پژوهش هراس اخلاقی.",
            "مطالعهٔ بازنمایی اقلیت‌ها.",
            "تحلیل خبر جرم.",
            "پژوهش فرهنگ عامه.",
            "مطالعهٔ مخاطب شبکه‌های اجتماعی.",
            "تحلیل تبلیغات کلیشه‌ای.",
            "آموزش سواد رسانه‌ای.",
            "پژوهش هواداران و بازآفرینی.",
            "تحلیل نژاد در رسانه.",
            "تحلیل مخاطب موسیقی عامه.",
            "پژوهش بازنمایی جنسیت.",
            "مطالعهٔ قرائت مخاطب خبر.",
            "تحلیل فرهنگ هواداری آنلاین.",
            "پژوهش کلیشهٔ نژادی در سریال.",
            "تحلیل گفتار رسانهٔ اقلیت.",
            "تحلیل متون تبلیغاتی تلویزیون.",
            "پژوهش مخاطب رادیو محلی.",
            "تحلیل قرائت مخاطب.",
        ],
        example_text="برنامه‌ای که به‌ظاهر نقد جرم است ممکن است با برچسب زدن به گروهی خاص، هراس اخلاقی بسازد؛ هال نشان می‌دهد قرائت مخاطب می‌تواند این رمزگذاری را بپذیرد یا به چالش بکشد.",
        evolution="هال در سال ۱۹۷۳ مدل رمزگذاری و رمزگشایی را در قالب مقالهٔ مرکز بیرمنگام نوشت و در سال ۱۹۸۰ در کتاب فرهنگ، رسانه، زبان بازچاپ شد؛ کتاب بازنمایی در سال ۱۹۹۷ رویکرد برساخت‌گرا را به آموزش مطالعات فرهنگی آورد.",
        key_concepts=["رمزگذاری", "رمزگشایی", "قرائت ترجیحی", "قرائت متضاد", "هراس اخلاقی", "بازنمایی"],
        theorists="ریچارد هگارت، ریموند ویلیامز و پل دوییس.",
        theorists_text="هال در سنت مطالعات فرهنگی بیرمنگام و در گفت‌وگو با ویلیامز کار کرد.",
        model="پیام رسانه‌ای به‌عنوان ساختار رمزگذاری‌شده‌ای که مخاطب آن را در سه موقعیت قرائت می‌کند.",
        studies=[
            "مقالهٔ سال ۱۹۷۳ دربارهٔ گفتمان تلویزیونی.",
            "کتاب پلیس‌کردن بحران سال ۱۹۷۸.",
            "کتاب فرهنگ، رسانه، زبان سال ۱۹۸۰.",
            "کتاب بازنمایی سال ۱۹۹۷.",
            "پژوهش هراس اخلاقی.",
            "مطالعهٔ مخاطب فرهنگی.",
            "مطالعهٔ قرائت مخاطب آگهی.",
            "پژوهش فرهنگ جوانان و موسیقی.",
            "تحلیل هراس اخلاقی در شبکه‌های اجتماعی.",
            "مطالعهٔ بازنمایی مهاجر در خبر.",
        ],
    ),
    "th-17": dict(
        year=1996,
        summary="پیر بوردیو (۱۹۳۰-۲۰۰۲) جامعه‌شناس فرانسوی و استاد کلژ دو فرانس است که نظریهٔ میدان، عادت‌واره و سرمایهٔ فرهنگی را برای فهم تولید و مصرف فرهنگ و خبر به کار برد. او در الجزایر پژوهش میدانی کرد و از آن تجربه، نقد جامعه‌شناسی تقویمی و توجه به سازوکار بازتولید نابرابری را ساخت. بوردیو در کتاب تمایز در سال ۱۹۷۹ نشان داد سلیقهٔ فرهنگی به سرمایهٔ نمادین و مرزبندی طبقاتی گره خورده است. در کتاب دربارهٔ تلویزیون در سال ۱۹۹۶ نقد تندی بر قلمرو روزنامه‌نگاری نوشت: فشار سنجش مخاطب، سرعت تولید و میدان مشترک با سیاست، نوعی سانسور نامرئی می‌سازد که دیدگاه‌های بدیل را حذف می‌کند. او مفهوم روشنفکر سریع را برای تحلیل اهل نظر تلویزیونی به کار برد و بر استقلال نسبی میدان دانشگاهی تأکید کرد. کتاب میدان تولید فرهنگی در سال ۱۹۹۳ چارچوب نظری او را برای تحلیل هنر و رسانه گرد آورد. نقدهای اصلی به او، جبرگرایی عادت‌واره، کم‌توجهی به تغییر اجتماعی، سبک دشوار و نگاه اندک به دریافت مخاطب را برجسته می‌کنند.",
        definition="پیر بوردیو جامعه‌شناس فرهنگ و رسانه است که با مفاهیم میدان، عادت‌واره و سرمایه، بازتولید نابرابری و سانسور نامرئی در روزنامه‌نگاری را تحلیل کرد.",
        main_problem="سلیقه و تولید فرهنگی چگونه نابرابری طبقاتی را بازتولید می‌کند و فشار میدان روزنامه‌نگاری چگونه دامنهٔ دیدگاه‌های ممکن را محدود می‌سازد.",
        mechanism="کنشگران در میدان‌ها با سرمایهٔ اقتصادی، فرهنگی، اجتماعی و نمادین رقابت می‌کنند؛ عادت‌وارهٔ درونی‌شده، سلیقه و عمل را هدایت می‌کند و فشار سنجش مخاطب، معیارهای میدان روزنامه‌نگاری را به همهٔ میدان‌ها تحمیل می‌کند.",
        assumptions=[
            "فرهنگ عرصهٔ رقابت است.",
            "سرمایهٔ فرهنگی نابرابری می‌سازد.",
            "عادت‌واره عمل را هدایت می‌کند.",
            "میدان‌ها استقلال نسبی دارند.",
            "سنجش مخاطب فشار ساختاری است.",
            "سانسور می‌تواند نامرئی باشد.",
        ],
        principles=[
            "میدان را با سرمایه‌هایش تحلیل کن.",
            "سلیقه را طبقاتی بخوان.",
            "فشار ساختاری را از نیت فرد جدا کن.",
            "استقلال نسبی میدان را بسنج.",
            "روشنفکر سریع را واشکافی کن.",
            "بازتولید را با داده پیوند بزن.",
        ],
        critiques=[
            "جبرگرایی عادت‌واره دارد.",
            "به تغییر اجتماعی کم بها می‌دهد.",
            "نگاهش به دریافت مخاطب اندک است.",
            "سبک او دشوار و نخبه‌گراست.",
            "به رسانهٔ دیجیتال کم توجه است.",
            "به نقش اقتصاد رسانه کم توجه است.",
            "به قدرت مالکیت رسانه کمتر می‌پردازد.",
            "به زمینهٔ رسانهٔ جهانی کم توجه است.",
            "به عاملیت فرد کمتر می‌پردازد.",
            "نقد تلویزیون را شخصی می‌سازد.",
            "تعمیم آن به جوامع دیگر محدود است.",
            "به مقاومت مخاطب کم توجه است.",
            "به تغییر میدان در بحران کم می‌پردازد.",
            "تحلیل تجربی میدان را دشوار می‌کند.",
        ],
        critique_text="منتقدان بوردیو می‌گویند نظریهٔ او بیش از اندازه بازتولیدگرا و جبرگراست و عاملیت و تغییر را کم می‌بیند؛ با این حال، تحلیل او از میدان روزنامه‌نگاری و سانسور نامرئی یکی از دقیق‌ترین نقدهای ساختاری رسانه است.",
        applications=[
            "تحلیل سلیقهٔ رسانه‌ای.",
            "پژوهش سرمایهٔ فرهنگی.",
            "نقد میدان روزنامه‌نگاری.",
            "مطالعهٔ سانسور نامرئی.",
            "تحلیل نابرابری آموزشی.",
            "پژوهش مصرف فرهنگی.",
            "نقد گفت‌وگوی تلویزیونی.",
            "تحلیل مرزهای طبقاتی.",
            "مطالعهٔ روشنفکر رسانه‌ای.",
            "پژوهش استقلال تحریریه.",
            "تحلیل سلیقهٔ موسیقی طبقاتی.",
            "پژوهش مصرف رسانهٔ خبری.",
            "مطالعهٔ سرمایهٔ نمادین خبرنگار.",
            "تحلیل میدان آموزش روزنامه‌نگاری.",
            "پژوهش سلسله‌مراتب خبری.",
            "تحلیل میدان نشر کتاب.",
        ],
        example_text="وقتی برنامهٔ گفت‌وگویی فقط چهره‌های شناخته‌شده را دعوت می‌کند و بحث را به رقابت سریع پاسخ‌ها فرومی‌کاهد، بوردیو این را سانسور نامرئی میدان روزنامه‌نگاری می‌نامد.",
        evolution="بوردیو در دههٔ ۱۹۶۰ نظریهٔ بازتولید را ساخت و در سال ۱۹۷۹ تمایز را منتشر کرد؛ میدان تولید فرهنگی در سال ۱۹۹۳ و دربارهٔ تلویزیون در سال ۱۹۹۶ نقد رسانه را به چارچوب میدان افزودند.",
        key_concepts=["میدان", "عادت‌واره", "سرمایهٔ فرهنگی", "سرمایهٔ نمادین", "سانسور نامرئی", "روشنفکر سریع"],
        theorists="امیل دورکیم، ماکس وبر و اروینگ گافمن.",
        theorists_text="بوردیو در سنت جامعه‌شناسی دورکیم و وبر و در گفت‌وگو با ساختارگرایی شکل گرفت.",
        model="میدان روزنامه‌نگاری به‌عنوان فضایی که فشار مخاطب و میدان سیاسی، دامنهٔ دیدگاه را محدود می‌کند.",
        studies=[
            "کتاب تمایز سال ۱۹۷۹.",
            "میدان تولید فرهنگی سال ۱۹۹۳.",
            "کتاب دربارهٔ تلویزیون سال ۱۹۹۶.",
            "پژوهش الجزایر در دههٔ ۱۹۶۰.",
            "مطالعهٔ بازتولید آموزشی.",
            "نقد روشنفکر رسانه‌ای.",
            "مطالعهٔ مصرف فرهنگی طبقات.",
            "پژوهش خبر و سلسله‌مراتب منابع.",
            "تحلیل میدان دانشگاهی و رسانه.",
            "مطالعهٔ سانسور در تلویزیون.",
        ],
    ),
}

NAME_FIX = {}
YEAR_FIX = {
    "th-19": "year field denotes Dialectic of Enlightenment (1947); life dates 1903-1969 stated in summary",
    "th-4": "year corrected: card year 1929 was the birth year; landmark work is Strukturwandel der Öffentlichkeit (1962), English 1989",
    "th-5": "year field denotes Encoding and Decoding (1973); life dates 1932-2014 stated in summary",
    "th-17": "year field denotes Sur la télévision (1996); life dates 1930-2002 stated in summary",
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
                                       "verified": n_verified, "batch": 167}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH167 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
