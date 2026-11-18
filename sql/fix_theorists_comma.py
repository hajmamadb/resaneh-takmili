# -*- coding: utf-8 -*-
import re
p = 'phase4-theorists.sql'
s = open(p, encoding='utf-8').read()
before = s.count(');,')
s2 = s.replace(');,', ');')
open(p, 'w', encoding='utf-8', newline='').write(s2)
after = s2.count(');,')
print('stray before=%d after=%d' % (before, after))
lines = s2.splitlines()
bad = [l[-70:] for l in lines
       if l.strip().startswith('INSERT INTO `ai_relationships`')
       and not l.rstrip().endswith(');')]
print('ai_relationships lines NOT ending with ");":', len(bad))
for b in bad[:5]:
    print('  BAD TAIL:', b)
# also ensure no INSERT ... VALUES line has a dangling comma at EOL
dangling = [l[-40:] for l in lines if l.rstrip().endswith(',')]
print('lines ending with a comma:', len(dangling))
for d in dangling[:5]:
    print('  DANGLE:', d)
