# -*- coding: utf-8 -*-
import io, re, sys, json
import pymysql

TOPF = sys.argv[1]
BATCH = sys.argv[2]
src = io.open(TOPF, encoding='utf-8').read()
cut = src.find('NAME_FIX = {}')
g = {}
exec(compile(src[:cut], TOPF, 'exec'), g)

ENRICH = g['ENRICH']
DB = g['DB']
WORD_KEYS = ["summary", "definition", "main_problem", "mechanism", "critiques",
             "applications", "evolution", "key_concepts", "principles",
             "studies", "assumptions"]

def flatten(v):
    if isinstance(v, str):
        return v
    if isinstance(v, list):
        out = []
        for it in v:
            if isinstance(it, str):
                out.append(it)
            elif isinstance(it, dict):
                out.append(" ".join(str(x) for x in it.values()))
        return " ".join(out)
    if isinstance(v, dict):
        return " ".join(str(x) for x in v.values())
    return ""

def wc(s):
    return len([t for t in re.split(r"\s+", s.strip()) if t])

conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="433700",
                       database=DB, charset="utf8mb4", autocommit=False)
cur = conn.cursor()
codes = list(ENRICH.keys())
cur.execute("SELECT code, properties FROM kb_entities WHERE code IN (%s)" %
            ",".join(["%s"] * len(codes)), codes)
props = {c: json.loads(p) if p else {} for c, p in cur.fetchall()}
conn.close()

APPEND = g.get('APPEND', {})
MERGED = {"mechanism", "studies", "principles", "assumptions"}
LAT = re.compile(r"[A-Za-z]")

def leaks(v, path, out):
    if isinstance(v, str):
        if LAT.search(v):
            out.append((path, v[:120]))
    elif isinstance(v, list):
        for i, it in enumerate(v):
            leaks(it, path + "[%d]" % i, out)
    elif isinstance(v, dict):
        for k, it in v.items():
            leaks(it, path + "." + str(k), out)

bad = 0
for c in codes:
    pr = props.get(c, {})
    ap = APPEND.get(c, {})
    new = dict(ENRICH[c])
    for k, v in ap.items():
        base = new.get(k, pr.get(k))
        if isinstance(v, list):
            bl = base if isinstance(base, list) else ([base] if base else [])
            new[k] = bl + v
        else:
            new[k] = (base or "") + v
    total = 0
    detail = []
    for k in WORD_KEYS:
        old = pr.get(k, "")
        nv = new.get(k, None)
        if k in MERGED:
            old_list = old if isinstance(old, list) else ([old] if old else [])
            new_list = nv if isinstance(nv, list) else ([nv] if nv not in (None, "") else [])
            merged = list(old_list)
            for it in new_list:
                if it not in merged:
                    merged.append(it)
            txt = flatten(merged)
        elif nv is None:
            txt = flatten(old)
        else:
            txt = flatten(nv)
        total += wc(txt)
        detail.append((k, wc(txt)))
    lk = []
    for k, v in (ap if ap else new).items():
        if k == "mapping":
            continue
        leaks(v, k, lk)
    flag = "OK " if total >= 500 and not lk else "FIX"
    if flag == "FIX":
        bad += 1
    print("[%s] %s words=%d %s" % (flag, c, total, detail))
    for p, t in lk:
        print("     LEAK %s :: %s" % (p, t))
print("---- cards needing fix:", bad)
