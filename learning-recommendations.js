(function () {
  function normalizeKey(value) {
    return (value || '')
      .toLowerCase()
      .trim()
      .replace(/[^a-z0-9]+/g, '-')
      .replace(/^-+|-+$/g, '');
  }

  function resolveConfiguredSlugs(context, learningMap) {
    const modelKey = [context.manufacturer, context.model]
      .map(normalizeKey)
      .join('--');
    const lookups = [
      [learningMap.issueOverrides, context.issueSlug],
      [learningMap.modelOverrides, modelKey],
      [learningMap.manufacturerOverrides, normalizeKey(context.manufacturer)],
      [learningMap.assetTypeDefaults, context.assetTypeSlug]
    ];

    for (const [mapping, key] of lookups) {
      if (!key || !mapping || !Object.prototype.hasOwnProperty.call(mapping, key)) continue;

      const configured = mapping[key];
      if (Array.isArray(configured)) return configured;
      if (
        typeof configured === 'string' &&
        learningMap.articleSets &&
        Array.isArray(learningMap.articleSets[configured])
      ) {
        return learningMap.articleSets[configured];
      }
      return [];
    }

    return [];
  }

  function findGuideMetadata() {
    const main = document.querySelector('main');
    if (!main) return null;

    function metadataValue(label) {
      const heading = Array.from(main.querySelectorAll('h3'))
        .find(item => item.textContent.trim() === label);
      return heading?.nextElementSibling?.textContent.trim() || '';
    }

    return {
      pageType: 'guide',
      issueSlug: window.location.pathname.split('/').pop().replace(/\.html$/, ''),
      assetType: metadataValue('Asset Type'),
      manufacturer: metadataValue('Manufacturer'),
      model: metadataValue('Model')
    };
  }

  function findInsertionPoint(pageType) {
    if (pageType === 'guide') {
      return Array.from(document.querySelectorAll('main h2'))
        .find(heading => heading.textContent.trim() === 'What This Guide Helps With');
    }
    return document.getElementById('section-issues') || document.getElementById('pm-section-wrap');
  }

  function createArticleLink(article) {
    const link = document.createElement('a');
    link.className = 'understand-basics-link';
    link.href = '/' + article.url.replace(/^\//, '');

    const title = document.createElement('strong');
    title.textContent = article.title;

    const note = document.createElement('span');
    note.textContent = article.cardNote || article.category || 'Biomed Basics';

    link.append(title, note);
    return link;
  }

  function render(context, learningMap, articles) {
    if (document.querySelector('.understand-before-troubleshoot')) return;

    const configuredSlugs = resolveConfiguredSlugs(context, learningMap);
    if (!configuredSlugs.length) return;

    const articlesBySlug = new Map(articles.map(article => [article.slug, article]));
    const matchedArticles = configuredSlugs
      .map(slug => articlesBySlug.get(slug))
      .filter(Boolean)
      .slice(0, 5);
    if (!matchedArticles.length) return;

    const insertionPoint = findInsertionPoint(context.pageType);
    if (!insertionPoint) return;

    const section = document.createElement('section');
    section.className = 'understand-before-troubleshoot';
    if (context.pageType !== 'guide') section.classList.add('hub-learning-recommendations');
    section.setAttribute('aria-labelledby', 'understand-before-troubleshoot-title');

    const heading = document.createElement('h2');
    heading.id = 'understand-before-troubleshoot-title';
    heading.textContent = 'Understand Before You Troubleshoot';

    const blurb = document.createElement('p');
    blurb.textContent = 'These Biomed Basics articles may provide helpful background:';

    const links = document.createElement('div');
    links.className = 'understand-basics-links';
    matchedArticles.forEach(article => links.appendChild(createArticleLink(article)));

    section.append(heading, blurb, links);
    insertionPoint.before(section);
  }

  async function load() {
    const path = window.location.pathname;
    const params = new URLSearchParams(window.location.search);
    const [learningMap, articles, assetHubs] = await Promise.all([
      fetch('/data/troubleshooting-learning-map.json').then(response => response.json()),
      fetch('/data/biomed-basics.json').then(response => response.json()),
      fetch('/data/hub-asset.json').then(response => response.json())
    ]);

    let context = null;
    if (path.endsWith('/hub-asset.html') || path.endsWith('hub-asset.html')) {
      const asset = assetHubs.find(item => item.slug === params.get('slug'));
      if (asset) context = { pageType: 'assetHub', assetType: asset.name, assetTypeSlug: asset.slug };
    } else if (path.endsWith('/hub-model.html') || path.endsWith('hub-model.html')) {
      const modelHubs = await fetch('/data/hub-model.json').then(response => response.json());
      const model = modelHubs.find(item => item.slug === params.get('slug'));
      if (model) {
        const asset = assetHubs.find(item => item.name === model.profile?.assetType);
        context = {
          pageType: 'modelHub',
          assetType: model.profile?.assetType || '',
          assetTypeSlug: asset?.slug || normalizeKey(model.profile?.assetType),
          manufacturer: model.profile?.manufacturer || '',
          model: model.name
        };
      }
    } else if (path.includes('/guides/')) {
      context = findGuideMetadata();
      if (context) {
        const asset = assetHubs.find(item => item.name === context.assetType);
        context.assetTypeSlug = asset?.slug || normalizeKey(context.assetType);
      }
    }

    if (context) render(context, learningMap, articles);
  }

  function start() {
    load().catch(error => console.error('Learning recommendations error:', error));
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', start);
  } else {
    start();
  }
})();
