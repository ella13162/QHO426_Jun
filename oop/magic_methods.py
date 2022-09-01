from oop.human import Human
from oop.robot import Robot

class Planet:

  def __init__(self):
    self.humans = []
    self.robots = []

  def __repr__(self):
    return f"Planet (human = {self.humans}, robots = {self.robots})"

  def __str__(self):
    return f"Humans include: {self.humans}. Robots are {self.robots}"

  def add_human(self, h):
    self.humans.append(h)

  def remove_human(self, h):
    if h in self.human:
      self.humans.remove(h)

  def add_robots(self, rob):
    self.robots.append(rob)

  def remove_robots(self, rob):
    if rob in self.robots:
      self.robots.remove(rob)


if __name__ == "__main__":
  h1 = Human()
  h2 = Human()
  r1 = Robot()
  r2 = Robot()
  earth = Planet()
  earth.add_human(h2)
  earth.add_robots(r1)
  print(earth)
  earth.add_human(h1)
  earth.remove_robots(r1)
  print(earth)
  earth.add_robots(r2)
  print(earth)
