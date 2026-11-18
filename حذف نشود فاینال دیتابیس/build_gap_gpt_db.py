"""Build gap-gpt-db-resanameh-irfable.sql.

Schema + registries come verbatim from final_database.sql (the pattern).
Content comes from resaname_editorial-final-20261115-1926.sql, limited to
editorial documents whose quality_score is 90 or higher.
"""
import collections
import json
import re
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
PATTERN_FILE = BASE / "final_database.sql"
EDITORIAL_FILE = BASE / "resaname_editorial-final-20261115-1926.sql"
DB_NAME = "gap-gpt-db-resanameh-irfable"
OUTPUT_FILE = BASE / (DB_NAME + ".sql")
REPORT_FILE = BASE / (DB_NAME + "-report.json")
MIN_SCORE = 90
SEED_ACTOR = "seed:editorial"

UNESCAPE = {"0": "\0", "n": "\n", "r": "\r", "t": "\t", "b": "\b", "Z": "\x1a"}

TYPE_BY_TAG = {
    "Theory": "THEORY",
    "Model": "MODEL",
    "Theoretical Framework": "FRAMEWORK",
    "Operational Framework": "FRAMEWORK",
    "Strategy": "FRAMEWORK",
    "Hypothesis": "HYPOTHESIS",
    "Research Method": "METHOD",
    "Effect": "CONCEPT",
    "Concept": "CONCEPT",
    "School": "SCHOOL",
    "Paradigm": "PARADIGM",
}
SUBTYPE_BY_TAG = {
    "Effect": "EFFECT",
    "Strategy": "APPLIED_STRATEGY",
    "Operational Framework": "OPERATIONAL_FRAMEWORK",
}
FAMILY_BY_TYPE = {
    "THEORY": "KNOWLEDGE_STRUCTURE",
    "MODEL": "KNOWLEDGE_STRUCTURE",
    "FRAMEWORK": "KNOWLEDGE_STRUCTURE",
    "HYPOTHESIS": "KNOWLEDGE_STRUCTURE",
    "CONCEPT": "KNOWLEDGE_STRUCTURE",
    "METHOD": "RESEARCH_METHODOLOGY",
    "SCHOOL": "THEORETICAL_SYSTEM",
    "PARADIGM": "THEORETICAL_SYSTEM",
    "PERSON": "INTELLECTUAL_AGENT",
    "DISCIPLINE": "SCIENTIFIC_DOMAIN",
    "SUBFIELD": "SCIENTIFIC_DOMAIN",
    "WORK": "RESEARCH_RESOURCE",
}
SCALE_BY_LEVEL = {"خرد": "MICRO", "میانی": "MESO", "کلان": "MACRO"}
LANGUAGE_CODES = {"انگلیسی": "en", "فارسی": "fa", "آلمانی": "de", "فرانسوی": "fr"}
PROPOSER_HINTS = ("بنیان", "واضع", "نظریه‌پرداز اصلی", "ارائه‌دهنده", "مبدع", "طراح", "خالق")
NOISE_WORDS = {"theory", "the", "of", "نظریه", "نظریه‌ی"}


def parse_rows(text, position):
    rows = []
    while True:
        while text[position] in " ,\n\r":
            position += 1
        if text[position] == ";":
            return rows
        position += 1
        row = []
        while True:
            if text[position] == "'":
                position += 1
                parts = []
                while True:
                    char = text[position]
                    if char == "\\":
                        following = text[position + 1]
                        parts.append(UNESCAPE.get(following, following))
                        position += 2
                    elif char == "'":
                        if text[position + 1] == "'":
                            parts.append("'")
                            position += 2
                        else:
                            position += 1
                            break
                    else:
                        end = position
                        while text[end] not in "\\'":
                            end += 1
                        parts.append(text[position:end])
                        position = end
                row.append("".join(parts))
            else:
                end = position
                while text[end] not in ",)":
                    end += 1
                token = text[position:end]
                row.append(None if token == "NULL" else token)
                position = end
            if text[position] == ",":
                position += 1
            else:
                position += 1
                break
        rows.append(row)


def load_tables(path, wanted):
    tables = collections.defaultdict(list)
    with open(path, encoding="utf-8") as handle:
        for line in handle:
            match = re.match(r"INSERT INTO `(\w+)` VALUES ", line)
            if match and match.group(1) in wanted:
                tables[match.group(1)].extend(parse_rows(line, match.end()))
    return tables


def sql(value):
    if value is None:
        return "NULL"
    if isinstance(value, bool):
        return "1" if value else "0"
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, (dict, list)):
        value = json.dumps(value, ensure_ascii=False, separators=(",", ":"))
    text = str(value)
    text = text.replace("\\", "\\\\").replace("'", "\\'").replace("\0", "\\0")
    text = text.replace("\n", "\\n").replace("\r", "\\r").replace("\x1a", "\\Z")
    return "'" + text + "'"


def insert(table, columns, values):
    return "INSERT INTO %s (%s) VALUES (%s);" % (table, ", ".join(columns), ", ".join(values))


def clip(value, limit):
    if value is None:
        return None
    text = str(value).strip()
    if not text:
        return None
    return text if len(text) <= limit else text[: limit - 1] + "…"


def name_keys(name):
    name = (name or "").strip()
    candidates = [name]
    if "(" in name and name.endswith(")"):
        candidates.append(name[: name.index("(")])
        candidates.append(name[name.index("(") + 1 : -1])
    keys = []
    for candidate in candidates:
        text = re.sub(r"[\-‐‑–—_/]", " ", candidate.lower().replace("\u200c", " "))
        text = re.sub(r"[^\w\s]", "", text)
        words = [word for word in text.split() if word not in NOISE_WORDS]
        if words:
            keys.append(" ".join(words))
    return keys


def english_tag(content_type):
    match = re.search(r"\(([^)]+)\)\s*$", content_type or "")
    return match.group(1).strip() if match else None


def norm_key(text):
    text = (text or "").replace("\u200c", " ").replace("\u200f", "")
    text = text.replace("ي", "ی").replace("ك", "ک").replace("\u0640", "")
    text = re.sub(r"[\u064b-\u0655\u0670]", "", text)
    return re.sub(r"\s+", " ", text).strip()


def display(text):
    text = (text or "").replace("\u200f", "").replace("ي", "ی").replace("ك", "ک").replace("\u0640", "")
    return re.sub(r"\s+", " ", text).strip()


def taxonomy_key(text):
    parts = re.split(r"\s*[/،؛]\s*|\s+و\s+", norm_key(text))
    return tuple(sorted(part.strip() for part in parts if part.strip()))


def slugify(text, limit=60):
    text = display(text).lower().replace(" ", "-")
    text = re.sub(r"[^\w\u0600-\u06ff-]", "", text)
    text = re.sub(r"-+", "-", text).strip("-")
    text = text.translate(DIGIT_MAP)
    return text[:limit] or "item"


DIGIT_MAP = str.maketrans("۰۱۲۳۴۵۶۷۸۹٠١٢٣٤٥٦٧٨٩", "01234567890123456789")


def ci_key(text):
    """Approximate utf8mb4_unicode_ci equality so unique keys survive in MySQL."""
    text = (text or "").replace("\u200c", "").replace("\u200d", "").replace("\u200f", "")
    text = text.replace("ي", "ی").replace("ك", "ک").replace("\u0640", "")
    text = re.sub(r"[\u064b-\u0655\u0670]", "", text)
    return text.translate(DIGIT_MAP).lower()


def build_derived(entities, sources, emit, insert, sql, clip, report):
    """Derive DISCIPLINE/SUBFIELD/PARADIGM/CONCEPT/WORK entities from approved dossiers."""
    next_id = len(entities) + 1
    used_codes = {ci_key(entity["code"]) for entity in entities}
    used_slugs = {ci_key(entity["slug"]) for entity in entities}
    cards = [entity for entity in entities if entity["entity_type"] != "PERSON"]

    def unique(base, index):
        candidate, counter = base, 2
        while ci_key(candidate) in index:
            candidate = "%s-%d" % (base, counter)
            counter += 1
        index.add(ci_key(candidate))
        return candidate

    def add_entity(entity_type, name_fa, name_en, slug_base, properties, aliases, stamp, origin):
        nonlocal next_id
        slug = unique(slug_base, used_slugs)
        code = unique(origin + "-" + slug, used_codes)
        entity = dict(
            id=next_id,
            code=code,
            entity_type=entity_type,
            family_code=FAMILY_BY_TYPE[entity_type],
            name_fa=clip(name_fa, 500),
            name_en=clip(name_en, 500),
            slug=slug,
            aliases=aliases or None,
            properties=properties,
            created_at=stamp,
            updated_at=stamp,
            derived=origin,
        )
        next_id += 1
        entities.append(entity)
        return entity

    groups = dict(
        discipline=collections.defaultdict(list),
        subfield=collections.defaultdict(list),
        paradigm=collections.defaultdict(list),
        concept=collections.defaultdict(list),
        work=collections.defaultdict(list),
    )
    for entity in cards:
        field = entity["content"].get("field") or {}
        if field.get("parent"):
            groups["discipline"][taxonomy_key(field["parent"])].append((entity, display(field["parent"])))
        if field.get("subfield"):
            groups["subfield"][taxonomy_key(field["subfield"])].append((entity, display(field["subfield"])))
        if entity["raw"].get("paradigm"):
            groups["paradigm"][norm_key(entity["raw"]["paradigm"]).lower()].append(
                (entity, display(entity["raw"]["paradigm"]))
            )
        for item in entity["content"].get("key_concepts") or []:
            if isinstance(item, dict) and item.get("term_fa"):
                groups["concept"][norm_key(item["term_fa"]).lower()].append((entity, item))
        for item in entity["content"].get("sources") or []:
            if isinstance(item, dict) and (item.get("citation") or "").strip():
                groups["work"][norm_key(item["citation"]).lower()].append((entity, item))

    def canonical(members):
        counts = collections.Counter(label for _, label in members)
        label = sorted(counts.items(), key=lambda pair: (-pair[1], pair[0]))[0][0]
        aliases = sorted(name for name in counts if name != label)
        stamp = max(entity["updated_at"] for entity, _ in members)
        return label, aliases, stamp

    index = {}
    existing_by_name = {}
    for entity in entities:
        if entity["entity_type"] != "CONCEPT":
            continue
        for name in (entity["name_fa"], entity["name_en"]):
            if name:
                existing_by_name.setdefault(norm_key(name).lower(), entity["id"])

    for key, members in sorted(groups["discipline"].items(), key=lambda pair: (-len(pair[1]), pair[0])):
        label, aliases, stamp = canonical(members)
        properties = collections.OrderedDict(
            taxonomy="field.parent",
            card_count=len(members),
            card_codes=sorted({entity["code"] for entity, _ in members}),
        )
        entity = add_entity("DISCIPLINE", label, None, slugify(label), properties, aliases, stamp, "discipline")
        index[("discipline", key)] = entity["id"]

    for key, members in sorted(groups["subfield"].items(), key=lambda pair: (-len(pair[1]), pair[0])):
        label, aliases, stamp = canonical(members)
        parents = collections.Counter(
            taxonomy_key(entity["content"]["field"]["parent"])
            for entity, _ in members
            if (entity["content"].get("field") or {}).get("parent")
        )
        parent_key = sorted(parents.items(), key=lambda pair: (-pair[1], pair[0]))[0][0] if parents else None
        properties = collections.OrderedDict(
            taxonomy="field.subfield",
            card_count=len(members),
            card_codes=sorted({entity["code"] for entity, _ in members}),
        )
        entity = add_entity("SUBFIELD", label, None, slugify(label), properties, aliases, stamp, "subfield")
        index[("subfield", key)] = entity["id"]
        if parent_key and ("discipline", parent_key) in index:
            index.setdefault("subfield_parent", {})[entity["id"]] = index[("discipline", parent_key)]

    for key, members in sorted(groups["paradigm"].items(), key=lambda pair: (-len(pair[1]), pair[0])):
        label, aliases, stamp = canonical(members)
        properties = collections.OrderedDict(
            taxonomy="card.paradigm",
            card_count=len(members),
            card_codes=sorted({entity["code"] for entity, _ in members}),
        )
        entity = add_entity("PARADIGM", label, None, slugify(label), properties, aliases, stamp, "paradigm")
        index[("paradigm", key)] = entity["id"]

    for key, members in sorted(groups["concept"].items(), key=lambda pair: (-len(pair[1]), pair[0])):
        if key in existing_by_name:
            index[("concept", key)] = existing_by_name[key]
            continue
        label, aliases, stamp = canonical([(entity, display(item["term_fa"])) for entity, item in members])
        english = collections.Counter(
            display(item["term_en"]) for _, item in members if item.get("term_en")
        )
        definition = max(
            (display(item.get("definition") or "") for _, item in members), key=len, default=""
        )
        properties = collections.OrderedDict(
            term_fa=label,
            term_en=sorted(english.items(), key=lambda pair: (-pair[1], pair[0]))[0][0] if english else None,
            definition=definition or None,
            card_count=len(members),
            card_codes=sorted({entity["code"] for entity, _ in members}),
        )
        slug_base = slugify(properties["term_en"] or label)
        entity = add_entity("CONCEPT", label, properties["term_en"], slug_base, properties, aliases, stamp, "concept")
        index[("concept", key)] = entity["id"]

    for key, members in sorted(groups["work"].items(), key=lambda pair: pair[0]):
        citation = max((display(item["citation"]) for _, item in members), key=len)
        stamp = max(entity["updated_at"] for entity, _ in members)
        year = re.search(r"\((1[5-9]\d\d|20\d\d)[a-z]?\)", citation)
        properties = collections.OrderedDict(
            citation=citation,
            year=int(year.group(1)) if year else None,
            doi=next((item.get("doi") for _, item in members if item.get("doi")), None),
            url=next((item.get("url") for _, item in members if item.get("url")), None),
            cited_by=sorted({entity["code"] for entity, _ in members}),
        )
        title = re.sub(r"^.*?\(\d{4}[a-z]?\)\.\s*", "", citation)
        title = re.split(r"\.\s", title)[0] or citation
        entity = add_entity("WORK", citation, title, slugify(title), properties, None, stamp, "work")
        index[("work", key)] = entity["id"]

    relations = collections.OrderedDict()
    fallback_stamp = max(entity["updated_at"] for entity in entities if entity.get("updated_at"))
    skipped = collections.Counter()

    def link(source_id, target_id, relation_type, note, confidence, stamp):
        if source_id == target_id:
            return
        key = (source_id, target_id, relation_type)
        if key not in relations:
            relations[key] = (note, confidence, stamp or fallback_stamp)

    for entity in cards:
        field = entity["content"].get("field") or {}
        if entity["raw"].get("paradigm"):
            target = index[("paradigm", norm_key(entity["raw"]["paradigm"]).lower())]
            link(entity["id"], target, "BELONGS_TO", "پارادایم کارت: %s" % display(entity["raw"]["paradigm"]), "0.900", entity["updated_at"])
        if field.get("subfield"):
            target = index[("subfield", taxonomy_key(field["subfield"]))]
            note = "زیرحوزه‌ی کارت: %s" % display(field["subfield"])
            if entity["entity_type"] in ("THEORY", "CONCEPT"):
                link(target, entity["id"], "STUDIES", note, "0.900", entity["updated_at"])
            elif entity["entity_type"] in ("MODEL", "FRAMEWORK"):
                link(entity["id"], target, "APPLIED_IN", note, "0.900", entity["updated_at"])
            else:
                skipped["STUDIES:" + entity["entity_type"]] += 1
        for item in entity["content"].get("key_concepts") or []:
            if isinstance(item, dict) and item.get("term_fa"):
                target = index[("concept", norm_key(item["term_fa"]).lower())]
                if entity["entity_type"] in ("THEORY", "MODEL", "FRAMEWORK"):
                    link(entity["id"], target, "USES_CONCEPT", "مفهوم کلیدی کارت", "0.900", entity["updated_at"])
                else:
                    skipped["USES_CONCEPT:" + entity["entity_type"]] += 1

    for subfield_id, discipline_id in (index.get("subfield_parent") or {}).items():
        link(subfield_id, discipline_id, "PART_OF", "حوزه‌ی بالادست در طبقه‌بندی ویراستاری", "0.900", None)

    concept_subfield = collections.defaultdict(collections.Counter)
    for entity in cards:
        subfield = (entity["content"].get("field") or {}).get("subfield")
        if not subfield:
            continue
        subfield_id = index[("subfield", taxonomy_key(subfield))]
        for item in entity["content"].get("key_concepts") or []:
            if isinstance(item, dict) and item.get("term_fa"):
                concept_subfield[index[("concept", norm_key(item["term_fa"]).lower())]][subfield_id] += 1
    for concept_id, counter in concept_subfield.items():
        subfield_id = sorted(counter.items(), key=lambda pair: (-pair[1], pair[0]))[0][0]
        link(subfield_id, concept_id, "STUDIES", "مشتق: مفهومِ نظریه‌ای که در این زیرحوزه مطالعه می‌شود", "0.700", None)

    surnames = {}
    for entity in entities:
        if entity["entity_type"] == "PERSON" and entity["name_en"]:
            surname = re.sub(r"[^\w]", "", entity["name_en"].split()[-1]).lower()
            if surname:
                surnames[surname] = entity["id"]
    for key, members in groups["work"].items():
        work_id = index[("work", key)]
        citation = max((display(item["citation"]) for _, item in members), key=len)
        head = citation.split("(")[0]
        tokens = {re.sub(r"[^\w]", "", token).lower() for token in re.split(r"[,&]", head)}
        for surname in sorted(tokens & set(surnames)):
            link(work_id, surnames[surname], "AUTHORED_BY", "نویسنده‌ی مستخرج از استناد", "0.800", None)

    for entity in cards:
        for item in entity["content"].get("related") or []:
            if not isinstance(item, dict):
                continue
            note = display(item.get("relation") or "")
            if "متعارض" not in note:
                continue
            target = resolve_title(item.get("name"), entities)
            if target and target != entity["id"]:
                low, high = sorted((entity["id"], target))
                link(low, high, "CONTRADICTS", "یادداشت ویراستاری: %s" % note, "0.700", entity["updated_at"])
            if "توسعه‌دهنده" in note and target:
                link(entity["id"], target, "EXTENDS", "یادداشت ویراستاری: %s" % note, "0.700", entity["updated_at"])

    emit("")
    emit("-- 6.9) موجودیت‌های مشتق از داسیه‌های تأییدشده (حوزه، زیرحوزه، پارادایم، مفهوم، اثر)")
    columns = ["id", "code", "entity_type", "family_code", "canonical_name_fa", "canonical_name_en", "slug",
               "aliases", "original_name", "original_language", "language", "properties", "status_workflow",
               "status_scientific", "status_lifecycle", "visibility", "version", "external_identifiers",
               "created_at", "created_by", "updated_at", "updated_by", "verified_at", "verified_by"]
    derived = [entity for entity in entities if entity.get("derived")]
    for entity in derived:
        emit(insert("kb_entities", columns, [
            sql(entity["id"]), sql(entity["code"]), sql(entity["entity_type"]), sql(entity["family_code"]),
            sql(entity["name_fa"]), sql(entity["name_en"]), sql(entity["slug"]), sql(entity["aliases"]),
            "NULL", "NULL", sql("fa"), sql(entity["properties"]), sql("approved"), sql("unassessed"),
            sql("active"), sql("public"), "1", "NULL", sql(entity["created_at"]), sql("seed:derived"),
            sql(entity["updated_at"]), sql("seed:derived"), "NULL", "NULL",
        ]))

    emit("")
    emit("-- 6.10) روابط مشتق")
    relation_columns = ["source_id", "target_id", "relation_type", "assertion_status", "asserted_by",
                        "extraction_confidence", "note", "weight", "status", "created_at", "updated_at"]
    for (source_id, target_id, relation_type), (note, confidence, stamp) in relations.items():
        emit(insert("kb_relations", relation_columns, [
            sql(source_id), sql(target_id), sql(relation_type), sql("under_review"), sql("seed:derived"),
            sql(confidence), sql(note), "50", sql("active"), sql(stamp), sql(stamp),
        ]))

    emit("")
    emit("-- 6.11) اتصال منابع به اثر علمی (kb_sources.work_id)")
    for source in sources.values():
        citation = (source["bibliographic"] or {}).get("citation") or source["title"]
        work_id = index.get(("work", norm_key(citation).lower()))
        if work_id:
            emit("UPDATE kb_sources SET work_id = %d WHERE id = %d;" % (work_id, source["id"]))

    emit("")
    emit("-- 6.12) نسخه و ممیزی موجودیت‌های مشتق")
    for entity in derived:
        snapshot = collections.OrderedDict(
            code=entity["code"], entity_type=entity["entity_type"], family_code=entity["family_code"],
            canonical_name_fa=entity["name_fa"], canonical_name_en=entity["name_en"], slug=entity["slug"],
            aliases=entity["aliases"], properties=entity["properties"], status_workflow="approved",
        )
        emit(insert("kb_entity_versions", ["entity_id", "version", "snapshot", "change_reason", "changed_by", "created_at"], [
            sql(entity["id"]), "1", sql(snapshot), sql("مشتق از داسیه‌های تأییدشده (امتیاز ۹۰+)"),
            sql("seed:derived"), sql(entity["created_at"]),
        ]))
        emit(insert("kb_audit_log", ["entity_code", "action", "detail", "source", "created_at"], [
            sql(entity["code"]), sql("derive_import"),
            sql(collections.OrderedDict(derived_from=entity["derived"], properties=entity["properties"])),
            sql("derived_seed"), sql(entity["created_at"]),
        ]))

    report["derived"] = collections.OrderedDict(
        (name, sum(1 for entity in derived if entity["entity_type"] == name))
        for name in ("DISCIPLINE", "SUBFIELD", "PARADIGM", "CONCEPT", "WORK")
    )
    report["derived_relations"] = dict(collections.Counter(key[2] for key in relations))
    report["derived_skipped_domain"] = dict(skipped)
    return relations


def resolve_title(name, entities):
    """Resolve a free-text related-item name to an entity id (exact title match)."""
    if not name:
        return None
    text = display(name)
    inner = text[text.find("(") + 1 : text.rfind(")")] if "(" in text and text.endswith(")") else ""
    outer = text.split("(")[0]
    for candidate in (inner, outer, text):
        key = norm_key(candidate).lower()
        for entity in entities:
            if entity["entity_type"] == "PERSON":
                continue
            names = [entity["name_fa"], entity["name_en"]]
            if any(norm_key(item).lower() == key for item in names if item):
                return entity["id"]
    return None


def build():
    tables = load_tables(
        EDITORIAL_FILE,
        {"editorial_documents", "editorial_revisions", "editorial_reviews", "editorial_users"},
    )
    users = {row[0]: row[1] for row in tables["editorial_users"]}
    documents = [
        row for row in tables["editorial_documents"]
        if row[11] is not None and int(row[11]) >= MIN_SCORE
    ]
    documents.sort(key=lambda row: int(row[0]))
    document_ids = {row[0] for row in documents}

    approved = {}
    for revision in tables["editorial_revisions"]:
        if revision[1] in document_ids and revision[2] == "approved":
            current = approved.get(revision[1])
            if current is None or (revision[7], int(revision[0])) > (current[7], int(current[0])):
                approved[revision[1]] = revision
    reviewers = {}
    for review in tables["editorial_reviews"]:
        if review[1] in document_ids and review[3] == "approved":
            reviewers[review[1]] = users.get(review[2], "editor")

    report = collections.OrderedDict()
    report["database"] = DB_NAME
    report["min_score"] = MIN_SCORE
    report["editorial_documents_total"] = len(tables["editorial_documents"])
    report["documents_selected"] = len(documents)
    report["skipped"] = []

    entities = []
    used_codes = set()
    used_slugs = set()
    for row in documents:
        document_id = row[0]
        revision = approved.get(document_id)
        if revision is None:
            report["skipped"].append({"document_id": int(document_id), "reason": "no approved revision"})
            continue
        raw = json.loads(row[8])
        content = json.loads(revision[3])
        score = int(row[11])
        editorial = collections.OrderedDict(
            document_id=int(document_id),
            source_table=row[1],
            source_id=row[2],
            quality_score=score,
            workflow_status=row[10],
            approved_revision_id=int(revision[0]),
            approved_content_hash=revision[4],
            content_category=row[17],
            content_type=row[18],
            structure_version=int(row[16]),
            site_status=row[4],
        )
        if row[1] == "theorists":
            entity_type = "PERSON"
            slug = raw["slug"]
            code = "person-" + slug
            name_fa = content.get("name") or row[3]
            name_en = content.get("name_en")
            aliases = None
            properties = collections.OrderedDict(
                (key, content.get(key))
                for key in ("nationality", "field", "main_theory", "year", "bio", "academic_career",
                            "quote", "importance", "cards_count", "avatar_url")
            )
            link_type = "theorist"
            tag = None
        elif row[1] == "cards":
            tag = english_tag(row[18])
            entity_type = TYPE_BY_TAG.get(tag)
            if entity_type is None:
                report["skipped"].append({"document_id": int(document_id), "reason": "unmapped content_type: %s" % row[18]})
                continue
            slug = content.get("slug") or raw["slug"]
            code = raw.get("code") or slug.upper()
            name_fa = content.get("title_fa") or row[3]
            name_en = content.get("title_en")
            aliases = content.get("aliases") or None
            properties = collections.OrderedDict(
                (key, content.get(key))
                for key in ("summary", "year", "theorists", "history", "field", "main_problem", "assumptions",
                            "key_concepts", "principles", "model", "mechanism", "applications", "studies",
                            "evolution", "critiques", "related", "sources", "research_guide")
            )
            tags = raw.get("tags")
            if isinstance(tags, str):
                try:
                    tags = json.loads(tags)
                except ValueError:
                    pass
            properties["card"] = collections.OrderedDict(
                code=raw.get("code"),
                card_type=raw.get("card_type"),
                macro_domain=raw.get("macro_domain"),
                paradigm=raw.get("paradigm"),
                level=raw.get("level"),
                category_id=raw.get("category_id"),
                image_url=raw.get("image_url"),
                tags=tags,
            )
            link_type = "card"
        else:
            report["skipped"].append({"document_id": int(document_id), "reason": "unsupported source_table: %s" % row[1]})
            continue
        if code in used_codes or slug in used_slugs:
            report["skipped"].append({"document_id": int(document_id), "reason": "duplicate code/slug: %s" % code})
            continue
        used_codes.add(code)
        used_slugs.add(slug)
        properties["editorial"] = editorial
        entities.append(dict(
            id=len(entities) + 1,
            code=code,
            entity_type=entity_type,
            family_code=FAMILY_BY_TYPE[entity_type],
            name_fa=clip(name_fa, 500),
            name_en=clip(name_en, 500),
            slug=slug,
            aliases=aliases,
            properties=properties,
            external={"editorial_document_id": int(document_id), "site_table": row[1], "site_id": row[2]},
            created_at=row[12],
            updated_at=row[13],
            verified_at=revision[7],
            verified_by=reviewers.get(document_id, users.get(revision[5], "editor")),
            revision=revision,
            score=score,
            link_type=link_type,
            link_id=row[2],
            tag=tag,
            raw=raw,
            content=content,
        ))

    out = []
    emit = out.append

    emit("-- 6.1) موجودیت‌ها (kb_entities)")
    entity_columns = ["id", "code", "entity_type", "family_code", "canonical_name_fa", "canonical_name_en", "slug",
                      "aliases", "original_name", "original_language", "language", "properties", "status_workflow",
                      "status_scientific", "status_lifecycle", "visibility", "version", "external_identifiers",
                      "created_at", "created_by", "updated_at", "updated_by", "verified_at", "verified_by"]
    for entity in entities:
        emit(insert("kb_entities", entity_columns, [
            sql(entity["id"]), sql(entity["code"]), sql(entity["entity_type"]), sql(entity["family_code"]),
            sql(entity["name_fa"]), sql(entity["name_en"]), sql(entity["slug"]), sql(entity["aliases"]),
            "NULL", "NULL", sql("fa"), sql(entity["properties"]), sql("approved"), sql("unassessed"),
            sql("active"), sql("public"), "1", sql(entity["external"]), sql(entity["created_at"]),
            sql(SEED_ACTOR), sql(entity["updated_at"]), sql(SEED_ACTOR), sql(entity["verified_at"]),
            sql(entity["verified_by"]),
        ]))

    emit("")
    emit("-- 6.2) زیرنوع‌ها (kb_entity_subtypes) — نوع ویراستاریِ ریزتر از نوع هستی‌شناختی")
    subtype_count = 0
    for entity in entities:
        subtype = SUBTYPE_BY_TAG.get(entity["tag"])
        if subtype:
            subtype_count += 1
            emit(insert("kb_entity_subtypes", ["entity_code", "subtype_code", "note"], [
                sql(entity["code"]), sql(subtype), sql(entity["properties"]["editorial"]["content_type"]),
            ]))

    emit("")
    emit("-- 6.3) روابط (kb_relations) — مستخرج از فیلدهای theorists و related داسیه‌های تأییدشده")
    person_index = collections.defaultdict(set)
    card_index = collections.defaultdict(set)
    for entity in entities:
        if entity["entity_type"] == "PERSON":
            names = [entity["name_fa"], entity["name_en"]]
            target = person_index
        else:
            names = [entity["name_fa"], entity["name_en"], entity["raw"].get("title_fa"), entity["raw"].get("title_en")]
            names += entity["aliases"] or []
            target = card_index
        for name in names:
            for key in name_keys(name):
                target[key].add(entity["id"])

    def resolve(index, names, self_id):
        for name in names:
            for key in name_keys(name):
                matches = index.get(key, set()) - {self_id}
                if len(matches) == 1:
                    return next(iter(matches))
        return None

    relations = collections.OrderedDict()
    relation_stats = collections.Counter()
    for entity in entities:
        if entity["entity_type"] == "PERSON":
            continue
        for theorist in entity["content"].get("theorists") or []:
            if not isinstance(theorist, dict):
                continue
            person_id = resolve(person_index, [theorist.get("name_en"), theorist.get("name_fa")], entity["id"])
            if person_id is None:
                relation_stats["theorist_unmatched"] += 1
                continue
            role = theorist.get("role") or ""
            relation_type = "PROPOSED_BY" if any(hint in role for hint in PROPOSER_HINTS) else "RELATED_TO"
            key = (entity["id"], person_id, relation_type)
            if key not in relations:
                relations[key] = (clip(role, 500), entity["updated_at"])
                relation_stats[relation_type + "(person)"] += 1
        for related in entity["content"].get("related") or []:
            if not isinstance(related, dict):
                continue
            target_id = resolve(card_index, [related.get("name")], entity["id"])
            if target_id is None:
                relation_stats["related_unmatched"] += 1
                continue
            low, high = sorted((entity["id"], target_id))
            key = (low, high, "RELATED_TO")
            if key not in relations:
                relations[key] = (clip(related.get("relation"), 500), entity["updated_at"])
                relation_stats["RELATED_TO(card)"] += 1
    relation_columns = ["source_id", "target_id", "relation_type", "assertion_status", "asserted_by",
                        "extraction_confidence", "note", "weight", "status", "created_at", "updated_at"]
    for (source_id, target_id, relation_type), (note, stamp) in relations.items():
        emit(insert("kb_relations", relation_columns, [
            sql(source_id), sql(target_id), sql(relation_type), sql("under_review"), sql(SEED_ACTOR),
            "0.900", sql(note), "50", sql("active"), sql(stamp), sql(stamp),
        ]))

    emit("")
    emit("-- 6.4) فاکت‌ها (kb_entity_facets) — analysis_scale از سطح تحلیل کارت")
    facet_count = 0
    for entity in entities:
        level = (entity["raw"].get("level") or "").split("(")[0].strip()
        scale = SCALE_BY_LEVEL.get(level)
        if scale:
            facet_count += 1
            emit(insert("kb_entity_facets", ["entity_id", "facet_code", "facet_value_id", "sort_order", "created_at"], [
                sql(entity["id"]), sql("analysis_scale"),
                "(SELECT id FROM kb_facet_values WHERE facet_code='analysis_scale' AND code=%s)" % sql(scale),
                "0", sql(entity["updated_at"]),
            ]))

    emit("")
    emit("-- 6.5) منابع (kb_sources) و شواهد (kb_evidence) — از فیلدهای sources و studies")
    sources = collections.OrderedDict()
    evidence = []

    def source_id_for(citation, item):
        key = re.sub(r"\s+", " ", citation).strip().lower()
        if key not in sources:
            year = re.search(r"\((1[5-9]\d\d|20\d\d)[a-z]?\)", citation)
            language = (item.get("language") or "").strip()
            sources[key] = dict(
                id=len(sources) + 1,
                title=clip(citation, 500),
                year=int(year.group(1)) if year else None,
                doi=clip(item.get("doi"), 120),
                url=clip(item.get("url"), 500),
                language=LANGUAGE_CODES.get(language),
                bibliographic=collections.OrderedDict(citation=citation.strip(), language_label=language or None, cited_by=[]),
            )
        return sources[key]

    for entity in entities:
        for item in entity["content"].get("sources") or []:
            if isinstance(item, dict) and (item.get("citation") or "").strip():
                source = source_id_for(item["citation"], item)
                if entity["code"] not in source["bibliographic"]["cited_by"]:
                    source["bibliographic"]["cited_by"].append(entity["code"])
                    evidence.append((source["id"], entity["code"], "bibliographic_reference", None))
        for item in entity["content"].get("studies") or []:
            if isinstance(item, dict) and (item.get("citation") or "").strip():
                source = source_id_for(item["citation"], item)
                if entity["code"] not in source["bibliographic"]["cited_by"]:
                    source["bibliographic"]["cited_by"].append(entity["code"])
                evidence.append((source["id"], entity["code"], "empirical_study", (item.get("findings") or "").strip() or None))
    for source in sources.values():
        emit(insert("kb_sources", ["id", "kind", "title_fa", "year", "doi", "url", "language", "access_type", "bibliographic"], [
            sql(source["id"]), sql("OTHER"), sql(source["title"]), sql(source["year"]), sql(source["doi"]),
            sql(source["url"]), sql(source["language"]), sql("unknown"), sql(source["bibliographic"]),
        ]))
    for source_id, about_code, evidence_type, summary in evidence:
        emit(insert("kb_evidence", ["source_id", "about_code", "evidence_type", "evidence_summary", "direction",
                                    "extraction_method", "verification_status"], [
            sql(source_id), sql(about_code), sql(evidence_type), sql(summary), sql("neutral"),
            sql("ai_extraction"), sql("unverified"),
        ]))

    emit("")
    emit("-- 6.6) نسخه‌ها (kb_entity_versions) — نسخه‌ی 1 = محتوای تأییدشده")
    for entity in entities:
        snapshot = collections.OrderedDict(
            code=entity["code"], entity_type=entity["entity_type"], family_code=entity["family_code"],
            canonical_name_fa=entity["name_fa"], canonical_name_en=entity["name_en"], slug=entity["slug"],
            aliases=entity["aliases"], properties=entity["properties"], status_workflow="approved",
            status_scientific="unassessed", status_lifecycle="active", visibility="public",
        )
        reason = "seed از نسخه‌ی approved شماره‌ی %s ویراستاری (امتیاز %d)" % (entity["revision"][0], entity["score"])
        emit(insert("kb_entity_versions", ["entity_id", "version", "snapshot", "change_reason", "changed_by", "created_at"], [
            sql(entity["id"]), "1", sql(snapshot), sql(reason), sql(entity["verified_by"]), sql(entity["verified_at"]),
        ]))

    emit("")
    emit("-- 6.7) ممیزی (kb_audit_log)")
    for entity in entities:
        detail = collections.OrderedDict(
            editorial_document_id=entity["external"]["editorial_document_id"],
            approved_revision_id=int(entity["revision"][0]),
            quality_score=entity["score"],
            source_file=EDITORIAL_FILE.name,
        )
        emit(insert("kb_audit_log", ["entity_code", "action", "detail", "source", "created_at"], [
            sql(entity["code"]), sql("seed_import"), sql(detail), sql("editorial_seed"), sql(entity["verified_at"]),
        ]))

    emit("")
    emit("-- 6.8) پیوند به سایت (kb_entity_links)")
    for entity in entities:
        emit(insert("kb_entity_links", ["entity_id", "link_type", "link_id", "link_title", "note", "confidence",
                                        "created_by", "created_at"], [
            sql(entity["id"]), sql(entity["link_type"]), sql(entity["link_id"]), sql(entity["name_fa"]),
            "NULL", sql("verified"), sql(SEED_ACTOR), sql(entity["updated_at"]),
        ]))

    base_count = len(entities)
    derived_relations = build_derived(entities, sources, emit, insert, sql, clip, report)

    report["counts"] = collections.OrderedDict(
        kb_entities=len(entities),
        kb_entity_subtypes=subtype_count,
        kb_relations=len(relations) + len(derived_relations),
        kb_entity_facets=facet_count,
        kb_sources=len(sources),
        kb_evidence=len(evidence),
        kb_citations=0,
        kb_entity_versions=base_count + (len(entities) - base_count),
        kb_audit_log=base_count + (len(entities) - base_count),
        kb_entity_links=base_count,
    )
    report["entities_by_type"] = dict(collections.Counter(entity["entity_type"] for entity in entities).most_common())
    report["score_distribution"] = dict(
        sorted(collections.Counter(entity["score"] for entity in entities if "score" in entity).items())
    )
    report["relations"] = dict(relation_stats)

    views = [
        "",
        "-- " + "=" * 76,
        "-- بخش 7 — ویوهای نمایش برای سایت (مبدأ / نوع رابطه / مقصد)",
        "-- " + "=" * 76,
        "",
        "-- 7.1) افزودنیِ نمایشی: برچسب فارسیِ جهت معکوس (در الگوی پایه ذخیره نمی‌شد)",
        "ALTER TABLE kb_relation_types ADD COLUMN inverse_label_fa VARCHAR(200) NULL AFTER inverse_code;",
        "UPDATE kb_relation_types SET inverse_label_fa = CASE code",
    ]
    inverse_labels = {
        "ADDRESSES": "پاسخ‌گفته در",
        "AGGREGATED_INTO": "تجمیع‌کننده‌ی",
        "ANALYZES": "تحلیل‌شده توسط",
        "ANALYZED_IN": "تحلیل‌کننده‌ی",
        "ANSWERED_BY": "پاسخ‌دهنده به",
        "APPLIES_TO": "دارای کاربردِ",
        "AUTHORED_BY": "تألیف‌کننده‌ی",
        "BASED_ON": "مبنای",
        "CHALLENGED_BY": "به چالش می‌کشد",
        "CITES": "مورد استناد",
        "COLLECTED_USING": "به‌کاررفته برای گردآوری",
        "COLLECTS": "گردآوری‌شده توسط",
        "CONDUCTED_BY": "انجام‌دهنده‌ی",
        "CONTAINS_VARIABLE": "متغیرِ موجود در",
        "CRITICIZES": "نقدشده توسط",
        "DERIVED_FROM": "منبعِ اشتقاق",
        "DEVELOPED_BY": "توسعه‌دهنده‌ی",
        "DOCUMENTED_BY": "مستندکننده‌ی",
        "EDITED_BY": "ویراستارِ",
        "EDITION_OF": "دارای ویراستِ",
        "ESTIMATES": "برآوردشده توسط",
        "EXTENDS": "توسعه‌یافته توسط",
        "EXTRACTED_FROM": "دارای شاهدِ استخراج‌شده",
        "FORMULATED_BY": "صورت‌بندی‌کننده‌ی",
        "GOVERNS": "تحت نظارتِ",
        "GUIDED_BY": "هدایت‌کننده‌ی",
        "HAS_BRANCH": "شاخه‌ای از",
        "HAS_DIMENSION": "بُعدی از",
        "HAS_PARTICIPANT": "شرکت‌کننده در",
        "HAS_PROPOSITION": "گزاره‌ای از",
        "HAS_SUBFIELD": "زیرمجموعه‌ی",
        "IMPLEMENTED_THROUGH": "پیاده‌سازنده‌ی",
        "INCLUDED_IN": "شاملِ",
        "INDICATES": "سنجیده‌شده با",
        "INFLUENCED": "متأثر از",
        "INFLUENCED_BY": "تأثیرگذار بر",
        "IS_A": "دارای زیرنوع",
        "JUSTIFIED_BY": "توجیه‌کننده‌ی",
        "MEASURES": "سنجیده‌شده با",
        "MEMBER_OF": "دارای عضوِ",
        "MOTIVATED_BY": "انگیزه‌بخشِ",
        "OPERATIONALIZES": "عملیاتی‌شده توسط",
        "PART_OF": "شاملِ جزء",
        "PRODUCED_BY": "تولیدکننده‌ی",
        "PROPOSED_BY": "ارائه‌دهنده‌ی",
        "PUBLISHED_BY": "ناشرِ",
        "REFUTED_BY": "ردکننده‌ی",
        "REPLACED_BY": "جایگزین می‌کند",
        "REPLICATES": "تکرارشده توسط",
        "REPORTED_IN": "گزارش‌کننده‌ی",
        "REQUIRES": "مورد نیازِ",
        "SPECIFIED_BY": "مشخص‌کننده‌ی",
        "STUDIES": "مطالعه‌شده در",
        "SUPERSEDES": "جانشین‌شده توسط",
        "SUPPORTED_BY": "پشتیبانِ",
        "TESTED_IN": "آزمون‌کننده‌ی",
        "TESTS": "آزموده‌شده توسط",
        "TRANSLATED_BY": "مترجمِ",
        "TRANSLATION_OF": "دارای ترجمه",
        "USES": "استفاده‌شده توسط",
        "USED_IN": "استفاده‌کننده‌ی",
        "VALIDATED_BY": "اعتبارسنجِ",
        "VERIFIED_BY": "تأییدکننده‌ی",
    }
    for code, label in inverse_labels.items():
        views.append("  WHEN '%s' THEN '%s'" % (code, label))
    views += [
        "  ELSE NULL END",
        " WHERE inverse_code IS NOT NULL;",
        "",
        "DROP VIEW IF EXISTS v_kb_relation_edges;",
        "CREATE VIEW v_kb_relation_edges AS",
        "SELECT r.id AS relation_id,",
        "       s.code AS source_code, s.canonical_name_fa AS source_name, s.entity_type AS source_type,",
        "       r.relation_type AS relation_code, rt.label_fa AS relation_label_fa,",
        "       t.code AS target_code, t.canonical_name_fa AS target_name, t.entity_type AS target_type,",
        "       'forward' AS direction, r.note",
        "  FROM kb_relations r",
        "  JOIN kb_entities s ON s.id = r.source_id",
        "  JOIN kb_entities t ON t.id = r.target_id",
        "  LEFT JOIN kb_relation_types rt ON rt.code = r.relation_type",
        "UNION ALL",
        "SELECT r.id,",
        "       t.code, t.canonical_name_fa, t.entity_type,",
        "       rt.inverse_code, rt.inverse_label_fa,",
        "       s.code, s.canonical_name_fa, s.entity_type,",
        "       'inverse', r.note",
        "  FROM kb_relations r",
        "  JOIN kb_entities s ON s.id = r.source_id",
        "  JOIN kb_entities t ON t.id = r.target_id",
        "  JOIN kb_relation_types rt ON rt.code = r.relation_type",
        " WHERE rt.inverse_code IS NOT NULL;",
        "",
        "DROP VIEW IF EXISTS v_kb_relation_coverage;",
        "CREATE VIEW v_kb_relation_coverage AS",
        "SELECT rt.code AS relation_code, rt.label_fa AS relation_label_fa,",
        "       rt.allowed_source_types, rt.allowed_target_types, rt.inverse_code, rt.inverse_label_fa,",
        "       COUNT(r.id) AS relation_count",
        "  FROM kb_relation_types rt",
        "  LEFT JOIN kb_relations r ON r.relation_type = rt.code",
        " GROUP BY rt.code, rt.label_fa, rt.allowed_source_types, rt.allowed_target_types, rt.inverse_code, rt.inverse_label_fa;",
        "",
    ]

    pattern = PATTERN_FILE.read_text(encoding="utf-8").splitlines()
    start = next(index for index, line in enumerate(pattern) if line.startswith("CREATE DATABASE"))
    end = next(index for index, line in enumerate(pattern) if "پایان. دیتابیس" in line) - 1
    body = "\n".join(pattern[start:end])
    if body.count("resaname_kb_final") != 2:
        raise SystemExit("unexpected database name occurrences in pattern")
    body = body.replace("resaname_kb_final", "`%s`" % DB_NAME)
    body = body.replace("USE `%s`;" % DB_NAME, "USE `%s`;\nSET NAMES utf8mb4;" % DB_NAME)

    counts = report["counts"]
    bar = "-- " + "=" * 76
    header = [
        bar,
        "-- هسته‌ی دانش علمی رسانامه — %s" % DB_NAME,
        "-- ساختار و registries: عیناً از الگوی final_database.sql (15 جدول)",
        "-- محتوا: اسناد با امتیاز کیفی %d و بالاتر از %s" % (MIN_SCORE, EDITORIAL_FILE.name),
        "--   %d موجودیت / %d رابطه / %d فاکت / %d منبع / %d شاهد / %d لینک" % (
            counts["kb_entities"], counts["kb_relations"], counts["kb_entity_facets"],
            counts["kb_sources"], counts["kb_evidence"], counts["kb_entity_links"]),
        "-- این فایل با build_gap_gpt_db.py ساخته می‌شود؛ دستی ویرایش نشود.",
        "-- موتور: InnoDB / utf8mb4 / utf8mb4_unicode_ci",
        bar,
        "",
    ]
    section = [
        bar,
        "-- بخش 6 — داده‌ی محتوایی (اسناد ویراستاری با quality_score >= %d)" % MIN_SCORE,
        bar,
        "",
        "START TRANSACTION;",
        "",
    ]
    footer = [
        "",
        "COMMIT;",
        "",
    ]
    tail = [
        bar,
        "-- پایان. %s: 15 جدول + registries + محتوای امتیاز %d به بالا." % (DB_NAME, MIN_SCORE),
        bar,
        "",
        "SET FOREIGN_KEY_CHECKS=1;",
        "",
    ]
    OUTPUT_FILE.write_text(
        "\n".join(header + [body] + section + out + footer + views + tail), encoding="utf-8", newline="\n"
    )
    REPORT_FILE.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    return report


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    print(json.dumps(build(), ensure_ascii=False, indent=2))
