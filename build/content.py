# -*- coding: utf-8 -*-
"""Contenu éditorial des pages. Un dict par page, injecté dans le gabarit."""

# --------------------------------------------------------------------------- #
#  Navigation : (groupe, [(libellé, slug, sous-titre)])
# --------------------------------------------------------------------------- #
NAV = [
    ("Débuter", [
        ("Débuter en 10 minutes", "debuter", "Les 4 étapes du premier soir"),
        ("Le concept 1/76", "concept", "Ce qui définit la discipline"),
        ("Où acheter &amp; budget", "budget", "Calculateur · à partir de 125 €"),
    ]),
    ("Matériel", [
        ("Choisir son modèle", "modeles", "Comparateur des 11 Turbo Racing"),
        ("Guide du Turbo Racing C76", "c76", "La référence, châssis TC-06"),
        ("Comprendre la radiocommande", "radio", "Schéma cliquable, 11 commandes"),
        ("Circuits et tapis", "circuits", "Dimensions, bordures, tracés"),
    ]),
    ("Piloter", [
        ("Réglages &amp; pilotage", "pilotage", "Les 4 gestes qui font le chrono"),
        ("Entretien &amp; personnalisation", "entretien", "La routine batterie par batterie"),
        ("Règlement type de course", "reglement", "6 articles prêts à copier"),
    ]),
    ("Communauté", [
        ("Clubs &amp; compétitions", "clubs", "Où rouler, comment organiser"),
        ("Galerie des circuits", "galerie", "Les pistes des pilotes"),
        ("Actus", "actus", "Essais, ateliers, comptes rendus"),
        ("Contact", "contact", "Signaler un club, corriger"),
    ]),
    ("Ressources", [
        ("Glossaire du 1/76", "glossaire", "20 termes expliqués"),
        ("Questions fréquentes", "faq", "Les 11 questions qui reviennent"),
        ("Plan du site", "plan", "Toutes les pages"),
    ]),
]

# Ordre de lecture (précédent / suivant en bas de page)
ORDER = ["debuter", "concept", "modeles", "c76", "radio", "pilotage", "entretien",
         "circuits", "budget", "reglement", "clubs", "galerie", "actus",
         "glossaire", "faq", "contact"]


# --------------------------------------------------------------------------- #
#  Fragments réutilisables
# --------------------------------------------------------------------------- #

MARQUEE = """<div class="marquee" aria-hidden="true">
  <div class="marquee-track">
    <span>Échelle 1/76</span><span>Voiture de 5,8 cm</span><span>Piste dès 95 × 50 cm</span>
    <span>Châssis TC-06</span><span>20 à 30 min d’autonomie</span><span>Ticket d’entrée ≈ 125 €</span>
    <span>Proche de la série</span><span>Objectif : championnat de France 1/76</span>
    <span>Échelle 1/76</span><span>Voiture de 5,8 cm</span><span>Piste dès 95 × 50 cm</span>
    <span>Châssis TC-06</span><span>20 à 30 min d’autonomie</span><span>Ticket d’entrée ≈ 125 €</span>
    <span>Proche de la série</span><span>Objectif : championnat de France 1/76</span>
  </div>
</div>"""


def statbar(items):
    cells = "".join(
        '<div class="stat"><span class="stat-k">{k}</span>'
        '<span class="stat-v"{attrs}>{v}</span></div>'.format(
            k=k, v=v, attrs=attrs)
        for k, v, attrs in items)
    return '<div class="statbar"><div class="statbar-grid">%s</div></div>' % cells


def cta(text, href, label, dark=False):
    return """<section class="section {cls}">
  <div class="wrap" style="display:flex;gap:26px;align-items:center;justify-content:space-between;flex-wrap:wrap" data-reveal>
    <p class="h3" style="max-width:24ch;margin:0">{t}</p>
    <a class="btn {btn}" href="{h}">{l} <span class="arrow" aria-hidden="true">→</span></a>
  </div>
</section>""".format(t=text, h=href, l=label,
                     cls="section--dark" if dark else "section--wash",
                     btn="btn--race" if dark else "btn--race")


# Tracé unique partagé par toutes les couches du circuit
_TRACK_D = ("M 120 300 C 60 300 60 130 150 130 C 250 130 250 250 320 250 "
            "C 390 250 390 100 470 100 C 570 100 590 240 540 320 "
            "C 490 400 400 400 330 380 C 250 357 210 300 120 300 Z")


def _car(color, shade, light, num=""):
    """Une voiture vue de dessus : carrosserie dégradée, pare-brise, reflet, ombre."""
    return """
    <ellipse cx="1" cy="1.5" rx="10.5" ry="6.5" fill="#000" opacity=".45" filter="url(#soft)"/>
    <rect x="-8.6" y="-6.9" width="4.6" height="2.1" rx=".7" fill="#101215"/>
    <rect x="-8.6" y="4.8" width="4.6" height="2.1" rx=".7" fill="#101215"/>
    <rect x="3.9" y="-6.9" width="4.6" height="2.1" rx=".7" fill="#101215"/>
    <rect x="3.9" y="4.8" width="4.6" height="2.1" rx=".7" fill="#101215"/>
    <path d="M -9.4 0 C -9.4 -3.6 -7.4 -5.2 -4.4 -5.2 L 5.4 -5.2 C 8.2 -5.2 9.6 -3.2 9.6 0
             C 9.6 3.2 8.2 5.2 5.4 5.2 L -4.4 5.2 C -7.4 5.2 -9.4 3.6 -9.4 0 Z"
          fill="url(#body{c})" stroke="{shade}" stroke-width=".45"/>
    <path d="M -1.6 -4.1 C 1.4 -4.1 3.4 -2.4 3.8 0 C 3.4 2.4 1.4 4.1 -1.6 4.1
             C -3.6 4.1 -4.6 2.2 -4.6 0 C -4.6 -2.2 -3.6 -4.1 -1.6 -4.1 Z" fill="#1b1f25" opacity=".92"/>
    <path d="M -1.6 -3.7 C 0.4 -3.7 2 -2.6 2.6 -1.2 L -3.4 -1.6 C -3.1 -2.9 -2.6 -3.7 -1.6 -3.7 Z"
          fill="#7d8894" opacity=".5"/>
    <path d="M -8.4 -3.5 C -7.4 -4.4 -6 -4.7 -4.4 -4.7 L 5.2 -4.7 C 7 -4.7 8.2 -3.8 8.8 -2.6
             L 8.4 -2.4 C 7.8 -3.4 6.7 -4.1 5.2 -4.1 L -4.4 -4.1 C -6 -4.1 -7.2 -3.8 -8.1 -3.1 Z"
          fill="{light}" opacity=".75"/>
    <rect x="8.4" y="-3.6" width="1.4" height="1.5" rx=".5" fill="#fff8e6" opacity=".95"/>
    <rect x="8.4" y="2.1" width="1.4" height="1.5" rx=".5" fill="#fff8e6" opacity=".95"/>
    <rect x="-9.2" y="-3.2" width="1" height="1.3" rx=".4" fill="#ff5533" opacity=".9"/>
    <rect x="-9.2" y="1.9" width="1" height="1.3" rx=".4" fill="#ff5533" opacity=".9"/>
    {num}""".format(c=color, shade=shade, light=light,
                    num=('<text x="-1" y="1.9" font-family="IBM Plex Mono,monospace" font-size="4.4" '
                         'font-weight="700" fill="#fff" opacity=".9" text-anchor="middle">%s</text>' % num) if num else "")


HERO_SVG = ("""<svg viewBox="0 0 640 480" role="img" preserveAspectRatio="xMidYMid slice"
     aria-label="Circuit de course RC à l’échelle 1/76 vu de dessus : tapis tissu, glissières blanches, vibreurs et trois voitures en piste"
     style="width:100%;aspect-ratio:4/3;display:block">
  <defs>
    <!-- tapis tissu : bruit fractal éclairé pour la trame du feutre -->
    <filter id="felt" x="0" y="0" width="100%" height="100%">
      <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="4" seed="7" result="n"/>
      <feColorMatrix in="n" type="saturate" values="0"/>
      <feComponentTransfer><feFuncA type="linear" slope=".16"/></feComponentTransfer>
    </filter>
    <!-- grain de l'asphalte -->
    <filter id="grain" x="-5%" y="-5%" width="110%" height="110%">
      <feTurbulence type="fractalNoise" baseFrequency="1.4" numOctaves="3" seed="3" result="n"/>
      <feColorMatrix in="n" type="saturate" values="0"/>
      <feComponentTransfer><feFuncA type="linear" slope=".1"/></feComponentTransfer>
    </filter>
    <filter id="soft" x="-60%" y="-60%" width="220%" height="220%">
      <feGaussianBlur stdDeviation="2.1"/>
    </filter>
    <filter id="wallShadow" x="-30%" y="-30%" width="160%" height="160%">
      <feDropShadow dx="0" dy="2.4" stdDeviation="2.2" flood-color="#000" flood-opacity=".55"/>
    </filter>
    <radialGradient id="matLight" cx="34%" cy="22%" r="88%">
      <stop offset="0%" stop-color="#3a3f47"/>
      <stop offset="55%" stop-color="#24272d"/>
      <stop offset="100%" stop-color="#131519"/>
    </radialGradient>
    <linearGradient id="asphalt" x1="0" y1="0" x2=".8" y2="1">
      <stop offset="0%" stop-color="#4a4f58"/>
      <stop offset="45%" stop-color="#3a3e46"/>
      <stop offset="100%" stop-color="#2b2f36"/>
    </linearGradient>
    <linearGradient id="wall" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#ffffff"/><stop offset="100%" stop-color="#b9bec6"/>
    </linearGradient>
    <linearGradient id="bodyO" x1=".2" y1="0" x2=".8" y2="1">
      <stop offset="0%" stop-color="#ff9a5c"/><stop offset="42%" stop-color="#e8642a"/>
      <stop offset="100%" stop-color="#a8380f"/>
    </linearGradient>
    <linearGradient id="bodyB" x1=".2" y1="0" x2=".8" y2="1">
      <stop offset="0%" stop-color="#7ab6f0"/><stop offset="42%" stop-color="#2f77c8"/>
      <stop offset="100%" stop-color="#164a86"/>
    </linearGradient>
    <linearGradient id="bodyY" x1=".2" y1="0" x2=".8" y2="1">
      <stop offset="0%" stop-color="#ffe89a"/><stop offset="42%" stop-color="#e8bf2c"/>
      <stop offset="100%" stop-color="#a8830c"/>
    </linearGradient>
    <radialGradient id="vig" cx="50%" cy="42%" r="76%">
      <stop offset="55%" stop-color="#000" stop-opacity="0"/>
      <stop offset="100%" stop-color="#000" stop-opacity=".62"/>
    </radialGradient>
  </defs>

  <!-- le tapis -->
  <rect width="640" height="480" fill="url(#matLight)"/>
  <rect width="640" height="480" filter="url(#felt)" opacity=".85"/>

  <!-- glissières : bande blanche large sous l'asphalte, ombre portée -->
  <path d="TRACK" fill="none" stroke="url(#wall)" stroke-width="63"
        stroke-linecap="round" stroke-linejoin="round" filter="url(#wallShadow)"/>
  <!-- vibreurs rouge et blanc en bord de piste -->
  <path d="TRACK" fill="none" stroke="#c8352a" stroke-width="60"
        stroke-linecap="butt" stroke-dasharray="13 13" stroke-linejoin="round"/>
  <!-- asphalte -->
  <path d="TRACK" fill="none" stroke="url(#asphalt)" stroke-width="54"
        stroke-linecap="round" stroke-linejoin="round"/>
  <path d="TRACK" fill="none" stroke="#000" stroke-width="54" stroke-linecap="round"
        stroke-linejoin="round" filter="url(#grain)" opacity=".55"/>
  <!-- trace de gomme dans la corde -->
  <path d="TRACK" fill="none" stroke="#1c1f24" stroke-width="17"
        stroke-linecap="round" stroke-linejoin="round" opacity=".3"/>
  <!-- axe médian -->
  <path class="track-line" d="TRACK" fill="none" stroke="#e6e9ee" stroke-width="1.8"
        stroke-dasharray="10 13" stroke-linecap="round" opacity=".62"/>

  <!-- ligne de départ, damier -->
  <g transform="translate(120,300)">
    <rect x="-5" y="-27" width="10" height="54" fill="#f2f3f5"/>
    <rect x="-5" y="-27" width="5" height="9" fill="#15171b"/><rect x="0" y="-18" width="5" height="9" fill="#15171b"/>
    <rect x="-5" y="-9" width="5" height="9" fill="#15171b"/><rect x="0" y="0" width="5" height="9" fill="#15171b"/>
    <rect x="-5" y="9" width="5" height="9" fill="#15171b"/><rect x="0" y="18" width="5" height="9" fill="#15171b"/>
  </g>

  <g data-runner="trk" data-speed="114">CAR_O</g>
  <g data-runner="trk" data-speed="97">CAR_B</g>
  <g data-runner="trk" data-speed="85">CAR_Y</g>

  <!-- chemin invisible qui guide les voitures -->
  <path id="trk" d="TRACK" fill="none" stroke="none"/>

  <rect width="640" height="480" fill="url(#vig)" pointer-events="none"/>
  <text x="26" y="456" font-family="IBM Plex Mono, monospace" font-size="11.5"
        letter-spacing="3.4" fill="#8a929b">160 × 90 CM · TAPIS L · 10 VIRAGES</text>
</svg>"""
            .replace("TRACK", _TRACK_D)
            .replace("CAR_O", _car("O", "#8f2f0c", "#ffc9a3", "7"))
            .replace("CAR_B", _car("B", "#123c6e", "#b6dcff", "4"))
            .replace("CAR_Y", _car("Y", "#8a6a08", "#fff3c2", "2")))


PAGES = {}

# Les modules de pages importent les fragments ci-dessus : l'import se fait
# volontairement en fin de fichier pour éviter une dépendance circulaire.
from pages1 import P as _P1   # noqa: E402
from pages2 import P as _P2   # noqa: E402
from pages3 import P as _P3   # noqa: E402
from pages4 import P as _P4   # noqa: E402

for _mod in (_P1, _P2, _P3, _P4):
    PAGES.update(_mod)
