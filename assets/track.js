// AlleKlussers: measure clicks on WhatsApp, phone and e-mail links.
// Sends a GA4 event "contact_click" with method (whatsapp/phone/email),
// cta (where on the page) and the page path. On the landing pages it
// also loads the same Google tag the homepage uses.
(function () {
  'use strict';
  var GOOGLE_TAG_ID = 'G-BS4BHXX0XL';

  if (!window.gtag) {
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag('js', new Date());
    window.gtag('config', GOOGLE_TAG_ID);
    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + GOOGLE_TAG_ID;
    document.head.appendChild(s);
  }

  function methodOf(href) {
    if (/^https:\/\/(wa\.me|api\.whatsapp\.com)\//.test(href)) return 'whatsapp';
    if (href.indexOf('tel:') === 0) return 'phone';
    if (href.indexOf('mailto:') === 0) return 'email';
    return null;
  }

  document.addEventListener('click', function (e) {
    var a = e.target && e.target.closest ? e.target.closest('a[href]') : null;
    if (!a) return;
    var method = methodOf(a.getAttribute('href') || '');
    if (!method) return;
    var cta = a.getAttribute('data-cta') || (a.closest('[data-cta]') && a.closest('[data-cta]').getAttribute('data-cta')) || 'other';
    try {
      window.gtag('event', 'contact_click', {
        method: method,
        cta: cta,
        page_path: location.pathname + location.hash,
        transport_type: 'beacon'
      });
    } catch (err) { /* never block the click */ }
  }, true);
})();
