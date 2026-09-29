const test = require('node:test');
const assert = require('node:assert/strict');
const { searchLinks, sourceMatches } = require('../jobs.js');

test('searches encode user text as query parameters, not URL structure', () => {
  const links = searchLinks('imaging service engineer', 'A&B #1 / PA');
  const linkedin = new URL(links.linkedin);
  assert.equal(linkedin.origin, 'https://www.linkedin.com');
  assert.equal(linkedin.searchParams.get('keywords'), 'imaging service engineer');
  assert.equal(linkedin.searchParams.get('location'), 'A&B #1 / PA');
  assert.equal(new URL(links.google).searchParams.get('q'), 'imaging service engineer jobs A&B #1 / PA');
});
test('blank location does not narrow the search', () => {
  assert.equal(new URL(searchLinks('BMET', '  ').linkedin).searchParams.has('location'), false);
});
test('employer type and all search words combine; clearing matches all', () => {
  assert.ok(sourceMatches('oem_manufacturer', 'GE HealthCare imaging field service', 'oem_manufacturer', 'IMAGING ge'));
  assert.equal(sourceMatches('dialysis', 'DaVita biomedical', 'oem_manufacturer', ''), false);
  assert.equal(sourceMatches('dialysis', 'DaVita biomedical', '', 'no such company'), false);
  assert.ok(sourceMatches('dialysis', 'DaVita biomedical', '', ''));
});
