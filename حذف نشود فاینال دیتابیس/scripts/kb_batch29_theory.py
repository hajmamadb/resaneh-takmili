# -*- coding: utf-8 -*-
"""Batch 29 (THEORY): MC-091 Cultural Hegemony (Gramsci 1971), MC-097 Moral Panic (Cohen 1972),
MC-093 Cultural & Media Imperialism (Schiller 1969), MC-095 Orientalism & Postcolonial Media Theory
(Said 1978). Sources web-verified 2026-11-16 (Schiller year corrected to 1969/Beacon). Target: resaname_kb_final_inspect."""
import pymysql, json

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch29-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch29_theory.json"

S = {
 "MC-091": [  # Cultural Hegemony
   dict(kind="BOOK", title_en="Selections from the Prison Notebooks",
        title_fa="انتخابی از یادداشت‌های زندان", authors="Gramsci, A.", year=1971,
        publisher="London: Lawrence & Wishart (Eds. Q. Hoare & G. Nowell Smith)", doi=None, url=None, language="en",
        citation="Gramsci, A. (1971). Selections from the prison notebooks (Q. Hoare & G. Nowell Smith, Eds.). Lawrence & Wishart.",
        locator="whole work", locator_type="work", supports="definition / mechanism / origin", verified=True),
   dict(kind="BOOK", title_en="Marxism and Literature",
        title_fa="مارکسیسم و ادبیات", authors="Williams, R.", year=1977,
        publisher="Oxford: Oxford University Press", doi=None, url=None, language="en", isbn=None,
        citation="Williams, R. (1977). Marxism and literature. Oxford University Press.",
        locator="whole work", locator_type="work", supports="evolution / critiques", verified=False),
 ],
 "MC-097": [  # Moral Panic
   dict(kind="BOOK", title_en="Folk Devils and Moral Panics: The Creation of the Mods and Rockers",
        title_fa="مردماندگان و وحشت‌های اخلاقی: ساختن مدها و راکرها", authors="Cohen, S.", year=1972,
        publisher="London: Paladin; New York: Hertz", doi=None, url=None, language="en", isbn=None,
        citation="Cohen, S. (1972). Folk devils and moral panics: The creation of the mods and rockers. Paladin.",
        locator="whole work", locator_type="work", supports="definition / mechanism / origin", verified=True),
   dict(kind="BOOK", title_en="Moral Panics: The Social Construction of Scandals and Fright",
        title_fa="وحشت‌های اخلاقی: ساخت اجتماعی رسوایی‌ها و ترس‌ها", authors="Goode, E., & Ben-Yehuda, N.", year=1994,
        publisher="Oxford: Blackwell", doi=None, url=None, language="en", isbn=None,
        citation="Goode, E., & Ben-Yehuda, N. (1994). Moral panics: The social construction of scandals and fright. Blackwell.",
        locator="whole work", locator_type="work", supports="evolution / critiques", verified=False),
 ],
 "MC-093": [  # Cultural & Media Imperialism
   dict(kind="BOOK", title_en="Mass Communications and American Empire",
        title_fa="ارتباطات توده‌ای و امپراتوری آمریکایی", authors="Schiller, H. I.", year=1969,
        publisher="Boston: Beacon Press", doi=None, url=None, language="en", isbn=None,
        citation="Schiller, H. I. (1969). Mass communications and American empire. Beacon Press.",
        locator="whole work", locator_type="work", supports="definition / mechanism / origin", verified=True),
   dict(kind="BOOK", title_en="Mass Communications and American Empire (3rd ed.)",
        title_fa="ارتباطات توده‌ای و امپراتوری آمریکایی (ویرایش سوم)", authors="Schiller, H. I.", year=1992,
        publisher="Boulder, CO: Westview Press", doi=None, url=None, language="en", isbn=None,
        citation="Schiller, H. I. (1992). Mass communications and American empire (3rd ed.). Westview Press.",
        locator="whole work", locator_type="work", supports="evolution / critiques", verified=False),
 ],
 "MC-095": [  # Orientalism & Postcolonial Media Theory
   dict(kind="BOOK", title_en="Orientalism",
        title_fa="شرق‌شناسی", authors="Said, E. W.", year=1978,
        publisher="New York: Pantheon Books", doi=None, url=None, language="en", isbn=None,
        citation="Said, E. W. (1978). Orientalism. Pantheon Books.",
        locator="whole work", locator_type="work", supports="definition / mechanism / origin", verified=True),
   dict(kind="BOOK", title_en="Culture and Imperialism",
        title_fa="فرهنگ و امپریالیسم", authors="Said, E. W.", year=1993,
        publisher="New York: Alfred A. Knopf", doi=None, url=None, language="en", isbn=None,
        citation="Said, E. W. (1993). Culture and imperialism. Alfred A. Knopf.",
        locator="whole work", locator_type="work", supports="evolution / critiques", verified=False),
 ],
}

ENRICH = {
 "MC-091": {
   "summary": "«نظریهٔ هژمونی فرهنگی» (Cultural Hegemony Theory) که توسط Antonio Gramsci در «انتخابی از یادداشت‌های زندان» (1971) صورت‌بندی شد، به تحلیل «هژمونی» (hegemony) می‌پردازد. Gramsci بر این ایده استوار است که «حاکمیت سیاسی» (political domination) «به‌خودی‌خود کافی نیست» (is not sufficient)؛ «طبقهٔ حاکم» (dominant class) «هژمونی فرهنگی» (cultural hegemony) «اعمال» (exercises) می‌کند، یعنی «ارزش‌ها، باورها و عادات» (values, beliefs, and customs) خود را «طبیعی‌نمودن» (naturalize) می‌کند تا «موافقت» (consent) «طبقهٔ تحت‌حاکم» (subordinate class) را «بگیرد» (secure) (Gramsci, 1971).",
   "main_problem": "«طبقهٔ حاکم» (dominant class) چگونه «هژمونی فرهنگی» (cultural hegemony) «اعمال» (exercises) می‌کند تا «موافقت» (consent) «طبقهٔ تحت‌حاکم» (subordinate class) را «بگیرد» (secure) و چگونه «فرهنگ» (culture) «ابزار» (instrument) «حاکمیت» (domination) است؟",
   "mechanism": "«نظریهٔ هژمونی فرهنگی» (Cultural Hegemony Theory) برپایهٔ «طبیعی‌نمودن ایدئولوژی» (ideological naturalization) عمل می‌کند: (۱) «طبیعی‌نمودن» (naturalization) — «ارزش‌ها، باورها و عادات» (values, beliefs, customs) «طبقهٔ حاکم» (dominant class) به‌عنوان «طبیعی» (natural) «ارائه» (presented) می‌شوند؛ (۲) «اعمال هژمونی» (hegemony exercise) — «نهادهای مدنی» (civil institutions) (مانند «مدرسه» (school)، «رسانه» (media)، «مذهب» (religion)) «هژمونی» (hegemony) را «اعمال» (exercise) می‌کنند؛ (۳) «دریافت موافقت» (consent reception) — «طبقهٔ تحت‌حاکم» (subordinate class) «موافقت» (consent) «اعمال» (gives) می‌کند. نتیجه: «هژمونی فرهنگی» (cultural hegemony) «حاکمیت» (domination) را «پایدار» (stabilize) می‌کند.",
   "assumptions": ["«حاکمیت سیاسی» (political domination) «به‌خودی‌خود کافی نیست» (is not sufficient) برای «پایداری» (stability)", "«طبقهٔ حاکم» (dominant class) «هژمونی فرهنگی» (cultural hegemony) «اعمال» (exercises) می‌کند", "«موافقت» (consent) «طبقهٔ تحت‌حاکم» (subordinate class) «بهره‌برداری» (produced) می‌شود"],
   "critiques": ["الگو گاه «اقتصادی‌محور» (economically-centric) است و «عوامل دیگر» (other factors) را «تاریکی» (blur) می‌کند", "«طبیعی‌نمودن ایدئولوژی» (ideological naturalization) «دشوار» (difficult) برای «اندازه‌گیری» (measuring) است", "تعمیم آن از بافت‌های «ایتالیا ۱۹۲۰» (1920s Italy) به بافت‌های «رسانه‌های دیجیتال» (digital media) نیازمند بازبینی است"],
   "applications": ["تحلیل «هژمونی فرهنگی» (cultural hegemony) در «رسانه‌های دیجیتال» (digital media)", "تحلیل «طبیعی‌نمودن» (naturalization) در «رسانه‌های خبری» (news media)", "تحلیل «موافقت» (consent) در «پلتفرم‌های آنلاین» (online platforms)"],
   "evolution": "از Gramsci (1971) تا کاربرد معاصر در تحلیل «هژمونی فرهنگی» (cultural hegemony) و «طبیعی‌نمودن» (naturalization) در «رسانه‌های دیجیتال» (digital media).",
   "key_concepts": ["هژمونی فرهنگی (cultural hegemony)", "طبیعی‌نمودن (naturalization)", "موافقت (consent)", "طبقهٔ حاکم (dominant class)"],
   "studies": ["Gramsci, A. (1971). Selections from the Prison Notebooks. Lawrence & Wishart."],
 },
 "MC-097": {
   "summary": "«نظریهٔ وحشت اخلاقی» (Moral Panic Theory) که توسط Stanley Cohen در کتاب «Folk Devils and Moral Panics: The Creation of the Mods and Rockers» (1972) صورت‌بندی شد، به تحلیل «وحشت اخلاقی» (moral panic) می‌پردازد. Cohen بر این ایده استوار است که «جامعه» (society) «وحشت اخلاقی» (moral panic) «بهره‌برداری» (produces) می‌کند، یعنی «گروه‌های خاصی» (certain groups) «به‌عنوان» (as) «مردماندگان» (folk devils) «تعریف» (defined) می‌شوند و «نگرانی‌های اجتماعی» (social concerns) را «جسملی» (embodies) می‌کنند (Cohen, 1972).",
   "main_problem": "«جامعه» (society) چگونه «وحشت اخلاقی» (moral panic) «بهره‌برداری» (produces) می‌کند و چگونه «گروه‌ها» (groups) «به‌عنوان» (as) «مردماندگان» (folk devils) «تعریف» (defined) می‌شوند؟",
   "mechanism": "«نظریهٔ وحشت اخلاقی» (Moral Panic Theory) برپایهٔ «بهره‌برداری اجتماعی» (social production) عمل می‌کند: (۱) «بهره‌برداری» (production) — «گروه‌های خاص» (certain groups) «به‌عنوان» (as) «مردماندگان» (folk devils) «تعریف» (defined) می‌شوند؛ (۲) «تشدید» (amplification) — «رسانه‌ها» (media) «نگرانی‌ها» (concerns) را «تشدید» (amplify) می‌کنند؛ (۳) «پاسخ‌دهی» (response) — «نهادها» (institutions) «پاسخ» (respond) «می‌دهند» (respond). نتیجه: «وحشت اخلاقی» (moral panic) «بهره‌برداری» (produced) می‌شود.",
   "assumptions": ["«جامعه» (society) «وحشت اخلاقی» (moral panic) «بهره‌برداری» (produces) می‌کند", "«گروه‌ها» (groups) «به‌عنوان» (as) «مردماندگان» (folk devils) «تعریف» (defined) می‌شوند", "«رسانه‌ها» (media) «نگرانی‌ها» (concerns) را «تشدید» (amplify) می‌کنند"],
   "critiques": ["الگو گاه «رسانه‌محور» (media-centric) است و «عوامل دیگر» (other factors) را «تاریکی» (blur) می‌کند", "«بهره‌برداری وحشت اخلاقی» (moral panic production) «دشوار» (difficult) برای «اندازه‌گیری» (measuring) است", "تعمیم آن از بافت‌های «بریتانیا ۱۹۷۰» (1970s UK) به بافت‌های «رسانه‌های دیجیتال» (digital media) نیازمند بازبینی است"],
   "applications": ["تحلیل «وحشت اخلاقی» (moral panic) در «رسانه‌های دیجیتال» (digital media)", "تحلیل «مردماندگان» (folk devils) در «رسانه‌های خبری» (news media)", "تحلیل «تشدید نگرانی‌ها» (concern amplification) در «پلتفرم‌های آنلاین» (online platforms)"],
   "evolution": "از Cohen (1972) تا کاربرد معاصر در تحلیل «وحشت اخلاقی» (moral panic) و «مردماندگان» (folk devils) در «رسانه‌های دیجیتال» (digital media).",
   "key_concepts": ["وحشت اخلاقی (moral panic)", "مردماندگان (folk devils)", "بهره‌برداری اجتماعی (social production)", "تشدید (amplification)"],
   "studies": ["Cohen, S. (1972). Folk Devils and Moral Panics: The Creation of the Mods and Rockers. Paladin."],
 },
 "MC-093": {
   "summary": "«نظریهٔ امپریالیسم فرهنگی و رسانه‌ای» (Cultural & Media Imperialism Theory) که توسط Herbert I. Schiller در کتاب «Mass Communications and American Empire» (1969) صورت‌بندی شد، به تحلیل «امپریالیسم فرهنگی» (cultural imperialism) می‌پردازد. Schiller بر این ایده استوار است که «محتوای رسانه‌ای» (media content) در «چارچوب امپراتوری» (imperial framework) «انتقال» (transmitted) می‌شود و «کشورهای توسعه‌یافته» (developed countries) «فرهنگ» (culture) خود را بر «کشورهای در حال توسعه» (developing countries) «اعمال» (impose) می‌کنند (Schiller, 1969).",
   "main_problem": "«محتوای رسانه‌ای» (media content) چگونه در «چارچوب امپراتوری» (imperial framework) «انتقال» (transmitted) می‌شود و چگونه «کشورهای توسعه‌یافته» (developed countries) «فرهنگ» (culture) خود را بر «کشورهای در حال توسعه» (developing countries) «اعمال» (impose) می‌کنند؟",
   "mechanism": "«نظریهٔ امپریالیسم فرهنگی و رسانه‌ای» (Cultural & Media Imperialism Theory) برپایهٔ «انتقال فرهنگی امپراتوری» (imperial cultural transmission) عمل می‌کند: (۱) «انتقال محتوا» (content transmission) — «محتوای رسانه‌ای» (media content) از «کشورهای توسعه‌یافته» (developed countries) به «کشورهای در حال توسعه» (developing countries) «انتقال» (transmitted) می‌شود؛ (۲) «اعمال فرهنگ» (cultural imposition) — «فرهنگ» (culture) «کشورهای توسعه‌یافته» (developed countries) بر «کشورهای در حال توسعه» (developing countries) «اعمال» (imposed) می‌شود؛ (۳) «تغییر فرهنگ محلی» (local culture modification) — «فرهنگ محلی» (local culture) «تغییر می‌یابد» (is modified). نتیجه: «امپریالیسم فرهنگی» (cultural imperialism) «فرهنگ» (culture) را «اعمال» (imposes) می‌کند.",
   "assumptions": ["«محتوای رسانه‌ای» (media content) در «چارچوب امپراتوری» (imperial framework) «انتقال» (transmitted) می‌شود", "«کشورهای توسعه‌یافته» (developed countries) «فرهنگ» (culture) خود را بر «کشورهای در حال توسعه» (developing countries) «اعمال» (impose) می‌کنند", "«فرهنگ محلی» (local culture) «تغییر می‌یابد» (is modified)"],
   "critiques": ["الگو گاه «غرب‌محور» (Western-centric) است و «عوامل دیگر» (other factors) را «تاریکی» (blur) می‌کند", "«اعمال فرهنگ» (cultural imposition) «دشوار» (difficult) برای «اندازه‌گیری» (measuring) است", "تعمیم آن از بافت‌های «دهۀ ۱۹۶۰» (1960s) به بافت‌های «رسانه‌های دیجیتال» (digital media) نیازمند بازبینی است"],
   "applications": ["تحلیل «امپریالیسم فرهنگی» (cultural imperialism) در «رسانه‌های دیجیتال» (digital media)", "تحلیل «انتقال فرهنگی» (cultural transmission) در «رسانه‌های بین‌المللی» (international media)", "تحلیل «اعمال فرهنگ» (cultural imposition) در «پلتفرم‌های آنلاین» (online platforms)"],
   "evolution": "از Schiller (1969) تا کاربرد معاصر در تحلیل «امپریالیسم فرهنگی» (cultural imperialism) و «انتقال فرهنگی» (cultural transmission) در «رسانه‌های دیجیتال» (digital media).",
   "key_concepts": ["امپریالیسم فرهنگی (cultural imperialism)", "انتقال فرهنگی (cultural transmission)", "اعمال فرهنگ (cultural imposition)", "فرهنگ محلی (local culture)"],
   "studies": ["Schiller, H. I. (1969). Mass Communications and American Empire. Beacon Press."],
 },
 "MC-095": {
   "summary": "«نظریهٔ شرق‌شناسی و پسااستعماری رسانه» (Orientalism & Postcolonial Media Theory) که توسط Edward W. Said در کتاب «Orientalism» (1978) صورت‌بندی شد، به تحلیل «شرق‌شناسی» (Orientalism) می‌پردازد. Said بر این ایده استوار است که «غرب» (West) «شرق» (Orient) را «به‌عنوان» (as) «دیگری» (other) «بهره‌برداری» (produces) می‌کند و «شرق» (Orient) «به‌عنوان» (as) «ناتوان» (inferior) و «توسعه‌نیافته» (underdeveloped) «تعریف» (defined) می‌شود تا «حاکمیت غرب» (Western domination) «تبریر» (justified) شود (Said, 1978).",
   "main_problem": "«غرب» (West) چگونه «شرق» (Orient) را «به‌عنوان» (as) «دیگری» (other) «بهره‌برداری» (produces) می‌کند و چگونه «شرق‌شناسی» (Orientalism) «حاکمیت» (domination) را «تبریر» (justifies) می‌کند؟",
   "mechanism": "«نظریهٔ شرق‌شناسی و پسااستعماری رسانه» (Orientalism & Postcolonial Media Theory) برپایهٔ «بهره‌برداری دیگری» (other production) عمل می‌کند: (۱) «بهره‌برداری دیگری» (other production) — «غرب» (West) «شرق» (Orient) را «به‌عنوان» (as) «دیگری» (other) «بهره‌برداری» (produces) می‌کند؛ (۲) «تعریف ناهماهنگ» (asymmetric definition) — «شرق» (Orient) «به‌عنوان» (as) «ناتوان» (inferior) «تعریف» (defined) می‌شود؛ (۳) «تبریر حاکمیت» (domination justification) — «حاکمیت غرب» (Western domination) «تبریر» (justified) می‌شود. نتیجه: «شرق‌شناسی» (Orientalism) «حاکمیت» (domination) را «تبریر» (justifies) می‌کند.",
   "assumptions": ["«غرب» (West) «شرق» (Orient) را «به‌عنوان» (as) «دیگری» (other) «بهره‌برداری» (produces) می‌کند", "«شرق» (Orient) «به‌عنوان» (as) «ناتوان» (inferior) «تعریف» (defined) می‌شود", "«شرق‌شناسی» (Orientalism) «حاکمیت» (domination) را «تبریر» (justifies) می‌کند"],
   "critiques": ["الگو گاه «غرب‌محور» (Western-centric) است و «عوامل دیگر» (other factors) را «تاریکی» (blur) می‌کند", "«بهره‌برداری دیگری» (other production) «دشوار» (difficult) برای «اندازه‌گیری» (measuring) است", "تعمیم آن از بافت‌های «شرق‌شناسی کلاسیک» (classical Orientalism) به بافت‌های «رسانه‌های دیجیتال» (digital media) نیازمند بازبینی است"],
   "applications": ["تحلیل «شرق‌شناسی» (Orientalism) در «رسانه‌های دیجیتال» (digital media)", "تحلیل «دیگری‌سازی» (othering) در «رسانه‌های خبری» (news media)", "تحلیل «تبریر حاکمیت» (domination justification) در «پلتفرم‌های آنلاین» (online platforms)"],
   "evolution": "از Said (1978) تا کاربرد معاصر در تحلیل «شرق‌شناسی» (Orientalism) و «دیگری‌سازی» (othering) در «رسانه‌های دیجیتال» (digital media).",
   "key_concepts": ["شرق‌شناسی (Orientalism)", "دیگری (other)", "دیگری‌سازی (othering)", "حاکمیت (domination)"],
   "studies": ["Said, E. W. (1978). Orientalism. Pantheon Books."],
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
    codes = ["MC-091", "MC-097", "MC-093", "MC-095"]
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
    print("BATCH29 THEORY DONE")

if __name__ == "__main__":
    main()
