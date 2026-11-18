# -*- coding: utf-8 -*-
"""Batch 191 relations."""
import pymysql

DB = "resaname_kb_final_inspect"
ASSERTED = "qoder-rel-batch191-20261116"
VERIFIED = "qoder-verify-batch191"

ROWS = [
    ("th-16", "TX-057", "RELATED_TO",
     "Group dynamics is the research tradition Lewin founded, and its theory entry draws directly on his field-theoretic account of groups.", 90, 5),
    ("th-16", "TX-056", "RELATED_TO",
     "Lewin's field theory treats group decisions as equilibria of forces, a foundation for later group decision-making theory.", 80, 3),
    ("th-16", "CPT-216", "RELATED_TO",
     "Lewin's unfreeze-change-refreeze account is an early framework for intentional behavior change.", 84, 4),
    ("th-16", "MC-572", "RELATED_TO",
     "Both frame behavior change as a staged process rather than a single event: Lewin through field equilibria, the transtheoretical model through readiness stages.", 78, 3),
    ("th-27", "MC-075", "RELATED_TO",
     "Barthes is a founding figure of semiology, the science of signs that the semiotics entry formalizes.", 90, 5),
    ("th-27", "MC-333", "RELATED_TO",
     "Barthes' myth analysis supplied British cultural studies with a method for reading ideology in popular culture.", 86, 4),
    ("th-27", "MC-091", "RELATED_TO",
     "Myth's naturalizing function is a semiotic counterpart to cultural hegemony: both explain how domination appears as common sense.", 84, 4),
    ("th-27", "MC-484", "RELATED_TO",
     "Barthes' structural analysis of narrative and the readerly/writerly distinction feed directly into narrative analysis.", 82, 3),
    ("th-32", "MC-166", "RELATED_TO",
     "The audience commodity thesis is a political-economy account of the cultural industries under advertising finance.", 88, 4),
    ("th-32", "MC-091", "RELATED_TO",
     "Selling audience attention links commercial media to ideological reproduction, the terrain of cultural hegemony.", 80, 3),
    ("th-32", "MC-225", "RELATED_TO",
     "The audience commodity is generalized in algorithmic culture, where user data and attention are continuously commodified.", 86, 4),
    ("th-32", "CPT-056", "RELATED_TO",
     "Smythe reframes media consumption as productive audience work sold to advertisers.", 88, 4),
    ("th-38", "MC-166", "RELATED_TO",
     "Hesmondhalgh's cultural industries framework is the major contemporary restatement of the cultural industries theory entry.", 92, 5),
    ("th-38", "MC-225", "RELATED_TO",
     "Platformization reorganizes cultural-industry labour and distribution, extending Hesmondhalgh's political economy to algorithmic media.", 84, 4),
    ("th-38", "MC-161", "RELATED_TO",
     "Star formation in cultural markets is an instance of winner-take-all dynamics driven by demand uncertainty and low reproduction costs.", 82, 3),
    ("th-38", "CPT-056", "RELATED_TO",
     "Cultural-industry analysis connects consumption to production conditions: what audiences consume is shaped by risk, labour and market structure.", 80, 3),
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
