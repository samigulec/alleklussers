// alleklussers — minimal nav + language toggle + WhatsApp deep-link

(function () {
  const root = document.documentElement;
  const navLinks = document.querySelectorAll('[data-nav]');
  const views = document.querySelectorAll('.view');
  const langButtons = document.querySelectorAll('[data-lang-set]');

  // International phone in wa.me format (digits only, no '+' or spaces).
  // Replace with the real number when known.
  const WA_PHONE = '31600000000';

  // Time-aware greeting so the WA opener starts naturally ("Goedemorgen"
  // before noon, "Goedemiddag" until 18:00, "Goedenavond" after).
  function timeGreeting(lang) {
    const h = new Date().getHours();
    if (lang === 'nl') {
      if (h < 6)  return 'Goedenacht';
      if (h < 12) return 'Goedemorgen';
      if (h < 18) return 'Goedemiddag';
      return 'Goedenavond';
    }
    if (h < 12) return 'Good morning';
    if (h < 18) return 'Good afternoon';
    return 'Good evening';
  }

  // Per-section conversation opener (greeting prepended at build time).
  const WA_CONTEXT = {
    nl: {
      home:       'ik heb een vraag.',
      about:      'ik wil graag meer weten over jullie.',
      services:   'ik heb een vraag over jullie diensten.',
      references: 'ik heb een vraag naar aanleiding van een project.',
      contact:    'ik wil graag contact opnemen.',
    },
    en: {
      home:       'I have a question.',
      about:      "I'd like to know more about you.",
      services:   'I have a question about your services.',
      references: 'I have a question about one of your projects.',
      contact:    "I'd like to get in touch.",
    },
  };

  const waFab = document.getElementById('wa-fab');
  let currentLang = 'nl';
  let currentView = 'home';

  function updateWaLink() {
    if (!waFab) return;
    const ctx = (WA_CONTEXT[currentLang] || WA_CONTEXT.nl);
    const tail = ctx[currentView] || ctx.home;
    const msg = `${timeGreeting(currentLang)} AlleKlussers, ${tail}`;
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

  // Contact form — until a backend is wired up, hand off to the user's
  // mail client with all fields prefilled. Works on every device without
  // a server roundtrip and degrades gracefully.
  const form = document.getElementById('contact-form');
  if (form) {
    form.addEventListener('submit', e => {
      e.preventDefault();
      const data = new FormData(form);
      const name    = (data.get('name')    || '').toString().trim();
      const email   = (data.get('email')   || '').toString().trim();
      const message = (data.get('message') || '').toString().trim();
      const subject = currentLang === 'en'
        ? `New enquiry from ${name || 'website'}`
        : `Nieuwe aanvraag van ${name || 'website'}`;
      const body = currentLang === 'en'
        ? `Name: ${name}\nE-mail: ${email}\n\n${message}`
        : `Naam: ${name}\nE-mail: ${email}\n\n${message}`;
      const href = `mailto:hallo@alleklussers.nl`
        + `?subject=${encodeURIComponent(subject)}`
        + `&body=${encodeURIComponent(body)}`;
      window.location.href = href;

      const status = document.getElementById('form-status');
      if (status) {
        status.classList.remove('hidden');
        form.reset();
      }
    });
  }

  // Editorial scroll progress bar — width tracks scroll position within
  // the currently visible view (other views are display:none so they
  // don't contribute to scrollHeight).
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
