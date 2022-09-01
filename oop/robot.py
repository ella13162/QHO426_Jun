#blueprint for Human object
class Robot:

  #class attribute
  MAX_ENERGY = 100

  #initialiser of class
  def __init__(self):
    #instance attributes
    self.name = "Robot"
    self.age = 0
    self.energy = 0

  def __str__(self):
    return f"Robot {self.name} is {self.age} years old, years old, and had energy {self.energy}"

  def __repr__(self):
    return f"Robot(name = {self.name}, age ={self.age}"
    
  #instance method
  def display(self):
    print(f"I am {self.name}")

  def grow(self):
    self.age += 1

  def eat (self, amount):
    self.energy += amount
    if self.energy > Robot.MAX_ENERGY:
      self.energy = Robot.MAX_ENERGY

  def move(self, distance):
    self.energy -= distance
    if self.energy < 0:
      self.energy = 0
      
if __name__ == "__main__":
  rob = Robot()
  rob.display()
  print(rob)
  print(repr(rob))
  rob.eat(94)
  print(rob)
  rob.move(73)
  print(rob)
  rob.eat(256)
  rob.move(101)
  rob.grow()
  rob.grow()
  print(rob)