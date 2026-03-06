// related-guides.js

// Get current guide's URL to identify it
const currentUrl = window.location.pathname.split('/').pop(); // e.g., "airlife-flowmate-gauge.html"
const container = document.getElementById('related-guides-grid');
if (!container) throw new Error('#related-guides-grid not found');

// Load the main guides JSON
fetch('../data/guides.json')
  .then(res => {
    if (!res.ok) throw new Error('Could not load guides.json');
    return res.json();
  })
  .then(jsonData => {
    // Check if it's a list of JSON files or full data
    const isFileList = Array.isArray(jsonData) && typeof jsonData[0] === 'string';
    if (isFileList) {
      // Fetch all sub-json files
      return Promise.all(
        jsonData.map(file =>
          fetch(`../${file}`).then(res => {
            if (!res.ok) throw new Error('Could not load ' + file);
            return res.json();
          })
        )
      ).then(allData => allData.flat());
    } else {
      return jsonData;
    }
  })
  .then(allGuides => {
    // Find the current guide object
    const currentGuide = allGuides.find(g => g.url.split('/').pop() === currentUrl);
    if (!currentGuide) {
      console.warn('Current guide not found in JSON:', currentUrl);
      return;
    }

    // Filter related guides (same model, not current guide)
    const relatedGuides = allGuides.filter(g =>
      g.model === currentGuide.model && g.url !== currentGuide.url
    );

    if (relatedGuides.length === 0) {
      container.innerHTML = '<p>No related guides found.</p>';
      return;
    }

    // Display related guides (no limit)
    relatedGuides.forEach(guide => {
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
  })
  .catch(err => console.error('Related guides load error:', err));
