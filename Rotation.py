import numpy as np
import cv2


def rotation(image, angle):
    #Cette méthode renvoie une image qui a subi une rotation de angle degre ainsi que les positions des coin de la nouvelle image
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)

    M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])

    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))

    M[0,2] =M[0, 2]+ (nW / 2) - cX
    M[1,2] =M[1, 2]+ (nH / 2) - cY

    imagefinale=cv2.warpAffine(image, M, (nW, nH))

    return (imagefinale)








