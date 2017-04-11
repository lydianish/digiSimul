from PIL import Image
def DonneNom(chemin):
    l=chemin.split("/")
    r=l[len(l)-1]
    return r
#Fonctions qui vont permettrent de calculer la taille en pixels, ou en pouce ou la resolution d'une image donee
#L'utilite de ces fonctions est qu'elles vont permettrent de calculer la nouvelle taille à donner en paramètres à rezize pour le changement de resolution

#------------------------------------------------------------------------
#Methode qui calcule la taille(largeur * hauteur) en pixels d'une image
#Donées :
#   - ro : la resolution de l'image
#   - d = (ld, hd) :dimensions physiques en pouces de l'image avec :
#           - ld = largeur en pouces
#           - hd = hauteur en pouces
#Remmarque : d est un tuple
#Containtes : ld et hd doivent etre exprimés en pouces

#Code :
def taille_en_pixels(ro, d):
    ld, hd = d
    lt = (int)(ld * ro)
    ht = (int)(hd * ro)
    return (lt,ht)

#Test de la methode :
#print(taille_en_pixels(500, (30,40)))

#------------------------------------------------------------------------
#Methode qui calcule la taille(largeur * hauteur) en pouce d'une image
#Donées :
#   - ro : la resolution de l'image
#   - t = (lt, ht) :dimensions en pixels (definition) de l'image avec :
#           - lt = largeur en pixels
#           - ht = hauteur en pixels
#Remmarque : t est un tuple
#Containtes : lt et ht doivent etre exprimés en pixels

#Code :
def taille_en_pouces(ro, t):
    lt, ht = t
    ld = lt / ro
    hd = ht / ro
    return (ld,hd)

#Test de la methode :
#1
#print(taille_en_pouces(500, (15000,20000)))

#2
#ro = 500
#rc = 400
#cheminf = "/Users/docteur/Desktop/L3/S2/Stage_Applicatif/Test_Photos/105_2.tif"
#i = Image.open(cheminf)
#d = taille_en_pouces(ro, i.size)
#print(d)
#t = taille_en_pixels(rc, d)
#print(t)
#i2 = (i.copy()).resize(t, Image.ANTIALIAS)
#i.show()
#i2.show()

#------------------------------------------------------------------------
#Methode qui calcule la resolution d'une image
#Donées :
#   - t = (lt, ht) :dimensions en pixels (definition) de l'image avec :
#           - lt = largeur en pixels
#           - ht = hauteur en pixels
#   - d = (ld, hd) :dimensions physiques en pouces de l'image avec :
#           - ld = largeur en pouces
#           - hd = hauteur en pouces
#Remmarque : t et d sont des tuples
#Containtes :   - lt et ht doivent etre exprimés en pixels
#               - ld et hd doivent etre exprimés en pouces

#Code :
def resolution(t, d):
    lt, ht = t
    ld, hd = d
    ro = lt//ld
    return ro

#Test de la methode :
#print(resolution((15000,20000), (30,40)))


# ----------------------------------------------------------------------------
# Methode qui sous-echantillonne l'image dont le chemin est donne en parametre
# Renvoie une copie de l'image sous-echantillonnee (avec une resolution rc)
# Données :
#       - ro : resolutionOriginale (c'est la resolution de l'image originale dont le chemin est donne en parametre)
#       - rc : resolutionCapteur (c'est la resolution finale)
#       - chemin : chemin vers l'image a re-echantillonner
#Contrainte : ro > rc

#Code :
def sous_echantillonnage(ro, rc, chemin):
    if(ro <= rc):
        print("Erreur de sous_echantillonnage, ro doit etre strictement plus grand que rc")
        return
    else:
        print("Vous etes dans Sous-echantillonnage")
        imageOriginale = Image.open(chemin)
        imOCopie = imageOriginale.copy()
        print("taille initiale", imOCopie.size)
        #Calcul des dimensions de l'image
        d = taille_en_pouces(ro, imOCopie.size)
        print("dimension", d)
        #Calcul de la nouvelle de l'image pour la resolution rc
        t = taille_en_pixels(rc, d)
        print("nouvelle taille", t)
        #sous-echantillonnage
        im = (imOCopie.copy()).resize(t, Image.ANTIALIAS)
        return im

# Test de la methode :
#ro = 500
#rc = 200
#cheminf = "/Users/docteur/Desktop/L3/S2/Stage_Applicatif/Test_Photos/105_2.tif"
#i = Image.open(cheminf)
#im1 = sous_echantillonnage(ro, rc, cheminf)
#i.show()
#im1.show()



# ----------------------------------------------------------------------------
# Methode qui sur-echantillonne l'image dont le chemin est donne en parametre
# Renvoie une copie de l'image sur-echantillonnee (avec une resolution rc)
# Données :
#       - ro : resolutionOriginale (c'est la resolution de l'image originale dont le chemin est donne en parametre)
#       - rc : resolutionCapteur (c'est la resolution finale)
#       - chemin : chemin vers l'image a re-echantillonner
# Contrainte : ro < rc

#Code :
def sur_echantillonnage(ro, rc, chemin):
    if (ro >= rc):
        print("Erreur de sur_echantillonnage, ro doit etre strictement plus petit que rc")
        return
    else:
        print("Vous etes dans Sur-echantillonnage")
        imageOriginale = Image.open(chemin)
        imOCopie = imageOriginale.copy()
        print("taille initiale", imOCopie.size)
        #Calcul des dimensions de l'image
        d = taille_en_pouces(ro, imOCopie.size)
        print("dimension", d)
        #Calcul de la nouvelle de l'image pour la resolution rc
        t = taille_en_pixels(rc, d)
        print("nouvelle taille", t)
        #sous-echantillonnage
        im = (imOCopie.copy()).resize(t, Image.ANTIALIAS)
        return im

# Test de la methode :
#ro = 500
#rc = 600
#cheminf = "/Users/docteur/Desktop/L3/S2/Stage_Applicatif/Test_Photos/105_2.tif"
#i = Image.open(cheminf)
#im2 = sur_echantillonnage(ro, rc, cheminf)
#i.show()
#im2.show()

# ----------------------------------------------------------------------------
# Methode qui re-echantillonne l'image dont le chemin est donne en parametre
# Renvoie une copie de l'image re-echantillonnee (avec une resolution rc)
# Données :
#       - ro : resolutionOriginale (c'est la resolution de l'image originale dont le chemin est donne en parametre)
#       - rc : resolutionCapteur (c'est la resolution finale)
#       - chemin : chemin vers l'image a re-echantillonner
#Contrainte : nulle

#Code :
def re_echantillonnage(ro, rc, chemin):
    if(ro > rc):                             #l 'image originale  une resolution plus grande que celle du capteur
        im = sous_echantillonnage(ro, rc, chemin)
        im.save("reechant.png","PNG")
        nom = DonneNom(chemin)
        print("nom", nom)
        return im,nom
    elif(ro < rc):                           #l 'image originale  une resolution plus petite que celle du capteur
        im = sur_echantillonnage(ro, rc, chemin)
        im.save("reechant.png","PNG")
        nom = DonneNom(chemin)
        print("nom", nom)
        return im,nom
    else:                                    #l 'image originale  une resolution egale a celle du capteur
        print("Vous etes dans Re-echantillonnage:\nro = rc --> rien à faire")
        imageOriginale = Image.open(chemin)
        imOCopie = imageOriginale.copy()
        print("taille initiale = finale ", imOCopie.size)
        imOCopie.save("reechant.png","PNG")
        nom = DonneNom(chemin)
        print("nom",nom)
        return (imOCopie,nom)

# Test de la methode :
ro = 500
rc = 200
cheminf = "/Users/Noemie/PycharmProjects/Projet/101_1.tif"
i = Image.open(cheminf)
# print(re_echantillonnage(ro, rc, cheminf))
(im3,nom) = re_echantillonnage(ro, rc, cheminf)

# i.show()
# im3.show()



import numpy as np
import cv2
from PIL.Image import *
import re

from MyException import MyException, test,test007


def rotate_boundredef(image, angle):
    #Cette méthode renvoie une image qui a subi une rotation de angle degre ainsi que les positions des coin de la nouvelle image
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)

    M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])

    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))

    M[0,2] =M[0, 2]+ (nW / 2) - cX
    M[1,2] =M[1, 2]+ (nH / 2) - cY

    imagefinale=cv2.warpAffine(image, M, (nW, nH))
    (h1, w1) = imagefinale.shape[:2]
    xhaut=M[0,2]
    xbas= w1-xhaut
    ydroite= xhaut/np.tan(angle*np.pi/180)
    ygauche = h1-ydroite
    return (imagefinale,round(xhaut,0),round(xbas,0),round(ydroite,0),round(ygauche,0))

def decoupe(image,x,y,taille_capteur_long,taille_capteur_hauteur,xh,xb,yd,yg):
    #Cette méthode renvoie une image découpée à partir des coordonnées (x,y) ainsi que la taille du capteur
    try :
        test(image,x,y,taille_capteur_long,taille_capteur_hauteur)
        test007(image, x, y, taille_capteur_long, taille_capteur_hauteur)
        box = (x, y, x+taille_capteur_long, y+taille_capteur_hauteur)
        coupe = image.crop(box)
        Image.show(coupe)
        return (coupe)
    except MyException as e:
        print(e)
        exit()



def rotdec (nom_image,angle,x,y,taille_capteur_long,taille_capteur_hauteur):
    #Cette méthode effectue à la fois la rotation et le découpage
    m = re.search('[^.]*', nom_image)
    prefixe=m.group(0)

    im2 = cv2.imread(nom_image, -2)

    rot, xh, xb, yd, yg = rotate_boundredef(im2, angle)  # ou rotated = rotate_b(im, angle)
    ima = open('rotok.jpg')

    n = decoupe(ima, x, y, taille_capteur_long, taille_capteur_hauteur,xh,xb,yd,yg)
    #format d'enregistrement: nom_angle_x_y
    a = "%s _angle%s" % (prefixe,angle)
    b= "%s _x%s" % (a,x)
    nom="%s _y%s" % (b,y)
    ext = ".png"
    nom_complet = "%s%s" % (nom, ext)
    n.save(nom_complet, "PNG")



rotdec(nom,30,200,250,100,100)
#im2 = cv2.imread(im3, -2)

