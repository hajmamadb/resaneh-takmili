-- Phase C: merge 16 duplicate entities into their canonical ids.
-- For each (dup, canon):
--   1) redirect knowledge_relations (both directions) dup -> canon,
--      but only when an identical row does not already exist (avoid uq_rel dup).
--   2) drop any redirected rows that are now exact duplicates.
--   3) delete the dup's kg_chunks (canon keeps its own; dup chunks were redundant).
--   4) delete the dup row from knowledge_entities.
-- All pairs verified to share the same construct. Idempotent: re-running on
-- already-merged ids is a no-op (dup id no longer exists -> 0 rows affected).

-- NOTE: entity_content_links rows pointing at a dup id are redirected to the
-- canonical id BEFORE the dup entity is deleted; if the canonical id already
-- has a link to the same content, the redirected row is dropped (PK conflict).

-- ============ 0) redirect all entity_content_links from dup -> canon first ============
-- (do it up-front so the per-pair DELETE entity can't hit an FK violation)
-- 0a) drop dup-side rows whose (canon, content_id) already exists (would hit PK)
DELETE e1 FROM entity_content_links e1
 JOIN entity_content_links e2
  ON e1.content_id=e2.content_id AND e2.entity_id=(
      CASE e1.entity_id
        WHEN 'kg-tech-crisis-comm' THEN 'kg-technique-tech-crisis-comm'
        WHEN 'kg-tech-development-comm' THEN 'kg-technique-tech-development-comm'
        WHEN 'kg-tech-political-comm' THEN 'kg-technique-tech-political-comm'
        WHEN 'kg-technique-advertising-research' THEN 'kg-technique-tech-advertising'
        WHEN 'kg-technique-audience-research' THEN 'kg-technique-tech-audience'
        WHEN 'kg-technique-digital-media-research' THEN 'kg-technique-tech-digital-media'
        WHEN 'kg-technique-film-tv-research' THEN 'kg-technique-tech-film-tv'
        WHEN 'kg-technique-news-research' THEN 'kg-technique-tech-journalism'
        WHEN 'kg-technique-pr-research' THEN 'kg-technique-tech-pr'
        WHEN 'kg-technique-social-media-research' THEN 'kg-technique-tech-social-media'
        WHEN 'kg-design-grounded-theory' THEN 'kg-framework-qual-grounded-theory'
        WHEN 'kg-framework-discourse-analysis' THEN 'kg-framework-qual-discourse-analysis'
        WHEN 'kg-framework-semiotic-analysis' THEN 'kg-framework-qual-semiotic-analysis'
        WHEN 'kg-theory-political-agenda' THEN 'kg-theory-agenda-setting'
        WHEN 'kg-theory-political-public-sphere' THEN 'kg-theory-public-sphere'
        WHEN 'kg-theory-political-spiral' THEN 'kg-theory-spiral-silence'
      END)
 WHERE e1.entity_id IN ('kg-tech-crisis-comm','kg-tech-development-comm','kg-tech-political-comm','kg-technique-advertising-research','kg-technique-audience-research','kg-technique-digital-media-research','kg-technique-film-tv-research','kg-technique-news-research','kg-technique-pr-research','kg-technique-social-media-research','kg-design-grounded-theory','kg-framework-discourse-analysis','kg-framework-semiotic-analysis','kg-theory-political-agenda','kg-theory-political-public-sphere','kg-theory-political-spiral');
-- 0b) redirect the remaining dup-side rows
UPDATE entity_content_links SET entity_id='kg-technique-tech-crisis-comm' WHERE entity_id='kg-tech-crisis-comm';
UPDATE entity_content_links SET entity_id='kg-technique-tech-development-comm' WHERE entity_id='kg-tech-development-comm';
UPDATE entity_content_links SET entity_id='kg-technique-tech-political-comm' WHERE entity_id='kg-tech-political-comm';
UPDATE entity_content_links SET entity_id='kg-technique-tech-advertising' WHERE entity_id='kg-technique-advertising-research';
UPDATE entity_content_links SET entity_id='kg-technique-tech-audience' WHERE entity_id='kg-technique-audience-research';
UPDATE entity_content_links SET entity_id='kg-technique-tech-digital-media' WHERE entity_id='kg-technique-digital-media-research';
UPDATE entity_content_links SET entity_id='kg-technique-tech-film-tv' WHERE entity_id='kg-technique-film-tv-research';
UPDATE entity_content_links SET entity_id='kg-technique-tech-journalism' WHERE entity_id='kg-technique-news-research';
UPDATE entity_content_links SET entity_id='kg-technique-tech-pr' WHERE entity_id='kg-technique-pr-research';
UPDATE entity_content_links SET entity_id='kg-technique-tech-social-media' WHERE entity_id='kg-technique-social-media-research';
-- 3 family pairs
UPDATE entity_content_links SET entity_id='kg-framework-qual-grounded-theory' WHERE entity_id='kg-design-grounded-theory';
UPDATE entity_content_links SET entity_id='kg-framework-qual-discourse-analysis' WHERE entity_id='kg-framework-discourse-analysis';
UPDATE entity_content_links SET entity_id='kg-framework-qual-semiotic-analysis' WHERE entity_id='kg-framework-semiotic-analysis';
-- 3 theory pairs
UPDATE entity_content_links SET entity_id='kg-theory-agenda-setting' WHERE entity_id='kg-theory-political-agenda';
UPDATE entity_content_links SET entity_id='kg-theory-public-sphere' WHERE entity_id='kg-theory-political-public-sphere';
UPDATE entity_content_links SET entity_id='kg-theory-spiral-silence' WHERE entity_id='kg-theory-political-spiral';
-- drop any entity_content_links rows that now violate the PK (entity_id, content_id)
DELETE e1 FROM entity_content_links e1 JOIN entity_content_links e2
  ON e1.entity_id=e2.entity_id AND e1.content_id=e2.content_id AND e1.created_at > e2.created_at;

-- ============ 9 research-area pairs (kg-tech-* / kg-technique-*-research -> kg-technique-tech-*) ============
-- pattern: duplicate side has the longer id, canonical is kg-technique-tech-*

-- kg-tech-crisis-comm -> kg-technique-tech-crisis-comm
UPDATE knowledge_relations SET source_entity_id='kg-technique-tech-crisis-comm' WHERE source_entity_id='kg-tech-crisis-comm';
UPDATE knowledge_relations SET target_entity_id='kg-technique-tech-crisis-comm' WHERE target_entity_id='kg-tech-crisis-comm';
DELETE r1 FROM knowledge_relations r1 JOIN knowledge_relations r2
  ON r1.source_entity_id=r2.source_entity_id AND r1.target_entity_id=r2.target_entity_id AND r1.relation_type=r2.relation_type AND r1.id>r2.id
 WHERE r1.source_entity_id='kg-technique-tech-crisis-comm' OR r1.target_entity_id='kg-technique-tech-crisis-comm';
DELETE FROM kg_chunks WHERE entity_id='kg-tech-crisis-comm';
DELETE FROM knowledge_entities WHERE id='kg-tech-crisis-comm';

-- kg-tech-development-comm -> kg-technique-tech-development
UPDATE knowledge_relations SET source_entity_id='kg-technique-tech-development-comm' WHERE source_entity_id='kg-tech-development-comm';
UPDATE knowledge_relations SET target_entity_id='kg-technique-tech-development-comm' WHERE target_entity_id='kg-tech-development-comm';
DELETE r1 FROM knowledge_relations r1 JOIN knowledge_relations r2
  ON r1.source_entity_id=r2.source_entity_id AND r1.target_entity_id=r2.target_entity_id AND r1.relation_type=r2.relation_type AND r1.id>r2.id
 WHERE r1.source_entity_id='kg-technique-tech-development-comm' OR r1.target_entity_id='kg-technique-tech-development-comm';
DELETE FROM kg_chunks WHERE entity_id='kg-tech-development-comm';
DELETE FROM knowledge_entities WHERE id='kg-tech-development-comm';

-- kg-tech-political-comm -> kg-technique-tech-political-comm
UPDATE knowledge_relations SET source_entity_id='kg-technique-tech-political-comm' WHERE source_entity_id='kg-tech-political-comm';
UPDATE knowledge_relations SET target_entity_id='kg-technique-tech-political-comm' WHERE target_entity_id='kg-tech-political-comm';
DELETE r1 FROM knowledge_relations r1 JOIN knowledge_relations r2
  ON r1.source_entity_id=r2.source_entity_id AND r1.target_entity_id=r2.target_entity_id AND r1.relation_type=r2.relation_type AND r1.id>r2.id
 WHERE r1.source_entity_id='kg-technique-tech-political-comm' OR r1.target_entity_id='kg-technique-tech-political-comm';
DELETE FROM kg_chunks WHERE entity_id='kg-tech-political-comm';
DELETE FROM knowledge_entities WHERE id='kg-tech-political-comm';

-- kg-technique-advertising-research -> kg-technique-tech-advertising
UPDATE knowledge_relations SET source_entity_id='kg-technique-tech-advertising' WHERE source_entity_id='kg-technique-advertising-research';
UPDATE knowledge_relations SET target_entity_id='kg-technique-tech-advertising' WHERE target_entity_id='kg-technique-advertising-research';
DELETE r1 FROM knowledge_relations r1 JOIN knowledge_relations r2
  ON r1.source_entity_id=r2.source_entity_id AND r1.target_entity_id=r2.target_entity_id AND r1.relation_type=r2.relation_type AND r1.id>r2.id
 WHERE r1.source_entity_id='kg-technique-tech-advertising' OR r1.target_entity_id='kg-technique-tech-advertising';
DELETE FROM kg_chunks WHERE entity_id='kg-technique-advertising-research';
DELETE FROM knowledge_entities WHERE id='kg-technique-advertising-research';

-- kg-technique-audience-research -> kg-technique-tech-audience
UPDATE knowledge_relations SET source_entity_id='kg-technique-tech-audience' WHERE source_entity_id='kg-technique-audience-research';
UPDATE knowledge_relations SET target_entity_id='kg-technique-tech-audience' WHERE target_entity_id='kg-technique-audience-research';
DELETE r1 FROM knowledge_relations r1 JOIN knowledge_relations r2
  ON r1.source_entity_id=r2.source_entity_id AND r1.target_entity_id=r2.target_entity_id AND r1.relation_type=r2.relation_type AND r1.id>r2.id
 WHERE r1.source_entity_id='kg-technique-tech-audience' OR r1.target_entity_id='kg-technique-tech-audience';
DELETE FROM kg_chunks WHERE entity_id='kg-technique-audience-research';
DELETE FROM knowledge_entities WHERE id='kg-technique-audience-research';

-- kg-technique-digital-media-research -> kg-technique-tech-digital-media
UPDATE knowledge_relations SET source_entity_id='kg-technique-tech-digital-media' WHERE source_entity_id='kg-technique-digital-media-research';
UPDATE knowledge_relations SET target_entity_id='kg-technique-tech-digital-media' WHERE target_entity_id='kg-technique-digital-media-research';
DELETE r1 FROM knowledge_relations r1 JOIN knowledge_relations r2
  ON r1.source_entity_id=r2.source_entity_id AND r1.target_entity_id=r2.target_entity_id AND r1.relation_type=r2.relation_type AND r1.id>r2.id
 WHERE r1.source_entity_id='kg-technique-tech-digital-media' OR r1.target_entity_id='kg-technique-tech-digital-media';
DELETE FROM kg_chunks WHERE entity_id='kg-technique-digital-media-research';
DELETE FROM knowledge_entities WHERE id='kg-technique-digital-media-research';

-- kg-technique-film-tv-research -> kg-technique-tech-film-tv
UPDATE knowledge_relations SET source_entity_id='kg-technique-tech-film-tv' WHERE source_entity_id='kg-technique-film-tv-research';
UPDATE knowledge_relations SET target_entity_id='kg-technique-tech-film-tv' WHERE target_entity_id='kg-technique-film-tv-research';
DELETE r1 FROM knowledge_relations r1 JOIN knowledge_relations r2
  ON r1.source_entity_id=r2.source_entity_id AND r1.target_entity_id=r2.target_entity_id AND r1.relation_type=r2.relation_type AND r1.id>r2.id
 WHERE r1.source_entity_id='kg-technique-tech-film-tv' OR r1.target_entity_id='kg-technique-tech-film-tv';
DELETE FROM kg_chunks WHERE entity_id='kg-technique-film-tv-research';
DELETE FROM knowledge_entities WHERE id='kg-technique-film-tv-research';

-- kg-technique-news-research -> kg-technique-tech-journalism
UPDATE knowledge_relations SET source_entity_id='kg-technique-tech-journalism' WHERE source_entity_id='kg-technique-news-research';
UPDATE knowledge_relations SET target_entity_id='kg-technique-tech-journalism' WHERE target_entity_id='kg-technique-news-research';
DELETE r1 FROM knowledge_relations r1 JOIN knowledge_relations r2
  ON r1.source_entity_id=r2.source_entity_id AND r1.target_entity_id=r2.target_entity_id AND r1.relation_type=r2.relation_type AND r1.id>r2.id
 WHERE r1.source_entity_id='kg-technique-tech-journalism' OR r1.target_entity_id='kg-technique-tech-journalism';
DELETE FROM kg_chunks WHERE entity_id='kg-technique-news-research';
DELETE FROM knowledge_entities WHERE id='kg-technique-news-research';

-- kg-technique-pr-research -> kg-technique-tech-pr
UPDATE knowledge_relations SET source_entity_id='kg-technique-tech-pr' WHERE source_entity_id='kg-technique-pr-research';
UPDATE knowledge_relations SET target_entity_id='kg-technique-tech-pr' WHERE target_entity_id='kg-technique-pr-research';
DELETE r1 FROM knowledge_relations r1 JOIN knowledge_relations r2
  ON r1.source_entity_id=r2.source_entity_id AND r1.target_entity_id=r2.target_entity_id AND r1.relation_type=r2.relation_type AND r1.id>r2.id
 WHERE r1.source_entity_id='kg-technique-tech-pr' OR r1.target_entity_id='kg-technique-tech-pr';
DELETE FROM kg_chunks WHERE entity_id='kg-technique-pr-research';
DELETE FROM knowledge_entities WHERE id='kg-technique-pr-research';

-- kg-technique-social-media-research -> kg-technique-tech-social-media
UPDATE knowledge_relations SET source_entity_id='kg-technique-tech-social-media' WHERE source_entity_id='kg-technique-social-media-research';
UPDATE knowledge_relations SET target_entity_id='kg-technique-tech-social-media' WHERE target_entity_id='kg-technique-social-media-research';
DELETE r1 FROM knowledge_relations r1 JOIN knowledge_relations r2
  ON r1.source_entity_id=r2.source_entity_id AND r1.target_entity_id=r2.target_entity_id AND r1.relation_type=r2.relation_type AND r1.id>r2.id
 WHERE r1.source_entity_id='kg-technique-tech-social-media' OR r1.target_entity_id='kg-technique-tech-social-media';
DELETE FROM kg_chunks WHERE entity_id='kg-technique-social-media-research';
DELETE FROM knowledge_entities WHERE id='kg-technique-social-media-research';

-- ============ 3 family vs bare (bare -> family) ============
-- kg-design-grounded-theory -> kg-framework-qual-grounded-theory
UPDATE knowledge_relations SET source_entity_id='kg-framework-qual-grounded-theory' WHERE source_entity_id='kg-design-grounded-theory';
UPDATE knowledge_relations SET target_entity_id='kg-framework-qual-grounded-theory' WHERE target_entity_id='kg-design-grounded-theory';
DELETE r1 FROM knowledge_relations r1 JOIN knowledge_relations r2
  ON r1.source_entity_id=r2.source_entity_id AND r1.target_entity_id=r2.target_entity_id AND r1.relation_type=r2.relation_type AND r1.id>r2.id
 WHERE r1.source_entity_id='kg-framework-qual-grounded-theory' OR r1.target_entity_id='kg-framework-qual-grounded-theory';
DELETE FROM kg_chunks WHERE entity_id='kg-design-grounded-theory';
DELETE FROM knowledge_entities WHERE id='kg-design-grounded-theory';

-- kg-framework-discourse-analysis -> kg-framework-qual-discourse-analysis
UPDATE knowledge_relations SET source_entity_id='kg-framework-qual-discourse-analysis' WHERE source_entity_id='kg-framework-discourse-analysis';
UPDATE knowledge_relations SET target_entity_id='kg-framework-qual-discourse-analysis' WHERE target_entity_id='kg-framework-discourse-analysis';
DELETE r1 FROM knowledge_relations r1 JOIN knowledge_relations r2
  ON r1.source_entity_id=r2.source_entity_id AND r1.target_entity_id=r2.target_entity_id AND r1.relation_type=r2.relation_type AND r1.id>r2.id
 WHERE r1.source_entity_id='kg-framework-qual-discourse-analysis' OR r1.target_entity_id='kg-framework-qual-discourse-analysis';
DELETE FROM kg_chunks WHERE entity_id='kg-framework-discourse-analysis';
DELETE FROM knowledge_entities WHERE id='kg-framework-discourse-analysis';

-- kg-framework-semiotic-analysis -> kg-framework-qual-semiotic-analysis
UPDATE knowledge_relations SET source_entity_id='kg-framework-qual-semiotic-analysis' WHERE source_entity_id='kg-framework-semiotic-analysis';
UPDATE knowledge_relations SET target_entity_id='kg-framework-qual-semiotic-analysis' WHERE target_entity_id='kg-framework-semiotic-analysis';
DELETE r1 FROM knowledge_relations r1 JOIN knowledge_relations r2
  ON r1.source_entity_id=r2.source_entity_id AND r1.target_entity_id=r2.target_entity_id AND r1.relation_type=r2.relation_type AND r1.id>r2.id
 WHERE r1.source_entity_id='kg-framework-qual-semiotic-analysis' OR r1.target_entity_id='kg-framework-qual-semiotic-analysis';
DELETE FROM kg_chunks WHERE entity_id='kg-framework-semiotic-analysis';
DELETE FROM knowledge_entities WHERE id='kg-framework-semiotic-analysis';

-- ============ 3 theory pairs (political-* -> canonical theory) ============
-- kg-theory-political-agenda -> kg-theory-agenda-setting
UPDATE knowledge_relations SET source_entity_id='kg-theory-agenda-setting' WHERE source_entity_id='kg-theory-political-agenda';
UPDATE knowledge_relations SET target_entity_id='kg-theory-agenda-setting' WHERE target_entity_id='kg-theory-political-agenda';
DELETE r1 FROM knowledge_relations r1 JOIN knowledge_relations r2
  ON r1.source_entity_id=r2.source_entity_id AND r1.target_entity_id=r2.target_entity_id AND r1.relation_type=r2.relation_type AND r1.id>r2.id
 WHERE r1.source_entity_id='kg-theory-agenda-setting' OR r1.target_entity_id='kg-theory-agenda-setting';
DELETE FROM kg_chunks WHERE entity_id='kg-theory-political-agenda';
DELETE FROM knowledge_entities WHERE id='kg-theory-political-agenda';

-- kg-theory-political-public-sphere -> kg-theory-public-sphere
UPDATE knowledge_relations SET source_entity_id='kg-theory-public-sphere' WHERE source_entity_id='kg-theory-political-public-sphere';
UPDATE knowledge_relations SET target_entity_id='kg-theory-public-sphere' WHERE target_entity_id='kg-theory-political-public-sphere';
DELETE r1 FROM knowledge_relations r1 JOIN knowledge_relations r2
  ON r1.source_entity_id=r2.source_entity_id AND r1.target_entity_id=r2.target_entity_id AND r1.relation_type=r2.relation_type AND r1.id>r2.id
 WHERE r1.source_entity_id='kg-theory-public-sphere' OR r1.target_entity_id='kg-theory-public-sphere';
DELETE FROM kg_chunks WHERE entity_id='kg-theory-political-public-sphere';
DELETE FROM knowledge_entities WHERE id='kg-theory-political-public-sphere';

-- kg-theory-political-spiral -> kg-theory-spiral-silence
UPDATE knowledge_relations SET source_entity_id='kg-theory-spiral-silence' WHERE source_entity_id='kg-theory-political-spiral';
UPDATE knowledge_relations SET target_entity_id='kg-theory-spiral-silence' WHERE target_entity_id='kg-theory-political-spiral';
DELETE r1 FROM knowledge_relations r1 JOIN knowledge_relations r2
  ON r1.source_entity_id=r2.source_entity_id AND r1.target_entity_id=r2.target_entity_id AND r1.relation_type=r2.relation_type AND r1.id>r2.id
 WHERE r1.source_entity_id='kg-theory-spiral-silence' OR r1.target_entity_id='kg-theory-spiral-silence';
DELETE FROM kg_chunks WHERE entity_id='kg-theory-political-spiral';
DELETE FROM knowledge_entities WHERE id='kg-theory-political-spiral';
