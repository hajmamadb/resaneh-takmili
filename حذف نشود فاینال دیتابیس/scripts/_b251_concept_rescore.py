# -*- coding: utf-8 -*-
"""Batch 251: truthful rescore sweep for CONCEPT entities against the live rubric."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch251-20261117"
NOW = "2026-11-17 00:00:00"


def main():
    import importlib.util
    spec = importlib.util.spec_from_file_location("fw", "scripts/kb_batch238_framework.py")
    fw = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(fw)
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="433700",
                           database=DB, charset="utf8mb4", autocommit=False)
    cur = conn.cursor()
    cur.execute("SELECT code,id,properties FROM kb_entities WHERE entity_type='CONCEPT'")
    rows = cur.fetchall()

    changes = []
    for code, eid, props in rows:
        p = json.loads(props)
        cur.execute("""SELECT COUNT(DISTINCT source_id),
                              COUNT(DISTINCT CASE WHEN verification_status='verified' THEN source_id END)
                       FROM kb_evidence WHERE about_code=%s""", (code,))
        ns, nv = cur.fetchone()
        cur.execute("SELECT COUNT(*) FROM kb_relations WHERE source_id=%s OR target_id=%s", (eid, eid))
        rel = cur.fetchone()[0]
        t, d, w = fw.rubric(p, nv, ns, rel)
        old = p.get("quality_score")
        if old != t:
            changes.append((code, eid, p, old, t, w, ns, nv, rel, d))

    ups = sum(1 for x in changes if x[4] > x[3])
    downs = sum(1 for x in changes if x[4] < x[3])
    print("concepts", len(rows), "changed", len(changes), "up", ups, "down", downs)
    for x in changes[:12]:
        print(" ", x[0], x[3], "->", x[4], "words", x[5], "src", x[6], "ver", x[7], "rel", x[8])

    for code, eid, p, old, t, w, ns, nv, rel, d in changes:
        p["quality_score"] = t
        p["quality_assessment"] = "ارزیابی خودکار SPEC §6.1: %d/100 (نمره پایه؛ نیازمند بازبینی علمی انسانی)" % t
        cur.execute("UPDATE kb_entities SET properties=%s,version=version+1,updated_at=%s,updated_by=%s WHERE id=%s",
                    (json.dumps(p, ensure_ascii=False), NOW, STAMP, eid))
        cur.execute("""INSERT INTO kb_audit_log (entity_code,action,detail,source,created_at)
            VALUES (%s,'DOC_FIX',%s,%s,%s)""",
                    (code, json.dumps({"batch": 251, "old": old, "new": t, "words": w,
                                       "sources": ns, "verified": nv, "relations": rel,
                                       "rubric": d}, ensure_ascii=False), STAMP, NOW))
    conn.commit()
    conn.close()
    print("BATCH251 DONE")


if __name__ == "__main__":
    main()
