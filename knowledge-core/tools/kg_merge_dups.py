# -*- coding: utf-8 -*-
"""Phase C: merge duplicate knowledge_entities into canonical ids (idempotent).
For each (dup, canon) pair, in one transaction:
  1) drop entity_content_links dup-side rows whose (canon, content_id) exists
  2) redirect remaining entity_content_links dup -> canon
  3) for knowledge_relations: drop dup-side rows that would collide with an
     existing canon row (same src/tgt/type), then redirect the rest
  4) delete dup's kg_chunks
  5) delete the dup entity row
Safe to re-run: a dup id that no longer exists makes the whole pair a no-op.
"""
import subprocess

MYSQL = "C:/Program Files/MySQL/MySQL Server 8.0/bin/mysql.exe"
DB = "resaname_v2"

# (duplicate_id, canonical_id)
PAIRS = [
    # 9 research-area pairs
    ("kg-tech-crisis-comm", "kg-technique-tech-crisis-comm"),
    ("kg-tech-development-comm", "kg-technique-tech-development-comm"),
    ("kg-tech-political-comm", "kg-technique-tech-political-comm"),
    ("kg-technique-advertising-research", "kg-technique-tech-advertising"),
    ("kg-technique-audience-research", "kg-technique-tech-audience"),
    ("kg-technique-digital-media-research", "kg-technique-tech-digital-media"),
    ("kg-technique-film-tv-research", "kg-technique-tech-film-tv"),
    ("kg-technique-news-research", "kg-technique-tech-journalism"),
    ("kg-technique-pr-research", "kg-technique-tech-pr"),
    ("kg-technique-social-media-research", "kg-technique-tech-social-media"),
    # 3 family vs bare
    ("kg-design-grounded-theory", "kg-framework-qual-grounded-theory"),
    ("kg-framework-discourse-analysis", "kg-framework-qual-discourse-analysis"),
    ("kg-framework-semiotic-analysis", "kg-framework-qual-semiotic-analysis"),
    # 3 theory pairs
    ("kg-theory-political-agenda", "kg-theory-agenda-setting"),
    ("kg-theory-political-public-sphere", "kg-theory-public-sphere"),
    ("kg-theory-political-spiral", "kg-theory-spiral-silence"),
]


def q(sql):
    r = subprocess.run(
        [MYSQL, "--default-character-set=utf8mb4", "-u", "root", "-p433700",
         DB, "-N", "-B", "-e", sql],
        capture_output=True, text=True, encoding="utf-8")
    if r.returncode != 0:
        raise SystemExit("SQL ERROR: " + r.stderr[:600])
    return r.stdout


def exists(eid):
    out = q(f"SELECT COUNT(*) FROM knowledge_entities WHERE id='{eid}'")
    return out.strip().splitlines()[0].strip() == "1"


for dup, canon in PAIRS:
    if not exists(dup):
        print(f"skip {dup} (already merged)")
        continue
    if not exists(canon):
        print(f"ERROR canon missing: {canon} — skipping {dup}")
        continue
    tx = [
        "START TRANSACTION;",
        # 1) drop dup-side ecl rows that would collide with canon
        f"DELETE e1 FROM entity_content_links e1 "
        f"JOIN entity_content_links e2 "
        f"ON e1.content_id=e2.content_id AND e2.entity_id='{canon}' "
        f"WHERE e1.entity_id='{dup}';",
        # 2) redirect remaining dup ecl -> canon
        f"UPDATE entity_content_links SET entity_id='{canon}' WHERE entity_id='{dup}';",
        # 3a) drop dup-side knowledge_relations rows that collide with a canon row
        f"DELETE kr FROM knowledge_relations kr "
        f"JOIN knowledge_relations kc "
        f"  ON (kr.source_entity_id='{dup}' AND kc.source_entity_id='{canon}' "
        f"      AND kr.target_entity_id=kc.target_entity_id AND kr.relation_type=kc.relation_type) "
        f"  OR (kr.target_entity_id='{dup}' AND kc.target_entity_id='{canon}' "
        f"      AND kr.source_entity_id=kc.source_entity_id AND kr.relation_type=kc.relation_type);",
        # 3b) redirect the rest
        f"UPDATE knowledge_relations SET source_entity_id='{canon}' WHERE source_entity_id='{dup}';",
        f"UPDATE knowledge_relations SET target_entity_id='{canon}' WHERE target_entity_id='{dup}';",
        # 4) delete dup kg_chunks
        f"DELETE FROM kg_chunks WHERE entity_id='{dup}';",
        # 5) delete dup entity
        f"DELETE FROM knowledge_entities WHERE id='{dup}';",
        "COMMIT;",
    ]
    sql = "\n".join(tx)
    r = subprocess.run(
        [MYSQL, "--default-character-set=utf8mb4", "-u", "root", "-p433700",
         DB],
        input=sql, capture_output=True, text=True, encoding="utf-8")
    if r.returncode != 0:
        print(f"ERROR merging {dup}->{canon}: {r.stderr[:400]}")
    else:
        print(f"merged {dup} -> {canon}")

# final counts
print("=== final counts ===")
for label, sql in [
    ("entities", "SELECT COUNT(*) FROM knowledge_entities"),
    ("relations", "SELECT COUNT(*) FROM knowledge_relations"),
    ("links", "SELECT COUNT(*) FROM entity_content_links"),
    ("kg_chunks", "SELECT COUNT(*) FROM kg_chunks"),
]:
    print(f"  {label}: {q(sql).strip()}")
print("  by status:")
for line in q("SELECT verification_status, COUNT(*) FROM knowledge_entities GROUP BY verification_status;").splitlines():
    if line.strip():
        print("   " + line.replace("\t", " / "))
