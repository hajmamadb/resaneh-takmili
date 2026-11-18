# -*- coding: utf-8 -*-
"""Check what literals are extracted from relation lines."""
import re

src3 = open('seed-731-cards-full.sql', encoding='utf-8').read()
lines3 = src3.splitlines()
pat = re.compile(r"'((?:[^'\\]|\\.)*)'")

# Find first relation line with __unresolved
for l in lines3:
    if not l.startswith('(') or "'rel-" not in l:
        continue
    if '__unresolved' not in l:
        continue
    print('Line:', l[:100])
    lits = pat.findall(l)
    print('Num literals:', len(lits))
    for i, lit in enumerate(lits):
        print(f'  [{i}] {lit[:50]!r}')
    break
