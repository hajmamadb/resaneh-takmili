# -*- coding: utf-8 -*-
"""
kb_seed.py — وارد کردن 771 سندِ resaname_editorial به resaname_kb_final_inspect
- هیچ داده‌ی ساختگی نمی‌سازد؛ فقط نگاشت (map) مستند داده‌های واقعی
- کارت‌های +90: properties.priority_90plus = true
- دیتابیس خام resaname_kb_final دست‌نخورده می‌ماند
"""
import pymysql, json, re
from collections import Counter

HOST, PORT = '127.0.0.1', 3306
ROOT_PW = '433700'
ED_USER, ED_PW = 'resaname_editorial_user', '790a141d76426c44657744741607b1c2c'
INSPECT_DB = 'resaname_kb_final_inspect'

# content_type editorial -> (entity_type, needs_review)
CT_MAP = {
    'نظریه (Theory)':                          ('THEORY', 0),
    'مدل (Model)':                             ('MODEL', 0),
    'چارچوب نظری (Theoretical Framework)':     ('FRAMEWORK', 0),
    'چارچوب اجرایی (Operational Framework)':  ('FRAMEWORK', 1),
    'اثر (Effect)':                            ('WORK', 0),
    'فرضیه (Hypothesis)':                      ('HYPOTHESIS', 0),
    'روش پژوهش (Research Method)':             ('METHOD', 0),
    'پارادایم (Paradigm)':                     ('PARADIGM', 0),
    'مکتب (School)':                           ('SCHOOL', 0),
    'مفهوم (Concept)':                        ('CONCEPT', 0),
    'قانون علمی (Law)':                       ('LAW', 0),
    'استراتژی (Strategy)':                     ('STRATEGY', 0),
    'روش‌شناسی (Methodology)':                 ('METHODOLOGY', 0),
    'پدیده (Phenomenon)':                      ('CONCEPT', 1),
    'شاخص (Indicator)':                        ('INDICATOR', 0),
    'الگو (Pattern)':                          ('MODEL', 1),
    'اصل (Principle)':                         ('CONCEPT', 1),
    'حوزه مطالعاتی (Field of Study)':         ('SUBFIELD', 1),
}
# برای 3 کارتِ بدون content_type -> card_type داخل json
FALLBACK_CT = {
    'نظریه': ('THEORY', 1),
    'مدل':   ('MODEL', 1),
}
WORKFLOW_MAP = {'approved': 'approved', 'draft_ready': 'draft',
                'review': 'in_review', 'published': 'published'}
LEVEL_MAP = {'خرد': 'MICRO', 'میانی': 'MESO', 'کلان (Macro-level)': 'MACRO'}
LINK_TYPE = {'cards': 'card', 'theorists': 'theorist', 'library_resources': 'library_resource'}

def read_all():
    c = pymysql.connect(host=HOST, port=PORT, user=ED_USER, password=ED_PW,
                        database='resaname_editorial', charset='utf8mb4', autocommit=True)
    cur = c.cursor()
    cur.execute("SELECT id, source_table, source_id, title, content_type, quality_score, "
                "workflow_status, current_json, created_at, updated_at "
                "FROM editorial_documents ORDER BY id")
    rows = []
    for doc_id, st, sid, title, ct, qs, ws, cj, ca, ua in cur.fetchall():
        rows.append({'doc_id': doc_id, 'st': st, 'sid': sid, 'title': title,
                     'ct': ct, 'qs': qs, 'ws': ws, 'd': json.loads(cj),
                     'doc_ca': str(ca), 'doc_ua': str(ua)})
    c.close()
    return rows

def main():
    rows = read_all()
    print(f"documents read: {len(rows)}")

    c = pymysql.connect(host=HOST, port=PORT, user='root', password=ROOT_PW,
                        database=INSPECT_DB, charset='utf8mb4', autocommit=False)
    cur = c.cursor()

    # registries lookups
    cur.execute("SELECT code, family_code FROM kb_entity_types")
    fam = dict(cur.fetchall())
    # build map for 3 values
    scale_id = {}
    for code in ('MICRO', 'MESO', 'MACRO'):
        cur.execute("SELECT id FROM kb_facet_values WHERE facet_code='analysis_scale' AND code=%s", (code,))
        scale_id[code] = cur.fetchone()[0]

    # clean (idempotent re-run)
    for t in ('kb_entity_links', 'kb_entity_facets', 'kb_relations', 'kb_sources', 'kb_entities'):
        cur.execute(f"DELETE FROM {t}")

    # ---- build entity rows
    ent_rows = []          # for executemany
    ent_codes = {}         # code -> (doc, entity_row_index)
    now = None
    type_counter = Counter()
    no_code_fallback = []
    fallback_used = []

    for r in rows:
        d = r['d']; st = r['st']
        # code
        if st == 'cards':
            code = d.get('code') or r['sid']
            if not d.get('code'):
                no_code_fallback.append({'sid': r['sid'], 'title': r['title'], 'qs': r['qs']})
        elif st == 'theorists':
            code = d.get('id') or r['sid']
        else:
            code = r['sid']
        # entity_type
        if st == 'theorists':
            etype, nr = 'PERSON', 0
            name_fa = d.get('name') or r['title']
            name_en = d.get('name_en')
        elif st == 'library_resources':
            etype, nr = 'WORK', 0
            name_fa = d.get('title') or r['title']
            name_en = d.get('title_en')
        else:
            ct = r['ct']
            if ct in CT_MAP:
                etype, nr = CT_MAP[ct]
            elif d.get('card_type') in FALLBACK_CT:
                etype, nr = FALLBACK_CT[d.get('card_type')]
                fallback_used.append({'sid': r['sid'], 'code': code, 'title': r['title'],
                                      'card_type': d.get('card_type'), 'mapped_to': etype})
            else:
                raise SystemExit(f"no mapping for doc {r['doc_id']} ct={ct} card_type={d.get('card_type')}")
            name_fa = d.get('title_fa') or r['title']
            name_en = d.get('title_en')
        # properties = full source json + provenance + priority flag (real data only)
        props = dict(d)
        props['quality_score'] = r['qs']
        if r['qs'] is not None and r['qs'] >= 90:
            props['priority_90plus'] = True
        props['source'] = {'table': st, 'id': r['sid'], 'editorial_document_id': r['doc_id']}
        if st == 'cards':
            props['mapping'] = {'content_type': r['ct'], 'entity_type': etype, 'needs_review': bool(nr)}
        ext = None
        if st == 'library_resources':
            ei = {}
            if d.get('isbn'): ei['isbn'] = d['isbn']
            if d.get('doi'): ei['doi'] = d['doi']
            ext = json.dumps(ei, ensure_ascii=False) if ei else None
        ent_rows.append((
            code, etype, fam[etype],
            name_fa, name_en or None,
            d.get('slug') or f"{st}-{r['sid']}",
            None,            # aliases
            None, None,      # original_name, original_language
            'fa',
            json.dumps(props, ensure_ascii=False),
            WORKFLOW_MAP.get(r['ws'], 'draft'),
            'unassessed',
            'active',
            'public',
            1,
            ext,
            d.get('created_at') or r['doc_ca'], 'seed',
            d.get('updated_at') or r['doc_ua'], 'seed',
            None, None,      # verified_at/by
        ))
        ent_codes[code] = r
        type_counter[etype] += 1

    cur.executemany("""
        INSERT INTO kb_entities
        (code, entity_type, family_code, canonical_name_fa, canonical_name_en, slug,
         aliases, original_name, original_language, language, properties,
         status_workflow, status_scientific, status_lifecycle, visibility, version,
         external_identifiers, created_at, created_by, updated_at, updated_by,
         verified_at, verified_by)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """, ent_rows)
    print(f"entities inserted: {len(ent_rows)}")

    cur.execute("SELECT id, code FROM kb_entities")
    id_by_code = {code: id for id, code in cur.fetchall()}

    # ---- facets (level -> analysis_scale)
    fac_rows = []
    for r in rows:
        d = r['d']
        if r['st'] != 'cards':
            continue
        lv = d.get('level')
        if lv in LEVEL_MAP:
            code = d.get('code') or r['sid']
            fac_rows.append((id_by_code[code], 'analysis_scale', scale_id[LEVEL_MAP[lv]], 0))
    cur.executemany("""
        INSERT INTO kb_entity_facets (entity_id, facet_code, facet_value_id, sort_order, created_at)
        VALUES (%s,%s,%s,%s,NOW())
    """, fac_rows)
    print(f"facets inserted: {len(fac_rows)}")

    # ---- relations: explicit MC-xxx refs in any text field (real, unverified)
    mc_re = re.compile(r'MC-\d{3}')
    rel_pairs = set()
    ref_total = 0
    for r in rows:
        d = r['d']
        own_code = d.get('code') if r['st'] == 'cards' else (d.get('id') if r['st'] == 'theorists' else r['sid'])
        own_code = own_code or r['sid']
        def walk(o):
            refs = []
            if isinstance(o, str):
                refs = mc_re.findall(o)
            elif isinstance(o, dict):
                for v in o.values(): refs.extend(walk(v))
            elif isinstance(o, list):
                for v in o: refs.extend(walk(v))
            return refs
        for ref in walk(d):
            ref_total += 1
            if ref == own_code:
                continue
            if ref in id_by_code and own_code in id_by_code:
                rel_pairs.add((id_by_code[own_code], id_by_code[ref]))
    rel_rows = [(s, t, 'RELATED_TO', 'unverified', 'seed', 0.950,
                 'ارجاع صریح MC در متن سند (extracted)', 50, 'needs_review')
                for s, t in sorted(rel_pairs)]
    cur.executemany("""
        INSERT INTO kb_relations
        (source_id, target_id, relation_type, valid_from, valid_until, assertion_status,
         asserted_by, verified_by, extraction_confidence, note, weight, status, created_at, updated_at)
        VALUES (%s,%s,%s,NULL,NULL,%s,%s,NULL,%s,%s,%s,%s,NOW(),NOW())
    """, rel_rows)
    print(f"MC refs found: {ref_total}, relations inserted: {len(rel_rows)}")

    # ---- links (provenance to source system)
    link_rows = []
    for r in rows:
        d = r['d']
        code = (d.get('code') if r['st'] == 'cards' else d.get('id') if r['st'] == 'theorists' else r['sid']) or r['sid']
        link_rows.append((id_by_code[code], LINK_TYPE[r['st']], r['sid'],
                          (r['title'] or d.get('name') or d.get('title') or '')[:500],
                          'verified'))
    cur.executemany("""
        INSERT INTO kb_entity_links (entity_id, link_type, link_id, link_title, note, confidence, created_by, created_at)
        VALUES (%s,%s,%s,%s,NULL,%s,'seed',NOW())
    """, link_rows)
    print(f"links inserted: {len(link_rows)}")

    # ---- kb_sources for the library resource (book)
    for r in rows:
        if r['st'] != 'library_resources':
            continue
        d = r['d']
        code = d.get('id') or r['sid']
        eid = id_by_code[code]
        cur.execute("""
            INSERT INTO kb_sources (kind, title_fa, title_en, year, publisher, doi, isbn, url,
                                    language, access_type, bibliographic, work_id)
            VALUES ('BOOK', %s, %s, %s, %s, NULLIF(%s,''), NULLIF(%s,''), NULLIF(%s,''),
                    %s, 'unknown', %s, %s)
        """, (d.get('title'), d.get('title_en'), d.get('publication_year'),
              d.get('publisher'), d.get('doi'), d.get('isbn'), d.get('source_url'),
              d.get('language'),
              json.dumps({'creator': d.get('creator'), 'resource_type': d.get('resource_type'),
                          'image_url': d.get('image_url'),
                          'year_note': 'publication_year به سال شمسی است' if d.get('publication_year') else None},
                         ensure_ascii=False),
              eid))
        print("kb_sources row inserted (book):", d.get('title'))

    c.commit()

    # ---- summary
    cur.execute("SELECT entity_type, COUNT(*), SUM(properties->>'$.priority_90plus') FROM kb_entities GROUP BY entity_type ORDER BY 2 DESC")
    print("\n=== kb_entities by type (n, +90) ===")
    for t, n, p90 in cur.fetchall():
        print(f"  {t:20s} {n:4d}  {p90 or 0}")
    print("\nfallback (no content_type -> card_type):")
    print(json.dumps(fallback_used, ensure_ascii=False, indent=1))
    print(f"\nno_code_fallback: {len(no_code_fallback)}")
    c.close()
    print("\nDONE — committed.")

if __name__ == '__main__':
    main()
