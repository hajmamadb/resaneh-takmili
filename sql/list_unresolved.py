# -*- coding: utf-8 -*-
import re
src = open('seed-731-cards-full.sql', encoding='utf-8').read()
lines = src.splitlines()
pat = re.compile(r"'((?:[^'\\]|\\.)*)'")
unresolved = set()
for l in lines:
    if not l.startswith('(') or "'rel-" not in l:
        continue
    lits = pat.findall(l)
    if len(lits) >= 6:
        tgt = lits[5]
        if '__unresolved' in tgt:
            # Remove the __unresolved suffix
            base = tgt.replace('__unresolved', '').strip()
            unresolved.add(base)
print('distinct unresolved targets:', len(unresolved))
for u in sorted(unresolved)[:30]:
    print(' ', u)
