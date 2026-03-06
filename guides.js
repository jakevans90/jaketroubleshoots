// guides.js

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

// Render guides in a container
function renderGuides(containerId, guides) {
  const container = document.getElementById(containerId);
  if (!container) return;

  container.innerHTML = ''; // Clear old content

  guides.forEach(guide => {
    const card = document.createElement('a');
    card.href = guide.url;
    card.classList.add('guide-card');

    card.innerHTML = `
      <div class="card-content">
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
function getRecentGuides(guides, count = 24) { // changed from 12 → 24
  return guides
    .slice()
    .sort((a, b) => new Date(b.dateAdded) - new Date(a.dateAdded))
    .slice(0, count);
}
