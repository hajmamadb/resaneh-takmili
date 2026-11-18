# -*- coding: utf-8 -*-
"""Batch 65 (THEORY): MC-338 Simulacra and Hyperreality (Baudrillard 1981),
MC-340 Dromology (Virilio 1977), MC-341 Postmodern Condition (Lyotard 1979),
MC-342 Dramaturgy (Goffman 1959). Anchors verified 2026-11-16.
Rewrites the mismatched boilerplate critique/example found on all four records."""
import pymysql, json

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch65-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch65_theory.json"

S = {
 "MC-338": [
   dict(kind="BOOK", title_en="Simulacra and Simulation",
        title_fa="وانموده‌ها و شبیه‌سازی",
        authors="Baudrillard, J.", year=1981, publisher="Paris: Éditions Galilée (English ed. 1994, University of Michigan Press)",
        doi=None, url="https://en.wikipedia.org/wiki/Simulacra_and_Simulation",
        language="fr", isbn=None,
        citation="Baudrillard, J. (1981). Simulacres et simulation. Éditions Galilée. [English: Simulacra and simulation, University of Michigan Press, 1994]",
        locator="whole work", locator_type="work", supports="definition / orders of simulacra / hyperreality", verified=True),
   dict(kind="BOOK", title_en="The Gulf War Did Not Take Place",
        title_fa="جنگ خلیج فارس رخ نداد",
        authors="Baudrillard, J.", year=1991, publisher="Paris: Éditions Galilée (English ed. 1995, Indiana University Press)",
        doi=None, url=None, language="fr", isbn=None,
        citation="Baudrillard, J. (1991). La guerre du Golfe n'a pas eu lieu. Éditions Galilée.",
        locator="whole work", locator_type="work", supports="application / war as media event", verified=False),
 ],
 "MC-340": [
   dict(kind="BOOK", title_en="Speed and Politics: An Essay on Dromology",
        title_fa="سرعت و سیاست: جستاری در درومولوژی",
        authors="Virilio, P.", year=1977, publisher="Paris: Éditions Galilée (English ed. 1986, Semiotext(e))",
        doi=None, url="https://monoskop.org/File:VIRILIO_Paul_-_1977_-_Vitesse_et_politique.pdf",
        language="fr", isbn=None,
        citation="Virilio, P. (1977). Vitesse et politique: Essai de dromologie. Éditions Galilée.",
        locator="whole work", locator_type="work", supports="definition / dromology / speed as power", verified=True),
   dict(kind="BOOK", title_en="The Aesthetics of Disappearance",
        title_fa="زیبایی‌شناسی ناپدیدشدن",
        authors="Virilio, P.", year=1980, publisher="Paris: Éditions Balland (English ed. 1991, Semiotext(e))",
        doi=None, url=None, language="fr", isbn=None,
        citation="Virilio, P. (1980). Esthétique de la disparition. Éditions Balland.",
        locator="whole work", locator_type="work", supports="evolution / picnolepsy and perception", verified=False),
 ],
 "MC-341": [
   dict(kind="BOOK", title_en="The Postmodern Condition: A Report on Knowledge",
        title_fa="وضعیت پست‌مدرن: گزارشی دربارهٔ دانش",
        authors="Lyotard, J.-F.", year=1979, publisher="Paris: Les Éditions de Minuit (English ed. 1984, University of Minnesota Press)",
        doi=None, url="https://www.leseditionsdeminuit.fr/livre-La_Condition_postmoderne-2180-1-1-0-1.html",
        language="fr", isbn=None,
        citation="Lyotard, J.-F. (1979). La condition postmoderne: Rapport sur le savoir. Les Éditions de Minuit.",
        locator="whole work", locator_type="work", supports="definition / incredulity toward metanarratives / performativity", verified=True),
   dict(kind="BOOK", title_en="The Differend: Phrases in Dispute",
        title_fa="اختلاف: گفتارها در نزاع",
        authors="Lyotard, J.-F.", year=1983, publisher="Paris: Les Éditions de Minuit (English ed. 1988, University of Minnesota Press)",
        doi=None, url=None, language="fr", isbn=None,
        citation="Lyotard, J.-F. (1983). Le différend. Les Éditions de Minuit.",
        locator="whole work", locator_type="work", supports="evolution / language games and justice", verified=False),
 ],
 "MC-342": [
   dict(kind="BOOK", title_en="The Presentation of Self in Everyday Life",
        title_fa="نمایش خود در زندگی روزمره",
        authors="Goffman, E.", year=1959, publisher="New York: Anchor Books / Doubleday", doi=None,
        url="https://monoskop.org/images/1/19/Goffman_Erving_The_Presentation_of_Self_in_Everyday_Life.pdf",
        language="en", isbn=None,
        citation="Goffman, E. (1959). The presentation of self in everyday life. Anchor Books.",
        locator="whole work", locator_type="work", supports="definition / front stage and backstage / impression management", verified=True),
   dict(kind="BOOK", title_en="Interaction Ritual: Essays on Face-to-Face Behavior",
        title_fa="آیین تعامل: جستارهایی در رفتار رودررو",
        authors="Goffman, E.", year=1967, publisher="New York: Pantheon Books", doi=None, url=None,
        language="en", isbn=None,
        citation="Goffman, E. (1967). Interaction ritual: Essays on face-to-face behavior. Pantheon Books.",
        locator="whole work", locator_type="work", supports="evolution / face-work and interaction order", verified=False),
 ],
}

ENRICH = {
 "MC-338": {
   "summary": "«وانموده و حادواقعیت» (Simulacra and Hyperreality) تحلیل ژان بودریار از وضعیتی است که در آن نشانه‌ها از واقعیت جدا شده‌اند و نسخه‌ای از واقعیت می‌سازند که از خود واقعیت واقعی‌تر به نظر می‌رسد. بودریار این تحلیل را در «Simulacres et simulation» (۱۹۸۱، Éditions Galilée) صورت‌بندی کرد (Baudrillard, 1981).",
   "definition": "وانموده، نسخه‌ای است که دیگر به واقعیت بیرونی ارجاع نمی‌دهد و به‌جای آن، واقعیت را جایگزین می‌کند؛ حادواقعیت، حالتی است که در آن مرز میان بازنمایی و واقعیت فرومی‌ریزد و تجربهٔ رسانه‌ای، معیار واقعی‌بودن می‌شود (Baudrillard, 1981).",
   "main_problem": "وقتی رسانه‌ها چنان فراگیر می‌شوند که تجربهٔ ما از جهان عمدتاً از طریق بازنمایی‌ها ساخته می‌شود، چه معیاری برای تشخیص واقعیت باقی می‌ماند؛ و سیاست و اخلاق بر چه پایه‌ای استوار می‌شوند؟",
   "mechanism": "تحلیل بودریار بر پنج سازوکار استوار است. (۱) استقلال نشانه: نشانه از شیء جدا می‌شود و ارزش خود را از نظام تفاوت نشانه‌ها می‌گیرد، نه از ارجاع به واقعیت. (۲) مراحل چهارگانهٔ تصویر: تصویر نخست بازتاب واقعیت است، سپس واقعیت را پنهان می‌کند، سپس نبودِ واقعیت را پنهان می‌کند و در نهایت، وانمودهٔ بی‌ارجاع می‌شود؛ در مرحلهٔ چهارم، پرسش از «اصل» بی‌معناست. (۳) فروپاشی معنا: مرز میان رسانه و واقعیت، سیاست و سرگرمی، خبر و نمایش فرومی‌ریزد و هر رویداد به «محتوای» قابل پخش بدل می‌شود. (۴) حادواقعیت: دیزنی‌لند نمونهٔ کلاسیک است؛ پارک، واقعیتی ساختگی می‌سازد که به ما اطمینان می‌دهد «بیرون» واقعی است، در حالی که بیرون نیز به همان منطق بازنمایی آلوده است. (۵) وانمودهٔ سیاسی: بودریار در «جنگ خلیج فارس رخ نداد» (۱۹۹۱) استدلال کرد که جنگ، بیش از رویدادی میدانی، رویدادی تلویزیونی بود که پیش از وقوع، در رسانه ساخته شد. در بستر رسانه، این چارچوب برای تحلیل واقعیت مجازی، تصویرسازی دیپلماسی، خبر جعلی و «واقعیت» شبکه‌های اجتماعی به‌کار می‌رود: هر جا مخاطب، تجربهٔ رسانه‌ای را به‌جای تجربهٔ مستقیم معیار می‌گیرد، حادواقعیت در کار است.",
   "assumptions": [
     "نشانه‌ها می‌توانند از ارجاع به واقعیت مستقل شوند.",
     "رسانه‌ها نه واسطه، بلکه سازندهٔ تجربهٔ واقعیت‌اند.",
     "در حادواقعیت، پرسش از «اصل» و «حقیقت» کارکرد خود را از دست می‌دهد."
   ],
   "principles": [
     "بازنمایی می‌تواند جای واقعیت را بگیرد.",
     "نشانه، ارزش خود را از نظام نشانه‌ها می‌گیرد، نه از شیء.",
     "حادواقعیت، معیارهای واقعی‌بودن را دگرگون می‌کند."
   ],
   "critiques": [
     "آزمون‌ناپذیری و سبک افراطی: گزاره‌ها بیشتر ادبی و بلاغی‌اند تا تجربی؛ ادعاهایی مانند «جنگ خلیج فارس رخ نداد» به‌راحتی بدفهمیده و به انکار واقعیت کشته‌شدگان بدل می‌شود.",
     "نیهیلیسم سیاسی: اگر همه‌چیز وانموده باشد، معیاری برای نقد و مقاومت باقی نمی‌ماند و نظریه به بی‌تفاوتی یا بدبینی منجر می‌شود.",
     "غفلت از نابرابری مادی: تحلیل نشانه‌ای، دسترسی نابرابر به تولید و مصرف نشانه‌ها و منافع اقتصادی پلتفرم‌ها را کم‌رنگ می‌کند."
   ],
   "applications": [
     "تحلیل خبر جعلی و سیاست پس‌حقیقت.",
     "پژوهش دربارهٔ تصویرسازی دیپلماسی و جنگ رسانه‌ای.",
     "نقد واقعیت مجازی و تجربهٔ رسانه‌ای در شبکه‌های اجتماعی.",
     "تحلیل گردشگری، موزه و بازسازی تاریخی به‌عنوان تولید وانموده."
   ],
   "evolution": "بودریار اندیشه را از «جامعهٔ مصرف» (۱۹۷۰) آغاز کرد و در ۱۹۸۱ به صورت‌بندی وانموده رساند؛ پس از ۱۹۹۱ و بحث جنگ خلیج فارس، مفهوم به تحلیل رسانهٔ جنگی و سپس به نقد اینترنت و واقعیت مجازی راه یافت.",
   "key_concepts": ["وانموده (simulacrum)", "حادواقعیت (hyperreality)", "فروپاشی معنا (implosion of meaning)", "ارزش نشانه‌ای (sign value)", "مراحل تصویر (orders of simulacra)", "ارجاع (referentiality)"],
   "studies": ["Baudrillard, J. (1981). Simulacres et simulation. Éditions Galilée.", "Baudrillard, J. (1991). La guerre du Golfe n'a pas eu lieu. Éditions Galilée."],
   "detailed_analysis": "۱. بنیان و منطق نظری\nبودریار از نقد اقتصاد سیاسی نشانه آغاز کرد: در جامعهٔ مصرف، ما اشیا را نه برای کاربرد، بلکه برای معنای نشانه‌ای‌شان می‌خریم. اگر ارزش از نظام نشانه‌ها بیاید، پس واقعیت بیرونی می‌تواند از معادله حذف شود؛ همین گام، به وانموده می‌رسد.\n\n۲. حادواقعیت چگونه کار می‌کند\nحادواقعیت ادعا نمی‌کند که واقعیتی وجود ندارد؛ می‌گوید معیار واقعی‌بودن تغییر کرده است. وقتی تصویر رویداد، بیش از خود رویداد دیده می‌شود، سیاست بر پایهٔ تصویر ساخته می‌شود، نه بر پایهٔ رویداد.\n\n۳. پیوند رسانه‌ای و نقد\nدر عصر پلتفرم، نقد بودریار تیزتر شده است: بازنمایی، دیگر نه بازتاب واقعیت، بلکه تولید آن است. اما نقد نیهیلیسم جدی است: اگر همه‌چیز وانموده باشد، مسئولیت چه می‌شود؟ پاسخ قابل دفاع این است که وانموده، نیازمند تحلیل سیاسی و اقتصادی است، نه انکار واقعیت.",
   "critique_text": "\n".join([
     "۱. آزمون‌ناپذیری و بلاغت: گزاره‌ها ادبی و کلی‌اند؛ ادعای «جنگ خلیج فارس رخ نداد» به‌راحتی بدفهمیده می‌شود و می‌تواند به انکار رنج واقعی بینجامد.",
     "۲. نیهیلیسم سیاسی: اگر همه‌چیز وانموده باشد، معیاری برای نقد و مقاومت باقی نمی‌ماند و نظریه به بی‌تفاوتی می‌رسد.",
     "۳. غفلت مادی: تحلیل نشانه‌ای، نابرابری دسترسی، منافع اقتصادی پلتفرم و ساختار مالکیت را کم‌رنگ می‌کند."]),
   "example_text": "دیزنی‌لند با ساختن واقعیتی آشکارا ساختگی، به بازدیدکننده اطمینان می‌دهد که «بیرون» واقعی است؛ اما همان بیرون نیز با منطق بازنمایی، تبلیغات و تصویر رسانه‌ای سازمان یافته است. همین دور، نمونهٔ روشن حادواقعیت است.",
 },
 "MC-340": {
   "summary": "«درومولوژی» (Dromology) علم سرعت است که پل ویریلیو آن را بنیان گذاشت: تاریخ سیاسی، تاریخ رقابت بر سر سرعت است و هر قدرت، پیش از هر چیز، قدرت تسلط بر سرعت است. ویریلیو این دیدگاه را در «Vitesse et politique» (۱۹۷۷، Éditions Galilée) صورت‌بندی کرد (Virilio, 1977).",
   "definition": "درومولوژی مطالعهٔ منطق سرعت در سازمان اجتماعی است: سرعت انتقال، جابه‌جایی و اطلاعات، ساختار قدرت، شهر، جنگ و ادراک را تعیین می‌کند، نه فقط کارآمدی را (Virilio, 1977).",
   "main_problem": "اگر قدرت سیاسی را نه با مالکیت زمین یا سرمایه، بلکه با تسلط بر سرعت تعریف کنیم، چه چیزی در فهم ما از دولت، جنگ، شهر و رسانه تغییر می‌کند؟",
   "mechanism": "تحلیل ویریلیو بر پنج سازوکار استوار است. (۱) سرعت به‌عنوان قدرت: هر کس سریع‌تر جابه‌جا شود یا اطلاعات را سریع‌تر منتقل کند، بر قلمرو تسلط دارد؛ جاده، راه‌آهن و کابل، ابزارهای سیاسی‌اند. (۲) دروموکراسی: ویریلیو جامعه را نه فقط بر پایهٔ طبقه، بلکه بر پایهٔ دسترسی به سرعت تقسیم می‌کند؛ کسانی که در «مسیر سریع» هستند و کسانی که در حاشیهٔ آن گیر افتاده‌اند. (۳) لجستیک و جنگ: جنگ مدرن، جنگ لجستیک و انتقال است، نه فقط نبرد میدانی؛ برتری، از آنِ طرفی است که سریع‌تر تأمین و مستقر می‌شود. (۴) بلادرنگ و فروپاشی فاصله: رسانهٔ الکترونیک، فاصله را به تأخیر فرومی‌کاهد؛ وقتی انتقال آنی شد، جغرافیا به‌عنوان مانع از میان می‌رود و «زمان واقعی» جای مکان را می‌گیرد. (۵) حادثهٔ جهانی: ویریلیو هشدار می‌داد که سرعت و به‌هم‌پیوستگی، «حادثهٔ جهانی» — بحران یا فروپاشی هم‌زمان در مقیاس سیاره‌ای — را ممکن می‌کند. در بستر رسانه، این چارچوب برای تحلیل خبر بیست‌وچهارساعته، پخش زنده و بازار مالی الگوریتمی به‌کار می‌رود: هر جا سرعت به ارزش اصلی بدل شود، تأمل، بررسی و پاسخ‌گویی قربانی می‌شوند و خبر به مسابقهٔ رسیدن اول فرومی‌کاهد.",
   "assumptions": [
     "سرعت، متغیر بنیادی سازمان اجتماعی و سیاسی است.",
     "تسلط بر فناوری‌های انتقال، تسلط بر قلمرو و افکار می‌آورد.",
     "فناوری رسانه‌ای، ادراک زمان و فضا را دگرگون می‌کند."
   ],
   "principles": [
     "قدرت، تسلط بر سرعت است.",
     "لجستیک، تعیین‌کنندهٔ نتیجهٔ جنگ است.",
     "سرعت بلادرنگ، فاصله و تأمل را از میان برمی‌دارد."
   ],
   "critiques": [
     "جبر فناورانه و بدبینی: تحلیل، سرعت را عاملی مستقل و غالب می‌بیند و ظرفیت مقاومت، سیاست‌گذاری و انتخاب انسانی را کم‌رنگ می‌کند.",
     "سبک قصیده‌وار: نوشتار ویریلیو بیشتر بیانیه‌ای و استعاری است تا استدلال نظام‌مند و آزمون‌پذیر؛ سنجش تجربی ادعاها دشوار است.",
     "غفلت از اقتصاد و نابرابری ساختاری: تمرکز بر سرعت، تفاوت منافع سرمایه و کار و نابرابری دسترسی را به حاشیه می‌راند."
   ],
   "applications": [
     "تحلیل خبر فوری و رقابت سرعت در اتاق خبر.",
     "پژوهش دربارهٔ پخش زنده و ادراک زمان.",
     "نقد تجارت الگوریتمی و بازار مالی پرسرعت.",
     "مطالعهٔ لجستیک رسانه‌ای و توزیع محتوا."
   ],
   "evolution": "ویریلیو اندیشه را از نقد معماری و شهر آغاز کرد و در ۱۹۷۷ به درومولوژی رساند؛ در «زیبایی‌شناسی ناپدیدشدن» (۱۹۸۰) به ادراک و در نوشته‌های بعدی به «حادثهٔ جهانی» و فناوری اطلاعات پرداخت.",
   "key_concepts": ["درومولوژی (dromology)", "دروموکراسی (dromocracy)", "لجستیک (logistics)", "بلادرنگ (real time)", "حادثهٔ جهانی (global accident)", "فروپاشی فاصله"],
   "studies": ["Virilio, P. (1977). Vitesse et politique. Éditions Galilée.", "Virilio, P. (1980). Esthétique de la disparition. Éditions Balland."],
   "detailed_analysis": "۱. بنیان و منطق نظری\nویریلیو از شهر و معماری آغاز کرد و به این نتیجه رسید که سازمان شهر، سازمان سرعت است: دیوار، دروازه و جاده، همه ابزار مدیریت حرکت‌اند. از این‌جا، پرسش سیاسی او شکل گرفت: چه کسی بر سرعت حکومت می‌کند؟\n\n۲. سرعت و دموکراسی\nدر تحلیل او، دموکراسی به زمان نیاز دارد: زمان بحث، بررسی و تصمیم. سرعت بلادرنگ، این زمان را حذف می‌کند و تصمیم را به واکنش فرومی‌کاهد؛ ازاین‌رو، «دروما-دموکراسی» تنشی درونی دارد.\n\n۳. پیوند رسانه‌ای و نقد\nدر اتاق خبر امروز، سرعت انتشار به ارزش اصلی بدل شده است. نقد ویریلیو این پیامد را روشن می‌کند، اما خود او کمتر راه‌حلی ارائه می‌دهد؛ نقد جدی این است که تحلیل باید با سیاست‌گذاری و بررسی تجربی تکمیل شود.",
   "critique_text": "\n".join([
     "۱. جبر فناورانه: سرعت به عاملی مستقل بدل می‌شود و ظرفیت مقاومت، تنظیم‌گری و انتخاب انسانی کم‌رنگ می‌شود.",
     "۲. سبک قصیده‌وار: استدلال‌ها استعاری و اعلامی‌اند، نه نظام‌مند و آزمون‌پذیر؛ سنجش تجربی ادعاها دشوار است.",
     "۳. غفلت از اقتصاد: تمرکز بر سرعت، نابرابری دسترسی و تضاد منافع سرمایه و کار را به حاشیه می‌راند."]),
   "example_text": "در یک بحران، خبرگزاری که چند دقیقه زودتر منتشر می‌کند، دستور کار رسانه‌ای را می‌سازد؛ حتی اگر بعداً ناچار به اصلاح شود، اثر اولیه باقی می‌ماند. همین مسابقه، دقیقاً همان چیزی است که ویریلیو آن را سلطهٔ سرعت بر دقت می‌نامد.",
 },
 "MC-341": {
   "summary": "«وضعیت پست‌مدرن» (The Postmodern Condition) تحلیل ژان-فرانسوا لیوتار از وضعیت دانش در جوامع پیشرفته است: اعتماد به «کلان‌روایت‌ها» — روایت‌های بزرگ رهایی، عقل و پیشرفت — فروپاشیده و دانش به بازی‌های زبانی متکثر و کالایی بدل شده است. لیوتار این تحلیل را در «La condition postmoderne» (۱۹۷۹، Les Éditions de Minuit) ارائه کرد (Lyotard, 1979).",
   "definition": "پست‌مدرنیسم در معنای لیوتار، بی‌اعتمادی به کلان‌روایت‌هاست؛ وضعیتی که در آن مشروعیت دانش دیگر از روایت‌های بزرگ نمی‌آید، بلکه از کارآمدی، عملکرد و توافق‌های محلی و موقت (Lyotard, 1979).",
   "main_problem": "اگر روایت‌های بزرگ که مشروعیت دانش و سیاست را تضمین می‌کردند فرو ریخته باشند، دانش بر چه پایه‌ای مشروع می‌شود و عدالت اجتماعی چگونه ممکن است؟",
   "mechanism": "تحلیل لیوتار بر پنج سازوکار استوار است. (۱) زوال کلان‌روایت: روایت رهایی انسان و روایت پیشرفت عقل، دیگر اقناع نمی‌کنند؛ هر دو، وعده‌هایی دادند که تجربهٔ قرن بیستم آن‌ها را نقض کرد. (۲) بازی‌های زبانی: دانش، مجموعه‌ای از بازی‌های زبانی با قواعد متفاوت است و هیچ فراگفتاری نمی‌تواند همهٔ آن‌ها را داوری کند. (۳) عملکرد به‌جای حقیقت: در جامعهٔ رایانه‌ای، معیار مشروعیت دانش به «کارآمدی» و «قابلیت بهینه‌سازی سیستم» منتقل می‌شود؛ دانشی که کارآمدتر باشد، مشروع‌تر است. (۴) کالایی‌شدن دانش: اطلاعات به کالا بدل می‌شود و دسترسی به آن، منبع نابرابری تازه‌ای می‌شود؛ لیوتار این را پیش از فراگیری اینترنت صورتبندی کرد. (۵) خردروایت‌ها: در غیاب روایت بزرگ، روایت‌های کوچک و محلی، مبنای موقت همبستگی و مشروعیت می‌شوند. در بستر رسانه، این چارچوب برای تحلیل فروپاشی رسانهٔ عمومی، ظهور رسانه‌های خرد و محلی، شکاف میان خبر حرفه‌ای و روایت‌های شخصی و بحران اعتماد به نهادهای خبری به‌کار می‌رود.",
   "assumptions": [
     "کلان‌روایت‌ها دیگر توان مشروعیت‌بخشی خود را از دست داده‌اند.",
     "دانش در قالب بازی‌های زبانی متکثر و ناهمگون سازمان می‌یابد.",
     "معیار مشروعیت از حقیقت به عملکرد و کارآمدی منتقل شده است."
   ],
   "principles": [
     "بی‌اعتمادی به کلان‌روایت‌ها تعریف وضعیت پست‌مدرن است.",
     "دانش، متکثر و بازی‌گون است، نه واحد و بنیادین.",
     "مشروعیت، محلی، موقت و عملکردمحور می‌شود."
   ],
   "critiques": [
     "ابهام و تاریخ‌مندی مفهوم: «پست‌مدرن» مفهومی لغزان و دوره‌بندی‌شده است و معلوم نیست چه چیزی دقیقاً پس از مدرنیته رخ داده است.",
     "مرگ زودهنگام کلان‌روایت‌ها: دین، ملی‌گرایی، نئولیبرالیسم و روایت‌های تازهٔ فناوری نشان می‌دهند کلان‌روایت‌ها بازگشته‌اند یا هرگز نرفته بودند.",
     "پیامد سیاسی: تأکید بر تکثر و ناتوانی داوری فراگیر، می‌تواند به نسبیت‌گرایی و تضعیف نقد سیاسی بینجامد، هرچند خود لیوتار به «عدالت» پایبند بود."
   ],
   "applications": [
     "تحلیل بحران اعتماد به رسانه و نهادهای خبری.",
     "پژوهش دربارهٔ رسانه‌های خرد و محلی.",
     "نقد سیاست‌های «کارآمدی» در آموزش و پژوهش.",
     "تحلیل اقتصاد دانش و کالایی‌شدن اطلاعات."
   ],
   "evolution": "لیوتار (۱۹۷۹) گزارش را به سفارش شورای دانشگاهی کبک نوشت؛ سپس در «اختلاف» (۱۹۸۳) نظریهٔ بازی‌های زبانی را به عدالت و حقوق گستراند و در دههٔ ۱۹۹۰، بحث اینترنت و «جامعهٔ اطلاعات» مفهوم او را دوباره مرکزی کرد.",
   "key_concepts": ["کلان‌روایت (metanarrative)", "بی‌اعتمادی (incredulity)", "بازی زبانی (language game)", "عملکرد (performativity)", "خردروایت (little narrative)", "کالایی‌شدن دانش"],
   "studies": ["Lyotard, J.-F. (1979). La condition postmoderne. Les Éditions de Minuit.", "Lyotard, J.-F. (1983). Le différend. Les Éditions de Minuit."],
   "detailed_analysis": "۱. بنیان و منطق نظری\nلیوتار از فلسفهٔ علم و ویتگنشتاین آغاز کرد: علم، خود یک بازی زبانی است و برای مشروعیت، به روایتی بیرون از خود نیاز دارد. پرسش او این بود که وقتی آن روایت‌ها فرو بریزند، علم بر چه چیزی تکیه می‌کند.\n\n۲. زوال مشروعیت\nپاسخ او، انتقال به عملکرد بود: دانشی که سیستم را کارآمدتر کند، مشروع است. همین انتقال، خطر را روشن می‌کند: دانش می‌تواند از حقیقت جدا شود و به ابزار بهینه‌سازی بدل گردد.\n\n۳. پیوند رسانه‌ای و نقد\nرسانه در این تحلیل، هم حامل روایت‌ها و هم ویرانگر آن‌هاست. نقد اصلی به لیوتار این است که «پایان روایت‌ها» را زود اعلام کرد؛ اما تحلیل او از تکثر روایت‌ها و کالایی‌شدن دانش، همچنان برای فهم رسانهٔ شبکه‌ای راهگشاست.",
   "critique_text": "\n".join([
     "۱. ابهام مفهوم: «پست‌مدرن» مفهومی لغزان و دوره‌بندی‌شده است و روشن نمی‌کند چه چیزی دقیقاً پس از مدرنیته رخ داده است.",
     "۲. مرگ زودهنگام روایت‌ها: دین، ملی‌گرایی و نئولیبرالیسم نشان می‌دهند کلان‌روایت‌ها بازگشته‌اند یا هرگز نرفته بودند.",
     "۳. نسبیت‌گرایی: تأکید بر تکثر و ناتوانی داوری فراگیر، می‌تواند نقد سیاسی را تضعیف کند؛ هرچند خود لیوتار به عدالت پایبند بود."]),
   "example_text": "یک پلتفرم خبری با میلیون‌ها کاربر، به‌جای تکیه بر روایت «رسانهٔ مستقل»، اعتبار خود را با شاخص‌های تعامل و سرعت می‌سازد؛ همین، انتقال از مشروعیت روایی به مشروعیت عملکردی است که لیوتار توصیف کرد.",
 },
 "MC-342": {
   "summary": "«نظریهٔ نمایشی» (Dramaturgy) اروینگ گافمن زندگی اجتماعی را به‌مثابهٔ اجرای تئاتری تحلیل می‌کند: افراد در تعامل، خود را برای مخاطب اجرا می‌کنند و با «مدیریت برداشت»، تصویری که دیگران از آن‌ها می‌سازند را هدایت می‌کنند. گافمن این چارچوب را در «The Presentation of Self in Everyday Life» (۱۹۵۹، Anchor Books) بسط داد (Goffman, 1959).",
   "definition": "نظریهٔ نمایشی، تعامل اجتماعی را اجرایی می‌بیند که در آن کنشگر با استفاده از محیط، ظاهر و رفتار، تعریفی از موقعیت ارائه می‌دهد و می‌کوشد برداشت مخاطب را مدیریت کند (Goffman, 1959).",
   "main_problem": "چگونه نظم اجتماعی در تعامل روزمره حفظ می‌شود، در حالی که هر فرد منافع و تصویری متفاوت دارد؛ و چگونه افراد میان «خودِ اجراشده» و «خودِ پشت صحنه» تمایز می‌گذارند؟",
   "mechanism": "تحلیل گافمن بر پنج سازوکار استوار است. (۱) اجرا و تعریف موقعیت: هر تعامل، اجرایی است که تعریفی از موقعیت را پیشنهاد می‌کند و طرفین آن را می‌پذیرند، تعدیل می‌کنند یا به چالش می‌کشند. (۲) صحنهٔ جلو: محیط (دکور)، ظاهر (نشانه‌های موقعیت اجتماعی) و رفتار (لحن و شیوهٔ حضور) سه عنصر اجرای جلوی صحنه‌اند. (۳) صحنهٔ پشت: جایی که اجرا آماده یا رها می‌شود و فرد از فشار حفظ ظاهر می‌آساید؛ دسترسی به پشت صحنه، امتیاز و نشانهٔ نزدیکی است. (۴) مدیریت برداشت: فرد با ایده‌آل‌سازی، پنهان‌کردن خطاها، هماهنگی با انتظارات و کنترل بیان، برداشت مخاطب را هدایت می‌کند. (۵) تیم اجرا: اجرا اغلب گروهی است و اعضای تیم برای حفظ تعریف مشترک موقعیت همکاری می‌کنند. در بستر رسانه، این چارچوب برای تحلیل پروفایل شبکهٔ اجتماعی، مصاحبهٔ تلویزیونی، اجرای سیاستمدار در دوربین و مرز میان «زندگی خصوصی» و «تصویر عمومی» به‌کار می‌رود؛ رسانه‌های شبکه‌ای، صحنهٔ جلو را گسترده و پشت صحنه را کم‌عمق کرده‌اند و مدیریت برداشت به مهارتی روزمره بدل شده است.",
   "assumptions": [
     "تعامل اجتماعی، اجرایی برای مخاطب است.",
     "افراد می‌کوشند برداشت دیگران را مدیریت کنند.",
     "مرز میان صحنهٔ جلو و پشت صحنه، نظم تعامل را ممکن می‌کند."
   ],
   "principles": [
     "خود، در تعامل اجرا و ارائه می‌شود.",
     "صحنهٔ جلو و پشت، دو قلمرو متفاوت تعامل‌اند.",
     "مدیریت برداشت، شرط پذیرش اجتماعی است."
   ],
   "critiques": [
     "استعارهٔ تئاتر، تعامل را بیش از حد محاسبه‌گرانه و ابزاری می‌بیند و صداقت و عادت را کم‌رنگ می‌کند.",
     "تحلیل، ساختار قدرت، طبقه و نابرابری را در حاشیه می‌گذارد و به سطح تعامل بسنده می‌کند.",
     "زمینهٔ فرهنگی: الگوی اجرا و مرز پشت صحنه در فرهنگ‌های جمع‌گرا و سلسله‌مراتبی متفاوت است و تعمیم آن نیازمند احتیاط است."
   ],
   "applications": [
     "تحلیل خودنمایی و مدیریت تصویر در شبکه‌های اجتماعی.",
     "پژوهش دربارهٔ اجرای سیاسی در تلویزیون و رسانه.",
     "مطالعهٔ خدمات مشتری و تعامل سازمانی.",
     "آموزش مهارت‌های ارتباطی و مصاحبه."
   ],
   "evolution": "گافمن چارچوب را در ۱۹۵۹ صورت‌بندی کرد و در «آیین تعامل» (۱۹۶۷) به مفهوم «آبرو» و نظم تعامل گستراند؛ در دههٔ اخیر، پژوهش هویت آنلاین آن را برای تحلیل پروفایل و اجرای دیجیتال بازخوانی کرده است.",
   "key_concepts": ["اجرا (performance)", "صحنهٔ جلو (front stage)", "پشت صحنه (backstage)", "مدیریت برداشت (impression management)", "تعریف موقعیت (definition of the situation)", "تیم اجرا (performance team)"],
   "studies": ["Goffman, E. (1959). The presentation of self in everyday life. Anchor Books.", "Goffman, E. (1967). Interaction ritual: Essays on face-to-face behavior. Pantheon Books."],
   "detailed_analysis": "۱. بنیان و منطق نظری\nگافمن پرسید نظم تعامل چگونه حفظ می‌شود. پاسخ او، نه هنجارهای انتزاعی، بلکه کار عملی افراد بود: هر کس در تعامل، تعریفی از موقعیت ارائه می‌دهد و برای اینکه تعامل پیش برود، طرفین آن را محترم می‌شمارند.\n\n۲. چرا استعارهٔ تئاتر کارآمد است\nتئاتر، سه عنصر دارد: اجرا، مخاطب و پشت صحنه. گافمن همین سه را در زندگی روزمره دید و نشان داد که «خود» نه جوهری ثابت، بلکه محصول اجرا و موقعیت است.\n\n۳. پیوند رسانه‌ای و نقد\nدر شبکه‌های اجتماعی، صحنهٔ جلو دائمی شده و پشت صحنه کم‌عمق؛ نتیجه، فشار مداوم مدیریت برداشت است. نقد اصلی این است که استعارهٔ تئاتر، تعامل را محاسبه‌گرانه می‌بیند و قدرت ساختاری را نادیده می‌گیرد؛ اما گافمن خود «خود» را اجتماعی می‌دید، نه صرفاً نمایشی.",
   "critique_text": "\n".join([
     "۱. محاسبه‌گری افراطی: استعارهٔ تئاتر، تعامل را ابزاری و نمایشی می‌بیند و صداقت، عادت و خودانگیختگی را کم‌رنگ می‌کند.",
     "۲. غفلت ساختاری: تحلیل به سطح تعامل بسنده می‌کند و طبقه، قدرت و نابرابری را در حاشیه می‌گذارد.",
     "۳. تفاوت فرهنگی: مرز پشت صحنه و الگوی اجرا در فرهنگ‌های جمع‌گرا و سلسله‌مراتبی متفاوت است و تعمیم آن نیازمند احتیاط است."]),
   "example_text": "یک سیاستمدار در مصاحبهٔ تلویزیونی، با انتخاب لباس، لحن و پاسخ‌های آماده، «صحنهٔ جلو» را مدیریت می‌کند؛ پس از پایان برنامه، در راهروی پشت استودیو، همان فرد با تیم خود از اجرا و خطاها حرف می‌زند. مرز این دو فضا، همان چیزی است که گافمن تحلیل می‌کند.",
 },
}

REQUIRED_SECTIONS = ["summary", "definition", "main_problem", "mechanism", "assumptions",
                     "principles", "critiques", "applications", "evolution", "key_concepts",
                     "theorists", "model", "studies"]

def wc(v):
    if isinstance(v, str): return len(v.split())
    if isinstance(v, list):
        n = 0
        for it in v:
            if isinstance(it, str): n += len(it.split())
            elif isinstance(it, dict): n += len(' '.join(str(x) for x in it.values()).split())
        return n
    if isinstance(v, dict): return len(' '.join(str(x) for x in v.values()).split())
    return 0

def has_content(v):
    if v is None: return False
    if isinstance(v, str): return len(v.strip()) > 10
    if isinstance(v, (list, dict)): return len(v) > 0
    return True

def rubric(p, n_verified, n_sources, n_relations):
    detail = {}
    present = [k for k in REQUIRED_SECTIONS if has_content(p.get(k))]
    detail["structure_15"] = round(15 * min(1, len(present)/7))
    words = sum(wc(p.get(k)) for k in ["summary","definition","main_problem","mechanism",
                "critiques","applications","evolution","key_concepts","principles","studies","assumptions"])
    a = 15 if words>=500 else 13 if words>=300 else 11 if words>=180 else 8 if words>=100 else 3
    detail["analysis_15"] = a
    if n_verified>=1 and n_sources>=2: detail["citation_20"] = 20
    elif n_verified>=1: detail["citation_20"] = 17
    elif n_sources>=1: detail["citation_20"] = 10
    else: detail["citation_20"] = 0
    acc = 0
    if has_content(p.get("summary")) or has_content(p.get("definition")): acc += 10
    if n_verified>=1: acc += 9
    if len(present)>=6: acc += 6
    detail["accuracy_25_auto"] = min(25, acc)
    detail["relations_10"] = 10 if n_relations>=1 else 6
    detail["classification_5"] = 5 if (p.get("field") or p.get("mapping")) else 2
    detail["clarity_5"] = 5 if has_content(p.get("summary")) else 2
    detail["currency_5"] = 5
    return min(100, sum(detail.values())), detail, words

def main():
    c = pymysql.connect(host="127.0.0.1", user="root", password="433700", database=DB, charset="utf8mb4", autocommit=False)
    cur = c.cursor()
    codes = ["MC-338", "MC-340", "MC-341", "MC-342"]
    cur.execute("SELECT id, code, properties FROM kb_entities WHERE code IN (%s)" % ",".join(["%s"]*len(codes)), codes)
    rows = {code:(eid, json.loads(pr)) for (eid, code, pr) in cur.fetchall()}
    with open(BACKUP, "w", encoding="utf-8") as f:
        json.dump([{"code": cd, "props": rows[cd][1]} for cd in codes if cd in rows], f, ensure_ascii=False, indent=1)
    print("backup ->", len(rows), "rows")

    for code in codes:
        eid, p = rows[code]
        e = ENRICH[code]
        if "critique_text" in e: p["critique"] = e["critique_text"]
        if "example_text" in e: p["example"] = e["example_text"]
        for k, v in e.items():
            if k in ("critique_text", "example_text"): continue
            p[k] = v
        if not has_content(p.get("definition")) and has_content(p.get("summary")):
            p["definition"] = p["summary"]
        spec = S[code]
        p["sources"] = [dict(citation=s["citation"], language=("انگلیسی" if s["language"]=="en" else "فارسی"),
                              doi=s.get("doi") or "", url=s.get("url") or "", year=s.get("year")) for s in spec]
        p["citations"] = [dict(source=s["citation"], locator=s["locator"], supports=s["supports"],
                               verified=bool(s.get("verified"))) for s in spec]
        n_sources = len(spec)
        n_verified = sum(1 for s in spec if s.get("verified"))
        cur.execute("SELECT COUNT(*) FROM kb_relations r JOIN kb_entities a ON r.source_id=a.id JOIN kb_entities b ON r.target_id=b.id WHERE a.code=%s OR b.code=%s", (code, code))
        n_relations = cur.fetchone()[0]
        score, detail, words = rubric(p, n_verified, n_sources, n_relations)
        p["quality_score"] = score
        p["quality_assessment"] = dict(breakdown=detail, total=score,
            method="SPEC §6.1 auto-structural (accuracy is auto-credit, NOT human verification)",
            scored_at=NOW, scored_by=STAMP)
        p["status_scientific_note"] = "score is structural/citation-based; requires human expert review for scientific verification (SPEC §6.4)"
        p["updated_at"] = NOW; p["updated_by"] = STAMP
        cur.execute("UPDATE kb_entities SET properties=%s, version=version+1, updated_at=%s, updated_by=%s WHERE id=%s",
                    (json.dumps(p, ensure_ascii=False), NOW, STAMP, eid))
        for s in spec:
            sid = None
            if s.get("doi"):
                cur.execute("SELECT id FROM kb_sources WHERE doi=%s", (s["doi"],))
                r = cur.fetchone(); sid = r[0] if r else None
            if sid is None:
                cur.execute("SELECT id FROM kb_sources WHERE title_en=%s AND year=%s", (s["title_en"], s.get("year")))
                r = cur.fetchone(); sid = r[0] if r else None
            if sid is None:
                cur.execute("""INSERT INTO kb_sources (kind,title_fa,title_en,year,publisher,doi,isbn,url,language,access_type,bibliographic)
                                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                    (s["kind"], s.get("title_fa"), s["title_en"], s.get("year"), s.get("publisher"),
                     s.get("doi"), s.get("isbn"), s.get("url"), s.get("language"),
                     "open" if (s.get("doi") or s.get("url")) else "unknown",
                     json.dumps({"authors": s.get("authors"), "citation": s["citation"]}, ensure_ascii=False)))
                sid = cur.lastrowid
            cur.execute("SELECT 1 FROM kb_evidence e WHERE e.about_code=%s AND e.source_id=%s LIMIT 1", (code, sid))
            if cur.fetchone(): continue
            lt = "PAGE" if s.get("locator_type") == "page_range" else ("CHAPTER" if s.get("locator_type") == "CHAPTER" else "SECTION")
            cur.execute("""INSERT INTO kb_citations (source_id,locator_type,locator_value,paraphrase,citation_style,language,accessed_at)
                            VALUES (%s,%s,%s,%s,'apa',%s,%s)""",
                        (sid, lt, s.get("locator"), "پشتیبانی از بخش: "+s.get("supports",""), s.get("language","en"), NOW))
            cid = cur.lastrowid
            cur.execute("""INSERT INTO kb_evidence (source_id,citation_id,about_code,evidence_type,evidence_summary,locator,verification_status,extraction_method,direction)
                            VALUES (%s,%s,%s,'bibliographic_reference',%s,%s,%s,'ai_extraction','supports')""",
                        (sid, cid, code, s["citation"], s.get("locator"), "verified" if s.get("verified") else "unverified"))
        cur.execute("SELECT COALESCE(MAX(version),0)+1 FROM kb_entity_versions WHERE entity_id=%s", (eid,))
        ver = cur.fetchone()[0]
        cur.execute("INSERT INTO kb_entity_versions (entity_id, version, snapshot, change_reason, changed_by, created_at) VALUES (%s,%s,%s,%s,%s,%s)",
                    (eid, ver, json.dumps({"quality_score": score, "words": words, "sources": n_sources, "verified": n_verified}, ensure_ascii=False),
                     "documented sourcing + rubric score; corrected mismatched boilerplate where present", STAMP, NOW))
        cur.execute("INSERT INTO kb_audit_log (entity_code, action, detail, source) VALUES (%s,%s,%s,%s)",
                    (code, "DOC_ENRICH", json.dumps({"quality_score": score, "words": words, "sources": n_sources, "verified": n_verified, "breakdown": detail}, ensure_ascii=False), STAMP))
        print(f"{code}: score={score} words={words} sources={n_sources} verified={n_verified} relations={n_relations} | {detail}")
    c.commit()
    c.close()
    print("BATCH65 THEORY DONE")

if __name__ == "__main__":
    main()
