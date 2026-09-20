(function () {
  'use strict';

  const PAGE_SIZE = 24;
  const LIBRARIES = ['guides', 'pms', 'basics'];
  const LABELS = { guides: 'guides', pms: 'PM procedures', basics: 'Biomed Basics articles' };
  const FIELDS = {
    guides: [['title', 12], ['model', 11], ['manufacturer', 8], ['assetType', 7], ['description', 3], ['searchText', 1]],
    pms: [['title', 12], ['model', 11], ['manufacturer', 8], ['assetType', 7], ['description', 3], ['interval', 2], ['searchAliases', 2]],
    basics: [['title', 12], ['badge', 8], ['category', 7], ['cardNote', 5], ['description', 3], ['slug', 2]]
  };
  const EXACT_TERMS = new Set(['ge', 'ip', 'ecg', 'ekg', 'esu', 'nibp', 'pacs', 'dicom', 'spo2', 'co2', 'etco2', 'pm', 'no', 'not']);
  const QUERY_ALIASES = {
    communicate: ['communicate', 'communication', 'communicating'],
    failed: ['fail', 'failure'], fails: ['fail', 'failure'],
    ekg: ['ekg', 'ecg'], ecg: ['ecg', 'ekg']
  };
  const FILLER_WORDS = new Set(['a', 'an', 'the', 'for', 'of', 'to', 'is', 'are', 'with', 'will']);
  const TYPO_SUGGESTIONS = { phillips: 'philips', intelliview: 'intellivue', maintanence: 'maintenance' };

  function normalize(value) {
    return String(value || '').normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase().replace(/[^a-z0-9]+/g, ' ').trim();
  }

  function tokens(value, joinModelTokens = false) {
    // Keep complete model numbers and also allow spacing such as "MX 450".
    const words = value.split(' ').filter(Boolean);
    const expanded = words.flatMap(word => [word, ...word.replace(/([a-z])([0-9])/g, '$1 $2').replace(/([0-9])([a-z])/g, '$1 $2').split(' ')]);
    // Title/model metadata also accepts joined names, e.g. ECG-1500 → ECG1500.
    // Never join the unordered instruction vocabulary or alter any digits.
    if (joinModelTokens) words.forEach((word, index) => {
      if (/^[a-z]+$/.test(word) && /^[0-9]+[a-z]*$/.test(words[index + 1] || '')) expanded.push(word + words[index + 1]);
    });
    return [...new Set(expanded)];
  }

  function createIndex(items, type) {
    return items.map(item => {
      const searchable = { ...item };
      if (type === 'pms') searchable.searchAliases = 'pm preventive maintenance';
      if (type === 'guides' && !searchable.searchText) searchable.searchText = (item.steps || []).map(step => step.instructions || '').join(' ');
      return {
        item,
        fields: FIELDS[type].map(([name, weight]) => {
          const value = normalize(searchable[name]);
          return { value, weight, words: tokens(value, name === 'model' || name === 'title'), phrase: name !== 'searchText' };
        })
      };
    });
  }

  function wordMatches(word, term) {
    return EXACT_TERMS.has(term) ? word === term : word.startsWith(term);
  }

  function rank(index, query) {
    const phrase = normalize(query);
    const terms = phrase.split(' ').filter(term => term && !FILLER_WORDS.has(term));
    if (!terms.length) return [];
    return index.map(entry => {
      const matches = terms.map(term => {
        const alternatives = QUERY_ALIASES[term] || [term];
        // Negation must still match, but the actual symptom should lead ranking.
        const importance = term === 'not' || term === 'no' ? 0.1 : 1;
        return entry.fields.map(field => {
          if (alternatives.some(option => field.words.includes(option))) return field.weight * 1.5 * importance;
          return alternatives.some(option => field.words.some(word => wordMatches(word, option))) ? field.weight * 0.5 * importance : 0;
        });
      });
      if (!matches.every(fields => fields.some(Boolean))) return { item: entry.item, value: 0 };
      let value = matches.reduce((total, fields) => total + fields.reduce((sum, weight) => sum + weight, 0), 1);
      entry.fields.forEach(field => {
        if (!field.value || !field.phrase) return;
        if (field.value === phrase) value += field.weight * 8;
        else if (field.value.startsWith(phrase)) value += field.weight * 5;
        else if (field.value.includes(phrase)) value += field.weight * 3;
      });
      return { item: entry.item, value };
    }).filter(result => result.value).sort((a, b) => b.value - a.value || a.item.title.localeCompare(b.item.title, undefined, { numeric: true })).map(result => result.item);
  }

  function suggestQuery(query) {
    const phrase = normalize(query);
    const suggestion = phrase.split(' ').map(term => TYPO_SUGGESTIONS[term] || term).join(' ');
    return suggestion === phrase ? '' : suggestion;
  }

  async function fetchArray(url) {
    const response = await fetch(url);
    if (!response.ok) throw new Error(`Could not load ${url}`);
    const data = await response.json();
    if (!Array.isArray(data)) throw new Error(`Invalid library data: ${url}`);
    return data;
  }

  async function loadLibraries(loadGuides, loadArray) {
    const loaded = await Promise.allSettled([
      loadGuides({ strict: true, search: true }), loadArray('data/preventive-maintenance.json'),
      loadArray('data/biomed-basics.json'), loadArray('data/hub-asset.json')
    ]);
    const data = {}, unavailable = [];
    [...LIBRARIES, 'assets'].forEach((name, index) => {
      data[name] = loaded[index].status === 'fulfilled' ? loaded[index].value : [];
      if (loaded[index].status === 'rejected' && name !== 'assets') unavailable.push(name);
    });
    return { data, unavailable };
  }

  // The same functions are exercised by Node's built-in test runner.
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { normalize, createIndex, rank, suggestQuery, loadLibraries };
    return;
  }
  // Reuse the same matching rules in the grouped guide library.
  window.JakeSearch = { normalize, createIndex, rank };
  if (!document.getElementById('search-bar')) return;

  const state = { indexes: {}, assets: [], query: '', type: 'all', ready: false, unavailable: [], results: {}, limits: {}, lastQuery: null };
  const escapeHtml = value => String(value || '').replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const slug = value => normalize(value).replace(/\s+/g, '-');
  const input = document.getElementById('search-bar');
  const summary = document.getElementById('search-count');
  let inputTimer;

  function iconFor(assetType) { return state.assets.find(asset => asset.name === assetType || asset.slug === slug(assetType))?.icon || ''; }
  function shell(item, className, html) {
    const card = document.createElement('a');
    card.href = item.url;
    card.className = `guide-card ${className}`.trim();
    card.innerHTML = `<div class="card-content">${html}</div>`;
    return card;
  }
  function equipmentCard(item, isPm) {
    const icon = iconFor(item.assetType);
    return shell(item, isPm ? 'pm-card' : '', `${icon ? `<img src="${escapeHtml(icon)}" alt="" class="guide-card-icon" width="56" height="56" loading="lazy">` : ''}${isPm ? '<span class="pm-card-label">PM Procedure</span>' : ''}<h3>${escapeHtml(item.title)}</h3><p>${escapeHtml(item.description)}</p><div class="badges"><span class="badge asset">${escapeHtml(item.assetType)}</span><span class="badge manufacturer">${escapeHtml(item.manufacturer)}</span><span class="badge model">${escapeHtml(item.model)}</span></div><p class="date"><em>Last Revision: ${escapeHtml(item.dateAdded)}</em></p>`);
  }
  function basicsCard(item) {
    return shell(item, 'basics-card', `<h3>${escapeHtml(item.title)}</h3><p>${escapeHtml(item.description)}</p><div class="badges"><span class="badge asset">${escapeHtml(item.category)}</span>${item.badge ? `<span class="badge model">${escapeHtml(item.badge)}</span>` : ''}</div>${item.cardNote ? `<p class="basics-card-note">${escapeHtml(item.cardNote)}</p>` : ''}<p class="date"><em>Last Revision: ${escapeHtml(item.lastRevision)}</em></p>`);
  }
  const BUILDERS = { guides: item => equipmentCard(item, false), pms: item => equipmentCard(item, true), basics: basicsCard };

  function typeVisible(name) { return state.type === 'all' || state.type === name; }
  function setGroup(name, append = false) {
    const results = state.results[name], limit = state.limits[name];
    const group = document.getElementById(`${name}-results-group`), grid = document.getElementById(`${name}-results`);
    const more = document.getElementById(`${name}-show-more`);
    group.hidden = !typeVisible(name) || !results.length;
    document.getElementById(`${name}-result-count`).textContent = results.length;
    const start = append ? grid.children.length : 0;
    if (!append) grid.replaceChildren();
    if (typeVisible(name)) {
      const fragment = document.createDocumentFragment();
      results.slice(start, limit).forEach(item => fragment.appendChild(BUILDERS[name](item)));
      grid.appendChild(fragment);
    }
    more.hidden = limit >= results.length;
    more.textContent = `Show ${Math.max(0, Math.min(PAGE_SIZE, results.length - limit))} more ${LABELS[name]}`;
    document.getElementById(`${name}-shown-count`).textContent = `Showing ${Math.min(limit, results.length)} of ${results.length} ${LABELS[name]}.`;
    if (append) {
      grid.children[start]?.focus();
      summary.textContent = `Showing ${Math.min(limit, results.length)} of ${results.length} ${LABELS[name]} for “${state.query.trim()}”.`;
    }
  }
  function updateUrl() {
    const params = new URLSearchParams();
    if (state.query.trim()) params.set('q', state.query.trim());
    if (state.type !== 'all') params.set('type', state.type);
    history.replaceState(null, '', `${location.pathname}${params.size ? `?${params}` : ''}`);
  }
  function render() {
    if (!state.ready) return;
    const query = state.query.trim(), start = document.getElementById('search-start'), empty = document.getElementById('search-empty');
    const unavailable = state.unavailable.length ? ` Could not load ${state.unavailable.map(name => LABELS[name]).join(', ')}. Reload to try again.` : '';
    const suggestion = document.getElementById('search-suggestion');
    suggestion.hidden = true;
    LIBRARIES.forEach(name => { document.getElementById(`${name}-results-group`).hidden = true; });
    if (!query) {
      start.hidden = false; empty.hidden = true;
      summary.textContent = `Search all three libraries, or choose a library to narrow the results.${unavailable}`;
      updateUrl();
      return;
    }
    if (query !== state.lastQuery) {
      LIBRARIES.forEach(name => { state.results[name] = rank(state.indexes[name], query); state.limits[name] = PAGE_SIZE; });
      state.lastQuery = query;
    }
    LIBRARIES.forEach(name => setGroup(name));
    const count = LIBRARIES.filter(typeVisible).reduce((total, name) => total + state.results[name].length, 0);
    start.hidden = true; empty.hidden = count !== 0;
    summary.textContent = `${count} result${count === 1 ? '' : 's'} for “${query}”${state.type === 'all' ? ' across the site' : ''}.${unavailable}`;
    if (!count) {
      const alternative = suggestQuery(query);
      if (alternative && LIBRARIES.filter(typeVisible).some(name => rank(state.indexes[name], alternative).length)) {
        suggestion.hidden = false;
        suggestion.textContent = `Search for “${alternative}”`;
        suggestion.dataset.query = alternative;
      }
    }
    document.getElementById('guide-results-link').href = `guides.html?q=${encodeURIComponent(query)}`;
    updateUrl();
  }
  function searchNow() { clearTimeout(inputTimer); state.query = input.value; render(); }
  function selectType() {
    document.querySelectorAll('.search-type-filter').forEach(button => {
      const active = button.dataset.searchType === state.type;
      button.classList.toggle('is-active', active);
      button.setAttribute('aria-pressed', String(active));
    });
  }
  function readUrl() {
    const params = new URLSearchParams(location.search);
    state.query = params.get('q') || '';
    state.type = ['all', ...LIBRARIES].includes(params.get('type')) ? params.get('type') : 'all';
    input.value = state.query;
    selectType();
  }

  readUrl();
  document.querySelectorAll('.search-type-filter').forEach(button => button.addEventListener('click', () => {
    state.type = button.dataset.searchType; selectType(); searchNow();
  }));
  input.addEventListener('input', () => { clearTimeout(inputTimer); inputTimer = setTimeout(searchNow, 180); });
  document.getElementById('site-search-form').addEventListener('submit', event => { event.preventDefault(); searchNow(); });
  document.getElementById('search-suggestion').addEventListener('click', event => { input.value = event.currentTarget.dataset.query; searchNow(); input.focus(); });
  LIBRARIES.forEach(name => document.getElementById(`${name}-show-more`).addEventListener('click', () => { state.limits[name] += PAGE_SIZE; setGroup(name, true); }));
  window.addEventListener('popstate', () => { clearTimeout(inputTimer); readUrl(); render(); });

  loadLibraries(fetchGuides, fetchArray).then(({ data, unavailable }) => {
    LIBRARIES.forEach(name => { state.indexes[name] = createIndex(data[name], name); });
    state.assets = data.assets; state.unavailable = unavailable; state.ready = true;
    document.getElementById('search-results').setAttribute('aria-busy', 'false');
    state.query = input.value;
    render();
  }).catch(error => {
    console.error('Site search load error:', error);
    document.getElementById('search-results').setAttribute('aria-busy', 'false');
    summary.textContent = 'The site library could not be loaded. Reload to try again, or use the library links below.';
  });
}());
