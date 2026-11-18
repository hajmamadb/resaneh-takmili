# -*- coding: utf-8 -*-
"""
بلوک «روابط دانش بین بلوک‌ها + ساختارهای تکمیلی»
فقط روابط بین‌بلوکی تولید می‌کند که در بلوک‌های قبلی ثبت نشده‌اند.
تمام idها از فایل‌های بلوک‌های قبلی گرفته می‌شوند تا اشتباه تایپی رخ ندهد.
"""
import json, os

DATA = os.path.join(os.path.dirname(__file__), "..", "data")
OUT  = os.path.join(DATA, "kg_data_relations.json")

files = ["kg_data_theories.json","kg_data_schools.json","kg_data_schools-critical.json",
         "kg_data_paradigms.json","kg_data_designs.json","kg_data_collection.json",
         "kg_data_analysis-quant.json","kg_data_analysis-qual.json","quality-ethics-tools.json"]

idmap={}   # id -> (entity_type, title_fa)
titles={}  # id -> title_fa
existing=set()  # (source,target,type) already recorded in prior blocks
for f in files:
    d=json.load(open(os.path.join(DATA,f),encoding="utf-8"))
    for e in d.get("entities",[]):
        idmap[e["id"]]=(e.get("entity_type"),e.get("title_fa"))
        titles[e["id"]]=e.get("title_fa")
    for r in d.get("relations",[]):
        existing.add((r["source_id"],r["target_id"],r["relation_type"]))

REL=[]
def add(s,t,rt,desc,conf):
    REL.append({"source_id":s,"target_id":t,"relation_type":rt,
                "description":desc,"confidence":conf,"verification_status":"unverified"})

def must(x):
    assert x in idmap, "UNKNOWN ID: "+x
    return x

def T(s):  # must exist
    return must(s)

# ---------- helper: all ids of a type ----------
def ids_of(etype):
    return [i for i,(ty,_) in idmap.items() if ty==etype]

THEORY = set(ids_of("THEORY"))
MODEL  = set(ids_of("MODEL"))
FRAMEW = set(ids_of("FRAMEWORK"))
DESIGN = set(ids_of("DESIGN"))
ANALY  = set(ids_of("ANALYSIS"))
SCHOOL = set(ids_of("SCHOOL"))
PARA   = set(ids_of("PARADIGM"))
APPR   = set(ids_of("APPROACH"))
SOFT   = set(ids_of("SOFTWARE"))
SUBF   = set(ids_of("SUBFIELD"))
TRAD   = set(ids_of("TRADITION"))

# ============================================================
# 1) THEORY/MODEL/FRAMEWORK -> BELONGS_TO -> SUBFIELD  (فقط موارد ثبت‌نشده)
# ============================================================
belong_map = {
    # حوزه ۱: اثرات رسانه
    T("kg-theory-magic-bullet"):"kg-subfield-media-effects",
    T("kg-theory-two-step"):"kg-subfield-media-effects",
    T("kg-theory-uses-and-gratifications"):"kg-subfield-media-effects",
    T("kg-theory-agenda-setting"):"kg-subfield-media-effects",
    T("kg-theory-framing"):"kg-subfield-media-effects",
    T("kg-theory-cultivation"):"kg-subfield-media-effects",
    T("kg-theory-dependence"):"kg-subfield-media-effects",
    T("kg-theory-knowledge-gap"):"kg-subfield-media-effects",
    T("kg-theory-third-person"):"kg-subfield-media-effects",
    # حوزه ۲: جامعه و رسانه
    T("kg-theory-network-society"):"kg-subfield-society-media",
    T("kg-theory-information-society"):"kg-subfield-society-media",
    T("kg-theory-mass-society"):"kg-subfield-society-media",
    T("kg-theory-culture-industry"):"kg-subfield-society-media",
    T("kg-theory-public-sphere"):"kg-subfield-society-media",
    T("kg-theory-cultural-imperialism"):"kg-subfield-society-media",
    T("kg-theory-media-globalization"):"kg-subfield-society-media",
    # حوزه ۳: مخاطب و دریافت
    T("kg-theory-encoding-decoding"):"kg-subfield-audience-reception",
    T("kg-theory-reception"):"kg-subfield-audience-reception",
    T("kg-theory-active-audience"):"kg-subfield-audience-reception",
    T("kg-theory-resisting-audience"):"kg-subfield-audience-reception",
    T("kg-theory-media-consumption"):"kg-subfield-audience-reception",
    T("kg-theory-audience-participation"):"kg-subfield-audience-reception",
    # حوزه ۴: ارتباطات بین‌فردی
    T("kg-theory-expectancy-violation"):"kg-subfield-interpersonal",
    T("kg-theory-sensemaking"):"kg-subfield-interpersonal",
    T("kg-theory-uncertainty-reduction"):"kg-subfield-interpersonal",
    T("kg-theory-social-penetration"):"kg-subfield-interpersonal",
    T("kg-theory-social-exchange"):"kg-subfield-interpersonal",
    T("kg-theory-communication-management"):"kg-subfield-interpersonal",
    # حوزه ۵: ارتباطات سیاسی
    T("kg-theory-political-agenda"):"kg-subfield-political",
    T("kg-theory-political-framing"):"kg-subfield-political",
    T("kg-theory-political-advertising"):"kg-subfield-political",
    T("kg-theory-political-spiral"):"kg-subfield-political",
    T("kg-theory-political-public-sphere"):"kg-subfield-political",
    T("kg-theory-policy-brokerage"):"kg-subfield-political",
    T("kg-theory-election-communication"):"kg-subfield-political",
    # حوزه ۶: رسانه‌های دیجیتال
    T("kg-theory-media-convergence"):"kg-subfield-digital-media",
    T("kg-theory-participatory-culture"):"kg-subfield-digital-media",
    T("kg-theory-platformization"):"kg-subfield-digital-media",
    T("kg-theory-attention-economy"):"kg-subfield-digital-media",
    T("kg-theory-networked-communication"):"kg-subfield-digital-media",
    T("kg-theory-algorithmic-agency"):"kg-subfield-digital-media",
    T("kg-theory-choice-architecture"):"kg-subfield-digital-media",
    T("kg-theory-platform-society"):"kg-subfield-digital-media",
    # مدل‌ها (۱۳.۱ تا ۱۳.۶)
    T("kg-model-onion-model"):"kg-subfield-interpersonal",
    T("kg-model-three-positions"):"kg-subfield-audience-reception",
    T("kg-model-convergence-model"):"kg-subfield-digital-media",
    T("kg-model-nudge-model"):"kg-subfield-digital-media",
    T("kg-model-surveillance-capitalism"):"kg-subfield-digital-media",
    # چارچوب‌های نظری (بخش ۱۳)
    T("kg-framework-two-flow"):"kg-subfield-media-effects",
    T("kg-framework-uses-gratifications"):"kg-subfield-media-effects",
    T("kg-framework-cultivation-analysis"):"kg-subfield-media-effects",
    T("kg-framework-political-framing"):"kg-subfield-political",
    T("kg-framework-public-sphere"):"kg-subfield-society-media",
    T("kg-framework-participatory"):"kg-subfield-digital-media",
    # چارچوب‌های مکاتب (بخش ۱) که هنوز بدون BELONGS_TO هستند
    T("kg-framework-culture-industry"):"kg-subfield-society-media",
    T("kg-framework-representation"):"kg-subfield-audience-reception",
    T("kg-framework-symbolic-interaction"):"kg-subfield-interpersonal",
    T("kg-framework-communication-systems"):"kg-subfield-interpersonal",
    T("kg-framework-systemic-approach"):"kg-subfield-interpersonal",
    T("kg-framework-media-bias"):"kg-subfield-society-media",
    T("kg-framework-medium-extension"):"kg-subfield-society-media",
    T("kg-framework-media-environment"):"kg-subfield-society-media",
    T("kg-framework-media-effects"):"kg-subfield-media-effects",
    T("kg-framework-structuralism"):"kg-subfield-audience-reception",
    T("kg-framework-saussurian-semiotics"):"kg-subfield-audience-reception",
    T("kg-framework-peircean-semiotics"):"kg-subfield-audience-reception",
    T("kg-framework-social-semiotics"):"kg-subfield-audience-reception",
    T("kg-framework-discourse-analysis"):"kg-subfield-audience-reception",
    T("kg-framework-critical-discourse"):"kg-subfield-political",
    T("kg-framework-meta-narrative-critique"):"kg-subfield-audience-reception",
    T("kg-framework-postmodern-media"):"kg-subfield-digital-media",
}
for src,sub in belong_map.items():
    add(src, must(sub), "BELONGS_TO",
        f"«{titles[src]}» در حوزه‌ی تخصصی «{titles[must(sub)]}» جای می‌گیرد", 0.9)

# ============================================================
# 2) PARADIGM -> INFLUENCED_BY -> TRADITION  (مبانی فلسفی بخش ۲)
# ============================================================
trad_base = {
    T("kg-paradigm-critical"): T("kg-tradition-critical-theory"),   # سنت انتقادی مارکسیستی
    T("kg-paradigm-constructivism"): T("kg-tradition-post-structuralism"),  # برساخت‌گرایی <- پساساختارگرایی
    T("kg-paradigm-postcolonial"): T("kg-tradition-postcolonial"),   # مطالعات پسااستعماری
    T("kg-paradigm-decolonial") if "kg-paradigm-decolonial" in idmap else T("kg-paradigm-participatory"): None,
}
# (decolonial paradigm does not exist; drop)
trad_base.pop(T("kg-paradigm-participatory"),None)
for p,tr in trad_base.items():
    if tr:
        add(p, tr, "INFLUENCED_BY",
            f"پارادایم «{titles[p]}» بر سنت فکری «{titles[tr]}» استوار است", 0.9)

# ============================================================
# 3) DESIGN -> USES -> TECHNIQUE  (مهارت‌های گردآوری، فقط موارد ثبت‌نشده)
# ============================================================
design_uses = {
    T("kg-design-experimental"):[T("kg-technique-structured-observation"),T("kg-technique-structured-interview")],
    T("kg-design-nonexperimental"):[T("kg-technique-structured-interview"),T("kg-technique-direct-observation"),T("kg-technique-focus-group")],
    T("kg-design-survey"):[T("kg-technique-delfi"),T("kg-technique-group-interview")],
    T("kg-design-case-study"):[T("kg-technique-participant-observation"),T("kg-technique-naturalistic-observation"),T("kg-technique-in-depth-interview"),T("kg-technique-archival-analysis")],
    T("kg-design-historical"):[T("kg-technique-official-document-analysis"),T("kg-technique-archival-analysis")],
    T("kg-design-ethnographic"):[T("kg-technique-field-observation"),T("kg-technique-naturalistic-observation"),T("kg-technique-participant-observation"),T("kg-technique-digital-observation")],
    T("kg-design-phenomenological"):[T("kg-technique-in-depth-interview"),T("kg-technique-group-interview")],
    T("kg-design-grounded-theory"):[T("kg-technique-semistructured-interview"),T("kg-technique-participant-observation"),T("kg-technique-archival-analysis")],
    T("kg-design-narrative"):[T("kg-technique-in-depth-interview"),T("kg-technique-group-interview")],
    T("kg-design-action-research"):[T("kg-technique-participant-observation"),T("kg-technique-focus-group"),T("kg-technique-questionnaire")],
    T("kg-design-comparative"):[T("kg-technique-official-document-analysis"),T("kg-technique-text-analysis")],
    T("kg-design-evaluation"):[T("kg-technique-satisfaction-measurement"),T("kg-technique-recognition-measurement"),T("kg-technique-structured-observation")],
    T("kg-design-design-based"):[T("kg-technique-participant-observation"),T("kg-technique-attention-measurement")],
    T("kg-design-computational"):[T("kg-technique-digital-log-analysis"),T("kg-technique-sensor-data"),T("kg-technique-digital-footprint-analysis")],
}
for des,techs in design_uses.items():
    for te in techs:
        add(des, te, "USES",
            f"طرح «{titles[des]}» از فن گردآوری «{titles[te]}» استفاده می‌کند", 0.9)

# ============================================================
# 4) ANALYSIS -> USES -> SOFTWARE  (نرم‌افزار، فقط موارد ثبت‌نشده)
# ============================================================
analysis_soft = {
    # کمّی
    T("kg-analysis-mean"):T("kg-software-spss"),
    T("kg-analysis-median"):T("kg-software-spss"),
    T("kg-analysis-mode"):T("kg-software-spss"),
    T("kg-analysis-variance"):T("kg-software-r-lang"),
    T("kg-analysis-standard-deviation"):T("kg-software-r-lang"),
    T("kg-analysis-hypothesis-testing"):T("kg-software-stata"),
    T("kg-analysis-confidence-interval"):T("kg-software-sas"),
    T("kg-analysis-t-test"):T("kg-software-spss"),
    T("kg-analysis-anova"):T("kg-software-spss"),
    T("kg-analysis-manova"):T("kg-software-sas"),
    T("kg-analysis-chi-square"):T("kg-software-stata"),
    T("kg-analysis-mann-whitney"):T("kg-software-spss"),
    T("kg-analysis-wilcoxon"):T("kg-software-spss"),
    T("kg-analysis-kruskal-wallis"):T("kg-software-stata"),
    T("kg-analysis-pearson"):T("kg-software-python"),
    T("kg-analysis-spearman"):T("kg-software-r-lang"),
    T("kg-analysis-kendall"):T("kg-software-r-lang"),
    T("kg-analysis-linear-regression"):T("kg-software-spss"),
    T("kg-analysis-logistic-regression"):T("kg-software-stata"),
    T("kg-analysis-multiple-regression"):T("kg-software-sas"),
    T("kg-analysis-multilevel-regression"):T("kg-software-r-lang"),
    T("kg-analysis-sem"):T("kg-software-amos"),
    T("kg-analysis-path-analysis"):T("kg-software-smartpls"),
    T("kg-analysis-factorial-models"):T("kg-software-lavaan"),
    T("kg-analysis-growth-models"):T("kg-software-lavaan"),
    T("kg-analysis-panel-data"):T("kg-software-stata"),
    T("kg-analysis-factor-analysis"):T("kg-software-sas"),
    T("kg-analysis-cluster-analysis"):T("kg-software-spss"),
    T("kg-analysis-discriminant-analysis"):T("kg-software-sas"),
    T("kg-analysis-causal-models"):T("kg-software-r-lang"),
    T("kg-analysis-causal-inference"):T("kg-software-python"),
    T("kg-analysis-difference-in-differences"):T("kg-software-stata"),
    T("kg-analysis-bayesian-inference"):T("kg-software-python"),
    T("kg-analysis-hierarchical-modeling"):T("kg-software-r-lang"),
    T("kg-analysis-arima"):T("kg-software-r-lang"),
    T("kg-analysis-trend-seasonal-decomposition"):T("kg-software-python"),
    # کیفی
    T("kg-analysis-qual-thematic-inductive"):T("kg-software-nvivo"),
    T("kg-analysis-qual-thematic-deductive"):T("kg-software-atlas-ti"),
    T("kg-analysis-qual-thematic-reflexive"):T("kg-software-maxqda"),
    T("kg-analysis-qual-content-conventional"):T("kg-software-nvivo"),
    T("kg-analysis-qual-content-directed"):T("kg-software-maxqda"),
    T("kg-analysis-qual-content-deductive-heinze"):T("kg-software-atlas-ti"),
    T("kg-analysis-qual-discourse-critical"):T("kg-software-maxqda"),
    T("kg-analysis-qual-discourse-foucauldian"):T("kg-software-atlas-ti"),
    T("kg-analysis-qual-discourse-laclau-mouffe"):T("kg-software-nvivo"),
    T("kg-analysis-qual-narrative-structural"):T("kg-software-nvivo"),
    T("kg-analysis-qual-narrative-episodes"):T("kg-software-atlas-ti"),
    T("kg-analysis-qual-narrative-functionalist"):T("kg-software-maxqda"),
    T("kg-analysis-qual-semiotic-saussurean"):T("kg-software-nvivo"),
    T("kg-analysis-qual-semiotic-peircean"):T("kg-software-atlas-ti"),
    T("kg-analysis-qual-semiotic-barthes"):T("kg-software-nvivo"),
    T("kg-analysis-qual-semiotic-social"):T("kg-software-maxqda"),
    T("kg-analysis-qual-conversation-sequence"):T("kg-software-nvivo"),
    T("kg-analysis-qual-conversation-turn-taking"):T("kg-software-atlas-ti"),
    T("kg-analysis-qual-conversation-interaction-order"):T("kg-software-maxqda"),
    T("kg-analysis-qual-phenomenological-ipa"):T("kg-software-nvivo"),
    T("kg-analysis-qual-phenomenological-descriptive"):T("kg-software-atlas-ti"),
    T("kg-analysis-qual-grounded-open"):T("kg-software-maxqda"),
    T("kg-analysis-qual-grounded-axial"):T("kg-software-nvivo"),
    T("kg-analysis-qual-grounded-selective"):T("kg-software-atlas-ti"),
    T("kg-analysis-qual-interpretive-hermeneutic"):T("kg-software-maxqda"),
    T("kg-analysis-qual-interpretive-text"):T("kg-software-nvivo"),
    T("kg-analysis-qual-visual-image"):T("kg-software-nvivo"),
    T("kg-analysis-qual-visual-framing"):T("kg-software-atlas-ti"),
    T("kg-analysis-qual-visual-composition"):T("kg-software-maxqda"),
    T("kg-analysis-qual-documentary-historical"):T("kg-software-nvivo"),
    T("kg-analysis-qual-documentary-critical"):T("kg-software-atlas-ti"),
    # محاسباتی / شبکه‌ای (سند: بخش ۹.۳)
    T("kg-technique-big-data-analysis") if "kg-technique-big-data-analysis" in idmap else T("kg-analysis-cluster-analysis"): T("kg-software-python"),
    T("kg-analysis-cluster-analysis"):T("kg-software-gephi"),
    T("kg-analysis-factor-analysis"):T("kg-software-ucinet"),
}
# dedupe: keep first mapping per analysis id
seen_a={}
for a,s in analysis_soft.items():
    if a in seen_a: continue
    seen_a[a]=s
for a,s in seen_a.items():
    add(a, s, "USES",
        f"روش تحلیل «{titles[a]}» با نرم‌افزار «{titles[s]}» اجرا می‌شود", 0.85)

# ============================================================
# 5) SCHOOL -> INFLUENCED -> THEORY  (نظریه‌های متأثر)
# ============================================================
school_infl = {
    T("kg-school-frankfurt"):[T("kg-theory-culture-industry"),T("kg-theory-public-sphere"),T("kg-theory-mass-society")],
    T("kg-school-birmingham"):[T("kg-theory-encoding-decoding"),T("kg-theory-reception"),T("kg-theory-active-audience"),T("kg-theory-resisting-audience")],
    T("kg-school-chicago"):[T("kg-theory-two-step"),T("kg-theory-magic-bullet")],
    T("kg-school-palo-alto"):[T("kg-theory-sensemaking"),T("kg-theory-communication-management")],
    T("kg-school-toronto"):[T("kg-theory-media-convergence"),T("kg-theory-attention-economy")],
}
for sc,th in school_infl.items():
    for t in th:
        add(sc, t, "INFLUENCED",
            f"مکتب «{titles[sc]}» بر شکل‌گیری «{titles[t]}» تأثیر گذاشت", 0.9)

# ============================================================
# 6) APPROACH -> RELATED_TO -> PARADIGM  (فقط موارد ثبت‌نشده)
# ============================================================
# ثبت‌شده بودند: quant<-positivism, quant<-postpos, qual<-interp, qual<-construct,
#                mixed<-pragmatism, mixed<-realism, comp<-critical/participatory/feminist/postcolonial
approach_rel = {
    T("kg-approach-quantitative"):T("kg-paradigm-realism"),        # واقع‌گرایی علمی <-> کمّی
    T("kg-approach-qualitative"):T("kg-paradigm-interpretivism"),  # تقویت (ثبت‌شده بود؟ بله interp) -> skip? ثبت شده؛ نگذار
    T("kg-approach-mixed-methods"):T("kg-paradigm-positivism"),    # آمیخته با اثبات‌گرایی
    T("kg-approach-mixed-methods"):T("kg-paradigm-postpositivism"),
    T("kg-approach-complementary"):T("kg-paradigm-pragmatism"),    # رویکردهای مکمل با پراگماتیسم
}
for a,p in approach_rel.items():
    if a==T("kg-approach-qualitative") and p==T("kg-paradigm-interpretivism"):
        continue  # قبلاً INFLUENCED_BY ثبت شده
    add(a, p, "RELATED_TO",
        f"رویکرد «{titles[a]}» با پارادایم «{titles[p]}» مرتبط است", 0.8)

# ============================================================
# 7) مناقشات علمی (بخش ۱۹.۸) -> CRITICIZES / CONTRADICTS  (فقط موارد ثبت‌نشده)
# ============================================================
disputes = [
    (T("kg-theory-magic-bullet"), T("kg-theory-uses-and-gratifications"), "CONTRADICTS",
     "نظریه‌ی تزریقی با دید مخاطب فعال در نظریه‌ی استفاده و رضامندی متناقض است", 0.85),
    (T("kg-theory-cultivation"), T("kg-theory-active-audience"), "CRITICIZES",
     "نظریه‌ی کاشت با تأکید بر اثرات بلندمدت، مدل مخاطب فعال را به چالش می‌کشد", 0.75),
    (T("kg-theory-spiral-silence"), T("kg-theory-public-sphere"), "CRITICIZES",
     "مارپیچ سکوت با فرض هومانی فضای عمومی بر ایده‌ی گفت‌وگوی آزاد نقد وارد می‌کند", 0.72),
    (T("kg-theory-culture-industry"), T("kg-theory-participatory-culture"), "CONTRADICTS",
     "نقد صنعت فرهنگ (مخاطب منفعل) با فرهنگ مشارکتی (مخاطب فعال) در تناقض است", 0.82),
    (T("kg-theory-network-society"), T("kg-theory-mass-society"), "CRITICIZES",
     "نظریه‌ی جامعه شبکه‌ای، مدل جامعه توده‌ای را ناکافی می‌داند", 0.8),
    (T("kg-theory-platform-society"), T("kg-theory-information-society"), "EXTENDS",
     "جامعه پلتفرمی، جامعه اطلاعاتی را با محوریت پلتفرم‌ها گسترش می‌دهد", 0.8),
    (T("kg-model-surveillance-capitalism"), T("kg-theory-attention-economy"), "CRITICIZES",
     "سرمایه‌داری نظارتی، اقتصاد توجه را به اقتصاد داده و پیش‌بینی رفتار ارتقا می‌دهد", 0.78),
    (T("kg-concept-hyperreality"), T("kg-theory-cultivation"), "CRITICIZES",
     "فراواقعیت با تأکید بر شبیه‌سازی، مدل کاشت را در بستر رسانه‌های دیجیتال نقد می‌کند", 0.7),
    (T("kg-framework-critical-discourse"), T("kg-framework-discourse-analysis"), "EXTENDS",
     "تحلیل گفتمان انتقادی، تحلیل گفتمان را با بُعد قدرت و ایدئولوژی گسترش می‌دهد", 0.88),
    (T("kg-tradition-post-structuralism"), T("kg-framework-structuralism"), "CONTRADICTS",
     "پساساختارگرایی با ساختارگرایی در مسئله‌ی ثبات معنا متناقض است", 0.86),
    (T("kg-approach-quantitative"), T("kg-approach-qualitative"), "COMPARED_WITH",
     "رویکرد کمّی و کیفی به‌عنوان دو منطق رقیب/مکمل قابل مقایسه‌اند", 0.85),
    (T("kg-paradigm-positivism"), T("kg-paradigm-constructivism"), "CONTRADICTS",
     "اثبات‌گرایی (واقعیت عینی) با برساخت‌گرایی (واقعیت ساخته‌شده) در تناقض معرفت‌شناختی است", 0.87),
]
for s,t,rt,desc,conf in disputes:
    add(s,t,rt,desc,conf)

# ============================================================
# 8) ساختارهای تکمیلی (بخش ۱۹): پیوند موجودیت‌ها به حوزه‌های کاربردی/مفاهیم
#    - حوزه‌های کاربردی (۱۹.۷): THEORY -> APPLIES_TO -> SUBFIELD (کاربردی)
# ============================================================
# بخش ۱۴ (روش‌های اختصاصی) -> APPLIES_TO -> SUBFIELD  (حوزه‌های کاربردی)
app_sub = {
    T("kg-technique-tech-journalism"):T("kg-subfield-media-effects"),
    T("kg-technique-tech-advertising"):T("kg-subfield-media-effects"),
    T("kg-technique-tech-pr"):T("kg-subfield-society-media"),
    T("kg-technique-tech-audience"):T("kg-subfield-audience-reception"),
    T("kg-technique-tech-social-media"):T("kg-subfield-digital-media"),
    T("kg-technique-tech-digital-media"):T("kg-subfield-digital-media"),
    T("kg-technique-tech-political-comm"):T("kg-subfield-political"),
    T("kg-technique-tech-crisis-comm"):T("kg-subfield-society-media"),
    T("kg-technique-tech-film-tv"):T("kg-subfield-audience-reception"),
    T("kg-technique-tech-development-comm"):T("kg-subfield-society-media"),
}
for s,sub in app_sub.items():
    add(s, must(sub), "APPLIES_TO",
        f"«{titles[s]}» کاربرد در حوزه‌ی «{titles[must(sub)]}» دارد", 0.8)

# نظریه‌های کلان -> APPLIES_TO حوزه‌های کاربردی (بخش ۱۹.۷)
theory_app = [
    (T("kg-theory-framing"), T("kg-subfield-political"), "چارچوب‌سازی در مطالعات ارتباطات سیاسی کاربرد دارد", 0.85),
    (T("kg-theory-media-convergence"), T("kg-subfield-digital-media"), "همگرایی رسانه‌ای در مطالعات رسانه‌های دیجیتال کاربرد دارد", 0.85),
    (T("kg-theory-participatory-culture"), T("kg-subfield-digital-media"), "فرهنگ مشارکتی در مطالعات شبکه‌های اجتماعی کاربرد دارد", 0.85),
    (T("kg-theory-public-sphere"), T("kg-subfield-political"), "حوزه‌ی عمومی در ارتباطات سیاسی و حکمرانی رسانه کاربرد دارد", 0.82),
    (T("kg-theory-cultivation"), T("kg-subfield-audience-reception"), "کاشت در مطالعات مخاطب و اثرات بلندمدت کاربرد دارد", 0.8),
    (T("kg-theory-uses-and-gratifications"), T("kg-subfield-audience-reception"), "استفاده و رضامندی در مطالعات مصرف رسانه کاربرد دارد", 0.85),
]
for s,t,desc,conf in theory_app:
    add(s,must(t),"APPLIES_TO",desc,conf)

# ---------- validate ----------
unknown=[]
for r in REL:
    for k in ("source_id","target_id"):
        if r[k] not in idmap:
            unknown.append((r[k],r["relation_type"]))
if unknown:
    raise SystemExit("UNKNOWN IDS: "+str(unknown))

# dedupe + drop relations already recorded in prior blocks
seen=set(); final=[]; dropped=0
for r in REL:
    key=(r["source_id"],r["target_id"],r["relation_type"])
    if key in seen: continue
    if key in existing:  # already recorded in a prior block
        dropped+=1; continue
    seen.add(key); final.append(r)

out={"entities":[], "relations":final}
os.makedirs(DATA,exist_ok=True)
with open(OUT,"w",encoding="utf-8") as f:
    json.dump(out,f,ensure_ascii=False,indent=2)
print("WROTE",OUT)
print("relations:",len(final))
import collections
c=collections.Counter(r["relation_type"] for r in final)
print(dict(c))
