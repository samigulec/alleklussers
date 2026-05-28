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
      closeMobileMenu();
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

  // Mobile menu — full overlay, hamburger morph, body scroll lock,
  // outside click and Escape close.
  const menuBtn = document.getElementById('menu-btn');
  const mobileMenu = document.getElementById('mobile-menu');
  function openMobileMenu() {
    if (!menuBtn || !mobileMenu) return;
    mobileMenu.classList.add('is-open');
    menuBtn.classList.add('is-open');
    menuBtn.setAttribute('aria-expanded', 'true');
    document.body.classList.add('menu-open');
  }
  function closeMobileMenu() {
    if (!menuBtn || !mobileMenu) return;
    mobileMenu.classList.remove('is-open');
    menuBtn.classList.remove('is-open');
    menuBtn.setAttribute('aria-expanded', 'false');
    document.body.classList.remove('menu-open');
  }
  if (menuBtn && mobileMenu) {
    menuBtn.addEventListener('click', () => {
      if (mobileMenu.classList.contains('is-open')) closeMobileMenu();
      else openMobileMenu();
    });
    document.addEventListener('keydown', e => {
      if (e.key === 'Escape' && mobileMenu.classList.contains('is-open')) closeMobileMenu();
    });
    // Closing footer-contact links should also dismiss the menu
    mobileMenu.querySelectorAll('.mobile-menu__contact').forEach(a =>
      a.addEventListener('click', closeMobileMenu)
    );
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

  // Hero bulb interactivity — pendulum sway, mouse-tracking tilt, cord
  // bend toward the cursor, click flash, and random sparks at intervals.
  // All rotations write to a single SVG `transform` attribute so they
  // compose cleanly. Skipped entirely when prefers-reduced-motion.
  (function initHeroBulb() {
    const heroArt = document.querySelector('.hero-art');
    if (!heroArt) return;
    const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (reduceMotion) return;
    const bulb = heroArt.querySelector('.hero-bulb');
    const cord = heroArt.querySelector('#hero-cord');
    const svg  = heroArt.querySelector('svg');
    if (!bulb || !svg) return;

    let mouseInside = false;
    let mouseFrac = 0.5;       // 0 (left) to 1 (right) inside the art region
    let currentTilt = 0;       // damped tilt (degrees)
    let currentCordBend = 0;   // damped cord-control-point x offset

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
      const sway = Math.sin(t / 1115) * 0.6;
      const targetTilt = mouseInside ? (mouseFrac - 0.5) * 8 : 0;
      currentTilt += (targetTilt - currentTilt) * 0.06;
      const angle = (sway + currentTilt).toFixed(3);
      bulb.setAttribute('transform', `rotate(${angle} 200 0)`);

      if (cord) {
        // Cord flexes toward cursor with its own slower damping —
        // the bend lags behind the rotation, like a wire catching up.
        const targetBend = mouseInside ? (mouseFrac - 0.5) * 28 : 0;
        currentCordBend += (targetBend - currentCordBend) * 0.045;
        cord.setAttribute('d', `M 200 0 Q ${(200 + currentCordBend).toFixed(1)} 70 200 138`);
      }

      requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);

    // Random electrical sparks — small radial bursts that pop on briefly
    // every 15-25s at one of a handful of positions around the bulb.
    const SVG_NS = 'http://www.w3.org/2000/svg';
    const sparkPositions = [
      { x: 60,  y: 244 }, { x: 340, y: 250 },
      { x: 80,  y: 360 }, { x: 322, y: 360 },
      { x: 100, y: 208 }, { x: 304, y: 210 },
      { x: 120, y: 420 }, { x: 282, y: 420 },
      { x: 50,  y: 312 }, { x: 354, y: 312 },
    ];
    function buildSpark() {
      const g = document.createElementNS(SVG_NS, 'g');
      g.setAttribute('class', 'hero-spark');
      g.setAttribute('stroke', 'currentColor');
      g.setAttribute('stroke-width', '1.4');
      g.setAttribute('stroke-linecap', 'round');
      const lines = [
        [0, -9, 0, -3], [0, 3, 0, 9],
        [-9, 0, -3, 0], [3, 0, 9, 0],
        [-6.5, -6.5, -2.5, -2.5], [2.5, 2.5, 6.5, 6.5],
        [-6.5, 6.5, -2.5, 2.5], [2.5, -2.5, 6.5, -6.5],
      ];
      lines.forEach(([x1, y1, x2, y2]) => {
        const l = document.createElementNS(SVG_NS, 'line');
        l.setAttribute('x1', x1); l.setAttribute('y1', y1);
        l.setAttribute('x2', x2); l.setAttribute('y2', y2);
        g.appendChild(l);
      });
      return g;
    }
    function spawnSpark() {
      const pos = sparkPositions[Math.floor(Math.random() * sparkPositions.length)];
      const wrap = document.createElementNS(SVG_NS, 'g');
      wrap.setAttribute('transform', `translate(${pos.x} ${pos.y})`);
      const spark = buildSpark();
      wrap.appendChild(spark);
      svg.appendChild(wrap);
      requestAnimationFrame(() => spark.classList.add('is-active'));
      setTimeout(() => wrap.remove(), 1100);
      // Next one in 15-25s
      setTimeout(spawnSpark, 15000 + Math.random() * 10000);
    }
    setTimeout(spawnSpark, 5000);  // first spark ~5s after load
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
