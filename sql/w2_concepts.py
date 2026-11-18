# -*- coding: utf-8 -*-
"""
W2 — populate `concepts` + `content_concepts` from 852 contents.

Strategy
--------
1. Seed concepts: one concept per content, named after its title
   (Persian title = name, english_title = name_en). Slugs come from a
   deterministic transliteration of the Persian title, suffixed with the
   content id's numeric tail when needed so the slug is GLOBAL UNIQUE
   (lesson from the old `uq_ke_slug` duplicate bug).
2. Shared umbrella concepts: a fixed lexicon of ~25 media/communication
   themes (social media, public opinion, framing, persuasion, ...).
3. Linking: every content is linked to its own concept + up to 4 umbrella
   concepts whose terms appear in its title / english title / summary /
   section titles (1-5 links per content, own concept first).
4. Idempotent: INSERT ... ON DUPLICATE KEY UPDATE everywhere; safe to re-run.

Writes ONLY to `concepts` and `content_concepts`. Read-only elsewhere.
"""
import hashlib
import re
import unicodedata
import pymysql

DB = dict(host="127.0.0.1", user="root", password="433700",
          database="resaname_v2", charset="utf8mb4")

# ------------------------------------------------------------------ translit
FA_DIGITS = str.maketrans("۰۱۲۳۴۵۶۷۸۹", "0123456789")

FA2EN = {
    "ا": "a", "آ": "a", "ب": "b", "پ": "p", "ت": "t", "ث": "s", "ج": "j",
    "چ": "ch", "ح": "h", "خ": "kh", "د": "d", "ذ": "z", "ر": "r", "ز": "z",
    "س": "s", "ش": "sh", "ص": "s", "ض": "z", "ط": "t", "ظ": "z", "ع": "e",
    "غ": "gh", "ف": "f", "ق": "q", "ک": "k", "گ": "g", "ل": "l", "م": "m",
    "ن": "n", "و": "o", "ه": "e", "ی": "y", "ئ": "e", "ؤ": "o",
    "‌": "",   # ZWNJ
    "ـ": "",   # tatweel
}

def norm_farsi(s):
    if not s:
        return ""
    s = unicodedata.normalize("NFC", s).translate(FA_DIGITS)
    s = s.replace("‌", "").replace("ـ", "")
    s = re.sub(r"[«»\"'()\[\]{}،.\u064b\u064c\u064d\u064e\u064f\u0650:؛;!?؟\u2013\u2014-]", " ", s)
    return s

def translit(name):
    s = norm_farsi(name)
    out = []
    for ch in s:
        if ch in FA2EN:
            out.append(FA2EN[ch])
        elif ch.isascii() and ch.isalnum():
            out.append(ch.lower())
        elif ch == " ":
            out.append("-")
    slug = re.sub(r"-+", "-", "".join(out)).strip("-").lower()
    slug = re.sub(r"[^a-z0-9-]", "", slug)
    return slug[:190] or "x"

def id_tail(cid):
    m = re.search(r"(\d+)$", cid or "")
    return m.group(1) if m else "x"

# --------------------------------------------------------------- umbrellas
# (name, name_en, slug, [case-insensitive match patterns])
UMBRELLAS = [
    ("رسانه‌های اجتماعی", "Social Media", "concept-social-media",
     ["شبکه‌های اجتماعی", "شبکه اجتماعی", "رسانه‌های اجتماعی", "اینستاگرام", "توییتر", "فیس‌بوک", "تلگرام"]),
    ("رسانه‌های دیجیتال", "Digital Media", "concept-digital-media",
     ["رسانه‌های دیجیتال", "رسانه دیجیتال", "فضای مجازی", "فضای سایبری", "پلتفرم‌های دیجیتال"]),
    ("اینترنت", "Internet", "concept-internet",
     ["اینترنت", "وب‌سایت", "وبسایت", "موتور جستجو"]),
    ("افکار عمومی", "Public Opinion", "concept-public-opinion",
     ["افکار عمومی", "نظر عمومی", "نظرخواهی"]),
    ("نظریه رسانه", "Media Theory", "concept-media-theory",
     ["نظریه‌های رسانه", "نظریه رسانه", "نظریه‌های ارتباطات", "نظریه ارتباطات", "نظریه‌پردازی", "پارادایم"]),
    ("ارتباطات جمعی", "Mass Communication", "concept-mass-communication",
     ["ارتباطات جمعی", "ارتباطات عامه", "ارتباطات انبوه"]),
    ("رسانه‌سازی", "Media Framing", "concept-media-framing",
     ["رسانه‌سازی", "کادرسازی", "چارچوب‌بندی", "چارچوب‌سازی", "فریمینگ"]),
    ("پوشش رسانه‌ای", "Media Coverage", "concept-media-coverage",
     ["پوشش رسانه‌ای", "پوشش خبری", "پوشش رسانه"]),
    ("اعتماد به رسانه", "Media Trust", "concept-media-trust",
     ["اعتماد به رسانه", "اعتماد رسانه‌ای", "بی‌اعتمادی به رسانه"]),
    ("خبرگزاری و روزنامه", "News Media", "concept-news-media",
     ["خبرگزاری", "روزنامه", "نشریه", "خبرنامه", "پرتال خبری"]),
    ("رسانه‌های بصری", "Visual Media", "concept-visual-media",
     ["سینما", "تلویزیون", "ویدیو", "مستند", "بازی ویدیویی"]),
    ("اقناع", "Persuasion", "concept-persuasion",
     ["اقناع", "تأثیرگذاری", "تبلیغات", "تبلیغ", "بیانه‌سازی"]),
    ("فرهنگ", "Culture", "concept-culture",
     ["فرهنگ", "مطالعات فرهنگی", "نقد فرهنگی", "فرهنگ عامه"]),
    ("سیاست", "Politics", "concept-politics",
     ["سیاست", "دولت", "انتخابات", "حزب", "مجلس", "قانون اساسی"]),
    ("اقتصاد رسانه", "Media Economics", "concept-media-economics",
     ["اقتصاد سیاسی", "اقتصاد رسانه", "بازار رسانه", "صنایع فرهنگی", "سرمایه‌داری نظارتی"]),
    ("روان‌شناسی رسانه", "Media Psychology", "concept-media-psychology",
     ["روان‌شناسی", "شناختی", "سوگیری", "احساسات", "هیجان", "هوش شناختی"]),
    ("اخلاق رسانه‌ای", "Media Ethics", "concept-media-ethics",
     ["اخلاق رسانه", "اخلاق حرفه‌ای", "کد اخلاق"]),
    ("مخاطب", "Audience", "concept-audience",
     ["مخاطب", "مخاطبان", "تماشاگر", "بازدیدکننده", "کاربران", "بازدیدکنندگان"]),
    ("خبرنگاری", "Journalism", "concept-journalism",
     ["خبرنگار", "روزنامه‌نگاری", "کارشناس خبر"]),
    ("تاریخ رسانه", "Media History", "concept-media-history",
     ["تاریخ رسانه", "تاریخ سینما", "تاریخ خبر", "سوابق تاریخی"]),
    ("روش‌شناسی", "Research Methodology", "concept-research-methodology",
     ["روش‌شناسی", "روش تحقیق", "روش‌های پژوهش", "کمّی", "کیفی", "پیمایش"]),
    ("محتوای تولیدشده توسط کاربر", "User-Generated Content", "concept-user-generated-content",
     ["محتوای تولیدشده", "محتوای ساخته‌شده", "یو‌جی‌سی"]),
    ("هوش مصنوعی", "Artificial Intelligence", "concept-artificial-intelligence",
     ["هوش مصنوعی", "الگوریتم", "یادگیری ماشین", "مدل‌های زبانی"]),
    ("حریم خصوصی", "Privacy", "concept-privacy",
     ["حریم خصوصی", "حریم‌مندی", "اطلاعات شخصی"]),
    ("سواد رسانه‌ای", "Media Literacy", "concept-media-literacy",
     ["سواد رسانه", "سواد رسانه‌ای"]),
]
UMB = [(n, ne, s, [p.lower() for p in pats]) for n, ne, s, pats in UMBRELLAS]

def find_umbrellas(text):
    t = norm_farsi(text).lower()
    hits = {}
    for name, name_en, slug, pats in UMB:
        for p in pats:
            if p in t:
                hits[slug] = hits.get(slug, 0) + 1
                break
    return hits

# -------------------------------------------------------------------- main
def main():
    conn = pymysql.connect(**DB, autocommit=False)
    cur = conn.cursor()

    cur.execute("SELECT id, title, english_title, summary FROM contents ORDER BY id")
    contents = cur.fetchall()
    assert len(contents) == 852, f"expected 852 contents, got {len(contents)}"

    sec_titles = {}
    cur.execute("SELECT content_id, section_title FROM sections "
                "WHERE section_title IS NOT NULL AND section_title<>''")
    for cid, st in cur.fetchall():
        sec_titles.setdefault(cid, []).append(st)

    # ---------- build concept rows: slug -> (id, name, name_en, slug, def)
    concepts = {}
    content_own = {}   # cid -> concept slug (mapped to id later)
    used_slugs = {s for _, _, s, _ in UMB}

    for name, name_en, slug, _ in UMB:
        concepts[slug] = (slug, name, name_en, slug,
                          f"مفهوم کلیدی «{name}» ({name_en}) در حوزه رسانه و ارتباطات.")

    for cid, title, en_title, summary in contents:
        base = translit(title)
        slug = base
        k = 2
        while slug in used_slugs:
            slug = base[:180] + "-" + id_tail(cid) + str(k)
            k += 1
        used_slugs.add(slug)
        cdef = (summary or "").strip() or None
        cen = (en_title or "").strip() or None
        concepts[slug] = (slug, (title or "").strip()[:300],
                          (cen[:300] if cen else None),
                          slug, cdef)
        content_own[cid] = slug

    # concept id: use the slug, but shorten over-long slugs (id is varchar(40))
    def make_id(slug):
        if len(slug) <= 40:
            return slug
        h = hashlib.sha1(slug.encode()).hexdigest()[:6]
        return f"c-{slug[:30]}-{h}"

    id_map = {s: make_id(s) for s in concepts}
    for s in concepts:
        concepts[s] = (id_map[s],) + tuple(concepts[s][1:])
    for row in concepts.values():
        assert len(row[0]) <= 40, f"concept id too long: {row[0]!r}"
    # ensure id uniqueness after shortening
    ids = [r[0] for r in concepts.values()]
    assert len(ids) == len(set(ids)), "concept id collision after shortening"
    for cid in content_own:
        content_own[cid] = id_map[content_own[cid]]
    slug_to_id = {s: id_map[s] for s in concepts}

    # ---------- write concepts
    up_concept = """
    INSERT INTO concepts (id, name, name_en, slug, definition)
    VALUES (%s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
      name = VALUES(name),
      name_en = VALUES(name_en),
      definition = VALUES(definition)
    """
    rows = list(concepts.values())
    B = 500
    for i in range(0, len(rows), B):
        cur.executemany(up_concept, rows[i:i + B])
    conn.commit()

    # ---------- build links
    links = {}
    for cid, title, en_title, summary in contents:
        text = f"{title or ''}\n{en_title or ''}\n{summary or ''}\n" + \
               "\n".join(sec_titles.get(cid, []))
        hits = find_umbrellas(text)
        own = content_own[cid]
        lst = [own]
        for s in sorted(hits, key=lambda x: (-hits[x], x)):
            c = slug_to_id[s]
            if c != own and c not in lst:
                lst.append(c)
            if len(lst) >= 5:
                break
        links[cid] = lst

    up_link = """
    INSERT INTO content_concepts (content_id, concept_id)
    VALUES (%s, %s)
    ON DUPLICATE KEY UPDATE content_id = content_id
    """
    link_rows = [(cid, c) for cid, lst in links.items() for c in lst]
    for i in range(0, len(link_rows), B):
        cur.executemany(up_link, link_rows[i:i + B])
    conn.commit()

    # ---------- verify
    cur.execute("SELECT COUNT(*) FROM concepts")
    n_concepts = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM content_concepts")
    n_links = cur.fetchone()[0]
    cur.execute("SELECT COUNT(DISTINCT concept_id) FROM content_concepts")
    n_dc = cur.fetchone()[0]
    cur.execute("SELECT COUNT(DISTINCT content_id) FROM content_concepts")
    n_covered = cur.fetchone()[0]
    cur.execute("SELECT slug, COUNT(*) c FROM concepts GROUP BY slug HAVING c>1")
    dup = cur.fetchall()
    cur.execute("SELECT id, COUNT(*) c FROM concepts GROUP BY id HAVING c>1")
    dup_id = cur.fetchall()
    cur.execute("SELECT MIN(n) FROM (SELECT COUNT(*) n FROM content_concepts "
                "GROUP BY content_id) t")
    min_links = cur.fetchone()[0]

    print(f"concepts:            {n_concepts}")
    print(f"content_concepts:    {n_links}")
    print(f"distinct concepts:   {n_dc}")
    print(f"contents covered:    {n_covered} / 852")
    print(f"min links/content:   {min_links}")
    print(f"duplicate slugs:     {dup}")
    print(f"duplicate ids:       {dup_id}")

    assert n_concepts >= 100, n_concepts
    assert n_links >= 500, n_links
    assert n_dc >= 50, n_dc
    assert n_covered == 852, n_covered
    assert not dup, dup
    assert not dup_id, dup_id

    conn.close()
    print("OK")

if __name__ == "__main__":
    main()
