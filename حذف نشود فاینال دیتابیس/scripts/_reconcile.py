import pymysql, json, re, unicodedata
from collections import Counter

c = pymysql.connect(host="127.0.0.1", user="root", password="433700", database="resaname_kb_final_inspect", charset="utf8mb4")
cur = c.cursor()

# databases for context
cur.execute("SHOW DATABASES")
print("DATABASES:", [r[0] for r in cur.fetchall()])

cur.execute("SELECT code, canonical_name_fa, canonical_name_en, entity_type, properties FROM kb_entities")
rows = cur.fetchall()

def norm(s):
    s = unicodedata.normalize("NFKC", s or "")
    s = s.replace("\u200c","").replace("\u0640","")
    s = s.replace("آ","a").replace("أ","a").replace("إ","a")
    s = s.replace("ى","i").replace("ی","i")
    s = s.replace("ك","k")
    s = re.sub(r"[\s.,:؛;()\-_/\\|'\"«»؟?!.]+", "", s)
    return s.lower()

pre = [r for r in rows if "taxonomy_seed_20261115" not in (r[4] or "")]
mine = [r for r in rows if "taxonomy_seed_20261115" in (r[4] or "")]
print(f"\npre-existing rows: {len(pre)} | my inserted rows: {len(mine)}")

# duplicate-name check: my names vs pre-existing names (normalized full & core)
def core(s):
    s = s.strip()
    for w in ("نظریه","نظریه‌","نظریه‌ی","مدل","الگو"):
        if s.startswith(w) and len(s) > len(w):
            s = s[len(w):].strip(" -‌ـ")
    for w in ("نظریه‌ای","نظریه","ی","مدل","الگو"):
        if s.endswith(w) and len(s) > len(w):
            s = s[:-len(w)].strip(" -‌ـ")
    return s

pre_names = {norm(r[1]) for r in pre}
pre_names_core = {}
for r in pre:
    pre_names_core.setdefault(norm(core(r[1])), []).append(r[0])

dups_full, dups_core = [], []
for r in mine:
    nm = norm(r[1])
    if nm in pre_names:
        dups_full.append(r[1])
    else:
        kc = norm(core(r[1]))
        if kc in pre_names_core:
            dups_core.append((r[1], r[2], pre_names_core[kc]))

print(f"\n== my items whose FULL normalized name equals a pre-existing entity ==")
for d in dups_full:
    print("  DUP(full):", d)
print("count:", len(dups_full))

print(f"\n== my items whose CORE (theory/model stripped) matches a pre-existing entity ==")
for d in dups_core:
    print(f"  DUP(core): {d[0]!r} en={d[1]!r} -> pre {d[2]}")
print("count:", len(dups_core))

# check the earlier _existing_names.json count
try:
    em = json.load(open(r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_existing_names.json", encoding="utf-8"))
    print(f"\n_existing_names.json entries: {len(em)}")
    # how many of my inserted names were already in that dump (would've been matched)
    dump_norms = {norm(e.get("canonical_name_fa")) for e in em}
    matched_any = [r[1] for r in mine if norm(r[1]) in dump_norms]
    print("my inserted names also present in the dump file:", len(matched_any))
    for m in matched_any[:20]:
        print("   ", m)
except Exception as e:
    print("dump check error:", e)

# sanity: sample of pre-existing names to confirm it's a communication-theory KB
print("\n== sample of 12 pre-existing entity names ==")
for r in pre[:12]:
    print("  ", r[0], r[3], r[1])

c.close()
print("RECONCILE DONE")
