// related-guides.js
async function loadRelatedGuides() {
  const container = document.getElementById("related-guides-grid");
  if (!container) {
    console.log("No related guides container on this page.");
    return;
  }

  const currentPage = window.location.pathname
    .split("/")
    .pop()
    .split("?")[0]
    .replace(".html", "");

  const currentPath = window.location.pathname
    .replace(/^\//, "")
    .split("?")[0];

  function slugify(text) {
    return (text || "")
      .toLowerCase()
      .trim()
      .replace(/\s+/g, "-")
      .replace(/[^a-z0-9-]/g, "");
  }

  function normalizeGuideUrl(url) {
    return (url || "").replace(/^\//, "");
  }

  try {
    const [allGuides, assetHubData] = await Promise.all([
      fetchGuides(),
      fetch("../data/hub-asset.json").then(res => {
        if (!res.ok) throw new Error("Could not load hub-asset.json");
        return res.json();
      })
    ]);

    const currentGuide = allGuides.find(g => {
      const guideUrl = normalizeGuideUrl(g.url);
      const guideFile = guideUrl.split("/").pop().replace(".html", "");

      return (
        guideFile === currentPage ||
        guideUrl === currentPath ||
        guideUrl.replace(".html", "") === currentPath.replace(".html", "") ||
        guideUrl.endsWith(currentPage + ".html") ||
        guideUrl.endsWith(currentPage)
      );
    });

    if (!currentGuide) {
      console.warn("Guide not found in JSON:", currentPage, "|", currentPath);
      container.innerHTML = "<p>No related guides found.</p>";
      return;
    }

    const related = allGuides.filter(g => {
      const guideFile = normalizeGuideUrl(g.url).split("/").pop().replace(".html", "");
      return (
        g.model === currentGuide.model &&
        guideFile !== currentPage
      );
    });

    if (related.length === 0) {
      container.innerHTML = "<p>No related guides yet.</p>";
      return;
    }

    container.innerHTML = "";

    related.forEach(guide => {
      const assetHub = assetHubData.find(a =>
        a.name === guide.assetType || a.slug === slugify(guide.assetType)
      );

      const iconPath = assetHub?.icon
        ? "../" + assetHub.icon.replace(/^\//, "")
        : "";

      const card = document.createElement("a");
      card.href = "../" + normalizeGuideUrl(guide.url);
      card.className = "guide-card";

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
  } catch (err) {
    console.error("Related guides error:", err);
    container.innerHTML = "<p>No related guides found.</p>";
  }
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", loadRelatedGuides);
} else {
  loadRelatedGuides();
}
