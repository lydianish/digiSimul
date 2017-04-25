import AjoutBruit
import Res_rot_dec
import LoisPositionnement
from scipy import stats
import Images
import os
import numpy as np
import cv2
from PIL import Image
import multiprocessing
import threading
import Res_rot_dec
import Resolution

nombreImagesGen = 0

def modeliserImage(pathBdd, pathSave, nomImages, nombreImages, nbPoints,resolutionOriginal, resolutionCapteur, largeur, longueur, var, alpha, gama,minX,maxX,minY,maxY,minAngle,maxAngle, methode):
    global nombreImagesGen
    itImage = 0
    numeroImage = 0
    reste = nombreImages % len(nomImages)
    # pour chaque image
    while itImage < len(nomImages):

        #Ouverture de l'image
        pathIm = "%s\%s" % (pathBdd, nomImages[numeroImage])
        img = cv2.imread(pathIm,-1)
        tailleImageX,tailleImageY = img.shape
        print(tailleImageX,tailleImageY)
    # Sous-résolution
    #     img  = Resolution.re_echantillonnage(resolutionOriginal,resolutionCapteur,img)

        nombreImagesTmp = nombreImages // len(nomImages)
        if (reste > 0):
            nombreImagesTmp += 1
            reste -= 1
        print("nombreImagesparImagesParCoeur %s"%nombreImagesTmp)
        it = 0
        while it <= nombreImagesTmp:
        # Découpage et rotation de l'image
            (x,y,theta) = LoisPositionnement.unePosition(minX,maxX,minY,maxY,minAngle,maxAngle)
            img = Res_rot_dec.ech_rot_dec(img, theta, x, y, largeur, longueur,tailleImageY,tailleImageX)
            print("shape %s" %img.size)
        # Ajout du bruit:
            img = AjoutBruit.AjoutBruit(img, nbPoints, methode, var, alpha, gama)
            it += 1
            # Image.fromarray(img).show()
            nombreImagesGen += 1
            Image.fromarray(img).save("%s/%s%s%s.gif" %(pathSave,nomImages[numeroImage],it,nombreImagesGen))
            #TODO enregistrer l'image

        print(nombreImagesGen)
        itImage += 1
    return img


def modeliserImagesMultithread(pathCapteur, pathBdd, pathSave, nombreImages, nbPoints, resolutionOriginal, resolutionCapteur, largeur, longueur, minX,maxX,minY,maxY,minAngle,maxAngle, analyse = False ,methodeLente = False, var = None, alpha = None, gama = None ,coeursLibres = 1 ):

    if analyse == True:
        # Analyse du capteur :
        var, alpha, gama = AjoutBruit.anayseImageCapteur(pathCapteur)
        if methodeLente == True:
            # Determination des fonctions de probabilité type kernel :
            drfVar = stats.gaussian_kde(var)
        if methodeLente == False:
            drfAlpha = stats.gaussian_kde(alpha)
            drfGama = stats.gaussian_kde(gama)



    listeImage = os.listdir(pathBdd)
    nbCore = multiprocessing.cpu_count() - coeursLibres

    listeImageCut = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    index = -1
    #Repartition des images par coeur
    print('nbCore: %s'%(nbCore))
    while index < len(listeImage)-1:
        index += 1
        listeImageCut[index % nbCore].append(listeImage[index])

     #Création et lancements des processus
    it = 0
    processus = {}

    reste = nombreImages % nbCore
    while it < nbCore:
        nombreImagesCore = (nombreImages // nbCore)
        if (reste > 0):
            nombreImagesCore += 1
            reste -= 1
        print("nbImgCore %s"%nombreImagesCore)
        processus[it]= threading.Thread(target=modeliserImage, args=(pathBdd, pathSave,listeImageCut[it], nombreImagesCore, nbPoints,resolutionOriginal, resolutionCapteur, largeur, longueur, var, alpha, gama,minX,maxX,minY,maxY,minAngle,maxAngle,"norm"))
        processus[it].start()
        it += 1

#main test

pathCapteur =  "C:/Users\polch_000\Desktop\ImagesEchographiques"
pathBdd = "C:/Users\polch_000\Desktop\imagesBdd"
pathSave = "C:/Users\polch_000\Desktop\imagesRes"
nombreImages = 100
nbPoints = 6
resolutionOriginal = 200
resolutionCapteur = 100
largeur = 50
longueur = 50
minX,maxX,minY,maxY,minAngle,maxAngle = 0,100,0,100,0,360
analyse = False
methodeLente = False
var = 5
alpha = 1.8
gama = 6
coeursLibres = 6
modeliserImagesMultithread( pathCapteur, pathBdd, pathSave,nombreImages, nbPoints, resolutionOriginal, resolutionCapteur, largeur, longueur, minX,maxX,minY,maxY,minAngle,maxAngle, analyse,methodeLente, var, alpha , gama  ,coeursLibres)