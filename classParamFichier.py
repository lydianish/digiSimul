#Librairies
import tkinter as Tk
from tkinter.messagebox import *

class ParametreFichier:

    """Classe permettant de construire la zone destinee a la saisie et a la recuperation des parametres du fichier"""

    def __init__(self, parent):
        """Constructeur du frame ParametreFichier"""
        self.couleur = "grey"
        self.framePrincipal = Tk.Frame(parent, bg=self.couleur)
        self.CheminImageSource = Tk.StringVar()
        self.CheminImageSource.set("")
        self.CheminDossierEnregistrement = Tk.StringVar()
        self.CheminDossierEnregistrement.set("")
        self.NombreImage = Tk.StringVar()
        self.NombreImage.set("0")

    def initialise(self):
        """Ajoute les composantes au frame ParametreFichier"""

        #Label Titre
        fltf = Tk.Frame(self.framePrincipal, bg=self.couleur, padx=5)
        fltf.pack()
        labelTitref = Tk.Label(fltf, text="FICHIER", width=150, fg="black", bg="grey80")
        labelTitref.pack()

        #Separateur horizontal
        separatorH = Tk.Frame( self.framePrincipal, height=2, bd=1, relief=Tk.SUNKEN)
        separatorH.pack(fill=Tk.X)

        #fp
        fpf = Tk.Frame(self.framePrincipal, bg=self.couleur, padx=5, pady=5)
        fpf.pack()
        #ImageSource
        labelIS = Tk.Label(fpf, text="Chemin de l'image source:", bg=self.couleur, padx=5, pady=5)
        labelIS.grid(row=0, column=0)
        entreeIS = Tk.Entry(fpf, textvariable=self.CheminImageSource, width=30)
        entreeIS.grid(row=0, column=1)

        #DossierEnregistrement
        labelDS = Tk.Label(fpf, text="Chemin du dossier d'enregistrement :", bg=self.couleur, padx=5, pady=5)
        labelDS.grid(row=1, column=0)
        entreeDS = Tk.Entry(fpf, textvariable=self.CheminDossierEnregistrement, width=30)
        entreeDS.grid(row=1, column=1)

        #NombreImage
        labelNI = Tk.Label(fpf, text="Nombre d'images:", bg=self.couleur, padx=5, pady=5)
        labelNI.grid(row=2, column=0)
        entreeNI = Tk.Entry(fpf, textvariable=self.NombreImage, width=30)
        entreeNI.grid(row=2, column=1)

        def getValF():
            self.CheminImageSource = entreeIS.get()
            self.CheminDossierEnregistrement = entreeDS.get()
            self.CheminNombreImage = (int)(entreeNI.get())
            print(self.CheminImageSource, self.CheminDossierEnregistrement, self.CheminNombreImage)

        # Zone pour valider les données
        #Tk.Button(self.framePrincipal, text=" Valider ", command=self.getParamFichier).pack()

    def getFramePrincipal(self):
        """Renvoie le framePrincipal"""
        return self.framePrincipal

    def getParamFichier(self):
        """Renvoie les valeurs saisies par l'utilisateur . 
           Ces valeurs correspondent aux parametres du fichier"""
        l = self.CheminImageSource.get()
        m = self.CheminDossierEnregistrement.get()
        n = self.NombreImage.get()
        self.estNombre(n)
        #print(l, m, n)
        return (l, m, n)

    def estNombre(self,n):
        """Affiche un message d'erreur si n n'est pas un nombre(autrement dit si le type de n n'est pas un reel)
            n est considere comme une chaine de caracteres"""
        try:
            f1 = float(n)
        except:
            showerror("Erreur de saisie du champ 'nombre d'images'", "Le champ 'nombre d'images' est incorrect, veuillez saisir un nombre")

    def execute(self):
        """Initiale et affiche le frame ParametreFichier"""
        self.initialise()
        self.framePrincipal.pack()

    def affiche(self):
        """Affiche le frame ParametreFichier"""
        self.framePrincipal.pack()

# Main
if __name__ == '__main__':
    fen = Tk.Tk()
    pFichier = ParametreFichier(fen)
    pFichier.execute()
    l = pFichier.getParamFichier()
    print(l)
    fen.mainloop()
