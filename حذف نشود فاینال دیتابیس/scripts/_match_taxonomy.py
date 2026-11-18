# -*- coding: utf-8 -*-
"""
_match_taxonomy.py — dry-run: تطبیق نوع‌آگاه آیتم‌های taxonomy با موجودیت‌های موجود
فقط گزارش؛ هیچ نوشتنی انجام نمی‌دهد.
"""
import json, re, unicodedata
from collections import Counter
from taxonomy_data import ITEMS

DB = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_existing_names.json"

ALEF = {"\u0622":"ا","\u0623":"ا","\u0625":"ا","\u0627":"ا",
        "\u0649":"ی","\u06CC":"ی","\u0643":"ک"}
# کلماتِ «نوع» فقط برای core — مدام و دقیق
TW = {"نظریه","نظریهی","مدل","مدلی","الگو","الگوی"}
FIELD_PREFIX = {"مطالعات","حوزه","علوم"}

def norm(s):
    if not s: return ""
    s = unicodedata.normalize("NFC", s)
    out=[]
    for ch in s:
        if ch in ALEF: out.append(ALEF[ch]); continue
        if ch in " \u200c\u0640\u0600-\u0605\u061c\u00a0\t\n\r-–—.,:;!?()[]{}\"'‘’“”·…/\\|_*#@&%+=<>~^": continue
        out.append(ch.lower())
    return "".join(out)

def _toks(name):
    return [norm(t) for t in name.split() if norm(t)]

def core(name, strip_type=True):
    toks=[t for t in _toks(name) if t]
    if strip_type:
        while len(toks)>1 and toks[0] in TW: toks=toks[1:]
        while len(toks)>1 and toks[-1] in TW: toks=toks[:-1]
    return "".join(toks)

def core2(name):
    """core with an extra leading field-word (مطالعات/حوزه/علوم) optionally removed"""
    toks=[t for t in _toks(name) if t]
    while len(toks)>1 and toks[0] in TW: toks=toks[1:]
    while len(toks)>1 and toks[-1] in TW: toks=toks[:-1]
    if len(toks)>1 and toks[0] in FIELD_PREFIX: toks=toks[1:]
    return "".join(toks)

def tokens(name):
    return set(t for t in _toks(name) if t)

def jaccard(a,b):
    if not a or not b: return 0
    u=len(a|b); return len(a&b)/u if u else 0

def sub_ratio(short, long):
    if not short or not long or len(short)<5: return 0
    if short in long: return len(short)/len(long)
    return 0

ex = json.load(open(DB, encoding="utf-8"))
ex_idx=[]
for e in ex:
    al_raw = e["aliases"]
    if isinstance(al_raw,str):
        al=[norm(a) for a in re.split(r"[,،;؛]", al_raw) if norm(a)]
    elif al_raw: al=[norm(a) for a in al_raw if norm(a)]
    else: al=[]
    ex_idx.append({"code":e["code"],"type":e["type"],"fa":e["fa"],
        "fa_core":core(e["fa"]),"fa_tok":tokens(e["fa"]),"fa_full":norm(e["fa"]),
        "en":norm(e["en"] or ""),"al":al})

def match_core(name, en, e):
    """score for a theory/model/method item vs an existing entity (any type)"""
    A_core=core(name); A_tok=tokens(name); A=norm(name); A_en=norm(en or "")
    s=0.0
    if A_core and A_core==e["fa_core"]: return 1.0
    if A_en and e["en"] and A_en==e["en"]: s=max(s,0.95)
    j=jaccard(A_tok,e["fa_tok"])
    if j>=0.7 and len(A)>=4: s=max(s,0.65+0.35*j)
    r=sub_ratio(A_core,e["fa_core"]) or sub_ratio(e["fa_core"],A_core)
    if r>=0.7: s=max(s,0.78)
    if any(a and (A==a or sub_ratio(A,a)>=0.8 or sub_ratio(a,A)>=0.8) for a in e["al"]): s=max(s,0.88)
    return s

def best_for(item):
    typ=item["type"]; sec=item["sec"]; name=item["name"]; en=item.get("en")
    best=None; bs=0
    for e in ex_idx:
        if sec==3:  # DISCIPLINE / SUBFIELD — only compare domain entities
            if e["type"] not in ("DISCIPLINE","SUBFIELD"): continue
            fA=norm(name); fE=e["fa_full"]
            if fA==fE: s=1.0
            else: s=sub_ratio(core2(name),core2(e["fa"]))*1.0 if False else (0.85 if (fA in fE or fE in fA) and min(len(fA),len(fE))>=8 else 0)
        elif sec==4:  # CONCEPT
            fA=norm(name); fE=e["fa_full"]
            if fA==fE: s=1.0
            elif e["type"]=="CONCEPT": s=match_core(name,en,e)
            else: s=0
        else:  # THEORY / MODEL / METHOD — any type
            s=match_core(name,en,e)
        if s>bs: bs=s; best=e
    return (best,bs) if bs>=0.78 else (None,bs)

# global dedup within taxonomy by normalized name, merge subsections
order=[]; merged={}
for it in ITEMS:
    k=norm(it["name"])
    if k not in merged:
        it2=dict(it); it2["_subs"]=[]; merged[k]=it2; order.append(k)
    merged[k]["_subs"].append((it["sub"],it["sub_fa"]))

matched=[]; newitems=[]
for k in order:
    it=merged[k]
    m,sc=best_for(it)
    if m:
        matched.append({"name":it["name"],"type":it["type"],"sub":it["sub"],
            "mcode":m["code"],"mtype":m["type"],"mfa":m["fa"],"score":round(sc,2)})
    else:
        newitems.append(it)

json.dump({"matched":matched,"new":newitems},
          open(r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_match_report.json","w",encoding="utf-8"),
          ensure_ascii=False,indent=1)

print("=== DRY RUN ===")
print(f"unique items: {len(order)} | matched(skip): {len(matched)} | NEW(add): {len(newitems)}")
print("NEW by type:", dict(Counter(i['type'] for i in newitems)))
print("\n--- MATCHED (attachment -> existing) ---")
for m in sorted(matched,key=lambda x:(x['type'],x['name'])):
    print(f"  [{m['sub']}] {m['name']}  ->  {m['mcode']} ({m['mtype']}) {m['mfa']}  ({m['score']})")
print("\n--- NEW by subsection ---")
c=Counter(i['sub'] for i in newitems)
for sub in sorted(c,key=lambda s:(int(s.split('-')[0]) if s.split('-')[0].isdigit() else 99,s)):
    print(f"  {sub}: {c[sub]}")
