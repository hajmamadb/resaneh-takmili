# -*- coding: utf-8 -*-
"""Batch 194 relations."""
import pymysql

DB = "resaname_kb_final_inspect"
ASSERTED = "qoder-rel-batch194-20261116"
VERIFIED = "qoder-verify-batch194"

ROWS = [
    ("SFL-001", "MC-531", "RELATED_TO",
     "Generative AI in media is the applied object this subfield analyzes for provenance, trust and machine agency.", 90, 5),
    ("SFL-001", "MC-421", "RELATED_TO",
     "Automated and algorithmic journalism is an early institutional site of human-machine communication.", 86, 4),
    ("SFL-001", "MC-704", "RELATED_TO",
     "Algorithmic gatekeeping is the selection layer through which communicative AI shapes what audiences see.", 82, 3),
    ("SFL-001", "MC-080", "RELATED_TO",
     "Computational social science supplies quantitative methods for studying machine-produced content and interaction.", 78, 3),
    ("SFL-002", "MC-119", "RELATED_TO",
     "The algorithmic imaginary operationalizes how users perceive and respond to algorithmic relevance.", 90, 5),
    ("SFL-002", "MC-225", "RELATED_TO",
     "Algorithmic culture is the broader cultural condition within which algorithm and media studies operates.", 88, 4),
    ("SFL-002", "MC-434", "RELATED_TO",
     "The black box theory of algorithms names the opacity problem at the core of this field.", 86, 4),
    ("SFL-002", "MC-667", "RELATED_TO",
     "Algorithmic salience theory explains how ranking systems make certain items prominent.", 82, 3),
    ("SFL-003", "MC-080", "RELATED_TO",
     "Data and communication studies shares computational social science's methods while adding a critique of datafication.", 84, 4),
    ("SFL-003", "MTH-006", "RELATED_TO",
     "Digital media analysis provides methods for studying platform data as communication traces.", 84, 4),
    ("SFL-003", "MTH-007", "RELATED_TO",
     "Computational analysis is the technical repertoire through which communication data is processed at scale.", 80, 3),
    ("SFL-003", "MC-730", "RELATED_TO",
     "Platformization explains the institutional context in which communication data is captured and commodified.", 82, 3),
    ("SFL-004", "MC-117", "RELATED_TO",
     "The platform society is the macro-level theory that platform studies operationalizes empirically.", 92, 5),
    ("SFL-004", "MC-169", "RELATED_TO",
     "Platformization is the core process this subfield traces across media and non-media sectors.", 90, 5),
    ("SFL-004", "MC-222", "RELATED_TO",
     "Platform capitalism supplies the political-economic account of the platform business model.", 86, 4),
    ("SFL-004", "MDL-038", "RELATED_TO",
     "Media as platform is the media-specific model through which platform logic enters communication research.", 84, 4),
    ("SFL-005", "MC-032", "RELATED_TO",
     "The attention economy theory is the foundational framework of attention economy studies.", 92, 5),
    ("SFL-005", "MC-383", "RELATED_TO",
     "Attention merchants describes the historical practice of harvesting and reselling audience attention.", 86, 4),
    ("SFL-005", "MC-154", "RELATED_TO",
     "The attention-based view connects media attention metrics to organizational and audience behavior.", 80, 3),
    ("SFL-005", "MC-676", "RELATED_TO",
     "The affective economy links engagement-driven attention capture to emotional content production.", 80, 3),
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
