import h5py
from PIL.Image import *


def sauv(image,nom,pathSave):
    """
    Enregistre l'image passee en parametre sous format hdf5 à l'adresse donnee par l'utilisateur ou dans un fichier
    prédéfinie, pour une génération random d'images.
    :param image: image à sauvegarder
    :param nom: nom de l'image à sauvegarder
    :param pathSave: adresse où enregistrer l'image
    :return: rajoute l'image dans le fichier h5 à l'adresse donnée par l'utilisateur ou créé un nouveau fichier s'il n'existe pas
    """

    #Création du fichier empreintedigitale
    empdig = h5py.File(pathSave + "/digi.h5")            # par défaut c'est , 'a' -> permet lecture et écriture s'il existe ou le créé s'il n'existe pas


    j = 0
    a=False
    while(pathSave+nom in empdig):
        j=j+1

        # print("Il existe déjà une image de ce nom dans le chemin suivant :"+fic+"/"+nomu+"/"+nomd)
        i = len(nom) - 1
        print(nom)
        print(i)
        while (nom[i] != '.'):
            print(nom[i])
            i = i - 1
        if(a):
            nom = nom[:(i-1-len(str(j)))] + '_'+str(j) + nom[i:]
        else:
            nom=nom[:i]+'_'+str(j) +nom[i:]
        a=True

    pixels = list(image.getdata())
    empdig.create_dataset(pathSave+ nom, data=pixels, dtype='i')
    empdig[pathSave+nom]
    # Fermeture du fichier
    empdig.close()



