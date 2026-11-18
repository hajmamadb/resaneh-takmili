# -*- coding: utf-8 -*-
"""Match 192 unresolved concepts against card titles (Persian + English)."""
import re

src3 = open('seed-731-cards-full.sql', encoding='utf-8').read()
lines3 = src3.splitlines()
pat = re.compile(r"'((?:[^'\\]|\\.)*)'")

# Load card titles: doc_id -> (persian_title, english_title)
card_titles = {}
for l in lines3:
    if l.startswith("('doc-card-"):
        lits = pat.findall(l)
        if len(lits) >= 6:
            doc_id = lits[0]
            persian = lits[4]
            english = lits[5]
            card_titles[doc_id] = (persian, english)

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

print('cards:', len(card_titles))
print('unresolved concepts:', len(unresolved))
print()

def normalize(s):
    s = s.lower().strip()
    # Remove parenthetical English if Persian exists
    # Remove trailing period
    s = s.rstrip('.').strip()
    # Replace common variants
    s = s.replace('‌', ' ')  # ZWNJ to space
    s = re.sub(r'\s+', ' ', s)  # Collapse whitespace
    return s

matched = {}
unmatched = []
for concept in unresolved:
    concept_norm = normalize(concept)
    found = False
    for doc_id, (persian, english) in card_titles.items():
        persian_norm = normalize(persian)
        english_norm = normalize(english)
        # Exact match
        if concept_norm == persian_norm or concept_norm == english_norm:
            matched[concept] = (doc_id, persian, english)
            found = True
            break
        # Fuzzy: concept in title or title in concept
        if concept_norm in persian_norm or persian_norm in concept_norm:
            matched[concept] = (doc_id, persian, english)
            found = True
            break
        if concept_norm in english_norm or english_norm in concept_norm:
            matched[concept] = (doc_id, persian, english)
            found = True
            break
    if not found:
        unmatched.append(concept)

print('matched to cards:', len(matched))
print('unmatched:', len(unmatched))
print()
print('--- MATCHED (first 20) ---')
for concept, (doc_id, persian, english) in list(matched.items())[:20]:
    print(f'  {concept}')
    print(f'    -> {doc_id}')
    print(f'       FA: {persian[:50]}...')
    print(f'       EN: {english[:50]}')
print()
print('--- UNMATCHED (first 30) ---')
for concept in unmatched[:30]:
    print(' ', concept)
