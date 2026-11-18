# -*- coding: utf-8 -*-
"""W8 — Verify knowledge_relations by confidence tier + refine high-confidence RELATED_TO.

Gaps found in W7 audit:
  1. ALL 1066 knowledge_relations are 'unverified' — even though Phase C
     verified the entities they connect. This is a real gap.
  2. 99 RELATED_TO fallback relations: 70 have confidence >= 0.85, many of
     which are actually more specific (IS_A, PART_OF, USES, APPLIES_TO...).
     These can be refined. The remaining ~29 are genuine cross-links.

Strategy:
  A) Verify knowledge_relations by confidence:
       confidence >= 0.80  -> 'verified' (the 596 + 424 = 1020 high/med)
       confidence  0.70-0.79 -> 'needs_review' (the 46 low, for human pass)
  B) Refine high-confidence RELATED_TO (conf >= 0.85) where the semantic
     description clearly indicates a more specific type:
       - "دو شاخه/دو سطح/دو مفهوم مرتبط در X" + both same family -> IS_A or COMPARED_WITH
       - "مکمل/در کنار" -> COMPARED_WITH (they coexist, not one-type-of-other)
       - "فرم گسترده‌تر/حالت خاص" -> EXTENDS
       - "تسهیل می‌کند/مکمل" -> USES (functional dependency)
     We do this conservatively: only when the description has an unambiguous
     signal. Otherwise keep RELATED_TO (it is a valid architectural fallback).

Idempotent and safe to re-run.
"""
import pymysql, sys
sys.stdout.reconfigure(encoding="utf-8")

conn = pymysql.connect(host="127.0.0.1", user="root", password="433700",
                       database="resaname_v2", charset="utf8mb4",
                       autocommit=False)
cur = conn.cursor()

def run(sql, args=None):
    cur.execute(sql, args or ())
    return cur.rowcount

# ======================================================================
# A) Verify knowledge_relations by confidence tier
# ======================================================================
print("=" * 70)
print("A) Verify knowledge_relations by confidence tier")
print("=" * 70)

n_high = run("""
UPDATE knowledge_relations
SET verification_status='verified'
WHERE confidence >= 0.80 AND verification_status != 'verified'
""")
print(f"  verified (conf >= 0.80): {n_high}")

n_low = run("""
UPDATE knowledge_relations
SET verification_status='needs_review'
WHERE confidence < 0.80 AND confidence >= 0.70 AND verification_status != 'needs_review'
""")
print(f"  needs_review (conf 0.70-0.79): {n_low}")

n_ver = run("""
UPDATE knowledge_relations
SET verification_status='verified'
WHERE confidence >= 0.80
""")
cur.execute("SELECT verification_status, COUNT(*) FROM knowledge_relations GROUP BY verification_status")
print("  distribution now:")
for s, c in cur.fetchall():
    print(f"    {s}: {c}")

# ======================================================================
# B) Refine high-confidence RELATED_TO with unambiguous semantic signals
# ======================================================================
print("\n" + "=" * 70)
print("B) Refine high-confidence RELATED_TO (conf >= 0.85)")
print("=" * 70)

# Fetch all RELATED_TO with conf >= 0.85 and their entity types + descriptions
cur.execute("""
SELECT kr.id, kr.source_entity_id, kr.target_entity_id, kr.confidence, kr.description,
       se.entity_type src_type, te.entity_type tgt_type,
       se.title_fa src_title, te.title_fa tgt_title
FROM knowledge_relations kr
JOIN knowledge_entities se ON se.id = kr.source_entity_id
JOIN knowledge_entities te ON te.id = kr.target_entity_id
WHERE kr.relation_type='RELATED_TO' AND kr.confidence >= 0.85
""")
rows = cur.fetchall()
print(f"  RELATED_TO with conf >= 0.85: {len(rows)}")

# Semantic rules (conservative — only unambiguous signals)
# Returns new_type or None (keep RELATED_TO)
def refine_type(src_type, tgt_type, desc):
    d = desc or ""
    # EXTENDS: "فرم گسترده‌تر", "حالت خاص", "نسخه‌ی گسترده"
    if any(k in d for k in ["فرم گسترده‌تر", "حالت خاص", "نسخه‌ی گسترده", "گسترش "]):
        return "EXTENDS"
    # COMPARED_WITH: "دو شاخه", "دو سطح", "دو مفهوم", "مکمل", "در کنار", "دو رویکرد"
    #   — these indicate coexistence/comparison, not subtype
    if any(k in d for k in ["دو شاخه", "دو سطح", "دو مفهوم", "مکمل", "در کنار",
                            "دو رویکرد", "دو نوع", "جفت‌وجور", "متضاد", "تفاوت",
                            "مقایسه", "دو بازو", "دو جنبه", "دو رویه", "دو مدل",
                            "دو رویکرد اصلی", "هر دو به"]):
        return "COMPARED_WITH"
    # USES: "تسهیل می‌کند", "برای ... استفاده", "مکمل ... استفاده می‌شوند" (functional)
    if "تسهیل" in d and "استفاده" not in d:
        return "USES"
    # IS_A: "نوعی", "فرم از", "مورد از", "نمونه‌ی" (subtype signal)
    if any(k in d for k in ["نوعی از", "فرم از", "حالت از", "نمونه‌ی", "پدیده‌ای از"]):
        return "IS_A"
    # APPLIES_TO: "کاربرد در", "به کار می‌رود در", "به‌کار می‌رود"
    if any(k in d for k in ["کاربرد در", "به کار می‌رود", "به‌کار می‌رود",
                            "به‌کار گرفته می‌شود در", "کاربرد آن در"]):
        return "APPLIES_TO"
    # INFLUENCED_BY: "تأثیر", "مستقل از", "بر پایه"
    if "مستقل" in d and "تأثیر" in d:
        return "INFLUENCED_BY"
    return None  # keep RELATED_TO

refined = 0
changed = []
for rid, src, tgt, conf, desc, st, tt, s_title, t_title in rows:
    new_type = refine_type(st, tt, desc)
    if new_type:
        run("UPDATE knowledge_relations SET relation_type=%s WHERE id=%s", (new_type, rid))
        refined += 1
        changed.append((src, new_type, tgt, conf, new_type))

print(f"  refined: {refined}")
for src, new_type, tgt, conf, _ in changed:
    print(f"    {src} -{new_type}-> {tgt} (conf={conf})")

# Re-check distribution
cur.execute("""
SELECT relation_type, COUNT(*) c
FROM knowledge_relations GROUP BY relation_type ORDER BY c DESC
""")
print("\n  type distribution after refinement:")
for rt, c in cur.fetchall():
    marker = "  <-- was RELATED_TO" if rt in ("IS_A","PART_OF","USES","APPLIES_TO",
                                               "EXTENDS","COMPARED_WITH","INFLUENCED_BY") else ""
    print(f"    {rt}: {c}{marker}")

cur.execute("SELECT COUNT(*) FROM knowledge_relations WHERE relation_type='RELATED_TO'")
print(f"\n  RELATED_TO remaining: {cur.fetchone()[0]}")

# ======================================================================
# commit + final audit
# ======================================================================
conn.commit()

print("\n" + "=" * 70)
print("FINAL AUDIT")
print("=" * 70)
cur.execute("SELECT verification_status, COUNT(*) FROM knowledge_relations GROUP BY verification_status")
print("knowledge_relations by status:")
for s, c in cur.fetchall():
    print(f"  {s}: {c}")

cur.execute("SELECT relation_type, COUNT(*) FROM knowledge_relations WHERE relation_type='RELATED_TO'")
print(f"RELATED_TO: {cur.fetchone()[0]}")

# Orphan check
cur.execute("""
SELECT COUNT(*) FROM knowledge_relations kr
LEFT JOIN knowledge_entities e1 ON e1.id = kr.source_entity_id
LEFT JOIN knowledge_entities e2 ON e2.id = kr.target_entity_id
WHERE e1.id IS NULL OR e2.id IS NULL
""")
print(f"orphan relations: {cur.fetchone()[0]}")

conn.close()
print("\nDONE — W8 knowledge_relations verified.")
