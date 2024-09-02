from upemtk import *
from time import sleep
from random import *
from doctest import testmod

# dimensions du jeu
taille_case = 15
largeur_plateau = 40  # en nombre de cases
hauteur_plateau = 30  # en nombre de cases

#images
image_debut = "image_debut.png"
image_obstacle = "block_obstacle.png"
menu = True

def case_vers_pixel(case):
    """
	Fonction recevant les coordonnées d'une case du plateau sous la 
	forme d'un couple d'entiers (id_colonne, id_ligne) et renvoyant les 
	coordonnées du pixel se trouvant au centre de cette case. Ce calcul 
	prend en compte la taille de chaque case, donnée par la variable 
	globale taille_case.
    """
    i, j = case
    return (i + .5) * taille_case, (j + .5) * taille_case

    
def affiche_pommes(pommes):
    """
    Fonction recevant les coordonnées de la liste pommes comprenant toutes les coordonées
    des pommes affichées jusqu'à présent sous la forme d'un couple d'entiers 
    (x, y) et affichant les pommes.
    """
    for pomme in pommes:
        x, y = case_vers_pixel(pomme)
        cercle(x, y, taille_case/2,
               couleur='darkred', remplissage='red')
        rectangle(x-2, y-taille_case*.4, x+2, y-taille_case*.7,
                  couleur='darkgreen', remplissage='darkgreen')

def ajoute_pommes():
    """
    Fonction qui ajoute de manière aléatoire sur la carte une pomme sur 
    une case vide.
    """
    while contre_2 == False:
        simu_coord = (randint(0,39), randint(0,29))
    
        while True:
            if simu_coord not in serpent and simu_coord not in pommes and simu_coord not in obstacles:
                pommes.append(simu_coord)
                return
            
def affiche_obstacles(obstacles):
    """
    Fonction recevant les coordonnées de la liste obstacles comprenant toutes les coordonées
    des obstacles affichées jusqu'à présent sous la forme d'un couple d'entiers 
    (x, y) et affichant les obstacles.
    """

    for obstacle in obstacles:
        x, y = case_vers_pixel(obstacle)
        image(x, y, image_obstacle, ancrage='center', tag='')
        
def ajoute_obstacles():
    """
    Fonction qui ajoute de manière aléatoire sur la carte un obstacle sur 
    une case vide.
    """
    simu_coord = (randint(0,39), randint(0,29))
    
    while True:
        if simu_coord not in serpent and simu_coord not in pommes and simu_coord not in obstacles:
            obstacles.append(simu_coord)
            return
            
def affiche_serpent(serpent):
    """
    Fonction qui affiche le serpent partant de sa tête en debut de partie
    et qui augmente de 1 à chaque pomme manger.
    """
    for boule in range(len(serpent)):
        x, y = case_vers_pixel(serpent[boule])  # à modifier !!! fait

        cercle(x, y, taille_case/2 + 1,
               couleur='darkgreen', remplissage='green')
        
    if contre_2 == True:
        for boule in range(len(serpent2)):
            x, y = case_vers_pixel(serpent2[boule])
            
            cercle(x, y, taille_case/2 + 1,
                   couleur='darkblue', remplissage='blue')
            
def change_direction(direction, touche, mouvement):
    """
    Fonction gérant la direction que le serpent vas prendre.
    >>> change_direction((0,0),'Down','Right')
    ((0, 1), 'Down')
    >>> change_direction((10,12),'Up','Left')
    ((0, -1), 'Up')
    >>> change_direction((15,9),'Left','Right')
    ((15, 9), 'Right')
    """
    # à compléter !!! fait
    if touche == 'Up' and mouvement != 'Down':
        # flèche haut pressée
        mouvement = 'Up' 
        return ((0, -1), mouvement)
    
    elif touche == 'Down' and mouvement != 'Up':
        # flèche bas pressée
        mouvement = 'Down' 
        return ((0, 1), mouvement)
    
    elif touche == 'Left' and mouvement != 'Right':
        # flèche gauche pressée         
        mouvement = 'Left' 
        return ((-1, 0), mouvement)
    
    elif touche == 'Right' and mouvement != 'Left':
        # flèche droite pressée
        mouvement = 'Right' 
        return ((1, 0), mouvement)
    
    else:
        # pas de changement !
        return (direction, mouvement)
    
def change_direction_2(direction, touche, mouvement):
    """
    Fonction gérant la direction que le serpent 2 va prendre.
    >>> change_direction((0,0),'s','d')
    ((0, 1), 's')
    >>> change_direction((10,12),'z','q')
    ((0, -1), 'z')
    >>> change_direction((15,9),'q','d')
    ((15, 9), 'd')
    """
    if touche == 'z' and mouvement != 's':
        # Z pressée
        mouvement = 'z'
        return ((0, -1), mouvement)
    
    elif touche == 's' and mouvement != 'z':
        # S pressée
        mouvement = 's'
        return ((0, 1), mouvement)
    
    elif touche == 'q' and mouvement != 'd':
        # Q pressée
        mouvement = 'q'
        return ((-1, 0), mouvement)
    
    elif touche == 'd' and mouvement != 'q':
        # D pressée
        mouvement = 'd'
        return ((1, 0), mouvement)
    
    else :
        return (direction, mouvement) 
    

def fonctions_serpent(direction,direction_2 ,lst_serpent,lst_serpent2):
    """
    Fonction permettant de faire fonctionner le serpent prenant en compte le jeu classique, 
    l'arene torique (qui permet de faire un tour c'est-à-dire passer d'un bord a son opposé),
    et le mode multijoueur (où il y a deux serpents qui jouent).
    
    Elle reçoit la direction du serpent et celle du serpent 2, ainsi que la 
    liste des coordonées du serpent et celle du serpent 2). 
    
    tete_x représente la tete du serpent et tete_y représente le corps du serpent.
    tete_w représente la tete du serpent et tete_z représente le corps du serpent.     
    """
    #coordonées du serpent pour la simulation
    tete_x, tete_y = lst_serpent[-1]
    test_x = tete_x + direction[0]
    test_y = tete_y + direction[1]
    
    #coordonées du serpent 2 pour la simulation
    tete_w, tete_z = lst_serpent2[-1]    
    test_w = tete_w + direction_2[0]
    test_z = tete_z + direction_2[1]
    
    #print(test_x)
    #print(test_y)
    #print(test_w)
    #print(test_z)

    #Version arène torique (PACMAN)
    if arene_torique == True:
        if test_y < 0:
            tete_y = 30
        elif test_y > 29:
            tete_y = 0
            
        if test_x < 0:
            tete_x = 40 
        elif test_x > 39:
            tete_x = 0
    
    #Version multijoueur
    elif contre_2 == True:
        mvm = True
        mvm_2 = True    
        
        #sortie de fenêtre
        if test_w < 0 or test_w > 39 or test_z < 0 or test_z > 29: #si le serpent 2 sort de la fenêtre
            return False, 2
        if test_x < 0 or test_x > 39 or test_y < 0 or test_y > 29: #si le serpent sort de la fenêtre
            return False, 1
        
        #rencontre obstacle
        if (tete_w,tete_z) in obstacles: #si le serpent 2 rencontre un obstacle
            return False, 2
        
        #rencontre l'autre serpent
        if (tete_w,test_z) == (tete_x,test_y): #si la tête des deux serpents se rencontrent
            return False, 0
        
        if (tete_w,tete_z) in serpent: #si le serpent 2 touche serpent 
            return False, 2
        
        if (tete_x,tete_y) in serpent2: #si le serpent touche serpent 2
            return False, 1
        
        #rencontre soi même   
        if len(serpent) > 2 and (test_x,test_y) in serpent: #si le serpent rencontre une partie de son corps
            return False, 1
            
        if len(serpent2) > 2 and (test_w,test_z) in serpent2: #si le serpent2 rencontre une partie de son corps
            return False, 2
        
        #ajouter un nouveau segment au serpent
        while direction != (0,0) and mvm == True:
             serpent.append((tete_x + direction[0], tete_y + direction[1])) #ajoute un nouveau segment au serpent
             mvm = False
             
        while direction_2 != (0,0) and mvm_2 == True:
             serpent2.append((tete_w + direction_2[0], tete_z + direction_2[1]))
             mvm_2 = False
        
    #Version basique        
    else : 
        if test_x < 0 or test_x > 39 or test_y < 0 or test_y > 29: #si le serpent sort de la fenêtre
            return False, 0
        if len(serpent) > 2 and (test_x,test_y) in serpent : #si le serpent rencontre une partie de son corps
            return False, 0


    #autres fonctions du serpent en plus
    if contre_2 == False:
        
        if len(serpent) > 2 and (test_x,test_y) in serpent and contre_2 == False: #si le serpent rencontre une partie de son corps
            return False, 0
        
        if (tete_x,tete_y) in obstacles: #si le serpent rencontre un obstacle
            return False, 0
            print("obstacle")
            
        if (test_x,test_y) in pommes: #si le serpent mange la pomme
            pommes.remove((test_x,test_y))
    
        else:   #uniquement si le jeu n'est pas arrêté et que le serpent mange pas de pomme
            serpent.pop(0) #retire un segment au serpent
            serpent2.pop(0)
        
        #ajouter un nouveau segment au serpent    
        serpent.append((tete_x + direction[0], tete_y + direction[1])) 
        serpent2.append((tete_w + direction_2[0], tete_z + direction_2[1]))
    
    return True, 0


print(testmod())

# PROGRAMME PRINCIPAL
if __name__ == "__main__":
    cree_fenetre(225, 225)
    image(112, 112, image_debut, ancrage='center', tag='')
    clic = attend_clic_gauche()
    ferme_fenetre()
    
    
    while menu == True:
        #initialisation des modes de jeu
        arene_torique = False
        contre_2 = False

        #menu initialisation
        cree_fenetre(taille_case * largeur_plateau,
                         taille_case * hauteur_plateau)
        

        #bouton jouer
        rectangle(170, 100, 430, 150, couleur='white', remplissage='black', epaisseur=1)
        texte(260, 110, "Jouer", couleur='white')
        
        #bouton Mods
        rectangle(170, 200, 430, 250, couleur='white', remplissage='black', epaisseur=1)
        texte(260 , 210, "Mods ", couleur='white')
        
        #bouton quitter
        rectangle(170, 300, 430, 350, couleur='white', remplissage='black', epaisseur=1)
        texte(252 , 310, "Quitter", couleur='white')
        
        
        
        while True:
            clic = attend_clic_gauche()
            
            #si clique sur bouton jouer
            if clic[0] >= 170 and clic[1] >= 100 and clic[0] <= 430 and clic[1] <= 150:
                ferme_fenetre()
                break
            
            #si clique sur bouton menu
            elif clic[0] >= 170 and clic[1] >= 200 and clic[0] <= 430 and clic[1] <= 250:
                mod = True
                
                efface_tout()
                mise_a_jour()
                
                #Arène tonique
                rectangle(170, 100, 430, 150, couleur='white', remplissage='black', epaisseur=1)
                texte(200, 110, "Arène torique", couleur='white')
                
                #Jouer contre J2
                rectangle(170, 200, 430, 250, couleur='white', remplissage='black', epaisseur=1)
                texte(220 , 210, "Multijoueur ", couleur='white')

            
                while mod == True:
                    #Mode Menu
                    clic = attend_clic_gauche()
                    
                    #Mode Arène tonique PACMAN
                    if clic[0] >= 170 and clic[1] >= 100 and clic[0] <= 430 and clic[1] <= 150:
                        arene_torique = True
                        ferme_fenetre()
                        break
                    
                    #Mode VS J2
                    if clic[0] >= 170 and clic[1] >= 200 and clic[0] <= 430 and clic[1] <= 250:
                        contre_2 = True
                        ferme_fenetre()
                        break

                break 
                #fin du mod
            
            #si clique sur bouton quitter
            elif clic[0] >= 170 and clic[1] >= 300 and clic[0] <= 430 and clic[1] <= 350:
                menu = False
                ferme_fenetre()
                break

        #quitter le programme
        if menu == False:   
             break
            
        
         # initialisation du jeu
        framerate = 10    # taux de rafraîchissement du jeu en images/s
        direction = (0, 0)  # direction initiale du serpent
        direction_2 =(0,0)  #  direction initiale du serpent 2
        pommes = [] # liste des coordonnées des cases contenant des pommes
        obstacles = [] # liste des coordonnées des cases contenant des obstacles
        serpent = [(0, 0)] # liste des coordonnées de cases adjacentes décrivant le serpent
        serpent2 = [(39,0)]# liste des coordonnées de cases adjacentes décrivant le serpent 2
        perdant = 0 #numéro du serpent ayant perdu, variable utile quand on joue en multijoueur
        mouvement = '' # dernier mouvement effectué au clavier pour serpent 
        mouvement_2 = '' # dernier mouvement effectué au clavier pour serpent 2
        resultat = "GAME OVER"  #texte affiché à la fin de la partie
        
        cree_fenetre(taille_case * largeur_plateau,
                     taille_case * hauteur_plateau) 
    
        # boucle principale
        compte = 0
        jouer = True
        
        while jouer:
            # affichage des objets
            efface_tout()
            affiche_pommes(pommes) 
            affiche_obstacles(obstacles)
            affiche_serpent(serpent)  # à modifier ! fait
            texte(500, 10, f"Score: {len(serpent)-1}", taille=14) #affiche le score en haut à droite
            mise_a_jour()
            
            # gestion des événements
            ev = donne_ev()
            ty = type_ev(ev)
            
            #appel de fonctions_serpent
            gagner_jeu, perdant = fonctions_serpent(direction,direction_2 ,serpent, serpent2)
            
            if ty == 'Quitte':
                jouer = False
                
            elif ty == 'Touche' and contre_2 == False:
                print(touche(ev))
                information = change_direction(direction, touche(ev), mouvement)
                
                direction = information[0]
                mouvement = information[1]
                
            
            elif contre_2 == True and ty == 'Touche':
                
                print(touche(ev))
                information_2 = change_direction_2(direction_2, touche(ev), mouvement_2)
                    
                direction_2 = information_2[0]
                mouvement_2 = information_2[1]

                information = change_direction(direction, touche(ev), mouvement)
                
                direction = information[0]
                mouvement = information[1]
            
               
            if gagner_jeu == False: #Si perdu 
                break #sortir du jeu
            
            if compte == 10: #apparition d'un obstacle
                ajoute_obstacles()
                
            if compte == 20 : #apparition d'une pomme
                compte = 0 #reinitialise le compte
                ajoute_pommes()
                if len(serpent)-1 >= 5: #à partir d'un score de 5 la vitesse augmente à chaque fois que serpent mange pomme
                    framerate += 1/2
            
            if len(serpent)-1 == 30 and contre_2 == False: #quitte la partie quand le score de 30 est atteint
                resultat = "BRAVO"  
                break 
            
            # attente avant rafraîchissement
            compte += 1
            sleep(1/framerate)
    
        
        #affichage jeu terminé
        efface_tout()
        if contre_2 == False:
            texte(170, 200, resultat, taille=34)
            texte(210, 250, f"Score:{len(serpent)-1}", taille=34)
        
        else:
            if perdant == 0:
                texte(80, 140, f"Ex equo!", taille=34)
            
            elif perdant == 2:
                texte(80, 140, f"Bravo serpent vert!\nSerpent bleu a perdu", taille=34)
            else:
                texte(80, 140, f"Bravo serpent bleu!\nSerpent vert a perdu", taille=34)

        # fermeture et sortie
        attend_ev()
        ferme_fenetre()
        
