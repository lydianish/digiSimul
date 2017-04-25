import cv2
import numpy as np
from PIL.Image import *
import re

from Resolution import re_echantillonnage
from Rotation import rotation
from Decoupage import decoupe


def ech_rot_dec(image, ro, rc, angle, x, y, taille_capteur_long, taille_capteur_hauteur):
    """
    :param chemin: chemin où se trouve l'image
    :param ro: resolutionOriginale (c'est la resolution de l'image originale dont le chemin est donne en parametre)
    :param rc: resolutionCapteur (c'est la resolution finale)
    :param angle: l'angle de rotation
    :param x: coordonnées de l'abscisse du pixel en haut à gauche où l'on veut découper
    :param y: coordonnées de l'ordonné du pixel en haut à gauche où l'on veut découper
    :param taille_capteur_long: taille du capteur en longueur
    :param taille_capteur_hauteur: taille du capteur en hauteur
    :return: l'image ayant subi un re-échantillonage, une rotation et un découpage
    """
    # taille de l'image

    im = open(image)
    tl,th=im.size

    # echantillonnage & sauvegarde de l'image
    (im3) = re_echantillonnage(ro, rc, im)
    im3.save("resolution.png", "PNG")
    im2 = cv2.imread('resolution.png', -2)

    # rotation et sauvegarde
    rot = rotation(im2, angle)

    # Nouvelles valeurs de x, y , taille_capteur
    hautmin, longmin = rot.shape[:2]
    xnouv = x * longmin / tl
    ynouv = y * hautmin / th
    tcl = taille_capteur_hauteur * hautmin / th
    tch = taille_capteur_long * longmin / tl

    #Passer d'une image à un tableau numpy
    tab = np.array(rot)
    h, l = tab.shape[:2]
    # découpage
    n = decoupe(tab, round(xnouv), round(ynouv), round(tcl), round(tch),l,h)
    
    # format d'enregistrement: nom_angle_x_y
    # m = re.search('[^.]*', image)
    # prefixe = m.group(0)
    # a = "%s_angle%s" % (prefixe, angle)
    # b = "%s_x%s" % (a, x)
    # nom = "%s_y%s" % (b, y)
    # ext = ".png"
    # nom_complet = "%s%s" % (nom, ext)
    # n.save(nom_complet, "PNG")
    os.remove('resolution.png')

# test de la méthode
ech_rot_dec('03_d_1.bmp', 500, 200, 0, 120, 278, 200, 200)
