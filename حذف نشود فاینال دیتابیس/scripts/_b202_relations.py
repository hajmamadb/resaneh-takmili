# -*- coding: utf-8 -*-
"""Batch 202 relations."""
import pymysql

DB = "resaname_kb_final_inspect"
ASSERTED = "qoder-rel-batch202-20261117"
VERIFIED = "qoder-verify-batch202"

ROWS = [
    ("MC-638", "MC-140", "RELATED_TO",
     "Public diplomacy is the state-led counterpart of media-driven foreign policy pressure.", 84, 4),
    ("MC-638", "MC-085", "RELATED_TO",
     "Public opinion and the pseudo-environment explain the domestic pressure the CNN effect transmits.", 86, 4),
    ("MC-638", "MC-219", "RELATED_TO",
     "Humanitarian spectatorship describes the distant-suffering audience real-time coverage mobilizes.", 84, 4),
    ("MC-638", "SFL-012", "RELATED_TO",
     "Strategic communication studies frame the policy-media relation as an influence contest.", 82, 3),
    ("MC-642", "MC-117", "RELATED_TO",
     "The platform society shows how private platforms now exercise governance functions.", 90, 5),
    ("MC-642", "MC-060", "RELATED_TO",
     "Platform governance and intermediary immunity are concrete regimes inside the Internet governance framework.", 90, 5),
    ("MC-642", "MC-051", "RELATED_TO",
     "Privacy is a core rights layer negotiated within Internet governance.", 84, 4),
    ("MC-642", "MC-120", "RELATED_TO",
     "The digital divide marks the distributive failure Internet governance must address.", 84, 4),
    ("MC-442", "MC-216", "RELATED_TO",
     "Cultural proximity theory operationalizes cross-cultural difference in media reception.", 84, 4),
    ("MC-442", "CPT-148", "RELATED_TO",
     "Cultural globalization debates use national value dimensions as an analytic baseline.", 82, 3),
    ("MC-442", "MC-231", "RELATED_TO",
     "Cultural mediation explains how value orientations shape meaning-making.", 80, 3),
    ("MC-442", "MC-189", "RELATED_TO",
     "Organizational culture research applies the dimensions to institutional communication.", 82, 3),
    ("MC-645", "MC-413", "RELATED_TO",
     "The original UTAUT is the direct predecessor UTAUT2 extends for consumers.", 94, 5),
    ("MC-645", "MC-412", "RELATED_TO",
     "The technology acceptance model supplies the perceived usefulness and ease-of-use constructs.", 90, 5),
    ("MC-645", "MC-120", "RELATED_TO",
     "The digital divide qualifies acceptance findings by access and skills inequality.", 82, 3),
    ("MC-645", "MDL-025", "RELATED_TO",
     "Audience acceptance models parallel consumer acceptance in media use research.", 80, 3),
    ("MC-647", "MC-516", "RELATED_TO",
     "Mediation theory is the broader frame within which remediation operates.", 90, 5),
    ("MC-647", "MC-520", "RELATED_TO",
     "Virtual reality is a central case of immediacy-driven remediation.", 88, 4),
    ("MC-647", "SFL-007", "RELATED_TO",
     "VR/AR studies apply remediation to immersive media genealogies.", 84, 4),
    ("MC-647", "MC-169", "RELATED_TO",
     "Platformization extends remediation logic to platform infrastructures.", 82, 3),
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
