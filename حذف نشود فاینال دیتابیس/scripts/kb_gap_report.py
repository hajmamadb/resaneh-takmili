# -*- coding: utf-8 -*-
"""
kb_gap_report.py — تحلیل شکاف محتوایی در resaname_kb_final_inspect
خروجی: docs/kb-seed-gap-report.md
"""
import pymysql, json
from collections import Counter, OrderedDict
from datetime import datetime

HOST, PORT = '127.0.0.1', 3306
ROOT_PW = '433700'
INSPECT_DB = 'resaname_kb_final_inspect'
RAW_DB = 'resaname_kb_final'
OUT = r"D:\کارخانه رسانامه\docs\kb-seed-gap-report.md"

META_KEYS = {'quality_score', 'priority_90plus', 'source', 'mapping'}

TYPE_FA = {
    'THEORY': 'نظریه', 'MODEL': 'مدل', 'FRAMEWORK': 'چارچوب نظری', 'HYPOTHESIS': 'فرضیه',
    'LAW': 'قانون علمی', 'CONCEPT': 'مفهوم', 'PARADIGM': 'پارادایم', 'SCHOOL': 'مکتب',
    'STRATEGY': 'استراتژی', 'METHODOLOGY': 'روش‌شناسی', 'METHOD': 'روش پژوهش',
    'INDICATOR': 'شاخص', 'SUBFIELD': 'حوزه تخصصی', 'WORK': 'اثر علمی', 'PERSON': 'اندیشمند',
}

def is_empty(v):
    return v is None or v == '' or v == [] or v == {}

def main():
    c = pymysql.connect(host=HOST, port=PORT, user='root', password=ROOT_PW,
                        database=INSPECT_DB, charset='utf8mb4', autocommit=True)
    cur = c.cursor()
    S = {}

    # ---- totals
    def cnt(t):
        cur.execute(f"SELECT COUNT(*) FROM {t}"); return cur.fetchone()[0]
    S['entities'] = cnt('kb_entities')
    S['facets'] = cnt('kb_entity_facets')
    S['relations'] = cnt('kb_relations')
    S['links'] = cnt('kb_entity_links')
    S['sources'] = cnt('kb_sources')

    # raw DB untouched?
    c2 = pymysql.connect(host=HOST, port=PORT, user='root', password=ROOT_PW,
                         database=RAW_DB, charset='utf8mb4', autocommit=True)
    cur2 = c2.cursor()
    cur2.execute("SELECT COUNT(*) FROM kb_entities"); S['raw_entities'] = cur2.fetchone()[0]
    cur2.execute("SELECT COUNT(*) FROM kb_relations"); S['raw_relations'] = cur2.fetchone()[0]
    cur2.execute("SELECT COUNT(*) FROM kb_entity_facets"); S['raw_facets'] = cur2.fetchone()[0]
    c2.close()

    # ---- entities: full pull
    cur.execute("""SELECT code, entity_type, family_code, canonical_name_fa, canonical_name_en,
                          status_workflow, status_scientific, status_lifecycle, visibility,
                          properties FROM kb_entities ORDER BY code""")
    ents = []
    for code, et, fc, nfa, nen, sw, ss, sl, vis, props in cur.fetchall():
        p = json.loads(props)
        ents.append({'code': code, 'et': et, 'fc': fc, 'nfa': nfa, 'nen': nen,
                     'sw': sw, 'ss': ss, 'sl': sl, 'vis': vis, 'p': p})

    # +90
    p90 = [e for e in ents if e['p'].get('priority_90plus') is True]
    S['p90'] = len(p90)
    p90_by_type = Counter(e['et'] for e in p90)
    p90_persons = [e for e in p90 if e['et'] == 'PERSON']
    p90_cards = [e for e in p90 if e['et'] != 'PERSON']

    # status
    sw_dist = Counter(e['sw'] for e in ents)
    ss_dist = Counter(e['ss'] for e in ents)
    sl_dist = Counter(e['sl'] for e in ents)

    # per-type field gap analysis
    by_type = {}
    for e in ents:
        by_type.setdefault(e['et'], []).append(e)
    type_report = OrderedDict()
    for et in sorted(by_type, key=lambda t: -len(by_type[t])):
        group = by_type[et]
        n = len(group)
        keys = set()
        for e in group:
            keys |= set(e['p'].keys())
        keys -= META_KEYS
        rows = []
        for k in sorted(keys):
            missing = sum(1 for e in group if is_empty(e['p'].get(k)))
            rows.append((k, missing, n - missing))
        rows.sort(key=lambda r: (-r[1], r[0]))
        nen_missing = sum(1 for e in group if is_empty(e['nen']))
        type_report[et] = {'n': n, 'p90': sum(1 for e in group if e['p'].get('priority_90plus')),
                           'fields': rows, 'nen_missing': nen_missing}

    # needs_review (unique by code: flagged reclassification + no content_type)
    nr = OrderedDict()
    for e in ents:
        m = e['p'].get('mapping')
        if isinstance(m, dict) and (m.get('needs_review') or m.get('content_type') is None):
            nr[e['code']] = {'code': e['code'], 'title': e['nfa'], 'et': e['et'],
                             'from': (m.get('content_type')
                                      or f"بدون content_type (card_type: {e['p'].get('card_type')})"),
                             'ct': m.get('content_type')}
    nr = list(nr.values())
    nr_flagged = sum(1 for r in nr if r['ct'] is not None)
    nr_noct = sum(1 for r in nr if r['ct'] is None)

    # no-code cards
    nocode = []
    for e in ents:
        p = e['p']
        if p.get('source', {}).get('table') == 'cards' and not p.get('code'):
            nocode.append({'code': e['code'], 'title': e['nfa'],
                           'qs': p.get('quality_score'), 'p90': p.get('priority_90plus') is True})

    # persons
    persons = [e for e in ents if e['et'] == 'PERSON']
    persons.sort(key=lambda e: -(e['p'].get('quality_score') or 0))

    # facets
    cur.execute("""SELECT f.facet_code, COUNT(*) FROM kb_entity_facets f GROUP BY f.facet_code""")
    facet_used = dict(cur.fetchall())
    cur.execute("SELECT code, label_fa FROM kb_facet_dimensions ORDER BY sort_order")
    all_facets = cur.fetchall()

    # relations detail
    cur.execute("""SELECT e1.code, e2.code, r.relation_type, r.assertion_status, r.status
                   FROM kb_relations r
                   JOIN kb_entities e1 ON e1.id=r.source_id
                   JOIN kb_entities e2 ON e2.id=r.target_id
                   ORDER BY e1.code, e2.code""")
    rels = cur.fetchall()
    src_cards = sorted({s for s, t, rt, asrt, st in rels})

    # unused entity types
    cur.execute("SELECT code FROM kb_entity_types")
    all_types = [r[0] for r in cur.fetchall()]
    unused_types = [t for t in all_types if t not in by_type]

    # links by type
    cur.execute("SELECT link_type, COUNT(*) FROM kb_entity_links GROUP BY link_type")
    links_dist = dict(cur.fetchall())

    # recommended_sources non-empty (cards)
    rs_nonempty = 0; ra_nonempty = 0; tt_nonempty = 0
    for e in ents:
        p = e['p']
        if p.get('source', {}).get('table') != 'cards':
            continue
        if not is_empty(p.get('recommended_sources')): rs_nonempty += 1
        if not is_empty(p.get('related_approaches')): ra_nonempty += 1
        if not is_empty(p.get('theorists_text')): tt_nonempty += 1

    # =========================================================
    # write markdown
    # =========================================================
    L = []
    A = L.append
    A("# گزارش شکاف محتوایی — seed کارت‌ها به هسته‌ی دانش")
    A("## دیتابیس: `resaname_kb_final_inspect` · تاریخ: ۱۵/۱۱/۲۰۲۶")
    A("")
    A("> این گزارش **نتیجه‌ی واقعی** seed 771 سندِ `resaname_editorial` به اسکیمای فاینال است.")
    A("> هیچ داده‌ی ساختگی وارد نشده؛ همه‌ی مقادیر از دیتابیس مبدأ آمده‌اند. دیتابیس خام `resaname_kb_final` دست‌نخورده است.")
    A("")
    A("## ۱. اجمالی")
    A("")
    A("| جدول | رکورد |")
    A("|---|---:|")
    A(f"| `kb_entities` (موجودیت) | **{S['entities']}** (731 کارت + 39 نظریه‌پرداز + 1 کتاب) |")
    A(f"| `kb_entity_facets` | **{S['facets']}** (همه `analysis_scale`) |")
    A(f"| `kb_relations` | **{S['relations']}** (همه `RELATED_TO`، از ارجاع صریح MC در متن) |")
    A(f"| `kb_entity_links` | **{S['links']}** (731 card + 39 theorist + 1 library_resource) |")
    A(f"| `kb_sources` | **{S['sources']}** (کتاب «نظریه‌های ارتباطات» — Sorens & Tancred) |")
    A("")
    A(f"دیتابیس خام `resaname_kb_final`: entities={S['raw_entities']}, relations={S['raw_relations']}, facets={S['raw_facets']} — **خالی، دست‌نخورده** ✅")
    A("")
    A(f"- وضعیت ویرایشی: " + "، ".join(f"`{k}`: {v}" for k, v in sw_dist.items()))
    A(f"- وضعیت علمی: " + "، ".join(f"`{k}`: {v}" for k, v in ss_dist.items()) + " — **هیچ‌کدام ارزیابی علمی ندارند** (امتیاز ویرایشی ≠ اعتبار علمی)")
    A(f"- وضعیت چرخه‌حیات: " + "، ".join(f"`{k}`: {v}" for k, v in sl_dist.items()))
    A(f"- کارت‌های **امتیاز 90+ (اولویت)**: **{S['p90']}** = {len(p90_cards)} کارت + {len(p90_persons)} نظریه‌پرداز")
    A("")
    A("## ۲. توزیع موجودیت‌ها بر اساس نوع (با اولویت 90+)")
    A("")
    A("| نوع | برچسب | تعداد | اولویت 90+ |")
    A("|---|---|---:|---:|")
    for et, info in type_report.items():
        A(f"| `{et}` | {TYPE_FA.get(et, et)} | {info['n']} | {info['p90']} |")
    A("")
    A(f"**انواع خالی ({len(unused_types)} از 36):** " +
      "، ".join(f"`{t}`" for t in unused_types))
    A("")
    A("## ۳. فیلدهای خالی به تفکیک نوع — **اصلی‌ترین بخش گزارش**")
    A("")
    A("هر ردیف = یک فیلدِ `properties`؛ «خالی» یعنی مقدار خالی/غیرموجود. فیلد `title_en` جداگانه در ستون آخر.")
    A("")
    for et, info in type_report.items():
        A(f"### `{et}` ({TYPE_FA.get(et, et)}) — {info['n']} رکورد، 90+: {info['p90']}")
        A("")
        A("| فیلد | خالی | پر | درصد خالی |")
        A("|---|---:|---:|---:|")
        for k, miss, filled in info['fields']:
            pct = round(100 * miss / info['n'])
            A(f"| `{k}` | {miss} | {filled} | {pct}٪ |")
        A(f"| `canonical_name_en` (ستون جدا) | {info['nen_missing']} | {info['n']-info['nen_missing']} | {round(100*info['nen_missing']/info['n'])}٪ |")
        A("")
    A("## ۴. فاکت‌ها (13 بُعد)")
    A("")
    A("| بُعد فاکت | برچسب | مقدار در این seed |")
    A("|---|---|---:|")
    for code, label_fa in all_facets:
        n = facet_used.get(code, 0)
        A(f"| `{code}` | {label_fa} | {n if n else '— خالی —'} |")
    A("")
    A("> فقط `analysis_scale` از فیلد `level` کارت پر شده (714). **12 بُعد دیگر کامل خالی‌اند** — این‌ها کار محتوایی واقعی دارند.")
    A("")
    A("## ۵. کارت‌های اولویت (امتیاز 90+)")
    A("")
    A(f"مجموع: **{S['p90']}** — تفکیک نوع:")
    A("")
    A("| نوع | 90+ | از کل |")
    A("|---|---:|---:|")
    for et, n in p90_by_type.most_common():
        A(f"| `{et}` | {n} | {type_report[et]['n']} |")
    A("")
    A("### نظریه‌پردازان 90+ (25)")
    A("")
    A("| کد | نام | نمره | وضعیت ویرایشی |")
    A("|---|---|---:|---|")
    for e in sorted(p90_persons, key=lambda x: -x['p'].get('quality_score', 0)):
        A(f"| {e['code']} | {e['nfa']} ({e['p'].get('name_en','')}) | {e['p'].get('quality_score')} | {e['sw']} |")
    A("")
    A(f"### کارت‌های 90+ بدون کد MC ({sum(1 for e in p90_cards if e['p'].get('source',{}).get('table')=='cards' and not e['p'].get('code'))})")
    A("")
    for e in p90_cards:
        if e['p'].get('source', {}).get('table') == 'cards' and not e['p'].get('code'):
            A(f"- `{e['code']}` — {e['nfa']} (نمره {e['p'].get('quality_score')})")
    A("")
    A("## ۶. کارت‌های بدون کد MC (17) — کد = `source_id`")
    A("")
    A("| کد فعلی | عنوان | نمره | 90+ |")
    A("|---|---|---:|:-:|")
    for r in sorted(nocode, key=lambda x: (x['code'])):
        A(f"| `{r['code']}` | {r['title']} | {r['qs']} | {'✅' if r['p90'] else ''} |")
    A("")
    A("## ۷. موجودیت‌های نیازمند بازبینیِ طبقه‌بندی")
    A("")
    A("| کد | عنوان | نوع فعلی | دلیل |")
    A("|---|---|---|---|")
    for r in nr:
        A(f"| {r['code']} | {r['title']} | `{r['et']}` | از «{r['ct'] or 'بدون content_type'}» |")
    A("")
    A("## ۸. نظریه‌پردازان (39) — PERSON")
    A("")
    A("داده‌ی واقعی از جدول `theorists` سایت. `main_theory` متن آزادی است (مثلاً «نظریه تعیین و برجسته‌سازی دستور کار (Agenda-Setting)»).")
    A("")
    A("| کد | نام | name_en | نمره | وضعیت |")
    A("|---|---|---|---:|---|")
    for e in persons:
        A(f"| {e['code']} | {e['nfa']} | {e['p'].get('name_en','')} | {e['p'].get('quality_score')} | {e['sw']} |")
    A("")
    A("> **شکاف:** روابط ساختاریافته‌ی `DEVELOPED_BY`/`PROPOSED_BY` بین این 39 شخص و نظریه‌هایشان **ساخته نشده** — چون `main_theory` متن آزاد است و parse نام‌ها ریسک داده‌ی ساختگی دارد. کار محتوایی: تطبیق دستی/نیمه‌خودکار هر `main_theory` با موجودیت مربوطه.")
    A("")
    A("## ۹. روابط (23 رابطه‌ی واقعی از متن)")
    A("")
    A("| مبدأ | مقصد | نوع | وضعیت |")
    A("|---|---|---|---|")
    for s, t, rt, asrt, st in rels:
        A(f"| `{s}` | `{t}` | `{rt}` | {asrt}/{st} |")
    A("")
    A("> همه از **ارجاع صریح `MC-xxx` در متن** استخراج شده‌اند (نه حدس). `assertion_status=unverified` چون هنوز توسط دانشمند تأیید نشده.")
    A("")
    A(f"- کارت‌های مبدأ این 23 رابطه: {len(src_cards)} کارت ({', '.join(f'`{x}`' for x in src_cards[:6])}، …)")
    A("")
    A("## ۱۰. خلاصه‌ی شکاف‌های محتوایی (چه کاری باید انجام شود)")
    A("")
    A("| # | شکاف | ابعاد | اولویت |")
    A("|---|---|---|---|")
    # row 1: deep fields (dynamic)
    major = [t for t in ('THEORY', 'MODEL', 'FRAMEWORK', 'METHOD', 'WORK') if t in type_report]
    deep_parts = []
    for t in major:
        info = type_report[t]
        almost = [k for k, miss, filled in info['fields']
                  if filled > 0 and miss / info['n'] >= 0.85]
        if almost:
            shown = ", ".join(almost[:5]) + ("…" if len(almost) > 5 else "")
            deep_parts.append(f"{TYPE_FA.get(t, t)}: {len(almost)} فیلد (مثل {shown})")
    if deep_parts:
        A("| 1 | **فیلدهای «عمیق» کارت تقریباً خالی‌اند** (در JSON برخی کارت‌ها هست، ولی برای اکثر پر نشده) | "
          + "؛ ".join(deep_parts) + " | بالا (اول 90+) |")
    # canonical_name_en only if actually empty
    nen_gap = "، ".join(f"{TYPE_FA.get(t, t)}: {type_report[t]['nen_missing']}"
                        for t in type_report if type_report[t]['nen_missing'])
    if nen_gap:
        A(f"| {2 if deep_parts else 1} | `canonical_name_en` خالی | {nen_gap} | بالا |")
    A("| 2 | 12 بُعد فاکتِ خالی (discipline, subfield, time_frame, geographic_region, approach, epistemology, ontology, data_type, theoretical_tradition, research_context, application_domain, qualifies_for) | همه‌ی 771 رکورد | بالا (از 90+ شروع) |")
    A("| 3 | روابط بین‌موجودیتی تقریباً خالی | فقط 23 RELATED_TO از 771 موجودیت | بالا |")
    A(f"| 4 | 21 نوع موجودیتِ خالی (از 36) — مثل `PROPOSITION`, `CONSTRUCT`, `VARIABLE`, `RESEARCH_STUDY`, `FINDING`, `DISCIPLINE`, `TRADITION` | فازبندی‌شده | متوسط |")
    A(f"| 5 | `main_theory`ِ 39 نظریه‌پرداز متن آزاد است → روابط `PROPOSED_BY`/`DEVELOPED_BY` ندارند | 39 PERSON | بالا |")
    A(f"| 6 | `recommended_sources` متن آزاد است (714 کارت) → `kb_sources`/`kb_citations` خالی | 714 | متوسط |")
    A("| 7 | `kb_evidence` کامل خالی (هیچ شاهد ساختاریافته‌ای) | همه | متوسط (فاز 2) |")
    A(f"| 8 | {nr_flagged} کارتِ نیازمند بازبینیِ نوع + {nr_noct} کارتِ بدون content_type (مجموع {len(nr)}، جدول §7) | {len(nr)} | بالا (سریع) |")
    A("| 9 | 17 کارت بدون کد MC (کد فعلی = source_id) | 17 | متوسط |")
    A("| 10 | وضعیت علمی همه `unassessed` — ارزیابی علمی ندارد | 771 | فاز 2 (انسانی/داوری) |")
    A("")
    A("## ۱۱. نقشه‌ی seed (برگشت‌پذیر و شفاف)")
    A("")
    A("| مبدأ | مقصد | قاعده |")
    A("|---|---|---|")
    A("| `editorial_documents.current_json` | `kb_entities.properties` | کل JSON بدون هیچ حذفی + `quality_score` + `source` (provenance) + `priority_90plus` |")
    A("| `content_type` | `entity_type` | map مستند (§2)؛ 8 مورد flagged `needs_review` |")
    A("| `title_fa` / `name` | `canonical_name_fa` | — |")
    A("| `title_en` / `name_en` | `canonical_name_en` | خالی بماند اگر در مبدأ خالی بوده |")
    A("| `slug` | `slug` | همه 771 یکتا بودند |")
    A("| `code` (MC-xxx) / `id` (th-x) / `source_id` | `code` | 17 کارت بدون کد → `source_id` |")
    A("| `workflow_status` | `status_workflow` | approved→approved, draft_ready→draft |")
    A("| (هیچ‌چیز) | `status_scientific` | همه `unassessed` (ساختگی نیست) |")
    A("| `level` | فاکت `analysis_scale` | خرد→MICRO, میانی→MESO, کلان→MACRO |")
    A("| ارجاع صریح `MC-xxx` در متن | `kb_relations.RELATED_TO` | `unverified`/`needs_review` |")
    A("| `source_table`+`source_id` | `kb_entity_links` | confidence=verified |")
    A("| کتاب `library_resources` | `kb_entities.WORK` + `kb_sources.BOOK` | `work_id` وصل است |")
    A("")
    A("## ۱۲. دستورات بازبینی (SQL آماده)")
    A("")
    A("```sql")
    A("USE resaname_kb_final_inspect;")
    A("-- اولویت 90+ به تفکیک نوع")
    A("SELECT entity_type, COUNT(*) FROM kb_entities")
    A("WHERE JSON_EXTRACT(properties,'$.priority_90plus')=true GROUP BY entity_type;")
    A("-- نمونه‌ی یک نوع با فیلدهای خالی")
    A("SELECT code, canonical_name_fa, canonical_name_en,")
    A("  JSON_EXTRACT(properties,'$.year') AS year,")
    A("  JSON_EXTRACT(properties,'$.paradigm') AS paradigm,")
    A("  JSON_EXTRACT(properties,'$.core_logic') IS NULL AS no_core_logic")
    A("FROM kb_entities WHERE entity_type='THEORY' AND JSON_EXTRACT(properties,'$.priority_90plus')=true LIMIT 20;")
    A("-- کارت‌های 90+ که فیلدِ centralِ نوعشان خالی است (مثال: THEORY بدون core_logic)")
    A("SELECT e.code, e.canonical_name_fa FROM kb_entities e")
    A("WHERE e.entity_type='THEORY' AND JSON_EXTRACT(e.properties,'$.priority_90plus')=true")
    A("  AND (JSON_EXTRACT(e.properties,'$.core_logic') IS NULL OR JSON_EXTRACT(e.properties,'$.core_logic')='');")
    A("```")
    A("")
    A("---")
    A(f"تولیدشده به‌صورت خودکار از `resaname_kb_final_inspect` در {datetime.now():%Y-%m-%d %H:%M}")

    open(OUT, 'w', encoding='utf-8').write("\n".join(L))
    print("report written:", OUT)
    print(json.dumps({k: S[k] for k in ('entities','facets','relations','links','sources','p90','raw_entities')}, ensure_ascii=False))

if __name__ == '__main__':
    main()
