import numpy as np
import cv2

#Methode qui renvoie une image ayant subi une rotation
#Données :
#   - image : l'image de depart
#   - angle : angle de rotation
#Containtes : - Utiliser la fonction cv2.imread() pour l'image
#             - l'angle doit etre exprimé en degres

def rotation(image, angle):
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2) #division entiere

    M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])

    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))

    M[0,2] =M[0, 2]+ (nW / 2) - cX
    M[1,2] =M[1, 2]+ (nH / 2) - cY

    imagefinale=cv2.warpAffine(image, M, (nW, nH))

    return (imagefinale)

# # Test de la méthode
# im = cv2.imread('101_1.tif', -2)
# a=rotation(im,120)
# cv2.imshow("a",a)
# cv2.waitKey(0)

