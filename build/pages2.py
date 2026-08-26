# -*- coding: utf-8 -*-
"""Choisir son modèle · Guide C76 · Radiocommande · Réglages & pilotage"""
from content import statbar, cta

P = {}

# =========================================================================== #
#  CHOISIR SON MODÈLE  (outils 01 & 02)
# =========================================================================== #
P["modeles"] = {
    "head_bg": "photos/gamme-c71-c75.webp",
    "url": "choisir-son-modele.html",
    "crumb": "Choisir son modèle",
    "title": "Choisir son modèle Turbo Racing 1/76 — comparateur des 11 voitures",
    "desc": "Comparateur filtrable des modèles Turbo Racing 1/76 : MINI, C61-C66 drift, C71 à C78, "
            "C82. Châssis, usage, prix 2026 et notre lecture de chaque modèle, plus un sélecteur "
            "en trois questions.",
    "image": "photos/gamme-c71-c75.jpg",
    "image_alt": "Les modèles Turbo Racing C71 à C75 alignés",
    "priority": "0.9", "changefreq": "monthly",
    "tools": True,
    "og_type": "article",
    "about": ["Turbo Racing C76", "Châssis TC-06", "Comparatif voitures RC 1/76"],
    "speakable": [".answer"],
    "jsonld": [{
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": "Comparatif des modèles Turbo Racing à l’échelle 1/76",
        "description": "Onze modèles Turbo Racing classés par génération de châssis et par usage, "
                       "avec prix indicatifs constatés en 2026.",
        "numberOfItems": 11,
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "item": {"@type": "Product", "name": "Turbo Racing MINI", "category": "Découverte", "description": "Rassurante et peu rapide, idéale pour apprendre les commandes sans casser.", "brand": {"@type": "Brand", "name": "Turbo Racing"}, "offers": {"@type": "AggregateOffer", "priceCurrency": "EUR", "lowPrice": "35", "availability": "https://schema.org/InStock"}}},
            {"@type": "ListItem", "position": 2, "item": {"@type": "Product", "name": "Turbo Racing C61 à C66", "category": "Drift", "description": "Pneus métalliques, dérive volontaire et contre-braquage. Spectaculaire, mais pas fait pour le chrono.", "brand": {"@type": "Brand", "name": "Turbo Racing"}, "offers": {"@type": "AggregateOffer", "priceCurrency": "EUR", "lowPrice": "45", "availability": "https://schema.org/InStock"}}},
            {"@type": "ListItem", "position": 3, "item": {"@type": "Product", "name": "Turbo Racing C71", "category": "Racing loisir", "description": "Première génération de châssis. Agréable en loisir, dépassée en course.", "brand": {"@type": "Brand", "name": "Turbo Racing"}, "offers": {"@type": "AggregateOffer", "priceCurrency": "EUR", "lowPrice": "45", "availability": "https://schema.org/InStock"}}},
            {"@type": "ListItem", "position": 4, "item": {"@type": "Product", "name": "Turbo Racing C74", "category": "Racing loisir", "description": "Fin de la génération v1. Bon compromis d’occasion.", "brand": {"@type": "Brand", "name": "Turbo Racing"}, "offers": {"@type": "AggregateOffer", "priceCurrency": "EUR", "lowPrice": "48", "availability": "https://schema.org/InStock"}}},
            {"@type": "ListItem", "position": 5, "item": {"@type": "Product", "name": "Turbo Racing C75", "category": "Racing", "description": "Châssis v2, plus rapide que la v1, mais moins précise à piloter.", "brand": {"@type": "Brand", "name": "Turbo Racing"}, "offers": {"@type": "AggregateOffer", "priceCurrency": "EUR", "lowPrice": "55", "availability": "https://schema.org/InStock"}}},
            {"@type": "ListItem", "position": 6, "item": {"@type": "Product", "name": "Turbo Racing C76", "category": "Référence racing", "description": "Châssis TC-06. Le meilleur rapport précision-vitesse-prix de la gamme, base de comparaison du site.", "brand": {"@type": "Brand", "name": "Turbo Racing"}, "offers": {"@type": "AggregateOffer", "priceCurrency": "EUR", "lowPrice": "85", "availability": "https://schema.org/InStock"}}},
            {"@type": "ListItem", "position": 7, "item": {"@type": "Product", "name": "Turbo Racing C76LE", "category": "Racing", "description": "Identique à la C76, carrosserie plus détaillée.", "brand": {"@type": "Brand", "name": "Turbo Racing"}, "offers": {"@type": "AggregateOffer", "priceCurrency": "EUR", "lowPrice": "95", "availability": "https://schema.org/InStock"}}},
            {"@type": "ListItem", "position": 8, "item": {"@type": "Product", "name": "Turbo Racing C78", "category": "Racing", "description": "Même châssis TC-06 que la C76, carrosserie plus détaillée et prix plus élevé.", "brand": {"@type": "Brand", "name": "Turbo Racing"}, "offers": {"@type": "AggregateOffer", "priceCurrency": "EUR", "lowPrice": "100", "availability": "https://schema.org/InStock"}}},
            {"@type": "ListItem", "position": 9, "item": {"@type": "Product", "name": "Turbo Racing C82", "category": "Fun", "description": "Hors gabarit pour la catégorie, mais parfaite comme pace car.", "brand": {"@type": "Brand", "name": "Turbo Racing"}, "offers": {"@type": "AggregateOffer", "priceCurrency": "EUR", "lowPrice": "65", "availability": "https://schema.org/InStock"}}},
        ],
    }],
    "body": """
<section class="page-head">
  <div class="wrap page-head-inner stack" style="--gap:20px">
    <p class="eyebrow">Matériel · outils 01 &amp; 02</p>
    <h1 class="h1" style="color:#fff">Choisir le bon modèle</h1>
    <p class="lead">Drift, loisir ou compétition. À ce jour, seule la marque Turbo&nbsp;Racing propose des
    modèles&nbsp;1/76 assez fiables et performants pour courser sérieusement. Voici comment ils se situent
    les uns par rapport aux autres.</p>
    <ul class="facts"><li><b>11 modèles</b> comparés</li><li><b>3 générations</b> de châssis</li><li>De <b>50 à 100 €</b></li><li>Référence <b>C76</b></li></ul>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="answer" style="margin-bottom:40px" data-reveal><strong>La réponse courte :</strong> prends une
    <strong>Turbo Racing C76</strong> (châssis TC-06, ≈&nbsp;85&nbsp;€). Les C76LE et C78 partagent la même
    mécanique pour 10 à 15&nbsp;€ de plus — la seule différence est la carrosserie. La MINI (≈&nbsp;50&nbsp;€)
    convient pour découvrir, et la famille C61-C66 est une famille <em>drift</em>, à ne pas mélanger avec le racing.</p>

    <section id="comparateur" class="tool" data-reveal>
      <div class="tool-head">
        <div><span class="tiny">Outil 01</span><h2>Le comparateur Turbo Racing</h2></div>
        <span class="tiny" style="color:#fff"><span data-compare-count>11</span> modèles affichés</span>
      </div>
      <div class="tool-body">
        <div class="field">
          <span class="tiny">Filtrer par usage</span>
          <div class="chips" role="group" aria-label="Filtrer les modèles par usage">
            <button type="button" class="chip" data-filter="tous" aria-pressed="true">Tous</button>
            <button type="button" class="chip" data-filter="racing" aria-pressed="false">Racing</button>
            <button type="button" class="chip" data-filter="drift" aria-pressed="false">Drift</button>
            <button type="button" class="chip" data-filter="decouverte" aria-pressed="false">Découverte</button>
            <button type="button" class="chip" data-filter="fun" aria-pressed="false">Fun</button>
          </div>
        </div>
        <div class="table-wrap">
          <table class="data">
            <caption>Prix indicatifs constatés en 2026 · kit complet radio + batterie + chargeur</caption>
            <thead><tr><th scope="col">Modèle</th><th scope="col">Châssis</th><th scope="col">Usage</th><th scope="col">Prix</th><th scope="col">Notre lecture</th></tr></thead>
            <tbody>
              <tr class="is-star"><th scope="row">C76<span class="star-tag">★</span></th><td>TC-06 · v3</td><td>Référence</td><td>≈ 85 €</td><td>La meilleure : précision et vitesse au prix le plus juste.</td></tr>
            </tbody>
          </table>
        </div>
        <noscript><p class="tiny" style="margin-top:14px">Le filtre nécessite JavaScript. Le tableau complet reste consultable sur la <a href="glossaire.html">page glossaire</a>.</p></noscript>
      </div>
    </section>
  </div>
</section>

<section class="section section--paper2">
  <div class="wrap">
    <section id="selecteur" class="tool" data-reveal>
      <div class="tool-head">
        <div><span class="tiny">Outil 02</span><h2>Quelle voiture pour moi&nbsp;?</h2></div>
        <span class="tiny" style="color:#fff">Aucune donnée envoyée</span>
      </div>
      <div class="tool-body grid g2" style="align-items:start">
        <div>
          <div class="field">
            <span class="tiny">01 · Quelle surface as-tu ?</span>
            <div class="chips" role="group" aria-label="Quelle surface as-tu ?">
              <button type="button" class="chip" data-q="q1" data-v="petite" aria-pressed="false">Un coin de table (≈ 1 m)</button>
              <button type="button" class="chip" data-q="q1" data-v="moyenne" aria-pressed="false">Une grande table (1,6 m)</button>
              <button type="button" class="chip" data-q="q1" data-v="grande" aria-pressed="false">Une pièce entière (2,4 m)</button>
            </div>
          </div>
          <div class="field">
            <span class="tiny">02 · Quel budget ?</span>
            <div class="chips" role="group" aria-label="Quel budget ?">
              <button type="button" class="chip" data-q="q2" data-v="mini" aria-pressed="false">Le minimum, pour essayer</button>
              <button type="button" class="chip" data-q="q2" data-v="juste" aria-pressed="false">Le bon rapport, une fois</button>
              <button type="button" class="chip" data-q="q2" data-v="libre" aria-pressed="false">Je veux le meilleur</button>
            </div>
          </div>
          <div class="field" style="margin-bottom:0">
            <span class="tiny">03 · Ce qui t’attire ?</span>
            <div class="chips" role="group" aria-label="Ce qui t’attire ?">
              <button type="button" class="chip" data-q="q3" data-v="chrono" aria-pressed="false">Le chrono et la trajectoire</button>
              <button type="button" class="chip" data-q="q3" data-v="drift" aria-pressed="false">La glisse et le style</button>
              <button type="button" class="chip" data-q="q3" data-v="both" aria-pressed="false">Rouler entre amis, sans chrono</button>
            </div>
          </div>
        </div>
        <div data-reco-out aria-live="polite"></div>
      </div>
    </section>
  </div>
</section>

<section class="section section--paper2" style="padding-top:0">
  <div class="wrap">
    <p class="eyebrow" data-reveal>Les deux familles à ne pas confondre</p>
    <h2 class="h2" style="margin:12px 0 28px" data-reveal>Drift ou racing&nbsp;?</h2>
    <div class="grid g2" data-stagger>
      <figure class="fig">
        <img src="img/photos/c66-drift.webp" width="1114" height="547" loading="lazy" decoding="async"
             alt="Turbo Racing C66 verte vue de profil : berline de drift à l’échelle 1/76 avec aileron, jantes larges et bas de caisse">
        <figcaption><strong>La famille drift (C61 à C66).</strong> Pneus durs, arrière qui décroche
        volontairement, contre-braquage permanent. Spectaculaire — et inutilisable au chrono.</figcaption>
      </figure>
      <figure class="fig">
        <img src="img/photos/c78-rallye.webp" width="900" height="689" loading="lazy" decoding="async"
             alt="Turbo Racing C78 blanche et rouge en livrée rallye, vue de trois quarts avant">
        <figcaption><strong>La C78.</strong> Même châssis TC-06 que la C76, carrosserie plus détaillée,
        16&nbsp;€ de plus. Belle, mais sans avantage en course.</figcaption>
      </figure>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap grid g-side">
    <div class="stack" data-reveal="left">
      <p class="eyebrow">Notre étalon</p>
      <h2 class="h2">Pourquoi la C76 devient la référence</h2>
      <p class="prose">Son comportement prévisible et son niveau de performance en font une base convaincante
      pour opposer des pilotes à matériel comparable — et à un prix inférieur aux modèles plus récents qui
      partagent la même mécanique.</p>
      <p class="prose">Les C61 à C66 restent une famille drift à part : pneus métalliques, dérive volontaire,
      contre-braquage. Ludique et spectaculaire, mais pas fait pour le chrono, et à ne pas mélanger avec
      le racing sur le même tapis.</p>
      <p><a class="btn btn--race" href="guide-turbo-racing-c76.html">Le guide complet du C76 <span class="arrow" aria-hidden="true">→</span></a></p>
    </div>
    <figure class="fig" data-reveal="right">
      <img src="img/photos/carrosseries-led.webp" width="1000" height="589" loading="lazy" decoding="async" alt="Trois carrosseries RC 1/76 côte à côte, phares et bandeaux LED allumés sous le châssis">
      <figcaption>Même châssis pour tous, livrées différentes : c’est le pacte de la catégorie.</figcaption>
    </figure>
  </div>
</section>

""" + cta("Une fois la voiture choisie : la radio, bouton par bouton.",
          "comprendre-la-radiocommande.html", "Comprendre la radio"),
}


# =========================================================================== #
#  GUIDE C76
# =========================================================================== #
P["c76"] = {
    "head_bg": "photos/c76-avant-large.webp",
    "url": "guide-turbo-racing-c76.html",
    "crumb": "Guide du C76",
    "title": "Turbo Racing C76 — guide complet du châssis TC-06 à l’échelle 1/76",
    "desc": "Fiche de référence du Turbo Racing C76 : châssis TC-06, 5,8 cm, 20 à 30 minutes "
            "d’autonomie selon l’usage, ≈ 85 €. Routine de session, points de vigilance direction, "
            "transmission et pneus.",
    "image": "photos/c76-avant.jpg",
    "image_alt": "Turbo Racing C76 orange vue de trois quarts avant",
    "priority": "0.9",
    "og_type": "article",
    "about": ["Turbo Racing C76", "Châssis TC-06", "Entretien RC 1/76"],
    "speakable": [".answer"],
    "jsonld": [{
        "@context": "https://schema.org",
        "@type": "Product",
        "name": "Turbo Racing C76",
        "description": "Voiture radiocommandée à l’échelle 1/76 sur châssis TC-06, longueur 5,8 cm, "
                       "autonomie de 20 à 30 minutes selon l’usage. Modèle de référence du RC table car racing.",
        "brand": {"@type": "Brand", "name": "Turbo Racing"},
        "category": "Voiture radiocommandée échelle 1/76",
        "image": "https://rctableracingcar.fr/img/chassis-annote.png",
        "additionalProperty": [
            {"@type": "PropertyValue", "name": "Châssis", "value": "TC-06 (3e génération)"},
            {"@type": "PropertyValue", "name": "Échelle", "value": "1/76"},
            {"@type": "PropertyValue", "name": "Longueur", "value": "5,8 cm"},
            {"@type": "PropertyValue", "name": "Empattement réglable", "value": "33,5 à 34,5 mm"},
            {"@type": "PropertyValue", "name": "Transmission", "value": "Propulsion (2 roues motrices)"},
            {"@type": "PropertyValue", "name": "Moteur", "value": "Coreless 1020, environ 42 000 tr/min"},
            {"@type": "PropertyValue", "name": "Modes de puissance", "value": "20 %, 50 %, 100 % (TH.LIM)"},
            {"@type": "PropertyValue", "name": "Batterie", "value": "LiPo 3,7 V 55 mAh"},
            {"@type": "PropertyValue", "name": "Charge", "value": "USB-C, environ 20 minutes pour une charge complète"},
            {"@type": "PropertyValue", "name": "Autonomie", "value": "20 à 30 minutes selon l’usage"},
            {"@type": "PropertyValue", "name": "Radiocommande", "value": "2,4 GHz, direction et gaz proportionnels"},
            {"@type": "PropertyValue", "name": "Éclairage", "value": "LED avant et arrière"},
            {"@type": "PropertyValue", "name": "Vitesse annoncée", "value": "environ 6 km/h"},
            {"@type": "PropertyValue", "name": "Type", "value": "RTR (Ready To Run)"},
        ],
        "offers": {"@type": "AggregateOffer", "priceCurrency": "EUR", "lowPrice": "85",
                   "highPrice": "100", "offerCount": "3",
                   "availability": "https://schema.org/InStock"},
    }],
    "body": """
<section class="page-head">
  <div class="wrap page-head-inner stack" style="--gap:20px">
    <p class="eyebrow">Matériel · fiche de référence</p>
    <h1 class="h1" style="color:#fff">Guide complet du Turbo&nbsp;Racing&nbsp;C76</h1>
    <p class="lead">Le châssis TC-06 est le meilleur que Turbo&nbsp;Racing propose aujourd’hui. Trois modèles
    le partagent : C76, C76LE et C78. Autant prendre la moins chère — pour une course équitable entre amis,
    mieux vaut le même châssis pour tous, quitte à se différencier à la peinture.</p>
    <ul class="facts">
      <li>Châssis <b>TC-06 v3</b></li><li>Moteur <b>coreless 1020</b></li>
      <li>Batterie <b>LiPo 3,7 V · 55 mAh</b></li><li>Charge <b>USB-C</b></li>
      <li>Puissance <b>20 / 50 / 100 %</b></li>
    </ul>
  </div>
</section>

""" + statbar([
        ("Châssis", "TC-06 · v3", ""),
        ("Longueur", "5,8 cm", ""),
        ("Autonomie", "20-30 min", ""),
        ("Prix constaté", '≈&nbsp;<span data-count="85" data-suffix="&nbsp;€">85&nbsp;€</span>', ""),
    ]) + """

<section class="section">
  <div class="wrap">
    <p class="answer" style="margin-bottom:40px" data-reveal><strong>Pourquoi la C76 plutôt qu’une autre :</strong>
    la C76, la C76LE et la C78 utilisent exactement le même châssis TC-06 et la même mécanique. Seule la
    carrosserie change. La C76 est la moins chère des trois (≈&nbsp;85&nbsp;€ contre 95 et 100&nbsp;€) :
    à performance identique, c’est le choix rationnel — et le bon choix pour que tous les pilotes d’une
    même course roulent à armes égales.</p>

    <figure class="fig exploded" style="margin-bottom:44px" data-reveal="scale">
      <div class="canvas">
        <img src="img/photos/chassis-vue-eclatee.webp" width="768" height="792" loading="lazy" decoding="async" alt="Vue éclatée d’une Turbo Racing 1/76 : carrosserie, vis, carte électronique, coque supérieure, arbres de transmission, train arrière, ressort, ensemble de direction et coque inférieure">
        <span class="xl" style="--x:80.3%;--y:9.0%">Carrosserie</span>
        <span class="xl" style="--x:80.3%;--y:17.8%">Vis</span>
        <span class="xl" style="--x:80.3%;--y:25.9%">Carte électronique</span>
        <span class="xl" style="--x:80.3%;--y:34.0%">Coque supérieure</span>
        <span class="xl" style="--x:74.3%;--y:42.4%">Transmission · 2<sup>e</sup> étage</span>
        <span class="xl" style="--x:74.3%;--y:50.6%">Transmission · 1<sup>er</sup> étage</span>
        <span class="xl" style="--x:77.7%;--y:58.5%">Train arrière</span>
        <span class="xl" style="--x:79.7%;--y:66.8%">Coque inférieure</span>
        <span class="xl" style="--x:8.1%;--y:40.5%">Vis sans tête</span>
        <span class="xl" style="--x:16.1%;--y:55.4%">Ressort</span>
        <span class="xl" style="--x:12.6%;--y:66.8%">Ensemble direction</span>
      </div>
      <figcaption>Vue éclatée du constructeur, <strong>légendes traduites en français</strong> : carrosserie, carte électronique, transmission à deux étages, train arrière, direction et coque. Les trois zones à surveiller en usage sont la direction, la transmission et les pneus.</figcaption>
    </figure>

    <div class="grid g-side" style="margin-bottom:48px;align-items:start">
      <div class="stack" data-reveal="left">
        <p class="eyebrow">Fiche technique</p>
        <h2 class="h2">Ce qu’il y a vraiment dedans</h2>
        <p class="prose">Les chiffres constructeur, rassemblés au même endroit. Un seul mérite une
        précision : l’autonomie varie avec le niveau de puissance et le style de conduite.
        <strong>Compte entre 20 et 30 minutes selon l’usage</strong>, selon le niveau de puissance et le style de conduite.</p>
        <p class="tiny">Sources : fiches revendeurs et documentation Turbo Racing, relevées en 2026.</p>
      </div>
      <dl class="specs" data-reveal="right">
        <div><dt>Échelle</dt><dd>1/76</dd></div>
        <div><dt>Longueur</dt><dd>5,8 cm</dd></div>
        <div><dt>Châssis</dt><dd>TC-06 · v3</dd></div>
        <div><dt>Empattement</dt><dd>33,5–34,5 mm</dd></div>
        <div><dt>Transmission</dt><dd>Propulsion</dd></div>
        <div><dt>Moteur</dt><dd>Coreless 1020</dd></div>
        <div><dt>Régime</dt><dd>≈ 42 000 tr/min</dd></div>
        <div><dt>Puissance</dt><dd>20 / 50 / 100 %</dd></div>
        <div><dt>Batterie</dt><dd>LiPo 3,7 V · 55 mAh</dd></div>
        <div><dt>Charge</dt><dd>USB-C · ≈ 20 min</dd></div>
        <div><dt>Autonomie</dt><dd>20–30 min selon l’usage</dd></div>
        <div><dt>Vitesse</dt><dd>≈ 6 km/h</dd></div>
        <div><dt>Radio</dt><dd>2,4 GHz proportionnelle</dd></div>
        <div><dt>Éclairage</dt><dd>LED avant / arrière</dd></div>
        <div><dt>Livraison</dt><dd>RTR, prêt à rouler</dd></div>
        <div><dt>Prix constaté</dt><dd>≈ 85 €</dd></div>
      </dl>
    </div>

    <div class="grid g2" style="margin-bottom:48px" data-stagger>
      <figure class="fig exploded" style="max-width:520px">
        <div class="canvas">
          <img src="img/photos/chassis-electronique.webp" width="618" height="900" loading="lazy" decoding="async"
               alt="Vue éclatée de la partie électrique d’un châssis RC 1/76 : carte électronique, moteur de propulsion, moteur de direction, ressort et emplacements de montage dans la coque">
          <span class="xl" style="--x:5.3%;--y:50.1%">Moteur de propulsion</span>
          <span class="xl" style="--x:5.3%;--y:55.7%">Moteur de direction</span>
          <span class="xl" style="--x:23.9%;--y:68.8%">Logement du ressort</span>
          <span class="xl" style="--x:12.6%;--y:75.1%">Logement moteur de direction</span>
          <span class="xl" style="--x:12.6%;--y:80.4%">Logement moteur de propulsion</span>
          <span class="xl" style="--x:12.6%;--y:86.2%">Transmission · 1<sup>er</sup> étage</span>
          <span class="xl" style="--x:12.6%;--y:91.8%">Transmission · 2<sup>e</sup> étage</span>
        </div>
        <figcaption>La partie électrique, <strong>légendes traduites</strong> : une seule carte, un moteur de
        propulsion, un moteur de direction. Les nombres à six chiffres sont les références de pièces
        détachées du constructeur. Rien de tout cela ne se modifie — c’est le principe de la catégorie.</figcaption>
      </figure>
      <figure class="fig">
        <img src="img/photos/chassis-eclairage-led.webp" width="900" height="802" loading="lazy" decoding="async"
             alt="Châssis RC 1/76 transparent montrant la batterie, la carte électronique et trois plaques de guidage lumineux bleue, rouge et jaune">
        <figcaption>Les plaques de guidage lumineux se changent sans outil : la couleur de l’éclairage de
        châssis se choisit en dix secondes. La batterie est soudée, mais reste facilement accessible si elle doit
        être remplacée : on trouve des LiPo <strong>12 × 15 × 4 mm</strong> (référence <strong>041215</strong>) sur AliExpress
        pour quelques euros. Savoir manier un fer à souder est toutefois recommandé. <span class="tiny">(Visuel du constructeur.)</span></figcaption>
      </figure>
    </div>

    <h2 class="h2" style="margin-bottom:26px" data-reveal>La routine d’une session propre</h2>
    <div class="grid g4" data-stagger>
      <div class="card card--flat"><span class="card-num">01 · Charge</span><h3 class="h4">Interrupteur sur OFF</h3><p>Et quand la LED rouge s’éteint, c’est chargé.</p></div>
      <div class="card card--flat"><span class="card-num">02 · Allumage</span><h3 class="h4">Radio d’abord</h3><p>Voiture ensuite. Extinction dans l’ordre inverse.</p></div>
      <div class="card card--flat"><span class="card-num">03 · Trim</span><h3 class="h4">Voiture bien droite</h3><p>ST.TRIM ajusté pour qu’elle roule droit toute seule.</p></div>
      <div class="card card--flat"><span class="card-num">04 · Range</span><h3 class="h4">Batterie vide</h3><p>Laisse refroidir, puis recharge juste 5 minutes pour la préserver.</p></div>
    </div>
  </div>
</section>

<section class="section section--paper2">
  <div class="wrap">
    <p class="eyebrow" data-reveal>Diagnostic</p>
    <h2 class="h2" style="margin:12px 0 30px" data-reveal>Les trois points de vigilance</h2>
    <div class="grid g3" data-stagger>
      <article class="card"><span class="card-num">01</span><h3 class="h3">Direction</h3>
        <p>Un trim correct centre les roues sans forcer la mécanique. Si tu dois pousser le trim à fond,
        quelque chose est de travers : vérifie la biellette avant de compenser à la radio.</p></article>
      <article class="card"><span class="card-num">02</span><h3 class="h3">Transmission</h3>
        <p>Cheveux et poussières sont ses premiers ennemis. Retire-les à la pincette après chaque batterie :
        c’est trente secondes, et c’est la première cause de perte de vitesse.</p></article>
      <article class="card"><span class="card-num">03</span><h3 class="h3">Pneus</h3>
        <p>Propreté et mécanique libre comptent plus qu’une modification radicale. Un coup de chiffon humide
        sur la gomme redonne plus de grip que n’importe quel produit miracle.</p></article>
    </div>

    <div class="callout callout--race" style="margin-top:40px" data-reveal>
      <span class="tiny">Les trois modèles du châssis TC-06</span>
      <div class="table-wrap" style="margin-top:16px;border:0">
        <table class="data">
          <thead><tr><th scope="col">Modèle</th><th scope="col">Châssis</th><th scope="col">Prix</th><th scope="col">Différence réelle</th></tr></thead>
          <tbody>
            <tr class="is-star"><th scope="row">C76</th><td>TC-06</td><td>≈ 85 €</td><td>Aucune, c’est la base — et la moins chère</td></tr>
            <tr><th scope="row">C76LE</th><td>TC-06</td><td>≈ 95 €</td><td>Carrosserie plus détaillée uniquement</td></tr>
            <tr><th scope="row">C78</th><td>TC-06</td><td>≈ 100 €</td><td>Carrosserie plus détaillée uniquement</td></tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</section>

""" + cta("La technique de pilotage, maintenant.", "reglages-et-pilotage.html", "Réglages &amp; pilotage"),
}


# =========================================================================== #
#  RADIOCOMMANDE  (outil 03)
# =========================================================================== #
P["radio"] = {
    "head_bg": "photos/radio-annotee.webp",
    "url": "comprendre-la-radiocommande.html",
    "crumb": "Radiocommande",
    "title": "Comprendre la radiocommande RC 1/76 — les 11 commandes expliquées",
    "desc": "Volant, gâchette, ST.TRIM, TH.TRIM, dual rate, TH.LIM, REV, appairage : chaque commande "
            "de la radio 1/76 expliquée, avec un schéma cliquable et trois réglages de départ "
            "selon le niveau.",
    "image": "photos/radio-annotee.jpg",
    "image_alt": "Face arrière de la radiocommande RC 1/76 avec ses réglages annotés",
    "priority": "0.85",
    "tools": True,
    "og_type": "article",
    "about": ["Radiocommande RC", "Trim", "Dual rate", "Limiteur de puissance"],
    "speakable": [".answer"],
    "jsonld": [{
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": "À quoi sert le réglage TH.LIM sur une radio RC 1/76 ?",
             "acceptedAnswer": {"@type": "Answer", "text": "TH.LIM limite la puissance globale du moteur sur trois crans : 20 %, 50 % et 100 %. C’est le réglage d’apprentissage par excellence, et l’égalisateur idéal entre pilotes de niveaux différents."}},
            {"@type": "Question", "name": "Que faire si la voiture ne répond plus à la radio ?",
             "acceptedAnswer": {"@type": "Answer", "text": "L’appairage est perdu. Appuie sur les deux petits contacteurs sous le véhicule avec le gros trombone livré dans la boîte, puis éteins et rallume la radio. Un témoin fixe signifie que la liaison est établie, un témoin clignotant qu’elle cherche encore."}},
            {"@type": "Question", "name": "Faut-il utiliser le bouton REV ?",
             "acceptedAnswer": {"@type": "Answer", "text": "Non. REV inverse le sens d’une voie. Si la voiture recule quand vous accélérez, la cause est presque toujours ailleurs. Ce bouton n’a pas de raison d’être touché en usage normal."}},
        ],
    }],
    "body": """
<section class="page-head">
  <div class="wrap page-head-inner stack" style="--gap:20px">
    <p class="eyebrow">Matériel · outil 03</p>
    <h1 class="h1" style="color:#fff">Comprendre la radiocommande</h1>
    <p class="lead">La radio des 1/76 est astucieusement séparable en deux pour prendre moins de place dans
    le sac. Clique un réglage sur le schéma : ce qu’il fait, quand y toucher, et quand surtout ne pas y toucher.</p>
    <ul class="facts"><li><b>11 commandes</b></li><li>Fréquence <b>2,4 GHz</b></li><li>Radio <b>séparable en 2</b></li><li>Réglage clé <b>TH.LIM</b></li></ul>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="answer" style="margin-bottom:40px" data-reveal><strong>Les trois commandes qui comptent vraiment :</strong>
    <strong>ST.TRIM</strong> pour que la voiture roule droit, <strong>TH.TRIM</strong> pour qu’elle ne
    bouge pas à l’arrêt, et <strong>TH.LIM</strong> pour choisir la puissance (20 %, 50 % ou 100 %).
    Le reste s’ajuste rarement — et le bouton <strong>REV</strong> ne se touche jamais.</p>

    <section id="radio-tool" class="tool" data-reveal>
      <div class="tool-head">
        <div><span class="tiny">Outil 03</span><h2>La radio, bouton par bouton</h2></div>
        <span class="tiny" style="color:#fff">11 commandes</span>
      </div>
      <div class="tool-body grid g-side" style="align-items:start;gap:28px">
        <div class="radio-map" data-radio-map>
          <img src="img/radio-schema.svg" width="900" height="620" loading="lazy" decoding="async"
               alt="Radiocommande RC à poignée pistolet et volant, vue de trois quarts arrière : volant de direction à gauche, gâchette des gaz sur la poignée, écran central, molettes ST-D/R, ST-TRM, TH-TRM et TH-D/R, limiteur TH.LIM, inverseur ST-REV, boutons CH3 et CH4, interrupteur et témoin lumineux">
        </div>
        <div>
          <div class="radio-detail" data-radio-detail aria-live="polite"></div>
          <div class="chips" data-radio-list style="margin-top:18px" role="group" aria-label="Choisir une commande"></div>
        </div>
      </div>
    </section>
  </div>
</section>

<section class="section section--paper2">
  <div class="wrap">
    <figure class="fig" style="margin-bottom:44px" data-reveal="scale">
      <img src="img/photos/radio-annotee.webp" width="1000" height="616" loading="lazy" decoding="async"
           alt="Face arrière de la radiocommande RC 1/76 annotée en français : limitation de puissance TH.LIM 20/50/100, inverseur de direction ST-REV, TH-TRM pour le ralenti, ST-TRM pour l’axe de direction, ST-D/R, interrupteur ON, charge et OFF, boutons CH3 éclairage châssis et CH4 phares">
      <figcaption>La face arrière de la radio d’origine, réglage par réglage. Les deux seuls qu’on touche
      à chaque session sont ST-TRM (rouler droit) et TH-TRM (vitesse zéro). L’inverseur ST-REV ne sert jamais.</figcaption>
    </figure>

    <p class="eyebrow" data-reveal>Réglage de départ</p>
    <h2 class="h2" style="margin:12px 0 30px" data-reveal>Trois réglages selon ton niveau</h2>
    <div class="grid g3" data-stagger>
      <article class="card"><span class="card-num">Débutant</span><h3 class="h3">TH.LIM 20 %</h3>
        <p>Direction et puissance réduites, le temps d’apprendre les commandes et de finir un tour sans toucher les bordures.</p></article>
      <article class="card" style="border-color:var(--race)"><span class="card-num">Loisir</span><h3 class="h3">TH.LIM 50 %</h3>
        <p>Direction moyenne, puissance progressive, tours réguliers. Le meilleur réglage pour rouler à plusieurs sans carambolage.</p></article>
      <article class="card"><span class="card-num">Course</span><h3 class="h3">TH.LIM 100 %</h3>
        <p>Pleine puissance, si elle est maîtrisée. À ce niveau, le frein compte plus que l’accélérateur.</p></article>
    </div>

    <div class="grid g2" style="margin-top:40px" data-stagger>
      <div class="callout"><span class="tiny">Perdu la liaison ?</span>
        <p class="prose">Appuie sur les deux petits contacteurs sous le véhicule avec le gros trombone livré
        dans la boîte. Éteins puis rallume la radio : la connexion revient. Un témoin fixe signifie que la
        liaison est établie, un témoin clignotant qu’elle cherche encore.</p></div>
      <div class="callout"><span class="tiny">Monter en gamme</span>
        <p class="prose">La radio d’origine peut être remplacée par un modèle plus évolué. La <strong>P32S</strong>
        ajoute l’exponentiel de direction et la gestion multi-modèles. L’<strong>A82</strong> propose la même
        chose dans un boîtier plus grand, avec un meilleur écran. Utile dès que tu pilotes plusieurs voitures.</p></div>
    </div>

    <div class="grid g2" style="margin-top:24px" data-stagger>
      <figure class="fig">
        <img src="img/photos/radio-p32s.webp" width="913" height="1024" loading="lazy" decoding="async"
             alt="Radiocommande Turbo Racing P32-S noire à quatre voies avec son écran LCD et son récepteur">
        <figcaption>La P32-S : quatre voies, écran LCD, exponentiel de direction et mémoire multi-modèles.</figcaption>
      </figure>
      <figure class="fig">
        <img src="img/photos/radio-a82s.webp" width="1000" height="977" loading="lazy" decoding="async"
             alt="Radiocommande Turbo Racing A82-S à sept voies avec écran, volant et récepteur">
        <figcaption>L’A82-S : sept voies, boîtier plus grand, meilleur écran. Visuel du constructeur.</figcaption>
      </figure>
    </div>
  </div>
</section>

""" + cta("Ces réglages ne servent à rien sans le geste. La suite :",
          "reglages-et-pilotage.html", "Les 4 gestes qui comptent"),
}


# =========================================================================== #
#  RÉGLAGES & PILOTAGE
# =========================================================================== #
P["pilotage"] = {
    "head_bg": "photos/grille-depart-tapis.webp",
    "url": "reglages-et-pilotage.html",
    "crumb": "Réglages & pilotage",
    "title": "Réglages et pilotage RC 1/76 — les 4 gestes qui font le chrono",
    "desc": "Freiner avant de tourner, viser la sortie, doser au bout des doigts, être régulier : "
            "la technique de pilotage en 1/76, plus un tableau de diagnostic des six symptômes "
            "les plus courants.",
    "image": "photos/grille-depart-tapis.jpg",
    "image_alt": "Voitures RC 1/76 en piste sur un tapis de course",
    "priority": "0.85",
    "og_type": "article",
    "about": ["Pilotage RC", "Trajectoire de course", "Survirage", "Diagnostic RC"],
    "speakable": [".answer"],
    "jsonld": [{
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": "Pourquoi ma voiture RC 1/76 tire-t-elle d’un côté ?",
             "acceptedAnswer": {"@type": "Answer", "text": "Vérifiez dans cet ordre : le ST.TRIM, puis la biellette de direction, puis un pneu encrassé d’un seul côté."}},
            {"@type": "Question", "name": "Pourquoi ma voiture RC avance-t-elle seule à l’arrêt ?",
             "acceptedAnswer": {"@type": "Answer", "text": "Le TH.TRIM est mal centré. Recalez le neutre des gaz, radio allumée et voiture posée au sol."}},
            {"@type": "Question", "name": "Pourquoi ma voiture RC 1/76 a-t-elle perdu sa vitesse de pointe ?",
             "acceptedAnswer": {"@type": "Answer", "text": "Trois causes, dans l’ordre de probabilité : des cheveux ou de la poussière dans la transmission, une batterie fatiguée, des pneus polis. Neuf fois sur dix, c’est la transmission."}},
            {"@type": "Question", "name": "Pourquoi ma voiture survire à la relance ?",
             "acceptedAnswer": {"@type": "Answer", "text": "Baissez le TH.LIM d’un cran et nettoyez les pneus arrière. Le tissu poussiéreux glisse plus qu’on ne croit."}},
            {"@type": "Question", "name": "Pourquoi l’avant décroche en entrée de virage ?",
             "acceptedAnswer": {"@type": "Answer", "text": "Vous freinez en braquant. Séparez les deux gestes, puis réduisez le ST.D/R pour vous obliger à moins braquer."}},
        ],
    }],
    "body": """
<section class="page-head">
  <div class="wrap page-head-inner stack" style="--gap:20px">
    <p class="eyebrow">Piloter · technique</p>
    <h1 class="h1" style="color:#fff">Réglages &amp; pilotage</h1>
    <p class="lead">À cette échelle, l’inertie est quasi nulle et le grip vient du tissu. Résultat : ce n’est
    pas la puissance qui fait le chrono, c’est la propreté du geste. Voici ce qui fait vraiment gagner du temps.</p>
    <ul class="facts"><li><b>4 gestes</b> à travailler</li><li><b>6 symptômes</b> diagnostiqués</li><li>Exercice <b>10 tours à 50 %</b></li></ul>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="answer" style="margin-bottom:40px" data-reveal><strong>Le principe central :</strong> en 1/76,
    une voiture de 5,8&nbsp;cm n’a aucune masse pour rattraper une glissade. Il faut donc <strong>séparer les
    gestes</strong> — freiner en ligne droite, puis tourner — et corriger au bout des doigts plutôt qu’au
    grand mouvement. La régularité bat la vitesse brute à presque tous les coups.</p>

    <div class="grid g-side" style="margin-bottom:48px">
      <figure class="fig" data-reveal="left">
        <img src="img/trajectoire.png" width="1400" height="900" loading="lazy" decoding="async"
             alt="Comparaison de deux trajectoires dans un virage : trajectoire idéale large-corde-large contre trajectoire à la corde">
        <figcaption>Entrer large, serrer au point de corde, ressortir large : c’est la relance qui fait le tour.</figcaption>
      </figure>
      <div class="stack" data-reveal="right">
        <p class="eyebrow">04 gestes</p>
        <h2 class="h2">Les quatre gestes qui comptent</h2>
        <p class="prose">Aucun ne demande de matériel, aucun ne coûte un euro. Ce sont les quatre seules
        choses à travailler pendant les premières semaines.</p>
      </div>
    </div>

    <ol class="steps" data-stagger>
      <li class="step"><span class="step-n" aria-hidden="true">01</span>
        <div><h2 class="h3">Freiner avant de tourner</h2>
        <p>Pousse la gâchette en ligne droite, relâche, puis tourne. Freiner et braquer en même temps fait
        décrocher l’avant : à 5&nbsp;cm de long, il n’y a aucune masse pour rattraper la glissade.</p></div></li>
      <li class="step"><span class="step-n" aria-hidden="true">02</span>
        <div><h2 class="h3">Viser la sortie, pas la corde</h2>
        <p>Entre large, serre au point de corde, ressors large. Sur un tapis étroit, le pilote qui colle la
        corde à l’entrée perd systématiquement la relance.</p></div></li>
      <li class="step"><span class="step-n" aria-hidden="true">03</span>
        <div><h2 class="h3">Doser au bout des doigts</h2>
        <p>Quelques degrés de volant suffisent. Le réflexe le plus coûteux du débutant est le grand geste de
        correction, qui provoque le tête-à-queue qu’il essayait d’éviter.</p></div></li>
      <li class="step"><span class="step-n" aria-hidden="true">04</span>
        <div><h2 class="h3">Être régulier, pas rapide</h2>
        <p>Dix tours propres battent trois tours héroïques et deux sorties de piste. En course, le classement
        se joue presque toujours sur le nombre de fautes.</p></div></li>
    </ol>
  </div>
</section>

<section class="section section--paper2">
  <div class="wrap">
    <p class="eyebrow" data-reveal>Dépannage</p>
    <h2 class="h2" style="margin:12px 0 26px" data-reveal>Ma voiture fait ça, pourquoi&nbsp;?</h2>
    <div class="table-wrap" data-reveal>
      <table class="data">
        <caption>Les six symptômes les plus courants et l’ordre dans lequel les vérifier</caption>
        <thead><tr><th scope="col">Symptôme</th><th scope="col">Ce qu’il faut vérifier, dans cet ordre</th></tr></thead>
        <tbody>
          <tr><th scope="row">Elle tire d’un côté</th><td>ST.TRIM, puis la biellette de direction, puis un pneu encrassé d’un seul côté.</td></tr>
          <tr><th scope="row">Elle avance seule à l’arrêt</th><td>TH.TRIM mal centré. Recale le neutre des gaz, radio allumée et voiture au sol.</td></tr>
          <tr><th scope="row">Elle a perdu sa vitesse</th><td>Cheveux ou poussière dans la transmission, batterie fatiguée, pneus polis. Dans cet ordre : neuf fois sur dix, c’est le premier.</td></tr>
          <tr><th scope="row">Elle survire à la relance</th><td>Baisse TH.LIM d’un cran et nettoie les pneus arrière. Le tissu poussiéreux glisse plus qu’on ne croit.</td></tr>
          <tr><th scope="row">Elle décroche à l’avant</th><td>Tu freines en braquant. Sépare les deux gestes, puis réduis ST.D/R pour t’obliger à moins braquer.</td></tr>
          <tr><th scope="row">Elle ne répond plus</th><td>Appairage perdu : deux contacteurs sous le châssis avec le trombone, puis redémarre la radio.</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section class="section section--dark">
  <div class="wrap" data-reveal>
    <p class="eyebrow">L’exercice qui progresse le plus vite</p>
    <h2 class="h1" style="margin:14px 0 20px;max-width:20ch">Dix tours, limiteur à 50 %, sans toucher une bordure</h2>
    <p class="lead">Tant que tu ne réussis pas, ne monte pas la puissance. C’est frustrant deux soirées, puis
    tout se débloque : tes trajectoires deviennent lisibles, tu anticipes, et le passage à 100 % ne te
    surprend plus. La plupart des pilotes rapides du 1/76 ont fait exactement ça.</p>
    <p style="margin-top:24px"><a class="btn btn--race" href="entretien-et-personnalisation.html">Entretien &amp; personnalisation <span class="arrow" aria-hidden="true">→</span></a></p>
  </div>
</section>
""",
}
