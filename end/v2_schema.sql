-- ============================================================================
-- resaname_v2 — ساختار ساختاریافته جدید (20/18 بخشی) + جدول works + لایه RAG
-- تاریخ: 2026-11-10 | مبنای داده‌ای: resaname_h
-- مدل: جدول مرکزی چندمرکب (contents) + جدول واحد بخش‌ها (sections)
--      + آثار جداگانه (works) + روابط (relation_links) + لایه RAG (chunks)
-- ============================================================================

DROP DATABASE IF EXISTS resaname_v2;
CREATE DATABASE resaname_v2
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;
USE resaname_v2;

-- ----------------------------------------------------------------------------
-- ۱) جدول مرکزی: contents
--    یک ردیف = یک مدخل (نظریه‌پرداز / نظریه / مدل / چارچوب / اثر / مجله / ...)
--    فیلدهای ثابتِ «شناسنامه + معرفی + دسته‌بندی» برای همه انواع.
-- ----------------------------------------------------------------------------
CREATE TABLE `contents` (
  `id`             VARCHAR(40)  NOT NULL,            -- doc-card-N / doc-new-theorist-N / doc-new-theory-N
  `source_type`    VARCHAR(20)  NOT NULL,            -- card | theorist | theory | book | journal | ...
  `content_type`   VARCHAR(40)  NOT NULL,            -- theory | model | framework | theorist | effect | ...
  `source_id`      VARCHAR(40)  NOT NULL,            -- card-N / th-new-N / th-N / nt-new-N
  `slug`           VARCHAR(200) NOT NULL,
  `title`          VARCHAR(500) NOT NULL,            -- عنوان فارسی
  `english_title`  VARCHAR(500) DEFAULT NULL,        -- عنوان انگلیسی
  `summary`        TEXT         DEFAULT NULL,        -- معرفی کوتاه (100-150 کلمه)
  `canonical_url`  VARCHAR(500) DEFAULT NULL,
  `language`       VARCHAR(5)   NOT NULL DEFAULT 'fa',
  `country`        VARCHAR(60)  DEFAULT NULL,
  `origin`         VARCHAR(30)  DEFAULT NULL,        -- iranian | islamic_middle_east | international
  `nationality`    VARCHAR(60)  DEFAULT NULL,
  `field`          VARCHAR(200) DEFAULT NULL,        -- حوزه تخصصی / رشته مادر
  `year`           INT          DEFAULT NULL,        -- سال شکل‌گیری / فعالیت
  `image_url`      VARCHAR(500) DEFAULT NULL,
  `image_urls`     JSON         DEFAULT NULL,        -- چند تصویر (برای انتخاب ویرایشگر)
  `verification_status` VARCHAR(20) NOT NULL DEFAULT 'unverified',
  `content_hash`   CHAR(64)     DEFAULT NULL,
  `source_updated_at` DATETIME  DEFAULT NULL,
  `indexed_at`     DATETIME     DEFAULT NULL,
  `created_at`     DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at`     DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_contents_source` (`source_type`,`source_id`),
  UNIQUE KEY `uq_contents_slug` (`slug`),
  KEY `idx_contents_type` (`content_type`),
  KEY `idx_contents_origin` (`origin`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------------------------------------------------------
-- ۲) جدول بخش‌ها: sections
--    هر ردیف = یک بخش (section) از یک content.
--    section_key از کالکشن 18 بخشی (نظریه) یا 20 بخشی (نظریه‌پرداز) می‌آید.
--    این جدول هم برای نظریه‌ها (18 بخش) و هم نظریه‌پردازان (20 بخش) و هم
--    کارتهای فعلی (8 بخش) استفاده می‌شود — یعنی یک جدول واحد چندمرکب.
-- ----------------------------------------------------------------------------
CREATE TABLE `sections` (
  `id`             VARCHAR(40)  NOT NULL,
  `content_id`     VARCHAR(40)  NOT NULL,
  `section_key`    VARCHAR(40)  NOT NULL,            -- از فهرست کلیدهای بخش (پایین)
  `section_title`  VARCHAR(300) DEFAULT NULL,
  `content`        MEDIUMTEXT   NOT NULL,
  `content_hash`   CHAR(64)     DEFAULT NULL,
  `sort_order`     INT          NOT NULL DEFAULT 0,
  `group`          VARCHAR(20)  DEFAULT NULL,        -- group 1..4 (برای نظریه‌ها) / group 1..5 (نظریه‌پرداز)
  `created_at`     DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at`     DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_section` (`content_id`,`section_key`,`sort_order`),
  KEY `idx_sections_key` (`section_key`),
  CONSTRAINT `fk_sections_content` FOREIGN KEY (`content_id`) REFERENCES `contents` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------------------------------------------------------
-- ۳) آثار و مطالعات: works  (جدول جداگانه، رابطه‌پذیر)
--    یک اثر = کتاب / مقاله / پژوهش / سخنرانی / مصاحبه
-- ----------------------------------------------------------------------------
CREATE TABLE `works` (
  `id`             VARCHAR(40)  NOT NULL,
  `work_type`      VARCHAR(20)  NOT NULL,            -- book | article | study | talk | interview | translation
  `title`          VARCHAR(500) NOT NULL,
  `title_en`       VARCHAR(500) DEFAULT NULL,
  `publisher`      VARCHAR(300) DEFAULT NULL,
  `journal`        VARCHAR(300) DEFAULT NULL,
  `publication_year` INT       DEFAULT NULL,
  `isbn`           VARCHAR(40)  DEFAULT NULL,
  `doi`            VARCHAR(100) DEFAULT NULL,
  `issn`           VARCHAR(20)  DEFAULT NULL,
  `source_url`     VARCHAR(500) DEFAULT NULL,
  `citation_apa`   TEXT         DEFAULT NULL,
  `image_urls`     JSON         DEFAULT NULL,
  `verification_status` VARCHAR(20) NOT NULL DEFAULT 'unverified',
  `created_at`     DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at`     DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_works_doi` (`doi`),
  KEY `idx_works_type` (`work_type`),
  KEY `idx_works_year` (`publication_year`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- نویسنده اثر (چندبه‌چند). person_ref = idِ theorist/content
CREATE TABLE `works_authors` (
  `work_id`   VARCHAR(40) NOT NULL,
  `person_id` VARCHAR(40) NOT NULL,      -- contents.id (نظریه‌پرداز) یا نام
  `role`      VARCHAR(30) NOT NULL DEFAULT 'author',  -- author | co_author | editor | translator
  `sort_order` INT NOT NULL DEFAULT 0,
  PRIMARY KEY (`work_id`,`person_id`,`role`),
  CONSTRAINT `fk_workauthor_work` FOREIGN KEY (`work_id`) REFERENCES `works` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------------------------------------------------------
-- ۴) روابط دانش: relation_links
--    چندمرکب: هر سر (source/target) می‌تواند content / work / concept باشد.
-- ----------------------------------------------------------------------------
CREATE TABLE `relation_links` (
  `id`             VARCHAR(40) NOT NULL,
  `source_type`    VARCHAR(30) NOT NULL,   -- content | work | concept
  `source_id`      VARCHAR(40) NOT NULL,
  `relationship_type` VARCHAR(40) NOT NULL, -- theorist | extends | derived_from | applied_in | related_to | competes_with | ...
  `target_type`    VARCHAR(30) NOT NULL,
  `target_id`      VARCHAR(200) NOT NULL,
  `description`    TEXT         DEFAULT NULL,
  `confidence`     DECIMAL(5,4) NOT NULL DEFAULT 0.8000,
  `verification_status` VARCHAR(20) NOT NULL DEFAULT 'unverified',
  `extracted_by`   VARCHAR(40)  DEFAULT NULL,
  `created_at`     DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`source_id`,`relationship_type`,`target_id`),
  KEY `idx_rel_id` (`id`),
  KEY `idx_rel_type` (`relationship_type`),
  KEY `idx_rel_target` (`target_id`),
  KEY `idx_rel_status` (`verification_status`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------------------------------------------------------
-- ۵) مفاهیم/اصطلاحات کلیدی: concepts + content_concepts
-- ----------------------------------------------------------------------------
CREATE TABLE `concepts` (
  `id`         VARCHAR(40) NOT NULL,
  `name`       VARCHAR(300) NOT NULL,
  `name_en`    VARCHAR(300) DEFAULT NULL,
  `slug`       VARCHAR(200) NOT NULL,
  `definition` TEXT DEFAULT NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_concepts_slug` (`slug`),
  KEY `idx_concepts_name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `content_concepts` (
  `content_id` VARCHAR(40) NOT NULL,
  `concept_id` VARCHAR(40) NOT NULL,
  PRIMARY KEY (`content_id`,`concept_id`),
  CONSTRAINT `fk_cc_concept` FOREIGN KEY (`concept_id`) REFERENCES `concepts` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_cc_content` FOREIGN KEY (`content_id`) REFERENCES `contents` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------------------------------------------------------
-- ۶) لایه RAG: chunks (برای embedding + جست‌وجوی برداری)
-- ----------------------------------------------------------------------------
CREATE TABLE `chunks` (
  `id`              VARCHAR(40)  NOT NULL,
  `content_id`      VARCHAR(40)  NOT NULL,
  `section_id`      VARCHAR(40)  DEFAULT NULL,
  `chunk_index`     INT          NOT NULL,
  `content`         MEDIUMTEXT   NOT NULL,
  `content_hash`    CHAR(64)     DEFAULT NULL,
  `token_count`     INT          DEFAULT NULL,
  `vector_point_id` VARCHAR(80)  DEFAULT NULL,
  `embedding_model` VARCHAR(100) DEFAULT NULL,
  `embedding_version` VARCHAR(20) DEFAULT NULL,
  `created_at`      DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at`      DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `idx_chunks_content` (`content_id`),
  CONSTRAINT `fk_chunks_content` FOREIGN KEY (`content_id`) REFERENCES `contents` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------------------------------------------------------
-- ۷) کالکشن کلیدهای بخش (مستندسازی + مرجع)
--    نظریه‌ها: 18 کلید در 4 گروه
--    نظریه‌پردازان: 20 کلید در 5 گروه
-- ----------------------------------------------------------------------------
CREATE TABLE `section_catalog` (
  `content_type` VARCHAR(40) NOT NULL,  -- theory | theorist | ...
  `group_no`     INT         NOT NULL,  -- 1..4 / 1..5
  `group_name`   VARCHAR(200) NOT NULL,
  `section_key`  VARCHAR(40) NOT NULL,
  `section_title` VARCHAR(300) NOT NULL,
  `importance`   VARCHAR(20) NOT NULL DEFAULT 'required', -- required | optional
  PRIMARY KEY (`content_type`,`section_key`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------------------------------------------------------
-- ۸) طبقه‌بندی 33 نوع محتوا در ۶ دسته (مرجع contents.content_type)
--    داده‌ها در v2_taxonomy.sql وارد می‌شوند.
-- ----------------------------------------------------------------------------
CREATE TABLE `content_type_taxonomy` (
  `category_no`  TINYINT      NOT NULL,
  `category_key` VARCHAR(40)  NOT NULL,
  `category_fa`  VARCHAR(200) NOT NULL,
  `category_en`  VARCHAR(200) NOT NULL,
  `type_key`     VARCHAR(40)  NOT NULL,
  `type_fa`      VARCHAR(200) NOT NULL,
  `type_en`      VARCHAR(200) NOT NULL,
  `sort_order`   INT          NOT NULL,
  PRIMARY KEY (`type_key`),
  KEY `idx_taxonomy_category` (`category_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
