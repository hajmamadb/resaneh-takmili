# -*- coding: utf-8 -*-
"""فاز B-5a: اصلاح link_type در entity_content_links
قاعده:
  اگر content_type = 'theorist'  -> هیچ theoricist مقاله‌ای same_as
    یک theory/model/framework نیست؛ لینک باید 'primary' باشد
    (مقاله درباره‌ی آن دانشمند است، نه درباره‌ی نظریه‌اش).
  همچنین same_as فقط برای جفت‌هایی معتبر است که عنوان محتوا
    و عنوان موجودیت تقریباً یکسان باشند (نزدیک‌خوانی دستی 44 جفت
    نشان داد بیشتر same_as‌ها نادرست‌اند).
خروجی: kg_fix_link_types.sql
"""
import subprocess

MYSQL = "C:/Program Files/MySQL/MySQL Server 8.0/bin/mysql.exe"


def dbq(sql):
    r = subprocess.run(
        [MYSQL, "--default-character-set=utf8mb4", "-u", "root", "-p433700",
         "resaname_v2", "-N", "-B", "-e", sql],
        capture_output=True, text=True, encoding="utf-8")
    if r.returncode != 0:
        raise SystemExit("DB ERROR: " + r.stderr[:500])
    return r.stdout


# 1) all same_as rows with their content_type
rows = dbq(
    "SELECT l.entity_id, l.content_id, c.content_type "
    "FROM entity_content_links l "
    "JOIN contents c ON c.id = l.content_id "
    "WHERE l.link_type='same_as';").splitlines()

downgrade = []  # (entity_id, content_id) -> same_as => primary
keep = []
for line in rows:
    p = line.split("\t", 2)
    if len(p) < 3:
        continue
    eid, cid, ctype = p
    if ctype == "theorist":
        downgrade.append((eid, cid))
    else:
        keep.append((eid, cid, ctype))

# 2) non-theorist same_as: keep only if content title ~ entity title (manual list)
# From the manual review, the legitimate same_as pairs (content IS the entity):
LEGIT_SAME_AS = {
    ("doc-card-313", "kg-approach-social-constructivism"),      # برساخت‌گرایی اجتماعی
    ("doc-card-687", "kg-theory-social-exchange"),              # نظریه تبادل اجتماعی
    ("doc-card-680", "kg-theory-uncertainty-reduction"),        # تقلیل عدم قطعیت
    ("doc-card-247", "kg-theory-uncertainty-reduction"),        # (دوباره، عنوان متفاوت)
    ("doc-card-83", "kg-theory-mass-society"),                  # نظریه جامعه توده‌ای
    ("doc-card-76", "kg-subfield-actor-network-theory"),        # نظریه کنشگر-شبکه
    ("doc-card-409", "kg-subfield-actor-network-theory"),       # (نسخهٔ با کشیدهٔ بلند)
    ("doc-card-558", "kg-theory-third-person"),                 # فرضیه اثر شخص سوم
    ("doc-card-681", "kg-theory-social-penetration"),           # نظریه نفوذ اجتماعی
    ("doc-card-12", "kg-theory-two-step"),                      # جریان دو مرحله‌ای
}
# everything else non-theorist same_as -> also downgrade to primary
downgrade += [(e, c) for (e, c, t) in keep
              if (c, e) not in LEGIT_SAME_AS]

lines = ["-- Phase B-5a: fix link_type (theorist same_as -> primary; "
         "non-legit same_as -> primary)", "START TRANSACTION;"]
for eid, cid in downgrade:
    lines.append(
        "UPDATE entity_content_links SET link_type='primary' "
        f"WHERE entity_id='{eid}' AND content_id='{cid}';")
lines.append("COMMIT;")
open("kg_fix_link_types.sql", "w", encoding="utf-8").write(
    "\n".join(lines) + "\n")
print(f"downgraded {len(downgrade)} same_as -> primary; "
      f"kept {len(LEGIT_SAME_AS)} legit same_as")
