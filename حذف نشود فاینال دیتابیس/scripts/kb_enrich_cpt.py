# -*- coding: utf-8 -*-
"""Enrich the 302 CONCEPT stubs (CPT-001..302). Idempotent, transactional, backup + audit."""
import pymysql, json, importlib, pkgutil

DB = "resaname_kb_final_inspect"
STAMP = "qoder-enrich-cpt-20261116"
NOW = "2026-11-16 00:00:00"

DATA = {}
for i in range(1, 20):
    try:
        mod = importlib.import_module(f"kb_cpt_data_{i}")
        for name in dir(mod):
            if name.startswith("CPT"):
                DATA.update(getattr(mod, name))
    except ImportError:
        break

def build(old, d):
    p = dict(old)
    p.update({
        "card_type": "مفهوم",
        "title_fa": d["fa"],
        "title_en": d["en"],
        "macro_domain": "مفاهیم کلیدی ارتباطات و رسانه",
        "field": {"family": "مفهوم", "subarea": d["sub"], "application": "مطالعات ارتباطات و رسانه"},
        "definition": d["summary"],
        "summary": d["summary"],
        "essence": d["essence"],
        "key_facets": [{"term_fa": c[0], "term_en": c[1], "definition": c[2]} for c in d["elements"]],
        "context": d["context"],
        "example": d["example"],
        "related": [{"name": r[0], "relation": r[1]} for r in d["related"]],
        "boundary": d["boundary"],
        "research_guide": d["guide"],
        "sources": [{"citation": s[0], "language": s[1]} for s in d["sources"]],
        "recommended_sources": d["sources"][0][0] if d["sources"] else None,
        "tags": d["tags"],
        "detailed_analysis": d["detail"],
        "theorists": [{"role": "نظریه‌پرداز کلیدی", "name_fa": t} for t in (d.get("theo") or [])],
        "theorists_text": "، ".join(d.get("theo") or []) if d.get("theo") else "مفهوم میان‌رشته‌ای",
        "mapping": {"entity_type": "CONCEPT", "content_type": "مفهوم (Concept)",
                     "taxonomy_section": d.get("sec", "4"), "needs_review": False},
        "status": "enriched",
        "quality_score": d["qs"],
        "needs_enrichment": False,
        "enriched_at": NOW,
        "enriched_by": STAMP,
    })
    return p

def main():
    print("loaded concept data:", len(DATA))
    c = pymysql.connect(host="127.0.0.1", user="root", password="433700",
                        database=DB, charset="utf8mb4", autocommit=False)
    cur = c.cursor()
    cur.execute("SELECT code, canonical_name_fa, canonical_name_en, properties FROM kb_entities WHERE code LIKE 'CPT-%' ORDER BY code")
    rows = cur.fetchall()
    with open(r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_cpt_before_enrich.json", "w", encoding="utf-8") as f:
        json.dump([{"code": r[0], "fa": r[1], "en": r[2], "props": json.loads(r[3])} for r in rows], f, ensure_ascii=False, indent=1)
    print("backup ->", len(rows), "rows")
    codes = [r[0] for r in rows]
    missing = [k for k in DATA if k not in codes]
    if missing: print("WARN not in DB:", missing)
    updated = 0
    for code, fa, en, pr in rows:
        if code not in DATA: continue
        d = DATA[code]
        props = build(json.loads(pr), d)
        cur.execute("""UPDATE kb_entities SET canonical_name_en=%s, properties=%s,
                       status_workflow='draft', status_scientific='unassessed',
                       version=version+1, updated_at=%s, updated_by=%s WHERE code=%s""",
                    (d["en"], json.dumps(props, ensure_ascii=False), NOW, STAMP, code))
        cur.execute("INSERT INTO kb_audit_log (entity_code, action, detail, source) VALUES (%s,%s,%s,%s)",
                    (code, "CONCEPT_ENRICH", json.dumps({"quality_score": d["qs"], "en": d["en"]}, ensure_ascii=False), STAMP))
        updated += 1
    c.commit()
    print("updated concepts:", updated, "/", len(DATA))
    c.close()
    print("ENRICH CPT DONE")

if __name__ == "__main__":
    main()
