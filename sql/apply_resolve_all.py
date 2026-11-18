# -*- coding: utf-8 -*-
"""Apply all 130 label mappings (37 deterministic + 93 manual) to
relation_links in resaname_v2.

For each label -> content_id:
  UPDATE relation_links
     SET target_id = '<content_id>', verification_status='verified',
         extracted_by='phase5v2-label-resolve'
   WHERE target_id = '<label>__unresolved'
      AND NOT EXISTS (same source+type+new_target already exists)

Idempotent: re-running is safe (rows already updated won't match).
"""
import json, sys
import pymysql

BASE = r"D:/رسانامه تکمیلی/sql"
DET = json.load(open(f"{BASE}/resolve_deterministic.json", encoding="utf-8"))
MAN = json.load(open(f"{BASE}/resolve_manual_93.json", encoding="utf-8"))

# merge: deterministic first, manual overrides if same key
label_map = {}
label_map.update({k: v["content_id"] for k, v in DET.items()})
label_map.update(MAN)
print(f"total label mappings: {len(label_map)} (det={len(DET)}, manual={len(MAN)})")

APPLY = "--apply" in sys.argv
conn = pymysql.connect(host="127.0.0.1", user="root", password="433700",
                       database="resaname_v2", charset="utf8mb4")
cur = conn.cursor()

# 1. dry-run coverage check
cur.execute("SELECT DISTINCT target_id FROM relation_links WHERE target_id LIKE '%__unresolved'")
db_labels = [r[0].replace("__unresolved", "").strip() for r in cur.fetchall()]
print(f"distinct unresolved labels in DB: {len(db_labels)}")

covered = [l for l in db_labels if l in label_map]
uncovered = [l for l in db_labels if l not in label_map]
print(f"covered by our map: {len(covered)}")
print(f"NOT covered: {len(uncovered)}")
for u in uncovered:
    print(f"  UNCOVERED: {u}")

# 2. verify all target content_ids exist
ids = list(set(label_map.values()))
ph = ",".join(["%s"] * len(ids))
cur.execute(f"SELECT id FROM contents WHERE id IN ({ph})", ids)
valid_ids = {r[0] for r in cur.fetchall()}
missing = [i for i in ids if i not in valid_ids]
print(f"target ids: {len(ids)}, missing from contents: {len(missing)}")
for m in missing:
    print(f"  MISSING CONTENT: {m}  (referenced by labels: {[k for k,v in label_map.items() if v==m][:3]}...)")

if missing:
    print("\nERROR: some target content_ids don't exist. Aborting.")
    conn.close()
    sys.exit(1)

if not APPLY:
    print("\nDRY RUN — no changes. Re-run with --apply.")
    conn.close()
    sys.exit(0)

# 3. apply: per label, update rows that don't create a duplicate combo
total = 0
skipped_dup = 0
for label, cid in label_map.items():
    old_target = f"{label}__unresolved"
    # rows currently pointing to this label
    cur.execute(
        "SELECT source_id, relationship_type FROM relation_links WHERE target_id = %s",
        (old_target,))
    rows = cur.fetchall()
    if not rows:
        continue
    # existing combos (non-unresolved) to avoid dup
    cur.execute(
        "SELECT source_id, relationship_type FROM relation_links WHERE target_id = %s",
        (cid,))
    existing = {(s, rt) for s, rt in cur.fetchall()}
    new_combos = set()
    updated = 0
    for s, rt in rows:
        key = (s, rt)
        if key in existing or key in new_combos:
            skipped_dup += 1
            continue
        new_combos.add(key)
        cur.execute(
            "UPDATE relation_links SET target_id=%s, verification_status='verified', "
            "extracted_by='phase5v2-label-resolve' WHERE source_id=%s AND relationship_type=%s AND target_id=%s",
            (cid, s, rt, old_target))
        updated += cur.rowcount
    total += updated
    print(f"  {label[:45]:45s} -> {cid}  (updated {updated} rows)")

conn.commit()
cur.execute("SELECT COUNT(*) FROM relation_links WHERE target_id LIKE '%__unresolved'")
left = cur.fetchone()[0]
cur.execute("SELECT COUNT(*) FROM relation_links")
tot = cur.fetchone()[0]
print(f"\nDONE. updated={total} rows, skipped_dup={skipped_dup}")
print(f"remaining __unresolved: {left}  / total relation_links: {tot}")
conn.close()
