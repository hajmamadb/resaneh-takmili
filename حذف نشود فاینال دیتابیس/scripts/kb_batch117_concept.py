# -*- coding: utf-8 -*-
"""Batch 117 (CONCEPT): full documentation for MC-524, MC-555, MC-556, MC-730."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch117-concept-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch117_concept.json"

S = {
    "MC-524": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Neocortex Size as a Constraint on Group Size in Primates",
             title_fa="اندازه نئوکورتکس به‌عنوان محدودیت اندازه گروه در نخستی‌ها",
             authors="Dunbar, R. I. M.", year=1992,
             publisher="Journal of Human Evolution",
             doi="10.1016/0047-2484(92)90081-J",
             url="https://www.sciencedirect.com/science/article/pii/004724849290081J",
             language="en", isbn=None,
             citation="Dunbar, R. I. M. (1992). Neocortex size as a constraint on group size in primates. Journal of Human Evolution, 22(6), 469-493.",
             locator="22(6):469-493", locator_type="page_range",
             supports="group size predicted by relative neocortical volume; basis of Dunbar's number", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Social Brain Hypothesis",
             title_fa="فرضیه مغز اجتماعی",
             authors="Dunbar, R. I. M.", year=1998,
             publisher="Evolutionary Anthropology",
             doi=None, url=None, language="en", isbn=None,
             citation="Dunbar, R. I. M. (1998). The social brain hypothesis. Evolutionary Anthropology, 6(5), 178-190.",
             locator="6(5):178-190", locator_type="page_range",
             supports="cognitive limits on social group size in humans", verified=False),
    ],
    "MC-555": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Mainstreaming of America: Violence Profile No. 11",
             title_fa="جریان اصلی‌شدن آمریکا: نیم‌رخ خشونت شماره ۱۱",
             authors="Gerbner, G.; Gross, L.; Morgan, M.; Signorielli, N.", year=1980,
             publisher="Journal of Communication",
             doi="10.1111/j.1460-2466.1980.tb01987.x",
             url="https://academic.oup.com/joc/article-abstract/30/3/10/4371855",
             language="en", isbn=None,
             citation="Gerbner, G., Gross, L., Morgan, M., & Signorielli, N. (1980). The mainstreaming of America: Violence profile no. 11. Journal of Communication, 30(3), 10-29.",
             locator="30(3):10-29", locator_type="page_range",
             supports="heavy viewing converges attitudes across social groups (mainstreaming)", verified=True),
        dict(kind="BOOK_CHAPTER",
             title_en="Living with Television: The Dynamics of the Cultivation Process",
             title_fa="زیستن با تلویزیون: پویایی فرایند کاشت",
             authors="Gerbner, G.; Gross, L.; Morgan, M.; Signorielli, N.", year=1986,
             publisher="Lawrence Erlbaum",
             doi=None, url=None, language="en", isbn=None,
             citation="Gerbner, G., Gross, L., Morgan, M., & Signorielli, N. (1986). Living with television: The dynamics of the cultivation process. In J. Bryant & D. Zillmann (Eds.), Perspectives on media effects (pp. 17-40). Lawrence Erlbaum.",
             locator="pp. 17-40", locator_type="page_range",
             supports="consolidated statement of mainstreaming within cultivation theory", verified=False),
    ],
    "MC-556": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Mainstreaming of America: Violence Profile No. 11",
             title_fa="جریان اصلی‌شدن آمریکا: نیم‌رخ خشونت شماره ۱۱",
             authors="Gerbner, G.; Gross, L.; Morgan, M.; Signorielli, N.", year=1980,
             publisher="Journal of Communication",
             doi="10.1111/j.1460-2466.1980.tb01987.x",
             url="https://academic.oup.com/joc/article-abstract/30/3/10/4371855",
             language="en", isbn=None,
             citation="Gerbner, G., Gross, L., Morgan, M., & Signorielli, N. (1980). The mainstreaming of America: Violence profile no. 11. Journal of Communication, 30(3), 10-29.",
             locator="30(3):10-29", locator_type="page_range",
             supports="resonance introduced as amplification of cultivation for viewers with relevant experience", verified=True),
        dict(kind="BOOK_CHAPTER",
             title_en="Living with Television: The Dynamics of the Cultivation Process",
             title_fa="زیستن با تلویزیون: پویایی فرایند کاشت",
             authors="Gerbner, G.; Gross, L.; Morgan, M.; Signorielli, N.", year=1986,
             publisher="Lawrence Erlbaum",
             doi=None, url=None, language="en", isbn=None,
             citation="Gerbner, G., Gross, L., Morgan, M., & Signorielli, N. (1986). Living with television: The dynamics of the cultivation process. In J. Bryant & D. Zillmann (Eds.), Perspectives on media effects (pp. 17-40). Lawrence Erlbaum.",
             locator="pp. 17-40", locator_type="page_range",
             supports="resonance as interaction between television content and lived experience", verified=False),
    ],
    "MC-730": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Platformization of the Web: Making Web Data Platform Ready",
             title_fa="پلتفرمی‌شدن وب: آماده‌سازی داده وب برای پلتفرم",
             authors="Helmond, A.", year=2015,
             publisher="Social Media + Society",
             doi="10.1177/2056305115603080",
             url="https://journals.sagepub.com/doi/10.1177/2056305115603080",
             language="en", isbn=None,
             citation="Helmond, A. (2015). The platformization of the web: Making web data platform ready. Social Media + Society, 1(2), 1-11.",
             locator="1(2):1-11", locator_type="page_range",
             supports="two-way platformization of the web and platform-ready data", verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Platformisation",
             title_fa="پلتفرمی‌شدن",
             authors="Poell, T.; Nieborg, D.; van Dijck, J.", year=2019,
             publisher="Internet Policy Review",
             doi=None,
             url="https://policyreview.info/concepts/platformisation",
             language="en", isbn=None,
             citation="Poell, T., Nieborg, D., & van Dijck, J. (2019). Platformisation. Internet Policy Review, 8(4).",
             locator="8(4)", locator_type="page_range",
             supports="platformization of cultural production through datafication, commodification and selection", verified=False),
    ],
}

ENRICH = {
    "MC-524": {
        "summary": "شماره دانبار، که از پژوهش رابین دانبار در ۱۹۹۲ برآمد، برآوردی شناختی از اندازه گروه پایدار انسانی است: حدود ۱۵۰ نفر. دانبار در نخستی‌ها نشان داد اندازه گروه با حجم نسبی نئوکورتکس رابطه دارد و با تعمیم این رابطه به انسان، به عددی رسید که بعدها شماره دانبار نام گرفت. پشتوانه نظری آن، فرضیه مغز اجتماعی است: مغز در فرگشت، پیش از هر چیز برای مدیریت پیچیدگی روابط اجتماعی بزرگ شده است. پژوهش‌های بعدی ساختار لایه‌ای روابط را پیشنهاد کردند: حدود ۵ نفر نزدیک، ۱۵ نفر صمیمی، ۵۰ نفر آشنا و ۱۵۰ نفر حلقه پایدار. در رسانه شبکه‌ای، عدد به معیاری برای نقد «دوستان» بی‌شمار و سنجش ظرفیت واقعی شبکه اجتماعی به کار می‌رود. نظریه توضیح می‌دهد چرا سازمان بزرگ به زیرگروه نیاز دارد و چرا فهرست تماس بی پایان، به رابطه پایدار نمی‌انجامد. نقد اصلی، قطعیت عدد و تعمیم میان‌فرهنگی است؛ بازکاوی‌های آماری، دامنه را میان ۱۰۰ تا ۲۵۰ نفر گسترده‌اند.",
        "definition": "شماره دانبار، برآوردی شناختی از شمار روابط پایدار و معناداری است که یک انسان می‌تواند حفظ کند؛ حدود ۱۵۰ نفر، بر پایه رابطه حجم مغز و اندازه گروه در نخستی‌ها.",
        "main_problem": "مسئله این است که چرا ظرفیت اجتماعی انسان محدود است و این محدودیت از کجا می‌آید. پاسخ، هزینه شناختی رابطه است. پرسش دوم، کاربرد است: سازمان و پلتفرم چگونه ساختار خود را با ظرفیت شناختی کاربر هم‌تراز کنند.",
        "mechanism": "۱. مغز اجتماعی: حجم نسبی نئوکورتکس با پیچیدگی گروه رابطه دارد.\n۲. هزینه رابطه: نگهداشت پیوند، حافظه و زمان می‌خواهد.\n۳. آستانه: با گذر از ظرفیت، کیفیت روابط کاهش می‌یابد.\n۴. لایه‌بندی: حلقه‌های نزدیک، صمیمی، آشنا و پایدار شکل می‌گیرد.\n۵. اولویت: در فشار، رابطه ضعیف‌تر کنار گذاشته می‌شود.\n۶. تعمیم: سازمان و شبکه آنلاین نیز به ساختار لایه‌ای نیاز دارند.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا کاربر با هزار «دوست» تنها با چند نفر گفت‌وگوی واقعی دارد، چرا سازمان بزرگ به واحدهای کوچک تقسیم می‌شود و چرا شبکه اجتماعی برای حفظ رابطه، سیگنال‌های ساده و مکرر می‌سازد. نکته مهم این است که عدد، سقف توان شناختی است نه هنجار مطلوب؛ از این رو، طراحی پلتفرم باید کیفیت رابطه را بر شمار تماس مقدم بدارد و سنجه موفقیت را از اندازه شبکه به پایداری پیوند تغییر دهد.",
        "assumptions": [
            "ظرفیت شناختی رابطه محدود است.",
            "اندازه گروه با حجم مغز رابطه دارد.",
            "روابط، ساختار لایه‌ای دارند.",
        ],
        "principles": [
            "شمار رابطه، معیار کیفیت نیست.",
            "نگهداشت رابطه، هزینه شناختی دارد.",
            "سازمان بزرگ به زیرگروه نیاز دارد.",
        ],
        "critiques": [
            "۱. قطعیت: عدد، برآوردی با دامنه گسترده است.\n۲. تعمیم: رابطه نخستی و انسان، ساده‌سازی می‌شود.\n۳. فرهنگ: اندازه گروه میان جوامع متفاوت است.\n۴. آنلاین: شبکه دیجیتال، هزینه نگهداشت را تغییر داده است.\n۵. سنجش: تعریف رابطه پایدار یکدست نیست.",
        ],
        "applications": [
            "طراحی سازمان: تقسیم به واحدهای کوچک.",
            "پلتفرم اجتماعی: سنجش کیفیت پیوند.",
            "مدیریت شبکه: شناخت ظرفیت ارتباطی.",
            "آموزش: مدیریت بار اجتماعی.",
        ],
        "evolution": "دانبار در ۱۹۹۲ رابطه مغز و گروه را منتشر کرد و در ۱۹۹۸ فرضیه مغز اجتماعی را گسترد. پژوهش بعدی، ساختار لایه‌ای را افزود و بازکاوی‌های آماری، دامنه عدد را بازبینی کردند.",
        "key_concepts": [
            "شماره دانبار (Dunbar's Number)",
            "فرضیه مغز اجتماعی (Social Brain Hypothesis)",
            "حجم نئوکورتکس (Neocortical Volume)",
            "حلقه پایدار (Stable Layer)",
            "هزینه نگهداشت رابطه (Relationship Maintenance Cost)",
            "ظرفیت شناختی (Cognitive Capacity)",
        ],
        "studies": [
            "Dunbar, R. I. M. (1992). Neocortex size as a constraint on group size in primates. Journal of Human Evolution, 22(6), 469-493.",
            "Dunbar, R. I. M. (1998). The social brain hypothesis. Evolutionary Anthropology, 6(5), 178-190.",
        ],
        "theorists": "رابین دانبار",
        "theorists_text": "دانبار (۱۹۹۲، ۱۹۹۸)",
        "year": 1992,
        "model": "حجم مغز → ظرفیت شناختی رابطه → اندازه گروه پایدار → لایه‌بندی روابط.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nدانبار از بوم‌شناسی رفتاری و عصب‌شناسی تطبیقی بهره گرفت. نوآوری چارچوب، پیوند ظرفیت مغز با ساختار اجتماعی است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با تحلیل تطبیقی گونه‌ها، داده شبکه و مصاحبه انجام می‌شود. پژوهشی که تنها شمار تماس را می‌سنجد، کیفیت رابطه را از دست می‌دهد؛ و پژوهشی که عدد را قانون قطعی می‌خواند، دامنه برآورد را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در نقد شبکه بی کران است، اما باید با مطالعه پلتفرم تکمیل شود. عدد بی زمینه، به شعار بدل می‌شود.",
        "critique_text": "\n".join([
            "۱. قطعیت: دامنه برآورد گسترده است.",
            "۲. تعمیم: مقایسه گونه‌ها ساده‌سازی است.",
            "۳. فرهنگ: اندازه گروه متفاوت است.",
            "۴. آنلاین: هزینه نگهداشت تغییر کرده است.",
            "۵. سنجش: تعریف رابطه یکدست نیست.",
        ]),
        "example_text": "کاربری با هزار پیوند آنلاین، در بحران تنها با چند نفر تماس می‌گیرد؛ ظرفیت شناختی، شبکه نمایشی را به حلقه کوچک پایدار فرو می‌کاهد.",
    },
    "MC-555": {
        "summary": "مفهوم جریان اصلی، که گربر و همکاران در ۱۹۸۰ در نیم‌رخ خشونت شماره ۱۱ عرضه کردند، توضیح می‌دهد چگونه تماشای سنگین تلویزیون، نگرش گروه‌های اجتماعی متفاوت را به هم نزدیک می‌کند. در این چارچوب، تلویزیون جریان اصلی فرهنگی می‌سازد: بینندگان پرمصرف، فارغ از پایگاه اجتماعی، برداشت‌های همگراتری از جهان پیدا می‌کنند، در حالی که کم‌مصرف‌ها واگرایی بیشتری نشان می‌دهند. سازوکار، کاشت تدریجی و مکرر تصویرهای مشترک است: تلویزیون با تکرار، مفروضات مشترکی درباره خطر، اعتماد و نظم اجتماعی می‌سازد. جریان اصلی به تفاوت کاشت میان گروه‌ها توجه می‌دهد: هرچه تماشا بیشتر، شکاف گروه‌ها کوچک‌تر. در محیط رسانه‌ای خردشده، این مفهوم به پرسش تازه‌ای بدل شده است: آیا پلتفرم‌های مشترک، جریان اصلی تازه می‌سازند یا خردگی رسانه، آن را از میان می‌برد. اهمیت نظری آن، پیوند مصرف رسانه با همگن‌شدن فرهنگی است.",
        "definition": "جریان اصلی، فرایندی است که در آن مصرف سنگین رسانه، نگرش‌ها و برداشت‌های گروه‌های اجتماعی متفاوت را به یک جریان فرهنگی مشترک نزدیک می‌کند.",
        "main_problem": "مسئله این است که چرا گروه‌های اجتماعی متفاوت، برداشت‌های مشابهی از جهان پیدا می‌کنند. پاسخ، تلویزیون به‌عنوان جریان اصلی است. پرسش دوم، دیجیتال است: رسانه خردشده، جریان اصلی را تقویت می‌کند یا از میان می‌برد.",
        "mechanism": "۱. مصرف سنگین: تکرار پیوسته، تصویر جهان را تثبیت می‌کند.\n۲. پیام مشترک: تلویزیون، مفروضات مشترک عرضه می‌کند.\n۳. همگرایی: نگرش گروه‌ها به هم نزدیک می‌شود.\n۴. واگرایی کم‌مصرف: کم‌مصرف‌ها وابسته به تجربه و گروه خود می‌مانند.\n۵. تفاضل کاشت: شکاف گروه‌ها با مصرف بیشتر کوچک‌تر می‌شود.\n۶. بازتولید: جریان اصلی، هنجار و سیاست را شکل می‌دهد.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا بینندگان پرمصرف با وجود تفاوت طبقه، برداشت مشابهی از جرم دارند، چرا تلویزیون عمومی گاه همگن‌ساز است و چرا رسانه خردشده، جریان‌های موازی می‌سازد. نکته مهم این است که جریان اصلی، یکدست‌سازی مطلق نیست؛ همگرایی در برخی موضوع‌ها رخ می‌دهد و در برخی نه؛ از این رو، سنجش آن نیازمند تفاضل گروهی و کنترل متغیرهای زمینه است، نه مقایسه ساده میانگین‌ها.",
        "assumptions": [
            "تلویزیون پیام فرهنگی مشترک می‌سازد.",
            "مصرف سنگین، برداشت را همگرا می‌کند.",
            "کم‌مصرف‌ها وابسته‌تر به تجربه‌اند.",
        ],
        "principles": [
            "جریان اصلی در تفاضل گروه‌ها دیده می‌شود.",
            "تکرار، مفروضات مشترک می‌سازد.",
            "همگرایی، در همه موضوع‌ها رخ نمی‌دهد.",
        ],
        "critiques": [
            "۱. آماری: برخی یافته‌ها به اثر آماری کاذب نسبت داده شدند.\n۲. سنجش: تفاضل گروهی، حساس به تعریف متغیرهاست.\n۳. تغییر: منظومه رسانه‌ای از تلویزیون فراتر رفته است.\n۴. زمینه: جریان اصلی در جوامع تک‌رسانه‌ای قوی‌تر است.\n۵. علیت: همبستگی مصرف و نگرش، جهت علی را نشان نمی‌دهد.",
        ],
        "applications": [
            "پژوهش کاشت: سنجش تفاضل گروهی.",
            "سیاست رسانه: تحلیل همگن‌سازی فرهنگی.",
            "رسانه عمومی: ارزیابی پیام مشترک.",
            "مطالعات دیجیتال: جریان اصلی در پلتفرم.",
        ],
        "evolution": "گربر و همکاران در ۱۹۸۰ جریان اصلی را با نیم‌رخ خشونت عرضه کردند، نقدهای آماری دهه ۱۹۸۰ آن را بازبینی کرد و پژوهش دیجیتال، پرسش جریان اصلی را به پلتفرم منتقل کرد.",
        "key_concepts": [
            "جریان اصلی (Mainstreaming)",
            "تفاضل کاشت (Cultivation Differential)",
            "مصرف سنگین (Heavy Viewing)",
            "واگرایی (Divergence)",
            "پیام مشترک (Shared Message)",
            "همگن‌سازی فرهنگی (Cultural Homogenization)",
        ],
        "studies": [
            "Gerbner, G., Gross, L., Morgan, M., & Signorielli, N. (1980). The mainstreaming of America. Journal of Communication, 30(3), 10-29.",
            "Gerbner, G., Gross, L., Morgan, M., & Signorielli, N. (1986). Living with television. In Perspectives on media effects (pp. 17-40). Lawrence Erlbaum.",
        ],
        "theorists": "جرج گربر؛ لری گراس؛ مایکل مورگان؛ نانسی سینیوریلی",
        "theorists_text": "گربر و همکاران (۱۹۸۰، ۱۹۸۶)",
        "year": 1980,
        "model": "مصرف سنگین پیام مشترک → همگرایی نگرش گروه‌ها → جریان اصلی فرهنگی.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nجریان اصلی در چارچوب نظریه کاشت شکل گرفت و کوشید تفاوت اثر میان گروه‌ها را توضیح دهد. نوآوری آن، تحلیل تفاضل به جای میانگین است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با پیمایش و تحلیل تفاضل گروهی انجام می‌شود. پژوهشی که تنها میانگین را می‌خواند، همگرایی را از دست می‌دهد؛ و پژوهشی که هر شباهت را جریان اصلی می‌خواند، اثر گزینش را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در تحلیل همگن‌سازی است، اما باید با داده پلتفرم تکمیل شود. جریان اصلی در محیط خردشده، به پرسش تجربی بدل می‌شود.",
        "critique_text": "\n".join([
            "۱. آماری: اثر کاذب ممکن است.",
            "۲. سنجش: تفاضل حساس است.",
            "۳. تغییر: منظومه رسانه‌ای دگرگون شده است.",
            "۴. زمینه: جوامع تک‌رسانه‌ای متفاوت‌اند.",
            "۵. علیت: جهت اثر روشن نیست.",
        ]),
        "example_text": "دو گروه با پایگاه اجتماعی متفاوت، هر دو بیننده پرمصرف تلویزیون، برداشت مشابهی از میزان جرم پیدا می‌کنند؛ جریان اصلی در تفاضل کوچک‌شده آن‌ها دیده می‌شود.",
    },
    "MC-556": {
        "summary": "مفهوم طنین، که گربر و همکاران در ۱۹۸۰ همراه با جریان اصلی عرضه کردند، توضیح می‌دهد چرا اثر کاشت برای برخی بینندگان قوی‌تر است. طنین زمانی رخ می‌دهد که محتوای تلویزیون با تجربه زیسته بیننده هم‌خوان شود؛ در این حالت، پیام رسانه و تجربه واقعی یکدیگر را تقویت می‌کنند و اثر دوچندان می‌شود. نمونه کلاسیک، ساکنان شهرهای بزرگ و موضوع جرم است: کسی که در محله پرجرم زندگی می‌کند، هم از تلویزیون و هم از تجربه خود، تصویر خطر می‌گیرد. طنین، برخلاف جریان اصلی که همگرایی می‌سازد، تفاوت تجربه را برجسته می‌کند. این مفهوم در پژوهش سوگیری شناختی و دسترس‌پذیری نیز تفسیر شده است: محتوای هم‌خوان با تجربه، آسان‌تر به یاد می‌آید و داوری را هدایت می‌کند. نقد اصلی، دشواری سنجش تجربه و ناهمخوانی یافته‌هاست. اهمیت آن، نشان‌دادن تعامل رسانه و زندگی روزمره است.",
        "definition": "طنین، تقویت اثر رسانه است زمانی که محتوای رسانه با تجربه مستقیم مخاطب هم‌خوان شود و پیام رسانه و تجربه واقعی یکدیگر را تقویت کنند.",
        "main_problem": "مسئله این است که چرا اثر رسانه برای همه یکسان نیست. پاسخ، هم‌خوانی محتوا با تجربه است. پرسش دوم، سنجش است: تجربه زیسته را چگونه می‌توان مستقل از مصرف رسانه اندازه گرفت.",
        "mechanism": "۱. هم‌خوانی: محتوای رسانه با تجربه مخاطب می‌خواند.\n۲. تقویت دوگانه: رسانه و تجربه، یک پیام را تقویت می‌کنند.\n۳. دسترس‌پذیری: نمونه‌های هم‌خوان، آسان‌تر به یاد می‌آیند.\n۴. تعمیم: نمونه ذهنی، داوری درباره جهان را شکل می‌دهد.\n۵. تفاوت گروهی: طنین، شکاف تجربه را برجسته می‌کند.\n۶. زمینه: در موضوع‌های نزدیک به زندگی، طنین قوی‌تر است.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا پوشش جرم بر ساکنان محله پرجرم اثر بیشتری دارد، چرا تبلیغ سلامت برای بیماران هم‌خوان‌تر است و چرا فید شخصی‌سازی‌شده می‌تواند طنین مصنوعی بسازد. نکته مهم این است که طنین، هم اثر رسانه را تقویت می‌کند و هم خطر قطبی‌شدن را بالا می‌برد؛ از این رو، سنجش آن نیازمند تفکیک تجربه واقعی از مواجهه رسانه‌ای است، نه پرسش ساده درباره میزان تماشا.",
        "assumptions": [
            "تجربه مخاطب، اثر رسانه را تعدیل می‌کند.",
            "محتوای هم‌خوان، دسترس‌پذیرتر است.",
            "طنین، تفاوت گروهی می‌سازد.",
        ],
        "principles": [
            "رسانه و تجربه، اثر را تقویت می‌کنند.",
            "طنین، برخلاف جریان اصلی، واگرا است.",
            "سنجش تجربه، شرط اعتبار است.",
        ],
        "critiques": [
            "۱. سنجش: تجربه زیسته سخت اندازه‌گیری می‌شود.\n۲. یافته: نتایج طنین در پژوهش‌ها ناهمخوان است.\n۳. علیت: تفکیک تجربه و مواجهه رسانه‌ای دشوار است.\n۴. زمینه: موضوع‌های نزدیک به زندگی، اثر را تغییر می‌دهند.\n۵. دیجیتال: طنین مصنوعی الگوریتمی، مفهوم را پیچیده کرده است.",
        ],
        "applications": [
            "پژوهش کاشت: کنترل تجربه در مدل.",
            "سلامت عمومی: پیام هم‌خوان با تجربه بیمار.",
            "نقد الگوریتم: شناخت طنین مصنوعی.",
            "سیاست رسانه: تحلیل قطبی‌شدن.",
        ],
        "evolution": "گربر و همکاران در ۱۹۸۰ طنین را در نظریه کاشت گنجاندند، پژوهش‌های بعدی آن را با دسترس‌پذیری شناختی تفسیر کردند و مطالعات پلتفرم، طنین الگوریتمی را افزودند.",
        "key_concepts": [
            "طنین (Resonance)",
            "تجربه زیسته (Lived Experience)",
            "دسترس‌پذیری (Accessibility)",
            "اثر دوچندان (Double Dose)",
            "تفاوت گروهی (Group Difference)",
            "طنین مصنوعی (Algorithmic Resonance)",
        ],
        "studies": [
            "Gerbner, G., Gross, L., Morgan, M., & Signorielli, N. (1980). The mainstreaming of America. Journal of Communication, 30(3), 10-29.",
            "Gerbner, G., Gross, L., Morgan, M., & Signorielli, N. (1986). Living with television. In Perspectives on media effects (pp. 17-40). Lawrence Erlbaum.",
        ],
        "theorists": "جرج گربر؛ لری گراس؛ مایکل مورگان؛ نانسی سینیوریلی",
        "theorists_text": "گربر و همکاران (۱۹۸۰، ۱۹۸۶)",
        "year": 1980,
        "model": "محتوای هم‌خوان با تجربه → تقویت دوگانه → دسترس‌پذیری → داوری شدت‌یافته.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nطنین، اصلاحی در نظریه کاشت بود که تفاوت اثر را توضیح می‌داد. نوآوری آن، پیوند محتوای رسانه با تجربه روزمره است.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با تفکیک گروه‌های تجربه‌ای و تحلیل تعامل انجام می‌شود. پژوهشی که تجربه را از مصرف جدا نمی‌کند، طنین را از دست می‌دهد؛ و پژوهشی که هر تفاوت گروهی را طنین می‌خواند، اثر گزینش را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در تحلیل اثر زمینه‌ای است، اما باید با داده تجربه تکمیل شود. طنین بی تفکیک، به تفسیر پس‌رو بدل می‌شود.",
        "critique_text": "\n".join([
            "۱. سنجش: تجربه سخت اندازه‌پذیر است.",
            "۲. یافته: نتایج ناهمخوان‌اند.",
            "۳. علیت: تفکیک دشوار است.",
            "۴. زمینه: اثر موضوع مهم است.",
            "۵. دیجیتال: طنین مصنوعی تازه است.",
        ]),
        "example_text": "ساکن محله پرجرم با دیدن خبرهای جرم، تصویری شدیدتر از خطر می‌سازد؛ پیام تلویزیون و تجربه روزمره، یکدیگر را طنین می‌دهند.",
    },
    "MC-730": {
        "summary": "پلتفرمی‌شدن، مفهومی است که هلموند در ۲۰۱۵ برای توصیف تبدیل پلتفرم به مدل غالب زیرساختی و اقتصادی وب اجتماعی صورت‌بندی کرد. در این چارچوب، پلتفرمی‌شدن فرایندی دوطرفه است: پلتفرم‌ها زیرساخت خود را به سراسر وب گسترش می‌دهند و در همان حال، داده و فعالیت وب را به درون خود می‌کشند و آن را برای پلتفرم آماده می‌کنند. پول، نیبورگ و ون دایک در ۲۰۱۹ این مفهوم را به تولید فرهنگی گستردند و سه بُعد آن را برشمردند: داده‌ای‌شدن، کالایی‌شدن و گزینش‌گری. پلتفرمی‌شدن تنها فناوری نیست؛ نهادمندشدن منطق پلتفرم در اقتصاد، سیاست و فرهنگ است. در رسانه، این چارچوب توضیح می‌دهد چرا خبر به فید وابسته می‌شود، چرا سنجه تعامل، ارزش خبری را تغییر می‌دهد و چرا زیرساخت داده، قدرت تازه‌ای می‌سازد. نقد اصلی، تمرکز بر پلتفرم‌های غربی و کم‌توجهی به کارگران و مقررات است. اهمیت آن، پیوند زیرساخت فنی با قدرت اقتصادی و فرهنگی است.",
        "definition": "پلتفرمی‌شدن، فرایند گسترش زیرساخت و منطق پلتفرم به حوزه‌های دیگر و بازگرداندن داده و فعالیت آن حوزه‌ها به پلتفرم است؛ نهادمندشدن منطق داده، کالا و گزینش پلتفرمی.",
        "main_problem": "مسئله این است که چرا پلتفرم به شکل غالب سازمان‌دهی رسانه و فرهنگ بدل شده است. پاسخ، گسترش زیرساخت و داده است. پرسش دوم، پیامد است: وابستگی رسانه به پلتفرم چه اثری بر استقلال و تنوع دارد.",
        "mechanism": "۱. گسترش بیرونی: پلتفرم، زیرساخت خود را به وب و رسانه دیگر می‌برد.\n۲. جذب درونی: داده فعالیت‌ها به پلتفرم بازمی‌گردد.\n۳. آماده‌سازی داده: داده، ساختارمند و قابل پردازش می‌شود.\n۴. داده‌ای‌شدن: رفتار به داده سنجش‌پذیر بدل می‌شود.\n۵. کالایی‌شدن: داده و توجه، به ارزش بازار ترجمه می‌شود.\n۶. گزینش: الگوریتم، دیده‌شدن و دسترسی را تعیین می‌کند.\n\nدر بستر رسانه، این چارچوب توضیح می‌دهد چرا رسانه خبری به ترافیک پلتفرم وابسته می‌شود، چرا سنجه‌های تعامل به تحریریه نفوذ می‌کنند و چرا مقررات پلتفرم به موضوع سیاست رسانه بدل شده است. نکته مهم این است که پلتفرمی‌شدن، تنها تسخیر بازار نیست؛ بازآرایی زیرساخت معناست؛ از این رو، ارزیابی آن باید سه سطح زیرساخت، اقتصاد و فرهنگ را هم‌زمان ببیند و استقلال رسانه را در وابستگی زیرساختی بسنجد.",
        "assumptions": [
            "پلتفرم، مدل غالب وب است.",
            "داده، منبع اصلی ارزش است.",
            "منطق پلتفرم به حوزه‌های دیگر گسترش می‌یابد.",
        ],
        "principles": [
            "پلتفرمی‌شدن دوطرفه است.",
            "داده‌ای‌شدن، پیش‌شرط کالایی‌شدن است.",
            "وابستگی زیرساختی، استقلال را محدود می‌کند.",
        ],
        "critiques": [
            "۱. تمرکز: پلتفرم‌های بزرگ غربی، نمونه اصلی‌اند.\n۲. کار: نیروی کار پلتفرمی کم دیده می‌شود.\n۳. عاملیت: مقاومت کاربر و رسانه کم تحلیل است.\n۴. مقررات: اثر قانون‌گذاری تازه ارزیابی نشده است.\n۵. تعمیم: پلتفرمی‌شدن در هر بخش یکسان نیست.",
        ],
        "applications": [
            "سیاست رسانه: تحلیل وابستگی به پلتفرم.",
            "تحریریه: مقاومت در برابر سنجه تعامل.",
            "حکمرانی داده: شفافیت زیرساخت.",
            "پژوهش پلتفرم: تحلیل سه‌سطحی.",
        ],
        "evolution": "هلموند در ۲۰۱۵ پلتفرمی‌شدن وب را صورت‌بندی کرد و پول و همکاران در ۲۰۱۹ آن را به تولید فرهنگی گستردند. پژوهش مقررات پلتفرم، ابعاد حقوقی و کار را افزود.",
        "key_concepts": [
            "پلتفرمی‌شدن (Platformization)",
            "آماده‌سازی داده برای پلتفرم (Platform-Ready Data)",
            "داده‌ای‌شدن (Datafication)",
            "کالایی‌شدن (Commodification)",
            "گزینش‌گری (Selection)",
            "وابستگی زیرساختی (Infrastructural Dependency)",
        ],
        "studies": [
            "Helmond, A. (2015). The platformization of the web. Social Media + Society, 1(2), 1-11.",
            "Poell, T., Nieborg, D., & van Dijck, J. (2019). Platformisation. Internet Policy Review, 8(4).",
        ],
        "theorists": "آن هلموند؛ توماس پول؛ دیوید نیبورگ؛ خوزه ون دایک",
        "theorists_text": "هلموند (۲۰۱۵)؛ پول و همکاران (۲۰۱۹)",
        "year": 2015,
        "model": "گسترش زیرساخت پلتفرم → جذب داده → داده‌ای‌شدن → کالایی‌شدن و گزینش.",
        "detailed_analysis": "۱. بنیان و منطق نظری\nهلموند پلتفرمی‌شدن را از مطالعه وب اجتماعی و رابط برنامه‌نویسی بیرون آورد. نوآوری چارچوب، دیدن پلتفرم به‌عنوان زیرساخت است، نه فقط سرویس.\n\n۲. منطق سنجش و دام‌های آن\nسنجش با تحلیل زیرساخت، ردیابی داده و مصاحبه انجام می‌شود. پژوهشی که تنها رابط کاربر را می‌بیند، زیرساخت را از دست می‌دهد؛ و پژوهشی که هر حضور آنلاین را پلتفرمی‌شدن می‌خواند، تفاوت درجه وابستگی را نادیده می‌گیرد.\n\n۳. دلالت رسانه‌ای و محدودیت‌ها\nقدرت چارچوب در تحلیل وابستگی رسانه است، اما باید با مطالعه کار و مقررات تکمیل شود. پلتفرم بی قاعده، به انحصار زیرساختی بدل می‌شود.",
        "critique_text": "\n".join([
            "۱. تمرکز: نمونه‌ها غربی‌اند.",
            "۲. کار: نیروی کار کم دیده می‌شود.",
            "۳. عاملیت: مقاومت کم تحلیل است.",
            "۴. مقررات: اثر قانون ارزیابی نشده است.",
            "۵. تعمیم: بخش‌ها یکسان نیستند.",
        ]),
        "example_text": "رسانه‌ای که خبر خود را تنها از راه فید پلتفرم توزیع می‌کند، با تغییر یک قاعده رتبه‌بندی، مخاطب خود را از دست می‌دهد؛ پلتفرمی‌شدن، وابستگی زیرساختی می‌سازد.",
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
YEAR_FIX = {
    "MC-556": "year filled: none -> 1980 (resonance introduced in Gerbner et al. 1980, Violence Profile No. 11)",
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
                                       "verified": n_verified, "batch": 117}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH117 CONCEPT DONE")


if __name__ == "__main__":
    main()
