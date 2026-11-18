# -*- coding: utf-8 -*-
"""Generate SQL to resolve 64 matched __unresolved relations to actual card IDs."""
import re

src3 = open('seed-731-cards-full.sql', encoding='utf-8').read()
lines3 = src3.splitlines()
pat = re.compile(r"'((?:[^'\\]|\\.)*)'")

def normalize(s):
    s = s.lower().strip().rstrip('.').strip()
    s = s.replace('‌', ' ')
    s = re.sub(r'\s+', ' ', s)
    return s

# Load card titles
card_titles = {}
for l in lines3:
    if l.startswith("('doc-card-"):
        lits = pat.findall(l)
        if len(lits) >= 6:
            doc_id = lits[0]
            persian = lits[4]
            english = lits[5]
            card_titles[doc_id] = (persian, english)

# Build lookup: normalized_title -> doc_id
title_to_doc = {}
for doc_id, (persian, english) in card_titles.items():
    title_to_doc[normalize(persian)] = doc_id
    title_to_doc[normalize(english)] = doc_id

# Build concept -> doc_id mapping (same logic as match_cards2.py)
concept_to_doc = {}
unresolved_set = set()
for l in lines3:
    if not l.startswith('(') or "'rel-" not in l:
        continue
    lits = pat.findall(l)
    if len(lits) >= 6:
        tgt = lits[5]
        if '__unresolved' in tgt:
            base = tgt.replace('__unresolved', '').strip().rstrip('.').strip()
            unresolved_set.add(base)

print('DEBUG: unresolved_set size:', len(unresolved_set))
print('DEBUG: card_titles size:', len(card_titles))
print('DEBUG: first concept:', repr(next(iter(unresolved_set))))
print('DEBUG: first card:', list(card_titles.items())[0])

for concept in unresolved_set:
    concept_norm = normalize(concept)
    found = False
    for doc_id, (persian, english) in card_titles.items():
        persian_norm = normalize(persian)
        english_norm = normalize(english)
        if concept_norm == persian_norm or concept_norm == english_norm:
            concept_to_doc[concept] = doc_id
            found = True
            break
        if concept_norm in persian_norm or persian_norm in concept_norm:
            concept_to_doc[concept] = doc_id
            found = True
            break
        if concept_norm in english_norm or english_norm in concept_norm:
            concept_to_doc[concept] = doc_id
            found = True
            break

print('DEBUG: concept_to_doc size:', len(concept_to_doc))
print('DEBUG: first 5 matched:', list(concept_to_doc.items())[:5])

# Now find all relations that need updating
updates = []
debug_count = 0
for i, l in enumerate(lines3):
    if not l.startswith('(') or "'rel-" not in l:
        continue
    lits = pat.findall(l)
    if len(lits) < 6:
        continue
    rel_id = lits[0]
    source_id = lits[2]
    target_id = lits[5]
    if '__unresolved' not in target_id:
        continue
    concept = target_id.replace('__unresolved', '').strip().rstrip('.').strip()
    if debug_count < 5:
        print(f'  DEBUG loop: concept={concept!r} in concept_to_doc={concept in concept_to_doc}')
        debug_count += 1
    if concept in concept_to_doc:
        updates.append((rel_id, source_id, target_id, concept_to_doc[concept]))

print('total updates:', len(updates))
print()

# Generate SQL
sql_lines = [
    '-- Phase 5: Resolve 64 matched __unresolved related_to relations',
    '-- Generated: 2026-11-09',
    'USE resaname_h;',
    'SET FOREIGN_KEY_CHECKS = 0;',
    '',
]
for rel_id, source_id, old_target, new_target in updates:
    sql_lines.append(f"UPDATE ai_relationships SET target_id = '{new_target}', verification_status = 'verified', extracted_by = 'phase5-auto-match' WHERE id = '{rel_id}';")

sql_lines.extend([
    '',
    'SET FOREIGN_KEY_CHECKS = 1;',
    '',
    '-- Verify:',
    "-- SELECT COUNT(*) FROM ai_relationships WHERE target_id LIKE '%__unresolved';",
    '-- Expected: 4220 - 64 = 4156',
])

open('resolve-64-matched.sql', 'w', encoding='utf-8', newline='').write('\n'.join(sql_lines))
print('wrote resolve-64-matched.sql')
print()
print('Sample updates (first 10):')
for rel_id, source_id, old, new in updates[:10]:
    print(f'  {rel_id}: {old[:40]}... -> {new}')
