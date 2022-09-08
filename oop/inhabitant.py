from abc import ABC
class Inhabitant(ABC):

    MAX_ENERGY = 100

    def __init__(self, name="Inhabitant", age=0, energy=MAX_ENERGY):
        self.name = name
        self.age = age
        self.energy = energy
   # @abstractmethod, all the classes must provide their own definition, to do it i need to import also abstractmethod on the top as library
    def grow(self):
        self.age += 1

    def eat(self, amount):
        self.energy += amount
        if self.energy > Inhabitant.MAX_ENERGY:
            self.energy = Inhabitant.MAX_ENERGY
    
    def move(self, distance):
        self.energy -= distance
        if self.energy < 0:
            self.energy = 0