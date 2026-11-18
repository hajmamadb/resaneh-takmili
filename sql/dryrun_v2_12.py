# -*- coding: utf-8 -*-
import re, pymysql
TWELVE = ['doc-new-book-21', 'doc-new-book-22',
          'doc-new-journal-16', 'doc-new-journal-17', 'doc-new-journal-18',
          'doc-new-journal-19', 'doc-new-journal-20',
          'doc-new-theorist-21', 'doc-new-theorist-22', 'doc-new-theorist-23',
          'doc-new-theorist-24', 'doc-new-theorist-25']
MAX_CHARS = 680
OVERLAP = 80
SENT_END = re.compile(r'(?<=[.!?؟۔…])\s+')

def split_text(text, max_chars=MAX_CHARS, overlap=OVERLAP):
    text = text.strip()
    if len(text) <= max_chars:
        return [text] if text else []
    out, start, n = [], 0, len(text)
    while start < n:
        end = min(start + max_chars, n)
        if end < n:
            seg = text[start:end]
            m = None
            for m in SENT_END.finditer(seg):
                pass
            if m and m.start() >= max_chars * 0.5:
                end = start + m.end()
            else:
                sp = seg.rfind(' ')
                if sp >= max_chars * 0.4:
                    end = start + sp
        c = text[start:end].strip()
        if c:
            out.append(c)
        if end >= n:
            break
        start = max(end - overlap, start + 1)
    return out

conn = pymysql.connect(host='127.0.0.1', user='root', password='433700',
                       database='resaname_v2', charset='utf8mb4')
cur = conn.cursor()
ph = ','.join(['%s'] * len(TWELVE))
cur.execute(
    "SELECT id, content_id, section_key, IFNULL(section_title,''), content, sort_order "
    "FROM sections WHERE content_id IN (" + ph + ") ORDER BY content_id, sort_order",
    TWELVE)
secs = cur.fetchall()
cur.execute(
    "SELECT id, IFNULL(summary,'') FROM contents WHERE id IN (" + ph + ")", TWELVE)
summ = {r[0]: (r[1] or '').strip() for r in cur.fetchall()}
by = {}
for s in secs:
    by.setdefault(s[1], []).append(s)
tot = 0
for cid in TWELVE:
    sc = 1 if (cid in summ and summ[cid]) else 0
    c = sum(len(split_text(s[4])) for s in sorted(by.get(cid, []), key=lambda x: x[5]))
    print(f"  {cid}: summary={sc} + section_chunks={c} = {sc + c}")
    tot += sc + c
print("TOTAL chunks:", tot)
print("total sections:", len(secs))
conn.close()
