# -*- coding: utf-8 -*-
"""Final column-accurate verification for the 4 phase4 seeds AND the merged file.
Fixes the lazy-regex flaw in verify_phase4_v2.py: the block is now located by a
string-aware scan to the terminating ';' (a ';' inside a quoted literal no longer
truncates the block). Every ai_documents row is hash-checked."""
import re, hashlib

def find_block(src, table):
    """Return the VALUES-payload (text between 'VALUES' and the terminating ';'
    outside of strings) for every INSERT INTO `table` ...; occurrence."""
    blocks = []
    pos = 0
    pat = 'INSERT INTO `%s`' % table
    while True:
        idx = src.find(pat, pos)
        if idx == -1:
            break
        v = src.find('VALUES', idx)
        if v == -1:
            break
        i = v + 6
        in_str = False; esc = False; term = -1
        while i < len(src):
            c = src[i]
            if in_str:
                if esc: esc = False
                elif c == chr(92): esc = True
                elif c == "'": in_str = False
            else:
                if c == "'": in_str = True
                elif c == ';':
                    term = i; break
            i += 1
        blocks.append(src[v+6:term])
        pos = term + 1
    return blocks

def tokenize_values(block):
    rows = []
    depth = 0; start = None; i = 0; in_str = False; esc = False
    n = len(block)
    while i < n:
        c = block[i]
        if in_str:
            if esc: esc = False
            elif c == chr(92): esc = True
            elif c == "'": in_str = False
            i += 1; continue
        if c == "'":
            in_str = True; i += 1; continue
        if c == '(':
            depth += 1
            if depth == 1: start = i + 1
            i += 1; continue
        if c == ')':
            if depth == 1 and start is not None:
                rows.append(block[start:i]); start = None
            if depth > 0:
                depth -= 1
            in_str = False
            i += 1; continue
        i += 1
    return rows

def split_fields(rowtext):
    fields = []; cur = ''; i = 0; in_str = False; esc = False
    n = len(rowtext)
    while i < n:
        c = rowtext[i]
        if in_str:
            if esc: cur += c; esc = False
            elif c == chr(92): cur += c; esc = True
            elif c == "'": in_str = False; cur += c
            else: cur += c
            i += 1; continue
        if c == "'":
            in_str = True; cur += c; i += 1; continue
        if c == ',':
            fields.append(cur.strip()); cur = ''; i += 1; continue
        cur += c; i += 1
    fields.append(cur.strip())
    return fields

def unescape_sql(s):
    if s == 'NULL':
        return None
    assert s[0] == "'" and s[-1] == "'", repr(s[:40])
    body = s[1:-1]; out = []; i = 0
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
    doc_total = 0
    if 'ai_documents' in tables:
        cols = None
        ok = bad = 0
        for m in re.finditer(r"INSERT INTO `ai_documents`\s*\(([^)]*)\)\s*VALUES", src):
            cols = [c.strip().strip('`') for c in m.group(1).split(',')]
            break
        assert cols, 'ai_documents column list not found'
        idx_sum = cols.index('summary'); idx_hash = cols.index('content_hash')
        for block in find_block(src, 'ai_documents'):
            for rt in tokenize_values(block):
                doc_total += 1
                fields = split_fields(rt)
                if len(fields) < len(cols):
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
        print('  ai_documents rows: %d | hash check ok=%d bad=%d' % (doc_total, ok, bad))
    for t in tables:
        if t == 'ai_documents':
            continue
        n = sum(len(tokenize_values(b)) for b in find_block(src, t))
        print('  %-26s rows: %d' % (t, n))
    return doc_total

tot = 0
for f in ['phase4-theorists.sql','phase4-theories.sql','phase4-books.sql','phase4-journals.sql']:
    tot += check(f, ['ai_documents','ai_document_sections','ai_entities',
                     'ai_references','ai_document_references','ai_relationships'])
merged = check('seed-phase4-70-items.sql',
               ['ai_documents','ai_document_sections','ai_entities',
                'ai_references','ai_document_references','ai_relationships'])
print('=' * 70)
print('TOTAL ai_documents (4 sources): %d (expect 70)' % tot)
print('ai_documents in MERGED file   : %d (expect 70)' % merged)
