# -*- coding: utf-8 -*-
import re
src = open('seed-731-cards-full.sql', encoding='utf-8').read()
lines = src.splitlines()
pat = re.compile(r"'((?:[^'\\]|\\.)*)'")
total = 0
over40 = 0
maxlen = 0
maxval = ''
unresolved_count = 0
for l in lines:
    if not l.startswith('(') or "'rel-" not in l:
        continue
    total += 1
    lits = pat.findall(l)
    if len(lits) < 6:
        continue
    tgt = lits[5]
    if '__unresolved' in tgt:
        unresolved_count += 1
        if len(tgt) > 40:
            over40 += 1
        if len(tgt) > maxlen:
            maxlen = len(tgt)
            maxval = tgt
print('total rel tuples:', total)
print('__unresolved count:', unresolved_count)
print('over40:', over40)
print('maxlen:', maxlen)
print('maxval:', maxval)
