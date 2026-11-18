# -*- coding: utf-8 -*-
import re, hashlib
src = open('phase4-books.sql', encoding='utf-8').read()
for n in [8, 18]:
    i = src.find("('doc-new-book-%d'" % n)
    j = src.find(');', i)
    row = src[i:j+2]
    print('==== BOOK', n, '====')
    print(row[:400])
    print('...')
    # print last 250 chars (tail: origin, hash, timestamps)
    print(row[-260:])
    print()
    # Extract all quoted strings in order, with positions
    strs = re.findall(r"'((?:[^'\\]|\\.)*)'", row)
    print('num strs =', len(strs))
    for k, s in enumerate(strs):
        print('  [%2d] %s' % (k, s[:70]))
    print()
