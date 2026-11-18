import pymysql, json
from collections import Counter

c = pymysql.connect(host="127.0.0.1", user="root", password="433700", database="resaname_kb_final_inspect", charset="utf8mb4")
cur = c.cursor()

print("== total ==")
cur.execute("SELECT COUNT(*) FROM kb_entities")
print("total:", cur.fetchone()[0])

print("\n== by entity_type ==")
cur.execute("SELECT entity_type, COUNT(*) FROM kb_entities GROUP BY entity_type ORDER BY 2 DESC")
for t, n in cur.fetchall():
    print(f"  {t}: {n}")

print("\n== my taxonomy-seed rows (properties.taxonomy.status) ==")
cur.execute("SELECT COUNT(*) FROM kb_entities WHERE properties LIKE '%taxonomy_seed%'")
print("taxonomy_seed rows:", cur.fetchone()[0])

print("\n== my added rows by type ==")
cur.execute("SELECT entity_type, COUNT(*) FROM kb_entities WHERE properties LIKE '%taxonomy_seed_20261115%' GROUP BY entity_type")
for t, n in cur.fetchall():
    print(f"  {t}: {n}")

print("\n== duplicate code / slug check (should be none) ==")
cur.execute("""SELECT code, COUNT(*) n FROM kb_entities GROUP BY code HAVING n>1""")
d = cur.fetchall()
print("dup codes:", d if d else "none")
cur.execute("""SELECT slug, COUNT(*) n FROM kb_entities GROUP BY slug HAVING n>1""")
d = cur.fetchall()
print("dup slugs:", d if d else "none")

print("\n== referential integrity: entity_type / family_code must exist ==")
cur.execute("""
  SELECT e.code, e.entity_type, e.family_code
  FROM kb_entities e
  LEFT JOIN kb_entity_types t ON t.code=e.entity_type
  WHERE t.code IS NULL
""")
d = cur.fetchall()
print("rows with unregistered entity_type:", d if d else "none")
cur.execute("""
  SELECT e.code, e.entity_type, e.family_code
  FROM kb_entities e
  LEFT JOIN kb_entity_families f ON f.code=e.family_code
  WHERE f.code IS NULL
""")
d = cur.fetchall()
print("rows with unregistered family_code:", d if d else "none")

print("\n== audit log rows for this run ==")
cur.execute("SELECT COUNT(*) FROM kb_audit_log WHERE action='TAXONOMY_ADD'")
print("TAXONOMY_ADD audit rows:", cur.fetchone()[0])

print("\n== sample of inserted (verify family/type alignment) ==")
cur.execute("""SELECT code, entity_type, family_code, canonical_name_fa FROM kb_entities
WHERE properties LIKE '%taxonomy_seed%' ORDER BY code LIMIT 8""")
for r in cur.fetchall():
    print(" ", r)

c.close()
print("VERIFY DONE")
