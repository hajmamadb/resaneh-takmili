# -*- coding: utf-8 -*-
import re
src = open('seed-phase4-70-items.sql', encoding='utf-8').read()
vocab = {'extends','derived_from','related_to','contrasts_with','theorist','cites','applied_in','predates'}
stypes = {'card','theorist','book','journal','theory','document','entity'}
lines = [l for l in src.splitlines() if l.strip().startswith('INSERT INTO `ai_relationships`')]
bad = []
checked = 0
for l in lines:
    m = re.match(r"INSERT INTO `ai_relationships`\s*\(([^)]*)\)\s*VALUES\s*\((.*)\);\s*$", l.strip())
    if not m:
        bad.append(('nomatch', l[:70])); continue
    cols = [c.strip().strip('`') for c in m.group(1).split(',')]
    rt_col = cols.index('relationship_type')
    # confidence (DECIMAL) is unquoted, so expect len(cols)-1 quoted literals
    lits = re.findall(r"'((?:[^'\\]|\\.)*)'", m.group(2))
    if len(lits) != len(cols) - 1:
        bad.append(('short', len(lits), len(cols))); continue
    checked += 1
    # reindex: every quoted literal before the confidence column keeps its
    # column index; the columns after shift by one.
    def lit_for(colname):
        ci = cols.index(colname)
        conf = cols.index('confidence')
        return lits[ci] if ci < conf else lits[ci - 1]
    rt = lit_for('relationship_type')
    if rt not in vocab:
        bad.append(('bad-rel-type', rt))
    st = lit_for('source_type')
    tt = lit_for('target_type')
    if st not in stypes or tt not in stypes:
        bad.append(('bad-typefield', st, tt))
print('checked:', checked, '| bad:', len(bad))
for b in bad[:8]:
    print('  ', b)
print('all OK' if not bad else 'PROBLEMS FOUND')
