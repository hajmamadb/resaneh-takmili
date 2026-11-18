# -*- coding: utf-8 -*-
"""Fix ai_references: insert NULL for `journal` after the 6th value.
Split on commas (accounting for quoted strings), insert NULL after position 6.
"""
import re

def split_sql_values(s):
    """Split SQL VALUES tuple into parts, respecting quoted strings."""
    parts = []
    in_str = False
    esc = False
    cur = []
    for ch in s:
        if in_str:
            if esc:
                esc = False
                cur.append(ch)
            elif ch == '\\':
                esc = True
                cur.append(ch)
            elif ch == "'":
                in_str = False
                cur.append(ch)
            else:
                cur.append(ch)
        else:
            if ch == "'":
                in_str = True
                cur.append(ch)
            elif ch == ',':
                parts.append(''.join(cur).strip())
                cur = []
            else:
                cur.append(ch)
    if cur:
        parts.append(''.join(cur).strip())
    return parts

src = open('seed-731-cards-full.sql', encoding='utf-8').read()
lines = src.splitlines()
fixed = 0
for i, l in enumerate(lines):
    if not l.startswith("('ref-"):
        continue
    # Remove trailing );
    if l.endswith(');'):
        body = l[1:-2]  # remove leading ( and trailing );
    else:
        body = l[1:-1]  # remove leading ( and trailing )
    parts = split_sql_values(body)
    # Insert NULL after index 5 (6th value = publisher)
    parts.insert(6, 'NULL')
    lines[i] = '(' + ', '.join(parts) + ');'
    fixed += 1
print('fixed rows:', fixed)
assert fixed == 731, f'Expected 731, got {fixed}'
open('seed-731-cards-full.sql', 'w', encoding='utf-8', newline='').write('\n'.join(lines))
print('file updated')
