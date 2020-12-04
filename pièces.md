# Chess
#dictionnaire permettant traduction de lettre à position
#plus besoin 
X = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}
Y = {1:0, 2:1, 3:2, 4:3, 5:4, 6:5, 7:6, 8:7}

class Piece:
  def __init__(self, couleur, positionix, positioniy, nom):
    self.couleur = couleur
    self.x = positionix
    self.y = positioniy
    #nom est le type de pièce
    self.nom = nom
    
  def deplacement(self, position):
    #traduit position entrée par joueur (on considère qu'il n'entre que des positions possibles c'est à dire de a à h et de 1 à 7
    #sera traité autre part (lors du clic) finalement
    #essai de prise en compte des bords de l'échiquier
    if (x not in X) or (y not in Y):
      return 'Déplacement impossible'
    else:
      x = X[position[0]]  #mettre le lien entre le déplacement sur le plateau et les coordonnées 
      y = Y[position [1]]
    #vérifier que le déplacement est possible pour la pièce
    if dpossible(self, x, y):
      #change la position de la pièce
      if (x,y) in Echiquier and self.tour_de_jouer==couleur.Echiquier[(x,y)]:  #vérifie la couleur de la pièce si la case est occupée
        if (Echiquier[(self.x,self.y)]==roiB) and (roiB.self.joué==False):  #vérifie que le roi n'a pas été joué
          if (Echiquier[(x,y)]==tourB1) and (tourB1.self.joué==False): #vérifie que la tour n'a pas été jouée
            entre=False
            for i in range(self.x-1,-1,-1):  #vérifie si il y a des pièces entre
              if (i,0) in Echiquier:
                entre=True
            if entre==False:
              Echiquier[(self.x,self.y)],Echiquier[(x,y)]=Echiquier[(x,y)],Echiquier[(self.x,self.y)]  #échange le roi et la tour
              tourB1.self.joué=roiB.self.joué=True
              return 'Roque effectué'
            else: return 'Déplacement impossible'  #peut-être inutile selon les cases atteintes possibles 
          if (Echiquier[(x,y)]==tourB2) and (tourB2.self.joué==False):
            entre=False
            for i in range(self.x+1,7):
              if (i,0) in Echiquier:
                entre=True
            if entre==False:
              Echiquier[(self.x,self.y)],Echiquier[(x,y)]=Echiquier[(x,y)],Echiquier[(self.x,self.y)]
              tourB2.self.joué=roiB.self.joué=True
              return 'Roque effectué'
            else: return 'Déplacement impossible'
        if (Echiquier[(self.x,self.y)]==roiN) and (roiN.self.joué==False):
          if (Echiquier[(x,y)]==tourN1) and (tourN1.self.joué==False):
            entre=False
            for i in range(self.x-1,-1,-1):
              if (i,7) in Echiquier:
                entre=True
            if entre==False:
              Echiquier[(self.x,self.y)],Echiquier[(x,y)]=Echiquier[(x,y)],Echiquier[(self.x,self.y)]
              tourN1.self.joué=roiN.self.joué=True
              return 'Roque effectué'
            else: return 'Déplacement impossible'
          if (Echiquier[(x,y)]==tourN2) and (tourN2.self.joué==False):
            entre=False
            for i in range(self.x+1,7):
              if (i,7) in Echiquier:
                entre=True
            if entre==False:
              Echiquier[(self.x,self.y)],Echiquier[(x,y)]=Echiquier[(x,y)],Echiquier[(self.x,self.y)]
              tourN2.self.joué=roiN.self.joué=True
              return 'Roque effectué'
            else: return 'Déplacement impossible'
        else :
          return 'Déplacement impossible (case déjà occupée)'
      if (x,y) in Echiquier and self.tour_de_jouer!=couleur.Echiquier[(x,y)]:
        Echiquier.pop((x,y))  #pièce prise = supprimée de l'échiquier
      else:
        a=(self.x,self.y)
        self.x = x
        self.y = y
        Echiquier[a]=(x,y)
    else : return 'Déplacement impossible' #à changer?
    
  def dpossible(self):
    #vérifie que le déplacement est un bon déplacement pour le type de pièce
    #vérifie qu'on ne 'saute' pas au dessus de pièce
    # à rajouter vérification de pas mise en échec de son propre roi
      return True or False

    
  def echec(self):  #à appeler après chaque tour : restreint les mvts possibles
    if Echiquier[(self.x,self.y)].dpossible((roiN.x,roiN.y)):   #self.x et y : coordonnées de la pièce bougée
      print("Échec") #est-ce qu'on ajoute la couleur du roi et/ou une indication graphique ?
      return True
 
    
class fou(Piece):
  def __init__(self, couleur, positionix, positioniy, nom='fou'):
    Piece.__init__(self, couleur,positionix, positioniy, nom)
  
  def dpossible(self, x, y):
    if (abs(x - self.x) == abs(y - self.y)): #déplacement autorisé pour ce type de pièce
      #vérification qu'on ne 'saute' pas au dessus d'autres pièces
      pasx = pasy = 1
      if x<self.x: pasx =-1 #parcours de gauche à droite
      if y<self.y: pasy =-1 #parcours de haut en bas
      xn = self.x + pasx #on part de la position initiale + 1 case
      yn = self.y + pasy 
      while xn!=x and yn!=y:
        if (xn,yn) in Echiquier:
          return False
        xn += pasx
        yn += pasy
      else : return True
    else : return False


class tour(Piece):
  def __init__(self, couleur, positionix, positioniy, nom='tour'):
    Piece.__init__(self, couleur,positionix, positioniy, nom)
    #variable bool pour le roque
    self.joué = False
  
  def dpossible(self, x, y):
    if (x == self.x and y!=self.y): #déplacement vertical #déplacement autorisé pour ce type de pièce
      #vérification qu'on ne 'saute' pas au dessus d'autres pièces
      #Pour cela on parcourt case entre la position initiale et finale
      pas = 1
      if y<self.y: pas = -1 #parcourir de haut en bas
      for i in range(self.y+pas, y,pas):
          if (x,i) in Echiquier:
            return False
      else: return True
    elif (x!=self.x and y == self.y): #déplacement horizontal #déplacement autorisé pour ce type de pièce
      #vérification qu'on ne 'saute' pas au dessus d'autres pièces
      pas = 1
      if x<self.x: pas = -1 #parcourir de gauche à droite
      for i in range(self.x+pas, x, pas):
          if (i,y) in Echiquier:
            return False
      else : return True
    else : return False

class dame(Piece):
  def __init__(self, couleur, positionix, positioniy, nom='dame'):
    Piece.__init__(self, couleur,positionix, positioniy, nom)
    
  def dpossible(self, x, y):
    #déplacement comme une tour
    if (x == self.x and y!=self.y):  #déplacement vertical
      #vérification qu'on ne 'saute' pas au dessus d'autres pièces
      pas = 1
      if y<self.y: pas = -1 #parcourir de haut en bas
      for i in range(self.y+pas, y,pas):
          if (x,i) in Echiquier:
            return False
      else: return True
    elif (x!=self.x and y == self.y): #déplacement horizontal autorisé pour ce type de pièce
      #vérification qu'on ne 'saute' pas au dessus d'autres pièces
      pas = 1
      if x<self.x: pas = -1 #parcourir de gauche à droite
      for i in range(self.x+pas, x, pas):
          if (i,y) in Echiquier:
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
        if (xn,yn) in Echiquier:
          return False
        xn += pasx
        yn += pasy
      else : return True
    else : return False

class roi(Piece):
  def __init__(self, couleur, positionix, positioniy, nom='roi'):
    Piece.__init__(self, couleur,positionix, positioniy, nom)
    #variable bool pour vérifier si le roque est possible
    self.joué = False
  
  #sans prendre en compte l'échec
  def dpossible(x,y):
    if NotEchec:
      davant_arriere1case = ( x == self.x and ((y == self.y + 1) or (y == self.y-1)))
      ddiagonale1case = (x == self.x + 1 and y == self.y + 1)or (x == self.x - 1 and y == self.y - 1)
      dcoté1case = (( y == self.y and ((x == self.x + 1) or (x == self.x-1)) ))
      if davant_arriere1case or dcoté1case or ddiagonale1case:
        return True
    
    else : return False
    

class cavalier(Piece):
  def __init__(self, couleur, positionix, positioniy, nom='cavalier'):
    Piece.__init__(self, couleur,positionix, positioniy, nom)
  
  def dpossible(x,y):
    dLavant = ( y == self.y + 2  and ((x == self.x + 1) or (x == self.x - 1)))
    dLarriere = (y == self.x - 1 and ((x == self.x + 1) or (x == self.x - 1)))
    dLdroite = (( x == self.x + 2 and ((y == self.y + 1) or (y == self.y - 1))))
    dLgauche = (( x == self.x - 2 and ((y == self.y + 1) or (y == self.y - 1))))
    if dLavant or dLarrière or dLdroite or dLgauche :
      return True
    else : return false
    
class pion(Piece):
  def __init__(self, couleur, positionix, positioniy, nom='pion'):
    Piece.__init__(self, couleur, positionix, positioniy, nom)
    #variable pour savoir si l'avancée de 2 cases est possible
    self.joué = False
    #peut être transformer par une autre pièce (ou plutôt détruit et initialise une autre pièce à la place)
    self.peutchanger = False
  def dpossible(self, x, y):
    #cas de prise en diagonale à considérer
    if not(self.joué):
      if (y == self.y +2) or (y == self.y +1) or (prise and y == self.y +1 and x == self.x +1) or (prise and y == self.y +1 and x == self.x -1):
        return True
    if (y == self.y +1) or (prise and y == self.y +1 and x == self.x +1) or (prise and y == self.y +1 and x == self.x -1): return True
    else : return false
    

    
    
    
    
    
    
    
    
 
    
 
 
    
