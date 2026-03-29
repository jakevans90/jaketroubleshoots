// hub-links.js
// Reads Asset Type, Manufacturer, and Model from the guide page,
// checks hub JSONs for matching entries with exists: true,
// and wraps the text in a clickable link to the hub page.

(async function () {
  // ── Find the three device info paragraphs ──
  // They follow <h3> tags with these exact text values
  function getValueAfterHeading(headingText) {
    const headings = document.querySelectorAll('main h3');
    for (const h of headings) {
      if (h.textContent.trim() === headingText) {
        const next = h.nextElementSibling;
        if (next && next.tagName === 'P') return next;
      }
    }
    return null;
  }

  const assetEl = getValueAfterHeading('Asset Type');
  const mfrEl = getValueAfterHeading('Manufacturer');
  const modelEl = getValueAfterHeading('Model');

  if (!assetEl && !mfrEl && !modelEl) return;

  const assetName = assetEl ? assetEl.textContent.trim() : null;
  const mfrName = mfrEl ? mfrEl.textContent.trim() : null;
  const modelName = modelEl ? modelEl.textContent.trim() : null;

  // ── Load hub JSONs in parallel ──
  // Guides live in /guides/ so paths go up one level
  try {
    const [hubMfr, hubAsset, hubModel] = await Promise.all([
      fetch('/data/hub-manufacturer.json').then(r => r.json()),
      fetch('/data/hub-asset.json').then(r => r.json()),
      fetch('/data/hub-model.json').then(r => r.json())
    ]);

    // ── Manufacturer ──
    if (mfrEl && mfrName) {
      const hub = hubMfr.find(h => h.name === mfrName && h.flags.exists === true);
      if (hub) {
        mfrEl.innerHTML = `<a href="/${hub.url}" style="color:#111; font-weight:bold; text-decoration:underline;">${mfrName}</a>`;
      }
    }

    // ── Asset Type ──
    if (assetEl && assetName) {
      const hub = hubAsset.find(h => h.name === assetName && h.flags.exists === true);
      if (hub) {
        assetEl.innerHTML = `<a href="/${hub.url}" style="color:#111; font-weight:bold; text-decoration:underline;">${assetName}</a>`;
      }
    }

    // ── Model ──
    if (modelEl && modelName) {
      const hub = hubModel.find(h => h.name === modelName && h.flags.exists === true);
      if (hub) {
        modelEl.innerHTML = `<a href="/${hub.url}" style="color:#111; font-weight:bold; text-decoration:underline;">${modelName}</a>`;
      }
    }

  } catch (err) {
    // Fail silently — hub links are an enhancement, not critical
    console.warn('hub-links.js: could not load hub data', err);
  }
})();
