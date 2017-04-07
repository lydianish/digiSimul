import numpy as np
import math
from PIL import Image
from scipy import interpolate
from random import uniform
from PIL import ImageOps
import cv2
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
            x += largeur / nbPointAbscisse
        y += longeur/ nbpointOrdonnee
    return imageSortie


def echantillonageRect2(npimage, longeur, largeur, nbPointAbscisse, nbpointOrdonnee):
    y = 0
    while y < largeur/2:
        print(y)
        npimage = np.delete(npimage,(y),axis=1)
        y += 1
    x = 0
    while x < longeur/2:
        print(x)
        npimage = np.delete(npimage,(x),axis=0)
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
                i = 1
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

def construireImageInterpelee(function,l,L):

    x = np.arange(0,l,1);
    y = np.arange(0,L,1)
    arr = np.zeros((l,L))
    for yi in y:
        for xi in x:
         arr[xi][yi] = function(xi/2,yi/2)
    print(arr)
    img = Image.fromarray(arr)
    img = ImageOps.mirror(img)
    img.rotate(90).show()
    return img


def AjoutBruit(image):
    # conversion de l'image en array numpy
    l,L = image.shape
    img = echantillonageRect2(image, l ,L ,l/2,L/2)
    print(img.shape)
    img4 = AjoutSpeckel(img, 2, 10, 2)
    # Image.fromarray(img4).show()
    img5 = interpolation(img4)
    img5 = construireImageInterpelee(img5,l,L)

# MAIN
img = cv2.imread("images/leia.jpg")
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
AjoutBruit(img)

#
# if __name__ == '__main__':
#     pool = Pool(processes=4)
#     possibleFactors = range(1,int(np.floor(np.sqrt(numToFactor)))+1)
#     print 'Checking ', possibleFactors
#     result = pool.map(isFactor, possibleFactors)
#     cleaned = [x for x in result if not x is None]
#     print 'Factors are', cleaned
# img = Image.open("images/fg1.bmp").convert("L")
# l, L = img.size
# print(l, L)
# img2 = echantillonageRadial(img, 20, 20, math.pi +0.1, 10, 15, 350)
# img3 = Image.fromarray(img2)

# img3.show()
#


