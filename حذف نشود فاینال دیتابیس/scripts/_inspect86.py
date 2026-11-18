# -*- coding: utf-8 -*-
import json, pymysql

DB = "resaname_kb_final_inspect"
CODES = ["MC-454", "MC-457", "MC-458", "MC-459"]

conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="433700",
                       database=DB, charset="utf8mb4", autocommit=True)
cur = conn.cursor()
cur.execute("SELECT code, canonical_name_fa, canonical_name_en, properties, version FROM kb_entities WHERE code IN (%s,%s,%s,%s)",
            CODES)
for code, fa, en, props, ver in cur.fetchall():
    p = json.loads(props) if props else {}
    print("=" * 70)
    print(code, "|", fa, "|", en, "| v", ver)
    print("year:", p.get("year"), "| theorists:", p.get("theorists_text"))
    print("field:", p.get("field"), "| core:", p.get("core_idea"))
    for k in ("summary", "definition", "critique", "example"):
        v = p.get(k) or ""
        print(f"-- {k} ({len(v)}):", v[:260].replace("\n", " | "))
    print("n sources:", len(p.get("sources") or []))

cur.execute("""SELECT e.code, COUNT(r.id) FROM kb_entities e
               LEFT JOIN kb_relations r ON r.from_entity_id=e.id OR r.to_entity_id=e.id
               WHERE e.code IN (%s,%s,%s,%s) GROUP BY e.code""", CODES)
print("relations:", cur.fetchall())
conn.close()
