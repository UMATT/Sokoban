from sokoban_graphisme import *

Grille= [[0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 3, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 1, 1, 2, 2, 3, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 2, 2, 3, 2, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 1, 1, 2, 1, 2, 1, 1, 2, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
         [1, 2, 2, 2, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 2, 2, 4, 1],
         [1, 2, 3, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
         [1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 5, 1, 1, 2, 2, 2, 2, 1],
         [0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]]

nb_caisse=6
ligneSokoban=8
colonneSokoban=11

# -4 : Grille[ligneSokoban][colonneSokoban] = 3

# -6 : ligneSokoban=8 / colonneSokoban=11

def representerLigne(ligne) :
    affichage=""
    for case in ligne:
        if case==0 :
            symbole=" "#rien
        elif case==1 :
            symbole="M"#mur
        elif case==2 :
            symbole=" "#libre
        elif case==3 :
            symbole="C"#caisse
        elif case==4 :
            symbole="O"#objectif
        elif case==5 :
            symbole="S"#sokoban
        affichage=affichage+symbole
    print(affichage)
    
def representer(Grille):
    for ligne in Grille:
        affichage=""
        for case in ligne:
            if case==0 :
                symbole=" "#rien
            elif case==1 :
                symbole="M"#mur
            elif case==2 :
                symbole=" "#libre
            elif case==3 :
                symbole="C"#caisse
            elif case==4 :
                symbole="O"#objectif
            elif case==5 :
                symbole="S"#sokoban
            affichage=affichage+symbole
        print(affichage)
        
def deplacer(direction) :
    global Grille
    global ligneSokoban
    global colonneSokoban
    global nb_caisse
    
    if direction=="Z" or direction=="z" :
        if Grille[ligneSokoban-1][colonneSokoban] == 2:
            Grille[ligneSokoban][colonneSokoban] = 2
            ligneSokoban = ligneSokoban-1
            Grille[ligneSokoban][colonneSokoban] = 5
        elif Grille[ligneSokoban-1][colonneSokoban] == 3:
            Grille[ligneSokoban][colonneSokoban] = 2
            ligneSokoban = ligneSokoban - 1
            Grille[ligneSokoban][colonneSokoban] = 5
            Grille[ligneSokoban-1][colonneSokoban] = 3
            if Grille[ligneSokoban-2][colonneSokoban] == 4 :
                Grille[ligneSokoban][colonneSokoban] = 2
                ligneSokoban= ligneSokoban - 1
                Grille[ligneSokoban][colonneSokoban] = 5
                nb_caisse=nb_caisse - 1
                
    if direction=="S" or direction=="s" :
        if Grille[ligneSokoban+1][colonneSokoban] == 2:
            Grille[ligneSokoban][colonneSokoban] = 2
            ligneSokoban = ligneSokoban+1
            Grille[ligneSokoban][colonneSokoban] = 5
        elif Grille[ligneSokoban+1][colonneSokoban] == 3:
            Grille[ligneSokoban][colonneSokoban] = 2
            ligneSokoban = ligneSokoban + 1
            Grille[ligneSokoban][colonneSokoban] = 5
            Grille[ligneSokoban+1][colonneSokoban] = 3
            if Grille[ligneSokoban+2][colonneSokoban] == 4 :
                Grille[ligneSokoban][colonneSokoban] = 2
                ligneSokoban= ligneSokoban + 1
                Grille[ligneSokoban][colonneSokoban] = 5
                nb_caisse=nb_caisse - 1  
                
    if direction=="Q" or direction=="q" :
        if Grille[ligneSokoban][colonneSokoban-1] == 2:
            Grille[ligneSokoban][colonneSokoban] = 2
            colonneSokoban = colonneSokoban-1
            Grille[ligneSokoban][colonneSokoban] = 5
        elif Grille[ligneSokoban][colonneSokoban-1] == 3:
            Grille[ligneSokoban][colonneSokoban] = 2
            colonneSokoban = colonneSokoban - 1
            Grille[ligneSokoban][colonneSokoban] = 5
            Grille[ligneSokoban][colonneSokoban-1] = 3
            if Grille[ligneSokoban][colonneSokoban-2] == 4 :
                Grille[ligneSokoban][colonneSokoban] = 2
                colonneSokoban = colonneSokoban -1
                Grille[ligneSokoban][colonneSokoban] = 5
                nb_caisse=nb_caisse - 1


                
    if direction=="D" or direction=="d" :
        if Grille[ligneSokoban][colonneSokoban+1] == 2:
            Grille[ligneSokoban][colonneSokoban] = 2
            colonneSokoban = colonneSokoban+1
            Grille[ligneSokoban][colonneSokoban] = 5
        elif Grille[ligneSokoban][colonneSokoban+1] == 3:
            Grille[ligneSokoban][colonneSokoban] = 2
            colonneSokoban = colonneSokoban + 1
            Grille[ligneSokoban][colonneSokoban] = 5
            Grille[ligneSokoban][colonneSokoban + 1] = 3
            if Grille[ligneSokoban][colonneSokoban+2] == 4 :
                Grille[ligneSokoban][colonneSokoban] = 2
                colonneSokoban = colonneSokoban +1
                Grille[ligneSokoban][colonneSokoban] = 5
                nb_caisse=nb_caisse - 1

# -11 : Oui, la case au dessus du Sokoban est une case libre.
# -12 : Elle permet de vérifier si la case du dessus est une case libre.

def jouer_Sokoban() :
    global Grille
    global ligneSokoban
    global colonneSokoban
    global nb_caisse
    
    representer(Grille)
    reponse="nImporteQuoi"
    while nb_caisse > 0 :
        print("Votre déplacement (z/q/s/d) ou r pour recommencer ? ")
        afficher_jeu(Grille)
        deplacer(reponse)
        
    if reponse=="r" :
        print("ce n’est pas grave, tu feras mieux la prochaine fois...")
    else :
        print("Bravo ! ! !")
    
    try_again=input("Voulez vous refaire une partie (y/n - y par défaut)")
    if try_again !="n" :
        jouer_Sokoban()
    else :
        print("A bientôt")
jouer_Sokoban()
