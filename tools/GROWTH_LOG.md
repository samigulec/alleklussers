# Growth log

Running log of the daily website/SEO improvements. One line per run, newest at the bottom.
Public repo: no prices, margins or internal business details here.

## Log

- 2026-11-08: New service page /aardlekschakelaar-rotterdam/ (aardlek slaat door: aardlek vs groep, stappenplan, oorzaken, testknop, aardlekautomaat, FAQ). Linked from /storing-elektra-rotterdam/; added to hub tiles, footer and sitemap. Added `.steps-list` style to assets/seo.css and bumped ASSET_V. Started this log.
- 2026-11-08 (2): Conversion: pre-filled WhatsApp message per landing page (photo of the meterkast asked where useful), photo hint under the hero buttons, sticky Bellen/WhatsApp bar on phones (landing pages), and new assets/track.js that sends a GA4 `contact_click` event (method, cta, page) for WhatsApp/phone/e-mail clicks on all pages. Landing pages had no Google tag before; track.js now loads the same tag as the homepage.
- 2026-11-08 (3): New page /elektricien-verhuurders-vve-rotterdam/ for landlords, property managers and VvE's (services, how we work together, who pays what per the Besluit kleine herstellingen, FAQ). Linked from the keuring page; in hub tiles, footer and sitemap.
- 2026-11-08 (4): Messaging first (owner prefers WhatsApp over calls): landing-page hero 'Bel' button replaced by 'Offerte aanvragen', phone button removed from the side card, mobile bar is now one WhatsApp button, copy changed from 'bel' to 'app/bericht'. Phone number stays in footer and structured data. Future pages and posts: lead with WhatsApp, not calling.
- 2026-11-08 (5): Speed and technical SEO after an external audit (homepage 77/100, LCP 5.4 s lab): WebP copies of all photos used in <img> tags (about 45% smaller; JPGs kept for og:image and lightbox), hero preload in WebP, Google Fonts loaded without blocking render (homepage and landing pages), homepage meta description shortened to 151 chars, full street address in JSON-LD, new generated /llms.txt.
- 2026-11-09: New service page /inductiekookplaat-aansluiten-rotterdam/ (1-fase vs perilex 2-fase vs krachtstroom with wattages, how to recognise a kookgroep, when verzwaren is (not) needed incl. netcongestie and the 1 July 2026 rule change, gas-to-inductie checklist (gas disconnection by a gas installer, pans, separate oven group), steps, FAQ). Linked from /groepenkast-vervangen-rotterdam/ and from the service list on all town pages; in hub tiles, footer, sitemap and llms.txt.
- 2026-11-09 (2): Full site audit at the owner's request (static + rendered at 390 and 1280 px; no broken links, JSON-LD valid, layout clean). Fixed: page titles and meta descriptions that were too long are now within about 65 / 160 characters on all 18 landing pages (new `_city_title()` helper, shorter town description). Stopped early at the owner's request; not done and still open: homepage link lists and footer miss /aardlekschakelaar-rotterdam/, /inductiekookplaat-aansluiten-rotterdam/ and /elektricien-verhuurders-vve-rotterdam/; homepage WhatsApp links have no pre-filled text or data-cta; thin pages (lampen, stopcontact, bedrading, keuring, laadpaal) could use 2-3 more FAQs; 'Gratis telefonisch advies' on the homepage is not on the approved claims list; Barendrecht FAQ promises laadpaal + thuisbatterij together while the team has no thuisbatterij experience yet.
- 2026-11-10: New service page /meterkast-verzwaren-rotterdam/ (how to read your connection, kW per 1x25A/1x35A/3x25A, what fits on 1-fase per appliance from the RVO overview of Sept 2026, when 3-fase makes sense, netcongestie and the 1 July 2026 single queue, who does what: netbeheerder vs. installer, steps, 8 FAQs). Linked from the groepenkast, inductie and laadpaal pages; in hub tiles, footer, sitemap and llms.txt. Accuracy fix on /inductiekookplaat-aansluiten-rotterdam/: removed 'ruim twee derde heeft 3x25A' (RVO: about 71% of Stedin connections are still 1-fase) and reworded the 1 July 2026 note to the single-queue rule.

## Backlog

Highest value first.

1. Service pages people search for:
   - groep bijplaatsen
   - buitenverlichting en tuinstopcontact
   - elektra keuring bij aankoop of verhuur
2. Town pages: Krimpen aan den IJssel, Albrandswaard (Rhoon, Poortugaal), Spijkenisse, Lansingerland (Berkel en Rodenrijs), Hoogvliet.
3. Knowledge articles (only if useful and accurate): "Salderen stopt 2027: wat betekent dat voor uw meterkast?".
   (The planned "Aardlek slaat steeds door" article is covered by /aardlekschakelaar-rotterdam/.)
4. Conversion follow-ups: homepage pre-filled WhatsApp text per language, data-cta labels on homepage links.
5. Accuracy: Barendrecht town page says we often do thuisbatterijen and promises laadpaal + thuisbatterij together; the team has no thuisbatterij experience yet. Reword once confirmed (or now, to 'laadpaal en extra groepen').
6. Technical SEO: privacy page (privacybeleid) for the contact form and Google Analytics; internal links from homepage views to landing pages; re-measure LCP after the WebP/font change; homepage has 5 H1s (one per view; site.js focuses the view's h1, so change carefully).
7. Wording check: site-wide "gecertificeerd" wording (homepage i18n, page template sidebar, several landing pages) is not on the approved claims list. Waiting for the owner's confirmation before changing or keeping it.
