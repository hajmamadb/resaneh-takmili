# -*- coding: utf-8 -*-
"""Fix ai_references: insert NULL for `journal` (7th col) after publisher (6th col).
The 6th value is always NULL (publisher). Insert NULL after it.
"""
import re

src = open('seed-731-cards-full.sql', encoding='utf-8').read()
lines = src.splitlines()
fixed = 0
for i, l in enumerate(lines):
    if not l.startswith("('ref-"):
        continue
    # Pattern: ('ref-...', 'type', 'title', NULL, NULL, NULL, <next>, ...
    # After the 3rd quoted value (title), there are 3 NULLs (title_en, authors, publisher)
    # We need to insert a 4th NULL (journal) before the 7th value
    m = re.match(r"^('ref-[^\']*',\s*'[^']*',\s*'[^']*',\s*NULL,\s*NULL,\s*NULL),", l)
    if m:
        lines[i] = m.group(1) + ', NULL, ' + l[m.end():]
        fixed += 1
print('fixed rows:', fixed)
assert fixed == 731, f'Expected 731, got {fixed}'
open('seed-731-cards-full.sql', 'w', encoding='utf-8', newline='').write('\n'.join(lines))
print('file updated')
