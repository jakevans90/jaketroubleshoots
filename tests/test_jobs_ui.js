const test = require('node:test');
const assert = require('node:assert/strict');
const { searchLinks, sourceMatches, postingMatches, validatePulseSnapshot, displayDate } = require('../jobs.js');

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

const posting = {
  id: 'job_1',
  title: 'Biomedical Equipment Technician II',
  employer: 'Example Health',
  employerId: 'emp_1',
  employerType: 'health-system',
  employerTypeLabel: 'Hospital / Health System',
  location: 'Pittsburgh, PA',
  state: 'PA',
  remote: true,
  roleCategory: 'BMET / Biomedical Equipment Technician',
  roleCategoryId: 'bmet',
  salary: null,
  postedDate: null,
  firstObserved: '2026-10-21T12:00:00Z',
  url: 'https://example.com/jobs/1',
};

test('Hiring Pulse filters combine employer, role, state, keyword, and remote', () => {
  assert.ok(postingMatches(posting, { employer: 'emp_1', employerType: 'health-system', role: 'bmet', state: 'PA', keyword: 'equipment pittsburgh', remote: true }));
  assert.equal(postingMatches(posting, { employer: '', employerType: 'oem', role: '', state: '', keyword: '', remote: false }), false);
  assert.equal(postingMatches(posting, { employer: '', role: 'imaging-service', state: '', keyword: '', remote: false }), false);
  assert.equal(postingMatches(posting, { employer: '', role: '', state: '', keyword: '', remote: false }), true);
});

test('Hiring Pulse snapshot validation rejects duplicate and unsafe canonical URLs', () => {
  const snapshot = { schemaVersion: 1, availability: 'available', postings: [posting] };
  assert.ok(validatePulseSnapshot(snapshot));
  assert.equal(validatePulseSnapshot({ ...snapshot, postings: [posting, { ...posting }] }), false);
  assert.equal(validatePulseSnapshot({ ...snapshot, postings: [{ ...posting, url: 'http://example.com/jobs/1' }] }), false);
  assert.equal(validatePulseSnapshot({ schemaVersion: 1, availability: 'unavailable', postings: [] }), false);
});

test('optional dates render only when valid and missing values stay blank', () => {
  assert.equal(displayDate(null), '');
  assert.equal(displayDate('not-a-date'), '');
  assert.equal(displayDate('2026-10-21'), 'Oct 21, 2026');
});
