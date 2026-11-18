# -*- coding: utf-8 -*-
"""resaname_v2 Phase 5: resolve the 2358 __unresolved relation_links.
Match the 130 distinct Persian-English target labels to real `contents` rows
(title / english_title), then UPDATE target_id + verification_status +
extracted_by. PK is (source_id, relationship_type, target_id) so we dedupe per
combo (first row wins; later dupes of the same combo are left __unresolved).

Phase 1 = DRY RUN: prints match coverage + samples, writes nothing.
Phase 2 = APPLY  : write + execute the UPDATEs, then verify.
Usage: python resolve_v2_unresolved.py            # dry run
       python resolve_v2_unresolved.py --apply    # apply
"""
import re, sys
import pymysql

APPLY = '--apply' in sys.argv

def normalize(s):
    s = s.lower().strip().rstrip('.').strip()
    s = s.replace('\u200c', ' ')   # ZWNJ
    s = re.sub(r'\s+', ' ', s)
    return s

conn = pymysql.connect(host='127.0.0.1', user='root', password='433700',
                       database='resaname_v2', charset='utf8mb4')
cur = conn.cursor()

# --- 1. load all contents (title + english_title) -> lookup keys ---
cur.execute("SELECT id, IFNULL(title,''), IFNULL(english_title,'') FROM contents")
title_to_id = {}
for cid, fa, en in cur.fetchall():
    for key in (fa, en):
        n = normalize(key)
        if n:
            title_to_id.setdefault(n, cid)

def match(concept):
    """Return (content_id, method) or (None, None)."""
    cn = normalize(concept)
    if not cn:
        return None, None
    if cn in title_to_id:
        return title_to_id[cn], 'exact'
    # concept may carry ' (English)' in parens; the Persian part alone may match
    m = re.match(r'^(.*?)\s*\(([^)]*)\)\s*$', concept)
    fa_part = m.group(1).strip() if m else None
    en_part = m.group(2).strip() if m else None
    if fa_part:
        fn = normalize(fa_part)
        if fn in title_to_id:
            return title_to_id[fn], 'fa-parens'
    if en_part:
        en = normalize(en_part)
        if en in title_to_id:
            return title_to_id[en], 'en-parens'
    # substring fallback (careful: longest match wins)
    best = (None, 0)
    for n, cid in title_to_id.items():
        if n and (cn in n or n in cn) and len(n) >= 4 and len(n) > best[1]:
            best = (cid, len(n))
    if best[0]:
        return best[0], 'substring'
    return None, None

# --- 2. gather the 130 distinct unresolved target labels ---
cur.execute("SELECT DISTINCT target_id FROM relation_links WHERE target_id LIKE '%__unresolved'")
labels = [r[0] for r in cur.fetchall()]
label_map = {}   # label -> content_id
method_map = {}  # label -> method
for t in labels:
    concept = t.replace('__unresolved', '').strip().rstrip('.').strip()
    cid, method = match(concept)
    label_map[t] = cid
    method_map[t] = method

matched = sum(1 for v in label_map.values() if v)
print(f"distinct unresolved labels: {len(labels)}")
print(f"  matched to a content: {matched}")
print(f"  unmatched:            {len(labels) - matched}")
print()
print("--- match methods ---")
from collections import Counter
print(Counter(method_map.values()))
print()
print("--- UNMATCHED labels (for manual review) ---")
for t in labels:
    if not label_map[t]:
        print(f"  {t.replace('__unresolved','')}")
print()
print("--- sample matches (first 15) ---")
shown = 0
for t in labels:
    if label_map[t] and shown < 15:
        print(f"  {t.replace('__unresolved','')[:45]:45s} -> {label_map[t]}  [{method_map[t]}]")
        shown += 1

if not APPLY:
    conn.close()
    print("\nDRY RUN — no changes written. Re-run with --apply to execute.")
    sys.exit(0)

# --- 3. build per-row updates, dedupe per combo ---
cur.execute(
    "SELECT source_id, relationship_type, target_id FROM relation_links "
    "WHERE target_id LIKE '%__unresolved' ORDER BY source_id, relationship_type, target_id")
rows = cur.fetchall()
existing_combos = set()
cur.execute("SELECT source_id, relationship_type, target_id FROM relation_links "
            "WHERE target_id NOT LIKE '%__unresolved'")
for s, rt, tid in cur.fetchall():
    existing_combos.add((s, rt, tid))

updates = []
skipped = 0
for source_id, rt, target_id in rows:
    cid = label_map.get(target_id)
    if not cid:
        continue
    combo = (source_id, rt, cid)
    if combo in existing_combos:
        skipped += 1
        continue
    existing_combos.add(combo)
    updates.append((source_id, rt, target_id, cid))

print(f"\nrows to UPDATE: {len(updates)}   (skipped dup-combo: {skipped})")

def esc(s):
    return s.replace('\\', '\\\\').replace("'", "''")
sql_lines = [
    "-- resaname_v2 Phase 5: resolve __unresolved related_to relations (deduped)",
    "-- Generated: 2026-11-10",
    "USE resaname_v2;",
    "SET FOREIGN_KEY_CHECKS = 0;",
    "",
]
for source_id, rt, old_target, new_target in updates:
    sql_lines.append(
        "UPDATE relation_links SET target_id = '%s', verification_status = 'verified', "
        "extracted_by = 'phase5-v2-auto-match' WHERE source_id = '%s' AND relationship_type = '%s' "
        "AND target_id = '%s';" % (
            esc(new_target), esc(source_id), esc(rt), esc(old_target)))
sql_lines += ["", "SET FOREIGN_KEY_CHECKS = 1;",
              "-- Verify:",
              "-- SELECT COUNT(*) FROM relation_links WHERE target_id LIKE '%__unresolved';"]
open('resolve_v2_unresolved.sql', 'w', encoding='utf-8', newline='').write('\n'.join(sql_lines))

# execute via pymysql
cur.executemany(
    "UPDATE relation_links SET target_id = %s, verification_status = 'verified', "
    "extracted_by = 'phase5-v2-auto-match' WHERE source_id = %s AND relationship_type = %s "
    "AND target_id = %s",
    [(nt, s, rt, ot) for s, rt, ot, nt in updates])
conn.commit()

cur.execute("SELECT COUNT(*) FROM relation_links WHERE target_id LIKE '%__unresolved'")
left = cur.fetchone()[0]
cur.execute("SELECT COUNT(*) FROM relation_links")
total = cur.fetchone()[0]
print(f"\nAPPLIED {len(updates)} updates")
print(f"remaining __unresolved: {left}   (total relation_links: {total})")
conn.close()
