# -*- coding: utf-8 -*-
"""Verify the 4 phase4 partial seeds: counts, id uniqueness, rel types, statuses."""
import re
from collections import Counter

def check(fname, tables, expect_doc_count, doc_id_prefix):
    src = open(fname, encoding='utf-8').read()
    print('=' * 70)
    print('FILE:', fname, '| bytes:', len(src.encode('utf-8')))
    for t in tables:
        n = src.count('INSERT INTO `%s`' % t)
        print('  INSERT INTO %s: %d' % (t, n))

    # document rows -> verify content_hash == sha256(summary)
    import hashlib
    # doc rows look like ('doc-...', 'type', 'src', 'slug', 'title', 'eng', 'ctype', 'summary', ...
    # We'll extract per-line: split on ');' boundaries is messy; instead regex per statement block
    # Find the ai_documents block
    m = re.search(r"INSERT INTO `ai_documents`.*?VALUES(.*?);", src, re.S)
    ok = 0; bad = 0; total = 0
    if m:
        block = m.group(1)
        rows = re.findall(r"\((\"[^\"]*\"|'[^']*'|NULL)(?:\s*,\s*(\"[^\"]*\"|'[^']*'|NULL))*\)", block)  # not used
        # simpler: iterate tuples by matching 'doc-' start through ');'
        for dm in re.finditer(r"\('doc-[^\n]*?\)\s*;?", block):
            row = dm.group(0)
            total += 1
            # extract summary (7th value) and content_hash (13th)
            # split on ', ' at top level (strings contain ', ' too... risky)
            # instead: find all quoted strings in order
            strs = re.findall(r"'((?:[^'\\]|\\.)*)'", row)
            # strs order: id, source_type, source_id, slug, title, english_title, content_type, summary, canonical_url?, language, country, origin, content_hash...
            # canonical_url is NULL so not in strs. So index: 0=id,1=st,2=sid,3=slug,4=title,5=eng,6=ctype,7=summary,8=language,9=country?,10=origin,11=content_hash
            if len(strs) >= 12:
                summary = strs[7]
                ch = strs[11]
                real = hashlib.sha256(summary.encode('utf-8')).hexdigest()
                if ch == real:
                    ok += 1
                else:
                    bad += 1
                    if bad <= 3:
                        print('    HASH MISMATCH:', strs[0])
    print('  ai_documents hash check: ok=%d bad=%d total=%d' % (ok, bad, total))

    # all ids uniqueness across the file (any 'xxx-...' literal that looks like a key id)
    ids = re.findall(r"\((?:'|\")((?:doc|sec|ref|rel|entity)[^'\",]*)", src)
    dupes = {k: v for k, v in Counter(ids).items() if v > 1}
    print('  unique ids:', len(set(ids)), '| dupes:', dupes if dupes else 'none')

    # relationship types used
    rtypes = re.findall(r"'(extends|derived_from|related_to|contrasts_with|theorist|cites|applied_in|predates)'", src)
    print('  relationship types:', dict(Counter(rtypes)))

    # verification status distribution
    vstat = re.findall(r"'(verified|unverified|disputed)'", src)
    print('  verification statuses:', dict(Counter(vstat)))
    return total

tot = 0
tot += check('phase4-theorists.sql', ['ai_documents','ai_entities','ai_relationships'], 20, 'doc-new-theorist')
tot += check('phase4-theories.sql', ['ai_documents','ai_document_sections','ai_relationships'], 15, 'doc-new-theory')
tot += check('phase4-books.sql', ['ai_documents','ai_references','ai_document_references','ai_relationships'], 20, 'doc-new-book')
tot += check('phase4-journals.sql', ['ai_documents','ai_entities','ai_references','ai_document_references','ai_relationships'], 15, 'doc-new-journal')
print('=' * 70)
print('TOTAL ai_documents across 4 files: %d (expect 70)' % tot)
