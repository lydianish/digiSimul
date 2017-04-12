from PIL.Image import *
from MyException import MyException, test, test007



def decoupe(image,x,y,taille_capteur_long,taille_capteur_hauteur):
    #Cette méthode renvoie une image découpée à partir des coordonnées (x,y) ainsi que la taille du capteur
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



