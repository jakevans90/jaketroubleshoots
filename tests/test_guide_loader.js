// Run with: node --test tests/test_guide_loader.js
const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');

const source = fs.readFileSync(path.join(__dirname, '..', 'guides.js'), 'utf8');
function loader(fetch) {
  const context = vm.createContext({ fetch, console: { error() {} } });
  vm.runInContext(source, context);
  return context.fetchGuides;
}

test('concurrent ordinary listings reuse metadata and never fetch search vocabulary or shards', async () => {
  const requests = [];
  const records = [{ url: 'guides/example.html', title: 'Example' }];
  const fetchGuides = loader(async url => {
    requests.push(url);
    return { ok: true, json: async () => records };
  });
  const [first, second] = await Promise.all([fetchGuides(), fetchGuides()]);
  assert.equal(first, records);
  assert.equal(second, records);
  assert.deepEqual(requests, ['/data/guide-discovery.json']);
});

test('search loads instruction vocabulary without mutating shared listing records', async () => {
  const requests = [];
  const records = [{ url: 'guides/example.html', title: 'Example' }];
  const fetchGuides = loader(async url => {
    requests.push(url);
    return { ok: true, json: async () => url.includes('search-terms') ? { 'guides/example.html': 'pacs dicom' } : records };
  });
  const result = await fetchGuides({ strict: true, search: true });
  assert.equal(result[0].searchText, 'pacs dicom');
  assert.equal(records[0].searchText, undefined);
  await fetchGuides({ search: true });
  assert.deepEqual(requests, ['/data/guide-discovery.json', '/data/guide-search-terms.json']);
});

test('strict failure rejects and a later request retries instead of caching an empty catalog', async () => {
  let attempts = 0;
  const fetchGuides = loader(async () => {
    attempts++;
    return { ok: attempts > 1, json: async () => [{ title: 'Recovered' }] };
  });
  await assert.rejects(fetchGuides({ strict: true }), /Could not load guide discovery/);
  assert.equal((await fetchGuides({ strict: true }))[0].title, 'Recovered');
  assert.equal(attempts, 2);
});

test('legacy callers retain the empty-list failure result', async () => {
  const fetchGuides = loader(async () => { throw new Error('offline'); });
  assert.equal((await fetchGuides()).length, 0);
});

test('a vocabulary failure does not poison successfully loaded listing metadata', async () => {
  const fetchGuides = loader(async url => ({
    ok: !url.includes('search-terms'), json: async () => [{ title: 'Available' }]
  }));
  await assert.rejects(fetchGuides({ strict: true, search: true }), /search vocabulary/);
  assert.equal((await fetchGuides())[0].title, 'Available');
});
