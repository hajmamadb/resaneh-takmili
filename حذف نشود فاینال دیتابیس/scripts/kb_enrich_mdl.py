# -*- coding: utf-8 -*-
"""Enrich the 79 MODEL stubs (MDL-001..079). Idempotent, transactional, backup + audit."""
import pymysql, json
from kb_mdl_data_1 import MDL1
from kb_mdl_data_2 import MDL2

DB = "resaname_kb_final_inspect"
STAMP = "qoder-enrich-mdl-20261116"
NOW = "2026-11-16 00:00:00"
DATA = {}
for d in (MDL1, MDL2): DATA.update(d)

def build(old, d):
    p = dict(old)
    p.update({
        "card_type": "مدل",
        "title_fa": d["fa"],
        "title_en": d["en"],
        "macro_domain": "مدل‌های ارتباطات و رسانه",
        "field": {"family": "مدل", "subarea": d["sub"], "application": "مطالعات ارتباطات و رسانه"},
        "year": d.get("year"),
        "level": "میانی",
        "summary": d["summary"],
        "main_problem": d["problem"],
        "approach": d["logic"],
        "core_logic": d["logic"],
        "key_concepts": [{"term_fa": c[0], "term_en": c[1], "definition": c[2]} for c in d["components"]],
        "components": [{"term_fa": c[0], "term_en": c[1], "definition": c[2]} for c in d["components"]],
        "assumptions": d["assume"],
        "example": d["example"],
        "applications": d["app"],
        "related": [{"name": r[0], "relation": r[1]} for r in d["related"]],
        "critique": d["limit"],
        "critiques": d["limit"],
        "limitation": d["limit"],
        "research_guide": d["guide"],
        "sources": [{"citation": s[0], "language": s[1]} for s in d["sources"]],
        "recommended_sources": d["sources"][0][0] if d["sources"] else None,
        "tags": d["tags"],
        "detailed_analysis": d["detail"],
        "theorists": [{"role": "بنیان‌گذار مدل", "name_fa": t} for t in (d.get("theo") or [])],
        "theorists_text": "، ".join(d.get("theo") or []) if d.get("theo") else "میان‌رشته‌ای / بدون بنیان‌گذار واحد",
        "mapping": {"entity_type": "MODEL", "content_type": "مدل (Model)",
                     "taxonomy_section": d.get("sec", "2"), "needs_review": False},
        "status": "enriched",
        "quality_score": d["qs"],
        "needs_enrichment": False,
        "enriched_at": NOW,
        "enriched_by": STAMP,
    })
    return p

def main():
    c = pymysql.connect(host="127.0.0.1", user="root", password="433700",
                        database=DB, charset="utf8mb4", autocommit=False)
    cur = c.cursor()
    cur.execute("SELECT code, canonical_name_fa, canonical_name_en, properties FROM kb_entities WHERE code LIKE 'MDL-%' ORDER BY code")
    rows = cur.fetchall()
    with open(r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_mdl_before_enrich.json", "w", encoding="utf-8") as f:
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
                    (code, "MODEL_ENRICH", json.dumps({"quality_score": d["qs"], "en": d["en"]}, ensure_ascii=False), STAMP))
        updated += 1
    c.commit()
    print("updated models:", updated, "/", len(DATA))
    c.close()
    print("ENRICH MDL DONE")

if __name__ == "__main__":
    main()
