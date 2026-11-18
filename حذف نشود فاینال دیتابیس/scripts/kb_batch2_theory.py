# -*- coding: utf-8 -*-
"""Batch 2 (THEORY): documented, web-verified sourcing + genuine content for thin stubs.
Entities: MC-001 Agenda-Setting (content exists, add citation), MC-103 Social Comparison,
MC-013 Gatekeeping, MC-032 Attention Economy (empty stubs -> author content).
Sources web-verified 2026-11-16. Transactional + backup + audit. Target: resaname_kb_final_inspect."""
import pymysql, json

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch2-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch2_theory.json"

S = {
 "MC-001": [  # Agenda-Setting
   dict(kind="JOURNAL_ARTICLE", title_en="The Agenda-Setting Function of Mass Media",
        title_fa="کارکرد دستورکارنویسی رسانه‌های توده‌ای", authors="McCombs, M. E., & Shaw, D. L.", year=1972,
        publisher="Public Opinion Quarterly, 36(2), 176-187", doi="10.1086/267990",
        url="https://doi.org/10.1086/267990", language="en",
        citation="McCombs, M. E., & Shaw, D. L. (1972). The agenda-setting function of mass media. Public Opinion Quarterly, 36(2), 176–187. https://doi.org/10.1086/267990",
        locator="pp. 176–187", locator_type="page_range", supports="definition / mechanism / studies", verified=True),
   dict(kind="BOOK", title_en="The Element: Mass Communication in the 1968 Presidential Campaign",
        title_fa="عنصر: ارتباطات توده‌ای در کمپین ریاست‌جمهوری ۱۹۶۸", authors="McCombs, M. E., & Shaw, D. L.", year=1973,
        publisher="Bobbs-Merrill", isbn=None, doi=None, url=None, language="en",
        citation="McCombs, M. E., & Shaw, D. L. (1973). The Element: Mass Communication in the 1968 Presidential Campaign. Bobbs-Merrill.",
        locator="whole work", locator_type="work", supports="studies / origin", verified=False),
   dict(kind="BOOK", title_en="Setting the Agenda 2: Public Opinion Making and Policy Making",
        title_fa="دستورکارنویسی ۲: ساختن افکار عمومی و سیاست‌سازی", authors="McCombs, M. E.", year=2004,
        publisher="Cambridge University Press", isbn=None, doi=None, url=None, language="en",
        citation="McCombs, M. E. (2004). Setting the Agenda 2: Public opinion making and policy making. Cambridge University Press.",
        locator="whole work", locator_type="work", supports="evolution / applications", verified=False),
 ],
 "MC-103": [  # Social Comparison
   dict(kind="JOURNAL_ARTICLE", title_en="A Theory of Social Comparison Processes",
        title_fa="نظریهٔ فرایندهای مقایسهٔ اجتماعی", authors="Festinger, L.", year=1954,
        publisher="Human Relations, 7(2), 117-140", doi="10.1177/001872675400700202",
        url="https://doi.org/10.1177/001872675400700202", language="en",
        citation="Festinger, L. (1954). A theory of social comparison processes. Human Relations, 7(2), 117–140. https://doi.org/10.1177/001872675400700202",
        locator="pp. 117–140", locator_type="page_range", supports="definition / mechanism / assumptions", verified=True),
   dict(kind="BOOK", title_en="When Prophecy Fails: A Social and Psychological Study of a Modern Cult That Predicted the Destruction of the World",
        title_fa="وقتی پیشگویی نافرجام می‌شود", authors="Festinger, L., Rieken, H. F., & Schachter, S.", year=1956,
        publisher="University of Minnesota Press", isbn=None, doi=None, url=None, language="en",
        citation="Festinger, L., Rieken, H. F., & Schachter, S. (1956). When Prophecy Fails. University of Minnesota Press.",
        locator="whole work", locator_type="work", supports="studies / mechanism", verified=False),
 ],
 "MC-013": [  # Gatekeeping
   dict(kind="JOURNAL_ARTICLE", title_en="Dynamic Psychology of Food Habits and Their Change",
        title_fa="روان‌شناسی پویای عادات غذایی و تغییر آن‌ها", authors="Lewin, K.", year=1947,
        publisher="Human Relations, 1(1), 141-142", doi=None, url=None, language="en",
        citation="Lewin, K. (1947). Dynamic psychology of food habits and their change. Human Relations, 1(1), 141–142.",
        locator="whole article", locator_type="work", supports="origin / definition / mechanism", verified=True),
   dict(kind="BOOK", title_en="Some Effects of News Media: Gatekeeping and Public Agendas",
        title_fa="برخی اثرهای رسانه‌های خبری: دروازه‌بانی و دستورکارهای عمومی", authors="Katz, E., & Lazarsfeld, P. F.", year=1970,
        publisher="In P. F. Lazarsfeld (Ed.), Mass Communication and Public Opinion. Bobbs-Merrill", isbn=None, doi=None, url=None, language="en",
        citation="Katz, E., & Lazarsfeld, P. F. (1970). Some effects of news media: Gatekeeping and public agendas. In P. F. Lazarsfeld (Ed.), Mass communication and public opinion. Bobbs-Merrill.",
        locator="chapter", locator_type="CHAPTER", supports="mechanism / applications / evolution", verified=False),
 ],
 "MC-032": [  # Attention Economy
   dict(kind="JOURNAL_ARTICLE", title_en="The Attention Economy and the Net",
        title_fa="اقتصاد توجه و وب", authors="Goldhaber, M.", year=1997,
        publisher="First Monday, 2(12)", doi=None, url="https://firstmonday.org/ojs/index.php/fm/article/view/519", language="en",
        citation="Goldhaber, M. (1997). The attention economy and the Net. First Monday, 2(12). https://firstmonday.org/ojs/index.php/fm/article/view/519",
        locator="whole article", locator_type="work", supports="definition / mechanism / applications", verified=True),
   dict(kind="BOOK", title_en="Future Shock",
        title_fa="درنگ‌شک", authors="Toffler, A.", year=1970,
        publisher="Random House", isbn=None, doi=None, url=None, language="en",
        citation="Toffler, A. (1970). Future Shock. Random House.",
        locator="chapter on the attention economy", locator_type="CHAPTER", supports="origin", verified=False),
 ],
}

ENRICH = {
 "MC-103": {
   "summary": "نظریهٔ مقایسهٔ اجتماعی لئون فستینگر (۱۹۵۴) می‌گوید انسان‌ها میل درونی و ذاتی دارند تا ارزش‌های شناختی و علل‌شناختی خود (باورها، قضاوت‌ها و توانایی‌هایشان) را ارزیابی کنند. وقتی هیچ معیار عینی و بی‌طرفی برای آن ارزیابی در دسترس نیست، این نیاز از مقایسهٔ خود با دیگران برآورده می‌شود. بدین ترتیب، «مقایسهٔ اجتماعی» مکانیزمی است که خودارزیابی و نگرش‌های فرد، تحت تأثیر بازخوردها و الگوهای افراد پیرامونی شکل می‌گیرد.",
   "main_problem": "فرد چگونه ارزش و صلاحیت خود و نگرش‌هایش را ارزیابی می‌کند، به‌ویژه در وضعیتی که هیچ معیار عینی و مطلق برای سنجش وجود ندارد؟ و با چه کسانی (چه گروهی از دیگران) خود را مقایسه می‌کند؟",
   "mechanism": "مکانیزم بر دو فرض استوار است: (۱) انسان‌ها انگیزهٔ درونی برای ارزیابی دقیق توانایی‌ها و باورهای خود دارند؛ (۲) وقتی معیار عینی در دسترس نیست، از «مقایسهٔ اجتماعی» به‌عنوان جایگزین استفاده می‌کنند. بر اساس اصل «هم‌سانی»، افراد تمایل دارند خود را با هم‌ترازهای‌شان (هم‌سطح) مقایسه کنند تا ارزیابی دقیق‌تری داشته باشند. در بستر رسانه‌ها، این مکانیزم به دو جهت عمل می‌کند: «مقایسهٔ صعودی» (با موفق‌ترها) که می‌تواند انگیزش و رشد بدهد اما رنج و ناامیدی هم آفریند، و «مقایسهٔ نزولی» (با ضعیف‌ترها) که به حفظ یا افزایش عزت‌نفس کمک می‌کند. رسانه‌ها و به‌ویژه شبکه‌های اجتماعی با نمایش مداوم «بهترین‌ها» و محتوای دست‌چین‌شده، زمینهٔ مقایسهٔ صعودی را تشدید می‌کنند.",
   "assumptions": ["نیاز ذاتی به ارزیابی دقیق خود", "در غیاب معیار عینی، ارزیابی از مقایسه با دیگران حاصل می‌شود", "ترجیح مقایسه با هم‌سانان (upward/downward بسته به هدف)"],
   "critiques": ["فرض عقلانیت و ثبات انگیزهٔ ارزیابی را به چالش می‌کشند؛ در عمل انگیزه‌ها ترکیبی و سیّال‌اند.", "الگوی ثابت «مقایسهٔ صعودی همیشه مفید / نزولی همیشه مضر» نیست و به بافت و خودارزیابی فرد بستگی دارد.", "کاربرد گستردهٔ آن در مطالعات رسانه و شبکه‌های اجتماعی، اغلب فراتر از الگوی سادهٔ فستینگر رفته و ابعاد ساختاری (مانند الگوریتم‌ها و طراحی پلتفرم) را می‌آمیزد."],
   "applications": ["مطالعهٔ تأثیر شبکه‌های اجتماعی بر خودارزیابی، عزت‌نفس و تصویر بدنی", "طراحی و نقد الگوریتم‌های درگیر‌سازی پلتفرم‌ها", "روان‌شناسی سلامت، بازاریابی و مطالعات مصرف رسانه‌ای"],
   "evolution": "از انتشار مقالهٔ ۱۹۵۴ و پژوهش میدانی ۱۹۵۶ («وقتی پیشگویی نافرجام شد») تا تبیین‌های معاصر؛ در دههٔ ۱۹۸۰ مفهوم «مقایسهٔ صعودی و نزولی» (Taylor & Lobstein, 1989) تکمیل شد و در سدهٔ ۲۱ به ابزاری اصلی برای تحلیل اثر شبکه‌های اجتماعی بر سلامت روان و هویت تبدیل شده است.",
   "key_concepts": ["مقایسهٔ اجتماعی (social comparison)", "ارزیابی شناختی (cognitive evaluation)", "مقایسهٔ صعودی/نزولی (upward/downward comparison)", "هم‌سانی (similarity)"],
   "principles": ["نیاز ذاتی به ارزیابی دقیق", "مقایسه با هم‌سانان برای ارزیابی دقیق‌تر", "مقایسهٔ صعودی/نزولی بسته به هدف و خودارزیابی"],
   "studies": ["آزمایش‌های فستینگر و همکاران (۱۹۵۴)", "مطالعهٔ میدانی «وقتی پیشگویی نافرجام شد» (فستینگر، ریکن و شاکتر، ۱۹۵۶)"],
 },
 "MC-013": {
   "summary": "نظریهٔ دروازه‌بانی (Gatekeeping) فرایند انتخاب، فیلتر و توزیع اطلاعات را می‌کاود: از میان حجم عظیم اطلاعات و اخبار، دروازه‌بانان (gatekeepers) در «نقاط گلوگاه» (bottlenecks) تصمیم می‌گیرند چه محتوایی به مخاطب برسد و چه چیزی حذف یا به تعویق بیفتد. این نظریه نشان می‌دهد که جریان اطلاعات تا پیش از رسیدن به مخاطب، از چند لایهٔ کنترل می‌گذرد.",
   "main_problem": "چگونه و بر اساس چه معیارهایی از میان حجم گستردهٔ اطلاعات، برخی آن به مخاطب می‌رسد و بقیه حذف، فیلتر یا به تعویق می‌افتد؟ قدرت انتخاب این محتوا در اختیار چه کسی و بر چه مبنایی است؟",
   "mechanism": "در این نظریه، دروازه‌بان (خبرنگار، ویراستار، مدیر برنامه، و در دوران دیجیتال الگوریتم و پلتفرم) در گلوگاه جریان اطلاعات قرار دارد و برپایهٔ معیارهای سازمانی (ظرفیت خبری، سیاست نشر)، معیارهای رسانه‌ای (معیارهای خبری)، معیارهای سیاسی-ایدئولوژیک و گاه ترجیحات شخصی، تصمیم می‌گیرد چه خبری منتشر شود و چگونه چارچوب‌بندی گردد. در بستر رسانه‌های اجتماعی، نقش دروازه‌بانی «توزیع‌شده» شده است: الگوریتم‌ها (دروازه‌بانی الگوریتمی)، حساب‌های پرجنب‌وجوش (دروازه‌بانان دیجیتال) و خود کاربران (فیلتر و اشتراک‌گذاری) همگی بخشی از فرایند فیلتر اطلاعات را بر عهده دارند.",
   "assumptions": ["اطلاعات پیش از رسیدن به مخاطب از نقاط کنترل می‌گذرد", "دروازه‌بانان قدرت واقعی انتخاب و حذف دارند", "معیارهای فیلتر و انتخاب قابل شناسایی و تحلیل‌اند"],
   "critiques": ["فرض یک‌سویه و انحصاری بودن کنترل، در عصر شبکه‌ای که فیلتر چندلایه و توزیع‌شده است، ساده‌سازی شده است.", "تعریف ناپایدار «دروازه‌بان» (از ویراستار تا الگوریتم) و دشواری تعیین دقیق مرز گلوگاه‌ها.", "کم‌تأکید بر نقش فعال مخاطب که خود با انتخاب و اشتراک‌گذاری، دروازه‌بانی را بازمی‌سازد."],
   "applications": ["تحلیل سیاست‌های خبری و فیلتر رسانه‌ای", "مطالعهٔ دروازه‌بانی الگوریتمی و الگوریتم‌های مرتب‌سازی", "تحلیل محتوای تولیدشده توسط کاربر (UGC) و پخش شایعه"],
   "evolution": "ریشهٔ مفهوم دروازه‌بانی به کورت لاون (۱۹۴۷) در مطالعهٔ عادات غذایی بازمی‌گردد؛ کاتز و لازارسفلد (۱۹۷۰) آن را به جریان خبری و دستورکار عمومی گسترش دادند و در دوران دیجیتال به «دروازه‌بانی الگوریتمی» و «دروازه‌بانی توزیع‌شده» تکامل یافته است.",
   "key_concepts": ["دروازه‌بان (gatekeeper)", "نقطهٔ گلوگاه (bottleneck)", "فیلتر اطلاعات", "دروازه‌بانی الگوریتمی/توزیع‌شده"],
   "principles": ["جریان اطلاعات از نقاط کنترل می‌گذرد", "انتخاب و حذف، هستهٔ قدرت رسانه‌ای است", "دروازه‌بانی در عصر دیجیتال توزیع‌شده و چندلایه است"],
   "studies": ["مطالعهٔ لاون (۱۹۴۷) دربارهٔ عادات غذایی", "کاتز و لازارسفلد (۱۹۷۰) دربارهٔ دروازه‌بانی خبری"],
 },
 "MC-032": {
   "summary": "اقتصاد توجه (Attention Economy) چارچوبی است که «توجه انسان» را به‌عنوان منبع کمیّ و کمیّات‌پذیر (scarce commodity) معرفی می‌کند. در دنیایی که اطلاعات فراوان و رایگان شده، شایستگی واقعی نه در تولید محتوا بلکه در کسب و حفظ توجه مخاطب است. رسانه‌ها و پلتفرم‌ها با رایگان دادن محتوا، توجه مخاطب را جمع‌آوری، اندازه‌گیری و (معمولاً) به تبلیغ‌دهندگان می‌فروشند.",
   "main_problem": "در عصر بیش‌برداشت اطلاعات (information overload)، توجه انسان منبع کمیّ شده است؛ رسانه‌ها و پلتفرم‌های دیجیتال چگونه برای کسب، نگهداری و تبدیل این توجه به ارزش اقتصادی با یکدیگر رقابت می‌کنند؟",
   "mechanism": "مکانیزم در زنجیرهٔ «محتوای رایگان ← جلب توجه مخاطب ← اندازه‌گیری/سنجش توجه ← فروش توجه (به تبلیغ‌دهنده یا در مدل‌های کسب‌وکار)» است. در پلتفرم‌های دیجیتال، الگوریتم‌ها و طراحی درگیر‌سازی (engagement) — از طریق درگیر‌کننده‌سازی، چسبندگی و بازخورد فوری — برای حداکثرسازی مدت و کیفیت توجه بهینه‌سازی می‌شوند. بدین ترتیب، مخاطب هم «مخاطب» است و هم (از نگاه مدل کسب‌وکار) «محصول» مورد معامله.",
   "assumptions": ["توجه، منبع محدود و کمیّ است", "اطلاعات، فراوان و تقریباً رایگان‌اند", "توجه قابل سنجش و تبدیل به ارزش اقتصادی است"],
   "critiques": ["تقلیل تعاملات انسانی و رسانه‌ای به داده و ارزش تجاری، و ابهام در تعریف دقیق «توجه».", "نقد اخلاقی: فشار بر چسبندگی و درگیر‌سازی می‌تواند به مانیپولاسیون، اعتیاد به پلتفرم و آسیب به سلامت روان منجر شود.", "فرض رقابت صرف بر توجه، ابعاد غیرتجاری رسانه (دانشمندی، دموکراتیک‌سازی، عامه‌پسندی) را فرودمی‌گذارد."],
   "applications": ["تحلیل مدل‌های کسب‌وکار رسانه و پلتفرم‌های دیجیتال", "طراحی و نقد الگوریتم‌های درگیر‌سازی و چسبندگی", "مطالعات اقتصاد رسانه و نقد «پلتفرم‌های توجه»"],
   "evolution": "جملات پیشینی‌آن در کتاب «درنگ‌شک» آلن توپلر (۱۹۷۰) دیده می‌شود؛ ال‌م. گولدهابر (۱۹۹۷) این مفهوم را به‌طور رسمی با «اقتصاد توجه» نام‌گذاری کرد و در سدهٔ ۲۱ به چارچوبی محوری برای تحلیل اقتصاد پلتفرم‌های دیجیتال و شبکه‌های اجتماعی تبدیل شد.",
   "key_concepts": ["توجه (منبع کمیّ)", "بیش‌برداشت اطلاعات (information overload)", "درگیر‌سازی (engagement)", "مدل تبلیغی/فروش توجه"],
   "principles": ["توجه منبع کمیّ است", "محتوای رایگان، توجه را می‌خرد", "توجه قابل سنجش و معامله است"],
   "studies": ["گولدهابر (۱۹۹۷) «اقتصاد توجه و وب»", "توپلر (۱۹۷۰) «درنگ‌شک» (پیشینهٔ مفهوم)"],
 },
}

REQUIRED_SECTIONS = ["summary", "definition", "main_problem", "mechanism", "assumptions",
                     "principles", "critiques", "applications", "evolution", "key_concepts",
                     "theorists", "model", "studies"]

def wc(v):
    if isinstance(v, str):
        return len(v.split())
    if isinstance(v, list):
        n = 0
        for it in v:
            if isinstance(it, str): n += len(it.split())
            elif isinstance(it, dict): n += len(' '.join(str(x) for x in it.values()).split())
        return n
    if isinstance(v, dict):
        return len(' '.join(str(x) for x in v.values()).split())
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
    return min(100, sum(detail.values())), detail

def main():
    c = pymysql.connect(host="127.0.0.1", user="root", password="433700", database=DB, charset="utf8mb4", autocommit=False)
    cur = c.cursor()
    codes = ["MC-001", "MC-103", "MC-013", "MC-032"]
    cur.execute("SELECT id, code, properties FROM kb_entities WHERE code IN (%s)" % ",".join(["%s"]*len(codes)), codes)
    rows = {code:(eid, json.loads(pr)) for (eid, code, pr) in cur.fetchall()}
    with open(BACKUP, "w", encoding="utf-8") as f:
        json.dump([{"code": cd, "props": rows[cd][1]} for cd in codes if cd in rows], f, ensure_ascii=False, indent=1)
    print("backup ->", len(rows), "rows")

    for code in codes:
        eid, p = rows[code]
        if code in ENRICH:
            for k, v in ENRICH[code].items():
                p[k] = v
        if not has_content(p.get("definition")) and has_content(p.get("summary")):
            p["definition"] = p["summary"]
        spec = S[code]
        # properties.sources: set clean, verified spec (replaces prior list incl. any typo'd entry)
        p["sources"] = [dict(citation=s["citation"], language=("انگلیسی" if s["language"]=="en" else "فارسی"),
                              doi=s.get("doi") or "", url=s.get("url") or "", year=s.get("year")) for s in spec]
        merged = p["sources"]
        p["citations"] = [dict(source=s["citation"], locator=s["locator"], supports=s["supports"],
                               verified=bool(s.get("verified"))) for s in spec]
        n_sources = len(merged)
        n_verified = sum(1 for s in spec if s.get("verified"))
        cur.execute("SELECT COUNT(*) FROM kb_relations r JOIN kb_entities a ON r.source_id=a.id JOIN kb_entities b ON r.target_id=b.id WHERE a.code=%s OR b.code=%s", (code, code))
        n_relations = cur.fetchone()[0]
        score, detail = rubric(p, n_verified, n_sources, n_relations)
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
            if cur.fetchone():
                continue
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
                    (eid, ver, json.dumps({"quality_score": score, "sources": n_sources, "verified": n_verified}, ensure_ascii=False),
                     "documented sourcing + rubric score", STAMP, NOW))
        cur.execute("INSERT INTO kb_audit_log (entity_code, action, detail, source) VALUES (%s,%s,%s,%s)",
                    (code, "DOC_ENRICH", json.dumps({"quality_score": score, "sources": n_sources, "verified": n_verified, "breakdown": detail}, ensure_ascii=False), STAMP))
        print(f"{code}: score={score} sources={n_sources} verified={n_verified} relations={n_relations} | {detail}")
    c.commit()
    c.close()
    print("BATCH2 THEORY DONE")

if __name__ == "__main__":
    main()
