---
name: kg-ingest
description: >
  ورود و ثبت موجودیت‌های دانش علمی (مکتب، نظریه، مدل، روش‌شناسی، فن، ابزار، فرضیه،
  مفهوم، دانشمند، اثر) به هسته‌ی دانش‌نمای resaname_v2 (جدول‌های knowledge_*).
  هر گاه کاربر بخواهد «یک مکتب/نظریه/روش/ابزار/دانشمند/اثر را به هسته‌ی دانش
  اضافه کن»، «موجودیت دانشی ثبت/وارد کن»، «روابط دانش بساز»، «facet/بُعد اضافه کن»
  یا «کریجستری/ingest دانش‌نامه» بگوید، این اسکیل را بار کن. الگوی SQL، الگوی JSON
  ورودی، الگوریتم content_hash و چک‌لیست اعتبارسنجی را می‌دهد.
---

# ورود به هسته‌ی دانش (KG Ingest)

این اسکیل، دستورالعمل ثبت **موجودیت‌های دانشی** در دیتابیس `resaname_v2` است
(اسکیمای `knowledge-core/kg_schema.sql`). همه‌چیز بر پایه‌ی جداول لایه‌ی دانشی:

- `knowledge_entities` — موجودیت دانشی با ۲۲ فیلد استاندارد
- `knowledge_relations` — روابط دانش (IS_A, EXTENDS, ...)
- `entity_facets` — بُعد‌های طبقه‌بندی (۸ `facet_key`)
- `knowledge_scholars` / `knowledge_works` / `knowledge_works_authors` — دانشمندان و آثار
- `entity_content_links` — reconcile موجودیت دانشی ↔ مدخل `contents`

## اصول سفت‌وسخت

1. **تنها `knowledge_*` را لمس کن.** هیچ UPDATE/DELETE روی `contents`,
   `sections`, `relation_links`, `chunks` مجاز نیست. اتصال به `contents` فقط از
   طریق ستون‌های nullable جدید (`knowledge_entity_id` / `knowledge_entity_type`)
   یا `entity_content_links` — و ترجیحاً با درج ردیف جدید، نه تغییر ردیف قدیمی.
2. **هر موجودیت باید ≥ ۳ رابطه‌ی دانش و ≥ ۲ منبع (references) داشته باشد** تا
   `verification_status` بتواند `verified` شود (قانون رول ویراستار).
3. **هر درج/به‌روزرسانی باید از hook `kg-verify-hook.js` عبور کند** و فقط اگر
   خروجی hook clean بود، ترمینال/سازنده تأیید می‌کند.
4. **`content_hash` باید محاسبه شود** (الگوریتم در پایین) و در هر به‌روزرسانی
   تغییر کند تا تغییرات قابل‌ردیابی باشند.

## الگوریتم content_hash

`content_hash` = SHA-256 (hex, ۶۴ کاراکتر) روی یک **canonical string**:

```
sha256(
  entity_type
  + "|" + title_fa
  + "|" + title_en
  + "|" + slug
  + "|" + abstract
  + "|" + description
  + "|" + historical_background
  + "|" + philosophical_foundations
  + "|" + key_propositions
  + "|" + key_figures
  + "|" + origin_period
  + "|" + geographical_origin
  + "|" + related_disciplines
  + "|" + applications
  + "|" + strengths
  + "|" + limitations
  + "|" + criticisms
  + "|" + references
  + "|" + status
)
```

نویسندگان NULL را به string خالی تبدیل می‌کنند؛ ترتیب فیلدها دقیقاً بالا (مطابق
ترتیب ستون‌های `knowledge_entities`). در Node:

```js
import { createHash } from 'node:crypto';
const h = createHash('sha256');
for (const v of fields) h.update(String(v ?? '') + '|');
const content_hash = h.digest('hex');
```

## الگوی JSON برای ورودی (entity)

هر موجودیت یک JSON به این شکل است — یا مستقیم به `kg_add_entity` (MCP) داده
می‌شود یا در SQL ترجمه می‌شود. فیلدهای **الزامی** علامت `*` دارند.

```json
{
  "id": "ke-frankfurt-school",
  "title_fa": "مکتب فرانکفورت",
  "title_en": "Frankfurt School",
  "slug": "frankfurt-school",
  "entity_type": "SCHOOL",
  "parent_id": null,
  "abstract": "مکتب فکری انتقادی تأسیس‌شده در ۱۹۲۳ در مؤسسه‌ی پژوهش اجتماعی فرانکفورت…",
  "description": "مطالعه‌ی انتقادی (critical theory) به‌عنوان چارچوبی برای تحلیل جامعه‌شناختی…",
  "historical_background": "پس از بحران ۱۹۲۹…",
  "philosophical_foundations": "مارکسیسم، هگل، ویکتور یاسپرس…",
  "key_propositions": [
    {"id": "kp1", "text": "جوامع صنعتی پیشرفته به‌جای آزادی، انضباط ایجاد می‌کنند", "confidence": 0.9}
  ],
  "key_figures": "مکس آدورنو، تئودور آدورنو (Adorno)، هابرماس",
  "origin_period": "1923-1969",
  "geographical_origin": "آلمان (فرانکفورت)",
  "related_disciplines": ["sociology", "philosophy", "cultural-studies"],
  "applications": "تحلیل رسانه‌ی جمعی، نقد فرهنگ",
  "strengths": "بین‌رشته‌ای، عمق تئوریک",
  "limitations": "گرایش ایدئالیستی، دوری از روش‌های کمّی",
  "criticisms": "تقلیل‌گرایی فرهنگی",
  "references": [
    {"type": "book", "author": "Adorno & Horkheimer", "title": "Dialectic of Enlightenment",
     "year": 1944, "publisher": "Verso (reprint 1972)", "language": "en"},
    {"type": "article", "author": "Habermas", "title": "Theorie der gesellschaftlichen Kommunikation",
     "year": 1985, "publisher": "Frankfurt: Suhrkamp", "language": "de"}
  ],
  "status": "active",
  "verification_status": "unverified",
  "facets": {
    "knowledge_type": "school",
    "domain": "cultural-studies",
    "approach": "qualitative",
    "theoretical_tradition": "critical-theory",
    "data_type": "text",
    "objective": "interpretive",
    "analysis_scale": "macro",
    "application": "media-analysis"
  }
}
```

قیدها (از اسکیما):

| فیلد | نوع DB | یادداشت |
|---|---|---|
| `id` | VARCHAR(40) PK | `ke-` یا `ent-` + slug انگلیسی کوچک |
| `title_fa` | VARCHAR(500) NOT NULL | |
| `title_en` | VARCHAR(500) | اختیاری |
| `slug` | VARCHAR(200) UNIQUE | فقط `[a-z0-9-]`، بدون Farsi؛ یکتا در جدول |
| `entity_type` | VARCHAR(40) NOT NULL | **باید یکی از ۲۳ کد** `knowledge_entity_types.type_code` باشد (FK RESTRICT) |
| `parent_id` | VARCHAR(40) | self-FK به `knowledge_entities.id` (hierarchy: مکتب→سنت→نظریه) |
| `status` | VARCHAR(20) | `draft` | `active` | `archived` | `superseded` |
| `verification_status` | VARCHAR(20) | `unverified` | `verified` | `rejected` (حداقل مشخص شود) |
| `content_hash` | CHAR(64) | الگوریتم بالا |

## الگوریتم slug

```
slug = to_ascii(title_en or transliterate(title_fa))
       .toLowerCase()
       .replace(/[^a-z0-9]+/g, '-')
       .replace(/^-+|-+$/g, '')
       .slice(0, 200)
```

مثال‌ها: `فرانکفورت` → `frankfurt`، `فرهنگ‌پژوهی انتقادی` → `critical-culture-studies`.
اگر slug تکراری شد، hook `E_SLUG_TAKEN` می‌دهد؛ باید suffix مثل `-2` اضافه شود.

## الگوی SQL برای درج موجودیت

```sql
USE resaname_v2;
START TRANSACTION;

INSERT INTO `knowledge_entities` (
  `id`, `title_fa`, `title_en`, `slug`, `entity_type`, `parent_id`,
  `abstract`, `description`, `historical_background`, `philosophical_foundations`,
  `key_propositions`, `key_figures`, `origin_period`, `geographical_origin`,
  `related_disciplines`, `applications`, `strengths`, `limitations`, `criticisms`,
  `references`, `status`, `verification_status`, `content_hash`
) VALUES (
  'ke-frankfurt-school',
  'مکتب فرانکفورت',
  'Frankfurt School',
  'frankfurt-school',
  'SCHOOL',
  NULL,
  'مکتب فکری انتقادی…',
  'مطالعه‌ی انتقادی…',
  'پس از بحران ۱۹۲۹…',
  'مارکسیسم، هگل…',
  '[{"id":"kp1","text":"…","confidence":0.9}]',
  'مکس آدورنو، هابرماس',
  '1923-1969',
  'آلمان (فرانکفورت)',
  '["sociology","philosophy"]',
  'تحلیل رسانه، نقد فرهنگ',
  'بین‌رشته‌ای',
  'گرایش ایدئالیستی',
  'تقلیل‌گرایی فرهنگی',
  '[{"type":"book","author":"Adorno & Horkheimer","title":"Dialectic of Enlightenment","year":1944,"publisher":"Verso","language":"en"},
    {"type":"article","author":"Habermas","title":"Theorie der gesellschaftlichen Kommunikation","year":1985,"publisher":"Suhrkamp","language":"de"}]',
  'active',
  'unverified',
  '9f8e7d6c5b4a3210fedcba9876543210fedcba9876543210fedcba9876543210'
) ON DUPLICATE KEY UPDATE
  title_fa = VALUES(title_fa),
  title_en = VALUES(title_en),
  abstract = VALUES(abstract),
  description = VALUES(description),
  historical_background = VALUES(historical_background),
  philosophical_foundations = VALUES(philosophical_foundations),
  key_propositions = VALUES(key_propositions),
  key_figures = VALUES(key_figures),
  origin_period = VALUES(origin_period),
  geographical_origin = VALUES(geographical_origin),
  related_disciplines = VALUES(related_disciplines),
  applications = VALUES(applications),
  strengths = VALUES(strengths),
  limitations = VALUES(limitations),
  criticisms = VALUES(criticisms),
  references = VALUES(references),
  status = VALUES(status),
  verification_status = VALUES(verification_status),
  content_hash = VALUES(content_hash);

-- Facets (در صورت وجود در JSON)
INSERT IGNORE INTO `entity_facets` (entity_id, facet_key, facet_value, sort_order) VALUES
  ('ke-frankfurt-school', 'knowledge_type',          'school',           1),
  ('ke-frankfurt-school', 'domain',                  'cultural-studies', 2),
  ('ke-frankfurt-school', 'approach',                'qualitative',      3),
  ('ke-frankfurt-school', 'theoretical_tradition',   'critical-theory',  4),
  ('ke-frankfurt-school', 'data_type',               'text',             5),
  ('ke-frankfurt-school', 'objective',               'interpretive',     6),
  ('ke-frankfurt-school', 'analysis_scale',          'macro',            7),
  ('ke-frankfurt-school', 'application',             'media-analysis',   8);

COMMIT;
```

## الگوی SQL برای روابط دانش

`knowledge_relations` یک جدول ۳-ستونی (PK تجمیعی `source+target+type`) است. `id`
یک شناسه‌ی یکتای VARCHAR(40) است (مثلاً `kr-` + hash ۶-تایی از سه‌تایی).

```sql
-- مثال: مکتب فرانکفورت «متأثر از» مکتب وین است
INSERT INTO `knowledge_relations`
  (`id`, `source_entity_id`, `target_entity_id`, `relation_type`,
   `description`, `confidence`, `verification_status`, `extracted_by`)
VALUES (
  'kr-1a2b3c',
  'ke-frankfurt-school',
  'ke-vienna-circle',
  'INFLUENCED_BY',
  'نقد مکتب فرانکفورت روی مکتب وین در منطق ارجاعی',
  0.9000,
  'verified',
  'kg-ingest@2026-11-10'
) ON DUPLICATE KEY UPDATE
  description = VALUES(description),
  confidence = VALUES(confidence),
  verification_status = VALUES(verification_status),
  extracted_by = VALUES(extracted_by);
```

قیدها:

- `source_entity_id` / `target_entity_id` → **باید** موجود باشند در
  `knowledge_entities.id` (FK سخت با `ON DELETE CASCADE`).
- `relation_type` → **باید** یکی از ۲۰ کد در `knowledge_relation_types.type_code`
  باشد (IS_A, PART_OF, BELONGS_TO, INFLUENCED_BY, INFLUENCED, CRITICIZES, EXTENDS,
  CONTRADICTS, RELATED_TO, APPLIES_TO, USES, MEASURES, ANALYZES, COLLECTS,
  DEVELOPED_BY, PROPOSED_BY, OPERATIONALIZES, TESTS, DERIVED_FROM, COMPARED_WITH).
  جدول soft-FK است، ولی hook سخت می‌گیرد.
- `confidence` DECIMAL(5,4) بین 0 و 1، پیش‌فرض 0.8000.
- `verification_status` پیش‌فرض `unverified`؛ `verified` فقط اگر ≥ ۲ منبع
  معتبر در references هر دو موجودیت وجود داشته باشد.

## الگوی SQL برای دانشمندان و آثار

```sql
-- دانشمند
INSERT INTO `knowledge_scholars` (
  `id`, `name_fa`, `name_en`, `slug`, `birth_year`, `death_year`,
  `nationality`, `affiliation`, `field`, `bio`, `known_for`,
  `content_id`, `verification_status`, `content_hash`
) VALUES (
  'sch-habermas',
  'یورگن هابرماس', 'Jürgen Habermas', 'jurgen-habermas',
  1929, NULL, 'آلمانی', 'مؤسسه‌ی پژوهش اجتماعی فرانکفورت',
  'فلسفه‌ی اجتماعی، نظریه‌ی عمل ارتباطی',
  '…', 'نظریه‌ی عمل ارتباطی (1981)',
  'ct-habermas',  -- content_id (soft) — اختیاری
  'verified',
  '<sha256>'
) ON DUPLICATE KEY UPDATE
  name_fa = VALUES(name_fa), name_en = VALUES(name_en),
  birth_year = VALUES(birth_year), death_year = VALUES(death_year),
  nationality = VALUES(nationality), affiliation = VALUES(affiliation),
  field = VALUES(field), bio = VALUES(bio), known_for = VALUES(known_for),
  content_hash = VALUES(content_hash);

-- اثر
INSERT INTO `knowledge_works` (
  `id`, `title`, `title_en`, `work_type`, `publisher`, `journal`,
  `publication_year`, `isbn`, `doi`, `issn`, `source_url`, `citation_apa`,
  `entity_id`, `verification_status`, `content_hash`
) VALUES (
  'wk-theorie-der-kommunikation',
  'Theorie der gesellschaftlichen Kommunikation',
  'Theorie der gesellschaftlichen Kommunikation',
  'book', 'Suhrkamp', NULL, 1985, NULL, '10.1234/tgk.1985', NULL, NULL,
  'Habermas, J. (1985). Theorie der gesellschaftlichen Kommunikation. Frankfurt: Suhrkamp.',
  'ke-frankfurt-school', 'verified', '<sha256>'
) ON DUPLICATE KEY UPDATE
  title = VALUES(title), title_en = VALUES(title_en),
  work_type = VALUES(work_type), publisher = VALUES(publisher),
  publication_year = VALUES(publication_year), citation_apa = VALUES(citation_apa),
  content_hash = VALUES(content_hash);

-- نویسنده‌ی اثر
INSERT IGNORE INTO `knowledge_works_authors` (work_id, scholar_id, role, sort_order)
VALUES ('wk-theorie-der-kommunikation', 'sch-habermas', 'author', 1);
```

## الگوی SQL برای reconcile (موجودیت ↔ contents)

```sql
-- وقتی یک موجودیت دانشی به یک مدخلِ قدیمیِ contents نگاشت می‌شود:
INSERT INTO `entity_content_links` (entity_id, content_id, link_type, sort_order)
VALUES ('ke-frankfurt-school', 'ct-frankfurt-old', 'primary', 1)
ON DUPLICATE KEY UPDATE link_type = VALUES(link_type), sort_order = VALUES(sort_order);

-- (اختیاری) ستون‌های nullable روی contents — فقط برای ردیف‌های «جدید» پر می‌شود:
UPDATE `contents`
   SET `knowledge_entity_type` = 'SCHOOL',
       `knowledge_entity_id`   = 'ke-frankfurt-school'
 WHERE `id` = 'ct-frankfurt-old';
```

## ۲۳ کد entity_type (از `knowledge_entity_types`)

```
SCHOOL, TRADITION, PARADIGM, APPROACH, THEORY, MODEL, FRAMEWORK, HYPOTHESIS, LAW,
CONCEPT, METHODOLOGY, METHOD, DESIGN, STRATEGY, TECHNIQUE, INSTRUMENT, SAMPLING,
ANALYSIS, QUALITY, ETHICS, SOFTWARE, DISCIPLINE, SUBFIELD
```

## ۲۰ کد relation_type (از `knowledge_relation_types`)

```
IS_A, PART_OF, BELONGS_TO, INFLUENCED_BY, INFLUENCED, CRITICIZES, EXTENDS,
CONTRADICTS, RELATED_TO, APPLIES_TO, USES, MEASURES, ANALYZES, COLLECTS,
DEVELOPED_BY, PROPOSED_BY, OPERATIONALIZES, TESTS, DERIVED_FROM, COMPARED_WITH
```

`legacy_code` برای ۵ کد (extends, derived_from, related_to, theorist, applied_in)
موجود است؛ canonical key = `COALESCE(legacy_code, type_code)`.

## ۸ بُعد facet (از `entity_facet_keys`)

```
knowledge_type, domain, approach, theoretical_tradition,
data_type, objective, analysis_scale, application
```

## چک‌لیست اعتبارسنجی (قبل از COMMIT)

این همان چک‌هایی است که hook `kg-verify-hook.js` اجرا می‌کند؛ اگر hook `OK`
نزد، **مجاز نیست COMMIT کنی**:

- [ ] **C1 — slug یکتا**: `SELECT 1 FROM knowledge_entities WHERE slug = ?` خالی است.
- [ ] **C2 — entity_type معتبر**: `SELECT 1 FROM knowledge_entity_types WHERE type_code = ?` دارد.
- [ ] **C3 — relation_type معتبر** (برای هر رابطه):
  `SELECT 1 FROM knowledge_relation_types WHERE type_code = ?` دارد.
- [ ] **C4 — verification_status مشخص**: ∈ {`unverified`, `verified`, `rejected`}.
- [ ] **C5 — content_hash محاسبه‌شده**: ۶۴ کاراکتر hex؛ اگر به‌روزرسانی شد،
  تغییر کرده باشد (مقایسه با `SELECT content_hash FROM knowledge_entities WHERE id=?`).
- [ ] **C6 — FK‌های سخت**: `parent_id` (اگر نه NULL) در `knowledge_entities.id`
  هست؛ `source_entity_id`/`target_entity_id` در `knowledge_entities.id` هست.
- [ ] **C7 — حداقل ۲ منبع**: `references` آرایه‌ای با ≥ ۲ عضو معتبر (یا ۲ ردیف در
  `knowledge_works` متصل از طریق `entity_id`).
- [ ] **C8 — حداقل ۳ رابطه**: بعد از درج،
  `SELECT COUNT(*) FROM knowledge_relations WHERE source_entity_id=? OR target_entity_id=?` ≥ ۳.
- [ ] **C9 — facet_value ≤ 200**: `LENGTH(facet_value) <= 200` برای هر facet.
- [ ] **C10 — facet_key معتبر**: هر `facet_key` ∈ ۸ کد `entity_facet_keys`.
- [ ] **C11 — no duplicate relation**: سه‌تایی
  `(source_entity_id, target_entity_id, relation_type)` قبلاً وجود ندارد (یا
  `ON DUPLICATE KEY UPDATE` استفاده شده).
- [ ] **C12 — id format**: `id` مطابق `^[a-z0-9-]{6,40}$`.

## جریان پیشنهادی (agent-driven)

1. JSON موجودیت را از کاربر/سند استخراج کن.
2. `kg_search(slug)` در MCP بزن تا مطمئن شوی موجود نیست.
3. `kg_add_entity(entity_json)` را صدا بزن — MCP hook `kg-verify-hook.js` را
   اجرا می‌کند و در صورت `E_*` خطا برمی‌گردد.
4. اگر OK: `kg_add_relation(...)` برای هر رابطه و `kg_list_types()` برای
   اطمینان از واژگان.
5. در پایان: `kg_get_entity(id)` و `kg_stats()` برای گزارش نهایی.

## خطاهای hook (کدهای خطا)

| کد | معنی |
|---|---|
| `E_SLUG_TAKEN` | slug تکراری در `knowledge_entities` |
| `E_BAD_ENTITY_TYPE` | entity_type در ۲۳ کد نیست |
| `E_BAD_RELATION_TYPE` | relation_type در ۲۰ کد نیست |
| `E_BAD_VERIFICATION_STATUS` | verification_status خارج از ۳ مقدار |
| `E_BAD_CONTENT_HASH` | hash خالی/غیر-64 کاراکتری/غیر-hex |
| `E_HASH_MISMATCH` | hash به‌روزرسانی‌شده با hash فعلی در DB یکسان است (بدون تغییر) |
| `E_BAD_PARENT` | parent_id در `knowledge_entities` نیست |
| `E_MISSING_FK` | source/target در `knowledge_entities` نیست |
| `E_FACET_TOO_LONG` | facet_value > 200 |
| `E_BAD_FACET_KEY` | facet_key در ۸ کد نیست |
| `E_ID_FORMAT` | id مطابق regex نیست |
| `E_DUPLICATE_RELATION` | سه‌تایی relation قبلاً وجود دارد و ON DUPLICATE استفاده نشده |

## یادداشت‌های عملیاتی

- **MySQL 8.0** و `SET NAMES utf8mb4` برای هر session.
- **ترتیب درج**: اول entity، بعد relation، بعد facet.
- **idempotency**: همیشه `ON DUPLICATE KEY UPDATE` (نه `INSERT ... IGNORE`)
  برای entity/relation تا به‌روزرسانی‌ها ثبت شوند.
- **transaction**: هر موجودیت + روابط + facets در یک transaction.
- **لاگ‌نویسی**: هر درج موفق در جدول لاگ (اختیاری) یا فایل `.zcode/logs/kg-ingest.log`
  ثبت شود با `id`, `verification_status`, `content_hash`.
