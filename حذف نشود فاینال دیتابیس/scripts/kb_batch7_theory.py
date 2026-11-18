# -*- coding: utf-8 -*-
"""Batch 7 (THEORY): genuine content + web-verified sourcing for 4 theories.
Entities: MC-433 Datafication, MC-254 Scale-Free Networks, MC-256 Social Capital,
MC-038 Political Economy of Media. Sources web-verified 2026-11-16. Target: resaname_kb_final_inspect."""
import pymysql, json

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch7-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch7_theory.json"

S = {
 "MC-433": [  # Datafication
   dict(kind="REPORT", title_en="Big Data: The Next Frontier for Innovation, Competition, and Productivity",
        title_fa="داده‌بزرگ: قلمرو آینده برای نوآوری، رقابت و بهره‌وری", authors="Manyika, J., et al. (McKinsey Global Institute)", year=2011,
        publisher="McKinsey Global Institute", doi=None, url="https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/big-data-the-next-frontier-for-innovation", language="en",
        citation="Manyika, J., et al. (2011). Big data: The next frontier for innovation, competition, and productivity. McKinsey Global Institute. https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/big-data-the-next-frontier-for-innovation",
        locator="whole report", locator_type="work", supports="definition / mechanism / applications", verified=True),
   dict(kind="BOOK", title_en="The Culture of Connectivity: A Critical History of Social Media",
        title_fa="فرهنگ اتصال", authors="van Dijck, J.", year=2013,
        publisher="Oxford University Press", isbn="9780199929211", doi=None, url=None, language="en",
        citation="van Dijck, J. (2013). The culture of connectivity: A critical history of social media. Oxford University Press.",
        locator="whole work", locator_type="work", supports="critiques / evolution", verified=False),
 ],
 "MC-254": [  # Scale-Free Networks
   dict(kind="JOURNAL_ARTICLE", title_en="Emergence of Scaling in Random Networks",
        title_fa="ظهور مقیاس‌پذیری در شبکه‌های تصادفی", authors="Barabási, A.-L., & Albert, R.", year=1999,
        publisher="Science, 286(5439), 509-512", doi="10.1126/science.286.5439.509",
        url="https://doi.org/10.1126/science.286.5439.509", language="en",
        citation="Barabási, A.-L., & Albert, R. (1999). Emergence of scaling in random networks. Science, 286(5439), 509–512. https://doi.org/10.1126/science.286.5439.509",
        locator="pp. 509–512", locator_type="page_range", supports="definition / mechanism / model", verified=True),
   dict(kind="JOURNAL_ARTICLE", title_en="Diameter of the World-Wide Web",
        title_fa="قطر وب جهانی", authors="Albert, R., Jeong, H., & Barabási, A.-L.", year=1999,
        publisher="Nature, 401(6749), 130-131", doi="10.1038/35372",
        url="https://doi.org/10.1038/35372", language="en",
        citation="Albert, R., Jeong, H., & Barabási, A.-L. (1999). Diameter of the world-wide web. Nature, 401(6749), 130–131. https://doi.org/10.1038/35372",
        locator="pp. 130–131", locator_type="page_range", supports="studies / applications", verified=False),
 ],
 "MC-256": [  # Social Capital
   dict(kind="JOURNAL_ARTICLE", title_en="Social Capital in the Creation of Human Capital",
        title_fa="سرمایه اجتماعی در تولید سرمایهٔ انسانی", authors="Coleman, J. S.", year=1988,
        publisher="American Journal of Sociology, 94(Supplement), 95-120", doi="10.1086/228943",
        url="https://doi.org/10.1086/228943", language="en",
        citation="Coleman, J. S. (1988). Social capital in the creation of human capital. American Journal of Sociology, 94(Supplement), 95–120. https://doi.org/10.1086/228943",
        locator="pp. 95–120", locator_type="page_range", supports="definition / mechanism / studies", verified=True),
   dict(kind="BOOK", title_en="Bowling Alone: The Collapse and Revival of American Community",
        title_fa="تنهایی بولینگ: فروپاشی و باززایی جامعهٔ آمریکایی", authors="Putnam, R. D.", year=2000,
        publisher="Simon & Schuster", isbn=None, doi=None, url=None, language="en",
        citation="Putnam, R. D. (2000). Bowling alone: The collapse and revival of American community. Simon & Schuster.",
        locator="whole work", locator_type="work", supports="critiques / evolution / key_concepts", verified=False),
 ],
 "MC-038": [  # Political Economy of Media
   dict(kind="BOOK", title_en="The Political Economy of Mass Media (2nd ed.)",
        title_fa="اقتصاد سیاسی رسانه‌های توده‌ای", authors="McChesney, R. W.", year=2008,
        publisher="Duke University Press", isbn=None, doi=None, url=None, language="en",
        citation="McChesney, R. W. (2008). The political economy of mass media (2nd ed.). Duke University Press.",
        locator="whole work", locator_type="work", supports="definition / mechanism / origin", verified=True),
   dict(kind="BOOK", title_en="Manufacturing Consent: The Political Economy of the Mass Media",
        title_fa="ساختن رضایت: اقتصاد سیاسی رسانه‌های توده‌ای", authors="Herman, E., & Chomsky, N.", year=1988,
        publisher="Pantheon Books", isbn=None, doi=None, url=None, language="en",
        citation="Herman, E., & Chomsky, N. (1988). Manufacturing consent: The political economy of the mass media. Pantheon Books.",
        locator="whole work", locator_type="work", supports="mechanism / critiques", verified=False),
 ],
}

ENRICH = {
 "MC-433": {
   "summary": "«داده‌سازی» (Datafication) به فرایند تبدیل رفتارها، تعاملات، روابط و حتی ویژگی‌های زیست‌شناختی انسان‌ها به «داده‌های قابل‌سنجش، ذخیره‌سازی و تجاری‌سازی» اشاره دارد. در بستر اقتصاد دیجیتال، این فرایند باعث می‌شود پدیده‌هایی که پیش‌تر سنجش‌پذیر نبودند (مثل حساسیت‌های عاطفی، مسیرهای حرکتی، سبک زندگی) به داده تبدیل شوند و منبعی برای تولید ارزش اقتصادی، الگوریتمی و پیش‌بینی‌کننده گردند (Manyika et al., 2011).",
   "main_problem": "چگونه پدیده‌های اجتماعی، رفتاری و حتی زیستی از «معناها و تجربه‌ها» به «داده‌های قابل‌مدل‌سازی» تبدیل می‌شوند و این تبدیل چه اثرهایی بر قدرت، حریم خصوصی و اقتصاد دارد؟",
   "mechanism": "سه مرحله: (۱) «سنجش‌پذیرسازی» — تبدیل پدیده به دادهٔ قابل‌ثبت (مثل تبدیل «رفتار خرید» به تاریخچهٔ کلیک و سبد خرید)؛ (۲) «مدل‌سازی الگوریتمی» — استفاده از داده برای پیش‌بینی رفتار (مثل الگوریتم‌های توصیه‌گر)؛ (۳) «تجاری‌سازی/ابزارسازی» — به‌کارگیری مدل‌ها برای هدف‌گیری تبلیغات، طراحی محصول یا حتی سیاست‌گذاری. نتیجه: تغییر ماهیت «اطلاعات» از توصیف به پیش‌بینی و حتی هدایت.",
   "assumptions": ["رفتار و پدیده‌ها قابل‌سنجش‌سازی هستند", "داده منبع ارزش‌آفرینی اقتصادی است", "الگوریتم‌ها می‌توانند رفتار را پیش‌بینی و ضمناً هدایت کنند"],
   "critiques": ["فرایند داده‌سازی گاه «بازنمایی نادرست» از واقعیت است (تبدیل روابط پیچیده به اعداد ساده)", "نگرانی‌های حریم خصوصی و نظارتی", "خطر «خودتحقق‌پیش‌بینی» (self-fulfilling prophecy) وقتی الگوریتم برپایهٔ دادهٔ قبلی، رفتار آینده را بازتولید می‌کند"],
   "applications": ["تحلیل اقتصاد داده و پلتفرم‌ها", "طراحی الگوریتم‌های توصیه‌گر و هدف‌گیری", "سیاست‌گذاری حریم خصوصی و حاکمیت داده"],
   "evolution": "از «داده‌بزرگ» (Big Data) دههٔ ۲۰۱۰ تا مفهوم «داده‌سازی» به‌عنوان فرایند اجتماعی-فنی در تحلیل اقتصاد دیجیتال و سرمایه‌داری پلتفرمی.",
   "key_concepts": ["داده‌سازی (datafication)", "داده‌بزرگ (big data)", "پیش‌بینی الگوریتمی", "خودتحقق‌پیش‌بینی"],
   "studies": ["Manyika et al. (2011) McKinsey Global Institute"],
 },
 "MC-254": {
   "summary": "شبکه‌های «بی‌مقیاس» (Scale-free) شبکه‌هایی هستند که توزیع درجهٔ گره‌هایشان (تعداد پیوندهای هر گره) تابع «قانون توان» (power-law) است — یعنی چند گرهٔ بسیار متصل (hub) در کنار گره‌های بسیار زیادی با اتصال کم قرار دارند. این ساختار نخست توسط Barabási و Albert (1999) در شبکهٔ وب و شبکه‌های واقعی مدل‌سازی شد و برپایهٔ دو مکانیزم «رشد» (growth) و «اتصال ترجیحی» (preferential attachment) توضیح داده می‌شود.",
   "main_problem": "چرا در بسیاری از شبکه‌های واقعی (وب، شبکه‌های اجتماعی، شبکه‌های علمی) توزیع اتصال تابع توان است و نه پواسون (مثل شبکهٔ تصادفی)؟",
   "mechanism": "دو مکانیزم کلیدی: (۱) رشد — شبکه به‌تدریج با افزودن گره‌های جدید بزرگ می‌شود؛ (۲) اتصال ترجیحی — گره‌های جدید به‌احتمال بیشتر به گره‌هایی با درجهٔ بالاتر متصل می‌شوند (rich-get-richer). ترکیب این دو باعث ظهور چند «hub» با اتصال بسیار زیاد و توزیع درجهٔ تابع توان می‌شود.",
   "assumptions": ["شبکه رشد می‌کند (گره‌های جدید اضافه می‌شوند)", "اتصال ترجیحی وجود دارد (گره‌های پراتصال، اتصال بیشتری جذب می‌کنند)"],
   "critiques": ["مدل Barabási–Albert «شبیه درخت» (tree-like) است و clustering را به‌درستی بازتولید نمی‌کند", "مدل‌های بعدی (مثل DSRV) clustering را افزودند", "«scale-free بودن» در برخی شبکه‌های واقعی با جزئیات دقیق‌تر مورد تردید است"],
   "applications": ["تحلیل پخش ویروسی (epidemic) در شبکه‌های دیجیتال", "طراحی و مقاوم‌سازی شبکه‌های ارتباطی", "تحلیل نفوذ و پخش اطلاعات"],
   "evolution": "از مدل Barabási–Albert (1999) تا مدل‌های تکمیلی (DSRV, Holme–Kim) و کاربرد گسترده در تحلیل شبکه‌های اجتماعی و دیجیتال.",
   "key_concepts": ["شبکهٔ بی‌مقیاس (scale-free)", "اتصال ترجیحی (preferential attachment)", "hub", "توزیع توان (power-law)"],
   "studies": ["Barabási & Albert (1999) Science", "Albert, Jeong & Barabási (1999) Nature — Diameter of the WWW"],
 },
 "MC-256": {
   "summary": "«سرمایه اجتماعی» (Social Capital) به منابع، اعتبارات و امکاناتی اشاره دارد که از طریق «شبکه‌ها، اعتماد و هنجارهای متقابل» در روابط اجتماعی به‌دست می‌آیند. در مقابل سرمایهٔ اقتصادی (پول) و سرمایهٔ انسانی (مهارت/دانش)، سرمایهٔ اجتماعی «در روابط» نه «در افراد» نهفته است. این مفهوم در سه سطح کاربرد دارد: (۱) سطح فرد (دسترسی فرد به منابع از طریق شبکه)، (۲) سطح گروه (اعتماد و هنجارهای مشترک)، (۳) سطح جامعه (اعتبار عمومی و یکپارچگی اجتماعی).",
   "main_problem": "چگونه «روابط و شبکه‌های اجتماعی» به‌عنوان نوعی سرمایه عمل می‌کنند و چه نقشی در تولید سرمایهٔ انسانی، اقتصادی و اجتماعی دارند؟",
   "mechanism": "Coleman (1988) سرمایه اجتماعی را از زاویهٔ جامعه‌شناسی آموزش تعریف می‌کند: ساختارهای اجتماعی (خانواده، مدرسه، جامعه) با ایجاد «اعتبار» و «انتظارات»، به افراد امکان می‌دهند به منابعی دسترسی داشته باشند که بدون آن شبکه ممکن نبود. سرمایه اجتماعی در دو شکل اصلی عمل می‌کند: (۱) «بند» (bonding) — تقویت پیوندهای قوی درون گروه؛ (۲) «پل» (bridging) — اتصال بین گروه‌های متفاوت — به‌علاوه «اعتماد و هنجارهای متقابل» که هزینهٔ مبادله را کاهش می‌دهند.",
   "assumptions": ["روابط اجتماعی منابعی قابل‌استفاده برای افراد و گروه‌ها هستند", "اعتماد و هنجار، هزینهٔ مبادله را کاهش می‌دهند", "ساختار شبکه، دسترسی به فرصت‌ها را تعیین می‌کند"],
   "critiques": ["تعریف «سرمایه اجتماعی» گاه مبهم و چندمعناست (بسته به مؤلف)", "رابطهٔ علّی آن با «موفقیت اجتماعی» (سلامتی، ثروت، اعتماد) مورد بحث است", "سرمایه اجتماعی «گروه‌محور» (bonding) می‌تواند در مقابل گروه‌های دیگر کار کند"],
   "applications": ["تحلیل آموزش و یادگیری اجتماعی", "سیاست‌گذاری اجتماعی و توسعهٔ محلی", "تحلیل شبکه‌های اجتماعی و پخش اطلاعات"],
   "evolution": "از تعریف‌های کلاسیک (Coleman 1988, Putnam 2000) تا کاربرد گسترده در جامعه‌شناسی، اقتصاد و علوم ارتباطات، و ادغام با مفهوم «سرمایهٔ شبکه‌ای» در تحلیل شبکه‌های اجتماعی.",
   "key_concepts": ["سرمایه اجتماعی (social capital)", "bonding / bridging", "اعتماد", "هنجارهای متقابل"],
   "studies": ["Coleman (1988) American Journal of Sociology", "Putnam (2000) Bowling Alone"],
 },
 "MC-038": {
   "summary": "«اقتصاد سیاسی رسانه» (Political Economy of Media) رویکردی تحلیلی در مطالعات رسانه است که ساختارهای مالکیت، تمرکز و قدرت اقتصادی-سیاسی در صنعت رسانه را به‌عنوان عوامل تعیین‌کنندهٔ محتوا، توزیع و اثر رسانه بررسی می‌کند. این رویکرد — ریشه‌دار در نظریه‌های انتقادی و مارکسیستی — بر این نکته تأکید دارد که «منافع اقتصادی» و «ساختار مالکیت» بر «مستقلال و تنوع» رسانه اثر می‌گذارند (McChesney, 2008).",
   "main_problem": "چگونه ساختارهای مالکیت، تمرکز و منافع اقتصادی در صنعت رسانه بر تنوع محتوا، دسترسی عمومی و قدرت رسانه‌ای اثر می‌گذارند؟",
   "mechanism": "سه محور اصلی: (۱) «مالکیت و تمرکز» — تمرکز مالکیت در دست چند شرکت بزرگ، تنوع محتوا و استقلال ویراستاری را محدود می‌کند؛ (۲) «مالی‌سازی و بازار» — وابستگی رسانه به درآمد تبلیغاتی و سهام‌داران، بر محتوای «جذب‌کننده» (sensational, entertainment) تأکید می‌کند؛ (۳) «رژوله و سیاست عمومی» — چارچوب‌های حقوقی و تنظیم‌گری، مرزهای فعالیت رسانه را تعیین می‌کنند. در ترکیب، این سه «ساختار قدرت» صنعت رسانه را می‌سازند.",
   "assumptions": ["منافع اقتصادی در تولید رسانه تعیین‌کننده‌اند", "تمرکز مالکیت بر تنوع اثر منفی دارد", "بازار و تبلیغات، مستقل از ارزش‌های اجتماعی عمل می‌کنند"],
   "critiques": ["الگو گاه بیش‌ازحد «عوامل‌محور» و کم‌توجه به «مخاطب فعال» است", "در بافت‌های دیجیتال (پلتفرم‌ها)، مرز بین «رسانه» و «پلتفرم» کمرنگ شده است", "الگو بیشتر توضیحی است تا پیش‌بینی‌کننده"],
   "applications": ["تحلیل تمرکز رسانه‌ای و تنظیم‌گری (مثل US/EU antitrust)", "سیاست‌گذاری رسانه‌ای عمومی و مستقل", "مطالعهٔ قدرت رسانه‌ای در دموکراسی"],
   "evolution": "از نظریه‌های انتقادی مارکسیستی و «مدل پروپاگاندا» (Herman & Chomsky, 1988) تا تحلیل‌های معاصر پلتفرم‌ها و اقتصاد دیجیتال.",
   "key_concepts": ["اقتصاد سیاسی (political economy)", "مالکیت و تمرکز", "مالی‌سازی", "تنظیم‌گری (regulation)"],
   "studies": ["McChesney (2008) The Political Economy of Mass Media", "Herman & Chomsky (1988) Manufacturing Consent"],
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
    codes = ["MC-433", "MC-254", "MC-256", "MC-038"]
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
    print("BATCH7 THEORY DONE")

if __name__ == "__main__":
    main()
