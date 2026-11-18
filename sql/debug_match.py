# -*- coding: utf-8 -*-
"""Debug: show card titles and unresolved concepts side by side."""
import re

src3 = open('seed-731-cards-full.sql', encoding='utf-8').read()
lines3 = src3.splitlines()
pat = re.compile(r"'((?:[^'\\]|\\.)*)'")

def normalize(s):
    s = s.lower().strip()
    s = s.rstrip('.').strip()
    s = s.replace('‌', ' ')
    s = re.sub(r'\s+', ' ', s)
    return s

card_titles = {}
for l in lines3:
    if l.startswith("('doc-card-"):
        lits = pat.findall(l)
        if len(lits) >= 6:
            card_titles[lits[0]] = (lits[4], lits[5])

print('card count:', len(card_titles))
print('First 5 cards:')
for i, (doc_id, (p, e)) in enumerate(list(card_titles.items())[:5]):
    print(f'  {doc_id}: FA={p[:50]!r} EN={e[:50]!r}')
print()

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

print('unresolved count:', len(unresolved))
print('First 15 unresolved:')
for u in sorted(unresolved)[:15]:
    print(f'  {u!r}')
print()

# Try matching with the same logic as match_cards2.py
matched = 0
for concept in unresolved:
    concept_norm = normalize(concept)
    for doc_id, (persian, english) in card_titles.items():
        persian_norm = normalize(persian)
        english_norm = normalize(english)
        if concept_norm == persian_norm or concept_norm == english_norm:
            matched += 1
            break
        if concept_norm in persian_norm or persian_norm in concept_norm:
            matched += 1
            break
        if concept_norm in english_norm or english_norm in concept_norm:
            matched += 1
            break

print('matched (this script):', matched)
print('unresolved set size:', len(unresolved))

# Check: are card_titles actually populated?
print()
print('card_titles keys sample:', list(card_titles.keys())[:5])
print('card_titles values sample:', list(card_titles.values())[:3])
