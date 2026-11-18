-- ============================================================================
-- RESANAME AI — Migration: جداول ai_* (فاز ۲)
-- تاریخ: 2026-11-09
-- مرجع: بند ۴ «ساختار داده» سند فنی سامانه‌ی هوشمند رسانامه (نسخه ۱٫۰)
-- موتور: InnoDB | کاراکتری: utf8mb4 | Collation: utf8mb4_unicode_ci
-- نکته: DDL سند فنی «الگوی مرجع» است؛ قبل از اجرا روی سرور مقصد،
--       نسخه‌ی MySQL/Collation را بررسی کنید (بخش ۴.۵ سند فنی).
--       این جداول با جدول‌های سایت فعلی (cards, theorists, …) مشترک نیستند.
-- ============================================================================

USE resaname_h;

-- ----------------------------------------------------------------------------
-- 1) ai_documents — هر مدخل (کارت/نظریه‌پرداز/کتاب/مجله) یک بار
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `ai_documents` (
  `id`            VARCHAR(40)  NOT NULL,                 -- document-N
  `source_type`   VARCHAR(20)  NOT NULL,                 -- card | theorist | book | journal | theory
  `source_id`     VARCHAR(40)  NOT NULL,                 -- e.g. card-1 / th-1 / book-N / journal-N
  `slug`          VARCHAR(200) NOT NULL,
  `title`         VARCHAR(500) NOT NULL,
  `english_title` VARCHAR(500) DEFAULT NULL,
  `content_type`  VARCHAR(40)  DEFAULT NULL,              -- theory/model/framework/effect/hypothesis/theorist/book/journal
  `summary`       TEXT         DEFAULT NULL,              -- تعریف کوتاه ۲–۴ جمله‌ای (خلاء اصلی)
  `canonical_url` VARCHAR(500) DEFAULT NULL,              -- https://resaname.ir/cards/card-N
  `language`      VARCHAR(5)   NOT NULL DEFAULT 'fa',
  `country`       VARCHAR(60)  DEFAULT NULL,              -- برای theorist: نام کشور
  `origin`        VARCHAR(30)  DEFAULT NULL,              -- iranian | islamic_middle_east | international
  `content_hash`  CHAR(64)     DEFAULT NULL,              -- SHA-256 متن کامل
  `source_updated_at` DATETIME DEFAULT NULL,
  `indexed_at`    DATETIME     DEFAULT NULL,
  `created_at`    DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at`    DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_ai_documents_source` (`source_type`, `source_id`),
  UNIQUE KEY `uq_ai_documents_slug` (`slug`),
  KEY `idx_ai_documents_type` (`content_type`),
  KEY `idx_ai_documents_origin` (`origin`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------------------------------------------------------
-- 2) ai_document_sections — بخش‌بندی هر مدخل (10 section_key استاندارد)
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `ai_document_sections` (
  `id`           VARCHAR(40)  NOT NULL,                  -- section-N
  `document_id`  VARCHAR(40)  NOT NULL,
  `section_key`  VARCHAR(40)  NOT NULL,
    -- definition | introduction | history | theoretical_framework |
    -- components | applications | examples | criticism |
    -- limitations | references
  `section_title` VARCHAR(300) DEFAULT NULL,
  `content`      MEDIUMTEXT   NOT NULL,
  `content_hash` CHAR(64)     DEFAULT NULL,
  `sort_order`   INT          NOT NULL DEFAULT 0,
  `created_at`   DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at`   DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_section_doc_key` (`document_id`, `section_key`, `sort_order`),
  CONSTRAINT `fk_sections_document` FOREIGN KEY (`document_id`) REFERENCES `ai_documents` (`id`) ON DELETE CASCADE,
  KEY `idx_sections_key` (`section_key`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------------------------------------------------------
-- 3) ai_concepts — مفاهیم کلیدی ساختاریافته
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `ai_concepts` (
  `id`         VARCHAR(40)  NOT NULL,                    -- concept-N
  `name`       VARCHAR(300) NOT NULL,
  `name_en`    VARCHAR(300) DEFAULT NULL,
  `slug`       VARCHAR(200) NOT NULL,
  `definition` TEXT         DEFAULT NULL,
  `created_at` DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_concepts_slug` (`slug`),
  KEY `idx_concepts_name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------------------------------------------------------
-- 4) ai_entities — موجودیت‌ها (theorist / person / org / platform / book / journal)
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `ai_entities` (
  `id`           VARCHAR(40)  NOT NULL,                  -- entity-N
  `entity_type`  VARCHAR(30)  NOT NULL,                   -- theorist | person | organization | platform | book | journal | concept
  `name`         VARCHAR(300) NOT NULL,
  `name_en`      VARCHAR(300) DEFAULT NULL,
  `slug`         VARCHAR(200) NOT NULL,
  `country`      VARCHAR(60)  DEFAULT NULL,
  `origin`       VARCHAR(30)  DEFAULT NULL,               -- iranian | islamic_middle_east | international
  `year`         INT          DEFAULT NULL,
  `nationality`  VARCHAR(60)  DEFAULT NULL,
  `field`        VARCHAR(200) DEFAULT NULL,
  `main_theory`  VARCHAR(300) DEFAULT NULL,
  `image_urls`   JSON         DEFAULT NULL,               -- ["url1","url2"] — الزام ۲ تصویر
  `summary`      TEXT         DEFAULT NULL,
  `external_url` VARCHAR(500) DEFAULT NULL,
  `verification_status` VARCHAR(20) NOT NULL DEFAULT 'unverified',  -- verified | unverified | disputed
  `created_at`   DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at`   DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_entities_slug` (`slug`),
  KEY `idx_entities_type` (`entity_type`),
  KEY `idx_entities_origin` (`origin`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------------------------------------------------------
-- 5) ai_relationships — روابط دانش (شبکه‌ی مفهومی)
--    واژگان relationship_type (نسخه اول):
--    extends | derived_from | related_to | contrasts_with |
--    theorist | cites | applied_in | predates
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `ai_relationships` (
  `id`                  VARCHAR(40)  NOT NULL,            -- rel-N
  `source_type`         VARCHAR(30)  NOT NULL,            -- document | entity | concept
  `source_id`           VARCHAR(40)  NOT NULL,
  `relationship_type`   VARCHAR(40)  NOT NULL,
  `target_type`         VARCHAR(30)  NOT NULL,            -- document | entity | concept
  `target_id`           VARCHAR(200) NOT NULL,
  `description`         TEXT         DEFAULT NULL,        -- توضیح رابطه به فارسی
  `confidence`          DECIMAL(5,4) NOT NULL DEFAULT 0.8000,  -- 0.0000 تا 1.0000
  `verification_status` VARCHAR(20)  NOT NULL DEFAULT 'unverified',  -- verified | unverified | disputed
  `extracted_by`        VARCHAR(40)  DEFAULT NULL,        -- manual | ai-model-N (طبق بند ۴.۳: AI → unverified)
  `created_at`          DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_rel` (`source_id`, `relationship_type`, `target_id`),
  KEY `idx_rel_type` (`relationship_type`),
  KEY `idx_rel_target` (`target_id`),
  KEY `idx_rel_status` (`verification_status`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------------------------------------------------------
-- 6) ai_references — منابع/ارجاعات ساختاریافته
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `ai_references` (
  `id`           VARCHAR(40)  NOT NULL,                  -- ref-N
  `reference_type` VARCHAR(20) NOT NULL,                 -- book | article | journal | chapter | website
  `title`        VARCHAR(500) NOT NULL,
  `title_en`     VARCHAR(500) DEFAULT NULL,
  `authors`      JSON         DEFAULT NULL,              -- ["Author, A.","Author, B."]
  `publisher`    VARCHAR(300) DEFAULT NULL,
  `journal`      VARCHAR(300) DEFAULT NULL,
  `publication_year` INT     DEFAULT NULL,
  `isbn`         VARCHAR(40)  DEFAULT NULL,
  `doi`          VARCHAR(100) DEFAULT NULL,              -- فقط اگر با Crossref تأییدشده باشد
  `issn`         VARCHAR(20)  DEFAULT NULL,              -- برای reference_type=journal
  `source_url`   VARCHAR(500) DEFAULT NULL,
  `citation_apa` TEXT         DEFAULT NULL,
  `image_urls`   JSON         DEFAULT NULL,
  `verification_status` VARCHAR(20) NOT NULL DEFAULT 'unverified',
  `created_at`   DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at`   DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_references_doi` (`doi`),
  KEY `idx_references_type` (`reference_type`),
  KEY `idx_references_year` (`publication_year`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------------------------------------------------------
-- 7) ai_document_references — اتصال مدخل ↔ منبع (relation_type=cites)
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `ai_document_references` (
  `document_id`  VARCHAR(40) NOT NULL,
  `section_id`   VARCHAR(40) DEFAULT NULL,               -- بخش references (اختیاری)
  `reference_id` VARCHAR(40) NOT NULL,
  `relation_type` VARCHAR(20) NOT NULL DEFAULT 'cites',  -- cites | discussed_in | reviewed
  `sort_order`   INT         NOT NULL DEFAULT 0,
  PRIMARY KEY (`document_id`, `reference_id`, `sort_order`),
  CONSTRAINT `fk_docref_document` FOREIGN KEY (`document_id`) REFERENCES `ai_documents` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_docref_reference` FOREIGN KEY (`reference_id`) REFERENCES `ai_references` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------------------------------------------------------
-- 8) ai_document_concepts — اتصال مدخل ↔ مفهوم
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `ai_document_concepts` (
  `document_id` VARCHAR(40) NOT NULL,
  `concept_id`  VARCHAR(40) NOT NULL,
  `role`        VARCHAR(30) NOT NULL DEFAULT 'key',      -- key | mentioned | central
  PRIMARY KEY (`document_id`, `concept_id`),
  CONSTRAINT `fk_docconcept_document` FOREIGN KEY (`document_id`) REFERENCES `ai_documents` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_docconcept_concept` FOREIGN KEY (`concept_id`) REFERENCES `ai_concepts` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------------------------------------------------------
-- 9) ai_chunks — قطعات برای embedding + Qdrant
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `ai_chunks` (
  `id`             VARCHAR(40) NOT NULL,                 -- chunk-N
  `document_id`    VARCHAR(40) NOT NULL,
  `section_id`     VARCHAR(40) DEFAULT NULL,
  `chunk_index`    INT         NOT NULL DEFAULT 0,
  `content`        MEDIUMTEXT  NOT NULL,
  `content_hash`   CHAR(64)    NOT NULL,
  `token_count`    INT         DEFAULT NULL,             -- هدف: ۴۰۰–۷۰۰
  `vector_point_id` VARCHAR(80) DEFAULT NULL,            -- point id در Qdrant
  `embedding_model` VARCHAR(100) DEFAULT NULL,
  `embedding_version` VARCHAR(20) DEFAULT NULL,
  `created_at`     DATETIME    NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at`     DATETIME    NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_chunks_doc` (`document_id`, `chunk_index`),
  CONSTRAINT `fk_chunks_document` FOREIGN KEY (`document_id`) REFERENCES `ai_documents` (`id`) ON DELETE CASCADE,
  KEY `idx_chunks_hash` (`content_hash`),
  KEY `idx_chunks_vector` (`vector_point_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------------------------------------------------------
-- 10) ai_sync_queue — صف همگام‌سازی (Initial / Incremental / Reindex)
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `ai_sync_queue` (
  `id`           BIGINT        NOT NULL AUTO_INCREMENT,
  `entity_type`  VARCHAR(30)   NOT NULL,                  -- document | entity | reference
  `entity_id`    VARCHAR(40)   NOT NULL,
  `operation`    VARCHAR(20)   NOT NULL DEFAULT 'upsert', -- upsert | delete | reindex
  `reason`       VARCHAR(100)  DEFAULT NULL,
  `status`       VARCHAR(20)   NOT NULL DEFAULT 'pending',-- pending | processing | done | failed
  `attempts`     INT           NOT NULL DEFAULT 0,
  `last_error`   TEXT          DEFAULT NULL,
  `created_at`   DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `processed_at` DATETIME      DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_sync_status` (`status`),
  KEY `idx_sync_entity` (`entity_type`, `entity_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------------------------------------------------------
-- 11) ai_sync_logs — لاگ هر اجرای همگام‌سازی
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `ai_sync_logs` (
  `id`          BIGINT        NOT NULL AUTO_INCREMENT,
  `run_type`    VARCHAR(20)   NOT NULL,                   -- initial | incremental | reindex
  `started_at`  DATETIME      NOT NULL,
  `finished_at` DATETIME      DEFAULT NULL,
  `documents`   INT           DEFAULT 0,
  `sections`    INT           DEFAULT 0,
  `relationships` INT        DEFAULT 0,
  `references`  INT           DEFAULT 0,
  `chunks`      INT           DEFAULT 0,
  `embeddings`  INT           DEFAULT 0,
  `skipped_hash` INT          DEFAULT 0,                  -- تکراری با content_hash
  `errors`      INT           DEFAULT 0,
  `details`     JSON          DEFAULT NULL,
  `status`      VARCHAR(20)   NOT NULL DEFAULT 'running', -- running | success | failed
  PRIMARY KEY (`id`),
  KEY `idx_logs_type` (`run_type`),
  KEY `idx_logs_started` (`started_at`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ============================================================================
-- پایان Migration — ۱۱ جدول ai_*
-- برای ساخت Collection Qdrant (resaname_knowledge_v1) به بخش فاز ۶ برنامه مراجعه شود.
-- ============================================================================
