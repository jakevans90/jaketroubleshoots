// related-guides.js
async function loadRelatedGuides() {
  const containerId = "related-guides-grid";
  const container = document.getElementById(containerId);

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

  try {
    const allGuides = await fetchGuides();

    const currentGuide = allGuides.find(g => {
      const guideFile = (g.url || "").split("/").pop().replace(".html", "");
      return (
        guideFile === currentPage ||
        g.url === currentPath ||
        (g.url || "").replace(".html", "") === currentPath.replace(".html", "") ||
        (g.url || "").endsWith(currentPage + ".html") ||
        (g.url || "").endsWith(currentPage)
      );
    });

    if (!currentGuide) {
      console.warn("Guide not found in JSON:", currentPage, "|", currentPath);
      return;
    }

    const related = allGuides.filter(g =>
      g.model === currentGuide.model &&
      (g.url || "").split("/").pop().replace(".html", "") !== currentPage
    );

    if (related.length === 0) {
      container.innerHTML = "<p>No related guides yet.</p>";
      return;
    }

    await renderGuides(containerId, related);
  } catch (err) {
    console.error("Related guides error:", err);
  }
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", loadRelatedGuides);
} else {
  loadRelatedGuides();
}
