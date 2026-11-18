# -*- coding: utf-8 -*-
import json, os

base = r"D:\رسانامه تکمیلی\knowledge-core\tools"
inp = json.load(open(os.path.join(base, "kg_abs_in", "in-06.json"), encoding="utf-8"))

content = []
for f in ["_abs_a.json", "_abs_b.json", "_abs_c.json", "_abs_d.json"]:
    with open(os.path.join(base, f), encoding="utf-8") as fh:
        content += json.load(fh)

by_id = {c["id"]: c for c in content}
order = [e["id"] for e in inp]

assert len(content) == 28, len(content)
assert len(by_id) == 28
missing = [i for i in order if i not in by_id]
extra = [c["id"] for c in content if c["id"] not in order]
print("missing:", missing)
print("extra:", extra)

ok = True
for i in order:
    a = by_id[i]["abstract_fa"]
    k = by_id[i]["key_propositions_fa"]
    L = len(a)
    if not (150 <= L <= 400):
        ok = False
        print("LEN out of range:", i, L)
    if not (3 <= len(k) <= 5):
        ok = False
        print("KP out of range:", i, len(k))
    for key in ("id", "abstract_fa", "key_propositions_fa"):
        if key not in by_id[i]:
            ok = False
            print("MISSING KEY:", i, key)

out = [
    {
        "id": i,
        "abstract_fa": by_id[i]["abstract_fa"],
        "key_propositions_fa": by_id[i]["key_propositions_fa"],
    }
    for i in order
]

outdir = os.path.join(base, "kg_abstracts_out")
os.makedirs(outdir, exist_ok=True)
outpath = os.path.join(outdir, "batch-06.json")
with open(outpath, "w", encoding="utf-8") as fh:
    json.dump(out, fh, ensure_ascii=False, indent=2)

# re-validate by loading the written file
re = json.load(open(outpath, encoding="utf-8"))
assert len(re) == 28
assert [x["id"] for x in re] == order
print("validation-ok:", ok)
