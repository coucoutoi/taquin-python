def cree_taquin(n):
    """
    cette fonction crée un une liste de taille n*n correspondant au taquin.
    CU: n doit être un entier
    Exemples :
    >>> cree_taquin(4)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]

    >>> cree_taquin(2.5)
    Traceback (most recent call last):
    ...
    AssertionError: n doit être un entier
    """
    assert type(n)==int,'n doit être un entier'
    return [n for n in range(1,n*n)] + [0]

def imprimer_taquin(taq):
    """
    cette fonction affoche le taquin correspondant à la liste taq passé en paramètre.
    CU: taq doit être une liste d'entiers
    Exemples :
    >>> imprimer_taquin([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0])
    +----+----+----+----+
    | 1  | 2  | 3  | 4  |
    +----+----+----+----+
    | 5  | 6  | 7  | 8  |
    +----+----+----+----+
    | 9  | 10 | 11 | 12 |
    +----+----+----+----+
    | 13 | 14 | 15 |    |
    +----+----+----+----+

    >>> imprimer_taquin((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0))
    Traceback (most recent call last):
    ...
    AssertionError: taq doit être une liste d'entiers
    """
    assert type(taq)==list,"taq doit être une liste d'entiers"
    lon = int((len(taq))**(0.5))
    for i in range(lon):
        print('+----'*lon+'+')
        for k in range(i*lon,lon+i*lon):
            if taq[k]>=10:
                print('|',taq[k],'',end='')
            elif taq[k]==0:
                print('|','   ',end='')
            else:
                print('|',taq[k],' ',end='')
        print('|')
    print('+----'*lon+'+')

def position_case_vide(taq):
    """
    cette fonction renvoie les coordonnées de la case vide du taquin passé en paramètre.
    CU: taq doit être une liste
    Exemples :
    >>> position_case_vide([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0])
    (3, 3)
    >>> position_case_vide((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0))
    Traceback (most recent call last):
    ...
    AssertionError: taq doit être une liste d'entiers
    """
    assert type(taq)==list,"taq doit être une liste d'entiers"
    lon = int((len(taq))**(1/2)) 
    c_v = taq.index(0)
    return c_v%lon,c_v//lon

def numero_piece(taq,col,row):
    """
    cette fonction renvoie le numéro correspondant à la colonne col, la ligne row, et le taquin taq passés en paramètre.
    CU: taq doit être une liste, col et row doivent être des entiers
    >>> numero_piece([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0],1,1)
    6

    >>> numero_piece((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0),1,1)
    Traceback (most recent call last):
    ...
    AssertionError: taq doit être une liste d'entiers

    >>> numero_piece([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0],2.5,2.5)
    Traceback (most recent call last):
    ...
    AssertionError: col et row doivent être des entiers

    >>> numero_piece([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0],16,16)
    Traceback (most recent call last):
    ...
    AssertionError: col et row doivent être plus petit que la racine de la longueur de la liste
    """
    assert type(taq)==list,"taq doit être une liste d'entiers"
    assert type(col)==int and type(row)==int,"col et row doivent être des entiers"
    assert row<len(taq)**(1/2) and col<len(taq)**(1/2),"col et row doivent être plus petit que la racine de la longueur de la liste"
    lon = int((len(taq))**(1/2))
    return taq[row*lon+col]

def echanger(taq,pos1,pos2):
    """
    cette fonction échange de place les cases pos1 et pos2 du taquin taq passé en paramètre.
    CU: taq doit être une liste, pos1 et pos2  doivent être des tuples de longueur 2 contenant deux entiers
    Exemples :
    >>> echanger((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0),(3,3),(3,2))
    Traceback (most recent call last):
    ...
    AssertionError: taq doit être une liste
    
    >>> echanger([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0],[3,3],[3,2])
    Traceback (most recent call last):
    ...
    AssertionError: pos1 et pos2 doivent être des tuples
    
    >>> echanger([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0],(3,3,2),(3,2,2))
    Traceback (most recent call last):
    ...
    AssertionError: pos1 et pos2 doivent être de longueur 2
    """
    assert type(taq)==list,"taq doit être une liste"
    assert type(pos1)==tuple and type(pos2)==tuple,"pos1 et pos2 doivent être des tuples"
    assert len(pos1)==2 and len(pos2)==2,"pos1 et pos2 doivent être de longueur 2"
    lon = int((len(taq))**(1/2))
    ip1 = pos1[1]*lon+pos1[0]
    ip2 = pos2[1]*lon+pos2[0]
    taq[ip1],taq[ip2] = taq[ip2],taq[ip1]

def est_resolu(taq):
    """
    cette fonction renvoie True si le taquin est résolu et False sinon.
    CU: taq doit être une liste
    Exemples :
    >>> est_resolu([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0])
    True

    >>> est_resolu('hjkl')
    Traceback (most recent call last):
    ...
    AssertionError: taq doit être une liste
    """
    assert type(taq)==list,"taq doit être une liste"
    resolu = cree_taquin(int(len(taq)**0.5))
    return taq==resolu

def haut(taq=''):
    """
    cette fonction fait un mouvement vers le haut.
    CU: taq doit être une liste d'entiers
    Exemples :
    >>> haut((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0))
    Traceback (most recent call last):
    ...
    AssertionError: taq doit être une liste
    """
    assert type(taq)==list,"taq doit être une liste"
    case_vide = taq.index(0)
    lon = int((len(taq))**(1/2))
    if not(taq=='') and case_vide>(lon-1):
        taq[case_vide], taq[case_vide - lon] = taq[case_vide - lon], taq[case_vide]
        sol[0]='B'+sol[0]
        nb_coups[0]+=1

def bas(taq=''):
    """
    cette fonction fait un mouvement vers le bas.
    CU: taq doit être une liste d'entiers
    Exemples :
    >>> bas((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0))
    Traceback (most recent call last):
    ...
    AssertionError: taq doit être une liste
    """
    assert type(taq)==list,"taq doit être une liste"
    case_vide = taq.index(0)
    lon = int((len(taq))**(1/2))
    if not(taq=='') and case_vide<(len(taq)-lon):
        taq[case_vide], taq[case_vide + lon] = taq[case_vide + lon], taq[case_vide] 
        sol[0]='H'+sol[0]
        nb_coups[0]+=1

def gauche(taq=''):
    """
    cette fonction fait un mouvement vers la gauche.
    CU: taq doit être une liste d'entiers
    Exemples :
    >>> gauche((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0))
    Traceback (most recent call last):
    ...
    AssertionError: taq doit être une liste
    """
    assert type(taq)==list,"taq doit être une liste"
    lon = int((len(taq))**(1/2))
    case_vide = taq.index(0)
    if not(taq=='') and (case_vide%lon!=0 and case_vide!=0):
        taq[case_vide], taq[case_vide - 1] = taq[case_vide - 1], taq[case_vide]
        sol[0]='D'+sol[0]
        nb_coups[0]+=1

def droit(taq=''):
    """
    cette fonction fait un mouvement vers la droite.
    CU: taq doit être une liste d'entiers
    Exemples :
    >>> droit((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0))
    Traceback (most recent call last):
    ...
    AssertionError: taq doit être une liste
    """
    assert type(taq)==list,"taq doit être une liste"
    lon = int((len(taq))**(1/2))
    case_vide = taq.index(0)
    if not(taq=='') and (case_vide+1)%lon:
        taq[case_vide], taq[case_vide + 1] = taq[case_vide + 1], taq[case_vide]
        sol[0]='G'+sol[0]
        nb_coups[0]+=1

def resoudre_taquin(taq=''):
    """
    cette fonction résouds le taquin.
    CU: taq doit être une liste d'entiers
    Exemples :
    >>> resoudre_taquin((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0))
    Traceback (most recent call last):
    ...
    AssertionError: taq doit être une liste
    """
    assert type(taq)==list,"taq doit être une liste"
    import time
    while sol[0]!=simplifier_sol(sol[0]):
        sol[0]=simplifier_sol(sol[0])
    for m in sol[0]:
        time.sleep(0.1)
        COMMANDES[m](taq)
        imprimer_taquin(taq)
        nb_coups[0]-=1
    sol[0]=''

COMMANDES = {'H':haut,'B':bas,'G':gauche,'D':droit,'A':resoudre_taquin}
AUX = ['H','B','D','G']
sol = ['']
nb_coups=[0]

def melanger_taquin(taq):
    """
    cette fonction mélange le taquin passé en paramètre.
    CU: taq doit être une liste d'entiers
    Exemples :
    >>> melanger_taquin([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0])==cree_taquin(4)
    False
    
    >>> melanger_taquin((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0))
    Traceback (most recent call last):
    ...
    AssertionError: taq doit être une liste
    """
    assert type(taq)==list,"taq doit être une liste"
    from random import randint
    for i in range(len(taq)*12):
        r = randint(0,3)
        COMMANDES[AUX[r]](taq)
    nb_coups[0]=0

def simplifier_sol(simp):
    """
    cette fonction simplifie la solution du taquin en lui enlevant deux mouvements consécutifs complémentairs.
    CU: simp doit être une chaîne de caractères composé exclusivement de B, D, G et H
    >>> simplifier_sol('BDGHBBDDBDHHBHHGDBBBGDHGDGBHHGHBGBBHDHBDGHBDBHBDGGDHDHBBHGGHGHDGDGDGDDBBGGHHBDBBDGGHHBDHBGDDDHGBDBGGGHDBDDGDHHHBGGGBHDDHDGDGDGBDBBDBHGHBBGGDGDGDHDBDGGGDDGDHDHHGDBBHGHBDBGDBHGHHDBGDBBGDGDGDHBGHGHDGHBDBHHDBHBBGGGDDBGGDDDGDHBHBHGHBBHBDGHDBHBGDGDHDDBHHHGDBBGBGHHDDBBGHBHBGGDGDHGHHBHDDBGGBHHDBHGDDDGBHDBHGDGBBHGDBDBHHHBBBGHGHBBGHHDDGHDDGDGDBBGGGDHGBDBHBDHHGBBHGHHBHBDBDHGDBGBDDGD')
    'BBDDBDHHHBBBHGHGGBDDBHDGGHGHDDBBGGHDBBGHDDDHGBDBGGGHDBDDHHGGGDDHBDBBDGBGHDBGDHDHHBGDBGHHDBBBGHGHDHDBBGGDBGDDHGBHDBHDDHHBBGBGHHDDBBGGHGHHDDBGGHDDDGBBDHBBGHGBGHHDHDDBBGGHGBDBDHHGBGHDBDHBGBDD'
    """
    i=0
    while i<(len(simp)-1):
        if simp[i:i+2] == 'HB' or simp[i:i+2] == 'BH' or simp[i:i+2] == 'DG' or simp[i:i+2] == 'GD':
            simp = simp[0:i]+simp[i+2:len(simp)]
        else:
            i=i+1
    return simp


if __name__=="__main__":
    import doctest
    doctest.testmod ()
