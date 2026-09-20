// Run with node --test tests/test_site_search.js
const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { normalize, createIndex, rank, suggestQuery, loadLibraries } = require('../site-search.js');
const read = file => JSON.parse(fs.readFileSync(path.join(__dirname, '..', 'data', file), 'utf8'));
const vocabulary = read('guide-search-terms.json');
const guides = read('guide-discovery.json').map(g => ({ ...g, searchText: vocabulary[g.url] }));
const guideIndex = createIndex(guides, 'guides');
const pmIndex = createIndex(read('preventive-maintenance.json'), 'pms');
const basicsIndex = createIndex(read('biomed-basics.json'), 'basics');

test('short acronyms do not match parts of unrelated words', () => {
  const index = createIndex([
    { title: 'Biomed Resume Basics', description: 'Compare test results' },
    { title: 'GE Patient Monitor', description: 'ECG and NIBP' },
    { title: 'ESU output failure', description: 'Electrosurgical unit' }
  ], 'guides');
  assert.deepEqual(rank(index, 'ESU').map(x => x.title), ['ESU output failure']);
  assert.deepEqual(rank(index, 'GE').map(x => x.title), ['GE Patient Monitor']);
  assert.deepEqual(rank(index, 'ECG').map(x => x.title), ['GE Patient Monitor']);
});

test('accent folding treats Dräger and Drager identically', () => {
  assert.equal(normalize('Dräger'), 'drager');
  assert.deepEqual(rank(guideIndex, 'Dräger'), rank(guideIndex, 'Drager'));
  assert.ok(rank(guideIndex, 'Dräger').length > 0);
});

test('partial models and spaced model numbers find equipment', () => {
  assert.ok(rank(guideIndex, 'IntelliVue MX').length > 0);
  assert.ok(rank(guideIndex, 'MX100').some(x => x.model.includes('MX100')));
  assert.ok(rank(guideIndex, 'MX 100').some(x => x.model.includes('MX100')));
});

test('joined model names find separated title and model metadata without changing digits', () => {
  const matches = rank(guideIndex, 'ECG1500');
  assert.ok(matches.length > 0);
  assert.ok(matches.every(x => x.model.includes('ECG-1500')));
  const index = createIndex([
    { title: 'ECG-1500 printer failure', model: 'ECG-1500' },
    { title: 'Other device', description: 'ECG 1500', searchText: 'ecg 1500' },
    { title: 'ECG-1501 printer failure', model: 'ECG-1501' }
  ], 'guides');
  assert.deepEqual(rank(index, 'ECG1500').map(x => x.title), ['ECG-1500 printer failure']);
  assert.equal(rank(index, 'ECG1050').length, 0);
});

test('an exact-model PM is found using the PM abbreviation', () => {
  const matches = rank(pmIndex, 'SIGMA Spectrum PM');
  assert.ok(matches.length > 0);
  assert.equal(matches[0].model, 'SIGMA Spectrum');
});

test('connectivity symptom wording ranks a useful IntelliVue communication guide first', () => {
  const matches = rank(guideIndex, 'Philips IntelliVue monitor will not communicate');
  assert.ok(matches.length > 0);
  assert.match(matches[0].title, /communication|network/i);
  assert.ok(matches.some(x => /central-station|network/i.test(x.url)));
});

test('negation remains a required whole word even with lower ranking weight', () => {
  const index = createIndex([
    { title: 'Battery not charging' },
    { title: 'Battery no charge' },
    { title: 'Battery charging normally' },
    { title: 'Battery charge notice' }
  ], 'guides');
  assert.deepEqual(rank(index, 'battery not charging').map(x => x.title), ['Battery not charging']);
  assert.deepEqual(rank(index, 'battery no charge').map(x => x.title), ['Battery no charge']);
});

test('core biomedical abbreviations retain relevant content', () => {
  for (const query of ['NIBP', 'ECG', 'ESU', 'PACS', 'DICOM']) {
    assert.ok(rank(guideIndex, query).length + rank(basicsIndex, query).length > 0, query);
  }
  assert.equal(rank(basicsIndex, 'ESU').some(x => /Resume/.test(x.title)), false);
});

test('numeric error-code queries and instruction vocabulary remain searchable', () => {
  assert.ok(rank(guideIndex, 'SIGMA 102').some(x => x.url.includes('error-102')));
  const index = createIndex([{ title: 'Device failure', searchText: 'connector oxidized' }], 'guides');
  assert.equal(rank(index, 'oxidized').length, 1);
});

test('misspellings offer an explicit alternative instead of silently changing intent', () => {
  assert.equal(suggestQuery('Phillips intelliview'), 'philips intellivue');
  assert.equal(suggestQuery('maintenance'), '');
  assert.equal(suggestQuery('C6'), '');
});

test('failure in one library preserves other libraries', async () => {
  const { data, unavailable } = await loadLibraries(async () => { throw new Error('offline'); }, async url => [{ title: url }]);
  assert.deepEqual(unavailable, ['guides']);
  assert.equal(data.guides.length, 0);
  assert.equal(data.pms.length, 1);
  assert.equal(data.basics.length, 1);
});

test('empty and filler-only searches do not return the whole catalog', () => {
  assert.equal(rank(guideIndex, '').length, 0);
  assert.equal(rank(guideIndex, 'the for').length, 0);
});
