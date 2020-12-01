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
  
  #appelé quand une pièce a été prise
  def __del__(self):
    #est ce qu'il faut qu'on code le genre de la pièce pour pouvoir dire La reine a été prise et non la reine a été pris?
    print(f"Le {self.nom} {self.couleur} a été pris")
    
  def deplacement(self, position):
    #traduit position entrée par joueur (on considère qu'il n'entre que des positions possibles c'est à dire de a à h et de 1 à 7
    #essai de prise en compte des bords de l'échiquier
    if (x not in X) or (y not in Y):
      return 'Déplacement impossible'
    else:
      x = X[position[0]]
      y = Y[position [1]]
    #vérifier que le déplacement est possible pour la pièce
    if dpossible(self, x, y):
      #change la position de la pièce
      self.x = x
      self.y = y
    else : return 'Déplacement impossible' #à changer?
    
  def dpossible(self):
    #vérifie que le déplacement est possible
      return True or False
    #rajouter vérification déplacment sans sauter au dessus d'autres pièces
 
    
class fou(Piece):
  def __init__(self, couleur, positionix, positioniy, nom=fou):
    Piece.__init__(self, couleur,positionix, positioniy, nom)
  
  def dpossible(self, x, y):
    if (x - self.x == y - self.y) and not( y == self.y): 
      return True
    else : return False
    
    

class tour(Piece):
  def __init__(self, couleur, positionix, positioniy, nom='tour'):
    Piece.__init__(self, couleur,positionix, positioniy, nom)
    #variable bool pour le roque
    self.joué = False
  
  def dpossible(self, x, y):
    if (x == self.x and y!=self.y) or (x!=self.x and y == self.y): 
      return True
    else : return False
    

class dame(Piece):
  def __init__(self, couleur, positionix, positioniy, nom='dame'):
    Piece.__init__(self, couleur,positionix, positioniy, nom)
    
  def dpossible(self, x, y):
    if (x == self.x and y!=self.y) or (x!=self.x and y == self.y) or ((x - self.x == y - self.y) and not( y == self.y)) : 
      return True
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
    

    
    
    
    
    
    
    
    
 
    
 
 
    
