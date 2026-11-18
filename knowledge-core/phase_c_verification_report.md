# Phase C — Expert Verification Report

*Rasaname — دایره‌المعارف فارسی رسانه و ارتباطات · knowledge-core (audit-only, read-only)*

## خلاصه (Summary)

- **Entities:** 436 verified / 93 needs_review / 0 error (total 529)
- **Relations:** 895 verified / 177 needs_review / 0 error (total 1072)

## روش و قواعد (Method & rules)

این واحد **فقط-خواندنی** است؛ هیچ UPDATE/INSERT/DELETE/ALTER انجام نشده است. هر entity/relation بر اساس قواعد قطعی زیر دسته‌بندی می‌شود:

**Entity — `error`:** entity_type نامعتبر در `knowledge_entity_types`.
**Entity — `needs_review`:** verification_status قبلی `flagged`/`duplicate`، نام فارسی تکراری، نام انگلیسی تکراری، نام فارسی خیلی کوتاه (<3 کاراکتر)، یا abstract ضعیف (<40 کاراکتر).
**Entity — `verified`:** همه موارد دیگر.

**Relation — `error`:** endpoint یتیم (source/target بدون entity) یا relation_type نامعتبر.
**Relation — `needs_review`:** type مبهم `RELATED_TO`، confidence < 0.80، حلقه‌ی خودی (source==target)، یا description حاوی شناسه‌ی خام `kg-…`.
**Relation — `verified`:** همه موارد دیگر.

## Entities با مشکل (needs_review + error)

| id | name (fa) | name_en | entity_type | status | problem | suggestion |
|---|---|---|---|---|---|---|
| kg-analysis-centrality-analysis | تحلیل مرکزیت | Centrality Analysis | ANALYSIS | needs_review | abstract thin (37 chars < 40) | enrich the definition/abstract |
| kg-analysis-cpd | تحلیل محاسباتی گفتمان | Computational Discourse Analysis | ANALYSIS | needs_review | abstract thin (28 chars < 40) | enrich the definition/abstract |
| kg-analysis-info-diffusion | تحلیل انتشار اطلاعات | Information Diffusion Analysis | ANALYSIS | needs_review | abstract thin (33 chars < 40) | enrich the definition/abstract |
| kg-analysis-multimedia-analysis | تحلیل چندرسانه‌ای | Multimedia Analysis | ANALYSIS | needs_review | abstract thin (35 chars < 40) | enrich the definition/abstract |
| kg-analysis-network-clustering-analysis | تحلیل خوشه‌های شبکه | Network Clustering Analysis | ANALYSIS | needs_review | abstract thin (35 chars < 40) | enrich the definition/abstract |
| kg-analysis-qual-deductive-heinze | تحلیل محتوای تلخیصی (Deductive) | Deductive Content Analysis (Heinze) | ANALYSIS | needs_review | verification_status='flagged' (prior-work flag) | human re-check of this entity's content/type |
| kg-analysis-qual-interp-herm | تحلیل هرمنوتیکی | Hermeneutic Analysis | ANALYSIS | needs_review | verification_status='flagged' (prior-work flag) | human re-check of this entity's content/type |
| kg-analysis-qual-multimodal-image | تحلیل تصویر (در تحلیل چندوجهی) | Image (in Multimodal Analysis) | ANALYSIS | needs_review | abstract thin (39 chars < 40) | enrich the definition/abstract |
| kg-analysis-qual-narrative-episodes | تحلیل روایی رویدادی (Episodic) | Episodic Narrative Analysis | ANALYSIS | needs_review | verification_status='flagged' (prior-work flag) | human re-check of this entity's content/type |
| kg-analysis-qual-narrative-functionalist | تحلیل روایی کارکردی (Functionalist) | Functionalist Narrative Analysis | ANALYSIS | needs_review | verification_status='flagged' (prior-work flag) | human re-check of this entity's content/type |
| kg-analysis-qual-phen-descriptive | تحلیل پدیدارشناختی توصیفی (DIP) | Descriptive Phenomenological Analysis (DIP) | ANALYSIS | needs_review | abstract thin (39 chars < 40) | enrich the definition/abstract |
| kg-analysis-qual-semiotic-barthes | تحلیل نشانه‌شناختی بارت | Barthesian Semiotic Analysis | ANALYSIS | needs_review | verification_status='flagged' (prior-work flag) | human re-check of this entity's content/type |
| kg-analysis-qual-semiotic-peircean | تحلیل نشانه‌شناختی پیرسی | Peircean Semiotic Analysis | ANALYSIS | needs_review | verification_status='flagged' (prior-work flag) | human re-check of this entity's content/type |
| kg-analysis-qual-visual-image | تحلیل تصویر | Image Analysis | ANALYSIS | needs_review | duplicate English name 'Image Analysis' (2 entities) | merge or rename to disambiguate the duplicate |
| kg-analysis-rumor-simulation | شبیه‌سازی انتشار شایعه | Rumor Diffusion Simulation | ANALYSIS | needs_review | abstract thin (27 chars < 40) | enrich the definition/abstract |
| kg-analysis-semantic-similarity-analysis | تحلیل شباهت معنایی | Semantic Similarity Analysis | ANALYSIS | needs_review | abstract thin (36 chars < 40) | enrich the definition/abstract |
| kg-analysis-virtual-community-analysis | تحلیل جامعه‌های مجازی | Virtual Community Analysis | ANALYSIS | needs_review | abstract thin (35 chars < 40) | enrich the definition/abstract |
| kg-approach-co-created-knowledge | دانش هم‌آفرین (Co-created Knowledge) | Co-created Knowledge | APPROACH | needs_review | verification_status='flagged' (prior-work flag) | human re-check of this entity's content/type |
| kg-approach-communication-systems | نظریه ارتباطی سیستم‌ها | Communication Systems Theory | APPROACH | needs_review | verification_status='flagged' (prior-work flag) | human re-check of this entity's content/type |
| kg-approach-complementary | رویکردهای مکمل (تطبیقی، تاریخی، انتقادی، مشارکتی، طراحی‌محور، محاسباتی) | Complementary Approaches (Comparative, Historical, Critical, Participatory, Design-based, Computational) | APPROACH | needs_review | verification_status='flagged' (prior-work flag) | human re-check of this entity's content/type |
| kg-approach-critical-realism-paradigm | واقع‌گرایی انتقادی (به‌عنوان پارادایم مستقل) | Critical Realism (as Standalone Paradigm) | APPROACH | needs_review | verification_status='flagged' (prior-work flag) | human re-check of this entity's content/type |
| kg-approach-decolonization | نظریه استعمارزدایی | Decolonial Theory | APPROACH | needs_review | verification_status='flagged' (prior-work flag) | human re-check of this entity's content/type |
| kg-approach-hermeneutic-phenomenology | پدیدارشناسی هرمنوتیکی | Hermeneutic Phenomenology | APPROACH | needs_review | duplicate English name 'Hermeneutic Phenomenology' (2 entities) | merge or rename to disambiguate the duplicate |
| kg-approach-postcolonial-studies | مطالعات پسااستعماری | Postcolonial Studies | APPROACH | needs_review | duplicate Persian name 'مطالعات پسااستعماری' (2 entities); duplicate English name 'Postcolonial Studies' (2 entities) | merge or rename to disambiguate the duplicate; merge or rename to disambiguate the duplicate |
| kg-approach-social-interactionism | کنش متقابل اجتماعی | Social Interactionism | APPROACH | needs_review | verification_status='flagged' (prior-work flag) | human re-check of this entity's content/type |
| kg-approach-social-interpretation | تفسیر اجتماعی (Social Interpretation) | Social Interpretation | APPROACH | needs_review | verification_status='flagged' (prior-work flag) | human re-check of this entity's content/type |
| kg-approach-structured-action | نظریه کنش ساختاری | Structured Action Theory | APPROACH | needs_review | verification_status='flagged' (prior-work flag) | human re-check of this entity's content/type |
| kg-concept-oppositional-reading | درک مقاومتی | Oppositional Reading | CONCEPT | needs_review | verification_status='flagged' (prior-work flag) | human re-check of this entity's content/type |
| kg-design-action-research | پژوهش اقدام‌پژوهانه | Action Research | DESIGN | needs_review | duplicate English name 'Action Research' (2 entities) | merge or rename to disambiguate the duplicate |
| kg-design-design-based | پژوهش طراحی‌محور | Design-Based Research | DESIGN | needs_review | duplicate Persian name 'پژوهش طراحی‌محور' (2 entities); duplicate English name 'Design-Based Research' (2 entities) | merge or rename to disambiguate the duplicate; merge or rename to disambiguate the duplicate |
| kg-framework-media-environment | نظریه‌ی محیط رسانه‌ای | Media Environment Theory | FRAMEWORK | needs_review | verification_status='flagged' (prior-work flag) | human re-check of this entity's content/type |
| kg-framework-participatory | چارچوب مشارکتی | Participatory Framework | FRAMEWORK | needs_review | verification_status='flagged' (prior-work flag) | human re-check of this entity's content/type |
| kg-framework-qual-documentary-analysis | تحلیل اسنادی (خانواده) | Documentary Analysis (family) | FRAMEWORK | needs_review | abstract thin (36 chars < 40) | enrich the definition/abstract |
| kg-framework-saussurian-semiotics | نشانه‌شناسی سوسوری | Saussurian Semiotics | FRAMEWORK | needs_review | verification_status='flagged' (prior-work flag) | human re-check of this entity's content/type |
| kg-paradigm-pragmatism | پارادایم پراگماتیسم | Pragmatism | PARADIGM | needs_review | duplicate English name 'Pragmatism' (2 entities) | merge or rename to disambiguate the duplicate |
| kg-sampling-case-volunteer | نمونه‌گیری موردی و داوطلبانه | Case & Voluntary Sampling | SAMPLING | needs_review | abstract thin (39 chars < 40) | enrich the definition/abstract |
| kg-sampling-multiphase-stratified | نمونه‌گیری تصادفی طبقه‌ای چندمرحله‌ای | Multi-Phase Stratified Random Sampling | SAMPLING | needs_review | verification_status='flagged' (prior-work flag) | human re-check of this entity's content/type |
| kg-software-pajek | Pajek | Pajek | SOFTWARE | needs_review | abstract thin (37 chars < 40) | enrich the definition/abstract |
| kg-software-r | R | R | SOFTWARE | needs_review | verification_status='flagged' (prior-work flag); duplicate Persian name 'R' (2 entities); duplicate English name 'R' (2 entities); Persian name too short ('R') | human re-check of this entity's content/type; merge or rename to disambiguate the duplicate; merge or rename to disambiguate the duplicate; expand the name for clarity/uniqueness |
| kg-software-r-lang | R | R | SOFTWARE | needs_review | duplicate Persian name 'R' (2 entities); duplicate English name 'R' (2 entities); Persian name too short ('R') | merge or rename to disambiguate the duplicate; merge or rename to disambiguate the duplicate; expand the name for clarity/uniqueness |
| kg-software-voyant | Voyant Tools | Voyant Tools | SOFTWARE | needs_review | abstract thin (31 chars < 40) | enrich the definition/abstract |
| kg-subfield-actor-network-theory | نظریه کنشگر-شبکه | Actor-Network Theory (ANT) | THEORY | needs_review | verification_status='flagged' (prior-work flag) | human re-check of this entity's content/type |
| kg-subfield-networked-society | جامعه شبکه‌ای | Networked Society | PARADIGM | needs_review | verification_status='flagged' (prior-work flag) | human re-check of this entity's content/type |
| kg-technique-action-research | اقدام‌پژوهی | Action Research | TECHNIQUE | needs_review | duplicate English name 'Action Research' (2 entities) | merge or rename to disambiguate the duplicate |
| kg-technique-attitude-scales | مقیاس‌های نگرش | Attitude Scales | TECHNIQUE | needs_review | verification_status='flagged' (prior-work flag) | human re-check of this entity's content/type |
| kg-technique-big-data-analysis | تحلیل داده‌های بزرگ | Big Data Analysis | TECHNIQUE | needs_review | abstract thin (32 chars < 40) | enrich the definition/abstract |
| kg-technique-cohort | نسلی | Cohort Design | TECHNIQUE | needs_review | verification_status='flagged' (prior-work flag) | human re-check of this entity's content/type |
| kg-technique-correlational | همبستگی | Correlational Design | TECHNIQUE | needs_review | verification_status='flagged' (prior-work flag) | human re-check of this entity's content/type |
| kg-technique-cross-sectional | مقطعی | Cross-Sectional Design | TECHNIQUE | needs_review | verification_status='flagged' (prior-work flag); abstract thin (39 chars < 40) | human re-check of this entity's content/type; enrich the definition/abstract |
| kg-technique-descriptive | توصیفی | Descriptive Design | TECHNIQUE | needs_review | duplicate Persian name 'توصیفی' (2 entities) | merge or rename to disambiguate the duplicate |
| kg-technique-descriptive-phenomenology | توصیفی | Descriptive Phenomenology | TECHNIQUE | needs_review | duplicate Persian name 'توصیفی' (2 entities) | merge or rename to disambiguate the duplicate |
| kg-technique-design-based-research | پژوهش طراحی‌محور | Design-Based Research | TECHNIQUE | needs_review | duplicate Persian name 'پژوهش طراحی‌محور' (2 entities); duplicate English name 'Design-Based Research' (2 entities) | merge or rename to disambiguate the duplicate; merge or rename to disambiguate the duplicate |
| kg-technique-design-science | پژوهش علم طراحی | Design Science | TECHNIQUE | needs_review | abstract thin (39 chars < 40) | enrich the definition/abstract |
| kg-technique-efficiency-evaluation | ارزیابی کارایی | Efficiency Evaluation | TECHNIQUE | needs_review | verification_status='flagged' (prior-work flag); abstract thin (25 chars < 40) | human re-check of this entity's content/type; enrich the definition/abstract |
| kg-technique-hermeneutic-phenomenology | هرمنوتیکی | Hermeneutic Phenomenology | TECHNIQUE | needs_review | verification_status='flagged' (prior-work flag); duplicate English name 'Hermeneutic Phenomenology' (2 entities) | human re-check of this entity's content/type; merge or rename to disambiguate the duplicate |
| kg-technique-historical-analysis | تحلیل تاریخی | Historical Analysis | TECHNIQUE | needs_review | abstract thin (39 chars < 40) | enrich the definition/abstract |
| kg-technique-historical-comparative | تطبیقی تاریخی | Historical Comparative | TECHNIQUE | needs_review | abstract thin (37 chars < 40) | enrich the definition/abstract |
| kg-technique-image-analysis | تحلیل تصاویر | Image Analysis | TECHNIQUE | needs_review | duplicate English name 'Image Analysis' (2 entities) | merge or rename to disambiguate the duplicate |
| kg-technique-impact-evaluation | ارزیابی اثر | Impact Evaluation | TECHNIQUE | needs_review | verification_status='flagged' (prior-work flag); abstract thin (36 chars < 40) | human re-check of this entity's content/type; enrich the definition/abstract |
| kg-technique-life-history | تاریخ زندگی | Life History | TECHNIQUE | needs_review | abstract thin (37 chars < 40) | enrich the definition/abstract |
| kg-technique-longitudinal | طولی | Longitudinal Design | TECHNIQUE | needs_review | abstract thin (34 chars < 40) | enrich the definition/abstract |
| kg-technique-online-survey | نظرسنجی آنلاین | Online Survey | TECHNIQUE | needs_review | verification_status='flagged' (prior-work flag) | human re-check of this entity's content/type |
| kg-technique-oral-history | تاریخ شفاهی | Oral History | TECHNIQUE | needs_review | abstract thin (38 chars < 40) | enrich the definition/abstract |
| kg-technique-organizational-ethnography | قوم‌نگاری سازمانی | Organizational Ethnography | TECHNIQUE | needs_review | abstract thin (32 chars < 40) | enrich the definition/abstract |
| kg-technique-outcome-evaluation | ارزیابی پیامد | Outcome Evaluation | TECHNIQUE | needs_review | verification_status='flagged' (prior-work flag); abstract thin (28 chars < 40) | human re-check of this entity's content/type; enrich the definition/abstract |
| kg-technique-part-action-rs | اقدام‌پژوهی مشارکتی | Participatory Action Research | TECHNIQUE | needs_review | abstract thin (36 chars < 40) | enrich the definition/abstract |
| kg-technique-personal-narrative | روایت شخصی | Personal Narrative | TECHNIQUE | needs_review | abstract thin (36 chars < 40) | enrich the definition/abstract |
| kg-technique-process-evaluation | ارزیابی فرایند | Process Evaluation | TECHNIQUE | needs_review | verification_status='flagged' (prior-work flag); abstract thin (32 chars < 40) | human re-check of this entity's content/type; enrich the definition/abstract |
| kg-technique-quasi-experimental | نیمه‌آزمایشی | Quasi-Experimental Design | TECHNIQUE | needs_review | verification_status='flagged' (prior-work flag) | human re-check of this entity's content/type |
| kg-technique-simulation | شبیه‌سازی | Simulation | TECHNIQUE | needs_review | abstract thin (38 chars < 40) | enrich the definition/abstract |
| kg-technique-single-case | مطالعه موردی منفرد | Single-Case Study | TECHNIQUE | needs_review | verification_status='flagged' (prior-work flag); abstract thin (24 chars < 40) | human re-check of this entity's content/type; enrich the definition/abstract |
| kg-technique-strawsonian | اشتراوسی | Straussian Grounded Theory | TECHNIQUE | needs_review | verification_status='flagged' (prior-work flag) | human re-check of this entity's content/type |
| kg-theory-active-audience | نظریه مخاطب فعال | Active Audience Theory | THEORY | needs_review | verification_status='flagged' (prior-work flag) | human re-check of this entity's content/type |
| kg-theory-algorithmic-agency | نظریه عاملیت الگوریتمی | Algorithmic Agency Theory | THEORY | needs_review | verification_status='flagged' (prior-work flag) | human re-check of this entity's content/type |
| kg-theory-attention-economy | نظریه اقتصاد توجه | Attention Economy Theory | THEORY | needs_review | verification_status='flagged' (prior-work flag) | human re-check of this entity's content/type |
| kg-theory-audience-participation | نظریه مشارکت مخاطب | Audience Participation Theory | THEORY | needs_review | verification_status='flagged' (prior-work flag) | human re-check of this entity's content/type |
| kg-theory-communication-management | نظریه مدیریت ارتباطات | Communication Management Theory | THEORY | needs_review | verification_status='flagged' (prior-work flag) | human re-check of this entity's content/type |
| kg-theory-election-communication | نظریه ارتباطات انتخاباتی | Election Communication Theory | THEORY | needs_review | verification_status='flagged' (prior-work flag) | human re-check of this entity's content/type |
| kg-theory-information-society | نظریه جامعه اطلاعاتی | Information Society Theory | THEORY | needs_review | verification_status='flagged' (prior-work flag) | human re-check of this entity's content/type |
| kg-theory-media-consumption | نظریه مصرف رسانه‌ای | Media Consumption Theory | THEORY | needs_review | verification_status='flagged' (prior-work flag) | human re-check of this entity's content/type |
| kg-theory-media-globalization | نظریه جهانی‌شدن رسانه | Media Globalization Theory | THEORY | needs_review | verification_status='flagged' (prior-work flag) | human re-check of this entity's content/type |
| kg-theory-networked-communication | نظریه ارتباطات شبکه‌ای | Networked Communication Theory | THEORY | needs_review | verification_status='flagged' (prior-work flag) | human re-check of this entity's content/type |
| kg-theory-participatory-culture | نظریه مشارکت و فرهنگ مشارکتی | Participatory Culture Theory | THEORY | needs_review | verification_status='flagged' (prior-work flag) | human re-check of this entity's content/type |
| kg-theory-platform-society | نظریه جامعه پلتفرمی | Platform Society Theory | THEORY | needs_review | verification_status='flagged' (prior-work flag) | human re-check of this entity's content/type |
| kg-theory-platformization | نظریه پلتفرمی‌شدن | Platformization Theory | THEORY | needs_review | verification_status='flagged' (prior-work flag) | human re-check of this entity's content/type |
| kg-theory-policy-brokerage | نظریه میانجی‌گری سیاست | Policy Brokerage / Policy Intermediation Theory | THEORY | needs_review | verification_status='flagged' (prior-work flag) | human re-check of this entity's content/type |
| kg-theory-political-advertising | نظریه تبلیغات سیاسی | Political Advertising Theory | THEORY | needs_review | verification_status='flagged' (prior-work flag) | human re-check of this entity's content/type |
| kg-theory-political-framing | نظریه چارچوب‌بندی سیاسی | Political Framing Theory | THEORY | needs_review | verification_status='flagged' (prior-work flag) | human re-check of this entity's content/type |
| kg-theory-resisting-audience | نظریه مخاطب مقاومت‌کننده | Resisting / Oppositional Audience Theory | THEORY | needs_review | verification_status='flagged' (prior-work flag) | human re-check of this entity's content/type |
| kg-theory-sensemaking | نظریه مدیریت هماهنگ معنا | Meaning Coordination / Sensemaking Theory | THEORY | needs_review | verification_status='flagged' (prior-work flag) | human re-check of this entity's content/type |
| kg-tradition-postcolonial | مطالعات پسااستعماری | Postcolonial Studies | TRADITION | needs_review | verification_status='flagged' (prior-work flag); duplicate Persian name 'مطالعات پسااستعماری' (2 entities); duplicate English name 'Postcolonial Studies' (2 entities) | human re-check of this entity's content/type; merge or rename to disambiguate the duplicate; merge or rename to disambiguate the duplicate |
| kg-tradition-postmodernism | پست‌مدرنیسم | Postmodernism | TRADITION | needs_review | verification_status='flagged' (prior-work flag) | human re-check of this entity's content/type |
| kg-tradition-pragmatism | پراگماتیسم | Pragmatism | TRADITION | needs_review | duplicate English name 'Pragmatism' (2 entities) | merge or rename to disambiguate the duplicate |

## Relations با مشکل (needs_review + error)

| source_id | target_id | relation_type | conf | status | problem | suggestion |
|---|---|---|---|---|---|---|
| kg-analysis-factor-analysis | kg-analysis-factorial-models | RELATED_TO | 0.75 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link); low confidence 0.75 < 0.80 | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...); human confirmation of the extraction |
| kg-analysis-mean | kg-analysis-median | COMPARED_WITH | 0.75 | needs_review | low confidence 0.75 < 0.80 | human confirmation of the extraction |
| kg-approach-althusser | kg-tradition-marxism | PART_OF | 0.95 | needs_review | description contains a raw 'kg-...' id (template leakage) | rewrite description with the human-readable names instead of ids |
| kg-approach-classical-marxism | kg-tradition-marxism | PART_OF | 0.95 | needs_review | description contains a raw 'kg-...' id (template leakage) | rewrite description with the human-readable names instead of ids |
| kg-approach-classical-pragmatism | kg-tradition-pragmatism | PART_OF | 0.95 | needs_review | description contains a raw 'kg-...' id (template leakage) | rewrite description with the human-readable names instead of ids |
| kg-approach-communication-systems | kg-tradition-systems-theory | PART_OF | 0.95 | needs_review | description contains a raw 'kg-...' id (template leakage) | rewrite description with the human-readable names instead of ids |
| kg-approach-communicative-action | kg-tradition-theory-of-action | PART_OF | 0.95 | needs_review | description contains a raw 'kg-...' id (template leakage) | rewrite description with the human-readable names instead of ids |
| kg-approach-complementary | kg-approach-mixed-methods | RELATED_TO | 0.80 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-approach-complementary | kg-paradigm-feminist | INFLUENCED_BY | 0.78 | needs_review | low confidence 0.78 < 0.80 | human confirmation of the extraction |
| kg-approach-complementary | kg-paradigm-postcolonial | INFLUENCED_BY | 0.72 | needs_review | low confidence 0.72 < 0.80 | human confirmation of the extraction |
| kg-approach-complementary | kg-paradigm-pragmatism | RELATED_TO | 0.80 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-approach-complex-systems | kg-tradition-systems-theory | PART_OF | 0.95 | needs_review | description contains a raw 'kg-...' id (template leakage) | rewrite description with the human-readable names instead of ids |
| kg-approach-critical-hermeneutics | kg-tradition-hermeneutics | PART_OF | 0.95 | needs_review | description contains a raw 'kg-...' id (template leakage) | rewrite description with the human-readable names instead of ids |
| kg-approach-decolonization | kg-tradition-postcolonialism | PART_OF | 0.95 | needs_review | description contains a raw 'kg-...' id (template leakage) | rewrite description with the human-readable names instead of ids |
| kg-approach-general-systems | kg-tradition-systems-theory | PART_OF | 0.95 | needs_review | description contains a raw 'kg-...' id (template leakage) | rewrite description with the human-readable names instead of ids |
| kg-approach-gramscian | kg-tradition-marxism | PART_OF | 0.95 | needs_review | description contains a raw 'kg-...' id (template leakage) | rewrite description with the human-readable names instead of ids |
| kg-approach-hermeneutic-phenomenology | kg-tradition-phenomenology | PART_OF | 0.95 | needs_review | description contains a raw 'kg-...' id (template leakage) | rewrite description with the human-readable names instead of ids |
| kg-approach-intersectional-feminism | kg-tradition-feminism | PART_OF | 0.95 | needs_review | description contains a raw 'kg-...' id (template leakage) | rewrite description with the human-readable names instead of ids |
| kg-approach-liberal-feminism | kg-tradition-feminism | PART_OF | 0.95 | needs_review | description contains a raw 'kg-...' id (template leakage) | rewrite description with the human-readable names instead of ids |
| kg-approach-media-functionalist | kg-tradition-functionalism | PART_OF | 0.95 | needs_review | description contains a raw 'kg-...' id (template leakage) | rewrite description with the human-readable names instead of ids |
| kg-approach-mixed-methods | kg-paradigm-postpositivism | RELATED_TO | 0.80 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-approach-mixed-methods | kg-paradigm-realism | INFLUENCED_BY | 0.75 | needs_review | low confidence 0.75 < 0.80 | human confirmation of the extraction |
| kg-approach-orientalism | kg-tradition-postcolonialism | PART_OF | 0.95 | needs_review | description contains a raw 'kg-...' id (template leakage) | rewrite description with the human-readable names instead of ids |
| kg-approach-philosophical-hermeneutics | kg-tradition-hermeneutics | PART_OF | 0.95 | needs_review | description contains a raw 'kg-...' id (template leakage) | rewrite description with the human-readable names instead of ids |
| kg-approach-postcolonial-studies | kg-tradition-postcolonialism | PART_OF | 0.95 | needs_review | description contains a raw 'kg-...' id (template leakage) | rewrite description with the human-readable names instead of ids |
| kg-approach-postmodern-feminism | kg-tradition-feminism | PART_OF | 0.95 | needs_review | description contains a raw 'kg-...' id (template leakage) | rewrite description with the human-readable names instead of ids |
| kg-approach-quantitative | kg-paradigm-realism | RELATED_TO | 0.80 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-approach-radical-feminism | kg-tradition-feminism | PART_OF | 0.95 | needs_review | description contains a raw 'kg-...' id (template leakage) | rewrite description with the human-readable names instead of ids |
| kg-approach-rational-action | kg-tradition-theory-of-action | PART_OF | 0.95 | needs_review | description contains a raw 'kg-...' id (template leakage) | rewrite description with the human-readable names instead of ids |
| kg-approach-social-interactionism | kg-tradition-interactionism | PART_OF | 0.95 | needs_review | description contains a raw 'kg-...' id (template leakage) | rewrite description with the human-readable names instead of ids |
| kg-approach-social-phenomenology | kg-approach-hermeneutic-phenomenology | RELATED_TO | 0.85 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-approach-social-phenomenology | kg-tradition-phenomenology | PART_OF | 0.95 | needs_review | description contains a raw 'kg-...' id (template leakage) | rewrite description with the human-readable names instead of ids |
| kg-approach-social-pragmatism | kg-tradition-pragmatism | PART_OF | 0.95 | needs_review | description contains a raw 'kg-...' id (template leakage) | rewrite description with the human-readable names instead of ids |
| kg-approach-socialist-feminism | kg-tradition-feminism | PART_OF | 0.95 | needs_review | description contains a raw 'kg-...' id (template leakage) | rewrite description with the human-readable names instead of ids |
| kg-approach-structural-functionalism | kg-tradition-functionalism | PART_OF | 0.95 | needs_review | description contains a raw 'kg-...' id (template leakage) | rewrite description with the human-readable names instead of ids |
| kg-approach-structured-action | kg-tradition-theory-of-action | PART_OF | 0.95 | needs_review | description contains a raw 'kg-...' id (template leakage) | rewrite description with the human-readable names instead of ids |
| kg-approach-symbolic-interactionism | kg-tradition-interactionism | PART_OF | 0.95 | needs_review | description contains a raw 'kg-...' id (template leakage) | rewrite description with the human-readable names instead of ids |
| kg-concept-hyperreality | kg-theory-cultivation | CRITICIZES | 0.70 | needs_review | low confidence 0.70 < 0.80 | human confirmation of the extraction |
| kg-concept-simulacra | kg-concept-hyperreality | RELATED_TO | 0.95 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-design-action-research | kg-technique-direct-observation | USES | 0.75 | needs_review | low confidence 0.75 < 0.80 | human confirmation of the extraction |
| kg-design-action-research | kg-technique-document-review | USES | 0.70 | needs_review | low confidence 0.70 < 0.80 | human confirmation of the extraction |
| kg-design-action-research | kg-technique-semistructured-interview | USES | 0.75 | needs_review | low confidence 0.75 < 0.80 | human confirmation of the extraction |
| kg-design-case-study | kg-technique-media-content-analysis | USES | 0.70 | needs_review | low confidence 0.70 < 0.80 | human confirmation of the extraction |
| kg-design-comparative | kg-technique-text-analysis | USES | 0.75 | needs_review | low confidence 0.75 < 0.80 | human confirmation of the extraction |
| kg-design-computational | kg-technique-digital-footprint-analysis | USES | 0.75 | needs_review | low confidence 0.75 < 0.80 | human confirmation of the extraction |
| kg-design-design-based | kg-technique-questionnaire | USES | 0.70 | needs_review | low confidence 0.70 < 0.80 | human confirmation of the extraction |
| kg-design-design-based | kg-technique-semistructured-interview | USES | 0.70 | needs_review | low confidence 0.70 < 0.80 | human confirmation of the extraction |
| kg-design-design-based | kg-technique-user-behavior-tracking | USES | 0.75 | needs_review | low confidence 0.75 < 0.80 | human confirmation of the extraction |
| kg-design-evaluation | kg-technique-attitude-scales | USES | 0.75 | needs_review | low confidence 0.75 < 0.80 | human confirmation of the extraction |
| kg-design-evaluation | kg-technique-user-behavior-tracking | USES | 0.70 | needs_review | low confidence 0.70 < 0.80 | human confirmation of the extraction |
| kg-design-experimental | kg-technique-user-behavior-tracking | USES | 0.75 | needs_review | low confidence 0.75 < 0.80 | human confirmation of the extraction |
| kg-design-historical | kg-technique-image-analysis | USES | 0.70 | needs_review | low confidence 0.70 < 0.80 | human confirmation of the extraction |
| kg-design-nonexperimental | kg-technique-document-review | USES | 0.70 | needs_review | low confidence 0.70 < 0.80 | human confirmation of the extraction |
| kg-ethics-anonymization | kg-ethics-confidentiality | RELATED_TO | 0.90 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-ethics-data-management | kg-ethics-open-data | RELATED_TO | 0.80 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-ethics-digital-research-ethics | kg-ethics-social-media-ethics | RELATED_TO | 0.85 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-ethics-open-data | kg-ethics-reproducibility | RELATED_TO | 0.85 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-ethics-pre-registration | kg-ethics-research-transparency | RELATED_TO | 0.85 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-ethics-reproducibility | kg-ethics-replicability | RELATED_TO | 0.90 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-framework-qual-discourse-analysis | kg-framework-critical-discourse | RELATED_TO | 0.95 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-framework-qual-grounded-theory | kg-technique-document-review | USES | 0.70 | needs_review | low confidence 0.70 < 0.80 | human confirmation of the extraction |
| kg-framework-saussurian-semiotics | kg-framework-peircean-semiotics | RELATED_TO | 0.95 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-instrument-survey | kg-technique-delfi | APPLIES_TO | 0.70 | needs_review | low confidence 0.70 < 0.80 | human confirmation of the extraction |
| kg-meth-sampling-probabilistic | kg-meth-sampling-nonprobabilistic | RELATED_TO | 0.90 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-model-surveillance-capitalism | kg-theory-attention-economy | CRITICIZES | 0.78 | needs_review | low confidence 0.78 < 0.80 | human confirmation of the extraction |
| kg-quality-criterion-validity | kg-quality-construct-validity | RELATED_TO | 0.80 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-sampling-availability | kg-approach-mixed-methods | APPLIES_TO | 0.75 | needs_review | low confidence 0.75 < 0.80 | human confirmation of the extraction |
| kg-sampling-availability | kg-sampling-purposeful | RELATED_TO | 0.80 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-sampling-cluster | kg-sampling-multistage | RELATED_TO | 0.85 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-sampling-maximum-variation | kg-sampling-theoretical | RELATED_TO | 0.75 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link); low confidence 0.75 < 0.80 | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...); human confirmation of the extraction |
| kg-sampling-multistage | kg-sampling-multiphase-stratified | RELATED_TO | 0.85 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-sampling-population | kg-sampling-sampling-frame | RELATED_TO | 0.90 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-sampling-population | kg-sampling-unit | RELATED_TO | 0.90 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-sampling-proportional | kg-sampling-stratified | RELATED_TO | 0.85 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-sampling-purposeful | kg-sampling-theoretical | RELATED_TO | 0.80 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-sampling-quota | kg-approach-mixed-methods | APPLIES_TO | 0.75 | needs_review | low confidence 0.75 < 0.80 | human confirmation of the extraction |
| kg-sampling-sample-size | kg-sampling-sampling-error | RELATED_TO | 0.85 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-sampling-sample-size | kg-sampling-selection-bias | RELATED_TO | 0.75 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link); low confidence 0.75 < 0.80 | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...); human confirmation of the extraction |
| kg-sampling-sample-size | kg-sampling-statistical-power | RELATED_TO | 0.85 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-sampling-sampling-frame | kg-sampling-selection-bias | RELATED_TO | 0.85 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-sampling-simple-random | kg-sampling-systematic-random | RELATED_TO | 0.85 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-sampling-snowball | kg-sampling-maximum-variation | COMPARED_WITH | 0.75 | needs_review | low confidence 0.75 < 0.80 | human confirmation of the extraction |
| kg-sampling-snowball | kg-sampling-sequential | RELATED_TO | 0.75 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link); low confidence 0.75 < 0.80 | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...); human confirmation of the extraction |
| kg-sampling-stratified | kg-sampling-cluster | RELATED_TO | 0.85 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-sampling-theoretical-saturation | kg-sampling-data-saturation | RELATED_TO | 0.90 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-sampling-unit | kg-sampling-analysis-unit | RELATED_TO | 0.85 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-software-antconc | kg-framework-qual-content-analysis | APPLIES_TO | 0.70 | needs_review | low confidence 0.70 < 0.80 | human confirmation of the extraction |
| kg-software-voyant | kg-framework-qual-content-analysis | APPLIES_TO | 0.70 | needs_review | low confidence 0.70 < 0.80 | human confirmation of the extraction |
| kg-subfield-actor-network-theory | kg-tradition-sts | PART_OF | 0.95 | needs_review | description contains a raw 'kg-...' id (template leakage) | rewrite description with the human-readable names instead of ids |
| kg-subfield-actor-network-theory | kg-tradition-systems-theory | RELATED_TO | 0.80 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-subfield-communication-networks | kg-theory-information-society | RELATED_TO | 0.85 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-subfield-communication-networks | kg-tradition-network-theory | PART_OF | 0.95 | needs_review | description contains a raw 'kg-...' id (template leakage) | rewrite description with the human-readable names instead of ids |
| kg-subfield-crisis-comm | kg-theory-media-consumption | RELATED_TO | 0.70 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link); low confidence 0.70 < 0.80 | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...); human confirmation of the extraction |
| kg-subfield-data-journalism | kg-subfield-digital-media | RELATED_TO | 0.90 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-subfield-development-comm | kg-subfield-international-comm | RELATED_TO | 0.85 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-subfield-digital-games | kg-theory-participatory-culture | RELATED_TO | 0.85 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-subfield-film-tv | kg-approach-classical-marxism | CRITICIZES | 0.75 | needs_review | low confidence 0.75 < 0.80 | human confirmation of the extraction |
| kg-subfield-film-tv | kg-theory-culture-industry | RELATED_TO | 0.85 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-subfield-journalism | kg-subfield-radio-tv | RELATED_TO | 0.80 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-subfield-media-governance | kg-subfield-media-ownership-economics | RELATED_TO | 0.90 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-subfield-media-literacy | kg-approach-communicative-action | RELATED_TO | 0.80 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-subfield-networked-society | kg-subfield-digital-media | RELATED_TO | 0.90 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-subfield-networked-society | kg-tradition-network-theory | PART_OF | 0.95 | needs_review | description contains a raw 'kg-...' id (template leakage) | rewrite description with the human-readable names instead of ids |
| kg-subfield-social-networks | kg-subfield-communication-networks | RELATED_TO | 0.90 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-subfield-social-networks | kg-technique-focus-group | USES | 0.70 | needs_review | low confidence 0.70 < 0.80 | human confirmation of the extraction |
| kg-subfield-social-networks | kg-tradition-network-theory | PART_OF | 0.95 | needs_review | description contains a raw 'kg-...' id (template leakage) | rewrite description with the human-readable names instead of ids |
| kg-subfield-sociology-of-science | kg-subfield-studies-of-technology | RELATED_TO | 0.95 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-subfield-sociology-of-science | kg-tradition-sts | PART_OF | 0.95 | needs_review | description contains a raw 'kg-...' id (template leakage) | rewrite description with the human-readable names instead of ids |
| kg-subfield-studies-of-technology | kg-tradition-sts | PART_OF | 0.95 | needs_review | description contains a raw 'kg-...' id (template leakage) | rewrite description with the human-readable names instead of ids |
| kg-technique-api-extraction | kg-technique-social-media-data | RELATED_TO | 0.85 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-technique-attitude-scales | kg-approach-mixed-methods | APPLIES_TO | 0.75 | needs_review | low confidence 0.75 < 0.80 | human confirmation of the extraction |
| kg-technique-attitude-scales | kg-technique-satisfaction-measurement | RELATED_TO | 0.80 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-technique-delfi | kg-approach-mixed-methods | APPLIES_TO | 0.75 | needs_review | low confidence 0.75 < 0.80 | human confirmation of the extraction |
| kg-technique-digital-log-analysis | kg-approach-mixed-methods | APPLIES_TO | 0.75 | needs_review | low confidence 0.75 < 0.80 | human confirmation of the extraction |
| kg-technique-digital-log-analysis | kg-technique-digital-footprint-analysis | RELATED_TO | 0.80 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-technique-digital-observation | kg-technique-digital-ethnography | RELATED_TO | 0.85 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-technique-direct-observation | kg-technique-participant-observation | RELATED_TO | 0.80 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-technique-direct-observation | kg-technique-structured-observation | RELATED_TO | 0.80 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-technique-document-review | kg-technique-archival-analysis | RELATED_TO | 0.80 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-technique-document-review | kg-technique-official-document-analysis | RELATED_TO | 0.85 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-technique-focus-group | kg-approach-mixed-methods | APPLIES_TO | 0.75 | needs_review | low confidence 0.75 < 0.80 | human confirmation of the extraction |
| kg-technique-group-interview | kg-approach-mixed-methods | APPLIES_TO | 0.75 | needs_review | low confidence 0.75 < 0.80 | human confirmation of the extraction |
| kg-technique-group-interview | kg-technique-focus-group | RELATED_TO | 0.85 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-technique-image-analysis | kg-technique-video-analysis | RELATED_TO | 0.85 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-technique-media-content-analysis | kg-technique-text-analysis | RELATED_TO | 0.80 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-technique-naturalistic-observation | kg-technique-field-observation | RELATED_TO | 0.80 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-technique-participant-observation | kg-technique-nonparticip-obs | RELATED_TO | 0.80 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-technique-psychometric-tests | kg-technique-attitude-scales | RELATED_TO | 0.85 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-technique-questionnaire | kg-technique-structured-interview | RELATED_TO | 0.80 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-technique-recognition-measurement | kg-technique-attention-measurement | RELATED_TO | 0.80 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-technique-satisfaction-measurement | kg-technique-trust-measurement | RELATED_TO | 0.75 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link); low confidence 0.75 < 0.80 | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...); human confirmation of the extraction |
| kg-technique-semistructured-interview | kg-technique-in-depth-interview | RELATED_TO | 0.85 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-technique-social-media-data | kg-technique-user-behavior-tracking | RELATED_TO | 0.85 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-technique-structured-interview | kg-technique-semistructured-interview | RELATED_TO | 0.85 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-technique-tech-development-comm | kg-theory-dependence | TESTS | 0.70 | needs_review | low confidence 0.70 < 0.80 | human confirmation of the extraction |
| kg-technique-tech-digital-media | kg-theory-attention-economy | TESTS | 0.70 | needs_review | low confidence 0.70 < 0.80 | human confirmation of the extraction |
| kg-technique-text-analysis | kg-technique-image-analysis | RELATED_TO | 0.75 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link); low confidence 0.75 < 0.80 | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...); human confirmation of the extraction |
| kg-technique-user-behavior-tracking | kg-technique-digital-log-analysis | RELATED_TO | 0.85 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-technique-web-scraping | kg-technique-api-extraction | RELATED_TO | 0.85 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-theory-active-audience | kg-theory-resisting-audience | RELATED_TO | 0.90 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-theory-agenda-setting | kg-theory-agenda-setting | EXTENDS | 0.90 | needs_review | self-loop (source == target) | remove the self-referencing relation |
| kg-theory-agenda-setting | kg-theory-agenda-setting | INFLUENCED_BY | 0.90 | needs_review | self-loop (source == target) | remove the self-referencing relation |
| kg-theory-agenda-setting | kg-theory-framing | RELATED_TO | 0.90 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-theory-agenda-setting | kg-theory-political-framing | RELATED_TO | 0.90 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-theory-attention-economy | kg-theory-algorithmic-agency | RELATED_TO | 0.85 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-theory-attention-economy | kg-theory-platformization | RELATED_TO | 0.85 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-theory-cultivation | kg-theory-active-audience | CRITICIZES | 0.75 | needs_review | low confidence 0.75 < 0.80 | human confirmation of the extraction |
| kg-theory-cultivation | kg-theory-dependence | RELATED_TO | 0.85 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-theory-culture-industry | kg-theory-cultivation | INFLUENCED | 0.70 | needs_review | low confidence 0.70 < 0.80 | human confirmation of the extraction |
| kg-theory-culture-industry | kg-theory-cultural-imperialism | RELATED_TO | 0.85 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-theory-culture-industry | kg-theory-mass-society | RELATED_TO | 0.90 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-theory-election-communication | kg-theory-political-advertising | RELATED_TO | 0.90 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-theory-encoding-decoding | kg-theory-active-audience | RELATED_TO | 0.95 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-theory-expectancy-violation | kg-theory-sensemaking | RELATED_TO | 0.80 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-theory-magic-bullet | kg-theory-two-step | RELATED_TO | 0.90 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-theory-media-convergence | kg-theory-participatory-culture | RELATED_TO | 0.95 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-theory-media-globalization | kg-theory-cultural-imperialism | RELATED_TO | 0.85 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-theory-network-society | kg-theory-information-society | RELATED_TO | 0.90 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-theory-network-society | kg-theory-networked-communication | RELATED_TO | 0.90 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-theory-participatory-culture | kg-theory-audience-participation | RELATED_TO | 0.90 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-theory-platformization | kg-theory-algorithmic-agency | RELATED_TO | 0.85 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-theory-platformization | kg-theory-platform-society | RELATED_TO | 0.90 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-theory-policy-brokerage | kg-theory-public-sphere | RELATED_TO | 0.85 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-theory-public-sphere | kg-theory-culture-industry | RELATED_TO | 0.85 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-theory-public-sphere | kg-theory-public-sphere | EXTENDS | 0.90 | needs_review | self-loop (source == target) | remove the self-referencing relation |
| kg-theory-public-sphere | kg-theory-public-sphere | INFLUENCED_BY | 0.90 | needs_review | self-loop (source == target) | remove the self-referencing relation |
| kg-theory-social-penetration | kg-theory-social-exchange | RELATED_TO | 0.85 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-theory-spiral-silence | kg-theory-public-sphere | CRITICIZES | 0.72 | needs_review | low confidence 0.72 < 0.80 | human confirmation of the extraction |
| kg-theory-spiral-silence | kg-theory-public-sphere | RELATED_TO | 0.85 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-theory-spiral-silence | kg-theory-spiral-silence | EXTENDS | 0.90 | needs_review | self-loop (source == target) | remove the self-referencing relation |
| kg-theory-spiral-silence | kg-theory-spiral-silence | INFLUENCED_BY | 0.90 | needs_review | self-loop (source == target) | remove the self-referencing relation |
| kg-theory-uncertainty-reduction | kg-theory-social-penetration | RELATED_TO | 0.85 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-theory-uses-and-gratifications | kg-theory-media-consumption | RELATED_TO | 0.90 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-tradition-columbia | kg-tradition-survey | RELATED_TO | 0.90 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-tradition-feminism | kg-tradition-postcolonialism | RELATED_TO | 0.85 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-tradition-hegemony | kg-tradition-ideology | RELATED_TO | 0.90 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |
| kg-tradition-postcolonial | kg-tradition-decolonial | RELATED_TO | 0.95 | needs_review | relation_type='RELATED_TO' (ambiguous/weak link) | refine to a more specific type (IS_A, PART_OF, INFLUENCED_BY, ...) |

## آمار به تفکیک entity_type

| entity_type | total | verified | needs_review | error |
|---|---|---|---|---|
| TECHNIQUE | 92 | 63 | 29 | 0 |
| ANALYSIS | 90 | 73 | 17 | 0 |
| APPROACH | 54 | 44 | 10 | 0 |
| FRAMEWORK | 46 | 42 | 4 | 0 |
| THEORY | 42 | 23 | 19 | 0 |
| TRADITION | 33 | 30 | 3 | 0 |
| SUBFIELD | 28 | 28 | 0 | 0 |
| CONCEPT | 27 | 26 | 1 | 0 |
| QUALITY | 23 | 23 | 0 | 0 |
| SOFTWARE | 20 | 16 | 4 | 0 |
| SAMPLING | 17 | 15 | 2 | 0 |
| ETHICS | 14 | 14 | 0 | 0 |
| DESIGN | 13 | 11 | 2 | 0 |
| PARADIGM | 11 | 9 | 2 | 0 |
| METHODOLOGY | 10 | 10 | 0 | 0 |
| MODEL | 5 | 5 | 0 | 0 |
| INSTRUMENT | 4 | 4 | 0 | 0 |

## آمار به تفکیک relation_type

| relation_type | total | verified | needs_review | error |
|---|---|---|---|---|
| PART_OF | 239 | 206 | 33 | 0 |
| APPLIES_TO | 204 | 194 | 10 | 0 |
| USES | 174 | 158 | 16 | 0 |
| RELATED_TO | 99 | 0 | 99 | 0 |
| BELONGS_TO | 68 | 68 | 0 | 0 |
| COLLECTS | 57 | 57 | 0 | 0 |
| INFLUENCED_BY | 46 | 40 | 6 | 0 |
| ANALYZES | 35 | 35 | 0 | 0 |
| IS_A | 28 | 28 | 0 | 0 |
| EXTENDS | 23 | 20 | 3 | 0 |
| MEASURES | 19 | 19 | 0 | 0 |
| INFLUENCED | 17 | 16 | 1 | 0 |
| CRITICIZES | 15 | 10 | 5 | 0 |
| COMPARED_WITH | 13 | 11 | 2 | 0 |
| PROPOSED_BY | 13 | 13 | 0 | 0 |
| TESTS | 13 | 11 | 2 | 0 |
| CONTRADICTS | 5 | 5 | 0 | 0 |
| DERIVED_FROM | 4 | 4 | 0 | 0 |

## نمونه‌های با مشکل (top samples)

### ۵ نمونه‌ی entity

- **kg-analysis-centrality-analysis** (ANALYSIS) — تحلیل مرکزیت / Centrality Analysis → abstract thin (37 chars < 40)
- **kg-analysis-cpd** (ANALYSIS) — تحلیل محاسباتی گفتمان / Computational Discourse Analys… → abstract thin (28 chars < 40)
- **kg-analysis-info-diffusion** (ANALYSIS) — تحلیل انتشار اطلاعات / Information Diffusion Analysis → abstract thin (33 chars < 40)
- **kg-analysis-multimedia-analysis** (ANALYSIS) — تحلیل چندرسانه‌ای / Multimedia Analysis → abstract thin (35 chars < 40)
- **kg-analysis-network-clustering-analysis** (ANALYSIS) — تحلیل خوشه‌های شبکه / Network Clustering Analysis → abstract thin (35 chars < 40)

### ۵ نمونه‌ی relation

- **RELATED_TO** kg-analysis-factor-analysis → kg-analysis-factorial-models (conf 0.75) → relation_type='RELATED_TO' (ambiguous/weak link); low confidence 0.75 < 0.80
- **COMPARED_WITH** kg-analysis-mean → kg-analysis-median (conf 0.75) → low confidence 0.75 < 0.80
- **PART_OF** kg-approach-althusser → kg-tradition-marxism (conf 0.95) → description contains a raw 'kg-...' id (template leakage)
- **PART_OF** kg-approach-classical-marxism → kg-tradition-marxism (conf 0.95) → description contains a raw 'kg-...' id (template leakage)
- **PART_OF** kg-approach-classical-pragmatism → kg-tradition-pragmatism (conf 0.95) → description contains a raw 'kg-...' id (template leakage)

---
*تولیدشده توسط `tools/w5_phase_c_audit.py` — read-only audit.*
