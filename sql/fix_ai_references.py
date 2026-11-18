# -*- coding: utf-8 -*-
"""Fix ai_references INSERT: add missing NULL for `journal` column (7th position).
Current: ('id', 'ref_type', 'title', NULL, NULL, NULL, 1972, ...
Should be: ('id', 'ref_type', 'title', NULL, NULL, NULL, NULL, 1972, ...
"""
import re

src = open('seed-731-cards-full.sql', encoding='utf-8').read()
lines = src.splitlines()
fixed = 0
for i, l in enumerate(lines):
    if l.startswith("('ref-") and 'INSERT' not in l:
        # Insert NULL after the 6th value (before publication_year)
        # Pattern: ('ref-...', 'type', 'title', v4, v5, v6, YEAR, ...
        # The 6th value (index 5) is publisher, 7th (index 6) should be journal (NULL)
        # Find the pattern: ... , NULL, 1972, ... -> ... , NULL, NULL, 1972, ...
        # More robust: match the specific pattern where a year follows a NULL
        m = re.match(r"^(('ref-[^']*',\s*'[^']*',\s*'[^']*',\s*NULL,\s*NULL,\s*NULL),\s*)(\d{4}),", l)
        if m:
            lines[i] = m.group(1) + ', NULL, ' + m.group(3) + l[m.end()-1:]
            fixed += 1
print('fixed rows:', fixed)
open('seed-731-cards-full.sql', 'w', encoding='utf-8', newline='').write('\n'.join(lines))
print('file updated')
