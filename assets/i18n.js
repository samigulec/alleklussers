/*
 * AlleKlussers — all interface text in six languages.
 * Order in every array: nl, en, tr, ar, pl, de.
 * Dutch is also written in index.html, so the page reads well before JS runs.
 */
window.AK_LANGS = ['nl', 'en', 'tr', 'ar', 'pl', 'de'];

window.AK_I18N = {
  // Navigation
  'nav.home': ['Home', 'Home', 'Ana sayfa', 'الرئيسية', 'Strona główna', 'Startseite'],
  'nav.services': ['Diensten', 'Services', 'Hizmetler', 'الخدمات', 'Usługi', 'Leistungen'],
  'nav.projects': ['Projecten', 'Projects', 'Projeler', 'المشاريع', 'Projekty', 'Projekte'],
  'nav.about': ['Over ons', 'About us', 'Hakkımızda', 'من نحن', 'O nas', 'Über uns'],
  'nav.contact': ['Contact', 'Contact', 'İletişim', 'اتصل بنا', 'Kontakt', 'Kontakt'],
  'nav.menu': ['Menu', 'Menu', 'Menü', 'القائمة', 'Menu', 'Menü'],
  'nav.lang': ['Taal kiezen', 'Choose language', 'Dil seçin', 'اختر اللغة', 'Wybierz język', 'Sprache wählen'],
  'nav.skip': ['Naar de inhoud', 'Skip to content', 'İçeriğe geç', 'انتقل إلى المحتوى', 'Przejdź do treści', 'Zum Inhalt'],
  'nav.close': ['Sluiten', 'Close', 'Kapat', 'إغلاق', 'Zamknij', 'Schließen'],
  'nav.prev': ['Vorige', 'Previous', 'Önceki', 'السابق', 'Poprzednie', 'Zurück'],
  'nav.next': ['Volgende', 'Next', 'Sonraki', 'التالي', 'Następne', 'Weiter'],

  // Top bar + trust
  'top.247': ['24/7 bereikbaar', '24/7 reachable', '7/24 ulaşılabilir', 'متاحون 24/7', 'Dostępni 24/7', '24/7 erreichbar'],
  'top.insured': ['Verzekerde vakmensen', 'Insured craftsmen', 'Sigortalı ustalar', 'حرفيون مؤمَّنون', 'Ubezpieczeni fachowcy', 'Versicherte Handwerker'],
  'top.nen': ['NEN 1010 gecertificeerd', 'NEN 1010 certified', 'NEN 1010 sertifikalı', 'معتمد وفق NEN 1010', 'Certyfikat NEN 1010', 'NEN 1010 zertifiziert'],
  'trust.certified': ['Gecertificeerde vakmensen', 'Certified craftsmen', 'Sertifikalı ustalar', 'حرفيون معتمدون', 'Certyfikowani fachowcy', 'Zertifizierte Handwerker'],
  'trust.viaMail': ['Via mail of WhatsApp', 'Via mail or WhatsApp', 'Mail veya WhatsApp ile', 'عبر البريد أو واتساب', 'Przez mail lub WhatsApp', 'Per Mail oder WhatsApp'],
  'trust.reply24': ['Binnen 24 uur reactie', 'Reply within 24 hours', '24 saat içinde yanıt', 'ردٌّ خلال 24 ساعة', 'Odpowiedź w 24 godziny', 'Antwort innerhalb 24 h'],
  'trust.reply24Sub': ['Inclusief offerte op maat', 'Including a tailored quote', 'Özel teklif dahil', 'بما في ذلك عرض مخصص', 'W tym oferta na miarę', 'Inkl. maßgeschneidertem Angebot'],
  'trust.talk': ['Vrijblijvend gesprek', 'No-obligation talk', 'Ücretsiz görüşme', 'استشارة مجانية', 'Niezobowiązująca rozmowa', 'Unverbindliches Gespräch'],
  'trust.talkSub': ['Bij u thuis', 'At your home', 'Evinizde', 'في منزلكم', 'U Państwa w domu', 'Bei Ihnen zu Hause'],
  'trust.onTime': ['Op tijd opgeleverd', 'Delivered on time', 'Zamanında teslim', 'تسليم في الموعد', 'Dostarczone na czas', 'Pünktlich geliefert'],
  'trust.onTimeSub': ['Zoals afgesproken', 'As agreed', 'Anlaştığımız gibi', 'كما هو متفق عليه', 'Zgodnie z umową', 'Wie vereinbart'],
  'trust.prices': ['Transparante prijzen', 'Transparent pricing', 'Şeffaf fiyatlar', 'أسعار شفافة', 'Przejrzyste ceny', 'Transparente Preise'],
  'trust.pricesSub': ['Geen verrassingen achteraf.', 'No surprises afterwards.', 'Sonradan sürpriz yok.', 'لا مفاجآت لاحقاً.', 'Bez niespodzianek na końcu.', 'Keine Überraschungen danach.'],
  'trust.advice': ['Gratis telefonisch advies', 'Free phone advice', 'Ücretsiz telefonla danışma', 'استشارة هاتفية مجانية', 'Bezpłatna porada telefoniczna', 'Kostenlose Telefonberatung'],
  'trust.adviceSub': ['Snel antwoord op al uw vragen.', 'Quick answer to all your questions.', 'Sorularınıza hızlı yanıt.', 'إجابة سريعة على كل أسئلتكم.', 'Szybka odpowiedź na wszystkie pytania.', 'Schnelle Antwort auf alle Fragen.'],
  'trust.install': ['Vakkundige installatie', 'Expert installation', 'Uzman montaj', 'تركيب احترافي', 'Fachowy montaż', 'Fachgerechte Installation'],
  'trust.installSub': ['Veilig, netjes en volgens de norm.', 'Safe, tidy and to standard.', 'Güvenli, temiz ve standartlara uygun.', 'آمن ومرتّب ووفق المعايير.', 'Bezpieczny, schludny i zgodny z normami.', 'Sicher, sauber und nach Norm.'],
  'trust.247Sub': ['Hulp wanneer u het nodig hebt.', 'Help when you need it.', 'İhtiyacınız olduğunda yanınızda.', 'مساعدة وقتما تحتاجونها.', 'Pomoc, gdy jej potrzebujesz.', 'Hilfe, wann immer Sie sie brauchen.'],

  // Buttons
  'cta.quote': ['Offerte aanvragen', 'Request a quote', 'Teklif al', 'اطلب عرض سعر', 'Poproś o wycenę', 'Angebot anfordern'],
  'cta.whatsapp': ['Direct WhatsAppen', 'WhatsApp us', "WhatsApp'tan yazın", 'راسلنا على واتساب', 'Napisz na WhatsApp', 'Per WhatsApp schreiben'],
  'cta.projects': ['Projecten bekijken', 'View projects', 'Projeleri gör', 'عرض المشاريع', 'Zobacz projekty', 'Projekte ansehen'],
  'cta.viewProject': ['Bekijk project', 'View project', 'Projeyi gör', 'عرض المشروع', 'Zobacz projekt', 'Projekt ansehen'],
  'cta.allProjects': ['Alle projecten bekijken', 'View all projects', 'Tüm projeleri gör', 'عرض جميع المشاريع', 'Zobacz wszystkie projekty', 'Alle Projekte ansehen'],
  'cta.allServices': ['Alle zeven diensten bekijken', 'See all seven services', 'Yedi hizmetin tamamını gör', 'عرض الخدمات السبع كاملةً', 'Zobacz wszystkie siedem usług', 'Alle sieben Leistungen ansehen'],
  'cta.moreAbout': ['Meer over ons', 'More about us', 'Hakkımızda daha fazla', 'المزيد عنا', 'Więcej o nas', 'Mehr über uns'],
  'cta.sendMail': ['Stuur een mail', 'Send an e-mail', 'Mail gönder', 'أرسل بريداً إلكترونياً', 'Wyślij e-mail', 'E-Mail senden'],
  'cta.sendMessage': ['Stuur een bericht', 'Send a message', 'Mesaj gönder', 'أرسل رسالة', 'Wyślij wiadomość', 'Nachricht senden'],

  // Hero
  'hero.eyebrow': ['Vakwerk in Nederland', 'Craftsmanship in the Netherlands', "Hollanda'da ustalık", 'حِرفية في هولندا', 'Rzemiosło w Holandii', 'Handwerk in den Niederlanden'],
  'hero.title': ['Uw elektra, <em>zonder gedoe.</em>', 'Your electrics, <em>without hassle.</em>', 'Elektriğiniz, <em>sorunsuz.</em>', 'كهرباؤكم، <em>دون عناء.</em>', 'Twoja elektryka, <em>bez kłopotów.</em>', 'Ihre Elektrik, <em>ohne Stress.</em>'],
  'hero.lede': [
    'Storingen, groepenkasten, verlichting, bedrading en veilige installaties — snel, veilig en netjes afgewerkt.',
    'Faults, fuse boxes, lighting, wiring and safe installations — fast, safe and neatly finished.',
    'Arızalar, sigorta kutuları, aydınlatma, kablolama ve güvenli tesisat — hızlı, güvenli ve özenle tamamlanır.',
    'أعطال، علب صمامات، إضاءة، تمديدات وتركيبات آمنة — بسرعة وأمان وإتقان.',
    'Awarie, skrzynki bezpieczników, oświetlenie, instalacja i bezpieczne systemy — szybko, bezpiecznie i starannie wykończone.',
    'Störungen, Sicherungskästen, Beleuchtung, Verkabelung und sichere Installationen — schnell, sicher und sauber ausgeführt.'
  ],
  'hero.photoAlt': ['Elektricien van AlleKlussers aan het werk', 'AlleKlussers electrician at work', 'AlleKlussers elektrikçisi çalışırken', 'كهربائي AlleKlussers أثناء العمل', 'Elektryk AlleKlussers przy pracy', 'Elektriker von AlleKlussers bei der Arbeit'],

  // Stats
  'stat.reach': ['Bereikbaar', 'Reachable', 'Ulaşılabilir', 'متاحون', 'Dostępni', 'Erreichbar'],
  'stat.reachSub': ['Mail of WhatsApp', 'Mail or WhatsApp', 'Mail veya WhatsApp', 'بريد أو واتساب', 'Mail lub WhatsApp', 'Mail oder WhatsApp'],
  'stat.projects': ['Projecten', 'Projects', 'Projeler', 'المشاريع', 'Projekty', 'Projekte'],
  'stat.projectsSub': ['Succesvol opgeleverd', 'Successfully delivered', 'Başarıyla teslim edildi', 'تم التسليم بنجاح', 'Pomyślnie dostarczone', 'Erfolgreich geliefert'],
  'stat.rating': ['Beoordeling', 'Rating', 'Değerlendirme', 'التقييم', 'Ocena', 'Bewertung'],
  'stat.ratingSub': ['Op basis van reviews', 'Based on reviews', 'Yorumlara göre', 'استناداً إلى المراجعات', 'Na podstawie opinii', 'Basierend auf Bewertungen'],
  'stat.insured': ['Verzekerd', 'Insured', 'Sigortalı', 'مؤمَّن', 'Ubezpieczeni', 'Versichert'],
  'stat.insuredSub': ['Vakmensen met certificaat', 'Certified craftsmen', 'Sertifikalı ustalar', 'حرفيون معتمدون', 'Certyfikowani fachowcy', 'Zertifizierte Handwerker'],

  // Services
  'svc.eyebrow': ['Onze diensten', 'Our services', 'Hizmetlerimiz', 'خدماتنا', 'Nasze usługi', 'Unsere Leistungen'],
  'svc.title': ['Onze elektrische <em>diensten.</em>', 'Our electrical <em>services.</em>', 'Elektrik <em>hizmetlerimiz.</em>', 'خدماتنا <em>الكهربائية.</em>', 'Nasze usługi <em>elektryczne.</em>', 'Unsere <em>Elektro-Leistungen.</em>'],
  'svc.lede': [
    'Voor particulieren en bedrijven. Van een storing tot een complete installatie.',
    'For homes and businesses. From a fault to a complete installation.',
    'Ev ve iş yerleri için. Bir arızadan komple tesisata kadar.',
    'للمنازل والشركات. من عطل بسيط إلى تركيب كامل.',
    'Dla domów i firm. Od awarii po kompletną instalację.',
    'Für Privat- und Geschäftskunden. Von der Störung bis zur kompletten Installation.'
  ],
  'svc.1': ['Storingen en spoed', 'Faults and urgent help', 'Arıza ve acil destek', 'الأعطال والطوارئ', 'Awarie i pilna pomoc', 'Störungen und Notdienst'],
  'svc.1.desc': [
    'Snelle hulp bij stroomuitval, kortsluiting en urgente elektrische problemen.',
    'Fast help with power outages, short circuits and urgent electrical issues.',
    'Elektrik kesintisi, kısa devre ve acil elektrik sorunlarında hızlı destek.',
    'مساعدة سريعة عند انقطاع الكهرباء، القصر الكهربائي والمشاكل العاجلة.',
    'Szybka pomoc przy awarii prądu, zwarciu i pilnych problemach elektrycznych.',
    'Schnelle Hilfe bei Stromausfall, Kurzschluss und dringenden Elektroproblemen.'
  ],
  'svc.2': ['Groepenkasten', 'Fuse boxes', 'Sigorta panoları', 'لوحات التوزيع', 'Rozdzielnice', 'Sicherungskästen'],
  'svc.2.desc': [
    'Vervangen, uitbreiden en veilig aanpassen van groepenkasten en zekeringen.',
    'Replacement, expansion and safe adjustment of fuse boxes and circuits.',
    'Sigorta panosu yenileme, genişletme ve güvenli devre düzenlemeleri.',
    'استبدال وتوسيع وضبط لوحات التوزيع والقواطع بأمان.',
    'Wymiana, rozbudowa i bezpieczne dostosowanie rozdzielnic.',
    'Austausch, Erweiterung und sichere Anpassung von Sicherungskästen.'
  ],
  'svc.3': ['Verlichting', 'Lighting', 'Aydınlatma', 'الإضاءة', 'Oświetlenie', 'Beleuchtung'],
  'svc.3.desc': [
    'Binnen- en buitenverlichting, spots, dimmers en nette montage.',
    'Indoor and outdoor lighting, spots, dimmers and clean installation.',
    'İç ve dış aydınlatma, spot, dimmer ve temiz montaj.',
    'إضاءة داخلية وخارجية، سبوتات، مخفتات وتركيب نظيف.',
    'Oświetlenie wewnętrzne i zewnętrzne, spoty, ściemniacze i czysty montaż.',
    'Innen- und Außenbeleuchtung, Spots, Dimmer und saubere Montage.'
  ],
  'svc.4': ['Stopcontacten en schakelaars', 'Sockets and switches', 'Prizler ve anahtarlar', 'المقابس والمفاتيح', 'Gniazdka i przełączniki', 'Steckdosen und Schalter'],
  'svc.4.desc': [
    'Extra stopcontacten, schakelaars en aansluitpunten veilig geplaatst.',
    'Extra sockets, switches and connection points installed safely.',
    'Ek priz, anahtar ve bağlantı noktaları güvenli şekilde kurulur.',
    'تركيب مقابس ومفاتيح ونقاط توصيل إضافية بأمان.',
    'Dodatkowe gniazdka, przełączniki i punkty podłączeń montowane bezpiecznie.',
    'Zusätzliche Steckdosen, Schalter und Anschlüsse sicher installiert.'
  ],
  'svc.5': ['Bedrading en aansluitingen', 'Wiring and connections', 'Kablolama ve bağlantılar', 'التمديدات والتوصيلات', 'Okablowanie i podłączenia', 'Verkabelung und Anschlüsse'],
  'svc.5.desc': [
    'Nieuwe leidingen en aansluitingen voor keuken, wasmachine en apparatuur.',
    'New wiring and connections for kitchen, washing machine and appliances.',
    'Mutfak, çamaşır makinesi ve cihazlar için yeni kablolama ve bağlantılar.',
    'تمديدات وتوصيلات جديدة للمطبخ والغسالة والأجهزة.',
    'Nowe okablowanie i podłączenia do kuchni, pralki i urządzeń.',
    'Neue Leitungen und Anschlüsse für Küche, Waschmaschine und Geräte.'
  ],
  'svc.6': ['Keuring en veiligheid', 'Inspection and safety', 'Kontrol ve güvenlik', 'الفحص والسلامة', 'Kontrola i bezpieczeństwo', 'Prüfung und Sicherheit'],
  'svc.6.desc': [
    'Controle van uw elektrische installatie, veilig en volgens de norm.',
    'A check of your electrical installation, safe and to standard.',
    'Elektrik tesisatınızın güvenli ve standartlara uygun kontrolü.',
    'فحص تركيباتكم الكهربائية بأمان ووفق المعايير.',
    'Kontrola instalacji elektrycznej, bezpiecznie i zgodnie z normą.',
    'Prüfung Ihrer Elektroinstallation, sicher und nach Norm.'
  ],
  'svc.7': ['Laadpalen en slimme elektra', 'EV chargers and smart electrics', 'Şarj istasyonu ve akıllı elektrik', 'الشحن والكهرباء الذكية', 'Ładowarki i smart elektryka', 'Ladestationen und Smart-Elektro'],
  'svc.7.desc': [
    'Een laadpaal bij uw woning en slimme schakelingen voor licht en apparaten.',
    'An EV charger at your home and smart switching for lights and appliances.',
    'Evinize şarj istasyonu ve ışıklar ile cihazlar için akıllı kontrol.',
    'شاحن سيارات كهربائية في منزلكم وتحكّم ذكي بالإضاءة والأجهزة.',
    'Ładowarka przy domu i inteligentne sterowanie oświetleniem i urządzeniami.',
    'Eine Ladestation an Ihrem Zuhause und smarte Schaltungen für Licht und Geräte.'
  ],
  'svc.other.title': ['Staat uw klus er niet bij?', 'Not seeing your job?', 'İşiniz listede yok mu?', 'لا تجدون عملكم في القائمة؟', 'Nie widzisz swojego zlecenia?', 'Ihr Auftrag ist nicht dabei?'],
  'svc.other.desc': [
    'Alles wat met elektra te maken heeft: vertel ons wat er moet gebeuren en wij denken mee.',
    'Anything to do with electrics: tell us what needs doing and we will think along.',
    'Elektrikle ilgili her şey: ne yapılması gerektiğini anlatın, birlikte çözüm bulalım.',
    'كل ما يتعلق بالكهرباء: أخبرونا بما يلزم وسنساعدكم في إيجاد الحل.',
    'Wszystko, co dotyczy elektryki: powiedz, co trzeba zrobić, a my doradzimy.',
    'Alles rund um Elektrik: Sagen Sie uns, was zu tun ist, und wir denken mit.'
  ],

  // Projects
  'proj.eyebrow': ['Projecten', 'Projects', 'Projeler', 'المشاريع', 'Projekty', 'Projekte'],
  'proj.title': ['Projecten die <em>netjes zijn afgewerkt.</em>', 'Projects, <em>neatly finished.</em>', '<em>Özenle tamamlanan</em> projeler.', 'مشاريع <em>منجزة بإتقان.</em>', 'Projekty <em>starannie wykończone.</em>', 'Projekte, <em>sauber abgeschlossen.</em>'],
  'proj.lede': [
    'Bij AlleKlussers leveren we strak afgewerkt elektrawerk, van een extra stopcontact tot een compleet verlichtingsplan. We denken mee, werken netjes en zorgen voor veilige, duurzame resultaten met oog voor detail.',
    'At AlleKlussers we deliver crisply finished electrical work, from an extra socket to a complete lighting plan. We think along, work tidily and ensure safe, durable results with attention to detail.',
    'AlleKlussers olarak tek bir prizden komple aydınlatma planına kadar özenli elektrik işleri sunuyoruz. Birlikte düşünür, temiz çalışır ve detaylara önem vererek güvenli, kalıcı sonuçlar üretiriz.',
    'في AlleKlussers نقدّم أعمالاً كهربائية منجزة بإتقان، من مقبس إضافي إلى خطة إضاءة كاملة. نُشارك بالأفكار ونعمل بترتيب ونضمن نتائج آمنة ودائمة بعناية للتفاصيل.',
    'W AlleKlussers starannie wykonujemy prace elektryczne, od dodatkowego gniazdka po kompletny plan oświetlenia. Doradzamy, pracujemy schludnie i dbamy o bezpieczne, trwałe efekty z dbałością o detal.',
    'Bei AlleKlussers liefern wir sauber ausgeführte Elektroarbeiten, von der zusätzlichen Steckdose bis zum kompletten Lichtplan. Wir denken mit, arbeiten ordentlich und sorgen für sichere, langlebige Ergebnisse mit Blick fürs Detail.'
  ],
  'proj.photos': ["foto's", 'photos', 'fotoğraf', 'صور', 'zdjęć', 'Fotos'],
  'proj.bath.title': ['Elektra en LED-verlichting in een badkamer', 'Electrics and LED lighting in a bathroom', 'Banyoda elektrik tesisatı ve LED aydınlatma', 'كهرباء وإضاءة LED في حمّام', 'Elektryka i oświetlenie LED w łazience', 'Elektrik und LED-Beleuchtung im Badezimmer'],
  'proj.bath.tag': ['Badkamer', 'Bathroom', 'Banyo', 'حمّام', 'Łazienka', 'Badezimmer'],
  'proj.bath.desc': [
    'Nieuwe elektra, LED-spiegelverlichting en een verlichtingsplan voor de hele badkamer, strak afgewerkt.',
    'New electrics, LED mirror lighting and a lighting plan for the whole bathroom, neatly finished.',
    'Yeni elektrik tesisatı, LED ayna aydınlatması ve tüm banyo için aydınlatma planı, özenle tamamlandı.',
    'كهرباء جديدة، إضاءة مرآة LED وخطة إضاءة للحمّام بالكامل، بتشطيب أنيق.',
    'Nowa elektryka, oświetlenie LED lustra i plan oświetlenia całej łazienki, starannie wykończone.',
    'Neue Elektrik, LED-Spiegelbeleuchtung und ein Lichtplan für das ganze Bad, sauber ausgeführt.'
  ],
  'proj.bath.h1': ['LED spiegelverlichting', 'LED mirror lighting', 'LED ayna aydınlatması', 'إضاءة مرآة LED', 'Oświetlenie LED lustra', 'LED-Spiegelbeleuchtung'],
  'proj.bath.h2': ['Nieuwe aansluitpunten', 'New connection points', 'Yeni bağlantı noktaları', 'نقاط توصيل جديدة', 'Nowe punkty podłączeń', 'Neue Anschlusspunkte'],
  'proj.bath.h3': ['Strakke afwerking', 'Crisp finishing', 'Özenli işçilik', 'تشطيب أنيق', 'Staranne wykończenie', 'Saubere Ausführung'],
  'proj.dine.title': ['Eettafelverlichting en aansluitpunten', 'Dining-table lighting and connections', 'Yemek masası aydınlatması ve bağlantılar', 'إضاءة طاولة الطعام والتوصيلات', 'Oświetlenie nad stołem i przyłącza', 'Esstisch-Beleuchtung und Anschlüsse'],
  'proj.dine.desc': [
    'Hanglampen op maat geplaatst met nieuwe bedrading en dimbare schakeling.',
    'Custom pendant lights with new wiring and dimmable switching.',
    "Yeni kablolama ve dim'li anahtarla özel sarkıt aydınlatma.",
    'إنارة معلّقة مخصّصة مع تمديدات جديدة وتحكّم خافت.',
    'Lampy wiszące na wymiar z nową instalacją i ściemnianiem.',
    'Maßgefertigte Pendelleuchten mit neuer Verkabelung und Dimmer.'
  ],
  'proj.dine.h1': ['Hanglampen op maat', 'Custom pendants', 'Özel sarkıt', 'إنارة معلّقة مخصّصة', 'Lampy na wymiar', 'Pendel nach Maß'],
  'proj.dine.h2': ['Nieuwe bedrading', 'New wiring', 'Yeni kablolama', 'تمديدات جديدة', 'Nowa instalacja', 'Neue Verkabelung'],
  'proj.dine.h3': ['Dimbare schakeling', 'Dimmable switching', "Dim'li anahtar", 'تحكّم خافت', 'Ściemnianie', 'Dimmer-Schaltung'],
  'proj.gym.title': ['Verlichting voor fitnessruimte', 'Lighting for a home gym', 'Fitness odası aydınlatması', 'إضاءة غرفة لياقة', 'Oświetlenie siłowni domowej', 'Beleuchtung für Fitnessraum'],
  'proj.gym.desc': [
    'Sfeervolle LED-verlichting en extra groepen voor apparatuur.',
    'Atmospheric LED lighting and extra circuits for equipment.',
    'Atmosferik LED aydınlatma ve cihazlar için ek hatlar.',
    'إضاءة LED مريحة ودوائر إضافية للأجهزة.',
    'Klimatyczne oświetlenie LED i dodatkowe obwody dla sprzętu.',
    'Stimmungsvolle LED-Beleuchtung und Extra-Stromkreise für Geräte.'
  ],
  'proj.gym.h1': ['Sfeer-LED', 'Ambient LED', 'Atmosfer LED', 'إضاءة LED مريحة', 'Klimatyczne LED', 'Ambiente-LED'],
  'proj.gym.h2': ['Extra groepen', 'Extra circuits', 'Ek hatlar', 'دوائر إضافية', 'Dodatkowe obwody', 'Extra-Stromkreise'],
  'proj.gym.h3': ['Veilige montage', 'Safe installation', 'Güvenli montaj', 'تركيب آمن', 'Bezpieczny montaż', 'Sichere Montage'],

  // Process
  'step.eyebrow': ['Werkwijze', 'Process', 'Çalışma şeklimiz', 'منهجية العمل', 'Proces', 'Vorgehen'],
  'step.title': ['In vier stappen <em>van vraag naar oplevering.</em>', 'Four steps <em>from question to handover.</em>', 'Sorudan teslime <em>dört adımda.</em>', 'أربع خطوات <em>من الطلب إلى التسليم.</em>', 'Cztery kroki <em>od pytania do odbioru.</em>', 'In vier Schritten <em>von der Anfrage zur Übergabe.</em>'],
  'step.1': ['Kennismaking', 'Intake', 'Tanışma', 'تعارف', 'Zapoznanie', 'Kennenlernen'],
  'step.1.desc': [
    'U vertelt wat er moet gebeuren, telefonisch of vrijblijvend bij u thuis.',
    'You tell us what needs doing, by phone or in a no-obligation visit at your home.',
    'Ne yapılması gerektiğini telefonda ya da evinizde ücretsiz bir görüşmede anlatırsınız.',
    'تخبروننا بما يلزم، عبر الهاتف أو في زيارة مجانية دون التزام في منزلكم.',
    'Mówisz, co trzeba zrobić — telefonicznie lub podczas niezobowiązującej wizyty u Ciebie w domu.',
    'Sie erzählen uns, was zu tun ist, telefonisch oder unverbindlich bei Ihnen zu Hause.'
  ],
  'step.2': ['Voorstel', 'Proposal', 'Teklif', 'عرض', 'Propozycja', 'Angebot'],
  'step.2.desc': [
    'Binnen 24 uur een heldere offerte op maat. Geen verrassingen achteraf.',
    'A clear, tailored quote within 24 hours. No surprises afterwards.',
    '24 saat içinde net ve size özel bir teklif. Sonradan sürpriz yok.',
    'عرض سعر واضح ومخصص خلال 24 ساعة. لا مفاجآت لاحقاً.',
    'Jasna wycena na miarę w ciągu 24 godzin. Bez niespodzianek na końcu.',
    'Innerhalb von 24 Stunden ein klares, maßgeschneidertes Angebot. Keine Überraschungen danach.'
  ],
  'step.3': ['Uitvoering', 'Execution', 'Uygulama', 'تنفيذ', 'Realizacja', 'Ausführung'],
  'step.3.desc': [
    'Gecertificeerde vakmensen werken veilig, netjes en volgens de norm.',
    'Certified craftsmen work safely, tidily and to standard.',
    'Sertifikalı ustalar güvenli, temiz ve standartlara uygun çalışır.',
    'حرفيون معتمدون يعملون بأمان وترتيب ووفق المعايير.',
    'Certyfikowani fachowcy pracują bezpiecznie, schludnie i zgodnie z normami.',
    'Zertifizierte Handwerker arbeiten sicher, sauber und nach Norm.'
  ],
  'step.4': ['Oplevering', 'Delivery', 'Teslim', 'تسليم', 'Odbiór', 'Übergabe'],
  'step.4.desc': [
    'We lopen alles samen na en laten de ruimte netjes achter. Zoals afgesproken.',
    'We go through everything together and leave the space tidy. As agreed.',
    'Her şeyi birlikte kontrol eder, alanı temiz bırakırız. Anlaştığımız gibi.',
    'نراجع كل شيء معاً ونترك المكان مرتباً. كما هو متفق عليه.',
    'Wspólnie wszystko sprawdzamy i zostawiamy porządek. Zgodnie z umową.',
    'Wir gehen alles gemeinsam durch und hinterlassen alles ordentlich. Wie vereinbart.'
  ],

  // About
  'about.eyebrow': ['Over ons', 'About us', 'Hakkımızda', 'من نحن', 'O nas', 'Über uns'],
  'about.title': ['Wij regelen uw elektra. <em>U blijft zorgeloos.</em>', 'We handle your electrics. <em>You stay worry-free.</em>', 'Elektriğinizi biz çözeriz. <em>Siz rahat edin.</em>', 'ننجز أعمال الكهرباء. <em>وأنتم مطمئنون.</em>', 'Zajmiemy się elektryką. <em>Ty masz spokój.</em>', 'Wir regeln Ihre Elektroarbeiten. <em>Sie bleiben sorgenfrei.</em>'],
  'about.lede': [
    'Wij zijn uw betrouwbare elektrotechnisch specialist voor particulieren en bedrijven. Met veilige installaties, snelle communicatie en netjes werk zorgen wij voor zekerheid in elke situatie.',
    'We provide reliable electrical solutions for homes and businesses. With safe installations, clear communication and tidy workmanship, we make every job feel secure.',
    'Ev ve iş yerleri için güvenilir elektrik çözümleri sunuyoruz. Güvenli tesisat, hızlı iletişim ve temiz işçilikle her durumda yanınızdayız.',
    'نوفّر حلولاً كهربائية موثوقة للمنازل والشركات. بتركيبات آمنة وتواصل واضح وعمل مرتّب، نضمن لكم الثقة في كل موقف.',
    'Oferujemy niezawodne rozwiązania elektryczne dla domów i firm. Dzięki bezpiecznym instalacjom, przejrzystej komunikacji i schludnemu wykonaniu każda praca daje poczucie pewności.',
    'Wir sind Ihr zuverlässiger Elektrotechnik-Spezialist für Privat- und Geschäftskunden. Mit sicheren Installationen, klarer Kommunikation und sauberer Ausführung sorgen wir in jeder Situation für Verlässlichkeit.'
  ],
  'about.approach': ['Aanpak', 'Approach', 'Yaklaşım', 'نهجنا', 'Podejście', 'Ansatz'],
  'about.approachSub': ['Eén aanspreekpunt voor uw elektra.', 'One point of contact for your electrics.', 'Elektrik işleriniz için tek muhatap.', 'نقطة اتصال واحدة لكل أعمال الكهرباء لديكم.', 'Jedna osoba kontaktowa do Twojej elektryki.', 'Ein Ansprechpartner für Ihre Elektrik.'],
  'about.projectsSub': ['Afgeronde elektra-opdrachten.', 'Completed electrical assignments.', 'Tamamlanan elektrik işleri.', 'مهام كهربائية مكتملة.', 'Ukończone zlecenia elektryczne.', 'Abgeschlossene Elektroaufträge.'],
  'about.langs': ['Talen', 'Languages', 'Diller', 'اللغات', 'Języki', 'Sprachen'],
  'about.langsSub': ['Duidelijke communicatie voor elke klant.', 'Clear communication for every client.', 'Her müşteri için net iletişim.', 'تواصل واضح مع كل عميل.', 'Przejrzysta komunikacja z każdym klientem.', 'Klare Kommunikation für jeden Kunden.'],
  'about.photoAlt': ['Elektricien van AlleKlussers bij een groepenkast', 'AlleKlussers electrician at a fuse box', 'Sigorta panosunda çalışan AlleKlussers elektrikçisi', 'كهربائي AlleKlussers عند لوحة التوزيع', 'Elektryk AlleKlussers przy rozdzielnicy', 'Elektriker von AlleKlussers am Sicherungskasten'],

  // Reviews + partners
  'rev.eyebrow': ['Klanten', 'Clients', 'Müşteriler', 'العملاء', 'Klienci', 'Kunden'],
  'rev.title': ['Wat zij <em>zeggen.</em>', 'What they <em>say.</em>', 'Onlar ne <em>diyor.</em>', 'ما <em>يقولونه.</em>', 'Co <em>mówią.</em>', 'Was sie <em>sagen.</em>'],
  'rev.1': [
    '“Snel geholpen bij een storing. Rustige communicatie, nette afwerking en geen verrassingen achteraf.”',
    '“Quick help with an electrical fault. Calm communication, tidy work and no surprises afterwards.”',
    '“Elektrik arızasında hızlı yardımcı oldular. Sakin iletişim, temiz işçilik ve sonradan sürpriz yok.”',
    '”ساعدونا بسرعة عند حدوث عطل كهربائي. تواصل واضح، عمل مرتب ولا مفاجآت لاحقاً.“',
    '„Szybka pomoc przy awarii elektrycznej. Spokojna komunikacja, schludne wykonanie i bez niespodzianek.”',
    '„Schnelle Hilfe bei einer Störung. Ruhige Kommunikation, saubere Arbeit und keine Überraschungen danach.“'
  ],
  'rev.1.tag': ['Storingen', 'Electrical fault', 'Arıza', 'أعطال كهربائية', 'Awarie', 'Störung'],
  'rev.2': [
    '“Groepenkast netjes vervangen en alles duidelijk uitgelegd. Binnen één dag geregeld.”',
    '“The consumer unit was replaced neatly and everything was explained clearly. Arranged within one day.”',
    '“Sigorta panosu temiz şekilde değiştirildi ve her şey net anlatıldı. Bir gün içinde tamamlandı.”',
    '”تم استبدال لوحة الكهرباء بشكل مرتب وشرحوا كل شيء بوضوح. أُنجز العمل خلال يوم واحد.“',
    '„Rozdzielnica została schludnie wymieniona, a wszystko jasno wyjaśniono. Załatwione w jeden dzień.”',
    '„Der Verteilerkasten wurde sauber ersetzt und alles klar erklärt. Innerhalb eines Tages erledigt.“'
  ],
  'rev.2.tag': ['Groepenkast', 'Consumer unit', 'Sigorta panosu', 'لوحة الكهرباء', 'Rozdzielnica', 'Verteilerkasten'],
  'rev.3': [
    '“Nieuwe stopcontacten en verlichting laten plaatsen. Alles strak afgewerkt en schoon achtergelaten.”',
    '“We had new sockets and lighting installed. Everything was finished sharply and left clean.”',
    '“Yeni prizler ve aydınlatma yaptırdık. Her şey özenli tamamlandı ve temiz bırakıldı.”',
    '”ركّبوا مقابس جديدة وإضاءة. كان التشطيب أنيقاً وتركوا المكان نظيفاً.“',
    '„Zamontowano nowe gniazdka i oświetlenie. Wszystko starannie wykończone i zostawione czysto.”',
    '„Neue Steckdosen und Beleuchtung montieren lassen. Alles sauber ausgeführt und ordentlich hinterlassen.“'
  ],
  'rev.3.tag': ['Verlichting', 'Lighting', 'Aydınlatma', 'إضاءة', 'Oświetlenie', 'Beleuchtung'],
  'partners': ['Onze partners', 'Trusted partners', 'Birlikte çalıştıklarımız', 'شركاؤنا', 'Nasi partnerzy', 'Unsere Partner'],

  // Contact + form
  'contact.title': ['Vraag een <em>offerte</em> aan.', 'Request a <em>quote.</em>', '<em>Teklif</em> isteyin.', 'اطلبوا <em>عرض سعر.</em>', 'Poproś o <em>wycenę.</em>', 'Fordern Sie ein <em>Angebot</em> an.'],
  'contact.pageTitle': ['Stuur een <em>bericht.</em>', 'Send a <em>message.</em>', 'Bir <em>mesaj</em> gönderin.', 'أرسلوا <em>رسالةً.</em>', 'Wyślij <em>wiadomość.</em>', 'Senden Sie eine <em>Nachricht.</em>'],
  'contact.lede': [
    'Vertel kort wat er moet gebeuren. U krijgt binnen 24 uur reactie, inclusief offerte op maat.',
    "Tell us briefly what needs doing. You'll get a reply within 24 hours, including a tailored quote.",
    'Ne yapılması gerektiğini kısaca anlatın. 24 saat içinde size özel teklifle birlikte yanıt alırsınız.',
    'أخبرونا باختصار بما يلزم. ستتلقون رداً خلال 24 ساعة مع عرض سعر مخصص.',
    'Opisz krótko, co trzeba zrobić. Odpowiemy w ciągu 24 godzin, wraz z wyceną na miarę.',
    'Beschreiben Sie kurz, was zu tun ist. Sie erhalten innerhalb von 24 Stunden eine Antwort inkl. maßgeschneidertem Angebot.'
  ],
  'contact.direct': ['Of neem direct contact op', 'Or contact us directly', 'Ya da doğrudan ulaşın', 'أو تواصلوا معنا مباشرة', 'Lub skontaktuj się bezpośrednio', 'Oder direkt Kontakt aufnehmen'],
  'contact.strip': ['Hulp nodig met uw elektra?', 'Need help with your electrics?', 'Elektrik işleriniz için yardım mı lazım?', 'هل تحتاجون مساعدة في الكهرباء؟', 'Potrzebujesz pomocy z elektryką?', 'Brauchen Sie Hilfe bei Ihrer Elektrik?'],
  'form.name': ['Naam', 'Name', 'Adınız', 'الاسم', 'Imię i nazwisko', 'Name'],
  'form.postcode': ['Postcode', 'Postcode', 'Posta kodu', 'الرمز البريدي', 'Kod pocztowy', 'Postleitzahl'],
  'form.city': ['Plaats', 'City', 'Şehir', 'المدينة', 'Miejscowość', 'Ort'],
  'form.type': ['Soort werk', 'Type of work', 'İş türü', 'نوع العمل', 'Rodzaj pracy', 'Art der Arbeit'],
  'form.other': ['Anders', 'Other', 'Diğer', 'أخرى', 'Inne', 'Sonstiges'],
  'form.desc': ['Omschrijving', 'Description', 'Açıklama', 'الوصف', 'Opis', 'Beschreibung'],
  'form.descPh': ['Beschrijf kort wat er moet gebeuren', 'Briefly describe what needs doing', 'Ne yapılması gerektiğini kısaca yazın', 'صفوا باختصار ما يلزم', 'Opisz krótko, co trzeba zrobić', 'Beschreiben Sie kurz, was zu tun ist'],
  'form.sendWa': ['Verstuur via WhatsApp', 'Send via WhatsApp', 'WhatsApp ile gönder', 'إرسال عبر واتساب', 'Wyślij przez WhatsApp', 'Per WhatsApp senden'],
  'form.sendMail': ['Verstuur via e-mail', 'Send via e-mail', 'E-posta ile gönder', 'إرسال عبر البريد', 'Wyślij e-mailem', 'Per E-Mail senden'],
  'form.note': [
    'Uw bericht opent in WhatsApp of uw e-mailprogramma. Wij antwoorden binnen 24 uur.',
    'Your message opens in WhatsApp or your e-mail app. We reply within 24 hours.',
    "Mesajınız WhatsApp'ta veya e-posta uygulamanızda açılır. 24 saat içinde yanıt veririz.",
    'تُفتح رسالتكم في واتساب أو تطبيق البريد. نرد خلال 24 ساعة.',
    'Wiadomość otworzy się w WhatsApp lub programie pocztowym. Odpowiadamy w ciągu 24 godzin.',
    'Ihre Nachricht öffnet sich in WhatsApp oder Ihrem E-Mail-Programm. Wir antworten innerhalb von 24 Stunden.'
  ],
  'form.error': ['Vul uw naam en een korte omschrijving in.', 'Please fill in your name and a short description.', 'Lütfen adınızı ve kısa bir açıklama yazın.', 'يرجى إدخال الاسم ووصف قصير.', 'Podaj imię i krótki opis.', 'Bitte Namen und eine kurze Beschreibung angeben.'],
  'msg.intro': ['Hallo AlleKlussers, ik wil graag een offerte aanvragen.', 'Hello AlleKlussers, I would like to request a quote.', 'Merhaba AlleKlussers, teklif almak istiyorum.', 'مرحباً AlleKlussers، أود طلب عرض سعر.', 'Dzień dobry AlleKlussers, chciałbym poprosić o wycenę.', 'Hallo AlleKlussers, ich möchte gerne ein Angebot anfordern.'],
  'msg.subject': ['Offerteaanvraag', 'Quote request', 'Teklif talebi', 'طلب عرض سعر', 'Prośba o wycenę', 'Angebotsanfrage'],

  // De Stroomploeg (characters)
  'cast.eyebrow': ['De Stroomploeg', 'The Power Crew', 'Akım Ekibi', 'فريق الكهرباء', 'Ekipa Prądu', 'Die Stromtruppe'],
  'cast.title': ['Maak kennis met <em>de Stroomploeg.</em>', 'Meet <em>the Power Crew.</em>', '<em>Akım Ekibi</em> ile tanışın.', 'تعرّفوا على <em>فريق الكهرباء.</em>', 'Poznaj <em>Ekipę Prądu.</em>', 'Lernen Sie <em>die Stromtruppe</em> kennen.'],
  'cast.lede': [
    'Onze kleine helpers wijzen u de weg op de site. Het echte werk doen onze gecertificeerde vakmensen.',
    'Our little helpers show you around the site. The real work is done by our certified craftsmen.',
    'Küçük yardımcılarımız size sitede yol gösterir. Asıl işi sertifikalı ustalarımız yapar.',
    'مساعدونا الصغار يرشدونكم في الموقع. أما العمل الحقيقي فيقوم به حرفيونا المعتمدون.',
    'Nasi mali pomocnicy oprowadzą Cię po stronie. Prawdziwą pracę wykonują nasi certyfikowani fachowcy.',
    'Unsere kleinen Helfer zeigen Ihnen die Seite. Die echte Arbeit machen unsere zertifizierten Handwerker.'
  ],
  'ch.stekkie': ['De regelaar', 'The fixer', 'İşleri yoluna koyan', 'المنظِّم', 'Złota rączka', 'Der Macher'],
  'ch.vonk': ['Spoedhulp, 24/7', 'Urgent help, 24/7', 'Acil destek, 7/24', 'مساعدة عاجلة، 24/7', 'Pilna pomoc, 24/7', 'Notdienst, 24/7'],
  'ch.kastje': ['Groepenkast-kenner', 'Fuse box expert', 'Sigorta panosu uzmanı', 'خبير لوحات التوزيع', 'Znawca rozdzielnic', 'Sicherungskasten-Profi'],
  'ch.lampje': ['Lichtexpert', 'Lighting expert', 'Aydınlatma uzmanı', 'خبير الإضاءة', 'Ekspert od światła', 'Lichtexperte'],
  'ch.dosie': ['Stopcontact-maatje', 'Socket buddy', 'Priz dostu', 'صديق المقابس', 'Kumpel od gniazdek', 'Steckdosen-Kumpel'],
  'ch.schildje': ['Veiligheidscheck', 'Safety check', 'Güvenlik kontrolü', 'فحص السلامة', 'Kontrola bezpieczeństwa', 'Sicherheitscheck'],
  'ch.laadie': ['Laadpaal-specialist', 'EV charger specialist', 'Şarj istasyonu uzmanı', 'خبير شواحن السيارات', 'Specjalista od ładowarek', 'Ladestation-Profi'],
  'say.hero': ['“Even appen? Wij regelen het.”', '“Just send a WhatsApp. We’ll handle it.”', '“Bir mesaj atın, gerisini biz hallederiz.”', '”أرسلوا رسالة، ونحن نتولى الباقي.“', '„Napisz do nas — resztą się zajmiemy.”', '„Kurz schreiben? Wir regeln das.“'],
  'say.services': ['“Stroom uit? Wij zijn 24/7 bereikbaar.”', '“Power out? We’re reachable 24/7.”', '“Elektrik mi kesildi? 7/24 ulaşılabiliriz.”', '”انقطعت الكهرباء؟ نحن متاحون 24/7.“', '„Brak prądu? Jesteśmy dostępni 24/7.”', '„Strom weg? Wir sind 24/7 erreichbar.“'],
  'say.projects': ['“Kijk gerust rond!”', '“Have a look around!”', '“Rahatça göz atın!”', '”تفضّلوا بالاطلاع!“', '„Rozejrzyj się!”', '„Schauen Sie sich um!“'],
  'say.about': ['“Veilig, netjes en volgens de norm.”', '“Safe, tidy and to standard.”', '“Güvenli, temiz ve standartlara uygun.”', '”آمن ومرتّب ووفق المعايير.“', '„Bezpiecznie, schludnie i zgodnie z normami.”', '„Sicher, sauber und nach Norm.“'],
  'say.steps': ['“Eerst kijken, dan pas klussen.”', '“First we look, then we work.”', '“Önce bakarız, sonra işe koyuluruz.”', '”ننظر أولاً، ثم نبدأ العمل.“', '„Najpierw patrzymy, potem działamy.”', '„Erst schauen, dann loslegen.“'],
  'say.contact': ['“Vertel het maar. Binnen 24 uur hoort u van ons.”', '“Tell us all about it. You’ll hear from us within 24 hours.”', '“Anlatın, 24 saat içinde size dönüyoruz.”', '”أخبرونا، وسنرد عليكم خلال 24 ساعة.“', '„Opowiedz nam — odezwiemy się w ciągu 24 godzin.”', '„Erzählen Sie es uns. Innerhalb von 24 Stunden hören Sie von uns.“'],

  'say.stekkie': ['“Eén aanspreekpunt voor al uw elektra.”', '“One point of contact for all your electrics.”', '“Tüm elektrik işleriniz için tek muhatap.”', '”نقطة اتصال واحدة لكل أعمال الكهرباء.“', '„Jedna osoba kontaktowa do całej elektryki.”', '„Ein Ansprechpartner für Ihre ganze Elektrik.“'],
  'say.kastje': ['“Slaan de stoppen door? Ik kijk even.”', '“Fuses keep tripping? Let me take a look.”', '“Sigortalar mı atıyor? Bir bakayım.”', '”القواطع تفصل باستمرار؟ دعوني أتحقق.“', '„Wywala korki? Zaraz sprawdzę.”', '„Fliegt die Sicherung raus? Ich schaue mal.“'],
  'say.lampje': ['“Spots, dimmers of een hanglamp? Ik zorg voor sfeer.”', '“Spots, dimmers or a pendant? I bring the mood.”', '“Spot, dimmer ya da sarkıt? Ortamı ben ayarlarım.”', '”سبوتات أو مخفتات أو إنارة معلّقة؟ أنا أصنع الأجواء.“', '„Spoty, ściemniacze czy lampa wisząca? Zadbam o klimat.”', '„Spots, Dimmer oder Pendelleuchte? Ich sorge für Stimmung.“'],
  'say.dosie': ['“Een stopcontact erbij? Komt goed.”', '“An extra socket? No problem.”', '“Bir priz daha mı? Hallederiz.”', '”مقبس إضافي؟ لا مشكلة.“', '„Dodatkowe gniazdko? Nie ma sprawy.”', '„Eine Steckdose mehr? Kein Problem.“'],
  'say.laadie': ['“Thuis laden? Ik regel de laadpaal.”', '“Charging at home? I’ll sort the charger.”', '“Evde şarj mı? Şarj istasyonunu ben hallederim.”', '”الشحن في المنزل؟ أتولى أمر الشاحن.“', '„Ładowanie w domu? Zajmę się ładowarką.”', '„Zu Hause laden? Ich kümmere mich um die Ladestation.“'],
  'cast.tap': ['Tik op een helper', 'Tap a helper', 'Bir yardımcıya dokunun', 'اضغطوا على أحد المساعدين', 'Kliknij pomocnika', 'Tippen Sie auf einen Helfer'],

  // Footer
  'foot.company': ['Bedrijf', 'Company', 'Şirket', 'الشركة', 'Firma', 'Unternehmen'],
  'foot.part': ['Onderdeel van Boss Tech VOF', 'Part of Boss Tech VOF', "Boss Tech VOF'a bağlıdır", 'جزء من Boss Tech VOF', 'Część Boss Tech VOF', 'Teil der Boss Tech VOF']
};
