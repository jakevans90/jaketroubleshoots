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
    const findArticles = (slugs) => [...new Set(slugs)]
      .map((slug) => catalog.get(slug))
      .filter(Boolean);
    const educationMatches = findArticles(mapping.educationPage || []);
    const educationSlugs = new Set(educationMatches.map((article) => article.slug));
    const certificationMatches = findArticles(Object.values(mapping.certifications || {}).flat())
      .filter((article) => !educationSlugs.has(article.slug));
    const matches = [...educationMatches, ...certificationMatches];

    if (!matches.length) return;

    const makeCards = (articlesToRender) => articlesToRender.map((article) => `
      <a class="career-learning-card" href="${article.url}">
        <span>${article.badge || article.category || "Biomed Basics"}</span>
        <strong>${article.title}</strong>
        <small>${article.cardNote || article.description}</small>
      </a>`).join("");

    const groups = [
      ["Education Pathways", "Compare training routes, degree levels, and the knowledge that helps new biomeds get started.", educationMatches],
      ["Certification Guides", "Understand major credentials, eligibility, preparation, comparisons, and legacy certifications.", certificationMatches]
    ].filter(([, , groupArticles]) => groupArticles.length)
      .map(([title, description, groupArticles]) => `
        <div class="career-learning-group">
          <h4>${title}</h4>
          <p>${description}</p>
          <div class="career-learning-grid">${makeCards(groupArticles)}</div>
        </div>`).join("");

    root.innerHTML = `
      <section class="content-box career-learning-panel">
        <p class="section-kicker">Keep Learning</p>
        <h3>Related Biomed Basics</h3>
        <p>Explore plain-English articles related to education, certification, and building a biomed career.</p>
        ${groups}
      </section>`;
  }).catch(() => {
    // This optional section stays absent when its data is unavailable.
  });
}());
