#blueprint for Human object
class Human:

  #class attribute
  MAX_ENERGY = 100

  #initialiser of class
  def __init__(self):
    #instance attributes
    self.name = "Human"
    self.age = 0
    self.energy = Human.MAX_ENERGY
    
  #magic methods
  def __str__(self):
    return f"Human {self.name} is {self.age} years old, and had energy {self.energy}"

  def __repr__(self):
    return f"Human(name = {self.name}, age = {self.age})"
  
  #instance method
  def display(self):
    print(f"I am {self.name}")

  def grow(self):
    self.age += 1

  def eat (self, amount):
    self.energy += amount
    if self.energy > Human.MAX_ENERGY:
      self.energy = Human.MAX_ENERGY

  def move(self, distance):
    self.energy -= distance
    if self.energy < 0:
      self.energy = 0

if __name__ == "__main__":
  h = Human()
  h.display()
  print(h)
  print(repr(h))
  h.eat(94)
  print(h)
  h.move(73)
  print(h)
  h.eat(256)
  h.move(101)
  h.grow()
  h.grow()
  print(h)