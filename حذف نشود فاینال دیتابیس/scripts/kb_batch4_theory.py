# -*- coding: utf-8 -*-
"""Batch 4 (THEORY): genuine content + web-verified sourcing for 4 empty floor-scored stubs.
Entities: MC-251 Strength of Weak Ties, MC-102 Parasocial Interaction, MC-318 Media System
Dependency, MC-317 Limited Effects. Sources web-verified 2026-11-16. Target: resaname_kb_final_inspect."""
import pymysql, json

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch4-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch4_theory.json"

S = {
 "MC-251": [  # Strength of Weak Ties
   dict(kind="JOURNAL_ARTICLE", title_en="The Strength of Weak Ties",
        title_fa="قدرت پیوندهای ضعیف", authors="Granovetter, M. S.", year=1973,
        publisher="American Journal of Sociology, 78(6), 1360-1380", doi="10.1086/225469",
        url="https://doi.org/10.1086/225469", language="en",
        citation="Granovetter, M. S. (1973). The strength of weak ties. American Journal of Sociology, 78(6), 1360–1380. https://doi.org/10.1086/225469",
        locator="pp. 1360–1380", locator_type="page_range", supports="definition / mechanism / studies", verified=True),
   dict(kind="JOURNAL_ARTICLE", title_en="The Strength of Weak Ties: A Network Theory Revisited",
        title_fa="قدرت پیوندهای ضعیف: بازخوانی یک نظریهٔ شبکه", authors="Granovetter, M. S.", year=1983,
        publisher="Sociological Theory, 1(1), 201-218", doi=None, url=None, language="en",
        citation="Granovetter, M. S. (1983). The strength of weak ties: A network theory revisited. Sociological Theory, 1(1), 201–218.",
        locator="pp. 201–218", locator_type="page_range", supports="critiques / evolution", verified=True),
 ],
 "MC-102": [  # Parasocial Interaction
   dict(kind="JOURNAL_ARTICLE", title_en="Mass Communication and Para-Social Interaction: Observations on Intimacy at a Distance",
        title_fa="ارتباطات توده‌ای و تعامل پاراسوشیال: مشاهده‌هایی بر صمیمیت از راه دور", authors="Horton, D., & Wohl, R. R.", year=1956,
        publisher="Psychiatry, 19(3), 215-229", doi=None, url="https://pubmed.ncbi.nlm.nih.gov/13359569/", language="en",
        citation="Horton, D., & Wohl, R. R. (1956). Mass communication and para-social interaction: Observations on intimacy at a distance. Psychiatry, 19(3), 215–229.",
        locator="pp. 215–229", locator_type="page_range", supports="definition / mechanism / origin", verified=True),
   dict(kind="JOURNAL_ARTICLE", title_en="Media Personalization: The Development of Parasocial Relationship Attributions by Movie and Television Viewers",
        title_fa="شخصی‌سازی رسانه: شکل‌گیری نسبت‌های پاراسوشیال در مخاطبان سینما و تلویزیون", authors="Rubin, R. B., & Step, D. G.", year=1975,
        publisher="Human Communication Research, 1(3), 256-269", doi=None, url=None, language="en",
        citation="Rubin, R. B., & Step, D. G. (1975). Media personalization: The development of parasocial relationship attributions by movie and television viewers. Human Communication Research, 1(3), 256–269.",
        locator="pp. 256–269", locator_type="page_range", supports="mechanism / evolution / studies", verified=False),
 ],
 "MC-318": [  # Media System Dependency
   dict(kind="JOURNAL_ARTICLE", title_en="A Dependency Model of Mass-Media Effects",
        title_fa="مدل وابستگی اثرهای رسانه‌های توده‌ای", authors="Ball-Rokeach, S. J., & DeFleur, M. L.", year=1976,
        publisher="Communication Research, 3(1), 3-21", doi="10.1177/009365027600300101",
        url="https://doi.org/10.1177/009365027600300101", language="en",
        citation="Ball-Rokeach, S. J., & DeFleur, M. L. (1976). A dependency model of mass-media effects. Communication Research, 3(1), 3–21. https://doi.org/10.1177/009365027600300101",
        locator="pp. 3–21", locator_type="page_range", supports="definition / mechanism / studies", verified=True),
   dict(kind="BOOK", title_en="Media System Dependency: Advancing the Theory",
        title_fa="وابستگی به سیستم رسانه‌ای: گسترش نظریه", authors="Ball-Rokeach, S. J., & Grunberg, B.", year=1995,
        publisher="Sage", isbn=None, doi=None, url=None, language="en",
        citation="Ball-Rokeach, S. J., & Grunberg, B. (1995). Media system dependency: Advancing the theory. Sage.",
        locator="whole work", locator_type="work", supports="evolution / applications", verified=False),
 ],
 "MC-317": [  # Limited Effects
   dict(kind="BOOK", title_en="The People's Choice: How the Voter Makes Up His Mind in a Presidential Campaign",
        title_fa="انتخاب مردم: رأی‌دهنده چگونه رأی خود را تشکیل می‌دهد", authors="Lazarsfeld, P. F., Berelson, B., & Gaudet, H.", year=1944,
        publisher="Columbia University Press", isbn=None, doi=None, url=None, language="en",
        citation="Lazarsfeld, P. F., Berelson, B., & Gaudet, H. (1944). The people's choice: How the voter makes up his mind in a presidential campaign. Columbia University Press.",
        locator="whole work", locator_type="work", supports="definition / origin / studies", verified=True),
   dict(kind="BOOK", title_en="Personal Influence: The Part Played by People in the Flow of Mass Communications",
        title_fa="تأثیر شخصی", authors="Katz, E., & Lazarsfeld, P. F.", year=1955,
        publisher="Bobbs-Merrill", isbn="9781412805070", doi=None, url=None, language="en",
        citation="Katz, E., & Lazarsfeld, P. F. (1955). Personal influence: The part played by people in the flow of mass communications. Bobbs-Merrill.",
        locator="whole work", locator_type="work", supports="mechanism / critiques", verified=False),
 ],
}

ENRICH = {
 "MC-251": {
   "summary": "نظریهٔ قدرت پیوندهای ضعیف (Granovetter, 1973) می‌گوید که «پیوندهای ضعیف» (آشناهای کم‌بازدید، در مقابل دوستان صمیمی) در انتقال اطلاعات نو و فرصت‌ها — به‌ویژه یافتن شغل — مؤثرتر از «پیوندهای قوی» هستند؛ زیرا پیوندهای قوی معمولاً به همان شبکهٔ اطلاعاتیِ تکراری تعلق دارند، درحالی‌که پیوندهای ضعیف «پلی» بین خوشه‌های اجتماعیِ جدا از هم می‌سازند و اطلاعات تازه را منتقل می‌کنند.",
   "main_problem": "اطلاعات نو و فرصت‌ها چگونه در شبکه‌های اجتماعی پخش می‌شوند و چه نوع پیوندی (قوی یا ضعیف) در انتقال اطلاعات تازه نقش مؤثرتری ایفا می‌کند؟",
   "mechanism": "دوستان صمیمی (پیوندهای قوی) معمولاً خودشان نیز یکدیگر را می‌شناسند، بنابراین اطلاعات آن‌ها هم‌پوشانی (redundant) دارد. در مقابل، آشناهای دور (پیوندهای ضعیف) در دایره‌های اجتماعیِ متفاوتی قرار دارند و اطلاعاتی را می‌دانند که فرد در شبکهٔ نزدیک خود ندارد؛ به‌این‌رو پیوندهای ضعیف «پل‌های ساختاری» (structural bridges) هستند و در پخش اطلاعات تازه و نوآوری‌ها کارآمدترند.",
   "assumptions": ["اطلاعات از مسیر پیوندهای شبکهٔ اجتماعی جریان می‌یابد", "پیوندهای قوی هم‌پوشانی اطلاعاتی دارند", "پیوندهای ضعیف به خوشه‌های جدا از هم متصل‌اند"],
   "critiques": ["کاربرد آن در شبکه‌های اجتماعی دیجیتال (که حجم پیوندهای ضعیف بسیار بالاست) بحث‌برانگیز است", "برخی پژوهش‌ها نقش پیوندهای قوی در اعتماد و سرمایهٔ اجتماعی را برجسته می‌کنند", "مرز عملی «قوی» و «ضعیف» نسبی و وابسته به بافت است"],
   "applications": ["تحلیل پخش اطلاعات و شایعه در شبکه‌های اجتماعی دیجیتال", "تحلیل نوآوری و پخش ایده", "بازار کار و شبکه‌های حرفه‌ای"],
   "evolution": "از ۱۹۷۳ و بازبینی ۱۹۸۳ گرانووتر، به یکی از بنیان‌های نظریهٔ شبکهٔ اجتماعی و در سدهٔ ۲۱ به ابزار اصلی تحلیل شبکه‌های دیجیتال و ویروسی‌شدن محتوا تبدیل شده است.",
   "key_concepts": ["پیوند ضعیف (weak tie)", "پل ساختاری (structural bridge)", "هم‌پوشانی اطلاعاتی", "نوآوری"],
   "studies": ["گرانووتر (۱۹۷۳) مطالعهٔ یافتن شغل از طریق شبکهٔ اجتماعی"],
 },
 "MC-102": {
   "summary": "تعامل پاراسوشیال (Parasocial Interaction) به رابطهٔ یک‌سویه و «شبیه‌اجتماعی» گفته می‌شود که بین مخاطب رسانه و شخصیت رسانه‌ای (مجری، بازیگر، اینفلوئنسر) شکل می‌گیرد؛ مخاطب احساس صمیمیت و رابطه با شخصیت می‌کند، هرچند آن شخصیت از مخاطب آگاهی و پاسخ واقعی ندارد. این مفهوم نخستین‌بار توسط هورتون و ول (Horton & Wohl, 1956) برای توضیح «صمیمیت از راه دور» (intimacy at a distance) در رسانه‌های توده‌ای مطرح شد.",
   "main_problem": "چگونه مخاطبان با شخصیت‌های رسانه‌ای که ارتباط دوسویه و واقعی با آن‌ها ندارند، رابطه‌ای احساسی و صمیمی (شبیه رابطهٔ اجتماعی) برقرار می‌کنند؟",
   "mechanism": "تکرار و تداوم مواجهه با یک شخصیت رسانه‌ای، در ذهن مخاطب تصویری «شخصی» از او می‌سازد؛ مخاطب برپایهٔ این تصویر، احساسات و رفتارهایی شبیه تعامل با یک فرد واقعی از خود نشان می‌دهد (اعتماد، همراهی و گاه تکیهٔ عاطفی). این رابطه یک‌سویه است: مخاطب «می‌بیند» اما شخصیت رسانه‌ای به او به‌شکل اختصاصی پاسخ نمی‌دهد. در رسانه‌های اجتماعی، این فرایند با ویژگی‌های تعاملی (پاسخ به کامنت، صحبت مستقیم به دوربین) تقویت می‌شود.",
   "assumptions": ["مخاطبان از رسانه‌ها انتظار تعامل شخصی دارند", "تکرار مواجهه، تصویر شخصی از شخصیت می‌سازد", "این رابطه احساسی واقعی است، حتی اگر یک‌سویه باشد"],
   "critiques": ["ممکن است به‌جای پیوندهای اجتماعی واقعی، جایگزین آن‌ها شود (نقد اجتماعی)", "مرز بین «پاراسوشیال» و «همراهی» (companionship) گاه مبهم است", "در پلتفرم‌های تعاملی، یک‌سویه‌بودن آن تضعیف می‌شود"],
   "applications": ["مطالعات هویت اینفلوئنسر و صمیمیت دیجیتال", "تحلیل هویت مخاطب رسانه‌ها", "طراحی شخصیت‌های رسانه‌ای و برندها"],
   "evolution": "از ۱۹۵۶ هورتون و ول، به مطالعات تلویزیون و سینما و در سدهٔ ۲۱ به قلب مطالعات اینفلوئنسر-مارکتینگ و تعامل دیجیتال رسیده است.",
   "key_concepts": ["تعامل پاراسوشیال", "صمیمیت از راه دور", "شخصیت رسانه‌ای", "همراهی (companionship)"],
   "studies": ["هورتون و ول (۱۹۵۶)", "Rubin & Step (1975) مطالعات شخصی‌سازی رسانه"],
 },
 "MC-318": {
   "summary": "نظریهٔ وابستگی به سیستم رسانه‌ای (Media System Dependency) می‌گوید که اثر رسانه بر مخاطب تابعِ «وابستگی» مخاطب به رسانه برای دستیابی به اهداف خود در محیط اجتماعی است؛ یعنی هرچه فرد برای تحقق اهدافش (شناخت محیط، هماهنگی اجتماعی، قدرت) بیشتر به رسانه وابسته باشد و رسانه برای اهداف او ارزشمندتر و جایگزین‌پذیریِ کمتری داشته باشد، اثر آن قوی‌تر است.",
   "main_problem": "چرا و چگونه اثر رسانه بر برخی افراد و در برخی بافت‌ها قوی‌تر از بقیه است؟ (پاسخ: شدت وابستگی متقابلِ مخاطب و رسانه به اهداف)",
   "mechanism": "یک مثلث «جامعه ← رسانه ← مخاطب» شکل می‌گیرد. اثر رسانه زمانی زیاد می‌شود که: (۱) مخاطب برای دستیابی به اهدافش به رسانه وابسته باشد، (۲) خود رسانه آن اهداف را برای مخاطب باارزش کند، و (۳) منابع جایگزین برای دستیابی به همان اهداف کم باشد. بنابراین اثر تابعِ رابطهٔ متقابلِ وابستگی است، نه یک‌سویه.",
   "assumptions": ["مخاطبان اهدافی در محیط اجتماعی دارند", "رسانه یکی از منابع دستیابی به این اهداف است", "اثر تابع شدت وابستگی و کمبود جایگزین است"],
   "critiques": ["تعریف دقیق و سنجش «وابستگی» دشوار است", "بیشتر یک چارچوب توضیحی است تا الگویی با پیش‌بینی‌های دقیق آزمایش‌پذیر", "مرز آن با مدل‌های اثر مستقیم/غیرمستقیم گاه مبهم است"],
   "applications": ["تحلیل تفاوت اثر رسانه بر گروه‌های مختلف (به‌ویژه در بحران)", "مطالعات پذیرش و نفوذ رسانه در جوامع", "بافت‌های کم‌جایگزین (جوامع روستایی، بحران)"],
   "evolution": "از ۱۹۷۶ Ball-Rokeach و DeFleur تا «وابستگی به سیستم رسانه‌ای» (1995) که نقش رسانه را به‌عنوان سیستم و متغیر ساختاریِ جوامع برجسته‌تر کرد.",
   "key_concepts": ["وابستگی (dependency)", "مثلث رسانه-مخاطب-جامعه", "کمبود جایگزین", "ارزشمندی اهداف"],
   "studies": ["Ball-Rokeach & DeFleur (1976)", "Ball-Rokeach & Grunberg (1995)"],
 },
 "MC-317": {
   "summary": "الگوی «تأثیرات محدود» (Limited Effects) نتیجه‌ای است از مطالعات رأی‌دهی دههٔ ۱۹۴۰ — به‌ویژه «انتخاب مردم» (Lazarsfeld, Berelson & Gaudet, 1944) — که نشان داد رسانه‌های توده‌ای به‌سختی نگرش‌ها و رفتارهای بنیادین مردم را تغییر می‌دهند؛ به‌جای «تغییر رأی»، اثر آن‌ها عمدتا‌ا در «تقویت و تثبیت» نگرش‌های پیشین است. این الگو در مقابل الگوی «اثرات قوی/سوزنی» (hypodermic needle) قرار می‌گیرد.",
   "main_problem": "آیا رسانه‌های توده‌ای می‌توانند نگرش و رفتار مردم را به‌طور مستقیم و قوی تغییر دهند، یا اثر آن‌ها محدود و عمدتا‌ا تقویتی است؟",
   "mechanism": "در الگوی تأثیرات محدود، مخاطبان در شبکه‌های اجتماعی و تحت تأثیر رهبران افکار و گروه‌های مرجع قرار دارند؛ پیام رسانه‌ای به‌جای «دستور»، بیشتر «تقویت» یا «وحدت‌بخشی» به نگرش‌های موجود انجام می‌دهد. اثر مستقیم رسانه کم است و اثر واقعی آن عمدتا‌ا از طریق واسطه‌های اجتماعی (جریان دومرحله‌ای) و با توجه به نگرش پیشین مخاطب شکل می‌گیرد.",
   "assumptions": ["مخاطب در شبکه‌های اجتماعی و تحت تأثیر گروه‌های مرجع است", "نگرش‌های پیشین، مقاومت در برابر تغییر ایجاد می‌کنند", "اثر رسانه عمدتا‌ا تقویتی است"],
   "critiques": ["الگو بیش از حد «کم‌اثر» جلوه داد و نقش بافت‌های خاص (بحران، موضوعات تازه) را کم‌رنگ کرد", "بعدا‌ا با مفاهیمی چون دستورکار (agenda-setting) و آماده‌سازی ذهنی (priming) تکمیل شد و نشان داد رسانه «نحوهٔ قضاوت» را تغییر می‌دهد، نه لزوماً «محتوای رأی»"],
   "applications": ["مطالعات انتخاب و رأی‌دهی", "تحلیل مقاومت مخاطب در برابر تغییر نگرش", "زمینه‌سازی برای مدل‌های جدیدتر (دستورکار، پرایمینگ)"],
   "evolution": "از مطالعات ۱۹۴۴ تا بازنگری در دهه‌های بعد؛ در نهایت الگوی «تأثیرات محدود» به الگوهای ظریف‌تر اثر (دستورکار، پرایمینگ، چارچوب‌بندی) انجامید.",
   "key_concepts": ["تأثیرات محدود", "تقویت نگرش", "شبکهٔ اجتماعی", "جریان دومرحله‌ای"],
   "studies": ["«انتخاب مردم» (Lazarsfeld, Berelson & Gaudet, 1944) — مطالعهٔ Erie County, 1940"],
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
    return min(100, sum(detail.values())), detail

def main():
    c = pymysql.connect(host="127.0.0.1", user="root", password="433700", database=DB, charset="utf8mb4", autocommit=False)
    cur = c.cursor()
    codes = ["MC-251", "MC-102", "MC-318", "MC-317"]
    cur.execute("SELECT id, code, properties FROM kb_entities WHERE code IN (%s)" % ",".join(["%s"]*len(codes)), codes)
    rows = {code:(eid, json.loads(pr)) for (eid, code, pr) in cur.fetchall()}
    with open(BACKUP, "w", encoding="utf-8") as f:
        json.dump([{"code": cd, "props": rows[cd][1]} for cd in codes if cd in rows], f, ensure_ascii=False, indent=1)
    print("backup ->", len(rows), "rows")

    for code in codes:
        eid, p = rows[code]
        for k, v in ENRICH[code].items():
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
                    (eid, ver, json.dumps({"quality_score": score, "sources": n_sources, "verified": n_verified}, ensure_ascii=False),
                     "documented sourcing + rubric score", STAMP, NOW))
        cur.execute("INSERT INTO kb_audit_log (entity_code, action, detail, source) VALUES (%s,%s,%s,%s)",
                    (code, "DOC_ENRICH", json.dumps({"quality_score": score, "sources": n_sources, "verified": n_verified, "breakdown": detail}, ensure_ascii=False), STAMP))
        print(f"{code}: score={score} sources={n_sources} verified={n_verified} relations={n_relations} | {detail}")
    c.commit()
    c.close()
    print("BATCH4 THEORY DONE")

if __name__ == "__main__":
    main()
