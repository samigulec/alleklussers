# -*- coding: utf-8 -*-
"""Content for the SEO landing pages. Edit the text here, then run:

    python3 tools/seo_pages.py

Each page is Dutch only (that is what people search in Rotterdam).
Keep claims in line with the homepage: certified (NEN 1010), insured,
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
        "desc": "Groepenkast vervangen of uitbreiden in Rotterdam? Voor inductie, laadpaal, warmtepomp of meer veiligheid. Gecertificeerd volgens NEN 1010, prijs vooraf.",
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
  <li>{check}<span><strong>U neemt iets zwaars in gebruik,</strong> zoals een inductiekookplaat, laadpaal, warmtepomp of zonnepanelen.</span></li>
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
