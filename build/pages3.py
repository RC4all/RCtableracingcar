# -*- coding: utf-8 -*-
"""Entretien · Circuits et tapis · Budget · Règlement type"""
from content import cta

P = {}

# =========================================================================== #
#  ENTRETIEN & PERSONNALISATION
# =========================================================================== #
P["entretien"] = {
    "head_bg": "photos/carrosseries-led.webp",
    "url": "entretien-et-personnalisation.html",
    "crumb": "Entretien & personnalisation",
    "title": "Entretien d’une RC 1/76 — la routine batterie par batterie",
    "desc": "Une minute d’entretien entre chaque batterie : cheveux à la pincette, pneus au chiffon, "
            "roues libres, charge à froid. Plus la méthode pour peindre ses carrosseries "
            "en polycarbonate.",
    "image": "photos/carrosseries-led.jpg",
    "image_alt": "Trois carrosseries RC 1/76 éclairées par leurs LED",
    "priority": "0.8",
    "og_type": "article",
    "about": ["Entretien RC", "Batterie LiPo", "Peinture polycarbonate"],
    "speakable": [".answer"],
    "jsonld": [{
        "@context": "https://schema.org",
        "@type": "HowTo",
        "name": "La routine d’entretien d’une voiture RC 1/76, batterie par batterie",
        "description": "Cinq gestes d’entretien à répéter entre chaque batterie pour conserver "
                       "la vitesse et la fiabilité d’une RC à l’échelle 1/76.",
        "totalTime": "PT6M",
        "inLanguage": "fr-FR",
        "tool": [{"@type": "HowToTool", "name": "Une pincette"},
                 {"@type": "HowToTool", "name": "Un chiffon légèrement humide"}],
        "step": [
            {"@type": "HowToStep", "position": 1, "name": "Retirer cheveux et fibres", "text": "30 secondes : cheveux et fibres retirés à la pincette autour des axes de roues."},
            {"@type": "HowToStep", "position": 2, "name": "Nettoyer les pneus", "text": "15 secondes : pneus essuyés au chiffon légèrement humide, puis séchés."},
            {"@type": "HowToStep", "position": 3, "name": "Vérifier que les roues tournent libres", "text": "10 secondes : roues tournées à la main, elles doivent tourner librement, sans point dur."},
            {"@type": "HowToStep", "position": 4, "name": "Recharger la batterie à froid", "text": "5 minutes : batterie refroidie, puis rechargée. Jamais de charge sur une LiPo chaude."},
            {"@type": "HowToStep", "position": 5, "name": "Ranger", "text": "Tapis roulé sans plier les bordures, voitures rangées à plat."},
        ],
    }],
    "body": """
<section class="page-head">
  <div class="wrap page-head-inner stack" style="--gap:20px">
    <p class="eyebrow">Piloter · atelier</p>
    <h1 class="h1" style="color:#fff">Entretien &amp; personnalisation</h1>
    <p class="lead">Une 1/76 bien entretenue va plus vite qu’une 1/76 modifiée. L’esprit de la catégorie est
    de rester proche de la série : ce qui reste à faire, c’est la propreté — et la peinture.</p>
    <ul class="facts"><li>Routine <b>≈ 1 min</b></li><li>Entre <b>chaque batterie</b></li><li>Charge <b>jamais à chaud</b></li></ul>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="answer" style="margin-bottom:40px" data-reveal><strong>Une minute entre chaque batterie suffit.</strong>
    Cheveux retirés à la pincette (30&nbsp;s), pneus essuyés au chiffon humide (15&nbsp;s), roues vérifiées
    libres (10&nbsp;s), puis charge une fois la batterie refroidie. C’est le meilleur gain de vitesse
    disponible, et il est gratuit.</p>

    <h2 class="h2" style="margin-bottom:26px" data-reveal>La routine, batterie par batterie</h2>
    <ol class="steps" data-stagger>
      <li class="step"><span class="step-n" aria-hidden="true">30s</span><div><h3 class="h3">Les axes de roues</h3><p>Cheveux et fibres retirés à la pincette autour des axes. C’est la première cause de perte de vitesse, loin devant toutes les autres.</p></div></li>
      <li class="step"><span class="step-n" aria-hidden="true">15s</span><div><h3 class="h3">Les pneus</h3><p>Essuyés au chiffon légèrement humide, puis séchés. Aucun produit miracle ne fait mieux.</p></div></li>
      <li class="step"><span class="step-n" aria-hidden="true">10s</span><div><h3 class="h3">Les roues à la main</h3><p>Elles doivent tourner libres, sans point dur. Un point dur signale une fibre coincée ou un axe forcé.</p></div></li>
      <li class="step"><span class="step-n" aria-hidden="true">5min</span><div><h3 class="h3">La charge</h3><p>Batterie refroidie, puis rechargée. Jamais de charge sur une LiPo chaude : c’est ce qui la tue en une saison.</p></div></li>
      <li class="step"><span class="step-n" aria-hidden="true">Fin</span><div><h3 class="h3">Le rangement</h3><p>Tapis roulé sans plier les bordures, voitures rangées à plat.</p></div></li>
    </ol>
  </div>
</section>

<section class="section section--paper2">
  <div class="wrap">
    <div class="grid g-side">
    <div class="stack" data-reveal="left">
      <p class="eyebrow">Atelier</p>
      <h2 class="h2">Peindre ses carrosseries</h2>
      <p class="prose">Le kit livre deux carrosseries vierges : c’est l’invitation. Dégraisse, applique une
      peinture pour polycarbonate en couches très fines <strong>depuis l’intérieur</strong>, laisse sécher
      entre les passes, puis pose les stickers de numéro.</p>
      <p class="prose">Une flotte où chacun reconnaît sa voiture d’un coup d’œil change complètement
      l’ambiance d’une course — et c’est la seule personnalisation que le règlement encourage.</p>
    </div>
    <figure class="fig" data-reveal="right">
      <img src="img/photos/carrosseries-led.webp" width="1000" height="589" loading="lazy" decoding="async" alt="Trois carrosseries RC 1/76 peintes différemment, éclairage LED allumé sous chaque châssis">
      <figcaption>Trois carrosseries, trois identités : la différence se voit, pas au chrono.</figcaption>
    </figure>
    </div>
    <figure class="fig" style="max-width:800px;margin:36px auto 0" data-reveal>
      <img src="img/photos/aerographe-debutant.jpg" width="1000" height="517" loading="lazy" decoding="async"
           alt="Aérographe portatif utilisé pour appliquer une fine couche de peinture sur une maquette">
      <figcaption><strong>Pas besoin de matériel coûteux pour commencer.</strong> Un aérographe simple autour de
      20&nbsp;€ fait déjà l’affaire pour peindre une carrosserie 1/76 : travaille avec des couches fines,
      laisse sécher entre les passes et nettoie l’outil immédiatement après usage.</figcaption>
    </figure>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="eyebrow" data-reveal>Savoir ce qu’on nettoie</p>
    <h2 class="h2" style="margin:12px 0 28px" data-reveal>Les deux ensembles qui s’encrassent</h2>
    <figure class="fig" style="max-width:760px;margin:0 auto 36px" data-reveal>
      <img src="img/photos/chassis-demontage-anglais.png" width="1234" height="1274" loading="lazy" decoding="async"
           alt="Vue éclatée complète d’une voiture Turbo Racing : carrosserie, vis, carte électronique, coque supérieure, transmission, roues, direction et coque inférieure">
      <figcaption><strong>Commencer par la vue d’ensemble.</strong> Elle montre l’ordre logique de démontage :
      carrosserie, vis, coque supérieure, transmission et trains roulants, avant d’ouvrir le châssis.</figcaption>
    </figure>
    <div class="grid g2" data-stagger>
      <figure class="fig exploded" style="max-width:520px">
        <div class="canvas">
          <img src="img/photos/transmission-vue-eclatee.webp" width="637" height="900" loading="lazy" decoding="async"
               alt="Vue éclatée de la transmission d’une RC 1/76 : pignons, arbre de transmission, axe et roues arrière, avec les références de pièces">
          <span class="xl xl--dark" style="--x:4.7%;--y:3.4%">Arbre de transmission</span>
          <span class="xl xl--dark" style="--x:4.7%;--y:44.2%">Train arrière</span>
        </div>
        <figcaption>La transmission et le train arrière, <strong>intitulés traduits</strong>. C’est là que
        cheveux et fibres s’enroulent, et c’est la première cause de perte de vitesse.</figcaption>
      </figure>
      <figure class="fig">
        <img src="img/photos/direction-vue-eclatee.webp" width="634" height="900" loading="lazy" decoding="async"
             alt="Vue éclatée de la direction d’une RC 1/76 : pignon de direction, biellettes, fusées et roues avant">
        <figcaption>La direction : pignon, biellettes et fusées. Si le trim doit être poussé à fond,
        c’est ici qu’il faut regarder avant de compenser à la radio.</figcaption>
      </figure>
    </div>
    <figure class="fig" style="max-width:700px;margin:36px auto 0" data-reveal>
      <img src="img/photos/chassis-ouverture-anglais.png" width="1038" height="1515" loading="lazy" decoding="async"
           alt="Schéma d’ouverture du châssis Turbo Racing : coque supérieure et inférieure, moteur de propulsion, moteur de direction et emplacements de transmission">
      <figcaption><strong>Ouvrir le châssis sans se perdre.</strong> Retire les vis, soulève la coque supérieure,
      puis repère le moteur de propulsion (<em>Drive motor</em>), le moteur de direction (<em>Steering motor</em>)
      et les deux étages de transmission avant de nettoyer.</figcaption>
    </figure>
    <p class="tiny" style="margin-top:16px">Vues éclatées issues de la documentation Turbo Racing.</p>
  </div>
</section>

<section class="section section--dark">
  <div class="wrap" data-reveal>
    <p class="eyebrow">Ce qu’on ne modifie pas</p>
    <h2 class="h1" style="margin:14px 0 20px;max-width:22ch">Moteur, électronique et pignons restent d’origine</h2>
    <p class="lead">C’est le pacte qui rend la catégorie intéressante : à matériel identique, le classement
    récompense le pilotage. Si tu veux jouer avec les rapports et les moteurs, les échelles supérieures sont
    faites pour ça. Ici, la seule modification qui compte, c’est celle de ton geste.</p>
    <p style="margin-top:24px"><a class="btn btn--race" href="reglement-type-de-course.html">Le règlement type <span class="arrow" aria-hidden="true">→</span></a></p>
  </div>
</section>
""",
}


# =========================================================================== #
#  CIRCUITS ET TAPIS
# =========================================================================== #
P["circuits"] = {
    "head_bg": "photos/tapis-ldarc-2412a.webp",
    "url": "circuits-et-tapis.html",
    "crumb": "Circuits et tapis",
    "title": "Circuits et tapis RC 1/76 — dimensions, bordures et tracés",
    "desc": "Comparatif des tapis de course RC 1/76 de 95 × 50 cm à 240 × 120 cm, rôle des bordures "
            "en polyuréthane, construction d’un circuit maison et solutions de comptage de tours.",
    "image": "photos/tapis-ldarc-1609a.jpg",
    "image_alt": "Plan d’un tapis de course RC 1/76 avec vibreurs et ligne de départ",
    "priority": "0.85",
    "og_type": "article",
    "about": ["Tapis de course RC", "Bordures polyuréthane", "Circuit RC maison", "Comptage de tours RFID"],
    "speakable": [".answer"],
    "jsonld": [{
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": "Les tapis de course pour le RC 1/76",
        "description": "Tapis tissu utilisés en RC table car racing, du format entraînement au format course.",
        "numberOfItems": 5,
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "LDARC XL — 240 × 120 cm — course jusqu’à 8 pilotes"},
            {"@type": "ListItem", "position": 2, "name": "LDARC L — 160 × 90 cm — course"},
            {"@type": "ListItem", "position": 3, "name": "Turbo Racing L — 160 × 90 cm — course"},
            {"@type": "ListItem", "position": 4, "name": "Turbo Racing M — 120 × 80 cm — démonstration"},
            {"@type": "ListItem", "position": 5, "name": "Turbo Racing XS — 95 × 50 cm — entraînement"},
        ],
    }],
    "body": """
<section class="page-head">
  <div class="wrap page-head-inner stack" style="--gap:20px">
    <p class="eyebrow">Matériel · la piste</p>
    <h1 class="h1" style="color:#fff">Circuits et tapis</h1>
    <p class="lead">Sans circuit, la discipline perd tout son intérêt. C’est l’élément qui permet d’apprendre
    et de se mesurer. Un petit tapis suffit pour s’entraîner ; il faut du grand pour se battre à cinq, six ou huit.</p>
    <ul class="facts"><li>Du <b>95 × 50</b> au <b>240 × 120 cm</b></li><li>Piste <b>≈ 12 cm</b> de large</li><li>Bordures <b>PU autocollant</b></li></ul>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="answer" style="margin-bottom:40px" data-reveal><strong>Le critère décisif est la largeur de piste,
    pas la surface totale.</strong> Trop étroit, on ne peut pas doubler et la course devient une file indienne.
    Compte un <strong>160 × 90 cm</strong> pour quatre pilotes et un <strong>240 × 120 cm</strong> pour huit.
    Un <strong>95 × 50 cm</strong> reste parfait pour s’entraîner seul.</p>

    <h2 class="h2" style="margin-bottom:24px" data-reveal>Les tapis à privilégier</h2>
    <div class="table-wrap" data-reveal>
      <table class="data">
        <caption>Tapis tissu utilisés en RC 1/76 · le critère décisif est la largeur de piste</caption>
        <thead><tr><th scope="col">Marque / référence</th><th scope="col">Dimensions</th><th scope="col">Surface</th><th scope="col">Usage</th></tr></thead>
        <tbody>
          <tr class="is-star"><th scope="row">LDARC XL</th><td>240 × 120 cm</td><td>Tissu + bordures</td><td>Course, jusqu’à 8 pilotes</td></tr>
          <tr><th scope="row">LDARC L</th><td>160 × 90 cm</td><td>Tissu + bordures</td><td>Course</td></tr>
          <tr><th scope="row">Turbo Racing L</th><td>160 × 90 cm</td><td>Tissu</td><td>Course</td></tr>
          <tr><th scope="row">Turbo Racing M</th><td>120 × 80 cm</td><td>Tissu</td><td>Démonstration</td></tr>
          <tr><th scope="row">Turbo Racing XS</th><td>95 × 50 cm</td><td>Tissu</td><td>Entraînement</td></tr>
        </tbody>
      </table>
    </div>

    <div class="grid g2" style="margin-top:44px" data-stagger>
      <figure class="fig">
        <img src="img/tailles-tapis.png" width="1600" height="920" loading="lazy" decoding="async"
             alt="Les quatre tailles de tapis RC 1/76 superposées à l’échelle : XS, M, L et XL">
        <figcaption>L’emprise réelle des quatre tapis, à l’échelle. Un XL demande une vraie table.</figcaption>
      </figure>
      <figure class="fig">
        <img src="img/photos/tapis-ldarc-1609a.webp" width="1024" height="584" loading="lazy" decoding="async" alt="Plan du tapis LDARC 1609A de 160 × 90 cm : piste noire, vibreurs rouge et blanc, ligne de départ à damier et zone de stand">
        <figcaption>Le tapis LDARC 1609A (160 × 90 cm) : vibreurs sur tous les virages, ligne de départ et zone de stand.</figcaption>
      </figure>
    </div>
  </div>
</section>

<section class="section section--paper2">
  <div class="wrap">
    <p class="eyebrow" data-reveal>Les tracés du commerce</p>
    <h2 class="h2" style="margin:12px 0 10px" data-reveal>À quoi ressemble un tapis, concrètement</h2>
    <p class="lead" style="margin-bottom:30px" data-reveal>Tous impriment la même grammaire : piste noire,
    vibreurs rouge et blanc dans les virages, ligne de départ à damier, emplacements de grille et zone de stand.
    Ce qui change, c’est la longueur des lignes droites et le nombre d’épingles.</p>
    <div class="grid g2" data-stagger>
      <figure class="fig">
        <img src="img/photos/tapis-ldarc-2412a.webp" width="1023" height="518" loading="lazy" decoding="async"
             alt="Plan du tapis LDARC 2412A de 240 × 120 cm : long tracé avec deux grandes courbes, épingle centrale, zone de stand et de relais">
        <figcaption><strong>LDARC 2412A · 240 × 120 cm.</strong> Le format course : jusqu’à huit pilotes,
        des lignes droites qui permettent vraiment de doubler.</figcaption>
      </figure>
      <figure class="fig">
        <img src="img/photos/tapis-ldarc-1609a.webp" width="1024" height="584" loading="lazy" decoding="async"
             alt="Plan du tapis LDARC 1609A de 160 × 90 cm : tracé technique avec épingles, ligne de départ à damier et zone de stand">
        <figcaption><strong>LDARC 1609A · 160 × 90 cm.</strong> Le meilleur compromis : quatre pilotes à
        l’aise sur une table de salle à manger.</figcaption>
      </figure>
      <figure class="fig">
        <img src="img/photos/tapis-turbo-racing-xl.webp" width="1024" height="588" loading="lazy" decoding="async"
             alt="Plan d’un tapis de course Turbo Racing avec chicane, zone de stand et plan d’eau décoratif">
        <figcaption><strong>Turbo Racing, grand format.</strong> Tracé plus sinueux, davantage de points
        de corde à travailler.</figcaption>
      </figure>
      <figure class="fig">
        <img src="img/photos/tapis-turbo-racing-l.webp" width="1023" height="684" loading="lazy" decoding="async"
             alt="Plan d’un tapis de course Turbo Racing avec quatre emplacements de grille numérotés et ligne de départ à damier">
        <figcaption><strong>Turbo Racing, format L.</strong> Quatre emplacements de grille numérotés,
        prêts pour un départ arrêté.</figcaption>
      </figure>
    </div>
    <p class="tiny" style="margin-top:16px">Plans des fabricants, reproduits à titre informatif. Ce site n’a
    aucun lien commercial avec Turbo Racing ni LDARC.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="grid g-side">
      <figure class="fig" data-reveal="left">
      <img src="img/bordure-coupe.png" width="1200" height="680" loading="lazy" decoding="async"
           alt="Vue en coupe d’une bordure en polyuréthane collée sur un tapis de course RC">
      <figcaption>En coupe : la bordure PU agit comme une glissière et renvoie la voiture en piste.</figcaption>
      </figure>
      <div class="stack" data-reveal="right">
      <p class="eyebrow">Indispensable</p>
      <h2 class="h2">Les bordures</h2>
      <p class="prose">Si ton tapis n’en a pas, procure-t’en : idéalement une bande autocollante en
      polyuréthane, qui agit comme une glissière et <strong>renvoie la voiture en piste au lieu de
      l’arrêter</strong>. On en trouve facilement sur les plateformes en ligne, autour de 15&nbsp;€ les 5 mètres.</p>
      <p class="prose">C’est le seul accessoire dont l’absence se paie immédiatement : sans bordure, chaque
      erreur devient un arrêt de course et une voiture à aller récupérer par terre.</p>
      </div>
    </div>
    <figure class="fig" style="max-width:1100px;margin:36px auto 0" data-reveal>
      <img src="img/photos/bordures-pu-turbo-racing.jpg" width="1500" height="386" loading="lazy" decoding="async"
           alt="Annonce d’une bordure en polyuréthane Turbo Racing de 13 mètres pour circuit RC 1/76">
      <figcaption>Exemple de bordure PU Turbo Racing, référence 760140, vendue en rouleau de 13 mètres.
      Les prix et disponibilités varient selon le vendeur.</figcaption>
    </figure>
  </div>
</section>

<section class="section">
  <div class="wrap grid g2" data-stagger>
    <div class="callout"><span class="tiny">Dans l’ADN du hobby</span>
      <h2 class="h3" style="margin-bottom:12px">Construire son circuit</h2>
      <p class="prose">Beaucoup de pilotes fabriquent le leur, et certains sont magnifiques. Un exemple
      ultra-compact : 80 × 120&nbsp;cm, un carton rigide et des bordures en polyuréthane. Il y a de quoi
      s’inspirer sur les groupes Facebook et sur YouTube.</p>
      <p style="margin-top:14px"><a class="link-arrow" href="galerie-des-circuits.html">Voir la galerie des circuits <span aria-hidden="true">→</span></a></p></div>
    <div class="callout"><span class="tiny">Pour augmenter le challenge</span>
      <h2 class="h3" style="margin-bottom:12px">Les systèmes de comptage</h2>
      <p class="prose">De l’application qui reconnaît les voitures à la caméra aux étiquettes
      <strong>NFC / RFID</strong> collées sous le châssis : le chrono transforme une soirée sympa en vraie compétition.</p>
      <p style="margin-top:14px"><a class="link-arrow" href="systemes-de-comptage.html">Les différents systèmes existants <span aria-hidden="true">→</span></a></p></div>
  </div>
</section>

""" + cta("Combien tout cela coûte-t-il vraiment ?", "ou-acheter-et-budget.html", "Le calculateur de budget"),
}


# =========================================================================== #
#  SYSTÈMES DE COMPTAGE
# =========================================================================== #
P["comptage"] = {
    "head_bg": "photos/grille-depart-carre.webp",
    "url": "systemes-de-comptage.html",
    "crumb": "Les systèmes de comptage",
    "title": "Systèmes de comptage RC — caméra et NFC/RFID",
    "desc": "Comparatif des systèmes de comptage de tours RC : application caméra sur smartphone"
            " et étiquettes NFC/RFID. Solutions et budgets indicatifs pour le 1/76.",
    "image": "photos/grille-depart-carre.jpg",
    "image_alt": "Voitures RC 1/76 alignées sur une grille de départ",
    "priority": "0.7", "changefreq": "monthly",
    "og_type": "article",
    "about": ["Comptage de tours RC", "NFC", "RFID"],
    "speakable": [".answer"],
    "body": """
<section class="page-head">
  <div class="wrap page-head-inner stack" style="--gap:20px">
    <p class="eyebrow">Matériel · chronométrage</p>
    <h1 class="h1" style="color:#fff">Les systèmes de comptage</h1>
    <p class="lead">Du téléphone posé au bord de la piste à la boucle qui identifie chaque voiture :
    le bon système est celui qui laisse les pilotes rouler, pas celui qui complique la soirée.</p>
    <ul class="facts"><li>De <b>0 €</b> à <b>200 €</b></li><li>Caméra ou <b>NFC/RFID</b></li><li>Compatible <b>1/76</b></li></ul>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="answer" style="margin-bottom:40px" data-reveal><strong>Pour découvrir la course, commence par la caméra d’un smartphone.</strong>
    Pour une piste 1/76 qui roule souvent, un système NFC à étiquette passive est le plus discret : aucun fil ni
    batterie à ajouter dans la voiture. Les transpondeurs actifs sont trop encombrants pour ces modèles : les systèmes
    de compétition professionnels sont donc surdimensionnés pour une table à la maison.</p>

    <h2 class="h2" style="margin-bottom:26px" data-reveal>Quatre façons de compter les tours</h2>
    <div class="grid g2" data-stagger>
      <article class="card"><span class="card-num">01 · SANS ÉLECTRONIQUE</span><h3>Un arbitre et un chrono</h3>
      <p>Une feuille, un téléphone et une personne qui note les passages. C’est gratuit et parfait pour tester un
      format de course. Pour suivre plusieurs pilotes à la fois, l’arbitre peut utiliser les smartphones des
      coureurs : un chrono par voiture. C’est sportif, mais ça marche.</p>
      <figure class="fig" style="max-width:250px;margin:18px auto 0"><img src="img/photos/chrono-iphone.jpg" width="618" height="495" loading="lazy" decoding="async"
      alt="iPhone affichant le chronomètre utilisé pour compter les tours manuellement"><figcaption>Un simple chronomètre suffit pour les premières manches.</figcaption></figure></article>
      <article class="card"><span class="card-num">02 · CAMÉRA</span><h3>Le smartphone reconnaît la voiture</h3>
      <p>Sur Android, <a href="https://play.google.com/store/apps/details?id=com.laptrap" target="_blank" rel="noopener">LapTrap</a>
      utilise la caméra du smartphone et des marqueurs imprimés sur les voitures. Sur iPhone, essaie
      <a href="https://apps.apple.com/us/app/rc-timing/id1092261747" target="_blank" rel="noopener">RC Timing</a>
      (reconnaissance par couleur) ou <a href="https://apps.apple.com/jp/app/mini4-lap-timer/id1280883925" target="_blank" rel="noopener">Mini4 Lap Timer</a>
      (caméra, conçu à l’origine pour les Mini 4WD). Pas de matériel de piste à acheter ; LapTrap et RC Timing
      proposent des achats intégrés, Mini4 Lap Timer est annoncé gratuit.</p>
      <figure class="fig" style="max-width:300px;margin:18px auto 0"><img src="img/photos/comptage-camera-smartphone.png" width="1536" height="1024" loading="lazy" decoding="async"
      alt="Smartphone sur trépied filmant une petite voiture RC qui passe la ligne de départ"><figcaption>Le smartphone filme et reconnaît la voiture qui lui passe devant.</figcaption></figure></article>
      <article class="card"><span class="card-num">03 · NFC / RFID</span><h3>Une étiquette passive sous la voiture</h3>
      <p>Le <a href="https://rsrc.biz/turbo-racing/8386-systeme-de-comptage-pour-micro-rc-176.html" target="_blank" rel="noopener">Mini Race Challenge</a>
      est pensé pour les micro-RC 1/76 : une fine étiquette NFC (famille RFID) collée sous le châssis et un lecteur
      sous le tapis. Le kit est vendu aux alentours de <strong>180 €</strong>, avec dix étiquettes incluses. Il est même
      possible d’ajouter en option des feux bicolores sur la ligne de départ, pour encore plus de réalisme.</p>
      <figure class="fig" style="max-width:280px;margin:18px auto 0"><img src="img/photos/mini-race-challenge-1-76.jpg" width="800" height="724" loading="lazy" decoding="async"
      alt="Kit Mini Race Challenge avec boîtier, antenne et étiquettes NFC pour micro RC"><figcaption>Le kit Mini Race Challenge, avec lecteur, antenne et étiquettes NFC.</figcaption></figure></article>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap" style="max-width:800px" data-reveal>
      <p class="eyebrow">Le conseil 1/76</p>
      <h2 class="h2">Le NFC/RFID évite d’alourdir la voiture</h2>
      <p class="prose">Sur une micro-RC, un transpondeur actif peut prendre de la place et demander une alimentation.
      Une étiquette NFC est passive : elle ne pèse presque rien et n’a rien à recharger. Le lecteur du Mini Race
      Challenge se place sous la zone de passage, avec une épaisseur de tapis limitée par le fabricant.</p>
      <p class="prose" style="margin-top:14px">À notre connaissance, il n’existe pas actuellement d’autre système
      de comptage performant, prêt à l’emploi et réellement adapté au 1/76 qui soit équivalent au Mini Race Challenge.
      Pour une première soirée, essaie la caméra ; pour une piste 1/76 régulière, c’est aujourd’hui le choix le plus cohérent.</p>
  </div>
</section>

""" + cta("Installer le comptage sur un circuit adapté", "circuits-et-tapis.html", "Voir les circuits et tapis"),
}


# =========================================================================== #
#  OÙ ACHETER & BUDGET  (outil 04)
# =========================================================================== #
P["budget"] = {
    "head_bg": "photos/tapis-turbo-racing-l.webp",
    "url": "ou-acheter-et-budget.html",
    "crumb": "Où acheter & budget",
    "title": "Budget RC 1/76 — combien coûte vraiment le RC racing sur table",
    "desc": "Calculateur de budget RC 1/76 : voiture, tapis, bordures, radio et comptage "
            "de tours, pour un pilote ou pour un club. Ticket d’entrée à partir d’environ 125 €, "
            "prix constatés en 2026.",
    "image": "photos/tapis-turbo-racing-l.jpg",
    "image_alt": "Plan d’un tapis de course Turbo Racing pour le 1/76",
    "priority": "0.9", "changefreq": "monthly",
    "tools": True,
    "og_type": "article",
    "about": ["Budget RC 1/76", "Prix Turbo Racing", "Où acheter du RC 1/76"],
    "speakable": [".answer"],
    "jsonld": [{
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": "Combien coûte le RC table car racing pour débuter ?",
             "acceptedAnswer": {"@type": "Answer", "text": "Comptez environ 125 € pour un ticket d’entrée complet : une voiture Turbo Racing C76 à environ 85 €, un tapis Turbo Racing XS à environ 25 €, et des bordures en polyuréthane autour de 15 € les 5 mètres. La radio, la batterie et le chargeur sont fournis avec la voiture."}},
            {"@type": "Question", "name": "Que faut-il vérifier avant d’acheter une RC 1/76 ?",
             "acceptedAnswer": {"@type": "Answer", "text": "Que le kit soit complet — radiocommande, batterie, chargeur, deux carrosseries — et que le modèle annoncé soit bien celui de la photo. Prévoyez quatre piles AAA, qui ne sont jamais fournies."}},
            {"@type": "Question", "name": "Quel matériel peut attendre quand on débute en RC 1/76 ?",
             "acceptedAnswer": {"@type": "Answer", "text": "La radio haut de gamme et le comptage de tours RFID. Commencez par une voiture, un tapis et des bordures : c’est déjà une vraie piste."}},
        ],
    }],
    "body": """
<section class="page-head">
  <div class="wrap page-head-inner stack" style="--gap:20px">
    <p class="eyebrow">Débuter · outil 04</p>
    <h1 class="h1" style="color:#fff">Où acheter &amp; combien ça coûte</h1>
    <p class="lead">Compose ta liste et vois le total. Les prix sont indicatifs, constatés en 2026 chez les
    revendeurs de modélisme et sur les grandes plateformes — ce site n’a aucun lien commercial avec les marques citées.</p>
    <ul class="facts"><li>Entrée <b>≈ 125 €</b></li><li>4 pilotes <b>≈ 415 €</b></li><li>Soit <b>≈ 104 € / pilote</b></li><li>Prix <b>2026</b></li></ul>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="answer" style="margin-bottom:40px" data-reveal><strong>Le ticket d’entrée est d’environ 125&nbsp;€ :</strong>
    une Turbo Racing C76 (≈&nbsp;85&nbsp;€, radio et batterie incluses), un tapis XS (≈&nbsp;25&nbsp;€) et
    des bordures PU (≈&nbsp;15&nbsp;€). Pour quatre pilotes sur un tapis L, compte plutôt
    <strong>environ 415&nbsp;€ au total</strong>, soit environ 104&nbsp;€ par personne.</p>

    <section id="budget-tool" class="tool" data-reveal>
      <div class="tool-head">
        <div><span class="tiny">Outil 04</span><h2>Le calculateur de budget</h2></div>
        <span class="tiny" style="color:#fff">Calcul local · rien n’est envoyé</span>
      </div>
      <div class="tool-body grid g-side" style="align-items:start;gap:30px">
        <div>
          <div class="field"><span class="tiny">La voiture</span>
            <div class="chips" role="group" aria-label="Choisir la voiture">
              <button type="button" class="chip" data-b="car" data-v="mini" aria-pressed="false">Turbo Racing MINI · 50 €</button>
              <button type="button" class="chip" data-b="car" data-v="c76" aria-pressed="true">Turbo Racing C76 · 85 €</button>
              <button type="button" class="chip" data-b="car" data-v="c76le" aria-pressed="false">Turbo Racing C76LE · 95 €</button>
            </div></div>
          <div class="field"><span class="tiny">Le tapis</span>
            <div class="chips" role="group" aria-label="Choisir le tapis">
              <button type="button" class="chip" data-b="mat" data-v="xs" aria-pressed="false">XS 95 × 50 · 25 €</button>
              <button type="button" class="chip" data-b="mat" data-v="m" aria-pressed="false">M 120 × 80 · 40 €</button>
              <button type="button" class="chip" data-b="mat" data-v="l" aria-pressed="true">L 160 × 90 · 60 €</button>
              <button type="button" class="chip" data-b="mat" data-v="xl" aria-pressed="false">XL 240 × 120 · 120 €</button>
              <button type="button" class="chip" data-b="mat" data-v="none" aria-pressed="false">Circuit maison · 0 €</button>
            </div></div>
          <div class="field"><span class="tiny">Les options</span>
            <div class="chips" role="group" aria-label="Options">
              <button type="button" class="chip" data-b="opt" data-v="bordures" aria-pressed="true">Bordures PU 5 m · 15 €</button>
              <button type="button" class="chip" data-b="opt" data-v="radio" aria-pressed="false">Radio P32S · 45 €</button>
              <button type="button" class="chip" data-b="opt" data-v="rfid" aria-pressed="false">Comptage RFID · 90 €</button>
            </div></div>
          <div class="field" style="margin-bottom:0"><span class="tiny">Combien de pilotes ?</span>
            <div class="chips" role="group" aria-label="Nombre de pilotes">
              <button type="button" class="chip" data-b="pilotes" data-v="1" aria-pressed="true">1</button>
              <button type="button" class="chip" data-b="pilotes" data-v="2" aria-pressed="false">2</button>
              <button type="button" class="chip" data-b="pilotes" data-v="4" aria-pressed="false">4</button>
              <button type="button" class="chip" data-b="pilotes" data-v="6" aria-pressed="false">6</button>
              <button type="button" class="chip" data-b="pilotes" data-v="8" aria-pressed="false">8</button>
            </div></div>
          <p class="tiny" style="margin-top:18px">Le tapis et le comptage sont partagés · la voiture est par pilote</p>
        </div>
        <div data-budget-out aria-live="polite"></div>
      </div>
    </section>
  </div>
</section>

<section class="section section--paper2">
  <div class="wrap grid g3" data-stagger>
    <article class="card"><span class="card-num">01</span><h2 class="h3">Où acheter</h2>
      <p>Les boutiques de modélisme en ligne francophones, les revendeurs officiels Turbo&nbsp;Racing, et les
      grandes plateformes internationales pour les accessoires (bordures PU, stickers).</p></article>
    <article class="card"><span class="card-num">02</span><h2 class="h3">Vérifier avant de payer</h2>
      <p>Que le kit soit complet — radio, batterie, chargeur, deux carrosseries — et que le modèle annoncé
      soit bien celui de la photo. Prévois quatre piles AAA, jamais fournies.</p></article>
    <article class="card"><span class="card-num">03</span><h2 class="h3">Ce qui peut attendre</h2>
      <p>La radio haut de gamme et le comptage RFID. Commence par une voiture, un tapis et des bordures :
      c’est déjà une vraie piste, et tu sauras ensuite ce qui te manque.</p></article>
  </div>
</section>

""" + cta("Le matériel est là. Reste à organiser la course.",
          "reglement-type-de-course.html", "Le règlement type"),
}


# =========================================================================== #
#  RÈGLEMENT TYPE
# =========================================================================== #
P["reglement"] = {
    "head_bg": "photos/grille-depart-carre.webp",
    "url": "reglement-type-de-course.html",
    "crumb": "Règlement type",
    "title": "Règlement type d’une course RC 1/76 — six articles prêts à copier",
    "desc": "Matériel, piste, format, classement, contacts et esprit : un règlement de course RC 1/76 "
            "en six articles, testé sur table, à copier et adapter. Plus le déroulé d’une soirée "
            "type à quatre pilotes.",
    "image": "photos/grille-depart-tapis.jpg",
    "image_alt": "Grille de départ d’une course RC 1/76",
    "priority": "0.85",
    "og_type": "article",
    "about": ["Règlement de course RC", "Organisation de course", "Classement RC"],
    "speakable": [".answer"],
    "jsonld": [{
        "@context": "https://schema.org",
        "@type": "HowTo",
        "name": "Organiser une soirée de course RC 1/76 à quatre pilotes",
        "description": "Le déroulé d’une soirée type de deux heures, du montage de la piste au podium.",
        "totalTime": "PT2H",
        "inLanguage": "fr-FR",
        "step": [
            {"@type": "HowToStep", "position": 1, "name": "0:00 — Installation", "text": "Tapis, bordures, comptage et appairage des quatre voitures."},
            {"@type": "HowToStep", "position": 2, "name": "0:20 — Essais libres", "text": "Essais libres de 10 minutes, trims réglés et limiteurs annoncés."},
            {"@type": "HowToStep", "position": 3, "name": "0:30 — Qualification 1", "text": "Qualification de 4 minutes, puis relevé des temps."},
            {"@type": "HowToStep", "position": 4, "name": "0:45 — Qualification 2", "text": "Qualification de 4 minutes. Le meilleur temps fixe la grille."},
            {"@type": "HowToStep", "position": 5, "name": "1:00 — Finale, manche 1", "text": "Première manche finale de 5 minutes."},
            {"@type": "HowToStep", "position": 6, "name": "1:15 — Finale, manche 2", "text": "Seconde manche finale de 5 minutes."},
            {"@type": "HowToStep", "position": 7, "name": "1:30 — Classement", "text": "Classement au cumul des deux manches, podium, photo et rangement."},
        ],
    }],
    "body": """
<section class="page-head">
  <div class="wrap page-head-inner stack" style="--gap:20px">
    <p class="eyebrow">Piloter · organiser</p>
    <h1 class="h1" style="color:#fff">Règlement type de course</h1>
    <p class="lead">Une base simple, testée sur table, à copier et adapter pour ta prochaine soirée.
    Objectif : que personne ne discute le classement, et que tout le monde ait envie de revenir.</p>
    <ul class="facts"><li><b>6 articles</b></li><li>Soirée <b>2 h</b></li><li><b>4 pilotes</b></li><li>Finale <b>2 × 5 min</b></li></ul>
    <p><button type="button" class="btn btn--race btn--sm" data-copy="#reglement-texte">Copier le règlement</button></p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="answer" style="margin-bottom:40px" data-reveal><strong>Le principe :</strong> un seul châssis
    autorisé pour toute l’épreuve (en pratique le TC-06), moteur et électronique d’origine, classement au
    <strong>nombre de tours d’abord</strong> puis au temps. Le pilote qui provoque un contact rend la position.</p>

    <div id="reglement-texte" class="grid g2" data-stagger>
      <article class="callout"><span class="tiny">Art. 1 · Matériel</span>
        <p class="prose" style="margin-top:8px">Un seul châssis autorisé pour toute l’épreuve, annoncé à
        l’inscription — en pratique le TC-06 (C76 / C76LE / C78). Moteur, électronique et pignons d’origine.
        Carrosserie libre, numéro obligatoire et lisible.</p></article>
      <article class="callout"><span class="tiny">Art. 2 · Piste</span>
        <p class="prose" style="margin-top:8px">Tapis tissu avec bordures sur toute la longueur, posé sur une
        surface plane et stable. Largeur minimale permettant deux voitures côte à côte. Sens de circulation
        annoncé avant la première série.</p></article>
      <article class="callout"><span class="tiny">Art. 3 · Format</span>
        <p class="prose" style="margin-top:8px">Essais libres 10 min, puis deux séries qualificatives de 4 min.
        Finale en deux manches de 5 min. Grille de départ selon le meilleur temps qualificatif.</p></article>
      <article class="callout"><span class="tiny">Art. 4 · Classement</span>
        <p class="prose" style="margin-top:8px">Nombre de tours d’abord, temps au dernier tour ensuite. Un tour
        non bouclé dans le sens de la piste n’est pas compté. Classement final par cumul des deux manches.</p></article>
      <article class="callout"><span class="tiny">Art. 5 · Contacts</span>
        <p class="prose" style="margin-top:8px">Le pilote qui provoque un contact rend la position. Voiture
        retournée : seul le commissaire la remet en piste, à l’endroit où elle s’est arrêtée. Deux fautes
        signalées : dernière position sur la série.</p></article>
      <article class="callout callout--race"><span class="tiny">Art. 6 · Esprit</span>
        <p class="prose" style="margin-top:8px">Régularité et fair-play avant la vitesse brute. Le pilote le plus
        rapide qui casse la course de deux autres ne gagne rien. Une réclamation se règle avant la série
        suivante, jamais après.</p></article>
    </div>
  </div>
</section>

<section class="section section--paper2">
  <div class="wrap grid g-side">
    <div class="stack" data-reveal="left">
      <p class="eyebrow">Soirée type · 4 pilotes</p>
      <h2 class="h2">Deux heures, du montage au podium</h2>
      <ol class="timeline" style="margin-top:18px">
        <li><span class="t">0:00</span><p>Installation : tapis, bordures, comptage et appairage des quatre voitures.</p></li>
        <li><span class="t">0:20</span><p>Essais libres · 10 min. Trims réglés et limiteurs annoncés.</p></li>
        <li><span class="t">0:30</span><p>Qualification 1 · 4 min, puis relevé des temps.</p></li>
        <li><span class="t">0:45</span><p>Qualification 2 · 4 min. La meilleure qualification fixe la grille.</p></li>
        <li><span class="t">1:00</span><p>Finale · manche 1 · 5 min.</p></li>
        <li><span class="t">1:15</span><p>Finale · manche 2 · 5 min.</p></li>
        <li><span class="t">1:30</span><p>Classement au cumul des deux manches, podium, photo et rangement.</p></li>
      </ol>
    </div>
    <figure class="fig" data-reveal="right">
      <img src="img/photos/grille-depart-carre.webp" width="941" height="706" loading="lazy" decoding="async" alt="Voitures RC 1/76 en position sur les emplacements peints de la grille de départ, ligne à damier au premier plan">
      <figcaption>La grille de départ se fait au meilleur temps qualificatif.</figcaption>
    </figure>
  </div>
</section>

""" + cta("Tu organises quelque chose ? Dis-le, ça se relaie ici.",
          "clubs-et-competitions.html", "Clubs &amp; compétitions"),
}
