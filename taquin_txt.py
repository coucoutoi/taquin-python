#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod: module

:author: FIL - IEEA - Univ. Lille1.fr <http://portail.fil.univ-lille1.fr>_

:date: 2015, december

"""

coups = ['g','G','b','B','h','H','d','D','a','A']
from taquin import *

def lire_coup_a_jouer ():
    """
    lecture d'un coup

    :CU: aucune
    """
    print('nombre de coups joués:',nb_coups[0])
    inp = input ('Votre coup ? ((H)aut, (B)as, (G)auche, (D)roit), (A)bandonner): ')
    while not(inp in coups):
        inp = input ('Votre coup ? ((H)aut, (B)as, (G)auche, (D)roit), (A)bandonner): ')
    return inp.upper()


def jouer (n):
    """
    procédure principale permettant de jouer au jeu du taquin.
    L'entier n détermine la taille nxn du taquin.
    
    :CU: pour des raisons de simplicité on impose à n d'être compris entre
         2 et 9 (bornes comprises)
    """
    assert 2<=n<=9,"n doit être unentier entre 0 et 9"
    taq = cree_taquin (n)
    while est_resolu(taq):
        melanger_taquin (taq)
    imprimer_taquin (taq)
    while not(est_resolu(taq)):
        coup = lire_coup_a_jouer ()
        COMMANDES[coup] (taq)
        if coup=='A':
            if nb_coups[0]!=0:
                print('Vous avez abandonné au bout de',nb_coups[0],'coup(s).')
            else:
                print('Vous avez abandonné sans même avoir essayé.')
    if coup!='A':
        print('Vous avez résolu le taquin en',nb_coups[0],'coups')
    
def usage ():
    print ('Usage : {:s} <n>'.format (sys.argv[0]))
    print ('\t<n> = taille du jeu (2 <= n <= 9)')
    exit (1)

if __name__ == '__main__':
    import sys

    # if len (sys.argv) == 1:
    #     n = 4
    # else:
    #     try:
    #         n = int (sys.argv[1])
    #     except (IndexError, ValueError):
    #         usage ()
    
    # jouer (n)
    # exit (0)

