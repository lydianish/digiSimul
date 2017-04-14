import AjoutBruit
import Decoupe
import Positionnement
import Préliminaire
from scipy import stats
import os
import numpy as np
import cv2
from PIL import Image

def modeliserImagesAutoPrecision(pathCapteur,pathBdd, nombre, ecartTypeX, ecartTypeY, ecartTypeAngle):
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
    #Ajout du bruit :
        pathIm = "%s\%s" % (pathBdd, imgTire)
        img = cv2.imread(pathIm)
        img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
        img = AjoutBruit.AjoutBruit(img, 4,"gen",var,alpha,gama)
        Image.fromarray(img).show()
        it+=1





#main test
modeliserImagesAutoPrecision("C:/Users\polch_000\Desktop\ImagesEchographiques","C:/Users\polch_000\Desktop\imagesBdd",2,5,5,5)
