# -*- coding: utf-8 -*-
"""Batch 201 relations."""
import pymysql

DB = "resaname_kb_final_inspect"
ASSERTED = "qoder-rel-batch201-20261117"
VERIFIED = "qoder-verify-batch201"

ROWS = [
    ("MC-731", "MC-432", "RELATED_TO",
     "Affective polarization is the structural outcome affective publics can harden into.", 86, 4),
    ("MC-731", "TX-038", "RELATED_TO",
     "Digital activism theory explains how affective publics turn into mobilization.", 88, 4),
    ("MC-731", "SFL-011", "RELATED_TO",
     "Digital polarization studies measure the divisive edge of affective publics.", 84, 4),
    ("MC-731", "TX-071", "RELATED_TO",
     "Narrative theory supplies the storytelling mechanism at the core of affective publics.", 82, 3),
    ("MC-432", "SFL-011", "RELATED_TO",
     "Digital polarization research is the subfield that measures affective polarization online.", 90, 5),
    ("MC-432", "MC-113", "RELATED_TO",
     "Echo chamber theory explains the informational reinforcement of out-group hostility.", 86, 4),
    ("MC-432", "MC-112", "RELATED_TO",
     "Filter bubbles are a debated platform mechanism behind affective sorting.", 84, 4),
    ("MC-432", "MC-731", "RELATED_TO",
     "Affective publics describe the sentiment-driven collectives polarization operates on.", 84, 4),
    ("MC-236", "MC-525", "RELATED_TO",
     "Big data is the object of critique this framework interrogates.", 94, 5),
    ("MC-236", "MC-284", "RELATED_TO",
     "Data justice extends the ethical critique to distributive inequality.", 88, 4),
    ("MC-236", "MC-434", "RELATED_TO",
     "The algorithmic black box is the opacity problem the provocations anticipate.", 84, 4),
    ("MC-236", "MC-223", "RELATED_TO",
     "Dataism is the ideology of data-driven knowledge the framework challenges.", 90, 5),
    ("MC-637", "MC-001", "RELATED_TO",
     "Agenda setting is the media mechanism that makes owned issues salient.", 90, 5),
    ("MC-637", "MC-144", "RELATED_TO",
     "Media agenda building explains how parties and news jointly construct issue salience.", 88, 4),
    ("MC-637", "MC-002", "RELATED_TO",
     "Network agenda setting extends issue salience to networked issue associations.", 82, 3),
    ("MC-637", "MC-667", "RELATED_TO",
     "Algorithmic salience theory explains platform-level variation in issue visibility.", 80, 3),
    ("MC-538", "MC-712", "RELATED_TO",
     "Gaming disorder marks the clinical boundary of the engagement gamification seeks.", 84, 4),
    ("MC-538", "MC-709", "RELATED_TO",
     "Media entertainment theory explains the engagement mechanics gamification borrows.", 82, 3),
    ("MC-538", "CPT-072", "RELATED_TO",
     "Media literacy is the educational counterpart of gameful learning design.", 80, 3),
    ("MC-538", "SFL-015", "RELATED_TO",
     "Participatory culture frames the user engagement gamification formalizes.", 78, 3),
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
