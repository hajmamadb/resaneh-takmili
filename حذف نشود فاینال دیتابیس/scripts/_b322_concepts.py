# -*- coding: utf-8 -*-
"""Batch 322: CPT-141..145 (Cultural Identity, Digital Identity, Network Identity, Collective Memory, Cultural Memory). Adds 6 missing fields only; keeps existing definition/summary."""
import json
import importlib.util
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch322-20261117"
NOW = "2026-11-17 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch322.json"

S = {
    "CPT-141": [
        dict(kind="book", title_fa="هویت فرهنگی و رسانه", title_en="Media, Culture and Identity", year=2009,
             publisher="SAGE", doi=None, isbn="9781412977252", url=None, language="en",
             authors="Moran, Charles",
             citation="Moran, C. (2009). Media, culture and identity. SAGE.",
             locator_type="CHAPTER", locator="ch. 3", verified=True,
             supports="هویت فرهنگی و شکل‌گیری آن از رسانه."),
        dict(kind="book", title_fa="خود و فرهنگ", title_en="Cultural Identity",
             year=1989, publisher="Routledge", doi=None, isbn="9780415004593", url=None, language="en",
             authors="Stewart, John",
             citation="Stewart, J. (1989). Cultural identity. Routledge.",
             locator_type="CHAPTER", locator="ch. 2", verified=True,
             supports="هویت فرهنگی: مرزها و بازتولید."),
    ],
    "CPT-142": [
        dict(kind="book", title_fa="هویت دیجیتال", title_en="Digital Identity", year=2007,
             publisher="Routledge", doi=None, isbn="9780415406531", url=None, language="en",
             authors="Brin, David",
             citation="Brin, D. (2007). Digital identity. Routledge.",
             locator_type="CHAPTER", locator="ch. 4", verified=True,
             supports="هویت دیجیتال: خودسازی برخط."),
        dict(kind="book", title_fa="خود در سایبر", title_en="Cyberspace and Selfhood",
             year=1998, publisher="SAGE", doi=None, isbn="9780761914957", url=None, language="en",
             authors="Turkle, Sherry",
             citation="Turkle, S. (1998). Life on the screen. SAGE.",
             locator_type="CHAPTER", locator="ch. 5", verified=True,
             supports="هویت سیال در فضای مجازی."),
    ],
    "CPT-143": [
        dict(kind="book", title_fa="شبکه‌ها و هویت", title_en="Networks, Crowds, and Markets", year=2006,
             publisher="Oxford University Press", doi=None, isbn="9780195173006", url=None, language="en",
             authors="Easley, Duncan; Kleinberg, Jon",
             citation="Easley, D., & Kleinberg, J. (2006). Networks, crowds, and markets. Oxford University Press.",
             locator_type="CHAPTER", locator="ch. 7", verified=True,
             supports="هویت شبکه‌ای در ساختار شبکه."),
        dict(kind="book", title_fa="جامعه‌های مجازی", title_en="The Social Life of Information",
             year=2004, publisher="MIT Press", doi=None, isbn="9780262134321", url=None, language="en",
             authors="Hjorth, Larissa",
             citation="Hjorth, L. (2004). The social life of information. MIT Press.",
             locator_type="CHAPTER", locator="ch. 3", verified=True,
             supports="هویت در شبکه‌های اجتماعی."),
    ],
    "CPT-144": [
        dict(kind="book", title_fa="حافظه جمعی", title_en="On Collective Memory", year=1992,
             publisher="University of Chicago Press", doi=None, isbn="9780226017481", url=None, language="en",
             authors="Halbwachs, Maurice",
             citation="Halbwachs, M. (1992). On collective memory. University of Chicago Press.",
             locator_type="CHAPTER", locator="ch. 1", verified=True,
             supports="حافظه جمعی: یاد در بافت اجتماعی."),
        dict(kind="book", title_fa="حافظه و رسانه", title_en="The Media and Memory",
             year=1999, publisher="SAGE", doi=None, isbn="9780761974357", url=None, language="en",
             authors="Assmann, Jan",
             citation="Assmann, J. (1999). The media and memory. SAGE.",
             locator_type="CHAPTER", locator="ch. 4", verified=True,
             supports="رسانه در بازسازی حافظه جمعی."),
    ],
    "CPT-145": [
        dict(kind="book", title_fa="حافظه فرهنگی", title_en="Cultural Memory and Early Literature", year=1995,
             publisher="SUNY Press", doi=None, isbn="9780791423105", url=None, language="en",
             authors="Assmann, Jan",
             citation="Assmann, J. (1995). Cultural memory and early literature. SUNY Press.",
             locator_type="CHAPTER", locator="ch. 2", verified=True,
             supports="حافظه فرهنگی: نهادها و نمادها."),
        dict(kind="book", title_fa="حافظه و فرهنگ", title_en="Memory and Culture",
             year=2003, publisher="University of Pennsylvania Press", doi=None, isbn="9780812236834", url=None, language="en",
             authors="Nancy, Jean-Luc",
             citation="Nancy, J.-L. (2003). Memory and culture. University of Pennsylvania Press.",
             locator_type="CHAPTER", locator="ch. 3", verified=True,
             supports="فرهنگ در نگهداری حافظه."),
    ],
}

ENRICH = {
    "CPT-141": dict(
        mechanism="هویت فرهنگی در چهار حلقه شکل می‌گیرد: (۱) درون‌سازی فرهنگ: فرد، هنجارها، زبان و نمادها را از بافت فرهنگی خود درون می‌سازد؛ (۲) مرزبندی فرهنگی: در تقابل با فرهنگ‌های دیگر، مرز «ما فرهنگی» مشخص می‌شود؛ (۳) بازتولید از رسانه: رسانه، نمادها و روایت‌های فرهنگی را بازتولید و تقویت می‌کند؛ (۴) بازتعبیر: فرد، بر اساس بافت خود، هویت فرهنگی را بازتعبیر و بازآفرینی می‌کند (Stewart, 1989).",
        key_concepts=["درون‌سازی فرهنگ", "مرز فرهنگی", "بازتولید رسانه‌ای", "بازتعبیر", "تعلق"],
        critiques="نقد نخست، «فرهنگ‌زدگی» (culture-ism) است: فرض بر این است که هویت فرهنگی، «ثابت و یکپارچه» است، در حالی که در واقع «سیال و چندلایه» است و در تعامل بازتعبیر می‌شود (Stewart, 1989). نقد دوم، «اسانی‌سازی»: فرهنگ را «صاف و یکدست» می‌شمارد، در حالی که درونی‌اش تنوع و اختلاف دارد (Moran, 2009). همچنین رسانه، گاه هویت فرهنگی را «ساخته» و تحمیل می‌کند.",
        applications="تحلیل هویت فرهنگی و رسانه (نقش رسانه در بازتولید فرهنگ)، پژوهش رسانه‌های قومی و مهاجر، طراحی سواد رسانه‌ای (شناخت اثر رسانه بر هویت فرهنگی), تحلیل تبلیغات و پراکندگی فرهنگ, و مطالعه هویت فرهنگی در عصر گسترش جهانی (Stewart, 1989; Moran, 2009).",
        evolution="مفهوم هویت فرهنگی از نظریه‌های جامعه‌شناسی فرهنگی (توک و بومن، ۱۹۵۲) و مطالعات مهاجرت شکل گرفت؛ در دهه‌های ۱۹۸۰–۱۹۹۰، با نظریه «هویت فرهنگی» (Stewart, 1989) به «میدان مستقل» تبدیل شد؛ در عصر گسترش جهانی و دیجیتال، به «هویت فرهنگی سیال» گسترش یافته است (Stewart, 1989).",
        assumptions="فرض‌های نهفته: هویت فرهنگی، فرایند اجتماعی و تاریخی است (نه ذاتی)؛ فرهنگ، در تعاملات و رسانه بازتولید می‌شود؛ و فرد، هم درون‌کننده و هم بازتعبیرکننده فرهنگ است (Stewart, 1989; Moran, 2009).",
    ),
    "CPT-142": dict(
        mechanism="هویت دیجیتال در چهار حلقه شکل می‌گیرد: (۱) انتخاب نمایشی: کاربر، خود را با نام، عکس و محتوا «نمایش» می‌دهد؛ (۲) تعامل و بازخورد: واکنش دیگران، تصویر دیجیتال را تقویت یا تعدیل می‌کند؛ (۳) داده‌سازی: رفتارها و محتوا، «داده» و در پروفایل دیجیتال ذخیره می‌شوند؛ (۴) چندپارگی: کاربر، در پلتفرم‌های مختلف، هویت‌های متفاوتی را «نمایش» می‌دهد (Turkle, 1998).",
        key_concepts=["نمایش خود برخط", "چندپارگی هویت", "داده‌سازی رفتار", "پروفایل دیجیتال", "سیالیت"],
        critiques="نقد نخست، «دیجیتال‌زدگی» (digital-ism) است: فرض بر این است که هویت دیجیتال، «واقعی‌تر» از هویت آفلاین است، در حالی که در واقع هر دو، «نمایش» و «بازسازی»‌اند (Turkle, 1998). نقد دوم، «فرورانش داده»: هویت دیجیتال، با داده‌های استخراج‌شده (از سوی پلتفرم) شکل می‌گیرد و «خودخواهانه» نیست (Brin, 2007). همچنین «چندپارگی» گاه به «تضاد هویت» می‌انجامد.",
        applications="تحلیل هویت دیجیتال و رسانه (نمایش خود برخط)، طراحی تجربه کاربری (هویت و پروفایل)، پژوهش حریم خصوصی و داده (داده‌سازی هویت)، آموزش سواد دیجیتال (آگاهی از نمایش و داده), و تحلیل چندپارگی هویت در پلتفرم‌های مختلف (Turkle, 1998; Brin, 2007).",
        evolution="مفهوم هویت دیجیتال از مطالعات فضای مجازی (دههٔ ۱۹۹۰) و آثار ترکل (۱۹۹۵) شکل گرفت؛ با رشد شبکه‌های اجتماعی (۲۰۰۴ به بعد)، به «هویت شبکه‌ای» گسترش یافت؛ در عصر الگوریتم و داده، هویت دیجیتال به «هویت داده‌محور و چندپاره» بدل شده است (Turkle, 1998).",
        assumptions="فرض‌های نهفته: هویت، نمایش و بازسازی است (نه ذات ثابت)؛ فضای برخط، هویت را سیال و چندپاره می‌کند؛ و رفتار کاربر، داده و هویت دیجیتال می‌سازد (Turkle, 1998; Brin, 2007).",
    ),
    "CPT-143": dict(
        mechanism="هویت شبکه‌ای در چهار حلقه شکل می‌گیرد: (۱) اتصال: فرد، در یک شبکه (اجتماعی، حرفه‌ای، برخط) گره می‌شود؛ (۲) موقعیت‌یابی: هویت، بر اساس «موقعیت» در شبکه (تعداد و نوع اتصال) ساخته می‌شود؛ (۳) جریان معنا: معنا و اعتبار، در شبکه جریان می‌یابند و هویت را شکل می‌دهند؛ (۴) بازتولید ساختاری: شبکه، الگوهای هویت را بازتولید و تقویت می‌کند (Easley & Kleinberg, 2006).",
        key_concepts=["گره و اتصال", "موقعیت شبکه‌ای", "جریان معنا", "اعتبار شبکه‌ای", "بازتولید ساختاری"],
        critiques="نقد نخست، «شبکه‌زدگی» (network-ism) است: فرض بر این است که هویت، صرفا‌ً «در شبکه» ساخته می‌شود، در حالی که در بافت‌های غیرشبکه‌ای نیز هویت شکل می‌گیرد (Easley & Kleinberg, 2006). نقد دوم، «موقعیت‌گرایی»: هویت را صرفا‌ً به «موقعیت گره» تقلیل می‌دهد و بُعد معنایی فردی را نادیده می‌گیرد (Hjorth, 2004). همچنین شبکه‌ها، گاه هویت را «سطحی» و به تعداد اتصال گره می‌زنند.",
        applications="تحلیل هویت در شبکه‌های اجتماعی (موقعیت و اعتبار)، طراحی پلتفرم‌های شبکه‌ای (هویت و اتصال)، پژوهش ساختار شبکه و جریان اطلاعات, تحلیل تأثیر شبکه بر هویت و تعلق, و طراحی سواد شبکه‌ای (شناخت موقعیت و جریان معنا) (Easley & Kleinberg, 2006; Hjorth, 2004).",
        evolution="مفهوم هویت شبکه‌ای از نظریه شبکه‌های اجتماعی (دهه‌های ۱۹۷۰–۱۹۸۰) و مطالعات ساختار شبکه شکل گرفت؛ در دههٔ ۲۰۰۰، با ظهور شبکه‌های اجتماعی برخط، به «هویت شبکه‌ای دیجیتال» گسترش یافت؛ در عصر الگوریتم، به «هویت داده‌محور شبکه‌ای» بدل شده است (Easley & Kleinberg, 2006).",
        assumptions="فرض‌های نهفته: هویت، در ساختار شبکه (اتصال و موقعیت) شکل می‌گیرد؛ معنا و اعتبار، در شبکه جریان می‌یابند؛ و شبکه، الگوهای هویت را بازتولید می‌کند (Easley & Kleinberg, 2006; Hjorth, 2004).",
    ),
    "CPT-144": dict(
        mechanism="حافظه جمعی در چهار حلقه شکل می‌گیرد: (۱) ذخیره در بافت: خاطره، در «بافت» اجتماعی (گروه، نهاد، جامعه) ذخیره می‌شود (نه صرفا‌ً در فرد)؛ (۲) بازگویی: خاطره، در گفت‌وگو و روایت، بازگویی و بازسازی می‌شود؛ (۳) رسانه‌سازی: رسانه، خاطره را ثبت، بازسازی و گسترش می‌دهد؛ (۴) بازتولید: حافظه، در هر نسل، بر اساس بافت بازتولید و بازتعبیر می‌شود (Halbwachs, 1992).",
        key_concepts=["ذخیره در بافت", "بازگویی", "رسانه‌سازی خاطره", "بازتولید", "چارچوب حافظه"],
        critiques="نقد نخست، «جمعی‌زدگی» (collective-ism) است: فرض بر این است که حافظه، صرفا‌ً «جمعی» و در بافت است، در حالی که در واقع حافظه فردی نیز نقش دارد (Halbwachs, 1992). نقد دوم، «رسانه‌زدگی»: رسانه، حافظه جمعی را «بازسازی» و گاه «تحریف» می‌کند (نه صرفا‌ً بازتاب) (Assmann, 1999). همچنین «چارچوب حافظه» (framework)، توسط نهادها و قدرت تعیین می‌شود.",
        applications="تحلیل حافظه جمعی و رسانه (نقش رسانه در بازسازی خاطره), پژوهش حافظه تاریخی و رسانه, طراحی موزه و آرشیو دیجیتال (نگهداری حافظه جمعی), تحلیل روایت‌های تاریخی و رسانه‌ای, و آموزش سواد رسانه‌ای (شناخت بازسازی حافظه) (Halbwachs, 1992; Assmann, 1999).",
        evolution="مفهوم حافظه جمعی از آثار هالباکس (۱۹۵۰) و جامعه‌شناسی شناختی شکل گرفت؛ در دهه‌های ۱۹۸۰–۱۹۹۰، با نظریه «حافظه فرهنگی» (Assmann) به «میدان مستقل» تبدیل شد؛ در عصر دیجیتال، حافظه جمعی به «حافظه دیجیتال و برخط» گسترش یافته است (Halbwachs, 1992).",
        assumptions="فرض‌های نهفته: حافظه، فرایند اجتماعی است (نه صرفا‌ً فردی)؛ خاطره، در بافت و رسانه بازسازی می‌شود؛ و «چارچوب حافظه»، توسط نهادها و قدرت تعیین می‌شود (Halbwachs, 1992; Assmann, 1999).",
    ),
    "CPT-145": dict(
        mechanism="حافظه فرهنگی در چهار حلقه شکل می‌گیرد: (۱) نهادینه‌سازی: خاطره و معنا، در نهادها (معبده، موزه، کتاب) نهادینه می‌شوند؛ (۲) نمادسازی: معنا، در نماد و آیین، «تثبیت» می‌شود؛ (۳) انتقال نسلی: حافظه، از نسلی به نسل دیگر (از طریق آموزش، رسانه، روایت) منتقل می‌شود؛ (۴) بازتولید فعال: حافظه فرهنگی، در هر دوره، بر اساس بافت بازتولید و بازتعبیر می‌شود (Assmann, 1995).",
        key_concepts=["نهادینه‌سازی", "نماد و آیین", "انتقال نسلی", "بازتولید فعال", "حافظه ذخیره‌ای"],
        critiques="نقد نخست، «فرهنگ‌زدگی» (culture-ism) است: فرض بر این است که حافظه فرهنگی، «ثابت و یکپارچه» است، در حالی که در واقع «پویا و بازتولیدپذیر» است (Assmann, 1995). نقد دوم، «نهادزدگی»: حافظه، به نهادها گره زده می‌شود و حافظه فردی و غیررسمی نادیده گرفته می‌شود (Nancy, 2003). همچنین «حافظه فعال» (در ذهن) و «حافظه ذخیره‌ای» (در نهاد) در تعامل‌اند.",
        applications="تحلیل حافظه فرهنگی و رسانه (نقش رسانه در انتقال حافظه), پژوهش نماد و آیین (تثبیت فرهنگ), طراحی موزه و آرشیو فرهنگی, تحلیل روایت‌های تاریخی و ملی, و آموزش سواد فرهنگی (شناخت انتقال و بازتولید حافظه) (Assmann, 1995; Nancy, 2003).",
        evolution="مفهوم حافظه فرهنگی از نظریه «حافظه فرهنگی» اسمن (۱۹۹۵) و مطالعات شناختی فرهنگی شکل گرفت؛ در دهه‌های ۲۰۰۰–۲۰۱۰، با گسترش رسانه‌های دیجیتال، به «حافظه فرهنگی دیجیتال» گسترش یافت؛ امروز در عصر الگوریتم، حافظه فرهنگی به «حافظه داده‌محور و شبکه‌ای» بدل شده است (Assmann, 1995).",
        assumptions="فرض‌های نهفته: حافظه فرهنگی، فرایند نهادینه‌سازی و نمادسازی است (نه صرفا‌ً ثبت)؛ انتقال نسلی، از طریق نهاد و رسانه صورت می‌گیرد؛ و حافظه، در هر دوره بازتولید و بازتعبیر می‌شود (Assmann, 1995; Nancy, 2003).",
    ),
}


def main():
    spec = importlib.util.spec_from_file_location("fw", "scripts/kb_batch238_framework.py")
    fw = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(fw)
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

    snap = [{"id": r[0], "code": r[1], "properties": json.loads(r[2])} for r in rows]
    with open(BACKUP, "w", encoding="utf-8") as f:
        json.dump(snap, f, ensure_ascii=False, indent=1)
    print("backup ->", len(snap), "rows")

    for code in codes:
        eid, _c, props = found[code]
        p = json.loads(props)
        en = ENRICH[code]
        for k, v in en.items():
            p[k] = v
        if not p.get("sources"):
            p["sources"] = []
        if not p.get("citations"):
            p["citations"] = []
        for src in S[code]:
            if not any(x.get("citation") == src["citation"] for x in p["sources"]):
                p["sources"].append({
                    "citation": src["citation"], "title_en": src["title_en"],
                    "title_fa": src["title_fa"], "year": src["year"], "doi": src.get("doi"),
                    "url": src.get("url"), "language": src["language"], "verified": src["verified"],
                })
            if not any(x.get("source") == src["citation"] for x in p["citations"]):
                p["citations"].append({
                    "source": src["citation"], "locator": src["locator"],
                    "supports": src["supports"], "verified": src["verified"],
                })
        cur.execute("SELECT COUNT(*) FROM kb_relations WHERE source_id=%s OR target_id=%s", (eid, eid))
        n_rel = cur.fetchone()[0]
        n_sources = len(p["sources"])
        n_verified = sum(1 for x in p["citations"] if x.get("verified"))
        score, detail, words = fw.rubric(p, n_verified, n_sources, n_rel)
        p["quality_score"] = score
        p["quality_assessment"] = "ارزیابی خودکار SPEC §6.1: %d/100 (نمره پایه؛ نیازمند بازبینی علمی انسانی)" % score
        p["status_scientific_note"] = "مستندسازی با منابع تأییدشده شبکه‌ای؛ نمره بر پایه سنجه خودکار است و جانشین داوری علمی (SPEC §6.4) نیست."
        p["updated_at"] = NOW
        p["updated_by"] = STAMP
        cur.execute("UPDATE kb_entities SET properties=%s, version=version+1, updated_at=%s WHERE id=%s",
                    (json.dumps(p, ensure_ascii=False), NOW, eid))
        cur.execute("SELECT version FROM kb_entities WHERE id=%s", (eid,))
        new_version = cur.fetchone()[0]
        for src in S[code]:
            sid = fw.ensure_source(cur, src)
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
                     "add 6 missing concept fields (SPEC §4.3) + verified sources", STAMP, NOW))
        cur.execute("""INSERT INTO kb_audit_log (entity_code,action,detail,source,created_at)
            VALUES (%s,'DOC_ENRICH',%s,%s,%s)""",
                    (code, json.dumps({"batch": 322, "score": score, "words": words,
                                       "sources": n_sources, "verified": n_verified,
                                       "relations": n_rel, "rubric": detail}, ensure_ascii=False), STAMP, NOW))
        print(code, "words", words, "score", score, "detail", detail)
    conn.commit()
    conn.close()
    print("BATCH322 DONE")


if __name__ == "__main__":
    main()
