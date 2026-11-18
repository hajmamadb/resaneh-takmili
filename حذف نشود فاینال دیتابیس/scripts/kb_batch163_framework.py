# -*- coding: utf-8 -*-
"""Batch 163 (HYPOTHESIS): MC-535 arousal transfer, MC-553 return to strong effects, MC-558 third-person effect, MC-559 first-person effect."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch163-hypothesis-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch163_hypothesis.json"

S = {
    "MC-535": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Excitation Transfer in Communication-Mediated Aggressive Behavior",
             title_fa="انتقال تحریک در رفتار پرخاشگرانهٔ واسطه‌شده با ارتباطات",
             authors="Zillmann, D.", year=1971,
             publisher="Journal of Experimental Social Psychology",
             doi="10.1016/0022-1031(71)90075-8",
             url="https://www.sciencedirect.com/science/article/pii/0022103171900758",
             language="en", isbn=None,
             citation="Zillmann, D. (1971). Excitation transfer in communication-mediated aggressive behavior. Journal of Experimental Social Psychology, 7(4), 419-434.",
             locator="7(4):419-434", locator_type="page_range",
             supports="original demonstration of residual excitation transfer after media exposure", verified=True),
        dict(kind="BOOK_CHAPTER",
             title_en="Excitation-Transfer Theory and Three-Factor Theory of Emotion",
             title_fa="نظریهٔ انتقال تحریک و نظریهٔ سه‌عاملی هیجان",
             authors="Bryant, J.; Miron, D.", year=2003,
             publisher="Lawrence Erlbaum Associates",
             doi="10.4324/9781410607584-4",
             url="https://www.taylorfrancis.com/chapters/edit/10.4324/9781410607584-4/excitation-transfer-theory-three-factor-theory-emotion-jennings-bryant-dorina-miron",
             language="en", isbn=None,
             citation="Bryant, J., & Miron, D. (2003). Excitation-transfer theory and three-factor theory of emotion. In J. Bryant, D. Roskos-Ewoldsen, & J. Cantor (Eds.), Communication and Emotion: Essays in Honor of Dolf Zillmann. Mahwah, NJ: Lawrence Erlbaum Associates.",
             locator="chapter 2", locator_type="chapter",
             supports="review of excitation transfer and the three-factor theory of emotion", verified=True),
    ],
    "MC-553": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Return to the Concept of Powerful Mass Media",
             title_fa="بازگشت به مفهوم رسانه‌های جمعی قدرتمند",
             authors="Noelle-Neumann, E.", year=1973,
             publisher="Studies of Broadcasting",
             doi=None,
             url="https://www.bibsonomy.org/bibtex/25bcb3844f2437cd493934d9327261059/snauth",
             language="en", isbn=None,
             citation="Noelle-Neumann, E. (1973). Return to the concept of powerful mass media. Studies of Broadcasting, 9, 67-112.",
             locator="9:67-112", locator_type="page_range",
             supports="call for a return to powerful media effects through cumulation, consonance and ubiquity", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Spiral of Silence: A Theory of Public Opinion",
             title_fa="مارپیچ سکوت: نظریه‌ای دربارهٔ افکار عمومی",
             authors="Noelle-Neumann, E.", year=1974,
             publisher="Journal of Communication",
             doi="10.1111/j.1460-2466.1974.tb00367.x",
             url="https://academic.oup.com/joc/article-abstract/24/2/43/4553587",
             language="en", isbn=None,
             citation="Noelle-Neumann, E. (1974). The spiral of silence: A theory of public opinion. Journal of Communication, 24(2), 43-51.",
             locator="24(2):43-51", locator_type="page_range",
             supports="powerful-media account in which perceived opinion climate shapes speech", verified=True),
    ],
    "MC-558": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Third-Person Effect in Communication",
             title_fa="اثر شخص سوم در ارتباطات",
             authors="Davison, W. P.", year=1983,
             publisher="Public Opinion Quarterly",
             doi="10.1086/268763",
             url="https://academic.oup.com/poq/article-abstract/47/1/1/1906961",
             language="en", isbn=None,
             citation="Davison, W. P. (1983). The third-person effect in communication. Public Opinion Quarterly, 47(1), 1-15.",
             locator="47(1):1-15", locator_type="page_range",
             supports="original statement of the third-person effect", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Third-Person Effect: A Critical Review and Synthesis",
             title_fa="اثر شخص سوم: مروری انتقادی و ترکیبی",
             authors="Perloff, R. M.", year=1999,
             publisher="Media Psychology",
             doi="10.1207/s1532785xmep0104_4",
             url="https://www.tandfonline.com/doi/abs/10.1207/s1532785xmep0104_4",
             language="en", isbn=None,
             citation="Perloff, R. M. (1999). The third-person effect: A critical review and synthesis. Media Psychology, 1(4), 353-378.",
             locator="1(4):353-378", locator_type="page_range",
             supports="review of perceptual and behavioral components of the third-person effect", verified=True),
    ],
    "MC-559": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Public's View of the Impact of the Mass Media: A Test of the 'Third Person' Effect",
             title_fa="نگاه عمومی به اثر رسانه‌های جمعی: آزمون اثر شخص سوم",
             authors="Innes, J. M.; Zeitz, H.", year=1988,
             publisher="European Journal of Social Psychology",
             doi="10.1002/ejsp.2420180507",
             url="https://onlinelibrary.wiley.com/doi/abs/10.1002/ejsp.2420180507",
             language="en", isbn=None,
             citation="Innes, J. M., & Zeitz, H. (1988). The public's view of the impact of the mass media: A test of the 'third person' effect. European Journal of Social Psychology, 18(5), 457-463.",
             locator="18(5):457-463", locator_type="page_range",
             supports="evidence that for some messages perceived influence on self exceeds influence on others", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Third-Person Effect: A Critical Review and Synthesis",
             title_fa="اثر شخص سوم: مروری انتقادی و ترکیبی",
             authors="Perloff, R. M.", year=1999,
             publisher="Media Psychology",
             doi="10.1207/s1532785xmep0104_4",
             url="https://www.tandfonline.com/doi/abs/10.1207/s1532785xmep0104_4",
             language="en", isbn=None,
             citation="Perloff, R. M. (1999). The third-person effect: A critical review and synthesis. Media Psychology, 1(4), 353-378.",
             locator="1(4):353-378", locator_type="page_range",
             supports="framework for reversed and first-person patterns of perceived influence", verified=True),
    ],
}

ENRICH = {
    "MC-535": dict(
        year=1971,
        summary="فرضیهٔ انتقال تحریک، که دولف زیلمن در سال ۱۹۷۱ با آزمایشی دربارهٔ پرخاشگری مطرح کرد، می‌گوید برانگیختگی فیزیولوژیکی برخاسته از یک تجربهٔ رسانه‌ای یا هیجانی، بلافاصله فرو نمی‌نشیند و می‌تواند به موقعیت بعدی منتقل شود. اگر فرد پس از تماشای محتوای هیجان‌انگیز در فاصلهٔ کوتاهی خشمگین یا تحریک شود، باقی‌ماندهٔ آن برانگیختگی به هیجان تازه افزوده می‌شود و شدت پاسخ او را بالا می‌برد، در حالی که منبع اصلی برانگیختگی را به‌درستی به آن نسبت نمی‌دهد. نظریهٔ سه‌عاملی هیجان، که زیلمن بعدها بسط داد، این فرایند را محصول سه مؤلفه می‌داند: برانگیختگی، تفسیر موقعیت و ارزیابی شناختی. بر این پایه، تماشاگر یک فیلم ترسناک یا مسابقهٔ ورزشی مهیج ممکن است در دقایق بعد واکنشی شدیدتر از حد معمول نشان دهد. در رسانه، نظریه برای تحلیل برنامه‌چینی صحنه‌ها، تبلیغات پرهیجان، سرگرمی خشونت‌آمیز، مناظرهٔ سیاسی و محتوای وایرال به کار می‌رود. نقدهای اصلی به آن، وابستگی اثر به فاصلهٔ زمانی، دشواری تفکیک برانگیختگی از تفسیر، تفاوت‌های فردی در حساسیت و محدودیت آزمون‌های آزمایشگاهی را برجسته می‌کنند.",
        definition="فرضیهٔ انتقال تحریک می‌گوید برانگیختگی باقی‌مانده از یک تجربهٔ رسانه‌ای به موقعیت هیجانی بعدی منتقل می‌شود و شدت واکنش فرد را بالا می‌برد.",
        main_problem="چگونه برانگیختگی ناشی از محتوای رسانه‌ای در زمان و موقعیت بعدی ادامه می‌یابد و بر هیجان و رفتار فرد اثر می‌گذارد.",
        mechanism="برانگیختگی فیزیولوژیکی پس از مواجههٔ رسانه‌ای برای مدتی باقی می‌ماند؛ اگر در این فاصله محرک هیجانی تازه‌ای برسد، باقی‌ماندهٔ برانگیختگی به آن افزوده می‌شود و پاسخ شدیدتر می‌شود، در حالی که فرد منبع را به محرک تازه نسبت می‌دهد.",
        assumptions=[
            "برانگیختگی فیزیولوژیکی کند فرو می‌نشیند.",
            "برانگیختگی باقی‌مانده قابل انتقال است.",
            "فرد منبع برانگیختگی را بازتفسیر می‌کند.",
            "شدت هیجان تابع مجموع برانگیختگی است.",
            "فاصلهٔ زمانی اثر را تعیین می‌کند.",
        ],
        principles=[
            "فاصلهٔ زمانی را در تحلیل بسنج.",
            "برانگیختگی را از تفسیر جدا کن.",
            "ترتیب صحنه‌ها را هدفمند بچین.",
            "شدت محرک بعدی را در نظر بگیر.",
            "تفاوت فردی را کنترل کن.",
            "به زمینهٔ طبیعی هم آزمون ببر.",
        ],
        critiques=[
            "وابستگی به فاصلهٔ زمانی زیاد است.",
            "برانگیختگی و تفسیر را نمی‌توان آسان جدا کرد.",
            "تفاوت‌های فردی را کم می‌بیند.",
            "بیشتر آزمون‌ها آزمایشگاهی‌اند.",
            "سنجش فیزیولوژیکی دشوار است.",
            "به اثر بلندمدت کم می‌پردازد.",
            "به زمینهٔ فرهنگی کم توجه دارد.",
            "تعمیم به محتوای دیجیتال کوتاه‌مدت نامعلوم است.",
        ],
        critique_text="منتقدان می‌گویند نظریهٔ انتقال تحریک سازوکار دقیقی از پیوند هیجان رسانه و رفتار بعدی داد اما وابستگی آن به فاصلهٔ زمانی و شرایط آزمایشگاهی، تعمیم آن را محدود می‌کند؛ با این حال، پایهٔ پژوهش هیجان رسانه است.",
        applications=[
            "تحلیل برنامه‌چینی صحنه.",
            "پژوهش تبلیغات پرهیجان.",
            "مطالعهٔ سرگرمی خشونت‌آمیز.",
            "تحلیل مناظرهٔ سیاسی.",
            "پژوهش محتوای وایرال.",
            "طراحی بازی هیجانی.",
            "مطالعهٔ واکنش به خبر بحران.",
            "تحلیل ترتیب محتوای ورزشی.",
            "پژوهش اثر تماشای فیلم ترسناک بر واکنش بعدی.",
            "تحلیل شدت واکنش کاربران پس از محتوای هیجانی.",
            "تحلیل ترتیب صحنه در برنامهٔ ورزشی زنده.",
            "پژوهش واکنش هیجانی به تبلیغات تلویزیونی.",
        ],
        example_text="تماشاگر یک فیلم ترسناک که بلافاصله پس از فیلم با همسایه بحث می‌کند، ممکن است واکنشی شدیدتر از حد معمول نشان دهد؛ نظریه می‌گوید باقی‌ماندهٔ برانگیختگی فیلم به این بحث منتقل شده است.",
        evolution="زیلمن در سال ۱۹۷۱ انتقال تحریک را با آزمایش پرخاشگری نشان داد و در دههٔ ۱۹۸۰ آن را در نظریهٔ سه‌عاملی هیجان گنجاند؛ پژوهش‌های بعدی آن را به سرگرمی، ورزش، تبلیغات و رسانهٔ دیجیتال گستردند.",
        key_concepts=["انتقال تحریک", "برانگیختگی باقی‌مانده", "نظریهٔ سه‌عاملی", "نسبت‌دهی نادرست", "شدت هیجان", "فاصلهٔ زمانی"],
        theorists="دولف زیلمن، جنیگز برایانت و دورینا میرون.",
        theorists_text="نظریه در سنت روان‌شناسی هیجان و پژوهش اثرات رسانه شکل گرفت.",
        model="برانگیختگی رسانه‌ای به‌عنوان منبعی که در موقعیت بعدی به هیجان تازه افزوده می‌شود.",
        studies=[
            "آزمایش سال ۱۹۷۱ انتقال را نشان داد.",
            "پژوهش دههٔ ۱۹۸۰ نظریهٔ سه‌عاملی را ساخت.",
            "مطالعهٔ ورزش، برانگیختگی را سنجید.",
            "پژوهش فیلم، فاصلهٔ زمانی را بررسی کرد.",
            "مطالعهٔ تبلیغات، ترتیب محتوا را تحلیل کرد.",
            "پژوهش دیجیتال، واکنش کوتاه‌مدت را بررسی کرد.",
            "مطالعهٔ صدا، برانگیختگی را تحلیل کرد.",
        ],
    ),
    "MC-553": dict(
        year=1973,
        summary="فرضیهٔ بازگشت به تأثیرات قوی، که الیزابت نوئل-نویمان در سال ۱۹۷۳ در مقالهٔ «بازگشت به مفهوم رسانه‌های جمعی قدرتمند» مطرح کرد، به پارادایم اثرات محدود پاسخ می‌داد و می‌گفت پژوهش تجربی، قدرت رسانه را کم‌برآورد کرده است. او استدلال کرد که آزمون‌های کوتاه‌مدت اقناع، اثر رسانه را در تغییر نگرش سنجیده‌اند، در حالی که قدرت واقعی رسانه در بلندمدت و از راه سه ویژگی انباشت، هم‌آوایی و همه‌جایی آشکار می‌شود. انباشت یعنی تکرار پیام در زمان، هم‌آوایی یعنی هم‌خوانی رسانه‌های مختلف در یک تصویر و همه‌جایی یعنی حضور فراگیر رسانه در زندگی روزمره. نوئل-نویمان این منطق را در نظریهٔ مارپیچ سکوت و در تحلیل نقش تلویزیون در شکل‌دهی اقلیم عقیده به کار برد. در کنار او، نظریهٔ کاشت گربنر و سنت اقتصاد سیاسی و مطالعات فرهنگی نیز بر قدرت بلندمدت رسانه تأکید کردند. در رسانه، فرضیه برای تحلیل تلویزیون، تبلیغات سیاسی، شکل‌گیری اجماع و اقلیم عقیده به کار می‌رود. نقدهای اصلی به آن، ابهام در سنجش انباشت، کم‌توجهی به گزینشگری مخاطب، خطر نزدیک‌شدن به الگوی تزریق و دشواری تعمیم به محیط رسانهٔ چندپاره را برجسته می‌کنند.",
        definition="فرضیهٔ بازگشت به تأثیرات قوی می‌گوید رسانه در بلندمدت و از راه انباشت، هم‌آوایی و همه‌جایی قدرتمند است، هرچند آزمون‌های کوتاه‌مدت اثرات محدود را نشان داده‌اند.",
        main_problem="آیا پارادایم اثرات محدود قدرت رسانه را کم‌برآورد کرده و قدرت واقعی رسانه در بلندمدت و در سطح اجتماعی چگونه آشکار می‌شود.",
        mechanism="پیام در زمان انباشته می‌شود، رسانه‌های مختلف تصویری هم‌آوا می‌سازند و حضور فراگیر رسانه، اقلیم عقیده و چارچوب عمومی را در بلندمدت شکل می‌دهد؛ اثر در آزمون کوتاه‌مدت دیده نمی‌شود.",
        assumptions=[
            "اثر رسانه بلندمدت است.",
            "انباشت پیام اثر می‌سازد.",
            "هم‌آوایی رسانه‌ها تصویر مشترک می‌سازد.",
            "حضور رسانه فراگیر است.",
            "سنجش کوتاه‌مدت کافی نیست.",
        ],
        principles=[
            "اثر را در بلندمدت بسنج.",
            "هم‌آوایی رسانه‌ها را تحلیل کن.",
            "حضور فراگیر را در نظر بگیر.",
            "اقلیم عقیده را رصد کن.",
            "گزینشگری مخاطب را نادیده نگیر.",
            "به چندپارگی رسانه توجه کن.",
        ],
        critiques=[
            "سنجش انباشت دشوار است.",
            "گزینشگری مخاطب را کم می‌بیند.",
            "به الگوی تزریق نزدیک می‌شود.",
            "به رسانهٔ چندپاره کم توجه دارد.",
            "اثر را بیش از اندازه بزرگ می‌کند.",
            "به تفاوت ژانرها کم می‌پردازد.",
            "به زمینهٔ غیرغربی کم توجه دارد.",
            "سنجش تجربی آن پیچیده است.",
        ],
        critique_text="منتقدان می‌گویند فرضیهٔ بازگشت به تأثیرات قوی نقد درستی بر آزمون‌های کوتاه‌مدت بود اما در عمل سنجش انباشت و هم‌آوایی دشوار است و خطر بازگشت به الگوی تزریق را دارد؛ با این حال، دروازهٔ ورود به نظریه‌های اثرات قوی جدید شد.",
        applications=[
            "تحلیل نقش تلویزیون.",
            "پژوهش تبلیغات سیاسی.",
            "مطالعهٔ اقلیم عقیده.",
            "تحلیل شکل‌گیری اجماع.",
            "پژوهش کاشت.",
            "مطالعهٔ رسانهٔ عمومی.",
            "تحلیل هم‌آوایی خبری.",
            "پژوهش اثر بلندمدت تبلیغات.",
            "تحلیل قدرت رسانه در انتخابات.",
            "مطالعهٔ بازگشت اثرات قوی در رسانهٔ دیجیتال.",
            "تحلیل نقش رسانهٔ عمومی در اجماع عمومی.",
            "پژوهش اثر بلندمدت تبلیغات سلامت.",
            "تحلیل هم‌آوایی رسانه‌ها در بحران سیاسی.",
        ],
        example_text="یک پیام تبلیغاتی در یک آگهی تنها اثر کمی دارد، اما همان پیام در ماه‌ها، در چند رسانه و در زندگی روزمره تکرار می‌شود و کم‌کم چارچوب فهم عمومی را می‌سازد؛ فرضیه می‌گوید قدرت رسانه را باید در همین انباشت دید.",
        evolution="نوئل-نویمان در سال ۱۹۷۳ بازگشت به رسانهٔ قدرتمند را مطرح کرد و در سال ۱۹۷۴ آن را در مارپیچ سکوت بسط داد؛ کاشت گربنر و سنت انتقادی، نسخه‌های دیگری از اثرات قوی بلندمدت ساختند و پژوهش دیجیتال، بحث را به الگوریتم و حباب گسترد.",
        key_concepts=["اثرات قوی", "انباشت", "هم‌آوایی", "همه‌جایی", "اقلیم عقیده", "مارپیچ سکوت"],
        theorists="الیزابت نوئل-نویمان و جورج گربنر.",
        theorists_text="فرضیه در سنت پژوهش اثرات بلندمدت و نقد پارادایم اثرات محدود شکل گرفت.",
        model="رسانه به‌عنوان نیروی بلندمدت که با انباشت و هم‌آوایی، اقلیم عقیده را می‌سازد.",
        studies=[
            "مقالهٔ سال ۱۹۷۳ بازگشت را اعلام کرد.",
            "نظریهٔ سال ۱۹۷۴ مارپیچ سکوت را ساخت.",
            "پژوهش کاشت، تصویر بلندمدت را سنجید.",
            "مطالعهٔ انتخاباتی، اقلیم عقیده را بررسی کرد.",
            "پژوهش رسانهٔ عمومی، هم‌آوایی را تحلیل کرد.",
            "مطالعهٔ دیجیتال، اثرات قوی شبکه‌ای را بررسی کرد.",
            "مطالعهٔ طولی، اقلیم عقیده را پیگیری کرد.",
        ],
    ),
    "MC-558": dict(
        year=1983,
        summary="فرضیهٔ اثر شخص سوم، که فیلیپس دیویسون در سال ۱۹۸۳ در فصل‌نامهٔ افکار عمومی مطرح کرد، می‌گوید فرد در مواجهه با پیام رسانه‌ای گمان می‌کند آن پیام بر دیگران بیشتر از خودش اثر می‌گذارد. این ادراک، که اثر شخص سوم نامیده می‌شود، دو مؤلفه دارد: مؤلفهٔ ادراکی، یعنی برآورد بیش‌ازحد اثر بر دیگران، و مؤلفهٔ رفتاری، یعنی پیامدهایی مانند حمایت از سانسور یا تنظیم محتوا برای حمایت از دیگران در برابر اثر. دیویسون توضیح می‌دهد که فرد خود را آگاه‌تر و مقاوم‌تر می‌بیند و دیگران را آسیب‌پذیرتر فرض می‌کند؛ همین سوگیری، به رفتار تنظیمی می‌انجامد. پژوهش‌های بعدی نشان دادند اثر شخص سوم در حوزهٔ خشونت، تبلیغات، اخبار جعلی و محتوای سیاسی قوی است و به ویژگی پیام، درگیری ذهنی و فاصلهٔ اجتماعی از دیگران بستگی دارد. در رسانه، فرضیه برای تحلیل حمایت از تنظیم محتوا، واکنش به اخبار جعلی، کمپین‌های سلامت و سیاست رسانه به کار می‌رود. نقدهای اصلی به آن، ابهام مرجع «دیگران»، تکیه بر خودگزارشی، فاصلهٔ زیاد میان ادراک و رفتار و کم‌توجهی به تفاوت‌های فرهنگی را برجسته می‌کنند.",
        definition="فرضیهٔ اثر شخص سوم می‌گوید افراد باور دارند پیام رسانه‌ای بر دیگران بیشتر از خودشان اثر می‌گذارد و همین ادراک، حمایت آنان از تنظیم محتوا را شکل می‌دهد.",
        main_problem="چرا افراد اثر رسانه بر خود را کمتر از اثر آن بر دیگران برآورد می‌کنند و این برآورد چه پیامدهای رفتاری و سیاستی دارد.",
        mechanism="فرد خود را آگاه و مقاوم و دیگران را آسیب‌پذیر می‌بیند؛ این سوگیری ادراکی، نگرانی برای دیگران و حمایت از سانسور یا تنظیم محتوا را می‌سازد و در نهایت بر رفتار رسانه‌ای اثر می‌گذارد.",
        assumptions=[
            "فرد اثر بر خود را کمتر می‌بیند.",
            "دیگران آسیب‌پذیرتر فرض می‌شوند.",
            "ادراک با رفتار پیوند دارد.",
            "ویژگی پیام اثر را تعدیل می‌کند.",
            "فاصلهٔ اجتماعی از دیگران مهم است.",
        ],
        principles=[
            "مرجع دیگران را روشن کن.",
            "ادراک و رفتار را جدا بسنج.",
            "ویژگی پیام را کنترل کن.",
            "درگیری ذهنی را در تحلیل بگنجان.",
            "به تفاوت فرهنگی توجه کن.",
            "از خودگزارشی صرف فراتر برو.",
        ],
        critiques=[
            "مرجع دیگران مبهم است.",
            "بر خودگزارشی تکیه دارد.",
            "فاصلهٔ ادراک و رفتار زیاد است.",
            "تفاوت فرهنگی را کم می‌بیند.",
            "سنجش اثر واقعی را نادیده می‌گیرد.",
            "به رسانهٔ دیجیتال کم توجه دارد.",
            "به ویژگی مخاطب کم می‌پردازد.",
            "تعمیم نتایج به رفتار واقعی دشوار است.",
        ],
        critique_text="منتقدان می‌گویند اثر شخص سوم الگوی مهمی از سوگیری ادراکی نشان داد اما پیوند آن با رفتار تنظیمی و مرجع مبهم «دیگران» سنجش را دشوار می‌کند؛ با این حال، چارچوب پایهٔ پژوهش ادراک اثر رسانه است.",
        applications=[
            "تحلیل حمایت از سانسور.",
            "پژوهش اخبار جعلی.",
            "مطالعهٔ کمپین سلامت.",
            "تحلیل سیاست رسانه.",
            "پژوهش تبلیغات.",
            "مطالعهٔ خشونت رسانه‌ای.",
            "تحلیل واکنش به محتوای سیاسی.",
            "پژوهش تنظیم محتوای کودک.",
            "تحلیل حمایت از تنظیم شبکه‌های اجتماعی.",
            "مطالعهٔ ادراک اثر تبلیغات انتخاباتی بر رأی‌دهندگان.",
            "تحلیل حمایت از تنظیم تبلیغات کودک.",
        ],
        example_text="والدی که باور دارد خشونت تلویزیونی بر کودکان دیگر اثر مخرب دارد اما بر فرزند خودش کمتر، از محدودسازی پخش حمایت می‌کند؛ فرضیه می‌گوید این حمایت از ادراک اثر شخص سوم می‌آید.",
        evolution="دیویسون در سال ۱۹۸۳ اثر را مطرح کرد و پژوهش‌های دههٔ ۱۹۹۰ مؤلفهٔ رفتاری و تعدیل‌کننده‌ها را بسط دادند؛ پرلاف در سال ۱۹۹۹ مرور انتقادی جامعی نوشت و پژوهش دیجیتال، اثر را به اخبار جعلی و شبکه‌های اجتماعی گسترد.",
        key_concepts=["اثر شخص سوم", "ادراک اثر", "مؤلفهٔ رفتاری", "حمایت از سانسور", "سوگیری خودبرتربین", "فاصلهٔ اجتماعی"],
        theorists="فیلیپس دیویسون و ریچارد پرلاف.",
        theorists_text="فرضیه در سنت پژوهش ادراک افکار عمومی و اثرات رسانه شکل گرفت.",
        model="برآورد بیش‌ازحد اثر رسانه بر دیگران به‌عنوان محرک حمایت از تنظیم محتوا.",
        studies=[
            "مقالهٔ سال ۱۹۸۳ فرضیه را ساخت.",
            "پژوهش دههٔ ۱۹۹۰ مؤلفهٔ رفتاری را بسط داد.",
            "مرور سال ۱۹۹۹ یافته‌ها را جمع کرد.",
            "مطالعهٔ خشونت، ادراک والدین را سنجید.",
            "پژوهش اخبار جعلی، تنظیم محتوا را تحلیل کرد.",
            "مطالعهٔ تطبیقی، تفاوت فرهنگی را بررسی کرد.",
        ],
    ),
    "MC-559": dict(
        year=1988,
        summary="فرضیهٔ اثر شخص اول، که جان اینس و هیلاری زایتز در سال ۱۹۸۸ در آزمایش اثر شخص سوم مشاهده کردند، الگوی معکوس آن است: در برخی پیام‌ها افراد باور دارند پیام بر خودشان بیشتر از دیگران اثر می‌گذارد. این الگو بیشتر در پیام‌های مطلوب و سودمند دیده می‌شود، مانند هشدار سلامت، آموزش عمومی یا توصیهٔ ایمنی، که پذیرش آن به عزت نفس فرد مربوط است. توضیح رایج این است که فرد می‌خواهد خود را منطقی و پذیرا ببیند و در برابر پیام خوب مقاومت نمی‌کند، در حالی که دیگران را کمتر پذیرا فرض می‌کند؛ از این رو اثر شخص اول را با خوش‌بینی سوگیرانه و انگیزهٔ خودافزایی پیوند داده‌اند. پژوهش‌های بعدی نشان دادند که قطب‌بندی پیام، یعنی مطلوب یا نامطلوب بودن آن، جهت اثر را تعیین می‌کند: پیام نامطلوب به اثر شخص سوم و پیام مطلوب به اثر شخص اول می‌انجامد. در رسانه، فرضیه برای تحلیل کمپین سلامت، تبلیغات خدمات عمومی، آموزش محیط زیست و ارتباطات بحران به کار می‌رود. نقدهای اصلی به آن، وابستگی به تعریف مطلوبیت پیام، سنجش خودگزارشی، تفاوت‌های فردی در عزت نفس و کم‌توجهی به رفتار واقعی را برجسته می‌کنند.",
        definition="فرضیهٔ اثر شخص اول می‌گوید افراد در برابر پیام‌های مطلوب و سودمند باور دارند آن پیام بر خودشان بیشتر از دیگران اثر می‌گذارد.",
        main_problem="چرا در برخی پیام‌ها افراد اثر بر خود را بیشتر از اثر بر دیگران می‌بینند و چه شرایطی این الگو را از اثر شخص سوم جدا می‌کند.",
        mechanism="فرد پذیرش پیام مطلوب را نشانهٔ منطقی‌بودن خود می‌داند و خود را پذیراتر از دیگران می‌بیند؛ این خودافزایی، برآورد اثر بر خود را بالا و برآورد اثر بر دیگران را پایین می‌برد.",
        assumptions=[
            "مطلوبیت پیام جهت اثر را تعیین می‌کند.",
            "فرد خود را منطقی می‌بیند.",
            "خوش‌بینی سوگیرانه وجود دارد.",
            "خودافزایی بر برآورد اثر می‌زند.",
            "ادراک با پذیرش پیام پیوند دارد.",
        ],
        principles=[
            "مطلوبیت پیام را مشخص کن.",
            "اثر بر خود و دیگران را جدا بسنج.",
            "عزت نفس را کنترل کن.",
            "رفتار واقعی را نیز اندازه بگیر.",
            "به تفاوت فرهنگی توجه کن.",
            "قطب‌بندی پیام را دستکاری کن.",
        ],
        critiques=[
            "تعریف مطلوبیت پیام مبهم است.",
            "بر خودگزارشی تکیه دارد.",
            "تفاوت‌های فردی را کم می‌بیند.",
            "به رفتار واقعی کم می‌پردازد.",
            "به زمینهٔ فرهنگی کم توجه دارد.",
            "مرز آن با اثر شخص سوم مبهم است.",
            "سنجش خوش‌بینی سوگیرانه دشوار است.",
            "به پیام‌های مختلط کم می‌پردازد.",
        ],
        critique_text="منتقدان می‌گویند اثر شخص اول الگوی مهمی از سوگیری مطلوب‌نگر نشان داد اما تعریف مطلوبیت پیام و پیوند آن با رفتار واقعی روشن نیست؛ با این حال، مکمل ضروری اثر شخص سوم در پژوهش ادراک اثر است.",
        applications=[
            "تحلیل کمپین سلامت.",
            "پژوهش تبلیغات خدمات عمومی.",
            "مطالعهٔ آموزش محیط زیست.",
            "تحلیل ارتباطات بحران.",
            "طراحی پیام واکسیناسیون.",
            "پژوهش سواد رسانه.",
            "مطالعهٔ پذیرش توصیهٔ ایمنی.",
            "تحلیل کمپین مالیاتی.",
            "پژوهش اثر پیام مطلوب بر خود.",
            "تحلیل پذیرش هشدار سلامت در شبکه‌های اجتماعی.",
        ],
        example_text="فردی که پیام ترک سیگار را می‌بیند، باور دارد خودش بیشتر از دوستانش تحت تأثیر قرار می‌گیرد و سیگار را ترک می‌کند؛ فرضیه می‌گوید چون پیام مطلوب است، پذیرش آن به عزت نفس و تصویر منطقی فرد گره می‌خورد.",
        evolution="اینس و زایتز در سال ۱۹۸۸ الگوی معکوس را در آزمون اثر شخص سوم دیدند و پژوهش‌های دههٔ ۱۹۹۰ آن را به پیام مطلوب و خوش‌بینی سوگیرانه پیوند دادند؛ مرور پرلاف در سال ۱۹۹۹ و پژوهش دیجیتال، الگو را در کمپین سلامت و شبکه‌های اجتماعی بسط دادند.",
        key_concepts=["اثر شخص اول", "اثر شخص سوم", "پیام مطلوب", "خوش‌بینی سوگیرانه", "خودافزایی", "ادراک اثر"],
        theorists="جان اینس، هیلاری زایتز و ریچارد پرلاف.",
        theorists_text="فرضیه در سنت پژوهش ادراک اثر و روان‌شناسی اجتماعی شکل گرفت.",
        model="برآورد بیش‌ازحد اثر پیام مطلوب بر خود، در تقابل با برآورد بیش‌ازحد اثر پیام نامطلوب بر دیگران.",
        studies=[
            "آزمایش سال ۱۹۸۸ الگوی معکوس را یافت.",
            "پژوهش دههٔ ۱۹۹۰ آن را به پیام مطلوب گره زد.",
            "مرور سال ۱۹۹۹ الگو را جمع‌بندی کرد.",
            "مطالعهٔ سلامت، پذیرش را سنجید.",
            "پژوهش محیط زیست، پیام مطلوب را تحلیل کرد.",
            "مطالعهٔ دیجیتال، کمپین شبکه‌ای را بررسی کرد.",
        ],
    ),
}

NAME_FIX = {
    "MC-553": ("فرضیهٔ بازگشت به تأثیرات قوی رسانه", "Return to Powerful Media Effects Hypothesis", "عنوان کارت با گیومه و تعریف مبهم بود؛ عنوان به صورت‌بندی اصلی نوئل-نویمان دربارهٔ بازگشت به رسانهٔ قدرتمند اصلاح شد."),
}
YEAR_FIX = {
    "MC-535": "بدنهٔ کارت قالب عمومی اقناع بود و به انتقال تحریک مربوط نبود؛ محتوا بر پایهٔ زیلمن ۱۹۷۱ و برایانت و میرون ۲۰۰۳ بازنویسی شد.",
    "MC-553": "نظریه‌پرداز کارت «نئومارکسیست‌ها و کاشت‌گرایان» ثبت شده بود؛ صورت‌بندی اصلی از نوئل-نویمان ۱۹۷۳ است و سال به ۱۹۷۳ اصلاح شد.",
    "MC-558": "بدنهٔ کارت قالب عمومی اقناع بود و به اثر شخص سوم مربوط نبود؛ محتوا بر پایهٔ دیویسون ۱۹۸۳ و پرلاف ۱۹۹۹ بازنویسی شد.",
    "MC-559": "بدنهٔ کارت ناقص و قالب عمومی اقناع بود و سال ۱۹۹۱ ثبت شده بود؛ نخستین شاهد تجربی الگو در اینس و زایتز ۱۹۸۸ است و سال اصلاح شد.",
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
                                       "verified": n_verified, "batch": 163}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH163 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
