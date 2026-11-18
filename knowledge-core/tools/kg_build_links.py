# -*- coding: utf-8 -*-
"""فاز B — مرحله ۲: ساخت SQL بارگذاری کاندیداهای اتصال در entity_content_links
ورودی:  kg_link_candidates.json (خروجی kg_link_candidates.py)
خروجی:  kg_links.sql  (INSERT ... ON DUPLICATE KEY UPDATE —幂otent)

قاعده‌ی link_type بر پایه‌ی امتیاز (سندسی برای مرور کارشناسی در فاز C):
  score >= 0.80  -> same_as    (محتوا تقریباً همان موجودیت هسته است)
  0.72 <= s < 0.80 -> primary  (محتوا مستقیماً درباره‌ی همین موجودیت است)
  s < 0.72        -> related   (مرتبط؛ نیازمند تأیید کارشناسی)
"""
import json

CANDS = "D:/رسانامه تکمیلی/knowledge-core/tools/kg_link_candidates.json"
OUT = "D:/رسانامه تکمیلی/knowledge-core/tools/kg_links.sql"

S_A, S_B = 0.80, 0.72


def link_type(s):
    if s >= S_A:
        return "same_as"
    if s >= S_B:
        return "primary"
    return "related"


cands = json.load(open(CANDS, encoding="utf-8"))
lines = ["-- entity_content_links from kg_link_candidates.json (Phase B)",
         "-- link_type: same_as >= 0.80 | primary >= 0.72 | related < 0.72",
         "START TRANSACTION;"]
n = 0
for o in cands:
    for c in o["candidates"]:
        lt = link_type(c["score"])
        lines.append(
            "INSERT INTO entity_content_links "
            "(entity_id, content_id, link_type, sort_order) "
            f"VALUES ('{c['entity_id']}', '{o['content_id']}', '{lt}', "
            f"{int(round(c['score'] * 100))}) "
            "ON DUPLICATE KEY UPDATE link_type = VALUES(link_type), "
            "sort_order = VALUES(sort_order);")
        n += 1
lines.append("COMMIT;")
open(OUT, "w", encoding="utf-8").write("\n".join(lines) + "\n")

import collections
dist = collections.Counter(link_type(c["score"]) for o in cands for c in o["candidates"])
print(f"rows={n}  {dict(dist)}  -> {OUT}")
