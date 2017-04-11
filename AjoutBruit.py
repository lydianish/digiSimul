import numpy as np
import math
from PIL import Image
from scipy import interpolate
from scipy import stats
from random import uniform
from PIL import ImageOps
import cv2
import _thread
from multiprocessing import Pool
import list
import threading

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


def echantillonageRect2(npimage, longeur, largeur, nbPoint):
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
    alpha = 1.9
    gama =  0.4
    matrixGauss = (stats.levy_stable.rvs(alpha, 0,size = longeur*largeur*u,scale=gama).reshape(longeur, largeur, u))
    matrixGauss2 = (stats.levy_stable.rvs(alpha,0,size = longeur*largeur*u,scale=gama).reshape(longeur, largeur, u))
    imgRetour = np.sqrt(img + 0j)
    i = 0
    while i < u-1:
        imgRetour += (matrixGauss[:,:,i]) + (matrixGauss2[:,:,i]*1j)
        i += 1
    img = np.square(imgRetour.real) + np.square(imgRetour.imag)
    return img


def interpolation(img):
    img = np.zeros(img.shape) + img
    l,L = img.shape
    x = np.arange(0,l,1)
    y = np.arange(0, L, 1)
    X,Y = np.meshgrid(x,y)
    fonctionInter = interpolate.interp2d(x,y,img, kind='cubic')
    return fonctionInter

def construireImageInterpelee(function,l,L,nbPoint):
    x = np.arange(0, l/nbPoint,1/nbPoint)
    y = np.arange(0, L/nbPoint,1/nbPoint)
    img = function(x,y)
    return img


def AjoutBruit(image):
    # conversion de l'image en array numpy
    nbPoint = 2
    l,L = image.shape
    img = echantillonageRect2(image, l ,L ,nbPoint)
    img4 = AjoutSpeckel(img, 1,1 , 0.2,50)
    img5 = interpolation(img4)
    img5 = construireImageInterpelee(img5,l,L,nbPoint)
    Image.fromarray(img5)



def AjoutBruitMultiThreah():
    img = cv2.imread("images/vador.bmp")
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    t1 = threading.Thread(target=multipleImage,args=(img,))
    t2 = threading.Thread(target=multipleImage,args=(img,))
    t3 = threading.Thread(target=multipleImage,args=(img,))
    t4 = threading.Thread(target=multipleImage,args=(img,))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    return 0;

def multipleImage(img):
    it = 0
    while it < 40:
        print(it)
        AjoutBruit(img)
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
    gama = math.exp( alpha * (esp - math.log(2,10) - 0.577215664901532860606512090082402431042159335939923598805*((1/alpha)-1) ))
    print(esp,var,alpha,gama)

# MAIN
img = cv2.imread("images/fg1.bmp")
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
AjoutBruitMultiThreah()

