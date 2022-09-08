from human import Human
from robot import Robot

class Planet:

    def __init__(self):
        self.inhabitants = []

    def __repr__(self):
        return f"Planet(inhabitants = {self.inhabitants} )"

    def __str__(self):
        return f"Inhabitants are{self.inhabitants}"

    def add(self, i):
        self.inhabitants.append(i)

    def remove(self, i):
        if i in self.inhabitants:
            self.inhabitants.remove(i)

if __name__ == "__main__":
    h1 = Human()
    h2 = Human()
    r1 = Robot()
    r2 = Robot()
    earth = Planet()
    earth.add_human(h2)
    earth.add_robot(r1)
    print(earth)
    earth.add_human(h1)
    earth.remove_robot(r1)
    print(earth)
    earth.add_robot(r2)
    print(earth)