#Librairies
from tkinter import ttk
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

        # Fonction permettant de lier le déplacement de la fenêtre avec la molette de la souris
        def scrollEvent(event):
            # print (event.delta)
            if event.delta > 0:
                # print ('déplacement vers le haut')
                self.canevas.yview_scroll(-2, 'units')

            else:
                # print ('déplacement vers le bas')
                self.canevas.yview_scroll(2, 'units')

        # Lorsque l'on rentre dans la fenêtre, on active la molette
        def enrEnter(event):
            self.fenetre.bind('<MouseWheel>', scrollEvent)

        # Lorsque l'on sort de la fenêtre, on désactive la liaison avec la molette
        def enrLeave(event):
            self.fenetre.unbind('<MouseWheel>')

        # Création de la fenêtre principale
        self.couleur = "grey"
        self.fenetre = Tk.Tk()
        #self.fenetre.geometry("1260x680")
        self.fenetre.title("DigiSimul")
        self.fenetre['bg'] = 'grey'

        # Création de la scrollbar
        self.scroll = Tk.Scrollbar(self.fenetre, orient=Tk.VERTICAL)
        self.scroll.grid(row=0, column=1, sticky=Tk.N + Tk.S)
        self.scroll1 = Tk.Scrollbar(self.fenetre, orient=Tk.HORIZONTAL)
        self.scroll1.grid(row=1, column=0, sticky=Tk.E + Tk.W)

        # Création du canevas qui contient la frame qui contient les boutons
        self.canevas = Tk.Canvas(self.fenetre,yscrollcommand=self.scroll.set,xscrollcommand=self.scroll1.set)
        self.canevas.config(width = 1230, height = 1500)

        self.fenetre.grid_columnconfigure(0,weight=1)
        self.fenetre.grid_rowconfigure(0,weight=1)
        self.fp = Tk.Frame(self.canevas)

        #Création de la frame contenant le CanvasPrincipal
        self.fex = Tk.Frame(self.fp)
        self.fex.pack()

        # Conteneur Principal: Canvas
        self.can = Tk.Canvas(self.fex)
        self.can.config(width=1230, height=850)
        self.can.pack()

        #Ecran d'accueil: DigiSimul
        self.FrameAccueil = Tk.Frame(self.can, width = 1230, height = 650)
        self.photo = None
        self.bouttonCommencer = Tk.Button(self.FrameAccueil, width = 40, height = 2, text=" Pour commencer, veuillez cliquez ici",font='Calibri 20', command=self.Commencer, cursor="hand2")
        #Frame Pricipal: pour la saisie des données
        self.framePrincipal = Tk.Frame(self.can, width = 1230, height = 650, bg=self.couleur)
        self.frameParamCapteur = ParametreCapteur(self.framePrincipal)
        self.frameParamDecoupe = ParametreDecoupe(self.framePrincipal)
        self.frameParamFichier = ParametreFichier(self.framePrincipal)
        self.frameParamVitesse = Tk.Frame(self.framePrincipal, bg=self.couleur)
        self.numVitesse = Tk.IntVar()
        self.frameParamValidation = Tk.Frame(self.framePrincipal)
        self.bouttonValider = Tk.Button(self.frameParamValidation, width = 10, text=" Valider ",font='Calibri 15', padx=5, pady=5, command=self.buttonValid, cursor="hand2")
        self.données = ()
        self.framebBarreDeProgression = Tk.Frame(self.framePrincipal, bg=self.couleur)
        self.barreDeProgression = ttk.Progressbar(self.framebBarreDeProgression, orient="horizontal", length=300, mode="determinate")
        self.bouttonProgStop = Tk.Button(self.framebBarreDeProgression, text=" STOP", bg="grey", command=self.stopBarreProg, cursor="hand2")


        # Pack du canevas
        self.canevas.grid(row=0, column=0)

        # Configuration de la scrollbar
        self.scroll.config(command=self.canevas.yview)
        self.scroll1.config(command=self.canevas.xview)

        # Positionnement du canevas au début
        self.canevas.create_window(0, 0, window=self.fp)
        self.fp.update_idletasks()
        self.canevas.config(scrollregion=self.canevas.bbox('all'))
        self.canevas.yview_moveto(0)
        self.canevas.xview_moveto(0)

    def initialise(self):
        """Ajoute les composantes a la fenetre"""

        #FRAME ACCUEIL
        #Zone pour l'affichage de l'image
        labelTitre = Tk.Label(self.FrameAccueil, text="BIENVENUE sur ...", font='Calibri 24', width=50, height=2, padx=5, fg="black")
        labelTitre.pack()
        # Image
        chemin = "digiSimul.png"
        image = Image.open(chemin)
        im = (image.copy()).resize((1000,500), Image.ANTIALIAS)
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
        labelTitre = Tk.Label(flt, text="VITESSE", font='Calibri 20 bold', width=150, padx=5, fg="black", bg="grey80")
        labelTitre.pack()
        #Separateur horizontal
        separatorH = Tk.Frame(flt, height=2, bd=1, relief=Tk.SUNKEN)
        separatorH.pack(fill=Tk.X)
        f = Tk.Frame(flt, bg=self.couleur)
        f.pack()
        #SpinBox :
        laSpinBox = Tk.Label(f, text="Nombre de coeur(s) utilisé(s)", fg="black", bg=self.couleur)
        laSpinBox.grid(row=0, column=0)
        s = Tk.Spinbox(f, from_=1, to=10)
        s.grid(row=0, column=1)
        labelTitre = Tk.Label(f, text="", width=10, padx=5, fg="black", bg=self.couleur)
        labelTitre.grid(row=0, column=2)
        #Boutons Lent et Rapide
        boutonLent = Tk.Radiobutton(f, bg=self.couleur, text="Lent", variable=self.numVitesse, value=0, command=self.valnumVitesse)
        boutonRapide = Tk.Radiobutton(f, bg=self.couleur, text="Rapide", variable=self.numVitesse, value=1, command=self.valnumVitesse)
        boutonLent.grid(row=0, column=3)
        boutonRapide.grid(row=0, column=4)
        #Zone pour valider les données
        self.bouttonValider.pack()

        #Barre de progression:
        labelprogression = Tk.Label(self.framebBarreDeProgression, text="Traitement des données", padx=5, fg="black", bg=self.couleur)
        labelprogression.grid(row=0, column=0)
        self.barreDeProgression.grid(row=0, column=1)
        self.barreDeProgression.start()
        self.bouttonProgStop.grid(row=0, column=2)

        #Affichage des frames
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

    def stopBarreProg(self):
        self.bouttonProgStop.config(state='disabled')
        self.barreDeProgression.stop()

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
            # showinfo('Merci', 'Vos données ont bien été prises en compte.')
            self.startTraitementDonnee()
        else:
            pass

    def startTraitementDonnee(self):
        self.frameParamValidation.forget()
        separatorH = Tk.Frame(self.framePrincipal, height=2, bd=1, relief=Tk.SUNKEN)
        separatorH.pack(fill=Tk.X)
        self.framebBarreDeProgression.pack()

    def execute(self):
        """Initiale et affiche la fenetre"""
        self.initialise()
        self.fenetre.mainloop()

# Main
if __name__ == '__main__':
    fen = Fenetre()
    fen.execute()
