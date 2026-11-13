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
    "storing-elektra-rotterdam": "Hallo AlleKlussers, ik heb een storing in mijn elektra. Wat er aan de hand is: ",
    "aardlekschakelaar-rotterdam": "Hallo AlleKlussers, mijn aardlekschakelaar slaat steeds door." + FOTO,
    "groepenkast-vervangen-rotterdam": "Hallo AlleKlussers, ik wil graag een prijs voor het vervangen of uitbreiden van mijn groepenkast." + FOTO,
    "groep-bijplaatsen-rotterdam": "Hallo AlleKlussers, ik wil graag een extra groep in mijn meterkast. Het is voor: ",
    "inductiekookplaat-aansluiten-rotterdam": "Hallo AlleKlussers, ik wil graag een inductiekookplaat laten aansluiten." + FOTO,
    "thuisbatterij-aansluiten-rotterdam": "Hallo AlleKlussers, ik wil graag een thuisbatterij laten aansluiten." + FOTO,
    "vrije-groep-stekkerbatterij-rotterdam": "Hallo AlleKlussers, ik wil graag een vrije groep voor mijn stekkerbatterij." + FOTO,
    "lampen-ophangen-rotterdam": "Hallo AlleKlussers, ik wil graag lampen laten ophangen. Het gaat om: ",
    "stopcontact-plaatsen-rotterdam": "Hallo AlleKlussers, ik wil graag stopcontacten laten plaatsen. Het gaat om: ",
    "buitenverlichting-tuinstopcontact-rotterdam": "Hallo AlleKlussers, ik wil graag buitenverlichting of een tuinstopcontact. Ik stuur een foto van de plek mee. Het gaat om: ",
    "bedrading-vervangen-rotterdam": "Hallo AlleKlussers, ik wil mijn bedrading laten controleren of vervangen. Het gaat om: ",
    "elektra-keuring-rotterdam": "Hallo AlleKlussers, ik wil mijn elektrische installatie laten keuren. Het is voor (aankoop, verhuur of eigen woning): ",
    "laadpaal-installeren-rotterdam": "Hallo AlleKlussers, ik wil graag een laadpaal laten installeren." + FOTO,
    "meterkast-verzwaren-rotterdam": "Hallo AlleKlussers, ik wil weten of ik mijn aansluiting moet laten verzwaren. Ik wil gaan gebruiken: ",
    "elektricien-verhuurders-vve-rotterdam": "Hallo AlleKlussers, ik ben verhuurder of beheerder en zoek een vaste elektricien. Het gaat om: ",
}

# Order here = order of tiles on the hub page and in the footer.
PAGES = [
    # ------------------------------------------------------------------ HUB
    {
        "slug": "elektricien-rotterdam",
        "short": "Elektricien Rotterdam",
        "title": "Elektricien Rotterdam | AlleKlussers, 24/7 bereikbaar",
        "desc": "Elektricien nodig in Rotterdam? AlleKlussers helpt bij storingen, groepenkasten, verlichting, stopcontacten en laadpalen. Verzekerd, binnen 24 uur reactie.",
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
<p>Sommige storingen kunt u zelf veilig nagaan voordat u ons een bericht stuurt:</p>
<ul class="checks">
  <li>{check}<span><strong>Heeft de buurt ook geen stroom?</strong> Dan ligt de storing waarschijnlijk bij de netbeheerder. In Rotterdam is dat Stedin.</span></li>
  <li>{check}<span><strong>Kijk in de meterkast.</strong> Staat er een groep of aardlekschakelaar omlaag? Haal dan eerst de stekkers van apparaten op die groep uit het stopcontact en zet de schakelaar weer omhoog.</span></li>
  <li>{check}<span><strong>Slaat hij direct weer door?</strong> Probeer het niet steeds opnieuw. Er is dan een fout in de installatie of in een apparaat, en die moet worden opgespoord.</span></li>
</ul>
<div class="note-box"><p><strong>Ruikt u een brandlucht, ziet u rook of zijn er vonken?</strong> Zet de hoofdschakelaar in de meterkast uit als dat veilig kan en bel bij gevaar direct 112.</p></div>

<h2>Veelvoorkomende <em>oorzaken.</em></h2>
<ul class="checks">
  <li>{check}<span><strong>Een defect apparaat,</strong> bijvoorbeeld een wasmachine, oven of waterkoker met lekstroom.</span></li>
  <li>{check}<span><strong>Vocht,</strong> vaak bij <a href="/buitenverlichting-tuinstopcontact-rotterdam/">buitenverlichting en buitenstopcontacten</a> of in de badkamer.</span></li>
  <li>{check}<span><strong>Een overbelaste groep,</strong> doordat te veel zware apparaten op dezelfde groep zitten.</span></li>
  <li>{check}<span><strong>Verouderde bedrading of een oude groepenkast</strong> die niet meer goed beveiligt.</span></li>
</ul>

<h2>Wat wij <em>doen.</em></h2>
<p>Onze elektricien meet de installatie door en zoekt groep voor groep uit waar de fout zit. Daarna lossen we het op, of bespreken we eerst met u wat er nodig is als de reparatie groter is. U krijgt uitleg over de oorzaak en advies om herhaling te voorkomen.</p>
<p>Gaat het om een aardlekschakelaar die steeds doorslaat? Op onze pagina over de <a href="/aardlekschakelaar-rotterdam/">aardlekschakelaar</a> staat een stappenplan om zelf de groep of het apparaat te vinden.</p>
<p>Valt steeds dezelfde groep uit als twee zware apparaten tegelijk aanstaan, zoals de wasmachine en de droger? Dan zit die groep te vol en is <a href="/groep-bijplaatsen-rotterdam/">een extra groep</a> de oplossing.</p>
""",
        "faq": [
            ("Mijn aardlekschakelaar slaat steeds door. Wat nu?",
             "Haal alle stekkers op die groep eruit en zet de aardlekschakelaar weer omhoog. Blijft hij staan, steek de apparaten dan één voor één terug om te zien welk apparaat de storing geeft. Slaat hij ook zonder apparaten door, dan zit de fout in de installatie en is een elektricien nodig."),
            ("De hele straat heeft geen stroom. Moet ik jullie inschakelen?",
             "Nee, dan is het een storing in het net. Die meldt u bij de netbeheerder; in Rotterdam is dat Stedin."),
            ("Zijn jullie ook 's avonds en in het weekend bereikbaar?",
             "Ja, we zijn 24/7 bereikbaar. Stuur ons een WhatsApp, dan kijken we hoe snel we bij u kunnen zijn."),
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
  <li>{check}<span><strong>U neemt iets zwaars in gebruik,</strong> zoals een <a href="/inductiekookplaat-aansluiten-rotterdam/">inductiekookplaat</a>, laadpaal, warmtepomp, zonnepanelen of een <a href="/thuisbatterij-aansluiten-rotterdam/">thuisbatterij</a>.</span></li>
  <li>{check}<span><strong>U gaat verbouwen</strong> en er komen nieuwe aansluitingen bij.</span></li>
</ul>

<h2>Wat wij <em>doen.</em></h2>
<p>We bekijken eerst uw huidige meterkast en bespreken wat u nodig heeft, nu en in de toekomst. Daarna vervangen of breiden we de groepenkast uit met de juiste aardlekbeveiliging, verdelen we de groepen logisch en zetten we op elke groep duidelijk waar hij voor is. Tot slot testen we alles en leggen we uit hoe uw nieuwe kast werkt.</p>
<p>Alles volgens NEN 1010, door gecertificeerde en verzekerde elektriciens.</p>
<p>Is uw kast nog goed en heeft u alleen een groep te weinig, bijvoorbeeld voor de droger of de airco? Dan is <a href="/groep-bijplaatsen-rotterdam/">een groep bijplaatsen</a> vaak genoeg.</p>

<div class="note-box"><p><strong>Zware aansluiting nodig?</strong> Voor bijvoorbeeld een laadpaal of warmtepomp kan uw aansluiting te licht zijn. Een verzwaring vraagt u aan bij de netbeheerder (Stedin). Wij vertellen u eerlijk of dat nodig is. Lees meer over <a href="/meterkast-verzwaren-rotterdam/">meterkast verzwaren</a>.</p></div>
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
        "desc": "Inductiekookplaat laten aansluiten in Rotterdam? Wij controleren uw meterkast, plaatsen een kookgroep met perilex en sluiten de kookplaat veilig aan.",
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
  <li>{check}<span><strong>3-fase krachtstroom, circa 11.000 watt.</strong> Alleen nodig voor sommige grote kookplaten en fornuizen. Kan uw kookplaat ook op twee fasen, dan is dat meestal de eenvoudigste keuze.</span></li>
</ul>

<h2>Zo herkent u wat er <em>nu in uw meterkast zit.</em></h2>
<ul class="checks">
  <li>{check}<span><strong>Een dubbele schakelaar met één hendel</strong> en een rond stopcontact met vijf gaatjes in de keuken: u heeft al een kookgroep. Dan is aansluiten vaak alleen de kookplaat monteren, een perilex-stekker aan het snoer zetten en testen.</span></li>
  <li>{check}<span><strong>Geen kookgroep,</strong> wat vaak voorkomt in woningen waar altijd op gas is gekookt: dan plaatsen we een kookgroep in de groepenkast en trekken we een nieuwe kabel naar de keuken.</span></li>
  <li>{check}<span><strong>Een volle of oude groepenkast,</strong> met draaistoppen of zonder plek voor een extra groep: dan moet de kast eerst worden <a href="/groepenkast-vervangen-rotterdam/">uitgebreid of vervangen</a>.</span></li>
</ul>
<p>Stuur ons een foto van uw meterkast en het typeplaatje of de productpagina van uw kookplaat. Dan zien we meestal al wat er nodig is.</p>

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
  <li>{check}<span><strong>Uw kookplaat, warmtepomp of ander apparaat</strong> is alleen in een 3-fase uitvoering te krijgen.</span></li>
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
    # -------------------------------------------------------- THUISBATTERIJ
    {
        "slug": "thuisbatterij-aansluiten-rotterdam",
        "short": "Thuisbatterij aansluiten",
        "sub": "Eigen groep en meterkast klaar voor 2027.",
        "title": "Thuisbatterij aansluiten Rotterdam | Vóór 2027 | AlleKlussers",
        "desc": "Thuisbatterij laten aansluiten in Rotterdam? Salderen stopt op 1 januari 2027. Wij controleren uw meterkast en sluiten de batterij aan op een eigen groep.",
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
  <li>{check}<span><strong>Stekkerbatterij:</strong> steekt u zelf in een stopcontact. Er is geen installateur nodig, maar de capaciteit is beperkt. Veiliger is een <a href="/vrije-groep-stekkerbatterij-rotterdam/">vrije groep voor uw stekkerbatterij</a>; die leggen wij aan.</span></li>
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
             "Voor stekkerbatterijen geldt geen registratieplicht bij de netbeheerder. Een vaste thuisbatterij meldt u wel aan via energieleveren.nl."),
        ],
    },
    # ------------------------------------------------------------ VERLICHTING
    {
        "slug": "lampen-ophangen-rotterdam",
        "short": "Lampen ophangen",
        "sub": "Plafondlampen, spots, dimmers en buitenverlichting.",
        "title": "Lampen ophangen Rotterdam | Verlichting | AlleKlussers",
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
  <li>{check}<span><strong>Buitenverlichting</strong> aan de gevel, in de tuin of bij de voordeur, waterdicht aangesloten. Meer daarover bij <a href="/buitenverlichting-tuinstopcontact-rotterdam/">buitenverlichting en tuinstopcontact</a>.</span></li>
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
  <li>{check}<span><strong>Buitenstopcontacten</strong> voor tuin, balkon of terras, spatwaterdicht. Zie <a href="/buitenverlichting-tuinstopcontact-rotterdam/">tuinstopcontact en buitenverlichting</a>.</span></li>
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
        "desc": "Oude bedrading vervangen of nieuwe aansluitingen nodig in Rotterdam? Voor keuken, wasmachine en apparatuur. Verzekerde vakmensen, duidelijke prijs vooraf.",
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
        "title": "Elektra keuring Rotterdam | Bij aankoop of verhuur | AlleKlussers",
        "desc": "Elektrische installatie laten keuren in Rotterdam? Bij aankoop, verhuur of na een verbouwing. Wij meten na, u krijgt een helder overzicht en advies vooraf.",
        "service": "Keuring van elektrische installaties",
        "char": "schildje",
        "say": "“Veilig of niet? Ik zoek het uit.”",
        "eyebrow": "Keuring en veiligheid",
        "h1": "Elektra keuring in <em>Rotterdam.</em>",
        "lede": "Een controle van de elektrische installatie in uw woning of huurwoning, met metingen waar nodig en een helder overzicht van wat in orde is, wat aandacht nodig heeft en wat meteen moet.",
        "body": """
<h2>Wanneer is een keuring <em>verstandig?</em></h2>
<ul class="checks">
  <li>{check}<span><strong>Bij aankoop van een woning,</strong> zodat u voor de koop weet of er kosten aankomen aan de elektra.</span></li>
  <li>{check}<span><strong>Bij verhuur en bij een wisseling van huurder,</strong> zodat de nieuwe huurder in een veilige woning start. Lees ook wat we doen <a href="/elektricien-verhuurders-vve-rotterdam/">voor verhuurders en VvE's</a>.</span></li>
  <li>{check}<span><strong>Na een verbouwing,</strong> of als een vorige eigenaar of een klusser zelf aan de elektra heeft gewerkt.</span></li>
  <li>{check}<span><strong>Voordat u zwaardere apparaten neemt,</strong> zoals een inductiekookplaat, warmtepomp of laadpaal. Dan weten we of de groepenkast en de aansluiting dat aankunnen.</span></li>
  <li>{check}<span><strong>In een ouder huis,</strong> of als groepen of de aardlekschakelaar vaak doorslaan.</span></li>
</ul>

<h2>Is een keuring <em>verplicht?</em></h2>
<p>Voor woningen is er in Nederland geen wettelijke keuringsplicht voor de elektra, ook niet bij verkoop of verhuur. Wel is de eigenaar verantwoordelijk voor een veilige installatie. Voor een vrijwillige veiligheidscontrole van bestaande woningen bestaat sinds 2005 de NTA 8025, ook bekend als de 'Woning-APK' (<a href="https://www.brandveilig.com/nieuws/nieuwe-woning-apk-nen-8025-op-komst-54008" target="_blank" rel="noopener noreferrer">brandveilig.com</a>).</p>
<p>Voor bedrijfspanden ligt dat anders. Daar vraagt de verzekeraar of de Arbowet soms een SCIOS-inspectie, zoals Scope 8 of Scope 10, door een bedrijf dat volgens de SCIOS-regels keurt (<a href="https://www.unive.nl/zakelijk/blog/hoe-zit-het-ook-alweer-met-de-verplichte-elektrakeuringen" target="_blank" rel="noopener noreferrer">Univé</a>). De controle op deze pagina is bedoeld voor woningen en is geen SCIOS-inspectie. Punten die uit zo'n inspectie komen, kunnen we wel voor u herstellen.</p>

<h2>Bij aankoop: meer dan <em>de bouwkundige keuring.</em></h2>
<p>Een bouwkundige keuring is een globale, visuele inspectie. De elektra wordt daarbij meestal alleen bekeken, niet doorgemeten. Dat blijkt ook uit een uitspraak van de Geschillencommissie: een koper ontdekte pas na de overdracht problemen met de elektra, en de bouwkundig keurder was daar niet verantwoordelijk voor (<a href="https://www.degeschillencommissie.nl/uitspraken/gebreken-pas-na-aankoop-ontdekt-maar-keurder-niet-verantwoordelijk/" target="_blank" rel="noopener noreferrer">degeschillencommissie.nl</a>).</p>
<p>Bij een elektra keuring kijken we gericht naar de installatie: we openen de groepenkast, testen de aardlekbeveiliging en meten waar dat nodig is. Zo weet u of er een nieuwe groepenkast, extra groepen of nieuwe bedrading nodig is, en kunt u dat meenemen in uw beslissing en uw budget.</p>
<div class="note-box"><p><strong>Tip voor kopers:</strong> heeft u een voorbehoud voor een bouwkundige keuring, plan de elektra keuring dan in dezelfde periode, voordat die termijn verloopt. Vraag via de makelaar of de verkoper toestemming om de woning te bezoeken. Stuur ons alvast het adres, het bouwjaar en een foto van de meterkast uit de advertentie.</p></div>

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
  <li><strong>Stuur ons via WhatsApp</strong> het adres of de wijk, het bouwjaar, waarvoor de keuring is (aankoop, verhuur of uw eigen woning) en een foto van de meterkast als u die heeft.</li>
  <li><strong>U krijgt een duidelijke prijs vooraf</strong> en we plannen een moment. Bij aankoop stemmen we dat af met de makelaar of de verkoper.</li>
  <li><strong>Wij controleren de installatie.</strong> Voor sommige metingen gaat de stroom per groep even uit. Houd daar rekening mee met de computer en de vriezer.</li>
  <li><strong>U krijgt het overzicht en ons advies,</strong> en als u dat wilt een offerte voor het herstel.</li>
</ol>
<p>Alles volgens NEN 1010, door verzekerde vakmensen. Blijkt de groepenkast aan vervanging toe, kijk dan bij <a href="/groepenkast-vervangen-rotterdam/">groepenkast vervangen</a>.</p>
""",
        "faq": [
            ("Is een elektra keuring verplicht bij aankoop of verhuur?",
             "Nee, voor woningen is er geen wettelijke keuringsplicht. De eigenaar is wel verantwoordelijk voor een veilige installatie. Een keuring geeft u zekerheid voordat u koopt, verhuurt of gaat verbouwen."),
            ("Wat is het verschil met een bouwkundige keuring?",
             "Een bouwkundige keuring is een globale, visuele inspectie van de hele woning. De elektra wordt daarbij meestal alleen bekeken. Bij een elektra keuring openen we de groepenkast, testen we de aardlekbeveiliging en meten we waar dat nodig is."),
            ("Hoe lang duurt een keuring?",
             "Dat hangt af van de grootte van de woning of het pand. Voor een gewone woning is het meestal binnen een paar uur klaar."),
            ("Moet de stroom eraf tijdens de keuring?",
             "Voor sommige metingen gaat de stroom per groep even uit. Dat duurt kort, maar zet de computer uit en houd de vriezer dicht."),
            ("Krijg ik een verslag?",
             "Ja, u krijgt een overzicht van wat we hebben gecontroleerd, wat we hebben gevonden en wat we adviseren. Per punt staat erbij hoe dringend het is."),
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
        "desc": "Laadpaal laten installeren in Rotterdam? We controleren uw meterkast, leggen een eigen groep aan en sluiten de laadpaal veilig aan. Duidelijke prijs vooraf.",
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
<p>Met een slimme laadpaal kunt u laden wanneer stroom goedkoop is of als uw zonnepanelen leveren. Met loadbalancing verdeelt de laadpaal het vermogen, zodat uw hoofdzekering niet doorslaat als ook de oven en de wasmachine aan staan. Zo is een laadpaal vaak ook mogelijk zonder uw <a href="/meterkast-verzwaren-rotterdam/">aansluiting te verzwaren</a>. We helpen ook met andere slimme schakelingen voor licht en apparaten.</p>
""",
        "faq": [
            ("Is mijn meterkast geschikt voor een laadpaal?",
             "Dat controleren we eerst. Vaak is een extra groep genoeg; soms is een zwaardere aansluiting bij Stedin nodig. Dat hoort u vooraf van ons. Meer uitleg vindt u op onze pagina over meterkast verzwaren."),
            ("Welke laadpaal moet ik kiezen?",
             "Dat hangt af van uw auto, uw aansluiting en of u slim wilt laden. We adviseren u graag."),
            ("Wat is loadbalancing?",
             "Loadbalancing zorgt dat de laadpaal minder vermogen gebruikt als andere apparaten veel stroom vragen. Zo slaat uw hoofdzekering niet door."),
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


def _city(slug, name, char, say, wijken_oud, wijken_nieuw, local, faq_extra):
    return {
        "slug": slug,
        "city": name,
        "short": f"Elektricien {name}",
        "title": _city_title(name),
        "desc": f"Elektricien nodig in {name}? Voor storingen, groepenkasten, verlichting, stopcontacten en laadpalen. Binnen 24 uur reactie, prijs vooraf.",
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
<p>In oudere wijken zoals {wijken_oud} komen we vaak verouderde groepenkasten en bedrading tegen. In nieuwere wijken zoals {wijken_nieuw} gaat het vaker om een laadpaal, een thuisbatterij of extra groepen voor inductie.</p>

<h2>Waarmee wij u <em>helpen in {name}.</em></h2>
<ul class="checks">
  <li>{{check}}<span><a href="/storing-elektra-rotterdam/">Storing verhelpen</a>: stroomuitval of een aardlekschakelaar die steeds doorslaat.</span></li>
  <li>{{check}}<span><a href="/groepenkast-vervangen-rotterdam/">Groepenkast vervangen of uitbreiden</a>, bijvoorbeeld voor <a href="/inductiekookplaat-aansluiten-rotterdam/">inductie</a> of een warmtepomp.</span></li>
  <li>{{check}}<span><a href="/groep-bijplaatsen-rotterdam/">Groep bijplaatsen</a> voor de wasmachine, droger, oven of airco.</span></li>
  <li>{{check}}<span><a href="/thuisbatterij-aansluiten-rotterdam/">Thuisbatterij aansluiten</a> op een eigen groep, op tijd voor 2027.</span></li>
  <li>{{check}}<span><a href="/lampen-ophangen-rotterdam/">Lampen ophangen</a>, spots en dimmers.</span></li>
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
          "Barendrecht ligt op een paar minuten van ons in Rotterdam-Zuid. In Carnisselande en Smitshoek wonen veel gezinnen met een auto voor de deur en zonnepanelen op het dak; daar gaat het vaak om een laadpaal, extra groepen of een vrije groep voor een stekkerbatterij.",
          [("Kunnen jullie een laadpaal en een groep voor een stekkerbatterij tegelijk aanleggen?",
            "Ja. We kijken eerst of uw meterkast en aansluiting dat aankunnen en geven de laadpaal en de batterij elk een eigen groep.")]),
    _city("elektricien-ridderkerk", "Ridderkerk", "lampje", "“Ridderkerk? Ik breng het licht.”",
          "Bolnes, Slikkerveer en het centrum", "Drievliet en Het Zand",
          "In Ridderkerk komen we in alle kernen: Bolnes, Slikkerveer, Rijsoord, Drievliet, Het Zand en het centrum. Ridderkerk ligt direct naast Rotterdam-Zuid, dus we zijn er snel bij een storing.",
          [("Rekenen jullie extra voor Ridderkerk?",
            "U krijgt vooraf één duidelijke prijs voor de klus, zodat u niet achteraf wordt verrast.")]),
]
