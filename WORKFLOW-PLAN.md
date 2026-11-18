# WORKFLOW-PLAN — تکمیل خودکار resaname (11-Nov-2026)

## کارهای باقی‌مانده (از بررسی وضعیت)

| # | واحد | دیتابیس | توصیف |
|---|------|---------|-------|
| 1 | works_authors | resaname_v2 | 42 work بدون نویسنده — populate از contents/sections |
| 2 | concepts + content_concepts | resaname_v2 | جدول مفاهیم خالی — استخراج از 852 contents |
| 3 | entity_content_links (Phase B) | resaname_v2 | 852 contents → knowledge_entities وصل |
| 4 | origin backfill (Phase 3b) | resaname_h | ستون origin در جدول theorists |
| 5 | Expert verification (Phase C) | resaname_v2 | تأیید 535 entities + 1077 relations |

## توپولوژی
- **A — fan-out / fan-in**: ۵ واحد مستقل، هرکدام یک ساب‌ایجنت با `background: true`
- حداکثر ۳-۴ هم‌زمان؛ بقیه بعد از نوتیفیکیشن اتمام
- هر واحد self-contained است: کانتکست + واحد + مالکیت فایل + معیار پذیرش
- Gate نهایی: سشن اصلی بعد از فرود همه، sanity check نهایی + dump

## Round cap
- هر واحد: حداکثر ۳ round (اگر ساب‌ایجنت گیر کرد، follow-up با sessionID)

## Gate (نهایی)
- `SELECT COUNT(*)` برای هر جدول هدف
- Referential integrity (orphan check)
- `__unresolved = 0` در relation_links
- dump پایدار `resaname_v2_dump-final.sql`

## گزارش
- `WORKFLOW-REPORT.md` با سه بخش: verified / notCovered / نتیجه به تفکیک واحد
