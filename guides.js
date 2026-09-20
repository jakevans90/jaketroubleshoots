// guides.js

let assetHubDataCache = null;
let guideDiscoveryPromise = null;
let guideSearchPromise = null;

// Listing pages need metadata, not every guide's troubleshooting instructions.
// Search opts into the separate full-content vocabulary. Failed requests can be
// retried, and strict callers can distinguish a failed library from no matches.
async function fetchGuides({ strict = false, search = false } = {}) {
  try {
    if (!guideDiscoveryPromise) {
      guideDiscoveryPromise = fetch('/data/guide-discovery.json')
        .then(response => {
          if (!response.ok) throw new Error('Could not load guide discovery index');
          return response.json();
        })
        .then(records => {
          if (!Array.isArray(records)) throw new Error('Invalid guide discovery index');
          return records;
        })
        .catch(error => {
          guideDiscoveryPromise = null;
          throw error;
        });
    }
    if (!search) return await guideDiscoveryPromise;
    if (!guideSearchPromise) {
      guideSearchPromise = fetch('/data/guide-search-terms.json')
        .then(response => {
          if (!response.ok) throw new Error('Could not load guide search vocabulary');
          return response.json();
        })
        .then(vocabulary => {
          if (!vocabulary || typeof vocabulary !== 'object' || Array.isArray(vocabulary)) {
            throw new Error('Invalid guide search vocabulary');
          }
          return vocabulary;
        })
        .catch(error => {
          guideSearchPromise = null;
          throw error;
        });
    }
    const [records, vocabulary] = await Promise.all([guideDiscoveryPromise, guideSearchPromise]);
    return records.map(record => ({ ...record, searchText: vocabulary[record.url] || '' }));
  } catch (err) {
    if (strict) throw err;
    console.error('Guide load error:', err);
    return [];
  }
}

// Fetch asset hub data once and cache it
async function fetchAssetHubData() {
  if (assetHubDataCache) return assetHubDataCache;

  try {
    const res = await fetch('/data/hub-asset.json');
    if (!res.ok) throw new Error('Could not load hub-asset.json');
    assetHubDataCache = await res.json();
    return assetHubDataCache;
  } catch (err) {
    console.error('Asset hub load error:', err);
    assetHubDataCache = [];
    return assetHubDataCache;
  }
}

function slugify(text) {
  return (text || '')
    .toLowerCase()
    .trim()
    .replace(/\s+/g, '-')
    .replace(/[^a-z0-9-]/g, '');
}

function findAssetHub(assetType, assetHubData) {
  return assetHubData.find(a =>
    a.name === assetType || a.slug === slugify(assetType)
  );
}

function getIconPath(assetType, assetHubData) {
  const assetHub = findAssetHub(assetType, assetHubData);
  return assetHub?.icon || '';
}

// Render guides in a container
async function renderGuides(containerId, guides) {
  const container = document.getElementById(containerId);
  if (!container) return;

  const assetHubData = await fetchAssetHubData();

  container.innerHTML = ''; // Clear old content

  guides.forEach(guide => {
    const card = document.createElement('a');
    card.href = guide.url;
    card.classList.add('guide-card');

    const iconPath = getIconPath(guide.assetType, assetHubData);

    card.innerHTML = `
      <div class="card-content">
        ${iconPath ? `
          <div style="display:flex; justify-content:center; margin-bottom:14px;">
            <img
              src="${iconPath}"
              alt="${guide.assetType} icon"
              class="guide-card-icon"
              style="width:56px; height:56px; object-fit:contain;"
              onerror="this.style.display='none'"
            >
          </div>
        ` : ''}
        <h3>${guide.title}</h3>
        <p>${guide.description}</p>
        <div class="badges">
          <span class="badge asset">${guide.assetType}</span>
          <span class="badge manufacturer">${guide.manufacturer}</span>
          <span class="badge model">${guide.model}</span>
        </div>
        <p class="date"><em>Last Revision: ${guide.dateAdded}</em></p>
      </div>
    `;

    container.appendChild(card);
  });

  // Update total if #total-guides exists
  const totalContainer = document.getElementById('total-guides');
  if (totalContainer) {
    totalContainer.textContent = `Total Guides: ${guides.length}`;
  }
}

// Utility: sort guides alphabetically
function sortGuidesAlphabetically(guides) {
  return guides.slice().sort((a, b) => a.title.localeCompare(b.title));
}

// Utility: get most recent guides
function getRecentGuides(guides, count = 24) {
  return guides
    .slice()
    .sort((a, b) => new Date(b.dateAdded) - new Date(a.dateAdded))
    .slice(0, count);
}
