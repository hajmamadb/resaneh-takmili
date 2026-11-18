# -*- coding: utf-8 -*-
"""Wrap the 15 theory ai_documents rows in parentheses (they were bare tuples)."""
import re
p = 'phase4-theories.sql'
s = open(p, encoding='utf-8').read()

# 1) VALUES\n'  ->  VALUES\n(
assert s.count("VALUES\n'") == 1, s.count("VALUES\n'")
s = s.replace("VALUES\n'", "VALUES\n('", 1)

# 2) the 14 row-boundaries inside that block: "00:00:00'),\n'doc-new-theory-"
n = s.count("00:00:00'),\n'doc-new-theory-")
print('row-boundary joins found:', n)
s = s.replace("00:00:00'),\n'doc-new-theory-", "00:00:00',\n('doc-new-theory-")

# 3) the final row of the block: the line ending with "00:00:00')," just before
#    the next INSERT (ai_document_sections) or blank line. Find the last
#    "00:00:00')," occurrence before 'INSERT INTO `ai_document_sections`'.
end = s.find('INSERT INTO `ai_document_sections`')
last = s.rfind("00:00:00');", 0, end)
assert last != -1, 'final-row terminator not found'
s = s[:last] + "00:00:00');" + s[last+len("00:00:00');"):]

open(p, 'w', encoding='utf-8', newline='').write(s)

# verify
s2 = open(p, encoding='utf-8').read()
print("VALUES-newline-paren (ai_documents block start):", s2.count("VALUES\n('doc-new-theory-1',"))
print("remaining bare joins:", s2.count("00:00:00'),\n'"))
i = s2.find('INSERT INTO `ai_document_sections`')
print('--- block tail before sections ---')
print(s2[i-200:i])
