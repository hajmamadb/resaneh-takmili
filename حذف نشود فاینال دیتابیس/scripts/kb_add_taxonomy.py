# -*- coding: utf-8 -*-
"""
kb_add_taxonomy.py — افزودن آیتم‌های ناقصِ طبقه‌بندیِ پیوست به resaname_kb_final_inspect
- فقط «افزودن» موجودیت جدید؛ هیچ موجودیتِ موجودی تغییر نمی‌کند
- موجودیت‌های موجود (از طریق تطبیق نام) تکراری اضافه نمی‌شوند
- هر آیتم با نوعِ درست + family + دسته‌بندی (properties.taxonomy) + نظریه‌پرداز/تکنیک ثبت می‌شود
- idempotent: با اجرای مجدد، ردیف‌های taxonomy_seed قبلی پاک و دوباره ساخته می‌شوند
- بکاپ/مانیفست + لاگ آدیت
"""
import pymysql, json, re, unicodedata
from collections import Counter
from taxonomy_data import ITEMS, S1, S2, S3, S4, S5

HOST, PORT = '127.0.0.1', 3306
ROOT_PW = '433700'
DB = 'resaname_kb_final_inspect'
BASE = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس"
STAMP = 'taxonomy_seed_20261115'
NOW = '2026-11-15 00:00:00'

FAMILY = {'THEORY':'KNOWLEDGE_STRUCTURE','MODEL':'KNOWLEDGE_STRUCTURE','CONCEPT':'KNOWLEDGE_STRUCTURE',
          'DISCIPLINE':'SCIENTIFIC_DOMAIN','SUBFIELD':'SCIENTIFIC_DOMAIN','METHOD':'RESEARCH_METHODOLOGY'}
PFX = {'THEORY':'TX','MODEL':'MDL','CONCEPT':'CPT','DISCIPLINE':'DSC','SUBFIELD':'SFL','METHOD':'MTH'}
SECT = {1:S1,2:S2,3:S3,4:S4,5:S5}
ITEM_FA = {'THEORY':'نظریه','MODEL':'مدل','CONCEPT':'مفهوم','DISCIPLINE':'حوزه/قلمرو','SUBFIELD':'زیرحوزه','METHOD':'روش'}
# override: مواردی که تطبیق‌شان اشتباه بود و باید «جدید» بمانند
FORCE_NEW = {"مدل پلتفرمی"}

# ---------- normalization / matching (same as dry-run) ----------
ALEF = {"\u0622":"ا","\u0623":"ا","\u0625":"ا","\u0627":"ا","\u0649":"ی","\u06CC":"ی","\u0643":"ک"}
TW = {"نظریه","نظریهی","مدل","مدلی","الگو","الگوی"}
FIELD_PREFIX = {"مطالعات","حوزه","علوم"}
def norm(s):
    if not s: return ""
    s = unicodedata.normalize("NFC", s); out=[]
    for ch in s:
        if ch in ALEF: out.append(ALEF[ch]); continue
        if ch in " \u200c\u0640\u0600-\u0605\u061c\u00a0\t\n\r-–—.,:;!?()[]{}\"'‘’“”·…/\\|_*#@&%+=<>~^": continue
        out.append(ch.lower())
    return "".join(out)
def _toks(n): return [norm(t) for t in n.split() if norm(t)]
def core(n, strip=True):
    t=[x for x in _toks(n) if x]
    if strip:
        while len(t)>1 and t[0] in TW: t=t[1:]
        while len(t)>1 and t[-1] in TW: t=t[:-1]
    return "".join(t)
def core2(n):
    t=[x for x in _toks(n) if x]
    while len(t)>1 and t[0] in TW: t=t[1:]
    while len(t)>1 and t[-1] in TW: t=t[:-1]
    if len(t)>1 and t[0] in FIELD_PREFIX: t=t[1:]
    return "".join(t)
def toks(n): return set(x for x in _toks(n) if x)
def jaccard(a,b):
    u=len(a|b); return len(a&b)/u if u else 0
def sub_ratio(s,l):
    if not s or not l or len(s)<5: return 0
    return len(s)/len(l) if s in l else 0
def load_ex():
    ex=[]
    for e in json.load(open(BASE+r"\_existing_names.json", encoding="utf-8")):
        al=e["aliases"]
        if isinstance(al,str): al=[norm(a) for a in re.split(r"[,،;؛]",al) if norm(a)]
        elif al: al=[norm(a) for a in al if norm(a)]
        else: al=[]
        ex.append({"type":e["type"],"fa":e["fa"],"fa_core":core(e["fa"]),"fa_tok":toks(e["fa"]),
                   "fa_full":norm(e["fa"]),"en":norm(e["en"] or ""),"al":al})
    return ex
def match_core(name,en,e):
    Ac=core(name); At=toks(name); A=norm(name); Ae=norm(en or ""); s=0.0
    if Ac and Ac==e["fa_core"]: return 1.0
    if Ae and e["en"] and Ae==e["en"]: s=max(s,0.95)
    j=jaccard(At,e["fa_tok"]); 
    if j>=0.7 and len(A)>=4: s=max(s,0.65+0.35*j)
    r=sub_ratio(Ac,e["fa_core"]) or sub_ratio(e["fa_core"],Ac)
    if r>=0.7: s=max(s,0.78)
    if any(a and (A==a or sub_ratio(A,a)>=0.8 or sub_ratio(a,A)>=0.8) for a in e["al"]): s=max(s,0.88)
    return s
def best_for(item, ex):
    sec=item["sec"]; name=item["name"]; en=item.get("en"); best=None; bs=0
    for e in ex:
        if sec==3:
            if e["type"] not in ("DISCIPLINE","SUBFIELD"): continue
            fA=norm(name); fE=e["fa_full"]
            s=1.0 if fA==fE else (0.85 if (fA in fE or fE in fA) and min(len(fA),len(fE))>=8 else 0)
        elif sec==4:
            fA=norm(name); fE=e["fa_full"]
            s=1.0 if fA==fE else (match_core(name,en,e) if e["type"]=="CONCEPT" else 0)
        else:
            s=match_core(name,en,e)
        if s>bs: bs=s; best=e
    return (best,bs) if bs>=0.78 else (None,bs)

def main(dry=False):
    ex = load_ex()
    # global in-list dedup + merge subsections
    order=[]; merged={}
    for it in ITEMS:
        k=norm(it["name"])
        if k not in merged:
            it2=dict(it); it2["_subs"]=[]; merged[k]=it2; order.append(k)
        merged[k]["_subs"].append((it["sub"],it["sub_fa"]))
    newitems=[]
    for k in order:
        it=merged[k]
        if it["name"] in FORCE_NEW:
            newitems.append(it); continue
        m,sc=best_for(it, ex)
        if not m: newitems.append(it)
    print("NEW to add:", len(newitems), dict(Counter(i['type'] for i in newitems)))

    # assign codes per type
    counters=Counter()
    rows=[]; manifest=[]
    for it in newitems:
        t=it["type"]; counters[t]+=1; n=counters[t]
        code=f"{PFX[t]}-{n:03d}"
        name=it["name"]
        subs=it.get("_subs",[(it["sub"],it["sub_fa"])])
        props={
            "taxonomy":{"section":str(it["sec"]),"section_fa":SECT[it["sec"]],
                        "subsection":it["sub"],"subsection_fa":it["sub_fa"],"item_type_fa":ITEM_FA[t]},
            "all_subsections":[[a,b] for a,b in subs] if len(subs)>1 else None,
            "name_core_fa": core(name),
            "status":"taxonomy_seed","needs_enrichment":True,
            "source":{"origin":"taxonomy_attachment","file":"taxonomy-20261115.txt","section":it["sub"]},
            "created_via":STAMP,"quality_score":None,"priority_90plus":False,
        }
        if it.get("who"): props["theorists_fa"]=it["who"]
        if it.get("tech"): props["techniques_fa"]=it["tech"]
        if it.get("desc"): props["description_fa"]=it["desc"]
        en=it.get("en")
        if en: props["en_name"]=en
        rows.append((code,t,FAMILY[t],name,en or None,f"{PFX[t].lower()}-{n:03d}",
            None,None,None,'fa',json.dumps(props,ensure_ascii=False),
            'draft','unassessed','active','public',1,None,NOW,STAMP,NOW,STAMP,None,None))
        manifest.append({"code":code,"type":t,"name":name,"sub":it["sub"],"en":en})

    if dry:
        for m in manifest[:8]: print("  ",m)
        print("  ... (dry run, no writes)")
        return

    c = pymysql.connect(host=HOST, port=PORT, user='root', password=ROOT_PW, database=DB,
                        charset='utf8mb4', autocommit=False)
    cur=c.cursor()
    # idempotency: remove my previous taxonomy_seed rows (only my prefixes)
    likes=" OR ".join([f"code LIKE %s" for _ in PFX.values()])
    ph=tuple(f"{p}-%" for p in PFX.values())
    cur.execute(f"DELETE FROM kb_entities WHERE {likes}", ph)
    print("removed prior taxonomy rows:", cur.rowcount)

    cur.executemany("""
        INSERT INTO kb_entities
        (code, entity_type, family_code, canonical_name_fa, canonical_name_en, slug,
         aliases, original_name, original_language, language, properties,
         status_workflow, status_scientific, status_lifecycle, visibility, version,
         external_identifiers, created_at, created_by, updated_at, updated_by,
         verified_at, verified_by)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """, rows)
    print("inserted:", len(rows))

    # audit: one row per added entity
    aud=[(m['code'],'TAXONOMY_ADD',json.dumps({"type":m["type"],"subsection":m["sub"],
            "name":m["name"]},ensure_ascii=False),STAMP,NOW) for m in manifest]
    cur.executemany("INSERT INTO kb_audit_log (entity_code,action,detail,source,created_at) VALUES (%s,%s,%s,%s,%s)", aud)
    c.commit()

    # verify
    cur.execute("SELECT entity_type,COUNT(*) FROM kb_entities WHERE code LIKE 'TX-%' OR code LIKE 'MDL-%' OR code LIKE 'CPT-%' OR code LIKE 'DSC-%' OR code LIKE 'SFL-%' OR code LIKE 'MTH-%' GROUP BY entity_type ORDER BY 2 DESC")
    print("\nadded by type:")
    for t,n in cur.fetchall(): print(f"  {t}: {n}")
    cur.execute("SELECT COUNT(*) FROM kb_entities"); print("total entities now:", cur.fetchone()[0])
    json.dump(manifest, open(BASE+r"\_taxonomy_added.json","w",encoding="utf-8"), ensure_ascii=False, indent=1)
    print("manifest -> _taxonomy_added.json")
    c.close(); print("DONE — committed.")

if __name__ == "__main__":
    import sys
    main(dry=("--dry" in sys.argv))
