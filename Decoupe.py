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

rotdec('03_d_4.bmp',30,200,250,100,100)


