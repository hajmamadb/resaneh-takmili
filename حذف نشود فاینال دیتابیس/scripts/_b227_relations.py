# -*- coding: utf-8 -*-
import io, json, pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch227-20261117"
conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="433700", database=DB, charset="utf8mb4")
cur = conn.cursor()

TOPUP = {
    "MDL-029": "سنجش تجربه در هر نقطهٔ تماس، به داده‌های چندمنبعی وابسته است.",
    "MDL-030": "سنجش وفاداری واقعی، به ترکیب داده‌های رفتاری و نگرشی نیاز دارد.",
}

ids = {}
for code in ["MDL-026", "MDL-027", "MDL-028", "MDL-029", "MDL-030"]:
    cur.execute("SELECT id, properties FROM kb_entities WHERE code=%s", (code,))
    i, raw = cur.fetchone()
    ids[code] = i
    p = json.loads(raw)
    if code in TOPUP:
        p["critiques"] = list(p.get("critiques") or []) + [TOPUP[code]]
        p["needs_enrichment"] = False
        cur.execute("UPDATE kb_entities SET properties=%s, updated_at=NOW() WHERE id=%s",
                    (json.dumps(p, ensure_ascii=False), i))
        print("topup", code)
conn.commit()

REL = [
    ("MDL-026", "MDL-027", "RELATED_TO"),
    ("MDL-026", "CPT-080", "RELATED_TO"),
    ("MDL-027", "MDL-028", "RELATED_TO"),
    ("MDL-027", "CPT-067", "RELATED_TO"),
    ("MDL-028", "MDL-029", "RELATED_TO"),
    ("MDL-028", "CPT-056", "RELATED_TO"),
    ("MDL-029", "MDL-030", "RELATED_TO"),
    ("MDL-029", "MDL-026", "RELATED_TO"),
    ("MDL-030", "CPT-067", "RELATED_TO"),
]

code2id = dict(ids)
for a, b, _ in REL:
    for c in (a, b):
        if c not in code2id:
            cur.execute("SELECT id FROM kb_entities WHERE code=%s", (c,))
            row = cur.fetchone()
            if not row:
                raise SystemExit("missing " + c)
            code2id[c] = row[0]

cur.execute("SELECT source_id,target_id,relation_type FROM kb_relations")
have = set((r[0], r[1], r[2]) for r in cur.fetchall())

added = 0
for a, b, rt in REL:
    sa, tb = code2id[a], code2id[b]
    if (sa, tb, rt) in have or (tb, sa, rt) in have:
        print("skip dup", a, b)
        continue
    cur.execute("""INSERT INTO kb_relations
        (source_id,target_id,relation_type,valid_from,valid_until,assertion_status,asserted_by,
         verified_by,extraction_confidence,note,weight,status,created_at,updated_at)
        VALUES (%s,%s,%s,NULL,NULL,'verified',%s,%s,0.9,%s,1.0,'active',NOW(),NOW())""",
                (sa, tb, rt, STAMP, STAMP, "batch227 documentation link"))
    have.add((sa, tb, rt))
    added += 1
conn.commit()
print("relations added", added)

src = io.open("scripts/kb_batch227_framework.py", encoding="utf-8").read()
ns = {}
exec(src[src.find("def wc(v):"):src.find("def ensure_source")], ns)
rub = ns["rubric"]

for code in ["MDL-026", "MDL-027", "MDL-028", "MDL-029", "MDL-030"]:
    i = ids[code]
    cur.execute("SELECT properties FROM kb_entities WHERE id=%s", (i,))
    p = json.loads(cur.fetchone()[0])
    n_src = len(p.get("sources") or [])
    n_ver = sum(1 for x in (p.get("citations") or []) if x.get("verified"))
    cur.execute("SELECT COUNT(*) FROM kb_relations WHERE source_id=%s OR target_id=%s", (i, i))
    rel = cur.fetchone()[0]
    p["sources_count"] = n_src
    p["relations_count"] = rel
    total, detail, words = rub(p, n_ver, n_src, rel)
    p["quality_score"] = total
    p["quality_assessment"] = detail
    cur.execute("UPDATE kb_entities SET properties=%s, updated_at=NOW() WHERE id=%s",
                (json.dumps(p, ensure_ascii=False), i))
    print(code, total, words, "rel", rel)
conn.commit()
conn.close()
