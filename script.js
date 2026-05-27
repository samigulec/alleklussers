// alleklussers — minimal nav + language toggle + WhatsApp deep-link

(function () {
  const root = document.documentElement;
  const navLinks = document.querySelectorAll('[data-nav]');
  const views = document.querySelectorAll('.view');
  const langButtons = document.querySelectorAll('[data-lang-set]');

  // International phone in wa.me format (digits only, no '+' or spaces).
  // Replace with the real number when known.
  const WA_PHONE = '31600000000';

  // Pre-filled openers per language and per section. The current section
  // tailors the message so the conversation starts with context.
  const WA_MESSAGES = {
    nl: {
      home:       'Hallo alleklussers, ik heb een vraag.',
      about:      'Hallo alleklussers, ik wil graag meer weten over jullie.',
      services:   'Hallo alleklussers, ik heb een vraag over jullie diensten.',
      references: 'Hallo alleklussers, ik heb een vraag naar aanleiding van jullie referenties.',
      contact:    'Hallo alleklussers, ik wil graag contact opnemen.',
    },
    en: {
      home:       'Hi alleklussers, I have a question.',
      about:      "Hi alleklussers, I'd like to know more about you.",
      services:   'Hi alleklussers, I have a question about your services.',
      references: 'Hi alleklussers, I have a question regarding your work.',
      contact:    "Hi alleklussers, I'd like to get in touch.",
    },
  };

  const waFab = document.getElementById('wa-fab');
  let currentLang = 'nl';
  let currentView = 'home';

  function updateWaLink() {
    if (!waFab) return;
    const msg = (WA_MESSAGES[currentLang] || WA_MESSAGES.nl)[currentView]
             || WA_MESSAGES[currentLang].home;
    waFab.href = `https://wa.me/${WA_PHONE}?text=${encodeURIComponent(msg)}`;
  }

  function showView(id) {
    currentView = id;
    views.forEach(v => v.classList.toggle('is-active', v.id === `view-${id}`));
    navLinks.forEach(n => n.classList.toggle('is-active', n.dataset.nav === id));
    window.scrollTo({ top: 0, behavior: 'instant' in window ? 'instant' : 'auto' });
    history.replaceState(null, '', `#${id}`);
    updateWaLink();
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
    updateWaLink();
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
  // Selecting any item inside also closes (handled below via nav-link click).
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
    // Close after any internal navigation
    more.querySelectorAll('a').forEach(a => a.addEventListener('click', closeMore));
  }

  // Contact form — client-side only for now.
  // Falls back to WhatsApp if the user prefers that channel.
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
