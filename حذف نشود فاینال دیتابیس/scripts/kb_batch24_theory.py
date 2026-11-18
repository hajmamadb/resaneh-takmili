# -*- coding: utf-8 -*-
"""Batch 24 (THEORY): MC-068 Agency Theory (Jensen & Meckling 1976), MC-063 Resource-Based View
(Barney 1991), MC-066 Institutional Isomorphism (DiMaggio & Powell 1983), MC-070 Sensemaking (Weick 1995).
Sources web-verified 2026-11-16. Target: resaname_kb_final_inspect."""
import pymysql, json

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch24-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch24_theory.json"

S = {
 "MC-068": [  # Agency Theory
   dict(kind="JOURNAL_ARTICLE", title_en="Theory of the firm: Managerial behavior, agency costs and ownership structure",
        title_fa="نظریهٔ شرکت: رفتار مدیریتی، هزینه‌های نمایندگی و ساختار مالکیت", authors="Jensen, M. C., & Meckling, W. H.", year=1976,
        publisher="Journal of Financial Economics, 3(4), 305-360", doi=None, url=None, language="en",
        citation="Jensen, M. C., & Meckling, W. H. (1976). Theory of the firm: Managerial behavior, agency costs and ownership structure. Journal of Financial Economics, 3(4), 305-360.",
        locator="pp. 305-360", locator_type="page_range", supports="definition / mechanism / origin", verified=True),
   dict(kind="JOURNAL_ARTICLE", title_en="Production, information costs, and economic organization",
        title_fa="تولید، هزینه‌های اطلاعاتی و سازمان اقتصادی", authors="Alchian, A. A., & Demsetz, H.", year=1972,
        publisher="American Economic Review, 62(5), 777-795", doi=None, url=None, language="en",
        citation="Alchian, A. A., & Demsetz, H. (1972). Production, information costs, and economic organization. American Economic Review, 62(5), 777-795.",
        locator="pp. 777-795", locator_type="page_range", supports="evolution / critiques", verified=False),
 ],
 "MC-063": [  # Resource-Based View
   dict(kind="JOURNAL_ARTICLE", title_en="Firm resources and sustained competitive advantage",
        title_fa="منابع شرکت و مزیت رقابتی پایدار", authors="Barney, J. B.", year=1991,
        publisher="Journal of Management, 17(1), 99-120", doi=None, url=None, language="en",
        citation="Barney, J. B. (1991). Firm resources and sustained competitive advantage. Journal of Management, 17(1), 99-120.",
        locator="pp. 99-120", locator_type="page_range", supports="definition / mechanism / origin", verified=True),
   dict(kind="BOOK", title_en="The Theory of the Growth of the Firm",
        title_fa="نظریهٔ رشد شرکت", authors="Penrose, E. T.", year=1959,
        publisher="Oxford University Press", doi=None, url=None, language="en", isbn=None,
        citation="Penrose, E. T. (1959). The theory of the growth of the firm. Oxford University Press.",
        locator="whole work", locator_type="work", supports="evolution / critiques", verified=False),
 ],
 "MC-066": [  # Institutional Isomorphism
   dict(kind="JOURNAL_ARTICLE", title_en="The iron cage revisited: Institutional isomorphism and collective rationality in organizational fields",
        title_fa="قفس آهنین بازنگری‌شده: هم‌شکلی نهادی و عقلانیت جمعی در میدان‌های سازمانی",
        authors="DiMaggio, P. J., & Powell, W. W.", year=1983,
        publisher="American Sociological Review, 48(2), 147-160", doi=None, url=None, language="en",
        citation="DiMaggio, P. J., & Powell, W. W. (1983). The iron cage revisited: Institutional isomorphism and collective rationality in organizational fields. American Sociological Review, 48(2), 147-160.",
        locator="pp. 147-160", locator_type="page_range", supports="definition / mechanism / origin", verified=True),
   dict(kind="JOURNAL_ARTICLE", title_en="Institutionalized organizations: Formal structure as myth and ceremony",
        title_fa="سازمان‌های نهادی‌شده: ساختار رسمی به‌عنوان افسانه و آیین", authors="Meyer, J. W., & Rowan, B.", year=1977,
        publisher="American Journal of Sociology, 83(2), 340-363", doi=None, url=None, language="en",
        citation="Meyer, J. W., & Rowan, B. (1977). Institutionalized organizations: Formal structure as myth and ceremony. American Journal of Sociology, 83(2), 340-363.",
        locator="pp. 340-363", locator_type="page_range", supports="evolution / critiques", verified=False),
 ],
 "MC-070": [  # Sensemaking
   dict(kind="BOOK", title_en="Sensemaking in Organizations",
        title_fa="معناسازی در سازمان‌ها", authors="Weick, K. E.", year=1995,
        publisher="Sage Publications", doi=None, url=None, language="en", isbn="0-8039-7177-X",
        citation="Weick, K. E. (1995). Sensemaking in organizations. Sage Publications.",
        locator="whole work", locator_type="work", supports="definition / mechanism / origin", verified=True),
   dict(kind="JOURNAL_ARTICLE", title_en="Sensemaking in organizations",
        title_fa="معناسازی در سازمان‌ها", authors="Weick, K. E.", year=1992,
        publisher="Journal of Management, 18(2), 197-218", doi=None, url=None, language="en",
        citation="Weick, K. E. (1992). Sensemaking in organizations. Journal of Management, 18(2), 197-218.",
        locator="pp. 197-218", locator_type="page_range", supports="evolution / critiques", verified=False),
 ],
}

ENRICH = {
 "MC-068": {
   "summary": "«نظریهٔ نمایندگی» (Agency Theory) که توسط Michael C. Jensen و William H. Meckling در مقالهٔ «Theory of the firm: Managerial behavior, agency costs and ownership structure» (1976) صورت‌بندی شد، به تحلیل «هزینه‌های نمایندگی» (agency costs) می‌پردازد که از «جداشدن مالکیت از کنترل» (separation of ownership and control) در «شرکت‌ها» (corporations) «به‌وجود می‌آید» (arise). Jensen و Meckling بر این ایده استوارند که «هزینه‌های نمایندگی» (agency costs) از «تنش» (tension) بین «نهادگزار» (principal) (مالک) و «نماینده» (agent) (مدیر) «به‌وجود می‌آید» (arise) و «ساختار مالکیت» (ownership structure) بر «رفتار مدیریتی» (managerial behavior) «تأثیر» (affects) دارد (Jensen & Meckling, 1976).",
   "main_problem": "چگونه «هزینه‌های نمایندگی» (agency costs) از «جداشدن مالکیت از کنترل» (separation of ownership and control) «به‌وجود می‌آید» (arise) و چگونه «ساختار مالکیت» (ownership structure) «رفتار مدیریتی» (managerial behavior) را «شکل‌دهی» (shape) می‌کند؟",
   "mechanism": "«نظریهٔ نمایندگی» (Agency Theory) برپایهٔ «رابطهٔ نمایندگی» (agency relationship) عمل می‌کند: (۱) «رابطهٔ نمایندگی» (agency relationship) — «نهادگزار» (principal) (مالک) یک «نماینده» (agent) (مدیر) را «گمارد» (appoint) تا «در جهت مصالح» (in the interest of) «نهادگزار» (principal) «عمل» (act) کند؛ (۲) «ناهماهنگی منافع» (misalignment of interests) — «نماینده» (agent) ممکن است «در جهت مصالح» (in the interest of) «خود» (own) «عمل» (act) کند، نه «نهادگزار» (principal)؛ (۳) «هزینه‌های نمایندگی» (agency costs) — «هزینه‌ها» (costs) شامل «هزینه‌های نظارتی» (monitoring costs)، «هزینه‌های تضمینی» (bonding costs)، و «زیان‌های باقی‌مانده» (residual losses) «به‌وجود می‌آید» (arise) تا «نماینده» (agent) را «همگرا» (aligned) نگه دارد. نتیجه: «هزینه‌های نمایندگی» (agency costs) «جداشدن مالکیت از کنترل» (separation of ownership and control) را «ارزش‌گذاری» (prices) می‌کند.",
   "assumptions": ["«نهادگزار» (principal) و «نماینده» (agent) «منافع ناهماهنگ» (misaligned interests) دارند", "«هزینه‌های نمایندگی» (agency costs) از «ناهماهنگی منافع» (misalignment of interests) «به‌وجود می‌آید» (arise)", "«ساختار مالکیت» (ownership structure) «رفتار مدیریتی» (managerial behavior) را «شکل‌دهی» (shape) می‌کند"],
   "critiques": ["الگو گاه «اقتصادی» (economic) بیش‌ازحد است و «عوامل اجتماعی و نهادی» (social and institutional factors) را «تاریکی» (blur) می‌کند", "«افراد عقلانی» (rational actors) «فرض» (assumption) بیش‌ازحد ساده‌ای است", "تعمیم آن از «شرکت‌های سهامی» (corporations) به «رسانه‌ها» (media) نیازمند بازبینی است"],
   "applications": ["تحلیل «ساختار مالکیت» (ownership structure) در «رسانه‌ها» (media)", "تحلیل «هزینه‌های نمایندگی» (agency costs) در «رابطهٔ مالک و مدیر» (owner-manager relationship)", "تحلیل «انگیزه‌ها و نظارت» (incentives and monitoring) در «سازمان‌های رسانه‌ای» (media organizations)"],
   "evolution": "از Jensen & Meckling (1976) تا کاربرد معاصر در تحلیل «ساختار مالکیت» (ownership structure) و «هزینه‌های نمایندگی» (agency costs) در «سازمان‌های رسانه‌ای» (media organizations).",
   "key_concepts": ["هزینه‌های نمایندگی (agency costs)", "نهادگزار (principal)", "نماینده (agent)", "جداشدن مالکیت از کنترل (separation of ownership and control)"],
   "studies": ["Jensen, M. C., & Meckling, W. H. (1976). Theory of the firm: Managerial behavior, agency costs and ownership structure. Journal of Financial Economics, 3(4), 305-360."],
 },
 "MC-063": {
   "summary": "«نظریهٔ دیدگاه مبتنی بر منابع» (Resource-Based View Theory) که توسط Jay B. Barney در مقالهٔ «Firm Resources and Sustained Competitive Advantage» (1991) صورت‌بندی شد، به تحلیل «منابع سازمانی» (organizational resources) می‌پردازد که «مزیت رقابتی پایدار» (sustained competitive advantage) «به‌وجود می‌آورد» (produces). Barney بر این ایده استوار است که «منابع» (resources) که «ارزشمند» (valuable)، «نادر» (rare)، «دشوار» (difficult to imitate)، و «جایگزین‌ناپذیر» (non-substitutable) (VRIO) باشند، «مزیت رقابتی پایدار» (sustained competitive advantage) «به‌وجود می‌آورد» (produces) (Barney, 1991).",
   "main_problem": "چرا برخی «سازمان‌ها» (organizations) «مزیت رقابتی پایدار» (sustained competitive advantage) «دارند» (possess) و چگونه «منابع» (resources) «مزیت» (advantage) «به‌وجود می‌آورد» (produce)؟",
   "mechanism": "«نظریهٔ دیدگاه مبتنی بر منابع» (Resource-Based View Theory) برپایهٔ «تحلیل منابع» (resource analysis) عمل می‌کند: (۱) «شناسایی منابع» (resource identification) — «منابع سازمانی» (organizational resources) «شناسایی» (identified) می‌شوند؛ (۲) «ارزیابی VRIO» (VRIO assessment) — «منابع» (resources) بر «پایهٔ» (based on) «ارزش» (value)، «ندرت» (rarity)، «دشواری تقلید» (difficulty of imitation)، و «جایگزینی» (substitutability) «ارزیابی» (assessed) می‌شوند؛ (۳) «مزیت پایدار» (sustained advantage) — «منابع» (resources) «VRIO» «مزیت رقابتی پایدار» (sustained competitive advantage) «به‌وجود می‌آورد» (produces). نتیجه: «منابع VRIO» (VRIO resources) «مزیت رقابتی پایدار» (sustained competitive advantage) «به‌وجود می‌آورد» (produce).",
   "assumptions": ["«منابع» (resources) «ناهمسان» (heterogeneous) بین «سازمان‌ها» (organizations) هستند", "«منابع VRIO» (VRIO resources) «مزیت پایدار» (sustained advantage) «به‌وجود می‌آورد» (produce)", "«منابع» (resources) «دشوار» (difficult) برای «انتقال» (transfer) هستند"],
   "critiques": ["الگو گاه «منبع‌محور» (resource-centric) است و «عوامل بازار» (market factors) را «تاریکی» (blur) می‌کند", "«منابع» (resources) «دشوار» (difficult) برای «شناسایی و ارزیابی دقیق» (precise identification and assessment) است", "تعمیم آن از «سازمان‌های صنعتی» (industrial organizations) به «رسانه‌ها» (media) نیازمند بازبینی است"],
   "applications": ["تحلیل «مزیت رقابتی» (competitive advantage) در «رسانه‌ها» (media)", "تحلیل «منابع سازمانی» (organizational resources) در «سازمان‌های رسانه‌ای» (media organizations)", "تحلیل «استراتژی رقابتی» (competitive strategy) در «صنایع رسانه‌ای» (media industries)"],
   "evolution": "از Penrose (1959) و Barney (1991) تا کاربرد معاصر در تحلیل «مزیت رقابتی» (competitive advantage) و «منابع سازمانی» (organizational resources) در «سازمان‌های رسانه‌ای» (media organizations).",
   "key_concepts": ["دیدگاه مبتنی بر منابع (resource-based view)", "مزیت رقابتی پایدار (sustained competitive advantage)", "منابع VRIO (VRIO resources)", "ناهمسانی منابع (resource heterogeneity)"],
   "studies": ["Barney, J. B. (1991). Firm resources and sustained competitive advantage. Journal of Management, 17(1), 99-120."],
 },
 "MC-066": {
   "summary": "«نظریهٔ هم‌شکلی نهادی» (Institutional Isomorphism Theory) که توسط Paul J. DiMaggio و Walter W. Powell در مقالهٔ «The Iron Cage Revisited» (1983) صورت‌بندی شد، به تحلیل «نحوه‌ای» می‌پردازد که «سازمان‌ها» (organizations) در «میدان‌های سازمانی» (organizational fields) «شبیه» (similar) «شده» (become) — «هم‌شکلی نهادی» (institutional isomorphism) «به‌وجود می‌آید» (occurs). DiMaggio و Powell بر این ایده استوارند که «سازمان‌ها» (organizations) «ساختارها» (structures) را از «شرایط نهادی» (institutional conditions) به «دنبال» (in pursuit of) «اعتباربخشی» (legitimacy) «پذیر» (adopt) می‌کنند، نه صرفاً «کارایی اقتصادی» (economic efficiency) (DiMaggio & Powell, 1983).",
   "main_problem": "چرا «سازمان‌ها» (organizations) در «میدان‌های سازمانی» (organizational fields) «شبیه» (similar) «شده» (become) و چگونه «هم‌شکلی نهادی» (institutional isomorphism) «به‌وجود می‌آید» (occurs)؟",
   "mechanism": "«نظریهٔ هم‌شکلی نهادی» (Institutional Isomorphism Theory) برپایهٔ «سه مکانیزم» (three mechanisms) عمل می‌کند: (۱) «هم‌شکلی اجباری» (coercive isomorphism) — «فشار» (pressure) از «سازمان‌ها و مقررات» (organizations and regulations) که «اعتباربخشی» (legitimacy) «می‌دهند» (confer)؛ (۲) «هم‌شکلی تقلیدی» (mimetic isomorphism) — «سازمان‌ها» (organizations) «سازمان‌های» (organizations) «موفق» (successful) را در «شرایط نامعلوم» (uncertainty) «کپی» (copy) می‌کنند؛ (۳) «هم‌شکلی هنجاری» (normative isomorphism) — «سازمان‌ها» (organizations) از طریق «اجتماع‌پذیری حرفه‌ای» (professional socialization) (کارکنان آموزش‌دیده) «شبیه» (similar) «شده» (become). نتیجه: «سازمان‌ها» (organizations) در «میدان‌های سازمانی» (organizational fields) «شبیه» (similar) «شده» (become).",
   "assumptions": ["«سازمان‌ها» (organizations) «اعتباربخشی» (legitimacy) را «دنبال» (pursue) می‌کنند", "«شرایط نهادی» (institutional conditions) «ساختارها» (structures) «سازمانی» (organizational) را «شکل‌دهی» (shape) می‌کنند", "«میدان‌های سازمانی» (organizational fields) «فشار» (pressure) «هم‌شکلی» (isomorphism) «ایجاد» (create) می‌کنند"],
   "critiques": ["الگو گاه «نهادی» (institutional) بیش‌ازحد است و «عوامل رقابتی» (competitive factors) را «تاریکی» (blur) می‌کند", "«سازمان‌ها» (organizations) «فراگیر» (passive) بیش‌ازحد «فرض» (assume) می‌شوند", "تعمیم آن از بافت‌های «آمریکا» (US) به «سازمان‌های رسانه‌ای» (media organizations) نیازمند بازبینی است"],
   "applications": ["تحلیل «هم‌شکلی نهادی» (institutional isomorphism) در «رسانه‌ها» (media)", "تحلیل «اعتباربخشی» (legitimacy) در «سازمان‌های رسانه‌ای» (media organizations)", "تحلیل «میدان‌های سازمانی» (organizational fields) در «صنایع رسانه‌ای» (media industries)"],
   "evolution": "از DiMaggio & Powell (1983) تا کاربرد معاصر در تحلیل «هم‌شکلی نهادی» (institutional isomorphism) و «اعتباربخشی» (legitimacy) در «سازمان‌های رسانه‌ای» (media organizations).",
   "key_concepts": ["هم‌شکلی نهادی (institutional isomorphism)", "اعتباربخشی (legitimacy)", "میدان سازمانی (organizational field)", "هم‌شکلی تقلیدی (mimetic isomorphism)"],
   "studies": ["DiMaggio, P. J., & Powell, W. W. (1983). The iron cage revisited: Institutional isomorphism and collective rationality in organizational fields. American Sociological Review, 48(2), 147-160."],
 },
 "MC-070": {
   "summary": "«نظریهٔ معناسازی» (Sensemaking Theory) که توسط Karl E. Weick در کتاب «Sensemaking in Organizations» (1995) صورت‌بندی شد، به تحلیل «نحوه‌ای» می‌پردازد که «افراد و سازمان‌ها» (individuals and organizations) «معنا» (meaning) از «تجربیات نامطمئن» (uncertain experiences) «ساخته» (create) می‌کنند. Weick بر این ایده استوار است که «معناسازی» (sensemaking) «فرآیندی» (process) است که در آن «افراد» (individuals) «واقعیت» (reality) را «ساخته» (construct) می‌کنند — از طریق «بازخوانی رویدادها» (retrospective re-reading of events) و «بازآفرینی و برچسب‌گذاری» (enactment and labeling) (Weick, 1995).",
   "main_problem": "چگونه «افراد و سازمان‌ها» (individuals and organizations) «معنا» (meaning) از «تجربیات نامطمئن» (uncertain experiences) «ساخته» (create) می‌کنند و چگونه «معناسازی» (sensemaking) «واقعیت» (reality) را «شکل‌دهی» (shape) می‌کند؟",
   "mechanism": "«نظریهٔ معناسازی» (Sensemaking Theory) برپایهٔ «فرآیند ساختن معنا» (meaning-construction process) عمل می‌کند: (۱) «شناسایی نشانه» (cuing) — «افراد» (individuals) «نشانه‌ها» (cues) از «محیط» (environment) «درک» (notice) می‌کنند؛ (۲) «بازخوانی» (retrospection) — «افراد» (individuals) «رویدادها» (events) را «بازخوانی» (retrospect) می‌کنند تا «معنا» (meaning) «ساخته» (construct) کنند؛ (۳) «بازآفرینی» (enactment) — «افراد» (individuals) «واقعیت» (reality) را از طریق «عمل» (action) «بازآفرینی» (enact) می‌کنند. نتیجه: «معناسازی» (sensemaking) «فرآیندی» (process) است که «واقعیت» (reality) را «ساخته» (constructs) و «شکل‌دهی» (shapes) می‌کند.",
   "assumptions": ["«افراد» (individuals) «معنا» (meaning) از «تجربیات» (experiences) «ساخته» (construct) می‌کنند", "«معناسازی» (sensemaking) «بازخوانی‌محور» (retrospective) است — «معنا» (meaning) «بعد از» (after) «رویداد» (event) «ساخته» (constructed) می‌شود", "«افراد» (individuals) «واقعیت» (reality) را «بازآفرینی» (enact) می‌کنند"],
   "critiques": ["الگو گاه «فرآیندمحور» (process-centric) است و «عوامل ساختاری» (structural factors) را «تاریکی» (blur) می‌کند", "«معناسازی» (sensemaking) «دشوار» (difficult) برای «سنجش دقیق» (precise measurement) است", "تعمیم آن از «سازمان‌های کوچک» (small organizations) به «سازمان‌های رسانه‌ای بزرگ» (large media organizations) نیازمند بازبینی است"],
   "applications": ["تحلیل «معناسازی» (sensemaking) در «سازمان‌های رسانه‌ای» (media organizations)", "تحلیل «خبرسازی» (news construction) در «میدان روزنامه‌نگاری» (journalistic field)", "تحلیل «معناسازی» (sensemaking) در «مدیریت بحران» (crisis management)"],
   "evolution": "از Weick (1995) تا کاربرد معاصر در تحلیل «معناسازی» (sensemaking) و «ساختن واقعیت» (reality construction) در «سازمان‌های رسانه‌ای» (media organizations).",
   "key_concepts": ["معناسازی (sensemaking)", "ساختن معنا (meaning construction)", "بازخوانی (retrospection)", "بازآفرینی (enactment)"],
   "studies": ["Weick, K. E. (1995). Sensemaking in Organizations. Sage Publications."],
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
    codes = ["MC-068", "MC-063", "MC-066", "MC-070"]
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
    print("BATCH24 THEORY DONE")

if __name__ == "__main__":
    main()
