# -*- coding: utf-8 -*-
"""Demote Gerbner and ELM duplicate records (non-destructive, cross-referenced)."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
SRC = "qoder-doc-dedupe-20261117"
NOW = "2026-11-17 00:00:00"

ITEMS = {
    "MC-465": dict(
        canonical="MC-309", canonical_name="مدل ادراکی گربر",
        new_fa="مدل گربر (رکورد دوم)",
        new_en="Gerbner's Model (second record)",
        pointer="این رکورد نسخهٔ دوم مدل گربر است؛ نسخهٔ کامل و ارجاع‌محور با عنوان «مدل ادراکی گربر» و کد MC-309 ثبت شده و برای استناد باید به آن مراجعه شود.",
        analysis=("جرج گربر در ۱۹۵۶ مدلی عمومی برای ارتباط عرضه کرد که ارتباط را زنجیره‌ای از رویداد، ادراک و گزینش، تبدیل به سیگنال و انتقال می‌دید. "
                  "او ده مؤلفهٔ مدل را برشمرد و بر دو بُعد افقی و عمودی تأکید کرد: بعد افقی زنجیرهٔ رویداد تا گیرنده را نشان می‌دهد و بعد عمودی بازخورد و تفسیر را. "
                  "در ۱۹۶۷ مدل را برای رسانه‌های جمعی گسترش داد.\n\n"
                  "این کارت نسخهٔ دوم است؛ تحلیل تفصیلی، نقدها و ارجاع‌های اصلی در کارت MC-309 آمده است."),
        recs="«به‌سوی مدلی عمومی برای ارتباط» (گربر، ۱۹۵۶)؛ «رسانه‌های جمعی و نظریهٔ ارتباط انسانی» (گربر، ۱۹۶۷).",
    ),
    "MC-550": dict(
        canonical="MC-309", canonical_name="مدل ادراکی گربر",
        new_fa="مدل شماتیک گربر (رکورد دوم)",
        new_en="Gerbner's Schematic Model (second record)",
        pointer="این رکورد نسخهٔ دوم مدل گربر است؛ نسخهٔ کامل و ارجاع‌محور با عنوان «مدل ادراکی گربر» و کد MC-309 ثبت شده و برای استناد باید به آن مراجعه شود.",
        analysis=("مدل شماتیک گربر، نمایش تصویری همان مدل عمومی ۱۹۵۶ است که در آن رویداد، ادراک، سیگنال و پیام در قالب یک نمودار دو‌بُعدی نشان داده می‌شوند. "
                  "بُعد افقی مسیر رویداد به گیرنده و بُعد عمودی بازخورد را نمایش می‌دهد و بر گزینش ادراکی خبرنگار یا رسانه تأکید دارد.\n\n"
                  "این کارت نسخهٔ دوم است؛ تحلیل تفصیلی و ارجاع‌های اصلی در کارت MC-309 آمده است."),
        recs="«به‌سوی مدلی عمومی برای ارتباط» (گربر، ۱۹۵۶)؛ «رسانه‌های جمعی و نظریهٔ ارتباط انسانی» (گربر، ۱۹۶۷).",
    ),
    "MC-319": dict(
        canonical="MC-021", canonical_name="مدل احتمال بسط",
        new_fa="مدل احتمال تفصیل / بسط (رکورد دوم)",
        new_en="Elaboration Likelihood Model (second record)",
        pointer="این رکورد نسخهٔ دوم مدل احتمال بسط است؛ نسخهٔ کامل و ارجاع‌محور با عنوان «مدل احتمال بسط» و کد MC-021 ثبت شده و برای استناد باید به آن مراجعه شود.",
        analysis=("مدل احتمال بسط، مدلی دومسیره در اقناع است که پتی و کاسیوپو در ۱۹۸۶ عرضه کردند. "
                  "در بسط بالا، گیرنده استدلال‌ها را عمیق پردازش می‌کند و مسیر مرکزی فعال می‌شود؛ در بسط پایین، نشانه‌های پیرامونی مانند جذابیت گوینده تصمیم را می‌سازند. "
                  "انگیزش و توانایی، احتمال بسط را تعیین می‌کنند.\n\n"
                  "این کارت نسخهٔ دوم است؛ تحلیل تفصیلی، نقدها و ارجاع‌های اصلی در کارت MC-021 آمده است."),
        recs="«مدل احتمال بسط اقناع» (پتی و کاسیوپو، ۱۹۸۶)؛ «ارتباط و اقناع» (پتی و کاسیوپو، ۱۹۸۶).",
    ),
    "MC-467": dict(
        canonical="MC-021", canonical_name="مدل احتمال بسط",
        new_fa="مدل احتمال تفصیل (رکورد دوم)",
        new_en="Elaboration Likelihood Model (second record)",
        pointer="این رکورد نسخهٔ دوم مدل احتمال بسط است؛ نسخهٔ کامل و ارجاع‌محور با عنوان «مدل احتمال بسط» و کد MC-021 ثبت شده و برای استناد باید به آن مراجعه شود.",
        analysis=("مدل احتمال تفصیل یا بسط، بر اساس میزان پردازش شناختی پیام، دو مسیر اقناع را از هم جدا می‌کند: مسیر مرکزی که بر کیفیت استدلال استوار است و تغییر پایدارتری می‌سازد، "
                  "و مسیر پیرامونی که با نشانه‌های سطحی و بدون پردازش عمیق عمل می‌کند. این مدل را پتی و کاسیوپو در ۱۹۸۶ معرفی کردند.\n\n"
                  "این کارت نسخهٔ دوم است؛ تحلیل تفصیلی، نقدها و ارجاع‌های اصلی در کارت MC-021 آمده است."),
        recs="«مدل احتمال بسط اقناع» (پتی و کاسیوپو، ۱۹۸۶)؛ «ارتباط و اقناع» (پتی و کاسیوپو، ۱۹۸۶).",
    ),
}

def main():
    c = pymysql.connect(host="127.0.0.1", port=3306, user="root",
                        password="433700", database=DB, charset="utf8mb4")
    cur = c.cursor()
    for code, it in ITEMS.items():
        cur.execute("SELECT id, properties FROM kb_entities WHERE code=%s", (code,))
        row = cur.fetchone()
        if not row:
            print("MISSING", code)
            continue
        eid, props = row
        p = json.loads(props)
        s = str(p.get("summary") or "")
        if not s.startswith(it["pointer"]):
            p["summary"] = it["pointer"] + " " + s
        p["detailed_analysis"] = it["analysis"]
        p["recommended_sources"] = it["recs"]
        cur.execute("""UPDATE kb_entities SET canonical_name_fa=%s, canonical_name_en=%s,
                       properties=%s, updated_by=%s WHERE id=%s""",
                    (it["new_fa"], it["new_en"], json.dumps(p, ensure_ascii=False), SRC, eid))
        cur.execute("""INSERT INTO kb_audit_log(entity_code,action,detail,source,created_at)
                       VALUES(%s,'DOC_FIX',%s,%s,%s)""",
                    (code, json.dumps({"note": "demoted duplicate and cross-referenced",
                                       "canonical": it["canonical"]}, ensure_ascii=False),
                     SRC, NOW))
        print("demoted", code, "->", it["canonical"])
    c.commit()
    c.close()

if __name__ == "__main__":
    main()
