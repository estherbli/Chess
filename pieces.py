import pygame
import dpieces
path=""
path_milo = "C:\\Users\\emili\\OneDrive\\Documents\\CPES-2\\informatique\\chess"
path_esther="C:\\Users\\esthe\\OneDrive\\Bureau\\CPES-L2\\Info\\projet"
path_clo="C:\\Users\\cloth\\Documents\\CPES\\CPES2\\algo\\projet"

class Piece:
  def __init__(self, couleur, positionix, positioniy, nom):
    pygame.init()
    self.couleur = couleur
    self.x = positionix
    self.y = positioniy
    #nom est le type de pièce
    self.nom = nom #nom est le type de pièce
    self.image = pygame.image.load(f"{path}\\{nom}.png")

  def deplacement(self, position): #change la position de la pièce et supprime la pièce mangée du dictionnaire
    x = position[0] #transforme le tuple en deux coordonnées distinctes
    y = position [1]
    #vérifier que le déplacement est possible pour la pièce
    if 'roi' in self.nom:
      if self.dpossible(x,y) and self.roque(x,y) == True:
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
        dpieces.Echiquier[(x,y)] = self #on bouge la pièce en la rajoutant dans le dictionnaire avec comme clé sa nouvelle position
        dpieces.Echiquier.pop(ancienxyroi) #on supprime l'ancienne pièce
        #bouger la tour
        dpieces.Echiquier[ancienxytour].joué = True
        dpieces.Echiquier[ancienxytour].x = nouveauxytour[0]
        dpieces.Echiquier[nouveauxytour] = dpieces.Echiquier[ancienxytour]
        dpieces.Echiquier.pop(ancienxytour)
        return None #le déplacement est fini, le roque a été fait
    #on vérifie que le déplacement est possible
    if self.dpossible(x,y):
      piece_prise = None
      if (x,y) in dpieces.Echiquier: #prendre une pièce
        if self.couleur != dpieces.Echiquier[(x,y)].couleur:  #vérifie que la pièce qui va être prise est bien de la couleur adverse
          if 'roi' in dpieces.Echiquier[(x,y)].nom: #on ne peut pas manger le roi
            return 'Déplacement impossible'
          else :
            piece_prise = dpieces.Echiquier[(x,y)]
            dpieces.Echiquier.pop((x,y))  #pièce prise = supprimée de l'échiquier
        else : return 'Déplacement impossible' #on ne peut pas manger un de ses propres pions
      else : #cas de la prise en passant
        if 'pion' in self.nom:
          if self.pepg == True:
            piece_prise = dpieces.Echiquier[(self.x-1,self.y)]
            dpieces.Echiquier.pop((self.x-1,self.y)) #prend la pièce en passant à gauche
            self.pepg = False
          if self.pepd == True:
            piece_prise = dpieces.Echiquier[(self.x+1,self.y)]
            dpieces.Echiquier.pop((self.x+1,self.y)) #prend la pièce en passant à droite
            self.pepd = False
      #bouger la pièce
      ancienxy = (self.x,self.y)
      self.x = x #changer les coordonnées de la pièce
      self.y = y
      dpieces.Echiquier[(x,y)] = self #on bouge la pièce en la rajoutant dans le dictionnaire avec comme clé sa nouvelle position
      dpieces.Echiquier.pop(ancienxy) #on supprime l'ancienne clé (position) de la pièce

      if (self.couleur == 'blanc' and dpieces.roiB.echec == True) or (self.couleur == 'noir' and dpieces.roiN.echec == True): #si on était déjà en échec on doit ne plus être en échec
        if 'roi' in self.nom : echec = False #déjà tester dans dpossible du roi
        else : echec = self.echectest()
        if echec:
          #remettre la piece prise
          (self.x,self.y) = ancienxy
          dpieces.Echiquier[ancienxy] = self #piece dans sa position originale
          dpieces.Echiquier.pop((x,y)) #enlève la piece déplacée
          if piece_prise != None :
            #remettre la piece prise
            dpieces.Echiquier[(piece_prise.x, piece_prise.y)] = piece_prise
          return 'Déplacement impossible'
        else : #on n'est plus en echec et on peut se déplacer
          if self.couleur == 'blanc': dpieces.roiB.echec = False
          if self.couleur == 'noir': dpieces.roiN.echec = False

      if (('roi' in self.nom) or ('pion' in self.nom) or ('tour' in self.nom)):
        self.joué = True

      #changer eppossible False sauf le self
      if self.couleur == 'blanc' : yep = 3 #yep = y (position) des pions qui auraient pu être pris en passant mais qui ne peuvent plus l'être
      else : yep = 4
      for i in range(0,8):
        if (i, yep) in dpieces.Echiquier and (i, yep) != (x,y):
          dpieces.Echiquier[(i,yep)].eppossible = False
    else : return 'Déplacement impossible'

  def dpossible(self,x,y):
    #vérifie que le déplacement est un bon déplacement pour le type de pièce
    # à rajouter vérification de pas mise en échec de son propre roi (fait avec cloué)
    # vérifie qu'on ne saute pas au dessus de pièce
    return True or False

  def dlegal(self, x,y):
    #deplacement autorisé pour ce type de pièce
    #ne sert que dans cloue
    return True or False

  def cloue(self,x,y):
    if self.couleur=="blanc": #couleur de la pièce sur laquelle on applique
      if self.x==dpieces.roiB.x or self.y==dpieces.roiB.y:   #déplacement en colonnes et lignes
        if self.x<dpieces.roiB.x:
          for xn in range(self.x+1,dpieces.roiB.x,1): #parcours entre pièce à clouer et roi
            if (xn,self.y) in dpieces.Echiquier:
              return False
          for xn in range(self.x-1,-1,-1):   #parcours entre pièce à clouer et suivante
            if (xn,self.y) in dpieces.Echiquier and not('roi' in dpieces.Echiquier[(xn,self.y)].nom):
              if dpieces.Echiquier[(xn,self.y)].couleur=="noir" and dpieces.Echiquier[(xn,self.y)].dlegal(dpieces.roiB.x,dpieces.roiB.y):
                if not(self.y==y):
                  return True
              else: return False
        if self.x>dpieces.roiB.x:
          for xn in range(self.x-1,dpieces.roiB.x,-1):
            if (xn,self.y) in dpieces.Echiquier:
              return False
          for xn in range(self.x+1,8):   #parcours entre pièce à clouer et suivante
            if (xn,self.y) in dpieces.Echiquier and not('roi' in dpieces.Echiquier[(xn,self.y)].nom):
              if dpieces.Echiquier[(xn,self.y)].couleur=="noir" and dpieces.Echiquier[(xn,self.y)].dlegal(dpieces.roiB.x,dpieces.roiB.y):
                if not(self.y==y):
                  return True
              else: return False
        if self.y<dpieces.roiB.y:
          for yn in range(self.y+1,dpieces.roiB.y,1):
            if (self.x,yn) in dpieces.Echiquier:
              return False
          for yn in range(self.y-1,-1,-1):   #parcours entre pièce à clouer et suivante
            if (self.x,yn) in dpieces.Echiquier and not('roi' in dpieces.Echiquier[(self.x,yn)].nom):
              if dpieces.Echiquier[(self.x,yn)].couleur=="noir" and dpieces.Echiquier[(self.x,yn)].dlegal(dpieces.roiB.x,dpieces.roiB.y):
                if not(self.x==x):
                  return True
              else: return False
        if self.y>dpieces.roiB.y:
          for yn in range(self.y-1,-dpieces.roiB.y,-1):
            if (self.x,yn) in dpieces.Echiquier:
              return False
          for yn in range(self.y+1,8):   #parcours entre pièce à clouer et suivante
            if (self.x,yn) in dpieces.Echiquier and not('roi' in dpieces.Echiquier[(self.x,yn)].nom):
              if dpieces.Echiquier[(self.x,yn)].couleur=="noir" and dpieces.Echiquier[(self.x,yn)].dlegal(dpieces.roiB.x,dpieces.roiB.y):
                if not(self.x==x):
                  return True
              else: return False
      if abs(self.x-dpieces.roiB.x)==abs(self.y-dpieces.roiB.y):    #déplacement en diagonales
        pasx = pasy = 1
        if self.x<dpieces.roiB.x: pasx =-1
        if self.y<dpieces.roiB.y: pasy =-1
        xn = self.x + pasx
        yn = self.y + pasy
        for xn in range(0,dpieces.roiB.x,-pasx):
          for yn in range(0,dpieces.roiB.y,-pasy):
            if (xn,yn) in dpieces.Echiquier:
              return False
        while not (xn,yn) in dpieces.Echiquier and 0<=xn<8 and 0<=yn<8:   #parcours entre pièce à clouer et suivante
          xn+=pasx
          yn+=pasy
        if (xn,yn) in dpieces.Echiquier and not('roi' in dpieces.Echiquier[(xn,yn)].nom):
          if dpieces.Echiquier[(xn,yn)].couleur=="noir" and dpieces.Echiquier[(xn,yn)].dlegal(dpieces.roiB.x,dpieces.roiB.y):
            if not(abs(xn-x)==abs(yn-y)):
              return True   #ds dpossible : si cloué=True => dpossible=False
          else: return False

    if self.couleur=="noir":   #couleur de la pièce sur laquelle on applique
      if self.x==dpieces.roiN.x or self.y==dpieces.roiN.y:   #déplacement en colonnes et lignes
        if self.x<dpieces.roiN.x:
          for xn in range(self.x+1,dpieces.roiN.x,1):
            if (xn,self.y) in dpieces.Echiquier:
              return False
          for xn in range(self.x-1,-1,-1):   #parcours entre pièce à clouer et suivante
            if (xn,self.y) in dpieces.Echiquier and not('roi' in dpieces.Echiquier[(xn,self.y)].nom):
              if dpieces.Echiquier[(xn,self.y)].couleur=="blanc" and dpieces.Echiquier[(xn,self.y)].dlegal(dpieces.roiN.x,dpieces.roiN.y):
                if not(self.y==y):
                  return True
              else: return False
        if self.x>dpieces.roiN.x:
          for xn in range(self.x-1,dpieces.roiN.x,-1):
            if (xn,self.y) in dpieces.Echiquier:
              return False
          for xn in range(self.x+1,8):   #parcours entre pièce à clouer et suivante
            if (xn,self.y) in dpieces.Echiquier and not('roi' in dpieces.Echiquier[(xn,self.y)].nom):
              if dpieces.Echiquier[(xn,self.y)].couleur=="blanc" and dpieces.Echiquier[(xn,self.y)].dlegal(dpieces.roiN.x,dpieces.roiN.y):
                if not(self.y==y):
                  return True
              else: return False
        if self.y<dpieces.roiN.y:
          for yn in range(self.y+1,dpieces.roiN.y,1):
            if (self.x,yn) in dpieces.Echiquier:
              return False
          for yn in range(self.y-1,-1,-1):   #parcours entre pièce à clouer et suivante
            if (self.x,yn) in dpieces.Echiquier and not('roi' in dpieces.Echiquier[(self.x,yn)].nom):
              if dpieces.Echiquier[(self.x,yn)].couleur=="blanc" and dpieces.Echiquier[(self.x,yn)].dlegal(dpieces.roiN.x,dpieces.roiN.y):
                if not(self.x==x):
                  return True
              else: return False
        if self.y>dpieces.roiN.y:
          for yn in range(self.y-1,dpieces.roiN.y,-1):
            if (self.x,yn) in dpieces.Echiquier:
              return False
          for yn in range(self.y+1,8):   #parcours entre pièce à clouer et suivante
            if (self.x,yn) in dpieces.Echiquier and not('roi' in dpieces.Echiquier[(self.x,yn)].nom):
              if dpieces.Echiquier[(self.x,yn)].couleur=="blanc" and dpieces.Echiquier[(self.x,yn)].dlegal(dpieces.roiN.x,dpieces.roiN.y):
                if not(self.x==x):
                  return True
              else: return False
      if abs(self.x-dpieces.roiN.x)==abs(self.y-dpieces.roiN.y):    #déplacement en diagonales
        pasx = pasy = 1
        if self.x<dpieces.roiN.x: pasx =-1
        if self.y<dpieces.roiN.y: pasy =-1
        xn = self.x + pasx
        yn = self.y + pasy
        for xn in range(0,dpieces.roiN.x,-pasx):
          for yn in range(0,dpieces.roiN.y,-pasy):
            if (xn,yn) in dpieces.Echiquier:
              return False
        while not (xn,yn) in dpieces.Echiquier and 0<=xn<8 and 0<=yn<8:   #parcours entre pièce à clouer et suivante
          xn+=pasx
          yn+=pasy
        if (xn,yn) in dpieces.Echiquier and not('roi' in dpieces.Echiquier[(xn,yn)].nom):
          if dpieces.Echiquier[(xn,yn)].couleur=="blanc" and dpieces.Echiquier[(xn,yn)].dlegal(dpieces.roiN.x,dpieces.roiN.y):
            if not(abs(xn-x)==abs(yn-y)):
              return True   #ds dpossible : si cloué=True => dpossible=False
          else: return False
    return False


  def echectest(self): #a appeler pour vérifier si echec sur roi de la même couleur sans changer propriété ni vérifier mat #renvoie True
    if self.couleur == 'noir': (roix, roiy) = (dpieces.roiN.x, dpieces.roiN.y)
    else : (roix, roiy) = (dpieces.roiB.x, dpieces.roiB.y)
    for i in dpieces.Echiquier:
      if self.couleur=="blanc" and dpieces.Echiquier[i].couleur=="noir":
        if not('roi' in dpieces.Echiquier[i].nom) and not(dpieces.Echiquier[i].x == roix and dpieces.Echiquier[i].y == roiy) and dpieces.Echiquier[i].dpossible(roix,roiy):   #vérifie si la pièce adverse atteint le roi
          #cas ou roi mange une piece on ne va pas tester si cette piece peut manger le roi sinon problème dans dpossible
          echec=True
          return echec
      if self.couleur=="noir" and dpieces.Echiquier[i].couleur=="blanc":
        if not('roi' in dpieces.Echiquier[i].nom) and not(dpieces.Echiquier[i].x == roix and dpieces.Echiquier[i].y == roiy) and dpieces.Echiquier[i].dpossible(roix,roiy):   #vérifie si la pièce adverse atteint le roi
          #cas ou roi mange une piece on ne va pas tester si cette piece peut manger le roi sinon problème dans dpossible
          echec=True
          return echec
    return False


  def echec_et_mat(self): #à appeler sur une pièce qqconque (qui vient d'être déplacée) #renvoie True ou 'mat'
    echec=False
    cavalier = False
    L=[] #garde la position des pièces qui mettent en échec (utile pour mat)
    for i in dpieces.Echiquier:
      if not('roi' in dpieces.Echiquier[i].nom):
        if self.couleur=="blanc" and dpieces.Echiquier[i].couleur=="blanc":
          if dpieces.Echiquier[i].dpossible(dpieces.roiN.x,dpieces.roiN.y):   #vérifie si la pièce adverse atteint le roi
            echec=True
            dpieces.roiN.echec = True
            L+=[i]
            if 'cavalier' in dpieces.Echiquier[i].nom :
              cavalier = True
        if self.couleur=="noir" and dpieces.Echiquier[i].couleur=="noir":
          if dpieces.Echiquier[i].dpossible(dpieces.roiB.x,dpieces.roiB.y):
            echec=True
            dpieces.roiB.echec = True
            L+=[i]
            if 'cavalier' in dpieces.Echiquier[i].nom :
              cavalier = True
    if echec:
      if self.mat(L,cavalier):
        return 'mat'
    return echec

  def mat(self, L, cavalier):    #appel sur la même pièce que echec
    mat=True          #part du principe que c'est vrai : plus facile à manipuler
    if self.couleur == 'blanc' : roi = dpieces.roiN
    else : roi = dpieces.roiB
    if len(L)>1 or cavalier:  #seul le roi peut se sauver #le cavalier peut être autre que la première pièce
      if roi.peut_bouger():
        return False
      else : return mat
    else: #une pièce peut s'interposer
      if roi.peut_bouger():
        return False
      #transformer en fct° "parcours" pr réutiliser ds fct° "cloué" ?
      P=[L[0]]   #trajectoire entre pièce qui met en échec et le roi
      if dpieces.Echiquier[L[0]].couleur=="blanc":  #roi noir en échec
        if dpieces.Echiquier[L[0]].x==dpieces.roiN.x or dpieces.Echiquier[L[0]].y==dpieces.roiN.y:   #cas de la tour et de la dame (ligne droite)
          if dpieces.Echiquier[L[0]].x<dpieces.roiN.x:
            for i in range(dpieces.Echiquier[L[0]].x,dpieces.roiN.x):
              P+=[(i,dpieces.Echiquier[L[0]].y)]
          if dpieces.Echiquier[L[0]].x>dpieces.roiN.x:
            for i in range(dpieces.Echiquier[L[0]].x,dpieces.roiN.x,-1):
              P+=[(i,dpieces.Echiquier[L[0]].y)]
          if dpieces.Echiquier[L[0]].y<dpieces.roiN.y:
            for i in range(dpieces.Echiquier[L[0]].y,dpieces.roiN.y):
              P+=[(dpieces.Echiquier[L[0]].x,i)]
          if dpieces.Echiquier[L[0]].y>dpieces.roiN.y:
            for i in range(dpieces.Echiquier[L[0]].y,dpieces.roiN.y,-1):
              P+=[(dpieces.Echiquier[L[0]].y,i)]
        if abs(dpieces.Echiquier[L[0]].x-dpieces.roiN.x)==abs(dpieces.Echiquier[L[0]].y-dpieces.roiN.y):   #cas de la dame, du pion et du fou (diagonale)
          pasx = pasy = 1
          if dpieces.Echiquier[L[0]].x>dpieces.roiN.x: pasx =-1
          if dpieces.Echiquier[L[0]].y>dpieces.roiN.y: pasy =-1
          xn = dpieces.Echiquier[L[0]].x + pasx
          yn = dpieces.Echiquier[L[0]].y + pasy
          while xn!=dpieces.roiN.x and yn!=dpieces.roiN.y:
            P+=[(xn,yn)]
            xn+=pasx
            yn+=pasy
        for i in dpieces.Echiquier:  #teste quelle(s) pièce(s) peuvent s'intercaler/manger
          if dpieces.Echiquier[i].couleur=="noir":
            for j in P:
              if dpieces.Echiquier[i].dpossible(j[0],j[1]):
                mat=False
                return mat   #sort dès qu'on trouve une pièce pour bloquer
        return mat
      if dpieces.Echiquier[L[0]].couleur=="noir":   #roi blanc en échec
        if dpieces.Echiquier[L[0]].x==dpieces.roiB.x or dpieces.Echiquier[L[0]].y==dpieces.roiB.y:   #cas de la tour et de la dame (ligne droite)
          if dpieces.Echiquier[L[0]].x<dpieces.roiB.x:
            for i in range(dpieces.Echiquier[L[0]].x,dpieces.roiB.x):
              P+=[(i,dpieces.Echiquier[L[0]].y)]
          if dpieces.Echiquier[L[0]].x>dpieces.roiB.x:
            for i in range(dpieces.Echiquier[L[0]].x,dpieces.roiB.x,-1):
              P+=[(i,dpieces.Echiquier[L[0]].y)]
          if dpieces.Echiquier[L[0]].y<dpieces.roiB.y:
            for i in range(dpieces.Echiquier[L[0]].y,dpieces.roiB.y):
              P+=[(dpieces.Echiquier[L[0]].x,i)]
          if dpieces.Echiquier[L[0]].y>dpieces.roiB.y:
            for i in range(dpieces.Echiquier[L[0]].y,dpieces.roiB.y,-1):
              P+=[(dpieces.Echiquier[L[0]].y,i)]
        if abs(dpieces.Echiquier[L[0]].x-dpieces.roiB.x)==abs(dpieces.Echiquier[L[0]].y-dpieces.roiB.y):   #cas de la dame, du pion et du fou (diagonale)
          pasx = pasy = 1
          if dpieces.Echiquier[L[0]].x>dpieces.roiB.x: pasx =-1
          if dpieces.Echiquier[L[0]].y>dpieces.roiB.y: pasy =-1
          xn = dpieces.Echiquier[L[0]].x + pasx
          yn = dpieces.Echiquier[L[0]].y + pasy
          while xn!=dpieces.roiB.x and yn!=dpieces.roiB.y:
            P+=[(xn,yn)]
            xn+=pasx
            yn+=pasy
        for i in dpieces.Echiquier:  #teste quelle(s) pièce(s) peuvent s'intercaler/manger
          if dpieces.Echiquier[i].couleur=="blanc":
            for j in P:
              if dpieces.Echiquier[i].dpossible(j[0],j[1]):
                mat=False
                return mat   #sort dès qu'on trouve une pièce pour bloquer
        return mat

  def pat(self): #vérifie que la couleur adverse peut encore bouger
    for piececle in dpieces.Echiquier:
      piece = dpieces.Echiquier[piececle]
      if self.couleur != piece.couleur :
        if 'cavalier' in piece.nom :
          #teste position
          for (x,y) in [(piececle[0]+1, piececle[1]+2),
                        (piececle[0]-1, piececle[1]+2),
                        (piececle[0]+1, piececle[1]-2),
                        (piececle[0]-1, piececle[1]-2),
                        (piececle[0]+2, piececle[1]-1),
                        (piececle[0]+2, piececle[1]-1),
                        (piececle[0]-2, piececle[1]-1),
                        (piececle[0]-2, piececle[1]+1)]:
            if piece.dpossible(x,y):
              return False
        else :
          #teste des positions
          (a,b) = (piece.x,piece.y)
          for x in [piece.x, piece.x+1, piece.x-1]:
            for y in [piece.y, piece.y-1, piece.y+1]:
              if (x,y) != (a,b):
                if piece.dpossible(x,y):
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
    if self.cloue(x,y) == False :
      if (abs(x - self.x) == abs(y - self.y)):
        pasx = pasy = 1
        if x<self.x: pasx =-1 #parcours de gauche à droite
        if y<self.y: pasy =-1 #parcours de haut en bas
        xn = self.x + pasx #on part de la position initiale + 1 case
        yn = self.y + pasy
        while xn!=x and yn!=y:
          if (xn,yn) in dpieces.Echiquier:
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
    if self.cloue(x,y) == False :
      if (x == self.x and y!=self.y): #déplacement vertical #déplacement autorisé pour ce type de pièce
        #vérification qu'on ne 'saute' pas au dessus d'autres pièces
        #Pour cela on parcourt case entre la position initiale et finale
        pas = 1
        if y<self.y: pas = -1 #parcourir de haut en bas
        for i in range(self.y+pas, y,pas):
            if (x,i) in dpieces.Echiquier:
              return False
        else: return True
      elif (x!=self.x and y == self.y): #déplacement horizontal #déplacement autorisé pour ce type de pièce
        #vérification qu'on ne 'saute' pas au dessus d'autres pièces
        pas = 1
        if x<self.x: pas = -1 #parcourir de gauche à droite
        for i in range(self.x+pas, x, pas):
            if (i,y) in dpieces.Echiquier:
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
    if self.cloue(x,y) == False :
      #déplacement comme une tour
      if (x == self.x and y!=self.y):  #déplacement vertical
        #vérification qu'on ne 'saute' pas au dessus d'autres pièces
        pas = 1
        if y<self.y: pas = -1 #parcourir de haut en bas
        for i in range(self.y+pas, y,pas):
            if (x,i) in dpieces.Echiquier:
              return False
        else: return True
      elif (x!=self.x and y == self.y): #déplacement horizontal autorisé pour ce type de pièce
        #vérification qu'on ne 'saute' pas au dessus d'autres pièces
        pas = 1
        if x<self.x: pas = -1 #parcourir de gauche à droite
        for i in range(self.x+pas, x, pas):
            if (i,y) in dpieces.Echiquier:
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
          if (xn,yn) in dpieces.Echiquier:
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


  def dpossible(self, x,y):
    if self.presderoioupion(x,y)==False: #echectest prend en compte toutes les situations qui aurait pu se faire sans déplacer le roi
      davant_arriere1case = ( x == self.x and ((y == self.y + 1) or (y == self.y-1)))
      ddiagonale1case = (x == self.x + 1 or x == self.x - 1) and ((y == self.y + 1) or (y == self.y - 1))
      dcoté1case = (( y == self.y and ((x == self.x + 1) or (x == self.x-1)) ))
      if davant_arriere1case or dcoté1case or ddiagonale1case or self.roque(x,y):
        if self.echectest(x,y) == False :
          return True
    else : return False

  def presderoioupion(self,x,y): #vérifie que le roi ne peut pas se mettre en echec en se rapprochant de l'autre roi
    if self.couleur == 'blanc':
      for i in [(x+1,y),(x+1,y-1),(x,y+1),(x-1,y),(x-1,y-1),(x,y-1)]: #mise en échec par le roi adverse ->déplacement impossible
        if i in dpieces.Echiquier and dpieces.Echiquier[i].couleur!=self.couleur and ('roi' in dpieces.Echiquier[i].nom):
          return True
      for i in [(x+1,y+1),(x-1,y+1)]: #emplacement de pion qui pourrait manger le roi -> déplacement impossible
        if i in dpieces.Echiquier and dpieces.Echiquier[i].couleur!=self.couleur and ('roi' in dpieces.Echiquier[i].nom or 'pion' in dpieces.Echiquier[i].nom):
          return True
      return False
    if self.couleur == 'noir':
      for i in [(x+1,y),(x+1,y+1),(x,y+1),(x-1,y),(x-1,y+1),(x,y-1)]: #mise en échec par le roi adverse ->déplacement impossible
        if i in dpieces.Echiquier and dpieces.Echiquier[i].couleur!=self.couleur and ('roi' in dpieces.Echiquier[i].nom):
          return True
      for i in [(x+1,y-1),(x-1,y-1)]: #emplacement de pion qui pourrait manger le roi -> déplacement impossible
        if i in dpieces.Echiquier and dpieces.Echiquier[i].couleur!=self.couleur and (('roi' in dpieces.Echiquier[i].nom) or 'pion' in dpieces.Echiquier[i].nom):
          return True
      return False



  def roque(self, x, y):
    #vérifier la couleur
    if self.couleur == 'blanc':
      if self.joué == False and (x,y) == (self.x+2, self.y) and ('tour' in dpieces.Echiquier[(7,0)].nom) and dpieces.Echiquier[(7,0)].joué==False: #roque à droite (petit roque)
        entre=False
        for i in range(self.x+1,self.x+3):  #vérifie si il y a des pièces entre
          if (i,0) in dpieces.Echiquier:
            entre=True
        if entre==False:
          return True

      elif self.joué == False and (x,y) == (self.x-2, self.y) and ('tour' in dpieces.Echiquier[(0,0)].nom) and dpieces.Echiquier[(0,0)].joué==False: #roque à gauche (grand roque)
        entre=False
        for i in range(self.x-1,self.x-4,-1):  #vérifie si il y a des pièces entre
          if (i,0) in dpieces.Echiquier:
            entre=True
        if entre==False:
          return True
      else : return None

    if self.couleur == 'noir':
      if self.joué == False and (x,y) == (self.x+2, self.y) and ('tour' in dpieces.Echiquier[(7,7)].nom) and dpieces.Echiquier[(7,7)].joué==False: #roque à droite (petit roque)
        entre=False
        for i in range(self.x+1,self.x+3):  #vérifie si il y a des pièces entre
          if (i,7) in dpieces.Echiquier:
            entre=True
        if entre==False:
          return True

      elif self.joué == False and (x,y) == (self.x-2, self.y) and ('tour' in dpieces.Echiquier[(0,7)].nom) and dpieces.Echiquier[(0,7)].joué==False: #roque à gauche (grand roque)
        entre=False
        for i in range(self.x-1, self.x-4,-1):  #vérifie si il y a des pièces entre
          if (i,7) in dpieces.Echiquier:
            entre=True
        if entre==False:
          return True
      else : return False

  def echectest(self, roix, roiy): #a appeler pour vérifier si echec sur roi de la même couleur sans changer propriété ni vérifier mat #renvoie True
    piece_à_prendre = False
    #on se place comme si le roi s'était déplacé
    roi = dpieces.Echiquier[(self.x,self.y)]
    if (roix,roiy) in dpieces.Echiquier :
      piece_à_prendre = True
      piece_prise = dpieces.Echiquier[(roix,roiy)]
      dpieces.Echiquier.pop((roix,roiy))
    dpieces.Echiquier[(roix,roiy)] = roi
    dpieces.Echiquier.pop((self.x,self.y)) #pour que le roi ne bloque pas artificiellement sa propre mise en échec

    for i in dpieces.Echiquier:
      if self.couleur=="blanc" and dpieces.Echiquier[i].couleur=="noir":
        if not('roi' in dpieces.Echiquier[i].nom) and not(dpieces.Echiquier[i].x == roix and dpieces.Echiquier[i].y == roiy) and dpieces.Echiquier[i].dpossible(roix,roiy):   #vérifie si la pièce adverse atteint le roi
          echec=True
          #remet sitution initiale
          dpieces.Echiquier.pop((roix,roiy))
          if piece_à_prendre:
            dpieces.Echiquier[(roix,roiy)] = piece_prise
          dpieces.Echiquier[(roi.x,roi.y)] = roi
          return echec
      if self.couleur=="noir" and dpieces.Echiquier[i].couleur=="blanc":
        if not('roi' in dpieces.Echiquier[i].nom) and not(dpieces.Echiquier[i].x == roix and dpieces.Echiquier[i].y == roiy) and dpieces.Echiquier[i].dpossible(roix,roiy):
          echec=True
          #remet sitution initiale
          dpieces.Echiquier.pop((roix,roiy))
          if piece_à_prendre:
            dpieces.Echiquier[(roix,roiy)] = piece_prise
          dpieces.Echiquier[(roi.x,roi.y)] = roi
          return echec
    #remet sitution initiale
    dpieces.Echiquier.pop((roix,roiy))
    if piece_à_prendre:
      dpieces.Echiquier[(roix,roiy)] = piece_prise
    dpieces.Echiquier[(roi.x,roi.y)] = roi
    return False

  def peut_bouger(self):
    (a,b)=(self.x,self.y)
    for x in [self.x, self.x+1, self.x-1]:
      for y in [self.y, self.y-1, self.y+1]:
        if 0<=x<8 and 0<=y<8 and (x,y) != (a,b) and self.dpossible(x,y):
          if (x,y) in dpieces.Echiquier:
            if dpieces.Echiquier[(x,y)].couleur != self.couleur:
              return True
          else : return True
    return False

class cavalier(Piece):
  def __init__(self, couleur, positionix, positioniy, nom):
    Piece.__init__(self, couleur,positionix, positioniy, nom)

  def dpossible(self, x,y):
    if self.cloue(x,y) == False :
      dLavant = ((y == self.y + 2)  and ((x == self.x + 1) or (x == self.x - 1)))
      dLarriere = ((y == self.y - 2) and ((x == self.x + 1) or (x == self.x - 1)))
      dLdroite = ((x == self.x + 2) and ((y == self.y + 1) or (y == self.y - 1)))
      dLgauche = ((x == self.x - 2) and ((y == self.y + 1) or (y == self.y - 1)))
      if dLavant or dLarriere or dLdroite or dLgauche :
        return True
    else : return False

  def dlegal(self,x,y):
    dLavant = ((y == self.y + 2)  and ((x == self.x + 1) or (x == self.x - 1)))
    dLarriere = ((y == self.y - 2) and ((x == self.x + 1) or (x == self.x - 1)))
    dLdroite = ((x == self.x + 2) and ((y == self.y + 1) or (y == self.y - 1)))
    dLgauche = ((x == self.x - 2) and ((y == self.y + 1) or (y == self.y - 1)))
    if dLavant or dLarriere or dLdroite or dLgauche :
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
    if self.cloue(x,y) == False :
      if self.couleur == 'blanc':
        pas = 1
      else : pas = -1 #noir
      if not(self.joué) and (x == self.x and y == self.y +2*pas) and not((self.x, self.y +2*pas) in dpieces.Echiquier): #avance de 2 cases
        return True
      elif (x == self.x and y == self.y +pas) and not((self.x, self.y +pas) in dpieces.Echiquier): #avance d'une case
        return True
      elif ((y == self.y +pas and x == self.x +pas) or (y == self.y +pas and x == self.x -pas)) and ((x,y) in dpieces.Echiquier): #prise en diagonale
        return True
      elif (x == self.x-1) and (y == self.y +pas) and ((self.x-1, self.y) in dpieces.Echiquier) and ('pion' in dpieces.Echiquier[(self.x-1,self.y)].nom) and (dpieces.Echiquier[(self.x-1,self.y)].eppossible): #prise en passant à gauche
        self.pepg = True
        return True #prise en passant gauche
      elif (x == self.x+1) and (y == self.y +pas) and ((self.x+1, self.y) in dpieces.Echiquier) and ('pion' in dpieces.Echiquier[(self.x+1,self.y)].nom) and (dpieces.Echiquier[(self.x+1,self.y)].eppossible): #pris en passant à droite
        self.pepd = True
        return True #prise en passant droite
      else : return False

  def dlegal(self, x, y):
    if self.couleur == 'blanc':
      pas = 1
    else : pas = -1
    if not(self.joué) and (x == self.x and y == self.y +2*pas) and not((self.x, self.y +2*pas) in dpieces.Echiquier): #avance de 2 cases
      return True
    elif (x == self.x and y == self.y +pas) and not((self.x, self.y +pas) in dpieces.Echiquier): #avance d'une case
      return True
    elif ((y == self.y +pas and x == self.x +pas) or (y == self.y +pas and x == self.x -pas)) and ((x,y) in dpieces.Echiquier): #prise en diagonale
      return True
    elif (x == self.x-1) and (y == self.y +pas) and ((self.x-1, self.y) in dpieces.Echiquier) and ('pion' in dpieces.Echiquier[(self.x-1,self.y)].nom) and (dpieces.Echiquier[(self.x-1,self.y)].eppossible): #prise en passant à gauche
      self.pepg = True
      return True #prise en passant gauche
    elif (x == self.x+1) and (y == self.y +pas) and ((self.x+1, self.y) in dpieces.Echiquier) and ('pion' in dpieces.Echiquier[(self.x+1,self.y)].nom) and (dpieces.Echiquier[(self.x-1,self.y)].eppossible): #pris en passant à droite
      self.pepd = True
      return True #prise en passant droite
    else : return False
