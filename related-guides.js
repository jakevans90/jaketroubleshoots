// related-guides.js
function renderModelSpecificPm(currentGuide, pmProcedures) {
  const exactPm = pmProcedures.find(pm =>
    pm.manufacturer === currentGuide.manufacturer &&
    pm.model === currentGuide.model
  );

  if (!exactPm) return;

  const guideMain = document.querySelector("main");
  if (!guideMain) return;

  const problemPersistsHeading = Array.from(guideMain.querySelectorAll("h2"))
    .find(heading => heading.textContent.trim() === "If the Problem Persists");

  if (!problemPersistsHeading) return;

  const card = document.createElement("section");
  card.className = "model-specific-pm-card";
  card.setAttribute("aria-labelledby", "model-specific-pm-title");

  const label = document.createElement("p");
  label.className = "model-specific-pm-label";
  label.textContent = "MODEL-SPECIFIC CHECKOUT";

  const heading = document.createElement("h2");
  heading.id = "model-specific-pm-title";
  heading.textContent = "Want to perform a proper checkout after this fix?";

  const description = document.createElement("p");
  description.textContent =
    `A preventive maintenance procedure is available for the exact ${exactPm.manufacturer} ${exactPm.model} model.`;

  const details = document.createElement("p");
  details.className = "model-specific-pm-details";
  details.textContent = exactPm.interval
    ? `Listed interval: ${exactPm.interval}`
    : "Follow the verified model-specific procedure and your facility policy.";

  const link = document.createElement("a");
  link.className = "model-specific-pm-link";
  link.href = "/" + exactPm.url.replace(/^\//, "");
  link.textContent = "Open the model-specific PM procedure";

  card.append(label, heading, description, details, link);
  problemPersistsHeading.before(card);
}

function loadRelatedGuides() {
  const container = document.getElementById("related-guides-grid");
  if (!container) {
    console.log("No related guides container on this page.");
    return;
  }

  const currentPage = window.location.pathname.split("/").pop().split("?")[0].replace(".html", "");
  const currentPath = window.location.pathname.replace(/^\//, "").split("?")[0];

  function slugify(text) {
    return (text || "")
      .toLowerCase()
      .trim()
      .replace(/\s+/g, "-")
      .replace(/[^a-z0-9-]/g, "");
  }

  Promise.all([
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
      }),
    fetch("/data/hub-asset.json?v=" + Date.now()).then(res => res.json()),
    fetch("/data/preventive-maintenance.json?v=" + Date.now())
      .then(res => res.ok ? res.json() : [])
      .catch(() => [])
  ])
    .then(([allGuides, assetHubData, pmProcedures]) => {
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

      renderModelSpecificPm(
        currentGuide,
        Array.isArray(pmProcedures) ? pmProcedures : []
      );

      const related = allGuides.filter(g =>
        g.model === currentGuide.model &&
        g.url.split("/").pop().replace(".html", "") !== currentPage
      );

      if (related.length === 0) {
        container.innerHTML = "<p>No related guides yet.</p>";
        return;
      }

      container.innerHTML = "";

      related.forEach(guide => {
        const assetHub = assetHubData.find(a =>
          a.name === guide.assetType || a.slug === slugify(guide.assetType)
        );

        const iconPath = assetHub?.icon || "";

        const card = document.createElement("a");
        card.href = "/" + guide.url;
        card.className = "guide-card";
        card.innerHTML = `
          <div class="card-content">
            ${iconPath ? `
              <div style="display:flex; justify-content:center; margin-bottom:14px;">
                <img
                  src="/${iconPath.replace(/^\//, "")}"
                  alt="${guide.assetType} icon"
                  class="guide-card-icon"
                  style="width:56px; height:56px; object-fit:contain;"
                  onerror="this.style.display='none'"
                >
              </div>
            ` : ""}
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
