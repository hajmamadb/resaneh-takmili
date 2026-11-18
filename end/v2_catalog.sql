-- ============================================================================
-- resaname_v2 — کالکشن کلیدهای بخش (section_catalog)
-- 18 بخش نظریه (4 گروه) + 20 بخش نظریه‌پرداز (5 گروه)
-- ============================================================================
USE resaname_v2;

-- ---- نظریه‌ها و مدل‌ها: 18 بخش در 4 گروه ----
INSERT INTO section_catalog (content_type, group_no, group_name, section_key, section_title, importance) VALUES
('theory', 1, 'شناسنامه و معرفی',           'title',            'عنوان نظریه',            'required'),
('theory', 1, 'شناسنامه و معرفی',           'summary',          'معرفی کوتاه',             'required'),
('theory', 1, 'شناسنامه و معرفی',           'theorists',        'نظریه‌پردازان اصلی',      'required'),
('theory', 1, 'شناسنامه و معرفی',           'history',          'تاریخچه شکل‌گیری',       'required'),
('theory', 1, 'شناسنامه و معرفی',           'classification',   'حوزه علمی و طبقه‌بندی',  'required'),
('theory', 2, 'بنیان‌های نظری',             'problem',          'مسئله و پرسش اصلی',     'required'),
('theory', 2, 'بنیان‌های نظری',             'assumptions',      'مفروضات بنیادین',        'required'),
('theory', 2, 'بنیان‌های نظری',             'key_concepts',     'مفاهیم کلیدی',           'required'),
('theory', 2, 'بنیان‌های نظری',             'propositions',     'گزاره‌ها و اصول',        'required'),
('theory', 2, 'بنیان‌های نظری',             'model',            'مدل و چارچوب مفهومی',   'optional'),
('theory', 2, 'بنیان‌های نظری',             'mechanism',        'سازوکار عملکرد',         'required'),
('theory', 3, 'تبیین و ارزیابی',             'applications',     'کاربردها و مصادیق',      'required'),
('theory', 3, 'تبیین و ارزیابی',             'studies',          'مطالعات شاخص',           'optional'),
('theory', 3, 'تبیین و ارزیابی',             'evolution',        'تحولات و توسعه نظریه',   'optional'),
('theory', 3, 'تبیین و ارزیابی',             'criticism',        'نقدها و محدودیت‌ها',      'required'),
('theory', 3, 'تبیین و ارزیابی',             'related_theories', 'نظریه‌های مرتبط و رقیب', 'required'),
('theory', 4, 'منابع و پژوهش',              'references',       'منابع و مآخذ',           'required'),
('theory', 4, 'منابع و پژوهش',              'research_guide',   'راهنمای استفاده پژوهشی',  'optional');

-- ---- نظریه‌پردازان: 20 بخش در 5 گروه ----
INSERT INTO section_catalog (content_type, group_no, group_name, section_key, section_title, importance) VALUES
('theorist', 1, 'شناسنامه و هویت',          'identity',         'نام و نام خانوادگی',     'required'),
('theorist', 1, 'شناسنامه و هویت',          'vitals',           'تصویر و اطلاعات پایه',    'required'),
('theorist', 1, 'شناسنامه و هویت',          'short_intro',      'معرفی کوتاه',             'required'),
('theorist', 1, 'شناسنامه و هویت',          'specialties',      'حوزه‌های تخصصی',          'required'),
('theorist', 1, 'شناسنامه و هویت',          'affiliations',     'وابستگی‌های علمی',       'required'),
('theorist', 2, 'زندگی‌نامه و مسیر علمی',   'education',        'زندگی و تحصیلات',         'required'),
('theorist', 2, 'زندگی‌نامه و مسیر علمی',   'career',           'مسیر حرفه‌ای و دانشگاهی',  'required'),
('theorist', 2, 'زندگی‌نامه و مسیر علمی',   'context',          'زمینه تاریخی و فکری',     'required'),
('theorist', 2, 'زندگی‌نامه و مسیر علمی',   'intellectual_evolution','سیر تحول فکری',       'required'),
('theorist', 2, 'زندگی‌نامه و مسیر علمی',   'mentors_students', 'شاگردان و تأثیرگذاران',   'required'),
('theorist', 3, 'اندیشه و دستاوردها',       'theories',         'نظریه‌های ارائه‌شده',     'required'),
('theorist', 3, 'اندیشه و دستاوردها',       'key_concepts',     'مفاهیم و اصطلاحات کلیدی','required'),
('theorist', 3, 'اندیشه و دستاوردها',       'works',            'آثار و تألیفات',          'required'),
('theorist', 3, 'اندیشه و دستاوردها',       'method',           'روش و رویکرد علمی',      'required'),
('theorist', 3, 'اندیشه و دستاوردها',       'legacy',           'تأثیرگذاری و میراث',      'required'),
('theorist', 4, 'نقد و ارزیابی',             'criticisms',       'نقدهای واردشده',          'required'),
('theorist', 4, 'نقد و ارزیابی',             'responses',        'پاسخ‌ها و دفاعیات',       'required'),
('theorist', 4, 'نقد و ارزیابی',             'evaluation',       'جایگاه علمی معاصر',      'required'),
('theorist', 5, 'ارتباطات و منابع',         'network',          'شبکه ارتباطات علمی',     'required'),
('theorist', 5, 'ارتباطات و منابع',         'references',       'منابع و مآخذ',           'required');
