# -*- coding: utf-8 -*-
"""Count and measure all __unresolved target_id values in Phase-3 seed."""
import re

src = open('seed-731-cards-full.sql', encoding='utf-8').read()
lines = src.splitlines()
pat = re.compile(r"'((?:[^'\\]|\\.)*)'")
total = 0
over40 = 0
maxlen = 0
maxval = ''
for l in lines:
    if not l.startswith('(') or "'rel-" not in l:
        continue
    total += 1
    lits = pat.findall(l)
    if len(lits) < 10:
        continue
    tgt = lits[5]
    if tgt.endswith('__unresolved'):
        total_u = 1
        if len(tgt) > 40:
            over40 += 1
        if len(tgt) > maxlen:
            maxlen = len(tgt)
            maxval = tgt
print('total rel tuples:', total)
print('max target_id len:', maxlen)
print('max value:', maxval)
print('target_id with __unresolved >40 chars:', over40)
