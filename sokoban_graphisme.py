from tkinter import * 
from PIL import Image 


 

##################################

   #############################
   #                           #
   #       Projet SOKOBAN      #
   #                           #
   #############################
   
Grille=[]
ligneSokoban=8
colonneSokoban=11
nb_caisse=6

reponse="nImporteQuoi"

Grille=[[0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,1,2,2,2,1,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,1,3,2,2,1,0,0,0,0,0,0,0,0,0,0],
        [0,0,1,1,1,2,2,3,1,1,0,0,0,0,0,0,0,0,0],
        [0,0,1,2,2,3,2,3,2,1,0,0,0,0,0,0,0,0,0],
        [1,1,1,2,1,2,1,1,2,1,0,0,0,1,1,1,1,1,1],
        [1,2,2,2,1,2,1,1,2,1,1,1,1,1,2,2,2,4,1],
        [1,2,3,2,2,3,2,2,2,2,2,2,2,2,2,2,2,2,1],
        [1,1,1,1,1,2,1,1,1,2,1,5,1,1,2,2,2,2,1],
        [0,0,0,0,1,2,2,2,2,2,1,1,1,1,1,1,1,1,1],
        [0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]]

def representer(zone):
    """
    procédure permettant d'afficher la représentation
    d'une partie de SOKOBAN codée par zone qui est
    une liste de listes contenant:
    - des 0 : rien
    - des 1 : mur
    - des 2 : emplacement libre
    - des 3 : caisse
    - des 4 : case objectif
    """
    for ligne in zone:
        affichage=""
        for case in ligne:
            if case==0:
                symbole=" "#rien
            elif case==1:
                symbole="M"#mur
            elif case==2:
                symbole=" "#libre
            elif case==3:
                symbole="C"#caisse
            elif case==4:
                symbole="O"#objectif
            elif case==5:
                symbole="S"#sokoban
                
            affichage=affichage+symbole
        print(affichage)
    
######################################"

#GESTION DU GRAPHISME

#################################

def clavier(event):
    global fenetre
    global reponse
    reponse = event.keysym
    fenetre.destroy()



def afficher_jeu(Grille):
    global fenetre
    fenetre = Tk()
    fenetre.title('Sokoban')
    fenetre.iconbitmap('icon.ico')
    largeur=len(Grille[0])
    hauteur=len(Grille)
    taille=50
    num_line=0
    num_case=0
    img = Image.open('mario.gif', 'r')
    x = taille # largeur
    y = taille # hauteur
    img=img.resize((taille,taille))
    img.save('mario_redim.gif')
    mon_mario=PhotoImage(file="mario_redim.gif")
    wall=PhotoImage(file="wall.png")
    box=PhotoImage(file="box.png")
    endpoint=PhotoImage(file="Endpoint.png")
    ground=PhotoImage(file="ground.png")
    character=PhotoImage(file="character.png")
    
    canvas = Canvas(fenetre, width=taille*largeur, height=taille*hauteur, background='white')
    for line in Grille:
        num_line=num_line+1
        for case in line:
            num_case=num_case+1
            if case==0:
                canvas.create_rectangle((num_case-1)*taille, (num_line-1)*taille, num_case*taille, num_line*taille, fill='black')
            if case==1:
                canvas.create_image((num_case-1)*taille+taille/2, (num_line-1)*taille+taille/2,image=wall)
            if case==2:
                canvas.create_image((num_case-1)*taille+taille/2, (num_line-1)*taille+taille/2,image=ground)
            if case==3:
                canvas.create_image((num_case-1)*taille+taille/2, (num_line-1)*taille+taille/2,image=box)
            if case==4:
                canvas.create_image((num_case-1)*taille+taille/2, (num_line-1)*taille+taille/2,image=endpoint)
            if case==5:
                canvas.create_image((num_case-1)*taille+taille/2, (num_line-1)*taille+taille/2,image=character)
                #canvas.create_rectangle((num_case-1)*taille, (num_line-1)*taille, num_case*taille, num_line*taille, fill='pink')
            #else:
                #canvas.create_rectangle((num_case-1)*taille, (num_line-1)*taille, num_case*taille, num_line*taille, fill='white', width=0)
        num_case=0
    canvas.pack()
    canvas.bind_all("<Key>", clavier)
    fenetre.mainloop()
