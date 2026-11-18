-- ============================================================================
-- resaname_v2 — طبقه‌بندی 33 نوع محتوا در ۶ دسته (content_type_taxonomy)
-- تاریخ: 2026-11-10
-- کاربرد: مرجع رسمی برای contents.content_type — هر یک از 731 کارت باید
--          دقیقاً یکی از این 33 نوع را داشته باشد.
-- ============================================================================
USE resaname_v2;

CREATE TABLE IF NOT EXISTS `content_type_taxonomy` (
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

-- ---------------------------------------------------------------------------
-- دسته ۱: ساختارهای نظری و تبیینی (6 نوع)
-- ---------------------------------------------------------------------------
INSERT INTO content_type_taxonomy
  (category_no, category_key, category_fa, category_en, type_key, type_fa, type_en, sort_order) VALUES
(1, 'a', 'ساختارهای نظری و تبیینی', 'Theoretical & Explanatory Structures', 'theory',   'نظریه',            'Theory',                1),
(1, 'a', 'ساختارهای نظری و تبیینی', 'Theoretical & Explanatory Structures', 'model',    'مدل',              'Model',               2),
(1, 'a', 'ساختارهای نظری و تبیینی', 'Theoretical & Explanatory Structures', 'framework','چارچوب نظری',      'Theoretical Framework', 3),
(1, 'a', 'ساختارهای نظری و تبیینی', 'Theoretical & Explanatory Structures', 'paradigm', 'پارادایم',          'Paradigm',            4),
(1, 'a', 'ساختارهای نظری و تبیینی', 'Theoretical & Explanatory Structures', 'hypothesis','فرضیه',            'Hypothesis',          5),
(1, 'a', 'ساختارهای نظری و تبیینی', 'Theoretical & Explanatory Structures', 'law',      'قانون علمی',        'Law',                 6);

-- ---------------------------------------------------------------------------
-- دسته ۲: جریان‌ها و سنت‌های فکری (5 نوع)
-- ---------------------------------------------------------------------------
INSERT INTO content_type_taxonomy
  (category_no, category_key, category_fa, category_en, type_key, type_fa, type_en, sort_order) VALUES
(2, 'b', 'جریان‌ها و سنت‌های فکری', 'Intellectual Movements & Traditions', 'school',  'مکتب',            'School',                  1),
(2, 'b', 'جریان‌ها و سنت‌های فکری', 'Intellectual Movements & Traditions', 'movement','جریان فکری',       'Intellectual Movement', 2),
(2, 'b', 'جریان‌ها و سنت‌های فکری', 'Intellectual Movements & Traditions', 'research_tradition', 'سنت پژوهشی',   'Research Tradition',    3),
(2, 'b', 'جریان‌ها و سنت‌های فکری', 'Intellectual Movements & Traditions', 'discourse','گفتمان',           'Discourse',             4),
(2, 'b', 'جریان‌ها و سنت‌های فکری', 'Intellectual Movements & Traditions', 'ideology', 'ایدئولوژی',         'Ideology',                5);

-- ---------------------------------------------------------------------------
-- دسته ۳: قلمروهای دانش (4 نوع)
-- ---------------------------------------------------------------------------
INSERT INTO content_type_taxonomy
  (category_no, category_key, category_fa, category_en, type_key, type_fa, type_en, sort_order) VALUES
(3, 'c', 'قلمروهای دانش', 'Domains of Knowledge', 'field',           'حوزه مطالعاتی',      'Field of Study',         1),
(3, 'c', 'قلمروهای دانش', 'Domains of Knowledge', 'discipline',      'رشته علمی',           'Discipline',             2),
(3, 'c', 'قلمروهای دانش', 'Domains of Knowledge', 'subdiscipline',   'زیررشته',              'Subdiscipline',          3),
(3, 'c', 'قلمروهای دانش', 'Domains of Knowledge', 'interdisciplinary','حوزه میان‌رشته‌ای',   'Interdisciplinary Field', 4);

-- ---------------------------------------------------------------------------
-- دسته ۴: مفاهیم و پدیده‌ها (6 نوع)
-- ---------------------------------------------------------------------------
INSERT INTO content_type_taxonomy
  (category_no, category_key, category_fa, category_en, type_key, type_fa, type_en, sort_order) VALUES
(4, 'd', 'مفاهیم و پدیده‌ها', 'Concepts & Phenomena', 'concept',    'مفهوم',   'Concept',     1),
(4, 'd', 'مفاهیم و پدیده‌ها', 'Concepts & Phenomena', 'construct',  'سازه',    'Construct',   2),
(4, 'd', 'مفاهیم و پدیده‌ها', 'Concepts & Phenomena', 'effect',     'اثر',     'Effect',      3),
(4, 'd', 'مفاهیم و پدیده‌ها', 'Concepts & Phenomena', 'phenomenon', 'پدیده',  'Phenomenon',  4),
(4, 'd', 'مفاهیم و پدیده‌ها', 'Concepts & Phenomena', 'process',    'فرایند',  'Process',     5),
(4, 'd', 'مفاهیم و پدیده‌ها', 'Concepts & Phenomena', 'principle',  'اصل',     'Principle',   6);

-- ---------------------------------------------------------------------------
-- دسته ۵: ابزارهای علمی و پژوهشی (7 نوع)
-- ---------------------------------------------------------------------------
INSERT INTO content_type_taxonomy
  (category_no, category_key, category_fa, category_en, type_key, type_fa, type_en, sort_order) VALUES
(5, 'e', 'ابزارهای علمی و پژوهشی', 'Scientific & Research Tools', 'method',       'روش پژوهش',   'Research Method', 1),
(5, 'e', 'ابزارهای علمی و پژوهشی', 'Scientific & Research Tools', 'methodology',  'روش‌شناسی',   'Methodology',     2),
(5, 'e', 'ابزارهای علمی و پژوهشی', 'Scientific & Research Tools', 'technique',    'تکنیک',        'Technique',       3),
(5, 'e', 'ابزارهای علمی و پژوهشی', 'Scientific & Research Tools', 'tool',         'ابزار',        'Tool',            4),
(5, 'e', 'ابزارهای علمی و پژوهشی', 'Scientific & Research Tools', 'indicator',    'شاخص',         'Indicator',       5),
(5, 'e', 'ابزارهای علمی و پژوهشی', 'Scientific & Research Tools', 'scale',        'مقیاس',        'Scale',           6),
(5, 'e', 'ابزارهای علمی و پژوهشی', 'Scientific & Research Tools', 'measure',      'سنجه',         'Measure',         7);

-- ---------------------------------------------------------------------------
-- دسته ۶: ساختارهای کاربردی (5 نوع)
-- ---------------------------------------------------------------------------
INSERT INTO content_type_taxonomy
  (category_no, category_key, category_fa, category_en, type_key, type_fa, type_en, sort_order) VALUES
(6, 'f', 'ساختارهای کاربردی', 'Applied Structures', 'strategy',              'استراتژی',        'Strategy',               1),
(6, 'f', 'ساختارهای کاربردی', 'Applied Structures', 'pattern',               'الگو',            'Pattern',                2),
(6, 'f', 'ساختارهای کاربردی', 'Applied Structures', 'operational_framework', 'چارچوب اجرایی',    'Operational Framework',  3),
(6, 'f', 'ساختارهای کاربردی', 'Applied Structures', 'standard',              'استاندارد',       'Standard',               4),
(6, 'f', 'ساختارهای کاربردی', 'Applied Structures', 'guideline',             'دستورالعمل',       'Guideline',              5);
