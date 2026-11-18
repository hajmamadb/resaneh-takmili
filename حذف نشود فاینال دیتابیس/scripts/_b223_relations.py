# -*- coding: utf-8 -*-
"""Batch 223: word top-up for MDL-007/008 + relations."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch223-20261117"

TOPUP = {
    "MDL-007": "در نهایت، مدل همگرا با تأکید بر کیفیت رابطه و اعتماد، تحلیل ارتباط را از شمارش پیام به سنجش فهم مشترک می‌برد.",
    "MDL-008": "در مجموع، مدل بلاغی ارتباط را به کنشی هدفمند در موقعیتی معین بدل می‌کند و داوری مخاطب را معیار اصلی موفقیت می‌شمارد.",
}

REL = [
    ("MDL-006", "MC-548", 80, "نسخهٔ سطح‌خانواده مدل آیینی به رکورد مرجع"),
    ("MDL-007", "MDL-002", 88, "مدل همگرا بر مدل تعاملی و بازخورد استوار است"),
    ("MDL-007", "MDL-003", 84, "همگرایی چرخه‌ای و مارپیچی را به هم پیوند می‌دهد"),
    ("MDL-008", "MDL-001", 85, "مدل بلاغی بدیل اقناعی مدل‌های انتقالی است"),
    ("MDL-008", "MC-026", 86, "جاذبه‌های بلاغی ارسطویی در عصر دیجیتال"),
    ("MDL-009", "MDL-001", 84, "مدل زمینه‌محور محدودیت مدل انتقالی را نشان می‌دهد"),
    ("MDL-009", "MDL-004", 86, "لایهٔ زمینه در مدل بوم‌شناختی ارتباط"),
    ("MDL-010", "MC-135", 90, "سلسله‌مراتب اثرات تبلیغ"),
]

conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="433700",
                       database=DB, charset="utf8mb4", autocommit=False)
try:
    cur = conn.cursor()
    for code, add in TOPUP.items():
        cur.execute("SELECT properties FROM kb_entities WHERE code=%s", (code,))
        row = cur.fetchone()
        p = json.loads(row[0])
        crit = p.get("critiques") or []
        crit.append(add)
        p["critiques"] = crit
        cur.execute("UPDATE kb_entities SET properties=%s, updated_at=NOW(), updated_by=%s WHERE code=%s",
                    (json.dumps(p, ensure_ascii=False), STAMP, code))
        print("topup", code)

    cur.execute("SELECT code FROM kb_entities")
    codes = {r[0] for r in cur.fetchall()}
    cur.execute("SELECT source_id, target_id, relation_type FROM kb_relations")
    have = {(r[0], r[1], r[2]) for r in cur.fetchall()}
    coded = {}
    cur.execute("SELECT id, code FROM kb_entities WHERE code IN (%s)" % ",".join(["%s"] * (len(REL) * 2)),
                tuple([c for a, b, _, _ in REL for c in (a, b)]))
    for i, c in cur.fetchall():
        coded[c] = i

    n = 0
    for a, b, conf, note in REL:
        if a not in coded or b not in coded:
            print("SKIP missing", a, b)
            continue
        A, B = coded[a], coded[b]
        if (A, B, "RELATED_TO") in have or (B, A, "RELATED_TO") in have:
            print("skip dup", a, b)
            continue
        cur.execute("""INSERT INTO kb_relations
            (source_id,target_id,relation_type,valid_from,valid_until,assertion_status,asserted_by,
             verified_by,extraction_confidence,note,weight,status,created_at,updated_at)
            VALUES (%s,%s,'RELATED_TO',NULL,NULL,'verified',%s,NULL,%s,%s,1.0,'active',NOW(),NOW())""",
                    (A, B, STAMP, conf / 100.0, note))
        have.add((A, B, "RELATED_TO"))
        n += 1
    conn.commit()
    print("relations inserted:", n)
finally:
    conn.close()
