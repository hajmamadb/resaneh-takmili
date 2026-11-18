# -*- coding: utf-8 -*-
"""Generate a dated SQL block for the 55 gap-fix summary chunks (Phase 6f)
and append it to sql/chunks-55-gapfix.sql + resaname_h.sql (persistence model)."""
import subprocess

MYSQL = ['C:/Program Files/MySQL/MySQL Server 8.0/bin/mysql.exe', '--default-character-set=utf8mb4',
         '-u', 'root', '-p433700', 'resaname_h', '-N', '-B']

def q(sql):
    r = subprocess.run(MYSQL + ['-e', sql], capture_output=True, text=True, encoding='utf-8')
    if r.returncode != 0:
        raise SystemExit(f"DB ERROR: {r.stderr[:500]}")
    return r.stdout

def esc(s):
    return (s.replace('\\', '\\\\').replace("'", "''")
             .replace('\n', '\\n').replace('\r', '\\r').replace('\t', '\\t'))

out = q(
    "SELECT id, document_id, IFNULL(section_id,''), chunk_index, content, content_hash, "
    "token_count, IFNULL(vector_point_id,''), IFNULL(embedding_model,''), IFNULL(embedding_version,'') "
    "FROM ai_chunks WHERE id LIKE 'ch-doc-new-theorist-%' OR id LIKE 'ch-doc-new-book-%' "
    "OR id LIKE 'ch-doc-new-journal-%' ORDER BY id;")

rows = []
for line in out.splitlines():
    parts = line.split('\t')
    if len(parts) >= 10:
        rows.append(tuple(parts))
assert len(rows) == 55, f"expected 55 rows, got {len(rows)}"

header = """-- ============================================================================
-- RESANAME AI — فاز 6f: رفع خلأ ۵۵ سند بدون section (20 theorist + 20 book + 15 journal)
-- تاریخ: 2026-11-09 | 55 ردیف ai_chunks (chunk summary، section_id=NULL)
-- این بلوک پس از seed-phase4-70-items.sql اجرا می‌شود. (idempotent: INSERT IGNORE)
-- ============================================================================
"""
stmts = []
for (cid, doc, sec, idx, content, chash, tok, pid, model, ver) in rows:
    sec_sql = "NULL" if sec == "" else f"'{esc(sec)}'"
    stmts.append(
        f"INSERT IGNORE INTO `ai_chunks` (`id`, `document_id`, `section_id`, `chunk_index`, "
        f"`content`, `content_hash`, `token_count`, `vector_point_id`, `embedding_model`, `embedding_version`) VALUES "
        f"('{esc(cid)}', '{esc(doc)}', {sec_sql}, {int(idx)}, '{esc(content)}', '{esc(chash)}', {int(tok)}, "
        f"'{esc(pid)}', '{esc(model)}', '{esc(ver)}');")

body = header + "\n".join(stmts) + "\n"
open("chunks-55-gapfix.sql", "w", encoding="utf-8").write(body)

# append to resaname_h.sql as a dated block
with open(r"..\resaname_h.sql", "a", encoding="utf-8") as f:
    f.write("\n" + header + "\n".join(stmts) + "\n")
print(f"wrote chunks-55-gapfix.sql ({len(stmts)} INSERTs) + appended block to resaname_h.sql")
