# -*- coding: utf-8 -*-
import re

src = open('seed-731-cards-full.sql', encoding='utf-8').read()
lines = src.splitlines()
start = None
for i, l in enumerate(lines):
    if l.startswith('INSERT INTO `ai_relationships`'):
        start = i
        break
assert start is not None
line = lines[start]
m = re.search(r'VALUES\s*(.*);?\s*$', line)
vals_str = m.group(1)
lits = re.findall(r"'((?:[^'\\]|\\.)*)'", vals_str)
# 10 quoted per tuple (11 cols, confidence unquoted)
n = len(lits) // 10
print('tuples:', n, '| lits:', len(lits))
for colname, idx in [('id',0),('source_id',2),('target_id',5)]:
    bad = []
    for k in range(n):
        v = lits[k*10+idx]
        if len(v) > 40:
            bad.append((k, v, len(v)))
    print('%-10s >40: %d' % (colname, len(bad)))
    for b in bad[:10]:
        print('   ', b)
