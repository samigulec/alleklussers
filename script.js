// KlusRegie 010 — minimal nav + language toggle

(function () {
  const root = document.documentElement;
  const navLinks = document.querySelectorAll('[data-nav]');
  const views = document.querySelectorAll('.view');
  const langButtons = document.querySelectorAll('[data-lang-set]');

  function showView(id) {
    views.forEach(v => v.classList.toggle('is-active', v.id === `view-${id}`));
    navLinks.forEach(n => n.classList.toggle('is-active', n.dataset.nav === id));
    window.scrollTo({ top: 0, behavior: 'instant' in window ? 'instant' : 'auto' });
    history.replaceState(null, '', `#${id}`);
  }

  navLinks.forEach(link => {
    link.addEventListener('click', e => {
      e.preventDefault();
      showView(link.dataset.nav);
      // Close mobile menu if open
      const menu = document.getElementById('mobile-menu');
      if (menu) menu.classList.add('hidden');
    });
  });

  function setLang(lang) {
    root.setAttribute('data-lang', lang);
    document.documentElement.lang = lang;
    langButtons.forEach(b => b.classList.toggle('is-active', b.dataset.langSet === lang));
    try { localStorage.setItem('kr010_lang', lang); } catch (e) {}
  }

  langButtons.forEach(b => {
    b.addEventListener('click', () => setLang(b.dataset.langSet));
  });

  // Init language
  let initialLang = 'nl';
  try {
    const saved = localStorage.getItem('kr010_lang');
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

  // Contact form — keep client-side only for now
  const form = document.getElementById('contact-form');
  if (form) {
    form.addEventListener('submit', e => {
      e.preventDefault();
      const status = document.getElementById('form-status');
      if (status) {
        status.classList.remove('hidden');
        form.reset();
      }
    });
  }
})();
