# -*- coding: utf-8 -*-
"""Batch 79: full documentation for MC-414, MC-416, MC-417, MC-418."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch79-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch79_theory.json"

S = {
    "MC-414": [
        dict(kind="BOOK",
             title_en="The Ecological Approach to Visual Perception",
             title_fa="رویکرد بوم‌شناختی به ادراک دیداری",
             authors="Gibson, J. J.", year=1979, publisher="Houghton Mifflin",
             doi=None, url="https://monoskop.org/images/c/c6/Gibson_James_J_1977_1979_The_Theory_of_Affordances.pdf",
             language="en", isbn=None,
             citation="Gibson, J. J. (1979). The ecological approach to visual perception. Houghton Mifflin.",
             locator="chapter 8", locator_type="CHAPTER",
             supports="affordance / direct perception", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Technologies, Texts and Affordances",
             title_fa="فناوری‌ها، متن‌ها و امکان‌پذیری‌ها",
             authors="Hutchby, I.", year=2001, publisher="SAGE Publications",
             doi=None, url=None, language="en", isbn=None,
             citation="Hutchby, I. (2001). Technologies, texts and affordances. Sociology, 35(2), 441-456.",
             locator="pp. 441-456", locator_type="page_range",
             supports="affordances of technology / anti-determinism", verified=False),
    ],
    "MC-416": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Californian Ideology",
             title_fa="ایدئولوژی کالیفرنیایی",
             authors="Barbrook, R.; Cameron, A.", year=1996, publisher="Taylor & Francis",
             doi="10.1080/09505439609526455",
             url="https://monoskop.org/images/d/dc/Barbrook_Richard_Cameron_Andy_1996_The_Californian_Ideology.pdf",
             language="en", isbn=None,
             citation="Barbrook, R., & Cameron, A. (1996). The Californian ideology. Science as Culture, 6(1), 44-72.",
             locator="pp. 44-72", locator_type="page_range",
             supports="hybrid of counterculture and neoliberalism", verified=True),
        dict(kind="BOOK",
             title_en="From Counterculture to Cyberculture: Stewart Brand, the Whole Earth Network, and the Rise of Digital Utopianism",
             title_fa="از ضدculture تا سایبرculture",
             authors="Turner, F.", year=2006, publisher="University of Chicago Press",
             doi=None, url=None, language="en", isbn=None,
             citation="Turner, F. (2006). From counterculture to cyberculture: Stewart Brand, the Whole Earth Network, and the rise of digital utopianism. University of Chicago Press.",
             locator="work", locator_type="work",
             supports="historical genealogy of digital utopianism", verified=False),
    ],
    "MC-417": [
        dict(kind="REPORT",
             title_en="Information Management: A Proposal",
             title_fa="مدیریت اطلاعات: یک پیشنهاد",
             authors="Berners-Lee, T.", year=1989, publisher="CERN",
             doi=None, url="https://cds.cern.ch/record/369245/files/dd-89-001.pdf",
             language="en", isbn=None,
             citation="Berners-Lee, T. (1989). Information management: A proposal. CERN.",
             locator="document", locator_type="work",
             supports="web architecture / decentralization / hypertext", verified=True),
        dict(kind="BOOK",
             title_en="Weaving the Web: The Original Design and Ultimate Destiny of the World Wide Web",
             title_fa="بافتن وب: طراحی اولیه و سرنوشت نهایی وب جهانی",
             authors="Berners-Lee, T.; Fischetti, M.", year=1999, publisher="HarperCollins",
             doi=None, url=None, language="en", isbn=None,
             citation="Berners-Lee, T., & Fischetti, M. (1999). Weaving the web: The original design and ultimate destiny of the World Wide Web. HarperCollins.",
             locator="work", locator_type="work",
             supports="open web principles / later reflections", verified=False),
    ],
    "MC-418": [
        dict(kind="BOOK",
             title_en="Collective Intelligence: Mankind's Emerging World in Cyberspace",
             title_fa="هوش جمعی: جهان نوپای بشر در فضای سایبر",
             authors="Levy, P.", year=1997, publisher="Plenum Trade",
             doi=None, url="https://archive.org/details/collectiveintell0000levy",
             language="en", isbn=None,
             citation="Levy, P. (1997). Collective intelligence: Mankind's emerging world in cyberspace. Plenum Trade.",
             locator="work", locator_type="work",
             supports="collective intelligence / knowledge space", verified=True),
        dict(kind="BOOK",
             title_en="Convergence Culture: Where Old and New Media Collide",
             title_fa="فرهنگ همگرایی: برخورد رسانه‌های قدیم و جدید",
             authors="Jenkins, H.", year=2006, publisher="New York University Press",
             doi=None, url=None, language="en", isbn=None,
             citation="Jenkins, H. (2006). Convergence culture: Where old and new media collide. New York University Press.",
             locator="work", locator_type="work",
             supports="participatory culture / collective intelligence", verified=False),
    ],
}

ENRICH = {
    "MC-414": {
        "summary": "(گیبسون، ۱۹۷۹؛ نورمن؛ هاچبی، ۲۰۰۱) نظریه امکان‌پذیری‌ها می‌گوید محیط، «امکان‌های عمل» را در برابر موجود فراهم می‌کند و این امکان‌ها به‌طور مستقیم ادراک می‌شوند. نورمن مفهوم را به طراحی رابط آورد و میان امکان واقعی و امکان ادراک‌شده تمایز گذاشت. هاچبی آن را به فناوری گستراند: فناوری کنش را ممکن و محدود می‌کند، اما تعیین نمی‌کند؛ عاملیت کاربر درون همین محدوده عمل می‌کند.",
        "definition": "امکان‌پذیری، ویژگی رابطه‌ای میان یک شیء یا محیط و یک کنشگر است که مشخص می‌کند چه اعمالی با آن ممکن، آسان یا دشوارند. در رسانه دیجیتال، امکان‌پذیری به قابلیت‌های رابط (دکمه اشتراک، اسکرول بی‌پایان، حذف خودکار) اشاره دارد که رفتار کاربر را شکل می‌دهند، بی‌آنکه آن را جبراً تعیین کنند.",
        "main_problem": "مسئله این است که چگونه می‌توان نقش شکل‌دهنده فناوری در رفتار را توضیح داد، بدون افتادن در جبرگرایی فناورانه یا نادیده‌گرفتن قدرت طراحی. مفهوم امکان‌پذیری پاسخ می‌دهد که فناوری امکان می‌سازد و کاربر انتخاب می‌کند.",
        "mechanism": "\n".join([
            "۱. تعریف بوم‌شناختی: امکان‌پذیری نه خصیصه شیء و نه حالت ذهن، بلکه رابطه محیط و موجود است؛ صندلی برای انسان «نشستن» و برای کودک «بالا رفتن» فراهم می‌کند.",
            "۲. ادراک مستقیم: گیبسون استدلال کرد امکان‌ها بدون استنتاج پیچیده ادراک می‌شوند؛ ما در عمل می‌بینیم که چه کاری ممکن است.",
            "۳. تفکیک نورمن: امکان واقعی با امکان ادراک‌شده یکی نیست؛ طراحی بد می‌تواند امکان را پنهان کند و «سیگنیفایر» باید آن را نشان دهد.",
            "۴. امکان‌پذیری فناوری: هاچبی نشان داد فناوری هم امکان می‌دهد و هم محدود می‌کند؛ اثر آن مشروط به بستر و تفسیر کاربر است.",
            "۵. امکان‌های ارتباطی: در رسانه‌های اجتماعی، دیده‌شدن، ماندگاری، ویرایش‌پذیری و پیوندپذیری، شکل تازه‌ای از امکان‌پذیری‌اند که عمل ارتباطی را قالب‌بندی می‌کنند.",
            "۶. عاملیت درون محدوده: کاربران می‌توانند امکان‌ها را بازتفسیر یا دور بزنند (استفاده تازه، مقاومت، ترک پلتفرم)؛ همین، مرز میان امکان و جبر است.",
            "در بستر رسانه، طراحی پلتفرم را می‌توان به‌عنوان مجموعه‌ای از امکان‌ها خواند: دکمه بازنشر، امکان حذف پیام، نمایش شمارنده لایک و پخش خودکار، هر یک رفتار خاصی را آسان‌تر می‌کند. اما هیچ‌کدام رفتار را جبری نمی‌کنند؛ کاربران می‌توانند بی‌صدا تماشا کنند، حساب خصوصی بسازند یا پلتفرم را ترک کنند. تحلیل امکان‌پذیری به پژوهشگر کمک می‌کند اثر طراحی را جدی بگیرد، بی‌آنکه کاربر را منفعل فرض کند یا مسئولیت طراحی را از میان بردارد.",
        ]),
        "assumptions": [
            "امکان‌های عمل در رابطه شیء و کنشگر تعریف می‌شوند.",
            "امکان‌پذیری‌ها تا حد زیادی به‌طور مستقیم ادراک می‌شوند.",
            "فناوری کنش را ممکن و محدود می‌کند، اما جبراً تعیین نمی‌کند.",
        ],
        "principles": [
            "اثر طراحی را در آسان یا دشوار کردن اعمال جست‌وجو کنید.",
            "تفاوت امکان واقعی و امکان ادراک‌شده را جدی بگیرید.",
            "عاملیت کاربر را درون محدوده امکان‌ها تحلیل کنید.",
        ],
        "critiques": [
            "کشش مفهومی: «امکان‌پذیری» به همه چیز از دکمه تا فرهنگ تعمیم یافته و مرز تحلیلی خود را از دست داده است.",
            "ابهام هستی‌شناختی: اینکه امکان‌پذیری خصیصه شیء است یا رابطه، هنوز محل مناقشه است و سنجش آن را دشوار می‌کند.",
            "جبرگرایی نرم: تحلیل امکان‌ها می‌تواند ناخواسته به این بینجامد که رفتار کاربر را پیامد طراحی بداند.",
            "کم‌توجهی به قدرت: نیت طراح، مدل کسب‌وکار و نابرابری دسترسی در بسیاری از کاربردها غایب است.",
            "سنجش تجربی: دشوار است نشان دهیم یک امکان مشخص، رفتار را تغییر داده و نه عوامل دیگر.",
        ],
        "applications": [
            "تحلیل رابط کاربری و اثر طراحی بر رفتار.",
            "پژوهش درباره شیوه‌های ارتباطی در شبکه‌های اجتماعی.",
            "طراحی اخلاقی و ارزیابی پیامدهای قابلیت‌های تازه.",
            "آموزش سواد دیجیتال با تمرکز بر انتخاب‌های طراحی.",
        ],
        "evolution": "گیبسون مفهوم را در روان‌شناسی بوم‌شناختی (۱۹۷۹) طرح کرد. نورمن آن را در طراحی انسان‌محور (۱۹۸۸) به کار برد. هاچبی (۲۰۰۱) وارد مطالعات فناوری کرد و پژوهش رسانه‌های اجتماعی، امکان‌های ارتباطی چون دیده‌شدن و ماندگاری را بسط داد. امروز مفهوم در طراحی هوش مصنوعی و اخلاق طراحی نیز به کار می‌رود.",
        "key_concepts": [
            "امکان‌پذیری (affordance)",
            "امکان ادراک‌شده (perceived affordance)",
            "سیگنیفایر (signifier)",
            "امکان‌های ارتباطی (communicative affordances)",
            "عاملیت (agency)",
            "بازتفسیر کاربر (user reappropriation)",
        ],
        "studies": [
            "Gibson, J. J. (1979). The ecological approach to visual perception. Houghton Mifflin.",
            "Hutchby, I. (2001). Technologies, texts and affordances. Sociology, 35(2), 441-456.",
        ],
        "theorists": "جیمز جی. گیبسون، دانالد نورمن و ایان هاچبی (James J. Gibson, Donald A. Norman & Ian Hutchby)",
        "model": "رابطه سه‌گانه: طراحی (امکان واقعی) ← ادراک (امکان ادراک‌شده و سیگنیفایر) ← کنش کاربر (پذیرش، بازتفسیر یا دورزدن)؛ با عاملیت مشروط به بستر.",
        "detailed_analysis": "\n\n".join([
            "۱. بنیان و منطق نظری\nگیبسون با رد تفکیک ذهن و محیط، ادراک را فعالیتی بوم‌شناختی دید: موجود، امکان‌های عمل را در محیط می‌بیند. نورمن این بینش را به طراحی منتقل کرد و نشان داد که رابط خوب، امکان را قابل ادراک می‌کند. هاچبی سپس پرسید آیا فناوری می‌تواند «متن» باشد؛ پاسخ او این بود که فناوری امکان‌هایی دارد که کنش را قالب می‌دهند، اما تفسیر و بستر، اثر را تعیین می‌کنند.",
            "۲. سازوکار عملی و تشخیصی\nبرای تحلیل یک قابلیت، سه پرسش مطرح می‌شود: چه اعمالی را آسان می‌کند؟ چه اعمالی را دشوار یا ناممکن می‌سازد؟ و کاربران چه استفاده‌های ناخواسته‌ای از آن می‌کنند؟ پاسخ این پرسش‌ها، اثر طراحی را از جبر جدا می‌کند.",
            "۳. دلالت‌ها برای پژوهش رسانه\nپژوهش معاصر امکان‌های ارتباطی را با سنجه‌های رفتاری ترکیب می‌کند. پرسش باز: آیا در محیط‌هایی که الگوریتم خود امکان‌ها را شخصی‌سازی می‌کند، «امکان‌پذیری» هنوز واحد تحلیلی ثابتی است یا باید از امکان‌های پویا سخن گفت؟",
        ]),
        "critique_text": "\n".join([
            "۱. کشش مفهومی: «امکان‌پذیری» به همه چیز از دکمه تا فرهنگ تعمیم یافته و مرز تحلیلی خود را از دست داده است.",
            "۲. ابهام هستی‌شناختی: اینکه امکان‌پذیری خصیصه شیء است یا رابطه، هنوز محل مناقشه است و سنجش آن را دشوار می‌کند.",
            "۳. جبرگرایی نرم: تحلیل امکان‌ها می‌تواند ناخواسته به این بینجامد که رفتار کاربر را پیامد طراحی بداند.",
            "۴. کم‌توجهی به قدرت: نیت طراح، مدل کسب‌وکار و نابرابری دسترسی در بسیاری از کاربردها غایب است.",
            "۵. سنجش تجربی: دشوار است نشان دهیم یک امکان مشخص، رفتار را تغییر داده و نه عوامل دیگر.",
        ]),
        "example_text": "دکمه «بازنشر» یک امکان‌پذیری است: انتشار را به یک کلیک کاهش می‌دهد و همین، گسترش محتوا را آسان می‌کند. اما کاربر می‌تواند همان محتوا را بی‌نام بازنشر کند یا اصلاً بازنشر نکند. در مقابل، پلتفرمی که امکان ویرایش پیام را حذف می‌کند، خطا را پرهزینه می‌سازد. این دو نمونه نشان می‌دهد طراحی، میدان عمل را تغییر می‌دهد، نه انتخاب را حذف می‌کند.",
    },
    "MC-416": {
        "summary": "(باربروک و کامرون، ۱۹۹۶) ایدئولوژی کالیفرنیایی به ترکیب پارادوکسیکال آرمان‌گرایی ضدفرهنگی دهه شصت و ایمان نئولیبرالی به بازار آزاد و فناوری اشاره دارد. این ایدئولوژی، آزادی فردی را با رهایی فناورانه و بازار بی‌قاعده پیوند می‌زند و دولت را مانع نوآوری می‌بیند. باربروک و کامرون آن را ایدئولوژی «طبقه مجازی» دره سیلیکون دانستند که نابرابری، کار و سیاست را از میدان تحلیل حذف می‌کند.",
        "definition": "ایدئولوژی کالیفرنیایی، آمیزه‌ای از لیبرتاریانیسم فناورانه، فردگرایی ضدفرهنگی و بازارگرایی است که اینترنت را نیرویی خودبه‌خود رهایی‌بخش می‌داند. قدرت تحلیلی مفهوم در نشان‌دادن این است که یک موضع سیاسی خاص، خود را «طبیعی» و «فناورانه» معرفی می‌کند.",
        "main_problem": "مسئله این است که چرا گفتمان دره سیلیکون، بازار آزاد و آزادی فردی را هم‌راستا و اجتناب‌ناپذیر معرفی می‌کند، در حالی که این دو در سنت‌های سیاسی رقیب‌اند. مقاله این ترکیب را نه فلسفه منسجم، بلکه ایدئولوژی می‌بیند.",
        "mechanism": "\n".join([
            "۱. آمیزش دو سنت: رادیکالیسم فرهنگی هیپی‌های دهه شصت و بازارگرایی محافظه‌کاران دهه هشتاد در یک روایت واحد از آزادی فناورانه ادغام می‌شوند.",
            "۲. طبقه مجازی: گروهی از کارآفرینان، روزنامه‌نگاران فناوری و مشاوران که این ایدئولوژی را تولید و توزیع می‌کنند.",
            "۳. جبر فناورانه به‌مثابه ایدئولوژی: اینترنت نیرویی خودمختار فرض می‌شود که دولت و سیاست را بی‌اثر می‌کند.",
            "۴. حاملان رسانه‌ای: مجلات و گفتمان فناوری دهه نود، ایده «آزادی از دولت» را به زبان مصرف‌کننده ترجمه کردند.",
            "۵. حذف‌ها: کار، جنسیت، نژاد، نابرابری طبقاتی و نقش دولت در ساخت اینترنت از روایت حذف می‌شوند.",
            "۶. پیامد سیاسی: مقررات‌زدایی، خصوصی‌سازی و مقاومت در برابر حقوق کار، به‌عنوان «ضرورت فناورانه» توجیه می‌شود.",
            "در بستر رسانه، ایدئولوژی کالیفرنیایی در شعارهای پلتفرم‌ها بازتولید می‌شود: «فقط وصل شو»، «دنیا را تغییر بده» و «دولت مانع است». موج‌های بعدی مانند رمزارز و وب۳ نیز اغلب همین ساختار را تکرار می‌کنند: وعده رهایی از واسطه، همراه با تمرکز ثروت و قدرت در لایه زیرساخت. تحلیل باربروک و کامرون کمک می‌کند بپرسیم چه کسی از «آزادی» سود می‌برد و چه کسی هزینه آن را می‌پردازد.",
        ]),
        "assumptions": [
            "گفتمان دره سیلیکون، ایدئولوژی است و نه توصیف بی‌طرف فناوری.",
            "ضدفرهنگ دهه شصت و نئولیبرالیسم دهه هشتاد در یک روایت ادغام شده‌اند.",
            "این ایدئولوژی، نابرابری و روابط کار را از میدان دید حذف می‌کند.",
        ],
        "principles": [
            "ادعای «طبیعی‌بودن» فناوری را به‌عنوان موضع سیاسی بررسی کنید.",
            "به حذف‌ها و سکوت‌های روایت فناورانه توجه کنید.",
            "منافع طبقه مجازی را در تولید گفتمان فناوری ببینید.",
        ],
        "critiques": [
            "تعمیم بیش از حد: دره سیلیکون مجموعه‌ای متنوع از بازیگران است و یکسان‌سازی آن، تفاوت‌های سیاسی را پنهان می‌کند.",
            "نگاه بیرونی: نویسندگان اروپایی، گفتمان آمریکایی را از فاصله تحلیل کرده‌اند و ممکن است تفاوت‌های محلی را کم‌ببینند.",
            "قاب زمانی: مقاله snapshot دهه نود است و تحول پلتفرم‌های بزرگ، سرمایه‌گذاری دولتی و اقتصاد داده را در بر نمی‌گیرد.",
            "نادیده‌گرفتن نقش دولت: خود اینترنت محصول سرمایه‌گذاری دولتی و پژوهشی است و روایت «ضددولت» ناقص است.",
            "ابهام مفهومی: «ایدئولوژی» گاه به‌معنای جهان‌بینی و گاه به‌معنای فریب به کار رفته و تحلیل را تیز نمی‌کند.",
        ],
        "applications": [
            "نقد گفتمان فناوری و روایت‌های رهایی‌بخش.",
            "تحلیل اقتصاد سیاسی پلتفرم و رمزارز.",
            "پژوهش درباره کار دیجیتال و مقررات‌زدایی.",
            "آموزش سواد فناورانه و پرسش از منافع پشت روایت‌ها.",
        ],
        "evolution": "مقاله در ۱۹۹۵ منتشر و در ۱۹۹۶ در Science as Culture چاپ شد. در دهه ۲۰۰۰ با رشد پلتفرم‌ها و اقتصاد اشتراکی بازخوانی شد و در دهه ۲۰۱۰ نقد «سرمایه‌داری پلتفرمی» آن را به کار گرفت. امروز در نقد وب۳، رمزارز و روایت‌های هوش مصنوعی نیز ارجاع می‌شود.",
        "key_concepts": [
            "ایدئولوژی کالیفرنیایی (Californian ideology)",
            "طبقه مجازی (virtual class)",
            "جبر فناورانه (technological determinism)",
            "نئولیبرالیسم (neoliberalism)",
            "ضدفرهنگ (counterculture)",
            "مقررات‌زدایی (deregulation)",
        ],
        "studies": [
            "Barbrook, R., & Cameron, A. (1996). The Californian ideology. Science as Culture, 6(1), 44-72.",
            "Turner, F. (2006). From counterculture to cyberculture. University of Chicago Press.",
        ],
        "theorists": "ریچارد باربروک و اندی کامرون (Richard Barbrook & Andy Cameron)",
        "model": "ترکیب ایدئولوژیک: ضدفرهنگ (فردگرایی بیانگر) + نئولیبرالیسم (بازار آزاد) ← روایت رهایی فناورانه ← حذف کار/دولت/نابرابری ← توجیه مقررات‌زدایی.",
        "detailed_analysis": "\n\n".join([
            "۱. بنیان و منطق نظری\nباربروک و کامرون با تحلیل گفتمان مجلات و کنفرانس‌های فناوری دهه نود، نشان دادند که دو سنت سیاسی متضاد در یک روایت جمع شده‌اند: آزادی بیانگر دهه شصت و بازار آزاد دهه هشتاد. نتیجه، ایدئولوژی‌ای است که فناوری را عامل رهایی و دولت را مانع آن می‌بیند.",
            "۲. سازوکار عملی و تشخیصی\nبرای تحلیل یک گفتمان فناورانه، سه پرسش مطرح می‌شود: چه چیزی «طبیعی» و اجتناب‌ناپذیر معرفی می‌شود؟ چه کسانی سخنگوی آن‌اند؟ و چه چیزهایی از روایت حذف شده‌اند؟ این پرسش‌ها ایدئولوژی را از توصیف فنی جدا می‌کند.",
            "۳. دلالت‌ها برای پژوهش رسانه\nپژوهش معاصر این چارچوب را برای نقد پلتفرم، رمزارز و هوش مصنوعی به کار می‌برد. پرسش باز: آیا «ایدئولوژی کالیفرنیایی» می‌تواند اشکال غیرآمریکایی و دولتی‌تر فناوری را نیز توضیح دهد، یا به یک نقد بافت‌محور محدود است؟",
        ]),
        "critique_text": "\n".join([
            "۱. تعمیم بیش از حد: دره سیلیکون مجموعه‌ای متنوع از بازیگران است و یکسان‌سازی آن، تفاوت‌های سیاسی را پنهان می‌کند.",
            "۲. نگاه بیرونی: نویسندگان اروپایی، گفتمان آمریکایی را از فاصله تحلیل کرده‌اند و ممکن است تفاوت‌های محلی را کم‌ببینند.",
            "۳. قاب زمانی: مقاله snapshot دهه نود است و تحول پلتفرم‌های بزرگ، سرمایه‌گذاری دولتی و اقتصاد داده را در بر نمی‌گیرد.",
            "۴. نادیده‌گرفتن نقش دولت: خود اینترنت محصول سرمایه‌گذاری دولتی و پژوهشی است و روایت «ضددولت» ناقص است.",
            "۵. ابهام مفهومی: «ایدئولوژی» گاه به‌معنای جهان‌بینی و گاه به‌معنای فریب به کار رفته و تحلیل را تیز نمی‌کند.",
        ]),
        "example_text": "شرکتی که مقررات حفاظت داده را «مانع نوآوری» می‌خواند و هم‌زمان از زیرساخت عمومی اینترنت سود می‌برد، نمونه‌ای از منطق این ایدئولوژی است: آزادی بازار برای خود، زیرساخت عمومی از دیگران. همین ساختار در گفتمان برخی پلتفرم‌ها دیده می‌شود که خود را «بی‌طرف» معرفی می‌کنند، در حالی که قواعد دیده‌شدن را تعیین می‌کنند.",
    },
    "MC-417": {
        "summary": "(برنرز-لی، ۱۹۸۹) وب به‌مثابه فضای باز، بر معماری توزیع‌شده و بدون مالک مرکزی استوار است که انتشار و پیوند آزاد اطلاعات را ممکن می‌کند. برنرز-لی در پیشنهاد ۱۹۸۹ خود در CERN، سیستمی از هایپر텍ست جهانی با شناسه یکتا، پروتکل مشترک و دسترسی بی‌اجازه طراحی کرد. این معماری، وب را به بستری برای نوآوری بدون مجوز و مشارکت جهانی بدل کرد.",
        "definition": "فضای باز وب، مجموعه‌ای از اصول معماری است: تمرکززدایی، جهان‌شمولی، سازگاری با هر دستگاه و زبان، استانداردهای باز و امکان پیوند آزاد میان منابع. «باز» در اینجا به دسترسی و پیوندپذیری بی‌اجازه اشاره دارد، نه به بی‌طرفی کامل محتوا یا نبود قدرت.",
        "main_problem": "مسئله این بود که چگونه می‌توان اطلاعات را در نظامی از رایانه‌های ناهمگون و بدون مرجع مرکزی به اشتراک گذاشت، به‌گونه‌ای که هر کس بتواند منتشر کند و به هر منبعی پیوند بزند. پیشنهاد برنرز-لی پاسخی فنی با پیامدهای اجتماعی بود.",
        "mechanism": "\n".join([
            "۱. هایپر텍ست جهانی: متن به پیوند بدل می‌شود و مسیر خواندن از سلسله‌مراتب ناشر به شبکه ارجاع منتقل می‌شود.",
            "۲. شناسه یکتا: هر منبع آدرس یکتایی می‌گیرد؛ این آدرس‌دهی، پیوند و یافتن را در مقیاس جهانی ممکن می‌کند.",
            "۳. پروتکل مشترک: زبان و قاعده‌ای مشترک (HTTP/HTML) امکان ارتباط میان سیستم‌های متفاوت را می‌دهد.",
            "۴. تمرکززدایی: هیچ فهرست مرکزی و مالک واحدی وجود ندارد؛ هر سرور می‌تواند منبع منتشر کند.",
            "۵. جهان‌شمولی: وب برای هر نوع محتوا، زبان و دستگاه طراحی می‌شود و به کاربرد خاص محدود نیست.",
            "۶. پیوند آزاد: هر کس می‌تواند بدون اجازه به هر منبع عمومی پیوند بزند؛ این «پیوندپذیری» موتور رشد وب بود.",
            "در بستر رسانه، اصول باز وب امکان ظهور وبلاگ، ویکی، روزنامه‌نگاری مستقل و تجارت الکترونیک را فراهم کرد. اما از دهه ۲۰۱۰، «پلتفرم‌سازی» بخش بزرگی از این فضا را به باغ‌های محصور منتقل کرد: محتوا در اپلیکیشن‌هایی قرار گرفت که پیوند بیرونی، جست‌وجو و دسترسی داده را محدود می‌کنند. امروز بحث «وب باز» بر استانداردهای باز، قابلیت انتقال داده و مقررات دروازه‌بانی متمرکز است؛ پرسش این است که آیا اصول معماری ۱۹۸۹ می‌تواند در اقتصاد پلتفرم زنده بماند.",
        ]),
        "assumptions": [
            "تمرکززدایی، انتشار و نوآوری را افزایش می‌دهد.",
            "استاندارد باز و پروتکل مشترک، همکاری در مقیاس جهانی را ممکن می‌کند.",
            "پیوند آزاد، دسترسی به دانش را گسترش می‌دهد.",
        ],
        "principles": [
            "معماری باید بدون مالک مرکزی کار کند.",
            "هر منبع باید شناسه یکتا و قابل پیوند داشته باشد.",
            "استانداردها باید باز و بدون هزینه مجوز باشند.",
        ],
        "critiques": [
            "رمانتیسم بازبودن: «باز» بودن فنی، تضمینی برای دموکراسی یا عدالت نیست و می‌تواند به نظارت و سوءاستفاده نیز بینجامد.",
            "تمرکز دوباره: پلتفرم‌ها با استفاده از همین وب باز، قدرت را در لایه خدمات متمرکز کرده‌اند.",
            "نابرابری دسترسی: جهان‌شمولی فنی با شکاف مهارت، زبان و زیرساخت همراه شده است.",
            "حاکمیت استانداردها: نهادهای استانداردسازی خود عرصه نفوذ شرکت‌ها و دولت‌ها هستند.",
            "کیفیت و اعتماد: پیوند آزاد بدون سازوکار اعتبارسنجی، اطلاعات نادرست و اسپم را نیز گسترش می‌دهد.",
        ],
        "applications": [
            "طراحی سرویس‌های قابل انتقال و پیوندپذیر.",
            "سیاست‌گذاری استانداردهای باز و دروازه‌بانی.",
            "پژوهش درباره تمرکز پلتفرم و باغ محصور.",
            "آموزش سواد وب و انتشار مستقل.",
        ],
        "evolution": "پیشنهاد ۱۹۸۹ به ساخت وب در CERN و سپس بنیاد W3C انجامید. در دهه ۲۰۰۰، وب۲ و پلتفرم‌ها لایه خدمات را متمرکز کردند. در دهه ۲۰۱۰، جنبش «وب باز» و مقررات دروازه‌بانی اروپا، اصول اولیه را بازخوانی کردند و پروژه‌هایی چون داده‌های قابل انتقال، تلاش کردند تعادل را بازگردانند.",
        "key_concepts": [
            "هایپر텍ست (hypertext)",
            "شناسه یکتا (URI)",
            "تمرکززدایی (decentralization)",
            "استاندارد باز (open standard)",
            "پیوند آزاد (permissionless linking)",
            "باغ محصور (walled garden)",
        ],
        "studies": [
            "Berners-Lee, T. (1989). Information management: A proposal. CERN.",
            "Berners-Lee, T., & Fischetti, M. (1999). Weaving the web. HarperCollins.",
        ],
        "theorists": "تیم برنرز-لی (Tim Berners-Lee)",
        "model": "معماری باز: شناسه یکتا + پروتکل مشترک + سرورهای توزیع‌شده ← انتشار و پیوند بی‌اجازه ← نوآوری و مشارکت؛ با تهدید معاصر تمرکز پلتفرمی.",
        "detailed_analysis": "\n\n".join([
            "۱. بنیان و منطق نظری\nبرنرز-لی در CERN با مسئله ناسازگاری سیستم‌های اطلاعاتی روبه‌رو بود. راه‌حل او نه یک نرم‌افزار واحد، بلکه مجموعه‌ای از قواعد ساده و باز بود: آدرس، پروتکل و زبان نشانه‌گذاری. همین سادگی و بازبودن، وب را از یک ابزار سازمانی به زیرساخت جهانی تبدیل کرد.",
            "۲. سازوکار عملی و تشخیصی\nبرای ارزیابی «بازبودن» یک سرویس، سه پرسش مطرح می‌شود: آیا داده قابل انتقال است؟ آیا پیوند بیرونی و خواندن مستقل ممکن است؟ و آیا استاندارد آن باز و بی‌طرف است؟ پاسخ این پرسش‌ها، بازبودن اعلامی را از بازبودن واقعی جدا می‌کند.",
            "۳. دلالت‌ها برای پژوهش رسانه\nپژوهش معاصر بر تعارض میان بازبودن معماری و تمرکز اقتصادی متمرکز است. پرسش باز: آیا می‌توان با مقررات قابلیت انتقال و استانداردهای باز، «فضای باز» را در اقتصاد پلتفرم بازسازی کرد، یا چرخه تمرکز اجتناب‌ناپذیر است؟",
        ]),
        "critique_text": "\n".join([
            "۱. رمانتیسم بازبودن: «باز» بودن فنی، تضمینی برای دموکراسی یا عدالت نیست و می‌تواند به نظارت و سوءاستفاده نیز بینجامد.",
            "۲. تمرکز دوباره: پلتفرم‌ها با استفاده از همین وب باز، قدرت را در لایه خدمات متمرکز کرده‌اند.",
            "۳. نابرابری دسترسی: جهان‌شمولی فنی با شکاف مهارت، زبان و زیرساخت همراه شده است.",
            "۴. حاکمیت استانداردها: نهادهای استانداردسازی خود عرصه نفوذ شرکت‌ها و دولت‌ها هستند.",
            "۵. کیفیت و اعتماد: پیوند آزاد بدون سازوکار اعتبارسنجی، اطلاعات نادرست و اسپم را نیز گسترش می‌دهد.",
        ]),
        "example_text": "وبلاگی که با دامنه شخصی منتشر می‌شود و به منابع دیگر پیوند می‌زند، منطق فضای باز را بازتولید می‌کند: هیچ پلتفرمی اجازه انتشار یا پیوند را صادر نمی‌کند. در مقابل، ویدیویی که فقط در یک اپلیکیشن قابل مشاهده است و پیوند آن به بیرون محدود می‌شود، نمونه باغ محصور است. تفاوت این دو، نه در محتوا، بلکه در معماری دسترسی است.",
    },
    "MC-418": {
        "summary": "(لوی، ۱۹۹۷) هوش جمعی به توانایی جوامع آنلاین در ترکیب و هم‌افزایی قابلیت‌های شناختی و دانشی خود اشاره دارد. لوی استدلال کرد فضای سایبر، «فضای دانش» تازه‌ای می‌سازد که در آن دانش از انحصار نهادها بیرون می‌آید و در شبکه‌ها توزیع می‌شود. او این وضعیت را «جهان‌شمولی بدون تمامیت» خواند: همگان در دانش سهیم می‌شوند، بدون آنکه در یک کل بسته ادغام شوند.",
        "definition": "هوش جمعی، ظرفیتی است که از اتصال شناخت‌ها، مهارت‌ها و تجربه‌های پراکنده در شبکه پدید می‌آید و از جمع ساده افراد بیشتر است. در معنای لوی، این ظرفیت نه فقط فنی، بلکه فرهنگی و سیاسی است: شکل تازه‌ای از شهروندی و تولید دانش.",
        "main_problem": "مسئله این است که چگونه می‌توان دانش پراکنده و متخصصان جزیره‌ای را برای حل مسائل پیچیده به هم وصل کرد، بدون تمرکز آن در نهاد یا نخبگان. لوی فضای سایبر را پاسخ می‌دید، زیرا امکان پیوند و مشارکت را گسترش می‌دهد.",
        "mechanism": "\n".join([
            "۱. هم‌افزایی شناختی: هوش جمعی حاصل ترکیب توانایی‌هاست، نه جمع حساب‌شده آن‌ها؛ پیوند میان افراد، توان تازه می‌سازد.",
            "۲. فضای دانش: هایپر텍ست و شبکه، دانش را از قفس کتاب و نهاد بیرون می‌آورد و آن را به نقشه‌ای قابل ناوبری بدل می‌کند.",
            "۳. جهان‌شمولی بدون تمامیت: همه می‌توانند مشارکت کنند، اما دانش به یک کل بسته و یکسان تبدیل نمی‌شود.",
            "۴. هویت جمعی: «ما»ی شبکه‌ای از راه اشتراک دانش و پروژه ساخته می‌شود، نه از راه مرز جغرافیایی.",
            "۵. کازمپدیا: لوی دانشنامه مشارکتی و پویا را الگوی تولید دانش جمعی می‌دید؛ الگویی که ویکی‌پدیا تا حدی محقق کرد.",
            "۶. شهروندی دانشی: مشارکت در تولید دانش، شکلی از کنش سیاسی و مدنی است و دموکراسی را به دانش گره می‌زند.",
            "در بستر رسانه، هوش جمعی در ویکی‌پدیا، نرم‌افزار آزاد، علم شهروندی و پلتفرم‌های اشتراک دانش دیده می‌شود. اما همین زیرساخت، امکان «هوش جمعی معکوس» را نیز فراهم می‌کند: هماهنگی برای اطلاعات نادرست، آزار گروهی و دستکاری نظر عمومی. پرسش معاصر این است که چه طراحی نهادی و چه مهارت‌هایی، هم‌افزایی شناختی را از هم‌افزایی سوگیری جدا می‌کند.",
        ]),
        "assumptions": [
            "شبکه‌های دیجیتال می‌توانند شناخت‌های پراکنده را به هم وصل کنند.",
            "مشارکت باز، کیفیت و تنوع دانش را افزایش می‌دهد.",
            "دانش جمعی می‌تواند از انحصار نهادی بیرون بیاید.",
        ],
        "principles": [
            "ارزش شبکه از پیوند کیفیت‌ها می‌آید، نه از تعداد اعضا.",
            "دانش باید قابل ناوبری، پیوندپذیر و مشارکتی باشد.",
            "شهروندی دانشی، مکمل شهروندی سیاسی است.",
        ],
        "critiques": [
            "خوش‌بینی فناورانه: فرض می‌شود شبکه به‌طور خودکار هم‌افزایی می‌سازد، در حالی که می‌تواند سوگیری و اطلاعات نادرست را نیز تقویت کند.",
            "نابرابری مشارکت: دسترسی، مهارت و زمان به‌طور نابرابر توزیع شده و «همگان» در عمل اقلیتی فعال‌اند.",
            "ابهام سنجش: هوش جمعی مفهومی گسترده است و شاخص روشنی برای سنجش آن ارائه نشده.",
            "کم‌توجهی به قدرت: مالکیت پلتفرم، الگوریتم و اقتصاد توجه در تحلیل لوی کم‌رنگ است.",
            "زبان آرمانی: لحن فلسفی و امیدوارانه کتاب، مرز توصیف و تجویز را مبهم می‌کند.",
        ],
        "applications": [
            "طراحی پلتفرم‌های دانش مشارکتی.",
            "مطالعه علم شهروندی و تولید همتا.",
            "آموزش همکاری دیجیتال و سواد مشارکتی.",
            "پژوهش درباره کیفیت دانش جمعی و اعتبارسنجی.",
        ],
        "evolution": "لوی مفهوم را در «هوش جمعی» (۱۹۹۴ به فرانسه، ۱۹۹۷ به انگلیسی) طرح کرد و در «کازمپدیا» (۲۰۱۰) بسط داد. پژوهش‌های بعدی آن را با ویکی‌پدیا، نرم‌افزار آزاد و رسانه‌های مشارکتی پیوند زدند و نقدهایی درباره اطلاعات نادرست و تمرکز پلتفرمی افزودند.",
        "key_concepts": [
            "هوش جمعی (collective intelligence)",
            "فضای دانش (knowledge space)",
            "جهان‌شمولی بدون تمامیت (universal without totality)",
            "کازمپدیا (cosmopedia)",
            "هایپر텍ست (hypertext)",
            "شهروندی دانشی (knowledge citizenship)",
        ],
        "studies": [
            "Levy, P. (1997). Collective intelligence: Mankind's emerging world in cyberspace. Plenum Trade.",
            "Jenkins, H. (2006). Convergence culture: Where old and new media collide. New York University Press.",
        ],
        "theorists": "پیر لوی (Pierre Levy)",
        "model": "زنجیره هوش جمعی: پیوند شناخت‌های پراکنده ← فضای دانش مشترک ← مشارکت و هم‌افزایی ← دانش جمعی و شهروندی دانشی؛ با خطر معکوس‌شدن به سوگیری جمعی.",
        "detailed_analysis": "\n\n".join([
            "۱. بنیان و منطق نظری\nلوی با سنت فلسفه دانش و مطالعات سایبرculture، فضای دیجیتال را نه ابزار انتقال، بلکه محیطی برای بازساخت دانش دید. او مفهوم «فضای دانش» را در برابر فضای جغرافیایی و فضای اقتصادی قرار داد و تأکید کرد که دانش در شبکه، پویا، پیوندی و مشارکتی است.",
            "۲. سازوکار عملی و تشخیصی\nبرای ارزیابی یک اجتماع دانشی، سه پرسش مطرح می‌شود: آیا مشارکت باز است؟ آیا سازوکار اعتبارسنجی وجود دارد؟ و آیا دانش تولیدشده قابل بازاستفاده و نقد است؟ پاسخ این پرسش‌ها، هوش جمعی را از تجمع نظر جدا می‌کند.",
            "۳. دلالت‌ها برای پژوهش رسانه\nپژوهش معاصر بر کیفیت، تنوع و آسیب‌پذیری دانش جمعی متمرکز است. پرسش باز: در عصر مدل‌های زبانی که دانش را بازتولید می‌کنند، آیا هوش جمعی به ماده خام شرکت‌ها بدل می‌شود یا شکل تازه‌ای از خرد جمعی می‌سازد؟",
        ]),
        "critique_text": "\n".join([
            "۱. خوش‌بینی فناورانه: فرض می‌شود شبکه به‌طور خودکار هم‌افزایی می‌سازد، در حالی که می‌تواند سوگیری و اطلاعات نادرست را نیز تقویت کند.",
            "۲. نابرابری مشارکت: دسترسی، مهارت و زمان به‌طور نابرابر توزیع شده و «همگان» در عمل اقلیتی فعال‌اند.",
            "۳. ابهام سنجش: هوش جمعی مفهومی گسترده است و شاخص روشنی برای سنجش آن ارائه نشده.",
            "۴. کم‌توجهی به قدرت: مالکیت پلتفرم، الگوریتم و اقتصاد توجه در تحلیل لوی کم‌رنگ است.",
            "۵. زبان آرمانی: لحن فلسفی و امیدوارانه کتاب، مرز توصیف و تجویز را مبهم می‌کند.",
        ]),
        "example_text": "در یک پروژه علم شهروندی، هزاران کاربر داده پراکنده را ثبت می‌کنند و پژوهشگران آن را تحلیل می‌کنند؛ نتیجه، دانشی است که هیچ گروهی به‌تنهایی نمی‌توانست تولید کند. اما اگر همان شبکه برای انتشار ادعای نادرست هماهنگ شود، «هوش جمعی» به «سوگیری جمعی» بدل می‌شود. تفاوت این دو، در سازوکار اعتبارسنجی و شفافیت است، نه در فناوری.",
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
    total = structure + analysis + citation + accuracy + relations + classification + clarity + currency
    detail = {"structure_15": structure, "analysis_15": analysis, "citation_20": citation,
              "accuracy_25_auto": accuracy, "relations_10": relations,
              "classification_5": classification, "clarity_5": clarity, "currency_5": currency}
    return total, detail, words


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
                                       "verified": n_verified, "batch": 79}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH79 THEORY DONE")


if __name__ == "__main__":
    main()
