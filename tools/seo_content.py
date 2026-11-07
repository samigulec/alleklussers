# -*- coding: utf-8 -*-
"""Content for the SEO landing pages. Edit the text here, then run:

    python3 tools/seo_pages.py

Each page is Dutch only (that is what people search in Rotterdam).
Keep claims in line with the homepage: work to NEN 1010, insured,
24/7 reachable, reply within 24 hours, clear price up front.
"""

AREAS_ROTTERDAM = [
    "Rotterdam Centrum", "Rotterdam-Zuid", "Feijenoord", "Charlois", "IJsselmonde",
    "Kralingen-Crooswijk", "Rotterdam-Noord", "Hillegersberg-Schiebroek", "Prins Alexander",
    "Delfshaven", "Overschie", "Hoogvliet",
]
AREAS_REGION = [
    "Schiedam", "Vlaardingen", "Capelle aan den IJssel", "Barendrecht", "Ridderkerk",
    "Krimpen aan den IJssel", "Albrandswaard",
]

# Order here = order of tiles on the hub page and in the footer.
PAGES = [
    # ------------------------------------------------------------------ HUB
    {
        "slug": "elektricien-rotterdam",
        "short": "Elektricien Rotterdam",
        "title": "Elektricien Rotterdam | AlleKlussers, 24/7 bereikbaar",
        "desc": "Elektricien nodig in Rotterdam? AlleKlussers helpt bij storingen, groepenkasten, verlichting, stopcontacten en laadpalen. Gecertificeerd, verzekerd en binnen 24 uur reactie.",
        "service": "Elektricien",
        "char": "stekkie",
        "say": "“Elektra in Rotterdam? Wij zitten om de hoek.”",
        "eyebrow": "Elektricien in Rotterdam",
        "h1": "Uw elektricien in <em>Rotterdam.</em>",
        "lede": "Van een storing tot een complete installatie. Gecertificeerde elektriciens uit Rotterdam-Zuid, snel bij u in de stad en de regio.",
        "hub": True,
        "body": """
<h2>Elektra geregeld, <em>zonder gedoe.</em></h2>
<p>AlleKlussers is een elektrotechnisch bedrijf uit Rotterdam. Wij helpen particulieren, verhuurders en bedrijven met alles wat met elektra te maken heeft: van een lamp ophangen of een extra stopcontact tot een nieuwe groepenkast, een laadpaal of het verhelpen van een storing.</p>
<p>U krijgt binnen 24 uur reactie met een duidelijke prijs vooraf. Onze elektriciens zijn gecertificeerd, verzekerd en werken volgens NEN 1010, de norm voor veilige elektrische installaties in Nederland.</p>

<h2>Waar kunnen wij <em>mee helpen?</em></h2>
{tiles}

<h2>Waarom kiezen voor <em>AlleKlussers?</em></h2>
<ul class="checks">
  <li>{check}<span><strong>Duidelijke prijs vooraf.</strong> U weet waar u aan toe bent voordat we beginnen. Geen verrassingen achteraf.</span></li>
  <li>{check}<span><strong>Snel geregeld.</strong> Binnen 24 uur reactie, en bij storingen 24/7 bereikbaar.</span></li>
  <li>{check}<span><strong>Veilig en volgens de norm.</strong> Gecertificeerde, verzekerde vakmensen die werken volgens NEN 1010.</span></li>
  <li>{check}<span><strong>Netjes opgeleverd.</strong> We lopen alles samen met u na en laten de ruimte schoon achter.</span></li>
</ul>

<h2>Werkgebied</h2>
<p>We werken in heel Rotterdam en in de gemeenten eromheen. Twijfelt u of we bij u in de buurt komen? Stuur ons gerust een berichtje.</p>
{areas}
""",
        "faq": [
            ("Wat kost een elektricien in Rotterdam?",
             "Dat hangt af van de klus. Voor kleine klussen zoals lampen ophangen of een stopcontact plaatsen spreken we vaak een vaste prijs af. Voor grotere klussen krijgt u eerst een offerte. U weet dus altijd vooraf wat het kost."),
            ("Hoe snel kunnen jullie komen?",
             "U krijgt binnen 24 uur reactie op uw aanvraag. Bij een storing zijn we 24/7 bereikbaar en plannen we zo snel mogelijk een afspraak in."),
            ("Zijn jullie gecertificeerd en verzekerd?",
             "Ja. Onze elektriciens zijn gecertificeerd, verzekerd en werken volgens NEN 1010."),
            ("Werken jullie ook voor verhuurders en bedrijven?",
             "Ja. Naast particulieren helpen we ook verhuurders, vastgoedbeheerders en bedrijven, voor losse klussen en voor terugkerend onderhoud."),
        ],
    },
    # ------------------------------------------------------------- STORING
    {
        "slug": "storing-elektra-rotterdam",
        "short": "Storing verhelpen",
        "sub": "Stroomuitval en een aardlekschakelaar die steeds doorslaat.",
        "title": "Storing elektra Rotterdam | Stroomuitval? AlleKlussers helpt",
        "desc": "Stroomuitval of slaat uw aardlekschakelaar steeds door in Rotterdam? AlleKlussers spoort de oorzaak op en lost de storing veilig op. 24/7 bereikbaar.",
        "service": "Storing elektra verhelpen",
        "char": "vonk",
        "say": "“Stroom uit? Wij zijn 24/7 bereikbaar.”",
        "eyebrow": "Storingen en spoed",
        "h1": "Storing of stroomuitval in <em>Rotterdam?</em>",
        "lede": "Valt de stroom uit of slaat de aardlekschakelaar steeds door? Wij zoeken de oorzaak en lossen het veilig op.",
        "body": """
<h2>Eerst dit: <em>zelf controleren.</em></h2>
<p>Sommige storingen kunt u zelf veilig nagaan voordat u belt:</p>
<ul class="checks">
  <li>{check}<span><strong>Heeft de buurt ook geen stroom?</strong> Dan ligt de storing waarschijnlijk bij de netbeheerder. In Rotterdam is dat Stedin.</span></li>
  <li>{check}<span><strong>Kijk in de meterkast.</strong> Staat er een groep of aardlekschakelaar omlaag? Haal dan eerst de stekkers van apparaten op die groep uit het stopcontact en zet de schakelaar weer omhoog.</span></li>
  <li>{check}<span><strong>Slaat hij direct weer door?</strong> Probeer het niet steeds opnieuw. Er is dan een fout in de installatie of in een apparaat, en die moet worden opgespoord.</span></li>
</ul>
<div class="note-box"><p><strong>Ruikt u een brandlucht, ziet u rook of zijn er vonken?</strong> Zet de hoofdschakelaar in de meterkast uit als dat veilig kan en bel bij gevaar direct 112.</p></div>

<h2>Veelvoorkomende <em>oorzaken.</em></h2>
<ul class="checks">
  <li>{check}<span><strong>Een defect apparaat,</strong> bijvoorbeeld een wasmachine, oven of waterkoker met lekstroom.</span></li>
  <li>{check}<span><strong>Vocht,</strong> vaak bij buitenverlichting, buitenstopcontacten of in de badkamer.</span></li>
  <li>{check}<span><strong>Een overbelaste groep,</strong> doordat te veel zware apparaten op dezelfde groep zitten.</span></li>
  <li>{check}<span><strong>Verouderde bedrading of een oude groepenkast</strong> die niet meer goed beveiligt.</span></li>
</ul>

<h2>Wat wij <em>doen.</em></h2>
<p>Onze elektricien meet de installatie door en zoekt groep voor groep uit waar de fout zit. Daarna lossen we het op, of bespreken we eerst met u wat er nodig is als de reparatie groter is. U krijgt uitleg over de oorzaak en advies om herhaling te voorkomen.</p>
""",
        "faq": [
            ("Mijn aardlekschakelaar slaat steeds door. Wat nu?",
             "Haal alle stekkers op die groep eruit en zet de aardlekschakelaar weer omhoog. Blijft hij staan, steek de apparaten dan één voor één terug om te zien welk apparaat de storing geeft. Slaat hij ook zonder apparaten door, dan zit de fout in de installatie en is een elektricien nodig."),
            ("De hele straat heeft geen stroom. Moet ik jullie bellen?",
             "Nee, dan is het een storing in het net. Die meldt u bij de netbeheerder; in Rotterdam is dat Stedin."),
            ("Zijn jullie ook 's avonds en in het weekend bereikbaar?",
             "Ja, we zijn 24/7 bereikbaar. Bel of app ons, dan kijken we hoe snel we bij u kunnen zijn."),
            ("Wat kost het verhelpen van een storing?",
             "Dat hangt af van de oorzaak. We bespreken de kosten met u voordat we aan de reparatie beginnen."),
        ],
    },
    # ---------------------------------------------------------- GROEPENKAST
    {
        "slug": "groepenkast-vervangen-rotterdam",
        "short": "Groepenkast vervangen",
        "sub": "Vervangen of uitbreiden voor inductie, laadpaal of warmtepomp.",
        "title": "Groepenkast vervangen Rotterdam | AlleKlussers",
        "desc": "Groepenkast vervangen of uitbreiden in Rotterdam? Voor inductie, laadpaal, warmtepomp of meer veiligheid. Werk volgens NEN 1010, prijs vooraf.",
        "service": "Groepenkast vervangen en uitbreiden",
        "char": "kastje",
        "say": "“Meer groepen nodig? Ik regel het.”",
        "eyebrow": "Groepenkasten",
        "h1": "Groepenkast vervangen in <em>Rotterdam.</em>",
        "lede": "Een veilige, moderne groepenkast met genoeg groepen voor inductie, een laadpaal, een warmtepomp of extra apparaten.",
        "body": """
<h2>Wanneer is vervangen <em>verstandig?</em></h2>
<ul class="checks">
  <li>{check}<span><strong>U heeft nog een oude kast</strong> met draaistoppen of smeltzekeringen.</span></li>
  <li>{check}<span><strong>Er zit geen of maar één aardlekschakelaar in.</strong> Een moderne kast beveiligt beter tegen lekstroom.</span></li>
  <li>{check}<span><strong>Groepen slaan vaak door,</strong> omdat er te veel apparaten op dezelfde groep zitten.</span></li>
  <li>{check}<span><strong>U neemt iets zwaars in gebruik,</strong> zoals een inductiekookplaat, laadpaal, warmtepomp, zonnepanelen of een <a href="/thuisbatterij-aansluiten-rotterdam/">thuisbatterij</a>.</span></li>
  <li>{check}<span><strong>U gaat verbouwen</strong> en er komen nieuwe aansluitingen bij.</span></li>
</ul>

<h2>Wat wij <em>doen.</em></h2>
<p>We bekijken eerst uw huidige meterkast en bespreken wat u nodig heeft, nu en in de toekomst. Daarna vervangen of breiden we de groepenkast uit met de juiste aardlekbeveiliging, verdelen we de groepen logisch en zetten we op elke groep duidelijk waar hij voor is. Tot slot testen we alles en leggen we uit hoe uw nieuwe kast werkt.</p>
<p>Alles volgens NEN 1010, door gecertificeerde en verzekerde elektriciens.</p>

<div class="note-box"><p><strong>Zware aansluiting nodig?</strong> Voor bijvoorbeeld een laadpaal of warmtepomp kan uw aansluiting te licht zijn. Een verzwaring vraagt u aan bij de netbeheerder (Stedin). Wij vertellen u eerlijk of dat nodig is.</p></div>
""",
        "faq": [
            ("Hoe lang duurt het vervangen van een groepenkast?",
             "Meestal is het in één dag klaar. Tijdens het werk is de stroom een aantal uur uit; dat stemmen we vooraf met u af."),
            ("Heb ik een aparte groep nodig voor een inductiekookplaat?",
             "Ja, een inductiekookplaat heeft meestal een eigen, zwaardere aansluiting nodig. We kijken of uw meterkast dat aankan en passen hem zo nodig aan."),
            ("Wat is het verschil tussen 1-fase en 3-fase?",
             "Een 3-fase aansluiting kan meer vermogen leveren en is handig bij zware verbruikers zoals een laadpaal of warmtepomp. We kijken samen wat u heeft en wat u nodig heeft."),
            ("Wat kost een nieuwe groepenkast?",
             "Dat hangt af van het aantal groepen en wat er verder moet gebeuren. U krijgt eerst een offerte met een vaste prijs."),
        ],
    },
    # -------------------------------------------------------- THUISBATTERIJ
    {
        "slug": "thuisbatterij-aansluiten-rotterdam",
        "short": "Thuisbatterij aansluiten",
        "sub": "Eigen groep en meterkast klaar voor 2027.",
        "title": "Thuisbatterij aansluiten Rotterdam | Klaar voor 2027 | AlleKlussers",
        "desc": "Thuisbatterij laten aansluiten in Rotterdam? Salderen stopt op 1 januari 2027. Wij controleren uw meterkast, leggen een eigen groep aan en sluiten de batterij veilig aan.",
        "service": "Thuisbatterij aansluiten",
        "char": "laadie",
        "say": "“Zonnestroom bewaren? Ik sluit hem aan.”",
        "eyebrow": "Thuisbatterij en meterkast",
        "h1": "Thuisbatterij aansluiten in <em>Rotterdam.</em>",
        "lede": "Op 1 januari 2027 stopt de salderingsregeling. Met een thuisbatterij gebruikt u meer van uw eigen zonnestroom. Wij zorgen dat uw meterkast er klaar voor is en sluiten de batterij veilig aan.",
        "body": """
<h2>Waarom nu <em>een thuisbatterij?</em></h2>
<p>Tot en met 31 december 2026 mag u de stroom die uw zonnepanelen terugleveren nog wegstrepen tegen de stroom die u van het net gebruikt. Vanaf 1 januari 2027 kan dat niet meer. U krijgt dan alleen een terugleververgoeding, en die is meestal lager dan wat u voor stroom betaalt. Zonnestroom die u zelf gebruikt, wordt dus meer waard.</p>
<p>Een thuisbatterij slaat overdag uw zonnestroom op, zodat u die 's avonds zelf kunt gebruiken. Of dat voor u loont, hangt af van uw zonnepanelen en uw verbruik. Reken het daarom eerst goed door, eventueel met uw leverancier.</p>

<h2>Stekkerbatterij of <em>vaste batterij?</em></h2>
<ul class="checks">
  <li>{check}<span><strong>Stekkerbatterij:</strong> steekt u zelf in een stopcontact. Er is geen installateur nodig, maar de capaciteit is beperkt. Wij kunnen controleren of de groep waarop hij komt dat aankan.</span></li>
  <li>{check}<span><strong>Vaste thuisbatterij:</strong> meer capaciteit, maar die moet vakkundig worden aangesloten op een eigen groep in de meterkast. Daar komen wij in beeld.</span></li>
</ul>

<h2>Wat wij <em>doen.</em></h2>
<ul class="checks">
  <li>{check}<span><strong>Meterkast controleren:</strong> heeft uw groepenkast ruimte voor een extra groep, en is uw aansluiting zwaar genoeg?</span></li>
  <li>{check}<span><strong>Groepenkast aanpassen of uitbreiden</strong> als dat nodig is, met de juiste aardlekbeveiliging.</span></li>
  <li>{check}<span><strong>Eigen groep en bekabeling</strong> van de meterkast naar de plek van de batterij.</span></li>
  <li>{check}<span><strong>Aansluiten en testen,</strong> in overleg met de leverancier van uw batterij of omvormer.</span></li>
</ul>

<div class="note-box"><p><strong>Druk richting 2027.</strong> Veel mensen willen hun batterij vóór 1 januari 2027 regelen. Plan daarom op tijd, dan voorkomt u wachttijden.</p></div>

<p>Moet uw groepenkast eerst worden vervangen of uitgebreid? Lees meer over <a href="/groepenkast-vervangen-rotterdam/">groepenkast vervangen in Rotterdam</a>.</p>
""",
        "faq": [
            ("Heb ik na 2027 een thuisbatterij nodig?",
             "Niet per se. Het hangt af van hoeveel zonnestroom u teruglevert en wanneer u stroom gebruikt. Wie veel teruglevert en 's avonds veel verbruikt, heeft er meer aan. Laat het goed doorrekenen voordat u koopt."),
            ("Mag ik een stekkerbatterij zelf aansluiten?",
             "Ja, een stekkerbatterij steekt u zelf in het stopcontact. Let wel op dat de groep niet overbelast raakt. Twijfelt u, dan controleren wij uw groep."),
            ("Is mijn meterkast geschikt voor een vaste thuisbatterij?",
             "Dat controleren we eerst. Vaak is een extra groep genoeg; soms moet de groepenkast worden uitgebreid of vervangen. Dat hoort u vooraf van ons, met een prijs."),
            ("Moet ik een thuisbatterij ergens aanmelden?",
             "Een vaste thuisbatterij die op het net is aangesloten, meldt u aan via energieleveren.nl, net als zonnepanelen. Wij helpen u daarbij."),
            ("Leveren jullie ook de batterij zelf?",
             "Wij richten ons op de elektrische aansluiting en de meterkast. Heeft u nog geen batterij, dan denken we graag mee over wat bij uw installatie past."),
        ],
    },
    # ------------------------------------------------------------ VERLICHTING
    {
        "slug": "lampen-ophangen-rotterdam",
        "short": "Lampen ophangen",
        "sub": "Plafondlampen, spots, dimmers en buitenverlichting.",
        "title": "Lampen ophangen Rotterdam | Verlichting installeren | AlleKlussers",
        "desc": "Lampen laten ophangen of verlichting installeren in Rotterdam? Plafondlampen, hanglampen, spots, dimmers en buitenverlichting, netjes en veilig aangesloten.",
        "service": "Lampen ophangen en verlichting installeren",
        "char": "lampje",
        "say": "“Meer licht? Daar ben ik voor.”",
        "eyebrow": "Verlichting",
        "h1": "Lampen ophangen in <em>Rotterdam.</em>",
        "lede": "Plafondlampen, hanglampen, wandlampen, spots en dimmers: netjes gemonteerd en veilig aangesloten.",
        "body": """
<h2>Wat wij <em>voor u doen.</em></h2>
<ul class="checks">
  <li>{check}<span><strong>Lampen ophangen</strong> op bestaande aansluitpunten: plafondlampen, hanglampen en wandlampen.</span></li>
  <li>{check}<span><strong>Nieuwe lichtpunten maken,</strong> bijvoorbeeld boven de eettafel of het keukeneiland.</span></li>
  <li>{check}<span><strong>Inbouwspots plaatsen</strong> in plafonds, keukens en badkamers.</span></li>
  <li>{check}<span><strong>Dimmers en schakelaars</strong> die geschikt zijn voor LED, zonder geknipper of gezoem.</span></li>
  <li>{check}<span><strong>Buitenverlichting</strong> aan de gevel, in de tuin of bij de voordeur, waterdicht aangesloten.</span></li>
  <li>{check}<span><strong>Badkamerverlichting en LED-spiegels,</strong> veilig in een natte ruimte.</span></li>
</ul>

<div class="note-box"><p><strong>Tip:</strong> heeft u meerdere lampen? Laat ze in één afspraak ophangen. Dat scheelt tijd en is per lamp voordeliger.</p></div>

<h2>Zo <em>werkt het.</em></h2>
<p>Stuur ons een berichtje met het aantal lampen en, als dat kan, een foto van de plek. U krijgt binnen 24 uur een prijs. Onze elektricien neemt het kleine materiaal mee, zoals schroeven, pluggen en lasklemmen, hangt alles op en test of het werkt.</p>
""",
        "faq": [
            ("Kunnen jullie ook zware lampen of kroonluchters ophangen?",
             "Ja. We kijken eerst of het plafond het gewicht kan dragen en gebruiken de juiste bevestiging."),
            ("Mijn LED-lamp knippert met de dimmer. Kunnen jullie dat oplossen?",
             "Meestal is de dimmer niet geschikt voor LED. We vervangen hem door een LED-dimmer die bij uw lampen past."),
            ("Moet ik de lampen zelf kopen?",
             "Meestal wel, dan kiest u precies wat u mooi vindt. Klein materiaal zoals schroeven, pluggen en lasklemmen nemen wij mee."),
            ("Kunnen jullie een nieuw lichtpunt maken waar nog geen aansluiting zit?",
             "Ja, dan trekken we een nieuwe kabel naar de gewenste plek. De prijs hangt af van de route; dat bespreken we vooraf."),
        ],
    },
    # ---------------------------------------------------------- STOPCONTACT
    {
        "slug": "stopcontact-plaatsen-rotterdam",
        "short": "Stopcontact plaatsen",
        "sub": "Extra of verplaatste stopcontacten en schakelaars.",
        "title": "Stopcontact plaatsen of verplaatsen Rotterdam | AlleKlussers",
        "desc": "Extra stopcontact laten plaatsen of verplaatsen in Rotterdam? Binnen en buiten, ook voor wasmachine, droger en kookplaat. Veilig aangesloten, prijs vooraf.",
        "service": "Stopcontacten en schakelaars plaatsen",
        "char": "dosie",
        "say": "“Te weinig stopcontacten? Niet meer.”",
        "eyebrow": "Stopcontacten en schakelaars",
        "h1": "Stopcontact plaatsen in <em>Rotterdam.</em>",
        "lede": "Extra stopcontacten, schakelaars en aansluitpunten, binnen en buiten, veilig aangesloten.",
        "body": """
<h2>Wat wij <em>voor u doen.</em></h2>
<ul class="checks">
  <li>{check}<span><strong>Extra stopcontacten</strong> waar u ze nodig heeft, of een enkel stopcontact dubbel maken.</span></li>
  <li>{check}<span><strong>Stopcontacten en schakelaars verplaatsen,</strong> bijvoorbeeld na een verbouwing.</span></li>
  <li>{check}<span><strong>Buitenstopcontacten</strong> voor tuin, balkon of terras, spatwaterdicht.</span></li>
  <li>{check}<span><strong>Aansluitingen voor zware apparaten</strong> zoals wasmachine, droger, vaatwasser en kookplaat, op een eigen groep.</span></li>
  <li>{check}<span><strong>Stopcontacten met USB</strong> voor bij het bed of op het bureau.</span></li>
</ul>

<div class="note-box"><p><strong>Veel stekkerdozen achter elkaar?</strong> Dat kan een groep overbelasten en is een bekende oorzaak van brand. Een paar extra stopcontacten zijn veiliger en netter.</p></div>

<h2>Inbouw of <em>opbouw?</em></h2>
<p>Bij inbouw zit het stopcontact in de muur en ziet u de kabel niet. Bij opbouw komt de kabel in een nette goot op de muur; dat is sneller en vaak voordeliger. We bespreken samen wat het beste past bij uw muur en uw budget.</p>
""",
        "faq": [
            ("Kan er overal een stopcontact bij?",
             "Bijna altijd. We kijken waar de dichtstbijzijnde aansluiting zit en welke route de kabel kan nemen."),
            ("Heeft mijn wasmachine een eigen groep nodig?",
             "Voor zware apparaten zoals een wasmachine, droger of vaatwasser is een eigen groep aan te raden. Zo raakt de groep niet overbelast."),
            ("Kunnen jullie een buitenstopcontact plaatsen?",
             "Ja, met een spatwaterdicht stopcontact en de juiste beveiliging in de meterkast."),
            ("Wat kost een extra stopcontact?",
             "Dat hangt af van de afstand tot de dichtstbijzijnde aansluiting en of het inbouw of opbouw wordt. U krijgt vooraf een prijs."),
        ],
    },
    # ------------------------------------------------------------ BEDRADING
    {
        "slug": "bedrading-vervangen-rotterdam",
        "short": "Bedrading en aansluitingen",
        "sub": "Oude bedrading vervangen, aansluitingen voor de keuken.",
        "title": "Bedrading vervangen Rotterdam | Elektra aansluitingen | AlleKlussers",
        "desc": "Oude bedrading vervangen of nieuwe aansluitingen nodig in Rotterdam? Voor keuken, wasmachine en apparatuur. Gecertificeerd, verzekerd en prijs vooraf.",
        "service": "Bedrading vervangen en aansluitingen maken",
        "char": "stekkie",
        "say": "“Oude draden? Ik maak het weer veilig.”",
        "eyebrow": "Bedrading en aansluitingen",
        "h1": "Bedrading vervangen in <em>Rotterdam.</em>",
        "lede": "Nieuwe leidingen en aansluitingen voor keuken, wasmachine en apparatuur, en vervanging van verouderde bedrading.",
        "body": """
<h2>Tekenen van <em>oude bedrading.</em></h2>
<p>In veel Rotterdamse woningen zit nog bedrading van tientallen jaren oud. Let op deze signalen:</p>
<ul class="checks">
  <li>{check}<span><strong>Stopcontacten zonder randaarde,</strong> waar een moderne stekker niet goed in past.</span></li>
  <li>{check}<span><strong>Verkleurde of warme stopcontacten en schakelaars.</strong></span></li>
  <li>{check}<span><strong>Draden met een stoffen omhulsel</strong> of een broos, gebarsten omhulsel.</span></li>
  <li>{check}<span><strong>Groepen die vaak doorslaan</strong> of een brandlucht bij een stopcontact.</span></li>
</ul>

<h2>Wat wij <em>doen.</em></h2>
<p>We controleren eerst de installatie en vertellen u eerlijk wat echt vervangen moet worden en wat nog goed is. Waar mogelijk trekken we nieuwe draden door de bestaande buizen; als er gefreesd moet worden, werken we dat netjes af.</p>
<p>Gaat u een keuken plaatsen of verbouwen? Dan leggen we de aansluitingen aan voor oven, kookplaat, vaatwasser, koelkast en afzuigkap, ieder op de juiste groep.</p>
""",
        "faq": [
            ("Moet in een oud huis alle bedrading vervangen worden?",
             "Niet altijd. Na een controle weet u precies wat nodig is. Soms is vervangen van een deel genoeg."),
            ("Moeten de muren open?",
             "Vaak kunnen we via de bestaande buizen nieuwe draden trekken. Als frezen nodig is, bespreken we dat vooraf en werken we het netjes af."),
            ("Kunnen jullie de elektra voor mijn nieuwe keuken aanleggen?",
             "Ja. Stuur ons de keukentekening, dan zorgen we dat alle apparaten de juiste aansluiting en groep krijgen."),
        ],
    },
    # -------------------------------------------------------------- KEURING
    {
        "slug": "elektra-keuring-rotterdam",
        "short": "Elektra keuring",
        "sub": "Controle bij aankoop, verhuur of na een verbouwing.",
        "title": "Elektra keuring Rotterdam | Elektrische installatie laten keuren | AlleKlussers",
        "desc": "Elektrische installatie laten keuren in Rotterdam? Bij aankoop, verhuur of na een verbouwing. U krijgt een helder overzicht en advies. AlleKlussers, gecertificeerd.",
        "service": "Keuring van elektrische installaties",
        "char": "schildje",
        "say": "“Veilig of niet? Ik zoek het uit.”",
        "eyebrow": "Keuring en veiligheid",
        "h1": "Elektra keuring in <em>Rotterdam.</em>",
        "lede": "Een controle van uw elektrische installatie, met een helder overzicht van wat in orde is en wat niet.",
        "body": """
<h2>Wanneer is een keuring <em>verstandig?</em></h2>
<ul class="checks">
  <li>{check}<span><strong>Bij aankoop van een woning,</strong> zodat u weet of er kosten aankomen.</span></li>
  <li>{check}<span><strong>Bij verhuur,</strong> voor de veiligheid van uw huurders en uw eigen gemoedsrust.</span></li>
  <li>{check}<span><strong>Na een verbouwing</strong> of als er door anderen aan de elektra is gewerkt.</span></li>
  <li>{check}<span><strong>In een ouder huis,</strong> of als groepen vaak doorslaan.</span></li>
</ul>

<h2>Wat wij <em>controleren.</em></h2>
<p>We kijken naar de groepenkast en de aardlekbeveiliging, de aarding, de staat van de bedrading, stopcontacten en schakelaars, en of groepen niet overbelast zijn. Waar nodig doen we metingen.</p>
<p>Na afloop krijgt u een overzicht van de bevindingen en een advies. Moet er iets verbeterd worden, dan krijgt u daar een offerte voor. U beslist zelf of en wanneer u dat laat doen.</p>
""",
        "faq": [
            ("Hoe lang duurt een keuring?",
             "Dat hangt af van de grootte van de woning of het pand. Voor een gewone woning is het meestal binnen een paar uur klaar."),
            ("Krijg ik een verslag?",
             "Ja, u krijgt een overzicht van wat we hebben gecontroleerd, wat we hebben gevonden en wat we adviseren."),
            ("Doen jullie ook keuringen voor verhuurders?",
             "Ja. We keuren ook huurwoningen en kunnen gevonden punten direct voor u oplossen."),
        ],
    },
    # -------------------------------------------------------------- LAADPAAL
    {
        "slug": "laadpaal-installeren-rotterdam",
        "short": "Laadpaal installeren",
        "sub": "Een laadpaal bij huis, op een eigen groep.",
        "title": "Laadpaal installeren Rotterdam | Thuis laden | AlleKlussers",
        "desc": "Laadpaal laten installeren in Rotterdam? We controleren uw meterkast, leggen een eigen groep aan en sluiten de laadpaal veilig aan. Prijs vooraf, gecertificeerd.",
        "service": "Laadpaal installeren",
        "char": "laadie",
        "say": "“Thuis laden? Ik sluit hem aan.”",
        "eyebrow": "Laadpalen en slimme elektra",
        "h1": "Laadpaal installeren in <em>Rotterdam.</em>",
        "lede": "Een laadpaal bij uw woning of bedrijf, veilig aangesloten op een eigen groep in de meterkast.",
        "body": """
<h2>Wat wij <em>voor u doen.</em></h2>
<ul class="checks">
  <li>{check}<span><strong>Meterkast controleren:</strong> we kijken of uw aansluiting genoeg vermogen heeft, 1-fase of 3-fase.</span></li>
  <li>{check}<span><strong>Eigen groep aanleggen</strong> met de juiste aardlekbeveiliging voor een laadpaal.</span></li>
  <li>{check}<span><strong>Kabel trekken</strong> van de meterkast naar de plek van de laadpaal, binnen of buiten.</span></li>
  <li>{check}<span><strong>Monteren, aansluiten en testen,</strong> en uitleg over het gebruik.</span></li>
</ul>

<div class="note-box"><p><strong>Geen eigen oprit?</strong> Een laadkabel over de stoep is in Rotterdam meestal niet toegestaan. U kunt bij de gemeente een openbare laadpaal in de buurt aanvragen.</p></div>

<h2>Slim laden <em>en slimme elektra.</em></h2>
<p>Met een slimme laadpaal kunt u laden wanneer stroom goedkoop is of als uw zonnepanelen leveren. Met loadbalancing verdeelt de laadpaal het vermogen, zodat uw hoofdzekering niet doorslaat als ook de oven en de wasmachine aan staan. We helpen ook met andere slimme schakelingen voor licht en apparaten.</p>
""",
        "faq": [
            ("Is mijn meterkast geschikt voor een laadpaal?",
             "Dat controleren we eerst. Vaak is een extra groep genoeg; soms is een zwaardere aansluiting bij Stedin nodig. Dat hoort u vooraf van ons."),
            ("Welke laadpaal moet ik kiezen?",
             "Dat hangt af van uw auto, uw aansluiting en of u slim wilt laden. We adviseren u graag."),
            ("Wat is loadbalancing?",
             "Loadbalancing zorgt dat de laadpaal minder vermogen gebruikt als andere apparaten veel stroom vragen. Zo slaat uw hoofdzekering niet door."),
        ],
    },
]


# ---------------------------------------------------------------- CITIES
# One page per nearby town ("elektricien Schiedam" etc.). Keep the local
# paragraph specific to the town so the pages are not near-duplicates.
def _city(slug, name, char, say, wijken_oud, wijken_nieuw, local, faq_extra):
    return {
        "slug": slug,
        "city": name,
        "short": f"Elektricien {name}",
        "title": f"Elektricien {name} | AlleKlussers, snel ter plaatse",
        "desc": f"Elektricien nodig in {name}? AlleKlussers helpt bij storingen, groepenkasten, verlichting, stopcontacten, laadpalen en thuisbatterijen. Binnen 24 uur reactie, prijs vooraf.",
        "service": f"Elektricien in {name}",
        "char": char,
        "say": say,
        "eyebrow": f"Elektricien in {name}",
        "h1": f"Uw elektricien in <em>{name}.</em>",
        "lede": f"Vanuit Rotterdam-Zuid zijn we snel in {name}. Voor storingen, groepenkasten, verlichting en alles wat met elektra te maken heeft.",
        "body": f"""
<h2>Elektra in {name}, <em>snel geregeld.</em></h2>
<p>AlleKlussers is een elektrotechnisch bedrijf uit Rotterdam-Zuid. {name} ligt vlakbij, dus we zijn er snel. U krijgt binnen 24 uur reactie met een duidelijke prijs vooraf, en bij storingen zijn we 24/7 bereikbaar.</p>
<p>{local}</p>
<p>In oudere wijken zoals {wijken_oud} komen we vaak verouderde groepenkasten en bedrading tegen. In nieuwere wijken zoals {wijken_nieuw} gaat het vaker om een laadpaal, een thuisbatterij of extra groepen voor inductie.</p>

<h2>Waarmee wij u <em>helpen in {name}.</em></h2>
<ul class="checks">
  <li>{{check}}<span><a href="/storing-elektra-rotterdam/">Storing verhelpen</a>: stroomuitval of een aardlekschakelaar die steeds doorslaat.</span></li>
  <li>{{check}}<span><a href="/groepenkast-vervangen-rotterdam/">Groepenkast vervangen of uitbreiden</a>, bijvoorbeeld voor inductie of een warmtepomp.</span></li>
  <li>{{check}}<span><a href="/thuisbatterij-aansluiten-rotterdam/">Thuisbatterij aansluiten</a> op een eigen groep, op tijd voor 2027.</span></li>
  <li>{{check}}<span><a href="/lampen-ophangen-rotterdam/">Lampen ophangen</a>, spots en dimmers.</span></li>
  <li>{{check}}<span><a href="/stopcontact-plaatsen-rotterdam/">Stopcontacten plaatsen</a> of verplaatsen, binnen en buiten.</span></li>
  <li>{{check}}<span><a href="/laadpaal-installeren-rotterdam/">Laadpaal installeren</a> bij uw woning of bedrijf.</span></li>
</ul>

<h2>Zo <em>werkt het.</em></h2>
<p>Stuur een berichtje via WhatsApp met wat er moet gebeuren, eventueel met een foto. U krijgt binnen 24 uur een prijs. We plannen een moment dat u uitkomt, voeren het werk uit en lopen alles samen met u na.</p>
""",
        "faq": [
            (f"Komen jullie ook in {name}?",
             f"Ja. We werken in heel {name} en de rest van de regio Rotterdam."),
            (f"Hoe snel kan een elektricien in {name} bij mij zijn?",
             "U krijgt binnen 24 uur reactie. Bij een storing zijn we 24/7 bereikbaar en plannen we zo snel mogelijk een afspraak in."),
            ("Wat kost het?",
             "Dat hangt af van de klus. U krijgt altijd eerst een prijs, zodat u vooraf weet waar u aan toe bent."),
        ] + faq_extra,
    }


CITY_PAGES = [
    _city("elektricien-schiedam", "Schiedam", "vonk", "“Schiedam? Daar zijn we zo.”",
          "de binnenstad, Schiedam-Oost en Nieuwland", "Kethel en Woudhoek",
          "Van de monumentale panden in de historische binnenstad tot de flats in Groenoord en de eengezinswoningen in Woudhoek: elke woning vraagt om een eigen aanpak. In oude panden kijken we extra goed naar de staat van de bedrading voordat we iets aanpassen.",
          [("Werken jullie ook in oude panden in de binnenstad?",
            "Ja. In oudere panden controleren we eerst de bestaande installatie en bespreken we met u wat nodig is voordat we beginnen.")]),
    _city("elektricien-vlaardingen", "Vlaardingen", "kastje", "“Vlaardingen? Ik ben onderweg.”",
          "Westwijk, Babberspolder en het centrum", "Holy en Ambacht",
          "In Vlaardingen werken we in alle wijken, van de portiekflats in de Westwijk en Babberspolder tot de woningen in Holy en Ambacht. Veel woningen hier zijn decennia oud; een controle van de groepenkast is dan vaak een goed begin.",
          [("Mijn groepenkast is oud. Moet hij vervangen worden?",
            "Niet altijd. We kijken eerst wat er zit en wat u nodig heeft. Pas als vervangen echt verstandig is, krijgt u daar een prijs voor.")]),
    _city("elektricien-capelle-aan-den-ijssel", "Capelle aan den IJssel", "dosie", "“Capelle? Gewoon even de brug over.”",
          "Middelwatering, Oostgaarde en Schollevaar", "Fascinatio",
          "Capelle aan den IJssel ligt direct naast Rotterdam. We werken in Middelwatering, Oostgaarde, Schollevaar, 's-Gravenland en Capelle-West, en ook in de nieuwbouw van Fascinatio. Voor bedrijven in de omgeving doen we ook onderhoud en storingen.",
          [("Werken jullie ook voor bedrijven in Capelle?",
            "Ja. Naast particulieren helpen we ook bedrijven, winkels en verhuurders met storingen, onderhoud en aanpassingen.")]),
    _city("elektricien-barendrecht", "Barendrecht", "laadie", "“Barendrecht? Laden maar.”",
          "het centrum en het oude dorp", "Carnisselande en Smitshoek",
          "Barendrecht ligt op een paar minuten van ons in Rotterdam-Zuid. In Carnisselande en Smitshoek wonen veel gezinnen met een auto voor de deur en zonnepanelen op het dak; daar helpen we vaak met laadpalen, thuisbatterijen en extra groepen.",
          [("Kunnen jullie een laadpaal en thuisbatterij tegelijk aansluiten?",
            "Ja. We kijken eerst of uw meterkast en aansluiting dat aankunnen en zorgen dat beide een eigen groep krijgen.")]),
    _city("elektricien-ridderkerk", "Ridderkerk", "lampje", "“Ridderkerk? Ik breng het licht.”",
          "Bolnes, Slikkerveer en het centrum", "Drievliet en Het Zand",
          "In Ridderkerk komen we in alle kernen: Bolnes, Slikkerveer, Rijsoord, Drievliet, Het Zand en het centrum. Ridderkerk ligt direct naast Rotterdam-Zuid, dus we zijn er snel bij een storing.",
          [("Rekenen jullie extra voor Ridderkerk?",
            "U krijgt vooraf één duidelijke prijs voor de klus, zodat u niet achteraf wordt verrast.")]),
]
