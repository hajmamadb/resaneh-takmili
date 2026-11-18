# -*- coding: utf-8 -*-
"""Match 193 unresolved names against Phase-4 theory documents."""
import re
import json

# Load unresolved names from Phase-3
src3 = open('seed-731-cards-full.sql', encoding='utf-8').read()
lines3 = src3.splitlines()
pat = re.compile(r"'((?:[^'\\]|\\.)*)'")
unresolved = set()
for l in lines3:
    if not l.startswith('(') or "'rel-" not in l:
        continue
    lits = pat.findall(l)
    if len(lits) >= 6:
        tgt = lits[5]
        if '__unresolved' in tgt:
            base = tgt.replace('__unresolved', '').strip()
            # Remove trailing period if present
            base = base.rstrip('.').strip()
            unresolved.add(base)

# Load Phase-4 theory titles
src4 = open('seed-phase4-70-items.sql', encoding='utf-8').read()
lines4 = src4.splitlines()
theory_docs = {}  # id -> title
for l in lines4:
    if l.startswith("('doc-new-theory-"):
        lits = pat.findall(l)
        if len(lits) >= 4:
            doc_id = lits[0]
            title = lits[3]  # 4th column is title
            theory_docs[doc_id] = title

print('unresolved names:', len(unresolved))
print('phase-4 theory docs:', len(theory_docs))
print()

# Try to match
matched = {}
unmatched = []
for name in unresolved:
    # Normalize: remove trailing period, standardize whitespace
    name_norm = name.rstrip('.').strip()
    # Try exact match first
    found = False
    for doc_id, title in theory_docs.items():
        if title == name_norm:
            matched[name] = doc_id
            found = True
            break
    if not found:
        # Try fuzzy: check if name is in title or vice versa
        for doc_id, title in theory_docs.items():
            if name_norm in title or title in name_norm:
                matched[name] = doc_id
                found = True
                break
    if not found:
        unmatched.append(name)

print('matched:', len(matched))
print('unmatched:', len(unmatched))
print()
print('--- MATCHED (first 20) ---')
for name, doc_id in list(matched.items())[:20]:
    print(f'  {name} -> {doc_id}')
print()
print('--- UNMATCHED (first 30) ---')
for name in unmatched[:30]:
    print(' ', name)
