# -*- coding: utf-8 -*-
import sys, json, re
import pymysql

codes = sys.argv[1:]
conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="433700",
                       database="resaname_kb_final_inspect", charset="utf8mb4")
cur = conn.cursor()
cur.execute("SELECT code,properties FROM kb_entities WHERE code IN (%s)" %
            ",".join(["%s"] * len(codes)), codes)
d = {c: json.loads(p or "{}") for c, p in cur.fetchall()}
conn.close()

WORD_KEYS = ["summary", "definition", "main_problem", "mechanism", "critiques",
             "applications", "evolution", "key_concepts", "principles",
             "studies", "assumptions"]

def flat(v):
    if isinstance(v, str):
        return v
    if isinstance(v, list):
        return " ".join(flat(x) for x in v)
    if isinstance(v, dict):
        return " ".join(flat(x) for x in v.values())
    return ""

def wc(s):
    return len([t for t in re.split(r"\s+", s.strip()) if t])

LAT = re.compile(r"[A-Za-z]")
for c in codes:
    pr = d.get(c, {})
    print("=====", c, "| score", pr.get("quality_score"), "| year", pr.get("year"))
    tot = 0
    for k in WORD_KEYS:
        n = wc(flat(pr.get(k)))
        tot += n
        print("   %-14s %4d" % (k, n))
    print("   TOTAL", tot)
    print("   sources:", json.dumps(pr.get("sources"), ensure_ascii=False)[:400])
    print("   citations:", json.dumps(pr.get("citations"), ensure_ascii=False)[:400])
    print("   theorists_text:", pr.get("theorists_text"))
    print("   recommended:", str(pr.get("recommended_sources"))[:200])
    lk = []
    for k, v in pr.items():
        if k in ("mapping", "sources", "citations", "image_url"):
            continue
        if LAT.search(flat(v)):
            lk.append(k)
    print("   LATIN keys:", lk)
