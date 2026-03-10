// related-guides.js
function loadRelatedGuides() {
  const container = document.getElementById("related-guides-grid");
  if (!container) {
    console.log("No related guides container on this page.");
    return;
  }

  const currentPage = window.location.pathname.split("/").pop().split("?")[0].replace(".html", "");
  const currentPath = window.location.pathname.replace(/^\//, "").split("?")[0];

  fetch("/data/guides.json?v=" + Date.now())
    .then(res => res.json())
    .then(fileList => {
      if (Array.isArray(fileList) && typeof fileList[0] === "string") {
        return Promise.all(
          fileList.map(file =>
            fetch("/" + file + "?v=" + Date.now()).then(r => r.json())
          )
        ).then(data => data.flat());
      }
      return fileList;
    })
    .then(allGuides => {
      const currentGuide = allGuides.find(g => {
        const guideFile = g.url.split("/").pop().replace(".html", "");
        return (
          guideFile === currentPage ||
          g.url === currentPath ||
          g.url.replace(".html", "") === currentPath.replace(".html", "") ||
          g.url.endsWith(currentPage + ".html") ||
          g.url.endsWith(currentPage)
        );
      });

      if (!currentGuide) {
        console.warn("Guide not found in JSON:", currentPage, "|", currentPath);
        return;
      }

      const related = allGuides.filter(g =>
        g.model === currentGuide.model &&
        g.url.split("/").pop().replace(".html", "") !== currentPage
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
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", loadRelatedGuides);
} else {
  loadRelatedGuides();
}
