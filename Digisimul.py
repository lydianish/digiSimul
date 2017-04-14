import AjoutBruit
import Res_rot_dec
import Positionnement
import Préliminaire
from scipy import stats
import os
import numpy as np
import cv2
from PIL import Image

def modeliserImagesAutoPrecision(pathCapteur,pathBdd, nombre, nbPoint, largeur, longueur,ecartTypeX, ecartTypeY, ecartTypeAngle):
# Analyse du capteur :
    var,alpha,gama = AjoutBruit.anayseImageCapteur(pathCapteur)
#Determination des fonctions de probabilité type kernel :
    fctAlpha = stats.gaussian_kde(alpha)
    fctGama = stats.gaussian_kde(gama)

#Tirage d'une image de la bdd
    listeImage = os.listdir(pathBdd)
    nbImageBdd = len(listeImage)
    it = 1
    while it < nombre:
    #Selection d'une valeur de la loi kernel:
        alpha = fctAlpha.resample(1)
        gama = fctGama.resample(1)
    #tirage de l'image en Bdd
        tirage = np.random.uniform(0,nbImageBdd -1)
        imgTire = listeImage[int(tirage)]
    # Découpage de l'image


    #Ajout du bruit :
        pathIm = "%s\%s" % (pathBdd, imgTire)
        img = cv2.imread(pathIm)
        img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
        img = AjoutBruit.AjoutBruit(img, nbPoint,"gen",var,alpha,gama)
        Image.fromarray(img).show()
        it+=1


def modeliserImagesAutoRapide(pathBdd, nombre, nbPoint, var, largeur, longueur,ecartTypeX, ecartTypeY, ecartTypeAngle):
#Tirage d'une image de la bdd
    listeImage = os.listdir(pathBdd)
    nbImageBdd = len(listeImage)
    it = 1
    while it < nombre:
    #tirage de l'image en Bdd
        tirage = np.random.uniform(0,nbImageBdd -1)
        imgTire = listeImage[int(tirage)]
    # Découpage de l'image

    #Ajout du bruit :
        pathIm = "%s\%s" % (pathBdd, imgTire)
        img = cv2.imread(pathIm)
        img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
        img = AjoutBruit.AjoutBruit(img, nbPoint,"norm",var,alpha=None,gama=None)
        Image.fromarray(img).show()
        it+=1


def modeliserImagesManuelRapide(pathCapteur,pathBdd, nombre, nbPoint, largeur, longueur,ecartTypeX, ecartTypeY, ecartTypeAngle):
# Analyse du capteur :
    var,alpha,gama = AjoutBruit.anayseImageCapteur(pathCapteur)
#Determination des fonctions de probabilité type kernel :
    fctVar = stats.gaussian_kde(var)
#Tirage d'une image de la bdd
    listeImage = os.listdir(pathBdd)
    nbImageBdd = len(listeImage)
    it = 1
    while it < nombre:
    #Selection d'une valeur de la loi kernel:
        var = fctVar.resample(1)
    #tirage de l'image en Bdd
        tirage = np.random.uniform(0,nbImageBdd -1)
        imgTire = listeImage[int(tirage)]
    # Découpage de l'image

    #Ajout du bruit :
        pathIm = "%s\%s" % (pathBdd, imgTire)
        img = cv2.imread(pathIm)
        img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
        img = AjoutBruit.AjoutBruit(img, nbPoint,"norm",var,alpha,gama)
        Image.fromarray(img).show()
        it+=1


def modeliserImagesManuelPrecision(pathBdd, nombre, nbPoint, alpha, gama, largeur, longueur,ecartTypeX, ecartTypeY, ecartTypeAngle):
#Tirage d'une image de la bdd
    listeImage = os.listdir(pathBdd)
    nbImageBdd = len(listeImage)
    var = None
    it = 1
    while it < nombre:
    #tirage de l'image en Bdd
        tirage = np.random.uniform(0,nbImageBdd -1)
        imgTire = listeImage[int(tirage)]
    # Découpage de l'image


    #Ajout du bruit :
        pathIm = "%s\%s" % (pathBdd, imgTire)
        img = cv2.imread(pathIm)
        img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
        img = AjoutBruit.AjoutBruit(img, nbPoint,"gen",var,alpha,gama)
        Image.fromarray(img).show()
        it+=1

#main test
modeliserImagesAutoPrecision("C:/Users\polch_000\Desktop\ImagesEchographiques","C:/Users\polch_000\Desktop\imagesBdd",2,4,5,5,5,5,5)
