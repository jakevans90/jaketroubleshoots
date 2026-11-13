/* Progressive enhancement: direct links and the Indeed form work without JS. */
(function () {
  'use strict';

  function searchLinks(role, location) {
    const term = role.trim();
    const place = location.trim();
    const linkedin = new URL('https://www.linkedin.com/jobs/search/');
    linkedin.searchParams.set('keywords', term);
    if (place) linkedin.searchParams.set('location', place);
    const google = new URL('https://www.google.com/search');
    google.searchParams.set('q', [term, 'jobs', place].filter(Boolean).join(' '));
    return { linkedin: linkedin.href, google: google.href };
  }

  function sourceMatches(sourceType, sourceText, type, query) {
    return (!type || sourceType === type) && query.trim().toLowerCase().split(/\s+/).every(term => sourceText.toLowerCase().includes(term));
  }

  function postingMatches(posting, filters) {
    const haystack = [posting.title, posting.employer, posting.location, posting.roleCategory].filter(Boolean).join(' ').toLowerCase();
    const words = (filters.keyword || '').trim().toLowerCase().split(/\s+/).filter(Boolean);
    return (!filters.employer || posting.employerId === filters.employer) &&
      (!filters.employerType || posting.employerType === filters.employerType) &&
      (!filters.role || posting.roleCategoryId === filters.role) &&
      (!filters.state || posting.state === filters.state) &&
      (!filters.remote || posting.remote === true) &&
      words.every(word => haystack.includes(word));
  }

  function validatePulseSnapshot(snapshot) {
    if (!snapshot || snapshot.schemaVersion !== 1 || snapshot.availability !== 'available' || !Array.isArray(snapshot.postings) || !snapshot.postings.length) return false;
    const ids = new Set();
    const urls = new Set();
    return snapshot.postings.every(posting => {
      let url;
      try { url = new URL(posting.url); } catch (_) { return false; }
      if (url.protocol !== 'https:' || !posting.id || !posting.title || !posting.employer || ids.has(posting.id) || urls.has(url.href)) return false;
      ids.add(posting.id);
      urls.add(url.href);
      return true;
    });
  }

  function displayDate(value) {
    if (!value) return '';
    const parsed = new Date(value.length === 10 ? `${value}T00:00:00Z` : value);
    return Number.isNaN(parsed.valueOf()) ? '' : new Intl.DateTimeFormat('en-US', { month: 'short', day: 'numeric', year: 'numeric', timeZone: 'UTC' }).format(parsed);
  }

  const stateNames = new Map([
    ['AL', 'Alabama'], ['AK', 'Alaska'], ['AZ', 'Arizona'], ['AR', 'Arkansas'], ['CA', 'California'],
    ['CO', 'Colorado'], ['CT', 'Connecticut'], ['DE', 'Delaware'], ['DC', 'District of Columbia'],
    ['FL', 'Florida'], ['GA', 'Georgia'], ['HI', 'Hawaii'], ['ID', 'Idaho'], ['IL', 'Illinois'],
    ['IN', 'Indiana'], ['IA', 'Iowa'], ['KS', 'Kansas'], ['KY', 'Kentucky'], ['LA', 'Louisiana'],
    ['ME', 'Maine'], ['MD', 'Maryland'], ['MA', 'Massachusetts'], ['MI', 'Michigan'], ['MN', 'Minnesota'],
    ['MS', 'Mississippi'], ['MO', 'Missouri'], ['MT', 'Montana'], ['NE', 'Nebraska'], ['NV', 'Nevada'],
    ['NH', 'New Hampshire'], ['NJ', 'New Jersey'], ['NM', 'New Mexico'], ['NY', 'New York'],
    ['NC', 'North Carolina'], ['ND', 'North Dakota'], ['OH', 'Ohio'], ['OK', 'Oklahoma'],
    ['OR', 'Oregon'], ['PA', 'Pennsylvania'], ['RI', 'Rhode Island'], ['SC', 'South Carolina'],
    ['SD', 'South Dakota'], ['TN', 'Tennessee'], ['TX', 'Texas'], ['UT', 'Utah'], ['VT', 'Vermont'],
    ['VA', 'Virginia'], ['WA', 'Washington'], ['WV', 'West Virginia'], ['WI', 'Wisconsin'], ['WY', 'Wyoming'],
  ]);

  function stateCountMap(postings) {
    const counts = new Map();
    postings.forEach(posting => {
      if (posting.state) counts.set(posting.state, (counts.get(posting.state) || 0) + 1);
    });
    return counts;
  }

  if (typeof module !== 'undefined' && module.exports) module.exports = { searchLinks, sourceMatches, postingMatches, validatePulseSnapshot, displayDate, stateCountMap, stateNames };
  if (typeof document === 'undefined') return;

  const role = document.getElementById('jobs-role');
  const location = document.getElementById('jobs-location');
  const linkedin = document.getElementById('jobs-linkedin');
  const google = document.getElementById('jobs-google');
  function updateSearches() {
    const links = searchLinks(role.value, location.value);
    linkedin.href = links.linkedin;
    google.href = links.google;
  }
  role.addEventListener('change', updateSearches);
  location.addEventListener('input', updateSearches);
  updateSearches();
  linkedin.hidden = google.hidden = false;

  const filters = document.getElementById('jobs-directory-filters');
  const type = document.getElementById('employer-type');
  const query = document.getElementById('employer-search');
  const cards = Array.from(document.querySelectorAll('.jobs-employer-card'));
  const status = document.getElementById('jobs-directory-status');
  const empty = document.getElementById('jobs-no-employers');
  function filterSources() {
    let shown = 0;
    cards.forEach(card => {
      card.hidden = !sourceMatches(card.dataset.employerType, card.dataset.search, type.value, query.value);
      if (!card.hidden) shown += 1;
    });
    status.textContent = `${shown} of ${cards.length} employer career sources shown. No live vacancy counts.`;
    empty.hidden = shown !== 0;
  }
  filters.addEventListener('submit', event => event.preventDefault());
  type.addEventListener('change', filterSources);
  query.addEventListener('input', filterSources);
  filters.addEventListener('reset', () => {
    type.value = '';
    query.value = '';
    filterSources();
  });
  filters.hidden = false;
  filterSources();

  const pulseFilters = document.getElementById('pulse-filters');
  const pulseList = document.getElementById('pulse-openings-list');
  const pulseStatus = document.getElementById('pulse-openings-status');
  const pulseFallback = document.getElementById('pulse-openings-fallback');
  const pulseLoadMore = document.getElementById('pulse-load-more');

  function addOption(select, value, label) {
    const option = document.createElement('option');
    option.value = value;
    option.textContent = label;
    select.appendChild(option);
  }

  function openingCard(posting) {
    const card = document.createElement('article');
    card.className = 'jobs-opening-card';
    const category = document.createElement('span');
    category.className = 'jobs-card-type';
    category.textContent = posting.roleCategory;
    const heading = document.createElement('h4');
    const link = document.createElement('a');
    link.href = posting.url;
    link.target = '_blank';
    link.rel = 'noopener';
    link.textContent = posting.title;
    heading.appendChild(link);
    const employer = document.createElement('p');
    employer.className = 'jobs-opening-employer';
    employer.textContent = posting.employer;
    const location = document.createElement('p');
    location.textContent = `${posting.location}${posting.remote ? ' · Remote' : ''}`;
    card.append(category, heading, employer, location);
    const details = [];
    if (posting.salary) details.push(posting.salary);
    if (displayDate(posting.postedDate)) details.push(`Posted ${displayDate(posting.postedDate)}`);
    else if (displayDate(posting.firstObserved)) details.push(`First observed ${displayDate(posting.firstObserved)}`);
    if (details.length) {
      const meta = document.createElement('p');
      meta.className = 'jobs-opening-meta';
      meta.textContent = details.join(' · ');
      card.appendChild(meta);
    }
    return card;
  }

  async function initializePulse() {
    if (!pulseFilters || !pulseList || !pulseStatus || !pulseFallback || !pulseLoadMore) return;
    try {
      const response = await fetch('data/htm-hiring-pulse-public.json', { cache: 'no-cache' });
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      const snapshot = await response.json();
      if (!validatePulseSnapshot(snapshot)) throw new Error('Invalid Hiring Pulse snapshot');
      const postings = snapshot.postings;
      const employerFilter = document.getElementById('pulse-employer');
      const employerTypeFilter = document.getElementById('pulse-employer-type');
      const roleFilter = document.getElementById('pulse-role');
      const stateFilter = document.getElementById('pulse-state');
      const keywordFilter = document.getElementById('pulse-keyword');
      const remoteFilter = document.getElementById('pulse-remote');
      const stateChart = document.getElementById('pulse-state-chart');
      const mapStatus = document.getElementById('pulse-map-status');
      const mapReset = document.getElementById('pulse-map-reset');
      const employers = new Map(postings.map(posting => [posting.employerId, posting.employer]));
      [...employers].sort((a, b) => a[1].localeCompare(b[1])).forEach(([id, name]) => addOption(employerFilter, id, name));
      const employerTypes = new Map(postings.map(posting => [posting.employerType, posting.employerTypeLabel]));
      [...employerTypes].sort((a, b) => a[1].localeCompare(b[1])).forEach(([id, name]) => addOption(employerTypeFilter, id, name));
      const roles = new Map(postings.map(posting => [posting.roleCategoryId, posting.roleCategory]));
      [...roles].sort((a, b) => a[1].localeCompare(b[1])).forEach(([id, name]) => addOption(roleFilter, id, name));
      stateNames.forEach((name, code) => addOption(stateFilter, code, `${name} (${code})`));
      const stateCounts = stateCountMap(postings);
      let visibleLimit = 24;

      function syncStateChart() {
        if (!stateChart) return;
        const selected = stateFilter.value;
        stateChart.querySelectorAll('button[data-state]').forEach(button => {
          const active = button.dataset.state === selected;
          button.classList.toggle('is-selected', active);
          button.setAttribute('aria-pressed', String(active));
        });
        if (mapReset) mapReset.hidden = !selected;
        if (mapStatus) {
          const count = stateCounts.get(selected) || 0;
          mapStatus.textContent = selected
            ? `${stateNames.get(selected) || selected}: ${count} active ${count === 1 ? 'posting' : 'postings'} in the observed sample.`
            : `${stateCounts.size} states and districts currently have observed openings. Choose a state to narrow the list.`;
        }
      }

      function initializeStateChart() {
        if (!stateChart) return;
        const buttons = [...stateNames].map(([code, name]) => {
          const count = stateCounts.get(code) || 0;
          const button = document.createElement('button');
          button.type = 'button';
          button.className = 'jobs-state-bar';
          button.dataset.state = code;
          button.setAttribute('aria-label', `${name}: ${count} active ${count === 1 ? 'posting' : 'postings'} in the observed sample`);
          button.setAttribute('aria-pressed', 'false');
          button.disabled = count === 0;
          const label = document.createElement('span');
          label.className = 'jobs-state-bar-label';
          const fullName = document.createElement('strong');
          fullName.textContent = name;
          const total = document.createElement('span');
          total.textContent = `${code} · ${count}`;
          label.append(fullName, total);
          button.appendChild(label);
          button.addEventListener('click', () => {
            stateFilter.value = code;
            renderOpenings(true);
            document.getElementById('pulse-openings-heading').scrollIntoView({ behavior: 'smooth', block: 'start' });
          });
          return button;
        });
        stateChart.replaceChildren(...buttons);
        stateChart.hidden = false;
        if (mapReset) mapReset.addEventListener('click', () => {
          stateFilter.value = '';
          renderOpenings(true);
        });
        syncStateChart();
      }

      function renderOpenings(resetLimit) {
        if (resetLimit) visibleLimit = 24;
        const currentFilters = {
          employer: employerFilter.value,
          employerType: employerTypeFilter.value,
          role: roleFilter.value,
          state: stateFilter.value,
          keyword: keywordFilter.value,
          remote: remoteFilter.checked,
        };
        const matches = postings.filter(posting => postingMatches(posting, currentFilters));
        pulseList.replaceChildren(...matches.slice(0, visibleLimit).map(openingCard));
        const shown = Math.min(matches.length, visibleLimit);
        pulseStatus.textContent = matches.length ? `Showing ${shown} of ${matches.length} matching openings in the observed sample.` : 'No openings match these filters.';
        pulseLoadMore.hidden = shown >= matches.length;
        pulseFallback.hidden = true;
        syncStateChart();
      }

      pulseFilters.addEventListener('submit', event => event.preventDefault());
      [employerFilter, employerTypeFilter, roleFilter, stateFilter, remoteFilter].forEach(control => control.addEventListener('change', () => renderOpenings(true)));
      keywordFilter.addEventListener('input', () => renderOpenings(true));
      pulseFilters.addEventListener('reset', () => setTimeout(() => renderOpenings(true), 0));
      pulseLoadMore.addEventListener('click', () => { visibleLimit += 24; renderOpenings(false); });
      pulseFilters.hidden = false;
      initializeStateChart();
      renderOpenings(true);
    } catch (_) {
      pulseFilters.hidden = true;
      pulseList.replaceChildren();
      pulseStatus.textContent = '';
      pulseLoadMore.hidden = true;
      pulseFallback.hidden = false;
    }
  }

  initializePulse();

  // Preserve links to original sections now grouped into disclosures.
  function revealAnchor() {
    let id;
    try { id = decodeURIComponent(window.location.hash.slice(1)); } catch (_) { return; }
    const target = document.getElementById(id);
    if (!target) return;
    let ancestor = target.closest('details');
    while (ancestor) {
      ancestor.open = true;
      ancestor = ancestor.parentElement.closest('details');
    }
    if (id) target.scrollIntoView();
  }
  window.addEventListener('hashchange', revealAnchor);
  revealAnchor();
}());
