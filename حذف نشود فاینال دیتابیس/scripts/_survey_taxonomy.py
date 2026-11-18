# -*- coding: utf-8 -*-
import pymysql, json, collections

c = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='433700',
                    database='resaname_kb_final_inspect', charset='utf8mb4')
cur = c.cursor()

def q(s, args=None):
    cur.execute(s, args or ()); return cur.fetchall()

out = {}

# --- registries ---
try:
    out['entity_families'] = q("SELECT * FROM kb_entity_families ORDER BY id")
except Exception as e:
    out['entity_families'] = f"ERR {e}"
try:
    out['entity_types'] = q("SELECT * FROM kb_entity_types ORDER BY id")
except Exception as e:
    out['entity_types'] = f"ERR {e}"
try:
    out['entity_subtypes'] = q("SELECT * FROM kb_entity_subtypes ORDER BY id")
except Exception as e:
    out['entity_subtypes'] = f"ERR {e}"
try:
    out['relation_types'] = q("SELECT * FROM kb_relation_types ORDER BY id")
except Exception as e:
    out['relation_types'] = f"ERR {e}"
try:
    out['facet_dimensions'] = q("SELECT * FROM kb_facet_dimensions ORDER BY id")
except Exception as e:
    out['facet_dimensions'] = f"ERR {e}"
try:
    out['facet_values'] = q("SELECT * FROM kb_facet_values ORDER BY id")
except Exception as e:
    out['facet_values'] = f"ERR {e}"

# --- entity counts by type ---
out['count_by_type'] = q("SELECT entity_type, COUNT(*) FROM kb_entities GROUP BY entity_type ORDER BY 2 DESC")
out['total_entities'] = q("SELECT COUNT(*) FROM kb_entities")[0][0]

# --- code prefixes ---
out['code_prefixes'] = q("SELECT SUBSTRING_INDEX(code,'-',1) AS pfx, COUNT(*) FROM kb_entities GROUP BY pfx ORDER BY 2 DESC")

# --- sample properties structures ---
for et in ('THEORY','MODEL','CONCEPT','METHOD','FIELD','SUBFIELD','PERSON','WORK'):
    rows = q("SELECT code, properties FROM kb_entities WHERE entity_type=%s LIMIT 1", (et,))
    if rows:
        code, p = rows[0]
        try:
            out[f'sample_props_{et}'] = {'code': code, 'keys': list(json.loads(p).keys())}
        except Exception:
            out[f'sample_props_{et}'] = {'code': code, 'raw': p[:300]}

# --- dump all entity names for matching ---
names = []
for code, et, fa, en, al in q("SELECT code, entity_type, canonical_name_fa, canonical_name_en, aliases FROM kb_entities ORDER BY code"):
    names.append({'code': code, 'type': et, 'fa': fa, 'en': en, 'aliases': al})
out['all_names'] = names

json.dump(out, open(r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_survey_taxonomy.json","w",encoding="utf-8"),
          ensure_ascii=False, indent=1, default=str)

# print a compact summary
print("=== entity_types ===")
for r in out['entity_types']:
    print(" ", r)
print("\n=== families ===")
for r in out['entity_families']:
    print(" ", r)
print("\n=== count by type ===")
for r in out['count_by_type']:
    print(" ", r)
print("\n=== code prefixes ===")
for r in out['code_prefixes']:
    print(" ", r)
print("\n=== facet_dimensions ===")
for r in out['facet_dimensions']:
    print(" ", r)
print("\n=== facet_values (count) ===")
if isinstance(out['facet_values'], list):
    print(" ", len(out['facet_values']), "values")
    for r in out['facet_values']:
        print("  ", r)
else:
    print(" ", out['facet_values'])
c.close()
print("\nDumped -> _survey_taxonomy.json ; total entities:", out['total_entities'])
