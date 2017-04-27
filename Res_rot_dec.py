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
    :param tl: taille en longueur de l'image de départ
    :param th: taille en hauteur de l'image de départ
    :return: l'image ayant subi un re-échantillonage, une rotation et un découpage
    """



    rot = rotation(image, angle,tl,th)


    # Passer d'une image à un tableau numpy
    tab = np.array(rot)
    h, l = tab.shape[:2]
    # découpage
    tabnumpy = decoupe(tab, x, y, taille_capteur_long, taille_capteur_hauteur,l,h)
    if(taille_capteur_hauteur%2==0):
        tabnumpy = tabnumpy[:, 0:taille_capteur_long - 1]
    if(taille_capteur_long%2==0):
        tabnumpy = tabnumpy[0:taille_capteur_hauteur-1,:]
    return tabnumpy

