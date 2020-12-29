import pygame
import dictionnaire_pieces
path_milo = "C:\\Users\\emili\\OneDrive\\Documents\\CPES-2\\informatique\\chess"
path_esther="C:\\Users\\esthe\\OneDrive\\Bureau\\CPES-L2\\Info\\projet"

class Piece:
  def __init__(self, couleur, positionix, positioniy, nom):
    pygame.init()
    self.couleur = couleur
    self.x = positionix
    self.y = positioniy
    #nom est le type de pièce
    self.nom = nom #nom est le type de pièce
    self.image = pygame.image.load(f"{path_esther}\\{nom}.png")
    
  def deplacement(self, position): #change la position de la pièce et supprime la pièce mangée du dictionnaire 
    x = position[0]  #mettre le lien entre le déplacement sur le plateau et les coordonnées 
    y = position [1]
    #vérifier que le déplacement est possible pour la pièce
    if 'roi' in self.nom:
      if self.roque(x,y) == True:
        if self.couleur == 'blanc': #test pour savoir quel type de roque
          if (x,y) == (self.x+2, self.y): 
            ancienxytour = (7,0)
            nouveauxytour = (5,0)
          else :
            ancienxytour = (0,0)
            nouveauxytour = (3,0)
        if self.couleur == 'noir':
          if (x,y) == (self.x+2, self.y):
            ancienxytour = (7,7)
            nouveauxytour = (5,7)   
          else :
            ancienxytour = (0,7)
            nouveauxytour = (3,7)
        #bouger le roi
        ancienxyroi = (self.x,self.y)
        self.x = x #changer les coordonnées de la pièce
        self.joué = True
        dictionnaire_pieces.Echiquier[(x,y)] = self #on bouge la pièce en la rajoutant dans le dictionnaire avec comme clé sa nouvelle position
        dictionnaire_pieces.Echiquier.pop(ancienxyroi) #on supprime l'ancienne pièce
        #bouger la tour
        dictionnaire_pieces.Echiquier[ancienxytour].joué = True
        dictionnaire_pieces.Echiquier[ancienxytour].x = nouveauxytour[0]
        dictionnaire_pieces.Echiquier[nouveauxytour] = dictionnaire_pieces.Echiquier[ancienxytour]
        dictionnaire_pieces.Echiquier.pop(ancienxytour)
        return None #le déplacement est fini, le roque a été fait
    #on vérifie que le déplacement est possible
    if self.dpossible(x,y): 
      if (x,y) in dictionnaire_pieces.Echiquier: #prendre une pièce
        if self.couleur != dictionnaire_pieces.Echiquier[(x,y)].couleur:  #vérifie que la pièce qui va être prise est bien de la couleur adverse
          if 'roi' in dictionnaire_pieces.Echiquier[(x,y)].nom: #on ne peut pas manger le roi
            return 'Déplacement impossible' 
          else : 
            dictionnaire_pieces.Echiquier.pop((x,y))  #pièce prise = supprimée de l'échiquier
        else : return 'Déplacement impossible' #on ne peut pas manger un de ses propres pions
      else : #cas de la prise en passant
        if 'pion' in self.nom:
          if self.pepg == True:
            dictionnaire_pieces.Echiquier.pop((self.x-1,self.y)) #prend la pièce en passant à gauche
            self.pepg = False
          if self.pepd == True:
            dictionnaire_pieces.Echiquier.pop((self.x+1,self.y)) #prend la pièce en passant à droite
            self.pepd = False
      #bouger la pièce 
      ancienxy = (self.x,self.y)
      self.x = x #changer les coordonnées de la pièce
      self.y = y
      if (('roi' in self.nom) or ('pion' in self.nom) or ('tour' in self.nom)):
        self.joué = True
      dictionnaire_pieces.Echiquier[(x,y)] = self #on bouge la pièce en la rajoutant dans le dictionnaire avec comme clé sa nouvelle position
      dictionnaire_pieces.Echiquier.pop(ancienxy) #on supprime l'ancienne clé (position) de la pièce                                     
      #changer eppossible False sauf le self
      if self.couleur == 'blanc' : yep = 3 #yep = y du prise en passant pour les blancs
      else : yep = 4
      for i in range(0,8):
        if (i, yep) in dictionnaire_pieces.Echiquier and (i, yep) != (x,y):
          dictionnaire_pieces.Echiquier[(i,yep)].eppossible = False
    else : return 'Déplacement impossible' #à changer?
    
  def dpossible(self,x,y):
    #vérifie que le déplacement est un bon déplacement pour le type de pièce
    # à rajouter vérification de pas mise en échec de son propre roi (fait avec cloué)
    # vérifie qu'on ne saute pas au dessus de pièce
    return True or False
  
  def dlegal(self, x,y):
    #deplacement autorisé pour ce type de pièce
    return True or False
    
  def cloue(self):
    if self.couleur=="blanc":   #couleur de la pièce sur laquelle on applique
      if self.x==roiB.x or self.y==roiB.y:   #déplacement en colonnes et lignes
        if self.x<roiB.x:
          xn=self.x-1
          while not (xn,self.y) in dictionnaire_pieces.Echiquier:   #parcours entre pièce à clouer et suivante
            xn-=1
          if dictionnaire_pieces.Echiquier[(xn,self.y)].couleur=="noir" and dictionnaire_pieces.Echiquier[(xn,self.y)].dlegal(roiB.x,roiB.y):
            return True
        if self.x>roiB.x:
          xn=self.x+1
          while not (xn,self.y) in dictionnaire_pieces.Echiquier:
            xn+=1
          if dictionnaire_pieces.Echiquier[(xn,self.y)].couleur=="noir" and dictionnaire_pieces.Echiquier[(xn,self.y)].dlegal(roiB.x,roiB.y):
            return True
        if self.y<roiB.y:
          yn=self.y-1
          while not (self.x,yn) in dictionnaire_pieces.Echiquier:
            yn-=1
          if dictionnaire_pieces.Echiquier[(self.x,yn)].couleur=="noir" and dictionnaire_pieces.Echiquier[(self.x,yn)].dlegal(roiB.x,roiB.y):
            return True
        if self.y>roiB.y:
          yn=self.y+1
          while not (self.x,yn) in dictionnaire_pieces.Echiquier:
            yn+=1
          if dictionnaire_pieces.Echiquier[(self.x,yn)].couleur=="noir" and dictionnaire_pieces.Echiquier[(self.x,yn)].dlegal(roiB.x,roiB.y):
            return True
      if abs(self.x-roiB.x)==abs(self.y-roiB.y):    #déplacement en diagonales
        pasx = pasy = 1
        if self.x<roiB.x: pasx =-1
        if self.y<roiB.y: pasy =-1
        xn = self.x + pasx
        yn = self.y + pasy
        while not (xn,yn) in dictionnaire_pieces.Echiquier:   #parcours entre pièce à clouer et suivante
          xn+=pasx
          yn+=paxy
        if dictionnaire_pieces.Echiquier[(xn,yn)].couleur=="noir" and dictionnaire_pieces.Echiquier[(xn,yn)].dlegal(roiB.x,roiB.y):
          return True   #ds dpossible : si cloué=True => dpossible=False
      return False
    if self.couleur=="noir":   #couleur de la pièce sur laquelle on applique
      if self.x==roiN.x or self.y==roiN.y:   #déplacement en colonnes et lignes
        if self.x<roiN.x:
          xn=self.x-1
          while not (xn,self.y) in dictionnaire_pieces.Echiquier:   #parcours entre pièce à clouer et suivante
            xn-=1
          if dictionnaire_pieces.Echiquier[(xn, self.y)].couleur=="blanc" and dictionnaire_pieces.Echiquier[(xn,self.y)].dlegal(roiN.x,roiN.y):
            return True
        if self.x>roiN.x:
          xn=self.x+1
          while not (xn,self.y) in dictionnaire_pieces.Echiquier:
            xn+=1
          if dictionnaire_pieces.Echiquier[(xn,self.y)].couleur=="blanc" and dictionnaire_pieces.Echiquier[(xn,self.y)].dlegal(roiN.x,roiN.y):
            return True
        if self.y<roiN.y:
          yn=self.y-1
          while not (self.x,yn) in dictionnaire_pieces.Echiquier:
            yn-=1
          if dictionnaire_pieces.Echiquier[(self.x,yn)].couleur=="blanc" and dictionnaire_pieces.Echiquier[(self.x,yn)].dlegal(roiN.x,roiN.y):
            return True
        if self.y>roiN.y:
          yn=self.y+1
          while not (self.x,yn) in dictionnaire_pieces.Echiquier:
            yn+=1
          if dictionnaire_pieces.Echiquier[(self.x,yn)].couleur=="blanc" and dictionnaire_pieces.Echiquier[(self.x,yn)].dlegal(roiN.x,roiN.y):
            return True
      if abs(self.x-roiN.x)==abs(self.y-roiN.y):    #déplacement en diagonales
        pasx = pasy = 1
        if self.x<roiN.x: pasx =-1
        if self.y<roiN.y: pasy =-1
        xn = self.x + pasx
        yn = self.y + pasy
        while not (xn,yn) in dictionnaire_pieces.Echiquier:   #parcours entre pièce à clouer et suivante
          xn+=pasx
          yn+=paxy
        if dictionnaire_pieces.Echiquier[(xn,yn)].couleur=="blanc" and dictionnaire_pieces.Echiquier[(xn,yn)].dlegal(roiN.x,roiN.y):
          return True   #ds dpossible : si cloué=True => dpossible=False
      return False

  def echectest(self): #a appeler pour vérifier si echec sur roi de la même couleur sans changer propriété ni vérifier mat #renvoie True
    echec=False
    for i in dictionnaire_pieces.Echiquier:
      if self.couleur=="blanc" and dictionnaire_pieces.Echiquier[i].couleur=="blanc":
        if dictionnaire_pieces.Echiquier[i].dlegal(roiN.x,roiN.y):   #vérifie si la pièce adverse atteint le roi
          echec=True
          return echec
      if self.couleur=="noir" and dictionnaire_pieces.Echiquier[i].couleur=="noir":
        if dictionnaire_pieces.Echiquier[i].dlegal(roiB.x,roiB.y):
          echec=True
          return echec
    return echec

    
  def echec_et_mat(self): #à appeler sur une pièce qqconque (qui vient d'être déplacée) #renvoie True ou 'mat'
    echec=False
    L=[] #garde la position des pièces qui mettent en échec (utile pour mat)
    for i in dictionnaire_pieces.Echiquier:
      if self.couleur=="blanc" and dictionnaire_pieces.Echiquier[i].couleur=="blanc":
        if dictionnaire_pieces.Echiquier[i].dlegal(roiN.x,roiN.y):   #vérifie si la pièce adverse atteint le roi
          echec=True
          roiB.echec = True
          L+=[i]
      if self.couleur=="noir" and dictionnaire_pieces.Echiquier[i].couleur=="noir":
        if dictionnaire_pieces.Echiquier[i].dlegal(roiB.x,roiB.y):
          echec=True
          roiN.echec = True
          L+=[i]
    if echec:
      if self.mat():
        return 'mat'
      else : return echec
  
  def mat(self, L):    #appel sur la même pièce que echec  #vérifier si le roi est en échec : on peut mettre la condition ailleurs
    mat=True          #part du principe que c'est vrai : plus facile à manipuler
    if len(L)>1 or "cavalier" in dictionnaire_pieces.Echiquier[L[0]].nom:  #seul le roi peut se sauver
      if dictionnaire_pieces.Echiquier[L[0]].couleur=="blanc":
        (a,b)=(roiN.x,roiN.y)
        for x in [roiN.x, roiN.x+1, roiN.x-1]:
          for y in [roiN.y, roiN.y-1, roiN.y+1]:
            if (x,y) != (a,b) and roiN.dlegal(x,y):
              if self.echectest() == False:
                mat=False
                return mat
      if self.couleur=="noir":
        (a,b)=(roiB.x,roiB.y)
        for x in [roiB.x, roiB.x+1, roiB.x-1]:
          for y in [roiB.y, roiB.y-1, roiB.y+1]:
            if (x,y) != (a,b) and roiB.dlegal(x,y):
              if self.echectest() == False:
                mat=False
                return False
    else:   #transformer en fct° "parcours" pr réutiliser ds fct° "cloué" ?
      P=[L[0]]   #trajectoire entre pièce qui met en échec et le roi
      if dictionnaire_pieces.Echiquier[L[0]].couleur=="blanc":  #roi noir en échec
        if dictionnaire_pieces.Echiquier[L[0]].x==roiN.x or dictionnaire_pieces.Echiquier[L[0]].y==roiN.y:   #cas de la tour et de la dame (ligne droite)
          if dictionnaire_pieces.Echiquier[L[0]].x<roiN.x:
            for i in range(dictionnaire_pieces.Echiquier[L[0]].x,roiN.x):
              P+=[(i,dictionnaire_pieces.Echiquier[L[0]].y)]
          if dictionnaire_pieces.Echiquier[L[0]].x>roiN.x:
            for i in range(dictionnaire_pieces.Echiquier[L[0]].x,roiN.x,-1):
              P+=[(i,dictionnaire_pieces.Echiquier[L[0]].y)]
          if dictionnaire_pieces.Echiquier[L[0]].y<roiN.y:
            for i in range(dictionnaire_pieces.Echiquier[L[0]].y,roiN.y):
              P+=[(dictionnaire_pieces.Echiquier[L[0]].x,i)]
          if dictionnaire_pieces.Echiquier[L[0]].y>roiN.y:
            for i in range(dictionnaire_pieces.Echiquier[L[0]].y,roiN.y,-1):
              P+=[(dictionnaire_pieces.Echiquier[L[0]].y,i)]
        if abs(dictionnaire_pieces.Echiquier[L[0]].x-roiN.x)==abs(dictionnaire_pieces.Echiquier[L[0]].y-roiN.y):   #cas de la dame, du pion et du fou (diagonale)
          pasx = pasy = 1
          if dictionnaire_pieces.Echiquier[L[0]].x>roiN.x: pasx =-1
          if dictionnaire_pieces.Echiquier[L[0]].y>roiN.y: pasy =-1
          xn = dictionnaire_pieces.Echiquier[L[0]].x + pasx
          yn = dictionnaire_pieces.Echiquier[L[0]].y + pasy
          while xn!=roiN.x and yn!=roiN.y:
            P+=[(xn,yn)]
            xn+=pasx
            yn+=pasy
        for i in dictionnaire_pieces.Echiquier:  #teste quelle(s) pièce(s) peuvent s'intercaler/manger
          if dictionnaire_pieces.Echiquier[i].couleur=="noir":
            for j in P:
              if dictionnaire_pieces.Echiquier[i].dpossible(j[0],j[1]):
                mat=False
                return mat   #sort dès qu'on trouve une pièce pour bloquer
      if dictionnaire_pieces.Echiquier[L[0]].couleur=="noir":   #roi blanc en échec
        if dictionnaire_pieces.Echiquier[L[0]].x==roiB.x or dictionnaire_pieces.Echiquier[L[0]].y==roiB.y:   #cas de la tour et de la dame (ligne droite)
          if dictionnaire_pieces.Echiquier[L[0]].x<roiB.x:
            for i in range(dictionnaire_pieces.Echiquier[L[0]].x,roiB.x):
              P+=[(i,dictionnaire_pieces.Echiquier[L[0]].y)]
          if dictionnaire_pieces.Echiquier[L[0]].x>roiB.x:
            for i in range(dictionnaire_pieces.Echiquier[L[0]].x,roiB.x,-1):
              P+=[(i,dictionnaire_pieces.Echiquier[L[0]].y)]
          if dictionnaire_pieces.Echiquier[L[0]].y<roiB.y:
            for i in range(dictionnaire_pieces.Echiquier[L[0]].y,roiB.y):
              P+=[(dictionnaire_pieces.Echiquier[L[0]].x,i)]
          if dictionnaire_pieces.Echiquier[L[0]].y>roiB.y:
            for i in range(dictionnaire_pieces.Echiquier[L[0]].y,roiB.y,-1):
              P+=[(dictionnaire_pieces.Echiquier[L[0]].y,i)]
        if abs(dictionnaire_pieces.Echiquier[L[0]].x-roiB.x)==abs(dictionnaire_pieces.Echiquier[L[0]].y-roiB.y):   #cas de la dame, du pion et du fou (diagonale)
          pasx = pasy = 1
          if dictionnaire_pieces.Echiquier[L[0]].x>roiB.x: pasx =-1
          if dictionnaire_pieces.Echiquier[L[0]].y>roiB.y: pasy =-1
          xn = dictionnaire_pieces.Echiquier[L[0]].x + pasx
          yn = dictionnaire_pieces.Echiquier[L[0]].y + pasy
          while xn!=roiB.x and yn!=roiB.y:
            P+=[(xn,yn)]
            xn+=pasx
            yn+=paxy
        for i in dictionnaire_pieces.Echiquier:  #teste quelle(s) pièce(s) peuvent s'intercaler/manger
          if dictionnaire_pieces.Echiquier[i].couleur=="blanc":
            for j in P:
              if dictionnaire_pieces.Echiquier[i].dpossible(j[0],j[1]):
                mat=False
                return mat   #sort dès qu'on trouve une pièce pour bloquer
    return mat

  def pat(self): #vérifie qu'une pièce de la couleur de la piece peut encore jouer sans mettre le roi en echec
    for piece in dictionnaire_pieces.Echiquier:
      if self.couleur == piece.couleur :
        if 'cavalier' in piece.nom :
          #teste position
          for (x,y) in [(piece.x+1, piece.y+2), (piece.x-1, piece.y+2), (piece.x+1, piece.y-2), (piece.x-1, piece.y-2), (piece.x+2, piece.y-1), (piece.x+2, piece.y-1), (piece.x-2, piece.y-1), (piece.x-2, piece.y+1)]:
            if piece.dlegal(x,y):
              return False
        else : 
          #teste des positions
          (a,b)=(self.x,self.y)
          for x in [self.x, self.x+1, self.x-1]:
            for y in [self.y, self.y-1, self.y+1]:
              if (self.x,self.y) != (a,b):
                if piece.dlegal(x,y):
                  return False
    return True


class fou(Piece):
  def __init__(self, couleur, positionix, positioniy, nom):
    Piece.__init__(self, couleur,positionix, positioniy, nom)
  
  def dlegal(self, x, y):
    if (abs(x - self.x) == abs(y - self.y)): #déplacement autorisé pour ce type de pièce
      return True
    else : return False
    
  def dpossible(self, x, y):
    if self.cloue == False : 
      if (abs(x - self.x) == abs(y - self.y)):
        pasx = pasy = 1
        if x<self.x: pasx =-1 #parcours de gauche à droite
        if y<self.y: pasy =-1 #parcours de haut en bas
        xn = self.x + pasx #on part de la position initiale + 1 case
        yn = self.y + pasy 
        while xn!=x and yn!=y:
          if (xn,yn) in dictionnaire_pieces.Echiquier:
            return False
          xn += pasx
          yn += pasy
        return True
    else : return False


class tour(Piece):
  def __init__(self, couleur, positionix, positioniy, nom):
    Piece.__init__(self, couleur,positionix, positioniy, nom)
    #variable bool pour le roque
    self.joué = False
  
  def dpossible(self, x, y):
    if self.cloue == False : 
      if (x == self.x and y!=self.y): #déplacement vertical #déplacement autorisé pour ce type de pièce
        #vérification qu'on ne 'saute' pas au dessus d'autres pièces
        #Pour cela on parcourt case entre la position initiale et finale
        pas = 1
        if y<self.y: pas = -1 #parcourir de haut en bas
        for i in range(self.y+pas, y,pas):
            if (x,i) in dictionnaire_pieces.Echiquier:
              return False
        else: return True
      elif (x!=self.x and y == self.y): #déplacement horizontal #déplacement autorisé pour ce type de pièce
        #vérification qu'on ne 'saute' pas au dessus d'autres pièces
        pas = 1
        if x<self.x: pas = -1 #parcourir de gauche à droite
        for i in range(self.x+pas, x, pas):
            if (i,y) in dictionnaire_pieces.Echiquier:
              return False
        else : return True
      else : return False

  def dlegal(self, x,y):
    if (x == self.x and y!=self.y) or (x!=self.x and y == self.y): #déplacement vertical ou horizontal #déplacement autorisé pour ce type de pièce
      return True
    else : return False


class dame(Piece):
  def __init__(self, couleur, positionix, positioniy, nom):
    Piece.__init__(self, couleur,positionix, positioniy, nom)
    
  def dpossible(self, x, y):
    if self.cloue == False : 
      #déplacement comme une tour
      if (x == self.x and y!=self.y):  #déplacement vertical
        #vérification qu'on ne 'saute' pas au dessus d'autres pièces
        pas = 1
        if y<self.y: pas = -1 #parcourir de haut en bas
        for i in range(self.y+pas, y,pas):
            if (x,i) in dictionnaire_pieces.Echiquier:
              return False
        else: return True
      elif (x!=self.x and y == self.y): #déplacement horizontal autorisé pour ce type de pièce
        #vérification qu'on ne 'saute' pas au dessus d'autres pièces
        pas = 1
        if x<self.x: pas = -1 #parcourir de gauche à droite
        for i in range(self.x+pas, x, pas):
            if (i,y) in dictionnaire_pieces.Echiquier:
              return False
        else: return True
      #déplacement comme un fou
      elif abs(x - self.x) == abs(y - self.y) :
        #vérification qu'on ne 'saute' pas au dessus d'autres pièces
        pasx = pasy = 1
        if x<self.x: pasx =-1 #parcours de gauche à droite
        if y<self.y: pasy =-1 #parcours de haut en bas
        xn = self.x + pasx #on part de la position initiale + 1 case
        yn = self.y + pasy 
        while xn!=x and yn!=y:
          if (xn,yn) in dictionnaire_pieces.Echiquier:
            return False
          xn += pasx
          yn += pasy
        else : return True
    else : return False
  
  def dlegal(self, x, y):
    if (x == self.x and y!=self.y) or (x!=self.x and y == self.y) or (abs(x - self.x) == abs(y - self.y)):
      return True
    else : return False


class roi(Piece):
  def __init__(self, couleur, positionix, positioniy, nom):
    Piece.__init__(self, couleur,positionix, positioniy, nom)
    #variable bool pour vérifier si le roque est possible
    self.joué = False
    self.echec = False #variable bool pour restreindre les mouvements du roi
  
  #sans prendre en compte l'échec
  def dpossible(self, x,y):
    if self.echec == False and self.echectest() == False:
      davant_arriere1case = ( x == self.x and ((y == self.y + 1) or (y == self.y-1)))
      ddiagonale1case = (x == self.x + 1 or x == self.x - 1) and ((y == self.y + 1) or (y == self.y - 1))
      dcoté1case = (( y == self.y and ((x == self.x + 1) or (x == self.x-1)) ))
      if davant_arriere1case or dcoté1case or ddiagonale1case or self.roque(x,y):
        return True
    else : return False
  
  def dlegal(self, x,y):
    if self.dpossible(x,y) or self.roque(x,y): #roque on regarde s'il y a des pièces entre donc pas le mieux
      return True
  
  def roque(self, x, y):
    #truc spécifique au roque
    #vérifier la couleur
    if self.couleur == 'blanc':
      if self.joué == False and (x,y) == (self.x+2, self.y) and ('tour' in dictionnaire_pieces.Echiquier[(7,0)].nom) and dictionnaire_pieces.Echiquier[(7,0)].joué==False: #roque à droite (petit roque)
        entre=False
        for i in range(self.x+1,self.x+3):  #vérifie si il y a des pièces entre
          if (i,0) in dictionnaire_pieces.Echiquier:
            entre=True
        if entre==False:
          return True

      elif self.joué == False and (x,y) == (self.x-2, self.y) and ('tour' in dictionnaire_pieces.Echiquier[(0,0)].nom) and dictionnaire_pieces.Echiquier[(0,0)].joué==False: #roque à gauche (grand roque)
        entre=False
        for i in range(self.x-1,self.x-4,-1):  #vérifie si il y a des pièces entre
          if (i,0) in dictionnaire_pieces.Echiquier:
            entre=True
        if entre==False:
          return True
      else : return None

    if self.couleur == 'noir':
      if self.joué == False and (x,y) == (self.x+2, self.y) and ('tour' in dictionnaire_pieces.Echiquier[(7,7)].nom) and dictionnaire_pieces.Echiquier[(7,7)].joué==False: #roque à droite (petit roque)
        entre=False
        for i in range(self.x+1,self.x+3):  #vérifie si il y a des pièces entre
          if (i,7) in dictionnaire_pieces.Echiquier:
            entre=True
        if entre==False:
          return True

      elif self.joué == False and (x,y) == (self.x-2, self.y) and ('tour' in dictionnaire_pieces.Echiquier[(0,7)].nom) and dictionnaire_pieces.Echiquier[(0,7)].joué==False: #roque à gauche (grand roque)
        entre=False
        for i in range(self.x-1, self.x-4,-1):  #vérifie si il y a des pièces entre
          if (i,7) in dictionnaire_pieces.Echiquier:
            entre=True
        if entre==False:
          return True
      else : return False


class cavalier(Piece):
  def __init__(self, couleur, positionix, positioniy, nom):
    Piece.__init__(self, couleur,positionix, positioniy, nom)
  
  def dpossible(self, x,y):
    if self.cloue() == False :
      dLavant = ((y == self.y + 2)  and ((x == self.x + 1) or (x == self.x - 1)))
      dLarriere = ((y == self.y - 2) and ((x == self.x + 1) or (x == self.x - 1)))
      dLdroite = ((x == self.x + 2) and ((y == self.y + 1) or (y == self.y - 1)))
      dLgauche = ((x == self.x - 2) and ((y == self.y + 1) or (y == self.y - 1)))
      if dLavant or dLarriere or dLdroite or dLgauche :
        return True
    else : return False
  
  def dlegal(self,x,y):
    if self.dpossible(x,y):
      return True
    else: return False


class pion(Piece):
  def __init__(self, couleur, positionix, positioniy, nom):
    Piece.__init__(self, couleur, positionix, positioniy, nom)
    #variable pour savoir si l'avancée de 2 cases est possible
    self.joué = False
    self.eppossible = False #ep = peut être pris en passant
    self.pepg = self.pepd = False #peut prendre en passant
  
  def dpossible(self, x, y):
    if self.cloue() == False :
      if self.couleur == 'blanc':
        pas = 1
      else : pas = -1 #noir
      if not(self.joué) and (x == self.x and y == self.y +2*pas) and not((self.x, self.y +pas) in dictionnaire_pieces.Echiquier): #avance de 2 cases
        self.eppossible = True
        return True
      elif (x == self.x and y == self.y +pas) and not((self.x, self.y +pas) in dictionnaire_pieces.Echiquier): #avance d'une case
        return True
      elif ((y == self.y +pas and x == self.x +pas) or (y == self.y +pas and x == self.x -pas)) and ((x,y) in dictionnaire_pieces.Echiquier): #prise en diagonale
        return True
      elif (x == self.x-1) and (y == self.y +pas) and ((self.x-1, self.y) in dictionnaire_pieces.Echiquier) and ('pion' in dictionnaire_pieces.Echiquier[(self.x-1,self.y)].nom) and (dictionnaire_pieces.Echiquier[(self.x-1,self.y)].eppossible): #prise en passant à gauche
        self.pepg = True
        return True #prise en passant gauche
      elif (x == self.x+1) and (y == self.y +pas) and ((self.x+1, self.y) in dictionnaire_pieces.Echiquier) and ('pion' in dictionnaire_pieces.Echiquier[(self.x+1,self.y)].nom) and (dictionnaire_pieces.Echiquier[(self.x+1,self.y)].eppossible): #pris en passant à droite
        self.pepd = True
        return True #prise en passant droite
      else : return False

  def dlegal(self, x, y):
    if self.couleur == 'blanc':
      pas = 1
    else : pas = -1
    if not(self.joué) and (x == self.x and y == self.y +2*pas): #avance de 2 cases
      self.eppossible = True
      return True
    elif (x == self.x and y == self.y +pas): #avance d'une case
      return True
    elif ((y == self.y +pas and x == self.x +pas) or (y == self.y +pas and x == self.x -pas)) and ((x,y) in dictionnaire_pieces.Echiquier): #prise en diagonale
      return True
    elif (x == self.x-1) and (y == self.y +pas) and ((self.x-1, self.y) in dictionnaire_pieces.Echiquier) and ('pion' in dictionnaire_pieces.Echiquier[(self.x-1,self.y)].nom) and (dictionnaire_pieces.Echiquier[(self.x-1,self.y)].eppossible): #prise en passant à gauche
      self.pepg = True
      return True #prise en passant gauche
    elif (x == self.x+1) and (y == self.y +pas) and ((self.x+1, self.y) in dictionnaire_pieces.Echiquier) and ('pion' in dictionnaire_pieces.Echiquier[(self.x+1,self.y)].nom) and (dictionnaire_pieces.Echiquier[(self.x-1,self.y)].eppossible): #pris en passant à droite
      self.pepd = True
      return True #prise en passant droite
    else : return False
