(function () {
  "use strict";

  const root = document.querySelector("[data-career-learning]");
  if (!root) return;

  Promise.all([
    fetch("data/career-learning-map.json").then((response) => {
      if (!response.ok) throw new Error("Career learning map unavailable");
      return response.json();
    }),
    fetch("data/biomed-basics.json").then((response) => {
      if (!response.ok) throw new Error("Biomed Basics catalog unavailable");
      return response.json();
    })
  ]).then(([mapping, articles]) => {
    const catalog = new Map(articles.map((article) => [article.slug, article]));
    const requested = [
      ...(mapping.educationPage || []),
      ...Object.values(mapping.certifications || {}).flat()
    ];
    const matches = [...new Set(requested)]
      .map((slug) => catalog.get(slug))
      .filter(Boolean);

    if (!matches.length) return;

    const cards = matches.map((article) => `
      <a class="career-learning-card" href="${article.url}">
        <span>${article.badge || article.category || "Biomed Basics"}</span>
        <strong>${article.title}</strong>
        <small>${article.cardNote || article.description}</small>
      </a>`).join("");

    root.innerHTML = `
      <section class="content-box career-learning-panel">
        <p class="section-kicker">Keep Learning</p>
        <h3>Related Biomed Basics</h3>
        <p>Explore plain-English articles related to education, certification, and building a biomed career.</p>
        <div class="career-learning-grid">${cards}</div>
      </section>`;
  }).catch(() => {
    // This optional section stays absent when its data is unavailable.
  });
}());
