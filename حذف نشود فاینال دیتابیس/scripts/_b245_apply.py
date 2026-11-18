# -*- coding: utf-8 -*-
"""Batch 245: critical/contextual closing for eight near-complete theory cards."""
import json
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch245-20261117"
NOW = "2026-11-17 00:00:00"

APPEND = {
    "MC-060": ("summary", " با این حال، این مصونیت «مطلق» نیست: اصلاحیه‌ها و قوانین پس از آن برای مواد مجرمانه، "
               "مالکیت فکری و در برخی ایالت‌ها افترا استثناهایی افزوده‌اند. مقررات خدمات دیجیتال اتحادیهٔ اروپا (۲۰۲۲) "
               "الگوی دیگری با الزام «شفافیت الگوریتمی»، «ارزیابی ریسک» و «رسیدگی به شکایت» معرفی کرده است؛ "
               "منتقدان می‌گویند مصونیت میانجی، اعتدال محتوا را به شرکت‌های خصوصی سپرده و به «حاکمیت خصوصی» بر گفتار عمومی انجامیده است."),
    "MC-115": ("summary", " این مفهوم با کار بری ولمن و همکارانش پیوند دارد که گذار از «اجتماعی‌شدن در مکان» به "
               "«شبکه‌سازی فرد» را توصیف می‌کنند: فرد محور شبکه است و «قابلیت‌های» (affordances) پلتفرم — "
               "مانند «همیشه‌در‌تماس‌بودن»، «عمومیت‌سازی» و «قابلیت جست‌وجو» — شکل و دامنهٔ این شبکه را تعیین می‌کنند. "
               "منتقدان هشدار می‌دهند که فردگرایی شبکه‌ای می‌تواند به انزوای اجتماعی، فرسودگی از «حضور دائمی» و "
               "نامرئی‌شدن کار مراقبت بینجامد؛ بوید نیز خود بر نابرابری دسترسی و مهارت تأکید می‌کند."),
    "MC-183": ("summary", " بیکچندانی، هرشلایفر و ولش نشان می‌دهند آبشارها شکننده‌اند: اطلاعات خصوصیِ کنارگذاشته‌شده "
               "با یک «شوک اطلاعاتی» کوچک می‌تواند کل جمع را از مسیر منحرف کند. در حوزهٔ رسانه، آبشارها توضیح می‌دهند "
               "چرا «موج» پوشش خبری، مُدهای مصرف یا باورهای جمعی بدون پشتوانهٔ واقعی شکل می‌گیرند و چرا "
               "«تصحیح» پس از وقوع دشوار است؛ نقش رسانه در این میان، هم‌زمان «تسهیل» و «شکستن» آبشار است."),
    "MC-026": ("summary", " در محیط دیجیتال، این سه «ابزار Persuasion» بازآرایی شده‌اند: اتوس از راه «اعتبارسنجی» "
               "(verification)، نشان‌های تیک و شمار فالوور سنجیده می‌شود؛ پاتوس با طراحی احساس‌محور، "
               "محتوای ویدئویی کوتاه و الگوریتم‌های تعامل‌محور تقویت می‌شود؛ و لوگوس با داده‌نمایی، "
               "نمودار و پیوند به منابع پشتیبانی می‌شود. نقد اصلی آن است که این سازوکارها گاه "
               "«اعتبار ظاهری» را جای «اعتبار واقعی» می‌نشانند و احساس را بر استدلال پیش می‌اندازند."),
    "MC-122": ("summary", " در این نظریه، «نوع بحران» و «شدت مسئولیت ادراک‌شده» پاسخ مناسب را تعیین می‌کند: "
               "از «انکار» و «کاهش» تا «جبران» و «عذرخواهی» و «وعدهٔ اصلاح». کوپس تأکید می‌کند که "
               "پیش از پاسخ، سازمان باید «تاریخچهٔ بحران» و «شهرت پیشین» خود را در نظر بگیرد. "
               "منتقدان می‌گویند مدل بیش از اندازه بر «مسئولیت» متمرکز است و نقش احساسات، "
               "پلتفرم‌های اجتماعی و «بحران‌های هم‌زمان چندگانه» را کم‌برجسته می‌کند."),
    "MC-134": ("summary", " این نظریه سه «عرض» (latitude) را در نگرش فرد متمایز می‌کند: «پذیرش» (acceptance)، "
               "«بی‌طرفی» (non-commitment) و «رد» (rejection)؛ پیام‌های نزدیک به نگرش فرد «جذب» (assimilation) "
               "و پیام‌های دور «تقابل» (contrast) ادراک می‌شوند. هرچه «درگیری خودی» (ego-involvement) بیشتر باشد، "
               "عرض پذیرش باریک‌تر و مقاومت شدیدتر است. کاربرد رسانه‌ای آن توضیح شکست کمپین‌ها در مخاطبان "
               "به‌شدت متعهد است؛ نقد اصلی، دشواری سنجش عرض‌ها و نادیده‌گرفتن تغییر نگرش تدریجی است. "
               "کاربرد تازهٔ آن در تحلیل «قطبی‌شدن» (polarization) سیاسی و شبکه‌های اجتماعی است، جایی که "
               "عرض رد بسیار باریک، گفت‌وگوی میان‌گروهی را دشوار می‌کند."),
    "MC-047": ("summary", " بوردیو میدان روزنامه‌نگاری را فضایی میان دو قطب «خودمختاری» (autonomy) و «دگرمختاری» "
               "(heteronomy) می‌داند: قطب نخست با معیارهای حرفه‌ای و اعتبار نمادین و قطب دوم با منطق بازار و "
               "شمار مخاطب تعریف می‌شود. «بنسون» و «نوین» نشان داده‌اند که ساختار مالکیت، "
               "سرمایهٔ نمادین و «هم‌سویی سیاسی» جایگاه هر رسانه را در این میدان تعیین می‌کند؛ "
               "نقد واردشده آن است که مفهوم میدان، عاملیت روزنامه‌نگار و نابرابری دسترسی دیجیتال را کم‌برجسته می‌کند."),
    "MC-087": ("summary", " کلاپر این سه سازوکار را «عوامل میانجی» (mediating factors) می‌داند و نتیجه می‌گیرد که "
               "رسانه اغلب «تقویت‌کننده» نگرش‌های پیشین است، نه تغییردهندهٔ آن‌ها؛ از این رو به «اثرات محدود» "
               "(limited effects) معروف شد. پژوهش‌های بعدی نشان دادند گزینش همیشه به تقویت نمی‌انجامد و "
               "در محیط «اطلاعات فراوان» (high-choice) امروز، «حباب‌های فیلتر» (filter bubbles) و "
               "«اتاق‌های پژواک» (echo chambers) شکل تازه‌ای از گزینش‌گری پدید آورده‌اند. "
               "کلاپر خود تأکید داشت که گزینش‌گری به «وضعیت روانی» و «وابستگی گروهی» مخاطب وابسته است و "
               "در محیط چندرسانه‌ای، اثر رسانه به «هم‌راستایی» با منابع دیگر بستگی دارد."),
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
                    (code, json.dumps({"batch": 245, "score": t, "words": w}, ensure_ascii=False), STAMP, NOW))
    conn.commit()
    conn.close()
    print("BATCH245 DONE")


if __name__ == "__main__":
    main()
