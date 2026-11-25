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

# Pre-filled WhatsApp message per page, so a visitor only has to add
# details (or a photo) and press send. City pages build theirs in _city().
FOTO = " Ik stuur een foto van mijn meterkast mee."
WA_TEXT = {
    "elektricien-rotterdam": "Hallo AlleKlussers, ik zoek een elektricien in Rotterdam. Het gaat om: ",
    "storing-elektra-rotterdam": "Hallo AlleKlussers, ik heb een storing in mijn elektra." + FOTO + " Wat er aan de hand is: ",
    "aardlekschakelaar-rotterdam": "Hallo AlleKlussers, mijn aardlekschakelaar slaat steeds door." + FOTO,
    "groepenkast-vervangen-rotterdam": "Hallo AlleKlussers, ik wil graag een prijs voor het vervangen of uitbreiden van mijn groepenkast." + FOTO,
    "groep-bijplaatsen-rotterdam": "Hallo AlleKlussers, ik wil graag een extra groep in mijn meterkast. Het is voor: ",
    "inductiekookplaat-aansluiten-rotterdam": "Hallo AlleKlussers, ik wil graag een inductiekookplaat laten aansluiten." + FOTO,
    "perilex-aansluiten-rotterdam": "Hallo AlleKlussers, ik wil graag een perilex laten aansluiten of verplaatsen." + FOTO + " Het gaat om: ",
    "thuisbatterij-aansluiten-rotterdam": "Hallo AlleKlussers, ik wil graag een thuisbatterij laten aansluiten." + FOTO,
    "vrije-groep-stekkerbatterij-rotterdam": "Hallo AlleKlussers, ik wil graag een vrije groep voor mijn stekkerbatterij." + FOTO,
    "lampen-ophangen-rotterdam": "Hallo AlleKlussers, ik wil graag lampen laten ophangen. Het gaat om: ",
    "elektra-badkamer-rotterdam": "Hallo AlleKlussers, ik ga mijn badkamer verbouwen en zoek een elektricien." + FOTO + " In de badkamer komt: ",
    "stopcontact-plaatsen-rotterdam": "Hallo AlleKlussers, ik wil graag stopcontacten laten plaatsen. Het gaat om: ",
    "buitenverlichting-tuinstopcontact-rotterdam": "Hallo AlleKlussers, ik wil graag buitenverlichting of een tuinstopcontact. Ik stuur een foto van de plek mee. Het gaat om: ",
    "bedrading-vervangen-rotterdam": "Hallo AlleKlussers, ik wil mijn bedrading laten controleren of vervangen. Het gaat om: ",
    "elektra-keuring-rotterdam": "Hallo AlleKlussers, ik wil mijn elektrische installatie laten keuren. Het is voor (aankoop, verkoop, verhuur of eigen woning): ",
    "laadpaal-installeren-rotterdam": "Hallo AlleKlussers, ik wil graag een laadpaal laten installeren." + FOTO,
    "meterkast-verzwaren-rotterdam": "Hallo AlleKlussers, ik wil weten of ik mijn aansluiting moet laten verzwaren. Ik wil gaan gebruiken: ",
    "infraroodpanelen-aansluiten-rotterdam": "Hallo AlleKlussers, ik wil graag een infraroodpaneel laten ophangen en aansluiten." + FOTO + " Het paneel is (watt) en komt in: ",
    "krachtstroom-aansluiten-rotterdam": "Hallo AlleKlussers, ik wil graag krachtstroom laten aanleggen. Het is voor dit apparaat en deze plek: ",
    "elektricien-verhuurders-vve-rotterdam": "Hallo AlleKlussers, ik ben verhuurder of beheerder en zoek een vaste elektricien. Het gaat om: ",
}

# Order here = order of tiles on the hub page and in the footer.
PAGES = [
    # ------------------------------------------------------------------ HUB
    {
        "slug": "elektricien-rotterdam",
        "short": "Elektricien Rotterdam",
        "title": "Elektricien Rotterdam | AlleKlussers, 24/7 bereikbaar",
        "desc": "Elektricien nodig in Rotterdam? Storing, groepenkast, inductie, lampen of laadpaal: app ons met een foto. Verzekerd, volgens NEN 1010, binnen 24 uur reactie.",
        "service": "Elektricien",
        "char": "stekkie",
        "say": "“Elektra in Rotterdam? Wij zitten om de hoek.”",
        "eyebrow": "Elektricien in Rotterdam",
        "h1": "Uw elektricien in <em>Rotterdam.</em>",
        "lede": "Van een storing tot een complete installatie. Verzekerde elektriciens uit Rotterdam-Zuid, snel bij u in de stad en de regio.",
        "hub": True,
        "body": """
<h2>Elektra geregeld, <em>zonder gedoe.</em></h2>
<p>AlleKlussers is een elektrotechnisch bedrijf uit Rotterdam. Wij helpen particulieren, verhuurders en bedrijven met alles wat met elektra te maken heeft: van een lamp ophangen of een extra stopcontact tot een nieuwe groepenkast, een laadpaal of het verhelpen van een storing.</p>
<p>U krijgt binnen 24 uur reactie met een duidelijke prijs vooraf. Onze elektriciens zijn verzekerd en werken volgens NEN 1010, de norm voor veilige elektrische installaties in Nederland.</p>
<p>We doen alleen elektra. Geen schilderwerk, vloeren of loodgieterswerk: daarvoor kunt u beter een specialist in dat vak zoeken.</p>

<h2>Wat speelt er <em>bij u?</em></h2>
<p>Kies de situatie die het meest op de uwe lijkt. Op elke pagina staat wat u zelf kunt nagaan, waar wij op letten en wat u ons het beste kunt sturen.</p>
<ul class="checks">
  <li>{check}<span><strong>Stroom uitgevallen of er slaat iets door.</strong> Begin bij <a href="/storing-elektra-rotterdam/">storing en stroomuitval</a>. Gaat steeds de schakelaar met de testknop omlaag, kijk dan bij <a href="/aardlekschakelaar-rotterdam/">aardlekschakelaar slaat door</a>.</span></li>
  <li>{check}<span><strong>Oude meterkast of te weinig groepen.</strong> Lees over <a href="/groepenkast-vervangen-rotterdam/">groepenkast vervangen of uitbreiden</a> en <a href="/groep-bijplaatsen-rotterdam/">een groep bijplaatsen</a>.</span></li>
  <li>{check}<span><strong>Nieuwe keuken of van het gas af.</strong> Zie <a href="/inductiekookplaat-aansluiten-rotterdam/">inductiekookplaat aansluiten</a>, <a href="/perilex-aansluiten-rotterdam/">perilex aansluiten of verplaatsen</a> en <a href="/meterkast-verzwaren-rotterdam/">meterkast verzwaren</a>.</span></li>
  <li>{check}<span><strong>Verbouwing van badkamer of zolder.</strong> Zie <a href="/elektra-badkamer-rotterdam/">elektra in de badkamer</a>, <a href="/infraroodpanelen-aansluiten-rotterdam/">infraroodpanelen</a> en <a href="/bedrading-vervangen-rotterdam/">bedrading vervangen</a>.</span></li>
  <li>{check}<span><strong>Lampen, stopcontacten en buiten.</strong> Zie <a href="/lampen-ophangen-rotterdam/">lampen ophangen</a>, <a href="/stopcontact-plaatsen-rotterdam/">stopcontact plaatsen of verplaatsen</a> en <a href="/buitenverlichting-tuinstopcontact-rotterdam/">buitenverlichting en tuinstopcontact</a>.</span></li>
  <li>{check}<span><strong>Elektrische auto of zonnepanelen.</strong> Zie <a href="/laadpaal-installeren-rotterdam/">laadpaal installeren</a>, <a href="/vrije-groep-stekkerbatterij-rotterdam/">vrije groep voor een stekkerbatterij</a> en onze uitleg over <a href="/salderen-stopt-2027/">het einde van salderen in 2027</a>.</span></li>
  <li>{check}<span><strong>Werkplaats, garage of machine op 400 volt.</strong> Zie <a href="/krachtstroom-aansluiten-rotterdam/">krachtstroom aansluiten</a>.</span></li>
  <li>{check}<span><strong>Huis kopen, verkopen, verhuren of beheren.</strong> Zie <a href="/elektra-keuring-rotterdam/">keuring van de elektrische installatie</a> en <a href="/elektricien-verhuurders-vve-rotterdam/">elektricien voor verhuurders en VvE's</a>.</span></li>
</ul>

<h2>Alle diensten <em>op een rij.</em></h2>
{tiles}

<h2>Elektra in Rotterdam: <em>oude huizen, veel flats.</em></h2>
<p>Rotterdam is voor een elektricien een bijzondere stad. Van de ruim 330.000 woningen is 29 procent gebouwd vóór 1945; in heel Nederland is dat 18 procent. Vooral de jaren 1925 tot 1944 springen eruit: 15 procent van de Rotterdamse woningen komt uit die periode, bijna twee keer zoveel als landelijk. Ruim de helft van alle woningen in de stad is gebouwd vóór 1975. En driekwart is een flat, portiekwoning, boven- of benedenwoning; in heel Nederland is dat ruim een derde.</p>
<p>Veel van die woningen hebben inmiddels een nieuwe installatie, maar lang niet allemaal. Wat er in een oudere Rotterdamse woning kan spelen:</p>
<ul class="checks">
  <li>{check}<span><strong>Geen of te weinig aardlekbeveiliging.</strong> In nieuwbouw is een aardlekschakelaar pas sinds 1975 verplicht. Een kast met draaistoppen heeft er meestal geen. Dan is <a href="/groepenkast-vervangen-rotterdam/">een nieuwe groepenkast</a> de veiligste stap.</span></li>
  <li>{check}<span><strong>Weinig groepen.</strong> Een oude kast is gemaakt voor verlichting en een paar apparaten, niet voor een inductiekookplaat, vaatwasser, droger en elektrische kachel tegelijk. Slaan groepen vaak door, dan helpt een <a href="/groep-bijplaatsen-rotterdam/">extra groep</a> of een nieuwe kast.</span></li>
  <li>{check}<span><strong>Oude bedrading.</strong> Stopcontacten met randaarde zonder aarddraad erachter, verkleurde draden of oude kleuren. Wij meten na wat er zit voordat we iets aansluiten. Zie <a href="/bedrading-vervangen-rotterdam/">bedrading vervangen</a>.</span></li>
  <li>{check}<span><strong>Betonnen plafonds en muren.</strong> In veel portiekflats uit de jaren 50 en 60 is frezen lastig. Nieuwe leidingen komen dan vaak in een nette opbouwgoot of via een bestaand lichtpunt.</span></li>
  <li>{check}<span><strong>Flat of VvE.</strong> Uw eigen meterkast en installatie zijn van u (of van uw verhuurder). Het trappenhuis, de lift en de gemeenschappelijke verlichting horen bij de VvE. Zie <a href="/elektricien-verhuurders-vve-rotterdam/">verhuurders en VvE's</a>.</span></li>
</ul>
<p>Wilt u weten hoe oud uw woning is? Het bouwjaar staat in het Kadaster (BAG). Stuur het gerust mee in uw bericht, samen met een foto van de meterkast.</p>

<h2>Gaat uw wijk <em>van het gas af?</em></h2>
<p>Rotterdam haalt wijk voor wijk woningen van het aardgas af. Woont u in een eigen woning in een van de aangewezen straten in Bospolder-Tussendijken, Heindijk, Pendrecht-Zuid of Reyeroord-West, en heeft u van de gemeente een persoonlijk aanbod gekregen om over te stappen op het warmtenet? Dan kunt u subsidie krijgen voor de overstap naar elektrisch koken: maximaal 500 euro per adres, één keer, aan te vragen tot en met 30 september 2030. Welke straten meedoen, staat op de pagina 'Subsidie elektrisch koken aanvragen' van de gemeente. Andere wijken komen later aan de beurt.</p>
<p>Voor elektrisch koken is meestal een eigen kookgroep nodig, vaak met een perilex-aansluiting bij de kookplaat. In een oudere kast is daar niet altijd ruimte voor. Met een foto van uw meterkast zien wij of een <a href="/inductiekookplaat-aansluiten-rotterdam/">extra groep voor inductie</a> genoeg is, of dat de kast eerst moet worden uitgebreid of vervangen. Een zwaardere aansluiting is voor een gewone inductiekookplaat bijna nooit nodig; zie <a href="/meterkast-verzwaren-rotterdam/">meterkast verzwaren</a>.</p>

<h2>Zo <em>werkt het.</em></h2>
<ol class="steps-list">
  <li><strong>Stuur een WhatsApp</strong> met wat er moet gebeuren, uw wijk of postcode en een foto van de meterkast of de plek.</li>
  <li><strong>Binnen 24 uur reactie,</strong> met een duidelijke prijs vooraf. Bij grotere klussen krijgt u eerst een offerte; soms vragen we nog een foto of komen we kijken.</li>
  <li><strong>We plannen een afspraak</strong> die u past. Bij een storing zijn we 24/7 bereikbaar.</li>
  <li><strong>Verzekerde vakmensen voeren het werk uit</strong> volgens NEN 1010.</li>
  <li><strong>Oplevering:</strong> we lopen alles samen met u na, vertellen wat er veranderd is en laten de ruimte schoon achter. Daarna krijgt u een factuur.</li>
</ol>

<h2>Waar let u op bij <em>een elektricien?</em></h2>
<p>Of u nu ons inschakelt of een ander bedrijf: met deze punten voorkomt u verrassingen.</p>
<ul class="checks">
  <li>{check}<span><strong>Ingeschreven bij de KvK.</strong> Een echt bedrijf heeft een KvK-nummer en een adres dat u kunt controleren in het Handelsregister. Het onze staat onderaan elke pagina.</span></li>
  <li>{check}<span><strong>Prijs vooraf, op schrift.</strong> Vraag wat er in de prijs zit: materiaal, voorrijden, afvoer van oude onderdelen. Zo kunt u eerlijk vergelijken.</span></li>
  <li>{check}<span><strong>Verzekerd en volgens de norm.</strong> Werk aan de vaste installatie hoort te voldoen aan NEN 1010.</span></li>
  <li>{check}<span><strong>Geen werk aan verzegelde delen.</strong> De hoofdzekering en de meter zijn van de netbeheerder (in Rotterdam Stedin) en zitten achter een zegel. Daar mag alleen aan worden gewerkt met toestemming van de netbeheerder.</span></li>
  <li>{check}<span><strong>Een factuur achteraf.</strong> Met het KvK- en btw-nummer van het bedrijf. Die heeft u ook nodig als er later iets is.</span></li>
</ul>

<h2>Waarom kiezen voor <em>AlleKlussers?</em></h2>
<ul class="checks">
  <li>{check}<span><strong>Duidelijke prijs vooraf.</strong> U weet waar u aan toe bent voordat we beginnen. Geen verrassingen achteraf.</span></li>
  <li>{check}<span><strong>Snel geregeld.</strong> Binnen 24 uur reactie, en bij storingen 24/7 bereikbaar.</span></li>
  <li>{check}<span><strong>Veilig en volgens de norm.</strong> Verzekerde vakmensen die werken volgens NEN 1010.</span></li>
  <li>{check}<span><strong>Netjes opgeleverd.</strong> We lopen alles samen met u na en laten de ruimte schoon achter.</span></li>
</ul>

<h2>Werkgebied</h2>
<p>We werken in heel Rotterdam en in de gemeenten eromheen. Twijfelt u of we bij u in de buurt komen? Stuur ons gerust een berichtje.</p>
{areas}

<div class="note-box"><p><strong>Bronnen:</strong> Bouwjaarkaart over <a href="https://bouwjaarkaart.nl/gemeente/rotterdam" target="_blank" rel="noopener noreferrer">de bouwjaren van woningen in Rotterdam</a> (CBS StatLine 82550NED, peildatum 1 januari 2026), gemeente Rotterdam over <a href="https://www.rotterdam.nl/subsidie-elektrisch-koken-aanvragen" target="_blank" rel="noopener noreferrer">subsidie elektrisch koken aanvragen</a>.</p></div>
""",
        "faq": [
            ("Wat kost een elektricien in Rotterdam?",
             "Dat hangt af van de klus. Voor kleine klussen zoals lampen ophangen of een stopcontact plaatsen spreken we vaak een vaste prijs af. Voor grotere klussen krijgt u eerst een offerte. U weet dus altijd vooraf wat het kost."),
            ("Hoe snel kunnen jullie komen?",
             "U krijgt binnen 24 uur reactie op uw aanvraag. Bij een storing zijn we 24/7 bereikbaar en plannen we zo snel mogelijk een afspraak in."),
            ("Zijn jullie verzekerd?",
             "Ja. Onze vakmensen zijn verzekerd en werken volgens NEN 1010, de norm voor veilige elektrische installaties in Nederland."),
            ("Werken jullie ook voor verhuurders en bedrijven?",
             "Ja. Naast particulieren helpen we ook verhuurders, vastgoedbeheerders en bedrijven, voor losse klussen en voor terugkerend onderhoud."),
            ("Doen jullie ook andere klussen dan elektra?",
             "Nee. We doen alleen elektra: storingen, groepenkasten, verlichting, stopcontacten, bedrading, keuringen, laadpalen en aansluitingen voor keuken en badkamer. Voor schilderwerk, vloeren of loodgieterswerk kunt u beter een specialist in dat vak zoeken."),
            ("Mijn huis is van vóór 1975. Moet de groepenkast dan vervangen worden?",
             "Niet altijd. Veel oudere woningen hebben al een nieuwere kast. Heeft uw kast nog draaistoppen of geen aardlekschakelaar, dan raden we vervangen wel aan. Stuur een foto van de open meterkast, dan zeggen we wat er nodig is."),
            ("Is er in Rotterdam subsidie voor elektrisch koken?",
             "Ja, maar alleen voor eigenaar-bewoners in aangewezen straten in Bospolder-Tussendijken, Heindijk, Pendrecht-Zuid en Reyeroord-West die een aanbod van de gemeente hebben gekregen om over te stappen op het warmtenet. Het gaat om maximaal 500 euro per adres, aan te vragen tot en met 30 september 2030. Kijk op de website van de gemeente Rotterdam of uw straat meedoet."),
            ("Wat stuur ik het beste mee in mijn bericht?",
             "Wat er moet gebeuren, uw wijk of postcode en een foto van de open meterkast of de plek waar het werk komt. Heeft u een nieuw apparaat, zoals een kookplaat of laadpaal, stuur dan ook een foto van het typeplaatje of het merk en type."),
            ("Ik huur mijn woning. Kan ik jullie zelf inschakelen?",
             "Een storing of gebrek in de vaste installatie meldt u eerst bij uw verhuurder of woningcorporatie. Wilt u zelf iets laten veranderen of bijplaatsen, vraag dan vooraf toestemming aan de verhuurder. Verhuurders en beheerders kunnen ons ook rechtstreeks inschakelen."),
        ],
    },
    # ------------------------------------------------------------- STORING
    {
        "slug": "storing-elektra-rotterdam",
        "short": "Storing verhelpen",
        "sub": "Stroomuitval en een aardlekschakelaar die steeds doorslaat.",
        "title": "Storing elektra Rotterdam | Stroom uitgevallen? AlleKlussers",
        "desc": "Stroom uitgevallen in Rotterdam? Zo ziet u of het aan het net of uw meterkast ligt, wat u zelf kunt nagaan en wanneer u ons appt. 24/7 bereikbaar.",
        "service": "Storing elektra verhelpen",
        "char": "vonk",
        "say": "“Stroom uit? Wij zijn 24/7 bereikbaar.”",
        "eyebrow": "Storingen en spoed",
        "h1": "Storing of stroomuitval in <em>Rotterdam?</em>",
        "lede": "Valt de stroom uit, of slaat er steeds iets door in de meterkast? Met de stappen hieronder ziet u in een paar minuten of het bij u thuis zit of in het net. Zit het bij u, dan zoeken wij de oorzaak en lossen het veilig op.",
        "body": """
<div class="note-box"><p><strong>Ruikt u een brandlucht, ziet u rook of vonken, of voelt de meterkast warm aan?</strong> Zet de hoofdschakelaar in de meterkast uit als dat veilig kan en bel bij gevaar direct 112. Komt er water in of bij de meterkast, raak dan niets aan.</p></div>

<h2>Stap 1: <em>bij u of in de buurt?</em></h2>
<p>Kijk eerst of de buren, het trappenhuis of de straatverlichting ook geen stroom hebben. Is het hele blok of de straat donker, dan is het een storing in het net. Daar kan geen elektricien iets aan doen; dat lost de netbeheerder op. In Rotterdam en omgeving is dat Stedin.</p>
<ul class="checks">
  <li>{check}<span><strong>Melden:</strong> bel het landelijke storingsnummer <strong>0800-9009</strong>. Dat is gratis en dag en nacht bereikbaar, voor stroom en gas. Houd uw postcode en huisnummer bij de hand. Bekende storingen staan ook op de website van Stedin.</span></li>
  <li>{check}<span><strong>Niet uw energieleverancier:</strong> die gaat niet over storingen in het net. De netbeheerder wel.</span></li>
  <li>{check}<span><strong>Lang zonder stroom?</strong> Duurt een storing in het net vier uur of langer achter elkaar, dan kunt u recht hebben op een vergoeding van de netbeheerder. Voor gepland onderhoud geldt dat niet.</span></li>
</ul>
<p>Hebben de buren wel stroom en u niet, dan ligt het bijna altijd aan uw eigen installatie. Ga dan naar stap 2.</p>

<h2>Stap 2: <em>wat staat er omlaag in de meterkast?</em></h2>
<p>Open de meterkast en kijk welke schakelaar naar beneden staat. Dat vertelt al veel over de oorzaak.</p>
<ul class="checks">
  <li>{check}<span><strong>Eén groepsschakelaar staat omlaag.</strong> Die groep is overbelast of er is kortsluiting. Viel hij uit nadat er een tijdje veel aanstond, zoals een kachel, waterkoker en magnetron tegelijk? Dan is het overbelasting. Viel hij direct uit toen u iets aanzette of insteekte? Dan is het vaak kortsluiting in dat apparaat, het snoer of een stekkerdoos.</span></li>
  <li>{check}<span><strong>De aardlekschakelaar staat omlaag</strong> (de schakelaar met een testknop T), en daarmee een heel deel van het huis. Dan is er ergens lekstroom gemeten, vaak door een apparaat of door vocht. Op de pagina over de <a href="/aardlekschakelaar-rotterdam/">aardlekschakelaar</a> staat een stappenplan om de groep en het apparaat te vinden.</span></li>
  <li>{check}<span><strong>De hoofdschakelaar staat uit.</strong> Zet eerst alle groepen uit, dan de hoofdschakelaar aan, en daarna de groepen één voor één. Valt hij meteen weer uit, stop dan en stuur ons een bericht.</span></li>
  <li>{check}<span><strong>Niets staat omlaag, toch is alles donker.</strong> Dan kan het probleem vóór uw groepenkast zitten: bij de hoofdzekering, de meter of de aansluitkabel. Die zijn van de netbeheerder en zitten achter een zegel. Kom daar niet aan en bel het storingsnummer 0800-9009.</span></li>
  <li>{check}<span><strong>Een oude kast met draaistoppen?</strong> Bij een gesprongen smeltzekering is het gekleurde plaatje achter het kijkglaasje weg. Gebeurt dat vaker, dan is de kast toe aan <a href="/groepenkast-vervangen-rotterdam/">vervanging</a>: zo'n kast heeft meestal ook geen aardlekbeveiliging.</span></li>
</ul>

<h2>Stap 3: <em>de schakelaar weer omhoog.</em></h2>
<ol class="steps-list">
  <li><strong>Haal de stekkers eruit</strong> van de apparaten op de groep die uitviel, of zet die apparaten uit.</li>
  <li><strong>Zet de schakelaar één keer omhoog.</strong> Blijft hij staan, steek de apparaten dan één voor één terug. Het apparaat waarbij hij weer uitvalt, gebruikt u niet meer tot het is nagekeken.</li>
  <li><strong>Valt hij direct weer uit, ook zonder apparaten?</strong> Probeer het dan niet steeds opnieuw. De fout zit dan in de vaste installatie, bijvoorbeeld in een lamp, een losse draad of een beschadigde leiding. Dat is werk voor een elektricien.</li>
</ol>
<p>Een schakelaar die uitvalt, doet precies zijn werk. Plak hem nooit vast en overbrug hem nooit: dan beschermt hij niemand meer tegen brand of een schok.</p>

<h2>In de winter: <em>kachel, kerstverlichting en droger.</em></h2>
<p>In de koude maanden krijgen we meer meldingen van groepen die doorslaan. Dat heeft meestal een eenvoudige oorzaak.</p>
<ul class="checks">
  <li>{check}<span><strong>Elektrische kachel.</strong> Een normale groep van 16 ampère kan ongeveer 3.680 watt aan. Een kachel van 2.000 watt met daarbij een waterkoker of föhn op dezelfde groep is al te veel. Zet de kachel op een andere groep, of laat <a href="/groep-bijplaatsen-rotterdam/">een extra groep</a> aanleggen als dit vaak gebeurt. Wilt u een kamer vaker elektrisch verwarmen, kijk dan ook naar <a href="/infraroodpanelen-aansluiten-rotterdam/">infraroodpanelen</a> met een vaste aansluiting.</span></li>
  <li>{check}<span><strong>Kerstverlichting buiten.</strong> Slaat de aardlek vooral door bij regen of mist, dan zit er vaak vocht in een stekker of verlengsnoer buiten. Gebruik verlichting en snoeren die geschikt zijn voor buiten, of een vast <a href="/buitenverlichting-tuinstopcontact-rotterdam/">buitenstopcontact</a>.</span></li>
  <li>{check}<span><strong>Wasdroger en wasmachine tegelijk.</strong> Twee apparaten die warmte maken op één groep, dat gaat vaak mis. Ieder hoort een eigen groep te hebben.</span></li>
  <li>{check}<span><strong>Stekkerdozen achter elkaar.</strong> Koppel geen stekkerdozen aan elkaar en zet geen zware apparaten op een stekkerdoos. Een snoer dat warm wordt, is een waarschuwing.</span></li>
</ul>

<h2>Tijdens de <em>stroomuitval.</em></h2>
<ul class="checks">
  <li>{check}<span><strong>Houd de vriezer en koelkast dicht.</strong> Een dichte vriezer houdt eten vaak 10 tot 18 uur bevroren; in de handleiding van uw vriezer staat hoe lang precies. Vries eten dat ontdooid is niet opnieuw in.</span></li>
  <li>{check}<span><strong>Zet zware apparaten uit,</strong> zoals de kookplaat, oven, kachel en het strijkijzer. Dan slaat er niet alles tegelijk aan als de stroom terugkomt, en blijft er niets onverwacht aan staan.</span></li>
  <li>{check}<span><strong>Liever een zaklamp dan kaarsen.</strong> Gebruikt u toch kaarsen, laat ze dan niet alleen branden.</span></li>
</ul>

<h2>Wat wij <em>doen.</em></h2>
<p>Zit de storing in uw eigen installatie, dan komt onze elektricien met meetapparatuur. We meten de installatie groep voor groep door en zoeken uit waar de fout zit: een defect apparaat, een losse verbinding in een lasdoos, een beschadigde leiding, vocht in een buitenpunt of een versleten schakelaar in de groepenkast. Daarna lossen we het op. Is de reparatie groter, dan bespreken we eerst met u wat er nodig is en wat het kost.</p>
<p>U krijgt uitleg over de oorzaak en advies om herhaling te voorkomen, bijvoorbeeld door groepen beter te verdelen. Is de kast oud of vol, dan zeggen we eerlijk of <a href="/groepenkast-vervangen-rotterdam/">uitbreiden of vervangen</a> verstandig is. Alles volgens NEN 1010, door verzekerde vakmensen.</p>

<h2>Zo <em>werkt het.</em></h2>
<ol class="steps-list">
  <li><strong>Stuur een WhatsApp</strong> met een foto van uw open meterkast. Vertel welke schakelaar omlaag staat, wanneer het gebeurt (altijd, bij regen, 's nachts of bij één apparaat) en wat u al geprobeerd heeft.</li>
  <li><strong>We reageren zo snel mogelijk.</strong> Bij een storing zijn we 24/7 bereikbaar. Soms is het met dit advies al opgelost; anders plannen we een afspraak.</li>
  <li><strong>U hoort de prijs vooraf,</strong> voordat we aan de reparatie beginnen.</li>
</ol>
<p>Huurt u? Een storing in de vaste installatie meldt u eerst bij uw verhuurder of woningcorporatie. Verhuurders en VvE's helpen we ook rechtstreeks, zie <a href="/elektricien-verhuurders-vve-rotterdam/">elektricien voor verhuurders en VvE's</a>.</p>

<div class="note-box"><p><strong>Bronnen:</strong> Selectra over <a href="https://selectra.nl/energie/netbeheerder/stedin/storing" target="_blank" rel="noopener noreferrer">wat te doen bij een Stedin-storing</a> (storingsnummer en vergoeding), Energievergelijk over <a href="https://www.energievergelijk.nl/onderwerpen/stroomstoring" target="_blank" rel="noopener noreferrer">stroomstoring: thuis of in het net</a>, Beko over <a href="https://www.beko.com/be-nl/Ondersteuning/vriezer--gebruiken--veelgestelde-vragen/de-stroom-naar-mijn-vriezer-is-uitgevallen-door-een-stroomstoring-hoe-zorg-ik-ervoor-dat-mijn-etenswaren-tijdens-een-stroomstoring-goed-blijven" target="_blank" rel="noopener noreferrer">de vriezer bij een stroomstoring</a>.</p></div>
""",
        "faq": [
            ("De hele straat heeft geen stroom. Moet ik jullie inschakelen?",
             "Nee, dan is het een storing in het net. Die meldt u bij het landelijke storingsnummer 0800-9009 (gratis, dag en nacht). In Rotterdam lost netbeheerder Stedin de storing op."),
            ("Alleen bij mij is de stroom uit, maar er staat niets omlaag. Wat nu?",
             "Kijk of de hoofdschakelaar aan staat. Staat alles goed en is het toch donker, dan kan het probleem bij de hoofdzekering, de meter of de aansluiting zitten. Die zijn van de netbeheerder en verzegeld: bel dan 0800-9009 en kom zelf niet aan de verzegelde delen."),
            ("Mijn aardlekschakelaar slaat steeds door. Wat nu?",
             "Zet de groepen eronder uit, zet de aardlekschakelaar omhoog en zet de groepen één voor één weer aan. Zo vindt u de groep, en daarna met de stekkers het apparaat. Slaat hij ook zonder apparaten door, dan zit de fout in de installatie en is een elektricien nodig."),
            ("Mijn groep valt uit als de elektrische kachel aan staat. Hoe komt dat?",
             "Een gewone groep van 16 ampère kan ongeveer 3.680 watt aan. Een kachel gebruikt vaak 2.000 watt of meer, dus samen met een waterkoker of föhn is de groep overbelast. Gebruik de kachel op een andere groep of laat een extra groep aanleggen."),
            ("Wat is het verschil tussen overbelasting en kortsluiting?",
             "Bij overbelasting vraagt u meer stroom dan de groep aankan; de schakelaar valt dan na een tijdje uit. Bij kortsluiting raken twee draden elkaar, vaak in een defect apparaat of snoer; de schakelaar valt dan direct uit, meestal op het moment dat u iets aanzet."),
            ("Hoe lang blijft eten in de vriezer goed bij stroomuitval?",
             "Houd de vriezer dicht. Een dichte vriezer houdt eten vaak 10 tot 18 uur bevroren; de handleiding van uw model geeft de precieze tijd. Eten dat ontdooid is, vriest u niet opnieuw in."),
            ("Krijg ik een vergoeding als de stroom lang uitvalt?",
             "Bij een storing in het net van vier uur of langer achter elkaar kunt u recht hebben op een vergoeding van de netbeheerder. Ligt de oorzaak in uw eigen installatie of gaat het om gepland onderhoud, dan niet."),
            ("Zijn jullie ook 's avonds en in het weekend bereikbaar?",
             "Ja, we zijn 24/7 bereikbaar. Stuur ons een WhatsApp met een foto van de meterkast, dan kijken we hoe snel we bij u kunnen zijn."),
            ("Wat kost het verhelpen van een storing?",
             "Dat hangt af van de oorzaak. We bespreken de kosten met u voordat we aan de reparatie beginnen."),
        ],
    },
    # ------------------------------------------------------------ AARDLEK
    {
        "slug": "aardlekschakelaar-rotterdam",
        "short": "Aardlekschakelaar",
        "sub": "Slaat hij steeds door, of is hij aan vervanging toe?",
        "title": "Aardlekschakelaar slaat door in Rotterdam? | AlleKlussers",
        "desc": "Slaat uw aardlekschakelaar steeds door in Rotterdam? Zo vindt u zelf de groep of het apparaat. Wij meten de oorzaak op en lossen het op volgens NEN 1010.",
        "service": "Aardlekschakelaar storing en vervangen",
        "char": "schildje",
        "say": "“Ik bescherm u. Soms iets te graag.”",
        "eyebrow": "Aardlekschakelaar",
        "h1": "Aardlekschakelaar slaat <em>steeds door?</em>",
        "lede": "Een aardlekschakelaar die uitvalt doet meestal precies zijn werk: hij ziet ergens stroom weglekken. Met dit stappenplan vindt u vaak zelf de groep of het apparaat. Lukt dat niet, dan zoeken wij het voor u uit.",
        "body": """
<h2>Wat doet een <em>aardlekschakelaar?</em></h2>
<p>De aardlekschakelaar in uw meterkast vergelijkt de stroom die een groep in gaat met de stroom die terugkomt. Zit daar verschil tussen, dan lekt er ergens stroom weg, bijvoorbeeld via een defect apparaat, via vocht of in het ergste geval via iemand die iets aanraakt. Binnen een fractie van een seconde schakelt hij dan alles erachter uit. Op de meeste Nederlandse woningschakelaars staat 30 mA: zo weinig lekstroom is al genoeg.</p>
<p>U herkent hem aan de testknop met een T. Meestal zitten er meerdere groepen achter. Daarom valt bij een aardlekstoring vaak een flink deel van het huis tegelijk uit.</p>

<h2>Aardlek of groep: <em>wat is er uitgevallen?</em></h2>
<ul class="checks">
  <li>{check}<span><strong>Alleen één groepsschakelaar staat omlaag?</strong> Dan is het meestal overbelasting of kortsluiting op die ene groep, bijvoorbeeld te veel zware apparaten tegelijk. Dat is iets anders dan een aardlekstoring.</span></li>
  <li>{check}<span><strong>De aardlekschakelaar staat omlaag?</strong> Dan is er lekstroom gemeten op een van de groepen erachter. Volg dan het stappenplan hieronder.</span></li>
  <li>{check}<span><strong>Valt alles uit, ook bij de buren?</strong> Dan is het een storing in het net. Die meldt u bij de netbeheerder; in Rotterdam is dat Stedin.</span></li>
</ul>

<h2>Stappenplan: <em>zelf de oorzaak vinden.</em></h2>
<ol class="steps-list">
  <li><strong>Zet alle groepen onder de aardlekschakelaar uit</strong> en zet daarna de aardlekschakelaar weer omhoog.</li>
  <li><strong>Zet de groepen één voor één weer aan.</strong> Slaat de aardlek door bij een bepaalde groep, dan weet u waar het probleem zit.</li>
  <li><strong>Haal op die groep alle stekkers uit het stopcontact</strong> en probeer het opnieuw. Blijft hij nu staan, steek de apparaten dan één voor één terug. Het apparaat waarbij hij doorslaat, is vaak de boosdoener.</li>
  <li><strong>Slaat hij door zonder dat er iets is aangesloten,</strong> of zelfs met alle groepen uit? Dan zit de fout in de vaste bedrading, een lamp of buitenpunt, of in de aardlekschakelaar zelf. Dat is werk voor een elektricien.</li>
</ol>
<div class="note-box"><p><strong>Nooit overbruggen of vastzetten.</strong> Een aardlekschakelaar die u "even" buiten werking zet, beschermt niemand meer tegen een elektrische schok. Ruikt u een brandlucht of ziet u rook of vonken? Zet de hoofdschakelaar uit als dat veilig kan en bel bij gevaar 112.</p></div>

<h2>Veelvoorkomende <em>oorzaken.</em></h2>
<ul class="checks">
  <li>{check}<span><strong>Vocht en regen.</strong> Slaat hij vooral door bij regen of mist, kijk dan naar buitenlampen, een <a href="/buitenverlichting-tuinstopcontact-rotterdam/">tuinstopcontact</a>, de schuur of de badkamer.</span></li>
  <li>{check}<span><strong>Apparaten met een verwarmingselement,</strong> zoals een wasdroger, wasmachine, boiler, vaatwasser, oven of een oude koelkast.</span></li>
  <li>{check}<span><strong>'s Nachts uitgevallen?</strong> Denk aan apparaten die op een tijdklok aanslaan, zoals een boiler, een vaatwasser met uitgestelde start of een opladende accu.</span></li>
  <li>{check}<span><strong>Te veel op één aardlek.</strong> Elk apparaat lekt een heel klein beetje. Zitten veel apparaten achter dezelfde aardlekschakelaar, dan tellen die kleine lekstromen op tot hij zonder duidelijke reden uitvalt.</span></li>
  <li>{check}<span><strong>Beschadigde of verouderde bedrading,</strong> bijvoorbeeld door een spijker of boorgat in een leiding. Lees meer over <a href="/bedrading-vervangen-rotterdam/">bedrading vervangen</a>.</span></li>
  <li>{check}<span><strong>Een defecte aardlekschakelaar.</strong> Ook de schakelaar zelf kan versleten raken en te snel, of juist niet meer, uitschakelen.</span></li>
</ul>

<h2>Test uw aardlekschakelaar <em>een paar keer per jaar.</em></h2>
<p>Druk op de testknop (T). De aardlekschakelaar moet direct uitschakelen; zet hem daarna weer omhoog. Gebeurt er niets, dan beschermt hij u niet meer en moet hij worden nagekeken. Een vaste regel voor hoe vaak u moet testen is er niet. Een paar keer per jaar, na een verbouwing en als u in een nieuw huis komt wonen, is een goede gewoonte.</p>

<h2>Wat wij <em>doen.</em></h2>
<ul class="checks">
  <li>{check}<span><strong>Meten in plaats van gokken.</strong> We meten de installatie groep voor groep door en zoeken uit waar de lekstroom vandaan komt.</span></li>
  <li>{check}<span><strong>De oorzaak oplossen:</strong> een vochtige buitenlamp vervangen, een beschadigde leiding herstellen of u vertellen welk apparaat defect is.</span></li>
  <li>{check}<span><strong>Aardlekschakelaar vervangen</strong> als hij zelf defect of verouderd is.</span></li>
  <li>{check}<span><strong>Groepen beter verdelen.</strong> Zitten bij u veel groepen achter één aardlekschakelaar, dan verdelen we ze over meer aardlekschakelaars of geven we groepen een eigen aardlekautomaat. Dan valt bij een storing niet meer het halve huis uit.</span></li>
</ul>
<p>Is de kast verouderd of vol, dan bespreken we eerlijk of <a href="/groepenkast-vervangen-rotterdam/">uitbreiden of vervangen</a> verstandiger is. Wilt u weten hoe uw hele installatie ervoor staat, kijk dan bij <a href="/elektra-keuring-rotterdam/">keuring van de installatie</a>. Alles volgens NEN 1010, door verzekerde vakmensen.</p>

<h2>Zo <em>werkt het.</em></h2>
<p>Stuur ons via WhatsApp een foto van uw meterkast en vertel wanneer de aardlek doorslaat: altijd, bij regen, 's nachts of bij één bepaald apparaat. Dat helpt ons de oorzaak sneller te vinden. U krijgt binnen 24 uur reactie met een duidelijke prijs vooraf, en bij een storing zijn we 24/7 bereikbaar.</p>
""",
        "faq": [
            ("Wat is het verschil tussen een aardlekschakelaar en een groepsschakelaar?",
             "Een groepsschakelaar (installatieautomaat) beschermt de leiding van één groep tegen overbelasting en kortsluiting. Een aardlekschakelaar beschermt mensen: hij schakelt meerdere groepen tegelijk uit zodra er ergens stroom weglekt."),
            ("Mijn aardlekschakelaar slaat alleen door als het regent. Hoe kan dat?",
             "Dan komt er waarschijnlijk vocht in een buitenlamp, buitenstopcontact, tuinverlichting of een leiding naar de schuur. Zet die groep zo nodig uit en laat het buitenpunt controleren; vocht in elektra wordt meestal niet vanzelf beter."),
            ("Wat is een aardlekautomaat?",
             "Een aardlekautomaat combineert een aardlekschakelaar en een groepsschakelaar in één module, voor één groep. Bij een storing valt dan alleen die ene groep uit en niet een heel deel van het huis."),
            ("Kan ik een aardlekschakelaar zelf vervangen?",
             "Dat raden we af. Ook met de hoofdschakelaar uit kan er in de meterkast nog spanning staan op de toevoer. Laat het werk in de groepenkast doen door een vakman die de installatie daarna ook doormeet."),
            ("Hoe vaak moet ik op de testknop drukken?",
             "Een vaste regel is er niet. Een paar keer per jaar testen, en ook na een verbouwing of bij een verhuizing, is een goede gewoonte. Schakelt hij bij de test niet uit, laat hem dan nakijken."),
            ("Wat kost het om de oorzaak te laten zoeken?",
             "Dat hangt af van de oorzaak en hoe groot de reparatie is. U hoort de prijs altijd voordat we aan de reparatie beginnen."),
        ],
    },
    # ---------------------------------------------------------- GROEPENKAST
    {
        "slug": "groepenkast-vervangen-rotterdam",
        "short": "Groepenkast vervangen",
        "sub": "Vervangen of uitbreiden, met hoofdschakelaar en ruimte voor later.",
        "title": "Groepenkast vervangen of uitbreiden Rotterdam | AlleKlussers",
        "desc": "Oude of volle groepenkast? We vervangen of breiden hem uit in Rotterdam en omgeving, met aardlek, hoofdschakelaar en ruimte voor later. Prijs vooraf.",
        "service": "Groepenkast vervangen en uitbreiden",
        "char": "kastje",
        "say": "“Meer groepen nodig? Ik regel het.”",
        "eyebrow": "Groepenkasten",
        "h1": "Groepenkast vervangen of uitbreiden in <em>Rotterdam.</em>",
        "lede": "Een veilige groepenkast met genoeg groepen voor inductie, een laadpaal, een warmtepomp of een verbouwing. Soms is uitbreiden genoeg, soms is een nieuwe kast verstandiger. Wij zeggen u eerlijk welke van de twee.",
        "body": """
<h2>Uitbreiden of vervangen: <em>wat past bij uw kast?</em></h2>
<p>Een groepenkast gaat gerust 30 tot 40 jaar mee. Er hoeft dus niet bij elke nieuwe wens een nieuwe kast te komen. Of uitbreiden genoeg is, hangt vooral af van wat er nu in zit.</p>
<ul class="checks">
  <li>{check}<span><strong>Uitbreiden kan vaak</strong> als de kast al aardlekschakelaars en een hoofdschakelaar heeft, en er nog plek is of een extra rij bij kan. Dan voegen we groepen of een aardlekautomaat toe. Gaat het om één apparaat, zoals een droger of airco? Dan is <a href="/groep-bijplaatsen-rotterdam/">een groep bijplaatsen</a> meestal genoeg.</span></li>
  <li>{check}<span><strong>Vervangen is verstandig</strong> bij draaistoppen of smeltzekeringen, als er geen of maar één aardlekschakelaar in zit, als er geen hoofdschakelaar is, of als de kast vol is en er geen plek meer bij kan.</span></li>
  <li>{check}<span><strong>Vervangen is ook slim bij een grote stap,</strong> zoals een nieuwe keuken met <a href="/inductiekookplaat-aansluiten-rotterdam/">inductie</a>, een warmtepomp, een <a href="/laadpaal-installeren-rotterdam/">laadpaal</a> of een aanbouw. Dan bouwt u niet steeds bij aan een kast die daar nooit voor gemaakt is.</span></li>
  <li>{check}<span><strong>Niet wachten bij deze tekens:</strong> een kast of automaat die warm aanvoelt, bruine verkleuring, brandlucht of een zoemend geluid. Zet dan de groep uit als dat veilig kan en <a href="/storing-elektra-rotterdam/">meld het als storing</a>.</span></li>
</ul>

<h2>Hoe oud is <em>uw groepenkast?</em></h2>
<p>Groepenkasten van voor ongeveer 1975 hebben vrijwel nooit een aardlekschakelaar, en de 1-fase kasten uit die tijd hebben meestal ook geen hoofdschakelaar. Zo herkent u een oude kast:</p>
<ul class="checks">
  <li>{check}<span><strong>Draaistoppen:</strong> porseleinen zekeringen met een kijkglaasje die u eruit kunt draaien, in plaats van automaten met een hendeltje.</span></li>
  <li>{check}<span><strong>Geen testknop:</strong> een aardlekschakelaar heeft een knop met een T. Ziet u die nergens, dan heeft uw kast waarschijnlijk geen aardlekbeveiliging.</span></li>
  <li>{check}<span><strong>Weinig groepen:</strong> twee tot vier groepen voor de hele woning, vaak met een stekkerdoos als oplossing in de keuken.</span></li>
  <li>{check}<span><strong>Geen aarde:</strong> stopcontacten zonder randaarde of draden zonder groen-gele aardedraad wijzen op oude <a href="/bedrading-vervangen-rotterdam/">bedrading</a>. Die nemen we dan mee in het advies.</span></li>
</ul>
<p>Op of in veel kasten zit een sticker of groepenverklaring met een datum. Stuur ons een foto van de open meterkast, dan zien we meestal meteen wat er in zit.</p>

<h2>Wat er in een <em>nieuwe kast</em> komt.</h2>
<ul class="checks">
  <li>{check}<span><strong>Een hoofdschakelaar.</strong> Volgens de huidige NEN 1010 hoort die erin. Zo maakt u in een noodgeval de hele installatie in één keer stroomloos.</span></li>
  <li>{check}<span><strong>Aardlekschakelaars met maximaal vier groepen per stuk,</strong> zo verdeeld dat niet het hele huis donker is als er één uitschakelt.</span></li>
  <li>{check}<span><strong>Eigen groepen voor zware apparaten:</strong> wasmachine, droger, vaatwasser en oven, en een kookgroep voor de kookplaat.</span></li>
  <li>{check}<span><strong>Aardlekautomaten</strong> voor groepen die los moeten staan, zoals een laadpaal of een <a href="/vrije-groep-stekkerbatterij-rotterdam/">vrije groep voor een stekkerbatterij</a>.</span></li>
  <li>{check}<span><strong>Ruimte voor later:</strong> lege plekken voor bijvoorbeeld een warmtepomp of zonnepanelen, en een kast die op 3-fase kan worden aangesloten als u later <a href="/meterkast-verzwaren-rotterdam/">verzwaart</a>.</span></li>
  <li>{check}<span><strong>Een duidelijke groepenverklaring,</strong> zodat u bij elke groep ziet welke ruimte of welk apparaat erop zit.</span></li>
</ul>

<h2>Wat van de netbeheerder is, <em>en wat van u.</em></h2>
<p>De aansluitkabel, de hoofdzekering en de meter zijn van de netbeheerder; in Rotterdam en omgeving is dat Stedin. Alles na de meter, dus de hoofdschakelaar, de groepenkast en de bedrading in huis, is uw eigen installatie. Daar werken wij aan.</p>
<p>De netbeheerder verzegelt de aansluiting en de meter. Die zegels mogen alleen worden verbroken met toestemming van de netbeheerder: door de netbeheerder zelf of door een erkende installateur met zegelrecht. Bij het vervangen van een groepenkast is dat soms nodig, bijvoorbeeld om de kabel tussen meter en groepenkast te vervangen of om tijdens het werk de hoofdzekering te verwijderen. U hoort vooraf of dat bij uw meterkast speelt en hoe het wordt geregeld. Breek een zegel nooit zelf.</p>

<h2>Groepenkasten in <em>Rotterdamse woningen.</em></h2>
<p>In de vooroorlogse woningen in bijvoorbeeld Noord, Kralingen-Crooswijk, Delfshaven, Feijenoord en Charlois zit de meterkast vaak klein in de gang of onder de trap, met een kast die in de loop der jaren is aangepast. In de portiekflats uit de jaren vijftig en zestig komen we nog kasten met maar een paar groepen of met draaistoppen tegen. In woningen uit de jaren zeventig en tachtig zit meestal wel aardlekbeveiliging, maar vaak met weinig groepen. Daar is uitbreiden regelmatig genoeg.</p>
<p>Ook buiten Rotterdam vervangen en breiden we groepenkasten uit, onder meer in <a href="/elektricien-schiedam/">Schiedam</a>, <a href="/elektricien-vlaardingen/">Vlaardingen</a>, <a href="/elektricien-capelle-aan-den-ijssel/">Capelle aan den IJssel</a>, <a href="/elektricien-barendrecht/">Barendrecht</a> en <a href="/elektricien-ridderkerk/">Ridderkerk</a>.</p>
<div class="note-box"><p><strong>Huis van voor 1994?</strong> Dan kan de aftimmering van de meterkast, of de bekleding van de deur en het bovenlicht, asbesthoudend karton of plaat bevatten. Twijfelt u, zeg het ons vooraf of stuur een foto. We boren of zagen daar niet in zolang niet duidelijk is wat het is.</p></div>
<p>Huurt u? De groepenkast hoort bij de woning, dus vraag eerst uw verhuurder of woningcorporatie. Verhuurders en VvE's helpen we ook rechtstreeks, zie <a href="/elektricien-verhuurders-vve-rotterdam/">elektricien voor verhuurders en VvE's</a>.</p>

<h2>Zo <em>pakken we het aan.</em></h2>
<ol class="steps-list">
  <li><strong>Stuur een foto</strong> van uw open meterkast via WhatsApp en vertel wat u van plan bent, nu en de komende jaren.</li>
  <li><strong>U krijgt een duidelijke prijs vooraf,</strong> met daarin of we uitbreiden of vervangen, hoeveel groepen er komen en wat er verder nodig is.</li>
  <li><strong>Op de afgesproken dag is de stroom een aantal uur uit.</strong> Houd de koelkast en vriezer dicht en laad vooraf uw telefoon en laptop op.</li>
  <li><strong>We bouwen de kast, sluiten alle groepen aan en testen ze,</strong> ook elke aardlekschakelaar.</li>
  <li><strong>U krijgt uitleg:</strong> welke groep waarvoor is, hoe de hoofdschakelaar werkt en hoe u de testknop gebruikt. Druk die minimaal twee keer per jaar in.</li>
</ol>
<p>Alles volgens NEN 1010, door verzekerde vakmensen.</p>

<div class="note-box"><p><strong>Bronnen:</strong> <a href="https://www.se.com/nl/nl/about-us/newsroom/news/press-releases/woning-renovatie%E2%80%A6-wel-of-geen-nieuwe-groepenkast-65f850cdb9f47a8ac107da47" target="_blank" rel="noopener noreferrer">Woning renovatie: wel of geen nieuwe groepenkast?</a> (Schneider Electric), <a href="https://www.stedin.net/zakelijk/techniek/zegelrecht" target="_blank" rel="noopener noreferrer">Zegelrecht</a> (Stedin), <a href="https://iplo.nl/thema/asbest/asbestwegwijzer/binnen-huis/" target="_blank" rel="noopener noreferrer">Asbest binnen in huis</a> (Informatiepunt Leefomgeving).</p></div>
""",
        "faq": [
            ("Kan mijn oude groepenkast worden uitgebreid in plaats van vervangen?",
             "Vaak wel, als er al aardlekschakelaars en een hoofdschakelaar in zitten en er plek is voor een extra rij of automaat. Heeft de kast draaistoppen of geen aardlekbeveiliging, dan raden we uitbreiden af en adviseren we een nieuwe kast."),
            ("Hoe weet ik hoe oud mijn groepenkast is?",
             "Kijk naar een sticker of groepenverklaring met een datum. Draaistoppen en het ontbreken van een testknop met een T wijzen op een kast van voor ongeveer 1975. Stuur een foto, dan kijken we mee."),
            ("Is een hoofdschakelaar verplicht?",
             "Volgens de huidige NEN 1010 hoort er een hoofdschakelaar in de installatie. Veel oude 1-fase kasten hebben er geen. Bij een nieuwe kast plaatsen we er altijd een."),
            ("Moet Stedin langskomen als mijn groepenkast wordt vervangen?",
             "Voor de groepenkast zelf meestal niet. De netbeheerder komt in beeld als een zegel op de aansluiting of meter open moet, of als u uw aansluiting wilt verzwaren. Dat hoort u vooraf van ons."),
            ("Moet de bedrading ook worden vervangen?",
             "Niet altijd. Is de bedrading in goede staat, dan sluiten we die aan op de nieuwe kast. Zitten er nog oude draden zonder aarde of met stoffen isolatie in huis, dan bespreken we of die beter ook vervangen kunnen worden."),
            ("Kan de nieuwe kast voorbereid worden op een laadpaal, warmtepomp of zonnepanelen?",
             "Ja. We laten lege plekken over en kiezen een kast die op 3-fase kan worden aangesloten. Dan hoeft er later geen nieuwe kast te komen, alleen de groep zelf."),
            ("Hoe lang duurt het vervangen van een groepenkast?",
             "Meestal is het in één dag klaar. Tijdens het werk is de stroom een aantal uur uit; dat stemmen we vooraf met u af."),
            ("Wie betaalt een nieuwe groepenkast in een huurwoning?",
             "De groepenkast staat niet in het Besluit kleine herstellingen. Vervanging hoort daarom in de regel bij de verhuurder. Overleg altijd eerst met uw verhuurder of woningcorporatie."),
            ("Wat kost een nieuwe groepenkast?",
             "Dat hangt af van het aantal groepen en wat er verder moet gebeuren. U krijgt eerst een offerte met een vaste prijs."),
        ],
    },
    # ------------------------------------------------------ GROEP BIJPLAATSEN
    {
        "slug": "groep-bijplaatsen-rotterdam",
        "short": "Groep bijplaatsen",
        "sub": "Extra groep voor wasmachine, droger, oven of airco.",
        "title": "Groep bijplaatsen Rotterdam | Extra groep | AlleKlussers",
        "desc": "Slaat een groep door als de wasmachine en droger tegelijk draaien? Wij plaatsen een extra groep in uw meterkast in Rotterdam. Volgens NEN 1010, prijs vooraf.",
        "service": "Extra groep bijplaatsen in de meterkast",
        "char": "stekkie",
        "say": "“Eén groep te weinig? Ik zet er een bij.”",
        "eyebrow": "Extra groep in de meterkast",
        "h1": "Groep bijplaatsen in <em>Rotterdam.</em>",
        "lede": "Slaat de stroom uit zodra de wasmachine en de droger samen draaien? Dan zitten er te veel apparaten op één groep. Met een extra groep in de meterkast is dat meestal snel opgelost.",
        "body": """
<h2>Waarom een groep <em>doorslaat.</em></h2>
<p>Een gewone groep in de meterkast is beveiligd met 16 ampère. Op 230 volt is dat samen ongeveer 3.680 watt. Een wasmachine die het water opwarmt, een droger, een vaatwasser of een oven vraagt elk al snel 2.000 watt of meer. Staan er twee van deze apparaten op dezelfde groep en draaien ze tegelijk, dan schakelt de installatieautomaat uit. Dat is geen defect, maar bescherming: zo wordt de bedrading niet te warm.</p>
<p>Gebruikt u voor zulke apparaten een stekkerdoos of verlengsnoer, of wordt een stopcontact of stekker warm? Dat is een teken dat de groep zwaarder wordt belast dan goed is. Slaat juist de aardlekschakelaar door, dan is er vaak iets anders aan de hand; lees dan eerst <a href="/aardlekschakelaar-rotterdam/">aardlek slaat door</a>.</p>

<h2>Welke apparaten <em>een eigen groep krijgen.</em></h2>
<ul class="checks">
  <li>{check}<span><strong>Wasmachine, droger en vaatwasser:</strong> elk op een eigen groep, zodat u ze tegelijk kunt gebruiken.</span></li>
  <li>{check}<span><strong>Oven of combimagnetron</strong> die ingebouwd is: een eigen groep, los van de kookplaat.</span></li>
  <li>{check}<span><strong>Inductiekookplaat:</strong> meestal een kookgroep met perilex-aansluiting op twee fasen. Zie <a href="/inductiekookplaat-aansluiten-rotterdam/">inductiekookplaat aansluiten</a>.</span></li>
  <li>{check}<span><strong>Airco of warmtepomp:</strong> een eigen groep, zodat de rest van het huis niet uitvalt als het apparaat opstart.</span></li>
  <li>{check}<span><strong>Infraroodpanelen:</strong> verwarming die urenlang aanstaat. Eén klein paneel past vaak op een bestaande groep, meerdere panelen krijgen liever een eigen groep. Zie <a href="/infraroodpanelen-aansluiten-rotterdam/">infraroodpanelen aansluiten</a>.</span></li>
  <li>{check}<span><strong><a href="/laadpaal-installeren-rotterdam/">Laadpaal</a>:</strong> altijd een eigen groep met de juiste aardlekbeveiliging.</span></li>
  <li>{check}<span><strong>Stekkerbatterij:</strong> een vrije groep waar alleen de batterij op zit. Zie <a href="/vrije-groep-stekkerbatterij-rotterdam/">vrije groep voor stekkerbatterij</a>.</span></li>
  <li>{check}<span><strong>Nieuwe ruimte:</strong> een aanbouw, zolderkamer of tuinhuis krijgt eigen groepen, en niet ‘nog een stopcontact erbij’ op een groep die al vol zit.</span></li>
</ul>

<h2>Is er ruimte <em>in uw groepenkast?</em></h2>
<p>Volgens NEN 1010 horen er maximaal vier groepen achter één aardlekschakelaar. Of een extra groep zo bij te plaatsen is, hangt dus af van wat er nu in uw kast zit:</p>
<ul class="checks">
  <li>{check}<span><strong>Vrije plek achter een aardlekschakelaar met minder dan vier groepen:</strong> dan kan er vaak gewoon een installatieautomaat bij.</span></li>
  <li>{check}<span><strong>Alle aardlekschakelaars hebben al vier groepen:</strong> dan plaatsen we een aardlekautomaat. Die combineert de aardlekbeveiliging en de automaat in één, voor die ene groep. Valt hij uit, dan blijft de rest van het huis gewoon aan.</span></li>
  <li>{check}<span><strong>De kast is vol:</strong> dan kan hij soms worden uitgebreid met een extra rij of een kleine kast ernaast.</span></li>
  <li>{check}<span><strong>Oude kast met draaistoppen of zonder aardlekschakelaar:</strong> dan raden we af om er nog iets bij te bouwen. <a href="/groepenkast-vervangen-rotterdam/">Vervangen</a> is dan veiliger en vaak ook verstandiger.</span></li>
</ul>
<p>In oudere Rotterdamse woningen, zoals portiekflats en vooroorlogse benedenwoningen, is de groepenkast vaak klein en zitten er soms maar een paar groepen in. Stuur ons een foto, dan ziet u vooraf welke van de vier situaties het is.</p>

<div class="note-box"><p><strong>Een extra groep geeft geen extra vermogen.</strong> Een nieuwe groep verdeelt de stroom beter over uw installatie, maar wat u in totaal tegelijk kunt gebruiken blijft bepaald door de hoofdzekering van de netbeheerder, bijvoorbeeld 1x35A. Komen er meerdere zware apparaten bij, zoals een warmtepomp en een laadpaal? Lees dan ook <a href="/meterkast-verzwaren-rotterdam/">meterkast verzwaren</a>.</p></div>

<h2>Zo <em>pakken we het aan.</em></h2>
<ol class="steps-list">
  <li><strong>Stuur een foto</strong> van uw open meterkast via WhatsApp en vertel voor welk apparaat de groep is en waar het staat.</li>
  <li><strong>U krijgt een duidelijke prijs vooraf,</strong> met daarin de groep zelf, de kabel naar de plek en eventueel een nieuw stopcontact.</li>
  <li><strong>Wij plaatsen de groep</strong> en trekken een nieuwe leiding naar de plek van het apparaat, waar het kan door bestaande buizen. Kan dat niet, dan bespreken we vooraf hoe de kabel loopt.</li>
  <li><strong>We testen de groep en de aardlekbeveiliging,</strong> zetten op de kast waar de nieuwe groep voor is en laten zien welke schakelaar bij welk apparaat hoort.</li>
</ol>
<p>Alles volgens NEN 1010, door verzekerde vakmensen. De stroom is tijdens het werk een korte tijd uit; dat stemmen we vooraf met u af.</p>
""",
        "faq": [
            ("Hoeveel watt kan er op één groep?",
             "Op een gewone groep van 16 ampère kunt u samen ongeveer 3.680 watt tegelijk gebruiken. Een wasmachine die verwarmt en een droger halen dat samen al snel. Daarom krijgen zware apparaten elk een eigen groep."),
            ("Mogen de wasmachine en de droger op dezelfde groep?",
             "Het kan als u ze nooit tegelijk gebruikt, maar dan slaat de groep door zodra dat toch gebeurt. Met een eigen groep voor elk apparaat hoeft u daar niet meer op te letten."),
            ("Hoeveel groepen mogen er achter één aardlekschakelaar?",
             "Maximaal vier. Zitten alle aardlekschakelaars in uw kast al vol, dan plaatsen we voor de nieuwe groep een aardlekautomaat, of breiden we de kast uit."),
            ("Wat is het verschil tussen een installatieautomaat en een aardlekautomaat?",
             "Een installatieautomaat beschermt tegen overbelasting en kortsluiting. Een aardlekautomaat doet dat ook, en beschermt daarnaast tegen lekstroom. Hij heeft dus geen aparte aardlekschakelaar nodig en schakelt alleen zijn eigen groep uit."),
            ("Hoe lang duurt het bijplaatsen van een groep?",
             "Is er ruimte in de kast en is de kabel kort, dan is het meestal binnen een paar uur klaar. Moet er een lange nieuwe leiding komen, bijvoorbeeld naar de zolder of de schuur, dan kan het een dagdeel tot een dag duren."),
            ("Mag ik zelf een groep bijplaatsen?",
             "Wij raden het af. Ook als de hoofdschakelaar uit staat, blijft een deel van de meterkast onder spanning. Een verkeerd aangesloten groep of te dunne kabel merkt u vaak pas als er iets misgaat."),
            ("Ik huur mijn woning. Kan ik een extra groep laten plaatsen?",
             "Vraag eerst toestemming aan uw verhuurder, want de groepenkast hoort bij de woning. Verhuurders en VvE's helpen we ook rechtstreeks."),
            ("Wat kost een extra groep?",
             "Dat hangt af van de ruimte in uw kast en hoe ver de kabel moet. Stuur een foto van uw meterkast, dan krijgt u vooraf een duidelijke prijs."),
        ],
    },
    # ---------------------------------------------------------- INDUCTIE
    {
        "slug": "inductiekookplaat-aansluiten-rotterdam",
        "short": "Inductiekookplaat aansluiten",
        "sub": "Kookgroep en perilex, ook bij de overstap van gas.",
        "title": "Inductiekookplaat aansluiten Rotterdam | Kookgroep | AlleKlussers",
        "desc": "Inductiekookplaat aansluiten in Rotterdam: extra kookgroep in de meterkast, perilex-aansluiting in de keuken en veilig aansluiten. Prijs vooraf via WhatsApp.",
        "service": "Inductiekookplaat aansluiten en kookgroep plaatsen",
        "char": "vonk",
        "say": "“Van gas naar inductie? Ik regel de stroom.”",
        "eyebrow": "Inductie koken",
        "h1": "Inductiekookplaat aansluiten in <em>Rotterdam.</em>",
        "lede": "Een inductiekookplaat vraagt meer stroom dan een gewoon stopcontact kan leveren. Wij kijken wat uw meterkast aankan, leggen zo nodig een kookgroep aan en sluiten de kookplaat veilig aan.",
        "body": """
<h2>Welke aansluiting heeft <em>uw kookplaat nodig?</em></h2>
<p>Kijk niet naar het aantal kookzones, maar naar het aansluitvermogen in de handleiding of op het typeplaatje. Een groep in de meterkast levert 230 volt bij 16 ampère, dus maximaal 3.680 watt. Daaruit volgen drie soorten aansluitingen:</p>
<ul class="checks">
  <li>{check}<span><strong>1-fase, tot 3.680 watt.</strong> Er zijn kleinere inductiekookplaten met een gewone stekker voor een geaard stopcontact. Ze zijn minder krachtig: u kunt bijvoorbeeld niet op alle zones tegelijk de boostfunctie gebruiken. Geef zo'n kookplaat een eigen groep; deelt hij een groep met de waterkoker of vaatwasser, dan slaat de groep door zodra die tegelijk aanstaan.</span></li>
  <li>{check}<span><strong>2-fase met perilex, tot 7.360 watt.</strong> Dit is de gewone aansluiting voor een inductiekookplaat. In de meterkast zit dan een kookgroep: twee gekoppelde groepen met één hendel. In de keuken zit een rond perilex-stopcontact met vijf gaatjes. De meeste kookplaten werken hierop, ook als ze vijf zones hebben: de kookplaat verdeelt het vermogen zelf.</span></li>
  <li>{check}<span><strong>3-fase krachtstroom, circa 11.000 watt.</strong> Alleen nodig voor sommige grote kookplaten en fornuizen. Kan uw kookplaat ook op twee fasen, dan is dat meestal de eenvoudigste keuze. Meer over het verschil leest u bij <a href="/krachtstroom-aansluiten-rotterdam/">krachtstroom aansluiten</a>.</span></li>
</ul>

<h2>Inductie aansluiten op uw meterkast: <em>wat zit er nu?</em></h2>
<ul class="checks">
  <li>{check}<span><strong>Een dubbele schakelaar met één hendel</strong> en een rond stopcontact met vijf gaatjes in de keuken: u heeft al een kookgroep. Dan is aansluiten vaak alleen de kookplaat monteren, een perilex-stekker aan het snoer zetten en testen.</span></li>
  <li>{check}<span><strong>Geen kookgroep,</strong> wat vaak voorkomt in woningen waar altijd op gas is gekookt: dan plaatsen we een kookgroep in de groepenkast en trekken we een nieuwe kabel naar de keuken.</span></li>
  <li>{check}<span><strong>Een volle of oude groepenkast,</strong> met draaistoppen of zonder plek voor een extra groep: dan moet de kast eerst worden <a href="/groepenkast-vervangen-rotterdam/">uitgebreid of vervangen</a>.</span></li>
</ul>
<p>Stuur ons een foto van uw meterkast en het typeplaatje of de productpagina van uw kookplaat. Dan zien we meestal al wat er nodig is.</p>

<h2>Extra groep voor inductie: <em>kookgroep en perilex.</em></h2>
<p>Een "extra groep voor inductie" is bijna altijd een kookgroep: twee groepen van 16 ampère die samen met één hendel schakelen, beveiligd door een aardlekschakelaar. Vanuit die kookgroep loopt een eigen kabel naar de keuken, waar een perilex-wandcontactdoos komt. Daar gaat de stekker van de kookplaat in.</p>
<ul class="checks">
  <li>{check}<span><strong>Kookgroep in de meterkast.</strong> Is er plek in de groepenkast, dan plaatsen we de kookgroep erbij. Zitten er al vier groepen aan dezelfde aardlekschakelaar, dan komt er een aardlekschakelaar bij of gebruiken we aardlekautomaten. Is de kast vol of verouderd, dan leest u meer bij <a href="/groep-bijplaatsen-rotterdam/">groep bijplaatsen</a>.</span></li>
  <li>{check}<span><strong>Perilex in de keuken.</strong> De perilex-wandcontactdoos komt achter of onder de kookplaat, op een plek die u na het monteren nog kunt bereiken.</span></li>
  <li>{check}<span><strong>Ook op 1-fase.</strong> Een kookgroep met perilex werkt op twee groepen van dezelfde 1-fase aansluiting. Krachtstroom is daarvoor niet nodig.</span></li>
</ul>
<p>Ligt er al een perilex-aansluiting van een oud elektrisch fornuis? Dan controleren we of de kabel en de groep in orde zijn; vaak kan de nieuwe kookplaat er dan direct op. Moet de perilex naar een andere plek, bijvoorbeeld in een kookeiland, of wilt u weten wat er achter uw perilex zit? Lees <a href="/perilex-aansluiten-rotterdam/">perilex aansluiten en verplaatsen</a>.</p>

<h2>Moet uw aansluiting <em>verzwaard worden?</em></h2>
<p>Meestal niet. Met een 3x25A-aansluiting past een kookgroep voor inductie gewoon. In de regio Rotterdam hebben veel woningen nog 1-fase, vaak 1x35A; ook dan past inductie meestal, want de kookplaat verdeelt het vermogen zelf. Heeft u een 1-fase aansluiting, dan kijken we of er naast de kookplaat genoeg ruimte overblijft voor de rest van het huis, zeker als er ook een warmtepomp of <a href="/laadpaal-installeren-rotterdam/">laadpaal</a> bij komt.</p>
<div class="note-box"><p><strong>Niet uit voorzorg verzwaren.</strong> Een zwaardere aansluiting vraagt u aan bij de netbeheerder; in Rotterdam is dat Stedin. Het stroomnet is op veel plekken vol en sinds 1 juli 2026 gaan alle aanvragen in één wachtrij, dus het kan lang duren. Laat daarom eerst uitrekenen of het echt nodig is. Lees meer over <a href="/meterkast-verzwaren-rotterdam/">meterkast verzwaren</a>.</p></div>

<h2>Van gas <em>naar inductie.</em></h2>
<ul class="checks">
  <li>{check}<span><strong>Wij regelen de elektra:</strong> de kookgroep in de meterkast met de juiste aardlekbeveiliging, de kabel naar de keuken, de perilex-aansluiting en het aansluiten van de kookplaat.</span></li>
  <li>{check}<span><strong>De gasleiding doen wij niet.</strong> Het afkoppelen en afdoppen van de gasaansluiting laat u doen door een gasinstallateur.</span></li>
  <li>{check}<span><strong>Denk aan uw pannen.</strong> Inductie werkt alleen met pannen met een magnetische bodem. Blijft een magneet aan de onderkant hangen, dan is de pan geschikt.</span></li>
  <li>{check}<span><strong>Oven en vaatwasser apart.</strong> Een inbouwoven, combimagnetron of vaatwasser in dezelfde keuken krijgt liefst een eigen gewone groep, los van de kookgroep. Ontbreken die stopcontacten, dan <a href="/stopcontact-plaatsen-rotterdam/">plaatsen we ze</a> in dezelfde ronde.</span></li>
</ul>

<h2>Wat wij <em>doen.</em></h2>
<ol class="steps-list">
  <li><strong>Meterkast en kookplaat beoordelen</strong> aan de hand van uw foto's, zodat u vooraf een duidelijke prijs krijgt.</li>
  <li><strong>Kookgroep plaatsen</strong> in de groepenkast, met aardlekbeveiliging, en de groep duidelijk labelen.</li>
  <li><strong>Kabel trekken</strong> van de meterkast naar de keuken en een perilex-wandcontactdoos monteren op de plek van de kookplaat.</li>
  <li><strong>Kookplaat aansluiten en testen.</strong> We zetten de perilex-stekker aan het aansluitsnoer, sluiten aan zoals de fabrikant voorschrijft en testen alle zones.</li>
</ol>
<p>Alles volgens NEN 1010, door verzekerde vakmensen. Een perilex-stekker zelf aansluiten raden we af: een draad op de verkeerde klem kan de kookplaat beschadigen.</p>
""",
        "faq": [
            ("Kan ik een inductiekookplaat op een gewoon stopcontact aansluiten?",
             "Alleen als het een 1-fase kookplaat is met een aansluitvermogen tot 3.680 watt en een gewone stekker. Geef hem dan een eigen groep, zodat de groep niet doorslaat als ook de waterkoker of vaatwasser aanstaat. De meeste inductiekookplaten hebben een perilex-aansluiting op twee fasen nodig."),
            ("Wat is een perilex-aansluiting?",
             "Een rond stopcontact met vijf gaatjes voor zware keukenapparatuur. Het hoort bij een kookgroep in de meterkast: twee gekoppelde groepen met één hendel, samen goed voor 7.360 watt."),
            ("Heb ik krachtstroom nodig voor inductie?",
             "Meestal niet. Krachtstroom (3-fase) is alleen nodig voor sommige grote kookplaten en fornuizen. Kan uw kookplaat ook op twee fasen worden aangesloten, dan is een gewone kookgroep vaak genoeg."),
            ("Moet ik mijn aansluiting bij Stedin laten verzwaren?",
             "In de meeste gevallen niet. Met een 3x25A-aansluiting past een kookgroep gewoon. Bij een 1-fase aansluiting of als er ook een warmtepomp of laadpaal komt, rekenen we eerst uit of het nodig is voordat u iets aanvraagt."),
            ("Koppelen jullie ook de gaskraan af?",
             "Nee, wij doen alleen elektra. Het afkoppelen en afdoppen van de gasleiding laat u doen door een gasinstallateur. Wij zorgen dat de elektrische aansluiting klaar is voor uw nieuwe kookplaat."),
            ("Moet de keuken open voor een nieuwe kabel?",
             "Niet altijd. Vaak kan de kabel via bestaande leidingen of langs een verborgen route. Kan dat niet, dan bespreken we vooraf met u hoe en waar de kabel komt."),
            ("Wat kost het aansluiten van een inductiekookplaat?",
             "Dat hangt af van wat er al is. Met een bestaande kookgroep is het een kleine klus; moet er een groep en een nieuwe kabel bij, dan is het meer werk. Stuur een foto van uw meterkast, dan krijgt u vooraf een duidelijke prijs."),
        ],
    },
    # ---------------------------------------------------------- PERILEX
    {
        "slug": "perilex-aansluiten-rotterdam",
        "short": "Perilex aansluiten",
        "sub": "Perilex plaatsen, verplaatsen of een stekker aan de kookplaat.",
        "title": "Perilex aansluiten of verplaatsen Rotterdam | AlleKlussers",
        "desc": "Perilex aansluiten in Rotterdam: nieuw perilex-stopcontact, verplaatsen bij een nieuwe keuken of kookeiland, stekker aan de kookplaat. Prijs vooraf.",
        "service": "Perilex-aansluiting plaatsen, verplaatsen en aansluiten",
        "char": "dosie",
        "say": "“Vijf gaatjes, één goede aansluiting.”",
        "eyebrow": "Perilex",
        "h1": "Perilex aansluiten in <em>Rotterdam.</em>",
        "lede": "Een nieuw perilex-stopcontact, een perilex die mee moet naar de nieuwe plek van uw kookplaat, of een kookplaat zonder stekker? Wij kijken eerst wat er achter uw perilex zit, en sluiten alles veilig aan.",
        "body": """
<h2>Wat is <em>perilex?</em></h2>
<p>Perilex is het ronde stopcontact met vijf gaatjes dat u in de keuken ziet, met de bijpassende stekker. Het systeem bestaat sinds 1951 en werd in de jaren zestig gewoon, toen elektrische fornuizen opkwamen. Het wordt vooral in Nederland, Duitsland en Zweden gebruikt. In woningen gaat het vrijwel altijd om de uitvoering van 16 ampère (Wikipedia).</p>
<p>De vijf polen zijn: één aarde in het midden, en daaromheen fasen en nul. Welke daarvan echt stroom krijgen, hangt af van hoe de groep in de meterkast is aangelegd. Van buiten zien twee perilex-stopcontacten er dus hetzelfde uit, terwijl er iets heel anders achter kan zitten.</p>

<h2>Wat zit er achter <em>uw perilex?</em></h2>
<ul class="checks">
  <li>{check}<span><strong>Kookgroep op één fase (2-fase perilex).</strong> Het meest voorkomend. In de meterkast zitten twee groepen van 16 ampère met één hendel. Elke groep heeft zijn eigen fase- en nuldraad naar de perilex (GAMMA). Samen goed voor ongeveer 7.400 watt, genoeg voor de meeste inductiekookplaten met vier zones (Consumentenbond). Dit kan gewoon op een 1-fase aansluiting.</span></li>
  <li>{check}<span><strong>Kookgroep op twee verschillende fasen.</strong> Hetzelfde idee, maar de twee groepen zitten op twee fasen van een 3-fase aansluiting. Voor de kookplaat werkt het hetzelfde; voor de meterkast wordt de belasting beter verdeeld.</span></li>
  <li>{check}<span><strong>3-fase perilex.</strong> Drie fasen en één nul, met 400 volt tussen de fasen. Fabrikanten adviseren dit meestal bij een kookplaat van 7.600 watt of meer, bij kookplaten met ingebouwde afzuiging (downdraft) en bij sommige kookplaten met vijf of meer zones (Consumentenbond). Zie ook <a href="/krachtstroom-aansluiten-rotterdam/">krachtstroom aansluiten</a>.</span></li>
</ul>
<p>Wij meten dat na voordat er iets wordt aangesloten. Bij een 2-fase perilex staat op twee polen spanning, bij een 3-fase perilex op drie, met 400 volt tussen twee fasen (Coolblue). Ook kijken we in de meterkast welke groep erbij hoort en of er een <a href="/aardlekschakelaar-rotterdam/">aardlekschakelaar</a> voor zit.</p>
<div class="note-box"><p><strong>Waarom dit belangrijk is.</strong> In de aansluitdoos van een kookplaat zitten bruggetjes die bepalen of hij op één, twee of drie fasen werkt. Past dat niet bij wat er in de muur zit, dan werkt de kookplaat maar half, helemaal niet, of slaan de stoppen door (Coolblue). Laat de stekker daarom aansluiten door iemand die eerst meet.</p></div>

<h2>Nieuwe perilex <em>plaatsen.</em></h2>
<p>Kookt u nu op gas, of heeft u alleen gewone stopcontacten in de keuken? Dan is er nog geen perilex. Een perilex-stopcontact is alleen veilig met een eigen kookgroep erachter:</p>
<ul class="checks">
  <li>{check}<span><strong>Kookgroep in de meterkast,</strong> beveiligd door een aardlekschakelaar. Is uw kast vol of oud, dan leest u bij <a href="/groep-bijplaatsen-rotterdam/">groep bijplaatsen</a> wat de mogelijkheden zijn.</span></li>
  <li>{check}<span><strong>Een eigen kabel naar de keuken.</strong> De perilex hoort op zijn eigen kookgroep, niet op een groep die ook andere stopcontacten voedt.</span></li>
  <li>{check}<span><strong>Inbouw of opbouw.</strong> In een gemetselde of gestucte muur werken we het liefst in. In een flat met betonnen muren, of in een keukenkastje, kan een opbouwdoos de beste keuze zijn.</span></li>
</ul>
<p>Gaat het om een inductiekookplaat, dan staat op <a href="/inductiekookplaat-aansluiten-rotterdam/">inductiekookplaat aansluiten</a> welke kookplaat welke aansluiting vraagt en of u moet verzwaren.</p>

<h2>Perilex verplaatsen <em>bij een nieuwe keuken.</em></h2>
<p>Bij een nieuwe keuken komt de kookplaat vaak op een andere plek: aan de andere muur, op een schiereiland of in een kookeiland. De perilex moet dan mee. Plan dit vóór de keukenmonteur komt, want als de kasten staan, kun je er slecht meer bij.</p>
<ul class="checks">
  <li>{check}<span><strong>Waar komt hij?</strong> In of achter het onderkastje onder de kookplaat, op een plek die u na het monteren nog kunt bereiken. Het aansluitsnoer van de kookplaat moet er zonder trekken bij kunnen.</span></li>
  <li>{check}<span><strong>Kookeiland of schiereiland.</strong> Dan moet de kabel door of over de vloer naar het eiland. Ligt er een nieuwe vloer, dan leggen we een buis mee voordat die dicht gaat. Op een betonvloer, zoals in veel Rotterdamse flats, zoeken we samen met u en de keukenmonteur de beste route, bijvoorbeeld via de plint of de kastjes.</span></li>
  <li>{check}<span><strong>Geen verborgen lassen.</strong> Moet de kabel langer worden, dan maken we de verbinding in een las- of inbouwdoos die bereikbaar blijft, of trekken we een nieuwe kabel vanaf de meterkast.</span></li>
  <li>{check}<span><strong>De oude plek.</strong> Een perilex die niet meer nodig is, halen we weg of maken we veilig dood. Er blijft geen kabel onder spanning achter in een dichte muur.</span></li>
</ul>
<p>Een verlengsnoer of koppelstuk achter de keukenkastjes om het snoer van de kookplaat langer te maken raden we af. Bij een apparaat dat urenlang veel stroom trekt, is elke extra verbinding een plek die warm kan worden.</p>

<h2>Kookplaat zonder <em>stekker?</em></h2>
<p>Inbouwkookplaten met vier of meer zones worden meestal geleverd zonder snoer en stekker (Consumentenbond). De perilex-stekker koopt u apart, of wij nemen hem mee. Wij zetten de stekker aan het aansluitsnoer, stellen de bruggetjes in de kookplaat in volgens de handleiding en passend bij uw perilex, en testen daarna alle zones. Heeft uw kookplaat geen snoer, dan monteren we een passend aansluitsnoer.</p>

<h2>Perilex is niet <em>voor machines.</em></h2>
<p>Perilex is gemaakt voor vaste keukenapparaten zoals een kookplaat of fornuis. Voor een compressor, zaagmachine of ander apparaat met een 3-fase motor is het geen goede keuze: de volgorde van de fasen is bij perilex niet eenduidig, en dan kan een motor de verkeerde kant op draaien (Wikipedia). Daarvoor gebruiken we een CEE-krachtstroomcontactdoos. Lees meer bij <a href="/krachtstroom-aansluiten-rotterdam/">krachtstroom aansluiten</a>.</p>

<h2>Oude perilex, <em>oude kookgroep.</em></h2>
<p>In veel oudere Rotterdamse woningen zit nog een perilex van een elektrisch fornuis van jaren geleden. Die kan vaak prima blijven, maar we kijken eerst:</p>
<ul class="checks">
  <li>{check}<span><strong>Is het stopcontact of de stekker verkleurd,</strong> wordt hij warm of zit hij los? Gebruik hem dan niet meer en stuur ons een foto.</span></li>
  <li>{check}<span><strong>Zit er een aardlekschakelaar voor de kookgroep?</strong> In kasten van vóór 1975 is die er bijna nooit. Dan komt die er eerst bij, of wordt de <a href="/groepenkast-vervangen-rotterdam/">groepenkast vervangen</a>.</span></li>
  <li>{check}<span><strong>Is de kabel dik genoeg en heel?</strong> Een nieuwe kookplaat kan meer vermogen vragen dan het oude fornuis.</span></li>
</ul>

<h2>Wat wij <em>doen.</em></h2>
<ol class="steps-list">
  <li><strong>U stuurt foto's</strong> via WhatsApp: van de meterkast, de perilex of de plek in de keuken, en het typeplaatje of de productpagina van de kookplaat.</li>
  <li><strong>U krijgt vooraf een duidelijke prijs,</strong> met wat er nodig is: alleen de stekker, een nieuwe of verplaatste perilex, of ook een kookgroep.</li>
  <li><strong>We meten en sluiten aan:</strong> kookgroep en kabel waar nodig, de perilex op de goede plek, de stekker aan de kookplaat.</li>
  <li><strong>We testen</strong> de aardlekschakelaar en alle kookzones, en labelen de groep in de meterkast.</li>
</ol>
<p>Alles volgens NEN 1010, door verzekerde vakmensen. Huurt u de woning? Vraag voor een nieuwe of verplaatste perilex eerst toestemming aan de verhuurder; met <a href="/elektricien-verhuurders-vve-rotterdam/">verhuurders en VvE's</a> werken we ook rechtstreeks.</p>
<div class="note-box"><p><strong>Bronnen:</strong> Wikipedia, <a href="https://en.wikipedia.org/wiki/Perilex" target="_blank" rel="noopener noreferrer">Perilex</a>; GAMMA klusadvies, <a href="https://www.gamma.nl/klusadvies/a/elektriciteit-aanleggen/stappenplan/perilex-aansluiten" target="_blank" rel="noopener noreferrer">perilex aansluiten</a>; Consumentenbond, <a href="https://www.consumentenbond.nl/inductiekookplaat/inductiekookplaat-aansluiten" target="_blank" rel="noopener noreferrer">inductiekookplaat aansluiten</a>; Coolblue, <a href="https://www.coolblue.nl/advies/aansluiting-elektrische-kookplaat.html" target="_blank" rel="noopener noreferrer">aansluiting voor een elektrische kookplaat</a> en <a href="https://www.coolblue.nl/advies/hoe-meet-ik-een-perilex-stopcontact-met-een-multimeter.html" target="_blank" rel="noopener noreferrer">een perilex-stopcontact meten</a>.</p></div>
""",
        "faq": [
            ("Wat is het verschil tussen perilex en krachtstroom?",
             "Perilex is een stekkervorm met vijf polen. Hoeveel fasen erop zitten, hangt af van de groep erachter. In een woning is het meestal een kookgroep met twee groepen van 16 ampère. Bij krachtstroom zitten er drie fasen op, met 400 volt tussen de fasen."),
            ("Kan ik een 2-fase kookplaat op een 3-fase perilex aansluiten?",
             "Meestal wel, als de aansluiting in de kookplaat volgens de handleiding wordt ingesteld en past bij wat er in de muur zit. Wij meten de perilex eerst na en stellen de kookplaat daarop in."),
            ("Kan ik een perilex-stekker zelf aansluiten?",
             "Dat raden we af. De bruggetjes in de kookplaat moeten precies passen bij de perilex; een draad op de verkeerde klem kan de kookplaat beschadigen of de groep laten doorslaan."),
            ("Waar komt de perilex bij een nieuwe keuken?",
             "In of achter het onderkastje onder de kookplaat, op een plek die u na het monteren nog kunt bereiken. Plan het verplaatsen vóór de keuken wordt geplaatst."),
            ("Kan er een perilex in een kookeiland?",
             "Ja. De kabel moet dan door of over de vloer naar het eiland. Bij een nieuwe vloer leggen we vooraf een buis mee; op een betonvloer zoeken we samen met u en de keukenmonteur een route."),
            ("Mag ik het snoer van mijn kookplaat verlengen?",
             "Liever niet met een verlengsnoer of koppelstuk achter de kastjes. Beter is de perilex dichter bij de kookplaat te plaatsen, of een langer aansluitsnoer te monteren."),
            ("Mijn perilex-stekker wordt warm of is verkleurd. Wat nu?",
             "Gebruik de kookplaat niet meer en zet de kookgroep in de meterkast uit. Stuur een foto via WhatsApp; meestal is een stekker of contactdoos aan vervanging toe, of zit er een draad los."),
            ("Kan een perilex op een 1-fase aansluiting?",
             "Ja. Een kookgroep met twee groepen van 16 ampère werkt gewoon op een 1-fase aansluiting. Voor een 3-fase perilex heeft u wel een 3-fase aansluiting nodig."),
            ("Wat kost een perilex aansluiten?",
             "Dat hangt af van wat er al is. Alleen een stekker aan de kookplaat is een kleine klus; een nieuwe kookgroep met kabel is meer werk. Stuur foto's van de meterkast en de keuken, dan krijgt u vooraf een duidelijke prijs."),
        ],
    },
    # ------------------------------------------------------- VERZWAREN
    {
        "slug": "meterkast-verzwaren-rotterdam",
        "short": "Meterkast verzwaren",
        "sub": "Van 1-fase naar 3-fase, of slim op uw huidige aansluiting.",
        "title": "Meterkast verzwaren Rotterdam | 1-fase naar 3-fase | AlleKlussers",
        "desc": "Aansluiting verzwaren in Rotterdam? Eerst kijken of het nodig is. Wij maken uw meterkast klaar voor 3-fase of zorgen dat alles past op uw huidige aansluiting.",
        "service": "Meterkast verzwaren en geschikt maken voor 3-fase",
        "char": "kastje",
        "say": "“Eerst rekenen, dan pas verzwaren.”",
        "eyebrow": "Meterkast verzwaren",
        "h1": "Meterkast verzwaren in <em>Rotterdam.</em>",
        "lede": "Warmtepomp, inductie of een laadpaal op komst? Dan vraagt u zich af of uw aansluiting zwaarder moet. Wij rekenen eerst uit wat u nodig heeft, en maken uw meterkast klaar als verzwaren echt nodig is.",
        "body": """
<h2>Welke aansluiting <em>heeft u nu?</em></h2>
<p>In uw meterkast zitten vóór de meter de verzegelde hoofdzekeringen van de netbeheerder. Ziet u er één, dan heeft u een 1-fase aansluiting; zijn het er drie, dan heeft u 3-fase. Het getal erop is het aantal ampère. Staat het er niet duidelijk op, kijk dan op de jaarafrekening van uw energieleverancier, of stuur ons een foto.</p>
<ul class="checks">
  <li>{check}<span><strong>1x25A:</strong> circa 5,7 kW tegelijk.</span></li>
  <li>{check}<span><strong>1x35A:</strong> circa 8 kW tegelijk, zo'n 40% meer dan 1x25A.</span></li>
  <li>{check}<span><strong>3x25A:</strong> circa 17,3 kW tegelijk. Dit is de standaard bij nieuwbouw.</span></li>
</ul>
<p>In het gebied van Stedin, waar Rotterdam onder valt, was in 2024 nog ongeveer 71% van de aansluitingen 1-fase, en 1x35A komt daarbij veel vaker voor dan 1x25A. Een 1-fase meterkast is hier dus heel gewoon.</p>

<h2>Is verzwaren <em>wel nodig?</em></h2>
<p>Vaak niet. Volgens een overzicht van RVO voor het ministerie van Economische Zaken en Klimaat (september 2026) is 1x35A voor veel huishoudens genoeg om vergaand elektrisch te gaan, zonder direct over te stappen op 3-fase. Wat telt is niet wat u in huis heeft, maar wat er <strong>tegelijk</strong> aanstaat:</p>
<ul class="checks">
  <li>{check}<span><strong><a href="/inductiekookplaat-aansluiten-rotterdam/">Inductiekookplaat</a>:</strong> meestal 2 tot 4 kW in gebruik. De kookplaat verdeelt het vermogen zelf over de zones.</span></li>
  <li>{check}<span><strong>Hybride warmtepomp:</strong> rond 1,5 kW, op een eigen groep.</span></li>
  <li>{check}<span><strong>Volledig elektrische warmtepomp:</strong> rond 3 kW, bij strenge kou 2 tot 4 kW. Een eventueel elektrisch bijverwarmingselement vraagt flink meer en zit vaak op een eigen groep.</span></li>
  <li>{check}<span><strong><a href="/laadpaal-installeren-rotterdam/">Laadpaal</a> op 1-fase:</strong> maximaal 3,7 kW. In tien uur laadt u zo hooguit 37 kWh, genoeg voor de meeste dagelijkse ritten.</span></li>
</ul>
<p>Op 1x35A passen deze apparaten samen vaak, als de laadpaal en eventueel de warmtepomp terugschakelen wanneer het huis veel stroom vraagt. Op 1x25A is dat bij inductie, een warmtepomp én een elektrische auto meestal alleen haalbaar met zo'n slimme begrenzing.</p>

<h2>Wanneer 3-fase <em>wel verstandig is.</em></h2>
<ul class="checks">
  <li>{check}<span><strong>U wilt snel laden met 11 kW.</strong> Dat kan alleen op drie fasen.</span></li>
  <li>{check}<span><strong>Uw kookplaat, warmtepomp of ander apparaat</strong> is alleen in een 3-fase uitvoering te krijgen, of u wilt <a href="/krachtstroom-aansluiten-rotterdam/">krachtstroom</a> voor een machine of sauna.</span></li>
  <li>{check}<span><strong>Er draaien vaak meerdere zware apparaten tegelijk</strong> en terugschakelen is geen optie, bijvoorbeeld bij een groot gezin met twee elektrische auto's.</span></li>
  <li>{check}<span><strong>Uw groepenkast moet toch al vervangen worden.</strong> Dan is het slim om een kast te kiezen die klaar is voor 3-fase, ook als u nu nog niet verzwaart.</span></li>
</ul>
<p>Van 1-fase naar 3x25A kost eenmalig geld bij de netbeheerder, maar uw vaste netbeheerkosten per jaar blijven in dezelfde categorie. Kiest u voor zwaarder dan 3x25A, zoals 3x35A, dan betaalt u elk jaar flink meer. Daarom adviseren we dat alleen als het echt nodig is.</p>

<div class="note-box"><p><strong>Netcongestie in de regio.</strong> Het stroomnet is op veel plekken vol. Sinds 1 juli 2026 reserveren netbeheerders niet meer automatisch ruimte voor kleinverbruikers: alle aanvragen gaan in één wachtrij, op volgorde van maatschappelijke prioriteit. Volgens Stedin kan een verzwaring in het gunstigste geval maanden duren, maar ook jaren, afhankelijk van uw buurt. Vraag daarom niet uit voorzorg aan, maar laat eerst uitrekenen wat u nodig heeft.</p></div>

<h2>Wie doet <em>wat?</em></h2>
<ul class="checks">
  <li>{check}<span><strong>De netbeheerder</strong> (in Rotterdam is dat Stedin; via mijnaansluiting.nl ziet u wie het bij u is) verzwaart de aansluiting zelf: de kabel, de hoofdzekeringen en zo nodig de meter. U vraagt dat online aan en krijgt eerst een offerte. De netbeheerder geeft geen technisch advies over uw installatie; daarvoor verwijst hij naar een installateur.</span></li>
  <li>{check}<span><strong>Wij doen alles achter de meter.</strong> We controleren of uw groepenkast geschikt is voor 3-fase, plaatsen een 3-fase hoofdschakelaar als die er nog niet is, en <a href="/groepenkast-vervangen-rotterdam/">breiden de groepenkast uit of vervangen hem</a> als hij te oud of te vol is. Dat moet klaar zijn vóór de netbeheerder langskomt.</span></li>
  <li>{check}<span><strong>Groepen verdelen over de fasen.</strong> Na de verzwaring zorgen we dat de zware verbruikers over de drie fasen verdeeld zijn, zodat niet één fase alles draagt. Daarna testen we de hele installatie.</span></li>
</ul>

<h2>Zo <em>pakken we het aan.</em></h2>
<ol class="steps-list">
  <li><strong>Stuur ons foto's</strong> van uw meterkast en vertel welke apparaten erbij komen: warmtepomp, inductie, laadpaal.</li>
  <li><strong>Wij rekenen het door</strong> en vertellen u eerlijk of uw huidige aansluiting genoeg is, eventueel met een extra groep of slimme begrenzing.</li>
  <li><strong>Is verzwaren nodig,</strong> dan vraagt u de verzwaring aan bij de netbeheerder. Wij vertellen u welke aansluiting u nodig heeft, zodat u niet zwaarder aanvraagt dan nodig.</li>
  <li><strong>Wij maken de meterkast klaar</strong> vóór de afspraak met de netbeheerder, met een duidelijke prijs vooraf.</li>
  <li><strong>Na de verzwaring</strong> verdelen we de groepen over de fasen, testen we alles en sluiten we de nieuwe apparaten aan.</li>
</ol>
<p>Alles volgens NEN 1010, door verzekerde vakmensen.</p>
""",
        "faq": [
            ("Hoe zie ik of ik 1-fase of 3-fase heb?",
             "Kijk in de meterkast naar de verzegelde hoofdzekeringen van de netbeheerder, vóór de meter. Eén zekering betekent 1-fase, drie zekeringen betekent 3-fase. Het getal erop is het aantal ampère, bijvoorbeeld 25 of 35. Twijfelt u, stuur ons dan een foto."),
            ("Kan een warmtepomp op een 1-fase aansluiting?",
             "Vaak wel. Een hybride warmtepomp vraagt rond 1,5 kW en een volledig elektrische warmtepomp rond 3 kW. Op 1x35A past dat in de meeste huizen, mits de warmtepomp een eigen groep krijgt. Komt er ook een laadpaal bij, dan is slim terugschakelen verstandig."),
            ("Kan ik een laadpaal gebruiken zonder 3-fase?",
             "Ja. Op 1-fase laadt u met maximaal 3,7 kW, genoeg voor de meeste dagelijkse ritten als de auto 's nachts aan de lader staat. Met loadbalancing laadt de auto langzamer als het huis veel stroom vraagt, zodat de hoofdzekering niet doorslaat. Snelladen met 11 kW kan alleen op 3-fase."),
            ("Wordt mijn netbeheerrekening hoger met 3-fase?",
             "Niet als u naar 3x25A gaat: 1-fase en 3x25A vallen in dezelfde tariefcategorie. U betaalt wel eenmalig voor de verzwaring zelf. Een aansluiting zwaarder dan 3x25A, zoals 3x35A, kost elk jaar duidelijk meer."),
            ("Hoe lang duurt een verzwaring bij Stedin?",
             "Dat verschilt per buurt. Is er ruimte op het net, dan plant de netbeheerder na uw akkoord op de offerte een afspraak. Waar het net vol is, kan het maanden tot jaren duren. Ons deel in de meterkast is meestal binnen een dag klaar."),
            ("Moet mijn groepenkast vervangen worden als ik verzwaar?",
             "Niet altijd. Soms is alleen een 3-fase hoofdschakelaar nodig. Is de kast oud, vol of zonder goede aardlekbeveiliging, dan is vervangen verstandig. Dat ziet u vooraf in onze prijs."),
            ("Ik huur mijn woning. Kan ik zelf laten verzwaren?",
             "Overleg eerst met uw verhuurder. De aansluiting en de groepenkast horen bij de woning, dus voor een verzwaring of nieuwe kast heeft u in de regel toestemming nodig."),
            ("Wat kost het om de meterkast klaar te maken?",
             "Dat hangt af van wat er nu zit. Stuur ons foto's van uw meterkast, dan krijgt u vooraf een duidelijke prijs voor ons deel van het werk."),
        ],
    },
    # ------------------------------------------------------- INFRAROOD
    {
        "slug": "infraroodpanelen-aansluiten-rotterdam",
        "short": "Infraroodpanelen aansluiten",
        "sub": "Vast aansluitpunt op plafond of muur, en een eigen groep als het nodig is.",
        "title": "Infraroodpanelen aansluiten Rotterdam | AlleKlussers",
        "desc": "Infraroodpaneel ophangen en aansluiten in Rotterdam: vast aansluitpunt op plafond of muur, eigen groep als het nodig is, ook in de badkamer. Prijs vooraf.",
        "service": "Infraroodpanelen ophangen en elektrisch aansluiten",
        "char": "stekkie",
        "say": "“Warm, zonder snoer over de muur.”",
        "eyebrow": "Infraroodpanelen",
        "h1": "Infraroodpanelen aansluiten in <em>Rotterdam.</em>",
        "lede": "Een infraroodpaneel op zolder, in de badkamer of in een koude kamer? Wij hangen het op, maken een vast aansluitpunt zonder snoer over de muur, en kijken of uw groep de extra warmte aankan.",
        "body": """
<h2>Bijverwarming of <em>hoofdverwarming?</em></h2>
<p>Een infraroodpaneel verwarmt niet de lucht, maar alles wat de straling raakt: mensen, de vloer, muren en meubels. Dat voelt snel warm aan, een beetje zoals de zon op uw huid. Volgens het Duurzaam Bouwloket is een paneel vooral geschikt als <strong>lokale bijverwarming</strong>: een werkplek op zolder, de badkamer, of een kamer die u maar een paar uur per dag gebruikt. Dan hoeft de cv niet het hele huis warm te stoken voor die ene kamer.</p>
<p>Als <strong>hoofdverwarming</strong> ligt het anders. Het Duurzaam Bouwloket wijst erop dat verwarmen met stroom per eenheid warmte flink duurder is dan met gas, en dat panelen als enige warmtebron alleen goed werken in een goed geïsoleerd huis en met een goede berekening per ruimte. De ANWB rekent voor dat een warmtepomp hetzelfde huis met minder stroom verwarmt. Wilt u het hele huis met infrarood verwarmen, laat dan eerst een warmteberekening maken. Wij zijn elektriciens: wij zorgen dat de elektra het veilig aankan.</p>

<h2>Hoeveel watt <em>heeft u nodig?</em></h2>
<p>Dat hangt af van de grootte van de ruimte, de isolatie en de hoogte van het plafond. Als ruwe vuistregel noemt de ANWB ongeveer 1.000 watt voor 25 tot 30 m². Gangbare panelen zitten tussen zo'n 300 en 1.000 watt. Een paneel van 600 watt verbruikt 0,6 kWh voor elk uur dat het vol aanstaat.</p>
<p>Voor de elektra telt vooral het totaal: hoeveel panelen er komen, in welke kamers, en wat er verder op die groepen zit.</p>

<h2>Hoeveel panelen <em>op één groep?</em></h2>
<p>Een gewone groep van 16 ampère kan ongeveer 3.680 watt leveren. Dat lijkt veel, maar op die groep zitten meestal ook stopcontacten en lampen, en verwarming staat urenlang achter elkaar aan. Daarom houden we ruim marge:</p>
<ul class="checks">
  <li>{check}<span><strong>Eén klein paneel</strong> in een slaapkamer, werkkamer of op het toilet kan vaak op de bestaande groep, als die niet al zwaar belast is.</span></li>
  <li>{check}<span><strong>Meerdere panelen,</strong> of een paneel in een kamer waar ook een kachel, föhn of computer aanstaat: dan geven we de panelen liever <a href="/groep-bijplaatsen-rotterdam/">een eigen groep</a>. Ook het Duurzaam Bouwloket noemt dat er bij het plaatsen van panelen één of meer groepen in de meterkast nodig kunnen zijn.</span></li>
  <li>{check}<span><strong>Een hele verdieping of het hele huis</strong> op infrarood: dan kijken we ook naar uw aansluiting. Een extra groep geeft geen extra vermogen; wat u in totaal tegelijk kunt gebruiken, bepaalt de hoofdzekering van de netbeheerder. Lees dan ook <a href="/meterkast-verzwaren-rotterdam/">meterkast verzwaren</a>.</span></li>
</ul>
<p>Valt een groep nu al uit als het paneel en de waterkoker tegelijk aanstaan? Dan is die groep overbelast. Lees wat u zelf kunt doen bij <a href="/storing-elektra-rotterdam/">stroom uitgevallen</a>.</p>

<h2>Stekker of <em>vaste aansluiting?</em></h2>
<p>Veel panelen worden geleverd met een snoer en een stekker. Dat werkt, maar aan het plafond wilt u geen snoer naar een stopcontact laag op de muur. Daarom maken we meestal een vast aansluitpunt op de plek van het paneel:</p>
<ul class="checks">
  <li>{check}<span><strong>Plafond heeft vaak de voorkeur.</strong> Volgens het Duurzaam Bouwloket wordt de straling dan minder snel tegengehouden door meubels. We maken een aansluitpunt in het plafond, of gebruiken een bestaand lichtpunt als dat op de goede plek zit en de groep het aankan.</span></li>
  <li>{check}<span><strong>Aan de muur</strong> komt het aansluitpunt achter of naast het paneel, zodat er geen snoer te zien is.</span></li>
  <li>{check}<span><strong>Betonnen plafonds.</strong> In veel Rotterdamse portiekwoningen en flats is het plafond van beton. Een nieuwe leiding in beton frezen is veel werk; vaak is een nette opbouwleiding of een bestaand lichtpunt handiger. Dat overleggen we vooraf.</span></li>
  <li>{check}<span><strong>Regeling.</strong> Een thermostaat per ruimte, vaak draadloos met een kleine ontvanger die we in een inbouwdoos wegwerken. Zo staat het paneel niet onnodig aan.</span></li>
</ul>
<p>Een thermostaat kan het verbruik volgens Zonneplan met 30 tot 40 procent verlagen, omdat het paneel uitschakelt zodra de kamer warm is. Een bewegingsmelder raadt het Duurzaam Bouwloket juist af: het paneel gaat dan pas aan als u binnenkomt, en de kamer wordt te laat warm. In de badkamer werkt een timer vaak goed, bijvoorbeeld 's ochtends een half uur.</p>

<h2>Infrarood <em>in de badkamer.</em></h2>
<p>De badkamer is een populaire plek voor een paneel, vaak als spiegel- of handdoekpaneel. Daar gelden strengere regels, omdat water en stroom dicht bij elkaar komen. De ruimte rond het bad en de douche is verdeeld in zones (volgens NEN 1010; uitleg van GAMMA klusadvies):</p>
<ul class="checks">
  <li>{check}<span><strong>Zone 0 en 1:</strong> in en direct boven het bad of de douchebak, en bij een inloopdouche zonder cabine een straal van 1,2 meter rond de douchekop. Hier hoort geen paneel van 230 volt.</span></li>
  <li>{check}<span><strong>Zone 2:</strong> tot 60 cm naast het bad of de douchecabine. Hier mag alleen apparatuur van minstens IPX4.</span></li>
  <li>{check}<span><strong>Daarbuiten</strong> is er meer mogelijk, maar de badkamer moet altijd achter een aardlekschakelaar van 30 mA zitten.</span></li>
</ul>
<p>Kies dus een paneel dat de fabrikant geschikt noemt voor de badkamer; de IP-waarde staat op het typeplaatje. Wij kijken waar het paneel veilig kan hangen en of uw badkamer goed beveiligd is. Verbouwt u de hele badkamer, lees dan ook <a href="/elektra-badkamer-rotterdam/">elektra in de badkamer</a>. Heeft uw groepenkast nog geen <a href="/aardlekschakelaar-rotterdam/">aardlekschakelaar</a>, dan komt die eerst.</p>

<h2>Zolders en oudere woningen <em>in Rotterdam.</em></h2>
<p>Op de zolder van een jaren-30 woning of in een naoorlogse portiekwoning zit vaak maar één groep voor de hele verdieping, soms nog met oude bedrading. Voordat er een paneel van 600 of 800 watt bij komt dat urenlang aanstaat, meten we die groep na. Zijn de draden oud of is er geen aarde, dan is <a href="/bedrading-vervangen-rotterdam/">de bedrading vervangen</a> of een nieuwe groep de veilige eerste stap.</p>
<p>Huurt u uw woning? Vraag dan eerst toestemming aan de verhuurder voor een vast paneel aan plafond of muur.</p>

<h2>Wat wij <em>doen.</em></h2>
<ul class="checks">
  <li>{check}<span><strong>De meterkast bekijken:</strong> op welke groep het paneel komt, wat er al op zit, en of er een aardlekschakelaar is.</span></li>
  <li>{check}<span><strong>Een vast aansluitpunt</strong> op plafond of muur, en <a href="/groep-bijplaatsen-rotterdam/">een eigen groep</a> als dat nodig is.</span></li>
  <li>{check}<span><strong>Het paneel ophangen</strong> met de beugels van de fabrikant en aansluiten, met de ontvanger van de thermostaat als u die heeft.</span></li>
  <li>{check}<span><strong>Testen en uitleggen:</strong> we testen de groep en de aardlekbeveiliging, en zetten op de groepenkast waar de groep voor is.</span></li>
</ul>
<p>Het paneel zelf koopt u bij een winkel of leverancier naar keuze. Twijfelt u welk vermogen past bij de plek? Stuur het typeplaatje of de link van het paneel mee, dan kijken we of de elektra het aankan.</p>

<h2>Zo <em>pakken we het aan.</em></h2>
<ol class="steps-list">
  <li><strong>Stuur foto's via WhatsApp</strong> van uw open meterkast en de plek waar het paneel komt, en vertel welk paneel het is (vermogen in watt).</li>
  <li><strong>Wij beoordelen</strong> of het op een bestaande groep kan of een eigen groep nodig heeft, en hoe de leiding naar de plek loopt. U krijgt een duidelijke prijs vooraf.</li>
  <li><strong>Wij hangen het paneel op en sluiten het aan,</strong> met een vast aansluitpunt en eventueel een nieuwe groep.</li>
  <li><strong>We testen alles en lopen het met u na,</strong> zodat u weet hoe de thermostaat of timer werkt.</li>
</ol>
<p>Alles volgens NEN 1010, door verzekerde vakmensen.</p>

<div class="note-box"><p><strong>Bronnen:</strong> Duurzaam Bouwloket, <a href="https://res.cloudinary.com/duurzaambouwloket/image/upload/v1619613396/Factsheets/Factsheet_Infrarood_panelen_2021.pdf" target="_blank" rel="noopener noreferrer">factsheet infraroodpanelen</a>; ANWB, <a href="https://www.anwb.nl/huis/energie/alles-over-infraroodverwarming" target="_blank" rel="noopener noreferrer">10 dingen over infraroodverwarming</a>; Zonneplan, <a href="https://www.zonneplan.nl/energie/besparen/hoeveel-stroom-verbruikt-een-infrarood-paneel/" target="_blank" rel="noopener noreferrer">hoeveel stroom verbruikt een infraroodpaneel</a>; GAMMA klusadvies, <a href="https://www.gamma.nl/klusadvies/a/elektra-badkamer-aansluiten" target="_blank" rel="noopener noreferrer">elektra in de badkamer</a>.</p></div>
""",
        "faq": [
            ("Kan ik een infraroodpaneel gewoon in het stopcontact steken?",
             "Een paneel met stekker kunt u in een gewoon geaard stopcontact steken. Let wel op wat er nog meer op die groep staat, want het paneel staat lang aan. Aan het plafond of in de badkamer is een vaste aansluiting netter, zonder snoer over de muur."),
            ("Hoeveel infraroodpanelen kunnen op één groep?",
             "Een groep van 16 ampère kan ongeveer 3.680 watt leveren, maar er zitten meestal ook stopcontacten en lampen op, en verwarming staat lang aan. Eén klein paneel past vaak; bij meerdere panelen geven we ze liever een eigen groep. Stuur een foto van uw meterkast, dan rekenen we het na."),
            ("Moet mijn meterkast verzwaard worden voor infrarood?",
             "Voor een paar panelen als bijverwarming bijna nooit. Wilt u een hele verdieping of het hele huis met infrarood verwarmen, zeker samen met inductie of een laadpaal, dan rekenen we eerst uit of uw aansluiting dat aankan."),
            ("Mag een infraroodpaneel in de badkamer?",
             "Ja, als het paneel daarvoor geschikt is en niet in zone 0 of 1 hangt, dus niet in of direct boven het bad of de douche. In zone 2, tot 60 cm naast bad of douchecabine, moet het minstens IPX4 zijn. De badkamer moet achter een aardlekschakelaar van 30 mA zitten."),
            ("Hang ik een infraroodpaneel aan het plafond of aan de muur?",
             "Het plafond heeft vaak de voorkeur, omdat meubels de straling dan minder tegenhouden. Aan de muur kan ook, bijvoorbeeld als spiegel- of handdoekpaneel. Wij maken op beide plekken een vast aansluitpunt."),
            ("Is infrarood goedkoper dan de cv?",
             "Als bijverwarming voor één kamer kan het voordelig zijn, omdat de cv dan niet het hele huis hoeft te verwarmen. Als hoofdverwarming is stroom per eenheid warmte meestal duurder dan gas, en verwarmt een warmtepomp hetzelfde huis met minder stroom. Laat voor hoofdverwarming eerst een warmteberekening maken."),
            ("Kunnen jullie een bestaand lichtpunt gebruiken?",
             "Vaak wel, als het lichtpunt op de goede plek zit en de groep het extra vermogen aankan. Dat meten we eerst na. Zit het lichtpunt verkeerd, dan maken we een nieuw aansluitpunt."),
            ("Wat kost een infraroodpaneel laten aansluiten?",
             "Dat hangt af van de plek, de afstand tot de meterkast en of er een eigen groep nodig is. Stuur foto's van de meterkast en de plek via WhatsApp, dan krijgt u vooraf een duidelijke prijs."),
        ],
    },
    # ----------------------------------------------------- KRACHTSTROOM
    {
        "slug": "krachtstroom-aansluiten-rotterdam",
        "short": "Krachtstroom aansluiten",
        "sub": "400V-groep en krachtstroomstopcontact voor garage, werkplaats of sauna.",
        "title": "Krachtstroom aansluiten Rotterdam | 400V-groep | AlleKlussers",
        "desc": "Krachtstroom aansluiten in Rotterdam: een 400V-groep en krachtstroomstopcontact voor garage, werkplaats of sauna. Eerst kijken of het nodig is, prijs vooraf.",
        "service": "Krachtstroom aanleggen: krachtgroep en krachtstroomstopcontact",
        "char": "vonk",
        "say": "“Drie fasen voor de zware jongens.”",
        "eyebrow": "Krachtstroom (400 volt)",
        "h1": "Krachtstroom aansluiten in <em>Rotterdam.</em>",
        "lede": "Een draaibank, compressor of saunakachel die 400 volt vraagt? Dan heeft u een krachtstroomgroep met een eigen stopcontact nodig. Wij kijken eerst of uw meterkast er klaar voor is, en of u krachtstroom echt nodig heeft.",
        "body": """
<h2>Wat is <em>krachtstroom?</em></h2>
<p>Krachtstroom, ook wel draaistroom genoemd, is stroom die via drie fasen naar een apparaat gaat. Tussen twee fasen staat 400 volt, terwijl een gewoon stopcontact 230 volt geeft. Een apparaat op krachtstroom kan daardoor veel meer vermogen opnemen zonder dat één groep overbelast raakt.</p>
<p>Ter vergelijking: een gewone groep van 16 ampère levert ongeveer 3.680 watt. Een krachtstroomgroep van 3x16A levert ongeveer 11 kW, verdeeld over de drie fasen.</p>

<h2>Heeft u krachtstroom <em>echt nodig?</em></h2>
<p>In een gewone woning is krachtstroom bijna nooit nodig. Veel mensen die "krachtstroom" zoeken, bedoelen eigenlijk iets anders:</p>
<ul class="checks">
  <li>{check}<span><strong>Inductiekookplaat:</strong> die sluiten we in een woning normaal aan op een kookgroep met perilex, op één of twee fasen. Krachtstroom is daar meestal niet voor nodig. Zie <a href="/inductiekookplaat-aansluiten-rotterdam/">inductiekookplaat aansluiten</a>.</span></li>
  <li>{check}<span><strong>Laadpaal:</strong> laden over drie fasen gaat sneller, tot 11 kW, maar daarvoor komt er een eigen 3-fase groep voor de laadpaal, geen krachtstroomstopcontact. Zie <a href="/laadpaal-installeren-rotterdam/">laadpaal installeren</a>.</span></li>
  <li>{check}<span><strong>Warmtepomp:</strong> dat is vooral een vraag of uw aansluiting genoeg capaciteit heeft. Lees daarvoor <a href="/meterkast-verzwaren-rotterdam/">meterkast verzwaren</a>.</span></li>
</ul>
<p>Krachtstroom is wel nodig voor apparaten die zelf 400 volt vragen. Op het typeplaatje of in de handleiding staat dan bijvoorbeeld 400 V of 3N~. Voorbeelden:</p>
<ul class="checks">
  <li>{check}<span><strong>Werkplaats in de garage of schuur:</strong> een draaibank, zaagtafel of andere zware machine.</span></li>
  <li>{check}<span><strong>Compressor</strong> voor een hobbywerkplaats of klein bedrijf.</span></li>
  <li>{check}<span><strong>Sauna</strong> met een zware kachel die de fabrikant op 400 volt laat aansluiten.</span></li>
  <li>{check}<span><strong>Beregeningspomp</strong> of professionele keukenapparatuur.</span></li>
</ul>
<p>Twijfelt u? Stuur ons een foto van het typeplaatje van het apparaat. Dan zeggen we u eerlijk of het op een gewone groep kan, op een kookgroep, of dat er echt krachtstroom moet komen.</p>

<h2>Heeft u al <em>3-fase in de meterkast?</em></h2>
<p>Krachtstroom kan alleen als uw woning of pand een 3-fase aansluiting heeft. Dat ziet u zo:</p>
<ul class="checks">
  <li>{check}<span><strong>1-fase:</strong> één hoofdzekering van de netbeheerder in de meterkast en twee draden op de kWh-meter. Op de jaarafrekening staat bijvoorbeeld 1x25A of 1x35A.</span></li>
  <li>{check}<span><strong>3-fase:</strong> drie hoofdzekeringen en vier draden op de meter. Op de jaarafrekening staat bijvoorbeeld 3x25A.</span></li>
</ul>
<p>Heeft u al 3-fase, dan kunnen wij de krachtstroomgroep gewoon aanleggen. Heeft u 1-fase, dan moet de netbeheerder de aansluiting eerst verzwaren; in Rotterdam is dat meestal Stedin. Omdat het stroomnet in de regio op veel plekken vol is, kan dat lang duren. Lees eerst <a href="/meterkast-verzwaren-rotterdam/">meterkast verzwaren</a> voordat u iets aanvraagt.</p>

<h2>3-fase aansluiting of krachtstroomgroep: <em>het verschil.</em></h2>
<p>Die twee worden vaak door elkaar gehaald. Een <strong>3-fase aansluiting</strong> is wat de netbeheerder levert: drie fasen tot aan uw meter. Daarmee kunt u het verbruik in huis over drie fasen verdelen, en het is de voorwaarde voor krachtstroom. Een <strong>krachtstroomgroep</strong> is wat de installateur daarachter aanlegt: één eigen groep met een eigen stopcontact of vaste aansluiting voor één apparaat dat 400 volt vraagt. Veel woningen met 3-fase hebben dus nog geen krachtstroomstopcontact.</p>

<h2>Wat wij <em>aanleggen.</em></h2>
<ul class="checks">
  <li>{check}<span><strong>Een krachtgroep in de groepenkast:</strong> een 3-polige installatieautomaat met nul, beveiligd met een aardlekschakelaar die alle drie de fasen bewaakt, of een 4-polige aardlekautomaat. Zit de kast vol of is hij verouderd, dan <a href="/groepenkast-vervangen-rotterdam/">breiden we hem uit of vervangen we hem</a>.</span></li>
  <li>{check}<span><strong>Een eigen kabel naar de plek,</strong> met aders voor de drie fasen, de nul en de aarde. De dikte kiezen we op het vermogen van het apparaat en de lengte van de kabel.</span></li>
  <li>{check}<span><strong>Een krachtstroomstopcontact:</strong> een rond CEE-stopcontact met vier of vijf pennen, meestal rood voor 400 volt, in 16 of 32 ampère. In een garage, schuur of buiten kiezen we een spatwaterdichte uitvoering. Schrijft de fabrikant een vaste aansluiting voor, dan sluiten we het apparaat direct aan.</span></li>
  <li>{check}<span><strong>De juiste draairichting.</strong> Bij een draaistroommotor maakt de volgorde van de fasen uit: verkeerd aangesloten draait de motor de verkeerde kant op. Wij controleren de fasevolgorde voordat u de machine gebruikt.</span></li>
</ul>

<div class="note-box"><p><strong>Een perilex-stopcontact is geen krachtstroom.</strong> Perilex, het ronde stopcontact met vijf gaatjes in de keuken, is een stekkervorm. Hoeveel fasen erop zitten, hangt af van hoe de groep is aangelegd; in een woning is het bijna altijd een kookgroep op twee fasen. Sluit een machine die 400 volt vraagt dus niet aan op een perilex-aansluiting of via een verloopstekker. Meer over perilex leest u bij <a href="/perilex-aansluiten-rotterdam/">perilex aansluiten</a>.</p></div>

<h2>Krachtstroom in de schuur <em>of garage.</em></h2>
<p>In Rotterdam en omgeving staat de werkplaats vaak in een schuur achter in de tuin, of in een garage naast of onder de woning. Dan loopt de kabel van de meterkast naar buiten, en vaak onder de grond door de tuin. Dat doen we net zo zorgvuldig als bij een <a href="/buitenverlichting-tuinstopcontact-rotterdam/">tuinstopcontact</a>: diep genoeg, in een beschermbuis en goed afgedicht waar de kabel de muur in gaat. In de schuur komt dan het krachtstroomstopcontact, en vaak ook meteen een gewone groep voor licht en een paar stopcontacten.</p>
<p>Huurt u een garagebox, een bedrijfsunit of uw woning, dan is de aansluiting meestal niet van u. Vraag dan eerst toestemming aan de eigenaar; wij kunnen het werk daarna met de eigenaar afstemmen.</p>

<h2>Zo <em>pakken we het aan.</em></h2>
<ol class="steps-list">
  <li><strong>Stuur foto's via WhatsApp</strong> van uw open meterkast en het typeplaatje van het apparaat, en vertel waar het komt te staan.</li>
  <li><strong>Wij beoordelen</strong> of u krachtstroom echt nodig heeft, of uw aansluiting 3-fase is en of er ruimte in de groepenkast is. U krijgt een duidelijke prijs vooraf.</li>
  <li><strong>Wij leggen de krachtgroep aan,</strong> trekken de kabel naar de plek en monteren het krachtstroomstopcontact of de vaste aansluiting.</li>
  <li><strong>We testen de groep, de aardlekbeveiliging en de draairichting,</strong> en zetten op de groepenkast waar de nieuwe groep voor is.</li>
</ol>
<p>Alles volgens NEN 1010, door verzekerde vakmensen. Zelf krachtstroom aanleggen raden we af: met 400 volt tussen de fasen is een fout veel gevaarlijker dan bij een gewoon stopcontact.</p>

<div class="note-box"><p><strong>Bronnen:</strong> Selectra over <a href="https://selectra.nl/energie/energiemeter/krachtstroom" target="_blank" rel="noopener noreferrer">krachtstroom: wat het is en wanneer u het nodig heeft</a> (met informatie van netbeheerder Enexis), Elektramat kennisbank over <a href="https://www.elektramat.nl/kennisbank/aanpassen-groepenkast" target="_blank" rel="noopener noreferrer">het aanpassen van de groepenkast</a>.</p></div>
""",
        "faq": [
            ("Wat is het verschil tussen krachtstroom en 3-fase?",
             "Een 3-fase aansluiting is wat de netbeheerder levert: drie fasen tot aan uw meter. Krachtstroom is het gebruik daarvan: een eigen groep en stopcontact voor een apparaat dat 400 volt vraagt. Zonder 3-fase aansluiting kan er geen krachtstroom komen."),
            ("Heb ik krachtstroom nodig voor een inductiekookplaat?",
             "Meestal niet. Een inductiekookplaat sluiten we in een woning normaal aan op een kookgroep met perilex, op één of twee fasen. Alleen sommige grote kookplaten en fornuizen vragen echt drie fasen."),
            ("Kan ik krachtstroom krijgen met een 1-fase aansluiting?",
             "Nee. Daarvoor moet de netbeheerder uw aansluiting eerst verzwaren naar 3-fase. Wij rekenen vooraf met u uit of dat nodig is, want in de regio Rotterdam kan een verzwaring lang duren."),
            ("Hoeveel vermogen levert een krachtstroomgroep?",
             "Een krachtstroomgroep van 3x16A levert ongeveer 11 kW, verdeeld over drie fasen. Voor zwaardere apparaten is er 32 ampère, met een dikkere kabel. Welke u nodig heeft, staat op het typeplaatje of in de handleiding van het apparaat."),
            ("Is een perilex-stopcontact krachtstroom?",
             "Niet vanzelf. Perilex is een stekkervorm; hoeveel fasen erop zitten hangt af van de groep erachter. In een woning is het bijna altijd een kookgroep op twee fasen. Sluit er geen 400V-machine op aan."),
            ("Mijn machine draait de verkeerde kant op. Wat nu?",
             "Dan is de fasevolgorde verkeerd aangesloten. Zet de machine uit en gebruik hem niet meer tot een installateur de fasen heeft omgezet. Wij controleren de draairichting altijd bij oplevering."),
            ("Kunnen jullie krachtstroom naar mijn schuur aanleggen?",
             "Ja. We trekken een eigen kabel van de meterkast naar de schuur, onder de grond in een beschermbuis, en plaatsen daar een krachtstroomstopcontact. Vaak komt er meteen een gewone groep bij voor licht en stopcontacten."),
            ("Wat kost krachtstroom aanleggen?",
             "Dat hangt af van uw aansluiting, de ruimte in de groepenkast en de afstand naar de plek. Stuur foto's van de meterkast en het typeplaatje via WhatsApp, dan krijgt u vooraf een duidelijke prijs."),
        ],
    },
    # -------------------------------------------------------- THUISBATTERIJ
    {
        "slug": "thuisbatterij-aansluiten-rotterdam",
        "short": "Thuisbatterij aansluiten",
        "sub": "Eigen groep en meterkast klaar voor 2027.",
        "title": "Thuisbatterij Rotterdam: meterkast en eigen groep | AlleKlussers",
        "desc": "Thuisbatterij in Rotterdam? Salderen stopt op 1 januari 2027. Wij maken uw meterkast klaar: eigen groep, aardlekbeveiliging en bekabeling naar de batterij.",
        "service": "Thuisbatterij aansluiten",
        "char": "laadie",
        "say": "“Zonnestroom bewaren? Ik sluit hem aan.”",
        "eyebrow": "Thuisbatterij en meterkast",
        "h1": "Thuisbatterij aansluiten in <em>Rotterdam.</em>",
        "lede": "Op 1 januari 2027 stopt de salderingsregeling. Met een thuisbatterij gebruikt u meer van uw eigen zonnestroom. Wij zorgen dat uw meterkast er klaar voor is: een eigen groep, de juiste beveiliging en de bekabeling naar de plek van de batterij.",
        "body": """
<h2>Waarom nu <em>een thuisbatterij?</em></h2>
<p>Tot en met 31 december 2026 mag u de stroom die uw zonnepanelen terugleveren nog wegstrepen tegen de stroom die u van het net gebruikt. Vanaf 1 januari 2027 kan dat niet meer. U krijgt dan alleen een terugleververgoeding, en die is meestal lager dan wat u voor stroom betaalt. Zonnestroom die u zelf gebruikt, wordt dus meer waard.</p>
<p>Een thuisbatterij slaat overdag uw zonnestroom op, zodat u die 's avonds zelf kunt gebruiken. Of dat voor u loont, hangt af van uw zonnepanelen en uw verbruik. Reken het daarom eerst goed door, eventueel met uw leverancier.</p>

<h2>Stekkerbatterij of <em>vaste batterij?</em></h2>
<ul class="checks">
  <li>{check}<span><strong>Stekkerbatterij:</strong> steekt u zelf in een stopcontact. Er is geen installateur nodig, maar de capaciteit is beperkt. Veiliger is een <a href="/vrije-groep-stekkerbatterij-rotterdam/">vrije groep voor uw stekkerbatterij</a>; die leggen wij aan.</span></li>
  <li>{check}<span><strong>Vaste thuisbatterij:</strong> meer capaciteit, maar die hoort op een eigen groep in de meterkast. Die groep en de bekabeling leggen wij aan; de batterij en omvormer zelf worden ingesteld door de leverancier of zijn installateur.</span></li>
</ul>

<h2>Wat wij <em>doen.</em></h2>
<ul class="checks">
  <li>{check}<span><strong>Meterkast controleren:</strong> heeft uw groepenkast ruimte voor een extra groep, en is uw aansluiting zwaar genoeg?</span></li>
  <li>{check}<span><strong>Groepenkast aanpassen of uitbreiden</strong> als dat nodig is, met de juiste aardlekbeveiliging.</span></li>
  <li>{check}<span><strong>Eigen groep en bekabeling</strong> van de meterkast naar de plek van de batterij.</span></li>
  <li>{check}<span><strong>Afstemmen met uw leverancier,</strong> zodat de groep, de beveiliging en de kabel passen bij de batterij en omvormer die u kiest.</span></li>
</ul>

<div class="note-box"><p><strong>Druk richting 2027.</strong> Veel mensen willen hun batterij vóór 1 januari 2027 regelen. Plan daarom op tijd, dan voorkomt u wachttijden.</p></div>

<p>Moet uw groepenkast eerst worden vervangen of uitgebreid? Lees meer over <a href="/groepenkast-vervangen-rotterdam/">groepenkast vervangen in Rotterdam</a>. Twijfelt u nog of een batterij loont? Lees eerst <a href="/salderen-stopt-2027/">wat het einde van salderen betekent</a>.</p>
""",
        "faq": [
            ("Heb ik na 2027 een thuisbatterij nodig?",
             "Niet per se. Het hangt af van hoeveel zonnestroom u teruglevert en wanneer u stroom gebruikt. Wie veel teruglevert en 's avonds veel verbruikt, heeft er meer aan. Laat het goed doorrekenen voordat u koopt."),
            ("Mag ik een stekkerbatterij zelf aansluiten?",
             "Ja, een stekkerbatterij steekt u zelf in het stopcontact. Let wel op dat de groep niet overbelast raakt. Twijfelt u, dan controleren wij uw groep."),
            ("Is mijn meterkast geschikt voor een vaste thuisbatterij?",
             "Dat controleren we eerst. Vaak is een extra groep genoeg; soms moet de groepenkast worden uitgebreid of vervangen. Dat hoort u vooraf van ons, met een prijs."),
            ("Moet ik een thuisbatterij ergens aanmelden?",
             "Ja. Een thuisbatterij registreert u via energieleveren.nl, net als zonnepanelen. Volgens RVO geldt die registratieplicht voor batterijsystemen van type A."),
            ("Leveren of installeren jullie ook de batterij zelf?",
             "Nee. Wij richten ons op de meterkast: een eigen groep, de juiste beveiliging en de bekabeling naar de plek van de batterij. De batterij en omvormer worden geleverd en ingesteld door de leverancier of zijn installateur. Wij stemmen met hen af."),
        ],
    },
    # ------------------------------------------------------- VRIJE GROEP
    {
        "slug": "vrije-groep-stekkerbatterij-rotterdam",
        "short": "Vrije groep stekkerbatterij",
        "sub": "Eigen groep en stopcontact voor uw stekkerbatterij.",
        "title": "Vrije groep voor stekkerbatterij Rotterdam | AlleKlussers",
        "desc": "Stekkerbatterij gekocht? Laat in Rotterdam een vrije groep met eigen stopcontact aanleggen, zodat uw bedrading niet overbelast raakt. Duidelijke prijs vooraf.",
        "service": "Vrije groep aanleggen voor stekkerbatterij",
        "char": "dosie",
        "say": "“Eigen stopcontact voor uw batterij? Komt goed.”",
        "eyebrow": "Stekkerbatterij veilig aansluiten",
        "h1": "Vrije groep voor uw <em>stekkerbatterij.</em>",
        "lede": "Een stekkerbatterij steekt u zelf in het stopcontact. Op een eigen, vrije groep is dat een stuk veiliger. Wij leggen die groep en het stopcontact voor u aan, in Rotterdam en omgeving.",
        "body": """
<h2>Waarom een <em>vrije groep?</em></h2>
<p>Een stekkerbatterij laadt op en levert stroom terug via een gewoon stopcontact. Zit dat stopcontact op een groep met andere apparaten, zoals de wasmachine of de oven, dan kan de bedrading van die groep meer stroom te verwerken krijgen dan waarvoor hij is beveiligd. De batterij levert namelijk stroom op de groep zelf, en die stroom ziet de zekering in de meterkast niet.</p>
<p>Daarom wordt een vrije groep, waar alleen de batterij op zit, sterk aangeraden. Sommige fabrikanten vragen er ook om.</p>

<h2>Wat wij <em>doen.</em></h2>
<ul class="checks">
  <li>{check}<span><strong>Meterkast controleren:</strong> is er ruimte voor een extra groep, en is uw groepenkast nog in orde?</span></li>
  <li>{check}<span><strong>Nieuwe groep plaatsen</strong> met een eigen aardlekautomaat.</span></li>
  <li>{check}<span><strong>Kabel en stopcontact</strong> naar de plek van de batterij: berging, zolder, meterkast of schuur. Buiten met een spatwaterdicht stopcontact.</span></li>
  <li>{check}<span><strong>Testen en uitleg,</strong> zodat u weet welke groep bij de batterij hoort.</span></li>
</ul>

<div class="note-box"><p><strong>Groepenkast vol?</strong> Dan breiden we hem uit of adviseren we een nieuwe. Lees meer over <a href="/groepenkast-vervangen-rotterdam/">groepenkast vervangen</a>. Overweegt u een grotere, vaste batterij? Kijk dan bij <a href="/thuisbatterij-aansluiten-rotterdam/">thuisbatterij aansluiten</a>.</p></div>

<h2>Zo <em>werkt het.</em></h2>
<p>Stuur ons via WhatsApp een foto van uw meterkast en vertel waar de batterij komt te staan. U krijgt binnen 24 uur een vaste prijs. Meestal is het werk binnen een dagdeel klaar.</p>
""",
        "faq": [
            ("Is een vrije groep verplicht voor een stekkerbatterij?",
             "Niet altijd, maar het wordt sterk aangeraden voor de brandveiligheid, en sommige fabrikanten vragen erom. Zo weet u zeker dat de bedrading niet overbelast raakt."),
            ("Hoe lang duurt het aanleggen van een vrije groep?",
             "Meestal is het binnen een dagdeel klaar. De stroom is daarbij kort uit; dat stemmen we vooraf met u af."),
            ("Wat als er geen ruimte is in mijn groepenkast?",
             "Dan kan de groepenkast vaak worden uitgebreid. Is hij verouderd, dan adviseren we eerlijk of vervangen verstandiger is. U krijgt altijd eerst een prijs."),
            ("Kan het stopcontact ook in de schuur of op het balkon?",
             "Ja. Buiten gebruiken we een spatwaterdicht stopcontact en de juiste beveiliging in de meterkast."),
            ("Moet ik mijn stekkerbatterij aanmelden?",
             "Thuisbatterijen moet u registreren via energieleveren.nl (RVO, type A). Een stekkerbatterij van 800 watt zit op de ondergrens daarvan. Aanmelden is gratis en eenmalig, dus wij raden het aan."),
        ],
    },
    # ------------------------------------------------------------ VERLICHTING
    {
        "slug": "lampen-ophangen-rotterdam",
        "short": "Lampen ophangen",
        "sub": "Plafondlampen, spots, dimmers en buitenverlichting.",
        "title": "Elektricien lampen ophangen Rotterdam | AlleKlussers",
        "desc": "Lampen laten ophangen in Rotterdam: hanglampen, kroonluchters, spots en LED-dimmers. LED knippert of gloeit na? Wij lossen het op. Prijs vooraf.",
        "service": "Lampen ophangen en verlichting installeren",
        "char": "lampje",
        "say": "“Meer licht? Daar ben ik voor.”",
        "eyebrow": "Verlichting",
        "h1": "Lampen ophangen in <em>Rotterdam.</em>",
        "lede": "Plafondlampen, hanglampen, kroonluchters, spots en dimmers: netjes gemonteerd en veilig aangesloten. En een LED die knippert of nagloeit, lossen we op.",
        "body": """
<h2>Wat wij <em>voor u doen.</em></h2>
<ul class="checks">
  <li>{check}<span><strong>Lampen ophangen</strong> op bestaande aansluitpunten: plafondlampen, hanglampen, kroonluchters en wandlampen.</span></li>
  <li>{check}<span><strong>Nieuwe lichtpunten maken,</strong> bijvoorbeeld boven de eettafel of het keukeneiland.</span></li>
  <li>{check}<span><strong>Inbouwspots plaatsen</strong> in plafonds, keukens en badkamers.</span></li>
  <li>{check}<span><strong>Dimmers en schakelaars</strong> die geschikt zijn voor LED, zonder geknipper of gezoem, en een tweede schakelaar, bijvoorbeeld onder en boven aan de trap.</span></li>
  <li>{check}<span><strong>Buitenverlichting</strong> aan de gevel, in de tuin of bij de voordeur, waterdicht aangesloten. Meer daarover bij <a href="/buitenverlichting-tuinstopcontact-rotterdam/">buitenverlichting en tuinstopcontact</a>.</span></li>
  <li>{check}<span><strong>Badkamerverlichting en LED-spiegels,</strong> veilig in een natte ruimte. Verbouwt u de hele badkamer? Lees alles over <a href="/elektra-badkamer-rotterdam/">badkamerverlichting en elektra in de badkamer</a>.</span></li>
</ul>

<div class="note-box"><p><strong>Tip:</strong> heeft u meerdere lampen? Laat ze in één afspraak ophangen. Dan hoeft u maar één keer thuis te blijven.</p></div>

<h2>LED knippert, zoemt <em>of gloeit na?</em></h2>
<p>LED-lampen gebruiken heel weinig stroom. Daardoor gaan ze sneller knipperen of nagloeien dan oude gloeilampen. De oorzaak zit bijna altijd in de combinatie van lamp, dimmer en bedrading:</p>
<ul class="checks">
  <li>{check}<span><strong>Een oude dimmer.</strong> Klassieke dimmers (fase-aansnijding) werken pas goed vanaf een minimale belasting. Met een paar zuinige LED-lampen haalt u die vaak niet, en dan knippert of zoemt de lamp. Een dimmer met fase-afsnijding is veel beter geschikt voor LED.</span></li>
  <li>{check}<span><strong>Te weinig of te veel vermogen.</strong> Elke dimmer heeft een bereik, bijvoorbeeld 5 tot 100 watt. Zit het totaal van uw lampen onder het minimum, dan knippert het; komt u boven het maximum, dan wordt de dimmer te warm. Bij veel dimmers kunt u de laagste stand ook bijstellen.</span></li>
  <li>{check}<span><strong>Nagloeien als het licht uit staat.</strong> Een zwak schijnsel nadat u het licht uitzet, kan komen door een slechte aarding van een metalen armatuur of door lange draden die naast andere draden lopen. We controleren de aarding en de aansluiting.</span></li>
  <li>{check}<span><strong>Een lamp die niet dimbaar is.</strong> Op de verpakking staat of een LED-lamp dimbaar is. Een niet-dimbare lamp op een dimmer gaat knipperen en slijt snel.</span></li>
</ul>
<p>Wij kiezen een dimmer die past bij uw lampen en het totale vermogen, en controleren de aansluiting. Knippert een lamp zonder dimmer, of gaan er meerdere lampen tegelijk raar doen? Dan kan er iets met de groep of de bedrading zijn; kijk ook op onze pagina over <a href="/storing-elektra-rotterdam/">storingen</a>.</p>
<div class="note-box"><p><strong>Bron:</strong> Volta, <a href="https://volta-org.be/media/pwvfq2vq/leds-zijn-gevoelig-herken-en-verhelp-flikkeren-en-nagloeien.pdf" target="_blank" rel="noopener noreferrer">Leds zijn gevoelig: herken en verhelp flikkeren en nagloeien</a>.</p></div>

<h2>Hanglamp of kroonluchter: <em>waar we op letten.</em></h2>
<ul class="checks">
  <li>{check}<span><strong>Het plafond.</strong> In een betonnen plafond gebruiken we andere bevestiging dan in gipsplaat of een houten plafond. Bij een zware lamp kijken we eerst of het plafond het gewicht kan dragen.</span></li>
  <li>{check}<span><strong>Het lichtpunt.</strong> Zit het aansluitpunt niet waar de lamp moet hangen, bijvoorbeeld boven de eettafel, dan verplaatsen we het of maken we een nieuw lichtpunt.</span></li>
  <li>{check}<span><strong>De aarde.</strong> Een metalen lamp met een aardedraad sluiten we aan op de aarde, als die bij het lichtpunt aanwezig is. In oudere woningen is dat niet altijd zo; dat bespreken we vooraf.</span></li>
</ul>

<h2>Inbouwspots: <em>wat kan er?</em></h2>
<p>Inbouwspots hebben ruimte boven het plafond nodig. In een verlaagd plafond of een houten plafond kan dat meestal; in een betonnen plafond niet zonder een verlaagd plafond eronder. We plannen de spots zo dat het licht gelijkmatig valt en de kabels netjes lopen.</p>
<p>In de badkamer gelden zones. Rond het bad en de douche mogen alleen spots die daarvoor geschikt zijn: vlak erboven alleen verlichting op 12 volt met een hoge waterdichtheid (IPX5), en tot 60 centimeter ernaast minimaal IPX4. Daarbuiten is IP44 genoeg. Meer over de zones, spiegelverlichting en de ventilator staat bij <a href="/elektra-badkamer-rotterdam/">elektra en verlichting in de badkamer</a>.</p>
<div class="note-box"><p><strong>Bron:</strong> GAMMA klusadvies over <a href="https://www.gamma.nl/klusadvies/a/elektra-badkamer-aansluiten" target="_blank" rel="noopener noreferrer">elektra in de badkamer</a>.</p></div>

<h2>Zo <em>werkt het.</em></h2>
<p>Stuur ons een berichtje met het aantal lampen en, als dat kan, een foto van de plek en de lamp. U krijgt binnen 24 uur een prijs. Onze elektricien neemt het kleine materiaal mee, zoals schroeven, pluggen en lasklemmen, hangt alles op en test of het werkt.</p>
""",
        "faq": [
            ("Kunnen jullie ook zware lampen of kroonluchters ophangen?",
             "Ja. We kijken eerst of het plafond het gewicht kan dragen en gebruiken de juiste bevestiging voor beton, gipsplaat of hout."),
            ("Mijn LED-lamp knippert met de dimmer. Kunnen jullie dat oplossen?",
             "Meestal is de dimmer niet geschikt voor LED, of komt het totale vermogen van de lampen onder het minimum van de dimmer. We vervangen hem door een LED-dimmer die bij uw lampen past."),
            ("Mijn LED-lamp gloeit zacht na als het licht uit staat. Is dat gevaarlijk?",
             "Meestal niet direct, maar het wijst op een aansluiting die beter kan, bijvoorbeeld een metalen armatuur zonder goede aarding. We controleren de aarding en de bedrading en lossen het op."),
            ("Kan ik een tweede schakelaar krijgen, bijvoorbeeld boven aan de trap?",
             "Ja. Met een wisselschakeling kunt u dezelfde lamp op twee plekken aan- en uitzetten. Daarvoor trekken we een extra kabel tussen de twee schakelaars."),
            ("Kunnen jullie inbouwspots in een betonnen plafond plaatsen?",
             "Niet direct in het beton. Daarvoor is een verlaagd plafond nodig. In een houten of gipsplaten plafond kan het meestal wel."),
            ("Moet ik de lampen zelf kopen?",
             "Meestal wel, dan kiest u precies wat u mooi vindt. Klein materiaal zoals schroeven, pluggen en lasklemmen nemen wij mee. Twijfelt u over een dimbare lamp of een dimmer? Vraag het ons vooraf."),
            ("Kunnen jullie een nieuw lichtpunt maken waar nog geen aansluiting zit?",
             "Ja, dan trekken we een nieuwe kabel naar de gewenste plek. De prijs hangt af van de route; dat bespreken we vooraf."),
        ],
    },
    # ------------------------------------------------------------ BADKAMER
    {
        "slug": "elektra-badkamer-rotterdam",
        "short": "Elektra badkamer",
        "sub": "Badkamerverlichting, stopcontacten, ventilator en vloerverwarming bij een verbouwing.",
        "title": "Badkamerverlichting en elektra badkamer Rotterdam | AlleKlussers",
        "desc": "Badkamer verbouwen in Rotterdam? Wij doen de elektra: badkamerverlichting en spots per zone, stopcontacten, ventilator en vloerverwarming. Prijs vooraf.",
        "service": "Elektra en verlichting in de badkamer",
        "char": "lampje",
        "say": "“Licht bij de spiegel, droog bij de douche.”",
        "eyebrow": "Badkamer",
        "h1": "Elektra en verlichting in de <em>badkamer.</em>",
        "lede": "Gaat uw badkamer op de schop? Wij doen het elektrische deel: verlichting en spots op de juiste plek, stopcontacten, een ventilator en vloerverwarming. Op tijd gepland, vóór de tegelzetter begint.",
        "body": """
<h2>Plan de elektra <em>vóór het tegelen.</em></h2>
<p>Bij een badkamerverbouwing is de volgorde belangrijk. Leidingen voor lampen, stopcontacten en de ventilator lopen in de muur of het plafond. Zitten de tegels er eenmaal op, dan is iets verplaatsen veel werk. Voor elektrische vloerverwarming geldt het nog sterker: een mat leg je alleen onder een nieuwe vloer, niet onder bestaande tegels (Selectra).</p>
<p>Daarom komen we het liefst twee keer:</p>
<ol class="steps-list">
  <li><strong>Voor het tegelen</strong> trekken we de leidingen en zetten we de inbouwdozen op de goede hoogte, en leggen we eventueel de vloerverwarming met de sensor.</li>
  <li><strong>Na het tegelen</strong> monteren we de lampen, spots, schakelaars, stopcontacten en de ventilator, sluiten alles aan en testen het.</li>
</ol>
<p>Werkt u met een badkamerbedrijf of een eigen tegelzetter? Dan stemmen we de planning met hen af. Maak voor uzelf foto's van de open muren met de leidingen, voordat de tegels erop gaan. Dan weet u later waar u niet mag boren.</p>

<h2>Eerst de meterkast: <em>aardlek en groepen.</em></h2>
<p>Volgens GAMMA klusadvies moet de groepenkast sinds 1975 beveiligd zijn met een aardlekschakelaar van 30 milliampère. Die schakelt de stroom uit bij het kleinste lek, en juist in een natte ruimte is dat de belangrijkste bescherming. In oudere Rotterdamse woningen zit de badkamer soms nog op een groep zonder aardlek. Dan komt die eerst; lees meer bij <a href="/aardlekschakelaar-rotterdam/">aardlekschakelaar</a> of <a href="/groepenkast-vervangen-rotterdam/">groepenkast vervangen</a>.</p>
<p>Daarna kijken we wat er in de nieuwe badkamer bij komt. Verlichting en een ventilator vragen weinig. Vloerverwarming, een elektrische handdoekradiator of een wasmachine in de badkamer vragen meer. Voor zware apparaten maken we liever <a href="/groep-bijplaatsen-rotterdam/">een eigen groep</a>, zodat de groep niet uitvalt als de föhn ook aangaat.</p>
<p>In oudere woningen ziet u soms een blanke of geel-groene aardedraad naar de waterleiding, de badkuip of metalen vloerdelen. Die hoort bij de veiligheid van de badkamer. Haal hem bij het slopen niet weg; wij controleren bij de verbouwing of de aarding van leidingen en installatie in orde is.</p>

<h2>De zones: <em>wat mag waar?</em></h2>
<p>NEN 1010 deelt de badkamer in zones rond het bad en de douche. Hoe dichter bij het water, hoe strenger de eisen. Kort samengevat (uitleg van GAMMA klusadvies; wij werken volgens de norm zelf):</p>
<ul class="checks">
  <li>{check}<span><strong>Zone 0</strong> is de binnenkant van het bad of de douchebak. Hier hoort geen gewone elektrische apparatuur; alleen speciale lampjes op 12 volt die volledig waterdicht zijn (IPX8).</span></li>
  <li>{check}<span><strong>Zone 1</strong> is de ruimte boven het bad of de douchebak. Bij een inloopdouche zonder cabine of bak is het een straal van 1,2 meter rond de douchekop. Hier alleen verlichting en apparatuur op veilige laagspanning (12 volt) met minimaal IPX5, geen lampen van 230 volt.</span></li>
  <li>{check}<span><strong>Zone 2</strong> loopt tot 60 cm naast het bad of de douchecabine. Hier mag apparatuur van minimaal IPX4. Bij een inloopdouche zonder cabine is er geen zone 2, want zone 1 is daar al groter.</span></li>
  <li>{check}<span><strong>Buiten de zones</strong> mogen schakelaars en geaarde stopcontacten, als alles achter een aardlekschakelaar zit.</span></li>
</ul>
<p>Een transformator of LED-driver voor spots op 12 volt hoort buiten de zones rond bad en douche, op een plek waar u er later nog bij kunt. De IP-waarde staat op de verpakking of het typeplaatje van de lamp. Twijfelt u bij een lamp of spiegel? Stuur ons de link, dan kijken we of hij past op de plek die u in gedachten heeft.</p>

<h2>Badkamerverlichting <em>die goed werkt.</em></h2>
<p>Een badkamer heeft meestal meer nodig dan één lamp in het midden van het plafond. Wij denken mee in drie lagen:</p>
<ul class="checks">
  <li>{check}<span><strong>Algemeen licht</strong> aan het plafond: een plafondlamp of een paar inbouwspots. Spots hebben ruimte boven het plafond nodig. In veel Rotterdamse flats en portiekwoningen is het plafond van beton; dan kan het alleen met een verlaagd plafond eronder, of kiest u een opbouwlamp.</span></li>
  <li>{check}<span><strong>Licht bij de spiegel,</strong> van voren en niet alleen van boven, zodat u geen schaduw op uw gezicht krijgt bij het scheren of opmaken. Een spiegel met ingebouwde LED of een spiegelkast met verlichting heeft een aansluitpunt in de muur nodig, op de goede hoogte achter de spiegel.</span></li>
  <li>{check}<span><strong>Sfeerlicht,</strong> bijvoorbeeld een LED-strip in een nis of onder het badmeubel. Ook hier telt de zone: in de douchenis alleen een strip op laagspanning die daarvoor gemaakt is, met de driver buiten de zones.</span></li>
</ul>
<p>Een dimmer op de plafondverlichting is fijn 's nachts en 's avonds in bad. Kies dan wel dimbare LED-lampen en een LED-dimmer; anders gaat het knipperen. Meer over dimmers en spots staat bij <a href="/lampen-ophangen-rotterdam/">lampen ophangen</a>.</p>

<h2>Stopcontacten <em>in de badkamer.</em></h2>
<p>Voor een föhn, een scheerapparaat of een elektrische tandenborstel wilt u een stopcontact bij de wastafel. Dat kan, maar niet overal:</p>
<ul class="checks">
  <li>{check}<span><strong>Buiten zone 2,</strong> dus verder dan 60 cm van het bad of de douchecabine, en bij een inloopdouche buiten de 1,2 meter rond de douchekop.</span></li>
  <li>{check}<span><strong>Geaard en achter een aardlekschakelaar.</strong> Een stopcontact met klapdeksel houdt spatwater buiten.</span></li>
  <li>{check}<span><strong>Op een handige hoogte</strong> naast de spiegel, niet vlak boven de kraan.</span></li>
</ul>
<p>Staat de wasmachine in de badkamer, wat in veel Rotterdamse appartementen zo is? Dan hoort ook dat stopcontact buiten de zones, en geven we de wasmachine liever een eigen groep. Lees ook <a href="/stopcontact-plaatsen-rotterdam/">stopcontact plaatsen of verplaatsen</a>.</p>

<h2>Ventilator: <em>vocht eruit.</em></h2>
<p>Zonder goede afzuiging blijft vocht hangen, en dat geeft schimmel en schade aan verf en voegen. Heeft uw woning mechanische ventilatie met een box op zolder of in een kast, dan zit er vaak al een afzuigpunt in de badkamer. Is er alleen een raam of een rooster, dan kan een losse badkamerventilator helpen:</p>
<ul class="checks">
  <li>{check}<span><strong>Capaciteit.</strong> Elektramat noemt als vuistregel dat de lucht ongeveer 10 keer per uur ververst moet worden: lengte x breedte x hoogte x 10 geeft de benodigde m³ per uur.</span></li>
  <li>{check}<span><strong>Nalooptimer of vochtsensor.</strong> Met een nalooptimer draait de ventilator nog een tijd door nadat u het licht uitzet; Elektramat adviseert 15 tot 30 minuten na het douchen. Een vochtsensor (hygrostaat) zet hem zelf aan als het vochtig wordt.</span></li>
  <li>{check}<span><strong>Aansluiting.</strong> Een ventilator met naloop heeft naast de gewone voeding een schakeldraad nodig, vaak vanaf de lichtschakelaar. Die leiding leggen we het liefst vóór het tegelen.</span></li>
</ul>
<p>Voor een afvoer naar buiten moet er soms een gat door de gevel of het dak. Dat werk, en het plaatsen of vervangen van een centrale ventilatiebox, laten we aan een ventilatie- of bouwbedrijf; wij zorgen voor de elektrische aansluiting.</p>

<h2>Warme vloer en <em>handdoekradiator.</em></h2>
<p><strong>Elektrische vloerverwarming</strong> is een dunne mat van 3 tot 5 mm onder de tegels, meestal 100 tot 150 watt per m² (Selectra). In een badkamer van 5 m² is dat zo'n 750 watt als alles aanstaat. Dat is genoeg voor warme tegels, maar zelden om de badkamer alleen daarmee op temperatuur te krijgen; reken erop dat er een radiator of handdoekradiator blijft. Wat wij erbij doen:</p>
<ul class="checks">
  <li>{check}<span><strong>Aansluitpunt en thermostaat buiten de zones</strong> rond bad en douche, op een groep met aardlekbeveiliging.</span></li>
  <li>{check}<span><strong>Een vloersensor</strong> tussen de verwarmingslussen, niet onder het badmeubel of vlak bij de muur. We tekenen in waar hij ligt.</span></li>
  <li>{check}<span><strong>Weerstand meten vóór en na het tegelen,</strong> want een beschadigde draad is na het tegelen niet meer te repareren zonder de vloer eruit te halen.</span></li>
  <li>{check}<span><strong>Een klokthermostaat.</strong> Een elektrische mat is binnen ongeveer een half uur warm, dus aanzetten als u hem nodig heeft is goedkoper dan de hele dag laag stoken (Selectra).</span></li>
</ul>
<p>Een <strong>elektrische handdoekradiator</strong> heeft vaak een vermogen tussen 300 en 750 watt en hoort niet in zone 1; in zone 2 moet hij minimaal IP44 zijn (Elektramat). Wij maken een vast aansluitpunt achter de radiator, zonder snoer langs de muur. Wilt u liever een paneel aan de muur of het plafond? Kijk dan bij <a href="/infraroodpanelen-aansluiten-rotterdam/">infraroodpanelen aansluiten</a>.</p>

<h2>Huurwoning, <em>flat of VvE.</em></h2>
<p>Huurt u? Vraag dan eerst toestemming aan de verhuurder voor vaste aanpassingen zoals extra stopcontacten, spots of vloerverwarming. In een flat of portiekwoning loopt de afvoer van de ventilatie vaak via een gezamenlijk kanaal; daar mag u niet zomaar een eigen ventilator op aansluiten. Vraag dat na bij de VvE of de beheerder. Bent u verhuurder of beheerder? Kijk ook bij <a href="/elektricien-verhuurders-vve-rotterdam/">elektricien voor verhuurders en VvE's</a>.</p>

<h2>Zo <em>pakken we het aan.</em></h2>
<ol class="steps-list">
  <li><strong>Stuur via WhatsApp</strong> een foto van uw open meterkast, een foto of schets van de badkamer en wat u wilt: verlichting, spiegel, stopcontacten, ventilator, vloerverwarming.</li>
  <li><strong>Wij geven aan wat waar kan</strong> volgens de zones, of de meterkast het aankan, en u krijgt een duidelijke prijs vooraf.</li>
  <li><strong>Voor het tegelen</strong> leggen we de leidingen en inbouwdozen, en eventueel de vloerverwarming.</li>
  <li><strong>Na het tegelen</strong> monteren en testen we alles, inclusief de aardlekbeveiliging, en zetten op de groepenkast welke groep waarvoor is.</li>
</ol>
<p>Alles volgens NEN 1010, door verzekerde vakmensen. Lampen, spiegel en ventilator kiest u zelf; wij kijken graag vooraf mee of ze geschikt zijn voor de plek.</p>

<div class="note-box"><p><strong>Bronnen:</strong> GAMMA klusadvies, <a href="https://www.gamma.nl/klusadvies/a/elektra-badkamer-aansluiten" target="_blank" rel="noopener noreferrer">elektra in de badkamer</a>; Elektramat, <a href="https://www.elektramat.nl/kennisbank/badkamer-afzuiging/" target="_blank" rel="noopener noreferrer">afzuiging in de badkamer</a> en <a href="https://www.elektramat.nl/kennisbank/elektrische-verwarming-badkamer/" target="_blank" rel="noopener noreferrer">elektrische verwarming in de badkamer</a>; Selectra, <a href="https://selectra.nl/energie/verwarming/elektrische-vloerverwarming-badkamer" target="_blank" rel="noopener noreferrer">elektrische vloerverwarming in de badkamer</a>.</p></div>
""",
        "faq": [
            ("Mogen er spots boven de douche?",
             "Ja, maar alleen spots die daarvoor gemaakt zijn. Direct boven de douchebak of het bad, en bij een inloopdouche binnen 1,2 meter van de douchekop, is zone 1: daar alleen verlichting op 12 volt met minimaal IPX5. De transformator of driver komt buiten de zones."),
            ("Hoe ver moet een stopcontact van de douche af?",
             "Buiten zone 2, dus verder dan 60 cm van het bad of de douchecabine. Bij een inloopdouche zonder cabine buiten de 1,2 meter rond de douchekop. Het stopcontact moet geaard zijn en achter een aardlekschakelaar zitten."),
            ("Wanneer moet de elektricien komen bij een badkamerverbouwing?",
             "Het liefst twee keer: voor het tegelen om leidingen, inbouwdozen en eventueel vloerverwarming te leggen, en na het tegelen om lampen, schakelaars, stopcontacten en de ventilator te monteren en te testen."),
            ("Kan elektrische vloerverwarming onder mijn bestaande tegels?",
             "Nee. Een verwarmingsmat komt onder een nieuwe tegelvloer. Gaat de vloer er toch uit bij de verbouwing, dan is dit het moment."),
            ("Is vloerverwarming genoeg om de badkamer te verwarmen?",
             "Meestal niet als enige bron. Een mat geeft warme tegels, maar een badkamer met een buitenmuur of raam heeft vaak ook een radiator of handdoekradiator nodig."),
            ("Kan de ventilator vanzelf blijven draaien na het douchen?",
             "Ja, met een ventilator met nalooptimer of vochtsensor. Voor een nalooptimer leggen we een extra schakeldraad vanaf de lichtschakelaar, het liefst voordat de tegels erop gaan."),
            ("Mag de wasmachine in de badkamer staan?",
             "Ja, als het stopcontact buiten de zones rond bad en douche zit, geaard is en achter een aardlekschakelaar zit. We geven de wasmachine bij voorkeur een eigen groep."),
            ("Mijn badkamer zit op een groep zonder aardlekschakelaar. Is dat een probleem?",
             "In een natte ruimte is een aardlekschakelaar van 30 mA de belangrijkste bescherming. Bij een verbouwing plaatsen we die eerst, of vervangen we de groepenkast als die verouderd is."),
            ("Wat kost de elektra voor een nieuwe badkamer?",
             "Dat hangt af van wat er komt: aantal lampen en spots, stopcontacten, ventilator, vloerverwarming en of er een groep bij moet. Stuur foto's van de badkamer en de meterkast via WhatsApp, dan krijgt u vooraf een duidelijke prijs."),
        ],
    },
    # ---------------------------------------------------------- STOPCONTACT
    {
        "slug": "stopcontact-plaatsen-rotterdam",
        "short": "Stopcontact plaatsen",
        "sub": "Extra of verplaatste stopcontacten en schakelaars.",
        "title": "Stopcontact plaatsen of verplaatsen Rotterdam | AlleKlussers",
        "desc": "Stopcontact laten plaatsen of verplaatsen in Rotterdam, of doet een stopcontact het niet? Geaard, badkamer en keuken, binnen en buiten. Prijs vooraf.",
        "service": "Stopcontacten en schakelaars plaatsen",
        "char": "dosie",
        "say": "“Te weinig stopcontacten? Niet meer.”",
        "eyebrow": "Stopcontacten en schakelaars",
        "h1": "Stopcontact plaatsen in <em>Rotterdam.</em>",
        "lede": "Extra stopcontacten, verplaatsen na een verbouwing of een stopcontact dat het niet meer doet. Binnen en buiten, veilig aangesloten.",
        "body": """
<h2>Wat wij <em>voor u doen.</em></h2>
<ul class="checks">
  <li>{check}<span><strong>Extra stopcontacten</strong> waar u ze nodig heeft, of een enkel stopcontact dubbel maken.</span></li>
  <li>{check}<span><strong>Stopcontacten en schakelaars verplaatsen,</strong> bijvoorbeeld na een verbouwing of voor een nieuwe keuken.</span></li>
  <li>{check}<span><strong>Een stopcontact dat het niet doet</strong> nakijken en repareren of vervangen.</span></li>
  <li>{check}<span><strong>Geaarde stopcontacten</strong> waar dat kan, en op verzoek met kinderbeveiliging of USB.</span></li>
  <li>{check}<span><strong>Buitenstopcontacten</strong> voor tuin, balkon of terras, spatwaterdicht. Zie <a href="/buitenverlichting-tuinstopcontact-rotterdam/">tuinstopcontact en buitenverlichting</a>.</span></li>
  <li>{check}<span><strong>Aansluitingen voor zware apparaten</strong> zoals wasmachine, droger, vaatwasser en kookplaat, op een <a href="/groep-bijplaatsen-rotterdam/">eigen groep</a>.</span></li>
</ul>

<h2>Stopcontact doet het niet? <em>Eerst dit.</em></h2>
<p>Vaak zit het probleem niet in het stopcontact zelf. Loop deze punten na voordat u ons een bericht stuurt:</p>
<ol class="steps-list">
  <li><strong>Probeer een ander apparaat.</strong> Een lamp of telefoonlader is genoeg. Werkt die wel, dan ligt het aan het apparaat of de stekkerdoos.</li>
  <li><strong>Kijk naar de andere stopcontacten in de kamer.</strong> Doen die het ook niet, dan is waarschijnlijk de hele groep uitgevallen.</li>
  <li><strong>Kijk in de meterkast.</strong> Staat een groep of aardlekschakelaar omlaag? Haal de stekkers uit de stopcontacten op die groep en zet de schakelaar weer omhoog. Slaat hij meteen weer door, lees dan onze pagina over de <a href="/aardlekschakelaar-rotterdam/">aardlekschakelaar</a>.</li>
  <li><strong>Zit er een lichtschakelaar op?</strong> Sommige stopcontacten zijn geschakeld, bijvoorbeeld voor een staande lamp. Dan krijgt het stopcontact alleen stroom als de schakelaar aan staat.</li>
  <li><strong>Buitenstopcontact?</strong> Vocht is een veelvoorkomende oorzaak. Gebruik het niet meer tot het is nagekeken.</li>
</ol>
<div class="note-box"><p><strong>Stop direct als het stopcontact warm wordt, verkleurd is, knettert of naar brand ruikt.</strong> Haal de stekker eruit als dat veilig kan, zet de groep in de meterkast uit en gebruik het stopcontact niet meer. Bij rook of vuur belt u 112.</p></div>
<p>Lukt het niet, of valt een groep steeds uit? Stuur een berichtje via WhatsApp, eventueel met een foto van het stopcontact en de meterkast. Meer over uitval van groepen staat op onze pagina over <a href="/storing-elektra-rotterdam/">storingen</a>.</p>

<h2>Stopcontact verplaatsen: <em>hoe gaat dat?</em></h2>
<p>In de meeste woningen lopen de draden door buizen in de muur. Bij verplaatsen kijken we eerst hoe de leiding loopt en waar de dichtstbijzijnde aansluiting zit. Daarna zijn er grofweg drie manieren:</p>
<ul class="checks">
  <li>{check}<span><strong>Een nieuwe route in de muur</strong> (inbouw). De kabel verdwijnt in de muur; daarna moet de sleuf worden dichtgesmeerd.</span></li>
  <li>{check}<span><strong>Een nette goot op de muur</strong> (opbouw). Sneller en zonder breekwerk, handig in huurwoningen en betonnen muren.</span></li>
  <li>{check}<span><strong>Via de vloer of het plafond,</strong> als daar ruimte is, bijvoorbeeld bij een houten vloer.</span></li>
</ul>
<p>Het oude stopcontact halen we weg of we dekken het netjes af. Verbindingen verdwijnen nooit achter het stucwerk: een las komt altijd in een doos die bereikbaar blijft.</p>

<h2>Geaard <em>of niet?</em></h2>
<p>Apparaten met een aardesymbool, zoals een wasmachine, koelkast of waterkoker, moeten op een geaard stopcontact. In oudere woningen in Rotterdam komen we nog kamers tegen waar geen aardedraad naar het stopcontact loopt. Een geaard stopcontact op een leiding zonder aarde geeft schijnveiligheid: het lijkt geaard, maar is het niet. We kijken daarom eerst of er een aardedraad is. Is die er niet, dan bespreken we of een nieuwe leiding of nieuwe <a href="/bedrading-vervangen-rotterdam/">bedrading</a> nodig is.</p>

<h2>Badkamer <em>en keuken.</em></h2>
<p>In de badkamer gelden strenge regels. Rond het bad en de douche zijn zones; tot 60 centimeter naast het bad of de douchecabine mag geen stopcontact. Daarbuiten mag het wel, maar alleen geaard en achter een aardlekschakelaar. Verbouwt u de badkamer, lees dan <a href="/elektra-badkamer-rotterdam/">elektra in de badkamer</a>. In de keuken zitten stopcontacten boven het aanrecht meestal op ongeveer 105 centimeter hoogte. Zware keukenapparaten, zoals een oven, vaatwasser of <a href="/inductiekookplaat-aansluiten-rotterdam/">inductiekookplaat</a>, horen op een eigen groep.</p>
<div class="note-box"><p><strong>Bronnen:</strong> GAMMA klusadvies over <a href="https://www.gamma.nl/klusadvies/a/elektra-badkamer-aansluiten" target="_blank" rel="noopener noreferrer">elektra in de badkamer</a> en <a href="https://www.gamma.nl/klusadvies/a/regels-elektra-aanleggen" target="_blank" rel="noopener noreferrer">de basisregels voor elektra aanleggen</a>.</p></div>

<div class="note-box"><p><strong>Veel stekkerdozen achter elkaar?</strong> Dat kan een groep overbelasten en is een bekende oorzaak van brand. Een paar extra stopcontacten zijn veiliger en netter.</p></div>

<h2>Inbouw of <em>opbouw?</em></h2>
<p>Bij inbouw zit het stopcontact in de muur en ziet u de kabel niet. Bij opbouw komt de kabel in een nette goot op de muur; dat is sneller en vaak voordeliger. We bespreken samen wat het beste past bij uw muur en uw budget.</p>
""",
        "faq": [
            ("Kan er overal een stopcontact bij?",
             "Bijna altijd. We kijken waar de dichtstbijzijnde aansluiting zit en welke route de kabel kan nemen."),
            ("Hoeveel werk is een stopcontact verplaatsen?",
             "Dat hangt af van de afstand en de muur. Een paar decimeter opzij via de bestaande buis is vaak snel gedaan. Een nieuwe route door een betonnen muur kost meer tijd; dan is een nette goot op de muur soms handiger. U krijgt vooraf een prijs."),
            ("Mijn stopcontact doet het niet meer. Wat nu?",
             "Probeer eerst een ander apparaat en kijk of de andere stopcontacten in de kamer het doen. Kijk daarna in de meterkast of er een groep of aardlekschakelaar omlaag staat. Wordt het stopcontact warm, is het verkleurd of ruikt het naar brand, gebruik het dan niet meer en zet de groep uit."),
            ("Mag ik een geaard stopcontact plaatsen als er geen aarde is?",
             "Liever niet. Dan lijkt het stopcontact geaard, maar is het dat niet. We kijken eerst of er een aardedraad naar het stopcontact loopt. Is die er niet, dan bespreken we een nieuwe leiding."),
            ("Mag er een stopcontact in de badkamer?",
             "Ja, maar niet vlak bij het bad of de douche. Tot 60 centimeter naast het bad of de douchecabine mag er geen stopcontact zitten. Verder weg mag het wel, geaard en achter een aardlekschakelaar."),
            ("Heeft mijn wasmachine een eigen groep nodig?",
             "Voor zware apparaten zoals een wasmachine, droger of vaatwasser is een eigen groep aan te raden. Zo raakt de groep niet overbelast."),
            ("Kunnen jullie een buitenstopcontact plaatsen?",
             "Ja, met een spatwaterdicht stopcontact en de juiste beveiliging in de meterkast."),
            ("Wat kost een extra stopcontact?",
             "Dat hangt af van de afstand tot de dichtstbijzijnde aansluiting en of het inbouw of opbouw wordt. U krijgt vooraf een prijs."),
        ],
    },
    # ---------------------------------------------- BUITENVERLICHTING / TUIN
    {
        "slug": "buitenverlichting-tuinstopcontact-rotterdam",
        "short": "Buitenverlichting en tuinstopcontact",
        "sub": "Licht bij de deur en in de tuin, stroom buiten en in de schuur.",
        "title": "Buitenverlichting en tuinstopcontact Rotterdam | AlleKlussers",
        "desc": "Buitenlamp, tuinverlichting of een stopcontact in de tuin of op het balkon in Rotterdam? Waterdicht, op aardlekbeveiliging en volgens NEN 1010. Prijs vooraf.",
        "service": "Buitenverlichting en tuinstopcontact aanleggen",
        "char": "lampje",
        "say": "“Donker buiten? Ik zet de tuin aan.”",
        "eyebrow": "Buitenverlichting en tuin",
        "h1": "Buitenverlichting en tuinstopcontact in <em>Rotterdam.</em>",
        "lede": "Licht bij de voordeur en het achterom, sfeer in de tuin en een stopcontact buiten voor de heggenschaar of de kerstverlichting. Zonder verlengsnoer door het raam, en goed afgedicht tegen regen.",
        "body": """
<h2>Stroom buiten, <em>maar dan veilig.</em></h2>
<p>Van november tot en met februari is het vroeg donker. Dan merkt u pas hoe weinig licht er bij de voordeur, op het tuinpad of bij de schuur is. Ook de politie raadt aan om bij een achterom te zorgen voor verlichting in de tuin, en om met een automatische schakelaar licht te laten branden als u niet thuis bent (<a href="https://www.politie.nl/informatie/tips-om-woninginbraak-te-voorkomen.html" target="_blank" rel="noopener noreferrer">politie.nl</a>).</p>
<p>Wie buiten stroom nodig heeft, pakt vaak een verlengsnoer door het raam of de achterdeur. Dat gaat lang goed, tot het snoer bekneld raakt in de deur, de stekkerverbinding in het natte gras ligt of een opgerolde haspel warm wordt. Een vast buitenpunt is veiliger en een stuk handiger.</p>

<h2>Wat wij <em>voor u aanleggen.</em></h2>
<ul class="checks">
  <li>{check}<span><strong>Buitenlamp bij de voordeur, de gevel of het achterom,</strong> met een schemerschakelaar of bewegingsmelder als u dat wilt.</span></li>
  <li>{check}<span><strong>Tuinverlichting:</strong> wandlampen, staande lampen langs het pad, grondspots in de border of verlichting bij het terras.</span></li>
  <li>{check}<span><strong>Tuinstopcontact</strong> aan de gevel, of op een paal achter in de tuin, voor het gereedschap, de vijverpomp of de kerstverlichting.</span></li>
  <li>{check}<span><strong>Stroom naar de schuur of het tuinhuis:</strong> een kabel door de grond, met licht en stopcontacten in de schuur zelf.</span></li>
  <li>{check}<span><strong>Stopcontact of lamp op het balkon,</strong> ook in een flat of portiekwoning.</span></li>
  <li>{check}<span><strong>Een schakelaar binnen</strong> waarmee u het buitenstopcontact of de tuinverlichting uitzet als u hem niet gebruikt.</span></li>
</ul>

<h2>Waar wij <em>op letten.</em></h2>
<ul class="checks">
  <li>{check}<span><strong>De juiste IP-waarde.</strong> Het getal achter IP zegt hoe goed een lamp of stopcontact tegen stof en water kan. Onder een afdak of luifel is IP44 (spatwaterdicht) vaak genoeg. Staat het vol in de regen, dan kiezen we een hogere klasse zoals IP65. Grondspots die in de grond liggen hebben meestal IP67 nodig.</span></li>
  <li>{check}<span><strong>Aardlekbeveiliging.</strong> Alles buiten komt op een groep met een aardlekschakelaar van 30 mA. Waar het kan krijgt het buitenwerk een eigen groep of een aardlekautomaat. Komt er toch vocht in een buitenlamp, dan valt alleen die groep uit en niet het halve huis. Lees meer over <a href="/groep-bijplaatsen-rotterdam/">een groep bijplaatsen</a>.</span></li>
  <li>{check}<span><strong>Een kabel die tegen de grond kan.</strong> Voor een punt achter in de tuin gebruiken we grondkabel, op zo'n 50 tot 60 centimeter diepte. Waar de kabel uit de grond komt, loopt hij door een stevige buis, zodat een schop of de grasmaaier hem niet raakt.</span></li>
  <li>{check}<span><strong>Hoogte en deksel.</strong> Een tuinstopcontact komt minstens zo'n 30 centimeter boven de grond, met een klapdeksel dat zichzelf sluit, zodat er geen plensbui of spatwater in komt.</span></li>
  <li>{check}<span><strong>Een dichte doorvoer.</strong> Het gat waar de kabel door de gevel gaat, dichten we goed af. Zo loopt er geen water langs de kabel naar binnen en kruipt er geen vocht in de muur.</span></li>
</ul>
<div class="note-box"><p><strong>Slaat uw aardlekschakelaar nu al door bij regen?</strong> Dan zit er waarschijnlijk vocht in een bestaande buitenlamp of buitenstopcontact. Zet die groep zo nodig uit en lees eerst <a href="/aardlekschakelaar-rotterdam/">aardlek slaat door</a>. Wij zoeken de oorzaak en vervangen het punt door een goed afgedicht exemplaar.</p></div>

<h2>Schemerschakelaar, bewegingsmelder <em>of tijdklok?</em></h2>
<ul class="checks">
  <li>{check}<span><strong>Schemerschakelaar:</strong> de lamp gaat aan als het donker wordt en uit als het licht wordt. Fijn bij de voordeur en het huisnummer, zodat bezoek en bezorgers uw deur vinden.</span></li>
  <li>{check}<span><strong>Bewegingsmelder:</strong> het licht gaat alleen aan als iemand langsloopt. Handig bij het achterom, de schuur en de vuilcontainers, en zuinig omdat de lamp meestal uit is.</span></li>
  <li>{check}<span><strong>Tijdschakelaar of slimme schakelaar:</strong> de tuinverlichting brandt op vaste tijden, of u zet hem aan met uw telefoon. Zo lijkt het ook thuis als u weg bent.</span></li>
</ul>
<p>Sommige buitenlampen combineren dit: de hele avond zacht licht, en fel licht zodra er beweging is. Een tip voor in de stad: richt de lamp naar beneden en niet op de ramen van de buren. Dat geeft minder verblinding en meer licht op het pad.</p>

<h2>Buiten in <em>Rotterdam.</em></h2>
<p>In Rotterdam zijn de tuinen vaak smal en diep, met een schuur achterin en een achterpad of steeg erachter. Juist daar is het 's avonds donker. Een lamp met bewegingsmelder bij de poort en een stopcontact in de schuur lossen dat in één afspraak op. In portiekflats en galerijwoningen gaat het meestal om een stopcontact of lamp op het balkon.</p>
<p>Huurt u, of hoort de gevel bij een VvE? Vraag dan eerst toestemming aan de verhuurder of de VvE voordat we iets aan de buitenmuur bevestigen. Verhuurders en VvE's helpen we ook rechtstreeks; zie <a href="/elektricien-verhuurders-vve-rotterdam/">elektricien voor verhuurders en VvE's</a>.</p>

<h2>Zo <em>pakken we het aan.</em></h2>
<ol class="steps-list">
  <li><strong>Stuur ons via WhatsApp foto's</strong> van de plek buiten en van uw meterkast, en vertel wat u wilt: hoeveel lampen, welk stopcontact, en hoe ver de schuur van het huis is.</li>
  <li><strong>U krijgt een duidelijke prijs vooraf,</strong> met de kabelroute erbij: langs de gevel, door de grond of via de kruipruimte.</li>
  <li><strong>Wij leggen alles aan</strong> en sluiten het aan in de meterkast. Heeft u de lampen zelf gekocht, dan kijken we vooraf of ze geschikt zijn voor de plek. Graaft u liever zelf de sleuf voor de grondkabel, dan spreken we af hoe diep en waar.</li>
  <li><strong>We testen de aardlekbeveiliging,</strong> stellen de schemerschakelaar of bewegingsmelder met u in en zetten op de groepenkast welke groep voor buiten is.</li>
</ol>
<p>Alles volgens NEN 1010, door verzekerde vakmensen. Wilt u binnen ook meer licht of extra stopcontacten? Kijk dan bij <a href="/lampen-ophangen-rotterdam/">lampen ophangen</a> en <a href="/stopcontact-plaatsen-rotterdam/">stopcontact plaatsen</a>. Dat combineren we graag in dezelfde afspraak.</p>
""",
        "faq": [
            ("Welke IP-waarde heeft een buitenlamp nodig?",
             "Onder een afdak of luifel is IP44 vaak genoeg. Staat de lamp of het stopcontact vol in de regen, kies dan een hogere klasse zoals IP65. Grondspots die in de grond liggen hebben meestal IP67 nodig. Het staat op de verpakking of op de lamp zelf."),
            ("Kan een buitenstopcontact op een bestaande groep?",
             "Vaak wel, als die groep niet al vol zit en achter een aardlekschakelaar hangt. Gebruikt u buiten zware apparaten, zoals een hogedrukreiniger of een elektrische terrasverwarmer, dan is een eigen groep beter. Dan valt binnen ook niets uit als er buiten iets misgaat."),
            ("Hoe diep moet een kabel in de tuin liggen?",
             "Een grondkabel leggen we op zo'n 50 tot 60 centimeter diepte, en waar hij uit de grond komt in een stevige buis. Zo blijft hij heel bij spitten en tuinwerk. Gewone installatiekabel van binnen hoort niet in de grond."),
            ("Kan ik mijn kerstverlichting op het buitenstopcontact aansluiten?",
             "Ja, als de verlichting geschikt is voor buiten. Gebruik buiten ook een verlengsnoer dat daarvoor bedoeld is, en leg stekkerverbindingen niet in het gras of in een plas. Slaat de aardlek door als het regent, haal de verlichting er dan af en kijk welke verbinding nat is geworden."),
            ("Bewegingsmelder of schemerschakelaar: wat is beter?",
             "Bij de voordeur is een schemerschakelaar fijn: dan brandt het licht de hele avond. Bij het achterom, de schuur en de containers is een bewegingsmelder handiger en zuiniger. Er zijn ook lampen die beide doen."),
            ("Kunnen jullie stroom naar mijn schuur of tuinhuis aanleggen?",
             "Ja. We leggen een grondkabel van het huis naar de schuur en maken daar licht en stopcontacten. Voor een werkplaats of een vriezer in de schuur geven we de schuur een eigen groep in de meterkast."),
            ("Ik woon in een flat. Kan ik een stopcontact op mijn balkon krijgen?",
             "Meestal wel. Huurt u of hoort de gevel bij de VvE, vraag dan eerst toestemming. Daarna kijken we waar de dichtstbijzijnde aansluiting binnen zit en hoe de kabel netjes naar buiten kan."),
            ("Wat kost buitenverlichting of een tuinstopcontact?",
             "Dat hangt vooral af van de afstand tot de meterkast en of er een kabel door de grond moet. Stuur foto's van de plek en de meterkast, dan krijgt u vooraf een duidelijke prijs."),
        ],
    },
    # ------------------------------------------------------------ BEDRADING
    {
        "slug": "bedrading-vervangen-rotterdam",
        "short": "Bedrading en aansluitingen",
        "sub": "Oude bedrading vervangen, aansluitingen voor de keuken.",
        "title": "Bedrading vervangen Rotterdam | Aansluitingen | AlleKlussers",
        "desc": "Oude bedrading vervangen in Rotterdam? Signalen, alles of een deel vervangen, nieuwe draden door bestaande buizen en aansluitingen voor de keuken. Prijs vooraf.",
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
  <li>{check}<span><strong>Andere draadkleuren dan nu gebruikelijk.</strong> Tegenwoordig is de fase bruin, de nul blauw, de aarde geel-groen en de schakeldraad zwart. Ziet u andere kleuren, dan is de installatie vaak oud. Ga er nooit van uit welke draad wat is; dat meten wij.</span></li>
  <li>{check}<span><strong>Groepen die vaak doorslaan</strong> of een brandlucht bij een stopcontact.</span></li>
</ul>
<div class="note-box"><p><strong>Ruikt u een brandlucht of is een stopcontact heet?</strong> Gebruik het niet meer en zet de groep in de meterkast uit. Bij rook of vuur belt u 112.</p></div>

<h2>Alles vervangen <em>of een deel?</em></h2>
<p>Niet elke oude installatie hoeft er helemaal uit. We meten de installatie groep voor groep door en kijken naar de staat van de draden, de aarding en de groepenkast. Daarna hoort u eerlijk wat echt vervangen moet worden en wat nog goed is. Vaak is het verstandig om eerst de groepen aan te pakken waar zware apparaten op zitten, zoals de keuken en de wasmachine.</p>
<p>Is de groepenkast zelf ook oud, bijvoorbeeld met draaizekeringen of zonder aardlekschakelaar? Dan combineren we het vervangen van de bedrading met een <a href="/groepenkast-vervangen-rotterdam/">nieuwe groepenkast</a>.</p>

<h2>Hoe we <em>het aanpakken.</em></h2>
<p>In de meeste woningen lopen de draden door buizen in de muren en plafonds. Elke kamer heeft een centraaldoos, meestal in het plafond, van waaruit de stroom naar de lampen, schakelaars en stopcontacten gaat. Waar het kan, trekken we de nieuwe draden door de bestaande buizen; dan hoeven de muren niet open. Waar dat niet lukt, frezen we een nieuwe sleuf of gebruiken we een nette goot op de muur. Dat bespreken we vooraf.</p>
<p>Voor stopcontacten in een woning gebruiken we draad van 2,5 mm². Aftakkingen en verbindingen komen in een centraaldoos of lasdoos die bereikbaar blijft.</p>
<div class="note-box"><p><strong>Bron:</strong> Elektramat kennisbank, <a href="https://www.elektramat.nl/kennisbank/elektriciteit-aanleggen" target="_blank" rel="noopener noreferrer">elektriciteitsleiding aanleggen</a>.</p></div>

<h2>Nieuwe keuken <em>of nieuwe apparaten?</em></h2>
<p>Gaat u een keuken plaatsen of verbouwen? Dan leggen we de aansluitingen aan voor oven, kookplaat, vaatwasser, koelkast en afzuigkap, ieder op de juiste groep. Een <a href="/inductiekookplaat-aansluiten-rotterdam/">inductiekookplaat</a>, droger, warmtepomp of <a href="/laadpaal-installeren-rotterdam/">laadpaal</a> vraagt om een eigen groep; oude bedrading is daar niet op gemaakt. Zie ook <a href="/groep-bijplaatsen-rotterdam/">een groep bijplaatsen</a>.</p>

<h2>Huur, koop <em>of verkoop?</em></h2>
<p>Huurt u, dan is de vaste elektrische installatie van de verhuurder. Meld oude of onveilige bedrading bij uw verhuurder of woningcorporatie. Koopt u een ouder huis, dan geeft een <a href="/elektra-keuring-rotterdam/">elektra keuring</a> vooraf inzicht in de staat van de bedrading. Verhuurders en VvE's kunnen ons ook rechtstreeks inschakelen; zie onze <a href="/elektricien-verhuurders-vve-rotterdam/">pagina voor verhuurders</a>.</p>
""",
        "faq": [
            ("Moet in een oud huis alle bedrading vervangen worden?",
             "Niet altijd. We meten de installatie groep voor groep door. Daarna weet u precies wat nodig is. Soms is vervangen van een deel genoeg."),
            ("Moeten de muren open?",
             "Vaak kunnen we via de bestaande buizen nieuwe draden trekken. Als frezen nodig is, bespreken we dat vooraf en werken we het netjes af. Een goot op de muur is ook mogelijk."),
            ("Welke kleuren hebben elektriciteitsdraden tegenwoordig?",
             "De fase is bruin, de nul blauw, de aarde geel-groen en de schakeldraad zwart. In oude installaties kunnen andere kleuren zitten. Ga er nooit vanuit welke draad wat is; laat het meten."),
            ("Is bedrading met een stoffen omhulsel gevaarlijk?",
             "Het omhulsel kan na veel jaren broos worden, waardoor draden bloot kunnen komen te liggen. Laat het controleren, zeker als er ook verkleurde stopcontacten zijn of groepen vaak doorslaan."),
            ("Ik huur mijn woning. Wie betaalt nieuwe bedrading?",
             "De vaste elektrische installatie is van de verhuurder. Meld het bij uw verhuurder of woningcorporatie. Werk dat u zelf heeft laten aanbrengen, onderhoudt u zelf."),
            ("Kunnen jullie de elektra voor mijn nieuwe keuken aanleggen?",
             "Ja. Stuur ons de keukentekening, dan zorgen we dat alle apparaten de juiste aansluiting en groep krijgen."),
        ],
    },
    # -------------------------------------------------------------- KEURING
    {
        "slug": "elektra-keuring-rotterdam",
        "short": "Elektra keuring",
        "sub": "Controle bij aankoop, verhuur of na een verbouwing.",
        "title": "Keuring elektrische installatie Rotterdam | AlleKlussers",
        "desc": "Keuring van de elektrische installatie in uw woning in Rotterdam: bij aankoop, verkoop, verhuur of na een verbouwing. Wij meten na en geven helder advies.",
        "service": "Keuring van elektrische installaties",
        "char": "schildje",
        "say": "“Veilig of niet? Ik zoek het uit.”",
        "eyebrow": "Keuring en veiligheid",
        "h1": "Keuring elektrische installatie in <em>Rotterdam.</em>",
        "lede": "Een elektra keuring: een controle van de elektrische installatie in uw woning of huurwoning, met metingen waar nodig en een helder overzicht van wat in orde is, wat aandacht nodig heeft en wat meteen moet.",
        "body": """
<h2>Wanneer is een keuring <em>verstandig?</em></h2>
<ul class="checks">
  <li>{check}<span><strong>Bij aankoop van een woning,</strong> zodat u voor de koop weet of er kosten aankomen aan de elektra.</span></li>
  <li>{check}<span><strong>Voordat u uw woning verkoopt,</strong> zodat u weet wat u aan de koper moet melden, of het vooraf laat herstellen.</span></li>
  <li>{check}<span><strong>Bij verhuur en bij een wisseling van huurder,</strong> zodat de nieuwe huurder in een veilige woning start. Lees ook wat we doen <a href="/elektricien-verhuurders-vve-rotterdam/">voor verhuurders en VvE's</a>.</span></li>
  <li>{check}<span><strong>Na een verbouwing,</strong> of als een vorige eigenaar of een klusser zelf aan de elektra heeft gewerkt.</span></li>
  <li>{check}<span><strong>Voordat u zwaardere apparaten neemt,</strong> zoals een inductiekookplaat, warmtepomp of laadpaal. Dan weten we of de groepenkast en de aansluiting dat aankunnen.</span></li>
  <li>{check}<span><strong>In een ouder huis,</strong> of als groepen of de aardlekschakelaar vaak doorslaan.</span></li>
</ul>

<h2>Is een keuring <em>verplicht?</em></h2>
<p>Voor woningen is er in Nederland geen wettelijke keuringsplicht voor de elektra, ook niet bij verkoop of verhuur. Wel is de eigenaar verantwoordelijk voor een veilige installatie. Voor een vrijwillige veiligheidscontrole van bestaande woningen bestaat sinds 2005 de NTA 8025, ook bekend als de 'Woning-APK' (<a href="https://www.brandveilig.com/nieuws/nieuwe-woning-apk-nen-8025-op-komst-54008" target="_blank" rel="noopener noreferrer">brandveilig.com</a>).</p>
<p>Voor bedrijfspanden ligt dat anders. Daar vraagt de verzekeraar of de Arbowet soms een SCIOS-inspectie, zoals Scope 8 of Scope 10, door een bedrijf dat volgens de SCIOS-regels keurt (<a href="https://www.unive.nl/zakelijk/blog/hoe-zit-het-ook-alweer-met-de-verplichte-elektrakeuringen" target="_blank" rel="noopener noreferrer">Univé</a>). De controle op deze pagina is bedoeld voor woningen en is geen SCIOS-inspectie. Punten die uit zo'n inspectie komen, kunnen we wel voor u herstellen.</p>
<div class="note-box"><p><strong>In België wel verplicht.</strong> Ziet u bij het zoeken naar een 'elektrische keuring' vooral Belgische sites? In België moet een woning met een oude installatie bij verkoop worden gekeurd door een erkend keuringsorganisme, volgens het AREI (<a href="https://www.vlaanderen.be/bouwen-wonen-en-energie/elektriciteit-en-aardgas/keuring-van-uw-elektrische-installatie-arei" target="_blank" rel="noopener noreferrer">vlaanderen.be</a>). In Nederland bestaat zo'n verplichting niet. Een keuring is hier een eigen keuze van de koper, verkoper of verhuurder.</p></div>

<h2>NEN 1010-inspectie <em>of Woning-APK?</em></h2>
<p>Wie zoekt naar een 'NEN 1010-inspectie' voor een woning, bedoelt meestal een controle of de elektra veilig is en volgens de norm is aangelegd. Twee normen spelen daarbij een rol:</p>
<ul class="checks">
  <li>{check}<span><strong>NEN 1010</strong> is de norm voor het aanleggen van elektrische installaties. Nieuwe woningen worden volgens NEN 1010 opgeleverd. Bij een kleine reparatie mag u volgens NEN voldoen aan de eisen die golden toen de woning werd gebouwd; bij een ingrijpende renovatie moet de installatie aan de eisen van nu voldoen.</span></li>
  <li>{check}<span><strong>NEN 8025, de 'Woning-APK',</strong> is een korte, periodieke inspectie van de technische installaties in bestaande woningen: gas, water en elektra. De overheid heeft deze norm niet verplicht gesteld. Verhuurders, corporaties en VvE's gebruiken haar om aan te tonen dat ze zorgen voor de veiligheid van hun bewoners.</span></li>
</ul>
<p>Onze keuring op deze pagina is een praktische controle van alleen de elektra in uw woning, met metingen en een helder overzicht van wat goed is en wat aandacht nodig heeft. Werk dat we daarna uitvoeren, doen we volgens NEN 1010.</p>
<div class="note-box"><p><strong>Bron:</strong> NEN, <a href="https://www.nen.nl/elektrotechniek/inspecteren/woning-apk" target="_blank" rel="noopener noreferrer">Woning-APK: inspecteren met NEN 8025</a>.</p></div>

<h2>Bij aankoop: meer dan <em>de bouwkundige keuring.</em></h2>
<p>Een bouwkundige keuring is een globale, visuele inspectie. De elektra wordt daarbij meestal alleen bekeken, niet doorgemeten. Dat blijkt ook uit een uitspraak van de Geschillencommissie: een koper ontdekte pas na de overdracht problemen met de elektra, en de bouwkundig keurder was daar niet verantwoordelijk voor (<a href="https://www.degeschillencommissie.nl/uitspraken/gebreken-pas-na-aankoop-ontdekt-maar-keurder-niet-verantwoordelijk/" target="_blank" rel="noopener noreferrer">degeschillencommissie.nl</a>).</p>
<p>Bij een elektra keuring kijken we gericht naar de installatie: we openen de groepenkast, testen de aardlekbeveiliging en meten waar dat nodig is. Zo weet u of er een nieuwe groepenkast, extra groepen of nieuwe bedrading nodig is, en kunt u dat meenemen in uw beslissing en uw budget.</p>
<div class="note-box"><p><strong>Tip voor kopers:</strong> heeft u een voorbehoud voor een bouwkundige keuring, plan de elektra keuring dan in dezelfde periode, voordat die termijn verloopt. Vraag via de makelaar of de verkoper toestemming om de woning te bezoeken. Stuur ons alvast het adres, het bouwjaar en een foto van de meterkast uit de advertentie.</p></div>

<h2>Bij verkoop: <em>wat moet u melden?</em></h2>
<p>Verkoopt u uw woning, dan heeft u een mededelingsplicht. Weet u van een gebrek dat het normale gebruik van de woning in de weg staat, dan moet u dat aan de koper vertellen. Doet u dat niet, dan bent u in beginsel aansprakelijk voor de schade die de koper daardoor lijdt (<a href="https://www.rechtspraak.nl/onderwerpen/verborgen-gebreken" target="_blank" rel="noopener noreferrer">Rechtspraak</a>). In de gewone NVM-koopovereenkomst verklaart de verkoper bovendien dat de koper mag verwachten dat de woning geschikt is voor normaal gebruik: veilig bewonen, zonder dat het woongenot wezenlijk wordt aangetast. Wat normaal is, hangt wel af van de leeftijd van het huis; een ouderdomsclausule kan uw aansprakelijkheid beperken (<a href="https://www.funda.nl/meer-weten/verkopen/je-rechten-en-plichten-als-verkoper/" target="_blank" rel="noopener noreferrer">funda</a>).</p>
<p>De koper heeft op zijn beurt een onderzoeksplicht: ziet hij signalen dat er iets mis is, dan moet hij daar vragen over stellen of het laten onderzoeken. Bij elektra zijn dat bijvoorbeeld draaistoppen, een kast zonder aardlekschakelaar, stopcontacten zonder randaarde of zichtbaar oude draad.</p>
<ul class="checks">
  <li>{check}<span><strong>Als verkoper</strong> weet u na een keuring precies wat er speelt. U kunt dat eerlijk melden in de vragenlijst voor de koper, of het vooraf laten herstellen. Gevaarlijke punten lossen we het liefst meteen op.</span></li>
  <li>{check}<span><strong>Als koper</strong> heeft u zwart op wit hoe de elektra ervoor staat, voordat uw voorbehoud verloopt. Dat helpt bij het onderhandelen en bij het plannen van uw budget.</span></li>
</ul>
<p>Dit is algemene informatie, geen juridisch advies. Twijfelt u wat u moet melden, vraag het dan aan uw makelaar of het Juridisch Loket.</p>

<h2>Bij verhuur en <em>mutatie.</em></h2>
<p>Gevaarlijke elektra in een huurwoning is een gebrek. In het Gebrekenboek van de Huurcommissie staat bijvoorbeeld 'een gevaarlijke situatie door losliggende leidingen en/of onvoldoende afscherming van bedrading' (<a href="https://www.huurcommissie.nl/site/binaries/site-content/collections/documents/2025/07/01/beleidsboek-gebreken/Gebrekenboek.pdf" target="_blank" rel="noopener noreferrer">Huurcommissie</a>). Volgens hetzelfde boek moet een huurder zelf het deel van de installatie onderhouden dat hij op eigen kosten heeft aangelegd.</p>
<p>Daarom is een controle bij de wisseling van huurder slim. U ziet wat de vertrekkende huurder heeft aangelegd of veranderd, zoals extra stopcontacten, een andere lamp of een losse groep, en of dat veilig is. Wat niet goed is, kunnen we in dezelfde periode herstellen, zodat de nieuwe huurder er meteen in kan.</p>

<h2>Wat wij <em>controleren.</em></h2>
<ul class="checks">
  <li>{check}<span><strong>De groepenkast:</strong> staat en leeftijd, verkleuring of warmteplekken, losse draden en of elke groep goed is aangegeven.</span></li>
  <li>{check}<span><strong>De aardlekbeveiliging:</strong> is er een aardlekschakelaar, hoeveel groepen hangen eraan en schakelt hij op tijd af bij een test. Meer daarover leest u bij <a href="/aardlekschakelaar-rotterdam/">aardlekschakelaar</a>.</span></li>
  <li>{check}<span><strong>De aarding:</strong> of er een goede aardverbinding is en of stopcontacten in de keuken, badkamer en bij de wasmachine randaarde hebben.</span></li>
  <li>{check}<span><strong>De bedrading:</strong> oude katoen- of canvasdraad, beschadigde isolatie en verdeeldozen. Vereniging Eigen Huis noemt katoenen isolatiedraad onveilig en niet meer toegestaan (<a href="https://www.eigenhuis.nl/huis-verbeteren/klussen/zorgen-voor-je-huis/elektrische-installatie-controleren" target="_blank" rel="noopener noreferrer">eigenhuis.nl</a>). Zie ook <a href="/bedrading-vervangen-rotterdam/">bedrading vervangen</a>.</span></li>
  <li>{check}<span><strong>Stopcontacten en schakelaars:</strong> los, gebarsten of verbrand, of te veel stekkerdozen achter elkaar.</span></li>
  <li>{check}<span><strong>De belasting:</strong> staan zware apparaten zoals de oven, vaatwasser en wasmachine samen op één groep, en is er ruimte voor meer. Is de aansluiting zelf te klein, dan leest u meer bij <a href="/meterkast-verzwaren-rotterdam/">meterkast verzwaren</a>.</span></li>
  <li>{check}<span><strong>Sporen van klussen:</strong> aanpassingen die niet volgens NEN 1010 zijn gedaan, zoals draden zonder kroonsteen of las, of een verkeerde draaddikte.</span></li>
</ul>

<h2>Oudere woningen <em>in Rotterdam.</em></h2>
<p>In Rotterdam staan veel vooroorlogse woningen, zoals in Noord, Kralingen, Delfshaven en delen van Zuid, en veel portiekflats uit de jaren vijftig en zestig. Daar komen we vaak dezelfde dingen tegen: een groepenkast met maar één aardlekschakelaar of zelfs geen, stopcontacten zonder randaarde in slaapkamers en gangen, en een installatie die in delen is uitgebreid. Dat hoeft niet meteen gevaarlijk te zijn, maar het is wel goed om te weten voordat u gaat verbouwen of verhuren.</p>

<h2>Wat u <em>krijgt.</em></h2>
<p>Na afloop krijgt u een overzicht in gewone taal. Per punt staat erbij of het in orde is, aandacht nodig heeft, of beter direct opgelost kan worden. Moet er iets verbeterd worden, dan krijgt u daar een duidelijke prijs vooraf voor. U beslist zelf of en wanneer u dat laat doen. Vindt de monteur iets dat echt gevaarlijk is, dan zegt hij dat meteen ter plekke.</p>

<h2>Zo <em>pakken we het aan.</em></h2>
<ol class="steps-list">
  <li><strong>Stuur ons via WhatsApp</strong> het adres of de wijk, het bouwjaar, waarvoor de keuring is (aankoop, verkoop, verhuur of uw eigen woning) en een foto van de meterkast als u die heeft.</li>
  <li><strong>U krijgt een duidelijke prijs vooraf</strong> en we plannen een moment. Bij aankoop stemmen we dat af met de makelaar of de verkoper.</li>
  <li><strong>Wij controleren de installatie.</strong> Voor sommige metingen gaat de stroom per groep even uit. Houd daar rekening mee met de computer en de vriezer.</li>
  <li><strong>U krijgt het overzicht en ons advies,</strong> en als u dat wilt een offerte voor het herstel.</li>
</ol>
<p>Alles volgens NEN 1010, door verzekerde vakmensen. Blijkt de groepenkast aan vervanging toe, kijk dan bij <a href="/groepenkast-vervangen-rotterdam/">groepenkast vervangen</a>.</p>
""",
        "faq": [
            ("Is een keuring van de elektrische installatie verplicht bij aankoop, verkoop of verhuur?",
             "Nee, voor woningen is er in Nederland geen wettelijke keuringsplicht. De eigenaar is wel verantwoordelijk voor een veilige installatie. Een keuring geeft u zekerheid voordat u koopt, verkoopt, verhuurt of gaat verbouwen."),
            ("Moet ik als verkoper gebreken aan de elektra melden?",
             "Ja, als u weet van een gebrek dat het normale gebruik van de woning in de weg staat, moet u dat aan de koper melden. Met een keuring weet u wat er speelt: u kunt het eerlijk melden of vooraf laten herstellen. Twijfelt u, vraag het dan aan uw makelaar of het Juridisch Loket."),
            ("In België is een elektrische keuring bij verkoop verplicht. Hier ook?",
             "Nee. In België moet een woning met een oude installatie bij verkoop worden gekeurd volgens het AREI. In Nederland bestaat die plicht niet; een keuring is hier een eigen keuze."),
            ("Wat is het verschil met een bouwkundige keuring?",
             "Een bouwkundige keuring is een globale, visuele inspectie van de hele woning. De elektra wordt daarbij meestal alleen bekeken. Bij een elektra keuring openen we de groepenkast, testen we de aardlekbeveiliging en meten we waar dat nodig is."),
            ("Hoe lang duurt een keuring?",
             "Dat hangt af van de grootte van de woning of het pand. Voor een gewone woning is het meestal binnen een paar uur klaar."),
            ("Moet de stroom eraf tijdens de keuring?",
             "Voor sommige metingen gaat de stroom per groep even uit. Dat duurt kort, maar zet de computer uit en houd de vriezer dicht."),
            ("Krijg ik een verslag?",
             "Ja, u krijgt een overzicht van wat we hebben gecontroleerd, wat we hebben gevonden en wat we adviseren. Per punt staat erbij hoe dringend het is."),
            ("Wat is het verschil tussen NEN 1010 en NEN 8025?",
             "NEN 1010 is de norm voor het aanleggen van elektrische installaties. NEN 8025, de 'Woning-APK', is een korte periodieke inspectie van gas, water en elektra in bestaande woningen. Die is niet verplicht, maar verhuurders gebruiken haar om hun zorgplicht aan te tonen."),
            ("Doen jullie ook een SCIOS Scope 8 of Scope 10 inspectie?",
             "Een SCIOS-inspectie voor een bedrijfspand moet worden gedaan door een bedrijf dat volgens de SCIOS-regels keurt. De keuring op deze pagina is bedoeld voor woningen en is geen SCIOS-inspectie. Punten uit een SCIOS-rapport kunnen we wel voor u herstellen."),
            ("Doen jullie ook keuringen voor verhuurders?",
             "Ja. We controleren huurwoningen, bijvoorbeeld bij een wisseling van huurder, en kunnen gevonden punten direct voor u oplossen."),
            ("Wat kost een elektra keuring?",
             "Dat hangt af van de grootte en de leeftijd van de woning. Stuur ons het adres, het bouwjaar en een foto van de meterkast, dan krijgt u vooraf een duidelijke prijs."),
        ],
    },
    # -------------------------------------------------------------- LAADPAAL
    {
        "slug": "laadpaal-installeren-rotterdam",
        "short": "Laadpaal installeren",
        "sub": "Een laadpaal bij huis, op een eigen groep.",
        "title": "Laadpaal installeren Rotterdam | Thuis laden | AlleKlussers",
        "desc": "Laadpaal thuis in Rotterdam? Eigen groep met de juiste aardlek, 1- of 3-fase, slim laden. En wat mag zonder oprit: geen kabel over de stoep. Prijs vooraf.",
        "service": "Laadpaal installeren",
        "char": "laadie",
        "say": "“Thuis laden? Ik sluit hem aan.”",
        "eyebrow": "Laadpalen en slimme elektra",
        "h1": "Laadpaal installeren in <em>Rotterdam.</em>",
        "lede": "Een laadpaal bij uw woning, op de oprit, in de carport of in de garage, veilig aangesloten op een eigen groep in de meterkast. Plus wat de gemeente wel en niet toestaat als u geen eigen oprit heeft.",
        "body": """
<h2>Wat wij <em>voor u doen.</em></h2>
<ul class="checks">
  <li>{check}<span><strong>Meterkast controleren:</strong> we kijken of uw aansluiting 1-fase of 3-fase is, hoeveel vermogen er over is en of er ruimte is voor een extra groep.</span></li>
  <li>{check}<span><strong>Eigen groep aanleggen</strong> met de juiste aardlekbeveiliging voor een laadpaal.</span></li>
  <li>{check}<span><strong>Kabel trekken</strong> van de meterkast naar de plek van de laadpaal, binnen of buiten, met een kabel die dik genoeg is voor de afstand en de stroom.</span></li>
  <li>{check}<span><strong>Monteren, aansluiten en testen,</strong> en uitleg over het gebruik en de instellingen.</span></li>
</ul>

<h2>Wat mag er <em>in Rotterdam?</em></h2>
<p>Een eigen laadpaal kan als u een eigen parkeerplaats heeft: een oprit, carport, garage of een plek op eigen terrein. De gemeente Rotterdam zegt dat er zelf ook op: houd rekening met netcongestie en met uw huidige aansluiting. Heeft u een zwaardere aansluiting nodig, dan komt u op een wachtlijst van de netbeheerder (<a href="https://www.rotterdam.nl/elektrisch-rijden" target="_blank" rel="noopener noreferrer">rotterdam.nl</a>).</p>
<ul class="checks">
  <li>{check}<span><strong>Geen kabel over de stoep.</strong> Laden op een openbare parkeerplek met een kabel vanuit uw woning mag in Rotterdam niet, ook niet als u de kabel afdekt met een kabelmat of goot. Dat geldt ook voor een kabel die over de stoep hangt.</span></li>
  <li>{check}<span><strong>Ligt uw parkeerplaats verder van huis,</strong> bijvoorbeeld een plek achter het blok of een garagebox, en moet er een kabel door openbare grond? Dan overlegt u eerst met de gemeente via een leidingvergunning. Daar zijn kosten aan verbonden.</span></li>
  <li>{check}<span><strong>Openbare laadpalen</strong> plaatst de gemeente op basis van data over waar ze nodig zijn. Op de kaart van <a href="https://viewer.evmaps.nl/rotterdam" target="_blank" rel="noopener noreferrer">EVmaps</a> ziet u welke palen er staan en welke in behandeling zijn. Heeft u een gehandicaptenparkeerplaats op kenteken, dan kunt u wel zelf een laadpaal bij die plek aanvragen.</span></li>
  <li>{check}<span><strong>Delen met de buren kan.</strong> Heeft een buurman of een bedrijf in de buurt een eigen laadpaal, dan kunt u afspraken maken om die te delen. De gemeente verwijst naar een modelovereenkomst van RVO.</span></li>
</ul>
<p>Buiten Rotterdam bepaalt elke gemeente dit zelf; de ene staat een kabelmat of kabelgoot toe, de andere niet (<a href="https://www.evupdate.nl/explainers/artikel/thuisladen-zonder-eigen-oprit-je-postcode-bepaalt-wat-wel-en-niet-mag" target="_blank" rel="noopener noreferrer">EV Update</a>). In Capelle aan den IJssel moet u op eigen terrein laden (<a href="https://www.duurzaamcapelle.nl/laadpalenbeleid-capelle-aan-den-ijssel/" target="_blank" rel="noopener noreferrer">duurzaamcapelle.nl</a>). In de regio verschilt het per gemeente: in <a href="/elektricien-capelle-aan-den-ijssel/">Capelle</a>, <a href="/elektricien-schiedam/">Schiedam</a>, <a href="/elektricien-barendrecht/">Barendrecht</a> en <a href="/elektricien-ridderkerk/">Ridderkerk</a> mag een kabel over de stoep niet, terwijl u in <a href="/elektricien-krimpen-aan-den-ijssel/">Krimpen aan den IJssel</a> kabelgoottegels bij de gemeente kunt aanvragen. Zonder toestemming loopt u volgens de ANWB het risico op een boete, en u kunt aansprakelijk zijn als iemand over uw kabel struikelt (<a href="https://www.anwb.nl/auto/elektrisch-rijden/opladen/laadkabel-over-de-stoep" target="_blank" rel="noopener noreferrer">ANWB</a>).</p>

<h2>Appartement <em>of VvE.</em></h2>
<p>Heeft u in een VvE een eigen parkeerplaats, bijvoorbeeld in een parkeergarage onder het gebouw, dan kan daar een laadpaal bij. Omdat de kabel meestal door gemeenschappelijke ruimte loopt, beslist de VvE mee. De gemeente Rotterdam verwijst naar het stappenplan op <a href="https://vveladen.nl/" target="_blank" rel="noopener noreferrer">vveladen.nl</a> en naar Stichting VVE-010. Wij kunnen voor de VvE uitzoeken waar de laadpunten op aangesloten kunnen worden. Lees ook wat we doen <a href="/elektricien-verhuurders-vve-rotterdam/">voor verhuurders en VvE's</a>.</p>

<h2>Waarom niet gewoon <em>aan het stopcontact?</em></h2>
<p>Met de kabel die bij veel auto's wordt geleverd kunt u aan een gewoon stopcontact laden. Dat gaat langzaam, en het stopcontact en de bedrading erachter krijgen dan urenlang een zware belasting. In oudere woningen, met oude bedrading of een groep waar ook andere apparaten op zitten, kan dat te warm worden. Laad nooit via een haspel of verlengsnoer. Laadt u vaak thuis, dan is een vaste laadpaal op een eigen groep de veilige keuze.</p>

<h2>1-fase <em>of 3-fase?</em></h2>
<p>Hoe snel u laadt hangt af van uw aansluiting, de laadpaal en de auto. Volgens de ANWB laadt u op 1x16A met maximaal 3,7 kW en op 3x16A met maximaal 11 kW (<a href="https://www.anwb.nl/auto/elektrisch-rijden/laadpalen/1-fase-of-3-fase-hoe-zit-het" target="_blank" rel="noopener noreferrer">ANWB</a>). Veel auto's laden thuis met maximaal 11 kW, en sommige auto's kunnen alleen op 1 fase laden. Dan heeft een 3-fase laadpaal voor die auto weinig zin.</p>
<p>Laadt u vooral 's nachts, dan is 1-fase voor veel mensen genoeg. Heeft u al 3-fase, dan kan de laadpaal daar gebruik van maken. Twijfelt u of uw aansluiting zwaarder moet, lees dan eerst <a href="/meterkast-verzwaren-rotterdam/">meterkast verzwaren</a>: met loadbalancing is dat vaak niet nodig.</p>

<h2>Wat er <em>in de meterkast moet.</em></h2>
<ul class="checks">
  <li>{check}<span><strong>Een eigen eindgroep</strong> alleen voor de laadpaal, zodat die niet samen met de oven of de wasmachine op één groep zit. Is de kast vol, dan leest u meer bij <a href="/groep-bijplaatsen-rotterdam/">groep bijplaatsen</a>.</span></li>
  <li>{check}<span><strong>Een aardlekautomaat van 30 mA.</strong> Heeft de laadpaal zelf DC-lekstroomdetectie, dan is een gewone aardlekautomaat vaak genoeg. Zonder die detectie is een aardlekschakelaar type B nodig (<a href="https://www.elektramat.nl/kennisbank/aanpassen-groepenkast/" target="_blank" rel="noopener noreferrer">Elektramat</a>). We kijken dat na in de specificaties van uw laadpaal.</span></li>
  <li>{check}<span><strong>De juiste kabel.</strong> De dikte hangt af van het vermogen en de afstand tot de meterkast. Gaat de kabel door de tuin, dan leggen we hem diep genoeg en in een beschermbuis, net als bij <a href="/buitenverlichting-tuinstopcontact-rotterdam/">buitenverlichting en tuinstopcontacten</a>.</span></li>
  <li>{check}<span><strong>Loadbalancing</strong> via de slimme meter of een meetklem, zodat de laadpaal minder vermogen pakt als de rest van het huis veel vraagt. Zo slaat uw hoofdzekering niet door.</span></li>
  <li>{check}<span><strong>Een oude groepenkast</strong> met draaizekeringen of zonder goede aardlekbeveiliging moet eerst op orde. Zie <a href="/groepenkast-vervangen-rotterdam/">groepenkast vervangen</a>.</span></li>
</ul>

<h2>Slim laden <em>en zonnepanelen na 2027.</em></h2>
<p>Op 1 januari 2027 stopt de salderingsregeling (<a href="https://www.rijksoverheid.nl/onderwerpen/energie-thuis/salderingsregeling" target="_blank" rel="noopener noreferrer">Rijksoverheid</a>). Zonnestroom die u teruglevert, kunt u dan niet meer wegstrepen tegen de stroom die u 's avonds gebruikt. Het wordt dus interessanter om uw eigen zonnestroom direct te gebruiken, bijvoorbeeld door overdag te laden als de panelen leveren. Met een slimme laadpaal kunt u dat instellen, of laden op de uren dat stroom goedkoop is als u een dynamisch contract heeft. We helpen ook met andere slimme schakelingen voor licht en apparaten. Meer uitleg staat in <a href="/salderen-stopt-2027/">salderen stopt in 2027: wat moet er in uw meterkast?</a></p>

<h2>Zo <em>pakken we het aan.</em></h2>
<ol class="steps-list">
  <li><strong>Stuur ons via WhatsApp</strong> een foto van uw meterkast, een foto van de plek waar de laadpaal moet komen, ongeveer hoeveel meter dat van de meterkast is, en welke laadpaal u heeft of wilt.</li>
  <li><strong>U krijgt een duidelijke prijs vooraf,</strong> en we zeggen eerlijk of uw meterkast en aansluiting genoeg zijn.</li>
  <li><strong>Wij leggen de groep aan, trekken de kabel en monteren de laadpaal.</strong> De stroom gaat daarvoor even uit.</li>
  <li><strong>We testen de laadpaal met u</strong> en leggen uit hoe u slim laden en loadbalancing instelt.</li>
</ol>
<p>Alles volgens NEN 1010, door verzekerde vakmensen.</p>
""",
        "faq": [
            ("Mag ik in Rotterdam mijn auto laden met een kabel over de stoep?",
             "Nee. Volgens de gemeente Rotterdam mag u een auto op een openbare parkeerplek niet opladen met een kabel vanuit uw woning, ook niet als de kabel is afgedekt of over de stoep hangt. Laad op eigen terrein, of gebruik een openbare laadpaal."),
            ("Kan ik bij de gemeente Rotterdam een openbare laadpaal aanvragen?",
             "Rotterdam plaatst openbare laadpalen op basis van data over waar ze nodig zijn. Op de kaart van EVmaps ziet u welke palen er staan en welke gepland zijn. Heeft u een gehandicaptenparkeerplaats op kenteken en een elektrische auto, dan kunt u wel zelf een laadpaal bij die plek aanvragen."),
            ("Is mijn meterkast geschikt voor een laadpaal?",
             "Dat controleren we eerst. Vaak is een extra groep genoeg; soms is een zwaardere aansluiting bij Stedin nodig. Dat hoort u vooraf van ons. Meer uitleg vindt u op onze pagina over meterkast verzwaren."),
            ("Heb ik 3-fase nodig voor een laadpaal?",
             "Niet altijd. Op 1x16A laadt u met maximaal 3,7 kW, op 3x16A met maximaal 11 kW. Laadt u vooral 's nachts, dan is 1-fase voor veel mensen genoeg. Kan uw auto alleen op 1 fase laden, dan heeft 3-fase voor het laden weinig zin."),
            ("Welke aardlekschakelaar is nodig voor een laadpaal?",
             "Een laadpaal krijgt een eigen groep met een aardlekautomaat van 30 mA. Heeft de laadpaal geen ingebouwde DC-lekstroomdetectie, dan is een aardlekschakelaar type B nodig. We kijken dat na in de gegevens van uw laadpaal."),
            ("Kan ik niet gewoon aan een stopcontact laden?",
             "Af en toe kan dat met de laadkabel van de fabrikant, maar het gaat langzaam en het stopcontact en de bedrading worden urenlang zwaar belast. Gebruik nooit een haspel of verlengsnoer. Laadt u vaak thuis, dan is een laadpaal op een eigen groep veiliger."),
            ("Kan ik een laadpaal plaatsen in de parkeergarage van mijn VvE?",
             "Als u daar een eigen parkeerplaats heeft, meestal wel, maar de VvE beslist mee omdat de kabel door gemeenschappelijke ruimte loopt. Kijk op vveladen.nl voor een stappenplan. Wij kunnen voor de VvE uitzoeken hoe de laadpunten het beste aangesloten worden."),
            ("Wat is loadbalancing?",
             "Loadbalancing zorgt dat de laadpaal minder vermogen gebruikt als andere apparaten veel stroom vragen. Zo slaat uw hoofdzekering niet door, en is een zwaardere aansluiting vaak niet nodig."),
            ("Welke laadpaal moet ik kiezen?",
             "Dat hangt af van uw auto, uw aansluiting en of u slim wilt laden, bijvoorbeeld op zonnestroom na het einde van de salderingsregeling in 2027. Let op loadbalancing en DC-lekstroomdetectie. We adviseren u graag."),
        ],
    },
    # ------------------------------------------------- VERHUURDERS / VVE
    {
        "slug": "elektricien-verhuurders-vve-rotterdam",
        "short": "Voor verhuurders en VvE's",
        "sub": "Eén aanspreekpunt voor storingen, mutaties en onderhoud.",
        "title": "Elektricien voor verhuurders en VvE's in Rotterdam | AlleKlussers",
        "desc": "Verhuurder, beheerder of VvE in Rotterdam? AlleKlussers regelt storingen bij huurders, controle bij mutatie, groepenkasten en verlichting. 24/7 bereikbaar.",
        "service": "Elektricien voor verhuurders, beheerders en VvE's",
        "char": "stekkie",
        "say": "“Uw huurder appt, wij regelen het.”",
        "eyebrow": "Verhuurders, beheerders en VvE's",
        "h1": "Elektricien voor verhuurders <em>en VvE's.</em>",
        "lede": "Eén vast aanspreekpunt voor de elektra in uw huurwoningen of complex in Rotterdam. Van een storing bij een huurder tot een keuring bij mutatie of een nieuwe groepenkast.",
        "body": """
<h2>Wat wij <em>voor u regelen.</em></h2>
<ul class="checks">
  <li>{check}<span><strong>Storingen bij huurders.</strong> Valt de stroom uit of slaat de <a href="/aardlekschakelaar-rotterdam/">aardlekschakelaar</a> steeds door? We zijn 24/7 bereikbaar, plannen direct met de huurder en zoeken de oorzaak.</span></li>
  <li>{check}<span><strong>Controle bij mutatie.</strong> Tussen twee huurders in de installatie laten nakijken, zodat de nieuwe huurder in een veilige woning start. Lees meer over <a href="/elektra-keuring-rotterdam/">keuring van de installatie</a>.</span></li>
  <li>{check}<span><strong>Groepenkasten en bedrading.</strong> Een verouderde kast of oude bedrading vervangen, of <a href="/groepenkast-vervangen-rotterdam/">extra groepen</a> voor inductie of een warmtepomp bij een renovatie.</span></li>
  <li>{check}<span><strong>Algemene ruimten.</strong> Verlichting en stopcontacten in het trappenhuis, de galerij, de bergingen of de fietsenstalling.</span></li>
  <li>{check}<span><strong>Laadpalen voor VvE's.</strong> We kijken vooraf wat de installatie aankan en maken een offerte die u in de vergadering kunt bespreken. Zie <a href="/laadpaal-installeren-rotterdam/">laadpaal installeren</a>.</span></li>
</ul>

<h2>Zo werken we <em>samen.</em></h2>
<ul class="checks">
  <li>{check}<span><strong>Eén aanspreekpunt.</strong> U stuurt ons het adres en de contactgegevens van de huurder via WhatsApp of e-mail. Wij plannen de afspraak met de huurder zelf.</span></li>
  <li>{check}<span><strong>Prijs vooraf.</strong> Voor elke reparatie krijgt u eerst een duidelijke prijs. Wilt u dat wij kleine storingen direct oplossen? Spreek dan met ons af tot welk bedrag dat mag zonder uw akkoord.</span></li>
  <li>{check}<span><strong>Terugkoppeling na afloop.</strong> U hoort wat de oorzaak was en wat we hebben gedaan, zo nodig met foto's.</span></li>
  <li>{check}<span><strong>Per klus of doorlopend.</strong> U kunt ons per klus inschakelen, of vast voor al uw adressen.</span></li>
</ul>
<p>Alles volgens NEN 1010, door verzekerde vakmensen. U krijgt binnen 24 uur reactie op een aanvraag.</p>

<h2>Huurder of verhuurder: <em>wie betaalt wat?</em></h2>
<p>Kleine herstellingen zijn voor de huurder. Welke dat zijn, staat in het Besluit kleine herstellingen. Voor elektra gaat het om het vastzetten en vervangen van schakelaars, stopcontacten en deurbellen, als dat zonder noemenswaardige kosten kan. Ook lampen aan de buitenkant van de woning en in gemeenschappelijke ruimten vervangt de huurder.</p>
<p>Groot onderhoud is voor de verhuurder, net als het vervangen van lamparmaturen in gemeenschappelijke ruimten. De groepenkast en de vaste bedrading staan niet in de lijst van kleine herstellingen. Ontstaat een kleine reparatie doordat de verhuurder een gebrek niet op tijd heeft verholpen, dan is die ook voor de verhuurder.</p>
<div class="note-box"><p><strong>Twijfelt u?</strong> Kijk in het huurcontract en op <a href="https://www.rijksoverheid.nl/documenten/vraag-en-antwoord/woning-huren/welke-kosten-zijn-voor-de-huurder-en-welke-voor-de-verhuurder" target="_blank" rel="noopener noreferrer">rijksoverheid.nl</a>. Wij vertellen u na een storing wat de oorzaak was, zodat u kunt bepalen bij wie de kosten horen.</p></div>
""",
        "faq": [
            ("Mogen mijn huurders ons zelf een bericht sturen?",
             "Ja, als u dat wilt. Spreek met ons af wat we zonder overleg mogen oplossen en vanaf welk bedrag we eerst uw akkoord vragen. U krijgt na afloop altijd een terugkoppeling."),
            ("Werken jullie ook voor VvE's en beheerders?",
             "Ja. We helpen VvE's en beheerders met storingen, verlichting in algemene ruimten, groepenkasten en laadpalen. Voor grotere werken maken we een offerte die u in de vergadering kunt bespreken."),
            ("Moet een VvE een laadpaal in de parkeergarage eerst goedkeuren?",
             "Meestal wel, omdat het om gemeenschappelijke delen gaat. Wij kunnen vooraf bekijken wat de installatie aankan, zodat de vergadering een besluit kan nemen op basis van een concrete offerte."),
            ("Is de groepenkast in een huurwoning voor de huurder of de verhuurder?",
             "De groepenkast staat niet in het Besluit kleine herstellingen. Onderhoud en vervanging horen daarom in de regel bij de verhuurder. Kijk voor uw situatie ook in het huurcontract."),
            ("Moet ik een vast contract afsluiten?",
             "Nee. U kunt ons per klus inschakelen. Heeft u meerdere adressen, dan maken we graag vaste afspraken over hoe we meldingen afhandelen."),
            ("Wat kost het?",
             "Dat hangt af van de klus. U krijgt altijd eerst een prijs, zodat u vooraf weet waar u aan toe bent."),
        ],
    },
]


# ---------------------------------------------------------------- CITIES
# One page per nearby town ("elektricien Schiedam" etc.). Keep the local
# paragraph specific to the town so the pages are not near-duplicates.
def _city_title(name):
    # Keep the page title within what Google shows (about 65 characters).
    title = f"Elektricien {name} | AlleKlussers, snel ter plaatse"
    return title if len(title) <= 65 else f"Elektricien {name} | AlleKlussers Rotterdam"


def _city(slug, name, char, say, wijken_oud, wijken_nieuw, local, faq_extra,
          extra="", mix=None, desc=None):
    # extra: optional town-specific HTML sections (use {check} for the icon,
    # no other braces). mix: replaces the old/new wijken sentence.
    if mix is None:
        mix = (f"In oudere wijken zoals {wijken_oud} komen we vaak verouderde groepenkasten en bedrading tegen. "
               f"In nieuwere wijken zoals {wijken_nieuw} gaat het vaker om een laadpaal, een thuisbatterij of extra groepen voor inductie.")
    return {
        "slug": slug,
        "city": name,
        "short": f"Elektricien {name}",
        "title": _city_title(name),
        "desc": desc or f"Elektricien nodig in {name}? Voor storingen, groepenkasten, verlichting, stopcontacten en laadpalen. Binnen 24 uur reactie, prijs vooraf.",
        "service": f"Elektricien in {name}",
        "wa": f"Hallo AlleKlussers, ik zoek een elektricien in {name}. Het gaat om: ",
        "char": char,
        "say": say,
        "eyebrow": f"Elektricien in {name}",
        "h1": f"Uw elektricien in <em>{name}.</em>",
        "lede": f"Vanuit Rotterdam-Zuid zijn we snel in {name}. Voor storingen, groepenkasten, verlichting en alles wat met elektra te maken heeft.",
        "body": f"""
<h2>Elektra in {name}, <em>snel geregeld.</em></h2>
<p>AlleKlussers is een elektrotechnisch bedrijf uit Rotterdam-Zuid. {name} ligt vlakbij, dus we zijn er snel. U krijgt binnen 24 uur reactie met een duidelijke prijs vooraf, en bij storingen zijn we 24/7 bereikbaar.</p>
<p>{local}</p>
<p>{mix}</p>
{extra}
<h2>Waarmee wij u <em>helpen in {name}.</em></h2>
<ul class="checks">
  <li>{{check}}<span><a href="/storing-elektra-rotterdam/">Storing verhelpen</a>: stroomuitval of een aardlekschakelaar die steeds doorslaat.</span></li>
  <li>{{check}}<span><a href="/groepenkast-vervangen-rotterdam/">Groepenkast vervangen of uitbreiden</a>, bijvoorbeeld voor <a href="/inductiekookplaat-aansluiten-rotterdam/">inductie</a> met een <a href="/perilex-aansluiten-rotterdam/">perilex-aansluiting</a> of een warmtepomp.</span></li>
  <li>{{check}}<span><a href="/groep-bijplaatsen-rotterdam/">Groep bijplaatsen</a> voor de wasmachine, droger, oven of airco, of voor <a href="/infraroodpanelen-aansluiten-rotterdam/">infraroodpanelen</a>.</span></li>
  <li>{{check}}<span><a href="/meterkast-verzwaren-rotterdam/">Meterkast verzwaren</a> of <a href="/krachtstroom-aansluiten-rotterdam/">krachtstroom aansluiten</a> voor een werkplaats, sauna of zware machine.</span></li>
  <li>{{check}}<span><a href="/vrije-groep-stekkerbatterij-rotterdam/">Vrije groep voor een stekkerbatterij</a>, of de meterkast klaarmaken voor een <a href="/thuisbatterij-aansluiten-rotterdam/">thuisbatterij</a>, op tijd voor 2027.</span></li>
  <li>{{check}}<span><a href="/lampen-ophangen-rotterdam/">Lampen ophangen</a>, spots en dimmers, en de <a href="/elektra-badkamer-rotterdam/">elektra voor een nieuwe badkamer</a>.</span></li>
  <li>{{check}}<span><a href="/stopcontact-plaatsen-rotterdam/">Stopcontacten plaatsen</a> of verplaatsen, binnen en <a href="/buitenverlichting-tuinstopcontact-rotterdam/">buiten in de tuin</a>.</span></li>
  <li>{{check}}<span><a href="/laadpaal-installeren-rotterdam/">Laadpaal installeren</a> bij uw woning of bedrijf.</span></li>
  <li>{{check}}<span><a href="/elektra-keuring-rotterdam/">Elektra keuring</a> bij aankoop of verhuur van een woning in {name}.</span></li>
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
          "We werken in heel Schiedam: in de historische binnenstad met haar havens en molens, in Oost, West en Zuid, in Nieuwland, en in Schiedam-Noord met Groenoord, Kethel, Woudhoek en Spaland/Sveaparken. Vanuit Rotterdam-Zuid zijn we er via de Beneluxtunnel of de Maastunnel snel.",
          [("Werken jullie ook in oude panden in de binnenstad?",
            "Ja. In oudere panden controleren we eerst de bestaande installatie en bespreken we met u wat nodig is voordat we beginnen. In een monument overleggen we vooraf hoe nieuwe leidingen zo netjes mogelijk lopen."),
           ("Kan ik in Schiedam een openbare laadpaal aanvragen?",
            "Nee. Sinds 1 januari 2026 plaatst de gemeente Schiedam openbare laadpalen op basis van voorspellingen, en kunt u zelf geen aanvraag meer indienen. Heeft u een eigen oprit of garage, dan kunnen wij daar een laadpaal plaatsen."),
           ("Mag ik in Schiedam laden met een kabel over de stoep?",
            "Nee. De gemeente staat geen kabel over of boven de stoep toe, ook niet als die is afgedekt met een kabelgoot, mat of tegels. Laad op eigen terrein of bij een openbare laadpaal."),
           ("Ik woon in een flat in Groenoord. Kan ik inductie koken?",
            "Meestal wel. De meeste inductiekookplaten hebben een kookgroep met perilex nodig; die kan vaak gewoon op een 1-fase aansluiting. Stuur een foto van uw meterkast via WhatsApp, dan zeggen we of er een groep bij kan of dat de kast eerst moet worden uitgebreid."),
           ("Mijn portiekwoning in Nieuwland heeft een oude groepenkast. Moet die eruit?",
            "Niet altijd. Soms is uitbreiden genoeg, bijvoorbeeld met een extra groep of een aardlekschakelaar erbij. Zitten er nog draaizekeringen in of is er geen aardlekschakelaar, dan is vervangen vaak verstandiger. U krijgt eerst advies en een prijs."),
           ("Ik huur mijn woning. Mag ik jullie inschakelen?",
            "Voor kleine dingen binnen uw woning, zoals een lamp of een extra stopcontact, meestal wel. De groepenkast, de bedrading en de meterkast zijn van de verhuurder; meld problemen daarmee eerst bij uw verhuurder of woningcorporatie.")],
          mix="Schiedam heeft woningen uit bijna elke periode, en dat ziet u terug in de meterkast. In de binnenstad en de oudere wijken komen we oude bedrading en groepenkasten met weinig groepen tegen. In de naoorlogse portiekwoningen van Nieuwland en de flats van Groenoord is de kast vaak nooit aangepast aan inductie, een droger of een warmtepomp. In Woudhoek gaat het vaker om extra groepen, verlichting of een laadpaal bij een eengezinswoning.",
          desc="Elektricien in Schiedam: binnenstad, Nieuwland, Groenoord, Kethel, Woudhoek en meer. Groepenkast, storing, inductie, laadpaal. Reactie binnen 24 uur.",
          extra="""
<h2>Elektra per wijk <em>in Schiedam.</em></h2>
<p>Schiedam is een oude stad met veel naoorlogse wijken eromheen. Wat er in uw meterkast hangt, hangt vooral af van wanneer uw wijk is gebouwd.</p>
<ul class="checks">
  <li>{check}<span><strong>Binnenstad.</strong> De historische binnenstad met haar havens en de hoogste windmolens ter wereld. In oude panden en bovenwoningen kijken we eerst naar de staat van de <a href="/bedrading-vervangen-rotterdam/">bedrading</a> en of alles geaard is, voordat we iets bijplaatsen.</span></li>
  <li>{check}<span><strong>Nieuwland.</strong> Direct na de Tweede Wereldoorlog in fasen aangelegd, met portiekwoningen van vier woonlagen en hogere flats. De meterkast is hier vaak klein; bij een nieuwe keuken is <a href="/groepenkast-vervangen-rotterdam/">uitbreiden of vervangen van de groepenkast</a> vaak de eerste stap.</span></li>
  <li>{check}<span><strong>Groenoord.</strong> Gebouwd in de jaren zestig, vooral flats van 6, 8 of 12 lagen. Voor een <a href="/inductiekookplaat-aansluiten-rotterdam/">inductiekookplaat</a>, droger of vaatwasser is vaak een <a href="/groep-bijplaatsen-rotterdam/">extra groep</a> nodig. Voor de verlichting in hal en trappenhuis is de VvE of verhuurder aan zet.</span></li>
  <li>{check}<span><strong>Kethel.</strong> Het oude dorp Kethel hoorde tot 1941 bij de gemeente Kethel en Spaland. Naast oudere huizen aan het lint staan hier nieuwere woningen; we passen onze aanpak aan op het bouwjaar.</span></li>
  <li>{check}<span><strong>Woudhoek.</strong> Ontstaan in de jaren zeventig en tachtig, met gestapelde bouw en eengezinswoningen. Vragen gaan hier vaak over een laadpaal op eigen terrein, <a href="/buitenverlichting-tuinstopcontact-rotterdam/">buitenverlichting en een tuinstopcontact</a> of extra groepen.</span></li>
</ul>
<div class="note-box"><p><strong>Bronnen:</strong> Wikipedia over <a href="https://nl.wikipedia.org/wiki/Schiedam" target="_blank" rel="noopener noreferrer">Schiedam</a>, <a href="https://nl.wikipedia.org/wiki/Nieuwland_(Schiedam)" target="_blank" rel="noopener noreferrer">Nieuwland</a>, <a href="https://nl.wikipedia.org/wiki/Groenoord_(Schiedam)" target="_blank" rel="noopener noreferrer">Groenoord</a>, <a href="https://nl.wikipedia.org/wiki/Kethel" target="_blank" rel="noopener noreferrer">Kethel</a> en <a href="https://nl.wikipedia.org/wiki/Woudhoek" target="_blank" rel="noopener noreferrer">Woudhoek</a>.</p></div>

<h2>Laadpaal in Schiedam: <em>wat mag wel?</em></h2>
<p>De gemeente Schiedam heeft duidelijke regels voor elektrisch laden:</p>
<ul class="checks">
  <li>{check}<span><strong>Geen kabel over de stoep.</strong> Een laadkabel vanuit uw woning naar een openbare parkeerplaats mag niet, ook niet afgedekt met een kabelgoot, mat of tegels, of via een zwenkarm.</span></li>
  <li>{check}<span><strong>Geen aanvraag meer.</strong> Sinds 1 januari 2026 plaatst de gemeente openbare laadpalen op basis van voorspellingen. U kunt zelf geen openbare laadpaal meer aanvragen.</span></li>
  <li>{check}<span><strong>Eigen oprit of garage?</strong> Dan plaatsen wij daar een <a href="/laadpaal-installeren-rotterdam/">laadpaal</a> op een eigen groep. Alleen dan kunt u ook met stroom van uw eigen zonnepanelen laden. We kijken eerst of uw meterkast en aansluiting het aankunnen.</span></li>
</ul>
<div class="note-box"><p><strong>Bron:</strong> <a href="https://www.schiedam.nl/a-tot-z/veelgestelde-vragen-over-laadpalen" target="_blank" rel="noopener noreferrer">Veelgestelde vragen over laadpalen</a>, gemeente Schiedam.</p></div>

<h2>Huur, flat <em>of VvE?</em></h2>
<p>Veel Schiedammers huren hun woning of wonen in een flat met een VvE. Werk binnen uw eigen woning, zoals een extra stopcontact of lamp, kunt u meestal zelf laten doen. Voor de groepenkast, de bedrading of gemeenschappelijke delen zoals de verlichting in het trappenhuis beslist de verhuurder of de VvE. Voor hen hebben we een <a href="/elektricien-verhuurders-vve-rotterdam/">aparte pagina</a>.</p>
"""),
    _city("elektricien-vlaardingen", "Vlaardingen", "kastje", "“Vlaardingen? Ik ben onderweg.”",
          "Westwijk, Babberspolder en het centrum", "Holy en Ambacht",
          "In Vlaardingen werken we in alle wijken: het centrum rond de Oude Haven, de Oostwijk, Vlaardinger Ambacht en de Babberspolders, de Westwijk, Holy-Zuid en Holy-Noord, en de nieuwbouw in de Rivierzone. Vanuit Rotterdam-Zuid zijn we er snel, en Schiedam ligt er direct naast.",
          [("Mijn groepenkast is oud. Moet hij vervangen worden?",
            "Niet altijd. Soms is uitbreiden genoeg, bijvoorbeeld met een extra groep of een aardlekschakelaar erbij. We kijken eerst wat er zit en wat u nodig heeft. Pas als vervangen echt verstandig is, krijgt u daar een prijs voor."),
           ("Moet ik in Vlaardingen een openbare laadpaal aanvragen?",
            "Nee. Volgens de gemeente Vlaardingen is aanvragen niet nodig: de gemeente kijkt zelf naar het gebruik van de bestaande laadpalen en het aantal elektrische auto's, en plaatst op basis daarvan nieuwe palen. Heeft u een oprit, carport of garage, dan kunt u ook een eigen laadpaal laten plaatsen op een eigen groep."),
           ("Ik woon in een bovenwoning in de Oostwijk. Waar let u op?",
            "In vooroorlogse woningen kijken we eerst naar de bedrading en de groepenkast: hoe oud is het, is alles geaard en zit er een aardlekschakelaar in? Daarna bespreken we wat er nodig is voor uw plannen, zoals inductie of extra stopcontacten. U krijgt vooraf een prijs."),
           ("Kan ik inductie koken in mijn flat in de Westwijk of Holy?",
            "Meestal wel. De meeste inductiekookplaten hebben een kookgroep met perilex nodig; die kan vaak gewoon op een 1-fase aansluiting. Stuur een foto van uw meterkast via WhatsApp, dan zeggen we of er een groep bij kan of dat de kast eerst moet worden uitgebreid."),
           ("Heb ik krachtstroom nodig?",
            "Voor een inductiekookplaat bijna nooit. Een 3-fase aansluiting is vooral zinvol als er een warmtepomp, laadpaal én inductie tegelijk komen. De netbeheerder verzwaart de aansluiting; wij passen daarna de groepenkast aan. We rekenen eerst uit of het nodig is."),
           ("Ik huur mijn woning. Mag ik jullie inschakelen?",
            "Voor kleine dingen die u zelf heeft aangebracht meestal wel. Voor de groepenkast, de bedrading of een nieuwe groep overlegt u eerst met uw verhuurder of woningcorporatie. Voor verhuurders en VvE's hebben we een aparte pagina.")],
          mix="Vlaardingen heeft woningen uit bijna elke bouwperiode, en dat ziet u terug in de meterkast. In de vooroorlogse Oostwijk en de jaren-30 huizen in Ambacht komen we vaak oude bedrading en een groepenkast met weinig groepen tegen. In de naoorlogse Westwijk, de Babberspolders en Holy gaat het vaak om een kast die nooit is aangepast aan inductie, een droger of een warmtepomp.",
          desc="Elektricien in Vlaardingen: Westwijk, Holy, Ambacht, Babberspolder, Oostwijk en centrum. Groepenkast vervangen, storing, inductie. Reactie binnen 24 uur.",
          extra="""
<h2>Elektra per wijk <em>in Vlaardingen.</em></h2>
<p>Vlaardingen groeide na de oorlog snel. Eerst kwamen de Westwijk en de Babberspolders, daarna Holy, dat inmiddels ongeveer een derde van de bebouwde oppervlakte van de stad beslaat. Elke wijk heeft zo een eigen bouwperiode, en elke periode zijn eigen meterkast.</p>
<ul class="checks">
  <li>{check}<span><strong>Centrum en Oude Haven.</strong> Historische panden aan de Oost- en Westhavenkade en in de straten erachter, vaak met bovenwoningen. Voordat we iets aansluiten, kijken we naar de staat van de <a href="/bedrading-vervangen-rotterdam/">bedrading</a>. In een monumentaal pand overleggen we vooraf hoe nieuwe leidingen zo netjes en onzichtbaar mogelijk lopen.</span></li>
  <li>{check}<span><strong>Oostwijk.</strong> Grotendeels gebouwd voor de Tweede Wereldoorlog; ruim 40 procent van de woningen is een bovenwoning of appartement. Hier komen we nog groepenkasten tegen met weinig groepen of zonder <a href="/aardlekschakelaar-rotterdam/">aardlekschakelaar</a>, en soms ruimtes waar niet alles geaard is.</span></li>
  <li>{check}<span><strong>Vlaardinger Ambacht en de Babberspolders.</strong> Van het oude dorp Ambacht en de vele jaren-30 woningen tot de huizen uit de jaren vijftig in de Babberspolders en het vernieuwde Babberspolder-Oost. Bij een nieuwe keuken of verbouwing is <a href="/groepenkast-vervangen-rotterdam/">uitbreiden of vervangen van de groepenkast</a> vaak de eerste stap.</span></li>
  <li>{check}<span><strong>Westwijk.</strong> De bouw begon in 1954 en de eerste bewoners kregen in 1957 de sleutel. Er staat vooral middelhoogbouw en wat laagbouw. In de flats is de meterkast vaak klein en zijn er weinig groepen; voor een <a href="/inductiekookplaat-aansluiten-rotterdam/">inductiekookplaat</a>, droger of vaatwasser is dan een <a href="/groep-bijplaatsen-rotterdam/">extra groep</a> nodig.</span></li>
  <li>{check}<span><strong>Holy-Zuid en Holy-Noord.</strong> Gebouwd vanaf eind jaren zestig, met hoogbouw en sociale huur, maar ook buurten met eengezinswoningen en vrijstaande huizen. Bij de eengezinswoningen gaat het vaak om een laadpaal op eigen terrein, <a href="/buitenverlichting-tuinstopcontact-rotterdam/">buitenverlichting en een tuinstopcontact</a> of extra groepen.</span></li>
  <li>{check}<span><strong>Rivierzone en nieuwbouw.</strong> Bij het gebied ten zuiden van station Vlaardingen Centrum en langs de rivier komen nieuwe woningen bij. De installatie is daar modern; vragen gaan vaker over <a href="/lampen-ophangen-rotterdam/">verlichting</a>, <a href="/stopcontact-plaatsen-rotterdam/">extra stopcontacten</a> of een laadpaal.</span></li>
</ul>
<div class="note-box"><p><strong>Bronnen:</strong> <a href="https://www.vlaardingswonen.nl/De_wijken" target="_blank" rel="noopener noreferrer">De wijken, Woonvisie Vlaardingen 2020-2030</a> (gemeente Vlaardingen) en Wikipedia over de <a href="https://nl.wikipedia.org/wiki/Westwijk_(Vlaardingen)" target="_blank" rel="noopener noreferrer">Westwijk</a> en <a href="https://nl.wikipedia.org/wiki/Vlaardingen-Holy" target="_blank" rel="noopener noreferrer">Vlaardingen-Holy</a>.</p></div>

<h2>Groepenkast, inductie <em>of krachtstroom?</em></h2>
<p>Wie in Vlaardingen van gas naar inductie gaat, of een droger en vaatwasser tegelijk wil laten draaien, loopt vaak tegen de groepenkast aan. Drie vragen bepalen wat er nodig is:</p>
<ul class="checks">
  <li>{check}<span><strong>Is er ruimte in de kast?</strong> Zit er nog plek voor een kookgroep of een extra groep, en hangen er niet meer dan vier groepen aan één aardlekschakelaar? Dan is <a href="/groep-bijplaatsen-rotterdam/">een groep bijplaatsen</a> vaak genoeg.</span></li>
  <li>{check}<span><strong>Is de kast verouderd?</strong> Draaizekeringen, geen of maar één aardlekschakelaar, of geen hoofdschakelaar: dan is <a href="/groepenkast-vervangen-rotterdam/">een nieuwe groepenkast</a> meestal de betere keuze.</span></li>
  <li>{check}<span><strong>Is uw aansluiting zwaar genoeg?</strong> Voor inductie meestal wel, ook op 1-fase. Komen er ook een warmtepomp en een laadpaal, dan rekenen we uit of <a href="/meterkast-verzwaren-rotterdam/">verzwaren naar 3-fase</a> nodig is.</span></li>
</ul>
<p>Stuur een foto van uw meterkast via WhatsApp. Dan ziet u vooraf wat er moet gebeuren en wat het kost.</p>

<h2>Laadpaal <em>in Vlaardingen.</em></h2>
<p>Een openbare laadpaal aanvragen is in Vlaardingen niet nodig. De gemeente houdt het gebruik van de bestaande laadpalen in de gaten en plaatst nieuwe palen waar ze nodig zijn, op basis van de drukte en het aantal elektrische auto's. Op een kaart van de gemeente staan de locaties waar in de toekomst mogelijk een laadpaal komt.</p>
<p>Heeft u een oprit, carport of garage, dan plaatsen wij daar een <a href="/laadpaal-installeren-rotterdam/">eigen laadpaal</a> op een eigen groep. We kijken eerst of uw meterkast en aansluiting het aankunnen.</p>
<div class="note-box"><p><strong>Bron:</strong> <a href="https://www.vlaardingen.nl/Onderwerpen/Duurzaamheid/Laadpaal_elektrisch_rijden" target="_blank" rel="noopener noreferrer">Laadpaal / elektrisch rijden</a>, gemeente Vlaardingen.</p></div>

<h2>Huur, flat <em>of VvE?</em></h2>
<p>Veel Vlaardingers huren hun woning of wonen in een flat met een VvE. Werk binnen uw eigen woning, zoals een extra stopcontact of lamp, kunt u meestal zelf laten doen. Voor de groepenkast, de bedrading of gemeenschappelijke delen zoals de verlichting in het trappenhuis beslist de verhuurder of de VvE. Voor hen hebben we een <a href="/elektricien-verhuurders-vve-rotterdam/">aparte pagina</a>.</p>
"""),
    _city("elektricien-capelle-aan-den-ijssel", "Capelle aan den IJssel", "dosie", "“Capelle? Gewoon even de brug over.”",
          "Middelwatering, Oostgaarde en Schollevaar", "Fascinatio",
          "Capelle aan den IJssel ligt direct naast Rotterdam. We werken in alle wijken: Middelwatering, 's-Gravenland, Capelle-West, Oostgaarde, Schenkel, Schollevaar en Fascinatio, en ook op bedrijvenpark Rivium. Net over de grens zijn we net zo goed in Rotterdam Prins Alexander.",
          [("Mag ik in Capelle mijn auto laden met een kabel over de stoep?",
            "Nee. De gemeente Capelle aan den IJssel staat niet toe dat u uw aansluiting in de openbare ruimte legt, omdat mensen over de kabel kunnen struikelen. Laad op eigen terrein, of vraag via laadpaalnodig.nl een openbare laadpaal aan. Heeft u een oprit, carport of garage, dan plaatsen wij daar een laadpaal op een eigen groep."),
           ("Mijn flat in Oostgaarde heeft een oude meterkast. Kan ik inductie koken?",
            "Vaak wel, maar meestal is er een extra groep of een perilex-aansluiting nodig. Stuur een foto van uw meterkast via WhatsApp, dan zeggen we wat er nodig is en krijgt u vooraf een prijs."),
           ("Hoe zie ik of mijn groepenkast verouderd is?",
            "Let op draaizekeringen (smeltpatronen), weinig groepen, geen aardlekschakelaar of één aardlekschakelaar voor alle groepen, en groepen die vaak doorslaan. Twijfelt u, stuur dan een foto van de meterkast, dan kijken we met u mee."),
           ("Ik woon in een flat. Mag ik zelf een elektricien inschakelen?",
            "Voor werk binnen uw eigen woning meestal wel, zoals een extra stopcontact of een nieuwe groep. Voor gemeenschappelijke delen, zoals de verlichting in het trappenhuis of een laadpaal in de parkeergarage, beslist de VvE. Huurt u, overleg dan eerst met uw verhuurder."),
           ("Werken jullie ook in Prins Alexander?",
            "Ja. Ommoord, Zevenkamp, Het Lage Land, Prinsenland, Nesselande en de rest van Prins Alexander horen gewoon bij ons werkgebied in Rotterdam."),
           ("Werken jullie ook voor bedrijven in Capelle?",
            "Ja. Naast particulieren helpen we ook bedrijven, winkels en verhuurders met storingen, onderhoud en aanpassingen, ook op het Rivium en de andere bedrijventerreinen.")],
          mix="Veel woningen in Capelle zijn gebouwd tussen de jaren zestig en tachtig, toen het dorp uitgroeide tot stad. Daar komen we vaak een groepenkast tegen die nooit is aangepast aan wat er nu in huis staat. In Fascinatio, de jongste wijk, gaat het vaker om een laadpaal, een extra groep voor inductie of verlichting in de tuin.",
          desc="Elektricien in Capelle aan den IJssel: Oostgaarde, Schollevaar, Middelwatering, Fascinatio en meer. Groepenkast, storing, laadpaal. Reactie binnen 24 uur.",
          extra="""
<h2>Elektra per wijk <em>in Capelle.</em></h2>
<p>Capelle groeide na de oorlog van een dijkdorp uit tot een stad: van ongeveer 9.000 inwoners halverwege de jaren vijftig naar 57.000 in 1988. Elke wijk heeft daardoor een eigen bouwperiode, en dat ziet u terug in de meterkast.</p>
<ul class="checks">
  <li>{check}<span><strong>Oostgaarde.</strong> De bouw begon eind jaren zestig met de grote flats aan de Abram van Rijckevorselweg. In flats en portiekwoningen zit vaak nog een meterkast met weinig groepen. Komt er een inductiekookplaat, droger of vaatwasser bij, dan is een <a href="/groep-bijplaatsen-rotterdam/">extra groep</a> of een <a href="/groepenkast-vervangen-rotterdam/">nieuwe groepenkast</a> vaak nodig.</span></li>
  <li>{check}<span><strong>Schollevaar.</strong> Gebouwd vanaf begin jaren zeventig, vooral laagbouw en woonerven. In eengezinswoningen uit die tijd zit soms nog een groepenkast met draaizekeringen, of zijn niet alle groepen beveiligd met een aardlekschakelaar. Slaat er iets door, kijk dan eerst op onze pagina over de <a href="/aardlekschakelaar-rotterdam/">aardlekschakelaar</a>.</span></li>
  <li>{check}<span><strong>Middelwatering, 's-Gravenland, Schenkel en Capelle-West.</strong> Hier staan veel woningen uit de jaren van snelle groei. Bij een verbouwing of een nieuwe keuken loont het om de <a href="/bedrading-vervangen-rotterdam/">bedrading</a> en de groepenkast te laten nakijken, of om een <a href="/elektra-keuring-rotterdam/">keuring</a> te laten doen als u een woning koopt.</span></li>
  <li>{check}<span><strong>Fascinatio.</strong> De jongste wijk van Capelle, sinds 2001, met veel wonen aan het water. De installatie is hier meestal moderner. Vragen gaan vaker over een laadpaal op eigen terrein, <a href="/buitenverlichting-tuinstopcontact-rotterdam/">buitenverlichting en een tuinstopcontact</a>, of een groep voor <a href="/inductiekookplaat-aansluiten-rotterdam/">inductie</a>.</span></li>
  <li>{check}<span><strong>Rivium en bedrijventerreinen.</strong> Voor kantoren en bedrijfsruimtes verhelpen we storingen, plaatsen we verlichting en leggen we extra groepen aan.</span></li>
</ul>

<h2>Laadpaal in Capelle: <em>wat mag wel?</em></h2>
<p>De gemeente Capelle aan den IJssel is duidelijk: laad uw auto op op uw eigen terrein. Een laadkabel over de stoep of door de openbare ruimte is niet toegestaan, omdat mensen erover kunnen struikelen. Ook mag u een openbare parkeerplek niet claimen als eigen laadplek.</p>
<p>Heeft u een oprit, carport of garage, dan plaatsen wij daar een <a href="/laadpaal-installeren-rotterdam/">laadpaal</a> op een eigen groep en kijken we eerst of uw aansluiting het aankan. Heeft u geen eigen terrein, dan kunt u via laadpaalnodig.nl een openbare laadpaal in de buurt aanvragen.</p>
<div class="note-box"><p><strong>Bron:</strong> <a href="https://www.duurzaamcapelle.nl/laadpalenbeleid-capelle-aan-den-ijssel/" target="_blank" rel="noopener noreferrer">laadpalenbeleid Capelle aan den IJssel 2025-2026</a> (Duurzaam Capelle, gemeente Capelle aan den IJssel).</p></div>

<h2>Flat, huur <em>of VvE?</em></h2>
<p>Veel Capellenaren wonen in een flat of portiekwoning. Werk binnen uw eigen woning, zoals een extra stopcontact of een nieuwe groep, kunt u meestal zelf laten doen. Voor gemeenschappelijke delen, zoals de verlichting in het trappenhuis of een laadpaal in de parkeergarage, beslist de VvE. Huurt u, overleg dan eerst met uw verhuurder. Voor VvE's en verhuurders hebben we een <a href="/elektricien-verhuurders-vve-rotterdam/">aparte pagina</a>.</p>
"""),
    _city("elektricien-barendrecht", "Barendrecht", "laadie", "“Barendrecht? Laden maar.”",
          "het centrum en het oude dorp", "Carnisselande en Smitshoek",
          "Barendrecht ligt op een paar minuten van ons in Rotterdam-Zuid. We werken in het hele dorp: het oude dorp rond de watertoren en de Dorpsstraat, het centrum rond de Middenbaan, de wijken daaromheen en de wijken van Carnisselande en Smitshoek aan de andere kant van de A29. Smitshoek ligt zelfs op loopafstand van de Rotterdamse wijk Zuidwijk.",
          [("Mag ik in Barendrecht mijn auto laden met een kabel over de stoep?",
            "Nee. De gemeente Barendrecht staat laden vanuit de woning naar een openbare parkeerplaats met een kabel over de stoep niet toe en sluit daarmee aan bij de regels van Rotterdam. Laad op eigen terrein, of vraag een openbare laadpaal aan als u op een openbare parkeerplaats bent aangewezen."),
           ("Wanneer kan ik een openbare laadpaal aanvragen?",
            "Volgens het uitvoeringsplan laadpalen van de gemeente kan dat als u geen eigen parkeerplek heeft en een elektrische auto heeft of heeft besteld ('paal volgt auto'). De gemeente streeft naar een publiek laadpunt binnen 200 meter van de aanvrager. Heeft u wel een oprit of garage, dan komt er geen openbare paal en plaatsen wij graag een laadpaal op uw eigen terrein."),
           ("Mijn huis in Carnisselande is van rond 2000. Is de groepenkast nog goed?",
            "Vaak wel, maar hij is wel ingericht op de apparaten van toen. Wilt u inductie, een droger, een warmtepomp of een laadpaal erbij, dan is er vaak een extra groep nodig, of een ruimere kast als er geen plek meer is. Stuur een foto van uw meterkast via WhatsApp, dan zeggen we wat er nodig is."),
           ("Kunnen jullie een laadpaal en een groep voor een stekkerbatterij tegelijk aanleggen?",
            "Ja. We kijken eerst of uw meterkast en aansluiting dat aankunnen en geven de laadpaal en de batterij elk een eigen groep."),
           ("Wat verandert er als het salderen in 2027 stopt?",
            "Vanaf 1 januari 2027 mag u de stroom van uw zonnepanelen niet meer wegstrepen tegen wat u afneemt. Het loont dan meer om zelf op te gebruiken, bijvoorbeeld door de auto overdag te laden of apparaten aan te zetten als de zon schijnt. Voor een stekkerbatterij leggen we een vrije groep aan."),
           ("Ik woon in het oude dorp. Waar let u op?",
            "In oudere woningen kijken we eerst naar de bedrading en de groepenkast: hoe oud is het, is alles geaard en zitten er aardlekschakelaars in? Daarna bespreken we wat nodig is voor uw plannen. U krijgt vooraf een prijs."),
           ("Werken jullie ook in Smitshoek en Rhoon?",
            "Ja. Smitshoek hoort bij ons werkgebied, ook het deel met een Rhoonse postcode. Ook in Rhoon en Poortugaal kunt u ons vragen.")],
          mix="Barendrecht groeide hard: van ongeveer 2.200 woningen in 1961 naar ruim 18.000 in 2011. Daardoor staan er naast oude dorpshuizen vooral woningen van na 1960. In de oudere straten komen we vaker een groepenkast met weinig groepen tegen. In Carnisselande en Smitshoek is de installatie jonger, maar ook die is ingericht op de apparaten van rond 2000: inductie, een warmtepomp of een laadpaal vragen dan vaak om extra groepen.",
          desc="Elektricien in Barendrecht: Carnisselande, Smitshoek, oude dorp en centrum. Laadpaal, groepenkast, extra groep, storing. Reactie binnen 24 uur.",
          extra="""
<h2>Elektra per wijk <em>in Barendrecht.</em></h2>
<p>In 1930 woonden er nog geen 5.000 mensen in Barendrecht, rond 2010 bijna 50.000. Die groei zit vooral in de wijken van na de oorlog en in de Vinex-wijk Carnisselande. Wat er in de meterkast hangt, hangt sterk af van de buurt.</p>
<ul class="checks">
  <li>{check}<span><strong>Oude dorp en centrum.</strong> Rond de watertoren, de Dorpsstraat en de Middenbaan staan de oudste huizen van Barendrecht, naast winkels en bovenwoningen. Hier kijken we eerst naar de staat van de <a href="/bedrading-vervangen-rotterdam/">bedrading</a> en of er een <a href="/aardlekschakelaar-rotterdam/">aardlekschakelaar</a> in de kast zit, voordat we iets bijplaatsen.</span></li>
  <li>{check}<span><strong>Wijken uit de groeijaren.</strong> Rond het centrum staan veel eengezinswoningen en flats uit de periode van snelle groei na 1960. Bij een nieuwe keuken of verbouwing is <a href="/groepenkast-vervangen-rotterdam/">uitbreiden of vervangen van de groepenkast</a> vaak de eerste stap, zeker als er nog draaizekeringen in zitten.</span></li>
  <li>{check}<span><strong>Carnisselande.</strong> De Vinex-wijk tussen het oude Barendrecht en Smitshoek, gebouwd vanaf 1997, met ongeveer 7.500 woningen en ruim 14.000 inwoners. Meerwede is het deel van Barendrecht met de meeste inwoners. De installatie is hier meestal in orde, maar heeft vaak weinig vrije plekken. Voor <a href="/inductiekookplaat-aansluiten-rotterdam/">inductie</a>, een droger of een warmtepomp is dan een <a href="/groep-bijplaatsen-rotterdam/">extra groep</a> nodig.</span></li>
  <li>{check}<span><strong>Smitshoek, Riederhoek en Vrijheidsakker.</strong> De 'Dorpse Driehoek' van Carnisselande, met het oude lint van Smitshoek aan de dijk. Hier gaat het vaak om een laadpaal op eigen terrein, <a href="/buitenverlichting-tuinstopcontact-rotterdam/">buitenverlichting en een tuinstopcontact</a>, of een <a href="/vrije-groep-stekkerbatterij-rotterdam/">vrije groep voor een stekkerbatterij</a>.</span></li>
  <li>{check}<span><strong>Bedrijventerreinen.</strong> Voor bedrijfsruimtes en winkels verhelpen we storingen, plaatsen we verlichting en leggen we extra groepen aan.</span></li>
</ul>
<div class="note-box"><p><strong>Bronnen:</strong> Wikipedia over <a href="https://en.wikipedia.org/wiki/Barendrecht" target="_blank" rel="noopener noreferrer">Barendrecht</a>, <a href="https://nl.wikipedia.org/wiki/Carnisselande" target="_blank" rel="noopener noreferrer">Carnisselande</a> en <a href="https://nl.wikipedia.org/wiki/Smitshoek" target="_blank" rel="noopener noreferrer">Smitshoek</a>.</p></div>

<h2>Laadpaal in Barendrecht: <em>wat mag wel?</em></h2>
<p>De gemeente Barendrecht werkt met de 'ladder van laden': eerst laden op eigen terrein, pas daarna in de openbare ruimte. Drie dingen om te weten:</p>
<ul class="checks">
  <li>{check}<span><strong>Geen kabel over de stoep.</strong> Laden vanuit uw woning naar een openbare parkeerplaats met een kabel over de stoep staat de gemeente niet toe. Daarmee volgt Barendrecht de regels van Rotterdam.</span></li>
  <li>{check}<span><strong>Openbare laadpaal: paal volgt auto.</strong> Bent u aangewezen op een openbare parkeerplaats, dan kunt u een publiek laadpunt aanvragen zodra u een elektrische auto heeft of heeft besteld. De gemeente streeft ernaar dat zo'n laadpunt binnen 200 meter van de aanvrager komt.</span></li>
  <li>{check}<span><strong>Eigen oprit of garage?</strong> Dan komt er geen openbare paal. Wij plaatsen een <a href="/laadpaal-installeren-rotterdam/">laadpaal op uw eigen terrein</a> op een eigen groep, en kijken eerst of uw meterkast en aansluiting het aankunnen. Is dat te krap, dan rekenen we uit of <a href="/meterkast-verzwaren-rotterdam/">verzwaren naar 3-fase</a> nodig is.</span></li>
</ul>
<div class="note-box"><p><strong>Bron:</strong> <a href="https://lokaleregelgeving.overheid.nl/CVDR663334" target="_blank" rel="noopener noreferrer">Uitvoeringsplan laadpalen Barendrecht 2021</a> (gemeente Barendrecht, geldend sinds 27 oktober 2021).</p></div>

<h2>Zonnepanelen <em>en 2027.</em></h2>
<p>Heeft u zonnepanelen? Vanaf 1 januari 2027 stopt de salderingsregeling: wat u teruglevert, mag u dan niet meer wegstrepen tegen wat u afneemt. Zelf meer stroom gebruiken als de zon schijnt wordt dan belangrijker, bijvoorbeeld met slim laden van de auto of een stekkerbatterij. Voor een stekkerbatterij leggen we een <a href="/vrije-groep-stekkerbatterij-rotterdam/">vrije groep</a> aan, zodat hij niet op een groep hangt die al vol zit met andere apparaten. Lees ook wat <a href="/salderen-stopt-2027/">het einde van salderen</a> betekent voor uw meterkast.</p>

<h2>Huur <em>of VvE?</em></h2>
<p>Huurt u, dan kunt u werk binnen uw eigen woning, zoals een extra stopcontact of lamp, meestal zelf laten doen. Voor de groepenkast, de bedrading of een nieuwe groep overlegt u eerst met uw verhuurder. In een appartementengebouw beslist de VvE over gemeenschappelijke delen, zoals de verlichting in de hal of laadpalen in de parkeergarage. Voor verhuurders en VvE's hebben we een <a href="/elektricien-verhuurders-vve-rotterdam/">aparte pagina</a>.</p>
"""),
    _city("elektricien-krimpen-aan-den-ijssel", "Krimpen aan den IJssel", "laadie", "“Krimpen? Gewoon de Algerabrug over.”",
          "", "",
          "In Krimpen aan den IJssel werken we in de hele gemeente: in de oude bebouwing langs de dijken, in de wijken die vanaf de jaren zestig zijn gebouwd, zoals Kortland en Langeland, en op bedrijventerrein Stormpolder. Via de Algerabrug en Capelle aan den IJssel zijn we er vanuit Rotterdam snel.",
          [("Mag ik in Krimpen mijn auto laden met een kabel over de stoep?",
            "Alleen via kabelgoottegels van de gemeente. Dat zijn speciale tegels met een afgedekte goot voor de laadkabel. U vraagt ze aan bij de gemeente; die beoordeelt of het bij uw woning kan en legt ze tegen kostprijs aan. Een losse kabel of mat over de stoep mag niet."),
           ("Wat zijn de voorwaarden voor kabelgoottegels?",
            "Volgens de gemeente onder meer: u heeft een elektrische auto, u kunt niet binnen 100 meter van uw woning op eigen terrein parkeren, er zit alleen een stoep tussen uw woning en de parkeerplaats, de goot loopt in een rechte lijn en is maximaal 3,2 meter lang, en de parkeerplaats blijft openbaar. De precieze voorwaarden staan bij de gemeente."),
           ("Wat doen jullie als ik kabelgoottegels krijg?",
            "Wij zorgen voor de aansluiting aan uw kant: een laadpunt aan de gevel of op uw eigen terrein, op een eigen groep in de meterkast met de juiste beveiliging. We kijken eerst of uw groepenkast en aansluiting het aankunnen."),
           ("Mijn woning is uit de jaren zeventig. Is mijn groepenkast nog goed?",
            "Vaak werkt hij nog, maar hij is ingericht op de apparaten van toen. In woningen van voor 1975 zit vaak geen aardlekschakelaar, tenzij de kast later is vernieuwd. Wilt u inductie, een droger of een laadpunt erbij, dan is er vaak een extra groep of een nieuwe kast nodig. Stuur een foto van uw meterkast."),
           ("Werken jullie ook voor bedrijven op de Stormpolder?",
            "Ja. Voor bedrijfsruimtes verhelpen we storingen, plaatsen we verlichting en leggen we extra groepen aan.")],
          mix="Krimpen groeide pas echt na 1958, toen de Algerabrug de eerste vaste verbinding met de overkant van de IJssel werd. Vanaf halverwege de jaren zestig werd Krimpen een forensengemeente van Rotterdam en breidde het flink uit. Veel woningen komen dus uit de jaren zestig en zeventig. Daar komen we vaak een groepenkast tegen die nooit is aangepast aan inductie, een droger of een laadpunt.",
          desc="Elektricien in Krimpen aan den IJssel: groepenkast, storing, inductie en laden met de kabelgoottegels van de gemeente. Reactie binnen 24 uur, prijs vooraf.",
          extra="""
<h2>Laden in Krimpen: <em>kabelgoottegels.</em></h2>
<p>Krimpen aan den IJssel heeft een eigen oplossing voor wie geen oprit heeft. Inwoners met een elektrische auto kunnen bij de gemeente kabelgoottegels aanvragen: speciale stoeptegels met een goot voor de laadkabel, afgedekt met een rubberen strip. Zo kunt u vanuit uw eigen woning laden, bijvoorbeeld met stroom van uw zonnepanelen, terwijl de auto op een openbare parkeerplaats staat. Volgens de gemeente is dit de enige manier waarop een laadkabel over de openbare weg mag.</p>
<ul class="checks">
  <li>{check}<span><strong>Voorwaarden van de gemeente.</strong> U heeft een elektrische auto en kunt niet binnen 100 meter van uw woning op eigen terrein parkeren. Tussen uw woning en de parkeerplaats ligt alleen een stoep. De goot loopt recht en is maximaal 3,2 meter. De parkeerplaats blijft openbaar en de tegels blijven van de gemeente.</span></li>
  <li>{check}<span><strong>Aanvragen.</strong> Via het e-loket van de gemeente, met een foto van de situatie. De gemeente legt de tegels aan tegen kostprijs en besluit binnen zes weken.</span></li>
  <li>{check}<span><strong>Wat wij doen.</strong> Een laadpunt aan de gevel of op uw eigen terrein, op een <a href="/groep-bijplaatsen-rotterdam/">eigen groep</a> met de juiste aardlekbeveiliging. We kijken eerst of uw <a href="/groepenkast-vervangen-rotterdam/">groepenkast</a> en aansluiting het aankunnen, en of <a href="/meterkast-verzwaren-rotterdam/">verzwaren</a> nodig is. Meer over laadpunten leest u op onze <a href="/laadpaal-installeren-rotterdam/">laadpaalpagina</a>.</span></li>
</ul>
<div class="note-box"><p><strong>Bron:</strong> <a href="https://krimpenaandenijssel.nl/producten/kabelgoottegels/" target="_blank" rel="noopener noreferrer">Kabelgoottegels</a>, gemeente Krimpen aan den IJssel (met een link naar de bindende voorwaarden).</p></div>

<h2>Elektra in <em>Krimpen.</em></h2>
<ul class="checks">
  <li>{check}<span><strong>Oude bebouwing langs de dijken.</strong> Hier kijken we eerst naar de staat van de <a href="/bedrading-vervangen-rotterdam/">bedrading</a> en of er een <a href="/aardlekschakelaar-rotterdam/">aardlekschakelaar</a> in de kast zit.</span></li>
  <li>{check}<span><strong>Wijken uit de jaren zestig en zeventig.</strong> In Kortland, Langeland en de andere uitbreidingswijken zit de groepenkast vaak vol. Voor <a href="/inductiekookplaat-aansluiten-rotterdam/">inductie</a>, een droger of een laadpunt is dan een extra groep of een nieuwe kast nodig.</span></li>
  <li>{check}<span><strong>Stormpolder.</strong> Voor bedrijfsruimtes verhelpen we storingen, plaatsen we verlichting en leggen we extra groepen aan.</span></li>
</ul>
<div class="note-box"><p><strong>Bron:</strong> Wikipedia over <a href="https://nl.wikipedia.org/wiki/Krimpen_aan_den_IJssel" target="_blank" rel="noopener noreferrer">Krimpen aan den IJssel</a>.</p></div>

<h2>Huur, flat <em>of VvE?</em></h2>
<p>Werk binnen uw eigen woning, zoals een extra stopcontact of lamp, kunt u meestal zelf laten doen. Voor de groepenkast, de bedrading of een laadpunt aan de gevel overlegt u eerst met uw verhuurder of VvE. Voor verhuurders en VvE's hebben we een <a href="/elektricien-verhuurders-vve-rotterdam/">aparte pagina</a>.</p>
"""),
    _city("elektricien-ridderkerk", "Ridderkerk", "lampje", "“Ridderkerk? Ik breng het licht.”",
          "Bolnes, Slikkerveer en het centrum", "Drievliet en Het Zand",
          "In Ridderkerk komen we in alle kernen: Bolnes, Slikkerveer, Rijsoord, het centrum, Oost, West en Drievliet/Het Zand, en ook op bedrijvenpark Donkersloot. Ridderkerk ligt direct naast Rotterdam-Zuid, dus we zijn er snel bij een storing.",
          [("Rekenen jullie extra voor Ridderkerk?",
            "U krijgt vooraf één duidelijke prijs voor de klus, zodat u niet achteraf wordt verrast."),
           ("Kan ik in Ridderkerk een openbare laadpaal aanvragen?",
            "Meestal niet meer. Sinds 2026 plaatst de gemeente openbare laadpalen op plekken waar de gegevens laten zien dat ze het meest nodig zijn. Een aanvraag kan alleen nog als u een eigen gehandicaptenparkeerplaats heeft. De gemeente verwacht medio 2027 nieuwe laadpalen te plaatsen."),
           ("Mag ik laden met een kabel over de stoep?",
            "Nee. In Ridderkerk mag u alleen vanuit uw woning laden als de auto op eigen terrein staat. Een kabel over de stoep mag niet, ook niet met een kabelgoot, mat of arm. De proef met een verlengd private aansluiting is afgerond; de gemeente werkt aan nieuw beleid."),
           ("Heb ik een vergunning nodig voor een laadpaal op mijn oprit?",
            "Nee, volgens de gemeente is voor een laadpaal op eigen terrein geen vergunning nodig. Huurt u, dan heeft u wel toestemming van de verhuurder nodig. Wij sluiten de laadpaal aan op een eigen groep in uw meterkast."),
           ("Ik heb een plek in een parkeergarage. Hoe kan ik laden?",
            "Dan gaat u in gesprek met uw VvE, want de garage is gemeenschappelijk. Een VvE kan subsidie krijgen voor onafhankelijk advies over laden. Wij denken graag mee over de aansluiting en de capaciteit van de installatie."),
           ("Mijn groepenkast in Bolnes of Slikkerveer is oud. Moet hij eruit?",
            "Niet altijd. Soms is uitbreiden genoeg, bijvoorbeeld met een extra groep of een aardlekschakelaar erbij. Zitten er nog draaizekeringen in of is er geen aardlekschakelaar, dan is vervangen vaak verstandiger. Stuur een foto van de meterkast, dan krijgt u advies en een prijs.")],
          mix="Ridderkerk bestaat uit oude dijkdorpen en nieuwere wijken. In de oudere straten van Bolnes, Slikkerveer, Rijsoord en het oude centrum komen we vaker een groepenkast met weinig groepen tegen. In Drievliet/Het Zand, de jongste uitbreiding, is de installatie nieuwer en gaan vragen vaker over een laadpaal, extra groepen of buitenverlichting.",
          desc="Elektricien in Ridderkerk: Bolnes, Slikkerveer, Rijsoord, centrum en Drievliet/Het Zand. Groepenkast, storing, laadpaal. Reactie binnen 24 uur.",
          extra="""
<h2>Elektra per kern <em>in Ridderkerk.</em></h2>
<p>Ridderkerk is gegroeid uit een paar dorpen langs de rivieren. Elke kern heeft zijn eigen karakter, en dat ziet u vaak terug in de meterkast.</p>
<ul class="checks">
  <li>{check}<span><strong>Bolnes en Slikkerveer.</strong> De twee kernen aan de rivier, waar vroeger scheepswerven zaten. In oudere woningen kijken we eerst naar de <a href="/bedrading-vervangen-rotterdam/">bedrading</a> en of er een <a href="/aardlekschakelaar-rotterdam/">aardlekschakelaar</a> in de kast zit, voordat we iets bijplaatsen.</span></li>
  <li>{check}<span><strong>Rijsoord.</strong> Het kleinste dorp van de gemeente, met molen De Kersenboom. Hier werken we vaak in vrijstaande en oudere woningen, waar een <a href="/groepenkast-vervangen-rotterdam/">nieuwe groepenkast</a> of een groep voor de schuur aan de orde is.</span></li>
  <li>{check}<span><strong>Centrum, Oost en West.</strong> Het centrum heeft een oude kern en sinds 2007 een nieuw centrum met gemeentehuis en winkels. In de wijken eromheen gaat het vaak om <a href="/groep-bijplaatsen-rotterdam/">extra groepen</a> voor een nieuwe keuken of <a href="/inductiekookplaat-aansluiten-rotterdam/">inductie</a>.</span></li>
  <li>{check}<span><strong>Drievliet/Het Zand.</strong> De jongste uitbreiding van Ridderkerk, met ruim 11.000 inwoners. Vragen gaan hier vaker over een laadpaal op eigen terrein, <a href="/buitenverlichting-tuinstopcontact-rotterdam/">buitenverlichting en een tuinstopcontact</a> of een <a href="/vrije-groep-stekkerbatterij-rotterdam/">vrije groep voor een stekkerbatterij</a>.</span></li>
  <li>{check}<span><strong>Donkersloot en andere bedrijventerreinen.</strong> Voor bedrijfsruimtes verhelpen we storingen, plaatsen we verlichting en leggen we extra groepen aan.</span></li>
</ul>
<div class="note-box"><p><strong>Bron:</strong> Wikipedia over <a href="https://nl.wikipedia.org/wiki/Ridderkerk" target="_blank" rel="noopener noreferrer">Ridderkerk</a>.</p></div>

<h2>Laadpaal in Ridderkerk: <em>wat mag wel?</em></h2>
<ul class="checks">
  <li>{check}<span><strong>Laden op eigen terrein.</strong> Dat mag, en voor een laadpaal op uw eigen oprit is geen vergunning nodig. Huurt u, vraag dan eerst toestemming aan de verhuurder. Wij plaatsen de <a href="/laadpaal-installeren-rotterdam/">laadpaal</a> op een eigen groep en kijken eerst of uw meterkast en aansluiting het aankunnen.</span></li>
  <li>{check}<span><strong>Geen kabel over de stoep.</strong> Ook niet met een kabelgoot, mat of arm over het trottoir. De proef met een verlengd private aansluiting is afgerond; de gemeente werkt aan nieuw beleid.</span></li>
  <li>{check}<span><strong>Openbare laadpalen op basis van gegevens.</strong> Sinds 2026 kiest de gemeente zelf de plekken. Een aanvraag kan alleen nog met een eigen gehandicaptenparkeerplaats. Staat er binnen 200 meter een laadpaal met genoeg capaciteit, dan komt er geen nieuwe bij.</span></li>
  <li>{check}<span><strong>Parkeergarage van een VvE?</strong> Dan regelt de VvE de laadoplossing. Voor onafhankelijk advies kan een VvE subsidie aanvragen bij RVO.</span></li>
</ul>
<div class="note-box"><p><strong>Bronnen:</strong> gemeente Ridderkerk over <a href="https://www.ridderkerk.nl/direct-regelen/wonen-leefomgeving-verbouwen/verkeer-en-vervoer/laadpalen-elektrische-autos/" target="_blank" rel="noopener noreferrer">laadpalen voor elektrische auto's</a> en de <a href="https://www.ridderkerk.nl/direct-regelen/wonen-leefomgeving-verbouwen/duurzaamheid/duurzaam/verlengd-private-aansluiting/" target="_blank" rel="noopener noreferrer">verlengd private aansluiting</a>.</p></div>

<h2>Huur <em>of VvE?</em></h2>
<p>Huurt u, dan kunt u werk binnen uw eigen woning, zoals een extra stopcontact of lamp, meestal zelf laten doen. Voor de groepenkast, de bedrading of een nieuwe groep overlegt u eerst met uw verhuurder. In een appartementengebouw beslist de VvE over gemeenschappelijke delen. Voor verhuurders en VvE's hebben we een <a href="/elektricien-verhuurders-vve-rotterdam/">aparte pagina</a>.</p>
"""),
]


# ---------------------------------------------------------------- INFO
# Plain information pages (no service schema, no FAQ, not in the service
# lists). Keep them factual: they describe what the site really does.
INFO_PAGES = [
    {
        "slug": "salderen-stopt-2027",
        "plain": True,
        "short": "Salderen stopt in 2027",
        "title": "Salderen stopt in 2027: wat moet er in uw meterkast?",
        "desc": "Op 1 januari 2027 stopt de salderingsregeling. Wat betekent dat voor uw zonnepanelen, meterkast, laadpaal en (stekker)batterij? Uitleg van een elektricien.",
        "eyebrow": "Uitleg",
        "h1": "Salderen stopt in 2027. <em>Wat nu?</em>",
        "lede": "Vanaf 1 januari 2027 mag u zonnestroom niet meer wegstrepen tegen wat u afneemt. Wat verandert er, en wat kan een elektricien in uw meterkast doen om meer van uw eigen stroom te gebruiken?",
        "body": """
<p><em>Laatst bijgewerkt: 18 november 2026.</em></p>

<h2>Wat verandert er <em>op 1 januari 2027?</em></h2>
<ul class="checks">
  <li>{check}<span><strong>Niet meer wegstrepen.</strong> Tot 2027 mag u de stroom die u teruglevert verrekenen met de stroom die u afneemt. Vanaf 1 januari 2027 mag dat niet meer.</span></li>
  <li>{check}<span><strong>Wel een terugleververgoeding.</strong> U krijgt een vergoeding voor de stroom die u teruglevert. Tot 2030 moet die minimaal 50 procent van het kale leveringstarief zijn.</span></li>
  <li>{check}<span><strong>Terugleverkosten blijven mogelijk.</strong> Leveranciers mogen alleen kosten rekenen die ze echt maken om de teruggeleverde stroom te verwerken. De ACM houdt toezicht.</span></li>
  <li>{check}<span><strong>Zonnepanelen blijven lonen.</strong> Volgens de Rijksoverheid gaan zonnepanelen gemiddeld 25 jaar mee en verdienen ze zich ruim binnen die tijd terug, ook na het einde van het salderen.</span></li>
</ul>
<div class="note-box"><p><strong>Bron:</strong> Rijksoverheid, <a href="https://www.rijksoverheid.nl/themas/klimaat-milieu-en-natuur/energie-thuis/salderingsregeling" target="_blank" rel="noopener noreferrer">Salderingsregeling stopt in 2027</a>.</p></div>

<h2>Zelf gebruiken <em>wordt belangrijker.</em></h2>
<p>Stroom uit uw eigen panelen is volgens Milieu Centraal ongeveer vier keer goedkoper dan stroom die u inkoopt. Huishoudens met zonnepanelen gebruiken gemiddeld zo'n 30 procent van hun zonnestroom zelf, vooral via apparaten die altijd aanstaan. Wie meer zelf gebruikt, koopt minder in.</p>
<p>De simpelste stap kost niets: zet de wasmachine, vaatwasser en droger aan als de zon schijnt, om de beurt. Heeft u een elektrische auto of een warmtepomp met een voorraadvat, laad of verwarm dan overdag.</p>
<div class="note-box"><p><strong>Bron:</strong> Milieu Centraal, <a href="https://www.milieucentraal.nl/energie-besparen/zonnepanelen/zonnestroom-als-de-saldering-stopt-dit-moet-je-weten/" target="_blank" rel="noopener noreferrer">Zonnestroom zonder saldering: dit moet je weten</a>.</p></div>

<h2>Wat een elektricien <em>in uw meterkast doet.</em></h2>
<p>Meer zelf gebruiken betekent vaak dat er meer apparaten tegelijk overdag draaien. Daar moet de installatie op berekend zijn. Dit zijn de klussen die wij het vaakst tegenkomen:</p>
<ul class="checks">
  <li>{check}<span><strong>Een eigen groep voor de omvormer.</strong> Sinds 1 januari 2017 moet de omvormer van zonnepanelen of een thuisbatterij altijd op een aparte groep. Daarvoor gold dat pas vanaf 600 watt, dus bij oudere installaties zit de omvormer soms op een groep met andere apparaten.</span></li>
  <li>{check}<span><strong>Losse groepen voor zware apparaten.</strong> Draaien wasmachine, droger en vaatwasser tegelijk, dan raakt één groep snel overbelast. <a href="/groep-bijplaatsen-rotterdam/">Een groep bijplaatsen</a> lost dat op.</span></li>
  <li>{check}<span><strong>Slim laden.</strong> Met een <a href="/laadpaal-installeren-rotterdam/">laadpaal</a> die op zonnestroom kan laden, gaat de auto vooral overdag aan de lader. Loadbalancing voorkomt dat de hoofdzekering eruit slaat.</span></li>
  <li>{check}<span><strong>Een vrije groep voor een stekkerbatterij.</strong> Op een groep met andere apparaten mag een stekkerbatterij volgens de NVWA maximaal 800 watt ontladen. Op een <a href="/vrije-groep-stekkerbatterij-rotterdam/">eigen, vrije groep</a> is het veiliger, omdat de bedrading dan niet ook andere apparaten hoeft te dragen.</span></li>
  <li>{check}<span><strong>Ruimte in de groepenkast.</strong> Zit de kast vol, of is hij verouderd, dan is <a href="/groepenkast-vervangen-rotterdam/">uitbreiden of vervangen</a> de eerste stap. Komen er ook een warmtepomp en een laadpaal, dan rekenen we uit of <a href="/meterkast-verzwaren-rotterdam/">verzwaren naar 3-fase</a> nodig is.</span></li>
</ul>

<div class="note-box"><p><strong>Bronnen:</strong> Vereniging Eigen Huis, <a href="https://www.eigenhuis.nl/kennisbank/wanneer-moet-een-elektrisch-apparaat-op-een-aparte-groep-worden-aangesloten-1746" target="_blank" rel="noopener noreferrer">wanneer moet een apparaat op een aparte groep</a>; Zonneplan, <a href="https://www.zonneplan.nl/thuisbatterij/thuisbatterij-met-stekker/wet-en-regelgeving" target="_blank" rel="noopener noreferrer">wet- en regelgeving thuisbatterij met stekker</a> (NVWA-grens van 800 watt).</p></div>

<h2>Thuisbatterij <em>of stekkerbatterij?</em></h2>
<p>Een batterij slaat zonnestroom op voor 's avonds. Een stekkerbatterij is klein en steekt u in het stopcontact; een vaste thuisbatterij is groter en wordt vast aangesloten. Of een batterij voor u loont, hangt af van uw verbruik, uw energiecontract en de prijs van de batterij. Reken dat vooraf goed door.</p>
<p>Thuisbatterijen moet u registreren via energieleveren.nl. Volgens RVO geldt die registratieplicht voor batterijsystemen van type A; een stekkerbatterij van 800 watt zit op de ondergrens daarvan. Aanmelden is gratis en eenmalig.</p>
<div class="note-box"><p><strong>Bron:</strong> RVO, <a href="https://www.rvo.nl/onderwerpen/netcongestie/registreer-uw-batterijsysteem" target="_blank" rel="noopener noreferrer">Registreer uw batterijsysteem</a>.</p></div>

<h2>Wat u <em>nu kunt doen.</em></h2>
<ol class="steps-list">
  <li><strong>Kijk naar uw verbruik.</strong> Welke apparaten kunt u naar overdag verplaatsen?</li>
  <li><strong>Maak een foto van uw meterkast.</strong> Daarop zien wij of de omvormer een eigen groep heeft, of er ruimte is voor extra groepen en hoe oud de kast is.</li>
  <li><strong>Stuur ons die foto via WhatsApp.</strong> U krijgt advies over wat zinvol is en een prijs vooraf. Geen batterij nodig? Dan zeggen we dat ook.</li>
</ol>
""",
        "faq": [
            ("Wanneer stopt de salderingsregeling?",
             "Op 1 januari 2027. Vanaf dan mag u teruggeleverde stroom niet meer verrekenen met de stroom die u afneemt. U krijgt wel een terugleververgoeding."),
            ("Hoe hoog is de terugleververgoeding na 2027?",
             "Dat bepaalt uw energieleverancier. Volgens de Rijksoverheid moet de vergoeding tot 2030 minimaal 50 procent van het kale leveringstarief zijn."),
            ("Moet ik mijn zonnepanelen uitzetten?",
             "Nee. Stroom die u zelf gebruikt, hoeft u niet in te kopen. Volgens Milieu Centraal is uw eigen zonnestroom ongeveer vier keer goedkoper dan ingekochte stroom."),
            ("Heb ik een thuisbatterij nodig?",
             "Niet per se. Eerst apparaten verplaatsen naar overdag en slim laden levert vaak al veel op. Of een batterij loont, hangt af van uw verbruik, contract en de prijs van de batterij."),
            ("Mag ik een stekkerbatterij in elk stopcontact steken?",
             "Op een groep met andere apparaten mag een stekkerbatterij volgens de NVWA maximaal 800 watt ontladen. Een eigen, vrije groep is veiliger, omdat de bedrading dan niet ook andere apparaten hoeft te dragen."),
            ("Moet de omvormer op een eigen groep?",
             "Ja. Sinds 1 januari 2017 moet de omvormer van zonnepanelen of een thuisbatterij altijd op een aparte groep. Bij oudere installaties zit hij soms op een groep met andere apparaten. Stuur ons een foto van uw meterkast, dan kijken we mee."),
        ],
    },
    {
        "slug": "privacy",
        "plain": True,
        "short": "Privacyverklaring",
        "title": "Privacyverklaring | AlleKlussers",
        "desc": "Hoe AlleKlussers (Boss Tech VOF) omgaat met uw gegevens: offerteaanvragen via formulier, WhatsApp of e-mail, Analytics, bewaartermijnen en uw rechten.",
        "eyebrow": "Privacy",
        "h1": "Privacy<em>verklaring.</em>",
        "lede": "Welke gegevens we van u krijgen, waarvoor we ze gebruiken en wat uw rechten zijn. Kort en in gewone taal.",
        "body": """
<p><em>Laatst bijgewerkt: 26 november 2026.</em></p>

<h2>Wie <em>wij zijn.</em></h2>
<p>AlleKlussers is een handelsnaam van Boss Tech VOF, Walravenstraat 17, 3074 NL Rotterdam (KvK 99149680). Wij zijn verantwoordelijk voor de gegevens die u ons geeft. Vragen over privacy kunt u sturen naar <a href="mailto:alleklussers@gmail.com">alleklussers@gmail.com</a>.</p>

<h2>Welke gegevens <em>we krijgen.</em></h2>
<p>We krijgen alleen gegevens die u zelf aan ons stuurt, bijvoorbeeld als u een offerte aanvraagt of een storing meldt:</p>
<ul class="checks">
  <li>{check}<span>uw naam, telefoonnummer en e-mailadres;</span></li>
  <li>{check}<span>het adres of de postcode en plaats waar de klus is;</span></li>
  <li>{check}<span>een omschrijving van de klus en eventueel foto's, bijvoorbeeld van uw meterkast;</span></li>
  <li>{check}<span>als u klant wordt: de afspraken, de offerte en de factuur.</span></li>
</ul>

<h2>Het formulier <em>op de website.</em></h2>
<p>Drukt u in het offerteformulier op 'Verstuur aanvraag', dan gaat uw aanvraag (naam, telefoon of e-mail, postcode, plaats, soort werk en omschrijving) naar ons e-mailadres. Daarvoor gebruiken we de dienst FormSubmit (formsubmit.co), die het bericht doorstuurt naar ons Gmail-account. De website zelf slaat niets op.</p>
<p>Kiest u in het formulier voor WhatsApp, dan zet het formulier uw bericht klaar in WhatsApp en verstuurt u het daar zelf. Berichten via WhatsApp lopen via WhatsApp (Meta), e-mails komen binnen in ons Gmail-account (Google). Voor FormSubmit, WhatsApp en Google gelden ook hun eigen privacyregels.</p>

<h2>Waarvoor <em>we ze gebruiken.</em></h2>
<ul class="checks">
  <li>{check}<span><strong>Uw vraag beantwoorden en een prijs maken.</strong> Dat doen we omdat u erom vraagt.</span></li>
  <li>{check}<span><strong>De klus plannen en uitvoeren.</strong> De vakmensen die het werk voor ons uitvoeren, krijgen alleen wat ze daarvoor nodig hebben: uw naam, het adres, uw telefoonnummer en wat er moet gebeuren.</span></li>
  <li>{check}<span><strong>Factureren en de administratie.</strong> Dat moeten we volgens de wet.</span></li>
</ul>
<p>We verkopen uw gegevens niet en gebruiken ze niet voor reclame van anderen.</p>

<h2>Hoe lang <em>we ze bewaren.</em></h2>
<p>We bewaren uw gegevens niet langer dan nodig. Wordt uw aanvraag geen opdracht, dan verwijderen we de gegevens als ze niet meer nodig zijn voor uw vraag. Facturen en de administratie bewaren we 7 jaar, omdat de Belastingdienst dat verplicht.</p>

<h2>Google Analytics <em>en cookies.</em></h2>
<p>We gebruiken Google Analytics om te zien hoe bezoekers onze website gebruiken, bijvoorbeeld welke pagina's worden bekeken en hoe vaak er op de WhatsApp-knop wordt gedrukt. Google Analytics plaatst daarvoor cookies. We gebruiken die cijfers alleen om de website te verbeteren.</p>
<p>U kunt cookies weigeren of verwijderen in de instellingen van uw browser. Google biedt ook een <a href="https://tools.google.com/dlpage/gaoptout" target="_blank" rel="noopener noreferrer">browser-add-on</a> om Google Analytics uit te zetten.</p>
<p>De lettertypen van de website worden geladen van Google Fonts. Daarbij ziet Google het IP-adres van uw apparaat. De website zelf staat bij Vercel; zoals elke webserver registreren hun servers technische gegevens, zoals uw IP-adres en het tijdstip van een bezoek.</p>

<h2>Uw <em>rechten.</em></h2>
<p>U mag ons vragen welke gegevens we van u hebben, en ze laten verbeteren of verwijderen. U kunt ook bezwaar maken tegen het gebruik ervan, het gebruik laten beperken of uw gegevens opvragen om ze aan een ander te geven. Stuur daarvoor een e-mail naar <a href="mailto:alleklussers@gmail.com">alleklussers@gmail.com</a>. We reageren binnen een maand.</p>
<p>Bent u het niet eens met hoe we met uw gegevens omgaan? Dan kunt u een klacht indienen bij de <a href="https://www.autoriteitpersoonsgegevens.nl/" target="_blank" rel="noopener noreferrer">Autoriteit Persoonsgegevens</a>.</p>

<h2>Wijzigingen</h2>
<p>Als we deze verklaring aanpassen, ziet u dat aan de datum bovenaan deze pagina.</p>
""",
        "faq": [],
    },
]


# Rotterdam-Zuid: our own part of town. Built with _city() and then given
# its own lede and intro, because "vanuit Rotterdam-Zuid naar Rotterdam-Zuid"
# reads oddly.
_zuid = _city("elektricien-rotterdam-zuid", "Rotterdam-Zuid", "schildje", "“Zuid? Daar zitten we zelf.”",
          "", "",
          "We werken in alle wijken op Zuid: in Feijenoord (Afrikaanderwijk, Bloemhof, Hillesluis, Feijenoord, Katendrecht, Noordereiland, Kop van Zuid en Vreewijk), in Charlois (Tarwewijk, Carnisse, Oud-Charlois, Zuidwijk, Pendrecht, Wielewaal en Heijplaat) en in IJsselmonde (Oud-IJsselmonde, Lombardijen, Groot-IJsselmonde, Beverwaard en De Veranda).",
          [("Komen jullie in heel Rotterdam-Zuid?",
            "Ja. We zitten zelf aan de Walravenstraat en werken in alle wijken van Feijenoord, Charlois en IJsselmonde, en ook net over de grens in Barendrecht, Ridderkerk en Albrandswaard."),
           ("Mijn portiekwoning in de Tarwewijk heeft nog draaizekeringen. Is dat gevaarlijk?",
            "Draaizekeringen zelf zijn niet meteen gevaarlijk, maar zo'n kast heeft meestal geen of te weinig aardlekschakelaars. Die schakelen de stroom uit als er stroom weglekt, bijvoorbeeld via een kapot apparaat. Stuur een foto van uw meterkast via WhatsApp, dan zeggen we of uitbreiden genoeg is of dat een nieuwe groepenkast verstandiger is."),
           ("Werken jullie ook in Vreewijk, met al die monumenten?",
            "Ja. Vreewijk is een beschermd stadsgezicht met bijna 300 monumenten. We overleggen vooraf hoe nieuwe leidingen zo netjes en onzichtbaar mogelijk lopen. Woont u in een rijksmonument, dan kan voor sommige aanpassingen een vergunning nodig zijn; dat zoeken we samen met u uit voordat we beginnen."),
           ("Ik huur van een woningcorporatie. Mag ik jullie inschakelen?",
            "Voor kleine dingen binnen uw woning, zoals een lamp of een extra stopcontact, meestal wel. De groepenkast, de bedrading en de meterkast zijn van de verhuurder; daarvoor meldt u zich eerst bij uw corporatie of verhuurder. Verhuurders en VvE's kunnen ons ook rechtstreeks inschakelen."),
           ("Kan ik inductie koken in mijn flat in Zuidwijk of Pendrecht?",
            "Meestal wel. De meeste inductiekookplaten hebben een kookgroep met perilex nodig; die kan vaak op een gewone 1-fase aansluiting. In flats uit de jaren vijftig zit vaak een kleine kast met weinig groepen, dus soms moet de kast eerst worden uitgebreid. Een foto van uw meterkast is genoeg voor een eerste antwoord."),
           ("Ik woon in een appartement op de Kop van Zuid. Kan ik een laadpaal in de parkeergarage krijgen?",
            "Dat beslist de VvE, want de parkeergarage is gemeenschappelijk. Vaak kiest een VvE voor één plan voor de hele garage, zodat de aansluiting niet overbelast raakt. We denken graag mee met het bestuur of de beheerder."),
           ("Mag ik in Rotterdam mijn auto laden met een kabel over de stoep?",
            "Nee. De gemeente Rotterdam staat geen laadkabel over of boven de stoep toe, ook niet afgedekt. Laad op eigen terrein of bij een openbare laadpaal. Meer staat op onze pagina over laadpalen.")],
          mix="Op Zuid staan woningen uit bijna elke periode van de vorige eeuw. In de vooroorlogse wijken bij de Maas, zoals de Tarwewijk en Bloemhof, zitten vaak nog oude groepenkasten en bedrading. In de naoorlogse wijken, zoals Zuidwijk, Pendrecht en Lombardijen, is de meterkast vaak klein en nooit aangepast aan inductie, een droger of een warmtepomp. Op de Kop van Zuid en in De Veranda is de installatie nieuw, en gaan vragen vaker over verlichting, extra stopcontacten of laden in de parkeergarage.",
          desc="Elektricien in Rotterdam-Zuid: Feijenoord, Charlois en IJsselmonde, van de Tarwewijk tot de Kop van Zuid. Storing, groepenkast, inductie. Reactie binnen 24 uur.",
          extra="""
<h2>Elektra per wijk <em>op Zuid.</em></h2>
<p>Rotterdam-Zuid bestaat uit drie gebieden: Feijenoord, Charlois en IJsselmonde. Wat er in uw meterkast hangt, hangt vooral af van wanneer uw wijk is gebouwd.</p>
<ul class="checks">
  <li>{check}<span><strong>Tarwewijk, Bloemhof en de andere wijken bij de Maas.</strong> De Tarwewijk is tussen 1900 en 1930 gebouwd voor havenarbeiders, met vooral portiekwoningen en kleine eengezinswoningen. Bloemhof is begin jaren twintig gebouwd. Hier komen we nog groepenkasten met draaizekeringen tegen, weinig groepen, geen <a href="/aardlekschakelaar-rotterdam/">aardlekschakelaar</a> en soms ruimtes zonder randaarde. Voordat we iets bijplaatsen, kijken we eerst naar de <a href="/bedrading-vervangen-rotterdam/">bedrading</a>.</span></li>
  <li>{check}<span><strong>Vreewijk.</strong> Het tuindorp waar in 1919 de eerste woningen werden opgeleverd. Vreewijk is een beschermd stadsgezicht met bijna 300 monumenten. We werken hier extra netjes en overleggen vooraf hoe nieuwe leidingen lopen.</span></li>
  <li>{check}<span><strong>Zuidwijk en Pendrecht.</strong> Gebouwd in de jaren vijftig. In Pendrecht waren de woningen bewust klein, gemiddeld niet groter dan 53 vierkante meter. De meterkast is in deze flats vaak krap. Voor een <a href="/inductiekookplaat-aansluiten-rotterdam/">inductiekookplaat</a>, droger of vaatwasser is vaak een <a href="/groep-bijplaatsen-rotterdam/">extra groep</a> nodig.</span></li>
  <li>{check}<span><strong>Lombardijen en Groot-IJsselmonde.</strong> Lombardijen is begin jaren zestig gebouwd, met rijtjeswoningen en flats. Bij een nieuwe keuken of verbouwing is <a href="/groepenkast-vervangen-rotterdam/">uitbreiden of vervangen van de groepenkast</a> hier vaak de eerste stap.</span></li>
  <li>{check}<span><strong>Kop van Zuid, Katendrecht en De Veranda.</strong> De Kop van Zuid is vanaf 1994 gebouwd op oude haventerreinen. In deze appartementen is de installatie modern; vragen gaan vaker over <a href="/lampen-ophangen-rotterdam/">verlichting</a>, <a href="/stopcontact-plaatsen-rotterdam/">extra stopcontacten</a> of laden in de parkeergarage van de VvE.</span></li>
</ul>
<div class="note-box"><p><strong>Bronnen:</strong> Wikipedia over <a href="https://nl.wikipedia.org/wiki/Rotterdam-Zuid" target="_blank" rel="noopener noreferrer">Rotterdam-Zuid</a>, de <a href="https://nl.wikipedia.org/wiki/Tarwewijk" target="_blank" rel="noopener noreferrer">Tarwewijk</a>, <a href="https://nl.wikipedia.org/wiki/Bloemhof_(Rotterdam)" target="_blank" rel="noopener noreferrer">Bloemhof</a>, <a href="https://nl.wikipedia.org/wiki/Vreewijk_(Rotterdam)" target="_blank" rel="noopener noreferrer">Vreewijk</a>, <a href="https://nl.wikipedia.org/wiki/Zuidwijk_(Rotterdam)" target="_blank" rel="noopener noreferrer">Zuidwijk</a>, <a href="https://nl.wikipedia.org/wiki/Pendrecht" target="_blank" rel="noopener noreferrer">Pendrecht</a>, <a href="https://nl.wikipedia.org/wiki/Lombardijen" target="_blank" rel="noopener noreferrer">Lombardijen</a> en de <a href="https://nl.wikipedia.org/wiki/Kop_van_Zuid" target="_blank" rel="noopener noreferrer">Kop van Zuid</a>.</p></div>

<h2>Storing op Zuid? <em>Wij zitten om de hoek.</em></h2>
<p>Valt de stroom uit of slaat de aardlekschakelaar steeds door? Kijk eerst of het bij u alleen is of in de hele straat. Is het alleen bij u, zet dan alle groepen uit en schakel ze een voor een weer in; zo ziet u welke groep het probleem geeft. Lukt het niet, stuur ons dan een berichtje. We zijn 24/7 bereikbaar en zitten zelf op Zuid. Meer tips staan op onze pagina over <a href="/storing-elektra-rotterdam/">storingen</a>.</p>

<h2>Huur, corporatie <em>of VvE?</em></h2>
<p>Op Zuid huren veel mensen hun woning, vaak van een woningcorporatie. Kleine dingen binnen uw woning, zoals een lamp of een extra stopcontact, kunt u meestal zelf laten doen. De groepenkast, de bedrading en de meterkast zijn van de verhuurder: meld problemen daarmee eerst bij uw corporatie of verhuurder. In appartementengebouwen beslist de VvE over gemeenschappelijke delen, zoals de verlichting in het trappenhuis of laadpalen in de parkeergarage. Voor verhuurders en VvE's hebben we een <a href="/elektricien-verhuurders-vve-rotterdam/">aparte pagina</a>.</p>

<h2>Laden <em>in Rotterdam.</em></h2>
<p>In Rotterdam mag een laadkabel niet over of boven de stoep, ook niet afgedekt. Heeft u een eigen oprit of garage, dan plaatsen we daar een <a href="/laadpaal-installeren-rotterdam/">laadpaal</a> op een eigen groep. Zonder eigen terrein laadt u bij een openbare laadpaal; op onze laadpaalpagina leest u hoe de gemeente die plaatst.</p>
""")
_zuid["lede"] = "Wij zitten zelf op Zuid, aan de Walravenstraat. Voor storingen, groepenkasten, inductie, verlichting en alles wat met elektra te maken heeft, in Feijenoord, Charlois en IJsselmonde."
_zuid["body"] = _zuid["body"].replace(
    "AlleKlussers is een elektrotechnisch bedrijf uit Rotterdam-Zuid. Rotterdam-Zuid ligt vlakbij, dus we zijn er snel.",
    "AlleKlussers is een elektrotechnisch bedrijf uit Rotterdam-Zuid; ons adres is Walravenstraat 17. Op Zuid zijn we dus snel bij u.")
_zuid["faq"] = [q for q in _zuid["faq"] if q[0] != "Komen jullie ook in Rotterdam-Zuid?"]
CITY_PAGES.insert(0, _zuid)


# Prins Alexander (Rotterdam-Oost): Search Console shows 'elektricien
# prins alexander' and 'elektricien zevenkamp'. Same pattern as Zuid.
_pa = _city("elektricien-prins-alexander", "Prins Alexander", "kastje", "“Ommoord, Zevenkamp of Nesselande? Wij komen.”",
          "", "",
          "We werken in alle wijken van Prins Alexander: Het Lage Land, Prinsenland en 's-Gravenland, Ommoord, Zevenkamp, Oosterflank, Kralingseveer en Nesselande. Ook net over de grens in Capelle aan den IJssel en Krimpen aan den IJssel zijn we snel.",
          [("Komen jullie ook in Nesselande en Zevenkamp?",
            "Ja. We werken in heel Prins Alexander, van Het Lage Land en Ommoord tot Zevenkamp en Nesselande, en ook in Capelle aan den IJssel."),
           ("Mijn flat in Ommoord heeft nog de oude groepenkast. Moet die eruit?",
            "Niet altijd. Ommoord is vanaf 1965 gebouwd; in woningen van voor 1975 zit vaak geen aardlekschakelaar, tenzij de kast later is vernieuwd. Soms is uitbreiden genoeg, soms is een nieuwe groepenkast verstandiger. Stuur een foto van uw meterkast via WhatsApp, dan krijgt u advies en een prijs."),
           ("Kan ik inductie koken in mijn woning in Zevenkamp?",
            "Meestal wel. De meeste inductiekookplaten hebben een kookgroep met perilex nodig; die kan vaak gewoon op een 1-fase aansluiting. We kijken of er ruimte is in de groepenkast of dat die eerst moet worden uitgebreid."),
           ("Mag ik in Rotterdam mijn auto laden met een kabel over de stoep?",
            "Nee. De gemeente Rotterdam staat geen laadkabel over of boven de stoep toe, ook niet afgedekt. Laad op eigen terrein of bij een openbare laadpaal."),
           ("Ik woon in een appartement met een VvE. Wie beslist over een laadpaal in de garage?",
            "De VvE, want de garage is gemeenschappelijk. Wij denken graag mee over de aansluiting en de capaciteit van de installatie, zodat er later meer laadpunten bij kunnen."),
           ("Ik huur mijn woning. Mag ik jullie inschakelen?",
            "Voor kleine dingen binnen uw woning, zoals een lamp of een extra stopcontact, meestal wel. De groepenkast, de bedrading en de meterkast zijn van de verhuurder; meld problemen daarmee eerst bij uw verhuurder of woningcorporatie.")],
          mix="Prins Alexander is na de oorlog in fasen gebouwd, en dat ziet u terug in de meterkast. In de woningen uit de jaren zestig in Het Lage Land en Ommoord komen we vaak een groepenkast tegen die nooit is aangepast aan inductie, een droger of een warmtepomp, soms zonder aardlekschakelaar. In Zevenkamp, gebouwd vanaf 1979, is de kast vaak wat jonger maar ook vol. In Nesselande, de jongste wijk, gaat het vaker om een laadpaal, buitenverlichting of extra groepen.",
          desc="Elektricien in Prins Alexander: Ommoord, Zevenkamp, Nesselande, Het Lage Land en Prinsenland. Groepenkast, storing, inductie. Reactie binnen 24 uur.",
          extra="""
<h2>Elektra per wijk <em>in Prins Alexander.</em></h2>
<p>Prins Alexander telt bijna 100.000 inwoners. De wijken zijn na elkaar gebouwd, van begin jaren zestig tot na 2000.</p>
<ul class="checks">
  <li>{check}<span><strong>Het Lage Land, Prinsenland en 's-Gravenland.</strong> De bouw van Het Lage Land begon in november 1961; kort daarna volgde Prinsenland, waarvan een deel pas in de jaren negentig werd gebouwd. In de oudere woningen is <a href="/groepenkast-vervangen-rotterdam/">uitbreiden of vervangen van de groepenkast</a> bij een nieuwe keuken vaak de eerste stap.</span></li>
  <li>{check}<span><strong>Ommoord.</strong> Vanaf 1965 gebouwd, met hoogbouw en laagbouw. In woningen van voor 1975 zit vaak geen <a href="/aardlekschakelaar-rotterdam/">aardlekschakelaar</a>, tenzij de kast later is vernieuwd. Voor een <a href="/inductiekookplaat-aansluiten-rotterdam/">inductiekookplaat</a> of droger is vaak een <a href="/groep-bijplaatsen-rotterdam/">extra groep</a> nodig.</span></li>
  <li>{check}<span><strong>Zevenkamp.</strong> In maart 1979 ging de eerste paal de grond in voor een woonwijk van 220 hectare. Hier gaat het vaak om een groepenkast die vol zit, extra stopcontacten of <a href="/buitenverlichting-tuinstopcontact-rotterdam/">buitenverlichting en een tuinstopcontact</a> bij een eengezinswoning.</span></li>
  <li>{check}<span><strong>Nesselande.</strong> Een Vinex-wijk waarvan de bouw in 2000 begon, met ruim 4.700 woningen. De installatie is hier nieuwer; vragen gaan vaker over een <a href="/laadpaal-installeren-rotterdam/">laadpaal</a> op eigen terrein, verlichting of een <a href="/vrije-groep-stekkerbatterij-rotterdam/">vrije groep voor een stekkerbatterij</a>.</span></li>
  <li>{check}<span><strong>Oosterflank en Kralingseveer.</strong> In Oosterflank en in Kralingseveer aan de Hollandse IJssel werken we in appartementen en eengezinswoningen, voor storingen, verlichting en extra groepen.</span></li>
</ul>
<div class="note-box"><p><strong>Bronnen:</strong> Wikipedia over <a href="https://nl.wikipedia.org/wiki/Prins_Alexander_(stadsdeel)" target="_blank" rel="noopener noreferrer">Prins Alexander</a>, <a href="https://nl.wikipedia.org/wiki/Ommoord" target="_blank" rel="noopener noreferrer">Ommoord</a> en <a href="https://nl.wikipedia.org/wiki/Nesselande" target="_blank" rel="noopener noreferrer">Nesselande</a>.</p></div>

<h2>Laden <em>in Rotterdam.</em></h2>
<p>In Rotterdam mag een laadkabel niet over of boven de stoep, ook niet afgedekt. Heeft u een oprit, carport of garage, dan plaatsen we daar een <a href="/laadpaal-installeren-rotterdam/">laadpaal</a> op een eigen groep, en kijken we eerst of uw meterkast en aansluiting het aankunnen. Zonder eigen terrein laadt u bij een openbare laadpaal; op onze laadpaalpagina leest u hoe de gemeente die plaatst.</p>

<h2>Huur, flat <em>of VvE?</em></h2>
<p>Werk binnen uw eigen woning, zoals een extra stopcontact of lamp, kunt u meestal zelf laten doen. Voor de groepenkast, de bedrading of gemeenschappelijke delen zoals de verlichting in het trappenhuis of laadpalen in de parkeergarage beslist de verhuurder of de VvE. Voor hen hebben we een <a href="/elektricien-verhuurders-vve-rotterdam/">aparte pagina</a>.</p>
""")
_pa["title"] = "Elektricien Prins Alexander, Ommoord, Zevenkamp | AlleKlussers"
_pa["lede"] = "Voor storingen, groepenkasten, inductie, verlichting en laadpalen in Ommoord, Zevenkamp, Nesselande, Het Lage Land, Prinsenland en Oosterflank."
_pa["body"] = _pa["body"].replace(
    "AlleKlussers is een elektrotechnisch bedrijf uit Rotterdam-Zuid. Prins Alexander ligt vlakbij, dus we zijn er snel.",
    "AlleKlussers is een elektrotechnisch bedrijf uit Rotterdam. Prins Alexander ligt aan de oostkant van de stad; via de ring zijn we er vanaf Zuid snel.")
_pa["faq"] = [q for q in _pa["faq"] if q[0] != "Komen jullie ook in Prins Alexander?"]
CITY_PAGES.insert(1, _pa)


# Albrandswaard (Rhoon, Poortugaal, Portland): people search the village
# names, so the title leads with them.
_alb = _city("elektricien-albrandswaard", "Albrandswaard", "lampje", "“Rhoon, Poortugaal of Portland? Wij komen.”",
          "", "",
          "Albrandswaard bestaat uit drie kernen: Rhoon, Poortugaal en Portland. We werken in alle drie, van de oude dijkbebouwing tot de nieuwbouw in Essendael en Portland. Vanuit Rotterdam-Zuid zijn we er via de A15 snel.",
          [("Komen jullie in Rhoon, Poortugaal en Portland?",
            "Ja. We werken in heel Albrandswaard, en ook in het naastgelegen Barendrecht en Hoogvliet."),
           ("Kan ik in Albrandswaard een openbare laadpaal aanvragen?",
            "Nee. Volgens de gemeente kunt u zelf geen openbare laadpaal meer aanvragen. Nieuwe laadpalen worden geplaatst op basis van verwachtingen en het gebruik van de bestaande palen. Heeft u een eigen oprit of garage, dan kunnen wij daar een laadpaal plaatsen."),
           ("Mag ik laden met een kabel over de stoep of door een kabelgoot?",
            "Nee. De gemeente Albrandswaard staat laden met een kabelgoot over de stoep niet toe. Laad op eigen terrein of bij een openbare laadpaal."),
           ("Mijn huis in 't Ghijseland is uit de jaren zeventig. Is de groepenkast nog goed?",
            "Vaak werkt hij nog, maar hij is ingericht op de apparaten van toen. In woningen van voor 1975 zit vaak geen aardlekschakelaar, tenzij de kast later is vernieuwd. Wilt u inductie, een droger of een laadpaal erbij, dan is er vaak een extra groep of een nieuwe kast nodig. Stuur een foto van uw meterkast."),
           ("Ik woon in Portland of Essendael. Wat kunnen jullie voor mij doen?",
            "In nieuwere woningen gaat het vaak om een laadpaal op eigen terrein, buitenverlichting, extra stopcontacten of een vrije groep voor een stekkerbatterij. We kijken eerst of er ruimte is in de groepenkast."),
           ("Ik heb een plek in een parkeergarage. Hoe kan ik laden?",
            "Dan gaat u in gesprek met uw VvE, want de garage is gemeenschappelijk. Een VvE kan subsidie krijgen voor onafhankelijk advies over laden. Wij denken graag mee over de aansluiting en de capaciteit van de installatie.")],
          mix="Rhoon en Poortugaal waren tot halverwege de vorige eeuw dijkdorpen. Daarna kwamen er in fasen nieuwe wijken bij, van de jaren vijftig tot na 2000. In de oudere straten komen we vaker een groepenkast met weinig groepen tegen; in Portland en Essendael is de installatie nieuwer en gaan vragen vaker over laden, verlichting en extra groepen.",
          desc="Elektricien in Albrandswaard: Rhoon, Poortugaal en Portland. Groepenkast, storing, inductie, laadpaal en verlichting. Reactie binnen 24 uur, prijs vooraf.",
          extra="""
<h2>Elektra per kern <em>in Albrandswaard.</em></h2>
<p>De gemeente Albrandswaard ontstond in 1985 uit Rhoon en Poortugaal. Sinds 2000 is Portland de derde kern, als deel van de Vinex-locatie Midden-IJsselmonde, samen met Carnisselande in Barendrecht.</p>
<ul class="checks">
  <li>{check}<span><strong>Rhoon.</strong> Tot halverwege de twintigste eeuw een lang dijkdorp, daarna sterk uitgebreid: rond de L.G. Molenaarstraat in de jaren vijftig, Rhoon-Zuid in de jaren vijftig en zestig, 't Ghijseland in de jaren zeventig, de Huyters en Rhoon-Noord in de jaren tachtig, en Essendael aan het begin van deze eeuw. Hoe ouder de wijk, hoe vaker <a href="/groepenkast-vervangen-rotterdam/">uitbreiden of vervangen van de groepenkast</a> nodig is voor inductie of een droger.</span></li>
  <li>{check}<span><strong>Poortugaal.</strong> Een oud dorp tussen de Rotterdamse havens en de Oude Maas, met wijken als Poortugaal-dorp, Valckestijn en Kasteeltuin. In oudere woningen kijken we eerst naar de <a href="/bedrading-vervangen-rotterdam/">bedrading</a> en of er een <a href="/aardlekschakelaar-rotterdam/">aardlekschakelaar</a> in de kast zit.</span></li>
  <li>{check}<span><strong>Portland.</strong> De jongste kern, gebouwd vanaf 2000. Hier gaat het vaak om een <a href="/laadpaal-installeren-rotterdam/">laadpaal</a> op eigen terrein, <a href="/buitenverlichting-tuinstopcontact-rotterdam/">buitenverlichting en een tuinstopcontact</a> of een <a href="/vrije-groep-stekkerbatterij-rotterdam/">vrije groep voor een stekkerbatterij</a>.</span></li>
</ul>
<div class="note-box"><p><strong>Bronnen:</strong> Wikipedia over <a href="https://nl.wikipedia.org/wiki/Albrandswaard" target="_blank" rel="noopener noreferrer">Albrandswaard</a>, <a href="https://nl.wikipedia.org/wiki/Rhoon" target="_blank" rel="noopener noreferrer">Rhoon</a> en <a href="https://nl.wikipedia.org/wiki/Poortugaal" target="_blank" rel="noopener noreferrer">Poortugaal</a>.</p></div>

<h2>Laadpaal in Albrandswaard: <em>wat mag wel?</em></h2>
<ul class="checks">
  <li>{check}<span><strong>Eigen terrein.</strong> Met een oprit, carport of garage kunt u een eigen laadpaal laten plaatsen en aansluiten op uw meterkast. Wij doen dat op een eigen groep en kijken eerst of uw aansluiting het aankan.</span></li>
  <li>{check}<span><strong>Geen kabelgoot over de stoep.</strong> Laden met een kabel door een kabelgoot over de stoep staat de gemeente niet toe.</span></li>
  <li>{check}<span><strong>Openbare laadpalen.</strong> Zelf aanvragen kan niet meer. De gemeente plaatst nieuwe palen op basis van verwachtingen en het gebruik van de bestaande palen; volgens de planning van de gemeente start de uitvoering van de nieuwe regionale concessie vanaf oktober 2026.</span></li>
  <li>{check}<span><strong>Parkeergarage van een VvE?</strong> Dan regelt de VvE de laadoplossing. Voor onafhankelijk advies kan een VvE subsidie aanvragen bij RVO.</span></li>
</ul>
<div class="note-box"><p><strong>Bron:</strong> <a href="https://www.albrandswaard.nl/direct-regelen/wonen-leefomgeving-verbouwen/parkeren/laadpalen-elektrische-autos/" target="_blank" rel="noopener noreferrer">Laadpalen elektrische auto's</a>, gemeente Albrandswaard.</p></div>

<h2>Huur <em>of VvE?</em></h2>
<p>Huurt u, dan kunt u werk binnen uw eigen woning, zoals een extra stopcontact of lamp, meestal zelf laten doen. Voor de groepenkast, de bedrading of een nieuwe groep overlegt u eerst met uw verhuurder. In een appartementengebouw beslist de VvE over gemeenschappelijke delen. Voor verhuurders en VvE's hebben we een <a href="/elektricien-verhuurders-vve-rotterdam/">aparte pagina</a>.</p>
""")
_alb["title"] = "Elektricien Rhoon, Poortugaal, Portland | AlleKlussers"
_alb["lede"] = "Vanuit Rotterdam-Zuid zijn we snel in Rhoon, Poortugaal en Portland. Voor storingen, groepenkasten, verlichting, laadpalen en alles wat met elektra te maken heeft."
_alb["faq"] = [q for q in _alb["faq"] if q[0] != "Komen jullie ook in Albrandswaard?"]
CITY_PAGES.append(_alb)


# Hoogvliet (Rotterdam): district on the Oude Maas, grew in the 1950s-60s.
_hv = _city("elektricien-hoogvliet", "Hoogvliet", "vonk", "“Hoogvliet? Via de A15 zijn we er zo.”",
          "", "",
          "We werken in heel Hoogvliet: in het Middengebied rond de Binnenban en de oude Dorpskerk, in Oudeland, Nieuw Engeland, Zalmplaat, Meeuwenplaat, Westpunt, Boomgaardshoek en Tussenwater, en op bedrijventerrein Gadering. Vanuit Rotterdam-Zuid zijn we er via de A15 snel, en ook in Pernis, Poortugaal en Rhoon komen we graag.",
          [("Komen jullie in heel Hoogvliet?",
            "Ja. Van Oudeland en Nieuw Engeland tot Zalmplaat, Meeuwenplaat, Boomgaardshoek en Tussenwater, en ook in Pernis en Poortugaal."),
           ("Mijn flat in Zalmplaat heeft een oude groepenkast. Moet die eruit?",
            "Niet altijd. In woningen van voor 1975 zit vaak geen aardlekschakelaar, tenzij de kast later is vernieuwd. Soms is uitbreiden genoeg, soms is vervangen verstandiger. Stuur een foto van uw meterkast via WhatsApp, dan krijgt u advies en een prijs."),
           ("Kan ik inductie koken in mijn woning in Hoogvliet?",
            "Meestal wel. De meeste inductiekookplaten hebben een kookgroep met perilex nodig; die kan vaak gewoon op een 1-fase aansluiting. We kijken eerst of er ruimte is in de groepenkast."),
           ("Mag ik in Hoogvliet mijn auto laden met een kabel over de stoep?",
            "Nee. Hoogvliet hoort bij de gemeente Rotterdam, en Rotterdam staat geen laadkabel over of boven de stoep toe, ook niet afgedekt. Laad op eigen terrein of bij een openbare laadpaal."),
           ("Ik huur mijn woning. Mag ik jullie inschakelen?",
            "Voor kleine dingen binnen uw woning, zoals een lamp of een extra stopcontact, meestal wel. De groepenkast, de bedrading en de meterkast zijn van de verhuurder; meld problemen daarmee eerst bij uw verhuurder of woningcorporatie."),
           ("Werken jullie ook voor bedrijven op Gadering?",
            "Ja. Voor bedrijfsruimtes verhelpen we storingen, plaatsen we verlichting en leggen we extra groepen aan.")],
          mix="Hoogvliet was lang een klein dijkdorp. In de jaren vijftig en zestig groeide het enorm, toen veel mensen kwamen wonen die in de petrochemische industrie werkten. Een groot deel van de woningen komt uit die periode; daar zit vaak een groepenkast die nooit is aangepast aan inductie, een droger of een warmtepomp. In Boomgaardshoek uit de jaren tachtig, het vernieuwde Nieuw Engeland en de jongste wijk Tussenwater is de installatie nieuwer.",
          desc="Elektricien in Hoogvliet: Oudeland, Zalmplaat, Meeuwenplaat, Boomgaardshoek en Tussenwater. Groepenkast, storing, inductie, laadpaal. Reactie binnen 24 uur.",
          extra="""
<h2>Elektra per wijk <em>in Hoogvliet.</em></h2>
<p>Hoogvliet hoort sinds 1934 bij Rotterdam en telt ruim 36.000 inwoners. Van het oude dorp is na de groei in de jaren vijftig en zestig weinig over; alleen rond de Dorpskerk staan nog enkele oorspronkelijke gebouwen.</p>
<ul class="checks">
  <li>{check}<span><strong>Middengebied en Oudeland.</strong> Rond winkelcentrum de Binnenban, metrostation Hoogvliet en de Wilhelm Tellplaats staan veel woningen uit de groeijaren. Bij een nieuwe keuken of verbouwing is <a href="/groepenkast-vervangen-rotterdam/">uitbreiden of vervangen van de groepenkast</a> vaak de eerste stap.</span></li>
  <li>{check}<span><strong>Zalmplaat en Meeuwenplaat.</strong> Wijken met hoog- en laagbouw; Meeuwenplaat is grootschalig gemoderniseerd. In flats is de meterkast vaak klein. Voor een <a href="/inductiekookplaat-aansluiten-rotterdam/">inductiekookplaat</a>, droger of vaatwasser is dan een <a href="/groep-bijplaatsen-rotterdam/">extra groep</a> nodig.</span></li>
  <li>{check}<span><strong>Nieuw Engeland.</strong> De eerste nieuwbouwwijk, uit de jaren dertig en kort na 1945, eind jaren tachtig grotendeels vervangen door nieuwe woningen. Vragen gaan hier vaker over extra stopcontacten, verlichting of een groep voor de droger.</span></li>
  <li>{check}<span><strong>Boomgaardshoek.</strong> Een typische jaren-80-wijk met woonerven en veel groen. Hier gaat het vaak om <a href="/buitenverlichting-tuinstopcontact-rotterdam/">buitenverlichting en een tuinstopcontact</a>, een laadpaal op eigen terrein of een <a href="/vrije-groep-stekkerbatterij-rotterdam/">vrije groep voor een stekkerbatterij</a>.</span></li>
  <li>{check}<span><strong>Tussenwater en Westpunt.</strong> Tussenwater is de jongste wijk van Hoogvliet; Westpunt ligt aan de Oude Maas bij het Ruigeplaatbos. In nieuwere woningen is de installatie modern; we helpen met <a href="/lampen-ophangen-rotterdam/">verlichting</a>, extra stopcontacten en storingen.</span></li>
</ul>
<div class="note-box"><p><strong>Bron:</strong> Wikipedia over <a href="https://nl.wikipedia.org/wiki/Hoogvliet_(stadsdeel)" target="_blank" rel="noopener noreferrer">Hoogvliet</a>.</p></div>

<h2>Laden <em>in Hoogvliet.</em></h2>
<p>Hoogvliet hoort bij Rotterdam, dus de Rotterdamse regels gelden: een laadkabel mag niet over of boven de stoep, ook niet afgedekt. Heeft u een oprit, carport of garage, dan plaatsen we daar een <a href="/laadpaal-installeren-rotterdam/">laadpaal</a> op een eigen groep, en kijken we eerst of uw meterkast en aansluiting het aankunnen. Zonder eigen terrein laadt u bij een openbare laadpaal.</p>

<h2>Huur, flat <em>of VvE?</em></h2>
<p>Werk binnen uw eigen woning, zoals een extra stopcontact of lamp, kunt u meestal zelf laten doen. Voor de groepenkast, de bedrading of gemeenschappelijke delen zoals de verlichting in het trappenhuis beslist de verhuurder of de VvE. Voor hen hebben we een <a href="/elektricien-verhuurders-vve-rotterdam/">aparte pagina</a>.</p>
""")
_hv["faq"] = [q for q in _hv["faq"] if q[0] != "Komen jullie ook in Hoogvliet?"]
CITY_PAGES.insert(2, _hv)
