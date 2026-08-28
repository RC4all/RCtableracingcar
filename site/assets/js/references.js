/* ===========================================================================
   RÉFÉRENCES PRODUITS ET PRIX — fichier à modifier manuellement

   Changez uniquement les valeurs entre guillemets ci-dessous. Les outils du
   site reprendront automatiquement ces noms et ces prix.
   =========================================================================== */
(function () {
  'use strict';

  window.RC_REFERENCE = {
    models: [
      { id: 'MINI',      cat: 'decouverte', chassis: 'v0',          usage: 'Découverte',   prix: 50,  note: 'Rassurante et peu rapide, idéale pour apprendre les commandes sans casser. Sortie en 2021.', thumb: 'photos/model-mini.jpg' },
      { id: 'C61 → C66', cat: 'drift',      chassis: 'Drift',      usage: 'Drift',        prix: 90,  note: 'Pneus métalliques, dérive volontaire et contre-braquage. Spectaculaire, mais pas fait pour le chrono. Sortie entre 2022 et 2025.', thumb: 'photos/c66-drift.webp' },
      { id: 'C71 → C74', cat: 'racing',     chassis: 'v1',         usage: 'Racing loisir', prix: 70,  note: 'Première génération. Agréable en loisir, dépassée en course. Sortie entre 2021 et 2023.', thumb: 'photos/model-c71-c74.png' },
      { id: 'C71 RTR',   cat: 'racing',     chassis: 'v3 TC-06',   usage: 'Racing', prix: 86,  note: 'Nouvelle version avec dernier châssis. Verte. Sortie en 2026.', thumb: 'photos/model-c71-2026.png' },
      { id: 'C72 RTR',   cat: 'racing',     chassis: 'v3 TC-06',   usage: 'Racing', prix: 86,  note: 'Nouvelle version avec dernier châssis. Jaune. Sortie en 2026.', thumb: 'photos/model-c72-2026.png' },
      { id: 'C73 RTR',   cat: 'racing',     chassis: 'v3 TC-06',   usage: 'Racing', prix: 86,  note: 'Nouvelle version avec dernier châssis. Violet. Sortie en 2026.', thumb: 'photos/model-c73-2026.png' },
      { id: 'C74 RTR',   cat: 'racing',     chassis: 'v3 TC-06',   usage: 'Racing', prix: 80,  note: 'Nouvelle version avec dernier châssis. Bleu. Sortie en 2026.', thumb: 'photos/model-c74-2026.png' },
      { id: 'C75',       cat: 'racing',     chassis: 'v2',         usage: 'Racing', prix: 90,  note: 'Plus rapide que la v1 et 3, mais moins précise à piloter. Sortie en 2023.', thumb: 'photos/model-c75-no-text.jpg' },
      { id: 'C76',       cat: 'racing',     chassis: 'v3 TC-06',   usage: 'Référence', prix: 85,  note: 'La meilleure : précision et vitesse au prix le plus juste. Notre base de comparaison. Sortie en 2025.', thumb: 'photos/model-c76-no-text.png', star: true },
      { id: 'C76LE',     cat: 'racing',     chassis: 'v3 TC-06',   usage: 'Racing', prix: 95,  note: 'Identique à la C76, carrosserie plus détaillée. Sortie en 2025.', thumb: 'photos/model-c76le.png' },
      { id: 'C78',       cat: 'racing',     chassis: 'v3 TC-06',   usage: 'Racing', prix: 100, note: 'Même base que la C76, carrosserie plus détaillée et prix plus élevé. Sortie en 2026.', thumb: 'photos/c78-rallye.webp' },
      { id: 'C81 → C82', cat: 'fun',        chassis: 'v2 Wide',    usage: 'Hors piste', prix: 70,  note: 'Hors gabarit pour la catégorie, mais parfaite comme pace car. Sortie entre 2021 et 2022.', thumb: 'photos/model-c82.jpg' }
    ],

    budget: {
      cars: {
        mini:  { label: 'Turbo Racing MINI',  prix: 50 },
        c76:   { label: 'Turbo Racing C76',   prix: 85 },
        c76le: { label: 'Turbo Racing C76LE', prix: 95 }
      },
      mats: {
        xs:   { label: 'Turbo Racing XS · 95 × 50 cm', prix: 25 },
        m:    { label: 'Turbo Racing M · 120 × 80 cm', prix: 40 },
        l:    { label: 'Turbo Racing L · 160 × 90 cm', prix: 60 },
        xl:   { label: 'LDARC XL · 240 × 120 cm',      prix: 120 },
        none: { label: 'Aucun (circuit maison)',       prix: 0 }
      },
      options: {
        bordures: { label: 'Bordures PU autocollantes · 5 m', prix: 15 },
        radio:    { label: 'Radio P32S',                      prix: 45 },
        rfid:     { label: 'Comptage de tours RFID',          prix: 90 }
      }
    }
  };
})();
