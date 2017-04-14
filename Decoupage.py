from PIL.Image import *
from MyException import MyException, test, test007



def decoupe(image,x,y,taille_capteur_long,taille_capteur_hauteur):
    """
    
    :param image: l'image de depart
    :param x: coordonnée de l' abscisse du pixel en haut à gauche où l'on veut découper
    :param y: coordonnée de  l' ordonnée du pixel en haut à gauche où l'on veut découper
    :param taille_capteur_long: taille de capteur en longueur
    :param taille_capteur_hauteur: taille du capteur en hauteur
    :return: une image découpée, renvoie une exception si (x,y) n'appartiennent pas à l'image ou
#           si la partie à découper ne contient que du noir
    """
    try :
        test(image,x,y,taille_capteur_long,taille_capteur_hauteur)
        test007(image, x, y, taille_capteur_long, taille_capteur_hauteur)
        box = (x, y, x+taille_capteur_long, y+taille_capteur_hauteur)
        coupe = image.crop(box)
        Image.show(coupe)
        return (coupe)
    except MyException as e:
        print(e)
        exit()


# # Test de la méthode
# im = open('101_1.tif')
# a=decoupe(im,0,0,200,200)
