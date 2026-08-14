(function () {
  const headings = document.querySelectorAll('main h3');
  let assetType = null;

  for (const h of headings) {
    if (h.textContent.trim() === 'Asset Type') {
      const next = h.nextElementSibling;
      if (next && next.tagName === 'P') {
        assetType = next.textContent.trim();
      }
      break;
    }
  }

  if (!assetType) return;

 const slug = assetType
  .toLowerCase()
  .replace(/[^a-z0-9]+/g, '-')
  .replace(/^-+|-+$/g, '');

  const iconPath = `/images/icons-asset/${slug}.png`;

  const hero = document.querySelector('.hero');
  if (!hero) return;

  let container = document.getElementById('guide-hero-icon');

  if (!container) {
    container = document.createElement('div');
    container.className = 'asset-hero-icon';
    container.id = 'guide-hero-icon';
    container.style.display = 'none';

    const img = document.createElement('img');
    img.id = 'guide-hero-img';
    container.appendChild(img);

    const subtitle = hero.querySelector('p');
    if (subtitle) {
      subtitle.insertAdjacentElement('beforebegin', container);
    } else {
      hero.appendChild(container);
    }
  }

  const img = container.querySelector('img');
  if (!img) return;

  img.src = iconPath;
  img.alt = `${assetType} icon`;

  img.onload = () => {
    container.style.display = 'flex';
  };

  img.onerror = () => {
    container.style.display = 'none';
  };
})();

// Guide pages already share this file, so it is the single low-maintenance
// entry point for site-wide footer enhancements.
(() => {
  if (document.querySelector('script[data-social-links]')) return;

  const socialScript = document.createElement('script');
  socialScript.src = new URL('social-links.js', document.currentScript.src).href;
  socialScript.defer = true;
  socialScript.dataset.socialLinks = '';
  document.head.appendChild(socialScript);
})();

// PM procedure pages use the same shared entry point to load their
// exact-model troubleshooting guide grid.
(() => {
  if (!window.location.pathname.includes('/preventive-maintenance/')) return;
  if (document.querySelector('script[data-pm-related-guides]')) return;

  const relatedScript = document.createElement('script');
  relatedScript.src = new URL('pm-related-guides.js', document.currentScript.src).href;
  relatedScript.defer = true;
  relatedScript.dataset.pmRelatedGuides = '';
  document.head.appendChild(relatedScript);
})();
