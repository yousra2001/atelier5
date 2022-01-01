class vecteur2d : #classe principale vecteur 2d
    x=0
    y=0
    def __init__(self,x,y): #methode pour defininie les variables
        self.x = x
        self.y = y
    def show(self): #fct qui affiche les objects
          return "vecteur: x=" +str(self.x)+" ,y= "+str(self.y)+ " ."
#la surcharge des 2 vecteurs
    def __add__(self, other):
         x = self.x + other.x
         y = self.y + other.y
         p = vecteur2d(x,y)
         return p
 v1 = vecteur2d(2,2) #object1
 print(v1.show())
 v2 = vecteur2d(4,3) #object2
 print(v2.show())

 v3 = v1 + v2
 print(v3.show())