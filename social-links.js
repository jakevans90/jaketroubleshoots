(() => {
  'use strict';

  const SOCIAL_LINKS = Object.freeze([
    {
      name: 'Reddit',
      url: 'https://www.reddit.com/user/JakeTroubleshoots/',
      icon: 'reddit.svg'
    },
    {
      name: 'Facebook',
      url: 'https://www.facebook.com/JakeTroubleshoots/',
      icon: 'facebook.svg'
    },
    {
      name: 'Bluesky',
      url: 'https://bsky.app/profile/jaketroubleshoots.bsky.social',
      icon: 'bluesky.svg'
    }
  ]);

  const scriptUrl = new URL(document.currentScript.src, document.baseURI);
  const iconBaseUrl = new URL('images/social/', scriptUrl);

  function addSocialLinks() {
    const footer = document.querySelector('footer');
    if (!footer || footer.querySelector('.footer-social')) return;

    const section = document.createElement('section');
    section.className = 'footer-social';
    section.setAttribute('aria-labelledby', 'footer-social-heading');

    const heading = document.createElement('h2');
    heading.id = 'footer-social-heading';
    heading.className = 'footer-social__heading';
    heading.textContent = 'Follow JakeTroubleshoots';

    const links = document.createElement('div');
    links.className = 'footer-social__links';

    SOCIAL_LINKS.forEach(({ name, url, icon }) => {
      const link = document.createElement('a');
      link.className = 'footer-social__link';
      link.href = url;
      link.target = '_blank';
      link.rel = 'noopener noreferrer';
      link.title = `Follow JakeTroubleshoots on ${name}`;

      const image = document.createElement('img');
      image.className = 'footer-social__icon';
      image.src = new URL(icon, iconBaseUrl).href;
      image.alt = '';
      image.width = 18;
      image.height = 18;
      image.setAttribute('aria-hidden', 'true');

      const label = document.createElement('span');
      label.textContent = name;

      link.append(image, label);
      links.appendChild(link);
    });

    section.append(heading, links);
    footer.insertBefore(section, footer.firstChild);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', addSocialLinks, { once: true });
  } else {
    addSocialLinks();
  }
})();
