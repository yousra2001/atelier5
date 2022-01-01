class Rectangle:
  name = "Rectangle"
  a = 0
  b = 0
  def __init__(self, a, b, name):
    self.name = name
    self.a = a
    self.b = b
  def show(self):
      return "le"+self.name+" est de langueur : " +str(self.a)+ " et de largeur: " +str(self.b)+"."
  def surface(self):
     return "sa surface est: "+(str(self.a * self.b))
class Carre(Rectangle):
  def __init__(self,a,name):
      super(). __init__(self,a)
      self.name = name
  def show(self):
     return "le" + self.name + " est de cote : " +str(self.a)+"."
  def surface(self):
      return "la surface du carre est : "+(str(self.a * self.a))
R = Rectangle(6,4," Rectangle ")
print(R.show())
print(R.surface())