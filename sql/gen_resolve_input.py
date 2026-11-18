# -*- coding: utf-8 -*-
"""Build the LLM input for resolving the remaining 94 __unresolved labels.
For each unmatched label, emit a candidate pool = top contents by English- and
Persian-title similarity (token-overlap scoring). Output: resolve_labels.json
(the 94 unmatched labels + their candidates) and the deterministic 36 already
mapped into resolve_deterministic.json.
"""
import re, json
import pymysql
from collections import Counter

def normalize(s):
    s = s.lower().strip().rstrip('.').strip()
    s = s.replace('\u200c', ' ')
    s = re.sub(r'\s+', ' ', s)
    return s

def tokens(s):
    return set(re.findall(r'[a-z0-9]+', s)) | set(re.findall(r'[\u0600-\u06FF]+', s))

conn = pymysql.connect(host='127.0.0.1', user='root', password='433700',
                       database='resaname_v2', charset='utf8mb4')
cur = conn.cursor()
cur.execute("SELECT id, IFNULL(english_title,''), IFNULL(title,'') FROM contents")
contents = [(cid, en, fa) for cid, en, fa in cur.fetchall()]

cur.execute("SELECT DISTINCT target_id FROM relation_links WHERE target_id LIKE '%__unresolved'")
labels = [r[0].replace('__unresolved', '').strip().rstrip('.').strip() for r in cur.fetchall()]

en_to_id = {}
fa_to_id = {}
for cid, en, fa in contents:
    n = normalize(en)
    if n:
        en_to_id.setdefault(n, cid)
    n2 = normalize(fa)
    if n2:
        fa_to_id.setdefault(n2, cid)

def en_term(concept):
    m = re.match(r'^(.*?)\s*\(([^)]*)\)\s*$', concept)
    if m and m.group(2):
        return m.group(2).strip()
    m2 = re.search(r'\(([^)]*)$', concept)
    if m2 and m2.group(1) and m2.group(1)[0].isascii():
        return m2.group(1).strip().rstrip(')')
    return None

def fa_part(concept):
    m = re.match(r'^(.*?)\s*\(([^)]*)\)\s*$', concept)
    if m and m.group(1):
        return m.group(1).strip()
    return concept.rstrip('.').strip()

def deterministic(concept):
    et, fp = en_term(concept), fa_part(concept)
    if et:
        en = normalize(et)
        if en in en_to_id:
            return en_to_id[en], 'en-exact'
        for n, cid in en_to_id.items():
            if en and (en in n or n in en) and min(len(en), len(n)) >= 4:
                return cid, 'en-sub'
    if fp:
        fn = normalize(fp)
        if fn in fa_to_id:
            return fa_to_id[fn], 'fa-exact'
        best = (None, 0)
        for n, cid in fa_to_id.items():
            if n and (fn in n or n in fn) and len(n) >= 5 and len(n) > best[1]:
                best = (cid, len(n))
        if best[0]:
            return best[0], 'fa-sub'
    return None, None

def score_candidates(concept, topk=8):
    et, fp = en_term(concept) or '', fa_part(concept)
    ct = tokens(normalize(et)) | tokens(normalize(fp))
    scored = []
    for cid, en, fa in contents:
        en_t = tokens(normalize(en))
        fa_t = tokens(normalize(fa))
        overlap_en = len(ct & en_t) / max(len(ct), 1) if ct else 0
        overlap_fa = len(tokens(normalize(fp)) & fa_t) / max(len(tokens(normalize(fp))), 1) if fa_part(concept) else 0
        s = max(overlap_en, overlap_fa)
        if s > 0:
            scored.append((s, cid, en, fa))
    scored.sort(key=lambda x: -x[0])
    out = []
    for s, cid, en, fa in scored[:topk]:
        out.append({'id': cid, 'fa': fa, 'en': en, 'sim': round(s, 3)})
    return out

det = {}
unmatched = []
for lab in labels:
    cid, method = deterministic(lab)
    if cid:
        det[lab] = {'content_id': cid, 'method': method}
    else:
        unmatched.append(lab)

out = []
for lab in unmatched:
    out.append({
        'label': lab,
        'en_term': en_term(lab),
        'fa_part': fa_part(lab),
        'candidates': score_candidates(lab),
    })

json.dump(det, open('resolve_deterministic.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(out, open('resolve_labels.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f"deterministic labels: {len(det)}")
print(f"unmatched labels -> resolve_labels.json: {len(out)}")
print(f"avg candidates per label: {sum(len(o['candidates']) for o in out)/len(out):.1f}")
# how many labels have ZERO candidates
zero = [o['label'] for o in out if not o['candidates']]
print(f"labels with zero candidates: {len(zero)}")
for z in zero:
    print("  " + z)
conn.close()
