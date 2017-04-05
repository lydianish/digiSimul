import numpy as np
import math
from PIL import Image
from random import uniform


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
    imageSortie = np.ones((longeur, largeur)) -2
    y = 1
    while y < largeur:
        x=1
        while x < longeur:
            imageSortie[int(x)][int(y)] = npimage[int(x)][int(y)]
            x += largeur / nbPointAbscisse
        y += longeur/ nbpointOrdonnee
    return imageSortie



def AjoutSpeckel( img, borneInf, borneSup, ecartTypeGauss):
    print(img)
    longeur,largeur = img.shape
    imgRetour = np.zeros((longeur, largeur))
    y = 0
    while y < largeur-1:
        x=0
        while x < longeur-1:
            if img[x,y] != -1:
                print(x,y)
                px = np.sqrt(img[x,y]) + 0j
                u = uniform(borneInf,borneSup)
                i = 1
                while i < u:
                    g = np.random.multivariate_normal((0,0),[[ecartTypeGauss, 0], [0, ecartTypeGauss]],1)
                    px += g[0,0]
                    px += np.complex(0,g[0,1])
                    i += 1
                x += 1
                imgRetour[x,y] = (np.square(px.real) + np.square(px.imag))
            else:
                x+= 1
                imgRetour[x,y] = 255
        y += 1
    return imgRetour



def AjoutBruit(image):
    # conversion de l'image en array numpy
    longeur, largeur = image.size
    image = list(image.getdata())
    image = [image[i * largeur:(i + 1) * largeur] for i in range(longeur)]
    img2 = echantillonageRect(image, longeur, largeur, 190, 190)
    img3 = AjoutSpeckel(img2, 2, 10, 2)
    img4 = Image.fromarray(img3)
    img4.show()


def interpolation(img):

    return 0

# MAIN
img = Image.open("images/vador.bmp").convert("L")
AjoutBruit(img)


# img = Image.open("images/fg1.bmp").convert("L")
# l, L = img.size
# print(l, L)
# img2 = echantillonageRadial(img, 20, 20, math.pi +0.1, 10, 15, 350)
# img3 = Image.fromarray(img2)

# img3.show()
#
