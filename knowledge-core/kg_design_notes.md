# نکات طراحی اسکیمای هسته‌ی دانش (Knowledge Graph Core)

**تاریخ:** 2026-11-10
**مبنای فیزیکی:** دیتابیس `resaname_v2` (MySQL 8.0.31) — 10 جدول موجود
**فایل اجرایی:** `kg_schema.sql`
**هدف:** افزودن لایه‌ی «هسته‌ی دانش» (شبکه‌ی دانش + ۲۳ نوع موجودیت + ۲۰ رابطه +
طبقه‌بندی چندبعدی) **بدون لمس هیچ داده‌ی موجود** (۸۴۰ contents / ۵۹۴۸ sections /
۴۶۶۷ relation_links / ۱۱۳۶۸ chunks).

---

## ۱. اصول کلی

| اصل | توضیح |
|---|---|
| **افزایشی (additive)** | فقط `CREATE TABLE IF NOT EXISTS` + `ALTER TABLE ADD COLUMN` (nullable) + seed با `INSERT ... ON DUPLICATE KEY UPDATE`. هیچ `UPDATE`/`DELETE` روی داده‌ی موجود انجام نمی‌شود. |
| **idempotent** | فایل را می‌توان هر چند بار اجرا کرد؛ seedها و ستون‌های جدید تکراری ایجاد نمی‌کنند (بررسی در `INFORMATION_SCHEMA` پیش از `ADD COLUMN`). |
| **مستقل از content_type** | `contents.content_type` (۳۳ نوع فعلی + ۴ نوع منبعی) دست‌نخورده می‌ماند. طبقه‌بندی دانشی ۲۳ نوعی در لایه‌ی جدا ثبت می‌شود. |
| **utf8mb4 / utf8mb4_unicode_ci** | هم‌خوانی کامل با `v2_schema.sql` (خط ۹–۱۱ و همه‌ی جداول). |
| **MySQL 8.0** | syntax استاندارد؛ بدون ویژگی خاص MariaDB. |

---

## ۲. جداول جدید و نقش هرکدام

| جدول | نقش | seed |
|---|---|---|
| `entity_types` | ۲۳ نوع موجودیت دانش (SCHOOL…SUBFIELD) + نگاشت ۱:۱ به `content_type_taxonomy.type_key` | ۲۳ ردیف |
| `knowledge_entity_types` | ۲۳ نوع طبقه‌بندی دانشی (لایه‌ی دوم، فیلتر/جست‌وجو) — ۱۳ همپوشان با taxonomy canonical می‌شوند | ۲۳ ردیف |
| `knowledge_relation_types` | ۲۰ رابطه‌ی دانش (IS_A…COMPARED_WITH) + نگاشت ۵ کد legacy به `relation_links` | ۲۰ ردیف |
| `entity_facet_keys` | ۸ بُعد طبقه‌بندی چندبعدی (سند، بخش ۱۸) | ۸ ردیف |
| `knowledge_entities` | موجودیت‌های دانش با ۲۲ فیلد استاندارد + verification/hash/timestamps | خالی |
| `knowledge_relations` | روابط میان موجودیت‌ها (PK تجمیعی source+target+type، مشابه `relation_links`) | خالی |
| `entity_facets` | طبقه‌بندی چندبعدی (entity_id, facet_key, facet_value) | خالی |
| `knowledge_scholars` | اندیشمندان/نظریه‌پردازان (لایه‌ی دانشی) | خالی |
| `knowledge_works` | آثار علمی بنیادین (لایه‌ی دانشی) | خالی |
| `knowledge_works_authors` | نویسنده‌ی اثر (چندبه‌چند با `knowledge_scholars`) | خالی |
| `entity_content_links` | reconcile: موجودیت دانش ↔ مدخل `contents` | خالی |

### چرا دو جدول `entity_types` و `knowledge_entity_types`؟

سند ۹۳۰ خطی (بخش ۱۵) و تحلیل نقشه‌برداری هر دو به همین نتیجه می‌رسند:
**`contents.content_type` دو نقش دارد** — (الف) نوع دانش (theory/model/…) که با
۲۳ نوع جدید همپوشانی دارد، و (ب) نوع منبع (book/journal/article/theorist — ۹۴ ردیف)
که با ۲۳ نوع جدید بی‌ارتباط است. اگر ۲۳ نوع جدید مستقیم داخل `content_type` بریزیم:

- ۹۴ ردیف article/book/journal/theorist و منطق `section_catalog` (۳۸ ردیف که
  بر اساس `content_type='theorist'/'theory'` کار می‌کند) می‌شکنند.
- ۱۳ نوع همپوشان (theory, model, framework, paradigm, hypothesis, law, school,
  research_tradition, discipline, concept, methodology, method, technique,
  strategy) دوبرابر می‌شوند.

بنابراین:

- **`knowledge_entity_types`** = طبقه‌بندی دانشی ۲۳ نوعی که در `knowledge_entities`
  و `entity_facets` استفاده می‌شود (فیلتر/جست‌وجو). ۱۳ همپوشان با
  `content_type_key` به taxonomy canonical می‌شوند (DRY) و ۹ rename با
  `is_canonical=0` مشخص می‌شوند.
- **`entity_types`** = همان ۲۳ نوع اما با ستون `legacy_type_code` و
  `content_type_key` برای نگاشت ۱:۱ صریح و canonical کردن ۲۳ نوع موجودیت به
  ۳۳ نوع فعلی `content_type_taxonomy`. این دو جدول عملاً یک taxonomy را از دو
  زاویه نگه می‌دارند؛ می‌توان در آینده یکی را canonical کرد و دیگری را
  view/reference نگه داشت. (تصمیم باز — بخش ۷)

---

## ۳. reconcile با داده‌ی موجود (۴۶۶۷ relation_links)

کلید اصلی: **هیچ UPDATE روی `relation_links` نمی‌شود.**

### ۳-۱) واژگان رابطه (۲۰ کد) با ۵ کد legacy موجود

جدول `knowledge_relation_types` الگوی `content_type_taxonomy` را تکرار می‌کند:
PK = `type_code` (UPPER_SNAKE) + ستون `legacy_code` (UNIQUE, nullable).

| type_code | legacy_code (در relation_links) | domain |
|---|---|---|
| `EXTENDS` | `extends` | epistemic |
| `DERIVED_FROM` | `derived_from` | epistemic |
| `RELATED_TO` | `related_to` | core |
| `APPLIES_TO` | `applied_in` | usage |
| `DEVELOPED_BY` | `theorist` | provenance |
| بقیه ۱۵ کد (IS_A, PART_OF, …, COMPARED_WITH) | NULL | — |

**Canonical key برای نمایش/JOIN:**
```sql
COALESCE(krt.legacy_code, krt.type_code) AS normalized_key
```
یعنی ردیف‌های قدیمی `related_to` (۴۳۸۸) از طریق همان ردیف `RELATED_TO` canonical
می‌شوند؛ بدون اینکه یک بایت از آن‌ها تغییر کند.

### ۳-۲) ستون canonical جدید: `relation_links.rel_type_code`

- `VARCHAR(40) DEFAULT NULL` — روی ۴۶۶۷ ردیف موجود **NULL** می‌ماند.
- برای ردیف‌های **جدید** (پس از مهاجرت لایه‌ی اپلیکیشن) مقدار = `type_code` UPPER_SNAKE.
- این، PK تجمیعی `(source_id, relationship_type, target_id)` را نمی‌شکند و lock
  طولانی‌ای ایجاد نمی‌کند.

### ۳-۳) چطور ۴۶۶۷ ردیف قدیمی canonical می‌شوند (بدون UPDATE)

برای canonical کردن تدریجی، می‌توان داده‌ی **موازی** ساخت (نه UPDATE):
```sql
-- برای هر سه‌تایی قدیمی، یک ردیف با کد جدید (اگر canonical لازم شد)
INSERT INTO relation_links (id, source_type, source_id, relationship_type,
  target_type, target_id, rel_type_code, ...)
VALUES (CONCAT('new-', ...), 'content', s, krt.type_code, 'content', t,
        krt.type_code, ...)
ON DUPLICATE KEY UPDATE rel_type_code = krt.type_code;
```
پس از آن می‌توان ردیف‌های legacy را deprecated علامت زد. **این مرحله اختیاری و
آهسته است** و روی داده‌ی فعلی lock نمی‌گیرد. (تصمیم باز — بخش ۷)

### ۳-۴) محافظت از integrity (اختیاری، آینده)

چون MySQL 8.0.16+ CHECK را apply می‌کند، می‌توان (بعداً) CHECK یا trigger افزود تا
هر `relationship_type` واردشده یا `legacy_code` یا `type_code` موجود در
`knowledge_relation_types` باشد. در این اسکیمای اولیه **افزوده نشده** تا
`relation_links` دست‌نخورده بماند.

---

## ۴. reconcile اندیشمندان (knowledge_scholars vs contents/theorist)

| | `contents` (source_type/content_type = `theorist`) | `knowledge_scholars` |
|---|---|---|
| نقش | **مدخل شناسنامه‌ای** (۵۹ ردیف موجود، ۲۰ بخش) در `sections` | **موجودیت دانشی** در شبکه‌ی دانش |
| داده | ۵۹ ردیف، ۲۰ section_catalog | خالی (جدید) |
| کاربرد | نمایش مدخل کامل + RAG | اتصال به `knowledge_relations` و `knowledge_works_authors` |

**تصمیم:** هر دو نگه می‌مانند و با `knowledge_scholars.content_id` (soft, بدون FK)
+ `entity_content_links` reconcile می‌شوند. یک اندیشمند می‌تواند هم مدخل
شناسنامه‌ای داشته باشد (theorist) و هم موجودیت دانشی؛ `entity_content_links`
رابط «same_as/primary/related» میان آن‌ها را نگه می‌دارد.

---

## ۵. FKها و اینکه کدام سخت است و کدام soft

| FK / ارجاع | سخت یا soft | چرا |
|---|---|---|
| `knowledge_entities.parent_id` → خود | سخت (SET NULL) | hierarchy درونی؛ حذف والد نباید بقیه را حذف کند |
| `knowledge_entities.entity_type` → `knowledge_entity_types.type_code` | سخت (RESTRICT) | نوع باید همیشه valid باشد |
| `knowledge_relations.source/target_entity_id` → `knowledge_entities.id` | سخت (CASCADE) | حذف موجودیت، روابطش را هم حذف کند |
| `knowledge_relations.relation_type` | **soft (بدون FK)** | تا کدهای legacy/موجود آزاد بمانند و ۴۶۶۷ ردیف reconcile شوند |
| `entity_facets.entity_id` → `knowledge_entities.id` | سخت (CASCADE) | حذف موجودیت، facetsش را حذف کند |
| `entity_facets.facet_key` → `entity_facet_keys.facet_key` | سخت (CASCADE) | |
| `knowledge_works_authors.work_id/scholar_id` | سخت (CASCADE) | |
| `entity_content_links.entity_id/content_id` | سخت (CASCADE) | reconcile با contents |
| `knowledge_scholars.content_id` → `contents.id` | **soft (بدون FK)** | اختیاری + ۵۹ ردیف theorist دست‌نخورده بماند |
| `contents.knowledge_entity_type` / `knowledge_entity_id` | **soft (بدون FK)** | nullable + ۸۴۰ ردیف دست‌نخورده بماند |
| `entity_types.content_type_key` / `knowledge_entity_types.content_type_key` | **soft (بدون FK)** | نگاشت ۱:۱ که نباید taxonomy را قفل کند |

**منطق:** ارجاع‌های **درون‌لایه‌ی دانش** سخت هستند (integrity شبکه). ارجاع‌های
**بین لایه‌ی دانش و داده‌ی موجود** (contents, relation_links) soft/nullable‌اند
تا داده‌ی ۸۴۰/۴۶۶۷/۱۱۳۶۸ ردیف دست‌نخورده بماند.

---

## ۶. indexها

| index | جدول | کاربرد |
|---|---|---|
| `idx_ke_type`, `idx_ke_parent`, `idx_ke_status`, `idx_ke_vstatus` | `knowledge_entities` | فیلتر بر اساس نوع/والد/وضعیت |
| `idx_kr_target`, `idx_kr_type`, `idx_kr_status` | `knowledge_relations` | query شبکه (بر اساس target/type) |
| `idx_ef_facet_value`, `idx_ef_entity` | `entity_facets` | فیلتر چندبعدی + reverse lookup |
| `idx_contents_ke_type`, `idx_contents_ke_id` | `contents` (جدید) | فیلتر بر طبقه‌بندی دانشی + join به موجودیت |
| `idx_reltypecode` | `relation_links` (جدید) | query ردیف‌های canonical جدید |
| `uq_ke_slug`, `uq_scholar_slug`, `uq_kw_doi` | — | یکتایی (هر موجودیت/اندیشمند/اثر یک شناسه) |
| `uq_et_legacy`, `uq_krt_legacy` | — | یکتایی نگاشت legacy |

---

## ۷. فرض‌های باز / تصمیمات عقب‌افتاده

1. **دو جدول entity_types / knowledge_entity_types:** فعلاً هر دو seed شده‌اند.
   پیشنهاد: `knowledge_entity_types` را canonical نگه دارید (چون در
   `knowledge_entities.entity_type` به‌کار می‌رود) و `entity_types` را فقط
   reference/نگاشت ۱:۱ به taxonomy. یا در آینده یکی را view کنید.
2. **canonical کردن ۴۶۶۷ relation_links:** داده‌ی موازی (INSERT ON DUPLICATE)
   در نظر گرفته شد اما **در این اسکیمای اولیه اجرا نمی‌شود** تا داده‌ی موجود
   کاملاً دست‌نخورده بماند. مرحله‌ی جدا، آهسته و بدون lock.
3. **CHECK/trigger روی relation_links:** برای جلوگیری از درج کدهای ناشناخته،
   اختیاری و آینده (بعد از مهاجرت کامل اپلیکیشن به UPPER_SNAKE).
4. **نحوه‌ی نگاشت ۵۹ theorist موجود به knowledge_scholars:** ۵۹ ردیف theorist
   در `contents` هست؛ آیا هرکدام یک ردیف در `knowledge_scholars` می‌گیرد؟
   پیشنهاد: بله، با `content_id` به `contents.id` و یک ردیف در
   `entity_content_links` با `link_type='primary'`. این مهاجرت داده‌ای است و در
   این اسکیمای اولیه (که فقط ساختار + seed است) انجام نشده.
5. **22 فیلد standard در knowledge_entities:** سند ۲۱ فیلد + status = ۲۱ فهرست
   کرده؛ این اسکیمای اولیه ۲۱ فیلد استاندارد + `verification_status` +
   `content_hash` + `created_at`/`updated_at` دارد (مطابق الزام ۴). ستون‌های
   `key_propositions`/`key_figures`/`related_disciplines`/`applications`/`strengths`/
   `limitations`/`criticisms`/`references` به‌صورت TEXT (یا JSON در آینده) تعریف
   شده‌اند.
6. **نوع داده facet_value:** فعلاً `VARCHAR(200)`. اگر مقدارهای facet بلندتر از
   ۲۰۰ کاراکتر شوند، باید به `TEXT` تغییر کند (آزمایش نشد).
7. **id generation برای knowledge_entities:** `VARCHAR(40)` (هم‌اندازه با
   contents.id) — برای سازگاری و join ساده. فرمت پیشنهادی: `ent-<slug>` یا
   `ke-<seq>`.

---

## ۸. خلاصه‌ی اجرا (چک‌لیست)

```text
1. USE resaname_v2;
2. mysql … < kg_schema.sql          # همه‌ی جداول + ستون‌های جدید + seed
3. (اختیاری) canonical کردن تدریجی ۴۶۶۷ ردیف با داده‌ی موازی
4. (اختیاری) مهاجرت ۵۹ theorist به knowledge_scholars + entity_content_links
5. (اختیاری) CHECK/trigger برای واژگان رابطه
```

**نتیجه:** ۸۴۰ contents + ۵۹۴۸ sections + ۴۶۶۷ relation_links + ۱۱۳۶۸ chunks
**کاملاً دست‌نخورده**؛ ۱۱ جدول جدید + ۳ ستون جدید (nullable) روی `contents` و
`relation_links` + ۲۳+۲۳+۲۰+۸ ردیف seed.
