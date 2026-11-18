#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
W5 — Phase C: Expert Verification (AUDIT-ONLY / read-only)

Reads the knowledge graph tables in `resaname_v2`:
  - knowledge_entities        (545)
  - knowledge_relations       (1077)
  - knowledge_entity_types    (23)
  - knowledge_relation_types  (20)

and classifies every entity / relation into one of:
    verified | needs_review | error

RULES (deterministic, read-only, no UPDATE/INSERT/DELETE/ALTER anywhere):

Entity:
  error        -> entity_type not in knowledge_entity_types.type_code
                  (or id/slug missing — should never happen on this schema)
  needs_review -> any of:
      * verification_status in {flagged, duplicate}   (prior-work signal)
      * duplicate name (same title_fa as another entity)
      * duplicate english name (same title_en as another entity)
      * title_fa shorter than 3 characters (e.g. "R")
      * abstract length < 40 chars (thin definition)
  verified     -> everything else

Relation:
  error        -> source_entity_id or target_entity_id orphan (no such entity)
                  (or relation_type not in knowledge_relation_types.type_code)
  needs_review -> any of:
      * relation_type == 'RELATED_TO'              (ambiguous / weak link)
      * confidence < 0.80                          (low confidence extraction)
      * source == target (self-loop)
      * description contains a raw 'kg-...' id     (template leakage)
  verified     -> everything else

Outputs (both beside this script's parent dir, i.e. knowledge-core/):
  - phase_c_verification_report.md
  - phase_c_verification_results.json

Only SELECT statements are executed.
"""

import json
import os
import sys
import re
from decimal import Decimal

import pymysql

# --------------------------------------------------------------------------- #
# Config
# --------------------------------------------------------------------------- #
DB = dict(host="127.0.0.1", user="root", password="433700",
          database="resaname_v2", charset="utf8mb4")

HERE = os.path.dirname(os.path.abspath(__file__))          # .../knowledge-core/tools
CORE = os.path.dirname(HERE)                               # .../knowledge-core
REPORT_MD = os.path.join(CORE, "phase_c_verification_report.md")
RESULTS_JSON = os.path.join(CORE, "phase_c_verification_results.json")

# Thresholds
ABSTRACT_MIN = 40          # chars; below -> "thin definition"
TITLE_FA_MIN = 3           # chars; below -> "too short"
CONF_MIN = 0.80            # confidence; below -> low confidence
AMBIGUOUS_REL = "RELATED_TO"
FLAG_STATES = {"flagged", "duplicate"}


# --------------------------------------------------------------------------- #
# DB helpers (SELECT ONLY)
# --------------------------------------------------------------------------- #
def fetch_all(cur, sql, args=None):
    cur.execute(sql, args or ())
    return cur.fetchall()


def load_reference_data(cur):
    """Valid type codes + per-entity type lookup + per-relation type metadata."""
    ent_types = fetch_all(cur,
        "SELECT type_code FROM knowledge_entity_types")
    valid_ent = {r[0] for r in ent_types}

    rel_types = fetch_all(cur,
        "SELECT type_code, is_bidirectional FROM knowledge_relation_types")
    valid_rel = {r[0] for r in rel_types}
    bidir = {r[0] for r in rel_types if r[1]}

    return valid_ent, valid_rel, bidir


def load_entities(cur):
    rows = fetch_all(cur, """
        SELECT id, title_fa, title_en, slug, entity_type, parent_id,
               abstract, verification_status
        FROM knowledge_entities
    """)
    out = []
    for r in rows:
        out.append({
            "id": r[0],
            "title_fa": r[1],
            "title_en": r[2],
            "slug": r[3],
            "entity_type": r[4],
            "parent_id": r[5],
            "abstract": r[6] or "",
            "verification_status": r[7],
        })
    return out


def load_relations(cur):
    rows = fetch_all(cur, """
        SELECT id, source_entity_id, target_entity_id, relation_type,
               description, confidence
        FROM knowledge_relations
    """)
    out = []
    for r in rows:
        out.append({
            "id": r[0],
            "source": r[1],
            "target": r[2],
            "relation_type": r[3],
            "description": r[4] or "",
            "confidence": float(r[5]),
        })
    return out


# --------------------------------------------------------------------------- #
# Verification logic
# --------------------------------------------------------------------------- #
def verify_entities(entities, valid_ent):
    # Build name frequency maps (for duplicate detection)
    fa_count, en_count = {}, {}
    for e in entities:
        if e["title_fa"]:
            fa_count[e["title_fa"]] = fa_count.get(e["title_fa"], 0) + 1
        if e["title_en"]:
            en_count[e["title_en"]] = en_count.get(e["title_en"], 0) + 1

    results = []
    for e in entities:
        problems, suggestions = [], []

        et = e["entity_type"]
        if et not in valid_ent:
            # Hard contradiction: invalid type code
            results.append({**e, "status": "error",
                            "problems": [f"entity_type '{et}' is not a valid "
                                         f"code in knowledge_entity_types"],
                            "suggestions": [f"map '{et}' to a valid type code "
                                            f"or add it to knowledge_entity_types"]})
            continue

        # needs_review checks
        if e["verification_status"] in FLAG_STATES:
            problems.append(f"verification_status='{e['verification_status']}' "
                            f"(prior-work flag)")
            suggestions.append("human re-check of this entity's content/type")

        if fa_count.get(e["title_fa"], 0) > 1:
            problems.append(f"duplicate Persian name '{e['title_fa']}' "
                            f"({fa_count[e['title_fa']]} entities)")
            suggestions.append("merge or rename to disambiguate the duplicate")

        if e["title_en"] and en_count.get(e["title_en"], 0) > 1:
            problems.append(f"duplicate English name '{e['title_en']}' "
                            f"({en_count[e['title_en']]} entities)")
            suggestions.append("merge or rename to disambiguate the duplicate")

        if len(e["title_fa"]) < TITLE_FA_MIN:
            problems.append(f"Persian name too short ('{e['title_fa']}')")
            suggestions.append("expand the name for clarity/uniqueness")

        if len(e["abstract"]) < ABSTRACT_MIN:
            problems.append(f"abstract thin ({len(e['abstract'])} chars < "
                            f"{ABSTRACT_MIN})")
            suggestions.append("enrich the definition/abstract")

        if problems:
            results.append({**e, "status": "needs_review",
                            "problems": problems, "suggestions": suggestions})
        else:
            results.append({**e, "status": "verified",
                            "problems": [], "suggestions": []})

    return results


def verify_relations(relations, valid_rel, entity_ids, bidir):
    results = []
    for r in relations:
        problems, suggestions = [], []

        src, tgt, rt = r["source"], r["target"], r["relation_type"]

        if src not in entity_ids or tgt not in entity_ids:
            missing = []
            if src not in entity_ids:
                missing.append(f"source '{src}'")
            if tgt not in entity_ids:
                missing.append(f"target '{tgt}'")
            results.append({**r, "status": "error",
                            "problems": ["orphan endpoint: " + " and ".join(missing)],
                            "suggestions": ["re-point or remove the dangling "
                                            "endpoint"]})
            continue

        if rt not in valid_rel:
            results.append({**r, "status": "error",
                            "problems": [f"relation_type '{rt}' not in "
                                         f"knowledge_relation_types"],
                            "suggestions": ["map to a valid relation type code"]})
            continue

        # needs_review checks
        if rt == AMBIGUOUS_REL:
            problems.append("relation_type='RELATED_TO' (ambiguous/weak link)")
            suggestions.append("refine to a more specific type "
                               "(IS_A, PART_OF, INFLUENCED_BY, ...)")

        if r["confidence"] < CONF_MIN:
            problems.append(f"low confidence {r['confidence']:.2f} < {CONF_MIN:.2f}")
            suggestions.append("human confirmation of the extraction")

        if src == tgt:
            problems.append("self-loop (source == target)")
            suggestions.append("remove the self-referencing relation")

        if re.search(r"kg-[a-z0-9-]+", r["description"]):
            problems.append("description contains a raw 'kg-...' id "
                            "(template leakage)")
            suggestions.append("rewrite description with the human-readable "
                               "names instead of ids")

        if problems:
            results.append({**r, "status": "needs_review",
                            "problems": problems, "suggestions": suggestions})
        else:
            results.append({**r, "status": "verified",
                            "problems": [], "suggestions": []})

    return results


# --------------------------------------------------------------------------- #
# Aggregation / report
# --------------------------------------------------------------------------- #
def tally(items, key):
    t = {"verified": 0, "needs_review": 0, "error": 0}
    for it in items:
        t[it[key]] += 1
    return t


def by_type_counts(items, type_field):
    agg = {}
    for it in items:
        d = agg.setdefault(it[type_field],
                           {"total": 0, "verified": 0, "needs_review": 0, "error": 0})
        d["total"] += 1
        d[it["status"]] += 1
    return agg


def md_escape(s):
    if s is None:
        return ""
    return str(s).replace("|", "\\|").replace("\n", " ").strip()


def short(s, n=60):
    s = str(s or "")
    return s if len(s) <= n else s[:n] + "…"


def build_report(ent_res, rel_res, ent_by_type, rel_by_type):
    et = tally(ent_res, "status")
    rt = tally(rel_res, "status")

    L = []
    L.append("# Phase C — Expert Verification Report")
    L.append("")
    L.append(f"*Rasaname — دایره‌المعارف فارسی رسانه و ارتباطات · "
             f"knowledge-core (audit-only, read-only)*")
    L.append("")
    L.append("## خلاصه (Summary)")
    L.append("")
    L.append(f"- **Entities:** {et['verified']} verified / "
             f"{et['needs_review']} needs_review / {et['error']} error "
             f"(total {len(ent_res)})")
    L.append(f"- **Relations:** {rt['verified']} verified / "
             f"{rt['needs_review']} needs_review / {rt['error']} error "
             f"(total {len(rel_res)})")
    L.append("")
    L.append("## روش و قواعد (Method & rules)")
    L.append("")
    L.append("این واحد **فقط-خواندنی** است؛ هیچ UPDATE/INSERT/DELETE/ALTER "
             "انجام نشده است. هر entity/relation بر اساس قواعد قطعی زیر "
             "دسته‌بندی می‌شود:")
    L.append("")
    L.append("**Entity — `error`:** entity_type نامعتبر در "
             "`knowledge_entity_types`.")
    L.append("**Entity — `needs_review`:** verification_status قبلی "
             "`flagged`/`duplicate`، نام فارسی تکراری، نام انگلیسی تکراری، "
             "نام فارسی خیلی کوتاه (<3 کاراکتر)، یا abstract ضعیف "
             f"(<{ABSTRACT_MIN} کاراکتر).")
    L.append("**Entity — `verified`:** همه موارد دیگر.")
    L.append("")
    L.append(f"**Relation — `error`:** endpoint یتیم (source/target بدون "
             "entity) یا relation_type نامعتبر.")
    L.append(f"**Relation — `needs_review`:** type مبهم `RELATED_TO`، "
             f"confidence < {CONF_MIN:.2f}، حلقه‌ی خودی (source==target)، یا "
             "description حاوی شناسه‌ی خام `kg-…`.")
    L.append("**Relation — `verified`:** همه موارد دیگر.")
    L.append("")

    # ---- Entities with problems ----
    L.append("## Entities با مشکل (needs_review + error)")
    L.append("")
    ent_problems = [e for e in ent_res if e["status"] != "verified"]
    if ent_problems:
        L.append("| id | name (fa) | name_en | entity_type | status | problem | suggestion |")
        L.append("|---|---|---|---|---|---|---|")
        for e in ent_problems:
            L.append(f"| {md_escape(e['id'])} | {md_escape(e['title_fa'])} | "
                     f"{md_escape(e['title_en'])} | {md_escape(e['entity_type'])} | "
                     f"{e['status']} | {md_escape('; '.join(e['problems']))} | "
                     f"{md_escape('; '.join(e['suggestions']))} |")
    else:
        L.append("_هیچ entity با مشکلی یافت نشد._")
    L.append("")

    # ---- Relations with problems ----
    L.append("## Relations با مشکل (needs_review + error)")
    L.append("")
    rel_problems = [r for r in rel_res if r["status"] != "verified"]
    if rel_problems:
        L.append("| source_id | target_id | relation_type | conf | status | problem | suggestion |")
        L.append("|---|---|---|---|---|---|---|")
        for r in rel_problems:
            L.append(f"| {md_escape(r['source'])} | {md_escape(r['target'])} | "
                     f"{md_escape(r['relation_type'])} | {r['confidence']:.2f} | "
                     f"{r['status']} | {md_escape('; '.join(r['problems']))} | "
                     f"{md_escape('; '.join(r['suggestions']))} |")
    else:
        L.append("_هیچ relation با مشکلی یافت نشد._")
    L.append("")

    # ---- Per entity_type ----
    L.append("## آمار به تفکیک entity_type")
    L.append("")
    L.append("| entity_type | total | verified | needs_review | error |")
    L.append("|---|---|---|---|---|")
    for t in sorted(ent_by_type, key=lambda k: (-ent_by_type[k]["total"], k)):
        d = ent_by_type[t]
        L.append(f"| {t} | {d['total']} | {d['verified']} | "
                 f"{d['needs_review']} | {d['error']} |")
    L.append("")

    # ---- Per relation_type ----
    L.append("## آمار به تفکیک relation_type")
    L.append("")
    L.append("| relation_type | total | verified | needs_review | error |")
    L.append("|---|---|---|---|---|")
    for t in sorted(rel_by_type, key=lambda k: (-rel_by_type[k]["total"], k)):
        d = rel_by_type[t]
        L.append(f"| {t} | {d['total']} | {d['verified']} | "
                 f"{d['needs_review']} | {d['error']} |")
    L.append("")

    # ---- Samples ----
    L.append("## نمونه‌های با مشکل (top samples)")
    L.append("")
    L.append("### ۵ نمونه‌ی entity")
    L.append("")
    samples_ent = ent_problems[:5]
    if samples_ent:
        for e in samples_ent:
            L.append(f"- **{e['id']}** ({e['entity_type']}) — "
                     f"{short(e['title_fa'])} / {short(e['title_en'],30)} → "
                     f"{'; '.join(e['problems'])}")
    else:
        L.append("- _هیچ نمونه‌ای_")
    L.append("")
    L.append("### ۵ نمونه‌ی relation")
    L.append("")
    samples_rel = rel_problems[:5]
    if samples_rel:
        for r in samples_rel:
            L.append(f"- **{r['relation_type']}** {r['source']} → {r['target']} "
                     f"(conf {r['confidence']:.2f}) → "
                     f"{'; '.join(r['problems'])}")
    else:
        L.append("- _هیچ نمونه‌ای_")
    L.append("")

    L.append("---")
    L.append("*تولیدشده توسط `tools/w5_phase_c_audit.py` — read-only audit.*")
    return "\n".join(L) + "\n"


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #
def main():
    conn = pymysql.connect(**DB)
    try:
        cur = conn.cursor()
        valid_ent, valid_rel, bidir = load_reference_data(cur)
        entities = load_entities(cur)
        relations = load_relations(cur)
        entity_ids = {e["id"] for e in entities}
    finally:
        conn.close()

    ent_res = verify_entities(entities, valid_ent)
    rel_res = verify_relations(relations, valid_rel, entity_ids, bidir)

    ent_by_type = by_type_counts(ent_res, "entity_type")
    rel_by_type = by_type_counts(rel_res, "relation_type")

    # Write report
    with open(REPORT_MD, "w", encoding="utf-8") as f:
        f.write(build_report(ent_res, rel_res, ent_by_type, rel_by_type))

    # Write JSON (strip big text fields for readability)
    def slim(e, keep_text=False):
        d = {k: e[k] for k in ("id", "title_fa", "title_en", "entity_type",
                               "parent_id", "verification_status", "status",
                               "problems", "suggestions")}
        return d

    payload = {
        "audit": "W5 Phase C — Expert Verification (read-only)",
        "database": "resaname_v2",
        "totals": {
            "entities": tally(ent_res, "status"),
            "relations": tally(rel_res, "status"),
            "entity_count": len(ent_res),
            "relation_count": len(rel_res),
        },
        "by_entity_type": ent_by_type,
        "by_relation_type": rel_by_type,
        "entities_with_problems": [slim(e) for e in ent_res
                                   if e["status"] != "verified"],
        "relations_with_problems": [
            {k: r[k] for k in ("id", "source", "target", "relation_type",
                               "confidence", "status", "problems", "suggestions")}
            for r in rel_res if r["status"] != "verified"],
        "verified_entities": [e["id"] for e in ent_res if e["status"] == "verified"],
        "verified_relations": [r["id"] for r in rel_res if r["status"] == "verified"],
    }
    with open(RESULTS_JSON, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    # Console summary
    t = payload["totals"]
    print(f"Entities  : {t['entities']['verified']} verified / "
          f"{t['entities']['needs_review']} needs_review / "
          f"{t['entities']['error']} error  (total {t['entity_count']})")
    print(f"Relations : {t['relations']['verified']} verified / "
          f"{t['relations']['needs_review']} needs_review / "
          f"{t['relations']['error']} error  (total {t['relation_count']})")
    print(f"Report    : {REPORT_MD}")
    print(f"JSON      : {RESULTS_JSON}")


if __name__ == "__main__":
    main()
