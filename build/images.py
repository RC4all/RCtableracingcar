#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Optimise les photos du dossier Images/ vers site/img/photos/.

Pour chaque visuel : dédoublonnage, recadrage centré au ratio voulu,
redimensionnement (jamais d'agrandissement), export WebP + JPEG de repli.

    python3 images.py
"""
import os, hashlib
from PIL import Image, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.normpath(os.path.join(HERE, "..", "Images"))
DST = os.path.normpath(os.path.join(HERE, "..", "site", "img", "photos"))

# nom de sortie -> (fichier source, ratio cible ou None, largeur max)
PLAN = {
    # --- photos réelles -----------------------------------------------------
    "grille-depart-tapis":      ("depart rc 1-76.webp",                 16/9,  1023),
    "grille-depart-carre":      ("depart rc 1-76.webp",                 4/3,   1023),
    "echelle-dans-la-main":     ("mini-size.webp",                      None,   900),
    "soiree-course-table":      ("tableracingparis-1.webp",             4/3,    900),
    "soiree-course-large":      ("tableracingparis-1.webp",             16/9,   900),
    "circuit-maison-80x120":    ("circuit-perso-80x120-1.webp",         None,   768),
    "carrosseries-led":         ("3-carro.webp",                        None,  1000),
    # --- modèles ------------------------------------------------------------
    "gamme-c71-c75":            ("tr-c71-76.webp",                      None,  1024),
    "c78-rallye":               ("tr-c78-1.webp",                       None,   900),
    "c66-drift":                ("tr-c66-1-edited.webp",                None,  1114),
    "c76-avant":                ("capture-decran-2026-07-26-a-01.26.17-1-edited.webp", None, 780),
    "c76-avant-large":          ("capture-decran-2026-07-26-a-01.26.17-1-edited.webp", 16/9, 780),
    # --- radiocommande ------------------------------------------------------
    "radio-annotee":            ("radio-boutons.webp",                  None,  1000),
    "radio-p32s":               ("radio-p32s.webp",                     None,   913),
    "radio-a82s":               ("capture-decran-2026-07-25-a-19.11.23.webp", None, 1000),
    # --- châssis (vues éclatées constructeur) -------------------------------
    "chassis-vue-eclatee":      ("fiche-chassis.webp",                  None,   768),
    "chassis-electronique":     ("fiche-chassis-2.webp",                None,   618),
    "direction-vue-eclatee":    ("fiche-direction.webp",                None,   634),
    "transmission-vue-eclatee": ("fiche-entrainement.webp",             None,   637),
    "chassis-eclairage-led":    ("capture-decran-2026-07-25-a-18.48.07.webp", None, 900),
    # --- plans de tapis -----------------------------------------------------
    "tapis-turbo-racing-s":     ("track-tr-s.webp",                     None,  1000),
    "tapis-turbo-racing-l":     ("capture-decran-2026-07-25-a-23.56.12.webp", None, 1023),
    "tapis-turbo-racing-xl":    ("capture-decran-2026-07-25-a-18.56.15.webp", None, 1024),
    "tapis-ldarc-1609a":        ("capture-decran-2026-07-25-a-18.59.37.webp", None, 1024),
    "tapis-ldarc-2412a":        ("capture-decran-2026-07-25-a-18.59.03.webp", None, 1023),
}

# Volontairement écartées : voir le compte rendu.
IGNOREES = {
    "capture-decran-2026-07-25-a-19.45.43.webp":
        "capture d'une fiche produit de place de marché (prix, boutons d'achat) — "
        "incompatible avec l'indépendance affichée du site",
}


def crop_to_ratio(im, ratio):
    """Recadrage centré au ratio demandé, sans déformation."""
    if ratio is None:
        return im
    w, h = im.size
    if w / h > ratio:                     # trop large : on rogne les côtés
        nw = int(round(h * ratio))
        left = (w - nw) // 2
        return im.crop((left, 0, left + nw, h))
    nh = int(round(w / ratio))            # trop haut : on rogne haut et bas
    top = int((h - nh) * 0.42)            # légèrement au-dessus du centre
    return im.crop((0, top, w, top + nh))


def main():
    os.makedirs(DST, exist_ok=True)
    seen, total_in, total_out, rows = {}, 0, 0, []

    for name, (src, ratio, maxw) in sorted(PLAN.items()):
        path = os.path.join(SRC, src)
        if not os.path.exists(path):
            print("  MANQUANT :", src); continue

        digest = hashlib.md5(open(path, "rb").read()).hexdigest()
        seen.setdefault(digest, src)

        im = Image.open(path)
        im = ImageOps.exif_transpose(im).convert("RGB")
        im = crop_to_ratio(im, ratio)
        if im.width > maxw:
            im = im.resize((maxw, round(im.height * maxw / im.width)), Image.LANCZOS)

        wp = os.path.join(DST, name + ".webp")
        jp = os.path.join(DST, name + ".jpg")
        im.save(wp, "WEBP", quality=84, method=6)
        im.save(jp, "JPEG", quality=82, optimize=True, progressive=True)

        size_in = os.path.getsize(path)
        size_out = os.path.getsize(wp)
        total_in += size_in; total_out += size_out
        rows.append((name, im.width, im.height, size_out // 1024))

    for n, w, h, k in rows:
        print(f"  {n:<26} {w:>5}x{h:<5} {k:>4} Ko")

    # doublons parfaits repérés dans la source
    by_hash = {}
    for f in os.listdir(SRC):
        p = os.path.join(SRC, f)
        if os.path.isfile(p):
            by_hash.setdefault(hashlib.md5(open(p, "rb").read()).hexdigest(), []).append(f)
    dups = [v for v in by_hash.values() if len(v) > 1]

    print(f"\n{len(rows)} visuels produits · {total_out/1024:.0f} Ko en WebP "
          f"(sources : {total_in/1024:.0f} Ko)")
    if dups:
        print("Doublons dans Images/ (un seul conservé) :")
        for d in dups:
            print("   ", " = ".join(d))
    if IGNOREES:
        print("Écartées :")
        for f, why in IGNOREES.items():
            print(f"    {f}\n      → {why}")


if __name__ == "__main__":
    main()
