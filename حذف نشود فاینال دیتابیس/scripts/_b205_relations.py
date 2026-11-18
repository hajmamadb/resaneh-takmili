# -*- coding: utf-8 -*-
"""Batch 205 relations + card-403 theorist name repair."""
import pymysql

DB = "resaname_kb_final_inspect"
ASSERTED = "qoder-rel-batch205-20261117"
VERIFIED = "qoder-verify-batch205"

ROWS = [
    ("MC-678", "MC-677", "RELATED_TO",
     "Collective memory theory is the general theory this framework operationalizes for media.", 92, 5),
    ("MC-678", "TX-069", "RELATED_TO",
     "Collective memory theory supplies the social-frameworks account of remembering.", 88, 4),
    ("MC-678", "TX-070", "RELATED_TO",
     "Cultural memory theory extends forgetting beyond the news cycle into long-term identity.", 84, 4),
    ("MC-678", "CPT-144", "RELATED_TO",
     "Collective memory is the core concept the framework builds on.", 90, 5),
    ("MC-694", "card-403", "RELATED_TO",
     "The MacBride Report is the founding document of the New World Information and Communication Order.", 96, 5),
    ("MC-694", "MC-193", "RELATED_TO",
     "The one-way flow of global news is the imbalance the report documented.", 90, 5),
    ("MC-694", "MC-477", "RELATED_TO",
     "Cultural and media imperialism theory frames the structural critique of the report.", 86, 4),
    ("MC-694", "MC-513", "RELATED_TO",
     "World information system theory formalizes the global structure the report proposed to reform.", 84, 4),
    ("card-403", "MC-694", "RELATED_TO",
     "The MacBride Report is the primary source and policy articulation of NWICO.", 96, 5),
    ("card-403", "MC-193", "RELATED_TO",
     "The one-way news flow is the empirical pattern NWICO sought to correct.", 90, 5),
    ("card-403", "CPT-273", "RELATED_TO",
     "Media justice is the normative concept that carries NWICO's agenda today.", 86, 4),
    ("card-403", "MC-513", "RELATED_TO",
     "World information system theory is the macro-theoretical companion of NWICO.", 84, 4),
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

# card-403: misspelled theorist name in nested list
cur.execute("SELECT id, properties FROM kb_entities WHERE code='card-403'")
eid, props = cur.fetchone()
if "Shane McBrady" in props:
    props = props.replace("Shane McBrady", "Seán MacBride")
    cur.execute("UPDATE kb_entities SET properties=%s WHERE id=%s", (props, eid))
    cur.execute("""INSERT INTO kb_audit_log (entity_code,action,detail,source,created_at)
        VALUES ('card-403','DOC_FIX',%s,%s,'2026-11-17 00:00:00')""",
                ('{"fix": "Shane McBrady -> Seán MacBride"}', "qoder-doc-batch205-20261117"))

c.commit()
c.close()
print("inserted=%d skipped=%d" % (inserted, skipped))
