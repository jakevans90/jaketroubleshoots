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

  if (typeof module !== 'undefined' && module.exports) module.exports = { searchLinks, sourceMatches };
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
