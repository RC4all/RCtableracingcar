/* ==========================================================================
   RC TABLE CAR RACING — les 4 outils interactifs
   01 Comparateur Turbo Racing · 02 Sélecteur « quelle voiture pour moi ? »
   03 Schéma de radiocommande     · 04 Calculateur de budget
   Aucune donnée n'est envoyée : tout est calculé dans le navigateur.
   ========================================================================== */
(function () {
  'use strict';

  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  var REFERENCES = window.RC_REFERENCE;
  if (!REFERENCES) return;
  var MODELS = REFERENCES.models;

  // top / left en % : coordonnées calées sur img/radio-schema.svg (viewBox 900 × 620)
  var RADIO = [
    { key: 'volant',   label: 'Volant',       title: 'Volant de direction',            tag: 'PILOTAGE',   top: 40.3, left: 18.4, text: 'Direction proportionnelle : quelques degrés suffisent pour tourner. À cette échelle, un geste ample fait décrocher l’avant. Travaille au bout des doigts.' },
    { key: 'gachette', label: 'Gâchette',     title: 'Gâchette des gaz',               tag: 'PILOTAGE',   top: 68.4, left: 36.7, text: 'Tirer = accélération, pousser = frein, pousser une deuxième fois = marche arrière. Le frein est ta première source de temps gagné.' },
    { key: 'sttrim',   label: 'ST-TRM',       title: 'ST-TRM · trim de direction',     tag: 'RÉGLAGE',    top: 48.1, left: 50.2, text: 'Recentre la direction pour rouler droit. Un trim correct centre les roues sans forcer la mécanique. À vérifier à chaque session.' },
    { key: 'thtrim',   label: 'TH-TRM',       title: 'TH-TRM · trim des gaz',          tag: 'RÉGLAGE',    top: 48.1, left: 58.0, text: 'Ajuste le neutre des gaz pour trouver la vitesse zéro. Si la voiture avance seule au repos, c’est ici que ça se règle.' },
    { key: 'stdr',     label: 'ST-D/R',       title: 'ST-D/R · dual rate direction',   tag: 'RÉGLAGE',    top: 48.1, left: 42.4, text: 'Limite la course maximale de direction à droite et à gauche. Baisse-le pour un pilotage plus doux sur piste étroite.' },
    { key: 'thdr',     label: 'TH-D/R',       title: 'TH-D/R · dual rate gaz',         tag: 'RÉGLAGE',    top: 48.1, left: 65.8, text: 'Limite la puissance d’accélération. En pratique, préfère le limiteur TH.LIM, plus lisible et plus reproductible.' },
    { key: 'thlim',    label: 'TH.LIM',       title: 'TH.LIM · limiteur de puissance', tag: 'CLÉ',        top: 24.2, left: 32.8, text: 'Limite la puissance globale sur trois crans : 20 %, 50 %, 100 %. C’est LE réglage d’apprentissage — et l’égalisateur idéal entre pilotes de niveaux différents.' },
    { key: 'rev',      label: 'ST-REV',       title: 'ST-REV · inversion de voie',     tag: 'À ÉVITER',   top: 20.5, left: 72.3, text: 'Inverse le sens d’une voie. À ne pas utiliser : si ta voiture recule quand tu accélères, c’est presque toujours autre chose.' },
    { key: 'ch3',      label: 'CH3 / CH4',    title: 'CH3 et CH4 · éclairages',        tag: 'CONFORT',    top: 38.4, left: 72.3, text: 'CH3 active l’éclairage sous le châssis, CH4 les phares. Aucun effet sur la performance, beaucoup d’effet sur les photos.' },
    { key: 'switch',   label: 'Interrupteur', title: 'Interrupteur d’alimentation',    tag: 'SÉCURITÉ',   top: 54.2, left: 72.0, text: 'Allume la radio AVANT le véhicule, et éteins-la APRÈS le véhicule. Toujours. C’est la règle qui évite les emballements.' },
    { key: 'led',      label: 'Témoin',       title: 'Indicateur lumineux',            tag: 'DIAGNOSTIC', top: 38.4, left: 36.7, text: 'État de l’alimentation et aide à l’appairage avec le véhicule. Fixe = lié, clignotant = en recherche.' }
  ];

  var MATS = REFERENCES.budget.mats;
  var CARS = REFERENCES.budget.cars;
  var OPTIONS = REFERENCES.budget.options;

  /* ================== OUTIL 01 — Comparateur de modèles ================== */
  function initComparator() {
    var root = $('#comparateur');
    if (!root) return;
    var tbody = $('tbody', root);
    var count = $('[data-compare-count]', root);
    var filter = 'tous';

    function render() {
      var rows = MODELS.filter(function (m) { return filter === 'tous' || m.cat === filter; });
      tbody.innerHTML = rows.map(function (m) {
        return '<tr class="' + (m.star ? 'is-star' : '') + '">' +
          '<td><img class="model-thumb" src="img/' + m.thumb + '"' + (m.thumbPos ? ' style="object-position:' + m.thumbPos + '"' : '') + ' alt="" loading="lazy" decoding="async"></td>' +
          '<th scope="row">' + m.id + (m.star ? '<span class="star-tag" title="Notre référence">★</span>' : '') + '</th>' +
          '<td>' + m.chassis + '</td>' +
          '<td>' + m.usage + '</td>' +
          '<td>≈ ' + m.prix + ' €</td>' +
          '<td>' + m.note + '</td>' +
        '</tr>';
      }).join('');
      if (count) count.textContent = rows.length;
    }

    $$('.chip', root).forEach(function (chip) {
      chip.addEventListener('click', function () {
        filter = chip.getAttribute('data-filter');
        $$('.chip', root).forEach(function (c) { c.setAttribute('aria-pressed', String(c === chip)); });
        render();
      });
    });
    render();
  }

  /* ============= OUTIL 02 — Quelle voiture pour moi ? (3 questions) ======= */
  function reco(q1, q2, q3) {
    if (!q1 || !q2 || !q3) return null;
    if (q3 === 'drift') return {
      titre: 'Turbo Racing C64 ou C66',
      sous: 'Famille drift · pneus métalliques',
      texte: 'Tu veux de la glisse, pas du chrono : la famille C6x est faite pour ça. Prends-en deux, le drift se joue à plusieurs ou pas du tout. Sache que le drift ne se mélange pas avec le racing sur le même tapis.',
      tapis: q1 === 'petite' ? 'Turbo Racing XS (95 × 50 cm)' : 'Turbo Racing M (120 × 80 cm)'
    };
    if (q2 === 'mini') return {
      titre: 'Turbo Racing MINI',
      sous: 'Découverte · la moins chère',
      texte: 'Budget serré et jamais piloté : la MINI est rassurante, lente, et pardonne tout. Elle t’apprend les trims et les trajectoires. Tu revendras vite pour une C76 — mais tu sauras pourquoi.',
      tapis: 'Turbo Racing XS (95 × 50 cm)'
    };
    if (q1 === 'petite') return {
      titre: 'Turbo Racing C76',
      sous: 'Référence · châssis TC-06',
      texte: 'Même sur une petite surface, prends la C76 : le limiteur TH.LIM à 20 % la rend docile, et tu ne rachèteras pas de voiture quand tu passeras sur un grand tapis. C’est le meilleur euro dépensé de la catégorie.',
      tapis: 'Turbo Racing XS (95 × 50 cm), avec bordures PU'
    };
    return {
      titre: 'Turbo Racing C76 × autant que de pilotes',
      sous: 'Référence · châssis TC-06',
      texte: 'Tu as la place et l’envie de courser : passe directement à la C76, et prends le même modèle pour tout le monde. Matériel identique, la différence se fait au volant. Différenciez-vous à la peinture — le kit livre deux carrosseries vierges.',
      tapis: q1 === 'grande' ? 'LDARC XL (240 × 120 cm) avec bordures' : 'Turbo Racing L (160 × 90 cm)'
    };
  }

  function initSelector() {
    var root = $('#selecteur');
    if (!root) return;
    var out = $('[data-reco-out]', root);
    var state = { q1: null, q2: null, q3: null };

    function render() {
      var r = reco(state.q1, state.q2, state.q3);
      if (!r) {
        var done = ['q1', 'q2', 'q3'].filter(function (k) { return state[k]; }).length;
        out.innerHTML = '<div class="reco-empty"><span class="tiny">En attente · ' + done + '/3</span>' +
          '<p style="margin-top:10px">Réponds aux trois questions pour voir la recommandation.</p></div>';
        return;
      }
      out.innerHTML = '<div class="reco">' +
        '<span class="tiny" style="color:var(--race-dark)">Notre recommandation</span>' +
        '<h3>' + r.titre + '</h3>' +
        '<p class="sub">' + r.sous + '</p>' +
        '<p>' + r.texte + '</p>' +
        '<div class="mat"><span class="tiny">Tapis conseillé</span>' +
        '<p style="margin-top:6px;font-weight:600;color:var(--ink)">' + r.tapis + '</p></div>' +
        '<p style="margin-top:20px"><button type="button" class="btn btn--sm" data-reset>Recommencer</button></p>' +
      '</div>';
      $('[data-reset]', out).addEventListener('click', function () {
        state = { q1: null, q2: null, q3: null };
        $$('.chip', root).forEach(function (c) { c.setAttribute('aria-pressed', 'false'); });
        render();
      });
    }

    $$('.chip', root).forEach(function (chip) {
      chip.addEventListener('click', function () {
        var q = chip.getAttribute('data-q');
        state[q] = chip.getAttribute('data-v');
        $$('.chip[data-q="' + q + '"]', root).forEach(function (c) {
          c.setAttribute('aria-pressed', String(c === chip));
        });
        render();
      });
    });
    render();
  }

  /* ============ OUTIL 03 — La radio, bouton par bouton (schéma) ========== */
  function initRadio() {
    var root = $('#radio-tool');
    if (!root) return;
    var map = $('[data-radio-map]', root);
    var list = $('[data-radio-list]', root);
    var detail = $('[data-radio-detail]', root);
    var current = 'volant';

    var tagClass = { 'CLÉ': 'pill--race', 'À ÉVITER': 'pill--warn', 'SÉCURITÉ': 'pill--warn' };

    RADIO.forEach(function (d, i) {
      var dot = document.createElement('button');
      dot.type = 'button';
      dot.className = 'dot';
      dot.style.top = d.top + '%';
      dot.style.left = d.left + '%';
      dot.textContent = String(i + 1);
      dot.setAttribute('aria-pressed', String(d.key === current));
      dot.setAttribute('aria-label', d.title);
      dot.setAttribute('data-key', d.key);
      dot.addEventListener('click', function () { select(d.key); });
      map.appendChild(dot);

      var b = document.createElement('button');
      b.type = 'button';
      b.className = 'chip';
      b.textContent = (i + 1) + ' · ' + d.label;
      b.setAttribute('aria-pressed', String(d.key === current));
      b.setAttribute('data-key', d.key);
      b.addEventListener('click', function () { select(d.key); });
      list.appendChild(b);
    });

    function select(key) {
      current = key;
      var d = RADIO.filter(function (x) { return x.key === key; })[0];
      $$('[data-key]', root).forEach(function (el) {
        el.setAttribute('aria-pressed', String(el.getAttribute('data-key') === key));
      });
      detail.innerHTML =
        '<span class="pill ' + (tagClass[d.tag] || '') + '">' + d.tag + '</span>' +
        '<h3>' + d.title + '</h3>' +
        '<p>' + d.text + '</p>';
    }
    select(current);
  }

  /* ============== OUTIL 04 — Calculateur de budget ======================= */
  function initBudget() {
    var root = $('#budget-tool');
    if (!root) return;
    var out = $('[data-budget-out]', root);
    var s = { car: 'c76', mat: 'l', pilotes: 1, bordures: true, radio: false, rfid: false };

    $$('.chip[data-b]', root).forEach(function (chip) {
      var group = chip.getAttribute('data-b');
      var key = chip.getAttribute('data-v');
      var item = group === 'car' ? CARS[key] : group === 'mat' ? MATS[key] : group === 'opt' ? OPTIONS[key] : null;
      if (item) chip.textContent = item.label + ' · ' + item.prix + ' €';
    });

    function compute() {
      var lignes = [];
      var carU = CARS[s.car].prix;
      var car = carU * s.pilotes;
      var mat = MATS[s.mat].prix;
      var opts = 0;

      lignes.push({ l: CARS[s.car].label + (s.pilotes > 1 ? ' × ' + s.pilotes : ''), v: car });
      lignes.push({ l: MATS[s.mat].label, v: mat });
      if (s.bordures) { opts += OPTIONS.bordures.prix; lignes.push({ l: OPTIONS.bordures.label, v: OPTIONS.bordures.prix }); }
      if (s.radio) { var vr = OPTIONS.radio.prix * s.pilotes; opts += vr; lignes.push({ l: OPTIONS.radio.label + (s.pilotes > 1 ? ' × ' + s.pilotes : ''), v: vr }); }
      if (s.rfid) { opts += OPTIONS.rfid.prix; lignes.push({ l: OPTIONS.rfid.label, v: OPTIONS.rfid.prix }); }

      var total = car + mat + opts;
      return { total: total, lignes: lignes, parPilote: Math.round(total / s.pilotes) };
    }

    function render() {
      var b = compute();
      out.innerHTML =
        '<div class="budget-total">' +
          '<span class="tiny" style="color:var(--race-light)">Total pour ' + s.pilotes + ' pilote' + (s.pilotes > 1 ? 's' : '') + '</span>' +
          '<p class="big" style="margin-top:8px">' + b.total + ' €</p>' +
          '<ul class="budget-lines">' +
            b.lignes.map(function (l) { return '<li><span>' + l.l + '</span><b>' + l.v + ' €</b></li>'; }).join('') +
            (s.pilotes > 1 ? '<li style="border-bottom:0;padding-top:14px"><span style="color:var(--race-light);font-weight:600">Par pilote</span><b style="color:var(--race-light)">' + b.parPilote + ' €</b></li>' : '') +
          '</ul>' +
        '</div>';
    }

    $$('.chip[data-b]', root).forEach(function (chip) {
      chip.addEventListener('click', function () {
        var group = chip.getAttribute('data-b');
        var val = chip.getAttribute('data-v');
        if (group === 'opt') {
          s[val] = !s[val];
          chip.setAttribute('aria-pressed', String(s[val]));
        } else {
          s[group] = group === 'pilotes' ? parseInt(val, 10) : val;
          $$('.chip[data-b="' + group + '"]', root).forEach(function (c) {
            c.setAttribute('aria-pressed', String(c === chip));
          });
        }
        render();
      });
    });
    render();
  }

  /* =============================== Formulaire ============================ */
  function initForm() {
    var form = $('#contact-form');
    if (!form) return;
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var d = new FormData(form);
      var body = 'Nom : ' + (d.get('nom') || '') + '\n' +
                 'E-mail : ' + (d.get('email') || '') + '\n' +
                 'Sujet : ' + (d.get('sujet') || '') + '\n\n' +
                 (d.get('message') || '');
      // ← adresse de contact du site, à changer ici si besoin
      window.location.href = 'mailto:c9149t0yz@relay.firefox.com'
        + '?subject=' + encodeURIComponent('[RC Table Racing Car] ' + (d.get('sujet') || 'Message'))
        + '&body=' + encodeURIComponent(body);
      var note = $('#form-note');
      if (note) { note.hidden = false; note.focus(); }
    });
  }

  /* ================================ Boot ================================= */
  function boot() {
    initComparator(); initSelector(); initRadio(); initBudget(); initForm();
  }
  document.readyState === 'loading'
    ? document.addEventListener('DOMContentLoaded', boot)
    : boot();
})();
