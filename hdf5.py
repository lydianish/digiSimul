import h5py
from PIL.Image import *


def sauv(image):
    """
    Enregistre l'image passee en parametre sous format hdf5 à l'adresse donnee par l'utilisateur ou dans un fichier
    prédéfinie, pour une génération random d'images.
    :param image: image à sauvegarder
    :return: rajoute l'image dans le fichier h5 à l'adresse donnée par l'utilisateur ou créé un nouveau fichier s'il n'existe pas
    """

    im = open(image)
    #Demande du nom du fichier
    fic = input("Entrez le nom du dossier : ")

    #Demande du nom de l'utilisateur
    numn = input("Entrez le numéro de l'utilisateur : ")
    nomu="utilisateur : "+numn

    #Demande du numéro du doigt
    numd = input("Entrez le numéro du doigt : ")
    nomd="doigt : "+numd

    #Création du fichier empreintedigitale
    empdig = h5py.File(fic + ".h5")            # par défaut c'est , 'a' -> permet lecture et écriture s'il existe ou le créé s'il n'existe pas

    if(nomu+"/"+nomd+"/"+image in empdig):
        print("Il existe déjà une image de ce nom dans le chemin suivant :"+fic+"/"+nomu+"/"+nomd)
    else:
        pixels = list(im.getdata())
        empdig.create_dataset(nomu + "/" + nomd + "/" + image, data=pixels, dtype='i')
        empdig[nomu + "/" + nomd + "/" + image]
    # Fermeture du fichier
    empdig.close()


#Test de la méthode
sauv('101_1.tif')


