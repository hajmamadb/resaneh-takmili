# -*- coding: utf-8 -*-
"""
W1 — populate works_authors for the 42 rows in `works` (resaname_v2).

Author extraction per work_type:
  book    -> author from `contents`/`sections` (short_intro / references)
  journal -> editor (سردبیر) if found, else publisher institution as editor
  article -> author(s) from short_intro / references (APA citation)

person_id resolution:
  1) if the author matches a `theorist` in `contents` (by English or Persian
     name), use that contents.id
  2) otherwise use 'person-' + stable slug of the English name
     (or of the Persian name when no English form is available)

Only writes to works_authors. Idempotent (INSERT ... ON DUPLICATE KEY UPDATE).
"""
import io
import re
import sys
import unicodedata
import pymysql

DB = dict(host='127.0.0.1', user='root', password='433700',
          database='resaname_v2', charset='utf8mb4')


# --------------------------------------------------------------------------
# name helpers
# --------------------------------------------------------------------------
def norm(s: str) -> str:
    """Normalize unicode (NFC), strip ZWNJ/zero-width and diacritics-light."""
    if s is None:
        return ''
    s = unicodedata.normalize('NFC', s)
    s = s.replace('\u200c', '').replace('\u200d', '').replace('\u200b', '')
    return s.strip()


def slugify(s: str) -> str:
    """Stable ascii slug for a name (English names are the canonical form)."""
    s = norm(s)
    s = s.lower()
    s = re.sub(r'[^a-z0-9]+', '-', s)
    s = re.sub(r'-+', '-', s).strip('-')
    return s


# --------------------------------------------------------------------------
# hand-mapped author tables (from the 42 works' short_intro + references)
# --------------------------------------------------------------------------
# Each entry: work_id -> list of (name_fa, name_en, role)
# role: 'author' for books/articles, 'editor' for journals.
WORK_AUTHORS = {
    'book-new-1':  [('شوشانا زابوف', 'Shoshana Zuboff', 'author')],
    'book-new-2':  [('سایفیا اومویا نوبل', 'Safiya Umoja Noble', 'author')],
    'book-new-3':  [('نیک اسرنیک', 'Nick Srnicek', 'author')],
    'book-new-4':  [('لی مکینتایر', 'Lee McIntyre', 'author')],
    'book-new-5':  [('متیو د آنکونا', "Matthew d'Ancona", 'author')],
    'book-new-6':  [('لیمور شیفمن', 'Limor Shifman', 'author')],
    'book-new-7':  [('وینسنت میلر', 'Vincent Miller', 'author')],
    'book-new-8':  [('برایان مک‌نیر', 'Brian McNair', 'author')],
    'book-new-9':  [('تیم وو', 'Tim Wu', 'author')],
    'book-new-10': [('الی پاریسر', 'Eli Pariser', 'author')],
    'book-new-11': [('سوروش وضحی', 'Soroush Vosoughi', 'author'),
                    ('دب روی', 'Deb Roy', 'author'),
                    ('سینان ارال', 'Sinan Aral', 'author')],
    'book-new-12': [('هانت آلتکات', 'Hunt Allcott', 'author'),
                    ('متیو گنتسکاو', 'Matthew Gentzkow', 'author')],
    'book-new-13': [('ایتان باخشای', 'Eytan Bakshy', 'author'),
                    ('سلیمان مسینگ', 'Solomon Messing', 'author'),
                    ('لادا آدامیک', 'Lada Adamic', 'author')],
    'book-new-14': [('حمید مولانا', 'Hamid Mowlana', 'author')],
    'book-new-15': [('غلام خیابانی', 'Gholam-Reza Khiabany', 'author')],
    'book-new-16': [('حامد نافیسی', 'Hamid Naficy', 'author')],
    'book-new-17': [('حمید مولانا', 'Hamid Mowlana', 'author')],
    'book-new-18': [('حمید مولانا', 'Hamid Mowlana', 'author')],
    'book-new-19': [('استیو فولر', 'Steve Fuller', 'author')],
    'book-new-20': [('شوشانا زابوف', 'Shoshana Zuboff', 'author')],
    'book-new-21': [],  # no author in source text
    'book-new-22': [],  # no author in source text
    'journal-new-1':  [('SAGE Publications', 'SAGE Publications', 'editor')],
    'journal-new-2':  [('SAGE Publications', 'SAGE Publications', 'editor')],
    'journal-new-3':  [('SAGE Publications', 'SAGE Publications', 'editor')],
    'journal-new-4':  [],  # publisher unspecified in source
    'journal-new-5':  [('Taylor & Francis', 'Taylor & Francis', 'editor')],
    'journal-new-6':  [('Taylor & Francis', 'Taylor & Francis', 'editor')],
    'journal-new-7':  [('USC Annenberg Press', 'USC Annenberg Press', 'editor')],
    'journal-new-8':  [('پژوهشگاه علوم انسانی و مطالعات فرهنگی',
                       'IHCHE', 'editor')],
    'journal-new-9':  [('پژوهشگاه فرهنگ، هنر و ارتباطات',
                       'RICC', 'editor')],
    'journal-new-10': [],  # publisher unspecified (احتمالا دانشگاه تهران، unverified)
    'journal-new-11': [('پژوهشگاه فرهنگ، هنر و ارتباطات',
                       'RICC', 'editor')],
    'journal-new-12': [('انجمن فرهنگی رسانه ایران',
                       'Iranian Media Culture Association', 'editor')],
    'journal-new-13': [('Taylor & Francis', 'Taylor & Francis', 'editor')],
    'journal-new-14': [('Cambridge University Press', 'Cambridge University Press', 'editor'),
                       ('انجمن مطالعات خاورمیانه (MESA)',
                       'Middle East Studies Association', 'editor')],
    'journal-new-15': [('مؤسسه خاورمیانه', 'Middle East Institute', 'editor')],
    'journal-new-16': [('پژوهشگاه فرهنگ و ارتباطات', 'RICC', 'editor')],
    'journal-new-17': [('پژوهشگاه فرهنگ و ارتباطات', 'RICC', 'editor')],
    'journal-new-18': [('دانشگاه تهران', 'University of Tehran', 'editor')],
    'journal-new-19': [('پژوهشگاه هنرهای تجسمی',
                       'Research Institute of Fine Arts', 'editor')],
    'journal-new-20': [('دانشگاه تهران', 'University of Tehran', 'editor')],
}


# --------------------------------------------------------------------------
# theorist name matching
# --------------------------------------------------------------------------
def load_theorist_index(cur):
    """Return {slug_of_english: contents.id} and list of (id, fa, en)."""
    cur.execute("""SELECT id, title, english_title FROM contents
                   WHERE content_type='theorist'""")
    rows = cur.fetchall()
    by_slug = {}
    for cid, fa, en in rows:
        en_n = norm(en or '')
        fa_n = norm(fa or '')
        if en_n:
            by_slug[slugify(en_n)] = (cid, fa_n, en_n)
        if fa_n:
            by_slug.setdefault('__fa__' + fa_n.lower(), (cid, fa_n, en_n))
    return rows, by_slug


def resolve_person(name_fa, name_en, theorist_rows, by_slug):
    """Return person_id for (name_fa, name_en). Prefer theorist contents.id."""
    en_n = norm(name_en or '')
    fa_n = norm(name_fa or '')
    # 1) exact English match against theorist
    if en_n:
        hit = by_slug.get(slugify(en_n))
        if hit:
            return hit[0], 'theorist'
    # 2) surname-level match: compare last two tokens of each theorist's English name
    if en_n:
        en_tokens = [t for t in re.split(r'[\s\-]+', en_n.lower()) if t]
        if en_tokens:
            tail = ' '.join(en_tokens[-2:])
            for cid, fa, en in theorist_rows:
                en2 = norm(en or '').lower()
                toks = [t for t in re.split(r'[\s\-]+', en2) if t]
                if toks and ' '.join(toks[-2:]) == tail and len(en_tokens) >= 1:
                    # require first token or a distinctive token to also match
                    if en_tokens[0] in toks:
                        return cid, 'theorist'
    # 3) Persian name match
    if fa_n:
        hit = by_slug.get('__fa__' + fa_n.lower())
        if hit:
            return hit[0], 'theorist'
    # 4) fallback: stable slug person id
    base = en_n if en_n else fa_n
    pid = 'person-' + slugify(base)
    return pid, 'new-person'


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------
def main():
    c = pymysql.connect(**DB)
    cur = c.cursor()

    # sanity: 42 works
    cur.execute("SELECT COUNT(*) FROM works")
    n_works = cur.fetchone()[0]
    print(f'works count = {n_works}')

    cur.execute("SELECT id FROM works")
    work_ids = [r[0] for r in cur.fetchall()]
    assert n_works == 42, f'expected 42 works, got {n_works}'

    # every work must be in our map
    missing = [w for w in work_ids if w not in WORK_AUTHORS]
    if missing:
        print('WARNING: works not in WORK_AUTHORS map:', missing)
        for w in missing:
            WORK_AUTHORS[w] = []

    theorist_rows, by_slug = load_theorist_index(cur)
    print(f'theorist contents: {len(theorist_rows)}')

    rows = []          # (work_id, person_id, role, sort_order)
    report = []        # per-work human-readable
    for work_id in sorted(work_ids):
        entries = WORK_AUTHORS.get(work_id, [])
        if not entries:
            report.append((work_id, 'NO-AUTHOR', '-'))
            continue
        for i, (fa, en, role) in enumerate(entries, start=1):
            person_id, how = resolve_person(fa, en, theorist_rows, by_slug)
            if len(person_id) > 40:
                raise ValueError(
                    f'person_id too long ({len(person_id)}) for '
                    f'{work_id} / {fa!r} / {en!r} -> {person_id!r}')
            rows.append((work_id, person_id, role, i))
            report.append((work_id, f'{fa} / {en} -> {person_id}', how))

    # idempotent upsert
    sql = ("INSERT INTO works_authors (work_id, person_id, role, sort_order) "
           "VALUES (%s, %s, %s, %s) "
           "ON DUPLICATE KEY UPDATE sort_order = VALUES(sort_order)")
    cur.executemany(sql, rows)
    c.commit()

    cur.execute("SELECT COUNT(*) FROM works_authors")
    total = cur.fetchone()[0]
    cur.execute("SELECT COUNT(DISTINCT work_id) FROM works_authors")
    distinct = cur.fetchone()[0]

    # verify no work left without author
    cur.execute("""SELECT w.id FROM works w
                   WHERE w.id NOT IN (SELECT work_id FROM works_authors)""")
    orphans = [r[0] for r in cur.fetchall()]

    print('\n=== per-work report ===')
    for w, name, how in report:
        print(f'{w:20s} {name:70s} [{how}]')
    print(f'\ntotal rows inserted/upserted : {len(rows)}')
    print(f'works_authors row count        : {total}')
    print(f'works with >=1 author          : {distinct}')
    print(f'works still without author     : {len(orphans)}')
    for o in orphans:
        print('  -', o)

    # breakdown
    cur.execute("""SELECT COUNT(*) FROM works_authors WHERE person_id LIKE 'person-%'""")
    print(f'\nperson- ids (new)            : {cur.fetchone()[0]}')
    cur.execute("""SELECT COUNT(*) FROM works_authors WHERE person_id NOT LIKE 'person-%'""")
    print(f'theorist contents ids          : {cur.fetchone()[0]}')
    cur.execute("""SELECT role, COUNT(*) FROM works_authors GROUP BY role""")
    print('by role:', cur.fetchall())

    c.close()


if __name__ == '__main__':
    main()
