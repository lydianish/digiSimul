import h5py
from PIL.Image import *


def sauv(image,nom,pathSave):
    print(pathSave)
    """
    Enregistre l'image passee en parametre sous format hdf5 à l'adresse donnee par l'utilisateur ou dans un fichier
    prédéfinie, pour une génération random d'images.
    :param image: image à sauvegarder
    :return: rajoute l'image dans le fichier h5 à l'adresse donnée par l'utilisateur ou créé un nouveau fichier s'il n'existe pas
    """


    #Création du fichier empreintedigitale
    empdig = h5py.File(pathSave + ".h5")            # par défaut c'est , 'a' -> permet lecture et écriture s'il existe ou le créé s'il n'existe pas

    if(pathSave+nom in empdig):
        print("Il existe déjà une image de ce nom dans le chemin suivant :"+pathSave+"/"+nom)
    else:
        pixels = list(image.getdata())
        empdig.create_dataset(pathSave+ nom, data=pixels, dtype='i')
        empdig[pathSave+ nom]
    # Fermeture du fichier
    empdig.close()


