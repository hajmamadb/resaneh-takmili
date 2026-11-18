# -*- coding: utf-8 -*-
"""Scan every ai_relationships INSERT in the Phase-3 seed for overlong
source_id / target_id (VARCHAR(40) columns)."""
import re

src = open('seed-731-cards-full.sql', encoding='utf-8').read()
lines = src.splitlines()
pat = re.compile(r"'((?:[^'\\]|\\.)*)'")
total = 0
bad = []
for i, l in enumerate(lines):
    if not l.startswith('('):
        continue
    if "INSERT" in l:
        continue
    # must be a relationship tuple: 11th field is a timestamp, 8th is confidence
    # quick filter: line contains 'rel-'
    if "'rel-" not in l:
        continue
    total += 1
    lits = pat.findall(l)
    if len(lits) < 10:
        continue
    # 10 quoted literals per rel tuple (confidence unquoted)
    src_id = lits[2]
    tgt_id = lits[5]
    if len(src_id) > 40:
        bad.append(('source_id', i + 1, src_id, len(src_id)))
    if len(tgt_id) > 40:
        bad.append(('target_id', i + 1, tgt_id, len(tgt_id)))
print('rel tuples scanned:', total)
print('overlong ids:', len(bad))
for b in bad[:30]:
    print(b)
