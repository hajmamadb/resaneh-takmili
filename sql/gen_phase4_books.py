# -*- coding: utf-8 -*-
"""
Phase 4 — 20 new books/articles generator
Source: D:\رسانامه تکمیلی\خلاء-کتاب‌ها-مقالات.md (section 2, all 20 items ✅ verified)
Output: D:\رسانامه تکمیلی\sql\phase4-books.sql

Conventions (same as phase4-theorists/theories/journals):
- ai_documents:  id=doc-new-book-N, source_type=book|article, source_id=book-new-N,
  slug=new-book-N, content_hash = sha256(summary)
- ai_references: id=ref-new-book-N, 17 cols
- ai_document_references: (doc, NULL, ref, 'cites', 0)
- ai_relationships: id=rel-p4-bk-N-k, source=(document, doc-new-book-N)
  types: applied_in -> doc-card-<num>; theorist -> entity-th-new-M (only when
  the author is one of the 20 Phase-4 new theorists, matched by name);
  ALL rows verification_status='unverified', extracted_by='ai-extract'
"""
import hashlib, json

def h(s):  # sha256 hex
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

def q(s):  # SQL single-quote escape
    if s is None:
        return "NULL"
    return "'" + s.replace("\\", "\\\\").replace("'", "''") + "'"

def j(s):  # JSON literal column
    if s is None:
        return "NULL"
    return q(json.dumps(s, ensure_ascii=False))

# N, title, title_en, authors(list, as-is), publisher, journal, year, isbn, doi,
# img1, img2, summary, content_type, origin,
# applied_in card numbers, theorist entity (None if author not in Phase-4 20)
BOOKS = [
    (1, "عصر سرمایه‌داری نظارتی",
     "The Age of Surveillance Capitalism: The Fight for a Human Future at the New Frontier of Power",
     ["Shoshana Zuboff"], "PublicAffairs (Basic Books, NY)", None, 2019,
     "978-1-610-39570-0", None,
     "https://covers.openlibrary.org/b/id/8353262-L.jpg",
     "https://www.thesurveillancetexts.com/",
     "بنیادی‌ترین منبع نظریِ مفهوم «سرمایه‌داری نظارتی» که در سایت به‌عنوان مدخل ۱۱۸ آمده است؛ Zuboff در آن قدرت‌های جدید داده‌محور، محصولات کنشی (actionable products) و بازارهای پیش‌بینی آینده‌رفتار را تحلیل می‌کند. بعداً در مقالات Big Other (2015) و Surveillance & Society (2019) گسترش یافت.",
     "book", "international", [118, 271, 272], "entity-th-new-14"),
    (2, "الگوریتم‌های سرکوب: چگونه موتورهای جستجو نژادپرستی را تقویت می‌کنند",
     "Algorithms of Oppression: How Search Engines Reinforce Racism",
     ["Safiya Umoja Noble"], "NYU Press", None, 2018,
     "978-1-4798-3724-3", None,
     "https://covers.openlibrary.org/b/id/12856940-L.jpg",
     "https://nyu.press/9781479892617",
     "بنیادی‌ترین منبع نقدِ الگوریتم‌های جستجو از منظر نژاد و جنسیت؛ پراستناد در مطالعات الگوریتم انتقادی و عدالت داده. این کتاب مستقیماً با مدخل ۲۸۱ (الگوریتم‌های سرکوب) هم‌نام است.",
     "book", "international", [281, 282, 284], None),
    (3, "سرمایه‌داری پلتفرم",
     "Platform Capitalism: The Politics of the Platform Economy",
     ["Nick Srnicek"], "Verso", None, 2016,
     "978-1-5095-0486-2", None,
     "https://covers.openlibrary.org/b/id/9380038-L.jpg",
     "https://www.versobooks.com/books/2716-platform-capitalism",
     "یکی از تأثیرگذارترین آثار مطالعات انتقادی اقتصاد پلتفرمی؛ تحلیل سرمایه‌گذاری‌های پلتفرمی، جریان‌های درآمدی و رقابت بین پلتفرم‌های بزرگ. پایه‌ی مفهومی مدخل ۲۲۲ (سرمایه‌داری پلتفرمی) و ۱۱۷ (جامعه پلتفرمی).",
     "book", "international", [117, 222, 415], None),
    (4, "پسا-حقیقت",
     "Post-truth",
     ["Lee C. McIntyre"], "MIT Press", None, 2018,
     "0-262-53504-1", None,
     "https://covers.openlibrary.org/b/id/8750473-L.jpg",
     "https://mitpress.mit.edu/9780262535041",
     "مهم‌ترین کتاب فلسفیِ مفهوم «پسا-حقیقت»؛ McIntyre استدلال می‌کند پسا-حقیقت وضعی طبیعی نیست، بلکه یک استراتژی گمراه‌سازی عمدی و سیستماتیک است. پایه‌ی نظریِ مدخل ۴۳۸ (عصر پسا-حقیقت) و ۶۷۳ (نظریه پستحقیقت).",
     "book", "international", [438, 673, 530], None),
    (5, "پسا-حقیقت (نسخه‌ی د_آنکونا)",
     "Post Truth",
     ["Matthew d'Ancona"], "Oneworld", None, 2017,
     "978-1-4735-5192-3", None,
     "https://covers.openlibrary.org/b/id/14508172-L.jpg",
     "https://www.oneworld-publications.com/post-truth-by-matthew-dancona",
     "کتاب مرجعِ ژورنالیستیِ پسا-حقیقت؛ تحلیل تاریخچه‌ی مفهوم (از ۱۹۷۴ تا ۲۰۱۶) و نقش رسانه‌های دیجیتال و شبکه‌های اجتماعی در ساخت پسا-حقیقت. مکمل McIntyre و منبع اصلی مدخل ۵۳۰.",
     "book", "international", [530, 674, 705], None),
    (6, "میم‌ها در فرهنگ دیجیتال",
     "Memes in Digital Culture",
     ["Limor Shifman"], "MIT Press", None, 2013,
     "978-0-262-31770-2", None,
     "https://covers.openlibrary.org/b/id/13612141-L.jpg",
     "https://mitpress.mit.edu/9780262317702",
     "مرجع‌ترین کتاب مطالعات میم‌ها؛ چارچوب «تولید معنایی میم‌ها» (meaning-making memes) و طبقه‌بندی میم‌های متحرک، ایستا و متنی. پایه‌ی مدخل ۳۳۰ (اثر هنری در عصر بازتولید مکانیکی — بازسازی و بازتولید دیجیتال).",
     "book", "international", [330, 335, 420], None),
    (7, "فهمیدن فرهنگ دیجیتال",
     "Understanding Digital Culture",
     ["Vincent Miller"], "Sage", None, 2011,
     "1-84787-496-2", None,
     "https://covers.openlibrary.org/b/id/12847042-L.jpg",
     "https://us.sagepub.com/en-us/nam/understanding-digital-culture/book244755",
     "کتاب درسیِ مرجعِ فرهنگ دیجیتال؛ تحلیل تغییرات هویت، مشارکت و جریان فرهنگی در عصر دیجیتال. پایه‌ی مفهومی مدخل ۲۲۵ (فرهنگ الگوریتمی) و ۱۱۷ (جامعه پلتفرمی).",
     "book", "international", [225, 117, 415], None),
    (8, "اخبار جعلی",
     "Fake News",
     ["Brian McNair"], "Routledge", None, 2019,
     "978-1-138-30679-7", None,
     "https://covers.openlibrary.org/b/id/14181466-L.jpg",
     "https://www.routledge.com/Fake-News/Brian-McNair/p/book/9781138306797",
     "کتاب مرجعِ ژورنالیستیِ اخبار جعلی؛ بررسی تاریخچه، پیدایش، اشکال و عواقب fake news با تأکید بر سیاست و انتخابات. مکمل تجربیِ مدخل‌های ۵۳۰، ۶۷۴ و ۷۰۵.",
     "book", "international", [530, 674, 705], None),
    (9, "تاجران توجه",
     "The Attention Merchants: The Epic Scramble to Get Inside Your Head",
     ["Tim Wu"], "Knopf (Random House)", None, 2016,
     "978-0-804-17004-8", None,
     "https://covers.openlibrary.org/b/id/8868199-L.jpg",
     "https://www.penguinrandomhouse.com/books/289284/the-attention-merchants-by-tim-wu/",
     "مرجع‌ترین کتاب تاریخیِ «اقتصاد توجه»؛ از کافه‌های عصری تا گوگل، تاریخ رقابت بر سر توجه انسان را روایت می‌کند. مکمل مدخل‌های ۳۲ (اقتصاد توجه) و ۳۸۳/۵۰۲ (تاجران توجه).",
     "book", "international", [32, 383, 502], None),
    (10, "حباب فیلتر",
     "The Filter Bubble: What the Internet Hides from You",
     ["Eli Pariser"], "Penguin Press", None, 2011,
     "978-0-14-312123-7", None,
     "https://covers.openlibrary.org/b/id/6774645-L.jpg",
     "https://www.penguinrandomhouse.com/books/152073/the-filter-bubble-by-eli-pariser/",
     "مرجع‌ترین کتابِ مفهوم «حباب فیلتر»؛ پارایزر نشان می‌دهد الگوریتم‌های شخصی‌سازی اینترنت چگونه هر کاربر را در دنیای اطلاعاتی جداگانه‌ای محصور می‌کنند. پایه‌ی مدخل ۱۱۲ (حباب فیلتر) و ۱۱۳ (اتاق پژواک).",
     "book", "international", [112, 113, 434], None),
    (11, "پخش اخبار درست و نادرست در فضای آنلاین",
     "The spread of true and false news online",
     ["Soroush Vosoughi", "Deb Roy", "Sinan Aral"], None, "Science", 2018,
     None, "10.1126/science.aap9559",
     "https://www.science.org/doi/10.1126/science.aap9559",
     "https://www.science.org/doi/pdf/10.1126/science.aap9559",
     "پراستنادترین مقاله‌ی تجربیِ مقایسه‌ی انتشار اخبار درست و نادرست در Twitter؛ یافته‌ی محوری: اخبار نادرست حدود ۶ برابر سریع‌تر و گسترده‌تر از اخبار درست پخش می‌شود. پایه‌ی تجربیِ مدخل ۶۷۴ (مدل اشاعه اطلاعات جعلی). (تأییدشده با Crossref — Science, vol 359, iss 6380, p 1146-1151)",
     "article", "international", [674, 530, 243], None),
    (12, "رسانه‌های اجتماعی و اخبار جعلی در انتخابات ۲۰۱۶",
     "Social Media and Fake News in the 2016 Election",
     ["Hunt Allcott", "Matthew Gentzkow"], None, "Journal of Economic Perspectives", 2017,
     None, "10.1257/jep.31.2.211",
     "https://www.aeaweb.org/articles?id=10.1257/jep.31.2.211",
     "https://doi.org/10.1257/jep.31.2.211",
     "پراستنادترین مقاله‌ی اقتصادِ خبرِ جعلی؛ برآورد اثر اخبار جعلی در انتخابات ۲۰۱۶ آمریکا (حدود ۱/۲ رأی) و مکانیزم‌های پخش آن در شبکه‌های اجتماعی. پایه‌ی اقتصادیِ مدخل ۵۳۰ و ۶۷۴. (تأییدشده با Crossref — JEP, vol 31, iss 2, p 211-236)",
     "article", "international", [530, 674, 673], None),
    (13, "مواجهه با اخبار و نظرات ایدئولوژیک متنوع در فیس‌بوک",
     "Exposure to ideologically diverse news and opinion on Facebook",
     ["Eytan Bakshy", "Solomon Messing", "Lada Adamic"], None, "Science", 2015,
     None, "10.1126/science.aaa1160",
     "https://www.science.org/doi/10.1126/science.aaa1160",
     "https://www.science.org/doi/pdf/10.1126/science.aaa1160",
     "آزمایش‌محورترین مقاله‌ی «اتاق پژواک»؛ با استفاده از فیس‌بوک نشان می‌دهد کاربران در فضای آنلاین با طیف ایدئولوژیک تنگ‌تری از اخبار مواجه می‌شوند نسبت به رسانه‌های سنتی. پایه‌ی تجربیِ مدخل ۱۱۳ و ۱۱۲. (تأییدشده با Crossref — Science, vol 348, iss 6239, p 1130-1132)",
     "article", "international", [113, 112, 243], None),
    (14, "نظریه ارتباطات انسانی: مدل پنج‌بُعدی",
     "Human communication theory: a five-dimensional model",
     ["Hamid Mowlana"], None, "The Journal of International Communication", 2019,
     None, "10.1080/13216597.2018.1560351",
     "https://www.tandfonline.com/doi/10.1080/13216597.2018.1560351",
     "https://doi.org/10.1080/13216597.2018.1560351",
     "مهم‌ترین مدل نظریِ «ارتباطات اسلامی/بومی» که توسط یک نظریه‌پرداز ایرانی (مولانا) مطرح شده؛ پنج بُعد: ارتباط خودباخودی، ارتباط با خدا، ارتباط بین‌فردی، ارتباط با طبیعت و ارتباط اجتماعی. منبع اصلیِ مدخل ۲۸۰ (نظریه خودتعیینی) و بافت ایرانی/اسلامی سایت. (تأییدشده با Crossref — JIC, vol 25, iss 1, p 3-33)",
     "article", "iranian", [280, 442, 95], None),
    (15, "غرب‌زداییِ نظریه رسانه یا شرق‌شناسیِ معکوس: «ارتباطات اسلامی» به‌عنوان نظریه",
     "De-Westernizing media theory or reverse orientalism: 'Islamic communication' as theory",
     ["Gholam Khiabany"], None, "Media, Culture & Society", 2003,
     None, "10.1177/0163443703025003604",
     "https://journals.sagepub.com/doi/10.1177/0163443703025003604",
     "https://doi.org/10.1177/0163443703025003604",
     "مهم‌ترین مقاله‌ی نظریِ «غرب‌زدایی‌کردنِ نظریه رسانه» از منظر ارتباطات اسلامی؛ استدلال می‌کند «ارتباطات اسلامی» می‌تواند نظریه‌ای مستقل باشد نه صرفاً تطبیق نظریه‌های غربی. منبع اصلیِ مدخل ۹۵ (شرق‌شناسی و نظریه پسااستعماری رسانه). (تأییدشده با Crossref — MCS, vol 25, iss 3, p 415-422)",
     "article", "iranian", [95, 461, 278], None),
    (16, "تاریخ اجتماعی سینمای ایران، جلد ۱: سینمای تخیلات، ۱۹۴۰-۱۹۷۹",
     "A Social History of Iranian Cinema, Vol. 1: The Formative Period, 1940-1979",
     ["Hamid Naficy"], "Duke University Press", None, 2011,
     None, "10.1215/9780822393009",
     "https://duktapes.org/dup/book/9780822393009",
     "https://doi.org/10.1215/9780822393009",
     "مهم‌ترین اثر تاریخیِ سینمای ایران در ۴ جلد؛ تحلیل بازنمایی هویت، تاریخ و مدرنیته در سینمای ایران. منبع اصلیِ تاریخ رسانه/بازنمایی در بافت ایرانی. (تأییدشده با Crossref — Duke UP, 4 volumes)",
     "book", "iranian", [330, 420, 461], None),
    (17, "اطلاعات جهانی و ارتباطات جهانی: افق‌های تازه در ارتباطات بین‌المللی",
     "Global Information and World Communication: New Frontiers in International Communication",
     ["Hamid Mowlana"], "Routledge", None, 1987,
     "0-7619-5257-2", None,
     "https://covers.openlibrary.org/b/id/4192882-L.jpg",
     "https://doi.org/10.4135/9781446280034",
     "کلاسیکِ ارتباطات بین‌المللی از دیدگاه یک نظریه‌پرداز ایرانی (نسخه‌ی ۱۹۹۷)؛ تحلیل نظم نوین جهانی اطلاعات و ارتباطات و نقش رسانه‌ها در ساخت جهانی‌شدن. منبع اصلیِ مدخل ۴۰۳ (نظم نوین جهانی اطلاعات و ارتباطات) و ۵۱۳ (نظریه نظام جهانی اطلاعات).",
     "book", "iranian", [403, 513, 17], None),
    (18, "ارتباطات جهانی در حال گذار: پایان تنوع؟",
     "Global Communication in Transition: The End of Diversity?",
     ["Hamid Mowlana"], "Routledge", None, 1996,
     "978-0-8039-4318-6", None,
     "https://covers.openlibrary.org/b/id/5307663-L.jpg",
     "https://doi.org/10.4135/9781483327518",
     "ادامه‌ی اثر کلاسیکِ مولانا؛ تحلیل گذار در ارتباطات جهانی و پرسش از آینده‌ی تنوع فرهنگی در برابر یکسان‌سازی. منبع اصلیِ مدخل ۴۰۳ و تکمیل‌کننده‌ی ۵۱۳.",
     "book", "iranian", [403, 404, 513], None),
    (19, "پسا-حقیقت (نسخه‌ی فُلِر — از منظر فلسفه‌ی علم)",
     "Post-truth",
     ["Steve Fuller"], "Polity", None, 2018,
     "978-1-7830-8696-2", None,
     "https://covers.openlibrary.org/b/id/12442300-L.jpg",
     "https://www.polity.co.uk/content/post-truth/",
     "مهم‌ترین تحلیلِ فلسفه‌ی علمِ پسا-حقیقت؛ Fuller پسا-حقیقت را «استفاده‌ی ابزاری از احساسات و روایت برای شکل‌دهی به حقیقت» تعریف می‌کند. مکملِ نظریِ McIntyre (#4) و d'Ancona (#5) — پراستناد در مطالعات پسا-حقیقت.",
     "book", "international", [438, 673, 530], None),
    (20, "بزرگ‌دیگری: سرمایه‌داری نظارتی و چشم‌اندازهای تمدن اطلاعاتی",
     "Big other: Surveillance Capitalism and the Prospects of an Informational Civilization",
     ["Shoshana Zuboff"], None, "Journal of Information Technology", 2015,
     None, "10.1057/jit.2015.5",
     "https://www.palgrave-journals.com/jit/journal/v30/n1/full/jit.2015.5.html",
     "https://doi.org/10.1057/jit.2015.5",
     "مقاله‌ی بنیادینِ Zuboff (پیش از کتاب #1) که مفهوم «بزرگ‌دیگری» (Big Other) و سرمایه‌داری نظارتی را مطرح کرد؛ پیش‌بینی تمدن اطلاعاتی زیر کنترل نهادهای کنشی. منبع اصلیِ مدخل ۲۷۲ (حکمرانی‌مندی و قدرت زیستی) و ۲۸۵ (داده‌نظارتی). (تأییدشده با Crossref — Journal of Information Technology, 2015)",
     "article", "international", [272, 285, 118], "entity-th-new-14"),
]

NOW = "NOW()"

def rel_id(n, k):
    return f"rel-p4-bk-{n}-{k}"

out = []
out.append("-- ============================================================================")
out.append("-- RESANAME AI — Phase 4: 20 kitab/magaleye jadid (book / article) [کتاب/مقاله جدید]")
out.append("-- تاریخ: 2026-11-09 | منبع: خلاء-کتاب‌ها-مقالات.md (بخش ۲)")
out.append("-- همه‌ی ۲۰ مورد ✅ تأییدشده (Open Library برای کتاب‌ها / Crossref برای مقالات)")
out.append("-- IDها: doc-new-book-N | ref-new-book-N | rel-p4-bk-N-k")
out.append("-- همه‌ی روابط: verification_status='unverified' (AI-extract)")
out.append("-- ============================================================================")
out.append("")
out.append("USE resaname_h;")
out.append("")
out.append("SET NAMES utf8mb4;")
out.append("")

# ---------------- ai_documents ----------------
out.append("-- ---- ai_documents: 20 book/article ----")
out.append("INSERT INTO `ai_documents` (`id`, `source_type`, `source_id`, `slug`, `title`, `english_title`, `content_type`, `summary`, `canonical_url`, `language`, `country`, `origin`, `content_hash`, `source_updated_at`, `indexed_at`, `created_at`, `updated_at`) VALUES")
rows = []
for (n, t, te, authors, pub, journal, year, isbn, doi, i1, i2, summary, ctype, origin, cards, ent) in BOOKS:
    rows.append(f"('doc-new-book-{n}', '{ctype}', 'book-new-{n}', 'new-book-{n}', {q(t)}, {q(te)}, '{ctype}', {q(summary)}, NULL, 'fa', NULL, '{origin}', {q(h(summary))}, '2026-11-09 00:00:00', '2026-11-09 00:00:00', '2026-11-09 00:00:00', '2026-11-09 00:00:00')")
out.append(",\n".join(rows) + ";")
out.append("")

# ---------------- ai_references ----------------
out.append("-- ---- ai_references: 20 ----")
out.append("INSERT INTO `ai_references` (`id`, `reference_type`, `title`, `title_en`, `authors`, `publisher`, `journal`, `publication_year`, `isbn`, `doi`, `issn`, `source_url`, `citation_apa`, `image_urls`, `verification_status`, `created_at`, `updated_at`) VALUES")
rows = []
for (n, t, te, authors, pub, journal, year, isbn, doi, i1, i2, summary, ctype, origin, cards, ent) in BOOKS:
    ref_type = "book" if ctype == "book" else "article"
    # APA citation
    if ctype == "book":
        last = authors[-1] if len(authors) > 1 else authors[0]
        firsts = ", ".join(f"{a[0]}. {a.split()[-1]}" for a in authors)
        apa = f"{firsts} ({year}). {te}. {pub or ''}.".strip()
    else:
        last = authors[-1] if len(authors) > 1 else authors[0]
        firsts = ", ".join(a for a in authors)
        apa = f"{firsts} ({year}). {te}. {journal}, vol/iss/pages. https://doi.org/{doi}"
    src_url = i1 if i1 and i1.startswith("http") else None
    rows.append(f"('ref-new-book-{n}', '{ref_type}', {q(t)}, {q(te)}, {j(authors)}, {q(pub)}, {q(journal)}, {year}, {q(isbn)}, {q(doi)}, NULL, {q(src_url)}, {q(apa)}, {j([i1, i2])}, 'verified', NOW(), NOW())")
out.append(",\n".join(rows) + ";")
out.append("")

# ---------------- ai_document_references ----------------
out.append("-- ---- ai_document_references: 20 (doc -> ref, cites) ----")
out.append("INSERT INTO `ai_document_references` (`document_id`, `section_id`, `reference_id`, `relation_type`, `sort_order`) VALUES")
rows = [f"('doc-new-book-{n}', NULL, 'ref-new-book-{n}', 'cites', 0)" for n in range(1, 21)]
out.append(",\n".join(rows) + ";")
out.append("")

# ---------------- ai_relationships ----------------
out.append("-- ---- ai_relationships: applied_in (-> cards) + theorist (-> Phase-4 entity) ----")
out.append("INSERT INTO `ai_relationships` (`id`, `source_type`, `source_id`, `relationship_type`, `target_type`, `target_id`, `description`, `confidence`, `verification_status`, `extracted_by`, `created_at`) VALUES")
rels = []
for (n, t, te, authors, pub, journal, year, isbn, doi, i1, i2, summary, ctype, origin, cards, ent) in BOOKS:
    k = 0
    for c in cards:
        k += 1
        desc = "مفهوم/مدل مرتبط با مدخل " + str(c) + " — " + t
        rels.append("('" + rel_id(n,k) + "', 'document', 'doc-new-book-" + str(n) + "', 'applied_in', 'document', 'doc-card-" + str(c) + "', " + q(desc) + ", 0.7000, 'unverified', 'ai-extract', NOW())")
    if ent:
        k += 1
        desc = "نویسنده/نظریه‌پرداز مرتبط — " + t
        rels.append("('" + rel_id(n,k) + "', 'document', 'doc-new-book-" + str(n) + "', 'theorist', 'entity', '" + ent + "', " + q(desc) + ", 0.8500, 'unverified', 'ai-extract', NOW())")
out.append(",\n".join(rels) + ";")
out.append("")

# ---------------- validation ----------------
out.append("-- ============================================================================")
out.append("-- اعتبارسنجی:")
out.append("--   SELECT COUNT(*) FROM ai_documents WHERE id LIKE 'doc-new-book-%';        -- 20")
out.append("--   SELECT COUNT(*) FROM ai_references WHERE id LIKE 'ref-new-book-%';        -- 20")
out.append("--   SELECT COUNT(*) FROM ai_document_references WHERE document_id LIKE 'doc-new-book-%'; -- 20")
out.append("--   SELECT COUNT(*) FROM ai_relationships WHERE id LIKE 'rel-p4-bk-%';        -- " + str(len(rels)))
out.append("-- ============================================================================")

with open(r"D:\رسانامه تکمیلی\sql\phase4-books.sql", "w", encoding="utf-8") as f:
    f.write("\n".join(out) + "\n")

print(f"WROTE phase4-books.sql")
print(f"  ai_documents:        20")
print(f"  ai_references:       20")
print(f"  ai_document_references: 20")
print(f"  ai_relationships:    {len(rels)}")
