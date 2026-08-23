# RC Table Racing Car

Le guide francophone du RC racing sur table à l'échelle 1/76.
Site statique, sans serveur, sans base de données, sans cookie ni traceur.

**En ligne :** https://rctableracingcar.fr
**Dépôt :** `git@github.com:mickael-IIDI/rctableracingcar.git`

---

## Structure du dépôt

```
site/                 ← ce que Vercel publie
  index.html          accueil
  *.html              19 autres pages
  assets/css/         un seul fichier de styles
  assets/js/          animations + les 4 outils interactifs
  img/                logo, favicon, schéma de la radio, illustrations
  img/photos/         photos optimisées (WebP + repli JPEG)
  robots.txt · sitemap.xml · llms.txt · manifest.webmanifest

build/                générateur des pages (facultatif pour déployer)
  build.py            assemble en-tête, contenu, pied de page et JSON-LD
  content.py          navigation, fragments partagés, hero animé
  pages1-4.py         contenu éditorial
  images.py           optimisation des photos sources

Images/               photos d'origine, non publiées
vercel.json           configuration du déploiement
```

## Déploiement

Vercel publie le contenu de `site/` — c'est déclaré dans `vercel.json`
(`outputDirectory`). Aucun réglage à faire dans l'interface, aucune étape de
build : chaque `git push` sur `main` déclenche une mise en ligne.

## Régénérer les pages

Nécessaire seulement si on touche aux menus, au pied de page, aux données
structurées ou au contenu éditorial — c'est-à-dire à tout ce qui est partagé
entre plusieurs pages.

```bash
cd build
python3 build.py        # réécrit les 20 pages + sitemap + robots + llms
python3 images.py       # ré-optimise Images/ vers site/img/photos/ (Pillow requis)
```

Pour une correction ponctuelle sur une seule page, éditer directement le
fichier HTML dans `site/` est plus rapide — mais penser à reporter la
modification dans `build/pages*.py`, sinon la prochaine génération l'écrasera.

## Changer de nom de domaine

1. Ajouter le domaine dans Vercel → Settings → Domains, et le passer en
   **domaine principal** (les autres adresses redirigeront vers lui en 308)
2. Modifier `DOMAIN` dans `build/build.py` (ligne 15)
3. `python3 build.py`
4. Commiter et pousser

Cela met à jour d'un coup les URL canoniques, les balises Open Graph,
`sitemap.xml`, `robots.txt`, `llms.txt` et les données structurées.

## Ce qui est en place pour le référencement

- Une URL, un `<title>` et une description rédigés par page
- URL canoniques, `hreflang`, Open Graph et Twitter Card
- 14 types de données structurées Schema.org : `WebSite`, `Organization`,
  `BreadcrumbList`, `FAQPage`, `HowTo`, `Product`, `ItemList`,
  `DefinedTermSet`, `ImageGallery`, `Blog`…
- `sitemap.xml` avec priorités et fréquences, `robots.txt`
- `llms.txt` et blocs de réponse directe pour la citation par les IA
- HTML sémantique, un seul `<h1>` par page, images en chargement différé

## Après la première mise en ligne

- [ ] Déclarer `sitemap.xml` dans la Google Search Console et Bing Webmaster Tools
- [ ] Compléter l'hébergeur dans `site/mentions-legales.html`
- [ ] Vérifier l'adresse de contact dans `site/assets/js/tools.js`
- [ ] Contrôler le rendu des aperçus sociaux (image `og:image` de chaque page)

## Licence et indépendance

Site indépendant. Aucun partenariat, aucune commission, aucun lien commercial
avec Turbo Racing, LDARC ou les revendeurs cités. Les marques et références
sont mentionnées à titre informatif, les prix sont des ordres de grandeur
constatés en 2026.
