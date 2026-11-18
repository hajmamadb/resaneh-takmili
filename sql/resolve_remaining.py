# -*- coding: utf-8 -*-
"""Generate remaining UPDATEs, skipping those that would create duplicate (source, relation, target) combos."""
import re
import subprocess

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
            card_titles[lits[0]] = (lits[4], lits[5])

# Build concept -> doc_id mapping
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

concept_to_doc = {}
for concept in unresolved_set:
    concept_norm = normalize(concept)
    for doc_id, (persian, english) in card_titles.items():
        persian_norm = normalize(persian)
        english_norm = normalize(english)
        if concept_norm == persian_norm or concept_norm == english_norm:
            concept_to_doc[concept] = doc_id
            break
        if concept_norm in persian_norm or persian_norm in concept_norm:
            concept_to_doc[concept] = doc_id
            break
        if concept_norm in english_norm or english_norm in concept_norm:
            concept_to_doc[concept] = doc_id
            break

print('concepts mapped:', len(concept_to_doc))

# Get existing (source_id, relation_type, target_id) combos from DB to avoid duplicates
existing = set()
result = subprocess.run(
    ['C:/Program Files/MySQL/MySQL Server 8.0/bin/mysql.exe', '-u', 'root', '-p433700', 'resaname_h',
     '-N', '-B', '-e',
     'SELECT source_id, relationship_type, target_id FROM ai_relationships;'],
    capture_output=True, text=True, encoding='utf-8'
)
for line in result.stdout.splitlines():
    parts = line.split('\t')
    if len(parts) >= 3:
        existing.add((parts[0], parts[1], parts[2]))

print('existing combos in DB:', len(existing))

# Generate updates, skipping duplicates (both DB and within-batch)
updates = []
skipped = 0
batch_combos = set()  # (source_id, relationship_type, new_target) already assigned in this batch
for l in lines3:
    if not l.startswith('(') or "'rel-" not in l:
        continue
    lits = pat.findall(l)
    if len(lits) < 6:
        continue
    rel_id = lits[0]
    source_id = lits[2]
    relationship_type = lits[3]
    target_id = lits[5]
    if '__unresolved' not in target_id:
        continue
    concept = target_id.replace('__unresolved', '').strip().rstrip('.').strip()
    if concept not in concept_to_doc:
        continue
    new_target = concept_to_doc[concept]
    combo = (source_id, relationship_type, new_target)
    # Check if this combo already exists in DB or in this batch
    if combo in existing or combo in batch_combos:
        skipped += 1
        continue
    batch_combos.add(combo)
    updates.append((rel_id, source_id, target_id, new_target))

print('remaining updates:', len(updates))
print('skipped (duplicate):', skipped)

# Generate SQL
sql_lines = [
    '-- Phase 5: Resolve remaining __unresolved related_to relations (deduped)',
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
])

open('resolve-remaining.sql', 'w', encoding='utf-8', newline='').write('\n'.join(sql_lines))
print('wrote resolve-remaining.sql')

if updates:
    print('Sample (first 5):')
    for rel_id, source_id, old, new in updates[:5]:
        print(f'  {rel_id}: {old[:40]}... -> {new}')
