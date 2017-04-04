import numpy as np
import math
from PIL import Image




def echantillonage(image, beamNumber, pxPerBeam, angle, height, dmin, dmax):
    longeur, largeur = image.size
    image = list(image.getdata())
    image = [image[i * largeur:(i + 1) * largeur] for i in range(longeur)]
    #Base sortie
    imageSortie = np.zeros((longeur,largeur))
    i = ((3 * math.pi) - angle)/2
    j = dmin
    while i <= ((3 * math.pi) + angle)/2:
        while j <= dmax:
            x = j*math.cos(i) + largeur/2
            y = -j*math.sin(i) + height
            x = int(math.fabs(x))
            y = int(y)
            print(x,y)
            imageSortie[x][y] = image[x][y]
            j += pxPerBeam
        i += beamNumber
    return imageSortie


img = Image.open("images/fg1.bmp").convert("L")
l,L = img.size
print(l,L)
img2 = echantillonage(img, 100, 2, 3, 10, 15, 350)
img3 = Image.fromarray(img2)
img3.show()