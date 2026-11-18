# -*- coding: utf-8 -*-
"""Batch 238: THEORY MC cards 013, 016, 017, 020, 023, 024, 025, 027, 030 (additive enrichment)."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch238-20261117"
NOW = "2026-11-17 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch238.json"

WHITE50 = dict(kind="JOURNAL_ARTICLE",
               title_en="The 'Gate Keeper': A Case Study in the Selection of News",
               title_fa="دروازه‌بان: مطالعهٔ موردی گزینش خبر",
               authors="David Manning White", year=1950, publisher="Journalism Quarterly",
               doi="10.1177/107769905002700403",
               url="https://journals.sagepub.com/doi/10.1177/107769905002700403",
               language="en", isbn=None,
               citation="White, D. M. (1950). The 'gate keeper': A case study in the selection of news. Journalism Quarterly, 27(4), 383-391.",
               locator="27(4), 383-391", locator_type="PAGE",
               supports="کاهش شدید مطالب دریافتی از خبرگزاری و نقش گزینش ذهنی سردبیر در ساخت تصویر خبری",
               verified=True)

CASTELLS09 = dict(kind="BOOK", title_en="Communication Power",
                  title_fa="قدرت ارتباطات",
                  authors="Manuel Castells", year=2009, publisher="Oxford University Press",
                  doi=None,
                  url="https://global.oup.com/academic/product/communication-power-9780199567041",
                  language="en", isbn="9780199567041",
                  citation="Castells, M. (2009). Communication Power. Oxford: Oxford University Press.",
                  locator="book", locator_type="BOOK",
                  supports="قدرت ارتباطی از راه برنامه‌نویسی شبکه‌ها و جابه‌جایی گره‌ها و مفهوم خودارتباطی انبوه",
                  verified=True)

BELL73 = dict(kind="BOOK", title_en="The Coming of Post-Industrial Society: A Venture in Social Forecasting",
              title_fa="آمدن جامعهٔ پساصنعتی: کوششی در پیش‌بینی اجتماعی",
              authors="Daniel Bell", year=1973, publisher="Basic Books",
              doi=None, url=None, language="en", isbn=None,
              citation="Bell, D. (1973). The Coming of Post-Industrial Society: A Venture in Social Forecasting. New York: Basic Books.",
              locator="book", locator_type="BOOK",
              supports="جامعهٔ پساصنعتی بر پایهٔ دانش نظری و خدمات و گذار از کار یدی به کار دانشی",
              verified=True)

WEBSTER06 = dict(kind="BOOK", title_en="Theories of the Information Society (3rd ed.)",
                 title_fa="نظریه‌های جامعهٔ اطلاعاتی (ویراست سوم)",
                 authors="Frank Webster", year=2006, publisher="Routledge",
                 doi=None, url=None, language="en", isbn=None,
                 citation="Webster, F. (2006). Theories of the Information Society (3rd ed.). London: Routledge.",
                 locator="book", locator_type="BOOK",
                 supports="تعدد تعریف‌های فناورانه، اقتصادی، حرفه‌ای، فضایی و فرهنگی از جامعهٔ اطلاعاتی و نقد سنجش‌پذیری آن",
                 verified=True)

BERGER66 = dict(kind="BOOK", title_en="The Social Construction of Reality: A Treatise in the Sociology of Knowledge",
                title_fa="ساخت اجتماعی واقعیت: رساله‌ای در جامعه‌شناسی معرفت",
                authors="Peter L. Berger; Thomas Luckmann", year=1966, publisher="Doubleday",
                doi=None, url=None, language="en", isbn=None,
                citation="Berger, P. L., & Luckmann, T. (1966). The Social Construction of Reality: A Treatise in the Sociology of Knowledge. New York: Doubleday.",
                locator="book", locator_type="BOOK",
                supports="برونی‌سازی، عینی‌سازی و درونی‌سازی واقعیت در تعامل اجتماعی و نهادها",
                verified=True)

SEARLE95 = dict(kind="BOOK", title_en="The Construction of Social Reality",
                title_fa="ساخت واقعیت اجتماعی",
                authors="John R. Searle", year=1995, publisher="Free Press",
                doi=None,
                url="https://archive.org/details/constructionofso00sear",
                language="en", isbn="9780684831798",
                citation="Searle, J. R. (1995). The Construction of Social Reality. New York: Free Press.",
                locator="book", locator_type="BOOK",
                supports="تفکیک واقعیت خام از واقعیت نهادی و کارکردهای منزلتی بر پایهٔ قصد جمعی و قاعدهٔ سازنده",
                verified=True)

FESTINGER57 = dict(kind="BOOK", title_en="A Theory of Cognitive Dissonance",
                   title_fa="نظریهٔ ناهماهنگی شناختی",
                   authors="Leon Festinger", year=1957, publisher="Stanford University Press",
                   doi=None, url=None, language="en", isbn=None,
                   citation="Festinger, L. (1957). A Theory of Cognitive Dissonance. Stanford: Stanford University Press.",
                   locator="book", locator_type="BOOK",
                   supports="ناهماهنگی به‌عنوان محرک تغییر شناخت و رفتار و راهبردهای کاهش آن",
                   verified=True)

FESTC59 = dict(kind="JOURNAL_ARTICLE",
               title_en="Cognitive Consequences of Forced Compliance",
               title_fa="پیامدهای شناختی اطاعت اجباری",
               authors="Leon Festinger; James M. Carlsmith", year=1959,
               publisher="Journal of Abnormal and Social Psychology",
               doi="10.1037/h0041593",
               url="https://doi.org/10.1037/h0041593",
               language="en", isbn=None,
               citation="Festinger, L., & Carlsmith, J. M. (1959). Cognitive consequences of forced compliance. Journal of Abnormal and Social Psychology, 58(2), 203-210.",
               locator="58(2), 203-210", locator_type="PAGE",
               supports="تغییر نگرش در شرایط توجیه ناکافی و اثر ادراک آزادی انتخاب بر شدت ناهماهنگی",
               verified=True)

ROGERS75 = dict(kind="JOURNAL_ARTICLE",
                title_en="A Protection Motivation Theory of Fear Appeals and Attitude Change",
                title_fa="نظریهٔ انگیزش محافظت دربارهٔ پیام‌های ترس و تغییر نگرش",
                authors="Ronald W. Rogers", year=1975, publisher="The Journal of Psychology",
                doi="10.1080/00223980.1975.9915803",
                url="https://www.tandfonline.com/doi/abs/10.1080/00223980.1975.9915803",
                language="en", isbn=None,
                citation="Rogers, R. W. (1975). A protection motivation theory of fear appeals and attitude change. The Journal of Psychology, 91(1), 93-114.",
                locator="91(1), 93-114", locator_type="PAGE",
                supports="ارزیابی تهدید و ارزیابی مقابله به‌عنوان مسیرهای انگیزش محافظت",
                verified=True)

MADDUX83 = dict(kind="JOURNAL_ARTICLE",
                title_en="Protection Motivation and Self-Efficacy: A Revised Theory of Fear Appeals and Attitude Change",
                title_fa="انگیزش محافظت و خودکارآمدی: نظریه‌ای بازنگری‌شده دربارهٔ پیام‌های ترس",
                authors="James E. Maddux; Ronald W. Rogers", year=1983,
                publisher="Journal of Experimental Social Psychology",
                doi="10.1016/0022-1031(83)90023-9",
                url="https://www.sciencedirect.com/science/article/pii/0022103183900239",
                language="en", isbn=None,
                citation="Maddux, J. E., & Rogers, R. W. (1983). Protection motivation and self-efficacy: A revised theory of fear appeals and attitude change. Journal of Experimental Social Psychology, 19(5), 469-479.",
                locator="19(5), 469-479", locator_type="PAGE",
                supports="افزودن خودکارآمدی به‌عنوان مؤلفهٔ چهارم و تفکیک آن از کارآمدی پاسخ",
                verified=True)

MCGUIRE61 = dict(kind="JOURNAL_ARTICLE",
                 title_en="Resistance to Persuasion Conferred by Active and Passive Prior Refutation of the Same and Alternative Counterarguments",
                 title_fa="مقاومت در برابر متقاعدسازی از راه ردّ پیشین فعال و منفعل استدلال‌های مقابل",
                 authors="William J. McGuire", year=1961,
                 publisher="Journal of Abnormal and Social Psychology",
                 doi="10.1037/h0048344",
                 url="https://doi.apa.org/doi/10.1037/h0048344",
                 language="en", isbn=None,
                 citation="McGuire, W. J. (1961). Resistance to persuasion conferred by active and passive prior refutation of the same and alternative counterarguments. Journal of Abnormal and Social Psychology, 63(2), 326-332.",
                 locator="63(2), 326-332", locator_type="PAGE",
                 supports="تلقین پیشین با استدلال‌های ضعیف‌شده و برتری ردّ فعال در ایجاد مقاومت",
                 verified=True)

COMPTON05 = dict(kind="BOOK_CHAPTER",
                 title_en="Inoculation Theory of Resistance to Influence at Maturity: Recent Progress in Theory, Research, and Practice",
                 title_fa="نظریهٔ تلقیح مقاومت در برابر تأثیر در مرحلهٔ بلوغ: پیشرفت نظری، پژوهشی و کاربردی",
                 authors="Josh Compton; Michael Pfau", year=2005,
                 publisher="Communication Yearbook 29 (Routledge)",
                 doi=None,
                 url="https://psycnet.apa.org/record/2005-05580-004",
                 language="en", isbn=None,
                 citation="Compton, J., & Pfau, M. (2005). Inoculation theory of resistance to influence at maturity: Recent progress in theory, research, and practice. In Communication Yearbook 29 (pp. 97-145). Mahwah, NJ: Lawrence Erlbaum.",
                 locator="pp. 97-145", locator_type="PAGE",
                 supports="تهدید و پیش‌درمانی ردّی به‌عنوان دو مؤلفهٔ سازوکار تلقیح",
                 verified=True)

AJZEN91 = dict(kind="JOURNAL_ARTICLE",
               title_en="The Theory of Planned Behavior",
               title_fa="نظریهٔ رفتار برنامه‌ریزی‌شده",
               authors="Icek Ajzen", year=1991,
               publisher="Organizational Behavior and Human Decision Processes",
               doi="10.1016/0749-5978(91)90020-T",
               url="https://doi.org/10.1016/0749-5978(91)90020-T",
               language="en", isbn=None,
               citation="Ajzen, I. (1991). The theory of planned behavior. Organizational Behavior and Human Decision Processes, 50(2), 179-211.",
               locator="50(2), 179-211", locator_type="PAGE",
               supports="نگرش، هنجار ذهنی و کنترل رفتار ادراک‌شده به‌عنوان تعیین‌کننده‌های نیت و رفتار",
               verified=True)

FISHBEIN75 = dict(kind="BOOK",
                  title_en="Belief, Attitude, Intention, and Behavior: An Introduction to Theory and Research",
                  title_fa="باور، نگرش، نیت و رفتار: درآمدی بر نظریه و پژوهش",
                  authors="Martin Fishbein; Icek Ajzen", year=1975, publisher="Addison-Wesley",
                  doi=None, url=None, language="en", isbn=None,
                  citation="Fishbein, M., & Ajzen, I. (1975). Belief, Attitude, Intention, and Behavior: An Introduction to Theory and Research. Reading, MA: Addison-Wesley.",
                  locator="book", locator_type="BOOK",
                  supports="نظریهٔ عمل و تبیین نیت رفتاری از نگرش و هنجار ذهنی",
                  verified=True)

BREHM66 = dict(kind="BOOK", title_en="A Theory of Psychological Reactance",
               title_fa="نظریهٔ واکنش روانی",
               authors="Jack W. Brehm", year=1966, publisher="Academic Press",
               doi=None,
               url="https://psycnet.apa.org/record/1967-08061-000",
               language="en", isbn=None,
               citation="Brehm, J. W. (1966). A Theory of Psychological Reactance. New York: Academic Press.",
               locator="book", locator_type="BOOK",
               supports="آزادی‌ها، تهدید آزادی و انگیزهٔ واکنشی بازیابی آن",
               verified=True)

BREHM81 = dict(kind="BOOK", title_en="Psychological Reactance: A Theory of Freedom and Control",
               title_fa="واکنش روانی: نظریهٔ آزادی و کنترل",
               authors="Sharon S. Brehm; Jack W. Brehm", year=1981, publisher="Academic Press",
               doi=None,
               url="https://archive.org/details/psychologicalrea0000breh",
               language="en", isbn=None,
               citation="Brehm, S. S., & Brehm, J. W. (1981). Psychological Reactance: A Theory of Freedom and Control. New York: Academic Press.",
               locator="book", locator_type="BOOK",
               supports="گسترش نظریه به روابط میان‌فردی و بالینی و عوامل تعیین‌کنندهٔ شدت واکنش",
               verified=True)

S = {
    "MC-013": [WHITE50, CASTELLS09],
    "MC-016": [CASTELLS09, WEBSTER06],
    "MC-017": [BELL73, WEBSTER06],
    "MC-020": [BERGER66, SEARLE95],
    "MC-023": [FESTINGER57, FESTC59],
    "MC-024": [ROGERS75, MADDUX83],
    "MC-025": [MCGUIRE61, COMPTON05],
    "MC-027": [FISHBEIN75, AJZEN91],
    "MC-030": [BREHM66, BREHM81],
}

ENRICH = {code: dict() for code in S}

APPEND = {
    "MC-013": dict(
        summary=(" وایت (۱۹۵۰) در مطالعهٔ کلاسیک «آقای گیتس» نشان داد که سردبیر دست‌کم نود درصد مطالب دریافتی از خبرگزاری را حذف می‌کند و همین گزینش، تصویری از جهان می‌سازد که با واقعیت فاصله دارد. "
                 "در چارچوب قدرت ارتباطی، کاستلز (۲۰۰۹) یادآوری می‌کند که دروازه‌بانی امروز تنها عمل ویراستار نیست؛ کنشگرانی که شبکه‌های ارتباطی را برنامه‌نویسی می‌کنند و گره‌ها را به هم وصل یا از هم جدا می‌کنند، قدرت تعیین اولویت‌های خبری را در دست دارند. "
                 "در رسانه‌های پلتفرمی، سنجه‌های تعامل، سرویس‌های شخصی‌سازی و الزامات بهینه‌سازی جست‌وجو به دروازه‌بانان تازه‌ای بدل شده‌اند که معیارهای خبری سنتی را با منطق توجه ترکیب می‌کنند."),
        mechanism=(" در عمل، دروازه‌بانی فرایندی بازگشتی است: بازخورد مخاطب و داده‌های مصرف، انتظارات تحریریه را تغییر می‌دهد و در دور بعدی گزینش، همان داده‌ها به معیار تبدیل می‌شوند. "
                   "گزینش خبر همچنین تابع رقابت میان رسانه‌هاست؛ رسانه‌ای که دیرتر منتشر کند، با وجود کیفیت بالاتر، ممکن است از گردش خبر حذف شود. "
                   "این وابستگی متقابل نشان می‌دهد که مرز میان دروازه‌بان و مخاطب در محیط دیجیتال سیال است و کنترل جریان اطلاعات به شکل شبکه‌ای توزیع شده است."),
        principles=[
            "گزینش خبر، پیش از انتشار و در چند گلوگاه رخ می‌دهد.",
            "معیارهای خبری، حاصل تعامل ارزش‌های حرفه‌ای و فشار سازمانی‌اند.",
            "دروازه‌بانی الگوریتمی، معیارهای انسانی را با منطق تعامل ترکیب می‌کند.",
            "مخاطب با اشتراک‌گذاری و بازنشر، خود به دروازه‌بان ثانویه بدل می‌شود.",
        ],
    ),
    "MC-016": dict(
        summary=(" کاستلز در «قدرت ارتباطات» (۲۰۰۹) استدلال می‌کند که قدرت در جامعهٔ شبکه‌ای از دو راه اعمال می‌شود: برنامه‌نویسی شبکه‌ها، یعنی تعریف قواعد و کدهای فرهنگی که شبکه بر پایهٔ آن‌ها کار می‌کند، و جابه‌جایی گره‌ها، یعنی وصل کردن یا برکندن پیوند میان شبکه‌ها. "
                 "بدین ترتیب، قدرت ارتباطی توانایی شکل دادن به ذهن‌ها از راه ساخت معناست و نه فقط کنترل ابزار تولید. "
                 "مفهوم «خودارتباطی انبوه» نیز نشان می‌دهد که کاربران با ترکیب پلتفرم‌های توزیع انبوه و تولید خودمختار محتوا، هم پیام‌رسان و هم دریافت‌کننده‌اند و می‌توانند در برابر قدرت برنامه‌نویسی شبکه، «ضدقدرت» بسازند."),
        mechanism=(" این سازوکار با تقابل «فضای جریان‌ها» و «فضای مکان‌ها» فهمیدنی‌تر می‌شود: فعالیت‌های اقتصادی، سیاسی و نمادین در جریان‌های فرامرزی سازمان می‌یابند، در حالی که تجربهٔ روزمره هنوز در مکان ریشه دارد. "
                   "زمان نیز در شبکه «بی‌زمان» می‌شود؛ خبر، سرمایه و نمادها هم‌زمان در چند نقطه حضور دارند. "
                   "نتیجهٔ این آرایش، همگرایی فزایندهٔ فناوری، نابرابری‌های تازه در دسترسی به شبکه و بازتعریف هویت جمعی بر پایهٔ پیوندهای شبکه‌ای است."),
        principles=[
            "شبکه، واحد بنیادین سازمان‌دهی اجتماعی در جامعهٔ معاصر است.",
            "قدرت از راه برنامه‌نویسی شبکه و جابه‌جایی گره‌ها اعمال می‌شود.",
            "خودارتباطی انبوه، امکان ضدقدرت شبکه‌ای را فراهم می‌کند.",
            "فضای جریان‌ها بر سازمان اقتصادی و نمادین چیره می‌شود.",
        ],
    ),
    "MC-017": dict(
        summary=(" وبستر (۲۰۰۶) نشان می‌دهد که «جامعهٔ اطلاعاتی» یک برچسب یکپارچه نیست و دست‌کم پنج خوانش فناورانه، اقتصادی، حرفه‌ای، فضایی و فرهنگی از آن وجود دارد که هر یک شاخص سنجش متفاوتی می‌سازد. "
                 "همین تعدد تعریف، خطر آن را دارد که سیاست‌گذاران تغییرات جزئی را به «گذار تاریخی» تعبیر کنند. "
                 "بنابراین، ارزش تحلیلی نظریهٔ بل بیشتر در پرسش‌های آن دربارهٔ جایگاه دانش نظری نهفته است تا در پیش‌بینی قطعی مسیر آینده."),
        principles=[
            "دانش نظری، محور بازسازمان‌دهی جامعهٔ پساصنعتی است.",
            "گذار از تولید کالا به خدمات، ساختار شغلی را دگرگون می‌کند.",
            "سنجش جامعهٔ اطلاعاتی به شاخص انتخابی وابسته است.",
            "پیش‌بینی تحول اجتماعی باید محدودیت‌های خود را آشکار کند.",
        ],
    ),
    "MC-020": dict(
        summary=(" سرل (۱۹۹۵) این خط فکری را با تفکیک «واقعیت‌های خام» از «واقعیت‌های نهادی» دقیق‌تر می‌کند: واقعیت‌های خام مستقل از انسان وجود دارند، حال آن‌که واقعیت‌های نهادی بر «قصد جمعی» و قواعد سازندهٔ «ایکس در بافت سی همچون ایگر شمرده می‌شود» استوارند. "
                 "پول، مالکیت و منصب نمونه‌هایی از کارکردهای منزلتی‌اند که تنها تا زمانی دوام می‌آورند که جمع به آن‌ها باور داشته باشد. "
                 "این تفکیک نشان می‌دهد که ساخت اجتماعی واقعیت، انکار جهان مادی نیست، بلکه توضیح لایهٔ نهادی‌ای است که بر آن سوار می‌شود."),
        principles=[
            "واقعیت روزمره در تعامل اجتماعی ساخته و بازتولید می‌شود.",
            "زبان، ابزار اصلی عینی‌سازی تجربه و انتقال معناست.",
            "نهادها با عادت‌واره شدن کنش، ثبات و مشروعیت می‌یابند.",
            "واقعیت نهادی به قصد جمعی و پذیرش همگانی وابسته است.",
        ],
    ),
    "MC-023": dict(
        summary=(" آزمون کلاسیک فستینگر و کارلاسمیت (۱۹۵۹) در موقعیت «اطاعت اجباری»، این پیش‌بینی را تأیید کرد: شرکت‌کنندگانی که در برابر پاداش ناچیز دربارهٔ کاری خسته‌کننده سخن گفته بودند، نگرش مثبت‌تری به آن پیدا کردند؛ زیرا پاداش اندک، توجیه کافی برای دروغ نمی‌ساخت و تغییر نگرش، تنها راه کاهش تنش بود. "
                 "این یافته نشان داد که شدت ناهماهنگی به اهمیت شناخت‌ها، شمار گزینه‌های ناهمخوان و ادراک آزادی انتخاب بستگی دارد."),
        principles=[
            "شناخت‌های ناهمخوان، تنش روانی می‌سازند.",
            "فرد برای کاهش تنش، شناخت یا رفتار را تغییر می‌دهد.",
            "توجیه ناکافی، تغییر نگرش را بیشتر می‌کند.",
            "ادراک آزادی انتخاب، شدت ناهماهنگی را تعیین می‌کند.",
        ],
    ),
    "MC-024": dict(
        summary=(" مادوکس و راجرز (۱۹۸۳) با افزودن «خودکارآمدی» به‌عنوان مؤلفهٔ چهارم، مدل را بازنگری کردند و نشان دادند که باور فرد به توانایی انجام پاسخ، جدا از کارآمدی خود پاسخ، بر قصد محافظتی اثر می‌گذارد. "
                 "در این نسخه، ارزیابی مقابله دو بخش دارد: کارآمدی پاسخ و خودکارآمدی. "
                 "همچنین پژوهش‌ها نشان داده‌اند که ترس شدید بدون راهکار مقابلهٔ روشن، به «مقابلهٔ ناسازگار» مانند اجتناب، انکار یا خوش‌بینی کاذب می‌انجامد؛ سازوکاری که در کمپین‌های سلامت اهمیت عملی دارد."),
        principles=[
            "پیام ترس، ارزیابی تهدید و مقابله را فعال می‌کند.",
            "شدت و احتمال تهدید، انگیزهٔ محافظت را شکل می‌دهند.",
            "کارآمدی پاسخ و خودکارآمدی، هر دو لازم‌اند.",
            "ترس بدون راهکار مقابله، به اجتناب می‌انجامد.",
        ],
    ),
    "MC-025": dict(
        summary=(" مک‌گوایر (۱۹۶۱) با آزمایش «تلقین» نشان داد که پیش‌درمانی ضعیف‌شده، مقاومت در برابر پیام‌های بعدی را افزایش می‌دهد، به‌ویژه وقتی مخاطب خود در تولید ضداستدلال فعال شود. "
                 "کامپتون و فاو (۲۰۰۵) در مرور بلوغ نظریه، سازوکار را در دو مؤلفه خلاصه می‌کنند: «تهدید» که ضرورت دفاع را فعال می‌کند و «پیش‌درمانی ردّی» که نمونهٔ استدلال‌های مقابل را پیشاپیش تمرین می‌دهد. "
                 "این دو با هم، نه فقط آگاهی، بلکه مهارت شناختی دفاع می‌سازند."),
        principles=[
            "مقاومت در برابر متقاعدسازی، آموختنی است.",
            "هشدار نسبت به تهدید قریب‌الوقوع، انگیزهٔ دفاع می‌سازد.",
            "ردّ ضعیف‌شدهٔ استدلال مقابل، پادتن شناختی می‌سازد.",
            "تولید فعال ضداستدلال، مقاومت پایدارتری ایجاد می‌کند.",
            "اثر تلقیح با گذر زمان و تغییر بافت، تضعیف می‌شود.",
        ],
    ),
    "MC-027": dict(
        summary=(" ریشهٔ مدل به نظریهٔ عمل بازمی‌گردد که فیش‌بین و آجزن (۱۹۷۵) آن را صورت‌بندی کردند: رفتار تابع نیت است و نیت از نگرش نسبت به رفتار و هنجار ذهنی ساخته می‌شود. "
                 "آجزن (۱۹۹۱) با افزودن کنترل رفتار ادراک‌شده، نظریه را برای رفتارهایی گسترد که انجامشان کاملاً ارادی نیست. "
                 "در سنجش، دو سطح متمایزند: سنجش مستقیم سازه‌ها و سنجش باورمحور که نگرش، هنجار و کنترل را از باورهای زیربنایی بازمی‌سازد. "
                 "پشتیبانی فراتحلیلی گسترده، این مدل را به یکی از پرکاربردترین چارچوب‌های پیش‌بینی رفتار بدل کرده است، هرچند شکاف نیت-رفتار و نقش عادت همچنان موضوع نقد است."),
        mechanism=(" سه عامل، وزن یکسانی ندارند: در رفتارهایی که کنترل واقعی بالاست، کنترل ادراک‌شده می‌تواند مستقیماً رفتار را پیش‌بینی کند و در رفتارهای هنجارمحور، هنجار ذهنی وزن بیشتری می‌گیرد. "
                   "اندازه‌گیری سازه‌ها نیز باید از نظر بافت، کنش، هدف و زمان هم‌خوان باشد؛ ناهم‌خوانی این چهار عنصر، پیش‌بینی را ضعیف می‌کند. "
                   "همچنین نیت هنگامی به رفتار تبدیل می‌شود که فرصت عمل و برنامهٔ اجرایی وجود داشته باشد؛ همین شکاف، توضیح‌دهندهٔ بخشی از نقدهای تجربی است."),
        principles=[
            "نیت، نزدیک‌ترین تعیین‌کنندهٔ رفتار ارادی است.",
            "نگرش، هنجار ذهنی و کنترل ادراک‌شده، نیت را می‌سازند.",
            "کنترل ادراک‌شده می‌تواند مستقیماً رفتار را پیش‌بینی کند.",
            "سازه‌ها باید در سطح باور و در سطح کلی سنجیده شوند.",
            "هم‌خوانی بافت، کنش، هدف و زمان، شرط پیش‌بینی معتبر است.",
        ],
    ),
    "MC-030": dict(
        summary=(" بریم و بریم (۱۹۸۱) نظریه را به روابط میان‌فردی و بافت‌های بالینی گستردند و نشان دادند که شدت واکنش به اهمیت آزادی تهدیدشده، شمار آزادی‌های در خطر و ادراک مشروعیت تهدید بستگی دارد. "
                 "وقتی تهدید نامشروع و آزادی مهم باشد، اثر متناقض یا «اثر بومرنگ» آشکارتر می‌شود. "
                 "همچنین واکنش می‌تواند به شکل بازسازی آزادی در حوزه‌ای دیگر ظاهر شود؛ مثلاً مخاطبی که از انتخاب یک برند منع می‌شود، برند رقیب را با جذابیت بیشتری برمی‌گزیند."),
        principles=[
            "تهدید آزادی، انگیزهٔ بازیابی آن را فعال می‌کند.",
            "اهمیت آزادی و شمار آزادی‌های تهدیدشده، شدت واکنش را تعیین می‌کنند.",
            "تهدید نامشروع، واکنش شدیدتری برمی‌انگیزد.",
            "واکنش می‌تواند به اثر بومرنگ و انتخاب گزینهٔ مقابل بینجامد.",
        ],
    ),
}

NAME_FIX = {}
YEAR_FIX = {}
