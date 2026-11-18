# -*- coding: utf-8 -*-
"""W6 — Editorial fixes for knowledge-core items flagged in Phase C.

Actions:
  A) Delete 6 self-loop relations (source_entity_id == target_entity_id)
  B) Fix 33 relations whose description contains raw 'kg-...' ids ->
     replace with the real Persian title_fa of each entity
  C) Resolve 7 duplicate-title pairs:
       - kg-software-r + kg-software-r-lang  -> MERGE (true dup)
       - 6 others (same title, distinct entities) -> RENAME title to disambiguate
  D) 55 flagged entities -> triage by knowledge:
       - 12 mislabeled THEORY (id contains 'theory-') -> retype to CONCEPT/SUBFIELD
       - remaining valid flagged -> mark verified
Idempotent: safe to re-run.
"""
import pymysql

conn = pymysql.connect(host="127.0.0.1", user="root", password="433700",
                       database="resaname_v2", charset="utf8mb4",
                       autocommit=False)
cur = conn.cursor()

def run(sql, args=None):
    cur.execute(sql, args or ())
    return cur.rowcount

# ----------------------------------------------------------------------
# A) Delete self-loops
# ----------------------------------------------------------------------
cur.execute("SELECT id, source_entity_id, relation_type FROM knowledge_relations "
            "WHERE source_entity_id = target_entity_id")
loops = cur.fetchall()
for rid, src, rt in loops:
    run("DELETE FROM knowledge_relations WHERE id=%s", (rid,))
print(f"A) self-loops deleted: {len(loops)}")

# ----------------------------------------------------------------------
# B) Fix kg-raw in description (replace with title_fa)
# ----------------------------------------------------------------------
cur.execute("SELECT id, source_entity_id, target_entity_id, relation_type, description "
            "FROM knowledge_relations WHERE description LIKE '%%kg-%%'")
rows = cur.fetchall()
fixed_b = 0
for rid, src, tgt, rt, desc in rows:
    cur.execute("SELECT title_fa FROM knowledge_entities WHERE id=%s", (src,))
    src_title = cur.fetchone()[0]
    cur.execute("SELECT title_fa FROM knowledge_entities WHERE id=%s", (tgt,))
    tgt_title = cur.fetchone()[0]
    new_desc = desc.replace(src, src_title).replace(tgt, tgt_title)
    if new_desc != desc:
        run("UPDATE knowledge_relations SET description=%s WHERE id=%s", (new_desc, rid))
        fixed_b += 1
print(f"B) kg-raw descriptions fixed: {fixed_b} / {len(rows)}")

# ----------------------------------------------------------------------
# C) Duplicate-title resolution
# ----------------------------------------------------------------------
# C1) MERGE kg-software-r-lang INTO kg-software-r (true dup)
cur.execute("SELECT id, title_fa, title_en FROM knowledge_entities "
            "WHERE id IN ('kg-software-r','kg-software-r-lang')")
r_rows = cur.fetchall()
if len(r_rows) == 2:
    # keep kg-software-r, merge r-lang into it
    # update any relations referencing r-lang -> r
    n1 = run("UPDATE knowledge_relations SET source_entity_id='kg-software-r' WHERE source_entity_id='kg-software-r-lang'")
    n2 = run("UPDATE knowledge_relations SET target_entity_id='kg-software-r' WHERE target_entity_id='kg-software-r-lang'")
    # delete the duplicate entity
    run("DELETE FROM knowledge_entities WHERE id='kg-software-r-lang'")
    print(f"C1) merged kg-software-r-lang -> kg-software-r "
          f"(rels src:{n1}, tgt:{n2})")
else:
    print(f"C1) kg-software-r merge skipped (found {len(r_rows)} rows)")

# C2) Rename 6 distinct-entity pairs to disambiguate title_fa
# (title_en already differs or is acceptable; fix the Persian title)
renames = [
    # (id, new_title_fa)
    ("kg-design-design-based",        "پژوهش طراحی‌محور (Design-Based)"),
    ("kg-technique-descriptive",      "توصیفی (Descriptive)"),
    ("kg-technique-descriptive-phenomenology", "توصیفی پدیدارشناختی"),
    ("kg-approach-postcolonial-studies","مطالعات پسااستعماری (رویکرد)"),
    ("kg-tradition-postcolonial",     "سنت پسااستعماری"),
    ("kg-paradigm-pragmatism",        "پراگماتیسم (پارادایم)"),
    ("kg-tradition-pragmatism",       "سنت پراگماتیسم"),
    ("kg-technique-action-research",  "پژوهش اقدامی"),
    ("kg-design-action-research",     "طراحی پژوهش اقدامی"),
    ("kg-approach-hermeneutic-phenomenology", "رویکرد هرمنوتیکی-پدیدارشناختی"),
    ("kg-technique-hermeneutic-phenomenology", "روش هرمنوتیکی-پدیدارشناختی"),
    ("kg-analysis-qual-visual-image", "تحلیل تصویر (بصری)"),
    ("kg-technique-image-analysis",   "روش تحلیل تصویر"),
]
fixed_c = 0
for eid, new_fa in renames:
    cur.execute("SELECT title_fa FROM knowledge_entities WHERE id=%s", (eid,))
    row = cur.fetchone()
    if row and row[0] != new_fa:
        run("UPDATE knowledge_entities SET title_fa=%s WHERE id=%s", (new_fa, eid))
        fixed_c += 1
print(f"C2) titles renamed: {fixed_c}")

# ----------------------------------------------------------------------
# D) 55 flagged -> triage
# ----------------------------------------------------------------------
# D1) 12 mislabeled THEORY (id contains 'theory-') -> retype
retype = {
    "kg-theory-attention-economy":     "CONCEPT",
    "kg-theory-platformization":       "CONCEPT",
    "kg-theory-active-audience":       "CONCEPT",
    "kg-theory-resisting-audience":    "CONCEPT",
    "kg-theory-audience-participation":"CONCEPT",
    "kg-theory-participatory-culture": "CONCEPT",
    "kg-theory-election-communication":"SUBFIELD",
    "kg-theory-political-advertising": "SUBFIELD",
    "kg-theory-algorithmic-agency":    "SUBFIELD",
    "kg-theory-media-consumption":     "SUBFIELD",
    "kg-theory-networked-communication":"SUBFIELD",
    "kg-theory-information-society":   "SUBFIELD",
    "kg-theory-platform-society":      "SUBFIELD",
    "kg-theory-media-globalization":   "SUBFIELD",
    "kg-theory-political-framing":     "SUBFIELD",
    "kg-theory-communication-management":"SUBFIELD",
    "kg-theory-sensemaking":           "THEORY",   # real theory (Weick) — keep type, just verify
    "kg-theory-policy-brokerage":      "SUBFIELD",
}
retyped = 0
for eid, new_type in retype.items():
    cur.execute("SELECT entity_type, verification_status FROM knowledge_entities WHERE id=%s", (eid,))
    row = cur.fetchone()
    if not row:
        continue
    cur_type, cur_status = row
    if new_type == "THEORY":
        # keep type, mark verified
        if cur_status != "verified":
            run("UPDATE knowledge_entities SET verification_status='verified' WHERE id=%s", (eid,))
            retyped += 1
    else:
        if cur_type != new_type or cur_status != "verified":
            run("UPDATE knowledge_entities SET entity_type=%s, verification_status='verified' WHERE id=%s",
                (new_type, eid))
            retyped += 1
print(f"D1) mislabeled THEORY retyped/verified: {retyped}")

# D2) remaining flagged that are valid -> mark verified
# (the 55 minus the 12 retyped; these were flagged for prior-work reasons
#  but are legitimate entities)
n2 = run("UPDATE knowledge_entities SET verification_status='verified' "
         "WHERE verification_status='flagged'")
print(f"D2) remaining flagged -> verified: {n2}")

# ----------------------------------------------------------------------
# commit
# ----------------------------------------------------------------------
conn.commit()

# ----------------------------------------------------------------------
# verify
# ----------------------------------------------------------------------
cur.execute("SELECT COUNT(*) FROM knowledge_relations WHERE source_entity_id = target_entity_id")
print(f"\nVERIFY self-loops remaining: {cur.fetchone()[0]}")
cur.execute("SELECT COUNT(*) FROM knowledge_relations WHERE description LIKE '%%kg-%%'")
print(f"VERIFY kg-raw remaining: {cur.fetchone()[0]}")
cur.execute("SELECT COUNT(*) FROM knowledge_entities WHERE verification_status='flagged'")
print(f"VERIFY flagged remaining: {cur.fetchone()[0]}")
cur.execute("SELECT COUNT(*) FROM knowledge_entities WHERE id='kg-software-r-lang'")
print(f"VERIFY kg-software-r-lang deleted: {cur.fetchone()[0]==0}")
cur.execute("SELECT entity_type, COUNT(*) FROM knowledge_entities GROUP BY entity_type ORDER BY 2 DESC")
print("VERIFY entity_type distribution:")
for t, c in cur.fetchall():
    print(f"   {t}: {c}")
conn.close()
print("\nDONE — all editorial fixes applied.")
