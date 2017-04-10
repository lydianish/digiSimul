import numpy as np
import math
from PIL import Image
from scipy import interpolate
from random import uniform
from PIL import ImageOps
import cv2
import _thread
from multiprocessing import Pool

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


def AjoutSpeckel( img, borneInf, borneSup, ecartTypeGauss):
    longeur,largeur = img.shape
    imgRetour = np.ones((longeur, largeur)) * 255
    y = -1
    while y < largeur -1:
        x = -1
        y += 1
        while x < longeur-1 :
            x += 1
            if img[x,y] != -1:
                px = np.sqrt(img[x,y]) + 0j
                u = uniform(borneInf,borneSup)
                i = 0
                while i < u:
                    g = np.random.multivariate_normal((0,0),[[ecartTypeGauss, 0], [0, ecartTypeGauss]],1)
                    px += g[0,0]
                    px += np.complex(0,g[0,1])
                    i += 1
                imgRetour[x,y] = (np.square(px.real) + np.square(px.imag))
    return imgRetour


def interpolation(img):
    img = np.zeros(img.shape) + img
    l,L = img.shape
    x = np.arange(0,l,1)
    y = np.arange(0, L, 1)
    img = interpolate.interp2d(x,y,img, kind='cubic')
    return img

def construireImageInterpelee(function,l,L,nbPoint):

    x = np.arange(0,l,1);
    y = np.arange(0,L,1)
    arr = np.zeros((l,L))
    for yi in y:
        for xi in x:
         arr[xi][yi] = function(xi/nbPoint,yi/nbPoint)
    print(arr)
    img = Image.fromarray(arr)
    img = ImageOps.mirror(img)
    img.rotate(90).show()
    return img


def AjoutBruit(image):
    # conversion de l'image en array numpy
    nbPoint = 2
    l,L = image.shape
    img = echantillonageRect2(image, l ,L ,nbPoint)
    print(img.shape)
    img4 = AjoutSpeckel(img, 1,1 , 0.2)
    # Image.fromarray(img4).show()
    img5 = interpolation(img4)
    img5 = construireImageInterpelee(img5,l,L,nbPoint)


def AjoutBruitMultiThreah():
    img = cv2.imread("images/vador.bmp")
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    t1 = _thread.start_new_thread(AjoutBruit,(img,))
    t2 = _thread.start_new_thread(AjoutBruit,(img,))
    t3 = _thread.start_new_thread(AjoutBruit,(img,))
    t4 = _thread.start_new_thread(AjoutBruit,(img,))
    return 0;


# MAIN
AjoutBruitMultiThreah()

