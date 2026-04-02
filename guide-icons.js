(function () {
  // Find "Asset Type" value from the guide page
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

  // Convert to slug (Infusion Pump → infusion-pump)
  const slug = assetType
    .toLowerCase()
    .replace(/\s+/g, '-')
    .replace(/[^a-z0-9-]/g, '');

  const iconPath = `/images/icons-asset/${slug}.png`;

  // Get hero section
  const hero = document.querySelector('.hero');
  if (!hero) return;

  // Create container if it doesn't exist
  let container = document.getElementById('guide-hero-icon');

  if (!container) {
    container = document.createElement('div');
    container.className = 'asset-hero-icon';
container.id = 'guide-hero-icon';
    container.style.display = 'none';

    const img = document.createElement('img');
    img.id = 'guide-hero-img';
    container.appendChild(img);

    // Insert BEFORE the subtitle paragraph
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
