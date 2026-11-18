# -*- coding: utf-8 -*-
"""Batch 39b touch-up: genuinely extend MC-145 analysis past 500 words, recompute rubric only."""
import pymysql, json

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch39b-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch39b_theory.json"

REQUIRED_SECTIONS = ["summary", "definition", "main_problem", "mechanism", "assumptions",
                     "principles", "critiques", "applications", "evolution", "key_concepts",
                     "theorists", "model", "studies"]

def wc(v):
    if isinstance(v, str): return len(v.split())
    if isinstance(v, list):
        n = 0
        for it in v:
            if isinstance(it, str): n += len(it.split())
            elif isinstance(it, dict): n += len(' '.join(str(x) for x in it.values()).split())
        return n
    if isinstance(v, dict): return len(' '.join(str(x) for x in v.values()).split())
    return 0

def has_content(v):
    if v is None: return False
    if isinstance(v, str): return len(v.strip()) > 10
    if isinstance(v, (list, dict)): return len(v) > 0
    return True

def rubric(p, n_verified, n_sources, n_relations):
    detail = {}
    present = [k for k in REQUIRED_SECTIONS if has_content(p.get(k))]
    detail["structure_15"] = round(15 * min(1, len(present)/7))
    words = sum(wc(p.get(k)) for k in ["summary","definition","main_problem","mechanism",
                "critiques","applications","evolution","key_concepts","principles","studies","assumptions"])
    a = 15 if words>=500 else 13 if words>=300 else 11 if words>=180 else 8 if words>=100 else 3
    detail["analysis_15"] = a
    if n_verified>=1 and n_sources>=2: detail["citation_20"] = 20
    elif n_verified>=1: detail["citation_20"] = 17
    elif n_sources>=1: detail["citation_20"] = 10
    else: detail["citation_20"] = 0
    acc = 0
    if has_content(p.get("summary")) or has_content(p.get("definition")): acc += 10
    if n_verified>=1: acc += 9
    if len(present)>=6: acc += 6
    detail["accuracy_25_auto"] = min(25, acc)
    detail["relations_10"] = 10 if n_relations>=1 else 6
    detail["classification_5"] = 5 if (p.get("field") or p.get("mapping")) else 2
    detail["clarity_5"] = 5 if has_content(p.get("summary")) else 2
    detail["currency_5"] = 5
    return min(100, sum(detail.values())), detail, words

def main():
    c = pymysql.connect(host="127.0.0.1", user="root", password="433700", database=DB, charset="utf8mb4", autocommit=False)
    cur = c.cursor()
    code = "MC-145"
    cur.execute("SELECT id, properties FROM kb_entities WHERE code=%s", (code,))
    eid, pr = cur.fetchone()
    p = json.loads(pr)
    with open(BACKUP, "w", encoding="utf-8") as f:
        json.dump({"code": code, "props": p}, f, ensure_ascii=False, indent=1)

    p["mechanism"] = ("نظریه مکانیسم را در قالب چرخهٔ رابطه توضیح می‌دهد: (۱) سازمان و عمومی‌ها در یک رابطهٔ متقابل قرار دارند که منافع و انتظارات دوطرفه را در بر می‌گیرد؛ (۲) کیفیت رابطه با ابعادی مانند «اعتماد» (trust)، «تعهد» (commitment)، «رضایت» (satisfaction) و «تعادل قدرت» (balance of power) سنجیده می‌شود؛ (۳) ارتباطات راهبردی باید در خدمت حفظ و تقویت این ابعاد باشد، به‌گونهٔ که «درک متقابل و منفعت متقابل» (mutual understanding and benefit) حاصل شود؛ (۴) رابطهٔ باکیفیت، سرمایه‌ای اجتماعی است که در بحران‌ها و مذاکرات، ظرفیت همکاری و تاب‌آوری ایجاد می‌کند (Ledingham, 2003). هان و گرونیگ (1999) شش شاخص رابطه — اعتماد، تعهد، رضایت، تعادل قدرت، مبادلهٔ رابطه‌ای و مبادلهٔ اجتماعی — را برای سنجش عملیاتی پیشنهاد کردند. "
        "لیدینگهام و برونینگ پیش‌تر در پژوهش‌های تجربی خود نشان دادند که ادراک عمومی‌ها از این ابعاد با رفتار حمایتی آنان (مانند مشارکت، وفاداری و رضایت از سازمان) همبستگی دارد و بنابراین رابطه را می‌توان به‌عنوان متغیری اندازه‌پذیر در پژوهش روابط عمومی به کار گرفت. "
        "تمایز نظریه از رویکرد «مدیریت پیام» در همین نکته نهفته است: در مدیریت پیام، معیار موفقیت تغییر نگرش یا انتشار محتواست، اما در مدیریت رابطه، معیار موفقیت کیفیت پایدار رابطه در طول زمان و در موقعیت‌های مختلف است. "
        "همچنین نظریهٔ مدیریت رابطه با نظریهٔ «تعالی» (excellence) گرونیگ در تأکید بر ارتباطات دوطرفه هم‌سو است، اما برخلاف آن، رابطه را نه یک آرمان هنجاری صرف، بلکه سازه‌ای قابل سنجش با شاخص‌های رفتاری و ادراکی می‌داند و بنابراین پلی میان نگرش هنجاری و پژوهش تجربی در روابط عمومی فراهم می‌آورد.")

    p["applications"] = [
        "سنجش کیفیت رابطهٔ سازمان با مشتریان، کارکنان و جامعه.",
        "طراحی برنامه‌های روابط عمومی رابطه‌محور در بحران و مذاکره.",
        "پژوهش در ارتباطات سازمانی، مسئولیت اجتماعی و دیپلماسی عمومی.",
        "ارزیابی راهبردی سرمایهٔ رابطه‌ای سازمان به‌عنوان دارایی نامشهود که تاب‌آوری سازمانی را در بحران‌ها افزایش می‌دهد.",
    ]

    p["critiques"] = [
        "ابهام مفهومی: مرز «رابطه» با «شهرت» و «اعتماد» روشن نیست و تعریف‌ها هم‌پوشانی دارند.",
        "اندازه‌گیری: ابزارهای پیمایشی رابطه عمدتاً ادراکی‌اند و به سوگیری پاسخ‌دهنده حساس‌اند؛ شاخص‌های عینی رابطه کمتر توسعه یافته‌اند.",
        "تعادل آرمانی: فرض «منفعت متقابل» در روابط نامتقارن قدرت (سازمان بزرگ-عمومی ضعیف) واقع‌بینانه نیست و ممکن است منافع عمومی را در پوشش زبان هم‌سود پنهان کند.",
    ]

    n_sources = len(p.get("sources") or [])
    n_verified = sum(1 for s in (p.get("citations") or []) if s.get("verified"))
    cur.execute("SELECT COUNT(*) FROM kb_relations r JOIN kb_entities a ON r.source_id=a.id JOIN kb_entities b ON r.target_id=b.id WHERE a.code=%s OR b.code=%s", (code, code))
    n_relations = cur.fetchone()[0]
    score, detail, words = rubric(p, n_verified, n_sources, n_relations)
    p["quality_score"] = score
    p["quality_assessment"] = dict(breakdown=detail, total=score,
        method="SPEC §6.1 auto-structural (accuracy is auto-credit, NOT human verification)",
        scored_at=NOW, scored_by=STAMP)
    p["updated_at"] = NOW; p["updated_by"] = STAMP
    cur.execute("UPDATE kb_entities SET properties=%s, version=version+1, updated_at=%s, updated_by=%s WHERE id=%s",
                (json.dumps(p, ensure_ascii=False), NOW, STAMP, eid))
    cur.execute("SELECT COALESCE(MAX(version),0)+1 FROM kb_entity_versions WHERE entity_id=%s", (eid,))
    ver = cur.fetchone()[0]
    cur.execute("INSERT INTO kb_entity_versions (entity_id, version, snapshot, change_reason, changed_by, created_at) VALUES (%s,%s,%s,%s,%s,%s)",
                (eid, ver, json.dumps({"quality_score": score, "words": words}, ensure_ascii=False),
                 "substantive analysis expansion", STAMP, NOW))
    cur.execute("INSERT INTO kb_audit_log (entity_code, action, detail, source) VALUES (%s,%s,%s,%s)",
                (code, "DOC_ENRICH", json.dumps({"quality_score": score, "words": words, "breakdown": detail}, ensure_ascii=False), STAMP))
    print(f"{code}: score={score} words={words} sources={n_sources} verified={n_verified} relations={n_relations} | {detail}")
    c.commit(); c.close()
    print("BATCH39b DONE")

if __name__ == "__main__":
    main()
