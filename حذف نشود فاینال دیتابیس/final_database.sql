-- ============================================================================
-- هسته‌ی دانش علمی رسانامه — دیتابیس فاینال (نسخه‌ی کامل‌تر سایت)
-- Resaname Knowledge Core — FINAL Database (v2, greenfield)
-- ----------------------------------------------------------------------------
-- این فایل:
--   (الف) دیتابیس خالیِ جدید را می‌سازد (فقط ساختار + registries هستی‌شناسی)
--   (ب) هیچ داده‌ی محتوایی (581 موجودیت / 384 رابطه / 1886 فاکت / 71 لینک) وارد نمی‌کند
-- registries (نوع/خانواده/رابطه/فاکت/واژگان) «ساختار» دیتابیس‌اند و اینجا پر می‌شوند.
-- داده‌ی محتوایی بعداً با اسکریپتِ seed یک‌باره از دیتابیس قدیمی map می‌شود.
--
-- مبنای طراحی: docs/RM-KCORE-ONTOLOGY-SPEC-review-v2-greenfield.md
-- تک منبع حقیقتِ کد: app/Knowledge/*  (EntityTypes, EntityFamilies, EntitySchemas,
--   RelationTypes, FacetTypes, ControlledVocab, EntitySchemaValidator)
--
-- موتور: InnoDB / utf8mb4 / utf8mb4_unicode_ci
-- ============================================================================

CREATE DATABASE IF NOT EXISTS resaname_kb_final
  DEFAULT CHARACTER SET utf8mb4
  DEFAULT COLLATE utf8mb4_unicode_ci;

USE resaname_kb_final;

-- برای اجرای مجددِ بدون خطا (DROP به ترتیبِ کودک-پیش-والد نیازی نیست)
SET FOREIGN_KEY_CHECKS=0;

-- ============================================================================
-- بخش 1 — جدول‌های «تک منبع حقیقت» (registries)
-- ============================================================================

-- 1.1) خانواده‌های هستی‌شناختی (8 خانواده)
DROP TABLE IF EXISTS kb_entity_families;
CREATE TABLE kb_entity_families (
  code        VARCHAR(40)  NOT NULL PRIMARY KEY,
  label_fa    VARCHAR(200) NOT NULL,
  label_en    VARCHAR(200) NOT NULL,
  description TEXT         NULL,
  sort_order  INT NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 1.2) انواع موجودیت (36 نوع) — family_code به خانواده اشاره دارد
DROP TABLE IF EXISTS kb_entity_types;
CREATE TABLE kb_entity_types (
  code        VARCHAR(40)  NOT NULL PRIMARY KEY,
  label_fa    VARCHAR(200) NOT NULL,
  label_en    VARCHAR(200) NOT NULL,
  family_code VARCHAR(40)  NOT NULL,
  domain      ENUM('theoretical','methodological','shared') NOT NULL,
  description TEXT         NULL,
  sort_order  INT NOT NULL DEFAULT 0,
  CONSTRAINT fk_type_family FOREIGN KEY (family_code) REFERENCES kb_entity_families(code)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 1.3) فرهنگِ روابط (canonical) — با domain/range و معکوس
DROP TABLE IF EXISTS kb_relation_types;
CREATE TABLE kb_relation_types (
  code                 VARCHAR(40)  NOT NULL PRIMARY KEY,
  label_fa             VARCHAR(200) NOT NULL,
  label_en             VARCHAR(200) NOT NULL,
  description          TEXT         NULL,
  symmetric            TINYINT(1)   NOT NULL DEFAULT 0,
  allowed_source_types JSON         NULL,   -- آرایه‌ی کدهای نوع مبدأ؛ ["*"] = هر نوع
  allowed_target_types JSON         NULL,   -- آرایه‌ی کدهای نوع مقصد؛ ["*"] = هر نوع
  inverse_code         VARCHAR(40)  NULL,   -- نمایش معکوس (رکورد جدا ذخیره نمی‌شود)
  requires_evidence    TINYINT(1)   NOT NULL DEFAULT 0,
  sort_order           INT NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 1.4) ابعاد فاکت (13 فاکت)
DROP TABLE IF EXISTS kb_facet_dimensions;
CREATE TABLE kb_facet_dimensions (
  code        VARCHAR(60)  NOT NULL PRIMARY KEY,
  label_fa    VARCHAR(200) NOT NULL,
  label_en    VARCHAR(200) NOT NULL,
  description TEXT         NULL,
  value_kind  ENUM('STRING','ENTITY_REF','TIME_PERIOD') NOT NULL DEFAULT 'STRING',
  sort_order  INT NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 1.5) registryِ واژگان کنترل‌شده‌ی مقادیر فاکت
DROP TABLE IF EXISTS kb_facet_values;
CREATE TABLE kb_facet_values (
  id          BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  facet_code  VARCHAR(60)  NOT NULL,
  code        VARCHAR(60)  NOT NULL,
  label_fa    VARCHAR(200) NOT NULL,
  label_en    VARCHAR(200) NULL,
  definition  TEXT         NULL,
  entity_ref  VARCHAR(80)  NULL,   -- برای value_kind=ENTITY_REF؛ کد موجودیتِ ارجاع‌شده
  active      TINYINT(1)   NOT NULL DEFAULT 1,
  sort_order  INT NOT NULL DEFAULT 0,
  UNIQUE KEY uq_facet_val (facet_code, code),
  KEY idx_fv_entity (entity_ref),
  CONSTRAINT fk_fv_facet FOREIGN KEY (facet_code) REFERENCES kb_facet_dimensions(code)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ============================================================================
-- بخش 2 — جدول‌های هسته (موجودیت، رابطه، فاکت)
-- ============================================================================

-- 2.1) موجودیت‌های دانش — قرارداد کامل (Core Entity Contract)
--     id = کلید فنی (PK) ; code = شناسه‌ی پایدار و خوانا (business key)
DROP TABLE IF EXISTS kb_entities;
CREATE TABLE kb_entities (
  id                BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  code              VARCHAR(80)  NOT NULL,
  entity_type       VARCHAR(40)  NOT NULL,
  family_code       VARCHAR(40)  NOT NULL,
  canonical_name_fa VARCHAR(500) NOT NULL,
  canonical_name_en VARCHAR(500) NULL,
  slug              VARCHAR(200) NOT NULL,
  aliases           JSON         NULL,          -- نام‌های جایگزین چندزبانه
  original_name     VARCHAR(500) NULL,          -- نام اصلی در زبان مبدأ
  original_language VARCHAR(10)  NULL,          -- زبان اصلی اصطلاح/موجودیت
  language          VARCHAR(10)  NOT NULL DEFAULT 'fa',
  properties        JSON         NULL,          -- ویژگی‌های اختصاصی نوع (تأییدشده با EntitySchemas)
  -- سه محور وضعیتِ مستقل (هرگز در یک فیلد ادغام نشوند):
  status_workflow   ENUM('draft','in_review','approved','published','archived') NOT NULL DEFAULT 'draft',
  status_scientific ENUM('unassessed','supported','partially_supported','contested','refuted','not_applicable') NOT NULL DEFAULT 'unassessed',
  status_lifecycle  ENUM('active','historical','superseded','deprecated','unknown') NOT NULL DEFAULT 'active',
  visibility        ENUM('public','restricted','private') NOT NULL DEFAULT 'public',
  version           INT NOT NULL DEFAULT 1,
  external_identifiers JSON      NULL,          -- DOI / ORCID / ISBN و ...
  created_at        DATETIME     NOT NULL,
  created_by        VARCHAR(80)  NOT NULL DEFAULT 'seed',
  updated_at        DATETIME     NOT NULL,
  updated_by        VARCHAR(80)  NOT NULL DEFAULT 'seed',
  verified_at       DATETIME     NULL,
  verified_by       VARCHAR(80)  NULL,
  UNIQUE KEY uq_e_code  (code),
  UNIQUE KEY uq_e_slug  (slug),
  KEY idx_e_type   (entity_type),
  KEY idx_e_family (family_code),
  KEY idx_e_status (status_workflow, status_scientific, status_lifecycle),
  KEY idx_e_vis    (visibility),
  CONSTRAINT fk_e_type   FOREIGN KEY (entity_type) REFERENCES kb_entity_types(code),
  CONSTRAINT fk_e_family FOREIGN KEY (family_code) REFERENCES kb_entity_families(code)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 2.2) زیرنوع / طبقه‌بندی چندوالد (به‌جای آرایه‌ی JSON)
DROP TABLE IF EXISTS kb_entity_subtypes;
CREATE TABLE kb_entity_subtypes (
  id          BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  entity_code VARCHAR(80)  NOT NULL,
  subtype_code VARCHAR(80) NOT NULL,   -- کدِ زیرنوع/طبقه‌ی متعلق
  note        VARCHAR(500) NULL,
  UNIQUE KEY uq_subtype (entity_code, subtype_code),
  KEY idx_sub_type (subtype_code),
  CONSTRAINT fk_sub_entity FOREIGN KEY (entity_code) REFERENCES kb_entities(code) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 2.3) روابطِ بین‌موجودیتی — qualified (با دوره‌ی اعتبار، شاهد، تأییدکننده)
DROP TABLE IF EXISTS kb_relations;
CREATE TABLE kb_relations (
  id          BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  source_id   BIGINT UNSIGNED NOT NULL,
  target_id   BIGINT UNSIGNED NOT NULL,
  relation_type VARCHAR(40)  NOT NULL,
  valid_from  DATE NULL,
  valid_until DATE NULL,
  assertion_status ENUM('unverified','under_review','verified','contested','rejected') NOT NULL DEFAULT 'under_review',
  asserted_by VARCHAR(80)  NULL,
  verified_by VARCHAR(80)  NULL,
  extraction_confidence DECIMAL(4,3) NULL,   -- اطمینانِ استخراج (نه اعتبار علمی)
  note        VARCHAR(500) NULL,
  weight      TINYINT UNSIGNED NOT NULL DEFAULT 50,
  status      ENUM('draft','active','needs_review','rejected') NOT NULL DEFAULT 'active',
  created_at  DATETIME NOT NULL,
  updated_at  DATETIME NOT NULL,
  UNIQUE KEY uq_rel (source_id, target_id, relation_type),
  KEY idx_rel_src  (source_id),
  KEY idx_rel_tgt  (target_id),
  KEY idx_rel_type (relation_type),
  KEY idx_rel_asrt (assertion_status),
  CONSTRAINT fk_rel_src  FOREIGN KEY (source_id)   REFERENCES kb_entities(id) ON DELETE CASCADE,
  CONSTRAINT fk_rel_tgt  FOREIGN KEY (target_id)   REFERENCES kb_entities(id) ON DELETE CASCADE,
  CONSTRAINT fk_rel_type FOREIGN KEY (relation_type) REFERENCES kb_relation_types(code)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 2.4) فاکت‌های موجودیت (ارجاع به واژگان کنترل‌شده)
DROP TABLE IF EXISTS kb_entity_facets;
CREATE TABLE kb_entity_facets (
  id             BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  entity_id      BIGINT UNSIGNED NOT NULL,
  facet_code     VARCHAR(60)  NOT NULL,
  facet_value_id BIGINT UNSIGNED NULL,   -- برای فاکت‌های STRING/ENTITY_REF
  sort_order     INT NOT NULL DEFAULT 0,
  created_at     DATETIME NOT NULL,
  UNIQUE KEY uq_ef (entity_id, facet_code, facet_value_id),
  KEY idx_ef_facet (facet_code, facet_value_id),
  CONSTRAINT fk_ef_entity   FOREIGN KEY (entity_id)      REFERENCES kb_entities(id) ON DELETE CASCADE,
  CONSTRAINT fk_ef_facet    FOREIGN KEY (facet_code)     REFERENCES kb_facet_dimensions(code),
  CONSTRAINT fk_ef_facetval FOREIGN KEY (facet_value_id) REFERENCES kb_facet_values(id) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ============================================================================
-- بخش 3 — جدول‌های منبع / استناد / شاهد / منشأ (provenance)
-- ============================================================================

-- 3.1) منابع علمی (SOURCE به‌عنوان جدول ارجاعی؛ اگر همان WORK است → work_id)
DROP TABLE IF EXISTS kb_sources;
CREATE TABLE kb_sources (
  id            BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  kind          ENUM('BOOK','JOURNAL_ARTICLE','BOOK_CHAPTER','THESIS','REPORT','STANDARD','DATA_REPOSITORY','WEBSITE','ARCHIVE','OTHER') NOT NULL,
  title_fa      VARCHAR(500) NOT NULL,
  title_en      VARCHAR(500) NULL,
  year          INT NULL,
  publisher     VARCHAR(300) NULL,
  doi           VARCHAR(120) NULL,
  isbn          VARCHAR(60)  NULL,
  issn          VARCHAR(60)  NULL,
  url           VARCHAR(500) NULL,
  language      VARCHAR(10)  NULL,
  access_type   ENUM('open','restricted','commercial','unknown') NOT NULL DEFAULT 'unknown',
  bibliographic JSON NULL,
  work_id       BIGINT UNSIGNED NULL,   -- اگر منبع همان یک WORK است (جلوگیری از duplicate)
  KEY idx_src_work (work_id),
  KEY idx_src_kind (kind),
  CONSTRAINT fk_src_work FOREIGN KEY (work_id) REFERENCES kb_entities(id) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 3.2) استنادها (Citation: به کدام بخش از منبع)
DROP TABLE IF EXISTS kb_citations;
CREATE TABLE kb_citations (
  id            BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  source_id     BIGINT UNSIGNED NOT NULL,
  locator_type  ENUM('PAGE','CHAPTER','SECTION','PARAGRAPH','TABLE','FIGURE','TIMESTAMP','URL_FRAGMENT') NOT NULL DEFAULT 'PAGE',
  locator_value VARCHAR(200) NULL,
  quoted_text   TEXT NULL,
  paraphrase    TEXT NULL,
  citation_style VARCHAR(40)  NULL,
  language      VARCHAR(10)   NULL,
  accessed_at   DATETIME      NULL,
  KEY idx_cit_source (source_id),
  CONSTRAINT fk_cit_source FOREIGN KEY (source_id) REFERENCES kb_sources(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 3.3) شواهد علمی (Evidence: قطعه‌ای که یک ادعا را پشتیبانی/به چالش می‌کشد)
DROP TABLE IF EXISTS kb_evidence;
CREATE TABLE kb_evidence (
  id            BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  source_id     BIGINT UNSIGNED NULL,
  citation_id   BIGINT UNSIGNED NULL,
  about_code    VARCHAR(80)  NULL,   -- موجودیتی که شاهد درباره‌ی آن است
  evidence_type VARCHAR(40)  NULL,   -- نقل مستقیم / نتیجه‌ی آماری / مشاهده / ...
  evidence_summary TEXT NULL,
  quoted_content  TEXT NULL,
  locator       VARCHAR(200) NULL,
  page_start    INT NULL,
  page_end      INT NULL,
  direction     ENUM('supports','challenges','neutral') NOT NULL DEFAULT 'neutral',
  extraction_method ENUM('manual','source_extraction','ai_extraction','inference') NOT NULL DEFAULT 'manual',
  verification_status ENUM('unverified','under_review','verified','contested','rejected') NOT NULL DEFAULT 'unverified',
  extraction_confidence DECIMAL(4,3) NULL,
  KEY idx_ev_source (source_id),
  KEY idx_ev_about  (about_code),
  KEY idx_ev_dir    (direction),
  CONSTRAINT fk_ev_source   FOREIGN KEY (source_id)   REFERENCES kb_sources(id) ON DELETE SET NULL,
  CONSTRAINT fk_ev_citation FOREIGN KEY (citation_id) REFERENCES kb_citations(id) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ============================================================================
-- بخش 4 — جدول‌های نسخه‌بندی / ممیزی / پیوند به سایت
-- ============================================================================

-- 4.1) نسخه‌های immutableِ رکورد (history کامل)
DROP TABLE IF EXISTS kb_entity_versions;
CREATE TABLE kb_entity_versions (
  id           BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  entity_id    BIGINT UNSIGNED NOT NULL,
  version      INT NOT NULL,
  snapshot     JSON NOT NULL,      -- تصویر کامل رکورد در آن نسخه
  change_reason VARCHAR(500) NULL,
  changed_by   VARCHAR(80)  NULL,
  created_at   DATETIME NOT NULL,
  UNIQUE KEY uq_ver (entity_id, version),
  CONSTRAINT fk_ver_entity FOREIGN KEY (entity_id) REFERENCES kb_entities(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 4.2) ممیزی: ردپای تغییرات
DROP TABLE IF EXISTS kb_audit_log;
CREATE TABLE kb_audit_log (
  id          BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  entity_code VARCHAR(80)  NULL,
  action      VARCHAR(60)  NOT NULL,
  detail      JSON         NULL,
  source      VARCHAR(60)  NOT NULL DEFAULT 'manual',
  created_at  DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  KEY idx_audit_entity (entity_code),
  KEY idx_audit_time   (created_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 4.3) پیوند به محتوای دیتابیسِ اصلیِ سایت (cards / theorists / library_resources / categories)
DROP TABLE IF EXISTS kb_entity_links;
CREATE TABLE kb_entity_links (
  id          BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  entity_id   BIGINT UNSIGNED NOT NULL,
  link_type   ENUM('card','theorist','library_resource','category') NOT NULL,
  link_id     VARCHAR(64)  NOT NULL,
  link_title  VARCHAR(500) NULL,
  note        VARCHAR(500) NULL,
  confidence  ENUM('verified','suggested') NOT NULL DEFAULT 'suggested',
  created_by  VARCHAR(80)  NOT NULL DEFAULT 'seed',
  created_at  DATETIME NOT NULL,
  UNIQUE KEY uq_link (entity_id, link_type, link_id),
  KEY idx_link (link_type, link_id),
  CONSTRAINT fk_link_entity FOREIGN KEY (entity_id) REFERENCES kb_entities(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ============================================================================
-- بخش 5 — SEEDِ registries (ساختار هستی‌شناسی؛ نه داده‌ی محتوایی)
-- ============================================================================

-- 5.1) 8 خانواده
INSERT INTO kb_entity_families (code, label_fa, label_en, description, sort_order) VALUES
('THEORETICAL_SYSTEM',   'نظام‌های فکری و پارادایمی',    'Theoretical & Paradigmatic Systems', 'مکتب‌ها، سنت‌ها و پارادایم‌ها', 1),
('KNOWLEDGE_STRUCTURE',  'ساختارهای نظری و مفهومی',      'Theoretical & Conceptual Structures', 'نظریه، مدل، چارچوب، فرضیه، قانون، مفهوم، گزاره، سازه، متغیر، شاخص', 2),
('SCIENTIFIC_DOMAIN',    'قلمروهای علمی و مناقشات',      'Scientific Domains & Disputes',       'رشته‌ها، حوزه‌های تخصصی و مناقشات علمی', 3),
('RESEARCH_METHODOLOGY',  'نظام روش‌شناختی و اجرایی پژوهش', 'Research Methodology & Execution',    'روش‌شناسی تا پروتکل', 4),
('RESEARCH_ACTIVITY',    'فعالیت و خروجی پژوهش',          'Research Activity & Outputs',           'مسئله، پرسش، مطالعه، یافته', 5),
('RESEARCH_RESOURCE',    'منابع و زیرساخت پژوهش',         'Research Resources & Infrastructure',   'اثر، مجموعه‌داده، نرم‌افزار', 6),
('INTELLECTUAL_AGENT',   'کنشگران علمی',                  'Intellectual Agents',                   'شخص‌ها و پژوهشگران', 7),
('SCIENTIFIC_ARGUMENTATION','استدلال و ادعا',              'Scientific Argumentation',              'رزرو برای مدل‌سازی استدلال (ARGUMENT) — فاز 2', 8);

-- 5.2) 36 نوع موجودیت
INSERT INTO kb_entity_types (code, label_fa, label_en, family_code, domain, description, sort_order) VALUES
-- THEORETICAL_SYSTEM
('SCHOOL',     'مکتب فکری',            'School of Thought',        'THEORETICAL_SYSTEM','theoretical','جریان یا سنت منسجمی از اندیشه که حول یک مرکز علمی شکل گرفته و نظریه‌ها و روش‌های مشخصی دارد.',1),
('TRADITION',  'سنت فکری',             'Intellectual Tradition',   'THEORETICAL_SYSTEM','theoretical','سنت و جریان فکری (معمولا میان‌رشته‌ای) که مبانی فلسفی/روش‌شناختی یک حوزه را تأمین می‌کند.',2),
('PARADIGM',   'پارادایم',              'Research Paradigm',        'THEORETICAL_SYSTEM','theoretical','مبانی هستی‌شناختی و معرفت‌شناختی پژوهش که چارچوب کلی پرسش، روش و تفسیر را تعیین می‌کند.',3),
-- KNOWLEDGE_STRUCTURE
('THEORY',     'نظریه',                'Theory',                   'KNOWLEDGE_STRUCTURE','theoretical','مجموعه‌ای منسجم از مفروضات و گزاره‌ها که یک پدیده را تبیین و پیش‌بینی می‌کند.',4),
('MODEL',      'مدل',                  'Model',                    'KNOWLEDGE_STRUCTURE','theoretical','ترسیم ساده‌شده و شماتیک از فرآیند یا نظامی واقعی؛ توصیفی است نه صرفا تبیینی.',5),
('FRAMEWORK',  'چارچوب نظری',           'Theoretical Framework',    'KNOWLEDGE_STRUCTURE','theoretical','چارچوب تحلیلی ترکیبی که پژوهشگر از چند نظریه/مفهوم می‌سازد.',6),
('HYPOTHESIS', 'فرضیه',                'Hypothesis',               'KNOWLEDGE_STRUCTURE','theoretical','گزاره‌ی آزمودنی درباره رابطه دو یا چند متغیر.',7),
('LAW',        'قانون علمی',           'Scientific Law',           'KNOWLEDGE_STRUCTURE','theoretical','گزاره‌ی عمومی و پایدار درباره رابطه پدیده‌ها که در طول زمان تأیید شده.',8),
('CONCEPT',    'مفهوم',                'Concept',                  'KNOWLEDGE_STRUCTURE','theoretical','واحد بنیادین تفکر علمی؛ اصطلاحی که پدیده‌ای را نام‌گذاری و مفهوم‌سازی می‌کند.',9),
('PROPOSITION','گزاره علمی',           'Scientific Proposition',   'KNOWLEDGE_STRUCTURE','theoretical','ادعای معنادار و قابل ارزیابی درباره یک مفهوم، رابطه یا سازوکار؛ الزاماً فرضیه تجربی نیست.',10),
('CONSTRUCT',  'سازه نظری',             'Theoretical Construct',    'KNOWLEDGE_STRUCTURE','theoretical','مفهوم نظری انتزاعی که برای کاربرد پژوهشی به تعریف نظری و عملیاتی‌سازی نیاز دارد.',11),
('VARIABLE',   'متغیر',                'Variable',                 'KNOWLEDGE_STRUCTURE','theoretical','ویژگی یا کمیتی از واحد تحلیل که در یک مطالعه می‌تواند مقادیر متفاوت بگیرد.',12),
('INDICATOR',  'شاخص',                 'Indicator',                'KNOWLEDGE_STRUCTURE','theoretical','نشانه یا سنجه‌ی مشاهده‌پذیر برای ارزیابی یک مفهوم یا سازه.',13),
-- SCIENTIFIC_DOMAIN
('DISCIPLINE',  'رشته علمی',           'Discipline',               'SCIENTIFIC_DOMAIN','theoretical','حوزه‌ای منسجم از دانش با روش‌ها و مرزهای مشخص.',14),
('SUBFIELD',   'حوزه تخصصی',           'Subfield',                 'SCIENTIFIC_DOMAIN','theoretical','حوزه مطالعاتی تخصصی زیر یک رشته یا مکتب.',15),
('DISPUTE',    'مناقشه علمی',           'Academic Dispute',         'SCIENTIFIC_DOMAIN','shared',     'اختلاف‌نظر نظری یا روش‌شناختی مستند بین دیدگاه‌ها یا اندیشمندان.',16),
-- RESEARCH_METHODOLOGY
('METHODOLOGY','روش‌شناسی',            'Methodology',              'RESEARCH_METHODOLOGY','methodological','نظام منسجم از اصول و معیارهایی که منطق کلی پژوهش را تعیین می‌کند.',17),
('METHOD',     'روش تحقیق',            'Research Method',          'RESEARCH_METHODOLOGY','methodological','راهبرد کلی و منسجمی برای پاسخ به پرسش پژوهش.',18),
('APPROACH',   'رویکرد پژوهش',          'Research Approach',        'RESEARCH_METHODOLOGY','methodological','نگاه و روی کار پژوهشگر در قبال پرسش و داده که از پارادایم می‌آید.',19),
('DESIGN',     'طرح پژوهش',            'Research Design',          'RESEARCH_METHODOLOGY','methodological','نقشه‌ی دقیق «چه کاری، در چه ترتیبی، با چه داده‌ای».',20),
('STRATEGY',   'استراتژی پژوهش',        'Research Strategy',        'RESEARCH_METHODOLOGY','methodological','راهبرد میان‌رده بین روش و فن.',21),
('TECHNIQUE',  'فن پژوهش',             'Research Technique',       'RESEARCH_METHODOLOGY','methodological','فن و ابزار عملی گردآوری/پردازش داده.',22),
('INSTRUMENT', 'ابزار پژوهش',           'Research Instrument',      'RESEARCH_METHODOLOGY','methodological','ابزار یا دسته ابزارهایی برای سنجش و گردآوری داده.',23),
('SAMPLING',   'روش نمونه‌گیری',        'Sampling Method',          'RESEARCH_METHODOLOGY','methodological','روش انتخاب نمونه از جامعه یا چارچوب نمونه‌گیری.',24),
('ANALYSIS',   'روش تحلیل داده',        'Data Analysis Method',     'RESEARCH_METHODOLOGY','methodological','روش و فن پردازش و تفسیر داده.',25),
('QUALITY',    'معیار کیفیت پژوهش',    'Quality Criterion',        'RESEARCH_METHODOLOGY','methodological','معیار سنجش اعتبار، پایایی و کیفیت پژوهش.',26),
('ETHICS',     'اصل اخلاقی پژوهش',     'Research Ethics',          'RESEARCH_METHODOLOGY','methodological','اصل و استاندارد اخلاقی در طراحی، اجرا و انتشار پژوهش.',27),
('SOFTWARE',   'نرم‌افزار پژوهشی',      'Research Software',        'RESEARCH_RESOURCE','methodological','نرم‌افزار یا ابزار محاسباتی مورد استفاده در پژوهش.',28),
('PROTOCOL',   'پروتکل پژوهشی',         'Research Protocol',        'RESEARCH_METHODOLOGY','methodological','دستورالعمل و راهنمای اجرایی استاندارد برای یک فرآیند پژوهشی.',29),
('DATASET',    'داده و منبع پژوهشی',    'Dataset / Data Source',    'RESEARCH_RESOURCE','methodological','مجموعه‌داده، آرشیو یا مخزن داده مورد استفاده پژوهشگران.',30),
-- RESEARCH_ACTIVITY
('RESEARCH_PROBLEM',  'مسئله‌ی پژوهش',     'Research Problem',       'RESEARCH_ACTIVITY','methodological','وضعیت، شکاف دانشی یا تناقضی که پژوهش برای فهم/حل آن صورت‌بندی می‌شود.',31),
('RESEARCH_QUESTION', 'پرسش پژوهش',        'Research Question',      'RESEARCH_ACTIVITY','methodological','پرسش دقیق و قابل پاسخ که دامنه و جهت مطالعه را تعیین می‌کند.',32),
('RESEARCH_STUDY',    'مطالعه‌ی پژوهشی',   'Research Study',         'RESEARCH_ACTIVITY','methodological','اجرای مشخص و محدودشده‌ی یک تحقیق با هدف، پرسش، طرح، داده و نتایج قابل شناسایی.',33),
('FINDING',           'یافته‌ی پژوهشی',   'Research Finding',       'RESEARCH_ACTIVITY','methodological','نتیجه‌ی مشخص حاصل از تحلیل داده که به یک مطالعه و شواهد قابل ردیابی است.',34),
-- RESEARCH_RESOURCE
('WORK',    'اثر علمی بنیادین',          'Foundational Work',        'RESEARCH_RESOURCE','shared',         'کتاب، مقاله یا پژوهش تأثیرگذار که مرجع یک نظریه، مکتب یا روش است.',35),
('PERSON',  'اندیشمند و نظریه‌پرداز',    'Scholar / Theorist',       'INTELLECTUAL_AGENT','shared',         'نظریه‌پرداز، دانشمند یا مؤثر علمی؛ صاحب نظریه، بنیان‌گذار مکتب یا توسعه‌دهنده‌ی روش.',36);

-- 5.3) فرهنگِ روابط (canonical) — با domain/range و معکوس
--     allowed_* = ["*"] یعنی هر نوع؛ در غیر این صورت فهرست صریح.
INSERT INTO kb_relation_types
(code, label_fa, label_en, description, symmetric, allowed_source_types, allowed_target_types, inverse_code, requires_evidence, sort_order) VALUES
-- 20 رابطه‌ی هسته (همان داده‌ی فعلی — برای سازگاری seed حفظ شدند)
('IS_A',           'از نوعِ',                 'is a kind of',     'رابطه‌ی جنس‌به‌فصله: source از نظر target است.', 0, JSON_ARRAY('*'), JSON_ARRAY('*'), 'HAS_SUBCLASS', 0, 1),
('PART_OF',        'زیرمجموعه',               'part of',          'source بخش یا زیرمجموعه‌ی target است.', 0, JSON_ARRAY('*'), JSON_ARRAY('*'), 'HAS_PART', 0, 2),
('BELONGS_TO',     'متعلق به',                'belongs to',       'source در قلمرو یا نظام target قرار دارد.', 0, JSON_ARRAY('*'), JSON_ARRAY('*'), NULL, 0, 3),
('INFLUENCED_BY',  'متأثر از',                'influenced by',    'source در شکل‌گیری از target متأثر بوده است.', 0, JSON_ARRAY('*'), JSON_ARRAY('*'), 'INFLUENCED', 1, 4),
('INFLUENCED',     'تأثیرگذار بر',           'influences',       'برعکسِ INFLUENCED_BY؛ منبع تأثیر را به مقصد می‌رساند.', 0, JSON_ARRAY('*'), JSON_ARRAY('*'), 'INFLUENCED_BY', 1, 5),
('CRITICIZES',     'نقدکننده',                'criticizes',       'source نقادِ دیدگاه‌ها یا نظام target است.', 0, JSON_ARRAY('PERSON','SCHOOL','TRADITION','THEORY','WORK'), JSON_ARRAY('PERSON','SCHOOL','TRADITION','THEORY','PARADIGM','WORK'), 'CRITICIZED_BY', 1, 6),
('EXTENDS',        'توسعه‌دهنده',             'extends',          'source، target را گسترش می‌دهد.', 0, JSON_ARRAY('THEORY','MODEL','FRAMEWORK','TRADITION'), JSON_ARRAY('THEORY','MODEL','FRAMEWORK','TRADITION'), 'EXTENDED_BY', 0, 7),
('CONTRADICTS',    'متناقض با',               'contradicts',      'مغایرت و تضاد مفهومی مستند بین دو دیدگاه.', 1, JSON_ARRAY('*'), JSON_ARRAY('*'), NULL, 1, 8),
('RELATED_TO',     'مرتبط با',                'related to',       'رابطه‌ی عمومی؛ وقتی نوع دقیق‌تر مشخص نیست.', 1, JSON_ARRAY('*'), JSON_ARRAY('*'), NULL, 0, 9),
('APPLIES_TO',     'کاربرد در',              'applies to',       'کاربرد source در حوزه/حالت target.', 0, JSON_ARRAY('*'), JSON_ARRAY('*'), 'HAS_APPLICATION', 0, 10),
('USES',           'استفاده می‌کند از',       'uses',             'source در اجرا از target بهره می‌برد.', 0, JSON_ARRAY('*'), JSON_ARRAY('*'), 'USED_BY', 0, 11),
('MEASURES',       'اندازه‌گیری می‌کند',     'measures',         'source سازه یا کمیتی را اندازه‌گیری می‌کند.', 0, JSON_ARRAY('*'), JSON_ARRAY('*'), 'MEASURED_BY', 0, 12),
('ANALYZES',       'تحلیل می‌کند',            'analyzes',         'source نوع داده یا مصادقی را تحلیل می‌کند.', 0, JSON_ARRAY('*'), JSON_ARRAY('*'), 'ANALYZED_BY', 0, 13),
('COLLECTS',       'گردآوری می‌کند',         'collects',         'source داده‌ای از نوع target را گردآوری می‌کند.', 0, JSON_ARRAY('*'), JSON_ARRAY('*'), 'COLLECTED', 0, 14),
('DEVELOPED_BY',   'توسعه‌یافته توسط',       'developed by',     'source توسط شخص/مجموعه‌ی target توسعه یافته.', 0, JSON_ARRAY('*'), JSON_ARRAY('PERSON'), 'DEVELOPED', 1, 15),
('PROPOSED_BY',    'پیشنهادشده توسط',        'proposed by',      'نظریه/مدل/روشِ source توسط شخص target پیشنهاد شده.', 0, JSON_ARRAY('*'), JSON_ARRAY('PERSON'), 'PROPOSED', 1, 16),
('OPERATIONALIZES','عملیاتی‌سازی می‌کند',    'operationalizes',  'source، مفهوم/نظریه‌ی target را به اندازه‌های قابل اجرا تبدیل می‌کند.', 0, JSON_ARRAY('*'), JSON_ARRAY('*'), 'OPERATIONALIZED_BY', 0, 17),
('TESTS',          'آزمون می‌کند',            'tests',            'روش/طرحِ source برای آزمون نظریه‌ی target.', 0, JSON_ARRAY('*'), JSON_ARRAY('*'), 'TESTED_BY', 0, 18),
('DERIVED_FROM',   'برگرفته از',              'derived from',     'source از target استنباط یا مشتق شده است.', 0, JSON_ARRAY('*'), JSON_ARRAY('*'), 'SOURCE_OF_DERIVATION', 0, 19),
('COMPARED_WITH',  'قابل مقایسه با',          'compared with',    'دو موجودیت هم‌سطح برای مقایسه و تقابل علمی.', 1, JSON_ARRAY('*'), JSON_ARRAY('*'), NULL, 0, 20),
-- روابط افزوده‌شده برای هستی‌شناسی کامل (canonical + معکوس)
('AUTHORED_BY',    'تألیف‌شده توسط',         'authored by',      'رابطه‌ی اثر/منبع و مؤلف.', 0, JSON_ARRAY('WORK'), JSON_ARRAY('PERSON'), 'AUTHORED', 1, 21),
('EDITED_BY',      'ویرایش‌شده توسط',       'edited by',        'ویراستار اثر.', 0, JSON_ARRAY('WORK'), JSON_ARRAY('PERSON'), 'EDITED', 0, 22),
('TRANSLATED_BY',  'ترجمه‌شده توسط',         'translated by',    'مترجم اثر/منبع.', 0, JSON_ARRAY('WORK'), JSON_ARRAY('PERSON'), 'TRANSLATED', 0, 23),
('PUBLISHED_BY',   'انتشارشده توسط',        'published by',     'ناشر اثر/منبع (نهاد یا شخص).', 0, JSON_ARRAY('WORK'), JSON_ARRAY('*'), 'PUBLISHED', 0, 24),
('CITES',          'استناد به',              'cites',            'source به target ارجاع دارد.', 0, JSON_ARRAY('WORK'), JSON_ARRAY('WORK'), 'CITED_BY', 0, 25),
('TESTED_IN',      'آزمون‌شده در',           'tested in',        'نظریه/فرضیه در یک مطالعه آزمون شده است.', 0, JSON_ARRAY('THEORY','HYPOTHESIS','PROPOSITION'), JSON_ARRAY('RESEARCH_STUDY'), 'TESTED_IN', 0, 26),
('SUPPORTED_BY',   'پشتیبانی‌شده توسط',     'supported by',     'ادعا/نظریه با شاهد/یافته/منبع پشتیبانی می‌شود.', 0, JSON_ARRAY('*'), JSON_ARRAY('FINDING','WORK'), 'SUPPORTS', 0, 27),
('CHALLENGED_BY',  'به چالش کشیده‌شده توسط', 'challenged by',    'ادعا/نظریه با یافته/شاهد به چالش کشیده شده.', 0, JSON_ARRAY('*'), JSON_ARRAY('FINDING'), 'CHALLENGES', 1, 28),
('REFUTED_BY',     'ردشده توسط',            'refuted by',       'ادعا/فرضیه توسط یافته/شاهد رد شده است.', 0, JSON_ARRAY('*'), JSON_ARRAY('FINDING'), 'REFUTES', 1, 29),
('BASED_ON',       'بر پایه‌ی',              'based on',         'یافته/تحلیل بر داده/شاهد/منبع استوار است.', 0, JSON_ARRAY('FINDING','ANALYSIS','RESEARCH_STUDY'), JSON_ARRAY('DATASET','WORK'), 'BASIS_FOR', 0, 30),
('PRODUCED_BY',    'حاصل از',                'produced by',      'یافته از یک مطالعه حاصل شده است.', 0, JSON_ARRAY('FINDING'), JSON_ARRAY('RESEARCH_STUDY'), 'PRODUCES', 0, 31),
('REPORTED_IN',    'گزارش‌شده در',           'reported in',      'مطالعه/یافته در یک اثر گزارش شده است.', 0, JSON_ARRAY('RESEARCH_STUDY','FINDING'), JSON_ARRAY('WORK'), 'REPORTS', 0, 32),
('CONDUCTED_BY',   'انجام‌شده توسط',        'conducted by',     'مطالعه توسط شخص/گروه/نهاد انجام شده است.', 0, JSON_ARRAY('RESEARCH_STUDY'), JSON_ARRAY('PERSON'), 'CONDUCTED', 0, 33),
('ADDRESSES',      'در پاسخ به',             'addresses',        'مطالعه/پرسش یک مسئله را هدف قرار می‌دهد.', 0, JSON_ARRAY('RESEARCH_STUDY','RESEARCH_QUESTION'), JSON_ARRAY('RESEARCH_PROBLEM'), 'ADDRESSED_BY', 0, 34),
('ANSWERED_BY',    'پاسخ‌داده‌شده توسط',     'answered by',      'پرسش پژوهش توسط مطالعه/یافته پاسخ شده است.', 0, JSON_ARRAY('RESEARCH_QUESTION'), JSON_ARRAY('RESEARCH_STUDY','FINDING'), 'ANSWERS', 0, 35),
('HAS_SUBFIELD',   'دارای حوزه تخصصی',       'has subfield',     'رشته/حوزه دارای زیرحوزه است.', 0, JSON_ARRAY('DISCIPLINE','SUBFIELD'), JSON_ARRAY('SUBFIELD'), 'PART_OF', 0, 36),
('HAS_PARTICIPANT','دارای شرکت‌کننده',       'has participant',  'طرفین/مشارکت‌کنندگان یک مناقشه.', 0, JSON_ARRAY('DISPUTE'), JSON_ARRAY('PERSON','SCHOOL','THEORY','PARADIGM'), 'PARTICIPATES_IN', 0, 37),
('CONCERNS',       'درباره‌ی',                'concerns',         'موضوع/مفهوم مورد مناقشه.', 0, JSON_ARRAY('DISPUTE'), JSON_ARRAY('CONCEPT','PROPOSITION','THEORY'), NULL, 0, 38),
('EXTRACTED_FROM', 'استخراج‌شده از',        'extracted from',   'شاهد از منبع/اثر/مجموعه‌داده استخراج شده است.', 0, JSON_ARRAY('*'), JSON_ARRAY('WORK','DATASET'), 'HAS_EXTRACTED_EVIDENCE', 0, 39),
('VERIFIED_BY',    'تأییدشده توسط',          'verified by',      'تأییدکننده‌ی ادعا/رابطه/شاهد.', 0, JSON_ARRAY('*'), JSON_ARRAY('PERSON'), 'VERIFIED', 0, 40),
('ALTERNATIVE_TO', 'جایگزینِ',               'alternative to',   'دو گزینه‌ی قابل جایگزینی (نرم‌افزار/روش/ابزار).', 1, JSON_ARRAY('*'), JSON_ARRAY('*'), NULL, 0, 41),
('SUPERSEDES',     'جانشینِ',               'supersedes',       'نسخه/موجودیت جدید، قبلی را جانشینی می‌کند.', 0, JSON_ARRAY('*'), JSON_ARRAY('*'), 'SUPERSEDED_BY', 0, 42),
('REPLACED_BY',    'جایگزین‌شده توسط',       'replaced by',      'پارادایم/نظریه قدیمی جایگزین شده است.', 0, JSON_ARRAY('PARADIGM','THEORY'), JSON_ARRAY('PARADIGM','THEORY'), 'REPLACES', 0, 43),
('TRANSLATION_OF', 'ترجمه‌ی',                'translation of',   'ترجمه‌ی یک اثر/منبع.', 0, JSON_ARRAY('WORK'), JSON_ARRAY('WORK'), 'HAS_TRANSLATION', 0, 44),
('EDITION_OF',     'ویراسته‌ی',              'edition of',       'ویراسته‌ی یک اثر.', 0, JSON_ARRAY('WORK'), JSON_ARRAY('WORK'), 'HAS_EDITION', 0, 45),
('JUSTIFIED_BY',   'توجیه‌شده توسط',         'justified by',     'روش/طرح توسط روش‌شناسی توجیه شده است.', 0, JSON_ARRAY('METHOD','DESIGN'), JSON_ARRAY('METHODOLOGY'), 'JUSTIFIES', 0, 46),
('ALIGNED_WITH',   'هم‌راستا با',            'aligned with',     'سازگاری روش/رویکرد با رویکرد/روش‌شناسی.', 1, JSON_ARRAY('*'), JSON_ARRAY('*'), NULL, 0, 47),
('IMPLEMENTED_THROUGH','اجراشده از طریق',    'implemented through','روش از طریق فن/طرح اجرا می‌شود.', 0, JSON_ARRAY('METHOD'), JSON_ARRAY('TECHNIQUE','DESIGN'), 'IMPLEMENTS', 0, 48),
('SPECIFIED_BY',   'مشخص‌شده توسط',          'specified by',     'روش در یک طرح مشخص شده است.', 0, JSON_ARRAY('METHOD'), JSON_ARRAY('DESIGN'), 'SPECIFIES', 0, 49),
('GOVERNS',        'ناظر بر',                'governs',          'پروتکل/اخلاق بر مطالعه/فن/تحلیل نظارت دارد.', 0, JSON_ARRAY('PROTOCOL','ETHICS'), JSON_ARRAY('RESEARCH_STUDY','TECHNIQUE','ANALYSIS','DESIGN'), 'GOVERNED_BY', 0, 50),
('FORMULATED_IN',  'صورت‌بندی‌شده در',       'formulated in',    'نظریه/قانون در یک اثر صورت‌بندی شده است.', 0, JSON_ARRAY('THEORY','LAW'), JSON_ARRAY('WORK'), NULL, 1, 51),
('FORMULATED_BY',  'صورت‌بندی‌شده توسط',     'formulated by',    'قانون علمی توسط شخص صورت‌بندی شده است.', 0, JSON_ARRAY('LAW'), JSON_ARRAY('PERSON'), 'FORMULATED', 1, 52),
('HAS_PROPOSITION','دارای گزاره',           'has proposition',  'نظریه دارای گزاره‌های تشکیل‌دهنده است.', 0, JSON_ARRAY('THEORY'), JSON_ARRAY('PROPOSITION'), 'PROPOSITION_OF', 0, 53),
('USES_CONCEPT',   'از مفهوم استفاده می‌کند','uses concept',     'نظریه/مدل/چارچوب روی مفاهیمی استوار است.', 0, JSON_ARRAY('THEORY','MODEL','FRAMEWORK'), JSON_ARRAY('CONCEPT'), NULL, 0, 54),
('USES_VARIABLE',  'از متغیر استفاده می‌کند','uses variable',    'فرضیه/مطالعه بر متغیرهایی استوار است.', 0, JSON_ARRAY('HYPOTHESIS','RESEARCH_STUDY'), JSON_ARRAY('VARIABLE'), NULL, 0, 55),
('ABOUT',          'درباره‌ی',                'about',            'گزاره/پرسش درباره‌ی مفهوم/متغیر/سازه است.', 0, JSON_ARRAY('PROPOSITION','RESEARCH_QUESTION'), JSON_ARRAY('CONCEPT','VARIABLE','CONSTRUCT'), NULL, 0, 56),
('INDICATES',      'سنجه‌ی',                  'indicates',        'شاخص، سازه/مفهومی را سنجه می‌کند.', 0, JSON_ARRAY('INDICATOR'), JSON_ARRAY('CONSTRUCT','CONCEPT'), 'INDICATED_BY', 0, 57),
('AGGREGATED_INTO','تجمیع‌شده در',           'aggregated into',  'شاخص در شاخصِ کلان‌تر تجمیع می‌شود.', 0, JSON_ARRAY('INDICATOR'), JSON_ARRAY('INDICATOR'), 'AGGREGATES', 0, 58),
('HAS_DIMENSION',  'دارای بُعد',             'has dimension',    'سازه/ابزار/مدل دارای بُعد/جمله است.', 0, JSON_ARRAY('CONSTRUCT','INSTRUMENT','MODEL'), JSON_ARRAY('CONSTRUCT','CONCEPT'), 'DIMENSION_OF', 0, 59),
('VALIDATED_IN',   'اعتبارسنجی‌شده در',      'validated in',     'ابزار/مدل در یک مطالعه اعتبارسنجی شده است.', 0, JSON_ARRAY('INSTRUMENT','MODEL'), JSON_ARRAY('RESEARCH_STUDY'), NULL, 0, 60),
('VALIDATED_BY',   'تأییدشده توسط (یافته)',  'validated by',     'مدل/نظریه با مطالعه/شاهد تأیید شده است.', 0, JSON_ARRAY('MODEL','THEORY'), JSON_ARRAY('RESEARCH_STUDY'), 'VALIDATES', 0, 61),
('APPLIED_IN',     'به‌کاررفته در',          'applied in',       'مدل/چارچوب/نظریه در حوزه/مطالعه به کار رفته است.', 0, JSON_ARRAY('MODEL','FRAMEWORK','THEORY'), JSON_ARRAY('SUBFIELD','RESEARCH_STUDY'), NULL, 0, 62),
('ESTIMATES',      'برآورد می‌کند',          'estimates',        'روش تحلیل، متغیر/سازه‌ای را برآورد می‌کند.', 0, JSON_ARRAY('ANALYSIS'), JSON_ARRAY('VARIABLE','CONSTRUCT'), 'ESTIMATED_BY', 0, 63),
('ANALYZED_IN',    'تحلیل‌شده در',           'analyzed in',      'مجموعه‌داده در تحلیل/مطالعه‌ای پردازش شده است.', 0, JSON_ARRAY('DATASET'), JSON_ARRAY('ANALYSIS','RESEARCH_STUDY'), 'ANALYZES', 0, 64),
('COLLECTED_USING','گردآوری‌شده با',         'collected using',  'داده/مطالعه با فن/ابزار/پروتکل گردآوری شده است.', 0, JSON_ARRAY('DATASET','RESEARCH_STUDY'), JSON_ARRAY('TECHNIQUE','INSTRUMENT','PROTOCOL'), 'USED_TO_COLLECT', 0, 65),
('CONTAINS_VARIABLE','دارای متغیر',         'contains variable',  'مجموعه‌داده متغیرهایی را در بر دارد.', 0, JSON_ARRAY('DATASET'), JSON_ARRAY('VARIABLE'), 'VARIABLE_IN', 0, 66),
('DOCUMENTED_BY',  'مستندشده توسط',         'documented by',    'مجموعه‌داده در کدبوک/اثری مستند شده است.', 0, JSON_ARRAY('DATASET'), JSON_ARRAY('WORK'), 'DOCUMENTS', 0, 67),
('INCLUDED_IN',    'شامل‌شده در',            'included in',      'متغیر در یک مجموعه‌داده موجود است.', 0, JSON_ARRAY('VARIABLE'), JSON_ARRAY('DATASET'), 'CONTAINS', 0, 68),
('USED_IN',        'به‌کاررفته در (مطالعه)', 'used in',          'ابزار/تحلیل/نرم‌افزار در یک مطالعه به کار رفته است.', 0, JSON_ARRAY('INSTRUMENT','ANALYSIS','SOFTWARE'), JSON_ARRAY('RESEARCH_STUDY'), 'USES', 0, 69),
('MEMBER_OF',      'عضوِ',                   'member of',        'شخص عضو گروه/نهاد/مکتب است.', 0, JSON_ARRAY('PERSON'), JSON_ARRAY('SCHOOL'), 'MEMBERS', 0, 70),
('REPLICATES',     'تکرارِ',                 'replicates',       'مطالعه‌ای، مطالعه‌ی دیگری را تکرار کرده است.', 0, JSON_ARRAY('RESEARCH_STUDY'), JSON_ARRAY('RESEARCH_STUDY'), 'REPLICATED_BY', 0, 71),
('INTERPRETED_WITHIN','تفسیرشده در',        'interpreted within','پارادایم در سنتی تفسیر می‌شود.', 0, JSON_ARRAY('PARADIGM'), JSON_ARRAY('TRADITION'), NULL, 0, 72),
('TRANSMITTED_THROUGH','انتقال‌یافته از طریق','transmitted through','سنت از طریق شخص/اثر منتقل شده است.', 0, JSON_ARRAY('TRADITION'), JSON_ARRAY('PERSON','WORK'), NULL, 0, 73),
('HAS_BRANCH',     'دارای شاخه',             'has branch',       'سنت/مکتب دارای شاخه است.', 0, JSON_ARRAY('TRADITION','SCHOOL'), JSON_ARRAY('TRADITION','SCHOOL'), 'BRANCH_OF', 0, 74),
('STUDIES',        'مطالعهِ',                'studies',          'حوزه تخصصی مفاهیم/نظریه‌هایی را مطالعه می‌کند.', 0, JSON_ARRAY('SUBFIELD'), JSON_ARRAY('CONCEPT','THEORY'), 'STUDIED_IN', 0, 75),
('HAS_RESEARCH_TOPIC','دارای موضوع پژوهش',  'has research topic','رشته/حوزه دارای موضوع پژوهش است.', 0, JSON_ARRAY('SUBFIELD','DISCIPLINE'), JSON_ARRAY('RESEARCH_PROBLEM'), NULL, 0, 76),
('MOTIVATED_BY',   'انگیزه‌ی‌شده توسط',       'motivated by',     'مسئله پژوهش با شاهد/یافته/مناقشه انگیزه گرفته است.', 0, JSON_ARRAY('RESEARCH_PROBLEM'), JSON_ARRAY('DISPUTE'), 'MOTIVATES', 0, 77),
('REQUIRES',       'نیازمندِ',               'requires',         'پرسش/مسئله به روش/طرح نیاز دارد.', 0, JSON_ARRAY('RESEARCH_QUESTION','RESEARCH_PROBLEM'), JSON_ARRAY('METHOD','DESIGN'), 'REQUIRED_BY', 0, 78),
('GUIDED_BY',      'هدایت‌شده توسط',         'guided by',        'پرسش/مطالعه با نظریه/چارچوب هدایت می‌شود.', 0, JSON_ARRAY('RESEARCH_QUESTION','RESEARCH_STUDY'), JSON_ARRAY('THEORY','FRAMEWORK'), 'GUIDES', 0, 79),
('CONTRASTS_WITH', 'در تقابل با',            'contrasts with',   'مفهوم/رویکرد در تقابل معنایی با دیگری است.', 1, JSON_ARRAY('CONCEPT','APPROACH'), JSON_ARRAY('CONCEPT','APPROACH'), NULL, 0, 80),
('DEFINED_IN',     'تعریف‌شده در',           'defined in',       'مفهوم/سازه در یک اثر تعریف شده است.', 0, JSON_ARRAY('CONCEPT','CONSTRUCT'), JSON_ARRAY('WORK'), NULL, 1, 81);

-- 5.4) 13 ابعاد فاکت
INSERT INTO kb_facet_dimensions (code, label_fa, label_en, description, value_kind, sort_order) VALUES
('discipline',            'رشته علمی',            'Discipline',            'رشته یا رشته‌های مرتبط.', 'ENTITY_REF', 1),
('subfield',              'حوزه تخصصی',           'Subfield',              'حوزه یا حوزه‌های تخصصی.', 'ENTITY_REF', 2),
('time_frame',            'دوره زمانی',           'Time Frame',            'بازه تاریخی/زمانی موضوع.', 'TIME_PERIOD', 3),
('geographic_region',     'منطقه جغرافیایی',      'Geographic Region',      'منطقه جغرافیایی ظهور/کاربرد.', 'STRING', 4),
('approach',              'رویکرد',               'Approach',              'جهت‌گیری پژوهشی/تحلیلی.', 'STRING', 5),
('epistemology',          'معرفت‌شناسی',          'Epistemology',           'موضع درباره امکان و ماهیت شناخت.', 'STRING', 6),
('ontology',              'هستی‌شناسی',           'Ontology',               'موضع درباره ماهیت واقعیت.', 'STRING', 7),
('data_type',             'نوع داده',             'Data Type',              'کمّی/کیفی/متنی/تصویری/شبکه‌ای و ...', 'STRING', 8),
('theoretical_tradition', 'سنت نظری',             'Theoretical Tradition',  'سنت یا سنت‌های فکری مرتبط.', 'ENTITY_REF', 9),
('research_context',      'زمینه پژوهش',          'Research Context',       'زمینه موضوعی/اجتماعی/نهادی.', 'STRING', 10),
('analysis_scale',        'مقیاس تحلیل',          'Analysis Scale',         'خرد/میانه/کلان (فاکتِ بهای قدیمی — برای seed).', 'STRING', 11),
('application_domain',    'حوزه کاربرد',          'Application Domain',     'رسانه/سیاست/سازمان/سلامت (فاکتِ بهای قدیمی — برای seed).', 'STRING', 12),
('qualifies_for',         'مناسب برای',           'Qualifies For',          'کاربردهای اصلی (فاکتِ بهای قدیمی — برای seed).', 'STRING', 13);

-- 5.5) واژگان کنترل‌شده‌ی پایه (فقط فاکت‌های STRING/TIME_PERIOD)
--     فاکت‌های ENTITY_REF (discipline/subfield/theoretical_tradition) بعد از seedِ موجودیت‌ها پر می‌شوند.
INSERT INTO kb_facet_values (facet_code, code, label_fa, label_en, definition, sort_order) VALUES
-- data_type
('data_type','QUANTITATIVE','کمّی','Quantitative','داده‌های عددی یا قابل تحلیل کمّی',1),
('data_type','QUALITATIVE','کیفی','Qualitative','داده‌های متنی، گفتاری، مشاهده‌ای یا معنایی',2),
('data_type','MIXED','آمیخته','Mixed','ترکیب نظام‌مند کمّی و کیفی',3),
('data_type','TEXTUAL','متنی','Textual',NULL,4),
('data_type','VISUAL','دیداری','Visual',NULL,5),
('data_type','AUDIO','صوتی','Audio',NULL,6),
('data_type','VIDEO','ویدئویی','Video',NULL,7),
('data_type','NETWORK','شبکه‌ای','Network',NULL,8),
('data_type','SPATIAL','مکانی','Spatial',NULL,9),
('data_type','ADMINISTRATIVE','ثبتی/اداری','Administrative',NULL,10),
('data_type','SENSOR','حسگر','Sensor',NULL,11),
('data_type','OTHER','سایر','Other',NULL,12),
-- approach
('approach','QUANTITATIVE','کمّی','Quantitative',NULL,1),
('approach','QUALITATIVE','کیفی','Qualitative',NULL,2),
('approach','MIXED','آمیخته','Mixed',NULL,3),
('approach','COMPUTATIONAL','محاسباتی','Computational',NULL,4),
('approach','CRITICAL','انتقادی','Critical',NULL,5),
('approach','PARTICIPATORY','مشارکتی','Participatory',NULL,6),
('approach','INTERPRETIVE','تفسیری','Interpretive',NULL,7),
-- epistemology
('epistemology','POSITIVIST','اثبات‌گرا','Positivist',NULL,1),
('epistemology','INTERPRETIVIST','تفسیری','Interpretivist',NULL,2),
('epistemology','CONSTRUCTIVIST','برساخت‌گرا','Constructivist',NULL,3),
('epistemology','CRITICAL','انتقادی','Critical',NULL,4),
('epistemology','PRAGMATIST','پراگماتیست','Pragmatist',NULL,5),
-- ontology
('ontology','OBJECTIVIST','واقع‌گرا/عینی','Objectivist',NULL,1),
('ontology','CONSTRUCTIVIST','برساخت‌گرا','Constructivist',NULL,2),
('ontology','RELATIVIST','نسبیت‌گرا','Relativist',NULL,3),
('ontology','IDEALIST','ایده‌آلیست','Idealist',NULL,4),
-- research_context
('research_context','MEDIA','رسانه','Media',NULL,1),
('research_context','POLICY','سیاست','Policy',NULL,2),
('research_context','ORGANIZATION','سازمان','Organization',NULL,3),
('research_context','HEALTH','سلامت','Health',NULL,4),
('research_context','EDUCATION','آموزش','Education',NULL,5),
('research_context','DEVELOPMENT','توسعه','Development',NULL,6),
('research_context','DIGITAL','دیجیتال','Digital',NULL,7),
('research_context','PLATFORM','پلتفرمی','Platform',NULL,8),
-- geographic_region
('geographic_region','IRAN','ایران','Iran',NULL,1),
('geographic_region','MIDDLE_EAST','خاورمیانه','Middle East',NULL,2),
('geographic_region','WESTERN','غرب','Western',NULL,3),
('geographic_region','ASIA','آسیا','Asia',NULL,4),
('geographic_region','EUROPE','اروپا','Europe',NULL,5),
('geographic_region','NORTH_AMERICA','شمال آمریکا','North America',NULL,6),
('geographic_region','GLOBAL','جهانی','Global',NULL,7),
-- time_frame (TIME_PERIOD)
('time_frame','PRE_MASS_MEDIA','پیش از رسانه‌های توده‌ای','Pre-mass media',NULL,1),
('time_frame','MASS_MEDIA','عصر رسانه‌های توده‌ای','Mass media era',NULL,2),
('time_frame','DIGITAL','دیجیتال','Digital',NULL,3),
('time_frame','PLATFORM','پلتفرمی','Platform',NULL,4),
-- analysis_scale (legacy)
('analysis_scale','MICRO','خرد/بین‌فردی','Micro',NULL,1),
('analysis_scale','MESO','میانه/سازمانی','Meso',NULL,2),
('analysis_scale','MACRO','کلان/جامعه‌شناختی','Macro',NULL,3),
-- application_domain (legacy)
('application_domain','MEDIA','رسانه','Media',NULL,1),
('application_domain','POLITICS','سیاست','Politics',NULL,2),
('application_domain','ORGANIZATION','سازمان','Organization',NULL,3),
('application_domain','HEALTH','سلامت','Health',NULL,4),
('application_domain','EDUCATION','آموزش','Education',NULL,5),
('application_domain','DEVELOPMENT','توسعه','Development',NULL,6),
-- qualifies_for (legacy)
('qualifies_for','QUANTITATIVE','کمّی','Quantitative',NULL,1),
('qualifies_for','QUALITATIVE','کیفی','Qualitative',NULL,2),
('qualifies_for','MIXED','آمیخته','Mixed',NULL,3),
('qualifies_for','ALL','همه','All',NULL,4);

-- ============================================================================
-- پایان. دیتابیس خالیِ فاینال آماده است:
--   15 جدول + registriesِ پر (8 خانواده / 36 نوع / 81 رابطه / 13 فاکت / واژگان کنترل‌شده)
--   هیچ داده‌ی محتوایی (موجودیت/رابطه/فاکتِ محتوایی/لینک) وارد نشده است.
-- ============================================================================

SET FOREIGN_KEY_CHECKS=1;
