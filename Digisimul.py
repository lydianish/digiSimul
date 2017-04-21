import AjoutBruit
import Res_rot_dec
import Positionnement
import Préliminaire
from scipy import stats
import os
import numpy as np
import cv2
from PIL import Image
import multiprocessing
import threading

def modeliserImagesAutoPrecision(pathBdd, nombre, nbPoint, drfAlpha, drfGama, largeur, longueur,ecartTypeX, ecartTypeY, ecartTypeAngle):
#Tirage d'une image de la bdd
    listeImage = os.listdir(pathBdd)
    nbImageBdd = len(listeImage)
    it = 1
    while it < nombre:
    #Selection d'une valeur de la loi kernel:
        alpha = drfAlpha.resample(1)
        gama = drfGama.resample(1)
    #tirage de l'image en Bdd
        tirage = np.random.uniform(0,nbImageBdd -1)
        imgTire = listeImage[int(tirage)]
    # Découpage de l'image

        var = None
    #Ajout du bruit :
        pathIm = "%s\%s" % (pathBdd, imgTire)
        img = cv2.imread(pathIm)
        img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
        img = AjoutBruit.AjoutBruit(img, nbPoint,"gen",var,alpha,gama)
        Image.fromarray(img).show()
        it+=1


def modeliserImagesAutoRapide(pathBdd, nombre, nbPoint, drfVar, largeur, longueur,ecartTypeX, ecartTypeY, ecartTypeAngle):
#Tirage d'une image de la bdd
    listeImage = os.listdir(pathBdd)
    nbImageBdd = len(listeImage)
    it = 1
    while it < nombre:
    #Selection d'une valeur de la loi kernel:
        var = drfVar.resample(1)
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


def modeliserImagesAutoPrecisionMultithread(pathCapteur, pathBdd, nombre, nbPoint, largeur, longueur, ecartTypeX, ecartTypeY, ecartTypeAngle):
# Analyse du capteur :
    var, alpha, gama = AjoutBruit.anayseImageCapteur(pathCapteur)
# Determination des fonctions de probabilité type kernel :
    drfAlpha = stats.gaussian_kde(alpha)
    drfGama = stats.gaussian_kde(gama)
    nbCore = multiprocessing.cpu_count()-1
    nombre2 = nombre/nbCore #
    it = 1
    p = {}
    while it < nbCore:
        p[it]= threading.Thread(target=modeliserImagesAutoPrecision,args=(pathBdd, nombre2, nbPoint, drfAlpha, drfGama, largeur, longueur,ecartTypeX, ecartTypeY, ecartTypeAngle) )
        p[it].start()
        it += 1


def modeliserImagesAutoRapideMultithread(pathCapteur, pathBdd, nombre, nbPoint, largeur, longueur, ecartTypeX, ecartTypeY, ecartTypeAngle):
# Analyse du capteur :
    var, alpha, gama = AjoutBruit.anayseImageCapteur(pathCapteur)
# Determination des fonctions de probabilité type kernel :
    drfVar = stats.gaussian_kde(var)
    nbCore = multiprocessing.cpu_count()-1
    nombre2 = nombre/nbCore #
    it = 1
    p = {}
    while it < nbCore:
        p[it]= threading.Thread(target=modeliserImagesAutoRapide, args=(pathBdd, nombre2, nbPoint, drfVar, largeur, longueur,ecartTypeX, ecartTypeY, ecartTypeAngle) )
        p[it].start()
        it += 1



#main test
modeliserImagesAutoPrecision("C:/Users\polch_000\Desktop\ImagesEchographiques","C:/Users\polch_000\Desktop\imagesBdd",2,4,5,5,5,5,5)
