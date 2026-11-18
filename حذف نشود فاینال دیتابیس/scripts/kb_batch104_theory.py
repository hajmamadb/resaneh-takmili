# -*- coding: utf-8 -*-
"""Batch 104: full documentation for MC-648, MC-651, MC-655, MC-656."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch104-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch104_theory.json"

S = {
    "MC-648": [
        dict(kind="BOOK",
             title_en="Convergence Culture: Where Old and New Media Collide",
             title_fa="فرهنگ همگرایی: آنجا که رسانه‌های قدیم و نو به هم می‌رسند",
             authors="Jenkins, H.", year=2006, publisher="New York University Press",
             doi=None, url="https://nyupress.org/9780814742815/convergence-culture/",
             language="en", isbn="978-0-8147-4281-5",
             citation="Jenkins, H. (2006). Convergence culture: Where old and new media collide. New York University Press.",
             locator="work", locator_type="work",
             supports="convergence as cultural process / participatory culture / transmedia storytelling", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Cultural Logic of Media Convergence",
             title_fa="منطق فرهنگی همگرایی رسانه‌ای",
             authors="Jenkins, H.", year=2004,
             publisher="International Journal of Cultural Studies",
             doi=None, url=None, language="en", isbn=None,
             citation="Jenkins, H. (2004). The cultural logic of media convergence. International Journal of Cultural Studies, 7(1), 33-43.",
             locator="7(1):33-43", locator_type="page_range",
             supports="early formulation of convergence as cultural process", verified=False),
    ],
    "MC-651": [
        dict(kind="REPORT",
             title_en="When to Leap on the Hype Cycle",
             title_fa="چه زمانی بر چرخه اغراق بجهیم",
             authors="Fenn, J.", year=1995, publisher="Gartner Group",
             doi=None, url="https://www.gartner.com/en/research/methodologies/gartner-hype-cycle",
             language="en", isbn=None,
             citation="Fenn, J. (1995). When to leap on the hype cycle. Gartner Group.",
             locator="work", locator_type="work",
             supports="five-phase hype cycle for emerging technologies", verified=True),
        dict(kind="REPORT",
             title_en="Understanding Gartner's Hype Cycles",
             title_fa="درک چرخه‌های اغراق گارتنر",
             authors="Linden, A.; Fenn, J.", year=2003, publisher="Gartner Research",
             doi=None, url=None, language="en", isbn=None,
             citation="Linden, A., & Fenn, J. (2003). Understanding Gartner's hype cycles. Gartner Research.",
             locator="work", locator_type="work",
             supports="methodology and critique of hype cycle positioning", verified=False),
    ],
    "MC-655": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Organizational Information Requirements, Media Richness and Structural Design",
             title_fa="نیازهای اطلاعاتی سازمان، غنای رسانه و طراحی ساختار",
             authors="Daft, R. L.; Lengel, R. H.", year=1986,
             publisher="Management Science",
             doi="10.1287/mnsc.32.5.554",
             url="https://pubsonline.informs.org/doi/10.1287/mnsc.32.5.554",
             language="en", isbn=None,
             citation="Daft, R. L., & Lengel, R. H. (1986). Organizational information requirements, media richness and structural design. Management Science, 32(5), 554-571. https://doi.org/10.1287/mnsc.32.5.554",
             locator="32(5):554-571", locator_type="page_range",
             supports="media richness dimensions and task-media fit", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Message Equivocality, Media Selection, and Manager Performance",
             title_fa="ابهام پیام، انتخاب رسانه و عملکرد مدیر",
             authors="Daft, R. L.; Lengel, R. H.; Trevino, L. K.", year=1987,
             publisher="MIS Quarterly",
             doi=None, url=None, language="en", isbn=None,
             citation="Daft, R. L., Lengel, R. H., & Trevino, L. K. (1987). Message equivocality, media selection, and manager performance. MIS Quarterly, 11(3), 355-366.",
             locator="11(3):355-366", locator_type="page_range",
             supports="empirical test of media selection under equivocality", verified=False),
    ],
    "MC-656": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Media, Tasks, and Communication Processes: A Theory of Media Synchronicity",
             title_fa="رسانه، تکالیف و فرایندهای ارتباطی: نظریه همزمانی رسانه‌ای",
             authors="Dennis, A. R.; Fuller, R. M.; Valacich, J. S.", year=2008,
             publisher="MIS Quarterly",
             doi=None,
             url="https://misq.umn.edu/misq/article/32/3/575/383/Media-Tasks-and-Communication-Processes-A-Theory",
             language="en", isbn=None,
             citation="Dennis, A. R., Fuller, R. M., & Valacich, J. S. (2008). Media, tasks, and communication processes: A theory of media synchronicity. MIS Quarterly, 32(3), 575-600.",
             locator="32(3):575-600", locator_type="page_range",
             supports="five media capabilities and conveyance-convergence fit", verified=True),
        dict(kind="OTHER",
             title_en="Rethinking Media Richness: Towards a Theory of Media Synchronicity",
             title_fa="بازاندیشی در غنای رسانه: به سوی نظریه همزمانی رسانه‌ای",
             authors="Dennis, A. R.; Valacich, J. S.", year=1999,
             publisher="Hawaii International Conference on System Sciences",
             doi=None, url=None, language="en", isbn=None,
             citation="Dennis, A. R., & Valacich, J. S. (1999). Rethinking media richness: Towards a theory of media synchronicity. Proceedings of the 32nd Hawaii International Conference on System Sciences.",
             locator="work", locator_type="work",
             supports="original conference formulation of media synchronicity", verified=False),
    ],
}

ENRICH = {
    "MC-648": {
        "summary": "(جنکینز، ۲۰۰۶) همگرایی رسانه‌ای نه یک نقطه پایانی فناورانه، بلکه فرایندی فرهنگی است که در آن محتوا میان چند سکوی رسانه‌ای جریان می‌یابد، صنایع رسانه‌ای با هم همکاری می‌کنند و مخاطبان برای یافتن تجربه دلخواه تقریباً هر جایی می‌روند. جنکینز این را با سه مفهوم گره می‌زند: همگرایی فناورانه و صناعتی، فرهنگ مشارکتی و روایت فرا رسانه‌ای. مخاطب از مصرف‌کننده منفعل به مشارکت‌کننده بدل می‌شود و دانش میان طرفداران توزیع می‌شود. همگرایی، رسانه‌های قدیم و نو را در هم می‌آمیزد نه اینکه یکی دیگری را حذف کند.",
        "definition": "همگرایی رسانه‌ای، جریان محتوا میان چند سکوی رسانه‌ای، همکاری صنایع رسانه‌ای و رفتار مهاجر مخاطبانی است که برای تجربه دلخواه میان رسانه‌ها جابه‌جا می‌شوند و در تولید و بازتوزیع محتوا مشارکت می‌کنند.",
        "main_problem": "مسئله این است که چرا مرز رسانه‌ها در عمل فرومی‌ریزد. پاسخ، همگرایی فرهنگی و صناعتی است. پرسش دوم، توزیع قدرت است: آیا همگرایی قدرت مخاطب را زیاد می‌کند یا قدرت صنعت را با ابزار مشارکت بازتولید می‌کند.",
        "mechanism": "۱. همگرایی فناورانه: سکوها و دستگاه‌ها یک کار را انجام می‌دهند و محتوا از مرزها می‌گذرد.\n۲. همگرایی صناعتی: شرکت‌ها در چند رسانه سرمایه‌گذاری و محتوا را میان آن‌ها تبلیغ می‌کنند.\n۳. همگرایی فرهنگی: مخاطب تنها مصرف نمی‌کند؛ بازنشر، اقتباس و نقد می‌سازد.\n۴. روایت فرا رسانه‌ای: داستان در چند سکو پخش می‌شود و هر سکو بخشی از تجربه را می‌سازد.\n۵. هوش جمعی: جوامع طرفدار دانش را گرد می‌آورند و تقسیم می‌کنند.\n۶. مخاطب مهاجر: مخاطب بی وفادار به یک سکو، تجربه را دنبال می‌کند.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا مخاطب هنگام پخش برنامه هم‌زمان در سکوی دیگر گفت‌وگو می‌کند، چرا طرفداران پیش از پخش رسمی، سرنخ‌ها را گرد می‌آورند و چرا کمپین خبری از یک روایت در چند سکو استفاده می‌کند. نکته مهم این است که همگرایی جایگزینی رسانه نیست؛ رادیو با تلویزیون نمرد و چاپ با شبکه نمرد. هر رسانه جایگاه خود را بازتعریف می‌کند.",
        "assumptions": [
            "مرز سکوهای رسانه‌ای فرومی‌ریزد.",
            "مخاطب مشارکت‌کننده و تولیدکننده است.",
            "محتوا میان سکوها جریان می‌یابد.",
        ],
        "principles": [
            "همگرایی فرایند است، نه وضعیت.",
            "مشارکت مخاطب، محور همگرایی است.",
            "رسانه قدیم با رسانه نو حذف نمی‌شود.",
        ],
        "critiques": [
            "۱. خوش‌بینی مشارکتی: قدرت مخاطب بیش از اندازه برجسته می‌شود.\n۲. آمیختن دو جریان: همگرایی از بالا و از پایین یکسان دیده می‌شوند.\n۳. خطای جعبه سیاه: همه دستگاه‌ها یکسان فرض می‌شوند.\n۴. شکاف دیجیتال: مشارکت برای همه یکسان ممکن نیست.\n۵. کنترل صنعت: مشارکت می‌تواند کار رایگان برای صنعت باشد.",
        ],
        "applications": [
            "راهبرد محتوای چندسکویی: طراحی روایت برای چند بستر.",
            "مطالعه طرفداران: تحلیل تولید و بازتوزیع مخاطب.",
            "سواد رسانه‌ای: شناخت جریان محتوا میان سکوها.",
            "بازاریابی: هم‌آفرینی برند با اجتماع مخاطب.",
        ],
        "evolution": "جنکینز در ۲۰۰۴ منطق فرهنگی همگرایی را صورت‌بندی کرد و در ۲۰۰۶ آن را در کتاب فرهنگ همگرایی گسترد. بعدها پژوهش طرفداران، اقتصاد سکو و روایت فرا رسانه‌ای، چارچوب را به تحلیل تولید و کار مخاطب گره زد.",
        "key_concepts": [
            "همگرایی رسانه‌ای (Media Convergence)",
            "فرهنگ مشارکتی (Participatory Culture)",
            "روایت فرا رسانه‌ای (Transmedia Storytelling)",
            "هوش جمعی (Collective Intelligence)",
            "مخاطب مهاجر (Migratory Audience)",
            "همگرایی صناعتی (Industrial Convergence)",
        ],
        "studies": [
            "Jenkins, H. (2006). Convergence culture: Where old and new media collide. New York University Press.",
            "Jenkins, H. (2004). The cultural logic of media convergence. International Journal of Cultural Studies, 7(1), 33-43.",
        ],
        "theorists": "هنری جنکینز",
        "theorists_text": "جنکینز (۲۰۰۴؛ ۲۰۰۶)",
        "year": 2006,
        "model": "همگرایی فناورانه + صناعتی + فرهنگی → جریان محتوا و روایت فرا رسانه‌ای → مشارکت مخاطب و هوش جمعی → بازتعریف جایگاه هر رسانه.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nجنکینز همگرایی را از دستگاه به فرهنگ منتقل کرد و مخاطب را در مرکز تغییر نشاند. نوآوری چارچوب، پیوند اقتصاد رسانه، روایت و مشارکت طرفداران است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با تحلیل جریان محتوا، مطالعه اجتماع طرفدار و مشاهده مصرف چندسکویی انجام می‌شود. پژوهشی که تنها همگرایی فناورانه را می‌سنجد، فرهنگ مشارکتی را از دست می‌دهد؛ و پژوهشی که هر بازنشر را مشارکت خلاق می‌خواند، کار مخاطب را تورم می‌دهد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در تحلیل مصرف چندسکویی است، اما باید با اقتصاد سیاسی رسانه تکمیل شود. مشارکت بی قدرت، به کار رایگان برای صنعت بدل می‌شود.",
        "critique_text": "\n".join([
            "۱. خوش‌بینی مشارکتی: قدرت مخاطب مبالغه می‌شود.",
            "۲. آمیختن دو جریان: همگرایی بالا و پایین یکسان دیده می‌شود.",
            "۳. خطای جعبه سیاه: همه دستگاه‌ها یکسان فرض می‌شوند.",
            "۴. شکاف دیجیتال: مشارکت برای همه ممکن نیست.",
            "۵. کنترل صنعت: مشارکت به کار رایگان بدل می‌شود.",
        ]),
        "example_text": "طرفداران یک مجموعه تلویزیونی در فاصله دو فصل، سرنخ‌ها را در شبکه‌های اجتماعی گرد می‌آورند، نظریه می‌سازند و شبکه را به اصلاح روایت وامی‌دارند؛ مخاطب در این نمونه هم مصرف‌کننده است و هم تولیدکننده.",
    },
    "MC-651": {
        "summary": "(فن، ۱۹۹۵) چرخه اغراق گارتنر، الگوی پذیرش فناوری نو را در پنج مرحله ترسیم می‌کند: جرقه فناوری، قله انتظارات متورم، دره سرخوردگی، شیب روشنگری و فلات بهره‌وری. این چرخه نشان می‌دهد فناوری نو پیش از رسیدن به کاربرد پایدار، دوره اغراق و سرخوردگی را می‌گذراند. سازمان‌ها از آن برای زمان‌بندی سرمایه‌گذاری، پذیرش فناوری و گفت‌وگو با ذی‌نفعان استفاده می‌کنند. چرخه، ابزار مدیریت انتظار است نه پیش‌گویی قطعی موفقیت. رسانه‌ها نیز در ساخت قله اغراق و سپس تخریب آن نقش دارند. این چرخه در گزارش‌های سالانه فناوری به زبان مشترک مدیران و تحلیلگران بدل شد. پژوهشگران فناوری از آن برای مقایسه مسیر فناوری‌های نو بهره می‌گیرند. منتقدان آن را ابزاری روابط‌عمومی می‌دانند که هیاهو را بازتولید می‌کند.",
        "definition": "چرخه اغراق گارتنر، الگویی پنج‌مرحله‌ای است که مسیر انتظار عمومی و بلوغ فناوری نو را از جرقه اولیه تا فلات بهره‌وری پایدار توصیف می‌کند.",
        "main_problem": "مسئله این است که چرا فناوری‌های نو با انتظاری بیش از توان واقعی پذیرفته و سپس کنار گذاشته می‌شوند. پاسخ، شکاف میان انتظار اجتماعی و بلوغ فنی است. پرسش دوم، کاربرد است: چرخه کجا راهنمای سرمایه‌گذاری است و کجا به ابزار بازاریابی فروشندگان بدل می‌شود.",
        "mechanism": "۱. جرقه فناوری: نمونه اولیه یا خبر، توجه آغازین را می‌سازد.\n۲. قله انتظارات متورم: پوشش رسانه‌ای و تبلیغ، انتظار را از واقعیت جلو می‌اندازد.\n۳. دره سرخوردگی: آزمایش‌های ناکام و هزینه‌های پنهان، اعتماد را می‌شکند.\n۴. شیب روشنگری: کاربردهای واقعی و استانداردها شکل می‌گیرد.\n۵. فلات بهره‌وری: فناوری در کار روزمره مستقر می‌شود.\n۶. پایش مستمر: جایگاه هر فناوری با شواهد بازبینی می‌شود، نه با هیاهو.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا تحریریه‌ها در قله اغراق هوش مصنوعی سرمایه‌گذاری می‌کنند، چرا در دره سرخوردگی پروژه‌های واقعیت مجازی تعطیل می‌شوند و چرا فناوری بالغ، بی سر و صدا بخشی از تولید خبر می‌شود. نکته مهم این است که چرخه، پیش‌گویی نیست؛ توصیف الگوی اجتماعی انتظار است و خوانش جبری آن، خطای برنامه‌ریزی می‌سازد.",
        "assumptions": [
            "انتظار اجتماعی از بلوغ فنی جلو می‌زند.",
            "پذیرش فناوری الگویی تکرارشونده دارد.",
            "کاربرد پایدار پس از سرخوردگی می‌آید.",
        ],
        "principles": [
            "هیاهو، نشانه بلوغ نیست.",
            "زمان‌بندی پذیرش، تصمیم مدیریتی است.",
            "چرخه ابزار مدیریت انتظار است.",
        ],
        "critiques": [
            "۱. پیش‌بینی‌ناپذیری: چرخه موفقیت یا شکست فناوری را نمی‌گوید.\n۲. ذهنیت جای‌گذاری: جایگاه فناوری بر داوری تحلیلگر تکیه دارد.\n۳. خودتحقق‌بخشی: برچسب دره، سرمایه‌گذاری را پس می‌زند.\n۴. ابزار بازاریابی: فروشندگان از قله برای فروش استفاده می‌کنند.\n۵. خطی‌بودن: مسیر پذیرش همیشه پنج‌مرحله‌ای نیست.",
        ],
        "applications": [
            "ارزیابی فناوری: زمان‌بندی پذیرش ابزار تحریریه.",
            "پوشش فناوری: پرهیز از هیاهو و تخریب یک‌سویه.",
            "سرمایه‌گذاری: تفکیک انتظار از شواهد بلوغ.",
            "ارتباط با ذی‌نفعان: مدیریت انتظار مدیران و مخاطبان.",
        ],
        "evolution": "فن در ۱۹۹۵ یادداشت پژوهشی چه زمانی بر چرخه اغراق بجهیم را در گارتنر منتشر کرد. بعدها چرخه به ابزار سالانه ارزیابی فناوری‌های نو بدل شد و پژوهشگران، مفروضات خطی و ذهنی آن را نقد کردند.",
        "key_concepts": [
            "چرخه اغراق (Hype Cycle)",
            "قله انتظارات متورم (Peak of Inflated Expectations)",
            "دره سرخوردگی (Trough of Disillusionment)",
            "شیب روشنگری (Slope of Enlightenment)",
            "فلات بهره‌وری (Plateau of Productivity)",
            "بلوغ فناوری (Technology Maturity)",
        ],
        "studies": [
            "Fenn, J. (1995). When to leap on the hype cycle. Gartner Group.",
            "Linden, A., & Fenn, J. (2003). Understanding Gartner's hype cycles. Gartner Research.",
        ],
        "theorists": "جکی فن",
        "theorists_text": "فن (۱۹۹۵)",
        "year": 1995,
        "model": "جرقه فناوری → قله انتظارات → دره سرخوردگی → شیب روشنگری → فلات بهره‌وری؛ مدیریت انتظار در هر مرحله.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nفن الگوی انتظار فناوری را از داده‌های پذیرش بازار ساخت و آن را به ابزار مدیریتی بدل کرد. نوآوری چارچوب، تفکیک هیاهوی اجتماعی از بلوغ فنی است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با پایش پوشش رسانه‌ای، سرمایه‌گذاری و کاربرد واقعی انجام می‌شود. پژوهشی که تنها هیاهو را می‌سنجد، بلوغ را از دست می‌دهد؛ و پژوهشی که جایگاه را بی شواهد تعیین می‌کند، داوری تحلیلگر را به داده بدل می‌کند.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در برنامه‌ریزی فناوری رسانه است، اما باید با ارزیابی مستقل تکمیل شود. چرخه بی شواهد، به تقویم تبلیغاتی فروشندگان بدل می‌شود.",
        "critique_text": "\n".join([
            "۱. پیش‌بینی‌ناپذیری: موفقیت فناوری از چرخه برنمی‌آید.",
            "۲. ذهنیت: جای‌گذاری بر داوری تحلیلگر تکیه دارد.",
            "۳. خودتحقق‌بخشی: برچسب دره سرمایه‌گذاری را می‌ترساند.",
            "۴. بازاریابی: فروشندگان از قله سود می‌برند.",
            "۵. خطی‌بودن: مسیر پذیرش همیشه پنج‌مرحله‌ای نیست.",
        ]),
        "example_text": "تحریریه‌ای در سال نخست هیاهوی واقعیت افزوده، بودجه کلان به آزمایش اختصاص می‌دهد و در سال دوم آن را کنار می‌گذارد؛ سه سال بعد با ابزار ارزان و کاربرد روشن، همان فناوری بی سر و صدا وارد تولید خبر می‌شود.",
    },
    "MC-655": {
        "summary": "(دفت و لنگل، ۱۹۸۶) نظریه غنای رسانه می‌گوید اثربخشی ارتباط به تناسب غنای رسانه با ابهام تکلیف بستگی دارد. غنا را با چهار ویژگی می‌سنجند: ظرفیت بازخورد فوری، تعداد نشانه‌ها، تنوع زبان و تمرکز شخصی. رسانه غنی مانند گفت‌وگوی رو در رو برای تکالیف مبهم و رسانه کم‌غنا مانند سند مکتوب برای تکالیف روشن مناسب است. انتخاب نادرست، ابهام را حل نمی‌کند یا هزینه ارتباط را بی‌هوده بالا می‌برد. سازمان‌ها برای کاهش عدم‌قطعیت و رفع ابهام، ساختار و رسانه را هم‌راستا می‌کنند. این نظریه، پایه پژوهش‌های بعدی درباره انتخاب رسانه سازمانی شد.",
        "definition": "نظریه غنای رسانه، چارچوبی است که ظرفیت رسانه برای انتقال نشانه‌ها و بازخورد را با میزان ابهام تکلیف تطبیق می‌دهد و اثربخشی ارتباط را در همین تناسب می‌بیند.",
        "main_problem": "مسئله این است که چرا پیام روشن در رسانه نامناسب مبهم می‌ماند و چرا جلسه برای موضوع ساده، وقت را هدر می‌دهد. پاسخ، عدم تناسب غنا و ابهام است. پرسش دوم، انتخاب است: آیا مدیران رسانه را عقلانی انتخاب می‌کنند یا بر پایه عادت و دسترسی.",
        "mechanism": "۱. عدم‌قطعیت: کمبود اطلاعات برای تصمیم؛ با اطلاعات بیشتر کاهش می‌یابد.\n۲. ابهام: چند معنایی موضوع؛ با گفت‌وگو و نشانه‌های غنی رفع می‌شود.\n۳. بازخورد فوری: رسانه غنی امکان اصلاح سریع پیام را می‌دهد.\n۴. نشانه‌ها و زبان: چهره، صدا و لحن، معنای افزوده می‌سازند.\n۵. تمرکز شخصی: پیام برای فرد خاص تنظیم می‌شود.\n۶. تناسب: رسانه غنی برای ابهام بالا و رسانه کم‌غنا برای تکلیف روشن.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا مذاکره حساس با منبع خبری در تماس رو در رو انجام می‌شود، چرا اطلاعیه سازمانی برای خبر ساده کارآمد است و چرا ایمیل برای حل اختلاف تحریریه کافی نیست. نکته مهم این است که غنا ویژگی مطلق رسانه نیست؛ کاربرد سازمانی و زمینه اجتماعی، معنای رسانه را تغییر می‌دهد.",
        "assumptions": [
            "تکالیف در ابهام متفاوت‌اند.",
            "رسانه‌ها در غنا تفاوت دارند.",
            "انتخاب رسانه می‌تواند با تکلیف تطبیق یابد.",
        ],
        "principles": [
            "ابهام بالا، رسانه غنی می‌خواهد.",
            "تکلیف روشن، رسانه کم‌غنا می‌خواهد.",
            "رسانه نامناسب، ارتباط را پرهزینه می‌کند.",
        ],
        "critiques": [
            "۱. جبر فناورانه: ویژگی رسانه، تعیین‌کننده اثر فرض می‌شود.\n۲. سوگیری حضور: رو در رو به‌طور هنجاری برتر دیده می‌شود.\n۳. شواهد ناهمسان: کاربرد ایمیل با پیش‌بینی نظریه هم‌خوان نیست.\n۴. زمینه اجتماعی: معنا و هنجار استفاده نادیده می‌ماند.\n۵. انتخاب عقلانی: مدیران همیشه رسانه را عقلانی انتخاب نمی‌کنند.",
        ],
        "applications": [
            "ارتباط تحریریه: انتخاب رسانه متناسب با ابهام موضوع.",
            "ارتباط بحران: گفت‌وگوی غنی در ابهام و اطلاع‌رسانی کم‌غنا در خبر روشن.",
            "کار از راه دور: تشخیص جلسه لازم از پیام نوشتاری.",
            "طراحی ساختار: هم‌راستایی کانال با نیاز اطلاعاتی.",
        ],
        "evolution": "دفت و لنگل در ۱۹۸۶ نظریه را در مدیریت علم عرضه کردند و در ۱۹۸۷ با ترِوینو آزمون تجربی آن را گستردند. بعدها پژوهش رسانه سازمانی، نقد زمینه اجتماعی و مدل‌های جایگزین مانند همزمانی رسانه‌ای شکل گرفت.",
        "key_concepts": [
            "غنای رسانه (Media Richness)",
            "ابهام (Equivocality)",
            "عدم‌قطعیت (Uncertainty)",
            "بازخورد فوری (Immediate Feedback)",
            "تناسب رسانه و تکلیف (Media-Task Fit)",
            "حضور اجتماعی (Social Presence)",
        ],
        "studies": [
            "Daft, R. L., & Lengel, R. H. (1986). Organizational information requirements, media richness and structural design. Management Science, 32(5), 554-571.",
            "Daft, R. L., Lengel, R. H., & Trevino, L. K. (1987). Message equivocality, media selection, and manager performance. MIS Quarterly, 11(3), 355-366.",
        ],
        "theorists": "ریچارد دفت؛ رابرت لنگل",
        "theorists_text": "دفت و لنگل (۱۹۸۶؛ ۱۹۸۷)",
        "year": 1986,
        "model": "ابهام تکلیف × غنای رسانه (بازخورد، نشانه، زبان، تمرکز شخصی) → تناسب → اثربخشی ارتباط.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nدفت و لنگل ارتباط سازمانی را به پردازش اطلاعات گره زدند و رسانه را ابزار کاهش ابهام دیدند. نوآوری چارچوب، تفکیک عدم‌قطعیت از ابهام و ساخت سلسله‌مراتب غنا است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با تحلیل انتخاب رسانه، آزمون عملکرد و بررسی ساختار انجام می‌شود. پژوهشی که تنها ویژگی رسانه را می‌سنجد، زمینه اجتماعی را از دست می‌دهد؛ و پژوهشی که رو در رو را برتر فرض می‌کند، سوگیری حضور را وارد نتیجه می‌کند.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در انتخاب کانال ارتباطی است، اما باید با نظریه اجتماعی رسانه تکمیل شود. غنا بی زمینه، به ترجیح هنجاری رو در رو بدل می‌شود.",
        "critique_text": "\n".join([
            "۱. جبر فناورانه: ویژگی رسانه تعیین‌کننده فرض می‌شود.",
            "۲. سوگیری حضور: رو در رو هنجاری برتر دیده می‌شود.",
            "۳. شواهد ناهمسان: کاربرد ایمیل با پیش‌بینی هم‌خوان نیست.",
            "۴. زمینه اجتماعی: هنجار استفاده نادیده می‌ماند.",
            "۵. انتخاب عقلانی: مدیران همیشه عقلانی انتخاب نمی‌کنند.",
        ]),
        "example_text": "سردبیر برای حل اختلاف درباره تیتر، جلسه حضوری می‌گذارد؛ اما برای اعلام تغییر ساعت نشست، پیام نوشتاری می‌فرستد. انتخاب متناسب با ابهام، هم وقت می‌خرد و هم سوءتفاهم را کم می‌کند.",
    },
    "MC-656": {
        "summary": "(دنیس، فولر و والاسیچ، ۲۰۰۸) نظریه همزمانی رسانه‌ای می‌گوید عملکرد ارتباطی به تناسب قابلیت‌های رسانه با نیاز فرایند ارتباط بستگی دارد، نه به غنای کلی رسانه. پنج قابلیت رسانه عبارت‌اند از سرعت انتقال، موازی بودن، مجموعه نشانه‌ها، تمرین‌پذیری پیام و پردازش‌پذیری آن. دو فرایند اصلی ارتباط، انتقال اطلاعات و هم‌گرایی معنا هستند. انتقال با رسانه کم‌همزمان و هم‌گرایی با رسانه همزمان بهتر انجام می‌شود. نظریه، غنای رسانه را از سلسله‌مراتب ثابت به تطبیق فرایندی می‌برد. نظریه، به‌جای رتبه‌بندی کلی رسانه‌ها، بر ترکیب ابزارها در یک فرایند ارتباطی تأکید می‌کند و برای طراحی هم‌کاری در تیم‌های پراکنده راهنما می‌سازد. این چرخش، پژوهش رسانه سازمانی را از پرسش کدام رسانه بهتر است به پرسش کدام ترکیب برای کدام فرایند مناسب است برد.",
        "definition": "همزمانی رسانه‌ای، میزان هم‌کاری هم‌زمان افراد بر یک فعالیت با الگوی رفتار هماهنگ است و نظریه، تناسب پنج قابلیت رسانه با فرایند انتقال یا هم‌گرایی معنا را می‌سنجد.",
        "main_problem": "مسئله این است که چرا یک رسانه در یک تکلیف کارآمد و در تکلیف دیگر ناکارآمد است. پاسخ، تفاوت فرایند ارتباط است. پرسش دوم، سنجش قابلیت‌هاست: چگونه سرعت، موازی بودن و پردازش‌پذیری به عملکرد گره می‌خورند.",
        "mechanism": "۱. سرعت انتقال: رسانه سریع، چرخه بازخورد را کوتاه می‌کند.\n۲. موازی بودن: چند گفت‌وگو هم‌زمان امکان‌پذیر می‌شود.\n۳. مجموعه نشانه‌ها: تعداد کانال‌های بیان (متن، صدا، تصویر) متفاوت است.\n۴. تمرین‌پذیری: فرصت بازخوانی و اصلاح پیام پیش از ارسال.\n۵. پردازش‌پذیری: امکان بازبینی مکرر پیام در طول زمان.\n۶. تطبیق فرایندی: انتقال اطلاعات با موازی بودن و پردازش‌پذیری و هم‌گرایی معنا با سرعت و نشانه‌های غنی بهتر انجام می‌شود.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا تحریریه برای هم‌گرایی درباره خط مشی، جلسه همزمان می‌گذارد و برای انتقال گزارش‌های بلند، سند ناهمزمان می‌فرستد. در تیم‌های پراکنده، ابزار ناهمزمان می‌تواند هم‌گرایی را کند و ابزار همزمان می‌تواند انتقال را گران کند. نکته مهم این است که همزمانی، ویژگی مطلق ابزار نیست؛ ترکیب ابزارها در یک فرایند، عملکرد را می‌سازد.",
        "assumptions": [
            "قابلیت‌های رسانه چندبعدی‌اند.",
            "فرایند ارتباط دو گونه است: انتقال و هم‌گرایی.",
            "تناسب قابلیت و فرایند، عملکرد را می‌سازد.",
        ],
        "principles": [
            "هم‌گرایی معنا، همزمانی می‌خواهد.",
            "انتقال اطلاعات، ناهمزمانی می‌پذیرد.",
            "ترکیب ابزارها بر تک‌ابزار برتری دارد.",
        ],
        "critiques": [
            "۱. هم‌پوشانی ابعاد: قابلیت‌ها مستقل نیستند.\n۲. سنجش: اندازه‌گیری همزمانی دشوار است.\n۳. تفکیک تکلیف و فرایند: مرز انتقال و هم‌گرایی روشن نیست.\n۴. هنجار اجتماعی: نقش فرهنگ تیم نادیده می‌ماند.\n۵. تکرارپذیری: شواهد تجربی یکدست نیست.",
        ],
        "applications": [
            "تیم‌های پراکنده: ترکیب همزمان و ناهمزمان بر پایه فرایند.",
            "هماهنگی تحریریه: جلسه برای معنا و سند برای انتقال.",
            "مدیریت بحران: کانال همزمان برای تصمیم و کانال ناهمزمان برای مستندسازی.",
            "طراحی ابزار: قابلیت‌های متناسب با فرایند کار.",
        ],
        "evolution": "دنیس و والاسیچ در ۱۹۹۹ صورت‌بندی اولیه را در کنفرانس سیستم‌های اطلاعاتی هاوایی عرضه کردند و در ۲۰۰۸ با فولر نظریه را در فصلنامه مدیریت سیستم‌های اطلاعاتی گستردند. بعدها پژوهش هم‌کاری و ابزارهای ناهمزمان، چارچوب را آزمود.",
        "key_concepts": [
            "همزمانی رسانه‌ای (Media Synchronicity)",
            "انتقال اطلاعات (Conveyance)",
            "هم‌گرایی معنا (Convergence)",
            "موازی بودن (Parallelism)",
            "پردازش‌پذیری (Reprocessability)",
            "تمرین‌پذیری (Rehearsability)",
        ],
        "studies": [
            "Dennis, A. R., Fuller, R. M., & Valacich, J. S. (2008). Media, tasks, and communication processes. MIS Quarterly, 32(3), 575-600.",
            "Dennis, A. R., & Valacich, J. S. (1999). Rethinking media richness. Proceedings of HICSS-32.",
        ],
        "theorists": "آلن دنیس؛ رابرت فولر؛ جوزف والاسیچ",
        "theorists_text": "دنیس، فولر و والاسیچ (۲۰۰۸)",
        "year": 2008,
        "model": "پنج قابلیت رسانه × دو فرایند (انتقال/هم‌گرایی) → هم‌زمانی متناسب → عملکرد ارتباطی.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nدنیس و همکاران غنای رسانه را از سلسله‌مراتب ثابت جدا کردند و ارتباط را به دو فرایند تفکیک کردند. نوآوری چارچوب، تعریف هم‌زمانی به‌عنوان تطبیق فرایندی است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با تحلیل ابزار، زمان پاسخ و کیفیت نتیجه انجام می‌شود. پژوهشی که تنها همزمانی را می‌سنجد، انتقال را از دست می‌دهد؛ و پژوهشی که هر ابزار را یک قابلیت می‌خواند، هم‌پوشانی ابعاد را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در طراحی هم‌کاری رسانه‌ای است، اما باید با فرهنگ تیم تکمیل شود. همزمانی بی هنجار مشترک، به آشفتگی جلسه بدل می‌شود.",
        "critique_text": "\n".join([
            "۱. هم‌پوشانی: قابلیت‌ها مستقل نیستند.",
            "۲. سنجش: همزمانی سخت اندازه‌گیری می‌شود.",
            "۳. مرز مبهم: انتقال و هم‌گرایی تفکیک‌پذیر نیستند.",
            "۴. فرهنگ تیم: هنجار اجتماعی نادیده می‌ماند.",
            "۵. تکرارپذیری: شواهد یکدست نیست.",
        ]),
        "example_text": "تیم خبری پراکنده، پیش‌نویس گزارش را ناهمزمان در سند مشترک می‌نویسد و برای توافق درباره لحن، جلسه همزمان کوتاه می‌گذارد؛ ترکیب دو ابزار، هم انتقال و هم هم‌گرایی را ممکن می‌کند.",
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


NAME_FIX = {}


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
                                       "verified": n_verified, "batch": 104}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH104 THEORY DONE")


if __name__ == "__main__":
    main()
