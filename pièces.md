# Chess
#dictionnaire permettant traduction de lettre à position
X = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}
Y = {1:0, 2:1, 3:2, 4:3, 5:4, 6:5, 7:6, 8:7}

class Piece:
  def __init__(self, couleur, positionix, positioniy, nom):
    self.couleur = couleur
    self.positionx = positionix
    self.positiony = positioniy
    #nom est le type de pièce
    self.nom = nom
  
  #appelé quand une pièce a été prise
  def __del__(self):
    #est ce qu'il faut qu'on code le genre de la pièce pour pouvoir dire La reine a été prise et non la reine a été pris?
    print(f"Le {self.nom} {self.couleur} a été pris")
    
  def deplacement(self, position):
    #traduit position entrée par joueur (on considère qu'il n'entre que des positions possibles c'est à dire de a à h et de 1 à 7
    x = X[position[0]]
    y = Y[position [1]]
    #vérifier que le déplacement est possible pour la pièce
    if dpossible(self, x, y):
      #change la position de la pièce
      self.position = [x,y]
    else : return 'Déplacement impossible'
    
  def dpossible(self):
    #vérifie que le déplacement est possible
    
class fou(Piece):
  def __init__(self, couleur, positionix, positioniy, nom=fou):
    Piece.__init__(self, couleur,positionix, positioniy, nom)
  
  #est ce qu'on doit considérer qu'une personne peut essayer de ne pas déplacer une pièce?
  def dpossible(self, x, y):
    if x - self.positionx == y - self.positiony : 
      return True
    else : return False
    
    

class tour(Piece):
  def __init__(self, couleur, positionix, positioniy, nom=tour):
    Piece.__init__(self, couleur,positionix, positioniy, nom)
    #variable bool pour le roque
    self.joué = False
  
  def dpossible(self, x, y):
    if x == self.positionx or y == self.positiony : 
      return True
    else : return False
    

class dame(Piece):
  def __init__(self, couleur, positionix, positioniy nom=dame):
    Piece.__init__(self, couleur,positionix, positioniy, nom)
    
  def dpossible(self, x, y):
    if (x == self.positionx or y == self.positiony) or (x - self.positionx == y - self.positiony) : 
      return True
    else : return False
    
class roi(Piece):
  def __init__(self, couleur, positionix, positioniy, nom=roi):
    Piece.__init__(self, couleur,positionix, positioniy, nom)
    #variable bool pour vérifier si le roque est possible
    self.joué = False
  
  #sans prendre en compte l'échec
  def dpossible(x,y):

class cavalier(Piece):
  def __init__(self, couleur, positionix, positioniy nom=cavalier):
    Piece.__init__(self, couleur,positionix, positioniy, nom)
    
class pion(Piece):
  def __init__(self, couleur, positionix, positioniy, nom=pion):
    Piece.__init__(self, couleur, positionix, positioniy, nom)
    #variable pour savoir si l'avancée de 2 cases est possible
    self.joué = False

    
    
    
    
    
    
    
    
 
    
 
 
    
