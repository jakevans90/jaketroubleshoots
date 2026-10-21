(() => {
  'use strict';

  const root = document.documentElement;
  if (root.dataset.mobileHeaderReady === 'true') return;
  root.dataset.mobileHeaderReady = 'true';

  const COMPACT_AFTER = 64;
  const mobileViewport = window.matchMedia('(max-width: 640px)');

  function initializeMobileHeader() {
    const header = document.querySelector('header');
    if (!header) return;

    let scheduled = false;

    function updateHeader() {
      header.classList.toggle(
        'mobile-header--compact',
        mobileViewport.matches && window.scrollY >= COMPACT_AFTER
      );
      scheduled = false;
    }

    function scheduleUpdate() {
      if (scheduled) return;
      scheduled = true;
      window.requestAnimationFrame(updateHeader);
    }

    window.addEventListener('scroll', scheduleUpdate, { passive: true });
    mobileViewport.addEventListener('change', updateHeader);
    updateHeader();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initializeMobileHeader, { once: true });
  } else {
    initializeMobileHeader();
  }
})();
