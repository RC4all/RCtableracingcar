# Mise en ligne

- **Dépôt GitHub :** `git@github.com:mickael-IIDI/rctableracingcar.git`
- **Domaine principal :** `https://rctableracingcar.fr` (acheté chez OVH)

Le site est déjà configuré pour ce domaine : URL canoniques, Open Graph,
`sitemap.xml`, `robots.txt`, `llms.txt` et données structurées.

---

## 1. Pousser sur GitHub

Clic droit dans le dossier `RC table car racing` → **Afficher plus d'options**
→ **Open Git Bash here**, puis :

```bash
git init
git branch -M main
git add .
git commit -m "Site RC Table Racing Car : 20 pages statiques, SEO et GEO"
git remote add origin git@github.com:mickael-IIDI/rctableracingcar.git
git push -u origin main
```

Si c'est ton premier usage de Git sur cette machine, à faire une seule fois
avant le `commit` :

```bash
git config --global user.name "Mickael"
git config --global user.email "mickael@iidi.fr"
```

Dans Git Bash, le collage se fait au **clic droit → Paste** ou **Maj+Inser**
(`Ctrl+V` ne fonctionne pas).

### Si ça bloque

| Message | Solution |
|---|---|
| `Permission denied (publickey)` | `git remote set-url origin https://github.com/mickael-IIDI/rctableracingcar.git` puis repousser — GitHub ouvrira une fenêtre d'authentification |
| `remote origin already exists` | Remplacer `git remote add` par `git remote set-url` |
| `Updates were rejected` | `git pull --rebase origin main` puis repousser |
| `Author identity unknown` | Lancer les deux `git config` ci-dessus |

---

## 2. Importer dans Vercel

1. vercel.com → **Add New** → **Project** → **Import Git Repository**
2. Choisir `mickael-IIDI/rctableracingcar`
3. **Ne toucher à aucun réglage** — `vercel.json` déclare déjà que le dossier
   à publier est `site/`, sans étape de build
4. **Deploy**

---

## 3. Brancher le domaine OVH

### Côté Vercel

Settings → **Domains** → ajouter **`rctableracingcar.fr`** et
**`www.rctableracingcar.fr`**.

⚠️ **Vérifier le sens de la redirection.** Vercel propose souvent par défaut
l'inverse de ce qu'il faut : `rctableracingcar.fr` redirigé vers le `www`.
Comme toutes les URL canoniques du site sont **sans www**, il faut :

| Domaine | Réglage attendu |
|---|---|
| `rctableracingcar.fr` | **Production** (aucune redirection) |
| `www.rctableracingcar.fr` | **Redirection 308** vers `rctableracingcar.fr` |
| `rctableracingcar.vercel.app` | laissé tel quel, il redirigera tout seul |

Si c'est configuré à l'envers, Google voit une canonique qui redirige ailleurs
et n'indexe pas. Bouton **Edit** sur chaque ligne pour corriger.

### Côté OVH

Espace client → **Noms de domaine** → `rctableracingcar.fr` → onglet **Zone DNS**.

1. **Supprimer** les enregistrements `A` et `AAAA` existants sur la racine —
   OVH en crée par défaut vers sa page de parking. Tant qu'ils sont là, le
   domaine ne pointera pas vers Vercel.
2. **Créer** les enregistrements indiqués par Vercel : dans l'écran Domains,
   déplier **View DNS configuration** sous chaque domaine.

En général un `A` sur la racine et un `CNAME` sur `www` vers
`cname.vercel-dns.com.` (le point final compte). **Ne pas recopier une adresse
IP trouvée ailleurs** : Vercel a changé la sienne pour les nouveaux projets,
seule la valeur affichée dans ton tableau de bord fait foi.

Revenir ensuite sur la page Domains et cliquer **Refresh**.

La propagation DNS prend de quelques minutes à quelques heures. Vercel émet le
certificat HTTPS automatiquement une fois le domaine résolu.

---

## 4. Vérifications après mise en ligne

| À vérifier | URL |
|---|---|
| Accueil, circuit animé | `/` |
| Images de fond des en-têtes | `/guide-turbo-racing-c76.html` |
| Les 4 outils interactifs | `/choisir-son-modele.html` |
| Schéma de la radiocommande | `/comprendre-la-radiocommande.html` |
| Sitemap servi en XML | `/sitemap.xml` |
| Fichier pour les IA | `/llms.txt` |
| Page 404 | `/nimporte-quoi` |
| Redirection du www | `www.rctableracingcar.fr` → `rctableracingcar.fr` |

Tester aussi en mobile (F12 puis Ctrl+Maj+M).

---

## 5. Référencement

Une fois le domaine actif et le HTTPS en place :

1. **Google Search Console** → ajouter la propriété `https://rctableracingcar.fr`,
   valider par enregistrement DNS TXT chez OVH, puis soumettre `sitemap.xml`
2. **Bing Webmaster Tools** → import depuis la Search Console
3. Tester les données structurées : `https://search.google.com/test/rich-results`
4. Mesurer la performance : `https://pagespeed.web.dev/`

---

## 6. Changer de domaine plus tard

1. Ajouter le nouveau domaine dans Vercel et le passer en principal
2. `build/build.py`, ligne 15 : modifier `DOMAIN`
3. `cd build && python3 build.py`
4. Commiter et pousser

Les canoniques, l'Open Graph, le sitemap, le `robots.txt`, le `llms.txt` et les
données structurées des 20 pages sont mis à jour d'un seul coup.

---

## Points à traiter avant de communiquer

- [ ] **Boîte e-mail** — le site utilise `contact@rctableracingcar.fr`
      (formulaire de contact et données structurées `Organization`). Cette
      adresse doit exister et être relevée. Chez OVH, elle se crée dans
      l'espace client → **E-mails** ; une redirection vers ta messagerie
      habituelle suffit et ne coûte rien. Sans ça, le formulaire de contact
      ouvrira un `mailto:` vers une adresse qui n'existe pas.
- [ ] **Mentions légales** — compléter l'hébergeur dans
      `site/mentions-legales.html`. Pour Vercel : Vercel Inc.,
      440 N Barranca Ave #4133, Covina, CA 91723, États-Unis.
- [ ] **Visuels du constructeur** — vues éclatées, plans de tapis et photos de
      radios proviennent de la documentation Turbo Racing et LDARC. Créditées
      dans les légendes, mais à remplacer progressivement par tes photos.
- [ ] **Photo de la soirée** — `site/img/photos/soiree-course-*.webp` montre
      des personnes identifiables : s'assurer d'avoir leur accord.
