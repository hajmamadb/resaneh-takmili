#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
apply_classification.py — Merge 31 batch classification files, validate,
and persist to resaname_v2.contents.content_type.

Reads:
  - llm/classify_llm_01.json ... classify_llm_31.json  (per-batch LLM output)
  - content_type_taxonomy (from resaname_v2) for validation

Writes:
  - llm/classify_merged.json  (merged 731-entry classification)
  - UPDATEs resaname_v2.contents.content_type for the 731 card rows
  - Reports before/after distribution
"""
import json
import os
import pymysql

BASE = os.path.dirname(os.path.abspath(__file__))
LLM_DIR = os.path.join(BASE, "llm")

# ---------------------------------------------------------------------------
# 1) Load all 31 batch files and merge
# ---------------------------------------------------------------------------
merged = {}
errors = []
for i in range(1, 32):
    fpath = os.path.join(LLM_DIR, f"classify_llm_{i:02d}.json")
    if not os.path.exists(fpath):
        errors.append(f"Missing: {fpath}")
        continue
    with open(fpath, "r", encoding="utf-8") as f:
        data = json.load(f)
    for source_id, cls in data.items():
        if source_id in merged:
            errors.append(f"Duplicate source_id: {source_id} in batch {i:02d}")
        merged[source_id] = cls

print(f"Merged {len(merged)} cards from 31 batch files")

# ---------------------------------------------------------------------------
# 2) Validate
# ---------------------------------------------------------------------------
# Load valid type_keys from taxonomy
conn = pymysql.connect(host="127.0.0.1", user="root", password="433700",
                       database="resaname_v2", charset="utf8mb4",
                       cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()
cur.execute("SELECT type_key, category_no FROM content_type_taxonomy")
taxonomy = {row["type_key"]: row["category_no"] for row in cur.fetchall()}
print(f"Taxonomy: {len(taxonomy)} valid type_keys")

# Validate each entry
invalid_types = []
missing_confidence = []
bad_category = []
for source_id, cls in merged.items():
    tk = cls.get("type_key", "")
    if tk not in taxonomy:
        invalid_types.append((source_id, tk))
    if "confidence" not in cls:
        missing_confidence.append(source_id)
    elif not (0.0 <= cls["confidence"] <= 1.0):
        invalid_types.append((source_id, f"confidence={cls['confidence']}"))
    cn = cls.get("category_no")
    if cn is not None and cn != taxonomy.get(tk, -1):
        bad_category.append((source_id, tk, cn, taxonomy.get(tk, -1)))

print(f"\nValidation results:")
print(f"  Total entries:       {len(merged)}")
print(f"  Expected:            731")
print(f"  Invalid type_keys:   {len(invalid_types)}")
print(f"  Missing confidence:  {len(missing_confidence)}")
print(f"  Bad category_no:     {len(bad_category)}")

if invalid_types:
    print(f"\n  Invalid types (first 10):")
    for sid, tk in invalid_types[:10]:
        print(f"    {sid}: '{tk}'")
if missing_confidence:
    print(f"\n  Missing confidence (first 10): {missing_confidence[:10]}")
if bad_category:
    print(f"\n  Bad category (first 10):")
    for sid, tk, cn, expected in bad_category[:10]:
        print(f"    {sid}: {tk} got cat {cn}, expected {expected}")

# ---------------------------------------------------------------------------
# 3) Write merged file
# ---------------------------------------------------------------------------
merged_path = os.path.join(LLM_DIR, "classify_merged.json")
with open(merged_path, "w", encoding="utf-8") as f:
    json.dump(merged, f, ensure_ascii=False, indent=2)
print(f"\nWrote merged file: {merged_path}")

# ---------------------------------------------------------------------------
# 4) Get current distribution (before)
# ---------------------------------------------------------------------------
cur.execute("""SELECT content_type, COUNT(*) as cnt
               FROM contents WHERE source_type='card'
               GROUP BY content_type ORDER BY cnt DESC""")
before = {row["content_type"]: row["cnt"] for row in cur.fetchall()}
print(f"\n=== BEFORE (current content_type distribution) ===")
for ct, cnt in sorted(before.items(), key=lambda x: -x[1]):
    print(f"  {ct:25s} {cnt:5d}")

# ---------------------------------------------------------------------------
# 5) Apply classification to DB
# ---------------------------------------------------------------------------
updated = 0
skipped = 0
for source_id, cls in merged.items():
    tk = cls.get("type_key", "")
    if tk not in taxonomy:
        skipped += 1
        continue
    cur.execute(
        "UPDATE contents SET content_type=%s WHERE source_type='card' AND source_id=%s",
        (tk, source_id)
    )
    updated += cur.rowcount

conn.commit()
print(f"\nApplied: {updated} rows updated, {skipped} skipped (invalid type)")

# ---------------------------------------------------------------------------
# 6) Get new distribution (after)
# ---------------------------------------------------------------------------
cur.execute("""SELECT content_type, COUNT(*) as cnt
               FROM contents WHERE source_type='card'
               GROUP BY content_type ORDER BY cnt DESC""")
after = {row["content_type"]: row["cnt"] for row in cur.fetchall()}
print(f"\n=== AFTER (new content_type distribution) ===")
for ct, cnt in sorted(after.items(), key=lambda x: -x[1]):
    print(f"  {ct:25s} {cnt:5d}")

# ---------------------------------------------------------------------------
# 7) Category-level summary
# ---------------------------------------------------------------------------
cur.execute("""SELECT t.category_no, t.category_fa, t.type_key, t.type_fa,
                      COUNT(c.id) as cnt
               FROM content_type_taxonomy t
               LEFT JOIN contents c
                 ON c.content_type = t.type_key AND c.source_type = 'card'
               GROUP BY t.type_key
               ORDER BY t.category_no, t.sort_order""")
rows = cur.fetchall()
print(f"\n=== Distribution by category ===")
cur_cat = None
for row in rows:
    if row["category_no"] != cur_cat:
        cur_cat = row["category_no"]
        print(f"\n  Category {cur_cat}: {row['category_fa']}")
    print(f"    {row['type_key']:25s} {row['type_fa']:20s} {row['cnt']:5d}")

# ---------------------------------------------------------------------------
# 8) Check for NULLs
# ---------------------------------------------------------------------------
cur.execute("SELECT COUNT(*) as cnt FROM contents WHERE source_type='card' AND content_type IS NULL OR content_type=''")
nulls = cur.fetchone()["cnt"]
print(f"\nNULL/empty content_type on cards: {nulls}")

# ---------------------------------------------------------------------------
# 9) Confirm non-cards untouched
# ---------------------------------------------------------------------------
cur.execute("""SELECT source_type, content_type, COUNT(*) as cnt
               FROM contents WHERE source_type != 'card'
               GROUP BY source_type, content_type ORDER BY source_type, cnt DESC""")
non_cards = cur.fetchall()
print(f"\n=== Non-card content_types (should be unchanged) ===")
for row in non_cards:
    print(f"  {row['source_type']:12s} {row['content_type']:20s} {row['cnt']:5d}")

conn.close()
print("\nDone.")
