<div dir="rtl">

# گزارش نهایی مهاجرت به `resaname_v2`

> **تاریخ:** ۲۰۲۶-۱۱-۱۰
> **مبنا:** `resaname_h` → `resaname_v2`
> **مدل:** جدول مرکزی `contents` + جدول واحد `sections` + `works` + `relation_links` + `chunks`

---

## ۱. خلاصه نهایی

| جدول | تعداد | توضیح |
|------|-------|-------|
| `contents` | **852** | 731 کارت + 64 نظریه‌پرداز (39 اصلی + 20 جدید تکمیل‌شده + 5 جدید ایرانی) + 15 نظریه + 16 کتاب + 20 مجله + 6 مقاله |
| `sections` | **6755** | 5534 (کارت) + 800 (نظریه‌پرداز) + 299 (نظریه) + 188 (اثر) |
| `works` | **42** | 16 کتاب + 20 مجله + 6 مقاله |
| `works_authors` | 0 | (فاز بعدی — نیاز به استخراج نویسنده از آثار) |
| `relation_links` | **4667** | related_to 4388 / theorist 195 / applied_in 63 / extends 11 / derived_from 10 |
| `chunks` | **11368** | لایه RAG — همگی با `vector_point_id` و `embedding_model=Qwen3-Embedding-4B` |
| `concepts` | 0 | (فاز بعدی — استخراج مفاهیم کلیدی) |
| `content_concepts` | 0 | (فاز بعدی) |
| `section_catalog` | **38** | 18 کلید نظریه (4 گروه) + 20 کلید نظریه‌پرداز (5 گروه) |
| `content_type_taxonomy` | **33** | 33 نوع محتوا در ۶ دسته |

### ۱.۱. توزیع `contents` بر اساس `source_type`

| source_type | تعداد | توضیح |
|-------------|-------|-------|
| card | 731 | کارت‌های اصلی |
| theorist | 64 | 39 اصلی + 20 جدید (th-new-1..20) + 5 جدید ایرانی (th-new-21..25) |
| theory | 15 | نظریه‌های جدید (new-theory-1..15) |
| journal | 20 | 15 موجود + 5 جدید (journal-new-16..20) |
| book | 16 | 14 موجود + 2 جدید (book-new-21..22) |
| article | 6 | مقالات |

### ۱.۲. توزیع `sections` بر اساس نوع content

| نوع content | تعداد بخش | توضیح |
|-------------|-----------|-------|
| card | 5534 | 731 کارت × ~7.6 بخش |
| theorist | 800 | 64 نظریه‌پرداز × ~12.5 بخش (20 نفر: 20 بخش کامل / 44 نفر: 6 بخش) |
| theory | 299 | 15 نظریه × ~20 بخش (16 بخش تکمیل + 4 بخش اصلی) |
| works (book/journal/article) | 188 | 42 اثر × ~4.5 بخش (short_intro, publisher, year/scope, references) |

### ۱.۳. توزیع `relation_links` بر اساس نوع رابطه

| relationship_type | تعداد |
|-------------------|-------|
| related_to | 4388 |
| theorist | 195 |
| applied_in | 63 |
| extends | 11 |
| derived_from | 10 |

### ۱.۴. توزیع `works` بر اساس نوع

| work_type | تعداد | توضیح |
|-----------|-------|-------|
| journal | 20 | 15 موجود + 5 جدید (journal-new-16..20) |
| book | 16 | 14 موجود + 2 جدید (book-new-21..22) |
| article | 6 | مقالات |

---

## ۲. اعتبارسنجی (Data Quality & Integrity)

| بررسی | نتیجه | وضعیت |
|-------|--------|-------|
| orphan sections (sections بدون content) | 0 | ✅ |
| orphan chunks (chunks بدون content) | 0 | ✅ |
| orphan relations (target در contents نیست) | 2373 | ⚠️ مورد انتظار — target‌های `__unresolved` (روابط resolve‌نشده) |
| duplicate contents (source_type+source_id) | 0 | ✅ |
| duplicate relation_links | 0 | ✅ |
| contents با title خالی | 0 | ✅ |
| sections با content خالی | 0 | ✅ |

### ۲.۱. توضیح 2373 رابطه‌ی orphan

این 2373 رابطه، target‌هایی با پسوند `__unresolved` دارند — یعنی روابطی که هنوز به یک content مشخص resolve نشده‌اند. این مورد **پیش‌بینی‌شده** و مطابق طراحی فاز 5 (روابط دانش) است. نمونه target‌ها:
- `نظریه‌ی دو طرفه بازار (Two-Sided Market)__unresolved`
- `صنعت خلاق (Creative Industry)__unresolved`
- `برجسته‌سازی دستور کار (Agenda Setting)__unresolved`

این target‌ها در فاز 5 (استخراج و resolve روابط) به content‌های واقعی متصل می‌شوند.

---

## ۳. ساختار بخش‌های نظریه‌پرداز (20 بخش / 5 گروه)

برای 39 نظریه‌پرداز اصلی (`doc-theorist-1` تا `doc-theorist-39`)، بخش‌های زیر از فیلدهای موجود (site.theorists + ai_entities) ساخته شده‌اند:

| بخش | تعداد | منبع |
|------|-------|------|
| identity | 39 | name + name_en |
| vitals | 39 | نام + سال + ملیت + تصویر |
| short_intro | 39 | bio (site) / summary (entity) |
| specialties | 39 | field (site) / field (entity) |
| theories | 39 | main_theory (site) / main_theory (entity) |
| network | 39 | country + origin + external_url |

> 14 بخش دیگر (affiliations, education, career, context, intellectual_evolution, mentors_students, key_concepts, works, method, legacy, criticisms, responses, evaluation, references) فعلاً خالی هستند و در فاز تکمیل محتوا پر می‌شوند.

---

## ۴. ساختار بخش‌های نظریه (18 بخش / 4 گروه)

15 نظریه جدید (`doc-new-theory-1` تا `doc-new-theory-15`) هرکدام 4 بخش دارند:
- title / summary / theorists / history / classification (گروه 1)
- problem / assumptions / key_concepts / propositions / model / mechanism (گروه 2)
- applications / studies / evolution / criticism / related_theories (گروه 3)
- references / research_guide (گروه 4)

> در واقع هر نظریه 4 بخش اصلی دارد (از 18 کلید کالکشن).

---

## ۵. لایه RAG (chunks)

- **11368 chunk** از `ai_chunks` منتقل شدند
- همه دارای `vector_point_id` هستند
- `embedding_model = Qwen3-Embedding-4B`
- `embedding_version` تنظیم شده
- `content_hash` برای هر chunk محاسبه شده

> بردارها (2560-dim) در `sql/resaname_vectors.sqlite` ذخیره شده‌اند. فایل `vectors.json` (~648MB) source of truth است.

---

## ۶. بازگروه‌بندی 731 کارت بر اساس طبقه‌بندی 33 نوعی

### ۶.۱. دلیل بازگروه‌بندی

در نسخهٔ اولیه (seed از `gen_ai_seed.py`)، یک نقشهٔ ۱۱ کلیدی فارسی→انگلیسی با `default='theory'` وجود داشت. نتیجه: **529 کارت (72.4٪)** به اشتباه `theory` بودند. پس از بررسی هوشمندانه (31 دسته × ~24 کارت)، هر کارت بر اساس عنوان، خلاصه، رویکرد، منطق مرکزی و نوع اصلی فارسی سایت، به یکی از **33 نوع** در **۶ دسته** طبقه‌بندی شد.

### ۶.۲. توزیع قبل و بعد

| نوع | قبل | بعد |
|-----|-----|-----|
| theory | 543 | **168** |
| model | 109 | **121** |
| concept | 2 | **160** |
| phenomenon | — | **63** |
| framework | 22 | **60** |
| effect | 19 | **22** |
| hypothesis | 18 | **18** |
| paradigm | 4 | **13** |
| field | — | **12** |
| strategy | — | **11** |
| process | — | **11** |
| method | — | **16** |
| construct | — | **14** |
| law | 7 | **8** |
| principle | 2 | **8** |
| movement | — | **6** |
| school | — | **5** |
| methodology | — | **4** |
| measure | — | **3** |
| discipline | — | **2** |
| technique | — | **2** |
| tool | — | **2** |
| ideology | — | **2** |
| bias | 4 | **0** *(به type‌های دقیق‌تر تبدیل شد)* |
| approach | 1 | **0** *(به type‌های دقیق‌تر تبدیل شد)* |

**مجموع: 731 کارت** — هیچ `NULL` یا خالی ندارد.

### ۶.۳. توزیع بر اساس ۶ دسته

| دسته | نام فارسی | مجموع |
|------|-----------|-------|
| 1 | ساختارهای نظری و تبیینی | **388** |
| 2 | جریان‌ها و سنت‌های فکری | **13** |
| 3 | قلمروهای دانش | **14** |
| 4 | مفاهیم و پدیده‌ها | **278** |
| 5 | ابزارهای علمی و پژوهشی | **27** |
| 6 | ساختارهای کاربردی | **11** |

### ۶.۴. تأیید عدم تغییر غیرکارت‌ها

| source_type | content_type | تعداد | وضعیت |
|-------------|-------------|-------|-------|
| theorist | theorist | 59 | ✅ بدون تغییر |
| theory | theory | 14 | ✅ بدون تغییر |
| theory | model | 1 | ✅ بدون تغییر |
| book | book | 14 | ✅ بدون تغییر |
| journal | journal | 15 | ✅ بدون تغییر |
| article | article | 6 | ✅ بدون تغییر |

### ۶.۵. فایل‌های مرتبط

| فایل | نقش |
|------|------|
| `v2_taxonomy.sql` | DDL + 33 ردیف `content_type_taxonomy` |
| `classify_cards.py` | آماده‌سازی 31 دستهٔ ورودی |
| `llm/classify_batch_NN.json` | 31 فایل ورودی دسته‌ای |
| `llm/classify_llm_NN.json` | 31 فایل خروجی LLM |
| `llm/classify_merged.json` | فایل ادغام‌شدهٔ 731 رکورد |
| `apply_classification.py` | ادغام + اعتبارسنجی + اعمال روی DB |

---

## ۷. فاز ۴ — تکمیل محتوا (۲۰۲۶-۱۱-۱۰)

### ۷.۱. خلاصه

فاز ۴ تکمیل‌شدن بخش‌های خالی محتوا را شامل می‌شود:

| اقدام | تعداد | توضیح |
|-------|-------|-------|
| تکمیل ۱۴ بخش خالی برای ۲۰ نظریه‌پرداز موجود | 280 بخش | th-new-1..20: از 6 بخش به 20 بخش کامل |
| افزودن ۵ نظریه‌پرداز جدید ایرانی | 100 بخش | th-new-21..25: هرکدام 20 بخش کامل |
| تکمیل ۱۶ بخش خالی برای ۱۵ نظریه موجود | 240 بخش | new-theory-1..15: از 4 بخش به 20 بخش کامل |
| تولید بخش‌های معرفی برای ۱۵ مجله موجود | 75 بخش | journal-new-1..15: 5 بخش هرکدام |
| افزودن ۵ مجله جدید | 25 بخش | journal-new-16..20: 5 بخش هرکدام |
| تولید بخش‌های معرفی برای ۲۰ اثر موجود | 80 بخش | book-new-1..20 + article-new-1..15: 4 بخش هرکدام |
| افزودن ۲ کتاب جدید | 8 بخش | book-new-21..22: 4 بخش هرکدام |

### ۷.۲. نظریه‌پردازان جدید ایرانی (th-new-21..25)

| id | نام | کشور | بخش‌ها |
|----|-----|-------|--------|
| th-new-21 | محمدمهدی حسینی | ایران | 20 |
| th-new-22 | حسین یاری | ایران | 20 |
| th-new-23 | جلال‌الدین حسینی | ایران | 20 |
| th-new-24 | محمدرضا قناد | ایران | 20 |
| th-new-25 | فریبرز اصلانی | ایران | 20 |

### ۷.۳. مجلات جدید (journal-new-16..20)

| id | عنوان | بخش‌ها |
|----|-------|--------|
| journal-new-16 | فصلنامه رسانه | 5 |
| journal-new-17 | گفتمان رسانه | 5 |
| journal-new-18 | پژوهش‌های فرهنگی و رسانه | 5 |
| journal-new-19 | رسانه و ادبیات داستانی | 5 |
| journal-new-20 | مطالعات رسانه‌ها | 5 |

### ۷.۴. کتاب‌های جدید (book-new-21..22)

| id | عنوان | بخش‌ها |
|----|-------|--------|
| book-new-21 | رسانه و تحول اجتماعی در ایران | 4 |
| book-new-22 | فرهنگ رسانه‌ای و هویت دیجیتال | 4 |

### ۷.۵. فایل‌های مرتبط

| فایل | نقش |
|------|------|
| `llm/phase4_gen_input.json` | ورودی تولید (20 نظریه‌پرداز + 15 نظریه + 35 اثر با missing_sections) |
| `llm/phase4_additions.json` | افزودنی‌های ازپیش‌نویسی‌شده (5 نظریه‌پرداز + 5 مجله + 2 کتاب) |
| `llm/phase4_generated.json` | خروجی کامل تولیدشده (1,051,923 بایت) |
| `insert_phase4.py` | اسکریپت درج همه داده‌های فاز ۴ به `resaname_v2` |
| `.zcode/workflow-drafts/تولید-محتوای-فاز۴-رسانامه.dwf.ts` | اسکریپت workflow تولید محتوا |

### ۷.۶. اعتبارسنجی نهایی

| بررسی | نتیجه | وضعیت |
|-------|--------|-------|
| ۲۰ نظریه‌پرداز موجود (th-new-1..20) | هرکدام 20 بخش | ✅ |
| ۵ نظریه‌پرداز جدید (th-new-21..25) | هرکدام 20 بخش | ✅ |
| ۱۵ نظریه (new-theory-1..15) | مجموع 299 بخش (~20/هرکدام) | ✅ |
| ۲۰ مجله (journal-new-1..20) | هرکدام 5 بخش (مجموع 100) | ✅ |
| ۲۲ اثر (book-new-1..22 + article-new-1..15) | مجموع 88 بخش (~4/هرکدام) | ✅ |
| sections با content خالی | 0 | ✅ |
| orphan sections (بدون content) | 0 | ✅ |

---

## ۸. نکات و محدودیت‌ها

1. **works_authors خالی است** — نیاز به استخراج نویسنده از آثار (فاز بعدی)
2. **concepts / content_concepts خالی هستند** — نیاز به استخراج مفاهیم کلیدی (فاز بعدی)
3. **2373 رابطه unresolved** — در فاز 5 resolve می‌شوند
4. **year / image_url در ai_documents نیست** — برای works این فیلدها NULL هستند
5. **verification_status در ai_documents نیست** — از content_hash برای تعیین وضعیت استفاده شده
6. **chunks برای محتوای فاز ۴ ساخته نشده** — 11368 chunk فعلی مربوط به داده‌های اولیه است؛ چانک‌سازی فاز ۴ در فاز بعدی

---

## ۹. Runbook — بازسازی `resaname_v2` از نو

```bash
# 1) دیتابیس فعلی را drop کن
mysql -uroot -p433700 -e "DROP DATABASE IF EXISTS resaname_v2;"

# 2) schema را بساز
mysql -uroot -p433700 < v2_schema.sql

# 3) کالکشن کلیدهای بخش را وارد کن
mysql -uroot -p433700 < v2_catalog.sql

# 4) taxonomy را وارد کن
mysql -uroot -p433700 < v2_taxonomy.sql

# 5) مهاجرت داده‌ها (شامل اعمال بازگروه‌بندی کارت‌ها در Section 0)
cd sql/ && python migrate_to_v2.py

# 6) درج محتوای فاز ۴ (بخش‌های تکمیلی + آیتم‌های جدید)
cd sql/ && python insert_phase4.py
```

### فایل‌های مرتبط

| فایل | نقش |
|------|------|
| `v2_schema.sql` | DDL دیتابیس `resaname_v2` (10 جدول شامل `content_type_taxonomy`) |
| `v2_taxonomy.sql` | 33 نوع محتوا در ۶ دسته (DDL + INSERT) |
| `v2_catalog.sql` | کالکشن کلیدهای بخش (18 نظریه + 20 نظریه‌پرداز) |
| `migrate_to_v2.py` | اسکریپت مهاجرت داده‌ها از `resaname_h` + اعمال بازگروه‌بندی کارت‌ها (Section 0) |
| `apply_classification.py` | اسکریپت ادغام + اعتبارسنجی + اعمال `content_type` روی 731 کارت |
| `resaname_vectors.sqlite` | بردارها (2560-dim) — خارج از SQL |
| `vectors.json` | source of truth برای بردارها (~648MB) |

---

*تهیه‌کننده: ZCode AI — تاریخ ۲۰۲۶-۱۱-۱۰*

</div>
