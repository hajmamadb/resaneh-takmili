# -*- coding: utf-8 -*-
"""Regenerate load_chunks.sql from vectors.json using ijson streaming."""
import ijson, hashlib

print("streaming vectors.json...", flush=True)
MODEL = "Qwen3-Embedding-4B"
sql = ['-- Phase 6: ai_chunks upsert', 'USE resaname_h;', 'SET FOREIGN_KEY_CHECKS=0;', '']

def q(s):
    return s.replace('\\', '\\\\').replace("'", "''")

n = 0
with open('vectors.json', 'rb') as f:
    for p in ijson.items(f, 'item'):
        pid = p['point_id']
        pl = p['payload']
        doc = pl['document_id']
        sec = pl['section_id']
        content = pl['content']
        tok = pl['token_count']
        h = hashlib.sha256(content.encode('utf-8')).hexdigest()
        sec_sql = "NULL" if sec is None else f"'{q(sec)}'"
        sql.append(
            f"INSERT INTO ai_chunks (id, document_id, section_id, chunk_index, content, "
            f"content_hash, token_count, vector_point_id, embedding_model, embedding_version) "
            f"VALUES ('{q(pid)}', '{q(doc)}', {sec_sql}, {pl['chunk_index']}, "
            f"'{q(content)}', '{h}', {tok}, '{q(pid)}', '{MODEL}', '1') "
            f"ON DUPLICATE KEY UPDATE content_hash='{h}', token_count={tok}, "
            f"vector_point_id='{q(pid)}', embedding_model='{MODEL}', embedding_version='1';")
        n += 1
        if n % 2000 == 0:
            print(f"  {n} rows", flush=True)

sql += ['', 'SET FOREIGN_KEY_CHECKS=1;', '-- verify: SELECT COUNT(*) FROM ai_chunks;']
open('load_chunks.sql', 'w', encoding='utf-8', newline='').write('\n'.join(sql))
print(f"wrote load_chunks.sql: {n} rows", flush=True)
print("DONE", flush=True)
