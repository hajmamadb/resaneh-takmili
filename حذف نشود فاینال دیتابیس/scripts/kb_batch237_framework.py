# -*- coding: utf-8 -*-
"""Batch 237: THEORY cards 248, 322, 323, 388, 391, 430, 456, 90."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch237-20261117"
NOW = "2026-11-17 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch237.json"

BURGOON78 = dict(kind="JOURNAL_ARTICLE", title_en="A Communication Model of Personal Space Violations: Explication and an Initial Test",
                 title_fa="مدلی ارتباطی برای نقض حریم شخصی: تبیین و آزمون اولیه",
                 authors="Judee K. Burgoon", year=1978, publisher="Human Communication Research",
                 doi="10.1111/j.1468-2958.1978.tb00603.x",
                 url="https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1468-2958.1978.tb00603.x",
                 language="en", isbn=None,
                 citation="Burgoon, J. K. (1978). A communication model of personal space violations: Explication and an initial test. Human Communication Research, 4(2), 129-142.",
                 locator="4(2), 129-142", locator_type="PAGE",
                 supports="expectancy, violation, arousal and communicator reward valence", verified=True)

BURGOON93 = dict(kind="JOURNAL_ARTICLE", title_en="Interpersonal Expectations, Expectancy Violations, and Emotional Communication",
                 title_fa="انتظارات میان‌فردی، نقض انتظار و ارتباط هیجانی",
                 authors="Judee K. Burgoon", year=1993, publisher="Journal of Language and Social Psychology",
                 doi="10.1177/0261927X93121003",
                 url="https://journals.sagepub.com/doi/abs/10.1177/0261927x93121003",
                 language="en", isbn=None,
                 citation="Burgoon, J. K. (1993). Interpersonal expectations, expectancy violations, and emotional communication. Journal of Language and Social Psychology, 12(1-2), 30-48.",
                 locator="12(1-2), 30-48", locator_type="PAGE",
                 supports="extension of expectancy violations theory to emotional communication", verified=True)

HEIDER46 = dict(kind="JOURNAL_ARTICLE", title_en="Attitudes and Cognitive Organization",
                title_fa="نگرش‌ها و سازمان شناختی",
                authors="Fritz Heider", year=1946, publisher="The Journal of Psychology",
                doi="10.1080/00223980.1946.9917275",
                url="https://www.tandfonline.com/doi/abs/10.1080/00223980.1946.9917275",
                language="en", isbn=None,
                citation="Heider, F. (1946). Attitudes and cognitive organization. The Journal of Psychology, 21(1), 107-112.",
                locator="21(1), 107-112", locator_type="PAGE",
                supports="P-O-X triad and balanced/imbalanced cognitive configurations", verified=True)

HEIDER58 = dict(kind="BOOK", title_en="The Psychology of Interpersonal Relations",
                title_fa="روان‌شناسی روابط میان‌فردی",
                authors="Fritz Heider", year=1958, publisher="Wiley",
                doi=None,
                url="http://cipra.cl/biblioteca/heider/1958-FritzHeider-ThePsychologyofInterpersonalRelations.pdf",
                language="en", isbn=None,
                citation="Heider, F. (1958). The Psychology of Interpersonal Relations. New York: Wiley.",
                locator="book", locator_type="BOOK",
                supports="balance theory developed within a general theory of interpersonal relations", verified=True)

BREHM66 = dict(kind="BOOK", title_en="A Theory of Psychological Reactance",
               title_fa="نظریهٔ واکنش روانی",
               authors="Jack W. Brehm", year=1966, publisher="Academic Press",
               doi=None,
               url="https://psycnet.apa.org/record/1967-08061-000",
               language="en", isbn=None,
               citation="Brehm, J. W. (1966). A Theory of Psychological Reactance. New York: Academic Press.",
               locator="book", locator_type="BOOK",
               supports="freedoms, threats to freedom and reactance motivation", verified=True)

BREHM81 = dict(kind="BOOK", title_en="Psychological Reactance: A Theory of Freedom and Control",
               title_fa="واکنش روانی: نظریهٔ آزادی و کنترل",
               authors="Sharon S. Brehm; Jack W. Brehm", year=1981, publisher="Academic Press",
               doi=None,
               url="https://archive.org/details/psychologicalrea0000breh",
               language="en", isbn=None,
               citation="Brehm, S. S., & Brehm, J. W. (1981). Psychological Reactance: A Theory of Freedom and Control. New York: Academic Press.",
               locator="book", locator_type="BOOK",
               supports="determinants of reactance magnitude and freedom restoration", verified=True)

SCHULTZ61 = dict(kind="JOURNAL_ARTICLE", title_en="Investment in Human Capital",
                 title_fa="سرمایه‌گذاری در سرمایهٔ انسانی",
                 authors="Theodore W. Schultz", year=1961, publisher="The American Economic Review",
                 doi=None,
                 url="https://la.utexas.edu/users/hcleaver/330T/350kPEESchultzInvestmentHumanCapital.pdf",
                 language="en", isbn=None,
                 citation="Schultz, T. W. (1961). Investment in human capital. The American Economic Review, 51(1), 1-17.",
                 locator="51(1), 1-17", locator_type="PAGE",
                 supports="education, training and health as productive investment", verified=True)

BECKER64 = dict(kind="BOOK", title_en="Human Capital: A Theoretical and Empirical Analysis, with Special Reference to Education",
                title_fa="سرمایهٔ انسانی: تحلیلی نظری و تجربی با تأکید بر آموزش",
                authors="Gary S. Becker", year=1964, publisher="National Bureau of Economic Research / Columbia University Press",
                doi=None,
                url="https://www.nber.org/books-and-chapters/human-capital-theoretical-and-empirical-analysis-special-reference-education-first-edition",
                language="en", isbn=None,
                citation="Becker, G. S. (1964). Human Capital: A Theoretical and Empirical Analysis, with Special Reference to Education. New York: National Bureau of Economic Research.",
                locator="book", locator_type="BOOK",
                supports="rates of return to schooling and on-the-job training", verified=True)

MCGREGOR60 = dict(kind="BOOK", title_en="The Human Side of Enterprise",
                  title_fa="وجه انسانی سازمان",
                  authors="Douglas McGregor", year=1960, publisher="McGraw-Hill",
                  doi=None,
                  url="https://web.mit.edu/curhan/www/docs/Articles/15341_Readings/Motivation/McGregor_The_Human_Side_of_Enterprise.pdf",
                  language="en", isbn=None,
                  citation="McGregor, D. (1960). The Human Side of Enterprise. New York: McGraw-Hill.",
                  locator="book", locator_type="BOOK",
                  supports="Theory X and Theory Y assumptions about workers", verified=True)

MCGREGOR66 = dict(kind="BOOK", title_en="Leadership and Motivation: Essays of Douglas McGregor",
                  title_fa="رهبری و انگیزش: مقالات داگلاس مک‌گرگور",
                  authors="Douglas McGregor; Warren G. Bennis; Edgar H. Schein (Eds.)", year=1966, publisher="MIT Press",
                  doi=None,
                  url="https://mitpress.mit.edu/9780262630153/leadership-and-motivation/",
                  language="en", isbn="9780262630153",
                  citation="McGregor, D. (1966). Leadership and Motivation: Essays of Douglas McGregor (W. G. Bennis & E. H. Schein, Eds.). Cambridge, MA: MIT Press.",
                  locator="book", locator_type="BOOK",
                  supports="managerial assumptions, leadership and motivation essays", verified=True)

RHEINGOLD93 = dict(kind="BOOK", title_en="The Virtual Community: Homesteading on the Electronic Frontier",
                   title_fa="جامعهٔ مجازی: خانه‌سازی در مرز الکترونیکی",
                   authors="Howard Rheingold", year=1993, publisher="Addison-Wesley",
                   doi=None,
                   url="https://direct.mit.edu/books/book/2147/The-Virtual-CommunityHomesteading-on-the",
                   language="en", isbn=None,
                   citation="Rheingold, H. (1993). The Virtual Community: Homesteading on the Electronic Frontier. Reading, MA: Addison-Wesley.",
                   locator="book", locator_type="BOOK",
                   supports="online networks as communities with norms, support and identity", verified=True)

WELLMAN01 = dict(kind="JOURNAL_ARTICLE", title_en="Physical Place and Cyberplace: The Rise of Personalized Networking",
                 title_fa="مکان فیزیکی و فضای سایبری: ظهور شبکه‌سازی شخصی‌شده",
                 authors="Barry Wellman", year=2001, publisher="International Journal of Urban and Regional Research",
                 doi=None,
                 url="https://www.ijurr.org/article/physical-place-and-cyberplace-the-rise-of-personalized-networking/",
                 language="en", isbn=None,
                 citation="Wellman, B. (2001). Physical place and cyberplace: The rise of personalized networking. International Journal of Urban and Regional Research, 25(2), 227-252.",
                 locator="25(2), 227-252", locator_type="PAGE",
                 supports="networked individualism and community beyond physical place", verified=True)

STEPHENSON67 = dict(kind="BOOK", title_en="The Play Theory of Mass Communication",
                    title_fa="نظریهٔ بازی در ارتباطات جمعی",
                    authors="William Stephenson", year=1967, publisher="University of Chicago Press",
                    doi=None,
                    url="https://books.google.com/books/about/The_Play_Theory_of_Mass_Communication.html?id=LJthAAAAMAAJ",
                    language="en", isbn=None,
                    citation="Stephenson, W. (1967). The Play Theory of Mass Communication. Chicago: University of Chicago Press.",
                    locator="book", locator_type="BOOK",
                    supports="mass communication as subjective play and communication-pleasure", verified=True)

BRYANT09 = dict(kind="BOOK", title_en="Media Effects: Advances in Theory and Research",
                title_fa="اثرات رسانه: پیشرفت‌ها در نظریه و پژوهش",
                authors="Jennings Bryant; Mary Beth Oliver (Eds.)", year=2009, publisher="Routledge",
                doi="10.4324/9780203877111",
                url="https://www.taylorfrancis.com/books/edit/10.4324/9780203877111/media-effects-jennings-bryant-mary-beth-oliver",
                language="en", isbn=None,
                citation="Bryant, J., & Oliver, M. B. (Eds.). (2009). Media Effects: Advances in Theory and Research (3rd ed.). New York: Routledge.",
                locator="book", locator_type="BOOK",
                supports="situates play and entertainment traditions within media effects research", verified=True)

PINCH84 = dict(kind="JOURNAL_ARTICLE", title_en="The Social Construction of Facts and Artefacts",
               title_fa="ساخت اجتماعی واقعیت‌ها و مصنوعات",
               authors="Trevor J. Pinch; Wiebe E. Bijker", year=1984, publisher="Social Studies of Science",
               doi="10.1177/030631284014003004",
               url="https://journals.sagepub.com/doi/10.1177/030631284014003004",
               language="en", isbn=None,
               citation="Pinch, T. J., & Bijker, W. E. (1984). The social construction of facts and artefacts: Or how the sociology of science and the sociology of technology might benefit each other. Social Studies of Science, 14(3), 399-441.",
               locator="14(3), 399-441", locator_type="PAGE",
               supports="interpretive flexibility, relevant social groups, closure and stabilization", verified=True)

BIJKER95 = dict(kind="BOOK", title_en="Of Bicycles, Bakelites, and Bulbs: Toward a Theory of Sociotechnical Change",
                title_fa="از دوچرخه و باکلیت تا لامپ: به سوی نظریه‌ای برای تغییر اجتماعی-فنی",
                authors="Wiebe E. Bijker", year=1995, publisher="MIT Press",
                doi=None,
                url="https://mitpress.mit.edu/9780262522274/of-bicycles-bakelites-and-bulbs/",
                language="en", isbn="9780262522274",
                citation="Bijker, W. E. (1995). Of Bicycles, Bakelites, and Bulbs: Toward a Theory of Sociotechnical Change. Cambridge, MA: MIT Press.",
                locator="book", locator_type="BOOK",
                supports="sociotechnical change through case studies of bicycle, Bakelite and lamp", verified=True)

S = {
    "card-248": [BURGOON78, BURGOON93],
    "card-322": [HEIDER46, HEIDER58],
    "card-323": [BREHM66, BREHM81],
    "card-388": [SCHULTZ61, BECKER64],
    "card-391": [MCGREGOR60, MCGREGOR66],
    "card-430": [RHEINGOLD93, WELLMAN01],
    "card-456": [STEPHENSON67, BRYANT09],
    "card-90": [PINCH84, BIJKER95],
}

ENRICH = {
    "card-248": dict(
        level="میانی",
        related_approaches="نظریهٔ تعادل نیوکامب؛ نظریهٔ واکنش روانی؛ تطبیق میان‌فردی؛ ارتباط غیرکلامی؛ مدیریت برداشت در شبکه‌های اجتماعی.",
        recommended_sources="«مدلی ارتباطی برای نقض حریم شخصی» (بورگون، ۱۹۷۸)؛ «انتظارات میان‌فردی و ارتباط هیجانی» (بورگون، ۱۹۹۳).",
        summary=("نظریهٔ نقض انتظار توضیح می‌دهد که افراد بر پایهٔ هنجارهای اجتماعی و تجربهٔ پیشین، انتظاراتی از رفتار ارتباطی دیگران می‌سازند و وقتی این انتظارات نقض می‌شوند، توجه و برانگیختگی ایجاد می‌شود. "
                 "بورگون (۱۹۷۸) این سازوکار را در پژوهش حریم شخصی صورت‌بندی کرد: نقض انتظار خودبه‌خود بد نیست؛ ارزش نهایی آن به ارزش پاداش ارتباط‌گر و تفسیر مخاطب بستگی دارد. "
                 "بورگون (۱۹۹۳) نظریه را به ارتباط هیجانی گسترد و نشان داد که نقض‌های مثبت می‌توانند جذابیت و اعتماد را افزایش دهند، در حالی که نقض‌های منفی از سوی فرستندهٔ کم‌ارزش، فاصله و بی‌اعتمادی می‌سازند. "
                 "در این نظریه، انتظار، نقض، برانگیختگی، تفسیر و ارزیابی، زنجیرهٔ اصلی تحلیل‌اند. "
                 "نقد اصلی، وابستگی فرهنگی انتظارات، سنجش ذهنی ارزش پاداش و دشواری پیش‌بینی نقض‌های مبهم است. در عمل، نظریه چارچوب مفیدی برای تحلیل لحن برند، ارتباط بحران و واکنش مخاطب به رفتار غیرمنتظرهٔ سازمان است."),
        definition="نظریهٔ نقض انتظار، تأثیر نقض انتظارات ارتباطی بر توجه، برانگیختگی و ارزیابی مخاطب را بر پایهٔ هنجارها و ارزش پاداش ارتباط‌گر تبیین می‌کند.",
        main_problem="چرا برخی نقض‌های انتظار واکنش مثبت و برخی واکنش منفی برمی‌انگیزند و چه عاملی ارزش نهایی نقض را تعیین می‌کند؟",
        mechanism=("مخاطب بر پایهٔ هنجارهای موقعیت و تجربهٔ پیشین، انتظاری از رفتار ارتباط‌گر می‌سازد. "
                   "اگر رفتار مشاهده‌شده با انتظار فاصله بگیرد، توجه به رفتار و برانگیختگی افزایش می‌یابد. "
                   "مخاطب سپس معنای نقض را تفسیر می‌کند و آن را با ارزش پاداش ارتباط‌گر می‌سنجد. "
                   "بورگون (۱۹۷۸) نشان داد که نقض از سوی ارتباط‌گر پاداش‌دهنده می‌تواند پیامد مثبت‌تری از همرنگی بی‌اثر بسازد و بورگون (۱۹۹۳) این منطق را به هیجان و صمیمیت گسترد. "
                   "ارزش پاداش، شامل جذابیت، اعتبار و منافع رابطه است. "
                   "در نتیجه، یک رفتار یکسان از دو فرستندهٔ متفاوت، دو ارزیابی متفاوت می‌گیرد و همین، نظریه را از مدل‌های سادهٔ همرنگی جدا می‌کند."),
        assumptions=[
            "افراد انتظارات ارتباطی هنجاری دارند.",
            "نقض انتظار، توجه و برانگیختگی می‌سازد.",
            "ارزش پاداش ارتباط‌گر، تفسیر نقض را جهت می‌دهد.",
            "نقض، همیشه منفی نیست.",
        ],
        principles=[
            "انتظار، از هنجار و تجربه ساخته می‌شود.",
            "نقض، ارزیابی را به تعویق می‌اندازد.",
            "ارتباط‌گر پاداش‌دهنده، نقض مثبت می‌سازد.",
            "بافت فرهنگی، انتظار را تعیین می‌کند. تفسیر، پیش از داوری می‌آید.",
        ],
        critiques=[
            "انتظارات، وابسته به فرهنگ و موقعیت‌اند.",
            "سنجش ارزش پاداش، ذهنی و دشوار است.",
            "نقض‌های مبهم، پیش‌بینی را پیچیده می‌کنند.",
            "نظریه بیشتر میان‌فردی است و تعمیم آن به رسانه نیازمند احتیاط است.",
            "عوامل شخصیتی و رابطهٔ پیشین، کم‌رنگ می‌مانند. اثر بلندمدت نقض، کمتر سنجیده شده است.",
        ],
        applications=[
            "تحلیل لحن برند در شبکه‌های اجتماعی.",
            "طراحی پاسخ غیرمنتظرهٔ سازمان در بحران.",
            "آموزش ارتباط غیرکلامی و حریم شخصی.",
            "تحلیل رابطهٔ استاد و دانشجو.",
            "طراحی تجربهٔ چت‌بات و عامل هوشمند.",
            "پژوهش اقناع و اعتماد.",
            "تحلیل تبلیغات طنزآمیز.",
            "طراحی کمپین شگفتی.",
            "ارزیابی واکنش به سخنرانی. تحلیل ارتباط بین‌فرهنگی.",
        ],
        evolution=("نظریه در ۱۹۷۸ از پژوهش حریم شخصی و انتظارات غیرکلامی برخاست. "
                   "بورگون (۱۹۷۸) مدل اولیه را آزمود و بورگون (۱۹۹۳) آن را به هیجان و صمیمیت گسترد. "
                   "در دههٔ ۱۹۹۰، پژوهش تطبیق میان‌فردی، نقض را در جریان تعامل جای داد. "
                   "در دههٔ ۲۰۱۰، عامل‌های گفت‌وگویی و ربات‌های اجتماعی، میدان تازه‌ای برای آزمون نظریه ساختند. "
                   "امروز، نظریه با طراحی تجربه، شخصی‌سازی و انتظارات پلتفرمی گره خورده است."),
        key_concepts=[
            {"term_en": "Expectancy", "term_fa": "انتظار", "definition": "پیش‌بینی رفتار دیگران بر پایهٔ هنجارهای موقعیت و تجربهٔ پیشین."},
            {"term_en": "Expectancy Violation", "term_fa": "نقض انتظار", "definition": "فاصلهٔ رفتار مشاهده‌شده از انتظار مخاطب که توجه و برانگیختگی می‌سازد."},
            {"term_en": "Communicator Reward Valence", "term_fa": "ارزش پاداش ارتباط‌گر", "definition": "ارزش مثبت یا منفی فرستنده در نظر مخاطب که تفسیر نقض را جهت می‌دهد."},
            {"term_en": "Arousal", "term_fa": "برانگیختگی", "definition": "افزایش هوشیاری و توجه پس از نقض که پردازش تفسیری را فعال می‌کند."},
            {"term_en": "Personal Space", "term_fa": "حریم شخصی", "definition": "فاصلهٔ فیزیکی و روانی مورد انتظار در تعامل که نقض آن پیام ارتباطی می‌سازد."},
        ],
        theorists=[{"role": "بنیان‌گذار نظریه", "name_en": "Judee K. Burgoon", "name_fa": "جودی بورگون"}],
        model={"elements": ["هنجار و تجربه", "انتظار", "نقض", "برانگیختگی", "ارزش پاداش", "تفسیر", "ارزیابی و پیامد"],
               "description": "هنجارها انتظار می‌سازند؛ نقض، برانگیختگی و تفسیر را فعال می‌کند؛ ارزش پاداش ارتباط‌گر، ارزیابی نهایی را جهت می‌دهد."},
        mapping={"entity_type": "THEORY", "content_type": "نظریه (Theory)", "needs_review": False},
        studies=[
            {"citation": "بورگون (۱۹۷۸)، آزمون اولیهٔ مدل نقض حریم شخصی", "findings": "نقض از سوی ارتباط‌گر پاداش‌دهنده پیامد مثبت‌تری از همرنگی ساخت؛ مدل اولیه تأیید شد."},
            {"citation": "بورگون (۱۹۹۳)، تبیین نظریه و کاربرد در ارتباط هیجانی", "findings": "نقض مثبت می‌تواند صمیمیت و جذابیت را افزایش دهد و هیجان، ارزیابی نقض را تعدیل می‌کند."},
        ],
        example_text="برندی که معمولاً لحن رسمی دارد، در یک کمپین با طنز خودمانی ظاهر می‌شود؛ مخاطب علاقه‌مند این نقض را مثبت می‌خواند، اما همان رفتار از نهادی دولتی، نقض منفی تلقی می‌شود.",
        critique_text="۱. انتظارات فرهنگی و موقعیتی‌اند و تعمیم یکسان را محدود می‌کنند. ۲. سنجش ارزش پاداش ذهنی است. ۳. نقض‌های مبهم پیش‌بینی را دشوار می‌کنند. ۴. تعمیم نظریهٔ میان‌فردی به رسانه نیازمند احتیاط است.",
    ),
    "card-322": dict(
        level="پایه",
        related_approaches="نظریهٔ تعادل نیوکامب؛ ناهماهنگی شناختی فستینگر؛ نظریهٔ شبکه؛ تبلیغات تأییدی؛ ارتباط میان‌فردی.",
        recommended_sources="«نگرش‌ها و سازمان شناختی» (هایدر، ۱۹۴۶)؛ «روان‌شناسی روابط میان‌فردی» (هایدر، ۱۹۵۸).",
        summary=("نظریهٔ توازن بر این اصل استوار است که انسان‌ها به ثبات و هماهنگی در روابط شناختی و اجتماعی خود گرایش دارند. "
                 "هایدر (۱۹۴۶) مدل سه‌گانهٔ P-O-X را معرفی کرد: فرد (P)، شخص دیگر (O) و موضوع یا نگرش (X). "
                 "اگر روابط میان این سه عنصر متوازن باشد، حالت روانی خوشایند می‌ماند؛ اگر ناتوازن شود، تنش شناختی ایجاد می‌شود و فرد می‌کوشد با تغییر نگرش، تغییر رابطه یا بازتفسیر موقعیت، توازن را بازگرداند. "
                 "هایدر (۱۹۵۸) نظریه را در چارچوب گسترده‌تر روان‌شناسی روابط میان‌فردی بسط داد و به احساسات، واحدها و روابط علّی پیوند زد. "
                 "در این نظریه، توازن، ناتوازن، شدت رابطه و جهت تغییر، سازه‌های اصلی‌اند. "
                 "نقد اصلی، پیش‌بینی‌نکردن جهت و میزان تغییر، سادگی روابط دوقطبی و نادیده‌گرفتن شدت نگرش است. در عمل، نظریه چارچوب مفیدی برای تحلیل تأیید Celebrity، تبلیغات سیاسی و هم‌راستایی رسانه و مخاطب است."),
        definition="نظریهٔ توازن، گرایش انسان به هماهنگی در سه‌گانهٔ فرد، شخص دیگر و موضوع را تبیین می‌کند و ناتوازن را محرک تغییر نگرش یا رابطه می‌داند.",
        main_problem="چگونه ناسازگاری میان نگرش فرد، نگرش شخص دیگر و نگرش به یک موضوع، تنش می‌سازد و فرد چگونه آن را کاهش می‌دهد؟",
        mechanism=("فرد سه عنصر را در ذهن دارد: خود، شخص دیگر و موضوع. "
                   "هر رابطه مثبت یا منفی است. "
                   "اگر حاصل‌ضرب نشانه‌ها مثبت باشد، سه‌گانه متوازن است و فشار تغییر کم می‌شود. "
                   "اگر حاصل‌ضرب منفی باشد، تنش ایجاد می‌شود. "
                   "هایدر (۱۹۴۶) نشان داد که فرد برای بازگرداندن توازن، یکی از رابطه‌ها را تغییر می‌دهد: نگرش خود را اصلاح می‌کند، ارزیابی شخص دیگر را تغییر می‌دهد یا موضوع را بازتفسیر می‌کند. "
                   "هایدر (۱۹۵۸) این سازوکار را به احساسات و واحدهای ادراکی پیوند زد. "
                   "شدت رابطه و اهمیت موضوع، میزان فشار را تعیین می‌کند. "
                   "در تبلیغات، چهرهٔ محبوب با محصول پیوند می‌خورد تا نگرش مثبت به محصول منتقل شود."),
        assumptions=[
            "انسان به هماهنگی شناختی گرایش دارد.",
            "ناتوازن، تنش روانی می‌سازد.",
            "روابط را می‌توان مثبت یا منفی خواند.",
            "فرد برای کاهش تنش، نگرش یا رابطه را تغییر می‌دهد.",
        ],
        principles=[
            "توازن، حالت خوشایند است.",
            "ناتوازن، محرک تغییر است.",
            "شدت رابطه، فشار تغییر را تعیین می‌کند.",
            "تغییر، کم‌هزینه‌ترین مسیر را می‌جوید. بازتفسیر، پیش از تغییر نگرش می‌آید.",
        ],
        critiques=[
            "جهت و میزان تغییر را پیش‌بینی نمی‌کند.",
            "روابط دوقطبی، شدت نگرش را نادیده می‌گیرد.",
            "تعامل چندجانبه را ساده می‌کند.",
            "عوامل هیجانی و هویتی، کم‌رنگ می‌مانند.",
            "در شبکه‌های پیچیده، سه‌گانه کافی نیست. آزمون تجربی، دشوار است.",
        ],
        applications=[
            "تحلیل تبلیغات با چهرهٔ محبوب.",
            "تحلیل تبلیغات سیاسی.",
            "بررسی هم‌راستایی رسانه و مخاطب.",
            "آموزش ارتباط میان‌فردی.",
            "تحلیل تعارض خانوادگی.",
            "پژوهش تغییر نگرش.",
            "طراحی پیام تأییدی.",
            "تحلیل شبکهٔ دوستی.",
            "ارزیابی تبلیغات منفی. تحلیل بحران اعتماد.",
        ],
        evolution=("نظریهٔ توازن در ۱۹۴۶ از پژوهش ادراک اجتماعی هایدر برخاست و در ۱۹۵۸ در چارچوب روان‌شناسی روابط میان‌فردی گسترش یافت. "
                   "در دههٔ ۱۹۵۰، نیوکامب آن را به ارتباط و جذابیت تعمیم داد و فستینگر مسیر ناهماهنگی شناختی را جدا کرد. "
                   "در دههٔ ۲۰۰۰، تحلیل شبکه، سه‌گانه را به ساختارهای بزرگ‌تر برد. "
                   "امروز، نظریه با تبلیغات تأییدی و حباب‌های هم‌فکری گره خورده است. سادگی مدل، هم مزیت و هم محدودیت آن است."),
        key_concepts=[
            {"term_en": "P-O-X Triad", "term_fa": "سه‌گانهٔ P-O-X", "definition": "فرد، شخص دیگر و موضوع که روابط میان آن‌ها توازن یا ناتوازن می‌سازد."},
            {"term_en": "Balance", "term_fa": "توازن", "definition": "حالتی که روابط سه‌گانه هماهنگ‌اند و تنش شناختی نمی‌سازند."},
            {"term_en": "Imbalance", "term_fa": "ناتوازن", "definition": "ناسازگاری روابط که فشار روانی برای تغییر ایجاد می‌کند."},
            {"term_en": "Unit Relation", "term_fa": "رابطهٔ وحدت", "definition": "پیوند ادراکی مانند مالکیت یا عضویت که دو عنصر را به هم می‌بندد."},
            {"term_en": "Sentiment Relation", "term_fa": "رابطهٔ احساسی", "definition": "ارزیابی مثبت یا منفی میان دو عنصر که در توازن سه‌گانه به کار می‌آید."},
        ],
        theorists=[{"role": "بنیان‌گذار نظریه", "name_en": "Fritz Heider", "name_fa": "فریتز هایدر"}],
        model={"elements": ["فرد (P)", "شخص دیگر (O)", "موضوع (X)", "روابط مثبت یا منفی", "توازن یا ناتوازن", "تغییر برای بازگرداندن توازن"],
               "description": "سه عنصر با روابط دوقطبی به هم می‌پیوندند؛ حاصل‌ضرب نشانه‌ها توازن را تعیین می‌کند و ناتوازن، تغییر می‌سازد."},
        mapping={"entity_type": "THEORY", "content_type": "نظریه (Theory)", "needs_review": False},
        studies=[
            {"citation": "هایدر (۱۹۴۶)، صورت‌بندی نگرش‌ها و سازمان شناختی", "findings": "روابط متوازن پایدارترند و ناتوازن، فشار تغییر نگرش یا رابطه می‌سازد."},
            {"citation": "هایدر (۱۹۵۸)، گسترش نظریه در روان‌شناسی روابط میان‌فردی", "findings": "توازن با احساسات، واحدهای ادراکی و روابط علّی پیوند دارد و ادراک اجتماعی را سازمان می‌دهد."},
        ],
        example_text="طرفدار یک فوتبالیست محبوب است و همان بازیکن از برندی تعریف می‌کند؛ پیوند مثبت دوگانه، نگرش مثبت به برند می‌سازد. اگر برند رفتاری ناپسند داشته باشد، طرفدار برای حفظ توازن، یا نگرش به برند یا نگرش به بازیکن را تغییر می‌دهد.",
        critique_text="۱. جهت و میزان تغییر را پیش‌بینی نمی‌کند. ۲. روابط دوقطبی، شدت نگرش را نادیده می‌گیرد. ۳. ساختارهای شبکه‌ای پیچیده را ساده می‌کند. ۴. آزمون تجربی سه‌گانه، دشوار است.",
    ),
    "card-323": dict(
        level="میانی",
        related_approaches="نظریهٔ نقض انتظار؛ اقناع و مقاومت پیام؛ نظریهٔ خودمختاری؛ ارتباط سلامت؛ اخلاق بازاریابی.",
        recommended_sources="«نظریهٔ واکنش روانی» (برِم، ۱۹۶۶)؛ «واکنش روانی: نظریهٔ آزادی و کنترل» (برِم و برِم، ۱۹۸۱).",
        summary=("نظریهٔ واکنش روانی توضیح می‌دهد که وقتی فرد احساس کند آزادی رفتاری یا شناختی‌اش تهدید شده است، حالت انگیزشی «واکنش روانی» فعال می‌شود و او می‌کوشد آزادی ازدست‌رفته را بازگرداند. "
                 "برِم (۱۹۶۶) این نظریه را با تمرکز بر آزادی‌های رفتاری صورت‌بندی کرد: هر چه آزادی مهم‌تر، تهدید جدی‌تر و شمار آزادی‌های تهدیدشده بیشتر باشد، واکنش شدیدتر است. "
                 "برِم و برِم (۱۹۸۱) سازوکارهای بازیابی آزادی و تفاوت‌های فردی را بسط دادند و نشان دادند که واکنش می‌تواند به شکل جذب گزینهٔ ممنوع، کاهش جذابیت منبع تهدید یا افزایش جذابیت گزینه‌های حذف‌شده ظاهر شود. "
                 "در این نظریه، آزادی، تهدید، واکنش، بازیابی و اثر بومرنگ سازه‌های اصلی‌اند. "
                 "نقد اصلی، دشواری سنجش، شرایط مرزی و تفاوت‌های فرهنگی است. در عمل، نظریه چارچوب مهمی برای طراحی هشدار سلامت، مقررات، تبلیغات فشارآور و تجربهٔ کاربری اجباری فراهم می‌کند و به پرهیز از پیام‌های کنترل‌گرانه در ارتباط اقناعی یاری می‌رساند."),
        definition="نظریهٔ واکنش روانی، حالت انگیزشی مقاومت در برابر تهدید آزادی‌های رفتاری و شناختی و کوشش برای بازیابی آن آزادی‌ها را تبیین می‌کند.",
        main_problem="چرا پیام‌ها و مقررات فشارآور اغلب نتیجهٔ معکوس می‌دهند و چه سازوکاری، مخاطب را به مقاومت و بازیابی آزادی وامی‌دارد؟",
        mechanism=("فرد مجموعه‌ای از آزادی‌های رفتاری را برای خود مسلم می‌داند. "
                   "وقتی پیام، قاعده یا محدودیتی این آزادی را تهدید می‌کند، واکنش روانی به‌عنوان حالت انگیزشی فعال می‌شود. "
                   "شدت واکنش به اهمیت آزادی، گسترهٔ تهدید و شمار گزینه‌های حذف‌شده بستگی دارد. "
                   "برِم (۱۹۶۶) نشان داد که فرد برای بازیابی آزادی، گزینهٔ ممنوع را جذاب‌تر می‌بیند یا نگرش خود را در جهت مخالف پیام تغییر می‌دهد. "
                   "برِم و برِم (۱۹۸۱) افزودند که جذابیت منبع تهدید نیز کاهش می‌یابد و تفاوت‌های فردی در حساسیت به تهدید مؤثر است. "
                   "این سازوکار، اثر بومرنگ را توضیح می‌دهد: فشار بیشتر، مقاومت بیشتر. "
                   "در ارتباط سلامت، پیام ترس‌محور بدون حمایت از خودمختاری، اغلب واکنش منفی می‌سازد."),
        assumptions=[
            "افراد مجموعه‌ای از آزادی‌های رفتاری دارند.",
            "تهدید آزادی، واکنش انگیزشی می‌سازد.",
            "شدت واکنش به اهمیت آزادی بستگی دارد.",
            "فرد برای بازیابی آزادی تلاش می‌کند.",
        ],
        principles=[
            "آزادی، ارزش روانی است.",
            "تهدید صریح، مقاومت می‌سازد.",
            "گزینهٔ ممنوع، جذاب‌تر می‌شود.",
            "کاهش فشار، مقاومت را می‌کاهد. خودمختاری، شرط پذیرش پیام است.",
        ],
        critiques=[
            "سنجش واکنش، اغلب غیرمستقیم و دشوار است.",
            "شرایط مرزی و تفاوت‌های فردی، تعمیم را محدود می‌کند.",
            "تفاوت‌های فرهنگی در حساسیت به تهدید، کم‌بررسی مانده است.",
            "رابطهٔ واکنش با رفتار واقعی، همیشه روشن نیست.",
            "نظریه بر آزادی فردی تمرکز دارد و قدرت ساختاری را کم‌رنگ می‌کند. سنجش بلندمدت، نادر است.",
        ],
        applications=[
            "طراحی پیام سلامت بدون فشار.",
            "تحلیل اثر ممنوعیت و سانسور.",
            "طراحی مقررات مدرسه و خانواده.",
            "آموزش اقناع اخلاقی.",
            "تحلیل تبلیغات فشارآور.",
            "طراحی تجربهٔ کاربری با آزادی انتخاب.",
            "پژوهش رفتار نوجوان.",
            "طراحی کمپین محیط‌زیست.",
            "ارزیابی هشدارهای قانونی. تحلیل مقاومت مصرف‌کننده.",
        ],
        evolution=("برِم (۱۹۶۶) نظریه را با آزمایش‌های آزادی رفتاری صورت‌بندی کرد. "
                   "برِم و برِم (۱۹۸۱) کتاب مرجع را نوشتند و سازوکارهای بازیابی را گستردند. "
                   "در دههٔ ۲۰۰۰، پژوهش پیام سلامت، واکنش را به طراحی اقناعی گره زد. "
                   "در دههٔ ۲۰۱۰، نظریه در تجربهٔ کاربری و طراحی پلتفرم کاربرد یافت. "
                   "امروز، با پیام‌های شخصی‌سازی‌شده و محدودیت‌های الگوریتمی، پرسش آزادی دوباره مرکزی شده است."),
        key_concepts=[
            {"term_en": "Free Behaviors", "term_fa": "رفتارهای آزاد", "definition": "کنش‌هایی که فرد حق انجام آن‌ها را برای خود مسلم می‌داند."},
            {"term_en": "Threat to Freedom", "term_fa": "تهدید آزادی", "definition": "پیام یا محدودیتی که انجام یا انتخاب آزاد را دشوار یا ممنوع می‌کند."},
            {"term_en": "Reactance", "term_fa": "واکنش روانی", "definition": "حالت انگیزشی مقاومت که پس از تهدید آزادی فعال می‌شود."},
            {"term_en": "Freedom Restoration", "term_fa": "بازیابی آزادی", "definition": "کوشش برای بازگرداندن آزادی از راه انجام گزینهٔ ممنوع یا تغییر نگرش."},
            {"term_en": "Boomerang Effect", "term_fa": "اثر بومرنگ", "definition": "نتیجهٔ معکوس پیام اقناعی که مخاطب را به سمت مخالف سوق می‌دهد."},
        ],
        theorists=[{"role": "بنیان‌گذار نظریه", "name_en": "Jack W. Brehm", "name_fa": "جک برِم"},
                   {"role": "گسترش‌دهندهٔ نظریه", "name_en": "Sharon S. Brehm", "name_fa": "شارون برِم"}],
        model={"elements": ["آزادی", "تهدید", "واکنش روانی", "شدت واکنش", "بازیابی آزادی", "اثر بومرنگ"],
               "description": "تهدید آزادی، واکنش انگیزشی می‌سازد؛ شدت آن به اهمیت آزادی و گسترهٔ تهدید بستگی دارد و به بازیابی آزادی یا مقاومت می‌انجامد."},
        mapping={"entity_type": "THEORY", "content_type": "نظریه (Theory)", "needs_review": False},
        studies=[
            {"citation": "برِم (۱۹۶۶)، صورت‌بندی و آزمون نظریهٔ واکنش روانی", "findings": "تهدید آزادی، جذابیت گزینهٔ ممنوع را افزایش داد و مقاومت در برابر فشار را نشان داد."},
            {"citation": "برِم و برِم (۱۹۸۱)، نظریهٔ آزادی و کنترل", "findings": "شدت واکنش به اهمیت آزادی، شمار گزینه‌ها و جذابیت منبع تهدید بستگی دارد."},
        ],
        example_text="هشدارهای اجباری «حتماً این کار را نکنید» در نوجوانان اغلب واکنش معکوس می‌سازد؛ در حالی که پیام حمایت‌گر که انتخاب را به خود مخاطب می‌سپارد، پذیرش بیشتری می‌یابد.",
        critique_text="۱. سنجش واکنش دشوار است. ۲. شرایط مرزی، تعمیم را محدود می‌کند. ۳. تفاوت‌های فرهنگی کم‌بررسی مانده‌اند. ۴. رابطهٔ واکنش با رفتار واقعی همیشه روشن نیست.",
    ),
    "card-388": dict(
        level="میانی",
        related_approaches="سرمایهٔ اجتماعی؛ اقتصاد رسانه؛ مدیریت استعداد؛ نظریهٔ خالقان محتوا؛ اقتصاد خلاق.",
        recommended_sources="«سرمایه‌گذاری در سرمایهٔ انسانی» (شولتز، ۱۹۶۱)؛ «سرمایهٔ انسانی» (بکر، ۱۹۶۴).",
        summary=("نظریهٔ سرمایهٔ انسانی، دانش، مهارت، سلامت و توانمندی افراد را نه هزینهٔ جاری، بلکه سرمایه‌گذاری مولد می‌بیند که بازده اقتصادی و اجتماعی می‌سازد. "
                 "شولتز (۱۹۶۱) نشان داد که کیفیت نیروی انسانی، متغیر کلیدی رشد اقتصادی است و آموزش، بهداشت و مهاجرت را می‌توان سرمایه‌گذاری خواند. "
                 "بکر (۱۹۶۴) با تحلیل نرخ بازده آموزش و آموزش ضمن خدمت، چارچوبی برای سنجش سود سرمایه‌گذاری در مهارت ساخت. "
                 "در بافت رسانه، مهارت‌های تحریریه، فنی و خلاق، دارایی سرمایه‌ای سازمان‌اند و سرمایه‌گذاری در آموزش، ابزار و محیط کار، توان تولید و نوآوری را می‌سازد. "
                 "در این نظریه، سرمایهٔ انسانی، آموزش، مهارت، بازده و فرسایش سرمایه سازه‌های اصلی‌اند. "
                 "نقد اصلی، کم‌توجهی به نابرابری ساختاری، مدرک‌گرایی و دشواری سنجش مهارت ضمنی است. در عمل، نظریه چارچوبی برای تصمیم سرمایه‌گذاری در استعداد رسانه‌ای و ارزیابی بازده آموزش فراهم می‌کند."),
        definition="نظریهٔ سرمایهٔ انسانی، دانش و مهارت افراد را سرمایه‌ای مولد می‌داند که با آموزش، تجربه و سلامت ساخته می‌شود و بازده اقتصادی و سازمانی می‌آفریند.",
        main_problem="سازمان رسانه چگونه سرمایه‌گذاری در مهارت و آموزش نیروی انسانی را به‌عنوان سرمایه و نه هزینه توجیه و اندازه‌گیری می‌کند؟",
        mechanism=("فرد با آموزش، تمرین و تجربه، مهارت و دانش خود را افزایش می‌دهد. "
                   "این سرمایه، بهره‌وری و توان حل مسئله را بالا می‌برد و بازده فرد و سازمان را می‌افزاید. "
                   "شولتز (۱۹۶۱) نشان داد که آموزش و سلامت، کیفیت نیروی کار را می‌سازند و رشد اقتصادی را توضیح می‌دهند. "
                   "بکر (۱۹۶۴) با محاسبهٔ نرخ بازده، تصمیم سرمایه‌گذاری در آموزش عمومی و ضمن خدمت را اقتصادی کرد. "
                   "در سازمان رسانه، مهارت چندرسانه‌ای، سواد داده و توان خلاق، سرمایه‌هایی‌اند که با آموزش هدفمند و ابزار مناسب رشد می‌کنند. "
                   "فرسایش سرمایه با ترک سازمان، کهنگی مهارت یا نبود انگیزه رخ می‌دهد. "
                   "سرمایه‌گذاری باید میان آموزش عمومی و مهارت ویژهٔ سازمان توازن بسازد."),
        assumptions=[
            "مهارت و دانش، سرمایه‌اند.",
            "آموزش، بازده اقتصادی می‌سازد.",
            "سرمایهٔ انسانی، قابل سنجش است.",
            "سازمان و فرد، هر دو سرمایه‌گذاری می‌کنند.",
        ],
        principles=[
            "آموزش، هزینه نیست.",
            "بازده، با نرخ و زمان سنجیده می‌شود.",
            "مهارت ویژه، وابستگی می‌سازد.",
            "سرمایه، فرسوده می‌شود. یادگیری پیوسته، سرمایه را حفظ می‌کند.",
        ],
        critiques=[
            "نابرابری ساختاری در دسترسی به آموزش را کم‌رنگ می‌کند.",
            "مدرک‌گرایی، مهارت واقعی را پنهان می‌سازد.",
            "سنجش مهارت ضمنی و خلاق، دشوار است.",
            "انسان را به سرمایه فرو می‌کاهد.",
            "بازده بلندمدت، اغلب نامعلوم است. فرسایش سرمایه، کمتر سنجیده می‌شود.",
        ],
        applications=[
            "برنامه‌ریزی آموزش خبرنگاران.",
            "ارزیابی بازده دورهٔ مهارت دیجیتال.",
            "مدیریت استعداد در رسانه.",
            "تحلیل سرمایهٔ خالقان محتوا.",
            "طراحی مسیر شغلی تحریریه.",
            "پژوهش اقتصاد رسانه.",
            "سنجش هزینهٔ ترک کار.",
            "طراحی برنامهٔ منتورینگ.",
            "ارزیابی سرمایه‌گذاری فناوری. تحلیل بهره‌وری تیم.",
        ],
        evolution=("نظریه در دههٔ ۱۹۶۰ با اقتصاد آموزش شکل گرفت. "
                   "شولتز (۱۹۶۱) سرمایهٔ انسانی را به رشد اقتصادی گره زد و بکر (۱۹۶۴) نرخ بازده را صورت‌بندی کرد. "
                   "در دههٔ ۱۹۸۰، اقتصاد دانش و سرمایهٔ فکری، چارچوب را گسترد. "
                   "در دههٔ ۲۰۰۰، مدیریت استعداد و اقتصاد خالقان، کاربرد رسانه‌ای آن را افزود. "
                   "امروز، مهارت دیجیتال و یادگیری مادام‌العمر، محور سرمایه‌گذاری شده‌اند."),
        key_concepts=[
            {"term_en": "Human Capital", "term_fa": "سرمایهٔ انسانی", "definition": "دانش، مهارت و سلامت افراد که به‌عنوان سرمایهٔ مولد به کار می‌آید."},
            {"term_en": "Investment in Education", "term_fa": "سرمایه‌گذاری در آموزش", "definition": "هزینهٔ آموزش که بازده آتی فرد و سازمان را افزایش می‌دهد."},
            {"term_en": "Rate of Return", "term_fa": "نرخ بازده", "definition": "سنجهٔ سود اقتصادی سرمایه‌گذاری در آموزش و مهارت."},
            {"term_en": "On-the-Job Training", "term_fa": "آموزش ضمن خدمت", "definition": "یادگیری مهارت در جریان کار که سرمایهٔ ویژهٔ سازمان می‌سازد."},
            {"term_en": "Capital Depreciation", "term_fa": "فرسایش سرمایه", "definition": "کاهش ارزش سرمایهٔ انسانی با کهنگی مهارت، ترک کار یا بی‌انگیزگی."},
        ],
        theorists=[{"role": "بنیان‌گذار نظریه", "name_en": "Theodore W. Schultz", "name_fa": "تئودور شولتز"},
                   {"role": "صورت‌بندی نرخ بازده", "name_en": "Gary S. Becker", "name_fa": "گری بکر"}],
        model={"elements": ["آموزش و تجربه", "مهارت و دانش", "بهره‌وری", "بازده اقتصادی", "فرسایش سرمایه"],
               "description": "سرمایه‌گذاری در آموزش و سلامت، مهارت می‌سازد؛ مهارت، بهره‌وری و بازده را افزایش می‌دهد و بی‌توجهی، سرمایه را فرسوده می‌کند."},
        mapping={"entity_type": "THEORY", "content_type": "نظریه (Theory)", "needs_review": False},
        studies=[
            {"citation": "شولتز (۱۹۶۱)، سرمایه‌گذاری در سرمایهٔ انسانی", "findings": "کیفیت نیروی انسانی و آموزش، بخش مهمی از رشد اقتصادی را توضیح می‌دهد."},
            {"citation": "بکر (۱۹۶۴)، تحلیل نظری و تجربی سرمایهٔ انسانی", "findings": "آموزش و آموزش ضمن خدمت، نرخ بازده قابل محاسبه می‌سازند و تصمیم سرمایه‌گذاری را اقتصادی می‌کنند."},
        ],
        example_text="یک خبرگزاری با آموزش داده و روایت دیجیتال به تحریریه، زمان تولید محتوای چندرسانه‌ای را کاهش می‌دهد و کیفیت را بالا می‌برد؛ این هزینه، سرمایه‌گذاری در سرمایهٔ انسانی است، نه هزینهٔ جاری.",
        critique_text="۱. نابرابری ساختاری دسترسی به آموزش را کم‌رنگ می‌کند. ۲. مدرک‌گرایی، مهارت واقعی را پنهان می‌سازد. ۳. سنجش مهارت خلاق دشوار است. ۴. انسان به سرمایه فروکاسته می‌شود.",
    ),
    "card-391": dict(
        level="پایه",
        related_approaches="سلسله‌مراتب نیازهای مازلو؛ نظریهٔ انگیزش هرزبرگ؛ رهبری تحول‌آفرین؛ فرهنگ سازمانی؛ ارتباطات سازمانی.",
        recommended_sources="«وجه انسانی سازمان» (مک‌گرگور، ۱۹۶۰)؛ «رهبری و انگیزش» (مک‌گرگور، ۱۹۶۶).",
        summary=("نظریهٔ X و Y، پیش‌فرض‌های مدیران دربارهٔ ماهیت کارکنان را به دو دستهٔ متضاد تقسیم می‌کند و نشان می‌دهد که این پیش‌فرض‌ها سبک مدیریت و ارتباط را می‌سازند. "
                 "مک‌گرگور (۱۹۶۰) نظریهٔ X را بر این باورها استوار کرد که کارکنان از کار می‌گریزند، نیاز به نظارت و اجبار دارند و مسئولیت‌پذیری کمتری می‌خواهند؛ نظریهٔ Y کار را طبیعی می‌داند، بر خودرهبری، تعهد و خلاقیت تأکید می‌کند و کنترل بیرونی را جایگزین کنترل درونی می‌سازد. "
                 "مک‌گرگور (۱۹۶۶) در مجموعهٔ مقالات خود، پیوند این پیش‌فرض‌ها با رهبری، انگیزش و توسعهٔ سازمان را بسط داد. "
                 "در این نظریه، پیش‌فرض مدیریتی، سبک رهبری، انگیزش درونی و خودشکوفایی سازه‌های اصلی‌اند. "
                 "نقد اصلی، تجربی‌نبودن دسته‌بندی، ساده‌سازی و نادیده‌گرفتن بافت و فرهنگ است. در عمل، نظریه چارچوبی برای بازاندیشی مدیریت تحریریه، بازخورد عملکرد و فرهنگ سازمانی فراهم می‌کند و هشدار می‌دهد که پیش‌فرض مدیر، پیش‌گویی خودسازنده می‌سازد."),
        definition="نظریهٔ X و Y، دو مجموعه پیش‌فرض مدیران دربارهٔ ماهیت کارکنان را از هم جدا می‌کند و اثر این پیش‌فرض‌ها بر سبک رهبری و انگیزش را نشان می‌دهد.",
        main_problem="پیش‌فرض‌های مدیران دربارهٔ کارکنان چگونه سبک مدیریت و ارتباط را می‌سازد و کدام پیش‌فرض، انگیزش و مسئولیت‌پذیری را تقویت می‌کند؟",
        mechanism=("مدیر بر پایهٔ پیش‌فرض خود، رفتار کارکنان را تفسیر می‌کند. "
                   "اگر نظریهٔ X را بپذیرد، کنترل بیرونی، نظارت نزدیک و انگیزهٔ تنبیهی را انتخاب می‌کند. "
                   "این سبک، وابستگی و مقاومت می‌سازد و پیش‌فرض منفی را تأیید می‌کند. "
                   "مک‌گرگور (۱۹۶۰) نشان داد که این چرخه، پیش‌گویی خودسازنده است. "
                   "اگر نظریهٔ Y را بپذیرد، مسئولیت می‌سپارد، مشارکت می‌خواهد و بازخورد سازنده می‌دهد. "
                   "این سبک، تعهد و خلاقیت را فعال می‌کند و پیش‌فرض مثبت را تقویت می‌سازد. "
                   "مک‌گرگور (۱۹۶۶) تأکید کرد که رهبری مؤثر، شرایط شکوفایی انگیزش درونی را می‌سازد. "
                   "در عمل، هیچ‌کدام مطلق نیستند و مدیر باید میان بافت، بلوغ کارکنان و ماهیت کار توازن بسازد."),
        assumptions=[
            "پیش‌فرض مدیر، رفتار او را شکل می‌دهد.",
            "کارکنان، انگیزش درونی دارند.",
            "مسئولیت، قابل واگذاری است.",
            "سبک رهبری، پیش‌گویی خودسازنده می‌سازد.",
        ],
        principles=[
            "پیش‌فرض، سبک می‌سازد.",
            "کنترل نزدیک، وابستگی می‌آفریند.",
            "مسئولیت، تعهد می‌سازد.",
            "بازخورد سازنده، یادگیری را فعال می‌کند. کار، می‌تواند منبع رضایت باشد.",
        ],
        critiques=[
            "دسته‌بندی، تجربی و دوگانه است.",
            "بافت و فرهنگ، نادیده می‌ماند.",
            "نظریهٔ Y، آرمانی و کم‌سنجیده است.",
            "تفاوت فردی کارکنان، کم‌رنگ می‌شود.",
            "مدیریت میانی و ساختار قدرت، تحلیل نمی‌شود. آزمون تجربی، محدود است.",
        ],
        applications=[
            "بازطراحی مدیریت تحریریه.",
            "آموزش رهبری رسانه.",
            "طراحی بازخورد عملکرد.",
            "تحلیل فرهنگ سازمانی.",
            "مدیریت تیم خلاق.",
            "پژوهش انگیزش کارکنان.",
            "طراحی واگذاری مسئولیت.",
            "بهبود ارتباط مدیر و کارمند.",
            "ارزیابی سبک رهبری. طراحی توسعهٔ سازمانی.",
        ],
        evolution=("نظریه در ۱۹۶۰ از تجربهٔ مشاورهٔ مک‌گرگور در سازمان‌ها برخاست و در ۱۹۶۶ با مقالات رهبری و انگیزش گسترش یافت. "
                   "در دههٔ ۱۹۷۰، توسعهٔ سازمانی و مدیریت مشارکتی آن را به کار گرفتند. "
                   "در دههٔ ۱۹۸۰، نظریهٔ رهبری تحول‌آفرین، مسیر انگیزش درونی را ادامه داد. "
                   "در دههٔ ۲۰۰۰، تیم‌های دانشی و خلاق، کاربرد تازه‌ای ساختند. "
                   "امروز، نظریه با رهبری خدمتگزار و فرهنگ اعتماد گره خورده است."),
        key_concepts=[
            {"term_en": "Theory X", "term_fa": "نظریهٔ X", "definition": "مجموعه پیش‌فرض‌هایی که کارکنان را گریزان از کار و نیازمند کنترل می‌داند."},
            {"term_en": "Theory Y", "term_fa": "نظریهٔ Y", "definition": "مجموعه پیش‌فرض‌هایی که کار را طبیعی و کارکنان را خودانگیخته و خلاق می‌داند."},
            {"term_en": "Self-Fulfilling Prophecy", "term_fa": "پیش‌گویی خودسازنده", "definition": "چرخه‌ای که پیش‌فرض مدیر، رفتاری می‌سازد که همان پیش‌فرض را تأیید می‌کند."},
            {"term_en": "Intrinsic Motivation", "term_fa": "انگیزش درونی", "definition": "انگیزهٔ ناشی از خود کار و رضایت آن، نه پاداش بیرونی."},
            {"term_en": "Management Assumptions", "term_fa": "پیش‌فرض‌های مدیریتی", "definition": "باورهای زیربنایی مدیر دربارهٔ ماهیت و انگیزهٔ کارکنان."},
        ],
        theorists=[{"role": "بنیان‌گذار نظریه", "name_en": "Douglas McGregor", "name_fa": "داگلاس مک‌گرگور"}],
        model={"elements": ["پیش‌فرض مدیریتی", "سبک رهبری", "انگیزش کارکنان", "رفتار و عملکرد", "تأیید پیش‌فرض"],
               "description": "پیش‌فرض X کنترل بیرونی و پیش‌فرض Y مسئولیت‌سپاری می‌سازد؛ رفتار حاصل، پیش‌فرض مدیر را تقویت می‌کند."},
        mapping={"entity_type": "THEORY", "content_type": "نظریه (Theory)", "needs_review": False},
        studies=[
            {"citation": "مک‌گرگور (۱۹۶۰)، وجه انسانی سازمان", "findings": "پیش‌فرض‌های X و Y سبک مدیریت را می‌سازند و نظریهٔ Y ظرفیت انگیزش درونی را نشان می‌دهد."},
            {"citation": "مک‌گرگور (۱۹۶۶)، رهبری و انگیزش", "findings": "رهبری مؤثر، شرایط شکوفایی انگیزش درونی و مسئولیت‌پذیری کارکنان را فراهم می‌کند."},
        ],
        example_text="سردبیری که خبرنگاران را تنها با نظارت نزدیک و تنبیه مدیریت می‌کند، وابستگی می‌سازد؛ سردبیر دیگری که مالکیت موضوع را می‌سپارد و بازخورد سازنده می‌دهد، تعهد و خلاقیت تحریریه را فعال می‌کند.",
        critique_text="۱. دسته‌بندی دوگانه، تجربی نیست. ۲. بافت و فرهنگ نادیده می‌ماند. ۳. نظریهٔ Y آرمانی است. ۴. ساختار قدرت و تفاوت فردی کم‌رنگ می‌شود.",
    ),
    "card-430": dict(
        level="میانی",
        related_approaches="جامعهٔ شبکه‌ای کاستلز؛ سرمایهٔ اجتماعی؛ نظریهٔ استفاده و رضامندی؛ مدیریت اجتماع آنلاین؛ شبکه‌های اجتماعی.",
        recommended_sources="«جامعهٔ مجازی» (راینگولد، ۱۹۹۳)؛ «مکان فیزیکی و فضای سایبری» (ولمن، ۲۰۰۱).",
        summary=("نظریهٔ جماعت‌های شبکه‌ای، جامعه را نه صرفاً مکان جغرافیایی، بلکه شبکه‌ای از روابط، تعامل‌ها و حمایت‌های متقابل می‌بیند که در فضای آنلاین نیز شکل می‌گیرد و تداوم می‌یابد. "
                 "راینگولد (۱۹۹۳) با تجربهٔ شبکهٔ WELL نشان داد که تعامل رایانه‌ای می‌تواند هنجار، هویت، حمایت احساسی و احساس تعلق بسازد و «جامعهٔ مجازی» را به مفهومی تجربی بدل کرد. "
                 "ولمن (۲۰۰۱) با مفهوم فردگرایی شبکه‌ای توضیح داد که جوامع معاصر حول شبکه‌های شخصی‌شده سازمان می‌یابند، نه حول محله؛ افراد به‌صورت انتخابی و چندکاناله با دیگران پیوند می‌گیرند و مکان فیزیکی، یکی از گره‌ها می‌شود. "
                 "در این نظریه، شبکهٔ روابط، هنجار مشترک، هویت جمعی، حمایت متقابل و مرزهای سیال سازه‌های اصلی‌اند. "
                 "نقد اصلی، شکاف دیجیتال، اتاق‌های پژواک، تجاری‌شدن پلتفرم و کاربرد بلاغی واژهٔ «جامعه» است. در عمل، نظریه چارچوبی برای تحلیل جوامع طرفداران، فضاهای گفت‌وگوی خبری، مدیریت تعامل و طراحی زیرساخت گفت‌وگو فراهم می‌کند."),
        definition="نظریهٔ جماعت‌های شبکه‌ای، جامعه را شبکه‌ای از روابط و تعامل‌های متقابل می‌داند که در فضای آنلاین نیز هنجار، هویت، حمایت و تعلق می‌سازد.",
        main_problem="آیا تعامل رایانه‌ای می‌تواند جامعهٔ واقعی با هنجار و حمایت بسازد و چه سازوکاری، شبکهٔ آنلاین را از مجموعه‌ای پراکنده به جماعت بدل می‌کند؟",
        mechanism=("افراد با تعامل پیوسته در یک فضای شبکه‌ای، شناخت و اعتماد متقابل می‌سازند. "
                   "تکرار گفت‌وگو، هنجارهای مشترک و زبان جمعی می‌آفریند. "
                   "این هنجارها، مرز عضویت و هویت جمعی را شکل می‌دهند. "
                   "راینگولد (۱۹۹۳) نشان داد که در شبکهٔ WELL، حمایت احساسی، همکاری و احساس تعلق از دل گفت‌وگوی متنی پدید آمد. "
                   "ولمن (۲۰۰۱) افزود که شبکه‌های شخصی، تعامل آنلاین و آفلاین را در هم می‌آمیزند و فرد، گره‌های شبکهٔ خود را انتخاب می‌کند. "
                   "حمایت متقابل، اطلاعات و اعتماد، سرمایهٔ اجتماعی جماعت را می‌سازد. "
                   "مدیریت فضا، هنجارگذاری و پاسخ به تعارض، پایداری جماعت را تعیین می‌کند. "
                   "اگر اعتماد بشکند یا فضا تجاری شود، عضویت به مصرف و تماشا فرو می‌کاهد."),
        assumptions=[
            "جامعه، شبکهٔ روابط است.",
            "تعامل آنلاین، هنجار و هویت می‌سازد.",
            "افراد، گره‌های شبکهٔ خود را انتخاب می‌کنند.",
            "حمایت متقابل، اعتماد می‌آفریند.",
        ],
        principles=[
            "جامعه، پیش از مکان، رابطه است.",
            "تکرار تعامل، هنجار می‌سازد.",
            "هویت جمعی، از گفت‌وگو برمی‌آید.",
            "مدیریت فضا، پایداری را تعیین می‌کند. اعتماد، سرمایهٔ اصلی است.",
        ],
        critiques=[
            "شکاف دیجیتال، دسترسی برابر را محدود می‌کند.",
            "اتاق‌های پژواک، تنوع را کاهش می‌دهند.",
            "تجاری‌شدن پلتفرم، اعتماد را فرسوده می‌کند.",
            "کاربرد واژهٔ جامعه، اغلب بلاغی است.",
            "روابط ضعیف، جانشین حمایت نزدیک نمی‌شود. مرز عمومی و خصوصی، مبهم است.",
        ],
        applications=[
            "تحلیل جوامع طرفداران.",
            "طراحی فضای گفت‌وگوی خبری.",
            "مدیریت اجتماع آنلاین.",
            "پژوهش سرمایهٔ اجتماعی.",
            "طراحی هنجار و مقررات پلتفرم.",
            "تحلیل حمایت آنلاین.",
            "آموزش سواد شبکه‌ای.",
            "طراحی مدل تعامل.",
            "ارزیابی انسجام جماعت. تحلیل تعارض آنلاین.",
        ],
        evolution=("مفهوم جامعهٔ مجازی در ۱۹۹۳ از تجربهٔ شبکه‌های متنی اولیه برخاست. "
                   "راینگولد (۱۹۹۳) آن را به هنجار، هویت و حمایت گره زد و ولمن (۲۰۰۱) فردگرایی شبکه‌ای را صورت‌بندی کرد. "
                   "در دههٔ ۲۰۰۰، پلتفرم‌های اجتماعی، مقیاس تعامل را دگرگون کردند. "
                   "در دههٔ ۲۰۱۰، الگوریتم و اقتصاد توجه، پرسش پایداری جماعت را تازه کرد. "
                   "امروز، نظریه با مدیریت اجتماع، حاکمیت محتوا و سلامت گفت‌وگو گره خورده است."),
        key_concepts=[
            {"term_en": "Virtual Community", "term_fa": "جامعهٔ مجازی", "definition": "شبکهٔ تعامل رایانه‌ای که هنجار، هویت و حمایت متقابل می‌سازد."},
            {"term_en": "Networked Individualism", "term_fa": "فردگرایی شبکه‌ای", "definition": "سازمان‌یابی جامعه حول شبکه‌های شخصی چندکاناله و نه محله."},
            {"term_en": "Social Capital", "term_fa": "سرمایهٔ اجتماعی", "definition": "اعتماد، اطلاعات و حمایت متقابلی که از شبکهٔ روابط برمی‌آید."},
            {"term_en": "Weak Ties", "term_fa": "پیوندهای ضعیف", "definition": "روابط کم‌نزدیک که دسترسی به اطلاعات و فرصت‌های تازه می‌سازند."},
            {"term_en": "Community Norms", "term_fa": "هنجارهای جماعت", "definition": "قواعد مشترک رفتار که از تعامل پیوسته و مدیریت فضا شکل می‌گیرد."},
        ],
        theorists=[{"role": "صورت‌بندی جامعهٔ مجازی", "name_en": "Howard Rheingold", "name_fa": "هوارد راینگولد"},
                   {"role": "نظریه‌پرداز فردگرایی شبکه‌ای", "name_en": "Barry Wellman", "name_fa": "بری ولمن"}],
        model={"elements": ["تعامل پیوسته", "هنجار مشترک", "هویت جمعی", "حمایت متقابل", "سرمایهٔ اجتماعی", "پایداری یا فروپاشی"],
               "description": "تعامل پیوسته هنجار و هویت می‌سازد؛ حمایت متقابل سرمایهٔ اجتماعی می‌آفریند و مدیریت فضا، پایداری جماعت را تعیین می‌کند."},
        mapping={"entity_type": "THEORY", "content_type": "نظریه (Theory)", "needs_review": False},
        studies=[
            {"citation": "راینگولد (۱۹۹۳)، جامعهٔ مجازی", "findings": "شبکهٔ WELL نشان داد تعامل متنی می‌تواند هنجار، حمایت احساسی و احساس تعلق بسازد."},
            {"citation": "ولمن (۲۰۰۱)، مکان فیزیکی و فضای سایبری", "findings": "جوامع معاصر حول شبکه‌های شخصی و ترکیب تعامل آنلاین و آفلاین سازمان می‌یابند."},
        ],
        example_text="جامعهٔ خوانندگان یک رسانهٔ تخصصی در گروه گفت‌وگو، هنجارِ احترام، زبان مشترک و حمایت فنی می‌سازد؛ وقتی مدیران گروه با شفافیت تعارض را مدیریت می‌کنند، عضویت پایدار می‌ماند و وقتی فضا به تبلیغ خالی بدل شود، اعتماد فرو می‌ریزد.",
        critique_text="۱. شکاف دیجیتال، دسترسی را محدود می‌کند. ۲. اتاق‌های پژواک، تنوع را کاهش می‌دهند. ۳. تجاری‌شدن، اعتماد را می‌شکند. ۴. واژهٔ جامعه اغلب بلاغی است.",
    ),
    "card-456": dict(
        level="میانی",
        related_approaches="نظریهٔ استفاده و رضامندی؛ نظریهٔ سرگرمی؛ روان‌شناسی مثبت؛ بازی‌وارسازی؛ نظریهٔ آیینی ارتباطات.",
        recommended_sources="«نظریهٔ بازی در ارتباطات جمعی» (استیفنسون، ۱۹۶۷)؛ «اثرات رسانه» (برایانت و الیور، ۲۰۰۹).",
        summary=("نظریهٔ بازی، مصرف رسانه را نه صرفاً کسب اطلاعات، بلکه فعالیتی خودانگیخته، لذت‌بخش و بازی‌گون می‌بیند که به مخاطب آزادی تفسیر و تجربهٔ ذهنی می‌دهد. "
                 "استیفنسون (۱۹۶۷) ارتباط جمعی را به بازی پیوند زد و مفهوم «ارتباط-لذت» را در برابر «ارتباط-درد» گذاشت: بخش بزرگی از مصرف رسانه، بازی با معنا و تجربهٔ درونی است، نه انتقال پیام. "
                 "او با روش‌شناسی Q، تجربهٔ ذهنی مخاطب را محور تحلیل قرار داد و بر آزادی انتخاب و لذت تفسیری تأکید کرد. "
                 "در آثار مرجع اثرات رسانه، سنت بازی و سرگرمی در کنار پژوهش اقناع و اطلاعات جای گرفته و به نظریه‌های سرگرمی و لذت رسانه‌ای راه داده است. "
                 "در این نظریه، بازی، لذت، آزادی تفسیر، تجربهٔ ذهنی و انتخاب مخاطب سازه‌های اصلی‌اند. "
                 "نقد اصلی، تمرکز بر سرگرمی و کم‌توجهی به خبر، ایدئولوژی و اثرات اجتماعی است. در عمل، نظریه چارچوبی برای تحلیل فرمت‌های سرگرمی، بازی‌وارسازی و تجربهٔ لذت‌بخش رسانه فراهم می‌کند."),
        definition="نظریهٔ بازی، مصرف رسانه را فعالیتی خودانگیخته و لذت‌بخش می‌داند که مخاطب با آزادی تفسیر، با معنا بازی می‌کند و تجربهٔ ذهنی می‌سازد.",
        main_problem="چرا مخاطبان بخش بزرگی از زمان خود را صرف رسانه‌ای می‌کنند که اطلاعات سودمندی به آن‌ها نمی‌دهد و لذت و بازی چه جایگاهی در مصرف رسانه دارد؟",
        mechanism=("مخاطب از میان محتواها، آن را برمی‌گزیند که تجربهٔ لذت‌بخش‌تری می‌سازد. "
                   "در جریان مصرف، او با معناها بازی می‌کند، تفسیر می‌سازد و احساس آزادی تجربه می‌کند. "
                   "استیفنسون (۱۹۶۷) این حالت را «ارتباط-لذت» نامید و آن را از مصرف اجباری یا دردناک جدا کرد. "
                   "روش Q، تجربهٔ ذهنی و خودارجاعی مخاطب را در مرکز سنجش گذاشت. "
                   "لذت، از فرم، ریتم، شگفتی و آزادی تفسیر می‌آید و به وفاداری و تکرار مصرف می‌انجامد. "
                   "در رسانه‌های دیجیتال، تعامل، بازی‌وارسازی و محتوای طرفدارمحور، این سازوکار را تقویت می‌کنند. "
                   "اگر لذت به اجبار یا تبلیغ فشارآور بدل شود، تجربهٔ بازی فرو می‌ریزد و مخاطب فاصله می‌گیرد."),
        assumptions=[
            "مصرف رسانه، فعالیتی خودانگیخته است.",
            "لذت، انگیزهٔ اصلی مصرف است.",
            "مخاطب، آزادی تفسیر دارد.",
            "تجربهٔ ذهنی، معیار ارزیابی است.",
        ],
        principles=[
            "رسانه، میدان بازی معناست.",
            "لذت، پیش از اطلاعات می‌آید.",
            "آزادی تفسیر، تجربه را می‌سازد.",
            "اجبار، بازی را می‌شکند. تنوع فرم، لذت می‌آفریند.",
        ],
        critiques=[
            "تمرکز بر سرگرمی، خبر و اطلاعات را کم‌رنگ می‌کند.",
            "ایدئولوژی و قدرت رسانه، تحلیل نمی‌شود.",
            "سنجش تجربهٔ ذهنی، دشوار است.",
            "نظریه، مصرف را رومانتیک می‌کند.",
            "اثرات اجتماعی و سیاسی، نادیده می‌ماند. کاربرد تجربی، محدود است.",
        ],
        applications=[
            "تحلیل فرمت‌های سرگرمی.",
            "طراحی بازی‌وارسازی رسانه.",
            "پژوهش لذت و رضامندی.",
            "طراحی تجربهٔ کاربری رسانه.",
            "تحلیل وفاداری مخاطب.",
            "آموزش سواد رسانه‌ای.",
            "طراحی محتوای تعاملی.",
            "ارزیابی سرگرمی خبری.",
            "پژوهش مخاطب کودک. تحلیل فرهنگ طرفداران.",
        ],
        evolution=("نظریه در ۱۹۶۷ از سنت پژوهش ذهنیت و روش Q برخاست. "
                   "استیفنسون (۱۹۶۷) ارتباط جمعی را به بازی و لذت پیوند زد. "
                   "در دههٔ ۱۹۸۰، پژوهش استفاده و رضامندی، لذت را به انگیزه‌های مخاطب گره زد. "
                   "در دههٔ ۲۰۰۰، نظریهٔ سرگرمی و بازی‌وارسازی، کاربرد تازه ساخت. "
                   "امروز، رسانهٔ تعاملی و محتوای طرفدارمحور، پرسش لذت و آزادی را زنده کرده‌اند."),
        key_concepts=[
            {"term_en": "Communication-Pleasure", "term_fa": "ارتباط-لذت", "definition": "تجربهٔ لذت‌بخش و خودانگیختهٔ مصرف رسانه که مخاطب آزادانه انتخاب می‌کند."},
            {"term_en": "Communication-Pain", "term_fa": "ارتباط-درد", "definition": "مصرف اجباری یا ناخوشایند رسانه که آزادی و لذت را محدود می‌کند."},
            {"term_en": "Subjective Play", "term_fa": "بازی ذهنی", "definition": "فعالیت درونی مخاطب با معناها و تفسیرها در جریان مصرف رسانه."},
            {"term_en": "Q Methodology", "term_fa": "روش Q", "definition": "روش سنجش ذهنیت که تجربهٔ خودارجاع مخاطب را محور تحلیل می‌گذارد."},
            {"term_en": "Audience Freedom", "term_fa": "آزادی مخاطب", "definition": "توان انتخاب و تفسیر آزاد محتوا که تجربهٔ بازی را ممکن می‌کند."},
        ],
        theorists=[{"role": "بنیان‌گذار نظریه", "name_en": "William Stephenson", "name_fa": "ویلیام استیفنسون"}],
        model={"elements": ["انتخاب مخاطب", "مصرف خودانگیخته", "بازی با معنا", "لذت", "تجربهٔ ذهنی", "تکرار مصرف"],
               "description": "مخاطب محتوای لذت‌بخش را برمی‌گزیند، با معنا بازی می‌کند و تجربهٔ ذهنی می‌سازد؛ لذت، تکرار مصرف را تقویت می‌کند."},
        mapping={"entity_type": "THEORY", "content_type": "نظریه (Theory)", "needs_review": False},
        studies=[
            {"citation": "استیفنسون (۱۹۶۷)، نظریهٔ بازی در ارتباطات جمعی", "findings": "بخش بزرگی از مصرف رسانه، بازی ذهنی و لذت است و با روش Q قابل سنجش است."},
            {"citation": "برایانت و الیور (۲۰۰۹)، اثرات رسانه", "findings": "سنت بازی و سرگرمی در کنار پژوهش اقناع و اطلاعات، به نظریه‌های لذت رسانه‌ای راه یافته است."},
        ],
        example_text="بازی موبایلی خبری که مخاطب را در نقش سردبیر می‌گذارد، با آزادی انتخاب و لذت تصمیم‌گیری، مصرف خبر را از وظیفه به بازی بدل می‌کند و زمان تعامل را افزایش می‌دهد.",
        critique_text="۱. تمرکز بر سرگرمی، خبر را کم‌رنگ می‌کند. ۲. قدرت و ایدئولوژی تحلیل نمی‌شود. ۳. سنجش تجربهٔ ذهنی دشوار است. ۴. نظریه مصرف را رومانتیک می‌کند.",
    ),
    "card-90": dict(
        level="پیشرفته",
        related_approaches="جامعهٔ شبکه‌ای؛ نظریهٔ کنشگر-شبکه؛ اقتصاد سیاسی رسانه؛ تاریخ فناوری؛ مطالعات علم و فناوری.",
        recommended_sources="«ساخت اجتماعی واقعیت‌ها و مصنوعات» (پینچ و بایکر، ۱۹۸۴)؛ «از دوچرخه و باکلیت تا لامپ» (بایکر، ۱۹۹۵).",
        summary=("این نظریه، دو موضع متضاد دربارهٔ نسبت فناوری و جامعه را به هم می‌سنجد: جبر فناورانه که فناوری را نیروی تعیین‌کنندهٔ تغییر اجتماعی می‌داند و ساخت اجتماعی فناوری که فناوری را محصول تفسیر، مذاکره و منافع گروه‌های اجتماعی می‌بیند. "
                 "پینچ و بایکر (۱۹۸۴) با مفهوم انعطاف تفسیری نشان دادند که یک مصنوع فنی می‌تواند در مرحلهٔ اولیه معناها و کاربردهای متفاوت داشته باشد و گروه‌های اجتماعی مرتبط، بر سر طراحی و کاربرد آن چانه‌زنی می‌کنند. "
                 "با بسته‌شدن مناقشه و تثبیت، یک تفسیر غالب می‌شود و فناوری، شکل پایدار می‌گیرد. "
                 "بایکر (۱۹۹۵) با مطالعهٔ دوچرخه، باکلیت و لامپ فلورسنت، نظریهٔ تغییر اجتماعی-فنی را بسط داد و نشان داد که طراحی، فرایندی اجتماعی و سیاسی است. "
                 "در این چارچوب، انعطاف تفسیری، گروه اجتماعی مرتبط، بسته‌شدن، تثبیت و چارچوب فن‌شناختی سازه‌های اصلی‌اند. "
                 "نقد اصلی، کم‌توجهی به ساختارهای کلان، قدرت مادی و محدودیت‌های فنی است. در عمل، چارچوبی برای تحلیل طراحی پلتفرم، سیاست فناوری و مسیر نوآوری رسانه‌ای فراهم می‌کند."),
        definition="این نظریه، جبر فناورانه را در برابر ساخت اجتماعی فناوری می‌گذارد و نشان می‌دهد که طراحی و کاربرد فناوری، محصول تفسیر و مذاکرهٔ گروه‌های اجتماعی است.",
        main_problem="فناوری، نیروی تعیین‌کنندهٔ جامعه است یا محصول تفسیر و منافع گروه‌های اجتماعی و کدام سازوکار، شکل نهایی یک فناوری را تعیین می‌کند؟",
        mechanism=("یک فناوری نوظهور با انعطاف تفسیری بالا وارد می‌شود؛ گروه‌های اجتماعی مختلف، معنا و کاربرد متفاوت برای آن می‌سازند. "
                   "طراحان، کاربران، سرمایه‌گذاران و تنظیم‌گران بر سر شکل و کارکرد آن چانه‌زنی می‌کنند. "
                   "پینچ و بایکر (۱۹۸۴) نشان دادند که مناقشه تا بسته‌شدن ادامه می‌یابد و سپس یک تفسیر غالب، تثبیت می‌شود. "
                   "بسته‌شدن، اغلب با حل یک مسئلهٔ عملی یا ائتلاف گروه‌ها رخ می‌دهد و نه با برتری ذاتی فناوری. "
                   "بایکر (۱۹۹۵) افزود که چارچوب فن‌شناختی گروه‌ها، مسئله‌ها و راه‌حل‌ها را تعریف می‌کند. "
                   "پس از تثبیت، فناوری طبیعی جلوه می‌کند و مسیرهای جایگزین فراموش می‌شوند. "
                   "همین فراموشی، جبر فناورانه را تقویت می‌کند. بازخوانی تاریخی، نشان می‌دهد که انتخاب‌های اجتماعی دیگری ممکن بود."),
        assumptions=[
            "فناوری، محصول اجتماعی است.",
            "معنای فناوری، در مرحلهٔ اولیه انعطاف دارد.",
            "گروه‌های اجتماعی، بر طراحی اثر می‌گذارند.",
            "بسته‌شدن مناقشه، شکل پایدار می‌سازد.",
        ],
        principles=[
            "طراحی، فرایند اجتماعی است.",
            "انعطاف تفسیری، گزینه‌ها را باز می‌کند.",
            "بسته‌شدن، گزینه‌ها را پنهان می‌کند.",
            "تثبیت، طبیعی‌شدن می‌آورد. ساختار کلان، باید افزوده شود.",
        ],
        critiques=[
            "ساختارهای اقتصادی و سیاسی کلان، کم‌رنگ می‌مانند.",
            "قدرت مادی و محدودیت فنی، کمتر تحلیل می‌شود.",
            "نسبی‌گرایی، خطر بی‌طرفی علمی را می‌سازد.",
            "گروه‌های اجتماعی، اغلب مبهم تعریف می‌شوند.",
            "کاربرد برای فناوری‌های پیچیده و جهانی، دشوار است. نقش مصرف‌کنندهٔ ضعیف، پنهان می‌ماند.",
        ],
        applications=[
            "تحلیل طراحی پلتفرم.",
            "پژوهش تاریخ رسانه.",
            "سیاست‌گذاری فناوری.",
            "تحلیل نوآوری رسانه‌ای.",
            "آموزش مطالعات علم و فناوری.",
            "بررسی پذیرش فناوری.",
            "تحلیل مناقشهٔ فنی.",
            "طراحی مشارکتی.",
            "ارزیابی اثر اجتماعی فناوری. تحلیل هوش مصنوعی در رسانه.",
        ],
        evolution=("چارچوب SCOT در دههٔ ۱۹۸۰ از جامعه‌شناسی علم و فناوری برخاست. "
                   "پینچ و بایکر (۱۹۸۴) انعطاف تفسیری و بسته‌شدن را صورت‌بندی کردند و بایکر (۱۹۹۵) نظریهٔ تغییر اجتماعی-فنی را گسترد. "
                   "در دههٔ ۱۹۹۰، نظریهٔ کنشگر-شبکه و اقتصاد سیاسی، نقد و تکمیل آن شد. "
                   "در دههٔ ۲۰۰۰، طراحی مشارکتی و مطالعات زیرساخت، کاربرد آن را افزود. "
                   "امروز، هوش مصنوعی و پلتفرم‌ها، میدان تازه‌ای برای آزمون چارچوب‌اند."),
        key_concepts=[
            {"term_en": "Technological Determinism", "term_fa": "جبر فناورانه", "definition": "موضعی که فناوری را نیروی اصلی و تعیین‌کنندهٔ تغییر اجتماعی می‌داند."},
            {"term_en": "Interpretive Flexibility", "term_fa": "انعطاف تفسیری", "definition": "امکان تفسیرها و کاربردهای متفاوت از یک فناوری در مرحلهٔ اولیه."},
            {"term_en": "Relevant Social Groups", "term_fa": "گروه‌های اجتماعی مرتبط", "definition": "گروه‌هایی که معنا و طراحی فناوری را از دیدگاه خود تعریف می‌کنند."},
            {"term_en": "Closure", "term_fa": "بسته‌شدن", "definition": "پایان مناقشهٔ تفسیری و پذیرش یک معنا یا طراحی غالب."},
            {"term_en": "Stabilization", "term_fa": "تثبیت", "definition": "پایداری شکل و کارکرد فناوری پس از بسته‌شدن مناقشه."},
        ],
        theorists=[{"role": "هم‌بنیان‌گذار SCOT", "name_en": "Trevor J. Pinch", "name_fa": "ترور پینچ"},
                   {"role": "هم‌بنیان‌گذار SCOT", "name_en": "Wiebe E. Bijker", "name_fa": "ویبه بایکر"}],
        model={"elements": ["فناوری نوظهور", "انعطاف تفسیری", "گروه‌های اجتماعی", "چانه‌زنی", "بسته‌شدن", "تثبیت"],
               "description": "فناوری با معناهای چندگانه وارد می‌شود؛ گروه‌ها چانه‌زنی می‌کنند و با بسته‌شدن مناقشه، یک شکل پایدار تثبیت می‌شود."},
        mapping={"entity_type": "THEORY", "content_type": "نظریه (Theory)", "needs_review": False},
        studies=[
            {"citation": "پینچ و بایکر (۱۹۸۴)، ساخت اجتماعی واقعیت‌ها و مصنوعات", "findings": "انعطاف تفسیری، گروه‌های اجتماعی و بسته‌شدن، شکل‌گیری مصنوع فنی را تبیین می‌کنند."},
            {"citation": "بایکر (۱۹۹۵)، از دوچرخه و باکلیت تا لامپ", "findings": "مطالعهٔ دوچرخه، باکلیت و لامپ نشان داد طراحی، فرایندی اجتماعی-فنی و مناقشه‌آمیز است."},
        ],
        example_text="در تاریخ رسانه، ضبط و پخش خانگی ابتدا تهدید صنعت موسیقی خوانده شد؛ گروه‌های کاربران، تولیدکنندگان و حقوق‌داران بر سر معنای فناوری چانه‌زنی کردند تا سرانجام کاربرد و مقررات آن تثبیت شد.",
        critique_text="۱. ساختارهای کلان و قدرت مادی کم‌رنگ می‌ماند. ۲. محدودیت فنی کمتر تحلیل می‌شود. ۳. نسبی‌گرایی، خطر بی‌طرفی می‌سازد. ۴. کاربرد برای فناوری‌های پیچیده دشوار است.",
    ),
}

NAME_FIX = {}
YEAR_FIX = {}


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
                                       "verified": n_verified, "batch": 237}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH237 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
