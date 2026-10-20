// AlleKlussers — language, views, menu, gallery and quote form.
(function () {
  'use strict';

  var LANGS = window.AK_LANGS || ['nl'];
  var DICT = window.AK_I18N || {};
  var RTL = ['ar'];
  var VIEWS = ['home', 'services', 'references', 'about', 'contact'];
  var WHATSAPP = '31685484000';
  var EMAIL = 'info@alleklussers.nl';
  var GOOGLE_TAG_ID = 'G-BS4BHXX0XL';
  var root = document.documentElement;
  var lang = 'nl';

  function $(sel, ctx) { return (ctx || document).querySelector(sel); }
  function $$(sel, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(sel)); }
  function t(key) {
    var row = DICT[key];
    if (!row) return '';
    return row[LANGS.indexOf(lang)] || row[0];
  }

  /* ---------- Analytics (unchanged from the old site) ---------- */
  (function loadGoogleTag() {
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag('js', new Date());
    window.gtag('config', GOOGLE_TAG_ID);
    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + GOOGLE_TAG_ID;
    document.head.appendChild(s);
  })();

  /* ---------- Templates ---------- */
  function fill(selector, tplId, prefixAttr) {
    var tpl = document.getElementById(tplId);
    $$(selector).forEach(function (host) {
      var html = tpl.innerHTML;
      if (prefixAttr) html = html.replace(/\{p\}/g, 'q-' + host.getAttribute(prefixAttr));
      host.innerHTML = html;
    });
  }
  fill('[data-contact-links]', 'tpl-contact-links');
  fill('[data-strip]', 'tpl-strip');
  fill('[data-reviews]', 'tpl-reviews');
  fill('[data-qform]', 'tpl-qform', 'data-qform');

  /* ---------- Language ---------- */
  function applyLang() {
    $$('[data-i18n]').forEach(function (el) {
      var v = t(el.getAttribute('data-i18n'));
      if (v) el.innerHTML = v;
    });
    $$('[data-i18n-attr]').forEach(function (el) {
      el.getAttribute('data-i18n-attr').split(',').forEach(function (pair) {
        var p = pair.split(':');
        var v = t(p[1]);
        if (v) el.setAttribute(p[0], v);
      });
    });
    renderChips();
  }

  function setLang(next) {
    lang = LANGS.indexOf(next) > -1 ? next : 'nl';
    root.setAttribute('lang', lang);
    root.setAttribute('dir', RTL.indexOf(lang) > -1 ? 'rtl' : 'ltr');
    var code = $('[data-lang-code]');
    if (code) code.textContent = lang.toUpperCase();
    $$('[data-set-lang]').forEach(function (b) {
      b.setAttribute('aria-checked', b.getAttribute('data-set-lang') === lang ? 'true' : 'false');
    });
    applyLang();
    try { localStorage.setItem('ak_lang', lang); } catch (e) {}
  }

  var langBox = $('[data-lang]');
  var langBtn = langBox && $('.lang__btn', langBox);
  function closeLang() {
    if (!langBox) return;
    langBox.classList.remove('is-open');
    langBtn.setAttribute('aria-expanded', 'false');
  }
  if (langBox) {
    langBtn.addEventListener('click', function (e) {
      e.stopPropagation();
      var open = langBox.classList.toggle('is-open');
      langBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    $$('[data-set-lang]').forEach(function (b) {
      b.addEventListener('click', function (e) {
        setLang(b.getAttribute('data-set-lang'));
        closeLang();
        if (e.detail === 0) langBtn.focus(); // keyboard: keep focus on the switcher
      });
    });
    document.addEventListener('click', function (e) { if (!langBox.contains(e.target)) closeLang(); });
  }

  /* ---------- Mobile menu ---------- */
  var header = $('#header');
  var burger = $('#burger');
  var menu = $('#mobile-menu');
  function setHeaderHeight() {
    root.style.setProperty('--header-h', header.getBoundingClientRect().bottom + 'px');
  }
  function closeMenu() {
    if (!menu) return;
    menu.classList.remove('is-open');
    burger.setAttribute('aria-expanded', 'false');
    document.body.classList.remove('no-scroll');
  }
  if (burger && menu) {
    burger.addEventListener('click', function () {
      setHeaderHeight();
      var open = menu.classList.toggle('is-open');
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
      document.body.classList.toggle('no-scroll', open);
    });
  }
  window.addEventListener('scroll', function () {
    header.classList.toggle('is-scrolled', window.scrollY > 8);
  }, { passive: true });

  /* ---------- Views (hash routing, keeps the old #services etc. links working) ---------- */
  var pendingScroll = null;
  function showView(id, focus) {
    if (VIEWS.indexOf(id) < 0) id = 'home';
    $$('.view').forEach(function (v) { v.classList.toggle('is-active', v.id === 'view-' + id); });
    $$('[data-nav]').forEach(function (a) {
      var on = a.getAttribute('data-nav') === id;
      a.classList.toggle('is-active', on);
      if (a.classList.contains('nav__link')) {
        if (on) a.setAttribute('aria-current', 'page'); else a.removeAttribute('aria-current');
      }
    });
    closeMenu();
    var target = pendingScroll && document.getElementById(pendingScroll);
    pendingScroll = null;
    if (target) {
      setTimeout(function () { target.scrollIntoView({ behavior: 'smooth', block: 'start' }); }, 30);
    } else {
      window.scrollTo(0, 0);
    }
    if (focus) {
      var h = $('#view-' + id + ' h1');
      if (h) { h.setAttribute('tabindex', '-1'); h.focus({ preventScroll: true }); }
    }
    if (focus && window.gtag) window.gtag('event', 'page_view', { page_title: id, page_location: location.href });
  }

  document.addEventListener('click', function (e) {
    var a = e.target.closest('[data-nav]');
    if (!a) return;
    e.preventDefault();
    var id = a.getAttribute('data-nav');
    pendingScroll = a.getAttribute('data-scroll');
    var svc = a.getAttribute('data-service');
    if (svc) preselect(svc);
    if (location.hash !== '#' + id) history.pushState(null, '', '#' + id);
    showView(id, true);
  });
  window.addEventListener('popstate', function () { showView(location.hash.slice(1)); });
  window.addEventListener('hashchange', function () { showView(location.hash.slice(1)); });

  document.addEventListener('keydown', function (e) {
    if (e.key !== 'Escape') return;
    closeLang();
    closeMenu();
    closeLightbox();
  });

  /* ---------- Reveal on scroll ---------- */
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('is-in'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    $$('.reveal').forEach(function (el) { io.observe(el); });
  } else {
    $$('.reveal').forEach(function (el) { el.classList.add('is-in'); });
  }

  /* ---------- Lightbox ---------- */
  var lb = $('#lightbox');
  var lbImg = $('#lightbox-img');
  var lbCount = $('#lightbox-count');
  var photos = [];
  var index = 0;
  var lastFocus = null;
  function showPhoto(i) {
    index = (i + photos.length) % photos.length;
    var img = photos[index];
    lbImg.src = img.getAttribute('data-full') || img.src;
    lbImg.alt = img.alt;
    lbCount.textContent = (index + 1) + ' / ' + photos.length;
  }
  function openLightbox(name, start) {
    var g = $('[data-gallery="' + name + '"]');
    if (!g) return;
    photos = $$('img', g);
    lastFocus = document.activeElement;
    showPhoto(start || 0);
    lb.hidden = false;
    lb.classList.add('is-open');
    document.body.classList.add('no-scroll');
    $('[data-lb="close"]', lb).focus();
  }
  function closeLightbox() {
    if (!lb || lb.hidden) return;
    lb.classList.remove('is-open');
    lb.hidden = true;
    document.body.classList.remove('no-scroll');
    if (lastFocus) lastFocus.focus();
  }
  $$('[data-gallery]').forEach(function (g) {
    $$('[data-index]', g).forEach(function (btn) {
      btn.addEventListener('click', function () {
        openLightbox(g.getAttribute('data-gallery'), parseInt(btn.getAttribute('data-index'), 10));
      });
    });
  });
  $$('[data-open-gallery]').forEach(function (btn) {
    btn.addEventListener('click', function () { openLightbox(btn.getAttribute('data-open-gallery'), 0); });
  });
  if (lb) {
    lb.addEventListener('click', function (e) {
      var act = e.target.closest('[data-lb]');
      if (act) {
        var a = act.getAttribute('data-lb');
        if (a === 'close') closeLightbox();
        if (a === 'prev') showPhoto(index - (root.dir === 'rtl' ? -1 : 1));
        if (a === 'next') showPhoto(index + (root.dir === 'rtl' ? -1 : 1));
      } else if (e.target === lb) {
        closeLightbox();
      }
    });
    document.addEventListener('keydown', function (e) {
      if (lb.hidden) return;
      if (e.key === 'ArrowLeft') showPhoto(index - 1);
      if (e.key === 'ArrowRight') showPhoto(index + 1);
      if (e.key === 'Tab') {
        var f = $$('button', lb);
        var first = f[0], last = f[f.length - 1];
        if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
        else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
      }
    });
  }

  /* ---------- Quote form → WhatsApp or e-mail ---------- */
  var SERVICES = ['svc.1', 'svc.2', 'svc.3', 'svc.4', 'svc.5', 'svc.6', 'svc.7', 'other'];
  var forms = $$('.qform');
  forms.forEach(function (f) { f._service = 'svc.1'; });

  function chipLabel(key) { return key === 'other' ? t('form.other') : t(key); }

  function renderChips() {
    forms.forEach(function (form) {
      var box = $('[data-chips]', form);
      box.innerHTML = '';
      SERVICES.forEach(function (key) {
        var b = document.createElement('button');
        b.type = 'button';
        b.className = 'chip';
        b.textContent = chipLabel(key);
        b.setAttribute('aria-pressed', form._service === key ? 'true' : 'false');
        b.addEventListener('click', function () {
          form._service = key;
          $$('.chip', box).forEach(function (c) { c.setAttribute('aria-pressed', c === b ? 'true' : 'false'); });
        });
        box.appendChild(b);
        box.appendChild(document.createTextNode(' '));
      });
    });
  }
  function preselect(key) {
    forms.forEach(function (f) { f._service = SERVICES.indexOf(key) > -1 ? key : 'other'; });
    renderChips();
  }

  forms.forEach(function (form) {
    var via = 'wa';
    $$('[data-send]', form).forEach(function (b) {
      b.addEventListener('click', function () { via = b.getAttribute('data-send'); });
    });
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var name = form.elements.name;
      var desc = form.elements.desc;
      var err = $('[data-error]', form);
      var ok = true;
      [name, desc].forEach(function (el) {
        var bad = !el.value.trim();
        el.setAttribute('aria-invalid', bad ? 'true' : 'false');
        if (bad) ok = false;
      });
      err.classList.toggle('is-shown', !ok);
      if (!ok) { (name.value.trim() ? desc : name).focus(); return; }

      var lines = [
        t('msg.intro'),
        '',
        t('form.name') + ': ' + name.value.trim()
      ];
      var pc = form.elements.postcode.value.trim();
      var city = form.elements.city.value.trim();
      if (pc || city) lines.push(t('form.postcode') + ' / ' + t('form.city') + ': ' + [pc, city].filter(Boolean).join(' '));
      lines.push(t('form.type') + ': ' + chipLabel(form._service));
      lines.push('');
      lines.push(desc.value.trim());
      var text = lines.join('\n');

      if (window.gtag) window.gtag('event', 'generate_lead', { method: via, service: form._service });
      if (via === 'mail') {
        location.href = 'mailto:' + EMAIL + '?subject=' + encodeURIComponent(t('msg.subject') + ' — ' + chipLabel(form._service)) + '&body=' + encodeURIComponent(text);
      } else {
        window.open('https://wa.me/' + WHATSAPP + '?text=' + encodeURIComponent(text), '_blank', 'noopener');
      }
    });
  });

  /* ---------- Talking cast ---------- */
  $$('[data-cast]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      $$('[data-cast]').forEach(function (b) { b.setAttribute('aria-pressed', b === btn ? 'true' : 'false'); });
    });
  });

  /* ---------- Start ---------- */
  var year = $('[data-year]');
  if (year) year.textContent = new Date().getFullYear();

  var initial = 'nl';
  try {
    var saved = localStorage.getItem('ak_lang');
    if (LANGS.indexOf(saved) > -1) initial = saved;
    else if (navigator.language && LANGS.indexOf(navigator.language.slice(0, 2).toLowerCase()) > -1) {
      initial = navigator.language.slice(0, 2).toLowerCase();
    }
  } catch (e) {}
  setLang(initial);
  showView(location.hash.slice(1));
})();
