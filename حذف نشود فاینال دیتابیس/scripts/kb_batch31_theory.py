# -*- coding: utf-8 -*-
"""Batch 31 (THEORY): MC-114 Participatory Culture (Jenkins 2006), MC-117 Platform Society
(van Dijck, Poell & de Waal 2018), MC-122 Situational Crisis Communication Theory (Coombs 2007),
MC-137 Nudge & Choice Architecture (Thaler & Sunstein 2008). Sources web-verified 2026-11-16.
Target: resaname_kb_final_inspect."""
import pymysql, json

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch31-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch31_theory.json"

S = {
 "MC-114": [  # Participatory Culture
   dict(kind="BOOK", title_en="Fans, Bloggers, and Gamers: Media Consumers in a Digital Age",
        title_fa="طرفداران، وبلاگ‌نویسان و گیمرها: مصرف‌کنندگان رسانه در عصر دیجیتال", authors="Jenkins, H.", year=2006,
        publisher="New York: New York University Press", doi=None, url=None, language="en", isbn=None,
        citation="Jenkins, H. (2006). Fans, bloggers, and gamers: Media consumers in a digital age. New York University Press.",
        locator="whole work", locator_type="work", supports="definition / mechanism / origin", verified=True),
   dict(kind="BOOK", title_en="Textual Poachers: Television Fans and Participatory Culture",
        title_fa="شکارچیان متنی: طرفداران تلویزیون و فرهنگ مشارکتی", authors="Jenkins, H.", year=1992,
        publisher="London: Routledge", doi=None, url=None, language="en", isbn=None,
        citation="Jenkins, H. (1992). Textual poachers: Television fans and participatory culture. Routledge.",
        locator="whole work", locator_type="work", supports="evolution / critiques", verified=False),
 ],
 "MC-117": [  # Platform Society
   dict(kind="BOOK", title_en="The Platform Society: Public Values in a Connective World",
        title_fa="جامعهٔ پلتفرمی: ارزش‌های عمومی در جهان پیوندی", authors="van Dijck, J., Poell, T., & de Waal, M.", year=2018,
        publisher="New York: Oxford University Press", doi=None, url=None, language="en", isbn=None,
        citation="van Dijck, J., Poell, T., & de Waal, M. (2018). The platform society: Public values in a connective world. Oxford University Press.",
        locator="whole work", locator_type="work", supports="definition / mechanism / origin", verified=True),
   dict(kind="BOOK", title_en="The Culture of Connectivity: A Critical History of Social Media",
        title_fa="فرهنگ پیوندی‌بودن: تاریخ انتقادی رسانه‌های اجتماعی", authors="van Dijck, J.", year=2013,
        publisher="New York: Oxford University Press", doi=None, url=None, language="en", isbn=None,
        citation="van Dijck, J. (2013). The culture of connectivity: A critical history of social media. Oxford University Press.",
        locator="whole work", locator_type="work", supports="evolution / critiques", verified=False),
 ],
 "MC-122": [  # Situational Crisis Communication Theory
   dict(kind="BOOK", title_en="Ongoing Crisis Communication: Planning, Managing, and Responding",
        title_fa="ارتباطات بحران مستمر: برنامه‌ریزی، مدیریت و پاسخ‌دهی", authors="Coombs, W. T.", year=2007,
        publisher="Thousand Oaks, CA: Sage", doi=None, url=None, language="en", isbn=None,
        citation="Coombs, W. T. (2007). Ongoing crisis communication: Planning, managing, and responding. Sage.",
        locator="whole work", locator_type="work", supports="definition / mechanism / origin", verified=True),
   dict(kind="BOOK", title_en="The Handbook of Crisis Communication",
        title_fa="راهنمای ارتباطات بحران", authors="Coombs, W. T., & Holladay, S. J.", year=2010,
        publisher="Oxford: Wiley-Blackwell", doi=None, url=None, language="en", isbn=None,
        citation="Coombs, W. T., & Holladay, S. J. (2010). The handbook of crisis communication. Wiley-Blackwell.",
        locator="whole work", locator_type="work", supports="evolution / critiques", verified=False),
 ],
 "MC-137": [  # Nudge & Choice Architecture
   dict(kind="BOOK", title_en="Nudge: Improving Decisions About Health, Wealth, and Happiness",
        title_fa="تلنگر: بهبود تصمیم‌ها دربارهٔ سلامت، ثروت و شادی", authors="Thaler, R. H., & Sunstein, C. R.", year=2008,
        publisher="New Haven, CT: Yale University Press", doi=None, url=None, language="en", isbn=None,
        citation="Thaler, R. H., & Sunstein, C. R. (2008). Nudge: Improving decisions about health, wealth, and happiness. Yale University Press.",
        locator="whole work", locator_type="work", supports="definition / mechanism / origin", verified=True),
   dict(kind="BOOK", title_en="The Ethics of Influence: Government in the Age of Behavioral Science",
        title_fa="اخلاق تأثیرگذاری: حکومت در عصر علم رفتار", authors="Sunstein, C. R.", year=2016,
        publisher="Cambridge: Cambridge University Press", doi=None, url=None, language="en", isbn=None,
        citation="Sunstein, C. R. (2016). The ethics of influence: Government in the age of behavioral science. Cambridge University Press.",
        locator="whole work", locator_type="work", supports="evolution / critiques", verified=False),
 ],
}

ENRICH = {
 "MC-114": {
   "summary": "«نظریهٔ فرهنگ مشارکتی» (Participatory Culture Theory) که توسط Henry Jenkins در کتاب «Fans, Bloggers, and Gamers: Media Consumers in a Digital Age» (2006) صورت‌بندی شد، به تحلیل «فرهنگ مشارکتی» (participatory culture) می‌پردازد. Jenkins بر این ایده استوار است که «مصرف‌کنندگان رسانه» (media consumers) «نه صرفاً مصرف‌کننده، بلکه مشارکت‌کننده» (not merely consumers but participants) هستند که «محتوا» (content) را «بازسازی» (remix) و «توزیع» (distribute) می‌کنند (Jenkins, 2006).",
   "main_problem": "«مصرف‌کنندگان رسانه» (media consumers) چگونه «مشارکت‌کننده» (participants) «تبدیل» (transform) می‌شوند و «فرهنگ مشارکتی» (participatory culture) چه «پتانسیلی» (potential) برای «توانمندسازی» (empowerment) دارد؟",
   "mechanism": "«نظریهٔ فرهنگ مشارکتی» (Participatory Culture Theory) برپایهٔ «مشارکت مخاطب» (audience participation) عمل می‌کند: (۱) «مشارکت» (participation) — «مصرف‌کنندگان» (consumers) «مشارکت‌کننده» (participants) «تبدیل» (transform) می‌شوند؛ (۲) «بازسازی» (remixing) — «محتوا» (content) «بازسازی» (remixed) و «توزیع» (distributed) می‌شود؛ (۳) «توانمندسازی» (empowerment) — «فرهنگ مشارکتی» (participatory culture) «پتانسیل» (potential) برای «توانمندسازی» (empowerment) دارد. نتیجه: «مصرف‌کنندگان» (consumers) «مشارکت‌کننده» (participants) «تبدیل» (transform) می‌شوند.",
   "assumptions": ["«مصرف‌کنندگان رسانه» (media consumers) «نه صرفاً مصرف‌کننده» (not merely consumers) هستند", "«مخاطبان» (audiences) «محتوا» (content) را «بازسازی» (remix) می‌کنند", "«فرهنگ مشارکتی» (participatory culture) «پتانسیل» (potential) برای «توانمندسازی» (empowerment) دارد"],
   "critiques": ["الگو گاه «مشارکت‌محور» (participation-centric) است و «عوامل دیگر» (other factors) را «تاریکی» (blur) می‌کند", "«مشارکت مخاطب» (audience participation) بیش‌ازحد «مثبت» (positive) فرض می‌شود و «نابرابری مشارکت» (participation inequality) را «نادیده» (overlook) می‌گیرد", "تعمیم آن از «بافت‌های آمریکا» (US context) به بافت‌های «رسانه‌های دیجیتال جهانی» (global digital media) نیازمند بازبینی است"],
   "applications": ["تحلیل «فرهنگ مشارکتی» (participatory culture) در «رسانه‌های دیجیتال» (digital media)", "تحلیل «بازسازی محتوا» (content remixing) در «رسانه‌های اجتماعی» (social media)", "تحلیل «توانمندسازی مخاطب» (audience empowerment) در «پلتفرم‌های آنلاین» (online platforms)"],
   "evolution": "از Jenkins (2006) تا کاربرد معاصر در تحلیل «فرهنگ مشارکتی» (participatory culture) و «بازسازی محتوا» (content remixing) در «رسانه‌های دیجیتال» (digital media).",
   "key_concepts": ["فرهنگ مشارکتی (participatory culture)", "مشارکت مخاطب (audience participation)", "بازسازی (remixing)", "توانمندسازی (empowerment)"],
   "studies": ["Jenkins, H. (2006). Fans, Bloggers, and Gamers: Media Consumers in a Digital Age. NYU Press."],
 },
 "MC-117": {
   "summary": "«نظریهٔ جامعهٔ پلتفرمی» (Platform Society Theory) که توسط José van Dijck، Thomas Poell و Martijn de Waal در کتاب «The Platform Society: Public Values in a Connective World» (2018) صورت‌بندی شد، به تحلیل «جامعهٔ پلتفرمی» (platform society) می‌پردازد. van Dijck و همکاران بر این ایده استوارند که «پلتفرم‌ها» (platforms) «ساختار اجتماعی» (social structure) «جامعه» (society) را «بازسازی» (reconfigure) می‌کنند و «ارزش‌های عمومی» (public values) را «به مخاطره» (challenge) می‌اندازند (van Dijck, Poell, & de Waal, 2018).",
   "main_problem": "«پلتفرم‌ها» (platforms) چگونه «ساختار اجتماعی» (social structure) «جامعه» (society) را «بازسازی» (reconfigure) می‌کنند و چگونه «ارزش‌های عمومی» (public values) «به مخاطره» (challenged) می‌افتند؟",
   "mechanism": "«نظریهٔ جامعهٔ پلتفرمی» (Platform Society Theory) برپایهٔ «بازسازی پلتفرمی» (platform reconfiguration) عمل می‌کند: (۱) «نفوذ پلتفرمی» (platform penetration) — «پلتفرم‌ها» (platforms) «ساختار اجتماعی» (social structure) «جامعه» (society) را «بازسازی» (reconfigure) می‌کنند؛ (۲) «ارزش عمومی» (public value) — «ارزش‌های عمومی» (public values) «به مخاطره» (challenged) می‌افتند؛ (۳) «منازعهٔ نظام‌ها» (system contestation) — «بازار، دولت و جامعهٔ مدنی» (market, government, civil society) «منازعه» (contest) می‌کنند. نتیجه: «پلتفرم‌ها» (platforms) «ساختار اجتماعی» (social structure) «جامعه» (society) را «بازسازی» (reconfigure) می‌کنند.",
   "assumptions": ["«پلتفرم‌ها» (platforms) «ساختار اجتماعی» (social structure) «جامعه» (society) را «بازسازی» (reconfigure) می‌کنند", "«ارزش‌های عمومی» (public values) «به مخاطره» (challenged) می‌افتند", "«بازار، دولت و جامعهٔ مدنی» (market, government, civil society) بر سر «پلتفرم‌ها» (platforms) «منازعه» (contest) می‌کنند"],
   "critiques": ["الگو گاه «پلتفرم‌محور» (platform-centric) است و «عوامل دیگر» (other factors) را «تاریکی» (blur) می‌کند", "«ارزش عمومی» (public value) «دشوار» (difficult) برای «اندازه‌گیری» (measuring) است", "تعمیم آن از بافت‌های «اروپا» (European context) به بافت‌های «رسانه‌های دیجیتال جهانی» (global digital media) نیازمند بازبینی است"],
   "applications": ["تحلیل «جامعهٔ پلتفرمی» (platform society) در «رسانه‌های دیجیتال» (digital media)", "تحلیل «ارزش عمومی» (public value) در «پلتفرم‌های آنلاین» (online platforms)", "تحلیل «حاکمیت پلتفرم» (platform governance) در «پلتفرم‌های دیجیتال» (digital platforms)"],
   "evolution": "از van Dijck, Poell & de Waal (2018) تا کاربرد معاصر در تحلیل «جامعهٔ پلتفرمی» (platform society) و «ارزش عمومی» (public value) در «رسانه‌های دیجیتال» (digital media).",
   "key_concepts": ["جامعهٔ پلتفرمی (platform society)", "ارزش عمومی (public value)", "بازسازی پلتفرمی (platform reconfiguration)", "حاکمیت پلتفرم (platform governance)"],
   "studies": ["van Dijck, J., Poell, T., & de Waal, M. (2018). The Platform Society: Public Values in a Connective World. Oxford University Press."],
 },
 "MC-122": {
   "summary": "«نظریهٔ ارتباطات بحران وضعیتی» (Situational Crisis Communication Theory - SCCT) که توسط W. Timothy Coombs در کتاب «Ongoing Crisis Communication: Planning, Managing, and Responding» (2007) صورت‌بندی شد، به تحلیل «ارتباطات بحران» (crisis communication) می‌پردازد. Coombs بر این ایده استوار است که «پاسخ سازمانی» (organizational response) «به بحران» (to crisis) باید بر «پایهٔ» (based on) «انتساب مسئولیت» (attribution of responsibility) «تنظیم» (catered) شود و «سازمان‌ها» (organizations) «پاسخ مناسب» (appropriate response) را «انتخاب» (select) کنند (Coombs, 2007).",
   "main_problem": "«سازمان‌ها» (organizations) چگونه «پاسخ سازمانی» (organizational response) «به بحران» (to crisis) را بر «پایهٔ» (based on) «انتساب مسئولیت» (attribution of responsibility) «تنظیم» (cater) می‌کنند و چه «پاسخی» (what response) «مناسب» (appropriate) است؟",
   "mechanism": "«نظریهٔ ارتباطات بحران وضعیتی» (SCCT) برپایهٔ «انتساب مسئولیت» (attribution of responsibility) عمل می‌کند: (۱) «انتساب مسئولیت» (attribution of responsibility) — «مخاطبان» (stakeholders) «مسئولیت» (responsibility) «سازمان» (organization) را در «بحران» (crisis) «انتساب» (attribute) می‌دهند؛ (۲) «انتخاب پاسخ» (response selection) — «سازمان» (organization) «پاسخ مناسب» (appropriate response) را «انتخاب» (selects) می‌کند؛ (۳) «حفاظت از اعتبار» (reputation protection) — «سازمان» (organization) «اعتبار» (reputation) خود را «حفظ» (protect) می‌کند. نتیجه: «سازمان‌ها» (organizations) «پاسخ سازمانی» (organizational response) را بر «پایهٔ» (based on) «انتساب مسئولیت» (attribution of responsibility) «تنظیم» (cater) می‌کنند.",
   "assumptions": ["«پاسخ سازمانی» (organizational response) «به بحران» (to crisis) باید بر «پایهٔ» (based on) «انتساب مسئولیت» (attribution of responsibility) «تنظیم» (catered) شود", "«انتساب مسئولیت» (attribution of responsibility) «پاسخ سازمانی» (organizational response) را «تعیین» (determines) می‌کند", "«پاسخ مناسب» (appropriate response) «اعتبار» (reputation) را «حفظ» (protects) می‌کند"],
   "critiques": ["الگو گاه «انتساب‌محور» (attribution-centric) است و «عوامل دیگر» (other factors) را «تاریکی» (blur) می‌کند", "«انتساب مسئولیت» (attribution of responsibility) «دشوار» (difficult) برای «اندازه‌گیری» (measuring) است", "تعمیم آن از بافت‌های «شرکتی» (corporate contexts) به بافت‌های «رسانه‌های دیجیتال» (digital media) نیازمند بازبینی است"],
   "applications": ["تحلیل «ارتباطات بحران» (crisis communication) در «رسانه‌های دیجیتال» (digital media)", "تحلیل «مدیریت سمعهٔ شرکتی» (corporate reputation management) در «پلتفرم‌های آنلاین» (online platforms)", "تحلیل «انتساب مسئولیت» (attribution of responsibility) در «رسانه‌های اجتماعی» (social media)"],
   "evolution": "از Coombs (2007) تا کاربرد معاصر در تحلیل «ارتباطات بحران» (crisis communication) و «مدیریت سمعه» (reputation management) در «رسانه‌های دیجیتال» (digital media).",
   "key_concepts": ["ارتباطات بحران (crisis communication)", "انتساب مسئولیت (attribution of responsibility)", "پاسخ سازمانی (organizational response)", "اعتبار (reputation)"],
   "studies": ["Coombs, W. T. (2007). Ongoing Crisis Communication: Planning, Managing, and Responding. Sage."],
 },
 "MC-137": {
   "summary": "«نظریهٔ تلنگر رفتاری و معماری انتخاب» (Nudge & Choice Architecture Theory) که توسط Richard H. Thaler و Cass R. Sunstein در کتاب «Nudge: Improving Decisions About Health, Wealth, and Happiness» (2008) صورت‌بندی شد، به تحلیل «تلنگر» (nudge) می‌پردازد. Thaler و Sunstein بر این ایده استوارند که «تغییرات کوچک در محیط» (small changes in the environment) («معماری انتخاب» (choice architecture)) می‌توانند «رفتار انسان» (human behavior) را «به‌طور قابل‌اعتماد» (reliably) «تغییر» (shift) دهند (Thaler & Sunstein, 2008).",
   "main_problem": "«تغییرات کوچک در محیط» (small changes in the environment) چگونه «رفتار انسان» (human behavior) را «به‌طور قابل‌اعتماد» (reliably) «تغییر» (shift) می‌دهند و «معماری انتخاب» (choice architecture) چگونه «تصمیم‌گیری» (decision-making) را «هدایت» (guides) می‌کند؟",
   "mechanism": "«نظریهٔ تلنگر رفتاری و معماری انتخاب» (Nudge & Choice Architecture Theory) برپایهٔ «معماری انتخاب» (choice architecture) عمل می‌کند: (۱) «معماری انتخاب» (choice architecture) — «محیط» (environment) «تصمیم‌گیری» (decision-making) را «هدایت» (guides) می‌کند؛ (۲) «تلنگر» (nudge) — «تغییر کوچک» (small change) «رفتار» (behavior) را «تغییر می‌دهد» (shifts)؛ (۳) «لیبرترین پدرسالاری» (libertarian paternalism) — «انتخاب» (choice) بدون «اجبار» (coercion) «حفظ» (preserved) می‌شود. نتیجه: «معماری انتخاب» (choice architecture) «رفتار انسان» (human behavior) را «هدایت» (guides) می‌کند.",
   "assumptions": ["«تغییرات کوچک در محیط» (small changes in the environment) «رفتار انسان» (human behavior) را «تغییر می‌دهند» (shift)", "«معماری انتخاب» (choice architecture) «تصمیم‌گیری» (decision-making) را «هدایت» (guides) می‌کند", "«انتخاب» (choice) را می‌توان بدون «اجبار» (coercion) «حفظ» (preserve) کرد"],
   "critiques": ["الگو گاه «رفتارگرا-محور» (behaviorally-centric) است و «عوامل ساختاری» (structural factors) را «تاریکی» (blur) می‌کند", "«اثربخشی تلنگر» (nudge effectiveness) «دشوار» (difficult) برای «اندازه‌گیری بلندمدت» (long-term measuring) است", "تعمیم آن از بافت‌های «سیاست عمومی» (public policy) به بافت‌های «رسانه‌های دیجیتال» (digital media) نیازمند بازبینی است"],
   "applications": ["تحلیل «تلنگر رفتاری» (nudge) در «رسانه‌های دیجیتال» (digital media)", "تحلیل «معماری انتخاب» (choice architecture) در «پلتفرم‌های آنلاین» (online platforms)", "تحلیل «طراحی» (design) در «فناوری‌های ارتباطی» (communication technologies)"],
   "evolution": "از Thaler & Sunstein (2008) تا کاربرد معاصر در تحلیل «تلنگر رفتاری» (nudge) و «معماری انتخاب» (choice architecture) در «رسانه‌های دیجیتال» (digital media).",
   "key_concepts": ["تلنگر (nudge)", "معماری انتخاب (choice architecture)", "لیبرترین پدرسالاری (libertarian paternalism)", "تصمیم‌گیری (decision-making)"],
   "studies": ["Thaler, R. H., & Sunstein, C. R. (2008). Nudge: Improving Decisions About Health, Wealth, and Happiness. Yale University Press."],
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
    codes = ["MC-114", "MC-117", "MC-122", "MC-137"]
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
    print("BATCH31 THEORY DONE")

if __name__ == "__main__":
    main()
