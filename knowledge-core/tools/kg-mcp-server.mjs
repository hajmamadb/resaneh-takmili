#!/usr/bin/env node
/**
 * kg-mcp-server.mjs — MCP server هسته‌ی دانش resaname_v2
 * ======================================================
 * Transport: stdio (JSON-RPC 2.0, newline-delimited).
 * Protocol:  2025-06-18 (with 2024-11-05 fallback).
 *
 * Tools:
 *   kg_search(query, entity_type?, limit?)
 *   kg_get_entity(id)
 *   kg_add_entity(entity_json)          -> validates via kg-verify-hook.js
 *   kg_add_relation(source_id, target_id, relation_type, description?)
 *   kg_list_types()
 *   kg_stats()
 *
 * Env:
 *   KG_DB_HOST     (default: localhost)
 *   KG_DB_USER     (default: root)
 *   KG_DB_PASSWORD (default: 433700)
 *   KG_DB_NAME     (default: resaname_v2)
 *   KG_VERIFY_DB   (default: true — pass to hook as KG_VERIFY_DB=true)
 *
 * اجرا:  node kg-mcp-server.mjs
 */

import mysql from 'mysql2/promise';
import { createHash } from 'node:crypto';
import { spawn } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const HOOK_PATH = path.join(__dirname, 'kg-verify-hook.js');

const DB = {
  host: process.env.KG_DB_HOST || 'localhost',
  user: process.env.KG_DB_USER || 'root',
  password: process.env.KG_DB_PASSWORD || '433700',
  database: process.env.KG_DB_NAME || 'resaname_v2'
};

const PROTOCOL_VERSION = '2025-06-18';
const SERVER_INFO = { name: 'kg-mcp-server', version: '1.0.0' };

// ---------------------------------------------------------------------------
// Connection pool (lazy)
// ---------------------------------------------------------------------------
let _pool = null;
function pool() {
  if (!_pool) {
    _pool = mysql.createPool({
      host: DB.host, user: DB.user, password: DB.password, database: DB.database,
      waitForConnections: true, connectionLimit: 4, charset: 'utf8mb4_unicode_ci',
      connectTimeout: 8000, acquireTimeout: 10000
    });
  }
  return _pool;
}

// ---------------------------------------------------------------------------
// content_hash — مطابق الگوریتم اسکیل kg-ingest
// ---------------------------------------------------------------------------
const HASH_FIELDS = [
  'entity_type','title_fa','title_en','slug','abstract','description',
  'historical_background','philosophical_foundations','key_propositions',
  'key_figures','origin_period','geographical_origin','related_disciplines',
  'applications','strengths','limitations','criticisms','references','status'
];
function computeContentHash(entity) {
  const h = createHash('sha256');
  for (const f of HASH_FIELDS) h.update(String(entity[f] ?? '') + '|');
  return h.digest('hex');
}

// ---------------------------------------------------------------------------
// JSON-ify complex columns (key_propositions, related_disciplines, references)
// ---------------------------------------------------------------------------
function toDbValue(v, kind) {
  if (v == null) return null;
  if (kind === 'json' && typeof v === 'object') return JSON.stringify(v);
  if (kind === 'list' && Array.isArray(v)) return JSON.stringify(v);
  return String(v);
}

// ---------------------------------------------------------------------------
// Hook runner
// ---------------------------------------------------------------------------
function runHook(table, payload) {
  return new Promise((resolve) => {
    const p = spawn('node', [HOOK_PATH], {
      env: {
        ...process.env,
        KG_VERIFY_DB: 'true',
        KG_VERIFY_DB_HOST: DB.host,
        KG_VERIFY_DB_USER: DB.user,
        KG_VERIFY_DB_PASSWORD: DB.password,
        KG_VERIFY_DB_NAME: DB.database
      },
      stdio: ['pipe', 'pipe', 'pipe']
    });
    let out = '', err = '';
    p.stdout.on('data', d => out += d);
    p.stderr.on('data', d => err += d);
    p.on('error', (e) => resolve({ ok: false, exit: -1, errors: [{ code: 'E_SPAWN', message: String(e) }] }));
    p.on('close', (code) => {
      let j = null;
      try { j = JSON.parse(err || out || '{}'); } catch {}
      if (code === 0 && (!j || j.ok !== false)) resolve({ ok: true, exit: code });
      else resolve({ ok: false, exit: code, errors: (j && j.errors) || [{ code: 'E_UNKNOWN', message: (err || out || 'unknown').slice(0, 500) }] });
    });
    p.stdin.end(JSON.stringify({ table, payload }));
  });
}

// ---------------------------------------------------------------------------
// Tool implementations
// ---------------------------------------------------------------------------
async function kgSearch({ query, entity_type, limit }) {
  const lim = Math.min(Math.max(parseInt(limit ?? 20, 10) || 20, 1), 200);
  const like = `%${String(query ?? '').trim()}%`;
  const conds = [
    'title_fa LIKE ?', 'title_en LIKE ?', 'slug LIKE ?', 'abstract LIKE ?'
  ];
  const params = [like, like, like, like];
  if (entity_type) { conds.push('entity_type = ?'); params.push(entity_type); }
  const sql = `SELECT id, title_fa, title_en, slug, entity_type, status,
                      verification_status, LEFT(abstract, 200) AS abstract_preview
               FROM knowledge_entities
               WHERE ${conds.join(' OR ')}
               ORDER BY updated_at DESC
               LIMIT ${lim}`;
  const [rows] = await pool().query(sql, params);
  return { count: rows.length, results: rows };
}

async function kgGetEntity({ id }) {
  const [e] = await pool().query(
    `SELECT * FROM knowledge_entities WHERE id = ? LIMIT 1`, [id]);
  if (!e.length) return { found: false, id };
  const ent = e[0];
  // Parse JSON-ish columns
  for (const f of ['key_propositions','related_disciplines','references']) {
    if (typeof ent[f] === 'string') {
      try { ent[f] = JSON.parse(ent[f]); } catch {}
    }
  }
  const [facets] = await pool().query(
    `SELECT facet_key, facet_value, sort_order FROM entity_facets
     WHERE entity_id = ? ORDER BY sort_order`, [id]);
  const [out] = await pool().query(
    `SELECT source_entity_id, relation_type, description, confidence, verification_status
     FROM knowledge_relations WHERE source_entity_id = ?`, [id]);
  const [inc] = await pool().query(
    `SELECT target_entity_id, relation_type, description, confidence, verification_status
     FROM knowledge_relations WHERE target_entity_id = ?`, [id]);
  const [links] = await pool().query(
    `SELECT content_id, link_type FROM entity_content_links WHERE entity_id = ?`, [id]);

  // Resolve titles of neighbors
  const allIds = [...new Set([...out.map(r => r.target_entity_id), ...inc.map(r => r.source_entity_id)])];
  let titles = {};
  if (allIds.length) {
    const [t] = await pool().query(
      `SELECT id, title_fa, title_en FROM knowledge_entities WHERE id IN (?)`, [allIds]);
    titles = Object.fromEntries(t.map(r => [r.id, { title_fa: r.title_fa, title_en: r.title_en }]));
  }
  const withTitles = (rows, otherIdCol) => rows.map(r => ({
    ...r,
    other: titles[r[otherIdCol]] || { id: r[otherIdCol] }
  }));

  return {
    found: true,
    entity: ent,
    facets: facets,
    outgoing: withTitles(out, 'target_entity_id'),
    incoming: withTitles(inc, 'source_entity_id'),
    content_links: links,
    relation_count: out.length + inc.length
  };
}

async function kgAddEntity({ entity }) {
  if (!entity || typeof entity !== 'object') {
    return { ok: false, errors: [{ code: 'E_INPUT', message: 'entity object is required' }] };
  }
  const e = { ...entity };

  // Defaults
  if (!e.id) e.id = 'ke-' + (e.slug || (e.title_fa || e.title_en || 'e').toString().toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, ''));
  if (!e.slug) e.slug = (e.title_en || e.title_fa || e.id)
    .toString().toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '').slice(0, 200);
  if (!e.status) e.status = 'draft';
  if (!e.verification_status) e.verification_status = 'unverified';

  // Compute content_hash
  const hash = computeContentHash(e);
  e.content_hash = hash;

  // Run hook for structural + DB checks
  const hookRes = await runHook('knowledge_entities', e);
  if (!hookRes.ok) return { ok: false, errors: hookRes.errors };

  // Prepare row
  const row = {
    id: e.id, title_fa: e.title_fa || '(fa)', title_en: e.title_en ?? null,
    slug: e.slug, entity_type: e.entity_type, parent_id: e.parent_id ?? null,
    abstract: e.abstract ?? null, description: e.description ?? null,
    historical_background: e.historical_background ?? null,
    philosophical_foundations: e.philosophical_foundations ?? null,
    key_propositions: toDbValue(e.key_propositions, 'json'),
    key_figures: e.key_figures ?? null,
    origin_period: e.origin_period ?? null,
    geographical_origin: e.geographical_origin ?? null,
    related_disciplines: toDbValue(e.related_disciplines, 'list'),
    applications: e.applications ?? null, strengths: e.strengths ?? null,
    limitations: e.limitations ?? null, criticisms: e.criticisms ?? null,
    references: toDbValue(e.references, 'list'),
    status: e.status, verification_status: e.verification_status,
    content_hash: e.content_hash
  };
  const cols = Object.keys(row);
  const ph = cols.map(c => `?`).join(',');
  // backticks روی هر دو طرف — `references` کلمه‌ی رزرو MySQL است
  const upd = cols.filter(c => c !== 'id').map(c => `\`${c}\` = VALUES(\`${c}\`)`).join(', ');
  const sql = `INSERT INTO knowledge_entities (${cols.map(c => '`' + c + '`').join(',')})
               VALUES (${ph}) ON DUPLICATE KEY UPDATE ${upd}`;
  const con = await pool().getConnection();
  try {
    await con.beginTransaction();
    const [r] = await con.query(sql, Object.values(row));
    // Facets
    if (e.facets && typeof e.facets === 'object') {
      const items = Object.entries(e.facets).filter(([k, v]) => v != null && String(v).length > 0);
      for (let i = 0; i < items.length; i++) {
        const [k, v] = items[i];
        await con.query(
          `INSERT INTO entity_facets (entity_id, facet_key, facet_value, sort_order)
           VALUES (?,?,?,?) ON DUPLICATE KEY UPDATE sort_order = VALUES(sort_order)`,
          [e.id, k, String(v).slice(0, 200), i + 1]);
      }
    }
    await con.commit();
    return { ok: true, id: e.id, inserted: r.affectedRows > 0, content_hash: hash };
  } catch (err) {
    await con.rollback();
    return { ok: false, errors: [{ code: 'E_DB', message: String(err.message || err) }] };
  } finally {
    con.release();
  }
}

async function kgAddRelation({ source_id, target_id, relation_type, description, confidence, verification_status }) {
  if (!source_id || !target_id || !relation_type) {
    return { ok: false, errors: [{ code: 'E_INPUT', message: 'source_id, target_id, relation_type are required' }] };
  }
  const payload = {
    source_entity_id: source_id, target_entity_id: target_id,
    relation_type, description: description ?? null,
    confidence: confidence ?? 0.8, verification_status: verification_status || 'unverified'
  };
  const hookRes = await runHook('knowledge_relations', payload);
  if (!hookRes.ok) return { ok: false, errors: hookRes.errors };

  const relId = 'kr-' + createHash('sha1')
    .update(source_id + '|' + target_id + '|' + relation_type).digest('hex').slice(0, 8);
  const sql = `INSERT INTO knowledge_relations
                (id, source_entity_id, target_entity_id, relation_type,
                 description, confidence, verification_status, extracted_by)
               VALUES (?,?,?,?,?,?,?,?)
               ON DUPLICATE KEY UPDATE description = VALUES(description),
                confidence = VALUES(confidence), verification_status = VALUES(verification_status)`;
  const [r] = await pool().query(sql, [
    relId, source_id, target_id, relation_type,
    description ?? null, confidence ?? 0.8, verification_status || 'unverified', 'kg-mcp-server'
  ]);
  return { ok: true, id: relId, affected: r.affectedRows };
}

async function kgListTypes() {
  const [entityTypes] = await pool().query(
    `SELECT type_code, content_type_key, is_canonical, display_fa, display_en, domain_group, sort_order
     FROM knowledge_entity_types ORDER BY sort_order`);
  const [relationTypes] = await pool().query(
    `SELECT type_code, legacy_code, code_fa, code_en, domain, is_bidirectional, sort_order
     FROM knowledge_relation_types ORDER BY sort_order`);
  const [facetKeys] = await pool().query(
    `SELECT facet_key, label_fa, label_en, sort_order FROM entity_facet_keys ORDER BY sort_order`);
  return { entity_types: entityTypes, relation_types: relationTypes, facet_keys: facetKeys };
}

async function kgStats() {
  const [byType] = await pool().query(
    `SELECT entity_type, verification_status, COUNT(*) AS n
     FROM knowledge_entities GROUP BY entity_type, verification_status
     ORDER BY entity_type, verification_status`);
  const [relByType] = await pool().query(
    `SELECT relation_type, COUNT(*) AS n
     FROM knowledge_relations GROUP BY relation_type ORDER BY relation_type`);
  const [totals] = await pool().query(`
    SELECT
      (SELECT COUNT(*) FROM knowledge_entities) AS entities,
      (SELECT COUNT(*) FROM knowledge_relations) AS relations,
      (SELECT COUNT(*) FROM entity_facets) AS facets,
      (SELECT COUNT(*) FROM knowledge_scholars) AS scholars,
      (SELECT COUNT(*) FROM knowledge_works) AS works,
      (SELECT COUNT(*) FROM entity_content_links) AS content_links
  `);
  return { totals: totals[0], by_entity_type: byType, by_relation_type: relByType };
}

// ---------------------------------------------------------------------------
// Tool schemas
// ---------------------------------------------------------------------------
const TOOLS = [
  {
    name: 'kg_search',
    description: 'جست‌وجوی LIKE در knowledge_entities (title_fa/title_en/slug/abstract). entity_type و limit اختیاری.',
    inputSchema: {
      type: 'object',
      properties: {
        query: { type: 'string', description: 'کلیدواژه‌ی جست‌وجو' },
        entity_type: { type: 'string', description: 'فیلتر بر اساس entity_type (مثلا SCHOOL)' },
        limit: { type: 'integer', default: 20, description: 'حداکثر ۲۰۰' }
      },
      required: ['query']
    }
  },
  {
    name: 'kg_get_entity',
    description: 'دریافت کامل یک موجودیت دانشی با facets، روابط (ورودی/خروجی) و content_links.',
    inputSchema: {
      type: 'object',
      properties: { id: { type: 'string', description: 'id موجودیت (مثلا ke-frankfurt-school)' } },
      required: ['id']
    }
  },
  {
    name: 'kg_add_entity',
    description: 'درج/به‌روزرسانی موجودیت دانشی (idempotent). entity = JSON با فیلدهای ۲۲-ستونی + facets. content_hash خودکار محاسبه و hook اجرا می‌شود.',
    inputSchema: {
      type: 'object',
      properties: {
        entity: {
          type: 'object',
          description: 'JSON موجودیت (id, title_fa, slug, entity_type, abstract, ..., facets)'
        }
      },
      required: ['entity']
    }
  },
  {
    name: 'kg_add_relation',
    description: 'درج/به‌روزرسانی رابطه‌ی دانش. relation_type باید از ۲۰ کد canonical باشد.',
    inputSchema: {
      type: 'object',
      properties: {
        source_id: { type: 'string' },
        target_id: { type: 'string' },
        relation_type: { type: 'string', description: 'IS_A | PART_OF | ...' },
        description: { type: 'string' },
        confidence: { type: 'number', default: 0.8 },
        verification_status: { type: 'string', enum: ['unverified', 'verified', 'rejected'], default: 'unverified' }
      },
      required: ['source_id', 'target_id', 'relation_type']
    }
  },
  {
    name: 'kg_list_types',
    description: 'فهرست ۲۳ entity_type، ۲۰ relation_type و ۸ facet_key از seed.',
    inputSchema: { type: 'object', properties: {} }
  },
  {
    name: 'kg_stats',
    description: 'آمار: تعداد موجودیت‌ها به تفکیک نوع/وضعیت، روابط به تفکیک نوع، totals.',
    inputSchema: { type: 'object', properties: {} }
  }
];

// ---------------------------------------------------------------------------
// JSON-RPC dispatcher
// ---------------------------------------------------------------------------
const dispatch = {
  initialize: (params) => ({
    protocolVersion: params?.protocolVersion === PROTOCOL_VERSION ? PROTOCOL_VERSION : PROTOCOL_VERSION,
    capabilities: { tools: { listChanged: true } },
    serverInfo: SERVER_INFO,
    instructions: 'Knowledge graph core for resaname_v2. Use kg_* tools to query/ingest entities and relations.'
  }),
  'tools/list': () => ({ tools: TOOLS }),
  'tools/call': async (params) => {
    const name = params?.name;
    const args = params?.arguments || {};
    try {
      switch (name) {
        case 'kg_search':      return await kgSearch(args);
        case 'kg_get_entity':  return await kgGetEntity(args);
        case 'kg_add_entity':  return await kgAddEntity(args);
        case 'kg_add_relation':return await kgAddRelation(args);
        case 'kg_list_types':  return await kgListTypes();
        case 'kg_stats':       return await kgStats();
        default: throw new Error(`Unknown tool: ${name}`);
      }
    } catch (err) {
      return { ok: false, errors: [{ code: 'E_TOOL', message: String(err.message || err) }] };
    }
  },
  'ping': () => ({})
};

// ---------------------------------------------------------------------------
// stdio loop
// ---------------------------------------------------------------------------
function write(msg) {
  process.stdout.write(JSON.stringify(msg) + '\n');
}
function writeResult(id, result) { if (id != null) write({ jsonrpc: '2.0', id, result }); }
function writeError(id, code, message) { if (id != null) write({ jsonrpc: '2.0', id, error: { code, message } }); }

let buffer = '';
process.stdin.setEncoding('utf8');
process.stdin.on('data', (chunk) => {
  buffer += chunk;
  let idx;
  while ((idx = buffer.indexOf('\n')) >= 0) {
    const line = buffer.slice(0, idx).trim();
    buffer = buffer.slice(idx + 1);
    if (!line) continue;
    let msg;
    try { msg = JSON.parse(line); } catch { writeError(null, -32700, 'Parse error'); continue; }
    handleMessage(msg).catch(err => {
      // لاگ خطای داخلی روی stderr (stdout فقط JSON-RPC)
      process.stderr.write(`[kg-mcp-server] internal: ${err.message}\n`);
    });
  }
});
process.stdin.on('end', () => process.exit(0));

async function handleMessage(msg) {
  const { id, method, params } = msg;
  if (method == null) return; // notification
  if (method.startsWith('notifications/')) return;
  const fn = dispatch[method];
  if (!fn) { writeError(id, -32601, `Method not found: ${method}`); return; }
  try {
    const result = await fn(params);
    writeResult(id, result);
  } catch (err) {
    writeError(id, -32603, String(err.message || err));
  }
}
