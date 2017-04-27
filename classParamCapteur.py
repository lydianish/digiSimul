#Librairies
import tkinter as Tk
from tkinter.messagebox import *

class ParametreCapteur:

    """Classe permettant de construire la zone destinee a la saisie et a la recuperation des parametres du capteur"""

    def __init__(self, parent):
        """Constructeur du frame ParametreCapteur"""
        self.couleur = "grey"
        col = "grey60"
        self.couleurManuel = "grey"
        self.couleurAnalyse = "grey"
        self.framePrincipal = Tk.Frame(parent, bg=self.couleur)
        self.frameMode = Tk.Frame(self.framePrincipal, bg=self.couleur)
        self.FrameChoixMode = Tk.Frame(self.framePrincipal)
        self.FrameAffiche = Tk.Frame(self.framePrincipal,bg=self.couleur)
        self.frameRes = Tk.Frame(self.framePrincipal, bg=self.couleur, borderwidth=2, padx=5, pady=5)
        self.frameManuel = Tk.Frame(self.FrameAffiche, bg=self.couleurManuel, padx=5, pady=5, relief=Tk.GROOVE)
        self.frameAnalyse = Tk.Frame(self.FrameAffiche, bg=self.couleurAnalyse, padx=5, pady=5, relief=Tk.SUNKEN)
        self.numMode = Tk.IntVar()
        self.alpha = Tk.StringVar()
        self.alpha.set("1.8")
        self.gama = Tk.StringVar()
        self.gama.set("9")
        self.var = Tk.StringVar()
        self.var.set("2")
        self.dossier = Tk.StringVar()
        self.dossier.set("")
        self.resolution = Tk.StringVar()
        self.resolution.set("120")
        self.largeur = Tk.StringVar()
        self.largeur.set("50")
        self.hauteur = Tk.StringVar()
        self.hauteur.set("100")
        self.nbPoints = Tk.StringVar()
        self.nbPoints.set("3")

    def initialise(self):
        """Ajoute les composantes au frame ParametreCapteur"""

        #Label Titre
        flt = Tk.Frame(self.framePrincipal, bg=self.couleur, padx=5)
        flt.pack()
        labelTitre = Tk.Label(flt, text="CAPTEUR", width=150,font='Calibri 20 bold', bg="grey80")
        labelTitre.pack()
        #Separateur horizontal
        separatorH = Tk.Frame( self.framePrincipal, height=2, bd=1, relief=Tk.SUNKEN)
        separatorH.pack(fill=Tk.X)
        #Label Mode
        flm = Tk.Frame(self.framePrincipal, bg=self.couleur)
        flm.pack()
        labelMode = Tk.Label(flm, text="Mode", width=120, font='Calibri 15 bold', fg="black", bg=self.couleur)
        labelMode.pack()
        labelMode = Tk.Label(flm, text="* Choisissez un mode", width=120, fg="red", bg=self.couleur)
        labelMode.pack()
        # Ajout des composantes au frameMode
        self.frameMode.pack()
        # Zone pour le choix du mode: Manuel ou Analyse
        #Frames
        #FrameChoixMode
        self.FrameChoixMode.pack()
        boutonManuel = Tk.Radiobutton(self.FrameChoixMode, bg=self.couleur, text="Manuel", variable=self.numMode, value=0, command=self.valnumMode)
        boutonManuel.deselect()
        boutonAnalyse = Tk.Radiobutton(self.FrameChoixMode, bg=self.couleur, text="Analyse", variable=self.numMode, value=1, command=self.valnumMode)
        boutonAnalyse.deselect()
        boutonManuel.grid(row=0, column=0)
        boutonAnalyse.grid(row=0, column=1)

        #self.FrameModeManuel
        # Zone pour la saisie des autres données
        # Manuel
        # FrameAlphaGamma
        FrameAlphaGamma = Tk.Frame(self.frameManuel, bg=self.couleurManuel)
        FrameAlphaGamma.pack()
        # Alpha
        labelAlpha = Tk.Label(FrameAlphaGamma, bg=self.couleurManuel, text="Alpha", padx=5, pady=5)
        labelAlpha.grid(row=0, column=0)
        entreeAlpha = Tk.Entry(FrameAlphaGamma, textvariable=self.alpha, width=30)
        entreeAlpha.grid(row=0, column=1)
        # Gamma
        labelGamma = Tk.Label(FrameAlphaGamma, bg=self.couleurManuel, text="Gamma", padx=5, pady=5)
        labelGamma.grid(row=1, column=0)
        entreeGamma = Tk.Entry(FrameAlphaGamma, textvariable=self.gama, width=30)
        entreeGamma.grid(row=1, column=1)

        labelRes = Tk.Label(FrameAlphaGamma, text="     (pour le mode lent)", fg="black", bg=self.couleur)
        labelRes.grid(row=0, column=2,rowspan=2 )

        # Separatuer horizontalMan
        separatorHM = Tk.Frame(self.frameManuel, bg=self.couleur, height=2, bd=1, relief=Tk.SUNKEN)
        separatorHM.pack(fill=Tk.X, padx=5, pady=5)
        # Var
        #FrameVar
        FrameVar = Tk.Frame(self.frameManuel, bg=self.couleurManuel)
        FrameVar.pack()
        #
        labelVar = Tk.Label(FrameVar, bg=self.couleurManuel, text="Variance  ")
        labelVar.grid(row=0, column=0)
        entreeVar = Tk.Entry(FrameVar, textvariable=self.var, width=30)
        entreeVar.grid(row=0, column=1)
        labelRes = Tk.Label(FrameVar, text="    (pour le mode rapide)", fg="black", bg=self.couleur)
        labelRes.grid(row=0, column=2)

        # self.FrameModeAnalyse.
        # Analyse
        labelDossier = Tk.Label(self.frameAnalyse, bg=self.couleurAnalyse, text="* Chemin vers le dossier")
        labelDossier.grid(row=0, column=0)
        entreeDossier = Tk.Entry(self.frameAnalyse, textvariable=self.dossier, width=30)
        entreeDossier.grid(row=0, column=1)

        self.FrameAffiche.pack()


        #Separateur horizontal
        separatorH = Tk.Frame( self.framePrincipal, height=2, bd=1, relief=Tk.SUNKEN)
        separatorH.pack(fill=Tk.X, padx=5, pady=5)

        #Label Caractériques
        flr = Tk.Frame(self.framePrincipal, bg=self.couleur)
        flr.pack()
        labelRes = Tk.Label(flr, text="Caractéristiques",font='Calibri 15 bold', width=120, fg="black", bg=self.couleur)
        labelRes.pack()

        # Ajout des composantes au frameRes
        self.frameRes.pack()
        # Resolution
        labelResolution = Tk.Label(self.frameRes, text="Resolution", bg=self.couleur, padx=5, pady=5)
        labelResolution.grid(row=0, column=0)
        entreeResolution = Tk.Entry(self.frameRes, textvariable=self.resolution, width=30)
        entreeResolution.grid(row=0, column=1)
        Tk.Label(self.frameRes, text="   dpi             ", bg="grey").grid(row=0, column=2)
        # Largeur
        labelLargeur = Tk.Label(self.frameRes, text="Largeur", bg=self.couleur, padx=5, pady=5)
        labelLargeur.grid(row=1, column=0)
        entreeLargeur = Tk.Entry(self.frameRes, textvariable=self.largeur, width=30)
        entreeLargeur.grid(row=1, column=1)
        Tk.Label(self.frameRes, text="   pixels           ", bg="grey").grid(row=1, column=2)
        # Hauteur
        labelHauteur = Tk.Label(self.frameRes, text="Hauteur", bg=self.couleur, padx=5, pady=5)
        labelHauteur.grid(row=2, column=0)
        entreeHauteur = Tk.Entry(self.frameRes, textvariable=self.hauteur, width=30)
        entreeHauteur.grid(row=2, column=1)
        Tk.Label(self.frameRes, text="   pixels           ", bg="grey").grid(row=2, column=2)
        # Nombre de points
        labelnbPoints = Tk.Label(self.frameRes, text="Nombre de point(s)", bg=self.couleur, padx=5, pady=5)
        labelnbPoints.grid(row=3, column=0)
        entreenbPoints = Tk.Entry(self.frameRes, textvariable=self.nbPoints, width=30)
        entreenbPoints.grid(row=3, column=1)

        #Tk.Button(self.framePrincipal, text=" Valider ", command=self.getParamCapteur()).pack()

    # affiche le frameManuel
    def miseAJourCouleurManuel(self):
        self.frameManuel.forget()
        self.frameAnalyse.forget()
        self.frameManuel.pack()


    # affiche le frameManuel
    def miseAJourCouleurAnalyse(self):
        self.frameAnalyse.forget()
        self.frameManuel.forget()
        self.frameAnalyse.pack()


    def valnumMode(self):
        """Methode a executer selon la valeur du numMode"""
        print(self.numMode.get())
        if (self.numMode.get()== 0):
            self.miseAJourCouleurManuel()
        else:
            self.miseAJourCouleurAnalyse()

    def getNumMode(self):
        """Renvoie le numero du mode de traitement des données: 0 pour Manuel et 1 pour Analyse"""
        return self.numMode

    def getFramePrincipal(self):
        """Renvoie le framePrincipal"""
        return self.framePrincipal

    def getParamCapteur(self):
        """Renvoie les valeurs saisies par l'utilisateur . 
           Ces valeurs correspondent aux parametres du capteur"""
        d1 = self.alpha.get()
        d2 =self.gama.get()
        e1 = self.var.get()
        e2 =self.dossier.get()
        f1 = self.resolution.get()
        f2 =self.largeur.get()
        g1 = self.hauteur.get()
        g2 = self.nbPoints.get()
        l = [d1, d2, e1, f1, f2, g1, g2]
        self.estNombre(l)
        return (d1, d2, e1, e2, f1, f2, g1, g2)

    def estNombre(self,n):
        """Affiche un message d'erreur si l'un des elements de n n'est pas un nombre (autrement dit si le type de l'un des elements de n n'est pas un reel)
            n est considere comme une liste de chaines de caracteres"""
        try:
            for i in n:
                fi = float(i)
        except:
            showerror("Erreur de saisie dans la section capteur ", "Erreur, veuillez saisir des nombres")
            return

    def execute(self):
        """Initiale et affiche le frame ParametreCapteur"""
        self.initialise()
        self.framePrincipal.pack()

    def affiche(self):
        """Affiche le frame ParametreCapteur"""
        self.framePrincipal.pack()

# Main
if __name__ == '__main__':
    fen = Tk.Tk()
    pCapteur = ParametreCapteur(fen)
    pCapteur.execute()
    l = pCapteur.getParamCapteur()
    print(l)
    fen.mainloop()
