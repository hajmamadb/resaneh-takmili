#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
inج فاز ۴: ثبت محتوای phase4_generated.json در resaname_v2
- تکمیل ۱۴ بخش خالی ۲۰ نظریه‌پرداز موجود
- ثبت ۵ نظریه‌پرداز جدید ایرانی (th-new-21..25) + ۲۰ بخش
- تکمیل ۱۶ بخش خالی ۱۵ نظریه موجود
- ثبت بخش‌های معرفی ۱۵ مجله موجود + ۵ مجله جدید
- ثبت بخش‌های معرفی ۲۰ کتاب/مقاله موجود + ۲ کتاب جدید
- ثبت works + contents برای مجلات/کتاب‌های جدید
"""
import json
import os
import pymysql

HOST = "127.0.0.1"
USER = "root"
PASS = "433700"

BASE = os.path.dirname(os.path.abspath(__file__))
GEN_PATH = os.path.join(BASE, "llm", "phase4_generated.json")
ADD_PATH = os.path.join(BASE, "llm", "phase4_additions.json")

with open(GEN_PATH, "r", encoding="utf-8") as f:
    GEN = json.load(f)
with open(ADD_PATH, "r", encoding="utf-8") as f:
    ADD = json.load(f)

# نگاشت (id -> key -> {sort_order, group}) از gen_input برای بخش‌های خالی
INP_PATH = os.path.join(BASE, "llm", "phase4_gen_input.json")
with open(INP_PATH, "r", encoding="utf-8") as f:
    INP = json.load(f)
T_SO = {t["id"]: {m["key"]: m for m in t["missing_sections"]} for t in INP["theorists"]}
TH_SO = {th["id"]: {m["key"]: m for m in th["missing_sections"]} for th in INP["theories"]}

# نگاشت 20 کلید کاتالوگ نظریه‌پرداز (برای نظریه‌پردازان جدید th-new-21..25)
T_ALL = {m["key"]: m for m in INP["theorists"][0]["missing_sections"]}
# کلیدهای موجود ۶گانه نظریه‌پرداز (از pattern idها در DB)
T_EXISTING = {"identity": 1, "vitals": 2, "short_intro": 3, "specialties": 4,
              "theories": 11, "network": 19}
# ترتیب نمایشی بخش‌های مجله و اثر (section_catalog برای این تایپ‌ها وجود ندارد)
J_ORDER = {"short_intro": 1, "publisher": 2, "scope": 3, "frequency": 4,
           "references": 5}
B_ORDER = {"short_intro": 1, "publisher": 2, "year": 3, "references": 4}

conn = pymysql.connect(
    host=HOST, user=USER, password=PASS, database="resaname_v2",
    charset="utf8mb4", autocommit=False, cursorclass=pymysql.cursors.DictCursor,
)
cur = conn.cursor()

# ---------------------------------------------------------------------------
# کمکی: title بخش از section_catalog (اگر موجود بود) وگرنه از خود کلید
# ---------------------------------------------------------------------------
def get_section_title(content_type: str, key: str) -> str:
    cur.execute(
        "SELECT section_title FROM section_catalog WHERE content_type=%s AND section_key=%s",
        (content_type, key),
    )
    row = cur.fetchone()
    return row["section_title"] if row else key

# نگاشت group از sort_order (مطابق منطق migrate_to_v2.py)
def group_of(sort_order: int) -> str:
    if sort_order <= 4:
        return "group1"
    if sort_order <= 10:
        return "group2"
    if sort_order <= 15:
        return "group3"
    if sort_order <= 18:
        return "group4"
    return "group5"

# ---------------------------------------------------------------------------
# ۱) تکمیل بخش‌های خالی ۲۰ نظریه‌پرداز موجود
# ---------------------------------------------------------------------------
print(">>> 1) تکمیل بخش‌های خالی ۲۰ نظریه‌پرداز ...")
sec_rows = []
for t in GEN["theorist_fill"]:
    content_id = t["content_id"]
    source_id = t["id"]  # e.g. th-new-1
    so_map = T_SO.get(source_id, {})
    for key, text in t["sections"].items():
        if not text or not text.strip():
            continue
        sid = f"sec-th-{source_id}-{key}"
        title = get_section_title("theorist", key)
        m = so_map.get(key)
        so = m["sort_order"] if m else 100
        grp = m["group"] if m else "group3"
        sec_rows.append((sid, content_id, key, title, text.strip(), None, so, grp))
cur.executemany(
    "INSERT IGNORE INTO sections (id, content_id, section_key, section_title, content, content_hash, sort_order, `group`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
    sec_rows,
)
conn.commit()
print(f"    sections نظریه‌پرداز: {len(sec_rows)} ردیف")

# ---------------------------------------------------------------------------
# ۲) ثبت ۵ نظریه‌پرداز جدید ایرانی (th-new-21..25)
# ---------------------------------------------------------------------------
print(">>> 2) ثبت ۵ نظریه‌پرداز جدید ایرانی ...")
new_th_contents = []
new_th_sections = []
for nt in GEN["new_theorists"]:
    meta = nt["meta"]
    cid = nt["content_id"]  # doc-new-theorist-21..25
    new_th_contents.append((
        cid, meta["source_id"], meta.get("slug"), meta["title"],
        meta.get("english_title"), meta.get("summary", ""),
        "fa", meta.get("country"), meta.get("origin"),
        meta.get("nationality"), meta.get("field"),
    ))
    for key, text in nt["sections"].items():
        if not text or not text.strip():
            continue
        sid = f"sec-th-{meta['source_id']}-{key}"
        title = get_section_title("theorist", key)
        so = T_EXISTING.get(key) or T_ALL.get(key, {}).get("sort_order", 100)
        grp = T_ALL.get(key, {}).get("group") or (
            "group1" if (so or 0) <= 4 else "group2" if (so or 0) <= 10
            else "group3" if (so or 0) <= 15 else "group4" if (so or 0) <= 18 else "group5")
        new_th_sections.append((sid, cid, key, title, text.strip(), None, so, grp))

# contents rows (INSERT IGNORE)
if new_th_contents:
    cur.executemany(
        """INSERT IGNORE INTO contents
        (id, source_type, content_type, source_id, slug, title, english_title,
         summary, language, country, origin, nationality, field, verification_status)
        VALUES (%s,'theorist','theorist',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,'unverified')""",
        new_th_contents,
    )
conn.commit()
print(f"    contents نظریه‌پردازان جدید: {len(new_th_contents)}")

if new_th_sections:
    cur.executemany(
        "INSERT IGNORE INTO sections (id, content_id, section_key, section_title, content, content_hash, sort_order, `group`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
        new_th_sections,
    )
conn.commit()
print(f"    new theorist sections: {len(new_th_sections)} ردیف")

# ---------------------------------------------------------------------------
# ۳) تکمیل بخش‌های خالی ۱۵ نظریه موجود
# ---------------------------------------------------------------------------
print(">>> 3) تکمیل بخش‌های خالی ۱۵ نظریه ...")
# Existing theory sections use non-catalog keys (definition/theoretical_framework/
# applications/references) with sort_orders 1,2,4,10. New catalog keys have
# sort_orders 1..18 in gen_input — using them as-is would collide with the
# existing IDs (sec-new-theory-N-{1,2,4,10}). So we offset by +10 (11..28),
# preserving catalog relative order and group mapping.
th_sec_rows = []
for th in GEN["theory_fill"]:
    source_id = th["id"]  # e.g. new-theory-1
    content_id = th["content_id"]
    so_map = TH_SO.get(source_id, {})
    for key, text in th["sections"].items():
        if not text or not text.strip():
            continue
        m = so_map.get(key)
        base = m["sort_order"] if m else 100
        so = base + 10
        sid = f"sec-{source_id}-{so}"
        title = get_section_title("theory", key)
        grp = m["group"] if m else group_of(so)
        th_sec_rows.append((sid, content_id, key, title, text.strip(), None, so, grp))
if th_sec_rows:
    cur.executemany(
        "INSERT IGNORE INTO sections (id, content_id, section_key, section_title, content, content_hash, sort_order, `group`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
        th_sec_rows,
    )
conn.commit()
print(f"    sections نظریه: {len(th_sec_rows)} ردیف")

# ---------------------------------------------------------------------------
# ۴) مجلات: موجود (۱۵) + جدید (۵)
# ---------------------------------------------------------------------------
print(">>> 4) مجلات ...")

# 4a) مجلات موجود — فقط sections (works + contents already exist)
j_existing_rows = []
for j in GEN["journals"]["existing"]:
    content_id = j["content_id"]
    work_id = j["id"]  # journal-new-N
    for key, text in j["sections"].items():
        if not text or not text.strip():
            continue
        sid = f"sec-w-{work_id}-{key}"
        j_existing_rows.append((sid, content_id, key, key, text.strip(), None, J_ORDER.get(key, 100), "group1"))
if j_existing_rows:
    cur.executemany(
        "INSERT IGNORE INTO sections (id, content_id, section_key, section_title, content, content_hash, sort_order, `group`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
        j_existing_rows,
    )
conn.commit()
print(f"    sections مجلات موجود: {len(j_existing_rows)} ردیف")

# 4b) مجلات جدید — works + contents + sections
j_new_rows_works = []
j_new_rows_contents = []
j_new_rows_sections = []
for j in GEN["journals"]["new"]:
    meta = j["meta"]
    work_id = j["id"]  # journal-new-16..20
    cid = j["content_id"]  # doc-new-journal-16..20
    # works row
    cur.execute("SELECT COUNT(*) AS c FROM works WHERE id=%s", (work_id,))
    if cur.fetchone()["c"] == 0:
        j_new_rows_works.append((
            work_id, "journal", meta.get("title"), meta.get("title_en"),
            meta.get("publisher"), None, meta.get("publication_year"),
            None, None, meta.get("issn"), None,
            meta.get("citation_apa"), None, "unverified",
        ))
    # contents row
    cur.execute("SELECT COUNT(*) AS c FROM contents WHERE id=%s", (cid,))
    if cur.fetchone()["c"] == 0:
        j_new_rows_contents.append((
            cid, "journal", "journal", work_id,
            work_id, meta.get("title"), meta.get("title_en"),
            meta.get("citation_apa"), None, "fa", None, None,
            None, None, None, None, None, "unverified", None, None, None,
        ))
    # sections
    for key, text in j["sections"].items():
        if not text or not text.strip():
            continue
        sid = f"sec-w-{work_id}-{key}"
        j_new_rows_sections.append((sid, cid, key, key, text.strip(), None, J_ORDER.get(key, 100), "group1"))

if j_new_rows_works:
    cur.executemany(
        """INSERT IGNORE INTO works
        (id, work_type, title, title_en, publisher, journal, publication_year,
         isbn, doi, issn, source_url, citation_apa, image_urls, verification_status)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
        j_new_rows_works,
    )
if j_new_rows_contents:
    cur.executemany(
        """INSERT IGNORE INTO contents
        (id, source_type, content_type, source_id, slug, title, english_title,
         summary, canonical_url, language, country, origin, nationality, field,
         year, image_url, image_urls, verification_status, content_hash,
         source_updated_at, indexed_at)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
        j_new_rows_contents,
    )
if j_new_rows_sections:
    cur.executemany(
        "INSERT IGNORE INTO sections (id, content_id, section_key, section_title, content, content_hash, sort_order, `group`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
        j_new_rows_sections,
    )
conn.commit()
print(f"    works مجلات جدید: {len(j_new_rows_works)}")
print(f"    contents مجلات جدید: {len(j_new_rows_contents)}")
print(f"    sections مجلات جدید: {len(j_new_rows_sections)} ردیف")

# ---------------------------------------------------------------------------
# ۵) آثار: کتاب/مقاله موجود (۲۰) + کتاب جدید (۲)
# ---------------------------------------------------------------------------
print(">>> 5) آثار ...")

# 5a) آثار موجود — فقط sections
w_existing_rows = []
for w in GEN["works"]["existing"]:
    content_id = w["content_id"]
    work_id = w["id"]  # book-new-N / article via book-new-N
    for key, text in w["sections"].items():
        if not text or not text.strip():
            continue
        sid = f"sec-w-{work_id}-{key}"
        w_existing_rows.append((sid, content_id, key, key, text.strip(), None, B_ORDER.get(key, 100), "group1"))
if w_existing_rows:
    cur.executemany(
        "INSERT IGNORE INTO sections (id, content_id, section_key, section_title, content, content_hash, sort_order, `group`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
        w_existing_rows,
    )
conn.commit()
print(f"    sections آثار موجود: {len(w_existing_rows)} ردیف")

# 5b) کتاب‌های جدید — works + contents + sections
b_new_rows_works = []
b_new_rows_contents = []
b_new_rows_sections = []
for b in GEN["works"]["new_books"]:
    meta = b["meta"]
    work_id = b["id"]  # book-new-21..22
    cid = b["content_id"]  # doc-new-book-21..22
    cur.execute("SELECT COUNT(*) AS c FROM works WHERE id=%s", (work_id,))
    if cur.fetchone()["c"] == 0:
        b_new_rows_works.append((
            work_id, "book", meta.get("title"), meta.get("title_en"),
            meta.get("publisher"), None, meta.get("publication_year"),
            meta.get("isbn"), None, None, None,
            meta.get("citation_apa"), None, "unverified",
        ))
    cur.execute("SELECT COUNT(*) AS c FROM contents WHERE id=%s", (cid,))
    if cur.fetchone()["c"] == 0:
        b_new_rows_contents.append((
            cid, "book", "book", work_id,
            work_id, meta.get("title"), meta.get("title_en"),
            meta.get("citation_apa"), None, "fa", None, None,
            None, None, None, None, None, "unverified", None, None, None,
        ))
    for key, text in b["sections"].items():
        text = str(text) if text is not None else ""
        if not text or not text.strip():
            continue
        sid = f"sec-w-{work_id}-{key}"
        b_new_rows_sections.append((sid, cid, key, key, text.strip(), None, B_ORDER.get(key, 100), "group1"))

if b_new_rows_works:
    cur.executemany(
        """INSERT IGNORE INTO works
        (id, work_type, title, title_en, publisher, journal, publication_year,
         isbn, doi, issn, source_url, citation_apa, image_urls, verification_status)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
        b_new_rows_works,
    )
if b_new_rows_contents:
    cur.executemany(
        """INSERT IGNORE INTO contents
        (id, source_type, content_type, source_id, slug, title, english_title,
         summary, canonical_url, language, country, origin, nationality, field,
         year, image_url, image_urls, verification_status, content_hash,
         source_updated_at, indexed_at)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
        b_new_rows_contents,
    )
if b_new_rows_sections:
    cur.executemany(
        "INSERT IGNORE INTO sections (id, content_id, section_key, section_title, content, content_hash, sort_order, `group`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
        b_new_rows_sections,
    )
conn.commit()
print(f"    works کتاب‌های جدید: {len(b_new_rows_works)}")
print(f"    contents کتاب‌های جدید: {len(b_new_rows_contents)}")
print(f"    sections کتاب‌های جدید: {len(b_new_rows_sections)} ردیف")

# ---------------------------------------------------------------------------
# ۶) خلاصه نهایی
# ---------------------------------------------------------------------------
print("\n=== خلاصه نهایی resaname_v2 ===")
for t in ["contents", "sections", "works", "works_authors", "relation_links", "chunks"]:
    cur.execute(f"SELECT COUNT(*) AS c FROM {t}")
    print(f"  {t:20s} {cur.fetchone()['c']:8d}")

# تفکیک sections بر اساس content_type
print("\n=== تفکیک sections بر اساس نوع ===")
cur.execute("""
    SELECT c.content_type, COUNT(s.id) AS cnt
    FROM sections s JOIN contents c ON s.content_id = c.id
    GROUP BY c.content_type ORDER BY cnt DESC
""")
for r in cur.fetchall():
    print(f"  {r['content_type']:20s} {r['cnt']:8d}")

# تأیید نظریه‌پردازان جدید
print("\n=== نظریه‌پردازان جدید (th-new-21..25) ===")
cur.execute("""
    SELECT c.id, c.title, COUNT(s.id) AS sec_count
    FROM contents c LEFT JOIN sections s ON s.content_id = c.id
    WHERE c.source_id IN ('th-new-21','th-new-22','th-new-23','th-new-24','th-new-25')
    GROUP BY c.id, c.title
""")
for r in cur.fetchall():
    print(f"  {r['id']:25s} {r['title']:30s} sections={r['sec_count']}")

conn.close()
print("\nتمام شد.")
