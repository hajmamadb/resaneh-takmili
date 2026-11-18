# -*- coding: utf-8 -*-
"""Batch 199 relations."""
import pymysql

DB = "resaname_kb_final_inspect"
ASSERTED = "qoder-rel-batch199-20261117"
VERIFIED = "qoder-verify-batch199"

ROWS = [
    ("MC-712", "MC-711", "RELATED_TO",
     "The internet and media addiction model is the general framework this diagnosis specializes.", 90, 5),
    ("MC-712", "MC-538", "RELATED_TO",
     "Serious games and gamification research supplies the design context for problematic play.", 82, 3),
    ("MC-712", "MC-709", "RELATED_TO",
     "Media entertainment theory explains engagement that the clinical frame may misread as pathology.", 80, 3),
    ("MC-712", "CPT-072", "RELATED_TO",
     "Media literacy is the main preventive response to gaming-related harm.", 84, 4),
    ("MC-419", "SFL-018", "RELATED_TO",
     "Human and machine studies operationalize the posthuman blurring of agency.", 88, 4),
    ("MC-419", "SFL-007", "RELATED_TO",
     "VR and AR studies extend the body into simulated environments.", 84, 4),
    ("MC-419", "MC-531", "RELATED_TO",
     "Generative media models redistribute authorship between humans and machines.", 82, 3),
    ("MC-419", "SFL-001", "RELATED_TO",
     "AI and communication studies provide the applied field for posthuman subjectivity.", 80, 3),
    ("MC-120", "MC-011", "RELATED_TO",
     "The knowledge gap hypothesis is the communication-side analogue of the digital divide.", 90, 5),
    ("MC-120", "CPT-264", "RELATED_TO",
     "The right to access information is the normative claim behind access policies.", 86, 4),
    ("MC-120", "CPT-072", "RELATED_TO",
     "Media literacy addresses the skills divide that access alone does not close.", 88, 4),
    ("MC-120", "MC-404", "RELATED_TO",
     "Digital governance frames universal access as a policy obligation.", 82, 3),
    ("MC-520", "SFL-007", "RELATED_TO",
     "VR and AR studies are the subfield that develops virtual reality as communication.", 92, 5),
    ("MC-520", "SFL-008", "RELATED_TO",
     "Metaverse debates build on VR's presence and immersion concepts.", 88, 4),
    ("MC-520", "MC-241", "RELATED_TO",
     "Social presence theory explains the relational dimension of telepresence.", 86, 4),
    ("MC-520", "CPT-207", "RELATED_TO",
     "Virtual presence is the core experiential variable VR systems produce.", 90, 5),
    ("MC-221", "th-3", "RELATED_TO",
     "McLuhan is the founding figure whose media-as-extensions thesis defines the field.", 94, 5),
    ("MC-221", "MC-344", "RELATED_TO",
     "Philosophy of technology supplies the ontological vocabulary for media environments.", 84, 4),
    ("MC-221", "MC-340", "RELATED_TO",
     "Dromology's focus on speed parallels media ecology's focus on environmental change.", 80, 3),
    ("MC-221", "MC-411", "RELATED_TO",
     "Domestication of technology shows how media environments enter everyday life.", 82, 3),
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
        VALUES (%s,%s,%s,'verified',%s,%s,%s,%s,%s,'active','2026-11-17 00:00:00','2026-11-17 00:00:00')""",
                (s, t, rel, ASSERTED, VERIFIED, conf / 100.0, note, weight))
    inserted += 1

c.commit()
c.close()
print("inserted=%d skipped=%d" % (inserted, skipped))
