// AlleKlussers — nav, language toggle, contact widget and page polish

(function () {
  const root = document.documentElement;
  const navLinks = document.querySelectorAll('[data-nav]');
  const views = document.querySelectorAll('.view');
  const langButtons = document.querySelectorAll('[data-lang-set]');
  const langSelect = document.querySelector('[data-lang-select]');
  const langSelectTrigger = langSelect && langSelect.querySelector('.lang-select__trigger');
  const langCodeLabel = document.querySelector('[data-lang-code]');

  const SUPPORTED_LANGS = ['nl', 'en', 'tr', 'ar', 'pl', 'de'];
  const RTL_LANGS = ['ar'];

  function loadPolishStyles() {
    ['hero-overrides.css', 'about-overrides.css', 'mobile-overrides.css', 'services-overrides.css'].forEach(href => {
      if (document.querySelector(`link[href="${href}"]`)) return;
      const link = document.createElement('link');
      link.rel = 'stylesheet';
      link.href = href;
      document.head.appendChild(link);
    });
  }
  loadPolishStyles();

  function closeMobileMenu() {
    const menuBtn = document.getElementById('menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    if (!menuBtn || !mobileMenu) return;
    mobileMenu.classList.remove('is-open');
    menuBtn.classList.remove('is-open');
    menuBtn.setAttribute('aria-expanded', 'false');
    document.body.classList.remove('menu-open');
  }

  function showView(id) {
    views.forEach(v => v.classList.toggle('is-active', v.id === `view-${id}`));
    navLinks.forEach(n => n.classList.toggle('is-active', n.dataset.nav === id));
    window.scrollTo({ top: 0, behavior: 'auto' });
    history.replaceState(null, '', `#${id}`);
  }

  navLinks.forEach(link => {
    link.addEventListener('click', e => {
      e.preventDefault();
      showView(link.dataset.nav);
      closeMobileMenu();
    });
  });

  function closeLangMenu() {
    if (!langSelect) return;
    langSelect.classList.remove('is-open');
    if (langSelectTrigger) langSelectTrigger.setAttribute('aria-expanded', 'false');
  }

  function setLang(lang) {
    if (!SUPPORTED_LANGS.includes(lang)) lang = 'nl';
    root.setAttribute('data-lang', lang);
    root.setAttribute('lang', lang);
    root.setAttribute('dir', RTL_LANGS.includes(lang) ? 'rtl' : 'ltr');
    langButtons.forEach(b => b.classList.toggle('is-active', b.dataset.langSet === lang));
    if (langCodeLabel) langCodeLabel.textContent = lang.toUpperCase();
    closeLangMenu();
    try { localStorage.setItem('ak_lang', lang); } catch (e) {}
  }

  langButtons.forEach(b => b.addEventListener('click', () => setLang(b.dataset.langSet)));

  if (langSelect && langSelectTrigger) {
    langSelectTrigger.addEventListener('click', e => {
      e.stopPropagation();
      const open = langSelect.classList.toggle('is-open');
      langSelectTrigger.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    document.addEventListener('click', e => {
      if (!langSelect.contains(e.target)) closeLangMenu();
    });
    document.addEventListener('keydown', e => {
      if (e.key === 'Escape') closeLangMenu();
    });
  }

  let initialLang = 'nl';
  try {
    const saved = localStorage.getItem('ak_lang');
    if (SUPPORTED_LANGS.includes(saved)) initialLang = saved;
    else if (navigator.language) {
      const browserLang = navigator.language.slice(0, 2).toLowerCase();
      if (SUPPORTED_LANGS.includes(browserLang)) initialLang = browserLang;
    }
  } catch (e) {}
  setLang(initialLang);

  const hash = window.location.hash.replace('#', '');
  const validViews = ['home', 'about', 'services', 'references', 'contact'];
  showView(validViews.includes(hash) ? hash : 'home');

  const menuBtn = document.getElementById('menu-btn');
  const mobileMenu = document.getElementById('mobile-menu');
  if (menuBtn && mobileMenu) {
    menuBtn.addEventListener('click', () => {
      const open = mobileMenu.classList.toggle('is-open');
      menuBtn.classList.toggle('is-open', open);
      menuBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
      document.body.classList.toggle('menu-open', open);
    });
    document.addEventListener('keydown', e => {
      if (e.key === 'Escape') closeMobileMenu();
    });
    mobileMenu.querySelectorAll('.mobile-menu__contact').forEach(a => a.addEventListener('click', closeMobileMenu));
  }

  const more = document.querySelector('[data-more]');
  if (more) {
    const trigger = more.querySelector('.nav-more__trigger');
    const closeMore = () => {
      more.classList.remove('is-open');
      if (trigger) trigger.setAttribute('aria-expanded', 'false');
    };
    if (trigger) {
      trigger.addEventListener('click', e => {
        e.stopPropagation();
        const open = more.classList.toggle('is-open');
        trigger.setAttribute('aria-expanded', open ? 'true' : 'false');
      });
    }
    document.addEventListener('click', e => {
      if (!more.contains(e.target)) closeMore();
    });
    document.addEventListener('keydown', e => {
      if (e.key === 'Escape') closeMore();
    });
    more.querySelectorAll('a').forEach(a => a.addEventListener('click', closeMore));
  }

  const widget = document.getElementById('contact-widget');
  if (widget) {
    const fab = widget.querySelector('#contact-fab');
    const closeBtn = widget.querySelector('#contact-pop-close');
    const setOpen = open => {
      widget.classList.toggle('is-open', open);
      if (fab) fab.setAttribute('aria-expanded', open ? 'true' : 'false');
    };
    if (fab) fab.addEventListener('click', e => {
      e.stopPropagation();
      setOpen(!widget.classList.contains('is-open'));
    });
    if (closeBtn) closeBtn.addEventListener('click', () => setOpen(false));
    document.addEventListener('click', e => {
      if (!widget.contains(e.target)) setOpen(false);
    });
    document.addEventListener('keydown', e => {
      if (e.key === 'Escape') setOpen(false);
    });
  }

  const progressEl = document.getElementById('scroll-progress');
  if (progressEl) {
    const updateProgress = () => {
      const max = document.documentElement.scrollHeight - window.innerHeight;
      const pct = max > 0 ? Math.min(100, (window.scrollY / max) * 100) : 0;
      progressEl.style.width = pct + '%';
    };
    window.addEventListener('scroll', updateProgress, { passive: true });
    window.addEventListener('resize', updateProgress);
    updateProgress();
  }
})();