
import cv2
from PIL.Image import *
import re

from Resolution import re_echantillonnage
from Rotation import rotation
from Decoupage import decoupe


def DonneNom(chemin):
    l = chemin.split("/")
    r = l[len(l) - 1]
    return r


class Res_rot_dec :

    def rotdec(angle, x, y, taille_capteur_long, taille_capteur_hauteur,chemin,ro,rc):
        #recupere le nom de l'image
        nom_image = DonneNom(chemin)

        #echantillonnage & sauvegarde de l'image
        (im3) = re_echantillonnage(ro, rc, chemin)
        im3.save("resolution.png","PNG")
        im2 = cv2.imread('resolution.png', -2)

        #rotation et sauvegarde
        rot = rotation(im2, angle)  # ou rotated = rotate_b(im, angle)
        cv2.imwrite('rotation.jpg', rot)
        ima = open('rotation.jpg')

        #Nouvelles valeurs de x, y , taille_capteur
        hautmin, longmin = ima.size
        lim = open(nom_image)
        hautmax, longmax = lim.size
        xnouv = x * longmin / longmax
        ynouv = y * hautmin / hautmax
        tcl = taille_capteur_hauteur * hautmin / hautmax
        tch = taille_capteur_long * longmin / longmax

        #découpage
        n = decoupe(ima, xnouv, ynouv, tcl, tch)

        # format d'enregistrement: nom_angle_x_y
        m = re.search('[^.]*', nom_image)
        prefixe = m.group(0)
        a = "%s _angle%s" % (prefixe, angle)
        b = "%s _x%s" % (a, x)
        nom = "%s _y%s" % (b, y)
        ext = ".png"
        nom_complet = "%s%s" % (nom, ext)
        n.save(nom_complet, "PNG")
        os.remove('resolution.png')
        os.remove('rotation.jpg')

    rotdec(0, 100, 200, 100, 100,"/Users/Noemie/PycharmProjects/Projet/101_1.tif",500,200)
