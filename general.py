import pygame
import dpieces
import pieces


class general() :
    def __init__(self):

        self.largeur_echiquier=560 #multiple de 8 
        
        self.echiquier=pygame.image.load(f'{pieces.path}\\echiquierabc2.png') #on charge l'echiquier ici pour n'avoir à le faire qu'une seule fois (opération plutôt lourde)
        self.echiquier=pygame.transform.scale(self.echiquier, (self.largeur_echiquier,self.largeur_echiquier)) #on redimensionne l'image

        self.tour_des_blancs=True
        
        self.main_surface=pygame.display.set_mode((1240,self.largeur_echiquier)) # 1240 -> largeur de la fenêtre
        pygame.display.set_caption('Echecs') #titre de la fenêtre

        self.main_surface.fill((255, 203, 96))
        self.ecrire("Bienvenue", (490,230), taille_ecriture=60)
        pygame.time.delay(1000)

        self.jouer = True #variable permet de savoir si l'utilisateur veut voir la partie entre deep blue et kasparov ou jouer

        self.main_surface.fill((255, 203, 96))
#page de démarrage
        running1=True
        while running1:
            self.ecrire("Que voulez-vous faire ?", (380,170), taille_ecriture=60)
            couleur_bouton1 = (100,100,100) 
            couleur_bouton2 = (210,200,80)
            mouse = pygame.mouse.get_pos() 

            if 300 <= mouse[0] <= 500 and 350 <= mouse[1] <= 410 : 
                pygame.draw.rect(self.main_surface,couleur_bouton1,[300,350,200,60]) 
                self.ecrire("observer", (339, 360), taille_ecriture=40)
                pygame.display.flip()
        
            else: 
                pygame.draw.rect(self.main_surface,couleur_bouton2,[300,350,200,60])
                self.ecrire("observer",(339, 360), taille_ecriture=40)
                pygame.display.flip() 
            
            if 700 <= mouse[0] <= 900 and 350 <= mouse[1] <= 410 : 
                pygame.draw.rect(self.main_surface,couleur_bouton1,[700,350,200,60]) 
                self.ecrire("jouer", (764, 360 ), taille_ecriture=40)
        
            else: 
                pygame.draw.rect(self.main_surface,couleur_bouton2,[700,350,200,60])
                self.ecrire("jouer", (764, 360 ), taille_ecriture=40)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running1=False
                    #Permet de garder la fenêtre ouverte jusqu'à ce que l'utilisateur veuille la fermer
                    #Par défaut l'evennement QUIT correspond à cliquer sur la croix
        
                if event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y postions of the mouse click 
                    x, y = mouse
                    if 300 <= x <= 500 and 350 <= y <= 410 : 
                        running1= False
                        self.pseudo_blanc= "DeepBlue"
                        self.pseudo_noir= "Kasparov"

                        self.jouer= False

                    if 700 <= x <= 900 and 350 <= y <= 410 : 
                        running1 = False
                        self.main_surface.fill((255, 203, 96))

                        self.pseudo_blanc = self.input("Joueur blanc, quel est ton nom ?")
                        self.ecrire(self.pseudo_blanc,(12,12))

                        self.main_surface.fill((255, 203, 96))

                        self.pseudo_noir = self.input("Joueur noir, quel est ton nom ?")
                        self.ecrire(self.pseudo_noir, (12,12))

                        running1=False

        self.setup_board()
        self.setup_pieces()
        self.__main__()
    
    def input(self, message):
        word=""
        self.ecrire(message,(24,12)) #
        pygame.display.flip()
        done = True
        while done:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key ==pygame.K_RETURN:
                        done=False
                    elif len(word)>0 and event.key ==pygame.K_BACKSPACE: #pour pouvoir effacer
                        word=word[:-1]
                        self.main_surface.fill((255, 203, 96))
                        self.ecrire(message,(24,12))
                        self.ecrire(word, (25,30))
                    else :
                        if len(word)<8:
                            try:
                                word+=str(chr(event.key))
                                self.ecrire(word, (25,30))
                            
                            except ValueError:
                                pass

        return word
    
    def setup_board(self):
        self.main_surface.fill((128, 208, 208))
        self.main_surface.blit(self.echiquier, (340,0))
        self.ecrire(f"BLANC : --- {self.pseudo_blanc} ---",(10,10), taille_ecriture=40)
        self.ecrire(f"NOIR : --- {self.pseudo_noir} ---",(self.largeur_echiquier+350,10), taille_ecriture=40)

        if self.tour_des_blancs:
            self.ecrire("C'est ton tour.", (10,60))
        else:
            self.ecrire("C'est ton tour.", (910,60))

        if dpieces.roiB.echec :
            self.ecrire("Echec", (10,130))
        if dpieces.roiN.echec :
            self.ecrire("Echec", (910, 130))
                
    def setup_pieces(self):

        for i in range(8):
            for j in range(8):

                if (i,j) in dpieces.Echiquier :

                    piece=dpieces.Echiquier[(i,j)]
                    image_piece=piece.image

                    self.main_surface.blit(image_piece, (i*70+343,560-j*70-70)) # +340 pour mettre les pièces sur l'échiquier

        pygame.display.flip() #met à jour l'écran

    def ecrire(self, message, position, taille_ecriture=25, taille=(20,100), ecriture="Playfair display"):
        # pick a font you have and set its size
        myfont = pygame.font.SysFont(ecriture, taille_ecriture)
        # apply it to text on a label
        label = myfont.render(message, 1, (0,0,0))
        # put the label object on the screen at point x=570, y=2
        self.main_surface.blit(label, position)

        pygame.display.flip() #met à jour l'écran

    
    def __main__(self):
        clock = pygame.time.Clock()
        running2 = True
        case=()
        memoire=[]
        fin_de_partie=False
        Game1=[(4,1),(4,3),
        (2,6),(2,4),
        (2,1),(2,2),
        (3,6),(3,4),
        (4,3),(3,4),
        (3,7),(3,4),
        (3,1),(3,3),
        (6,7),(5,5),
        (6,0),(5,2),
        (2,7),(6,3),
        (5,0),(4,1),
        (4,6),(4,5),
        (7,1),(7,2),
        (6,3),(7,4),
        (4,0),(6,0),
        (1,7),(2,5),
        (2,0),(4,2),
        (2,4),(3,3),
        (2,2),(3,3),
        (5,7),(1,3),
        (0,1),(0,2),
        (1,3),(0,4),
        (1,0),(2,2),
        (3,4),(3,5),
        (2,2),(1,4),
        (3,5),(4,6),
        (5,2),(4,4),
        (7,4),(4,1),
        (3,0),(4,1),
        (4,7),(6,7),
        (0,0),(2,0),
        (0,7),(2,7),
        (4,2),(6,4),
        (0,4),(1,5),
        (6,4),(5,5),
        (6,6),(5,5),
        (4,4),(2,3),
        (5,7),(3,7),
        (2,3),(1,5),
        (0,6),(1,5),
        (5,0),(3,0),
        (5,5),(5,4),
        (4,1),(4,2),
        (4,6),(5,5),
        (3,3),(3,4),
        (3,7),(3,4),
        (3,0),(3,4),
        (4,5),(3,4),
        (1,1),(1,2),
        (6,7),(7,7),
        (4,2),(1,5),
        (2,7),(6,7),
        (1,5),(2,4),
        (3,4),(3,3),
        (1,4),(3,5),
        (5,4),(5,3),
        (3,5),(1,6), 
        (2,5),(4,4),
        (2,4),(3,4),
        (5,3),(5,2),
        (6,1),(6,2),
        (4,4),(3,2),
        (2,0),(2,6),
        (6,7),(4,7),
        (1,6),(3,5),
        (4,7),(4,0),
        (6,0),(7,1),
        (3,2),(5,1),
        (3,5),(5,6), 
        (7,7),(6,6),
        (5,6),(6,4),
        (6,6),(7,5),
        (2,6),(7,6)]
        tour=0 #nombre de tour pour la partie de Kasparov


        while running2:
            #boutons abandonner
            couleur_bouton1 = (100,100,100) 
            couleur_bouton2 = (210,200,80)
            mouse = pygame.mouse.get_pos() 

            #boutons abandonner
            if 20 <= mouse[0] <= 120 and 450 <= mouse[1] <= 510 : 
                pygame.draw.rect(self.main_surface,couleur_bouton1,[20,450,100,60]) 
                self.ecrire("Abandonner", (32, 472), taille_ecriture=20)
                pygame.display.flip()
          
            else: 
                pygame.draw.rect(self.main_surface,couleur_bouton2,[20,450,100,60])
                self.ecrire("Abandonner",(32, 472), taille_ecriture=20)
                pygame.display.flip() 
            
            if self.largeur_echiquier+360 <= mouse[0] <= self.largeur_echiquier+460 and 450 <= mouse[1] <= 510 : 
                pygame.draw.rect(self.main_surface,couleur_bouton1,[self.largeur_echiquier+360,450,100,60]) 
                self.ecrire("Abandonner", (self.largeur_echiquier+371, 472), taille_ecriture=20)
          
            else: 
                pygame.draw.rect(self.main_surface,couleur_bouton2,[self.largeur_echiquier+360,450,100,60])
                self.ecrire("Abandonner", (self.largeur_echiquier+371, 472), taille_ecriture=20)

            #boutons la nulle
            if 140+40 <= mouse[0] <= 260+40 and 450 <= mouse[1] <= 510 : 
                pygame.draw.rect(self.main_surface,couleur_bouton1,[140+40,450,120,60]) 
                self.ecrire("Proposer la nulle", (152+34, 472), taille_ecriture=20)
                pygame.display.flip()
          
            else: 
                pygame.draw.rect(self.main_surface,couleur_bouton2,[140+40,450,120,60])
                self.ecrire("Proposer la nulle",(152+34, 472), taille_ecriture=20)
                pygame.display.flip() 
            
            if self.largeur_echiquier+480+40 <= mouse[0] <= self.largeur_echiquier+600+40 and 450 <= mouse[1] <= 510 : 
                pygame.draw.rect(self.main_surface,couleur_bouton1,[self.largeur_echiquier+480+40,450,120,60]) 
                self.ecrire("Proposer la nulle", (self.largeur_echiquier+490+34, 472), taille_ecriture=20)
          
            else: 
                pygame.draw.rect(self.main_surface,couleur_bouton2,[self.largeur_echiquier+480+40,450,120,60])
                self.ecrire("Proposer la nulle", (self.largeur_echiquier+490+34, 472), taille_ecriture=20)

            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running2 = False
                    #Permet de garder la fenêtre ouverte jusqu'à ce que l'utilisateur veuille la fermer
                    #Par défaut l'evennement QUIT correspond à cliquer sur la croix
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Set the x, y postions of the mouse click 
                    
                    x, y = mouse
#si on clique sur l'echiquier
                    if 340<=x<=self.largeur_echiquier+340 and y<=560: 
                        if self.jouer==False: #cas où on observe la partie entre Kasparov et Deep Blue
                            if tour>len(Game1)-1: #Il reste des coups à jouer
                                self.main_surface.fill((131, 166, 151))
                                self.ecrire("Ici, Kasparov a abandonné", (460,250), taille_ecriture=35)
                                pygame.time.delay(2000)
                                fin_de_partie= True
                            else:
                                case=Game1[tour+1]
                                memoire=Game1[tour:tour+2]
                                tour+=2
                        
                        else:
                            i=(x-340)//70 #correspnd à la colonne
                            j=(560-y)//70 #correspond à la ligne

                            if (i,j) == case:
                                case=()
                                memoire=[]

                            else :
                                case=(i,j)
                                memoire+=[case]

                            if len(memoire)==1:
                                if (i,j) in dpieces.Echiquier:
                                    if self.tour_des_blancs:
                                        if dpieces.Echiquier[case].couleur=="blanc": #on vérifie que la pièce est bien de la couleur de la personne qui doit jouer
                                            self.ecrire("Où veux-tu aller?",(10,90) )
                                        else:
                                            case=()
                                            memoire=[]
                                    else:
                                        if dpieces.Echiquier[case].couleur=="noir":
                                            self.ecrire("Où veux-tu aller?",(910,90) ) 
                                        else:
                                            case=()
                                            memoire=[]

                                else : #si le joueur a cliqué sur une case vide
                                    case=()
                                    memoire=[]


                        if len(memoire)==2:
                            position_depart=memoire[0][0],memoire[0][1]
                            position_arrivee=case[0],case[1]
                            piece_a_deplacer=dpieces.Echiquier[position_depart]
                            if position_depart in dpieces.Echiquier:
                                result=pieces.Piece.deplacement(piece_a_deplacer, position_arrivee)

                                if result=="Déplacement impossible": 
                                    if self.tour_des_blancs:
                                        self.ecrire("Déplacement impossible", (10,110))
                                        pygame.time.delay(1000)
                                    else :
                                        self.ecrire("Déplacement impossible", (910, 110))
                                        pygame.time.delay(1000)
                                
                                else :
                                    if self.tour_des_blancs:
                                        self.tour_des_blancs=False
                                    else :
                                        self.tour_des_blancs=True
                                    
                                    #promotion
                                    if piece_a_deplacer.nom[:-1]=="pion": # ici on regarde si un pion a atteint la dernière ligne de l'échiquier d'un côté ou de l'autre
                                        if piece_a_deplacer.couleur=="blanc" and piece_a_deplacer.y==7:
                                            
                                            couleur_bouton1 = (100,100,100) 
                                            couleur_bouton2 = (210,200,80)
                                            en_attente_de_decision=True
                                            while en_attente_de_decision:
                                                self.ecrire("Votre pion se transforme en?", (10, 130))

                                                mouse = pygame.mouse.get_pos()

                                                #différentes options de promotion
                                                if 10 <= mouse[0] <= 80 and 250 <= mouse[1] <= 310 : 
                                                    pygame.draw.rect(self.main_surface,couleur_bouton1,[10,250,70,60]) 
                                                    self.ecrire("Dame", (22, 272), taille_ecriture=20)
                                                    pygame.display.flip()
                
                                                else: 
                                                    pygame.draw.rect(self.main_surface,couleur_bouton2,[10,250,70,60])
                                                    self.ecrire("Dame",(22, 272), taille_ecriture=20)
                                                    pygame.display.flip() 
                
                                                if 90 <= mouse[0] <= 160 and 250 <= mouse[1] <= 310 : 
                                                    pygame.draw.rect(self.main_surface,couleur_bouton1,[90,250,70,60]) 
                                                    self.ecrire("fou", (102, 272), taille_ecriture=20)
                
                                                else: 
                                                    pygame.draw.rect(self.main_surface,couleur_bouton2,[90,250,70,60])
                                                    self.ecrire("fou", (102, 272), taille_ecriture=20)
                                                
                                                if 170 <= mouse[0] <= 240 and 250 <= mouse[1] <= 310 : 
                                                    pygame.draw.rect(self.main_surface,couleur_bouton1,[170,250,70,60]) 
                                                    self.ecrire("tour", (182, 272), taille_ecriture=20)
                                                    pygame.display.flip()
                
                                                else: 
                                                    pygame.draw.rect(self.main_surface,couleur_bouton2,[170,250,70,60])
                                                    self.ecrire("tour",(182, 272), taille_ecriture=20)
                                                    pygame.display.flip() 
                
                                                if 250 <= mouse[0] <= 320 and 250 <= mouse[1] <= 310 : 
                                                    pygame.draw.rect(self.main_surface,couleur_bouton1,[250,250,100,60]) 
                                                    self.ecrire("cavalier", (262, 272), taille_ecriture=20)
                
                                                else: 
                                                    pygame.draw.rect(self.main_surface,couleur_bouton2,[250,250,100,60])
                                                    self.ecrire("cavalier", (262, 272), taille_ecriture=20)

                                                for event in pygame.event.get():
                                                    if event.type == pygame.QUIT:
                                                        en_attente_de_decision = False
                                                        running2=False
                                                        #Permet de garder la fenêtre ouverte jusqu'à ce que l'utilisateur veuille la fermer
                                                        #Par défaut l'evennement QUIT correspond à cliquer sur la croix
                    
                                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                                        # Set the x, y postions of the mouse click 
                                                        mouse=pygame.mouse.get_pos()

                                                        if 10 <= mouse[0] <= 80 and 250 <= mouse[1] <= 310: #le joueur choisit une dame
                                                            dpieces.Echiquier[position_arrivee]=pieces.dame('blanc', position_arrivee[0],position_arrivee[1], 'dameB')
                                                            piece_a_deplacer=dpieces.Echiquier[position_arrivee]
                                                            en_attente_de_decision=False

                                                        if 90 <= mouse[0] <= 160 and 250 <= mouse[1] <= 310: #le joueur choisit un fou
                                                            dpieces.Echiquier[position_arrivee]=pieces.fou('blanc', position_arrivee[0],position_arrivee[1], 'fouB')
                                                            piece_a_deplacer=dpieces.Echiquier[position_arrivee]
                                                            en_attente_de_decision=False

                                                        if 170 <= mouse[0] <= 240 and 250 <= mouse[1] <= 310: #le joueur choisit une tour 
                                                            dpieces.Echiquier[position_arrivee]=pieces.tour('blanc', position_arrivee[0],position_arrivee[1], 'tourB')
                                                            piece_a_deplacer=dpieces.Echiquier[position_arrivee]
                                                            en_attente_de_decision=False

                                                        if 250 <= mouse[0] <= 320 and 250 <= mouse[1] <= 310: #le joueur choisit un cavalier
                                                            dpieces.Echiquier[position_arrivee]=pieces.cavalier('blanc', position_arrivee[0],position_arrivee[1], 'cavalierB')
                                                            piece_a_deplacer=dpieces.Echiquier[position_arrivee]
                                                            en_attente_de_decision=False
                                                        
                                                


                                        else:
                                            if position_arrivee[1]==0:
                                                self.ecrire("Votre pion se transforme en ?", (340+self.largeur_echiquier +10, 130))
                                                couleur_bouton1 = (100,100,100) 
                                                couleur_bouton2 = (210,200,80)
                                                
                                                en_attente_de_decision=True

                                                while en_attente_de_decision:

                                                    mouse = pygame.mouse.get_pos() 

                                                    #différentes options de promotion
                                                    if 340+self.largeur_echiquier + 10 <= mouse[0] <= 340+self.largeur_echiquier + 80 and 250 <= mouse[1] <= 310 : 
                                                        pygame.draw.rect(self.main_surface,couleur_bouton1,[340+self.largeur_echiquier +10,250,70,60]) 
                                                        self.ecrire("Dame", (340+self.largeur_echiquier + 22, 272), taille_ecriture=20)
                                                        pygame.display.flip()
                
                                                    else: 
                                                        pygame.draw.rect(self.main_surface,couleur_bouton2,[340+self.largeur_echiquier +10,250,70,60])
                                                        self.ecrire("Dame",(340+self.largeur_echiquier +22, 272), taille_ecriture=20)
                                                        pygame.display.flip() 
                    
                                                    if 340+self.largeur_echiquier +90 <= mouse[0] <= 340+self.largeur_echiquier +160 and 250 <= mouse[1] <= 310 : 
                                                        pygame.draw.rect(self.main_surface,couleur_bouton1,[340+self.largeur_echiquier +90,250,70,60]) 
                                                        self.ecrire("fou", (340+self.largeur_echiquier +102, 272), taille_ecriture=20)
                
                                                    else: 
                                                        pygame.draw.rect(self.main_surface,couleur_bouton2,[340+self.largeur_echiquier +90,250,70,60])
                                                        self.ecrire("fou", (340+self.largeur_echiquier +102, 272), taille_ecriture=20)
                                                    
                                                    if 340+self.largeur_echiquier +170 <= mouse[0] <= 340+self.largeur_echiquier +240 and 250 <= mouse[1] <= 310 : 
                                                        pygame.draw.rect(self.main_surface,couleur_bouton1,[340+self.largeur_echiquier +170,250,70,60]) 
                                                        self.ecrire("tour", (340+self.largeur_echiquier +182, 272), taille_ecriture=20)
                                                        pygame.display.flip()
                
                                                    else: 
                                                        pygame.draw.rect(self.main_surface,couleur_bouton2,[340+self.largeur_echiquier +170,250,70,60])
                                                        self.ecrire("tour",(340+self.largeur_echiquier +182, 272), taille_ecriture=20)
                                                        pygame.display.flip() 
                    
                                                    if 340+self.largeur_echiquier +250 <= mouse[0] <= 340+self.largeur_echiquier +310 and 250 <= mouse[1] <= 310 : 
                                                        pygame.draw.rect(self.main_surface,couleur_bouton1,[340+self.largeur_echiquier +250,250,90,60]) 
                                                        self.ecrire("cavalier", (340+self.largeur_echiquier +262, 272), taille_ecriture=20)
                
                                                    else: 
                                                        pygame.draw.rect(self.main_surface,couleur_bouton2,[340+self.largeur_echiquier +250,250,90,60])
                                                        self.ecrire("cavalier", (340+self.largeur_echiquier +262, 272), taille_ecriture=20)

                                                    for event in pygame.event.get():

                                                        if event.type == pygame.QUIT:
                                                            en_attente_de_decision = False
                                                            running2=False
                                                            #l'utilisateur peut encore fermer la fenêtre sans problème
                        
                                                        if event.type == pygame.MOUSEBUTTONDOWN:
                                                            # Set the x, y postions of the mouse click 
                                                            mouse=pygame.mouse.get_pos()

                                                            if 340+self.largeur_echiquier +10 <= mouse[0] <= 340+self.largeur_echiquier +80 and 250 <= mouse[1] <= 310: #le joueur choisit une dame
                                                                dpieces.Echiquier[position_arrivee]=pieces.dame('noir', position_arrivee[0],position_arrivee[1], 'dameN')
                                                                piece_a_deplacer=dpieces.Echiquier[position_arrivee]
                                                                en_attente_de_decision=False

                                                            if 340+self.largeur_echiquier +90 <= mouse[0] <= 340+self.largeur_echiquier +160 and 250 <= mouse[1] <= 310: #le joueur choisit un fou
                                                                dpieces.Echiquier[position_arrivee]=pieces.fou('noir', position_arrivee[0],position_arrivee[1], 'fouN')
                                                                piece_a_deplacer=dpieces.Echiquier[position_arrivee]
                                                                en_attente_de_decision=False

                                                            if 340+self.largeur_echiquier +170 <= mouse[0] <= 340+self.largeur_echiquier +240 and 250 <= mouse[1] <= 310: #le joueur choisit une tour 
                                                                dpieces.Echiquier[position_arrivee]=pieces.tour('noir', position_arrivee[0],position_arrivee[1], 'tourN')
                                                                piece_a_deplacer=dpieces.Echiquier[position_arrivee]
                                                                en_attente_de_decision=False

                                                            if 340+self.largeur_echiquier +250 <= mouse[0] <= 340+self.largeur_echiquier +310 and 250 <= mouse[1] <= 310: #le joueur choisit un cavalier
                                                                dpieces.Echiquier[position_arrivee]=pieces.cavalier('noir', position_arrivee[0],position_arrivee[1], 'cavalierN')
                                                                piece_a_deplacer=dpieces.Echiquier[position_arrivee]
                                                                en_attente_de_decision=False
                                                              
                                    resultat = piece_a_deplacer.echec_et_mat() #on appelle echec_et_mat sur la piece qui vient de bouger
                                                                            
                                    if resultat == "mat": #on est dans un cas d'échec et mat, c'est la fin de la partie
                                        self.main_surface.fill((131, 166, 151))
                                        self.ecrire(f"Echec et mat, Les {piece_a_deplacer.couleur}s ont gagné !", (440,250), taille_ecriture=35)
                                        pygame.time.delay(2000)
                                        fin_de_partie=True
                                    
                                    elif resultat == False: #dans le cas où on est pas en échec
                                        if piece_a_deplacer.pat(): #on regarde si on est en pat
                                            self.main_surface.fill((131, 166, 151))
                                            self.ecrire("Pat", (460,250), taille_ecriture=35)
                                            pygame.time.delay(2000)
                                            fin_de_partie=True

                                case=()
                                memoire=[]
                                self.setup_board()
                                self.setup_pieces()
                            
                            pygame.display.flip()

    #déclarer forfait de l'un ou de l'autre des joueurs
                    elif 20 <= mouse[0] <= 120 and 450 <= mouse[1] <= 510:

                        self.ecrire(f"{self.pseudo_blanc} a déclaré forfait.", (910, 200))
                        pygame.time.delay(2000) #pause for a given number of milliseconds based on the CPU clock 

                        self.main_surface.fill((131, 166, 151))
                        self.ecrire(f"{self.pseudo_noir} a gagné !", (470,250), taille_ecriture=35)
                        pygame.time.delay(2000)

                        fin_de_partie=True

                    
                    elif self.largeur_echiquier+360 <= mouse[0] <= self.largeur_echiquier+460 and 450 <= mouse[1] <= 510:

                        self.ecrire(f"{self.pseudo_noir} a déclaré forfait.", (10, 200))
                        pygame.time.delay(2000)

                        self.main_surface.fill((131, 166, 151))
                        self.ecrire(f"{self.pseudo_blanc} a gagné !", (470,250), taille_ecriture=35)
                        pygame.time.delay(2000) 
                        fin_de_partie=True
                                                    
                    pygame.display.flip() 

    #proposer la nulle en cliquant sur l'un des boutons proposer la nulle
                    if 140+40 <= mouse[0] <= 260+40 and 450 <= mouse[1] <= 510 : #ie les blancs demandent match nul
                        self.ecrire(f"{self.pseudo_blanc} propose la nulle.", (910, 300))
                        self.ecrire("Acceptes-tu?", (910, 330))
                        pause=True

                        while pause :
                            mouse=pygame.mouse.get_pos()

                            if self.largeur_echiquier+360 <= mouse[0] <= self.largeur_echiquier+460 and 450 <= mouse[1] <= 510 : #bouton change de couleur quand la souris passe dessus
                                pygame.draw.rect(self.main_surface,couleur_bouton1,[self.largeur_echiquier+360,450,100,60]) 
                                self.ecrire("Oui", (self.largeur_echiquier+371, 472), taille_ecriture=20)
            
                            else: 
                                pygame.draw.rect(self.main_surface,couleur_bouton2,[self.largeur_echiquier+360,450,100,60])
                                self.ecrire("Oui", (self.largeur_echiquier+371, 472), taille_ecriture=20)

                            if self.largeur_echiquier+480+40 <= mouse[0] <= self.largeur_echiquier+600+40 and 450 <= mouse[1] <= 510 : 
                                pygame.draw.rect(self.main_surface,couleur_bouton1,[self.largeur_echiquier+480+40,450,120,60]) 
                                self.ecrire("Non", (self.largeur_echiquier+490+40, 472), taille_ecriture=20)

                            else: 
                                pygame.draw.rect(self.main_surface,couleur_bouton2,[self.largeur_echiquier+480+40,450,120,60])
                                self.ecrire("Non", (self.largeur_echiquier+490+40, 472), taille_ecriture=20)

                            
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pause = False
                                    running2=False
                                    #permet à l'utilisateur de fermer la fenêtre à tout moment
                
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    # Set the x, y postions of the mouse click 
                                    x, y = mouse

                                    if self.largeur_echiquier+360+40 <= x <= self.largeur_echiquier+460+40 and 450 <= y <= 510 :
                                        pause=False
                                        self.main_surface.fill((131, 166, 151))
                                        self.ecrire("Partie nulle", (510,250), taille_ecriture=50)
                                        pygame.time.delay(2000) 
                                        fin_de_partie=True
                                    
                                    elif self.largeur_echiquier+480+40 <= x <= self.largeur_echiquier+600+40 and 450 <= y <= 510 :
                                        pause=False
                                        self.setup_board() 
                                        self.setup_pieces() 
                        continue       
                    
                    if self.largeur_echiquier+480+40 <= mouse[0] <= self.largeur_echiquier+600+40 and 450 <= mouse[1] <= 510 : #ie les noirs demandent match nul
                        
                        self.ecrire(f"{self.pseudo_noir} propose la nulle.", (10, 300))
                        self.ecrire("Acceptes-tu?", (10, 330))
                        pause1=True

                        while pause1 :
                            mouse = pygame.mouse.get_pos() 

                            if 20 <= mouse[0] <= 120 and 450 <= mouse[1] <= 510 : #bouton change de couleur quand la souris passe dessus
                                pygame.draw.rect(self.main_surface,couleur_bouton1,[20,450,100,60]) 
                                self.ecrire("Oui", (31, 472), taille_ecriture=20)
            
                            else: 
                                pygame.draw.rect(self.main_surface,couleur_bouton2,[20,450,100,60])
                                self.ecrire("Oui", (31, 472), taille_ecriture=20)

                            if 140+40 <= mouse[0] <= 260+40 and 450 <= mouse[1] <= 510 : 
                                pygame.draw.rect(self.main_surface,couleur_bouton1,[140+40,450,120,60]) 
                                self.ecrire("Non", (150+40, 472), taille_ecriture=20)

                            else: 
                                pygame.draw.rect(self.main_surface,couleur_bouton2,[140+40,450,120,60])
                                self.ecrire("Non", (150+40, 472), taille_ecriture=20)

                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pause1 = False
                                    running2=False
                                    #permet à l'utilisateur de fermer la fenêtre à tout moment
                
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    # Set the x, y postions of the mouse click 
                                    x, y = mouse

                                    if 20 <= x <= 120 and 450 <= y <= 510 :
                                        pause1=False
                                        self.main_surface.fill((131, 166, 151))
                                        self.ecrire("Partie nulle", (510,250), taille_ecriture=50)
                                        pygame.time.delay(2000) 
                                        fin_de_partie=True
                                    
                                    elif 140+40 <= x <= 260+40 and 450 <= y <= 510:
                                        pause1=False
                                        self.setup_board() 
                                        self.setup_pieces()                                      

#la partie qui suit code la fin de partie, laissant aux joueurs le choix de rejouer ou de quitter                
                if fin_de_partie==True:

                    running3=True
                    self.main_surface.fill((131, 166, 151))

                    while running3:
                        self.ecrire("Voulez-vous rejouer ?", (380,150), taille_ecriture=60)
                        couleur_bouton1 = (100,100,100) 
                        couleur_bouton2 = (210,200,80)
                        mouse = pygame.mouse.get_pos() 

                        if 300 <= mouse[0] <= 500 and 350 <= mouse[1] <= 410 : 
                            pygame.draw.rect(self.main_surface,couleur_bouton1,[300,350,200,60]) 
                            self.ecrire("Pour sûr", (310, 360), taille_ecriture=40)
                            pygame.display.flip()
                    
                        else: 
                            pygame.draw.rect(self.main_surface,couleur_bouton2,[300,350,200,60])
                            self.ecrire("Pour sûr",(310, 360), taille_ecriture=40)
                            pygame.display.flip() 
                        
                        if 700 <= mouse[0] <= 900 and 350 <= mouse[1] <= 410 : 
                            pygame.draw.rect(self.main_surface,couleur_bouton1,[700,350,200,60]) 
                            self.ecrire("Une autre fois", (710, 360 ), taille_ecriture=40)
                    
                        else: 
                            pygame.draw.rect(self.main_surface,couleur_bouton2,[700,350,200,60])
                            self.ecrire("Une autre fois", (710, 360 ), taille_ecriture=40)
                        
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                running2=False
                                running3 = False
                                #Permet de garder la fenêtre ouverte jusqu'à ce que l'utilisateur veuille la fermer
                                #Par défaut l'evennement QUIT correspond à cliquer sur la croix
                    
                            if event.type == pygame.MOUSEBUTTONDOWN:
                            # Set the x, y postions of the mouse click 
                                x, y = mouse
                                if 300 <= x <= 500 and 350 <= y <= 410 : 
                                    running3=False
                                    tour=0
                                    #on réinitialise le dictionnaire
                                    dpieces.pionB1= pieces.pion( "blanc", 0, 1, 'pionB')
                                    dpieces.pionB2= pieces.pion( "blanc", 1, 1, 'pionB')
                                    dpieces.pionB3= pieces.pion( "blanc", 2, 1, 'pionB')
                                    dpieces.pionB4= pieces.pion( "blanc", 3, 1, 'pionB')
                                    dpieces.pionB5= pieces.pion( "blanc", 4, 1, 'pionB')
                                    dpieces.pionB6= pieces.pion( "blanc", 5, 1, 'pionB')
                                    dpieces.pionB7= pieces.pion( "blanc", 6, 1, 'pionB')
                                    dpieces.pionB8= pieces.pion( "blanc", 7, 1, 'pionB')

                                    dpieces.pionN1 = pieces.pion( "noir", 0, 6, 'pionN')
                                    dpieces.pionN2 = pieces.pion( "noir", 1, 6, 'pionN')
                                    dpieces.pionN3 = pieces.pion( "noir", 2, 6, 'pionN')
                                    dpieces.pionN4 = pieces.pion( "noir", 3, 6, 'pionN')
                                    dpieces.pionN5 = pieces.pion( "noir", 4, 6, 'pionN')
                                    dpieces.pionN6 = pieces.pion( "noir", 5, 6, 'pionN')
                                    dpieces.pionN7 = pieces.pion( "noir", 6, 6, 'pionN')
                                    dpieces.pionN8 = pieces.pion( "noir", 7, 6, 'pionN')

                                    #crée les autres pièces blanches et noires
                                    dpieces.tourB1 = pieces.tour('blanc', 0, 0, 'tourB')
                                    dpieces.tourB2 = pieces.tour('blanc', 7, 0, 'tourB')
                                    dpieces.cavalierB1 = pieces.cavalier('blanc', 1, 0, 'cavalierB')
                                    dpieces.cavalierB2 = pieces.cavalier('blanc', 6, 0, 'cavalierB')
                                    dpieces.fouB1 = pieces.fou('blanc', 2, 0, 'fouB')
                                    dpieces.fouB2 = pieces.fou('blanc', 5, 0,'fouB')
                                    dpieces.dameB = pieces.dame('blanc', 3, 0, 'dameB') 
                                    dpieces.roiB = pieces.roi('blanc', 4, 0, 'roiB')

                                    dpieces.tourN1 = pieces.tour('noir', 0, 7, 'tourN')
                                    dpieces.tourN2 = pieces.tour('noir', 7, 7, 'tourN')
                                    dpieces.cavalierN1 = pieces.cavalier('noir', 1, 7, 'cavalierN')
                                    dpieces.cavalierN2 = pieces.cavalier('noir', 6, 7, 'cavalierN')
                                    dpieces.fouN1 = pieces.fou('noir', 2, 7, 'fouN')
                                    dpieces.fouN2 = pieces.fou('noir', 5, 7, 'fouN')
                                    dpieces.dameN = pieces.dame('noir', 3, 7, 'dameN') 
                                    dpieces.roiN = pieces.roi('noir', 4, 7, 'roiN')

                                    dpieces.Echiquier={
                                        (0,0) : dpieces.tourB1, (7,0) : dpieces.tourB2, (1,0) : dpieces.cavalierB1, (6,0) : dpieces.cavalierB2, (2,0) : dpieces.fouB1, (5,0) : dpieces.fouB2, (3,0) : dpieces.dameB, (4,0) : dpieces.roiB, 
                                        (0,1) : dpieces.pionB1, (1,1): dpieces.pionB2, (2,1) : dpieces.pionB3, (3,1) : dpieces.pionB4, (4,1) : dpieces.pionB5, (5,1): dpieces.pionB6, (6,1): dpieces.pionB7, (7,1) : dpieces.pionB8,
                                        (0,7) : dpieces.tourN1, (7,7) : dpieces.tourN2, (1,7) : dpieces.cavalierN1, (6,7) : dpieces.cavalierN2, (2,7) : dpieces.fouN1, (5,7) : dpieces.fouN2, (3,7) : dpieces.dameN, (4,7) : dpieces.roiN,
                                        (0,6) : dpieces.pionN1, (1,6): dpieces.pionN2, (2,6) : dpieces.pionN3, (3,6) : dpieces.pionN4, (4,6) : dpieces.pionN5, (5,6): dpieces.pionN6, (6,6): dpieces.pionN7, (7,6) : dpieces.pionN8}
                                    self.__init__()

                                if 700 <= x <= 900 and 350 <= y <= 410 : 
                                    running2=False
                                    running3 = False

        clock.tick(150)
        #détermine le nombre de fois que cette boucle est exécutée par seconde
        pygame.quit()
        


b=general()
