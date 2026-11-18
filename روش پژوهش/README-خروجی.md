# خروجی vector DB — مرجع پژوهش

محتوای پردازش‌شده کتاب «مرجع پژوهش-آشنایی با انواع روشهای تحقیق.pdf» (۹۸۵ صفحه)
در این پوشه قرار دارد.

## فایل‌ها

| فایل | محتوا |
|---|---|
| `chunks-review.txt` | کل متن کتاب در **2,022 بخش (chunk)** با ترتیب صفحه؛ هر بخش برچسب «ردیف | صفحه | سرفصل» دارد |

## مشخصات فنی

- **Vector DB:** Chroma (فولدر `vector_db` در پروژه)
- **Embedding:** `Qwen3-Embedding-4B` از API ismc (کلکشن `pdf_chunks`)
  + نسخه جدا با `Qwen3-Embedding-0.6B` (کلکشن `pdf_chunks_qwen3-embedding-0.6b`)
- **پردازش متن:** بازسازی هندسی لایه متن تکه‌تکه PDF + نرمال‌سازی فارسی (ی/ك، ارقام، نیم‌فاصله)
- **تشخیص سرفصل:** از فلگ bold فونت + حذف header تکراری صفحه

## جستجو روی این داده (از داخل پوشه پروژه)

```
C:\Users\MamaDDelta\Documents\Default Project>

python query.py "انواع روش تحقیق کوانتیتاتیو چیست؟"
python query.py "روش نمونه‌گیری" -k 5
python query.py "سوال" --model Qwen3-Embedding-0.6B
```

## بازتولید این خروجی

```
python export_chunks.py --out "D:\رسانامه تکمیلی\روش پژوهش\chunks-review.txt"
```

تاریخ تولید: 2026-11-09
