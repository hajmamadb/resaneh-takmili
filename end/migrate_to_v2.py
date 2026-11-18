#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
resaname_h -> resaname_v2  migration
مهاجرت کامل داده‌ها به ساختار ساختاریافته جدید (contents + sections + works + relation_links + chunks)
"""
import json
import os
import pymysql
import sys

HOST = "127.0.0.1"
USER = "root"
PASS = "433700"

src = pymysql.connect(host=HOST, user=USER, password=PASS, database="resaname_h",
                      charset="utf8mb4", cursorclass=pymysql.cursors.DictCursor)
dst = pymysql.connect(host=HOST, user=USER, password=PASS, database="resaname_v2",
                      charset="utf8mb4", autocommit=False, cursorclass=pymysql.cursors.DictCursor)

src_cur = src.cursor()
dst_cur = dst.cursor()

# ---------------------------------------------------------------------------
# 0) Apply refined card classification (from classify_merged.json)
#    If the file exists, override content_type for the 731 card rows.
#    If missing, fall back to the original ai_documents content_type.
# ---------------------------------------------------------------------------
_CLASSIFY_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                              "llm", "classify_merged.json")
if os.path.exists(_CLASSIFY_PATH):
    with open(_CLASSIFY_PATH, "r", encoding="utf-8") as _f:
        _class_map = json.load(_f)  # {"card-1": {"type_key": "model", ...}, ...}
    print(f">>> 0) Applying refined classification to {len(_class_map)} cards ...")
    _n_upd = 0
    for _sid, _cls in _class_map.items():
        _tk = _cls.get("type_key", "")
        if not _tk:
            continue
        dst_cur.execute(
            "UPDATE contents SET content_type=%s WHERE source_type='card' AND source_id=%s",
            (_tk, _sid),
        )
        _n_upd += dst_cur.rowcount
    dst.commit()
    print(f"    {len(_class_map)} cards re-classified ({_n_upd} rows updated)")
else:
    print(f">>> 0) No classify_merged.json found — using original content_type (skipped)")

# ---------------------------------------------------------------------------
# 1) ai_documents -> contents  (تمام 801 مدخل)
#    نگاشت: source_type -> contents.source_type
#            content_type (card: از ai_documents.content_type؛ theorist/theory: همان)
# ---------------------------------------------------------------------------
print(">>> 1) contents از ai_documents ...")
src_cur.execute("SELECT * FROM ai_documents ORDER BY id")
docs = src_cur.fetchall()
content_rows = []
for d in docs:
    st = d["source_type"]           # card | theorist | theory | book | journal | article
    ct = d["content_type"] or st    # theory/model/... ; theorist; book; journal; article
    row = (
        d["id"], st, ct, d["source_id"], d["slug"], d["title"], d["english_title"],
        d["summary"], d["canonical_url"], d["language"] or "fa", d["country"],
        d["origin"], None, None, None, None, None,
        "verified" if d["content_hash"] else "unverified",
        d["content_hash"], d["source_updated_at"], d["indexed_at"],
    )
    content_rows.append(row)
sql = """INSERT IGNORE INTO contents
 (id, source_type, content_type, source_id, slug, title, english_title, summary,
  canonical_url, language, country, origin, nationality, field, year, image_url,
  image_urls, verification_status, content_hash, source_updated_at, indexed_at)
 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
dst_cur.executemany(sql, content_rows)
dst.commit()
print(f"    contents از ai_documents: {len(content_rows)} ردیف")

# ---------------------------------------------------------------------------
# 1b) 39 نظریه‌پرداز اصلی از site.theorists -> contents
#      (در ai_documents ثبت نشده‌اند؛ id=doc-theorist-N)
# ---------------------------------------------------------------------------
print(">>> 1b) contents از theorists site (39) ...")
src_cur.execute("""SELECT id, name, name_en, slug, avatar_url, year, nationality,
                          field, main_theory, bio, academic_career, quote
                   FROM theorists""")
site_theorists = src_cur.fetchall()
th_rows = []
for t in site_theorists:
    cid = f"doc-theorist-{t['id'][len('th-'):]}"
    th_rows.append((
        cid, 'theorist', 'theorist', t["id"], t["slug"], t["name"], t["name_en"],
        t.get("bio"), None, "fa", None, None,
        t["nationality"], t["field"], None, t["avatar_url"], None,
        'verified', None, None, None,
    ))
sql1b = """INSERT IGNORE INTO contents
 (id, source_type, content_type, source_id, slug, title, english_title, summary,
  canonical_url, language, country, origin, nationality, field, year, image_url,
  image_urls, verification_status, content_hash, source_updated_at, indexed_at)
 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
dst_cur.executemany(sql1b, th_rows)
dst.commit()
print(f"    contents از theorists site: {len(th_rows)} ردیف")

# ---------------------------------------------------------------------------
# 2) sections  (از ai_document_sections؛ document_id -> content_id)
# ---------------------------------------------------------------------------
print(">>> 2) sections از ai_document_sections ...")
src_cur.execute("""SELECT s.id, s.document_id, s.section_key, s.section_title,
                          s.content, s.content_hash, s.sort_order
                   FROM ai_document_sections s ORDER BY s.document_id, s.sort_order""")
sec_rows = src_cur.fetchall()
sql2 = """INSERT IGNORE INTO sections
 (id, content_id, section_key, section_title, content, content_hash, sort_order)
 VALUES (%s,%s,%s,%s,%s,%s,%s)"""
dst_cur.executemany(sql2, [(r["id"], r["document_id"], r["section_key"],
                            r["section_title"], r["content"], r["content_hash"],
                            r["sort_order"]) for r in sec_rows])
dst.commit()
print(f"    sections: {len(sec_rows)} ردیف")

# ---------------------------------------------------------------------------
# 3) نظریه‌پردازان: 20 بخش را از فیلدهای موجود بسازیم
#    - 59 از ai_entities (entity_type='theorist')
#    - 39 از site.theorists (bio / academic_career / quote / importance)
#    نگاشت فیلدهای site -> section_key:
#      name           -> identity
#      avatar_url     -> vitals
#      bio            -> short_intro
#      field          -> specialties
#      (nationality/country/year) -> vitals
#      academic_career-> career
#      quote          -> evaluation
#      main_theory    -> theories
# ---------------------------------------------------------------------------
print(">>> 3) بخش‌های نظریه‌پرداز (59) ...")
src_cur.execute("""SELECT id, name, name_en, country, origin, year, nationality,
                          field, main_theory, summary, external_url, verification_status
                   FROM ai_entities WHERE entity_type='theorist'""")
entities = {e["id"]: e for e in src_cur.fetchall()}

# site theorists (bio/career/quote) — id مانند th-1
src_cur.execute("""SELECT id, name, name_en, slug, avatar_url, year, nationality,
                          field, main_theory, bio, academic_career, quote, importance
                   FROM theorists""")
site_th = {t["id"]: t for t in src_cur.fetchall()}

# entity-th-N  <->  site th-N  (N یکسان) ;  entity-th-new-N -> site نیست
def site_of(entity_id: str):
    # entity-th-1 -> th-1 ;  entity-th-new-1 -> None
    if entity_id.startswith("entity-th-new-"):
        return None
    if entity_id.startswith("entity-th-"):
        return entity_id[len("entity-th-"):]
    return None

def make_vitals(e, site):
    parts = []
    if site:
        parts.append(f"نام: {site['name']}")
        if site.get("name_en"): parts.append(f"نام انگلیسی: {site['name_en']}")
        if site.get("year"): parts.append(f"سال: {site['year']}")
        if site.get("nationality"): parts.append(f"ملیت: {site['nationality']}")
        if site.get("avatar_url"): parts.append(f"تصویر: {site['avatar_url']}")
    else:
        parts.append(f"نام: {e['name']}")
        if e.get("name_en"): parts.append(f"نام انگلیسی: {e['name_en']}")
        if e.get("year"): parts.append(f"سال: {e['year']}")
        if e.get("nationality"): parts.append(f"ملیت: {e['nationality']}")
    return "\n".join(parts)

def make_short_intro(e, site):
    # bio (site) غنی‌تر است؛ وگرنه summary (entity)
    if site and site.get("bio"):
        return site["bio"]
    return e.get("summary") or ""

def make_specialties(e, site):
    if site and site.get("field"):
        return site["field"]
    return e.get("field") or ""

def make_career(e, site):
    if site and site.get("academic_career"):
        return site["academic_career"]
    return ""

def make_evaluation(e, site):
    if site and site.get("quote"):
        return f"گزاره:\n{site['quote']}"
    return ""

def make_theories(e, site):
    if site and site.get("main_theory"):
        return site["main_theory"]
    return e.get("main_theory") or ""

def make_network(e):
    # country + origin + external_url
    parts = []
    if e.get("country"): parts.append(f"کشور: {e['country']}")
    if e.get("origin"): parts.append(f"مبدأ: {e['origin']}")
    if e.get("external_url"): parts.append(f"وب‌سایت/پروفایل: {e['external_url']}")
    return "\n".join(parts)

new_sections = []   # (id, content_id, section_key, section_title, content, sort_order, group)
sec_title_map = {
    "identity": ("نام و نام خانوادگی", 1),
    "vitals": ("تصویر و اطلاعات پایه", 1),
    "short_intro": ("معرفی کوتاه", 1),
    "specialties": ("حوزه‌های تخصصی", 1),
    "affiliations": ("وابستگی‌های علمی", 1),
    "education": ("زندگی و تحصیلات", 2),
    "career": ("مسیر حرفه‌ای و دانشگاهی", 2),
    "context": ("زمینه تاریخی و فکری", 2),
    "intellectual_evolution": ("سیر تحول فکری", 2),
    "mentors_students": ("شاگردان و تأثیرگذاران", 2),
    "theories": ("نظریه‌های ارائه‌شده", 3),
    "key_concepts": ("مفاهیم و اصطلاحات کلیدی", 3),
    "works": ("آثار و تألیفات", 3),
    "method": ("روش و رویکرد علمی", 3),
    "legacy": ("تأثیرگذاری و میراث", 3),
    "criticisms": ("نقدهای واردشده", 4),
    "responses": ("پاسخ‌ها و دفاعیات", 4),
    "evaluation": ("جایگاه علمی معاصر", 4),
    "network": ("شبکه ارتباطات علمی", 5),
    "references": ("منابع و مآخذ", 5),
}
order = ["identity","vitals","short_intro","specialties","affiliations",
         "education","career","context","intellectual_evolution","mentors_students",
         "theories","key_concepts","works","method","legacy",
         "criticisms","responses","evaluation","network","references"]

def content_id_of_entity(eid):
    # entity-th-1 -> doc-theorist-1 ;  entity-th-new-1 -> doc-new-theorist-1
    if eid.startswith("entity-th-new-"):
        return "doc-new-theorist-" + eid[len("entity-th-new-"):]
    if eid.startswith("entity-th-"):
        return "doc-theorist-" + eid[len("entity-th-"):]
    return None

# content_id برای 59 نظریه‌پرداز — باید در contents وجود داشته باشد
# بررسی: آیا doc-theorist-N در contents هست؟ (از ai_documents theorist)
# در ai_documents theorist فقط 20 ردیف (doc-new-theorist-1..20) وجود دارد
# یعنی 39 نظریه‌پرداز اصلی (entity-th-1..39) در ai_documents ثبت نکرده‌اند -> باید اضافه شوند
print("    ... 39 نظریه‌پرداز اصلی در ai_documents موجود نیستند؛ اضافه می‌کنم")
src_cur.execute("SELECT COUNT(*) AS c FROM ai_documents WHERE id LIKE 'doc-theorist-%'")
have = src_cur.fetchone()["c"]
if have == 0:
    # 39 نظریه‌پرداز اصلی را به contents اضافه کن (id=doc-theorist-N)
    for eid, e in entities.items():
        if not eid.startswith("entity-th-new-") and eid.startswith("entity-th-"):
            n = eid[len("entity-th-"):]
            cid = f"doc-theorist-{n}"
            # فقط اگر هنوز در contents نیست
            site = site_th.get(n)
            dst_cur.execute("SELECT COUNT(*) AS c FROM contents WHERE id=%s", (cid,))
            if dst_cur.fetchone()["c"] == 0:
                dst_cur.execute("""INSERT IGNORE INTO contents
                 (id, source_type, content_type, source_id, slug, title, english_title,
                  summary, country, origin, nationality, field, year, image_url,
                  verification_status)
                 VALUES (%s,'theorist','theorist',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,'verified')""",
                 (cid, n, e["slug"], e["name"], e["name_en"],
                  e.get("summary") or "", e.get("country"), e.get("origin"),
                  e.get("nationality"), e.get("field"), e.get("year"),
                  (site or {}).get("avatar_url")))
    dst.commit()
    print(f"    ... 39 content جدید برای نظریه‌پردازان اصلی اضافه شد")

# حالا 20 section برای هر 59 نظریه‌پرداز
for eid, e in entities.items():
    cid = content_id_of_entity(eid)
    if not cid:
        continue
    site = site_th.get(site_of(eid)) if not eid.startswith("entity-th-new-") else None
    builders = {
        "identity": e["name"] + (f"\n{e['name_en']}" if e.get("name_en") else ""),
        "vitals": make_vitals(e, site),
        "short_intro": make_short_intro(e, site),
        "specialties": make_specialties(e, site),
        "affiliations": "",
        "education": "",
        "career": make_career(e, site),
        "context": "",
        "intellectual_evolution": "",
        "mentors_students": "",
        "theories": make_theories(e, site),
        "key_concepts": "",
        "works": "",
        "method": "",
        "legacy": "",
        "criticisms": "",
        "responses": "",
        "evaluation": make_evaluation(e, site),
        "network": make_network(e),
        "references": "",
    }
    for i, key in enumerate(order, 1):
        content = builders.get(key, "")
        if not content:
            continue
        title, grp = sec_title_map[key]
        sid = f"sec-th-{eid.replace('entity-','')}-{key}"
        new_sections.append((sid, cid, key, title, content, i, f"group{grp}"))

sql3 = """INSERT IGNORE INTO sections
 (id, content_id, section_key, section_title, content, sort_order, `group`)
 VALUES (%s,%s,%s,%s,%s,%s,%s)"""
dst_cur.executemany(sql3, new_sections)
dst.commit()
print(f"    sections نظریه‌پرداز: {len(new_sections)} ردیف (برای 59 نظریه‌پرداز)")

# ---------------------------------------------------------------------------
# 4) works  (از ai_documents با source_type IN book/article/journal)
# ---------------------------------------------------------------------------
print(">>> 4) works از book/article/journal ...")
src_cur.execute("""SELECT id, source_type, source_id, title, english_title, summary,
                          canonical_url, language, country, origin, content_hash
                   FROM ai_documents
                   WHERE source_type IN ('book','article','journal')""")
work_rows = src_cur.fetchall()
# id برای works: از source_id (book-new-1 / journal-new-N / article-new-N)
sql4 = """INSERT IGNORE INTO works
 (id, work_type, title, title_en, publisher, journal, publication_year, isbn, doi,
  issn, source_url, citation_apa, image_urls, verification_status)
 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
work_vals = []
for w in work_rows:
    work_vals.append((
        w["source_id"], w["source_type"], w["title"], w["english_title"],
        None, None, None, None, None, None, w["canonical_url"],
        w["summary"], None,
        "verified" if w["content_hash"] else "unverified",
    ))
dst_cur.executemany(sql4, work_vals)
dst.commit()
print(f"    works: {len(work_vals)} ردیف")

# ---------------------------------------------------------------------------
# 5) relation_links  (از ai_relationships؛ 4667)
#    target_type='entity'  -> work/concept؟  خیر: entity-theorist -> content (theorist)
#    target_type='document'-> content (card/theory/book/...)
#    در v2 همه target یک content_id هستند (entity-th-N -> doc-theorist-N / doc-new-theorist-N)
# ---------------------------------------------------------------------------
print(">>> 5) relation_links از ai_relationships ...")
src_cur.execute("""SELECT id, source_type, source_id, relationship_type,
                          target_type, target_id, description, confidence,
                          verification_status, extracted_by
                   FROM ai_relationships""")
rels = src_cur.fetchall()

def map_target(ttype, tid):
    """target_id را به content_id (v2) تبدیل کن"""
    if ttype == "document":
        # tid مانند doc-card-1 / doc-new-theory-1 / doc-new-theorist-1 / doc-new-book-1
        # در v2، idِ content همان tid است
        return tid
    if ttype == "entity":
        # tid مانند entity-th-1 / entity-th-new-1
        if tid.startswith("entity-th-new-"):
            return "doc-new-theorist-" + tid[len("entity-th-new-"):]
        if tid.startswith("entity-th-"):
            return "doc-theorist-" + tid[len("entity-th-"):]
        # entity-book-new-N / entity-journal-new-N -> work
        return tid
    return tid

rel_vals = []
for r in rels:
    target_id = map_target(r["target_type"], r["target_id"])
    rel_vals.append((
        r["id"], "content", r["source_id"], r["relationship_type"],
        "content", target_id, r["description"], r["confidence"],
        r["verification_status"], r["extracted_by"],
    ))
sql5 = """INSERT IGNORE INTO relation_links
 (id, source_type, source_id, relationship_type, target_type, target_id,
  description, confidence, verification_status, extracted_by)
 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
dst_cur.executemany(sql5, rel_vals)
dst.commit()
print(f"    relation_links: {len(rel_vals)} ردیف")

# ---------------------------------------------------------------------------
# 6) chunks  (لایه RAG؛ از ai_chunks)
# ---------------------------------------------------------------------------
print(">>> 6) chunks از ai_chunks ...")
src_cur.execute("""SELECT id, document_id, section_id, chunk_index, content,
                          content_hash, token_count, vector_point_id,
                          embedding_model, embedding_version
                   FROM ai_chunks""")
ch_rows = src_cur.fetchall()
sql6 = """INSERT IGNORE INTO chunks
 (id, content_id, section_id, chunk_index, content, content_hash, token_count,
  vector_point_id, embedding_model, embedding_version)
 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
dst_cur.executemany(sql6, [(r["id"], r["document_id"], r["section_id"],
                            r["chunk_index"], r["content"], r["content_hash"],
                            r["token_count"], r["vector_point_id"],
                            r["embedding_model"], r["embedding_version"])
                           for r in ch_rows])
dst.commit()
print(f"    chunks: {len(ch_rows)} ردیف")

# ---------------------------------------------------------------------------
# 7) خلاصه نهایی
# ---------------------------------------------------------------------------
print("\n=== خلاصه نهایی resaname_v2 ===")
for t in ["contents","sections","works","works_authors","relation_links","chunks","concepts","content_concepts","section_catalog"]:
    dst_cur.execute(f"SELECT COUNT(*) AS c FROM {t}")
    print(f"  {t:20s} {dst_cur.fetchone()['c']:8d}")

dst.close()
src.close()
print("\nتمام شد.")
