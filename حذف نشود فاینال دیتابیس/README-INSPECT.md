# دیتابیس‌های ساخته‌شده در MySQL (سرور 127.0.0.1:3306، MySQL 8.0.31)

**تاریخ:** ۱۵/۱۱/۲۰۲۶

| دیتابیس | وضعیت | نقش |
|---|---|---|
| `resaname_kb_final` | **خالی — خام (دست‌نخورده)** | فقط ساختار + registries. این همان دیتابیس نهایی است؛ بعداً داده فقط از این ساختار پیروی می‌کند. |
| `resaname_kb_final_inspect` | **پر (seed شده)** | همان اسکیمای دقیق، با 771 سندِ `resaname_editorial` map شده — برای **بررسی شکاف محتوایی**. |

## محتوای `resaname_kb_final_inspect` (همه از داده‌ی واقعی، بدون ساختگی)

| جدول | رکورد | توضیح |
|---|---:|---|
| `kb_entities` | 771 | 731 کارت (MC-xxx) + 39 نظریه‌پرداز (th-x, PERSON) + 1 کتاب (WORK) |
| `kb_entity_facets` | 714 | فقط `analysis_scale` (از فیلد `level` کارت) |
| `kb_relations` | 23 | فقط `RELATED_TO` از ارجاع صریح `MC-xxx` در متن (unverified/needs_review) |
| `kb_entity_links` | 771 | provenance به `cards`/`theorists`/`library_resources` (verified) |
| `kb_sources` | 1 | کتاب «نظریه‌های ارتباطات» (Sorens & Tancred) — متصل به WORK با `work_id` |

### قرارداد seed
- `properties` = **کل `current_json`** سند + `quality_score` + `source` (table/id) + برای 183 رکوردِ 90+ فیلد `priority_90plus: true`
- `status_workflow`: approved→approved (178)، draft_ready→draft (593)
- `status_scientific`: همه `unassessed` (امتیاز ویرایشی ≠ اعتبار علمی)
- کارت بدون کد MC (17 عدد) → `code = source_id` (مثل `card-540`)
- نظریه‌پرداز → `code = id` (مثل `th-1`)

## گزارش شکاف (چه چیزی خالی مانده)
📄 `D:\کارخانه رسانامه\docs\kb-seed-gap-report.md`

خلاصه‌ی کلیدی:
- **فیلدهای «عمیق» کارت** (summary, main_problem, key_concepts, mechanism, assumptions, critiques, applications, history, evolution, studies, research_guide, …) برای ۹۸–۱۰۰٪ خالی‌اند — بزرگ‌ترین کار محتوایی.
- **12 از 13 بُعد فاکت** کاملاً خالی (فقط `analysis_scale` پر است).
- **روابط:** فقط 23 از 771 (بقیه باید ساخته شود).
- **21 نوع موجودیت** از 36 خالی‌اند (مثل RESEARCH_STUDY, FINDING, CONSTRUCT, PROPOSITION, DISCIPLINE).
- **39 نظریه‌پرداز** بدون رابطه‌ی ساختاریافته به نظریه‌هایشان (`main_theory` متن آزاد است).
- **اولویت 90+: 183 رکورد** (158 کارت + 25 نظریه‌پرداز) — با `priority_90plus: true` علامت‌گذاری شده‌اند.

## دستورالعمل بازبینی
```sql
-- کارت‌های 90+ یک نوع را با فیلدهایشان ببینید
SELECT code, canonical_name_fa, canonical_name_en, properties
FROM resaname_kb_final_inspect.kb_entities
WHERE entity_type='THEORY' AND JSON_EXTRACT(properties,'$.priority_90plus')=true
LIMIT 20;
```
اسکریپت‌های seed (قابل اجرا/بازگشت‌پذیر) — در همین پوشه، زیر `scripts\`:
- `kb_load_raw.py` → ساخت دیتابیس خام
- `kb_load_inspect.py` → ساخت دیتابیس inspect
- `kb_seed.py` → seed (idempotent: هر بار پاک و دوباره می‌ریزد)
- `kb_gap_report.py` → بازتولید گزارش شکاف
- `kb_verify.py` → نمونه‌گیری و کنترل صحت رکوردها

اجرا با: `python scripts\kb_seed.py` (و بقیه)
