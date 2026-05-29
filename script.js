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
  const GOOGLE_TAG_ID = 'G-BS4BHXX0XL';

  function loadGoogleTag() {
    if (window.gtag || document.querySelector(`script[src*="${GOOGLE_TAG_ID}"]`)) return;
    window.dataLayer = window.dataLayer || [];
    window.gtag = function gtag(){ window.dataLayer.push(arguments); };
    window.gtag('js', new Date());
    window.gtag('config', GOOGLE_TAG_ID);

    const script = document.createElement('script');
    script.async = true;
    script.src = `https://www.googletagmanager.com/gtag/js?id=${GOOGLE_TAG_ID}`;
    document.head.appendChild(script);
  }
  loadGoogleTag();

  function loadPolishStyles() {
    ['hero-overrides.css', 'about-overrides.css', 'mobile-overrides.css', 'services-overrides.css', 'services-polish.css', 'home-services-polish.css', 'home-services-fixes.css', 'topbar-polish.css', 'clients-polish.css'].forEach(href => {
      if (document.querySelector(`link[href="${href}"]`)) return;
      const link = document.createElement('link');
      link.rel = 'stylesheet';
      link.href = href;
      document.head.appendChild(link);
    });
  }
  loadPolishStyles();

  function polishClientQuotes() {
    const figures = Array.from(document.querySelectorAll('#view-references .quote-figure'));
    if (!figures.length) return;
    const wrap = figures[0].parentElement;
    if (wrap) wrap.classList.add('clients-testimonials');

    const quotes = [
      {
        name: '— Marleen & Tom',
        service: {
          nl: 'Storingen', en: 'Electrical fault', tr: 'Arıza', ar: 'أعطال كهربائية', pl: 'Awarie', de: 'Störung'
        },
        text: {
          nl: '“Snel geholpen bij een storing. Rustige communicatie, nette afwerking en geen verrassingen achteraf.”',
          en: '“Quick help with an electrical fault. Calm communication, tidy work and no surprises afterwards.”',
          tr: '“Elektrik arızasında hızlı yardımcı oldular. Sakin iletişim, temiz işçilik ve sonradan sürpriz yok.”',
          ar: '”ساعدونا بسرعة عند حدوث عطل كهربائي. تواصل واضح، عمل مرتب ولا مفاجآت لاحقاً.“',
          pl: '„Szybka pomoc przy awarii elektrycznej. Spokojna komunikacja, schludne wykonanie i bez niespodzianek.”',
          de: '„Schnelle Hilfe bei einer Störung. Ruhige Kommunikation, saubere Arbeit und keine Überraschungen danach.“'
        }
      },
      {
        name: '— Familie Yılmaz',
        service: {
          nl: 'Groepenkast', en: 'Consumer unit', tr: 'Sigorta panosu', ar: 'لوحة الكهرباء', pl: 'Rozdzielnica', de: 'Verteilerkasten'
        },
        text: {
          nl: '“Groepenkast netjes vervangen en alles duidelijk uitgelegd. Binnen één dag geregeld.”',
          en: '“The consumer unit was replaced neatly and everything was explained clearly. Arranged within one day.”',
          tr: '“Sigorta panosu temiz şekilde değiştirildi ve her şey net anlatıldı. Bir gün içinde tamamlandı.”',
          ar: '”تم استبدال لوحة الكهرباء بشكل مرتب وشرحوا كل شيء بوضوح. أُنجز العمل خلال يوم واحد.“',
          pl: '„Rozdzielnica została schludnie wymieniona, a wszystko jasno wyjaśniono. Załatwione w jeden dzień.”',
          de: '„Der Verteilerkasten wurde sauber ersetzt und alles klar erklärt. Innerhalb eines Tages erledigt.“'
        }
      },
      {
        name: '— S. Bakker',
        service: {
          nl: 'Verlichting', en: 'Lighting', tr: 'Aydınlatma', ar: 'إضاءة', pl: 'Oświetlenie', de: 'Beleuchtung'
        },
        text: {
          nl: '“Nieuwe stopcontacten en verlichting laten plaatsen. Alles strak afgewerkt en schoon achtergelaten.”',
          en: '“We had new sockets and lighting installed. Everything was finished sharply and left clean.”',
          tr: '“Yeni prizler ve aydınlatma yaptırdık. Her şey özenli tamamlandı ve temiz bırakıldı.”',
          ar: '”ركّبوا مقابس جديدة وإضاءة. كان التشطيب أنيقاً وتركوا المكان نظيفاً.“',
          pl: '„Zamontowano nowe gniazdka i oświetlenie. Wszystko starannie wykończone i zostawione czysto.”',
          de: '„Neue Steckdosen und Beleuchtung montieren lassen. Alles sauber ausgeführt und ordentlich hinterlassen.“'
        }
      }
    ];

    figures.forEach((figure, i) => {
      const q = quotes[i];
      if (!q) return;
      const block = figure.querySelector('blockquote');
      const caption = figure.querySelector('figcaption');
      if (block) {
        block.innerHTML = SUPPORTED_LANGS.map(lang => `<span class="lang-${lang}">${q.text[lang]}</span>`).join('');
      }
      // Service tag goes ABOVE the quote as a small category chip; name stays in figcaption.
      const existingChip = figure.querySelector('.client-quote__service');
      if (existingChip) existingChip.remove();
      const chip = document.createElement('span');
      chip.className = 'client-quote__service';
      chip.innerHTML = SUPPORTED_LANGS.map(lang => `<span class="lang-${lang}">${q.service[lang]}</span>`).join('');
      figure.insertBefore(chip, block || figure.firstChild);
      if (caption) {
        caption.textContent = q.name;
      }
    });
  }
  polishClientQuotes();

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

  // Project gallery lightbox — open from thumbnails or "Bekijk project" CTA,
  // navigate with arrows / keyboard, close with Escape or backdrop click.
  const lightbox = document.getElementById('project-lightbox');
  if (lightbox) {
    const lightboxImg = document.getElementById('project-lightbox-img');
    const counterEl = lightbox.querySelector('[data-lightbox-counter]');
    let currentPhotos = [];
    let currentIndex = 0;

    function showLightboxPhoto(i) {
      if (!currentPhotos.length) return;
      currentIndex = (i + currentPhotos.length) % currentPhotos.length;
      const photo = currentPhotos[currentIndex];
      lightboxImg.src = photo.src;
      lightboxImg.alt = photo.alt || '';
      if (counterEl) counterEl.textContent = (currentIndex + 1) + ' / ' + currentPhotos.length;
    }
    function openLightbox(galleryName, startIndex) {
      const gallery = document.querySelector('[data-gallery="' + galleryName + '"]');
      if (!gallery) return;
      currentPhotos = Array.from(gallery.querySelectorAll('img'));
      if (!currentPhotos.length) return;
      showLightboxPhoto(startIndex || 0);
      lightbox.classList.add('is-open');
      lightbox.setAttribute('aria-hidden', 'false');
      document.body.classList.add('lightbox-open');
    }
    function closeLightbox() {
      lightbox.classList.remove('is-open');
      lightbox.setAttribute('aria-hidden', 'true');
      document.body.classList.remove('lightbox-open');
    }

    document.querySelectorAll('[data-photo-index]').forEach(btn => {
      btn.addEventListener('click', () => {
        const gallery = btn.closest('[data-gallery]');
        const name = gallery && gallery.dataset.gallery;
        if (name) openLightbox(name, parseInt(btn.dataset.photoIndex, 10) || 0);
      });
    });
    document.querySelectorAll('[data-open-gallery]').forEach(btn => {
      btn.addEventListener('click', () => openLightbox(btn.dataset.openGallery, 0));
    });

    lightbox.querySelector('[data-lightbox-close]').addEventListener('click', closeLightbox);
    lightbox.querySelector('[data-lightbox-prev]').addEventListener('click', () => showLightboxPhoto(currentIndex - 1));
    lightbox.querySelector('[data-lightbox-next]').addEventListener('click', () => showLightboxPhoto(currentIndex + 1));
    lightbox.addEventListener('click', e => {
      if (e.target === lightbox) closeLightbox();
    });
    document.addEventListener('keydown', e => {
      if (!lightbox.classList.contains('is-open')) return;
      if (e.key === 'Escape') closeLightbox();
      else if (e.key === 'ArrowLeft') showLightboxPhoto(currentIndex - 1);
      else if (e.key === 'ArrowRight') showLightboxPhoto(currentIndex + 1);
    });
  }

  // Project carousel — horizontal swipe with arrows + dots (Reels-style).
  const carousel = document.querySelector('.project-carousel');
  if (carousel) {
    const track = carousel.querySelector('[data-carousel-track]');
    const slides = Array.from(track.querySelectorAll('.project-slide'));
    const prevBtn = carousel.querySelector('[data-carousel-prev]');
    const nextBtn = carousel.querySelector('[data-carousel-next]');
    const dotsWrap = carousel.querySelector('[data-carousel-dots]');
    let active = 0;

    // Build dots
    const dots = slides.map((_, i) => {
      const d = document.createElement('button');
      d.type = 'button';
      d.className = 'project-carousel__dot' + (i === 0 ? ' is-active' : '');
      d.setAttribute('aria-label', 'Project ' + (i + 1));
      d.addEventListener('click', () => goToSlide(i));
      dotsWrap.appendChild(d);
      return d;
    });

    function goToSlide(i) {
      active = Math.max(0, Math.min(slides.length - 1, i));
      track.scrollTo({ left: slides[active].offsetLeft - track.offsetLeft, behavior: 'smooth' });
      updateControls();
    }
    function updateControls() {
      dots.forEach((d, i) => d.classList.toggle('is-active', i === active));
      if (prevBtn) prevBtn.disabled = active === 0;
      if (nextBtn) nextBtn.disabled = active === slides.length - 1;
    }
    if (prevBtn) prevBtn.addEventListener('click', () => goToSlide(active - 1));
    if (nextBtn) nextBtn.addEventListener('click', () => goToSlide(active + 1));

    // Sync active dot when the user swipes/scrolls manually
    let scrollTimer;
    track.addEventListener('scroll', () => {
      clearTimeout(scrollTimer);
      scrollTimer = setTimeout(() => {
        const center = track.scrollLeft + track.clientWidth / 2;
        let nearest = 0, best = Infinity;
        slides.forEach((s, i) => {
          const sc = s.offsetLeft - track.offsetLeft + s.clientWidth / 2;
          const dist = Math.abs(sc - center);
          if (dist < best) { best = dist; nearest = i; }
        });
        active = nearest;
        updateControls();
      }, 90);
    }, { passive: true });

    updateControls();
  }
})();