# -*- coding: utf-8 -*-
"""Batch 244: address the critique/limit gap on eight near-complete theory cards."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch244-20261117"
NOW = "2026-11-17 00:00:00"

APPEND = {
    "MC-103": ("mechanism", " فستینگر میان مقایسهٔ «بالاسو» (upward) و «پایین‌سو» (downward) تمایز می‌گذارد: "
               "نخست به انگیزهٔ بهبود و الگوگیری می‌انجامد و دوم به حفظ عزت نفس از راه مقایسه با وضعیت فرودست‌تر. "
               "در پژوهش رسانه، این سازوکار توضیح می‌دهد چگونه بازنمایی آرمانی سبک زندگی در تبلیغات و شبکه‌های اجتماعی، "
               "فاصلهٔ ادراک‌شدهٔ مخاطب از الگوها و نارضایتی بدنی یا مصرف‌گرایی را تشدید می‌کند، هرچند اثر آن به "
               "ویژگی‌های فردی و زمینهٔ اجتماعی وابسته است."),
    "MC-196": ("summary", " با این حال، منتقدان «اگونیستی» مانند شانتال موف استدلال می‌کنند که تأکید بر اجماع عقلانی "
               "می‌تواند جنبهٔ خصومت‌آمیز سیاست و احساسات گروه‌های حاشیه‌ای را سرکوب کند و به «پلورالیسم آگونیستی» "
               "(agonistic pluralism) نیاز است؛ افزون بر این، مشارکت واقعی به سواد مدنی، برابری منابع و "
               "زیرساخت گفت‌وگوی عمومی وابسته است، نه صرفاً به طراحی نهادهای مشورتی."),
    "MC-271": ("summary", " پژوهش‌های معاصر از «پانوپتیکون دیجیتال» سخن می‌گویند: داده‌های رفتاری، پلتفرم‌ها و دوربین‌های "
               "شهری نظارت را از مکان بسته به زندگی روزمره گسترده‌اند و «نظارت افقی» هم‌شهروندان را نیز درگیر می‌کند؛ "
               "اثر اصلی این نظارت اغلب «خودسانسوری پیشگیرانه» و درونی‌شدن هنجار است، نه مجازات مستقیم."),
    "MC-163": ("summary", " آکرلوف نتیجه می‌گیرد که در نبود «نشانه‌دهی» (signaling) معتبر مانند ضمانت، گواهی و "
               "«اعتبار» (reputation)، بازار به‌سمت کیفیت پایین می‌رود و گاه به فروپاشی کامل می‌انجامد؛ "
               "در بازار رسانه و تبلیغات نیز فقدان سنجهٔ شفاف کیفیت مخاطب، توزیع بودجه را به‌سود شاخص‌های قابل دستکاری سوق می‌دهد."),
    "MC-052": ("summary", " نیسنباوم چهار «پارامتر» هر جریان اطلاعاتی را «کنشگران» (actors)، «ویژگی‌ها» (attributes)، "
               "«اصل انتقال» (transmission principle) و «بافت» (context) می‌داند؛ نقض زمانی رخ می‌دهد که "
               "انتقال داده از انتظارهای بافت مبدأ فراتر رود. این چارچوب برای ارزیابی پلتفرم‌ها، داده‌کاوی و "
               "اشتراک‌گذاری میان سازمانی به‌کار می‌رود، هرچند تعیین مرز بافت‌ها در عمل مناقشه‌برانگیز است."),
    "MC-198": ("summary", " هالین و مانچینی نشان می‌دهند تسخیر نتیجهٔ هم‌آمیزی «خویشاوندی سیاسی» (political parallelism)، "
               "حمایت دولتی و ضعف حرفه‌گرایی است و در نظام‌های رسانه‌ای جنوب اروپا بیشتر دیده می‌شود؛ "
               "نشانگان آن شامل خودسانسوری، پوشش یک‌سویه، جابه‌جایی مدیران با تغییر دولت و "
               "کاهش اعتماد عمومی به رسانه است."),
    "MC-346": ("summary", " بارت این فرایند را «دلالت مرتبهٔ دوم» (second-order signification) می‌نامد: نشانهٔ کاملِ "
               "مرتبهٔ اول، خود به «دالِ» (signifier) اسطوره تبدیل می‌شود. اسطوره تاریخ را از چیزها می‌زداید، "
               "آن‌ها را «طبیعی» و بدیهی جلوه می‌دهد و بدین‌سان ایدئولوژی را پنهان می‌کند؛ "
               "از این رو، نقد اسطوره‌شناختی وظیفهٔ «رمزگشایی» (demythologizing) بازنمایی‌های روزمره را دارد."),
    "MC-172": ("summary", " پففر و سالانسیک سه راهبرد کاهش وابستگی را برمی‌شمارند: «جذب» (co-optation) یعنی پیوند با "
               "منابع قدرت از راه عضویت‌های مشترک، «تنوع‌بخشی» (diversification) در تأمین‌کنندگان و بازارها، و "
               "«کنش جمعی» (collective action) از طریق اتحادیه‌ها و انجمن‌های صنفی؛ "
               "در سازمان‌های رسانه‌ای، وابستگی به درآمد تبلیغاتی نمونهٔ کلاسیک این فشار بیرونی است."),
}

FIELD = {k: v[0] for k, v in APPEND.items()}
TEXT = {k: v[1] for k, v in APPEND.items()}


def main():
    import importlib.util
    spec = importlib.util.spec_from_file_location("fw", "scripts/kb_batch238_framework.py")
    fw = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(fw)
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="433700",
                           database=DB, charset="utf8mb4", autocommit=False)
    cur = conn.cursor()
    codes = list(TEXT.keys())
    cur.execute("SELECT code,id,properties FROM kb_entities WHERE code IN (%s)" %
                ",".join(["%s"] * len(codes)), codes)
    found = {r[0]: (r[1], json.loads(r[2])) for r in cur.fetchall()}
    assert len(found) == len(codes), "missing"

    staged = []
    for code in codes:
        eid, p = found[code]
        p[FIELD[code]] = (p.get(FIELD[code]) or "").rstrip() + TEXT[code]
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
                    (code, json.dumps({"batch": 244, "score": t, "words": w}, ensure_ascii=False), STAMP, NOW))
    conn.commit()
    conn.close()
    print("BATCH244 DONE")


if __name__ == "__main__":
    main()
