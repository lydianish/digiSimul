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
    matrixGauss = stats.gennorm.rvs(gamma,scale=alpha,loc=0,size=longeur*longeur).reshape(longeur, largeur)
    matrixGauss2 =  stats.gennorm.rvs(gamma,scale=alpha,loc=0,size=longeur*longeur).reshape(longeur, largeur)
    imgRetour = np.sqrt(img + 0j)
    imgRetour += (matrixGauss[:,:]) + (matrixGauss2[:,:]*1j)
    img = np.square(imgRetour.real) + np.square(imgRetour.imag)
    return img


def ajoutSpeckelGauss(img, ecartType):
    longeur,largeur = img.shape
    #matrices de vecteurs loi normal :
    matrixGauss =  ecartType + np.random.randn(longeur * largeur).reshape(longeur, largeur)
    matrixGauss2 = ecartType + np.random.randn(longeur * largeur).reshape(longeur, largeur)
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
    x = np.arange(0,l,1)
    y = np.arange(0, L, 1)
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
    x = np.arange(0, l/nbPoint,1/nbPoint)
    y = np.arange(0, L/nbPoint,1/nbPoint)
    img = function(x,y)
    return img


def anayseImageCapteur(path):
    """
    Analyse les paramètre du capteurs 
    :param path: 
    :return: Une liste de la variation des intensités des images, de Alpha, et de Gamma
    """
    listPx = [0]
    listeImage = os.listdir(path)
    listVar = []
    listGama = []
    listAlpha = []
    for image in listeImage:
        pathIm= "%s\%s"%(path,image)
        print(pathIm)
        img = cv2.imread(pathIm,1)
        #Supprime les valeurs 0 et 255
        mask = np.logical_and(img != 0,img != 255)
        img = img[mask]
        var = np.var(img)
        esp = np.mean(img)
        alpha = np.sqrt(np.square(math.pi) / (6 * var))
        gama = math.exp(alpha * (esp - math.log(2, 10) - 0.5772156 * ((1 / alpha) - 1)))
        listVar.append(esp)
        listAlpha.append(alpha)
        listGama.append(gama)
    print(listVar,listAlpha,listGama)


def AjoutBruit(image):
    """
    Fonction principale appelant les méthodes permettant d'ajouter un bruit de peckel à image de type optique
    
    :param image: Une image provenant de la bibliothèque "PIL Image" 
    :return: Un tableau bidimentionel numpy représentant une image 
    """
    # conversion de l'image en array numpy
    nbPoint = 2
    l,L = image.shape
    img = echantillonageRect(image,nbPoint)
    img4 = ajoutSpeckelGenNorm(img,1.8,8)
    img5 = interpolation(img4)
    img5 = construireImageInterpelee(img5,l,L,nbPoint)
    return img5



def AjoutBruitMultiThreah():
    """
    Produit plusieurs threads permettant d'utiliser tous les coeurs pour l'ajout du bruit de speckel 
    :return: Void
    """
    img = cv2.imread("images/vador.bmp")
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    t1 = threading.Thread(target=multipleImage,args=(img,1))
    t2 = threading.Thread(target=multipleImage,args=(img,2))
    t3 = threading.Thread(target=multipleImage,args=(img,3))
    t4 = threading.Thread(target=multipleImage,args=(img,4))
    t5 = threading.Thread(target=multipleImage,args=(img,5))
    t6 = threading.Thread(target=multipleImage,args=(img,6))
    t7 = threading.Thread(target=multipleImage,args=(img,7))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    return 0;

def multipleImage(img,p):
    it = 0
    while it < 10:
        print(it)
        img2 = AjoutBruit(img)
        img3 = Image.fromarray(img2).\
         save("imgT1It%sP%s"%(it,p),"gif")
        it += 1



# MAIN
anayseImageCapteur("C:/Users\polch_000\Desktop\ImagesEchographiques")


# img = cv2.imread("images/fg1.bmp")
# img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
# AjoutBruit(img)
# Image.fromarray(img).show()


# # GPU
# # creer un contexte
# myContext = cl.create_some_context()
# # creer une file de commandes
# myQueue = cl.CommandQueue(myContext)
# # allouer et initialiser la memoire du device
# inputData = np.random.rand(50000).astype(np.float32)
# outputData = np.empty_like(inputData)
# myFlags = cl.mem_flags
# inputBuffer = cl.Buffer(myContext,
# myFlags.READ_ONLY | myFlags.COPY_HOST_PTR, hostbuf=inputData)
# outputBuffer = cl.Buffer(myContext, myFlags.WRITE_ONLY, inputData.nbytes)
# # charger et compiler le kernel
# myProgram = cl.Program(myContext,
# """__kernel void add42(__global const float *data, __global float *result){int gid = get_global_id(0);result[gid] = data[gid] + 42.f;}""").build()
# # ajouter le kernel dans la file de commandes
# # recuperer les donnees dans la memoire du device
# myProgram.add42(myQueue, inputData.shape,None, inputBuffer, outputBuffer)
# cl.enqueue_copy(myQueue, outputData, outputBuffer)
# # verifier le resultat du calcul
# if abs(np.linalg.norm(outputData - (inputData + 42))) < 1e-6 :
#     print("passed")
# else:
#     print("failed")
#
