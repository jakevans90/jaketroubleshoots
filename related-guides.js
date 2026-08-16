// related-guides.js
function normalizeLearningKey(value) {
  return (value || "")
    .toLowerCase()
    .trim()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "");
}

function findConfiguredArticleSlugs(currentGuide, learningMap, assetHubData) {
  const guideSlug = currentGuide.url
    .split("/")
    .pop()
    .replace(/\.html(?:\?.*)?$/, "");
  const modelKey = [currentGuide.manufacturer, currentGuide.model]
    .map(normalizeLearningKey)
    .join("--");
  const manufacturerKey = normalizeLearningKey(currentGuide.manufacturer);
  const normalizedAssetType = normalizeLearningKey(currentGuide.assetType);
  const assetRecord = assetHubData.find(asset =>
    asset.name === currentGuide.assetType || asset.slug === normalizedAssetType
  );
  const assetTypeKey = assetRecord?.slug || normalizedAssetType;

  const lookups = [
    [learningMap.issueOverrides, guideSlug],
    [learningMap.modelOverrides, modelKey],
    [learningMap.manufacturerOverrides, manufacturerKey],
    [learningMap.assetTypeDefaults, assetTypeKey]
  ];

  for (const [mapping, key] of lookups) {
    if (mapping && Object.prototype.hasOwnProperty.call(mapping, key)) {
      const configuredValue = mapping[key];
      if (Array.isArray(configuredValue)) return configuredValue;
      if (
        typeof configuredValue === "string" &&
        learningMap.articleSets &&
        Array.isArray(learningMap.articleSets[configuredValue])
      ) {
        return learningMap.articleSets[configuredValue];
      }
      return [];
    }
  }

  return [];
}

function createLearningArticleLink(article) {
  const link = document.createElement("a");
  link.className = "understand-basics-link";
  link.href = "/" + article.url.replace(/^\//, "");

  const title = document.createElement("strong");
  title.textContent = article.title;

  const note = document.createElement("span");
  note.textContent = article.cardNote || article.category || "Biomed Basics";

  link.append(title, note);
  return link;
}

function renderUnderstandBeforeTroubleshoot(currentGuide, learningMap, articles, assetHubData) {
  const configuredSlugs = findConfiguredArticleSlugs(
    currentGuide,
    learningMap,
    assetHubData
  );
  if (!configuredSlugs.length) return;

  const articlesBySlug = new Map(
    articles.map(article => [article.slug, article])
  );
  const matchedArticles = configuredSlugs
    .map(slug => articlesBySlug.get(slug))
    .filter(Boolean)
    .slice(0, 5);

  if (!matchedArticles.length) return;

  const guideMain = document.querySelector("main");
  if (!guideMain) return;

  const helpsHeading = Array.from(guideMain.querySelectorAll("h2"))
    .find(heading => heading.textContent.trim() === "What This Guide Helps With");
  if (!helpsHeading) return;

  const section = document.createElement("section");
  section.className = "understand-before-troubleshoot";
  section.setAttribute("aria-labelledby", "understand-before-troubleshoot-title");

  const heading = document.createElement("h2");
  heading.id = "understand-before-troubleshoot-title";
  heading.textContent = "Understand Before You Troubleshoot";

  const blurb = document.createElement("p");
  blurb.textContent =
    "Before troubleshooting this equipment, these Biomed Basics articles may provide helpful background:";

  const links = document.createElement("div");
  links.className = "understand-basics-links";
  matchedArticles.forEach(article =>
    links.appendChild(createLearningArticleLink(article))
  );

  section.append(heading, blurb, links);
  helpsHeading.before(section);
}

function renderModelSpecificPm(currentGuide, pmProcedures, assetHubData) {
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

  const section = document.createElement("section");
  section.className = "model-specific-pm-section";
  section.setAttribute("aria-labelledby", "model-specific-pm-title");

  const heading = document.createElement("h2");
  heading.id = "model-specific-pm-title";
  heading.textContent = "Want to do a proper checkout after this fix?";

  const blurb = document.createElement("p");
  blurb.className = "model-specific-pm-blurb";
  blurb.textContent =
    `Use the verified preventive maintenance procedure below for the exact ${exactPm.manufacturer} ${exactPm.model} model. Follow facility policy when deciding whether a full PM is required after the repair.`;

  const grid = document.createElement("div");
  grid.className = "guides-grid model-specific-pm-grid";

  const assetHub = assetHubData.find(asset =>
    asset.name === exactPm.assetType
  );
  const iconPath = assetHub?.icon || "";

  const card = document.createElement("a");
  card.href = "/" + exactPm.url.replace(/^\//, "");
  card.className = "guide-card pm-card";
  card.innerHTML = `
    <div class="card-content">
      ${iconPath ? `
        <img
          src="/${iconPath.replace(/^\//, "")}"
          alt="${exactPm.assetType} icon"
          class="guide-card-icon"
          onerror="this.style.display='none'"
        >
      ` : ""}

      <span class="pm-card-label">PM Procedure</span>

      <h3>${exactPm.title}</h3>

      <div class="badges">
        <span class="badge asset">${exactPm.assetType}</span>
        <span class="badge manufacturer">${exactPm.manufacturer}</span>
        <span class="badge model">${exactPm.model}</span>
      </div>

      <p>${exactPm.description}</p>

      <p class="pm-interval"><strong>Interval:</strong> ${exactPm.interval}</p>

      <p class="pm-safety"><strong>Electrical Safety:</strong> ${exactPm.requiresElectricalSafety ? "Included" : "Not specified"}</p>

      <p class="date">Added: ${exactPm.dateAdded}</p>
    </div>
  `;

  grid.appendChild(card);
  section.append(heading, blurb, grid);
  problemPersistsHeading.before(section);
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
      .catch(() => []),
    fetch("/data/troubleshooting-learning-map.json?v=" + Date.now())
      .then(res => res.ok ? res.json() : {})
      .catch(() => ({})),
    fetch("/data/biomed-basics.json?v=" + Date.now())
      .then(res => res.ok ? res.json() : [])
      .catch(() => [])
  ])
    .then(([allGuides, assetHubData, pmProcedures, learningMap, biomedArticles]) => {
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
        Array.isArray(pmProcedures) ? pmProcedures : [],
        assetHubData
      );

      renderUnderstandBeforeTroubleshoot(
        currentGuide,
        learningMap && typeof learningMap === "object" ? learningMap : {},
        Array.isArray(biomedArticles) ? biomedArticles : [],
        assetHubData
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
