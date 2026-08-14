// Adds exact-model troubleshooting guides to preventive maintenance pages.
function loadPmRelatedGuides() {
  const currentPage = window.location.pathname.split('/').pop().split('?')[0];

  function slugify(text) {
    return (text || '')
      .toLowerCase()
      .trim()
      .replace(/\s+/g, '-')
      .replace(/[^a-z0-9-]/g, '');
  }

  function loadAllGuides() {
    return fetch('/data/guides.json?v=' + Date.now())
      .then(response => response.json())
      .then(manifest => {
        if (!Array.isArray(manifest) || typeof manifest[0] !== 'string') {
          return manifest;
        }

        return Promise.all(
          manifest.map(file =>
            fetch('/' + file + '?v=' + Date.now()).then(response => response.json())
          )
        ).then(shards => shards.flat());
      });
  }

  Promise.all([
    loadAllGuides(),
    fetch('/data/preventive-maintenance.json?v=' + Date.now()).then(response => response.json()),
    fetch('/data/hub-asset.json?v=' + Date.now()).then(response => response.json())
  ])
    .then(([allGuides, pmProcedures, assetHubData]) => {
      const currentPm = pmProcedures.find(pm =>
        pm.url.split('/').pop().split('?')[0] === currentPage
      );

      if (!currentPm) return;

      const modelGuides = allGuides.filter(guide =>
        guide.manufacturer === currentPm.manufacturer &&
        guide.model === currentPm.model
      );

      if (!modelGuides.length) return;

      const feedback = document.querySelector('.guide-feedback');
      if (!feedback) return;

      const section = document.createElement('section');
      section.className = 'pm-related-guides-section';

      const heading = document.createElement('h3');
      heading.textContent = 'Troubleshooting Guides for This Model';

      const blurb = document.createElement('p');
      blurb.textContent =
        `Explore troubleshooting guides for the ${currentPm.manufacturer} ${currentPm.model}.`;

      const grid = document.createElement('div');
      grid.className = 'guides-grid';

      modelGuides
        .sort((a, b) => a.title.localeCompare(b.title))
        .forEach(guide => {
          const assetHub = assetHubData.find(asset =>
            asset.name === guide.assetType ||
            asset.slug === slugify(guide.assetType)
          );
          const iconPath = assetHub?.icon || '';

          const card = document.createElement('a');
          card.href = '/' + guide.url.replace(/^\//, '');
          card.className = 'guide-card';
          card.innerHTML = `
            <div class="card-content">
              ${iconPath ? `
                <div style="display:flex; justify-content:center; margin-bottom:14px;">
                  <img
                    src="/${iconPath.replace(/^\//, '')}"
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

          grid.appendChild(card);
        });

      section.append(heading, blurb, grid);
      feedback.before(section);
    })
    .catch(error => console.error('PM related guides error:', error));
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', loadPmRelatedGuides);
} else {
  loadPmRelatedGuides();
}
