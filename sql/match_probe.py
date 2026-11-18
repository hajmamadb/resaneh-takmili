# -*- coding: utf-8 -*-
"""Probe: how well do the 130 labels' ENGLISH terms match contents.english_title?
English is the stable anchor (Persian wordings diverge)."""
import re
import pymysql

def normalize(s):
    s = s.lower().strip().rstrip('.').strip()
    s = s.replace('\u200c', ' ')
    s = re.sub(r'\s+', ' ', s)
    return s

conn = pymysql.connect(host='127.0.0.1', user='root', password='433700',
                       database='resaname_v2', charset='utf8mb4')
cur = conn.cursor()
cur.execute("SELECT id, IFNULL(english_title,'') FROM contents")
en_to_id = {}
enlist = []
for cid, en in cur.fetchall():
    n = normalize(en)
    if n:
        en_to_id.setdefault(n, cid)
        enlist.append((n, cid))
print("contents with english_title:", len(en_to_id))

cur.execute("SELECT DISTINCT target_id FROM relation_links WHERE target_id LIKE '%__unresolved'")
labels = [r[0] for r in cur.fetchall()]

def en_term(concept):
    # parenthetical english, if present
    m = re.match(r'^(.*?)\s*\(([^)]*)\)\s*$', concept)
    if m and m.group(2):
        return m.group(2).strip()
    # trailing ' (Flow' / ' (ELM' style
    m2 = re.search(r'\(([^)]*)$', concept)
    if m2 and m2.group(1) and m2.group(1)[0].isascii():
        return m2.group(1).strip().rstrip(')')
    return None

def fa_part(concept):
    m = re.match(r'^(.*?)\s*\(([^)]*)\)\s*$', concept)
    if m and m.group(1):
        return m.group(1).strip()
    return concept.rstrip('.').strip()

exact = fa_match = sub_match = nomatch = 0
nomatch_list = []
fa_to_id = {}
cur.execute("SELECT id, IFNULL(title,'') FROM contents")
for cid, fa in cur.fetchall():
    n = normalize(fa)
    if n:
        fa_to_id.setdefault(n, cid)

for t in labels:
    concept = t.replace('__unresolved', '').strip().rstrip('.').strip()
    et = en_term(concept)
    fp = fa_part(concept)
    hit = None
    # 1) english exact
    if et:
        en = normalize(et)
        if en in en_to_id:
            hit = ('en-exact', en_to_id[en])
        else:
            for n, cid in enlist:
                if en and (en in n or n in en) and min(len(en), len(n)) >= 4:
                    hit = ('en-sub', cid)
                    break
    # 2) persian exact
    if not hit and fp:
        fn = normalize(fp)
        if fn in fa_to_id:
            hit = ('fa-exact', fa_to_id[fn])
        else:
            best = (None, 0)
            for n, cid in fa_to_id.items():
                if n and (fn in n or n in fn) and len(n) >= 5 and len(n) > best[1]:
                    best = (cid, len(n))
            if best[0]:
                hit = ('fa-sub', best[0])
    if hit:
        if hit[0] == 'en-exact': exact += 1
        elif hit[0] == 'en-sub': sub_match += 1
        elif hit[0] in ('fa-exact', 'fa-sub'): fa_match += 1
    else:
        nomatch += 1
        nomatch_list.append(concept)

print(f"\nen-exact: {exact}  en-substring: {sub_match}  fa: {fa_match}  NOMATCH: {nomatch}")
print("\n--- NOMATCH (need LLM / manual) ---")
for c in nomatch_list:
    print("  " + c)
conn.close()
