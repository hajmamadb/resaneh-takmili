# -*- coding: utf-8 -*-
"""Batch 189 relations."""
import pymysql

DB = "resaname_kb_final_inspect"
ASSERTED = "qoder-rel-batch189-20261116"
VERIFIED = "qoder-verify-batch189"

ROWS = [
    ("MC-153", "MC-151", "RELATED_TO",
     "Two competing strategy frameworks: Porter chooses a defensible position inside an existing industry, while blue ocean strategy redesigns industry boundaries to create uncontested demand.", 86, 4),
    ("MC-153", "MC-161", "RELATED_TO",
     "Blue ocean creation is the strategic answer to winner-take-all star markets: rather than contest a concentrated market, the firm opens a new space where the star dynamic does not yet apply.", 82, 3),
    ("MC-153", "CPT-180", "RELATED_TO",
     "Value innovation is presented as a route to competitive advantage that sidesteps the cost-versus-differentiation trade-off on which the competitive advantage concept rests.", 84, 4),
    ("MC-153", "MC-171", "RELATED_TO",
     "Both frameworks treat rivals as interdependent actors: co-opetition through value nets and complementors, blue ocean through noncustomers and complementary offerings.", 78, 3),
    ("MC-277", "MC-355", "RELATED_TO",
     "Gamification is read critically as a way of channeling audience activity: the same active audience that resists media power can be steered through reward loops and visible progress.", 80, 3),
    ("MC-277", "MC-225", "RELATED_TO",
     "Game elements operationalize engagement metrics inside algorithmic platforms, making participation measurable and rankable and tying user behavior to platform governance.", 85, 4),
    ("MC-277", "CPT-056", "RELATED_TO",
     "Gamified interfaces reshape media consumption by attaching points, streaks and levels to reading, listening and sharing, turning consumption into a tracked routine.", 88, 4),
    ("MC-277", "MC-369", "RELATED_TO",
     "Reward loops and progress tracking are a soft form of engineering consent: they make continued engagement feel voluntary while structuring the choices users can make.", 76, 3),
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
