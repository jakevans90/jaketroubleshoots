(function () {
  const MAX_RESULTS = 24;
  const state = { guides: [], pms: [], basics: [], assets: [], query: '', type: 'all' };
  const normalize = value => String(value || '').toLowerCase().replace(/[^a-z0-9]+/g, ' ').trim();
  const escapeHtml = value => String(value || '').replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const slug = value => normalize(value).replace(/\s+/g, '-');

  function score(item, query, fields) {
    const phrase = normalize(query), terms = phrase.split(' ').filter(Boolean);
    if (!phrase || !terms.length) return 0;
    const values = fields.map(([name, weight]) => [normalize(item[name]), weight]);
    if (!terms.every(term => values.some(([value]) => value.includes(term)))) return 0;
    return values.reduce((total, [value, weight]) => {
      if (!value) return total;
      if (value === phrase) total += weight * 8;
      else if (value.startsWith(phrase)) total += weight * 5;
      else if (value.includes(phrase)) total += weight * 3;
      terms.forEach(term => { total += value.split(' ').includes(term) ? weight * 1.5 : value.includes(term) ? weight * .5 : 0; });
      return total;
    }, 1);
  }

  function rank(items, query, fields) {
    return items.map(item => ({ item, value: score(item, query, fields) })).filter(x => x.value).sort((a, b) => b.value - a.value || a.item.title.localeCompare(b.item.title, undefined, { numeric: true })).map(x => x.item);
  }

  function iconFor(assetType) { return state.assets.find(asset => asset.name === assetType || asset.slug === slug(assetType))?.icon || ''; }
  function shell(item, className, html) { const card = document.createElement('a'); card.href = item.url; card.className = `guide-card ${className}`.trim(); card.innerHTML = `<div class="card-content">${html}</div>`; return card; }
  function guideCard(g) { const icon = iconFor(g.assetType); return shell(g, '', `${icon ? `<img src="${escapeHtml(icon)}" alt="${escapeHtml(g.assetType)} icon" class="guide-card-icon" onerror="this.style.display='none'">` : ''}<h3>${escapeHtml(g.title)}</h3><p>${escapeHtml(g.description)}</p><div class="badges"><span class="badge asset">${escapeHtml(g.assetType)}</span><span class="badge manufacturer">${escapeHtml(g.manufacturer)}</span><span class="badge model">${escapeHtml(g.model)}</span></div><p class="date"><em>Last Revision: ${escapeHtml(g.dateAdded)}</em></p>`); }
  function pmCard(pm) { const icon = iconFor(pm.assetType); return shell(pm, 'pm-card', `${icon ? `<img src="${escapeHtml(icon)}" alt="${escapeHtml(pm.assetType)} icon" class="guide-card-icon" onerror="this.style.display='none'">` : ''}<span class="pm-card-label">PM Procedure</span><h3>${escapeHtml(pm.title)}</h3><p>${escapeHtml(pm.description)}</p><div class="badges"><span class="badge asset">${escapeHtml(pm.assetType)}</span><span class="badge manufacturer">${escapeHtml(pm.manufacturer)}</span><span class="badge model">${escapeHtml(pm.model)}</span></div><p class="date"><em>Last Revision: ${escapeHtml(pm.dateAdded)}</em></p>`); }
  function basicsCard(a) { return shell(a, 'basics-card', `<h3>${escapeHtml(a.title)}</h3><p>${escapeHtml(a.description)}</p><div class="badges"><span class="badge asset">${escapeHtml(a.category)}</span>${a.badge ? `<span class="badge model">${escapeHtml(a.badge)}</span>` : ''}</div>${a.cardNote ? `<p class="basics-card-note">${escapeHtml(a.cardNote)}</p>` : ''}<p class="date"><em>Last Revision: ${escapeHtml(a.lastRevision)}</em></p>`); }

  function typeVisible(name) { return state.type === 'all' || state.type === name; }
  function setGroup(name, results, builder) {
    const group = document.getElementById(`${name}-results-group`), grid = document.getElementById(`${name}-results`);
    group.hidden = !typeVisible(name) || !results.length;
    document.getElementById(`${name}-result-count`).textContent = results.length;
    grid.innerHTML = '';
    if (typeVisible(name)) results.slice(0, MAX_RESULTS).forEach(item => grid.appendChild(builder(item)));
  }
  function updateUrl() { const params = new URLSearchParams(); if (state.query) params.set('q', state.query); if (state.type !== 'all') params.set('type', state.type); history.replaceState(null, '', `${location.pathname}${params.size ? `?${params}` : ''}`); }
  function render() {
    const q = state.query.trim(), start = document.getElementById('search-start'), empty = document.getElementById('search-empty'), summary = document.getElementById('search-count');
    ['guides', 'pms', 'basics'].forEach(name => document.getElementById(`${name}-results-group`).hidden = true);
    if (!q) { start.hidden = false; empty.hidden = true; summary.textContent = 'Search all three libraries, or choose a library to narrow the results.'; updateUrl(); return; }
    const guides = rank(state.guides, q, [['title',12],['model',11],['manufacturer',8],['assetType',7],['description',3],['url',2],['stepsSearch',1]]);
    const pms = rank(state.pms, q, [['title',12],['model',11],['manufacturer',8],['assetType',7],['description',3],['interval',2]]);
    const basics = rank(state.basics, q, [['title',12],['badge',8],['category',7],['cardNote',5],['description',3],['slug',2]]);
    setGroup('guides', guides, guideCard); setGroup('pms', pms, pmCard); setGroup('basics', basics, basicsCard);
    const counts = { guides: guides.length, pms: pms.length, basics: basics.length }, relevant = state.type === 'all' ? guides.length + pms.length + basics.length : counts[state.type];
    start.hidden = true; empty.hidden = relevant !== 0; summary.textContent = `${relevant} result${relevant === 1 ? '' : 's'} for “${q}”${state.type === 'all' ? ' across the site' : ''}.`;
    document.getElementById('guide-results-link').href = `guides.html?q=${encodeURIComponent(q)}`; updateUrl();
  }

  Promise.all([fetchGuides(), fetch('data/preventive-maintenance.json').then(r => r.json()), fetch('data/biomed-basics.json').then(r => r.json()), fetch('data/hub-asset.json').then(r => r.json())]).then(([guides,pms,basics,assets]) => {
    state.guides = guides.map(g => ({ ...g, stepsSearch: Array.isArray(g.steps) ? g.steps.map(step => step.instructions || '').join(' ') : '' })); state.pms = pms; state.basics = basics; state.assets = assets;
    const params = new URLSearchParams(location.search); state.query = params.get('q') || ''; state.type = ['all','guides','pms','basics'].includes(params.get('type')) ? params.get('type') : 'all';
    const input = document.getElementById('search-bar'); input.value = state.query;
    document.querySelectorAll('.search-type-filter').forEach(button => { const active = button.dataset.searchType === state.type; button.classList.toggle('is-active', active); button.setAttribute('aria-pressed', active); button.addEventListener('click', () => { state.type = button.dataset.searchType; document.querySelectorAll('.search-type-filter').forEach(item => { const selected = item === button; item.classList.toggle('is-active', selected); item.setAttribute('aria-pressed', selected); }); render(); }); });
    input.addEventListener('input', event => { state.query = event.target.value; render(); }); document.getElementById('search-submit').addEventListener('click', () => { state.query = input.value; render(); }); input.addEventListener('keydown', event => { if (event.key === 'Enter') { event.preventDefault(); render(); } }); render();
  }).catch(error => { console.error('Site search load error:', error); document.getElementById('search-count').textContent = 'The site library could not be loaded. Please try again.'; });
}());
