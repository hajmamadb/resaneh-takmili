# -*- coding: utf-8 -*-
"""Merge the 4 phase4 partial seeds into seed-phase4-70-items.sql (dependency-safe order)."""
import re

FILES = [
    'phase4-theorists.sql',
    'phase4-theories.sql',
    'phase4-books.sql',
    'phase4-journals.sql',
]

def load_body(fname):
    """Return only the data-bearing lines: drop the file's own header comment block,
    its USE resaname_h; and its SET FOREIGN_KEY_CHECKS lines (we add our own once)."""
    lines = []
    in_header = True
    for ln in open(fname, encoding='utf-8'):
        raw = ln.rstrip('\n')
        stripped = raw.strip()
        # stop header mode once we hit the first INSERT or a non-header, non-empty line that isn't a leading comment we already skipped
        if in_header:
            if stripped == '' :
                continue
            if stripped.startswith('--'):
                lines.append(raw)
                continue
            # first non-comment non-empty line
            if stripped == 'USE resaname_h;':
                in_header = False
                continue
            if stripped.startswith('SET NAMES'):
                in_header = False
                continue
            if stripped.startswith('SET FOREIGN_KEY_CHECKS'):
                in_header = False
                continue
            in_header = False
            lines.append(raw)
        else:
            # In body: still strip any stray USE / SET NAMES / SET FOREIGN_KEY_CHECKS (defensive)
            if stripped == 'USE resaname_h;':
                continue
            if stripped.startswith('SET NAMES'):
                continue
            if stripped.startswith('SET FOREIGN_KEY_CHECKS'):
                continue
            lines.append(raw)
    return '\n'.join(lines).strip('\n')

out = []
out.append('-- ============================================================================')
out.append('-- RESANAME AI — Seed فاز ۴: ۷۰ مدخل جدید (Phase 4) | تاریخ: 2026-11-09')
out.append('-- ترکیب ۴ فایل جزئی در یک ترتیب وابستگی‌محور:')
out.append('--   ۱) ai_documents        (۲۰ نظریه‌پرداز + ۱۵ نظریه + ۲۰ کتاب/مقاله + ۱۵ مجله = ۷۰)')
out.append('--   ۲) ai_document_sections(بخش‌بندی نظریه‌ها)')
out.append('--   ۳) ai_entities         (۲۰ موجودیت نظریه‌پرداز + ۱۵ موجودیت مجله)')
out.append('--   ۴) ai_references       (۲۰ منبع کتاب/مقاله + ۱۵ منبع مجله)')
out.append('--   ۵) ai_document_references (اتصال کتاب‌ها/مجلات به منابع)')
out.append('--   ۶) ai_relationships    (شبکه‌ی روابط دانش)')
out.append('-- موتور: InnoDB | کاراکتری: utf8mb4 | Collation: utf8mb4_unicode_ci')
out.append('-- همه‌ی روابطِ استنباط‌شده: verification_status=\'unverified\', extracted_by=\'ai-extract\'')
out.append('-- ============================================================================')
out.append('')
out.append('USE resaname_h;')
out.append('')
out.append('SET NAMES utf8mb4;')
out.append('SET FOREIGN_KEY_CHECKS = 0;')
out.append('')

order_note = []
for fname in FILES:
    body = load_body(fname)
    out.append('')
    out.append('-- ----------------------------------------------------------------------------')
    out.append('-- ▼▼▼ از فایل: %s ▼▼▼' % fname)
    out.append('-- ----------------------------------------------------------------------------')
    out.append(body)
    out.append('')

# final wrap
out.append('-- ----------------------------------------------------------------------------')
out.append('-- ▼▼▼ پایان داده‌ها ▼▼▼')
out.append('-- ----------------------------------------------------------------------------')
out.append('SET FOREIGN_KEY_CHECKS = 1;')
out.append('')
out.append('-- ============================================================================')
out.append('-- اعتبارسنجی نهایی (پس از اجرا باید ۷۰ باشد):')
out.append('--   SELECT COUNT(*) AS total_new_documents FROM ai_documents')
out.append("--     WHERE id LIKE 'doc-new-theorist-%'")
out.append("--        OR id LIKE 'doc-new-theory-%'")
out.append("--        OR id LIKE 'doc-new-book-%'")
out.append("--        OR id LIKE 'doc-new-journal-%';   -- expect: 70")
out.append('-- تفکیک:')
out.append("--   SELECT source_type, COUNT(*) FROM ai_documents WHERE id LIKE 'doc-new-%' GROUP BY source_type;")
out.append('--   -- expect: theorist=20, theory=15, book/article=20, journal=15')
out.append('-- ============================================================================')
out.append('')

merged = '\n'.join(out)
with open('seed-phase4-70-items.sql', 'w', encoding='utf-8', newline='') as f:
    f.write(merged)

# ---- post-merge verification ----
src = open('seed-phase4-70-items.sql', encoding='utf-8').read()
print('merged bytes:', len(src.encode('utf-8')))
print('USE resaname_h count :', src.count('USE resaname_h;'))
print('SET NAMES count      :', src.count('SET NAMES utf8mb4;'))
print('FK off / on          :', src.count('SET FOREIGN_KEY_CHECKS = 0;'), '/', src.count('SET FOREIGN_KEY_CHECKS = 1;'))
print('stray ");,"          :', src.count(');,'))

import collections

def count_value_tuples(block):
    """Count top-level ( ... ) tuples in a VALUES block, respecting quoted strings."""
    depth = 0; cnt = 0; in_str = False; esc = False; i = 0
    n = len(block)
    while i < n:
        c = block[i]
        if in_str:
            if esc: esc = False
            elif c == chr(92): esc = True
            elif c == "'": in_str = False
            i += 1; continue
        if c == "'": in_str = True; i += 1; continue
        if c == '(':
            depth += 1
            if depth == 1: cnt += 1
            i += 1; continue
        if c == ')':
            depth -= 1
            i += 1; continue
        i += 1
    return cnt

# For each table, grab the union of all its VALUES blocks and count tuples
for table in ['ai_documents','ai_document_sections','ai_entities',
              'ai_references','ai_document_references','ai_relationships']:
    total = 0
    for m in re.finditer(r"INSERT INTO `%s`[^V]*VALUES\s*(.*?);\s*" % table, src, re.S):
        total += count_value_tuples(m.group(1))
    print('rows in %-24s : %d' % (table, total))

# expected
exp = {'ai_documents':70,'ai_document_sections':15,'ai_entities':35,
       'ai_references':35,'ai_document_references':35,'ai_relationships':206}
print('expected               :', exp)
print('relationships total = 87(theorists)+45(theories)+62(books)+59(journals) =', 87+45+62+59)
print('document_references total = 20(books)+15(journals) =', 20+15)
