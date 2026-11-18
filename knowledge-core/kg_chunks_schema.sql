-- ============================================================================
-- هسته‌ی دانش (resaname_v2) — جدول kg_chunks (فاز A: RAG)
-- additive: هیچ جدول/ستون موجودی دست نمی‌خورد.
-- آیینه‌ی سبک ai_chunks (resaname_h) برای موجودیت‌های هسته‌ی دانش.
-- ============================================================================
SET NAMES utf8mb4;
USE resaname_v2;

CREATE TABLE IF NOT EXISTS `kg_chunks` (
  `id`                VARCHAR(60)  NOT NULL,          -- kc-<entity_id>-<n>
  `entity_id`         VARCHAR(40)  NOT NULL,
  `chunk_index`       INT          NOT NULL DEFAULT 0,
  `content`           MEDIUMTEXT   NOT NULL,
  `content_hash`      CHAR(64)     NOT NULL,          -- SHA-256(content)
  `token_count`       INT          NOT NULL DEFAULT 0,
  `vector_point_id`   VARCHAR(60)  DEFAULT NULL,      -- = id (1:1)
  `embedding_model`   VARCHAR(60)  DEFAULT NULL,
  `embedding_version` VARCHAR(10)  DEFAULT NULL,
  `created_at`        DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `idx_kgc_entity` (`entity_id`),
  CONSTRAINT `fk_kgc_entity` FOREIGN KEY (`entity_id`)
    REFERENCES `knowledge_entities` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
