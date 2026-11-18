/* ============================================================
   هسته‌ی دانش رسانامه — SPA (hash router, static data bundles)
   ============================================================ */
(function () {
  "use strict";

  const DATA = './data/';
  const cache = {};

  // ---------- helpers ----------
  const FA_DIGITS = '۰۱۲۳۴۵۶۷۸۹';
  function faDigits(s) {
    if (s === null || s === undefined) return '';
    return String(s).replace(/[0-9]/g, (d) => FA_DIGITS[+d]);
  }
  function esc(s) {
    if (s === null || s === undefined) return '';
    return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }
  async function jget(name) {
    if (cache[name]) return cache[name];
    // live bridge (local dev) first — reads MySQL on demand; static bundle as fallback
    try {
      const r = await fetch('/api/data/' + name, { cache: 'no-store' });
      if (!r.ok) throw new Error('live ' + r.status);
      cache[name] = await r.json();
      window.__live = true;
      revealLive();
      return cache[name];
    } catch (_) { /* fall through to static */ }
    window.__static = true;
    revealStatic('');
    const r2 = await fetch(DATA + name, { cache: 'force-cache' });
    if (!r2.ok) throw new Error('data ' + name + ' -> ' + r2.status);
    cache[name] = await r2.json();
    return cache[name];
  }
  function slugFile(type) { return (type || '').toLowerCase() + '.json'; }

  // char-by-char 1:1 normalization (preserves length so indices map back to the original text)
  function normName(s) {
    return String(s || '')
      .replace(/[\u064a\u0649]/g, 'ی')
      .replace(/\u0643/g, 'ک')
      .replace(/[\u200c\u200d\u200e\u200f]/g, ' ')
      .replace(/[-–—\/·]/g, ' ')
      .toLowerCase();
  }
  const GENERIC_LEAD = 'نظریه|مدل|چارچوب نظری|چارچوب|مفهوم|پارادایم|روش‌شناسی|روش|اصل|قانون|سنت|مکتب|حوزه|زیرحوزه|شاخص|سازه|گزاره|متغیر|رشته|استراتژی|فرضیه';
  const GENERIC_TAIL = 'theory|model|framework|hypothesis|law|concept|paradigm|methodology|method|strategy|indicator|construct|proposition|variable|school|tradition|discipline|subfield|approach';
  function nameVariants(nm) {
    const full = normName(nm).trim();
    const vars = [full];
    const lead = full.match(new RegExp('^(?:' + GENERIC_LEAD + ')\\s+(.+)$'));
    if (lead) vars.push(lead[1].trim());
    const tail = full.match(new RegExp('^(.+?)\\s+(?:' + GENERIC_TAIL + ')$'));
    if (tail) vars.push(tail[1].trim());
    return vars.filter((v) => v.length >= 2);
  }
  function buildNameIndex(dir) {
    const idx = {};
    (dir || []).forEach((d) => {
      if (!d.slug && !d.code) return;
      const target = { slug: d.slug || d.code, type: d.type };
      [d.fa, d.en].forEach((nm) => {
        nameVariants(nm).forEach((k) => { if (!idx[k]) idx[k] = target; });
      });
    });
    return idx;
  }
  // scan text left-to-right; longest name match wins; matched names become entity links
  function linkifyNames(text, idx, keys) {
    const s = String(text);
    const norm = normName(s);
    let out = '', i = 0;
    while (i < norm.length) {
      let hit = null;
      if (/[\p{L}\p{N}]/u.test(norm[i])) {
        for (const k of keys) {
          if (k.length < 2 || !norm.startsWith(k, i)) continue;
          const after = norm[i + k.length] || '';
          if (after && /[\p{L}\p{N}]/u.test(after)) continue;
          hit = k; break;
        }
      }
      if (hit) {
        const ent = idx[hit];
        const label = s.slice(i, i + hit.length);
        out += '<a class="fieldlink entlink" href="#/' + ent.type.toLowerCase() + '/' + encodeURIComponent(ent.slug) + '" title="مشاهده‌ی موجودیت">' + esc(faDigits(label)) + '</a>';
        i += hit.length;
      } else {
        out += esc(s[i]); i++;
      }
    }
    return out;
  }

  const FAM_VAR = {
    THEORETICAL_SYSTEM: 'var(--fam-system)',
    KNOWLEDGE_STRUCTURE: 'var(--fam-structure)',
    SCIENTIFIC_DOMAIN: 'var(--fam-domain)',
    RESEARCH_METHODOLOGY: 'var(--fam-method)',
    RESEARCH_ACTIVITY: 'var(--fam-activity)',
    RESEARCH_RESOURCE: 'var(--fam-resource)',
    INTELLECTUAL_AGENT: 'var(--fam-agent)',
    SCIENTIFIC_ARGUMENTATION: 'var(--fam-activity)',
  };
  const famColor = (fam) => FAM_VAR[fam] || 'var(--site-accent)';

  const SW_FA = { draft: 'پیش‌نویس', in_review: 'در بازبینی', approved: 'تأییدشده', published: 'منتشرشده', archived: 'بایگانی‌شده' };
  const SS_FA = { unassessed: 'سنجیده‌نشده', supported: 'پشتیبانی‌شده', partially_supported: 'پشتیبانی‌شده‌ی جزئی', contested: 'در مناقشه', refuted: 'نقض‌شده', not_applicable: 'نامرتبط' };
  const SL_FA = { active: 'فعال', historical: 'تاریخی', superseded: 'جانشین‌شده', deprecated: 'منسوخ', unknown: 'نامشخص' };
  const swColor = (v) => ({ draft: 'var(--site-gold)', in_review: 'var(--site-accent-2)', approved: 'var(--site-ok)', published: 'var(--site-accent)', archived: 'var(--site-muted)' }[v] || 'var(--site-muted)');
  const ssColor = (v) => ({ unassessed: 'var(--site-muted)', supported: 'var(--site-ok)', partially_supported: 'var(--site-gold)', contested: 'var(--site-warn)', refuted: 'var(--site-warn)', not_applicable: 'var(--site-muted)' }[v] || 'var(--site-muted)');
  const slColor = (v) => ({ active: 'var(--site-ok)', historical: 'var(--site-accent-2)', superseded: 'var(--site-gold)', deprecated: 'var(--site-warn)', unknown: 'var(--site-muted)' }[v] || 'var(--site-muted)');

  const CONTENT_SECTIONS = [
    ['summary', 'خلاصه'], ['core_logic', 'منطق هسته‌ای'], ['abstract', 'تعریف'],
    ['definition', 'تعریف'], ['main_problem', 'مسئله‌ی اصلی'], ['key_concepts', 'مفاهیم کلیدی'],
    ['constructs', 'سازه‌ها'], ['mechanism', 'سازوکار'], ['assumptions', 'پیش‌فرض‌ها'],
    ['critiques', 'نقدها'], ['critique', 'نقد'], ['limitations', 'محدودیت‌ها'],
    ['applications', 'کاربردها'], ['history', 'تاریخچه'], ['evolution', 'تکامل'],
    ['studies', 'مطالعات و پژوهش‌ها'], ['research_guide', 'راهنمای پژوهش'],
    ['detailed_analysis', 'تحلیل تفصیلی'], ['example', 'مثال'], ['principles', 'اصول'],
    ['bio', 'درباره'], ['academic_career', 'سابقه‌ی علمی'], ['nationality', 'تابعیت'],
    ['main_theory', 'نظریه‌ی اصلی'], ['importance', 'اهمیت'], ['field', 'حوزه‌ی تخصصی'],
  ];

  function renderText(v) {
    if (v === null || v === undefined || v === '') return '';
    if (typeof v === 'number') return esc(faDigits(v));
    if (typeof v === 'object') {
      if (Array.isArray(v)) return '<ul>' + v.map((x) => '<li>' + esc(faDigits(x)) + '</li>').join('') + '</ul>';
      return '<p class="txt">' + esc(JSON.stringify(v)) + '</p>';
    }
    const s = String(v);
    const lines = s.split('\n').filter((l) => l.trim() !== '');
    const bulletish = lines.filter((l) => /^\s*(•|-|\u2022|\d+[\.\)\u066b\u064b]|[\u200a-])/.test(l) || /^\s*\d+[\.\)\u066b]/.test(l)).length;
    if (lines.length >= 2 && bulletish >= Math.min(2, Math.ceil(lines.length * 0.4))) {
      const items = lines.map((l) => l.replace(/^\s*(•|-|\u2022)\s*/, '').replace(/^\s*\d+[\.\)\u066b]\s*/, ''));
      return '<ul>' + items.map((li) => '<li>' + esc(faDigits(li)) + '</li>').join('') + '</ul>';
    }
    return '<p class="txt">' + esc(faDigits(s)) + '</p>';
  }

  function qBadge(q) {
    if (q === null || q === undefined) return '';
    q = +q;
    let cls = 'low';
    if (q >= 90) cls = '';
    else if (q >= 70) cls = 'mid';
    return '<span class="qbadge ' + cls + '" title="امتیاز کیفیت ویرایشی: ' + faDigits(q) + '">' + faDigits(q) + '</span>';
  }

  function loading(msg) {
    return '<div class="loading"><div class="spinner"></div><div>' + (msg || 'در حال بارگذاری…') + '</div></div>';
  }

  function revealLive() {
    const b = document.getElementById('liveBadge');
    if (!b || !b.hidden) return;
    b.hidden = false;
    const btn = document.getElementById('liveRefresh');
    if (btn) btn.onclick = () => { for (const k in cache) delete cache[k]; location.reload(); };
  }

  function revealStatic(dateStr) {
    if (window.__live) return; // live source wins
    const b = document.getElementById('staticBadge');
    if (!b) return;
    if (!b.hidden && !dateStr) return; // already shown and no new date to merge
    b.hidden = false;
    if (dateStr) {
      b.innerHTML = '<span class="static-dot"></span> خروجی ثابت از ' + faDigits(dateStr);
      b.title = 'سرور زنده در دسترس نیست؛ این خروجی ثابت از «' + dateStr + '» ساخته شده است. برای داده‌ی زنده، سرور محلی (live_server.py) را اجرا کنید.';
    }
  }

  function syncSourceBadge(meta) {
    if (window.__live) revealLive();
    else if (window.__static) revealStatic((meta && meta.builtAt) || '');
  }

  // ---------- views ----------
  const app = document.getElementById('app');

  async function renderHome() {
    app.innerHTML = loading();
    const meta = await jget('meta.json');
    const dir = await jget('directory.json');
    syncSourceBadge(meta);
    // featured = top quality 90+ theories/models
    const featured = dir.filter((d) => d.q >= 90 && (d.type === 'THEORY' || d.type === 'MODEL'))
      .sort((a, b) => (b.q - a.q) || (String(b.fa).localeCompare(String(a.fa), 'fa'))).slice(0, 12);

    const stat = (num, lbl) => '<div class="stat"><div class="num">' + faDigits(num) + '</div><div class="lbl">' + lbl + '</div></div>';

    let html = '';
    html += '<section class="hero fadein">';
    html += '<span class="hero-eyebrow">دانشنامه‌ی دانش‌شناختی · ۳۶ نوع موجودیت</span>';
    html += '<h1>هسته‌ی دانش علمی رسانامه</h1>';
    html += '<p class="lead">نمایندگی شفاف و ساختاریافته از ' + faDigits(meta.total_entities) + ' موجودیت دانشی — از نظریه‌ها و مدل‌ها تا اندیشمندان، آثار و روش‌ها. هر مورد با سه محور مستقل وضعیت، فیلدهای کامل و ارتباطات مستند به سایر بخش‌ها نمایش داده می‌شود.</p>';
    html += '<div class="statband">'
      + stat(meta.total_entities, 'موجودیت دانشی')
      + stat(meta.total_relations, 'رابطه‌ی ساختاریافته')
      + stat(meta.total_sources, 'منبع علمی')
      + stat(meta.total_theorists, 'اندیشمند و نظریه‌پرداز')
      + '</div></section>';

    // type grid
    html += '<section class="section"><div class="section-head"><h2>نوع‌های موجودیت</h2><span class="sub">برای دیدن فهرست، روی هر نوع کلیک کنید</span></div><div class="typegrid">';
    meta.types.forEach((t) => {
      const fc = famColor(t.fam);
      html += '<a class="typecard" style="--fc:' + fc + '" href="#/browse?type=' + t.type + '"><div class="dot">' + esc((t.fa || t.type).charAt(0)) + '</div><div class="tc-body"><div class="tc-name">' + esc(t.fa) + '</div><div class="tc-count">' + faDigits(t.count) + ' مورد</div></div></a>';
    });
    html += '</div></section>';

    // families
    const maxFam = Math.max.apply(null, meta.families.map((f) => f.count));
    html += '<section class="section"><div class="section-head"><h2>خانواده‌های هستی‌شناختی</h2><span class="sub">' + meta.families.length + ' خانواده‌ی بنیادی</span></div><div class="famlist">';
    meta.families.forEach((f) => {
      const fc = famColor(f.fam);
      const w = Math.round((f.count / maxFam) * 100);
      html += '<div class="fam" style="--fc:' + fc + '"><div class="f-top"><span class="f-name">' + esc(f.fa) + '</span><span class="f-count">' + faDigits(f.count) + '</span></div><div class="f-bar"><i style="width:' + w + '%"></i></div></div>';
    });
    html += '</div></section>';

    // status legend (transparency)
    html += '<section class="section"><div class="section-head"><h2>سه محور مستقل وضعیت</h2><span class="sub">«منتشرشده» ≠ «تأییدشده‌ی علمی»</span></div><div class="legend">';
    html += legendCard('sw', 'پروژه‌ای', 'وضعیت کار روی سند: پیش‌نویس، در بازبینی، تأییدشده، منتشرشده، بایگانی‌شده.');
    html += legendCard('ss', 'علمی', 'اعتبار علمی ادعا: سنجیده‌نشده، پشتیبانی‌شده، ناقص، در مناقشه، نقض‌شده.');
    html += legendCard('sl', 'چرخه‌ی حیات', 'وضعیت پایداری مفهوم: فعال، تاریخی، جانشین‌شده، منسوخ، نامشخص.');
    html += '</div></section>';

    // featured
    html += '<section class="section"><div class="section-head"><h2>موردنمایای برتر</h2><span class="sub">موجودیت‌ها با کیفیت ویرایشی ۹۰ و بالاتر</span></div>';
    html += '<div class="entgrid">' + featured.map(entCard).join('') + '</div></section>';

    app.innerHTML = html;
  }

  function legendCard(cls, title, desc) {
    const col = { sw: 'var(--site-accent)', ss: 'var(--site-ok)', sl: 'var(--site-gold)' }[cls];
    return '<div class="card"><h4><span class="axis-dot" style="background:' + col + '"></span>' + title + '</h4><p>' + desc + '</p></div>';
  }

  function entCard(d) {
    const fc = famColor(d.fam);
    return '<a class="entcard" style="--fc:' + fc + '" href="#/' + d.type.toLowerCase() + '/' + d.slug + '">'
      + '<span class="badge" style="--fc:' + fc + '">' + esc(d.typeFa) + '</span>'
      + (d.sw && d.sw !== 'approved' && d.sw !== 'published' ? '<span class="badge sw-draft">' + esc(SW_FA[d.sw] || 'پیش‌نویس') + '</span>' : '')
      + '<div class="e-name">' + esc(d.fa) + '</div>'
      + (d.en ? '<div class="e-en">' + esc(d.en) + '</div>' : '')
      + '<div class="e-foot"><span>' + qBadge(d.q) + '</span>'
      + (d.level ? '<span>سطح: ' + esc(faDigits(d.level)) + '</span>' : '')
      + (d.year ? '<span>سال: ' + esc(faDigits(d.year)) + '</span>' : '')
      + (d.macro ? '<span class="muted">' + esc(d.macro) + '</span>' : '')
      + '</div></a>';
  }

  async function renderBrowse(type, q, fam, sw) {
    app.innerHTML = loading();
    const [meta, dir] = await Promise.all([jget('meta.json'), jget('directory.json')]);
    syncSourceBadge(meta);

    let filtered = dir.slice();
    if (type) filtered = filtered.filter((d) => d.type === type);
    if (fam) filtered = filtered.filter((d) => d.fam === fam);
    if (q) {
      const s = q.toLowerCase();
      filtered = filtered.filter((d) =>
        (d.fa || '').toLowerCase().includes(s) ||
        (d.en || '').toLowerCase().includes(s) ||
        (d.code || '').toLowerCase().includes(s));
    }
    // status (workflow) filter + counts before applying it
    const swBase = filtered.slice();
    const nApproved = swBase.filter((d) => d.sw === 'approved' || d.sw === 'published').length;
    const nDraft = swBase.length - nApproved;
    if (sw === 'approved') filtered = filtered.filter((d) => d.sw === 'approved' || d.sw === 'published');
    else if (sw === 'draft') filtered = filtered.filter((d) => d.sw !== 'approved' && d.sw !== 'published');
    filtered.sort((a, b) => (b.q || 0) - (a.q || 0) || String(a.fa).localeCompare(String(b.fa), 'fa'));

    const famFa = fam ? ((meta.families.find((f) => f.fam === fam) || {}).fa || fam) : '';
    const activeFa = fam ? ('ساختار: ' + famFa) : (type ? (meta.typeFa[type] || type) : 'همه');
    const PAGE = 48;
    window.__browse = { filtered, type, q, fam, page: 0 };

    let chips = '<button class="chip' + (!type ? ' active' : '') + '" data-type="">' + 'همه' + '<span class="n">' + faDigits(dir.length) + '</span></button>';
    meta.types.forEach((t) => {
      chips += '<button class="chip' + (type === t.type ? ' active' : '') + '" data-type="' + t.type + '">' + esc(t.fa) + '<span class="n">' + faDigits(t.count) + '</span></button>';
    });

    let swchips = '<button class="chip' + (!sw ? ' active' : '') + '" data-sw="">همه‌ی وضعیت‌ها</button>'
      + '<button class="chip' + (sw === 'approved' ? ' active' : '') + '" data-sw="approved">تأییدشده<span class="n">' + faDigits(nApproved) + '</span></button>'
      + '<button class="chip' + (sw === 'draft' ? ' active' : '') + '" data-sw="draft">پیش‌نویس<span class="n">' + faDigits(nDraft) + '</span></button>';

    const heading = q
      ? ('نتایج جست‌وجو برای «' + esc(q) + '»' + (type ? ' در ' + esc(meta.typeFa[type] || type) : ''))
      : fam ? ('ساختار: ' + esc(famFa)) : (type ? ('آرشیو: ' + esc(meta.typeFa[type] || type)) : 'مرور موجودیت‌ها');

    const famNote = fam ? '<span class="fam-note" id="famNote">در ساختار «' + esc(famFa) + '» · <a href="#/browse' + (type ? '?type=' + type : '') + '">نمایش همه‌ی انواع</a></span>' : '';

    app.innerHTML =
      '<div class="fadein"><div class="section-head" style="margin-top:0"><h2>' + heading + '</h2></div>'
      + famNote
      + '<div class="browsebar"><div class="chips" id="chips">' + chips + '</div>'
      + '<div class="chips sw-chips" id="swchips">' + swchips + '</div></div>'
      + '<div class="browse-meta"><span id="bcount"></span><span id="bactive"></span></div>'
      + '<div class="entgrid" id="bgrid"></div>'
      + '<div id="bmore"></div></div>';

    function paint() {
      const st = window.__browse;
      const shown = st.filtered.slice(0, st.page * PAGE);
      document.getElementById('bgrid').innerHTML = shown.length ? shown.map(entCard).join('') : '<div class="empty-state" style="grid-column:1/-1"><h3>نتیجه‌ای یافت نشد</h3><p>عبارت دیگری امتحان کنید یا فیلتر را تغییر دهید.</p></div>';
      document.getElementById('bcount').textContent = faDigits(st.filtered.length) + ' موجودیت';
      document.getElementById('bactive').textContent = activeFa;
      const more = st.page * PAGE < st.filtered.length;
      document.getElementById('bmore').innerHTML = more ? '<button class="btn ghost" id="loadMoreBtn">نمایش بیشتر</button>' : '';
      if (more) document.getElementById('loadMoreBtn').onclick = () => { st.page++; paint(); };
    }
    const buildHash = (t, s) => {
      const extra = [];
      if (t) extra.push('type=' + t);
      if (fam) extra.push('fam=' + encodeURIComponent(fam));
      if (s) extra.push('sw=' + s);
      if (q) extra.push('q=' + encodeURIComponent(q));
      return '#/browse' + (extra.length ? '?' + extra.join('&') : '');
    };
    document.getElementById('chips').onclick = (e) => {
      const b = e.target.closest('.chip'); if (!b) return;
      location.hash = buildHash(b.dataset.type, sw);
    };
    document.getElementById('swchips').onclick = (e) => {
      const b = e.target.closest('.chip'); if (!b) return;
      location.hash = buildHash(type, b.dataset.sw);
    };
    window.__browse.page = 1; paint();
  }

  async function renderDetail(type, slug) {
    app.innerHTML = loading('در حال بارگذاری موجودیت…');
    let recs;
    try { recs = await jget(slugFile(type)); }
    catch (e) { app.innerHTML = '<div class="empty-state"><h3>فایل داده یافت نشد</h3><p>نوع «' + esc(type) + '» در این دیتابیس وجود ندارد.</p><a class="backlink" href="#/browse">بازگشت به مرور</a></div>'; return; }
    const e = recs.find((r) => r.slug === slug || r.code === slug);
    if (!e) { app.innerHTML = '<div class="empty-state"><h3>موجودیت یافت نشد</h3><a class="backlink" href="#/browse">بازگشت</a></div>'; return; }
    const fc = famColor(e.family);

    // name → entity index (for linking theorists / related approaches text)
    let linkify = (t) => esc(faDigits(t));
    try {
      const nidx = buildNameIndex(await jget('directory.json'));
      const nkeys = Object.keys(nidx).sort((a, b) => b.length - a.length);
      linkify = (t) => linkifyNames(t, nidx, nkeys);
    } catch (_) { /* keep plain rendering */ }

    // meta cells
    const cell = (k, v, empty) => '<div class="meta-cell"><div class="k">' + k + '</div><div class="v' + (v === '' ? ' empty' : '') + '">' + (v === '' ? (empty || '—') : v) + '</div></div>';
    let metaHtml = '';
    if (e.year) metaHtml += cell('سال', esc(faDigits(e.year)));
    if (e.level) metaHtml += cell('سطح تحلیل', esc(faDigits(e.level)));
    if (e.approach) metaHtml += cell('رویکرد', esc(e.approach));
    if (e.paradigm) metaHtml += cell('پارادایم', esc(e.paradigm));
    if (e.macro) metaHtml += cell('حوزه‌ی کلان', esc(e.macro));
    if (e.views) metaHtml += cell('بازدید', faDigits(e.views));
    if (e.quality) metaHtml += cell('امتیاز کیفیت', '<span class="qbadge' + (e.quality < 90 ? (e.quality < 70 ? ' low' : ' mid') : '') + '">' + faDigits(e.quality) + ' / ۱۰۰</span>');
    if (e.tags) { let tg = ''; try { const a = JSON.parse(e.tags); if (Array.isArray(a) && a.length) tg = a.map((x) => esc(x)).join('، '); } catch (_) { tg = esc(e.tags); } if (tg) metaHtml += cell('برچسب‌ها', tg); }
    if (metaHtml) metaHtml = '<div class="metagrid">' + metaHtml + '</div>';

    // content blocks
    let blocks = '';
    const c = e.content || {};
    CONTENT_SECTIONS.forEach(([key, label]) => {
      if (c[key] === undefined || c[key] === '' || c[key] === null) return;
      let body;
      if (key === 'model' && typeof c.model === 'object') {
        const m = c.model;
        body = (m.description ? '<p class="txt">' + esc(faDigits(m.description)) + '</p>' : '')
          + (m.elements && m.elements.length ? '<div class="model-elems">' + m.elements.map((x) => '<span>' + esc(x) + '</span>').join('') + '</div>' : '');
      } else if (key === 'field' && typeof c.field === 'object') {
        const f = c.field;
        const vlink = (val) => '<a class="fieldlink" href="#/browse?q=' + encodeURIComponent(val) + '" title="جست‌وجوی این عبارت">' + esc(faDigits(val)) + '</a>';
        body = '<ul class="fieldlist">'
          + (f.family ? '<li><b>خانواده:</b> ' + vlink(f.family) + '</li>' : '')
          + (f.parent ? '<li><b>حوزه‌ی مادر:</b> ' + vlink(f.parent) + '</li>' : '')
          + (f.subfield ? '<li><b>زیرحوزه:</b> ' + vlink(f.subfield) + '</li>' : '')
          + (f.application ? '<li><b>کاربرد:</b> ' + vlink(f.application) + '</li>' : '')
          + '</ul>';
        if (body === '<ul class="fieldlist"></ul>') body = renderText(c[key]);
      } else {
        body = renderText(c[key]);
      }
      if (!body) return;
      blocks += '<div class="block fadein"><h3><span class="bar"></span>' + label + '</h3>' + body + '</div>';
    });
    // person extra: cards_count
    if (e.type === 'PERSON' && c.cards_count) blocks += '<div class="block"><h3><span class="bar"></span>تعداد کارت‌ها</h3><p>' + faDigits(c.cards_count) + ' کارت مرتبط</p></div>';

    // ---------- relationships (aside) ----------
    const rels = e.relations || [];
    const buckets = { agents: [], theories: [], works: [], other: [] };
    const THEORYISH = ['THEORY', 'MODEL', 'FRAMEWORK', 'HYPOTHESIS', 'LAW', 'CONCEPT', 'PARADIGM'];
    rels.forEach((r) => {
      if (r.otherType === 'PERSON') buckets.agents.push(r);
      else if (r.otherType === 'WORK') buckets.works.push(r);
      else if (THEORYISH.includes(r.otherType)) buckets.theories.push(r);
      else buckets.other.push(r);
    });
    const dedupe = (arr) => { const seen = {}; const out = []; arr.forEach((r) => { const id = r.otherSlug || r.otherCode; if (!seen[id]) { seen[id] = 1; out.push(r); } }); return out; };
    buckets.theories = dedupe(buckets.theories);
    buckets.agents = dedupe(buckets.agents);
    buckets.works = dedupe(buckets.works);
    buckets.other = dedupe(buckets.other);

    const relList = (title, icon, items, fallback) =>
      '<div class="relcard"><h3>' + icon + title + '</h3>'
      + (items.length ? '<ul>' + items.map(relItem).join('') + '</ul>' : (fallback ? '<p class="plain-list muted">' + fallback + '</p>' : '<p class="muted" style="font-size:13px">رابطه‌ای ثبت نشده است.</p>'))
      + '</div>';

    const ico = (p) => '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true">' + p + '</svg>';
    const I = {
      person: '<circle cx="12" cy="8" r="4"/><path d="M4 21v-1a6 6 0 0 1 12 0v1"/>',
      theory: '<path d="M12 3l9 5-9 5-9-5 9-5z"/><path d="M3 13l9 5 9-5"/>',
      work: '<path d="M4 5a2 2 0 0 1 2-2h6v18H6a2 2 0 0 1-2-2z"/><path d="M20 5a2 2 0 0 0-2-2h-6v18h6a2 2 0 0 0 2-2z"/>',
      link: '<path d="M9 15l6-6"/><path d="M11 6l1-1a4 4 0 0 1 6 6l-1 1"/><path d="M13 18l-1 1a4 4 0 0 1-6-6l1-1"/>',
      book: '<path d="M12 7v14"/><path d="M3 18V6a2 2 0 0 1 2-2h4v16H5a2 2 0 0 1-2-2z"/><path d="M21 18V6a2 2 0 0 0-2-2h-4v16h4a2 2 0 0 0 2-2z"/>',
    };

    let aside = '';
    aside += relList('نظریه‌پردازان و طراحان', ico(I.person), buckets.agents, e.theorists ? linkify(e.theorists) : null);
    aside += relList('نظریه‌ها و مدل‌های مرتبط', ico(I.theory), buckets.theories, null);
    aside += relList('آثار علمی مرتبط', ico(I.work), buckets.works, null);
    if (buckets.other.length) aside += relList('روابط دیگر', ico(I.link), buckets.other, null);
    // related approaches text
    if (e.relatedApproaches) aside += '<div class="relcard"><h3>' + ico(I.theory) + 'رویکردها و نظریه‌های هم‌خانواده</h3><p class="plain-list">' + linkify(e.relatedApproaches) + '</p></div>';
    // sources (cited / related works)
    if (e.sources && e.sources.length) {
      aside += '<div class="relcard"><h3>' + ico(I.book) + 'مقالات، کتاب‌ها و منابع مرتبط</h3><ul class="src-list">'
        + e.sources.slice(0, 12).map(srcItem).join('')
        + '</ul>' + (e.sources.length > 12 ? '<p class="muted" style="font-size:12px;margin-top:10px">و ' + faDigits(e.sources.length - 12) + ' منبع دیگر…</p>' : '') + '</div>';
    }
    if (e.recSources) aside += '<div class="relcard"><h3>' + ico(I.book) + 'منابع پیشنهادی در سند</h3><p class="plain-list">' + esc(e.recSources) + '</p></div>';

    // provenance / links
    if (e.links && e.links.length) {
      aside += '<div class="relcard"><h3>' + ico(I.link) + 'منشأ و پیوند</h3><ul class="src-list">'
        + e.links.map((l) => '<li class="src-item"><div class="s-kind">' + esc(l.type || 'link') + '</div><div class="s-title">' + esc(l.title || l.id) + '</div>' + (l.note ? '<div class="s-meta">' + esc(l.note) + '</div>' : '') + '</li>').join('')
        + '</ul></div>';
    }

    const statusChip = (label, val, fa, col) => '<span class="statuschip"><span class="d" style="background:' + col + '"></span><span class="muted">' + label + ':</span> ' + fa + '</span>';

    app.innerHTML =
      '<a class="backlink" href="#/browse' + (e.type ? '?type=' + e.type : '') + '"><svg class="ico" style="width:16px;height:16px" viewBox="0 0 24 24" aria-hidden="true"><path d="M9 6l6 6-6 6"/></svg> بازگشت به ' + esc(e.typeFa) + 'ها</a>'
      + '<div class="detail-hero fadein" style="--fc:' + fc + '">'
      + '<div class="dh-badges">'
      + '<a class="badge" style="--fc:' + fc + '" href="#/browse?type=' + e.type + '" title="آرشیوی از این نوع">' + esc(e.typeFa) + '</a>'
      + (e.familyFa ? (e.family ? '<a class="badge" style="--fc:' + fc + '" href="#/browse?fam=' + encodeURIComponent(e.family) + '" title="همه‌ی موجودیت‌های این ساختار">' + esc(e.familyFa) + '</a>' : '<span class="badge" style="--fc:' + fc + '">' + esc(e.familyFa) + '</span>') : '')
      + '<a class="badge badge-id" href="#/browse?q=' + encodeURIComponent(e.code) + '" title="جست‌وجوی این شناسه">شناسه: <bdir="ltr" style="direction:ltr">' + esc(e.code) + '</b></a>'
      + '</div>'
      + '<h1>' + esc(e.nameFa) + '</h1>'
      + (e.nameEn ? '<p class="en">' + esc(e.nameEn) + '</p>' : '')
      + '<div class="statusrow">'
      + statusChip('پروژه‌ای', e.sw, SW_FA[e.sw] || e.sw, swColor(e.sw))
      + statusChip('علمی', e.ss, SS_FA[e.ss] || e.ss, ssColor(e.ss))
      + statusChip('حیات', e.sl, SL_FA[e.sl] || e.sl, slColor(e.sl))
      + '</div></div>'
      + (metaHtml || '')
      + '<div class="detail-body"><div class="content-main">' + (blocks || '<div class="block"><h3><span class="bar"></span>محتوا</h3><p class="muted">برای این موجودیت فیلد محتوایی کاملی در سند ثبت نشده است؛ اطلاعات در بخش‌های وضعیت، فیلدهای تکمیلی و ارتباطات زیر در دسترس است.</p></div>') + '</div><aside class="rel-aside">' + aside + '</aside></div>';
  }

  function relItem(r) {
    const conf = (r.conf !== null && r.conf !== undefined) ? '<span class="conf ' + (+r.conf >= 0.8 ? 'verified' : 'low') + '">استخراج: ' + faDigits(Math.round(+r.conf * 100)) + '٪</span>' : '';
    const arrow = r.dir === 'in' ? '←' : '→';
    const target = r.otherSlug || r.otherCode;
    const name = esc(r.otherFa);
    const link = target && r.otherType
      ? '<a href="#/' + r.otherType.toLowerCase() + '/' + encodeURIComponent(target) + '">' + name + '</a>'
      : '<span>' + name + '</span>';
    return '<li class="rel-item" data-id="' + (target || '') + '">' + link
      + '<span class="rel-type">' + arrow + ' ' + esc(r.relFa || r.type) + ' · <span style="color:var(--fc,var(--site-muted))">' + esc(r.otherTypeFa) + '</span> ' + conf + '</span></li>';
  }
  function srcItem(s) {
    const bib = s.bib || {};
    const title = s.titleFa || s.titleEn || (bib.citation ? bib.citation : 'منبع');
    return '<li class="src-item"><div class="s-kind">' + esc(s.kind || 'منبع') + (s.year ? ' · ' + faDigits(s.year) : '') + '</div><div class="s-title">' + esc(title) + '</div>'
      + ((s.publisher || bib.creator) ? '<div class="s-meta">' + esc(s.publisher || bib.creator) + '</div>' : '') + '</li>';
  }

  // ---------- router ----------
  function route() {
    const raw = (location.hash || '#/').replace(/^#/, '');
    const qIdx = raw.indexOf('?');
    const path = qIdx >= 0 ? raw.slice(0, qIdx) : raw;
    const queryStr = qIdx >= 0 ? raw.slice(qIdx + 1) : '';
    const qs = {};
    queryStr.split('&').forEach((kv) => { const [k, v] = kv.split('='); if (k) qs[decodeURIComponent(k)] = decodeURIComponent(v || ''); });
    const parts = path.split('/').filter(Boolean);
    if (parts[0] === 'browse') {
      renderBrowse(qs.type || null, qs.q || null, qs.fam || null, qs.sw || null);
    } else if (parts.length >= 2) {
      renderDetail(parts[0].toUpperCase(), parts[1]);
    } else {
      renderHome();
    }
  }

  // ---------- global search ----------
  let searchTimer = null;
  const searchEl = document.getElementById('globalSearch');
  if (searchEl) {
    searchEl.addEventListener('input', () => {
      clearTimeout(searchTimer);
      const v = searchEl.value.trim();
      searchTimer = setTimeout(() => {
        if (location.hash && location.hash !== '#/' && !location.hash.startsWith('#/browse')) {
          location.hash = v ? '#/browse?q=' + encodeURIComponent(v) : '#/browse';
        } else if (v) {
          location.hash = '#/browse?q=' + encodeURIComponent(v);
        }
      }, 250);
    });
    searchEl.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') {
        clearTimeout(searchTimer);
        const v = searchEl.value.trim();
        location.hash = v ? '#/browse?q=' + encodeURIComponent(v) : '#/browse';
      }
    });
  }

  window.addEventListener('hashchange', () => { route(); window.scrollTo({ top: 0 }); });
  // set search value when navigating to browse?q=
  new MutationObserver(() => {
    const m = (location.hash || '').match(/[?&]q=([^&]+)/);
    if (m) { const v = decodeURIComponent(m[1]); if (searchEl.value !== v) searchEl.value = v; }
  }).observe(document.getElementById('app'), { subtree: true, characterData: true, childList: true });

  route();
})();
