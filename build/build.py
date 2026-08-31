#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Générateur du site RC Table Racing Car.
Assemble head + header + contenu + footer + JSON-LD pour chaque page,
puis écrit sitemap.xml, robots.txt et llms.txt.

    python3 build.py
"""
import json, os, re, sys, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(HERE, "..", "site"))

# Domaine de production. Pour basculer sur un nom de domaine personnalisé :
# changer cette ligne, relancer « python3 build.py », puis pousser sur GitHub.
DOMAIN = "https://www.rctableracingcar.fr"
SITE_NAME = "RC Table Racing Car"
TAGLINE = "Le guide francophone du RC racing sur table à l’échelle 1/76"
AUTHOR = "RC Table Racing Car"
EMAIL = "c9149t0yz@relay.firefox.com"
TODAY = "2026-08-31"

from content import PAGES, NAV, ORDER   # noqa: E402

# --------------------------------------------------------------------------- #
#  Fragments partagés
# --------------------------------------------------------------------------- #

FONTS = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link rel="preload" as="style" '
    'href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700&amp;'
    'family=IBM+Plex+Mono:wght@400;500;600&amp;family=Archivo:wght@400;500;600;700&amp;display=swap">'
    '<link rel="stylesheet" media="print" onload="this.media=\'all\'" '
    'href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700&amp;'
    'family=IBM+Plex+Mono:wght@400;500;600&amp;family=Archivo:wght@400;500;600;700&amp;display=swap">'
    '<noscript><link rel="stylesheet" '
    'href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700&amp;'
    'family=IBM+Plex+Mono:wght@400;500;600&amp;family=Archivo:wght@400;500;600;700&amp;display=swap"></noscript>'
)


def header(slug):
    """Barre de navigation, avec l'onglet courant marqué."""
    groups = []
    for gname, items in NAV:
        current_group = any(u == slug for _, u, _ in items)
        links = "".join(
            '<a href="{u}"{cur}>{t}<small>{d}</small></a>'.format(
                u=PAGES[u]["url"], t=t, d=d,
                cur=' aria-current="page"' if u == slug else "")
            for t, u, d in items
        )
        groups.append(
            '<li>'
            '<button type="button" class="nav-top{cls}" aria-haspopup="true" aria-expanded="false">{g}</button>'
            '<div class="nav-panel">{links}</div>'
            '</li>'.format(g=gname, links=links, cls=" is-current" if current_group else "")
        )
    return """<a class="skip-link" href="#main">Aller au contenu</a>
<header class="site-header">
  <div class="header-bar">
    <a class="brand" href="index.html" aria-label="{sn} — accueil">
      <span class="brand-mark" aria-hidden="true"><i></i><i></i><i></i><i></i></span>
      <span class="brand-txt">
        <span class="brand-name">RC Table Racing Car</span>
        <span class="brand-sub">ÉCHELLE 1/76</span>
      </span>
    </a>
    <nav aria-label="Navigation principale">
      <ul class="nav-main" id="nav-main">{groups}</ul>
    </nav>
    <div style="display:flex;align-items:center;gap:12px">
      <a class="btn btn--race btn--sm header-cta" href="choisir-son-modele.html">Choisir ma voiture</a>
      <button type="button" class="btn-burger" aria-expanded="false" aria-controls="nav-main">MENU</button>
    </div>
  </div>
</header>""".format(sn=SITE_NAME, groups="".join(groups))


FOOTER = """<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div class="footer-col footer-about">
        <a class="brand" href="index.html" style="color:#fff;margin-bottom:16px">
          <span class="brand-mark" aria-hidden="true"><i></i><i></i><i></i><i></i></span>
          <span class="brand-txt">
            <span class="brand-name" style="color:#fff">RC Table Racing Car</span>
            <span class="brand-sub" style="color:var(--race-light)">ÉCHELLE 1/76</span>
          </span>
        </a>
        <p>Le guide francophone du RC racing sur table à l’échelle&nbsp;1/76. Site indépendant,
        sans lien commercial avec Turbo&nbsp;Racing, LDARC ou les revendeurs cités.</p>
        <p style="margin-top:14px"><a href="contact.html" class="link-arrow" style="color:var(--race-light)">Écrire au site <span aria-hidden="true">→</span></a></p>
      </div>
      <div class="footer-col">
        <span class="tiny">Débuter</span>
        <ul>
          <li><a href="debuter-en-10-minutes.html">Débuter en 10 minutes</a></li>
          <li><a href="le-concept.html">Le concept 1/76</a></li>
          <li><a href="ou-acheter-et-budget.html">Où acheter &amp; budget</a></li>
          <li><a href="glossaire.html">Glossaire</a></li>
          <li><a href="questions-frequentes.html">Questions fréquentes</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <span class="tiny">Technique</span>
        <ul>
          <li><a href="choisir-son-modele.html">Choisir son modèle</a></li>
          <li><a href="guide-turbo-racing-c76.html">Guide du C76</a></li>
          <li><a href="comprendre-la-radiocommande.html">Radiocommande</a></li>
          <li><a href="reglages-et-pilotage.html">Réglages &amp; pilotage</a></li>
          <li><a href="entretien-et-personnalisation.html">Entretien</a></li>
          <li><a href="circuits-et-tapis.html">Circuits et tapis</a></li>
          <li><a href="systemes-de-comptage.html">Systèmes de comptage</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <span class="tiny">Communauté</span>
        <ul>
          <li><a href="clubs-et-competitions.html">Clubs &amp; compétitions</a></li>
          <li><a href="galerie-des-circuits.html">Galerie des circuits</a></li>
          <li><a href="reglement-type-de-course.html">Règlement type</a></li>
          <li><a href="actus.html">Actus</a></li>
          <li><a href="contact.html">Contact</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>RC Table Racing Car · <span data-year>2026</span></span>
      <span>Prix indicatifs · marques citées à titre informatif</span>
      <span><a href="mentions-legales.html">Mentions légales</a> · <a href="plan-du-site.html">Plan du site</a></span>
    </div>
  </div>
  <div class="checker checker--thin" aria-hidden="true"></div>
</footer>"""


def crumbs(slug):
    p = PAGES[slug]
    if slug == "index":
        return ""
    items = ['<li><a href="index.html">Accueil</a></li>']
    if p.get("parent"):
        pp = PAGES[p["parent"]]
        items.append('<li><a href="%s">%s</a></li>' % (pp["url"], pp["crumb"]))
    items.append('<li><span aria-current="page">%s</span></li>' % p["crumb"])
    return ('<nav class="crumbs" aria-label="Fil d\'Ariane"><div class="wrap">'
            '<ol>%s</ol></div></nav>' % "".join(items))


def pagenav(slug):
    if slug not in ORDER:
        return ""
    i = ORDER.index(slug)
    prev = ORDER[i - 1] if i > 0 else None
    nxt = ORDER[i + 1] if i < len(ORDER) - 1 else None
    out = ['<nav class="pagenav" aria-label="Pages précédente et suivante">']
    if prev:
        out.append('<a href="{u}"><span class="tiny">← Précédent</span><b>{t}</b></a>'.format(
            u=PAGES[prev]["url"], t=PAGES[prev]["crumb"]))
    else:
        out.append('<a href="index.html"><span class="tiny">← Retour</span><b>Accueil</b></a>')
    if nxt:
        out.append('<a href="{u}"><span class="tiny">Suivant →</span><b>{t}</b></a>'.format(
            u=PAGES[nxt]["url"], t=PAGES[nxt]["crumb"]))
    else:
        out.append('<a href="questions-frequentes.html"><span class="tiny">Suivant →</span><b>Questions fréquentes</b></a>')
    out.append('</nav>')
    return "".join(out)


# --------------------------------------------------------------------------- #
#  Données structurées
# --------------------------------------------------------------------------- #

def jsonld_common(slug):
    p = PAGES[slug]
    url = DOMAIN + "/" + ("" if slug == "index" else p["url"])
    blocks = []

    blocks.append({
        "@context": "https://schema.org",
        "@type": "WebSite",
        "@id": DOMAIN + "/#website",
        "url": DOMAIN + "/",
        "name": SITE_NAME,
        "alternateName": ["RC Table Racing", "RC racing sur table 1/76"],
        "description": TAGLINE,
        "inLanguage": "fr-FR",
        "publisher": {"@id": DOMAIN + "/#org"},
    })

    blocks.append({
        "@context": "https://schema.org",
        "@type": "Organization",
        "@id": DOMAIN + "/#org",
        "name": SITE_NAME,
        "url": DOMAIN + "/",
        "description": TAGLINE,
        "email": EMAIL,
        "logo": {"@type": "ImageObject", "url": DOMAIN + "/img/logo.svg", "width": 512, "height": 512},
        "knowsAbout": [
            "RC racing sur table", "Modélisme échelle 1/76", "Turbo Racing C76",
            "Châssis TC-06", "Radiocommande proportionnelle", "Tapis de course RC",
            "Drift RC 1/76", "Organisation de courses RC",
        ],
        "areaServed": {"@type": "Country", "name": "France"},
    })

    bc = [{"@type": "ListItem", "position": 1, "name": "Accueil", "item": DOMAIN + "/"}]
    if p.get("parent"):
        bc.append({"@type": "ListItem", "position": 2, "name": PAGES[p["parent"]]["crumb"],
                   "item": DOMAIN + "/" + PAGES[p["parent"]]["url"]})
    if slug != "index":
        bc.append({"@type": "ListItem", "position": len(bc) + 1, "name": p["crumb"], "item": url})
    blocks.append({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": bc})

    wp = {
        "@context": "https://schema.org",
        "@type": p.get("page_type", "WebPage"),
        "@id": url + "#webpage",
        "url": url,
        "name": p["title"],
        "description": p["desc"],
        "inLanguage": "fr-FR",
        "isPartOf": {"@id": DOMAIN + "/#website"},
        "mainEntityOfPage": url,
        "isAccessibleForFree": True,
        "datePublished": "2026-07-01",
        "dateModified": TODAY,
        "author": {"@id": DOMAIN + "/#org"},
        "primaryImageOfPage": {"@type": "ImageObject", "url": DOMAIN + "/img/" + p.get("image", "hero-track.png")},
    }
    if p.get("about"):
        wp["about"] = [{"@type": "Thing", "name": a} for a in p["about"]]
    if p.get("speakable"):
        wp["speakable"] = {"@type": "SpeakableSpecification", "cssSelector": p["speakable"]}
    blocks.append(wp)

    for extra in p.get("jsonld", []):
        blocks.append(extra)
    return blocks


# --------------------------------------------------------------------------- #
#  Gabarit
# --------------------------------------------------------------------------- #

TEMPLATE = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="{robots}">
<meta name="author" content="{author}">
<meta name="theme-color" content="#101215">
<meta name="format-detection" content="telephone=no">
<link rel="alternate" hreflang="fr" href="{canonical}">
<link rel="alternate" hreflang="x-default" href="{canonical}">

<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{site_name}">
<meta property="og:locale" content="fr_FR">
<meta property="og:title" content="{og_title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{domain}/img/{image}">
<meta property="og:image:alt" content="{image_alt}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{og_title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{domain}/img/{image}">

<link rel="icon" href="img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="img/logo.svg">
<link rel="manifest" href="manifest.webmanifest">
{fonts}
<link rel="stylesheet" href="assets/css/style.css">
<script type="application/ld+json">{jsonld}</script>
</head>
<body>
<div id="read-progress" style="position:fixed;top:0;left:0;height:3px;width:100%;background:var(--race);transform-origin:left;transform:scaleX(0);z-index:100;transition:transform .1s linear" aria-hidden="true"></div>
{header}
{crumbs}
<main id="main">
{body}
</main>
{pagenav}
{footer}
<script src="assets/js/main.js" defer></script>
{tools}
<script defer src="https://cdn.vercel-insights.com/v1/script.js"></script>
</body>
</html>
"""


def inject_head_bg(body, p):
    """Insère l'image de fond décorative dans l'en-tête de page."""
    bg = p.get("head_bg", p.get("image"))
    if not bg or '<section class="page-head">' not in body:
        return body
    layer = ('<section class="page-head">'
             '<div class="page-head-bg" aria-hidden="true">'
             '<img src="img/{bg}" alt="" width="1600" height="900" decoding="async" fetchpriority="high">'
             '</div>').format(bg=bg)
    return body.replace('<section class="page-head">', layer, 1)


def build_page(slug):
    p = PAGES[slug]
    p["body"] = inject_head_bg(p["body"], p)
    url = DOMAIN + "/" + ("" if slug == "index" else p["url"])
    blocks = jsonld_common(slug)
    jsonld = json.dumps(blocks[0] if len(blocks) == 1 else
                        {"@context": "https://schema.org", "@graph": [
                            {k: v for k, v in b.items() if k != "@context"} for b in blocks]},
                        ensure_ascii=False, separators=(",", ":"))
    html = TEMPLATE.format(
        title=p["title"], desc=p["desc"], canonical=url, author=AUTHOR,
        robots=("noindex, follow" if slug == "404" else
                "index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1"),
        og_type=p.get("og_type", "website"), og_title=p.get("og_title", p["title"]),
        site_name=SITE_NAME, domain=DOMAIN, image=p.get("image", "hero-track.png"),
        image_alt=p.get("image_alt", "Circuit RC 1/76 vu de dessus"),
        fonts=FONTS, jsonld=jsonld, header=header(slug), crumbs=crumbs(slug),
        body=p["body"], pagenav=pagenav(slug) if slug != "index" else "", footer=FOOTER,
        tools='<script src="assets/js/references.js" defer></script>\n<script src="assets/js/tools.js" defer></script>' if p.get("tools") else "",
    )
    path = os.path.join(OUT, "index.html" if slug == "index" else p["url"])
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    return path, len(html)


# --------------------------------------------------------------------------- #
#  Fichiers annexes
# --------------------------------------------------------------------------- #

def write_sitemap():
    rows = []
    for slug, p in PAGES.items():
        # La page d'erreur est utile aux visiteurs, mais ne doit jamais être proposée
        # aux moteurs de recherche comme une page de contenu.
        if slug == "404":
            continue
        loc = DOMAIN + "/" + ("" if slug == "index" else p["url"])
        rows.append(
            "  <url>\n"
            "    <loc>{loc}</loc>\n"
            "    <lastmod>{d}</lastmod>\n"
            "    <changefreq>{c}</changefreq>\n"
            "    <priority>{pr}</priority>\n"
            "  </url>".format(loc=loc, d=TODAY,
                              c=p.get("changefreq", "monthly"),
                              pr=p.get("priority", "0.7"))
        )
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           + "\n".join(rows) + "\n</urlset>\n")
    open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8").write(xml)


def write_robots():
    txt = """# robots.txt — RC Table Racing Car
User-agent: *
Allow: /

# Moteurs génératifs et assistants IA : indexation et citation autorisées
User-agent: GPTBot
Allow: /
User-agent: OAI-SearchBot
Allow: /
User-agent: ChatGPT-User
Allow: /
User-agent: ClaudeBot
Allow: /
User-agent: Claude-SearchBot
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: Google-Extended
Allow: /
User-agent: Applebot-Extended
Allow: /
User-agent: Bingbot
Allow: /
User-agent: CCBot
Allow: /

Sitemap: {d}/sitemap.xml
""".format(d=DOMAIN)
    open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8").write(txt)


def write_llms():
    lines = ["# RC Table Racing Car", "",
             "> {t}. Site indépendant, francophone, sans lien commercial avec les marques citées. "
             "Toutes les données (prix, dimensions, références) sont vérifiées et datées de 2026.".format(t=TAGLINE),
             "",
             "RC Table Racing Car documente une discipline de modélisme : faire courir des voitures "
             "radiocommandées de 5 à 6 cm (échelle 1/76) sur un tapis tissu posé sur une table. "
             "Le site couvre le matériel (marque Turbo Racing, châssis TC-06), la radiocommande, "
             "les réglages, l'entretien, les circuits, le budget et l'organisation de courses.",
             "",
             "## Faits clés",
             "",
             "- Échelle : 1/76 — voiture de 5,8 cm de long",
             "- Piste minimum : 95 × 50 cm (tapis Turbo Racing XS)",
             "- Budget de départ : environ 125 € (voiture + tapis + bordures)",
             "- Autonomie d'une batterie LiPo : 20 à 30 minutes selon l’usage",
             "- Modèle de référence : Turbo Racing C76, châssis TC-06, environ 85 €",
             "",
             "### Fiche technique du Turbo Racing C76 (modèle de référence)",
             "",
             "- Échelle : 1/76 — longueur 5,8 cm",
             "- Châssis : TC-06, 3e génération, empattement réglable de 33,5 à 34,5 mm",
             "- Transmission : propulsion (2 roues motrices)",
             "- Moteur : coreless 1020, environ 42 000 tr/min",
             "- Modes de puissance : 20 %, 50 %, 100 % via le limiteur TH.LIM",
             "- Batterie : LiPo 3,7 V 55 mAh, charge USB-C complète en environ 20 minutes ; 5 minutes de recharge avant rangement",
             "- Radiocommande : 2,4 GHz, direction et accélération proportionnelles",
             "- Éclairage : LED avant et arrière",
             "- Vitesse annoncée : environ 6 km/h",
             "- Livraison : RTR (Ready To Run), environ 85 €",
             "- Modèles partageant le même châssis TC-06 : C76 (85 €), C76LE (95 €), C78 (100 €)",
             "- Réglage clé pour débuter : limiteur de puissance TH.LIM sur 20 %",
             "- Règle de sécurité : allumer la radio avant la voiture, l'éteindre après",
             "",
             "## Pages", ""]
    for slug in ["index"] + ORDER:
        p = PAGES[slug]
        lines.append("- [{t}]({d}/{u}): {desc}".format(
            t=p["crumb"], d=DOMAIN, u=("" if slug == "index" else p["url"]), desc=p["desc"]))
    lines += ["", "## Ressources", "",
              "- [Sitemap XML]({d}/sitemap.xml)".format(d=DOMAIN),
              "- Contact : {e}".format(e=EMAIL),
              "", "## Conditions de citation", "",
              "Le contenu peut être cité et résumé par les assistants IA à condition de mentionner "
              "« RC Table Racing Car » et de renvoyer vers l'URL de la page source.", ""]
    open(os.path.join(OUT, "llms.txt"), "w", encoding="utf-8").write("\n".join(lines))


def write_manifest():
    m = {
        "name": SITE_NAME, "short_name": "RC 1/76", "lang": "fr",
        "description": TAGLINE, "start_url": "/", "display": "standalone",
        "background_color": "#ffffff", "theme_color": "#101215",
        "icons": [{"src": "img/logo.svg", "sizes": "any", "type": "image/svg+xml", "purpose": "any maskable"}],
    }
    open(os.path.join(OUT, "manifest.webmanifest"), "w", encoding="utf-8").write(
        json.dumps(m, ensure_ascii=False, indent=2))


# --------------------------------------------------------------------------- #

def main():
    os.makedirs(OUT, exist_ok=True)
    total = 0
    for slug in PAGES:
        path, size = build_page(slug)
        total += size
        print("  {:<38} {:>7,} o".format(os.path.basename(path), size))
    write_sitemap(); write_robots(); write_llms(); write_manifest()
    print("\n{} pages · {:,} octets · sitemap.xml, robots.txt, llms.txt, manifest.webmanifest".format(len(PAGES), total))


if __name__ == "__main__":
    main()
