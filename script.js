// AlleKlussers — minimal nav + language toggle + scroll progress

(function () {
  const root = document.documentElement;
  const navLinks = document.querySelectorAll('[data-nav]');
  const views = document.querySelectorAll('.view');
  const langButtons = document.querySelectorAll('[data-lang-set]');

  let currentLang = 'nl';
  let currentView = 'home';

  function showView(id) {
    currentView = id;
    views.forEach(v => v.classList.toggle('is-active', v.id === `view-${id}`));
    navLinks.forEach(n => n.classList.toggle('is-active', n.dataset.nav === id));
    window.scrollTo({ top: 0, behavior: 'instant' in window ? 'instant' : 'auto' });
    history.replaceState(null, '', `#${id}`);
  }

  navLinks.forEach(link => {
    link.addEventListener('click', e => {
      e.preventDefault();
      showView(link.dataset.nav);
      const menu = document.getElementById('mobile-menu');
      if (menu) menu.classList.add('hidden');
    });
  });

  function setLang(lang) {
    currentLang = lang;
    root.setAttribute('data-lang', lang);
    document.documentElement.lang = lang;
    langButtons.forEach(b => b.classList.toggle('is-active', b.dataset.langSet === lang));
    try { localStorage.setItem('ak_lang', lang); } catch (e) {}
  }

  langButtons.forEach(b => {
    b.addEventListener('click', () => setLang(b.dataset.langSet));
  });

  // Init language
  let initialLang = 'nl';
  try {
    const saved = localStorage.getItem('ak_lang');
    if (saved === 'en' || saved === 'nl') initialLang = saved;
  } catch (e) {}
  setLang(initialLang);

  // Init view from hash
  const hash = window.location.hash.replace('#', '');
  const validViews = ['home', 'about', 'services', 'references', 'contact'];
  showView(validViews.includes(hash) ? hash : 'home');

  // Mobile menu toggle
  const menuBtn = document.getElementById('menu-btn');
  const menu = document.getElementById('mobile-menu');
  if (menuBtn && menu) {
    menuBtn.addEventListener('click', () => menu.classList.toggle('hidden'));
  }

  // "Meer" dropdown — click to toggle, outside-click and Escape close.
  const more = document.querySelector('[data-more]');
  if (more) {
    const trigger = more.querySelector('.nav-more__trigger');
    const closeMore = () => {
      more.classList.remove('is-open');
      trigger.setAttribute('aria-expanded', 'false');
    };
    const toggleMore = () => {
      const open = more.classList.toggle('is-open');
      trigger.setAttribute('aria-expanded', open ? 'true' : 'false');
    };
    trigger.addEventListener('click', e => {
      e.stopPropagation();
      toggleMore();
    });
    document.addEventListener('click', e => {
      if (!more.contains(e.target)) closeMore();
    });
    document.addEventListener('keydown', e => {
      if (e.key === 'Escape') closeMore();
    });
    more.querySelectorAll('a').forEach(a => a.addEventListener('click', closeMore));
  }

  // Floating contact widget — toggle popover, close on outside click / Esc
  const widget = document.getElementById('contact-widget');
  if (widget) {
    const fab = widget.querySelector('#contact-fab');
    const pop = widget.querySelector('#contact-pop');
    const closeBtn = widget.querySelector('#contact-pop-close');
    const setOpen = (open) => {
      widget.classList.toggle('is-open', open);
      fab.setAttribute('aria-expanded', open ? 'true' : 'false');
    };
    fab.addEventListener('click', e => {
      e.stopPropagation();
      setOpen(!widget.classList.contains('is-open'));
    });
    closeBtn.addEventListener('click', () => setOpen(false));
    document.addEventListener('click', e => {
      if (!widget.contains(e.target)) setOpen(false);
    });
    document.addEventListener('keydown', e => {
      if (e.key === 'Escape') setOpen(false);
    });
  }

  // Hero bulb interactivity — composes a slow pendulum sway with a
  // mouse-tracking tilt and adds a click flash. SVG `transform` attribute
  // is used (not CSS) so both rotations multiply into one matrix without
  // fighting each other. Skipped entirely when prefers-reduced-motion.
  (function initHeroBulb() {
    const heroArt = document.querySelector('.hero-art');
    if (!heroArt) return;
    const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (reduceMotion) return;
    const bulb = heroArt.querySelector('.hero-bulb');
    if (!bulb) return;

    let mouseInside = false;
    let mouseFrac = 0.5;       // 0 (left) to 1 (right) inside the art region
    let currentTilt = 0;       // damped follow of mouseTilt target

    heroArt.addEventListener('mouseenter', () => { mouseInside = true; });
    heroArt.addEventListener('mouseleave', () => { mouseInside = false; });
    heroArt.addEventListener('mousemove', e => {
      const rect = heroArt.getBoundingClientRect();
      mouseFrac = Math.max(0, Math.min(1, (e.clientX - rect.left) / rect.width));
    });

    heroArt.addEventListener('click', () => {
      heroArt.classList.add('is-flashing');
      setTimeout(() => heroArt.classList.remove('is-flashing'), 700);
    });

    function tick(t) {
      // Base pendulum: ~7s period, ±0.6deg amplitude
      const sway = Math.sin(t / 1115) * 0.6;
      // Mouse-aware tilt: up to ±4deg, only while cursor is inside
      const targetTilt = mouseInside ? (mouseFrac - 0.5) * 8 : 0;
      currentTilt += (targetTilt - currentTilt) * 0.06;
      const angle = (sway + currentTilt).toFixed(3);
      // Rotate around (200, 0) — the top of the cord in viewBox space
      bulb.setAttribute('transform', `rotate(${angle} 200 0)`);
      requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
  })();

  // Editorial scroll progress bar
  const progressEl = document.getElementById('scroll-progress');
  if (progressEl) {
    let ticking = false;
    const updateProgress = () => {
      const max = document.documentElement.scrollHeight - window.innerHeight;
      const pct = max > 0 ? Math.min(100, (window.scrollY / max) * 100) : 0;
      progressEl.style.width = pct + '%';
      ticking = false;
    };
    const onScroll = () => {
      if (!ticking) {
        requestAnimationFrame(updateProgress);
        ticking = true;
      }
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', onScroll);
    updateProgress();
  }
})();
