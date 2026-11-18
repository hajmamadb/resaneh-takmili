# -*- coding: utf-8 -*-
"""Batch 195 relations."""
import pymysql

DB = "resaname_kb_final_inspect"
ASSERTED = "qoder-rel-batch195-20261116"
VERIFIED = "qoder-verify-batch195"

ROWS = [
    ("SFL-006", "MC-610", "RELATED_TO",
     "Creator economy is the core model this subfield analyzes for revenue, platform dependency and creative labor.", 92, 5),
    ("SFL-006", "CPT-235", "RELATED_TO",
     "Influencer marketing is the main commercial interface between creator audiences and advertisers.", 86, 4),
    ("SFL-006", "MC-262", "RELATED_TO",
     "The subscription economy supplies one of the recurring revenue models on which creators depend.", 82, 3),
    ("SFL-006", "MDL-037", "RELATED_TO",
     "The content-economy model frames how creator output is packaged, distributed and monetized.", 80, 3),
    ("SFL-007", "MC-520", "RELATED_TO",
     "Virtual reality is the technology framework whose experiences this subfield studies.", 90, 5),
    ("SFL-007", "MC-241", "RELATED_TO",
     "Social presence theory explains the felt co-presence that immersive media aim to produce.", 86, 4),
    ("SFL-007", "CPT-207", "RELATED_TO",
     "Virtual presence is the core experiential concept operationalized in VR research.", 84, 4),
    ("SFL-007", "SFL-008", "RELATED_TO",
     "Metaverse studies extends immersive VR from single experiences to persistent shared environments.", 82, 3),
    ("SFL-008", "MC-520", "RELATED_TO",
     "Metaverse environments build on virtual reality frameworks and hardware.", 86, 4),
    ("SFL-008", "CPT-207", "RELATED_TO",
     "Ubiquitous immersive communication depends on producing presence across distributed environments.", 80, 3),
    ("SFL-008", "MC-730", "RELATED_TO",
     "Platformization is the economic and institutional process through which metaverse worlds are governed and monetized.", 82, 3),
    ("SFL-008", "MC-169", "RELATED_TO",
     "Platformization theory helps explain interoperability conflicts and walled gardens among metaverse operators.", 80, 3),
    ("SFL-009", "MC-080", "RELATED_TO",
     "Computational social science is the adjacent field from which computational communication studies borrows methods.", 90, 5),
    ("SFL-009", "MTH-007", "RELATED_TO",
     "Computational analysis is the core methodological repertoire of this subfield.", 88, 4),
    ("SFL-009", "MTH-006", "RELATED_TO",
     "Digital media analysis supplies the data-collection and platform-research techniques used here.", 84, 4),
    ("SFL-009", "SFL-003", "RELATED_TO",
     "Data and communication studies shares the datafication critique that computational communication must address.", 82, 3),
    ("SFL-010", "MC-530", "RELATED_TO",
     "The misinformation, fake news and post-truth theory is the conceptual core of this research area.", 92, 5),
    ("SFL-010", "MC-674", "RELATED_TO",
     "The fake-information diffusion model explains the spread dynamics this subfield measures.", 86, 4),
    ("SFL-010", "MC-705", "RELATED_TO",
     "The fake news and fact-checking model links correction practices to reception research.", 84, 4),
    ("SFL-010", "CPT-072", "RELATED_TO",
     "Media literacy is the main demand-side intervention against misinformation.", 82, 3),
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
