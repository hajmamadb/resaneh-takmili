"""Dump resaname_v2 to a SQL file + copy supporting files into end/."""
import pymysql
import os
import shutil

END = r"D:\رسانامه تکمیلی\end"
SQL_DIR = r"D:\رسانامه تکمیلی\sql"
OUT = os.path.join(END, "resaname_v2_dump.sql")

os.makedirs(END, exist_ok=True)

conn = pymysql.connect(
    host="127.0.0.1", user="root", password="433700",
    database="resaname_v2", charset="utf8mb4",
)
cur = conn.cursor()

cur.execute("SHOW TABLES")
tables = [r[0] for r in cur.fetchall()]
print("Tables:", tables)

def esc(v):
    if v is None:
        return "NULL"
    if isinstance(v, (int, float)):
        return str(v)
    s = str(v)
    s = s.replace("\\", "\\\\")
    s = s.replace("'", "\\'")
    s = s.replace('"', '\\"')
    s = s.replace("\n", "\\n")
    s = s.replace("\r", "\\r")
    s = s.replace("\t", "\\t")
    return "'" + s + "'"

with open(OUT, "w", encoding="utf-8") as f:
    f.write("-- resaname_v2 dump\n")
    f.write("-- Generated: 2026-11-10\n")
    f.write("USE resaname_v2;\n\n")
    for table in tables:
        cur.execute("SELECT COUNT(*) AS c FROM `" + table + "`")
        count = cur.fetchone()[0]
        f.write("-- Table: " + table + " (" + str(count) + " rows)\n")
        cur.execute("SHOW CREATE TABLE `" + table + "`")
        f.write(cur.fetchone()[1] + ";\n\n")
        cur.execute("SELECT * FROM `" + table + "`")
        rows = cur.fetchall()
        if rows:
            cols = [d[0] for d in cur.description]
            f.write("INSERT INTO `" + table + "` (" + ", ".join("`" + c + "`" for c in cols) + ") VALUES\n")
            f.write(",\n".join("(" + ", ".join(esc(v) for v in row) + ")" for row in rows) + ";\n\n")

conn.close()
print("Dump written:", OUT, os.path.getsize(OUT), "bytes")

# Copy the 8 supporting files
files = [
    "v2_schema.sql",
    "v2_taxonomy.sql",
    "v2_catalog.sql",
    "migrate_to_v2.py",
    "insert_phase4.py",
    "llm/phase4_generated.json",
    "v2_report.md",
    "resaname_vectors.sqlite",
]
for fn in files:
    src = os.path.join(SQL_DIR, fn)
    dst = os.path.join(END, os.path.basename(fn))
    shutil.copy2(src, dst)
    print("Copied:", fn, "->", os.path.basename(dst), os.path.getsize(dst), "bytes")

print("\n=== end/ contents ===")
for name in sorted(os.listdir(END)):
    p = os.path.join(END, name)
    print(f"  {name:40s} {os.path.getsize(p):>14,} bytes")
