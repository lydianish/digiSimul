from PIL.Image import *


class Exception(Exception):
    def __init__(self, raison):
        self.raison = raison

    def __str__(self):
        return self.raison


def test(tab,x, y, taille_capteur_long, taille_capteur_hauteur, l, h):
    """
    Teste si le rectangle à découper dépasse l'image
    :param image: image à tester
    :param x: coordonnées de l'abscisse du pixel
    :param y: coordonnées de l'ordonnée du pixel
    :param taille_capteur_long: taille du capteur en longueur
    :param taille_capteur_hauteur: taille du capteur en hauteur
    :param l: taille en longueur en pixels de l'image de départ
    :param h: taille en hauteur en pixels de l'image de départ

    """
    if (x < 0 or y < 0 or taille_capteur_long <= 0 or taille_capteur_hauteur <= 0):
        raise Exception("Il faut des valeurs positives.")
    elif (l < x or h < y or l - x < taille_capteur_long  or h - y < taille_capteur_hauteur+1 ):
        raise Exception("Les valeurs sortent de l'image.")


def test007(tab, x, y, taille_capteur_long, taille_capteur_hauteur):
    """
    Teste si la partie à découper ne contient que du noir (il faut au moins 10 pixels de
     couleur pour que l'image soit affichée)
    :param tab: tableau numpy d'une image de départ
    :param x: coordonnées de l'abscisse du pixel
    :param y: coordonnées de l'ordonnée du pixel
    :param taille_capteur_long: taille du capteur en longueur
    :param taille_capteur_hauteur: taille du capteur en hauteur
    """
    i = x
    j = y
    e = 0
    while (i < x + taille_capteur_long and e < 10):
        a = tab[j, i]  # coin supG
        d = tab[j + taille_capteur_hauteur, i]  # coin infG
        if (a.all() == 0 and d.all() == 0):
            e = e
        else:
            e = e + 1
        i = i + 1
    i = x
    while (j < y + taille_capteur_hauteur and e < 10):
        a = tab[j, i]  # coin supG
        d = tab[j, i+ taille_capteur_long]
        if (a.all() == 0 and d.all() == 0):
            e = e
        else:
            e = e + 1
        j = j + 1
    if (e < 10):
        raise Exception("Aucune empreinte n'est détectée.")
