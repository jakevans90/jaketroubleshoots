// Run with node --test tests/test_mobile_header.js
const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');

const source = fs.readFileSync(path.join(__dirname, '..', 'mobile-header.js'), 'utf8');

function runHeaderScript({ mobile = true, scrollY = 0 } = {}) {
  const classes = new Set();
  const listeners = {};
  const mediaListeners = {};
  const header = {
    classList: {
      toggle(name, force) {
        if (force) classes.add(name);
        else classes.delete(name);
      }
    }
  };
  const media = {
    matches: mobile,
    addEventListener(type, listener) {
      mediaListeners[type] = listener;
    }
  };
  const document = {
    readyState: 'complete',
    documentElement: { dataset: {} },
    querySelector: selector => selector === 'header' ? header : null
  };
  const window = {
    scrollY,
    matchMedia: () => media,
    addEventListener(type, listener) {
      listeners[type] = listener;
    },
    requestAnimationFrame(callback) {
      callback();
    }
  };

  vm.runInNewContext(source, { document, window });
  return { classes, listeners, media, mediaListeners, window };
}

test('mobile header compacts at 64px and expands above the threshold', () => {
  const page = runHeaderScript({ scrollY: 63 });
  assert.equal(page.classes.has('mobile-header--compact'), false);

  page.window.scrollY = 64;
  page.listeners.scroll();
  assert.equal(page.classes.has('mobile-header--compact'), true);

  page.window.scrollY = 20;
  page.listeners.scroll();
  assert.equal(page.classes.has('mobile-header--compact'), false);
});

test('desktop header never receives the compact class', () => {
  const page = runHeaderScript({ mobile: false, scrollY: 500 });
  assert.equal(page.classes.has('mobile-header--compact'), false);
});

test('leaving the mobile breakpoint clears the compact class', () => {
  const page = runHeaderScript({ scrollY: 100 });
  assert.equal(page.classes.has('mobile-header--compact'), true);

  page.media.matches = false;
  page.mediaListeners.change();
  assert.equal(page.classes.has('mobile-header--compact'), false);
});
