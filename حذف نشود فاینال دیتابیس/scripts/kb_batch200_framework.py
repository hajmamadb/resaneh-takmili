# -*- coding: utf-8 -*-
"""Batch 200: MC-123, MC-627, MC-128, MC-728, MC-729 (FRAMEWORK)."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch200-20261117"
NOW = "2026-11-17 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch200.json"

S = {
    "MC-123": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Social Amplification of Risk: A Conceptual Framework",
             title_fa="تقویت اجتماعی ریسک: چارچوبی مفهومی",
             authors="Roger E. Kasperson; Ortwin Renn; Paul Slovic; Halina S. Brown; Jacque Emel; Robert Goble; Jeanne X. Kasperson; Samuel Ratick", year=1988,
             publisher="Risk Analysis",
             doi="10.1111/j.1539-6924.1988.tb01168.x",
             url="https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1539-6924.1988.tb01168.x",
             language="en", isbn=None,
             citation="Kasperson, R. E., Renn, O., Slovic, P., Brown, H. S., Emel, J., Goble, R., Kasperson, J. X., & Ratick, S. (1988). The social amplification of risk: A conceptual framework. Risk Analysis, 8(2), 177-187. https://doi.org/10.1111/j.1539-6924.1988.tb01168.x",
             locator="8(2), 177-187",
             locator_type="PAGE",
             supports="social stations amplify or attenuate risk through information processing and ripple effects",
             verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Social Amplification of Risk Framework: New Perspectives",
             title_fa="چارچوب تقویت اجتماعی ریسک: چشم‌اندازهای تازه",
             authors="Roger E. Kasperson et al.", year=2022,
             publisher="Risk Analysis",
             doi=None,
             url="https://pmc.ncbi.nlm.nih.gov/articles/PMC10360138/",
             language="en", isbn=None,
             citation="Kasperson, R. E., et al. (2022). The social amplification of risk framework: New perspectives. Risk Analysis.",
             locator="special issue review",
             locator_type="PAGE",
             supports="a retrospective assessment of the framework and its extensions to digital media",
             verified=True),
    ],
    "MC-627": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="Testing for Competence Rather Than for Intelligence",
             title_fa="سنجش شایستگی به‌جای هوش",
             authors="David C. McClelland", year=1973,
             publisher="American Psychologist",
             doi="10.1037/h0034092",
             url="https://psycnet.apa.org/record/1973-22126-001",
             language="en", isbn=None,
             citation="McClelland, D. C. (1973). Testing for competence rather than for intelligence. American Psychologist, 28(1), 1-14. https://doi.org/10.1037/h0034092",
             locator="28(1), 1-14",
             locator_type="PAGE",
             supports="criterion sampling and competence testing as an alternative to intelligence tests",
             verified=True),
        dict(kind="BOOK",
             title_en="The Competent Manager: A Model for Effective Performance",
             title_fa="مدیر شایسته: مدلی برای عملکرد اثربخش",
             authors="Richard E. Boyatzis", year=1982,
             publisher="Wiley",
             doi=None,
             url=None,
             language="en", isbn=None,
             citation="Boyatzis, R. E. (1982). The Competent Manager: A Model for Effective Performance. New York: Wiley.",
             locator="competency model chapters",
             locator_type="CHAPTER",
             supports="the distinction between threshold and differentiating competencies in managerial performance",
             verified=True),
    ],
    "MC-128": [
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Pyramid of Corporate Social Responsibility: Toward the Moral Management of Organizational Stakeholders",
             title_fa="هرم مسئولیت اجتماعی شرکتی: به‌سوی مدیریت اخلاقی ذی‌نفعان سازمان",
             authors="Archie B. Carroll", year=1991,
             publisher="Business Horizons",
             doi="10.1016/0007-6813(91)90005-G",
             url="https://www.sciencedirect.com/science/article/pii/000768139190005G",
             language="en", isbn=None,
             citation="Carroll, A. B. (1991). The pyramid of corporate social responsibility: Toward the moral management of organizational stakeholders. Business Horizons, 34(4), 39-48. https://doi.org/10.1016/0007-6813(91)90005-G",
             locator="34(4), 39-48",
             locator_type="PAGE",
             supports="the four-layered CSR pyramid: economic, legal, ethical and philanthropic responsibilities",
             verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="Corporate Social Responsibility: Evolution of a Definitional Construct",
             title_fa="مسئولیت اجتماعی شرکتی: تحول یک سازهٔ تعریفی",
             authors="Archie B. Carroll", year=1999,
             publisher="Business & Society",
             doi=None,
             url=None,
             language="en", isbn=None,
             citation="Carroll, A. B. (1999). Corporate social responsibility: Evolution of a definitional construct. Business & Society, 38(3), 268-295.",
             locator="38(3), 268-295",
             locator_type="PAGE",
             supports="the historical evolution of CSR as a definitional construct",
             verified=True),
    ],
    "MC-728": [
        dict(kind="BOOK",
             title_en="Sensemaking in Organizations",
             title_fa="حس‌سازی در سازمان‌ها",
             authors="Karl E. Weick", year=1995,
             publisher="Sage Publications",
             doi=None,
             url="https://www.sagepub.com/shop/buy-a-book/sensemaking-in-organizations-1-4988",
             language="en", isbn=None,
             citation="Weick, K. E. (1995). Sensemaking in Organizations. Thousand Oaks, CA: Sage Publications.",
             locator="book",
             locator_type="BOOK",
             supports="seven properties of sensemaking and the priority of plausibility over accuracy",
             verified=True),
        dict(kind="JOURNAL_ARTICLE",
             title_en="The Collapse of Sensemaking in Organizations: The Mann Gulch Disaster",
             title_fa="فروپاشی حس‌سازی در سازمان‌ها: فاجعهٔ مان گالچ",
             authors="Karl E. Weick", year=1993,
             publisher="Administrative Science Quarterly",
             doi=None,
             url="https://psycnet.apa.org/record/1994-23633-001",
             language="en", isbn=None,
             citation="Weick, K. E. (1993). The collapse of sensemaking in organizations: The Mann Gulch disaster. Administrative Science Quarterly, 38(4), 628-652.",
             locator="38(4), 628-652",
             locator_type="PAGE",
             supports="the case study of how sensegiving and structure collapse under sudden ambiguity",
             verified=True),
    ],
    "MC-729": [
        dict(kind="BOOK",
             title_en="Strategic Management in the Media: Theory to Practice",
             title_fa="مدیریت راهبردی در رسانه: از نظریه تا عمل",
             authors="Lucy Küng", year=2017,
             publisher="SAGE Publications",
             doi=None,
             url="https://api.pageplace.de/preview/DT0400.9781473987364_A28765658/preview-9781473987364_A28765658.pdf",
             language="en", isbn="9781473929494",
             citation="Küng, L. (2017). Strategic Management in the Media: Theory to Practice (2nd ed.). London: SAGE Publications. (First edition 2008)",
             locator="book",
             locator_type="BOOK",
             supports="media-specific adaptation of strategic management theory",
             verified=True),
        dict(kind="BOOK",
             title_en="Strategic Management in the Media: Theory to Practice (1st ed.)",
             title_fa="مدیریت راهبردی در رسانه: از نظریه تا عمل (ویرایش نخست)",
             authors="Lucy Küng", year=2008,
             publisher="SAGE Publications",
             doi=None,
             url=None,
             language="en", isbn=None,
             citation="Küng, L. (2008). Strategic Management in the Media: Theory to Practice. London: SAGE Publications.",
             locator="book",
             locator_type="BOOK",
             supports="the original formulation of the media-specific strategic management framework",
             verified=True),
    ],
}

ENRICH = {
    "MC-123": dict(
        needs_enrichment=False,
        key_concepts=["ایستگاه تقویت", "اثر موجی", "تقویت اطلاعاتی و پیامدی", "برچسب‌خوردگی", "زیان ثانویه"],
        recommended_sources="«تقویت اجتماعی ریسک: چارچوبی مفهومی» (کاسپرسون و همکاران، ۱۹۸۸) در مجلهٔ تحلیل ریسک؛ «چشم‌اندازهای تازه در چارچوب تقویت اجتماعی ریسک» (کاسپرسون و همکاران، ۲۰۲۲)؛ پژوهش‌های ارتباطات بحران و ریسک برای کاربرد رسانه‌ای.",
    ),
    "MC-627": dict(
        needs_enrichment=False,
        detailed_analysis="چارچوب شایستگی از نقد سنجش هوش آغاز می‌شود: مک‌کللند (۱۹۷۳) استدلال کرد که پیش‌بینی عملکرد شغلی با نمونه‌گیری ملاک‌محور و سنجش رفتار واقعی، بهتر از آزمون‌های هوش ممکن است. بوایاتزیس (۱۹۸۲) این ایده را به مدل مدیر شایسته گسترش داد و میان شایستگی‌های آستانه‌ای (حداقل لازم برای نقش) و شایستگی‌های تمایزساز (که عملکرد برتر می‌سازند) فرق گذاشت. در عمل، چارچوب با مصاحبهٔ رویداد رفتاری، مشاهدهٔ کار و ارزیابی چندمنبعی سنجیده می‌شود. کاربرد رسانه‌ای آن در طراحی مدل شایستگی خبرنگار، تولیدکنندهٔ محتوا و مدیر رسانه دیده می‌شود، به‌ویژه برای مهارت‌های دیجیتال و داده‌محور. نقد اصلی این است که فهرست‌های شایستگی می‌توانند به مجموعه‌ای کلی و غیرقابل سنجش بدل شوند و بافت سازمانی و قدرت را نادیده بگیرند.",
        recommended_sources="«سنجش شایستگی به‌جای هوش» (مک‌کللند، ۱۹۷۳) در مجلهٔ روان‌شناس آمریکایی؛ «مدیر شایسته» (بوایاتزیس، ۱۹۸۲)؛ پژوهش‌های مدل شایستگی در سازمان‌های رسانه‌ای و آموزش روزنامه‌نگاری.",
    ),
    "MC-128": dict(
        needs_enrichment=False,
        key_concepts=["هرم مسئولیت اجتماعی", "ذی‌نفعان", "سبزشویی", "گزارش پایداری", "شکاف گفتار و کردار"],
        recommended_sources="«هرم مسئولیت اجتماعی شرکتی» (کرول، ۱۹۹۱)؛ «مسئولیت اجتماعی شرکتی: تحول یک سازهٔ تعریفی» (کرول، ۱۹۹۹)؛ «روابط عمومی: یک تاریخ» (گرانیگ، ۱۹۸۳)؛ «مدیریت شهرت» (فومبرون، ۲۰۰۰).",
    ),
    "MC-728": dict(
        needs_enrichment=False,
        detailed_analysis="حس‌سازی پاسخ سازمان به ابهام است: مردم با ساختن روایتی قابل قبول از نشانه‌های ناقص، جهان را فهم‌پذیر می‌کنند. وایک (۱۹۹۵) هفت ویژگی برای این فرایند برشمرد: آن را در بستر هویت سازمانی و کنش (ساختن محیط) می‌بیند، به نشانه‌های برجسته و گذشتهٔ تجربه وابسته است، اجتماعی و پیوسته است، و به باورپذیری بیش از دقت گرایش دارد. مطالعهٔ فاجعهٔ مان گالچ (۱۹۹۳) نشان داد وقتی ساختار نقش و معنای مشترک فرو می‌ریزد، سازمان حتی با افراد توانمند نیز نمی‌تواند کنش هماهنگ بسازد. در ارتباطات رسانه‌ای، این چارچوب توضیح می‌دهد چگونه سازمان‌ها در بحران روایت خود را می‌سازند و چگونه رسانه‌ها و کاربران در شکل‌گیری یا فروپاشی این روایت شریک می‌شوند.",
        recommended_sources="«حس‌سازی در سازمان‌ها» (وایک، ۱۹۹۵)؛ «فروپاشی حس‌سازی در سازمان‌ها: فاجعهٔ مان گالچ» (وایک، ۱۹۹۳) در فصلنامهٔ علوم اداری؛ پژوهش‌های ارتباطات بحران و روایت سازمانی.",
    ),
    "MC-729": dict(
        needs_enrichment=False,
        detailed_analysis="مدیریت راهبردی رسانه نمی‌تواند نسخهٔ صنایع تولیدی را بی‌تغییر بپذیرد، زیرا محصول رسانه نمادین و دوسویه است و بازار آن هم مخاطب و هم تبلیغ‌دهنده را در بر می‌گیرد. کونگ (۲۰۰۸، ۲۰۱۷) نشان می‌دهد ابزارهای عمومی راهبردی، مانند تحلیل پنج نیرو و دیدگاه مبتنی بر منابع، باید با ویژگی‌های محصول خلاق و نیروی کار پروژه‌ای سازگار شوند. مفهوم کانونی چارچوب، دوسوتوانی راهبردی است: توان هم‌زمان بهره‌برداری از کسب‌وکار موجود و کاوش در قلمروهای نو. اختلال دیجیتال، نوآوری مختل‌کننده و اکوسیستم‌های پلتفرمی چارچوب را به‌سوی تحلیل گذار سوق داده‌اند. نقدها بر دشواری سنجش عملکرد خلاق، سوگیری نسبت به سازمان‌های بزرگ و کم‌توجهی به قدرت حرفه‌ای در تصمیم راهبردی تمرکز دارند.",
        recommended_sources="«مدیریت راهبردی در رسانه: از نظریه تا عمل» (کونگ، ویرایش نخست ۲۰۰۸ و ویرایش دوم ۲۰۱۷)؛ «استراتژی رقابتی» (پورتر، ۱۹۸۰) برای مبانی؛ «اقتصاد رسانه» (هاردوود، ۲۰۱۰).",
    ),
}

NAME_FIX = {}

YEAR_FIX = {
    "MC-123": "year=1988 (Kasperson et al. 1988); 2022 retrospective verified; removed Latin glosses from concepts and mixed-script recommendations",
    "MC-627": "year=1973 (McClelland 1973); Boyatzis 1982 verified; rebuilt template-contaminated analysis and recommendation list",
    "MC-128": "year=1991 (Carroll 1991); Carroll 1999 verified; removed Latin glosses from concepts and mixed-script recommendations",
    "MC-728": "year=1995 (Weick 1995); Weick 1993 Mann Gulch verified; rebuilt wrong-topic detailed analysis",
    "MC-729": "year=2008 (Küng 1st ed.; 2nd ed. 2017); removed Latin glosses from detailed analysis",
}

def wc(v):
    if v is None:
        return 0
    if isinstance(v, str):
        return len(v.split())
    if isinstance(v, (list, tuple)):
        return sum(len(str(x).split()) for x in v)
    return 0


def has_content(v):
    if v is None:
        return False
    if isinstance(v, str):
        return bool(v.strip())
    if isinstance(v, (list, dict)):
        return len(v) > 0
    return True


REQUIRED_SECTIONS = ["summary", "definition", "main_problem", "mechanism", "assumptions",
                     "principles", "critiques", "applications", "evolution", "key_concepts",
                     "theorists", "model", "studies"]
WORD_KEYS = ["summary", "definition", "main_problem", "mechanism", "critiques",
             "applications", "evolution", "key_concepts", "principles", "studies", "assumptions"]


def rubric(p, n_verified, n_sources, n_relations):
    present = sum(1 for k in REQUIRED_SECTIONS if has_content(p.get(k)))
    structure = round(15 * min(1, present / 7))
    words = sum(wc(p.get(k)) for k in WORD_KEYS)
    if words >= 500:
        analysis = 15
    elif words >= 300:
        analysis = 13
    elif words >= 180:
        analysis = 11
    elif words >= 100:
        analysis = 8
    else:
        analysis = 3
    if n_verified >= 1 and n_sources >= 2:
        citation = 20
    elif n_verified >= 1:
        citation = 17
    elif n_sources >= 1:
        citation = 10
    else:
        citation = 0
    accuracy = 0
    if has_content(p.get("summary")) and has_content(p.get("definition")):
        accuracy += 10
    if n_verified >= 1:
        accuracy += 9
    if present >= 6:
        accuracy += 6
    accuracy = min(25, accuracy)
    relations = 10 if n_relations >= 1 else 6
    classification = 5 if (p.get("mapping") or p.get("category_id")) else 0
    clarity = 5 if has_content(p.get("summary")) else 0
    currency = 5
    score = structure + analysis + citation + accuracy + relations + classification + clarity + currency
    detail = "structure=%d analysis=%d citation=%d accuracy=%d relations=%d classification=%d clarity=%d currency=%d" % (
        structure, analysis, citation, accuracy, relations, classification, clarity, currency)
    return score, detail, words


def ensure_source(cur, src):
    if src.get("doi"):
        cur.execute("SELECT id FROM kb_sources WHERE doi=%s LIMIT 1", (src["doi"],))
        r = cur.fetchone()
        if r:
            return r[0]
    cur.execute("SELECT id FROM kb_sources WHERE title_en=%s AND year=%s LIMIT 1",
                (src["title_en"], src["year"]))
    r = cur.fetchone()
    if r:
        return r[0]
    cur.execute("""INSERT INTO kb_sources
        (kind,title_fa,title_en,year,publisher,doi,isbn,issn,url,language,access_type,bibliographic,work_id)
        VALUES (%s,%s,%s,%s,%s,%s,%s,NULL,%s,%s,'unknown',%s,NULL)""",
                (src["kind"], src["title_fa"], src["title_en"], src["year"], src["publisher"],
                 src.get("doi"), src.get("isbn"), src.get("url"), src["language"],
                 json.dumps({"authors": src["authors"], "citation": src["citation"]}, ensure_ascii=False)))
    return cur.lastrowid



YEAR_FIX.update({
    "MC-582": "year corrected 2000 -> 2001 (verified anchor: Baker & Martinson, TARES Test, 2001); note: editorial card theorist attribution was unverifiable and documentation rebuilt from verified literature",
    "MC-598": "no year change; note: editorial card core_logic was a mismatched media-economics template, documentation rebuilt from Heath (1993) and Ihlen (2011)",
})


def main():
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="433700",
                           database=DB, charset="utf8mb4", autocommit=False)
    cur = conn.cursor()
    codes = list(ENRICH.keys())
    ph = ",".join(["%s"] * len(codes))
    cur.execute("SELECT id,code,properties FROM kb_entities WHERE code IN (%s)" % ph, codes)
    rows = cur.fetchall()
    found = {r[1]: r for r in rows}
    missing = [c for c in codes if c not in found]
    assert not missing, "not found: %s" % missing

    snap = []
    for code, (eid, _c, props) in found.items():
        snap.append({"id": eid, "code": code, "properties": json.loads(props)})
    with open(BACKUP, "w", encoding="utf-8") as f:
        json.dump(snap, f, ensure_ascii=False, indent=1)
    print("backup ->", len(snap), "rows")

    for code in codes:
        eid, _c, props = found[code]
        p = json.loads(props)
        en = ENRICH[code]

        if "critique_text" in en:
            p["critique"] = en["critique_text"]
        if "example_text" in en:
            p["example"] = en["example_text"]
        for k, v in en.items():
            if k in ("critique_text", "example_text"):
                continue
            p[k] = v

        p["sources"] = []
        p["citations"] = []
        for src in S[code]:
            p["sources"].append({
                "citation": src["citation"],
                "title_en": src["title_en"],
                "title_fa": src["title_fa"],
                "year": src["year"],
                "doi": src.get("doi"),
                "url": src.get("url"),
                "language": src["language"],
                "verified": src["verified"],
            })
            p["citations"].append({
                "source": src["citation"],
                "locator": src["locator"],
                "supports": src["supports"],
                "verified": src["verified"],
            })

        cur.execute("SELECT COUNT(*) FROM kb_relations WHERE source_id=%s OR target_id=%s", (eid, eid))
        n_rel = cur.fetchone()[0]
        n_sources = len(p["sources"])
        n_verified = sum(1 for x in p["citations"] if x.get("verified"))
        score, detail, words = rubric(p, n_verified, n_sources, n_rel)

        p["quality_score"] = score
        p["quality_assessment"] = "ارزیابی خودکار SPEC §6.1: %d/100 (نمره پایه؛ نیازمند بازبینی علمی انسانی)" % score
        p["status_scientific_note"] = "مستندسازی با منابع تأییدشده شبکه‌ای؛ نمره بر پایه سنجه خودکار است و جانشین داوری علمی (SPEC §6.4) نیست."
        p["updated_at"] = NOW
        p["updated_by"] = STAMP

        if code in NAME_FIX:
            fa_name, en_name, why = NAME_FIX[code]
            cur.execute("UPDATE kb_entities SET canonical_name_fa=%s, canonical_name_en=%s WHERE id=%s",
                        (fa_name, en_name, eid))
            cur.execute("""INSERT INTO kb_audit_log (entity_code,action,detail,source,created_at)
                VALUES (%s,'DOC_FIX',%s,%s,%s)""",
                        (code, json.dumps({"fix": why}, ensure_ascii=False), STAMP, NOW))

        if code in YEAR_FIX:
            cur.execute("""INSERT INTO kb_audit_log (entity_code,action,detail,source,created_at)
                VALUES (%s,'DOC_FIX',%s,%s,%s)""",
                        (code, json.dumps({"fix": YEAR_FIX[code]}, ensure_ascii=False), STAMP, NOW))

        cur.execute("UPDATE kb_entities SET properties=%s, version=version+1, updated_at=%s WHERE id=%s",
                    (json.dumps(p, ensure_ascii=False), NOW, eid))
        cur.execute("SELECT version FROM kb_entities WHERE id=%s", (eid,))
        new_version = cur.fetchone()[0]

        for src in S[code]:
            sid = ensure_source(cur, src)
            cur.execute("SELECT id FROM kb_evidence WHERE about_code=%s AND source_id=%s LIMIT 1", (code, sid))
            if cur.fetchone():
                continue
            lt = {"work": "SECTION", "page_range": "PAGE", "CHAPTER": "CHAPTER", "PAGE": "PAGE"}.get(src["locator_type"], "SECTION")
            cur.execute("""INSERT INTO kb_citations
                (source_id,locator_type,locator_value,quoted_text,paraphrase,citation_style,language,accessed_at)
                VALUES (%s,%s,%s,NULL,%s,'apa',%s,%s)""",
                        (sid, lt, src["locator"], src["supports"], src["language"], NOW))
            cid = cur.lastrowid
            cur.execute("""INSERT INTO kb_evidence
                (source_id,citation_id,about_code,evidence_type,evidence_summary,quoted_content,locator,
                 page_start,page_end,direction,extraction_method,verification_status,extraction_confidence)
                VALUES (%s,%s,%s,'bibliographic_reference',%s,NULL,%s,NULL,NULL,'supports','ai_extraction',%s,NULL)""",
                        (sid, cid, code, src["supports"], src["locator"],
                         "verified" if src["verified"] else "unverified"))

        cur.execute("""INSERT INTO kb_entity_versions
            (entity_id,version,snapshot,change_reason,changed_by,created_at)
            VALUES (%s,%s,%s,%s,%s,%s)""",
                    (eid, new_version, json.dumps(p, ensure_ascii=False),
                     "full documentation enrichment + verified sources", STAMP, NOW))

        cur.execute("""INSERT INTO kb_audit_log (entity_code,action,detail,source,created_at)
            VALUES (%s,'DOC_ENRICH',%s,%s,%s)""",
                    (code, json.dumps({"score": score, "words": words, "sources": n_sources,
                                       "verified": n_verified, "batch": 200}, ensure_ascii=False),
                     STAMP, NOW))

        print("%s: score=%d words=%d sources=%d verified=%d relations=%d | %s"
              % (code, score, words, n_sources, n_verified, n_rel, detail))

    conn.commit()
    conn.close()
    print("BATCH200 FRAMEWORK DONE")


if __name__ == "__main__":
    main()
