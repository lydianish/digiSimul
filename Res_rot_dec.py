
import cv2
from PIL.Image import *
import re

from Resolution import re_echantillonnage
from Rotation import rotation
from Decoupage import decoupe


def DonneNom(chemin):
    """
    
    :param chemin: chemin où se trouve l'image
    :return: le nom de l'image quand on lui donne un chemin
    """
    l = chemin.split("/")
    r = l[len(l) - 1]
    return r


class Res_rot_dec :

    # Methode qui renvoie l'image ayant subi un re-échantillonage, une rotation et un découpage
    # Donées :
    #   - chemin : chemin où se trouve l'image
    #   - ro:
    #   - rc:
    #   - angle :
    #   - (x,y)  :
    #   - taille du capteur: -taille_capteur_longueur
    #                        - taille_capteur_hauteur

    def ech_rot_dec(chemin,ro,rc,angle, x, y, taille_capteur_long, taille_capteur_hauteur):
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
        #recupere le nom de l'image
        nom_image = DonneNom(chemin)

        #echantillonnage & sauvegarde de l'image
        (im3) = re_echantillonnage(ro, rc, chemin)
        im3.save("resolution.png","PNG")
        im2 = cv2.imread('resolution.png', -2)

        #rotation et sauvegarde
        rot = rotation(im2, angle)
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
        a = "%s_angle%s" % (prefixe, angle)
        b = "%s_x%s" % (a, x)
        nom = "%s_y%s" % (b, y)
        ext = ".png"
        nom_complet = "%s%s" % (nom, ext)
        n.save(nom_complet, "PNG")
        os.remove('resolution.png')
        os.remove('rotation.jpg')

#test de la méthode
    # ech_rot_dec("/Users/Noemie/PycharmProjects/Projet/101_1.tif",500,200,0, 100, 200, 100, 100)
