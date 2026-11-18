# -*- coding: utf-8 -*-
"""Close the 15 theory ai_documents rows: each ends "00:00:00'," (or ");" for
the last) but is missing its closing tuple paren. Pattern inside the block:
  ... '2026-11-09 00:00:00',\n('doc-new-theory-N'  ->  ... '2026-11-09 00:00:00'),\n('doc-new-theory-N'
and the final row:
  ... '2026-11-09 00:00:00');  (before the sections INSERT) -> stays "00:00:00');"
"""
p = 'phase4-theories.sql'
s = open(p, encoding='utf-8').read()

i = s.find('INSERT INTO `ai_documents`')
j = s.find('INSERT INTO `ai_document_sections`')
assert 0 < i < j
head, block, tail = s[:i], s[i:j], s[j:]

# 14 row-boundaries: "00:00:00',\n('doc-new-theory-" -> "00:00:00'),\n('doc-new-theory-"
n = block.count("00:00:00',\n('doc-new-theory-")
assert n == 14, n
block = block.replace("00:00:00',\n('doc-new-theory-", "00:00:00'),\n('doc-new-theory-")

# 15th (final) row: must end with "00:00:00');" (the block may include trailing
# comment lines up to the next section, so look for the pattern, not the very tail)
assert "00:00:00');" in block, 'final-row terminator not found'

s2 = head + block + tail
open(p, 'w', encoding='utf-8', newline='').write(s2)
print('fixed 14 boundaries; final row tail OK')

# verify: 15 opening, 15 closing in the block
s3 = open(p, encoding='utf-8').read()
i3 = s3.find('INSERT INTO `ai_documents`')
j3 = s3.find('INSERT INTO `ai_document_sections`')
b3 = s3[i3:j3]
print('open   (doc-new-theory- :', b3.count("('doc-new-theory-"))
print('close  00:00:00),        :', b3.count("00:00:00'),"))
print('close  00:00:00);        :', b3.count("00:00:00');"))
print("tail :", repr(b3.rstrip()[-20:]))
