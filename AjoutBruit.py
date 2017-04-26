import numpy as np
import math
from PIL import Image
from scipy import interpolate
from scipy import stats
from PIL import ImageOps
import cv2
import list
import threading
import os
# import pyopencl as cl
import multiprocessing

def echantillonageRect(npimage,nbPoint):
    """
    Echantillone l'image selon le ration du nombre de point que l'on veut garder
    
    :param npimage: Image à echantilloner en format numpy 
    :param nbPoint: Ratio des points que l'on veut garder : 1 sur nbpoint
    :return: Image echantillonée sous forme de tableau numpy 
    """
    longeur,largeur = npimage.shape
    y = 0
    while y < int(largeur/nbPoint):
        again = 1
        while again < nbPoint:
            npimage = np.delete(npimage,(y),axis=1)
            again += 1
        y += 1
    x = 0
    while x < int(longeur/nbPoint):
        again = 1
        while again < nbPoint:
            npimage = np.delete(npimage,(x),axis=0)
            again += 1
        x += 1
    return npimage


def ajoutSpeckelGenNorm(img, alpha, gamma):
    longeur,largeur = img.shape
    #matrices de vecteurs généralisation de loi gaussienne :
    matrixGauss = stats.gennorm.rvs(gamma,scale=alpha,loc=0,size=longeur*largeur).reshape(longeur, largeur)
    matrixGauss2 =  stats.gennorm.rvs(gamma,scale=alpha,loc=0,size=longeur*largeur).reshape(longeur, largeur)
    imgRetour = np.sqrt(img + 0j)
    imgRetour += (matrixGauss[:,:]) + (matrixGauss2[:,:]*1j)
    img = np.square(imgRetour.real) + np.square(imgRetour.imag)
    return img


def ajoutSpeckelGauss(img, ecartType):
    longueur,largeur = img.shape
    #matrices de vecteurs loi normal :
    matrixGauss =  ecartType * np.random.randn(longueur * largeur).reshape(longueur, largeur)
    matrixGauss2 = ecartType * np.random.randn(longueur * largeur).reshape(longueur, largeur)
    imgRetour = np.sqrt(img + 0j)
    imgRetour += (matrixGauss[:,:]) + (matrixGauss2[:,:]*1j)
    img = np.square(imgRetour.real) + np.square(imgRetour.imag)
    return img

def interpolation(img):
    """
    Interpolation bicubique
    :param img: Image à interpoler, sous forme de tableau numpy
    :return: Une fonction d'interpoaltion de l'image 
    """
    img = np.zeros(img.shape) + img
    l,L = img.shape
    x = np.arange(0,L,1)
    y = np.arange(0, l, 1)
    X,Y = np.meshgrid(x,y)
    fonctionInter = interpolate.interp2d(x,y,img, kind='cubic')
    return fonctionInter

def construireImageInterpelee(function,l,L,nbPoint):
    """
    Reconstruit une image grâce à une fonction d'interpolation de R² dans R 
    :param function: Une fonction de R² dans R 
    :param l: Longeur de l'image voulu 
    :param L: Largeur de l'image voulu 
    :param nbPoint: Nombre de point à interpoler 
    :return: Un tableau numpy bidimentionnel représentant une image 
    """
    x = np.arange(0, L/nbPoint,1/nbPoint)
    y = np.arange(0, l/nbPoint,1/nbPoint)
    img = function(x,y)
    return img


def anayseImageCapteur(path):
    """
    Analyse les paramètre du capteurs 
    :param path: 
    :return: Une liste de la variation des intensités des images, de Alpha, et de Gamma
    """
    listeImage = os.listdir(path)
    listVar = []
    listGama = []
    listAlpha = []
    for image in listeImage:
        #Lecture des images
        pathIm= "%s\%s"%(path,image)
        img = cv2.imread(pathIm,0)
        #Supprime les valeurs 0 et 255
        mask = np.logical_and(img != 0,img != 255)
        img = img[mask]
        #Calcul de  la variance, esperance, alpha et gama
        var = np.var(img)
        esp = np.mean(img)
        alpha = np.sqrt(np.square(math.pi) / (6 * var))
        gama = math.exp(alpha * (esp - math.log(2, 10) - 0.5772156 * ((1 / alpha) - 1)))
       #Ajout dans des valeurs dans une liste
        listVar.append(esp)
        listAlpha.append(alpha)
        listGama.append(gama)
    return listVar,listAlpha,listGama

def AjoutBruit(image,nbPoint, method,var,alpha,gama):
    """
    Fonction principale appelant les méthodes permettant d'ajouter un bruit de peckel à image de type optique
    
    :param image: Une image provenant de la bibliothèque "PIL Image" 
    :return: Un tableau bidimentionel numpy représentant une image 
    """
    if method == "gen":
        l,L = image.shape
        img = echantillonageRect(image,nbPoint)
        #Ajout du bruit :
        img4 = ajoutSpeckelGenNorm(img,alpha,gama)
        img5 = interpolation(img4)
        img6 = construireImageInterpelee(img5,l,L,nbPoint)
        return img6
    if method == "norm":
        l,L = image.shape
        img = echantillonageRect(image,nbPoint)
        #Ajout du bruit
        img4 = ajoutSpeckelGauss(img, np.sqrt(var))
        img5 = interpolation(img4)
        img6 = construireImageInterpelee(img5,l,L,nbPoint)
        return img6



def AjoutBruitMultiThreah():
    """
    Produit plusieurs threads permettant d'utiliser tous les coeurs, pour l'ajout du bruit de speckel 
    :return: Void
    """
    nbCore = multiprocessing.cpu_count()
    img = cv2.imread("images/fg1.bmp")
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    it = 0
    p = {}
    while it < nbCore:
        print(it)
        p[it] = threading.Thread(target=multipleImage,args=(img,))
        p[it].start()
        it += 1

def multipleImage(img):
    it = 0
    while it < 100:
        print(it)
        img2 = AjoutBruit(img, 2, "gen")
        it += 1
