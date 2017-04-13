# pour pouvoir visualiser les fichier h5, utiliser : hdf view soft en java

import h5py
import numpy as np
from PIL.Image import *


# Methode qui enregistre l'image passee en parametre sous format hdf5 à l'adresse donnee par l'utilisateur ou dans un fichier
    # prédéfinie, pour une génération random d'images.
# Donées :
#   - image: image à sauvegarder

def sauv(image):

    im = open(image)
    #Demande du nom du fichier
    doss = input("Entrez le nom du dossier : ")

    #Demande du nom de l'utilisateur
    numn = input("Entrez le numéro de l'utilisateur : ")
    nomu="utilisateur"+numn

    #Demande du numéro du doigt
    numd = input("Entrez le numéro du doigt : ")
    nomd="doigt"+numd

    #Création du fichier empreintedigitale
    empdig = h5py.File(doss + ".h5")            # par défaut c'est , 'a' -> permet lecture et écriture s'il existe ou le créé s'il n'existe pas

    if(nomu+"/"+nomd+"/"+image in empdig):
        print("Il existe déjà une image de ce nom dans le chemin suivant :"+doss+"/"+nomu+"/"+nomd)
    else:
        pixels = list(im.getdata())
        empdig.create_dataset(nomu + "/" + nomd + "/" + image, data=pixels, dtype='i')
        empdig[nomu + "/" + nomd + "/" + image]

    # Fermeture du fichier
    empdig.close()


#test de la méthode
sauv('03_d_1.bmp')



