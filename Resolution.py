from PIL import Image


#Fonctions qui vont permettrent de calculer la taille en pixels, ou en pouce ou la resolution d'une image donee
#L'utilite de ces fonctions est qu'elles vont permettrent de calculer la nouvelle taille à donner en paramètres à rezize pour le changement de resolution

#------------------------------------------------------------------------
#Methode qui calcule la taille(largeur * hauteur) en pixels d'une image
#Donées :
#   - ro : la resolution de l'image
#   - d = (ld, hd) :dimensions physiques en pouces de l'image avec :
#           - ld = largeur en pouces
#           - hd = hauteur en pouces
#Remmarque : d est un tuple
#Containtes : ld et hd doivent etre exprimés en pouces

#Code :
def taille_en_pixels(ro, d):
    ld, hd = d
    lt = (int)(ld * ro)
    ht = (int)(hd * ro)
    return (lt,ht)

#Test de la methode :
#print(taille_en_pixels(500, (30,40)))

#------------------------------------------------------------------------
#Methode qui calcule la taille(largeur * hauteur) en pouce d'une image
#Donées :
#   - ro : la resolution de l'image
#   - t = (lt, ht) :dimensions en pixels (definition) de l'image avec :
#           - lt = largeur en pixels
#           - ht = hauteur en pixels
#Remmarque : t est un tuple
#Containtes : lt et ht doivent etre exprimés en pixels

#Code :
def taille_en_pouces(ro, t):
    lt, ht = t
    ld = lt / ro
    hd = ht / ro
    return (ld,hd)

#Test de la methode :
#1
#print(taille_en_pouces(500, (15000,20000)))

#2
#ro = 500
#rc = 400
#cheminf = "/Users/docteur/Desktop/L3/S2/Stage_Applicatif/Test_Photos/105_2.tif"
#i = Image.open(cheminf)
#d = taille_en_pouces(ro, i.size)
#print(d)
#t = taille_en_pixels(rc, d)
#print(t)
#i2 = (i.copy()).resize(t, Image.ANTIALIAS)
#i.show()
#i2.show()

#------------------------------------------------------------------------
#Methode qui calcule la resolution d'une image
#Donées :
#   - t = (lt, ht) :dimensions en pixels (definition) de l'image avec :
#           - lt = largeur en pixels
#           - ht = hauteur en pixels
#   - d = (ld, hd) :dimensions physiques en pouces de l'image avec :
#           - ld = largeur en pouces
#           - hd = hauteur en pouces
#Remmarque : t et d sont des tuples
#Containtes :   - lt et ht doivent etre exprimés en pixels
#               - ld et hd doivent etre exprimés en pouces

#Code :
def resolution(t, d):
    lt, ht = t
    ld, hd = d
    ro = lt//ld
    return ro

#Test de la methode :
#print(resolution((15000,20000), (30,40)))


# ----------------------------------------------------------------------------
# Methode qui sous-echantillonne l'image dont le chemin est donne en parametre
# Renvoie une copie de l'image sous-echantillonnee (avec une resolution rc)
# Données :
#       - ro : resolutionOriginale (c'est la resolution de l'image originale dont le chemin est donne en parametre)
#       - rc : resolutionCapteur (c'est la resolution finale)
#       - chemin : chemin vers l'image a re-echantillonner
#Contrainte : ro > rc

#Code :
def sous_echantillonnage(ro, rc, image):
    if(ro <= rc):
        print("Erreur de sous_echantillonnage, ro doit etre strictement plus grand que rc")
        return
    else:
        # print("Vous etes dans Sous-echantillonnage")
        #Calcul des dimensions de l'image
        d = taille_en_pouces(ro, image.size)
        # print("dimension", d)
        #Calcul de la nouvelle de l'image pour la resolution rc
        t = taille_en_pixels(rc, d)
        # print("nouvelle taille", t)
        #sous-echantillonnage
        im = (image.copy()).resize(t, Image.ANTIALIAS)
        return im

# Test de la methode :
#ro = 500
#rc = 200
#cheminf = "/Users/docteur/Desktop/L3/S2/Stage_Applicatif/Test_Photos/105_2.tif"
#i = Image.open(cheminf)
#im1 = sous_echantillonnage(ro, rc, cheminf)
#i.show()
#im1.show()



# ----------------------------------------------------------------------------
# Methode qui sur-echantillonne l'image dont le chemin est donne en parametre
# Renvoie une copie de l'image sur-echantillonnee (avec une resolution rc)
# Données :
#       - ro : resolutionOriginale (c'est la resolution de l'image originale dont le chemin est donne en parametre)
#       - rc : resolutionCapteur (c'est la resolution finale)
#       - chemin : chemin vers l'image a re-echantillonner
# Contrainte : ro < rc

#Code :
def sur_echantillonnage(ro, rc, image):
    if (ro >= rc):
        print("Erreur de sur_echantillonnage, ro doit etre strictement plus petit que rc")
        return
    else:
        # print("Vous etes dans Sur-echantillonnage")
        # print("taille initiale", imOCopie.size)
        #Calcul des dimensions de l'image
        d = taille_en_pouces(ro, image.size)
        # print("dimension", d)
        #Calcul de la nouvelle de l'image pour la resolution rc
        t = taille_en_pixels(rc, d)
        # print("nouvelle taille", t)
        #sous-echantillonnage
        im = (image.copy()).resize(t, Image.ANTIALIAS)
        return im

# Test de la methode :
#ro = 500
#rc = 600
#cheminf = "/Users/docteur/Desktop/L3/S2/Stage_Applicatif/Test_Photos/105_2.tif"
#i = Image.open(cheminf)
#im2 = sur_echantillonnage(ro, rc, cheminf)
#i.show()
#im2.show()

# ----------------------------------------------------------------------------
# Methode qui re-echantillonne l'image dont le chemin est donne en parametre
# Renvoie une copie de l'image re-echantillonnee (avec une resolution rc)
# Données :
#       - ro : resolutionOriginale (c'est la resolution de l'image originale dont le chemin est donne en parametre)
#       - rc : resolutionCapteur (c'est la resolution finale)
#       - chemin : chemin vers l'image a re-echantillonner
#Contrainte : nulle

#Code :
def re_echantillonnage(ro, rc, image):
    if(ro > rc):                             #l 'image originale  une resolution plus grande que celle du capteur
        im = sous_echantillonnage(ro, rc, image)
        return im
    elif(ro < rc):                           #l 'image originale  une resolution plus petite que celle du capteur
        im = sur_echantillonnage(ro, rc, image)
        return im
    else:                                    #l 'image originale  une resolution egale a celle du capteur
        # print("Vous etes dans Re-echantillonnage:\nro = rc --> rien à faire")
        # print("taille initiale = finale ", imOCopie.size)
        return image

# chemin= 'C:/Users/Noemie/PycharmProjects/Projet/03_d_2.bmp'
# t= (102,145)
# image = Image.open('101_1.tif')
# print(image.size)
# im = (image.resize(t, Image.ANTIALIAS))
# tl,th=image.shape
# print(image.size)
