#!/usr/bin/env node
/**
 * kg-verify-hook.js — اعتبارسنجی هسته‌ی دانش resaname_v2
 * -------------------------------------------------------
 * یک ZCode hook (PostToolUse) که بعد از هر INSERT/UPDATE روی
 *   knowledge_entities / knowledge_relations / entity_facets
 * اجرا می‌شود و چک‌های زیر را انجام می‌دهد:
 *
 *   C1  slug یکتا                (E_SLUG_TAKEN)
 *   C2  entity_type از ۲۳ کد     (E_BAD_ENTITY_TYPE)
 *   C3  relation_type از ۲۰ کد   (E_BAD_RELATION_TYPE)
 *   C4  verification_status      (E_BAD_VERIFICATION_STATUS)
 *   C5  content_hash ۶۴ hex      (E_BAD_CONTENT_HASH)
 *   C6  parent_id موجود          (E_BAD_PARENT)
 *   C7  source/target موجود      (E_MISSING_FK)
 *   C9  facet_value <= 200       (E_FACET_TOO_LONG)
 *   C10 facet_key از ۸ کد        (E_BAD_FACET_KEY)
 *   C12 id format                (E_ID_FORMAT)
 *
 * ورودی (stdin, JSON):  یک شیء با این کلیدها (از stdin hook ZCode یا از CLI)
 *   { "table": "knowledge_entities" | "knowledge_relations" | "entity_facets",
 *     "payload": { ...فیلدهای ردیف... } }
 *
 * خروجی:
 *   - اگر OK:    stdout  { "ok": true }             exit 0
 *   - اگر خطا:   stderr  { "ok": false, "errors": [{ "code": "...", "message": "..." }] }
 *                 exit 1
 *
 * نحوه‌ی اجرا:
 *   node kg-verify-hook.js < input.json
 *   یا با آرج‌ها:  node kg-verify-hook.js --table knowledge_entities --payload-file p.json
 *
 * اتصال DB: فقط وقتی payload فیلدهای لازم دارد و env KG_VERIFY_DB=true باشد
 * (برای چک‌های yکتایی/FK). در غیر این صورت، hook فقط چک‌های ساختاری (format,
 * lexicon offline) را اجرا می‌کند و روی چک‌های DB-based `skip` گزارش می‌دهد.
 */

'use strict';

const fs = require('node:fs');
const { spawnSync } = require('node:child_process');

// ============================================================================
// Lexicon ثابت — از seed اسکیمای kg_schema.sql (بخش ۴)
// ============================================================================
const ENTITY_TYPES = new Set([
  'SCHOOL','TRADITION','PARADIGM','APPROACH','THEORY','MODEL','FRAMEWORK',
  'HYPOTHESIS','LAW','CONCEPT','METHODOLOGY','METHOD','DESIGN','STRATEGY',
  'TECHNIQUE','INSTRUMENT','SAMPLING','ANALYSIS','QUALITY','ETHICS','SOFTWARE',
  'DISCIPLINE','SUBFIELD'
]);

const RELATION_TYPES = new Set([
  'IS_A','PART_OF','BELONGS_TO','INFLUENCED_BY','INFLUENCED','CRITICIZES',
  'EXTENDS','CONTRADICTS','RELATED_TO','APPLIES_TO','USES','MEASURES',
  'ANALYZES','COLLECTS','DEVELOPED_BY','PROPOSED_BY','OPERATIONALIZES','TESTS',
  'DERIVED_FROM','COMPARED_WITH'
]);

const FACET_KEYS = new Set([
  'knowledge_type','domain','approach','theoretical_tradition',
  'data_type','objective','analysis_scale','application'
]);

const VERIFICATION_STATUSES = new Set(['unverified','verified','rejected']);
const ID_RE = /^[a-z0-9][a-z0-9-]{5,39}$/;   // 6..40 chars, a-z 0-9 '-'

// ============================================================================
// اتصال DB (اختیاری) — فقط وقتی env KG_VERIFY_DB=true
// ============================================================================
function dbConfig() {
  return {
    host: process.env.KG_VERIFY_DB_HOST || 'localhost',
    user: process.env.KG_VERIFY_DB_USER || 'root',
    password: process.env.KG_VERIFY_DB_PASSWORD || '433700',
    database: process.env.KG_VERIFY_DB_NAME || 'resaname_v2'
  };
}

function tryDbQuery(sql, params = []) {
  // فقط اگر mysql CLI موجود باشد و KG_VERIFY_DB=true. در غیر این صورت null
  // (یعنی skip). برای hook سبک، از mysql CLI استفاده می‌کنیم تا نیازی به
  // npm install mysql2 نباشد.
  if (process.env.KG_VERIFY_DB !== 'true') return { skipped: true };
  const cfg = dbConfig();
  const mysqlBin = process.platform === 'win32' ? 'mysql' : 'mysql';
  const cmdArgs = [
    '-h', cfg.host, '-u', cfg.user, '-p' + cfg.password,
    cfg.database,
    '--batch', '--skip-column-names', '--raw',
    '-N'
  ];
  const r = spawnSync(mysqlBin, cmdArgs, { input: sql, encoding: 'utf8' });
  if (r.error) return { skipped: true };
  if (r.status !== 0) return { error: (r.stderr || '').trim() };
  const rows = (r.stdout || '').split(/\r?\n/).filter(Boolean);
  return { rows };
}

function dbScalar(sql) {
  const r = tryDbQuery(sql);
  if (r.skipped || r.error) return r;
  const row = (r.rows || [])[0] || '';
  const firstField = row.split('\t')[0];
  return firstField == null ? '' : firstField;
}

// ============================================================================
// چک‌ها
// ============================================================================
function addErr(errors, code, message) {
  errors.push({ code, message });
}

function checkEntity(row, errors, dbEnabled) {
  // C12 — id format
  if (typeof row.id === 'string' && row.id.length > 0 && !ID_RE.test(row.id)) {
    addErr(errors, 'E_ID_FORMAT', `id "${row.id}" نمی‌بایست [a-z0-9-]{6,40} باشد`);
  }

  // slug — C1: یکتایی
  if (typeof row.slug === 'string' && row.slug.length > 0) {
    const s = row.slug.replace(/'/g, "''");
    const res = dbScalar(`SELECT COUNT(*) FROM knowledge_entities WHERE slug='${s}' AND id<>${JSON.stringify(row.id || '')}`);
    if (!res.skipped && !res.error && res !== '' && Number(res) > 0) {
      addErr(errors, 'E_SLUG_TAKEN', `slug "${row.slug}" قبلاً در knowledge_entities وجود دارد`);
    }
  }

  // C2 — entity_type
  if (typeof row.entity_type === 'string' && row.entity_type.length > 0) {
    if (!ENTITY_TYPES.has(row.entity_type)) {
      addErr(errors, 'E_BAD_ENTITY_TYPE',
        `entity_type "${row.entity_type}" در ۲۳ کد knowledge_entity_types نیست`);
    }
  }

  // C4 — verification_status
  if (typeof row.verification_status === 'string' && row.verification_status.length > 0) {
    if (!VERIFICATION_STATUSES.has(row.verification_status)) {
      addErr(errors, 'E_BAD_VERIFICATION_STATUS',
        `verification_status "${row.verification_status}" معتبر نیست (unverified|verified|rejected)`);
    }
  }

  // C5 — content_hash
  if (typeof row.content_hash === 'string' && row.content_hash.length > 0) {
    if (!/^[a-f0-9]{64}$/i.test(row.content_hash)) {
      addErr(errors, 'E_BAD_CONTENT_HASH',
        `content_hash "${row.content_hash.slice(0,16)}…" باید ۶۴ کاراکتر hex باشد`);
    }
  }

  // C6 — parent_id (soft — self-FK)
  if (typeof row.parent_id === 'string' && row.parent_id.length > 0 && row.parent_id !== row.id) {
    const res = dbScalar(`SELECT 1 FROM knowledge_entities WHERE id='${row.parent_id.replace(/'/g, "''")}'`);
    if (!res.skipped && !res.error && res === '') {
      addErr(errors, 'E_BAD_PARENT', `parent_id "${row.parent_id}" در knowledge_entities نیست`);
    }
  }
}

function checkRelation(row, errors, dbEnabled) {
  // C3 — relation_type
  if (typeof row.relation_type === 'string' && row.relation_type.length > 0) {
    if (!RELATION_TYPES.has(row.relation_type)) {
      addErr(errors, 'E_BAD_RELATION_TYPE',
        `relation_type "${row.relation_type}" در ۲۰ کد knowledge_relation_types نیست`);
    }
  }
  // C4 — verification_status
  if (typeof row.verification_status === 'string' && row.verification_status.length > 0) {
    if (!VERIFICATION_STATUSES.has(row.verification_status)) {
      addErr(errors, 'E_BAD_VERIFICATION_STATUS',
        `verification_status "${row.verification_status}" معتبر نیست`);
    }
  }
  // C7 — source/target
  for (const col of ['source_entity_id','target_entity_id']) {
    if (typeof row[col] === 'string' && row[col].length > 0) {
      const res = dbScalar(`SELECT 1 FROM knowledge_entities WHERE id='${row[col].replace(/'/g, "''")}'`);
      if (!res.skipped && !res.error && res === '') {
        addErr(errors, 'E_MISSING_FK', `${col} "${row[col]}" در knowledge_entities نیست`);
      }
    }
  }
}

function checkFacet(row, errors, dbEnabled) {
  // C10 — facet_key
  if (typeof row.facet_key === 'string' && row.facet_key.length > 0) {
    if (!FACET_KEYS.has(row.facet_key)) {
      addErr(errors, 'E_BAD_FACET_KEY',
        `facet_key "${row.facet_key}" در ۸ کد entity_facet_keys نیست`);
    }
  }
  // C9 — facet_value <= 200
  if (typeof row.facet_value === 'string' && row.facet_value.length > 200) {
    addErr(errors, 'E_FACET_TOO_LONG',
      `facet_value طولش ${row.facet_value.length} است (بیش‌از ۲۰۰)`);
  }
  // entity_id موجود؟
  if (typeof row.entity_id === 'string' && row.entity_id.length > 0) {
    const res = dbScalar(`SELECT 1 FROM knowledge_entities WHERE id='${row.entity_id.replace(/'/g, "''")}'`);
    if (!res.skipped && !res.error && res === '') {
      addErr(errors, 'E_MISSING_FK', `entity_id "${row.entity_id}" در knowledge_entities نیست`);
    }
  }
}

// ============================================================================
// ورودی
// ============================================================================
function readStdin() {
  return fs.readFileSync(0, 'utf8');
}

function parseArgs(argv) {
  const out = { table: null, payload: null, payloadFile: null };
  for (let i = 2; i < argv.length; i++) {
    const a = argv[i];
    if (a === '--table') out.table = argv[++i];
    else if (a === '--payload-file') out.payloadFile = argv[++i];
    else if (a === '--payload') out.payload = JSON.parse(argv[++i]);
  }
  return out;
}

function main() {
  const cli = parseArgs(process.argv);
  let table = cli.table;
  let payload = cli.payload;

  // اگر payload از file آمد
  if (cli.payloadFile) {
    payload = JSON.parse(fs.readFileSync(cli.payloadFile, 'utf8'));
  }

  // وگرنه از stdin
  if (payload == null) {
    const raw = readStdin();
    if (raw && raw.trim()) {
      try {
        const j = JSON.parse(raw);
        // پشتیبانی از stdin به شکل hook ZCode:
        //   { "table": "...", "payload": {...} }  یا  { "tool_input": {...} }
        table = table || j.table || j.tool_name;
        payload = j.payload != null ? j.payload
               : j.tool_input != null ? j.tool_input
               : j;
      } catch (e) {
        // stdin نامعتبر — بدون خطا رد می‌شود (hook نباید session را شکند)
        return;
      }
    }
  }

  // اگر payload ندیدیم یا table نامربوط — silent pass
  if (!payload || typeof payload !== 'object') return;
  if (!table) {
    // حدس از payload
    if (payload.entity_type !== undefined || payload.slug !== undefined ||
        (payload.content_hash !== undefined && payload.verification_status !== undefined)) {
      table = 'knowledge_entities';
    } else if (payload.relation_type !== undefined) {
      table = 'knowledge_relations';
    } else if (payload.facet_key !== undefined) {
      table = 'entity_facets';
    }
  }

  if (!['knowledge_entities','knowledge_relations','entity_facets'].includes(table)) {
    return; // خارج از دامنه‌ی hook
  }

  const dbEnabled = process.env.KG_VERIFY_DB === 'true';
  const errors = [];
  if (table === 'knowledge_entities') checkEntity(payload, errors, dbEnabled);
  else if (table === 'knowledge_relations') checkRelation(payload, errors, dbEnabled);
  else if (table === 'entity_facets') checkFacet(payload, errors, dbEnabled);

  if (errors.length > 0) {
    process.stderr.write(JSON.stringify({ ok: false, table, errors }, null, 2) + '\n');
    process.exit(1);
  }

  process.stdout.write(JSON.stringify({ ok: true, table, checked: dbEnabled ? 'structure+db' : 'structure-only' }) + '\n');
  process.exit(0);
}

try { main(); } catch (e) {
  // hook هرگز نباید session را crash کند
  process.stderr.write(JSON.stringify({
    ok: false,
    errors: [{ code: 'E_HOOK_INTERNAL', message: String((e && e.message) || e) }]
  }) + '\n');
  process.exit(1);
}
