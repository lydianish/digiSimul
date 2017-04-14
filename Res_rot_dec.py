
import cv2
from PIL.Image import *
import re

from Resolution import re_echantillonnage
from Rotation import rotation
from Decoupage import decoupe

#Methode qui renvoie le nom de l'image quand on lui donne un chemin
#Données :
#   - chemin : chemin où se trouve l'image

def DonneNom(chemin):
    l = chemin.split("/")
    r = l[len(l) - 1]
    return r


class Res_rot_dec :

    # Methode qui renvoie l'image ayant subi un re-échantillonage, une rotation et un découpage
    # Donées :
    #   - chemin : chemin où se trouve l'image
    #   - ro: resolutionOriginale (c'est la resolution de l'image originale dont le chemin est donne en parametre)
    #   - rc: resolutionCapteur (c'est la resolution finale)
    #   - angle : l'angle de rotation
    #   - (x,y)  : coordonnées du pixel en haut à gauche où l'on veut découper
    #   - taille du capteur: -taille_capteur_longueur
    #                        - taille_capteur_hauteur

    def ech_rot_dec(chemin,ro,rc,angle, x, y, taille_capteur_long, taille_capteur_hauteur):
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
        a = "%s _angle%s" % (prefixe, angle)
        b = "%s _x%s" % (a, x)
        nom = "%s _y%s" % (b, y)
        ext = ".png"
        nom_complet = "%s%s" % (nom, ext)
        n.save(nom_complet, "PNG")
        os.remove('resolution.png')
        os.remove('rotation.jpg')

#test de la méthode
    # ech_rot_dec("/Users/Noemie/PycharmProjects/Projet/101_1.tif",500,200,0, 100, 200, 100, 100)
