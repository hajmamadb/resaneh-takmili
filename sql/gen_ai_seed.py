#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RESANAME AI — تولید seed از دیتابیس فعلی (فاز ۱+۳: گیت کیفی ۲۰ کارت)
خروجی: sql/seed-731-cards-sample.sql
مبنای سند: برنامه-تکمیل-محتوا-برای-سامانه-هوشمند.md (بخش ۲ و ۳)

اصول:
- فقط از داده‌های موجود در resaname_h.sql (cards, card_theorist, theorists,
  library_resources, library_resource_links) استفاده می‌شود.
- summary از ۲۴۰ کاراکتر اول core_logic به‌صورت خودکار تولید می‌شود
  (گیت کیفی: بعداً می‌توان با LLM باکیفیت‌تر تولید کرد).
- بخش‌بندی: ۱۰ section_key استاندارد از فیلدهای موجود.
- روابط دانش: card_theorist→theorist(0.9,verified)، related_approaches→related_to(0.7,unverified)،
  library_resource_links→cites(1.0,verified).
- nationality از جدول theorists (نام کشور دقیق) → ai_documents.country/origin برای کارت‌ها.
"""
import re
import io
import os
import sys
import json

SQL = r"D:\رسانامه تکمیلی\resaname_h.sql"
OUT = r"D:\رسانامه تکمیلی\sql\seed-731-cards-full.sql"
# LLM-generated summaries (2-4 sentence, high quality) — optional overlay
# Format: {"card-1": {"summary": "..."}, ...}
LLM_SUMMARIES = r"D:\رسانامه تکمیلی\sql\llm\summaries.json"

# ---------------------------------------------------------------- helpers
def esc(s):
    """SQL string escape for single-quoted literal"""
    if s is None:
        return "NULL"
    s = s.replace("\\", "\\\\").replace("'", "''")
    return "'" + s + "'"

def q(s):
    return "NULL" if s is None else esc(s)

def sha256_hex(s):
    import hashlib
    return hashlib.sha256((s or "").encode("utf-8")).hexdigest()

def _parse_tuple_line(raw):
    """Parse one mysqldump tuple line: (v1, v2, ..., vn) — no trailing semicolon.
    Handles MySQL backslash escapes (\\n, \\', \\\\, etc.) and NULL."""
    vals = []
    k = 1
    L = len(raw)
    ESC = {"\\": "\\", "'": "'", "n": "\n", "r": "\r", "t": "\t", "0": "\0"}
    while k < L - 1:
        # skip leading whitespace
        while k < L - 1 and raw[k] == " ":
            k += 1
        if k >= L - 1:
            break
        c = raw[k]
        if c == "'":
            # quoted string: scan to the unescaped closing quote
            k += 1
            buf = []
            while k < L - 1:
                if raw[k] == "\\" and k + 1 < L:
                    nxt = raw[k+1]
                    if nxt == "N" and (k == 1 or raw[k-1] == ","):
                        buf.append("\x00NULLMARK\x00")
                    else:
                        buf.append(ESC.get(nxt, nxt))
                    k += 2
                    continue
                if raw[k] == "'":
                    break
                buf.append(raw[k])
                k += 1
            vals.append("".join(buf))
            k += 1  # past closing quote
        elif c == ")":
            break
        else:
            # bare token (number / NULL): scan to the next comma or closing paren
            k2 = k
            while k2 < L - 1 and raw[k2] not in ",)":
                k2 += 1
            tok = raw[k:k2].strip()
            vals.append(None if tok == "NULL" else tok)
            k = k2
        # skip one separator comma, if present
        if k < L - 1 and raw[k] == ",":
            k += 1
    return vals

# ---------------------------------------------------------------- parse helpers
def _find_insert_bodies(seg, table):
    """Yield (cols_list, body_string) for each INSERT INTO `table` in seg.
    Finds the true end of each statement by scanning for `;` outside quotes."""
    for ins in re.finditer(r"INSERT INTO `" + table + r"` \(([^)]*)\) VALUES", seg):
        header = ins.group(1)
        start = ins.end()
        # Scan forward to find the terminating semicolon outside any quote
        j = start
        n = len(seg)
        in_str = False
        while j < n:
            c = seg[j]
            if in_str:
                if c == "\\" and j + 1 < n:
                    j += 2
                    continue
                if c == "'":
                    in_str = False
            else:
                if c == "'":
                    in_str = True
                elif c == ";":
                    break
            j += 1
        body = seg[start:j]
        cols = [c.strip().strip("`") for c in header.split(",")]
        yield cols, body

# ---------------------------------------------------------------- parse cards
def parse_cards(text):
    m = re.search(r"--\n-- Dumping data for table `cards`\n--", text)
    seg = text[m.end():]
    end = seg.find("\n-- --------------------------------------------------------")
    seg = seg[:end] if end != -1 else seg
    cards = {}
    for cols, body in _find_insert_bodies(seg, "cards"):
        for ln in body.split("\n"):
            ln = ln.strip()
            if not ln.startswith("("):
                continue
            ln = ln.rstrip(";").rstrip(",").rstrip()
            if not ln.endswith(")"):
                continue
            vals = _parse_tuple_line(ln)
            r = dict(zip(cols, vals))
            if r.get("id") and len(vals) == len(cols):
                cards[r["id"]] = r
    return cards

# ---------------------------------------------------------------- parse card_theorist
def parse_card_theorist(text):
    m = re.search(r"--\n-- Dumping data for table `card_theorist`\n--", text)
    seg = text[m.end():]
    end = seg.find("\n-- --------------------------------------------------------")
    seg = seg[:end] if end != -1 else seg
    links = []
    for ins in re.finditer(r"INSERT INTO `card_theorist` \(([^)]*)\) VALUES(.*?);\n", seg, re.S):
        cols = [c.strip().strip("`") for c in ins.group(1).split(",")]
        for tup in re.finditer(r"\(([^)]*)\)", ins.group(2)):
            parts = [p.strip().strip("'") for p in tup.group(1).split(",")]
            links.append(dict(zip(cols, parts)))
    return links

# ---------------------------------------------------------------- parse theorists
def parse_theorists(text):
    m = re.search(r"--\n-- Dumping data for table `theorists`\n--", text)
    seg = text[m.end():]
    end = seg.find("\n-- --------------------------------------------------------")
    seg = seg[:end] if end != -1 else seg
    theorists = {}
    for cols, body in _find_insert_bodies(seg, "theorists"):
        for ln in body.split("\n"):
            ln = ln.strip()
            if not ln.startswith("("):
                continue
            ln = ln.rstrip(";").rstrip(",").rstrip()
            if not ln.endswith(")"):
                continue
            vals = _parse_tuple_line(ln)
            r = dict(zip(cols, vals))
            if r.get("id") and len(vals) == len(cols):
                theorists[r["id"]] = r
    return theorists

# ---------------------------------------------------------------- parse library links
def parse_library_links(text):
    m = re.search(r"--\n-- Dumping data for table `library_resource_links`\n--", text)
    if not m:
        return []
    seg = text[m.end():]
    end = seg.find("\n-- --------------------------------------------------------")
    seg = seg[:end] if end != -1 else seg
    links = []
    for ins in re.finditer(r"INSERT INTO `library_resource_links` \(([^)]*)\) VALUES(.*?);\n", seg, re.S):
        cols = [c.strip().strip("`") for c in ins.group(1).split(",")]
        for tup in re.finditer(r"\(([^)]*)\)", ins.group(2)):
            parts = [p.strip().strip("'") for p in tup.group(1).split(",")]
            links.append(dict(zip(cols, parts)))
    return links

# ---------------------------------------------------------------- section builder
def build_sections(card):
    """Return list of (section_key, section_title, content, sort_order)"""
    out = []
    def add(key, title, content, order):
        if content and content.strip():
            out.append((key, title, content.strip(), order))

    approach = card.get("approach") or ""
    core_logic = card.get("core_logic") or ""
    detailed = card.get("detailed_analysis") or ""
    constructs = card.get("constructs") or ""
    example = card.get("example") or ""
    critique = card.get("critique") or ""

    # definition: approach + core_logic
    defn = "\n\n".join(x for x in [approach, core_logic] if x and x.strip())
    add("definition", "تعریف", defn, 1)

    # theoretical_framework: first ~30% of detailed_analysis if it exists, else core_logic
    if detailed and len(detailed) > 400:
        third = max(300, len(detailed) // 3)
        add("theoretical_framework", "چارچوب نظری", detailed[:third], 2)
    elif core_logic:
        add("theoretical_framework", "چارچوب نظری", core_logic, 2)

    # components: constructs
    add("components", "اجزای نظری", constructs, 3)

    # applications: from detailed if long (middle 30%)
    if detailed and len(detailed) > 800:
        mid_start = max(300, len(detailed) // 3)
        mid_end = max(mid_start + 300, len(detailed) * 2 // 3)
        add("applications", "کاربردها", detailed[mid_start:mid_end], 4)

    # examples
    add("examples", "مثال‌ها", example, 5)

    # criticism + limitations from critique (split if long)
    if critique:
        if len(critique) > 600:
            half = len(critique) // 2
            add("criticism", "نقدها", critique[:half], 6)
            add("limitations", "محدودیت‌ها", critique[half:], 7)
        else:
            add("criticism", "نقدها", critique, 6)

    # references: recommended_sources
    add("references", "منابع", card.get("recommended_sources") or "", 10)

    return out

# ---------------------------------------------------------------- reference parser (APA-ish)
def parse_sources(text_src):
    """Split recommended_sources into individual references (each ends with a year in parens)."""
    if not text_src:
        return []
    # Split on patterns like ". " followed by a capital letter and ending with a year
    # Simple heuristic: split on newline first, then on ". " boundaries that start a new author
    parts = []
    for para in re.split(r"\n+", text_src):
        para = para.strip()
        if not para:
            continue
        # if paragraph contains multiple sentences that look like separate refs, split on ". "
        # but keep DOI/URL intact
        sub = re.split(r"(?<=[.)])\s+(?=[A-Z][a-zA-Z\u0600-\u06FF])", para)
        for s in sub:
            s = s.strip().rstrip(".")
            if len(s) > 20:
                parts.append(s)
    return parts

def extract_year(ref):
    m = re.search(r"\(?(19|20)\d{2}\)?", ref)
    return int(m.group(0).strip("()")) if m else None

# ---------------------------------------------------------------- main
def main():
    with io.open(SQL, "r", encoding="utf-8") as f:
        text = f.read()

    cards = parse_cards(text)
    ct = parse_card_theorist(text)
    theorists = parse_theorists(text)
    lib_links = parse_library_links(text)

    print(f"Parsed: {len(cards)} cards, {len(ct)} card_theorist, "
          f"{len(theorists)} theorists, {len(lib_links)} library links")

    # ---- full set: all 731 cards (فاز ۳ — مقیاس‌بندی کامل)
    sample_ids = sorted(cards.keys(), key=lambda s: int(s.split("-")[1]))
    print(f"Full run: {len(sample_ids)} cards")

    # ---- optional LLM summary overlay
    llm_summ = {}
    if os.path.exists(LLM_SUMMARIES):
        with io.open(LLM_SUMMARIES, "r", encoding="utf-8") as f:
            llm_summ = json.load(f)
        print(f"LLM summaries loaded: {len(llm_summ)}")
    else:
        print("No LLM summaries file yet — using auto summaries (placeholder)")

    # card_theorist indexed by card
    ct_by_card = {}
    for l in ct:
        ct_by_card.setdefault(l.get("card_id"), []).append(l.get("theorist_id"))

    # library links: card -> resource
    lib_by_card = {}
    for l in lib_links:
        if l.get("entity_type") == "card":
            lib_by_card.setdefault(l["entity_id"], []).append(l.get("resource_id") or l.get("library_resource_id"))

    # ---- counters
    n_doc = 0; n_sec = 0; n_rel = 0; n_ref = 0; n_reflink = 0
    # entity/relationship id sequences
    ent_seq = 0; rel_seq = 0; ref_seq = 0

    out = io.StringIO()
    w = out.write
    n_llm = sum(1 for cid in sample_ids if llm_summ.get(cid, {}).get("summary"))
    w("-- ============================================================================\n")
    w(f"-- RESANAME AI — Seed: کل ۷۳۱ کارت (فاز ۳ — مقیاس‌بندی کامل)\n")
    w(f"-- تاریخ: 2026-11-09\n")
    w("-- مبنای داده: resaname_h.sql (cards + card_theorist + theorists + library)\n")
    w(f"-- summary: {n_llm} با LLM (کیفیت بالا) + {len(sample_ids)-n_llm} خودکار (placeholder — قابل به‌روزرسانی با sql/llm/summaries.json)\n")
    w("-- خروجی: ai_documents + ai_document_sections + ai_relationships +\n")
    w("--        ai_references + ai_document_references + ai_entities (theorists)\n")
    w("-- همه روابط استنباط‌شده: verification_status='unverified' (بند ۴.۳ سند فنی)\n")
    w("-- ============================================================================\n\n")
    w("USE resaname_h;\n\n")
    w("SET FOREIGN_KEY_CHECKS = 0;\n")
    w("TRUNCATE TABLE ai_document_references;\n")
    w("TRUNCATE TABLE ai_document_concepts;\n")
    w("TRUNCATE TABLE ai_relationships;\n")
    w("TRUNCATE TABLE ai_entities;\n")
    w("TRUNCATE TABLE ai_references;\n")
    w("TRUNCATE TABLE ai_document_sections;\n")
    w("TRUNCATE TABLE ai_documents;\n")
    w("SET FOREIGN_KEY_CHECKS = 1;\n\n")

    # ---- 1) ai_entities: all 39 theorists (nationality from DB = country)
    w("-- ----------------------------------------------------------------------------\n")
    w("-- 1) ai_entities — ۳۹ نظریه‌پرداز (country از nationality جدول theorists)\n")
    w("-- ----------------------------------------------------------------------------\n")
    ent_rows = []
    for tid in sorted(theorists.keys(), key=lambda x: int(x.split("-")[1])):
        t = theorists[tid]
        ent_seq += 1
        eid = f"entity-th-{tid.split('-')[1]}"
        nationality = t.get("nationality") or ""
        # origin: all existing are international
        origin = "international"
        # year -> int if possible (strip Persian digits)
        year_raw = t.get("year") or ""
        year_val = None
        m = re.search(r"(19|20)\d{2}", year_raw.replace("۰","0").replace("۱","1").replace("۲","2").replace("۳","3").replace("۴","4").replace("۵","5").replace("۶","6").replace("۷","7").replace("۸","8").replace("۹","9"))
        if m:
            year_val = int(m.group(0))
        image = t.get("avatar_url") or ""
        image_json = f'["{image}"]' if image else "NULL"
        summary = (t.get("bio") or "")[:400]
        ent_rows.append(
            f"('{eid}', 'theorist', {q(t.get('name'))}, {q(t.get('name_en'))}, "
            f"{q(t.get('slug'))}, {q(nationality)}, {q(origin)}, {year_val if year_val else 'NULL'}, "
            f"{q(nationality)}, {q(t.get('field'))}, {q(t.get('main_theory'))}, "
            f"{image_json}, {q(summary)}, NULL, 'verified', NOW(), NOW())"
        )
    if ent_rows:
        w("INSERT INTO `ai_entities` (`id`, `entity_type`, `name`, `name_en`, `slug`, `country`, `origin`, `year`, `nationality`, `field`, `main_theory`, `image_urls`, `summary`, `external_url`, `verification_status`, `created_at`, `updated_at`) VALUES\n")
        w(",\n".join(ent_rows) + ";\n\n")
    print(f"ai_entities: {ent_seq} rows (theorists)")

    # ---- 2) per-card: ai_documents + sections + relationships + references
    for cid in sample_ids:
        c = cards[cid]
        doc_id = f"doc-{cid}"
        slug = c.get("slug") or cid
        title = c.get("title_fa") or ""
        etitle = c.get("title_en") or None
        ctype_raw = c.get("card_type") or ""
        # map card_type -> content_type
        ctype_map = {"نظریه": "theory", "مدل": "model", "چارچوب": "framework",
                     "اثر": "effect", "فرضیه": "hypothesis", "پارادایم": "paradigm",
                     "سوگیری": "bias", "اصل": "principle", "مفهوم": "concept",
                     "قانون": "law", "رویکرد": "approach"}
        content_type = ctype_map.get(ctype_raw, "theory")
        core_logic = c.get("core_logic") or ""
        approach = c.get("approach") or ""
        # summary: prefer LLM-generated (high quality, 2-4 sentences)
        llm_entry = llm_summ.get(cid)
        if llm_entry and llm_entry.get("summary"):
            summary = llm_entry["summary"].strip()
        else:
            # fallback: first ~240 chars of core_logic (auto-generated placeholder)
            src_text = core_logic if core_logic else approach
            summary = re.sub(r"\s+", " ", src_text).strip()
            if len(summary) > 300:
                cut = summary[:300]
                cut = cut[:cut.rfind(" ")]
                summary = cut.rstrip("،. ") + " …"
            elif summary:
                summary = summary.rstrip("،. ") + "." if not summary.endswith(".") else summary
        canonical = f"https://resaname.ir/cards/{cid}"
        # country for cards: the most-linked theorist's nationality (or NULL)
        card_th = ct_by_card.get(cid, [])
        country = None
        if card_th:
            t0 = theorists.get(card_th[0])
            if t0:
                country = t0.get("nationality")
        origin = "international" if country else None
        content_hash = sha256_hex((c.get("approach") or "") + (c.get("core_logic") or "") +
                                  (c.get("detailed_analysis") or "") + (c.get("example") or "") +
                                  (c.get("critique") or ""))
        w(f"-- {cid}: {title}\n")
        w(f"INSERT INTO `ai_documents` (`id`, `source_type`, `source_id`, `slug`, `title`, `english_title`, `content_type`, `summary`, `canonical_url`, `language`, `country`, `origin`, `content_hash`, `source_updated_at`, `indexed_at`) VALUES\n")
        w(f"('{doc_id}', 'card', {q(cid)}, {q(slug)}, {q(title)}, {q(etitle)}, {q(content_type)}, {q(summary)}, {q(canonical)}, 'fa', {q(country)}, {q(origin)}, {q(content_hash)}, {q(c.get('updated_at'))}, NOW());\n")
        n_doc += 1

        # sections
        secs = build_sections(c)
        if secs:
            sec_rows = []
            for key, stitle, content, order in secs:
                sec_id = f"sec-{cid}-{order}"
                c_hash = sha256_hex(content)
                sec_rows.append(
                    f"('{sec_id}', '{doc_id}', {q(key)}, {q(stitle)}, {q(content)}, {q(c_hash)}, {order}, NOW(), NOW())"
                )
            w("INSERT INTO `ai_document_sections` (`id`, `document_id`, `section_key`, `section_title`, `content`, `content_hash`, `sort_order`, `created_at`, `updated_at`) VALUES\n")
            w(",\n".join(sec_rows) + ";\n")
            n_sec += len(sec_rows)
            # remember references section id
            ref_sec_id = f"sec-{cid}-10" if any(s[0] == "references" for s in secs) else None
        else:
            ref_sec_id = None

        # relationships: card_theorist
        rel_rows = []
        for th_id in card_th:
            rel_seq += 1
            t = theorists.get(th_id)
            desc = f"نظریه‌پرداز مرتبط با {title}" if t else None
            th_num = th_id.split("-")[1]
            rel_rows.append(
                f"('rel-{rel_seq:05d}', 'document', '{doc_id}', 'theorist', 'entity', "
                f"'entity-th-{th_num}', {q(desc)}, 0.9000, 'verified', 'manual', NOW())"
            )
        # related_approaches -> related_to (unverified, AI-derived)
        related = (c.get("related_approaches") or "").strip()
        if related:
            # split on common separators
            items = re.split(r"[؛;،,\n]+", related)
            for it in items:
                it = it.strip()
                if len(it) > 3:
                    rel_seq += 1
                    it_escaped = esc(it)
                    rel_rows.append(
                        f"('rel-{rel_seq:05d}', 'document', '{doc_id}', 'related_to', 'document', "
                        f"'{it}__unresolved', {it_escaped}, 0.7000, 'unverified', 'ai-extract', NOW())"
                    )
        if rel_rows:
            w("INSERT INTO `ai_relationships` (`id`, `source_type`, `source_id`, `relationship_type`, `target_type`, `target_id`, `description`, `confidence`, `verification_status`, `extracted_by`, `created_at`) VALUES\n")
            w(",\n".join(rel_rows) + ";\n")
            n_rel += len(rel_rows)

        # references: parse recommended_sources
        sources = parse_sources(c.get("recommended_sources") or "")
        if sources:
            ref_rows = []
            ref_links = []
            for i, s in enumerate(sources, 1):
                ref_seq += 1
                ref_id = f"ref-{cid}-{i:02d}"
                year = extract_year(s)
                # heuristic type: if contains "Journal" or "Review" -> article, else book
                rtype = "article" if re.search(r"journal|review|quarterly", s, re.I) else "book"
                ref_rows.append(
                    f"('{ref_id}', {q(rtype)}, {q(s)}, NULL, NULL, NULL, "
                    f"{year if year else 'NULL'}, NULL, NULL, NULL, NULL, "
                    f"{q(s)}, NULL, 'unverified', NOW(), NOW())"
                )
                ref_links.append(
                    f"('{doc_id}', {q(ref_sec_id)}, '{ref_id}', 'cites', {i})"
                )
            w("INSERT INTO `ai_references` (`id`, `reference_type`, `title`, `title_en`, `authors`, `publisher`, `journal`, `publication_year`, `isbn`, `doi`, `issn`, `source_url`, `citation_apa`, `image_urls`, `verification_status`, `created_at`, `updated_at`) VALUES\n")
            w(",\n".join(ref_rows) + ";\n")
            w("INSERT INTO `ai_document_references` (`document_id`, `section_id`, `reference_id`, `relation_type`, `sort_order`) VALUES\n")
            w(",\n".join(ref_links) + ";\n")
            n_ref += len(ref_rows)
            n_reflink += len(ref_links)

        w("\n")

    # ---- footer
    w("-- ============================================================================\n")
    w(f"-- پایان seed — خلاصه:\n")
    w(f"--   ai_documents:           {n_doc}\n")
    w(f"--   ai_document_sections:   {n_sec}\n")
    w(f"--   ai_relationships:       {n_rel}\n")
    w(f"--   ai_references:          {n_ref}\n")
    w(f"--   ai_document_references: {n_reflink}\n")
    w(f"--   ai_entities:            {ent_seq}\n")
    w("-- ============================================================================\n")
    w("-- ⚠️ note: related_to روابط به target_id unresolved هستند؛ در فاز ۵ با\n")
    w("--    resolution به card-id واقعی جایگزین می‌شوند.\n")
    w("-- ⚠️ summary‌ها خودکار تولید شده‌اند؛ برای مقیاس به ۷۳۱ با LLM بازنویسی.\n")

    with io.open(OUT, "w", encoding="utf-8") as f:
        f.write(out.getvalue())
    print(f"\nWrote {OUT}")
    print(f"Summary: docs={n_doc} sections={n_sec} rels={n_rel} refs={n_ref} reflinks={n_reflink} entities={ent_seq}")

if __name__ == "__main__":
    main()
