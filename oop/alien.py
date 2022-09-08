from inhabitant import Inhabitant

class Alien(Inhabitant):

  def __init__(self, name="E.T", age = 0):
    super().__init__(name, age)
    self.technology = []

  def __str__(self):
    return f"Alien {self.name} of age {self.age} has access to {self.technology}"

  def __repr__(self):
    return f"Alien(name = {self.name}, age = {self.age}, technology = {self.technology}")

  def pickup(self, tech):
    self.technology.append(tech)
    print(f"{self.name} picked up {tech}")

  def drop(self, tech):
    if tech in self.technology:
      self.technology.remove(tech)
      print(f"{self.name} dropped {tech}")

if __name__ == "__main__":
  a1 = Alien("Wall-E", 5)
  a2 = Alien()
  print(a1)
  print(a2)
  a1.pickup("Machine Gun")
  a1.pickup("Jetpack")
  a1.pickup("Torch")
  print(a1)
  a1.drop("Jetpack")
  print(a1)
