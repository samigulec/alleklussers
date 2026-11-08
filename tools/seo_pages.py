#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the SEO landing pages, sitemap.xml and robots.txt.

    python3 tools/seo_pages.py

Content lives in tools/seo_content.py. Each page is written to
/<slug>/index.html so it is served at https://www.alleklussers.nl/<slug>/.
Icons and characters are copied from the sprite in index.html, so the
pages always use the same artwork as the homepage.
"""
import datetime
import html
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from seo_content import AREAS_REGION, AREAS_ROTTERDAM, CITY_PAGES, PAGES  # noqa: E402

ALL_PAGES = PAGES + CITY_PAGES
CITY_LINKS = {p["city"]: p["slug"] for p in CITY_PAGES}

BASE = "https://www.alleklussers.nl"
PHONE_DISPLAY = "+31 6 8548 4000"
PHONE_TEL = "+31685484000"
WA = "https://wa.me/31685484000"
EMAIL = "alleklussers@gmail.com"
ASSET_V = "20261108"

ICONS = ["i-wa", "i-arrow", "i-check", "i-tag", "i-chat", "i-shield", "i-clock", "i-pin", "i-mail", "i-phone"]


def sprite():
    src = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
    out = []
    for m in re.finditer(r'<symbol id="([a-z0-9-]+)".*?</symbol>', src, re.S):
        sid = m.group(1)
        if sid in ICONS or sid.startswith("ch-"):
            out.append(m.group(0))
    have = " ".join(out)
    if 'id="i-phone"' not in have:
        out.append('<symbol id="i-phone" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="1.7" '
                   'stroke-linejoin="round" d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"/></symbol>')
    return ('<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false"><defs>\n'
            + "\n".join(out) + "\n</defs></svg>")


def icon(name, size=18):
    return f'<svg width="{size}" height="{size}" aria-hidden="true"><use href="#{name}"/></svg>'


CHECK = icon("i-check", 18)


def tiles(exclude=None):
    items = []
    for p in PAGES:
        if p.get("hub") or p.get("city") or p["slug"] == exclude:
            continue
        items.append(
            f'<a class="tile" href="/{p["slug"]}/"><span class="ch-tile ch-tile--{p["char"]}">'
            f'<svg class="ch" aria-hidden="true"><use href="#ch-{p["char"]}"/></svg></span>'
            f'<span><strong>{p["short"]}</strong><span class="tile__sub">{p["sub"]}</span></span></a>')
    return '<div class="tiles">' + "".join(items) + "</div>"


def areas():
    lis = "".join(
        f'<li><a href="/{CITY_LINKS[a]}/">{a}</a></li>' if a in CITY_LINKS else f"<li>{a}</li>"
        for a in AREAS_ROTTERDAM + AREAS_REGION)
    return f'<ul class="areas">{lis}</ul>'


def strip_tags(s):
    return re.sub(r"<[^>]+>", "", s)


def jsonld(p):
    url = f"{BASE}/{p['slug']}/"
    business = {
        "@type": "Electrician",
        "@id": f"{BASE}/#business",
        "name": "AlleKlussers",
        "url": f"{BASE}/",
        "logo": f"{BASE}/logo.png",
        "image": f"{BASE}/img/hero.jpg",
        "telephone": PHONE_DISPLAY,
        "email": EMAIL,
        "address": {"@type": "PostalAddress", "addressLocality": "Rotterdam", "addressCountry": "NL"},
        "areaServed": [{"@type": "City", "name": n} for n in ["Rotterdam"] + AREAS_REGION],
    }
    graph = []
    if p.get("hub"):
        graph.append(dict(business, description=p["desc"]))
    else:
        graph.append(business)
        graph.append({
            "@type": "Service",
            "name": p["service"],
            "serviceType": p["service"],
            "url": url,
            "description": p["desc"],
            "provider": {"@id": f"{BASE}/#business"},
            "areaServed": {"@type": "City", "name": p.get("city", "Rotterdam")},
        })
    graph.append({
        "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faq"]],
    })
    crumbs = [("Home", f"{BASE}/")]
    if not p.get("hub") and not p.get("city"):
        crumbs.append(("Elektricien Rotterdam", f"{BASE}/elektricien-rotterdam/"))
    crumbs.append((p["short"], url))
    graph.append({
        "@type": "BreadcrumbList",
        "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": u}
                            for i, (n, u) in enumerate(crumbs)],
    })
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=2)


def footer_services():
    return "".join(f'<li><a href="/{p["slug"]}/">{p["short"]}</a></li>' for p in PAGES)


def page(p, sprite_svg):
    url = f"{BASE}/{p['slug']}/"
    body = p["body"].format(check=CHECK, tiles=tiles(), areas=areas())
    faq = "".join(f"<details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>" for q, a in p["faq"])

    crumbs = '<a href="/">Home</a> <span aria-hidden="true">/</span> '
    if not p.get("hub") and not p.get("city"):
        crumbs += '<a href="/elektricien-rotterdam/">Elektricien Rotterdam</a> <span aria-hidden="true">/</span> '
    crumbs += f'<span aria-current="page">{p["short"]}</span>'

    extra = ""
    if p.get("city"):
        extra = f"""
  <section class="section" style="padding-top: 0">
    <div class="wrap prose">
      <h2>Onze <em>diensten.</em></h2>
      {tiles()}
      <h2>Ook in <em>de buurt.</em></h2>
      <p>We werken in heel Rotterdam en de gemeenten eromheen.</p>
      {areas()}
    </div>
  </section>"""
    elif not p.get("hub"):
        extra = f"""
  <section class="section" style="padding-top: 0">
    <div class="wrap prose">
      <h2>Andere diensten <em>in Rotterdam.</em></h2>
      {tiles(exclude=p["slug"])}
      <h2>Werkgebied</h2>
      <p>We werken in heel Rotterdam en de gemeenten eromheen.</p>
      {areas()}
    </div>
  </section>"""

    title = html.escape(p["title"])
    desc = html.escape(p["desc"])
    return f"""<!DOCTYPE html>
<html lang="nl" dir="ltr">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title}</title>
  <meta name="description" content="{desc}" />
  <link rel="canonical" href="{url}" />
  <link rel="icon" href="/icon.png" type="image/png" sizes="any" />
  <link rel="apple-touch-icon" href="/icon.png" />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="{url}" />
  <meta property="og:locale" content="nl_NL" />
  <meta property="og:site_name" content="AlleKlussers" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{desc}" />
  <meta property="og:image" content="{BASE}/img/hero.jpg" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="theme-color" content="#0c0c0d" />
  <script type="application/ld+json">
{jsonld(p)}
  </script>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;1,9..144,300;1,9..144,400&family=Manrope:wght@400;500;600;700;800&display=swap" />
  <link rel="stylesheet" href="/assets/site.css?v={ASSET_V}" />
  <link rel="stylesheet" href="/assets/seo.css?v={ASSET_V}" />
</head>
<body class="seo">

{sprite_svg}

<a class="skip" href="#main">Naar de inhoud</a>

<div class="topbar">
  <div class="wrap">
    <div class="topbar__group">
      <span class="topbar__item"><span class="dot dot--pulse" aria-hidden="true"></span><span>24/7 bereikbaar</span></span>
      <span class="topbar__item topbar__hide-sm">Verzekerde vakmensen</span>
      <span class="topbar__item topbar__hide-sm">Werken volgens NEN 1010</span>
    </div>
    <div class="topbar__group">
      <a href="{WA}" target="_blank" rel="noopener noreferrer">WhatsApp {PHONE_DISPLAY}</a>
      <a class="topbar__hide-sm" href="mailto:{EMAIL}">{EMAIL}</a>
    </div>
  </div>
</div>

<header class="header" id="header">
  <div class="wrap">
    <a class="brand" href="/" aria-label="AlleKlussers — Home">
      <img src="/img/logo-dark.png" alt="AlleKlussers" width="600" height="150" />
    </a>
    <nav class="nav" aria-label="Hoofdmenu">
      <a class="nav__link" href="/">Home</a>
      <a class="nav__link" href="/elektricien-rotterdam/">Diensten</a>
      <a class="nav__link" href="/#references">Projecten</a>
      <a class="nav__link" href="/#about">Over ons</a>
      <a class="nav__link" href="/#contact">Contact</a>
    </nav>
    <div class="header__actions">
      <a class="btn btn--ink btn--sm header__cta" href="/#contact">Offerte aanvragen</a>
      <a class="btn btn--ink btn--sm header__wa" href="{WA}" target="_blank" rel="noopener noreferrer">{icon("i-wa", 16)}WhatsApp</a>
    </div>
  </div>
</header>

<main id="main" tabindex="-1">

  <div class="page-head on-dark">
    <div class="wrap">
      <nav class="crumbs" aria-label="Kruimelpad">{crumbs}</nav>
      <p class="eyebrow eyebrow--dash" style="margin-top: 28px">{p["eyebrow"]}</p>
      <h1 class="h-page">{p["h1"]}</h1>
      <p class="lede">{p["lede"]}</p>
      <div class="seo-actions">
        <a class="btn btn--amber" href="{WA}" target="_blank" rel="noopener noreferrer">{icon("i-wa")}WhatsApp ons</a>
        <a class="btn btn--ghost" href="tel:{PHONE_TEL}">{icon("i-phone")}Bel {PHONE_DISPLAY}</a>
      </div>
      <div class="speaker page-head__buddy"><p class="say">{p["say"]}</p><svg class="ch ch-float speaker__ch ch-badge ch-badge--{p["char"]}" aria-hidden="true"><use href="#ch-{p["char"]}"/></svg></div>
    </div>
  </div>

  <section class="section">
    <div class="wrap seo-body">
      <div class="prose">
{body}
      </div>
      <aside class="seo-card" aria-label="Contact">
        <h2>Offerte of advies <em>nodig?</em></h2>
        <p>Stuur een berichtje met wat er moet gebeuren, eventueel met een foto. U krijgt binnen 24 uur reactie met een prijs.</p>
        <a class="btn btn--amber btn--block" href="{WA}" target="_blank" rel="noopener noreferrer">{icon("i-wa")}WhatsApp ons</a>
        <a class="btn btn--ghost btn--block" href="tel:{PHONE_TEL}">{icon("i-phone")}{PHONE_DISPLAY}</a>
        <a class="btn btn--ghost btn--block" href="mailto:{EMAIL}">{icon("i-mail")}{EMAIL}</a>
        <ul>
          <li>{icon("i-tag")}Duidelijke prijs vooraf</li>
          <li>{icon("i-clock")}Binnen 24 uur reactie</li>
          <li>{icon("i-shield")}Gecertificeerd en verzekerd</li>
        </ul>
      </aside>
    </div>
  </section>

  <section class="section section--sand">
    <div class="wrap prose">
      <h2>Veelgestelde <em>vragen.</em></h2>
      <div class="faq">{faq}</div>
    </div>
  </section>
{extra}
  <section class="section section--dark on-dark">
    <div class="wrap seo-cta">
      <h2 class="h-section">Elektra geregeld, <em>zonder gedoe.</em></h2>
      <div class="seo-actions" style="margin-top: 0">
        <a class="btn btn--amber" href="{WA}" target="_blank" rel="noopener noreferrer">{icon("i-wa")}WhatsApp ons</a>
        <a class="btn btn--ghost" href="/#contact">Offerte aanvragen {icon("i-arrow", 16)}</a>
      </div>
    </div>
  </section>

</main>

<footer class="footer">
  <div class="wrap footer__grid">
    <div class="footer__brand">
      <img src="/img/logo-light.png" alt="AlleKlussers" width="600" height="150" loading="lazy" />
      <p>Storingen, groepenkasten, verlichting, bedrading en veilige installaties — snel, veilig en netjes afgewerkt.</p>
    </div>
    <nav aria-labelledby="f-svc">
      <h2 id="f-svc">Diensten in Rotterdam</h2>
      <ul>{footer_services()}</ul>
    </nav>
    <nav aria-labelledby="f-co">
      <h2 id="f-co">Bedrijf</h2>
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/#references">Projecten</a></li>
        <li><a href="/#about">Over ons</a></li>
        <li><a href="/#contact">Contact</a></li>
      </ul>
    </nav>
    <div>
      <h2>Contact</h2>
      <ul>
        <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li><a href="{WA}" target="_blank" rel="noopener noreferrer">WhatsApp {PHONE_DISPLAY}</a></li>
        <li><a href="tel:{PHONE_TEL}">Bel {PHONE_DISPLAY}</a></li>
      </ul>
    </div>
  </div>
  <div class="wrap footer__bottom">
    <span>© {datetime.date.today().year} AlleKlussers · Onderdeel van Boss Tech VOF</span>
    <span>KvK 99149680 · BTW NL868827885B01</span>
  </div>
</footer>

<a class="fab" href="{WA}" target="_blank" rel="noopener noreferrer" aria-label="WhatsApp">{icon("i-wa", 28)}</a>

</body>
</html>
"""


def main():
    svg = sprite()
    today = datetime.date.today().isoformat()
    for p in ALL_PAGES:
        d = os.path.join(ROOT, p["slug"])
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
            f.write(page(p, svg))
        print("wrote", f"/{p['slug']}/")

    urls = [f"{BASE}/"] + [f"{BASE}/{p['slug']}/" for p in ALL_PAGES]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        sm.append(f"  <url><loc>{u}</loc><lastmod>{today}</lastmod></url>")
    sm.append("</urlset>\n")
    open(os.path.join(ROOT, "sitemap.xml"), "w").write("\n".join(sm))
    open(os.path.join(ROOT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")
    print("wrote /sitemap.xml and /robots.txt")


if __name__ == "__main__":
    main()
