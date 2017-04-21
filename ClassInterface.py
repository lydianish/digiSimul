#Librairies
import tkinter as Tk
from tkinter.messagebox import *
from classParamCapteur import *
from classParamDecoupe import *
from classParamFichier import *

class Fenetre:

    """Classe permettant de construire linterface DiSimul"""

    def __init__(self):
        """Constructeur de la fenetre"""
        self.couleur = "grey"
        self.fenetre = Tk.Tk()
        self.fenetre.title("DigiSimul")
        self.fenetre['bg'] = 'white'
        self.framePrincipal = Tk.Frame(self.fenetre)
        self.frameParamCapteur = ParametreCapteur(self.framePrincipal)
        self.frameParamDecoupe = ParametreDecoupe(self.framePrincipal)
        self.frameParamFichier = ParametreFichier(self.framePrincipal)
        self.frameParamVitesse = Tk.Frame(self.framePrincipal, bg=self.couleur)
        self.numVitesse = Tk.IntVar()
        self.frameParamValidation = Tk.Frame(self.framePrincipal)

    def initialise(self):
        """Ajoute les composantes a la fenetre"""

        #Zone pour les données du capteur
        self.frameParamCapteur.initialise()
        #Zone pour les données de la decoupe
        self.frameParamDecoupe.initialise()
        #Zone pour les données du fichier
        self.frameParamFichier.initialise()
        #Zone pour le choix de la vitesse
        flt = Tk.Frame(self.frameParamVitesse, bg=self.couleur)
        flt.pack()
        labelTitre = Tk.Label(flt, text="VITESSE", width=150, padx=5, fg="black", bg=self.couleur)
        labelTitre.grid(row=0, column=0, columnspan=2)
        boutonLent = Tk.Radiobutton(flt, bg=self.couleur, text="Lent", variable=self.numVitesse, value=0, command=self.valnumVitesse)
        boutonRapide = Tk.Radiobutton(flt, bg=self.couleur, text="Rapide", variable=self.numVitesse, value=1, command=self.valnumVitesse)
        boutonLent.grid(row=1, column=0)
        boutonRapide.grid(row=1, column=1)
        #Zone pour valider les données
        Tk.Button(self.frameParamValidation, text=" Valider ", command=self.getValues).pack()

        #Affichage des frames
        self.framePrincipal.pack()
        self.frameParamCapteur.affiche()
        #Separateur horizontal
        separatorH = Tk.Frame( self.framePrincipal, height=2, bd=1, relief=Tk.SUNKEN)
        separatorH.pack(fill=Tk.X)
        self.frameParamDecoupe.affiche()
        #Separateur horizontal
        separatorH = Tk.Frame( self.framePrincipal, height=2, bd=1, relief=Tk.SUNKEN)
        separatorH.pack(fill=Tk.X)
        self.frameParamFichier.affiche()
        #Separateur horizontal
        separatorH = Tk.Frame( self.framePrincipal, height=2, bd=1, relief=Tk.SUNKEN)
        separatorH.pack(fill=Tk.X)
        self.frameParamVitesse.pack()
        #Separateur horizontal
        separatorH = Tk.Frame( self.framePrincipal, height=2, bd=1, relief=Tk.SUNKEN)
        separatorH.pack(fill=Tk.X)
        self.frameParamValidation.pack()

    def valnumVitesse(self):
        """Methode a executer selon la valeur du numVitesse"""
        pass        #Pour l'instant, ne fais rien

    def getNumVitesse(self):
        """Renvoie le numero de la vitesse de traitement des données: 0 pour lent et 1 pour rapide"""
        return self.numVitesse

    def getNumModeInt(self):
        """Renvoie le numero du mode de traitement des données: 0 pour Manuel et 1 pour Analyse"""
        return self.frameParamCapteur.getNumMode()

    def getValues(self):
        """Renvoie les valeurs des variables"""
        vc = self.frameParamCapteur.getParamCapteur()
        vd = self.frameParamDecoupe.getParamDecoupe()
        vf = self.frameParamFichier.getParamFichier()
        #print(vc + vd + vf)
        return (vc,vd,vf)

    def execute(self):
        """Initiale et affiche la fenetre"""
        self.initialise()
        self.fenetre.mainloop()

# Main
if __name__ == '__main__':
    fen = Fenetre()
    fen.execute()