# -*- coding: utf-8 -*-
import subprocess

def db(sql):
    r = subprocess.run(
        ['C:/Program Files/MySQL/MySQL Server 8.0/bin/mysql.exe',
         '--default-character-set=utf8mb4', '-u', 'root', '-p433700', 'resaname_h',
         '-N', '-B', '-e', sql],
        capture_output=True, text=True, encoding='utf-8'
    )
    if r.returncode != 0:
        print("ERR", r.stderr[:300]); return ""
    return r.stdout

rows = db("SELECT document_id, REPLACE(REPLACE(REPLACE(content,'\\t',' '),'\\n',' '),'\\r',' ') FROM ai_document_sections;")
lines = [l for l in rows.splitlines() if l.strip()]
MAXC = 680
def nchunk(t):
    t = t.strip(); n = len(t)
    if n <= MAXC: return 1 if t else 0
    c = 1; start = 0
    while start < n:
        c += 1
        end = min(start + MAXC, n)
        if end >= n: break
        start = max(end - 80, start + 1)
    return c
tot = 0; mx = 0
for l in lines:
    doc, _, content = l.partition('\t')
    k = nchunk(content); tot += k; mx = max(mx, k)
summ = db("SELECT COUNT(*) FROM ai_documents WHERE summary IS NOT NULL AND summary != '';").strip()
print("sections:", len(lines))
print("content chunks:", tot)
print("max chunks/section:", mx)
print("doc summaries (chunk 0):", summ)
print("TOTAL chunks ~", tot + int(summ or 0))
