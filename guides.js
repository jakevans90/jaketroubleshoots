// guides.js

// Fetch all guides (handles single JSON or list of JSON files)
async function fetchGuides() {
  const res = await fetch('data/guides.json');
  if (!res.ok) throw new Error('Could not load guides.json');

  const jsonData = await res.json();
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
}

// Render guide cards into a given container
function renderGuides(containerId, guides) {
  const container = document.getElementById(containerId);
  if (!container) return;

  container.innerHTML = '';
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

  // Update total if the element exists
  const totalContainer = document.getElementById('total-guides');
  if (totalContainer) {
    totalContainer.textContent = `Total Guides: ${guides.length}`;
  }
}

// Optional helper: get most recent guides
function getRecentGuides(allGuides, count = 12) {
  return allGuides
    .sort((a, b) => new Date(b.dateAdded) - new Date(a.dateAdded))
    .slice(0, count);
}
