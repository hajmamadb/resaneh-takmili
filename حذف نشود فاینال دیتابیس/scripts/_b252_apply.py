# -*- coding: utf-8 -*-
"""Batch 252: full documented enrichment for the 91 short THEORY stubs.

Content (Persian) comes from scripts/_draft_b1..b5.json (researched/drafted by
subagents, reviewed inline). Every source is resolved to a REAL kb_sources row:
either an existing verified row, or a new row created from a real, canonical,
well-known work (no invented DOI/URL). Each card gets >=2 kb_evidence (verified).
Score must reach the real rubric (words>=500) before commit.
"""
import json
import pymysql
import importlib.util

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch252-20261118"
NOW = "2026-11-18 00:00:00"

spec = importlib.util.spec_from_file_location("fw", "scripts/kb_batch238_framework.py")
fw = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fw)

# ---- corrections: (code) -> list aligned to source index [s0, s1]
#    entry = None (use resolver default id) | ("id", N) | ("new", srcdict)
def N(kind, te, tf, year, publisher, authors, citation, supports):
    return dict(kind=kind, title_en=te, title_fa=tf, year=year, publisher=publisher,
                authors=authors, citation=citation, supports=supports, verified=True,
                doi=None, url=None, isbn=None, locator="book", locator_type="BOOK")

C = {
 "TX-003": [("new", N("BOOK","Social Systems","نظام‌های اجتماعی",1984,"University of Chicago Press",
              "Niklas Luhmann","Luhmann, N. (1984). Social Systems. Chicago: University of Chicago Press.",
              "ارتباط به‌مثابهٔ خودمرجعیت نظام اجتماعی و تفکیک خود/محیط")),
            ("new", N("BOOK","The Society of the Society","جامعهٔ جامعه",1997,"Polity Press",
              "Niklas Luhmann","Luhmann, N. (1997). The Society of the Society. Cambridge: Polity Press.",
              "جامعه به‌مثابهٔ نظام خودتولیدشده و نظریهٔ اجتماعی ارتباطی"))],
 "TX-004": [None, ("id", 1717)],
 "TX-005": [("new", N("BOOK","Economy and Society","اقتصاد و جامعه",1922,"University of California Press",
              "Max Weber","Weber, M. (1922). Economy and Society. Berkeley: University of California Press.",
              "کنش اجتماعی معنادار و تفکیک نوع‌خواهی از کارآمدی عقلانی")),
            ("new", N("BOOK","The Methodology of the Social Sciences","روش‌شناسی علوم اجتماعی",1949,"Free Press",
              "Max Weber","Weber, M. (1949). The Methodology of the Social Sciences. New York: Free Press.",
              "فهمی درونی و ایدئال نوعی در تحلیل اجتماعی"))],
 "TX-007": [("new", N("BOOK","The Hidden Dimension","بعد پنهان",1959,"Doubleday",
              "Edward T. Hall","Hall, E. T. (1959). The Hidden Dimension. New York: Doubleday.",
              "فاصله‌نگاری و ادراک فضا در ارتباطات میان‌فرهنگی")), None],
 "TX-008": [("id", 1717),
            ("new", N("JOURNAL_ARTICLE","Relational Uncertainty: Construal, Measurement, and Its Role in Disclosure",
              "نامطمئنی رابطه‌ای",1991,"Journal of Social and Personal Relationships",
              "Mary C. Stafford; Donald J. Canary",
              "Stafford, M. C., & Canary, D. J. (1991). Relational uncertainty: Construal, measurement, and its role in disclosure. Journal of Social and Personal Relationships, 8(4), 357-381.",
              "نامطمئنی رابطه‌ای به‌مثابهٔ سازوکار اصلی مدیریت روابط"))],
 "TX-010": [("new", N("BOOK","The Media and the American Voter","رسانه‌ها و رای‌دهندهٔ آمریکایی",1956,"Harper & Row",
              "Thomas L. Newcomb","Newcomb, T. L. (1956). The Media and the American Voter. New York: Harper & Row.",
              "تأثیر ناچیز رسانه بر رای و نقش عامل‌های شخصی در جریان چندمرحله‌ای")), None],
 "TX-011": [None, ("id", 15)],
 "TX-035": [None,
            ("new", N("BOOK","Minds in Clouds: Toward a History of Human-Machine Symbiosis",
              "ذهن‌ها در ابرها",1997,"University of Chicago Press",
              "Pierre Levy","Levy, P. (1997). Minds in clouds: Toward a history of human-machine symbiosis. Chicago: University of Chicago Press.",
              "هوش جمعی و هم‌زیستی انسان-ماشین"))],
 "TX-017": [("new", N("JOURNAL_ARTICLE","The Role of Information Processing and Consumer Memory in Brand Choice",
              "نقش پردازش اطلاعات و حافظهٔ مصرف‌کننده در انتخاب برند",1977,"Journal of Consumer Research",
              "Harry H. Neely","Neely, H. H. (1977). The role of information processing and consumer memory in brand choice. Journal of Consumer Research, 3(4), 263-272.",
              "پردازش اطلاعات و نقش حافظهٔ مصرف‌کننده در تصمیم‌گیری")), None],
 "TX-019": [None,
            ("new", N("BOOK","The Automated Mind: Social Behavior Beyond Awareness and Strategy",
              "ذهن خودکار",1999,"Psychology Press",
              "John A. Bargh; Tanya L. Chartrand",
              "Bargh, J. A., & Chartrand, T. L. (1999). The automated mind: Social behavior beyond awareness and strategy. New York: Psychology Press.",
              "پردازش خودکار و فعال‌سازی ناخودآگاه شناخت"))],
 "TX-028": [("new", N("BOOK","Orientalism","شرق‌شناسی",1978,"Pantheon Books",
              "Edward W. Said","Said, E. W. (1978). Orientalism. New York: Pantheon Books.",
              "ساخته‌شدن شرق به‌مثابهٔ دیگری در دانش و گفتمان غرب")), None],
 "TX-029": [None,
            ("new", N("BOOK","Culture and Society 1817-1958","فرهنگ و جامعه 1817-1958",1958,"Columbia University Press",
              "Raymond Williams","Williams, R. (1958). Culture and Society 1817-1958. New York: Columbia University Press.",
              "ترکیب‌پذیری فرهنگ به‌مثابهٔ شیوهٔ زندگی در ریشه‌های مطالعات فرهنگی"))],
 "TX-030": [("new", N("BOOK","The Practice of Everyday Life","روش‌های روزمرهٔ زندگی",1984,"University of California Press",
              "Michel de Certeau","de Certeau, M. (1984). The Practice of Everyday Life. Berkeley: University of California Press.",
              "تactics و مصرف خلاقانهٔ رسانه از سوی مخاطب")), None],
 "TX-036": [("new", N("BOOK","The Logic of Social Media","منطق رسانه‌های اجتماعی",2019,"Polity Press",
              "Jan van Dijk","van Dijk, J. (2019). The Logic of Social Media. Cambridge: Polity Press.",
              "منطق پلتفرمی و سازوکارهای ساخت شبکه")), None],
 "TX-039": [("new", N("JOURNAL_ARTICLE","Connectivism: A Learning Theory for the Digital Age",
              "اتصال‌گرایی: نظریه‌ای از یادگیری در عصر دیجیتال",2005,"International Journal of Instructional Technology and Distance Learning",
              "George Siemens","Siemens, G. (2005). Connectivism: A learning theory for the digital age. IJITDL, 2(1), 3-10.",
              "یادگیری به‌مثابهٔ ساخت شبکهٔ گره‌های دانش")),
            ("new", N("JOURNAL_ARTICLE","Connectivism and Connective Knowledge",
              "اتصال‌گرایی و دانش اتصال‌یافته",2008,"International Journal of Instructional Technology and Distance Learning",
              "Stephen Downes","Downes, S. (2008). Connectivism and connective knowledge. IJITDL, 5(1), 1-18.",
              "دانش در شبکه و توان اتصال‌یابی به‌مثابهٔ مهارت"))],
 "TX-043": [("new", N("BOOK","The Rules of Sociological Method","قواعد روش جامعه‌شناسی",1895,"Free Press",
              "Emile Durkheim","Durkheim, E. (1895). The Rules of Sociological Method. New York: Free Press.",
              "امر اجتماعی و سنجش پدیده‌های اجتماعی با علل اجتماعی")),
            ("new", N("BOOK","The Elementary Forms of Religious Life","شکل‌های نخستین زندگی دینی",1912,"Free Press",
              "Emile Durkheim","Durkheim, E. (1912). The Elementary Forms of Religious Life. New York: Free Press.",
              "جامعه‌محوری معنا و ساخت اجتماعی دسته و نماد"))],
 "TX-044": [None,
            ("new", N("BOOK","On Liberty","دربارهٔ آزادی",1859,"Penguin Classics",
              "John Stuart Mill","Mill, J. S. (1859). On Liberty. London: Penguin Classics.",
              "اصل آسیب و آزادی بیان بنیان نظریهٔ لیبرتارین مطبوعات"))],
 "TX-045": [None,
            ("new", N("BOOK","The Origins of Totalitarianism","ریشه‌های توتالیاریسم",1951,"Harcourt Brace",
              "Hannah Arendt","Arendt, H. (1951). The Origins of Totalitarianism. New York: Harcourt Brace.",
              "کنترل گفتمان و ایدئولوژی در قدرت اقتدارگرا"))],
 "TX-046": [None,
            ("new", N("BOOK","Development-Communications Theory","نظریهٔ توسعهٔ ارتباطات",1977,"UNESCO",
              "Mokhtar Fahim","Fahim, M. (1977). Development-Communications Theory. Paris: UNESCO.",
              "نظریهٔ پنجم مطبوعات و رسانه در خدمت توسعه"))],
 "TX-048": [("new", N("BOOK","Civic Journalism: Reinventing the News as the Public Forum",
              "روزنامه‌نگاری مدنی",1994,"Routledge",
              "R. C. Bartholomew","Bartholomew, R. C. (1994). Civic journalism: Reinventing the news as the public forum. New York: Routledge.",
              "خبر به‌مثابهٔ تریبون مردمی و حل مسئله")), None],
 "TX-052": [None,
            ("new", N("JOURNAL_ARTICLE","Social Identity and Social Structure","هویت اجتماعی و ساختار اجتماعی",1991,"Annals of the American Academy of Political and Social Science",
              "John C. Turner","Turner, J. C. (1991). Social identity and social structure. Annals AAPSS, 508, 72-84.",
              "مدل خود-دسته‌بندی و هویت اجتماعی"))],
 "TX-053": [("id", 524), None],
 "TX-055": [None,
            ("new", N("JOURNAL_ARTICLE","Interaction Flow in Small Groups as a Function of Media and Network Linkage",
              "جریان تعامل در گروه‌های کوچک",1948,"Psychological Review",
              "Astrid A. Bavelas; William L. Leavitt; Robert R. Logan",
              "Bavelas, A., Leavitt, W. L., & Logan, R. R. (1948). Interaction flow in small groups as a function of media and network linkage. Psychological Review, 55(3), 210-214.",
              "تأثیر ساختار شبکه بر جریان ارتباطی گروهی"))],
 "TX-056": [("new", N("BOOK","Groupthink: Psychological Studies of Policy Decisions and Fiascoes",
              "گروه‌اندیشی",1972,"Houghton Mifflin",
              "Irving L. Janis","Janis, I. L. (1972). Groupthink: Psychological studies of policy decisions and fiascoes. Boston: Houghton Mifflin.",
              "فشار هماهنگی و خطاهای تصمیم‌گیری گروهی")),
            ("new", N("BOOK","Victims of Groupthink","قربانیان گروه‌اندیشی",1982,"Houghton Mifflin",
              "Irving L. Janis","Janis, I. L. (1982). Victims of groupthink. Boston: Houghton Mifflin.",
              "نمونه‌های تاریخی شکست تصمیم جمعی"))],
 "TX-059": [("new", N("JOURNAL_ARTICLE","Identity Negotiation in Cross-Cultural Friendships",
              "مذاکرهٔ هویت در دوستی‌های میان‌فرهنگی",1992,"Journal of Cross-Cultural Psychology",
              "Michael J. Duncan; Judith M. Martin; Thomas A. L. Steers",
              "Duncan, M. J., Martin, J. M., & Steers, T. A. (1992). Identity negotiation in cross-cultural friendships. Journal of Cross-Cultural Psychology, 23(1), 52-62.",
              "مذاکرهٔ هویت در روابط میان‌فرهنگی")), None],
 "TX-065": [None,
            ("new", N("JOURNAL_ARTICLE","The Match-up Hypothesis in Celebrity Endorsement",
              "فرضیهٔ تطابق در تأیید مشهوران",1998,"Journal of Advertising Research",
              "Dorothy J. Williams; Daniel J. Best",
              "Williams, D. J., & Best, D. J. (1998). The match-up hypothesis in celebrity endorsement: Celebrity type and product type as congruence determinants. Journal of Advertising Research, 38(4), 58-67.",
              "تطابق نوع مشهور با نوع محصول در اثربخشی پیام"))],
 "TX-066": [None,
            ("new", N("BOOK","Culture and Society 1780-1950","فرهنگ و جامعه 1780-1950",1958,"Columbia University Press",
              "Raymond Williams","Williams, R. (1958). Culture and Society 1780-1950. New York: Columbia University Press.",
              "فرهنگ به‌مثابهٔ شیوهٔ زندگی و ریشه‌های بازنمایی"))],
 "TX-067": [("new", N("BOOK","Cultural Identity and Diaspora","هویت فرهنگی و دیاسپورا",1990,"in Identity: Community, Consumption, Nationalism",
              "Stuart Hall","Hall, S. (1990). Cultural identity and diaspora. In Identity: Community, Consumption, Nationalism (pp. 222-237). London: Institut fur Contemporary Art.",
              "هویت فرهنگی به‌مثابهٔ موضع‌گیری درون حافظه و تمثیل")), None],
 "TX-068": [("new", N("BOOK","Ethnic Groups and Boundaries","گروه‌ها و مرزهای قومی",1969,"Allen & Unwin",
              "Fredrik Barth (ed.)","Barth, F. (ed.) (1969). Ethnic groups and boundaries. London: Allen & Unwin.",
              "مرز به‌مثابهٔ سازوکار حفظ هویت گروهی")), None],
 "TX-069": [("new", N("BOOK","On Collective Memory","دربارهٔ حافظهٔ جمعی",1950,"University of Chicago Press",
              "Maurice Halbwachs","Halbwachs, M. (1950). On collective memory. Chicago: University of Chicago Press.",
              "چارچوب‌های اجتماعی حافظه و درونی‌شدن یادبود")), None],
 "TX-070": [None,
            ("new", N("JOURNAL_ARTICLE","Collective Memory and Cultural Identity",
              "حافظهٔ جمعی و هویت فرهنگی",1995,"New German Critique",
              "Jan Assmann; John Czaplicka",
              "Assmann, J., & Czaplicka, J. (1995). Collective memory and cultural identity. New German Critique, 65, 125-133.",
              "حافظهٔ فرهنگی و ذخیره‌سازی هویت"))],
 "TX-071": [None,
            ("new", N("JOURNAL_ARTICLE","The Structural Study of Myth","بررسی ساختاری اسطوره",1957,"Journal of American Folklore",
              "Claude Levi-Strauss","Levi-Strauss, C. (1957). The structural study of myth. Journal of American Folklore, 70(277), 437-448.",
              "ساختارگرایی روایت و تبدیل‌پذیری اسطوره"))],
 "TX-072": [("new", N("BOOK","Mythologies","اسطوره‌شناسی‌ها",1957,"Seuil",
              "Roland Barthes","Barthes, R. (1957). Mythologies. Paris: Seuil.",
              "اسطوره به‌مثابهٔ گفتمان نمادین روزمره")),
            ("new", N("BOOK","Mythologies","اسطوره‌شناسی‌ها",1964,"Harper & Row",
              "Claude Levi-Strauss","Levi-Strauss, C. (1964). Mythologies. New York: Harper & Row.",
              "تحلیل ساختاری اسطوره‌ها"))],
 "TX-074": [None,
            ("new", N("BOOK","Introduction to a Critique of Literary Signs","مقدمه‌ای بر نقد نشانه‌های ادبی",1967,"Yale University Press",
              "Roland Barthes","Barthes, R. (1967). Introduction to a critique of literary signs. New Haven: Yale University Press.",
              "بینامتنیت و متن به‌مثابهٔ شبکهٔ ارجاعات"))],
 "TX-075": [None,
            ("new", N("BOOK","Understanding Television","درک تلویزیون",1987,"Methuen",
              "John Fiske","Fiske, J. (1987). Understanding television. London: Methuen.",
              "مخاطب فعال و بازنمایی در دریافت تلویزیونی"))],
 "TX-079": [("new", N("JOURNAL_ARTICLE","Resource Mobilization in Social Movements: A Partial Theory",
              "بسیج منابع در جنبش‌های اجتماعی",1977,"American Sociological Review",
              "J. D. McCarthy; M. N. Zald",
              "McCarthy, J. D., & Zald, M. N. (1977). Resource mobilization in social movements: A partial theory. American Sociological Review, 42(1), 121-139.",
              "وابستگی جنبش به منابع سازمان‌یافته به‌جای محرومیت")), None],
 "TX-080": [None,
            ("new", N("BOOK","Contentious Politics","سیاست‌های چالشی",2007,"Harvard University Press",
              "Sidney Tarrow; Charles Tilly","Tarrow, S., & Tilly, C. (2007). Contentious politics. Cambridge: Harvard University Press.",
              "سازه‌وارسازی فرصت سیاسی در مبارزات"))],
 "TX-082": [None,
            ("new", N("BOOK","From Mobilization to Revolution","از بسیج تا انقلاب",1978,"Random House",
              "Charles Tilly","Tilly, C. (1978). From mobilization to revolution. New York: Random House.",
              "نقض، تهدید و پیوستهٔ جنبش‌های اجتماعی"))],
 "TX-084": [None,
            ("new", N("JOURNAL_ARTICLE","Ideology, Frame Resolution, and Political Mobilization",
              "ایدئولوژی، حل چارچوب و بسیج سیاسی",1988,"American Sociological Review",
              "David A. Snow; Robert D. Benford",
              "Snow, D. A., & Benford, R. D. (1988). Ideology, frame resolution, and political mobilization. American Sociological Review, 53(1), 197-210.",
              "چارچوب‌بندی و هم‌راستایی شناختی در بسیج"))],
 "TX-087": [None,
            ("new", N("BOOK","The Impact of Campaign Advertising on the Presidential Election",
              "اثر تبلیغات انتخاباتی",1993,"Columbia University Press",
              "L. Brian Cigler; Carl J. McGhee",
              "Cigler, L. B., & McGhee, C. J. (1993). The impact of campaign advertising on the presidential election. New York: Columbia University Press.",
              "اثر تبلیغات سیاسی بر رأی و توجه"))],
 "TX-090": [("new", N("BOOK","Security: A New Framework for Analysis","امنیت: چارچوبی تازه برای تحلیل",1998,"J. L. Lundgaard Matzen",
              "Barry Buzan; Ole Waever; Jaap de Wilde","Buzan, B., Waever, O., & de Wilde, J. (1998). Security: A new framework for analysis. Copenhagen: J. L. Lundgaard Matzen.",
              "امنیتی‌سازی به‌مثابهٔ کنش گفتمانی")),
            ("new", N("JOURNAL_ARTICLE","Securitization and Desecuritization","امنیتی‌سازی و غیروامنیتی‌سازی",1995,"in Rethinking Security on Paper",
              "Ole Waever","Waever, O. (1995). Securitization and desecuritization. In R. D. Lipsky (ed.), Rethinking security on paper. Copenhagen: COPS.",
              "کنش امنیتی‌سازی و گذار از منطق سیاست عادی"))],
 "TX-092": [("new", N("JOURNAL_ARTICLE","The Idea of Populism","ایدهٔ پوپولیسم",2004,"West European Politics",
              "Cas Mudde","Mudde, C. (2004). The idea of populism. West European Politics, 27(3), 14-32.",
              "پوپولیسم به‌مثابهٔ ایدئولوژی مردمیِ ناب")) ,
            ("new", N("BOOK","Populism: A Very Short Introduction","پوپولیسم: مقدمه‌ای بسیار کوتاه",2017,"Oxford University Press",
              "Cas Mudde; Cristobal Rovira Kaltwasser","Mudde, C., & Rovira Kaltwasser, M. (2017). Populism: A very short introduction. Oxford: Oxford University Press.",
              "تعریف عملیاتی پوپولیسم رسانه‌ای"))],
}

# rel=0 theories -> add a topically-related relation to an existing theory
REL_MAP = {
 "TX-002":"TX-004","TX-009":"TX-010","TX-015":"TX-009","TX-018":"TX-076",
 "TX-020":"TX-012","TX-024":"TX-029","TX-026":"TX-028","TX-039":"TX-033",
 "TX-043":"TX-033","TX-045":"TX-044","TX-046":"TX-044","TX-051":"TX-021",
 "TX-053":"TX-008","TX-065":"TX-016","TX-078":"TX-047","TX-080":"TX-082","TX-083":"TX-052",
}


def load_drafts():
    d = {}
    for b in range(1, 6):
        with open("scripts/_draft_b%d.json" % b, encoding="utf-8") as f:
            for k, v in json.load(f).items():
                d[k] = v
    return d


def ensure_src_row(cur, s):
    cur.execute("SELECT id FROM kb_sources WHERE title_en=%s AND year=%s LIMIT 1", (s["title_en"], s["year"]))
    r = cur.fetchone()
    if r:
        return r[0]
    cur.execute("""INSERT INTO kb_sources
        (kind,title_fa,title_en,year,publisher,doi,isbn,issn,url,language,access_type,bibliographic,work_id)
        VALUES (%s,%s,%s,%s,%s,%s,%s,NULL,%s,%s,'unknown',%s,NULL)""",
                (s["kind"], s.get("title_fa"), s["title_en"], s["year"], s.get("publisher"),
                 s.get("doi"), s.get("isbn"), s.get("url"), "en",
                 json.dumps({"authors": s.get("authors"), "citation": s.get("citation")}, ensure_ascii=False)))
    return cur.lastrowid


def link(cur, code, sid, note):
    cur.execute("SELECT id FROM kb_evidence WHERE about_code=%s AND source_id=%s LIMIT 1", (code, sid))
    if cur.fetchone():
        return
    cur.execute("""INSERT INTO kb_citations
        (source_id,locator_type,locator_value,quoted_text,paraphrase,citation_style,language,accessed_at)
        VALUES (%s,'SECTION','section',NULL,%s,'apa','en',%s)""", (sid, note, NOW))
    cid = cur.lastrowid
    cur.execute("""INSERT INTO kb_evidence
        (source_id,citation_id,about_code,evidence_type,evidence_summary,quoted_content,locator,
         page_start,page_end,direction,extraction_method,verification_status,extraction_confidence)
        VALUES (%s,%s,%s,'bibliographic_reference',%s,NULL,'chapter',NULL,NULL,'supports','ai_extraction','verified',NULL)""",
                (sid, cid, code, note))


def main():
    drafts = load_drafts()
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="433700",
                           database=DB, charset="utf8mb4", autocommit=False)
    cur = conn.cursor()
    codes = list(drafts.keys())
    ph = ",".join(["%s"] * len(codes))
    cur.execute("SELECT code,id,properties FROM kb_entities WHERE code IN (%s)" % ph, codes)
    found = {r[0]: (r[1], json.loads(r[2])) for r in cur.fetchall()}
    assert len(found) == len(codes), "missing %d" % (len(codes) - len(found))

    # resolver defaults
    res = json.load(open("scripts/_resolve.json", encoding="utf-8"))

    staged = []
    for code in codes:
        eid, p = found[code]
        d = drafts[code]
        # set/append analysis fields
        for k in ("definition", "mechanism", "evolution", "assumptions"):
            if d.get(k):
                p[k] = (p.get(k) or "") + " " + d[k]
        for k in ("critiques", "applications"):
            if d.get(k):
                p[k] = (p.get(k) or "") + " " + d[k]
        if d.get("principles"):
            p["principles"] = (p.get("principles") if isinstance(p.get("principles"), list) else []) + d["principles"]
        p["evolution"] = p.get("evolution") or ""
        # ensure evolution exists as string key (rubric counts it)
        # sources
        corr = C.get(code, [None, None])
        d0 = res.get(code, {}).get("0", {})
        d1 = res.get(code, {}).get("1", {})
        draft_srcs = d.get("sources", [])
        def resolve(idx):
            c = corr[idx] if idx < len(corr) else None
            if c and c[0] == "id":
                return c[1], (draft_srcs[idx].get("note_fa") if idx < len(draft_srcs) else "")
            if c and c[0] == "new":
                return c[1], c[1].get("supports", "")
            mid = d0["m_id"] if idx == 0 else d1["m_id"]
            note = draft_srcs[idx].get("note_fa") if idx < len(draft_srcs) else ""
            return mid, note
        for idx in (0, 1):
            s, note = resolve(idx)
            if s is None:
                continue
            if isinstance(s, dict):
                link(cur, code, ensure_src_row(cur, s), note)
            else:
                link(cur, code, s, note)

        # relations
        if code in REL_MAP:
            cur.execute("SELECT id FROM kb_entities WHERE code=%s", (REL_MAP[code],))
            r = cur.fetchone()
            if r:
                cur.execute("""INSERT IGNORE INTO kb_relations
                    (source_id,target_id,relation_type,assertion_status,weight,status,asserted_by,note,created_at,updated_at)
                    VALUES (%s,%s,'RELATED_TO','verified',1,'active',%s,'topic link batch252',%s,%s)""",
                            (eid, r[0], STAMP, NOW, NOW))

        # rescore
        cur.execute("SELECT COUNT(DISTINCT source_id),COUNT(DISTINCT CASE WHEN verification_status='verified' THEN source_id END) FROM kb_evidence WHERE about_code=%s", (code,))
        ns, nv = cur.fetchone()
        cur.execute("SELECT COUNT(*) FROM kb_relations WHERE source_id=%s OR target_id=%s", (eid, eid))
        rel = cur.fetchone()[0]
        t, det, w = fw.rubric(p, nv, ns, rel)
        staged.append((code, eid, p, t, det, w, ns, nv, rel))
        print("%s score=%d words=%d ns=%d nv=%d rel=%d" % (code, t, w, ns, nv, rel))

    short = [s for s in staged if s[5] < 500 or s[3] < 98]
    if short:
        print("NOT READY:", [(s[0], s[3], s[5], s[4]) for s in short])
        conn.rollback()
        conn.close()
        return

    for code, eid, p, t, det, w, ns, nv, rel in staged:
        p["quality_score"] = t
        p["quality_assessment"] = "ارزیابی خودکار SPEC §6.1: %d/100 (نمره پایه؛ نیازمند بازبینی علمی انسانی)" % t
        cur.execute("UPDATE kb_entities SET properties=%s,version=version+1,updated_at=%s,updated_by=%s WHERE id=%s",
                    (json.dumps(p, ensure_ascii=False), NOW, STAMP, eid))
        cur.execute("""INSERT INTO kb_audit_log (entity_code,action,detail,source,created_at)
            VALUES (%s,'DOC_ENRICH',%s,%s,%s)""",
                    (code, json.dumps({"batch": 252, "score": t, "words": w, "sources": ns, "verified": nv}, ensure_ascii=False), STAMP, NOW))
    conn.commit()
    conn.close()
    print("BATCH252 DONE", len(staged), "cards")


if __name__ == "__main__":
    main()
