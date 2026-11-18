# -*- coding: utf-8 -*-
"""Batch 193 relations."""
import pymysql

DB = "resaname_kb_final_inspect"
ASSERTED = "qoder-rel-batch193-20261116"
VERIFIED = "qoder-verify-batch193"

ROWS = [
    ("DSC-015", "MC-507", "RELATED_TO",
     "Media management studies is the applied discipline built on the strategic management of media organizations.", 92, 5),
    ("DSC-015", "MC-166", "RELATED_TO",
     "Cultural-industry economics supplies the market and labour conditions that media managers must strategize around.", 84, 4),
    ("DSC-015", "MC-040", "RELATED_TO",
     "The crisis of the news business model is the concrete strategic problem that media management addresses.", 86, 4),
    ("DSC-015", "SFL-004", "RELATED_TO",
     "Platform studies reframes media strategy around platform dependence, data and algorithmic distribution.", 82, 3),
    ("DSC-016", "CPT-117", "RELATED_TO",
     "Freedom of expression is the core legal value that media law and policy must balance against harm.", 92, 5),
    ("DSC-016", "CPT-268", "RELATED_TO",
     "Media regulation is the institutional instrument through which media policy is implemented.", 92, 5),
    ("DSC-016", "CPT-270", "RELATED_TO",
     "Platform liability is the central contemporary question of media law in the platform era.", 88, 4),
    ("DSC-016", "MC-060", "RELATED_TO",
     "Platform governance and intermediary immunity provide the doctrinal frame for allocating responsibility online.", 86, 4),
    ("DSC-017", "MC-011", "RELATED_TO",
     "The knowledge-gap hypothesis is one of the empirical findings that science communication must explain and counter.", 86, 4),
    ("DSC-017", "CPT-071", "RELATED_TO",
     "Trust in media and institutions is the key mediating variable in public uptake of science.", 88, 4),
    ("DSC-017", "CPT-072", "RELATED_TO",
     "Media literacy is a primary intervention through which science communication builds public evaluation skills.", 84, 4),
    ("DSC-017", "SFL-010", "RELATED_TO",
     "Misinformation studies is the subfield where science communication confronts contested and false scientific claims.", 86, 4),
    ("DSC-018", "CPT-281", "RELATED_TO",
     "Digital religion is the core object of religious communication studies in networked settings.", 92, 5),
    ("DSC-018", "CPT-290", "RELATED_TO",
     "Media authority is reshaped when religious authority is negotiated through media institutions.", 84, 4),
    ("DSC-018", "CPT-302", "RELATED_TO",
     "Digital authority describes the redistribution of religious legitimation across platforms and influencers.", 86, 4),
    ("DSC-018", "CPT-297", "RELATED_TO",
     "Religious media literacy is the applied competence that religious communication studies aims to cultivate.", 80, 3),
    ("DSC-019", "MC-133", "RELATED_TO",
     "The health belief model is a core behavioural frame used to design health communication interventions.", 90, 5),
    ("DSC-019", "MC-497", "RELATED_TO",
     "Situational crisis communication theory guides message design in health and environmental crises.", 88, 4),
    ("DSC-019", "MC-004", "RELATED_TO",
     "Media framing determines how health and environmental risks are interpreted by audiences.", 86, 4),
    ("DSC-019", "CPT-256", "RELATED_TO",
     "Health misinformation is a central challenge for health and environment communication campaigns.", 88, 4),
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
