# -*- coding: utf-8 -*-
"""Batch 198 relations."""
import pymysql

DB = "resaname_kb_final_inspect"
ASSERTED = "qoder-rel-batch198-20261117"
VERIFIED = "qoder-verify-batch198"

ROWS = [
    ("MC-600", "MC-505", "RELATED_TO",
     "Network effects are the underlying economic mechanism the law formalizes.", 92, 5),
    ("MC-600", "MC-031", "RELATED_TO",
     "Two-sided and multi-sided markets show where network value meets platform pricing.", 86, 4),
    ("MC-600", "MC-117", "RELATED_TO",
     "The platform society explains how network effects concentrate infrastructural power.", 84, 4),
    ("MC-600", "MC-601", "RELATED_TO",
     "Reed's law extends Metcalfe's argument to group-forming networks.", 90, 5),
    ("MC-601", "MC-505", "RELATED_TO",
     "Network effects supply the baseline that group-forming value accelerates beyond.", 90, 5),
    ("MC-601", "MC-031", "RELATED_TO",
     "Multi-sided markets are where group-forming value is monetized.", 85, 4),
    ("MC-601", "MC-415", "RELATED_TO",
     "Platformization describes the spread of group-forming architectures across sectors.", 82, 3),
    ("MC-601", "MC-600", "RELATED_TO",
     "Metcalfe's law is the direct predecessor against which Reed's law is defined.", 90, 5),
    ("MC-702", "TX-050", "RELATED_TO",
     "Constructive journalism is the broader normative program this practice belongs to.", 92, 5),
    ("MC-702", "MC-401", "RELATED_TO",
     "Watchdog journalism is the function solutions reporting is accused of softening.", 84, 4),
    ("MC-702", "MC-224", "RELATED_TO",
     "Technological solutionism marks the line between reporting responses and promoting fixes.", 82, 3),
    ("MC-702", "MC-366", "RELATED_TO",
     "Participatory journalism overlaps in sourcing audience-led responses.", 78, 3),
    ("MC-706", "MC-088", "RELATED_TO",
     "Social cognitive theory is the direct theoretical successor to social learning theory.", 94, 5),
    ("MC-706", "MC-566", "RELATED_TO",
     "The media aggression growth model applies observational learning to violent content.", 88, 4),
    ("MC-706", "MC-106", "RELATED_TO",
     "The general aggression model incorporates observational learning into media effects.", 84, 4),
    ("MC-706", "MC-565", "RELATED_TO",
     "The frustration-aggression hypothesis marks the alternative explanation learning theory qualifies.", 76, 3),
    ("MC-607", "MC-729", "RELATED_TO",
     "Strategic management in media is the applied field for the generic strategies.", 92, 5),
    ("MC-607", "MDL-061", "RELATED_TO",
     "The media strategic management model operationalizes cost, differentiation and focus choices.", 88, 4),
    ("MC-607", "CPT-180", "RELATED_TO",
     "Competitive advantage is the outcome concept the three strategies aim at.", 90, 5),
    ("MC-607", "MC-176", "RELATED_TO",
     "Strategic groups map firms by the strategy choices they adopt within an industry.", 82, 3),
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
