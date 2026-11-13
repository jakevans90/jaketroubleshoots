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

  const stateTiles = [
    ['AK', 'Alaska', 1, 1], ['ME', 'Maine', 1, 12],
    ['WA', 'Washington', 2, 1], ['ID', 'Idaho', 2, 2], ['MT', 'Montana', 2, 3], ['ND', 'North Dakota', 2, 4], ['MN', 'Minnesota', 2, 5], ['WI', 'Wisconsin', 2, 6], ['MI', 'Michigan', 2, 7], ['NY', 'New York', 2, 9], ['VT', 'Vermont', 2, 10], ['NH', 'New Hampshire', 2, 11],
    ['OR', 'Oregon', 3, 1], ['NV', 'Nevada', 3, 2], ['WY', 'Wyoming', 3, 3], ['SD', 'South Dakota', 3, 4], ['IA', 'Iowa', 3, 5], ['IL', 'Illinois', 3, 6], ['IN', 'Indiana', 3, 7], ['OH', 'Ohio', 3, 8], ['PA', 'Pennsylvania', 3, 9], ['NJ', 'New Jersey', 3, 10], ['CT', 'Connecticut', 3, 11], ['RI', 'Rhode Island', 3, 12],
    ['CA', 'California', 4, 1], ['UT', 'Utah', 4, 2], ['CO', 'Colorado', 4, 3], ['NE', 'Nebraska', 4, 4], ['MO', 'Missouri', 4, 5], ['KY', 'Kentucky', 4, 6], ['WV', 'West Virginia', 4, 7], ['VA', 'Virginia', 4, 8], ['MD', 'Maryland', 4, 9], ['DE', 'Delaware', 4, 10], ['DC', 'District of Columbia', 4, 11], ['MA', 'Massachusetts', 4, 12],
    ['AZ', 'Arizona', 5, 2], ['NM', 'New Mexico', 5, 3], ['KS', 'Kansas', 5, 4], ['AR', 'Arkansas', 5, 5], ['TN', 'Tennessee', 5, 6], ['NC', 'North Carolina', 5, 8], ['SC', 'South Carolina', 5, 9],
    ['HI', 'Hawaii', 6, 1], ['TX', 'Texas', 6, 4], ['OK', 'Oklahoma', 6, 5], ['LA', 'Louisiana', 6, 6], ['MS', 'Mississippi', 6, 7], ['AL', 'Alabama', 6, 8], ['GA', 'Georgia', 6, 9], ['FL', 'Florida', 6, 10],
  ];

  function stateCountMap(postings) {
    const counts = new Map();
    postings.forEach(posting => {
      if (posting.state) counts.set(posting.state, (counts.get(posting.state) || 0) + 1);
    });
    return counts;
  }

  function stateIntensity(count, maximum) {
    if (!count || !maximum) return 0;
    return Math.min(4, Math.max(1, Math.ceil((count / maximum) * 4)));
  }

  if (typeof module !== 'undefined' && module.exports) module.exports = { searchLinks, sourceMatches, postingMatches, validatePulseSnapshot, displayDate, stateCountMap, stateIntensity, stateTiles };
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
      const stateMap = document.getElementById('pulse-state-map');
      const mapStatus = document.getElementById('pulse-map-status');
      const mapReset = document.getElementById('pulse-map-reset');
      const employers = new Map(postings.map(posting => [posting.employerId, posting.employer]));
      [...employers].sort((a, b) => a[1].localeCompare(b[1])).forEach(([id, name]) => addOption(employerFilter, id, name));
      const employerTypes = new Map(postings.map(posting => [posting.employerType, posting.employerTypeLabel]));
      [...employerTypes].sort((a, b) => a[1].localeCompare(b[1])).forEach(([id, name]) => addOption(employerTypeFilter, id, name));
      const roles = new Map(postings.map(posting => [posting.roleCategoryId, posting.roleCategory]));
      [...roles].sort((a, b) => a[1].localeCompare(b[1])).forEach(([id, name]) => addOption(roleFilter, id, name));
      [...new Set(postings.map(posting => posting.state).filter(Boolean))].sort().forEach(state => addOption(stateFilter, state, state));
      const stateCounts = stateCountMap(postings);
      const maximumStateCount = Math.max(...stateCounts.values(), 0);
      const stateNames = new Map(stateTiles.map(tile => [tile[0], tile[1]]));
      let visibleLimit = 24;

      function syncStateMap() {
        if (!stateMap) return;
        const selected = stateFilter.value;
        stateMap.querySelectorAll('button[data-state]').forEach(button => {
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

      function initializeStateMap() {
        if (!stateMap) return;
        const buttons = stateTiles.map(([code, name, row, column]) => {
          const count = stateCounts.get(code) || 0;
          const button = document.createElement('button');
          button.type = 'button';
          button.className = `jobs-state-tile level-${stateIntensity(count, maximumStateCount)}`;
          button.dataset.state = code;
          button.style.gridRow = String(row);
          button.style.gridColumn = String(column);
          button.setAttribute('aria-label', `${name}: ${count} active ${count === 1 ? 'posting' : 'postings'} in the observed sample`);
          button.setAttribute('aria-pressed', 'false');
          button.disabled = count === 0;
          const abbreviation = document.createElement('strong');
          abbreviation.textContent = code;
          const total = document.createElement('span');
          total.textContent = String(count);
          button.append(abbreviation, total);
          button.addEventListener('click', () => {
            stateFilter.value = code;
            renderOpenings(true);
            document.getElementById('pulse-openings-heading').scrollIntoView({ behavior: 'smooth', block: 'start' });
          });
          return button;
        });
        stateMap.replaceChildren(...buttons);
        stateMap.hidden = false;
        if (mapReset) mapReset.addEventListener('click', () => {
          stateFilter.value = '';
          renderOpenings(true);
        });
        syncStateMap();
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
        syncStateMap();
      }

      pulseFilters.addEventListener('submit', event => event.preventDefault());
      [employerFilter, employerTypeFilter, roleFilter, stateFilter, remoteFilter].forEach(control => control.addEventListener('change', () => renderOpenings(true)));
      keywordFilter.addEventListener('input', () => renderOpenings(true));
      pulseFilters.addEventListener('reset', () => setTimeout(() => renderOpenings(true), 0));
      pulseLoadMore.addEventListener('click', () => { visibleLimit += 24; renderOpenings(false); });
      pulseFilters.hidden = false;
      initializeStateMap();
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
