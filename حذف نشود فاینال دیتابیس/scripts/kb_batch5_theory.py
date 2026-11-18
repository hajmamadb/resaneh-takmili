# -*- coding: utf-8 -*-
"""Batch 5 (THEORY): genuine content + web-verified sourcing for 4 theories.
Entities: MC-316 Opinion Leaders, MC-037 Long Tail, MC-027 Theory of Planned Behavior,
MC-253 Small-World Networks. Sources web-verified 2026-11-16. Target: resaname_kb_final_inspect."""
import pymysql, json

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch5-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch5_theory.json"

S = {
 "MC-316": [  # Opinion Leaders
   dict(kind="BOOK", title_en="Personal Influence: The Part Played by People in the Flow of Mass Communications",
        title_fa="تأثیر شخصی", authors="Katz, E., & Lazarsfeld, P. F.", year=1955,
        publisher="Bobbs-Merrill", isbn="9781412805070", doi=None, url=None, language="en",
        citation="Katz, E., & Lazarsfeld, P. F. (1955). Personal influence: The part played by people in the flow of mass communications. Bobbs-Merrill.",
        locator="whole work", locator_type="work", supports="definition / mechanism / origin", verified=True),
   dict(kind="BOOK", title_en="Voting: A Study of Opinion Formation in a Presidential Campaign",
        title_fa="رأی‌گیری: مطالعه‌ای در شکل‌گیری نگرش در یک کمپین ریاست‌جمهوری", authors="Berelson, B. R., Lazarsfeld, P. F., & McPhee, W. N.", year=1954,
        publisher="University of Chicago Press", isbn=None, doi=None, url=None, language="en",
        citation="Berelson, B. R., Lazarsfeld, P. F., & McPhee, W. N. (1954). Voting: A study of opinion formation in a presidential campaign. University of Chicago Press.",
        locator="whole work", locator_type="work", supports="studies / mechanism", verified=True),
 ],
 "MC-037": [  # Long Tail
   dict(kind="JOURNAL_ARTICLE", title_en="The Long Tail",
        title_fa="دم بلند", authors="Anderson, C.", year=2004,
        publisher="Wired, 12(10)", doi=None, url="https://www.wired.com/2004/10/tail/", language="en",
        citation="Anderson, C. (2004). The long tail. Wired, 12(10). https://www.wired.com/2004/10/tail/",
        locator="whole article", locator_type="work", supports="definition / mechanism / origin", verified=True),
   dict(kind="BOOK", title_en="The Long Tail: Why the Future of Business Is Selling Less of More",
        title_fa="دم بلند: چرا آیندهٔ کسب‌وکار، فروش کمتر از چیزهای بیشتر است", authors="Anderson, C.", year=2006,
        publisher="Hyperion", isbn=None, doi=None, url=None, language="en",
        citation="Anderson, C. (2006). The long tail: Why the future of business is selling less of more. Hyperion.",
        locator="whole work", locator_type="work", supports="applications / evolution / critiques", verified=True),
 ],
 "MC-027": [  # Theory of Planned Behavior
   dict(kind="JOURNAL_ARTICLE", title_en="The Theory of Planned Behavior",
        title_fa="نظریهٔ رفتار برنامه‌ریزی‌شده", authors="Ajzen, I.", year=1991,
        publisher="Organizational Behavior and Human Decision Processes, 50(2), 179-211", doi="10.1016/0749-5978(91)90020-T",
        url="https://doi.org/10.1016/0749-5978(91)90020-T", language="en",
        citation="Ajzen, I. (1991). The theory of planned behavior. Organizational Behavior and Human Decision Processes, 50(2), 179–211. https://doi.org/10.1016/0749-5978(91)90020-T",
        locator="pp. 179–211", locator_type="page_range", supports="definition / mechanism / assumptions", verified=True),
   dict(kind="BOOK", title_en="Belief, Attitude, Intention, and Behavior: An Introduction to Theory and Research",
        title_fa="باور، نگرش، نیت و رفتار", authors="Fishbein, M., & Ajzen, I.", year=1975,
        publisher="Addison-Wesley", isbn=None, doi=None, url=None, language="en",
        citation="Fishbein, M., & Ajzen, I. (1975). Belief, attitude, intention, and behavior: An introduction to theory and research. Addison-Wesley.",
        locator="whole work", locator_type="work", supports="origin / evolution", verified=False),
 ],
 "MC-253": [  # Small-World Networks
   dict(kind="JOURNAL_ARTICLE", title_en="Collective Dynamics of 'Small-World' Networks",
        title_fa="دینامیک گروهی شبکه‌های «جهان کوچک»", authors="Watts, D. J., & Strogatz, S. H.", year=1998,
        publisher="Nature, 393(6684), 440-442", doi="10.1038/30918",
        url="https://doi.org/10.1038/30918", language="en",
        citation="Watts, D. J., & Strogatz, S. H. (1998). Collective dynamics of 'small-world' networks. Nature, 393(6684), 440–442. https://doi.org/10.1038/30918",
        locator="pp. 440–442", locator_type="page_range", supports="definition / mechanism / model", verified=True),
   dict(kind="JOURNAL_ARTICLE", title_en="The Small World Problem",
        title_fa="مسئلهٔ جهان کوچک", authors="Milgram, S.", year=1967,
        publisher="Psychology Today, 2(1), 60-67", doi=None, url=None, language="en",
        citation="Milgram, S. (1967). The small world problem. Psychology Today, 2(1), 60–67.",
        locator="pp. 60–67", locator_type="page_range", supports="origin / studies", verified=False),
 ],
}

ENRICH = {
 "MC-316": {
   "summary": "«رهبران افکار» (opinion leaders) کسانی هستند که در حوزه‌ای خاص، به‌دلیل مصرف بیشتر و آگاهی بیشتر از رسانه، نقش واسطه بین رسانه و باقی افراد گروه را ایفا می‌کنند. آن‌ها پیام‌های رسانه‌ای را دریافت، پردازش و تفسیر کرده و از طریق تعاملات شخصی به اطرافیانشان می‌رسانند. این مفهوم هستهٔ نظریهٔ جریان دومرحله‌ای ارتباطات است و نخستین‌بار در مطالعات رأی‌دهی دههٔ ۱۹۴۰ به‌طور رسمی صورت‌بندی شد (Katz & Lazarsfeld, 1955).",
   "main_problem": "در فرایند اثرگذاری رسانه، چه کسانی نقش واسطه و تفسیرگر را دارند و چگونه پیام رسانه‌ای از طریق آن‌ها به بقیهٔ جمعیت می‌رسد؟",
   "mechanism": "رهبران افکار مصرف‌کننده‌های فعال‌تر و پراستفاده‌تر از رسانه در حوزه‌ای خاص هستند. آن‌ها اطلاعات را از رسانه می‌گیرند، برپایهٔ دانش و جایگاه اجتماعی خود تفسیر می‌کنند و در تعاملات روزمرهٔ شخصی به اطرافیان منتقل می‌کنند. چون ارتباط شخصی اعتبار اجتماعی بیشتری از رسانه دارد، اثر واقعی رسانه عمدتا‌ا از همین واسطه‌ها تحقق می‌یابد.",
   "assumptions": ["برخی افراد در حوزه‌های خاص، مصرف و آگاهی بیشتری از رسانه دارند", "آن‌ها مورد اعتماد اطرافیان هستند", "ارتباط شخصی اثر قوی‌تری از رسانه بر نگرش دارد"],
   "critiques": ["رهبری افکار «نقشی» است نه «ویژگی شخصیتی»؛ فردی ممکن است در حوزه‌ای رهبر افکار باشد و در حوزهٔ دیگر نباشد", "تعمیم‌پذیری بیشتر در بافت رأی‌دهی آزمون شده", "در شبکه‌های اجتماعی، مرز بین رهبر افکار و رسانهٔ پخش کمرنگ شده است"],
   "applications": ["طراحی کمپین‌های تبلیغاتی مبتنی بر اینفلوئنسرها", "مطالعات پخش اطلاعات و شایعه", "تحلیل نفوذ رسانه در بافت‌های اجتماعی"],
   "evolution": "از مطالعات Erie County و Decatur در دهه‌های ۱۹۴۰–۱۹۵۰ تا گسترش به مفهوم «اینفلوئنسر» در شبکه‌های اجتماعی دیجیتال.",
   "key_concepts": ["رهبر افکار (opinion leader)", "تفسیر پیام", "جریان دومرحله‌ای", "شبکهٔ شخصی"],
   "studies": ["Katz & Lazarsfeld (1955) مطالعهٔ Decatur", "Berelson, Lazarsfeld & McPhee (1954) Voting"],
 },
 "MC-037": {
   "summary": "مفهوم «دم بلند» (Long Tail) که توسط کریس اندرسن (Anderson, 2004; 2006) مطرح شد، می‌گوید در اقتصاد دیجیتال و بازارهای آنلاین، ارزش کلان بازار نه فقط از «چند محصول پرفروش» (حلقهٔ نمودار) بلکه از تجمیع «بسیار محصول‌های کم‌فروش» در انتهای توزیع (دم) به‌دست می‌آید. با کاهش هزینهٔ ذخیره‌سازی، توزیع و جستجو در بسترهای دیجیتال، کالاهای «محبوب اما کم‌فروش» می‌توانند در کنار «مگاتوف‌های» پرفروش، سهم قابل‌توجهی از بازار ایجاد کنند.",
   "main_problem": "آیا ارزش بازار دیجیتال بیشتر از «چند موفق بزرگ» یا از «تجمیع هزاران موفق کوچک» به‌دست می‌آید؟",
   "mechanism": "در بازارهای فیزیکی، قفسهٔ محدود و هزینهٔ توزیع، فقط محصولات پرفروش را مقبول می‌کند. در بستر دیجیتال (نیمفا، کتاب‌فروشی آنلاین، استریمینگ) هزینهٔ ذخیره‌سازی و توزیع به‌شدت پایین می‌آید؛ همزمان ابزارهای «یافتن» (الگوریتم‌های پیشنهاد، جستجو) به مخاطب امکان می‌دهند کالاهای نادر را بیابند و ابزارهای «تولید» ارزان‌تر، به تولیدکنندگان امکان ساخت کالاهای تخصصی می‌دهند. نتیجه: تجمیع فروش از «دم» (کالاهای کم‌فروش اما بسیار متنوع) می‌تواند با فروش از «حلقه» (مگاتوف‌ها) رقابت کند.",
   "assumptions": ["هزینهٔ توزیع/ذخیره در بستر دیجیتال به‌شدت پایین است", "ابزارهای یافتن و تولید ارزان‌شده‌اند", "تقاضا برای تنوع وجود دارد"],
   "critiques": ["در بسیاری از بازارها، «حلقه» (موفقیت‌های بزرگ) همچنان بخش غالب سهم را دارد", "الگوریتم‌های پیشنهادگاهی خود باعث تمرکز بر چند محصول برتر می‌شوند (head concentration)", "الگوی دم بلند در بازارهایی با نیاز اجتماعی قوی (مثل موسیقی پاپ) کمتر صدق می‌کند"],
   "applications": ["استراتژی‌های بازاریابی دیجیتال و e-commerce", "برنامه‌ریزی محتوای استریمینگ و پلتفرم‌های دیجیتال", "تحلیل تنوع فرهنگی و اقتصادی"],
   "evolution": "از مقالهٔ Wired (2004) تا کتاب (2006) و کاربرد گسترده در اقتصاد دیجیتال و اقتصاد پلتفرم‌ها.",
   "key_concepts": ["دم بلند (long tail)", "حلقه (head)", "تنوع", "هزینهٔ تراز/دسترسی"],
   "studies": ["Anderson (2004) مقالهٔ Wired", "Anderson (2006) کتاب"],
 },
 "MC-027": {
   "summary": "نظریهٔ رفتار برنامه‌ریزی‌شده (Theory of Planned Behavior — TPB) مدل شناختی-رفتاری Icek Ajzen (1991) است که برپایهٔ نظریهٔ عمل (Fishbein & Ajzen, 1975) و با افزودن متغیر «کنترل رفتار ادراک‌شده» (perceived behavioral control) توسعه یافته است. در این نظریه، «نیت» (intention) پیش‌بینی‌کنندهٔ اصلی رفتار است و خود نیت از سه ریشه شکل می‌گیرد: نگرش نسبت به رفتار، هنجارهای ذهنی، و کنترل رفتار ادراک‌شده.",
   "main_problem": "چگونه می‌توان پیش‌بینی کرد که فرد یک رفتار مشخص را انجام خواهد داد و چه عوامل شناختی، این رفتار را به‌دنبال می‌آورند؟",
   "mechanism": "رفتار از طریق «نیت» به‌دنبال می‌آید. نیت از سه عامل شکل می‌گیرد: (۱) نگرش نسبت به رفتار (ارزش قضاوت فرد نسبت به پیامدهای آن)، (۲) هنجارهای ذهنی (فشار درونی‌شده از گروه‌های مرجع)، و (۳) کنترل رفتار ادراک‌شده (اعتقاد فرد به آسانی/سختی انجام آن رفتار برپایهٔ منابع و موانع). وقتی کنترل ادراک‌شده قوی باشد، خود آن عامل (علاوه بر نیت) رفتار را پیش‌بینی می‌کند.",
   "assumptions": ["رفتار از نیت به‌دنبال می‌آید", "نگرش، هنجار و کنترل ادراک‌شده، نیت را تعیین می‌کنند", "افراد به‌طور نسبی منطقی و عقلانی رفتار می‌کنند"],
   "critiques": ["رابطهٔ «نیت→رفتار» در بسیاری از بافت‌های رفتاری (به‌ویژه رفتارهای خودکار و عادت‌محور) ضعیف است", "مدل «کنترل واقعی» (منابع، مهارت، موانع) را مستقیما‌ا نمی‌سنجد", "کاربرد آن بیشتر در پژوهش‌های آزمایشگاهی و بافت‌های «تصمیم‌محور» است"],
   "applications": ["پیش‌بینی رفتار مصرفی و سلامت", "طراحی مداخلات آموزشی و تغییر نگرش", "پژوهش رفتارهای محیط‌زیستی و دیجیتال"],
   "evolution": "از نظریهٔ عمل (1975) تا TPB (Ajzen, 1991) و کاربرد گسترده در روان‌شناسی سلامت، بازاریابی و علوم ارتباطات.",
   "key_concepts": ["نیت (intention)", "نگرش", "هنجار ذهنی", "کنترل رفتار ادراک‌شده"],
   "studies": ["Ajzen (1991) — مطالعات چندگانه در سلامت و رفتار مصرفی"],
 },
 "MC-253": {
   "summary": "مفهوم «جهان کوچک» (Small World) می‌گوید در شبکه‌های اجتماعی، هر دو فرد دلخواه در جهان، با احتمال بالا، در تعداد محدودی گام (معمولا‌ا «شش درجهٔ تفکیک» — six degrees of separation) از هم فاصله دارند. این پدیده نخست توسط Stanley Milgram (1967) در آزمایش‌های کلاسیک آزمایش شد و بعدا‌ا با مدل Watts–Strogatz (1998) توضیح داده شد: شبکه‌های جهان کوچک، هم‌زمان «همسایگی محلی» (clustering بالا) و «مسیرهای کوتاه میان‌مدت» (short path length) را دارند.",
   "main_problem": "چگونه می‌شود در شبکه‌ای با میلیاردها گره و تنها چند اتصال برای هر گره، میانگین فاصله بین دو گره تصادفی بسیار کوتاه باشد؟",
   "mechanism": "در شبکهٔ منظم (regular) هر گره فقط به همسایه‌های نزدیک متصل است؛ فاصله‌ها بلندند اما clustering بالاست. در شبکهٔ کاملاً تصادفی، فاصله‌ها کوتاهند اما clustering پایین است. مدل Watts–Strogatz با «بازسیم‌کشی» (rewiring) تصادفی بخشی از پیوندهای شبکهٔ منظم، هم‌زمان clustering بالا و path length پایین را به‌دست می‌آورد — ویژگی تعریفی شبکهٔ «جهان کوچک».",
   "assumptions": ["شبکه از گره‌ها و پیوندها تشکیل شده", "هر گره چند اتصال دارد", "حتی تغییرات کوچک در اتصال‌ها، مسیرهای کوتاه ایجاد می‌کنند"],
   "critiques": ["مدل Watts–Strogatz همگن است (بدون درجهٔ ناهمگن)", "در شبکه‌های واقعی، توزیع درجهٔ «بی‌مقیاس» (power-law) نقش کلیدی دارد (Barabási–Albert, 1999)", "مفهوم «شش درجه» یک میانگین توصیفی است نه قانون دقیق"],
   "applications": ["تحلیل شبکه‌های اجتماعی دیجیتال", "مطالعهٔ پخش اطلاعات، ویروسی‌شدن و ابتلا (epidemic) در شبکه‌ها", "مهندسی شبکهٔ ابرتر و شبکه‌های فیزیکی"],
   "evolution": "از آزمایش Milgram (1967) تا مدل Watts–Strogatz (1998) و تکمیل با مدل‌های بی‌مقیاس (Barabási–Albert, 1999).",
   "key_concepts": ["جهان کوچک (small world)", "شش درجهٔ تفکیک", "clustering", "path length", "بازسیم‌کشی (rewiring)"],
   "studies": ["Milgram (1967) Small World Problem", "Watts & Strogatz (1998)"],
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
    codes = ["MC-316", "MC-037", "MC-027", "MC-253"]
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
    print("BATCH5 THEORY DONE")

if __name__ == "__main__":
    main()
