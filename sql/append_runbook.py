# -*- coding: utf-8 -*-
"""Append the full AI runbook blocks to ../resaname_h.sql in execution order.

Preconditions (verified):
  - resaname_h.sql currently = site dump + ONLY the Phase-6f block (11,878,369 B).
  - source files exist in sql/: migration-ai-tables.sql, seed-731-cards-full.sql,
    seed-phase4-70-items.sql, resolve-64-matched.sql, resolve-remaining.sql.
  - the Phase-6f block is ALREADY in resaname_h.sql (do NOT re-append).

Blocks appended (each wrapped in a dated Persian header):
  1. فاز 0 — ساختار ai_*        (migration-ai-tables.sql)
  2. فاز 3 — 731 کارت           (seed-731-cards-full.sql)
  3. فاز 4 — 70 مورد جدید        (seed-phase4-70-items.sql)
  4. فاز 5 — حل روابط            (resolve-64-matched.sql + resolve-remaining.sql)
  5. فاز 6 — ابزار (سندسازی)      (no SQL; documents build_vectorstore.py + gap_fix_55.py)
  6. فاز 3b — ستون origin (DoD #9) (theorists: ADD COLUMN IF NOT EXISTS + 39-row backfill)

The 39 original site theorists (th-1..th-39) all map 1:1 to ai_entities
entity-th-1..entity-th-39, every one origin='international' in the live DB.
"""
import sys
import hashlib

SQL_DIR = r"D:\رسانامه تکمیلی\sql"
TARGET = r"D:\رسانامه تکمیلی\resaname_h.sql"
DATE = "2026-11-09"

def read(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def md5(s):
    return hashlib.md5(s.encode("utf-8")).hexdigest()[:12]

def header(title, note=""):
    h = (
        "\n-- ============================================================================\n"
        f"-- RESANAME AI — {title}\n"
        f"-- تاریخ: {DATE} | منبع: {note}\n"
        "-- ============================================================================\n"
    )
    return h

# ---- read source files ----
mig = read(f"{SQL_DIR}\\migration-ai-tables.sql")
s3 = read(f"{SQL_DIR}\\seed-731-cards-full.sql")
s4 = read(f"{SQL_DIR}\\seed-phase4-70-items.sql")
r1 = read(f"{SQL_DIR}\\resolve-64-matched.sql")
r2 = read(f"{SQL_DIR}\\resolve-remaining.sql")

# sanity: each must contain a USE or be pure DDL/INSERT
for name, txt in [("migration", mig), ("s3", s3), ("s4", s4), ("r1", r1), ("r2", r2)]:
    assert txt.strip(), f"{name} is empty"
    print(f"  {name}: {len(txt)} bytes, md5={md5(txt)}")

# ---- origin backfill (theorists) ----
# 39 rows: th-1..th-39 -> international (all verified from ai_entities live DB)
origin_rows = []
for i in range(1, 40):
    origin_rows.append(
        f"UPDATE `theorists` SET `origin`='international' WHERE `id`='th-{i}';"
    )

origin_block = header(
    "فاز 3b — ستون origin بر روی جدول theorists (DoD #9)",
    "theorists (site) | 39 نظریه‌پرداز اصلی | همه international"
) + (
    "-- ستون origin به جدول سایت theorists اضافه می‌شود (idempotent, MySQL 8.0).\n"
    "-- ارزش‌ها از ai_entities (DB زنده) خوانده شده‌اند: th-1..th-39 همه international.\n"
    "-- (جدول ai_entities خودش در seed-731 ستون origin دارد؛ این بلوک فقط برای ستون سایت است.)\n"
    "DROP PROCEDURE IF EXISTS `_add_origin_col`;\n"
    "DELIMITER //\n"
    "CREATE PROCEDURE `_add_origin_col`()\n"
    "BEGIN\n"
    "  IF NOT EXISTS (\n"
    "    SELECT 1 FROM information_schema.COLUMNS\n"
    "    WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = 'theorists' AND COLUMN_NAME = 'origin'\n"
    "  ) THEN\n"
    "    ALTER TABLE `theorists` ADD COLUMN `origin` VARCHAR(30) DEFAULT NULL\n"
    "      COMMENT 'iranian | islamic_middle_east | international' AFTER `nationality`;\n"
    "  END IF;\n"
    "END //\n"
    "DELIMITER ;\n"
    "CALL `_add_origin_col`();\n"
    "DROP PROCEDURE IF EXISTS `_add_origin_col`;\n\n"
    + "\n".join(origin_rows) + "\n"
)

# ---- assemble in execution order ----
blocks = [
    header("فاز 0 — ساختار جداول ai_* (فاز ۲)", "sql/migration-ai-tables.sql") + mig.strip() + "\n",
    header("فاز 3 — 731 کارت (ساختاردهی کامل)", "sql/seed-731-cards-full.sql") + s3.strip() + "\n",
    header("فاز 4 — 70 مورد جدید (theorist/theory/book/journal)", "sql/seed-phase4-70-items.sql") + s4.strip() + "\n",
    header("فاز 5 — حل روابط __unresolved (بخش 1: 64 matched)", "sql/resolve-64-matched.sql") + r1.strip() + "\n"
        + header("فاز 5 — حل روابط __unresolved (بخش 2: باقی‌مانده، dedup)", "sql/resolve-remaining.sql") + r2.strip() + "\n",
    header("فاز 6 — ابزار (سندسازی، بدون SQL)", "sql/build_vectorstore.py + sql/gap_fix_55.py")
        + (
            "-- ---------------------------------------------------------------\n"
            "-- فاز 6 (chunk + embed) بخشی از runbook SQL نیست: 648MB بردار\n"
            "-- 2560-dim به‌درستی در یک فایل SQL جا نمی‌شود.\n"
            "-- ابزارها (روی DB ساخته‌شده از همین فایل اجرا می‌شوند):\n"
            "--   1) python sql/build_vectorstore.py  → ai_chunks + resaname_vectors.sqlite\n"
            "--   2) python sql/gap_fix_55.py         → 55 چانک رفع‌خلأ + vectors.json\n"
            "-- بردارها: Qwen3-Embedding-4B (2560-dim)، L2-normalized، store محلی SQLite+numpy.\n"
            "-- ---------------------------------------------------------------\n"
        ),
    origin_block,
]

append_text = "\n".join(blocks)

# ---- guard: ensure we don't duplicate (check target tail) ----
target_now = read(TARGET)
assert "فاز 6f" in target_now, "Phase-6f block not found in target — unexpected state"
# make sure we are NOT about to double-append migration (it should be absent now)
assert "فاز 0 — ساختار" not in target_now, "migration block already present — would double-append"

with open(TARGET, "a", encoding="utf-8") as f:
    f.write("\n" + append_text)

new_size = len(read(TARGET).encode("utf-8"))
print(f"\nAppended {len(append_text)} bytes ({len(blocks)} blocks)")
print(f"resaname_h.sql now {new_size} bytes")
print("Blocks: migration | seed-731 | seed-phase4 | resolve-64 | resolve-remaining | phase6-note | origin-backfill")
