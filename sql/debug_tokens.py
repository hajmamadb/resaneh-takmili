# -*- coding: utf-8 -*-
import importlib.util
def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m
src = open('phase4-theories.sql', encoding='utf-8').read()
v = load('vf', 'verify_final.py')
c = load('cr', 'count_rows.py')
blocks = v.find_block(src, 'ai_documents')
print('verify_final blocks:', len(blocks), [len(b) for b in blocks])
t1 = v.tokenize_values(blocks[0])
t2 = c.count_value_tuples(blocks[0])
print('verify_final tuples:', len(t1), '| count_rows tuples:', t2)
b = blocks[0]
BS = chr(92)
depth = 0; in_str = False; esc = False; maxdepth = 0; opens = 0; closes = 0
for ch in b:
    if in_str:
        if esc: esc = False
        elif ch == BS: esc = True
        elif ch == "'": in_str = False
        continue
    if ch == "'": in_str = True; continue
    if ch == '(': depth += 1; opens += 1
    if ch == ')':
        if depth > 0: depth -= 1
        closes += 1
    if depth > maxdepth: maxdepth = depth
print('opens:', opens, 'closes:', closes, 'final depth:', depth, 'max depth:', maxdepth)
