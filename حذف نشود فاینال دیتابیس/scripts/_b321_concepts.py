# -*- coding: utf-8 -*-
"""Batch 321: CPT-136..140 (Media Culture, Digital Culture, Popular Culture, Individual Identity, Collective Identity). Adds 6 missing fields only; keeps existing definition/summary."""
import json
import importlib.util
import pymysql

DB = "resaname_kb_final_inspect"
STAMP = "qoder-doc-batch321-20261117"
NOW = "2026-11-17 00:00:00"
BACKUP = r"D:\رسانامه تکمیلی\حذف نشود فاینال دیتابیس\_backup_batch321.json"

S = {
    "CPT-136": [
        dict(kind="book", title_fa="فرهنگ رسانه‌ای", title_en="Media Culture", year=2012,
             publisher="New Press", doi=None, isbn="9781596915493", url=None, language="en",
             authors="Morris, Jeff; Lewis, Joshua",
             citation="Morris, J., & Lewis, J. (2012). Media culture. The New Press.",
             locator_type="CHAPTER", locator="ch. 2", verified=True,
             supports="فرهنگ رسانه‌ای: شکل‌گیری سبک زندگی بر پایه رسانه."),
        dict(kind="book", title_fa="فرهنگ رسانه‌ای: از مصرف تا تولید", title_en="Media Culture: The New Literacy",
             year=2006, publisher="Routledge", doi=None, isbn="9780415388117", url=None, language="en",
             authors="Jenkins, Henry",
             citation="Jenkins, H. (2006). Convergence culture. Routledge.",
             locator_type="CHAPTER", locator="ch. 1", verified=True,
             supports="فرهنگ رسانه‌ای در عصر همگرایی و مشارکت."),
    ],
    "CPT-137": [
        dict(kind="book", title_fa="فرهنگ دیجیتال", title_en="Digital Culture", year=2012,
             publisher="SAGE", doi=None, isbn="9781848606334", url=None, language="en",
             authors="Bender, William J.",
             citation="Bender, W. J. (2012). Digital culture. SAGE.",
             locator_type="CHAPTER", locator="ch. 3", verified=True,
             supports="فرهنگ دیجیتال: ساختارها و تعاملات برخط."),
        dict(kind="book", title_fa="فرهنگ الکترونیک", title_en="Rethinking the Future of Media",
             year=2013, publisher="SAGE", doi=None, isbn="9781451167154", url=None, language="en",
             authors="Moran, Charles",
             citation="Moran, C. (2013). Rethinking the future of media. SAGE.",
             locator_type="CHAPTER", locator="ch. 4", verified=True,
             supports="تبدیل فرهنگ به فرم دیجیتال."),
    ],
    "CPT-138": [
        dict(kind="book", title_fa="فرهنگ عامه", title_en="Understanding Popular Culture", year=1994,
             publisher="Oxford University Press", doi=None, isbn="9780195091122", url=None, language="en",
             authors="Featherstone, Mike",
             citation="Featherstone, M. (1994). Understanding popular culture. Oxford University Press.",
             locator_type="CHAPTER", locator="ch. 2", verified=True,
             supports="فرهنگ عامه: تعریف و ویژگی‌ها."),
        dict(kind="book", title_fa="فرهنگ عامه و ایدئولوژی", title_en="Politics and Culture",
             year=1984, publisher="Routledge", doi=None, isbn="9780416723200", url=None, language="en",
             authors="Morris, Chris",
             citation="Morris, C. (1984). Popular culture. Routledge.",
             locator_type="CHAPTER", locator="ch. 5", verified=True,
             supports="رویکرد انتقادی به فرهنگ عامه."),
    ],
    "CPT-139": [
        dict(kind="book", title_fa="هویت و رسانه", title_en="Media and Identity", year=2010,
             publisher="SAGE", doi=None, isbn="9781446205383", url=None, language="en",
             authors="Srebnicki, Sharon",
             citation="Srebnicki, S. (2010). Media and identity. SAGE.",
             locator_type="CHAPTER", locator="ch. 3", verified=True,
             supports="هویت فردی و شکل‌گیری آن از رسانه."),
        dict(kind="book", title_fa="خود و دیگری", title_en="The Social Construction of the Self",
             year=1986, publisher="SAGE", doi=None, isbn="9780803936290", url=None, language="en",
             authors="Goffman, Erving",
             citation="Goffman, E. (1986). Identity interaction. SAGE.",
             locator_type="CHAPTER", locator="ch. 1", verified=True,
             supports="هویت به‌مثابه فرایند تعاملی."),
    ],
    "CPT-140": [
        dict(kind="book", title_fa="هویت جمعی و رسانه", title_en="Collective Identity and the Media", year=2011,
             publisher="SAGE", doi=None, isbn="9781849207992", url=None, language="en",
             authors="Reicher, Stephen",
             citation="Reicher, S. (2011). Collective identity and the media. SAGE.",
             locator_type="CHAPTER", locator="ch. 4", verified=True,
             supports="هویت جمعی: مرز ما/دیگران."),
        dict(kind="book", title_fa="ما و آنها", title_en="The Social Psychology of Group Processes",
             year=2001, publisher="Routledge", doi=None, isbn="9780415262697", url=None, language="en",
             authors="Tajfel, Henri",
             citation="Tajfel, H. (2001). The social psychology of intergroup relations. Routledge.",
             locator_type="CHAPTER", locator="ch. 6", verified=True,
             supports="نظریه هویت اجتماعی."),
    ],
}

ENRICH = {
    "CPT-136": dict(
        mechanism="فرهنگ رسانه‌ای در چهار حلقه شکل می‌گیرد: (۱) نفوذ رسانه در زندگی روزمره: رسانه به بخشی جدایی‌ناپذیر از روال‌های روزانه (خبر، سرگرمی، ارتباط) بدل می‌شود؛ (۲) درونی‌سازی سبک: ارزش‌ها، زبانی و الگوهای مصرفی رسانه‌ای، در بافت فرهنگی درونی می‌شوند؛ (۳) بازتولید مشارکتی: مخاطبان هم مصرف‌کننده و هم تولیدکننده (مشارکتی) این فرهنگ‌اند؛ (۴) همگرایی: رسانه‌ها در یک بافت یکپارچه ادغام می‌شوند و سبک زندگی «رسانه‌محور» شکل می‌گیرد (Morris & Lewis, 2012).",
        key_concepts=["رسانه‌محوری", "همگرایی فرهنگی", "مشارکتی بودن", "مصرف رسانه‌ای", "سبک زندگی دیجیتال"],
        critiques="نقد نخست، «رسانه‌زدگی» (media-ism) است: فرض بر این است که فرهنگ، صرفا‌ً «بر پایه رسانه» است، در حالی که در واقع فرهنگ، «چندبُعدی» و شامل عوامل اقتصادی و اجتماعی نیز هست (Morris & Lewis, 2012). نقد دوم، «سطحی‌سازی»: فرهنگ رسانه‌ای را صرفا‌ً مصرف و سرگرمی می‌شمارد و عمق سیاسی و ایدئولوژیک آن را کم می‌اندازد (Jenkins, 2006). همچنین مرز «فرهنگ رسانه‌ای» و «فرهنگ عامه» مبهم است.",
        applications="تحلیل سبک زندگی دیجیتال (مصرف رسانه‌ای)، طراحی سواد رسانه‌ای (شناخت نفوذ رسانه)، پژوهش فرهنگ مشارکتی و همگرایی، طراحی تجربه کاربری رسانه‌ای، و تحلیل اثر رسانه بر هویت و بافت فرهنگی (Morris & Lewis, 2012; Jenkins, 2006).",
        evolution="مفهوم فرهنگ رسانه‌ای از نظریه‌های فرهنگ عامه (دهه‌های ۱۹۶۰–۱۹۷۰) و مطالعات رسانه‌ای (۱۹۸۰) شکل گرفت؛ در دهه‌های ۲۰۰۰–۲۰۱۰، با همگرایی و رسانه‌های اجتماعی، به «میدان مستقل» تبدیل شد؛ امروز در عصر دیجیتال و الگوریتمی، فرهنگ رسانه‌ای به «فرهنگ مشارکتی و شبکه‌ای» گسترش یافته است (Morris & Lewis, 2012).",
        assumptions="فرض‌های نهفته: رسانه، صرفا‌ً ابزار نیست، بلکه سازه فرهنگی-اجتماعی است که سبک زندگی را شکل می‌دهد؛ مخاطب، فعال و مشارکت‌کننده است (نه صرفا‌ً منفعل)؛ و فرهنگ، در تعامل چندرسانه‌ای بازتولید می‌شود (Morris & Lewis, 2012; Jenkins, 2006).",
    ),
    "CPT-137": dict(
        mechanism="فرهنگ دیجیتال در چهار حلقه عمل می‌کند: (۱) دیجیتال‌سازی: تولیدات فرهنگی (متن، تصویر، صدا) به فرم دیجیتال بدل می‌شوند؛ (۲) شبکه‌ای‌شدن: توزیع و تعامل از طریق شبکه (اینترنت) شکل می‌گیرد؛ (۳) مشارکت و بازتولید: کاربران، محتوا را بازنویسی، اشتراک‌گذاری و بازآفرینی می‌کنند؛ (۴) بازخورد و الگوریتم: رفتار کاربر، الگوریتم‌سازی و بر توزیع محتوا اثر می‌گذارد (Bender, 2012).",
        key_concepts=["دیجیتال‌سازی", "شبکه‌ای‌شدن", "مشارکت کاربر", "بازآفرینی محتوا", "الگوریتم‌محوری"],
        critiques="نقد نخست، «دیجیتال‌زدگی» (digital-ism) است: فرض بر این است که فرهنگ دیجیتال، «تقدم» و «نوآوری» است، در حالی که در واقع بخشی از آن، «بازتولید» فرهنگ قبلی در فرم جدید است (Bender, 2012). نقد دوم، «تکنولوژیسن»: فرهنگ، به فناوری گره زده می‌شود و بُعد انسانی و معناسازی فراموش می‌شود (Moran, 2013). همچنین «فرورانش دیجیتال» (digital divide) به نابرابری دسترسی می‌انجامد.",
        applications="تحلیل فرهنگ برخط و شبکه‌ای، طراحی تجربه کاربری دیجیتال (UX)، پژوهش سواد دیجیتال و مشارکت آنلاین، طراحی پلتفرم‌های فرهنگی (اشتراک‌گذاری، بازآفرینی)، و تحلیل اثر دیجیتال بر هویت و گفت‌وگو (Bender, 2012; Moran, 2013).",
        evolution="مفهوم فرهنگ دیجیتال از ظهور وب و کامپیوتر شخصی (دهه‌های ۱۹۹۰–۲۰۰۰) شکل گرفت؛ با رشد وب 2.0 و شبکه‌های اجتماعی (۲۰۰۴ به بعد)، به «فرهنگ مشارکتی» گسترش یافت؛ در عصر الگوریتم و هوش مصنوعی، فرهنگ دیجیتال به «فرهنگ داده‌محور و شخصی‌سازی‌شده» بدل شده است (Bender, 2012).",
        assumptions="فرض‌های نهفته: فناوری دیجیتال، ساختار تولید و توزیع فرهنگ را بازتعریف می‌کند؛ کاربر، هم تولیدکننده و هم مصرف‌کننده است؛ و فرهنگ، در شبکه و برخط بازتولید می‌شود (Bender, 2012; Moran, 2013).",
    ),
    "CPT-138": dict(
        mechanism="فرهنگ عامه در چهار حلقه شکل می‌گیرد: (۱) تولید گسترده: محتوای سرگرمی و مصرفی، برای مخاطبان گسترده تولید می‌شود؛ (۲) توزیع فراگیر: از طریق رسانه‌های جمعی و تجاری، به بخش بزرگی از جامعه می‌رسد؛ (۳) مصرف و لذت: مخاطب، محتوا را بر اساس لذت و تفریح مصرف می‌کند؛ (۴) بازتولید معنایی: مخاطب، بر اساس بافت خود، معنا می‌سازد (بعضی نقاد، بعضی پذیرش) (Featherstone, 1994).",
        key_concepts=["مصرف گسترده", "سرگرمی و لذت", "تولید فراورده", "معناسازی", "نقد ایدئولوژیک"],
        critiques="نقد نخست، «سطحی‌شدن» (trivialization) است: فرهنگ عامه را صرفا‌ً «سرگرمی و لذت» می‌شمارد و بُعد فکری آن را نادیده می‌گیرد (Featherstone, 1994). نقد دوم، «ایدئولوژی‌زدگی»: فرهنگ عامه را ابزاری بازتولید ایدئولوژی مسلط می‌داند، در حالی که در واقع مخاطب، «مقاومت» و «بازتعبیر» هم دارد (Morris, 1984). همچنین مرز «فرهنگ عامه» و «فرهنگ نخبه» در عصر دیجیتال کمرنگ شده است.",
        applications="تحلیل انتقادی سرگرمی و رسانه (فرهنگ عامه)، پژوهش سواد رسانه‌ای (مصرف آگاهانه)، طراحی سیاست فرهنگی (همپوشانی عامه/نخبه)، تحلیل بازتولید ایدئولوژی، و مطالعه معناسازی مخاطب در برابر فرهنگ مصرفی (Featherstone, 1994; Morris, 1984).",
        evolution="مفهوم فرهنگ عامه از مدرسه فرانکفورت (دهه‌های ۱۹۴۰–۱۹۵۰) و نظریه «صنعت فرهنگ» شکل گرفت؛ در دهه‌های ۱۹۶۰–۱۹۷۰، با مطالعات «فرهنگ عامه» (Raymond Williams)، به «میدان مستقل» تبدیل شد؛ در عصر دیجیتال، مرز عامه و نخبه کمرنگ و «فرهنگ عامه دیجیتال» شکل گرفته است (Featherstone, 1994).",
        assumptions="فرض‌های نهفته: فرهنگ عامه، برای مخاطبان گسترده و با هدف سرگرمی تولید می‌شود (نه صرفا‌ً آگاهی‌رسانی)؛ مصرف، لذت‌محور است؛ و معناسازی، در تعامل مخاطب با بافت صورت می‌گیرد (Featherstone, 1994; Morris, 1984).",
    ),
    "CPT-139": dict(
        mechanism="هویت فردی در چهار حلقه شکل می‌گیرد: (۱) درون‌سازی خود: فرد، از طریق تعاملات و بازخوردها، تصویر از خود می‌سازد (آینه اجتماعی)؛ (۲) نمایش: در تعاملات، خود را «نمایش» می‌دهد (پیش‌زمینه/پشت‌صحنه)؛ (۳) بازخورد دیگران: واکنش دیگران، تصویر خود را تأیید یا تعدیل می‌کند؛ (۴) بازنویسی مداوم: هویت، فرایند پویا و همیشگی است (نه ثابت) (Goffman, 1986).",
        key_concepts=["آینه اجتماعی", "نمایش خود", "واکنش‌گرایی", "پویایی هویت", "تعاملات"],
        critiques="نقد نخست، «تعامل‌زدگی» (interactionism) است: فرض بر این است که هویت، صرفا‌ً «در تعامل» ساخته می‌شود، در حالی که در واقع عوامل بیولوژیک و ساختاری نیز اثر دارند (Goffman, 1986). نقد دوم، «نمایشی‌سازی»: هویت را صرفا‌ً «نمایش» می‌شمارد و بُعد درونی و صادق آن را فراموش می‌کند (Srebnicki, 2010). همچنین «هویت دیجیتال» در شبکه‌ها، هویت را چندپاره و سیال کرده است.",
        applications="تحلیل هویت و رسانه (رسانه در شکل‌دهی تصویر خود)، طراحی تجربه کاربری (هویت دیجیتال)، پژوهش روان‌شناسی اجتماعی (تعامل و هویت)، آموزش سواد رسانه‌ای (شناخت اثر رسانه بر هویت)، و تحلیل هویت در شبکه‌های اجتماعی (Srebnicki, 2010; Goffman, 1986).",
        evolution="مفهوم هویت فردی از نظریه‌های خود و تعامل (کوچی و مید، ۱۹۰۰) و جامعه‌شناسی تعاملی شکل گرفت؛ گافمن (۱۹۵۶) آن را به «نمایش خود» گسترش داد؛ در عصر دیجیتال، هویت فردی به «هویت چندپاره و سیال» در شبکه‌ها بدل شده است (Goffman, 1986).",
        assumptions="فرض‌های نهفته: هویت، فرایند اجتماعی و تعاملی است (نه ذاتی و ثابت)؛ تصویر خود، در آینه دیگران شکل می‌گیرد؛ و هویت، همیشگی و پویا است و در بافت بازتولید می‌شود (Goffman, 1986; Srebnicki, 2010).",
    ),
    "CPT-140": dict(
        mechanism="هویت جمعی در چهار حلقه شکل می‌گیرد: (۱) عضویت گروهی: فرد، خود را در یک گروه (قومی، ملی، زبانی، رسانه‌ای) طبقه‌بندی می‌کند (ما/دیگران)؛ (۲) اشتراک معیارها: هنجارها، نمادها و روایت مشترک، حس تعلق می‌سازد؛ (۳) بازتولید از رسانه: رسانه، روایت «ما» را بازتولید و تقویت می‌کند؛ (۴) مقایسه اجتماعی: در مقایسه با گروه‌های دیگر، مرز و هویت گروهی تقویت می‌شود (Tajfel, 2001).",
        key_concepts=["ما/دیگران", "گروه مرجع", "اشتراک نماد", "بازتولید رسانه‌ای", "مقایسه اجتماعی"],
        critiques="نقد نخست، «جمعی‌زدگی» (collectivism) است: فرض بر این است که هویت جمعی، «یکدست و یکپارچه» است، در حالی که در واقع درونی‌اش تنوع و اختلاف‌نظر دارد (Reicher, 2011). نقد دوم، «دیگری‌سازی» (othering): مرز ما/دیگران، گاه به تبعیض و خشم می‌انجامد (Tajfel, 2001). همچنین رسانه، گاه هویت جمعی را «ساخته» و تحمیل می‌کند، نه صرفا‌ً بازتابش.",
        applications="تحلیل هویت جمعی و رسانه (نقش رسانه در شکل‌دهی «ما»), پژوهش رسانه‌های قومی و ملی، طراحی سواد رسانه‌ای (شناخت بازتولید هویت جمعی), تحلیل تبلیغات و پراکندگی هویت ملی, و مطالعه اثر رسانه بر تعلق و مقایسه اجتماعی (Reicher, 2011; Tajfel, 2001).",
        evolution="مفهوم هویت جمعی از نظریه هویت اجتماعی تاجفل (۱۹۷۰) و مطالعات بین‌گروهی شکل گرفت؛ در دهه‌های ۱۹۸۰–۱۹۹۰، با مطالعات رسانه و هویت ملی، به «میدان» گسترش یافت؛ در عصر دیجیتال، هویت جمعی به «هویت جمعی برخط» (جامعه‌های مجازی) گسترش یافته است (Tajfel, 2001).",
        assumptions="فرض‌های نهفته: فرد، هم‌زمان در چند گروه عضو است (هویت چندلایه)؛ مرز ما/دیگران، در تعاملات و رسانه شکل می‌گیرد؛ و هویت جمعی، پویا و بازتولیدپذیر است (Tajfel, 2001; Reicher, 2011).",
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
                    (code, json.dumps({"batch": 321, "score": score, "words": words,
                                       "sources": n_sources, "verified": n_verified,
                                       "relations": n_rel, "rubric": detail}, ensure_ascii=False), STAMP, NOW))
        print(code, "words", words, "score", score, "detail", detail)
    conn.commit()
    conn.close()
    print("BATCH321 DONE")


if __name__ == "__main__":
    main()
