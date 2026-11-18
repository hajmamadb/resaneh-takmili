# -*- coding: utf-8 -*-
import re
src = open('seed-731-cards-full.sql', encoding='utf-8').read()
lines = src.splitlines()
pat = re.compile(r"'((?:[^'\\]|\\.)*)'")
# check line 111 (rel-00004)
for idx in [110, 111]:
    l = lines[idx]
    print('line', idx+1, 'starts_with_paren:', l.startswith('('))
    print('has rel-:', "'rel-" in l)
    lits = pat.findall(l)
    print('num lits:', len(lits))
    if len(lits) >= 6:
        print('lits[5] len:', len(lits[5]), 'val:', repr(lits[5][:60]))
