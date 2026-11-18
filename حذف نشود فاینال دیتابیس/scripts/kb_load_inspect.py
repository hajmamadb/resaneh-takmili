import pymysql, re, json

SQL_FILE = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\final_database.sql"
SRC_DB = "resaname_kb_final"
DST_DB = "resaname_kb_final_inspect"

def split_statements(sql):
    stmts=[]; buf=[]; i=0; n=len(sql); in_str=False
    while i < n:
        ch=sql[i]
        if in_str:
            buf.append(ch)
            if ch=="'":
                if i+1<n and sql[i+1]=="'":
                    buf.append("'"); i+=2; continue
                in_str=False
            i+=1; continue
        else:
            if ch=="'":
                in_str=True; buf.append(ch); i+=1; continue
            if ch=='-' and i+1<n and sql[i+1]=='-':
                while i<n and sql[i]!='\n': i+=1
                continue
            if ch==';':
                s=''.join(buf).strip()
                if s: stmts.append(s)
                buf=[]; i+=1; continue
            buf.append(ch); i+=1; continue
    s=''.join(buf).strip()
    if s: stmts.append(s)
    return stmts

sql = open(SQL_FILE, encoding='utf-8').read()
sql = sql.replace(SRC_DB, DST_DB)
stmts = split_statements(sql)
print("statements:", len(stmts))

root = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='433700',
                       charset='utf8mb4', autocommit=True)
cur = root.cursor()
for idx, s in enumerate(stmts):
    head = s[:60].replace('\n', ' ')
    try:
        cur.execute(s)
        while cur.nextset(): pass
    except Exception as e:
        print(f"ERROR stmt#{idx}: {head} -> {e}")
        break
root.close()

c = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='433700',
                    database=DST_DB, charset='utf8mb4', autocommit=True)
cur = c.cursor()
def cnt(t):
    cur.execute(f"SELECT COUNT(*) FROM {t}"); return cur.fetchone()[0]
print(json.dumps({
    "families": cnt("kb_entity_families"),
    "entity_types": cnt("kb_entity_types"),
    "relation_types": cnt("kb_relation_types"),
    "facet_dimensions": cnt("kb_facet_dimensions"),
    "facet_values": cnt("kb_facet_values"),
    "entities": cnt("kb_entities"),
    "relations": cnt("kb_relations"),
    "entity_facets": cnt("kb_entity_facets"),
    "entity_links": cnt("kb_entity_links"),
    "sources": cnt("kb_sources"),
}, ensure_ascii=False, indent=2))
c.close()
