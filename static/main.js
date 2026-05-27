/* ════════════════════════════════════════════════════════════════
   MiniLang Workbench — main.js
   ════════════════════════════════════════════════════════════════ */

/* ── Helpers ──────────────────────────────────────────────────── */
const $ = id => document.getElementById(id);
const show = id => $(id)?.classList.remove('hidden');
const hide = id => $(id)?.classList.add('hidden');

/* ── "New Proof" — clears editors and resets all results ──────── */
document.addEventListener('DOMContentLoaded', () => {
  const btn = $('newProofBtn');
  if (!btn) return;
  btn.addEventListener('click', () => {
    // Clear all textareas on the current page
    ['codeArea', 'progA', 'progB'].forEach(id => {
      const el = $(id);
      if (el) { el.value = ''; el.dispatchEvent(new Event('input')); }
    });
    // Reset verify panel
    ['v-status-card','v-ssa-section','v-smt-section',
     'v-witnesses-section','v-cfg-section'].forEach(hide);
    hide('v-smt-btn');
    show('v-idle');
    if ($('v-status-badge')) $('v-status-badge').textContent = 'Ready to Solve';
    if ($('v-status-text'))  $('v-status-text').textContent  = 'Idle';
    if ($('s-runtime'))      $('s-runtime').textContent      = '—';
    if ($('s-assertions'))   $('s-assertions').textContent   = '—';
    // Reset equiv panel
    hide('eq-banner');
    hide('eq-details');
  });
});

/**
 * Format an SSA expression (Python tuple → JSON array) to a
 * human-readable string.
 */
function fmtExpr(e) {
  if (e === null || e === undefined) return '?';
  if (typeof e === 'boolean') return e ? 'true' : 'false';
  if (typeof e === 'number') return String(e);
  if (typeof e === 'string') return e;
  // ["binop", null, L, op, R]
  if (Array.isArray(e) && e[0] === 'binop') {
    return `(${fmtExpr(e[2])} ${e[3]} ${fmtExpr(e[4])})`;
  }
  return JSON.stringify(e);
}

/** Render an SSA instruction list to a string. */
function ssaToText(ssa) {
  return (ssa || []).map(ins => {
    if (ins[0] === 'assign') return `${ins[1]}  :=  ${fmtExpr(ins[2])}`;
    if (ins[0] === 'store')  return `${ins[1]}[${fmtExpr(ins[2])}]  :=  ${fmtExpr(ins[3])}`;
    if (ins[0] === 'assert') return `assert( ${fmtExpr(ins[2])} )`;
    return JSON.stringify(ins);
  }).join('\n');
}


/* ══ LINE NUMBERS (verify page) ══════════════════════════════════ */
(function initLineNumbers() {
  const ta  = $('codeArea');
  const gutter = $('lineNumbers');
  if (!ta || !gutter) return;

  function sync() {
    const count = ta.value.split('\n').length;
    gutter.innerHTML = Array.from({ length: count }, (_, i) =>
      `<span>${i + 1}</span>`).join('');
    gutter.scrollTop = ta.scrollTop;
  }

  ta.addEventListener('input',  sync);
  ta.addEventListener('scroll', () => { gutter.scrollTop = ta.scrollTop; });
  sync();
})();


/* ══ VERIFY ══════════════════════════════════════════════════════ */
(function initVerify() {
  const runBtn = $('runVerify');
  if (!runBtn) return;

  /* Reset the results panel back to the idle placeholder. */
  function resetResults() {
    ['v-status-card', 'v-ssa-section', 'v-smt-section',
     'v-witnesses-section', 'v-cfg-section'].forEach(hide);
    hide('v-smt-btn');
    show('v-idle');
  }

  /* Style the status card according to outcome. */
  function setStatusCard(holds, elapsed) {
    const card     = $('v-status-card');
    const iconWrap = $('v-card-icon-wrap');
    const icon     = $('v-card-icon');
    const title    = $('v-card-title');
    const msg      = $('v-card-msg');
    const time     = $('v-card-time');

    if (holds) {
      card.className     = 'flex items-center gap-4 p-5 rounded border border-primary/20 bg-primary/5';
      iconWrap.className = 'w-12 h-12 rounded-full flex items-center justify-center border bg-primary/20 border-primary/30 shrink-0';
      icon.className     = 'material-symbols-outlined text-[28px] text-primary';
      title.className    = 'font-headline-md text-headline-md leading-none mb-1 text-primary';
      icon.textContent   = 'check_circle';
      title.textContent  = 'Verified';
      msg.textContent    = 'All assertions hold. No violations found.';
    } else {
      card.className     = 'flex items-center gap-4 p-5 rounded border border-error/20 bg-error/5';
      iconWrap.className = 'w-12 h-12 rounded-full flex items-center justify-center border bg-error/20 border-error/30 shrink-0';
      icon.className     = 'material-symbols-outlined text-[28px] text-error';
      title.className    = 'font-headline-md text-headline-md leading-none mb-1 text-error';
      icon.textContent   = 'cancel';
      title.textContent  = 'Counter-example Found';
      msg.textContent    = 'Assertion violated. A counter-example is shown below.';
    }
    icon.style.fontVariationSettings = "'FILL' 1";
    time.textContent = `${elapsed}ms`;
    show('v-status-card');
  }

  /* Build a witness variable card. */
  function witnessCard(varName, val) {
    return `
      <div class="bg-surface-container-high p-3 rounded border border-outline-variant/20 flex justify-between items-center">
        <span class="font-code-md text-on-surface-variant text-[12px]">${varName}</span>
        <span class="font-code-lg text-primary font-bold text-[13px]">${val}</span>
      </div>`;
  }

  /* Render the CFG with Cytoscape. */
  function renderCFG(adj) {
    if (!adj || !Object.keys(adj).length) return;
    show('v-cfg-section');
    const nodes = Object.keys(adj).map(id => ({ data: { id } }));
    const edges = [];
    Object.entries(adj).forEach(([src, dsts]) =>
      dsts.forEach(tgt => edges.push({ data: { id: `${src}__${tgt}`, source: src, target: tgt } }))
    );
    cytoscape({
      container: $('cfgCanvas'),
      elements:  { nodes, edges },
      layout:    { name: 'breadthfirst', directed: true, padding: 12 },
      style: [
        { selector: 'node', style: {
            content:          'data(id)',
            'background-color': '#57f1db',
            color:            '#003731',
            'font-size':      '10px',
            'text-valign':    'center',
            width:            '34px',
            height:           '34px',
        }},
        { selector: 'edge', style: {
            'curve-style':         'bezier',
            'target-arrow-shape':  'triangle',
            width:                 1.5,
            'line-color':          '#3c4a46',
            'target-arrow-color':  '#3c4a46',
        }},
      ],
    });
  }

  runBtn.addEventListener('click', async () => {
    resetResults();
    hide('v-idle');

    $('v-status-badge').textContent = 'Solving…';
    $('v-status-text').textContent  = 'Running';
    runBtn.disabled = true;
    runBtn.classList.add('opacity-60');

    const t0 = performance.now();
    let j;

    try {
      const res = await fetch('/parse', {
        method:  'POST',
        headers: { 'Content-Type': 'application/json' },
        body:    JSON.stringify({
          program: $('codeArea').value,
          unroll:  $('unrollN').value,
        }),
      });
      j = await res.json();
      if (!res.ok) throw new Error((j.errors || []).join('\n') || 'Server error');
    } catch (err) {
      // Error card
      const card = $('v-status-card');
      card.className    = 'flex items-center gap-4 p-5 rounded border border-error/20 bg-error/5';
      $('v-card-icon-wrap').className = 'w-12 h-12 rounded-full flex items-center justify-center border bg-error/20 border-error/30 shrink-0';
      const ic = $('v-card-icon');
      ic.className = 'material-symbols-outlined text-[28px] text-error';
      ic.style.fontVariationSettings = "'FILL' 1";
      ic.textContent = 'error';
      $('v-card-title').className  = 'font-headline-md text-headline-md leading-none mb-1 text-error';
      $('v-card-title').textContent = 'Parse Error';
      $('v-card-msg').textContent   = err.message;
      $('v-card-time').textContent  = '';
      show('v-status-card');
      $('v-status-badge').textContent = 'Error';
      $('v-status-text').textContent  = 'Error';
      runBtn.disabled = false;
      runBtn.classList.remove('opacity-60');
      return;
    }

    const elapsed = Math.round(performance.now() - t0);
    const holds   = j.verification?.holds;

    // ── Status card ──
    setStatusCard(holds, elapsed);
    $('v-status-badge').textContent = holds ? 'Holds' : 'Violated';
    $('v-status-text').textContent  = holds ? 'Verified ✓' : 'Failed ✗';

    // ── Solver info ──
    if ($('s-runtime'))    $('s-runtime').textContent    = `${elapsed}ms`;
    if ($('s-assertions')) {
      const count = (j.smt?.match(/\(assert/g) || []).length;
      $('s-assertions').textContent = count || '—';
    }

    // ── Optimised SSA ──
    $('v-ssa-lines').textContent = ssaToText(j.optSSA);
    show('v-ssa-section');

    // ── SMT-LIB ──
    if (j.smt) {
      $('v-smt-code').textContent = j.smt;
      show('v-smt-btn');
    }

    // ── Witnesses / counter-examples ──
    const examples = j.verification?.witnesses || j.verification?.counterexamples || [];
    if (examples.length) {
      $('v-witnesses-title').textContent = holds ? 'Satisfying Assignments' : 'Counter-examples';
      $('v-witness-grid').innerHTML = Object.entries(examples[0])
        .map(([k, v]) => witnessCard(k, v)).join('');
      show('v-witnesses-section');
    }

    // ── CFG ──
    if (j.cfgCode) renderCFG(j.cfgCode);

    runBtn.disabled = false;
    runBtn.classList.remove('opacity-60');
  });
})();


/* ══ EQUIVALENCE ═════════════════════════════════════════════════ */
(function initEquiv() {
  const runBtn = $('runEquiv');
  if (!runBtn) return;

  /** Render a flat key→value object as table rows. */
  function witnessRows(obj, valueClass) {
    return Object.entries(obj)
      .map(([k, v]) => `
        <div class="flex justify-between border-b border-outline-variant/5 pb-1">
          <span>${k}</span>
          <span class="${valueClass} font-bold">${v}</span>
        </div>`)
      .join('');
  }

  runBtn.addEventListener('click', async () => {
    const banner  = $('eq-banner');
    const details = $('eq-details');

    // Loading state
    banner.className = 'w-full bg-surface-container-low border border-outline-variant/30 rounded-xl p-4 flex items-center gap-4';
    banner.innerHTML = `
      <span class="material-symbols-outlined text-primary animate-spin">progress_activity</span>
      <span class="text-on-surface-variant font-label-caps text-label-caps">Checking equivalence…</span>`;
    show('eq-banner');
    hide('eq-details');

    const k = $('unrollEquiv').value;
    let j;

    try {
      const res = await fetch('/equiv-api', {
        method:  'POST',
        headers: { 'Content-Type': 'application/json' },
        body:    JSON.stringify({
          progA:  $('progA').value,
          progB:  $('progB').value,
          unroll: k,
        }),
      });
      j = await res.json();
      if (!res.ok) throw new Error((j.errors || []).join('\n') || 'Server error');
    } catch (err) {
      banner.className = 'w-full bg-error/5 border border-error/20 rounded-xl p-4 flex items-center gap-4';
      banner.innerHTML = `
        <div class="w-10 h-10 rounded-full bg-error/20 flex items-center justify-center shrink-0">
          <span class="material-symbols-outlined text-error" style="font-variation-settings:'FILL' 1">error</span>
        </div>
        <div>
          <h3 class="font-headline-md text-[16px] text-error">Parse Error</h3>
          <p class="text-on-surface-variant text-[13px]">${err.message}</p>
        </div>`;
      return;
    }

    // ── Result banner ──
    if (j.equivalent) {
      banner.className = 'w-full bg-primary/5 border border-primary/20 rounded-xl p-4 flex items-center gap-4 shadow-[0_0_20px_-10px_rgba(87,241,219,0.2)]';
      banner.innerHTML = `
        <div class="w-10 h-10 rounded-full bg-primary/20 flex items-center justify-center shrink-0">
          <span class="material-symbols-outlined text-primary" style="font-variation-settings:'FILL' 1">check_circle</span>
        </div>
        <div>
          <h3 class="font-headline-md text-[16px] text-primary">Programs are Equivalent</h3>
          <p class="text-on-surface-variant text-[13px]">
            Logical verification successful using Z3. Bisimulation confirmed for unroll bound k=${k}.
          </p>
        </div>`;
    } else {
      banner.className = 'w-full bg-error/5 border border-error/20 rounded-xl p-4 flex items-center gap-4';
      banner.innerHTML = `
        <div class="w-10 h-10 rounded-full bg-error/20 flex items-center justify-center shrink-0">
          <span class="material-symbols-outlined text-error" style="font-variation-settings:'FILL' 1">cancel</span>
        </div>
        <div>
          <h3 class="font-headline-md text-[16px] text-error">Programs are NOT Equivalent</h3>
          <p class="text-on-surface-variant text-[13px]">
            Z3 found a divergence in final states for unroll bound k=${k}.
          </p>
        </div>`;
    }

    // ── Witness tables ──
    const keyA = j.resultA?.counterexamples ? 'counterexamples' : 'witnesses';
    const keyB = j.resultB?.counterexamples ? 'counterexamples' : 'witnesses';
    const arrA = (j.resultA?.[keyA] || [])[0] || {};
    const arrB = (j.resultB?.[keyB] || [])[0] || {};

    $('eq-witnesses-a').innerHTML = Object.keys(arrA).length
      ? witnessRows(arrA, 'text-primary-fixed')
      : '<p class="text-on-surface-variant/50 text-[11px]">No data returned</p>';

    $('eq-witnesses-b').innerHTML = Object.keys(arrB).length
      ? witnessRows(arrB, 'text-secondary-fixed-dim')
      : '<p class="text-on-surface-variant/50 text-[11px]">No data returned</p>';

    // ── Solver stats ──
    const kStat = $('eq-k-stat');
    const rStat = $('eq-result-stat');
    if (kStat) kStat.textContent = k;
    if (rStat) {
      rStat.textContent  = j.equivalent ? 'Equivalent' : 'Not Equivalent';
      rStat.className    = `font-code-md text-xs ${j.equivalent ? 'text-primary' : 'text-error'}`;
    }

    show('eq-details');
  });
})();
