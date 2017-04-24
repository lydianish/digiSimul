from PIL.Image import *

class MyException(Exception) :
    def __init__(self, raison):
        self.raison = raison

    def __str__(self):
        return self.raison

def test(image,x,y,taille_capteur_long,taille_capteur_hauteur):
    """
    Teste si le rectangle à découper dépasse l'image
    :param image: image à tester
    :param x: coordonnées de l'abscisse du pixel
    :param y: coordonnées de l'ordonnée du pixel
    :param taille_capteur_long: taille du capteur en longueur
    :param taille_capteur_hauteur: taille du capteur en hauteur
    """
    h, l = image.size
    if ( x < 0 or  y < 0 or taille_capteur_long <= 0 or taille_capteur_hauteur <= 0):
        raise MyException("Il faut des valeurs positives.")
    elif(h < x or l<y or h-x<taille_capteur_long or l-y< taille_capteur_hauteur):
        raise MyException("Les valeurs sortent de l'image.")

def test007(image,x,y,taille_capteur_long,taille_capteur_hauteur):
    """
    Teste si la partie à découper ne contient que du noir (il faut au moins 10 pixels de
     couleur pour que l'image soit affichée)
    :param image: image à tester
    :param x: coordonnées de l'abscisse du pixel
    :param y: coordonnées de l'ordonnée du pixel
    :param taille_capteur_long: taille du capteur en longueur
    :param taille_capteur_hauteur: taille du capteur en hauteur
    """
    i=x
    j=y
    e=0
    while (i < x+taille_capteur_long and e<10):
        a = Image.getpixel(image, (i, j))  # coin supG
        d = Image.getpixel(image, (i, j + taille_capteur_hauteur))  # coin infG
        if (a == 0 and d==0 ):
            e = e
        else:
            e = e + 1
        i = i + 1
    i=x
    while (j<y+taille_capteur_hauteur and e<10):
        a = Image.getpixel(image, (i, j))  # coin supG
        d = Image.getpixel(image, (i+taille_capteur_long, j))  # coin infG
        if (a == 0 and d == 0):  # and d == 0 and g == 0 and j == 0):
            e = e
        else:
            e = e + 1
        j = j + 1
    if (e < 10):
        raise MyException("Aucune empreinte n'est détectée.")
