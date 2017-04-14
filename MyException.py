from PIL.Image import *

class MyException(Exception) :

    # Methode qui teste si le rectangle à découper dépasse l'image
    # Données :
    #   - image : l'image à tester
    #   - (x,y)  : coordonnées du pixel
    #   - taille du capteur: -taille_capteur_long
    #                        - taille_capteur_hauteur

    def test(image,x,y,taille_capteur_long,taille_capteur_hauteur):
        # on traite les cas ou les coordonnees du capteur sont en dehors de l'image
        h, l = image.shape[:2]
        if ( x < 0 or  y < 0 or taille_capteur_long <= 0 or taille_capteur_hauteur <= 0):
            raise MyException("Il faut des valeurs positives.")
        elif(h < x or l<y or h-x<taille_capteur_long or l-y< taille_capteur_hauteur):
            raise MyException("Les valeurs sortent de l'image.")



    # Methode qui teste si le rectangle à découper ne contient que du noir (il faut au moins 10 pixels de
    # couleur pour que l'image soit affichée
    # Données :
    #   - image : l'image à tester
    #   - (x,y)  : coordonnées du pixel
    #   - taille du capteur: -taille_capteur_long
    #                        - taille_capteur_hauteur
    
    def test007(image,x,y,taille_capteur_long,taille_capteur_hauteur):
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
            if (a == 0 and d == 0):
                e = e
            else:
                e = e + 1
            j = j + 1
        if (e < 10):
            raise MyException("Aucune empreinte n'est détectée.")

