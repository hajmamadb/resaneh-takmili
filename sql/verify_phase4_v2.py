# -*- coding: utf-8 -*-
"""Robust verify: parse each ai_documents row by column position using a proper SQL literal tokenizer."""
import re, hashlib

def tokenize_values(block):
    """Given a VALUES (...) block (may contain multiple tuples), return list of tuples of raw field strings."""
    rows = []
    depth = 0
    cur = []
    i = 0
    in_str = False
    esc = False
    n = len(block)
    # First, split into top-level tuples by scanning parens
    start = None
    while i < n:
        c = block[i]
        if in_str:
            if esc:
                esc = False
            elif c == chr(92):  # backslash
                esc = True
            elif c == "'":
                in_str = False
            i += 1
            continue
        if c == "'":
            in_str = True
            i += 1
            continue
        if c == '(':
            depth += 1
            if depth == 1:
                start = i + 1
            i += 1
            continue
        if c == ')':
            depth -= 1
            if depth == 0 and start is not None:
                rows.append(block[start:i])
                start = None
            i += 1
            continue
        i += 1
    return rows

def split_fields(rowtext):
    fields = []
    cur = ''
    i = 0
    in_str = False
    esc = False
    n = len(rowtext)
    while i < n:
        c = rowtext[i]
        if in_str:
            if esc:
                cur += c
                esc = False
            elif c == chr(92):
                cur += c
                esc = True
            elif c == "'":
                in_str = False
                cur += c
            else:
                cur += c
            i += 1
            continue
        if c == "'":
            in_str = True
            cur += c
            i += 1
            continue
        if c == ',':
            fields.append(cur.strip())
            cur = ''
            i += 1
            continue
        cur += c
        i += 1
    fields.append(cur.strip())
    return fields

def unescape_sql(s):
    # s is a quoted literal including surrounding quotes, or NULL
    if s == 'NULL':
        return None
    assert s[0] == "'" and s[-1] == "'"
    body = s[1:-1]
    # process backslash escapes and '' doubling
    out = []
    i = 0
    while i < len(body):
        c = body[i]
        if c == chr(92) and i + 1 < len(body):
            out.append(body[i+1]); i += 2
        elif c == "'" and i + 1 < len(body) and body[i+1] == "'":
            out.append("'"); i += 2
        else:
            out.append(c); i += 1
    return ''.join(out)

def check(fname, tables):
    src = open(fname, encoding='utf-8').read()
    print('=' * 70)
    print('FILE:', fname)
    for t in tables:
        n = src.count('INSERT INTO `%s`' % t)
        print('  INSERT INTO %s: %d' % (t, n))
    m = re.search(r"INSERT INTO `ai_documents`\s*\(([^)]*)\)\s*VALUES\s*(.*?);", src, re.S)
    if not m:
        print('  (no ai_documents block found)')
        return 0
    cols = [c.strip().strip('`') for c in m.group(1).split(',')]
    idx_sum = cols.index('summary')
    idx_hash = cols.index('content_hash')
    total = ok = bad = 0
    rows = tokenize_values(m.group(2))
    for rt in rows:
        total += 1
        fields = split_fields(rt)
        if len(fields) < len(cols):
            # field count mismatch: row text may contain multi-line; report
            print('    WARN field count %d < %d cols' % (len(fields), len(cols)))
            continue
        summary = unescape_sql(fields[idx_sum])
        ch = unescape_sql(fields[idx_hash])
        real = hashlib.sha256((summary or '').encode('utf-8')).hexdigest()
        if ch == real:
            ok += 1
        else:
            bad += 1
            print('    HASH MISMATCH:', fields[0])
    print('  ai_documents hash check (column-accurate): ok=%d bad=%d total=%d' % (ok, bad, total))
    # relationship types
    from collections import Counter
    rtypes = re.findall(r"'(extends|derived_from|related_to|contrasts_with|theorist|cites|applied_in|predates)'", src)
    print('  relationship types:', dict(Counter(rtypes)))
    vstat = re.findall(r"'(verified|unverified|disputed)'", src)
    print('  verification statuses:', dict(Counter(vstat)))
    return total

tot = check('phase4-theorists.sql', ['ai_documents','ai_entities','ai_relationships'])
tot += check('phase4-theories.sql', ['ai_documents','ai_document_sections','ai_relationships'])
tot += check('phase4-books.sql', ['ai_documents','ai_references','ai_document_references','ai_relationships'])
tot += check('phase4-journals.sql', ['ai_documents','ai_entities','ai_references','ai_document_references','ai_relationships'])
print('=' * 70)
print('TOTAL ai_documents across 4 files: %d (expect 70)' % tot)
