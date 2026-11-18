# -*- coding: utf-8 -*-
"""فاز B — مرحله ۳: ذخیره امتیاز برترین موجودیت برای هر ۸۵۲ محتوا (بدون آستانه)
ورودی:  state embed عنوان‌ها (kg_link_state.json) + kg_vectors
خروجی:  kg_link_scores_all.json
   [{"content_id","content_title","top_score","top_entity_id","top_title_fa",
     "top_type","top2":{...},"top3":{...}}, ...]  (نرخ‌شده به 4 رقم)
بدون نیاز به embed مجدد — فقط ضرب برداری.
"""
import json

import numpy as np

# reuse the exact same load pipeline as kg_link_candidates.py
exec(open("kg_link_candidates.py", encoding="utf-8").read().split(
    "# --- score ---------------------------------------------------------------------")[0])
# ^ loads: contents, entities, cv, kgv, kg_ent_of, vecs (resumed from state)

kg_ids = list(kgv.keys())
kg_mat = np.stack([kgv[k] / max(np.linalg.norm(kgv[k]), 1e-9) for k in kg_ids])
kg_idx = {e["id"]: i for i, e in enumerate(entities)}


def norm(x):
    n = np.linalg.norm(x)
    return x / n if n > 0 else x


ent_idx = np.array([kg_idx[kg_ent_of[k]] for k in kg_ids])
qmat = np.stack([norm(np.asarray(v, dtype=np.float32)) for v in vecs])
SIM = qmat @ kg_mat.T  # (852, 4464)
ent_max = np.full((len(contents), len(entities)), -2.0)
np.maximum.at(ent_max, (np.repeat(np.arange(len(contents)), len(kg_ids)),
                        np.tile(ent_idx, len(contents))), SIM.ravel())

out = []
for ci, c in enumerate(contents):
    row = np.asarray(ent_max[ci])
    order = np.argsort(-row)[:3]
    tops = []
    for pos in order:
        e = entities[pos]
        tops.append({"entity_id": e["id"], "title_fa": e["title_fa"],
                     "entity_type": e["entity_type"],
                     "score": round(float(row[pos]), 4)})
    out.append({"content_id": c["id"], "content_title": c["title"],
                "tops": tops})

json.dump(out, open("kg_link_scores_all.json", "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)

# distribution report
import collections
bands = collections.Counter()
for o in out:
    s = o["tops"][0]["score"]
    if s >= 0.80:
        bands["0.80+"] += 1
    elif s >= 0.72:
        bands["0.72-0.80"] += 1
    elif s >= 0.66:
        bands["0.66-0.72"] += 1
    elif s >= 0.60:
        bands["0.60-0.66"] += 1
    elif s >= 0.55:
        bands["0.55-0.60"] += 1
    elif s >= 0.50:
        bands["0.50-0.55"] += 1
    elif s >= 0.45:
        bands["0.45-0.50"] += 1
    elif s >= 0.40:
        bands["0.40-0.45"] += 1
    else:
        bands["<0.40"] += 1
for k in ["0.80+", "0.72-0.80", "0.66-0.72", "0.60-0.66",
          "0.55-0.60", "0.50-0.55", "0.45-0.50", "0.40-0.45", "<0.40"]:
    print(f"  {k}: {bands.get(k,0)}")
