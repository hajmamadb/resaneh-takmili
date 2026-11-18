# -*- coding: utf-8 -*-
"""Batch 192 relations."""
import pymysql

DB = "resaname_kb_final_inspect"
ASSERTED = "qoder-rel-batch192-20261116"
VERIFIED = "qoder-verify-batch192"

ROWS = [
    ("card-71", "MTH-002", "RELATED_TO",
     "Grounded theory is one of the canonical qualitative methodologies: inductive, interpretive and theory-generating rather than hypothesis-testing.", 92, 5),
    ("card-71", "MC-484", "RELATED_TO",
     "Both work on interview and field material through iterative coding; grounded theory supplies the coding paradigm that narrative analysis often borrows.", 82, 3),
    ("card-71", "MC-717", "RELATED_TO",
     "Digital-media ethnography routinely uses grounded-theory coding to turn fieldnotes and platform traces into categories.", 80, 3),
    ("card-71", "MC-073", "RELATED_TO",
     "Grounded theory's constant comparison is a form of within-method triangulation across data sources, investigators and time.", 78, 3),
    ("card-77", "MTH-002", "RELATED_TO",
     "Q-methodology is anchored in qualitative epistemology: it studies subjectivity and viewpoint structure rather than population parameters.", 88, 4),
    ("card-77", "MTH-001", "RELATED_TO",
     "Q combines qualitative statement selection with quantitative factor analysis, so it is often classed as a mixed or qualiquantological design.", 86, 4),
    ("card-77", "MC-239", "RELATED_TO",
     "Q is a standard example of a mixed-methods design that joins structured ranking with interpretive factor reading.", 84, 4),
    ("card-77", "MTH-003", "RELATED_TO",
     "Q factors are competing discourses about an issue, so factor interpretation converges with discourse analysis of viewpoint positions.", 80, 3),
    ("MTH-006", "MTH-007", "RELATED_TO",
     "Digital media analysis often feeds computational pipelines (network metrics, automated classification), and the two are frequently combined.", 90, 5),
    ("MTH-006", "MC-717", "RELATED_TO",
     "Digital-media ethnography shares the natively digital field but adds sustained observation and participant interpretation to platform data.", 86, 4),
    ("MTH-006", "MC-718", "RELATED_TO",
     "Social network analysis supplies the core graph measures used to map information flows and interaction structures online.", 88, 4),
    ("MTH-006", "MC-080", "RELATED_TO",
     "Digital methods is a methodological strand of computational social science, sharing its data sources while insisting on medium-specific techniques.", 84, 4),
    ("MTH-007", "MC-080", "RELATED_TO",
     "Computational analysis is the toolkit of computational social science, whose programmatic statement is the Lazer et al. manifesto.", 92, 5),
    ("MTH-007", "MC-072", "RELATED_TO",
     "Automated text classification extends quantitative content analysis to corpora far beyond manual coding capacity.", 88, 4),
    ("MTH-007", "MC-718", "RELATED_TO",
     "Computational analysis of networks applies graph algorithms and machine learning to large-scale relational data.", 86, 4),
    ("MTH-007", "MTH-006", "RELATED_TO",
     "Computational analysis provides the algorithms that digital media analysis applies to platform-native data.", 90, 5),
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
