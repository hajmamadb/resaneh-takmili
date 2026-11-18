# -*- coding: utf-8 -*-
"""Batch 243: final word top-up for eight near-complete theory cards."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch243-20261117"
NOW = "2026-11-17 00:00:00"

APPEND = {
    "MC-191": (" با این حال، فهرست ارزش‌های خبری توصیفی است و وزن هر ارزش در بافت‌های فرهنگی و سازمانی متفاوت می‌شود؛ "
               "پژوهش‌های دیجیتال نشان می‌دهند اشتراک‌گذاری، احساسات و تصویر نیز به ارزش‌های خبری افزوده شده‌اند."),
    "MC-358": (" این مشارکت گاه رایگان و نامرئی است و پلتفرم‌ها با شرایط استفاده، مالکیت محتوای هوادار را به خود منتقل می‌کنند؛ "
               "از این رو، مشارکت هواداری هم فرصت خلاقیت و هم عرصهٔ کار بدون مزد است."),
    "MC-086": (" راجرز خود به سوگیری نوآوری‌محور در بسیاری از پژوهش‌ها اشاره می‌کند: تمرکز بر پذیرش سریع، هزینه‌ها و پیامدهای منفی نوآوری را کم‌برجسته می‌کند."),
    "MC-259": (" ساختار، هم قید و هم منبع توانمندسازی است و ساخت‌یابی با پیامدهای ناخواسته همراه می‌شود؛ "
               "همین دو نکته، نظریه را از جبر ساختاری و از ارادی‌گرایی محض جدا می‌کند."),
    "MC-176": (" نقد اصلی این است که مرز گروه‌های راهبردی اغلب مبهم و متغیر است و موانع جابه‌جایی، بیشتر توصیف پس‌رویدادی‌اند تا پیش‌بین."),
    "MC-455": (" جنکینز میان «گسترش‌پذیری» محتوا توسط مخاطب و «کاوشگری» عمیق در جهان داستان تفکیک می‌کند؛ "
               "موفقیت پروژه به همکاری تولیدکننده و مخاطب وابسته است."),
    "TX-014": (" با این حال، این رویکرد به گزارش خودخواستهٔ مخاطب وابسته است، انگیزه‌های ناخودآگاه را کم‌می‌سنجد و گاه کارکرد نظام رسانه را طبیعی می‌کند؛ "
               "پژوهش‌های پلتفرمی نیز رضامندی‌های تازه‌ای مانند نظارت بر دیگران و مدیریت تصویر افزوده‌اند."),
    "MC-258": (" بوید چهار امکان پلتفرمی «ماندگاری»، «تکرارپذیری»، «مقیاس‌پذیری» و «قابلیت جست‌وجو» را عامل «درهم‌ریختگی زمینه» می‌داند؛ "
               "همان سازوکاری که مرز مخاطب خصوصی و عمومی را از میان برمی‌دارد."),
}


def main():
    import importlib.util
    spec = importlib.util.spec_from_file_location("fw", "scripts/kb_batch238_framework.py")
    fw = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(fw)
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="433700",
                           database=DB, charset="utf8mb4", autocommit=False)
    cur = conn.cursor()
    codes = list(APPEND.keys())
    cur.execute("SELECT code,id,properties FROM kb_entities WHERE code IN (%s)" %
                ",".join(["%s"] * len(codes)), codes)
    found = {r[0]: (r[1], json.loads(r[2])) for r in cur.fetchall()}
    assert len(found) == len(codes), "missing"

    staged = []
    for code in codes:
        eid, p = found[code]
        p["summary"] = (p.get("summary") or "") + APPEND[code]
        cur.execute("SELECT COUNT(DISTINCT source_id),COUNT(DISTINCT CASE WHEN verification_status='verified' THEN source_id END) FROM kb_evidence WHERE about_code=%s", (code,))
        ns, nv = cur.fetchone()
        cur.execute("SELECT COUNT(*) FROM kb_relations WHERE source_id=%s OR target_id=%s", (eid, eid))
        rel = cur.fetchone()[0]
        t, d, w = fw.rubric(p, nv, ns, rel)
        staged.append((code, eid, p, t, d, w))
        print(code, "words", w, "score", t)

    short = [s for s in staged if s[5] < 500]
    if short:
        print("SHORT:", [(s[0], s[5]) for s in short])
        conn.close()
        return

    for code, eid, p, t, d, w in staged:
        p["quality_score"] = t
        p["quality_assessment"] = "ارزیابی خودکار SPEC §6.1: %d/100 (نمره پایه؛ نیازمند بازبینی علمی انسانی)" % t
        cur.execute("UPDATE kb_entities SET properties=%s,version=version+1,updated_at=%s,updated_by=%s WHERE id=%s",
                    (json.dumps(p, ensure_ascii=False), NOW, STAMP, eid))
        cur.execute("""INSERT INTO kb_audit_log (entity_code,action,detail,source,created_at)
            VALUES (%s,'DOC_ENRICH',%s,%s,%s)""",
                    (code, json.dumps({"batch": 243, "score": t, "words": w}, ensure_ascii=False), STAMP, NOW))
    conn.commit()
    conn.close()
    print("BATCH243 DONE")


if __name__ == "__main__":
    main()
