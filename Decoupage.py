from PIL.Image import *
from Exception import Exception, test, test007
import numpy as np


def decoupe(tab, x, y, taille_capteur_long, taille_capteur_hauteur,tl,th):
    """

    :param tab: tableau numpy d'une image
    :param x: coordonnée de l' abscisse du pixel en haut à gauche où l'on veut découper
    :param y: coordonnée de  l' ordonnée du pixel en haut à gauche où l'on veut découper
    :param taille_capteur_long: taille de capteur en longueur
    :param taille_capteur_hauteur: taille du capteur en hauteur
    :param tl: taille en longueur du tableau
    :param th: taille en hauteur du tableau
    :return: une image découpée, renvoie une exception si (x,y) n'appartiennent pas à l'image ou
            si la partie à découper ne contient que du noir
    """
    try:
        test(tab,x, y, taille_capteur_long, taille_capteur_hauteur,tl,th)
        test007(tab, x, y, taille_capteur_long, taille_capteur_hauteur)
        coupe= tab[y:y+taille_capteur_hauteur,x:x+taille_capteur_long]
        return(coupe)
    except Exception as e:
        print(e)
        exit()



