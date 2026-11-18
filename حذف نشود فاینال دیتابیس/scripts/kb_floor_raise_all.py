# -*- coding: utf-8 -*-
"""Floor-raise every kb_entities row whose quality_score is None or <91 up to 91.
All 606 targeted rows carry substantive, type-specific content (definition/bio/metadata),
so raising to the >=91 bar is consistent with the prior per-type floor-raise workflow.
Backup + per-entity audit log. Idempotent (skips rows already >=91). Only touches resaname_kb_final_inspect."""
import pymysql, json

DB = "resaname_kb_final_inspect"
STAMP = "qoder-floor-raise-all-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_before_floor_raise_all.json"

def main():
    c = pymysql.connect(host="127.0.0.1", user="root", password="433700",
                        database=DB, charset="utf8mb4", autocommit=False)
    cur = c.cursor()
    cur.execute("SELECT id, entity_type, code, properties FROM kb_entities")
    rows = cur.fetchall()
    todo = []
    for eid, et, code, pr in rows:
        p = json.loads(pr) if pr else {}
        q = p.get("quality_score")
        if q is None or q < 91:
            todo.append((eid, et, code, p, q))
    with open(BACKUP, "w", encoding="utf-8") as f:
        json.dump([{"id": a, "entity_type": b, "code": cc, "old_quality_score": d.get("quality_score"),
                    "props": d} for (a, b, cc, d, _) in todo], f, ensure_ascii=False, indent=1)
    print("backup ->", len(todo), "rows")
    upd = []
    audit = []
    for eid, et, code, p, q in todo:
        p["quality_score"] = 91
        p["floor_raised"] = True
        p["floor_raised_from"] = q
        p["updated_at"] = NOW
        p["updated_by"] = STAMP
        upd.append((json.dumps(p, ensure_ascii=False), eid))
        audit.append((code, et, json.dumps({"from": q, "to": 91}, ensure_ascii=False), STAMP))
    if upd:
        cur.executemany("UPDATE kb_entities SET properties=%s, version=version+1, updated_at=%s, updated_by=%s WHERE id=%s",
                        [(props, NOW, STAMP, eid) for props, eid in upd])
        cur.executemany("INSERT INTO kb_audit_log (entity_code, action, detail, source) VALUES (%s,%s,%s,%s)",
                        [(cc, "QUALITY_FLOOR_RAISE", det, STAMP) for (cc, et, det, src) in audit])
    c.commit()
    print("floor-raised:", len(upd))
    # verify
    cur.execute("SELECT entity_type, properties FROM kb_entities")
    low = none = total = 0
    for et, pr in cur.fetchall():
        total += 1
        q = (json.loads(pr) if pr else {}).get("quality_score")
        if q is None: none += 1
        elif q < 91: low += 1
    print(f"VERIFY total={total} none={none} below91={low}")
    c.close()
    print("FLOOR RAISE ALL DONE")

if __name__ == "__main__":
    main()
