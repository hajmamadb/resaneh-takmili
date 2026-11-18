# -*- coding: utf-8 -*-
"""W3 — Phase B: وصل کردن 467 contentِ بی‌link به knowledge_entities

الگوریتم (دeterministic، idempotent):
  1. exact match  -> link_type='same_as'
     (مطابقت دقیق normalized title fa یا en با title_fa/title_en entity)
  2. token-overlap (الگوریتم gen_resolve_input.py) روی سه سطح:
       s_en  : overlap(content.english_title, entity.title_en)
       s_fa  : content FA-core-tokens در entity FA-core-tokens (نسبت به اندازه entity)
       s_sum : entity FA-core-tokens در summary content (نسبت به اندازه entity)
       s = max(s_en, s_fa, s_sum)
       s >= 0.60 -> 'primary'
       0.45 <= s < 0.60 -> 'related'
       s < 0.45 -> رها
  3. هر content حداکثر 5 entity لینک می‌شود (best-first)
  4. INSERT ... ON DUPLICATE KEY UPDATE — فقط entity_content_links نوشته می‌شود.

اجرا: python w3_phase_b_links.py
"""
import re
import sys
import collections
import pymysql

THRESHOLD_HIGH = 0.60   # primary
THRESHOLD_MED = 0.45    # related
MAX_LINKS = 5

DB = dict(host="127.0.0.1", user="root", password="433700",
          database="resaname_v2", charset="utf8mb4")

# کلمات پرکاربرد فارسی که سیگنال مفهومی ندارند (برای s_fa / s_sum)
FA_STOP = {"و", "های", "در", "از", "به", "با", "ای", "ی", "رسانه", "مدل",
           "نظریه", "نظریه‌", "چارچوب", "تحلیل", "مطالعه", "مطالعات",
           "پژوهش", "پدیده", "مفهوم", "فناور", "روش", "کاربرد", "بافتار",
           "برای", "یک", "این", "آن", "که", "است", "شد", "شده", "درباره",
           "فناوری", "تک", "دو", "سه", "چهار", "پنج"}


def normalize(s):
    if not s:
        return ""
    s = s.lower().strip().rstrip(".").strip()
    s = s.replace("\u200c", " ")
    s = re.sub(r"\s+", " ", s)
    return s


def tokens(s):
    return set(re.findall(r"[a-z0-9]+", s)) | set(re.findall(r"[\u0600-\u06FF]+", s))


def fa_core(s):
    """tokens فارسی با حذف stopwords و تک‌حرفی‌ها"""
    return {t for t in tokens(s) if t not in FA_STOP and len(t) > 2}


def overlap(a, b):
    if not a or not b:
        return 0.0
    return len(a & b) / max(len(a), 1)


def main():
    conn = pymysql.connect(**DB)
    cur = conn.cursor()

    cur.execute("SELECT id, title_fa, IFNULL(title_en,'') FROM knowledge_entities")
    ents = cur.fetchall()

    cur.execute("SELECT id, content_type, title, IFNULL(english_title,''), "
                "IFNULL(summary,'') FROM contents")
    contents = cur.fetchall()

    cur.execute("SELECT content_id, entity_id, link_type FROM entity_content_links")
    existing = {}   # content_id -> {entity_id: link_type}
    for cid, eid, lt in cur.fetchall():
        existing.setdefault(cid, {})[eid] = lt

    # --- prepare entity side ---------------------------------------------------
    ent_norm, ent_tok = {}, {}
    ent_by_fa, ent_by_en = {}, {}
    for eid, fa, en in ents:
        f, e = normalize(fa), normalize(en)
        ent_norm[eid] = (f, e)
        ent_tok[eid] = (fa_core(f), tokens(e))
        if f:
            ent_by_fa.setdefault(f, []).append(eid)
        if e:
            ent_by_en.setdefault(e, []).append(eid)

    # --- score every content ----------------------------------------------------
    rows = []          # (content_id, entity_id, link_type, score)
    exact = 0
    lt_counter = collections.Counter()
    no_match = []
    newly_covered = 0

    for cid, ctype, fa, en, summ in contents:
        already = existing.get(cid, {})
        f, e = normalize(fa), normalize(en)
        st = fa_core(normalize(summ))
        ftc = fa_core(f)
        et = tokens(e)

        cands = {}  # entity_id -> (score, link_type)
        # 1) exact
        for src, idx in ((f, ent_by_fa), (e, ent_by_en)):
            if src:
                for eid in idx.get(src, []):
                    cands[eid] = (1.0, "same_as")
        if any(lt == "same_as" for _, lt in cands.values()):
            exact += 1

        # 2) token overlap
        for eid, (ef, ee) in ent_norm.items():
            if eid in already or eid in cands:
                continue
            eft, eet = ent_tok[eid]
            s = max(
                overlap(et, eet),
                (len(ftc & eft) / max(len(eft), 1)) if (ftc and eft) else 0.0,
                (len(eft & st) / max(len(eft), 1)) if (eft and st) else 0.0,
            )
            if s >= THRESHOLD_HIGH:
                lt = "primary"
            elif s >= THRESHOLD_MED:
                lt = "related"
            else:
                continue
            if eid not in cands or s > cands[eid][0]:
                cands[eid] = (s, lt)

        # 3) cap at MAX_LINKS (counting pre-existing links)
        ranked = sorted(cands.items(), key=lambda kv: (-kv[1][0], kv[0]))
        slots = MAX_LINKS - len(already)
        if slots <= 0:
            continue
        picked = ranked[:slots]
        if not already and not cands:
            no_match.append((cid, ctype, fa, en))
            continue
        if not already:
            newly_covered += 1
        for eid, (s, lt) in picked:
            rows.append((cid, eid, lt, s))
            lt_counter[lt] += 1

    # --- apply ------------------------------------------------------------------
    sql = ("INSERT INTO entity_content_links (entity_id, content_id, link_type) "
           "VALUES (%s, %s, %s) "
           "ON DUPLICATE KEY UPDATE link_type = VALUES(link_type)")
    if rows:
        cur.executemany(sql, [(eid, cid, lt) for cid, eid, lt, s in rows])
        conn.commit()

    # --- report -----------------------------------------------------------------
    cur.execute("SELECT COUNT(DISTINCT content_id) FROM entity_content_links")
    covered = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM contents")
    total = cur.fetchone()[0]
    cur.execute("SELECT link_type, COUNT(*) FROM entity_content_links GROUP BY link_type")
    dist = dict(cur.fetchall())
    cur.execute("SELECT COUNT(*) FROM entity_content_links")
    total_links = cur.fetchone()[0]

    print("=" * 62)
    print(f"total contents              : {total}")
    print(f"newly linked contents       : {newly_covered}")
    print(f"distinct linked contents    : {covered}  ({covered / total * 100:.1f}%)")
    print(f"new links written           : {len(rows)}  (total now {total_links})")
    print(f"  via exact match           : {exact} content(s)")
    print(f"  new by link_type          : {dict(lt_counter)}")
    print(f"contents still no match     : {len(no_match)}")
    print(f"link_type distribution      : {dist}")
    for nm in no_match:
        print(f"  nomatch: {nm[0]} [{nm[1]}] {nm[2]} / {nm[3]}")
    print("=" * 62)
    ok = covered >= 700 and (covered / total) >= 0.80
    print(f"acceptance (>=700 & >=80%): {'PASS' if ok else 'CHECK'}")
    conn.close()
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
