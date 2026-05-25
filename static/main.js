// static/js/main.js

/* ───────────────── page fade-out ───────────────────────── */
document.querySelectorAll('a[href]').forEach(a=>{
  if(a.target||a.href.includes('#'))return;
  a.addEventListener('click',e=>{
    e.preventDefault();
    document.body.classList.remove('fade-in');
    document.body.style.transition='opacity .25s ease';
    document.body.style.opacity='0';
    setTimeout(()=>window.location=a.href,180);
  });
});

/* ───────────────── VERIFY ───────────────────────── */
if (document.getElementById('runVerify')) {
  const tabs  = document.getElementById('verifyTabs');
  const panes = document.getElementById('verifyPanes');
  let idx = 0;
  const addPane = (t, h) => {
    const id = `v${idx}`;
    tabs.insertAdjacentHTML('beforeend',
      `<li class="nav-item">
         <button class="nav-link${idx?'':' active'}"
                 data-bs-toggle="pill"
                 data-bs-target="#${id}"
                 type="button">${t}</button>
       </li>`);
    panes.insertAdjacentHTML('beforeend',
      `<div class="tab-pane fade${idx?'':' show active'}" id="${id}">
         ${h}
       </div>`);
    idx++;
  };
  const resetUI = ()=>{ tabs.innerHTML=''; panes.innerHTML=''; idx=0; };
  const ssaLines = arr=>arr.map(ins=>{
    if(ins[0]==='assign') return `${ins[1]} := ${JSON.stringify(ins[2])}`;
    if(ins[0]==='store')  return `${ins[1]}[${ins[2]}] := ${ins[3]}`;
    if(ins[0]==='assert') return `assert ${JSON.stringify(ins[2])}`;
    return JSON.stringify(ins);
  }).join('\n');

  const drawCFG = adj=>{
    addPane('cfg',
      `<div id="cfgCanvas" class="d-flex justify-content-center"></div>`);
    if(!adj||!Object.keys(adj).length) return;
    const nodes = Object.keys(adj).map(i=>({data:{id:i}}));
    const edges = [];
    Object.entries(adj).forEach(([s,ds])=>
      ds.forEach(t=>edges.push({data:{id:`${s}_${t}`,source:s,target:t}}))
    );
    const cy = cytoscape({
      container: document.getElementById('cfgCanvas'),
      elements: {nodes, edges},
      layout: {name:'breadthfirst', directed:true, padding:10},
      style: [
        { selector:'node',
          style:{content:'data(id)','background-color':'#0FA4AF',
                  color:'#fff', 'font-size':'11px'}},
        { selector:'edge',
          style:{'curve-style':'bezier','target-arrow-shape':'triangle','width':2} }
      ]
    });
    cy.fit(cy.elements(), 40);
  };

  document.getElementById('runVerify').onclick = async()=>{
    resetUI();
    const res = await fetch('/parse',{
      method:'POST',
      headers:{'Content-Type':'application/json'},
      body:JSON.stringify({
        program:document.getElementById('codeArea').value,
        unroll :document.getElementById('unrollN').value
      })
    });
    const j = await res.json();
    if(!res.ok){
      addPane('error', `<pre>${j.errors.join('\n')}</pre>`);
      return;
    }
    addPane('unrolled',  `<pre>${j.unrolled}</pre>`);
    addPane('ssa',       `<pre>${ssaLines(j.origSSA)}</pre>`);
    addPane('optimised', `<pre>${ssaLines(j.optSSA)}</pre>`);
    const esc = s=>s.replace(/&/g,'&amp;').replace(/</g,'&lt;');
    addPane('smt', `<pre>${esc(j.smt)}</pre>`);
    drawCFG(j.cfgCode);
    addPane('verify', `<pre>${JSON.stringify(j.verification,null,2)}</pre>`);
  };
}


/* ───────────────── EQUIVALENCE ───────────────────────── */
if (document.getElementById('runEquiv')) {
  document.getElementById('runEquiv').onclick = async () => {
    const out = document.getElementById('equivOut');
    out.innerHTML = ''; 
    out.className = 'alert alert-secondary small';
    out.textContent = '⏳ running…';

    const resp = await fetch('/equiv-api', {
      method: 'POST',
      headers: { 'Content-Type':'application/json' },
      body: JSON.stringify({
        progA : document.getElementById('progA').value,
        progB : document.getElementById('progB').value,
        unroll: document.getElementById('unrollEquiv').value
      })
    });

    const j = await resp.json();
    if (!resp.ok) {
      out.className = 'alert alert-danger small';
      out.textContent = j.errors.join('\n');
      return;
    }

    // show equivalence status
    if (j.equivalent) {
      out.className = 'alert alert-success small';
      out.textContent = '✅ Programs are equivalent';
    } else {
      out.className = 'alert alert-warning small';
      out.textContent = '❌ Not equivalent';
    }

    // now render examples below
    const exList = document.createElement('div');
    exList.className = 'mt-2';

    // decide key: counter or witness
    const keyA = j.resultA && j.resultA.counterexamples ? 'counterexamples' : 'witnesses';
    const keyB = j.resultB && j.resultB.counterexamples ? 'counterexamples' : 'witnesses';

    // helper to build HTML
    function buildExamples(title, result, key) {
      const arr = result[key] || [];
      if (!arr.length) return '';
      let html = `<strong>${title} (${key}):</strong><ul class="mb-2">`;
      arr.forEach((ex, i) => {
        const assign = Object.entries(ex)
          .map(([v,val]) => `${v} = ${val}`)
          .join(', ');
        html += `<li>${assign}</li>`;
      });
      html += `</ul>`;
      return html;
    }

    // Program A
    if (j.resultA) {
      exList.innerHTML += buildExamples('Program A', j.resultA, keyA);
    }
    // Program B
    if (j.resultB) {
      exList.innerHTML += buildExamples('Program B', j.resultB, keyB);
    }

    // append to out
    out.parentNode.insertBefore(exList, out.nextSibling);
  };
}

