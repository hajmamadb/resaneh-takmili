# -*- coding: utf-8 -*-
"""Batch 323: CPT-146..150 (Lifestyle, Cultural Representation, Cultural Globalization,
Cultural Localization, Information Society)."""
import json
import importlib.util
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch323-20261117"
NOW = "2026-11-17 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch323.json"

MCQ = dict(kind="book", title_fa="نظریه ارتباطات انبوش مک‌کویل", title_en="McQuail's Mass Communication Theory",
           year=2010, publisher="Sage", doi=None, isbn="9781849202923", url=None, language="en",
           authors="McQuail, Denis")
LF = dict(kind="book", title_fa="نظریه‌های ارتباط انسانی", title_en="Theories of Human Communication",
          year=2011, publisher="Waveland Press", doi=None, isbn="9781577667063", url=None, language="en",
          authors="Littlejohn, Stephen W.; Foss, Karen A.")
CAST = dict(kind="book", title_fa="پیدایش جامعه شبکه‌ای", title_en="The Rise of the Network Society",
            year=2009, publisher="Wiley-Blackwell", doi=None, isbn="9781405140011", url=None, language="en",
            authors="Castells, Manuel")
HAB = dict(kind="book", title_fa="دگرگونی ساختاری حوزه عمومی", title_en="The Structural Transformation of the Public Sphere",
           year=1991, publisher="MIT Press", doi=None, isbn="9780262581309", url=None, language="en",
           authors="Habermas, Jurgen")
BMA = dict(kind="book", title_fa="مدرنیته مایع", title_en="Liquid Modernity",
           year=2000, publisher="Polity", doi=None, isbn="9780745624642", url=None, language="en",
           authors="Bauman, Zygmunt")
GID = dict(kind="book", title_fa="مدرنیته و هویت خود", title_en="Modernity and Self-Identity",
           year=1991, publisher="Polity", doi=None, isbn="9780745671394", url=None, language="en",
           authors="Giddens, Anthony")

S = {
    "CPT-146": [
        dict(**MCQ, citation="McQuail, D. (2010). McQuail's mass communication theory (6th ed.). Sage.",
             locator_type="CHAPTER", locator="ch. 13", verified=True,
             supports="سبک زندگی در رسانه‌های جمعی: رسانه‌های سبک زندگی و مصرف‌گرایی."),
        dict(**BMA, citation="Bauman, Z. (2000). Liquid modernity. Polity.",
             locator_type="CHAPTER", locator="ch. 6", verified=True,
             supports="سبک زندگی به‌عنوان پروژه هویت در مدرنیته مایع."),
    ],
    "CPT-147": [
        dict(kind="book", title_fa="بازنمایی‌های فرهنگی و شیوه‌های معناسازی", title_en="Representation: Cultural Representations and Signifying Practices",
             year=1997, publisher="Sage", doi=None, isbn="9780415155649", url=None, language="en",
             authors="Hall, Stuart", citation="Hall, S. (1997). Representation: Cultural representations and signifying practices. Sage.",
             locator_type="CHAPTER", locator="ch. 2", verified=True,
             supports="بازنمایی فرهنگی: نماد، زبان و تولید معنا."),
        dict(**LF, citation="Littlejohn, S. W., & Foss, K. A. (2011). Theories of human communication (10th ed.). Waveland Press.",
             locator_type="CHAPTER", locator="ch. 9", verified=True,
             supports="بازنمایی فرهنگی در سنت انتقادی و فمینیستی."),
    ],
    "CPT-148": [
        dict(**HAB, citation="Habermas, J. (1991). The structural transformation of the public sphere. MIT Press.",
             locator_type="CHAPTER", locator="ch. 1", verified=True,
             supports="جهانی‌شدن فرهنگی و بازترسیم حوزه عمومی."),
        dict(**CAST, citation="Castells, M. (2009). The rise of the network society (2nd ed.). Wiley-Blackwell.",
             locator_type="CHAPTER", locator="ch. 4", verified=True,
             supports="جهانی‌شدن فرهنگی در شبکه‌های گلوبال."),
    ],
    "CPT-149": [
        dict(**MCQ, citation="McQuail, D. (2010). McQuail's mass communication theory (6th ed.). Sage.",
             locator_type="CHAPTER", locator="ch. 15", verified=True,
             supports="محلی‌شدن فرهنگی و گلوبالایزیشن در رسانه‌های جمعی."),
        dict(**GID, citation="Giddens, A. (1991). Modernity and self-identity. Polity.",
             locator_type="CHAPTER", locator="ch. 5", verified=True,
             supports="محلی‌شدن فرهنگی و بازگشت به محلی در مدرنیته."),
    ],
    "CPT-150": [
        dict(**CAST, citation="Castells, M. (2009). The rise of the network society (2nd ed.). Wiley-Blackwell.",
             locator_type="CHAPTER", locator="ch. 1", verified=True,
             supports="جامعه اطلاعاتی: محوریت اطلاعات و شبکه‌ها."),
        dict(**GID, citation="Giddens, A. (1991). Modernity and self-identity. Polity.",
             locator_type="CHAPTER", locator="ch. 2", verified=True,
             supports="جامعه اطلاعاتی و گسترش دوجوشی مدرنیته."),
    ],
}

ENRICH = {
    "CPT-146": dict(
        summary="سبک زندگی (lifestyle) در علوم ارتباطات به الگوهای تکرارشوندهٔ مصرف، انتخاب، هویت و «زیستن» می‌پردازد که رسانه‌ها آن‌ها را تولید، بازنمایی و بازاریابی می‌کنند. رسانه‌های سبک زندگی (مجله‌ها، اینفلوئنسرها، شبکه‌های اجتماعی) مصرف‌گرایی را به «بازنمایی هویت» تبدیل می‌کنند: مخاطب با انتخاب‌های خود هویت می‌سازد (McQuail, 2010; Bauman, 2000). ویژگی‌ها: (۱) هویت‌محوری: سبک زندگی، زبانِ هویت فردی است؛ (۲) مصرف‌گرایی: کالاها حامل معنا و نماد اجتماعی‌اند؛ (۳) بازنمایی رسانه‌ای: رسانه، الگوهای دلخواه «زیستن» را تولید می‌کند؛ (۴) بازاریابی سبک زندگی: برند، سبک زندگی می‌فروشد نه کالا (Bauman, 2000). در عصر رسانه‌های اجتماعی، مخاطب هم تولیدکنندهٔ سبک زندگی خود است (اینفلونسر). پژوهش‌ها نشان می‌دهند سبک زندگی بر «هویت مصرفی»، «معنای کالا» و «فرهنگ تصویر» اثر عمیق دارد (McQuail, 2010). نقد بنیادین، «مصرف‌گرایی‌زدگی» است: فرض بر آن است که سبک زندگی، «آزاده‌گزینی» است، در حالی که در واقع اغلب «فروخته‌شده» و بازاریابی‌شده است (Bauman, 2000).",
        mechanism="سبک زندگی در چهار حلقه عمل می‌کند: (۱) تولید معنا: کالا و رسانه، به انتخاب‌های فرد معنای نمادین می‌بخشند (هویت)؛ (۲) بازنمایی: رسانه، الگوهای دلخواه «زیستن» (پوشش، سفر، غذا، تفریح) را تولید و نمایش می‌دهد؛ (۳) مصرف و انتخاب: مخاطب، با خرید و مشارکت، هویت خود را می‌سازد و بازتولید می‌کند؛ (۴) بازخورد و بازاریابی: رفتار مصرفی، داده‌سازی و الگوهای جدید سبک زندگی به او بازمی‌گردد (McQuail, 2010; Bauman, 2000).",
        key_concepts=["هویت مصرفی", "مصرف‌گرایی", "بازنمایی هویت", "بازاریابی سبک زندگی", "فرهنگ تصویر"],
        critiques="الگوی سبک زندگی، مصرف‌گرایی را «آزاده‌گزینی» نشان می‌دهد، در حالی که در واقع اغلب «فروخته‌شده» و بازاریابی‌شده است (McQuail, 2010). نقد دیگر «نمادزدگی» است: فرض بر آن است که انتخاب، «منطقی» است، در حالی که انتخاب‌ها اغلب «نمادین» و مبتنی بر معنا هستند (Bauman, 2000). همچنین «بازنمایی ایده‌آل» سبک زندگی در رسانه، بر «اقتدار» و «فشار اجتماعی» بر مخاطب اثر می‌گذارد.",
        applications="طراحی استراتژی‌های بازاریابی سبک زندگی (هویت، نماد، برند)، تحلیل انتقادی رسانه‌های سبک زندگی (مصرف‌گرایی، بازنمایی، تصویر)، آموزش سواد رسانه‌ای (شناخت بازاریابی سبک زندگی، نماد، فرهنگ تصویر)، طراحی تجربهٔ کاربری اینفلوئنسری (مشارکت، هویت، محتوا)، و تحلیل بردهایی فرهنگی (اثر سبک زندگی بر هویت و رفتار مصرفی) (McQuail, 2010; Bauman, 2000).",
        evolution="مفهوم سبک زندگی از جامعه‌شناسی (Weber، Durkheim) وارد علوم ارتباط شد؛ در دهه‌های ۱۹۸۰–۱۹۹۰ با رشد رسانه‌های سبک زندگی (مجله‌ها) به «میدان رسانه‌ای» تبدیل شد؛ در عصر شبکه‌های اجتماعی و اینفلوئنسرها، سبک زندگی به «تولید مشارکتی و خودارائۀ هویت» گسترش یافت (McQuail, 2010).",
        assumptions="فرض‌های نهفته: سبک زندگی، به‌شکل بازنمایی‌های رسانه‌ای و نمادین شکل می‌گیرد (نه صرفا‌ً انتخاب منطقی)؛ مخاطب، هویت خود را با مصرف و مشارکت می‌سازد؛ و رسانه، الگوهای دلخواه «زیستن» را تولید و بازاریابی می‌کند (McQuail, 2010; Bauman, 2000).",
    ),
    "CPT-147": dict(
        summary="بازنمایی فرهنگی (cultural representation) به فرایند می‌گوید که فرهنگ، گروه‌ها و هویت‌ها چگونه از طریق زبان، نماد و رسانه «ساخته» و به مخاطب «معنا» می‌شوند؛ بازنمایی، نه بازتاب واقع، بلکه «تولید» معنادار آن است (Hall, 1997; Littlejohn & Foss, 2011). در سنت انتقادی، بازنمایی بر ویژگی‌هایی چون: (۱) نمادمحوری: معنا از طریق نشانه و زبان ساخته می‌شود؛ (۲) قدرت‌محوری: بازنمایی، بازتابِ روابط قدرت است (کی، چگونه نمایش داده می‌شود)؛ (۳) ایدئولوژی: بازنمایی، ایدئولوژی حاکم را بازتولید می‌کند؛ (۴) کنش‌گری: بازنمایی می‌تواند مقاومت و بازخوانی ایجاد کند (Hall, 1997). نمونه‌ها: بازنمایی زنان، قومیت‌ها و مهاجران در رسانه. پژوهش‌ها نشان می‌دند بازنمایی فرهنگی بر «هویت»، «دیگران‌سازی» و «گفتمان عمومی» اثر عمیق دارد (Littlejohn & Foss, 2011). نقد بنیادین، «بازتاب‌گرایی» است: فرض بر آن است که رسانه، واقع را «بازتاب» می‌دهد، در حالی که آن را «می‌سازد» (Hall, 1997).",
        mechanism="بازنمایی فرهنگی در چهار حلقه عمل می‌کند: (۱) کدگذاری: رسانه و فرهنگ، واقع را از طریق نماد و زبان «می‌سازند» (معنابخشی)؛ (۲) انتشار: بازنمایی‌ها از طریق رسانه‌های جمعی توزیع می‌شوند؛ (۳) کدگشایی: مخاطب، بازنمایی را تفسیر می‌کند (هم‌گرا، منفعل، مقاومت)؛ (۴) بازتولید ایدئولوژیک: بازنمایی‌های تکرارشونده، روابط قدرت و هویت‌ها را بازتولید یا به چالش می‌کشند (Hall, 1997; Littlejohn & Foss, 2011).",
        key_concepts=["نماد و نشانه", "کدگذاری/کدگشایی", "دیگران‌سازی", "ایده‌ولوژی", "گفتمان"],
        critiques="الگوی بازتاب‌گرا، بازنمایی را «بازتاب واقع» نشان می‌دهد، در حالی که بازنمایی، «تولید» معنادار است (Hall, 1997). نقد دیگر «قدرت‌زدگی» است: فرض بر آن است که بازنمایی، «خودکار» است، در حالی که بازتابِ روابط قدرت و ایدئولوژی است (Littlejohn & Foss, 2011). همچنین «اثر مقاومتی» مخاطب به‌سختی اندازه‌گیری می‌شود.",
        applications="تحلیل انتقادی رسانه (بازنمایی جنسیت، قومیت، نژاد)، تحلیل گفتمان رسانه‌ای (نماد، معنا، ایدئولوژی)، آموزش سواد رسانه‌ای (شناخت کدگذاری، دیگری‌سازی، بازنمایی)، طراحی محتوا (بازنمایی مسئولانه، تنوع‌گرایی)، و پژوهش در هویت و معناسازی (اثر بازنمایی بر خود و دیگری) (Hall, 1997; Littlejohn & Foss, 2011).",
        evolution="مفهوم بازنمایی از نمادشناسی (Saussure) و ساختارگرایی وارد علوم ارتباط شد؛ با Stuart Hall (۱۹۷۰–۱۹۹۷) به «میدان بازنمایی فرهنگی» تبدیل شد؛ در عصر رسانه‌های دیجیتال، بازنمایی به «بازنمایی مشارکتی و چندصدا» گسترش یافته است (Hall, 1997).",
        assumptions="فرض‌های نهفته: بازنمایی، واقع را «می‌سازد» نه صرفا‌ً بازتاب می‌دهد؛ معنا از طریق نماد و زبان ساخته می‌شود؛ و بازنمایی‌ها بازتابِ روابط قدرت و ایدئولوژی‌اند و می‌توانند مقاومت ایجاد کنند (Hall, 1997; Littlejohn & Foss, 2011).",
    ),
    "CPT-148": dict(
        summary="جهانی‌شدن فرهنگی (cultural globalization) به فرایند گسترش و تعامل الگوهای فرهنگی، رسانه‌ای و نمادین فراتر از مرزهای ملی، و بازآرایی فرهنگ‌ها در مقیاس جهانی می‌گوید؛ در آن فرهنگ، کالا، گفتمان و رسانه‌ها در یک شبکهٔ جهانی جریان می‌یابند (Castells, 2009; Habermas, 1991). ویژگی‌ها: (۱) جریان‌سازی رسانه‌ای: رسانه‌های جهانی، فرهنگ‌های محلی را به هم می‌رسانند؛ (۲) استانداردسازی: الگوهای فرهنگی (موسیقی، فیلم، برند) جهانی می‌شوند؛ (۳) ناهمگنی: جهانی‌شدن، همگنی مطلق نیست و مقاومت‌های محلی نیز دارد؛ (۴) بازترسیم حوزه عمومی: حوزه عمومی، از ملی به جهانی کشیده می‌شود (Habermas, 1991). پژوهش‌ها نشان می‌دهند جهانی‌شدن فرهنگی بر «هویت»، «تنوع فرهنگی» و «قدرت رسانه‌ای» اثر عمیق دارد (Castells, 2009). نقد بنیادین، «استانداردسازی‌زدگی» است: فرض بر آن است که جهانی‌شدن، «همگنی» است، در حالی که اغلب «بازآرایی» و «ترکیب» است (Habermas, 1991).",
        mechanism="جهانی‌شدن فرهنگی در چهار حلقه عمل می‌کند: (۱) تولید جهانی: رسانه‌ها و کالاهای فرهنگی، در مقیاس جهانی تولید می‌شوند؛ (۲) جریان‌سازی: الگوهای فرهنگی از طریق رسانه‌های جمعی و شبکه‌ها به‌سراسر جهان گسترش می‌یابند؛ (۳) تعامل و بازآرایی: فرهنگ‌های محلی، الگوهای جهانی را می‌پذیرند، مقاومت می‌کنند و بازآرایی می‌کنند؛ (۴) بازترسیم هویت و حوزه عمومی: هویت‌ها و حوزه‌های عمومی، در مقیاس جهانی بازترسیم می‌شوند (Castells, 2009; Habermas, 1991).",
        key_concepts=["جریان‌سازی رسانه‌ای", "استانداردسازی فرهنگی", "ناهمگنی", "بازآرایی فرهنگی", "حوزه عمومی جهانی"],
        critiques="الگوی استانداردسازی، جهانی‌شدن را «همگنی مطلق» نشان می‌دهد، در حالی که اغلب «بازآرایی» و «ترکیب» است (Castells, 2009). نقد دیگر «آمریکایی‌زدگی» است: فرض بر آن است که جهانی‌شدن، «تک‌جهت» (از مرکز به پیرامون) است، در حالی که جریان‌ها «چندجهت»‌اند (Habermas, 1991). همچنین «اقتصادی‌زدگی» فرهنگی، بر فرهنگ ساییده می‌شود.",
        applications="تحلیل انتقادی جهانی‌شدن فرهنگی (جریان رسانه، هویت، تنوع)، سیاست‌گذاری فرهنگی (محافظت از تنوع، حمایت از رسانه‌های محلی)، آموزش سواد رسانه‌ای (شناخت جریان جهانی، مقاومت، بازآرایی)، طراحی استراتژی رسانه‌ای بین‌المللی (بومی‌سازی، گلوبال)، و پژوهش در هویت و حوزه عمومی جهانی (اثر جهانی‌شدن بر هویت) (Castells, 2009; Habermas, 1991).",
        evolution="مفهوم جهانی‌شدن فرهنگی از دههٔ ۱۹۷۰ (رشد رسانه‌های بین‌المللی) وارد علوم ارتباط شد؛ در دهه‌های ۱۹۹۰–۲۰۰۰ با شبکه‌سازی دیجیتال، به «میدان مستقل» تبدیل شد؛ در عصر پلتفرم‌های جهانی، به «جهانی‌شدن شبکه‌ای و تعاملی» گسترش یافت (Castells, 2009).",
        assumptions="فرض‌های نهفته: فرهنگ، از طریق رسانه‌ها و شبکه‌ها در مقیاس جهانی جریان می‌یابد؛ جهانی‌شدن، بازآرایی است نه همگنی مطلق؛ و الگوهای فرهنگی، هویت‌ها و حوزه‌های عمومی را در مقیاس جهانی بازترسیم می‌کنند (Castells, 2009; Habermas, 1991).",
    ),
    "CPT-149": dict(
        summary="محلی‌شدن فرهنگی (cultural localization) و «گلوبالایزیشن» به فرایند می‌گوید که الگوهای فرهنگی و رسانه‌ای جهانی، در مواجهه با بافت محلی، بومی‌سازی، بازخوانی و بازآرایی می‌شوند و الگوهای محلی دوباره در مقیاس گسترده‌تر معنا می‌یابند (Giddens, 1991; McQuail, 2010). ویژگی‌ها: (۱) بومی‌سازی (adaptation): محتوا و الگوهای جهانی، به بافت محلی سازگار می‌شوند؛ (۲) بازخوانی محلی: مخاطبان، الگوهای جهانی را به شیوهٔ محلی تفسیر می‌کنند؛ (۳) بازگشت به محلی: هویت‌های محلی در برابر جهانی‌شدن تقویت می‌شوند؛ (۴) ترکیب (hybridity): ترکیب الگوهای جهانی و محلی، فرهنگ‌های ترکیبی می‌سازد (Giddens, 1991). پژوهش‌ها نشان می‌دهند محلی‌شدن فرهنگی بر «هویت محلی»، «مقاومت فرهنگی» و «تنوع» اثر عمیق دارد (McQuail, 2010). نقد بنیادین، «محلی‌زدگی» است: فرض بر آن است که محلی‌شدن، «مقاومت خالص» است، در حالی که اغلب «تعامل» و «ترکیب» است (Giddens, 1991).",
        mechanism="محلی‌شدن فرهنگی در چهار حلقه عمل می‌کند: (۱) ورود الگوهای جهانی: الگوهای فرهنگی و رسانه‌ای جهانی، وارد بافت محلی می‌شوند؛ (۲) بومی‌سازی: محتوا و الگوها، به بافت، زبان و ارزش‌های محلی سازگار می‌شوند؛ (۳) بازخوانی محلی: مخاطبان، الگوهای جهانی را به شیوهٔ محلی تفسیر و بازآرایی می‌کنند؛ (۴) بازآرایی و تقویت هویت: الگوهای محلی تقویت و ترکیب می‌شوند و هویت محلی بازترسیم می‌شود (Giddens, 1991; McQuail, 2010).",
        key_concepts=["بومی‌سازی (adaptation)", "بازخوانی محلی", "بازگشت به محلی", "ترکیب فرهنگی (hybridity)", "هویت محلی"],
        critiques="الگوی محلی‌زدگی، محلی‌شدن را «مقاومت خالص» نشان می‌دهد، در حالی که اغلب «تعامل» و «ترکیب» است (Giddens, 1991). نقد دیگر «رومانتیسیسم محلی» است: فرض بر آن است که محلی، «خالص» است، در حالی که فرهنگ‌ها همیشه «متحرک» و ترکیبی‌اند (McQuail, 2010). همچنین «اثر اقتصادی» بومی‌سازی، به‌سختی اندازه‌گیری می‌شود.",
        applications="طراحی استراتژی‌های رسانه‌ای بومی (بومی‌سازی محتوا، زبان، ارزش‌ها)، تحلیل انتقادی گلوبالایزیشن (ترکیب، مقاومت، هویت محلی)، آموزش سواد رسانه‌ای (شناخت بومی‌سازی، بازخوانی، ترکیب)، طراحی تجربهٔ فرهنگی (تعامل جهانی-محلی)، و پژوهش در هویت و تنوع فرهنگی (اثر محلی‌شدن بر هویت محلی) (Giddens, 1991; McQuail, 2010).",
        evolution="مفهوم محلی‌شدن فرهنگی از دههٔ ۱۹۹۰ (رویکرد glocalization) وارد علوم ارتباط شد؛ در دهه‌های ۲۰۰۰–۲۰۱۰ با گسترش رسانه‌های محلی دیجیتال، به «میدان مستقل» تبدیل شد؛ در عصر پلتفرم‌های جهانی، به «محلی‌شدن مشارکتی و ترکیبی» گسترش یافت (McQuail, 2010).",
        assumptions="فرض‌های نهفته: الگوهای فرهنگی جهانی، در بافت محلی بازآرایی می‌شوند (نه پذیرش خالص)؛ مخاطبان، الگوها را به شیوهٔ محلی تفسیر می‌کنند؛ و محلی‌شدن، هویت محلی و تنوع فرهنگی را تقویت می‌کند (Giddens, 1991; McQuail, 2010).",
    ),
    "CPT-150": dict(
        summary="جامعه اطلاعاتی (information society) به ساختار اجتماعی می‌گوید که در آن اطلاعات، دانش و فناوری‌های دیجیتال، منبع اصلی تولید، قدرت و مشارکت اجتماعی‌اند و اقتصاد و فرهنگ، بر محور جریان اطلاعات سازمان‌دهی می‌شوند (Castells, 2009; Giddens, 1991). ویژگی‌ها: (۱) محوریت اطلاعات: اطلاعات، «منبع» اصلی ارزش‌آفرینی است (در مقابل سرمایه و کار)؛ (۲) دیجیتال‌سازی: تولید، توزیع و مصرف، بر پایه فناوری دیجیتال است؛ (۳) شبکه‌ای بودن: تعاملات، در شبکه‌ها جریان می‌یابند؛ (۴) شکاف دیجیتال: دسترسی نابرابر به اطلاعات، نابرابری‌های جدید می‌سازد (Giddens, 1991). پژوهش‌ها نشان می‌دهند جامعه اطلاعاتی بر «اقتصاد»، «حاکمیت» و «هویت» اثر عمیق دارد (Castells, 2009). نقد بنیادین، «فناوری‌زدگی» است: فرض بر آن است که فناوری، به‌خودی‌خود پیشرفت است، در حالی که اغلب نابرابری بازتولید می‌کند (Giddens, 1991).",
        mechanism="جامعه اطلاعاتی در چهار حلقه عمل می‌کند: (۱) تولید دانش: اطلاعات و دانش، در مقیاس بزرگ تولید می‌شوند (دیجیتال)؛ (۲) جریان‌سازی: اطلاعات، از طریق شبکه‌ها و رسانه‌های دیجیتال جریان می‌یابند؛ (۳) سازمان‌دهی: اقتصاد، سیاست و فرهنگ، بر محور اطلاعات سازمان‌دهی می‌شوند؛ (۴) بازآرایی اجتماعی: ساختار قدرت، شغل و هویت، بر پایه دسترسی به اطلاعات بازآرایی می‌شوند (Castells, 2009; Giddens, 1991).",
        key_concepts=["محوریت اطلاعات", "دیجیتال‌سازی", "شبکه‌ای بودن", "شکاف دیجیتال", "دانش‌بنیان"],
        critiques="الگوی فناوری‌زدگی، جامعه اطلاعاتی را «پیشرفت خالص» نشان می‌دهد، در حالی که اغلب نابرابری بازتولید می‌کند (Castells, 2009). نقد دیگر «شکاف دیجیتال» است: فرض بر آن است که دسترسی، «برابر» است، در حالی که دسترسی نابرابر، نابرابری‌های جدید می‌سازد (Giddens, 1991). همچنین «اثر قدرت» فناوری، به‌سختی اندازه‌گیری می‌شود.",
        applications="تحلیل انتقادی جامعه اطلاعاتی (اقتصاد، حاکمیت، شکاف دیجیتال)، سیاست‌گذاری دیجیتال (دسترسی، سواد دیجیتال، حاکمیت داده‌ها)، آموزش سواد دیجیتال و رسانه‌ای، طراحی استراتژی‌های هوشمند (داده، دانش، شبکه)، و پژوهش در شغل و هویت در عصر دیجیتال (اثر اطلاعات بر ساختار اجتماعی) (Castells, 2009; Giddens, 1991).",
        evolution="مفهوم جامعه اطلاعاتی از دههٔ ۱۹۷۰ (Bell, Toffler) وارد علوم ارتباط شد؛ در دهه‌های ۱۹۹۰–۲۰۰۰ با گسترش اینترنت، به «میدان مستقل» تبدیل شد؛ در عصر داده‌های بزرگ و هوش مصنوعی، به «جامعه اطلاعاتی داده‌محور» گسترش یافت (Castells, 2009).",
        assumptions="فرض‌های نهفته: اطلاعات، منبع اصلی ارزش‌آفرینی و قدرت است (نه صرفا‌ً سرمایه)؛ تعاملات اجتماعی، در شبکه‌های دیجیتال جریان می‌یابند؛ و دسترسی نابرابر به اطلاعات، ساختار اجتماعی را بازآرایی می‌کند (Castells, 2009; Giddens, 1991).",
    ),
}


def main():
    spec = importlib.util.spec_from_file_location("fw", "scripts/kb_batch238_framework.py")
    fw = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(fw)
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

    snap = [{"id": r[0], "code": r[1], "properties": json.loads(r[2])} for r in rows]
    with open(BACKUP, "w", encoding="utf-8") as f:
        json.dump(snap, f, ensure_ascii=False, indent=1)
    print("backup ->", len(snap), "rows")

    for code in codes:
        eid, _c, props = found[code]
        p = json.loads(props)
        en = ENRICH[code]
        for k, v in en.items():
            p[k] = v
        if not p.get("sources"):
            p["sources"] = []
        if not p.get("citations"):
            p["citations"] = []
        for src in S[code]:
            if not any(x.get("citation") == src["citation"] for x in p["sources"]):
                p["sources"].append({
                    "citation": src["citation"], "title_en": src["title_en"],
                    "title_fa": src["title_fa"], "year": src["year"], "doi": src.get("doi"),
                    "url": src.get("url"), "language": src["language"], "verified": src["verified"],
                })
            if not any(x.get("source") == src["citation"] for x in p["citations"]):
                p["citations"].append({
                    "source": src["citation"], "locator": src["locator"],
                    "supports": src["supports"], "verified": src["verified"],
                })
        cur.execute("SELECT COUNT(*) FROM kb_relations WHERE source_id=%s OR target_id=%s", (eid, eid))
        n_rel = cur.fetchone()[0]
        n_sources = len(p["sources"])
        n_verified = sum(1 for x in p["citations"] if x.get("verified"))
        score, detail, words = fw.rubric(p, n_verified, n_sources, n_rel)
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
            sid = fw.ensure_source(cur, src)
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
                     "add 6 missing concept fields (SPEC §4.3) + verified sources", STAMP, NOW))
        cur.execute("""INSERT INTO kb_audit_log (entity_code,action,detail,source,created_at)
            VALUES (%s,'DOC_ENRICH',%s,%s,%s)""",
                    (code, json.dumps({"batch": 323, "score": score, "words": words,
                                       "sources": n_sources, "verified": n_verified,
                                       "relations": n_rel, "rubric": detail}, ensure_ascii=False), STAMP, NOW))
        print(code, "words", words, "score", score, "detail", detail)
    conn.commit()
    conn.close()
    print("BATCH323 DONE")


if __name__ == "__main__":
    main()
