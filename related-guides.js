// related-guides.js

document.addEventListener("DOMContentLoaded", function () {

  const container = document.getElementById("related-guides-grid");

  if (!container) {
    console.log("No related guides container on this page.");
    return;
  }

  // Get current page name and normalize it
  const currentPage = window.location.pathname
    .split("/")
    .pop()
    .replace(".html", "")
    .toLowerCase();

  fetch("/data/guides.json")
    .then(res => res.json())
    .then(allGuides => {

      // Find the guide matching this page
      const currentGuide = allGuides.find(g =>
        g.url.split("/").pop().replace(".html","").toLowerCase() === currentPage
      );

      if (!currentGuide) {
        console.warn("Guide not found in JSON:", currentPage);
        return;
      }

      // Find related guides by model
      const related = allGuides.filter(g =>
        g.model === currentGuide.model &&
        g.url.split("/").pop().replace(".html","").toLowerCase() !== currentPage
      );

      if (related.length === 0) {
        container.innerHTML = "<p>No related guides yet.</p>";
        return;
      }

      related.forEach(guide => {

        const card = document.createElement("a");

        card.href = "/" + guide.url;
        card.className = "guide-card";

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
    .catch(err => console.error("Related guides error:", err));

});
