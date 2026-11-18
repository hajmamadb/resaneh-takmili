# -*- coding: utf-8 -*-
"""Touch-up batch 65b: MC-340 (488w), MC-341 (473w), MC-342 (489w) scored 94 under the
500-word threshold. Append genuine analytic content (mechanism point, critique, application
each), then rescore."""
import pymysql, json

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch65b-theory-20261116"
NOW = "2026-11-16 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch65b_theory.json"

ADD = {
 "MC-340": dict(
   mech=("\n\n(۶) پیکنولپسی و توجه تکه‌تکه: ویریلیو در «زیبایی‌شناسی ناپدیدشدن» (۱۹۸۰) مفهوم «خواب‌های کوچک» توجه را طرح کرد: در محیط پرسرعت، آگاهی به وقفه‌های کوتاه و ناخودآگاه تقسیم می‌شود و تجربهٔ پیوسته جای خود را به توالی لحظه‌های گسسته می‌دهد. "
         "این ایده توضیح می‌دهد چرا مصرف رسانه‌ای پرسرعت، حس زمان و پیوستگی روایت را دگرگون می‌کند، حتی وقتی مخاطب احساس می‌کند «همه‌چیز را دیده است»."),
   crits=["۴. تمرکز نظامی: تحلیل ویریلیو بیش از اندازه بر جنگ و لجستیک نظامی متمرکز است و کاربردهای مدنی سرعت — درمان، آموزش، تجارت — و منافع متفاوت آن‌ها را کم‌رنگ می‌کند."],
   apps=["تحلیل تجربهٔ اسکرول بی‌پایان و مصرف تکه‌تکهٔ ویدئو: سرعت، شکل روایت و حافظهٔ مخاطب را تغییر می‌دهد."],
 ),
 "MC-341": dict(
   mech=("\n\n(۶) پارالوژی و مشروعیت از راه اختلاف: لیوتار در بخش پایانی گزارش، «پارالوژی» را پیشنهاد می‌کند: مشروعیت علم نه از اجماع، بلکه از تولید اختلاف و نوآوری می‌آید. "
         "در این نگاه، پژوهشگری که قاعدهٔ موجود را به چالش می‌کشد، مشروعیت را بازتولید می‌کند؛ بنابراین پست‌مدرنیسم لیوتار، دعوت به نسبیت نیست، دعوت به پذیرش تکثر و آزمون مداوم است."),
   crits=["۴. تقلیل سبکی: در کاربرد عامه‌پسند، «پست‌مدرن» به برچسبی سبکی در هنر و رسانه تقلیل یافت («هر چیز آمیخته و بی‌قاعده») و بار تحلیلی خود را از دست داد."],
   apps=["تحلیل خردروایت‌ها در پادکست و شبکه‌های اجتماعی: چگونه روایت شخصی جای روایت نهادی را می‌گیرد."],
 ),
 "MC-342": dict(
   mech=("\n\n(۶) فاصلهٔ نقش: گافمن نشان داد که فرد می‌تواند هم‌زمان نقش را اجرا کند و از آن فاصله بگیرد؛ شوخی، کنایه یا رفتار خودمانی، نشانه‌ای است که می‌گوید «من فقط این نقش نیستم». "
         "همین مفهوم توضیح می‌دهد چرا اصالت در اجرا، نه غیبت اجرا، بلکه توانایی نمایش فاصله از نقش است."),
   crits=["۴. چندپارگی خود: اگر خود محصول اجراهای موقعیتی باشد، پرسش از «خود اصیل» بی‌پاسخ می‌ماند؛ منتقدان این را نقطهٔ ضعف نظریه در برابر پرسش اخلاقی صداقت می‌دانند."],
   apps=["تحلیل مصاحبهٔ استخدامی و ارزیابی عملکرد: داوطلب و کارمند، برداشتی از شایستگی خود را اجرا و مدیریت می‌کنند."],
 ),
}

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
    codes = list(ADD.keys())
    cur.execute("SELECT id, code, properties FROM kb_entities WHERE code IN (%s)" % ",".join(["%s"]*len(codes)), codes)
    rows = {code:(eid, json.loads(pr)) for (eid, code, pr) in cur.fetchall()}
    with open(BACKUP, "w", encoding="utf-8") as f:
        json.dump([{"code": cd, "props": rows[cd][1]} for cd in codes if cd in rows], f, ensure_ascii=False, indent=1)
    print("backup ->", len(rows), "rows")

    for code in codes:
        eid, p = rows[code]
        a = ADD[code]
        p["mechanism"] = p.get("mechanism", "") + a["mech"]
        p["critiques"] = list(p.get("critiques", [])) + a["crits"]
        p["applications"] = list(p.get("applications", [])) + a["apps"]
        n_sources = len(p.get("sources", []))
        n_verified = sum(1 for civ in p.get("citations", []) if civ.get("verified"))
        cur.execute("SELECT COUNT(*) FROM kb_relations r JOIN kb_entities a ON r.source_id=a.id JOIN kb_entities b ON r.target_id=b.id WHERE a.code=%s OR b.code=%s", (code, code))
        n_relations = cur.fetchone()[0]
        score, detail, words = rubric(p, n_verified, n_sources, n_relations)
        p["quality_score"] = score
        p["quality_assessment"] = dict(breakdown=detail, total=score,
            method="SPEC §6.1 auto-structural (accuracy is auto-credit, NOT human verification)",
            scored_at=NOW, scored_by=STAMP)
        p["status_scientific_note"] = "score is structural/citation-based; requires human expert review for scientific verification (SPEC §6.4)"
        p["updated_at"] = NOW; p["updated_by"] = STAMP
        cur.execute("UPDATE kb_entities SET properties=%s, version=version+1, updated_at=%s, updated_by=%s WHERE id=%s",
                    (json.dumps(p, ensure_ascii=False), NOW, STAMP, eid))
        cur.execute("SELECT COALESCE(MAX(version),0)+1 FROM kb_entity_versions WHERE entity_id=%s", (eid,))
        ver = cur.fetchone()[0]
        cur.execute("INSERT INTO kb_entity_versions (entity_id, version, snapshot, change_reason, changed_by, created_at) VALUES (%s,%s,%s,%s,%s,%s)",
                    (eid, ver, json.dumps({"quality_score": score, "words": words, "sources": n_sources, "verified": n_verified}, ensure_ascii=False),
                     "expanded analysis above 500-word threshold to clear 94 cap", STAMP, NOW))
        cur.execute("INSERT INTO kb_audit_log (entity_code, action, detail, source) VALUES (%s,%s,%s,%s)",
                    (code, "DOC_ENRICH", json.dumps({"quality_score": score, "words": words, "sources": n_sources, "verified": n_verified, "breakdown": detail}, ensure_ascii=False), STAMP))
        print(f"{code}: score={score} words={words} sources={n_sources} verified={n_verified} relations={n_relations} | {detail}")
    c.commit()
    c.close()
    print("BATCH65b THEORY DONE")

if __name__ == "__main__":
    main()
