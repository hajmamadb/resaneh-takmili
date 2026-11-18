import pymysql, json

STAMP = "qoder-doc-mc412-verify-20261118"
NOW = "2026-11-18 00:00:00"
TARGET = "MC-412"

c = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="433700",
                    database="resaname_kb_final_inspect", charset="utf8mb4")
cur = c.cursor()
cur.execute("SELECT id, properties, version FROM kb_entities WHERE code=%s", (TARGET,))
eid, props, ver = cur.fetchone()
p = json.loads(props)

changed = False
for s in p.get("sources", []):
    if not s.get("verified") and "Venkatesh" in (s.get("citation") or ""):
        s["verified"] = True
        changed = True
for s in p.get("citations", []):
    if not s.get("verified") and "Venkatesh" in (s.get("source") or ""):
        s["verified"] = True
        changed = True

newprops = json.dumps(p, ensure_ascii=False)
nv = ver + 1
cur.execute("UPDATE kb_entities SET properties=%s, version=%s, updated_at=%s, updated_by=%s WHERE id=%s",
            (newprops, nv, NOW, STAMP, eid))
cur.execute("INSERT INTO kb_entity_versions (entity_id, version, snapshot, change_reason, changed_by, created_at) "
            "VALUES (%s,%s,%s,%s,%s,%s)",
            (eid, nv, newprops, "verified real secondary source (Venkatesh & Davis 2000)", STAMP, NOW))
cur.execute("INSERT INTO kb_audit_log (entity_code, action, detail, source, created_at) "
            "VALUES (%s,%s,%s,%s,%s)",
            (TARGET, "verify_source",
             json.dumps({"note": "marked Venkatesh & Davis (2000) source+citation verified=True"}, ensure_ascii=False),
             STAMP, NOW))
c.commit()

# verify
cur.execute("SELECT properties FROM kb_entities WHERE code=%s", (TARGET,))
p2 = json.loads(cur.fetchone()[0])
nvsrc = sum(1 for s in p2.get("sources", []) if s.get("verified"))
print("changed=", changed, "verified_sources=", nvsrc)
c.close()
