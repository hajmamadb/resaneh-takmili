# دیتابیس فاینال هسته‌ی دانش علمی رسانامه
## راهنمای ساختار (README)

**موقعیت:** `D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\`
**فایل اسکیما:** `final_database.sql`
**وضعیت:** دیتابیس **خالیِ فاینال** — فقط ساختار + registries هستی‌شناسی؛ **بدون** داده‌ی محتوایی.

---

## ۱. این چیست؟

این دیتابیس **نسخه‌ی کامل‌تر** هسته‌ی دانش علمی رسانامه است که در یک دیتابیس **جدید و خالی** ساخته شده.
دیتابیس قدیمی (581 موجودیت / 384 رابطه / 1886 فاکت / 71 لینک) **در این دیتابیس نیست**؛ داده‌ی آن بعداً با یک
اسکریپتِ seed یک‌باره به این ساختار map می‌شود (استراتژی «ساخت سبز»).

**چرا خالی؟** registries (نوع/خانواده/رابطه/فاکت/واژگان) «**ساختار**» دیتابیس‌اند و اینجا پر شده‌اند.
«**داده**» (خودِ 581 موجودیت و روابطشان) عمداً وارد **نمی‌شود** تا دیتابیس خالی بماند و seed تمیز انجام شود.

---

## ۲. معماری ۴ لایه‌ای

```
لایه‌ی 1 — registries (تک منبع حقیقت، در کد app/Knowledge/*)
   ↓ seed
لایه‌ی 2 — این دیتابیس (final_database.sql)  ← شما این‌جا هستید
   ↓ seed داده‌ی قدیمی
لایه‌ی 3 — داده‌ی محتوایی (581/384/1886/71 — بعدا)
   ↓
لایه‌ی 4 — سایت v2 (فرم‌های نوع‌به‌نوع + صفحه‌ی هر موجودیت + جست‌وجو)
```

---

## ۳. جدول‌ها (15 جدول)

### گروه A — registries (ساختار؛ در این فایل پر شده‌اند)
| جدول | شرح | ردیف |
|---|---|---:|
| `kb_entity_families` | 8 خانواده‌ی هستی‌شناختی | 8 |
| `kb_entity_types` | 36 نوع موجودیت (با family) | 36 |
| `kb_relation_types` | فرهنگِ روابط canonical (با domain/range + inverse) | 81 |
| `kb_facet_dimensions` | 13 ابعاد فاکت (با value_kind) | 13 |
| `kb_facet_values` | واژگان کنترل‌شده‌ی مقادیر فاکت | ~60 |

### گروه B — هسته (موجودیت/رابطه/فاکت؛ خالی‌اند)
| جدول | شرح |
|---|---|
| `kb_entities` | موجودیت‌های دانش — قرارداد کامل (3 محور وضعیت، version، provenance) |
| `kb_entity_subtypes` | زیرنوع/طبقه‌بندیِ چندوالد (به‌جای آرایه‌ی JSON) |
| `kb_relations` | روابطِ بین‌موجودیتی — qualified (دوره اعتبار، شاهد، تأییدکننده) |
| `kb_entity_facets` | فاکت‌های موجودیت (ارجاع به `kb_facet_values`) |

### گروه C — منبع/استناد/شاهد (provenance؛ خالی‌اند)
| جدول | شرح |
|---|---|
| `kb_sources` | منابع علمی (SOURCE). اگر همان WORK است → `work_id` (جلوگیری از duplicate) |
| `kb_citations` | استنادها (به کدام بخش از منبع: صفحه/فصل/جدول/...) |
| `kb_evidence` | شواهد (قطعه‌ای که یک ادعا را supports/challenges/neutral می‌کند) |

### گروه D — نسخه‌بندی/ممیزی/پیوند (خالی‌اند)
| جدول | شرح |
|---|---|
| `kb_entity_versions` | نسخه‌های immutableِ هر رکورد (تصویر کامل + دلیل تغییر) |
| `kb_audit_log` | ردپای تغییرات |
| `kb_entity_links` | پیوند به محتوای دیتابیسِ اصلیِ سایت (cards/theorist/library/category) |

---

## ۴. 36 نوع موجودیت (به تفکیک خانواده)

### نظام فکری و پارادایمی — `THEORETICAL_SYSTEM`
`SCHOOL` (مکتب فکری) · `TRADITION` (سنت فکری) · `PARADIGM` (پارادایم)

### ساختارهای نظری و مفهومی — `KNOWLEDGE_STRUCTURE`
`THEORY` (نظریه) · `MODEL` (مدل) · `FRAMEWORK` (چارچوب نظری) · `HYPOTHESIS` (فرضیه) ·
`LAW` (قانون علمی) · `CONCEPT` (مفهوم) ·
**جدید:** `PROPOSITION` (گزاره علمی) · `CONSTRUCT` (سازه نظری) · `VARIABLE` (متغیر) · `INDICATOR` (شاخص)

### قلمروهای علمی و مناقشات — `SCIENTIFIC_DOMAIN`
`DISCIPLINE` (رشته علمی) · `SUBFIELD` (حوزه تخصصی) · `DISPUTE` (مناقشه علمی)

### نظام روش‌شناختی — `RESEARCH_METHODOLOGY`
`METHODOLOGY` (روش‌شناسی) · `METHOD` (روش تحقیق) · `APPROACH` (رویکرد) · `DESIGN` (طرح) ·
`STRATEGY` (استراتژی) · `TECHNIQUE` (فن) · `INSTRUMENT` (ابزار) · `SAMPLING` (نمونه‌گیری) ·
`ANALYSIS` (تحلیل داده) · `QUALITY` (معیار کیفیت) · `ETHICS` (اخلاق) · `PROTOCOL` (پروتکل)

### فعالیت و خروجی پژوهش — `RESEARCH_ACTIVITY` (همه‌ی 4 جدید)
`RESEARCH_PROBLEM` (مسئله) · `RESEARCH_QUESTION` (پرسش) · `RESEARCH_STUDY` (مطالعه) · `FINDING` (یافته)

### منابع و زیرساخت — `RESEARCH_RESOURCE`
`WORK` (اثر علمی) · `DATASET` (مجموعه‌داده) · `SOFTWARE` (نرم‌افزار)

### کنشگران علمی — `INTELLECTUAL_AGENT`
`PERSON` (اندیشمند و نظریه‌پرداز)

> **تصمیم (ADR):** `EVIDENCE` و `SOURCE` به‌جای نوع موجودیت، **جدول‌های ارجاعی** در گروه C شدند
> (چون ماهیتشان «ارجاع/نقل» است نه «مفهوم دانشی»). نتیجه: 36 نوع + 3 جدول ارجاعی.

---

## ۵. فرهنگِ روابط (81 رابطه‌ی canonical)

- **20 رابطه‌ی هسته** (همان داده‌ی فعلی) حفظ شدند تا seed بدون mapِ دوباره کار کند:
  `IS_A, PART_OF, BELONGS_TO, INFLUENCED_BY, INFLUENCED, CRITICIZES, EXTENDS, CONTRADICTS,
  RELATED_TO, APPLIES_TO, USES, MEASURES, ANALYZES, COLLECTS, DEVELOPED_BY, PROPOSED_BY,
  OPERATIONALIZES, TESTS, DERIVED_FROM, COMPARED_WITH`
- **61 رابطه‌ی افزوده** برای نوع‌های جدید و provenance (مثل `AUTHORED_BY, TESTED_IN, SUPPORTED_BY,
  CHALLENGED_BY, PRODUCED_BY, REPORTED_IN, CONDUCTED_BY, ADDRESSES, ANSWERED_BY, EXTRACTED_FROM, ...`).
- هر رابطه: `allowed_source_types` + `allowed_target_types` (domain/range) + `inverse_code` (نمایش معکوس) + `requires_evidence`.
- **`["*"]` = هر نوع.** معکوس‌ها **رکورد جدا ذخیره نمی‌شوند** (از `inverse_code` نمایش می‌شوند).

---

## ۶. فاکت‌ها (13)

| فاکت | value_kind | توضیح |
|---|---|---|
| `discipline` | ENTITY_REF | → DISCIPLINE (بعد از seed پر می‌شود) |
| `subfield` | ENTITY_REF | → SUBFIELD (بعد از seed پر می‌شود) |
| `theoretical_tradition` | ENTITY_REF | → TRADITION (بعد از seed پر می‌شود) |
| `time_frame` | TIME_PERIOD | دوره‌های تاریخی (4 مقدار پایه) |
| `approach` | STRING | رویکرد (7 مقدار پایه) |
| `epistemology` | STRING | معرفت‌شناسی (5 مقدار) |
| `ontology` | STRING | هستی‌شناسی (4 مقدار) |
| `data_type` | STRING | نوع داده (12 مقدار) |
| `research_context` | STRING | زمینه پژوهش (8 مقدار) |
| `geographic_region` | STRING | منطقه جغرافیایی (7 مقدار) |
| `analysis_scale` | STRING | **بهای قدیمی** — برای seedِ 1886 فاکتِ فعلی |
| `application_domain` | STRING | **بهای قدیمی** — برای seed |
| `qualifies_for` | STRING | **بهای قدیمی** — برای seed |

> **چرا 3 فاکتِ «بهای قدیمی»?** دیتابیس فعلی 1886 فاکت در `analysis_scale`/`application_domain`/`qualifies_for`
> دارد. برای اینکه seed بدون از دست رفتن داده انجام شود، این 3 فاکت نگه داشته شدند (با علامت legacy).
> در فاز بعد می‌توانید آن‌ها را soft-disable کنید.

---

## ۷. سه محور وضعیت (هرگز در یک فیلد ادغام نشوند)

```
status_workflow    : draft → in_review → approved → published → archived
status_scientific  : unassessed / supported / partially_supported / contested / refuted / not_applicable
status_lifecycle   : active / historical / superseded / deprecated / unknown
```
**«منتشرشده» ≠ «تأییدشده‌ی علمی».** این تمایز اصلِ طلایی است.

---

## ۸. کلیدها و ارجاع‌ها

- `kb_entities.id` = کلید فنی (PK, autoincrement).
- `kb_entities.code` = **شناسه‌ی پایدار و خوانا** (business key, unique). در slug و ارجاع‌های بیرونی.
- `kb_relations` به **`id`** (FK تمیز) ارجاع می‌دهد، نه `code`.
- `kb_sources.work_id` → اگر منبع همان WORK است، به همان رکورد وصل می‌شود (duplicate نمی‌سازد).

---

## ۹. نسخه‌بندی و منشأ

- **`kb_entity_versions`**: هر ویرایش مهم، یک سطر immutable (تصویر کامل + دلیل + عامل).
- **`kb_audit_log`**: ردپای همه‌ی تغییرات.
- **`extraction_confidence`** (روی رابطه و شاهد): اطمینانِ **استخراج** است، **نه** اعتبار علمی. دو امتیاز جدا.

---

## ۱۰. نحوه‌ی ساخت

```bash
mysql -u <user> -p < "D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\final_database.sql"
```
دیتابیس `resaname_kb_final` ساخته می‌شود با 15 جدول + registriesِ پر.

> اگر سرور MySQL ندارد یا نسخه‌ی متفاوت دارد: فقط نام دیتابیس و `JSON_ARRAY(...)` (MySQL 5.7+) را
> در صورت نیاز با `JSON'["*"]'` جایگزین کنید.

---

## ۱۱. نحوه‌ی seedِ داده‌ی قدیمی (قدم بعدی — هنوز انجام نشده)

اسکریپتِ seed (پیشنهادی: `php bin/kb.php seed --target=resaname_kb_final`) باید:
1. 581 موجودیتِ قدیمی را بخواند → `kb_entities` جدید (map: `abstract`→`canonical_name_fa`/`summary`؛
   `status` قدیمی → 3 محور جدید).
2. 384 رابطه را بخواند → `kb_relations` جدید (هر رابطه با domain/range validate شود؛ ناسازگارها
   در **گزارش** بیایند، نه delete).
3. 1886 فاکتِ متن‌آزاد را به `kb_facet_values` نگاشت کند (همسان‌سازی — **پرحجم‌ترین کار**؛ انسانی + کمک AI + بازبینی).
4. 71 لینک را به `kb_entity_links` (بدون تغییر).
5. خروجی: یک seed deterministic + **گزارش انطباق**.

---

## ۱۲. تصمیمات ADR (قفل‌شده در این ساختار)

| # | تصمیم |
|---|---|
| ADR-1 | کلید: `id` (PK) + `code` (business key)؛ روابط به `id`. |
| ADR-2 | `EVIDENCE`/`SOURCE` = **جدول ارجاعی** (نه نوع موجودیت). |
| ADR-3 | فاکت‌ها **کنترل‌شده** (`kb_facet_values`)؛ 3 فاکتِ legacy برای seed نگه داشته شد. |
| ADR-4 | 8 نوع جدید دانشی در `kb_entities`؛ پر کردن داده + UI فازبندی (A: STUDY/FINDING/QUESTION/PROBLEM — B: PROPOSITION/CONSTRUCT/VARIABLE/INDICATOR). |

---

## ۱۳. آنچه در این نسخه **نیست** (فاز 2)

نوع‌های اختیاری که هنوز به عنوان Entity Type ساخته **نشده‌اند** (نیاز واقعی‌شان باید اثبات شود):
`INSTITUTION, JOURNAL, CONFERENCE, CODEBOOK, RESEARCH_GROUP, RESEARCH_PROJECT, RESEARCH_REPORT,
CRITIQUE, ARGUMENT, POPULATION, SAMPLE, STATISTICAL_TEST, ALGORITHM, INSTRUMENT_VERSION,
CONCEPTUAL_FRAMEWORK, CORPUS, RESEARCH_TOPIC, SCIENTIFIC_EVENT`.
(خانواده‌ی `SCIENTIFIC_ARGUMENTATION` برای `ARGUMENT` رزرو شده و خالی است.)

---

## ۱۴. فایل‌های مرتبط

| فایل | نقش |
|---|---|
| `final_database.sql` (این پوشه) | اسکیما + registries (ساخت) |
| `app/Knowledge/EntityTypes.php` | registry نوع (باید 36 نوع + family را بازتاب دهد) |
| `app/Knowledge/EntityFamilies.php` | **جدید** — registry خانواده |
| `app/Knowledge/EntitySchemas.php` | **جدید** — schema فیلدیِ هر نوع (properties) |
| `app/Knowledge/RelationTypes.php` | registry رابطه (باید domain/range + inverse را بازتاب دهد) |
| `app/Knowledge/FacetTypes.php` | registry فاکت |
| `app/Knowledge/ControlledVocab.php` | **جدید** — واژگان کنترل‌شده |
| `app/Knowledge/EntitySchemaValidator.php` | **جدید** — اعتبارسنج |
| `docs/RM-KCORE-ONTOLOGY-SPEC.md` | سند اصلی |
| `docs/RM-KCORE-ONTOLOGY-SPEC-review-v2-greenfield.md` | بازبینیِ ساخت سبز |

> **یادآوری:** `final_database.sql` یک **بازتاب (mirror)** از registries است. «تک منبع حقیقت» کد است؛
> هر تغییری اول در `app/Knowledge/*` و بعد (با ابزار/اسکریپت) در این اسکیما اعمال شود تا drift نشود.

---

## ۱۵. دیتابیس `gap-gpt-db-resanameh-irfable` (ساخته‌شده)

نسخه‌ی **پر‌شده**ی همین الگو: ساختار و registries عیناً از `final_database.sql`، و محتوا فقط از
اسنادِ ویراستاریِ دارای `quality_score >= 90` در `resaname_editorial-final-20261115-1926.sql`.

| فایل | نقش |
|---|---|
| `gap-gpt-db-resanameh-irfable.sql` | اسکریپت کامل ساخت (اسکیما + registries + محتوا) |
| `gap-gpt-db-resanameh-irfable-report.json` | گزارش شمارش‌ها، توزیع امتیاز و موارد رد‌شده |
| `build_gap_gpt_db.py` | سازنده‌ی deterministic (منبع حقیقتِ تولید) |
| `verify_gap_gpt_db.py` | بررسی ساختاری پیش از ایمپورت |
| `RELATION-MODEL.md` | نگاشت ۱۹ الگوی رابطه‌ی درخواستی + وضعیت پوشش داده |

**محتوا:** 1261 موجودیت (663 مفهوم، 264 اثر، 123 زیرحوزه، 106 نظریه، 31 حوزه، 30 مدل، 21 شخص،
10 چارچوب، 5 پارادایم، 4 فرضیه، 3 روش، 1 مکتب) · 2396 رابطه · 157 فاکت · 371 منبع · 648 شاهد.

**دو لایه‌ی محتوا:**
- لایه‌ی ۱ (۱۷۸ موجودیت): مستقیم از اسناد ویراستاری — نظریه/مدل/شخص/چارچوب/فرضیه/روش/مفهوم/مکتب/پارادایم.
- لایه‌ی ۲ (۱۰۸۳ موجودیت مشتق): از `field`، `card.paradigm`، `key_concepts` و `sources` همان داسیه‌ها
  (حوزه، زیرحوزه، پارادایم، مفهوم، اثر علمی) با `created_by='seed:derived'`.

**نگاشت:** هر سند ویراستاری → یک `kb_entities` (نسخه‌ی `approved` در `properties` و `kb_entity_versions`)،
`theorists`/`related` → `kb_relations`، `level` → فاکت `analysis_scale`، `sources`/`studies` → `kb_sources` + `kb_evidence`.

**نمایش سایت:** ویو `v_kb_relation_edges` هر رابطه را در دو جهت (اصلی + معکوس با برچسب فارسی) می‌دهد؛
ستون `inverse_label_fa` در بخش ۷ به رجیستری اضافه شده تا «نقدشده توسط» و مانند آن قابل نمایش باشد.

```bash
python build_gap_gpt_db.py
mysql -u root -p < gap-gpt-db-resanameh-irfable.sql
```
