// Fetch guides and populate any page with #guides-grid
fetch('data/guides.json')
  .then(res => {
    if (!res.ok) throw new Error('Could not load guides.json');
    return res.json();
  })
  .then(jsonData => {
    // If guides.json is a list of filenames, fetch all
    const isFileList = Array.isArray(jsonData) && typeof jsonData[0] === 'string';
    if (isFileList) {
      return Promise.all(
        jsonData.map(file =>
          fetch(file).then(res => {
            if (!res.ok) throw new Error('Could not load ' + file);
            return res.json();
          })
        )
      ).then(allData => allData.flat());
    }
    return jsonData;
  })
  .then(allGuides => {
    // Sort alphabetically by title
    allGuides.sort((a, b) => a.title.localeCompare(b.title));

    // Display guides in any page with #guides-grid
    const container = document.getElementById('guides-grid');
    if (!container) return; // skip if page doesn't have grid

    container.innerHTML = ''; // clear existing content

    allGuides.forEach(guide => {
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

    // Update total
    const totalContainer = document.getElementById('total-guides');
if (totalContainer) {
  totalContainer.textContent = `Total Guides: ${allGuides.length}`;
}
  .catch(err => console.error('Guide load error:', err));
