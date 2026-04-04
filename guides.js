// guides.js

let assetHubDataCache = null;

// Fetch all guides (handles JSON array or list of JSON filenames)
async function fetchGuides() {
  try {
    const res = await fetch('data/guides.json');
    if (!res.ok) throw new Error('Could not load guides.json');

    const jsonData = await res.json();

    // If jsonData is a list of JSON files, fetch all of them
    const isFileList = Array.isArray(jsonData) && typeof jsonData[0] === 'string';
    if (isFileList) {
      const allData = await Promise.all(
        jsonData.map(file =>
          fetch(file).then(res => {
            if (!res.ok) throw new Error('Could not load ' + file);
            return res.json();
          })
        )
      );
      return allData.flat();
    }

    return jsonData;
  } catch (err) {
    console.error('Guide load error:', err);
    return [];
  }
}

// Fetch asset hub data once and cache it
async function fetchAssetHubData() {
  if (assetHubDataCache) return assetHubDataCache;

  try {
    const res = await fetch('data/hub-asset.json');
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
