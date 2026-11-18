# -*- coding: utf-8 -*-
"""Batch 197 relations."""
import pymysql

DB = "resaname_kb_final_inspect"
ASSERTED = "qoder-rel-batch197-20261116"
VERIFIED = "qoder-verify-batch197"

ROWS = [
    ("SFL-016", "TX-038", "RELATED_TO",
     "The theory of digital activism supplies the core explanatory frame for networked mobilization.", 92, 5),
    ("SFL-016", "TX-082", "RELATED_TO",
     "Social movement theory provides the baseline models of organization that networked activism modifies.", 88, 4),
    ("SFL-016", "TX-079", "RELATED_TO",
     "Resource mobilization theory explains the capacity deficits that connective action struggles to solve.", 84, 4),
    ("SFL-016", "CPT-121", "RELATED_TO",
     "Social mobilization is the outcome concept this subfield measures online and offline.", 86, 4),
    ("SFL-017", "SFL-001", "RELATED_TO",
     "AI and communication studies share the machine-mediated layer of smart communication.", 88, 4),
    ("SFL-017", "SFL-018", "RELATED_TO",
     "Human and machine studies supply the interactional vocabulary for smart devices.", 86, 4),
    ("SFL-017", "MC-531", "RELATED_TO",
     "Generative AI models are a key driver of context-aware smart communication.", 84, 4),
    ("SFL-017", "CPT-260", "RELATED_TO",
     "AI journalism shows how sensor and model outputs enter news production.", 80, 3),
    ("SFL-018", "SFL-001", "RELATED_TO",
     "AI and communication studies provide the broader field in which human-machine communication sits.", 88, 4),
    ("SFL-018", "SFL-017", "RELATED_TO",
     "Smart communication embeds human-machine interaction in everyday environments.", 86, 4),
    ("SFL-018", "MC-241", "RELATED_TO",
     "Social presence theory explains why users treat mediated agents as social others.", 90, 5),
    ("SFL-018", "MC-531", "RELATED_TO",
     "Generative models raise the transparency and anthropomorphism problems this subfield studies.", 84, 4),
    ("SFL-019", "MC-668", "RELATED_TO",
     "Algorithmic discrimination theory is the central bias mechanism in media AI ethics.", 90, 5),
    ("SFL-019", "CPT-271", "RELATED_TO",
     "Algorithmic transparency is the operative principle this subfield turns into policy.", 88, 4),
    ("SFL-019", "MC-284", "RELATED_TO",
     "Data justice links AI ethics to distributive and structural inequality.", 86, 4),
    ("SFL-019", "card-59", "RELATED_TO",
     "Algorithmic accountability is the governance mechanism that closes the ethics loop.", 90, 5),
]

c = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="433700",
                    database=DB, charset="utf8mb4")
cur = c.cursor()

codes = sorted({r[0] for r in ROWS} | {r[1] for r in ROWS})
cur.execute("SELECT code,id FROM kb_entities WHERE code IN (%s)" % ",".join(["%s"] * len(codes)), codes)
ids = dict(cur.fetchall())
missing = [x for x in codes if x not in ids]
assert not missing, "missing: %s" % missing

inserted = skipped = 0
for src, tgt, rel, note, conf, weight in ROWS:
    s, t = ids[src], ids[tgt]
    cur.execute("""SELECT id FROM kb_relations
                   WHERE source_id=%s AND target_id=%s AND relation_type=%s""", (s, t, rel))
    if cur.fetchone():
        skipped += 1
        continue
    cur.execute("""INSERT INTO kb_relations
        (source_id,target_id,relation_type,assertion_status,asserted_by,verified_by,
         extraction_confidence,note,weight,status,created_at,updated_at)
        VALUES (%s,%s,%s,'verified',%s,%s,%s,%s,%s,'active','2026-11-16 00:00:00','2026-11-16 00:00:00')""",
                (s, t, rel, ASSERTED, VERIFIED, conf / 100.0, note, weight))
    inserted += 1

c.commit()
c.close()
print("inserted=%d skipped=%d" % (inserted, skipped))
