import cv2
import numpy as np
from PIL import Image
import re

from Rotation import rotation
from Decoupage import decoupe


def ech_rot_dec(image, angle, x, y, taille_capteur_long, taille_capteur_hauteur,tl,th):
    """
    :param chemin: chemin où se trouve l'image
    :param angle: l'angle de rotation
    :param x: coordonnées de l'abscisse du pixel en haut à gauche où l'on veut découper
    :param y: coordonnées de l'ordonné du pixel en haut à gauche où l'on veut découper
    :param taille_capteur_long: taille du capteur en longueur
    :param taille_capteur_hauteur: taille du capteur en hauteur
    :return: l'image ayant subi un re-échantillonage, une rotation et un découpage
    """



    rot = rotation(image, angle,tl,th)


    # Nouvelles valeurs de x, y , taille_capteur
    hautmin, longmin = rot.shape[:2]
    xnouv = x * longmin / tl
    ynouv = y * hautmin / th
    tcl = taille_capteur_hauteur * hautmin / th
    tch = taille_capteur_long * longmin / tl

    # Passer d'une image à un tableau numpy
    tab = np.array(rot)
    h, l = tab.shape[:2]
    # découpage
    n = decoupe(tab, round(xnouv), round(ynouv), round(tcl), round(tch), l, h)
    return n

