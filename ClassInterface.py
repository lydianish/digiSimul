#Librairies
from PIL import Image, ImageTk
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
        self.fenetre.geometry("1000x680")
        self.fenetre.title("DigiSimul")
        self.fenetre['bg'] = 'grey'
        #Conteneur Principal: Canvas
        self.can = Tk.Canvas(self.fenetre)
        #Ecran d'accueil: DigiSimul
        self.FrameAccueil = Tk.Frame(self.can, width = 1000, height = 680)
        self.photo = None
        self.bouttonCommencer = Tk.Button(self.FrameAccueil, width = 30, height = 2, text=" Commencer ",font='Times 20', command=self.Commencer)
        #Frame Pricipal: pour la saisie des données
        self.framePrincipal = Tk.Frame(self.can, width = 1000, height = 680)
        #self.framePrincipal = Tk.Frame(self.can)
        self.frameParamCapteur = ParametreCapteur(self.framePrincipal)
        self.frameParamDecoupe = ParametreDecoupe(self.framePrincipal)
        self.frameParamFichier = ParametreFichier(self.framePrincipal)
        self.frameParamVitesse = Tk.Frame(self.framePrincipal, bg=self.couleur)
        self.numVitesse = Tk.IntVar()
        self.frameParamValidation = Tk.Frame(self.framePrincipal)
        self.bouttonValider = Tk.Button(self.frameParamValidation, text=" Valider ", command=self.buttonValid)
        self.données = ()

    def initialise(self):
        """Ajoute les composantes a la fenetre"""

        #FRAME ACCUEIL
        #Zone pour l'affichage de l'image
        labelTitre = Tk.Label(self.FrameAccueil, text="BIENVENU !", font='Times 24', width=50, height=2, padx=5, fg="black")
        labelTitre.pack()
        # Image
        chemin = "digiSimul.png"
        image = Image.open(chemin)
        im = (image.copy()).resize((1000,550), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(im)
        #Canvas d'affichage
        canvas3 = Tk.Canvas(self.FrameAccueil, width=1000, height=550, borderwidth=2, relief=Tk.GROOVE)
        canvas3.create_image(0, 0, anchor=Tk.NW, image=self.photo)
        canvas3.pack()
        #Separateur horizontal
        separatorH = Tk.Frame(self.FrameAccueil, height=2, pady=5, bd=1, relief=Tk.SUNKEN)
        separatorH.pack(fill=Tk.X)
        #Bouton Commencer
        self.bouttonCommencer.pack()

        #FRAME PRINCIPAL
        #Zone pour les données du capteur
        self.frameParamCapteur.initialise()
        #Zone pour les données de la decoupe
        self.frameParamDecoupe.initialise()
        #Zone pour les données du fichier
        self.frameParamFichier.initialise()
        #Zone pour le choix de la vitesse
        flt = Tk.Frame(self.frameParamVitesse, bg=self.couleur)
        flt.pack()
        labelTitre = Tk.Label(flt, text="VITESSE", width=150, padx=5, fg="black", bg="grey80")
        labelTitre.pack()
        #Separateur horizontal
        separatorH = Tk.Frame(flt, height=2, bd=1, relief=Tk.SUNKEN)
        separatorH.pack(fill=Tk.X)
        f = Tk.Frame(flt, bg=self.couleur)
        f.pack()
        #SpinBox :
        s = Tk.Spinbox(f, from_=1, to=10)
        s.grid(row=0, column=0)
        labelTitre = Tk.Label(f, text="", width=50, padx=5, fg="black", bg=self.couleur)
        labelTitre.grid(row=0, column=1)
        #Boutons Lent et Rapide
        boutonLent = Tk.Radiobutton(f, bg=self.couleur, text="Lent", variable=self.numVitesse, value=0, command=self.valnumVitesse)
        boutonRapide = Tk.Radiobutton(f, bg=self.couleur, text="Rapide", variable=self.numVitesse, value=1, command=self.valnumVitesse)
        boutonLent.grid(row=0, column=1)
        boutonRapide.grid(row=0, column=2)
        #Zone pour valider les données
        self.bouttonValider.pack()

        #Affichage des frames
        self.can.pack()
        self.FrameAccueil.pack()

    def Commencer(self):
        self.FrameAccueil.forget()
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
        return self.données

    def Valid(self):
        """Action à executer losrque le bouton valider est appuyer"""
        self.bouttonValider.bind('<ButtonPress>', self.buttonValid)

#    def buttonValid(self, event):
    def buttonValid(self):
        """Action à executer losrque le bouton valider est appuyer"""
        if askyesno('Confirmation', 'Êtes-vous sûr de vouloir valider ces données ?'):
            vc = self.frameParamCapteur.getParamCapteur()
            vd = self.frameParamDecoupe.getParamDecoupe()
            vf = self.frameParamFichier.getParamFichier()
            self.données = (vc + vd + vf)
            showwarning('Merci', 'Vos données ont bien été prises en compte.')
        else:
            pass

    def execute(self):
        """Initiale et affiche la fenetre"""
        self.initialise()
        self.fenetre.mainloop()

# Main
if __name__ == '__main__':
    fen = Fenetre()
    fen.execute()
