# -*- coding: utf-8 -*-
"""Authoritative per-table row counts: sum of 4 source files vs the merged file."""
import re

def count_value_tuples(block):
    depth = 0; cnt = 0; in_str = False; esc = False; i = 0
    n = len(block)
    while i < n:
        c = block[i]
        if in_str:
            if esc: esc = False
            elif c == chr(92): esc = True
            elif c == "'": in_str = False
            i += 1; continue
        if c == "'": in_str = True; i += 1; continue
        if c == '(':
            depth += 1
            if depth == 1: cnt += 1
            i += 1; continue
        if c == ')':
            if depth > 0:
                depth -= 1
            in_str = False
            i += 1; continue
        i += 1
    return cnt

def table_counts(path):
    src = open(path, encoding='utf-8').read()
    res = {}
    for table in ['ai_documents','ai_document_sections','ai_entities',
                  'ai_references','ai_document_references','ai_relationships']:
        total = 0
        # match each INSERT ... VALUES <block>;  block ends at first ';' that is outside a string
        pos = 0
        while True:
            idx = src.find('INSERT INTO `%s`' % table, pos)
            if idx == -1: break
            # find the VALUES keyword
            v = src.find('VALUES', idx)
            # scan to the terminating ';' outside strings
            i = v + 6
            in_str = False; esc = False
            term = -1
            while i < len(src):
                c = src[i]
                if in_str:
                    if esc: esc = False
                    elif c == chr(92): esc = True
                    elif c == "'": in_str = False
                else:
                    if c == "'": in_str = True
                    elif c == ';':
                        term = i; break
                i += 1
            block = src[v+6:term]
            total += count_value_tuples(block)
            pos = term + 1
        res[table] = total
    return res

srcs = ['phase4-theorists.sql','phase4-theories.sql','phase4-books.sql','phase4-journals.sql']
tables = ['ai_documents','ai_document_sections','ai_entities',
          'ai_references','ai_document_references','ai_relationships']

print('%-26s' % 'table', '  ' + '  '.join(s.replace('phase4-','').replace('.sql','') for s in srcs) + '   SUM')
sums = {t:0 for t in tables}
for s in srcs:
    c = table_counts(s)
    for t in tables:
        sums[t] += c[t]
    print('%-26s' % s.replace('phase4-','').replace('.sql',''),
          '  '.join('%4d' % c[t] for t in tables))
print('-' * 90)
merged = table_counts('seed-phase4-70-items.sql')
print('%-26s' % 'MERGED', '  '.join('%4d' % merged[t] for t in tables))
print('%-26s' % 'EXPECTED-SUM', '  '.join('%4d' % sums[t] for t in tables))
print()
ok = all(merged[t] == sums[t] for t in tables)
print('MERGED == SUM of 4 sources for ALL tables:', ok)
for t in tables:
    flag = 'OK ' if merged[t]==sums[t] else 'XX '
    print('  %s %-24s merged=%d sum=%d' % (flag, t, merged[t], sums[t]))
print()
print('ai_documents total new (should be 70):', sums['ai_documents'])
