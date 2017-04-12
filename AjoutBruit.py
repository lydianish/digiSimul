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

def echantillonageRadial(image, beamNumber, pxPerBeam, angle, height, dmin, dmax):
    longeur, largeur = image.size
    image = list(image.getdata())
    image = [image[i * largeur:(i + 1) * largeur] for i in range(longeur)]
    # Base sortie
    imageSortie = np.zeros((longeur, largeur))
    i = (3 * math.pi - angle) / 2
    while i < (3 * math.pi + angle) / 2:
        j = dmin
        while j < dmax:
            x = j * math.cos(i) + largeur / 2
            y = -j * math.sin(i) + height
            x = int(x)
            y = int(y)
            imageSortie[x][y] = image[x][y]

            j += (((3 * math.pi + angle) / 2) - ((3 * math.pi - angle) / 2)) / (pxPerBeam - 1)
        i += (dmax - dmin) / (beamNumber - 1)
    return imageSortie


def echantillonageRect(npimage, longeur, largeur, nbPointAbscisse, nbpointOrdonnee):
    # Image base sortie :
    imageSortie = np.ones((longeur, largeur))-2
    y = 0
    while y < largeur:
        x=0
        while x < longeur:
            imageSortie[int(x)][int(y)] = npimage[int(x)][int(y)]
            x += largeur
        y += longeur/ nbpointOrdonnee
    return imageSortie


def echantillonageRect2(npimage,nbPoint):
    """
    
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


def AjoutSpeckel( img, borneInf, borneSup, ecartTypeGauss, u):
    longeur,largeur = img.shape
    #matrices de vecteurs gaussiens
    beta = 8
    alpha = 1.98
    # matrixGauss = stats.gennorm.rvs(beta,scale=alpha,loc=0,size=longeur*longeur*u).reshape(longeur, largeur, u)
    # matrixGauss2 =  stats.gennorm.rvs(beta,scale=alpha,loc=0,size=longeur*longeur*u).reshape(longeur, largeur, u)
    # matrixGauss = (stats.levy_stable_gen.rvs(alpha, 0,size = longeur*largeur*u,scale=gama).reshape(longeur, largeur, u))
    # matrixGauss2 = (stats.levy_stable_gen.rvs(alpha,0,size = longeur*largeur*u,scale=gama).reshape(longeur, largeur, u))
    matrixGauss = np.random.randn(longeur * largeur, u).reshape(longeur, largeur, u)
    matrixGauss2 = np.random.randn(longeur * largeur, u).reshape(longeur, largeur, u)
    imgRetour = np.sqrt(img + 0j)
    i = 0
    while i < u-1:
        imgRetour += (matrixGauss[:,:,i]) + (matrixGauss2[:,:,i]*1j)
        i += 1
    img = np.square(imgRetour.real) + np.square(imgRetour.imag)
    return img


def interpolation(img):
    """
    Interpolation bicubique
    :param img: Image à interpoler sous forme de tableau numpy
    :return: Fonction d'interpoaltion de l'image 
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


def AjoutBruit(image):
    """
    Fonction principale appelant les méthodes permettant d'ajouter un bruit de peckel à image de type optique
    
    :param image: Une image provenant de la bibliothèque "PIL Image" 
    :return: Un tableau bidimentionel numpy représentant une image 
    """
    # conversion de l'image en array numpy
    nbPoint = 2
    l,L = image.shape
    img = echantillonageRect2(image,nbPoint)
    img4 = AjoutSpeckel(img, 1,1 , 0.2,3)
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

def trouveAlphaGama():
    img = cv2.imread("images/01_d_3.bmp")
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    l,L = img.shape
    y = -1
    somme = 0
    sommeC = 0
    cpt = 0
    a = [0]
    while y < L-1:
        y +=1
        x = -1
        while x < l-1:
            print(x,y)
            x += 1
            if ( img[x][y] != 0):
                a.append(img[x][y])

    print(a)
    esp = np.mean(a,dtype=np.float64)
    var = np.var(a,dtype=np.float64)
    alpha = np.sqrt(np.square(math.pi)/(6*var))
    gama = math.exp( alpha * (esp - math.log(2,10) - 0.57721566490153286*((1/alpha)-1) ))
    print(esp,var,alpha,gama)



def anayseImageCapteur(path):
    listPx = [0]
    listeImage = os.listdir(path)
    for image in listeImage:
        p= "%s\%s"%(path,image)
        y = -1
        try :
            imgTmp = cv2.imread(imgTmp)
            l,L = imgTmp.shape
            while y < L-1:
                y +=1
                x = -1
                while x < l-1:
                    print(x,y)
                    x += 1
                    if ( imgTmp[x][y] != 0):
                        listPx.append(imgTmp[x][y])
        except: print("Impossible d'analyser l'image %s"%(p))


        esp = np.mean(listPx, dtype=np.float64)
        var = np.var(listPx, dtype=np.float64)
        alpha = np.sqrt(np.square(math.pi) / (6 * var))
        gama = math.exp(alpha * (
            esp - math.log(2, 10) - 0.5772156 * ((1 / alpha) - 1)))
        print (esp,var,alpha,gama)

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
