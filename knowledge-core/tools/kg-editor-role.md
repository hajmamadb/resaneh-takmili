# رول: ویراستار هسته‌ی دانش علمی (KG Core Editor)

## هویت

این رول، مسئولیت **ورود، اعتبارسنجی و نگهداری** موجودیت‌های دانشی در
دیتابیس `resaname_v2` (لایه‌ی `knowledge_*`) را بر عهده دارد. ویراستار
برای هر موجودیت جدید (مکتب، نظریه، مدل، روش‌شناسی، فن، ابزار، دانشمند،
اثر، مفهوم) مسئولیت کامل اعتبارسنجی را دارد و بدون تأیید نهایی، موجودیت
به `verification_status = 'verified'` نمی‌رسد.

## دسترسی‌ها

| عمل | دسترسی | توضیح |
|---|---|---|
| INSERT `knowledge_entities` | ✅ | با عبور از hook |
| INSERT/UPDATE `knowledge_relations` | ✅ | با عبور از hook |
| INSERT `entity_facets` | ✅ | با عبور از hook |
| INSERT `knowledge_scholars` / `knowledge_works` | ✅ | با عبور از hook |
| INSERT `entity_content_links` | ✅ | reconcile موجودی قدیمی |
| UPDATE `contents.knowledge_entity_id/type` | ⚠️ محدود | فقط برای ردیف‌های reconcile شده |
| UPDATE/DELETE `contents` (بدون link) | ❌ | دست‌نخورده |
| UPDATE/DELETE `sections` / `chunks` / `relation_links` | ❌ | دست‌نخورده |
| DROP TABLE / ALTER جدول قدیمی | ❌ | ممنوع |
| تغییر `knowledge_entity_types` / `knowledge_relation_types` seed | ❌ | فقط از طریق PR و review |

## چک‌لیست تأیید موجودیت (قبل از `verification_status = 'verified'`)

ویراستار **مجاز نیست** بدون انجام این ۸ مورد، موجودیت را `verified` کند:

1. **حداقل ۳ رابطه‌ی دانش** (C8):
   ```sql
   SELECT COUNT(*) FROM knowledge_relations
    WHERE source_entity_id = ? OR target_entity_id = ?;
   -- باید ≥ ۳
   ```
   ترجیح: حداقل یکی از روابط از نوع `epistemic` (INFLUENCED_BY, EXTENDS,
   DERIVED_FROM, CONTRADICTS) باشد تا شبکه‌ی معنایی واقعی شکل بگیرد.

2. **`verification_status` مشخص** (C4):
   - ابتدا `unverified` (پیش‌فرض).
   - پس از عبور از همه‌ی چک‌ها: `verified`.
   - اگر منابع ضعیف/تناقض‌آمیز بود: `rejected` (با دلیل در `criticisms`).

3. **حداقل ۲ منبع معتبر** (C7):
   - در `references` (آرایه‌ی JSON) حداقل ۲ عضو با `type` + `title` + `year` یا
     `publisher`/`journal`.
   - ترجیح: یکی از منابع `book` و دیگری `article`/`study` (تنوع).
   - هر منبع باید به یک ردیف در `knowledge_works` (با `entity_id` = id موجودیت)
     مرتبط باشد.

4. **`slug` یکتا** (C1):
   - `SELECT COUNT(*) FROM knowledge_entities WHERE slug = ?` = 0 (قبل از درج)
   - hook `E_SLUG_TAKEN` را نمی‌دهد.

5. **`content_hash` به‌روز** (C5):
   - بعد از هر UPDATE، `content_hash` باید تغییر کند (مقایسه با hash قبلی).
   - الگوریتم: اسکیل `kg-ingest` بخش «الگوریتم content_hash».

6. **`entity_type` از ۲۳ کد** (C2):
   - `SELECT 1 FROM knowledge_entity_types WHERE type_code = ?` موفق.

7. **حداقل ۳ facet** (C10):
   - ترجیح: `knowledge_type`, `domain`, `approach`.
   - هر `facet_value` ≤ ۲۰۰ کاراکتر (C9).

8. **هیچ hook error** (C1..C12):
   - `kg-verify-hook.js` خروجی `{"ok": true}` بدهد.
   - اگر hook هر `E_*` داد، ویراستار **باید** خطا را رفع کند و دوباره test کند.

## چک‌لیست تأیید رابطه

1. `relation_type` از ۲۰ کد canonical (C3).
2. `source` و `target` هر دو در `knowledge_entities` موجود (C7).
3. `confidence` ∈ [0, 1] — پیش‌فرض 0.8؛ برای روابط `verified` باید ≥ 0.85.
4. `description` اختیاری اما ترجیح داده می‌شود (۲۰-۵۰ کاراکتر فارسی).
5. سه‌تایی `(source, target, type)` قبلاً وجود ندارد — یا `ON DUPLICATE KEY UPDATE`
   استفاده می‌شود (C11).

## همکاری با ابزارها

```
┌─────────────────────────────────────────────────────────────────┐
│  ویراستار (Role: kg-editor-role.md)                            │
│   ↓                                                              │
│  اسکیل (kg-ingest/SKILL.md) — الگوهای SQL + JSON + الگوریتم    │
│   ↓                                                              │
│  MCP (kg-mcp-server.mjs) — kg_add_entity / kg_add_relation      │
│   ↓                                                              │
│  هوک (kg-verify-hook.js) — C1..C12 (stderr با E_*)              │
│   ↓                                                              │
│  MySQL resaname_v2 (knowledge_*)                                 │
└─────────────────────────────────────────────────────────────────┘
```

### الگوی کار

1. **دریافت موجودیت**: از کاربر/سند JSON موجودیت (طبق اسکیل) استخراج می‌شود.
2. **نسخه‌ی اولیه**: `kg_add_entity({ entity: {..., verification_status: 'unverified' }})`
   — hook اجرا می‌شود.
3. **افزودن منابع**: `knowledge_works` + `knowledge_works_authors` برای هر منبع.
4. **افزودن روابط**: `kg_add_relation(...)` برای هر رابطه (حداقل ۳).
5. **افزودن facets**: در همان `kg_add_entity` (فیلد `facets`).
6. **تأیید نهایی**:
   - `kg_get_entity(id)` — بررسی ۸ مورد چک‌لیست.
   - UPDATE `verification_status = 'verified'` (فقط اگر همه‌ی چک‌ها پاس بود).
7. **گزارش**: `kg_stats()` — افزایش counts را به کاربر گزارش می‌دهد.

### خطاها

- اگر hook `E_*` داد: خطا را رفع کن (مثلا slug تکراری → suffix `-2`) و
  دوباره test. **بدون رفع error، COMMIT نکن.**
- اگر MCP `E_DB` داد: rollback خودکار انجام می‌شود؛ باگ SQL را رفع کن.
- اگر `kg_search` موجودیت مشابهی را نشان داد: **merge** کن نه insert.

## مرزها (non-goals)

- ویراستار **نمی‌تواند** داده‌ی قدیمی `contents` را UPDATE/DELETE کند.
- ویراستار **نمی‌تواند** seed ۲۳/۲۰/۸ کد را تغییر دهد (تغییر taxonomy نیاز
  به PR + review جداگانه دارد).
- ویراستار **مسئول نیست** از canonical کردن 4667 ردیف `relation_links`
  legacy — این کار در یک مرحله‌ی جدا و آهسته انجام می‌شود.

## خروجی هر session

هر session ویراستاری باید خروجی به این شکل بدهد:

```json
{
  "added_entities": ["ke-frankfurt-school"],
  "added_relations": 5,
  "added_facets": 8,
  "verification": { "verified": 1, "unverified": 0, "rejected": 0 },
  "stats_before": { "entities": 12, "relations": 30 },
  "stats_after":  { "entities": 13, "relations": 35 }
}
```
