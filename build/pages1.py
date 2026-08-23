# -*- coding: utf-8 -*-
"""Accueil · Débuter en 10 minutes · Le concept"""
from content import MARQUEE, statbar, cta, HERO_SVG

P = {}

# =========================================================================== #
#  ACCUEIL
# =========================================================================== #
P["index"] = {
    "head_bg": "photos/grille-depart-tapis.webp",
    "url": "index.html",
    "crumb": "Accueil",
    "title": "RC Table Racing Car — le guide du RC racing sur table à l’échelle 1/76",
    "og_title": "RC Table Racing Car · Small cars, big racing",
    "desc": "Faire courir des voitures radiocommandées de 5,8 cm sur une table : matériel, "
            "réglages, circuits, budget et règlement. Le guide francophone de l’échelle 1/76, "
            "avec comparateur Turbo Racing et calculateur de budget.",
    "image": "photos/grille-depart-tapis.jpg",
    "image_alt": "Grille de départ sur un tapis de course RC 1/76, quatre voitures alignées",
    "priority": "1.0", "changefreq": "weekly",
    "page_type": "CollectionPage",
    "speakable": [".hero h1", ".hero .lead"],
    "about": ["RC racing sur table", "Modélisme échelle 1/76", "Turbo Racing"],
    "tools": False,
    "jsonld": [{
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": "Les quatre outils interactifs de RC Table Racing Car",
        "itemListOrder": "https://schema.org/ItemListOrderAscending",
        "numberOfItems": 4,
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Comparateur des modèles Turbo Racing",
             "url": "https://rctableracingcar.fr/choisir-son-modele.html#comparateur"},
            {"@type": "ListItem", "position": 2, "name": "Quelle voiture pour moi ?",
             "url": "https://rctableracingcar.fr/choisir-son-modele.html#selecteur"},
            {"@type": "ListItem", "position": 3, "name": "La radio, bouton par bouton",
             "url": "https://rctableracingcar.fr/comprendre-la-radiocommande.html#radio-tool"},
            {"@type": "ListItem", "position": 4, "name": "Calculateur de budget",
             "url": "https://rctableracingcar.fr/ou-acheter-et-budget.html#budget-tool"},
        ],
    }],
    "body": """
<section class="hero">
  <div class="hero-bg" aria-hidden="true">
    <img src="img/photos/grille-depart-tapis.webp" width="1023" height="575" decoding="async" fetchpriority="high" alt="">
  </div>
  <div class="wrap hero-inner">
    <div class="stack" style="--gap:24px">
      <p class="eyebrow">Le guide francophone du RC racing sur table</p>
      <h1 class="h-hero">Small&nbsp;cars.<br>Big&nbsp;racing.</h1>
      <p class="lead">La précision du RC racing dans le creux de la main. Direction et accélération
      proportionnelles, pneus interchangeables, réglages fins — sur une piste qui tient sur une table.</p>
      <div class="btn-row">
        <a class="btn btn--race" href="debuter-en-10-minutes.html">Débuter en 10 min <span class="arrow" aria-hidden="true">→</span></a>
        <a class="btn btn--ghost-inv" href="choisir-son-modele.html">Comparer les modèles</a>
      </div>
    </div>
    <div class="hero-media" data-parallax="0.05">""" + HERO_SVG + """
      <span class="hero-badge">1/76 · 5,8 CM</span>
    </div>
  </div>
</section>

""" + statbar([
        ("Échelle", "1/76", ""),
        ("Longueur", '<span data-count="5,8" data-suffix="&nbsp;cm">5,8&nbsp;cm</span>', ""),
        ("Piste minimum", "95 × 50 cm", ""),
        ("Ticket d’entrée", '≈&nbsp;<span data-count="90" data-suffix="&nbsp;€">90&nbsp;€</span>', ""),
    ]) + """

""" + MARQUEE + """

<section class="section">
  <div class="wrap">
    <div class="grid g-side" data-reveal>
      <div class="stack">
        <p class="eyebrow">06 principes</p>
        <h2 class="h1">Ce n’est plus un jouet.<br>C’est du modélisme.</h2>
        <p class="answer"><strong>Le RC table car racing</strong>, c’est faire courir des voitures
        radiocommandées de 5 à 6&nbsp;cm à l’échelle&nbsp;1/76 sur un tapis tissu posé sur une table.
        Direction et accélération proportionnelles, trims, limiteur de puissance, pneus interchangeables,
        batterie LiPo rechargeable : tout l’essentiel du RC racing, réduit à un format qui se pose
        et se range en quelques secondes.</p>
      </div>
      <figure class="fig" data-reveal="right">
        <img src="img/photos/soiree-course-table.webp" width="900" height="675" loading="lazy" decoding="async" alt="Quatre pilotes debout autour d’un circuit RC 1/76 posé sur une table, radiocommandes en main">
        <figcaption>Une piste complète tient sur une table : quatre pilotes, deux heures, aucune infrastructure.</figcaption>
      </figure>
    </div>

    <div class="grid g3" style="margin-top:48px" data-stagger>
      <article class="principle" data-ghost="01"><span class="n">01 · Sur table</span>
        <h3>Tout le monde voit tout</h3>
        <p>Une piste facile à observer et à partager. Elle se pose et se range en quelques secondes.</p></article>
      <article class="principle" data-ghost="02"><span class="n">02 · Au 1/76</span>
        <h3>Une échelle commune</h3>
        <p>Compacte, comparable d’un pilote à l’autre — la seule qui tienne vraiment sur une table de salle à manger.</p></article>
      <article class="principle" data-ghost="03"><span class="n">03 · Proportionnel</span>
        <h3>Ça se dose</h3>
        <p>Direction et accélération progressives : le freinage, la corde et la relance se travaillent vraiment.</p></article>
      <article class="principle" data-ghost="04"><span class="n">04 · Proche de la série</span>
        <h3>Le budget ne classe pas</h3>
        <p>Même châssis pour tous, moteur et électronique d’origine. La différence se fait au volant.</p></article>
      <article class="principle" data-ghost="05"><span class="n">05 · Convivial</span>
        <h3>Quatre pilotes, un apéro</h3>
        <p>Des rencontres simples à organiser : une table, un tapis, deux heures.</p></article>
      <article class="principle" data-ghost="06"><span class="n">06 · Sportif</span>
        <h3>Régularité avant vitesse</h3>
        <p>Fair-play et constance. Objectif affiché : un championnat de France&nbsp;1/76.</p></article>
    </div>

    <p class="prose" style="margin-top:36px;max-width:78ch" data-reveal>L’échelle&nbsp;1/76 est le format
    le plus adapté pour organiser des courses entre amis ou de vraies compétitions sur un tapis posé sur
    une table. Les formats supérieurs — 1/64, 1/28, 1/24 — demandent un circuit au sol, donc de l’espace
    et de l’infrastructure. <a class="link-arrow" href="le-concept.html">Le concept en détail <span aria-hidden="true">→</span></a></p>
  </div>
</section>

<section class="section section--tight section--dark scale-section">
  <div class="grid g-side scale-band">
    <div class="wrap stack scale-band-txt">
      <p class="eyebrow">L’échelle, en vrai</p>
      <h2 class="h2" style="color:#fff">5,8 cm.<br>Ça tient dans la main.</h2>
      <p class="lead">C’est toute la proposition : une voiture assez petite pour qu’une piste complète
      tienne sur une table, assez sérieuse pour que le pilotage compte. Direction et gaz proportionnels,
      pneus interchangeables, réglages fins — au format d’une boîte d’allumettes.</p>
    </div>
    <img class="scale-band-img" src="img/photos/echelle-dans-la-main.webp" width="900" height="384"
         loading="lazy" decoding="async"
         alt="Voiture radiocommandée à l’échelle 1/76 posée dans le creux d’une main, qui montre ses 5,8 cm de long">
  </div>
</section>

<section class="section section--paper2">
  <div class="wrap">
    <p class="eyebrow" data-reveal>Parcours</p>
    <h2 class="h1" style="margin:12px 0 36px" data-reveal>Deux façons d’entrer</h2>
    <div class="grid g2" data-stagger>
      <article class="card">
        <span class="card-num">Je n’ai jamais touché une RC</span>
        <h3 class="h3">Le parcours découverte</h3>
        <p>Ce qu’il y a dans la boîte, comment charger, comment allumer, comment ne pas casser sa
        transmission le premier soir. En dix minutes, tu roules droit.</p>
        <ul style="margin-top:8px;display:grid;gap:9px">
          <li style="list-style:none"><a class="link-arrow" href="debuter-en-10-minutes.html">Débuter en 10 minutes</a></li>
          <li style="list-style:none"><a class="link-arrow" href="ou-acheter-et-budget.html">Combien ça coûte vraiment</a></li>
          <li style="list-style:none"><a class="link-arrow" href="glossaire.html">Glossaire : ESC, trim, D/R…</a></li>
        </ul>
      </article>
      <article class="card">
        <span class="card-num">Je fais déjà du RC</span>
        <h3 class="h3">Le parcours modéliste</h3>
        <p>Ce que change l’échelle : inertie quasi nulle, grip du tissu, trims critiques, poussière
        comme premier ennemi. Et ce qui reste identique au 1/12.</p>
        <ul style="margin-top:8px;display:grid;gap:9px">
          <li style="list-style:none"><a class="link-arrow" href="reglages-et-pilotage.html">Réglages &amp; pilotage</a></li>
          <li style="list-style:none"><a class="link-arrow" href="guide-turbo-racing-c76.html">Le châssis TC-06 en détail</a></li>
          <li style="list-style:none"><a class="link-arrow" href="reglement-type-de-course.html">Règlement type de course</a></li>
        </ul>
      </article>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="eyebrow" data-reveal>Interactif</p>
    <h2 class="h1" style="margin:12px 0 8px" data-reveal>Les quatre outils du site</h2>
    <p class="lead" style="margin-bottom:36px" data-reveal>Tout est calculé dans ton navigateur. Aucune donnée n’est envoyée.</p>
    <div class="grid g4" data-stagger>
      <a class="card card--link" href="choisir-son-modele.html#comparateur">
        <span class="card-num">Outil 01</span><h3 class="h4">Le comparateur Turbo Racing</h3>
        <p>Onze modèles, trois générations de châssis, filtrés par usage. Ce qui se vaut, ce qui se dépasse.</p></a>
      <a class="card card--link" href="choisir-son-modele.html#selecteur">
        <span class="card-num">Outil 02</span><h3 class="h4">Quelle voiture pour moi&nbsp;?</h3>
        <p>Trois questions — surface, budget, drift ou chrono — et une recommandation argumentée.</p></a>
      <a class="card card--link" href="comprendre-la-radiocommande.html#radio-tool">
        <span class="card-num">Outil 03</span><h3 class="h4">La radio, bouton par bouton</h3>
        <p>Clique un réglage sur le schéma : ce qu’il fait, quand y toucher, quand ne pas y toucher.</p></a>
      <a class="card card--link" href="ou-acheter-et-budget.html#budget-tool">
        <span class="card-num">Outil 04</span><h3 class="h4">Le calculateur de budget</h3>
        <p>Voiture, tapis, bordures, batteries, comptage de tours. Pour un pilote ou pour un club.</p></a>
    </div>
  </div>
</section>

<section class="section section--dark">
  <div class="wrap grid g-side">
    <div class="stack" data-reveal="left">
      <p class="eyebrow">L’ambition</p>
      <h2 class="h1">Faire du 1/76 une vraie catégorie de compétition</h2>
      <p class="lead">Le 1/8, le 1/10, le 1/12 et le 1/24 ont leurs championnats. Le 1/76 a tout ce
      qu’il faut : matériel homogène, règles simples, et l’énorme avantage de se pratiquer chez soi.
      Transmettons cette passion — je rêve déjà d’un championnat de France&nbsp;1/76.</p>
      <div class="btn-row">
        <a class="btn btn--race" href="clubs-et-competitions.html">Rejoindre la communauté <span class="arrow" aria-hidden="true">→</span></a>
        <a class="btn btn--ghost-inv" href="reglement-type-de-course.html">Le règlement type</a>
      </div>
    </div>
    <figure class="fig" style="border-color:var(--ink-3);background:var(--ink-2)" data-reveal="right">
      <img src="img/photos/grille-depart-carre.webp" width="941" height="706" loading="lazy" decoding="async" alt="Grille de départ sur tapis de course RC 1/76 : une MINI, un coupé orange et deux buggys alignés">
      <figcaption style="background:var(--ink-2);border-color:var(--ink-3);color:#a3aab2">Grille de départ, quatre pilotes : le format le plus courant d’une soirée.</figcaption>
    </figure>
  </div>
</section>
""",
}


# =========================================================================== #
#  DÉBUTER EN 10 MINUTES
# =========================================================================== #
P["debuter"] = {
    "head_bg": "photos/c76-avant-large.webp",
    "url": "debuter-en-10-minutes.html",
    "crumb": "Débuter en 10 minutes",
    "title": "Débuter en RC 1/76 en 10 minutes — les 4 étapes du premier soir",
    "desc": "Charger, allumer dans le bon ordre, régler les trims, rouler au limiteur 20 % : "
            "le guide pas à pas du premier soir en RC table car racing, et les cinq erreurs "
            "qui cassent une transmission.",
    "image": "photos/c76-avant.jpg",
    "image_alt": "Avant d’une Turbo Racing C76 orange à l’échelle 1/76",
    "priority": "0.9", "changefreq": "monthly",
    "og_type": "article",
    "about": ["Débuter en RC", "Batterie LiPo", "Trim de direction", "Limiteur TH.LIM"],
    "speakable": [".answer"],
    "jsonld": [{
        "@context": "https://schema.org",
        "@type": "HowTo",
        "name": "Débuter en RC table car racing 1/76 en 10 minutes",
        "description": "Les quatre étapes à suivre dans l’ordre pour une première session réussie "
                       "avec une voiture radiocommandée à l’échelle 1/76.",
        "totalTime": "PT10M",
        "inLanguage": "fr-FR",
        "estimatedCost": {"@type": "MonetaryAmount", "currency": "EUR", "value": "90"},
        "supply": [
            {"@type": "HowToSupply", "name": "4 piles AAA pour la radiocommande"},
            {"@type": "HowToSupply", "name": "Un tapis tissu ou une surface non glissante"},
            {"@type": "HowToSupply", "name": "Une table plane"},
        ],
        "tool": [{"@type": "HowToTool", "name": "Une pincette"},
                 {"@type": "HowToTool", "name": "Le trombone d’appairage fourni"}],
        "step": [
            {"@type": "HowToStep", "position": 1, "name": "Charge sans improviser",
             "text": "Interrupteur de la voiture sur OFF, batterie branchée au chargeur. Quand la LED rouge s’éteint, c’est chargé. Charger interrupteur sur ON chauffe l’électronique pour rien et raccourcit la vie de la batterie."},
            {"@type": "HowToStep", "position": 2, "name": "Allume dans le bon ordre",
             "text": "La radio d’abord, la voiture ensuite. À l’extinction, l’inverse : la voiture d’abord, la radio en dernier. C’est la règle de sécurité de tout le RC : une voiture allumée sans radio peut partir seule."},
            {"@type": "HowToStep", "position": 3, "name": "Pose-la bien droite, puis règle le trim",
             "text": "Voiture au sol, volant au neutre. Corrige avec ST.TRIM jusqu’à ce qu’elle roule droit sans que tu touches au volant. Si elle avance seule à l’arrêt, ajuste TH.TRIM pour retrouver la vitesse zéro."},
            {"@type": "HowToStep", "position": 4, "name": "Roule, limiteur sur 20 %",
             "text": "TH.LIM sur 20 % pour les premiers tours, 50 % quand tu enchaînes proprement, 100 % quand la piste ne te surprend plus. Batterie vide : laisse refroidir, puis recharge cinq minutes."},
        ],
    }],
    "body": """
<section class="page-head">
  <div class="wrap page-head-inner stack" style="--gap:20px">
    <p class="eyebrow">Parcours découverte · étape 01</p>
    <h1 class="h1" style="color:#fff">Débuter en 10 minutes</h1>
    <p class="lead">Le kit contient tout, sauf quatre piles AAA pour la radio. Suis ces quatre étapes
    dans l’ordre : c’est ce qui sépare une première soirée réussie d’une transmission bloquée.</p>
    <ul class="facts"><li>Durée <b>10 min</b></li><li>Limiteur <b>TH.LIM 20 %</b></li><li>À prévoir <b>4 piles AAA</b></li><li>Charge <b>USB-C · ≈ 5 min</b></li></ul>
    <p class="tiny" style="color:var(--race-light);border:1px solid var(--ink-3);padding:14px 18px;display:block;max-width:max-content">
      À prévoir avant · 4 piles AAA · une table plane · un tapis ou une surface non glissante · une pincette</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="answer" style="margin-bottom:40px" data-reveal><strong>En résumé :</strong> charge la batterie
    interrupteur sur OFF, allume la radio avant la voiture, règle ST.TRIM pour qu’elle roule droite, puis
    roule avec le limiteur TH.LIM sur 20 %. Ces quatre gestes suffisent pour une première session sans casse.</p>

    <ol class="steps" data-stagger>
      <li class="step"><span class="step-n" aria-hidden="true">01</span>
        <div><h2 class="h3">Charge sans improviser</h2>
        <p>Interrupteur de la voiture sur <strong>OFF</strong>, batterie branchée au chargeur.
        Quand la LED rouge s’éteint, c’est chargé.</p>
        <p class="note">Charger interrupteur sur ON chauffe l’électronique pour rien et raccourcit la vie de la batterie.</p></div></li>
      <li class="step"><span class="step-n" aria-hidden="true">02</span>
        <div><h2 class="h3">Allume dans le bon ordre</h2>
        <p>La <strong>radio d’abord</strong>, la voiture ensuite. À l’extinction, l’inverse : la voiture
        d’abord, la radio en dernier.</p>
        <p class="note">C’est la règle de sécurité de tout le RC. Une voiture allumée sans radio peut partir seule.</p></div></li>
      <li class="step"><span class="step-n" aria-hidden="true">03</span>
        <div><h2 class="h3">Pose-la bien droite, puis règle le trim</h2>
        <p>Voiture au sol, volant au neutre. Corrige avec <strong>ST.TRIM</strong> jusqu’à ce qu’elle
        roule droit sans que tu touches au volant.</p>
        <p class="note">Si elle avance seule à l’arrêt, ajuste TH.TRIM pour retrouver la vitesse zéro.</p></div></li>
      <li class="step"><span class="step-n" aria-hidden="true">04</span>
        <div><h2 class="h3">Roule — limiteur sur 20 %</h2>
        <p><strong>TH.LIM sur 20 %</strong> pour les premiers tours, 50 % quand tu enchaînes proprement,
        100 % quand la piste ne te surprend plus.</p>
        <p class="note">Batterie vide : laisse refroidir, puis recharge cinq minutes. C’est ce qui la fait durer une saison.</p></div></li>
    </ol>
  </div>
</section>

<section class="section section--paper2">
  <div class="wrap">
    <p class="eyebrow" data-reveal>Le kit</p>
    <h2 class="h2" style="margin:12px 0 32px" data-reveal>Dans la boîte</h2>
    <div class="grid g3" data-stagger>
      <div class="card card--flat"><span class="card-num">RTR</span><h3 class="h4">La voiture montée</h3><p>Prête à rouler à la sortie de la boîte, carrosserie posée et batterie fournie.</p></div>
      <div class="card card--flat"><span class="card-num">4 × AAA</span><h3 class="h4">La radiocommande</h3><p>Séparable en deux pour tenir dans un sac. Les piles ne sont jamais fournies.</p></div>
      <div class="card card--flat"><span class="card-num">20–30 min</span><h3 class="h4">Batterie LiPo + chargeur USB</h3><p>20 à 30 minutes d’autonomie selon l’usage, 20 minutes de charge.</p></div>
      <div class="card card--flat"><span class="card-num">× 2</span><h3 class="h4">Deux carrosseries vierges</h3><p>À peindre : c’est l’invitation à se différencier sans toucher à la mécanique.</p></div>
      <div class="card card--flat"><span class="card-num">Kit</span><h3 class="h4">Outils et pièces d’usure</h3><p>Plus le gros trombone qui sert à refaire l’appairage radio-voiture.</p></div>
      <div class="card card--flat" style="border-color:var(--race);background:var(--race-wash)"><span class="card-num">À acheter</span><h3 class="h4">Ce qui manque</h3><p>Quatre piles AAA, et un tapis avec bordures si tu veux vraiment rouler vite.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="eyebrow" data-reveal>À éviter</p>
    <h2 class="h2" style="margin:12px 0 28px" data-reveal>Les cinq erreurs du premier soir</h2>
    <ul class="warn-list" data-stagger>
      <li><span class="x" aria-hidden="true">01</span><div><b>Rouler sur la moquette.</b><span>Les poils s’enroulent autour des axes en quelques secondes.</span></div></li>
      <li><span class="x" aria-hidden="true">02</span><div><b>Piloter à 100 % tout de suite.</b><span>Le limiteur existe pour ça, sers-t’en.</span></div></li>
      <li><span class="x" aria-hidden="true">03</span><div><b>Ignorer les cheveux dans la transmission.</b><span>Une pincette, dix secondes, à chaque batterie.</span></div></li>
      <li><span class="x" aria-hidden="true">04</span><div><b>Recharger une batterie brûlante.</b><span>Laisse-la revenir à température.</span></div></li>
      <li><span class="x" aria-hidden="true">05</span><div><b>Toucher au bouton REV.</b><span>Il n’y a jamais de raison. Vraiment jamais.</span></div></li>
    </ul>
  </div>
</section>

""" + cta("Prochaine étape : choisir la voiture qui te correspond.",
          "choisir-son-modele.html", "Étape 02 · choisir son modèle"),
}


# =========================================================================== #
#  LE CONCEPT
# =========================================================================== #
P["concept"] = {
    "head_bg": "photos/soiree-course-large.webp",
    "url": "le-concept.html",
    "crumb": "Le concept",
    "title": "Le concept du RC Table Racing Car — la discipline du 1/76 expliquée",
    "desc": "Des voitures RC de 5 à 6 cm à l’échelle 1/76, une piste surélevée, six principes : "
            "ce qui définit le RC table car racing et pourquoi cette échelle peut devenir "
            "une vraie catégorie de compétition.",
    "image": "photos/soiree-course-table.jpg",
    "image_alt": "Quatre pilotes autour d’un circuit RC 1/76 posé sur une table",
    "priority": "0.8",
    "og_type": "article",
    "about": ["RC table car racing", "Échelle 1/76", "Compétition RC"],
    "speakable": [".answer"],
    "jsonld": [{
        "@context": "https://schema.org",
        "@type": "DefinedTerm",
        "name": "RC table car racing",
        "inDefinedTermSet": "https://rctableracingcar.fr/glossaire.html",
        "description": "Discipline de modélisme consistant à faire courir des voitures radiocommandées "
                       "de 5 à 6 cm à l’échelle 1/76 sur un tapis tissu posé sur une table, avec "
                       "direction et accélération proportionnelles et un matériel proche de la série.",
    }],
    "body": """
<section class="page-head">
  <div class="wrap page-head-inner stack" style="--gap:20px">
    <p class="eyebrow">La discipline</p>
    <h1 class="h1" style="color:#fff">Le concept RC&nbsp;Table&nbsp;Car&nbsp;Racing</h1>
    <p class="lead">Un cadre simple : des mini véhicules très performants de 5 à 6&nbsp;cm à
    l’échelle&nbsp;1/76, et une piste surélevée pour que les pilotes s’affrontent le plus simplement possible.</p>
    <ul class="facts"><li>Échelle <b>1/76</b></li><li>Voiture <b>5,8 cm</b></li><li>Piste dès <b>95 × 50 cm</b></li><li>Entrée <b>≈ 90 €</b></li></ul>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="answer" style="margin-bottom:44px" data-reveal><strong>Définition —</strong> le
    <strong>RC table car racing</strong> est une discipline de modélisme qui consiste à faire courir des
    voitures radiocommandées à l’échelle&nbsp;1/76 (5 à 6&nbsp;cm de long) sur un tapis tissu posé sur une
    table. Elle se distingue par trois choses : la direction et l’accélération sont <em>proportionnelles</em>,
    le matériel reste <em>proche de la série</em>, et la piste se monte et se range en quelques minutes.</p>

    <div class="grid g3" data-stagger>
      <article class="principle" data-ghost="01"><span class="n">01 · Sur table</span><h2 class="h4">Tout le monde voit tout, tout le temps</h2><p>Une piste facile à observer et à partager, à hauteur des yeux.</p></article>
      <article class="principle" data-ghost="02"><span class="n">02 · Au 1/76</span><h2 class="h4">Une échelle commune et compacte</h2><p>Elle rend le matériel comparable d’un pilote à l’autre.</p></article>
      <article class="principle" data-ghost="03"><span class="n">03 · Proportionnel</span><h2 class="h4">Direction et accélération progressives</h2><p>Ce n’est pas du tout-ou-rien : ça se dose.</p></article>
      <article class="principle" data-ghost="04"><span class="n">04 · Proche de la série</span><h2 class="h4">Le budget ne décide pas du classement</h2><p>On roule tous avec la même base mécanique.</p></article>
      <article class="principle" data-ghost="05"><span class="n">05 · Convivial</span><h2 class="h4">Des rencontres simples à organiser</h2><p>Chez soi, entre amis ou entre collègues.</p></article>
      <article class="principle" data-ghost="06"><span class="n">06 · Sportif</span><h2 class="h4">Régularité et fair-play</h2><p>Le plus rapide n’est pas toujours devant.</p></article>
    </div>
  </div>
</section>

<section class="section section--paper2">
  <div class="wrap grid g-side">
    <figure class="fig" data-reveal="left">
      <img src="img/photos/gamme-c71-c75.webp" width="1024" height="860" loading="lazy" decoding="async" alt="Six modèles Turbo Racing 1/76 photographiés en studio et légendés C71, C72, C73, C74 et C75">
      <figcaption>Six générations de carrosseries, de la C71 à la C75. Seule la famille racing sert à courser.</figcaption>
    </figure>
    <div class="stack" data-reveal="right">
      <p class="eyebrow">Pourquoi ce site existe</p>
      <h2 class="h2">Le 1/76 a tout ce qu’il faut pour devenir une catégorie de compétition</h2>
      <p class="prose">Le 1/8, le 1/10, le 1/12 et le 1/24 sont des échelles très populaires, avec leurs
      championnats. Le 1/76 offre le même socle technique — matériel homogène, règles simples, pilotage
      exigeant — avec l’énorme avantage de se pratiquer chez soi, et pour une fraction du budget.</p>
      <p class="prose">Transmettons cette passion : je rêve déjà d’un championnat de France&nbsp;1/76.
      <strong>Vive le RC table car racing.</strong></p>
      <p><a class="link-arrow" href="reglement-type-de-course.html">Voir le règlement type de course <span aria-hidden="true">→</span></a></p>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <h2 class="h2" style="margin-bottom:26px" data-reveal>Le 1/76 face aux autres échelles</h2>
    <div class="table-wrap" data-reveal>
      <table class="data">
        <caption>Comparaison des échelles RC courantes · ce qu’elles demandent comme espace</caption>
        <thead><tr><th scope="col">Échelle</th><th scope="col">Longueur type</th><th scope="col">Surface nécessaire</th><th scope="col">Se pratique</th></tr></thead>
        <tbody>
          <tr class="is-star"><th scope="row">1/76</th><td>5 à 6 cm</td><td>Dès 95 × 50 cm</td><td>Sur une table, chez soi</td></tr>
          <tr><th scope="row">1/64</th><td>≈ 7 cm</td><td>Environ 3 × 2 m</td><td>Au sol, pièce dédiée</td></tr>
          <tr><th scope="row">1/24</th><td>≈ 18 cm</td><td>Piste dédiée</td><td>Club, infrastructure</td></tr>
          <tr><th scope="row">1/12</th><td>≈ 36 cm</td><td>Piste indoor dédiée</td><td>Club, compétition</td></tr>
          <tr><th scope="row">1/10</th><td>≈ 45 cm</td><td>Piste extérieure ou hall</td><td>Club, championnats</td></tr>
          <tr><th scope="row">1/8</th><td>≈ 50 cm</td><td>Grande piste extérieure</td><td>Club, compétition</td></tr>
        </tbody>
      </table>
    </div>
    <p class="tiny" style="margin-top:14px">Ordres de grandeur indicatifs · du 1/12 au 1/8, ces formats populaires demandent une piste dédiée. L’intérêt du 1/76 est de ne demander aucune infrastructure.</p>
  </div>
</section>

<section class="section section--paper2">
  <div class="wrap">
    <figure class="fig" style="max-width:900px;margin:0 auto" data-reveal>
      <img src="img/photos/echelles-1-8-a-1-76.jpg" width="800" height="442" loading="lazy" decoding="async"
           alt="Comparaison de taille entre plusieurs voitures radiocommandées, d’un grand buggy 1/8 à une très petite voiture 1/76">
      <figcaption><strong>Du 1/8 au 1/76, la différence est immédiate.</strong> À droite, la voiture 1/76 tient
      presque dans la paume de la main : c’est ce qui permet de rouler sur une table plutôt que sur une piste dédiée.</figcaption>
    </figure>
  </div>
</section>

""" + cta("Prêt à choisir ta première voiture ?", "choisir-son-modele.html", "Le comparateur"),
}
