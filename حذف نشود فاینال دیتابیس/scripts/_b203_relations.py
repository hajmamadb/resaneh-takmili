# -*- coding: utf-8 -*-
"""Batch 203 relations."""
import pymysql

DB = "resaname_kb_final_inspect"
ASSERTED = "qoder-rel-batch203-20261117"
VERIFIED = "qoder-verify-batch203"

ROWS = [
    ("MC-653", "MC-428", "RELATED_TO",
     "Diffusion of innovations supplies the firm-level adoption logic TOE contextualizes.", 88, 4),
    ("MC-653", "MC-645", "RELATED_TO",
     "UTAUT2 is the individual-level consumer counterpart of the firm-level TOE framework.", 84, 4),
    ("MC-653", "MC-155", "RELATED_TO",
     "Organizational learning explains how adoption capacity changes over time.", 82, 3),
    ("MC-653", "MC-169", "RELATED_TO",
     "Platformization is a key environmental pressure driving media firms' technology adoption.", 84, 4),
    ("MC-660", "MC-251", "RELATED_TO",
     "The strength of weak ties explains the bridging role closure cannot provide.", 92, 5),
    ("MC-660", "MC-659", "RELATED_TO",
     "Homophily is the selection mechanism behind triadic closure.", 90, 5),
    ("MC-660", "MC-254", "RELATED_TO",
     "Preferential attachment complements closure in explaining network clustering.", 82, 3),
    ("MC-660", "MC-253", "RELATED_TO",
     "Small-world networks combine clustering (closure) with short path lengths.", 84, 4),
    ("MC-461", "MC-095", "RELATED_TO",
     "Orientalism theory is the media-studies operationalization of this framework.", 94, 5),
    ("MC-461", "TX-028", "RELATED_TO",
     "Postcolonial theory is the broader intellectual tradition the framework belongs to.", 90, 5),
    ("MC-461", "MC-232", "RELATED_TO",
     "Colonial power is the structural condition representation helps legitimize.", 84, 4),
    ("MC-461", "MC-278", "RELATED_TO",
     "Data colonialism extends the othering critique to digital extraction.", 82, 3),
    ("MC-363", "MC-328", "RELATED_TO",
     "Framing theory supplies the selection and salience operations the cascade distributes.", 92, 5),
    ("MC-363", "MC-004", "RELATED_TO",
     "Media framing research provides the newsroom-level evidence of frame transmission.", 86, 4),
    ("MC-363", "MC-001", "RELATED_TO",
     "Agenda setting is the parallel top-down influence process at the issue level.", 84, 4),
    ("MC-363", "MC-220", "RELATED_TO",
     "Policy narrative analysis tracks elite frames in policy contests.", 80, 3),
    ("MC-572", "MC-133", "RELATED_TO",
     "The health belief model is the main rival individual-level model in health campaigns.", 86, 4),
    ("MC-572", "MC-027", "RELATED_TO",
     "The theory of planned behavior explains intention formation within stages.", 84, 4),
    ("MC-572", "MC-137", "RELATED_TO",
     "Behavioral nudges operationalize stage-matched persuasion at scale.", 82, 3),
    ("MC-572", "CPT-213", "RELATED_TO",
     "Behavioral intention is the proximal outcome stage-matched messages target.", 80, 3),
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
