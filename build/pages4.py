# -*- coding: utf-8 -*-
"""Clubs · Galerie · Actus · Glossaire · FAQ · Contact · Mentions · Plan · 404"""
from content import cta

P = {}

# =========================================================================== #
#  CLUBS & COMPÉTITIONS
# =========================================================================== #
P["clubs"] = {
    "head_bg": "photos/soiree-course-large.webp",
    "url": "clubs-et-competitions.html",
    "crumb": "Clubs & compétitions",
    "title": "Clubs et compétitions RC 1/76 en France — où rouler, comment organiser",
    "desc": "La communauté francophone du RC racing sur table : groupes actifs, calendrier des "
            "rencontres, et ce qu’il faut pour monter sa propre course à quatre pilotes en deux heures.",
    "image": "photos/soiree-course-table.jpg",
    "image_alt": "Soirée de course RC 1/76 autour d’une table",
    "priority": "0.75", "changefreq": "weekly",
    "about": ["Club RC", "Compétition RC 1/76", "Communauté modélisme"],
    "speakable": [".answer"],
    "body": """
<section class="page-head">
  <div class="wrap page-head-inner stack" style="--gap:20px">
    <p class="eyebrow">Communauté</p>
    <h1 class="h1" style="color:#fff">Clubs &amp; compétitions</h1>
    <p class="lead">Des groupes de pilotes existent un peu partout, sur les forums et sur Facebook. Dès que
    des compétitions s’organisent, elles sont relayées ici. N’hésite pas à me contacter pour faire grandir
    la communauté.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="answer" style="margin-bottom:40px" data-reveal><strong>Il n’existe pas encore de championnat
    structuré en 1/76.</strong> Les rencontres se montent de façon informelle, principalement via le groupe
    Facebook « Turbo Racing RC 1:76 France ». Monter la vôtre demande peu : une table, un tapis avec bordures,
    quatre pilotes et deux heures. Ce site est là pour rassembler les amateurs et pilotes de 1/76 : n’hésite pas à
    proposer un lieu ou une soirée pour vous challenger.</p>

    <div class="grid g3" data-stagger>
      <article class="card"><span class="card-num">Le groupe le plus actif</span>
        <h2 class="h3">Turbo Racing RC 1:76 France</h2>
        <p>Sur Facebook. Circuits maison, réglages, annonces de rencontres : c’est le point de rendez-vous
        francophone de la catégorie.</p></article>
      <article class="card"><span class="card-num">Monter un rendez-vous</span>
        <h2 class="h3">Ce qu’il faut, vraiment</h2>
        <p>Une table, un tapis avec bordures, quatre pilotes et deux heures. Prends le règlement type,
        annonce le châssis autorisé, et tu as une vraie course.</p>
        <p style="margin-top:8px"><a class="link-arrow" href="reglement-type-de-course.html">Voir le règlement type <span aria-hidden="true">→</span></a></p></article>
      <article class="card"><span class="card-num">Signaler un club</span>
        <h2 class="h3">Faire la carte du 1/76</h2>
        <p>Tu roules régulièrement quelque part ? Envoie-moi la ville et le contact : cette page a vocation
        à devenir la carte du 1/76 francophone.</p>
        <p style="margin-top:8px"><a class="link-arrow" href="contact.html">Me contacter <span aria-hidden="true">→</span></a></p></article>
    </div>
  </div>
</section>

<section class="section section--paper2">
  <div class="wrap">
    <p class="eyebrow" data-reveal>Mise à jour au fil des annonces</p>
    <h2 class="h2" style="margin:12px 0 26px" data-reveal>Calendrier</h2>
    <div class="callout" data-reveal>
      <h3 class="h3" style="margin-bottom:12px">Aucune date annoncée pour l’instant</h3>
      <p class="prose">La catégorie est jeune : les rencontres se montent de façon informelle. Si tu organises
      quelque chose, même à quatre autour d’une table, dis-le — c’est comme ça qu’un championnat commence.</p>
      <p style="margin-top:18px"><a class="btn btn--race" href="contact.html">Annoncer une rencontre <span class="arrow" aria-hidden="true">→</span></a></p>
    </div>
    <figure class="fig" style="margin-top:32px" data-reveal="scale">
      <img src="img/photos/soiree-course-large.webp" width="900" height="506" loading="lazy" decoding="async" alt="Quatre pilotes autour d’un circuit RC 1/76 monté sur une table dans un bar, radiocommandes en main">
      <figcaption>Une rencontre n’a besoin de rien de plus : une table, un tapis avec bordures, quatre pilotes et deux heures.</figcaption>
    </figure>
  </div>
</section>

""" + cta("Regarde ce que les autres construisent.", "galerie-des-circuits.html", "La galerie des circuits"),
}


# =========================================================================== #
#  GALERIE
# =========================================================================== #
P["galerie"] = {
    "head_bg": "photos/circuit-maison-80x120.webp",
    "url": "galerie-des-circuits.html",
    "crumb": "Galerie des circuits",
    "title": "Galerie des circuits RC 1/76 — les pistes des pilotes francophones",
    "desc": "Tapis du commerce, constructions maison et tracés improbables sur une table de cuisine : "
            "les circuits RC 1/76 des pilotes francophones, en photos.",
    "image": "photos/circuit-maison-80x120.jpg",
    "image_alt": "Circuit RC 1/76 fait maison, vue de dessus, bordures blanches",
    "priority": "0.7", "changefreq": "weekly",
    "page_type": "CollectionPage",
    "about": ["Circuit RC maison", "Galerie photo modélisme"],
    "jsonld": [{
        "@context": "https://schema.org",
        "@type": "ImageGallery",
        "name": "Galerie des circuits RC 1/76",
        "description": "Les pistes des pilotes francophones de RC table car racing.",
        "associatedMedia": [
            {"@type": "ImageObject", "contentUrl": "https://rctableracingcar.fr/img/photos/circuit-maison-80x120.jpg",
             "caption": "Circuit maison 80 × 120 cm, plaque rigide et bordures polyuréthane."},
            {"@type": "ImageObject", "contentUrl": "https://rctableracingcar.fr/img/photos/grille-depart-carre.jpg",
             "caption": "Grille de départ sur tapis tissu, vibreurs rouge et blanc."},
            {"@type": "ImageObject", "contentUrl": "https://rctableracingcar.fr/img/photos/soiree-course-table.jpg",
             "caption": "Quatre pilotes, un apéro, deux heures de course."},
            {"@type": "ImageObject", "contentUrl": "https://rctableracingcar.fr/img/photos/carrosseries-led.jpg",
             "caption": "Trois carrosseries et leurs plaques d’éclairage interchangeables."},
            {"@type": "ImageObject", "contentUrl": "https://rctableracingcar.fr/img/photos/echelle-dans-la-main.jpg",
             "caption": "Une voiture 1/76 de 5,8 cm dans le creux d’une main."},
        ],
    }],
    "body": """
<section class="page-head">
  <div class="wrap page-head-inner stack" style="--gap:20px">
    <p class="eyebrow">Communauté</p>
    <h1 class="h1" style="color:#fff">Galerie des circuits</h1>
    <p class="lead">Les pistes des pilotes francophones : tapis du commerce, constructions maison, tracés
    improbables sur une table de cuisine. Envoie les tiennes, elles seront publiées ici avec ton nom.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="gallery" data-stagger>
      <figure class="shot"><img src="img/photos/circuit-maison-80x120.webp" width="768" height="513" loading="lazy" decoding="async"
        alt="Circuit RC 1/76 fait maison vu de dessus : plaque beige, bordures blanches en polyuréthane, quatre voitures en piste">
        <figcaption>Circuit maison 80 × 120 cm : une plaque rigide, des bordures PU collées, quatre repères de virage. L’exemple le plus compact du site.</figcaption></figure>
      <figure class="shot"><img src="img/photos/grille-depart-carre.webp" width="941" height="706" loading="lazy" decoding="async"
        alt="Gros plan d’une grille de départ sur tapis tissu : MINI verte, coupé orange et deux buggys">
        <figcaption>La grille de départ d’un tapis du commerce, vibreurs rouge et blanc et emplacements peints.</figcaption></figure>
      <figure class="shot"><img src="img/photos/soiree-course-table.webp" width="900" height="675" loading="lazy" decoding="async"
        alt="Quatre pilotes debout autour d’un circuit RC 1/76 posé sur une table dans un bar">
        <figcaption>Quatre pilotes, un apéro, deux heures de course. Le format qui fait vivre la catégorie.</figcaption></figure>
      <figure class="shot"><img src="img/photos/carrosseries-led.webp" width="1000" height="589" loading="lazy" decoding="async"
        alt="Trois carrosseries RC 1/76 avec phares et bandeaux LED de couleurs différentes allumés">
        <figcaption>Les plaques d’éclairage se changent sans outil : vert, rouge, bleu. Aucun effet sur le chrono, beaucoup sur les photos.</figcaption></figure>
      <figure class="shot"><img src="img/photos/echelle-dans-la-main.webp" width="900" height="384" loading="lazy" decoding="async"
        alt="Voiture RC 1/76 posée dans le creux d’une main, qui montre ses 5,8 cm">
        <figcaption>5,8 cm : l’échelle 1/76 tient littéralement dans le creux de la main.</figcaption></figure>
      <figure class="shot"><img src="img/photos/tapis-turbo-racing-s.webp" width="1000" height="551" loading="lazy" decoding="async"
        alt="Plan d’un tapis de course Turbo Racing avec ligne de départ à damier et emplacements de grille">
        <figcaption>Un tapis du commerce : tracé imprimé, vibreurs, emplacements de grille et zone de stand.</figcaption></figure>
      <div class="shot shot--empty">
        <span class="tiny">Emplacement libre</span>
        <p class="h3">ta piste ici</p>
        <p class="prose" style="font-size:15px">Envoie une photo et une légende, elle est publiée avec ton nom.</p>
        <a class="btn btn--sm btn--race" href="contact.html">Envoyer une photo</a>
      </div>
    </div>
  </div>
</section>

""" + cta("Envie de construire la tienne ?", "circuits-et-tapis.html", "Circuits et tapis"),
}


# =========================================================================== #
#  ACTUS
# =========================================================================== #
_POSTS = [
    ("2026-07-27", "27 juil. 2026", "Essai", "Le châssis TC-06 après trois mois",
     "Une centaine de batteries plus tard : ce qui s’use, ce qui tient, et pourquoi la C76 reste la "
     "meilleure affaire de la gamme malgré l’arrivée de la C78.", "guide-turbo-racing-c76.html"),
    ("2026-07-20", "20 juil. 2026", "Atelier", "Un circuit 80 × 120 en carton rigide",
     "Le pas-à-pas du tracé le plus compact du site : découpe, collage des bordures polyuréthane, "
     "et les deux erreurs de conception à éviter.", "circuits-et-tapis.html"),
    ("2026-07-12", "12 juil. 2026", "Course", "Première soirée à quatre, règlement à l’épreuve",
     "Deux séries, une finale, et trois articles du règlement type réécrits après coup. Le compte rendu, "
     "avec les temps et ce qu’on a appris.", "reglement-type-de-course.html"),
    ("2026-07-04", "04 juil. 2026", "Matériel", "Passer à la radio P32S : ce que ça change",
     "Exponentiel de direction et gestion multi-modèles. Utile, mais pas avant d’avoir maîtrisé la radio "
     "d’origine — voici quand franchir le pas.", "comprendre-la-radiocommande.html"),
]

P["actus"] = {
    "head_bg": "photos/circuit-maison-80x120.webp",
    "url": "actus.html",
    "crumb": "Actus",
    "title": "Actus RC 1/76 — essais, ateliers et comptes rendus de course",
    "desc": "Nouveautés matériel, essais longue durée, ateliers de construction et comptes rendus "
            "de soirées : le journal du RC table car racing à l’échelle 1/76.",
    "image": "photos/circuit-maison-80x120.jpg",
    "image_alt": "Circuit RC 1/76 construit à la main",
    "priority": "0.75", "changefreq": "weekly",
    "page_type": "CollectionPage",
    "about": ["Actualités RC 1/76"],
    "jsonld": [{
        "@context": "https://schema.org",
        "@type": "Blog",
        "name": "Actus — RC Table Racing Car",
        "description": "Essais, ateliers et comptes rendus de course en RC 1/76.",
        "inLanguage": "fr-FR",
        "blogPost": [
            {"@type": "BlogPosting", "headline": t, "datePublished": d, "dateModified": d,
             "description": x, "articleSection": s,
             "author": {"@type": "Organization", "name": "RC Table Racing Car"},
             "url": "https://rctableracingcar.fr/" + u}
            for d, _, s, t, x, u in _POSTS
        ],
    }],
    "body": """
<section class="page-head">
  <div class="wrap page-head-inner stack" style="--gap:20px">
    <p class="eyebrow">Communauté · journal</p>
    <h1 class="h1" style="color:#fff">Actus</h1>
    <p class="lead">Nouveautés matériel, essais, comptes rendus de soirées et avancées de la catégorie.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div data-stagger>
""" + "".join(
        """      <article class="post">
        <div class="post-meta"><time datetime="{d}">{human}</time><span class="tag{race}">{sec}</span></div>
        <div><h2><a href="{u}" style="color:inherit">{t}</a></h2><p>{x}</p>
        <p style="margin-top:10px"><a class="link-arrow" href="{u}">Lire la page liée <span aria-hidden="true">→</span></a></p></div>
      </article>
""".format(d=d, human=h, sec=s.upper(), t=t, x=x, u=u, race=" tag--race" if i == 0 else "")
        for i, (d, h, s, t, x, u) in enumerate(_POSTS)) + """
    </div>
    <p class="tiny" style="margin-top:26px">Une info à partager, un essai à proposer ?
      <a href="contact.html">Écris-moi</a>.</p>
  </div>
</section>
""",
}


# =========================================================================== #
#  GLOSSAIRE
# =========================================================================== #
_TERMS = [
    ("1/76", "L’échelle de la catégorie : une voiture de 5 à 6 cm, soit 76 fois plus petite que le modèle réel."),
    ("Appairage", "La liaison radio-voiture. Se refait avec les deux contacteurs sous le châssis et le trombone du kit."),
    ("Bordure", "La glissière qui limite la piste, idéalement en polyuréthane autocollant. Elle renvoie la voiture au lieu de l’arrêter."),
    ("Corde", "Le point le plus intérieur d’un virage. On la serre au milieu de la courbe, pas à l’entrée."),
    ("Coreless", "Moteur sans noyau de fer, plus léger et plus réactif qu’un moteur classique. Le châssis TC-06 utilise un coreless 1020, qui tourne à environ 42 000 tr/min."),
    ("D/R · Dual Rate", "Réglage qui limite l’amplitude d’une commande : ST.D/R pour la direction, TH.D/R pour les gaz."),
    ("ESC", "Le variateur électronique : il traduit la position de la gâchette en puissance moteur. Intégré au châssis, non modifiable."),
    ("Exponentiel", "Courbe qui adoucit le centre de la commande de direction. Disponible sur les radios P32S et A82."),
    ("LiPo", "La batterie lithium-polymère du kit : 3,7 V pour 55 mAh, rechargée en USB-C. Ne se recharge jamais chaude, ne se stocke jamais complètement vide."),
    ("mAh", "Milliampère-heure, la capacité d’une batterie. Les 55 mAh du 1/76 donnent 20 à 30 minutes d’autonomie selon l’usage."),
    ("Neutre", "La position de repos d’une commande. Un neutre mal réglé fait avancer la voiture toute seule."),
    ("Pace car", "Voiture d’ouverture qui donne le rythme du tour de formation. La C82, hors gabarit, fait très bien l’affaire."),
    ("Propulsion · RWD", "Seules les roues arrière sont motrices, comme sur la plupart des voitures de course. C’est ce qui rend le survirage possible — et le contre-braquage utile."),
    ("Proportionnel", "Une commande qui répond progressivement à l’amplitude du geste, par opposition au tout-ou-rien des jouets."),
    ("RFID", "Étiquette collée sous le châssis, lue par un capteur au passage : la solution de comptage de tours la plus fiable."),
    ("RTR", "« Ready To Run » : le kit est complet et roule à la sortie de la boîte. C’est le cas de tous les 1/76."),
    ("Survirage", "L’arrière décroche avant l’avant. À cette échelle, presque toujours un excès de gaz sur des pneus sales."),
    ("TC-06", "La troisième génération de châssis Turbo Racing, partagée par les C76, C76LE et C78. La référence actuelle."),
    ("Trim", "Le réglage fin du neutre : ST.TRIM pour rouler droit, TH.TRIM pour trouver la vitesse zéro."),
]

P["glossaire"] = {
    "head_bg": "photos/chassis-vue-eclatee.webp",
    "url": "glossaire.html",
    "crumb": "Glossaire",
    "title": "Glossaire du RC 1/76 — 20 termes du RC racing sur table expliqués",
    "desc": "ESC, trim, dual rate, LiPo, RTR, survirage, TC-06, RFID : le vocabulaire du RC racing "
            "traduit pour l’échelle 1/76, en vingt définitions courtes et vérifiées.",
    "image": "photos/chassis-vue-eclatee.jpg",
    "image_alt": "Vue éclatée d’un châssis RC 1/76",
    "priority": "0.8",
    "about": ["Vocabulaire RC", "Termes techniques modélisme"],
    "jsonld": [{
        "@context": "https://schema.org",
        "@type": "DefinedTermSet",
        "name": "Glossaire du RC 1/76",
        "description": "Le vocabulaire du RC racing appliqué à l’échelle 1/76.",
        "inLanguage": "fr-FR",
        "hasDefinedTerm": [
            {"@type": "DefinedTerm", "name": t, "description": d,
             "inDefinedTermSet": "https://rctableracingcar.fr/glossaire.html"}
            for t, d in _TERMS
        ],
    }],
    "body": """
<section class="page-head">
  <div class="wrap page-head-inner stack" style="--gap:20px">
    <p class="eyebrow">Ressources</p>
    <h1 class="h1" style="color:#fff">Glossaire du 1/76</h1>
    <p class="lead">Le vocabulaire du RC racing, traduit pour l’échelle de la table.
    À garder ouvert la première semaine.</p>
    <ul class="facts"><li><b>20 termes</b></li><li>Balisé <b>DefinedTermSet</b></li></ul>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <dl class="gloss" data-stagger>
""" + "".join(
        '      <div class="gloss-item"><dt>{t}</dt><dd>{d}</dd></div>\n'.format(t=t, d=d)
        for t, d in _TERMS) + """    </dl>
    <p class="tiny" style="margin-top:22px">Un terme manque ? <a href="contact.html">Signale-le</a>.</p>
  </div>
</section>

""" + cta("Les questions qui reviennent le plus souvent.", "questions-frequentes.html", "Questions fréquentes"),
}


# =========================================================================== #
#  FAQ
# =========================================================================== #
_FAQ = [
    ("C’est un jouet ou du modélisme ?",
     "Du modélisme. Direction et accélération proportionnelles, trims, dual rate, limiteur de puissance, "
     "pneus interchangeables, batterie rechargeable : tout l’essentiel du RC racing est là, simplement miniaturisé."),
    ("Quel âge minimum ?",
     "À partir de 8-10 ans avec le limiteur TH.LIM sur 20 %. Les pièces sont petites : ce n’est pas un jouet "
     "pour les tout-petits, mais c’est une excellente première radiocommande."),
    ("Ça roule sur quoi ?",
     "Idéalement un tapis tissu de course, posé sur une table plane. Une table nue est trop glissante, une "
     "moquette épaisse trop molle. Les bordures sont indispensables dès qu’on roule vite."),
    ("Combien de temps roule une batterie ?",
     "Compte entre 20 et 30 minutes selon l’usage, selon le niveau de puissance et le style de conduite. "
     "Laisse refroidir la LiPo 3,7 V de 55 mAh avant de recharger, et "
     "compte cinq minutes de charge en USB-C. Deux batteries de rechange changent une soirée."),
    ("Quelle est la fiche technique de la Turbo Racing C76 ?",
     "Échelle 1/76, 5,8 cm de long, châssis TC-06 v3 à empattement réglable de 33,5 à 34,5 mm, propulsion, "
     "moteur coreless 1020 tournant à environ 42 000 tr/min, trois modes de puissance (20 %, 50 %, 100 %), "
     "batterie LiPo 3,7 V 55 mAh rechargée en USB-C, radiocommande 2,4 GHz proportionnelle, LED avant et "
     "arrière, vitesse annoncée autour de 6 km/h. Livrée RTR, prête à rouler, pour environ 85 €."),
    ("Peut-on rouler à plusieurs sur la même piste ?",
     "Oui : c’est tout l’intérêt. Chaque voiture s’appaire à sa propre radio, sans réglage de fréquence. "
     "Quatre pilotes tiennent confortablement sur un tapis L, huit sur un XL."),
    ("Faut-il un système de chronométrage ?",
     "Pas pour commencer : un téléphone et un compteur de tours à la voix suffisent. Ensuite, il existe des "
     "applications qui suivent les voitures à la caméra, et des capteurs RFID collés sous le châssis."),
    ("La C76 est-elle vraiment la meilleure ?",
     "C’est la meilleure base de compétition à ce jour : châssis TC-06, comportement prévisible, et un prix "
     "inférieur aux C76LE et C78 qui partagent la même mécanique. Pour courser à armes égales, choisissez tous la même."),
    ("Peut-on améliorer sa voiture ?",
     "Un peu, et c’est volontaire : l’esprit de la catégorie est de rester proche de la série. Propreté de la "
     "transmission, pneus sains, trims justes et batterie en forme comptent bien plus que n’importe quelle option."),
    ("Où acheter en France ?",
     "Les boutiques de modélisme en ligne, les revendeurs Turbo Racing, et les grandes plateformes. Vérifie "
     "toujours que le kit est complet (radio, chargeur, deux carrosseries) et prévois quatre piles AAA."),
    ("Existe-t-il des compétitions officielles ?",
     "Pas encore de championnat structuré en 1/76. Des rencontres locales s’organisent via les groupes Facebook. "
     "C’est précisément l’ambition de ce site : rassembler assez de pilotes pour que ça arrive."),
]

P["faq"] = {
    "head_bg": "photos/echelle-dans-la-main.webp",
    "url": "questions-frequentes.html",
    "crumb": "Questions fréquentes",
    "title": "Questions fréquentes sur le RC 1/76 — les 11 réponses essentielles",
    "desc": "Jouet ou modélisme, âge minimum, surface de roulage, autonomie, chronométrage, choix du "
            "modèle, fiche technique, où acheter : les onze questions les plus fréquentes sur le RC racing sur table.",
    "image": "photos/echelle-dans-la-main.jpg",
    "image_alt": "Voiture RC 1/76 posée dans le creux d’une main",
    "priority": "0.85",
    "page_type": "FAQPage",
    "about": ["FAQ RC 1/76"],
    "speakable": [".faq summary", ".faq .faq-a"],
    "jsonld": [{
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "inLanguage": "fr-FR",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in _FAQ
        ],
    }],
    "body": """
<section class="page-head">
  <div class="wrap page-head-inner stack" style="--gap:20px">
    <p class="eyebrow">Ressources</p>
    <h1 class="h1" style="color:#fff">Questions fréquentes</h1>
    <p class="lead">Les onze questions qui reviennent le plus souvent, de la part des curieux comme des modélistes.</p>
    <ul class="facts"><li><b>11 questions</b></li><li>Balisé <b>FAQPage</b></li></ul>
  </div>
</section>

<section class="section">
  <div class="wrap-narrow">
    <div class="faq" data-reveal>
""" + "".join(
        '      <details{op}><summary><h2 style="display:inline;font:inherit;text-transform:inherit">{q}</h2></summary>'
        '<div class="faq-a"><p>{a}</p></div></details>\n'.format(q=q, a=a, op=" open" if i == 0 else "")
        for i, (q, a) in enumerate(_FAQ)) + """    </div>
    <p class="tiny" style="margin-top:28px">Ta question n’est pas là ? <a href="contact.html">Pose-la</a>.</p>
  </div>
</section>

""" + cta("Le vocabulaire technique, terme par terme.", "glossaire.html", "Le glossaire"),
}


# =========================================================================== #
#  CONTACT
# =========================================================================== #
P["contact"] = {
    "head_bg": "photos/soiree-course-large.webp",
    "url": "contact.html",
    "crumb": "Contact",
    "title": "Contact — signaler un club, proposer une photo, corriger une erreur",
    "desc": "Ce site est tenu par un pilote, pas par une marque. Écrivez pour signaler un club, "
            "proposer une photo de circuit, corriger une erreur technique ou organiser une rencontre.",
    "image": "photos/soiree-course-table.jpg",
    "image_alt": "Pilotes autour d’un circuit RC 1/76",
    "priority": "0.6",
    "page_type": "ContactPage",
    "tools": True,
    "body": """
<section class="page-head">
  <div class="wrap page-head-inner stack" style="--gap:20px">
    <p class="eyebrow">Communauté</p>
    <h1 class="h1" style="color:#fff">Contact</h1>
    <p class="lead">Ce site est tenu par un pilote, pas par une marque. Écris-moi pour signaler un club,
    proposer une photo de circuit, corriger une erreur technique ou organiser une rencontre.</p>
  </div>
</section>

<section class="section">
  <div class="wrap grid g-side" style="align-items:start">
    <div data-reveal="left">
      <h2 class="h2" style="margin-bottom:22px">Écrire un message</h2>
      <form id="contact-form" class="form-grid" novalidate>
        <div><label class="lb" for="f-nom">Nom</label>
          <input class="inp" id="f-nom" name="nom" type="text" autocomplete="name" required placeholder="Ton nom ou ton pseudo"></div>
        <div><label class="lb" for="f-mail">E-mail</label>
          <input class="inp" id="f-mail" name="email" type="email" autocomplete="email" required placeholder="pour te répondre"></div>
        <div><label class="lb" for="f-sujet">Sujet</label>
          <select class="inp" id="f-sujet" name="sujet">
            <option>Signaler un club</option><option>Photo de circuit</option>
            <option>Correction technique</option><option>Organiser une rencontre</option><option>Autre</option>
          </select></div>
        <div><label class="lb" for="f-msg">Message</label>
          <textarea class="inp" id="f-msg" name="message" required placeholder="Ville, matériel, ce que tu veux partager…"></textarea></div>
        <div><button type="submit" class="btn btn--race">Envoyer <span class="arrow" aria-hidden="true">→</span></button></div>
        <p id="form-note" class="tiny" tabindex="-1" hidden style="color:var(--race-dark)">
          Ton logiciel de messagerie vient de s’ouvrir avec le message prérempli. Il ne reste qu’à l’envoyer.</p>
      </form>
      <p class="tiny" style="margin-top:16px">Ce formulaire ouvre ton logiciel de messagerie : aucune donnée
      ne transite par ce site, il n’y a ni serveur ni base de données.</p>
    </div>

    <div class="stack" style="--gap:20px" data-reveal="right">
      <div class="callout callout--race"><span class="tiny">Le plus rapide</span>
        <h2 class="h3" style="margin:6px 0 10px">Le groupe Facebook</h2>
        <p class="prose">« Turbo Racing RC 1:76 France » — pour une réponse en quelques heures et l’avis de
        plusieurs pilotes plutôt qu’un seul.</p></div>
      <div class="callout"><span class="tiny">Ce site est indépendant</span>
        <p class="prose" style="margin-top:8px">Aucun partenariat, aucune commission, aucun lien commercial avec
        Turbo&nbsp;Racing, LDARC ou les revendeurs cités. Les prix sont des ordres de grandeur constatés,
        pas des offres.</p></div>
      <div class="callout"><span class="tiny">Une erreur technique ?</span>
        <p class="prose" style="margin-top:8px">Signale-la précisément — page, phrase, et ce qui devrait être
        écrit. Le but est que ce site devienne la référence du 1/76, et ça se construit à plusieurs.</p></div>
    </div>
  </div>
</section>
""",
}


# =========================================================================== #
#  MENTIONS LÉGALES
# =========================================================================== #
P["mentions"] = {
    "head_bg": "photos/grille-depart-tapis.webp",
    "url": "mentions-legales.html",
    "crumb": "Mentions légales",
    "title": "Mentions légales — RC Table Racing Car",
    "desc": "Éditeur, hébergement, propriété intellectuelle, absence de lien commercial et absence "
            "de collecte de données personnelles sur RC Table Racing Car.",
    "priority": "0.2", "changefreq": "yearly",
    "body": """
<section class="page-head">
  <div class="wrap page-head-inner stack" style="--gap:16px">
    <p class="eyebrow">Informations</p>
    <h1 class="h1" style="color:#fff">Mentions légales</h1>
  </div>
</section>
<section class="section">
  <div class="wrap-narrow stack" style="--gap:28px">
    <div><h2 class="h3" style="margin-bottom:10px">Éditeur</h2>
      <p class="prose">Site personnel édité par un passionné de modélisme RC, à titre non commercial.
      Contact : le <a href="contact.html">formulaire de contact</a>.</p></div>
    <div><h2 class="h3" style="margin-bottom:10px">Indépendance</h2>
      <p class="prose">RC Table Racing Car n’a aucun lien commercial, partenariat ni programme d’affiliation
      avec Turbo Racing, LDARC ou les revendeurs cités. Les marques et références sont mentionnées à titre
      strictement informatif. Les prix indiqués sont des ordres de grandeur constatés en 2026 et ne
      constituent pas des offres de vente.</p></div>
    <div><h2 class="h3" style="margin-bottom:10px">Données personnelles</h2>
      <p class="prose">Ce site est un ensemble de pages statiques. Il ne dépose aucun cookie, n’utilise
      aucun outil de mesure d’audience et ne collecte aucune donnée personnelle. Les outils interactifs
      (comparateur, sélecteur, calculateur de budget) fonctionnent entièrement dans le navigateur : aucune
      information saisie n’est transmise. Le formulaire de contact ouvre votre logiciel de messagerie et
      ne transite par aucun serveur.</p></div>
    <div><h2 class="h3" style="margin-bottom:10px">Propriété intellectuelle</h2>
      <p class="prose">Les textes et illustrations de ce site sont la propriété de leur auteur. Toute
      reprise est bienvenue à condition de citer « RC Table Racing Car » et de renvoyer vers la page source.
      Les photos envoyées par les pilotes restent la propriété de leurs auteurs et sont publiées avec
      leur accord.</p></div>
    <div><h2 class="h3" style="margin-bottom:10px">Responsabilité</h2>
      <p class="prose">Les informations techniques sont fournies de bonne foi et vérifiées, mais sans
      garantie. Les batteries lithium-polymère demandent des précautions : ne jamais charger une batterie
      chaude, gonflée ou endommagée, et ne jamais laisser une charge sans surveillance.</p></div>
    <div><h2 class="h3" style="margin-bottom:10px">Hébergement</h2>
      <p class="prose">À compléter avec le nom et l’adresse de votre hébergeur avant la mise en ligne.</p></div>
  </div>
</section>
""",
}


# =========================================================================== #
#  PLAN DU SITE
# =========================================================================== #
P["plan"] = {
    "head_bg": "photos/grille-depart-tapis.webp",
    "url": "plan-du-site.html",
    "crumb": "Plan du site",
    "title": "Plan du site — RC Table Racing Car",
    "desc": "Toutes les pages de RC Table Racing Car : débuter, matériel, pilotage, communauté "
            "et ressources sur le RC racing sur table à l’échelle 1/76.",
    "priority": "0.4", "changefreq": "monthly",
    "body": """
<section class="page-head">
  <div class="wrap page-head-inner stack" style="--gap:16px">
    <p class="eyebrow">Navigation</p>
    <h1 class="h1" style="color:#fff">Plan du site</h1>
    <p class="lead">Vingt pages, quatre outils interactifs.</p>
  </div>
</section>
<section class="section">
  <div class="wrap grid g3" data-stagger>
    <div class="card card--flat"><h2 class="h3">Débuter</h2><ul style="display:grid;gap:9px;margin-top:8px">
      <li style="list-style:none"><a href="debuter-en-10-minutes.html">Débuter en 10 minutes</a></li>
      <li style="list-style:none"><a href="le-concept.html">Le concept 1/76</a></li>
      <li style="list-style:none"><a href="ou-acheter-et-budget.html">Où acheter &amp; budget</a></li></ul></div>
    <div class="card card--flat"><h2 class="h3">Matériel</h2><ul style="display:grid;gap:9px;margin-top:8px">
      <li style="list-style:none"><a href="choisir-son-modele.html">Choisir son modèle</a></li>
      <li style="list-style:none"><a href="guide-turbo-racing-c76.html">Guide du Turbo Racing C76</a></li>
      <li style="list-style:none"><a href="comprendre-la-radiocommande.html">Comprendre la radiocommande</a></li>
      <li style="list-style:none"><a href="circuits-et-tapis.html">Circuits et tapis</a></li>
      <li style="list-style:none"><a href="systemes-de-comptage.html">Les systèmes de comptage</a></li></ul></div>
    <div class="card card--flat"><h2 class="h3">Piloter</h2><ul style="display:grid;gap:9px;margin-top:8px">
      <li style="list-style:none"><a href="reglages-et-pilotage.html">Réglages &amp; pilotage</a></li>
      <li style="list-style:none"><a href="entretien-et-personnalisation.html">Entretien &amp; personnalisation</a></li>
      <li style="list-style:none"><a href="reglement-type-de-course.html">Règlement type de course</a></li></ul></div>
    <div class="card card--flat"><h2 class="h3">Communauté</h2><ul style="display:grid;gap:9px;margin-top:8px">
      <li style="list-style:none"><a href="clubs-et-competitions.html">Clubs &amp; compétitions</a></li>
      <li style="list-style:none"><a href="galerie-des-circuits.html">Galerie des circuits</a></li>
      <li style="list-style:none"><a href="actus.html">Actus</a></li>
      <li style="list-style:none"><a href="contact.html">Contact</a></li></ul></div>
    <div class="card card--flat"><h2 class="h3">Ressources</h2><ul style="display:grid;gap:9px;margin-top:8px">
      <li style="list-style:none"><a href="glossaire.html">Glossaire du 1/76</a></li>
      <li style="list-style:none"><a href="questions-frequentes.html">Questions fréquentes</a></li>
      <li style="list-style:none"><a href="mentions-legales.html">Mentions légales</a></li></ul></div>
    <div class="card card--flat"><h2 class="h3">Outils</h2><ul style="display:grid;gap:9px;margin-top:8px">
      <li style="list-style:none"><a href="choisir-son-modele.html#comparateur">Comparateur Turbo Racing</a></li>
      <li style="list-style:none"><a href="choisir-son-modele.html#selecteur">Quelle voiture pour moi ?</a></li>
      <li style="list-style:none"><a href="comprendre-la-radiocommande.html#radio-tool">La radio bouton par bouton</a></li>
      <li style="list-style:none"><a href="ou-acheter-et-budget.html#budget-tool">Calculateur de budget</a></li></ul></div>
  </div>
</section>
""",
}


# =========================================================================== #
#  404
# =========================================================================== #
P["404"] = {
    "head_bg": "photos/grille-depart-tapis.webp",
    "url": "404.html",
    "crumb": "Page introuvable",
    "title": "Page introuvable — RC Table Racing Car",
    "desc": "Cette page n’existe pas ou a changé d’adresse. Retrouvez le guide du RC racing "
            "sur table à l’échelle 1/76 depuis l’accueil ou le plan du site.",
    "priority": "0.1", "changefreq": "yearly",
    "body": """
<section class="section" style="background:var(--ink);color:var(--text-inv);min-height:56vh;display:grid;align-items:center">
  <div class="wrap stack" style="--gap:22px">
    <p class="eyebrow">Erreur 404</p>
    <h1 class="h-hero" style="color:#fff">Sortie<br>de piste.</h1>
    <p class="lead">Cette page n’existe pas, ou elle a changé d’adresse. Reprends la course ici :</p>
    <div class="btn-row">
      <a class="btn btn--race" href="index.html">Retour à l’accueil</a>
      <a class="btn btn--ghost-inv" href="plan-du-site.html">Plan du site</a>
    </div>
  </div>
</section>
""",
}
