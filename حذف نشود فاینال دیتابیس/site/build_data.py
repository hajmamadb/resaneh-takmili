# -*- coding: utf-8 -*-
"""Export resaname_kb_final_inspect into static JSON bundles for the site."""
import pymysql, json, os, collections, decimal, datetime

DB = 'resaname_kb_final_inspect'
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'web', 'data')
os.makedirs(OUT, exist_ok=True)

c = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='433700',
                    database=DB, charset='utf8mb4')
cur = c.cursor()

TYPE_FA = {
    'THEORY': 'نظریه', 'MODEL': 'مدل', 'FRAMEWORK': 'چارچوب نظری', 'HYPOTHESIS': 'فرضیه',
    'LAW': 'قانون علمی', 'CONCEPT': 'مفهوم', 'PERSON': 'اندیشمند / نظریه‌پرداز',
    'WORK': 'اثر علمی', 'PARADIGM': 'پارادایم', 'METHOD': 'روش پژوهش',
    'METHODOLOGY': 'روش‌شناسی', 'STRATEGY': 'استراتژی', 'INDICATOR': 'شاخص',
    'SUBFIELD': 'حوزه تخصصی', 'SCHOOL': 'مکتب فکری', 'DISCIPLINE': 'رشته علمی',
    'TRADITION': 'سنت فکری', 'DISPUTE': 'مناقشه علمی', 'CONSTRUCT': 'سازه نظری',
    'PROPOSITION': 'گزاره علمی', 'VARIABLE': 'متغیر',
}
FAMILY_FA = {
    'THEORETICAL_SYSTEM': 'نظام فکری و پارادایمی',
    'KNOWLEDGE_STRUCTURE': 'ساختارهای نظری و مفهومی',
    'SCIENTIFIC_DOMAIN': 'قلمروهای علمی و مناقشات',
    'RESEARCH_METHODOLOGY': 'نظام روش‌شناختی',
    'RESEARCH_ACTIVITY': 'فعالیت و خروجی پژوهش',
    'RESEARCH_RESOURCE': 'منابع و زیرساخت',
    'INTELLECTUAL_AGENT': 'کنشگران علمی',
    'SCIENTIFIC_ARGUMENTATION': 'استدلال علمی',
}
REL_FA = {
    'RELATED_TO': 'مرتبط با', 'PROPOSED_BY': 'مطرح‌شده توسط', 'DEVELOPED_BY': 'توسعه‌یافته توسط',
    'AUTHORED_BY': 'تالیف‌شده توسط', 'CRITICIZES': 'نقد می‌کند', 'INFLUENCED_BY': 'تأثیرپذیر از',
    'INFLUENCED': 'تأثیرگذار بر', 'EXTENDS': 'توسعه‌دهنده‌ی', 'CONTRADICTS': 'متضاد با',
    'APPLIES_TO': 'کاربرد در', 'TESTED_IN': 'آزمون‌شده در', 'SUPPORTED_BY': 'پشتیبانی از',
    'CHALLENGED_BY': 'چالش‌پذیر از', 'REPORTED_IN': 'گزارش‌شده در', 'USES': 'استفاده از',
    'PART_OF': 'بخشی از', 'BELONGS_TO': 'متعلق به', 'IS_A': 'موردی از',
}

CONTENT_KEYS = ['summary', 'core_logic', 'abstract', 'definition', 'mechanism', 'main_problem',
                'key_concepts', 'constructs', 'assumptions', 'critiques', 'critique', 'limitations',
                'applications', 'history', 'evolution', 'studies', 'research_guide',
                'detailed_analysis', 'model', 'principles', 'example', 'quote', 'bio',
                'academic_career', 'nationality', 'main_theory', 'importance', 'field']

def _def(o):
    if isinstance(o, (decimal.Decimal,)):
        return float(o)
    return str(o)

def jdump(o):
    return json.dumps(o, ensure_ascii=False, default=_def)

# ---- load entities ----
cur.execute("""SELECT id, code, entity_type, family_code, canonical_name_fa, canonical_name_en,
                      slug, properties, status_workflow, status_scientific, status_lifecycle
               FROM kb_entities""")
raw = cur.fetchall()
by_id = {}
by_code = {}
for row in raw:
    eid, code, et, fam, fa, en, slug, props, sw, ss, sl = row
    d = json.loads(props) if props else {}
    by_id[eid] = dict(id=eid, code=code, type=et, fam=fam, fa=fa, en=en, slug=slug,
                      sw=sw, ss=ss, sl=sl, props=d)
    by_code[code] = eid

# ---- load relations ----
cur.execute("SELECT source_id, target_id, relation_type, note, extraction_confidence FROM kb_relations")
rels = cur.fetchall()

# ---- load sources ----
cur.execute("SELECT id, kind, title_fa, title_en, year, publisher, doi, url, language, bibliographic, work_id FROM kb_sources")
sources = cur.fetchall()

def brief(e):
    d = e['props']
    content = {}
    for k in CONTENT_KEYS:
        v = d.get(k)
        if v in (None, '', [], {}):
            continue
        content[k] = v
    rec = dict(
        id=e['id'], code=e['code'], type=e['type'], family=e['fam'],
        nameFa=e['fa'], nameEn=e['en'], slug=e['slug'],
        sw=e['sw'], ss=e['ss'], sl=e['sl'],
        typeFa=TYPE_FA.get(e['type'], e['type']),
        familyFa=FAMILY_FA.get(e['fam'], e['fam'] or ''),
        img=d.get('image_url'),
        year=d.get('year'), level=d.get('level'), approach=d.get('approach'),
        paradigm=d.get('paradigm'), views=d.get('views'), quality=d.get('quality_score'),
        macro=d.get('macro_domain'), cat=d.get('category_id'),
        tags=d.get('tags'), theorists=d.get('theorists_text'),
        relatedApproaches=d.get('related_approaches'), recSources=d.get('recommended_sources'),
        content=content,
    )
    return rec

# per-entity relations
rel_map = collections.defaultdict(list)
for sid, tid, rtype, note, conf in rels:
    rel_map[sid].append(dict(type=rtype, relFa=REL_FA.get(rtype, rtype), dir='out',
                             other=tid, conf=conf))
    rel_map[tid].append(dict(type=rtype, relFa=REL_FA.get(rtype, rtype), dir='in',
                             other=sid, conf=conf))

# per-entity cited sources
src_map = collections.defaultdict(list)
for (sid, kind, tfa, ten, year, pub, doi, url, lang, bib, wid) in sources:
    entry = dict(id=sid, kind=kind, titleFa=tfa, titleEn=ten, year=year,
                 publisher=pub, doi=doi, url=url, lang=lang)
    if wid and wid in by_id:
        src_map[wid].append(entry)
    if bib:
        try:
            bd = json.loads(bib)
            entry['bib'] = {k: bd[k] for k in ('creator', 'citation', 'resource_type', 'image_url', 'year_note') if k in bd}
            for code in (bd.get('cited_by') or []):
                if code in by_code:
                    src_map[by_code[code]].append(entry)
        except Exception:
            pass

# links per entity
cur.execute("SELECT entity_id, link_type, link_id, link_title, note FROM kb_entity_links")
link_map = collections.defaultdict(list)
for eid, lt, lid, ltitle, note in cur.fetchall():
    link_map[eid].append(dict(type=lt, id=lid, title=ltitle, note=note))

# evidence-backed citations (kb_evidence is the authoritative card<->source link)
cur.execute("""SELECT e.about_code, s.id, s.kind, s.title_fa, s.title_en, s.year, s.publisher,
                      s.doi, s.url, s.language, s.bibliographic, s.work_id,
                      c.locator_value, e.verification_status, e.evidence_summary
               FROM kb_evidence e
               JOIN kb_sources s ON s.id = e.source_id
               LEFT JOIN kb_citations c ON c.id = e.citation_id""")
ev_index = {}
for (about, sid, kind, tfa, ten, syear, pub, doi, url, lang, bib, wid,
     locator, vstatus, esum) in cur.fetchall():
    eid = by_code.get(about)
    if not eid:
        continue
    key = (eid, sid)
    entry = ev_index.get(key)
    if entry is None:
        entry = dict(id=sid, kind=kind, titleFa=tfa, titleEn=ten, year=syear,
                     publisher=pub, doi=doi, url=url, lang=lang,
                     locator=locator, verified=(vstatus == 'verified'),
                     evidence=esum)
        if bib:
            try:
                bd = json.loads(bib)
                entry['bib'] = {k: bd[k] for k in ('creator', 'citation', 'resource_type', 'image_url', 'year_note') if k in bd}
            except Exception:
                pass
        ev_index[key] = entry
    elif vstatus == 'verified':
        entry['verified'] = True
        entry['locator'] = entry.get('locator') or locator
for (eid, sid), entry in ev_index.items():
    existing = src_map[eid]
    hit = next((x for x in existing if x.get('id') == sid), None)
    if hit is None:
        existing.append(entry)
    else:
        hit['verified'] = hit.get('verified') or entry['verified']
        hit['locator'] = hit.get('locator') or entry.get('locator')

# ---- write per-type files ----
groups = collections.defaultdict(list)
for e in by_id.values():
    rec = brief(e)
    # relations with resolved other entity
    rl = []
    for r in rel_map.get(e['id'], []):
        o = by_id.get(r['other'])
        if not o:
            continue
        r = dict(r)
        r['otherFa'] = o['fa']
        r['otherType'] = o['type']
        r['otherTypeFa'] = TYPE_FA.get(o['type'], o['type'])
        r['otherSlug'] = o['slug']
        r['otherCode'] = o['code']
        del r['other']
        rl.append(r)
    rec['relations'] = rl
    rec['sources'] = src_map.get(e['id'], [])
    rec['links'] = link_map.get(e['id'], [])
    groups[e['type']].append(rec)

manifest = {}
for et, recs in groups.items():
    fn = et.lower() + '.json'
    with open(os.path.join(OUT, fn), 'w', encoding='utf-8') as f:
        f.write(jdump(recs))
    manifest[et] = dict(fa=TYPE_FA.get(et, et), file=fn, count=len(recs))

# ---- directory (lightweight) ----
directory = []
for e in by_id.values():
    d = e['props']
    directory.append(dict(id=e['id'], code=e['code'], type=e['type'], fam=e['fam'],
                          typeFa=TYPE_FA.get(e['type'], e['type']),
                          fa=e['fa'], en=e['en'], slug=e['slug'], sw=e['sw'],
                          q=d.get('quality_score'), year=d.get('year'),
                          level=d.get('level'), img=d.get('image_url'),
                          macro=d.get('macro_domain')))
with open(os.path.join(OUT, 'directory.json'), 'w', encoding='utf-8') as f:
    f.write(jdump(directory))

# ---- sources ----
src_out = []
for (sid, kind, tfa, ten, year, pub, doi, url, lang, bib, wid) in sources:
    entry = dict(id=sid, kind=kind, titleFa=tfa, titleEn=ten, year=year,
                 publisher=pub, doi=doi, url=url, lang=lang, workId=wid)
    if bib:
        try:
            bd = json.loads(bib)
            entry['bib'] = bd
        except Exception:
            pass
    src_out.append(entry)
with open(os.path.join(OUT, 'sources.json'), 'w', encoding='utf-8') as f:
    f.write(jdump(src_out))

# ---- meta ----
type_counts = collections.Counter(e['type'] for e in by_id.values())
family_counts = collections.Counter(e['fam'] for e in by_id.values() if e['fam'])
meta = dict(
    title='هسته‌ی دانش علمی رسانامه',
    db=DB,
    builtAt=datetime.datetime.now().strftime('%Y-%m-%d %H:%M'),
    total_entities=len(by_id),
    total_relations=len(rels),
    total_sources=len(src_out),
    total_theorists=type_counts.get('PERSON', 0),
    typeFa=TYPE_FA, familyFa=FAMILY_FA, relFa=REL_FA,
    types=[dict(type=k, fa=TYPE_FA.get(k, k), count=v, fam=next((e['fam'] for e in by_id.values() if e['type'] == k), '')) for k, v in
           sorted(type_counts.items(), key=lambda x: -x[1])],
    families=[dict(fam=k, fa=FAMILY_FA.get(k, k), count=v) for k, v in
              sorted(family_counts.items(), key=lambda x: -x[1])],
    manifest=manifest,
)
with open(os.path.join(OUT, 'meta.json'), 'w', encoding='utf-8') as f:
    f.write(jdump(meta))

print("entities:", len(by_id), "relations:", len(rels), "sources:", len(src_out))
print("wrote to", OUT)
for fn in sorted(os.listdir(OUT)):
    print("  ", fn, round(os.path.getsize(os.path.join(OUT, fn)) / 1e6, 2), "MB")
