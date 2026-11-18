import pymysql, json

c = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='433700',
                    database='resaname_kb_final_inspect', charset='utf8mb4', autocommit=True)
cur = c.cursor()
out = {}

# 1) MC-001 entity (Agenda Setting) — real record check
cur.execute("""SELECT code, entity_type, family_code, canonical_name_fa, canonical_name_en,
                      status_workflow, status_scientific, JSON_EXTRACT(properties,'$.core_logic'),
                      JSON_EXTRACT(properties,'$.quality_score'),
                      JSON_EXTRACT(properties,'$.priority_90plus'),
                      JSON_EXTRACT(properties,'$.source')
               FROM kb_entities WHERE code='MC-001'""")
r = cur.fetchone()
out['MC-001'] = {
    'type': r[1], 'family': r[2], 'name_fa': r[3], 'name_en': r[4],
    'workflow': r[5], 'scientific': r[6],
    'core_logic': (r[7][:150] + '…') if r[7] else None,
    'qs': r[8], 'p90': r[9], 'source': r[10]}

# 2) its facet
cur.execute("""SELECT f.facet_code, v.code, v.label_fa FROM kb_entity_facets f
               JOIN kb_entities e ON e.id=f.entity_id
               LEFT JOIN kb_facet_values v ON v.id=f.facet_value_id
               WHERE e.code='MC-001'""")
out['MC-001_facet'] = cur.fetchall()

# 3) th-1 (McCombs) person
cur.execute("""SELECT entity_type, canonical_name_fa, canonical_name_en,
                      JSON_EXTRACT(properties,'$.nationality'),
                      JSON_EXTRACT(properties,'$.main_theory'),
                      JSON_EXTRACT(properties,'$.quality_score')
               FROM kb_entities WHERE code='th-1'""")
r = cur.fetchone()
out['th-1'] = {'type': r[0], 'name': r[1], 'name_en': r[2],
               'nationality': r[3], 'main_theory': r[4][:100], 'qs': r[5]}

# 4) the book + kb_sources link
cur.execute("""SELECT e.code, e.entity_type, e.canonical_name_fa, s.kind, s.publisher, s.year
               FROM kb_entities e JOIN kb_sources s ON s.work_id=e.id""")
out['book'] = cur.fetchall()

# 5) card-540 (no-code 90+ card)
cur.execute("""SELECT code, entity_type, canonical_name_fa,
                      JSON_EXTRACT(properties,'$.quality_score'),
                      JSON_EXTRACT(properties,'$.priority_90plus')
               FROM kb_entities WHERE code='card-540'""")
out['card-540'] = cur.fetchone()

# 6) a relation example with names
cur.execute("""SELECT e1.canonical_name_fa, e2.canonical_name_fa, r.note
               FROM kb_relations r JOIN kb_entities e1 ON e1.id=r.source_id
               JOIN kb_entities e2 ON e2.id=r.target_id LIMIT 3""")
out['relations_sample'] = cur.fetchall()

# 7) link provenance sample
cur.execute("""SELECT e.code, l.link_type, l.link_id, l.confidence
               FROM kb_entity_links l JOIN kb_entities e ON e.id=l.entity_id LIMIT 3""")
out['links_sample'] = cur.fetchall()

print(json.dumps(out, ensure_ascii=False, indent=2))
c.close()
