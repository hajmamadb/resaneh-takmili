#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
classify_cards.py — Prepare batch input files for LLM classification of 731 cards.

Reads:
  - llm/cards_all.json  (731 cards with title_fa, title_en, card_type, approach, core_logic, ...)
  - resaname_v2.contents (current_content_type for each card)

Writes (to sql/llm/):
  - classify_batch_manifest.json  (31 batches × ~24 cards)
  - classify_batch_01.json ... classify_batch_31.json  (per-batch input)

Each batch item:
  id            doc-card-N (contents.id)
  source_id     card-N
  title_fa      Persian title
  title_en      English title
  current_ct    current content_type (from resaname_v2.contents)
  card_type_fa  original Persian card_type (from site)
  category_id   cat-N
  summary       first 300 chars of summary (from contents)
  approach      first 300 chars of approach
  core_logic    first 300 chars of core_logic
"""
import json
import os
import pymysql

BASE = os.path.dirname(os.path.abspath(__file__))
LLM_DIR = os.path.join(BASE, "llm")

BATCH_SIZE = 24

# ---------------------------------------------------------------------------
# 1) Load 731 cards from cards_all.json
# ---------------------------------------------------------------------------
with open(os.path.join(LLM_DIR, "cards_all.json"), "r", encoding="utf-8") as f:
    cards_all = json.load(f)
print(f"Loaded {len(cards_all)} cards from cards_all.json")

cards_by_source_id = {c["source_id"] if "source_id" in c else c["id"]: c for c in cards_all}

# ---------------------------------------------------------------------------
# 2) Load current content_type from resaname_v2.contents
# ---------------------------------------------------------------------------
conn = pymysql.connect(host="127.0.0.1", user="root", password="433700",
                       database="resaname_v2", charset="utf8mb4",
                       cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()
cur.execute("""SELECT id, source_id, title, english_title, summary, content_type
               FROM contents WHERE source_type='card' ORDER BY source_id""")
v2_cards = cur.fetchall()
conn.close()
print(f"Loaded {len(v2_cards)} cards from resaname_v2.contents")

v2_by_source_id = {c["source_id"]: c for c in v2_cards}

# ---------------------------------------------------------------------------
# 3) Build batch items (sorted by card number)
# ---------------------------------------------------------------------------
def card_num(source_id):
    """card-123 -> 123"""
    return int(source_id.replace("card-", ""))

all_source_ids = sorted(v2_by_source_id.keys(), key=card_num)
print(f"Total cards to classify: {len(all_source_ids)}")

items = []
for sid in all_source_ids:
    v2 = v2_by_source_id[sid]
    ca = cards_by_source_id.get(sid, {})
    items.append({
        "id": v2["id"],
        "source_id": sid,
        "title_fa": v2["title"],
        "title_en": v2["english_title"] or ca.get("title_en", ""),
        "current_ct": v2["content_type"],
        "card_type_fa": ca.get("card_type", ""),
        "category_id": ca.get("category_id", ""),
        "macro_domain": ca.get("macro_domain", ""),
        "paradigm": ca.get("paradigm", ""),
        "summary": (v2["summary"] or "")[:300],
        "approach": (ca.get("approach", "") or "")[:300],
        "core_logic": (ca.get("core_logic", "") or "")[:300],
    })

# ---------------------------------------------------------------------------
# 4) Split into batches
# ---------------------------------------------------------------------------
n_batches = (len(items) + BATCH_SIZE - 1) // BATCH_SIZE
print(f"Splitting into {n_batches} batches of {BATCH_SIZE}")

manifest = []
for b in range(n_batches):
    batch_items = items[b * BATCH_SIZE : (b + 1) * BATCH_SIZE]
    batch_no = b + 1
    out_file = f"classify_llm_{batch_no:02d}.json"
    in_file = f"classify_batch_{batch_no:02d}.json"

    # Write batch input
    with open(os.path.join(LLM_DIR, in_file), "w", encoding="utf-8") as f:
        json.dump(batch_items, f, ensure_ascii=False, indent=2)

    manifest.append({
        "file": in_file,
        "out": out_file,
        "ids": [it["source_id"] for it in batch_items],
    })

# Write manifest
with open(os.path.join(LLM_DIR, "classify_batch_manifest.json"), "w", encoding="utf-8") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

print(f"Wrote {n_batches} batch files + manifest to {LLM_DIR}")
print("Done.")
