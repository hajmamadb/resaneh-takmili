# -*- coding: utf-8 -*-
"""Batch 204 relations."""
import pymysql

DB = "resaname_kb_final_inspect"
ASSERTED = "qoder-rel-batch204-20261117"
VERIFIED = "qoder-verify-batch204"

ROWS = [
    ("MC-078", "MC-719", "RELATED_TO",
     "Experimental communication research is the applied setting where validity threats are managed.", 92, 5),
    ("MC-078", "MC-576", "RELATED_TO",
     "Confirmation bias is one of the threats experimental design must control.", 82, 3),
    ("MC-078", "MC-238", "RELATED_TO",
     "Platform experiment ethics raise the external-validity and consent limits of lab designs.", 84, 4),
    ("MC-078", "MC-575", "RELATED_TO",
     "Decision framing effects are a typical causal claim tested by experimental designs.", 80, 3),
    ("MC-199", "SFL-010", "RELATED_TO",
     "Disinformation and fake news studies are the subfield this typology organizes.", 94, 5),
    ("MC-199", "MC-530", "RELATED_TO",
     "The misinformation/post-truth theory provides the broader diagnosis the typology refines.", 90, 5),
    ("MC-199", "MC-705", "RELATED_TO",
     "The fake news and fact-checking model operationalizes disorder detection.", 86, 4),
    ("MC-199", "CPT-248", "RELATED_TO",
     "Fact-checking is the main corrective practice against information disorder.", 84, 4),
    ("MC-481", "MC-345", "RELATED_TO",
     "Triadic semiotics is the model-level restatement of Peirce's sign triad.", 92, 5),
    ("MC-481", "MC-480", "RELATED_TO",
     "Structural semiotics offers the Saussurean alternative Peirce's triad contrasts with.", 88, 4),
    ("MC-481", "MC-075", "RELATED_TO",
     "Semiotics is the discipline in which this framework operates.", 90, 5),
    ("MC-481", "MC-715", "RELATED_TO",
     "Semiotic analysis is the method that applies the triad to media texts.", 86, 4),
    ("MC-582", "TX-016", "RELATED_TO",
     "Persuasion theory supplies the effects the ethical test constrains.", 90, 5),
    ("MC-582", "MC-165", "RELATED_TO",
     "The informational versus persuasive advertising debate hinges on the TARES criteria.", 84, 4),
    ("MC-582", "CPT-261", "RELATED_TO",
     "Media ethics is the professional field where the framework is applied.", 86, 4),
    ("MC-582", "TX-087", "RELATED_TO",
     "Political advertising theory is a high-stakes test case for ethical persuasion.", 82, 3),
    ("MC-598", "MC-141", "RELATED_TO",
     "Excellence theory is the normative benchmark for symmetric meaning management.", 88, 4),
    ("MC-598", "MC-373", "RELATED_TO",
     "Dialogic public relations operationalizes the public dialogue component.", 86, 4),
    ("MC-598", "MC-447", "RELATED_TO",
     "Sensemaking theory explains how organizational meaning is produced collectively.", 82, 3),
    ("MC-598", "MC-379", "RELATED_TO",
     "Reputation management is the instrumental outcome of meaning management.", 84, 4),
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
