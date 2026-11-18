-- ============================================================================
-- resaname_v2 — لایه‌ی هسته‌ی دانش (Knowledge Graph Core)
-- تاریخ: 2026-11-10 | مبنای: resaname_v2 (10 جدول موجود) + سند ۹۳۰ خطی
--
-- اصول طراحی:
--   * کاملاً افزایشی (additive): فقط CREATE TABLE IF NOT EXISTS + ALTER TABLE
--     برای ستون‌های NULL-able. هیچ داده‌ی موجودی (840 contents / 5948 sections /
--     4667 relation_links / 11368 chunks) UPDATE یا DELETE نمی‌شود.
--   * contents.content_type دست‌نخورده می‌ماند (2 نقش دارد: نوع دانش + نوع
--     منبع). طبقه‌بندی دانشی 23 نوعی در لایه‌ی جدا (knowledge_entity_type)
--     ثبت می‌شود و با نگاشت 1:1 به content_type_taxonomy canonical می‌شود.
--   * واژگان رابطه (20 کد UPPER_SNAKE) در جدول مرجع knowledge_relation_types
--     ثبت می‌شود؛ 5 کد legacy موجود (extends, derived_from, related_to,
--     theorist, applied_in) با legacy_code canonical می‌شوند — بدون لمس
--     4667 ردیف relation_links و بدون تغییر PK تجمیعی آن.
--   * همه‌ی جداول: ENGINE=InnoDB, utf8mb4 / utf8mb4_unicode_ci (مطابق v2_schema.sql).
--   * قابل اجرا روی MySQL 8.0 (syntax استاندارد، بدون ویژگی خاص MariaDB).
--
-- ترتیب اجرا (idempotent — قابل اجرا بار‌ها):
--   1) جداول مرجع: entity_types, knowledge_entity_types,
--      knowledge_relation_types, entity_facet_keys
--   2) جداول هسته: knowledge_entities, knowledge_relations, entity_facets,
--      knowledge_scholars, knowledge_works, knowledge_works_authors,
--      entity_content_links
--   3) ALTER TABLE: ستون‌های جدید (nullable) روی contents
--   4) seed: 23 entity type + 23 knowledge entity type + 20 relation type
--      + 8 facet key  (INSERT ... ON DUPLICATE KEY UPDATE)
--
-- نکته‌ی اجرا: این فایل به‌تنهایی USE نمی‌کند تا در هر DB قابل اجرا باشد؛
--   استفاده‌کننده پیش از اجرا `USE resaname_v2;` کند. در این فایل از SET
--   FOREIGN_KEY_CHECKS استفاده شده است تا ترتیب FK و idempotency تضمین شود.
-- ============================================================================

SET NAMES utf8mb4;
SET @OLD_FOREIGN_KEY_CHECKS = @@FOREIGN_KEY_CHECKS;
SET FOREIGN_KEY_CHECKS = 0;

-- ============================================================================
-- بخش ۱: جداول مرجع (reference / vocabulary)
-- ============================================================================

-- ----------------------------------------------------------------------------
-- ۱-۱) entity_types — 23 نوع موجودیت دانش (SCHOOL ... SUBFIELD)
--      نگاشت 1:1 (اختیاری) به type_keyِ content_type_taxonomy برای 13 نوع
--      همپوشان؛ rename‌ها در همین جدول canonical می‌شوند (is_canonical).
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `entity_types` (
  `type_code`         VARCHAR(40)  NOT NULL,          -- SCHOOL, THEORY, METHODOLOGY, ...
  `legacy_type_code`  VARCHAR(40)  DEFAULT NULL,       -- برای merge کدهای هم‌معنا (nullable, unique)
  `content_type_key`  VARCHAR(40)  DEFAULT NULL,       -- نگاشت به content_type_taxonomy.type_key (soft, بدون FK سخت)
  `is_canonical`      TINYINT(1)   NOT NULL DEFAULT 1, -- 0 برای کدهای منسوخ/تکراری
  `domain_group`      VARCHAR(40)  DEFAULT NULL,       -- theoretical | methodological | applied | ...
  `display_fa`        VARCHAR(200) NOT NULL,
  `display_en`        VARCHAR(200) NOT NULL,
  `sort_order`        INT          NOT NULL DEFAULT 0,
  `created_at`        DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at`        DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`type_code`),
  UNIQUE KEY `uq_et_legacy` (`legacy_type_code`),
  KEY `idx_et_content_type` (`content_type_key`),
  KEY `idx_et_group` (`domain_group`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------------------------------------------------------
-- ۱-۲) knowledge_entity_types — 23 نوع طبقه‌بندی دانشی سند (لایه‌ی دوم)
--      این جدول «طبقه‌بندی دانشی» مستقل از contents.content_type است.
--      13 نوع همپوشان با content_type_taxonomy از طریق content_type_key
--      canonical می‌شوند (DRY)؛ 9 rename + 8 جدید اینجا seed می‌شوند.
--      کاربرد: فیلتر/جست‌وجو/دسته‌بندی بدون دست‌کاری contents.
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `knowledge_entity_types` (
  `type_code`         VARCHAR(40)  NOT NULL,           -- SCHOOL, TRADITION, PARADIGM, ...
  `content_type_key`  VARCHAR(40)  DEFAULT NULL,       -- نگاشت به content_type_taxonomy.type_key (برای 13 همپوشان)
  `is_canonical`      TINYINT(1)   NOT NULL DEFAULT 1, -- برای rename (TRADITION->research_tradition و ...)
  `display_fa`        VARCHAR(200) NOT NULL,
  `display_en`        VARCHAR(200) NOT NULL,
  `domain_group`      VARCHAR(40)  DEFAULT NULL,       -- theoretical | methodological | applied | domain
  `sort_order`        INT          NOT NULL DEFAULT 0,
  `created_at`        DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at`        DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`type_code`),
  KEY `idx_ket_content_type` (`content_type_key`),
  KEY `idx_ket_group` (`domain_group`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------------------------------------------------------
-- ۱-۳) knowledge_relation_types — 20 رابطه‌ی دانش (IS_A ... COMPARED_WITH)
--      الگوی content_type_taxonomy: PK = type_code UPPER_SNAKE.
--      legacy_code = کد فعلی در relation_links (5 کد legacy) که canonical
--      می‌شوند؛ 17 کد جدید legacy_code=NULL دارند.
--      canonical key برای نمایش: COALESCE(legacy_code, type_code).
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `knowledge_relation_types` (
  `type_code`         VARCHAR(40)  NOT NULL,           -- IS_A, PART_OF, ..., COMPARED_WITH (UPPER_SNAKE)
  `legacy_code`       VARCHAR(40)  DEFAULT NULL,       -- کد فعلی در relation_links (extends, derived_from, ...)
  `code_fa`           VARCHAR(200) NOT NULL,
  `code_en`           VARCHAR(200) NOT NULL,
  `domain`            ENUM('core','epistemic','provenance','usage') NOT NULL DEFAULT 'core',
  `is_bidirectional`  TINYINT(1)   NOT NULL DEFAULT 0, -- آیا رابطه دوطرفه است؟ (COMPARED_WITH, RELATED_TO)
  `superseded_by`     VARCHAR(40)  DEFAULT NULL,       -- اگر منسوخ شده، به کدام type_code
  `sort_order`        INT          NOT NULL DEFAULT 0,
  `created_at`        DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at`        DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`type_code`),
  UNIQUE KEY `uq_krt_legacy` (`legacy_code`),
  KEY `idx_krt_domain` (`domain`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------------------------------------------------------
-- ۱-۴) entity_facet_keys — بُعد‌های طبقه‌بندی چندبعدی (taxonomies)
--      8 بُعد از سند (بخش ۱۸): نوع دانش، حوزه، رویکرد، سنت نظری،
--      نوع داده، هدف، مقیاس تحلیل، کاربرد.
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `entity_facet_keys` (
  `facet_key`    VARCHAR(40)  NOT NULL,
  `label_fa`     VARCHAR(200) NOT NULL,
  `label_en`     VARCHAR(200) NOT NULL,
  `sort_order`   INT          NOT NULL DEFAULT 0,
  `is_active`    TINYINT(1)   NOT NULL DEFAULT 1,
  `created_at`   DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`facet_key`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ============================================================================
-- بخش ۲: جداول هسته‌ی دانش (core knowledge graph)
-- ============================================================================

-- ----------------------------------------------------------------------------
-- ۲-۱) knowledge_entities — موجودیت‌های دانش با 22 فیلد استاندارد
--      + verification_status, content_hash, created_at, updated_at
--      entity_type -> knowledge_entity_types.type_code (soft)
--      parent_id   -> خود (self-referencing FK, برای hierarchy: مکتب>سنت>نظریه)
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `knowledge_entities` (
  `id`                          VARCHAR(40)  NOT NULL,   -- e.g. ent-frankfurt / ke-0001
  `title_fa`                    VARCHAR(500) NOT NULL,
  `title_en`                    VARCHAR(500) DEFAULT NULL,
  `slug`                        VARCHAR(200) NOT NULL,
  `entity_type`                 VARCHAR(40)  NOT NULL,   -- SCHOOL, THEORY, ... (از knowledge_entity_types)
  `parent_id`                   VARCHAR(40)  DEFAULT NULL, -- self FK (hierarchy)
  `abstract`                    TEXT         DEFAULT NULL,
  `description`                 TEXT         DEFAULT NULL,
  `historical_background`       MEDIUMTEXT   DEFAULT NULL,
  `philosophical_foundations`   TEXT         DEFAULT NULL,
  `key_propositions`            MEDIUMTEXT   DEFAULT NULL, -- متن/JSON گزاره‌های کلیدی
  `key_figures`                 TEXT         DEFAULT NULL, -- نام/معرّف اندیشمندان کلیدی
  `origin_period`               VARCHAR(60)  DEFAULT NULL,  -- e.g. '1923-1969'
  `geographical_origin`         VARCHAR(120) DEFAULT NULL,
  `related_disciplines`         TEXT         DEFAULT NULL,  -- لیست رشته‌های مرتبط
  `applications`                TEXT         DEFAULT NULL,
  `strengths`                   TEXT         DEFAULT NULL,
  `limitations`                 TEXT         DEFAULT NULL,
  `criticisms`                  TEXT         DEFAULT NULL,
  `references`                  MEDIUMTEXT   DEFAULT NULL,  -- منابع/مآخذ (JSON یا متن)
  `status`                      VARCHAR(20)  NOT NULL DEFAULT 'draft', -- draft|active|archived|superseded
  `verification_status`         VARCHAR(20)  NOT NULL DEFAULT 'unverified',
  `content_hash`                CHAR(64)     DEFAULT NULL,
  `created_at`                  DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at`                  DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_ke_slug` (`slug`),
  KEY `idx_ke_type` (`entity_type`),
  KEY `idx_ke_parent` (`parent_id`),
  KEY `idx_ke_status` (`status`),
  KEY `idx_ke_vstatus` (`verification_status`),
  CONSTRAINT `fk_ke_parent` FOREIGN KEY (`parent_id`) REFERENCES `knowledge_entities` (`id`) ON DELETE SET NULL,
  CONSTRAINT `fk_ke_type`   FOREIGN KEY (`entity_type`) REFERENCES `knowledge_entity_types` (`type_code`) ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------------------------------------------------------
-- ۲-۲) knowledge_relations — روابط میان موجودیت‌های دانش
--      source/target -> knowledge_entities.id (FK سخت, CASCADE)
--      relation_type -> knowledge_relation_types.type_code (soft, بدون FK سخت
--      تا درج کدهای legacy/موجود آزاد بماند و 4667 ردیف قدیمی reconcile شوند)
--      PK تجمیعی (source, target, relation_type) — مشابه الگوی relation_links
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `knowledge_relations` (
  `id`                     VARCHAR(40)  NOT NULL,
  `source_entity_id`       VARCHAR(40)  NOT NULL,
  `target_entity_id`       VARCHAR(40)  NOT NULL,
  `relation_type`          VARCHAR(40)  NOT NULL,   -- IS_A, EXTENDS, ... (UPPER_SNAKE)
  `description`            TEXT         DEFAULT NULL,
  `confidence`             DECIMAL(5,4) NOT NULL DEFAULT 0.8000,
  `verification_status`    VARCHAR(20)  NOT NULL DEFAULT 'unverified',
  `extracted_by`           VARCHAR(40)  DEFAULT NULL,
  `created_at`             DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`source_entity_id`,`target_entity_id`,`relation_type`),
  KEY `idx_kr_id` (`id`),
  KEY `idx_kr_target` (`target_entity_id`),
  KEY `idx_kr_type` (`relation_type`),
  KEY `idx_kr_status` (`verification_status`),
  CONSTRAINT `fk_kr_source` FOREIGN KEY (`source_entity_id`) REFERENCES `knowledge_entities` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_kr_target` FOREIGN KEY (`target_entity_id`) REFERENCES `knowledge_entities` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------------------------------------------------------
-- ۲-۳) entity_facets — طبقه‌بندی چندبعدی (entity_id, facet_key, facet_value)
--      facet_value VARCHAR (قابل FTS/index) برای فیلترهای قابل‌جست‌وجو.
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `entity_facets` (
  `entity_id`    VARCHAR(40)  NOT NULL,
  `facet_key`    VARCHAR(40)  NOT NULL,   -- از entity_facet_keys
  `facet_value`  VARCHAR(200) NOT NULL,
  `sort_order`   INT          NOT NULL DEFAULT 0,
  `created_at`   DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`entity_id`,`facet_key`,`facet_value`),
  KEY `idx_ef_facet_value` (`facet_key`,`facet_value`),
  KEY `idx_ef_entity` (`entity_id`),
  CONSTRAINT `fk_ef_entity` FOREIGN KEY (`entity_id`) REFERENCES `knowledge_entities` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_ef_facet`  FOREIGN KEY (`facet_key`) REFERENCES `entity_facet_keys` (`facet_key`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------------------------------------------------------
-- ۲-۴) knowledge_scholars — اندیشمندان/نظریه‌پردازان (لایه‌ی دانشی)
--      تداخل با contents(content_type='theorist'): این جدول برای «موجودیت
--      دانشی» اندیشمند در KG است؛ contents/theorist برای «مدخل شناسنامه‌ای»
--      است. entity_content_links دو را reconcile می‌کند (یک مدخل <-> موجودیت).
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `knowledge_scholars` (
  `id`                    VARCHAR(40)  NOT NULL,
  `name_fa`               VARCHAR(300) NOT NULL,
  `name_en`               VARCHAR(300) DEFAULT NULL,
  `slug`                  VARCHAR(200) NOT NULL,
  `birth_year`            INT          DEFAULT NULL,
  `death_year`            INT          DEFAULT NULL,
  `nationality`           VARCHAR(60)  DEFAULT NULL,
  `affiliation`           VARCHAR(300) DEFAULT NULL,   -- دانشگاه/مؤسسه
  `field`                 VARCHAR(200) DEFAULT NULL,   -- حوزه تخصصی
  `bio`                   MEDIUMTEXT   DEFAULT NULL,
  `known_for`             TEXT         DEFAULT NULL,   -- دستاوردهای شاخص
  `content_id`            VARCHAR(40)  DEFAULT NULL,   -- ارجاع اختیاری به contents(id) (soft, بدون FK)
  `verification_status`   VARCHAR(20)  NOT NULL DEFAULT 'unverified',
  `content_hash`          CHAR(64)     DEFAULT NULL,
  `created_at`            DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at`            DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_scholar_slug` (`slug`),
  KEY `idx_scholar_content` (`content_id`),
  KEY `idx_scholar_name` (`name_fa`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------------------------------------------------------
-- ۲-۵) knowledge_works — آثار علمی بنیادین (لایه‌ی دانشی)
--      مستقل از works موجود (آن برای آثار/مجلات عمومی است). اینجا آثار
--      «بنیادین» که در شبکه‌ی دانش به موجودیت‌ها متصل می‌شوند.
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `knowledge_works` (
  `id`                    VARCHAR(40)  NOT NULL,
  `title`                 VARCHAR(500) NOT NULL,
  `title_en`              VARCHAR(500) DEFAULT NULL,
  `work_type`             VARCHAR(20)  NOT NULL,   -- book | article | study | talk | interview | translation
  `publisher`             VARCHAR(300) DEFAULT NULL,
  `journal`               VARCHAR(300) DEFAULT NULL,
  `publication_year`      INT          DEFAULT NULL,
  `isbn`                  VARCHAR(40)  DEFAULT NULL,
  `doi`                   VARCHAR(100) DEFAULT NULL,
  `issn`                  VARCHAR(20)  DEFAULT NULL,
  `source_url`            VARCHAR(500) DEFAULT NULL,
  `citation_apa`          TEXT         DEFAULT NULL,
  `image_urls`            JSON         DEFAULT NULL,
  `entity_id`             VARCHAR(40)  DEFAULT NULL, -- موجودیت دانشی که اثر متعلق به اوست (soft)
  `verification_status`   VARCHAR(20)  NOT NULL DEFAULT 'unverified',
  `content_hash`          CHAR(64)     DEFAULT NULL,
  `created_at`            DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at`            DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_kw_doi` (`doi`),
  KEY `idx_kw_type` (`work_type`),
  KEY `idx_kw_year` (`publication_year`),
  KEY `idx_kw_entity` (`entity_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------------------------------------------------------
-- ۲-۶) knowledge_works_authors — نویسنده‌ی اثر (چندبه‌چند با knowledge_scholars)
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `knowledge_works_authors` (
  `work_id`    VARCHAR(40) NOT NULL,
  `scholar_id` VARCHAR(40) NOT NULL,
  `role`       VARCHAR(30) NOT NULL DEFAULT 'author', -- author | co_author | editor | translator
  `sort_order` INT         NOT NULL DEFAULT 0,
  PRIMARY KEY (`work_id`,`scholar_id`,`role`),
  KEY `idx_kwa_scholar` (`scholar_id`),
  CONSTRAINT `fk_kwa_work`    FOREIGN KEY (`work_id`)    REFERENCES `knowledge_works`   (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_kwa_scholar` FOREIGN KEY (`scholar_id`) REFERENCES `knowledge_scholars`(`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------------------------------------------------------
-- ۲-۷) entity_content_links — reconcile: موجودیت دانش <-> مدخل contents
--      هر موجودیت دانشی می‌تواند به یک (یا چند) مدخل contents map شود.
--      این، حل تداخل knowledge_scholars با contents/theorist است.
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `entity_content_links` (
  `entity_id`    VARCHAR(40) NOT NULL,
  `content_id`   VARCHAR(40) NOT NULL,
  `link_type`    VARCHAR(30) NOT NULL DEFAULT 'same_as', -- same_as | primary | related
  `sort_order`   INT         NOT NULL DEFAULT 0,
  `created_at`   DATETIME    NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`entity_id`,`content_id`),
  KEY `idx_ecl_content` (`content_id`),
  CONSTRAINT `fk_ecl_entity`  FOREIGN KEY (`entity_id`)  REFERENCES `knowledge_entities` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_ecl_content` FOREIGN KEY (`content_id`) REFERENCES `contents`           (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ============================================================================
-- بخش ۳: ALTER TABLE — ستون‌های جدید روی جدول‌های موجود (کاملاً additive)
--      همه ستون‌ها NULL-able / DEFAULT NULL — هیچ UPDATE روی داده‌ی موجود
--      نمی‌شود و PK / UNIQUE / FK موجود دست‌نخورده می‌مانند.
--
--      برای idempotency (اجرای تکراری بدون خطا)، از stored proc‌هایی
--      استفاده می‌شود که پیش از ADD COLUMN / CREATE INDEX، موجود بودن آن را
--      در INFORMATION_SCHEMA بررسی می‌کنند. این روی MySQL 8.0 استاندارد است
--      (ADD COLUMN IF NOT EXISTS در MySQL 8.0 موجود نیست).
-- ============================================================================

DROP PROCEDURE IF EXISTS `kg_add_column`;
DELIMITER //
CREATE PROCEDURE `kg_add_column`(
  IN p_table VARCHAR(64),
  IN p_column VARCHAR(64),
  IN p_defn TEXT
)
BEGIN
  IF NOT EXISTS (
    SELECT 1 FROM information_schema.COLUMNS
    WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = p_table AND COLUMN_NAME = p_column
  ) THEN
    SET @ddl = CONCAT('ALTER TABLE `', p_table, '` ADD COLUMN `', p_column, '` ', p_defn);
    PREPARE stmt FROM @ddl;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
  END IF;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS `kg_add_index`;
DELIMITER //
CREATE PROCEDURE `kg_add_index`(
  IN p_index VARCHAR(64),
  IN p_table VARCHAR(64),
  IN p_cols TEXT
)
BEGIN
  IF NOT EXISTS (
    SELECT 1 FROM information_schema.STATISTICS
    WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = p_table AND INDEX_NAME = p_index
  ) THEN
    SET @ddl = CONCAT('CREATE INDEX `', p_index, '` ON `', p_table, '` (', p_cols, ')');
    PREPARE stmt FROM @ddl;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
  END IF;
END //
DELIMITER ;

-- contents: ستون‌های جدید برای اتصال به لایه‌ی دانشی (nullable)
--   knowledge_entity_type : type_code از knowledge_entity_types (طبقه‌بندی دانشی)
--   knowledge_entity_id   : id از knowledge_entities (موجودیت دانشی reconcile شده)
CALL kg_add_column('contents','knowledge_entity_type',
  "VARCHAR(40) DEFAULT NULL COMMENT 'طبقه‌بندی دانشی (knowledge_entity_types.type_code)'");
CALL kg_add_column('contents','knowledge_entity_id',
  "VARCHAR(40) DEFAULT NULL COMMENT 'موجودیت دانشی reconcile شده (knowledge_entities.id)'");

-- فیلترهای index روی ستون‌های جدید (nullable)
CALL kg_add_index('idx_contents_ke_type','contents','`knowledge_entity_type`');
CALL kg_add_index('idx_contents_ke_id','contents','`knowledge_entity_id`');

-- relation_links: ستون canonical (nullable) برای canonical کردن بدون UPDATE
--   rel_type_code : type_code از knowledge_relation_types (برای ردیف‌های جدید)
--   روی 4667 ردیف موجود NULL می‌ماند و از طریق legacy_code قابل query است.
CALL kg_add_column('relation_links','rel_type_code',
  "VARCHAR(40) DEFAULT NULL COMMENT 'canonical type_code (knowledge_relation_types.type_code) — برای ردیف‌های جدید'");
CALL kg_add_index('idx_reltypecode','relation_links','`rel_type_code`');

-- پاک‌سازی proc‌های کمکی (پس از اجرا)
DROP PROCEDURE IF EXISTS `kg_add_column`;
DROP PROCEDURE IF EXISTS `kg_add_index`;

SET FOREIGN_KEY_CHECKS = @OLD_FOREIGN_KEY_CHECKS;

-- ============================================================================
-- بخش ۴: seed داده‌های اولیه (idempotent — ON DUPLICATE KEY UPDATE)
-- ============================================================================

-- ----------------------------------------------------------------------------
-- ۴-۱) entity_types — 23 نوع موجودیت دانش (سند، بخش ۱۵)
--      content_type_key: نگاشت به type_key فعلی content_type_taxonomy (13 همپوشان)
-- ----------------------------------------------------------------------------
INSERT INTO `entity_types`
  (type_code, legacy_type_code, content_type_key, is_canonical, domain_group, display_fa, display_en, sort_order) VALUES
  ('SCHOOL',        NULL, 'school',            1, 'theoretical',    'مکتب فکری',            'School of Thought',     1),
  ('TRADITION',     NULL, 'research_tradition',1, 'theoretical',    'سنت فکری',              'Intellectual Tradition',2),
  ('PARADIGM',      NULL, 'paradigm',          1, 'theoretical',    'پارادایم',               'Paradigm',              3),
  ('APPROACH',      NULL, 'paradigm',          0, 'theoretical',    'رویکرد',                'Approach',              4),
  ('THEORY',        NULL, 'theory',            1, 'theoretical',    'نظریه',                 'Theory',                5),
  ('MODEL',         NULL, 'model',             1, 'theoretical',    'مدل',                   'Model',                 6),
  ('FRAMEWORK',     NULL, 'framework',         1, 'theoretical',    'چارچوب نظری',           'Framework',             7),
  ('HYPOTHESIS',    NULL, 'hypothesis',        1, 'theoretical',    'فرضیه',                 'Hypothesis',            8),
  ('LAW',           NULL, 'law',               1, 'theoretical',    'قانون علمی',            'Scientific Law',        9),
  ('CONCEPT',       NULL, 'concept',           1, 'theoretical',    'مفهوم',                 'Concept',              10),
  ('METHODOLOGY',  NULL, 'methodology',       1, 'methodological', 'روش‌شناسی',              'Methodology',          11),
  ('METHOD',        NULL, 'method',            1, 'methodological', 'روش تحقیق',             'Research Method',      12),
  ('DESIGN',        NULL, NULL,                1, 'methodological', 'طرح پژوهش',             'Research Design',      13),
  ('STRATEGY',      NULL, 'strategy',          1, 'methodological', 'استراتژی پژوهش',        'Research Strategy',    14),
  ('TECHNIQUE',     NULL, 'technique',         1, 'methodological', 'فن پژوهش',              'Research Technique',   15),
  ('INSTRUMENT',    NULL, 'tool',              0, 'methodological', 'ابزار پژوهش',           'Research Instrument',  16),
  ('SAMPLING',      NULL, 'method',            0, 'methodological', 'روش نمونه‌گیری',        'Sampling Method',      17),
  ('ANALYSIS',      NULL, 'technique',         0, 'methodological', 'روش تحلیل',             'Analysis Method',      18),
  ('QUALITY',       NULL, 'standard',          0, 'methodological', 'معیار کیفیت پژوهش',     'Quality Criterion',    19),
  ('ETHICS',        NULL, 'principle',         0, 'applied',        'اصل اخلاقی',             'Research Ethics',      20),
  ('SOFTWARE',      NULL, 'tool',              0, 'methodological', 'نرم‌افزار پژوهشی',      'Research Software',    21),
  ('DISCIPLINE',   NULL, 'discipline',        1, 'domain',         'رشته علمی',              'Discipline',           22),
  ('SUBFIELD',      NULL, 'subdiscipline',     1, 'domain',         'حوزه تخصصی',            'Subfield',             23)
ON DUPLICATE KEY UPDATE
  legacy_type_code = VALUES(legacy_type_code),
  content_type_key = VALUES(content_type_key),
  is_canonical     = VALUES(is_canonical),
  domain_group     = VALUES(domain_group),
  display_fa       = VALUES(display_fa),
  display_en       = VALUES(display_en),
  sort_order       = VALUES(sort_order);

-- ----------------------------------------------------------------------------
-- ۴-۲) knowledge_entity_types — 23 نوع طبقه‌بندی دانشی (لایه‌ی دوم)
--      content_type_key: 13 همپوشان canonical؛ rename‌ها is_canonical=0.
-- ----------------------------------------------------------------------------
INSERT INTO `knowledge_entity_types`
  (type_code, content_type_key, is_canonical, display_fa, display_en, domain_group, sort_order) VALUES
  ('SCHOOL',        'school',            1, 'مکتب فکری',            'School of Thought',      'theoretical',    1),
  ('TRADITION',     'research_tradition',0, 'سنت فکری',              'Intellectual Tradition', 'theoretical',    2),
  ('PARADIGM',      'paradigm',          1, 'پارادایم',               'Paradigm',               'theoretical',    3),
  ('APPROACH',      'paradigm',          0, 'رویکرد',                'Approach',               'theoretical',    4),
  ('THEORY',        'theory',            1, 'نظریه',                 'Theory',                 'theoretical',    5),
  ('MODEL',         'model',             1, 'مدل',                   'Model',                  'theoretical',    6),
  ('FRAMEWORK',     'framework',         1, 'چارچوب نظری',           'Framework',              'theoretical',    7),
  ('HYPOTHESIS',    'hypothesis',        1, 'فرضیه',                 'Hypothesis',             'theoretical',    8),
  ('LAW',           'law',               1, 'قانون علمی',            'Scientific Law',         'theoretical',    9),
  ('CONCEPT',       'concept',           1, 'مفهوم',                 'Concept',                'theoretical',   10),
  ('METHODOLOGY',  'methodology',       1, 'روش‌شناسی',              'Methodology',            'methodological',11),
  ('METHOD',        'method',            1, 'روش تحقیق',             'Research Method',        'methodological',12),
  ('DESIGN',        NULL,                1, 'طرح پژوهش',             'Research Design',        'methodological',13),
  ('STRATEGY',      'strategy',          1, 'استراتژی پژوهش',        'Research Strategy',      'methodological',14),
  ('TECHNIQUE',     'technique',         1, 'فن پژوهش',              'Research Technique',     'methodological',15),
  ('INSTRUMENT',    'tool',              0, 'ابزار پژوهش',           'Research Instrument',    'methodological',16),
  ('SAMPLING',      'method',            0, 'روش نمونه‌گیری',        'Sampling Method',        'methodological',17),
  ('ANALYSIS',      'technique',         0, 'روش تحلیل',             'Analysis Method',        'methodological',18),
  ('QUALITY',       'standard',          0, 'معیار کیفیت پژوهش',     'Quality Criterion',      'methodological',19),
  ('ETHICS',        'principle',         0, 'اصل اخلاقی',             'Research Ethics',        'applied',        20),
  ('SOFTWARE',      'tool',              0, 'نرم‌افزار پژوهشی',      'Research Software',      'methodological',21),
  ('DISCIPLINE',   'discipline',        1, 'رشته علمی',              'Discipline',             'domain',         22),
  ('SUBFIELD',      'subdiscipline',     1, 'حوزه تخصصی',            'Subfield',               'domain',         23)
ON DUPLICATE KEY UPDATE
  content_type_key = VALUES(content_type_key),
  is_canonical     = VALUES(is_canonical),
  display_fa       = VALUES(display_fa),
  display_en       = VALUES(display_en),
  domain_group     = VALUES(domain_group),
  sort_order       = VALUES(sort_order);

-- ----------------------------------------------------------------------------
-- ۴-۳) knowledge_relation_types — 20 رابطه‌ی دانش (سند، بخش ۱۶)
--      legacy_code: 5 کد فعلی در relation_links (extends, derived_from,
--      related_to, theorist, applied_in) canonical می‌شوند؛ 15 کد جدید NULL.
--      canonical key = COALESCE(legacy_code, type_code).
-- ----------------------------------------------------------------------------
INSERT INTO `knowledge_relation_types`
  (type_code, legacy_code, code_fa, code_en, domain, is_bidirectional, sort_order) VALUES
  ('IS_A',            NULL,         'از نوعِ',            'is a',                 'core',       0,  1),
  ('PART_OF',         NULL,         'زیرمجموعه',           'part of',              'core',       0,  2),
  ('BELONGS_TO',      NULL,         'متعلق به',            'belongs to',           'core',       0,  3),
  ('INFLUENCED_BY',   NULL,         'متأثر از',            'influenced by',        'epistemic',  0,  4),
  ('INFLUENCED',      NULL,         'تأثیرگذار بر',        'influenced',           'epistemic',  0,  5),
  ('CRITICIZES',      NULL,         'نقدکننده',            'criticizes',           'epistemic',  0,  6),
  ('EXTENDS',         'extends',    'توسعه‌دهنده',          'extends',              'epistemic',  0,  7),
  ('CONTRADICTS',     NULL,         'متناقض با',           'contradicts',          'epistemic',  1,  8),
  ('RELATED_TO',      'related_to', 'مرتبط با',            'related to',           'core',       1,  9),
  ('APPLIES_TO',      'applied_in', 'کاربرد در',           'applies to',           'usage',      0, 10),
  ('USES',            NULL,         'استفاده می‌کند از',    'uses',                 'usage',      0, 11),
  ('MEASURES',        NULL,         'اندازه‌گیری می‌کند',   'measures',             'usage',      0, 12),
  ('ANALYZES',        NULL,         'تحلیل می‌کند',         'analyzes',             'usage',      0, 13),
  ('COLLECTS',        NULL,         'گردآوری می‌کند',       'collects',             'usage',      0, 14),
  ('DEVELOPED_BY',    'theorist',   'توسعه‌یافته توسط',     'developed by',         'provenance', 0, 15),
  ('PROPOSED_BY',     NULL,         'پیشنهادشده توسط',     'proposed by',          'provenance', 0, 16),
  ('OPERATIONALIZES', NULL,         'عملیاتی‌سازی می‌کند',  'operationalizes',      'usage',      0, 17),
  ('TESTS',           NULL,         'آزمون می‌کند',         'tests',                'usage',      0, 18),
  ('DERIVED_FROM',    'derived_from','برگرفته از',          'derived from',         'epistemic',  0, 19),
  ('COMPARED_WITH',   NULL,         'قابل مقایسه با',       'compared with',        'epistemic',  1, 20)
ON DUPLICATE KEY UPDATE
  legacy_code        = VALUES(legacy_code),
  code_fa            = VALUES(code_fa),
  code_en            = VALUES(code_en),
  domain             = VALUES(domain),
  is_bidirectional   = VALUES(is_bidirectional),
  sort_order         = VALUES(sort_order);

-- ----------------------------------------------------------------------------
-- ۴-۴) entity_facet_keys — 8 بُعد طبقه‌بندی چندبعدی (سند، بخش ۱۸)
-- ----------------------------------------------------------------------------
INSERT INTO `entity_facet_keys` (facet_key, label_fa, label_en, sort_order) VALUES
  ('knowledge_type',  'نوع دانش',      'Knowledge Type',    1),
  ('domain',          'حوزه',          'Domain',            2),
  ('approach',        'رویکرد',        'Approach',          3),
  ('theoretical_tradition', 'سنت نظری', 'Theoretical Tradition', 4),
  ('data_type',       'نوع داده',      'Data Type',         5),
  ('objective',       'هدف',          'Objective',         6),
  ('analysis_scale',  'مقیاس تحلیل',   'Analysis Scale',    7),
  ('application',     'کاربرد',       'Application',       8)
ON DUPLICATE KEY UPDATE
  label_fa   = VALUES(label_fa),
  label_en   = VALUES(label_en),
  sort_order = VALUES(sort_order);

-- ============================================================================
-- پایان — idempotent، کاملاً افزایشی، بدون لمس داده‌ی موجود.
-- ============================================================================
