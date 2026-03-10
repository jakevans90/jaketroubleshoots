// related-guides.js

document.addEventListener("DOMContentLoaded", function() {

  const container = document.getElementById("related-guides-grid");

  if (!container) {
    console.log("No related guides container on this page.");
    return;
  }

  // current page filename
  const currentPage = window.location.pathname.split("/").pop();

  fetch("../data/guides.json")
    .then(res => res.json())
    .then(fileList => {

      if (Array.isArray(fileList) && typeof fileList[0] === "string") {
        return Promise.all(
          fileList.map(file =>
            fetch("../" + file).then(r => r.json())
          )
        ).then(data => data.flat());
      }

      return fileList;

    })
    .then(allGuides => {

      const currentGuide = allGuides.find(g =>
        g.url.split("/").pop() === currentPage
      );

      if (!currentGuide) {
        console.warn("Guide not found in JSON:", currentPage);
        return;
      }

      const related = allGuides.filter(g =>
        g.model === currentGuide.model &&
        g.url.split("/").pop() !== currentPage
      );

      if (related.length === 0) {
        container.innerHTML = "<p>No related guides yet.</p>";
        return;
      }

      related.forEach(guide => {
        const card = document.createElement("a");

        // Fix relative path
        card.href = "../" + guide.url;

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
