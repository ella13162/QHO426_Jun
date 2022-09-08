from planet import Planet
from human import Human
from robot import Robot
import random
import matplotlib.pyplot as plt

class Universe:

    def __init__(self):
        self.planets = []

    def __str__(self):
        return f"This universe contains:\n {self.planets}"

    def __repr__(self):
        return f"Universe(planets={self.planets})"

    def generate(self):
        n_planet = Planet()
        hum_num = random.randint(1,8)
        rob_num = random.randint(1,8)

        for hum in range(hum_num):
            h = Human(f"Human {hum}")
            n_planet.add(h)

        for rob in range(rob_num):
            r = Robot(f"Robot {rob}")
            n_planet.add(r)

        self.planets.append(n_planet)

    # [p1, p2, p3, p4]
    def show_populations(self):
        num_planets = len(self.planets)

        fig = plt.figure()
        for i in range(num_planets):
          planet = self.planets[i]
          num_hum = 0
          num_rob = 0
          for dude in planet.inhabitants:
            if isinstance(dude, Human):
              num_hum += 1
            elif isinstance(dude, Robot):
              num_rob +=1
              
          ax = fig.add_subplot(num_planets,1, i+1)
          ax.bar(["Humans", "Robots"], [num_hum, num_rob])

        plt.tight_layout()
        plt.show()
            

if __name__ == "__main__":
    u = Universe()
    u.generate()
    u.generate()
    u.show_populations()
    print(u)



    