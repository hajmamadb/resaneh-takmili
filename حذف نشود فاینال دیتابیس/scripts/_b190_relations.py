# -*- coding: utf-8 -*-
"""Batch 190 relations."""
import pymysql

DB = "resaname_kb_final_inspect"
ASSERTED = "qoder-rel-batch190-20261116"
VERIFIED = "qoder-verify-batch190"

ROWS = [
    ("card-479", "MC-344", "RELATED_TO",
     "Heidegger's Gestell essay is a founding text of the humanities tradition in the philosophy of technology, the tradition this school entry surveys.", 88, 4),
    ("card-479", "MC-472", "RELATED_TO",
     "Marcuse's one-dimensionality is a critical-theory diagnosis of technology and instrumental reason, a central position within the philosophy of technology.", 84, 4),
    ("card-479", "MC-476", "RELATED_TO",
     "Virilio's technology-and-civilization argument is a substantive position inside the philosophy of technology, stressing speed and accident.", 80, 3),
    ("card-479", "MC-727", "RELATED_TO",
     "Philosophy of media extends the philosophy of technology to mediation, perception and the materiality of communication.", 86, 4),
    ("card-33", "MC-161", "RELATED_TO",
     "Network effects are the demand-side mechanism behind winner-take-all and star markets: value concentration follows from compatible user bases.", 88, 5),
    ("card-33", "MC-602", "RELATED_TO",
     "Both are scaling laws of digital infrastructure: Nielsen's law describes bandwidth supply growth, while network effects describe demand-side value growth.", 78, 3),
    ("card-33", "MC-418", "RELATED_TO",
     "Collective intelligence is an application of network effects: the value of shared knowledge grows with the number and connectivity of participants.", 82, 3),
    ("card-33", "MDL-060", "RELATED_TO",
     "Internet television business models rely on cross-side network effects between audiences, content providers and advertisers.", 84, 4),
    ("card-581", "MC-030", "RELATED_TO",
     "Psychological reactance theory supplies the main mechanism explaining why persuasive pressure can produce the opposite of the intended response.", 90, 5),
    ("card-581", "CPT-100", "RELATED_TO",
     "The boomerang effect is a failure mode of persuasion, defined against the intended direction of attitude change.", 88, 4),
    ("card-581", "MC-369", "RELATED_TO",
     "Engineering consent assumes campaigns can steer public opinion; boomerang findings mark the limits of that assumption under identity threat.", 80, 3),
    ("card-581", "MC-355", "RELATED_TO",
     "The active audience that resists media power is the same audience whose reactance and motivated reasoning produce boomerang effects.", 86, 4),
    ("res-e081bac707848a7377a4", "MC-075", "RELATED_TO",
     "Semiotics is one of the seven traditions in Craig's map of communication theory and a core theory of meaning in the field.", 86, 4),
    ("res-e081bac707848a7377a4", "MC-091", "RELATED_TO",
     "Cultural hegemony belongs to the critical tradition of communication theory, concerned with power and ideology in meaning-making.", 84, 4),
    ("res-e081bac707848a7377a4", "MC-727", "RELATED_TO",
     "Philosophy of media is a contemporary theoretical stream within the broader field of communication theories.", 80, 3),
    ("res-e081bac707848a7377a4", "MC-418", "RELATED_TO",
     "Cyberculture and collective intelligence extend communication theory to networked, algorithmically mediated publics.", 78, 3),
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
