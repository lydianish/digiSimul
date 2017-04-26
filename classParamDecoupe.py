#Librairies
import tkinter as Tk
from tkinter.messagebox import *

class ParametreDecoupe:

    """Classe permettant de construire la zone destinee a la saisie et a la recuperation des parametres de la decoupe"""

    def __init__(self, parent):
        """Constructeur du frame ParametreDecoupe"""
        self.couleur = "grey"
        self.framePrincipal = Tk.Frame(parent, bg=self.couleur)
        self.minX = Tk.StringVar()
        self.minX.set("0")
        self.maxX = Tk.StringVar()
        self.maxX.set("100")
        self.minY = Tk.StringVar()
        self.minY.set("0")
        self.maxY = Tk.StringVar()
        self.maxY.set("100")
        self.minA = Tk.StringVar()
        self.minA.set("0")
        self.maxA = Tk.StringVar()
        self.maxA.set("100")

    def initialise(self):
        """Ajoute les composantes au frame ParametreDecoupe"""

        #Label Titre
        fltd = Tk.Frame(self.framePrincipal, bg=self.couleur, padx=5)
        fltd.pack()
        labelTitred = Tk.Label(fltd, text="DECOUPE", width=150,font='Calibri 20 bold', fg="black", bg="grey80")
        labelTitred.pack()

        #Separateur horizontal
        separatorH = Tk.Frame( self.framePrincipal, height=2, bd=1, relief=Tk.SUNKEN)
        separatorH.pack(fill=Tk.X)

        #fp
        fp = Tk.Frame(self.framePrincipal, bg=self.couleur, padx=5, pady=5)
        fp.pack()
        #Position en x
        labelX = Tk.Label(fp, text="    Position en x    :", bg=self.couleur, padx=5, pady=5)
        labelX.grid(row=0, column=0)
        # Min
        labelminX = Tk.Label(fp, text="Min", bg=self.couleur)
        labelminX.grid(row=0, column=1)
        entreeminX = Tk.Entry(fp, textvariable=self.minX, width=30)
        entreeminX.grid(row=0, column=2)
        #Max
        labelmaxX = Tk.Label(fp, text="   Max", bg=self.couleur)
        labelmaxX.grid(row=0, column=3)
        entreemaxX = Tk.Entry(fp, textvariable=self.maxX, width=30)
        entreemaxX.grid(row=0, column=4)

        # Position en y
        labelY = Tk.Label(fp, text="    Position en y    :", bg=self.couleur, padx=5, pady=5)
        labelY.grid(row=1, column=0)
        # Min
        labelminY = Tk.Label(fp, text="Min", bg=self.couleur)
        labelminY.grid(row=1, column=1)
        entreeminY = Tk.Entry(fp, textvariable=self.minY, width=30)
        entreeminY.grid(row=1, column=2)
        # Max
        labelmaxY = Tk.Label(fp, text="Max", bg=self.couleur)
        labelmaxY.grid(row=1, column=3)
        entreemaxY = Tk.Entry(fp, textvariable=self.maxY, width=30)
        entreemaxY.grid(row=1, column=4)

        # Angle de rotation
        labelA = Tk.Label(fp, text="Angle de rotation :", bg=self.couleur, padx=5, pady=5)
        labelA.grid(row=2, column=0)
        #Min
        labelminA = Tk.Label(fp, text="Min", bg=self.couleur)
        labelminA.grid(row=2, column=1)
        entreeminA = Tk.Entry(fp, textvariable=self.minA, width=30)
        entreeminA.grid(row=2, column=2)
        #Max
        labelmaxA = Tk.Label(fp, text="Max", bg=self.couleur)
        labelmaxA.grid(row=2, column=3)
        entreemaxA = Tk.Entry(fp, textvariable=self.maxA, width=30)
        entreemaxA.grid(row=2, column=4)

        la = Tk.Label(fp, text="  degré(s)", fg="black", bg=self.couleur)
        la.grid(row=2, column=5)

        #Tk.Button(self.framePrincipal, text=" Valider ", command=self.getParamDecoupe).pack()

    def getFramePrincipal(self):
        """Renvoie le framePrincipal"""
        return self.framePrincipal

    def getParamDecoupe(self):
        """Renvoie les valeurs saisies par l'utilisateur . 
           Ces valeurs correspondent aux parametres de la decoupe"""
        a1 = self.minX.get()
        a2 =self.maxX.get()
        b1 = self.minY.get()
        b2 =self.maxY.get()
        c1 = self.minA.get()
        c2 =self.maxA.get()
        l = [a1, a2, b1, b2, c1, c2]
        self.estNombre(l)
        #print(a1, a2, b1, b2, c1, c2)
        return (a1, a2, b1, b2, c1, c2)

    def estNombre(self,n):
        """Affiche un message d'erreur si l'un des elements de n n'est pas un nombre (autrement dit si le type de l'un des elements de n n'est pas un reel)
            n est considere comme une liste de chaines de caracteres"""
        try:
            for i in n:
                fi = float(i)
        except:
            showerror("Erreur de saisie dans la section decoupe ", "Erreur, veuillez saisir des nombres")
            return

    def execute(self):
        """Initiale et affiche le frame ParametreDecoupe"""
        self.initialise()
        self.framePrincipal.pack()

    def affiche(self):
        """Affiche le frame ParametreDecoupe"""
        self.framePrincipal.pack()

# Main
if __name__ == '__main__':
    fen = Tk.Tk()
    pDecoupe = ParametreDecoupe(fen)
    pDecoupe.execute()
    l = pDecoupe.getParamDecoupe()
    print(l)
    fen.mainloop()
