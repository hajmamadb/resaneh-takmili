# -*- coding: utf-8 -*-
"""Batch 196 relations."""
import pymysql

DB = "resaname_kb_final_inspect"
ASSERTED = "qoder-rel-batch196-20261116"
VERIFIED = "qoder-verify-batch196"

ROWS = [
    ("SFL-011", "MC-112", "RELATED_TO",
     "The filter bubble thesis is the most debated mechanism this subfield tests empirically.", 90, 5),
    ("SFL-011", "MC-113", "RELATED_TO",
     "Echo chamber theory explains the social reinforcement of like-minded belief.", 88, 4),
    ("SFL-011", "MC-205", "RELATED_TO",
     "Affective polarization is a core outcome measured in digital polarization research.", 86, 4),
    ("SFL-011", "TX-091", "RELATED_TO",
     "Political polarization theory supplies the baseline against which digital amplification is assessed.", 84, 4),
    ("SFL-012", "MC-227", "RELATED_TO",
     "Computational propaganda is the data-driven operational layer of cognitive warfare.", 90, 5),
    ("SFL-012", "TX-089", "RELATED_TO",
     "Psychological warfare theory is the historical predecessor of cognitive warfare.", 86, 4),
    ("SFL-012", "MC-370", "RELATED_TO",
     "Propaganda and opinion manipulation studies provide the conceptual vocabulary for strategic influence.", 84, 4),
    ("SFL-012", "MC-582", "RELATED_TO",
     "The ethics of persuasion framework marks the boundary between legitimate and manipulative influence.", 80, 3),
    ("SFL-013", "MC-671", "RELATED_TO",
     "Contextual integrity is the normative standard this subfield uses to judge privacy violations.", 90, 5),
    ("SFL-013", "MC-285", "RELATED_TO",
     "Dataveillance describes the monitoring risk that security and communication studies analyze together.", 86, 4),
    ("SFL-013", "MC-435", "RELATED_TO",
     "Panoptic surveillance theory frames the power asymmetry of communication monitoring.", 82, 3),
    ("SFL-013", "MC-118", "RELATED_TO",
     "Surveillance capitalism links data security failures to commercial extraction of behavioral data.", 84, 4),
    ("SFL-014", "MC-048", "RELATED_TO",
     "The hybrid media system theory is the central framework for ecosystem-level analysis.", 92, 5),
    ("SFL-014", "CPT-049", "RELATED_TO",
     "The media ecosystem concept is the unit of analysis for this subfield.", 90, 5),
    ("SFL-014", "MC-009", "RELATED_TO",
     "Media system dependency theory explains how actors rely on the ecosystem for information.", 84, 4),
    ("SFL-014", "MC-117", "RELATED_TO",
     "The platform society specifies how platform institutions reshape the ecosystem's power structure.", 84, 4),
    ("SFL-015", "MC-114", "RELATED_TO",
     "Participatory culture theory is the foundational concept of this subfield.", 92, 5),
    ("SFL-015", "MC-453", "RELATED_TO",
     "Convergence culture explains how audience participation crosses media platforms.", 88, 4),
    ("SFL-015", "MDL-039", "RELATED_TO",
     "The participatory content production model describes the workflow through which audiences create.", 82, 3),
    ("SFL-015", "MC-366", "RELATED_TO",
     "Participatory journalism applies participatory culture to news production and audience contribution.", 84, 4),
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
