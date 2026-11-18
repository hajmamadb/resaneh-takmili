# -*- coding: utf-8 -*-
import re

src = open('seed-731-cards-full.sql', encoding='utf-8').read()
lines = src.splitlines()
start = next(i for i, l in enumerate(lines) if l.startswith('INSERT INTO `ai_relationships`'))
block = []
for i in range(start + 1, len(lines)):
    l = lines[i]
    if l.startswith('('):
        block.append(l)
        if l.rstrip().endswith(');'):
            break
    elif l.strip().endswith(');'):
        block.append(l)
        break
print('block lines:', len(block))

pat = re.compile(r"'((?:[^'\\]|\\.)*)'")
longs = []
for ln in block:
    for m in pat.finditer(ln):
        v = m.group(1)
        if len(v) > 40:
            longs.append((ln[:40], v, len(v)))
print('long quoted values (>40):', len(longs))
for x in longs[:30]:
    print(x)
