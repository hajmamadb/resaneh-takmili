# -*- coding: utf-8 -*-
import re
src = open('phase4-theories.sql', encoding='utf-8').read()
print("lines starting with '(':", len(re.findall(r"^\(", src, re.M)))
print("lines starting with 'doc-new-theory':", len(re.findall(r"^'doc-new-theory", src, re.M)))
print("VALUES-newline-quote :", src.count("VALUES\n'"))
print("VALUES-newline-paren :", src.count("VALUES\n('"))
# per-table scan: does each INSERT VALUES start with '(' ?
for m in re.finditer(r"INSERT INTO `(\w+)`[^V]*VALUES\n(.{1})", src, re.S):
    pass
# simpler: for each INSERT, look at the char after 'VALUES\n'
for m in re.finditer(r"INSERT INTO `(\w+)`[^V]*VALUES\n", src):
    pos = m.end()
    ch = src[pos]
    t = m.group(1)
    print('table=%-24s first char after VALUES: %r' % (t, ch))
i = src.find('INSERT INTO `ai_document_sections`')
print('--- sections block head ---')
print(src[i:i+500])
