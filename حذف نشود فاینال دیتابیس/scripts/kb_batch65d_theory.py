# -*- coding: utf-8 -*-
"""Touch-up batch 65d: MC-302 `related_approaches` and `recommended_sources` still carry
generic communication-model boilerplate (and a non-existent "Lasswell 1948 book"). Replace
with Shannon-specific, web-verified anchors: Cover & Thomas 2006 (Wiley) and MacKay 2003 (CUP)."""
import pymysql, json

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch65d-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch65d_theory.json"
CODE = "MC-302"

RELATED = ("نظریهٔ کدگذاری کانال (Channel Coding Theory)؛ سیبرنتیک (Wiener) و مفهوم بازخورد؛ "
           "نظریهٔ پیام‌ها و سطوح سه‌گانهٔ شانون-ویور (فنی/معنایی/اثربخشی)؛ نظریهٔ پیچیدگی و آنتروپی در علم اطلاعات؛ "
           "نظریهٔ سیستم‌های عمومی (BERTALANFFY) به‌عنوان چارچوب کلان؛ مدل لاسول به‌عنوان نقطهٔ مقایسه در سنت انتقالی؛ "
           "نظریهٔ انتقالی و نقد آن در مطالعات ارتباطات")

SOURCES = ("Cover, T. M., & Thomas, J. A. (2006). Elements of Information Theory (2nd ed.). Wiley-Interscience. ISBN 978-0-471-24195-9؛ "
           "MacKay, D. J. C. (2003). Information Theory, Inference, and Learning Algorithms. Cambridge University Press. ISBN 978-0-521-64298-9؛ "
           "Shannon, C. E. (1948). A Mathematical Theory of Communication. Bell System Technical Journal, 27(3), 379-423؛ "
           "Shannon, C. E., & Weaver, W. (1949). The Mathematical Theory of Communication. University of Illinois Press.")

def main():
    c = pymysql.connect(host="127.0.0.1", user="root", password="433700", database=DB, charset="utf8mb4", autocommit=False)
    cur = c.cursor()
    cur.execute("SELECT id, properties FROM kb_entities WHERE code=%s", (CODE,))
    eid, pr = cur.fetchone()
    p = json.loads(pr)
    with open(BACKUP, "w", encoding="utf-8") as f:
        json.dump([{"code": CODE, "related_approaches": p.get("related_approaches"), "recommended_sources": p.get("recommended_sources")}], f, ensure_ascii=False, indent=1)
    p["related_approaches"] = RELATED
    p["recommended_sources"] = SOURCES
    p["updated_at"] = NOW; p["updated_by"] = STAMP
    cur.execute("UPDATE kb_entities SET properties=%s, version=version+1, updated_at=%s, updated_by=%s WHERE id=%s",
                (json.dumps(p, ensure_ascii=False), NOW, STAMP, eid))
    cur.execute("INSERT INTO kb_audit_log (entity_code, action, detail, source) VALUES (%s,%s,%s,%s)",
                (CODE, "DOC_ENRICH", json.dumps({"fix": "related_approaches + recommended_sources replaced (boilerplate + non-existent Lasswell 1948 book)", "anchors": ["Cover & Thomas 2006", "MacKay 2003", "Shannon 1948", "Shannon & Weaver 1949"]}, ensure_ascii=False), STAMP))
    c.commit(); c.close()
    print(f"{CODE}: related_approaches + recommended_sources rewritten")
    print("BATCH65d THEORY DONE")

if __name__ == "__main__":
    main()
