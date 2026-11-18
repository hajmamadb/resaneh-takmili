# -*- coding: utf-8 -*-
"""Check if 192 unresolved concepts match existing card titles."""
import re

src3 = open('seed-731-cards-full.sql', encoding='utf-8').read()
lines3 = src3.splitlines()
pat = re.compile(r"'((?:[^'\\]|\\.)*)'")

# Load card titles
card_titles = {}  # doc_id -> title
for l in lines3:
    if l.startswith("('doc-card-"):
        lits = pat.findall(l)
        if len(lits) >= 4:
            doc_id = lits[0]
            title = lits[3]
            card_titles[doc_id] = title

# Load unresolved names
unresolved = set()
for l in lines3:
    if not l.startswith('(') or "'rel-" not in l:
        continue
    lits = pat.findall(l)
    if len(lits) >= 6:
        tgt = lits[5]
        if '__unresolved' in tgt:
            base = tgt.replace('__unresolved', '').strip().rstrip('.').strip()
            unresolved.add(base)

print('card titles:', len(card_titles))
print('unresolved concepts:', len(unresolved))
print()

# Try to match
matched = {}
unmatched = []
for concept in unresolved:
    concept_norm = concept.strip()
    found = False
    for doc_id, title in card_titles.items():
        # Exact match
        if title == concept_norm:
            matched[concept] = doc_id
            found = True
            break
        # Fuzzy: concept in title or title in concept
        if concept_norm in title or title in concept_norm:
            matched[concept] = doc_id
            found = True
            break
    if not found:
        unmatched.append(concept)

print('matched to cards:', len(matched))
print('unmatched (no card):', len(unmatched))
print()
print('--- MATCHED (first 20) ---')
for concept, doc_id in list(matched.items())[:20]:
    title = card_titles[doc_id]
    print(f'  {concept} -> {doc_id} ({title[:40]}...)')
print()
print('--- UNMATCHED (first 30) ---')
for concept in unmatched[:30]:
    print(' ', concept)
