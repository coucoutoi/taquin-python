#!/usr/bin/python3
# -*- coding: utf-8 -*- 

from tkinter.messagebox import *

sol=['']
compteur=[0]
nb_aff='le nombre de coups joués: '+str(compteur[0])
"""
:mod: module

:author: FIL - IEEA - Univ. Lille1.fr <http://portail.fil.univ-lille1.fr>_
:completed by:

:date: 2015, december

Interface graphique pour jouer eu taquin
"""

from tkinter import *
import tkinter.filedialog as tkfdial

from taquin import *

# nbre de lignes et de pièces par lignes du taquin
DIM_TAQUIN = 4
# dimension en pixels de la taille de l'image du taquin
TAILLE_TAQUIN = 600
# taille d'une pièce carrée du taquin (en pixels)
TAILLE_PIECE = TAILLE_TAQUIN // DIM_TAQUIN
GEOMETRIE = '{:d}x{:d}'.format (30 + 2 * DIM_TAQUIN * TAILLE_PIECE,
                                52 + DIM_TAQUIN * TAILLE_PIECE)

image = None
image_decoupee = [None for k in range(DIM_TAQUIN * DIM_TAQUIN)]
taquin = None
fenetre = None
case_vide = None
puzzle = None
modele = None



def cases_voisines (c1, c2):
    """
    renvoie 
    - True si les cases c1 et c2 sont voisines
    - False sinon
    CU: c1 et c2 doivent être des tuples comportants 2 entiers
    Exemples :
    >>> cases_voisines((1,2), (1,3))
    True

    >>> cases_voisines((1,2), (1,1))
    True

    >>> cases_voisines((1,2), (0,2))
    True

    >>> cases_voisines((1,2), (2,2))
    True

    >>> cases_voisines((1,2), (2,1))
    False

    >>> cases_voisines([1,2],[2,1])
    Traceback (most recent call last):
    ...
    AssertionError: c1 et c2 doivent être des tuples

    >>> cases_voisines((1,2,3),(2,1,3))
    Traceback (most recent call last):
    ...
    AssertionError: c1 et c2 doivent être de longueur 2
    """
    assert type(c1)==tuple and type(c2)==tuple,"c1 et c2 doivent être des tuples"
    assert len(c1)==2 and len(c2)==2,"c1 et c2 doivent être de longueur 2"
    if c1[0]==c2[0]:
        if abs(c1[1]-c2[1])==1:
            return True
        else:
            return False
    elif c1[1]==c2[1]:
        if abs(c1[0]-c2[0])==1:
            return True
        else:
            return False
    else:
        return False

def afficher_pieces ():
    """
    affiche les pièces du puzzle.
    """
    for l in range (DIM_TAQUIN):
        for c in range (DIM_TAQUIN):
            num_piece = numero_piece (taquin, c, l)
            if num_piece==0:
                piece = case_vide         
            else:

                piece = image_decoupee [num_piece - 1]
            puzzle.create_image (c * (TAILLE_PIECE + 1),
                                 l * (TAILLE_PIECE + 1),
                                 anchor = NW,
                                 image = piece)
    if compteur[0]==1:
        var.set('Nombre de coup joué: '+str(compteur[0]))
    elif compteur[0]==0:
        var.set("Aucun coup n'a été joué")
    else:
        var.set('Nombre de coups joués: '+str(compteur[0]))

def melanger ():
    """
    mélange les pièces du taquin
    """
    if image != None:
        melanger_taquin(taquin)
        afficher_pieces()

def sous_image (src,xA,yA,xB,yB):
    """
    renvoie un morceau rectangulaire de l'image ``src``
    depuis le point supérieur gauche de coordonnées (xA,yA)
    au point inférieur droit de coordonnées (xB,yB).
    """
    pce = PhotoImage ()
    pce.tk.call (pce, 'copy', src,
                 '-from', xA, yA, xB, yB, '-to', 0, 0)
    return pce

currentimage=['']

def choix_image ():
    """
    permet de choisir via une boîte de dialogues un fichier contenant une image.

    Ce fichier doit être au format PNG ou GIF, et l'image qu'il contient doit 
    être au moins de taille 600x600.

    L'image choisie est découpée en morceaux.
    Les morceaux sont affichée à gauche, et l'image originale à droite.
    L'ensemble des boutons est ensuite réactivé.
    """
    global image, taquin, imagename
    imagename = tkfdial.askopenfilename (title = 'Choisir une image',
                                         filetypes = [('PNG','.png')])
    if imagename=="" or imagename==():
        imagename=currentimage[0]
    else:
        currentimage[0]=imagename
        taquin = cree_taquin (DIM_TAQUIN)
        image = PhotoImage (file = imagename)
        for k in range (len(image_decoupee)):
            l = k // DIM_TAQUIN
            c = k % DIM_TAQUIN
            image_decoupee[k] = sous_image (image, c * TAILLE_PIECE, l * TAILLE_PIECE,
                                            (c+1) * TAILLE_PIECE, (l+1) * TAILLE_PIECE)
        sol[0]=''
        compteur[0]=0
        melanger()
        modele.create_image (0,0,anchor = NW, image = image)
        Bouton_choix.config(state = NORMAL)
        Bouton_melanger.config(state = NORMAL)
        Bouton_quitter.config(state = NORMAL)
        Bouton_abandon.config(state = NORMAL)

def bouger_piece (event):
    """
    Active le bouton d'abandon et bouge la pièce désignée par le clic de souris (event),
    uniquement si cette pièce est voisine de la case vide tout en gardant en mémoire une trace du mouvement effectué.
    """
    Bouton_abandon.config(state = NORMAL)
    c = event.x // (TAILLE_PIECE + 1)
    l = event.y // (TAILLE_PIECE + 1)
    cv = position_case_vide(taquin)
    if cases_voisines((c,l),cv):
        echanger(taquin,(c,l),cv)
        compteur[0]+=1
        if (c+1==cv[0]) and (l==cv[1]):
            sol[0]='D'+sol[0]
            afficher_pieces ()
            est_res(taquin)
        if c-1==cv[0] and (l==cv[1]):
            sol[0]='G'+sol[0]
            afficher_pieces ()
            est_res(taquin)
        elif l+1==cv[1] and (c==cv[0]):
            sol[0]='B'+sol[0]
            afficher_pieces ()
            est_res(taquin)
        elif l-1==cv[1] and c==cv[0]:
            sol[0]='H'+sol[0]
            afficher_pieces ()
            est_res(taquin)

def est_res(taquin):
    """
    si le taquin est résolu, cette fonction fait apparaitre une fenetre de félicitation avec le nombre de coups joués si le taquin est résolu puis désactive le bouton d'abandon.
    """
    if taquin==cree_taquin(DIM_TAQUIN):
        showinfo('Bravo','vous avez resolu le taquin en '+str(compteur[0])+' coups')
        compteur[0]=0
        var.set('nombre de coups joués: '+str(compteur[0]))
        Bouton_abandon.config(state = DISABLED)
    

def resoudre():
    """
    cette fonction résouds le taquin et désactive les boutons et l'évènement click pendant cette execution.
    """
    import time
    puzzle.bind ('<Button-1>',DISABLED)
    Bouton_abandon.config(state = DISABLED)
    Bouton_quitter.config(state = DISABLED)
    Bouton_melanger.config(state = DISABLED)
    Bouton_choix.config(state = DISABLED)
    while sol[0]!=simplifier_sol(sol[0]):
        sol[0]=simplifier_sol(sol[0])
    i=0
    for m in sol[0]:
        time.sleep(0.1)
        cv=position_case_vide(taquin)
        if m=='H':
            echanger(taquin,(cv[0],cv[1]-1),cv)
        elif m=='B':
            echanger(taquin,(cv[0],cv[1]+1),cv)
        elif m=='D':
            echanger(taquin,(cv[0]+1,cv[1]),cv)
        elif m=='G':
            echanger(taquin,(cv[0]-1,cv[1]),cv)
        elif est_res(taquin):
            break
        afficher_pieces()
        var.set('Le taquin se résoud veuillez patienter'+'.'*(i%5))
        fenetre.update()
        i+=1
    sol[0]=''
    if compteur[0]!=0:
        showinfo('Game Over', "Honte à vous, vous venez d'abandonner la partie après "+str(compteur[0])+" coup(s).")
    else:
        showinfo('Game Over',"Honte à vous, vous venez d'abandonné la partie sans avoir essayé de résoudre ce taquin...")
    compteur[0]=0
    var.set("Choisissez ce que vous souhaitez faire")
    puzzle.bind ('<Button-1>',bouger_piece)

def btn_abandon():
    """
    cette fonction fait apparaitre une popup qui nous propose de voir la solution au taquin et active les boutons lorsque le taquin est résolu.
    """
    result = askquestion("Abandon","Voulez-vous voir la solution?")
    if result=='yes':
        resoudre()
        Bouton_choix.config(state = NORMAL)
        Bouton_melanger.config(state = NORMAL)
        Bouton_quitter.config(state = NORMAL)
    else:
        global image, taquin, imagename
        taquin = cree_taquin (DIM_TAQUIN)
        image = PhotoImage (file = imagename)
        for k in range (len(image_decoupee)):
            l = k // DIM_TAQUIN
            c = k % DIM_TAQUIN
            image_decoupee[k] = sous_image (image, c * TAILLE_PIECE, l * TAILLE_PIECE,
                                            (c+1) * TAILLE_PIECE, (l+1) * TAILLE_PIECE)
        sol[0]=''
        compteur[0]=0
        modele.create_image (0,0,anchor = NW, image = image)
        afficher_pieces()

def btn_melanger():
    """
    cette fonction remet le taquin à 0 pour le mélanger ensuite tout en réactivant le bouton d'abandon.
    """
    Bouton_abandon.config(state = NORMAL)
    global image, taquin, imagename
    taquin = cree_taquin (DIM_TAQUIN)
    image = PhotoImage (file = imagename)
    for k in range (len(image_decoupee)):
        l = k // DIM_TAQUIN
        c = k % DIM_TAQUIN
        image_decoupee[k] = sous_image (image, c * TAILLE_PIECE, l * TAILLE_PIECE,
                                        (c+1) * TAILLE_PIECE, (l+1) * TAILLE_PIECE)
    sol[0]=''
    compteur[0]=0
    melanger()
    modele.create_image (0,0,anchor = NW, image = image)

def main ():
    """
    cette fonction est le jeu du taquin
    """
    global fenetre, case_vide, puzzle, modele, montexte, var, Bouton_abandon, Bouton_quitter, Bouton_melanger, Bouton_choix, puzzle


    # La fenêtre principale
    fenetre = Tk ()
    fenetre.title ('Jeu du taquin')
    fenetre.geometry (GEOMETRIE)
    fenetre.resizable (width=False, height= False)

    # L'image représentant la case vide
    case_vide = sous_image(PhotoImage(file='images/case_vide_bleue.gif'),
                           0, 0,
                           TAILLE_PIECE-1, TAILLE_PIECE-1)

    # La zone gauche contenant le puzzle
    puzzle = Canvas (fenetre, width = TAILLE_PIECE * DIM_TAQUIN + DIM_TAQUIN - 1,
                     height = TAILLE_PIECE * DIM_TAQUIN +  DIM_TAQUIN - 1,
                     background = 'blue')
    puzzle.bind ('<Button-1>',bouger_piece)
    puzzle.grid (row=0, column=0, rowspan = DIM_TAQUIN, columnspan = DIM_TAQUIN,
                 padx = 6, pady = 8)

    # La zone droite contenant l'image modèle à reconstituer
    modele = Canvas (fenetre, width = TAILLE_PIECE * DIM_TAQUIN,
                     height = TAILLE_PIECE * DIM_TAQUIN,
                     background = 'black')
    modele.grid (row=0, column=DIM_TAQUIN, rowspan = DIM_TAQUIN,
                 columnspan = DIM_TAQUIN, padx=6, pady=8)

    # La zone du bas contenant les boutons
    Bouton_choix = Button (fenetre, text ='Choix image',
                           command = choix_image)
    Bouton_choix.grid (row = DIM_TAQUIN, column = 1, padx = 5, sticky = N)

    Bouton_melanger = Button (fenetre, text ='Mélanger',
                              command = btn_melanger)
    Bouton_melanger.grid(row = DIM_TAQUIN, column = 2)
    Bouton_melanger.config(state = DISABLED)

    Bouton_quitter = Button (fenetre, text ='Quitter',
                             command = fenetre.destroy)
    Bouton_quitter.grid(row = DIM_TAQUIN, column = 3)

    Bouton_abandon =  Button (fenetre, text='Abandon',
                              command = btn_abandon)
    Bouton_abandon.grid(row = DIM_TAQUIN, column = 4)
    Bouton_abandon.config(state = DISABLED)

    var=StringVar()
    nb_coups=Label(fenetre, textvariable=var)
    nb_coups.grid(row = DIM_TAQUIN, column = 5)

    var.set("Choisissez une image pour commencer")
    
    fenetre.mainloop ()

if __name__ == '__main__':
    import doctest
    doctest.testmod ()


    main ()
