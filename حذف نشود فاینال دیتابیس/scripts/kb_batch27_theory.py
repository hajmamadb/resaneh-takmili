# -*- coding: utf-8 -*-
"""Batch 27 (THEORY): MC-076 Actor-Network Theory (Latour 1987), MC-084 The Culture Industry
(Adorno & Horkheimer 1944), MC-075 Semiotics (Saussure 1916), MC-074 Critical Discourse Analysis
(Fairclough 1992). Sources web-verified 2026-11-16. Target: resaname_kb_final_inspect."""
import pymysql, json

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch27-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch27_theory.json"

S = {
 "MC-076": [  # Actor-Network Theory
   dict(kind="BOOK", title_en="Science in Action: How to Follow Scientists and Engineers through Society",
        title_fa="علم در عمل: چگونه دانشمندان و مهندسان را در جامعه دنبال کنیم", authors="Latour, B.", year=1987,
        publisher="Harvard University Press", doi=None, url=None, language="en", isbn=None,
        citation="Latour, B. (1987). Science in action: How to follow scientists and engineers through society. Harvard University Press.",
        locator="whole work", locator_type="work", supports="definition / mechanism / origin", verified=True),
   dict(kind="BOOK", title_en="Reassembling the Social: An Introduction to Actor-Network-Theory",
        title_fa="دوباره‌آرایی اجتماعی: مقدمه‌ای بر نظریهٔ کنشگر-شبکه", authors="Latour, B.", year=2005,
        publisher="Oxford University Press", doi=None, url=None, language="en", isbn=None,
        citation="Latour, B. (2005). Reassembling the social: An introduction to actor-network-theory. Oxford University Press.",
        locator="whole work", locator_type="work", supports="evolution / critiques", verified=False),
 ],
 "MC-084": [  # The Culture Industry
   dict(kind="JOURNAL_ARTICLE", title_en="The culture industry: Enlightenment as mass deception (chapter in Dialectic of Enlightenment)",
        title_fa="صنعت فرهنگ: روشن‌فکری به‌مثابهٔ فریب انبوه (فصل در دیالکتیک روشن‌فکری)", authors="Adorno, T. W., & Horkheimer, M.", year=1944,
        publisher="In Dialectic of Enlightenment (English trans. J. M. Bernstein, 1979, Verso)", doi=None, url=None, language="en",
        citation="Adorno, T. W., & Horkheimer, M. (1944). The culture industry: Enlightenment as mass deception. In Dialectic of the enlightenment.",
        locator="whole chapter", locator_type="CHAPTER", supports="definition / mechanism / origin", verified=True),
   dict(kind="BOOK", title_en="The Culture Industry: Selected Essays on Mass Culture",
        title_fa="صنعت فرهنگ: مقالات برگزیده دربارۀ فرهنگ انبوه", authors="Adorno, T. W.", year=1991,
        publisher="Routledge", doi=None, url=None, language="en", isbn=None,
        citation="Adorno, T. W. (1991). The culture industry: Selected essays on mass culture. Routledge.",
        locator="whole work", locator_type="work", supports="evolution / critiques", verified=False),
 ],
 "MC-075": [  # Semiotics
   dict(kind="BOOK", title_en="Course in General Linguistics (Cours de linguistique generale)",
        title_fa="دورهٔ عمومی زبان‌شناسی", authors="Saussure, F. de", year=1916,
        publisher="First published 1916 (posthumous; English trans. 1959, Washington Square Press)", doi=None, url=None, language="en",
        citation="Saussure, F. de (1916). Course in general linguistics.",
        locator="whole work", locator_type="work", supports="definition / mechanism / origin", verified=True),
   dict(kind="JOURNAL_ARTICLE", title_en="The rhetoric of the image (in Image-Music-Text)",
        title_fa="رتوریک تصویر", authors="Barthes, R.", year=1967,
        publisher="In Image-Music-Text (English trans. 1977, Hill and Wang)", doi=None, url=None, language="en",
        citation="Barthes, R. (1967). The rhetoric of the image. In Image-music-text.",
        locator="whole essay", locator_type="CHAPTER", supports="evolution / critiques", verified=False),
 ],
 "MC-074": [  # Critical Discourse Analysis
   dict(kind="BOOK", title_en="Discourse and Social Change",
        title_fa="گفتمان و تحول اجتماعی", authors="Fairclough, N.", year=1992,
        publisher="Cambridge: Polity Press", doi=None, url=None, language="en", isbn=None,
        citation="Fairclough, N. (1992). Discourse and social change. Polity Press.",
        locator="whole work", locator_type="work", supports="definition / mechanism / origin", verified=True),
   dict(kind="BOOK", title_en="Analysing Discourse: Textual Analysis for Social Research",
        title_fa="تحلیل گفتمان: تحلیل متنی برای پژوهش اجتماعی", authors="Fairclough, N.", year=2003,
        publisher="Routledge", doi=None, url=None, language="en", isbn=None,
        citation="Fairclough, N. (2003). Analysing discourse: Textual analysis for social research. Routledge.",
        locator="whole work", locator_type="work", supports="evolution / critiques", verified=False),
 ],
}

ENRICH = {
 "MC-076": {
   "summary": "«نظریهٔ کنشگر-شبکه» (Actor-Network Theory) که توسط Bruno Latour در کتاب «Science in Action» (1987) صورت‌بندی شد، به تحلیل «شبکه‌های کنشگری» (actor-networks) می‌پردازد که از «ارتباطات» (relations) «اجزای انسانی و غیرانسانی» (human and non-human actors) تشکیل می‌شوند. Latour بر این ایده استوار است که «اجتماع» (society) از «شبکه‌هایی» (networks) از «کنشگران» (actors) (شامل «افراد» (humans) و «اجسام/تکنولوژی‌ها» (objects/technologies)) «شکل می‌گیرد» (is constituted) که از طریق «بازنمایی‌ها» (mediations) و «ترجمه‌ها» (translations) «متنوع» (diverse) می‌شوند (Latour, 1987).",
   "main_problem": "«اجتماع» (society) چگونه از «شبکه‌ها» (networks) «کنشگران» (actors) انسانی و غیرانسانی «شکل می‌گیرد» (constituted) می‌شود و «اجسام» (objects) چگونه در «شبکه‌های اجتماعی» (social networks) «درگیر» (involved) می‌شوند؟",
   "mechanism": "«نظریهٔ کنشگر-شبکه» (Actor-Network Theory) برپایهٔ «دنبال‌کردن شبکه» (following the network) عمل می‌کند: (۱) «بازنمایی» (mediation) — «اجسام» (objects) «تأثیر» (influence) را «متنوع» (diverse) می‌کنند و «شبکه» (network) را «شکل‌دهی» (shape) می‌کنند؛ (۲) «ترجمه» (translation) — «کنشگران» (actors) «عناوین» (roles) یکدیگر را «تایید» (ratify) می‌کنند و «شبکه» (network) را «ثبات» (stabilize) می‌کنند؛ (۳) «شبکه‌سازی» (networking) — «شبکه» (network) از «ارتباطات» (relations) «کنشگران» (actors) «پدید می‌آید» (emerges). نتیجه: «اجتماع» (society) از «شبکه‌های» (networks) «کنشگران» (actors) انسانی و غیرانسانی «شکل می‌گیرد» (is constituted).",
   "assumptions": ["«اجتماع» (society) از «شبکه‌های کنشگری» (actor-networks) «شکل می‌گیرد» (is constituted) می‌شود", "«اجسام» (objects) «کنشگری» (agency) دارند", "«بازنمایی‌ها و ترجمه‌ها» (mediations and translations) «شبکه‌ها» (networks) را «شکل‌دهی» (shape) می‌کنند"],
   "critiques": ["الگو گاه «شبکه‌محور» (network-centric) است و «عوامل دیگر» (other factors) را «تاریکی» (blur) می‌کند", "«کنشگری اجسام» (object agency) «دشوار» (difficult) برای «اندازه‌گیری» (measuring) است", "تعمیم آن از «مطالعات علم» (science studies) به «رسانه‌ها» (media) نیازمند بازبینی است"],
   "applications": ["تحلیل «شبکه‌های رسانه‌ای» (media networks) در «رسانه‌های دیجیتال» (digital media)", "تحلیل «فناوری‌های ارتباطی» (communication technologies) در «شبکه‌های اجتماعی» (social networks)", "تحلیل «کنشگران غیرانسانی» (non-human actors) در «پلتفرم‌های آنلاین» (online platforms)"],
   "evolution": "از Latour (1987) تا کاربرد معاصر در تحلیل «شبکه‌های رسانه‌ای» (media networks) و «فناوری‌های ارتباطی» (communication technologies) در «رسانه‌های دیجیتال» (digital media).",
   "key_concepts": ["کنشگر-شبکه (actor-network)", "بازنمایی (mediation)", "ترجمه (translation)", "شبکه‌سازی (networking)"],
   "studies": ["Latour, B. (1987). Science in Action: How to Follow Scientists and Engineers through Society. Harvard University Press."],
 },
 "MC-084": {
   "summary": "«نظریهٔ صنعت فرهنگ» (Culture Industry Theory) که توسط Theodor W. Adorno و Max Horkheimer در فصل «The Culture Industry: Enlightenment as Mass Deception» از کتاب «Dialectic of Enlightenment» (1944) صورت‌بندی شد، به تحلیل «تولید انبوه فرهنگ» (mass production of culture) می‌پردازد. Adorno و Horkheimer بر این ایده استوارند که «صنعت فرهنگ» (culture industry) «فرهنگ» (culture) را به «کالاهای» (commodities) «تبدیل» (transform) می‌کند و «مخاطبان» (consumers) را «فریب» (deceive) می‌دهد که «انتخاب» (choice) و «آزادی» (freedom) دارند (Adorno & Horkheimer, 1944).",
   "main_problem": "«صنعت فرهنگ» (culture industry) چگونه «فرهنگ» (culture) را «تولید انبوه» (mass-produced) می‌کند و «روشن‌فکری» (enlightenment) چگونه به «فریب انبوه» (mass deception) «تبدیل» (transformed) می‌شود؟",
   "mechanism": "«نظریهٔ صنعت فرهنگ» (Culture Industry Theory) برپایهٔ «تولید انبوه فرهنگ» (mass production of culture) عمل می‌کند: (۱) «تولید انبوه» (mass production) — «صنعت فرهنگ» (culture industry) «فرهنگ» (culture) را به «کالاهای» (commodities) «تولید انبوه» (mass-produced) «تبدیل» (transforms) می‌کند؛ (۲) «استانداردسازی» (standardization) — «محتوای فرهنگی» (cultural content) «استاندارد» (standardized) و «قابل‌کالاسازی» (commodifiable) می‌شود؛ (۳) «فریب انبوه» (mass deception) — «مخاطبان» (consumers) «فریب» (deceived) داده می‌شوند که «انتخاب» (choice) دارند. نتیجه: «صنعت فرهنگ» (culture industry) «فرهنگ» (culture) را «کالاسازی» (commodify) می‌کند.",
   "assumptions": ["«صنعت فرهنگ» (culture industry) «فرهنگ» (culture) را «تولید انبوه» (mass-produced) می‌کند", "«روشن‌فکری» (enlightenment) به «فریب انبوه» (mass deception) «تبدیل» (transformed) می‌شود", "«مخاطبان» (consumers) «فریب» (deceived) داده می‌شوند"],
   "critiques": ["الگو گاه «تولید-محور» (production-centric) است و «عوامل دیگر» (other factors) را «تاریکی» (blur) می‌کند", "«مخاطبان» (consumers) بیش‌ازحد «منفعل» (passive) فرض می‌شوند", "تعمیم آن از بافت‌های «دهۀ ۱۹۴۰» (1940s) به بافت‌های «رسانه‌های دیجیتال» (digital media) نیازمند بازبینی است"],
   "applications": ["تحلیل «صنعت فرهنگ» (culture industry) در «رسانه‌های دیجیتال» (digital media)", "تحلیل «کالاسازی فرهنگ» (cultural commodification) در «پلتفرم‌های آنلاین» (online platforms)", "تحلیل «محتوای انبوه» (mass content) در «رسانه‌های اجتماعی» (social media)"],
   "evolution": "از Adorno & Horkheimer (1944) تا کاربرد معاصر در تحلیل «صنعت فرهنگ» (culture industry) و «کالاسازی فرهنگ» (cultural commodification) در «رسانه‌های دیجیتال» (digital media).",
   "key_concepts": ["صنعت فرهنگ (culture industry)", "تولید انبوه (mass production)", "کالاسازی (commodification)", "فریب انبوه (mass deception)"],
   "studies": ["Adorno, T. W., & Horkheimer, M. (1944). The culture industry: Enlightenment as mass deception. In Dialectic of the Enlightenment."],
 },
 "MC-075": {
   "summary": "«نشانه‌شناسی» (Semiotics) که توسط Ferdinand de Saussure در کتاب «Course in General Linguistics» (1916) صورت‌بندی شد، به تحلیل «نشانه‌ها» (signs) و «معناسازی» (meaning-making) می‌پردازد. Saussure بر این ایده استوار است که «نشانه» (sign) از «دو بخش» (two parts) تشکیل می‌شود: «صورت» (signifier) (بخش صوتی/بصری) و «مفهوم» (signified) (مفهوم ذهنی)، و «معنا» (meaning) از «ارتباط نسبی» (differential relation) «نشانه‌ها» (signs) در «زبان» (language) «پدید می‌آید» (emerges) (Saussure, 1916).",
   "main_problem": "«نشانه‌ها» (signs) چگونه «معنا» (meaning) «می‌سازند» (make) و «بُعد فراتر از زبان» (extra-linguistic dimensions) چگونه در «نشانه‌شناسی» (semiotics) «تحلیل» (analysed) می‌شوند؟",
   "mechanism": "«نشانه‌شناسی» (Semiotics) برپایهٔ «تحلیل نشانه‌ها» (analysis of signs) عمل می‌کند: (۱) «نشانه» (sign) — «نشانه» (sign) از «صورت» (signifier) و «مفهوم» (signified) «تشکیل» (composed) می‌شود؛ (۲) «منطقهٔ نشانه‌شناختی» (semiological system) — «معنا» (meaning) از «ارتباط نسبی» (differential relation) «نشانه‌ها» (signs) «پدید می‌آید» (emerges)؛ (۳) «بُعد فراتر از زبان» (extra-linguistic dimension) — «نشانه‌های بصری، صوتی و نمادین» (visual, sonic, and symbolic signs) «تحلیل» (analysed) می‌شوند. نتیجه: «نشانه‌ها» (signs) «معنا» (meaning) را «می‌سازند» (make).",
   "assumptions": ["«نشانه» (sign) از «صورت» (signifier) و «مفهوم» (signified) «تشکیل» (composed) می‌شود", "«معنا» (meaning) از «ارتباط نسبی» (differential relation) «نشانه‌ها» (signs) «پدید می‌آید» (emerges)", "«نشانه‌ها» (signs) «فراتر از زبان» (beyond language) نیز «معنا» (meaning) «می‌سازند» (make)"],
   "critiques": ["الگو گاه «نشانه‌محور» (sign-centric) است و «عوامل دیگر» (other factors) را «تاریکی» (blur) می‌کند", "«ارتباط نسبی» (differential relation) «دشوار» (difficult) برای «اندازه‌گیری» (measuring) است", "تعمیم آن از «زبان» (language) به «رسانه‌های دیجیتال» (digital media) نیازمند بازبینی است"],
   "applications": ["تحلیل «نشانه‌های رسانه‌ای» (media signs) در «رسانه‌های دیجیتال» (digital media)", "تحلیل «نشانه‌های بصری» (visual signs) در «رسانه‌های تصویری» (visual media)", "تحلیل «معناسازی» (meaning-making) در «پلتفرم‌های آنلاین» (online platforms)"],
   "evolution": "از Saussure (1916) تا کاربرد معاصر در تحلیل «نشانه‌های رسانه‌ای» (media signs) و «معناسازی» (meaning-making) در «رسانه‌های دیجیتال» (digital media).",
   "key_concepts": ["نشانه (sign)", "صورت (signifier)", "مفهوم (signified)", "معنا (meaning)"],
   "studies": ["Saussure, F. de (1916). Course in General Linguistics."],
 },
 "MC-074": {
   "summary": "«تحلیل گفتمان انتقادی» (Critical Discourse Analysis) که توسط Norman Fairclough در کتاب «Discourse and Social Change» (1992) صورت‌بندی شد، به تحلیل «ارتباط گفتمان و قدرت» (discourse and power) می‌پردازد. Fairclough بر این ایده استوار است که «گفتمان» (discourse) «در» (in) «بافت‌های اجتماعی» (social contexts) «به‌کار می‌رود» (is used) تا «رابطه‌های قدرت» (power relations) و «نابرابری‌ها» (inequalities) را «حافظه‌محور» (reproduce) یا «چالش» (challenge) کند (Fairclough, 1992).",
   "main_problem": "«گفتمان» (discourse) چگونه «رابطه‌های قدرت» (power relations) و «نابرابری‌ها» (inequalities) را «حافظه‌محور» (reproduce) می‌کند و «تحلیل گفتمان انتقادی» (critical discourse analysis) چگونه «این رابطه‌ها» (these relations) را «فاح» (expose) می‌کند؟",
   "mechanism": "«تحلیل گفتمان انتقادی» (Critical Discourse Analysis) برپایهٔ «تحلیل سه‌سطحی» (three-dimensional analysis) عمل می‌کند: (۱) «تحلیل متن» (text analysis) — «ساختارهای زبانی» (linguistic structures) «تحلیل» (analysed) می‌شوند؛ (۲) «تحلیل گفتمان» (discourse practice analysis) — «فرآیندهای تولید و مصرف گفتمان» (discourse production and consumption) «تحلیل» (analysed) می‌شوند؛ (۳) «تحلیل اجتماعی» (social practice analysis) — «بافت‌های اجتماعی» (social contexts) «گفتمان» (discourse) «تحلیل» (analysed) می‌شوند. نتیجه: «گفتمان» (discourse) «رابطه‌های قدرت» (power relations) را «حافظه‌محور» (reproduce) یا «چالش» (challenge) می‌کند.",
   "assumptions": ["«گفتمان» (discourse) «رابطه‌های قدرت» (power relations) را «حافظه‌محور» (reproduce) می‌کند", "«گفتمان» (discourse) «در بافت اجتماعی» (in social context) «به‌کار می‌رود» (is used)", "«تحلیل گفتمان انتقادی» (critical discourse analysis) «این رابطه‌ها» (these relations) را «فاح» (expose) می‌کند"],
   "critiques": ["الگو گاه «گفتمان‌محور» (discourse-centric) است و «عوامل دیگر» (other factors) را «تاریکی» (blur) می‌کند", "«ارتباط گفتمان و قدرت» (discourse-power relation) «دشوار» (difficult) برای «اندازه‌گیری» (measuring) است", "تعمیم آن از «بافت‌های انگلیسی» (English-language contexts) به بافت‌های «رسانه‌های فارسی» (Persian media contexts) نیازمند بازبینی است"],
   "applications": ["تحلیل «گفتمان رسانه‌ای» (media discourse) در «رسانه‌های دیجیتال» (digital media)", "تحلیل «گفتمان قدرت» (power discourse) در «رسانه‌های خبری» (news media)", "تحلیل «گفتمان انتقادی» (critical discourse) در «پلتفرم‌های آنلاین» (online platforms)"],
   "evolution": "از Fairclough (1992) تا کاربرد معاصر در تحلیل «گفتمان رسانه‌ای» (media discourse) و «گفتمان قدرت» (power discourse) در «رسانه‌های دیجیتال» (digital media).",
   "key_concepts": ["گفتمان (discourse)", "رابطهٔ قدرت (power relation)", "نابرابری (inequality)", "تحلیل گفتمان انتقادی (critical discourse analysis)"],
   "studies": ["Fairclough, N. (1992). Discourse and Social Change. Polity Press."],
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
    codes = ["MC-076", "MC-084", "MC-075", "MC-074"]
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
    print("BATCH27 THEORY DONE")

if __name__ == "__main__":
    main()
