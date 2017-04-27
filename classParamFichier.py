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
        self.CheminImageSource.set("C:/Users\polch_000\Desktop\imagesBdd")
        self.CheminDossierEnregistrement = Tk.StringVar()
        self.CheminDossierEnregistrement.set("C:/Users\polch_000\Desktop\imagesRes")
        self.NombreImage = Tk.StringVar()
        self.NombreImage.set("50")
        self.ResolutionOriginale = Tk.StringVar()
        self.ResolutionOriginale.set("100")
        self.numDebuitage = Tk.IntVar()

    def initialise(self):
        """Ajoute les composantes au frame ParametreFichier"""

        #Label Titre
        fltf = Tk.Frame(self.framePrincipal, bg=self.couleur, padx=5)
        fltf.pack()
        labelTitref = Tk.Label(fltf, text="FICHIER",font='Calibri 20 bold', width=150, fg="black", bg="grey80")
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

        #ResolutionOriginale
        labelRO = Tk.Label(fpf, text="Resolution de l'image source", bg=self.couleur, padx=5, pady=5)
        labelRO.grid(row=3, column=0)
        entreeRO = Tk.Entry(fpf, textvariable=self.ResolutionOriginale, width=30)
        entreeRO.grid(row=3, column=1)
        labelRO2 = Tk.Label(fpf, text="     dpi", bg=self.couleur, padx=5, pady=5)
        labelRO2.grid(row=3, column=2)

        #Debruitage de l'image de base
        #Frame
        frameDebruitage = Tk.Frame(self.framePrincipal, bg=self.couleur, padx=5, pady=5)
        frameDebruitage.pack()
        labelDebruitage = Tk.Label(frameDebruitage, text="Debruitage de l'image source", width=70, bg=self.couleur, padx=5, pady=5)
        labelDebruitage.grid(row=0, column=0)
        boutonDebruitageOui = Tk.Radiobutton(frameDebruitage, bg=self.couleur, text="Oui", variable=self.numDebruitage, value=0, command=self.valnumDebruitage)
        boutonDebruitageOui.deselect()
        boutonDebruitageNon = Tk.Radiobutton(frameDebruitage, bg=self.couleur, text="Non", variable=self.numDebruitage, value=1, command=self.valnumDebruitage)
        boutonDebruitageNon.deselect()
        boutonDebruitageOui.grid(row=0, column=1)
        boutonDebruitageNon.grid(row=0, column=2)

        def getValF():
            self.CheminImageSource = entreeIS.get()
            self.CheminDossierEnregistrement = entreeDS.get()
            self.CheminNombreImage = (int)(entreeNI.get())
            print(self.CheminImageSource, self.CheminDossierEnregistrement, self.CheminNombreImage)

        # Zone pour valider les données
        #Tk.Button(self.framePrincipal, text=" Valider ", command=self.getParamFichier).pack()

    def valnumDebruitage(self):
        """Methode a executer selon la valeur du numMode"""
        pass     #Ne fais rien pour l'instant
        #self.getNumDebruitage()
        #print(self.numDebruitage.get())
        # if (self.numDebruitage.get()== 0):
        # else:

    def getFramePrincipal(self):
        """Renvoie le framePrincipal"""
        return self.framePrincipal

    def getParamFichier(self):
        """Renvoie les valeurs saisies par l'utilisateur . 
           Ces valeurs correspondent aux parametres du fichier"""
        l = self.CheminImageSource.get()
        m = self.CheminDossierEnregistrement.get()
        n = self.NombreImage.get()
        r = self.ResolutionOriginale.get()
        res =[n, r]
        self.estNombre(res)
        return (l, m, n, r)

    def estNombre(self,n):
        """Affiche un message d'erreur si l'un des elements de n n'est pas un nombre (autrement dit si le type de l'un des elements de n n'est pas un reel)
            n est considere comme une liste de chaines de caracteres"""
        try:
            for i in n:
                fi = float(i)
        except:
            showerror("Erreur de saisie dans la section decoupe ", "Erreur, veuillez saisir des nombres")
            return

    def getNumDebruitage(self):
        """Renvoie  0 si on doit debruiter l'image, 1 sinon"""
        return self.numDebruitage.get()

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
