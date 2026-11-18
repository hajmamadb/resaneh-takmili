# -*- coding: utf-8 -*-
"""Batch 200 relations."""
import pymysql

DB = "resaname_kb_final_inspect"
ASSERTED = "qoder-rel-batch200-20261117"
VERIFIED = "qoder-verify-batch200"

ROWS = [
    ("MC-123", "MC-129", "RELATED_TO",
     "Risk communication is the applied practice the amplification framework explains.", 92, 5),
    ("MC-123", "MC-122", "RELATED_TO",
     "Situational crisis communication theory models organizational responses to amplified risk events.", 86, 4),
    ("MC-123", "MC-591", "RELATED_TO",
     "The social-media crisis communication model captures digital amplification dynamics.", 88, 4),
    ("MC-123", "MC-447", "RELATED_TO",
     "Sensemaking explains how audiences interpret and amplify risk signals.", 84, 4),
    ("MC-627", "MC-489", "RELATED_TO",
     "The professionalism and editorial independence model defines the occupational standards competencies support.", 88, 4),
    ("MC-627", "MDL-062", "RELATED_TO",
     "Digital media maturity models specify the skills a competency framework must cover.", 82, 3),
    ("MC-627", "CPT-175", "RELATED_TO",
     "Media innovation is the capability that differentiating competencies are meant to produce.", 80, 3),
    ("MC-627", "MDL-041", "RELATED_TO",
     "Professional user-generated content models the boundary between amateur skill and professional competence.", 78, 3),
    ("MC-128", "MC-045", "RELATED_TO",
     "Social responsibility theory is the normative foundation of CSR communication.", 90, 5),
    ("MC-128", "CPT-262", "RELATED_TO",
     "Media social responsibility applies the CSR logic to news organizations.", 88, 4),
    ("MC-128", "MC-371", "RELATED_TO",
     "Excellence theory supplies the dialogic PR model CSR communication draws on.", 84, 4),
    ("MC-128", "MC-499", "RELATED_TO",
     "Reputation management is the outcome CSR communication is often expected to protect.", 86, 4),
    ("MC-728", "MC-447", "RELATED_TO",
     "The organizational sensemaking theory is the direct theoretical companion to this framework.", 94, 5),
    ("MC-728", "MC-122", "RELATED_TO",
     "Crisis communication theory relies on sensemaking to explain audience and organizational responses.", 86, 4),
    ("MC-728", "MC-200", "RELATED_TO",
     "Strategic narratives are the discursive products of collective sensemaking.", 84, 4),
    ("MC-728", "MDL-076", "RELATED_TO",
     "Organizational change communication models apply sensemaking to change and ambiguity.", 85, 4),
    ("MC-729", "MC-607", "RELATED_TO",
     "Porter's generic strategies are the analytical base Küng adapts to media firms.", 90, 5),
    ("MC-729", "MC-039", "RELATED_TO",
     "Disruptive innovation in media is the core driver of strategic renewal.", 88, 4),
    ("MC-729", "MC-168", "RELATED_TO",
     "The business model canvas operationalizes media strategy choices.", 84, 4),
    ("MC-729", "MC-176", "RELATED_TO",
     "Strategic groups map competitive positions within media industries.", 80, 3),
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
