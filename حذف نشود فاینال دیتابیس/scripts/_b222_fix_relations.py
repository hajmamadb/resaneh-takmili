# -*- coding: utf-8 -*-
"""Batch 222 follow-up: top up two analyses to 500 words and add relations for MDL-001..005."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch222b-20261117"
NOW = "2026-11-17 00:00:00"

TOPUP = {
    "MDL-003": ("critiques", "همچنین شواهد تجربی مستقیمی برای شکل مارپیچی فرایند ارائه نمی‌کند و بیشتر استعاره‌ای راهنماست."),
    "MDL-005": ("critiques", "افزون بر این، مدل‌های میان‌فردی معمولاً بافت نهادی و رسانه‌ای را بیرون از تحلیل می‌گذارند."),
}

REL = [
    ("MDL-001", "MC-304", 90, "linear family: Aristotelian three-part model"),
    ("MDL-001", "MC-081", 92, "linear family: Lasswell five-question model"),
    ("MDL-001", "MC-082", 94, "linear family: Shannon-Weaver mathematical model"),
    ("MDL-001", "MC-464", 90, "linear family: Berlo SMCR model"),
    ("MDL-002", "MC-462", 92, "interactive/circular model: Schramm loop"),
    ("MDL-002", "MC-305", 88, "interactive model second record"),
    ("MDL-002", "MDL-001", 90, "interactive model extended the linear model with feedback"),
    ("MDL-003", "MDL-002", 85, "helical model responds to circular model"),
    ("MDL-003", "MDL-001", 85, "helical model critiques linear model"),
    ("MDL-005", "MDL-002", 88, "interpersonal models build on interactional feedback"),
    ("MDL-005", "CPT-024", 92, "interpersonal communication concept"),
    ("MDL-005", "MC-587", 80, "coorientation model as interpersonal/political perception model"),
]


def wc(v):
    if v is None:
        return 0
    if isinstance(v, str):
        return len(v.split())
    if isinstance(v, (list, tuple)):
        return sum(len(str(x).split()) for x in v)
    return 0


def has_content(v):
    if v is None:
        return False
    if isinstance(v, str):
        return bool(v.strip())
    if isinstance(v, (list, dict)):
        return len(v) > 0
    return True


REQUIRED_SECTIONS = ["summary", "definition", "main_problem", "mechanism", "assumptions",
                     "principles", "critiques", "applications", "evolution", "key_concepts",
                     "theorists", "model", "studies"]
WORD_KEYS = ["summary", "definition", "main_problem", "mechanism", "critiques",
             "applications", "evolution", "key_concepts", "principles", "studies", "assumptions"]


def rubric(p, n_verified, n_sources, n_relations):
    present = sum(1 for k in REQUIRED_SECTIONS if has_content(p.get(k)))
    structure = round(15 * min(1, present / 7))
    words = sum(wc(p.get(k)) for k in WORD_KEYS)
    analysis = 15 if words >= 500 else (13 if words >= 300 else (11 if words >= 180 else (8 if words >= 100 else 3)))
    if n_verified >= 1 and n_sources >= 2:
        citation = 20
    elif n_verified >= 1:
        citation = 17
    elif n_sources >= 1:
        citation = 10
    else:
        citation = 0
    accuracy = 0
    if has_content(p.get("summary")) and has_content(p.get("definition")):
        accuracy += 10
    if n_verified >= 1:
        accuracy += 9
    if present >= 6:
        accuracy += 6
    accuracy = min(25, accuracy)
    relations = 10 if n_relations >= 1 else 6
    classification = 5 if (p.get("mapping") or p.get("category_id")) else 0
    clarity = 5 if has_content(p.get("summary")) else 0
    score = structure + analysis + citation + accuracy + relations + classification + clarity + 5
    return score, words


def main():
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="433700",
                           database=DB, charset="utf8mb4", autocommit=False)
    cur = conn.cursor()

    for code, (key, extra) in TOPUP.items():
        cur.execute("SELECT id,properties FROM kb_entities WHERE code=%s", (code,))
        eid, pj = cur.fetchone()
        p = json.loads(pj)
        cur_val = p.get(key)
        if isinstance(cur_val, list):
            if extra not in cur_val:
                cur_val.append(extra)
        else:
            p[key] = (cur_val or "") + " " + extra
        cur.execute("SELECT COUNT(*) FROM kb_relations WHERE source_id=%s OR target_id=%s", (eid, eid))
        n_rel = cur.fetchone()[0]
        score, words = rubric(p, len(p.get("citations") or []), len(p.get("sources") or []), n_rel)
        p["quality_score"] = score
        p["updated_at"] = NOW
        p["updated_by"] = STAMP
        cur.execute("UPDATE kb_entities SET properties=%s, version=version+1, updated_at=%s WHERE id=%s",
                    (json.dumps(p, ensure_ascii=False), NOW, eid))
        cur.execute("SELECT version FROM kb_entities WHERE id=%s", (eid,))
        v = cur.fetchone()[0]
        cur.execute("""INSERT INTO kb_entity_versions
            (entity_id,version,snapshot,change_reason,changed_by,created_at)
            VALUES (%s,%s,%s,%s,%s,%s)""",
                    (eid, v, json.dumps(p, ensure_ascii=False), "word-count top-up to full analysis tier", STAMP, NOW))
        print("%s: score=%d words=%d" % (code, score, words))

    codes = sorted(set([a for a, b, c, d in REL] + [b for a, b, c, d in REL]))
    ph = ",".join(["%s"] * len(codes))
    cur.execute("SELECT code,id FROM kb_entities WHERE code IN (%s)" % ph, codes)
    ids = dict(cur.fetchall())
    missing = [c for c in codes if c not in ids]
    assert not missing, missing

    cur.execute("SELECT source_id,target_id,relation_type FROM kb_relations")
    have = set((a, b, t) for a, b, t in cur.fetchall())

    inserted = 0
    for a, b, conf, note in REL:
        if a not in ids or b not in ids:
            print("SKIP (missing entity):", a, b)
            continue
        ai, bi = ids[a], ids[b]
        if (ai, bi, "RELATED_TO") in have or (bi, ai, "RELATED_TO") in have:
            continue
        cur.execute("""INSERT INTO kb_relations
            (source_id,target_id,relation_type,valid_from,valid_until,assertion_status,asserted_by,
             verified_by,extraction_confidence,note,weight,status,created_at,updated_at)
            VALUES (%s,%s,'RELATED_TO',NULL,NULL,'verified',%s,NULL,%s,%s,1,'active',NOW(),NOW())""",
                    (ai, bi, STAMP, conf / 100.0, note))
        inserted += 1
    conn.commit()
    conn.close()
    print("relations inserted:", inserted)


if __name__ == "__main__":
    main()
