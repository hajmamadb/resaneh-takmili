import pymysql, re, json

SQL_FILE = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\final_database.sql"

def split_statements(sql):
    """Split SQL into statements, respecting single-quoted strings and -- line comments."""
    stmts=[]; buf=[]; i=0; n=len(sql); in_str=False
    while i < n:
        ch=sql[i]
        if in_str:
            buf.append(ch)
            if ch=="'":
                # check escaped ''
                if i+1<n and sql[i+1]=="'":
                    buf.append("'"); i+=2; continue
                in_str=False
            i+=1; continue
        else:
            if ch=="'":
                in_str=True; buf.append(ch); i+=1; continue
            if ch=='-' and i+1<n and sql[i+1]=='-':
                # line comment: skip to end of line
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

sql=open(SQL_FILE, encoding='utf-8').read()
stmts=split_statements(sql)
print("statements:", len(stmts))

root=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='433700',
                     charset='utf8mb4',autocommit=True)
cur=root.cursor()
errors=[]
for idx,s in enumerate(stmts):
    head=s[:60].replace('\n',' ')
    try:
        cur.execute(s)
        # drain any extra results
        while cur.nextset(): pass
    except Exception as e:
        errors.append((idx, head, str(e)))
        print(f"ERROR stmt#{idx}: {head} -> {e}")
        break
root.close()

# verify
c=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='433700',
                  database='resaname_kb_final',charset='utf8mb4',autocommit=True)
cur=c.cursor()
cur.execute("SHOW TABLES"); tables=[r[0] for r in cur.fetchall()]
def cnt(t):
    cur.execute(f"SELECT COUNT(*) FROM {t}"); return cur.fetchone()[0]
summary={
  "tables": tables,
  "families": cnt("kb_entity_families"),
  "entity_types": cnt("kb_entity_types"),
  "relation_types": cnt("kb_relation_types"),
  "facet_dimensions": cnt("kb_facet_dimensions"),
  "facet_values": cnt("kb_facet_values"),
  "entities": cnt("kb_entities"),
  "relations": cnt("kb_relations"),
  "entity_facets": cnt("kb_entity_facets"),
}
c.close()
summary["errors"]=errors
print(json.dumps(summary, ensure_ascii=False, indent=2))
